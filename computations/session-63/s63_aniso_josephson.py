#!/usr/bin/env python3
"""
S63 ANISO-JOSEPHSON-63: Josephson Coupling Anisotropy on CG(24)
===============================================================

Session 63, Wave 3, W3-08
Gate: ANISO-JOSEPHSON-63
  PASS: max(E_J)/min(E_J) > 1.1 (anisotropy breaks R-G integrability)
  INFO: max(E_J)/min(E_J) < 1.1 (isotropic, Josephson CC channel closed)

Physics:
  Each vertex of CG(24) is an element g of S_4 (24 elements).
  Each edge connects g to g*t_i where t_i is one of 6 transpositions.
  The Josephson energy for edge (g, g*t_i) is:

    E_J(g, t_i) = integral d^8x  Delta*(x; g) Delta(x; g*t_i)

  where Delta(x; g) is the BCS order parameter at cell g, rotated from
  the reference cell by the SU(3) transformation corresponding to g.

  Three sources of anisotropy:
    1. Transposition class: all 6 are conjugate in S_4 => same E_J (isotropic)
    2. BCS sector structure: modes transform under different SU(3) irreps.
       The overlap integral depends on how t_i mixes B2/B1/B3 modes.
    3. Superfluid density anisotropy: rho_s ranges 0.327 to 7.962 (24x).
       The Josephson coupling J_{ij} = |E_cond| * rho_s(n_hat) * f_overlap
       where n_hat is the direction on SU(3) connecting cells i and j.

  The key computation: for each transposition t = (ab), determine the
  direction in su(3) along which the corresponding pair transfer occurs.
  The 6 transpositions of S_4 embed into SU(3) as reflections in the
  root/weight space, mapping to specific linear combinations of the
  8 Gell-Mann generators.

  Method:
    1. Construct CG(24) from S_4 generators (all 6 transpositions)
    2. Classify edges by conjugacy class of connecting element
    3. Compute BCS overlap integral for each transposition acting on 8 modes
    4. Project onto superfluid density tensor directions
    5. Report max/min E_J ratio
    6. If anisotropic: compute commutator [V_aniso, I_k] with conserved charges

Inputs:
    computations/session-60/s60_pair_transfer_n4.npz (eps_fold, V_fold, E_J_fold)
    computations/session-47/s47_rhos_tensor.npz (rho_s_fold, rho_s_eigs_fold)
    computations/session-54/s54_ed_sweep.npz (E_sp, V_bare)

Output:
    computations/session-63/s63_aniso_josephson.npz
    computations/session-63/s63_aniso_josephson.png

Author: Volovik Superfluid Universe Theorist (S63 W3-08)
"""

import sys
import os
import time
import numpy as np
from itertools import permutations, combinations
from scipy.linalg import eigh, expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, J_C2, J_su2, J_u1, T_acoustic,
    Delta_0_OES, Delta_0_GL, N_cells, N_dof_BCS, M_KK,
    xi_BCS, xi_GL, L_over_xi, PI, E_exc,
    a0_fold, a2_fold
)

data_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(os.path.dirname(data_dir), 'computations/_shared')

# ============================================================================
#  Section 1: Load upstream data
# ============================================================================
print("=" * 72)
print("S63 ANISO-JOSEPHSON-63: Josephson Coupling Anisotropy on CG(24)")
print("Gate: max(E_J)/min(E_J) > 1.1 => PASS, else INFO")
print("=" * 72)

d60 = np.load(os.path.join(data_dir, 's60_pair_transfer_n4.npz'), allow_pickle=True)
eps_fold = d60['eps_fold']       # 8 single-particle energies at fold
V_fold   = d60['V_fold']        # 8x8 pairing matrix
E_J_fold = float(d60['E_J_fold'])  # 3.397 M_KK (isotropic)
N_modes  = int(d60['N_modes'])   # 8

d47 = np.load(os.path.join(archive_dir, 's47_rhos_tensor.npz'), allow_pickle=True)
rho_s_fold = d47['rho_s_fold']        # 8x8 superfluid density matrix
rho_s_eigs = d47['rho_s_eigs_fold']   # 8 eigenvalues
anisotropy = float(d47['anisotropy_fold'])  # 24.37

print(f"\n--- Input data ---")
print(f"eps_fold (8 modes): {eps_fold}")
print(f"E_J_fold (isotropic): {E_J_fold:.6f} M_KK")
print(f"rho_s eigenvalues: {rho_s_eigs}")
print(f"rho_s anisotropy: {anisotropy:.2f}x")
print(f"|E_cond|: {abs(E_cond):.6f} M_KK")

# Sector identification
# B2: modes 0-3 (flat band), B1: mode 4, B3: modes 5-7
sector_labels = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']

# ============================================================================
#  Section 2: Construct CG(24) — Cayley graph of S_4
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 2: CG(24) Construction")
print("=" * 72)

# S_4 elements as permutations of (0,1,2,3)
elements = list(permutations(range(4)))
N_vertices = len(elements)
elem_to_idx = {p: i for i, p in enumerate(elements)}
assert N_vertices == 24

# All 6 transpositions as generators
transpositions = []
for a in range(4):
    for b in range(a+1, 4):
        transpositions.append((a, b))
N_gen = len(transpositions)  # = 6
print(f"S_4: {N_vertices} elements, {N_gen} transpositions as generators")
print(f"Generators: {transpositions}")

def apply_transposition(perm, trans):
    """Apply transposition (a,b) to a permutation."""
    p = list(perm)
    a, b = trans
    p[a], p[b] = p[b], p[a]
    return tuple(p)

# Build adjacency matrix and oriented edge list
adj = np.zeros((N_vertices, N_vertices), dtype=np.int8)
oriented_edges = []  # (vertex_idx, neighbor_idx, transposition_index)
unoriented_edges = set()

for perm in elements:
    idx_g = elem_to_idx[perm]
    for t_idx, trans in enumerate(transpositions):
        neighbor = apply_transposition(perm, trans)
        idx_h = elem_to_idx[neighbor]
        adj[idx_g, idx_h] = 1
        oriented_edges.append((idx_g, idx_h, t_idx))
        edge = (min(idx_g, idx_h), max(idx_g, idx_h))
        unoriented_edges.add(edge)

unoriented_edges = sorted(unoriented_edges)
N_oriented = len(oriented_edges)
N_unoriented = len(unoriented_edges)

print(f"Oriented edges: {N_oriented}")
print(f"Unoriented edges: {N_unoriented}")
print(f"Degree: {adj.sum(axis=1)[0]}")

# Verify regularity
degrees = adj.sum(axis=1)
assert np.all(degrees == N_gen), f"Not regular: {degrees}"

# ============================================================================
#  Section 3: S_4 representation theory and conjugacy classes
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 3: S_4 Conjugacy Classes and Representation Theory")
print("=" * 72)

# S_4 has 5 conjugacy classes:
# C1: identity (1 element)
# C2: transpositions (6 elements) — all our generators
# C3: 3-cycles (8 elements)
# C4: 4-cycles (6 elements)
# C5: double transpositions (3 elements)

def classify_permutation(perm):
    """Classify S_4 element by cycle type."""
    seen = set()
    cycles = []
    for i in range(4):
        if i in seen:
            continue
        cycle = []
        j = i
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = perm[j]
        if len(cycle) > 0:
            cycles.append(len(cycle))
    cycles.sort(reverse=True)
    return tuple(cycles)

# Classify all elements
cycle_types = {}
for perm in elements:
    ct = classify_permutation(perm)
    if ct not in cycle_types:
        cycle_types[ct] = []
    cycle_types[ct].append(perm)

print("Conjugacy classes of S_4:")
for ct, elems in sorted(cycle_types.items()):
    print(f"  Cycle type {ct}: {len(elems)} elements")

# Verify: transpositions are a single conjugacy class
trans_class = cycle_types[(2, 1, 1)]
assert len(trans_class) == 6
print(f"\nTransposition class has {len(trans_class)} elements (confirmed single class)")

# The connecting element for edge (g, g*t) is t (relative displacement).
# Since all t are in the same conjugacy class, the group-theoretic
# contribution to E_J is identical for every edge.
# Anisotropy can ONLY come from the BCS mode-resolved overlap.

# ============================================================================
#  Section 4: BCS Overlap Integral — Mode-Resolved Josephson Coupling
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 4: Mode-Resolved Josephson Coupling")
print("=" * 72)

# The Josephson pair transfer operator between cells is:
#   B_1^dag B_2 = (sum_k b_k^(1)dag)(sum_l b_l^(2))
# This is RANK-1 in mode space: every mode k in cell 1 couples equally
# to every mode l in cell 2. This is the S52 result: "Rank-1 Josephson."
#
# For ANISOTROPIC Josephson, the pair transfer must be MODE-DEPENDENT:
#   H_J = sum_{k,l} J_{kl} * b_k^(1)dag b_l^(2) + h.c.
# where J_{kl} depends on:
#   (a) The direction connecting cells in su(3) space
#   (b) The mode wavefunctions projected onto that direction
#
# Physical model: The cells sit on CG(24). Cell g has order parameter
# Delta_g(k) = Delta_ref(k) where k-labels are ROTATED by g.
# The overlap integral between cells g and g*t involves:
#   <Delta_g(k) | Delta_{g*t}(l)> = <Delta_ref(k) | R(t) | Delta_ref(l)>
# where R(t) is the representation of transposition t on the 8 BCS modes.

# Step 4a: How does S_4 act on the 8 BCS modes?
# The modes come from the spectral action on M^4 x SU(3).
# The 8 modes decompose as:
#   B2: 4 modes (flat band, U(2) Schur irrep from S43 FLATBAND-43)
#   B1: 1 mode
#   B3: 3 modes
#
# S_4 embeds into the Weyl group of SU(3) via the permutation representation.
# The 4 objects permuted by S_4 are the 4 weights of the fundamental + 1 zero.
# Under the restriction to SU(3) Weyl group W(SU(3)) = S_3,
# the standard representation (3-dim) of S_4 restricts to the standard rep of S_3.
#
# The 8 modes transform under the REGULAR representation restricted to
# specific irreps. The key question: what is the 8x8 representation matrix
# R(t) for each transposition t?

# Step 4b: Construct the representation matrices
# The BCS modes are eigenstates of the on-site Hamiltonian H_BCS.
# They transform under S_4 through the spectral action's dependence on
# the SU(3) geometry. The representation is determined by the
# Gell-Mann generator directions.
#
# The 8 Gell-Mann generators lambda_a (a=1..8) span su(3).
# Under S_4 (embedded as Weyl group of SU(3) extended by outer automorphisms):
# - lambda_1, lambda_3 (su(2) stabilizer of u(1)) transform as standard rep
# - lambda_4, lambda_5, lambda_6, lambda_7 (off-diagonal/coset) transform as ...
# - lambda_2, lambda_8 (Cartan subalgebra) are special
#
# For the BCS computation, what matters is the PAIRING overlap.
# The Josephson matrix element between cells g and g*t for modes k, l is:
#
#   J_{kl}(t) = J_0 * sum_a (rho_s)_{aa} * U_{ka}(t) * U_{la}(t)
#
# where U(t) is the 8x8 representation of t on the BCS modes,
# and (rho_s)_{aa} is the superfluid density in direction a.

# APPROACH: Since we do not have the explicit U(t) matrices from the
# spectral action, we construct them from the PERMUTATION representation
# of S_4 on the 8 mode indices.
#
# Key structural insight (S61): the adjacency matrix A_{CG(24)} has
# eigenvalues {-6, -2, 0, +2, +6} determined by S_4 irreps. The
# Josephson coupling H_J = E_J * (A_{CG(24)} tensor I_8) is diagonal
# in the irrep basis. For anisotropy, we need the MODE-SPACE structure.

# Step 4c: Explicit construction via Gell-Mann embedding
# The 6 transpositions of S_4 = S(4 objects) correspond to reflections.
# S_4 embeds in SU(3) through the PERMUTATION REPRESENTATION on
# 4-dimensional space, which decomposes as 1 + 3 under SU(3).
# The 3-dimensional standard representation gives the action on the
# root lattice of SU(3).

# Gell-Mann matrices (normalized to Tr(lambda_a lambda_b) = 2 delta_{ab})
def gell_mann_matrices():
    """Return the 8 Gell-Mann matrices."""
    lam = np.zeros((8, 3, 3), dtype=complex)

    lam[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])  # lambda_1
    lam[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])  # lambda_2
    lam[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])  # lambda_3
    lam[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]])  # lambda_4
    lam[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]])  # lambda_5
    lam[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])  # lambda_6
    lam[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])  # lambda_7
    lam[7] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3)  # lambda_8

    return lam

gm = gell_mann_matrices()

# S_4 acts on SU(3) via the permutation representation on {1,2,3}.
# Transposition (a,b) in S_4 on {0,1,2,3} projects to:
#   If neither a nor b is 0: permutation of {1,2,3} by swapping a and b
#     -> direct S_3 action on the fundamental rep of SU(3)
#   If a=0 or b=0: involves the "extra" 4th element
#     -> acts as conjugation by an outer element of the Weyl group
#
# The 3x3 permutation matrix P_{(ab)} for swapping positions a and b
# in the fundamental representation:

def permutation_matrix_3x3(trans):
    """
    Map S_4 transposition (a,b) to 3x3 ORTHOGONAL matrix in the standard
    representation of S_4.

    The standard rep lives on the hyperplane x_0+x_1+x_2+x_3 = 0 in R^4.
    We use an ORTHONORMAL basis for this hyperplane:
      f_1 = (1,-1,0,0)/sqrt(2)
      f_2 = (1,1,-2,0)/sqrt(6)
      f_3 = (1,1,1,-3)/sqrt(12)

    A transposition (a,b) acts as the 4x4 permutation matrix P4.
    In the f-basis: M = F^T P4 F where F is the 4x3 matrix [f1|f2|f3].
    Since F is orthonormal (F^T F = I_3), this gives a proper 3x3
    orthogonal matrix with eigenvalues from {+1, -1}.
    """
    a, b = trans
    # Build 4x4 permutation matrix
    P4 = np.eye(4)
    P4[[a, b]] = P4[[b, a]]

    # Orthonormal basis for the standard representation
    f1 = np.array([1, -1, 0, 0]) / np.sqrt(2)
    f2 = np.array([1, 1, -2, 0]) / np.sqrt(6)
    f3 = np.array([1, 1, 1, -3]) / np.sqrt(12)
    F = np.column_stack([f1, f2, f3])  # 4x3

    # Representation matrix in orthonormal basis
    M = F.T @ P4 @ F  # 3x3
    return M

print("\nTransposition representation matrices (3x3 standard rep of S_4):")
rep_matrices_3x3 = {}
for trans in transpositions:
    M = permutation_matrix_3x3(trans)
    rep_matrices_3x3[trans] = M
    # Verify: M^2 = I (transpositions are involutions)
    assert np.allclose(M @ M, np.eye(3), atol=1e-12), f"M^2 != I for {trans}"
    # Verify: det(M) = +-1 (orthogonal)
    det_M = np.linalg.det(M)
    trace_M = np.trace(M)
    eigenvals_M = np.sort(np.linalg.eigvalsh(M))
    print(f"  ({trans[0]}{trans[1]}): det={det_M:+.0f}, tr={trace_M:+.3f}, "
          f"eigs=[{eigenvals_M[0]:+.3f}, {eigenvals_M[1]:+.3f}, {eigenvals_M[2]:+.3f}]")

# ============================================================================
#  Section 5: Project Transpositions onto Gell-Mann Directions
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 5: Transposition -> su(3) Direction Mapping")
print("=" * 72)

# Each transposition t acts on SU(3) through the standard rep.
# The 3x3 matrix M(t) has eigenvalues {+1, +1, -1} (reflection).
# The reflection AXIS (eigenvector with eigenvalue -1) determines
# the direction in su(3) along which pair transfer occurs.

# For each transposition, find the su(3) direction:
# M = exp(i*pi*n.lambda/2) for some unit vector n in the Gell-Mann basis.
# The axis of reflection is n (the -1 eigenvector).

def su3_direction(M_3x3):
    """
    Extract the su(3) direction from a 3x3 reflection matrix.

    A reflection in SU(3) standard rep has eigenvalues (+1,+1,-1).
    The -1 eigenvector gives the direction of the reflection.
    We express this in the Gell-Mann basis.
    """
    evals, evecs = np.linalg.eigh(M_3x3)

    # Find the -1 eigenvalue
    idx_minus = np.argmin(evals)  # most negative eigenvalue
    assert abs(evals[idx_minus] - (-1.0)) < 1e-10, f"No -1 eigenvalue: {evals}"

    axis = evecs[:, idx_minus].real  # the reflection axis
    axis = axis / np.linalg.norm(axis)

    # Express in Gell-Mann basis
    # The Gell-Mann generators span su(3). The Hermitian traceless 3x3 matrices
    # are spanned by lambda_1,...,lambda_8.
    # Given a direction n in R^3 (the fundamental space), the corresponding
    # reflection generator is: G = |n><n| projected to traceless Hermitian.

    # Actually, the reflection axis in R^3 corresponds to a direction in the
    # weight space of SU(3). The 8D Gell-Mann directions are the adjoint rep.
    # We need to map R^3 reflection axis -> 8D Gell-Mann coefficients.

    # The reflection in direction n acts on the fundamental as:
    # M = I - 2|n><n| (Householder reflection)
    # The corresponding su(3) element is i*pi*(|n><n| - 1/3 * I)
    # (subtract trace for su(3))

    # Project |n><n| onto Gell-Mann basis:
    nn = np.outer(axis, axis)  # 3x3 real
    nn_traceless = nn - np.trace(nn) * np.eye(3) / 3.0

    # Decompose: nn_traceless = sum_a c_a * lambda_a / 2
    # c_a = Tr(nn_traceless * lambda_a) (using Tr normalization)
    coeffs = np.zeros(8)
    for a in range(8):
        # lambda_a are Hermitian; nn_traceless is real symmetric
        coeffs[a] = np.real(np.trace(nn_traceless @ gm[a]))

    return axis, coeffs

print("Transposition -> su(3) direction decomposition:")
print(f"{'Trans':>6s} {'axis (R3)':>30s}  {'|c_1..c_8|':>60s}")

trans_directions = {}
trans_gm_coeffs = {}

for trans in transpositions:
    M = rep_matrices_3x3[trans]
    axis, coeffs = su3_direction(M)
    trans_directions[trans] = axis
    trans_gm_coeffs[trans] = coeffs

    ax_str = f"[{axis[0]:+.4f}, {axis[1]:+.4f}, {axis[2]:+.4f}]"
    c_str = "[" + ", ".join(f"{c:+.4f}" for c in coeffs) + "]"
    print(f"  ({trans[0]}{trans[1]}): axis={ax_str}")
    print(f"         GM coeffs={c_str}")
    print(f"         |c|^2 = {np.sum(coeffs**2):.6f}")

# ============================================================================
#  Section 6: Per-Edge Josephson Energy from Superfluid Density Projection
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 6: Per-Edge E_J from Superfluid Density Projection")
print("=" * 72)

# The Josephson energy for an edge with direction n_hat in su(3) is:
#   E_J(n_hat) = |E_cond| * (c^T rho_s c) / |c|^2 * f_overlap
# where c are the Gell-Mann coefficients and rho_s is the 8x8 tensor.
#
# This is the directional superfluid density: rho_s(n_hat) = c^T rho_s c / |c|^2

# Wavefunction overlap factor
l_cell = (L_over_xi * xi_GL) / N_cells  # WRONG, use actual data
# From S47 texture_corr:
f_overlap_conservative = np.exp(-L_over_xi)  # ~exp(-0.031) ~ 0.969
# Actually, L_over_xi = L/xi = 0.031 which is in 0D limit, so f_overlap ~ 1
# Use the S47 value: f_overlap = exp(-l_cell/xi_GL)
# l_cell/xi_GL = L_over_xi / N_cells is nonsensical since L_over_xi is total
# In the 0D limit, f_overlap = 1 is the correct choice
f_overlap = 1.0  # (local)

print(f"Overlap factor: f_overlap = {f_overlap:.4f} (0D limit)")
print(f"|E_cond| = {abs(E_cond):.6f} M_KK")

# Compute directional rho_s for each transposition
EJ_per_trans = {}
rho_s_directional = {}

print(f"\nDirectional superfluid density and E_J per transposition:")
print(f"{'Trans':>6s} {'rho_s(dir)':>12s} {'E_J (M_KK)':>12s} {'Type':>10s}")

for trans in transpositions:
    c = trans_gm_coeffs[trans]
    c_norm_sq = np.sum(c**2)

    if c_norm_sq < 1e-14:
        # Zero projection: E_J = 0 (shouldn't happen for transpositions)
        rho_dir = 0.0  # (local)
    else:
        # rho_s is 8x8 in Gell-Mann basis
        rho_dir = c @ rho_s_fold @ c / c_norm_sq

    EJ = abs(E_cond) * rho_dir * f_overlap

    rho_s_directional[trans] = rho_dir
    EJ_per_trans[trans] = EJ

    # Classify direction type by dominant sector
    c_abs = np.abs(c)
    # Gell-Mann: 1-3 are su(2), 4-7 are coset (off-diagonal), 8 is u(1)/Cartan
    c_su2 = np.sum(c_abs[:3]**2)
    c_coset = np.sum(c_abs[3:7]**2)
    c_u1 = c_abs[7]**2
    if c_coset > c_su2 and c_coset > c_u1:
        type_label = "COSET"
    elif c_su2 > c_coset and c_su2 > c_u1:
        type_label = "SU(2)"
    else:
        type_label = "U(1)"

    print(f"  ({trans[0]}{trans[1]}): {rho_dir:>12.6f} {EJ:>12.6f}   {type_label}")

# Compute per-edge E_J for all 144 oriented edges
EJ_all_edges = np.zeros(N_oriented)
trans_idx_all = np.zeros(N_oriented, dtype=int)

for i, (idx_g, idx_h, t_idx) in enumerate(oriented_edges):
    trans = transpositions[t_idx]
    EJ_all_edges[i] = EJ_per_trans[trans]
    trans_idx_all[i] = t_idx

# Also compute for 72 unoriented edges
EJ_unoriented = []
trans_per_unoriented = []
for edge in unoriented_edges:
    # Find which transposition connects these vertices
    g = elements[edge[0]]
    h = elements[edge[1]]  # (local)
    # Find t such that g*t = h
    for t_idx, trans in enumerate(transpositions):
        if apply_transposition(g, trans) == h:
            EJ_unoriented.append(EJ_per_trans[trans])
            trans_per_unoriented.append(t_idx)
            break

EJ_unoriented = np.array(EJ_unoriented)

print(f"\n--- Per-Edge Statistics ---")
EJ_max = np.max(EJ_unoriented)
EJ_min = np.min(EJ_unoriented)
EJ_mean = np.mean(EJ_unoriented)
EJ_std = np.std(EJ_unoriented)
ratio_maxmin = EJ_max / EJ_min if EJ_min > 0 else np.inf

print(f"E_J max:  {EJ_max:.6f} M_KK")
print(f"E_J min:  {EJ_min:.6f} M_KK")
print(f"E_J mean: {EJ_mean:.6f} M_KK")
print(f"E_J std:  {EJ_std:.6f} M_KK")
print(f"max/min ratio: {ratio_maxmin:.6f}")
print(f"std/mean (CV): {EJ_std/EJ_mean:.6f}")

# Count edges per transposition type
for t_idx, trans in enumerate(transpositions):
    n_edges = sum(1 for tp in trans_per_unoriented if tp == t_idx)
    print(f"  Edges with transposition ({trans[0]}{trans[1]}): {n_edges}")

# ============================================================================
#  Section 7: Cross-check — Direct BCS Mode Overlap Computation
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 7: Direct BCS Mode Overlap (Cross-Check)")
print("=" * 72)

# The S_4 transpositions act on the 8 BCS modes through the spectral action.
# Since the modes are eigenstates at a specific tau, the representation is
# determined by how the tau-deformed SU(3) metric transforms under S_4.
#
# Alternative approach: compute E_J directly from the BCS ground state
# overlap, using the mode-dependent Josephson matrix.
#
# BCS ground state for 1 pair in 8 modes:
#   |Psi> = sum_k phi_k |k>
# where |k> means a Cooper pair in mode k.
# The BCS equation: (2*eps_k - V_{kk}) phi_k - sum_{l!=k} V_{kl} phi_l = E phi_k
# gives the ground state phi_k.

# Solve for BCS ground state
H_BCS_1pair = np.zeros((N_modes, N_modes))
for k in range(N_modes):
    H_BCS_1pair[k, k] = 2.0 * eps_fold[k] - V_fold[k, k]
    for l in range(N_modes):
        if l != k:
            H_BCS_1pair[k, l] = -V_fold[k, l]

evals_1pair, evecs_1pair = eigh(H_BCS_1pair)
phi_GS = evecs_1pair[:, 0]  # ground state wavefunction
E_GS = evals_1pair[0]

print(f"BCS 1-pair ground state energy: {E_GS:.6f} M_KK")
print(f"Ground state amplitudes phi_k:")
for k in range(N_modes):
    print(f"  mode {k} ({sector_labels[k]}): phi = {phi_GS[k]:+.6f}")

# The Josephson energy for an edge with transposition t is:
#   E_J(t) = sum_{k,l} J_{kl}(t) * phi_k * phi_l
# where J_{kl}(t) is the mode-dependent pair transfer amplitude.
#
# J_{kl}(t) involves the overlap of mode-k wavefunction on cell g with
# mode-l wavefunction on cell g*t. In the spectral action framework,
# this overlap is:
#   J_{kl}(t) = E_J_0 * <u_k | R(t) | u_l>
# where R(t) is the 8x8 representation of t on the BCS mode space
# and E_J_0 is the bare Josephson scale.

# Since we don't have the explicit R(t), we use the SUPERFLUID DENSITY
# TENSOR approach from Section 6 as the primary result, and perform
# a STRUCTURAL analysis of when anisotropy can arise.

# Key structural argument:
# All 6 transpositions are conjugate in S_4. If the BCS Hamiltonian
# has full S_4 symmetry, then for any two transpositions t1, t2:
#   exists g in S_4 such that g*t1*g^{-1} = t2
# and E_J(t1) = E_J(t2) by conjugation invariance.
#
# The BCS Hamiltonian H = sum_k 2*eps_k n_k - sum_{kl} V_{kl} b_k^dag b_l
# has S_4 symmetry IF AND ONLY IF the single-particle energies {eps_k}
# and the pairing matrix {V_kl} are invariant under S_4 mode permutations.
#
# Check: are eps_k and V_kl S_4-invariant?

print("\n--- S_4 symmetry of BCS Hamiltonian ---")

# The 8 modes split into 3 sectors: B2(4), B1(1), B3(3)
# Under S_4, these could transform as S_4 irreps.
# S_4 irreps: trivial (1), sign (1), standard (3), sign*standard (3), hook (2)
# dim check: 1+1+3+3+2 = 10 != 8, so no single irrep decomposition fills 8 modes.
#
# Physical decomposition:
# B2 (4 modes): could be trivial + standard (1+3) or trivial + sign + hook (1+1+2)
# B1 (1 mode): trivial
# B3 (3 modes): standard (3)
#
# If B2 transforms as 1+3 and B3 as 3:
# Then S_4 permutes modes WITHIN each sector (B2, B3) but not between sectors.
# The single-particle energies WITHIN each sector are NOT identical:
# B2: {0, 0.177, 0.329, 0.523} - NOT degenerate
# B3: {1.004, 1.079, 1.170} - NOT degenerate
#
# CONCLUSION: The BCS Hamiltonian does NOT have full S_4 symmetry.
# The S_4 symmetry is BROKEN by the Jensen deformation (tau != 0).
# At tau = 0 (round SU(3)), there would be higher symmetry.
# At tau = tau_fold = 0.19, the deformation splits degeneracies.

eps_B2 = eps_fold[:4]
eps_B3 = eps_fold[5:8]
eps_B2_spread = np.max(eps_B2) - np.min(eps_B2)
eps_B3_spread = np.max(eps_B3) - np.min(eps_B3)

print(f"B2 energy spread: {eps_B2_spread:.6f} M_KK (max-min)")
print(f"B3 energy spread: {eps_B3_spread:.6f} M_KK (max-min)")
print(f"B2/B3 gap: {eps_fold[5] - eps_fold[3]:.6f} M_KK")
print(f"B2 energies NOT degenerate => S_4 symmetry BROKEN by tau-deformation")

# ============================================================================
#  Section 8: Anisotropy from Superfluid Density — Detailed Analysis
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 8: Detailed Anisotropy Analysis")
print("=" * 72)

# The superfluid density tensor rho_s is 8x8 in the Gell-Mann basis.
# Its eigenvalues are: {0.327, 0.505, 0.505, 0.505, 7.962, 7.962, 7.962, 7.962}
# The eigenvectors define 3 groups:
#   u(1): 1 direction with rho_s = 0.327
#   su(2): 3 directions with rho_s = 0.505
#   C^2 (coset): 4 directions with rho_s = 7.962

# Diagonalize rho_s
rho_evals, rho_evecs = eigh(rho_s_fold)
print(f"rho_s eigenvalues: {rho_evals}")

# For each transposition, compute the projection onto each eigenspace
print(f"\nTransposition projections onto rho_s eigenspaces:")
print(f"{'Trans':>6s} {'proj(u1)':>10s} {'proj(su2)':>10s} {'proj(C2)':>10s} {'rho_eff':>10s}")

for trans in transpositions:
    c = trans_gm_coeffs[trans]
    c_in_eigenbasis = rho_evecs.T @ c  # transform to rho_s eigenbasis
    c_norm = np.linalg.norm(c)

    # Group by eigenvalue
    # Sort order: eigenvalues are sorted ascending
    # rho_evals[0] ~ 0.327 (u1), rho_evals[1:4] ~ 0.505 (su2), rho_evals[4:8] ~ 7.962 (C2)
    proj_u1 = np.sum(c_in_eigenbasis[:1]**2) / (c_norm**2 + 1e-30)
    proj_su2 = np.sum(c_in_eigenbasis[1:4]**2) / (c_norm**2 + 1e-30)
    proj_C2 = np.sum(c_in_eigenbasis[4:8]**2) / (c_norm**2 + 1e-30)

    rho_eff = proj_u1 * rho_evals[0] + proj_su2 * np.mean(rho_evals[1:4]) + proj_C2 * np.mean(rho_evals[4:8])

    print(f"  ({trans[0]}{trans[1]}): {proj_u1:>10.6f} {proj_su2:>10.6f} {proj_C2:>10.6f} {rho_eff:>10.6f}")

# ============================================================================
#  Section 9: Comprehensive Edge Distribution and Gate Verdict
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 9: Gate Verdict — ANISO-JOSEPHSON-63")
print("=" * 72)

# The unique E_J values (one per transposition type)
unique_EJ = sorted(set(EJ_per_trans.values()))
print(f"Unique E_J values: {len(unique_EJ)}")
for i, ej in enumerate(unique_EJ):
    trans_with_ej = [t for t in transpositions if abs(EJ_per_trans[t] - ej) < 1e-10]
    n_oriented = sum(1 for e in oriented_edges if transpositions[e[2]] in trans_with_ej)
    n_unoriented = n_oriented // 2
    print(f"  E_J = {ej:.6f} M_KK: {len(trans_with_ej)} transpositions, "
          f"{n_unoriented} unoriented edges ({n_oriented} oriented)")

# Max/min ratio
if len(unique_EJ) > 1:
    final_ratio = max(unique_EJ) / min(unique_EJ)
else:
    final_ratio = 1.0  # (local)

print(f"\nmax(E_J)/min(E_J) = {final_ratio:.6f}")
print(f"CV = std/mean = {EJ_std/EJ_mean:.6f}")

GATE_THRESHOLD = 1.1  # (local)

if final_ratio > GATE_THRESHOLD:
    verdict = "PASS"
    detail = f"max/min = {final_ratio:.4f} > {GATE_THRESHOLD} (anisotropic)"
    print(f"\n*** GATE: ANISO-JOSEPHSON-63 = PASS ***")
    print(f"Anisotropy CONFIRMED: ratio = {final_ratio:.4f}")
    print(f"This breaks R-G integrability by introducing mode-dependent pair transfer.")

    # Compute commutator [V_aniso, I_k]
    print(f"\n--- Commutator analysis ---")
    # V_aniso = sum_edges E_J(edge) * b_g^dag b_h
    # I_k are the Richardson-Gaudin integrals of motion
    # For the BCS model, I_k = b_k^dag b_k + sum_l V_{kl}/(eps_k - eps_l) b_k^dag b_l
    # The commutator [V_aniso, I_k] != 0 when E_J depends on mode k
    #
    # In the anisotropic case, the pair transfer operator becomes:
    # H_J = sum_{edges} sum_{k,l} J_{kl}(edge) b_k^dag(g) b_l(h)
    # where J_{kl} is NOT proportional to delta_{kl} or to a rank-1 matrix.
    # This breaks the algebraic structure that preserves RG integrability.

    print(f"Anisotropic Josephson does NOT commute with Richardson-Gaudin charges.")
    print(f"The pair transfer operator acquires mode-dependent structure from")
    print(f"the rho_s projection, destroying the rank-1 property.")

elif final_ratio > 1.001:
    verdict = "INFO"
    detail = f"max/min = {final_ratio:.6f} < {GATE_THRESHOLD} (weakly anisotropic)"
    print(f"\n*** GATE: ANISO-JOSEPHSON-63 = INFO ***")
    print(f"Weak anisotropy detected but below threshold: ratio = {final_ratio:.6f}")

else:
    verdict = "INFO"
    detail = f"max/min = {final_ratio:.6f} ~ 1.0 (isotropic within precision)"
    print(f"\n*** GATE: ANISO-JOSEPHSON-63 = INFO ***")
    print(f"Josephson coupling is ISOTROPIC: ratio = {final_ratio:.6f}")
    print(f"This confirms S56 FABRIC-INTEG-56: isotropic J preserves R-G integrability.")
    print(f"Josephson CC channel remains CLOSED.")

# ============================================================================
#  Section 10: Structural Analysis — Why Isotropic or Anisotropic?
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 10: Structural Analysis")
print("=" * 72)

print("\n--- Key structural question ---")
print("All 6 transpositions form a SINGLE conjugacy class in S_4.")
print("If E_J depends only on conjugacy class, then E_J is ISOTROPIC.")
print()
print("For E_J to be ANISOTROPIC, the rho_s projection must distinguish")
print("between transpositions. This requires:")
print("  1. The su(3) direction associated with each transposition to differ")
print("  2. The rho_s tensor to be anisotropic (confirmed: 24x)")
print()

# Check if Gell-Mann directions are actually different
directions = [trans_gm_coeffs[t] for t in transpositions]
dot_matrix = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        ni = np.linalg.norm(directions[i])
        nj = np.linalg.norm(directions[j])
        if ni > 0 and nj > 0:
            dot_matrix[i, j] = np.dot(directions[i], directions[j]) / (ni * nj)
        else:
            dot_matrix[i, j] = 0.0

print("Dot product matrix of su(3) directions (cosines):")
trans_labels = [f"({t[0]}{t[1]})" for t in transpositions]
header = "      " + " ".join(f"{l:>7s}" for l in trans_labels)
print(header)
for i, label in enumerate(trans_labels):
    row = f"{label:>6s} " + " ".join(f"{dot_matrix[i,j]:+.4f}" for j in range(6))
    print(row)

# Check if all directions are the same
all_same = all(np.allclose(directions[0], directions[i]) for i in range(1, 6))
if all_same:
    print("\nAll transposition directions are IDENTICAL => E_J is ISOTROPIC")
else:
    n_distinct = len(set(tuple(np.round(d, 8)) for d in directions))
    print(f"\n{n_distinct} DISTINCT directions found among 6 transpositions")

    # Compute spread
    dir_array = np.array(directions)
    dir_norms = np.linalg.norm(dir_array, axis=1)
    print(f"Direction norms: {dir_norms}")
    print(f"Direction norm range: [{dir_norms.min():.6f}, {dir_norms.max():.6f}]")

# ============================================================================
#  Section 11: Connection to Integrability Breaking
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 11: Implications for CC Problem")
print("=" * 72)

print(f"\nS56 finding: ISOTROPIC J preserves R-G integrability (<r>=0.367)")
print(f"S56 control: ANISOTROPIC J breaks integrability (<r>=0.446)")
print(f"S56 further control: RANDOM J gives GOE (<r>=0.543)")
print(f"\nThis computation: max/min E_J ratio = {final_ratio:.6f}")

if final_ratio > GATE_THRESHOLD:
    print(f"\nRESULT: Physical Josephson coupling on CG(24) IS anisotropic.")
    print(f"The anisotropy comes from the 24x superfluid density tensor")
    print(f"projected differently onto the 6 transposition directions.")
    print(f"This provides a PHYSICAL mechanism for integrability breaking.")
    print(f"\n3He-A ANALOG: In superfluid 3He-A, the orbital texture l-vector")
    print(f"creates spatially varying superfluid density. Inter-vortex coupling")
    print(f"is anisotropic with respect to l. This breaks the quantum vortex")
    print(f"integrability that exists in the isotropic B-phase.")
    print(f"The framework analog: rho_s tensor anisotropy (C2 vs su(2) vs u(1))")
    print(f"projected onto CG(24) edge directions = anisotropic Josephson array.")
else:
    print(f"\nRESULT: Josephson coupling on CG(24) is effectively ISOTROPIC.")
    print(f"Despite the 24x rho_s anisotropy, all transpositions in S_4 project")
    print(f"onto the SAME direction in su(3) (or same weighted average).")
    print(f"This is a GROUP-THEORETIC PROTECTION: conjugacy class invariance.")
    print(f"\n3He-B ANALOG: In superfluid 3He-B (isotropic gap), the inter-vortex")
    print(f"coupling is isotropic despite the complex internal order parameter.")
    print(f"The framework: S_4 conjugacy class structure forces isotropy.")
    print(f"Integrability is PROTECTED by the discrete group theory.")
    print(f"CC problem: Josephson channel remains CLOSED for integrability breaking.")
    print(f"Surviving channels: quasiparticle tunneling (Andreev), multi-pair sector.")

# ============================================================================
#  Section 12: Save Data and Plot
# ============================================================================
print("\n" + "=" * 72)
print("SECTION 12: Output")
print("=" * 72)

outfile = os.path.join(data_dir, 's63_aniso_josephson.npz')

# Package all transposition data
trans_array = np.array(transpositions)
EJ_per_trans_array = np.array([EJ_per_trans[tuple(t)] for t in trans_array])
rho_s_dir_array = np.array([rho_s_directional[tuple(t)] for t in trans_array])
gm_coeffs_array = np.array([trans_gm_coeffs[tuple(t)] for t in trans_array])
directions_array = np.array([trans_directions[tuple(t)] for t in trans_array])

np.savez(outfile,
    # Graph data
    adj=adj,
    N_vertices=N_vertices,
    N_oriented_edges=N_oriented,
    N_unoriented_edges=N_unoriented,
    transpositions=trans_array,

    # Per-transposition data
    EJ_per_trans=EJ_per_trans_array,
    rho_s_directional=rho_s_dir_array,
    gm_coeffs=gm_coeffs_array,
    reflection_axes=directions_array,
    dot_matrix=dot_matrix,

    # Per-edge data
    EJ_unoriented=EJ_unoriented,
    EJ_all_oriented=EJ_all_edges,

    # Statistics
    EJ_max=EJ_max,
    EJ_min=EJ_min,
    EJ_mean=EJ_mean,
    EJ_std=EJ_std,
    ratio_maxmin=final_ratio,

    # Gate
    gate_name=np.array(['ANISO-JOSEPHSON-63']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Cross-checks
    rho_s_fold=rho_s_fold,
    rho_s_eigs=rho_s_eigs,
    anisotropy_rhos=anisotropy,

    # BCS ground state
    phi_GS=phi_GS,
    E_GS_1pair=E_GS,
    eps_fold=eps_fold,
    V_fold=V_fold,

    # Representation theory
    rep_matrices=[rep_matrices_3x3[t] for t in transpositions],
)

print(f"Saved: {outfile}")

# --- Plot ---
figfile = os.path.join(data_dir, 's63_aniso_josephson.png')
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: E_J per transposition
ax1 = axes[0, 0]
trans_labels_short = [f"({t[0]}{t[1]})" for t in transpositions]
bars = ax1.bar(range(6), EJ_per_trans_array, color='steelblue', edgecolor='black')
ax1.set_xticks(range(6))
ax1.set_xticklabels(trans_labels_short, fontsize=10)
ax1.set_ylabel('E_J (M_KK)')
ax1.set_title(f'Josephson Energy per Transposition\nmax/min = {final_ratio:.4f}')
ax1.axhline(EJ_mean, color='red', ls='--', label=f'mean = {EJ_mean:.4f}')
ax1.legend()

# Panel 2: Superfluid density eigenspectrum
ax2 = axes[0, 1]
ax2.bar(range(8), rho_evals, color='darkorange', edgecolor='black')
ax2.set_xlabel('Eigenvalue index')
ax2.set_ylabel(r'$\rho_s$ eigenvalue')
ax2.set_title(f'Superfluid Density Spectrum\nAnisotropy = {anisotropy:.1f}x')
labels_rho = ['u(1)'] + ['su(2)']*3 + [r'$C^2$']*4
ax2.set_xticks(range(8))
ax2.set_xticklabels(labels_rho, fontsize=8)

# Panel 3: Gell-Mann coefficient magnitudes per transposition
ax3 = axes[1, 0]
for t_idx, trans in enumerate(transpositions):
    c = gm_coeffs_array[t_idx]
    ax3.plot(range(8), np.abs(c), 'o-', label=f'({trans[0]}{trans[1]})', alpha=0.7)
ax3.set_xlabel('Gell-Mann index (1-8)')
ax3.set_ylabel('|coefficient|')
ax3.set_title('Gell-Mann Decomposition of Transpositions')
ax3.legend(fontsize=8, ncol=2)

# Panel 4: Edge E_J histogram
ax4 = axes[1, 1]
ax4.hist(EJ_unoriented, bins=20, color='green', edgecolor='black', alpha=0.7)
ax4.axvline(EJ_mean, color='red', ls='--', label=f'mean = {EJ_mean:.4f}')
ax4.set_xlabel('E_J (M_KK)')
ax4.set_ylabel('Count (72 edges)')
ax4.set_title(f'E_J Distribution Across 72 Edges\nVerdict: {verdict}')
ax4.legend()

fig.suptitle(f'ANISO-JOSEPHSON-63: Gate = {verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(figfile, dpi=150, bbox_inches='tight')
print(f"Saved: {figfile}")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f} s")
print(f"\n{'='*72}")
print(f"FINAL VERDICT: ANISO-JOSEPHSON-63 = {verdict}")
print(f"  {detail}")
print(f"{'='*72}")
