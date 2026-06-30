#!/usr/bin/env python3
"""
RICHARDSON-GAUDIN-N2-63: Multi-Pair Integrability on CG(24) Sub-Lattices
=========================================================================

Gate: RICHARDSON-GAUDIN-N2-63 | W6-08 | CC-PATH
  PASS: P(s) matches Wigner-Dyson (integrability broken at N_pair = 2)
  FAIL: P(s) remains Poisson (integrability persists)

Physics:
  The Richardson-Gaudin model is exactly integrable for separable pairing.
  At N_pair = 1, there are no pair-pair interactions — the system is trivially
  integrable (Poisson level statistics). At N_pair = 2, pair-pair interactions
  (Pauli blocking + non-separable pairing vertex) may break integrability.

  S55 showed a 2-sigma hint of integrability breaking at N_pair = 2 on a
  single cell. S58 extended to 2 cells. This computation tests N_pair = 2
  on both 2-cell and 4-cell sub-lattices of CG(24) with the physical
  Josephson coupling E_J = 7.042 M_KK.

  The test quantity is the nearest-neighbour spacing ratio <r> (Oganesyan-Huse):
    Poisson (integrable):  <r> ~ 0.386
    GOE (Wigner-Dyson):    <r> ~ 0.530
    GUE:                   <r> ~ 0.603

  We also compute the full P(s) distribution and the Brody parameter eta:
    P(s) = (1+eta) * a * s^eta * exp(-a * s^{1+eta})
    eta = 0: Poisson.  eta = 1: Wigner-Dyson (GOE).  # (local)

  Symmetry resolution is mandatory: level repulsion is sector-wise.
  - 2-cell: Z_2 exchange symmetry
  - 4-cell: depends on sub-lattice geometry (chain vs tetrahedron)
  Both sub-lattices are embedded in CG(24) via its adjacency structure.

Method:
  1. Load CG(24) adjacency and single-cell BCS data
  2. Extract 2-cell and 4-cell sub-lattices from CG(24)
  3. For each sub-lattice:
     a. Build pair Fock space: C(N_modes * N_cells, N_pair) states
     b. Construct BCS + Josephson Hamiltonian
     c. Resolve by discrete symmetries
     d. Compute <r> and P(s) in each symmetry sector
     e. Fit Brody parameter
  4. Compare against Poisson and GOE references
  5. Gate verdict

References:
  - Oganesyan & Huse, PRB 75, 155111 (2007): r-statistic
  - Brody, Lett. Nuovo Cim. 7, 482 (1973): Brody distribution
  - Paper 15 (Dukelsky et al. 2004): Richardson-Gaudin colloquium
  - S55 s55_npair2_ed.py: 2-sigma hint at N=2
  - S58 s58_npair2_integ.py: 2-cell Z_2-resolved analysis

Session: S63 W6-08
Agent: landau-condensed-matter-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
from scipy.optimize import curve_fit, minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_0_GL, Delta_0_OES, xi_BCS, S_inst,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, T_acoustic,
    hbar_GeV_s, t_Planck, t_universe_s
)

data_dir = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

print("=" * 70)
print("RICHARDSON-GAUDIN-N2-63: Multi-Pair Integrability on CG(24)")
print("=" * 70)

# CG(24) adjacency
cg24_data = np.load(os.path.join(data_dir, 's60_entangle_cg24.npz'), allow_pickle=True)
adj_cg24 = cg24_data['adj'].astype(float)
N_vertices_cg24 = int(cg24_data['N_vertices'])  # 24
degree_cg24 = int(cg24_data['degree'])           # 6

# Single-cell BCS data from S52 HFB
hfb_data = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction
labels = hfb_data['labels']            # mode labels

# S56 GGE fabric data (for cross-check)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']
V_fold = d56['V_fold']

# Josephson coupling: E_J = 7.042 M_KK (task specification)
E_J = 7.042  # M_KK  # (local)

N_modes = len(eps_bare)  # 8
N_pair = 2  # (local)

print(f"CG(24): {N_vertices_cg24} vertices, degree {degree_cg24}")
print(f"N_modes/cell = {N_modes}, N_pair = {N_pair}")
print(f"E_J = {E_J:.3f} M_KK")
print(f"eps_bare = {eps_bare}")
print(f"labels = {list(labels)}")
print()

# Cross-check V matrices
V_diff = np.max(np.abs(V_fold - V_bare))
print(f"V_fold vs V_bare max diff = {V_diff:.2e}")
assert V_diff < 1e-8, f"V matrices disagree by {V_diff}"

# =====================================================================
#  2. SUB-LATTICE EXTRACTION FROM CG(24)
# =====================================================================

print("\n" + "=" * 70)
print("SUB-LATTICE EXTRACTION")
print("=" * 70)

# 2-cell sub-lattice: pick two adjacent vertices of CG(24)
# Any edge in CG(24) gives a 2-cell sub-lattice.
# Find the first edge.
edge_2cell = None
for i in range(N_vertices_cg24):
    for j in range(i+1, N_vertices_cg24):
        if adj_cg24[i, j] > 0.5:
            edge_2cell = (i, j)
            break
    if edge_2cell is not None:
        break

print(f"2-cell sub-lattice: vertices {edge_2cell}")
adj_2cell = np.array([[0, 1], [1, 0]], dtype=float)

# 4-cell sub-lattice: pick a connected 4-vertex subgraph of CG(24).
# Strategy: start from a vertex, take its first 3 neighbours -> star topology.
# Or find a 4-clique (complete subgraph K_4) if it exists.
# CG(24) is the 1-skeleton of the 24-cell. It has cliques of various sizes.

# Method: find a K_4 (4-clique) first. If not, use a path or star.
def find_cliques(adj, size):
    """Find all cliques of given size in adjacency matrix."""
    n = adj.shape[0]
    cliques = []
    for combo in combinations(range(n), size):
        is_clique = True
        for a, b in combinations(combo, 2):
            if adj[a, b] < 0.5:
                is_clique = False
                break
        if is_clique:
            cliques.append(combo)
    return cliques

cliques_4 = find_cliques(adj_cg24, 4)
print(f"Number of K_4 cliques in CG(24): {len(cliques_4)}")

if len(cliques_4) > 0:
    verts_4cell = list(cliques_4[0])
    adj_4cell = np.zeros((4, 4), dtype=float)
    for i in range(4):
        for j in range(4):
            if i != j:
                adj_4cell[i, j] = adj_cg24[verts_4cell[i], verts_4cell[j]]
    topo_4cell = "K4_clique"
    print(f"4-cell sub-lattice: K_4 clique at vertices {verts_4cell}")
else:
    # Fallback: connected path
    v0 = edge_2cell[0]
    neighbours = np.where(adj_cg24[v0] > 0.5)[0]
    v1 = neighbours[0]
    neighbours_v1 = np.where(adj_cg24[v1] > 0.5)[0]
    v2 = [v for v in neighbours_v1 if v != v0][0]
    neighbours_v2 = np.where(adj_cg24[v2] > 0.5)[0]
    v3 = [v for v in neighbours_v2 if v not in (v0, v1)][0]
    verts_4cell = [v0, v1, v2, v3]
    adj_4cell = np.zeros((4, 4), dtype=float)
    for i in range(4):
        for j in range(4):
            if i != j:
                adj_4cell[i, j] = adj_cg24[verts_4cell[i], verts_4cell[j]]
    topo_4cell = "path"
    print(f"4-cell sub-lattice: path at vertices {verts_4cell}")

print(f"4-cell adjacency:\n{adj_4cell}")
n_bonds_4 = int(np.sum(adj_4cell) / 2)
print(f"4-cell bonds: {n_bonds_4}")

# =====================================================================
#  3. PAIR FOCK SPACE CONSTRUCTION
# =====================================================================

def build_pair_fock_space(n_cells, n_modes, n_pair):
    """Build the pair Fock space for n_pair pairs on n_cells * n_modes slots."""
    n_slots = n_cells * n_modes
    dim = mcomb(n_slots, n_pair)
    basis = list(combinations(range(n_slots), n_pair))
    assert len(basis) == dim

    # Map slot -> (mode, cell)
    def slot_to_mc(s):
        return (s % n_modes, s // n_modes)

    state_info = []
    for b in basis:
        state_info.append(tuple(slot_to_mc(s) for s in b))

    state_index = {s: i for i, s in enumerate(basis)}

    return basis, state_info, state_index, dim, n_slots


# =====================================================================
#  4. HAMILTONIAN CONSTRUCTION
# =====================================================================

def build_H_BCS_multi_cell(eps, V, E_J_val, adj, n_cells, n_modes, n_pair,
                           basis, state_info, state_index, dim):
    """
    Build the BCS + Josephson Hamiltonian for N_pair pairs on a multi-cell system.

    H = H_kinetic + H_pairing + H_Josephson

    H_kinetic: Sum over occupied pair-slots of 2*eps[mode]
    H_pairing: Intra-cell pair scattering V[k,l] P_k^dag P_l
    H_Josephson: -(E_J/2) * Sum_{<ij>} (B_i^dag B_j + h.c.)
                 where B_i = Sum_k b_{k,i} is the collective pair operator
                 on cell i. This tunnels a pair from any mode in cell i to
                 any mode in cell j, for each bond <ij> in the adjacency.
    """
    H = np.zeros((dim, dim), dtype=np.float64)

    for i_state in range(dim):
        slots_i = basis[i_state]

        # --- Diagonal: kinetic + pairing diagonal ---
        for s in slots_i:
            m = s % n_modes
            H[i_state, i_state] += 2.0 * eps[m]

        # Pairing diagonal: V[m,m] for each occupied mode in each cell
        # (self-interaction of the pair)
        for s in slots_i:
            m = s % n_modes
            H[i_state, i_state] -= V[m, m]

        # Density-density between pairs in the same cell
        # If two pairs occupy modes k, l in the same cell: V[k,l] contribution
        for a_idx in range(n_pair):
            for b_idx in range(a_idx + 1, n_pair):
                s_a = slots_i[a_idx]
                s_b = slots_i[b_idx]
                m_a, c_a = s_a % n_modes, s_a // n_modes
                m_b, c_b = s_b % n_modes, s_b // n_modes
                if c_a == c_b:
                    # Same cell: density-density interaction
                    H[i_state, i_state] += V[m_a, m_b]

        # --- Off-diagonal: intra-cell pair scattering ---
        for p_idx in range(n_pair):
            s_p = slots_i[p_idx]
            m_p = s_p % n_modes
            c_p = s_p // n_modes

            other_slots = list(slots_i[:p_idx]) + list(slots_i[p_idx+1:])

            # Scatter pair p: mode m_p -> mode k in same cell c_p
            for k in range(n_modes):
                if k == m_p:
                    continue
                new_slot = c_p * n_modes + k
                if new_slot in other_slots:
                    continue  # Pauli blocked
                new_state = tuple(sorted(other_slots + [new_slot]))
                if new_state in state_index:
                    j_state = state_index[new_state]
                    H[j_state, i_state] -= V[k, m_p]

            # --- Josephson tunneling: pair p -> any mode in adjacent cell ---
            for c_target in range(n_cells):
                if adj[c_p, c_target] < 0.5:
                    continue  # Not connected
                for l in range(n_modes):
                    new_slot = c_target * n_modes + l
                    if new_slot == s_p:
                        continue  # Same slot
                    if new_slot in other_slots:
                        continue  # Pauli blocked
                    new_state = tuple(sorted(other_slots + [new_slot]))
                    if new_state in state_index:
                        j_state = state_index[new_state]
                        H[j_state, i_state] += -E_J_val / 2.0

    # Symmetrize
    H = 0.5 * (H + H.T)

    return H


# =====================================================================
#  5. LEVEL STATISTICS
# =====================================================================

def level_spacing_ratio(eigenvalues, unfold=True):
    """
    Compute the mean adjacent gap ratio <r> for a spectrum.
    Returns <r>, array of individual r_n values, and unfolded spacings.
    """
    E = np.sort(eigenvalues)

    if unfold:
        N = np.arange(1, len(E) + 1)
        deg = min(5, len(E) - 2)
        if deg < 1:
            deg = 1  # (local)
        poly = np.polyfit(E, N, deg=deg)
        E_unf = np.polyval(poly, E)
    else:
        E_unf = E

    s = np.diff(E_unf)
    s = s[s > 1e-14]

    if len(s) < 3:
        return np.nan, np.array([]), np.array([])

    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])

    return np.mean(r_n), r_n, s


def brody_pdf(s, eta):
    """Brody distribution P(s; eta) = (1+eta)*a*s^eta*exp(-a*s^{1+eta})."""
    from scipy.special import gamma as gamma_fn
    a = (gamma_fn((eta + 2) / (eta + 1)))**(1 + eta)
    return (1 + eta) * a * s**eta * np.exp(-a * s**(1 + eta))


def fit_brody(spacings):
    """Fit the Brody parameter eta to an array of spacings."""
    if len(spacings) < 5:
        return np.nan, np.nan

    # Normalize spacings to mean = 1
    s = spacings / np.mean(spacings)
    s = s[s > 1e-14]

    # Method: MLE via minimizing negative log-likelihood
    from scipy.special import gamma as gamma_fn

    def neg_log_lik(eta_val):
        eta_val = eta_val[0] if hasattr(eta_val, '__len__') else eta_val
        if eta_val < 0 or eta_val > 2:
            return 1e10
        a = (gamma_fn((eta_val + 2) / (eta_val + 1)))**(1 + eta_val)
        ll = np.sum(np.log(1 + eta_val) + np.log(a) + eta_val * np.log(s + 1e-30)
                     - a * s**(1 + eta_val))
        return -ll

    result = minimize_scalar(neg_log_lik, bounds=(0.0, 1.5), method='bounded')
    eta_fit = result.x
    # Bootstrap error
    n_boot = 200
    eta_boots = []
    for _ in range(n_boot):
        idx = np.random.choice(len(s), size=len(s), replace=True)
        s_boot = s[idx]

        def neg_ll_boot(eta_val):
            if eta_val < 0 or eta_val > 2:
                return 1e10
            a = (gamma_fn((eta_val + 2) / (eta_val + 1)))**(1 + eta_val)
            ll = np.sum(np.log(1 + eta_val) + np.log(a) + eta_val * np.log(s_boot + 1e-30)
                         - a * s_boot**(1 + eta_val))
            return -ll

        r = minimize_scalar(neg_ll_boot, bounds=(0.0, 1.5), method='bounded')
        eta_boots.append(r.x)

    eta_err = np.std(eta_boots)
    return eta_fit, eta_err


# =====================================================================
#  6. SYMMETRY OPERATORS
# =====================================================================

def build_exchange_operator(basis, state_index, n_modes, cell_a, cell_b, dim):
    """Build the Z_2 operator that exchanges cell_a <-> cell_b."""
    P = np.zeros((dim, dim), dtype=np.float64)
    for i, slots in enumerate(basis):
        new_slots = []
        for s in slots:
            m = s % n_modes
            c = s // n_modes
            if c == cell_a:
                new_slots.append(cell_b * n_modes + m)
            elif c == cell_b:
                new_slots.append(cell_a * n_modes + m)
            else:
                new_slots.append(s)
        new_state = tuple(sorted(new_slots))
        if new_state in state_index:
            j = state_index[new_state]
            P[j, i] = 1.0
    return P


def project_to_sector(H, projector_evecs, mask):
    """Project Hamiltonian into a symmetry sector."""
    Q = projector_evecs[:, mask]
    H_sector = Q.T @ H @ Q
    return H_sector, Q


# =====================================================================
#  7. REFERENCE DISTRIBUTIONS (Finite-size Poisson and GOE)
# =====================================================================

print("\n" + "=" * 70)
print("FINITE-SIZE REFERENCE DISTRIBUTIONS")
print("=" * 70)

np.random.seed(42)
N_MC = 5000  # (local)

def mc_reference(dim_ref, N_MC_ref):
    """Generate MC reference for Poisson and GOE <r> at given dimension."""
    r_poi = []
    r_goe = []
    for _ in range(N_MC_ref):
        E_rand = np.sort(np.random.uniform(0, 10, dim_ref))
        r_val, _, _ = level_spacing_ratio(E_rand, unfold=False)
        r_poi.append(r_val)

        M = np.random.randn(dim_ref, dim_ref)
        M = (M + M.T) / 2
        E_goe = np.linalg.eigvalsh(M)
        r_val, _, _ = level_spacing_ratio(E_goe, unfold=False)
        r_goe.append(r_val)

    return np.mean(r_poi), np.std(r_poi), np.mean(r_goe), np.std(r_goe)


# =====================================================================
#  8. MAIN COMPUTATION: 2-CELL SUB-LATTICE
# =====================================================================

print("\n" + "=" * 70)
print("2-CELL SUB-LATTICE: N_pair = 2")
print("=" * 70)

N_cells_2 = 2
basis_2, sinfo_2, sidx_2, dim_2, nslots_2 = build_pair_fock_space(N_cells_2, N_modes, N_pair)
print(f"Fock space: C({nslots_2}, {N_pair}) = {dim_2} states")

# Build Hamiltonian
print("Building Hamiltonian...")
H_2cell = build_H_BCS_multi_cell(eps_fold, V_fold, E_J, adj_2cell,
                                  N_cells_2, N_modes, N_pair,
                                  basis_2, sinfo_2, sidx_2, dim_2)

# Hermiticity check
herm_check_2 = np.max(np.abs(H_2cell - H_2cell.T))
print(f"Hermiticity: max|H - H^T| = {herm_check_2:.2e}")
assert herm_check_2 < 1e-12

# Also build integrable control (E_J = 0)
H_2cell_noJ = build_H_BCS_multi_cell(eps_fold, V_fold, 0.0, adj_2cell,
                                      N_cells_2, N_modes, N_pair,
                                      basis_2, sinfo_2, sidx_2, dim_2)

# Diagonalize
print("Diagonalizing...")
evals_2cell, evecs_2cell = eigh(H_2cell)
evals_2cell_noJ, evecs_2cell_noJ = eigh(H_2cell_noJ)

print(f"E_GS(2-cell, E_J={E_J:.3f}) = {evals_2cell[0]:.8f} M_KK")
print(f"E_GS(2-cell, E_J=0) = {evals_2cell_noJ[0]:.8f} M_KK")
print(f"Spectrum: [{evals_2cell[0]:.4f}, {evals_2cell[-1]:.4f}]")

# --- Z_2 symmetry resolution ---
print("\n--- Z_2 Symmetry Resolution ---")
P_z2 = build_exchange_operator(basis_2, sidx_2, N_modes, 0, 1, dim_2)

# Verify P^2 = I
p2_check = np.max(np.abs(P_z2 @ P_z2 - np.eye(dim_2)))
print(f"P^2 = I check: {p2_check:.2e}")

# Verify [H, P] = 0
comm_hp = np.max(np.abs(H_2cell @ P_z2 - P_z2 @ H_2cell))
print(f"[H, P] = 0 check: {comm_hp:.2e}")

# Decompose into even/odd sectors
P_evals, P_evecs = eigh(P_z2)
even_mask = P_evals > 0.5
odd_mask = P_evals < -0.5
n_even_2 = np.sum(even_mask)
n_odd_2 = np.sum(odd_mask)
print(f"Even sector: {n_even_2} states, Odd sector: {n_odd_2} states")

H_even_2, Q_even_2 = project_to_sector(H_2cell, P_evecs, even_mask)
H_odd_2, Q_odd_2 = project_to_sector(H_2cell, P_evecs, odd_mask)

evals_even_2 = np.linalg.eigvalsh(H_even_2)
evals_odd_2 = np.linalg.eigvalsh(H_odd_2)

# Level statistics in each sector
r_even_2, r_dist_even_2, s_even_2 = level_spacing_ratio(evals_even_2)
r_odd_2, r_dist_odd_2, s_odd_2 = level_spacing_ratio(evals_odd_2)

# Unsectorized (for comparison)
r_full_2, r_dist_full_2, s_full_2 = level_spacing_ratio(evals_2cell)
r_noJ_2, _, _ = level_spacing_ratio(evals_2cell_noJ)

# Weighted sector average
n_r_even = len(r_dist_even_2) if len(r_dist_even_2) > 0 else 0
n_r_odd = len(r_dist_odd_2) if len(r_dist_odd_2) > 0 else 0
if n_r_even + n_r_odd > 0:
    r_combined_2 = (n_r_even * r_even_2 + n_r_odd * r_odd_2) / (n_r_even + n_r_odd)
else:
    r_combined_2 = np.nan

# Also do no-J control with Z_2 resolution
H_even_2_noJ, _ = project_to_sector(H_2cell_noJ, P_evecs, even_mask)
H_odd_2_noJ, _ = project_to_sector(H_2cell_noJ, P_evecs, odd_mask)
evals_even_2_noJ = np.linalg.eigvalsh(H_even_2_noJ)
evals_odd_2_noJ = np.linalg.eigvalsh(H_odd_2_noJ)
r_even_2_noJ, _, _ = level_spacing_ratio(evals_even_2_noJ)
r_odd_2_noJ, _, _ = level_spacing_ratio(evals_odd_2_noJ)

# Standard errors
r_se_even_2 = np.std(r_dist_even_2) / np.sqrt(len(r_dist_even_2)) if len(r_dist_even_2) > 1 else np.nan
r_se_odd_2 = np.std(r_dist_odd_2) / np.sqrt(len(r_dist_odd_2)) if len(r_dist_odd_2) > 1 else np.nan

# Brody parameter
eta_even_2, eta_err_even_2 = fit_brody(s_even_2) if len(s_even_2) > 5 else (np.nan, np.nan)
eta_odd_2, eta_err_odd_2 = fit_brody(s_odd_2) if len(s_odd_2) > 5 else (np.nan, np.nan)

# MC references at sector dimensions
r_poi_even, sig_poi_even, r_goe_even, sig_goe_even = mc_reference(n_even_2, N_MC)
r_poi_odd, sig_poi_odd, r_goe_odd, sig_goe_odd = mc_reference(n_odd_2, N_MC)

print(f"\n--- 2-Cell Results ---")
print(f"{'':12s} {'<r>':>8s} {'SE':>8s} {'eta':>8s} {'eta_err':>8s}")
print(f"{'Even':12s} {r_even_2:8.4f} {r_se_even_2:8.4f} {eta_even_2:8.4f} {eta_err_even_2:8.4f}")
print(f"{'Odd':12s} {r_odd_2:8.4f} {r_se_odd_2:8.4f} {eta_odd_2:8.4f} {eta_err_odd_2:8.4f}")
print(f"{'Combined':12s} {r_combined_2:8.4f}")
print(f"{'Full(unsec)':12s} {r_full_2:8.4f}")
print(f"{'No-J even':12s} {r_even_2_noJ:8.4f}")
print(f"{'No-J odd':12s} {r_odd_2_noJ:8.4f}")
print(f"{'Control E_J=0':12s} {r_noJ_2:8.4f}")
print(f"\nFinite-size references (even sector, dim={n_even_2}):")
print(f"  Poisson: {r_poi_even:.4f} +/- {sig_poi_even:.4f}")
print(f"  GOE:     {r_goe_even:.4f} +/- {sig_goe_even:.4f}")
print(f"Finite-size references (odd sector, dim={n_odd_2}):")
print(f"  Poisson: {r_poi_odd:.4f} +/- {sig_poi_odd:.4f}")
print(f"  GOE:     {r_goe_odd:.4f} +/- {sig_goe_odd:.4f}")

# Sigma from Poisson (using sector-resolved MC)
sigma_from_poi_even = (r_even_2 - r_poi_even) / sig_poi_even if sig_poi_even > 0 else np.nan
sigma_from_poi_odd = (r_odd_2 - r_poi_odd) / sig_poi_odd if sig_poi_odd > 0 else np.nan
print(f"\nSigma from Poisson:")
print(f"  Even: {sigma_from_poi_even:+.2f} sigma")
print(f"  Odd:  {sigma_from_poi_odd:+.2f} sigma")


# =====================================================================
#  9. MAIN COMPUTATION: 4-CELL SUB-LATTICE
# =====================================================================

print("\n" + "=" * 70)
print("4-CELL SUB-LATTICE: N_pair = 2")
print("=" * 70)

N_cells_4 = 4
basis_4, sinfo_4, sidx_4, dim_4, nslots_4 = build_pair_fock_space(N_cells_4, N_modes, N_pair)
print(f"Fock space: C({nslots_4}, {N_pair}) = {dim_4} states")
print(f"Topology: {topo_4cell}")
print(f"4-cell adjacency bonds: {n_bonds_4}")

# Build Hamiltonian
print("Building Hamiltonian...")
H_4cell = build_H_BCS_multi_cell(eps_fold, V_fold, E_J, adj_4cell,
                                  N_cells_4, N_modes, N_pair,
                                  basis_4, sinfo_4, sidx_4, dim_4)

herm_check_4 = np.max(np.abs(H_4cell - H_4cell.T))
print(f"Hermiticity: max|H - H^T| = {herm_check_4:.2e}")
assert herm_check_4 < 1e-12

# Control: E_J = 0
H_4cell_noJ = build_H_BCS_multi_cell(eps_fold, V_fold, 0.0, adj_4cell,
                                      N_cells_4, N_modes, N_pair,
                                      basis_4, sinfo_4, sidx_4, dim_4)

# Diagonalize
print("Diagonalizing...")
evals_4cell, evecs_4cell = eigh(H_4cell)
evals_4cell_noJ, evecs_4cell_noJ = eigh(H_4cell_noJ)

print(f"E_GS(4-cell, E_J={E_J:.3f}) = {evals_4cell[0]:.8f} M_KK")
print(f"E_GS(4-cell, E_J=0) = {evals_4cell_noJ[0]:.8f} M_KK")
print(f"Spectrum: [{evals_4cell[0]:.4f}, {evals_4cell[-1]:.4f}]")

# --- Symmetry resolution for 4-cell ---
# If K_4 clique: the symmetry group is S_4 (24 elements).
# However, pair permutation is part of this. For tractability, we
# resolve by available Z_2 symmetries (pairwise cell exchanges).
# The key requirement: resolve ALL symmetries that commute with H.

# For K_4: exchange (0<->1), (0<->2), (0<->3) generate S_4.
# For a chain: only (0<->3)&(1<->2) inversion symmetry.

print("\n--- Symmetry Resolution (4-cell) ---")

if topo_4cell == "K4_clique":
    # In K_4, all cells are equivalent. S_4 symmetry.
    # For tractable resolution, use Z_2 x Z_2 subgroup:
    # P_01: swap cells 0<->1,  P_23: swap cells 2<->3
    P_01 = build_exchange_operator(basis_4, sidx_4, N_modes, 0, 1, dim_4)
    P_23 = build_exchange_operator(basis_4, sidx_4, N_modes, 2, 3, dim_4)

    # Verify they commute with H and with each other
    comm_01 = np.max(np.abs(H_4cell @ P_01 - P_01 @ H_4cell))
    comm_23 = np.max(np.abs(H_4cell @ P_23 - P_23 @ H_4cell))
    comm_cross = np.max(np.abs(P_01 @ P_23 - P_23 @ P_01))
    print(f"[H, P_01] = {comm_01:.2e}")
    print(f"[H, P_23] = {comm_23:.2e}")
    print(f"[P_01, P_23] = {comm_cross:.2e}")

    if comm_01 < 1e-10 and comm_23 < 1e-10:
        # Simultaneous diagonalization: first project by P_01, then by P_23
        P01_evals, P01_evecs = eigh(P_01)
        even_01 = P01_evals > 0.5
        odd_01 = P01_evals < -0.5

        sectors_4 = {}
        for label_01, mask_01 in [("e01", even_01), ("o01", odd_01)]:
            Q1 = P01_evecs[:, mask_01]
            H_sub = Q1.T @ H_4cell @ Q1
            P23_sub = Q1.T @ P_23 @ Q1
            P23_evals, P23_evecs = eigh(P23_sub)
            even_23 = P23_evals > 0.5
            odd_23 = P23_evals < -0.5
            for label_23, mask_23 in [("e23", even_23), ("o23", odd_23)]:
                Q2 = P23_evecs[:, mask_23]
                H_sec = Q2.T @ H_sub @ Q2
                evals_sec = np.linalg.eigvalsh(H_sec)
                sector_name = f"{label_01}_{label_23}"
                sectors_4[sector_name] = evals_sec
                print(f"  Sector {sector_name}: {len(evals_sec)} levels")
    else:
        # Fall back to unsectorized
        print("  Symmetries don't commute cleanly. Using full spectrum.")
        sectors_4 = {"full": evals_4cell}
else:
    # The 4-cell adjacency [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]] is a 4-cycle C_4.
    # Its automorphism group acting on cells is the Klein four-group Z_2 x Z_2:
    #   P_A: (0<->3, 1<->2) — the original "inversion"
    #   P_B: (0<->2, 1<->3) — the bipartite swap
    #   P_A * P_B: (0<->1, 2<->3) — the third Z_2
    # All three commute with H (they are graph automorphisms).
    # We MUST resolve BOTH to avoid spurious level crossings.

    def build_cell_permutation_op(cell_map, basis_loc, sidx_loc, n_modes_loc, dim_loc):
        """Build permutation operator from a cell mapping dict."""
        P = np.zeros((dim_loc, dim_loc), dtype=np.float64)
        for i, slots in enumerate(basis_loc):
            new_slots = []
            for s in slots:
                m = s % n_modes_loc
                c = s // n_modes_loc
                new_c = cell_map.get(c, c)
                new_slots.append(new_c * n_modes_loc + m)
            new_state = tuple(sorted(new_slots))
            if new_state in sidx_loc:
                j = sidx_loc[new_state]
                P[j, i] = 1.0
        return P

    # P_A: (0<->3, 1<->2)
    P_A = build_cell_permutation_op({0:3, 3:0, 1:2, 2:1}, basis_4, sidx_4, N_modes, dim_4)
    # P_B: (0<->2, 1<->3)
    P_B = build_cell_permutation_op({0:2, 2:0, 1:3, 3:1}, basis_4, sidx_4, N_modes, dim_4)

    # Verify symmetries
    comm_A = np.max(np.abs(H_4cell @ P_A - P_A @ H_4cell))
    comm_B = np.max(np.abs(H_4cell @ P_B - P_B @ H_4cell))
    comm_AB = np.max(np.abs(P_A @ P_B - P_B @ P_A))
    pa2_check = np.max(np.abs(P_A @ P_A - np.eye(dim_4)))
    pb2_check = np.max(np.abs(P_B @ P_B - np.eye(dim_4)))
    print(f"[H, P_A] = {comm_A:.2e}")
    print(f"[H, P_B] = {comm_B:.2e}")
    print(f"[P_A, P_B] = {comm_AB:.2e}")
    print(f"P_A^2 = I check: {pa2_check:.2e}")
    print(f"P_B^2 = I check: {pb2_check:.2e}")

    if comm_A < 1e-10 and comm_B < 1e-10 and comm_AB < 1e-10:
        # Z_2 x Z_2 resolution: 4 sectors (++, +-, -+, --)
        PA_evals, PA_evecs = eigh(P_A)
        even_A = PA_evals > 0.5
        odd_A = PA_evals < -0.5

        sectors_4 = {}
        for label_A, mask_A in [("eA", even_A), ("oA", odd_A)]:
            Q_A = PA_evecs[:, mask_A]
            H_sub_A = Q_A.T @ H_4cell @ Q_A
            PB_sub = Q_A.T @ P_B @ Q_A
            PB_evals, PB_evecs = eigh(PB_sub)
            even_B = PB_evals > 0.5
            odd_B = PB_evals < -0.5
            for label_B, mask_B in [("eB", even_B), ("oB", odd_B)]:
                Q_B = PB_evecs[:, mask_B]
                H_sec = Q_B.T @ H_sub_A @ Q_B
                evals_sec = np.linalg.eigvalsh(H_sec)
                sector_name = f"{label_A}_{label_B}"
                sectors_4[sector_name] = evals_sec
                print(f"  Sector {sector_name}: {len(evals_sec)} levels")
    elif comm_A < 1e-10:
        # Only P_A is a symmetry
        PA_evals, PA_evecs = eigh(P_A)
        even_A = PA_evals > 0.5
        odd_A = PA_evals < -0.5
        n_even_A = np.sum(even_A)
        n_odd_A = np.sum(odd_A)
        print(f"  P_A even: {n_even_A}, P_A odd: {n_odd_A}")
        H_even_A, _ = project_to_sector(H_4cell, PA_evecs, even_A)
        H_odd_A, _ = project_to_sector(H_4cell, PA_evecs, odd_A)
        sectors_4 = {
            "eA": np.linalg.eigvalsh(H_even_A),
            "oA": np.linalg.eigvalsh(H_odd_A)
        }
    else:
        sectors_4 = {"full": evals_4cell}

# Compute level statistics in each sector
results_4cell_sectors = {}
print(f"\n--- 4-Cell Sector Results ---")
print(f"{'Sector':15s} {'N':>5s} {'<r>':>8s} {'SE':>8s} {'eta':>8s} {'eta_err':>8s}")

all_r_4 = []
all_r_weights_4 = []

for sec_name, sec_evals in sectors_4.items():
    r_sec, r_dist_sec, s_sec = level_spacing_ratio(sec_evals)
    r_se_sec = np.std(r_dist_sec) / np.sqrt(len(r_dist_sec)) if len(r_dist_sec) > 1 else np.nan
    eta_sec, eta_err_sec = fit_brody(s_sec) if len(s_sec) > 5 else (np.nan, np.nan)
    results_4cell_sectors[sec_name] = {
        'evals': sec_evals,
        'r': r_sec,
        'r_se': r_se_sec,
        'r_dist': r_dist_sec,
        's': s_sec,
        'eta': eta_sec,
        'eta_err': eta_err_sec,
        'n_levels': len(sec_evals)
    }
    print(f"{sec_name:15s} {len(sec_evals):5d} {r_sec:8.4f} {r_se_sec:8.4f} {eta_sec:8.4f} {eta_err_sec:8.4f}")
    all_r_4.append(r_sec * len(r_dist_sec))
    all_r_weights_4.append(len(r_dist_sec))

if sum(all_r_weights_4) > 0:
    r_combined_4 = sum(all_r_4) / sum(all_r_weights_4)
else:
    r_combined_4 = np.nan

# Unsectorized for comparison
r_full_4, r_dist_full_4, _ = level_spacing_ratio(evals_4cell)
r_noJ_4, _, _ = level_spacing_ratio(evals_4cell_noJ)

print(f"\n{'Combined':15s} {'':>5s} {r_combined_4:8.4f}")
print(f"{'Full(unsec)':15s} {dim_4:5d} {r_full_4:8.4f}")
print(f"{'Control E_J=0':15s} {dim_4:5d} {r_noJ_4:8.4f}")

# MC references for the largest sector
max_sec_dim = max(len(v['evals']) for v in results_4cell_sectors.values())
r_poi_4, sig_poi_4, r_goe_4, sig_goe_4 = mc_reference(max_sec_dim, N_MC)
print(f"\nFinite-size references (largest sector, dim={max_sec_dim}):")
print(f"  Poisson: {r_poi_4:.4f} +/- {sig_poi_4:.4f}")
print(f"  GOE:     {r_goe_4:.4f} +/- {sig_goe_4:.4f}")


# =====================================================================
#  10. COMBINED P(s) ANALYSIS
# =====================================================================

print("\n" + "=" * 70)
print("P(s) DISTRIBUTION ANALYSIS")
print("=" * 70)

# Pool all sector-resolved spacings for each system
all_s_2cell = np.concatenate([s_even_2 / np.mean(s_even_2) if len(s_even_2) > 0 else np.array([]),
                               s_odd_2 / np.mean(s_odd_2) if len(s_odd_2) > 0 else np.array([])])

all_s_4cell = []
for sec_name, sec_res in results_4cell_sectors.items():
    s_sec = sec_res['s']
    if len(s_sec) > 0:
        all_s_4cell.append(s_sec / np.mean(s_sec))
all_s_4cell = np.concatenate(all_s_4cell) if len(all_s_4cell) > 0 else np.array([])

# Overall Brody fits
eta_2cell_pooled, eta_err_2cell_pooled = fit_brody(all_s_2cell) if len(all_s_2cell) > 5 else (np.nan, np.nan)
eta_4cell_pooled, eta_err_4cell_pooled = fit_brody(all_s_4cell) if len(all_s_4cell) > 5 else (np.nan, np.nan)

print(f"Pooled Brody parameter:")
print(f"  2-cell: eta = {eta_2cell_pooled:.4f} +/- {eta_err_2cell_pooled:.4f}")
print(f"  4-cell: eta = {eta_4cell_pooled:.4f} +/- {eta_err_4cell_pooled:.4f}")
print(f"  (Poisson: eta = 0, GOE: eta = 1)")


# =====================================================================
#  11. CROSS-CHECK: PAIR NUMBER CONSERVATION
# =====================================================================

print("\n" + "=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# Verify total pair number is conserved
def build_total_pair_number(basis, n_pair, dim):
    """Total pair number operator (should be n_pair * I)."""
    N_op = np.zeros((dim, dim))
    for i, slots in enumerate(basis):
        N_op[i, i] = len(slots)  # = n_pair for all states
    return N_op

N_op_2 = build_total_pair_number(basis_2, N_pair, dim_2)
N_op_4 = build_total_pair_number(basis_4, N_pair, dim_4)

comm_N_2 = np.max(np.abs(H_2cell @ N_op_2 - N_op_2 @ H_2cell))
comm_N_4 = np.max(np.abs(H_4cell @ N_op_4 - N_op_4 @ H_4cell))
print(f"[H_2cell, N_total] = {comm_N_2:.2e} (should be 0)")
print(f"[H_4cell, N_total] = {comm_N_4:.2e} (should be 0)")

# Trace checks: Tr(H) should scale linearly with dim
tr_2 = np.trace(H_2cell)
tr_4 = np.trace(H_4cell)
print(f"\nTr(H_2cell) = {tr_2:.4f}, Tr(H_2cell)/dim = {tr_2/dim_2:.6f}")
print(f"Tr(H_4cell) = {tr_4:.4f}, Tr(H_4cell)/dim = {tr_4/dim_4:.6f}")

# Energy scale checks
E_range_2 = evals_2cell[-1] - evals_2cell[0]
E_range_4 = evals_4cell[-1] - evals_4cell[0]
print(f"\nSpectrum range: 2-cell = {E_range_2:.4f}, 4-cell = {E_range_4:.4f} M_KK")
print(f"Mean spacing: 2-cell = {E_range_2/(dim_2-1):.6f}, 4-cell = {E_range_4/(dim_4-1):.6f}")

# Compare with S58 result
try:
    d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
    r_s58 = float(d58['r_combined'])
    print(f"\nS58 <r> (combined, 2-cell): {r_s58:.4f}")
    print(f"This <r> (combined, 2-cell): {r_combined_2:.4f}")
    print(f"Difference: {r_combined_2 - r_s58:.4f}")
    # Note: S58 used E_J from s56_gge_fabric.npz which may differ from 7.042
    E_J_s58 = float(d58['E_J_fold'])
    print(f"S58 E_J = {E_J_s58:.4f} vs this E_J = {E_J:.4f}")
except Exception as e:
    print(f"Could not load S58 data for comparison: {e}")


# =====================================================================
#  12. GATE VERDICT
# =====================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: RICHARDSON-GAUDIN-N2-63")
print("=" * 70)

# The definitive quantity is the sector-resolved <r>.
# Use the 4-cell result as primary (larger Hilbert space, better statistics),
# with 2-cell as cross-check.

print(f"\n--- Summary ---")
print(f"2-cell: <r> (Z_2-resolved) = {r_combined_2:.4f}, eta = {eta_2cell_pooled:.4f} +/- {eta_err_2cell_pooled:.4f}")
print(f"4-cell: <r> (sector-resolved) = {r_combined_4:.4f}, eta = {eta_4cell_pooled:.4f} +/- {eta_err_4cell_pooled:.4f}")
print(f"Controls: 2-cell E_J=0: {r_noJ_2:.4f}, 4-cell E_J=0: {r_noJ_4:.4f}")
print(f"\nPoisson: <r> = 0.386, eta = 0")
print(f"GOE:     <r> = 0.530, eta = 1")
print(f"Gate threshold: <r> > 0.48 for PASS (Wigner-Dyson)")
print(f"                <r> < 0.42 for FAIL (Poisson)")

# Use the 4-cell combined <r> as the primary verdict variable
r_verdict = r_combined_4
eta_verdict = eta_4cell_pooled

# Also compute the distance in <r> space
# Interpolation parameter: q = (r - r_Poisson) / (r_GOE - r_Poisson)
# q = 0: Poisson,  q = 1: GOE
r_Poisson_ref = 0.386  # (local)
r_GOE_ref = 0.530  # (local)
q_2cell = (r_combined_2 - r_Poisson_ref) / (r_GOE_ref - r_Poisson_ref)
q_4cell = (r_combined_4 - r_Poisson_ref) / (r_GOE_ref - r_Poisson_ref)

print(f"\nInterpolation parameter q = (<r> - 0.386)/(0.530 - 0.386):")
print(f"  2-cell: q = {q_2cell:.4f}")
print(f"  4-cell: q = {q_4cell:.4f}")
print(f"  (q = 0: Poisson, q = 1: GOE)")

if r_verdict > 0.48:
    verdict = "PASS"
    detail = (f"<r> = {r_verdict:.4f} > 0.48. "
              f"Brody eta = {eta_verdict:.3f}. "
              f"Integrability broken at N_pair = 2. P(s) consistent with Wigner-Dyson.")
elif r_verdict < 0.42:
    verdict = "FAIL"
    detail = (f"<r> = {r_verdict:.4f} < 0.42. "
              f"Brody eta = {eta_verdict:.3f}. "
              f"Integrability persists at N_pair = 2. P(s) consistent with Poisson.")
else:
    verdict = "INFORMATIVE"
    detail = (f"<r> = {r_verdict:.4f} in [0.42, 0.48]. "
              f"Brody eta = {eta_verdict:.3f}. "
              f"Intermediate regime: partial integrability breaking. "
              f"Consistent with S55 2-sigma hint. "
              f"N_pair = 3 or larger sub-lattice needed for definitive verdict.")

print(f"\n>>> VERDICT: {verdict}")
print(f">>> {detail}")


# =====================================================================
#  13. SAVE DATA
# =====================================================================

save_path = os.path.join(data_dir, 's63_rg_n2.npz')
np.savez(save_path,
    # Metadata
    N_pair=N_pair,
    N_modes=N_modes,
    E_J=E_J,

    # 2-cell
    N_cells_2=N_cells_2,
    dim_2=dim_2,
    evals_2cell=evals_2cell,
    evals_2cell_noJ=evals_2cell_noJ,
    evals_even_2=evals_even_2,
    evals_odd_2=evals_odd_2,
    r_even_2=r_even_2,
    r_odd_2=r_odd_2,
    r_combined_2=r_combined_2,
    r_full_2=r_full_2,
    r_noJ_2=r_noJ_2,
    eta_2cell_pooled=eta_2cell_pooled,
    eta_err_2cell_pooled=eta_err_2cell_pooled,
    s_even_2=s_even_2,
    s_odd_2=s_odd_2,

    # 4-cell
    N_cells_4=N_cells_4,
    dim_4=dim_4,
    topo_4cell=np.array([topo_4cell]),
    evals_4cell=evals_4cell,
    evals_4cell_noJ=evals_4cell_noJ,
    r_combined_4=r_combined_4,
    r_full_4=r_full_4,
    r_noJ_4=r_noJ_4,
    eta_4cell_pooled=eta_4cell_pooled,
    eta_err_4cell_pooled=eta_err_4cell_pooled,
    q_2cell=q_2cell,
    q_4cell=q_4cell,

    # Gate
    gate_name=np.array(['RICHARDSON-GAUDIN-N2-63']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"\nData saved to {save_path}")


# =====================================================================
#  14. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'S63 W6-08: RICHARDSON-GAUDIN-N2-63 — {verdict}',
             fontsize=14, fontweight='bold')

# (a) 2-cell spectrum
ax = axes[0, 0]
ax.plot(evals_2cell, 'b-', alpha=0.7, label=f'E_J = {E_J:.2f}')
ax.plot(evals_2cell_noJ, 'r--', alpha=0.5, label='E_J = 0')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title(f'2-cell spectrum (dim={dim_2})')
ax.legend(fontsize=8)

# (b) 4-cell spectrum
ax = axes[0, 1]
ax.plot(evals_4cell, 'b-', alpha=0.7, label=f'E_J = {E_J:.2f}')
ax.plot(evals_4cell_noJ, 'r--', alpha=0.5, label='E_J = 0')
ax.set_xlabel('Eigenstate index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title(f'4-cell spectrum (dim={dim_4})')
ax.legend(fontsize=8)

# (c) P(s) distribution: 2-cell pooled
ax = axes[0, 2]
if len(all_s_2cell) > 5:
    ax.hist(all_s_2cell, bins=25, density=True, alpha=0.6, color='steelblue',
            label=f'2-cell (eta={eta_2cell_pooled:.3f})')
    s_th = np.linspace(0, 4, 200)
    ax.plot(s_th, np.exp(-s_th), 'r--', label='Poisson')
    ax.plot(s_th, (np.pi/2) * s_th * np.exp(-(np.pi/4) * s_th**2), 'g-', label='GOE')
    if not np.isnan(eta_2cell_pooled):
        ax.plot(s_th, brody_pdf(s_th, eta_2cell_pooled), 'k:', lw=2, label=f'Brody (eta={eta_2cell_pooled:.2f})')
ax.set_xlabel('s (normalized spacing)')
ax.set_ylabel('P(s)')
ax.set_title('P(s): 2-cell, sector-resolved')
ax.legend(fontsize=7)
ax.set_xlim(0, 4)

# (d) P(s) distribution: 4-cell pooled
ax = axes[1, 0]
if len(all_s_4cell) > 5:
    ax.hist(all_s_4cell, bins=30, density=True, alpha=0.6, color='darkorange',
            label=f'4-cell (eta={eta_4cell_pooled:.3f})')
    s_th = np.linspace(0, 4, 200)
    ax.plot(s_th, np.exp(-s_th), 'r--', label='Poisson')
    ax.plot(s_th, (np.pi/2) * s_th * np.exp(-(np.pi/4) * s_th**2), 'g-', label='GOE')
    if not np.isnan(eta_4cell_pooled):
        ax.plot(s_th, brody_pdf(s_th, eta_4cell_pooled), 'k:', lw=2, label=f'Brody (eta={eta_4cell_pooled:.2f})')
ax.set_xlabel('s (normalized spacing)')
ax.set_ylabel('P(s)')
ax.set_title(f'P(s): 4-cell ({topo_4cell}), sector-resolved')
ax.legend(fontsize=7)
ax.set_xlim(0, 4)

# (e) <r> comparison bar chart
ax = axes[1, 1]
labels_bar = ['2c Even', '2c Odd', '2c Comb', '4c Comb', '4c Full', '2c noJ', '4c noJ']
r_vals_bar = [r_even_2, r_odd_2, r_combined_2, r_combined_4, r_full_4, r_noJ_2, r_noJ_4]
colors_bar = ['steelblue', 'steelblue', 'navy', 'darkorange', 'orange', 'lightcoral', 'lightcoral']
ax.bar(range(len(labels_bar)), r_vals_bar, color=colors_bar, alpha=0.8)
ax.axhline(0.386, color='red', ls='--', lw=1, label='Poisson')
ax.axhline(0.530, color='green', ls='--', lw=1, label='GOE')
ax.axhline(0.48, color='purple', ls=':', lw=1, label='PASS threshold')
ax.set_xticks(range(len(labels_bar)))
ax.set_xticklabels(labels_bar, rotation=45, fontsize=8)
ax.set_ylabel('<r>')
ax.set_title('<r> comparison')
ax.legend(fontsize=7)

# (f) Brody parameter summary
ax = axes[1, 2]
eta_labels = ['2-cell\n(pooled)', '4-cell\n(pooled)']
eta_vals = [eta_2cell_pooled, eta_4cell_pooled]
eta_errs = [eta_err_2cell_pooled, eta_err_4cell_pooled]
valid = [not np.isnan(v) for v in eta_vals]
eta_vals_plot = [v if valid[i] else 0 for i, v in enumerate(eta_vals)]
eta_errs_plot = [v if valid[i] else 0 for i, v in enumerate(eta_errs)]
ax.bar(range(len(eta_labels)), eta_vals_plot, yerr=eta_errs_plot,
       color=['steelblue', 'darkorange'], alpha=0.8, capsize=5)
ax.axhline(0, color='red', ls='--', lw=1, label='Poisson (eta=0)')
ax.axhline(1, color='green', ls='--', lw=1, label='GOE (eta=1)')
ax.set_xticks(range(len(eta_labels)))
ax.set_xticklabels(eta_labels, fontsize=10)
ax.set_ylabel('Brody eta')
ax.set_title('Brody parameter')
ax.legend(fontsize=8)
ax.set_ylim(-0.1, 1.2)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's63_rg_n2.png')
plt.savefig(plot_path, dpi=150)
print(f"Plot saved to {plot_path}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
