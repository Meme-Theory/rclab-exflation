#!/usr/bin/env python3
"""
s58_npair2_integ.py — N_pair = 2 Exact Diagonalization on 2-Cell System
=========================================================================

Gate: NPAIR2-INTEG-58
  PASS: <r> > 0.45 (integrability broken; CC solution path opens)
  FAIL: <r> < 0.40 (integrability persists; CC remains locked)
  INFO: <r> in [0.40, 0.45] (intermediate; N_pair = 3 needed)

Physics: At N_pair = 1, a single Cooper pair in a 2-cell Josephson array
is trivially integrable (non-interacting). At N_pair = 2, pair-pair
interactions (Pauli blocking + pairing vertex) emerge. If these break
Richardson-Gaudin integrability, the GGE thermalizes and the CC can relax.

Method:
  1. Construct 2-cell BCS Hamiltonian in the N_pair = 2 pair Fock space
     (16 pair-slots, C(16,2) = 120 two-pair states)
  2. Exact diagonalization
  3. Level spacing statistics: <r> ratio
  4. Richardson-Gaudin integral check
  5. GGE comparison: sudden quench from tau=0 to tau_fold

Session: S58 W1-1
Agent: landau-condensed-matter-theorist
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
    tau_fold, E_cond, N_dof_BCS, t_Planck, t_universe_s,
    hbar_GeV_s, M_KK
)

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # 8 single-particle energies at tau=0
V_fold   = d56['V_fold']        # 8x8 pairing matrix (tau-independent)
E_J_fold = float(d56['E_J_fold'])  # Josephson coupling at fold
E_J_tau0 = float(d56['E_J_tau0'])  # Josephson coupling at tau=0
tau_fold_actual = float(d56['tau_fold_actual'])

# S54 for cross-check
d54 = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
V_bare = d54['V_bare_cont']     # 8x8 pairing matrix (cross-check)

N_modes = 8  # modes per cell (local)
N_cells = 2   # cells
N_pair  = 2  # Cooper pairs (local)

print("=" * 70)
print("S58 W1-1: N_pair = 2 Exact Diagonalization — NPAIR2-INTEG-58")
print("=" * 70)
print(f"tau_fold = {tau_fold_actual:.6f}")
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"E_J_tau0 = {E_J_tau0:.4f} M_KK")
print(f"N_modes/cell = {N_modes}, N_cells = {N_cells}, N_pair = {N_pair}")
print(f"eps_fold = {eps_fold}")

# Cross-check V matrices
V_diff = np.max(np.abs(V_fold - V_bare))
print(f"\nV_fold vs V_bare_cont max diff = {V_diff:.2e} (should be ~1e-30)")
assert V_diff < 1e-10, f"V matrices disagree: diff = {V_diff}"

# =====================================================================
#  2. CONSTRUCT PAIR FOCK SPACE
# =====================================================================
# A "pair-slot" is (mode_index, cell_index).
# Total pair-slots = N_modes * N_cells = 16.
# A state with N_pair = 2 is specified by choosing 2 of these 16 slots.
# Pair-slot i in [0..7] = mode i in cell 0
# Pair-slot i in [8..15] = mode (i-8) in cell 1

N_slots = N_modes * N_cells  # 16
pair_states = list(combinations(range(N_slots), N_pair))
dim = len(pair_states)
print(f"\nFock space: C({N_slots},{N_pair}) = {dim} two-pair states")

# Map pair-slot to (mode, cell)
def slot_to_mode_cell(s):
    """Convert pair-slot index to (mode_index, cell_index)."""
    return (s % N_modes, s // N_modes)

# Pre-compute for each basis state: which modes in which cells
state_info = []
for idx, (s1, s2) in enumerate(pair_states):
    m1, c1 = slot_to_mode_cell(s1)
    m2, c2 = slot_to_mode_cell(s2)
    state_info.append(((m1, c1), (m2, c2)))

# Index lookup: pair_states tuple -> index
state_index = {s: i for i, s in enumerate(pair_states)}


# =====================================================================
#  3. CONSTRUCT HAMILTONIAN
# =====================================================================

def build_H_BCS_2cell(eps, V, E_J):
    """
    Build the full BCS + Josephson Hamiltonian for N_pair=2 on a 2-cell system.

    H = H_kinetic + H_pairing + H_Josephson

    H_kinetic: Sum over occupied pair-slots of 2*eps[mode]
               (factor 2 because each pair occupies both spin-up and spin-down)

    H_pairing: For each cell independently:
               V[k,l] * (pair_k^dag pair_l) scatters pair from mode l to mode k
               within the SAME cell.

    H_Josephson: -(E_J/2) * (B_1^dag B_2 + h.c.)
                 where B_i = Sum_k b_{k,i} is the collective pair operator.
                 This tunnels a pair from ANY mode in one cell to ANY mode
                 in the other cell. This matches the S56 convention exactly.

    Parameters
    ----------
    eps : (N_modes,) array — single-particle energies
    V   : (N_modes, N_modes) array — pairing interaction matrix
    E_J : float — Josephson coupling strength

    Returns
    -------
    H : (dim, dim) array — Hamiltonian matrix in the pair Fock basis
    """
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, (s1, s2) in enumerate(pair_states):
        (m1, c1), (m2, c2) = state_info[i]

        # --- Diagonal: kinetic energy ---
        # Each occupied pair contributes 2 * eps[mode]
        H[i, i] += 2.0 * eps[m1] + 2.0 * eps[m2]

        # --- Pairing interaction (within each cell) ---
        # V[k,l] scatters a pair from mode l to mode k in the same cell.
        # For this to act on state |s1, s2>, one of the pairs must be in mode l
        # of some cell, and the result puts it in mode k of the same cell,
        # provided mode k is not already occupied.

        # Scatter pair 1: mode m1 in cell c1 -> mode k in cell c1
        for k in range(N_modes):
            if k == m1:
                # Diagonal pairing: V[m1,m1] contributes to diagonal
                H[i, i] -= V[m1, m1]
                continue
            # Check the other pair isn't already in slot (k, c1)
            new_slot1 = c1 * N_modes + k
            old_slot1 = c1 * N_modes + m1
            # The new state has new_slot1 instead of old_slot1, plus s2
            if new_slot1 == s2:
                continue  # Pauli blocked
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                # Sign: for pair operators, sign is always +1 (pairs are bosonic composites)
                H[j, i] -= V[k, m1]

        # Scatter pair 2: mode m2 in cell c2 -> mode k in cell c2
        for k in range(N_modes):
            if k == m2:
                H[i, i] -= V[m2, m2]
                continue
            new_slot2 = c2 * N_modes + k
            old_slot2 = c2 * N_modes + m2
            if new_slot2 == s1:
                continue  # Pauli blocked
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] -= V[k, m2]

        # --- Josephson tunneling (COLLECTIVE) ---
        # H_J = -(E_J/2)(B_1^dag B_2 + h.c.)
        # B_i = Sum_k b_{k,i} tunnels a pair from ANY mode in one cell
        # to ANY mode in the other cell. Matches S56 convention.

        # Tunnel pair 1: (m1, c1) -> (any mode l, 1-c1)
        for l in range(N_modes):
            new_slot1 = (1 - c1) * N_modes + l
            if new_slot1 == s2:
                continue  # Pauli blocked
            new_state = tuple(sorted([new_slot1, s2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

        # Tunnel pair 2: (m2, c2) -> (any mode l, 1-c2)
        for l in range(N_modes):
            new_slot2 = (1 - c2) * N_modes + l
            if new_slot2 == s1:
                continue  # Pauli blocked
            new_state = tuple(sorted([s1, new_slot2]))
            if new_state in state_index:
                j = state_index[new_state]
                H[j, i] += -E_J / 2.0

    # Symmetrize (should be Hermitian by construction, but enforce numerically)
    H = 0.5 * (H + H.T)

    return H


# =====================================================================
#  4. BUILD AND DIAGONALIZE
# =====================================================================

print("\n--- Building Hamiltonians ---")

# (a) Full Hamiltonian at the fold (with Josephson)
H_fold_full = build_H_BCS_2cell(eps_fold, V_fold, E_J_fold)
print(f"H_fold_full: {H_fold_full.shape}, Hermiticity check = {np.max(np.abs(H_fold_full - H_fold_full.T)):.2e}")

# (b) Hamiltonian at fold WITHOUT Josephson (control: two isolated cells)
H_fold_noJ = build_H_BCS_2cell(eps_fold, V_fold, 0.0)
print(f"H_fold_noJ:  {H_fold_noJ.shape}, Hermiticity check = {np.max(np.abs(H_fold_noJ - H_fold_noJ.T)):.2e}")

# (c) Hamiltonian at tau=0 (for quench initial state)
H_tau0_full = build_H_BCS_2cell(eps_tau0, V_fold, E_J_tau0)
print(f"H_tau0_full: {H_tau0_full.shape}, Hermiticity check = {np.max(np.abs(H_tau0_full - H_tau0_full.T)):.2e}")

# Diagonalize all three
print("\n--- Diagonalizing ---")
evals_fold_full, evecs_fold_full = eigh(H_fold_full)
evals_fold_noJ, evecs_fold_noJ  = eigh(H_fold_noJ)
evals_tau0_full, evecs_tau0_full = eigh(H_tau0_full)

print(f"E_GS(fold, full J) = {evals_fold_full[0]:.8f} M_KK")
print(f"E_GS(fold, no J)   = {evals_fold_noJ[0]:.8f} M_KK")
print(f"E_GS(tau=0, full J) = {evals_tau0_full[0]:.8f} M_KK")
print(f"Spectrum range (fold, full J): [{evals_fold_full[0]:.4f}, {evals_fold_full[-1]:.4f}]")


# =====================================================================
#  5. LEVEL SPACING STATISTICS
# =====================================================================

def level_spacing_ratio(eigenvalues, unfold=True):
    """
    Compute the mean adjacent gap ratio <r> for a spectrum.

    <r> = <min(s_n, s_{n+1}) / max(s_n, s_{n+1})>

    Poisson (integrable): <r> ~ 0.386
    GOE (chaotic):        <r> ~ 0.530
    GUE:                  <r> ~ 0.603

    If unfold=True, first unfold the spectrum using a polynomial fit
    to the cumulative level density.
    """
    E = np.sort(eigenvalues)

    if unfold:
        # Unfold: map E -> N(E) where N is the smoothed staircase
        # Use polynomial unfolding (degree 5)
        N = np.arange(1, len(E) + 1)
        # Fit cumulative density
        poly = np.polyfit(E, N, deg=min(5, len(E) - 1))
        N_smooth = np.polyval(poly, E)
        # Unfolded levels
        E_unf = N_smooth
    else:
        E_unf = E

    # Spacings
    s = np.diff(E_unf)
    # Remove near-zero spacings (degeneracies)
    s = s[s > 1e-12]

    if len(s) < 3:
        return 0.0, np.array([])

    # Adjacent gap ratios
    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])

    return np.mean(r_n), r_n


print("\n" + "=" * 70)
print("LEVEL SPACING STATISTICS")
print("=" * 70)

# Full spectrum analysis
r_fold_full, r_dist_fold_full = level_spacing_ratio(evals_fold_full)
r_fold_noJ, r_dist_fold_noJ = level_spacing_ratio(evals_fold_noJ)
r_tau0_full, r_dist_tau0_full = level_spacing_ratio(evals_tau0_full)

print(f"\n<r> (fold, full E_J = {E_J_fold:.3f}): {r_fold_full:.6f}")
print(f"<r> (fold, E_J = 0):               {r_fold_noJ:.6f}")
print(f"<r> (tau=0, full E_J = {E_J_tau0:.3f}): {r_tau0_full:.6f}")
print(f"\nPoisson reference:  0.386")
print(f"GOE reference:      0.530")
print(f"Gate threshold:     0.450")

# Also compute without unfolding as cross-check
r_fold_full_raw, _ = level_spacing_ratio(evals_fold_full, unfold=False)
r_fold_noJ_raw, _  = level_spacing_ratio(evals_fold_noJ, unfold=False)
print(f"\nCross-check (no unfolding):")
print(f"<r> (fold, full J, raw): {r_fold_full_raw:.6f}")
print(f"<r> (fold, no J, raw):   {r_fold_noJ_raw:.6f}")

# Standard error
r_stderr_full = np.std(r_dist_fold_full) / np.sqrt(len(r_dist_fold_full))
r_stderr_noJ  = np.std(r_dist_fold_noJ) / np.sqrt(len(r_dist_fold_noJ))
print(f"\nStandard error:")
print(f"  fold full J: <r> = {r_fold_full:.4f} +/- {r_stderr_full:.4f} (N_gaps = {len(r_dist_fold_full)})")
print(f"  fold no J:   <r> = {r_fold_noJ:.4f} +/- {r_stderr_noJ:.4f} (N_gaps = {len(r_dist_fold_noJ)})")


# =====================================================================
#  5b. SYMMETRY-RESOLVED LEVEL STATISTICS
# =====================================================================
# The 2-cell system has a Z_2 exchange symmetry (cell 1 <-> cell 2).
# Level repulsion is sector-wise. We must resolve the spectrum by
# the Z_2 quantum number to get a clean <r>.

print("\n" + "-" * 70)
print("SYMMETRY-RESOLVED ANALYSIS (Z_2 cell exchange)")
print("-" * 70)

# Build the Z_2 exchange operator: P |s1, s2> = |P(s1), P(s2)>
# where P swaps cell 0 <-> cell 1 for each pair-slot.
def swap_slot(s):
    """Swap cell index of a pair-slot."""
    mode = s % N_modes
    cell = s // N_modes
    return (1 - cell) * N_modes + mode

P_mat = np.zeros((dim, dim), dtype=np.float64)
for i, (s1, s2) in enumerate(pair_states):
    new_s1 = swap_slot(s1)
    new_s2 = swap_slot(s2)
    new_state = tuple(sorted([new_s1, new_s2]))
    j = state_index[new_state]
    P_mat[j, i] = 1.0

# Verify P^2 = I
P2_check = np.max(np.abs(P_mat @ P_mat - np.eye(dim)))
print(f"P^2 = I check: max|P^2 - I| = {P2_check:.2e}")

# Verify [H, P] = 0
commHP = H_fold_full @ P_mat - P_mat @ H_fold_full
comm_norm = np.max(np.abs(commHP))
print(f"[H_fold, P] = 0 check: max|[H,P]| = {comm_norm:.2e}")

# Project onto Z_2 sectors
# P eigenvalues are +1 (even) and -1 (odd)
P_evals, P_evecs = eigh(P_mat)
# P_evals should be +1 or -1
even_mask = P_evals > 0.5
odd_mask  = P_evals < -0.5
n_even = np.sum(even_mask)
n_odd  = np.sum(odd_mask)
print(f"Z_2 sectors: even = {n_even}, odd = {n_odd}, total = {n_even + n_odd}")

# Diagonalize H in each Z_2 sector
# Project H into even sector
Q_even = P_evecs[:, even_mask]  # (dim, n_even)
H_even = Q_even.T @ H_fold_full @ Q_even
evals_even, evecs_even_proj = eigh(H_even)

Q_odd = P_evecs[:, odd_mask]
H_odd = Q_odd.T @ H_fold_full @ Q_odd
evals_odd, evecs_odd_proj = eigh(H_odd)

# Compute <r> in each sector
r_even, r_dist_even = level_spacing_ratio(evals_even)
r_odd, r_dist_odd   = level_spacing_ratio(evals_odd)

r_even_raw, _ = level_spacing_ratio(evals_even, unfold=False)
r_odd_raw, _  = level_spacing_ratio(evals_odd, unfold=False)

print(f"\n<r> (even sector, {n_even} levels): {r_even:.6f} (raw: {r_even_raw:.6f})")
print(f"<r> (odd sector, {n_odd} levels):  {r_odd:.6f} (raw: {r_odd_raw:.6f})")

# Combined sector-resolved <r>: weighted average
r_combined = (len(r_dist_even) * r_even + len(r_dist_odd) * r_odd) / (len(r_dist_even) + len(r_dist_odd))
print(f"<r> (sector-resolved combined): {r_combined:.6f}")

r_stderr_even = np.std(r_dist_even) / np.sqrt(len(r_dist_even)) if len(r_dist_even) > 0 else 0
r_stderr_odd  = np.std(r_dist_odd) / np.sqrt(len(r_dist_odd)) if len(r_dist_odd) > 0 else 0
print(f"  even: <r> = {r_even:.4f} +/- {r_stderr_even:.4f} (N_gaps = {len(r_dist_even)})")
print(f"  odd:  <r> = {r_odd:.4f} +/- {r_stderr_odd:.4f} (N_gaps = {len(r_dist_odd)})")

# Do the same for no-J control
H_even_noJ = Q_even.T @ H_fold_noJ @ Q_even
H_odd_noJ  = Q_odd.T @ H_fold_noJ @ Q_odd
evals_even_noJ, _ = eigh(H_even_noJ)
evals_odd_noJ, _  = eigh(H_odd_noJ)
r_even_noJ, r_dist_even_noJ = level_spacing_ratio(evals_even_noJ)
r_odd_noJ, r_dist_odd_noJ   = level_spacing_ratio(evals_odd_noJ)
r_combined_noJ = (len(r_dist_even_noJ) * r_even_noJ + len(r_dist_odd_noJ) * r_odd_noJ) / max(1, len(r_dist_even_noJ) + len(r_dist_odd_noJ))
print(f"\nControl (E_J = 0):")
print(f"  <r> even: {r_even_noJ:.6f}, odd: {r_odd_noJ:.6f}, combined: {r_combined_noJ:.6f}")


# =====================================================================
#  6. RICHARDSON-GAUDIN INTEGRALS OF MOTION
# =====================================================================

print("\n" + "=" * 70)
print("RICHARDSON-GAUDIN INTEGRALS")
print("=" * 70)

# The Richardson-Gaudin model has N_modes integrals per cell:
#   R_k = n_k + g * Sum_{l != k} [ V_{kl} / (eps_k - eps_l) ] * (pair_k^dag pair_l + h.c.)
# where n_k is the pair number operator for mode k.
# These satisfy [R_k, R_l] = 0 and H_BCS = Sum_k 2*eps_k * R_k + const.
#
# For the 2-cell system, the Josephson coupling H_J is NOT part of the
# Richardson-Gaudin integrable structure. The question is whether [H, R_k] = 0
# survives when H includes H_J.

def build_pair_number_op(mode, cell):
    """Build n_{mode,cell} operator in pair Fock basis."""
    n_op = np.zeros((dim, dim))
    slot = cell * N_modes + mode
    for i, (s1, s2) in enumerate(pair_states):
        if s1 == slot or s2 == slot:
            n_op[i, i] = 1.0
    return n_op

def build_pair_hop_op(k, l, cell):
    """Build pair_k^dag pair_l operator for modes k,l in given cell."""
    op = np.zeros((dim, dim))
    slot_k = cell * N_modes + k
    slot_l = cell * N_modes + l
    for i, (s1, s2) in enumerate(pair_states):
        # pair_l must be occupied, pair_k must be unoccupied
        if slot_l in (s1, s2) and slot_k not in (s1, s2):
            # Replace slot_l with slot_k
            if s1 == slot_l:
                new_state = tuple(sorted([slot_k, s2]))
            else:
                new_state = tuple(sorted([s1, slot_k]))
            if new_state in state_index:
                j = state_index[new_state]
                op[j, i] = 1.0
    return op

# Build Richardson-Gaudin integrals for each cell
# Use a coupling constant g that matches the BCS Hamiltonian structure
# H_BCS = Sum_k 2*eps_k * n_k - Sum_{k,l} V_{kl} pair_k^dag pair_l
# RG form: R_k = n_k - Sum_{l!=k} V_{kl}/(2*(eps_k - eps_l)) * (pair_k^dag pair_l + pair_l^dag pair_k)
# such that [R_k, H_BCS] = 0 IF V has the right structure (separable: V_{kl} = g for all k,l)

# For a general non-separable V, Richardson-Gaudin integrability is NOT guaranteed.
# Let's compute [H, R_k] directly to test.

print("\nBuilding Richardson-Gaudin integrals for each cell...")

# For the RG model with interaction V_{kl}, the integrals are:
# R_k^{(c)} = n_k^{(c)} + Sum_{l != k} (V_{kl}/(eps_k - eps_l)) * S^+_k S^-_l
# where S^+_k = pair_k^dag, S^-_k = pair_k
# This is exact for the single-cell BCS Hamiltonian with SEPARABLE interaction.
# For general V_{kl}, there's no standard RG form.

# Instead, let's test integrability more directly: check if the single-cell
# BCS Hamiltonian commutes with the pair number operators or any simple integrals.

# Actually, the correct approach: the standard Richardson-Gaudin model has
# V_{kl} = g (constant, separable). Our V_{kl} is NOT separable.
# For non-separable V, there are no known integrals of motion in general.
# Let's quantify this by computing [H_BCS, n_k] for the single-cell problem.

# First build single-cell BCS Hamiltonian in the 2-cell Fock space
H_BCS_cell0 = np.zeros((dim, dim))
for k in range(N_modes):
    n_k = build_pair_number_op(k, 0)
    H_BCS_cell0 += 2.0 * eps_fold[k] * n_k
    for l in range(N_modes):
        hop = build_pair_hop_op(k, l, 0)
        H_BCS_cell0 -= V_fold[k, l] * hop

# Check: how many independent integrals commute with H_fold_full?
# Method: compute [H, O] for candidate operators
# Candidates: pair number operators n_k^{(c)} for each mode and cell

print("\n[H_full, n_k^(cell)] norms:")
print("  (If small: n_k approximately conserved -> integrable)")
comm_norms_full = np.zeros((N_cells, N_modes))
for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c)
        comm = H_fold_full @ n_k - n_k @ H_fold_full
        comm_norms_full[c, k] = np.linalg.norm(comm, 'fro')

print(f"  Cell 0: {comm_norms_full[0]}")
print(f"  Cell 1: {comm_norms_full[1]}")
print(f"  Max norm: {np.max(comm_norms_full):.6f}")

# Compare with H_noJ
print("\n[H_noJ, n_k^(cell)] norms (control):")
comm_norms_noJ = np.zeros((N_cells, N_modes))
for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c)
        comm = H_fold_noJ @ n_k - n_k @ H_fold_noJ
        comm_norms_noJ[c, k] = np.linalg.norm(comm, 'fro')

print(f"  Cell 0: {comm_norms_noJ[0]}")
print(f"  Cell 1: {comm_norms_noJ[1]}")
print(f"  Max norm: {np.max(comm_norms_noJ):.6f}")

# Total pair number N_total = Sum_k Sum_c n_k^(c) should commute (particle conservation)
N_total = np.zeros((dim, dim))
for c in range(N_cells):
    for k in range(N_modes):
        N_total += build_pair_number_op(k, c)
comm_N = H_fold_full @ N_total - N_total @ H_fold_full
print(f"\n[H_full, N_total] = {np.linalg.norm(comm_N, 'fro'):.2e} (should be ~0: pair conservation)")

# Cell pair number N_cell = Sum_k n_k^(cell)
N_cell0 = np.zeros((dim, dim))
N_cell1 = np.zeros((dim, dim))
for k in range(N_modes):
    N_cell0 += build_pair_number_op(k, 0)
    N_cell1 += build_pair_number_op(k, 1)

comm_Nc0 = H_fold_full @ N_cell0 - N_cell0 @ H_fold_full
comm_Nc0_noJ = H_fold_noJ @ N_cell0 - N_cell0 @ H_fold_noJ
print(f"[H_full, N_cell0] = {np.linalg.norm(comm_Nc0, 'fro'):.6f} (broken by Josephson)")
print(f"[H_noJ, N_cell0]  = {np.linalg.norm(comm_Nc0_noJ, 'fro'):.2e} (conserved without J)")

# Build proper RG integrals for the separable part of V
# Decompose V = g * |u><u| + V_remainder
# SVD of V to find the separable component
U_V, S_V, Vt_V = np.linalg.svd(V_fold)
print(f"\nV_fold SVD singular values: {S_V}")
print(f"Separability ratio (s1/trace): {S_V[0]/np.sum(S_V):.4f}")
# If s1 dominates, V is approximately separable

# Build RG integrals using the separable approximation
# g_eff = S_V[0], u_k = U_V[:,0]
g_eff = S_V[0]
u = U_V[:, 0]
print(f"g_eff = {g_eff:.6f}, u = {u}")

# RG integrals for separable model: R_k = S_z^k + g * Sum_{l!=k} (S^+_k S^-_l + S^-_k S^+_l) / (eps_k - eps_l)
# where the "coupling" is weighted by u_k * u_l
# Standard form: R_k = S_z^k + 2*g * Sum_{l!=k} u_k*u_l * (S^+_k S^-_l / (eps_k - eps_l))

# Actually, let's just directly count the number of mutually commuting operators
# that also commute with H. This gives the number of independent integrals.

# Strategy: diagonalize H in the full space, then check the entropy of the
# eigenstates. If integrable, eigenstates have low entanglement.

# More directly: count number of independent conservation laws by checking
# if there exist operators O such that [H, O] = 0 and O is not a function of H.
# The number of such independent O is the number of integrals of motion.

# For an integrable system of N_slots "spins", we need N_slots = 16 independent integrals.
# Total pair number N = 2 is always conserved (we work in fixed-N sector).
# Z_2 parity is another.

# Let's use a more systematic approach: compute the participation entropy
# of eigenstates in the occupation number basis.

print("\n" + "=" * 70)
print("EIGENSTATE STRUCTURE ANALYSIS")
print("=" * 70)

# Participation ratio in the pair-occupation basis
# IPR = Sum_i |<i|psi>|^4, PR = 1/IPR
# For a localized state: IPR ~ 1, PR ~ 1
# For a random state: IPR ~ 1/dim, PR ~ dim

PR_fold = np.zeros(dim)
for n in range(dim):
    psi = evecs_fold_full[:, n]
    ipr = np.sum(psi**4)
    PR_fold[n] = 1.0 / ipr if ipr > 0 else 0.0

PR_noJ = np.zeros(dim)
evecs_noJ = eigh(H_fold_noJ)[1]
for n in range(dim):
    psi = evecs_noJ[:, n]
    ipr = np.sum(psi**4)
    PR_noJ[n] = 1.0 / ipr if ipr > 0 else 0.0

print(f"Mean participation ratio (full J): {np.mean(PR_fold):.2f} / {dim}")
print(f"Mean participation ratio (no J):   {np.mean(PR_noJ):.2f} / {dim}")
print(f"PR ratio (full/noJ):               {np.mean(PR_fold)/np.mean(PR_noJ):.3f}")


# =====================================================================
#  7. GGE OCCUPATION NUMBERS AND QUENCH DYNAMICS
# =====================================================================

print("\n" + "=" * 70)
print("QUENCH DYNAMICS: tau=0 -> tau_fold")
print("=" * 70)

# Ground state of H(tau=0)
psi0 = evecs_tau0_full[:, 0]
print(f"Initial state: GS of H(tau=0), E = {evals_tau0_full[0]:.6f}")

# Overlap with fold eigenstates
c_n = evecs_fold_full.T @ psi0  # overlap coefficients
p_n = c_n**2                     # probabilities
print(f"Sum |c_n|^2 = {np.sum(p_n):.10f} (should be 1)")

# Diagonal ensemble energy
E_DE = np.sum(p_n * evals_fold_full)
print(f"Diagonal ensemble energy: {E_DE:.6f}")
print(f"Ground state energy (fold): {evals_fold_full[0]:.6f}")
print(f"Excitation energy: {E_DE - evals_fold_full[0]:.6f}")

# Diagonal ensemble entropy
p_nz = p_n[p_n > 1e-30]
S_DE = -np.sum(p_nz * np.log(p_nz))
print(f"Diagonal ensemble entropy: {S_DE:.6f}")
print(f"Maximum entropy (log {dim}): {np.log(dim):.6f}")
print(f"S_DE / S_max: {S_DE / np.log(dim):.6f}")

# Excitation probability
P_exc = 1.0 - p_n[0]
print(f"P_exc = 1 - |<GS_fold|GS_tau0>|^2 = {P_exc:.8f}")

# GGE occupation numbers: <n_k^(c)>_DE for each mode and cell
nk_DE_2pair = np.zeros((N_cells, N_modes))
for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c)
        # <n_k>_DE = Sum_n p_n <n|n_k|n>
        nk_DE_2pair[c, k] = np.sum(p_n * np.diag(evecs_fold_full.T @ n_k @ evecs_fold_full))

print(f"\nGGE pair occupations (N_pair = 2):")
print(f"  Cell 0: {nk_DE_2pair[0]}")
print(f"  Cell 1: {nk_DE_2pair[1]}")
print(f"  Total per mode: {nk_DE_2pair[0] + nk_DE_2pair[1]}")
print(f"  Sum: {np.sum(nk_DE_2pair):.6f} (should be {N_pair})")

# Ground state occupations for comparison
nk_GS_2pair = np.zeros((N_cells, N_modes))
psi_GS = evecs_fold_full[:, 0]
for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op(k, c)
        nk_GS_2pair[c, k] = psi_GS @ n_k @ psi_GS

print(f"\nGS pair occupations (N_pair = 2):")
print(f"  Cell 0: {nk_GS_2pair[0]}")
print(f"  Cell 1: {nk_GS_2pair[1]}")

# Occupation mismatch
delta_n = nk_DE_2pair - nk_GS_2pair
delta_n_norm = np.linalg.norm(delta_n)
print(f"\n||delta_n|| = ||n_DE - n_GS|| = {delta_n_norm:.8f}")

# Compare with N_pair = 1 data from S56
nk_DE_1pair = d56['nk_DE'][:N_modes]   # Cell 0 occupations from S56
nk_GS_1pair = d56['nk_GS'][:N_modes]
delta_n_1pair = nk_DE_1pair - nk_GS_1pair
delta_n_1pair_norm = np.linalg.norm(delta_n_1pair)
print(f"\nN_pair = 1 comparison (from S56):")
print(f"  ||delta_n|| (N=1) = {delta_n_1pair_norm:.8f}")
print(f"  ||delta_n|| (N=2) = {delta_n_norm:.8f}")
print(f"  Ratio (N=2)/(N=1) = {delta_n_norm/delta_n_1pair_norm:.4f}")


# =====================================================================
#  8. ENTANGLEMENT ENTROPY (Inter-cell)
# =====================================================================

print("\n" + "=" * 70)
print("ENTANGLEMENT ENTROPY")
print("=" * 70)

# Compute entanglement entropy between cells for each eigenstate
# Reduced density matrix of cell 0 by tracing over cell 1

# Organize states by cell-0 content
# State |s1, s2> has a certain occupation of cell 0 and cell 1
# For N_pair = 2: cell-0 can have 0, 1, or 2 pairs
# n0 = 0: both pairs in cell 1 -> C(8,2) = 28 states
# n0 = 1: one pair in cell 0, one in cell 1 -> 8*8 = 64 states
# n0 = 2: both pairs in cell 0 -> C(8,2) = 28 states

def get_cell_content(state_idx):
    """Return (modes_in_cell0, modes_in_cell1) for a basis state."""
    (m1, c1), (m2, c2) = state_info[state_idx]
    cell0_modes = []
    cell1_modes = []
    if c1 == 0: cell0_modes.append(m1)
    else: cell1_modes.append(m1)
    if c2 == 0: cell0_modes.append(m2)
    else: cell1_modes.append(m2)
    return tuple(sorted(cell0_modes)), tuple(sorted(cell1_modes))

# Build the bipartite structure
# Cell-0 basis: {}, {k}, {k,l} for k,l in 0..7
# Cell-1 basis: same
# |state> = Sum_{a,b} C_{a,b} |a>_0 |b>_1

# Enumerate cell-0 sub-basis states
cell0_states = set()
cell1_states = set()
for i in range(dim):
    c0, c1 = get_cell_content(i)
    cell0_states.add(c0)
    cell1_states.add(c1)

cell0_list = sorted(cell0_states)
cell1_list = sorted(cell1_states)
cell0_idx = {s: i for i, s in enumerate(cell0_list)}
cell1_idx = {s: i for i, s in enumerate(cell1_list)}

d0 = len(cell0_list)
d1 = len(cell1_list)
print(f"Cell-0 sub-basis: {d0} states")
print(f"Cell-1 sub-basis: {d1} states")

def entanglement_entropy(psi):
    """Compute von Neumann entanglement entropy between cells."""
    # Build coefficient matrix C[a,b] where |psi> = Sum C[a,b] |a>_0 |b>_1
    C = np.zeros((d0, d1))
    for i in range(dim):
        c0, c1 = get_cell_content(i)
        a = cell0_idx[c0]
        b = cell1_idx[c1]
        C[a, b] += psi[i]

    # SVD to get Schmidt coefficients
    _, sigma, _ = np.linalg.svd(C, full_matrices=False)
    sigma2 = sigma**2
    sigma2 = sigma2[sigma2 > 1e-30]
    S_ent = -np.sum(sigma2 * np.log(sigma2))  # (local)
    return S_ent

# Entanglement entropy of ground state
S_ent_GS = entanglement_entropy(evecs_fold_full[:, 0])
print(f"\nEntanglement entropy (GS, fold): {S_ent_GS:.6f}")
print(f"Max possible (log min(d0,d1) = log {min(d0,d1)}): {np.log(min(d0, d1)):.6f}")

# Entanglement entropy of diagonal ensemble (time-averaged)
S_ent_DE = np.sum([p_n[n] * entanglement_entropy(evecs_fold_full[:, n]) for n in range(dim)])
print(f"Entanglement entropy (DE average): {S_ent_DE:.6f}")

# Entanglement entropy of the quenched state |psi(0)>
S_ent_quench = entanglement_entropy(psi0)
print(f"Entanglement entropy (initial |GS(tau=0)>): {S_ent_quench:.6f}")


# =====================================================================
#  9. THERMALIZATION TIMESCALE (if integrability breaks)
# =====================================================================

print("\n" + "=" * 70)
print("THERMALIZATION TIMESCALE ESTIMATE")
print("=" * 70)

# If <r> indicates broken integrability, estimate thermalization time
# from the spectral fluctuations. The Thouless time (inverse level spacing)
# sets the timescale for eigenstate thermalization.

# Mean level spacing (in the relevant Z_2 sector)
delta_E_even = np.mean(np.diff(evals_even))
delta_E_odd  = np.mean(np.diff(evals_odd))
delta_E_full = np.mean(np.diff(evals_fold_full))

print(f"Mean level spacing:")
print(f"  Full spectrum: {delta_E_full:.6f} M_KK")
print(f"  Even sector: {delta_E_even:.6f} M_KK")
print(f"  Odd sector:  {delta_E_odd:.6f} M_KK")

# Thouless time: t_Th ~ hbar / delta_E
# In M_KK units: t_Th ~ 1/delta_E (M_KK^{-1})
t_Th_full = 1.0 / delta_E_full if delta_E_full > 0 else np.inf
t_Th_even = 1.0 / delta_E_even if delta_E_even > 0 else np.inf

# Convert to physical units
# M_KK = 7.43e16 GeV, so t = 1/M_KK ~ hbar_GeV_s / M_KK
t_MKK_inv_seconds = hbar_GeV_s / M_KK  # time unit in seconds
t_Th_seconds = t_Th_full * t_MKK_inv_seconds
t_Th_Planck = t_Th_seconds / t_Planck

print(f"\nThouless time (hbar/delta_E):")
print(f"  t_Th = {t_Th_full:.2f} M_KK^{{-1}}")
print(f"  t_Th = {t_Th_seconds:.4e} s")
print(f"  t_Th = {t_Th_Planck:.4e} t_Pl")
print(f"  t_universe / t_Th = {t_universe_s / t_Th_seconds:.4e}")

# Heisenberg time: t_H ~ 2*pi*hbar / (mean spacing in spectrum used by initial state)
# More relevant: the overlap-weighted effective level spacing
delta_E_eff = 1.0 / np.sum(p_n**2) * delta_E_full  # effective spacing from IPR
t_H = 2 * np.pi / delta_E_eff if delta_E_eff > 0 else np.inf
t_H_seconds = t_H * t_MKK_inv_seconds
t_H_Planck = t_H_seconds / t_Planck

print(f"\nHeisenberg time (from diagonal ensemble IPR):")
print(f"  t_H = {t_H:.2f} M_KK^{{-1}}")
print(f"  t_H = {t_H_seconds:.4e} s")
print(f"  t_H = {t_H_Planck:.4e} t_Pl")

# Compare t_Th with CC relaxation requirement
# Need t_therm < t_universe to solve CC
print(f"\n--- CC Relaxation Requirement ---")
if t_Th_seconds < t_universe_s:
    print(f"t_Th < t_universe: thermalization fast enough (ratio = {t_Th_seconds/t_universe_s:.2e})")
else:
    print(f"t_Th > t_universe: thermalization too slow (ratio = {t_Th_seconds/t_universe_s:.2e})")
print(f"Mack criterion (t_therm < 10^60 t_Pl): {'PASS' if t_Th_Planck < 1e60 else 'FAIL'}")


# =====================================================================
#  10. GATE VERDICT
# =====================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: NPAIR2-INTEG-58")
print("=" * 70)

# The definitive <r> is the SECTOR-RESOLVED combined value
# (unsectorized <r> is contaminated by cross-sector level crossings)
r_definitive = r_combined
r_definitive_raw = (len(r_dist_even) * r_even_raw + len(r_dist_odd) * r_odd_raw) / (len(r_dist_even) + len(r_dist_odd))

print(f"\nDefinitive <r> (Z_2-resolved, unfolded): {r_definitive:.6f}")
print(f"Definitive <r> (Z_2-resolved, raw):      {r_definitive_raw:.6f}")
print(f"Unsectorized <r> (unfolded):              {r_fold_full:.6f}")
print(f"Control <r> (E_J = 0, Z_2-resolved):      {r_combined_noJ:.6f}")
print(f"\nPoisson:   0.386")
print(f"GOE:       0.530")
print(f"Threshold: 0.450")

if r_definitive > 0.45:
    verdict = "PASS"
    detail = f"<r> = {r_definitive:.4f} > 0.45 — integrability broken at N_pair = 2"
elif r_definitive < 0.40:
    verdict = "FAIL"
    detail = f"<r> = {r_definitive:.4f} < 0.40 — integrability persists at N_pair = 2"
else:
    verdict = "INFO"
    detail = f"<r> = {r_definitive:.4f} in [0.40, 0.45] — intermediate, N_pair = 3 needed"

print(f"\n>>> VERDICT: {verdict}")
print(f">>> {detail}")

# Count surviving integrals
# An integral is "surviving" if ||[H, R_k]|| / ||H|| < threshold
H_norm = np.linalg.norm(H_fold_full, 'fro')
threshold_integ = 0.01  # 1% of H norm  # (local)
n_surviving = 0
n_surviving_noJ = 0
for c in range(N_cells):
    for k in range(N_modes):
        if comm_norms_full[c, k] / H_norm < threshold_integ:
            n_surviving += 1
        if comm_norms_noJ[c, k] / H_norm < threshold_integ:
            n_surviving_noJ += 1

print(f"\nSurviving approximate integrals (||[H,n_k]||/||H|| < {threshold_integ}):")
print(f"  Full J: {n_surviving} / {N_cells * N_modes}")
print(f"  No J:   {n_surviving_noJ} / {N_cells * N_modes}")


# =====================================================================
#  11. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's58_npair2_integ.npz')
np.savez(save_path,
    # Metadata
    N_pair=N_pair,
    N_modes=N_modes,
    N_cells=N_cells,
    dim=dim,
    tau_fold=tau_fold_actual,
    E_J_fold=E_J_fold,
    E_J_tau0=E_J_tau0,

    # Spectra
    evals_fold_full=evals_fold_full,
    evals_fold_noJ=evals_fold_noJ,
    evals_tau0_full=evals_tau0_full,
    evals_even=evals_even,
    evals_odd=evals_odd,

    # Level statistics
    r_fold_full=r_fold_full,
    r_fold_noJ=r_fold_noJ,
    r_even=r_even,
    r_odd=r_odd,
    r_combined=r_combined,
    r_combined_noJ=r_combined_noJ,
    r_dist_fold_full=r_dist_fold_full,
    r_dist_even=r_dist_even,
    r_dist_odd=r_dist_odd,

    # Quench dynamics
    c_n_quench=c_n,
    p_n_quench=p_n,
    E_DE=E_DE,
    S_DE=S_DE,
    P_exc=P_exc,
    nk_DE_2pair=nk_DE_2pair,
    nk_GS_2pair=nk_GS_2pair,
    delta_n_norm=delta_n_norm,

    # Entanglement
    S_ent_GS=S_ent_GS,
    S_ent_DE=S_ent_DE,
    S_ent_quench=S_ent_quench,

    # Integrability
    comm_norms_full=comm_norms_full,
    comm_norms_noJ=comm_norms_noJ,
    n_surviving_integrals=n_surviving,

    # Timescales
    t_Th_MKK_inv=t_Th_full,
    t_Th_seconds=t_Th_seconds,
    t_Th_Planck=t_Th_Planck,

    # Participation ratios
    PR_fold=PR_fold,
    PR_noJ=PR_noJ,

    # Gate
    gate_name=np.array(['NPAIR2-INTEG-58']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"\nData saved to {save_path}")


# =====================================================================
#  12. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'S58 W1-1: N_pair = 2 Exact Diagonalization — NPAIR2-INTEG-58: {verdict}',
             fontsize=14, fontweight='bold')

# (a) Spectrum comparison
ax = axes[0, 0]
ax.plot(evals_fold_full, 'b-', alpha=0.7, label=f'Full E_J = {E_J_fold:.2f}')
ax.plot(evals_fold_noJ, 'r--', alpha=0.7, label='E_J = 0')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('Energy Spectrum (fold, N_pair = 2)')
ax.legend()

# (b) Level spacing ratio distribution
ax = axes[0, 1]
bins = np.linspace(0, 1, 25)
if len(r_dist_even) > 0:
    ax.hist(r_dist_even, bins=bins, alpha=0.5, color='blue', label=f'Even (<r>={r_even:.3f})', density=True)
if len(r_dist_odd) > 0:
    ax.hist(r_dist_odd, bins=bins, alpha=0.5, color='red', label=f'Odd (<r>={r_odd:.3f})', density=True)
ax.axvline(0.386, color='green', ls='--', lw=2, label='Poisson (0.386)')
ax.axvline(0.530, color='orange', ls='--', lw=2, label='GOE (0.530)')
ax.axvline(0.45, color='black', ls=':', lw=2, label='Gate threshold')
ax.axvline(r_combined, color='purple', ls='-', lw=2, label=f'Measured ({r_combined:.3f})')
ax.set_xlabel('Gap ratio r')
ax.set_ylabel('Density')
ax.set_title('Level Spacing Ratio (Z_2-resolved)')
ax.legend(fontsize=8)

# (c) Participation ratios
ax = axes[0, 2]
ax.semilogy(PR_fold / dim, 'b.', alpha=0.5, label='Full E_J')
ax.semilogy(PR_noJ / dim, 'r.', alpha=0.3, label='E_J = 0')
ax.axhline(1.0 / dim, color='gray', ls=':', label=f'Localized (1/{dim})')
ax.axhline(1.0, color='gray', ls='--', label='Ergodic')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('PR / dim')
ax.set_title('Participation Ratio')
ax.legend(fontsize=8)

# (d) Quench overlap distribution
ax = axes[1, 0]
ax.semilogy(evals_fold_full, p_n, 'b.', markersize=3)
ax.set_xlabel('Energy (M_KK)')
ax.set_ylabel('|c_n|^2')
ax.set_title(f'Quench Overlaps (P_exc = {P_exc:.6f})')

# (e) GGE occupations vs GS
ax = axes[1, 1]
modes = np.arange(N_modes)
width = 0.2  # (local)
ax.bar(modes - 0.3, nk_DE_2pair[0], width, color='blue', alpha=0.7, label='DE cell 0')
ax.bar(modes - 0.1, nk_DE_2pair[1], width, color='cyan', alpha=0.7, label='DE cell 1')
ax.bar(modes + 0.1, nk_GS_2pair[0], width, color='red', alpha=0.7, label='GS cell 0')
ax.bar(modes + 0.3, nk_GS_2pair[1], width, color='orange', alpha=0.7, label='GS cell 1')
ax.set_xlabel('Mode index')
ax.set_ylabel('Pair occupation')
ax.set_title(f'GGE vs GS occupations (||delta_n|| = {delta_n_norm:.4f})')
ax.legend(fontsize=7)

# (f) Commutator norms
ax = axes[1, 2]
ax.bar(np.arange(N_modes) - 0.15, comm_norms_full[0] / H_norm, 0.3, color='blue', alpha=0.7, label='Cell 0 (full J)')
ax.bar(np.arange(N_modes) + 0.15, comm_norms_full[1] / H_norm, 0.3, color='red', alpha=0.7, label='Cell 1 (full J)')
ax.axhline(threshold_integ, color='black', ls=':', label=f'Threshold ({threshold_integ})')
ax.set_xlabel('Mode index k')
ax.set_ylabel('||[H, n_k]|| / ||H||')
ax.set_title(f'Commutator Norms ({n_surviving}/{N_cells*N_modes} surviving)')
ax.legend(fontsize=8)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's58_npair2_integ.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plot_path}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
