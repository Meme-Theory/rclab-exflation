#!/usr/bin/env python3
"""
S65 SFF-NPAIR3-65: Spectral Form Factor for N_pair=3 Pairing-Only Hamiltonian
==============================================================================

Gate: SFF-NPAIR3-65
  PASS: slope/GUE > 0.3
  FAIL: slope/GUE < 0.1
  INFO: 0.1 < slope/GUE < 0.3

Physics: The spectral form factor K(t) = <|Z(it)|^2> / <|Z(0)|^2> is the
Fourier transform of the two-point spectral correlation function. For chaotic
systems (GOE/GUE), K(t) exhibits:
  - Dip: initial decay from disconnected part
  - Ramp: linear rise K(t) ~ t/t_H (GOE: slope = 2/(2*pi*t_H), GUE: 1/(2*pi*t_H))
  - Plateau: saturation at K = 1/D (Hilbert space dimension D)

For integrable systems (Poisson), K(t) = 1/D for all t (no ramp).

The ramp is the CLEANEST diagnostic of spectral rigidity. At dim=56, r-ratio
has large finite-size fluctuations. The SFF ramp, when disorder-averaged, can
be detected even at small dimensions.

Method:
  1. Reconstruct N_pair=3 pairing Hamiltonian from S64 parameters
  2. Generate ensemble via sigma_lift perturbations (break degeneracies)
  3. Unfold each spectrum (cumulative spectral density -> unit mean spacing)
  4. Compute SFF K(t) = <|sum_n exp(i*E_n*t)|^2> / D^2, averaged over ensemble
  5. Compare ramp slope to GUE prediction

Input: computations/session-64/s64_npair3_rg.npz
Output: computations/session-65/s65_sff_npair3.npz, s65_sff_npair3.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import numpy as np
from scipy.linalg import eigh
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# Section 1: Load S64 Data
# ============================================================================

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's64_npair3_rg.npz')
d = np.load(data_path, allow_pickle=True)

eps_bare = d['eps_bare']       # (8,) single-particle energies
V_bare = d['V_bare']           # (8,8) pairing interaction matrix
N_modes = len(eps_bare)        # 8
N_pair = 3  # number of pairs (local)
sigma_lift = float(d['sigma_lift'])  # 0.001 degeneracy-lifting scale
n_ensemble = 500               # increase from S64's 100 for SFF averaging

# Reference eigenvalues from S64
evals_full_s64 = d['N3_evals_full']
r_full_s64 = float(d['N3_r_mean_full'])

print(f"N_modes = {N_modes}, N_pair = {N_pair}")
from math import factorial, comb
print(f"Fock dim = C({N_modes},{N_pair}) = {comb(N_modes, N_pair)}")
print(f"S64 <r>_full = {r_full_s64:.4f}")
print(f"sigma_lift = {sigma_lift}")
print(f"n_ensemble = {n_ensemble}")
print()

# ============================================================================
# Section 2: Construct N_pair=3 Pairing Hamiltonian in Fock Space
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

    Matches S64 construction.
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


# Build basis and Hamiltonian
basis = build_fock_basis(N_modes, N_pair)
dim = len(basis)
print(f"Fock basis dimension: {dim}")

# Verify with unperturbed Hamiltonian (full V)
H0_full = build_hamiltonian_full(eps_bare, V_bare, basis)
evals_check = np.sort(np.linalg.eigvalsh(H0_full))
print(f"Eigenvalue range: [{evals_check[0]:.6f}, {evals_check[-1]:.6f}]")
print(f"S64 range:        [{evals_full_s64.min():.6f}, {evals_full_s64.max():.6f}]")

# Check agreement with S64
max_diff = np.max(np.abs(np.sort(evals_check) - np.sort(evals_full_s64)))
print(f"Max |evals - evals_s64| = {max_diff:.2e}")
assert max_diff < 1e-8, f"Eigenvalue reconstruction failed: max_diff = {max_diff}"
print("Hamiltonian reconstruction: VERIFIED (matches S64 to machine epsilon)")

# Also verify RG Hamiltonian
g_N3 = float(d['N3_g'])
mu_N3 = float(d['N3_mu'])
H0_rg = build_hamiltonian_RG(eps_bare, g_N3, basis)
evals_rg_check = np.sort(np.linalg.eigvalsh(H0_rg))
evals_rg_s64 = np.sort(d['N3_evals_RG'])
max_diff_rg = np.max(np.abs(evals_rg_check - evals_rg_s64))
print(f"RG max diff: {max_diff_rg:.2e}")
assert max_diff_rg < 1e-8, f"RG reconstruction failed: max_diff = {max_diff_rg}"
print("RG Hamiltonian reconstruction: VERIFIED")
print()

# ============================================================================
# Section 3: Spectrum Unfolding
# ============================================================================

def unfold_spectrum(evals):
    """Unfold spectrum to unit mean spacing using cumulative staircase.

    Maps E_n -> xi_n where xi has mean spacing 1.
    Uses a smooth polynomial fit to the integrated density of states.

    For dim=56, a low-order polynomial (degree 3-5) captures the smooth
    part without overfitting to fluctuations.
    """
    E_sorted = np.sort(evals)
    n = np.arange(1, len(E_sorted) + 1)  # staircase N(E)

    # Fit polynomial to N(E) vs E (degree 3 for dim=56)
    # Use degree = min(3, dim//10) to avoid overfitting
    deg = min(3, max(1, len(E_sorted) // 15))
    coeffs = np.polyfit(E_sorted, n, deg)
    N_smooth = np.polyval(coeffs, E_sorted)

    # Unfolded spectrum: xi_n = N_smooth(E_n)
    xi = N_smooth

    # Normalize to unit mean spacing
    xi = (xi - xi[0]) / (xi[-1] - xi[0]) * (len(xi) - 1)

    return xi


def unfold_spectrum_mean_normalization(evals):
    """Unfold by simple mean-spacing normalization (robust for small dim).

    Per S53 methodology note: polynomial unfolding with n<50 creates
    artifacts. Mean normalization is safer.
    """
    E_sorted = np.sort(evals)
    spacings = np.diff(E_sorted)
    mean_spacing = np.mean(spacings)
    xi = (E_sorted - E_sorted[0]) / mean_spacing
    return xi


# ============================================================================
# Section 4: Spectral Form Factor Computation
# ============================================================================

def compute_sff(evals_unfolded, t_values):
    """Compute the spectral form factor K(t) for unfolded eigenvalues.

    K(t) = |Z(it)|^2 / D^2
    where Z(it) = sum_n exp(i * xi_n * t)
    and D = number of eigenvalues.

    At beta=0 (infinite temperature):
    K(t) = (1/D^2) * |sum_n exp(i * xi_n * t)|^2
    """
    D = len(evals_unfolded)
    K = np.zeros(len(t_values))

    for it, t in enumerate(t_values):
        Z = np.sum(np.exp(1j * evals_unfolded * t))
        K[it] = np.abs(Z)**2 / D**2

    return K


def compute_connected_sff(evals_unfolded, t_values):
    """Compute the connected SFF: K_c(t) = K(t) - |<Z>/<|Z|>|^2

    For a single realization, the connected SFF is:
    K_c(t) = K(t) - 1

    But with ensemble averaging, the disconnected part is
    K_disc(t) = |<Z(t)>|^2 / <|Z(0)|>^2

    So K_c(t) = <K(t)> - K_disc(t)
    """
    D = len(evals_unfolded)
    Z = np.array([np.sum(np.exp(1j * evals_unfolded * t)) for t in t_values])
    K = np.abs(Z)**2 / D**2
    return K, Z / D


# ============================================================================
# Section 5: RMT Predictions
# ============================================================================

def sff_gue_prediction(t_values, D):
    """GUE spectral form factor prediction.

    For unfolded spectrum with mean spacing 1:
    - t_H = 2*pi*D (Heisenberg time)
    - Ramp: K(t) = t / (2*pi*D) for t < t_H
    - Plateau: K(t) = 1/D for t > t_H (here normalized as 1 since K already /D^2)

    Actually, for the normalized K(t) = |Z|^2/D^2:
    - Plateau: K(t) -> 1/D
    - Ramp: K(t) = t / t_H * (1/D) = t/(2*pi*D^2)
    """
    t_H = 2 * np.pi * D  # Heisenberg time in unfolded units
    K_gue = np.where(t_values < t_H,
                     t_values / (2 * np.pi * D**2),  # ramp
                     1.0 / D)                          # plateau
    return K_gue, t_H


def sff_goe_prediction(t_values, D):
    """GOE spectral form factor prediction.

    GOE ramp slope is 2x GUE:
    - Ramp: K(t) = 2*t / t_H * (1/D) = 2*t/(2*pi*D^2)
    - Plateau: K(t) -> 2/D (from time-reversal doubling)

    More precisely for GOE:
    K_GOE(t) = 2*t/t_H - t/t_H * log(1 + 2t/t_H)  for t < t_H
    but for t << t_H, this simplifies to K ~ 2*t/t_H
    """
    t_H = 2 * np.pi * D
    K_goe = np.where(t_values < t_H,
                     2 * t_values / (2 * np.pi * D**2),
                     2.0 / D)
    return K_goe, t_H


def sff_poisson_prediction(D):
    """Poisson (integrable) SFF prediction.

    For uncorrelated eigenvalues, K(t) = 1/D for all t > 0.
    (No ramp, immediate plateau.)
    """
    return 1.0 / D


# ============================================================================
# Section 6: Ensemble Generation and SFF Computation
# ============================================================================

print("="*70)
print("Generating ensemble and computing SFF")
print("="*70)
print()

# Time grid: logarithmic from t=0.01 to t=10*t_H
t_H_est = 2 * np.pi * dim  # ~351.9
t_min = 0.01  # (local)
t_max = 5 * t_H_est  # (local)
n_t = 2000  # (local)
t_values = np.geomspace(t_min, t_max, n_t)

# Also a linear grid for fine structure near the ramp
t_lin = np.linspace(0.1, 2 * t_H_est, 4000)

print(f"Heisenberg time estimate: t_H = 2*pi*D = {t_H_est:.1f}")
print(f"Time range: [{t_min}, {t_max:.1f}]")
print(f"Logarithmic grid: {n_t} points")
print(f"Linear grid: {len(t_lin)} points")
print()

# Storage for ensemble
all_evals_full = np.zeros((n_ensemble, dim))
all_evals_rg = np.zeros((n_ensemble, dim))
all_evals_unf_full = np.zeros((n_ensemble, dim))
all_evals_unf_rg = np.zeros((n_ensemble, dim))

# RG Hamiltonian uses uniform coupling g from S64 gap equation
print(f"RG coupling g = {g_N3:.6f}")
# SVD for reference
U_svd, S_svd, Vt_svd = np.linalg.svd(V_bare)
print(f"V_bare SVD: s0={S_svd[0]:.4f}, s1={S_svd[1]:.4f}, rank-1 fraction = {S_svd[0]**2/np.sum(S_svd**2):.4f}")

rng = np.random.default_rng(seed=65)

for i_ens in range(n_ensemble):
    # Perturb single-particle energies to break degeneracies
    eps_pert = eps_bare + rng.normal(0, sigma_lift, N_modes)

    # Full pairing Hamiltonian
    H_full = build_hamiltonian_full(eps_pert, V_bare, basis)
    evals_full_i = np.sort(np.linalg.eigvalsh(H_full))
    all_evals_full[i_ens] = evals_full_i

    # RG Hamiltonian (uniform g)
    H_rg = build_hamiltonian_RG(eps_pert, g_N3, basis)
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

# Full Hamiltonian SFF (log grid)
K_full_log = np.zeros(n_t)
K_rg_log = np.zeros(n_t)
Z_full_avg_log = np.zeros(n_t, dtype=complex)
Z_rg_avg_log = np.zeros(n_t, dtype=complex)

for i_ens in range(n_ensemble):
    # Full
    Z_full = np.array([np.sum(np.exp(1j * all_evals_unf_full[i_ens] * t))
                        for t in t_values])
    K_full_log += np.abs(Z_full)**2 / dim**2
    Z_full_avg_log += Z_full / dim

    # RG
    Z_rg = np.array([np.sum(np.exp(1j * all_evals_unf_rg[i_ens] * t))
                      for t in t_values])
    K_rg_log += np.abs(Z_rg)**2 / dim**2
    Z_rg_avg_log += Z_rg / dim

K_full_log /= n_ensemble
K_rg_log /= n_ensemble
Z_full_avg_log /= n_ensemble
Z_rg_avg_log /= n_ensemble

# Connected SFF
K_full_conn_log = K_full_log - np.abs(Z_full_avg_log)**2
K_rg_conn_log = K_rg_log - np.abs(Z_rg_avg_log)**2

print("Computing SFF on linear grid...")

# Linear grid for slope extraction
K_full_lin = np.zeros(len(t_lin))
K_rg_lin = np.zeros(len(t_lin))
Z_full_avg_lin = np.zeros(len(t_lin), dtype=complex)
Z_rg_avg_lin = np.zeros(len(t_lin), dtype=complex)

for i_ens in range(n_ensemble):
    Z_full = np.array([np.sum(np.exp(1j * all_evals_unf_full[i_ens] * t))
                        for t in t_lin])
    K_full_lin += np.abs(Z_full)**2 / dim**2
    Z_full_avg_lin += Z_full / dim

    Z_rg = np.array([np.sum(np.exp(1j * all_evals_unf_rg[i_ens] * t))
                      for t in t_lin])
    K_rg_lin += np.abs(Z_rg)**2 / dim**2
    Z_rg_avg_lin += Z_rg / dim

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

# -- Ramp slope extraction --
# Strategy: fit K_connected(t) = a + b*t in the ramp region
# Ramp region: t_dip < t < t_H, where t_dip is when K starts rising
# For small systems, use the region [0.1*t_H, 0.8*t_H]

# Use connected SFF on linear grid for slope
t_ramp_lo = 0.05 * t_H
t_ramp_hi = 0.8 * t_H
mask_ramp = (t_lin >= t_ramp_lo) & (t_lin <= t_ramp_hi)

# Full Hamiltonian ramp
if np.sum(mask_ramp) > 10:
    from numpy.polynomial.polynomial import polyfit
    coeffs_full = polyfit(t_lin[mask_ramp], K_full_conn_lin[mask_ramp], 1)
    slope_full = coeffs_full[1]  # linear coefficient
    intercept_full = coeffs_full[0]

    coeffs_rg = polyfit(t_lin[mask_ramp], K_rg_conn_lin[mask_ramp], 1)
    slope_rg = coeffs_rg[1]
    intercept_rg = coeffs_rg[0]

    # GUE slope: 1/(2*pi*D^2) for connected part
    slope_gue = 1.0 / (2 * np.pi * dim**2)
    slope_goe = 2.0 / (2 * np.pi * dim**2)

    ratio_full_gue = slope_full / slope_gue
    ratio_full_goe = slope_full / slope_goe
    ratio_rg_gue = slope_rg / slope_gue
    ratio_rg_goe = slope_rg / slope_goe

    print(f"Ramp fit region: [{t_ramp_lo:.1f}, {t_ramp_hi:.1f}]")
    print(f"  {np.sum(mask_ramp)} points in fit region")
    print()
    print(f"GUE ramp slope (theory): {slope_gue:.6e}")
    print(f"GOE ramp slope (theory): {slope_goe:.6e}")
    print()
    print(f"Full H connected SFF:")
    print(f"  slope = {slope_full:.6e}")
    print(f"  slope/GUE = {ratio_full_gue:.4f}")
    print(f"  slope/GOE = {ratio_full_goe:.4f}")
    print()
    print(f"RG H connected SFF:")
    print(f"  slope = {slope_rg:.6e}")
    print(f"  slope/GUE = {ratio_rg_gue:.4f}")
    print(f"  slope/GOE = {ratio_rg_goe:.4f}")
else:
    print("ERROR: insufficient points in ramp region")
    slope_full = 0
    ratio_full_gue = 0
    ratio_rg_gue = 0

print()

# -- Also extract slope from connected SFF on log grid using a window --
# Smoothed approach: compute running slope
def running_slope(t, K, window=20):
    """Compute local slope dK/dt using sliding window."""
    slopes = np.zeros(len(t))
    for i in range(window, len(t) - window):
        idx = slice(i - window, i + window)
        p = np.polyfit(t[idx], K[idx], 1)
        slopes[i] = p[0]
    return slopes

# -- Alternative: fit in multiple windows to assess ramp robustness --
print("Ramp robustness analysis (full H, connected SFF):")
windows = [(0.05, 0.3), (0.1, 0.5), (0.2, 0.6), (0.3, 0.8), (0.05, 0.8)]
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
print(f"  Mean slope/GUE = {slope_mean:.4f} +/- {slope_std:.4f}")
print()

# -- Goodness of fit: R^2 for linear fit in ramp region --
if np.sum(mask_ramp) > 10:
    K_pred = intercept_full + slope_full * t_lin[mask_ramp]
    SS_res = np.sum((K_full_conn_lin[mask_ramp] - K_pred)**2)
    SS_tot = np.sum((K_full_conn_lin[mask_ramp] - np.mean(K_full_conn_lin[mask_ramp]))**2)
    R2_full = 1 - SS_res / SS_tot if SS_tot > 0 else 0

    K_pred_rg = intercept_rg + slope_rg * t_lin[mask_ramp]
    SS_res_rg = np.sum((K_rg_conn_lin[mask_ramp] - K_pred_rg)**2)
    SS_tot_rg = np.sum((K_rg_conn_lin[mask_ramp] - np.mean(K_rg_conn_lin[mask_ramp]))**2)
    R2_rg = 1 - SS_res_rg / SS_tot_rg if SS_tot_rg > 0 else 0

    print(f"Linear fit R^2 (full H): {R2_full:.4f}")
    print(f"Linear fit R^2 (RG H): {R2_rg:.4f}")
else:
    R2_full = 0
    R2_rg = 0

print()

# -- Dip time extraction --
# Find minimum of K_full on log grid after initial decay
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

# -- Check if connected SFF is positive (ramp signature) --
ramp_mask = (t_lin > 0.1 * t_H) & (t_lin < 0.9 * t_H)
frac_positive_full = np.mean(K_full_conn_lin[ramp_mask] > 0) if np.any(ramp_mask) else 0
frac_positive_rg = np.mean(K_rg_conn_lin[ramp_mask] > 0) if np.any(ramp_mask) else 0
print(f"Fraction of connected SFF > 0 in ramp region:")
print(f"  Full H: {frac_positive_full:.4f}")
print(f"  RG H:   {frac_positive_rg:.4f}")
print()

# ============================================================================
# Section 9: Additional Diagnostics
# ============================================================================

# -- Number variance Sigma^2(L) --
# Sigma^2(L) = variance of number of eigenvalues in interval of length L
# For Poisson: Sigma^2(L) = L
# For GUE: Sigma^2(L) ~ (2/pi^2) * ln(L) for large L
# For GOE: Sigma^2(L) ~ (2/pi^2) * ln(L) + const

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
        # Count eigenvalues in windows of length L
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
sigma2_poisson = L_values  # Sigma^2 = L
sigma2_gue = (2.0 / np.pi**2) * (np.log(2 * np.pi * L_values) + 1 + np.euler_gamma - np.pi**2/8)
sigma2_gue = np.maximum(sigma2_gue, 0)  # clip negative at small L

print(f"Number variance at L=5:")
print(f"  Full H: Sigma^2 = {np.interp(5, L_values, sigma2_full):.4f}")
print(f"  RG H:   Sigma^2 = {np.interp(5, L_values, sigma2_rg):.4f}")
print(f"  Poisson: {5.0:.4f}")
print(f"  GUE:     {np.interp(5, L_values, sigma2_gue):.4f}")
print()

# -- Ensemble-averaged r-ratio for verification --
r_full_ens = []
r_rg_ens = []
for i_ens in range(n_ensemble):
    sp_full = np.diff(np.sort(all_evals_full[i_ens]))
    sp_rg = np.diff(np.sort(all_evals_rg[i_ens]))

    ratios_full = np.minimum(sp_full[:-1], sp_full[1:]) / np.maximum(sp_full[:-1], sp_full[1:])
    ratios_rg = np.minimum(sp_rg[:-1], sp_rg[1:]) / np.maximum(sp_rg[:-1], sp_rg[1:])

    r_full_ens.append(np.mean(ratios_full))
    r_rg_ens.append(np.mean(ratios_rg))

r_full_mean = np.mean(r_full_ens)
r_full_err = np.std(r_full_ens) / np.sqrt(n_ensemble)
r_rg_mean = np.mean(r_rg_ens)
r_rg_err = np.std(r_rg_ens) / np.sqrt(n_ensemble)

print(f"Ensemble r-ratio verification:")
print(f"  Full H: <r> = {r_full_mean:.4f} +/- {r_full_err:.4f} (S64: {r_full_s64:.4f})")
print(f"  RG H:   <r> = {r_rg_mean:.4f} +/- {r_rg_err:.4f}")
print(f"  Poisson: 0.386, GOE: 0.531, GUE: 0.603")
print()

# ============================================================================
# Section 10: Gate Verdict
# ============================================================================

print("="*70)
print("GATE VERDICT: SFF-NPAIR3-65")
print("="*70)
print()

# Use the connected SFF slope ratio as the decisive quantity
decisive_ratio = ratio_full_gue

if decisive_ratio > 0.3:
    verdict = "PASS"
    reason = f"Ramp detected with slope/GUE = {decisive_ratio:.4f} > 0.3"
elif decisive_ratio < 0.1:
    verdict = "FAIL"
    reason = f"No ramp: slope/GUE = {decisive_ratio:.4f} < 0.1"
else:
    verdict = "INFO"
    reason = f"Intermediate: slope/GUE = {decisive_ratio:.4f} in [0.1, 0.3]"

print(f"  Threshold: slope/GUE > 0.3 (PASS), < 0.1 (FAIL)")
print(f"  Computed:  slope/GUE = {decisive_ratio:.4f}")
print(f"  R^2 of linear fit: {R2_full:.4f}")
print(f"  Verdict:   {verdict} -- {reason}")
print()
print(f"  Additional context:")
print(f"    slope/GOE = {ratio_full_goe:.4f}")
print(f"    RG slope/GUE = {ratio_rg_gue:.4f}")
print(f"    <r>_full = {r_full_mean:.4f}, <r>_RG = {r_rg_mean:.4f}")
print(f"    Fraction connected SFF > 0 in ramp: {frac_positive_full:.4f}")
print()

# ============================================================================
# Section 11: Save Data
# ============================================================================

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's65_sff_npair3.npz')

np.savez(out_path,
         # Gate
         gate_name='SFF-NPAIR3-65',
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

         # RMT predictions (log grid)
         K_gue_log=K_gue_log,
         K_goe_log=K_goe_log,
         K_poisson=K_poisson,

         # Slopes
         slope_full=slope_full,
         slope_rg=slope_rg,
         slope_gue=slope_gue,
         slope_goe=slope_goe,
         ratio_full_gue=ratio_full_gue,
         ratio_full_goe=ratio_full_goe,
         ratio_rg_gue=ratio_rg_gue,
         R2_full=R2_full,
         R2_rg=R2_rg,

         # Dip
         t_dip_full=t_dip_full,
         K_dip_full=K_dip_full,

         # Number variance
         L_values=L_values,
         sigma2_full=sigma2_full,
         sigma2_rg=sigma2_rg,
         sigma2_poisson=sigma2_poisson,
         sigma2_gue=sigma2_gue,

         # r-ratio verification
         r_full_mean=r_full_mean,
         r_full_err=r_full_err,
         r_rg_mean=r_rg_mean,
         r_rg_err=r_rg_err,

         # Ensemble data (for reproducibility)
         frac_positive_full=frac_positive_full,
         frac_positive_rg=frac_positive_rg,
         slope_windows=np.array(slopes_windows),
         slope_mean=slope_mean,
         slope_std=slope_std,
         )

print(f"Data saved to: {out_path}")
print()

# ============================================================================
# Section 12: Plot
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
# Plot absolute value of connected SFF
K_fc_pos = np.where(K_full_conn_log > 0, K_full_conn_log, np.nan)
K_fc_neg = np.where(K_full_conn_log < 0, -K_full_conn_log, np.nan)
ax.loglog(t_values, K_fc_pos, 'b-', lw=1.0, alpha=0.8, label='Full H (K_c > 0)')
ax.loglog(t_values, K_fc_neg, 'b--', lw=0.7, alpha=0.5, label='Full H (|K_c| < 0)')

K_rc_pos = np.where(K_rg_conn_log > 0, K_rg_conn_log, np.nan)
K_rc_neg = np.where(K_rg_conn_log < 0, -K_rg_conn_log, np.nan)
ax.loglog(t_values, K_rc_pos, 'r-', lw=1.0, alpha=0.6, label='RG H (K_c > 0)')
ax.loglog(t_values, K_rc_neg, 'r--', lw=0.7, alpha=0.4, label='RG H (|K_c| < 0)')

# GUE ramp on connected SFF
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
# GUE/GOE predictions
t_lin_norm = t_lin / t_H
gue_ramp_lin = np.where(t_lin_norm < 1, slope_gue * t_lin, 0)
goe_ramp_lin = np.where(t_lin_norm < 1, slope_goe * t_lin, 0)
ax.plot(t_lin / t_H, gue_ramp_lin, 'k--', lw=1.0, alpha=0.5, label='GUE')
ax.plot(t_lin / t_H, goe_ramp_lin, 'k:', lw=1.0, alpha=0.5, label='GOE')
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(1.0, color='green', ls='--', lw=0.8, alpha=0.5, label='$t_H$')
ax.set_xlabel('$t / t_H$')
ax.set_ylabel('$K_c(t)$')
ax.set_title(f'(c) Connected SFF (linear) | slope/GUE = {ratio_full_gue:.3f}')
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
ax.set_title('(d) Number Variance')
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
summary_text = f"""SFF-NPAIR3-65 Gate Verdict: {verdict}

Parameters:
  N_modes = {N_modes}, N_pair = {N_pair}, dim = {dim}
  n_ensemble = {n_ensemble}, sigma_lift = {sigma_lift}

SFF Ramp Analysis:
  slope/GUE (full H) = {ratio_full_gue:.4f}
  slope/GOE (full H) = {ratio_full_goe:.4f}
  slope/GUE (RG H)   = {ratio_rg_gue:.4f}
  R² linear fit (full) = {R2_full:.4f}
  R² linear fit (RG)   = {R2_rg:.4f}

  Mean slope/GUE across windows = {slope_mean:.4f} ± {slope_std:.4f}
  Frac. K_c > 0 in ramp (full) = {frac_positive_full:.4f}
  Frac. K_c > 0 in ramp (RG)   = {frac_positive_rg:.4f}

Dip: t_dip = {t_dip_full:.1f}, K_dip/plateau = {K_dip_full/plateau_level:.3f}

r-ratio verification:
  Full H: <r> = {r_full_mean:.4f} ± {r_full_err:.4f}
  RG H:   <r> = {r_rg_mean:.4f} ± {r_rg_err:.4f}

Threshold: PASS > 0.3, FAIL < 0.1
Reason: {reason}
"""
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle(f'S65 SFF-NPAIR3: Spectral Form Factor for N_pair=3 Pairing Hamiltonian (dim={dim})',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's65_sff_npair3.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")
print()
print("DONE.")
