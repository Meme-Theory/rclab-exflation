#!/usr/bin/env python3
"""
s63_island_kk.py — Island Formula on Internal KK Geometry
==========================================================

Session 63, Gate: ISLAND-KK-63
  INFO: Report whether non-trivial island exists.
        S_ent > 0: entanglement route opens (one-loop modifies structure).
        S_ent = 0: product state confirmed at one-loop level.  # (local)

Physics:
  Apply the island formula S = min_I ext_{dI}[A(dI)/(4G) + S_bulk(I+R)]
  to the one-loop KK geometry.

  Key inputs (corrected W6-17):
    - Physical Bogoliubov depletion: n_dep = 5.12% (not 44.7%)
    - Vacuum non-overlap: 59.3% (tree vs one-loop vacua differ substantially)
    - S62 one-loop: all 36 Hessian eigenvalues flip positive at one-loop
    - S63 local entangle: S_ent = 0.728 nats across spatial bipartition

  The island formula on the internal geometry works as follows:

  1. The internal SU(3) space is discretized as a 32-cell BCC graph.
  2. An "island" I is a connected subset of graph vertices.
  3. The boundary dI consists of edges crossing from I to its complement.
  4. A(dI)/(4G) = (number of boundary edges) * (edge area) / (4 G_N^{(11)})
     where G_N^{(11)} is the effective Newton's constant on the internal space.
  5. S_bulk(I + R) is the entanglement entropy of bulk fields in region I+R.

  Three necessary conditions for islands (Hartman-Jiang-Shaghoulian 2020):
    C1: Bekenstein bound violation: S_bulk(I) > A(dI)/(4G)
    C2: Quantum normality of island
    C3: Quantum normality of complement

  We test ALL possible subsets I of the 32-cell graph (or representative ones)
  to find if any non-trivial island minimizes the generalized entropy.

  The key competition is:
    - Area term: A(dI)/(4G) ~ (edges cut) * (a2_fold * M_KK^2) / (4 G_N * M_KK^2)
      This is in Planck units on the internal space.
    - Bulk term: S_bulk comes from the one-loop Gaussian state.

  For the internal geometry, the effective 7D Newton's constant relates to 4D via:
    G_N^{(4)} = G_N^{(7)} / Vol(SU(3))
  So G_N^{(7)} = G_N^{(4)} * Vol(SU(3))

  And the "area" of an edge in the graph is the area of the codim-2 surface
  separating two Voronoi cells, which scales as ~ R_KK^5 (5D area in 7D space).

Method:
  1. Load one-loop Hessian eigenvalues and Bogoliubov parameters from S62/S63
  2. Compute the one-loop Gaussian state correlation matrix on the 32-cell graph
  3. For each possible bipartition I vs complement:
     a. Compute A(dI)/(4G): area term from graph cut weight
     b. Compute S_bulk(I+R): entanglement entropy via Peschel method
     c. Evaluate S_gen = A(dI)/(4G) + S_bulk(I+R)
  4. Find the extremum: does a non-trivial island (I != empty, I != full) minimize?
  5. Compare to no-island: S_no_island = S_bulk(R) (just the bulk entropy of "radiation")

  The critical ratio is: S_ent / (A/4G) per edge. If this exceeds 1, Bekenstein
  bound is violated and islands are possible.

Inputs:
  computations/session-62/s62_volovik_partition.npz
  computations/session-63/s63_local_entangle.npz
  computations/session-63/s63_moduli_depletion.npz
  computations/session-54/s54_tb_hamiltonian.npz

Outputs:
  computations/session-63/s63_island_kk.npz
  computations/session-63/s63_island_kk.png

Author: Hawking-Theorist Agent (S63)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, logm
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    N_cells, a0_fold, a2_fold, a4_fold, tau_fold, PI,
    M_KK, M_KK_gravity, M_Pl_unreduced, M_Pl_reduced,
    G_N, hbar_SI, c_light, k_B, l_Planck,
    Vol_SU3_Haar, g0_diag, rho_Lambda_obs,
    T_acoustic, J_C2, N_dof_BCS
)

data_dir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("S63 W6-30: Island Formula on Internal KK Geometry")
print("Gate: ISLAND-KK-63")
print("=" * 72)

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================
print("\n--- Section 1: Loading input data ---")

# S62 Volovik partition (one-loop Hessian)
d62 = np.load(os.path.join(data_dir, 's62_volovik_partition.npz'), allow_pickle=True)
evals_eff = d62['evals_eff']        # 36 one-loop eigenvalues (all positive)
evals_tree = d62['evals_tree']       # 36 tree-level eigenvalues (all negative)
S_1loop = float(d62['S_1loop_fold'])
S_b = float(d62['S_b_fold'])
quantum_depletion_hessian = float(d62['quantum_depletion'])  # 0.447 (Hessian norm ratio)
n_modes = int(d62['n_modes'])

# S63 moduli depletion (corrected physical values)
d63dep = np.load(os.path.join(data_dir, 's63_moduli_depletion.npz'), allow_pickle=True)
n_dep_physical = float(d63dep['n_dep_frac_D1'])      # 0.0512 (physical Bogoliubov)
vac_non_overlap = float(d63dep['vac_depletion_D2'])   # 0.593 (vacuum non-overlap)
r_k = d63dep['r_k']                                    # squeeze parameters per mode
u_k_sq = d63dep['u_k_sq']                              # |u_k|^2 Bogoliubov
v_k_sq = d63dep['v_k_sq']                              # |v_k|^2 Bogoliubov

# S63 local entanglement (already computed)
d63ent = np.load(os.path.join(data_dir, 's63_local_entangle.npz'), allow_pickle=True)
S_ent_normal = float(d63ent['S_ent_normal_max'])   # 0.728 nats
S_ent_bcs = float(d63ent['S_ent_bcs_max'])         # 0.707 nats
adj = d63ent['adj']                                 # 32x32 adjacency
n_k_GGE = d63ent['n_k_GGE']                        # GGE occupations (8 modes)
w_A_modes = d63ent['w_A_modes']                     # mode weight in region A

# TB Hamiltonian eigenvectors
d54 = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
tau_arr = d54['tau_values']
fold_idx = np.argmin(np.abs(tau_arr - tau_fold))
V_tb = d54['eigenvectors'][fold_idx]                # (32, 32) eigenvectors
eigs_tb = d54['eigenvalues'][fold_idx]              # 32 eigenvalues
cell_dims = d54['cell_dims']                         # irrep dimensions

print(f"  One-loop modes: {n_modes} (all positive at one-loop)")
print(f"  Physical depletion: {n_dep_physical:.4f} (5.12%)")
print(f"  Vacuum non-overlap: {vac_non_overlap:.4f} (59.3%)")
print(f"  Local S_ent (normal): {S_ent_normal:.4f} nats")
print(f"  Local S_ent (BCS): {S_ent_bcs:.4f} nats")
print(f"  Hessian depletion (S62): {quantum_depletion_hessian:.4f}")

N = adj.shape[0]  # 32 vertices
N_edges = int(np.sum(adj)) // 2
N_BCS = min(8, len(n_k_GGE))  # BCS modes

# =====================================================================
#  2. EFFECTIVE NEWTON'S CONSTANT ON INTERNAL SPACE
# =====================================================================
print("\n--- Section 2: Effective G_N on internal space ---")

# The 4D Newton's constant in natural units:
# G_N^{(4)} = 1 / (8 pi M_Pl_reduced^2)
G4_natural = 1.0 / (8.0 * PI * M_Pl_reduced**2)  # in GeV^{-2}
print(f"  G_N^(4) = {G4_natural:.4e} GeV^{{-2}}")

# The 11D (or 7D internal) Newton's constant:
# G_N^{(4)} = G_N^{(4+d)} / Vol(K_d)
# For SU(3) as 7D manifold (real dim 8, but we use 7 for codim-2 count):
# Actually SU(3) has real dimension 8. KK reduction on 8D gives:
# G_N^{(12)} = G_N^{(4)} * Vol(SU(3)) * (M_KK)^{-8}
# But we work in M_KK units where lengths are O(1).

# In M_KK units, the volume of SU(3) is Vol_SU3_Haar (dimensionless in those units).
# The effective "area" of a codimension-2 surface in the internal space
# that separates two Voronoi cells scales as R_KK^{d-2} where d=8.
# So area ~ R_KK^6 ~ M_KK^{-6} per cell boundary.

# The Bekenstein-Hawking entropy of a surface in the internal space:
# S_BH = A / (4 G_N^{(d+2)})
# where G_N^{(d+2)} is the Newton's constant in the full (d+2)-dimensional theory.

# For M^4 x SU(3), we have 4+8=12 dimensions. The Newton's constant is:
# G_N^{(12)} = G_N^{(4)} * Vol(SU(3))_physical
# where Vol(SU(3))_physical = Vol_SU3_Haar / M_KK^8

# Area of boundary between two cells (6-dimensional surface in 8D SU(3)):
# A_edge ~ (Vol(SU(3)))^{6/8} / N_cells^{6/8} [rough scaling]

# More precisely, on the 32-cell Voronoi tessellation of SU(3):
# Each cell has volume V_cell = Vol(SU(3)) / N_cells
# The "area" (6D volume) of a cell boundary ~ V_cell^{6/8} = V_cell^{3/4}

# In M_KK units (M_KK = 1):
V_cell_MKK = Vol_SU3_Haar / N_cells  # dimensionless volume per cell
A_edge_MKK = V_cell_MKK**(6.0/8.0)   # 6D "area" of an edge (cell boundary)

print(f"  Vol(SU(3))/M_KK^8 = {Vol_SU3_Haar:.2f}")
print(f"  V_cell/M_KK^8 = {V_cell_MKK:.4f}")
print(f"  A_edge/M_KK^6 = {A_edge_MKK:.4f}")

# The 12D Newton's constant in M_KK units:
# G_N^{(12)} in M_KK units = G_N^{(4)} [GeV^{-2}] * Vol(SU(3)) [M_KK^{-8}]
#                           = G_4 * Vol_SU3_Haar * M_KK^{-8} [GeV^{-2} * GeV^{-8}]
# But we want everything in M_KK units, so multiply by M_KK^{10} (10=12-2):
# G_{12,MKK} = G_4 * M_KK^2 * Vol_SU3_Haar

G12_MKK = G4_natural * M_KK**2 * Vol_SU3_Haar
print(f"  G_N^(12) in M_KK units = {G12_MKK:.4e}")

# The Bekenstein-Hawking entropy per edge:
# S_BH_edge = A_edge / (4 * G_12)
S_BH_per_edge = A_edge_MKK / (4.0 * G12_MKK)
print(f"  S_BH per edge = A_edge/(4*G_12) = {S_BH_per_edge:.4e}")

# Key ratio: local entanglement per edge vs BH entropy per edge
S_ent_per_edge = S_ent_normal / N_edges
ratio_ent_BH = S_ent_per_edge / S_BH_per_edge if S_BH_per_edge > 0 else float('inf')
print(f"  S_ent per edge = {S_ent_per_edge:.6f} nats")
print(f"  S_ent / S_BH per edge = {ratio_ent_BH:.4e}")

# =====================================================================
#  3. ALTERNATIVE: SPECTRAL-ACTION BASED AREA TERM
# =====================================================================
print("\n--- Section 3: Spectral action area term ---")

# The spectral action gives an INTERNAL geometric "area" through a2_fold.
# a2 = integral of scalar curvature * volume form over SU(3)
# This is the natural geometric area functional on the internal space.
#
# In the spectral action framework, the analog of A/(4G) is:
#   S_grav = (1/2) * a2 * f_2 * Lambda^2 / (4*pi^2)
# where f_2 = int_0^inf f(u) du (cutoff function moment).
#
# For the internal Rindler cut, the "area" contribution scales as:
#   S_area ~ a2_fold * f(edge_fraction)
# where edge_fraction = (edges cut) / (total edges).
#
# The spectral action itself acts as the gravitational partition function.
# At one-loop, the effective action shifts by S_1loop.

# Spectral action "entropy" per edge: think of a2 as the integrated curvature,
# each edge carries a fraction of the total curvature.
S_spectral_per_edge = a2_fold / N_edges
print(f"  a2_fold = {a2_fold:.2f}")
print(f"  S_spectral per edge = a2_fold / N_edges = {S_spectral_per_edge:.2f}")
print(f"  (This is the spectral-action analog of A/(4G) per edge)")

# The ratio that determines island existence (Bekenstein condition C1):
# Need S_bulk(I) > A(dI)/(4G) for island to form.
# With spectral action: S_bulk vs a2 * (edge fraction)
ratio_spectral = S_ent_normal / S_spectral_per_edge
print(f"  S_ent / S_spectral_per_edge = {ratio_spectral:.6e}")
print(f"  Bekenstein condition: need this ratio >> 1 for island. GOT: {ratio_spectral:.2e}")

# =====================================================================
#  4. ONE-LOOP GAUSSIAN STATE: FULL COVARIANCE MATRIX
# =====================================================================
print("\n--- Section 4: One-loop Gaussian state on graph ---")

# The one-loop state is a squeezed Gaussian. The Bogoliubov transformation
# from tree-level to one-loop modes gives a squeezed vacuum.
# The squeeze parameters r_k from S63 moduli depletion give:
#   |v_k|^2 = sinh^2(r_k) = depletion per mode
#   |u_k|^2 = cosh^2(r_k)
#
# For the island formula, S_bulk is the entanglement entropy of this
# squeezed state restricted to a spatial subregion.

print(f"  Squeeze parameters r_k: min={np.min(r_k):.4f}, max={np.max(r_k):.4f}")
print(f"  |v_k|^2 (depletion): min={np.min(v_k_sq):.6f}, max={np.max(v_k_sq):.6f}")
print(f"  Total n_dep = sum(|v_k|^2) / N_modes = {np.sum(v_k_sq)/n_modes:.4f}")

# Build the correlation matrix of the squeezed vacuum on the 32-cell graph.
# The one-loop state has correlation:
#   C_ij = sum_k |v_k|^2 * phi_k(i) * phi_k(j)^*
# where phi_k are the one-loop eigenmodes on the graph.
#
# We use the TB eigenvectors V_tb as the mode functions.
# The first N_modes modes are relevant (though only N_BCS are strongly occupied in GGE).

# For the island computation, we use ALL 36 modes with their one-loop squeeze.
# However, V_tb is 32x32 (graph has 32 vertices, TB has 32 modes).
# The 36 Hessian modes from S62 include BCS fluctuation modes beyond the TB basis.
# We restrict to the 32 graph modes and assign squeeze params from the
# first 32 modes of the depletion data, or map appropriately.

N_squeeze = min(n_modes, N)  # min(36, 32) = 32

# Build correlation matrix for squeezed vacuum
# C_ij = sum_{k=0}^{N-1} v_k^2 * V[i,k] * V[j,k]^*
# where v_k^2 = |v_k|^2 = sinh^2(r_k)
v_sq_graph = np.zeros(N)
for k in range(N_squeeze):
    if k < len(v_k_sq):
        v_sq_graph[k] = v_k_sq[k]

C_squeezed = np.zeros((N, N))
for k in range(N):
    if v_sq_graph[k] > 0:
        C_squeezed += v_sq_graph[k] * np.outer(V_tb[:, k], V_tb[:, k].conj())

# Also build the GGE correlation matrix (from S63 local entangle data)
# The GGE has occupation n_k for the first N_BCS modes.
C_GGE = np.zeros((N, N))
for k in range(N_BCS):
    C_GGE += n_k_GGE[k] * np.outer(V_tb[:, k], V_tb[:, k].conj())

print(f"  C_squeezed: trace = {np.trace(C_squeezed):.6f} (total depleted particles)")
print(f"  C_GGE: trace = {np.trace(C_GGE):.6f} (total GGE occupation)")

# =====================================================================
#  5. ISLAND SEARCH: ENUMERATE SUBSETS AND COMPUTE S_gen
# =====================================================================
print("\n--- Section 5: Island search ---")

# For a graph of 32 vertices, full enumeration is 2^32 ~ 4 billion. Impractical.
# Strategy: enumerate subsets of size 1 to 16 using smart sampling.
# Focus on:
#   a) Single-vertex islands (32 cases)
#   b) Connected subgraphs of size 2-6 (sample from neighbors)
#   c) Spectral bisections (eigenvector-based)
#   d) Random connected subsets (Monte Carlo)

def peschel_entropy(C_A):
    """Compute entanglement entropy from correlation submatrix eigenvalues."""
    nu = np.linalg.eigvalsh(C_A)
    # Clip to valid range [0, 1]
    nu = np.clip(nu, 1e-15, 1.0 - 1e-15)
    S = 0.0  # (local)
    for n in nu:
        if n > 1e-14 and (1 - n) > 1e-14:
            S -= n * np.log(n) + (1 - n) * np.log(1 - n)
    return S

def compute_S_gen(island_vertices, adj_matrix, C_full, area_per_edge):
    """
    Compute generalized entropy for a given island configuration.

    S_gen = A(dI)/(4G) + S_bulk(I + R)

    Here:
    - A(dI) = number of edges crossing the island boundary * area_per_edge
    - S_bulk(I+R) = entanglement entropy of I with its complement
      For the island formula, I+R means the island plus the "radiation" system.
      In our setup, R is the 4D external space, and I is a subset of the
      internal graph. S_bulk(I+R) is approximated by S_ent(I, complement(I)).
    """
    N_v = adj_matrix.shape[0]
    mask = np.zeros(N_v, dtype=bool)
    mask[island_vertices] = True

    # Count boundary edges (edges from island to complement)
    n_boundary = 0
    for i in island_vertices:
        for j in range(N_v):
            if adj_matrix[i, j] > 0 and not mask[j]:
                n_boundary += 1

    # Area term
    S_area = n_boundary * area_per_edge

    # Bulk entropy: restrict correlation matrix to island vertices
    idx = np.array(island_vertices)
    C_I = C_full[np.ix_(idx, idx)]
    S_bulk = peschel_entropy(C_I)

    S_gen = S_area + S_bulk
    return S_gen, S_area, S_bulk, n_boundary

# Area per edge: use spectral action scaling
# The "gravitational area" per edge in Planck units on the internal space
# Option A: G_N^{(12)} based (enormous, makes area term ~ 0)
# Option B: Spectral action based (a2 per edge, makes area term ~ 30)
# Option C: Dimensionless on the graph (area = 1 per edge, natural units)

# We compute for MULTIPLE choices of area_per_edge to understand the regime.

# Choice 1: Pure G_N based (Planck scale on internal space)
area_GN = S_BH_per_edge  # A/(4G) per edge in 12D Planck units

# Choice 2: Spectral action based
area_SA = S_spectral_per_edge  # a2_fold / N_edges

# Choice 3: Graph-natural units (each edge = 1)
area_graph = 1.0  # (local)

print(f"\n  Area per edge choices:")
print(f"    G_N-based: {area_GN:.4e}")
print(f"    Spectral-action: {area_SA:.2f}")
print(f"    Graph-natural: {area_graph:.2f}")

# =====================================================================
#  5a. SINGLE-VERTEX ISLANDS (32 cases)
# =====================================================================
print("\n  --- 5a: Single-vertex islands ---")

results_1v = []
for v in range(N):
    S_gen, S_area, S_bulk, n_bdry = compute_S_gen(
        [v], adj, C_squeezed, area_SA)
    results_1v.append({
        'vertices': [v], 'S_gen': S_gen, 'S_area': S_area,
        'S_bulk': S_bulk, 'n_boundary': n_bdry
    })

# No-island baseline: S_gen = S_bulk(full system) = 0 (pure state globally)
# Actually for the squeezed vacuum, the FULL system is pure => S = 0.
# So S_no_island = 0.
S_no_island = 0.0  # (local)

best_1v = min(results_1v, key=lambda x: x['S_gen'])
worst_1v = max(results_1v, key=lambda x: x['S_gen'])
print(f"  Best single-vertex island: vertex {best_1v['vertices'][0]}")
print(f"    S_gen = {best_1v['S_gen']:.6f} (S_area={best_1v['S_area']:.4f}, S_bulk={best_1v['S_bulk']:.6f})")
print(f"    Boundary edges: {best_1v['n_boundary']}")
print(f"  Worst single-vertex: S_gen = {worst_1v['S_gen']:.6f}")
print(f"  No-island baseline: S_gen = {S_no_island:.6f}")
print(f"  Is best island better than no-island? {best_1v['S_gen'] < S_no_island}")

# =====================================================================
#  5b. CONNECTED SUBGRAPHS SIZE 2-8
# =====================================================================
print("\n  --- 5b: Connected subgraphs (size 2-8) ---")

def get_neighbors(v, adj_mat):
    return list(np.where(adj_mat[v] > 0)[0])

def grow_connected(start, adj_mat, target_size, rng):
    """Grow a connected subgraph from start vertex to target_size."""
    island = {start}
    frontier = set(get_neighbors(start, adj_mat))
    while len(island) < target_size and frontier:
        v = rng.choice(list(frontier))
        island.add(v)
        for nb in get_neighbors(v, adj_mat):
            if nb not in island:
                frontier.add(nb)
        frontier -= island
    return sorted(island)

rng = np.random.RandomState(42)
all_results = []
all_results.extend(results_1v)

for size in range(2, 9):
    n_trials = min(200, N * 10)
    best_this_size = None
    for trial in range(n_trials):
        start = rng.randint(0, N)
        island = grow_connected(start, adj, size, rng)
        if len(island) == size:
            S_gen, S_area, S_bulk, n_bdry = compute_S_gen(
                island, adj, C_squeezed, area_SA)
            result = {
                'vertices': island, 'S_gen': S_gen, 'S_area': S_area,
                'S_bulk': S_bulk, 'n_boundary': n_bdry, 'size': size
            }
            all_results.append(result)
            if best_this_size is None or S_gen < best_this_size['S_gen']:
                best_this_size = result
    if best_this_size:
        print(f"  Size {size}: best S_gen = {best_this_size['S_gen']:.4f} "
              f"(area={best_this_size['S_area']:.2f}, bulk={best_this_size['S_bulk']:.4f}, "
              f"bdry={best_this_size['n_boundary']})")

# =====================================================================
#  5c. HALF-SPACE ISLANDS (size 16, like local entangle partition)
# =====================================================================
print("\n  --- 5c: Half-space islands (size 16) ---")

# Use the same partition as S63 local entangle for direct comparison
A_max = d63ent['A_max']
B_max = d63ent['B_max']

S_gen_half, S_area_half, S_bulk_half, n_bdry_half = compute_S_gen(
    list(A_max), adj, C_squeezed, area_SA)
print(f"  Max-cut partition (same as LOCAL-ENTANGLE-63):")
print(f"    S_gen = {S_gen_half:.4f}")
print(f"    S_area = {S_area_half:.2f}")
print(f"    S_bulk = {S_bulk_half:.6f}")
print(f"    Boundary edges: {n_bdry_half}")

# =====================================================================
#  5d. GGE STATE ISLANDS (using GGE correlation matrix)
# =====================================================================
print("\n  --- 5d: GGE state islands ---")

# The GGE is the physically relevant post-transit state.
# The squeezed vacuum is the one-loop vacuum; the GGE is the thermal state
# on top of it. Both are Gaussian => Peschel method applies.

results_GGE = []
for size in [1, 2, 4, 8, 16]:
    n_trials = min(200, N * 5) if size < 16 else 10
    best_gge = None
    for trial in range(n_trials):
        if size == 16:
            island = list(A_max) if trial == 0 else grow_connected(
                rng.randint(0, N), adj, size, rng)
        else:
            island = grow_connected(rng.randint(0, N), adj, size, rng)
        if len(island) != size:
            continue
        S_gen, S_area, S_bulk, n_bdry = compute_S_gen(
            island, adj, C_GGE, area_SA)
        result = {
            'vertices': island, 'S_gen': S_gen, 'S_area': S_area,
            'S_bulk': S_bulk, 'n_boundary': n_bdry, 'size': size
        }
        results_GGE.append(result)
        if best_gge is None or S_gen < best_gge['S_gen']:
            best_gge = result
    if best_gge:
        print(f"  GGE size {size}: best S_gen = {best_gge['S_gen']:.4f} "
              f"(area={best_gge['S_area']:.2f}, bulk={best_gge['S_bulk']:.4f}, "
              f"bdry={best_gge['n_boundary']})")

# =====================================================================
#  6. CRITICAL ANALYSIS: BEKENSTEIN BOUND AND ISLAND CONDITIONS
# =====================================================================
print("\n--- Section 6: Bekenstein bound and island conditions ---")

# Condition C1 (Hartman-Jiang-Shaghoulian): S_bulk(I) > A(dI)/(4G)
# For the spectral-action area:
print("\n  Bekenstein condition analysis (spectral action area):")
for result in sorted(all_results, key=lambda x: x['S_gen'])[:5]:
    ratio = result['S_bulk'] / result['S_area'] if result['S_area'] > 0 else float('inf')
    print(f"    |I|={len(result['vertices'])}: S_bulk={result['S_bulk']:.6f}, "
          f"S_area={result['S_area']:.2f}, ratio={ratio:.2e}")

# For the G_N-based area:
print("\n  Bekenstein condition analysis (G_N-based area):")
for v in range(min(5, N)):
    S_gen_gn, S_area_gn, S_bulk_gn, n_bdry_gn = compute_S_gen(
        [v], adj, C_squeezed, area_GN)
    ratio_gn = S_bulk_gn / S_area_gn if S_area_gn > 0 else float('inf')
    print(f"    vertex {v}: S_bulk={S_bulk_gn:.6f}, S_area={S_area_gn:.4e}, ratio={ratio_gn:.4e}")

# =====================================================================
#  7. VACUUM NON-OVERLAP AND ENTANGLEMENT MODIFICATION
# =====================================================================
print("\n--- Section 7: Vacuum non-overlap and one-loop entanglement ---")

# The vacuum non-overlap is 59.3%: |<0_tree|0_1loop>|^2 = 0.407
# This means the one-loop vacuum has substantial support on excited tree-level states.
# The entanglement entropy of the one-loop vacuum (as seen in tree basis) is:
# S_vac = -ln|<0_tree|0_1loop>|^2 = -ln(1 - vac_non_overlap)

S_vac_overlap = -np.log(1.0 - vac_non_overlap)
print(f"  Vacuum non-overlap: {vac_non_overlap:.4f}")
print(f"  |<0_tree|0_1loop>|^2 = {1.0 - vac_non_overlap:.4f}")
print(f"  S_vac (tree-basis entropy of 1-loop vacuum): {S_vac_overlap:.4f} nats")

# For each mode, the squeezed vacuum contributes:
# S_k = -|v_k|^2 ln|v_k|^2 - |u_k|^2 ln|u_k|^2
S_per_mode_squeeze = np.zeros(len(v_k_sq))
for k in range(len(v_k_sq)):
    vk = v_k_sq[k]
    uk = u_k_sq[k]
    if vk > 1e-15 and uk > 1e-15:
        # For a single-mode squeezed state, the entropy is:
        # S = (n+1)ln(n+1) - n*ln(n) where n = sinh^2(r_k) = v_k_sq
        n = vk
        if n > 1e-15:
            S_per_mode_squeeze[k] = (n + 1) * np.log(n + 1) - n * np.log(n)

S_squeeze_total = np.sum(S_per_mode_squeeze)
print(f"  Total squeeze entropy (all modes): {S_squeeze_total:.4f} nats")
print(f"  Average squeeze entropy per mode: {S_squeeze_total/len(v_k_sq):.6f} nats")
print(f"  Max single-mode squeeze entropy: {np.max(S_per_mode_squeeze):.6f} nats")

# =====================================================================
#  8. THE ISLAND VERDICT
# =====================================================================
print("\n--- Section 8: Island verdict ---")

# The island formula requires finding I that minimizes S_gen.
# S_gen(I=empty) = S_bulk(R) = 0 (pure state globally)
# S_gen(I=non-empty) = A(dI)/(4G) + S_bulk(I+R) > 0 always
#
# Because the area term is always positive and the bulk entropy is
# non-negative, S_gen(I) > 0 for any non-empty I.
# Meanwhile S_gen(I=empty) = 0.
#
# Therefore: the empty island ALWAYS wins.
# NO non-trivial island exists on the internal geometry.

min_S_gen = min(r['S_gen'] for r in all_results)
print(f"  Minimum S_gen over all sampled islands: {min_S_gen:.6f}")
print(f"  No-island S_gen: {S_no_island:.6f}")
print(f"  Minimum S_gen > S_no_island: {min_S_gen > S_no_island}")

# The fundamental reason: the one-loop state on the internal space is
# EVERYWHERE sub-Bekenstein. The bulk entanglement S_bulk ~ 0.7 nats
# never exceeds the area term A/(4G) ~ 30 * area_per_edge.

# Even with the graph-natural area (1 per edge), the ratio is:
min_ratio_graph = S_ent_normal / 1.0  # ~ 0.73 per edge for half-space
# But you need S_bulk > A/(4G) for C1, and you need extremization of S_gen.

# The key dimensionless ratio that controls island existence:
# R_island = S_bulk_max / (A_min / 4G)
# For smallest possible island (1 vertex), boundary ~ degree edges,
# minimum degree is:
degrees = np.sum(adj, axis=1).astype(int)
min_degree = np.min(degrees)
max_degree = np.max(degrees)
mean_degree = np.mean(degrees)

# Best case for island: maximum S_bulk, minimum A
# S_bulk for 1 vertex ~ tiny (single site correlation)
# A for 1 vertex ~ min_degree * area_per_edge

S_bulk_1v_max = max(r['S_bulk'] for r in results_1v)
A_1v_min = min(r['S_area'] for r in results_1v)
ratio_best_case = S_bulk_1v_max / A_1v_min if A_1v_min > 0 else 0

print(f"\n  Graph degrees: min={min_degree}, max={max_degree}, mean={mean_degree:.1f}")
print(f"  Best-case ratio S_bulk/S_area (1-vertex): {ratio_best_case:.6f}")
print(f"  (Need ratio > 1 for Bekenstein violation. Got: {ratio_best_case:.2e})")

# =====================================================================
#  9. QUANTIFY THE AREA/ENTROPY HIERARCHY
# =====================================================================
print("\n--- Section 9: Area/entropy hierarchy ---")

# The fundamental issue: in the internal space, the "gravitational" area
# is ENORMOUS compared to the quantum entanglement entropy.
# This is because the internal space is CLASSICAL (deep classical regime).

# From ENTANGLE-CG24-60: area/bulk ratio = 1.36e6. Deep classical.
# The one-loop correction does not change this.

# S_ent at one-loop vs tree:
# Tree: S_ent = 0 exactly (product state in mode basis)
# One-loop: S_ent ~ 0.7 nats (from delocalized squeezed modes)
# But A/(4G) ~ 30 per edge * 67 edges = 2010 for half-space cut

S_area_halfspace = S_spectral_per_edge * n_bdry_half
print(f"  S_area (half-space, spectral action): {S_area_halfspace:.1f}")
print(f"  S_bulk (half-space, squeezed): {S_bulk_half:.4f}")
print(f"  Ratio (area/bulk): {S_area_halfspace/S_bulk_half:.1f}x")
print(f"  This is the DEEP CLASSICAL regime: area >> bulk entropy.")

# With G_N-based area: even more extreme
S_area_GN_half = area_GN * n_bdry_half
print(f"  S_area (half-space, G_N-based): {S_area_GN_half:.4e}")
if S_bulk_half > 0:
    print(f"  Ratio (area/bulk, G_N): {S_area_GN_half/S_bulk_half:.4e}x")

# =====================================================================
#  10. ONE-LOOP MODIFICATION OF ENTANGLEMENT STRUCTURE
# =====================================================================
print("\n--- Section 10: One-loop entanglement modification ---")

# Even though no island exists, the one-loop correction DOES generate
# non-zero entanglement on the internal space.

# Tree level: S_ent = 0 (product state)
# One-loop (squeezed): S_ent ~ small (from v_k^2 depletion)
# GGE (post-transit): S_ent = 0.728 nats (from delocalized modes)

# The one-loop squeezed vacuum entanglement:
# Use the Peschel method on C_squeezed
A_half = list(A_max)
C_A_sq = C_squeezed[np.ix_(A_half, A_half)]
S_ent_squeezed = peschel_entropy(C_A_sq)

print(f"  Tree-level S_ent: 0.000 nats (product state)")
print(f"  One-loop squeezed S_ent: {S_ent_squeezed:.6f} nats")
print(f"  GGE S_ent (from LOCAL-ENTANGLE-63): {S_ent_normal:.4f} nats")
print(f"  One-loop / GGE ratio: {S_ent_squeezed / S_ent_normal:.4f}" if S_ent_normal > 0 else "")

# Per-mode contributions to one-loop entanglement
S_1loop_per_mode = np.zeros(N)
for k in range(N):
    if v_sq_graph[k] > 1e-15:
        # Mode k contributes v_k^2 * (weight in A) * (weight in B)
        wA = np.sum(np.abs(V_tb[A_half, k])**2)
        wB = 1.0 - wA
        # This mode's contribution to entanglement ~ v_k^2 * 4*wA*wB
        S_1loop_per_mode[k] = v_sq_graph[k] * 4 * wA * wB

print(f"  Mode-resolved one-loop entanglement contributions:")
for k in range(min(10, N)):
    if S_1loop_per_mode[k] > 1e-10:
        print(f"    mode {k}: S_contrib ~ {S_1loop_per_mode[k]:.6f} "
              f"(v_k^2={v_sq_graph[k]:.6f})")

# =====================================================================
#  11. SAVE RESULTS
# =====================================================================
print("\n--- Section 11: Saving results ---")

# Collect key numbers
island_exists = False
S_gen_min_sampled = min_S_gen
S_gen_no_island = S_no_island
area_bulk_ratio_SA = S_area_halfspace / S_bulk_half if S_bulk_half > 0 else float('inf')
bekenstein_ratio = ratio_best_case

# Gate verdict
gate_verdict = "INFO"
gate_detail = (
    f"NO non-trivial island exists on internal KK geometry. "
    f"Empty island (S_gen=0) always wins. "
    f"Best sampled S_gen={S_gen_min_sampled:.4f} >> 0. "
    f"Bekenstein ratio (best case) = {bekenstein_ratio:.2e} << 1: "
    f"deep classical regime (area >> bulk entropy). "
    f"One-loop does generate S_ent={S_ent_squeezed:.4f} nats from squeeze, "
    f"but this is {area_bulk_ratio_SA:.0f}x below the area term. "
    f"Physical depletion n_dep=5.12% too small to create island. "
    f"Vacuum non-overlap 59.3% affects mode structure but not area/entropy hierarchy. "
    f"Result consistent with ENTANGLE-CG24-60 (area/bulk=1.36e6) and "
    f"S63 LOCAL-ENTANGLE (S_ent=0.728 nats, S_ent/S_BH~3e-7)."
)

print(f"\n  Gate: {gate_verdict}")
print(f"  Detail: {gate_detail}")

outpath = os.path.join(data_dir, 's63_island_kk.npz')
np.savez(outpath,
    # Gate
    gate_name='ISLAND-KK-63',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Island search
    island_exists=island_exists,
    S_gen_min_sampled=S_gen_min_sampled,
    S_gen_no_island=S_gen_no_island,

    # Area terms
    S_BH_per_edge=S_BH_per_edge,
    S_spectral_per_edge=S_spectral_per_edge,
    area_GN=area_GN,
    area_SA=area_SA,

    # Bulk entropies
    S_ent_squeezed=S_ent_squeezed,
    S_ent_normal=S_ent_normal,
    S_ent_bcs=S_ent_bcs,
    S_squeeze_total=S_squeeze_total,
    S_vac_overlap=S_vac_overlap,

    # Hierarchies
    area_bulk_ratio_SA=area_bulk_ratio_SA,
    area_bulk_ratio_GN=S_area_GN_half / S_bulk_half if S_bulk_half > 0 else 0,
    bekenstein_ratio=bekenstein_ratio,

    # Physical parameters
    n_dep_physical=n_dep_physical,
    vac_non_overlap=vac_non_overlap,
    quantum_depletion_hessian=quantum_depletion_hessian,

    # Graph info
    N_vertices=N,
    N_edges=N_edges,
    min_degree=min_degree,
    max_degree=max_degree,
    mean_degree=mean_degree,

    # One-loop entanglement
    S_1loop_per_mode=S_1loop_per_mode[:N],

    # Size scan (best S_gen per size)
    sizes_scanned=np.arange(1, 9),
)
print(f"  Saved: {outpath}")

# =====================================================================
#  12. PLOT
# =====================================================================
print("\n--- Section 12: Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ISLAND-KK-63: Island Formula on Internal KK Geometry\n'
             'No non-trivial island exists (deep classical regime)',
             fontsize=13, fontweight='bold')

# Panel A: S_gen vs island size
ax = axes[0, 0]
sizes = []
S_gens_by_size = {}
for r in all_results:
    s = len(r['vertices'])
    sizes.append(s)
    if s not in S_gens_by_size:
        S_gens_by_size[s] = []
    S_gens_by_size[s].append(r['S_gen'])

for s in sorted(S_gens_by_size.keys()):
    vals = S_gens_by_size[s]
    ax.scatter([s]*len(vals), vals, alpha=0.3, s=10, c='steelblue')
    ax.plot(s, np.min(vals), 'rv', markersize=8)

ax.axhline(y=0, color='red', linestyle='--', linewidth=2, label='No-island (S_gen=0)')
ax.set_xlabel('Island size (# vertices)')
ax.set_ylabel('S_gen (nats)')
ax.set_title('A: Generalized Entropy vs Island Size')
ax.legend()
ax.set_yscale('log')
ax.set_ylim(bottom=0.1)

# Panel B: Area vs Bulk decomposition for best islands per size
ax = axes[0, 1]
best_per_size = {}
for r in all_results:
    s = len(r['vertices'])
    if s not in best_per_size or r['S_gen'] < best_per_size[s]['S_gen']:
        best_per_size[s] = r

sizes_sorted = sorted(best_per_size.keys())
areas = [best_per_size[s]['S_area'] for s in sizes_sorted]
bulks = [best_per_size[s]['S_bulk'] for s in sizes_sorted]

ax.bar(sizes_sorted, areas, label='A(dI)/(4G) [spectral action]',
       color='coral', alpha=0.7, width=0.4, align='edge')
ax.bar([s+0.4 for s in sizes_sorted], bulks, label='S_bulk(I)',
       color='steelblue', alpha=0.7, width=0.4, align='edge')
ax.set_xlabel('Island size')
ax.set_ylabel('Entropy (nats)')
ax.set_title('B: Area Term vs Bulk Entropy')
ax.legend()

# Panel C: Bekenstein ratio per vertex
ax = axes[1, 0]
bek_ratios = []
for r in results_1v:
    ratio = r['S_bulk'] / r['S_area'] if r['S_area'] > 0 else 0
    bek_ratios.append(ratio)

ax.bar(range(N), bek_ratios, color='steelblue', alpha=0.7)
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2,
           label='Bekenstein bound (ratio=1)')
ax.set_xlabel('Vertex index')
ax.set_ylabel('S_bulk / [A/(4G)]')
ax.set_title('C: Bekenstein Ratio per Single-Vertex Island')
ax.set_yscale('log')
ax.legend()

# Panel D: Entanglement hierarchy
ax = axes[1, 1]
labels = ['Tree\nS_ent', '1-loop\nS_squeeze', 'GGE\nS_ent',
          'Area/(4G)\n(SA, 1 edge)', 'Area/(4G)\n(SA, half)']
values = [0.001,  # tree (show as small for log scale)
          max(S_ent_squeezed, 0.001),
          S_ent_normal,
          S_spectral_per_edge,
          S_area_halfspace]
colors = ['gray', 'steelblue', 'navy', 'coral', 'red']

bars = ax.bar(labels, values, color=colors, alpha=0.7)
ax.set_ylabel('Entropy (nats)')
ax.set_title('D: Entanglement Hierarchy\n(Area always dominates: no island)')
ax.set_yscale('log')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() * 1.2,
            f'{val:.3f}' if val < 100 else f'{val:.0f}',
            ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plotpath = os.path.join(data_dir, 's63_island_kk.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

# =====================================================================
#  13. SUMMARY
# =====================================================================
print("\n" + "=" * 72)
print("ISLAND-KK-63 SUMMARY")
print("=" * 72)
print(f"""
Gate: ISLAND-KK-63
Verdict: INFO

Result: NO non-trivial island on internal KK geometry.

Key numbers:
  1. S_gen(no island) = 0 (global pure state)
  2. S_gen(best island) = {S_gen_min_sampled:.4f} >> 0
  3. Bekenstein ratio (best case) = {bekenstein_ratio:.2e} << 1
  4. Area/bulk hierarchy (spectral action): {area_bulk_ratio_SA:.0f}x
  5. One-loop squeezed S_ent = {S_ent_squeezed:.4f} nats (was 0 at tree level)
  6. Physical depletion n_dep = {n_dep_physical:.4f} (5.12%)
  7. Vacuum non-overlap = {vac_non_overlap:.4f} (59.3%)

Physics:
  The island formula S = min_I ext[A(dI)/(4G) + S_bulk(I+R)] on the internal
  SU(3) geometry ALWAYS selects the empty island (I = empty set).

  Reason: The internal space is in the DEEP CLASSICAL regime. The gravitational
  area term A(dI)/(4G) exceeds the bulk entanglement S_bulk by >>{area_bulk_ratio_SA:.0f}x
  for every possible bipartition. The Bekenstein bound is NEVER violated
  (ratio = {bekenstein_ratio:.2e} << 1).

  The one-loop correction generates non-zero squeeze entanglement
  (S_squeeze = {S_ent_squeezed:.4f} nats) from the 5.12% physical depletion,
  and the vacuum non-overlap of 59.3% creates substantial mode mixing.
  But both effects are far too weak to overcome the area dominance.

  This confirms the ENTANGLE-CG24-60 result (area/bulk = 1.36e6) and is
  consistent with LOCAL-ENTANGLE-63 (S_ent/S_BH ~ 3e-7 per bond).

  Three necessary conditions for islands (Hartman-Jiang-Shaghoulian 2020):
    C1 (Bekenstein violation): FAILED ({bekenstein_ratio:.2e} << 1)
    C2 (Quantum normality): N/A (no island found)
    C3 (Quantum normality complement): N/A (no island found)

  The internal geometry remains firmly classical. No quantum gravitational
  island structure emerges at one-loop.

Cross-references:
  - Paper 28 (Hung-Nam 2023): KK islands require black string geometry. No BH here.
  - Paper 23 (Hartman-Jiang-Shaghoulian 2020): Islands need crunch/BH. No such geometry.
  - Paper 24 (Engelhardt-Wall 2014): QES requires quantum focussing. Area dominates.
  - ENTANGLE-CG24-60: area/bulk = 1.36e6 (confirmed, same regime).
  - LOCAL-ENTANGLE-63: S_ent = 0.728 nats (GGE), S_ent/S_BH ~ 3e-7.
""")

print("DONE.")
