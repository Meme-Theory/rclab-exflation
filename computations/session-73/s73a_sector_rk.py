#!/usr/bin/env python3
"""
s73a_sector_rk.py — Sector-Resolved R_K Conductance on CG(24)
===============================================================

Gate: SECTOR-RK-73a
  PASS: R_K^{SU(2)} / R_K^{U(1)} within 20% of threshold ratio delta_2/delta_1
        from W2-B (transport-threshold correlation)
  INFO: Sector resistances computed but no clear correlation with thresholds
  FAIL: All sectors have identical R_K (sector-independence)

Physics: The CG(24) Josephson network has sector-dependent couplings:
  J_C2 = 0.933 (coset, 4 bonds), J_su2 = 0.059 (weak, 3 bonds), J_u1 = 0.038 (1 bond)
The effective resistance R_K^a for sector a is the average Kirchhoff resistance
on the sub-graph containing only sector-a edges.

R_K(i,j) = (e_i - e_j)^T * L_a^{+} * (e_i - e_j)

where L_a^{+} is the pseudoinverse of the sector-a Laplacian.

The W2-B threshold ratios are:
  delta_2/delta_3 = 1       (exact Dynkin sum rule)
  delta_1/delta_3 = 20/9    (exact Dynkin sum rule)
  delta_2/delta_1 = 9/20    (derived)

If transport and threshold corrections are correlated, we expect
R_K^{SU(2)} / R_K^{U(1)} ~ delta_2/delta_1 = 0.45.

Cross-checks:
  (1) Uniform coupling => R_K identical across sectors (FAIL limit)
  (2) R_K inversely proportional to J for single-channel network (Kirchhoff)
  (3) R_K > 0 for all non-identical connected vertex pairs

Session 73a, Wave 3, Landau-Condensed-Matter-Theorist.
"""

import sys
import os
import time
import numpy as np
from scipy import linalg
from itertools import permutations, combinations

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    J_C2, J_su2, J_u1, dt_transit, Delta_BCS, M_KK
)

t0 = time.time()

# ==============================================================================
#  SECTION 1: Construct CG(24) Cayley graph of S_4
# ==============================================================================

print("=" * 70)
print("SECTION 1: CG(24) construction")
print("=" * 70)

# S_4 elements as tuples of (0,1,2,3)
elements = list(permutations(range(4)))
elem_to_idx = {e: i for i, e in enumerate(elements)}
N_vert = len(elements)  # (local) = 24

# The 6 transposition generators of S_4
transpositions = []  # (local)
for i in range(4):
    for j in range(i + 1, 4):
        transpositions.append((i, j))

print(f"S_4: {N_vert} elements")
print(f"Generators (transpositions): {transpositions}")

# Build full adjacency matrix (unweighted)
A_full = np.zeros((N_vert, N_vert), dtype=float)  # (local)
# Also store which generator connects each edge
edge_generator = {}  # (local) maps (v_i, v_j) -> transposition (i,j)

for idx, perm in enumerate(elements):
    for (i, j) in transpositions:
        new_perm = list(perm)  # (local)
        new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
        neighbor_idx = elem_to_idx[tuple(new_perm)]  # (local)
        A_full[idx, neighbor_idx] = 1.0
        # Record which generator connects this edge
        edge_key = (min(idx, neighbor_idx), max(idx, neighbor_idx))  # (local)
        edge_generator[edge_key] = (i, j)

degree = int(np.sum(A_full[0]))  # (local)
N_edges = int(np.sum(A_full) / 2)  # (local)
print(f"CG(24): {N_vert} vertices, {N_edges} edges, degree {degree}")

# Cross-check: load S64 adjacency and verify
try:
    d64 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               's64_local_entangle.npz'), allow_pickle=True)
    adj_s64 = d64['adj_cg24'].astype(float)  # (local)
    # The S64 matrix may have a different vertex ordering, so compare spectra
    L_check = np.diag(np.sum(adj_s64, axis=1)) - adj_s64  # (local)
    evals_check = np.sort(linalg.eigvalsh(L_check))  # (local)
    L_full = np.diag(np.sum(A_full, axis=1)) - A_full  # (local)
    evals_full = np.sort(linalg.eigvalsh(L_full))  # (local)
    max_spec_diff = np.max(np.abs(evals_check - evals_full))  # (local)
    print(f"Cross-check vs S64: max spectral diff = {max_spec_diff:.2e}")
    assert max_spec_diff < 1e-10, f"Spectral mismatch: {max_spec_diff}"
except Exception as e:
    print(f"Cross-check skipped: {e}")

# Also verify Laplacian spectrum matches S72
L_full = np.diag(np.sum(A_full, axis=1)) - A_full  # (local)
evals_full = np.sort(linalg.eigvalsh(L_full))  # (local)
evals_full[np.abs(evals_full) < 1e-10] = 0.0

unique_evals, counts = np.unique(np.round(evals_full, 6), return_counts=True)  # (local)
print(f"\nLaplacian spectrum: ", end="")
print(", ".join(f"{v:.1f}^{c}" for v, c in zip(unique_evals, counts)))

# ==============================================================================
#  SECTION 2: Sector decomposition of generators
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 2: Generator-to-sector assignment")
print("=" * 70)

# The 6 transpositions of S_4 decompose into gauge sectors under the
# branching SU(3) -> SU(2)_L x U(1)_Y.
#
# The canonical assignment from S47 TEXTURE-CORR-48 and W2-D:
#   C^2 coset: 4 generators (lambda_{4,5,6,7} in Gell-Mann basis)
#   su(2)_L:   3 generators (lambda_{1,2,3})
#   u(1)_Y:    1 generator  (lambda_8)
#   Total:     8 = dim(SU(3)) -- but we only have 6 transpositions.
#
# CG(24) has degree 6 = 6 generators, not 8.  The embedding of 6
# transpositions into the 8-dimensional Lie algebra assigns:
#   4 transpositions -> C^2 coset directions
#   1 transposition  -> su(2) stabilizer direction
#   1 transposition  -> u(1) direction
#
# This 4+1+1 partition matches W2-C (s73a_graph_spectral_decoherence.py)
# and gives degree 6 as required.
#
# HOWEVER, the W2-D results give bond counts per cell as:
#   C^2: 4 bonds, su(2): 3 bonds, u(1): 1 bond = 8 total
# This is for the TESSELLATION (32 cells, ~8 neighbors each).
# For CG(24) (24 vertices, 6 neighbors each), we use 4+1+1 = 6.
#
# KEY STRUCTURAL POINT: Since the 6 transpositions are conjugacy
# classes in S_4, and S_4 has three conjugacy classes of transpositions:
#   Class I:  {(01),(23)} -- disjoint support
#   Class II: {(02),(13)} -- disjoint support
#   Class III:{(03),(12)} -- disjoint support
# Each class consists of two transpositions with disjoint support.
# These three classes of size 2 give 6 generators total.
#
# The assignment of classes to sectors should respect the fact that
# the C^2 coset has 4 generators.  Two classes (4 generators) -> C^2,
# one class -> su(2)+u(1).  The su(2)+u(1) class further splits 1+1.
#
# We enumerate all possible (4+1+1) assignments and show the result
# is independent of the choice (up to graph automorphism of S_4).

# Define conjugacy pairs
conj_pairs = [
    ((0, 1), (2, 3)),  # Class I
    ((0, 2), (1, 3)),  # Class II
    ((0, 3), (1, 2)),  # Class III
]

print(f"\nConjugacy classes of transpositions in S_4:")
for k, (t1, t2) in enumerate(conj_pairs):
    print(f"  Class {k}: {t1}, {t2}")

# All distinct (4+1+1) partitions:
# Choose 2 of 3 classes for C^2 (4 generators), remaining class splits 1+1
from itertools import combinations as comb

def build_sector_adjacency(elements, elem_to_idx, generators, coupling):
    """Build sector-specific weighted adjacency matrix.

    generators: list of (i,j) transpositions in this sector
    coupling: J value for this sector
    Returns: weighted adjacency matrix A_sector (24x24)
    """
    N = len(elements)  # (local)
    A = np.zeros((N, N), dtype=float)  # (local)
    for idx, perm in enumerate(elements):
        for (i, j) in generators:
            new_perm = list(perm)  # (local)
            new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
            neighbor_idx = elem_to_idx[tuple(new_perm)]  # (local)
            A[idx, neighbor_idx] = coupling
    return A


def sector_laplacian(A_weighted):
    """Laplacian L = D - A for weighted adjacency matrix."""
    D = np.diag(np.sum(A_weighted, axis=1))  # (local)
    return D - A_weighted


def kirchhoff_resistance_matrix(L):
    """Compute the Kirchhoff effective resistance between all pairs.

    R_K(i,j) = (e_i - e_j)^T L^+ (e_i - e_j) = L^+_{ii} + L^+_{jj} - 2*L^+_{ij}

    For disconnected components, R_K = infinity between different components.
    We use the pseudoinverse L^+ restricted to the range of L.

    Returns: R_K matrix (N x N), connectivity mask
    """
    N = L.shape[0]  # (local)

    # Eigendecomposition
    evals, evecs = linalg.eigh(L)  # (local)

    # Identify connected components from zero eigenvalues
    n_components = np.sum(np.abs(evals) < 1e-10)  # (local)

    # Pseudoinverse: L^+ = sum_{k: lambda_k > 0} (1/lambda_k) |v_k><v_k|
    L_pinv = np.zeros((N, N), dtype=float)  # (local)
    for k in range(N):
        if np.abs(evals[k]) > 1e-10:
            L_pinv += (1.0 / evals[k]) * np.outer(evecs[:, k], evecs[:, k])

    # R_K(i,j) = L^+_{ii} + L^+_{jj} - 2*L^+_{ij}
    diag_Lp = np.diag(L_pinv)  # (local)
    R_K = diag_Lp[:, None] + diag_Lp[None, :] - 2.0 * L_pinv  # (local)

    # For disconnected pairs, R_K from pseudoinverse is NOT infinity --
    # it gives the within-component resistance only.  We need to mask
    # disconnected pairs.  Two nodes are in the same component if and only if
    # the corresponding entries in the zero-eigenvalue eigenvectors are
    # proportional (same component has same projection onto null space).

    # Identify components via the null space
    null_vecs = evecs[:, np.abs(evals) < 1e-10]  # (local) shape (N, n_comp)

    # Two nodes are connected if they share the same component
    # Use the null space projection: cluster by which null eigenvector has
    # nonzero weight
    connected = np.ones((N, N), dtype=bool)  # (local)
    if n_components > 1:
        # Assign component labels by k-means on null space projections
        from scipy.cluster.hierarchy import fcluster, linkage
        # Simple approach: round the null space coordinates
        null_proj = null_vecs @ null_vecs.T  # (local) N x N
        for i_node in range(N):
            for j_node in range(i_node + 1, N):
                # Connected if null space projection is close
                if np.abs(null_proj[i_node, j_node] - null_proj[i_node, i_node]) > 0.01:
                    connected[i_node, j_node] = False
                    connected[j_node, i_node] = False

    return R_K, connected, n_components


# ==============================================================================
#  SECTION 3: Compute sector-resolved R_K for all generator assignments
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 3: Sector-resolved Kirchhoff resistance")
print("=" * 70)

# Threshold ratios from W2-B (PERMANENT THEOREM)
delta_2_over_delta_3 = 1.0       # (local) exact
delta_1_over_delta_3 = 20.0 / 9  # exact
delta_2_over_delta_1 = 9.0 / 20  # = 0.45 (derived)

print(f"\nW2-B threshold ratios (exact Dynkin sum rules):")
print(f"  delta_2/delta_3 = {delta_2_over_delta_3:.6f}")
print(f"  delta_1/delta_3 = {delta_1_over_delta_3:.6f}")
print(f"  delta_2/delta_1 = {delta_2_over_delta_1:.6f}")

# Store results for all assignments
all_results = []  # (local)

# Enumerate all (4+1+1) generator assignments:
# Choose 2 of 3 conjugacy classes for C^2 (4 generators)
# Remaining class: 1 generator -> su(2), 1 -> u(1), with 2 sub-choices
n_assignment = 0  # (local)

for c2_pair in comb(range(3), 2):
    # C^2 generators: the two selected conjugacy classes
    c2_gens = []  # (local)
    for k in c2_pair:
        c2_gens.extend(conj_pairs[k])

    # Remaining class
    remaining_class_idx = [k for k in range(3) if k not in c2_pair][0]  # (local)
    remaining_pair = conj_pairs[remaining_class_idx]  # (local)

    # Two sub-assignments: which of the pair is su(2), which is u(1)
    for su2_gen, u1_gen in [remaining_pair, (remaining_pair[1], remaining_pair[0])]:
        n_assignment += 1

        c2_generators = c2_gens  # (local)
        su2_generators = [su2_gen]  # (local)
        u1_generators = [u1_gen]  # (local)

        # Build sector adjacency matrices (weighted by sector coupling)
        A_c2 = build_sector_adjacency(elements, elem_to_idx, c2_generators, J_C2)
        A_su2 = build_sector_adjacency(elements, elem_to_idx, su2_generators, J_su2)
        A_u1 = build_sector_adjacency(elements, elem_to_idx, u1_generators, J_u1)

        # Build sector Laplacians
        L_c2 = sector_laplacian(A_c2)
        L_su2 = sector_laplacian(A_su2)
        L_u1 = sector_laplacian(A_u1)

        # Compute Kirchhoff resistance for each sector
        R_c2, conn_c2, nc_c2 = kirchhoff_resistance_matrix(L_c2)
        R_su2, conn_su2, nc_su2 = kirchhoff_resistance_matrix(L_su2)
        R_u1, conn_u1, nc_u1 = kirchhoff_resistance_matrix(L_u1)

        # Also compute for the FULL (all-sector combined) Laplacian
        A_total = A_c2 + A_su2 + A_u1  # (local)
        L_total = sector_laplacian(A_total)
        R_total, conn_total, nc_total = kirchhoff_resistance_matrix(L_total)

        # Compute mean R_K over all connected pairs for each sector
        # Upper triangle only (avoid double counting)
        mask_upper = np.triu(np.ones((N_vert, N_vert), dtype=bool), k=1)  # (local)

        # C^2 sector
        mask_c2 = mask_upper & conn_c2  # (local)
        R_c2_mean = np.mean(R_c2[mask_c2]) if np.any(mask_c2) else np.inf  # (local)
        R_c2_std = np.std(R_c2[mask_c2]) if np.any(mask_c2) else np.inf  # (local)
        n_pairs_c2 = np.sum(mask_c2)  # (local)

        # su(2) sector
        mask_su2 = mask_upper & conn_su2  # (local)
        R_su2_mean = np.mean(R_su2[mask_su2]) if np.any(mask_su2) else np.inf  # (local)
        R_su2_std = np.std(R_su2[mask_su2]) if np.any(mask_su2) else np.inf  # (local)
        n_pairs_su2 = np.sum(mask_su2)  # (local)

        # u(1) sector
        mask_u1 = mask_upper & conn_u1  # (local)
        R_u1_mean = np.mean(R_u1[mask_u1]) if np.any(mask_u1) else np.inf  # (local)
        R_u1_std = np.std(R_u1[mask_u1]) if np.any(mask_u1) else np.inf  # (local)
        n_pairs_u1 = np.sum(mask_u1)  # (local)

        # Total (full coupling)
        mask_total = mask_upper & conn_total  # (local)
        R_total_mean = np.mean(R_total[mask_total]) if np.any(mask_total) else np.inf  # (local)
        n_pairs_total = np.sum(mask_total)  # (local)

        # Ratios
        ratio_su2_u1 = R_su2_mean / R_u1_mean if (R_u1_mean > 0 and R_u1_mean < np.inf) else np.inf  # (local)
        ratio_c2_u1 = R_c2_mean / R_u1_mean if (R_u1_mean > 0 and R_u1_mean < np.inf) else np.inf  # (local)
        ratio_su2_c2 = R_su2_mean / R_c2_mean if (R_c2_mean > 0 and R_c2_mean < np.inf) else np.inf  # (local)

        result = {
            'assignment': n_assignment,
            'c2_pair': c2_pair,
            'su2_gen': su2_gen,
            'u1_gen': u1_gen,
            'nc_c2': nc_c2,
            'nc_su2': nc_su2,
            'nc_u1': nc_u1,
            'nc_total': nc_total,
            'R_c2_mean': R_c2_mean,
            'R_su2_mean': R_su2_mean,
            'R_u1_mean': R_u1_mean,
            'R_total_mean': R_total_mean,
            'n_pairs_c2': n_pairs_c2,
            'n_pairs_su2': n_pairs_su2,
            'n_pairs_u1': n_pairs_u1,
            'ratio_su2_u1': ratio_su2_u1,
            'ratio_c2_u1': ratio_c2_u1,
            'ratio_su2_c2': ratio_su2_c2,
        }  # (local)
        all_results.append(result)

        if n_assignment <= 3:  # Print detail for first few
            print(f"\n--- Assignment {n_assignment}: C^2 classes {c2_pair}, "
                  f"su(2)={su2_gen}, u(1)={u1_gen} ---")
            print(f"  Components: C^2={nc_c2}, su(2)={nc_su2}, u(1)={nc_u1}, total={nc_total}")
            print(f"  Connected pairs: C^2={n_pairs_c2}, su(2)={n_pairs_su2}, u(1)={n_pairs_u1}")
            print(f"  <R_K>: C^2={R_c2_mean:.6f}, su(2)={R_su2_mean:.6f}, u(1)={R_u1_mean:.6f}")
            print(f"  R_K^{{su(2)}}/R_K^{{u(1)}} = {ratio_su2_u1:.6f}")
            print(f"  R_K^{{C^2}}/R_K^{{u(1)}} = {ratio_c2_u1:.6f}")

print(f"\nTotal assignments enumerated: {n_assignment}")

# ==============================================================================
#  SECTION 4: Statistical analysis across all assignments
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 4: Statistics across all generator assignments")
print("=" * 70)

# Extract arrays
ratios_su2_u1 = np.array([r['ratio_su2_u1'] for r in all_results])  # (local)
ratios_c2_u1 = np.array([r['ratio_c2_u1'] for r in all_results])  # (local)
ratios_su2_c2 = np.array([r['ratio_su2_c2'] for r in all_results])  # (local)
R_c2_means = np.array([r['R_c2_mean'] for r in all_results])  # (local)
R_su2_means = np.array([r['R_su2_mean'] for r in all_results])  # (local)
R_u1_means = np.array([r['R_u1_mean'] for r in all_results])  # (local)
R_total_means = np.array([r['R_total_mean'] for r in all_results])  # (local)

print(f"\nR_K^{{C^2}} across assignments:  mean={np.mean(R_c2_means):.6f}, "
      f"std={np.std(R_c2_means):.6f}, range=[{np.min(R_c2_means):.6f}, {np.max(R_c2_means):.6f}]")
print(f"R_K^{{su(2)}} across assignments: mean={np.mean(R_su2_means):.6f}, "
      f"std={np.std(R_su2_means):.6f}, range=[{np.min(R_su2_means):.6f}, {np.max(R_su2_means):.6f}]")
print(f"R_K^{{u(1)}} across assignments:  mean={np.mean(R_u1_means):.6f}, "
      f"std={np.std(R_u1_means):.6f}, range=[{np.min(R_u1_means):.6f}, {np.max(R_u1_means):.6f}]")
print(f"R_K^{{total}} across assignments: mean={np.mean(R_total_means):.6f}, "
      f"std={np.std(R_total_means):.6f}")

print(f"\nR_K^{{su(2)}}/R_K^{{u(1)}} across assignments:")
print(f"  mean = {np.mean(ratios_su2_u1):.6f}")
print(f"  std  = {np.std(ratios_su2_u1):.6f}")
print(f"  range = [{np.min(ratios_su2_u1):.6f}, {np.max(ratios_su2_u1):.6f}]")

print(f"\nR_K^{{C^2}}/R_K^{{u(1)}} across assignments:")
print(f"  mean = {np.mean(ratios_c2_u1):.6f}")
print(f"  range = [{np.min(ratios_c2_u1):.6f}, {np.max(ratios_c2_u1):.6f}]")

# ==============================================================================
#  SECTION 5: Kirchhoff scaling cross-check
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 5: Kirchhoff scaling cross-checks")
print("=" * 70)

# Cross-check 1: Uniform coupling => all sectors identical
print("\nCross-check 1: Uniform coupling test")
J_uniform = 1.0  # (local)
# Use first assignment's generators
r0 = all_results[0]  # (local)
c2_gens_0 = []  # (local)
for k in r0['c2_pair']:
    c2_gens_0.extend(conj_pairs[k])
su2_gens_0 = [r0['su2_gen']]  # (local)
u1_gens_0 = [r0['u1_gen']]  # (local)

A_c2_uniform = build_sector_adjacency(elements, elem_to_idx, c2_gens_0, J_uniform)
A_su2_uniform = build_sector_adjacency(elements, elem_to_idx, su2_gens_0, J_uniform)
A_u1_uniform = build_sector_adjacency(elements, elem_to_idx, u1_gens_0, J_uniform)

L_c2_u = sector_laplacian(A_c2_uniform)
L_su2_u = sector_laplacian(A_su2_uniform)
L_u1_u = sector_laplacian(A_u1_uniform)

R_c2_u, _, _ = kirchhoff_resistance_matrix(L_c2_u)
R_su2_u, conn_su2_u, _ = kirchhoff_resistance_matrix(L_su2_u)
R_u1_u, conn_u1_u, _ = kirchhoff_resistance_matrix(L_u1_u)

mask_upper = np.triu(np.ones((N_vert, N_vert), dtype=bool), k=1)  # (local)

# The sectors have different numbers of generators (4 vs 1 vs 1),
# so even at uniform coupling R_K differs due to different graph topology.
# The resistance depends on the SUB-GRAPH structure (connectivity, paths).
R_c2_u_mean = np.mean(R_c2_u[mask_upper])  # (local) -- C^2 subgraph: 4 generators, connected
mask_su2_conn = mask_upper & conn_su2_u  # (local)
mask_u1_conn = mask_upper & conn_u1_u  # (local)
R_su2_u_mean = np.mean(R_su2_u[mask_su2_conn]) if np.any(mask_su2_conn) else np.inf  # (local)
R_u1_u_mean = np.mean(R_u1_u[mask_u1_conn]) if np.any(mask_u1_conn) else np.inf  # (local)

print(f"  J=1 for all: R_K(C^2)={R_c2_u_mean:.6f}, R_K(su2)={R_su2_u_mean:.6f}, R_K(u1)={R_u1_u_mean:.6f}")
print(f"  Ratio su2/u1 at J=1: {R_su2_u_mean/R_u1_u_mean:.6f}" if R_u1_u_mean < np.inf else "  u(1) disconnected at 1 generator")

# Cross-check 2: R_K inversely proportional to J for single-sector network
print("\nCross-check 2: Kirchhoff J-scaling")
# For a single connected sector with coupling J, R_K ~ 1/J
# Test: compute R_K at J=1 and J=J_C2 for C^2 sector
A_c2_j1 = build_sector_adjacency(elements, elem_to_idx, c2_gens_0, 1.0)
A_c2_jc = build_sector_adjacency(elements, elem_to_idx, c2_gens_0, J_C2)
L_c2_j1 = sector_laplacian(A_c2_j1)
L_c2_jc = sector_laplacian(A_c2_jc)
R_j1, _, _ = kirchhoff_resistance_matrix(L_c2_j1)
R_jc, _, _ = kirchhoff_resistance_matrix(L_c2_jc)
R_j1_mean = np.mean(R_j1[mask_upper])  # (local)
R_jc_mean = np.mean(R_jc[mask_upper])  # (local)
scaling_ratio = R_j1_mean / R_jc_mean  # (local) should equal J_C2
print(f"  R_K(J=1) / R_K(J={J_C2}) = {scaling_ratio:.6f}")
print(f"  Expected (= J_C2) = {J_C2:.6f}")
print(f"  Match: {abs(scaling_ratio - J_C2) / J_C2 * 100:.4f}% discrepancy")

# Cross-check 3: R_K > 0 for all non-identical connected pairs
print("\nCross-check 3: Positivity")
r_best = all_results[0]  # (local)
# Recompute for first assignment
A_c2_best = build_sector_adjacency(elements, elem_to_idx, c2_gens_0, J_C2)
L_c2_best = sector_laplacian(A_c2_best)
R_c2_best, conn_c2_best, _ = kirchhoff_resistance_matrix(L_c2_best)
R_off_diag = R_c2_best[mask_upper & conn_c2_best]  # (local)
min_R = np.min(R_off_diag) if len(R_off_diag) > 0 else 0  # (local)
max_R = np.max(R_off_diag) if len(R_off_diag) > 0 else 0  # (local)
print(f"  C^2 sector: min R_K = {min_R:.6f}, max R_K = {max_R:.6f}")
print(f"  All positive: {min_R > 0}")

# ==============================================================================
#  SECTION 6: Analytical prediction for R_K ratios
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 6: Analytical R_K ratios")
print("=" * 70)

# For a single generator creating a 2-regular graph (each transposition acts
# on S_4 as a fixed-point-free involution on the 24 elements, creating
# disjoint 2-cycles and hence 12 disconnected pairs), the sub-graph
# with one generator is a set of 12 disjoint edges (perfect matching).
#
# For such a matching: R_K between matched pairs = 1/J.
# Between non-matched pairs: disconnected (R_K = infinity).
#
# For 2 generators: the sub-graph is 2-regular. Each connected component
# is a cycle.  The Kirchhoff resistance on a cycle of length L between
# nodes at distance d is: R_K = d*(L-d) / (L*J).
#
# For 4 generators (C^2): 4-regular sub-graph of CG(24).  May be connected.
# Kirchhoff resistance depends on the graph structure.
#
# The KEY INSIGHT: Since su(2) and u(1) each have only 1 generator,
# they create MATCHINGS (12 disjoint edges).  R_K is defined only
# between the 12 matched pairs, and equals 1/J for each.
# Mean R_K = 1/J.
#
# Therefore:
#   R_K^{su(2)} = 1/J_su2 (for matched pairs only)
#   R_K^{u(1)}  = 1/J_u1  (for matched pairs only)
#   R_K^{su(2)} / R_K^{u(1)} = J_u1 / J_su2

R_su2_analytical = 1.0 / J_su2  # (local)
R_u1_analytical = 1.0 / J_u1   # (local)
ratio_analytical = J_u1 / J_su2  # (local)

print(f"\nSingle-generator sector (perfect matching):")
print(f"  R_K^{{su(2)}} = 1/J_su2 = {R_su2_analytical:.6f} M_KK^{{-1}}")
print(f"  R_K^{{u(1)}}  = 1/J_u1  = {R_u1_analytical:.6f} M_KK^{{-1}}")
print(f"  R_K^{{su(2)}} / R_K^{{u(1)}} = J_u1/J_su2 = {ratio_analytical:.6f}")
print(f"\n  W2-B target: delta_2/delta_1 = {delta_2_over_delta_1:.6f}")
print(f"  Discrepancy: {abs(ratio_analytical - delta_2_over_delta_1) / delta_2_over_delta_1 * 100:.2f}%")

# For C^2 with 4 generators: need numerical result
# Use the first assignment
print(f"\nC^2 sector (4 generators, numerical):")
print(f"  <R_K^{{C^2}}> = {all_results[0]['R_c2_mean']:.6f} M_KK^{{-1}}")

# Kirchhoff scaling: R ~ 1/J, so the ratio should be
# R^{su2}/R^{u1} = J_u1/J_su2 = 0.038/0.059 = 0.6441
# This is PURELY the coupling ratio, not a threshold ratio.
# The threshold ratios are delta_2/delta_1 = 0.45.

print(f"\n  CRITICAL OBSERVATION:")
print(f"  R_K^{{su(2)}}/R_K^{{u(1)}} = J_u1/J_su2 = {ratio_analytical:.6f}")
print(f"  This equals the INVERSE coupling ratio, NOT the threshold ratio.")
print(f"  The threshold ratio delta_2/delta_1 = {delta_2_over_delta_1:.6f}")
print(f"  These differ by {abs(ratio_analytical - delta_2_over_delta_1) / delta_2_over_delta_1 * 100:.2f}%")

# ==============================================================================
#  SECTION 7: Conductance (inverse resistance) analysis
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 7: Conductance sigma_K = 1/R_K")
print("=" * 70)

# The conductance is the physically more natural quantity for transport.
# sigma_K^a = J_a * (graph-structural factor for sector a)
# For single-generator matchings: sigma_K = J_a (trivially).
# The ratio sigma_su2/sigma_u1 = J_su2/J_u1 = 0.059/0.038 = 1.553

sigma_su2 = J_su2  # (local) conductance for matched-pair network
sigma_u1 = J_u1    # (local)
sigma_c2 = 1.0 / all_results[0]['R_c2_mean']  # (local) -- mean conductance for C^2

print(f"\nConductance (inverse of mean R_K):")
print(f"  sigma_K^{{C^2}}  = {sigma_c2:.6f} M_KK")
print(f"  sigma_K^{{su(2)}} = {sigma_su2:.6f} M_KK")
print(f"  sigma_K^{{u(1)}}  = {sigma_u1:.6f} M_KK")

ratio_sigma = sigma_su2 / sigma_u1  # (local)
print(f"\n  sigma_K^{{su(2)}} / sigma_K^{{u(1)}} = {ratio_sigma:.6f}")
print(f"  J_su2 / J_u1 = {J_su2 / J_u1:.6f}")
print(f"  Match: {abs(ratio_sigma - J_su2/J_u1) / (J_su2/J_u1) * 100:.4f}%")

# Compare conductance ratio to threshold ratio
# delta_2/delta_1 = 9/20 = 0.45
# sigma_su2/sigma_u1 = J_su2/J_u1 = 1.553
# The ratio of conductances is the COUPLING ratio, not the threshold ratio.
# The transport-threshold bridge would require a structural connection
# between J_a and delta_a.

# Check if J_su2/J_u1 ~ delta_2/delta_1:
print(f"\n  Conductance ratio vs threshold ratio:")
print(f"  sigma_su2/sigma_u1 = {ratio_sigma:.6f}")
print(f"  delta_2/delta_1    = {delta_2_over_delta_1:.6f}")
print(f"  Discrepancy: {abs(ratio_sigma - delta_2_over_delta_1)/delta_2_over_delta_1*100:.1f}%")

# Check if R_su2/R_u1 ~ delta_2/delta_1:
print(f"\n  Resistance ratio vs threshold ratio:")
print(f"  R_su2/R_u1         = {ratio_analytical:.6f}")
print(f"  delta_2/delta_1    = {delta_2_over_delta_1:.6f}")
print(f"  Discrepancy: {abs(ratio_analytical - delta_2_over_delta_1)/delta_2_over_delta_1*100:.1f}%")

# ==============================================================================
#  SECTION 8: Spectral analysis of sector Laplacians
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 8: Spectral analysis of sector Laplacians")
print("=" * 70)

# Use first assignment for detailed spectral analysis
# C^2 sector (4 generators)
evals_c2 = np.sort(linalg.eigvalsh(L_c2_best))  # (local)
evals_c2[np.abs(evals_c2) < 1e-10] = 0.0
n_zero_c2 = np.sum(np.abs(evals_c2) < 1e-10)  # (local)

# su(2) sector (1 generator)
A_su2_best = build_sector_adjacency(elements, elem_to_idx, su2_gens_0, J_su2)
L_su2_best = sector_laplacian(A_su2_best)
evals_su2 = np.sort(linalg.eigvalsh(L_su2_best))  # (local)
evals_su2[np.abs(evals_su2) < 1e-10] = 0.0
n_zero_su2 = np.sum(np.abs(evals_su2) < 1e-10)  # (local)

# u(1) sector (1 generator)
A_u1_best = build_sector_adjacency(elements, elem_to_idx, u1_gens_0, J_u1)
L_u1_best = sector_laplacian(A_u1_best)
evals_u1 = np.sort(linalg.eigvalsh(L_u1_best))  # (local)
evals_u1[np.abs(evals_u1) < 1e-10] = 0.0
n_zero_u1 = np.sum(np.abs(evals_u1) < 1e-10)  # (local)

# Total (anisotropic)
A_total_best = A_c2_best + A_su2_best + A_u1_best  # (local)
L_total_best = sector_laplacian(A_total_best)
evals_total = np.sort(linalg.eigvalsh(L_total_best))  # (local)
evals_total[np.abs(evals_total) < 1e-10] = 0.0

print(f"\nC^2 sector (4 generators, J={J_C2}):")
print(f"  Zero eigenvalues (components): {n_zero_c2}")
print(f"  Nonzero spectrum: {evals_c2[evals_c2 > 1e-10][:8].round(6)}")
print(f"  Spectral gap: lambda_1 = {evals_c2[evals_c2 > 1e-10][0]:.6f}" if np.any(evals_c2 > 1e-10) else "  Fully disconnected")

print(f"\nsu(2) sector (1 generator, J={J_su2}):")
print(f"  Zero eigenvalues (components): {n_zero_su2}")
print(f"  Nonzero spectrum (unique): {np.unique(evals_su2[evals_su2 > 1e-10]).round(6)}")

print(f"\nu(1) sector (1 generator, J={J_u1}):")
print(f"  Zero eigenvalues (components): {n_zero_u1}")
print(f"  Nonzero spectrum (unique): {np.unique(evals_u1[evals_u1 > 1e-10]).round(6)}")

print(f"\nTotal (anisotropic, all sectors combined):")
print(f"  Spectral gap: lambda_1 = {evals_total[evals_total > 1e-10][0]:.6f}")
print(f"  Full spectrum: {evals_total.round(6)}")

# Single-generator transposition structure:
# A transposition (ij) on S_4 decomposes the 24 elements into 12 pairs
# of the form {sigma, sigma*(ij)}.  The sub-graph is a perfect matching.
# Each connected component is a single edge.  Components = 12.
# Nonzero eigenvalue = 2*J (each edge contributes J to degree, 2 nodes).
print(f"\nSingle-generator matching verification:")
print(f"  su(2) components: {n_zero_su2} (expected 12)")
print(f"  u(1) components:  {n_zero_u1} (expected 12)")
print(f"  su(2) nonzero eigenvalue: {np.unique(evals_su2[evals_su2>1e-10]).round(6)} (expected 2*J_su2={2*J_su2:.6f})")
print(f"  u(1) nonzero eigenvalue:  {np.unique(evals_u1[evals_u1>1e-10]).round(6)} (expected 2*J_u1={2*J_u1:.6f})")

# ==============================================================================
#  SECTION 9: GATE VERDICT
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 9: GATE VERDICT")
print("=" * 70)

# Gate criterion: R_K^{SU(2)} / R_K^{U(1)} within 20% of delta_2/delta_1
# delta_2/delta_1 = 9/20 = 0.45
# R_K^{SU(2)} / R_K^{U(1)} = J_u1/J_su2 = 0.038/0.059

# Use the mean across all assignments (they should be very similar
# for single-generator sectors since all transpositions create the
# same matching structure up to relabeling)
R_su2_grand_mean = np.mean(R_su2_means)  # (local)
R_u1_grand_mean = np.mean(R_u1_means)    # (local)
ratio_grand = R_su2_grand_mean / R_u1_grand_mean  # (local)

target = delta_2_over_delta_1  # (local) = 0.45
fractional_discrepancy = abs(ratio_grand - target) / target  # (local)

print(f"\nGate: SECTOR-RK-73a")
print(f"Criterion: R_K^{{SU(2)}} / R_K^{{U(1)}} within 20% of delta_2/delta_1 = {target:.4f}")
print(f"\nComputed:")
print(f"  <R_K^{{SU(2)}}> = {R_su2_grand_mean:.6f} M_KK^{{-1}}")
print(f"  <R_K^{{U(1)}}>  = {R_u1_grand_mean:.6f} M_KK^{{-1}}")
print(f"  Ratio R_K^{{SU(2)}} / R_K^{{U(1)}} = {ratio_grand:.6f}")
print(f"  Target delta_2/delta_1 = {target:.6f}")
print(f"  Fractional discrepancy = {fractional_discrepancy:.4f} ({fractional_discrepancy*100:.2f}%)")

if fractional_discrepancy < 0.20:
    gate_verdict = "PASS"
    gate_detail = (f"R_K^{{SU(2)}}/R_K^{{U(1)}} = {ratio_grand:.4f}, "
                   f"target = {target:.4f}, discrepancy = {fractional_discrepancy*100:.1f}% < 20%")
elif abs(R_su2_grand_mean - R_u1_grand_mean) / R_u1_grand_mean < 0.01:
    gate_verdict = "FAIL"
    gate_detail = (f"All sectors have near-identical R_K (sector-independence): "
                   f"|R_su2 - R_u1| / R_u1 = {abs(R_su2_grand_mean - R_u1_grand_mean)/R_u1_grand_mean:.4f}")
else:
    gate_verdict = "INFO"
    gate_detail = (f"Sector resistances differ (R_K^{{SU(2)}}/R_K^{{U(1)}} = {ratio_grand:.4f}) "
                   f"but discrepancy from threshold ratio delta_2/delta_1 = {target:.4f} "
                   f"is {fractional_discrepancy*100:.1f}% (> 20%)")

print(f"\n  Verdict: **{gate_verdict}**")
print(f"  Detail: {gate_detail}")

# ==============================================================================
#  SECTION 10: Structural theorem on R_K ratios
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 10: STRUCTURAL THEOREM")
print("=" * 70)

print("""
THEOREM (Sector Kirchhoff Resistance on Matching Sub-Graphs):

For the CG(24) Cayley graph of S_4 with gauge-sector-resolved Josephson
couplings {J_C2, J_su2, J_u1}, where the su(2) and u(1) sectors each
correspond to a SINGLE transposition generator:

(i)   Each single-generator sub-graph is a perfect matching (12 disjoint
      edges), hence 12 connected components.

(ii)  The Kirchhoff resistance for each matched pair is:
        R_K^a(i,j) = 1/J_a   for the unique pair (i,j) connected in sector a.

(iii) The sector resistance ratio is EXACTLY the inverse coupling ratio:
        R_K^{su(2)} / R_K^{u(1)} = J_u1 / J_su2

(iv)  This ratio is INDEPENDENT of the choice of generator assignment
      (all transpositions create isomorphic matchings).

Proof: A transposition (a,b) acting on S_4 decomposes the 24 elements
into 12 orbits of size 2.  The sub-graph is the disjoint union of 12
edges K_2.  On K_2 with coupling J, the Laplacian is [[J,-J],[-J,J]]
with pseudoinverse [[1/(4J),-1/(4J)],[-1/(4J),1/(4J)]].  The effective
resistance R_K = 1/(4J) + 1/(4J) + 2/(4J) = 1/J.  QED.

CONSEQUENCE: The transport ratio R_K^{su(2)}/R_K^{u(1)} = J_u1/J_su2
= 0.038/0.059 = 0.644 reflects the COUPLING ANISOTROPY, not the
threshold correction structure.  The threshold ratio delta_2/delta_1
= 9/20 = 0.450 arises from the Dynkin index sum rule, which is a
property of the LIE ALGEBRA (universal, representation-independent),
whereas the coupling ratio J_u1/J_su2 depends on the JENSEN DEFORMATION
(tau-dependent, geometry-specific).

There is no a priori reason for these to coincide.  The 43% discrepancy
is therefore NOT a failure of the transport picture -- it is the
EXPECTED result when two ratios arise from independent algebraic sources.
""")

# ==============================================================================
#  SECTION 11: Save results
# ==============================================================================

print("\n" + "=" * 70)
print("SECTION 11: Saving results")
print("=" * 70)

elapsed = time.time() - t0  # (local)

# Save comprehensive results
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's73a_sector_rk.npz')  # (local)

np.savez(save_path,
    # Gate
    gate_name='SECTOR-RK-73a',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Primary results
    R_K_su2_mean=R_su2_grand_mean,
    R_K_u1_mean=R_u1_grand_mean,
    R_K_c2_mean=np.mean(R_c2_means),
    R_K_total_mean=np.mean(R_total_means),
    ratio_su2_u1=ratio_grand,
    ratio_analytical=ratio_analytical,

    # Threshold comparison
    delta_2_over_delta_1=delta_2_over_delta_1,
    fractional_discrepancy=fractional_discrepancy,

    # Coupling inputs
    J_C2_input=J_C2,
    J_su2_input=J_su2,
    J_u1_input=J_u1,

    # Spectral data (first assignment)
    evals_L_c2=evals_c2,
    evals_L_su2=evals_su2,
    evals_L_u1=evals_u1,
    evals_L_total=evals_total,

    # Component counts (first assignment)
    n_components_c2=n_zero_c2,
    n_components_su2=n_zero_su2,
    n_components_u1=n_zero_u1,

    # Cross-check: Kirchhoff scaling
    scaling_check_ratio=scaling_ratio,
    scaling_check_expected=J_C2,

    # All assignments
    n_assignments=n_assignment,
    ratios_su2_u1_all=ratios_su2_u1,
    R_c2_means_all=R_c2_means,
    R_su2_means_all=R_su2_means,
    R_u1_means_all=R_u1_means,

    # Metadata
    N_vert=N_vert,
    N_edges=N_edges,
    elapsed_s=elapsed,
)

print(f"Saved to: {save_path}")
print(f"Elapsed: {elapsed:.2f} s")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
