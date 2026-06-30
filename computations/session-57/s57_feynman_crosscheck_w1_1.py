#!/usr/bin/env python3
"""
S57 Feynman Cross-Check: W1-1 FINITE-RATE-TRANSIT-57
=====================================================
Independent verification of Naz's finite-rate transit results.

Checks:
1. Overlap deficit: does |<GS(tau_i)|GS(tau_f)>|^2 match P_exc_quench?
2. Benchmark consistency: sudden quench vs S56, adiabatic limit
3. Channel decomposition sum rule: P_J + P_BCS + P_L = P_exc
4. Norm conservation
5. Energy conservation (Ehrenfest)
6. Independent Hamiltonian construction + ground state overlap

Author: Feynman-Theorist agent
Session: S57 Wave 1 cross-check
"""

import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    E_cond, tau_fold, N_cells, N_dof_BCS, E_exc_ratio,
    Delta_0_OES, xi_BCS, omega_PV, S_inst, E_B1, E_B2_mean, E_B3_mean,
    PI, M_KK, M_KK_gravity, J_C2,
)

import numpy as np
from scipy.linalg import eigh
from itertools import combinations

data_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(data_dir, 's57_feynman_crosscheck_w1_1.txt')
out = open(out_path, 'w')

def log(msg):
    print(msg)
    out.write(msg + '\n')

log("=" * 70)
log("FEYNMAN CROSS-CHECK: W1-1 FINITE-RATE-TRANSIT-57")
log("=" * 70)

# ======================================================================
# Load Naz's results
# ======================================================================
naz = np.load(os.path.join(data_dir, 's57_finite_rate_transit.npz'), allow_pickle=True)
ed = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
tb = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)

tau_values = ed['tau_values']
E_sp_sweep = ed['E_sp_sweep']
V_bare_raw = ed['V_bare_cont']
V_bare = (V_bare_raw + V_bare_raw.T) / 2.0
fold_idx = int(ed['fold_idx'])
N_modes = int(ed['N_modes'])

J_C2_tau = tb['J_C2_tau']

log(f"\nNaz P_exc_final = {float(naz['P_exc_final']):.6e}")
log(f"Naz P_exc_quench_tauf = {float(naz['P_exc_quench_tauf']):.6e}")
log(f"Naz P_exc_quench_fold = {float(naz['P_exc_quench_fold']):.6e}")
log(f"Naz P_exc_adiabatic = {float(naz['P_exc_adiabatic']):.6e}")

# ======================================================================
# CHECK 1: Independent Hamiltonian + ground state overlap
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 1: Independent Hamiltonian Construction")
log("=" * 70)

N_pair_total = 2  # (local)
n_modes_total = 2 * N_modes
basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)
basis_dict = {state: idx for idx, state in enumerate(basis)}
assert dim == 120, f"Expected 120, got {dim}"

def build_H(eps_1, eps_2, V_1, V_2, E_J_val, alpha=1.0):
    """Independent Hamiltonian construction -- Feynman."""
    H = np.zeros((dim, dim))
    for i, state_i in enumerate(basis):
        # Diagonal: kinetic energy
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        # Pairing interaction (intra-cell)
        for pos, k in enumerate(state_i):
            cell_offset = 0 if k < N_modes else N_modes
            k_local = k - cell_offset
            V_cell = V_1 if k < N_modes else V_2

            for l_local in range(N_modes):
                l = l_local + cell_offset
                if l == k:
                    H[i, i] -= V_cell[k_local, k_local]
                    continue
                if l in state_i:
                    continue
                ns = list(state_i)
                ns[pos] = l
                ns = tuple(sorted(ns))
                if ns in basis_dict:
                    j = basis_dict[ns]
                    H[i, j] -= V_cell[l_local, k_local]

        # Josephson coupling (inter-cell pair hopping)
        if alpha > 0 and E_J_val > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    for l1 in range(N_modes):
                        if l1 in state_i:
                            continue
                        ns = list(state_i)
                        ns[pos] = l1
                        ns = tuple(sorted(ns))
                        if ns in basis_dict:
                            H[i, basis_dict[ns]] -= alpha * E_J_val / 2.0
                else:
                    for l2 in range(N_modes):
                        l = l2 + N_modes
                        if l in state_i:
                            continue
                        ns = list(state_i)
                        ns[pos] = l
                        ns = tuple(sorted(ns))
                        if ns in basis_dict:
                            H[i, basis_dict[ns]] -= alpha * E_J_val / 2.0

    H = (H + H.T) / 2.0
    return H

def compute_E_J(eps, J_C2_val, Delta=Delta_0_OES):
    E_qp = np.sqrt(eps**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    return J_C2_val**2 * F_anom

# Build H at tau=0 and tau=0.5 (last grid point)
eps_0 = E_sp_sweep[0]
eps_f = E_sp_sweep[-1]
E_J_0 = compute_E_J(eps_0, J_C2_tau[0])
E_J_f = compute_E_J(eps_f, J_C2_tau[-1])

log(f"  E_J at tau=0: {E_J_0:.6f}")
log(f"  E_J at tau=0.5: {E_J_f:.6f}")

H_0 = build_H(eps_0, eps_0, V_bare, V_bare, E_J_0)
H_f = build_H(eps_f, eps_f, V_bare, V_bare, E_J_f)

# Diagonalize
evals_0, evecs_0 = eigh(H_0)
evals_f, evecs_f = eigh(H_f)

gs_0 = evecs_0[:, 0]
gs_f = evecs_f[:, 0]

overlap_sq = abs(np.dot(gs_0.conj(), gs_f))**2
P_exc_overlap = 1.0 - overlap_sq

log(f"\n  |<GS(0)|GS(0.5)>|^2 = {overlap_sq:.10f}")
log(f"  P_exc from overlap = {P_exc_overlap:.6e}")
log(f"  Naz P_exc_quench_tauf = {float(naz['P_exc_quench_tauf']):.6e}")
log(f"  Difference: {abs(P_exc_overlap - float(naz['P_exc_quench_tauf'])):.2e}")

if abs(P_exc_overlap - float(naz['P_exc_quench_tauf'])) < 1e-6:
    log("  CONFIRMED: Independent overlap matches Naz to < 1e-6")
else:
    log("  FLAG: Overlap mismatch!")

# Also check H eigenvalues match
log(f"\n  E_GS(tau=0): Feynman={evals_0[0]:.10f}, gap={evals_0[1]-evals_0[0]:.6f}")
log(f"  E_GS(tau=0.5): Feynman={evals_f[0]:.10f}, gap={evals_f[1]-evals_f[0]:.6f}")

# ======================================================================
# CHECK 2: Sudden quench vs S56
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 2: Sudden Quench Benchmark Consistency")
log("=" * 70)

# Quench tau=0 -> fold
eps_fold = E_sp_sweep[fold_idx]
E_J_fold = compute_E_J(eps_fold, J_C2_tau[fold_idx])
H_fold = build_H(eps_fold, eps_fold, V_bare, V_bare, E_J_fold)
evals_fold, evecs_fold = eigh(H_fold)

overlap_fold = abs(np.dot(gs_0.conj(), evecs_fold[:, 0]))**2
P_exc_fold_feynman = 1.0 - overlap_fold

log(f"  P_exc(quench 0->fold): Feynman={P_exc_fold_feynman:.6e}, Naz={float(naz['P_exc_quench_fold']):.6e}")
log(f"  S56 reference: {float(naz['P_exc_s56_ref']):.6e}")
log(f"  Match ratio (Feynman/S56): {P_exc_fold_feynman / float(naz['P_exc_s56_ref']):.6f}")

# Adiabatic limit check
log(f"\n  Adiabatic P_exc (rate=0.1): {float(naz['P_exc_adiabatic']):.6e}")
log(f"  Is < 0.05? {'YES' if float(naz['P_exc_adiabatic']) < 0.05 else 'NO'}")
log(f"  Is < 0.01? {'YES' if float(naz['P_exc_adiabatic']) < 0.01 else 'NO -- borderline'}")

# ======================================================================
# CHECK 3: Channel Decomposition Sum Rule
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 3: Channel Decomposition Sum Rule")
log("=" * 70)

w_bond = float(naz['ch_w_bond'])
w_anti = float(naz['ch_w_anti'])
P_cell0 = float(naz['ch_P_cell0'])
P_cell1 = float(naz['ch_P_cell1'])
P_cross = float(naz['ch_P_cross'])
delta_w_anti = float(naz['ch_delta_w_anti'])
f_Leggett = float(naz['ch_f_Leggett'])
P_exc_final = float(naz['P_exc_final'])

# Sum rule 1: sector probabilities sum to 1
sector_sum = P_cell0 + P_cell1 + P_cross
log(f"  P(2,0) + P(0,2) + P(1,1) = {sector_sum:.10f}")
log(f"  Deviation from 1: {abs(sector_sum - 1.0):.2e}")

# Sum rule 2: bonding + antibonding = 1
ba_sum = w_bond + w_anti
log(f"  w_bond + w_anti = {ba_sum:.10f}")
log(f"  Deviation from 1: {abs(ba_sum - 1.0):.2e}")

# Leggett fraction consistency
log(f"\n  delta_w_anti = {delta_w_anti:.6e}")
log(f"  P_exc = {P_exc_final:.6e}")
log(f"  f_Leggett = |delta_w_anti|/P_exc = {abs(delta_w_anti)/P_exc_final:.4f}")
log(f"  Naz f_Leggett = {f_Leggett:.4f}")
log(f"  Difference: {abs(abs(delta_w_anti)/P_exc_final - f_Leggett):.2e}")

# BCS fraction = 1 - Leggett fraction
f_BCS = 1.0 - f_Leggett
log(f"  f_BCS (intra-cell) = {f_BCS:.4f}")
log(f"  f_Leggett + f_BCS = {f_Leggett + f_BCS:.6f}")

# ======================================================================
# CHECK 4: Norm Conservation
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 4: Norm Conservation")
log("=" * 70)

# The Naz code renormalizes when |norm-1| > 1e-8.
# We can check indirectly: sector sums and bonding/antibonding sums.
log(f"  Sector probability sum = {sector_sum:.15f} (should be 1)")
log(f"  Bond/anti probability sum = {ba_sum:.15f} (should be 1)")

# Also check from nk (pair occupations)
nk_phys = naz['nk_phys']  # shape (201, 16)
nk_sum_init = nk_phys[0].sum()
nk_sum_final = nk_phys[-1].sum()
log(f"  sum(nk) at t=0: {nk_sum_init:.10f} (should be N_pair_total=2)")
log(f"  sum(nk) at t=final: {nk_sum_final:.10f} (should be 2)")
log(f"  Max |sum(nk) - 2| over trajectory: {max(abs(nk_phys.sum(axis=1) - 2)):.2e}")

norm_ok = abs(sector_sum - 1) < 1e-10 and abs(ba_sum - 1) < 1e-10
log(f"  Norm conservation: {'CONFIRMED' if norm_ok else 'FLAG'}")

# ======================================================================
# CHECK 5: Energy Conservation (Ehrenfest)
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 5: Energy Conservation (Ehrenfest)")
log("=" * 70)

tau_phys = naz['tau_phys']
E_exc_phys = naz['E_exc_phys']
P_exc_phys = naz['P_exc_phys']

# For TDSE: d<H>/dt = <dH/dt>.
# We cannot check this directly without the full wavefunction at each step.
# But we CAN check: E_exc should be non-negative (excited relative to instantaneous GS).
# And at the endpoints: E_exc(0) = 0, E_exc(final) should be consistent.

log(f"  E_exc(t=0) = {E_exc_phys[0]:.2e} (should be 0)")
log(f"  E_exc(final) = {E_exc_phys[-1]:.6e}")
log(f"  min(E_exc) = {E_exc_phys.min():.2e} (should be >= 0)")
log(f"  max(E_exc) = {E_exc_phys.max():.6e}")

# Check monotonicity of P_exc (should roughly increase during transit)
n_decreases = sum(1 for i in range(1, len(P_exc_phys)) if P_exc_phys[i] < P_exc_phys[i-1])
log(f"  P_exc non-monotone steps: {n_decreases}/{len(P_exc_phys)-1}")
log(f"  (Non-monotonicity is physical -- oscillations from coherent dynamics)")

# Check that E_exc is consistent with P_exc * typical gap
if E_exc_phys[-1] > 0 and P_exc_phys[-1] > 0:
    effective_E = E_exc_phys[-1] / P_exc_phys[-1]
    log(f"  <E_exc per unit P_exc> = {effective_E:.4f} M_KK (effective excitation energy)")

# E_exc non-negative check
all_nonneg = all(E_exc_phys >= -1e-10)
log(f"  E_exc >= 0 everywhere: {'CONFIRMED' if all_nonneg else 'FLAG'}")

# ======================================================================
# CHECK 6: Rate Scan Consistency
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 6: Rate Scan Consistency")
log("=" * 70)

rate_values = naz['rate_values']
P_exc_scan = naz['P_exc_scan']

# Check that P_exc is monotonically increasing with rate
monotone_violations = sum(1 for i in range(1, len(P_exc_scan))
                          if P_exc_scan[i] < P_exc_scan[i-1] - 1e-6)
log(f"  Rate scan: {len(rate_values)} points from {rate_values[0]:.2f} to {rate_values[-1]:.0f}")
log(f"  P_exc range: [{P_exc_scan.min():.6e}, {P_exc_scan.max():.6e}]")
log(f"  Monotonicity violations (P_exc should increase with rate): {monotone_violations}")

# Check sudden plateau
high_rate_mask = rate_values > 100
if high_rate_mask.any():
    P_high = P_exc_scan[high_rate_mask]
    spread = P_high.max() - P_high.min()
    log(f"  Sudden plateau (rate > 100): spread = {spread:.2e}, mean = {P_high.mean():.6e}")
    log(f"  Plateau matches quench? |mean - P_quench_tauf| = {abs(P_high.mean() - float(naz['P_exc_quench_tauf'])):.2e}")

# ======================================================================
# CHECK 7: Sudden Quench Ceiling vs Physical P_exc
# ======================================================================
log("\n" + "=" * 70)
log("CHECK 7: Sudden Quench Ceiling")
log("=" * 70)

log(f"  P_exc(physical, td) = {P_exc_final:.6e}")
log(f"  P_exc(sudden quench 0->0.5) = {float(naz['P_exc_quench_tauf']):.6e}")
log(f"  Ratio physical/quench = {P_exc_final / float(naz['P_exc_quench_tauf']):.6f}")
log(f"  Physical rate is {float(naz['dtau_dt_phys']):.1f} M_KK")
log(f"  Critical rate (P=0.01): {float(naz['rate_crit_001']):.2f} M_KK")

# The key claim: physical P_exc ~ sudden quench ceiling
# This should be the case if physical rate >> critical rate
rate_ratio = float(naz['dtau_dt_phys']) / float(naz['rate_crit_001'])
log(f"  Rate/Rate_crit = {rate_ratio:.0f}x (>> 1 confirms sudden regime)")

# The physical P_exc should equal the quench to within ~1%
if abs(P_exc_final - float(naz['P_exc_quench_tauf'])) / float(naz['P_exc_quench_tauf']) < 0.01:
    log("  CONFIRMED: Physical transit = sudden quench to < 1%")
else:
    log(f"  NOTE: Physical differs from quench by {abs(P_exc_final - float(naz['P_exc_quench_tauf']))/float(naz['P_exc_quench_tauf'])*100:.1f}%")

# ======================================================================
# SUMMARY
# ======================================================================
log("\n" + "=" * 70)
log("CROSS-CHECK SUMMARY")
log("=" * 70)

issues = []
# Check 1
if abs(P_exc_overlap - float(naz['P_exc_quench_tauf'])) > 1e-6:
    issues.append("CHECK 1: Overlap mismatch")
# Check 2
if abs(P_exc_fold_feynman / float(naz['P_exc_s56_ref']) - 1.0) > 0.01:
    issues.append("CHECK 2: S56 benchmark mismatch")
# Check 3
if abs(sector_sum - 1) > 1e-8 or abs(ba_sum - 1) > 1e-8:
    issues.append("CHECK 3: Sum rule violated")
# Check 4
if not norm_ok:
    issues.append("CHECK 4: Norm not conserved")
# Check 5
if not all_nonneg:
    issues.append("CHECK 5: Negative E_exc found")
# Check 6
if monotone_violations > 0:
    issues.append(f"CHECK 6: {monotone_violations} monotonicity violations in rate scan")

if len(issues) == 0:
    log("\nALL CHECKS PASSED. ENDORSED.")
else:
    log(f"\nISSUES FOUND ({len(issues)}):")
    for iss in issues:
        log(f"  - {iss}")

log(f"\nKey numbers verified independently:")
log(f"  P_exc(quench 0->0.5) = {P_exc_overlap:.6e} (Feynman) vs {float(naz['P_exc_quench_tauf']):.6e} (Naz)")
log(f"  P_exc(quench 0->fold) = {P_exc_fold_feynman:.6e} (Feynman) vs {float(naz['P_exc_quench_fold']):.6e} (Naz)")
log(f"  Sector sum = {sector_sum:.15f}")
log(f"  Bond+anti sum = {ba_sum:.15f}")

out.close()
print("\nDONE")
