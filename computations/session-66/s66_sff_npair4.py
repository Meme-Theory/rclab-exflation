#!/usr/bin/env python3
"""
S66 SFF-NPAIR4-66: Spectral Form Factor for N_pair=4 Pairing Hamiltonian
=========================================================================

Gate: SFF-NPAIR4-66
  PASS (integrability): slope/GUE < 0.1
  FAIL (chaos): slope/GUE > 0.5
  INFO: 0.1 < slope/GUE < 0.5

Physics: At half-filling (N_pair=4, N_modes=8), the Hilbert space dimension
is C(8,4) = 70 -- the LARGEST for 8 modes. S65 found slope/GUE = 0.002
(genuine ramp region) at N_pair=3 (dim=56), firmly integrable. Does the
larger Hilbert space at half-filling produce a ramp?

Half-filling is special: particle-hole symmetry is exact, the Hilbert space
is maximally large, and the density of states is highest. If integrability
breaks anywhere, it is most likely here.

Method (following S65 exactly):
  1. Load eps_bare, V_bare from S64 data
  2. Build N_pair=4 Fock basis (dim = 70)
  3. Construct full pairing H and RG H
  4. Generate ensemble (sigma_lift perturbations, n=500)
  5. Unfold each spectrum (mean normalization, per S53)
  6. Compute ensemble-averaged SFF K(t)
  7. Extract ramp slope, compare to GUE
  8. Number variance Sigma^2(L) as independent check

Input: computations/session-64/s64_npair3_rg.npz (contains eps_bare, V_bare)
Output: computations/session-66/s66_sff_npair4.npz, s66_sff_npair4.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import numpy as np
from scipy.linalg import eigh
from itertools import combinations
from math import factorial, comb
from numpy.polynomial.polynomial import polyfit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# Section 1: Load Data and Set Parameters
# ============================================================================

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's64_npair3_rg.npz')
d = np.load(data_path, allow_pickle=True)

eps_bare = d['eps_bare']       # (8,) single-particle energies
V_bare = d['V_bare']           # (8,8) pairing interaction matrix
N_modes = len(eps_bare)        # 8
N_pair = 4  # HALF-FILLING (local)
sigma_lift = float(d['sigma_lift'])  # 0.001 degeneracy-lifting scale
n_ensemble = 500               # same as S65

dim_expected = comb(N_modes, N_pair)
print(f"N_modes = {N_modes}, N_pair = {N_pair}")
print(f"Fock dim = C({N_modes},{N_pair}) = {dim_expected}")
print(f"sigma_lift = {sigma_lift}")
print(f"n_ensemble = {n_ensemble}")
print()

# Load S65 N_pair=3 results for comparison
s65_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's65_sff_npair3.npz')
if os.path.exists(s65_path):
    s65 = np.load(s65_path, allow_pickle=True)
    s65_ratio_full_gue = float(s65['ratio_full_gue'])
    s65_r_full_mean = float(s65['r_full_mean'])
    s65_dim = int(s65['dim'])
    print(f"S65 baseline (N_pair=3, dim={s65_dim}):")
    print(f"  slope/GUE = {s65_ratio_full_gue:.4f}")
    print(f"  <r> = {s65_r_full_mean:.4f}")
    print()
else:
    s65_ratio_full_gue = None
    s65_r_full_mean = None
    s65_dim = None
    print("S65 data not found -- proceeding without baseline comparison")
    print()

# ============================================================================
# Section 2: Construct N_pair=4 Pairing Hamiltonian in Fock Space
# ============================================================================

def build_fock_basis(N_modes, N_pair):
    """Build all N_pair-subset configurations of N_modes levels.
    Each basis state |S> has S = frozenset of occupied pair-modes.
    Returns list of tuples (sorted mode indices).
    """
    return list(combinations(range(N_modes), N_pair))


def build_hamiltonian_full(eps, V, basis):
    """Build full pairing Hamiltonian with non-separable V_{kl}.

    H_full = sum_k eps_k n_k - sum_{k,l} V_{kl} P_k^+ P_l

    In the pair Fock basis:
      - Diagonal: sum_{k in state} (2*eps_k - V_{kk})
      - Off-diagonal (differ by one pair k<->l): -V_{kl}

    Matches S64 (s64_npair3_rg.py) construction EXACTLY.
    """
    dim = len(basis)
    H = np.zeros((dim, dim))

    for i, si in enumerate(basis):
        # Diagonal: kinetic + diagonal pairing
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        H[i, i] -= sum(V[k, k] for k in si)

        for j in range(i + 1, dim):
            sj = basis[j]
            si_set = set(si)
            sj_set = set(sj)
            diff_i = si_set - sj_set
            diff_j = sj_set - si_set
            if len(diff_i) == 1 and len(diff_j) == 1:
                k = diff_i.pop()
                l = diff_j.pop()
                H[i, j] = -V[k, l]
                H[j, i] = -V[l, k]

    return H


def build_hamiltonian_RG(eps, g, basis):
    """Build Richardson-Gaudin Hamiltonian with UNIFORM coupling g.

    H_RG = sum_k eps_k n_k - g sum_{k,l} P_k^+ P_l
    """
    dim = len(basis)
    H = np.zeros((dim, dim))

    for i, si in enumerate(basis):
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        H[i, i] -= g * len(si)  # diagonal pairing self-energy

        for j in range(i + 1, dim):
            sj = basis[j]
            si_set = set(si)
            sj_set = set(sj)
            diff_i = si_set - sj_set
            diff_j = sj_set - si_set
            if len(diff_i) == 1 and len(diff_j) == 1:
                H[i, j] = -g
                H[j, i] = -g

    return H


# Build basis
basis = build_fock_basis(N_modes, N_pair)
dim = len(basis)
assert dim == dim_expected, f"dim mismatch: {dim} != {dim_expected}"
print(f"Fock basis dimension: {dim}")

# Solve BCS gap equation at N_pair=4 for RG coupling
# From S64 methodology: g is chosen so that the ground state of the RG Hamiltonian
# has N_pair pairs. For N_pair=4 (half-filling), we use the same eps_bare
# and find g from the gap equation.
# For the RG model, the gap equation is: 1/g = sum_k 1/(2*E_k)
# where E_k = sqrt((eps_k - mu)^2 + Delta^2)
# At half-filling mu is near the center of the band.

# Method: scan g to find where ground state is in N=4 sector
# Since we directly diagonalize, we use the S64 approach: take g from N3
# and also compute the correct g for N4 from the gap equation.
# For simplicity and direct comparison, use the SAME V_bare and eps_bare.
# The RG coupling g for N=4 comes from the BCS gap equation at half-filling.

# Solve gap equation: 1/g = sum_k 1/(2*sqrt((eps_k - mu)^2 + Delta^2))
# Use Delta from the condensation energy scale
from scipy.optimize import brentq

def gap_eq_residual(g, eps, N_pair):
    """Solve for g given N_pair by finding self-consistent mu and Delta."""
    N = len(eps)
    # At T=0, the BCS gap equation:
    # 1/g = sum_k 1/(2*E_k), E_k = sqrt((eps_k - mu)^2 + Delta^2)
    # Number equation: sum_k (1 - (eps_k - mu)/E_k) / 2 = N_pair
    # For the RG model, we just need the coupling that gives the right filling.
    # Direct approach: diagonalize H_RG at this g and check ground state sector.
    # But this is expensive. Instead use the mean-field gap equation.

    # Actually, for the SFF comparison, what matters is:
    # 1. The FULL H (non-separable V) -- this is the physics
    # 2. The RG H (uniform g) -- this is the integrable reference
    # We need to pick g so RG is a fair comparison.
    # Use g = average of V_bare matrix elements (same as S64).
    pass

# Use the S64 approach: g = mean of V_bare off-diagonal
g_mean = np.mean(np.abs(V_bare))
# But S64 used a specific g from the N=3 gap equation. For N=4, we need the
# N=4 version. Let's just use the same g from N=3 -- the key question is
# whether the FULL H shows a ramp, and the RG reference provides the contrast.
g_N3 = float(d['N3_g'])
g_RG = g_N3  # Use same coupling for consistency with S65

print(f"RG coupling g = {g_RG:.6f} (from N=3 gap equation, same as S65)")
print()

# Build unperturbed Hamiltonians for verification
H0_full = build_hamiltonian_full(eps_bare, V_bare, basis)
evals_full_0 = np.sort(np.linalg.eigvalsh(H0_full))

H0_rg = build_hamiltonian_RG(eps_bare, g_RG, basis)
evals_rg_0 = np.sort(np.linalg.eigvalsh(H0_rg))

print(f"Full H eigenvalue range: [{evals_full_0[0]:.6f}, {evals_full_0[-1]:.6f}]")
print(f"RG H eigenvalue range:   [{evals_rg_0[0]:.6f}, {evals_rg_0[-1]:.6f}]")
print(f"Full H bandwidth: {evals_full_0[-1] - evals_full_0[0]:.6f}")
print(f"RG H bandwidth:   {evals_rg_0[-1] - evals_rg_0[0]:.6f}")

# SVD of V_bare for reference
U_svd, S_svd, Vt_svd = np.linalg.svd(V_bare)
print(f"V_bare SVD: s0={S_svd[0]:.4f}, s1={S_svd[1]:.4f}, rank-1 fraction = {S_svd[0]**2/np.sum(S_svd**2):.4f}")
print()

# Compute r-ratio for unperturbed spectrum
sp0 = np.diff(evals_full_0)
r0 = np.minimum(sp0[:-1], sp0[1:]) / np.maximum(sp0[:-1], sp0[1:])
r0[np.isnan(r0)] = 0
print(f"Unperturbed r-ratio (full): <r> = {np.mean(r0):.4f}")
sp0_rg = np.diff(evals_rg_0)
r0_rg = np.minimum(sp0_rg[:-1], sp0_rg[1:]) / np.maximum(sp0_rg[:-1], sp0_rg[1:])
r0_rg[np.isnan(r0_rg)] = 0
print(f"Unperturbed r-ratio (RG):   <r> = {np.mean(r0_rg):.4f}")
print()

# ============================================================================
# Section 3: Spectrum Unfolding
# ============================================================================

def unfold_spectrum_mean_normalization(evals):
    """Unfold by simple mean-spacing normalization (robust for small dim).

    Per S53 methodology note: polynomial unfolding with n<50 creates
    artifacts. Mean normalization is safer.
    """
    E_sorted = np.sort(evals)
    spacings = np.diff(E_sorted)
    mean_spacing = np.mean(spacings)
    if mean_spacing < 1e-15:
        return np.arange(len(E_sorted), dtype=float)
    xi = (E_sorted - E_sorted[0]) / mean_spacing
    return xi


# ============================================================================
# Section 4: Spectral Form Factor Computation
# ============================================================================

def compute_sff(evals_unfolded, t_values):
    """Compute K(t) = |Z(it)|^2 / D^2 where Z(it) = sum_n exp(i*xi_n*t)."""
    D = len(evals_unfolded)
    # Vectorized: phases is (D, n_t), sum over eigenvalues
    phases = np.exp(1j * np.outer(evals_unfolded, t_values))  # (D, n_t)
    Z = np.sum(phases, axis=0)  # (n_t,)
    K = np.abs(Z)**2 / D**2
    return K, Z / D


# ============================================================================
# Section 5: RMT Predictions
# ============================================================================

def sff_gue_prediction(t_values, D):
    """GUE SFF: ramp K = t/(2*pi*D^2), plateau K = 1/D."""
    t_H = 2 * np.pi * D
    K_gue = np.where(t_values < t_H,
                     t_values / (2 * np.pi * D**2),
                     1.0 / D)
    return K_gue, t_H


def sff_goe_prediction(t_values, D):
    """GOE SFF: ramp slope is 2x GUE."""
    t_H = 2 * np.pi * D
    K_goe = np.where(t_values < t_H,
                     2 * t_values / (2 * np.pi * D**2),
                     2.0 / D)
    return K_goe, t_H


def sff_poisson_prediction(D):
    """Poisson: K(t) = 1/D for all t > 0."""
    return 1.0 / D


# ============================================================================
# Section 6: Ensemble Generation and SFF Computation
# ============================================================================

print("="*70)
print(f"Generating ensemble (n={n_ensemble}) and computing SFF")
print("="*70)
print()

# Time grid
t_H_est = 2 * np.pi * dim  # ~439.8
t_min = 0.01  # (local)
t_max = 5 * t_H_est  # (local)
n_t = 2000  # (local)
t_values = np.geomspace(t_min, t_max, n_t)

# Linear grid for ramp slope extraction
t_lin = np.linspace(0.1, 2 * t_H_est, 4000)

print(f"Heisenberg time estimate: t_H = 2*pi*D = {t_H_est:.1f}")
print(f"Logarithmic grid: {n_t} points in [{t_min}, {t_max:.1f}]")
print(f"Linear grid: {len(t_lin)} points in [0.1, {2*t_H_est:.1f}]")
print()

# Storage
all_evals_full = np.zeros((n_ensemble, dim))
all_evals_rg = np.zeros((n_ensemble, dim))
all_evals_unf_full = np.zeros((n_ensemble, dim))
all_evals_unf_rg = np.zeros((n_ensemble, dim))

rng = np.random.default_rng(seed=66)

for i_ens in range(n_ensemble):
    # Perturb single-particle energies to break degeneracies
    eps_pert = eps_bare + rng.normal(0, sigma_lift, N_modes)

    # Full pairing Hamiltonian
    H_full = build_hamiltonian_full(eps_pert, V_bare, basis)
    evals_full_i = np.sort(np.linalg.eigvalsh(H_full))
    all_evals_full[i_ens] = evals_full_i

    # RG Hamiltonian (uniform g)
    H_rg = build_hamiltonian_RG(eps_pert, g_RG, basis)
    evals_rg_i = np.sort(np.linalg.eigvalsh(H_rg))
    all_evals_rg[i_ens] = evals_rg_i

    # Unfold both using mean normalization (per S53 methodology)
    all_evals_unf_full[i_ens] = unfold_spectrum_mean_normalization(evals_full_i)
    all_evals_unf_rg[i_ens] = unfold_spectrum_mean_normalization(evals_rg_i)

print(f"Ensemble generated: {n_ensemble} realizations")
print()

# ============================================================================
# Section 7: Compute Ensemble-Averaged SFF
# ============================================================================

print("Computing SFF on logarithmic grid...")

# SFF on log grid
K_full_log = np.zeros(n_t)
K_rg_log = np.zeros(n_t)
Z_full_avg_log = np.zeros(n_t, dtype=complex)
Z_rg_avg_log = np.zeros(n_t, dtype=complex)

for i_ens in range(n_ensemble):
    K_f, Z_f = compute_sff(all_evals_unf_full[i_ens], t_values)
    K_full_log += K_f
    Z_full_avg_log += Z_f

    K_r, Z_r = compute_sff(all_evals_unf_rg[i_ens], t_values)
    K_rg_log += K_r
    Z_rg_avg_log += Z_r

K_full_log /= n_ensemble
K_rg_log /= n_ensemble
Z_full_avg_log /= n_ensemble
Z_rg_avg_log /= n_ensemble

# Connected SFF: K_c = <|Z|^2/D^2> - |<Z/D>|^2
K_full_conn_log = K_full_log - np.abs(Z_full_avg_log)**2
K_rg_conn_log = K_rg_log - np.abs(Z_rg_avg_log)**2

print("Computing SFF on linear grid...")

# SFF on linear grid
K_full_lin = np.zeros(len(t_lin))
K_rg_lin = np.zeros(len(t_lin))
Z_full_avg_lin = np.zeros(len(t_lin), dtype=complex)
Z_rg_avg_lin = np.zeros(len(t_lin), dtype=complex)

for i_ens in range(n_ensemble):
    K_f, Z_f = compute_sff(all_evals_unf_full[i_ens], t_lin)
    K_full_lin += K_f
    Z_full_avg_lin += Z_f

    K_r, Z_r = compute_sff(all_evals_unf_rg[i_ens], t_lin)
    K_rg_lin += K_r
    Z_rg_avg_lin += Z_r

K_full_lin /= n_ensemble
K_rg_lin /= n_ensemble
Z_full_avg_lin /= n_ensemble
Z_rg_avg_lin /= n_ensemble

K_full_conn_lin = K_full_lin - np.abs(Z_full_avg_lin)**2
K_rg_conn_lin = K_rg_lin - np.abs(Z_rg_avg_lin)**2

print("SFF computation complete.")
print()

# ============================================================================
# Section 8: Ramp Detection and Slope Extraction
# ============================================================================

print("="*70)
print("Ramp Analysis")
print("="*70)
print()

# RMT predictions
K_gue_log, t_H_gue = sff_gue_prediction(t_values, dim)
K_goe_log, t_H_goe = sff_goe_prediction(t_values, dim)
K_poisson = sff_poisson_prediction(dim)

K_gue_lin, _ = sff_gue_prediction(t_lin, dim)
K_goe_lin, _ = sff_goe_prediction(t_lin, dim)

t_H = 2 * np.pi * dim
plateau_level = 1.0 / dim

print(f"Heisenberg time: t_H = {t_H:.2f}")
print(f"Plateau level: 1/D = {plateau_level:.6f}")
print()

# GUE/GOE ramp slopes
slope_gue = 1.0 / (2 * np.pi * dim**2)
slope_goe = 2.0 / (2 * np.pi * dim**2)

# --- Ramp slope extraction ---
# CRITICAL S65 LESSON: Use the GENUINE ramp region [0.3, 0.8]*t_H, not [0.05, 0.8].
# The early-time region (0.05-0.3)*t_H is contaminated by the dip-to-plateau transition.
# A genuine ramp has slope STABLE across sub-windows (variation < 2x).

# Primary: genuine ramp region [0.3, 0.8]*t_H (per S65 methodology)
t_ramp_lo_genuine = 0.3 * t_H
t_ramp_hi_genuine = 0.8 * t_H
mask_genuine = (t_lin >= t_ramp_lo_genuine) & (t_lin <= t_ramp_hi_genuine)

# Secondary: full region [0.05, 0.8]*t_H (for comparison)
t_ramp_lo_full = 0.05 * t_H
t_ramp_hi_full = 0.8 * t_H
mask_full_region = (t_lin >= t_ramp_lo_full) & (t_lin <= t_ramp_hi_full)

# Fit in genuine region
if np.sum(mask_genuine) > 10:
    coeffs_full_g = polyfit(t_lin[mask_genuine], K_full_conn_lin[mask_genuine], 1)
    slope_full_genuine = coeffs_full_g[1]
    intercept_full_genuine = coeffs_full_g[0]

    coeffs_rg_g = polyfit(t_lin[mask_genuine], K_rg_conn_lin[mask_genuine], 1)
    slope_rg_genuine = coeffs_rg_g[1]
    intercept_rg_genuine = coeffs_rg_g[0]

    ratio_full_genuine = slope_full_genuine / slope_gue
    ratio_rg_genuine = slope_rg_genuine / slope_gue

    # R^2 for linear fit
    K_pred_g = intercept_full_genuine + slope_full_genuine * t_lin[mask_genuine]
    SS_res_g = np.sum((K_full_conn_lin[mask_genuine] - K_pred_g)**2)
    SS_tot_g = np.sum((K_full_conn_lin[mask_genuine] - np.mean(K_full_conn_lin[mask_genuine]))**2)
    R2_full_genuine = 1 - SS_res_g / SS_tot_g if SS_tot_g > 0 else 0

    K_pred_rg_g = intercept_rg_genuine + slope_rg_genuine * t_lin[mask_genuine]
    SS_res_rg_g = np.sum((K_rg_conn_lin[mask_genuine] - K_pred_rg_g)**2)
    SS_tot_rg_g = np.sum((K_rg_conn_lin[mask_genuine] - np.mean(K_rg_conn_lin[mask_genuine]))**2)
    R2_rg_genuine = 1 - SS_res_rg_g / SS_tot_rg_g if SS_tot_rg_g > 0 else 0

    print(f"GENUINE ramp region [{0.3:.1f}, {0.8:.1f}]*t_H:")
    print(f"  {np.sum(mask_genuine)} points in fit region")
    print(f"  slope_GUE = {slope_gue:.6e}")
    print(f"  slope_GOE = {slope_goe:.6e}")
    print()
    print(f"  Full H: slope = {slope_full_genuine:.6e}, slope/GUE = {ratio_full_genuine:.4f}, R^2 = {R2_full_genuine:.4f}")
    print(f"  RG H:   slope = {slope_rg_genuine:.6e}, slope/GUE = {ratio_rg_genuine:.4f}, R^2 = {R2_rg_genuine:.4f}")
else:
    print("ERROR: insufficient points in genuine ramp region")
    slope_full_genuine = 0
    ratio_full_genuine = 0
    R2_full_genuine = 0
    slope_rg_genuine = 0
    ratio_rg_genuine = 0
    R2_rg_genuine = 0

print()

# Also fit in full ramp region for comparison with S65
if np.sum(mask_full_region) > 10:
    coeffs_full_f = polyfit(t_lin[mask_full_region], K_full_conn_lin[mask_full_region], 1)
    slope_full_nominal = coeffs_full_f[1]
    ratio_full_nominal = slope_full_nominal / slope_gue

    coeffs_rg_f = polyfit(t_lin[mask_full_region], K_rg_conn_lin[mask_full_region], 1)
    slope_rg_nominal = coeffs_rg_f[1]
    ratio_rg_nominal = slope_rg_nominal / slope_gue

    K_pred_f = coeffs_full_f[0] + slope_full_nominal * t_lin[mask_full_region]
    SS_res_f = np.sum((K_full_conn_lin[mask_full_region] - K_pred_f)**2)
    SS_tot_f = np.sum((K_full_conn_lin[mask_full_region] - np.mean(K_full_conn_lin[mask_full_region]))**2)
    R2_full_nominal = 1 - SS_res_f / SS_tot_f if SS_tot_f > 0 else 0

    print(f"NOMINAL (full) ramp region [{0.05:.2f}, {0.8:.1f}]*t_H:")
    print(f"  Full H: slope/GUE = {ratio_full_nominal:.4f}, R^2 = {R2_full_nominal:.4f}")
    print(f"  RG H:   slope/GUE = {ratio_rg_nominal:.4f}")
else:
    slope_full_nominal = 0
    ratio_full_nominal = 0
    R2_full_nominal = 0
    slope_rg_nominal = 0
    ratio_rg_nominal = 0

print()

# --- Ramp robustness: fit in multiple sub-windows ---
print("Ramp robustness analysis (full H, connected SFF):")
windows = [(0.05, 0.3), (0.1, 0.5), (0.2, 0.6), (0.3, 0.8), (0.5, 0.9), (0.05, 0.8)]
slopes_windows = []
for lo_frac, hi_frac in windows:
    t_lo = lo_frac * t_H
    t_hi = hi_frac * t_H
    m = (t_lin >= t_lo) & (t_lin <= t_hi)
    if np.sum(m) > 5:
        c = polyfit(t_lin[m], K_full_conn_lin[m], 1)
        s = c[1]
        r = s / slope_gue
        slopes_windows.append(r)
        print(f"  [{lo_frac:.2f}, {hi_frac:.2f}]*t_H: slope/GUE = {r:.4f}")
    else:
        slopes_windows.append(0)
        print(f"  [{lo_frac:.2f}, {hi_frac:.2f}]*t_H: insufficient data")

slope_mean = np.mean(slopes_windows)
slope_std = np.std(slopes_windows)
slope_max = np.max(slopes_windows)
slope_min = np.min(slopes_windows)
slope_variation = slope_max / max(abs(slope_min), 1e-10) if slope_min != 0 else float('inf')
print(f"  Mean slope/GUE = {slope_mean:.4f} +/- {slope_std:.4f}")
print(f"  Variation (max/min): {slope_variation:.1f}x")
print(f"  Genuine ramp criterion: variation < 2x = {'PASS' if slope_variation < 2 else 'FAIL'}")
print()

# --- Dip time extraction ---
idx_after_init = t_values > 1.0
if np.any(idx_after_init):
    K_sub = K_full_log[idx_after_init]
    t_sub = t_values[idx_after_init]
    idx_dip = np.argmin(K_sub)
    t_dip_full = t_sub[idx_dip]
    K_dip_full = K_sub[idx_dip]
    print(f"Dip time (full H): t_dip = {t_dip_full:.2f}")
    print(f"Dip level (full H): K_dip = {K_dip_full:.6f}")
    print(f"Dip / plateau ratio: {K_dip_full / plateau_level:.4f}")
else:
    t_dip_full = 0
    K_dip_full = 0
print()

# --- Fraction of connected SFF > 0 in ramp region ---
ramp_mask = (t_lin > 0.1 * t_H) & (t_lin < 0.9 * t_H)
frac_positive_full = np.mean(K_full_conn_lin[ramp_mask] > 0) if np.any(ramp_mask) else 0
frac_positive_rg = np.mean(K_rg_conn_lin[ramp_mask] > 0) if np.any(ramp_mask) else 0
print(f"Fraction of connected SFF > 0 in ramp region:")
print(f"  Full H: {frac_positive_full:.4f}")
print(f"  RG H:   {frac_positive_rg:.4f}")
print()

# ============================================================================
# Section 9: Number Variance Sigma^2(L)
# ============================================================================

print("="*70)
print("Number Variance Sigma^2(L)")
print("="*70)
print()

L_values = np.linspace(0.5, dim/3, 50)
sigma2_full = np.zeros(len(L_values))
sigma2_rg = np.zeros(len(L_values))

for i_ens in range(n_ensemble):
    xi_full = all_evals_unf_full[i_ens]
    xi_rg = all_evals_unf_rg[i_ens]

    for iL, L in enumerate(L_values):
        counts_full = []
        counts_rg = []
        n_windows = max(1, int((xi_full[-1] - xi_full[0]) / L * 2))
        for w in range(n_windows):
            center = xi_full[0] + (xi_full[-1] - xi_full[0]) * (w + 0.5) / n_windows
            n_in_full = np.sum((xi_full >= center - L/2) & (xi_full < center + L/2))
            n_in_rg = np.sum((xi_rg >= center - L/2) & (xi_rg < center + L/2))
            counts_full.append(n_in_full)
            counts_rg.append(n_in_rg)

        sigma2_full[iL] += np.var(counts_full)
        sigma2_rg[iL] += np.var(counts_rg)

sigma2_full /= n_ensemble
sigma2_rg /= n_ensemble

# RMT predictions
sigma2_poisson = L_values
sigma2_gue = (2.0 / np.pi**2) * (np.log(2 * np.pi * L_values) + 1 + np.euler_gamma - np.pi**2/8)
sigma2_gue = np.maximum(sigma2_gue, 0)

sigma2_at_5_full = np.interp(5, L_values, sigma2_full)
sigma2_at_5_rg = np.interp(5, L_values, sigma2_rg)
sigma2_at_5_gue = np.interp(5, L_values, sigma2_gue)

print(f"Number variance at L=5:")
print(f"  Full H:  Sigma^2 = {sigma2_at_5_full:.4f}")
print(f"  RG H:    Sigma^2 = {sigma2_at_5_rg:.4f}")
print(f"  Poisson: {5.0:.4f}")
print(f"  GUE:     {sigma2_at_5_gue:.4f}")
print(f"  Full/Poisson ratio: {sigma2_at_5_full / 5.0:.3f}")
print(f"  Full/GUE ratio:     {sigma2_at_5_full / sigma2_at_5_gue:.3f}")
print()

# ============================================================================
# Section 10: Ensemble r-ratio
# ============================================================================

print("="*70)
print("Ensemble r-ratio")
print("="*70)
print()

r_full_ens = []
r_rg_ens = []
for i_ens in range(n_ensemble):
    sp_full = np.diff(np.sort(all_evals_full[i_ens]))
    sp_rg = np.diff(np.sort(all_evals_rg[i_ens]))

    # Avoid division by zero
    sp_full = np.maximum(sp_full, 1e-15)
    sp_rg = np.maximum(sp_rg, 1e-15)

    ratios_full = np.minimum(sp_full[:-1], sp_full[1:]) / np.maximum(sp_full[:-1], sp_full[1:])
    ratios_rg = np.minimum(sp_rg[:-1], sp_rg[1:]) / np.maximum(sp_rg[:-1], sp_rg[1:])

    r_full_ens.append(np.mean(ratios_full))
    r_rg_ens.append(np.mean(ratios_rg))

r_full_mean = np.mean(r_full_ens)
r_full_err = np.std(r_full_ens) / np.sqrt(n_ensemble)
r_rg_mean = np.mean(r_rg_ens)
r_rg_err = np.std(r_rg_ens) / np.sqrt(n_ensemble)

print(f"Full H: <r> = {r_full_mean:.4f} +/- {r_full_err:.4f}")
print(f"RG H:   <r> = {r_rg_mean:.4f} +/- {r_rg_err:.4f}")
print(f"Poisson: 0.386, GOE: 0.531, GUE: 0.603")
if s65_r_full_mean is not None:
    print(f"S65 N_pair=3: <r> = {s65_r_full_mean:.4f}")
    print(f"Change N3->N4: delta_r = {r_full_mean - s65_r_full_mean:+.4f}")
print()

# ============================================================================
# Section 11: Gate Verdict
# ============================================================================

print("="*70)
print("GATE VERDICT: SFF-NPAIR4-66")
print("="*70)
print()

# Use the GENUINE ramp slope (per S65 lesson: early-time contamination inflates nominal)
decisive_ratio = ratio_full_genuine

if decisive_ratio < 0.1:
    verdict = "PASS"
    reason = f"No ramp: slope/GUE = {decisive_ratio:.4f} < 0.1 (INTEGRABLE)"
elif decisive_ratio > 0.5:
    verdict = "FAIL"
    reason = f"Ramp detected: slope/GUE = {decisive_ratio:.4f} > 0.5 (CHAOTIC)"
else:
    verdict = "INFO"
    reason = f"Intermediate: slope/GUE = {decisive_ratio:.4f} in [0.1, 0.5]"

print(f"  Threshold: PASS < 0.1, FAIL > 0.5")
print(f"  Computed:  slope/GUE (genuine region) = {decisive_ratio:.4f}")
print(f"  R^2 of linear fit: {R2_full_genuine:.4f}")
print(f"  Verdict:   {verdict} -- {reason}")
print()
print(f"  Additional context:")
print(f"    slope/GUE (nominal) = {ratio_full_nominal:.4f}")
print(f"    slope/GUE (RG, genuine) = {ratio_rg_genuine:.4f}")
print(f"    <r>_full = {r_full_mean:.4f}, <r>_RG = {r_rg_mean:.4f}")
print(f"    Sigma^2(5) = {sigma2_at_5_full:.4f} (Poisson: 5, GUE: {sigma2_at_5_gue:.4f})")
print(f"    Frac K_c > 0 in ramp: {frac_positive_full:.4f}")
print(f"    Window variation: {slope_variation:.1f}x (< 2 = genuine ramp)")
if s65_ratio_full_gue is not None:
    print(f"    S65 N_pair=3 slope/GUE (nominal): {s65_ratio_full_gue:.4f}")
    print(f"    N3->N4 change: {decisive_ratio - s65_ratio_full_gue:+.4f}")
print()

# ============================================================================
# Section 12: Save Data
# ============================================================================

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's66_sff_npair4.npz')

np.savez(out_path,
         # Gate
         gate_name='SFF-NPAIR4-66',
         gate_verdict=verdict,
         gate_reason=reason,

         # Parameters
         N_modes=N_modes,
         N_pair=N_pair,
         dim=dim,
         n_ensemble=n_ensemble,
         sigma_lift=sigma_lift,
         eps_bare=eps_bare,
         V_bare=V_bare,
         g_RG=g_RG,

         # Time grids
         t_log=t_values,
         t_lin=t_lin,
         t_H=t_H,

         # SFF (log grid)
         K_full_log=K_full_log,
         K_rg_log=K_rg_log,
         K_full_conn_log=K_full_conn_log,
         K_rg_conn_log=K_rg_conn_log,

         # SFF (linear grid)
         K_full_lin=K_full_lin,
         K_rg_lin=K_rg_lin,
         K_full_conn_lin=K_full_conn_lin,
         K_rg_conn_lin=K_rg_conn_lin,

         # RMT predictions
         K_gue_log=K_gue_log,
         K_goe_log=K_goe_log,
         K_poisson=K_poisson,

         # Slopes -- genuine ramp region
         slope_full_genuine=slope_full_genuine,
         slope_rg_genuine=slope_rg_genuine,
         ratio_full_genuine=ratio_full_genuine,
         ratio_rg_genuine=ratio_rg_genuine,
         R2_full_genuine=R2_full_genuine,
         R2_rg_genuine=R2_rg_genuine,

         # Slopes -- nominal (full) ramp region
         slope_full_nominal=slope_full_nominal,
         ratio_full_nominal=ratio_full_nominal,
         R2_full_nominal=R2_full_nominal,

         # RMT slopes
         slope_gue=slope_gue,
         slope_goe=slope_goe,

         # Dip
         t_dip_full=t_dip_full,
         K_dip_full=K_dip_full,

         # Number variance
         L_values=L_values,
         sigma2_full=sigma2_full,
         sigma2_rg=sigma2_rg,
         sigma2_poisson=sigma2_poisson,
         sigma2_gue=sigma2_gue,
         sigma2_at_5_full=sigma2_at_5_full,

         # r-ratio
         r_full_mean=r_full_mean,
         r_full_err=r_full_err,
         r_rg_mean=r_rg_mean,
         r_rg_err=r_rg_err,

         # Robustness
         frac_positive_full=frac_positive_full,
         frac_positive_rg=frac_positive_rg,
         slope_windows=np.array(slopes_windows),
         slope_mean=slope_mean,
         slope_std=slope_std,
         slope_variation=slope_variation,

         # Unperturbed spectra
         evals_full_0=evals_full_0,
         evals_rg_0=evals_rg_0,
         )

print(f"Data saved to: {out_path}")
print()

# ============================================================================
# Section 13: Plot
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# --- Panel (a): Total SFF on log-log scale ---
ax = axes[0, 0]
ax.loglog(t_values, K_full_log, 'b-', lw=1.0, alpha=0.8, label='Full H (data)')
ax.loglog(t_values, K_rg_log, 'r-', lw=1.0, alpha=0.6, label='RG H (data)')
ax.loglog(t_values, K_gue_log, 'k--', lw=1.0, alpha=0.5, label='GUE')
ax.loglog(t_values, K_goe_log, 'k:', lw=1.0, alpha=0.5, label='GOE')
ax.axhline(K_poisson, color='gray', ls='-.', lw=0.8, alpha=0.5, label=f'Poisson = 1/D')
ax.axvline(t_H, color='green', ls='--', lw=0.8, alpha=0.5, label=f'$t_H = {t_H:.0f}$')
ax.set_xlabel('t (unfolded units)')
ax.set_ylabel('K(t)')
ax.set_title('(a) Spectral Form Factor (total)')
ax.legend(fontsize=7, loc='lower right')
ax.set_xlim(t_min, t_max)

# --- Panel (b): Connected SFF on log-log ---
ax = axes[0, 1]
K_fc_pos = np.where(K_full_conn_log > 0, K_full_conn_log, np.nan)
K_fc_neg = np.where(K_full_conn_log < 0, -K_full_conn_log, np.nan)
ax.loglog(t_values, K_fc_pos, 'b-', lw=1.0, alpha=0.8, label='Full H ($K_c > 0$)')
ax.loglog(t_values, K_fc_neg, 'b--', lw=0.7, alpha=0.5, label='Full H ($|K_c| < 0$)')

K_rc_pos = np.where(K_rg_conn_log > 0, K_rg_conn_log, np.nan)
K_rc_neg = np.where(K_rg_conn_log < 0, -K_rg_conn_log, np.nan)
ax.loglog(t_values, K_rc_pos, 'r-', lw=1.0, alpha=0.6, label='RG H ($K_c > 0$)')
ax.loglog(t_values, K_rc_neg, 'r--', lw=0.7, alpha=0.4, label='RG H ($|K_c| < 0$)')

K_gue_conn = np.where(t_values < t_H, t_values / (2 * np.pi * dim**2), 0)
ax.loglog(t_values[t_values < t_H], K_gue_conn[t_values < t_H], 'k--', lw=1.0, alpha=0.5, label='GUE ramp')
ax.axvline(t_H, color='green', ls='--', lw=0.8, alpha=0.5)
ax.set_xlabel('t (unfolded units)')
ax.set_ylabel('$K_c(t)$')
ax.set_title('(b) Connected SFF')
ax.legend(fontsize=7, loc='lower right')

# --- Panel (c): Linear-scale SFF in ramp region ---
ax = axes[0, 2]
ax.plot(t_lin / t_H, K_full_conn_lin, 'b-', lw=0.8, alpha=0.8, label='Full H $K_c$')
ax.plot(t_lin / t_H, K_rg_conn_lin, 'r-', lw=0.8, alpha=0.6, label='RG H $K_c$')
t_lin_norm = t_lin / t_H
gue_ramp_lin = np.where(t_lin_norm < 1, slope_gue * t_lin, 0)
goe_ramp_lin = np.where(t_lin_norm < 1, slope_goe * t_lin, 0)
ax.plot(t_lin / t_H, gue_ramp_lin, 'k--', lw=1.0, alpha=0.5, label='GUE')
ax.plot(t_lin / t_H, goe_ramp_lin, 'k:', lw=1.0, alpha=0.5, label='GOE')
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(1.0, color='green', ls='--', lw=0.8, alpha=0.5, label='$t_H$')
# Mark genuine ramp region
ax.axvspan(0.3, 0.8, alpha=0.1, color='blue', label='genuine ramp')
ax.set_xlabel('$t / t_H$')
ax.set_ylabel('$K_c(t)$')
ax.set_title(f'(c) Connected SFF | slope/GUE = {ratio_full_genuine:.4f} (genuine)')
ax.legend(fontsize=7)
ax.set_xlim(0, 2)

# --- Panel (d): Number variance ---
ax = axes[1, 0]
ax.plot(L_values, sigma2_full, 'b-', lw=1.5, label='Full H')
ax.plot(L_values, sigma2_rg, 'r-', lw=1.5, label='RG H')
ax.plot(L_values, sigma2_poisson, 'k--', lw=1.0, alpha=0.5, label='Poisson ($\\Sigma^2 = L$)')
ax.plot(L_values, sigma2_gue, 'k:', lw=1.0, alpha=0.5, label='GUE')
ax.set_xlabel('L (mean spacings)')
ax.set_ylabel('$\\Sigma^2(L)$')
ax.set_title(f'(d) Number Variance | $\\Sigma^2(5)$ = {sigma2_at_5_full:.2f}')
ax.legend(fontsize=8)

# --- Panel (e): r-ratio histogram ---
ax = axes[1, 1]
bins = np.linspace(0, 1, 30)
ax.hist(r_full_ens, bins=bins, density=True, alpha=0.6, color='blue', label=f'Full H: <r>={r_full_mean:.3f}')
ax.hist(r_rg_ens, bins=bins, density=True, alpha=0.4, color='red', label=f'RG H: <r>={r_rg_mean:.3f}')
ax.axvline(0.386, color='gray', ls='--', lw=1, label='Poisson (0.386)')
ax.axvline(0.531, color='green', ls='--', lw=1, label='GOE (0.531)')
ax.axvline(0.603, color='purple', ls='--', lw=1, label='GUE (0.603)')
ax.set_xlabel('<r>')
ax.set_ylabel('Density')
ax.set_title('(e) Ensemble r-ratio Distribution')
ax.legend(fontsize=7)

# --- Panel (f): Verdict summary ---
ax = axes[1, 2]
ax.axis('off')
summary_text = f"""SFF-NPAIR4-66 Gate Verdict: {verdict}

Parameters:
  N_modes = {N_modes}, N_pair = {N_pair}, dim = {dim}
  n_ensemble = {n_ensemble}, sigma_lift = {sigma_lift}

SFF Ramp Analysis (genuine region [0.3, 0.8]*t_H):
  slope/GUE (full H) = {ratio_full_genuine:.4f}
  slope/GUE (RG H)   = {ratio_rg_genuine:.4f}
  R^2 linear fit (full) = {R2_full_genuine:.4f}

  Nominal slope/GUE [0.05, 0.8]*t_H = {ratio_full_nominal:.4f}
  Mean slope/GUE (windows) = {slope_mean:.4f} +/- {slope_std:.4f}
  Frac. K_c > 0 in ramp = {frac_positive_full:.4f}
  Window variation: {slope_variation:.1f}x

Dip: t_dip = {t_dip_full:.1f}, K_dip/plateau = {K_dip_full/plateau_level:.3f}

Number variance: Sigma^2(5) = {sigma2_at_5_full:.2f}
  (Poisson: 5, GUE: {sigma2_at_5_gue:.2f})

r-ratio:
  Full H: <r> = {r_full_mean:.4f} +/- {r_full_err:.4f}
  RG H:   <r> = {r_rg_mean:.4f} +/- {r_rg_err:.4f}"""

if s65_r_full_mean is not None:
    summary_text += f"""

S65 comparison (N_pair=3, dim={s65_dim}):
  slope/GUE = {s65_ratio_full_gue:.4f}, <r> = {s65_r_full_mean:.4f}"""

summary_text += f"""

Threshold: PASS < 0.1, FAIL > 0.5
Reason: {reason}"""

ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=7.5,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle(f'S66 SFF-NPAIR4: Spectral Form Factor at Half-Filling (N_pair=4, dim={dim})',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's66_sff_npair4.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")
print()
print("DONE.")
