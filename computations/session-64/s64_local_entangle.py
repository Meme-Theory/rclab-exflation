#!/usr/bin/env python3
"""
s64_local_entangle.py — Local Entanglement Entropy of GGE on CG(24) Fabric
============================================================================

Session 64, Gate: LOCAL-ENTANGLE-64
  INFO: Report S_ent value and scaling law.
        If S_ent = 0 → Jacobson Lambda = 0 (no entanglement contribution to CC).
        If S_ent > 0 → magnitude, area/volume scaling, connection to spectral action.

Physics:
  The GGE state is a product state in the QUASIPARTICLE (Bogoliubov mode) basis:
    rho_GGE = prod_k [n_k |1_k><1_k| + (1-n_k) |0_k><0_k|]

  Globally, S_ent = 0 in mode basis (no mode-mode entanglement).
  But Bogoliubov modes are DELOCALIZED across the CG(24) Cayley graph.
  Spatial bipartition into hemispheres A (12 vertices) and B (12 vertices)
  generates nonzero entanglement entropy because:
    - Mode k has weight |U[i,k]|^2 at vertex i
    - Tracing over B projects out B-components of each mode
    - This creates spatial entanglement in the VERTEX basis

  For Gaussian states, S_ent is determined entirely by eigenvalues of the
  restricted correlation matrix C_A (Peschel, J. Phys. A 36 (2003) L205):
    S_A = -sum_alpha [nu_alpha ln(nu_alpha) + (1-nu_alpha) ln(1-nu_alpha)]
  where nu_alpha are eigenvalues of (C_A)_{ij} = <c_i^dag c_j> for i,j in A.

  CRITICAL UPDATE (S64 W1-B): 94.6% of rho_ZP lies OUTSIDE the Gaudin charge
  space. The entanglement entropy's relationship to vacuum energy is through
  the spectral action (a_0 coefficient), not through integrable charges.

  The CG(24) graph is the Cayley graph of S_4 with generators being all 6
  transpositions: 24 vertices, 72 edges, regular degree 6, diameter 4.

Method:
  1. Build CG(24) Cayley graph (S_4 with transposition generators)
  2. Construct tight-binding Hamiltonian H_TB on CG(24) with Josephson couplings
  3. Map 8 BCS modes (4 B2 + 1 B1 + 3 B3) onto CG(24) TB eigenstates
  4. Build correlation matrix C_ij = sum_k n_k U[i,k] U[j,k]^*
  5. For EACH balanced bipartition (12+12):
     a. Restrict C to subsystem A: C_A = C[A,A]
     b. Compute S_ent from eigenvalues of C_A (Peschel formula)
  6. Also compute with anomalous correlations (BCS pairing, Peschel-Eisler 2009)
  7. Sample bipartitions: spectral (Fiedler), random, min-cut, max-cut
  8. Analyze: area law (S ~ |boundary|) vs volume law (S ~ |A|)
  9. Connect to CC via S64 W1-B: rho_ZP decomposition outside Gaudin span

Inputs:
  computations/session-62/s62_meissner_gge.npz  (GGE occupations, anomalous amplitudes)
  computations/session-56/s56_gge_fabric.npz    (single-particle energies, pairing V)
  computations/_shared/canonical_constants.py

Outputs:
  computations/session-64/s64_local_entangle.npz
  computations/session-64/s64_local_entangle.png

Author: Landau Condensed-Matter Theorist (S64)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from itertools import permutations, combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, J_C2, J_su2, J_u1, PI, T_acoustic,
    M_KK, M_KK_gravity, rho_Lambda_obs, a0_fold, a2_fold, a4_fold,
    E_cond, N_dof_BCS
)

data_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 76)
print("S64 W5-C: Local Entanglement Entropy of GGE on CG(24) Fabric")
print("Gate: LOCAL-ENTANGLE-64")
print("Method: Peschel correlation matrix (exact for Gaussian states)")
print("=" * 76)

# =====================================================================
#  1. BUILD THE CG(24) CAYLEY GRAPH
# =====================================================================
print("\n--- Section 1: Constructing CG(24) Cayley Graph ---")

def build_cayley_graph_S4():
    """
    Build the Cayley graph of S_4 (symmetric group on 4 elements) with
    generators = ALL 6 transpositions {(01),(02),(03),(12),(13),(23)}.

    Properties:
    - 24 vertices (= |S_4| = 4!)
    - Regular degree 6 (each transposition is its own inverse)
    - 72 edges (= 24 * 6 / 2)
    - Diameter 4 (max distance between any two permutations)
    - Vertex-transitive (S_4 acts transitively on itself by left multiplication)

    Returns: adjacency matrix (24x24), element list, element-to-index mapping
    """
    elements = list(permutations(range(4)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}
    N = len(elements)
    assert N == 24, f"Expected 24 elements of S_4, got {N}"

    # Generators: all 6 transpositions of {0,1,2,3}
    generators = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    def apply_transposition(perm, i, j):
        lst = list(perm)
        lst[i], lst[j] = lst[j], lst[i]
        return tuple(lst)

    adj = np.zeros((N, N), dtype=np.int8)
    for perm in elements:
        idx = elem_to_idx[perm]  # (local)
        for (i, j) in generators:
            neighbor = apply_transposition(perm, i, j)
            nbr_idx = elem_to_idx[neighbor]
            adj[idx, nbr_idx] = 1
            adj[nbr_idx, idx] = 1

    # Verify properties
    degrees = adj.sum(axis=1)
    assert np.all(degrees == 6), f"Not regular degree 6: {degrees}"
    N_edges = int(np.sum(adj)) // 2
    assert N_edges == 72, f"Expected 72 edges, got {N_edges}"

    return adj, elements, elem_to_idx


def graph_diameter(adj):
    """Compute graph diameter via BFS from each vertex."""
    N = adj.shape[0]
    max_dist = 0
    dist_matrix = np.full((N, N), -1, dtype=int)
    for start in range(N):
        dist = np.full(N, -1, dtype=int)
        dist[start] = 0
        queue = [start]
        qi = 0
        while qi < len(queue):
            v = queue[qi]; qi += 1
            for u in range(N):
                if adj[v, u] == 1 and dist[u] == -1:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        dist_matrix[start] = dist
        max_dist = max(max_dist, dist.max())
    return max_dist, dist_matrix


adj_cg24, elements_S4, elem_to_idx = build_cayley_graph_S4()
N_vert = adj_cg24.shape[0]  # 24
N_edges = int(np.sum(adj_cg24)) // 2  # 72
diameter, dist_matrix = graph_diameter(adj_cg24)

# Graph Laplacian
D_diag = np.diag(adj_cg24.sum(axis=1).astype(float))
L_graph = D_diag - adj_cg24.astype(float)
evals_L, evecs_L = np.linalg.eigh(L_graph)

print(f"  CG(24): {N_vert} vertices, {N_edges} edges, degree 6, diameter {diameter}")
print(f"  Laplacian spectrum: {evals_L}")
print(f"  Fiedler value (algebraic connectivity): {evals_L[1]:.6f}")
print(f"  Spectral gap: {evals_L[1]:.6f}")

# =====================================================================
#  2. TIGHT-BINDING HAMILTONIAN ON CG(24)
# =====================================================================
print("\n--- Section 2: Tight-binding Hamiltonian on CG(24) ---")
print("  Building site-resolved TB Hamiltonian with Josephson couplings...")

# The CG(24) is vertex-transitive, so the TB Hamiltonian is:
#   H_TB = -J * adjacency_matrix
# where J is the dominant Josephson coupling J_C2.
#
# For the full anisotropic version, each edge type (corresponding to
# different transposition generators) would carry a different coupling.
# However, on CG(24) with all-transposition generators, the graph is
# edge-transitive as well (Aut(CG(24)) acts transitively on edges).
# So all bonds are equivalent and J_eff = J_C2.

J_eff = J_C2  # Dominant coupling, all bonds equivalent on CG(24)
H_TB = -J_eff * adj_cg24.astype(float)

# Diagonalize
evals_TB, evecs_TB = eigh(H_TB)

print(f"  J_eff = {J_eff:.6f} M_KK (all bonds equivalent by edge-transitivity)")
print(f"  TB eigenvalues: {evals_TB}")
print(f"  Bandwidth: {evals_TB[-1] - evals_TB[0]:.6f} M_KK")
print(f"  Eigenvector shape: {evecs_TB.shape}")

# Verify eigendecomposition
H_recon = evecs_TB @ np.diag(evals_TB) @ evecs_TB.T
recon_err = np.max(np.abs(H_recon - H_TB))
print(f"  Eigendecomposition check: max|V D V^T - H| = {recon_err:.2e}")
assert recon_err < 1e-12

# Verify orthonormality
orth_err = np.max(np.abs(evecs_TB.T @ evecs_TB - np.eye(N_vert)))
print(f"  Orthonormality: max|V^T V - I| = {orth_err:.2e}")
assert orth_err < 1e-12

# =====================================================================
#  3. LOAD GGE STATE AND MAP TO CG(24) MODES
# =====================================================================
print("\n--- Section 3: GGE state on CG(24) ---")

# Load GGE occupation numbers from S62 meissner computation
d62m = np.load(os.path.join(data_dir, 's62_meissner_gge.npz'), allow_pickle=True)
n_k_GGE_8mode = d62m['n_k_GGE']   # 8 GGE occupations (single-cell)
F_k_GGE_8mode = d62m['F_k_GGE']   # 8 anomalous amplitudes
n_k_GS_8mode = d62m['n_k_GS']     # 8 ground state occupations
F_k_GS_8mode = d62m['F_k_GS']     # 8 anomalous amplitudes (GS)

# Load single-particle spectrum
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']  # 8 single-particle energies at fold

print(f"  GGE occupations (8-mode, single cell):")
mode_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
for k in range(8):
    lam_k = np.log((1 - n_k_GGE_8mode[k]) / n_k_GGE_8mode[k]) if 0 < n_k_GGE_8mode[k] < 1 else 0
    print(f"    k={k} ({mode_labels[k]}): n_k = {n_k_GGE_8mode[k]:.6e}, "
          f"lambda_k = {lam_k:.4f}, F_k = {F_k_GGE_8mode[k]:.6e}")

# On the CG(24) fabric, each vertex carries 8 internal modes.
# The TOTAL number of modes is 24 * 8 = 192.
# However, we work in the tight-binding approximation where the
# 8 internal modes at each site are broadened into 8 BANDS,
# each with 24 k-states (one per TB eigenstate).
#
# The GGE state on the fabric:
#   rho_GGE = product over all (band, k-state) of Fermi factors.
#
# For the Peschel method, we need the correlation matrix in the
# SITE basis. For band alpha and sites i,j:
#   C^{alpha}_{ij} = <c_{i,alpha}^dag c_{j,alpha}>
#                  = sum_k n_{alpha,k} U[i,k] U[j,k]
#
# Here n_{alpha,k} is the occupation of band alpha at k-point k.
# For the GGE product state, the inter-band correlations are zero.
#
# The single-cell GGE has 8 occupations n_k. On the fabric with
# Josephson coupling, each mode k hybridizes across cells.
# The k-dependent occupation for mode alpha at TB eigenstate k is:
#   n_{alpha}(k) = n_{alpha} (uniform for product-state GGE)
# because the GGE Lagrange multipliers couple to LOCAL conserved
# charges, not to Bloch-wave momenta.

N_bands = 8  # 4 B2 + 1 B1 + 3 B3
N_total_modes = N_vert * N_bands  # 192

# Build the full correlation matrix C in the (site, band) basis
# C is block-diagonal in band index (no inter-band correlations in GGE):
#   C_{(i,alpha),(j,beta)} = delta_{alpha,beta} * sum_k n_alpha U[i,k] U[j,k]

# For the entanglement computation, we can compute the contribution
# from EACH BAND INDEPENDENTLY and sum the entropies, because the
# GGE is a product state across bands.
#
# WAIT: This is WRONG. The entanglement entropy of a product state
# over bands is NOT the sum of per-band entropies. The entropy is
# a nonlinear function of the eigenvalues. We must work with the
# FULL correlation matrix of the composite system.
#
# The full correlation matrix has dimension N_A * N_bands x N_A * N_bands
# where N_A = 12 (half of 24 vertices). So dim = 96 x 96.
# This is perfectly tractable.

print(f"\n  Building full correlation matrix: {N_vert*N_bands} x {N_vert*N_bands}")
print(f"  (block-diagonal in band index, {N_bands} blocks of {N_vert}x{N_vert})")

# Full correlation matrix in (site, band) composite basis
# Ordering: (site_0 band_0, site_0 band_1, ..., site_0 band_7, site_1 band_0, ...)
# i.e., C[(i*N_bands+alpha), (j*N_bands+beta)] = delta_{alpha,beta} * C^alpha_{ij}

dim_full = N_vert * N_bands  # 192

# Build per-band correlation matrices in site basis
# C^alpha_{ij} = n_alpha * sum_k U[i,k] U[j,k] = n_alpha * (U U^T)_{ij}
#
# Since U U^T = I (orthogonal), C^alpha = n_alpha * I for UNIFORM occupation.
#
# This would give S_ent = 0 for any bipartition (diagonal C_A has all eigenvalues
# equal to n_alpha, and the entropy from each eigenvalue is
# -n_alpha ln(n_alpha) - (1-n_alpha) ln(1-n_alpha) per mode in A,
# which is the same as the thermal entropy -- NOT entanglement.
#
# CRUCIAL PHYSICS POINT: If all k-states in a band have the SAME occupation
# (which is the case for a local GGE), then C^alpha = n_alpha * I, and
# the ENTANGLEMENT entropy (which is S(rho_A) - S_thermal) is ZERO.
#
# This is the key structural result: the local entanglement entropy on
# CG(24) is NOT simply determined by the diagonal n_k values.
# It comes from SPATIALLY INHOMOGENEOUS occupations, which arise when:
# (a) The Josephson coupling is site-dependent (not the case for CG(24))
# (b) The GGE Lagrange multipliers are site-dependent
# (c) The modes themselves have SITE-DEPENDENT STRUCTURE
#
# For the BCS condensate on CG(24), the relevant modes are NOT the
# single-particle TB eigenstates (which span all 24 modes per band)
# but the BCS quasiparticle modes, which mix particle and hole.
#
# The BCS state has anomalous correlations <c_i c_j> != 0, and these
# are what generate spatial entanglement even when the normal part is
# diagonal.
#
# Let me implement both:
# (A) Normal correlations only: C^alpha_{ij} from GGE occupations
# (B) Full BCS with anomalous: Gamma matrix method (Peschel-Eisler 2009)

# =====================================================================
#  3A. PER-BAND CORRELATION MATRICES WITH JOSEPHSON HYBRIDIZATION
# =====================================================================
print("\n--- Section 3A: Per-band correlation matrices ---")

# The actual GGE on the fabric is NOT a simple product of identical
# single-cell GGE states. The Josephson coupling hybridizes the
# modes across cells. The resulting GGE state has occupations that
# depend on the Bloch wave-vector.
#
# For band alpha with single-particle energy eps_alpha, the
# Josephson-hybridized spectrum is:
#   E_{alpha,k} = eps_alpha + J_eff * lambda_k
# where lambda_k are the TB (Laplacian) eigenvalues.
#
# The GGE occupation at each k-point is:
#   n_{alpha}(k) = 1 / (1 + exp(beta_alpha * E_{alpha,k}))
#
# where beta_alpha is the effective inverse temperature for band alpha.
# From the single-cell GGE occupations:
#   beta_alpha = ln((1 - n_alpha) / n_alpha) / eps_alpha
#
# This gives k-DEPENDENT occupations, which generate spatial entanglement.

# Effective inverse temperatures from single-cell GGE
beta_eff = np.zeros(N_bands)
for alpha in range(N_bands):
    n_a = n_k_GGE_8mode[alpha]
    e_a = eps_fold[alpha]
    if n_a > 1e-30 and n_a < 1 - 1e-30 and abs(e_a) > 1e-15:
        beta_eff[alpha] = np.log((1 - n_a) / n_a) / e_a
    elif abs(e_a) < 1e-15:
        # Zero-energy mode: use the Lagrange multiplier directly
        beta_eff[alpha] = np.log((1 - n_a) / n_a) if 0 < n_a < 1 else 0
    else:
        beta_eff[alpha] = 0

print("  Effective inverse temperatures (beta_alpha * eps_alpha = lambda_alpha):")
for alpha in range(N_bands):
    print(f"    {mode_labels[alpha]}: beta = {beta_eff[alpha]:.4f}, "
          f"eps = {eps_fold[alpha]:.6f}, "
          f"lambda = {beta_eff[alpha]*eps_fold[alpha]:.4f}")

# Build k-dependent occupations
# evals_TB are the 24 eigenvalues of -J_eff * adj (TB Hamiltonian eigenvalues)
# For CG(24) with H_TB = -J * A, the eigenvalues are -J * eigenvalues_of_A
# The TB eigenvalues include the Josephson shift.
# Actually, the correct hybridized spectrum should use the LAPLACIAN:
#   E_{alpha,k} = eps_alpha - J_eff * lambda_k^{adj}
# where lambda_k^{adj} are eigenvalues of the adjacency matrix.
# evals_TB = -J_eff * lambda_k^{adj}, so lambda_k^{adj} = -evals_TB / J_eff

lambda_adj = -evals_TB / J_eff  # Adjacency matrix eigenvalues
print(f"\n  Adjacency eigenvalues: {lambda_adj}")

# Hybridized spectrum for each band
E_hybrid = np.zeros((N_bands, N_vert))
n_k_hybrid = np.zeros((N_bands, N_vert))

for alpha in range(N_bands):
    e_a = eps_fold[alpha]
    for k in range(N_vert):
        # Energy of band alpha at k-point k
        # The TB Hamiltonian shifts the on-site energy by the TB eigenvalue
        E_hybrid[alpha, k] = e_a + evals_TB[k]

        # GGE occupation: n = 1/(1 + exp(beta * E))
        # For the zero-energy mode (alpha=0), use the direct Lagrange multiplier
        if abs(e_a) < 1e-15:
            # Mode 0 has eps=0. The Lagrange multiplier is lambda_0 = ln((1-n_0)/n_0) = -4.45
            # The hybridized lambda is lambda_0 + beta_eff_adj * evals_TB[k]
            # Since this mode's occupation is almost 1, beta is large and negative
            lam_0 = np.log((1 - n_k_GGE_8mode[0]) / n_k_GGE_8mode[0])
            # The shift from Josephson: ratio of TB eigenvalue to single-cell energy scale
            # Use the NEXT mode's beta as the reference for the energy scale
            beta_ref = beta_eff[1] if abs(beta_eff[1]) > 1e-10 else 1.0
            lam_k = lam_0 + beta_ref * evals_TB[k]
            n_k_hybrid[alpha, k] = 1.0 / (1.0 + np.exp(lam_k))
        else:
            beta_a = beta_eff[alpha]
            n_k_hybrid[alpha, k] = 1.0 / (1.0 + np.exp(beta_a * E_hybrid[alpha, k]))

    print(f"  Band {mode_labels[alpha]}: E in [{E_hybrid[alpha].min():.4f}, "
          f"{E_hybrid[alpha].max():.4f}], "
          f"n_k in [{n_k_hybrid[alpha].min():.6e}, {n_k_hybrid[alpha].max():.6e}]")

# Build per-band correlation matrices in site basis
# C^alpha_{ij} = sum_k n_{alpha,k} U[i,k] U[j,k]
# where U = evecs_TB (site-to-k transformation)

C_bands_GGE = np.zeros((N_bands, N_vert, N_vert))
for alpha in range(N_bands):
    for k in range(N_vert):
        C_bands_GGE[alpha] += n_k_hybrid[alpha, k] * np.outer(evecs_TB[:, k], evecs_TB[:, k])

# Verify: Tr(C^alpha) = sum_k n_{alpha,k}
for alpha in range(N_bands):
    tr_C = np.trace(C_bands_GGE[alpha])
    sum_n = n_k_hybrid[alpha].sum()
    print(f"  Band {mode_labels[alpha]}: Tr(C) = {tr_C:.8f}, sum(n_k) = {sum_n:.8f}, "
          f"match: {np.isclose(tr_C, sum_n)}")

# Build FULL correlation matrix in composite (site, band) basis
# C_full[(i*N_bands+alpha), (j*N_bands+beta)] = delta_{alpha,beta} * C^alpha_{ij}
C_full = np.zeros((dim_full, dim_full))
for alpha in range(N_bands):
    for i in range(N_vert):
        for j in range(N_vert):
            C_full[i*N_bands + alpha, j*N_bands + alpha] = C_bands_GGE[alpha, i, j]

# Verify: all eigenvalues of C_full in [0, 1]
eigs_C_full = np.linalg.eigvalsh(C_full)
print(f"\n  C_full eigenvalues: min = {eigs_C_full.min():.6e}, max = {eigs_C_full.max():.6e}")
print(f"  All in [0,1]: {np.all(eigs_C_full >= -1e-12) and np.all(eigs_C_full <= 1+1e-12)}")

# =====================================================================
#  3B. ANOMALOUS CORRELATION MATRICES (BCS PAIRING)
# =====================================================================
print("\n--- Section 3B: Anomalous (BCS pairing) correlations ---")

# The anomalous correlation F^alpha_{ij} = <c_{i,alpha} c_{j,alpha}>
# For a BCS state with pairing amplitude F_alpha and k-dependent structure:
#   F^alpha_{ij} = sum_k f_{alpha,k} U[i,k] U[j,k]
#
# For the GGE state, f_{alpha,k} = F_alpha * (mode structure factor)
# In the simplest approximation, f is k-independent within a band:

F_bands_GGE = np.zeros((N_bands, N_vert, N_vert))
for alpha in range(N_bands):
    # The anomalous amplitude is k-independent to leading order
    f_a = F_k_GGE_8mode[alpha]
    F_bands_GGE[alpha] = f_a * np.eye(N_vert)
    # More accurately, with k-dependence from BCS self-consistency:
    # f_{alpha,k} = Delta_alpha / (2 * E_{alpha,k})
    # But we use the single-cell GGE values as the best available data.

# Build full anomalous matrix
F_full = np.zeros((dim_full, dim_full))
for alpha in range(N_bands):
    for i in range(N_vert):
        for j in range(N_vert):
            F_full[i*N_bands + alpha, j*N_bands + alpha] = F_bands_GGE[alpha, i, j]

print(f"  Anomalous matrix: ||F_full|| = {np.linalg.norm(F_full):.6e}")
print(f"  Max |F_ij| = {np.max(np.abs(F_full)):.6e}")

# =====================================================================
#  4. BIPARTITION STRATEGIES ON CG(24)
# =====================================================================
print("\n--- Section 4: Bipartition strategies ---")

def cut_size_fast(adj, A_set):
    """Count edges crossing from A to its complement."""
    mask = np.zeros(adj.shape[0], dtype=bool)
    for v in A_set:
        mask[v] = True
    return int(np.sum(adj[mask][:, ~mask]))

# Strategy 1: Spectral (Fiedler) bipartition
fiedler = evecs_L[:, 1]  # Fiedler vector (2nd eigenvector of Laplacian)
sorted_by_fiedler = np.argsort(fiedler)
A_fiedler = set(sorted_by_fiedler[12:].tolist())  # Upper half
cut_fiedler = cut_size_fast(adj_cg24, A_fiedler)
print(f"  Fiedler partition: cut = {cut_fiedler} edges, "
      f"A = {sorted(A_fiedler)}")

# Strategy 2: Greedy max-cut from Fiedler
A_maxcut = set(A_fiedler)
best_cut = cut_fiedler
for iteration in range(500):
    improved = False
    for i in list(A_maxcut):
        for j in range(N_vert):
            if j in A_maxcut:
                continue
            new_A = (A_maxcut - {i}) | {j}
            new_cut = cut_size_fast(adj_cg24, new_A)
            if new_cut > best_cut:
                best_cut = new_cut
                A_maxcut = new_A
                improved = True
                break
        if improved:
            break
    if not improved:
        break

print(f"  Max-cut (greedy): cut = {best_cut} edges, "
      f"A = {sorted(A_maxcut)}")

# Strategy 3: Random search for max-cut
np.random.seed(42)
A_random_best = set(A_maxcut)
cut_random_best = best_cut
for trial in range(100000):
    perm = np.random.permutation(N_vert)
    A_try = set(perm[:12].tolist())
    c = cut_size_fast(adj_cg24, A_try)
    if c > cut_random_best:
        cut_random_best = c
        A_random_best = set(A_try)

# Greedy refine from random best
if cut_random_best > best_cut:
    A_maxcut = set(A_random_best)
    best_cut = cut_random_best
    for iteration in range(500):
        improved = False
        for i in list(A_maxcut):
            for j in range(N_vert):
                if j in A_maxcut:
                    continue
                new_A = (A_maxcut - {i}) | {j}
                new_cut = cut_size_fast(adj_cg24, new_A)
                if new_cut > best_cut:
                    best_cut = new_cut
                    A_maxcut = new_A
                    improved = True
                    break
            if improved:
                break
        if not improved:
            break

print(f"  Max-cut (random+greedy): cut = {best_cut} edges")

# Strategy 4: Greedy min-cut
A_mincut = set(sorted_by_fiedler[:12].tolist())
min_cut_val = cut_size_fast(adj_cg24, A_mincut)
for iteration in range(500):
    improved = False
    for i in list(A_mincut):
        for j in range(N_vert):
            if j in A_mincut:
                continue
            new_A = (A_mincut - {i}) | {j}
            new_cut = cut_size_fast(adj_cg24, new_A)
            if new_cut < min_cut_val:
                min_cut_val = new_cut
                A_mincut = new_A
                improved = True
                break
        if improved:
            break
    if not improved:
        break

print(f"  Min-cut (greedy): cut = {min_cut_val} edges, "
      f"A = {sorted(A_mincut)}")

# =====================================================================
#  5. ENTANGLEMENT ENTROPY VIA PESCHEL METHOD
# =====================================================================
print("\n--- Section 5: Entanglement entropy computation ---")

def peschel_entropy_normal(C_full, A_sites, N_bands):
    """
    Compute von Neumann entanglement entropy of a Gaussian (free-fermion)
    state via the Peschel method, for a composite (site, band) system.

    The correlation matrix C has dimension (N_sites * N_bands) x (N_sites * N_bands).
    Restriction to subsystem A means keeping rows/columns for sites in A,
    across all bands.

    S_A = -sum_alpha [nu_alpha ln(nu_alpha) + (1-nu_alpha) ln(1-nu_alpha)]
    where nu_alpha are eigenvalues of C_A.

    Reference: Peschel, J. Phys. A 36 (2003) L205.
    """
    A_list = sorted(A_sites)
    N_A = len(A_list)

    # Build the list of composite indices for sites in A
    A_indices = []
    for site in A_list:
        for band in range(N_bands):
            A_indices.append(site * N_bands + band)
    A_indices = np.array(A_indices)

    # Restrict correlation matrix
    C_A = C_full[np.ix_(A_indices, A_indices)]

    # Eigenvalues
    nu = np.linalg.eigvalsh(C_A)

    # Clip to avoid log(0)
    tol = 1e-15  # (local)
    S_ent = 0.0  # (local)
    n_entangled = 0
    nu_active = []
    for v in nu:
        if v > tol and v < 1.0 - tol:
            s = -v * np.log(v) - (1.0 - v) * np.log(1.0 - v)
            S_ent += s
            n_entangled += 1
            nu_active.append(v)

    return S_ent, nu, n_entangled, C_A


def peschel_entropy_bcs(C_full, F_full, A_sites, N_bands):
    """
    Entanglement entropy for BCS Gaussian state with anomalous correlations.

    Uses the generalized 2D x 2D covariance matrix (Peschel-Eisler 2009):
      Gamma = [[C_A, F_A], [F_A, I - C_A]]

    Eigenvalues of Gamma come in pairs (lambda, 1-lambda).
    S_ent = sum over DISTINCT pairs of h(lambda).
    """
    A_list = sorted(A_sites)
    N_A = len(A_list)

    # Composite indices
    A_indices = []
    for site in A_list:
        for band in range(N_bands):
            A_indices.append(site * N_bands + band)
    A_indices = np.array(A_indices)
    dim_A = len(A_indices)

    C_A = C_full[np.ix_(A_indices, A_indices)]
    F_A = F_full[np.ix_(A_indices, A_indices)]

    # Build generalized covariance matrix
    Gamma = np.zeros((2 * dim_A, 2 * dim_A))
    Gamma[:dim_A, :dim_A] = C_A
    Gamma[:dim_A, dim_A:] = F_A
    Gamma[dim_A:, :dim_A] = F_A  # F^T = F for time-reversal symmetric BCS
    Gamma[dim_A:, dim_A:] = np.eye(dim_A) - C_A

    # Eigenvalues
    lam = np.linalg.eigvalsh(Gamma)
    lam_sorted = np.sort(lam)

    # Take the dim_A eigenvalues >= 0.5 (each paired with one <= 0.5)
    lam_upper = lam_sorted[dim_A:]

    # Entropy from distinct eigenvalues
    tol = 1e-15  # (local)
    S_ent = 0.0  # (local)
    for l in lam_upper:
        if l > tol and l < 1.0 - tol:
            S_ent += -l * np.log(l) - (1.0 - l) * np.log(1.0 - l)

    # Verify pairing
    lam_lower = lam_sorted[:dim_A]
    pair_err = np.max(np.abs(np.sort(lam_upper) + np.sort(1.0 - lam_lower[::-1]) - 1.0))

    return S_ent, lam, pair_err


# --- 5a. Max-cut partition ---
print("\n  5a. Max-cut partition (Peschel method)")
S_normal_max, nu_max, n_eff_max, C_A_max = peschel_entropy_normal(
    C_full, A_maxcut, N_bands)
S_bcs_max, lam_bcs_max, pair_err_max = peschel_entropy_bcs(
    C_full, F_full, A_maxcut, N_bands)

print(f"  S_ent(normal, max-cut) = {S_normal_max:.6f} nats")
print(f"  S_ent(BCS, max-cut)    = {S_bcs_max:.6f} nats")
print(f"  BCS eigenvalue pairing error: {pair_err_max:.2e}")
print(f"  Number of entangled modes: {n_eff_max} / {len(nu_max)}")

# --- 5b. Fiedler partition ---
S_normal_fiedler, _, n_eff_fiedler, _ = peschel_entropy_normal(
    C_full, A_fiedler, N_bands)
S_bcs_fiedler, _, _ = peschel_entropy_bcs(
    C_full, F_full, A_fiedler, N_bands)
print(f"\n  S_ent(normal, Fiedler) = {S_normal_fiedler:.6f} nats")
print(f"  S_ent(BCS, Fiedler)    = {S_bcs_fiedler:.6f} nats")

# --- 5c. Min-cut partition ---
S_normal_min, _, n_eff_min, _ = peschel_entropy_normal(
    C_full, A_mincut, N_bands)
S_bcs_min, _, _ = peschel_entropy_bcs(
    C_full, F_full, A_mincut, N_bands)
print(f"\n  S_ent(normal, min-cut) = {S_normal_min:.6f} nats")
print(f"  S_ent(BCS, min-cut)    = {S_bcs_min:.6f} nats")

# --- 5d. Complement entropy (for mutual information) ---
B_maxcut = set(range(N_vert)) - A_maxcut
S_B_normal, _, _, _ = peschel_entropy_normal(C_full, B_maxcut, N_bands)
S_B_bcs, _, _ = peschel_entropy_bcs(C_full, F_full, B_maxcut, N_bands)
print(f"\n  S_ent(B, normal) = {S_B_normal:.6f} nats  [complement of max-cut A]")
print(f"  S_ent(B, BCS)    = {S_B_bcs:.6f} nats")

# =====================================================================
#  6. BIPARTITION SWEEP (2000 RANDOM SAMPLES)
# =====================================================================
print("\n--- Section 6: Bipartition sweep (2000 random 12+12 samples) ---")

np.random.seed(137)
N_sample = 2000
S_sweep_normal = np.zeros(N_sample)
S_sweep_bcs = np.zeros(N_sample)
cut_sweep = np.zeros(N_sample, dtype=int)

for trial in range(N_sample):
    perm = np.random.permutation(N_vert)
    A_try = set(perm[:12].tolist())

    S_n, _, _, _ = peschel_entropy_normal(C_full, A_try, N_bands)
    S_b, _, _ = peschel_entropy_bcs(C_full, F_full, A_try, N_bands)

    S_sweep_normal[trial] = S_n
    S_sweep_bcs[trial] = S_b if np.isfinite(S_b) else 0.0
    cut_sweep[trial] = cut_size_fast(adj_cg24, A_try)

    if (trial + 1) % 500 == 0:
        print(f"    ... completed {trial+1}/{N_sample} samples")

print(f"\n  Normal S_ent: mean = {S_sweep_normal.mean():.6f}, "
      f"std = {S_sweep_normal.std():.6f}, "
      f"range = [{S_sweep_normal.min():.6f}, {S_sweep_normal.max():.6f}]")
print(f"  BCS S_ent:    mean = {S_sweep_bcs.mean():.6f}, "
      f"std = {S_sweep_bcs.std():.6f}, "
      f"range = [{S_sweep_bcs.min():.6f}, {S_sweep_bcs.max():.6f}]")
print(f"  Cut sizes:    mean = {cut_sweep.mean():.1f}, "
      f"range = [{cut_sweep.min()}, {cut_sweep.max()}]")

# =====================================================================
#  7. AREA LAW ANALYSIS
# =====================================================================
print("\n--- Section 7: Area law analysis ---")

# Fit S_ent vs cut_size (area law: S = s_0 * n_cut + gamma_topo)
coeffs_normal = np.polyfit(cut_sweep, S_sweep_normal, 1)
s0_normal = coeffs_normal[0]
gamma_topo_normal = coeffs_normal[1]

coeffs_bcs = np.polyfit(cut_sweep, S_sweep_bcs, 1)
s0_bcs = coeffs_bcs[0]
gamma_topo_bcs = coeffs_bcs[1]

# R^2 values
SS_res_n = np.sum((S_sweep_normal - np.polyval(coeffs_normal, cut_sweep))**2)
SS_tot_n = np.sum((S_sweep_normal - S_sweep_normal.mean())**2)
R2_normal = 1.0 - SS_res_n / SS_tot_n if SS_tot_n > 0 else 0.0

SS_res_b = np.sum((S_sweep_bcs - np.polyval(coeffs_bcs, cut_sweep))**2)
SS_tot_b = np.sum((S_sweep_bcs - S_sweep_bcs.mean())**2)
R2_bcs = 1.0 - SS_res_b / SS_tot_b if SS_tot_b > 0 else 0.0

# Correlation coefficients
corr_cut_normal = np.corrcoef(cut_sweep, S_sweep_normal)[0, 1]
corr_cut_bcs = np.corrcoef(cut_sweep, S_sweep_bcs)[0, 1]

print(f"  Normal: S = {s0_normal:.6f} * n_cut + {gamma_topo_normal:.6f}")
print(f"    s_0 (entropy per cut edge) = {s0_normal:.6f} nats/edge")
print(f"    gamma (topological term)   = {gamma_topo_normal:.6f} nats")
print(f"    R^2 = {R2_normal:.6f}")
print(f"    Pearson r = {corr_cut_normal:.6f}")
print(f"\n  BCS: S = {s0_bcs:.6f} * n_cut + {gamma_topo_bcs:.6f}")
print(f"    s_0 = {s0_bcs:.6f} nats/edge")
print(f"    gamma = {gamma_topo_bcs:.6f} nats")
print(f"    R^2 = {R2_bcs:.6f}")
print(f"    Pearson r = {corr_cut_bcs:.6f}")

# Also check volume-law scaling (S vs |A| = 12 for all, so trivially constant)
# Instead, use the variance of S across partitions with DIFFERENT cut sizes
# to distinguish area law from volume law.
# For a volume-law state, S depends on |A| not |boundary|, so all 12+12
# partitions would give the same S. The variance should be near zero.
# For an area-law state, S varies with cut size.

S_std_over_mean = S_sweep_normal.std() / S_sweep_normal.mean() if S_sweep_normal.mean() > 0 else 0
print(f"\n  Coefficient of variation (std/mean) = {S_std_over_mean:.6f}")
print(f"  If << 1: volume-law-like (S independent of boundary)")
print(f"  If ~ O(1): area-law-like (S varies with boundary)")

# =====================================================================
#  8. MUTUAL INFORMATION AND TOTAL GGE ENTROPY
# =====================================================================
print("\n--- Section 8: Mutual information ---")

# Total GGE von Neumann entropy (product state over all (band, k) modes)
S_total_GGE = 0.0  # (local)
for alpha in range(N_bands):
    for k in range(N_vert):
        n = n_k_hybrid[alpha, k]
        if n > 1e-30 and n < 1.0 - 1e-30:
            S_total_GGE += -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

print(f"  S_total(GGE) = {S_total_GGE:.6f} nats (thermal entropy of all 192 modes)")

# Mutual information: I(A:B) = S(A) + S(B) - S(AB)
I_AB_normal = S_normal_max + S_B_normal - S_total_GGE
I_AB_bcs = S_bcs_max + S_B_bcs - S_total_GGE
print(f"\n  Max-cut partition:")
print(f"    S(A, normal) = {S_normal_max:.6f}")
print(f"    S(B, normal) = {S_B_normal:.6f}")
print(f"    S(AB) = {S_total_GGE:.6f}")
print(f"    I(A:B, normal) = {I_AB_normal:.6f} nats")
print(f"    I(A:B, BCS)    = {I_AB_bcs:.6f} nats")

# =====================================================================
#  9. PER-BAND ENTROPY DECOMPOSITION
# =====================================================================
print("\n--- Section 9: Per-band entropy decomposition ---")

S_per_band = np.zeros(N_bands)
n_eff_per_band = np.zeros(N_bands, dtype=int)
S_thermal_per_band = np.zeros(N_bands)

for alpha in range(N_bands):
    # Build per-band C_A
    C_alpha = C_bands_GGE[alpha]  # N_vert x N_vert
    A_list = sorted(A_maxcut)
    C_alpha_A = C_alpha[np.ix_(A_list, A_list)]

    nu_alpha = np.linalg.eigvalsh(C_alpha_A)
    S_a = 0.0  # (local)
    n_eff = 0
    tol = 1e-15  # (local)
    for v in nu_alpha:
        if v > tol and v < 1.0 - tol:
            S_a += -v * np.log(v) - (1.0 - v) * np.log(1.0 - v)
            n_eff += 1

    S_per_band[alpha] = S_a
    n_eff_per_band[alpha] = n_eff

    # Compare to thermal entropy of this band
    S_th = 0.0  # (local)
    for k in range(N_vert):
        n = n_k_hybrid[alpha, k]
        if n > 1e-30 and n < 1.0 - 1e-30:
            S_th += -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)
    S_thermal_per_band[alpha] = S_th

    print(f"  {mode_labels[alpha]}: S_ent = {S_a:.6f} nats, "
          f"n_eff = {n_eff}, "
          f"S_thermal = {S_th:.6f}")

print(f"\n  Sum(S_per_band) = {S_per_band.sum():.6f} nats")
print(f"  S_ent(full)     = {S_normal_max:.6f} nats")
print(f"  Match (sum should equal full for block-diagonal C): "
      f"{np.isclose(S_per_band.sum(), S_normal_max, atol=1e-6)}")

# =====================================================================
#  10. MODE DELOCALIZATION ANALYSIS
# =====================================================================
print("\n--- Section 10: Mode delocalization across cut ---")

A_list = sorted(A_maxcut)
B_list = sorted(set(range(N_vert)) - A_maxcut)

# For each TB eigenstate k, compute weight in A and B
w_A_TB = np.zeros(N_vert)
w_B_TB = np.zeros(N_vert)
for k in range(N_vert):
    w_A_TB[k] = np.sum(evecs_TB[A_list, k]**2)
    w_B_TB[k] = np.sum(evecs_TB[B_list, k]**2)

print(f"  TB eigenstate weights in region A (max-cut):")
for k in range(N_vert):
    print(f"    k={k:2d}: w_A = {w_A_TB[k]:.6f}, w_B = {w_B_TB[k]:.6f}, "
          f"asymmetry = {abs(w_A_TB[k] - 0.5):.6f}")

# Inverse participation ratio (localization measure)
ipr = np.zeros(N_vert)
for k in range(N_vert):
    ipr[k] = np.sum(evecs_TB[:, k]**4)
print(f"\n  IPR: mean = {ipr.mean():.4f}, range = [{ipr.min():.4f}, {ipr.max():.4f}]")
print(f"  Participation ratio: mean = {(1.0/ipr).mean():.2f} sites")

# =====================================================================
#  11. JACOBSON THERMODYNAMIC ANALYSIS + CC CONNECTION
# =====================================================================
print("\n--- Section 11: Jacobson CC analysis ---")

# S64 W1-B result: 94.6% of rho_ZP is OUTSIDE the Gaudin charge span.
# The entanglement entropy contributes to the CC through the spectral action.
# The relevant density is the entanglement entropy density:
#   s_ent = S_ent / A_cut
# where A_cut is the area of the cut in units of M_KK^{-2}.
#
# In Jacobson's derivation (1995), the Einstein equations emerge from dQ = T dS.
# The CC is determined by the vacuum entanglement entropy density.
# On the graph, A_cut ~ n_cut * (M_KK^{-2}) and
# rho_ent ~ (S_ent / V_cell) * T_ent * M_KK^4.

# Entanglement entropy per cut edge
s_per_edge_normal = S_normal_max / best_cut if best_cut > 0 else 0
s_per_edge_bcs = S_bcs_max / best_cut if best_cut > 0 else 0

# Bekenstein-Hawking reference: S_BH = A / (4 G_N)
# In our units: S_BH per bond = 4 * pi * a_2
G_eff = 1.0 / (16.0 * PI * a2_fold)
S_BH_per_bond = 4.0 * PI * a2_fold

print(f"  Max-cut edges: {best_cut}")
print(f"  S_ent / n_cut (normal) = {s_per_edge_normal:.6f} nats/edge")
print(f"  S_ent / n_cut (BCS)    = {s_per_edge_bcs:.6f} nats/edge")
print(f"  S_BH / bond = 4*pi*a_2 = {S_BH_per_bond:.2f}")
print(f"  Ratio S_ent/S_BH per bond = {s_per_edge_normal / S_BH_per_bond:.4e}")

# Entanglement temperature for the graph
# For a graph with diameter d, the Rindler-like temperature scale is:
# T_ent ~ 1 / (2*pi*R) where R is the characteristic cut distance
R_cut = diameter / 2.0
T_ent = 1.0 / (2.0 * PI * R_cut) if S_normal_max > 1e-20 else 0.0

# Vacuum energy from entanglement
V_cell_graph = 1.0  # one cell = one vertex  # (local)
rho_ent = S_normal_max * T_ent / V_cell_graph if S_normal_max > 1e-20 else 0.0

print(f"\n  Jacobson analysis:")
print(f"    Diameter = {diameter}, R_cut = {R_cut:.1f}")
print(f"    T_ent = 1/(2*pi*R) = {T_ent:.6f} (graph units)")
print(f"    rho_ent = S_ent * T_ent / V = {rho_ent:.6e} (graph units)")

if rho_ent > 1e-30:
    rho_ent_GeV4 = rho_ent * M_KK**4
    log_ratio = np.log10(rho_ent_GeV4 / rho_Lambda_obs)
    print(f"    rho_ent (GeV^4) = {rho_ent_GeV4:.4e}")
    print(f"    rho_Lambda_obs  = {rho_Lambda_obs:.4e} GeV^4")
    print(f"    log10(rho_ent/rho_obs) = {log_ratio:.1f}")
    CC_reduction = log_ratio
else:
    log_ratio = 0
    CC_reduction = 0
    print(f"    rho_ent effectively zero")

# Connection to W1-B result: 94.6% of rho_ZP outside Gaudin span
frac_outside_gaudin = 0.946  # (local)
print(f"\n  S64 W1-B connection:")
print(f"    {100*frac_outside_gaudin:.1f}% of rho_ZP OUTSIDE Gaudin charge span")
print(f"    Entanglement entropy probes the SPATIAL structure of rho_ZP")
print(f"    The uncontrolled (non-Gaudin) part of rho_ZP is what generates S_ent > 0")

# =====================================================================
#  12. STRUCTURAL ANALYSIS: ORIGIN OF SPATIAL ENTANGLEMENT
# =====================================================================
print("\n--- Section 12: Structural analysis ---")

# The key question: WHY is S_ent > 0 (or = 0)?
#
# For a uniform occupation n across all k-states in a band:
#   C^alpha = n * I  (diagonal)
#   C_A = n * I_{|A|}
#   All eigenvalues = n
#   S_ent = |A| * h(n) = 12 * h(n) = thermal entropy of |A| modes
#   This equals the thermal entropy, NOT entanglement entropy.
#
# For k-DEPENDENT occupations:
#   C^alpha_{ij} = sum_k n_k U[i,k] U[j,k]  != n_avg * delta_{ij}
#   The off-diagonal elements couple different sites
#   Eigenvalues of C_A differ from the uniform case
#   The DIFFERENCE between S(C_A) and the thermal case is the
#   genuine spatial entanglement.
#
# Quantify: how much does n_k vary across k for each band?

print("  Occupation spread across k-points (measures spatial entanglement source):")
for alpha in range(N_bands):
    n_min = n_k_hybrid[alpha].min()
    n_max = n_k_hybrid[alpha].max()
    n_mean = n_k_hybrid[alpha].mean()
    n_std = n_k_hybrid[alpha].std()
    spread = (n_max - n_min) / n_mean if n_mean > 1e-30 else 0
    print(f"  {mode_labels[alpha]}: n_mean = {n_mean:.6e}, n_std = {n_std:.6e}, "
          f"spread = {spread:.4f}")

# Separate the entanglement part from the thermal part
# S_thermal = 12 * h(n_mean) for each band
# S_entangle = S_ent - S_thermal
S_thermal_total = 0.0  # (local)
for alpha in range(N_bands):
    n_mean = n_k_hybrid[alpha].mean()
    if n_mean > 1e-30 and n_mean < 1.0 - 1e-30:
        S_th = 12.0 * (-n_mean * np.log(n_mean) - (1 - n_mean) * np.log(1 - n_mean))
        S_thermal_total += S_th

S_genuine_entangle = S_normal_max - S_thermal_total
print(f"\n  S_ent(total, max-cut) = {S_normal_max:.6f} nats")
print(f"  S_thermal(uniform)   = {S_thermal_total:.6f} nats")
print(f"  S_genuine_entangle   = {S_genuine_entangle:.6f} nats")
print(f"  Ratio (genuine/total) = {S_genuine_entangle/S_normal_max:.4f}"
      if S_normal_max > 0 else "  Ratio: N/A (S_ent = 0)")

# =====================================================================
#  13. GATE VERDICT
# =====================================================================
print("\n" + "=" * 76)
print("GATE VERDICT: LOCAL-ENTANGLE-64")
print("=" * 76)

# Determine S_ent status
if S_normal_max > 1e-10:
    S_status = "NONZERO"
    jacobson_open = True
else:
    S_status = "ZERO"
    jacobson_open = False

verdict = "INFO"
detail = (
    f"CG(24) graph: {N_vert} vertices, {N_edges} edges, diameter {diameter}. "
    f"S_ent(normal, max-cut) = {S_normal_max:.4f} nats, "
    f"S_ent(BCS, max-cut) = {S_bcs_max:.4f} nats. "
    f"Cut = {best_cut} edges. "
    f"S_ent status: {S_status}. "
)

if S_normal_max > 1e-10:
    detail += (
        f"Genuine entanglement = {S_genuine_entangle:.4f} nats "
        f"({100*S_genuine_entangle/S_normal_max:.1f}% of total). "
        f"Area law: s_0 = {s0_normal:.4f} nats/edge (R^2 = {R2_normal:.4f}). "
        f"I(A:B) = {I_AB_normal:.4f} nats. "
        f"Jacobson path: OPEN (S_ent > 0). "
        f"S64 W1-B: 94.6% rho_ZP outside Gaudin span. "
        f"CC from entanglement: log10(rho_ent/rho_obs) = {log_ratio:.1f}."
    )
else:
    detail += "Jacobson path: CLOSED."

print(f"\n  S_ent (normal, max-cut) = {S_normal_max:.6f} nats")
print(f"  S_ent (BCS, max-cut)    = {S_bcs_max:.6f} nats")
print(f"  S_ent genuine (non-thermal)  = {S_genuine_entangle:.6f} nats")
print(f"  S_ent status: {S_status}")
print(f"  Jacobson CC path: {'OPEN' if jacobson_open else 'CLOSED'}")
print(f"\n  Area law fit: S = {s0_normal:.6f} * n_cut + {gamma_topo_normal:.6f}")
print(f"  R^2 = {R2_normal:.6f}, Pearson r = {corr_cut_normal:.6f}")
print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =====================================================================
#  14. SAVE RESULTS
# =====================================================================
print("\n--- Section 14: Saving results ---")

out_path = os.path.join(data_dir, 's64_local_entangle.npz')

np.savez(out_path,
    # Gate
    gate_name='LOCAL-ENTANGLE-64',
    gate_verdict=verdict,
    gate_detail=detail,

    # Graph
    N_vert=N_vert,
    N_edges=N_edges,
    diameter=diameter,
    adj_cg24=adj_cg24,
    evals_L=evals_L,

    # TB Hamiltonian
    J_eff=J_eff,
    evals_TB=evals_TB,

    # GGE state
    n_k_GGE_8mode=n_k_GGE_8mode,
    F_k_GGE_8mode=F_k_GGE_8mode,
    eps_fold=eps_fold,
    beta_eff=beta_eff,
    n_k_hybrid=n_k_hybrid,
    E_hybrid=E_hybrid,

    # Partitions
    A_maxcut=np.array(sorted(A_maxcut)),
    cut_maxcut=best_cut,
    A_fiedler=np.array(sorted(A_fiedler)),
    cut_fiedler=cut_fiedler,
    A_mincut=np.array(sorted(A_mincut)),
    cut_mincut=min_cut_val,

    # Entanglement entropy
    S_normal_max=S_normal_max,
    S_bcs_max=S_bcs_max,
    S_normal_fiedler=S_normal_fiedler,
    S_bcs_fiedler=S_bcs_fiedler,
    S_normal_min=S_normal_min,
    S_bcs_min=S_bcs_min,
    S_B_normal=S_B_normal,
    S_B_bcs=S_B_bcs,
    S_total_GGE=S_total_GGE,
    S_genuine_entangle=S_genuine_entangle,
    S_thermal_total=S_thermal_total,

    # C_A eigenvalues (max-cut)
    nu_max=nu_max,

    # Per-band decomposition
    S_per_band=S_per_band,
    n_eff_per_band=n_eff_per_band,
    S_thermal_per_band=S_thermal_per_band,

    # Mutual information
    I_AB_normal=I_AB_normal,
    I_AB_bcs=I_AB_bcs,

    # Area law
    s0_normal=s0_normal,
    s0_bcs=s0_bcs,
    gamma_topo_normal=gamma_topo_normal,
    gamma_topo_bcs=gamma_topo_bcs,
    R2_normal=R2_normal,
    R2_bcs=R2_bcs,
    corr_cut_normal=corr_cut_normal,
    corr_cut_bcs=corr_cut_bcs,

    # Mode delocalization
    w_A_TB=w_A_TB,
    w_B_TB=w_B_TB,
    ipr=ipr,

    # Sweep data
    S_sweep_normal=S_sweep_normal,
    S_sweep_bcs=S_sweep_bcs,
    cut_sweep=cut_sweep,

    # Jacobson analysis
    jacobson_open=jacobson_open,
    rho_ent=rho_ent,
    T_ent=T_ent,
    CC_reduction_OOM=CC_reduction,

    # Connection to S64 W1-B
    frac_outside_gaudin=frac_outside_gaudin,
)

print(f"  Saved: {out_path}")

# =====================================================================
#  15. PLOT
# =====================================================================
print("\n--- Section 15: Generating plot ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: C_A eigenvalue spectrum (max-cut)
ax = axes[0, 0]
nu_sorted = np.sort(nu_max)[::-1]
ax.semilogy(range(len(nu_sorted)), np.clip(nu_sorted, 1e-20, None),
            'o-', color='steelblue', markersize=4, label='GGE')
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'$\nu_\alpha$')
ax.set_title(r'$C_A$ eigenvalue spectrum (max-cut)')
ax.legend()
ax.set_xlim(-0.5, len(nu_sorted) - 0.5)

# Panel 2: S_ent vs cut size (area law test)
ax = axes[0, 1]
ax.scatter(cut_sweep, S_sweep_normal, s=3, alpha=0.3, c='steelblue', label='Normal')
ax.scatter(cut_sweep, S_sweep_bcs, s=3, alpha=0.3, c='coral', label='BCS')
x_fit = np.linspace(cut_sweep.min(), cut_sweep.max(), 100)
ax.plot(x_fit, np.polyval(coeffs_normal, x_fit), 'b-', lw=2,
        label=f'Normal: {s0_normal:.4f}*n + {gamma_topo_normal:.2f}')
ax.plot(x_fit, np.polyval(coeffs_bcs, x_fit), 'r-', lw=2,
        label=f'BCS: {s0_bcs:.4f}*n + {gamma_topo_bcs:.2f}')
ax.axvline(best_cut, color='blue', ls=':', alpha=0.5, label=f'Max-cut ({best_cut})')
ax.axvline(min_cut_val, color='green', ls=':', alpha=0.5, label=f'Min-cut ({min_cut_val})')
ax.set_xlabel('Cut edges')
ax.set_ylabel(r'$S_\mathrm{ent}$ (nats)')
ax.set_title(r'Area law: $S$ vs cut size')
ax.legend(fontsize=7, loc='best')

# Panel 3: Per-band entropy decomposition
ax = axes[0, 2]
x_pos = np.arange(N_bands)
width = 0.35  # (local)
ax.bar(x_pos - width/2, S_per_band, width, label='Entanglement', color='steelblue', alpha=0.8)
ax.bar(x_pos + width/2, S_thermal_per_band, width, label='Thermal', color='coral', alpha=0.8)
ax.set_xlabel('Band')
ax.set_ylabel('Entropy (nats)')
ax.set_title('Per-band entropy decomposition')
ax.set_xticks(x_pos)
ax.set_xticklabels(mode_labels, rotation=45, fontsize=8)
ax.legend()

# Panel 4: TB eigenstate delocalization
ax = axes[1, 0]
ax.bar(range(N_vert), w_A_TB, color='steelblue', alpha=0.8, label='w(A)')
ax.bar(range(N_vert), -w_B_TB, color='coral', alpha=0.8, label='-w(B)')
ax.axhline(0.5, color='gray', ls='--', lw=1, alpha=0.5)
ax.axhline(-0.5, color='gray', ls='--', lw=1, alpha=0.5)
ax.set_xlabel('TB eigenstate k')
ax.set_ylabel('Weight in A / -weight in B')
ax.set_title('Mode delocalization across max-cut')
ax.legend(fontsize=8)

# Panel 5: Histogram of S_ent over random partitions
ax = axes[1, 1]
ax.hist(S_sweep_normal, bins=40, alpha=0.6, color='steelblue',
        label='Normal', density=True)
bcs_valid = S_sweep_bcs[np.isfinite(S_sweep_bcs)]
if len(bcs_valid) > 0:
    ax.hist(bcs_valid, bins=40, alpha=0.4, color='coral',
            label='BCS', density=True)
ax.axvline(S_normal_max, color='blue', ls='--', lw=2,
           label=f'Max-cut: {S_normal_max:.3f}')
ax.axvline(S_normal_min, color='green', ls='--', lw=2,
           label=f'Min-cut: {S_normal_min:.3f}')
ax.set_xlabel(r'$S_\mathrm{ent}$ (nats)')
ax.set_ylabel('Density')
ax.set_title(r'Distribution of $S_\mathrm{ent}$ over random bipartitions')
ax.legend(fontsize=7)

# Panel 6: Hybrid occupation spectrum
ax = axes[1, 2]
for alpha in range(N_bands):
    color = plt.cm.Set1(alpha / N_bands)
    ax.semilogy(range(N_vert), np.sort(n_k_hybrid[alpha])[::-1],
                'o-', color=color, markersize=3, label=mode_labels[alpha])
ax.set_xlabel('k-point (sorted by occupation)')
ax.set_ylabel(r'$n_{\alpha,k}$ (GGE occupation)')
ax.set_title('Hybridized GGE occupations per band')
ax.legend(fontsize=7, ncol=2)

fig.suptitle(
    f'LOCAL-ENTANGLE-64: GGE Entanglement on CG(24) Fabric\n'
    f'$S_{{ent}}$ = {S_normal_max:.4f} nats (normal), {S_bcs_max:.4f} nats (BCS) | '
    f'Cut = {best_cut}/{N_edges} edges | Genuine = {S_genuine_entangle:.4f} nats',
    fontsize=12, fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plot_path = os.path.join(data_dir, 's64_local_entangle.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.1f}s")

print("\n" + "=" * 76)
print("LOCAL-ENTANGLE-64 COMPLETE")
print("=" * 76)
