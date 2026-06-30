#!/usr/bin/env python3
"""
s61_seniority_fabric.py — Seniority Purity of 2-Cell Josephson Eigenstates
==========================================================================

Gate: SENIORITY-FABRIC-61
  INFO (characterization): purity distribution reported.
  If purity > 0.5 at physical E_J: seniority survives (integrability consistent).
  If purity < 0.3: seniority destroyed (integrability breaking).

Physics:
  Seniority (v) counts the number of unpaired particles. In a pair-Fock space
  of Omega modes, the seniority operator is:
    v_hat = N - 2 S_+ S_-
  where S_+ = sum_k c_{k,up}^dag c_{k,down}^dag creates a Cooper pair.

  In the pair representation (pairs occupy modes), we work with the
  quasi-spin algebra. For Omega modes each with degeneracy 2j+1=2 (pair
  slots), the pair-creation operator for mode k is s_k^+ = c_{k,up}^dag c_{k,down}^dag.

  The total pair-creation operator is S_+ = sum_k s_k^+.
  The seniority-zero state for N pairs is (S_+)^N|0> / norm.

  For the 2-cell fabric system, we define:
    - Per-cell seniority: v_alpha for cell alpha = 0,1
    - Total seniority: v_total = v_0 + v_1
    - Fabric seniority: from the fabric pair operator S_+^fabric = S_+^(0) + S_+^(1)

  The key question: does Josephson coupling mix seniority sectors?

  For tractability: 2 modes per cell, N_pair = 0,1,2 in total.
  Fock space: each slot (mode, cell) occupied or not. 2 modes x 2 cells = 4 slots.
  dim(N=0) = 1, dim(N=1) = 4, dim(N=2) = 6. Total dim = 1+4+6 = 11.
  But we work sector-by-sector in fixed N.

  ALSO: full 8-mode per cell, 2-cell computation for N=1 (dim=16),
  to connect directly with NAZ-6 single-cell seniority purities.

Method:
  1. Build H in pair-Fock space for 2 modes/cell (and 8 modes/cell)
  2. Exact diagonalization per N-sector
  3. Seniority decomposition:
     a) Construct |v=0, N> = (S_+)^N |0> / norm  (fully paired condensate)
     b) Remaining orthogonal states carry v > 0
     c) Purity P_v(n) = |<v=0|psi_n>|^2 for each eigenstate n
  4. Compare E_J=0 (decoupled, purity=1 exactly) vs physical E_J
  5. Report per-cell and fabric seniority

Session: S61
Agent: nazarewicz-nuclear-structure-theorist
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
from canonical_constants import tau_fold, E_cond, N_dof_BCS, M_KK

# =====================================================================
#  0. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S60 RG integrals data (2-cell system at fold)
d60 = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)
eps_8 = d60['eps_fold']           # 8 single-particle energies at fold
V_8 = d60['V_fold']              # 8x8 pairing matrix
E_J_phys = float(d60['E_J_fold'])  # Josephson coupling = 3.397 M_KK
tau_fold_actual = float(d60['tau_fold'])

print("=" * 70)
print("S61: Seniority Purity on 2-Cell Fabric — SENIORITY-FABRIC-61")
print("=" * 70)
print(f"tau_fold = {tau_fold_actual:.6f}")
print(f"E_J_phys = {E_J_phys:.4f} M_KK")
print(f"8-mode eps_fold = {eps_8}")
print(f"8-mode V_fold diag = {np.diag(V_8)}")


# =====================================================================
#  1. FOCK-SPACE MACHINERY (pair representation)
# =====================================================================

def build_fock_space(n_pair, n_slots):
    """Build pair Fock space: n_pair Cooper pairs in n_slots pair-slots.
    Returns (pair_states, state_index, dim)."""
    if n_pair == 0:
        return [()], {(): 0}, 1
    states = list(combinations(range(n_slots), n_pair))
    index = {s: i for i, s in enumerate(states)}
    return states, index, len(states)


def build_hamiltonian(n_pair, n_modes, n_cells, eps, V, E_J):
    """Build BCS + Josephson Hamiltonian for n_pair pairs.

    Pair-slot index: slot = cell * n_modes + mode

    H = H_kinetic + H_pairing + H_Josephson
    H_kinetic: 2*eps[mode] per occupied slot
    H_pairing: -V[k,l] scatters pair from mode l to k within same cell
    H_Josephson: -(E_J/2) for moving a pair between cells (any mode)
    """
    n_slots = n_modes * n_cells

    if n_pair == 0:
        return np.array([[0.0]])

    pair_states, state_index, dim = build_fock_space(n_pair, n_slots)
    H = np.zeros((dim, dim), dtype=np.float64)

    for i, slots_i in enumerate(pair_states):
        slots_set = set(slots_i)
        infos = [(s % n_modes, s // n_modes) for s in slots_i]  # (mode, cell)

        # --- Diagonal: kinetic + diagonal pairing ---
        for (mk, ck) in infos:
            H[i, i] += 2.0 * eps[mk]
            H[i, i] -= V[mk, mk]

        # --- Off-diagonal pairing (within same cell) ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * n_modes + m_p

            for k in range(n_modes):
                if k == m_p:
                    continue  # diagonal already counted
                new_slot = c_p * n_modes + k
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] -= V[k, m_p]

        # --- Josephson tunneling ---
        for p_idx in range(n_pair):
            m_p, c_p = infos[p_idx]
            old_slot = c_p * n_modes + m_p
            target_cell = 1 - c_p

            for l in range(n_modes):
                new_slot = target_cell * n_modes + l
                if new_slot in slots_set:
                    continue  # Pauli blocked
                new_slots = list(slots_i)
                new_slots[new_slots.index(old_slot)] = new_slot
                new_state = tuple(sorted(new_slots))
                if new_state in state_index:
                    j = state_index[new_state]
                    H[j, i] += -E_J / 2.0

    # Symmetrize
    H = 0.5 * (H + H.T)
    return H


# =====================================================================
#  2. SENIORITY PROJECTION OPERATORS
# =====================================================================

def build_seniority_zero_state(n_pair, n_modes, n_cells):
    """Construct the seniority-zero state |v=0, N> in the pair Fock space.

    For a SINGLE cell: |v=0, N> ~ (S_+)^N |0> = sum over all N-pair
    combinations of modes, each with EQUAL weight (BCS condensate limit).

    For the FABRIC (2 cells): the fabric S_+ = S_+^(0) + S_+^(1).
    (S_+^fabric)^N |0> involves distributing N pairs across both cells
    in all possible ways with equal weight per pair-slot combination.

    Returns: normalized vector in pair-Fock basis.
    """
    n_slots = n_modes * n_cells
    pair_states, state_index, dim = build_fock_space(n_pair, n_slots)

    # The seniority-zero state is (S_+)^N |0> / norm
    # where S_+ = sum_{s=0}^{n_slots-1} c_{s,up}^dag c_{s,down}^dag
    # Acting N times: (S_+)^N |0> = sum_{s1<s2<...<sN} sum_{perm} |s_{p1},...,s_{pN}>
    # In the pair-Fock basis where states are sorted tuples, each basis state
    # gets coefficient 1 (every N-combination appears once).
    v0 = np.ones(dim, dtype=np.float64)
    v0 /= np.linalg.norm(v0)
    return v0


def build_per_cell_seniority_zero(n_pair, n_modes, n_cells):
    """Construct states with definite per-cell seniority (v_0, v_1).

    For the 2-cell system with N pairs total, we can distribute them
    as (n_0, n_1) with n_0 + n_1 = N. Within each cell, the
    seniority-zero state is (S_+^alpha)^{n_alpha} |0>.

    Returns dict: {(n_0, n_1): normalized_vector}
    """
    n_slots = n_modes * n_cells
    pair_states, state_index, dim = build_fock_space(n_pair, n_slots)

    result = {}
    for n_0 in range(n_pair + 1):
        n_1 = n_pair - n_0
        if n_0 > n_modes or n_1 > n_modes:
            continue

        # States with n_0 pairs in cell 0 (slots 0..n_modes-1)
        # and n_1 pairs in cell 1 (slots n_modes..2*n_modes-1)
        cell0_combos = list(combinations(range(n_modes), n_0)) if n_0 > 0 else [()]
        cell1_combos = list(combinations(range(n_modes, 2 * n_modes), n_1)) if n_1 > 0 else [()]

        vec = np.zeros(dim, dtype=np.float64)
        count = 0  # (local)
        for c0 in cell0_combos:
            for c1 in cell1_combos:
                state = tuple(sorted(c0 + c1))
                if state in state_index:
                    vec[state_index[state]] = 1.0
                    count += 1

        if count > 0:
            vec /= np.linalg.norm(vec)
            result[(n_0, n_1)] = vec

    return result


def compute_seniority_purity(eigvecs, n_pair, n_modes, n_cells, label=""):
    """Compute seniority purity for each eigenstate.

    Two definitions:
    1. Fabric seniority: overlap with (S_+^fabric)^N |0>
    2. Per-cell seniority: max over (n_0, n_1) partitions of
       overlap with per-cell v=0 states

    Returns dict with purity arrays.
    """
    n_slots = n_modes * n_cells
    dim = eigvecs.shape[0]
    n_states = eigvecs.shape[1]

    # 1. Fabric seniority-zero state
    v0_fabric = build_seniority_zero_state(n_pair, n_modes, n_cells)

    # Fabric purity: P_fabric(n) = |<v0_fabric|psi_n>|^2
    P_fabric = np.abs(eigvecs.T @ v0_fabric)**2

    # 2. Per-cell seniority-zero states
    cell_states = build_per_cell_seniority_zero(n_pair, n_modes, n_cells)

    # Per-cell purity: max overlap with any (v0_0, v0_1) product
    P_cell_max = np.zeros(n_states)
    P_cell_all = {}
    for (n0, n1), vec in cell_states.items():
        overlaps = np.abs(eigvecs.T @ vec)**2
        P_cell_all[(n0, n1)] = overlaps
        P_cell_max = np.maximum(P_cell_max, overlaps)

    # 3. Total v=0 subspace: span of all per-cell v=0 states
    # Project eigenstates onto the v=0 subspace
    if len(cell_states) > 0:
        V_basis = np.column_stack(list(cell_states.values()))
        # Gram-Schmidt to orthonormalize
        Q, R = np.linalg.qr(V_basis)
        rank = np.sum(np.abs(np.diag(R)) > 1e-12)
        Q = Q[:, :rank]
        P_v0_subspace = np.sum(np.abs(Q.T @ eigvecs)**2, axis=0)
    else:
        P_v0_subspace = np.zeros(n_states)

    if label:
        print(f"\n  [{label}] Fabric v=0 purity (GS): {P_fabric[0]:.6f}")
        print(f"  [{label}] Cell-max v=0 purity (GS): {P_cell_max[0]:.6f}")
        print(f"  [{label}] v=0 subspace purity (GS): {P_v0_subspace[0]:.6f}")
        print(f"  [{label}] All-state mean fabric purity: {np.mean(P_fabric):.6f}")

    return {
        'P_fabric': P_fabric,
        'P_cell_max': P_cell_max,
        'P_v0_subspace': P_v0_subspace,
        'P_cell_all': P_cell_all,
    }


# =====================================================================
#  3. COHERENCE FACTOR SENIORITY MEASURE (Z_k proxy)
# =====================================================================

def compute_Zk_purity(eigvecs, pair_states, n_modes, n_cells):
    """Compute coherence-factor based seniority purity.

    For each eigenstate |psi>, compute:
      n_k = <psi| hat{n}_k |psi>  (occupation of slot k)
      Z_k = n_k * (1 - n_k)       (coherence factor)

    Seniority-zero has Z_k -> 0.25 for all active modes (half-filled).
    Seniority-max has Z_k -> 0 (modes either full or empty).

    Purity_Z = <Z_k>_active / 0.25 where active = modes with 0 < n_k < 1.

    This was the NAZ-6 measure: 0.60 (N=1), 0.94 (N=2), 0.98 (N=3).
    """
    n_slots = n_modes * n_cells
    dim = len(pair_states)
    n_eig = eigvecs.shape[1]

    results = []
    for e_idx in range(n_eig):
        psi = eigvecs[:, e_idx]
        probs = psi**2  # |<basis|psi>|^2

        # Compute occupation of each slot
        n_occ = np.zeros(n_slots)
        for i, state in enumerate(pair_states):
            for s in state:
                n_occ[s] += probs[i]

        # Coherence factors
        Z_k = n_occ * (1.0 - n_occ)

        # Active modes: those with nontrivial occupation
        active = (n_occ > 0.01) & (n_occ < 0.99)
        if np.any(active):
            purity_Z = np.mean(Z_k[active]) / 0.25
        else:
            # All modes fully occupied or empty: seniority is maximal
            purity_Z = 0.0  # (local)

        results.append({
            'n_occ': n_occ,
            'Z_k': Z_k,
            'purity_Z': purity_Z,
            'n_active': np.sum(active),
        })

    return results


# =====================================================================
#  4. REDUCED MODEL: 2 modes per cell (dim=16 at N=2)
# =====================================================================

print("\n" + "=" * 70)
print("  PART A: REDUCED MODEL (2 modes/cell)")
print("=" * 70)

# Select 2 modes from the 8-mode spectrum: one from B2 sector, one from B1
# Use modes 0 (B2, lowest) and 4 (B1, Fermi-surface mode)
# These are the most physically relevant: the Fermi-surface mode and the
# lowest-energy mode that drives pairing
mode_indices = [0, 4]
eps_2 = eps_8[mode_indices]
V_2 = V_8[np.ix_(mode_indices, mode_indices)]

print(f"\nReduced model: modes {mode_indices}")
print(f"  eps_2 = {eps_2}")
print(f"  V_2 = \n{V_2}")
print(f"  E_J = {E_J_phys:.4f}")

n_modes_red = 2
n_cells = 2
n_slots_red = n_modes_red * n_cells  # 4 slots

# Sweep over E_J from 0 to physical value
E_J_values = [0.0, 0.1, 0.5, 1.0, 2.0, E_J_phys, 5.0, 10.0]
results_reduced = {}

for N_pair in [1, 2]:
    print(f"\n--- N_pair = {N_pair}, reduced model ---")
    pair_states_N, state_index_N, dim_N = build_fock_space(N_pair, n_slots_red)
    print(f"  dim = {dim_N}")

    sweep_data = []
    for ej in E_J_values:
        H = build_hamiltonian(N_pair, n_modes_red, n_cells, eps_2, V_2, ej)
        evals, evecs = eigh(H)

        # Seniority purity
        sen = compute_seniority_purity(evecs, N_pair, n_modes_red, n_cells,
                                       label=f"N={N_pair}, E_J={ej:.3f}")

        # Z_k purity
        zk = compute_Zk_purity(evecs, pair_states_N, n_modes_red, n_cells)

        sweep_data.append({
            'E_J': ej,
            'evals': evals,
            'P_fabric_gs': sen['P_fabric'][0],
            'P_cell_max_gs': sen['P_cell_max'][0],
            'P_v0_sub_gs': sen['P_v0_subspace'][0],
            'P_fabric_all': sen['P_fabric'],
            'P_cell_max_all': sen['P_cell_max'],
            'purity_Z_gs': zk[0]['purity_Z'],
            'n_occ_gs': zk[0]['n_occ'],
            'Z_k_gs': zk[0]['Z_k'],
        })

    results_reduced[N_pair] = sweep_data


# =====================================================================
#  5. FULL MODEL: 8 modes per cell, N_pair = 1
# =====================================================================

print("\n" + "=" * 70)
print("  PART B: FULL 8-MODE MODEL (N_pair=1, dim=16)")
print("=" * 70)

n_modes_full = 8
n_slots_full = n_modes_full * n_cells  # 16 slots

# N=1: dim = C(16,1) = 16
pair_states_1, state_index_1, dim_1 = build_fock_space(1, n_slots_full)
print(f"  dim(N=1) = {dim_1}")

results_full_N1 = []
E_J_sweep_full = [0.0, 0.5, 1.0, 2.0, E_J_phys, 5.0, 10.0]

for ej in E_J_sweep_full:
    H = build_hamiltonian(1, n_modes_full, n_cells, eps_8, V_8, ej)
    evals, evecs = eigh(H)

    # Seniority purity
    sen = compute_seniority_purity(evecs, 1, n_modes_full, n_cells,
                                   label=f"8-mode N=1, E_J={ej:.3f}")

    # Z_k purity
    zk = compute_Zk_purity(evecs, pair_states_1, n_modes_full, n_cells)

    results_full_N1.append({
        'E_J': ej,
        'evals': evals,
        'P_fabric_gs': sen['P_fabric'][0],
        'P_cell_max_gs': sen['P_cell_max'][0],
        'P_v0_sub_gs': sen['P_v0_subspace'][0],
        'purity_Z_gs': zk[0]['purity_Z'],
        'n_occ_gs': zk[0]['n_occ'],
        'Z_k_gs': zk[0]['Z_k'],
        'P_fabric_all': sen['P_fabric'],
        'gap': evals[1] - evals[0] if len(evals) > 1 else 0.0,
    })


# =====================================================================
#  6. FULL MODEL: 8 modes per cell, N_pair = 2 (dim = C(16,2) = 120)
# =====================================================================

print("\n" + "=" * 70)
print("  PART C: FULL 8-MODE MODEL (N_pair=2, dim=120)")
print("=" * 70)

pair_states_2, state_index_2, dim_2 = build_fock_space(2, n_slots_full)
print(f"  dim(N=2) = {dim_2}")

results_full_N2 = []

for ej in E_J_sweep_full:
    H = build_hamiltonian(2, n_modes_full, n_cells, eps_8, V_8, ej)
    evals, evecs = eigh(H)

    # Seniority purity
    sen = compute_seniority_purity(evecs, 2, n_modes_full, n_cells,
                                   label=f"8-mode N=2, E_J={ej:.3f}")

    # Z_k purity
    zk = compute_Zk_purity(evecs, pair_states_2, n_modes_full, n_cells)

    results_full_N2.append({
        'E_J': ej,
        'evals': evals,
        'P_fabric_gs': sen['P_fabric'][0],
        'P_cell_max_gs': sen['P_cell_max'][0],
        'P_v0_sub_gs': sen['P_v0_subspace'][0],
        'purity_Z_gs': zk[0]['purity_Z'],
        'n_occ_gs': zk[0]['n_occ'],
        'Z_k_gs': zk[0]['Z_k'],
        'P_fabric_all': sen['P_fabric'],
        'gap': evals[1] - evals[0] if len(evals) > 1 else 0.0,
    })


# =====================================================================
#  7. SINGLE-CELL REFERENCE (NAZ-6 reproduction)
# =====================================================================

print("\n" + "=" * 70)
print("  PART D: SINGLE-CELL REFERENCE (8 modes, N=1,2,3)")
print("=" * 70)

results_single_cell = {}
for N_sc in [1, 2, 3]:
    pair_states_sc, state_index_sc, dim_sc = build_fock_space(N_sc, 8)
    H_sc = build_hamiltonian(N_sc, 8, 1, eps_8, V_8, 0.0)  # No Josephson
    evals_sc, evecs_sc = eigh(H_sc)

    sen_sc = compute_seniority_purity(evecs_sc, N_sc, 8, 1,
                                      label=f"1-cell N={N_sc}")
    zk_sc = compute_Zk_purity(evecs_sc, pair_states_sc, 8, 1)

    results_single_cell[N_sc] = {
        'P_fabric_gs': sen_sc['P_fabric'][0],
        'P_v0_sub_gs': sen_sc['P_v0_subspace'][0],
        'purity_Z_gs': zk_sc[0]['purity_Z'],
        'n_occ_gs': zk_sc[0]['n_occ'],
        'Z_k_gs': zk_sc[0]['Z_k'],
        'gs_energy': evals_sc[0],
    }
    print(f"\n  Single-cell N={N_sc}: P_fabric={sen_sc['P_fabric'][0]:.6f}, "
          f"P_Z={zk_sc[0]['purity_Z']:.6f}")


# =====================================================================
#  8. SUMMARY AND ANALYSIS
# =====================================================================

print("\n" + "=" * 70)
print("  RESULTS SUMMARY")
print("=" * 70)

# --- Single-cell reference ---
print("\n--- Single-cell seniority (NAZ-6 reference) ---")
print(f"  {'N':>3s}  {'P_fabric':>10s}  {'P_v0_sub':>10s}  {'P_Z':>10s}")
for N_sc in [1, 2, 3]:
    r = results_single_cell[N_sc]
    print(f"  {N_sc:3d}  {r['P_fabric_gs']:10.6f}  {r['P_v0_sub_gs']:10.6f}  "
          f"{r['purity_Z_gs']:10.6f}")

# --- Reduced model E_J sweep ---
print("\n--- Reduced model (2 modes/cell) E_J sweep ---")
for N_pair in [1, 2]:
    print(f"\n  N_pair = {N_pair}:")
    print(f"  {'E_J':>8s}  {'P_fabric':>10s}  {'P_cell_max':>10s}  "
          f"{'P_v0_sub':>10s}  {'P_Z':>10s}")
    for d in results_reduced[N_pair]:
        print(f"  {d['E_J']:8.3f}  {d['P_fabric_gs']:10.6f}  "
              f"{d['P_cell_max_gs']:10.6f}  {d['P_v0_sub_gs']:10.6f}  "
              f"{d['purity_Z_gs']:10.6f}")

# --- Full model E_J sweep ---
print("\n--- Full 8-mode model E_J sweep ---")
print("\n  N_pair = 1 (dim=16):")
print(f"  {'E_J':>8s}  {'P_fabric':>10s}  {'P_cell_max':>10s}  "
      f"{'P_v0_sub':>10s}  {'P_Z':>10s}  {'gap':>8s}")
for d in results_full_N1:
    print(f"  {d['E_J']:8.3f}  {d['P_fabric_gs']:10.6f}  "
          f"{d['P_cell_max_gs']:10.6f}  {d['P_v0_sub_gs']:10.6f}  "
          f"{d['purity_Z_gs']:10.6f}  {d['gap']:8.4f}")

print("\n  N_pair = 2 (dim=120):")
print(f"  {'E_J':>8s}  {'P_fabric':>10s}  {'P_cell_max':>10s}  "
      f"{'P_v0_sub':>10s}  {'P_Z':>10s}  {'gap':>8s}")
for d in results_full_N2:
    print(f"  {d['E_J']:8.3f}  {d['P_fabric_gs']:10.6f}  "
          f"{d['P_cell_max_gs']:10.6f}  {d['P_v0_sub_gs']:10.6f}  "
          f"{d['purity_Z_gs']:10.6f}  {d['gap']:8.4f}")


# =====================================================================
#  9. SPECTRAL DISTRIBUTION OF PURITY
# =====================================================================

print("\n--- Full spectrum purity at physical E_J ---")
# Find physical E_J entry
phys_n1 = [d for d in results_full_N1 if abs(d['E_J'] - E_J_phys) < 0.01][0]
phys_n2 = [d for d in results_full_N2 if abs(d['E_J'] - E_J_phys) < 0.01][0]

# N=1 spectrum
p_fab_n1 = phys_n1['P_fabric_all']
n1_high = np.sum(p_fab_n1 > 0.5)
n1_low = np.sum(p_fab_n1 < 0.3)
print(f"\n  N=1 (16 states): mean P_fabric = {np.mean(p_fab_n1):.4f}, "
      f"median = {np.median(p_fab_n1):.4f}")
print(f"    States with P > 0.5: {n1_high}/{len(p_fab_n1)}")
print(f"    States with P < 0.3: {n1_low}/{len(p_fab_n1)}")
print(f"    GS: {p_fab_n1[0]:.6f}, 1st excited: {p_fab_n1[1]:.6f}")

# N=2 spectrum
p_fab_n2 = phys_n2['P_fabric_all']
n2_high = np.sum(p_fab_n2 > 0.5)
n2_low = np.sum(p_fab_n2 < 0.3)
print(f"\n  N=2 (120 states): mean P_fabric = {np.mean(p_fab_n2):.4f}, "
      f"median = {np.median(p_fab_n2):.4f}")
print(f"    States with P > 0.5: {n2_high}/{len(p_fab_n2)}")
print(f"    States with P < 0.3: {n2_low}/{len(p_fab_n2)}")
print(f"    GS: {p_fab_n2[0]:.6f}, 1st excited: {p_fab_n2[1]:.6f}")


# =====================================================================
#  10. GATE VERDICT
# =====================================================================

# Physical E_J results
gs_purity_n1 = phys_n1['P_fabric_gs']
gs_purity_n2 = phys_n2['P_fabric_gs']
gs_pZ_n1 = phys_n1['purity_Z_gs']
gs_pZ_n2 = phys_n2['purity_Z_gs']

# Comparison with single-cell
sc_pZ_1 = results_single_cell[1]['purity_Z_gs']
sc_pZ_2 = results_single_cell[2]['purity_Z_gs']

# Decoupled reference (E_J=0)
dec_n1 = [d for d in results_full_N1 if d['E_J'] == 0.0][0]
dec_n2 = [d for d in results_full_N2 if d['E_J'] == 0.0][0]

print("\n" + "=" * 70)
print("  GATE VERDICT: SENIORITY-FABRIC-61")
print("=" * 70)

print(f"\n  Fabric seniority-zero purity (GS):")
print(f"    N=1: E_J=0 -> {dec_n1['P_fabric_gs']:.6f}, "
      f"E_J={E_J_phys:.3f} -> {gs_purity_n1:.6f}")
print(f"    N=2: E_J=0 -> {dec_n2['P_fabric_gs']:.6f}, "
      f"E_J={E_J_phys:.3f} -> {gs_purity_n2:.6f}")

print(f"\n  Z_k purity (GS):")
print(f"    N=1: 1-cell={sc_pZ_1:.6f}, 2-cell(E_J=phys)={gs_pZ_n1:.6f}")
print(f"    N=2: 1-cell={sc_pZ_2:.6f}, 2-cell(E_J=phys)={gs_pZ_n2:.6f}")

# Verdict logic
all_gs_above_05 = (gs_purity_n1 > 0.5) and (gs_purity_n2 > 0.5)
any_gs_below_03 = (gs_purity_n1 < 0.3) or (gs_purity_n2 < 0.3)

if all_gs_above_05:
    verdict = "INFO (seniority SURVIVES on fabric, purity > 0.5)"
elif any_gs_below_03:
    verdict = "INFO (seniority DESTROYED on fabric, purity < 0.3)"
else:
    verdict = "INFO (seniority PARTIALLY survives, 0.3 < purity < 0.5)"

print(f"\n  VERDICT: {verdict}")


# =====================================================================
#  11. PLOTS
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): E_J sweep for fabric seniority purity (full model)
ax = axes[0, 0]
ej_n1 = [d['E_J'] for d in results_full_N1]
pf_n1 = [d['P_fabric_gs'] for d in results_full_N1]
ej_n2 = [d['E_J'] for d in results_full_N2]
pf_n2 = [d['P_fabric_gs'] for d in results_full_N2]
ax.plot(ej_n1, pf_n1, 'bo-', label='N=1 (dim=16)', markersize=8)
ax.plot(ej_n2, pf_n2, 'rs-', label='N=2 (dim=120)', markersize=8)
ax.axvline(E_J_phys, color='gray', linestyle='--', alpha=0.7, label=f'E_J phys={E_J_phys:.2f}')
ax.axhline(0.5, color='green', linestyle=':', alpha=0.5, label='purity=0.5')
ax.axhline(0.3, color='red', linestyle=':', alpha=0.5, label='purity=0.3')
ax.set_xlabel('E_J (M_KK)')
ax.set_ylabel('Fabric seniority-zero purity (GS)')
ax.set_title('(a) Fabric Seniority vs Josephson Coupling')
ax.legend(fontsize=8)
ax.set_ylim(-0.05, 1.05)

# Panel (b): Z_k purity E_J sweep
ax = axes[0, 1]
pz_n1 = [d['purity_Z_gs'] for d in results_full_N1]
pz_n2 = [d['purity_Z_gs'] for d in results_full_N2]
ax.plot(ej_n1, pz_n1, 'bo-', label='N=1', markersize=8)
ax.plot(ej_n2, pz_n2, 'rs-', label='N=2', markersize=8)
# Single-cell references
ax.axhline(sc_pZ_1, color='blue', linestyle=':', alpha=0.4, label=f'1-cell N=1: {sc_pZ_1:.3f}')
ax.axhline(sc_pZ_2, color='red', linestyle=':', alpha=0.4, label=f'1-cell N=2: {sc_pZ_2:.3f}')
ax.axvline(E_J_phys, color='gray', linestyle='--', alpha=0.7)
ax.set_xlabel('E_J (M_KK)')
ax.set_ylabel('Z_k purity (GS)')
ax.set_title('(b) Coherence Factor Purity vs E_J')
ax.legend(fontsize=8)
ax.set_ylim(-0.05, 1.05)

# Panel (c): Spectral distribution of purity at physical E_J, N=2
ax = axes[1, 0]
ax.bar(range(len(p_fab_n2)), sorted(p_fab_n2, reverse=True), color='steelblue', alpha=0.7)
ax.axhline(0.5, color='green', linestyle=':', alpha=0.5)
ax.axhline(0.3, color='red', linestyle=':', alpha=0.5)
ax.set_xlabel('Eigenstate index (sorted by purity)')
ax.set_ylabel('Fabric seniority-zero purity')
ax.set_title(f'(c) Purity Distribution, N=2, E_J={E_J_phys:.2f}')
ax.set_xlim(-1, min(30, len(p_fab_n2)))  # Show first 30

# Panel (d): Occupation profile at physical E_J
ax = axes[1, 1]
n_occ_n1 = phys_n1['n_occ_gs']
n_occ_n2 = phys_n2['n_occ_gs']
x_labels = [f'C0:m{i}' for i in range(8)] + [f'C1:m{i}' for i in range(8)]
x = np.arange(16)
width = 0.35  # (local)
ax.bar(x - width/2, n_occ_n1, width, label='N=1', alpha=0.7, color='blue')
ax.bar(x + width/2, n_occ_n2, width, label='N=2', alpha=0.7, color='red')
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=45, ha='right', fontsize=6)
ax.set_ylabel('Occupation n_k')
ax.set_title(f'(d) GS Occupation at E_J={E_J_phys:.2f}')
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's61_seniority_fabric.png'), dpi=150)
print(f"\nPlot saved: s61_seniority_fabric.png")


# =====================================================================
#  12. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's61_seniority_fabric.npz')

# Collect key results
np.savez(save_path,
    # Input parameters
    tau_fold=tau_fold_actual,
    E_J_phys=E_J_phys,
    eps_8=eps_8,
    V_8_diag=np.diag(V_8),
    eps_2=eps_2,
    V_2=V_2,
    mode_indices_reduced=np.array(mode_indices),

    # Single-cell reference (NAZ-6)
    sc_purity_Z=np.array([results_single_cell[n]['purity_Z_gs'] for n in [1,2,3]]),
    sc_P_fabric=np.array([results_single_cell[n]['P_fabric_gs'] for n in [1,2,3]]),

    # Full model N=1 sweep
    full_N1_E_J=np.array([d['E_J'] for d in results_full_N1]),
    full_N1_P_fabric=np.array([d['P_fabric_gs'] for d in results_full_N1]),
    full_N1_P_cell_max=np.array([d['P_cell_max_gs'] for d in results_full_N1]),
    full_N1_P_v0_sub=np.array([d['P_v0_sub_gs'] for d in results_full_N1]),
    full_N1_purity_Z=np.array([d['purity_Z_gs'] for d in results_full_N1]),
    full_N1_gap=np.array([d['gap'] for d in results_full_N1]),

    # Full model N=2 sweep
    full_N2_E_J=np.array([d['E_J'] for d in results_full_N2]),
    full_N2_P_fabric=np.array([d['P_fabric_gs'] for d in results_full_N2]),
    full_N2_P_cell_max=np.array([d['P_cell_max_gs'] for d in results_full_N2]),
    full_N2_P_v0_sub=np.array([d['P_v0_sub_gs'] for d in results_full_N2]),
    full_N2_purity_Z=np.array([d['purity_Z_gs'] for d in results_full_N2]),
    full_N2_gap=np.array([d['gap'] for d in results_full_N2]),

    # Spectral purity at physical E_J
    spec_N1_P_fabric=p_fab_n1,
    spec_N2_P_fabric=p_fab_n2,

    # Physical E_J ground-state occupations
    n_occ_N1_phys=phys_n1['n_occ_gs'],
    n_occ_N2_phys=phys_n2['n_occ_gs'],
    Z_k_N1_phys=phys_n1['Z_k_gs'],
    Z_k_N2_phys=phys_n2['Z_k_gs'],

    # Reduced model sweeps
    red_N1_E_J=np.array([d['E_J'] for d in results_reduced[1]]),
    red_N1_P_fabric=np.array([d['P_fabric_gs'] for d in results_reduced[1]]),
    red_N2_E_J=np.array([d['E_J'] for d in results_reduced[2]]),
    red_N2_P_fabric=np.array([d['P_fabric_gs'] for d in results_reduced[2]]),

    # Gate
    gate_name=np.array(['SENIORITY-FABRIC-61']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([verdict]),
)

print(f"\nData saved: {save_path}")
print("\n" + "=" * 70)
print("  COMPUTATION COMPLETE")
print("=" * 70)
