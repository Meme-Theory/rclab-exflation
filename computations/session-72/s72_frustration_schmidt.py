#!/usr/bin/env python3
"""
S72 FRUSTRATION-SCHMIDT-72: Per-Junction Schmidt Number on Frustrated Sub-Graphs
==================================================================================

PHYSICS:
    S71 INTER-SITE-ENTANGLE-71 found K = 3.99 (near-maximal 4-state entanglement)
    for an isolated 2-cell BCS+Josephson junction at N_pair = 2.  S71 THREE-CELL-GSL
    showed that frustration on a 3-cell ring reduces S_GGE by 48%.

    This computation asks: how does geometric frustration affect the QUANTUM
    entanglement (Schmidt number) at individual junctions?

    The physical picture (Landau quasiparticle framework):
    - Each cell has 8 BCS modes (4 B2 + 1 B1 + 3 B3) at the fold
    - Cells are coupled by Josephson pair-tunneling J_C2 = 0.933 M_KK
    - The frustrated triangle forces 120-degree phase separation
    - The 4-cell ring (C_4, bipartite) has NO frustration
    - The 4-cell open chain has boundary effects but no frustration

    Symmetry analysis:
    - 2-cell: Z_2 swap symmetry. Order parameter space U(1)/Z_2.
    - 3-cell ring (C_3): Z_3 cyclic symmetry, frustrated (odd ring).
      Ground state breaks Z_3 -> Z_1 (selects chirality).
    - 4-cell ring (C_4): Z_4 cyclic symmetry, NOT frustrated (even ring).
      Ground state preserves Z_2 sublattice symmetry.
    - 4-cell chain: no cyclic symmetry, open boundary.

    Hilbert space construction:
    For N_cell cells at N_pair = 2 with 8 modes per cell:
    - 2-cell: C(16, 2) = 120 states (from S71)
    - 3-cell: C(24, 2) = 276 states
    - 4-cell: C(32, 2) = 496 states
    All tractable by exact diagonalization.

    The Schmidt number K = 1/Tr(rho_A^2) where rho_A is the reduced density
    matrix of one cell obtained by tracing out all others.

Gate: FRUSTRATION-SCHMIDT-72
    PASS: K(frustrated 3-cell ring) > 2.0
    INFO: K in [1.5, 2.0]
    FAIL: K < 1.5

Cross-checks:
    1. J -> 0 limit: K -> 1 (product state, pairs localized)
    2. J -> infinity limit: K -> 4 (maximally delocalized over 4 n1-sectors)
    3. K(2-cell) must reproduce S71 result: K = 3.99
    4. Z_2 symmetry of ring ground states: S(cell_i) = S(cell_j) for all i,j

Author: landau-condensed-matter-theorist (Session 72, Wave 4)
Date: 2026-04-10
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh
from itertools import combinations

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    PI, N_cells as N_CELLS_FABRIC, tau_fold, T_acoustic,
    E_cond, Delta_BCS, Delta_0_OES,
    J_C2, J_su2, J_u1,
    N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("FRUSTRATION-SCHMIDT-72: Per-Junction Schmidt Number on Frustrated Graphs")
print("=" * 78)

# ============================================================================
# SECTION 1: LOAD UPSTREAM DATA
# ============================================================================
print("\n--- Section 1: Load upstream data ---")

# BCS Hamiltonian ingredients from S60
pt_data = np.load(os.path.join(SCRIPT_DIR, 's60_pair_transfer_n4.npz'), allow_pickle=True)
eps_fold = pt_data['eps_fold']      # 8 single-particle energies at fold
V_fold = pt_data['V_fold']          # 8x8 pairing interaction matrix
E_J_fold = float(pt_data['E_J_fold'])

# S71 isolated junction results (cross-check target)
s71_data = np.load(os.path.join(SCRIPT_DIR, 's71_inter_site_entangle.npz'), allow_pickle=True)
K_isolated = float(s71_data['schmidt_number'])
S_vN_isolated = float(s71_data['S_vN_GS_bits'])

# S71 3-cell frustration data (entropy comparison)
s71_3cell = np.load(os.path.join(SCRIPT_DIR, 's71_three_cell_gsl.npz'), allow_pickle=True)
S_GGE_frust_s71 = float(s71_3cell['S_GGE_cell_frust'])
S_GGE_bare_s71 = float(s71_3cell['S_GGE_cell_bare'])

N = N_dof_BCS  # 8 modes per cell
sector_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1[0]', 'B3[0]', 'B3[1]', 'B3[2]']

print(f"  N_modes/cell = {N}")
print(f"  J_C2 = {J_C2:.3f} M_KK")
print(f"  E_J_fold = {E_J_fold:.6f} M_KK (from S60 2-cell)")
print(f"  Delta_BCS = {Delta_BCS:.6f} M_KK")
print(f"  J_C2/Delta = {J_C2/Delta_BCS:.4f} (strong coupling)")
print(f"  K_isolated (S71) = {K_isolated:.4f}")
print(f"  S_vN_isolated (S71) = {S_vN_isolated:.6f} bits")
print(f"  S_GGE_frust (S71 3-cell) = {S_GGE_frust_s71:.6f} nats")
print(f"  S_GGE_bare  (S71 3-cell) = {S_GGE_bare_s71:.6f} nats")
print(f"  Frustration reduction ratio = {S_GGE_frust_s71/S_GGE_bare_s71:.4f}")

print(f"\n  Single-particle energies eps_fold:")
for i in range(N):
    print(f"    {sector_labels[i]}: eps = {eps_fold[i]:.10f} M_KK")


# ============================================================================
# SECTION 2: GENERIC MULTI-CELL HAMILTONIAN BUILDER
# ============================================================================
print("\n--- Section 2: Generic multi-cell Hamiltonian builder ---")

def build_multi_cell_hamiltonian(n_cells, adjacency, eps, V_pair, E_J_val,
                                  n_modes, basis_list, lookup):
    """
    Build the N-cell BCS + Josephson Hamiltonian in the N_pair=2 sector.

    H = sum_c H_kinetic^(c) + sum_c H_pairing^(c) + sum_{<c,c'>} H_Josephson^(c,c')

    Kinetic:   sum_k 2*eps_k * n_{k,c}  (for each cell c)
    Pairing:   -V_{kk'} P^+_{k,c} P_{k',c}  (within each cell)
    Josephson: -E_J * sum_k (P^+_{k,c} P_{k,c'} + h.c.)  for each bond (c,c')

    Parameters:
        n_cells: number of cells
        adjacency: list of (i, j) bonds (0-indexed)
        eps: single-particle energies (n_modes,)
        V_pair: pairing matrix (n_modes, n_modes)
        E_J_val: Josephson coupling
        n_modes: modes per cell
        basis_list: list of basis state arrays (each of length n_cells * n_modes)
        lookup: dict mapping tuple(state) -> index
    """
    dim_H = len(basis_list)
    n_slots = n_cells * n_modes
    H = np.zeros((dim_H, dim_H), dtype=np.float64)

    for idx in range(dim_H):
        state = tuple(basis_list[idx])

        # --- Diagonal: kinetic energy ---
        E_kin = 0.0  # (local)
        for c in range(n_cells):
            offset = c * n_modes
            for k in range(n_modes):
                if state[offset + k] == 1:
                    E_kin += 2.0 * eps[k]
        H[idx, idx] += E_kin

        # --- Intra-cell pairing: -V_{kk'} P^+_k P_{k'} ---
        for c in range(n_cells):
            offset = c * n_modes
            for k in range(n_modes):
                for kp in range(n_modes):
                    if k == kp:
                        continue
                    if state[offset + kp] == 1 and state[offset + k] == 0:
                        ns = list(state)
                        ns[offset + kp] = 0
                        ns[offset + k] = 1
                        nst = tuple(ns)
                        if nst in lookup:
                            H[idx, lookup[nst]] += -V_pair[k, kp]

        # --- Inter-cell Josephson: -E_J * P^+_{k,c} P_{k,c'} + h.c. ---
        for (c1, c2) in adjacency:
            off1 = c1 * n_modes
            off2 = c2 * n_modes
            for k in range(n_modes):
                # Transfer from cell c2 to cell c1
                if state[off2 + k] == 1 and state[off1 + k] == 0:
                    ns = list(state)
                    ns[off2 + k] = 0
                    ns[off1 + k] = 1
                    nst = tuple(ns)
                    if nst in lookup:
                        H[idx, lookup[nst]] += -E_J_val
                # Transfer from cell c1 to cell c2 (h.c.)
                if state[off1 + k] == 1 and state[off2 + k] == 0:
                    ns = list(state)
                    ns[off1 + k] = 0
                    ns[off2 + k] = 1
                    nst = tuple(ns)
                    if nst in lookup:
                        H[idx, lookup[nst]] += -E_J_val

    # Symmetrize (enforce numerical symmetry)
    H = 0.5 * (H + H.T)
    return H


def build_fock_basis(n_slots, n_pair):
    """Build the N_pair sector Fock basis for n_slots pair-mode slots."""
    basis_tuples = list(combinations(range(n_slots), n_pair))
    dim = len(basis_tuples)
    basis = []
    for combo in basis_tuples:
        s = np.zeros(n_slots, dtype=int)
        for c in combo:
            s[c] = 1
        basis.append(s)
    lookup = {tuple(b): i for i, b in enumerate(basis)}
    return basis, lookup, dim


def build_cell_basis(n_modes, max_pairs):
    """Build the reduced basis for a single cell with up to max_pairs pairs."""
    cell_basis = []
    for n_p in range(max_pairs + 1):
        if n_p == 0:
            cell_basis.append(tuple(np.zeros(n_modes, dtype=int)))
        else:
            for combo in combinations(range(n_modes), n_p):
                s = np.zeros(n_modes, dtype=int)
                for c in combo:
                    s[c] = 1
                cell_basis.append(tuple(s))
    cell_lookup = {s: i for i, s in enumerate(cell_basis)}
    return cell_basis, cell_lookup, len(cell_basis)


def partial_trace_single_cell(psi, target_cell, n_cells, n_modes,
                               basis_list, dim_H, cell_basis, cell_lookup):
    """
    Compute rho_target = Tr_{all other cells}(|psi><psi|).

    Groups full-space basis states by the configuration of all cells
    EXCEPT the target cell, then sums outer products of the target-cell
    amplitudes.
    """
    dim_target = len(cell_basis)
    rho = np.zeros((dim_target, dim_target), dtype=np.float64)

    # Group by "environment" configuration (all cells except target)
    env_groups = {}
    for idx_full in range(dim_H):
        state = basis_list[idx_full]
        # Extract target cell config
        off = target_cell * n_modes
        target_config = tuple(state[off:off + n_modes])
        # Extract environment config (everything else)
        env_config = tuple(state[:off]) + tuple(state[off + n_modes:])

        if target_config not in cell_lookup:
            continue
        a_idx = cell_lookup[target_config]

        if env_config not in env_groups:
            env_groups[env_config] = []
        env_groups[env_config].append((a_idx, idx_full))

    # Partial trace
    for env_config, a_list in env_groups.items():
        for (a_idx, full_idx) in a_list:
            for (a_idx_p, full_idx_p) in a_list:
                rho[a_idx, a_idx_p] += psi[full_idx] * psi[full_idx_p]

    return rho


def compute_entanglement_measures(rho):
    """Compute S_vN, S_2, purity, K from a density matrix."""
    evals = np.sort(np.linalg.eigvalsh(rho))[::-1]
    evals = np.maximum(evals, 0.0)
    s = np.sum(evals)
    if s > 0:
        evals /= s

    mask = evals > 1e-30
    S_vN_bits = -np.sum(evals[mask] * np.log2(evals[mask]))
    S_vN_nats = -np.sum(evals[mask] * np.log(evals[mask]))

    purity = np.sum(evals**2)
    S_2_bits = -np.log2(purity) if purity > 0 else np.inf
    K = 1.0 / purity if purity > 0 else np.inf

    return {
        'evals': evals,
        'S_vN_bits': S_vN_bits,
        'S_vN_nats': S_vN_nats,
        'S_2_bits': S_2_bits,
        'purity': purity,
        'K': K,
    }


def analyze_topology(label, n_cells, adjacency, eps, V_pair, E_J_val, n_modes, N_pair=2):
    """
    Full analysis for a given graph topology.
    Returns dict with all results.
    """
    n_slots = n_cells * n_modes
    print(f"\n  === {label}: {n_cells} cells, {len(adjacency)} bonds ===")
    print(f"  Adjacency: {adjacency}")
    print(f"  N_slots = {n_slots}, N_pair = {N_pair}")

    # Build Fock basis
    basis, lookup, dim = build_fock_basis(n_slots, N_pair)
    print(f"  Hilbert space dim = C({n_slots},{N_pair}) = {dim}")

    # Build cell basis (for partial trace)
    cell_basis, cell_lookup, dim_cell = build_cell_basis(n_modes, N_pair)
    print(f"  Cell reduced dim = {dim_cell}")

    # Build and diagonalize Hamiltonian
    t_build = time.time()
    H = build_multi_cell_hamiltonian(n_cells, adjacency, eps, V_pair, E_J_val,
                                      n_modes, basis, lookup)
    t_diag = time.time()
    print(f"  H build time: {t_diag - t_build:.2f} s")

    # Hermiticity check
    asym = np.max(np.abs(H - H.T))
    print(f"  Hermiticity: max|H - H^T| = {asym:.2e}")

    evals_all, evecs_all = eigh(H)
    t_done = time.time()
    print(f"  Diag time: {t_done - t_diag:.2f} s")

    E_GS = evals_all[0]
    gap = evals_all[1] - evals_all[0]
    print(f"  E_GS = {E_GS:.10f} M_KK")
    print(f"  Gap = {gap:.10f} M_KK")

    psi_GS = evecs_all[:, 0]

    # Compute partial trace for EACH cell
    K_per_cell = []
    S_per_cell = []
    results_per_cell = []

    for c in range(n_cells):
        rho_c = partial_trace_single_cell(psi_GS, c, n_cells, n_modes,
                                           basis, dim, cell_basis, cell_lookup)

        # Verify trace = 1
        tr = np.trace(rho_c)
        if abs(tr - 1.0) > 1e-10:
            print(f"  WARNING: Tr(rho_{c}) = {tr:.15f}")

        measures = compute_entanglement_measures(rho_c)
        K_per_cell.append(measures['K'])
        S_per_cell.append(measures['S_vN_bits'])
        results_per_cell.append(measures)
        print(f"  Cell {c}: K = {measures['K']:.4f}, S_vN = {measures['S_vN_bits']:.6f} bits, "
              f"purity = {measures['purity']:.8f}")

    K_mean = np.mean(K_per_cell)
    K_std = np.std(K_per_cell)
    S_mean = np.mean(S_per_cell)

    print(f"\n  K(mean) = {K_mean:.4f} +/- {K_std:.4f}")
    print(f"  S_vN(mean) = {S_mean:.6f} bits")

    # Z_n symmetry check: all cells should give same result for ring topologies
    K_spread = max(K_per_cell) - min(K_per_cell)
    print(f"  K spread (max-min) = {K_spread:.2e} (cyclic symmetry check)")

    return {
        'label': label,
        'n_cells': n_cells,
        'adjacency': adjacency,
        'dim': dim,
        'E_GS': E_GS,
        'gap': gap,
        'K_per_cell': np.array(K_per_cell),
        'S_per_cell': np.array(S_per_cell),
        'K_mean': K_mean,
        'K_std': K_std,
        'S_mean': S_mean,
        'evals_all': evals_all,
        'results_per_cell': results_per_cell,
    }


# ============================================================================
# SECTION 3: ANALYZE ALL TOPOLOGIES
# ============================================================================
print("\n" + "=" * 78)
print("Section 3: Analyze all topologies")
print("=" * 78)

# --- (A) 2-cell chain (S71 cross-check) ---
result_2cell = analyze_topology(
    "2-cell chain (S71 cross-check)",
    n_cells=2,
    adjacency=[(0, 1)],
    eps=eps_fold,
    V_pair=V_fold,
    E_J_val=E_J_fold,
    n_modes=N,
)

# Cross-check against S71
K_2cell = result_2cell['K_mean']
print(f"\n  S71 cross-check: K(here) = {K_2cell:.4f}, K(S71) = {K_isolated:.4f}")
print(f"  Difference: {abs(K_2cell - K_isolated):.2e}")

# --- (B) 3-cell ring (FRUSTRATED -- the main target) ---
result_3ring = analyze_topology(
    "3-cell ring (frustrated, C_3)",
    n_cells=3,
    adjacency=[(0, 1), (1, 2), (2, 0)],
    eps=eps_fold,
    V_pair=V_fold,
    E_J_val=E_J_fold,
    n_modes=N,
)

# --- (C) 4-cell ring (NOT frustrated, C_4) ---
result_4ring = analyze_topology(
    "4-cell ring (unfrustrated, C_4)",
    n_cells=4,
    adjacency=[(0, 1), (1, 2), (2, 3), (3, 0)],
    eps=eps_fold,
    V_pair=V_fold,
    E_J_val=E_J_fold,
    n_modes=N,
)

# --- (D) 4-cell open chain (boundary effects, no frustration) ---
result_4chain = analyze_topology(
    "4-cell open chain",
    n_cells=4,
    adjacency=[(0, 1), (1, 2), (2, 3)],
    eps=eps_fold,
    V_pair=V_fold,
    E_J_val=E_J_fold,
    n_modes=N,
)

# --- (E) 3-cell open chain (no frustration, 3 cells for comparison) ---
result_3chain = analyze_topology(
    "3-cell open chain",
    n_cells=3,
    adjacency=[(0, 1), (1, 2)],
    eps=eps_fold,
    V_pair=V_fold,
    E_J_val=E_J_fold,
    n_modes=N,
)

all_results = {
    '2cell': result_2cell,
    '3ring': result_3ring,
    '4ring': result_4ring,
    '4chain': result_4chain,
    '3chain': result_3chain,
}


# ============================================================================
# SECTION 4: J-DEPENDENCE SWEEP (FRUSTRATION VS UNFRUSTRATED)
# ============================================================================
print("\n" + "=" * 78)
print("Section 4: J-dependence sweep")
print("=" * 78)

N_J_sweep = 15
J_ratios = np.linspace(0.0, 2.5, N_J_sweep)
J_values = J_ratios * E_J_fold

K_sweep_3ring = np.zeros(N_J_sweep)
K_sweep_3chain = np.zeros(N_J_sweep)
K_sweep_2cell = np.zeros(N_J_sweep)

for i_j, J_val in enumerate(J_values):
    # 3-cell ring (frustrated)
    basis_3, lookup_3, dim_3 = build_fock_basis(3 * N, 2)
    cell_b_3, cell_lu_3, dim_c_3 = build_cell_basis(N, 2)
    H_3r = build_multi_cell_hamiltonian(3, [(0, 1), (1, 2), (2, 0)],
                                         eps_fold, V_fold, J_val, N, basis_3, lookup_3)
    evals_3r, evecs_3r = eigh(H_3r)
    psi_3r = evecs_3r[:, 0]
    rho_3r = partial_trace_single_cell(psi_3r, 0, 3, N, basis_3, dim_3,
                                        cell_b_3, cell_lu_3)
    m_3r = compute_entanglement_measures(rho_3r)
    K_sweep_3ring[i_j] = m_3r['K']

    # 3-cell open chain (unfrustrated)
    H_3c = build_multi_cell_hamiltonian(3, [(0, 1), (1, 2)],
                                         eps_fold, V_fold, J_val, N, basis_3, lookup_3)
    evals_3c, evecs_3c = eigh(H_3c)
    psi_3c = evecs_3c[:, 0]
    # Measure at the CENTER cell (index 1) to avoid boundary effects
    rho_3c = partial_trace_single_cell(psi_3c, 1, 3, N, basis_3, dim_3,
                                        cell_b_3, cell_lu_3)
    m_3c = compute_entanglement_measures(rho_3c)
    K_sweep_3chain[i_j] = m_3c['K']

    # 2-cell chain
    basis_2, lookup_2, dim_2 = build_fock_basis(2 * N, 2)
    cell_b_2, cell_lu_2, dim_c_2 = build_cell_basis(N, 2)
    H_2 = build_multi_cell_hamiltonian(2, [(0, 1)],
                                        eps_fold, V_fold, J_val, N, basis_2, lookup_2)
    evals_2, evecs_2 = eigh(H_2)
    psi_2 = evecs_2[:, 0]
    rho_2 = partial_trace_single_cell(psi_2, 0, 2, N, basis_2, dim_2,
                                       cell_b_2, cell_lu_2)
    m_2 = compute_entanglement_measures(rho_2)
    K_sweep_2cell[i_j] = m_2['K']

    if i_j % 3 == 0 or abs(J_ratios[i_j] - 1.0) < 0.1:
        print(f"  J/J_fold = {J_ratios[i_j]:.2f}: K(3ring) = {K_sweep_3ring[i_j]:.4f}, "
              f"K(3chain_center) = {K_sweep_3chain[i_j]:.4f}, "
              f"K(2cell) = {K_sweep_2cell[i_j]:.4f}")


# ============================================================================
# SECTION 5: LIMITING CASE CROSS-CHECKS
# ============================================================================
print("\n" + "=" * 78)
print("Section 5: Limiting case cross-checks")
print("=" * 78)

# Cross-check 1: J = 0 => K = 1 (product state)
print(f"\n  Cross-check 1: J = 0")
print(f"    K(3ring, J=0)  = {K_sweep_3ring[0]:.6f} (should be 1.0)")
print(f"    K(3chain, J=0) = {K_sweep_3chain[0]:.6f} (should be 1.0)")
print(f"    K(2cell, J=0)  = {K_sweep_2cell[0]:.6f} (should be 1.0)")

# Cross-check 2: Large J => K -> 4 (maximally delocalized among n1=0,1,2 sectors)
# At N_pair=2, max K = dim_cell = 37, but for the pair delocalization limit
# the dominant contribution is the 3 n_1-sectors (0, 1, 2), so K <= 3 for equal
# sector weights... Actually the n1=1 sector has 8 sub-states, so the limiting
# K depends on the structure.
K_large_J_3ring = K_sweep_3ring[-1]
K_large_J_2cell = K_sweep_2cell[-1]
print(f"\n  Cross-check 2: Large J (J/J_fold = {J_ratios[-1]:.1f})")
print(f"    K(3ring)  = {K_large_J_3ring:.4f}")
print(f"    K(2cell)  = {K_large_J_2cell:.4f}")

# Cross-check 3: 2-cell vs S71
print(f"\n  Cross-check 3: 2-cell at physical J vs S71")
# Find the J_ratio closest to 1.0
idx_phys = np.argmin(np.abs(J_ratios - 1.0))
print(f"    K(2cell, J/J_fold={J_ratios[idx_phys]:.2f}) = {K_sweep_2cell[idx_phys]:.4f}")
print(f"    K(S71) = {K_isolated:.4f}")

# Cross-check 4: Cyclic symmetry of ring topologies
print(f"\n  Cross-check 4: Cyclic symmetry")
print(f"    3-ring cell-to-cell K spread = {result_3ring['K_std']:.2e}")
print(f"    4-ring cell-to-cell K spread = {result_4ring['K_std']:.2e}")


# ============================================================================
# SECTION 6: FRUSTRATION ANALYSIS
# ============================================================================
print("\n" + "=" * 78)
print("Section 6: Frustration analysis")
print("=" * 78)

K_frust = result_3ring['K_mean']
K_unfrust_3chain = result_3chain['K_mean']  # 3-cell open chain, average
K_unfrust_4ring = result_4ring['K_mean']   # 4-cell ring, average
K_unfrust_4chain = result_4chain['K_mean'] # 4-cell open chain, average

# For proper frustration comparison: 3-ring vs 3-chain (same cell count)
# Use center cell of chain to remove boundary effects
K_3chain_center = result_3chain['K_per_cell'][1]

print(f"\n  Schmidt numbers at physical J:")
print(f"    K(2-cell chain)            = {result_2cell['K_mean']:.4f}")
print(f"    K(3-cell ring, frustrated) = {K_frust:.4f}")
print(f"    K(3-cell chain, center)    = {K_3chain_center:.4f}")
print(f"    K(3-cell chain, average)   = {K_unfrust_3chain:.4f}")
print(f"    K(4-cell ring)             = {K_unfrust_4ring:.4f}")
print(f"    K(4-cell chain, average)   = {K_unfrust_4chain:.4f}")

# Frustration reduction
reduction_vs_isolated = K_frust / K_isolated
reduction_vs_3chain = K_frust / K_3chain_center
reduction_vs_4ring = K_frust / K_unfrust_4ring

print(f"\n  Frustration reduction ratios:")
print(f"    K(3ring)/K(2cell)          = {reduction_vs_isolated:.4f}")
print(f"    K(3ring)/K(3chain_center)  = {reduction_vs_3chain:.4f}")
print(f"    K(3ring)/K(4ring)          = {reduction_vs_4ring:.4f}")

# Decompose: multi-cell effect vs frustration effect
multi_cell_effect = K_3chain_center / K_isolated
frustration_effect = K_frust / K_3chain_center
print(f"\n  Effect decomposition:")
print(f"    Multi-cell effect (3chain_center/2cell) = {multi_cell_effect:.4f}")
print(f"    Frustration effect (3ring/3chain_center) = {frustration_effect:.4f}")
print(f"    Product = {multi_cell_effect * frustration_effect:.4f} (should match {reduction_vs_isolated:.4f})")

# Compare with S71 GGE entropy frustration reduction (48%)
S_vN_frust = result_3ring['S_mean']
S_vN_3chain_center = result_3chain['S_per_cell'][1]
S_vN_reduction = S_vN_frust / S_vN_3chain_center if S_vN_3chain_center > 0 else float('inf')
print(f"\n  Entanglement entropy comparison:")
print(f"    S_vN(3ring)          = {S_vN_frust:.6f} bits")
print(f"    S_vN(3chain_center)  = {S_vN_3chain_center:.6f} bits")
print(f"    S_vN ratio           = {S_vN_reduction:.4f}")
print(f"    S_GGE ratio (S71)    = {S_GGE_frust_s71/S_GGE_bare_s71:.4f} (48% reduction)")


# ============================================================================
# SECTION 7: ENTANGLEMENT SPECTRUM COMPARISON
# ============================================================================
print("\n" + "=" * 78)
print("Section 7: Entanglement spectrum comparison")
print("=" * 78)

for label, result in [('2-cell', result_2cell), ('3-ring', result_3ring),
                       ('3-chain', result_3chain), ('4-ring', result_4ring)]:
    print(f"\n  {label} entanglement spectrum (cell 0):")
    evals_c0 = result['results_per_cell'][0]['evals']
    n_nonzero = np.sum(evals_c0 > 1e-15)
    print(f"    Nonzero eigenvalues: {n_nonzero}")
    for i, ev in enumerate(evals_c0):
        if ev > 1e-15:
            print(f"      lambda_{i} = {ev:.10e}")
        if i > 10 and ev < 1e-15:
            break


# ============================================================================
# SECTION 8: GATE EVALUATION
# ============================================================================
print("\n" + "=" * 78)
print("Section 8: Gate evaluation")
print("=" * 78)

K_target = result_3ring['K_mean']

print(f"\n  Gate FRUSTRATION-SCHMIDT-72:")
print(f"    K(frustrated 3-cell ring) = {K_target:.4f}")
print(f"    K(isolated 2-cell, S71)   = {K_isolated:.4f}")

if K_target > 2.0:
    gate_verdict = "PASS"
    gate_detail = (f"PASS: K(frustrated) = {K_target:.4f} > 2.0. "
                   f"Entanglement significantly survives frustration. "
                   f"K_frust/K_isolated = {K_target/K_isolated:.4f}.")
elif K_target >= 1.5:
    gate_verdict = "INFO"
    gate_detail = (f"INFO: K(frustrated) = {K_target:.4f} in [1.5, 2.0]. "
                   f"Partial entanglement reduction. "
                   f"K_frust/K_isolated = {K_target/K_isolated:.4f}.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"FAIL: K(frustrated) = {K_target:.4f} < 1.5. "
                   f"Frustration destroys most entanglement. "
                   f"K_frust/K_isolated = {K_target/K_isolated:.4f}.")

print(f"\n  Verdict: {gate_verdict}")
print(f"  {gate_detail}")


# ============================================================================
# SECTION 9: PLOT
# ============================================================================
print("\n--- Section 9: Generate plot ---")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Schmidt number comparison across topologies
ax1 = axes[0]
topologies = ['2-cell\nchain', '3-cell\nring\n(frust.)', '3-cell\nchain', '4-cell\nring', '4-cell\nchain']
K_values = [result_2cell['K_mean'], result_3ring['K_mean'],
            result_3chain['K_mean'], result_4ring['K_mean'],
            result_4chain['K_mean']]
colors = ['steelblue', 'crimson', 'steelblue', 'steelblue', 'steelblue']
bars = ax1.bar(topologies, K_values, color=colors, alpha=0.8, edgecolor='black')
ax1.axhline(2.0, color='green', linestyle='--', alpha=0.7, label='PASS threshold (K=2)')
ax1.axhline(1.5, color='orange', linestyle=':', alpha=0.7, label='FAIL threshold (K=1.5)')
ax1.axhline(1.0, color='gray', linestyle=':', alpha=0.4, label='Product state (K=1)')
ax1.set_ylabel('Schmidt number K')
ax1.set_title('K by topology')
ax1.legend(fontsize=7, loc='upper right')
ax1.set_ylim(0, max(K_values) * 1.15)

# Panel 2: K vs J sweep
ax2 = axes[1]
ax2.plot(J_ratios, K_sweep_3ring, 'r-o', label='3-ring (frustrated)', markersize=4)
ax2.plot(J_ratios, K_sweep_3chain, 'b-s', label='3-chain center', markersize=4)
ax2.plot(J_ratios, K_sweep_2cell, 'g-^', label='2-cell', markersize=4)
ax2.axvline(1.0, color='gray', linestyle='--', alpha=0.5, label='Physical J')
ax2.axhline(2.0, color='green', linestyle='--', alpha=0.3)
ax2.axhline(1.0, color='gray', linestyle=':', alpha=0.3)
ax2.set_xlabel('$J / J_{\\mathrm{fold}}$')
ax2.set_ylabel('Schmidt number K')
ax2.set_title('K vs Josephson coupling')
ax2.legend(fontsize=7)

# Panel 3: Entanglement spectrum comparison
ax3 = axes[2]
for label, result, color, marker in [
    ('2-cell', result_2cell, 'steelblue', 'o'),
    ('3-ring', result_3ring, 'crimson', 's'),
    ('3-chain', result_3chain, 'forestgreen', '^'),
    ('4-ring', result_4ring, 'darkorange', 'D'),
]:
    evals_c0 = result['results_per_cell'][0]['evals']
    nonzero = evals_c0[evals_c0 > 1e-15]
    ax3.semilogy(range(len(nonzero)), np.sort(nonzero)[::-1],
                 f'{marker}-', color=color, label=label, markersize=4, alpha=0.8)

ax3.set_xlabel('Eigenvalue index')
ax3.set_ylabel('$\\lambda_i$ (Schmidt coefficients)')
ax3.set_title('Entanglement spectrum (cell 0)')
ax3.legend(fontsize=7)

plt.tight_layout()
fig.savefig(os.path.join(SCRIPT_DIR, 's72_frustration_schmidt.png'), dpi=150)
print(f"  Plot saved: s72_frustration_schmidt.png")


# ============================================================================
# SECTION 10: SAVE DATA
# ============================================================================
print("\n--- Section 10: Save data ---")

elapsed = time.time() - t0

np.savez(
    os.path.join(SCRIPT_DIR, 's72_frustration_schmidt.npz'),
    # Gate
    gate_name='FRUSTRATION-SCHMIDT-72',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Primary result
    K_frustrated=result_3ring['K_mean'],
    K_isolated=K_isolated,
    K_ratio=K_target / K_isolated,
    # Per-topology Schmidt numbers
    K_2cell=result_2cell['K_mean'],
    K_3ring=result_3ring['K_mean'],
    K_3chain_mean=result_3chain['K_mean'],
    K_3chain_center=K_3chain_center,
    K_4ring=result_4ring['K_mean'],
    K_4chain=result_4chain['K_mean'],
    # Per-topology entropies
    S_vN_2cell=result_2cell['S_mean'],
    S_vN_3ring=result_3ring['S_mean'],
    S_vN_3chain=result_3chain['S_mean'],
    S_vN_4ring=result_4ring['S_mean'],
    S_vN_4chain=result_4chain['S_mean'],
    # Per-topology ground state energies and gaps
    E_GS_2cell=result_2cell['E_GS'],
    E_GS_3ring=result_3ring['E_GS'],
    E_GS_3chain=result_3chain['E_GS'],
    E_GS_4ring=result_4ring['E_GS'],
    E_GS_4chain=result_4chain['E_GS'],
    gap_2cell=result_2cell['gap'],
    gap_3ring=result_3ring['gap'],
    gap_3chain=result_3chain['gap'],
    gap_4ring=result_4ring['gap'],
    gap_4chain=result_4chain['gap'],
    # Per-cell Schmidt arrays
    K_per_cell_2cell=result_2cell['K_per_cell'],
    K_per_cell_3ring=result_3ring['K_per_cell'],
    K_per_cell_3chain=result_3chain['K_per_cell'],
    K_per_cell_4ring=result_4ring['K_per_cell'],
    K_per_cell_4chain=result_4chain['K_per_cell'],
    # Entanglement spectra (cell 0)
    ent_spec_2cell=result_2cell['results_per_cell'][0]['evals'],
    ent_spec_3ring=result_3ring['results_per_cell'][0]['evals'],
    ent_spec_3chain=result_3chain['results_per_cell'][0]['evals'],
    ent_spec_4ring=result_4ring['results_per_cell'][0]['evals'],
    ent_spec_4chain=result_4chain['results_per_cell'][0]['evals'],
    # J-sweep data
    J_ratios=J_ratios,
    J_values=J_values,
    K_sweep_3ring=K_sweep_3ring,
    K_sweep_3chain=K_sweep_3chain,
    K_sweep_2cell=K_sweep_2cell,
    # Effect decomposition
    multi_cell_effect=multi_cell_effect,
    frustration_effect=frustration_effect,
    # S71 comparison
    S_GGE_frust_s71=S_GGE_frust_s71,
    S_GGE_bare_s71=S_GGE_bare_s71,
    # Hilbert space dimensions
    dim_2cell=result_2cell['dim'],
    dim_3ring=result_3ring['dim'],
    dim_4ring=result_4ring['dim'],
    dim_4chain=result_4chain['dim'],
    dim_3chain=result_3chain['dim'],
    # Metadata
    E_J_fold=E_J_fold,
    N_modes=N,
    elapsed_s=elapsed,
)

print(f"  Data saved: s72_frustration_schmidt.npz")
print(f"\n  Total elapsed: {elapsed:.1f} s")


# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY: FRUSTRATION-SCHMIDT-72")
print("=" * 78)
print(f"  K(2-cell, isolated)         = {result_2cell['K_mean']:.4f}")
print(f"  K(3-ring, frustrated)       = {result_3ring['K_mean']:.4f}  <-- TARGET")
print(f"  K(3-chain, center)          = {K_3chain_center:.4f}")
print(f"  K(4-ring, unfrustrated)     = {result_4ring['K_mean']:.4f}")
print(f"  K(4-chain, average)         = {result_4chain['K_mean']:.4f}")
print(f"\n  Frustration reduction: K_frust/K_iso = {K_target/K_isolated:.4f}")
print(f"  Multi-cell effect:    {multi_cell_effect:.4f}")
print(f"  Frustration effect:   {frustration_effect:.4f}")
print(f"\n  Gate: FRUSTRATION-SCHMIDT-72 = {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 78)
