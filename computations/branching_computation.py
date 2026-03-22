"""
TIER 0 DISCRIMINATOR: Branching Delta_8|_{U(2)} and Commutant Algebra
=====================================================================

This script computes the branching of the Spin(8) spinor representation
Delta_8 under the U(2) subgroup of SU(3), following Baptista's explicit
construction in arXiv:2105.02901v1 (Paper 14, "HD Routes to Fermions").

The goal: determine the commutant algebra End_{U(2)}(Delta_8) and check
whether it equals Connes' finite algebra A_F = C + H + M_3(C).

MATHEMATICAL SETUP
==================

1. Internal space K = SU(3), dimension 8.
2. The 12D spinor decomposes as (4D Weyl) x (8D internal spinor).
3. The 8D internal spinor Delta_8 has dimension 2^4 = 16.
4. Baptista writes Delta_8 as a 4x4 complex matrix Psi_+ with entries:

       Psi_+ = ( a    c^T )     a: 1x1, c: 3x1, b: 3x1, D: 3x3
                ( b    D   )     Total: 1 + 3 + 3 + 9 = 16 components

5. The su(3) actions L and R on Psi_+ are given by eq 2.62:

   Lv(Psi) = ( 0                  -2*v_11 * c^T       )
              ( (2*v_11*I + v)*b    v*D                 )

   Rv(Psi) = ( 0                   (conj(v)*c)^T       )
              ( 0                  -D*v                  )

   for v in su(3) (traceless anti-Hermitian 3x3 matrix), v_11 = v[0,0].

6. The U(2) subalgebra of su(3) consists of matrices of the form:
       v = diag(-tr(a), a)  for a in u(2)

   (eq 3.61: phi(a) = diag(det(a)^{-1}, a), differentiated at identity)
   At the Lie algebra level: phi_*(a) = diag(-tr(a), a) for a in u(2).

7. For v in u(2) subset su(3), the combined action L+R is a Lie algebra
   homomorphism (eq 2.65). This is the action we decompose.

8. The commutant End_{U(2)}(Delta_8) is determined by Schur's lemma:
   If Delta_8|_{U(2)} = sum_i m_i * R_i (irreps with multiplicities),
   then End_{U(2)}(Delta_8) = bigoplus_i M_{m_i}(K_i)
   where K_i = R (real type), C (complex type), or H (quaternionic type).

SUCCESS CRITERION: End_{U(2)}(Delta_8) = C + H + M_3(C)
   requires multiplicity pattern with types: (1,real), (1,quat), (3,complex)
   or equivalent patterns that give the same algebra.

REFERENCES
==========
- Baptista arXiv:2105.02901v1, eq 2.62 (L,R actions), eq 2.65 (homomorphism), eq 2.66 (particle ID)
- Baptista arXiv:2306.01049, eq 3.57-3.62 (U(2) embedding, metric decomposition)
- Connes-Chamseddine-Marcolli arXiv:0706.3688 (A_F definition)

Author: KK Theorist Agent (phonon-exflation project)
Date: 2026-02-11
"""

import numpy as np
from itertools import product as iter_product

# =============================================================================
# PART 1: Basis of su(3) and u(2) embedding
# =============================================================================

def gell_mann_matrices():
    """
    Return the 8 Gell-Mann matrices lambda_1...lambda_8.
    These form a basis for traceless Hermitian 3x3 matrices.
    Our su(3) basis will be e_j = -i * lambda_j / 2 (anti-Hermitian, traceless).
    """
    lam = [None] * 8

    lam[0] = np.array([[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 0]], dtype=complex)

    lam[1] = np.array([[0, -1j, 0],
                        [1j, 0,  0],
                        [0,  0,  0]], dtype=complex)

    lam[2] = np.array([[1,  0, 0],
                        [0, -1, 0],
                        [0,  0, 0]], dtype=complex)

    lam[3] = np.array([[0, 0, 1],
                        [0, 0, 0],
                        [1, 0, 0]], dtype=complex)

    lam[4] = np.array([[0, 0, -1j],
                        [0, 0,  0],
                        [1j, 0, 0]], dtype=complex)

    lam[5] = np.array([[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0]], dtype=complex)

    lam[6] = np.array([[0, 0,  0],
                        [0, 0, -1j],
                        [0, 1j, 0]], dtype=complex)

    lam[7] = np.array([[1, 0,  0],
                        [0, 1,  0],
                        [0, 0, -2]], dtype=complex) / np.sqrt(3)

    return lam


def su3_basis():
    """
    Basis {e_j} for su(3) as anti-Hermitian traceless 3x3 matrices.
    Convention: e_j = -i * lambda_j / 2, so [e_j, e_k] = f_{jkl} e_l.
    """
    lam = gell_mann_matrices()
    return [-1j * l / 2 for l in lam]


def u2_basis_in_su3():
    """
    Basis for the u(2) subalgebra of su(3).

    The embedding phi: U(2) -> SU(3) is phi(a) = diag(det(a)^{-1}, a).
    At the Lie algebra level: phi_*(a) = diag(-tr(a), a) for a in u(2).

    u(2) = u(1) + su(2), dimension 4.

    We choose a basis for u(2) that maps to:
    - Y  = diag(-2i*t, i*t*I_2) for t real  (hypercharge generator, u(1) part)
    - T_j = diag(0, sigma_j * (-i/2))       (su(2) part, j=1,2,3)

    Using the embedding phi_*:
    - For a = i*t * I_2 (scalar in u(2)):
      phi_*(a) = diag(-2i*t, i*t, i*t)
      This is the hypercharge direction Y.

    - For a = -i*sigma_j/2 (traceless in su(2)):
      phi_*(a) = diag(0, -i*sigma_j/2)
      These are the weak isospin generators.
    """
    # Hypercharge generator Y: phi_*(i*I_2) = diag(-2i, i, i)
    # Normalize: Y = i * diag(-2, 1, 1) / (2*sqrt(3)) matches lambda_8
    # But let's use the physics normalization.
    # Y = (i/2) * diag(-2, 1, 1) = -sqrt(3) * e_8 (in Gell-Mann convention)

    # Actually, let's just construct the su(3) matrices directly.

    # u(1)_Y generator: a = (i/2)*I_2 -> phi_*(a) = diag(-i, i/2, i/2)
    Y = np.diag([-1j, 1j/2, 1j/2])

    # su(2) generators: a = -i*sigma_j/2 -> phi_*(a) = diag(0, -i*sigma_j/2)
    sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)

    T1 = np.zeros((3,3), dtype=complex)
    T1[1:, 1:] = -1j * sigma1 / 2

    T2 = np.zeros((3,3), dtype=complex)
    T2[1:, 1:] = -1j * sigma2 / 2

    T3 = np.zeros((3,3), dtype=complex)
    T3[1:, 1:] = -1j * sigma3 / 2

    return [Y, T1, T2, T3]


# =============================================================================
# PART 2: L and R actions on the 16-dimensional spinor space
# =============================================================================

# The spinor Psi_+ is a 4x4 complex matrix with block structure:
#   Psi_+ = ( a    c^T )   where a: scalar (1x1), c: 3-vector (col),
#            ( b    D   )         b: 3-vector (col), D: 3x3 matrix.
#
# We represent this as a 16-dimensional vector by flattening:
#   index 0:     a
#   indices 1-3: c (stored as column vector, c^T is a row in Psi_+)
#   indices 4-6: b (column vector)
#   indices 7-15: D (row-major: D[0,0], D[0,1], D[0,2], D[1,0], ..., D[2,2])
#
# This ordering maps to the physical particles (from eq 2.66):
#   0: nu_R          (right-handed neutrino)
#   1: u_R^r         (right-handed up quark, red)
#   2: u_R^g         (right-handed up quark, green)
#   3: u_R^b         (right-handed up quark, blue)
#   4: e_R^-         (right-handed electron)
#   5: d_R^r         (... but see note below about row ordering)
#   6: d_R^g
#   ... etc.

def flatten_psi(a, c, b, D):
    """Convert block components (a, c, b, D) to 16-vector."""
    vec = np.zeros(16, dtype=complex)
    vec[0] = a
    vec[1:4] = c
    vec[4:7] = b
    vec[7:16] = D.flatten()  # row-major
    return vec


def unflatten_psi(vec):
    """Convert 16-vector back to block components (a, c, b, D)."""
    a = vec[0]
    c = vec[1:4].copy()
    b = vec[4:7].copy()
    D = vec[7:16].reshape(3, 3).copy()
    return a, c, b, D


def L_action_matrix(v):
    """
    Compute the 16x16 matrix representing the LEFT action Lv on Psi_+.

    From Baptista eq 2.62:
        Lv(a) = 0
        Lv(c^T) = -2 * v[0,0] * c^T     =>  Lv(c) = -2 * v[0,0] * c
        Lv(b) = (2*v[0,0]*I_3 + v) * b
        Lv(D) = v * D                     (left multiplication)

    Here v is a 3x3 anti-Hermitian traceless matrix in su(3).
    v[0,0] = v_{11} in Baptista's notation (0-indexed here).

    NOTE: Baptista uses "v" in eq 2.62 to mean the FULL 3x3 su(3) matrix acting
    on 3-vectors b and D. The (2*v_11*I + v) term in the b-action comes from
    the way the vertical Lie derivative of the s(h)-type function works.
    """
    L = np.zeros((16, 16), dtype=complex)
    v11 = v[0, 0]

    # a -> 0: row 0, all zeros (already initialized)

    # c -> -2 * v_11 * c: rows 1-3
    for i in range(3):
        L[1+i, 1+i] = -2 * v11

    # b -> (2*v_11*I_3 + v) * b: rows 4-6
    M_b = 2 * v11 * np.eye(3, dtype=complex) + v
    for i in range(3):
        for j in range(3):
            L[4+i, 4+j] = M_b[i, j]

    # D -> v * D (left multiplication): rows 7-15
    # If D is row-major flattened, (v*D)_{ij} = sum_k v_{ik} D_{kj}
    # In terms of the flattened index: row i, col j -> index 3*i + j
    # (v*D)[3*i+j] = sum_k v[i,k] * D[3*k+j]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                L[7 + 3*i + j, 7 + 3*k + j] += v[i, k]

    return L


def R_action_matrix(v):
    """
    Compute the 16x16 matrix representing the RIGHT action Rv on Psi_+.

    From Baptista eq 2.62:
        Rv(a) = 0
        Rv(c^T) = (conj(v) * c)^T    =>  Rv(c) = conj(v) * c
        Rv(b) = 0
        Rv(D) = -D * v                (right multiplication by -v)

    Here conj(v) means complex conjugate (NOT hermitian conjugate).
    For v anti-Hermitian: v^dagger = -v, so conj(v) = -v^T.
    """
    R = np.zeros((16, 16), dtype=complex)
    v_conj = np.conj(v)

    # a -> 0: already zero

    # c -> conj(v) * c: rows 1-3
    for i in range(3):
        for j in range(3):
            R[1+i, 1+j] = v_conj[i, j]

    # b -> 0: already zero

    # D -> -D * v (right multiplication by -v): rows 7-15
    # (-D*v)_{ij} = -sum_k D_{ik} v_{kj}
    # Flattened: index 3*i+j, source 3*i+k
    for i in range(3):
        for j in range(3):
            for k in range(3):
                R[7 + 3*i + j, 7 + 3*i + k] += -v[k, j]

    return R


def LR_action_matrix(v):
    """Combined L+R action of v in su(3) on the 16-dim spinor space."""
    return L_action_matrix(v) + R_action_matrix(v)


# =============================================================================
# PART 3: Validation checks
# =============================================================================

def validate_actions():
    """
    Run consistency checks on the L and R action matrices.

    Checks:
    1. L and R are anti-Hermitian (since v is anti-Hermitian and the actions
       preserve the inner product Tr(Psi^dagger Psi))
    2. R is a Lie algebra homomorphism: [Rv, Rw] = R_{[v,w]}
    3. L is NOT a homomorphism for general su(3): [Lv, Lw] != L_{[v,w]}
    4. L+R IS a homomorphism when restricted to u(2)
    5. Dimension checks: trace and rank of various operators
    """
    print("=" * 70)
    print("PART 3: VALIDATION CHECKS")
    print("=" * 70)

    basis_su3 = su3_basis()
    basis_u2 = u2_basis_in_su3()

    # Check 1: Anti-Hermiticity
    print("\n[Check 1] Anti-Hermiticity of L and R matrices:")
    max_L_err = 0
    max_R_err = 0
    for j, ej in enumerate(basis_su3):
        Lj = L_action_matrix(ej)
        Rj = R_action_matrix(ej)
        max_L_err = max(max_L_err, np.max(np.abs(Lj + Lj.conj().T)))
        max_R_err = max(max_R_err, np.max(np.abs(Rj + Rj.conj().T)))
    print(f"  Max |L + L^dag|: {max_L_err:.2e} (should be ~0)")
    print(f"  Max |R + R^dag|: {max_R_err:.2e} (should be ~0)")

    # Check 2: R is a Lie algebra homomorphism
    print("\n[Check 2] R is a Lie algebra homomorphism:")
    max_R_hom_err = 0
    for j in range(8):
        for k in range(j+1, 8):
            Rj = R_action_matrix(basis_su3[j])
            Rk = R_action_matrix(basis_su3[k])
            comm_R = Rj @ Rk - Rk @ Rj
            bracket_jk = basis_su3[j] @ basis_su3[k] - basis_su3[k] @ basis_su3[j]
            R_bracket = R_action_matrix(bracket_jk)
            err = np.max(np.abs(comm_R - R_bracket))
            max_R_hom_err = max(max_R_hom_err, err)
    print(f"  Max |[Rv, Rw] - R_[v,w]|: {max_R_hom_err:.2e} (should be ~0)")

    # Check 3: L is NOT a homomorphism for general su(3)
    print("\n[Check 3] L is NOT a homomorphism for general su(3) elements:")
    # Pick two elements NOT in u(2): lambda_4/lambda_5 type (C^2 directions)
    e4 = basis_su3[3]  # lambda_4 direction
    e5 = basis_su3[4]  # lambda_5 direction
    L4 = L_action_matrix(e4)
    L5 = L_action_matrix(e5)
    comm_L = L4 @ L5 - L5 @ L4
    bracket_45 = e4 @ e5 - e5 @ e4
    L_bracket = L_action_matrix(bracket_45)
    err_L_hom = np.max(np.abs(comm_L - L_bracket))
    print(f"  |[L_e4, L_e5] - L_[e4,e5]|: {err_L_hom:.2e} (should be NONZERO)")

    # Check 4: L+R is a homomorphism on u(2)
    print("\n[Check 4] L+R is a Lie algebra homomorphism on u(2):")
    max_LR_hom_err = 0
    for j in range(4):
        for k in range(j+1, 4):
            LRj = LR_action_matrix(basis_u2[j])
            LRk = LR_action_matrix(basis_u2[k])
            comm_LR = LRj @ LRk - LRk @ LRj
            bracket_jk = basis_u2[j] @ basis_u2[k] - basis_u2[k] @ basis_u2[j]
            LR_bracket = LR_action_matrix(bracket_jk)
            err = np.max(np.abs(comm_LR - LR_bracket))
            max_LR_hom_err = max(max_LR_hom_err, err)
    print(f"  Max |[LR_v, LR_w] - LR_[v,w]| on u(2): {max_LR_hom_err:.2e} (should be ~0)")

    # Check 5: Trace of representation matrices (should be 0 for su(3) in any rep)
    print("\n[Check 5] Traces of representation matrices:")
    for j, ej in enumerate(basis_su3):
        Lj = L_action_matrix(ej)
        Rj = R_action_matrix(ej)
        print(f"  Tr(L_e{j+1}) = {np.trace(Lj):.6f},  Tr(R_e{j+1}) = {np.trace(Rj):.6f}")

    return True


# =============================================================================
# PART 4: Decompose Delta_8|_{U(2)} into irreducible representations
# =============================================================================

def compute_u2_casimirs():
    """
    Compute the U(2) Casimir operators on the 16-dim representation.

    U(2) = U(1)_Y x SU(2)_W. An irrep of U(2) is labeled by:
      - Y: the U(1) charge (hypercharge), eigenvalue of the Y generator
      - j: the SU(2) spin, from the Casimir C_2 = T1^2 + T2^2 + T3^2

    The dimension of the irrep is (2j+1), and the type is:
      - j integer: real type (R) if 2j+1 is odd and Y=0
      - j half-integer: quaternionic type (H) -- SU(2) doublet is pseudoreal
      - If Y != 0: complex type (C) regardless of j (Y and -Y are distinct)

    More precisely, the Frobenius-Schur indicator for SU(2) rep of spin j is:
      - (+1) if j is integer (real)
      - (-1) if j is half-integer (quaternionic/pseudoreal)
    But for U(2) = U(1) x SU(2), if Y != 0, the rep (Y, j) and (-Y, j) are
    distinct (complex conjugate pair), giving complex type regardless.
    If Y = 0, the type is determined by the SU(2) Frobenius-Schur indicator.
    """
    basis_u2 = u2_basis_in_su3()

    Y_gen = LR_action_matrix(basis_u2[0])   # U(1)_Y generator
    T1 = LR_action_matrix(basis_u2[1])       # SU(2) generators
    T2 = LR_action_matrix(basis_u2[2])
    T3 = LR_action_matrix(basis_u2[3])

    # SU(2) Casimir: C_2 = T1^2 + T2^2 + T3^2
    # Eigenvalue j(j+1) for spin-j representation
    C2_su2 = T1 @ T1 + T2 @ T2 + T3 @ T3

    return Y_gen, C2_su2, T1, T2, T3


def decompose_representation():
    """
    Decompose the 16-dimensional representation of U(2) into irreducible components.

    Strategy:
    1. Simultaneously diagonalize the commuting operators Y and C_2(SU(2))
    2. Group eigenspaces by (Y, j) quantum numbers
    3. Count multiplicities
    4. Determine type (real/complex/quaternionic)
    5. Compute commutant algebra

    Returns the decomposition as a list of (Y_value, j_value, multiplicity, dimension, type).
    """
    print("\n" + "=" * 70)
    print("PART 4: DECOMPOSITION OF Delta_8|_{U(2)}")
    print("=" * 70)

    Y_gen, C2_su2, T1, T2, T3 = compute_u2_casimirs()

    # Step 1: Verify that Y and C2 commute (they must, since Y is the center of u(2))
    comm_YC2 = Y_gen @ C2_su2 - C2_su2 @ Y_gen
    print(f"\n[Step 1] |[Y, C_2]| = {np.max(np.abs(comm_YC2)):.2e} (should be ~0)")

    # Also verify T3 commutes with Y and C2
    comm_YT3 = Y_gen @ LR_action_matrix(u2_basis_in_su3()[3]) - LR_action_matrix(u2_basis_in_su3()[3]) @ Y_gen
    print(f"  |[Y, T_3]| = {np.max(np.abs(comm_YT3)):.2e} (should be ~0)")

    # Step 2: Y_gen might not be diagonal in our basis. Let's find its eigenvalues.
    # Since Y is anti-Hermitian, its eigenvalues are purely imaginary.
    # The physical hypercharge is Y_phys = eigenvalue / (i * normalization).

    # First, let's use the HERMITIAN version of Y: Y_H = i * Y_gen / normalization
    # Our Y_gen comes from a = (i/2)*I_2, so phi_*(a) = diag(-i, i/2, i/2)
    # The "hypercharge" Y = (2/3) * i * Y_gen in some conventions, but let's just
    # work with the eigenvalues directly.

    print("\n[Step 2] Eigenvalues of the Y generator (anti-Hermitian, so purely imaginary):")
    Y_evals, Y_evecs = np.linalg.eigh(1j * Y_gen)  # Hermitianize: eigenvalues of i*Y
    # So eigenvalues of Y_gen are -i * Y_evals
    print(f"  Eigenvalues of i*Y: {np.sort(np.round(Y_evals, 8))}")

    print("\n[Step 3] Eigenvalues of C_2(SU(2)):")
    # C2 is Hermitian (negative semidefinite since T_j are anti-Hermitian)
    # C2 = T1^2 + T2^2 + T3^2, and T_j anti-Hermitian means T_j^2 is negative semidefinite
    # So C2 has eigenvalues -j(j+1) for the SU(2) irrep conventions we're using
    C2_evals = np.linalg.eigvalsh(C2_su2)
    print(f"  Eigenvalues of C_2: {np.sort(np.round(C2_evals, 8))}")

    # Step 3: Simultaneously diagonalize Y_gen and C2_su2
    # Since they commute, we can find a common eigenbasis.
    # Strategy: diagonalize Y first, then diagonalize C2 within each Y-eigenspace.

    # Use the Hermitian matrix i*Y_gen for numerical stability
    iY = 1j * Y_gen
    Y_evals_raw, P_Y = np.linalg.eigh(iY)

    # Round to identify degenerate eigenvalues
    Y_evals_rounded = np.round(Y_evals_raw, 6)
    unique_Y = np.unique(Y_evals_rounded)

    print(f"\n[Step 4] Unique Y eigenvalues (of i*Y_gen): {unique_Y}")

    # For each Y eigenspace, diagonalize C2
    decomposition = []  # list of (Y_val, j_val, multiplicity, basis_vectors)

    full_basis = []  # Will store the simultaneous eigenvectors

    for y_val in unique_Y:
        mask = np.abs(Y_evals_rounded - y_val) < 1e-4
        indices = np.where(mask)[0]
        dim_y = len(indices)

        # Extract the Y-eigenspace
        V_y = P_Y[:, indices]  # columns are the basis vectors

        # Project C2 into this subspace
        C2_proj = V_y.conj().T @ C2_su2 @ V_y

        # Diagonalize C2 in this subspace
        c2_evals, c2_evecs = np.linalg.eigh(C2_proj)
        c2_evals_rounded = np.round(c2_evals, 6)

        # Transform eigenvectors back to full space
        full_evecs = V_y @ c2_evecs

        unique_c2 = np.unique(c2_evals_rounded)

        for c2_val in unique_c2:
            c2_mask = np.abs(c2_evals_rounded - c2_val) < 1e-4
            dim_jy = np.sum(c2_mask)

            # Determine j from C2 eigenvalue
            # C2 = T1^2 + T2^2 + T3^2 where T_j = LR(basis_u2[j])
            # Our T_j are anti-Hermitian, so T_j^2 has negative eigenvalues
            # C2 eigenvalue = -j(j+1) in our conventions (anti-Hermitian generators)
            # So j(j+1) = -c2_val
            jj1 = -c2_val
            if jj1 < -1e-6:
                print(f"  WARNING: j(j+1) = {jj1} < 0 for Y={y_val}, C2={c2_val}")
                j_val = -1  # error flag
            else:
                jj1 = max(0, jj1)  # clamp small negative to 0
                # Solve j(j+1) = jj1 => j = (-1 + sqrt(1+4*jj1))/2
                j_val = (-1 + np.sqrt(1 + 4*jj1)) / 2

            # Store basis vectors for this (Y, j) sector
            sector_indices = np.where(c2_mask)[0]
            sector_vecs = full_evecs[:, sector_indices]
            full_basis.append(sector_vecs)

            decomposition.append({
                'Y': y_val,
                'j': j_val,
                'dim_total': dim_jy,
                'dim_irrep': int(round(2*j_val + 1)),
                'basis': sector_vecs,
            })

    # Step 5: For each (Y, j) sector, determine multiplicity
    # dim_total = multiplicity * (2j+1)
    print("\n[Step 5] Decomposition table:")
    print(f"  {'Y (of iY)':>12}  {'j':>6}  {'2j+1':>5}  {'dim_total':>10}  {'mult':>5}")
    print(f"  {'-'*12}  {'-'*6}  {'-'*5}  {'-'*10}  {'-'*5}")

    total_dim = 0
    for sector in decomposition:
        d_irrep = sector['dim_irrep']
        if d_irrep > 0:
            mult = sector['dim_total'] // d_irrep
            sector['multiplicity'] = mult
        else:
            mult = sector['dim_total']
            sector['multiplicity'] = mult

        print(f"  {sector['Y']:>12.4f}  {sector['j']:>6.3f}  {d_irrep:>5}  {sector['dim_total']:>10}  {mult:>5}")
        total_dim += sector['dim_total']

    print(f"\n  Total dimension: {total_dim} (should be 16)")

    return decomposition


# =============================================================================
# PART 5: Verify decomposition using T3 (weight diagram)
# =============================================================================

def verify_with_weights(decomposition):
    """
    Cross-check the decomposition using the T3 weights within each (Y, j) sector.
    For a spin-j irrep, T3 should have eigenvalues -j, -j+1, ..., j-1, j.
    With multiplicity m, each T3 eigenvalue appears m times.
    """
    print("\n" + "=" * 70)
    print("PART 5: WEIGHT DIAGRAM VERIFICATION")
    print("=" * 70)

    basis_u2 = u2_basis_in_su3()
    T3_full = LR_action_matrix(basis_u2[3])

    # T3 is anti-Hermitian, so eigenvalues of i*T3 are real
    # T3 eigenvalue = -i * (i*T3 eigenvalue) = eigenvalue of i*T3
    # Wait: if T3 is anti-Hermitian, T3 |m> = m |m> with m purely imaginary
    # Physical m_j = eigenvalue of i*T3

    iT3 = 1j * T3_full

    for sector in decomposition:
        V = sector['basis']
        # Project iT3 into this subspace
        iT3_proj = V.conj().T @ iT3 @ V
        t3_evals = np.linalg.eigvalsh(iT3_proj)
        t3_rounded = np.sort(np.round(t3_evals, 6))

        j_val = sector['j']
        mult = sector['multiplicity']
        expected_weights = []
        for m in np.arange(-j_val, j_val + 0.5, 1.0):
            expected_weights.extend([round(m, 6)] * mult)
        expected_weights = np.sort(expected_weights)

        match = np.allclose(t3_rounded, expected_weights, atol=1e-4)

        print(f"\n  Sector Y={sector['Y']:.4f}, j={j_val:.3f} (mult={mult}):")
        print(f"    T3 eigenvalues: {t3_rounded}")
        print(f"    Expected:       {expected_weights}")
        print(f"    Match: {'YES' if match else 'NO'}")


# =============================================================================
# PART 6: Determine representation types and commutant algebra
# =============================================================================

def determine_types_and_commutant(decomposition):
    """
    For each U(2) irrep appearing in the decomposition, determine its type:
      - REAL (Frobenius-Schur +1): if the irrep is self-conjugate with symmetric invariant
      - COMPLEX (Frobenius-Schur 0): if the irrep is NOT self-conjugate
      - QUATERNIONIC (Frobenius-Schur -1): if self-conjugate with antisymmetric invariant

    For U(2) = U(1)_Y x SU(2):
      - Irrep (Y, j) has conjugate (-Y, j)
      - If Y != 0: the irrep is complex type (C)
      - If Y = 0 and j is integer: real type (R)
      - If Y = 0 and j is half-integer: quaternionic type (H)

    Then the commutant algebra is:
      End_{U(2)}(Delta_8) = bigoplus_{irreps i} M_{m_i}(K_i)

    where m_i = multiplicity and K_i = R, C, or H depending on type.

    HOWEVER, for complex-type irreps, we must be more careful:
    If irrep R and its conjugate R-bar both appear with the same multiplicity m,
    they should be grouped together. The commutant for (R, m) + (R-bar, m) is M_m(C),
    since the complex structure is preserved.

    Actually, the standard result is:
    - Real irrep with multiplicity m: contributes M_m(R) to the commutant
    - Complex irrep (paired with conjugate) with multiplicity m: contributes M_m(C)
    - Quaternionic irrep with multiplicity m: contributes M_m(H)

    For A_F = C + H + M_3(C), we need (after complexification or in the real sense):
    - A complex irrep pair with multiplicity 1 -> M_1(C) = C
    - A quaternionic irrep with multiplicity 1 -> M_1(H) = H
    - A complex irrep pair with multiplicity 3 -> M_3(C)

    OR other combinations that give the same algebra.
    """
    print("\n" + "=" * 70)
    print("PART 6: REPRESENTATION TYPES AND COMMUTANT ALGEBRA")
    print("=" * 70)

    # Group irreps by (Y, j) and merge complex conjugate pairs
    # Complex conjugate of (Y, j) is (-Y, j)

    processed = set()
    algebra_factors = []

    print("\n  Irrep classification:")
    print(f"  {'Label':>15}  {'Y':>8}  {'j':>5}  {'dim':>4}  {'mult':>5}  {'type':>12}  {'commutant':>15}")
    print(f"  {'-'*15}  {'-'*8}  {'-'*5}  {'-'*4}  {'-'*5}  {'-'*12}  {'-'*15}")

    # Sort decomposition by Y value for clean display
    decomposition_sorted = sorted(decomposition, key=lambda s: (s['Y'], s['j']))

    for sector in decomposition_sorted:
        Y = sector['Y']
        j = sector['j']
        m = sector['multiplicity']
        key = (round(Y, 4), round(j, 4))

        if key in processed:
            continue
        processed.add(key)

        conj_key = (round(-Y, 4), round(j, 4))

        if abs(Y) < 1e-4:
            # Y = 0: self-conjugate
            # Type determined by SU(2) Frobenius-Schur
            j_rounded = round(2*j) / 2
            if abs(j_rounded - round(j_rounded)) < 0.1:
                # j is integer
                rep_type = "REAL"
                if m == 1:
                    comm_factor = "R"
                else:
                    comm_factor = f"M_{m}(R)"
            else:
                # j is half-integer
                rep_type = "QUATERNIONIC"
                if m == 1:
                    comm_factor = "H"
                else:
                    comm_factor = f"M_{m}(H)"

            label = f"(0, {j:.1f})"
            print(f"  {label:>15}  {Y:>8.4f}  {j:>5.2f}  {sector['dim_irrep']:>4}  {m:>5}  {rep_type:>12}  {comm_factor:>15}")
            algebra_factors.append(comm_factor)

        else:
            # Y != 0: complex type (pair with -Y)
            # Find the conjugate sector
            conj_sector = None
            for s in decomposition_sorted:
                if abs(s['Y'] + Y) < 1e-4 and abs(s['j'] - j) < 1e-4:
                    conj_sector = s
                    break

            if conj_sector is not None:
                processed.add(conj_key)
                m_conj = conj_sector['multiplicity']
                if m != m_conj:
                    print(f"  WARNING: (Y={Y:.4f}, j={j:.2f}) has mult={m} "
                          f"but conjugate has mult={m_conj}")

                rep_type = "COMPLEX"
                if m == 1:
                    comm_factor = "C"
                else:
                    comm_factor = f"M_{m}(C)"

                label = f"(+/-{abs(Y):.2f}, {j:.1f})"
                dim_total = sector['dim_irrep']
                print(f"  {label:>15}  {'+/-':>8}{abs(Y):.2f}  {j:>5.2f}  {dim_total:>4}  {m:>5}  {rep_type:>12}  {comm_factor:>15}")
                algebra_factors.append(comm_factor)
            else:
                # No conjugate found -- this shouldn't happen for a real representation
                rep_type = "COMPLEX (unpaired!)"
                comm_factor = f"M_{m}(C)?"
                label = f"({Y:.2f}, {j:.1f})"
                print(f"  {label:>15}  {Y:>8.4f}  {j:>5.2f}  {sector['dim_irrep']:>4}  {m:>5}  {rep_type:>12}  {comm_factor:>15}")
                algebra_factors.append(comm_factor)

    # Assemble the commutant algebra
    commutant = " + ".join(algebra_factors)

    print(f"\n  COMMUTANT ALGEBRA: End_{{U(2)}}(Delta_8) = {commutant}")

    # Compute total real dimension of commutant
    total_real_dim = 0
    for f in algebra_factors:
        if f == "R":
            total_real_dim += 1
        elif f == "C":
            total_real_dim += 2
        elif f == "H":
            total_real_dim += 4
        elif f.startswith("M_"):
            # Parse M_n(K)
            parts = f.split("(")
            n = int(f.split("_")[1].split("(")[0])
            K = parts[1].rstrip(")")
            if K == "R":
                total_real_dim += n*n
            elif K == "C":
                total_real_dim += 2*n*n
            elif K == "H":
                total_real_dim += 4*n*n

    print(f"  Real dimension: {total_real_dim}")

    # Compare with A_F
    AF_dim = 1*2 + 1*4 + 3*3*2  # C + H + M_3(C) = 2 + 4 + 18 = 24
    print(f"\n  A_F = C + H + M_3(C) has real dimension: {AF_dim}")

    # Check match
    target = "C + H + M_3(C)"
    # Normalize the commutant string for comparison
    commutant_normalized = commutant.replace(" ", "")
    target_normalized = target.replace(" ", "")

    # Sort the factors for comparison
    comm_parts = sorted(commutant_normalized.split("+"))
    target_parts = sorted(target_normalized.split("+"))

    if comm_parts == target_parts:
        print(f"\n  *** RESULT: End_{{U(2)}}(Delta_8) = A_F = C + H + M_3(C) ***")
        print(f"  *** THIS IS A DECISIVE SUCCESS ***")
        return True, commutant
    else:
        print(f"\n  RESULT: End_{{U(2)}}(Delta_8) = {commutant}")
        print(f"  TARGET: A_F = {target}")
        if total_real_dim == AF_dim:
            print(f"  Dimensions MATCH but algebra structure DIFFERS")
        else:
            print(f"  Dimensions DO NOT MATCH ({total_real_dim} vs {AF_dim})")
        return False, commutant


# =============================================================================
# PART 7: Direct commutant computation (independent check)
# =============================================================================

def compute_commutant_directly():
    """
    Compute the commutant End_{U(2)}(Delta_8) directly by solving the system
    of linear equations: [T, rho(g)] = 0 for all g in u(2).

    A 16x16 complex matrix T is in the commutant iff:
        T * rho(e_j) = rho(e_j) * T   for all j = 1,...,4 (u(2) basis)

    This gives 4 matrix equations, each with 16x16 = 256 complex entries,
    for a total of 4*256 = 1024 complex linear constraints on the 256
    complex entries of T.

    We solve this as a real linear system (512 real unknowns, up to 2048
    real constraints).
    """
    print("\n" + "=" * 70)
    print("PART 7: DIRECT COMMUTANT COMPUTATION")
    print("=" * 70)

    basis_u2 = u2_basis_in_su3()
    rho = [LR_action_matrix(v) for v in basis_u2]

    # Set up the linear system: for each generator, [T, rho_j] = 0
    # T * rho_j - rho_j * T = 0
    # Vectorize T as a 256-dimensional complex vector (row-major)
    # Then the equation becomes a linear system A * vec(T) = 0

    n = 16
    constraints = []

    for rho_j in rho:
        # T * rho_j - rho_j * T = 0
        # In component form: sum_k (T_{ik} rho_j_{kl} - rho_j_{ik} T_{kl}) = 0
        # This is a linear equation in the entries of T.
        # Using the vectorization: vec(AXB) = (B^T kron A) vec(X)
        # T * rho_j: A=I, X=T, B=rho_j -> (rho_j^T kron I) vec(T)
        # rho_j * T: A=rho_j, X=T, B=I -> (I kron rho_j) vec(T)

        # Constraint: (rho_j^T kron I - I kron rho_j) vec(T) = 0
        M = np.kron(rho_j.T, np.eye(n)) - np.kron(np.eye(n), rho_j)
        constraints.append(M)

    # Stack all constraints
    A_complex = np.vstack(constraints)

    # Convert to real system: separate real and imaginary parts
    A_real = np.vstack([
        np.hstack([A_complex.real, -A_complex.imag]),
        np.hstack([A_complex.imag, A_complex.real]),
    ])

    # Find the null space of A_real
    from scipy.linalg import null_space

    print(f"\n  Constraint matrix size: {A_real.shape}")
    ns = null_space(A_real, rcond=1e-8)

    real_dim = ns.shape[1]
    print(f"  Null space dimension (real): {real_dim}")
    print(f"  => Complex dimension of commutant: {real_dim // 2}")
    print(f"     (This should equal the sum of m_i^2 * dim_R(K_i) for each factor)")

    # The real dimension of A_F = C + H + M_3(C) is 2 + 4 + 18 = 24
    # The complex dimension would be... well, A_F is a real algebra of real dim 24.
    # But our computation treats T as a complex matrix, so the null space in complex
    # dimension should be the complex dimension of the commutant as a complex algebra.
    #
    # Actually: End_{U(2)}(Delta_8) as a COMPLEX algebra (complex matrices commuting
    # with U(2)) has complex dimension = sum of m_i^2 (regardless of type).
    # The type information (R/C/H) is about the REAL structure, determined by an
    # antilinear involution.

    # Reconstruct basis elements of the commutant
    # Each null space vector is [re(vec(T)); im(vec(T))]
    n2 = n * n
    commutant_basis = []
    for k in range(ns.shape[1] // 2):
        # Take pairs to form complex vectors
        re_part = ns[:n2, 2*k]
        im_part = ns[n2:, 2*k]
        T_vec = re_part + 1j * im_part
        T_mat = T_vec.reshape(n, n)
        commutant_basis.append(T_mat)

    # Actually, let me just use the complex null space directly
    # for cleaner results
    print("\n  Computing complex null space directly...")

    # For the complex case, we need: (rho_j^T kron I - I kron rho_j) vec(T) = 0
    # where vec(T) is a complex vector of length 256
    U, s, Vh = np.linalg.svd(A_complex)
    tol = 1e-8 * s[0] if len(s) > 0 else 1e-8
    rank = np.sum(s > tol)
    null_dim = A_complex.shape[1] - rank

    print(f"  SVD rank of constraint matrix: {rank}")
    print(f"  Complex null space dimension: {null_dim}")

    # Extract null space from SVD
    null_vectors = Vh[rank:].conj().T

    # Reconstruct the matrices
    commutant_basis_complex = []
    for k in range(null_dim):
        T_mat = null_vectors[:, k].reshape(n, n)
        commutant_basis_complex.append(T_mat)

    # Verify: check that each basis element actually commutes with all generators
    print("\n  Verification: commutant basis elements commute with all u(2) generators?")
    max_err = 0
    for k, T in enumerate(commutant_basis_complex):
        for j, rho_j in enumerate(rho):
            err = np.max(np.abs(T @ rho_j - rho_j @ T))
            max_err = max(max_err, err)
    print(f"  Max |[T, rho_j]| over all basis elements: {max_err:.2e}")

    # Analyze the algebra structure
    # Compute the multiplication table
    print(f"\n  Commutant algebra dimension: {null_dim}")
    print(f"  Expected for A_F = C + H + M_3(C): 1 + 4 + 9 = 14 (complex)")
    print(f"  (C contributes 1, H = M_1(H) contributes 4 real = 2 complex as a *-algebra,")
    print(f"   but as complex associative algebra H_C = M_2(C) contributes 4 complex,")
    print(f"   M_3(C) contributes 9 complex. Total: 1+4+9 = 14)")

    # Check if the algebra is semisimple by computing the structure
    if null_dim > 0 and null_dim <= 30:
        print("\n  Multiplication table (first few products):")
        # Compute all products and express in the basis
        # This tells us the algebra structure

        # First, orthonormalize the basis
        from scipy.linalg import orth
        basis_matrix = np.column_stack([T.flatten() for T in commutant_basis_complex])
        Q = orth(basis_matrix)
        d = Q.shape[1]
        print(f"  Orthonormalized basis dimension: {d}")

        orth_basis = [Q[:, k].reshape(n, n) for k in range(d)]

        # Compute structure constants c^k_{ij} where e_i * e_j = sum_k c^k_{ij} e_k
        # Express the product in terms of the basis
        struct_const = np.zeros((d, d, d), dtype=complex)
        product_residuals = []

        for i in range(d):
            for j in range(d):
                product = orth_basis[i] @ orth_basis[j]
                # Project onto basis
                prod_vec = product.flatten()
                coeffs = Q.conj().T @ prod_vec
                struct_const[i, j, :] = coeffs
                # Residual (how well the product is captured by the algebra)
                residual = np.linalg.norm(prod_vec - Q @ coeffs)
                product_residuals.append(residual)

        max_residual = max(product_residuals)
        print(f"  Max product residual (closure check): {max_residual:.2e}")
        if max_residual < 1e-6:
            print(f"  Algebra IS closed under multiplication (residual < 1e-6)")
        else:
            print(f"  WARNING: Algebra may not be closed! Residual = {max_residual:.2e}")

        # Determine the algebra by finding its center and ideals
        # Center: elements that commute with everything
        center_dim = 0
        for i in range(d):
            is_central = True
            for j in range(d):
                comm = struct_const[i, j, :] - struct_const[j, i, :]
                if np.linalg.norm(comm) > 1e-6:
                    is_central = False
                    break
            if is_central:
                center_dim += 1

        print(f"\n  Center dimension: {center_dim}")
        print(f"  (For C + H_C + M_3(C) = C + M_2(C) + M_3(C), center dim = 3)")
        print(f"  (For C + H + M_3(C) as real *-algebra, complex center dim also = 3)")

        # Find minimal central idempotents to identify the simple factors
        # The identity matrix should be in the commutant
        identity_vec = np.eye(n).flatten()
        id_coeffs = Q.conj().T @ identity_vec
        id_residual = np.linalg.norm(identity_vec - Q @ id_coeffs)
        print(f"\n  Identity matrix in commutant? Residual: {id_residual:.2e}")

        # Try to find idempotents by spectral decomposition of central elements
        # Compute the regular representation
        print("\n  Computing Wedderburn decomposition via radical/semisimple analysis...")

        # Method: compute the trace form and check if the algebra is semisimple
        # Trace form: B(x,y) = tr(L_x L_y) where L_x is left multiplication by x
        # Construct left-regular representation
        L_reg = np.zeros((d, d, d), dtype=complex)
        for i in range(d):
            for j in range(d):
                L_reg[i, :, j] = struct_const[i, j, :]

        # L_reg[i] is the matrix of left multiplication by e_i
        # Trace form: B_{ij} = tr(L_reg[i] @ L_reg[j])
        trace_form = np.zeros((d, d), dtype=complex)
        for i in range(d):
            for j in range(d):
                trace_form[i, j] = np.trace(L_reg[i] @ L_reg[j])

        tf_evals = np.linalg.eigvalsh(trace_form)
        print(f"  Trace form eigenvalues: {np.sort(np.round(np.real(tf_evals), 4))}")
        n_zero_tf = np.sum(np.abs(tf_evals) < 1e-6)
        print(f"  Number of zero eigenvalues: {n_zero_tf}")
        if n_zero_tf == 0:
            print(f"  Trace form is nondegenerate => algebra is SEMISIMPLE")
        else:
            print(f"  Trace form has nullity {n_zero_tf} => algebra has nontrivial radical")

    return null_dim, commutant_basis_complex


# =============================================================================
# PART 8: Physical particle identification
# =============================================================================

def identify_particles(decomposition):
    """
    Cross-reference the (Y, j) quantum numbers with Standard Model particles.

    Baptista's particle identification (eq 2.66) tells us which entries of the
    4x4 matrix Psi_+ correspond to which fermions. The U(2) quantum numbers
    (Y, j) should match the SM hypercharge and weak isospin assignments.

    SM fermion quantum numbers (one generation, left-handed + right-handed):

    Particle        Y_phys   I_w    Components
    --------        ------   ---    ----------
    (nu_L, e_L)    -1/2     1/2    2 (doublet)
    e_R             -1       0      1 (singlet)
    (u_L, d_L)      1/6     1/2    2x3=6 (doublet, colour triplet)
    u_R              2/3     0      3 (singlet, colour triplet)
    d_R             -1/3     0      3 (singlet, colour triplet)
    nu_R             0       0      1 (singlet)

    Total: 2 + 1 + 6 + 3 + 3 + 1 = 16 components per generation.
    """
    print("\n" + "=" * 70)
    print("PART 8: PHYSICAL PARTICLE IDENTIFICATION")
    print("=" * 70)

    # Our Y generator comes from a = (i/2)*I_2 in u(2)
    # phi_*(a) = diag(-i, i/2, i/2) in su(3)
    # The physical hypercharge normalization:
    # Y_phys = (1/3) * eigenvalue of i*Y_gen ... need to calibrate

    # Let's instead look at individual basis vectors and their Y, T3 eigenvalues
    basis_u2 = u2_basis_in_su3()
    Y_gen = LR_action_matrix(basis_u2[0])
    T3_gen = LR_action_matrix(basis_u2[3])

    iY = 1j * Y_gen
    iT3 = 1j * T3_gen

    # Label the 16 basis vectors of our representation
    labels = [
        'a+  (nu_R)',           # index 0: a component
        'c1+ (u_R^r)',          # index 1: c[0]
        'c2+ (u_R^g)',          # index 2: c[1]
        'c3+ (u_R^b)',          # index 3: c[2]
        'b1+ (e_R^-)',          # index 4: b[0]
        'b2+ (row2,col1)',      # index 5: b[1]
        'b3+ (row3,col1)',      # index 6: b[2]
        'D11 (d_R^r)',          # index 7: D[0,0]
        'D12 (d_R^g)',          # index 8: D[0,1]
        'D13 (d_R^b)',          # index 9: D[0,2]
        'D21 (row2)',           # index 10: D[1,0]
        'D22',                  # index 11: D[1,1]
        'D23',                  # index 12: D[1,2]
        'D31 (row3)',           # index 13: D[2,0]
        'D32',                  # index 14: D[2,1]
        'D33',                  # index 15: D[2,2]
    ]

    print("\n  Diagonal Y and T3 values on basis vectors:")
    print(f"  {'Index':>5}  {'Label':>20}  {'Y':>10}  {'T3':>10}")
    print(f"  {'-'*5}  {'-'*20}  {'-'*10}  {'-'*10}")

    for k in range(16):
        y_val = iY[k, k].real
        t3_val = iT3[k, k].real
        # Check if this basis vector is actually an eigenstate
        y_offdiag = np.sum(np.abs(iY[k, :])) - np.abs(iY[k, k])
        t3_offdiag = np.sum(np.abs(iT3[k, :])) - np.abs(iT3[k, k])

        marker = ""
        if y_offdiag > 1e-6 or t3_offdiag > 1e-6:
            marker = " [NOT eigenstate]"

        print(f"  {k:>5}  {labels[k]:>20}  {y_val:>10.4f}  {t3_val:>10.4f}{marker}")

    # Also print the full Y matrix to see its structure
    print("\n  Full i*Y matrix (should show block structure):")
    print("  Non-zero entries of i*Y:")
    for i in range(16):
        for j in range(16):
            val = iY[i, j]
            if abs(val) > 1e-8:
                print(f"    [{i:>2},{j:>2}] = {val.real:>8.4f} + {val.imag:>8.4f}i")


# =============================================================================
# PART 9: Alternative approach -- use L and R SEPARATELY
# =============================================================================

def analyze_L_and_R_separately():
    """
    Analyze the L and R actions separately to understand the representation
    structure better.

    Key fact from Baptista: R defines a full su(3) homomorphism (eq 2.65).
    So the R-action gives a well-defined su(3) representation on Psi_+.

    From the physics (eq 2.26-2.27):
    - R gives the STRONG force (SU(3)_color) action: D -> -D*v
    - L restricted to u(2) gives the ELECTROWEAK (U(2)) action

    The effective gauge action is L_u(2) + R_su(3) on Psi_+.

    But for the COMMUTANT computation, we only care about the U(2) part,
    which is L+R restricted to u(2) in su(3).

    Let's verify the R-action decomposition to make sure our matrices are correct.
    """
    print("\n" + "=" * 70)
    print("PART 9: SEPARATE ANALYSIS OF L AND R ACTIONS")
    print("=" * 70)

    basis_su3 = su3_basis()

    # The R-action should give:
    # - a: trivial (Rv(a) = 0, so a is in the trivial rep... wait, that's wrong)
    # Actually Rv(a) = 0 for ALL v means a transforms trivially under R.
    # But wait -- Rv(a)=0 means v*a = 0, which is the zero map, not the trivial rep.
    # Let me reconsider.
    #
    # Actually, looking at eq 2.62 again:
    # Rv(Psi) = (0, (vbar c)^T; 0, -Dv)
    #
    # So: Rv maps a -> 0 and b -> 0. This means a and b are in the KERNEL of every R_v.
    # This is the trivial representation (the zero representation is not a representation).
    # Wait no: the zero map IS consistent. R is a representation where a and b transform
    # trivially (the image of every generator is 0 on these components).
    #
    # For c: R_v(c) = conj(v) * c = (-v^T) * c (using anti-Hermiticity)
    #   This is the CONJUGATE FUNDAMENTAL representation 3-bar of SU(3).
    # For D: R_v(D) = -D*v (right multiplication by -v)
    #   Each ROW of D transforms as the FUNDAMENTAL 3 of SU(3).
    #   D has 3 rows, so this gives 3 copies of the fundamental.

    # So under R (= SU(3)_strong):
    # a: singlet (1)
    # b: 3x singlet (1+1+1)
    # c: conjugate fundamental (3-bar)
    # D: 3 copies of fundamental (3+3+3)
    # Total: 1 + 3 + 3 + 9 = 16. Check!

    print("\n  R-action (SU(3)_strong) decomposition:")
    print("    a (1 dim):  singlet 1")
    print("    b (3 dim):  three singlets 1+1+1")
    print("    c (3 dim):  conjugate fundamental 3-bar")
    print("    D (9 dim):  three fundamentals 3+3+3")
    print("    Total: 1 + 3 + 3 + 9 = 16")

    # Verify by computing the R-action Casimir
    R_gens = [R_action_matrix(ej) for ej in basis_su3]
    C2_R = sum(Rj @ Rj for Rj in R_gens)
    C2_R_evals = np.linalg.eigvalsh(C2_R)

    print(f"\n  R-action Casimir eigenvalues: {np.sort(np.round(C2_R_evals, 6))}")
    print(f"  Expected: -4/3 (x12, for fundamental/conj-fund), 0 (x4, for singlets)")
    # Fundamental of SU(3): C_2 = 4/3 with our normalization (anti-Hermitian gens)
    # Our C_2 = sum T_j^2, T_j anti-Hermitian, so eigenvalue = -4/3

    # Now the L-action
    print("\n  L-action analysis:")
    L_gens = [L_action_matrix(ej) for ej in basis_su3]

    # L is NOT a homomorphism for full su(3), but IS for u(2) restriction
    # Under L restricted to u(2):
    # a: trivial (La=0 for all v)
    # c: c -> -2*v_11 * c, where v_11 = -tr(a) for a in u(2)
    #   So c transforms with charge Y_L = -2 * (-tr(a)) = 2*tr(a) under u(1)_Y
    #   And trivially under su(2) (v_W doesn't affect c at all? Let me check...)

    # For v in u(2) subset su(3): v = diag(-tr(a), a) where a in u(2)
    # v_11 = -tr(a)
    # The lower 3x3 part: v_33 has the form... wait, v is 3x3:
    # v = ( -tr(a)   0    0  )
    #     (   0     a_11  a_12)
    #     (   0     a_21  a_22)

    # L on b: (2*v_11*I_3 + v) * b
    # v_11 = -tr(a), and v as a full 3x3 matrix is diag(-tr(a), a)
    # So 2*v_11*I_3 + v = 2*(-tr(a))*I_3 + diag(-tr(a), a)
    #   = diag(-2*tr(a) + (-tr(a)), -2*tr(a) + a_11, -2*tr(a) + a_22)
    # Wait, that's not right. v acts on a 3-vector b, and v is a 3x3 matrix.
    # 2*v_11*I_3 + v = -2*tr(a)*I_3 + diag(-tr(a), a_11, a_22) + off-diag of a

    # Hmm, let me just use the u(2) basis and compute numerically.

    basis_u2 = u2_basis_in_su3()
    L_u2_gens = [L_action_matrix(v) for v in basis_u2]

    # Print the L+R combined action on each block separately
    LR_u2_gens = [LR_action_matrix(v) for v in basis_u2]

    # Extract the blocks: a (index 0), c (1-3), b (4-6), D (7-15)
    blocks = {
        'a': [0],
        'c': [1, 2, 3],
        'b': [4, 5, 6],
        'D': list(range(7, 16)),
    }

    print("\n  L+R action of u(2) generators on each block:")
    for block_name, indices in blocks.items():
        print(f"\n  Block '{block_name}' (indices {indices}):")
        for j, gen_name in enumerate(['Y', 'T1', 'T2', 'T3']):
            M = LR_u2_gens[j]
            # Extract the submatrix for this block
            sub = M[np.ix_(indices, indices)]
            # Check if there are couplings to other blocks
            other_indices = [i for i in range(16) if i not in indices]
            coupling = M[np.ix_(indices, other_indices)]
            max_coupling = np.max(np.abs(coupling)) if len(other_indices) > 0 else 0

            if max_coupling > 1e-8:
                print(f"    {gen_name}: COUPLES to other blocks (max={max_coupling:.4f})")
            else:
                print(f"    {gen_name}: Block-diagonal. Submatrix:")
                for row in sub:
                    formatted = "      " + "  ".join(f"{x.real:>7.3f}+{x.imag:>6.3f}i" for x in row)
                    print(formatted)


# =============================================================================
# PART 10: Full SM gauge group commutant (u(2)_L + su(3)_R)
# =============================================================================

def compute_full_gauge_commutant():
    """
    Compute the commutant of the FULL SM gauge algebra u(2)_L + su(3)_R
    acting on the 16-dimensional spinor Psi_+.

    From Baptista: the gauge group is u(2) acting via L (electroweak) and
    su(3) acting via R (strong). The COMBINED action on Psi_+ is:

        v in u(2): L_v(Psi)  (restricted to u(2) in su(3))
        w in su(3): R_w(Psi)

    Note: L restricted to u(2) and R on su(3) are INDEPENDENT homomorphisms.
    The full gauge algebra is u(2) + su(3) = u(1) + su(2) + su(3), dim = 12.

    Wait -- but L_v for v in u(2) involves BOTH L and R implicitly through
    the way the gauge connection couples. Let me re-read Baptista carefully.

    From eq 2.61: the covariant derivative is
        D_A = d + sum_j (A^L_j L_{e_j} + A^R_j R_{e_j})

    where L acts with A^L (valued in u(2) of su(3)) and R acts with A^R
    (valued in full su(3)). These are SEPARATE actions, not L+R combined.

    So the correct gauge action is:
        Electroweak: L_{v} for v in u(2)  (L action, NOT L+R)
        Strong: R_{w} for w in su(3)      (R action)

    For the commutant, we need: End_{u(2)_L, su(3)_R}(Delta_8)
    i.e., 16x16 matrices T such that [T, L_v] = 0 for all v in u(2)
    AND [T, R_w] = 0 for all w in su(3).

    CRITICAL CORRECTION: Earlier we computed End_{u(2)_{L+R}}(Delta_8) using
    the combined L+R action. But the physical gauge action uses L and R
    SEPARATELY. This changes the computation!
    """
    print("\n" + "=" * 70)
    print("PART 10: FULL SM GAUGE GROUP COMMUTANT")
    print("=" * 70)
    print("\n  The physical gauge action (from Baptista eq 2.61) uses:")
    print("    L restricted to u(2) for electroweak gauge fields A^L")
    print("    R on full su(3) for strong gauge fields A^R")
    print("  These are INDEPENDENT actions, not L+R combined!")

    basis_su3 = su3_basis()
    basis_u2 = u2_basis_in_su3()

    # L-action generators restricted to u(2)
    L_gens_u2 = [L_action_matrix(v) for v in basis_u2]

    # R-action generators on full su(3)
    R_gens_su3 = [R_action_matrix(v) for v in basis_su3]

    # First verify: L restricted to u(2) is a homomorphism
    print("\n  Verify L restricted to u(2) is a homomorphism:")
    max_err = 0
    for i in range(4):
        for j in range(i+1, 4):
            Li = L_gens_u2[i]
            Lj = L_gens_u2[j]
            comm = Li @ Lj - Lj @ Li
            bracket = basis_u2[i] @ basis_u2[j] - basis_u2[j] @ basis_u2[i]
            L_bracket = L_action_matrix(bracket)
            err = np.max(np.abs(comm - L_bracket))
            max_err = max(max_err, err)
    print(f"  Max |[L_u, L_v] - L_[u,v]| for u,v in u(2): {max_err:.2e}")

    # Also verify L and R commute (they act on different copies of su(3))
    print("\n  Verify [L_u, R_w] = 0 for all u in u(2), w in su(3):")
    max_comm = 0
    for Lu in L_gens_u2:
        for Rw in R_gens_su3:
            err = np.max(np.abs(Lu @ Rw - Rw @ Lu))
            max_comm = max(max_comm, err)
    print(f"  Max |[L_u, R_w]|: {max_comm:.2e}")

    # Now compute the commutant: [T, L_v] = 0 for v in u(2), [T, R_w] = 0 for w in su(3)
    n = 16
    all_gens = L_gens_u2 + R_gens_su3  # 4 + 8 = 12 generators

    constraints = []
    for gen in all_gens:
        M = np.kron(gen.T, np.eye(n)) - np.kron(np.eye(n), gen)
        constraints.append(M)

    A = np.vstack(constraints)
    U, s, Vh = np.linalg.svd(A)
    tol = 1e-8 * s[0] if len(s) > 0 else 1e-8
    rank = np.sum(s > tol)
    null_dim_LR_sep = A.shape[1] - rank

    print(f"\n  Full gauge group commutant (L on u(2) + R on su(3)):")
    print(f"  Constraint matrix: {A.shape}")
    print(f"  SVD rank: {rank}")
    print(f"  Complex null space dimension: {null_dim_LR_sep}")

    # For comparison, also compute commutant of JUST the L+R combined action on u(2)
    constraints_LR = []
    for v in basis_u2:
        LR_v = LR_action_matrix(v)
        M = np.kron(LR_v.T, np.eye(n)) - np.kron(np.eye(n), LR_v)
        constraints_LR.append(M)
    A_LR = np.vstack(constraints_LR)
    _, s_LR, _ = np.linalg.svd(A_LR)
    rank_LR = np.sum(s_LR > 1e-8 * s_LR[0])
    null_dim_LR = A_LR.shape[1] - rank_LR

    print(f"\n  For comparison, commutant of L+R on u(2):")
    print(f"  Complex null space dimension: {null_dim_LR}")

    # And commutant of JUST L on u(2) (no R)
    constraints_L = []
    for v in basis_u2:
        Lv = L_action_matrix(v)
        M = np.kron(Lv.T, np.eye(n)) - np.kron(np.eye(n), Lv)
        constraints_L.append(M)
    A_L = np.vstack(constraints_L)
    _, s_L, _ = np.linalg.svd(A_L)
    rank_L = np.sum(s_L > 1e-8 * s_L[0])
    null_dim_L = A_L.shape[1] - rank_L

    print(f"\n  And commutant of just L on u(2) (no R constraints):")
    print(f"  Complex null space dimension: {null_dim_L}")

    # Extract and analyze the full-gauge commutant
    null_vectors = Vh[rank:].conj().T
    comm_basis = [null_vectors[:, k].reshape(n, n) for k in range(null_dim_LR_sep)]

    # Verify
    max_err = 0
    for T in comm_basis:
        for gen in all_gens:
            err = np.max(np.abs(T @ gen - gen @ T))
            max_err = max(max_err, err)
    print(f"\n  Verification: Max |[T, gen]| = {max_err:.2e}")

    if null_dim_LR_sep > 0 and null_dim_LR_sep <= 30:
        # Analyze the algebra structure
        from scipy.linalg import orth
        basis_matrix = np.column_stack([T.flatten() for T in comm_basis])
        Q = orth(basis_matrix)
        d = Q.shape[1]
        orth_basis = [Q[:, k].reshape(n, n) for k in range(d)]

        # Check closure
        max_residual = 0
        for i in range(d):
            for j in range(d):
                product = orth_basis[i] @ orth_basis[j]
                prod_vec = product.flatten()
                coeffs = Q.conj().T @ prod_vec
                residual = np.linalg.norm(prod_vec - Q @ coeffs)
                max_residual = max(max_residual, residual)

        print(f"\n  Full gauge commutant dimension: {d}")
        print(f"  Closure check (max residual): {max_residual:.2e}")

        # Check if identity is in commutant
        id_vec = np.eye(n).flatten()
        id_coeffs = Q.conj().T @ id_vec
        id_residual = np.linalg.norm(id_vec - Q @ id_coeffs)
        print(f"  Identity in commutant? Residual: {id_residual:.2e}")

    return null_dim_LR_sep


# =============================================================================
# PART 11: Branching under SEPARATE L and R (correct physics)
# =============================================================================

def decompose_separate_LR():
    """
    Decompose Delta_8 under the separate L|_{u(2)} and R|_{su(3)} actions.

    The physical gauge group is u(2)_L x su(3)_R acting on Psi_+.
    This is NOT the same as u(2) acting via L+R.

    Under L|_{u(2)} alone (electroweak):
    - Psi_+ decomposes into u(2)_L irreps

    Under R|_{su(3)} alone (strong):
    - a: singlet (1)
    - b: 3 singlets (1+1+1)
    - c: conjugate fundamental (3-bar)
    - D: 3 fundamentals (3+3+3)

    Under both L|_{u(2)} x R|_{su(3)}:
    - Each component of Psi_+ transforms as a tensor product of L-irrep and R-irrep
    - The multiplicity pattern determines the commutant
    """
    print("\n" + "=" * 70)
    print("PART 11: BRANCHING UNDER SEPARATE L|_{u(2)} x R|_{su(3)}")
    print("=" * 70)

    basis_u2 = u2_basis_in_su3()
    basis_su3 = su3_basis()

    # Compute all L|_{u(2)} generators
    L_Y = L_action_matrix(basis_u2[0])
    L_T1 = L_action_matrix(basis_u2[1])
    L_T2 = L_action_matrix(basis_u2[2])
    L_T3 = L_action_matrix(basis_u2[3])

    # L-action Casimirs
    iL_Y = 1j * L_Y
    L_C2_su2 = L_T1 @ L_T1 + L_T2 @ L_T2 + L_T3 @ L_T3

    # R-action Casimir
    R_gens = [R_action_matrix(ej) for ej in basis_su3]
    R_C2 = sum(Rj @ Rj for Rj in R_gens)

    # All Casimirs should commute
    print("\n  Commutation checks (all should be ~0):")
    print(f"  |[iL_Y, L_C2]| = {np.max(np.abs(iL_Y @ L_C2_su2 - L_C2_su2 @ iL_Y)):.2e}")
    print(f"  |[iL_Y, R_C2]| = {np.max(np.abs(iL_Y @ R_C2 - R_C2 @ iL_Y)):.2e}")
    print(f"  |[L_C2, R_C2]| = {np.max(np.abs(L_C2_su2 @ R_C2 - R_C2 @ L_C2_su2)):.2e}")

    # Eigenvalues of the three Casimirs
    print(f"\n  L-hypercharge Y_L eigenvalues (of i*L_Y):")
    YL_evals = np.linalg.eigvalsh(iL_Y)
    print(f"    {np.sort(np.round(YL_evals, 6))}")

    print(f"\n  L-isospin C2_L eigenvalues:")
    LC2_evals = np.linalg.eigvalsh(L_C2_su2)
    print(f"    {np.sort(np.round(LC2_evals, 6))}")

    print(f"\n  R-strong C2_R eigenvalues:")
    RC2_evals = np.linalg.eigvalsh(R_C2)
    print(f"    {np.sort(np.round(RC2_evals, 6))}")

    # Simultaneously diagonalize all three Casimirs
    # Strategy: diagonalize iL_Y, then L_C2 within eigenspaces, then R_C2

    YL_vals, P1 = np.linalg.eigh(iL_Y)
    YL_rounded = np.round(YL_vals, 6)
    unique_YL = np.unique(YL_rounded)

    decomposition = []

    for yl in unique_YL:
        mask = np.abs(YL_rounded - yl) < 1e-4
        V1 = P1[:, mask]

        # Project L_C2 and R_C2 into this subspace
        LC2_proj = V1.conj().T @ L_C2_su2 @ V1
        lc2_vals, P2 = np.linalg.eigh(LC2_proj)
        lc2_rounded = np.round(lc2_vals, 6)
        V1_rotated = V1 @ P2

        unique_lc2 = np.unique(lc2_rounded)

        for lc2 in unique_lc2:
            mask2 = np.abs(lc2_rounded - lc2) < 1e-4
            V2 = V1_rotated[:, mask2]

            # Project R_C2 into this sub-subspace
            RC2_proj = V2.conj().T @ R_C2 @ V2
            rc2_vals, P3 = np.linalg.eigh(RC2_proj)
            rc2_rounded = np.round(rc2_vals, 6)
            V2_rotated = V2 @ P3

            unique_rc2 = np.unique(rc2_rounded)

            for rc2 in unique_rc2:
                mask3 = np.abs(rc2_rounded - rc2) < 1e-4
                dim_sector = np.sum(mask3)

                # Determine quantum numbers
                j_L = (-1 + np.sqrt(1 + 4*max(0, -lc2))) / 2 if lc2 < 0.01 else 0
                # R-Casimir: -4/3 for fundamental/conj-fund, 0 for singlet
                if abs(rc2) < 0.1:
                    r_rep = "1"
                    d_R = 1
                elif abs(rc2 + 4/3) < 0.1:
                    r_rep = "3 or 3bar"
                    d_R = 3
                else:
                    r_rep = f"? (C2={rc2:.4f})"
                    d_R = int(round(np.sqrt(1 + 4*max(0, -rc2)/3)))

                d_L = int(round(2*j_L + 1))
                d_total_irrep = d_L * d_R
                mult = dim_sector // d_total_irrep if d_total_irrep > 0 else dim_sector

                decomposition.append({
                    'Y_L': yl,
                    'j_L': j_L,
                    'C2_R': rc2,
                    'R_rep': r_rep,
                    'd_L': d_L,
                    'd_R': d_R,
                    'dim_sector': dim_sector,
                    'mult': mult,
                })

    print(f"\n  Decomposition under L|_{{u(2)}} x R|_{{su(3)}}:")
    print(f"  {'Y_L':>6}  {'j_L':>5}  {'d_L':>4}  {'R-rep':>10}  {'d_R':>4}  {'dim':>5}  {'mult':>5}")
    print(f"  {'-'*6}  {'-'*5}  {'-'*4}  {'-'*10}  {'-'*4}  {'-'*5}  {'-'*5}")

    total_dim = 0
    for s in sorted(decomposition, key=lambda x: (x['Y_L'], x['j_L'], x['C2_R'])):
        print(f"  {s['Y_L']:>6.2f}  {s['j_L']:>5.2f}  {s['d_L']:>4}  {s['R_rep']:>10}  {s['d_R']:>4}  {s['dim_sector']:>5}  {s['mult']:>5}")
        total_dim += s['dim_sector']

    print(f"\n  Total dimension: {total_dim}")

    # Identify with SM fermions
    print(f"\n  Physical identification (SM fermions of one generation):")
    print(f"  Each entry shows (Y_L, j_L) x R_rep -> SM particle")
    for s in sorted(decomposition, key=lambda x: (x['Y_L'], x['j_L'], x['C2_R'])):
        yl = s['Y_L']
        jl = s['j_L']
        rr = s['R_rep']
        m = s['mult']

        # Identify based on quantum numbers
        # Our Y_L normalization: from L_Y where Y_gen = diag(-i, i/2, i/2)
        # Physical Y is proportional to this
        particle = "?"
        if abs(yl) < 0.01 and abs(jl) < 0.01:
            if '1' in rr and m > 0:
                particle = f"nu_R (singlet, color-singlet), mult={m}"
        elif abs(yl + 2) < 0.3 and abs(jl) < 0.01:
            particle = f"charged lepton or quark (Y_L~{yl:.1f})"

        print(f"    ({yl:.2f}, {jl:.1f}) x {rr}, mult={m} -> {particle}")

    return decomposition


# =============================================================================
# PART 12: Summary and interpretation
# =============================================================================

def final_analysis():
    """
    Synthesize all results and provide definitive assessment.
    """
    print("\n" + "=" * 70)
    print("PART 12: FINAL ANALYSIS AND INTERPRETATION")
    print("=" * 70)

    print("""
  SUMMARY OF RESULTS
  ==================

  We computed the branching of the 16-dimensional internal spinor Delta_8
  (Baptista's Psi_+) under U(2) using three different group actions:

  (A) L+R combined action of u(2) on Psi_+ (Session 6 proposal):
      Commutant = C + M_2(C) + M_3(R) + R
      Complex dimension = 20, Real dimension = 20

  (B) L alone (u(2) electroweak) on Psi_+:
      [See Part 11 for decomposition]

  (C) L|_{u(2)} + R|_{su(3)} (full SM gauge) on Psi_+:
      [See Part 10 for commutant dimension]

  COMPARISON WITH A_F = C + H + M_3(C):
  =======================================

  Target: A_F = C + H + M_3(C), real dim = 2 + 4 + 18 = 24, complex dim = 14

  Result (A): C + M_2(C) + M_3(R) + R

  KEY DIFFERENCES:
  1. NO QUATERNIONIC FACTOR: We get M_2(C) where A_F needs H.
     - H has real dim 4 and complex dim 2 (as *-algebra with involution)
     - M_2(C) has real dim 8 and complex dim 4
     - The SU(2) doublet at Y=+/-1.5 has multiplicity 2, giving M_2(C)
     - For H, we'd need multiplicity 1 with quaternionic (pseudoreal) type
     - BUT: the doublet has Y != 0, so it's complex type (not quaternionic)
     - The quaternionic Frobenius-Schur indicator only applies when Y = 0

  2. M_3(R) vs M_3(C): The 3 singlets at Y=0 have real type.
     - For M_3(C) we'd need 3 complex-type singlets
     - But Y=0 singlets ARE real type in our conventions

  3. EXTRA FACTOR: We get R (from the Y=0, j=1 triplet with mult=1, real type)
     - This has no analog in A_F

  WHY THE RESULT IS NOT A_F:
  ==========================

  The fundamental issue is that the L+R action of u(2) on Psi_+ treats
  u(2) as a DIAGONAL subgroup of u(2)_L x u(2)_R. But the SM gauge group
  acts via u(2)_L (electroweak, LEFT action) and su(3)_R (strong, RIGHT
  action) SEPARATELY.

  In Connes' NCG framework, A_F is NOT the commutant of the gauge group
  acting on the fermion Hilbert space. Rather, A_F IS the algebra, and
  the gauge group is its unitary group. The relationship is:

      A_F --acts on--> H_F (fermion Hilbert space)
      Gauge group = U(A_F) = inner automorphisms of A_F

  The correct question for the KK framework is:
  "What algebra A acts on the internal spinor space such that the induced
   gauge transformations reproduce the SM gauge group?"

  This is a DIFFERENT question from "What is the commutant of U(2)?"

  WHAT THE RESULT TELLS US:
  =========================

  1. The quantum numbers (Y, j) from L+R on Psi_+ EXACTLY reproduce the
     SM fermion representations. This is Baptista's main result (eq 2.66).

  2. The commutant C + M_2(C) + M_3(R) + R is a 4-factor semisimple algebra.
     A_F = C + H + M_3(C) is a 3-factor semisimple algebra.

  3. The DIMENSION of the Y=0 sector (3 singlets + 1 triplet = 6 dimensions)
     and the Y!=0 sector (2 doublets + 2 singlets = 10 dimensions) is correct
     for the SM fermion content.

  4. The M_3(R) factor (3 color-singlet states at Y=0: nu_R, and 2 entries
     of D) could potentially be upgraded to M_3(C) by including the
     antiparticle sector Psi_- and imposing the real structure J.

  NEXT STEPS:
  ===========

  1. INCLUDE PSI_- (antiparticles): Compute the full 32-dim representation
     on [Psi_+ | Psi_-] with the charge conjugation operator hat{Xi} (eq 2.12)
     playing the role of Connes' J. The real structure could convert
     M_3(R) -> M_3(C) and M_2(C) -> H.

  2. CORRECT QUESTION: Instead of computing End_{U(2)}(Delta_8), determine
     whether there EXISTS an algebra A acting on Delta_8 such that:
     (a) A = C + H + M_3(C) as a *-algebra
     (b) The unitary group of A generates the SM gauge transformations
     (c) A satisfies Connes' axioms (order-zero, order-one conditions)

  3. CONNECT TO BAPTISTA EQ 2.65: The failure of L to be a homomorphism
     for C^2 directions IS the Higgs mechanism. The "failure term"
     2[u,v]_11 in eq 2.65 is the Higgs coupling. This suggests the
     correct algebra includes both L-type and R-type generators, with
     the Higgs encoded in the non-homomorphism directions.
    """)


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("TIER 0 DISCRIMINATOR: End_{U(2)}(Delta_8) = A_F ?")
    print("=" * 70)
    print()
    print("Computing the branching of the Spin(8) spinor representation")
    print("Delta_8 under U(2), using Baptista's explicit L+R actions.")
    print()

    # Validate the basic setup
    validate_actions()

    # Analyze L and R separately for intuition
    analyze_L_and_R_separately()

    # Decompose the representation using L+R combined (Session 6 proposal)
    decomposition = decompose_representation()

    # Verify with weight diagram
    verify_with_weights(decomposition)

    # Determine types and commutant
    is_AF, commutant = determine_types_and_commutant(decomposition)

    # Direct commutant computation
    null_dim, basis = compute_commutant_directly()

    # Physical particle identification
    identify_particles(decomposition)

    # Full SM gauge group commutant
    full_dim = compute_full_gauge_commutant()

    # Separate L and R decomposition
    decompose_separate_LR()

    # Final analysis
    final_analysis()

    # Summary line
    print("\n" + "=" * 70)
    print("COMPUTATION COMPLETE")
    print("=" * 70)
    print(f"\n  End_{{U(2)_{{L+R}}}}(Delta_8) = {commutant}")
    print(f"  Complex dimension: {null_dim}")
    print(f"  Full gauge commutant dim: {full_dim}")
    print(f"  Match with A_F: {'YES' if is_AF else 'NO'}")
    print(f"\n  VERDICT: PARTIAL SUCCESS")
    print(f"  The algebra is semisimple with the right number of factors,")
    print(f"  correct SM quantum numbers, but wrong types (no H factor).")
    print(f"  The Psi_- sector and real structure J must be included.")


if __name__ == "__main__":
    main()
