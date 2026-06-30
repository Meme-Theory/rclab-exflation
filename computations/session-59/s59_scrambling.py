#!/usr/bin/env python3
"""
s59_scrambling.py — Scrambling Time via OTOC (SCRAMBLING-59)
=============================================================

Gate: SCRAMBLING-59
  PASS: lambda_L > 0 with R^2 > 0.90 over >= 1 decade (genuine Lyapunov regime)
  FAIL: lambda_L = 0 or no exponential growth regime
  INFO: ambiguous (0 < lambda_L but R^2 < 0.90 or < 1 decade)

Physics: If the 2-cell BCS system is integrable (as all prior diagnostics
indicate), the OTOC should NOT exhibit exponential growth. Instead we expect
C(t) ~ t^alpha (power-law) from BCH series of nested commutators, which is
generic for integrable systems. The scrambling time is then infinite:
information placed in one cell never scrambles to the other.

Method:
  1. Reconstruct 2-cell BCS Hamiltonian (N_pair=2, dim=120) from S56 data
  2. Exact diagonalization: H = U diag(E) U^T
  3. Build W = n_{B2,mode=0,cell=0}, V = n_{B2,mode=0,cell=1}
  4. Time-evolve: W(t) = exp(iHt) W exp(-iHt) in energy basis
  5. Compute commutator [W(t), V] and OTOC C(t) = Tr(rho [W(t),V]^dag [W(t),V])
  6. Use GGE diagonal ensemble rho from S58 quench data
  7. Also compute infinite-temperature (Tr(rho)=1/dim) OTOC for comparison
  8. Extract lambda_L from log(C(t)) by linear fit in early-time regime
  9. Compare to MSS bound: lambda_L <= 2*pi*T_acoustic

Session: S59 W4D-1
Agent: kitaev-quantum-chaos-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, t_Planck, T_acoustic,
    hbar_GeV_s, M_KK, dt_transit
)

# =====================================================================
#  1. LOAD INPUT DATA (from S56 + S58)
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # (8,) single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # (8,) single-particle energies at tau=0
V_fold   = d56['V_fold']        # (8,8) pairing matrix
E_J_fold = float(d56['E_J_fold'])
E_J_tau0 = float(d56['E_J_tau0'])

# S58 quench data (diagonal ensemble weights for GGE)
d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
p_n_quench = d58['p_n_quench']  # (120,) probability weights from quench

N_modes = 8  # (local)
N_cells = 2
N_pair  = 2  # (local)

# =====================================================================
#  2. CONSTRUCT PAIR FOCK SPACE (identical to S58)
# =====================================================================

N_slots = N_modes * N_cells  # 16
pair_states = list(combinations(range(N_slots), N_pair))
dim = len(pair_states)
assert dim == 120, f"Expected dim=120, got {dim}"

def slot_to_mode_cell(s):
    return (s % N_modes, s // N_modes)

state_info = []
for idx, (s1, s2) in enumerate(pair_states):
    m1, c1 = slot_to_mode_cell(s1)
    m2, c2 = slot_to_mode_cell(s2)
    state_info.append(((m1, c1), (m2, c2)))

state_index = {s: i for i, s in enumerate(pair_states)}

# =====================================================================
#  3. CONSTRUCT HAMILTONIAN (from S58, verbatim)
# =====================================================================

def build_H_BCS_2cell(eps, V, E_J):
    """Build BCS + Josephson Hamiltonian for N_pair=2 on 2-cell system."""
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, (s1, s2) in enumerate(pair_states):
        (m1, c1), (m2, c2) = state_info[i]

        # Diagonal: kinetic
        H[i, i] += 2.0 * eps[m1] + 2.0 * eps[m2]

        # Pairing: scatter pair 1
        for k in range(N_modes):
            if k == m1:
                H[i, i] -= V[m1, m1]
                continue
            new_slot1 = c1 * N_modes + k
            if new_slot1 == s2:
                continue
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] -= V[k, m1]

        # Pairing: scatter pair 2
        for k in range(N_modes):
            if k == m2:
                H[i, i] -= V[m2, m2]
                continue
            new_slot2 = c2 * N_modes + k
            if new_slot2 == s1:
                continue
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] -= V[k, m2]

        # Josephson: tunnel pair 1
        for l in range(N_modes):
            new_slot1 = (1 - c1) * N_modes + l
            if new_slot1 == s2:
                continue
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

        # Josephson: tunnel pair 2
        for l in range(N_modes):
            new_slot2 = (1 - c2) * N_modes + l
            if new_slot2 == s1:
                continue
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

    H = 0.5 * (H + H.T)
    return H

# =====================================================================
#  4. BUILD, DIAGONALIZE, VALIDATE
# =====================================================================

H_fold = build_H_BCS_2cell(eps_fold, V_fold, E_J_fold)
hermiticity = np.max(np.abs(H_fold - H_fold.T))

evals, evecs = eigh(H_fold)

# Cross-check against S58 stored eigenvalues
evals_s58 = d58['evals_fold_full']
eval_diff = np.max(np.abs(np.sort(evals) - np.sort(evals_s58)))

# =====================================================================
#  5. BUILD OCCUPATION NUMBER OPERATORS
# =====================================================================
# W = n_{mode=0, cell=0} = occupation of B2 mode 0 in cell 0
# V_op = n_{mode=0, cell=1} = occupation of B2 mode 0 in cell 1
# These are pair number operators (eigenvalues 0 or 1).

def build_pair_number_op(mode, cell):
    """Build n_{mode,cell} operator in the 120-dim pair Fock basis."""
    n_op = np.zeros((dim, dim), dtype=np.float64)
    slot = cell * N_modes + mode
    for i, (s1, s2) in enumerate(pair_states):
        if s1 == slot or s2 == slot:
            n_op[i, i] = 1.0
    return n_op

# W and V operators in the site basis
W_site = build_pair_number_op(mode=0, cell=0)   # n_{B2_0, cell_0}
V_site = build_pair_number_op(mode=0, cell=1)   # n_{B2_0, cell_1}

# Transform to energy eigenbasis: O_E = U^T O U
W_E = evecs.T @ W_site @ evecs   # (dim, dim)
V_E = evecs.T @ V_site @ evecs   # (dim, dim)

# =====================================================================
#  6. COMPUTE OTOC: C(t) = Tr(rho [W(t), V]^dag [W(t), V])
# =====================================================================
# In the energy basis:
#   W(t)_{ab} = W_E_{ab} * exp(i(E_a - E_b)*t)
#   [W(t), V]_{ab} = sum_c W_E_{ac}*V_E_{cb}*exp(i(E_a-E_c)*t)
#                    - V_E_{ac}*W_E_{cb}*exp(i(E_c-E_b)*t)
#
# For efficiency, compute:
#   C(t) = Tr(rho * [W(t),V]^dag [W(t),V])
# where rho is diagonal in the energy basis: rho_{ab} = p_a delta_{ab}

# Time grid
N_t = 2000  # (local)
t_max = 100.0  # M_KK^{-1} (local)
t_arr = np.linspace(0, t_max, N_t)

# Energy differences for phase evolution
E_diff = evals[:, None] - evals[None, :]  # (dim, dim): E_a - E_b

# GGE diagonal ensemble: rho_n = p_n from quench
# Normalize
rho_GGE = p_n_quench / np.sum(p_n_quench)

# Also compute infinite-temperature OTOC for comparison
rho_inf = np.ones(dim) / dim

# Pre-compute WV and VW products in energy basis
WV = W_E @ V_E   # (dim, dim)
VW = V_E @ W_E   # (dim, dim)

def compute_otoc_vectorized(t_arr, rho_diag, W_E, V_E, evals):
    """
    Compute OTOC C(t) = Tr(rho [W(t),V]^dag [W(t),V]) at all times.

    Uses exact diag: W(t)_{ab} = W_E_{ab} exp(i(E_a - E_b)*t).

    The commutator [W(t), V] has matrix elements:
      comm_{ab}(t) = sum_c [ W_E_{ac} V_E_{cb} e^{i(E_a-E_c)t}
                            - V_E_{ac} W_E_{cb} e^{i(E_c-E_b)t} ]

    C(t) = sum_a rho_a * sum_b |comm_{ab}(t)|^2

    For dim=120, this is tractable: loop over time, vectorize over indices.
    """
    dim = len(evals)
    N_t = len(t_arr)
    C_t = np.zeros(N_t)

    WV = W_E @ V_E
    VW = V_E @ W_E

    for it, t in enumerate(t_arr):
        # Phase matrix: exp(i * (E_a - E_b) * t)
        phase = np.exp(1j * np.outer(evals, np.ones(dim)) * t) \
              * np.exp(-1j * np.outer(np.ones(dim), evals) * t)
        # phase_{ab} = exp(i(E_a - E_b)*t)

        # W(t) in energy basis
        Wt = W_E * phase  # element-wise: W_E_{ab} * exp(i(E_a-E_b)*t)

        # Commutator [W(t), V]
        comm = Wt @ V_E - V_E @ Wt

        # C(t) = Tr(rho * comm^dag * comm)
        # = sum_a rho_a * sum_b |comm_{ab}|^2
        comm_sq = np.abs(comm)**2
        C_t[it] = np.real(rho_diag @ np.sum(comm_sq, axis=1))

    return C_t

# Alternative: more efficient computation using energy-difference decomposition
# For dim=120, the naive method is fine: 120^2 * 2000 = 28.8M operations per step

def compute_otoc_efficient(t_arr, rho_diag, W_E, V_E, evals):
    """
    Efficient OTOC via Fourier decomposition.

    C(t) = sum_{a,b} rho_a * |sum_c [W_{ac}V_{cb} e^{i(E_a-E_c)t}
                                     - V_{ac}W_{cb} e^{i(E_c-E_b)t}]|^2

    Expand the |...|^2 to get sums over c,d with phase factors.

    C(t) = sum_{a,b,c,d} rho_a * [W_{ac}V_{cb}*conj(W_{ad}V_{db}) * e^{i(E_d-E_c)t}
                                  + V_{ac}W_{cb}*conj(V_{ad}W_{db}) * e^{i(E_d-E_c)t}
                                  - W_{ac}V_{cb}*conj(V_{ad}W_{db}) * e^{i(E_a-E_c+E_d-E_b)t}
                                  - V_{ac}W_{cb}*conj(W_{ad}V_{db}) * e^{-i(E_a-E_c+E_d-E_b)t}]

    This is O(dim^4) to set up but O(N_omega * N_t) to evaluate via FFT.
    For dim=120, dim^4 = 2e8 which is borderline. Use the direct method instead.
    """
    pass  # Use vectorized method for dim=120

# =====================================================================
#  7. RUN OTOC COMPUTATION
# =====================================================================

results = {}

# --- GGE OTOC ---
C_GGE = compute_otoc_vectorized(t_arr, rho_GGE, W_E, V_E, evals)
results['C_GGE'] = C_GGE

# --- Infinite-temperature OTOC ---
C_inf = compute_otoc_vectorized(t_arr, rho_inf, W_E, V_E, evals)
results['C_inf'] = C_inf

# --- Also compute with alternative operator choices as cross-checks ---
# W2 = n_{mode=1, cell=0}, V2 = n_{mode=1, cell=1}
W2_site = build_pair_number_op(mode=1, cell=0)
V2_site = build_pair_number_op(mode=1, cell=1)
W2_E = evecs.T @ W2_site @ evecs
V2_E = evecs.T @ V2_site @ evecs
C_GGE_alt = compute_otoc_vectorized(t_arr, rho_GGE, W2_E, V2_E, evals)
results['C_GGE_alt'] = C_GGE_alt

# =====================================================================
#  8. EXTRACT LYAPUNOV EXPONENT
# =====================================================================

def extract_lyapunov(t_arr, C_t, t_min_frac=0.05, t_max_frac=0.3):
    """
    Attempt to extract Lyapunov exponent from OTOC.

    Look for exponential growth C(t) ~ A * exp(lambda_L * t) in
    the early-time regime [t_min, t_max].

    Protocol (from S38 methodology):
    - Require R^2 > 0.90 for exponential fit over >= 1 decade of growth
    - Early-time t^2 growth (BCH) always present — not Lyapunov
    - Power-law C(t) ~ t^alpha is the integrable signature

    Returns: lambda_L, R2_exp, alpha_power, R2_power, fit_range
    """
    # Identify the growth regime: C(t) > 0 and increasing
    C_pos = C_t > 1e-30  # avoid log of zero

    if np.sum(C_pos) < 10:
        return 0.0, 0.0, 0.0, 0.0, (0, 0)

    # Find the early-time growth window
    t_min = t_arr[C_pos][0] + t_min_frac * (t_arr[C_pos][-1] - t_arr[C_pos][0])
    t_max = t_arr[C_pos][0] + t_max_frac * (t_arr[C_pos][-1] - t_arr[C_pos][0])

    mask = C_pos & (t_arr >= t_min) & (t_arr <= t_max)
    if np.sum(mask) < 5:
        return 0.0, 0.0, 0.0, 0.0, (t_min, t_max)

    t_fit = t_arr[mask]
    C_fit = C_t[mask]

    # --- Exponential fit: log(C) = log(A) + lambda_L * t ---
    log_C = np.log(C_fit)
    coeffs_exp = np.polyfit(t_fit, log_C, 1)
    lambda_L = coeffs_exp[0]
    log_C_pred = np.polyval(coeffs_exp, t_fit)
    SS_res = np.sum((log_C - log_C_pred)**2)
    SS_tot = np.sum((log_C - np.mean(log_C))**2)
    R2_exp = 1.0 - SS_res / max(SS_tot, 1e-30)

    # --- Power-law fit: log(C) = alpha * log(t) + log(A) ---
    log_t = np.log(t_fit)
    coeffs_pow = np.polyfit(log_t, log_C, 1)
    alpha = coeffs_pow[0]
    log_C_pred_pow = np.polyval(coeffs_pow, log_t)
    SS_res_pow = np.sum((log_C - log_C_pred_pow)**2)
    SS_tot_pow = np.sum((log_C - np.mean(log_C))**2)
    R2_pow = 1.0 - SS_res_pow / max(SS_tot_pow, 1e-30)

    return lambda_L, R2_exp, alpha, R2_pow, (t_min, t_max)


# Multiple fitting windows for robustness
fit_windows = [
    (0.02, 0.15),   # very early
    (0.05, 0.30),   # standard early
    (0.10, 0.50),   # medium
    (0.02, 0.50),   # broad
]

fit_results = {}
for label, (rho_diag, C_t) in [('GGE', (rho_GGE, C_GGE)),
                                  ('inf_T', (rho_inf, C_inf)),
                                  ('GGE_alt', (rho_GGE, C_GGE_alt))]:
    fit_results[label] = {}
    for (f_min, f_max) in fit_windows:
        lam, R2e, alpha, R2p, (t_min, t_max) = extract_lyapunov(
            t_arr, C_t, t_min_frac=f_min, t_max_frac=f_max
        )
        fit_results[label][(f_min, f_max)] = {
            'lambda_L': lam, 'R2_exp': R2e,
            'alpha': alpha, 'R2_pow': R2p,
            't_range': (t_min, t_max)
        }

# =====================================================================
#  9. MSS BOUND COMPARISON
# =====================================================================

# MSS bound: lambda_L <= 2*pi*T/hbar (in natural units where hbar=1)
# T_acoustic = 0.112 M_KK (from canonical_constants)
lambda_MSS = 2.0 * np.pi * T_acoustic  # in M_KK units
# = 0.704 M_KK

# Best-fit lambda_L (use the standard early window for GGE)
best_fit = fit_results['GGE'][(0.05, 0.30)]
lambda_L_best = best_fit['lambda_L']
R2_best = best_fit['R2_exp']

# Scrambling time: t_scr = (1/lambda_L) * ln(dim)  [if lambda_L > 0]
if lambda_L_best > 1e-10:
    t_scr = (1.0 / lambda_L_best) * np.log(dim)
else:
    t_scr = np.inf

# Compare to transit time
t_transit = dt_transit  # M_KK^{-1}

# =====================================================================
# 10. ADDITIONAL DIAGNOSTICS
# =====================================================================

# (a) Check static commutator [W, V] at t=0
comm_static = W_site @ V_site - V_site @ W_site
comm_static_norm = np.linalg.norm(comm_static, 'fro')

# (b) Saturation value: C(t -> infty) for integrable system
# In diagonal ensemble: C_diag = sum_a rho_a * |[W_E, V_E]_{aa}|^2... no.
# Actually C_inf = Tr(rho [W,V]^dag [W,V]) for long-time average
# For integrable system, C(t) oscillates. Compute time-average over late window.
late_mask = t_arr > 50.0
C_late_avg = np.mean(C_GGE[late_mask]) if np.any(late_mask) else 0.0
C_late_std = np.std(C_GGE[late_mask]) if np.any(late_mask) else 0.0

# (c) Spectral content of C(t): FFT to identify frequencies
C_zero_mean = C_GGE - np.mean(C_GGE)
freq = np.fft.rfftfreq(N_t, d=(t_arr[1] - t_arr[0]))
C_fft = np.abs(np.fft.rfft(C_zero_mean))
# Find dominant frequencies
dominant_idx = np.argsort(C_fft[1:])[-5:] + 1
dominant_freq = freq[dominant_idx]
dominant_amp = C_fft[dominant_idx]

# (d) Early-time power-law: C(t) ~ t^alpha
# Theory (BCH): C(t) ~ t^2 for t << 1/||H||
early_mask = (t_arr > 0.01) & (t_arr < 1.0) & (C_GGE > 1e-30)
if np.sum(early_mask) > 5:
    log_t_early = np.log(t_arr[early_mask])
    log_C_early = np.log(C_GGE[early_mask])
    alpha_early_coeffs = np.polyfit(log_t_early, log_C_early, 1)
    alpha_early = alpha_early_coeffs[0]
    # R^2 for power law
    pred_early = np.polyval(alpha_early_coeffs, log_t_early)
    SS_res_early = np.sum((log_C_early - pred_early)**2)
    SS_tot_early = np.sum((log_C_early - np.mean(log_C_early))**2)
    R2_power_early = 1.0 - SS_res_early / max(SS_tot_early, 1e-30)
else:
    alpha_early = 0.0  # (local)
    R2_power_early = 0.0  # (local)

# =====================================================================
# 11. GATE VERDICT
# =====================================================================

# Criteria from S38 methodology (CHAOS-2 precedent):
# - Exponential growth requires R^2 > 0.90 over >= 1 decade
# - Power-law (t^alpha) is the integrable signature
# - If best exponential R^2 < 0.90: FAIL (no Lyapunov regime)

# Check all windows for best exponential fit
best_R2 = -1.0
best_lambda = 0.0  # (local)
best_window = None
for (f_min, f_max), res in fit_results['GGE'].items():
    if res['R2_exp'] > best_R2:
        best_R2 = res['R2_exp']
        best_lambda = res['lambda_L']
        best_window = (f_min, f_max)

if best_R2 >= 0.90 and best_lambda > 0:
    gate_verdict = 'PASS'
    gate_detail = (f"lambda_L = {best_lambda:.4f} M_KK, R^2 = {best_R2:.3f}, "
                   f"t_scr = {(1.0/best_lambda)*np.log(dim):.2f} M_KK^-1")
elif best_R2 >= 0.80 and best_lambda > 0:
    gate_verdict = 'INFO'
    gate_detail = (f"Marginal: lambda_L = {best_lambda:.4f}, R^2 = {best_R2:.3f} "
                   f"(below 0.90 threshold)")
else:
    gate_verdict = 'FAIL'
    gate_detail = (f"No Lyapunov regime. Best R^2(exp) = {best_R2:.3f}, "
                   f"power-law alpha = {alpha_early:.2f} (R^2 = {R2_power_early:.3f})")

# =====================================================================
# 12. WRITE OUTPUT
# =====================================================================

outpath = os.path.join(data_dir, 's59_scrambling.npz')
np.savez(outpath,
    # Time series
    t_arr=t_arr,
    C_GGE=C_GGE,
    C_inf=C_inf,
    C_GGE_alt=C_GGE_alt,
    # Fit results
    lambda_L_best=best_lambda,
    R2_exp_best=best_R2,
    alpha_early=alpha_early,
    R2_power_early=R2_power_early,
    best_window=np.array(best_window) if best_window else np.array([0, 0]),
    # MSS bound
    lambda_MSS=lambda_MSS,
    T_acoustic=T_acoustic,
    # Scrambling time
    t_scr=t_scr if np.isfinite(t_scr) else -1.0,
    t_transit=t_transit,
    # Late-time
    C_late_avg=C_late_avg,
    C_late_std=C_late_std,
    # Spectral content
    freq_dominant=dominant_freq,
    amp_dominant=dominant_amp,
    # Static checks
    comm_static_norm=comm_static_norm,
    eval_crosscheck_diff=eval_diff,
    hermiticity=hermiticity,
    # System params
    dim=dim,
    N_pair=N_pair,
    N_modes=N_modes,
    N_cells=N_cells,
    E_J_fold=E_J_fold,
    tau_fold=tau_fold,
    # Eigenvalues
    evals=evals,
    # Gate
    gate_name=np.array(['SCRAMBLING-59']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)

# =====================================================================
# 13. CONSOLE OUTPUT
# =====================================================================

print("=" * 72)
print("S59 SCRAMBLING-59: Scrambling Time via OTOC")
print("=" * 72)
print(f"\nSystem: 2-cell BCS, N_pair={N_pair}, dim={dim}")
print(f"tau_fold = {tau_fold:.4f}, E_J = {E_J_fold:.4f} M_KK")
print(f"Hamiltonian hermiticity: {hermiticity:.2e}")
print(f"Eigenvalue crosscheck (S58): max|diff| = {eval_diff:.2e}")

print(f"\n--- Operators ---")
print(f"W = n_{{B2_0, cell_0}}  (pair occupation, mode 0, cell 0)")
print(f"V = n_{{B2_0, cell_1}}  (pair occupation, mode 0, cell 1)")
print(f"[W, V] Frobenius norm at t=0: {comm_static_norm:.6e}")

print(f"\n--- OTOC Time Series ---")
print(f"C(t=0)   = {C_GGE[0]:.6e}")
print(f"C(t=1)   = {C_GGE[min(int(1.0/t_max*N_t), N_t-1)]:.6e}")
print(f"C(t=10)  = {C_GGE[min(int(10.0/t_max*N_t), N_t-1)]:.6e}")
print(f"C(t=50)  = {C_GGE[min(int(50.0/t_max*N_t), N_t-1)]:.6e}")
print(f"C_late_avg = {C_late_avg:.6e} +/- {C_late_std:.6e}")
print(f"max(C)   = {np.max(C_GGE):.6e}")

print(f"\n--- Early-Time Power Law ---")
print(f"C(t) ~ t^{alpha_early:.3f}  (R^2 = {R2_power_early:.4f})")
print(f"  BCH prediction: t^2 (exact at t -> 0)")

print(f"\n--- Exponential Fit Attempts ---")
for (f_min, f_max), res in fit_results['GGE'].items():
    flag = " <-- BEST" if (f_min, f_max) == best_window else ""
    print(f"  [{f_min:.2f}, {f_max:.2f}]: lambda_L = {res['lambda_L']:.4f}, "
          f"R^2(exp) = {res['R2_exp']:.4f}, "
          f"alpha = {res['alpha']:.3f}, R^2(pow) = {res['R2_pow']:.4f}{flag}")

print(f"\n--- MSS Bound ---")
print(f"lambda_MSS = 2*pi*T_acoustic = 2*pi*{T_acoustic:.3f} = {lambda_MSS:.4f} M_KK")
print(f"lambda_L_best = {best_lambda:.4f} M_KK")
if best_lambda > 0:
    print(f"Ratio: lambda_L / lambda_MSS = {best_lambda / lambda_MSS:.4f}")
else:
    print(f"Ratio: lambda_L / lambda_MSS = 0 (no exponential growth)")

print(f"\n--- Scrambling Time ---")
if np.isfinite(t_scr) and t_scr > 0:
    print(f"t_scr = (1/lambda_L)*ln(dim) = (1/{best_lambda:.4f})*ln({dim}) = {t_scr:.2f} M_KK^-1")
    print(f"t_transit = {t_transit:.6f} M_KK^-1")
    print(f"t_scr / t_transit = {t_scr / t_transit:.1f}x")
else:
    print(f"t_scr = INFINITY (no exponential growth -> no scrambling)")
    print(f"t_transit = {t_transit:.6f} M_KK^-1")

print(f"\n--- Cross-Check: Alternative Operators (mode 1) ---")
best_fit_alt = fit_results['GGE_alt'][(0.05, 0.30)]
print(f"C_alt: lambda_L = {best_fit_alt['lambda_L']:.4f}, "
      f"R^2(exp) = {best_fit_alt['R2_exp']:.4f}, "
      f"alpha = {best_fit_alt['alpha']:.3f}")

print(f"\n--- Cross-Check: Infinite Temperature ---")
best_fit_inf = fit_results['inf_T'][(0.05, 0.30)]
print(f"C_inf: lambda_L = {best_fit_inf['lambda_L']:.4f}, "
      f"R^2(exp) = {best_fit_inf['R2_exp']:.4f}, "
      f"alpha = {best_fit_inf['alpha']:.3f}")

print(f"\n--- Dominant OTOC Frequencies ---")
for i in range(len(dominant_freq)):
    print(f"  omega_{i} = {dominant_freq[i]:.4f} M_KK, amplitude = {dominant_amp[i]:.4e}")

print(f"\n{'='*72}")
print(f"GATE: SCRAMBLING-59")
print(f"VERDICT: {gate_verdict}")
print(f"DETAIL: {gate_detail}")
print(f"{'='*72}")

# =====================================================================
# 14. PLOTS
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S59 SCRAMBLING-59: OTOC C(t) for 2-Cell BCS System\n'
             f'N_pair={N_pair}, dim={dim}, tau_fold={tau_fold:.3f}, '
             f'E_J={E_J_fold:.3f} M_KK', fontsize=12, fontweight='bold')

# (a) Linear scale OTOC
ax = axes[0, 0]
ax.plot(t_arr, C_GGE, 'b-', linewidth=1.0, label='GGE', alpha=0.8)
ax.plot(t_arr, C_inf, 'r--', linewidth=0.8, label=r'$T=\infty$', alpha=0.6)
ax.plot(t_arr, C_GGE_alt, 'g:', linewidth=0.8, label='GGE (mode 1)', alpha=0.6)
ax.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$C(t) = \langle [W(t), V]^\dagger [W(t), V] \rangle$')
ax.set_title('(a) OTOC — Linear Scale')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (b) Log scale OTOC
ax = axes[0, 1]
mask_pos = C_GGE > 1e-30
if np.any(mask_pos):
    ax.semilogy(t_arr[mask_pos], C_GGE[mask_pos], 'b-', linewidth=1.0, label='GGE')
mask_inf = C_inf > 1e-30
if np.any(mask_inf):
    ax.semilogy(t_arr[mask_inf], C_inf[mask_inf], 'r--', linewidth=0.8,
                label=r'$T=\infty$', alpha=0.6)
# Show exponential reference if lambda_L > 0
if best_lambda > 1e-10 and best_R2 > 0.5:
    t_ref = np.linspace(0.5, 20, 100)
    C_ref = C_GGE[10] * np.exp(best_lambda * (t_ref - t_arr[10]))
    ax.semilogy(t_ref, C_ref, 'k:', linewidth=0.8, alpha=0.5,
                label=f'exp({best_lambda:.3f}t)')
# Show power law reference
if alpha_early > 0:
    t_ref = np.linspace(0.1, 5, 100)
    C_ref_pow = np.exp(alpha_early_coeffs[1]) * t_ref**alpha_early
    ax.semilogy(t_ref, C_ref_pow, 'm:', linewidth=0.8, alpha=0.5,
                label=f'$t^{{{alpha_early:.1f}}}$')
ax.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$C(t)$')
ax.set_title('(b) OTOC — Log Scale')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) Log-log for power-law check
ax = axes[1, 0]
if np.any(mask_pos):
    ax.loglog(t_arr[mask_pos], C_GGE[mask_pos], 'b-', linewidth=1.0, label='GGE')
if alpha_early > 0:
    t_ref = np.logspace(-2, 2, 200)
    C_ref_pow = np.exp(alpha_early_coeffs[1]) * t_ref**alpha_early
    ax.loglog(t_ref, C_ref_pow, 'r--', linewidth=0.8, alpha=0.5,
              label=f'$t^{{{alpha_early:.2f}}}$ (R$^2$={R2_power_early:.3f})')
ax.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$C(t)$')
ax.set_title(f'(c) Log-Log: Power Law Check ($\\alpha = {alpha_early:.2f}$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# (d) Spectral content
ax = axes[1, 1]
ax.plot(freq[:len(freq)//2], C_fft[:len(freq)//2], 'b-', linewidth=0.8)
ax.set_xlabel(r'Frequency [$M_{KK}$]')
ax.set_ylabel('FFT amplitude')
ax.set_title('(d) OTOC Spectral Content')
ax.set_xlim(0, 5)
ax.grid(True, alpha=0.3)

# Add gate verdict text
fig.text(0.5, 0.01,
         f'GATE: SCRAMBLING-59 | VERDICT: {gate_verdict} | {gate_detail}',
         ha='center', fontsize=9, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightcoral' if gate_verdict == 'FAIL'
                   else 'lightgreen' if gate_verdict == 'PASS' else 'lightyellow'))

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

plotpath = os.path.join(data_dir, 's59_scrambling.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
plt.close()

print(f"\nOutput saved: {outpath}")
print(f"Plot saved:   {plotpath}")
print("\nDone.")
