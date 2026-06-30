#!/usr/bin/env python3
"""
s59_npair3_integ.py — N_pair = 3 Exact Diagonalization on 2-Cell System
=========================================================================

Gate: NPAIR3-INTEG-59
  PASS: <r>_even > 0.50 (GOE regime -- integrability broken)
  FAIL: <r>_even < 0.42 (approximate integrability persists)
  INFO: <r>_even in [0.42, 0.50]

Physics: At N_pair = 2, S58 found <r>_even = 0.442, in the intermediate regime.
The V_fold pairing matrix is only 37% rank-1 (Richardson-Gaudin integrability
requires exact rank-1 separability). At N_pair = 3, the 560-dimensional Hilbert
space provides stronger statistics, and the non-separable fraction of V_fold
has more channels through which to break integrability.

Volovik predicts crossover at N_pair ~ N_modes/2 = 4, so N_pair = 3 should
give <r>_even ~ 0.46-0.48. If <r>_even > 0.50, integrability is broken and
both the CC path (GGE thermalization -> Lambda -> 0) and the f_DM
redistribution path open.

Method:
  1. Load 2-cell Hamiltonian data from S58/S56
  2. Construct 3-pair Fock space: C(16,3) = 560 states
  3. Build H = H_BCS(cell_0) + H_BCS(cell_1) + H_Josephson
  4. Exact diagonalize the 560x560 Hamiltonian
  5. Resolve by Z_2 cell-exchange symmetry; compute <r> per sector
  6. Occupation number analysis: ||delta_n|| scaling with N_pair
  7. V_fold separability analysis in the 3-pair sector

Session: S59 W0-2
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
from canonical_constants import *

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S56 GGE fabric data (2-cell system at fold) — primary source
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold
eps_tau0 = d56['eps_tau0']       # 8 single-particle energies at tau=0
V_fold   = d56['V_fold']        # 8x8 pairing matrix
E_J_fold = float(d56['E_J_fold'])  # Josephson coupling at fold
E_J_tau0 = float(d56['E_J_tau0'])  # Josephson coupling at tau=0
tau_fold_actual = float(d56['tau_fold_actual'])

# S58 data for N_pair=2 cross-reference
d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
r_even_np2   = float(d58['r_even'])
r_odd_np2    = float(d58['r_odd'])
r_combined_np2 = float(d58['r_combined'])
delta_n_np2  = float(d58['delta_n_norm'])
nk_DE_np2    = d58['nk_DE_2pair']
nk_GS_np2    = d58['nk_GS_2pair']

# N_pair=1 data from S56 for scaling analysis
nk_DE_np1 = d56['nk_DE']        # 16-element array
nk_GS_np1 = d56['nk_GS']        # 16-element array
delta_n_np1 = np.linalg.norm(nk_DE_np1 - nk_GS_np1)

N_modes = 8  # modes per cell (local)
N_cells = 2   # cells
N_pair  = 3  # Cooper pairs (local)

print("=" * 70)
print("S59 W0-2: N_pair = 3 Exact Diagonalization — NPAIR3-INTEG-59")
print("=" * 70)
print(f"tau_fold = {tau_fold_actual:.6f}")
print(f"E_J_fold = {E_J_fold:.4f} M_KK")
print(f"E_J_tau0 = {E_J_tau0:.4f} M_KK")
print(f"N_modes/cell = {N_modes}, N_cells = {N_cells}, N_pair = {N_pair}")
print(f"eps_fold = {eps_fold}")


# =====================================================================
#  2. CONSTRUCT PAIR FOCK SPACE
# =====================================================================
# Pair-slot i in [0..7] = mode i in cell 0
# Pair-slot i in [8..15] = mode (i-8) in cell 1
# A state with N_pair = 3 is specified by choosing 3 of these 16 slots.

N_slots = N_modes * N_cells  # 16
pair_states = list(combinations(range(N_slots), N_pair))
dim = len(pair_states)
print(f"\nFock space: C({N_slots},{N_pair}) = {dim} three-pair states")
assert dim == 560, f"Expected 560, got {dim}"

# Map pair-slot to (mode, cell)
def slot_to_mode_cell(s):
    """Convert pair-slot index to (mode_index, cell_index)."""
    return (s % N_modes, s // N_modes)

# Pre-compute for each basis state: list of (mode, cell) for each pair
state_slots = pair_states  # tuple of 3 slot indices
state_info = []
for idx, slots in enumerate(pair_states):
    info = [slot_to_mode_cell(s) for s in slots]
    state_info.append(info)

# Index lookup: pair_states tuple -> index
state_index = {s: i for i, s in enumerate(pair_states)}


# =====================================================================
#  3. CONSTRUCT HAMILTONIAN
# =====================================================================

def build_H_BCS_2cell_3pair(eps, V, E_J):
    """
    Build the full BCS + Josephson Hamiltonian for N_pair=3 on a 2-cell system.

    H = H_kinetic + H_pairing + H_Josephson

    H_kinetic: Sum over occupied pair-slots of 2*eps[mode]
               (factor 2: each pair occupies both spin-up and spin-down)

    H_pairing: For each cell independently:
               -V[k,l] * (pair_k^dag pair_l) scatters pair from mode l to mode k
               within the SAME cell. Operates on one pair at a time.

    H_Josephson: -(E_J/2) * (B_0^dag B_1 + h.c.)
                 where B_c = Sum_k b_{k,c} is the collective pair operator.
                 Tunnels a pair from ANY mode in one cell to ANY mode in the other.

    For N_pair=3, each state has 3 occupied slots. The pairing and Josephson
    operators act on one pair at a time; Pauli exclusion prevents scattering
    into an already-occupied slot.
    """
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, slots_i in enumerate(pair_states):
        slots_set = set(slots_i)
        infos = state_info[i]

        # --- Diagonal: kinetic energy ---
        for (mk, ck) in infos:
            H[i, i] += 2.0 * eps[mk]

        # --- Pairing interaction (within each cell) ---
        # For each occupied pair p at (m_p, c_p): scatter m_p -> k in cell c_p
        # provided slot (k, c_p) is not occupied by another pair.
        for p_idx in range(N_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * N_modes + m_p

            for k in range(N_modes):
                new_slot = c_p * N_modes + k
                if k == m_p:
                    # Diagonal pairing
                    H[i, i] -= V[m_p, m_p]
                    continue
                if new_slot in slots_set:
                    continue  # Pauli blocked
                # Build new state: replace old_slot with new_slot
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] -= V[k, m_p]

        # --- Josephson tunneling ---
        # -(E_J/2) tunnels one pair from (m_p, c_p) -> (l, 1-c_p) for any l
        for p_idx in range(N_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * N_modes + m_p
            target_cell = 1 - c_p

            for l in range(N_modes):
                new_slot = target_cell * N_modes + l
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] += -E_J / 2.0

    # Symmetrize (should be Hermitian by construction, enforce numerically)
    H = 0.5 * (H + H.T)

    return H


# =====================================================================
#  4. BUILD AND DIAGONALIZE
# =====================================================================

print("\n--- Building Hamiltonians ---")

H_fold_full = build_H_BCS_2cell_3pair(eps_fold, V_fold, E_J_fold)
herm_check = np.max(np.abs(H_fold_full - H_fold_full.T))
print(f"H_fold_full: {H_fold_full.shape}, Hermiticity check = {herm_check:.2e}")

H_fold_noJ = build_H_BCS_2cell_3pair(eps_fold, V_fold, 0.0)
print(f"H_fold_noJ:  {H_fold_noJ.shape}, Hermiticity check = {np.max(np.abs(H_fold_noJ - H_fold_noJ.T)):.2e}")

H_tau0_full = build_H_BCS_2cell_3pair(eps_tau0, V_fold, E_J_tau0)
print(f"H_tau0_full: {H_tau0_full.shape}, Hermiticity check = {np.max(np.abs(H_tau0_full - H_tau0_full.T)):.2e}")

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
    """
    E = np.sort(eigenvalues)

    if unfold:
        # Polynomial unfolding (degree 5)
        N = np.arange(1, len(E) + 1)
        poly = np.polyfit(E, N, deg=min(5, len(E) - 1))
        N_smooth = np.polyval(poly, E)
        E_unf = N_smooth
    else:
        E_unf = E

    s = np.diff(E_unf)
    s = s[s > 1e-12]  # remove degeneracies

    if len(s) < 3:
        return 0.0, np.array([])

    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])

    return np.mean(r_n), r_n


print("\n" + "=" * 70)
print("LEVEL SPACING STATISTICS — FULL SPECTRUM")
print("=" * 70)

r_fold_full, r_dist_fold_full = level_spacing_ratio(evals_fold_full)
r_fold_noJ, r_dist_fold_noJ = level_spacing_ratio(evals_fold_noJ)
r_fold_full_raw, _ = level_spacing_ratio(evals_fold_full, unfold=False)
r_fold_noJ_raw, _  = level_spacing_ratio(evals_fold_noJ, unfold=False)

print(f"<r> (fold, full E_J, unfolded):  {r_fold_full:.6f}")
print(f"<r> (fold, E_J = 0, unfolded):   {r_fold_noJ:.6f}")
print(f"<r> (fold, full E_J, raw):       {r_fold_full_raw:.6f}")
print(f"<r> (fold, E_J = 0, raw):        {r_fold_noJ_raw:.6f}")
print(f"Poisson: 0.386, GOE: 0.530")


# =====================================================================
#  5b. SYMMETRY-RESOLVED LEVEL STATISTICS (Z_2 cell exchange)
# =====================================================================

print("\n" + "-" * 70)
print("SYMMETRY-RESOLVED ANALYSIS (Z_2 cell exchange)")
print("-" * 70)

# Build the Z_2 exchange operator: P swaps cell 0 <-> cell 1
def swap_slot(s):
    """Swap cell index of a pair-slot."""
    mode = s % N_modes
    cell = s // N_modes
    return (1 - cell) * N_modes + mode

P_mat = np.zeros((dim, dim), dtype=np.float64)
for i, slots in enumerate(pair_states):
    new_slots = tuple(sorted([swap_slot(s) for s in slots]))
    j = state_index[new_slots]
    P_mat[j, i] = 1.0

# Verify P^2 = I
P2_check = np.max(np.abs(P_mat @ P_mat - np.eye(dim)))
print(f"P^2 = I check: max|P^2 - I| = {P2_check:.2e}")

# Verify [H, P] = 0
commHP = H_fold_full @ P_mat - P_mat @ H_fold_full
comm_norm = np.max(np.abs(commHP))
print(f"[H_fold, P] = 0 check: max|[H,P]| = {comm_norm:.2e}")

# Project onto Z_2 sectors
P_evals, P_evecs = eigh(P_mat)
even_mask = P_evals > 0.5
odd_mask  = P_evals < -0.5
n_even = np.sum(even_mask)
n_odd  = np.sum(odd_mask)
print(f"Z_2 sectors: even = {n_even}, odd = {n_odd}, total = {n_even + n_odd}")

# Diagonalize H in each Z_2 sector
Q_even = P_evecs[:, even_mask]
H_even = Q_even.T @ H_fold_full @ Q_even
evals_even, evecs_even_proj = eigh(H_even)

Q_odd = P_evecs[:, odd_mask]
H_odd = Q_odd.T @ H_fold_full @ Q_odd
evals_odd, evecs_odd_proj = eigh(H_odd)

# <r> in each sector
r_even, r_dist_even = level_spacing_ratio(evals_even)
r_odd, r_dist_odd   = level_spacing_ratio(evals_odd)
r_even_raw, _ = level_spacing_ratio(evals_even, unfold=False)
r_odd_raw, _  = level_spacing_ratio(evals_odd, unfold=False)

print(f"\n<r> (even sector, {n_even} levels): {r_even:.6f} (raw: {r_even_raw:.6f})")
print(f"<r> (odd sector, {n_odd} levels):  {r_odd:.6f} (raw: {r_odd_raw:.6f})")

# Combined sector-resolved <r>
n_gaps_even = len(r_dist_even)
n_gaps_odd  = len(r_dist_odd)
r_combined = (n_gaps_even * r_even + n_gaps_odd * r_odd) / max(1, n_gaps_even + n_gaps_odd)
print(f"<r> (sector-resolved combined): {r_combined:.6f}")

r_stderr_even = np.std(r_dist_even) / np.sqrt(n_gaps_even) if n_gaps_even > 0 else 0
r_stderr_odd  = np.std(r_dist_odd) / np.sqrt(n_gaps_odd) if n_gaps_odd > 0 else 0
r_stderr_combined = np.sqrt((n_gaps_even * r_stderr_even)**2 + (n_gaps_odd * r_stderr_odd)**2) / max(1, n_gaps_even + n_gaps_odd)

print(f"  even: <r> = {r_even:.4f} +/- {r_stderr_even:.4f} (N_gaps = {n_gaps_even})")
print(f"  odd:  <r> = {r_odd:.4f} +/- {r_stderr_odd:.4f} (N_gaps = {n_gaps_odd})")
print(f"  combined: <r> = {r_combined:.4f} +/- {r_stderr_combined:.4f}")

# Control: no-J
H_even_noJ = Q_even.T @ H_fold_noJ @ Q_even
H_odd_noJ  = Q_odd.T @ H_fold_noJ @ Q_odd
evals_even_noJ, _ = eigh(H_even_noJ)
evals_odd_noJ, _  = eigh(H_odd_noJ)
r_even_noJ, r_dist_even_noJ = level_spacing_ratio(evals_even_noJ)
r_odd_noJ, r_dist_odd_noJ   = level_spacing_ratio(evals_odd_noJ)
n_gaps_even_noJ = len(r_dist_even_noJ)
n_gaps_odd_noJ = len(r_dist_odd_noJ)
r_combined_noJ = (n_gaps_even_noJ * r_even_noJ + n_gaps_odd_noJ * r_odd_noJ) / max(1, n_gaps_even_noJ + n_gaps_odd_noJ)
print(f"\nControl (E_J = 0):")
print(f"  <r> even: {r_even_noJ:.6f}, odd: {r_odd_noJ:.6f}, combined: {r_combined_noJ:.6f}")


# =====================================================================
#  5c. ADDITIONAL UNFOLDING CROSS-CHECK: Cubic + Quartic
# =====================================================================

print("\n--- Unfolding robustness check ---")

def level_spacing_ratio_poly(eigenvalues, deg=5):
    """<r> with polynomial unfolding of given degree."""
    E = np.sort(eigenvalues)
    N = np.arange(1, len(E) + 1)
    poly = np.polyfit(E, N, deg=min(deg, len(E) - 1))
    E_unf = np.polyval(poly, E)
    s = np.diff(E_unf)
    s = s[s > 1e-12]
    if len(s) < 3:
        return 0.0
    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return np.mean(r_n)

for deg in [3, 5, 7, 9]:
    r_e = level_spacing_ratio_poly(evals_even, deg)
    r_o = level_spacing_ratio_poly(evals_odd, deg)
    wt = n_gaps_even * r_e + n_gaps_odd * r_o
    r_c = wt / max(1, n_gaps_even + n_gaps_odd)
    print(f"  poly deg {deg}: <r>_even = {r_e:.4f}, <r>_odd = {r_o:.4f}, combined = {r_c:.4f}")


# =====================================================================
#  6. QUENCH DYNAMICS AND GGE OCCUPATION NUMBERS
# =====================================================================

print("\n" + "=" * 70)
print("QUENCH DYNAMICS: tau=0 -> tau_fold")
print("=" * 70)

# Ground state of H(tau=0)
psi0 = evecs_tau0_full[:, 0]
print(f"Initial state: GS of H(tau=0), E = {evals_tau0_full[0]:.6f}")

# Overlap with fold eigenstates
c_n = evecs_fold_full.T @ psi0
p_n = c_n**2
print(f"Sum |c_n|^2 = {np.sum(p_n):.10f} (should be 1)")

# Diagonal ensemble energy
E_DE = np.sum(p_n * evals_fold_full)
P_exc = 1.0 - p_n[0]
p_nz = p_n[p_n > 1e-30]
S_DE = -np.sum(p_nz * np.log(p_nz))
print(f"Diagonal ensemble energy: {E_DE:.6f}")
print(f"Ground state energy (fold): {evals_fold_full[0]:.6f}")
print(f"Excitation energy: {E_DE - evals_fold_full[0]:.6f}")
print(f"P_exc = {P_exc:.8f}")
print(f"S_DE = {S_DE:.6f}, S_max = {np.log(dim):.6f}, S_DE/S_max = {S_DE/np.log(dim):.6f}")

# Build pair number operators for N_pair = 3
def build_pair_number_op_3(mode, cell):
    """Build n_{mode,cell} operator in 3-pair Fock basis."""
    n_op = np.zeros((dim, dim))
    slot = cell * N_modes + mode
    for i, slots in enumerate(pair_states):
        if slot in slots:
            n_op[i, i] = 1.0
    return n_op

# GGE occupation numbers
nk_DE_3pair = np.zeros((N_cells, N_modes))
nk_GS_3pair = np.zeros((N_cells, N_modes))
psi_GS = evecs_fold_full[:, 0]

for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op_3(k, c)
        # <n_k>_DE = Sum_n p_n <n|n_k|n>
        nk_DE_3pair[c, k] = np.sum(p_n * np.diag(evecs_fold_full.T @ n_k @ evecs_fold_full))
        nk_GS_3pair[c, k] = psi_GS @ n_k @ psi_GS

print(f"\nGGE pair occupations (N_pair = 3):")
print(f"  Cell 0: {nk_DE_3pair[0]}")
print(f"  Cell 1: {nk_DE_3pair[1]}")
print(f"  Sum: {np.sum(nk_DE_3pair):.6f} (should be {N_pair})")

print(f"\nGS pair occupations (N_pair = 3):")
print(f"  Cell 0: {nk_GS_3pair[0]}")
print(f"  Cell 1: {nk_GS_3pair[1]}")

delta_n_3pair = nk_DE_3pair - nk_GS_3pair
delta_n_np3 = np.linalg.norm(delta_n_3pair)
print(f"\n||delta_n|| = {delta_n_np3:.8f}")


# =====================================================================
#  6b. OCCUPATION NUMBER SCALING ANALYSIS
# =====================================================================

print("\n" + "-" * 70)
print("OCCUPATION NUMBER SCALING: ||delta_n|| vs N_pair")
print("-" * 70)

# N_pair = 1 data (from S56, 16-element array reshaped to 2x8)
nk_DE_np1_2x8 = nk_DE_np1.reshape(2, 8)
nk_GS_np1_2x8 = nk_GS_np1.reshape(2, 8)
delta_n_np1_2x8 = np.linalg.norm(nk_DE_np1_2x8 - nk_GS_np1_2x8)

# N_pair = 2 data (from S58)
# Already loaded as delta_n_np2

print(f"||delta_n|| at N_pair = 1: {delta_n_np1_2x8:.8f}")
print(f"||delta_n|| at N_pair = 2: {delta_n_np2:.8f}")
print(f"||delta_n|| at N_pair = 3: {delta_n_np3:.8f}")

# Check if sqrt(N_pair) scaling (independent pairs) holds
if delta_n_np1_2x8 > 0:
    ratio_21 = delta_n_np2 / delta_n_np1_2x8
    ratio_31 = delta_n_np3 / delta_n_np1_2x8
    print(f"\nScaling ratios (relative to N=1):")
    print(f"  ||delta_n(2)|| / ||delta_n(1)|| = {ratio_21:.4f} (sqrt(2) = {np.sqrt(2):.4f} for indep)")
    print(f"  ||delta_n(3)|| / ||delta_n(1)|| = {ratio_31:.4f} (sqrt(3) = {np.sqrt(3):.4f} for indep)")
    # Power law fit
    if delta_n_np2 > 0 and delta_n_np3 > 0:
        ns = np.array([1, 2, 3], dtype=float)
        dns = np.array([delta_n_np1_2x8, delta_n_np2, delta_n_np3])
        # Fit log(dn) = alpha * log(N) + const
        mask = dns > 0
        if np.sum(mask) >= 2:
            coeffs = np.polyfit(np.log(ns[mask]), np.log(dns[mask]), 1)
            alpha = coeffs[0]
            print(f"  Power law exponent: alpha = {alpha:.4f} (0.5 = indep, >0.5 = interacting)")
            if alpha > 0.7:
                print(f"  --> SUPERLINEAR: pairs interact, breaking independent-pair assumption")
            elif alpha < 0.3:
                print(f"  --> SUBLINEAR: pairing weakens with N (unlikely)")
            else:
                print(f"  --> CONSISTENT with sqrt(N) scaling (independent pairs)")


# =====================================================================
#  7. V_FOLD SEPARABILITY ANALYSIS IN 3-PAIR SECTOR
# =====================================================================

print("\n" + "=" * 70)
print("V_FOLD SEPARABILITY ANALYSIS")
print("=" * 70)

# SVD of V_fold
U_V, S_V, Vt_V = np.linalg.svd(V_fold)
rank1_frac = S_V[0] / np.sum(S_V)
rank2_frac = (S_V[0] + S_V[1]) / np.sum(S_V)
print(f"V_fold SVD singular values: {S_V}")
print(f"Rank-1 fraction: {rank1_frac:.4f} (37% — Richardson-Gaudin requires ~1.0)")
print(f"Rank-2 fraction: {rank2_frac:.4f}")

# Project pairing interaction into the 3-pair sector and measure effective
# separability. The pairing part of H is H_pair = -Sum_{cell} Sum_{k,l} V_{kl} b_k^dag b_l.
# Build H_pair alone in the 3-pair Fock space.
H_pair_only = np.zeros((dim, dim), dtype=np.float64)
for i, slots_i in enumerate(pair_states):
    slots_set = set(slots_i)
    infos = state_info[i]

    for p_idx in range(N_pair):
        m_p, c_p = infos[p_idx]
        old_slot = c_p * N_modes + m_p

        for k in range(N_modes):
            new_slot = c_p * N_modes + k
            if k == m_p:
                H_pair_only[i, i] -= V_fold[m_p, m_p]
                continue
            if new_slot in slots_set:
                continue
            new_slots = list(slots_i)
            new_slots[new_slots.index(old_slot)] = new_slot
            new_state = tuple(sorted(new_slots))
            if new_state in state_index:
                j = state_index[new_state]
                H_pair_only[j, i] -= V_fold[k, m_p]

H_pair_only = 0.5 * (H_pair_only + H_pair_only.T)

# Now build the rank-1 approximation of V
V_rank1 = S_V[0] * np.outer(U_V[:, 0], Vt_V[0, :])
V_rank1 = 0.5 * (V_rank1 + V_rank1.T)  # ensure symmetric

H_pair_rank1 = np.zeros((dim, dim), dtype=np.float64)
for i, slots_i in enumerate(pair_states):
    slots_set = set(slots_i)
    infos = state_info[i]

    for p_idx in range(N_pair):
        m_p, c_p = infos[p_idx]
        old_slot = c_p * N_modes + m_p

        for k in range(N_modes):
            new_slot = c_p * N_modes + k
            if k == m_p:
                H_pair_rank1[i, i] -= V_rank1[m_p, m_p]
                continue
            if new_slot in slots_set:
                continue
            new_slots = list(slots_i)
            new_slots[new_slots.index(old_slot)] = new_slot
            new_state = tuple(sorted(new_slots))
            if new_state in state_index:
                j = state_index[new_state]
                H_pair_rank1[j, i] -= V_rank1[k, m_p]

H_pair_rank1 = 0.5 * (H_pair_rank1 + H_pair_rank1.T)

# Separability fraction in the projected space
norm_full = np.linalg.norm(H_pair_only, 'fro')
norm_rank1 = np.linalg.norm(H_pair_rank1, 'fro')
norm_resid = np.linalg.norm(H_pair_only - H_pair_rank1, 'fro')
sep_frac_3pair = 1.0 - (norm_resid / norm_full) if norm_full > 0 else 0

print(f"\nPairing Hamiltonian in 3-pair sector:")
print(f"  ||H_pair||     = {norm_full:.6f}")
print(f"  ||H_pair_rk1|| = {norm_rank1:.6f}")
print(f"  ||residual||   = {norm_resid:.6f}")
print(f"  Separability fraction: {sep_frac_3pair:.4f}")

# Compare with 2-pair sector (using S58 data or recomputing)
# For N_pair=2 (120 states), the separability was S_V[0]/sum(S_V) = 0.369
# The projected separability in the many-body space may differ.
# Report the comparison:
print(f"\nComparison:")
print(f"  V_fold rank-1 fraction (bare): {rank1_frac:.4f}")
print(f"  Projected separability (N=3):  {sep_frac_3pair:.4f}")


# =====================================================================
#  8. COMMUTATOR ANALYSIS (INTEGRABILITY CHECK)
# =====================================================================

print("\n" + "=" * 70)
print("COMMUTATOR ANALYSIS")
print("=" * 70)

H_norm = np.linalg.norm(H_fold_full, 'fro')
comm_norms_full = np.zeros((N_cells, N_modes))
comm_norms_noJ  = np.zeros((N_cells, N_modes))

for c in range(N_cells):
    for k in range(N_modes):
        n_k = build_pair_number_op_3(k, c)
        comm_full = H_fold_full @ n_k - n_k @ H_fold_full
        comm_noJ  = H_fold_noJ @ n_k  - n_k @ H_fold_noJ
        comm_norms_full[c, k] = np.linalg.norm(comm_full, 'fro')
        comm_norms_noJ[c, k]  = np.linalg.norm(comm_noJ, 'fro')

print(f"[H_full, n_k] / ||H|| (cell 0): {comm_norms_full[0] / H_norm}")
print(f"[H_full, n_k] / ||H|| (cell 1): {comm_norms_full[1] / H_norm}")
print(f"Max commutator / ||H||: {np.max(comm_norms_full / H_norm):.6f}")

print(f"\n[H_noJ, n_k] / ||H_noJ|| (cell 0): {comm_norms_noJ[0] / np.linalg.norm(H_fold_noJ, 'fro')}")

# Count surviving approximate integrals
threshold_integ = 0.01  # (local)
n_surviving = np.sum(comm_norms_full / H_norm < threshold_integ)
n_surviving_noJ = np.sum(comm_norms_noJ / np.linalg.norm(H_fold_noJ, 'fro') < threshold_integ)
print(f"\nSurviving integrals (||[H,n_k]||/||H|| < {threshold_integ}):")
print(f"  Full J: {n_surviving} / {N_cells * N_modes}")
print(f"  No J:   {n_surviving_noJ} / {N_cells * N_modes}")


# =====================================================================
#  9. PARTICIPATION RATIO ANALYSIS
# =====================================================================

print("\n" + "=" * 70)
print("EIGENSTATE STRUCTURE (PARTICIPATION RATIO)")
print("=" * 70)

PR_fold = np.zeros(dim)
for n in range(dim):
    psi = evecs_fold_full[:, n]
    ipr = np.sum(psi**4)
    PR_fold[n] = 1.0 / ipr if ipr > 0 else 0.0

PR_noJ = np.zeros(dim)
for n in range(dim):
    psi = evecs_fold_noJ[:, n]
    ipr = np.sum(psi**4)
    PR_noJ[n] = 1.0 / ipr if ipr > 0 else 0.0

print(f"Mean participation ratio (full J): {np.mean(PR_fold):.2f} / {dim}")
print(f"Mean participation ratio (no J):   {np.mean(PR_noJ):.2f} / {dim}")
print(f"PR ratio (full/noJ):               {np.mean(PR_fold)/np.mean(PR_noJ):.3f}")


# =====================================================================
#  10. ENTANGLEMENT ENTROPY (Inter-cell)
# =====================================================================

print("\n" + "=" * 70)
print("ENTANGLEMENT ENTROPY")
print("=" * 70)

# For N_pair = 3, cell-0 can have 0,1,2,3 pairs
# Organize bipartite structure

def get_cell_content_3(state_idx):
    """Return (modes_in_cell0, modes_in_cell1) for a 3-pair basis state."""
    infos = state_info[state_idx]
    cell0 = tuple(sorted([m for m, c in infos if c == 0]))
    cell1 = tuple(sorted([m for m, c in infos if c == 1]))
    return cell0, cell1

cell0_states = set()
cell1_states = set()
for i in range(dim):
    c0, c1 = get_cell_content_3(i)
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

def entanglement_entropy_3(psi):
    """Compute von Neumann entanglement entropy between cells for 3-pair state."""
    C = np.zeros((d0, d1))
    for i in range(dim):
        c0, c1 = get_cell_content_3(i)
        a = cell0_idx[c0]
        b = cell1_idx[c1]
        C[a, b] += psi[i]
    _, sigma, _ = np.linalg.svd(C, full_matrices=False)
    sigma2 = sigma**2
    sigma2 = sigma2[sigma2 > 1e-30]
    return -np.sum(sigma2 * np.log(sigma2))

S_ent_GS = entanglement_entropy_3(evecs_fold_full[:, 0])
S_ent_DE = np.sum([p_n[n] * entanglement_entropy_3(evecs_fold_full[:, n]) for n in range(dim)])
S_ent_quench = entanglement_entropy_3(psi0)

print(f"Entanglement entropy (GS, fold): {S_ent_GS:.6f}")
print(f"Entanglement entropy (DE average): {S_ent_DE:.6f}")
print(f"Entanglement entropy (initial |GS(tau=0)>): {S_ent_quench:.6f}")
print(f"Max possible (log min({d0},{d1})): {np.log(min(d0, d1)):.6f}")


# =====================================================================
#  11. GATE VERDICT
# =====================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: NPAIR3-INTEG-59")
print("=" * 70)

# The definitive <r> is <r>_even (even sector of Z_2)
r_definitive = r_even
r_def_err = r_stderr_even

print(f"\nDefinitive <r>_even (Z_2-resolved, unfolded): {r_definitive:.6f} +/- {r_def_err:.4f}")
print(f"<r>_odd (Z_2-resolved, unfolded):  {r_odd:.6f} +/- {r_stderr_odd:.4f}")
print(f"<r>_combined (sector-resolved):     {r_combined:.6f}")
print(f"Control <r> (E_J = 0, combined):    {r_combined_noJ:.6f}")
print(f"\nPoisson:   0.386")
print(f"GOE:       0.530")
print(f"Gate thresholds: PASS > 0.50, FAIL < 0.42, INFO in [0.42, 0.50]")

# Comparison with N_pair = 2
print(f"\nN_pair = 2 results (S58): <r>_even = {r_even_np2:.4f}, <r>_odd = {r_odd_np2:.4f}, combined = {r_combined_np2:.4f}")
print(f"N_pair = 3 results:       <r>_even = {r_even:.4f}, <r>_odd = {r_odd:.4f}, combined = {r_combined:.4f}")
print(f"Shift: Delta<r>_even = {r_even - r_even_np2:.4f}")

if r_definitive > 0.50:
    verdict = "PASS"
    detail = f"<r>_even = {r_definitive:.4f} > 0.50 — GOE regime, integrability broken at N_pair = 3"
elif r_definitive < 0.42:
    verdict = "FAIL"
    detail = f"<r>_even = {r_definitive:.4f} < 0.42 — approximate integrability persists at N_pair = 3"
else:
    verdict = "INFO"
    detail = f"<r>_even = {r_definitive:.4f} in [0.42, 0.50] — intermediate regime at N_pair = 3"

print(f"\n>>> VERDICT: {verdict}")
print(f">>> {detail}")


# =====================================================================
#  12. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's59_npair3_integ.npz')
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
    r_stderr_even=r_stderr_even,
    r_stderr_odd=r_stderr_odd,

    # N_pair = 2 reference
    r_even_np2=r_even_np2,
    r_odd_np2=r_odd_np2,
    r_combined_np2=r_combined_np2,

    # Quench dynamics
    c_n_quench=c_n,
    p_n_quench=p_n,
    E_DE=E_DE,
    S_DE=S_DE,
    P_exc=P_exc,
    nk_DE_3pair=nk_DE_3pair,
    nk_GS_3pair=nk_GS_3pair,
    delta_n_norm_np3=delta_n_np3,
    delta_n_norm_np2=delta_n_np2,
    delta_n_norm_np1=delta_n_np1_2x8,

    # Entanglement
    S_ent_GS=S_ent_GS,
    S_ent_DE=S_ent_DE,
    S_ent_quench=S_ent_quench,

    # Integrability
    comm_norms_full=comm_norms_full,
    comm_norms_noJ=comm_norms_noJ,
    n_surviving_integrals=n_surviving,

    # Participation ratios
    PR_fold=PR_fold,
    PR_noJ=PR_noJ,

    # V_fold separability
    V_svd_values=S_V,
    rank1_frac=rank1_frac,
    sep_frac_3pair=sep_frac_3pair,

    # Gate
    gate_name=np.array(['NPAIR3-INTEG-59']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"\nData saved to {save_path}")


# =====================================================================
#  13. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'S59 W0-2: N_pair = 3 Exact Diagonalization — NPAIR3-INTEG-59: {verdict}',
             fontsize=14, fontweight='bold')

# (a) Spectrum comparison
ax = axes[0, 0]
ax.plot(evals_fold_full, 'b-', alpha=0.7, label=f'Full E_J = {E_J_fold:.2f}')
ax.plot(evals_fold_noJ, 'r--', alpha=0.7, label='E_J = 0')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title(f'Energy Spectrum (fold, N_pair = 3, dim = {dim})')
ax.legend()

# (b) Level spacing ratio distribution — Z_2-resolved
ax = axes[0, 1]
bins = np.linspace(0, 1, 30)
if n_gaps_even > 0:
    ax.hist(r_dist_even, bins=bins, alpha=0.5, color='blue',
            label=f'Even (<r>={r_even:.3f})', density=True)
if n_gaps_odd > 0:
    ax.hist(r_dist_odd, bins=bins, alpha=0.5, color='red',
            label=f'Odd (<r>={r_odd:.3f})', density=True)
ax.axvline(0.386, color='green', ls='--', lw=2, label='Poisson (0.386)')
ax.axvline(0.530, color='orange', ls='--', lw=2, label='GOE (0.530)')
ax.axvline(0.50, color='black', ls=':', lw=2, label='Gate: PASS > 0.50')
ax.axvline(0.42, color='gray', ls=':', lw=2, label='Gate: FAIL < 0.42')
ax.axvline(r_even, color='purple', ls='-', lw=2, label=f'<r>_even ({r_even:.3f})')
ax.set_xlabel('Gap ratio r')
ax.set_ylabel('Density')
ax.set_title('Level Spacing Ratio (Z_2-resolved)')
ax.legend(fontsize=7)

# (c) <r> vs N_pair — the scaling plot
ax = axes[0, 2]
n_pairs = [2, 3]
r_evens = [r_even_np2, r_even]
r_odds  = [r_odd_np2, r_odd]
ax.plot(n_pairs, r_evens, 'bo-', markersize=10, linewidth=2, label='<r>_even')
ax.plot(n_pairs, r_odds, 'rs-', markersize=10, linewidth=2, label='<r>_odd')
ax.axhline(0.386, color='green', ls='--', lw=1.5, label='Poisson')
ax.axhline(0.530, color='orange', ls='--', lw=1.5, label='GOE')
ax.axhline(0.50, color='black', ls=':', lw=1.5, label='PASS threshold')
ax.axhline(0.42, color='gray', ls=':', lw=1.5, label='FAIL threshold')
ax.set_xlabel('N_pair')
ax.set_ylabel('<r>')
ax.set_title('<r> vs N_pair')
ax.set_xticks([1, 2, 3, 4])
ax.set_xlim(1.5, 3.5)
ax.set_ylim(0.30, 0.60)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (d) ||delta_n|| scaling
ax = axes[1, 0]
ns_plot = np.array([1, 2, 3])
dns_plot = np.array([delta_n_np1_2x8, delta_n_np2, delta_n_np3])
ax.semilogy(ns_plot, dns_plot, 'ko-', markersize=10, linewidth=2, label='Measured')
# sqrt(N) reference
if delta_n_np1_2x8 > 0:
    dns_sqrt = delta_n_np1_2x8 * np.sqrt(ns_plot)
    ax.semilogy(ns_plot, dns_sqrt, 'g--', linewidth=1.5, label=r'$\sqrt{N}$ scaling')
ax.set_xlabel('N_pair')
ax.set_ylabel('||delta_n||')
ax.set_title('Occupation Mismatch Scaling')
ax.legend()
ax.grid(True, alpha=0.3)

# (e) Participation ratios
ax = axes[1, 1]
ax.semilogy(PR_fold / dim, 'b.', alpha=0.4, markersize=3, label='Full E_J')
ax.semilogy(PR_noJ / dim, 'r.', alpha=0.2, markersize=3, label='E_J = 0')
ax.axhline(1.0 / dim, color='gray', ls=':', label=f'Localized (1/{dim})')
ax.axhline(1.0, color='gray', ls='--', label='Ergodic')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('PR / dim')
ax.set_title(f'Participation Ratio (N_pair = 3, dim = {dim})')
ax.legend(fontsize=8)

# (f) Quench overlap distribution
ax = axes[1, 2]
ax.semilogy(evals_fold_full, p_n, 'b.', markersize=2)
ax.set_xlabel('Energy (M_KK)')
ax.set_ylabel('|c_n|^2')
ax.set_title(f'Quench Overlaps (P_exc = {P_exc:.6f})')

plt.tight_layout()
plot_path = os.path.join(data_dir, 's59_npair3_integ.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plot_path}")

print("\n" + "=" * 70)
print("Script completed successfully")
print("=" * 70)
