#!/usr/bin/env python3
"""
Session 35: ED-CORRECTED-35 -- Exact Diagonalization at Corrected Smooth-Wall DOS
==================================================================================
The BMF-35a exact diagonalization found E_cond = 0 (vacuum ground state) at
rho = 8.81 per mode (step-function wall with old impedance). The corrected
smooth-wall van Hove DOS gives rho = 14.02/mode (VH-IMP-35a), with multi-sector
factor rho = 14.66/mode.

At rho = 14.02, the mean-field Thouless M_max = 1.445 > 1.0 (PASS).
The DECISIVE QUESTION: Does the ED ground state shift from vacuum to paired
at this higher DOS?

COMPUTATION:
  1. Rerun 5-mode exact diagonalization (32-state Fock space) at:
     (a) rho = 14.02  (smooth wall, imp=1.0)          x  V_bare=0.057
     (b) rho = 14.66  (smooth wall, imp=1.0, ms=1.046) x  V_bare=0.057
     (c) rho = 14.02  (smooth wall, imp=1.0)          x  V_gap=0.086
     (d) rho = 14.66  (smooth wall, imp=1.0, ms=1.046) x  V_gap=0.086

  2. For each: E_0, E_cond, chi_pp(exact), chi_pp(MF), suppression ratio

GATE ED-CORRECTED-35 (pre-registered):
  PASS:  E_cond < 0 (paired ground state) at rho = 14.02, V_bare
  FAIL:  E_cond = 0 (vacuum ground state) at rho = 14.02, V_bare

Author: qa (quantum-acoustics-theorist), Session 35
Date: 2026-03-07
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigvals, eigh
from numpy.polynomial import polynomial as P
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 35: ED-CORRECTED-35 -- Exact Diag at Corrected Smooth-Wall DOS")
print("=" * 78)

# ======================================================================
#  Load data and reconstruct bare quantities
# ======================================================================

kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)
dphys_kosmann = np.load(os.path.join(SCRIPT_DIR, 's34a_dphys_kosmann.npz'),
                        allow_pickle=True)
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)
old_bmf = np.load(os.path.join(SCRIPT_DIR, 's35a_beyond_mean_field.npz'),
                  allow_pickle=True)

ETA_REG = 0.001
ti = 3  # tau = 0.20 (near fold at 0.190)

# Build V_5x5 in spinor eigenbasis from K_a_matrix
evals_raw = kosmann[f'eigenvalues_{ti}']
evecs_raw = kosmann[f'eigenvectors_{ti}']
si = np.argsort(evals_raw)
evals_s = evals_raw[si]

pos_idx = np.where(evals_s > 0)[0]
B1_idx = pos_idx[0:1]   # 1 mode (acoustic)
B2_idx = pos_idx[1:5]   # 4 modes (flat optical quartet)
idx_5 = np.concatenate([B2_idx, B1_idx])  # B2 first, then B1

# Build bare V_16x16 from Kosmann kernel
V_16 = np.zeros((16, 16))
for a in range(8):
    K = kosmann[f'K_a_matrix_{ti}_{a}']
    V_16 += np.abs(K)**2

V_5x5_bare = V_16[np.ix_(idx_5, idx_5)]
E_5 = evals_s[idx_5]

print(f"\nEigenvalues E_5 = {E_5}")
print(f"V(B2,B2) off-diag max (bare) = {np.max(V_5x5_bare[:4,:4] - np.diag(np.diag(V_5x5_bare[:4,:4]))):.6f}")
print(f"V(B2,B1) = {V_5x5_bare[0,4]:.6f}")
print(f"V(B1,B1) = {V_5x5_bare[4,4]:.2e}")

# V_5x5 at phi=gap: scale by retention ratio from D_phys Kosmann
# The retention ratio is V_at_gap / V_bare for the B2-B2 off-diagonal max
retention_ratio = float(dphys_kosmann['retention_ratio'])  # 1.504
V_at_gap_max = float(dphys_kosmann['V_at_gap'])           # 0.0859
V_bare_max = float(dphys_kosmann['V_bare'])                # 0.0572

print(f"\nD_phys retention ratio = {retention_ratio:.6f}")
print(f"V_at_gap (B2,B2 max) = {V_at_gap_max:.6f}")
print(f"V_bare   (B2,B2 max) = {V_bare_max:.6f}")

# Scale the V_5x5 by the retention ratio for the phi=gap case
# This is approximate: D_phys mixes SU(2) and C^2 generators differently.
# The B1-B2 coupling changes less (+/-3%), so we scale B2-B2 by retention_ratio
# and leave B1-B2 scaled by the measured B1-B2 ratio.
V_B1B2_at_gap = float(dphys_kosmann['V_B1B2_max_vs_phi'][13])  # phi=0.13
V_B1B2_bare = V_5x5_bare[0, 4]
B1B2_ratio = V_B1B2_at_gap / V_B1B2_bare if V_B1B2_bare > 1e-15 else 1.0

V_5x5_gap = V_5x5_bare.copy()
# Scale B2-B2 block (4x4)
V_5x5_gap[:4, :4] *= retention_ratio
# Scale B2-B1 coupling
V_5x5_gap[:4, 4] *= B1B2_ratio
V_5x5_gap[4, :4] *= B1B2_ratio
# B1-B1 stays zero (Trap 1, exact)

print(f"\nScaled V_5x5 (phi=gap):")
print(f"  V(B2,B2) off-diag max = {np.max(V_5x5_gap[:4,:4] - np.diag(np.diag(V_5x5_gap[:4,:4]))):.6f}")
print(f"  V(B2,B1) = {V_5x5_gap[0,4]:.6f}")
print(f"  B1B2_ratio = {B1B2_ratio:.6f}")

# DOS values from VH-IMP-35a arbiter
rho_smooth_per_mode = float(vh_arbiter['rho_at_physical'])     # 14.02
MULTI_SECTOR_FACTOR = 1.046
rho_with_ms = rho_smooth_per_mode * MULTI_SECTOR_FACTOR        # 14.66

print(f"\nDOS values:")
print(f"  rho_smooth (per mode) = {rho_smooth_per_mode:.4f}")
print(f"  rho_with_ms           = {rho_with_ms:.4f}")
print(f"  OLD rho (step+imp)    = {float(old_bmf['rho_full']):.4f}")


# ======================================================================
#  Thouless M_max computation
# ======================================================================

def compute_thouless(V, E, mu_val, rho_v, eta_reg=ETA_REG):
    """M_nm = V_nm * rho_m / (2|xi_m|). Return M_max, M_evals, M, G, |xi|."""
    n = len(E)
    xi = E - mu_val
    lam_min = np.min(np.abs(E))
    eta = max(eta_reg * lam_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)
    G = rho_v / (2.0 * abs_xi)
    M = np.zeros((n, n))
    for m in range(n):
        M[:, m] = V[:, m] * G[m]
    M_evals = eigvals(M)
    M_max = np.max(np.real(M_evals))
    return M_max, M_evals, M, G, abs_xi


# ======================================================================
#  Exact Diagonalization Function
# ======================================================================

def exact_diag_bcs(V_matrix, E_vec, mu_val, rho_v, label=""):
    """Run exact diagonalization of the 5-mode BCS pair Hamiltonian.

    The BCS reduced Hamiltonian in the pair occupation basis:
      |n_0, n_1, ..., n_4> with n_m in {0, 1} (pair occupied or empty)

      H = sum_m 2*xi_m * n_m - sum_{n!=m} V_nm * sqrt(rho_n * rho_m) * b_n^dag b_m

    The DOS factor enters as sqrt(rho_n * rho_m) in the pair scattering
    matrix element, because the gap equation involves rho_m and the pair
    Hamiltonian must reproduce M_nm = V_nm * rho_m / (2|xi_m|) upon
    linearization.

    Returns dict with all results.
    """
    n_modes = 5
    n_states = 2**n_modes
    xi = E_vec - mu_val

    # First compute mean-field Thouless for comparison
    M_max_mf, M_evals_mf, M_mf, G_mf, abs_xi_mf = compute_thouless(
        V_matrix, E_vec, mu_val, rho_v)

    N_eff = 4
    epsilon_mf = 1.0 - M_max_mf
    L_mf = 1.0 / abs(epsilon_mf) if abs(epsilon_mf) > 1e-15 else 1e15
    exp_param = M_max_mf**2 * L_mf / N_eff

    print(f"\n{'='*78}")
    print(f"EXACT DIAGONALIZATION: {label}")
    print(f"{'='*78}")
    print(f"  M_max (MF) = {M_max_mf:.10f}")
    print(f"  epsilon = 1 - M_max = {epsilon_mf:.10f}")
    if M_max_mf > 1.0:
        print(f"  *** M_max > 1: MEAN-FIELD BCS INSTABILITY ***")
    print(f"  L = 1/|epsilon| = {L_mf:.4f}")
    print(f"  Expansion parameter M^2*L/N_eff = {exp_param:.4f}")

    # Build Hamiltonian
    H = np.zeros((n_states, n_states))

    # Diagonal: kinetic energy
    for state in range(n_states):
        for m in range(n_modes):
            if state & (1 << m):
                H[state, state] += 2 * xi[m]

    # Off-diagonal: pair scattering
    for state in range(n_states):
        for n in range(n_modes):
            for m in range(n_modes):
                if n == m:
                    continue
                if V_matrix[n, m] < 1e-15:
                    continue
                # b_n^dag b_m: annihilate pair m, create pair n
                if (state & (1 << m)) and not (state & (1 << n)):
                    new_state = state ^ (1 << m) ^ (1 << n)
                    H[new_state, state] -= V_matrix[n, m] * np.sqrt(
                        rho_v[n] * rho_v[m])

    H = 0.5 * (H + H.T)  # Ensure Hermiticity

    # Diagonalize
    E_all, psi_all = np.linalg.eigh(H)
    E_gs = E_all[0]
    psi_gs = psi_all[:, 0]
    E_cond = E_gs  # Vacuum is state 0, energy = 0

    print(f"\n  Ground state energy E_0 = {E_gs:.10f}")
    print(f"  Vacuum energy           = 0.0")
    print(f"  Condensation energy E_cond = E_0 - E_vac = {E_cond:.10f}")

    if E_cond < -1e-10:
        print(f"  *** PAIRING IS ENERGETICALLY FAVORABLE ***")
        paired = True
    else:
        print(f"  Pairing NOT favorable: vacuum is ground state")
        paired = False

    # Pair occupation
    pair_occ = np.zeros(n_modes)
    for state in range(n_states):
        prob = abs(psi_gs[state])**2
        for m in range(n_modes):
            if state & (1 << m):
                pair_occ[m] += prob

    vacuum_overlap = abs(psi_gs[0])**2
    pair_content = 1.0 - vacuum_overlap

    print(f"\n  Pair occupations:")
    for m in range(n_modes):
        branch = "B2" if m < 4 else "B1"
        print(f"    <n_{m}> ({branch}) = {pair_occ[m]:.10f}")
    print(f"  |<vacuum|GS>|^2 = {vacuum_overlap:.10f}")
    print(f"  Pair content     = {pair_content:.10f}")

    # First 10 eigenvalues
    print(f"\n  Pair Hamiltonian spectrum (first 10):")
    for i in range(min(10, len(E_all))):
        print(f"    E[{i:2d}] = {E_all[i]:.10f}")

    # Exact pair susceptibility via quadratic fit to E(delta_ext)
    delta_ext_values = np.array([0, 1e-7, 2e-7, 5e-7, 1e-6, 2e-6, 5e-6, 1e-5])
    E_gs_vs_delta = []

    for d_ext in delta_ext_values:
        H_d = H.copy()
        for state in range(n_states):
            for m in range(n_modes):
                if not (state & (1 << m)):
                    new_state = state | (1 << m)
                    H_d[new_state, state] -= d_ext * np.sqrt(rho_v[m])
                    H_d[state, new_state] -= d_ext * np.sqrt(rho_v[m])
        H_d = 0.5 * (H_d + H_d.T)
        E_d = np.linalg.eigvalsh(H_d)
        E_gs_vs_delta.append(E_d[0])

    E_gs_vs_delta = np.array(E_gs_vs_delta)
    coeffs = P.polyfit(delta_ext_values, E_gs_vs_delta, 2)
    chi_pp_exact = -2 * coeffs[2]

    # Mean-field chi_pp = chi_0 * L where chi_0 = sum rho_m / (2|xi_m|)
    chi_0 = np.sum(rho_v / (2.0 * abs_xi_mf))
    if M_max_mf < 1.0:
        chi_pp_MF = chi_0 * L_mf
    else:
        # M_max > 1: MF chi diverges (instability). Use |L| for comparison
        chi_pp_MF = chi_0 * L_mf  # This will be negative (L < 0), or very large

    chi_ratio = chi_pp_exact / chi_pp_MF if abs(chi_pp_MF) > 1e-15 else np.nan

    print(f"\n  Pair susceptibility:")
    print(f"    chi_pp (exact, ED):   {chi_pp_exact:.6f}")
    print(f"    chi_0 (bare bubble):  {chi_0:.6f}")
    if M_max_mf < 1.0:
        print(f"    chi_pp (MF = chi_0*L): {chi_pp_MF:.6f}")
        print(f"    Ratio exact/MF:       {chi_ratio:.6f}")
        if chi_ratio < 1.0:
            print(f"    ED chi is {(1-chi_ratio)*100:.1f}% LOWER than MF.")
        else:
            print(f"    ED chi is {(chi_ratio-1)*100:.1f}% HIGHER than MF.")
    else:
        print(f"    chi_pp (MF): DIVERGENT (M_max > 1, instability)")
        print(f"    chi_pp (exact) finite at {chi_pp_exact:.4f} -- ED regularizes instability")

    # Also: check if any excited state is lower than vacuum
    # The vacuum state (state index 0) has energy H[0,0] = 0
    # But the ground state may be a superposition
    E_vacuum_diag = H[0, 0]
    print(f"\n  H[vacuum, vacuum] = {E_vacuum_diag:.10f} (diagonal element)")
    print(f"  E_gs = {E_gs:.10f}")
    if E_gs < E_vacuum_diag - 1e-10:
        print(f"  GS is BELOW diagonal vacuum entry by {E_vacuum_diag - E_gs:.10f}")

    # BCS gap equation check: if paired, extract Delta
    Delta_eff = np.zeros(n_modes)
    if paired:
        # Delta_m = sum_n V_mn * sqrt(rho_m * rho_n) * <b_n>
        # where <b_n> = sum_{states} psi_gs(state with n) * conj(psi_gs(state without n))
        # This is approximate; proper extraction needs anomalous correlator
        for m in range(n_modes):
            # Anomalous average <b_m> = sum_state psi_gs*(state ^ (1<<m)) * psi_gs(state)
            # where state has m occupied, state ^ (1<<m) has m empty
            b_m = 0.0
            for state in range(n_states):
                if state & (1 << m):
                    partner = state ^ (1 << m)
                    b_m += np.conj(psi_gs[partner]) * psi_gs[state]
            Delta_eff[m] = abs(b_m)
        print(f"\n  Anomalous correlator |<b_m>|:")
        for m in range(n_modes):
            branch = "B2" if m < 4 else "B1"
            print(f"    |<b_{m}>| ({branch}) = {Delta_eff[m]:.10f}")
        print(f"  Sum |<b_m>| = {np.sum(Delta_eff):.10f}")

    return {
        'label': label,
        'V_matrix': V_matrix,
        'E_vec': E_vec,
        'rho_v': rho_v,
        'M_max_mf': M_max_mf,
        'epsilon_mf': epsilon_mf,
        'L_mf': L_mf,
        'exp_param': exp_param,
        'E_gs': E_gs,
        'E_cond': E_cond,
        'paired': paired,
        'pair_occ': pair_occ,
        'vacuum_overlap': vacuum_overlap,
        'pair_content': pair_content,
        'E_spectrum': E_all[:20],
        'chi_pp_exact': chi_pp_exact,
        'chi_0': chi_0,
        'chi_pp_MF': chi_pp_MF,
        'chi_ratio': chi_ratio,
        'psi_gs': psi_gs,
        'Delta_eff': Delta_eff,
        'N_eff': N_eff,
    }


# ======================================================================
#  Run all 4 scenarios
# ======================================================================

mu = 0.0

scenarios = [
    # (label, V_matrix, rho_per_mode, description)
    ("A: rho=14.02, V_bare",   V_5x5_bare, rho_smooth_per_mode,
     "Smooth-wall VH, imp=1.0, bare spinor V"),
    ("B: rho=14.66, V_bare",   V_5x5_bare, rho_with_ms,
     "Smooth-wall VH, imp=1.0, ms=1.046, bare spinor V"),
    ("C: rho=14.02, V_gap",    V_5x5_gap,  rho_smooth_per_mode,
     "Smooth-wall VH, imp=1.0, phi=gap spinor V"),
    ("D: rho=14.66, V_gap",    V_5x5_gap,  rho_with_ms,
     "Smooth-wall VH, imp=1.0, ms=1.046, phi=gap spinor V"),
]

results = []
for label, V_mat, rho_pm, desc in scenarios:
    print(f"\n\n{'#'*78}")
    print(f"# SCENARIO {label}")
    print(f"# {desc}")
    print(f"# rho_per_mode = {rho_pm:.4f}")
    print(f"{'#'*78}")

    rho_v = np.array([rho_pm] * 4 + [1.0])  # B2 gets rho_pm, B1 gets 1.0
    res = exact_diag_bcs(V_mat, E_5, mu, rho_v, label=label)
    res['rho_per_mode'] = rho_pm
    res['description'] = desc
    results.append(res)


# ======================================================================
#  Cross-check: reproduce old BMF-35a result at rho=8.81
# ======================================================================

print(f"\n\n{'#'*78}")
print(f"# CROSS-CHECK: Reproduce old BMF-35a at rho=8.81")
print(f"{'#'*78}")

rho_old = float(old_bmf['rho_full'])
rho_v_old = np.array([rho_old] * 4 + [1.0])
res_old = exact_diag_bcs(V_5x5_bare, E_5, mu, rho_v_old,
                          label="XCHECK: rho=8.81 (old)")

print(f"\n  Cross-check against stored old results:")
print(f"    E_gs (new):     {res_old['E_gs']:.10f}")
print(f"    E_gs (stored):  {float(old_bmf['E_gs']):.10f}")
print(f"    chi_pp (new):   {res_old['chi_pp_exact']:.6f}")
print(f"    chi_pp (stored):{float(old_bmf['chi_pp_exact']):.6f}")
match_E = abs(res_old['E_gs'] - float(old_bmf['E_gs'])) < 1e-8
match_chi = abs(res_old['chi_pp_exact'] - float(old_bmf['chi_pp_exact'])) / max(abs(float(old_bmf['chi_pp_exact'])), 1e-15) < 0.01
print(f"    E_gs match: {'YES' if match_E else 'NO'}")
print(f"    chi_pp match (1%): {'YES' if match_chi else 'NO'}")


# ======================================================================
#  BMF corrections at the corrected DOS
# ======================================================================

print(f"\n\n{'='*78}")
print("BMF CORRECTIONS AT CORRECTED DOS (rho=14.02, V_bare)")
print(f"{'='*78}")

# Use scenario A results
res_A = results[0]
M_max_A = res_A['M_max_mf']

# GMB screening
gmb_factor = (4.0 / np.e)**(1.0/3.0)
M_max_GMB = M_max_A / gmb_factor
print(f"\n  GMB screening: {gmb_factor:.6f}")
print(f"    M_max -> {M_max_GMB:.6f} (from {M_max_A:.6f})")
if M_max_GMB >= 1.0:
    print(f"    STILL ABOVE 1.0 even with GMB")
else:
    print(f"    Falls below 1.0")

# Gorkov channel mixing
# Recompute M eigenvalues
_, M_evals_arr, M_mat_A, G_A, abs_xi_A = compute_thouless(
    V_5x5_bare, E_5, mu, np.array([rho_smooth_per_mode]*4 + [1.0]))
M_evals_sorted = sorted(np.real(M_evals_arr), reverse=True)

delta_Gorkov = 0.0
N_eff = 4
for i, ev in enumerate(M_evals_sorted):
    if i == 0:
        continue
    if abs(M_evals_sorted[0] - ev) > 1e-15:
        contrib = ev**2 / (M_evals_sorted[0] - ev)
        delta_Gorkov -= contrib / N_eff

print(f"\n  Gorkov channel mixing:")
print(f"    delta_M = {delta_Gorkov:.10f}")
print(f"    M_max + delta = {M_max_A + delta_Gorkov:.10f}")

# Eliashberg Z-factor
Z_factors = np.ones(5)
for n in range(5):
    Z_factors[n] = 1.0 + np.sum(V_5x5_bare[n, :] * G_A) / abs_xi_A[n]

M_Z = np.diag(1.0 / Z_factors) @ M_mat_A
M_max_Z = np.max(np.real(eigvals(M_Z)))

print(f"\n  Eliashberg Z-factors:")
for m in range(5):
    branch = "B2" if m < 4 else "B1"
    print(f"    Z({branch}[{m}]) = {Z_factors[m]:.6f}")
print(f"    M_max with Z: {M_max_Z:.6f}")

# N_eff analysis
print(f"\n  N_eff corridor analysis:")
print(f"    M_max (MF):  {M_max_A:.6f}")
print(f"    M_max (GMB): {M_max_GMB:.6f}")
print(f"    M_max (Z):   {M_max_Z:.6f}")
print(f"    For M_max > 1 after BMF:")
print(f"      GMB alone: {'PASS' if M_max_GMB > 1 else 'FAIL'}")
print(f"      Z alone:   {'PASS' if M_max_Z > 1 else 'FAIL'}")
print(f"      Combined (GMB+Z): ~{M_max_A / (gmb_factor * max(Z_factors)):.6f}")

# Key question: does ED agree with MF about having an instability?
print(f"\n  KEY COMPARISON:")
print(f"    MF says M_max = {M_max_A:.6f} {'> 1 (BCS INSTABILITY)' if M_max_A > 1 else '< 1 (no instability)'}")
print(f"    ED says E_cond = {res_A['E_cond']:.10f} {'< 0 (PAIRED)' if res_A['E_cond'] < -1e-10 else '>= 0 (VACUUM)'}")


# ======================================================================
#  Comprehensive Summary
# ======================================================================

print(f"\n\n{'='*78}")
print("COMPREHENSIVE SUMMARY: ALL SCENARIOS")
print(f"{'='*78}")

print(f"\n  {'Scenario':<30s}  {'rho/mode':>10s}  {'M_max(MF)':>10s}  {'E_cond':>12s}  {'chi_pp(ED)':>12s}  {'Paired?':>8s}")
print(f"  {'-'*30}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*8}")

for res in results:
    paired_str = "YES" if res['paired'] else "NO"
    print(f"  {res['label']:<30s}  {res['rho_per_mode']:10.4f}  {res['M_max_mf']:10.6f}  "
          f"{res['E_cond']:12.6f}  {res['chi_pp_exact']:12.4f}  {paired_str:>8s}")

# Old result for comparison
print(f"  {'OLD: rho=8.81, V_bare':<30s}  {rho_old:10.4f}  "
      f"{float(old_bmf['M_max_bare']):10.6f}  {float(old_bmf['E_cond']):12.6f}  "
      f"{float(old_bmf['chi_pp_exact']):12.4f}  {'NO':>8s}")


# ======================================================================
#  GATE ED-CORRECTED-35
# ======================================================================

print(f"\n\n{'='*78}")
print("GATE ED-CORRECTED-35")
print(f"{'='*78}")

# Pre-registered criterion: PASS if E_cond < 0 at rho=14.02, V_bare (Scenario A)
res_gate = results[0]  # Scenario A
E_cond_gate = res_gate['E_cond']

if E_cond_gate < -1e-10:
    verdict = "PASS"
    verdict_detail = (f"E_cond = {E_cond_gate:.10f} < 0: "
                     f"Paired ground state at corrected DOS.")
else:
    verdict = "FAIL"
    verdict_detail = (f"E_cond = {E_cond_gate:.10f} >= 0: "
                     f"Vacuum remains ground state even at corrected DOS.")

print(f"\n  Pre-registered criterion: E_cond < 0 at rho=14.02, V_bare")
print(f"  Result: E_cond = {E_cond_gate:.10f}")
print(f"\n  *** ED-CORRECTED-35: {verdict} ***")
print(f"  {verdict_detail}")

# Secondary checks
any_paired = any(r['paired'] for r in results)
if any_paired:
    paired_scenarios = [r['label'] for r in results if r['paired']]
    print(f"\n  Paired ground state found in: {paired_scenarios}")
else:
    print(f"\n  No paired ground state in ANY scenario.")

# Expansion parameter assessment
print(f"\n  Expansion parameters:")
for res in results:
    print(f"    {res['label']}: M^2*L/N_eff = {res['exp_param']:.4f} "
          f"{'(perturbative)' if res['exp_param'] < 1 else '(non-perturbative)'}")

# What this constrains
print(f"\n  CONSTRAINT MAP UPDATE:")
if verdict == "PASS":
    print(f"    ED CONFIRMS paired ground state at corrected smooth-wall DOS.")
    print(f"    The BCS mechanism SURVIVES exact treatment at N_eff=4.")
    print(f"    BMF-35a FAIL at old rho was due to insufficient DOS, not inherent suppression.")
    print(f"    Next gate: BMF corrections (GMB, Z-factor) at corrected DOS.")
else:
    print(f"    ED CONFIRMS vacuum ground state persists at corrected DOS.")
    if any(r['M_max_mf'] > 1.0 for r in results):
        print(f"    Despite MF M_max > 1, ED finds no pairing: quantum fluctuations")
        print(f"    suppress the instability for N_eff = 4 discrete modes.")
        print(f"    This means the 'N_eff corridor' from BMF-35a is CLOSED by exact treatment.")
    else:
        print(f"    MF M_max also < 1: even mean-field predicts no instability.")
    print(f"    Surviving region: multi-wall stacking, continuum limit N_eff >> 1.")
    print(f"    Next gate: continuum-limit N_eff scaling (how many walls are needed?).")


# ======================================================================
#  SAVE
# ======================================================================

save_dict = {
    'verdict': np.array([verdict]),
}

for i, res in enumerate(results):
    prefix = f'scenario_{chr(65+i)}_'
    save_dict[prefix + 'label'] = np.array([res['label']])
    save_dict[prefix + 'rho_per_mode'] = res['rho_per_mode']
    save_dict[prefix + 'M_max_mf'] = res['M_max_mf']
    save_dict[prefix + 'E_gs'] = res['E_gs']
    save_dict[prefix + 'E_cond'] = res['E_cond']
    save_dict[prefix + 'paired'] = res['paired']
    save_dict[prefix + 'pair_occ'] = res['pair_occ']
    save_dict[prefix + 'vacuum_overlap'] = res['vacuum_overlap']
    save_dict[prefix + 'pair_content'] = res['pair_content']
    save_dict[prefix + 'E_spectrum'] = res['E_spectrum']
    save_dict[prefix + 'chi_pp_exact'] = res['chi_pp_exact']
    save_dict[prefix + 'chi_0'] = res['chi_0']
    save_dict[prefix + 'chi_pp_MF'] = res['chi_pp_MF']
    save_dict[prefix + 'chi_ratio'] = res['chi_ratio']
    save_dict[prefix + 'exp_param'] = res['exp_param']
    save_dict[prefix + 'N_eff'] = res['N_eff']
    if res['paired']:
        save_dict[prefix + 'Delta_eff'] = res['Delta_eff']

# Cross-check
save_dict['xcheck_E_gs'] = res_old['E_gs']
save_dict['xcheck_chi_pp'] = res_old['chi_pp_exact']
save_dict['xcheck_match_E'] = match_E
save_dict['xcheck_match_chi'] = match_chi

# BMF corrections
save_dict['gmb_factor'] = gmb_factor
save_dict['M_max_GMB'] = M_max_GMB
save_dict['delta_Gorkov'] = delta_Gorkov
save_dict['Z_factors'] = Z_factors
save_dict['M_max_Z'] = M_max_Z
save_dict['M_evals_sorted'] = np.array(M_evals_sorted)

# V matrices
save_dict['V_5x5_bare'] = V_5x5_bare
save_dict['V_5x5_gap'] = V_5x5_gap
save_dict['E_5'] = E_5
save_dict['retention_ratio'] = retention_ratio
save_dict['B1B2_ratio'] = B1B2_ratio

out_npz = os.path.join(SCRIPT_DIR, 's35_ed_corrected_dos.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"\nSaved: {out_npz}")
print(f"File size: {os.path.getsize(out_npz) / 1024:.1f} KB")


# ======================================================================
#  PLOT
# ======================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel 1: Condensation energy across scenarios
ax = axes[0, 0]
labels = [r['label'].split(':')[0] for r in results] + ['OLD']
E_conds = [r['E_cond'] for r in results] + [float(old_bmf['E_cond'])]
M_maxs = [r['M_max_mf'] for r in results] + [float(old_bmf['M_max_bare'])]
colors = ['green' if e < -1e-10 else 'red' for e in E_conds]
bars = ax.bar(labels, E_conds, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(0, color='black', ls='--', lw=2, label='E=0 (vacuum)')
for bar, v, m in zip(bars, E_conds, M_maxs):
    y_pos = min(v, 0) - 0.005 * max(abs(min(E_conds)), 0.01)
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
            f'E={v:.4f}\nM={m:.3f}', ha='center', va='bottom', fontsize=8,
            fontweight='bold')
ax.set_ylabel('E_cond')
ax.set_title('Condensation Energy (green=paired, red=vacuum)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel 2: Pair susceptibility comparison
ax = axes[0, 1]
chi_labels_plot = [r['label'].split(':')[0] for r in results]
chi_exact = [r['chi_pp_exact'] for r in results]
chi_mf_vals = [r['chi_pp_MF'] for r in results]
x = np.arange(len(chi_labels_plot))
w = 0.35
bars1 = ax.bar(x - w/2, chi_exact, w, label='chi_pp (ED, exact)',
               color='steelblue', alpha=0.7, edgecolor='black')
# Only plot MF chi where finite and positive
chi_mf_plot = [c if c > 0 and c < 1e10 else 0 for c in chi_mf_vals]
bars2 = ax.bar(x + w/2, chi_mf_plot, w, label='chi_pp (MF)',
               color='coral', alpha=0.7, edgecolor='black')
for bar, v in zip(bars1, chi_exact):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{v:.1f}', ha='center', va='bottom', fontsize=8)
for bar, v, v_orig in zip(bars2, chi_mf_plot, chi_mf_vals):
    if v > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{v:.1f}', ha='center', va='bottom', fontsize=8)
    else:
        ax.text(bar.get_x() + bar.get_width()/2, 1,
                'DIV', ha='center', va='bottom', fontsize=8, color='red')
ax.set_xticks(x)
ax.set_xticklabels(chi_labels_plot, fontsize=8)
ax.set_ylabel('chi_pp')
ax.set_title('Pair Susceptibility: ED vs MF')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel 3: ED spectrum for scenario A
ax = axes[1, 0]
res_A = results[0]
n_show = min(15, len(res_A['E_spectrum']))
spectrum = res_A['E_spectrum'][:n_show]
colors_spec = ['green' if E < -1e-10 else 'steelblue' for E in spectrum]
ax.barh(range(n_show), spectrum, color=colors_spec, alpha=0.7, edgecolor='black')
ax.axvline(0, color='red', lw=2, label='Vacuum energy')
ax.set_xlabel('Energy')
ax.set_ylabel('State index')
ax.set_title(f'ED Spectrum (Scenario A, rho={rho_smooth_per_mode:.1f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='x')
ax.invert_yaxis()

# Panel 4: Pair occupation in ground state
ax = axes[1, 1]
for i, res in enumerate(results):
    marker = ['o', 's', '^', 'D'][i]
    mode_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1']
    ax.plot(range(5), res['pair_occ'], f'-{marker}', lw=2,
            label=f"{res['label'].split(':')[0]} (rho={res['rho_per_mode']:.1f})",
            alpha=0.8, ms=8)
ax.set_xticks(range(5))
ax.set_xticklabels(mode_labels, fontsize=10)
ax.set_ylabel('Pair occupation <n_m>')
ax.set_title('Ground State Pair Content')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

fig.suptitle(f'ED-CORRECTED-35: {verdict} | E_cond(A) = {results[0]["E_cond"]:.6f} | '
             f'M_max(A) = {results[0]["M_max_mf"]:.4f}',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])
out_png = os.path.join(SCRIPT_DIR, 's35_ed_corrected_dos.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"Plot saved: {out_png}")

elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"ED-CORRECTED-35 FINAL: {verdict}")
for res in results:
    print(f"  {res['label']}: E_cond={res['E_cond']:.6f}, M_max(MF)={res['M_max_mf']:.6f}, "
          f"chi_pp(ED)={res['chi_pp_exact']:.4f}, paired={res['paired']}")
print(f"  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
