#!/usr/bin/env python3
"""
OTOC-NPAIR3-65: Out-of-Time-Ordered Correlator for N=3 Pairing-Only Sector
===========================================================================

Gate: OTOC-NPAIR3-65
  PASS: lambda_L > 0 with R^2 > 0.90 (genuine chaos, exponential scrambling)
  FAIL: R^2 < 0.90 for exponential fit (no clear exponential growth)
  INFO: Power-law growth consistent with pre-thermalization (not chaos)

Physics:
  The OTOC measures quantum information scrambling. For operators W, V:
    C(t) = <[W(t), V(0)]^dag [W(t), V(0)]>_beta                    (1)

  Chaotic systems: C(t) ~ A * exp(2 * lambda_L * t) at early times.
  The Maldacena-Shenker-Stanford (MSS) bound constrains:
    lambda_L <= 2 * pi * T / hbar                                    (2)
  Systems saturating this bound are MAXIMALLY CHAOTIC (black holes, SYK).

  Integrable systems: C(t) ~ t^alpha (polynomial, no exponential regime).
  The Richardson-Gaudin pairing Hamiltonian is exactly integrable.
  The full V_{kl} from D_K on Jensen-deformed SU(3) is non-separable
  (rank-1 captures only 64% of ||V||^2 at N_pair=3, S64). This breaks
  Richardson-Gaudin integrability, but the question is whether the
  breaking is strong enough to produce genuine scrambling.

  Prior results:
  - S38 CHAOS-2: 256-dim full Fock space, OTOC ~ t^{1.9}, lambda_L = 0. FAIL.
  - S59 2-cell: C(t) ~ t^{1.04}, lambda_L = 0 (R^2=0.041). FAIL.
  - S64 N-PAIR-3-RG-64: <r> = 0.478+/-0.021 (transition) for full V (lifted).
    But Brody beta = 0.01+/-0.14 (contradicts). OTOC resolves this.

  This computation focuses on the N_pair=3 sector (dim=56) with the FULL
  pairing interaction, which showed the most interesting level statistics
  in S64. We use number operators n_k as OTOC probes because they:
  (a) Are diagonal in the Fock basis (natural observables)
  (b) Do NOT change pair number (so OTOC probes scrambling WITHIN the sector)
  (c) Are the operators whose correlations define GGE occupation numbers

Method:
  1. Build H_full in the N_pair=3 Fock basis (C(8,3) = 56 states)
  2. Exact diagonalization: H = U D U^T
  3. Build W = n_1 (mode 1 occupation) and V = n_2 (mode 2 occupation)
  4. In the energy eigenbasis:
     W(t)_{ij} = W_{ij} * exp(i*(E_i - E_j)*t)
     C(t) = [W(t), V] = W(t)V - VW(t)
     OTOC(t) = Tr(rho * C(t)^dag C(t)) / Z
  5. Evaluate at 200 time points, t in [0, 50/J]
  6. Fit early-time growth: C(t) ~ A*exp(2*lambda_L*t) vs C(t) ~ B*t^alpha
  7. Compare to MSS bound

References:
  - Paper 05: Maldacena, Shenker, Stanford (2016) — MSS bound
  - Paper 06: Larkin, Ovchinnikov (1969) — original OTOC in BCS context
  - S38 CHAOS-2: Full 256-dim OTOC (no Lyapunov regime)
  - S59: 2-cell OTOC (power-law, no scrambling)
  - S64 N-PAIR-3-RG-64: Level statistics showing <r>=0.478 (transition)

Session: S65 W4-B
Agent: kitaev-quantum-chaos-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
from scipy.optimize import curve_fit, fsolve
from scipy.stats import kstest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time

# === Import canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_0_OES, T_acoustic, PI, dt_transit,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
#  1. LOAD INPUT DATA AND BUILD HAMILTONIAN
# =====================================================================

print("=" * 72)
print("OTOC-NPAIR3-65: OTOC for N=3 Pairing-Only Sector")
print("=" * 72)

# Load S52 HFB data (same source as S64)
hfb_data = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies (M_KK)
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction (M_KK)
labels = hfb_data['labels']
N_modes = len(eps_bare)

# Cross-check against S64 archived data
d64 = np.load(os.path.join(data_dir, 's64_npair3_rg.npz'), allow_pickle=True)
assert np.allclose(eps_bare, d64['eps_bare']), "eps_bare mismatch vs S64"
assert np.allclose(V_bare, d64['V_bare']), "V_bare mismatch vs S64"

# Parameters
N_pair = 3  # (local)
Delta_target = Delta_0_OES  # 0.4643 M_KK

print(f"N_modes = {N_modes}")
print(f"eps_bare = {eps_bare}")
print(f"labels = {list(labels)}")
print(f"N_pair = {N_pair}")
print(f"Delta_target = {Delta_target:.6f} M_KK")

# Solve BCS gap equation for coupling g at N_pair=3
def bcs_equations(params, eps, Delta, N_target):
    """BCS gap + number equations for uniform g."""
    mu, g = params
    E_k = np.sqrt((eps - mu)**2 + Delta**2)
    v2 = 0.5 * (1 - (eps - mu) / E_k)
    number_eq = np.sum(v2) - N_target
    gap_eq = 1.0/g - 0.5 * np.sum(1.0/E_k)
    return [number_eq, gap_eq]

mu0 = np.mean(eps_bare)
g0 = 0.15  # (local)
sol = fsolve(bcs_equations, [mu0, g0], args=(eps_bare, Delta_target, N_pair), full_output=True)
mu_sol, g_sol = sol[0]
print(f"BCS solution: mu = {mu_sol:.6f}, g = {g_sol:.6f}")

# Verify against S64 values
assert abs(g_sol - float(d64['N3_g'])) < 1e-6, \
    f"g mismatch: {g_sol} vs {float(d64['N3_g'])}"
assert abs(mu_sol - float(d64['N3_mu'])) < 1e-6, \
    f"mu mismatch: {mu_sol} vs {float(d64['N3_mu'])}"
print("  Cross-check vs S64 data: PASSED")

# =====================================================================
#  2. BUILD FOCK SPACE AND HAMILTONIANS
# =====================================================================

print("\n" + "=" * 72)
print("BUILDING FOCK SPACE (N_pair=3, C(8,3) = 56 states)")
print("=" * 72)

states = list(combinations(range(N_modes), N_pair))
dim = len(states)
assert dim == mcomb(N_modes, N_pair), f"dim={dim} != C({N_modes},{N_pair})"
print(f"Fock space dimension: {dim}")

# State-to-index lookup
state_to_idx = {s: i for i, s in enumerate(states)}

def build_hamiltonian_full(eps, V, states, N_modes):
    """
    Build full pairing Hamiltonian with non-separable V_{kl}.
    H_full = sum_k 2*eps_k n_k - sum_{k,l} V_{kl} P_k^+ P_l
    Diagonal: sum_{k in state} (2*eps_k - V_{kk})
    Off-diagonal (differ by one pair k<->l): -V_{kl}
    """
    dim = len(states)
    H = np.zeros((dim, dim))
    for i, si in enumerate(states):
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        H[i, i] -= sum(V[k, k] for k in si)
        for j in range(i+1, dim):
            sj = states[j]
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

print("Building H_full (full V_{kl})...")
t0 = time.time()
H_full = build_hamiltonian_full(eps_bare, V_bare, states, N_modes)
t1 = time.time()
print(f"  Build time: {t1-t0:.4f}s")

# Verify Hermiticity
herm_err = np.max(np.abs(H_full - H_full.T))
print(f"  Hermiticity error: {herm_err:.2e}")
assert herm_err < 1e-12, f"H_full not Hermitian: {herm_err}"

# Diagonalize
print("  Diagonalizing...")
evals, evecs = eigh(H_full)
print(f"  E_min = {evals[0]:.6f}, E_max = {evals[-1]:.6f}")
print(f"  Bandwidth = {evals[-1] - evals[0]:.6f}")

# Cross-check against S64 eigenvalues
evals_s64 = d64['N3_evals_full']
eval_err = np.max(np.abs(np.sort(evals) - np.sort(evals_s64)))
print(f"  Eigenvalue cross-check vs S64: max|delta_E| = {eval_err:.2e}")
assert eval_err < 1e-10, f"Eigenvalue mismatch: {eval_err}"
print("  Cross-check: PASSED")

# =====================================================================
#  3. BUILD NUMBER OPERATORS n_k IN FOCK BASIS
# =====================================================================

print("\n" + "=" * 72)
print("BUILDING NUMBER OPERATORS")
print("=" * 72)

def build_number_operator(mode_idx, states, dim):
    """
    Build n_k (pair occupation of mode k) in the Fock basis.
    n_k|state> = (1 if k in state, else 0) |state>
    This is diagonal in the Fock basis.
    """
    n_op = np.zeros((dim, dim))
    for i, s in enumerate(states):
        if mode_idx in s:
            n_op[i, i] = 1.0
    return n_op

# W = n_1 (number operator for mode 1 = B2[1])
# V = n_2 (number operator for mode 2 = B2[2])
# Choice rationale: different modes within the B2 shell, so
# inter-mode correlations probe scrambling within the dominant sector.
W_mode = 1  # B2[1]
V_mode = 2  # B2[2]

W_op = build_number_operator(W_mode, states, dim)
V_op = build_number_operator(V_mode, states, dim)

print(f"W = n_{W_mode} ({labels[W_mode]})")
print(f"V = n_{V_mode} ({labels[V_mode]})")
print(f"  Tr(W) = {np.trace(W_op):.0f}")
print(f"  Tr(V) = {np.trace(V_op):.0f}")
print(f"  Tr(WV) = {np.trace(W_op @ V_op):.0f}")

# Transform to energy eigenbasis
W_eig = evecs.T @ W_op @ evecs
V_eig = evecs.T @ V_op @ evecs

# Verify: [H, n_k] should be nonzero in general (n_k is not conserved)
# Actually: n_k IS conserved by H_RG (uniform g), but NOT by H_full
# because V_{kl} for k != l scatters pairs between modes.
comm_HW = H_full @ W_op - W_op @ H_full
comm_HV = H_full @ V_op - V_op @ H_full
print(f"  ||[H, W]|| = {np.linalg.norm(comm_HW):.6f}")
print(f"  ||[H, V]|| = {np.linalg.norm(comm_HV):.6f}")

if np.linalg.norm(comm_HW) < 1e-12:
    print("  WARNING: [H, W] = 0 => W is conserved => OTOC identically zero.")
    print("  This would mean mode occupation is a conserved quantity.")

# Also build n_4 (B1 mode) for cross-sector probe
W2_mode = 4  # B1
V2_mode = 5  # B3[0]
W2_op = build_number_operator(W2_mode, states, dim)
V2_op = build_number_operator(V2_mode, states, dim)
W2_eig = evecs.T @ W2_op @ evecs
V2_eig = evecs.T @ V2_op @ evecs
print(f"\nCross-sector probe: W2 = n_{W2_mode} ({labels[W2_mode]}), "
      f"V2 = n_{V2_mode} ({labels[V2_mode]})")
print(f"  ||[H, W2]|| = {np.linalg.norm(H_full @ W2_op - W2_op @ H_full):.6f}")
print(f"  ||[H, V2]|| = {np.linalg.norm(H_full @ V2_op - V2_op @ H_full):.6f}")

# =====================================================================
#  4. COMPUTE OTOC C(t)
# =====================================================================

print("\n" + "=" * 72)
print("COMPUTING OTOC C(t)")
print("=" * 72)

# Method: exact diagonalization in the energy eigenbasis.
# W(t)_{ij} = W_{ij} * exp(i*(E_i - E_j)*t)
# C(t) = [W(t), V] = W(t)V - VW(t)
# OTOC(t) = Tr(rho * C(t)^dag C(t)) / Z
#
# For the microcanonical (infinite temperature within sector):
#   rho = I/dim, so OTOC(t) = Tr(C(t)^dag C(t)) / dim

# Energy differences
E_diff = evals[:, None] - evals[None, :]

# Time array: 200 points from 0 to 50/J
# J scale: the mean off-diagonal coupling strength
J_scale = np.mean(np.abs(V_bare[np.triu_indices(N_modes, k=1)]))
t_max = 50.0 / J_scale  # (local)
n_times = 200
t_array = np.linspace(0, t_max, n_times)

print(f"J_scale (mean off-diag |V|) = {J_scale:.6f} M_KK")
print(f"t_max = 50/J = {t_max:.4f} M_KK^{{-1}}")
print(f"n_times = {n_times}")
print(f"Bandwidth / J = {(evals[-1]-evals[0]) / J_scale:.2f}")

# Temperature for MSS bound comparison
# Use T_acoustic = 0.112 M_KK (GGE temperature from S42/S47)
T_GGE = T_acoustic
beta_GGE = 1.0 / T_GGE
lambda_MSS = 2.0 * PI * T_GGE  # MSS bound in natural units (hbar=1)
print(f"T_GGE = {T_GGE:.4f} M_KK")
print(f"MSS bound: lambda_L_max = 2*pi*T = {lambda_MSS:.4f} M_KK")

# Also compute at infinite temperature within the sector (microcanonical)
# and at T_GGE (thermal)

# --- Probe 1: n_1 vs n_2 (intra-B2) ---
print("\n--- Probe 1: W=n_1(B2[1]), V=n_2(B2[2]) ---")

def compute_otoc(W_eig, V_eig, evals, E_diff, t_array, beta=None):
    """
    Compute OTOC C(t) = Tr(rho * [W(t),V]^dag [W(t),V]) / Z.

    Parameters:
        W_eig, V_eig: operators in energy eigenbasis
        evals: energy eigenvalues
        E_diff: E_i - E_j matrix
        t_array: time points
        beta: inverse temperature (None = infinite T within sector)

    Returns:
        C_t: OTOC values at each time point
    """
    dim = len(evals)
    n_t = len(t_array)
    C_t = np.zeros(n_t)

    # Thermal weights
    if beta is not None:
        boltzmann = np.exp(-beta * (evals - evals[0]))
        Z = np.sum(boltzmann)
        rho_diag = boltzmann / Z
    else:
        rho_diag = np.ones(dim) / dim

    for t_idx, t in enumerate(t_array):
        # W(t) in eigenbasis
        phase = np.exp(1j * E_diff * t)
        Wt = W_eig * phase

        # Commutator [W(t), V]
        comm = Wt @ V_eig - V_eig @ Wt

        # C(t) = Tr(rho * comm^dag comm) / Z
        # = sum_i rho_i (comm^dag comm)_{ii}
        # = sum_i rho_i sum_j |comm_{ji}|^2
        # = sum_{i,j} rho_i |comm_{ji}|^2
        comm_dag_comm = np.conj(comm).T @ comm
        C_t[t_idx] = np.real(np.sum(rho_diag * np.diag(comm_dag_comm)))

    return C_t

print("Computing OTOC (infinite T)...")
t0 = time.time()
C_infT = compute_otoc(W_eig, V_eig, evals, E_diff, t_array, beta=None)
t1 = time.time()
print(f"  Time: {t1-t0:.2f}s")
print(f"  C(0) = {C_infT[0]:.2e} (should be ~0)")
print(f"  C_max = {np.max(C_infT):.6f}")
print(f"  C_max time = {t_array[np.argmax(C_infT)]:.4f} M_KK^{{-1}}")

print("Computing OTOC (T = T_GGE)...")
t0 = time.time()
C_GGE = compute_otoc(W_eig, V_eig, evals, E_diff, t_array, beta=beta_GGE)
t1 = time.time()
print(f"  Time: {t1-t0:.2f}s")
print(f"  C(0) = {C_GGE[0]:.2e}")
print(f"  C_max = {np.max(C_GGE):.6f}")

# --- Probe 2: n_4(B1) vs n_5(B3[0]) (cross-sector) ---
print("\n--- Probe 2: W=n_4(B1), V=n_5(B3[0]) ---")

C_cross_infT = compute_otoc(W2_eig, V2_eig, evals, E_diff, t_array, beta=None)
print(f"  C_max = {np.max(C_cross_infT):.6f}")

# --- Probe 3: n_0(B2[0]) vs n_4(B1) (B2-B1 cross) ---
W3_mode = 0  # B2[0]
V3_mode = 4  # B1
W3_eig = evecs.T @ build_number_operator(W3_mode, states, dim) @ evecs
V3_eig = evecs.T @ build_number_operator(V3_mode, states, dim) @ evecs
C_B2B1_infT = compute_otoc(W3_eig, V3_eig, evals, E_diff, t_array, beta=None)
print(f"\n--- Probe 3: W=n_0(B2[0]), V=n_4(B1) ---")
print(f"  C_max = {np.max(C_B2B1_infT):.6f}")

# =====================================================================
#  5. EXTRACT LYAPUNOV EXPONENT
# =====================================================================

print("\n" + "=" * 72)
print("LYAPUNOV EXPONENT EXTRACTION")
print("=" * 72)

# Find the early-time growth regime.
# The OTOC starts at C(0) = 0 and grows. The BCH expansion gives
# C(t) ~ t^2 at very early times (always, chaotic or not).
# A genuine Lyapunov regime has C(t) ~ A*exp(2*lambda_L*t) sustained
# over at least 1 decade in C(t).
#
# Criterion: R^2 > 0.90 for exponential fit over at least 1 decade.

def extract_lyapunov(t_arr, C_arr, label=""):
    """
    Attempt to extract Lyapunov exponent from early-time OTOC growth.

    Returns:
        lambda_L: Lyapunov exponent (0 if no exponential regime)
        R2_exp: R^2 for exponential fit
        alpha_pow: power-law exponent
        R2_pow: R^2 for power-law fit
        fit_info: dict with detailed results
    """
    info = {}

    # Find the growth regime: C(t) > threshold and before saturation
    C_max = np.max(C_arr)
    if C_max < 1e-15:
        print(f"  [{label}] C_max = {C_max:.2e} < 1e-15. No growth.")
        info['status'] = 'NO_GROWTH'
        return 0.0, 0.0, 0.0, 0.0, info

    # Define growth regime: C > 1e-4 * C_max and C < 0.5 * C_max
    # (below half-saturation)
    mask_low = C_arr > 1e-4 * C_max
    mask_high = C_arr < 0.5 * C_max
    mask = mask_low & mask_high & (t_arr > 0)

    if np.sum(mask) < 10:
        # Try more relaxed bounds
        mask = (C_arr > 1e-6 * C_max) & (C_arr < 0.8 * C_max) & (t_arr > 0)

    if np.sum(mask) < 5:
        print(f"  [{label}] Growth regime too short ({np.sum(mask)} points).")
        info['status'] = 'SHORT_GROWTH'
        return 0.0, 0.0, 0.0, 0.0, info

    t_fit = t_arr[mask]
    C_fit = C_arr[mask]

    # Power-law fit: C(t) ~ B * t^alpha
    # In log-log: log(C) = log(B) + alpha * log(t)
    log_t = np.log(t_fit)
    log_C = np.log(C_fit)

    # Linear regression in log-log
    coeffs_pow = np.polyfit(log_t, log_C, 1)
    alpha_pow = coeffs_pow[0]
    B_pow = np.exp(coeffs_pow[1])
    log_C_pred_pow = np.polyval(coeffs_pow, log_t)
    SS_res_pow = np.sum((log_C - log_C_pred_pow)**2)
    SS_tot = np.sum((log_C - np.mean(log_C))**2)
    R2_pow = 1 - SS_res_pow / SS_tot if SS_tot > 0 else 0.0

    # Exponential fit: C(t) ~ A * exp(2*lambda_L*t)
    # In semi-log: log(C) = log(A) + 2*lambda_L * t
    coeffs_exp = np.polyfit(t_fit, log_C, 1)
    lambda_L = coeffs_exp[0] / 2.0  # C ~ exp(2*lambda_L*t)
    A_exp = np.exp(coeffs_exp[1])
    log_C_pred_exp = np.polyval(coeffs_exp, t_fit)
    SS_res_exp = np.sum((log_C - log_C_pred_exp)**2)
    R2_exp = 1 - SS_res_exp / SS_tot if SS_tot > 0 else 0.0

    # Check if exponential fit spans at least 1 decade
    C_range = np.max(C_fit) / np.min(C_fit)

    print(f"  [{label}] Growth regime: t in [{t_fit[0]:.3f}, {t_fit[-1]:.3f}]")
    print(f"    C range: [{np.min(C_fit):.2e}, {np.max(C_fit):.2e}] "
          f"({np.log10(C_range):.2f} decades)")
    print(f"    Power-law: C ~ {B_pow:.2e} * t^{alpha_pow:.3f} (R^2 = {R2_pow:.4f})")
    print(f"    Exponential: C ~ {A_exp:.2e} * exp(2*{lambda_L:.4f}*t) "
          f"(R^2 = {R2_exp:.4f})")

    if lambda_L < 0:
        print(f"    lambda_L < 0 => NO exponential growth")
        lambda_L = 0.0  # (local)

    info.update({
        'status': 'FITTED',
        't_fit': t_fit,
        'C_fit': C_fit,
        'alpha_pow': alpha_pow,
        'B_pow': B_pow,
        'R2_pow': R2_pow,
        'lambda_L_raw': coeffs_exp[0] / 2.0,
        'A_exp': A_exp,
        'R2_exp': R2_exp,
        'C_range_decades': np.log10(C_range),
    })

    return lambda_L, R2_exp, alpha_pow, R2_pow, info

# Probe 1: intra-B2
lambda_L_1, R2_exp_1, alpha_1, R2_pow_1, info_1 = extract_lyapunov(
    t_array, C_infT, label="Probe1(B2-B2)")

# Probe 2: cross-sector
lambda_L_2, R2_exp_2, alpha_2, R2_pow_2, info_2 = extract_lyapunov(
    t_array, C_cross_infT, label="Probe2(B1-B3)")

# Probe 3: B2-B1 cross
lambda_L_3, R2_exp_3, alpha_3, R2_pow_3, info_3 = extract_lyapunov(
    t_array, C_B2B1_infT, label="Probe3(B2-B1)")

# Also at T_GGE
lambda_L_GGE, R2_exp_GGE, alpha_GGE, R2_pow_GGE, info_GGE = extract_lyapunov(
    t_array, C_GGE, label="Probe1-GGE")

# =====================================================================
#  6. MSS BOUND COMPARISON
# =====================================================================

print("\n" + "=" * 72)
print("MSS BOUND COMPARISON")
print("=" * 72)

# Maximum lambda_L across all probes
lambda_max = max(lambda_L_1, lambda_L_2, lambda_L_3, lambda_L_GGE)
R2_best = max(R2_exp_1, R2_exp_2, R2_exp_3, R2_exp_GGE)

print(f"Maximum lambda_L across probes: {lambda_max:.6f} M_KK")
print(f"Best R^2 (exponential): {R2_best:.4f}")
print(f"MSS bound: lambda_L_max = 2*pi*T_GGE = {lambda_MSS:.4f} M_KK")

if R2_best >= 0.90:
    print(f"  R^2 >= 0.90 => GENUINE Lyapunov regime detected")
    if lambda_max > lambda_MSS:
        print(f"  KILL CONDITION: lambda_L = {lambda_max:.4f} > MSS = {lambda_MSS:.4f}")
        print(f"  This would violate a fundamental quantum bound!")
    else:
        print(f"  lambda_L / MSS = {lambda_max / lambda_MSS:.4f}")
        print(f"  Bound satisfied.")
else:
    print(f"  R^2 < 0.90 => No genuine Lyapunov regime")
    print(f"  System does NOT exhibit exponential scrambling")

# =====================================================================
#  7. SCRAMBLING TIME ESTIMATE
# =====================================================================

print("\n" + "=" * 72)
print("SCRAMBLING TIME ESTIMATE")
print("=" * 72)

# Scrambling time from OTOC: time at which C(t) reaches O(1) fraction of C_max
# Standard criterion: C(t_scr) = 0.5 * C_max

def estimate_scrambling_time(t_arr, C_arr, fraction=0.5):
    """Estimate scrambling time as when C reaches fraction of C_max."""
    C_max = np.max(C_arr)
    threshold = fraction * C_max
    above = np.where(C_arr >= threshold)[0]
    if len(above) == 0:
        return np.inf
    return t_arr[above[0]]

t_scr_1 = estimate_scrambling_time(t_array, C_infT)
t_scr_cross = estimate_scrambling_time(t_array, C_cross_infT)
t_scr_GGE = estimate_scrambling_time(t_array, C_GGE)

t_transit = dt_transit  # from canonical constants

print(f"Scrambling times (C = 0.5 * C_max):")
print(f"  Probe 1 (B2-B2, inf T): t_scr = {t_scr_1:.4f} M_KK^{{-1}}")
print(f"  Probe 2 (B1-B3, inf T): t_scr = {t_scr_cross:.4f} M_KK^{{-1}}")
print(f"  Probe 1 (B2-B2, GGE T): t_scr = {t_scr_GGE:.4f} M_KK^{{-1}}")
print(f"  Transit time: t_transit = {t_transit:.6f} M_KK^{{-1}}")
print(f"  t_scr / t_transit (Probe 1, inf T): {t_scr_1 / t_transit:.0f}x")
print(f"  t_scr / t_transit (Probe 2, inf T): {t_scr_cross / t_transit:.0f}x")

# =====================================================================
#  8. SPECTRAL FORM FACTOR
# =====================================================================

print("\n" + "=" * 72)
print("SPECTRAL FORM FACTOR K(t)")
print("=" * 72)

# K(t) = |sum_n exp(-i E_n t)|^2 / dim^2
# Ramp+plateau in K(t) is a diagnostic for level repulsion (chaos).
# Poisson: K(t) = 1 for all t > 0 (no ramp).
# GUE: K(t) = t/dim for t < dim (ramp), K(t) = 1 for t > dim (plateau).

t_sff = np.linspace(0, 200.0 / J_scale, 2000)
K_t = np.zeros(len(t_sff))

# Unfolded eigenvalues for SFF
evals_unf = (evals - evals[0]) / np.mean(np.diff(evals))

for t_idx, t in enumerate(t_sff):
    phases = np.exp(-1j * evals_unf * t)
    K_t[t_idx] = np.abs(np.sum(phases))**2 / dim**2

# Detect ramp
# Connected SFF: K_c(t) = K(t) - |<exp(-iEt)>|^2
# For the ramp, look at K(t) > 1/dim
K_plateau = 1.0 / dim
K_early = np.mean(K_t[10:50])  # avoid t=0
K_late = np.mean(K_t[-200:])

print(f"  K(0) = {K_t[0]:.4f} (should be 1)")
print(f"  K(early, t~{t_sff[30]:.1f}) = {K_early:.4f}")
print(f"  K(late) = {K_late:.4f}")
print(f"  K_plateau (1/dim) = {K_plateau:.4f}")
print(f"  K_late / K_plateau = {K_late / K_plateau:.2f}")

# GUE ramp slope: dK/dt = 1/(dim * t_H) where t_H = 2*pi*dim/bandwidth
# For Poisson: K(t) drops to 1/dim immediately (no ramp)
# Check if there's a linear ramp region
ramp_mask = (t_sff > 10/J_scale) & (t_sff < 100/J_scale) & (K_t > 0.5*K_plateau)
if np.sum(ramp_mask) > 10:
    t_ramp = t_sff[ramp_mask]
    K_ramp = K_t[ramp_mask]
    ramp_coeffs = np.polyfit(t_ramp, K_ramp, 1)
    slope_actual = ramp_coeffs[0]
    # Expected GUE slope
    bandwidth = evals_unf[-1] - evals_unf[0]
    slope_GUE = 1.0 / (2 * PI * dim)
    print(f"  Ramp slope: {slope_actual:.2e}")
    print(f"  GUE expected slope: {slope_GUE:.2e}")
    print(f"  slope/slope_GUE = {slope_actual/slope_GUE:.4f}")
else:
    slope_actual = 0.0  # (local)
    slope_GUE = 1.0 / (2 * PI * dim)
    print(f"  No ramp region detected (Poisson-like)")

# =====================================================================
#  9. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: OTOC-NPAIR3-65")
print("=" * 72)

# Determine verdict
probes = {
    'B2-B2 (infT)': (lambda_L_1, R2_exp_1, alpha_1, R2_pow_1),
    'B1-B3 (infT)': (lambda_L_2, R2_exp_2, alpha_2, R2_pow_2),
    'B2-B1 (infT)': (lambda_L_3, R2_exp_3, alpha_3, R2_pow_3),
    'B2-B2 (GGE)':  (lambda_L_GGE, R2_exp_GGE, alpha_GGE, R2_pow_GGE),
}

any_chaotic = False
for name, (lam, r2e, alp, r2p) in probes.items():
    chaotic = (lam > 0) and (r2e > 0.90)
    tag = "CHAOTIC" if chaotic else "NOT CHAOTIC"
    if chaotic:
        any_chaotic = True
    print(f"  {name}: lambda_L={lam:.4f}, R2_exp={r2e:.4f}, "
          f"alpha={alp:.3f}, R2_pow={r2p:.4f} => {tag}")

print()
if any_chaotic:
    gate_verdict = "PASS"
    gate_reason = (f"Genuine Lyapunov regime detected. "
                   f"lambda_L={lambda_max:.4f}, R2={R2_best:.4f}.")
    if lambda_max > lambda_MSS:
        gate_verdict = "KILL"
        gate_reason = (f"MSS BOUND VIOLATED: lambda_L={lambda_max:.4f} > "
                       f"2*pi*T={lambda_MSS:.4f}. Framework inconsistency!")
else:
    # Check if power-law is a good fit
    best_R2_pow = max(R2_pow_1, R2_pow_2, R2_pow_3, R2_pow_GGE)
    best_alpha = alpha_1  # from primary probe
    if best_R2_pow > 0.90:
        gate_verdict = "INFO"
        gate_reason = (f"Power-law C~t^{{{best_alpha:.2f}}} (R2={best_R2_pow:.4f}). "
                       f"Pre-thermalization dephasing, not chaos.")
    else:
        gate_verdict = "FAIL"
        gate_reason = (f"No Lyapunov regime (R2_exp={R2_best:.4f} < 0.90). "
                       f"Best power-law alpha={best_alpha:.2f}.")

print(f"Gate OTOC-NPAIR3-65: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print(f"  Threshold: R^2 > 0.90 for exponential fit => PASS")
print(f"  Computed: R^2_exp = {R2_best:.4f} (max across probes)")
print(f"  MSS bound: lambda_L_max = {lambda_MSS:.4f} M_KK")
print(f"  Scrambling time (primary): {t_scr_1:.4f} M_KK^{{-1}}")
print(f"  t_scr / t_transit: {t_scr_1 / t_transit:.0f}x")

# =====================================================================
#  10. SAVE DATA
# =====================================================================

print("\n" + "=" * 72)
print("SAVING DATA")
print("=" * 72)

output_path = os.path.join(data_dir, 's65_otoc_npair3.npz')
np.savez(output_path,
    # Gate
    gate_name='OTOC-NPAIR3-65',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    # Parameters
    N_pair=N_pair,
    dim=dim,
    N_modes=N_modes,
    eps_bare=eps_bare,
    V_bare=V_bare,
    labels=labels,
    g_sol=g_sol,
    mu_sol=mu_sol,
    Delta_target=Delta_target,
    J_scale=J_scale,
    T_GGE=T_GGE,
    lambda_MSS=lambda_MSS,
    # Spectrum
    evals=evals,
    # Time array
    t_array=t_array,
    t_max=t_max,
    n_times=n_times,
    # OTOC results
    C_infT=C_infT,
    C_GGE=C_GGE,
    C_cross_infT=C_cross_infT,
    C_B2B1_infT=C_B2B1_infT,
    # Lyapunov extraction
    lambda_L_1=lambda_L_1, R2_exp_1=R2_exp_1, alpha_1=alpha_1, R2_pow_1=R2_pow_1,
    lambda_L_2=lambda_L_2, R2_exp_2=R2_exp_2, alpha_2=alpha_2, R2_pow_2=R2_pow_2,
    lambda_L_3=lambda_L_3, R2_exp_3=R2_exp_3, alpha_3=alpha_3, R2_pow_3=R2_pow_3,
    lambda_L_GGE=lambda_L_GGE, R2_exp_GGE=R2_exp_GGE,
    alpha_GGE=alpha_GGE, R2_pow_GGE=R2_pow_GGE,
    lambda_max=lambda_max, R2_best=R2_best,
    # Scrambling time
    t_scr_1=t_scr_1, t_scr_cross=t_scr_cross, t_scr_GGE=t_scr_GGE,
    t_transit=t_transit,
    # SFF
    t_sff=t_sff, K_t=K_t,
    K_early=K_early, K_late=K_late, K_plateau=K_plateau,
    slope_actual=slope_actual, slope_GUE=slope_GUE,
    # Probe modes
    W_mode=W_mode, V_mode=V_mode,
    W2_mode=W2_mode, V2_mode=V2_mode,
)
print(f"  Saved: {output_path}")

# =====================================================================
#  11. PLOTTING
# =====================================================================

print("\n" + "=" * 72)
print("GENERATING PLOT")
print("=" * 72)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# --- Panel (a): OTOC C(t) log scale, all probes ---
ax1 = fig.add_subplot(gs[0, 0])
mask_pos_1 = C_infT > 0
mask_pos_2 = C_cross_infT > 0
mask_pos_3 = C_B2B1_infT > 0
mask_pos_G = C_GGE > 0

if np.any(mask_pos_1):
    ax1.semilogy(t_array[mask_pos_1], C_infT[mask_pos_1], 'b-', lw=1.5,
                 label=f'$n_1$-$n_2$ (B2-B2)')
if np.any(mask_pos_2):
    ax1.semilogy(t_array[mask_pos_2], C_cross_infT[mask_pos_2], 'r-', lw=1.5,
                 label=f'$n_4$-$n_5$ (B1-B3)')
if np.any(mask_pos_3):
    ax1.semilogy(t_array[mask_pos_3], C_B2B1_infT[mask_pos_3], 'g-', lw=1.5,
                 label=f'$n_0$-$n_4$ (B2-B1)')

ax1.set_xlabel('$t$ ($M_{KK}^{-1}$)')
ax1.set_ylabel('$C(t)$')
ax1.set_title('(a) OTOC $C(t)$ [$T = \\infty$ in sector]')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# --- Panel (b): OTOC log-log with power-law fit ---
ax2 = fig.add_subplot(gs[0, 1])
if np.any(mask_pos_1):
    t_pos = t_array[mask_pos_1]
    C_pos = C_infT[mask_pos_1]
    ax2.loglog(t_pos, C_pos, 'b-', lw=1.5, label='Data')
    # Overlay power-law fit
    if info_1.get('status') == 'FITTED':
        t_fit = info_1['t_fit']
        C_pow_fit = info_1['B_pow'] * t_fit**info_1['alpha_pow']
        ax2.loglog(t_fit, C_pow_fit, 'k--', lw=1.0,
                   label=f'$t^{{{alpha_1:.2f}}}$ ($R^2$={R2_pow_1:.3f})')

ax2.set_xlabel('$t$ ($M_{KK}^{-1}$)')
ax2.set_ylabel('$C(t)$')
ax2.set_title('(b) Power-law fit (B2-B2)')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3, which='both')

# --- Panel (c): OTOC semi-log with exponential fit attempt ---
ax3 = fig.add_subplot(gs[0, 2])
if np.any(mask_pos_1):
    ax3.semilogy(t_array[mask_pos_1], C_infT[mask_pos_1], 'b-', lw=1.5, label='Data')
    if info_1.get('status') == 'FITTED':
        t_fit = info_1['t_fit']
        C_exp_fit = info_1['A_exp'] * np.exp(2 * info_1['lambda_L_raw'] * t_fit)
        ax3.semilogy(t_fit, C_exp_fit, 'r--', lw=1.0,
                     label=f'exp($2\\lambda_L t$), $\\lambda_L$={lambda_L_1:.4f}\n'
                           f'$R^2$={R2_exp_1:.3f}')

ax3.set_xlabel('$t$ ($M_{KK}^{-1}$)')
ax3.set_ylabel('$C(t)$')
ax3.set_title('(c) Exponential fit attempt (B2-B2)')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# --- Panel (d): OTOC at T_GGE ---
ax4 = fig.add_subplot(gs[1, 0])
if np.any(mask_pos_G):
    ax4.semilogy(t_array[mask_pos_G], C_GGE[mask_pos_G], 'b-', lw=1.5,
                 label=f'$T = T_{{GGE}}$ = {T_GGE:.3f}')
if np.any(mask_pos_1):
    ax4.semilogy(t_array[mask_pos_1], C_infT[mask_pos_1], 'b--', lw=0.8,
                 alpha=0.5, label=f'$T = \\infty$')  # (local)

ax4.set_xlabel('$t$ ($M_{KK}^{-1}$)')
ax4.set_ylabel('$C(t)$')
ax4.set_title(f'(d) OTOC at $T_{{GGE}}$ = {T_GGE:.3f} $M_{{KK}}$')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# --- Panel (e): Spectral form factor ---
ax5 = fig.add_subplot(gs[1, 1])
ax5.semilogy(t_sff * J_scale, K_t, 'b-', lw=0.5, alpha=0.8)
ax5.axhline(y=K_plateau, color='r', ls='--', lw=1.0, label=f'$1/d$ = {K_plateau:.4f}')
ax5.set_xlabel('$t \\cdot J$')
ax5.set_ylabel('$K(t)$')
ax5.set_title('(e) Spectral form factor')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)
ax5.set_ylim(K_plateau * 0.1, 1.2)

# --- Panel (f): Summary table ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')

summary_text = (
    f"GATE: OTOC-NPAIR3-65\n"
    f"VERDICT: {gate_verdict}\n"
    f"{'─'*35}\n"
    f"N_pair = {N_pair}, dim = {dim}\n"
    f"{'─'*35}\n"
    f"Probe 1 (B2-B2):\n"
    f"  lambda_L = {lambda_L_1:.4f}, R2_exp = {R2_exp_1:.4f}\n"
    f"  alpha = {alpha_1:.3f}, R2_pow = {R2_pow_1:.4f}\n"
    f"{'─'*35}\n"
    f"Probe 2 (B1-B3):\n"
    f"  lambda_L = {lambda_L_2:.4f}, R2_exp = {R2_exp_2:.4f}\n"
    f"  alpha = {alpha_2:.3f}, R2_pow = {R2_pow_2:.4f}\n"
    f"{'─'*35}\n"
    f"MSS bound: {lambda_MSS:.4f} M_KK\n"
    f"t_scr / t_transit = {t_scr_1 / t_transit:.0f}x\n"
    f"{'─'*35}\n"
    f"SFF: K_late/K_plateau = {K_late/K_plateau:.2f}\n"
    f"{'─'*35}\n"
    f"{gate_reason}"
)

ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle('S65 OTOC-NPAIR3-65: OTOC for $N_{pair}$=3 Pairing-Only Sector',
             fontsize=14, fontweight='bold')

plot_path = os.path.join(data_dir, 's65_otoc_npair3.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

plt.close(fig)

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
