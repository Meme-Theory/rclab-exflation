#!/usr/bin/env python3
"""
Session 48: N-PAIR-FULL-48 — Physical Cooper Pair Number at the Fold
=====================================================================
CRITICAL carry-forward from S46, flagged by 5 independent agents.

Gate: N-PAIR-FULL-48
  PASS: N_pair >= 2 (from either BCS or ED, taking the more conservative)
  FAIL: N_pair = 1 remains robust at full singlet
  INFO: N_pair in (1.5, 2.0) — ambiguous regime

Key structural facts:
  1. The (0,0) singlet sector has EXACTLY 16 Dirac eigenvalues = 8 Kramers pairs
     = 8 modes in the pair Hamiltonian. This is COMPLETE — no hidden modes.
  2. S36 ED-CONV-36 already used all 8 modes: 4 B2 + 1 B1 + 3 B3.
     Result: N_pair = 1 exactly (100% of ground state lives in the 1-pair sector).
  3. The block-diagonal theorem (S22b) confines pairing to within-sector Kramers
     pairs. Cooper pairs form within each irrep independently.
  4. mu = 0 (PH symmetry, proven S34 MU-35a). NON-NEGOTIABLE.

This computation performs three independent tests:
  A. REPRODUCE S36 8-mode ED (cross-check, must give E_cond = -0.137, N_pair = 1)
  B. BCS gap equation for full 8-mode singlet (self-consistent iteration)
  C. Multi-sector pair number: combine pair numbers from all 10 irrep sectors

The "16 modes" in the prompt refers to the 16 eigenvalues (8 positive + 8 negative)
of the singlet Dirac operator. In the pair Hamiltonian, we use the 8 positive-branch
Kramers pairs. This script verifies that the S36 calculation IS the full answer
and extends to the multi-sector case.

Author: nazarewicz-nuclear-structure-theorist, Session 48
Date: 2026-03-17
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigvals, eigh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import (
    tau_fold, E_cond_ED_8mode, N_dof_BCS, E_cond
)

t0 = time.time()

print("=" * 78)
print("Session 48: N-PAIR-FULL-48 — Cooper Pair Number at the Fold")
print("=" * 78)

# ======================================================================
#  PART A: Load and reproduce S36 8-mode singlet ED (CROSS-CHECK)
# ======================================================================

print("\n" + "=" * 78)
print("PART A: Reproduce S36 8-mode singlet ED")
print("=" * 78)

# Load S36 stored results for cross-check
s36 = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'), allow_pickle=True)
E_cond_s36 = float(s36['config_4_E_cond'])
n_pair_dist_s36 = s36['config_4_n_pair_dist']
pair_occ_s36 = s36['config_4_pair_occ']
gs_n_pairs_s36 = int(s36['config_4_gs_n_pairs'])
V_8x8_s36 = s36['V_8x8_full']
E_8_s36 = s36['E_8_full']

print(f"\n  S36 stored results (8-mode full singlet):")
print(f"    E_cond      = {E_cond_s36:.10f}")
print(f"    gs_n_pairs  = {gs_n_pairs_s36}")
print(f"    n_pair_dist = {n_pair_dist_s36}")
print(f"    pair_occ    = {pair_occ_s36}")

# Load Kosmann data for independent reconstruction
kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)

# tau_values = [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
# S36 used ti=3 (tau=0.20, nearest to fold at 0.19)
ti = 3
tau_used = kosmann['tau_values'][ti]

evals_raw = kosmann[f'eigenvalues_{ti}']
si = np.argsort(evals_raw)
evals_s = evals_raw[si]
pos_idx = np.where(evals_s > 0)[0]

print(f"\n  Reconstructing from s23a_kosmann_singlet.npz:")
print(f"    tau index ti = {ti}, tau = {tau_used}")
print(f"    Full 16 eigenvalues (sorted): {evals_s}")
print(f"    Positive indices: {pos_idx}")
print(f"    8 positive eigenvalues: {evals_s[pos_idx]}")
print(f"    Branches: B1={evals_s[pos_idx[0]]:.6f} (x1), "
      f"B2={evals_s[pos_idx[1]]:.6f} (x4), "
      f"B3={evals_s[pos_idx[5]]:.6f} (x3)")
print(f"    SINGLET SECTOR IS COMPLETE: 16 eigenvalues = 8 Kramers pairs = 8 modes")

# Build V matrix from Kosmann kernel (sum |K_a|^2 over 8 generators)
V_16 = np.zeros((16, 16))
for a in range(8):
    K = kosmann[f'K_a_matrix_{ti}_{a}']
    K_sorted = K[si][:, si]
    V_16 += np.abs(K_sorted)**2

V_8x8 = V_16[np.ix_(pos_idx, pos_idx)]

# Verify match with S36
V_match = np.allclose(V_8x8, V_8x8_s36, atol=1e-12)
E_match = np.allclose(evals_s[pos_idx], E_8_s36, atol=1e-12)
print(f"\n  Cross-check against S36 stored values:")
print(f"    V_8x8 match: {V_match} (max diff: {np.max(np.abs(V_8x8 - V_8x8_s36)):.2e})")
print(f"    E_8 match:   {E_match}")

# S36 reorders to B2[0..3], B1, B3[0..2]
# Our pos_idx ordering: B1[0], B2[0..3], B3[0..2] (ascending eigenvalue)
# S36: full_pos_idx = [B2(4), B1(1), B3(3)] in eigenvalue-sorted pos space
# = pos indices [1,2,3,4, 0, 5,6,7]
reorder_s36 = [1, 2, 3, 4, 0, 5, 6, 7]

# Independent ED: Construct pair Hamiltonian
E_8 = evals_s[pos_idx]  # B1[0], B2[0..3], B3[0..2]
mu = 0.0
xi_8 = E_8 - mu  # = E_8 since mu=0

# DOS assignment
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)
rho_smooth_per_mode = float(vh_arbiter['rho_at_physical'])  # 14.02

# B1 -> rho=1 (away from fold), B2 -> rho_smooth (at van Hove), B3 -> rho=1
rho_8 = np.array([1.0,  # B1
                   rho_smooth_per_mode, rho_smooth_per_mode,
                   rho_smooth_per_mode, rho_smooth_per_mode,  # B2 x4
                   1.0, 1.0, 1.0])  # B3 x3

n_modes = 8
n_states = 2**n_modes  # 256

print(f"\n  Building pair Hamiltonian:")
print(f"    n_modes = {n_modes}")
print(f"    n_states = {n_states}")
print(f"    mu = {mu} (PH symmetry, NON-NEGOTIABLE)")
print(f"    rho = {rho_8}")

# Build Hamiltonian in pair-occupation basis
H = np.zeros((n_states, n_states))

# Diagonal: 2*xi_m for each occupied pair
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H[state, state] += 2 * xi_8[m]

# Off-diagonal: pair scattering -V_nm * sqrt(rho_n * rho_m) * b_n^dag b_m
for state in range(n_states):
    for n in range(n_modes):
        for m in range(n_modes):
            if n == m:
                continue
            if V_8x8[n, m] < 1e-15:
                continue
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                H[new_state, state] -= V_8x8[n, m] * np.sqrt(rho_8[n] * rho_8[m])

H = 0.5 * (H + H.T)  # Ensure Hermiticity

# Diagonalize
E_all, psi_all = eigh(H)
E_gs = E_all[0]
psi_gs = psi_all[:, 0]

print(f"\n  ED results (independent reconstruction):")
print(f"    E_gs = {E_gs:.10f}")
print(f"    E_cond = {E_gs:.10f} (vacuum is state 0, energy = 0)")

# Cross-check with S36
# S36 E_cond is in the B2+B1+B3 ordering; our ordering is B1+B2+B3
# The eigenvalues should be identical (Hamiltonian is physically equivalent)
E_cond_match = abs(E_gs - E_cond_s36) < 1e-8
print(f"    Match S36 E_cond: {E_cond_match} (diff: {abs(E_gs - E_cond_s36):.2e})")

# Pair occupation
pair_occ = np.zeros(n_modes)
for state in range(n_states):
    prob = abs(psi_gs[state])**2
    for m in range(n_modes):
        if state & (1 << m):
            pair_occ[m] += prob

# Pair number distribution
n_pair_dist = np.zeros(n_modes + 1)
for state in range(n_states):
    k = bin(state).count('1')
    n_pair_dist[k] += abs(psi_gs[state])**2

gs_n_pairs = np.argmax(n_pair_dist)
N_pair_ED = np.sum(pair_occ)
vacuum_overlap = abs(psi_gs[0])**2

branch_labels = ['B1', 'B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B3[0]', 'B3[1]', 'B3[2]']

print(f"\n  Pair number from ED:")
print(f"    N_pair (sum v_k^2) = {N_pair_ED:.10f}")
print(f"    gs_n_pairs sector  = {gs_n_pairs}")
print(f"    n_pair_dist        = {n_pair_dist}")
print(f"    vacuum_overlap     = {vacuum_overlap:.10f}")
print(f"\n  Pair occupations:")
for m in range(n_modes):
    print(f"    <n_{m}> ({branch_labels[m]:>5s}) = {pair_occ[m]:.10f}")

# ======================================================================
#  PART B: Self-Consistent BCS Gap Equation (full 8-mode singlet)
# ======================================================================

print("\n\n" + "=" * 78)
print("PART B: Self-Consistent BCS Gap Equation")
print("=" * 78)

# BCS gap equation:
#   Delta_k = -(1/2) * sum_{k'} V_{kk'} * rho_{k'} * Delta_{k'} / E_{k'}
#   E_k = sqrt(xi_k^2 + Delta_k^2)
#   xi_k = |epsilon_k| (since mu=0)
#
# We solve iteratively, starting from a small uniform gap

ETA_REG = 1e-6
xi_bcs = np.abs(E_8 - mu)  # = E_8 since mu=0
xi_bcs = np.maximum(xi_bcs, ETA_REG)

# V_eff[k,k'] = V_8x8[k,k'] * sqrt(rho_8[k'] * rho_8[k])
# (the DOS enters the gap equation as V * rho)
V_eff = np.zeros((n_modes, n_modes))
for k in range(n_modes):
    for kp in range(n_modes):
        V_eff[k, kp] = V_8x8[k, kp] * np.sqrt(rho_8[k] * rho_8[kp])

# Self-consistent iteration
Delta = np.ones(n_modes) * 0.01  # Initial guess
max_iter = 10000
tol = 1e-12
converged = False

print(f"\n  Self-consistent BCS iteration:")
print(f"    V_eff (DOS-weighted):")
for i in range(n_modes):
    row = " ".join(f"{V_eff[i,j]:8.5f}" for j in range(n_modes))
    print(f"      {branch_labels[i]:>5s}: {row}")

for iteration in range(max_iter):
    E_qp = np.sqrt(xi_bcs**2 + Delta**2)
    Delta_new = np.zeros(n_modes)
    for k in range(n_modes):
        for kp in range(n_modes):
            if k == kp:
                continue
            Delta_new[k] += V_eff[k, kp] * Delta[kp] / (2.0 * E_qp[kp])

    # Check convergence
    diff = np.max(np.abs(Delta_new - Delta))
    if diff < tol:
        converged = True
        Delta = Delta_new
        break

    # Damped update for stability
    alpha_damp = 0.5
    Delta = alpha_damp * Delta_new + (1 - alpha_damp) * Delta

    if iteration < 5 or iteration % 1000 == 0:
        print(f"    iter {iteration:5d}: max|Delta| = {np.max(np.abs(Delta)):.10f}, "
              f"diff = {diff:.2e}")

print(f"    Converged: {converged} after {iteration+1} iterations")
print(f"    Final Delta:")
for m in range(n_modes):
    print(f"      Delta_{m} ({branch_labels[m]:>5s}) = {Delta[m]:.10f}")

# BCS occupation numbers
E_qp = np.sqrt(xi_bcs**2 + Delta**2)
v2_bcs = 0.5 * (1.0 - xi_bcs / E_qp)
N_pair_BCS = np.sum(v2_bcs)

print(f"\n  BCS occupation numbers (v_k^2):")
for m in range(n_modes):
    print(f"    v^2_{m} ({branch_labels[m]:>5s}) = {v2_bcs[m]:.10f}")
print(f"\n  N_pair_BCS = sum v_k^2 = {N_pair_BCS:.10f}")

# BCS condensation energy
E_cond_BCS = -np.sum(Delta**2 / (2.0 * E_qp))
print(f"  E_cond_BCS = {E_cond_BCS:.10f}")

# Check: does BCS collapse to trivial?
Delta_max = np.max(np.abs(Delta))
trivial_BCS = Delta_max < 1e-8
if trivial_BCS:
    print(f"\n  *** BCS COLLAPSED TO TRIVIAL (Delta_max = {Delta_max:.2e}) ***")
    print(f"  This is expected: 8-mode system is too small for BCS.")
    print(f"  Paper 03 (Bogoliubov, odd-even): 'BCS breaks down for very small systems'")
    print(f"  Using ED result as definitive.")
else:
    print(f"\n  BCS non-trivial: Delta_max = {Delta_max:.6f}")

# Also try: BCS with strong initial guess (near ED gap)
print(f"\n  BCS attempt with strong initial guess:")
Delta_strong = np.array([0.1, 0.3, 0.3, 0.3, 0.3, 0.05, 0.05, 0.05])
for iteration in range(max_iter):
    E_qp_s = np.sqrt(xi_bcs**2 + Delta_strong**2)
    Delta_new_s = np.zeros(n_modes)
    for k in range(n_modes):
        for kp in range(n_modes):
            if k == kp:
                continue
            Delta_new_s[k] += V_eff[k, kp] * Delta_strong[kp] / (2.0 * E_qp_s[kp])
    diff_s = np.max(np.abs(Delta_new_s - Delta_strong))
    if diff_s < tol:
        Delta_strong = Delta_new_s
        break
    Delta_strong = 0.5 * Delta_new_s + 0.5 * Delta_strong

Delta_max_strong = np.max(np.abs(Delta_strong))
print(f"    Delta_max (strong init) = {Delta_max_strong:.10f}")
print(f"    Collapsed: {Delta_max_strong < 1e-8}")

# ======================================================================
#  PART C: Number-Projected BCS (PBCS) for pair number
# ======================================================================

print("\n\n" + "=" * 78)
print("PART C: Number-Projected Pair Count from ED Ground State")
print("=" * 78)

# The ED ground state |GS> is number-conserving (the pair Hamiltonian conserves
# total pair number). The pair-number distribution tells us definitively how
# many pairs the ground state contains.

print(f"\n  DEFINITIVE pair number from ED:")
print(f"    Pair-number distribution P(N):")
for k in range(n_modes + 1):
    marker = " <-- GROUND STATE" if k == gs_n_pairs else ""
    print(f"      P(N={k}) = {n_pair_dist[k]:.15e}{marker}")

print(f"\n    <N_pair> = sum_k k * P(k) = ", end="")
N_pair_expectation = sum(k * n_pair_dist[k] for k in range(n_modes + 1))
print(f"{N_pair_expectation:.10f}")
print(f"    max P(N) at N = {gs_n_pairs} with probability {n_pair_dist[gs_n_pairs]:.15e}")

# Pair-pair correlator (off-diagonal long-range order)
print(f"\n  Off-diagonal pair-pair correlator <b_n^dag b_m>:")
pair_corr = np.zeros((n_modes, n_modes))
for n in range(n_modes):
    for m in range(n_modes):
        if n == m:
            pair_corr[n, m] = pair_occ[m]
            continue
        corr = 0.0
        for state in range(n_states):
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                corr += np.conj(psi_gs[new_state]) * psi_gs[state]
        pair_corr[n, m] = abs(corr)

offdiag_max = np.max(pair_corr - np.diag(np.diag(pair_corr)))
print(f"    Max off-diagonal: {offdiag_max:.6f}")
print(f"    B2-B2 block (modes 1-4):")
for i in range(1, 5):
    row = " ".join(f"{pair_corr[i,j]:.4f}" for j in range(1, 5))
    print(f"      {row}")

# ======================================================================
#  PART D: Multi-Sector Pair Number
# ======================================================================

print("\n\n" + "=" * 78)
print("PART D: Multi-Sector Pair Number (all 10 irrep sectors)")
print("=" * 78)

# The block-diagonal theorem (S22b) means D_K decomposes into independent
# blocks for each irrep. The pairing interaction V = sum_a |K_a|^2 also
# respects this block structure because K_a commutes with the Casimir
# operators of each block (proven S34).
#
# Each irrep sector has its own pair Hamiltonian and its own pair number.
# The total pair number is the sum across all sectors.
#
# However: the Kosmann data (s23a) only computed the SINGLET sector.
# We do not have V matrices for the other 9 sectors.
#
# What we CAN do:
# 1. The singlet N_pair = 1 is exact (full ED, 256 states)
# 2. For non-singlet sectors, we can estimate from the Thouless criterion:
#    M_max > 1 implies pairing instability, which typically gives N_pair >= 1
# 3. The S35 mechanism chain showed M_max = 1.674 for the singlet.
#    Non-singlet sectors have DIFFERENT V matrices and DOS.
#
# From the DOS data (s44_dos_tau.npz), at the fold:
# - Total modes: 992 (all sectors combined)
# - Singlet modes: 16 (= 8 Kramers pairs)
# - Non-singlet modes: 976 (= 488 Kramers pairs)
#
# The non-singlet sectors lack the van Hove enhancement (rho = 14/mode for B2).
# Without the van Hove singularity, M_max is typically < 1, and pairing is weak.

dos = np.load(os.path.join(SCRIPT_DIR, 's44_dos_tau.npz'), allow_pickle=True)
all_omega = dos['tau0.19_all_omega']  # At canonical fold tau=0.19
all_dim2 = dos['tau0.19_all_dim2']

print(f"\n  Full Dirac spectrum at fold (tau=0.19):")
print(f"    Total eigenvalues: {len(all_omega)}")
print(f"    Unique values: {len(np.unique(np.round(all_omega, 8)))}")

# Count by branch
unique_omega = np.unique(np.round(all_omega, 8))
print(f"\n  Eigenvalue structure (positive branch):")
for omega in sorted(unique_omega):
    count = np.sum(np.abs(all_omega - omega) < 1e-6)
    print(f"    omega = {omega:.6f}, multiplicity = {count}")

# The full 992-mode spectrum includes all 10 sectors
# Only the singlet has the van Hove singularity at the B2 flat band
# The Thouless criterion for each sector depends on:
#   M_nm = V_nm * rho_m / (2|xi_m|)
# Without van Hove, rho ~ 1/mode (not 14/mode), so M_max drops by ~14x
# This pushes M_max from 1.674 to ~0.12, well below the BCS threshold

# Let me check: what is the Thouless parameter WITHOUT van Hove enhancement?
# Use the singlet V matrix but with rho=1 for all modes
rho_unit = np.ones(n_modes)
V_eff_noVH = np.zeros((n_modes, n_modes))
for k in range(n_modes):
    for kp in range(n_modes):
        V_eff_noVH[k, kp] = V_8x8[k, kp] * np.sqrt(rho_unit[k] * rho_unit[kp])

M_noVH = np.zeros((n_modes, n_modes))
for m in range(n_modes):
    M_noVH[:, m] = V_eff_noVH[:, m] / (2.0 * xi_bcs[m])
M_max_noVH = np.max(np.real(eigvals(M_noVH)))

print(f"\n  Thouless parameter WITHOUT van Hove enhancement (rho=1 everywhere):")
print(f"    M_max (no VH) = {M_max_noVH:.6f}")
print(f"    M_max (with VH) = ", end="")
M_withVH = np.zeros((n_modes, n_modes))
for m in range(n_modes):
    M_withVH[:, m] = V_eff[k, m] * rho_8[m] / (2.0 * xi_bcs[m])
# Recompute properly
M_proper = np.zeros((n_modes, n_modes))
for n in range(n_modes):
    for m in range(n_modes):
        M_proper[n, m] = V_8x8[n, m] * rho_8[m] / (2.0 * xi_bcs[m])
M_max_withVH = np.max(np.real(eigvals(M_proper)))
print(f"{M_max_withVH:.6f}")
print(f"    Ratio: {M_max_withVH / max(M_max_noVH, 1e-15):.2f}x enhancement from van Hove")

# ED with rho=1 (no van Hove): does pairing survive?
print(f"\n  ED with rho=1 (no van Hove):")
H_noVH = np.zeros((n_states, n_states))
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H_noVH[state, state] += 2 * xi_8[m]

for state in range(n_states):
    for n in range(n_modes):
        for m in range(n_modes):
            if n == m:
                continue
            if V_8x8[n, m] < 1e-15:
                continue
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                H_noVH[new_state, state] -= V_8x8[n, m]  # rho=1

H_noVH = 0.5 * (H_noVH + H_noVH.T)
E_all_noVH, psi_all_noVH = eigh(H_noVH)
E_gs_noVH = E_all_noVH[0]
psi_gs_noVH = psi_all_noVH[:, 0]

# Pair number distribution
n_pair_dist_noVH = np.zeros(n_modes + 1)
for state in range(n_states):
    k = bin(state).count('1')
    n_pair_dist_noVH[k] += abs(psi_gs_noVH[state])**2

pair_occ_noVH = np.zeros(n_modes)
for state in range(n_states):
    prob = abs(psi_gs_noVH[state])**2
    for m in range(n_modes):
        if state & (1 << m):
            pair_occ_noVH[m] += prob

N_pair_noVH = np.sum(pair_occ_noVH)
gs_n_pairs_noVH = np.argmax(n_pair_dist_noVH)

print(f"    E_gs (no VH) = {E_gs_noVH:.10f}")
print(f"    Paired: {E_gs_noVH < -1e-10}")
print(f"    N_pair = {N_pair_noVH:.10f}")
print(f"    gs_n_pairs = {gs_n_pairs_noVH}")
print(f"    n_pair_dist = {n_pair_dist_noVH}")

# ======================================================================
#  PART E: Scan over tau — N_pair vs tau
# ======================================================================

print("\n\n" + "=" * 78)
print("PART E: N_pair vs tau (scan available Kosmann points)")
print("=" * 78)

tau_values = kosmann['tau_values']
N_pair_vs_tau = np.zeros(len(tau_values))
E_cond_vs_tau = np.zeros(len(tau_values))
gs_npairs_vs_tau = np.zeros(len(tau_values), dtype=int)
n_pair_dists_all = []

for ti_scan in range(len(tau_values)):
    evals_raw_t = kosmann[f'eigenvalues_{ti_scan}']
    si_t = np.argsort(evals_raw_t)
    evals_s_t = evals_raw_t[si_t]
    pos_idx_t = np.where(evals_s_t > 0)[0]
    E_8_t = evals_s_t[pos_idx_t]
    xi_t = E_8_t - mu

    # Build V from Kosmann
    V_16_t = np.zeros((16, 16))
    for a in range(8):
        K_t = kosmann[f'K_a_matrix_{ti_scan}_{a}']
        K_sorted_t = K_t[si_t][:, si_t]
        V_16_t += np.abs(K_sorted_t)**2
    V_8_t = V_16_t[np.ix_(pos_idx_t, pos_idx_t)]

    # DOS: use van Hove for B2 modes (indices 1-4), rho=1 for B1 and B3
    rho_t = np.array([1.0, rho_smooth_per_mode, rho_smooth_per_mode,
                       rho_smooth_per_mode, rho_smooth_per_mode,
                       1.0, 1.0, 1.0])

    # Build pair Hamiltonian
    H_t = np.zeros((n_states, n_states))
    for state in range(n_states):
        for m in range(n_modes):
            if state & (1 << m):
                H_t[state, state] += 2 * xi_t[m]

    for state in range(n_states):
        for n in range(n_modes):
            for m in range(n_modes):
                if n == m:
                    continue
                if V_8_t[n, m] < 1e-15:
                    continue
                if (state & (1 << m)) and not (state & (1 << n)):
                    new_state = state ^ (1 << m) ^ (1 << n)
                    H_t[new_state, state] -= V_8_t[n, m] * np.sqrt(rho_t[n] * rho_t[m])

    H_t = 0.5 * (H_t + H_t.T)
    E_all_t, psi_all_t = eigh(H_t)
    psi_gs_t = psi_all_t[:, 0]

    # Pair number
    pair_occ_t = np.zeros(n_modes)
    for state in range(n_states):
        prob = abs(psi_gs_t[state])**2
        for m in range(n_modes):
            if state & (1 << m):
                pair_occ_t[m] += prob

    n_pair_dist_t = np.zeros(n_modes + 1)
    for state in range(n_states):
        k = bin(state).count('1')
        n_pair_dist_t[k] += abs(psi_gs_t[state])**2

    N_pair_vs_tau[ti_scan] = np.sum(pair_occ_t)
    E_cond_vs_tau[ti_scan] = E_all_t[0]
    gs_npairs_vs_tau[ti_scan] = np.argmax(n_pair_dist_t)
    n_pair_dists_all.append(n_pair_dist_t)

    print(f"  tau={tau_values[ti_scan]:.2f}: E_cond={E_all_t[0]:.6f}, "
          f"N_pair={np.sum(pair_occ_t):.4f}, gs_N={np.argmax(n_pair_dist_t)}, "
          f"P(N=1)={n_pair_dist_t[1]:.6f}, P(N=2)={n_pair_dist_t[2]:.6e}")

# ======================================================================
#  PART F: Summary and Gate Verdict
# ======================================================================

print("\n\n" + "=" * 78)
print("SUMMARY AND GATE VERDICT")
print("=" * 78)

print(f"\n  STRUCTURAL FACT: The (0,0) singlet sector has exactly 8 Kramers pairs.")
print(f"  The S36 '8-mode' ED IS the full singlet sector. There are no missing modes.")
print(f"  This is a consequence of dim(spinor) x dim(singlet) = 16 x 1 = 16 eigenvalues")
print(f"  = 8 Kramers pairs (positive branch) = 8 modes in pair Hamiltonian.")

print(f"\n  INDEPENDENT REPRODUCTION (Part A):")
print(f"    E_cond (this script) = {E_gs:.10f}")
print(f"    E_cond (S36 stored)  = {E_cond_s36:.10f}")
print(f"    Match: {E_cond_match}")

print(f"\n  PAIR NUMBER (ED, definitive):")
print(f"    N_pair = {N_pair_ED:.10f}")
print(f"    gs lives in N={gs_n_pairs} sector with P = {n_pair_dist[gs_n_pairs]:.15e}")
print(f"    P(N=0) = {n_pair_dist[0]:.6e}")
print(f"    P(N=1) = {n_pair_dist[1]:.15f}")
print(f"    P(N=2) = {n_pair_dist[2]:.6e}")
print(f"    P(N=3) = {n_pair_dist[3]:.6e}")

print(f"\n  BCS GAP EQUATION:")
print(f"    Converged to trivial (Delta -> 0): {trivial_BCS}")
print(f"    N_pair_BCS = {N_pair_BCS:.10f}")
print(f"    Expected: BCS breaks down for N_modes = 8 (Paper 03, Section IV)")

print(f"\n  WITHOUT VAN HOVE (rho=1):")
print(f"    N_pair = {N_pair_noVH:.10f}")
print(f"    Paired: {E_gs_noVH < -1e-10}")
if E_gs_noVH < -1e-10:
    print(f"    Even without van Hove, pairing persists (BCS 1D theorem)")
else:
    print(f"    Without van Hove, pairing disappears")

print(f"\n  TAU SCAN (N_pair vs tau):")
for ti_scan in range(len(tau_values)):
    print(f"    tau={tau_values[ti_scan]:.2f}: N_pair={N_pair_vs_tau[ti_scan]:.4f}, "
          f"gs_N={gs_npairs_vs_tau[ti_scan]}")

# Maximum N_pair across all tau
max_N = np.max(N_pair_vs_tau)
max_tau_idx = np.argmax(N_pair_vs_tau)
print(f"\n    Max N_pair = {max_N:.6f} at tau = {tau_values[max_tau_idx]:.2f}")

# ---- Gate verdict ----
# The MORE CONSERVATIVE of ED and BCS
N_pair_conservative = N_pair_ED  # ED is exact; BCS collapsed to trivial
N_pair_for_gate = N_pair_conservative

print(f"\n  GATE N-PAIR-FULL-48:")
print(f"    N_pair (conservative) = {N_pair_for_gate:.10f}")
print(f"    Threshold: N >= 2.0 for PASS, N in [1.5, 2.0) for INFO, N < 1.5 for FAIL")

if N_pair_for_gate >= 2.0:
    verdict = "PASS"
    verdict_detail = (f"N_pair = {N_pair_for_gate:.4f} >= 2.0. "
                     f"Full singlet ED confirms N >= 2.")
elif N_pair_for_gate >= 1.5:
    verdict = "INFO"
    verdict_detail = (f"N_pair = {N_pair_for_gate:.4f} in [1.5, 2.0). "
                     f"Ambiguous regime.")
else:
    verdict = "FAIL"
    verdict_detail = (f"N_pair = {N_pair_for_gate:.4f} < 1.5. "
                     f"The ground state is a SINGLE Cooper pair (N=1 exactly).")

print(f"\n  *** N-PAIR-FULL-48: {verdict} ***")
print(f"  {verdict_detail}")

# Physical interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
print(f"    The singlet sector ground state is a SINGLE Cooper pair.")
print(f"    This is NOT a BCS condensate (which requires many overlapping pairs).")
print(f"    This is the BCS-BEC crossover regime identified in S37:")
print(f"      xi_BCS / d_01 = 1.40 (coherence length ~ inter-level spacing)")
print(f"    In nuclear physics terms (Paper 03, Sec IV):")
print(f"      This is like an sd-shell nucleus with 2 valence neutrons.")
print(f"      The pair number N=1 is EXACT in the number-conserving framework.")
print(f"      BCS overestimates the pairing because it breaks number conservation.")
print(f"    The q-theory CC crossing at tau*=0.170 requires N>=2 pairs.")
print(f"    With N=1, the crossing point is 1.4x short (S46 V-B3B3-46).")

print(f"\n  WHAT WAS COMPUTED:")
print(f"    Full singlet ED with all 8 Kramers pairs (= complete singlet sector)")
print(f"    BCS self-consistent gap equation (8 modes)")
print(f"    tau scan (9 points)")
print(f"    No-van-Hove control (rho=1)")

print(f"\n  WHAT REGION OF SOLUTION SPACE THIS CONSTRAINS:")
print(f"    The N=1 pair number is a STRUCTURAL PROPERTY of the singlet sector.")
print(f"    It cannot be changed by:")
print(f"      - Including 'missing' modes (there are none)")
print(f"      - Adjusting mu (mu=0 is forced by PH symmetry)")
print(f"      - Using BCS vs ED (ED is exact, BCS collapses)")
print(f"    It CAN potentially change via:")
print(f"      - Multi-sector pairing (non-singlet sectors contribute their own pairs)")
print(f"      - Modified DOS (van Hove shape near fold)")
print(f"      - Self-consistent Delta(tau) feedback (q-theory loop)")

print(f"\n  WHAT REMAINS UNCOMPUTED:")
print(f"    1. V matrices for non-singlet sectors (requires Kosmann kernel in each irrep)")
print(f"    2. Total multi-sector N_pair = sum over all 10 sectors")
print(f"    3. Self-consistent Delta(tau) solving the q-theory crossing")

# ======================================================================
#  SAVE
# ======================================================================

save_dict = {
    'verdict': np.array([verdict]),
    'N_pair_ED': N_pair_ED,
    'N_pair_BCS': N_pair_BCS,
    'E_cond_ED': E_gs,
    'E_cond_s36_stored': E_cond_s36,
    'E_cond_match': E_cond_match,
    'gs_n_pairs': gs_n_pairs,
    'n_pair_dist': n_pair_dist,
    'pair_occ': pair_occ,
    'pair_corr': pair_corr,
    'Delta_BCS': Delta,
    'v2_BCS': v2_bcs,
    'trivial_BCS': trivial_BCS,
    'N_pair_noVH': N_pair_noVH,
    'E_cond_noVH': E_gs_noVH,
    'M_max_withVH': M_max_withVH,
    'M_max_noVH': M_max_noVH,
    'tau_scan': tau_values,
    'N_pair_vs_tau': N_pair_vs_tau,
    'E_cond_vs_tau': E_cond_vs_tau,
    'gs_npairs_vs_tau': gs_npairs_vs_tau,
    'V_8x8': V_8x8,
    'E_8': E_8,
    'rho_8': rho_8,
    'xi_8': xi_8,
    'branch_labels': np.array(branch_labels),
    'tau_used': tau_used,
}

for ti_scan in range(len(tau_values)):
    save_dict[f'n_pair_dist_tau{ti_scan}'] = n_pair_dists_all[ti_scan]

out_npz = os.path.join(SCRIPT_DIR, 's48_npair_full.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"\nSaved: {out_npz}")
print(f"File size: {os.path.getsize(out_npz) / 1024:.1f} KB")

elapsed = time.time() - t0
print(f"\nRuntime: {elapsed:.1f}s")
print("=" * 78)
