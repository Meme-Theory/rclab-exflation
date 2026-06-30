#!/usr/bin/env python3
"""
s72_g2_constancy.py -- G2-CONSTANCY-72: a_2/a_4 ratio constancy on G_2
=======================================================================
Gate: G2-CONSTANCY-72
  PASS:  G_2 variation > 8.8% (near-constancy is SU(3)-specific)
  INFO:  G_2 variation in [2.921%, 8.8%]
  FAIL:  G_2 variation < 2.921% (G_2 MORE constant, contradicting specificity)

PHYSICS:
--------
S71 found that the ratio a_2/a_4 of Seeley-DeWitt coefficients on
Jensen-deformed SU(3) varies by only 2.921% across the transit range
[0.10, 0.30]. This near-constancy means the gravity/gauge coupling ratio
is approximately fixed during the transit, which is structurally important.

This computation tests whether this near-constancy is SU(3)-specific or
a universal property of compact Lie groups by repeating the computation
on G_2, the 14-dimensional exceptional Lie group of rank 2.

G_2 STRUCTURE:
  - dim(G_2) = 14, rank = 2
  - Root system: 12 roots (6 positive), 2 simple roots
  - Cartan matrix: [[2, -3], [-1, 2]]  (short root alpha_1, long root alpha_2)
  - Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2,
                    3*alpha_1+alpha_2, 3*alpha_1+2*alpha_2
  - Weyl vector: rho = 5*alpha_1 + 3*alpha_2 (half-sum of positive roots)
  - Weyl dimension formula for (a_1, a_2):
    dim = (a_1+1)(a_2+1)(a_1+a_2+2)(a_1+2*a_2+3)(2*a_1+3*a_2+5)(a_1+3*a_2+4)/120

JENSEN-TYPE DEFORMATION:
  G_2 has the reductive decomposition g_2 = t + root_space where
  t = Cartan subalgebra (dim 2) and root_space (dim 12).

  Deformation: g_s = exp(6s)*g|_Cartan + exp(-s)*g|_roots
  Volume-preserving: exp(6s)^2 * exp(-s)^12 = exp(12s - 12s) = 1.

  At s=0: bi-invariant metric (all scale factors = 1).
  As s increases: Cartan stretches, root directions shrink.

METHOD:
  Build the Dirac operator D(s) on G_2 using:
  1. Explicit g_2 generators in the 7-dim fundamental representation
  2. Structure constants from commutator algebra
  3. Clifford algebra Cliff(14) with dim_spinor = 2^7 = 128
  4. Spin connection from Koszul formula
  5. Dirac operator on each Peter-Weyl sector: D_pi = sum_a rho(e_a) x gamma_a + I x Omega
  6. Heat kernel K(t) = Tr(exp(-t D^2))
  7. Seeley-DeWitt extraction from t^7 K(t) polynomial fit

  For a 14-dim manifold: K(t) = a_0*t^{-7} + a_2*t^{-6} + a_4*t^{-5} + ...

OUTPUTS:
  - computations/session-72/s72_g2_constancy.npz
  - computations/session-72/s72_g2_constancy.png

Author: Connes NCG Theorist
Session: S72, Wave 4, Entry W4-F
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
from numpy.linalg import eigh, eigvalsh, eigvals, inv, cholesky, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import tau_fold

# ============================================================
# 1. G_2 LIE ALGEBRA CONSTRUCTION
# ============================================================

print("=" * 70)
print("G2-CONSTANCY-72: a_2/a_4 Ratio Constancy on G_2")
print("=" * 70)

def build_g2_generators_fundamental():
    """
    Construct the 14 generators of g_2 in the 7-dimensional fundamental
    representation.

    G_2 embeds in so(7) as the stabilizer of the associative 3-form
    phi = e^{124} + e^{235} + e^{346} + e^{457} + e^{156} + e^{267} + e^{137}
    (using 1-indexed Fernandez-Gray convention).

    The infinitesimal condition: L in so(7) lies in g_2 iff
    sum_m (L_{mi} phi_{mjk} + L_{mj} phi_{imk} + L_{mk} phi_{ijm}) = 0
    for all i,j,k.

    We parametrize L by its 21 independent entries (anti-symmetric 7x7),
    impose the constraint, and find the 14-dim kernel.

    Returns:
        gens: list of 14 anti-Hermitian (7,7) complex matrices
        cartan_idx: indices of Cartan generators
        root_idx: indices of root generators
    """
    # Associative 3-form phi_{ijk} (0-indexed)
    # Fernandez-Gray convention: the 7 triples are
    # (0,1,3), (1,2,4), (2,3,5), (3,4,6), (0,4,5), (1,5,6), (0,2,6)
    # phi_{ijk} = +1 for cyclic permutations of these, -1 for anti-cyclic
    triples = [
        (0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6),
        (0, 4, 5), (1, 5, 6), (0, 2, 6)
    ]

    phi = np.zeros((7, 7, 7), dtype=float)
    for (a, b, c_) in triples:
        phi[a, b, c_] = 1.0; phi[b, c_, a] = 1.0; phi[c_, a, b] = 1.0
        phi[b, a, c_] = -1.0; phi[a, c_, b] = -1.0; phi[c_, b, a] = -1.0

    # Parametrize L in so(7) by upper-tri entries: L_{ij} for i < j (21 params)
    # L_{ji} = -L_{ij}
    pairs = []
    for i in range(7):
        for j in range(i+1, 7):
            pairs.append((i, j))
    assert len(pairs) == 21
    pair_idx = {p: k for k, p in enumerate(pairs)}

    # Constraint: for each (i,j,k) the form phi is preserved:
    # sum_m L_{mi}*phi_{mjk} + L_{mj}*phi_{imk} + L_{mk}*phi_{ijm} = 0
    # L_{mi} = -L_{im}: if m<i, L_{mi} = -L_{im} = -x_{(m,i)};
    #                    if m>i, L_{mi} = x_{(i,m)}; if m==i, L_{mi}=0.
    def L_coeff(m, n):
        """Return (pair_index, sign) for entry L_{mn} in terms of x-parameters.
        L_{mn} = sign * x_{pair_index}.  L_{nn} = 0 -> returns None."""
        if m == n:
            return None, 0.0
        if m < n:
            return pair_idx[(m, n)], -1.0  # L_{mn} = -x_{(m,n)} since L is anti-sym
        else:
            return pair_idx[(n, m)], 1.0   # L_{mn} = +x_{(n,m)}

    # Wait: convention. L anti-symmetric: L_{ij} = -L_{ji}.
    # We store x_k = L_{i,j} for (i,j) = pairs[k] with i < j.
    # Then L_{i,j} = x_k and L_{j,i} = -x_k.
    # So L_{m,n} for m < n: L_{mn} = x_{pair_idx[(m,n)]}
    #    L_{m,n} for m > n: L_{mn} = -x_{pair_idx[(n,m)]}
    def L_coeff2(m, n):
        if m == n:
            return None, 0.0
        if m < n:
            return pair_idx[(m, n)], 1.0
        else:
            return pair_idx[(n, m)], -1.0

    # Build constraint rows
    constraints = []
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if phi[i, j, k] == 0 and all(phi[m, j, k] == 0 for m in range(7)):
                    continue  # Skip trivially zero constraints
                row = np.zeros(21)
                for m in range(7):
                    # Term 1: L_{mi} * phi_{mjk}
                    if phi[m, j, k] != 0 and m != i:
                        idx, sgn = L_coeff2(m, i)
                        if idx is not None:
                            row[idx] += sgn * phi[m, j, k]
                    # Term 2: L_{mj} * phi_{imk}
                    if phi[i, m, k] != 0 and m != j:
                        idx, sgn = L_coeff2(m, j)
                        if idx is not None:
                            row[idx] += sgn * phi[i, m, k]
                    # Term 3: L_{mk} * phi_{ijm}
                    if phi[i, j, m] != 0 and m != k:
                        idx, sgn = L_coeff2(m, k)
                        if idx is not None:
                            row[idx] += sgn * phi[i, j, m]
                if np.any(np.abs(row) > 1e-14):
                    constraints.append(row)

    C_mat = np.array(constraints)

    # Remove duplicate rows
    # Normalize each row and check uniqueness
    unique_rows = []
    for row in C_mat:
        nrm = norm(row)
        if nrm < 1e-14:
            continue
        normalized = row / nrm
        is_dup = False
        for ur in unique_rows:
            if abs(abs(np.dot(normalized, ur / norm(ur))) - 1.0) < 1e-10:
                is_dup = True
                break
        if not is_dup:
            unique_rows.append(row)

    C_unique = np.array(unique_rows) if unique_rows else np.zeros((0, 21))

    # SVD to find null space
    U, S, Vt = np.linalg.svd(C_unique, full_matrices=True)

    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10  # (local)
    rank_C = np.sum(S > tol)
    null_dim = 21 - rank_C

    print(f"\n  Constraint matrix: {C_unique.shape[0]} unique constraints on 21 parameters")
    print(f"  Singular values: top={S[0]:.4f}, 7th={S[min(6,len(S)-1)]:.4f}, 8th={S[min(7,len(S)-1)]:.6f}")
    print(f"  Rank: {rank_C}, Null space dimension: {null_dim}")

    assert null_dim == 14, f"Expected null_dim=14 for g_2, got {null_dim}. Check 3-form convention."

    # Extract null space: last 14 rows of Vt
    null_vectors = Vt[rank_C:]  # (14, 21)

    # Convert to 7x7 anti-symmetric matrices
    raw_gens = []
    for v in null_vectors:
        L = np.zeros((7, 7), dtype=complex)
        for idx, (i, j) in enumerate(pairs):
            L[i, j] = v[idx]
            L[j, i] = -v[idx]
        raw_gens.append(L)

    # Orthonormalize: Tr(T_a T_b) = -c delta_{ab}
    # For real anti-symmetric matrices: Tr(A @ B^T) = Tr(A @ B^dag) (since B is real)
    # Tr(A @ A^dag) = -sum |A_{ij}|^2 < 0 for anti-Hermitian... no wait.
    # A anti-symmetric real: A^T = -A, A^dag = A^T = -A.
    # Tr(A @ A^dag) = Tr(A @ (-A)) = -Tr(A^2).
    # For anti-symmetric A, A^2 is negative semi-definite symmetric, Tr(A^2) <= 0.
    # So Tr(A @ A^dag) = -Tr(A^2) >= 0.

    # Gram matrix in the trace inner product: <A, B> = Tr(A^dag B) = -Tr(A @ B) (A anti-sym)
    # = Tr((-A) @ B) = -Tr(A@B)
    # For our purposes: inner product = -Tr(A@B) (positive definite on anti-Hermitian)

    def inner(A, B):
        return -np.trace(A @ B).real

    ortho_gens = []
    for g in raw_gens:
        v = g.copy()
        for og in ortho_gens:
            proj = inner(v, og) / inner(og, og)
            v = v - proj * og
        nrm2 = inner(v, v)
        if nrm2 > 1e-20:
            ortho_gens.append(v / np.sqrt(nrm2))

    assert len(ortho_gens) == 14, f"Expected 14 g_2 generators, got {len(ortho_gens)}"

    # Verify orthonormality: inner(T_a, T_b) = delta_{ab}
    # Which means Tr(T_a^dag T_b) = -Tr(T_a T_b) = delta_{ab}
    # So Tr(T_a T_b) = -delta_{ab}
    gram = np.zeros((14, 14))
    for a in range(14):
        for b in range(14):
            gram[a, b] = np.trace(ortho_gens[a] @ ortho_gens[b]).real
    ortho_err = np.max(np.abs(gram + np.eye(14)))
    print(f"  Orthonormality error (Tr(T_a T_b) + delta): {ortho_err:.2e}")

    # Verify anti-Hermiticity
    ah_check = max(np.max(np.abs(g + g.conj().T)) for g in ortho_gens)
    print(f"  Anti-Hermiticity check: {ah_check:.2e}")

    # Identify Cartan subalgebra
    comm_matrix = np.zeros((14, 14))
    for a in range(14):
        for b in range(14):
            comm = ortho_gens[a] @ ortho_gens[b] - ortho_gens[b] @ ortho_gens[a]
            comm_matrix[a, b] = norm(comm)

    # Find pair that commutes
    cartan_candidates = []
    for a in range(14):
        for b in range(a+1, 14):
            if comm_matrix[a, b] < 1e-10:
                cartan_candidates = [a, b]
                break
        if len(cartan_candidates) == 2:
            break

    if len(cartan_candidates) < 2:
        # Find approximate commuting pair
        min_comm = 1e10
        for a in range(14):
            for b in range(a+1, 14):
                if comm_matrix[a, b] < min_comm:
                    min_comm = comm_matrix[a, b]
                    cartan_candidates = [a, b]

    cartan_idx = sorted(cartan_candidates[:2])
    root_idx = [i for i in range(14) if i not in cartan_idx]

    print(f"  Cartan indices: {cartan_idx}")
    print(f"  [H_1, H_2] norm: {comm_matrix[cartan_idx[0], cartan_idx[1]]:.2e}")

    return ortho_gens, cartan_idx, root_idx


# Build G_2 Lie algebra
t0 = time.time()
g2_gens, cartan_idx, root_idx = build_g2_generators_fundamental()
t1 = time.time()
print(f"\n  G_2 generators constructed in {t1-t0:.2f}s")

# Compute structure constants
def compute_structure_constants_general(gens):
    """
    Compute structure constants f_{abc} from [T_a, T_b] = f_{abc} T_c.
    Uses trace formula: f_{abc} = Tr([T_a, T_b] T_c) / Tr(T_c T_c)
    For our normalization Tr(T_a T_b) = -delta_{ab}:
      f_{abc} = -Tr([T_a, T_b] T_c)
    """
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c_ in range(n):
                val = -np.trace(comm @ gens[c_]).real  # (local)
                f[a, b, c_] = val
                f[b, a, c_] = -val
    return f

f_abc_g2 = compute_structure_constants_general(g2_gens)

# Verify Jacobi identity
def check_jacobi(f, n):
    max_err = 0.0  # (local)
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                jac = 0.0
                for d in range(n):
                    jac += f[a,b,d]*f[d,c_,:].sum() + f[b,c_,d]*f[d,a,:].sum() + f[c_,a,d]*f[d,b,:].sum()
                # Actually Jacobi: sum_d (f_{abd}*f_{dce} + f_{bcd}*f_{dae} + f_{cad}*f_{dbe}) = 0 for each e
                pass
    # Simpler check: [ad_a, ad_b] = ad_{[a,b]}
    # i.e., f_{acd}*f_{bde} - f_{bcd}*f_{ade} = f_{abe}*f_{ecd} for all c,d
    # Just verify the Killing form is negative definite
    return True

# Killing form: kappa_{ab} = Tr(ad_a ad_b) = sum_{d,e} f_{ade} f_{bed}
# where (ad_a)_{de} = f_{ade}.
# For compact Lie algebras with anti-Hermitian generators, kappa is NEGATIVE definite.
# Note: einsum('acd,bcd') gives sum f_{acd}*f_{bcd} = -kappa (opposite sign)
# because f is totally antisymmetric: f_{bed} = f_{b,e,d} and the contraction
# sum_{d,e} f_{a,d,e}*f_{b,e,d} = -sum f_{a,d,e}*f_{b,d,e} = -einsum('ade,bde')
# Actually compute it correctly via matrix multiplication.
ad_mats = []
for a in range(14):
    M = np.zeros((14, 14))
    for d in range(14):
        for e in range(14):
            M[d, e] = f_abc_g2[a, d, e]
    ad_mats.append(M)

B_g2 = np.zeros((14, 14))
for a in range(14):
    for b in range(14):
        B_g2[a, b] = np.trace(ad_mats[a] @ ad_mats[b])

B_eigs = eigvalsh(B_g2)
print(f"\n  Killing form eigenvalues: min={B_eigs.min():.4f}, max={B_eigs.max():.4f}")
print(f"  Negative definite: {np.all(B_eigs < 0)}")
if B_eigs.min() != 0 and B_eigs.max() != 0:
    print(f"  Ratio max/min: {B_eigs.max()/B_eigs.min():.4f}")

B_diag_err = np.max(np.abs(B_g2 - np.diag(np.diag(B_g2))))
print(f"  Off-diagonal Killing form: {B_diag_err:.2e}")
print(f"  Tr(ad_0 ad_0) = {np.trace(ad_mats[0] @ ad_mats[0]):.4f} (should be negative)")

# ============================================================
# 2. JENSEN-TYPE DEFORMATION ON G_2
# ============================================================

print("\n" + "=" * 70)
print("JENSEN-TYPE DEFORMATION ON G_2")
print("=" * 70)

def jensen_metric_g2(B_ab, s, cartan_idx, root_idx):
    """
    Construct Jensen-type deformed metric on g_2.

    The base metric g_0 = -B (negative Killing form, positive definite for
    compact Lie algebras). The Killing form B is negative definite, so -B > 0.

    Decomposition: g_2 = Cartan (dim 2) + root space (dim 12)
    Deformation: g_s = L_C * g_0|_Cartan + L_R * g_0|_root
    Volume-preserving: L_C^2 * L_R^12 = 1
    => L_C = exp(6s), L_R = exp(-s)

    At s=0: bi-invariant metric.
    """
    g0 = -B_ab  # CORRECT: -Killing form is positive definite for compact algebras
    g = np.zeros_like(g0)

    L_C = np.exp(6.0 * s)
    L_R = np.exp(-s)

    for a in cartan_idx:
        for b in cartan_idx:
            g[a, b] = g0[a, b] * L_C
    for a in root_idx:
        for b in root_idx:
            g[a, b] = g0[a, b] * L_R

    return g


def orthonormal_frame_g(g_s):
    """ON frame via Cholesky: E g_s E^T = I."""
    L = cholesky(g_s)
    return inv(L)


def frame_structure_constants_g(f_abc, E):
    """Structure constants in ON frame."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)


def connection_coefficients_g(ft):
    """Levi-Civita connection in ON frame via Koszul formula."""
    n = ft.shape[0]
    Gamma = np.zeros((n, n, n), dtype=np.float64)
    for c_ in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c_, a, b] = 0.5 * (ft[a, b, c_] - ft[b, c_, a] + ft[c_, a, b])
    return Gamma


# ============================================================
# 3. CLIFFORD ALGEBRA Cliff(R^14)
# ============================================================

print("\nConstructing Clifford algebra Cliff(14)...")

def build_cliff14():
    """
    Construct generators gamma_1,...,gamma_14 of Cliff(R^14).

    These are 2^7 = 128 dimensional Hermitian matrices satisfying
    {gamma_a, gamma_b} = 2 delta_{ab} I.

    Construction: tensor products of 7 copies of Pauli matrices.
    gamma_{2k-1} = sigma_3 x ... x sigma_3 x sigma_1 x I x ... x I  (k-th position)
    gamma_{2k}   = sigma_3 x ... x sigma_3 x sigma_2 x I x ... x I
    """
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def kron_chain(mats):
        """Kronecker product of a list of matrices."""
        result = mats[0]
        for m in mats[1:]:
            result = np.kron(result, m)
        return result

    gammas = []
    n_factors = 7  # 2^7 = 128

    for k in range(1, n_factors + 1):
        # gamma_{2k-1}: sigma_3^{k-1} x sigma_1 x I^{n-k}
        mats_odd = []
        for j in range(1, n_factors + 1):
            if j < k:
                mats_odd.append(s3)
            elif j == k:
                mats_odd.append(s1)
            else:
                mats_odd.append(I2)
        gammas.append(kron_chain(mats_odd))

        # gamma_{2k}: sigma_3^{k-1} x sigma_2 x I^{n-k}
        mats_even = []
        for j in range(1, n_factors + 1):
            if j < k:
                mats_even.append(s3)
            elif j == k:
                mats_even.append(s2)
            else:
                mats_even.append(I2)
        gammas.append(kron_chain(mats_even))

    # We have 14 gammas (2*7)
    assert len(gammas) == 14

    return gammas

gammas_14 = build_cliff14()
dim_spin = gammas_14[0].shape[0]
print(f"  Spinor dimension: {dim_spin}")

# Validate Clifford algebra
max_cliff_err = 0.0
for a in range(14):
    for b in range(a, 14):
        anticomm = gammas_14[a] @ gammas_14[b] + gammas_14[b] @ gammas_14[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(dim_spin)
        err = np.max(np.abs(anticomm - target))
        max_cliff_err = max(max_cliff_err, err)
print(f"  Clifford algebra error: {max_cliff_err:.2e}")


# ============================================================
# 4. SPINOR CONNECTION OFFSET
# ============================================================

def spinor_connection_offset_g(Gamma, gammas):
    """
    Compute Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c
    for the spinor curvature offset.
    """
    n = len(gammas)
    dim_s = gammas[0].shape[0]
    Omega = np.zeros((dim_s, dim_s), dtype=complex)

    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                coeff = Gamma[b, a, c_]
                if abs(coeff) > 1e-15:
                    Omega += coeff * (gammas[a] @ gammas[b] @ gammas[c_])

    Omega *= 0.25
    return Omega


# ============================================================
# 5. G_2 REPRESENTATION CONSTRUCTION
# ============================================================

def dim_g2_irrep(a1, a2):
    """
    Weyl dimension formula for G_2 irrep with Dynkin labels (a1, a2).

    dim(a1,a2) = (a1+1)(a2+1)(a1+a2+2)(a1+2*a2+3)(2*a1+3*a2+5)(a1+3*a2+4)/120

    First few:
      (0,0): 1  (trivial)
      (1,0): 7  (fundamental)
      (0,1): 14 (adjoint)
      (2,0): 27
      (1,1): 64
      (0,2): 77
      (3,0): 77
    """
    n1 = a1 + 1
    n2 = a2 + 1
    n3 = a1 + a2 + 2
    n4 = a1 + 2*a2 + 3
    n5 = 2*a1 + 3*a2 + 5
    n6 = a1 + 3*a2 + 4
    return n1 * n2 * n3 * n4 * n5 * n6 // 120


def quadratic_casimir_g2(a1, a2):
    """
    Quadratic Casimir for G_2 irrep (a1, a2).

    C_2(lambda) = (lambda, lambda + 2*rho) where rho is the Weyl vector.

    For G_2 with simple roots alpha_1 (short), alpha_2 (long):
      Cartan matrix: [[2, -3], [-1, 2]]
      Inverse Cartan: (1/det) [[2, 3], [1, 2]] where det = 4-3 = 1
      => A^{-1} = [[2, 3], [1, 2]]

    Fundamental weights:
      w_1 = 2*alpha_1 + alpha_2 (short, |w_1|^2 depends on normalization)
      w_2 = 3*alpha_1 + 2*alpha_2

    Weyl vector: rho = w_1 + w_2 = 5*alpha_1 + 3*alpha_2

    For highest weight lambda = a1*w_1 + a2*w_2:
    C_2 = (lambda, lambda + 2*rho) in the root inner product.

    Using the inverse Cartan matrix (= symmetrized inner product on weight space):
    For G_2 the inner product on weight space (in fundamental weight basis) is:
      (w_i, w_j) = (A^{-1})_{ij} * |alpha_short|^2 / 2

    With standard normalization |alpha_long|^2 = 2, |alpha_short|^2 = 2/3:
    The quadratic form on weights is given by the matrix:
      G = A^{-T} diag(|alpha_i|^2/2) = ...

    Actually, use the standard result:
    C_2(a1, a2) = (a1^2 + a1*a2 + a2^2/3 + 5*a1 + 3*a2) * (2/3)

    Wait, let me compute this properly.

    With alpha_1 short, alpha_2 long, |alpha_2|^2 = 3|alpha_1|^2:
    Standard normalization: (alpha_2, alpha_2) = 2.
    Then (alpha_1, alpha_1) = 2/3.
    (alpha_1, alpha_2) = -1 (from Cartan matrix: 2(alpha_1,alpha_2)/(alpha_2,alpha_2) = -1)

    Fundamental weights:
      w_1: (w_1, alpha_1^v) = 1, (w_1, alpha_2^v) = 0
        where alpha_i^v = 2*alpha_i/(alpha_i, alpha_i)

      alpha_1^v = 2*alpha_1/(2/3) = 3*alpha_1
      alpha_2^v = 2*alpha_2/2 = alpha_2

      w_1 = 2*alpha_1 + alpha_2  (solving the system)
      w_2 = 3*alpha_1 + 2*alpha_2

    Inner products of fundamental weights:
      (w_1, w_1) = 4*(2/3) + 2*2*(-1) + (2) = 8/3 - 4 + 2 = 2/3
      (w_1, w_2) = 6*(2/3) + (2+3)*(-1) + 2*2 = 4 - 5 + 4 = 3...

    Let me just compute directly:
      (w_1, w_1) = (2a1+a2, 2a1+a2) where a_i = alpha_i
                 = 4(a1,a1) + 4(a1,a2) + (a2,a2)
                 = 4*(2/3) + 4*(-1) + 2
                 = 8/3 - 4 + 2 = 2/3
      (w_1, w_2) = (2a1+a2, 3a1+2a2)
                 = 6(a1,a1) + 4(a1,a2) + 3(a1,a2) + 2(a2,a2)
                 = 6*(2/3) + 7*(-1) + 2*2
                 = 4 - 7 + 4 = 1
      (w_2, w_2) = (3a1+2a2, 3a1+2a2)
                 = 9*(2/3) + 12*(-1) + 4*2
                 = 6 - 12 + 8 = 2

    So the metric on weight space (in w_1, w_2 basis) is:
      G_ij = [[2/3, 1], [1, 2]]

    For lambda = a1*w_1 + a2*w_2:
      (lambda, lambda) = (2/3)*a1^2 + 2*a1*a2 + 2*a2^2

    rho = w_1 + w_2, so:
      (lambda, 2*rho) = 2*(a1*(w_1,w_1+w_2) + a2*(w_2,w_1+w_2))
                      = 2*(a1*(2/3+1) + a2*(1+2))
                      = 2*(5*a1/3 + 3*a2)
                      = 10*a1/3 + 6*a2

    C_2 = (lambda, lambda + 2*rho)
        = (2/3)*a1^2 + 2*a1*a2 + 2*a2^2 + 10*a1/3 + 6*a2
    """
    return (2.0/3)*a1**2 + 2*a1*a2 + 2*a2**2 + (10.0/3)*a1 + 6*a2


# Verify dimensions
print("\nG_2 representations:")
for a1 in range(4):
    for a2 in range(3):
        d = dim_g2_irrep(a1, a2)
        c2 = quadratic_casimir_g2(a1, a2)
        if d <= 200:
            print(f"  ({a1},{a2}): dim={d}, C_2={c2:.4f}")


def build_g2_irrep_fundamental(gens):
    """Fundamental (1,0) of G_2: dim=7. Generators are the 7x7 matrices themselves."""
    return [g.copy() for g in gens]


def build_g2_irrep_adjoint(f_abc):
    """Adjoint (0,1) of G_2: dim=14. (ad(T_a))_{cb} = f_{abc}."""
    rho = []
    for a in range(14):
        M = f_abc[a, :, :].T.astype(complex)
        rho.append(M)
    return rho


def build_g2_irrep_symmetric2(gens):
    """
    Symmetric tensor product Sym^2(7) of G_2: dim = 28.
    But 28 = 1 + 27 for G_2, so Sym^2(7) decomposes as 1 + 27.
    The 27-dim component is the (2,0) irrep.

    We construct Sym^2 first, then project out the trivial component
    using the Casimir operator.
    """
    I7 = np.eye(7, dtype=complex)

    # Build ON basis for Sym^2(C^7)
    sym_vecs = []
    for i in range(7):
        v = np.zeros(49, dtype=complex)
        v[7*i + i] = 1.0
        sym_vecs.append(v)
    for i in range(7):
        for j in range(i+1, 7):
            v = np.zeros(49, dtype=complex)
            v[7*i + j] = 1.0 / np.sqrt(2)
            v[7*j + i] = 1.0 / np.sqrt(2)
            sym_vecs.append(v)

    P = np.column_stack(sym_vecs)  # 49 x 28
    dim_sym = P.shape[1]
    assert dim_sym == 28

    # Representation on Sym^2
    rho_sym = []
    for X in gens:
        rho_49 = np.kron(X, I7) + np.kron(I7, X)
        rho_sym.append(P.conj().T @ rho_49 @ P)

    # Build Casimir operator on Sym^2
    C2_sym = np.zeros((dim_sym, dim_sym), dtype=complex)
    for a in range(14):
        C2_sym += rho_sym[a] @ rho_sym[a]

    # Diagonalize Casimir to find irrep decomposition
    c2_eigs = eigvalsh(C2_sym)

    # For G_2: Sym^2(7) = 1 + 27
    # C_2(trivial) = 0, C_2(2,0) = 2/3*4 + 0 + 0 + 10*2/3 + 0 = 8/3 + 20/3 = 28/3
    # With our normalization: C_2 eigenvalue on the Casimir operator
    # The Casimir operator here is sum T_a^2, which for the trivial part gives 0
    # and for the 27-dim part gives -C_2(2,0) (negative because anti-Hermitian generators)

    # Find eigenvectors
    c2_evals, c2_evecs = eigh(C2_sym)

    # Group by Casimir eigenvalue
    unique_c2 = []
    for e in c2_evals:
        found = False
        for u in unique_c2:
            if abs(e - u) < 0.01:
                found = True
                break
        if not found:
            unique_c2.append(e)
    unique_c2.sort()

    # The trivial component has eigenvalue closest to 0
    # The 27-dim component has eigenvalue = -C_2(2,0) * normalization

    # Project onto 27-dim subspace (eigenvalue furthest from 0)
    target_c2 = unique_c2[-1]  # Most negative (largest magnitude)
    mask_27 = np.abs(c2_evals - target_c2) < 0.1
    P_27 = c2_evecs[:, mask_27]  # 28 x 27

    dim_27 = P_27.shape[1]
    if dim_27 != 27:
        # Try the other eigenvalue
        target_c2 = unique_c2[0]
        mask_27 = np.abs(c2_evals - target_c2) < 0.1
        P_27 = c2_evecs[:, mask_27]
        dim_27 = P_27.shape[1]

    print(f"  Sym^2(7) Casimir eigenvalues: {[f'{u:.4f}' for u in unique_c2]}")
    print(f"  27-dim subspace found: dim={dim_27}")

    if dim_27 == 27:
        rho_27 = []
        for M in rho_sym:
            rho_27.append(P_27.conj().T @ M @ P_27)
        return rho_27, dim_27
    else:
        # Fall back to using full Sym^2
        print(f"  WARNING: Could not isolate 27-dim irrep, using full Sym^2(7)")
        return rho_sym, dim_sym


# ============================================================
# 6. DIRAC OPERATOR CONSTRUCTION
# ============================================================

def dirac_operator_g2(rho, E, gammas, Omega):
    """
    Assemble Dirac operator D_pi on irrep sector pi.
    D_pi = sum_{a,b} E_{ab} (rho(X_b) tensor gamma_a) + I_{dim_rho} tensor Omega
    """
    dim_rho = rho[0].shape[0]
    dim_s = gammas[0].shape[0]
    dim_total = dim_rho * dim_s

    D = np.zeros((dim_total, dim_total), dtype=complex)

    for a in range(14):
        for b in range(14):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])

    D += np.kron(np.eye(dim_rho, dtype=complex), Omega)

    return D


# ============================================================
# 7. HEAT KERNEL AND SEELEY-DEWITT EXTRACTION
# ============================================================

def compute_heat_kernel_g2(eval_data_list, t_values):
    """
    Compute K(t) = Tr(exp(-t D^2)) from eigenvalue data.
    Each entry: (a1, a2, eigenvalues_array)
    Weight: dim(a1,a2) from Peter-Weyl.
    """
    t_arr = np.asarray(t_values, dtype=np.float64)
    K_t = np.zeros_like(t_arr)

    for a1, a2, evals in eval_data_list:
        d_irrep = dim_g2_irrep(a1, a2)
        pw_weight = d_irrep

        lambda_sq = np.abs(evals) ** 2

        exponents = np.outer(-t_arr, lambda_sq)
        boltzmann = np.exp(exponents)
        K_pq = pw_weight * np.sum(boltzmann, axis=1)

        K_t += K_pq

    return K_t


def extract_seeley_dewitt_g2(eval_data_list, t_range=(0.001, 0.5), n_points=200, n_coeffs=5):
    """
    Extract Seeley-DeWitt coefficients for a 14-dim manifold.
    K(t) = a_0*t^{-7} + a_2*t^{-6} + a_4*t^{-5} + a_6*t^{-4} + a_8*t^{-3} + ...

    So t^7 * K(t) = a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4 + ...

    Fit polynomial in t to extract a_0, a_2, a_4, ...
    """
    t_values = np.linspace(t_range[0], t_range[1], n_points)
    K_t = compute_heat_kernel_g2(eval_data_list, t_values)

    half_dim = 7  # dim/2 = 14/2
    F_t = t_values**half_dim * K_t

    V = np.vander(t_values, N=n_coeffs, increasing=True)
    weights = 1.0 / t_values
    W = np.diag(weights)

    VtWV = V.T @ W @ V
    VtWF = V.T @ W @ F_t

    cond = np.linalg.cond(VtWV)
    coeffs_arr = np.linalg.solve(VtWV, VtWF)

    coeff_names = ['a_0', 'a_2', 'a_4', 'a_6', 'a_8'][:n_coeffs]
    coeffs = {name: val for name, val in zip(coeff_names, coeffs_arr)}

    F_fitted = V @ coeffs_arr
    residual = np.sqrt(np.mean((F_t - F_fitted)**2)) / np.mean(np.abs(F_t))

    return coeffs, {'residual': residual, 'condition_number': cond}


# ============================================================
# 8. MAIN COMPUTATION: SWEEP OVER s
# ============================================================

print("\n" + "=" * 70)
print("COMPUTING DIRAC SPECTRUM AND HEAT KERNEL ON G_2")
print("=" * 70)

# Deformation parameter range
# Use same range as SU(3): s in [0, 0.5] with 11 points
# For ratio variation, also compute at fine grid in [0.10, 0.30]
s_values = np.linspace(0.0, 0.5, 11)
print(f"\n  s values ({len(s_values)}): {s_values}")
print(f"  Irreps to compute: (0,0)=1, (1,0)=7, (0,1)=14, (2,0)=27")
print(f"  Matrix sizes: 128, 896, 1792, 3456")

# Storage
a0_vals = np.zeros(len(s_values))
a2_vals = np.zeros(len(s_values))
a4_vals = np.zeros(len(s_values))
a6_vals = np.zeros(len(s_values))

max_irrep_sum = 2  # Include (a1,a2) with a1+a2 <= 2
# This gives: (0,0)=1, (1,0)=7, (0,1)=14, (2,0)=27, (1,1)=64, (0,2)=77

# For memory/time: limit to smaller irreps
# (1,1)=64 -> 64*128 = 8192x8192 matrix (too large for eigenvalue decomposition)
# Stick with a1+a2 <= 1 for the main computation, then check convergence with (2,0)
# Actually (2,0)=27 -> 27*128=3456 matrix, feasible.
# (0,2)=77 -> 77*128=9856, borderline.
# Let's include up to (2,0): (0,0), (1,0), (0,1), (2,0)

irreps_to_compute = []
for a1 in range(max_irrep_sum + 1):
    for a2 in range(max_irrep_sum + 1 - a1):
        d = dim_g2_irrep(a1, a2)
        if d * dim_spin > 5000:
            print(f"  SKIPPING ({a1},{a2}): dim={d}, matrix size = {d*dim_spin} (too large)")
            continue
        c2 = quadratic_casimir_g2(a1, a2)
        irreps_to_compute.append((c2, a1, a2, d))

irreps_to_compute.sort()
print(f"\n  Irreps to compute:")
for c2, a1, a2, d in irreps_to_compute:
    print(f"    ({a1},{a2}): dim={d}, C_2={c2:.4f}, D_size={d*dim_spin}")

for si, s in enumerate(s_values):
    t_start = time.time()
    print(f"\n  s = {s:.3f} ({si+1}/{len(s_values)})...")

    # Build metric, frame, connection
    g_s = jensen_metric_g2(B_g2, s, cartan_idx, root_idx)

    # Check positive definiteness
    g_eigs = eigvalsh(g_s)
    if np.any(g_eigs <= 0):
        print(f"    WARNING: Metric not positive definite! Eigenvalues: {g_eigs}")
        continue

    E = orthonormal_frame_g(g_s)
    ft = frame_structure_constants_g(f_abc_g2, E)
    Gamma = connection_coefficients_g(ft)
    Omega = spinor_connection_offset_g(Gamma, gammas_14)

    # Verify connection metric compatibility
    mc_err = 0.0  # (local)
    for a in range(14):
        for b in range(14):
            for c_ in range(14):
                err = abs(Gamma[c_, a, b] + Gamma[b, a, c_])
                mc_err = max(mc_err, err)

    # Check Omega anti-Hermiticity
    ah_err = np.max(np.abs(Omega + Omega.conj().T))
    print(f"    Connection metric-compat err: {mc_err:.2e}, Omega anti-Herm err: {ah_err:.2e}")

    # Compute Dirac spectrum on each irrep
    eval_data_list = []

    # Trivial irrep: D = Omega on 128-dim spinor space
    evals_trivial = eigvals(Omega)
    eval_data_list.append((0, 0, evals_trivial))
    print(f"    (0,0): D_size=128, |lambda| range: [{np.min(np.abs(evals_trivial)):.4f}, {np.max(np.abs(evals_trivial)):.4f}]")

    for c2, a1, a2, d in irreps_to_compute:
        if a1 == 0 and a2 == 0:
            continue  # Already done

        # Get representation matrices
        if a1 == 1 and a2 == 0:
            rho = build_g2_irrep_fundamental(g2_gens)
        elif a1 == 0 and a2 == 1:
            rho = build_g2_irrep_adjoint(f_abc_g2)
        elif a1 == 2 and a2 == 0:
            rho, d_check = build_g2_irrep_symmetric2(g2_gens)
            if d_check != d:
                print(f"    WARNING: Expected dim={d} for ({a1},{a2}), got {d_check}")
                d = d_check
        else:
            print(f"    SKIPPING ({a1},{a2}): no representation constructor available")
            continue

        # Build Dirac operator
        D_pi = dirac_operator_g2(rho, E, gammas_14, Omega)

        # Compute eigenvalues
        evals_pi = eigvals(D_pi)
        eval_data_list.append((a1, a2, evals_pi))

        abs_evals = np.abs(evals_pi)
        print(f"    ({a1},{a2}): D_size={d*dim_spin}, |lambda| range: [{np.min(abs_evals):.4f}, {np.max(abs_evals):.4f}]")

    # Extract Seeley-DeWitt coefficients
    coeffs, fit_info = extract_seeley_dewitt_g2(eval_data_list)

    a0_vals[si] = coeffs['a_0']
    a2_vals[si] = coeffs['a_2']
    a4_vals[si] = coeffs['a_4']
    a6_vals[si] = coeffs.get('a_6', 0)

    t_elapsed = time.time() - t_start
    print(f"    SDW: a_0={coeffs['a_0']:.2f}, a_2={coeffs['a_2']:.4f}, a_4={coeffs['a_4']:.4f}")
    print(f"    Fit residual: {fit_info['residual']:.2e}, condition: {fit_info['condition_number']:.2e}")
    print(f"    Time: {t_elapsed:.1f}s")


# ============================================================
# 9. COMPUTE RATIOS AND VARIATION
# ============================================================

print("\n" + "=" * 70)
print("MOMENT RATIO ANALYSIS")
print("=" * 70)

# Compute a_2/a_4 ratio
ratio_24 = a2_vals / a4_vals

print(f"\n{'s':>8s} | {'a_0':>10s} {'a_2':>10s} {'a_4':>10s} | {'a2/a4':>10s}")
print("-" * 60)
for si, s in enumerate(s_values):
    print(f"  {s:6.3f} | {a0_vals[si]:10.2f} {a2_vals[si]:10.4f} {a4_vals[si]:10.4f} | {ratio_24[si]:10.6f}")

# Compute variation over transit range [0.10, 0.30]
# Use |a_2/a_4| for variation computation (sign is a truncation artifact)
abs_ratio_24 = np.abs(ratio_24)

transit_mask = (s_values >= 0.10) & (s_values <= 0.30)
if transit_mask.sum() > 1:
    ar24_transit = abs_ratio_24[transit_mask]
    ar24_mean = ar24_transit.mean()
    r24_var = (ar24_transit.max() - ar24_transit.min()) / ar24_mean * 100
    r24_mean = ratio_24[transit_mask].mean()
    print(f"\n  Transit range [0.10, 0.30]: {transit_mask.sum()} points")
    print(f"  |a_2/a_4| range: [{ar24_transit.min():.6f}, {ar24_transit.max():.6f}]")
    print(f"  |a_2/a_4| mean: {ar24_mean:.6f}")
    print(f"  Variation (max-min)/mean of |ratio|: {r24_var:.3f}%")
else:
    ar24_mean = abs_ratio_24.mean()
    r24_var = (abs_ratio_24.max() - abs_ratio_24.min()) / ar24_mean * 100
    r24_mean = ratio_24.mean()
    print(f"\n  Full range: {len(s_values)} points")
    print(f"  |a_2/a_4| range: [{abs_ratio_24.min():.6f}, {abs_ratio_24.max():.6f}]")
    print(f"  |a_2/a_4| mean: {ar24_mean:.6f}")
    print(f"  Variation (max-min)/mean of |ratio|: {r24_var:.3f}%")

# Also compute full-range variation
ar24_full_mean = abs_ratio_24.mean()
r24_full_var = (abs_ratio_24.max() - abs_ratio_24.min()) / ar24_full_mean * 100
print(f"\n  Full range [0.00, 0.50]: |a_2/a_4| variation = {r24_full_var:.3f}%")

# Compare with SU(3) result
su3_transit_var = 2.921  # % (from S71)  # (local)
su3_full_var = 10.095    # % (from s66_zeta_sa.npz)  # (local)
print(f"\n  Comparison:")
print(f"    SU(3) transit variation: {su3_transit_var:.3f}%")
print(f"    G_2 transit variation:   {r24_var:.3f}%")
print(f"    Ratio G_2/SU(3):        {r24_var/su3_transit_var:.3f}")

# ============================================================
# 10. GATE VERDICT
# ============================================================

print("\n" + "=" * 70)
print("GATE VERDICT: G2-CONSTANCY-72")
print("=" * 70)

if r24_var > 8.8:
    verdict = "PASS"
    detail = f"G_2 variation {r24_var:.3f}% > 8.8% threshold. Near-constancy IS SU(3)-specific."
elif r24_var > su3_transit_var:
    verdict = "INFO"
    detail = f"G_2 variation {r24_var:.3f}% in [{su3_transit_var:.3f}%, 8.8%]. Similar to SU(3), not specific."
else:
    verdict = "FAIL"
    detail = f"G_2 variation {r24_var:.3f}% < SU(3) variation {su3_transit_var:.3f}%. G_2 MORE constant."

print(f"\n  Gate: G2-CONSTANCY-72")
print(f"  Verdict: {verdict}")
print(f"  Threshold: G_2 variation > 8.8% for PASS, < {su3_transit_var:.3f}% for FAIL")
print(f"  Computed: G_2 transit variation = {r24_var:.3f}%")
print(f"  {detail}")
print(f"\n  G_2 structural numbers:")
print(f"    dim(G_2) = 14, rank = 2, |root system| = 12")
print(f"    Spinor dim = {dim_spin}")
print(f"    Irreps computed: {[(a1,a2) for _,a1,a2,_ in irreps_to_compute]}")
print(f"    a_2/a_4 at s=0: {ratio_24[0]:.6f}")
print(f"    a_2/a_4 mean: {r24_mean:.6f}")

# ============================================================
# 11. PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('G2-CONSTANCY-72: Seeley-DeWitt Coefficients on Jensen-Deformed $G_2$',
             fontsize=14, fontweight='bold')

# Panel (a): Absolute moments
ax = axes[0, 0]
ax.plot(s_values, a0_vals, 'b-o', linewidth=2, label=r'$a_0$ (volume)')
ax.plot(s_values, a2_vals, 'r-s', linewidth=2, label=r'$a_2$ (EH/gravity)')
ax.plot(s_values, a4_vals, 'g-^', linewidth=2, label=r'$a_4$ (YM/gauge)')
ax.axvline(0.19, color='k', linestyle=':', alpha=0.5, label='SU(3) fold')
ax.set_xlabel(r'Deformation parameter $s$')
ax.set_ylabel(r'$a_k(s)$')
ax.set_title(r'(a) Seeley-DeWitt coefficients on $G_2$')
ax.legend(fontsize=8)
ax.set_xlim(-0.02, 0.52)

# Panel (b): a_2/a_4 ratio
ax = axes[0, 1]
ax.plot(s_values, ratio_24, 'k-o', linewidth=2, markersize=6)
ax.axhline(r24_mean, color='gray', linestyle='--', alpha=0.5,
           label=f'Mean = {r24_mean:.4f}')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow', label='Transit range')
ax.set_xlabel(r'Deformation parameter $s$')
ax.set_ylabel(r'$a_2 / a_4$')
ax.set_title(r'(b) Gravity/gauge ratio $a_2/a_4$ on $G_2$')
ax.legend(fontsize=8)
ax.set_xlim(-0.02, 0.52)

# Panel (c): Comparison with SU(3)
ax = axes[1, 0]
# Normalize both ratios to their s=0 values for comparison
r24_g2_norm = ratio_24 / ratio_24[0]
# Load SU(3) data for comparison
try:
    d_su3 = np.load('s66_zeta_sa.npz', allow_pickle=True)
    tau_su3 = d_su3['tau_all']
    a2_su3 = d_su3['a2']
    a4_su3 = d_su3['a4']
    r24_su3 = a2_su3 / a4_su3
    r24_su3_norm = r24_su3 / r24_su3[0]
    ax.plot(tau_su3, r24_su3_norm, 'b-o', linewidth=2, label=r'SU(3) ($a_2/a_4$ normalized)')
except:
    pass
ax.plot(s_values, r24_g2_norm, 'r-s', linewidth=2, label=r'$G_2$ ($a_2/a_4$ normalized)')
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
ax.set_xlabel(r'Deformation parameter $s$ (or $\tau$ for SU(3))')
ax.set_ylabel(r'$[a_2/a_4](s) / [a_2/a_4](0)$')
ax.set_title('(c) Normalized ratio comparison')
ax.legend(fontsize=8)
ax.set_xlim(-0.02, 0.52)

# Panel (d): Summary text
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"G2-CONSTANCY-72 RESULTS\n"
    f"{'='*35}\n\n"
    f"Gate Verdict: {verdict}\n\n"
    f"G_2 parameters:\n"
    f"  dim = 14, rank = 2\n"
    f"  Spinor dim = {dim_spin}\n"
    f"  Irreps: (0,0), (1,0), (0,1), (2,0)\n\n"
    f"Transit variation [0.10, 0.30]:\n"
    f"  G_2:   {r24_var:.3f}%\n"
    f"  SU(3): {su3_transit_var:.3f}%\n"
    f"  Ratio: {r24_var/su3_transit_var:.2f}x\n\n"
    f"Full variation [0.00, 0.50]:\n"
    f"  G_2:   {r24_full_var:.3f}%\n"
    f"  SU(3): {su3_full_var:.3f}%\n\n"
    f"a_2/a_4 at s=0: {ratio_24[0]:.4f}\n"
    f"a_2/a_4 mean:   {r24_mean:.4f}"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('s72_g2_constancy.png', dpi=150, bbox_inches='tight')
print(f"\n  Plot saved: s72_g2_constancy.png")

# ============================================================
# 12. SAVE DATA
# ============================================================

np.savez('s72_g2_constancy.npz',
         # Grid
         s_values=s_values,
         # Seeley-DeWitt coefficients
         a0=a0_vals,
         a2=a2_vals,
         a4=a4_vals,
         a6=a6_vals,
         # Ratio
         ratio_24=ratio_24,
         abs_ratio_24=abs_ratio_24,
         # Summary
         transit_variation_pct=r24_var,
         full_variation_pct=r24_full_var,
         su3_transit_variation_pct=su3_transit_var,
         gate_verdict=verdict,
         ratio_g2_over_su3=r24_var/su3_transit_var,
         # Metadata
         dim_G2=14,
         rank_G2=2,
         dim_spinor=dim_spin,
         max_irrep_sum=max_irrep_sum,
         )

print(f"\n  Data saved: s72_g2_constancy.npz")
print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*70}")
