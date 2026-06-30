#!/usr/bin/env python3
"""
S75-E2-DIMER-Z2: Parker Pair Production in Z_2-Odd Sector
============================================================

Computes the fraction of Parker-produced quasiparticles in the Z_2-odd
(dimer-parity-odd) sector of the 2-cell GGE.

Resonance structure:
  - Oscillator: 8 D_K modes per cell (4 B2 + 1 B1 + 3 B3), 16 total
  - Cavity: 2-cell Josephson-coupled SU(3) fiber dimer
  - Symmetry: Z_2 = cell exchange (swap cell 1 <-> cell 2)
  - Boundary condition: periodic (Born-von Karman on internal geometry)
  - Normal modes: 120-dim Hilbert space = C(16,2) for N_pair=2
  - Excitation mechanism: sudden quench (Parker pair production)

The Z_2 exchange operator P acts on pair states |s1, s2> as:
  P|s1, s2> = |P(s1), P(s2)>
where P(s) swaps the cell index: mode k in cell 1 <-> mode k in cell 2.

P^2 = I, so eigenvalues are +1 (even/bonding) and -1 (odd/antibonding).
The Z_2-odd sector is the DM candidate (Leggett channel).

Method:
  1. Load 2-cell data from s56_gge_fabric.npz
  2. Reconstruct the 120-dim Hilbert space and H at tau=0 and tau_fold
  3. Build the Z_2 exchange operator P on the pair basis
  4. Compute the diagonal ensemble from sudden quench
  5. Project each eigenstate onto Z_2 sectors
  6. Sum diagonal ensemble weight in Z_2-odd: n_Z2 = sum_{odd n} p_n

Gate: S75-E2-DIMER-Z2
  PASS: n_Z2/n_total in [0.1, 0.5]
  INFO: n_Z2/n_total outside [0.1, 0.5] but computable
  FAIL: Z_2 parity not well-defined for GGE modes

Session: S75 W2-N
Agent: Tesla-Resonance (Workhorse-Resonance)
"""

import sys
import os
import numpy as np
from itertools import combinations
from scipy.linalg import eigh
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, Delta_0_OES, J_C2, n_pairs, N_dof_BCS
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("S75-E2-DIMER-Z2: Parker Pair Production in Z_2-Odd Sector")
print("=" * 78)

# ============================================================================
# 1. Load data from S56 GGE fabric
# ============================================================================
d56 = np.load(os.path.join(SCRIPT_DIR, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # (8,) single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # (8,) single-particle energies at tau=0
V_fold = d56['V_fold']           # (8,8) pairing interaction
E_J_fold = float(d56['E_J_fold'])
E_J_tau0 = float(d56['E_J_tau0'])
tau_fold_actual = float(d56['tau_fold_actual'])
dim_expected = int(d56['dim'])    # 120

# Cross-check stored values
c_n_stored = d56['c_n']          # (120,) overlap coefficients
p_n_stored = d56['p_n']          # (120,) diagonal ensemble probabilities
nk_DE_stored = d56['nk_DE']     # (16,) mode occupations

print(f"Loaded s56_gge_fabric.npz")
print(f"  eps_fold = {eps_fold}")
print(f"  eps_tau0 = {eps_tau0}")
print(f"  E_J_fold = {E_J_fold:.6f} M_KK")
print(f"  E_J_tau0 = {E_J_tau0:.6f} M_KK")
print(f"  tau_fold = {tau_fold_actual:.6f}")

# ============================================================================
# 2. Build 2-cell Hilbert space (same construction as s56_gge_fabric.py)
# ============================================================================
N_modes = 8  # (local) modes per cell
N_pair_total = 2  # (local) total Cooper pairs
n_modes_total = 2 * N_modes  # (local) 16 total pair-slots

# Pair basis: all ways to place 2 pairs in 16 slots
basis = list(combinations(range(n_modes_total), N_pair_total))
dim = len(basis)  # (local)
assert dim == dim_expected == 120, f"Expected 120, got {dim}"
basis_dict = {state: idx for idx, state in enumerate(basis)}

print(f"\nHilbert space: C({n_modes_total},{N_pair_total}) = {dim}")

# Branch labels: modes 0-3 = B2, mode 4 = B1, modes 5-7 = B3 (per cell)
branch_labels = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3'] * 2

# ============================================================================
# 3. Build Hamiltonian (identical to s56)
# ============================================================================
def build_H_2cell(eps_1, eps_2, V_1, V_2, E_J_coupling, alpha=1.0):
    """
    Build 2-cell BCS Hamiltonian in pair basis.
    H = H_BCS(1) + H_BCS(2) + alpha * H_J
    """
    H = np.zeros((dim, dim))  # (local)

    for i, state_i in enumerate(basis):
        # Diagonal: kinetic
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        # BCS off-diagonal within each cell
        for pos, k in enumerate(state_i):
            if k < N_modes:
                cell_offset = 0  # (local)
                k_local = k  # (local)
                V_cell = V_1  # (local)
            else:
                cell_offset = N_modes  # (local)
                k_local = k - N_modes  # (local)
                V_cell = V_2  # (local)

            for l_local in range(N_modes):
                l = l_local + cell_offset  # (local)
                if l == k:
                    H[i, i] -= V_cell[k_local, k_local]
                    continue
                if l in state_i:
                    continue
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))
                if new_state in basis_dict:
                    j = basis_dict[new_state]  # (local)
                    H[i, j] -= V_cell[l_local, k_local]

        # Josephson coupling
        if alpha > 0 and E_J_coupling > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    for l1 in range(N_modes):
                        if l1 in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l1
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]  # (local)
                            H[i, j] -= alpha * E_J_coupling / 2.0
                else:
                    for l2 in range(N_modes):
                        l = l2 + N_modes  # (local)
                        if l in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]  # (local)
                            H[i, j] -= alpha * E_J_coupling / 2.0

    H = (H + H.T) / 2.0
    return H


# ============================================================================
# 4. Build Z_2 exchange operator
# ============================================================================
print("\n" + "=" * 60)
print("STEP 1: Z_2 Exchange Operator Construction")
print("=" * 60)

def swap_slot(s):
    """Swap cell index of a pair-slot: cell 1 <-> cell 2."""
    mode = s % N_modes  # (local)
    cell = s // N_modes  # (local)
    return (1 - cell) * N_modes + mode

# Build P matrix: P|s1,s2> = |P(s1), P(s2)>
P_mat = np.zeros((dim, dim), dtype=np.float64)
for i, state_i in enumerate(basis):
    s1, s2 = state_i
    new_s1 = swap_slot(s1)  # (local)
    new_s2 = swap_slot(s2)  # (local)
    new_state = tuple(sorted([new_s1, new_s2]))  # (local)
    if new_state in basis_dict:
        j = basis_dict[new_state]  # (local)
        P_mat[j, i] = 1.0

# Verify P^2 = I
P2_err = np.max(np.abs(P_mat @ P_mat - np.eye(dim)))  # (local)
print(f"P^2 = I check: max|P^2 - I| = {P2_err:.2e}")
assert P2_err < 1e-12, f"P^2 != I: error = {P2_err}"

# Diagonalize P to get Z_2 sectors
P_evals, P_evecs = eigh(P_mat)
even_mask = P_evals > 0.5  # (local) eigenvalue +1
odd_mask = P_evals < -0.5   # (local) eigenvalue -1
n_even = int(np.sum(even_mask))  # (local)
n_odd = int(np.sum(odd_mask))    # (local)

print(f"Z_2 sectors: even = {n_even}, odd = {n_odd}, total = {n_even + n_odd}")
print(f"  Expected: even = 64, odd = 56 (from C(16,2) symmetry)")

# Projectors onto Z_2 sectors
Q_even = P_evecs[:, even_mask]  # (dim, n_even) (local)
Q_odd = P_evecs[:, odd_mask]    # (dim, n_odd) (local)
Pi_even = Q_even @ Q_even.T     # (local) projector onto even sector
Pi_odd = Q_odd @ Q_odd.T        # (local) projector onto odd sector

# Verify completeness
proj_check = np.max(np.abs(Pi_even + Pi_odd - np.eye(dim)))  # (local)
print(f"Projector completeness: max|Pi_+ + Pi_- - I| = {proj_check:.2e}")

# ============================================================================
# 5. Diagonalize Hamiltonians and compute diagonal ensemble
# ============================================================================
print("\n" + "=" * 60)
print("STEP 2: Sudden Quench and Diagonal Ensemble")
print("=" * 60)

V_sym = (V_fold + V_fold.T) / 2.0  # (local) symmetrize

# H at tau=0
H_tau0 = build_H_2cell(eps_tau0, eps_tau0, V_sym, V_sym, E_J_tau0, alpha=1.0)
evals_tau0, evecs_tau0 = eigh(H_tau0)

# H at fold
H_fold = build_H_2cell(eps_fold, eps_fold, V_sym, V_sym, E_J_fold, alpha=1.0)
evals_fold, evecs_fold = eigh(H_fold)

print(f"H(tau=0): E_min = {evals_tau0[0]:.6f}, E_max = {evals_tau0[-1]:.6f}")
print(f"H(fold):  E_min = {evals_fold[0]:.6f}, E_max = {evals_fold[-1]:.6f}")

# Verify [H, P] = 0
comm_HP = H_fold @ P_mat - P_mat @ H_fold  # (local)
comm_HP_norm = np.max(np.abs(comm_HP))  # (local)
print(f"[H_fold, P] = 0 check: max|[H,P]| = {comm_HP_norm:.2e}")

comm_HP_tau0 = H_tau0 @ P_mat - P_mat @ H_tau0  # (local)
comm_HP_tau0_norm = np.max(np.abs(comm_HP_tau0))  # (local)
print(f"[H_tau0, P] = 0 check: max|[H,P]| = {comm_HP_tau0_norm:.2e}")

# Ground state at tau=0
gs_tau0 = evecs_tau0[:, 0]  # (local)

# Z_2 parity of the initial ground state
gs_parity_val = gs_tau0 @ P_mat @ gs_tau0  # (local)
print(f"\nInitial ground state Z_2 parity: <GS|P|GS> = {gs_parity_val:+.6f}")
gs_even_weight = gs_tau0 @ Pi_even @ gs_tau0  # (local)
gs_odd_weight = gs_tau0 @ Pi_odd @ gs_tau0    # (local)
print(f"  Even component: {gs_even_weight:.6f}")
print(f"  Odd component:  {gs_odd_weight:.6f}")

# Overlap coefficients: project GS(tau=0) onto fold eigenstates
c_n = evecs_fold.T @ gs_tau0  # (local)
p_n = np.abs(c_n)**2           # (local)

# Verify against stored values
max_cn_diff = np.max(np.abs(np.abs(c_n) - np.abs(c_n_stored)))  # (local)
max_pn_diff = np.max(np.abs(p_n - p_n_stored))  # (local)
print(f"\nCross-check vs s56 stored data:")
print(f"  max||c_n| - |c_n_stored|| = {max_cn_diff:.2e}")
print(f"  max|p_n - p_n_stored| = {max_pn_diff:.2e}")
print(f"  sum(p_n) = {np.sum(p_n):.15f}")

# ============================================================================
# 6. Classify each eigenstate by Z_2 parity
# ============================================================================
print("\n" + "=" * 60)
print("STEP 3: Z_2 Classification of Eigenstates")
print("=" * 60)

# For each eigenstate |n> of H_fold, compute <n|P|n>
z2_expectation = np.zeros(dim)  # (local)
for n in range(dim):
    v = evecs_fold[:, n]  # (local)
    z2_expectation[n] = v @ P_mat @ v

# Since [H, P] = 0, each eigenstate should be a definite Z_2 eigenstate
# (in non-degenerate subspaces). Check how sharp the parity is.
z2_sharp = np.abs(np.abs(z2_expectation) - 1.0)  # (local) deviation from +/-1
max_z2_blur = np.max(z2_sharp)  # (local)
mean_z2_blur = np.mean(z2_sharp)  # (local)

print(f"Z_2 sharpness check (deviation from +/-1):")
print(f"  max|<P> - (+/-1)| = {max_z2_blur:.2e}")
print(f"  mean|<P> - (+/-1)| = {mean_z2_blur:.2e}")

# Classify: +1 = even, -1 = odd
z2_label = np.sign(z2_expectation)  # (local) +1 or -1
n_even_eigstates = int(np.sum(z2_label > 0))  # (local)
n_odd_eigstates = int(np.sum(z2_label < 0))   # (local)
print(f"Eigenstate Z_2 count: even = {n_even_eigstates}, odd = {n_odd_eigstates}")

# Check for degenerate states with ambiguous parity
ambiguous = np.sum(np.abs(z2_expectation) < 0.5)  # (local)
print(f"Ambiguous parity states (|<P>| < 0.5): {ambiguous}")

z2_well_defined = (max_z2_blur < 0.01 and ambiguous == 0)  # (local)
print(f"Z_2 parity well-defined: {z2_well_defined}")

# ============================================================================
# 7. Compute Z_2-odd fraction of Parker pair production
# ============================================================================
print("\n" + "=" * 60)
print("STEP 4: Z_2-Odd Fraction of Parker Pairs")
print("=" * 60)

# The diagonal ensemble weight in the Z_2-odd sector
p_odd = np.sum(p_n[z2_label < 0])   # (local)
p_even = np.sum(p_n[z2_label > 0])  # (local)
n_Z2_ratio = p_odd / (p_odd + p_even)  # (local) this IS n_Z2/n_total

print(f"Diagonal ensemble weight:")
print(f"  Z_2 even: {p_even:.10f}")
print(f"  Z_2 odd:  {p_odd:.10f}")
print(f"  Total:    {p_even + p_odd:.15f}")
print(f"\n  n_Z2 / n_total = {n_Z2_ratio:.10f}")
print(f"  (= fraction of quasiparticle weight in Z_2-odd sector)")

# Alternative calculation: project initial state directly
# |GS(tau=0)> -> Pi_odd |GS(tau=0)> / ||Pi_odd |GS(tau=0)>||
gs_odd_proj = Pi_odd @ gs_tau0  # (local)
gs_even_proj = Pi_even @ gs_tau0  # (local)
weight_odd_direct = np.dot(gs_odd_proj, gs_odd_proj)  # (local)
weight_even_direct = np.dot(gs_even_proj, gs_even_proj)  # (local)
ratio_direct = weight_odd_direct / (weight_odd_direct + weight_even_direct)  # (local)

print(f"\nDirect projection (cross-check):")
print(f"  ||Pi_odd |GS>||^2 = {weight_odd_direct:.10f}")
print(f"  ||Pi_even |GS>||^2 = {weight_even_direct:.10f}")
print(f"  Odd fraction = {ratio_direct:.10f}")
print(f"  Agreement with DE method: {abs(n_Z2_ratio - ratio_direct):.2e}")

# ============================================================================
# 8. Sector-resolved analysis: energy and occupation
# ============================================================================
print("\n" + "=" * 60)
print("STEP 5: Sector-Resolved Energy and Occupation")
print("=" * 60)

# Energy in each Z_2 sector
E_odd = np.sum(p_n[z2_label < 0] * evals_fold[z2_label < 0])  # (local)
E_even = np.sum(p_n[z2_label > 0] * evals_fold[z2_label > 0])  # (local)
E_total = E_odd + E_even  # (local)

print(f"Energy partition:")
print(f"  E_even = {E_even:.6f} M_KK (weight {p_even:.6f})")
print(f"  E_odd  = {E_odd:.6f} M_KK (weight {p_odd:.6f})")
print(f"  E_total = {E_total:.6f} M_KK")
print(f"  E_odd / E_total = {E_odd / E_total:.6f}")

# Mean energy per sector
E_mean_even = E_even / p_even if p_even > 1e-15 else 0.0  # (local)
E_mean_odd = E_odd / p_odd if p_odd > 1e-15 else 0.0      # (local)
print(f"\nMean energy per sector:")
print(f"  <E>_even = {E_mean_even:.6f} M_KK")
print(f"  <E>_odd  = {E_mean_odd:.6f} M_KK")

# ============================================================================
# 9. Mode-resolved |beta_k|^2 by Z_2 sector
# ============================================================================
print("\n" + "=" * 60)
print("STEP 6: Mode-Resolved Bogoliubov Coefficients by Z_2 Sector")
print("=" * 60)

# Build number operators
def build_number_operator(mode_idx):
    """Build n_k = b_k^dag b_k in the pair basis."""
    N_op = np.zeros((dim, dim))  # (local)
    for i, state_i in enumerate(basis):
        if mode_idx in state_i:
            N_op[i, i] = 1.0
    return N_op

n_ops = [build_number_operator(k) for k in range(n_modes_total)]

# Mode occupations in each Z_2 sector
# For each mode k, compute <n_k> restricted to Z_2-odd eigenstates
nk_odd = np.zeros(n_modes_total)  # (local)
nk_even = np.zeros(n_modes_total)  # (local)

for k in range(n_modes_total):
    for n in range(dim):
        v = evecs_fold[:, n]
        nk_val = v @ n_ops[k] @ v  # (local) <n|n_k|n>
        if z2_label[n] < 0:
            nk_odd[k] += p_n[n] * nk_val
        else:
            nk_even[k] += p_n[n] * nk_val

# Normalize to get occupation fractions
nk_total = nk_odd + nk_even  # (local)

print(f"{'Mode':>6} {'Cell':>4} {'k_loc':>5} {'Branch':>8} {'<n_k>_total':>12} "
      f"{'<n_k>_even':>12} {'<n_k>_odd':>12} {'f_odd':>10}")
print("-" * 80)

for k in range(n_modes_total):
    cell = 1 if k < N_modes else 2  # (local)
    k_loc = k if k < N_modes else k - N_modes  # (local)
    branch = branch_labels[k]
    f_odd_k = nk_odd[k] / nk_total[k] if nk_total[k] > 1e-15 else 0.0  # (local)
    print(f"  {k:4d}   {cell:3d}   {k_loc:4d}   {branch:>6s}   {nk_total[k]:12.8f}   "
          f"{nk_even[k]:12.8f}   {nk_odd[k]:12.8f}   {f_odd_k:10.6f}")

print(f"\nSum <n_k>_total = {np.sum(nk_total):.6f} (should be 2)")
print(f"Sum <n_k>_even  = {np.sum(nk_even):.6f}")
print(f"Sum <n_k>_odd   = {np.sum(nk_odd):.6f}")

# Branch-resolved Z_2-odd fractions
B2_modes = [0,1,2,3,8,9,10,11]  # (local)
B1_modes = [4, 12]  # (local)
B3_modes = [5,6,7,13,14,15]  # (local)

f_odd_B2 = np.sum(nk_odd[B2_modes]) / np.sum(nk_total[B2_modes])  # (local)
f_odd_B1 = np.sum(nk_odd[B1_modes]) / np.sum(nk_total[B1_modes])  # (local)
f_odd_B3 = np.sum(nk_odd[B3_modes]) / np.sum(nk_total[B3_modes])  # (local)

print(f"\nBranch-resolved Z_2-odd fractions:")
print(f"  B2 (flat band):   f_odd = {f_odd_B2:.6f}")
print(f"  B1 (acoustic):    f_odd = {f_odd_B1:.6f}")
print(f"  B3 (optical):     f_odd = {f_odd_B3:.6f}")

# ============================================================================
# 10. Connection to Parker pair production count
# ============================================================================
print("\n" + "=" * 60)
print("STEP 7: Parker Pair Production Count")
print("=" * 60)

# The total 59.8 pairs (from canonical) are produced from the full fabric
# (N_cells = 32). The fraction in Z_2-odd scales as n_Z2_ratio.
n_Z2_abs = n_pairs * n_Z2_ratio  # (local) absolute count in Z_2-odd
n_even_abs = n_pairs * (1.0 - n_Z2_ratio)  # (local)

print(f"Total Parker pairs (canonical): {n_pairs}")
print(f"Z_2-odd fraction: {n_Z2_ratio:.6f}")
print(f"  Z_2-odd pairs:  {n_Z2_abs:.2f}")
print(f"  Z_2-even pairs: {n_even_abs:.2f}")

# Energy-weighted Z_2-odd fraction
E_Z2_frac = E_odd / E_total if abs(E_total) > 1e-15 else 0.0  # (local)
print(f"\nEnergy-weighted Z_2-odd fraction: {E_Z2_frac:.6f}")

# ============================================================================
# 11. GGE temperature in Z_2-odd sector
# ============================================================================
print("\n" + "=" * 60)
print("STEP 8: Z_2-Odd Sector GGE Temperature")
print("=" * 60)

# Entropy in each sector
p_n_odd_normalized = p_n[z2_label < 0] / p_odd if p_odd > 1e-15 else p_n[z2_label < 0]  # (local)
p_n_even_normalized = p_n[z2_label > 0] / p_even if p_even > 1e-15 else p_n[z2_label > 0]  # (local)

# Remove zeros for log
mask_o = p_n_odd_normalized > 1e-30  # (local)
mask_e = p_n_even_normalized > 1e-30  # (local)
S_odd = -np.sum(p_n_odd_normalized[mask_o] * np.log(p_n_odd_normalized[mask_o]))  # (local)
S_even = -np.sum(p_n_even_normalized[mask_e] * np.log(p_n_even_normalized[mask_e]))  # (local)

S_odd_max = np.log(n_odd_eigstates) if n_odd_eigstates > 0 else 0.0  # (local)
S_even_max = np.log(n_even_eigstates) if n_even_eigstates > 0 else 0.0  # (local)

print(f"Entropy (within sector, normalized):")
print(f"  S_even = {S_even:.6f} nats (max = {S_even_max:.6f})")
print(f"  S_odd  = {S_odd:.6f} nats (max = {S_odd_max:.6f})")
print(f"  S_even/S_max = {S_even/S_even_max:.6f}" if S_even_max > 0 else "")
print(f"  S_odd/S_max  = {S_odd/S_odd_max:.6f}" if S_odd_max > 0 else "")

# Effective number of participating states per sector
N_eff_odd = np.exp(S_odd)  # (local)
N_eff_even = np.exp(S_even)  # (local)
print(f"\nEffective participating states:")
print(f"  N_eff_even = {N_eff_even:.2f} / {n_even_eigstates}")
print(f"  N_eff_odd  = {N_eff_odd:.2f} / {n_odd_eigstates}")

# ============================================================================
# 12. Consistency: Leggett DM channel identification
# ============================================================================
print("\n" + "=" * 60)
print("STEP 9: Leggett DM Channel Consistency")
print("=" * 60)

# The DM candidate is the Leggett mode = inter-band coherence.
# In the dimer picture, Z_2-odd = antibonding = relative phase mode.
# This is exactly the Leggett channel (relative phase oscillation
# between the two cells).
#
# Condensed matter analog: In a Josephson junction array, the
# antisymmetric mode corresponds to the relative phase oscillation
# (Leggett mode), while the symmetric mode is the center-of-mass
# phase (Goldstone). The Leggett mode is gapped (omega_L1 = 0.138 M_KK),
# CPT-neutral, and non-annihilating -- exactly the DM properties.

# Check: does the Z_2-odd fraction match the Leggett DM fraction?
# From Omega_DM h^2 = 0.120 (Planck), Omega_b h^2 = 0.0224
# The DM/baryon ratio is ~5.4. If DM = Z_2-odd pairs, the DM fraction
# of the GGE should be related to n_Z2_ratio.
# But the direct observable is n_Z2/n_total itself.

print(f"Z_2-odd = antibonding = Leggett channel = DM candidate")
print(f"Z_2-even = bonding = Goldstone + Higgs channels = visible sector")
print(f"\nKey result: f_DM(Z_2) = n_Z2/n_total = {n_Z2_ratio:.6f}")

# The Omega_DM / Omega_total is not simply n_Z2_ratio because the
# energy per quasiparticle differs between sectors. The energy-weighted
# fraction is the better proxy:
print(f"Energy-weighted f_DM = E_odd/E_total = {E_Z2_frac:.6f}")

# ============================================================================
# 13. Gate verdict
# ============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: S75-E2-DIMER-Z2")
print("=" * 78)

GATE_LO = 0.1  # (local)
GATE_HI = 0.5  # (local)

if not z2_well_defined:
    verdict = "FAIL"
    reason = f"Z_2 parity not well-defined (max blur = {max_z2_blur:.4f}, ambiguous = {ambiguous})"
elif GATE_LO <= n_Z2_ratio <= GATE_HI:
    verdict = "PASS"
    reason = f"n_Z2/n_total = {n_Z2_ratio:.6f} in [{GATE_LO}, {GATE_HI}]"
else:
    verdict = "INFO"
    reason = f"n_Z2/n_total = {n_Z2_ratio:.6f} outside [{GATE_LO}, {GATE_HI}] but computable"

print(f"  Criterion: n_Z2/n_total in [{GATE_LO}, {GATE_HI}]")
print(f"  Computed:  n_Z2/n_total = {n_Z2_ratio:.6f}")
print(f"  Z_2 well-defined: {z2_well_defined}")
print(f"  Verdict: {verdict}")
print(f"  Reason: {reason}")

# ============================================================================
# 14. Save results
# ============================================================================
print("\n" + "=" * 60)
print("Saving results...")
print("=" * 60)

np.savez(
    os.path.join(SCRIPT_DIR, 's75_dimer_z2_pair_production.npz'),
    # Z_2 structure
    n_even=n_even,
    n_odd=n_odd,
    P2_err=P2_err,
    comm_HP_norm=comm_HP_norm,
    z2_expectation=z2_expectation,
    z2_label=z2_label,
    z2_well_defined=z2_well_defined,
    max_z2_blur=max_z2_blur,
    # Main results
    n_Z2_ratio=n_Z2_ratio,
    p_odd=p_odd,
    p_even=p_even,
    E_odd=E_odd,
    E_even=E_even,
    E_Z2_frac=E_Z2_frac,
    # Mode-resolved
    nk_odd=nk_odd,
    nk_even=nk_even,
    nk_total=nk_total,
    f_odd_B2=f_odd_B2,
    f_odd_B1=f_odd_B1,
    f_odd_B3=f_odd_B3,
    # Parker pair count
    n_Z2_abs=n_Z2_abs,
    n_even_abs=n_even_abs,
    # Sector entropy
    S_odd=S_odd,
    S_even=S_even,
    N_eff_odd=N_eff_odd,
    N_eff_even=N_eff_even,
    # Initial state
    gs_parity_val=gs_parity_val,
    gs_even_weight=gs_even_weight,
    gs_odd_weight=gs_odd_weight,
    # Gate
    gate_name='S75-E2-DIMER-Z2',
    gate_verdict=verdict,
    gate_reason=reason,
)

elapsed = time.time() - t0  # (local)
print(f"\nDone. Elapsed: {elapsed:.1f}s")
print(f"Output: computations/session-75/s75_dimer_z2_pair_production.npz")
