#!/usr/bin/env python3
"""
S73a W2-C: Graph-Spectral Decoherence on CG(24)
=================================================
Gate: GRAPH-SPECTRAL-DECOHERENCE-73a
  PASS: t_dec/t_transit in [0.57, 0.88]
  INFO: t_dec/t_transit computed but outside [0.57, 0.88]
  FAIL: t_dec < 0.1 * t_transit (over-decohered) or > 5 (irrelevant)

Physics: The BCS inter-cell phase equilibration rate is controlled by the
graph Laplacian spectral gap lambda_1 of CG(24), NOT the Euclidean cell
diameter.  On a 6-regular Ramanujan graph with 24 vertices, lambda_1 = 4.

The phase diffusion equation on the graph:
    d(phi_i)/dt = -J_eff * sum_{j~i} (phi_i - phi_j) = -J_eff * (L*phi)_i

Solution: phi_i(t) = sum_k c_k * v_k * exp(-J_eff * lambda_k * t)
Decoherence timescale: t_dec = 1 / (J_eff * lambda_1)

The aggregate decoherence includes ALL Laplacian modes, not just lambda_1.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy import linalg
from canonical_constants import (
    J_C2, J_su2, J_u1, dt_transit, c_fabric, T_acoustic,
    N_cells, Delta_0_GL, Delta_0_OES, omega_L1
)

# ============================================================================
#  SECTION 1: Construct CG(24) and compute Laplacian spectrum
# ============================================================================

def cayley_graph_S4():
    """Construct the Cayley graph of S_4 with transposition generators.

    S_4 has 24 elements.  The 6 transpositions (ij) for 1<=i<j<=4 generate S_4.
    The Cayley graph has 24 vertices (group elements) and each vertex has
    degree 6 (one edge per transposition generator).  Since transpositions are
    self-inverse, all edges are undirected.

    Returns: adjacency matrix A (24x24), list of permutations as tuples
    """
    from itertools import permutations

    # All 24 elements of S_4 as tuples
    elements = list(permutations(range(4)))
    elem_to_idx = {e: i for i, e in enumerate(elements)}
    N = len(elements)  # (local)

    # The 6 transposition generators: (01),(02),(03),(12),(13),(23)
    transpositions = []  # (local)
    for i in range(4):
        for j in range(i+1, 4):
            transpositions.append((i, j))

    # Build adjacency matrix
    A = np.zeros((N, N), dtype=float)  # (local)
    for idx, perm in enumerate(elements):
        for (i, j) in transpositions:
            # Apply transposition to permutation
            new_perm = list(perm)  # (local)
            new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
            neighbor_idx = elem_to_idx[tuple(new_perm)]  # (local)
            A[idx, neighbor_idx] = 1.0

    return A, elements


def graph_laplacian(A):
    """Compute L = D - A where D = diag(degree vector)."""
    D = np.diag(np.sum(A, axis=1))  # (local)
    return D - A


def normalized_laplacian(A):
    """Compute L_norm = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}."""
    d = np.sum(A, axis=1)  # (local)
    d_inv_sqrt = 1.0 / np.sqrt(d)  # (local)
    D_inv_sqrt = np.diag(d_inv_sqrt)  # (local)
    return np.eye(len(d)) - D_inv_sqrt @ A @ D_inv_sqrt


# Build CG(24)
A_cg24, elements_S4 = cayley_graph_S4()
N_vert = A_cg24.shape[0]  # (local)
degree = int(np.sum(A_cg24[0]))  # (local)
N_edges = int(np.sum(A_cg24) / 2)  # (local)

print(f"CG(24): {N_vert} vertices, {N_edges} edges, degree {degree}")

# Laplacian and its spectrum
L_cg24 = graph_laplacian(A_cg24)  # (local)
evals_L, evecs_L = linalg.eigh(L_cg24)  # (local)

# Clean numerical zeros
evals_L[np.abs(evals_L) < 1e-10] = 0.0

print(f"\nLaplacian spectrum:")
# Group by unique eigenvalues
unique_evals, counts = np.unique(np.round(evals_L, 8), return_counts=True)  # (local)
for val, cnt in zip(unique_evals, counts):
    print(f"  lambda = {val:.4f}  (degeneracy {cnt})")

lambda_1 = evals_L[evals_L > 1e-10][0]  # (local) -- first nonzero eigenvalue
lambda_max = evals_L[-1]  # (local)
print(f"\nlambda_1 (spectral gap) = {lambda_1:.6f}")
print(f"lambda_max = {lambda_max:.6f}")
print(f"lambda_max / lambda_1 = {lambda_max / lambda_1:.4f}")

# Ramanujan bound check: lambda_1 >= d - 2*sqrt(d-1)
ramanujan_bound = degree - 2 * np.sqrt(degree - 1)  # (local)
print(f"\nRamanujan bound: lambda_1 >= {ramanujan_bound:.4f}")
print(f"CG(24) lambda_1 = {lambda_1:.4f} >= {ramanujan_bound:.4f}: "
      f"{'RAMANUJAN' if lambda_1 >= ramanujan_bound - 1e-10 else 'NOT RAMANUJAN'}")

# Cross-check: verify against S72 stored eigenvalues
data_s72 = np.load(os.path.join(os.path.dirname(__file__), 's72_island_graph.npz'),
                    allow_pickle=True)
evals_s72 = data_s72['evals_L']  # (local)
max_diff = np.max(np.abs(np.sort(evals_L) - np.sort(evals_s72)))  # (local)
print(f"\nCross-check vs S72: max |eigenvalue diff| = {max_diff:.2e}")
assert max_diff < 1e-10, f"Eigenvalue mismatch: {max_diff}"

# ============================================================================
#  SECTION 2: Effective Josephson coupling
# ============================================================================
#
# CG(24) is the Cayley graph of S_4 on 6 transposition generators.
# The 6 edges per vertex decompose by direction in the fiber:
#   - 4 edges along C^2 coset directions (coupling J_C2 = 0.933 M_KK)
#   - 1 edge along su(2) stabilizer direction (coupling J_su2 = 0.059 M_KK)
#   - 1 edge along u(1) direction (coupling J_u1 = 0.038 M_KK)
#
# Wait -- the transpositions generate edges in the Cayley graph, but the
# Josephson couplings are associated with bonds in the 32-cell tessellation.
# The CG(24) has 72 edges.  Each edge has a coupling determined by which
# generator it corresponds to.
#
# The transposition generators of S_4 partition as:
#   {(01),(02),(03),(12),(13),(23)} -- 6 generators
# In the coset decomposition SU(3) -> S_4:
#   - 4 of the 6 generators correspond to C^2 coset motions (J_C2)
#   - The remaining 2 are mixed su(2)/u(1) directions
# But the canonical constants give the coupling per bond type on the
# TESSELLATION, not per generator.  For the graph spectral decoherence,
# what matters is the effective coupling on the graph Laplacian.
#
# Approach: Use the bond-weighted average coupling.
# On the tessellation, each vertex has:
#   4 bonds with J_C2, 3 bonds with J_su2, 1 bond with J_u1 (total 8 bonds)
# But CG(24) is 6-regular, not 8-regular.
#
# Actually, the N_cells=32 tessellation and CG(24) are different objects.
# CG(24) captures the discrete symmetry group structure.  The tessellation
# has 32 cells with average 6.5 neighbors each.
#
# For this computation, we use the CG(24) graph structure (24 vertices,
# 6-regular) as established in S72 ISLAND-GRAPH-72.  The effective coupling
# per edge is the degree-weighted average:
#   J_eff = (4*J_C2 + 1*J_su2 + 1*J_u1) / 6
#
# This weights by the fraction of edges in each channel.
# Alternative: use just the dominant channel J_C2 as a bound.

print("\n" + "="*70)
print("SECTION 2: Effective Josephson coupling")
print("="*70)

# Bond-type decomposition on CG(24)
# 6 generators: partition 4 coset + 1 su(2) + 1 u(1)
n_C2 = 4     # (local)
n_su2 = 1    # (local)
n_u1 = 1     # (local)
n_total = n_C2 + n_su2 + n_u1  # (local)

J_eff_avg = (n_C2 * J_C2 + n_su2 * J_su2 + n_u1 * J_u1) / n_total  # (local)
J_eff_rms = np.sqrt((n_C2 * J_C2**2 + n_su2 * J_su2**2 + n_u1 * J_u1**2) / n_total)  # (local)
J_eff_C2_only = J_C2  # (local) -- upper bound: all edges at B2 coupling

print(f"\nJosephson couplings (M_KK units):")
print(f"  J_C2  = {J_C2:.3f}  (4 bonds, dominant)")
print(f"  J_su2 = {J_su2:.3f}  (1 bond)")
print(f"  J_u1  = {J_u1:.3f}  (1 bond)")
print(f"\nEffective coupling (6 edges per vertex):")
print(f"  J_eff (weighted avg) = {J_eff_avg:.6f} M_KK")
print(f"  J_eff (RMS)          = {J_eff_rms:.6f} M_KK")
print(f"  J_eff (C2 only)      = {J_eff_C2_only:.6f} M_KK")

# ============================================================================
#  SECTION 3: Decoherence timescale from spectral gap
# ============================================================================

print("\n" + "="*70)
print("SECTION 3: Decoherence timescale")
print("="*70)

# Phase diffusion on graph:
#   d(phi)/dt = -J_eff * L * phi
#   phi_k(t) = phi_k(0) * exp(-J_eff * lambda_k * t)
#
# The slowest-decaying mode has eigenvalue lambda_1:
#   t_dec = 1 / (J_eff * lambda_1)
#
# The mixing time (all modes decayed by 1/e) is set by lambda_1.
# The GRAPH mixing time is:
#   t_mix = (1/lambda_1) * log(N) / (J_eff)  for random walk normalization
# But our diffusion equation directly gives exp(-J_eff * lambda_k * t),
# so t_dec = 1 / (J_eff * lambda_1).

print(f"\nlambda_1 = {lambda_1:.6f}")
print(f"dt_transit = {dt_transit:.10f} M_KK^{{-1}}")

# Three estimates with different J_eff choices
for label, J_val in [("weighted avg", J_eff_avg),
                      ("RMS", J_eff_rms),
                      ("C2 only", J_eff_C2_only)]:
    t_dec = 1.0 / (J_val * lambda_1)  # (local)  -- M_KK^{-1}
    ratio = t_dec / dt_transit  # (local)
    print(f"\n  J_eff = {J_val:.4f} ({label}):")
    print(f"    t_dec = 1/(J*lambda_1) = {t_dec:.6f} M_KK^{{-1}}")
    print(f"    t_dec/t_transit = {ratio:.4f}")

    if 0.57 <= ratio <= 0.88:
        print(f"    --> IN GATE BAND [0.57, 0.88]: PASS")
    elif ratio < 0.1:
        print(f"    --> OVER-DECOHERED (< 0.1): FAIL")
    elif ratio > 5.0:
        print(f"    --> TOO SLOW (> 5.0): FAIL")
    else:
        print(f"    --> OUTSIDE [0.57, 0.88]: INFO")

# PRIMARY RESULT: Use the weighted average coupling
J_eff_primary = J_eff_avg  # (local)
t_dec_primary = 1.0 / (J_eff_primary * lambda_1)  # (local)
ratio_primary = t_dec_primary / dt_transit  # (local)

print(f"\n{'='*70}")
print(f"PRIMARY RESULT (weighted average J_eff):")
print(f"  t_dec = {t_dec_primary:.6f} M_KK^{{-1}}")
print(f"  t_dec/t_transit = {ratio_primary:.4f}")
print(f"{'='*70}")

# ============================================================================
#  SECTION 4: Full diffusion spectrum (aggregate decoherence)
# ============================================================================

print("\n" + "="*70)
print("SECTION 4: Aggregate multi-mode decoherence")
print("="*70)

# The aggregate phase variance decay is:
#   <delta_phi^2>(t) / <delta_phi^2>(0) = (1/N) * sum_k exp(-2*J_eff*lambda_k*t)
# where the sum excludes the k=0 zero mode (uniform phase).
#
# This decays FASTER than the single lambda_1 estimate because higher modes
# contribute exponentially decaying terms.
#
# Define t_dec_aggregate as the time where the aggregate drops to 1/e.

nonzero_evals = evals_L[evals_L > 1e-10]  # (local)
degeneracies = []  # (local)
unique_nonzero = np.unique(np.round(nonzero_evals, 6))  # (local)

print(f"\nNonzero Laplacian eigenvalues and their degeneracies:")
for lam in unique_nonzero:
    deg = np.sum(np.abs(nonzero_evals - lam) < 0.1)  # (local)
    degeneracies.append((lam, int(deg)))
    print(f"  lambda = {lam:.4f}, degeneracy = {int(deg)}")

print(f"\nTotal nonzero modes: {len(nonzero_evals)} (= N-1 = {N_vert - 1})")

# Compute aggregate decoherence for the primary J_eff
t_grid = np.linspace(0, 2 * t_dec_primary, 2000)  # (local)
aggregate = np.zeros_like(t_grid)  # (local)

for t_idx, t_val in enumerate(t_grid):
    # Sum over all nonzero modes with their degeneracies
    total = 0.0  # (local)
    for lam in nonzero_evals:
        total += np.exp(-2.0 * J_eff_primary * lam * t_val)
    aggregate[t_idx] = total / (N_vert - 1)  # Normalize by number of nonzero modes

# Find time where aggregate = 1/e
idx_e = np.argmin(np.abs(aggregate - 1.0/np.e))  # (local)
t_dec_aggregate = t_grid[idx_e]  # (local)
ratio_aggregate = t_dec_aggregate / dt_transit  # (local)

print(f"\nAggregate decoherence (all 23 nonzero modes):")
print(f"  t_dec_agg = {t_dec_aggregate:.6f} M_KK^{{-1}} (1/e crossing)")
print(f"  t_dec_agg/t_transit = {ratio_aggregate:.4f}")
print(f"  Speedup vs single-mode: {t_dec_primary / t_dec_aggregate:.3f}x")

# Also compute 1/e time using RMS J_eff
t_grid_rms = np.linspace(0, 2.0 / (J_eff_rms * lambda_1), 2000)  # (local)
aggregate_rms = np.zeros_like(t_grid_rms)  # (local)
for t_idx, t_val in enumerate(t_grid_rms):
    total = 0.0  # (local)
    for lam in nonzero_evals:
        total += np.exp(-2.0 * J_eff_rms * lam * t_val)
    aggregate_rms[t_idx] = total / (N_vert - 1)

idx_e_rms = np.argmin(np.abs(aggregate_rms - 1.0/np.e))  # (local)
t_dec_agg_rms = t_grid_rms[idx_e_rms]  # (local)
ratio_agg_rms = t_dec_agg_rms / dt_transit  # (local)

print(f"\nAggregate with RMS coupling:")
print(f"  t_dec_agg = {t_dec_agg_rms:.6f} M_KK^{{-1}}")
print(f"  t_dec_agg/t_transit = {ratio_agg_rms:.4f}")

# C2-only aggregate
t_grid_c2 = np.linspace(0, 2.0 / (J_eff_C2_only * lambda_1), 2000)  # (local)
aggregate_c2 = np.zeros_like(t_grid_c2)  # (local)
for t_idx, t_val in enumerate(t_grid_c2):
    total = 0.0  # (local)
    for lam in nonzero_evals:
        total += np.exp(-2.0 * J_eff_C2_only * lam * t_val)
    aggregate_c2[t_idx] = total / (N_vert - 1)

idx_e_c2 = np.argmin(np.abs(aggregate_c2 - 1.0/np.e))  # (local)
t_dec_agg_c2 = t_grid_c2[idx_e_c2]  # (local)
ratio_agg_c2 = t_dec_agg_c2 / dt_transit  # (local)

print(f"\nAggregate with C2-only coupling:")
print(f"  t_dec_agg = {t_dec_agg_c2:.6f} M_KK^{{-1}}")
print(f"  t_dec_agg/t_transit = {ratio_agg_c2:.4f}")

# ============================================================================
#  SECTION 5: Cross-checks (complete graph K_24 and path graph P_24)
# ============================================================================

print("\n" + "="*70)
print("SECTION 5: Cross-checks")
print("="*70)

# Cross-check 1: Complete graph K_24
# lambda_1 = N = 24, all nonzero eigenvalues equal to N
A_K24 = np.ones((24, 24)) - np.eye(24)  # (local)
L_K24 = graph_laplacian(A_K24)  # (local)
evals_K24 = np.sort(linalg.eigvalsh(L_K24))  # (local)
lambda_1_K24 = evals_K24[1]  # (local)
t_dec_K24 = 1.0 / (J_eff_primary * lambda_1_K24)  # (local)

print(f"\nComplete graph K_24:")
print(f"  lambda_1 = {lambda_1_K24:.4f} (expected: 24)")
print(f"  t_dec/t_transit = {t_dec_K24/dt_transit:.4f} (should be very small)")

# Cross-check 2: Path graph P_24
A_P24 = np.zeros((24, 24))  # (local)
for i in range(23):
    A_P24[i, i+1] = 1.0
    A_P24[i+1, i] = 1.0
L_P24 = graph_laplacian(A_P24)  # (local)
evals_P24 = np.sort(linalg.eigvalsh(L_P24))  # (local)
lambda_1_P24 = evals_P24[1]  # (local)
t_dec_P24 = 1.0 / (J_eff_primary * lambda_1_P24)  # (local)

# Analytic: lambda_k = 2 - 2*cos(pi*k/N) for k=0,...,N-1
lambda_1_P24_analytic = 2 - 2*np.cos(np.pi / 24)  # (local)

print(f"\nPath graph P_24:")
print(f"  lambda_1 = {lambda_1_P24:.6f} (analytic: {lambda_1_P24_analytic:.6f})")
print(f"  t_dec/t_transit = {t_dec_P24/dt_transit:.2f} (should be very large)")

# Cross-check 3: Cycle graph C_24
A_C24 = np.zeros((24, 24))  # (local)
for i in range(24):
    A_C24[i, (i+1) % 24] = 1.0
    A_C24[(i+1) % 24, i] = 1.0
L_C24 = graph_laplacian(A_C24)  # (local)
evals_C24 = np.sort(linalg.eigvalsh(L_C24))  # (local)
lambda_1_C24 = evals_C24[1]  # (local)
t_dec_C24 = 1.0 / (J_eff_primary * lambda_1_C24)  # (local)

print(f"\nCycle graph C_24:")
print(f"  lambda_1 = {lambda_1_C24:.6f}")
print(f"  t_dec/t_transit = {t_dec_C24/dt_transit:.2f}")

print(f"\n--- Summary of cross-checks ---")
print(f"  K_24 (complete):   lambda_1={lambda_1_K24:.2f}, t_dec/t_transit = {t_dec_K24/dt_transit:.4f}")
print(f"  CG(24) (Cayley):   lambda_1={lambda_1:.2f}, t_dec/t_transit = {ratio_primary:.4f}")
print(f"  C_24 (cycle):      lambda_1={lambda_1_C24:.4f}, t_dec/t_transit = {t_dec_C24/dt_transit:.2f}")
print(f"  P_24 (path):       lambda_1={lambda_1_P24:.4f}, t_dec/t_transit = {t_dec_P24/dt_transit:.2f}")
print(f"  Hierarchy check: K_24 << CG(24) << C_24 << P_24: "
      f"{'PASS' if t_dec_K24 < t_dec_primary < t_dec_C24 < t_dec_P24 else 'FAIL'}")

# ============================================================================
#  SECTION 6: Mixing time analysis
# ============================================================================

print("\n" + "="*70)
print("SECTION 6: Mixing time (log N / lambda_1)")
print("="*70)

# The random walk mixing time on a graph:
#   t_mix ~ (log N) / lambda_1  (in units of the natural step time 1/J_eff)
#
# This accounts for the convergence to the stationary distribution
# and gives a more physical estimate than the bare spectral gap.

t_mix_graph = np.log(N_vert) / lambda_1  # (local) -- in units of 1/J_eff
t_mix_physical = t_mix_graph / J_eff_primary  # (local) -- in M_KK^{-1}
ratio_mix = t_mix_physical / dt_transit  # (local)

print(f"\nGraph mixing time:")
print(f"  log(N)/lambda_1 = log({N_vert})/{lambda_1:.0f} = {t_mix_graph:.4f} (graph units)")
print(f"  t_mix = {t_mix_physical:.6f} M_KK^{{-1}}")
print(f"  t_mix/t_transit = {ratio_mix:.4f}")

# Also with Josephson frequency as clock (Phonon-First argument)
# The Josephson oscillation frequency sets the fastest timescale
omega_J = J_C2  # (local) -- Josephson frequency ~ J_C2 for B2 channel
t_J = 1.0 / omega_J  # (local) -- Josephson period
t_mix_J = t_mix_graph * t_J  # (local) -- mixing time in Josephson units
ratio_mix_J = t_mix_J / dt_transit  # (local)

print(f"\nWith Josephson frequency clock (omega_J = J_C2 = {omega_J:.3f}):")
print(f"  t_J = 1/omega_J = {t_J:.4f} M_KK^{{-1}}")
print(f"  t_mix = {t_mix_J:.6f} M_KK^{{-1}}")
print(f"  t_mix/t_transit = {ratio_mix_J:.4f}")

# ============================================================================
#  SECTION 7: Physical interpretation — diffusion vs hopping
# ============================================================================

print("\n" + "="*70)
print("SECTION 7: Physical interpretation")
print("="*70)

# The graph diffusion equation is continuous-time.  In the physical system,
# the Josephson coupling drives discrete phase hops at rate J_eff.
# The continuous diffusion approximation is valid when J_eff * lambda_1 >> 1/t_transit,
# i.e., when many hops occur during the transit.

N_hops_transit = J_eff_primary * dt_transit  # (local) -- mean hops per site during transit
print(f"\nMean hops per site during transit: {N_hops_transit:.4f}")
print(f"J_eff * lambda_1 * t_transit = {J_eff_primary * lambda_1 * dt_transit:.4f}")
print(f"  (>> 1 needed for diffusion approximation)")

# Decoherence efficiency: fraction of phase variance eliminated during transit
f_dec = 1.0 - np.exp(-dt_transit / t_dec_primary)  # (local)
print(f"\nFraction of phase variance eliminated during transit:")
print(f"  1 - exp(-t_transit/t_dec) = {f_dec:.6f}")

# Aggregate decoherence efficiency
f_dec_agg = 1.0 - aggregate[np.argmin(np.abs(t_grid - dt_transit))]  # (local)
print(f"  Aggregate (all modes): {f_dec_agg:.6f}")

# Compare to cell-crossing estimate from S72
d_cell_est = 2.0 * np.sqrt(3) / np.sqrt(N_vert)  # (local) -- for CG(24) embedded in S^3
t_cross_cell_est = d_cell_est / c_fabric  # (local) -- Euclidean cell crossing
ratio_cell_cross = t_cross_cell_est / dt_transit  # (local)

# S72 value: t_dec/t_transit = 6.73
print(f"\nComparison to S72 cell-crossing estimate:")
print(f"  S72 t_dec/t_transit (cell crossing) = 6.73")
print(f"  Graph spectral t_dec/t_transit = {ratio_primary:.4f}")
print(f"  Speedup from graph topology: {6.73 / ratio_primary:.1f}x")

# ============================================================================
#  SECTION 8: Anisotropic Laplacian (channel-dependent couplings)
# ============================================================================

print("\n" + "="*70)
print("SECTION 8: Anisotropic Laplacian")
print("="*70)

# In reality, the coupling is NOT the same on all edges.
# The 6 generators of S_4 via transpositions decompose as:
#   (01),(02),(03) -- "large" transpositions involving element 0 → C^2 coset?
#   (12),(13),(23) -- "small" transpositions among {1,2,3} → su(2)/u(1)?
#
# More precisely, the partition of the 6 transpositions into C^2/su(2)/u(1)
# channels depends on the embedding of S_4 in the Weyl group of SU(3).
# S_4 is NOT the Weyl group of SU(3) (that's S_3), so we need the coset
# decomposition explicitly.
#
# For this computation, we assign couplings based on the structure:
# The 6 transpositions split as:
#   4 "cross-coset" generators with J_C2
#   1 "within su(2)" with J_su2
#   1 "within u(1)" with J_u1
# We label: (01),(02),(12),(13) -> J_C2; (03) -> J_su2; (23) -> J_u1
# (This particular assignment doesn't change the SPECTRUM much due to the
# algebraic symmetry of S_4, but we compute it to bound the effect.)

def build_anisotropic_laplacian(elements, J_assignment):
    """Build graph Laplacian with edge-dependent couplings.

    J_assignment: dict mapping (i,j) transposition -> coupling strength
    """
    N = len(elements)  # (local)
    elem_to_idx = {e: i for i, e in enumerate(elements)}  # (local)

    L_aniso = np.zeros((N, N), dtype=float)  # (local)
    for idx, perm in enumerate(elements):
        for (i, j), J_val in J_assignment.items():
            new_perm = list(perm)  # (local)
            new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
            neighbor_idx = elem_to_idx[tuple(new_perm)]  # (local)
            L_aniso[idx, neighbor_idx] -= J_val
            L_aniso[idx, idx] += J_val

    return L_aniso

# Assignment: 4 generators J_C2, 1 generator J_su2, 1 generator J_u1
J_assign = {
    (0,1): J_C2, (0,2): J_C2, (1,2): J_C2, (1,3): J_C2,
    (0,3): J_su2,
    (2,3): J_u1
}  # (local)

L_aniso = build_anisotropic_laplacian(elements_S4, J_assign)  # (local)
evals_aniso = np.sort(linalg.eigvalsh(L_aniso))  # (local)
evals_aniso[np.abs(evals_aniso) < 1e-10] = 0.0

lambda_1_aniso = evals_aniso[evals_aniso > 1e-10][0]  # (local)

print(f"\nAnisotropic Laplacian (4xJ_C2 + 1xJ_su2 + 1xJ_u1):")
print(f"  lambda_1 = {lambda_1_aniso:.6f}")

# For anisotropic, J_eff is already built into the Laplacian:
# t_dec = 1 / lambda_1_aniso
t_dec_aniso = 1.0 / lambda_1_aniso  # (local) -- already in M_KK^{-1}
ratio_aniso = t_dec_aniso / dt_transit  # (local)

print(f"  t_dec = 1/lambda_1 = {t_dec_aniso:.6f} M_KK^{{-1}}")
print(f"  t_dec/t_transit = {ratio_aniso:.4f}")

# Full anisotropic spectrum
nonzero_aniso = evals_aniso[evals_aniso > 1e-10]  # (local)
unique_aniso = np.unique(np.round(nonzero_aniso, 4))  # (local)
print(f"\nAnisotropic spectrum (unique nonzero):")
for val in unique_aniso[:10]:
    deg = np.sum(np.abs(nonzero_aniso - val) < 0.05)  # (local)
    print(f"  lambda = {val:.4f}  (deg {int(deg)})")

# Aggregate anisotropic decoherence
t_grid_an = np.linspace(0, 3 * t_dec_aniso, 2000)  # (local)
agg_aniso = np.zeros_like(t_grid_an)  # (local)
for t_idx, t_val in enumerate(t_grid_an):
    total = 0.0  # (local)
    for lam in nonzero_aniso:
        total += np.exp(-2.0 * lam * t_val)
    agg_aniso[t_idx] = total / len(nonzero_aniso)

idx_e_an = np.argmin(np.abs(agg_aniso - 1.0/np.e))  # (local)
t_dec_agg_aniso = t_grid_an[idx_e_an]  # (local)
ratio_agg_aniso = t_dec_agg_aniso / dt_transit  # (local)

print(f"\nAggregate anisotropic:")
print(f"  t_dec_agg = {t_dec_agg_aniso:.6f} M_KK^{{-1}}")
print(f"  t_dec_agg/t_transit = {ratio_agg_aniso:.4f}")

# Try ALL possible 4-1-1 assignments (C(6,1)*C(5,1) = 30 choices)
# to bound the range of lambda_1
from itertools import combinations

transpositions_list = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]  # (local)
lambda_1_range = []  # (local)

for su2_idx in range(6):
    for u1_idx in range(6):
        if u1_idx == su2_idx:
            continue
        J_assign_trial = {}  # (local)
        for k, trans in enumerate(transpositions_list):
            if k == su2_idx:
                J_assign_trial[trans] = J_su2
            elif k == u1_idx:
                J_assign_trial[trans] = J_u1
            else:
                J_assign_trial[trans] = J_C2
        L_trial = build_anisotropic_laplacian(elements_S4, J_assign_trial)  # (local)
        evals_trial = np.sort(linalg.eigvalsh(L_trial))  # (local)
        evals_trial[np.abs(evals_trial) < 1e-10] = 0.0
        lam1_trial = evals_trial[evals_trial > 1e-10][0]  # (local)
        lambda_1_range.append(lam1_trial)

lambda_1_min = min(lambda_1_range)  # (local)
lambda_1_max_aniso = max(lambda_1_range)  # (local)

t_dec_max = 1.0 / lambda_1_min  # (local) -- slowest decoherence
t_dec_min = 1.0 / lambda_1_max_aniso  # (local) -- fastest decoherence

print(f"\nRange over all 30 (4-1-1) generator assignments:")
print(f"  lambda_1 in [{lambda_1_min:.6f}, {lambda_1_max_aniso:.6f}]")
print(f"  t_dec/t_transit in [{t_dec_min/dt_transit:.4f}, {t_dec_max/dt_transit:.4f}]")

# ============================================================================
#  SECTION 9: Compare to MSS bound
# ============================================================================

print("\n" + "="*70)
print("SECTION 9: MSS bound comparison")
print("="*70)

# The MSS chaos bound: lambda_L <= 2*pi*T/hbar
# Here T = T_acoustic = 0.112 M_KK
# The phase diffusion rate on the graph is NOT a Lyapunov exponent --
# it is a dissipative/mixing rate.  But we compare for completeness.

lambda_MSS = 2 * np.pi * T_acoustic  # (local) -- in M_KK units
mixing_rate = J_eff_primary * lambda_1  # (local) -- graph diffusion rate
mixing_rate_aniso = lambda_1_aniso  # (local) -- anisotropic rate

print(f"\nMSS bound: lambda_L_max = 2*pi*T = {lambda_MSS:.4f} M_KK")
print(f"Graph diffusion rate (isotropic): {mixing_rate:.4f} M_KK")
print(f"Graph diffusion rate (anisotropic): {mixing_rate_aniso:.4f} M_KK")
print(f"Ratio (iso/MSS): {mixing_rate / lambda_MSS:.4f}")
print(f"Ratio (aniso/MSS): {mixing_rate_aniso / lambda_MSS:.4f}")
print(f"\nNote: Graph diffusion is DISSIPATIVE mixing, not chaotic scrambling.")
print(f"The MSS bound applies to the Lyapunov exponent of OTOCs.")
print(f"The system is INTEGRABLE (all chaos gates FAIL), so lambda_L = 0.")
print(f"The phase equilibration here is dephasing, not scrambling.")

# ============================================================================
#  SECTION 10: GATE VERDICT
# ============================================================================

print("\n" + "="*70)
print("SECTION 10: GATE VERDICT")
print("="*70)

# Primary metric: single-mode decoherence with weighted average coupling
# Also report: anisotropic Laplacian, aggregate multi-mode, mixing time

print(f"\nGate: GRAPH-SPECTRAL-DECOHERENCE-73a")
print(f"Criterion: PASS if t_dec/t_transit in [0.57, 0.88]")
print(f"           FAIL if t_dec/t_transit < 0.1 or > 5.0")
print(f"           INFO otherwise")

results = {
    "Isotropic single-mode (J_avg)": ratio_primary,
    "Isotropic aggregate (J_avg)": ratio_aggregate,
    "Anisotropic single-mode": ratio_aniso,
    "Anisotropic aggregate": ratio_agg_aniso,
    "Mixing time (J_avg)": ratio_mix,
    "Mixing time (J_C2)": ratio_mix_J,
}

print(f"\nAll estimates:")
for label, r in results.items():
    status = "PASS" if 0.57 <= r <= 0.88 else ("FAIL" if (r < 0.1 or r > 5.0) else "INFO")  # (local)
    print(f"  {label}: t_dec/t_transit = {r:.4f}  [{status}]")

# The anisotropic result is the most physically accurate
verdict = "INFO"  # (local)
primary_ratio = ratio_aniso  # (local) -- anisotropic single-mode
if 0.57 <= primary_ratio <= 0.88:
    verdict = "PASS"
elif primary_ratio < 0.1 or primary_ratio > 5.0:
    verdict = "FAIL"

print(f"\n{'='*70}")
print(f"GATE VERDICT: {verdict}")
print(f"Primary metric: anisotropic single-mode t_dec/t_transit = {primary_ratio:.4f}")
if verdict == "PASS":
    print(f"Falls within gate band [0.57, 0.88].")
elif verdict == "INFO":
    if primary_ratio < 0.57:
        print(f"Below gate band lower bound 0.57 (faster decoherence than needed).")
    else:
        print(f"Above gate band upper bound 0.88 (slower decoherence than needed).")
else:
    if primary_ratio < 0.1:
        print(f"Over-decohered: t_dec/t_transit < 0.1.")
    else:
        print(f"Graph diffusion irrelevant: t_dec/t_transit > 5.0.")
print(f"{'='*70}")

# ============================================================================
#  SECTION 11: Save data
# ============================================================================

output_path = os.path.join(os.path.dirname(__file__), 's73a_graph_spectral_decoherence.npz')  # (local)

np.savez(output_path,
    # Gate
    gate_name='GRAPH-SPECTRAL-DECOHERENCE-73a',
    gate_verdict=verdict,
    gate_detail=f"t_dec/t_transit = {primary_ratio:.4f} (aniso single-mode). "
                f"Agg aniso: {ratio_agg_aniso:.4f}. Iso: {ratio_primary:.4f}. "
                f"Mix: {ratio_mix:.4f}. CG(24) lambda_1={lambda_1:.1f}, "
                f"lambda_1_aniso={lambda_1_aniso:.4f}.",
    # CG(24) properties
    N_vert=N_vert,
    N_edges=N_edges,
    degree=degree,
    evals_L=evals_L,
    evecs_L=evecs_L,
    lambda_1=lambda_1,
    lambda_max=lambda_max,
    ramanujan_bound=ramanujan_bound,
    # Coupling
    J_eff_avg=J_eff_avg,
    J_eff_rms=J_eff_rms,
    J_eff_C2=J_eff_C2_only,
    # Decoherence ratios
    t_dec_primary=t_dec_primary,
    ratio_primary=ratio_primary,
    t_dec_aggregate=t_dec_aggregate,
    ratio_aggregate=ratio_aggregate,
    t_dec_aniso=t_dec_aniso,
    ratio_aniso=ratio_aniso,
    t_dec_agg_aniso=t_dec_agg_aniso,
    ratio_agg_aniso=ratio_agg_aniso,
    t_mix_physical=t_mix_physical,
    ratio_mix=ratio_mix,
    ratio_mix_J=ratio_mix_J,
    # Anisotropic spectrum
    evals_aniso=evals_aniso,
    lambda_1_aniso=lambda_1_aniso,
    lambda_1_range_min=lambda_1_min,
    lambda_1_range_max=lambda_1_max_aniso,
    ratio_aniso_range_min=t_dec_min/dt_transit,
    ratio_aniso_range_max=t_dec_max/dt_transit,
    # Cross-checks
    lambda_1_K24=lambda_1_K24,
    lambda_1_P24=lambda_1_P24,
    lambda_1_C24=lambda_1_C24,
    ratio_K24=t_dec_K24/dt_transit,
    ratio_P24=t_dec_P24/dt_transit,
    ratio_C24=t_dec_C24/dt_transit,
    # Aggregate decoherence curves
    t_grid_agg=t_grid,
    aggregate_decay=aggregate,
    t_grid_aniso=t_grid_an,
    aggregate_aniso=agg_aniso,
    # MSS comparison
    lambda_MSS=lambda_MSS,
    mixing_rate_iso=mixing_rate,
    mixing_rate_aniso=mixing_rate_aniso,
    # Physical interpretation
    N_hops_transit=N_hops_transit,
    f_dec_single=f_dec,
    f_dec_aggregate=f_dec_agg,
    # Metadata
    dt_transit=dt_transit,
)

print(f"\nData saved to: {output_path}")
print(f"Total arrays: {len(np.load(output_path, allow_pickle=True).files)}")
print(f"\nDone.")
