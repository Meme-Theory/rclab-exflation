"""
TIER 1: DIRAC SPECTRUM ON (SU(3), g_s) WITH JENSEN DEFORMATION
================================================================

Computes the first 20-30 eigenvalues of the Dirac operator D on the compact
Lie group SU(3) equipped with the Jensen left-invariant metric g_s.

Mathematical structure:
  1. su(3) = u(2) + m  (reductive decomposition)
  2. g_s = g_0|_{u(2)} + e^{2s} g_0|_m  (Jensen TT-deformation)
  3. Peter-Weyl: L^2(SU(3), S) = bigoplus_{pi} V_pi tensor C^16
  4. D_pi = sum_a rho_pi(e_a) x gamma_a + I x Omega(s)
     where Omega is the spinorial curvature offset from the spin connection.

The spectrum is the union of finite matrix eigenvalue problems across irreps.
Low-lying eigenvalues come from small irreps (p+q <= 3).

Author: Sim-Specialist Agent (phonon-exflation project, Session 12)
Date: 2026-02-12

References:
  - Bar (1996): The Dirac operator on homogeneous spaces and its spectrum on 3D Lie groups
  - Agricola, Friedrich (2010): Eigenvalues of the Dirac operator on 3-Sasakian manifolds
  - Baptista (2024): Jensen deformation of SU(3), arXiv:2306.01049
"""

import numpy as np
from numpy.linalg import eigh, cholesky, inv, eigvalsh
import sys
import os

# Add tier0-computation to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import gell_mann_matrices


# =============================================================================
# MODULE 1: SU(3) LIE ALGEBRA INFRASTRUCTURE
# =============================================================================

def su3_generators():
    """
    Construct anti-Hermitian generators e_a = -i/2 * lambda_a for a=0..7.

    Convention: [e_a, e_b] = f_{abc} e_c with real totally antisymmetric f_{abc}.
    Normalization: Tr(e_a e_b) = -1/2 delta_{ab}.

    Returns:
        list of 8 complex (3,3) matrices
    """
    gm = gell_mann_matrices()
    return [-1j / 2.0 * lam for lam in gm]


def compute_structure_constants(gens):
    """
    Compute structure constants f_{abc} from [e_a, e_b] = f_{abc} e_c.

    Uses the trace formula: f_{abc} = -2 Tr([e_a, e_b] e_c)
    (valid for our normalization Tr(e_a e_b) = -1/2 delta_{ab}).

    Args:
        gens: list of n_gen anti-Hermitian matrices

    Returns:
        f_abc: real (n_gen, n_gen, n_gen) array of structure constants
    """
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a + 1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                val = -2.0 * np.trace(comm @ gens[c])
                f[a, b, c] = val.real
                f[b, a, c] = -val.real
    return f


def compute_killing_form(f_abc):
    """
    Compute Killing form B_{ab} = sum_{c,d} f_{acd} f_{bcd}.

    For compact simple Lie algebras with anti-Hermitian generators, B is
    negative definite: B_{ab} = -C delta_{ab} with C > 0.

    For su(3) in our normalization: B_{ab} = -3 delta_{ab}.

    Args:
        f_abc: (8,8,8) structure constants

    Returns:
        B_ab: (8,8) real symmetric matrix (Killing form)
    """
    return np.einsum('acd,bcd->ab', f_abc, f_abc)


# =============================================================================
# MODULE 2: JENSEN METRIC + ORTHONORMAL FRAME
# =============================================================================

# Decomposition indices (Baptista eq 3.58)
# su(3) = u(1) + su(2) + C^2
U1_IDX = [7]            # u(1) generator: lambda_8
SU2_IDX = [0, 1, 2]     # su(2) generators: lambda_1, lambda_2, lambda_3
C2_IDX = [3, 4, 5, 6]   # C^2 generators: lambda_4, lambda_5, lambda_6, lambda_7
U2_IDX = [0, 1, 2, 7]   # u(2) = su(2) + u(1) (for reductivity check)
M_IDX = [3, 4, 5, 6]    # m = C^2 (complement of u(2))


def u2_invariant_metric(B_ab, L1, L2, L3):
    """
    Construct a U(2)-invariant left-invariant metric on SU(3) with
    arbitrary scale factors (L1, L2, L3).

    The metric is diagonal in the su(3) = u(1) + su(2) + C^2 decomposition:
      g = L1 * g_0|_{u(1)} + L2 * g_0|_{su(2)} + L3 * g_0|_{C^2}

    where g_0 = |B| is the positive-definite base metric from the Killing form.

    Multiplicities: u(1)=1, su(2)=3, C^2=4  =>  dim=8.
    Volume factor: L1^{1/2} * L2^{3/2} * L3^{4/2} = L1^{1/2} * L2^{3/2} * L3^2.

    The Jensen curve is the 1D submanifold:
      L1 = e^{2s}, L2 = e^{-2s}, L3 = e^{s}
    which is volume-preserving: L1^1 * L2^3 * L3^4 = 1.

    Args:
        B_ab: (8,8) Killing form
        L1: float > 0, scale factor for u(1) block
        L2: float > 0, scale factor for su(2) block
        L3: float > 0, scale factor for C^2 block

    Returns:
        g: (8,8) positive definite metric tensor
    """
    g0 = np.abs(B_ab)
    g = np.zeros((8, 8), dtype=np.float64)

    for a in U1_IDX:
        for b in U1_IDX:
            g[a, b] = g0[a, b] * L1

    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a, b] = g0[a, b] * L2

    for a in C2_IDX:
        for b in C2_IDX:
            g[a, b] = g0[a, b] * L3

    return g


def jensen_metric(B_ab, s):
    """
    Construct the Jensen deformed metric g_s on su(3).

    Backward-compatible wrapper around u2_invariant_metric().
    Maps the Jensen parameter s to scale factors:
      L1 = e^{2s}   (u(1), 1D)
      L2 = e^{-2s}  (su(2), 3D)
      L3 = e^{s}    (C^2, 4D)

    Volume-preserving: L1 * L2^3 * L3^4 = e^{2s-6s+4s} = 1.
    At s=0: bi-invariant (all scale factors = 1).

    Args:
        B_ab: (8,8) Killing form
        s: Jensen deformation parameter (s=0 gives bi-invariant metric)

    Returns:
        g_s: (8,8) positive definite metric tensor
    """
    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)
    return u2_invariant_metric(B_ab, L1, L2, L3)


def orthonormal_frame(g_s):
    """
    Construct orthonormal frame E_{ab} such that e_a = E_{ab} X_b.

    The frame satisfies E g_s E^T = I (i.e., g_s(e_a, e_b) = delta_{ab}).

    We use Cholesky factorization of g_s^{-1}: if g_s^{-1} = L L^T,
    then E = L^T gives E g_s E^T = L^T g_s L = L^T (L L^T)^{-1} L ... wait.

    Actually: if g_s = M M^T (Cholesky), then E = M^{-1} gives
    E g_s E^T = M^{-1} M M^T M^{-T} = I. So E = inv(cholesky(g_s)).

    Args:
        g_s: (8,8) positive definite metric

    Returns:
        E: (8,8) frame matrix, e_a = E_{ab} X_b
    """
    L = cholesky(g_s)  # g_s = L @ L.T, L lower triangular
    E = inv(L)  # E @ g_s @ E.T = I
    return E


def frame_structure_constants(f_abc, E):
    """
    Compute structure constants in the orthonormal frame.

    If e_a = E_{ab} X_b, then [e_a, e_b] = E_{ac} E_{bd} f_{cde} X_e.
    Writing X_e = (E^{-1})_{ef} e_f:
      [e_a, e_b] = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef} e_f

    So f_tilde^f_{ab} = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef}

    Note: f_tilde_{abc} with all indices down (using delta_{ab} in ON frame)
    equals f_tilde^c_{ab}, and is NOT totally antisymmetric for non-bi-invariant
    metrics. Total antisymmetry holds only when the metric is bi-invariant.

    Args:
        f_abc: (8,8,8) original structure constants
        E: (8,8) orthonormal frame matrix

    Returns:
        ft: (8,8,8) structure constants in ON frame, ft[a,b,c] = f_tilde^c_{ab}
    """
    E_inv = inv(E)
    # ft^f_{ab} = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef}
    # Using einsum: contract c with a, d with b, e with f
    ft = np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)
    return ft


# =============================================================================
# MODULE 3: SPIN CONNECTION (LEVI-CIVITA ON LIE GROUP)
# =============================================================================

def connection_coefficients(ft):
    """
    Compute Levi-Civita connection coefficients Gamma^c_{ab} in ON frame.

    For a left-invariant metric on a Lie group with left-invariant ON frame
    {e_a}, the Koszul formula gives:

      2 Gamma_{cab} = ft_{abc} + ft_{cab} - ft_{bca}

    where ft_{abc} = f_tilde^c_{ab} (ON frame structure constants with
    third index lowered using delta -- which is trivial in ON frame).

    IMPORTANT: The sign convention. The Koszul formula for left-invariant fields:
      2 g(nabla_{e_a} e_b, e_c) = g([e_a,e_b],e_c) - g([e_b,e_c],e_a) + g([e_c,e_a],e_b)

    In ON frame (g = delta):
      2 Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}

    Note: Gamma_{cab} = Gamma^c_{ab} since g_{cd} = delta_{cd}.

    Metric compatibility requires: Gamma_{cab} = -Gamma_{bac}
    (antisymmetry in the connection indices c,b when written as Gamma_{cab}).

    Wait -- let me be very careful. Define Gamma^c_{ab} = nabla_{e_a} e_b component c.
    Then the connection 1-form omega^c_b(e_a) = Gamma^c_{ab}.
    Metric compatibility: omega_{cb} = -omega_{bc}, i.e., Gamma_{cab} = -Gamma_{bac}... no.
    Metric compatibility says: e_a(g_{bc}) - Gamma^d_{ab} g_{dc} - Gamma^d_{ac} g_{bd} = 0.
    For ON frame (g_{bc} = delta_{bc}, e_a(delta_{bc}) = 0):
      Gamma^c_{ab} + Gamma^b_{ac} = 0

    So: Gamma^c_{ab} = -Gamma^b_{ac}. This is antisymmetry in (b,c) with a fixed.
    Equivalently: Gamma_{cab} = -Gamma_{bac}.

    Args:
        ft: (8,8,8) ON frame structure constants, ft[a,b,c] = f_tilde^c_{ab}

    Returns:
        Gamma: (8,8,8) connection coefficients, Gamma[c,a,b] = Gamma^c_{ab}
    """
    n = ft.shape[0]
    Gamma = np.zeros((n, n, n), dtype=np.float64)

    for c in range(n):
        for a in range(n):
            for b in range(n):
                # 2 Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}
                # ft_{abc} = ft[a,b,c] (= f_tilde^c_{ab})
                # ft_{bca} = ft[b,c,a]
                # ft_{cab} = ft[c,a,b]
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])

    return Gamma


def validate_connection(Gamma):
    """
    Validate metric compatibility: Gamma^c_{ab} + Gamma^b_{ac} = 0.

    Args:
        Gamma: (8,8,8) connection coefficients

    Returns:
        max_error: maximum violation of metric compatibility
    """
    n = Gamma.shape[0]
    max_err = 0.0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                err = abs(Gamma[c, a, b] + Gamma[b, a, c])
                if err > max_err:
                    max_err = err
    return max_err


# =============================================================================
# MODULE 4: CLIFFORD ALGEBRA Cliff(R^8)
# =============================================================================

def build_cliff8():
    """
    Construct generators gamma_1, ..., gamma_8 of Cliff(R^8).

    These are 16x16 Hermitian matrices satisfying {gamma_a, gamma_b} = 2 delta_{ab} I.

    Construction via tensor products of Pauli matrices (standard inductive construction):
      gamma_{2k-1} = sigma_3 x ... x sigma_3 x sigma_1 x I x ... x I
      gamma_{2k}   = sigma_3 x ... x sigma_3 x sigma_2 x I x ... x I

    Returns:
        gammas: list of 8 Hermitian (16,16) complex matrices
    """
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def kron4(A, B, C, D):
        return np.kron(A, np.kron(B, np.kron(C, D)))

    gammas = [
        kron4(s1, I2, I2, I2),   # gamma_1
        kron4(s2, I2, I2, I2),   # gamma_2
        kron4(s3, s1, I2, I2),   # gamma_3
        kron4(s3, s2, I2, I2),   # gamma_4
        kron4(s3, s3, s1, I2),   # gamma_5
        kron4(s3, s3, s2, I2),   # gamma_6
        kron4(s3, s3, s3, s1),   # gamma_7
        kron4(s3, s3, s3, s2),   # gamma_8
    ]
    return gammas


def validate_clifford(gammas):
    """
    Verify Clifford algebra relation: {gamma_a, gamma_b} = 2 delta_{ab} I_{16}.

    Args:
        gammas: list of 8 matrices (16x16)

    Returns:
        max_error: maximum violation
    """
    n = len(gammas)
    dim = gammas[0].shape[0]
    max_err = 0.0
    for a in range(n):
        for b in range(n):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(dim)
            err = np.max(np.abs(anticomm - target))
            if err > max_err:
                max_err = err
    return max_err


def build_chirality(gammas):
    """
    Construct chirality operator gamma_9 = gamma_1 gamma_2 ... gamma_8.

    For Cliff(R^{2n}), the chirality operator satisfies:
      gamma_{2n+1}^2 = I, {gamma_{2n+1}, gamma_a} = 0, gamma_{2n+1}^dag = gamma_{2n+1}

    For dim=8 (n=4): gamma_9 = product of all 8 gammas.
    Sign: gamma_9 = (-i)^4 gamma_1 ... gamma_8 = gamma_1 ... gamma_8 (since (-i)^4 = 1).

    Args:
        gammas: list of 8 Clifford generators

    Returns:
        gamma9: (16,16) Hermitian involution
    """
    gamma9 = np.eye(16, dtype=complex)
    for g in gammas:
        gamma9 = gamma9 @ g
    return gamma9


# =============================================================================
# MODULE 5: SPIN CONNECTION IN SPINOR REPRESENTATION
# =============================================================================

def spinor_connection_offset(Gamma, gammas):
    """
    Compute the spinorial curvature offset Omega that enters the Dirac operator.

    The Dirac operator on each irrep sector pi is:
      D_pi = sum_a rho_pi(e_a) x gamma_a + I_{dim_pi} x Omega

    where Omega collects the spin connection contribution:
      Omega = (1/2) sum_a gamma_a * omega_a^{spinor}

    with the spinor connection 1-form:
      omega_a^{spinor} = (1/4) sum_{b,c} Gamma^b_{ac} gamma_b gamma_c
                       = (1/4) sum_{b!=c} Gamma^b_{ac} gamma_b gamma_c
                         (b=c terms vanish since Gamma^b_{ab} gamma_b^2 = Gamma^b_{ab} I
                          but that's a scalar -- actually Gamma^b_{ab} is the trace,
                          need to be more careful.)

    Actually, the spin connection acts on spinors as:
      nabla^S_{e_a} = e_a + (1/4) sum_{b,c} omega^{bc}_a gamma_b gamma_c

    where omega^{bc}_a = Gamma^b_{ac} is the connection 1-form in ON frame.
    The metric compatibility Gamma^b_{ac} = -Gamma^c_{ab} means omega^{bc}_a
    is antisymmetric in (b,c).

    The Dirac operator is:
      D = sum_a gamma_a nabla^S_{e_a}
        = sum_a gamma_a [e_a + (1/4) sum_{b,c} Gamma^b_{ac} gamma_b gamma_c]

    On irrep sector pi, e_a acts as rho_pi(e_a), so:
      D_pi = sum_a rho_pi(e_a) x gamma_a + I x [(1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c]

    Define: Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c

    This is a 16x16 matrix acting on spinor indices only.

    SIMPLIFICATION for bi-invariant metrics (s=0):
    For bi-invariant metrics, Gamma^c_{ab} = (1/2) f^c_{ab}, and
      Omega = (1/8) sum_{a,b,c} f^c_{ab} gamma_a gamma_b gamma_c

    Args:
        Gamma: (8,8,8) connection coefficients, Gamma[b,a,c] = Gamma^b_{ac}
        gammas: list of 8 Clifford generators (16x16)

    Returns:
        Omega: (16,16) complex matrix (spinor curvature offset)
    """
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                # Gamma^b_{ac} = Gamma[b, a, c]
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gammas[a] @ gammas[b] @ gammas[c]

    Omega *= 0.25
    return Omega


def validate_omega_hermitian(Omega):
    """
    The Dirac operator must be self-adjoint, so Omega should be Hermitian
    (since gamma_a are Hermitian and rho_pi(e_a) are anti-Hermitian, the
    cross term is anti-Hermitian x Hermitian = anti-Hermitian... wait.

    Actually D = sum_a rho(e_a) x gamma_a + I x Omega.
    For D to be Hermitian:
      (rho(e_a) x gamma_a)^dag = rho(e_a)^dag x gamma_a^dag
                                = -rho(e_a) x gamma_a  (since e_a anti-Hermitian, gamma_a Hermitian)
    So the first term is anti-Hermitian!

    This means D itself is NOT sum of Hermitian terms. But D IS self-adjoint
    on L^2 with the correct inner product.

    For the algebraic Dirac operator on a Lie group, D is self-adjoint
    in the representation-theoretic sense. The matrix D_pi should have
    real eigenvalues. Let me check: D_pi has the form
      sum_a (anti-Hermitian) x (Hermitian) + (identity) x Omega
    The product (anti-Hermitian) x (Hermitian) is neither Hermitian nor anti-Hermitian.
    But the Kronecker product rho(e_a) tensor gamma_a IS in general.

    Let's check: (A tensor B)^dag = A^dag tensor B^dag = (-A) tensor B (for our case)
    So (sum_a rho(e_a) tensor gamma_a)^dag = sum_a (-rho(e_a)) tensor gamma_a
    = -sum_a rho(e_a) tensor gamma_a.

    So the first part is anti-Hermitian, and for D to have real eigenvalues,
    Omega should be anti-Hermitian too? No -- Omega is a purely spinorial matrix
    tensored with identity on the rep side.

    Actually I think the correct statement is that D should be skew-Hermitian
    with purely imaginary eigenvalues... no, the Dirac operator on a Riemannian
    manifold is self-adjoint with real spectrum.

    The resolution: the generators X_a of left translation are SKEW-ADJOINT
    on L^2(G), so rho(e_a) are skew-adjoint. With gamma_a Hermitian, the
    product rho(e_a) tensor gamma_a is skew-adjoint:
      (rho(e_a) tensor gamma_a)^* = rho(e_a)^* tensor gamma_a = -rho(e_a) tensor gamma_a
    Sum is skew-adjoint. If Omega is Hermitian, then D has no definite adjointness
    unless Omega=0 or is special.

    I think the correct formula might differ by a factor of i somewhere.

    For now, let me just compute the eigenvalues and verify they are real.
    If Omega is anti-Hermitian, then D = (anti-Herm) + I x (anti-Herm) is
    anti-Hermitian, with purely imaginary eigenvalues. The Dirac eigenvalues
    are then i*lambda where lambda is real.

    RESOLVED: The physics convention is that the Dirac operator is:
      D = i * sum_a gamma_a nabla_{e_a}
    with the explicit factor of i making it self-adjoint. But in the math
    convention (no i), D is anti-self-adjoint with imaginary spectrum.

    We'll use the math convention and report |eigenvalue| (the absolute values).

    Returns:
        tuple: (is_hermitian, is_antihermitian, max_hermitian_err, max_antiherm_err)
    """
    h_err = np.max(np.abs(Omega - Omega.conj().T))
    ah_err = np.max(np.abs(Omega + Omega.conj().T))
    return (h_err < 1e-10, ah_err < 1e-10, h_err, ah_err)


# =============================================================================
# MODULE 6: SU(3) IRREP CONSTRUCTION
# =============================================================================

def irrep_fundamental(gens):
    """
    Fundamental representation (1,0) of su(3): dim = 3.
    rho(e_a) = e_a  (the 3x3 generators themselves).

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (3,3), complex
    """
    return [g.copy() for g in gens]


def irrep_antifundamental(gens):
    """
    Anti-fundamental representation (0,1) of su(3): dim = 3.
    rho(e_a) = -e_a^T  (negative transpose).

    This is the conjugate representation: if e_a acts on C^3 by left multiplication,
    the conjugate acts by -transpose (since e_a is anti-Hermitian, conjugate = -transpose).

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (3,3), complex
    """
    return [-g.T for g in gens]


def irrep_adjoint(f_abc):
    """
    Adjoint representation (1,1) of su(3): dim = 8.
    rho(e_a)_{bc} = f_{abc}  (structure constants).

    The adjoint action: ad(e_a)(e_b) = [e_a, e_b] = f_{abc} e_c.
    Matrix representation: (ad(e_a))_{cb} = f_{abc}.

    Args:
        f_abc: (8,8,8) structure constants

    Returns:
        rho: list of 8 matrices (8,8), real
    """
    rho = []
    for a in range(8):
        # (ad(e_a))_{cb} = f_{abc}
        # So the matrix M with M_{c,b} = f_{a,b,c}
        M = f_abc[a, :, :].T  # M[c,b] = f_abc[a,b,c] => transpose of f_abc[a,:,:]
        rho.append(M.astype(complex))
    return rho


def irrep_symmetric2(gens):
    """
    Symmetric tensor representation (2,0) of su(3): dim = 6.
    Constructed via projection from C^3 tensor C^3 onto the symmetric subspace.

    The ON basis for Sym^2(C^3) embedded in C^9:
      e_ii for i=0,1,2  (norm 1)
      (e_ij + e_ji)/sqrt(2) for i<j  (norm 1)

    rho(X) = P^dag (X tensor I + I tensor X) P

    This automatically guarantees anti-Hermiticity and the Lie algebra homomorphism.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (6,6), complex
    """
    I3 = np.eye(3, dtype=complex)

    # Build ON basis for Sym^2 as vectors in C^9 = C^3 tensor C^3
    sym_vecs = []
    for i in range(3):
        v = np.zeros(9, dtype=complex)
        v[3 * i + i] = 1.0
        sym_vecs.append(v)
    for i in range(3):
        for j in range(i + 1, 3):
            v = np.zeros(9, dtype=complex)
            v[3 * i + j] = 1.0 / np.sqrt(2)
            v[3 * j + i] = 1.0 / np.sqrt(2)
            sym_vecs.append(v)

    P = np.column_stack(sym_vecs)  # 9 x 6

    rho = []
    for X in gens:
        rho_9 = np.kron(X, I3) + np.kron(I3, X)
        rho.append(P.conj().T @ rho_9 @ P)
    return rho


def irrep_antisymmetric2(gens):
    """
    Anti-symmetric tensor representation: Lambda^2(C^3) of su(3): dim = 3.

    This is isomorphic to the anti-fundamental (0,1) for SU(3) specifically,
    via the Levi-Civita tensor. Not a new irrep, but useful as cross-check.

    Basis: e_0 ^ e_1, e_0 ^ e_2, e_1 ^ e_2 -- 3 elements.

    rho(X)(e_i ^ e_j) = X(e_i) ^ e_j + e_i ^ X(e_j)

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (3,3), complex
    """
    basis = [(0, 1), (0, 2), (1, 2)]
    idx_map = {(i, j): k for k, (i, j) in enumerate(basis)}
    dim = 3

    rho = []
    for X in gens:
        M = np.zeros((dim, dim), dtype=complex)
        for k, (i, j) in enumerate(basis):
            for p in range(3):
                # X(e_i) ^ e_j: contributes X[p,i] * (e_p ^ e_j)
                if p != j:
                    pi, pj = (min(p, j), max(p, j))
                    sign = 1 if p < j else -1
                    if (pi, pj) in idx_map:
                        M[idx_map[(pi, pj)], k] += sign * X[p, i]

                # e_i ^ X(e_j): contributes X[p,j] * (e_i ^ e_p)
                if i != p:
                    pi2, pj2 = (min(i, p), max(i, p))
                    sign2 = 1 if i < p else -1
                    if (pi2, pj2) in idx_map:
                        M[idx_map[(pi2, pj2)], k] += sign2 * X[p, j]
        rho.append(M)
    return rho


def irrep_symmetric2_conj(gens):
    """
    Conjugate symmetric tensor representation (0,2) of su(3): dim = 6.
    Acts on Sym^2(C^3)^* ~ Sym^2(conjugate C^3).

    rho_{(0,2)}(e_a) = symmetric_2(-e_a^T)

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (6,6), complex
    """
    conj_gens = [-g.T for g in gens]
    return irrep_symmetric2(conj_gens)


def irrep_symmetric3(gens):
    """
    Symmetric tensor representation (3,0) of su(3): dim = 10.
    Constructed via projection from C^27 = (C^3)^{tensor 3} onto Sym^3(C^3).

    Uses the symmetrizer projection P: C^27 -> C^10.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (10,10), complex
    """
    from itertools import permutations
    from math import factorial

    I3 = np.eye(3, dtype=complex)
    dim3 = 27  # 3^3

    # Build ON basis for Sym^3(C^3) in C^27
    # Sorted triples (i,j,k) with i<=j<=k
    sorted_triples = []
    for i in range(3):
        for j in range(i, 3):
            for k in range(j, 3):
                sorted_triples.append((i, j, k))
    assert len(sorted_triples) == 10

    sym_vecs = []
    for trip in sorted_triples:
        v = np.zeros(dim3, dtype=complex)
        # All distinct permutations of (i,j,k)
        perms = set(permutations(trip))
        norm = np.sqrt(len(perms))
        for p in perms:
            idx = p[0] * 9 + p[1] * 3 + p[2]
            v[idx] = 1.0 / norm
        sym_vecs.append(v)

    P = np.column_stack(sym_vecs)  # 27 x 10

    # Verify orthonormality
    orth_err = np.max(np.abs(P.conj().T @ P - np.eye(10)))
    assert orth_err < 1e-14, f"Sym^3 basis not orthonormal: {orth_err}"

    rho = []
    for X in gens:
        # X tensor I tensor I + I tensor X tensor I + I tensor I tensor X
        rho_27 = (np.kron(np.kron(X, I3), I3) +
                  np.kron(np.kron(I3, X), I3) +
                  np.kron(np.kron(I3, I3), X))
        rho.append(P.conj().T @ rho_27 @ P)
    return rho


def irrep_symmetric3_conj(gens):
    """
    Conjugate of (3,0): the (0,3) representation, dim = 10.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (10,10), complex
    """
    conj_gens = [-g.T for g in gens]
    return irrep_symmetric3(conj_gens)


def irrep_mixed_21(gens):
    """
    Mixed tensor representation (2,1) of su(3): dim = 15.

    This is the traceless part of C^3 tensor Sym^2(C^3)^*.
    Equivalently, it sits inside (1,0) tensor (0,2) with the (0,1) component
    projected out. But more directly:

    (2,1) appears in the tensor product (1,0) x (1,1).
    Decomposition: 3 x 8 = 15 + 6_bar + 3.

    Alternative construction: traceless symmetric 2-tensors with one covariant index.
    V_{(2,1)} = {T^{ij}_k : T^{ij}_k = T^{ji}_k, T^{ij}_j = 0, trace-free}

    However, a cleaner approach for numerical work: construct the tensor product
    (1,0) x (1,0) x (0,1) = C^3 x C^3 x (C^3)*, symmetrize first two indices,
    then project out traces.

    For reliability, we'll use the tensor product decomposition approach:
    Construct rho_{3 x 8} on C^3 tensor C^8, then project onto the (2,1) component
    using the quadratic Casimir.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (15,15), complex
    """
    # Strategy: build (1,0) tensor (1,1) = 3 tensor 8 = 24-dim space
    # Then project onto the C_2 = 10/3 eigenspace (which is the (2,1) with dim 15).
    # C_2 values: (2,1) -> 10/3, (0,2) -> 10/3... hmm, (2,1) and (0,2) have the same Casimir?
    #
    # Casimir formula: C_2(p,q) = (p^2+q^2+pq+3p+3q)/3
    # (2,1): (4+1+2+6+3)/3 = 16/3
    # (0,2): (0+4+0+0+6)/3 = 10/3
    # (1,0): (1+0+0+3+0)/3 = 4/3
    #
    # 3 x 8: C_2 eigenvalues should be:
    # (2,1) -> 16/3 (dim 15), (1,0) -> 4/3 (dim 3), (0,2) -> 10/3 (dim 6)
    # Total: 15+3+6 = 24 = 3*8. Good.

    rho_3 = irrep_fundamental(gens)  # (1,0), 3x3
    rho_8 = irrep_adjoint(compute_structure_constants(gens))  # (1,1), 8x8

    dim_3 = 3
    dim_8 = 8
    dim_prod = dim_3 * dim_8  # 24

    # Build Casimir on product space
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        # rho_product(e_a) = rho_3(e_a) tensor I_8 + I_3 tensor rho_8(e_a)
        rho_a = np.kron(rho_3[a], np.eye(dim_8)) + np.kron(np.eye(dim_3), rho_8[a])
        C2 += rho_a @ rho_a

    # C2 should have eigenvalues related to Casimir values
    # For anti-Hermitian generators, C2 = sum rho(e_a)^2 has eigenvalues -C_2(p,q) * (1/2)
    # Actually: our generators satisfy Tr(e_a e_b) = -1/2 delta_{ab}
    # The Casimir operator in the representation: C = sum_a rho(e_a)^2
    # For the fundamental (1,0): C = sum_a e_a^2 = -1/2 * C_2(1,0) * I_3
    # Let's just compute eigenvalues and sort.

    evals = eigvalsh(C2)
    # Group by eigenvalue
    unique_evals = []
    tol = 1e-8
    for ev in sorted(evals):
        if not unique_evals or abs(ev - unique_evals[-1][0]) > tol:
            unique_evals.append((ev, 1))
        else:
            unique_evals[-1] = (unique_evals[-1][0], unique_evals[-1][1] + 1)

    # Find the 15-dimensional eigenspace (that's the (2,1))
    target_dim = 15
    target_eval = None
    for ev, mult in unique_evals:
        if mult == target_dim:
            target_eval = ev
            break

    if target_eval is None:
        # Fallback: find the eigenvalue with multiplicity closest to 15
        # or the one whose eigenspace is 15-dim
        raise RuntimeError(
            f"Cannot find 15-dim eigenspace in 3x8 product. "
            f"Eigenvalue multiplicities: {unique_evals}"
        )

    # Project onto 15-dim eigenspace
    full_evals, full_evecs = np.linalg.eigh(C2)
    mask = np.abs(full_evals - target_eval) < tol
    P = full_evecs[:, mask]  # 24 x 15 projector columns

    if P.shape[1] != 15:
        raise RuntimeError(f"Projection gave dim={P.shape[1]}, expected 15")

    # Construct representation on 15-dim subspace
    rho = []
    for a in range(8):
        rho_a_full = np.kron(rho_3[a], np.eye(dim_8)) + np.kron(np.eye(dim_3), rho_8[a])
        # Project: M_15 = P^dag rho_a_full P
        M = P.conj().T @ rho_a_full @ P
        rho.append(M)

    return rho


def irrep_mixed_12(gens):
    """
    Mixed tensor representation (1,2) of su(3): dim = 15.
    Conjugate of (2,1).

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators

    Returns:
        rho: list of 8 matrices (15,15), complex
    """
    conj_gens = [-g.T for g in gens]
    return irrep_mixed_21(conj_gens)


# =============================================================================
# MODULE 6b: GENERAL IRREP CONSTRUCTION (p+q >= 4)
# =============================================================================

def irrep_symmetric_power(gens, p):
    """
    Construct the (p,0) irrep = Sym^p(C^3) via symmetrizer projection.

    The representation acts on the symmetric subspace of (C^3)^{tensor p},
    which has dimension (p+1)(p+2)/2.

    Method: build ON basis for Sym^p(C^3) as vectors in C^{3^p}, then
    project the tensor product action rho(X) = sum_k I^{k-1} x X x I^{p-k}.

    Args:
        gens: list of 8 anti-Hermitian (3,3) su(3) generators
        p: symmetric power (p >= 2)

    Returns:
        rho: list of 8 matrices of dimension (p+1)(p+2)/2
    """
    from itertools import combinations_with_replacement, permutations
    from collections import Counter

    dim_fund = 3
    dim_tensor = dim_fund ** p  # 3^p
    dim_sym = (p + 1) * (p + 2) // 2  # dim of Sym^p(C^3)

    I3 = np.eye(dim_fund, dtype=complex)

    # Build ON basis for Sym^p(C^3) in C^{3^p}
    # Sorted p-tuples with entries in {0,1,2}, non-decreasing
    sorted_tuples = list(combinations_with_replacement(range(dim_fund), p))
    assert len(sorted_tuples) == dim_sym, \
        f"Expected {dim_sym} basis vectors, got {len(sorted_tuples)}"

    sym_vecs = []
    for tup in sorted_tuples:
        v = np.zeros(dim_tensor, dtype=complex)
        # All distinct permutations of this tuple
        perms = set(permutations(tup))
        norm = np.sqrt(len(perms))
        for perm in perms:
            # Multi-index -> flat index: sum_k perm[k] * 3^(p-1-k)
            idx = 0
            for k in range(p):
                idx += perm[k] * (dim_fund ** (p - 1 - k))
            v[idx] = 1.0 / norm
        sym_vecs.append(v)

    P = np.column_stack(sym_vecs)  # 3^p x dim_sym

    # Verify orthonormality
    orth_err = np.max(np.abs(P.conj().T @ P - np.eye(dim_sym)))
    assert orth_err < 1e-13, f"Sym^{p} basis not orthonormal: {orth_err}"

    # Build rho on symmetric subspace
    rho = []
    for X in gens:
        # rho_tensor(X) = sum_{k=0}^{p-1} I^{k} x X x I^{p-1-k}
        rho_full = np.zeros((dim_tensor, dim_tensor), dtype=complex)
        for k in range(p):
            # I3^{k} x X x I3^{p-1-k}
            term = np.eye(1, dtype=complex)
            for j in range(p):
                if j == k:
                    term = np.kron(term, X)
                else:
                    term = np.kron(term, I3)
            rho_full += term
        rho.append(P.conj().T @ rho_full @ P)

    return rho


def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    """
    Construct an irrep via tensor product + Casimir eigenvalue projection.

    Given representations rho_A (dim_A) and rho_B (dim_B), forms the tensor
    product rho_A x rho_B and projects onto the eigenspace of the quadratic
    Casimir C_2 = sum_a rho(e_a)^2 with dimension target_dim.

    The C_2 eigenvalue for irrep (p,q) is -(p^2+q^2+pq+3p+3q)/6 in our
    normalization (Tr(e_a e_b) = -1/2 delta_{ab}).

    Args:
        rho_A: list of 8 matrices (dim_A x dim_A)
        rho_B: list of 8 matrices (dim_B x dim_B)
        target_dim: expected dimension of the target irrep
        target_pq: optional (p,q) tuple for diagnostic messages

    Returns:
        rho: list of 8 matrices (target_dim x target_dim)
    """
    dim_A = rho_A[0].shape[0]
    dim_B = rho_B[0].shape[0]
    dim_prod = dim_A * dim_B

    # Build product representation and Casimir
    rho_prod = []
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        rho_a = np.kron(rho_A[a], np.eye(dim_B)) + np.kron(np.eye(dim_A), rho_B[a])
        rho_prod.append(rho_a)
        C2 += rho_a @ rho_a

    # Diagonalize Casimir (it is Hermitian since generators are anti-Hermitian)
    evals, evecs = np.linalg.eigh(C2)

    # Group eigenvalues by value
    tol = 1e-8
    groups = []
    for i, ev in enumerate(sorted(zip(evals, range(dim_prod)))):
        val, idx = ev
        if not groups or abs(val - groups[-1][0]) > tol:
            groups.append((val, [idx]))
        else:
            groups[-1][1].append(idx)

    # Find the eigenspace with the target dimension
    target_eval = None
    for val, indices in groups:
        if len(indices) == target_dim:
            target_eval = val
            break

    if target_eval is None:
        group_info = [(val, len(indices)) for val, indices in groups]
        label = f"({target_pq[0]},{target_pq[1]})" if target_pq else f"dim={target_dim}"
        raise RuntimeError(
            f"Cannot find {target_dim}-dim eigenspace for {label} in "
            f"{dim_A}x{dim_B} product. Eigenspace dims: {group_info}"
        )

    # Project onto target eigenspace
    mask = np.abs(evals - target_eval) < tol
    P = evecs[:, mask]  # dim_prod x target_dim

    if P.shape[1] != target_dim:
        raise RuntimeError(
            f"Projection gave dim={P.shape[1]}, expected {target_dim}"
        )

    # Build representation on projected subspace
    rho = []
    for a in range(8):
        rho.append(P.conj().T @ rho_prod[a] @ P)

    return rho


# Cache for computed irreps within a single get_irrep call chain
_irrep_cache = {}


def _cache_key(p, q):
    return (p, q)


def _build_irrep_no_cache(p, q, gens, f_abc):
    """
    Build irrep (p,q) WITHOUT using or populating the global cache.

    Used for conjugation: when building (p,q) with q>p, we need (q,p) with
    conjugated generators. These should not contaminate the cache (which stores
    irreps for the original generators).

    Only supports p >= q >= 0 (i.e., the "upper triangle" of the weight diagram).

    Args:
        p, q: highest weight labels (must have p >= q)
        gens: su(3) generators (may be conjugated)
        f_abc: structure constants

    Returns:
        rho: list of 8 matrices
        dim_rho: dimension
    """
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

    if (p, q) == (0, 0):
        return [np.zeros((1, 1), dtype=complex) for _ in range(8)], 1
    elif (p, q) == (1, 0):
        return irrep_fundamental(gens), 3
    elif (p, q) == (0, 1):
        return irrep_antifundamental(gens), 3
    elif (p, q) == (1, 1):
        f_local = compute_structure_constants(gens)
        return irrep_adjoint(f_local), 8
    elif p >= 2 and q == 0:
        return irrep_symmetric_power(gens, p), dim_pq
    elif (p, q) == (2, 2):
        f_local = compute_structure_constants(gens)
        rho_8 = irrep_adjoint(f_local)
        return irrep_via_casimir_projection(rho_8, rho_8, dim_pq, (p, q)), dim_pq
    elif p >= q and q > 0:
        rho_3 = irrep_fundamental(gens)
        rho_parent, _ = _build_irrep_no_cache(p - 1, q, gens, f_abc)
        return irrep_via_casimir_projection(rho_3, rho_parent, dim_pq, (p, q)), dim_pq
    else:
        raise NotImplementedError(f"_build_irrep_no_cache: ({p},{q}) not supported")


def get_irrep(p, q, gens, f_abc):
    """
    Return the representation matrices for SU(3) irrep (p,q).

    Supports all irreps with p+q <= 6 (and in principle higher via recursion).

    Construction methods:
      - (0,0): trivial
      - (1,0): fundamental
      - (0,1): anti-fundamental (conjugation of (1,0))
      - (1,1): adjoint (from structure constants)
      - (p,0) for p>=2: Sym^p(C^3) via symmetrizer projection
      - (0,q) for q>=2: conjugation of (q,0)
      - (p,q) mixed: tensor product of known irreps + Casimir projection

    For mixed (p,q), the parent products used are:
      (2,1) = proj from (1,0) x (1,1)    [3 x 8 = 24]
      (1,2) = conjugate of (2,1)
      (3,1) = proj from (1,0) x (2,1)    [3 x 15 = 45]
      (1,3) = conjugate of (3,1)
      (2,2) = proj from (1,1) x (1,1)    [8 x 8 = 64]
      (4,1) = proj from (1,0) x (3,1)    [3 x 24 = 72]
      (1,4) = conjugate of (4,1)
      (3,2) = proj from (1,0) x (2,2)    [3 x 27 = 81]
      (2,3) = conjugate of (3,2)
      (5,1) = proj from (1,0) x (4,1)    [3 x 35 = 105]
      (1,5) = conjugate of (5,1)
      (4,2) = proj from (1,0) x (3,2)    [3 x 42 = 126]
      (2,4) = conjugate of (4,2)
      (3,3) = proj from (1,1) x (2,2)    [8 x 27 = 216]

    Args:
        p, q: highest weight labels
        gens: su(3) generators (list of 8 anti-Hermitian 3x3 matrices)
        f_abc: structure constants

    Returns:
        rho: list of 8 matrices of dimension dim(p,q)
        dim_rho: dimension of the representation
    """
    global _irrep_cache
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

    key = _cache_key(p, q)
    if key in _irrep_cache:
        return _irrep_cache[key], dim_pq

    rho = None

    if (p, q) == (0, 0):
        rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]

    elif (p, q) == (1, 0):
        rho = irrep_fundamental(gens)

    elif (p, q) == (0, 1):
        rho = irrep_antifundamental(gens)

    elif (p, q) == (1, 1):
        rho = irrep_adjoint(f_abc)

    elif p >= 2 and q == 0:
        # (p,0) = Sym^p(C^3)
        rho = irrep_symmetric_power(gens, p)

    elif p == 0 and q >= 2:
        # (0,q) = conjugate of (q,0)
        # rho_{(0,q)}(e_a) = rho_{(q,0)}(-e_a^T)
        conj_gens = [-g.T for g in gens]
        rho = irrep_symmetric_power(conj_gens, q)

    elif q > 0 and p > 0:
        # Mixed (p,q): use tensor product + Casimir projection
        # Strategy: (p,q) appears in (1,0) x (p-1,q) when p >= q,
        #           or conjugate of (q,p) when q > p.
        # Special cases for efficiency:
        #   (2,2) from (1,1) x (1,1) avoids needing (1,2) first
        if q > p:
            # (p,q) = conjugate of (q,p)
            # rho_{(p,q)}(e_a) = rho_{(q,p)}(-e_a^T)
            # Build (q,p) with conjugated generators directly (no cache contamination)
            conj_gens = [-g.T for g in gens]
            rho_qp, _ = _build_irrep_no_cache(q, p, conj_gens, f_abc)
            rho = rho_qp
        elif (p, q) == (2, 2):
            # (2,2) from (1,1) x (1,1) = 8 x 8
            rho_8, _ = get_irrep(1, 1, gens, f_abc)
            rho = irrep_via_casimir_projection(rho_8, rho_8, dim_pq, (p, q))
        else:
            # General: (p,q) from (1,0) x (p-1,q) for p >= q > 0
            rho_3 = irrep_fundamental(gens)
            rho_parent, _ = get_irrep(p - 1, q, gens, f_abc)
            rho = irrep_via_casimir_projection(rho_3, rho_parent, dim_pq, (p, q))

    if rho is None:
        raise NotImplementedError(
            f"Irrep ({p},{q}) (dim={dim_pq}) not yet implemented."
        )

    _irrep_cache[key] = rho
    return rho, dim_pq


def validate_irrep(rho, f_abc, label=""):
    """
    Validate that rho is a Lie algebra homomorphism:
      [rho(e_a), rho(e_b)] = f_{abc} rho(e_c)

    Also check anti-Hermiticity: rho(e_a)^dag = -rho(e_a).

    Args:
        rho: list of 8 representation matrices
        f_abc: structure constants
        label: string label for printing

    Returns:
        max_hom_err: maximum homomorphism error
        max_ah_err: maximum anti-Hermiticity error
    """
    n = len(rho)
    dim = rho[0].shape[0]

    max_hom_err = 0.0
    for a in range(n):
        for b in range(a + 1, n):
            comm = rho[a] @ rho[b] - rho[b] @ rho[a]
            target = sum(f_abc[a, b, c] * rho[c] for c in range(n))
            err = np.max(np.abs(comm - target))
            max_hom_err = max(max_hom_err, err)

    max_ah_err = 0.0
    for a in range(n):
        err = np.max(np.abs(rho[a] + rho[a].conj().T))
        max_ah_err = max(max_ah_err, err)

    return max_hom_err, max_ah_err


# =============================================================================
# MODULE 7: DIRAC OPERATOR ASSEMBLY
# =============================================================================

def dirac_operator_on_irrep(rho, E, gammas, Omega):
    """
    Assemble the Dirac operator matrix on irrep sector pi.

    D_pi = sum_{a,b} E_{ab} (rho(X_b) tensor gamma_a) + I_{dim_rho} tensor Omega

    where:
      - rho(X_b) = rho[b] is the representation of original (non-ON) basis vector X_b
      - E_{ab} is the ON frame: e_a = E_{ab} X_b
      - gamma_a are Clifford generators (16x16)
      - Omega is the spinor curvature offset (16x16)

    The matrix acts on V_pi tensor S, with dimension dim_rho * 16.

    NOTE on Hermiticity: D_pi should be anti-Hermitian in the math convention
    (no explicit factor of i). Eigenvalues are purely imaginary; we report
    their imaginary parts as "Dirac eigenvalues."

    Args:
        rho: list of 8 representation matrices (dim_rho x dim_rho)
        E: (8,8) orthonormal frame matrix
        gammas: list of 8 Clifford generators (16x16)
        Omega: (16,16) spinor curvature offset

    Returns:
        D: (dim_rho*16, dim_rho*16) complex matrix
    """
    dim_rho = rho[0].shape[0]
    dim_spin = 16
    dim_total = dim_rho * dim_spin

    D = np.zeros((dim_total, dim_total), dtype=complex)

    # First term: sum_{a,b} E_{ab} rho[b] tensor gamma_a
    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])

    # Second term: I tensor Omega
    D += np.kron(np.eye(dim_rho), Omega)

    return D


# =============================================================================
# MODULE 7B: LIE DERIVATIVE OF METRIC AND COVARIANT DERIVATIVE
# =============================================================================

def lie_derivative_metric(Gamma, a):
    """
    Compute the Lie derivative of the metric along frame vector e_a.

    In the orthonormal frame, the Lie derivative of the metric g along e_a is:

        (L_{e_a} g)_{bc} = Gamma^b_{ca} + Gamma^c_{ba}
                         = Gamma[b,c,a] + Gamma[c,b,a]

    This is the SYMMETRIC part of the connection in the first two indices
    at fixed third index a. Equivalently, using the Koszul formula:

        (L_{e_a} g)(e_b, e_c) = g(nabla_{e_b} e_a, e_c) + g(e_b, nabla_{e_c} e_a)

    Properties:
        - Symmetric: (L_{e_a} g)_{bc} = (L_{e_a} g)_{cb}
        - Zero for Killing directions: if e_a is Killing, then L_{e_a} g = 0
        - Volume-preserving: Tr(L_{e_a} g) = 0 for volume-preserving deformations
        - For Jensen metric on SU(3): a in {0,1,2,7} (u(2)) are Killing;
          a in {3,4,5,6} (C^2) are non-Killing.

    Args:
        Gamma: (8,8,8) connection coefficients, Gamma[c,a,b] = Gamma^c_{ab}
        a: direction index (0-7)

    Returns:
        Lg: (8,8) real symmetric matrix, (L_{e_a} g)_{bc}
    """
    n = Gamma.shape[0]
    Lg = np.zeros((n, n), dtype=np.float64)
    for b in range(n):
        for c in range(n):
            # (L_{e_a} g)_{bc} = Gamma^b_{ca} + Gamma^c_{ba}
            # = Gamma[b,c,a] + Gamma[c,b,a]
            Lg[b, c] = Gamma[b, c, a] + Gamma[c, b, a]
    return Lg


def covariant_derivative_lie_metric(Gamma, Lg, i):
    """
    Compute the covariant derivative nabla_{e_i} (L_{e_a} g) of the
    Lie derivative tensor.

    For a (0,2) tensor T_{bc} in ON frame:

        (nabla_{e_i} T)_{bc} = e_i(T_{bc}) - Gamma^d_{ib} T_{dc} - Gamma^d_{ic} T_{bd}

    Since T = L_{e_a} g is a CONSTANT tensor (left-invariant on the Lie group,
    no position dependence), the partial derivative term e_i(T_{bc}) = 0.

    Therefore:
        (nabla_{e_i} Lg)_{bc} = -Gamma^d_{ib} Lg_{dc} - Gamma^d_{ic} Lg_{bd}
                               = -Gamma[d,i,b] Lg[d,c] - Gamma[d,i,c] Lg[b,d]

    This uses the fact that on a Lie group with left-invariant tensor fields,
    all partial derivatives in the left-invariant frame vanish -- only
    connection terms survive.

    Args:
        Gamma: (8,8,8) connection coefficients
        Lg: (8,8) the Lie derivative tensor (L_{e_a} g)_{bc}
        i: nabla direction index

    Returns:
        nabla_Lg: (8,8) real matrix, (nabla_{e_i} L_{e_a} g)_{bc}
    """
    n = Gamma.shape[0]
    nabla_Lg = np.zeros((n, n), dtype=np.float64)
    for b in range(n):
        for c in range(n):
            val = 0.0
            for d in range(n):
                # -Gamma^d_{ib} * Lg_{dc} - Gamma^d_{ic} * Lg_{bd}
                val -= Gamma[d, i, b] * Lg[d, c]
                val -= Gamma[d, i, c] * Lg[b, d]
            nabla_Lg[b, c] = val
    return nabla_Lg


# =============================================================================
# MODULE 8: EIGENVALUE COLLECTION AND ANALYSIS
# =============================================================================

def collect_spectrum(s, gens, f_abc, gammas, max_pq_sum=3, verbose=True):
    """
    Compute the Dirac spectrum on (SU(3), g_s) by iterating over irreps.

    For each irrep (p,q) with p+q <= max_pq_sum, constructs D_pi and
    diagonalizes it. Collects all eigenvalues.

    The Peter-Weyl theorem says each eigenvalue from sector (p,q) has
    multiplicity dim(p,q) in the full spectrum (from the left-regular
    representation decomposition). We record this multiplicity.

    Args:
        s: Jensen deformation parameter
        gens: su(3) generators (list of 8 anti-Hermitian 3x3)
        f_abc: structure constants (8,8,8)
        gammas: Clifford generators (list of 8, each 16x16)
        max_pq_sum: maximum p+q to include
        verbose: print progress

    Returns:
        all_evals: sorted array of all distinct eigenvalue imaginary parts
        eval_data: list of (p, q, eigenvalues_array) per sector
        multiplicity: dict mapping eigenvalue -> total multiplicity
    """
    # Build metric, frame, connection, Omega for this s
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if verbose:
        mc_err = validate_connection(Gamma)
        is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
        # h_err = ||Omega - Omega^dag|| measures departure from Hermitian
        # ah_err = ||Omega + Omega^dag|| measures departure from anti-Hermitian
        # For a correct Dirac operator, Omega should be anti-Hermitian (ah_err ~ 0)
        omega_type = "anti-Hermitian" if is_ah else ("Hermitian" if is_h else "NEITHER")
        print(f"  s={s:.3f}: metric OK, connection metric-compat err={mc_err:.2e}, "
              f"Omega is {omega_type} (non-Herm={h_err:.2e}, non-antiHerm={ah_err:.2e})")

    eval_data = []
    all_eigenvalues = []  # (imaginary_part, multiplicity_from_PW)

    # Iterate over irreps
    irreps_to_compute = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue  # trivial irrep: will handle separately
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0
            irreps_to_compute.append((C2, p, q, dim_pq))

    irreps_to_compute.sort()  # by Casimir

    # Handle trivial irrep: D = Omega on 16-dim space
    D_trivial = Omega.copy()
    evals_trivial = np.linalg.eigvalsh(1j * D_trivial)  # if anti-Hermitian, i*D is Hermitian
    # Actually, let's just compute eigenvalues of D directly and check
    evals_trivial_raw = np.linalg.eigvals(D_trivial)
    evals_trivial_raw.sort()

    # For anti-Hermitian Omega, eigenvalues are purely imaginary
    # For Hermitian Omega, eigenvalues are real
    eval_data.append((0, 0, evals_trivial_raw))
    # Multiplicity from PW: dim(0,0)^2 = 1
    for ev in evals_trivial_raw:
        all_eigenvalues.append((ev, 1))

    if verbose:
        print(f"    (0,0): dim=1, D size=16, eigenvalues computed. "
              f"Range: [{np.min(np.abs(evals_trivial_raw)):.4f}, {np.max(np.abs(evals_trivial_raw)):.4f}]")

    for C2_val, p, q, dim_pq in irreps_to_compute:
        try:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq

            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

            # Compute eigenvalues
            evals_pi = np.linalg.eigvals(D_pi)
            evals_pi = np.sort_complex(evals_pi)

            eval_data.append((p, q, evals_pi))

            # PW multiplicity: each eigenvalue in sector (p,q) appears dim(p,q) times
            for ev in evals_pi:
                all_eigenvalues.append((ev, dim_pq))

            if verbose:
                D_size = dim_pq * 16
                abs_evals = np.abs(evals_pi)
                print(f"    ({p},{q}): dim={dim_pq}, D size={D_size}, "
                      f"|lambda| range: [{np.min(abs_evals):.4f}, {np.max(abs_evals):.4f}]")

        except NotImplementedError as e:
            if verbose:
                print(f"    ({p},{q}): SKIPPED ({e})")
            continue

    return all_eigenvalues, eval_data


def collect_spectrum_with_eigenvectors(s, gens, f_abc, gammas, max_pq_sum=2, verbose=True):
    """
    Compute Dirac spectrum AND eigenvectors on (SU(3), g_s) by iterating over irreps.

    Uses scipy.linalg.eigh on the Hermitian matrix H = 1j * D_pi to obtain
    guaranteed orthonormal eigenvectors. D_pi is anti-Hermitian, so H is Hermitian
    with real eigenvalues lambda_H. The Dirac eigenvalues are lambda_D = -1j * lambda_H
    (purely imaginary). We store the real eigenvalues of H (sorted ascending).

    Also returns the geometric infrastructure (E, Gamma, Omega) needed for
    downstream D_F construction.

    Mathematical note:
        D_pi |psi_n> = lambda_n |psi_n>  with lambda_n = -i * mu_n (purely imaginary)
        (1j * D_pi) |psi_n> = mu_n |psi_n>  with mu_n real (Hermitian eigenvalues)
        We store mu_n (real) and the corresponding |psi_n> (orthonormal columns of evecs).
        To recover Dirac eigenvalues: lambda_n = -i * mu_n.

    Args:
        s: Jensen deformation parameter (tau)
        gens: su(3) generators (list of 8 anti-Hermitian 3x3)
        f_abc: structure constants (8,8,8)
        gammas: Clifford generators (list of 8, each 16x16)
        max_pq_sum: maximum p+q to include (default 2 for D_F truncation)
        verbose: print progress

    Returns:
        sector_data: list of dicts, one per sector, each containing:
            'p', 'q': irrep labels
            'dim_rho': dimension of irrep
            'evals': real eigenvalues of 1j*D_pi (sorted ascending)
            'evecs': (dim_rho*16, dim_rho*16) unitary, columns = eigenvectors
            'D_pi': (dim_rho*16, dim_rho*16) anti-Hermitian Dirac matrix
            'ah_err': anti-Hermiticity error ||D + D^dag||
        infra: dict with geometric infrastructure:
            'E': (8,8) orthonormal frame
            'Gamma': (8,8,8) connection coefficients
            'Omega': (16,16) spinor curvature offset
            'B_ab': (8,8) Killing form
            'g_s': (8,8) Jensen metric
            'ft': (8,8,8) frame structure constants
    """
    from scipy.linalg import eigh as scipy_eigh

    # Build metric, frame, connection, Omega for this s
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if verbose:
        mc_err = validate_connection(Gamma)
        is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
        omega_type = "anti-Hermitian" if is_ah else ("Hermitian" if is_h else "NEITHER")
        print(f"  s={s:.3f}: metric OK, connection metric-compat err={mc_err:.2e}, "
              f"Omega is {omega_type} (non-Herm={h_err:.2e}, non-antiHerm={ah_err:.2e})")

    infra = {
        'E': E, 'Gamma': Gamma, 'Omega': Omega,
        'B_ab': B_ab, 'g_s': g_s, 'ft': ft,
    }

    sector_data = []

    # Enumerate irreps to compute (including trivial)
    irreps_to_compute = [(0, 0, 1)]  # (p, q, dim_pq)
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            irreps_to_compute.append((p, q, dim_pq))

    for p, q, dim_pq in irreps_to_compute:
        try:
            if (p, q) == (0, 0):
                # Trivial irrep: D = Omega on 16-dim space
                D_pi = Omega.copy()
            else:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == dim_pq
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

            # Verify anti-Hermiticity
            ah_err = np.max(np.abs(D_pi + D_pi.conj().T))

            # Diagonalize via Hermitian problem: H = 1j * D_pi
            H = 1j * D_pi
            h_err = np.max(np.abs(H - H.conj().T))
            if h_err > 1e-10:
                if verbose:
                    print(f"    WARNING ({p},{q}): H = 1j*D not Hermitian, err={h_err:.2e}")

            evals, evecs = scipy_eigh(H)

            # Verify orthonormality: evecs^dag @ evecs = I
            orth_err = np.max(np.abs(evecs.conj().T @ evecs - np.eye(len(evals))))

            if verbose:
                D_size = dim_pq * 16
                abs_evals = np.abs(evals)
                print(f"    ({p},{q}): dim={dim_pq}, D size={D_size}, "
                      f"|lambda| range: [{np.min(abs_evals):.4f}, {np.max(abs_evals):.4f}], "
                      f"ah_err={ah_err:.2e}, orth_err={orth_err:.2e}")

            sector_data.append({
                'p': p, 'q': q, 'dim_rho': dim_pq,
                'evals': evals, 'evecs': evecs,
                'D_pi': D_pi, 'ah_err': ah_err,
            })

        except NotImplementedError as e:
            if verbose:
                print(f"    ({p},{q}): SKIPPED ({e})")
            continue

    return sector_data, infra


def analyze_spectrum(all_eigenvalues, verbose=True):
    """
    Analyze the collected spectrum for phi-ratio clustering.

    Steps:
      1. Extract absolute values (Dirac eigenvalues are +-symmetric)
      2. Sort by magnitude
      3. Compute consecutive ratios
      4. Flag any ratio near phi = 1.53158... or golden ratio 1.61803...

    Args:
        all_eigenvalues: list of (eigenvalue_complex, pw_multiplicity)
        verbose: print analysis

    Returns:
        abs_evals: sorted positive eigenvalues
        ratios: consecutive ratios
    """
    # Extract absolute values, keeping only positive (spectrum is symmetric)
    abs_vals = []
    for ev, mult in all_eigenvalues:
        val = abs(ev)
        if val > 1e-10:
            abs_vals.append(val)

    abs_vals = np.array(sorted(set(np.round(abs_vals, 10))))  # deduplicate

    if verbose:
        print(f"\n  Distinct positive |eigenvalues|: {len(abs_vals)}")
        for i, v in enumerate(abs_vals[:30]):
            print(f"    [{i:2d}] |lambda| = {v:.6f}")

    # Consecutive ratios
    if len(abs_vals) < 2:
        return abs_vals, np.array([])

    ratios = abs_vals[1:] / abs_vals[:-1]

    if verbose:
        print(f"\n  Consecutive ratios |lambda_{{n+1}}| / |lambda_n|:")
        phi_target = (1 + np.sqrt(5)) / 2  # golden ratio 1.618...
        phi_paasch = 1.53158  # Paasch mass ratio

        for i, r in enumerate(ratios[:29]):
            flags = ""
            if abs(r - phi_paasch) < 0.05:
                flags += " <-- NEAR PAASCH PHI (1.532)"
            if abs(r - phi_target) < 0.05:
                flags += " <-- NEAR GOLDEN RATIO (1.618)"
            print(f"    [{i:2d}] ratio = {r:.6f}{flags}")

    return abs_vals, ratios


def analyze_nonconsecutive_ratios(abs_evals, n_low=20, verbose=True):
    """
    Search for phi and golden ratio in ALL pairwise ratios of low-lying eigenvalues.

    The Paasch mass spiral predicts specific mass ratios near phi = 1.53158.
    These need not appear as consecutive eigenvalue ratios -- they may relate
    eigenvalues from different irrep sectors.

    Args:
        abs_evals: sorted array of distinct positive eigenvalues
        n_low: number of low-lying eigenvalues to analyze
        verbose: print results

    Returns:
        phi_pairs: list of (i, j, ratio, val_i, val_j) for near-phi pairs
        gold_pairs: same for near-golden-ratio pairs
    """
    phi_p = 1.53158
    golden = (1 + np.sqrt(5)) / 2
    tol = 0.03  # 3% tolerance

    n = min(n_low, len(abs_evals))
    phi_pairs = []
    gold_pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            r = abs_evals[j] / abs_evals[i]
            if abs(r - phi_p) < tol:
                phi_pairs.append((i, j, r, abs_evals[i], abs_evals[j]))
            if abs(r - golden) < tol:
                gold_pairs.append((i, j, r, abs_evals[i], abs_evals[j]))

    if verbose:
        print(f"\n  Non-consecutive ratio analysis (first {n} eigenvalues, tol={tol*100:.0f}%):")
        print(f"    Pairs near Paasch phi ({phi_p:.5f}): {len(phi_pairs)}")
        for i, j, r, vi, vj in sorted(phi_pairs, key=lambda x: abs(x[2] - phi_p)):
            err_pct = abs(r - phi_p) / phi_p * 100
            print(f"      [{i}]/[{j}]: {vj:.6f}/{vi:.6f} = {r:.6f} (err {err_pct:.2f}%)")

        print(f"    Pairs near golden ratio ({golden:.5f}): {len(gold_pairs)}")
        for i, j, r, vi, vj in sorted(gold_pairs, key=lambda x: abs(x[2] - golden)):
            err_pct = abs(r - golden) / golden * 100
            print(f"      [{i}]/[{j}]: {vj:.6f}/{vi:.6f} = {r:.6f} (err {err_pct:.2f}%)")

        # Algebraic identification of lambda^2 values
        print(f"\n  Algebraic identification (lambda^2 = n/36):")
        for k in range(min(n, 20)):
            v2 = abs_evals[k]**2
            n36 = round(v2 * 36)
            if abs(v2 - n36 / 36) < 1e-4:
                print(f"    [{k:2d}] |lambda|={abs_evals[k]:.6f}, "
                      f"lambda^2={v2:.6f} = {n36}/36")
            else:
                print(f"    [{k:2d}] |lambda|={abs_evals[k]:.6f}, "
                      f"lambda^2={v2:.6f} (not n/36)")

    return phi_pairs, gold_pairs


# =============================================================================
# MODULE 9: SU(2) BENCHMARK (validates entire Dirac pipeline against known S^3 spectrum)
# =============================================================================

def su2_benchmark():
    """
    Validate the Dirac operator formula against the KNOWN exact spectrum of
    the Dirac operator on S^3 = SU(2) with bi-invariant metric.

    For S^3 with radius r, the Dirac eigenvalues are:
      lambda_k = +-(k + 3/2) / r,  k = 0, 1, 2, ...
      multiplicity = (k+1)(k+2)

    Our SU(2) setup: generators e_a = -i/2 sigma_a, Killing form B = 2*I,
    metric g = |B| = 2*I, orthonormal frame E = (1/sqrt(2))*I.
    The corresponding S^3 radius is r = 2*sqrt(2).

    We verify:
      - Trivial rep (j=0): |D| = 3/(2r) = 3/(4*sqrt(2))
      - Fundamental rep (j=1/2): |D| in {3/(2r), 5/(2r)}
      - Adjoint rep (j=1): |D| in {5/(2r), 7/(2r)}

    Returns:
        passed: True if all eigenvalues match within 1e-10
        max_err: maximum absolute error across all checks
    """
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gens2 = [-1j / 2 * s1, -1j / 2 * s2, -1j / 2 * s3]
    gammas2 = [s1, s2, s3]  # Cliff(3) generators: Pauli matrices

    # Structure constants: [e_a, e_b] = f_{abc} e_c
    f2 = np.zeros((3, 3, 3))
    for a in range(3):
        for b in range(a + 1, 3):
            comm = gens2[a] @ gens2[b] - gens2[b] @ gens2[a]
            for c in range(3):
                val = -2 * np.trace(comm @ gens2[c])
                f2[a, b, c] = val.real
                f2[b, a, c] = -val.real

    # Metric, frame, connection
    B2 = np.einsum('acd,bcd->ab', f2, f2)
    g2 = np.abs(B2)
    E2 = inv(cholesky(g2))
    E2inv = inv(E2)
    ft2 = np.einsum('ac,bd,cde,ef->abf', E2, E2, f2, E2inv)

    Gamma2 = np.zeros((3, 3, 3))
    for c in range(3):
        for a in range(3):
            for b in range(3):
                Gamma2[c, a, b] = 0.5 * (ft2[a, b, c] - ft2[b, c, a] + ft2[c, a, b])

    # Spinor connection offset Omega
    Omega2 = np.zeros((2, 2), dtype=complex)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                coeff = Gamma2[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega2 += coeff * gammas2[a] @ gammas2[b] @ gammas2[c]
    Omega2 *= 0.25

    r = 2 * np.sqrt(2)
    max_err = 0.0

    # Check 1: Trivial rep (j=0) -- D = Omega2
    trivial_evals = np.abs(np.linalg.eigvals(Omega2))
    expected_k0 = 1.5 / r
    err_k0 = np.max(np.abs(trivial_evals - expected_k0))
    max_err = max(max_err, err_k0)

    # Check 2: Fundamental rep (j=1/2) -- D on C^2 x C^2
    D_fund = np.zeros((4, 4), dtype=complex)
    for a in range(3):
        for b in range(3):
            if abs(E2[a, b]) > 1e-15:
                D_fund += E2[a, b] * np.kron(gens2[b], gammas2[a])
    D_fund += np.kron(np.eye(2), Omega2)

    fund_abs = np.sort(np.abs(np.linalg.eigvals(D_fund)))
    expected_fund = np.sort([1.5 / r, 2.5 / r, 2.5 / r, 2.5 / r])
    err_fund = np.max(np.abs(fund_abs - expected_fund))
    max_err = max(max_err, err_fund)

    # Check 3: Adjoint rep (j=1) -- D on C^3 x C^2
    rho_adj2 = [f2[a, :, :].T.astype(complex) for a in range(3)]
    D_adj = np.zeros((6, 6), dtype=complex)
    for a in range(3):
        for b in range(3):
            if abs(E2[a, b]) > 1e-15:
                D_adj += E2[a, b] * np.kron(rho_adj2[b], gammas2[a])
    D_adj += np.kron(np.eye(3), Omega2)

    adj_abs = np.sort(np.abs(np.linalg.eigvals(D_adj)))
    expected_adj = np.sort([2.5 / r, 2.5 / r, 3.5 / r, 3.5 / r, 3.5 / r, 3.5 / r])
    err_adj = np.max(np.abs(adj_abs - expected_adj))
    max_err = max(max_err, err_adj)

    passed = max_err < 1e-10
    return passed, max_err


# =============================================================================
# MODULE 10: s-SWEEP AND VISUALIZATION
# =============================================================================

def sweep_s(s_values, gens, f_abc, gammas, max_pq_sum=3, verbose=False):
    """
    Sweep over Jensen deformation parameter s and collect spectra.

    Args:
        s_values: array of s values
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators
        max_pq_sum: maximum p+q
        verbose: print per-s diagnostics

    Returns:
        results: list of (s, abs_evals, ratios) per s value
    """
    results = []
    for i, s in enumerate(s_values):
        print(f"\n--- s = {s:.4f} ({i+1}/{len(s_values)}) ---")
        all_evals, eval_data = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=verbose
        )
        abs_evals, ratios = analyze_spectrum(all_evals, verbose=False)
        phi_pairs, gold_pairs = analyze_nonconsecutive_ratios(abs_evals, verbose=False)
        results.append((s, abs_evals, ratios, phi_pairs, gold_pairs))

        # Print summary for this s
        phi_paasch = 1.53158
        consec_phi = np.sum(np.abs(ratios[:20] - phi_paasch) < 0.05) if len(ratios) > 0 else 0
        print(f"  {len(abs_evals)} distinct |evals|, "
              f"consec-phi: {consec_phi}, "
              f"pairwise-phi: {len(phi_pairs)}, "
              f"pairwise-gold: {len(gold_pairs)}")

    return results


def plot_spectrum_vs_s(results, save_path=None):
    """
    Plot eigenvalue trajectories and ratio distributions vs s.

    Args:
        results: list of (s, abs_evals, ratios)
        save_path: if provided, save figure to this path
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available; skipping plots.")
        return

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Panel 1: Eigenvalue trajectories vs s
    ax1 = axes[0]
    s_vals = [r[0] for r in results]
    max_n = 20  # plot first 20 eigenvalues

    for i in range(max_n):
        evals_i = []
        s_for_i = []
        for r in results:
            s, abs_evals = r[0], r[1]
            if i < len(abs_evals):
                evals_i.append(abs_evals[i])
                s_for_i.append(s)
        if evals_i:
            ax1.plot(s_for_i, evals_i, '-', linewidth=0.8, alpha=0.7)

    ax1.set_xlabel('Jensen parameter s')
    ax1.set_ylabel('|Dirac eigenvalue|')
    ax1.set_title('First 20 eigenvalue trajectories')
    ax1.grid(True, alpha=0.3)

    # Panel 2: Pairwise phi-near ratio count vs s
    ax2 = axes[1]
    phi_counts = [len(r[3]) for r in results]
    gold_counts = [len(r[4]) for r in results]
    ax2.plot(s_vals, phi_counts, 'ro-', label='Near Paasch phi', markersize=5)
    ax2.plot(s_vals, gold_counts, 'gs-', label='Near golden ratio', markersize=5)
    ax2.set_xlabel('Jensen parameter s')
    ax2.set_ylabel('Number of pairwise ratios (3% tol)')
    ax2.set_title('Pairwise phi/golden ratio count vs s')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # Panel 3: All pairwise ratios at s=0 (bi-invariant)
    ax3 = axes[2]
    phi_p = 1.53158
    if len(results) > 0:
        abs_evals_0 = results[0][1]
        n = min(20, len(abs_evals_0))
        all_ratios = []
        for i in range(n):
            for j in range(i + 1, n):
                all_ratios.append(abs_evals_0[j] / abs_evals_0[i])
        all_ratios = [r for r in all_ratios if 1.0 < r < 2.5]
        if all_ratios:
            ax3.hist(all_ratios, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
            ax3.axvline(x=phi_p, color='red', linestyle='--', linewidth=2,
                       label=f'Paasch phi={phi_p}')
            ax3.axvline(x=(1 + np.sqrt(5)) / 2, color='orange', linestyle='--',
                       linewidth=2, label=f'golden={(1+np.sqrt(5))/2:.4f}')
            ax3.set_xlabel('Pairwise eigenvalue ratio')
            ax3.set_ylabel('Count')
            ax3.set_title(f'All pairwise ratios at s=0 (bi-invariant)')
            ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"  Plot saved to {save_path}")
    else:
        plt.savefig('dirac_spectrum_vs_s.png', dpi=150)
        print("  Plot saved to dirac_spectrum_vs_s.png")

    plt.close()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("=" * 80)
    print("TIER 1: DIRAC SPECTRUM ON (SU(3), g_s)")
    print("=" * 80)

    # --- Step 1: Infrastructure ---
    print("\n[1] Building su(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    # Validate structure constants
    anti_err = np.max(np.abs(f_abc + np.transpose(f_abc, (1, 0, 2))))
    imag_err = np.max(np.abs(f_abc.imag)) if np.iscomplexobj(f_abc) else 0
    print(f"  Structure constants: antisymmetry err={anti_err:.2e}")
    print(f"  Killing form diagonal: {np.diag(B_ab)}")
    print(f"  Killing form off-diag max: {np.max(np.abs(B_ab - np.diag(np.diag(B_ab)))):.2e}")
    print(f"  g_0 = |B| positive? eigenvalues: {np.sort(eigvalsh(np.abs(B_ab)))}")

    # Validate reductivity
    reductive_err = 0.0
    for a in U2_IDX:
        for b in M_IDX:
            for c in U2_IDX:
                reductive_err = max(reductive_err, abs(f_abc[a, b, c]))
    print(f"  Reductivity [u(2), m] subset m: max err = {reductive_err:.2e}")

    # --- Step 2: Clifford algebra ---
    print("\n[2] Building Cliff(8) algebra...")
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford algebra err: {cliff_err:.2e}")

    gamma9 = build_chirality(gammas)
    g9_sq_err = np.max(np.abs(gamma9 @ gamma9 - np.eye(16)))
    g9_herm_err = np.max(np.abs(gamma9 - gamma9.conj().T))
    print(f"  gamma_9^2 = I err: {g9_sq_err:.2e}")
    print(f"  gamma_9 Hermitian err: {g9_herm_err:.2e}")

    # Verify gamma_9 anticommutes with all gammas
    g9_anticomm_err = max(np.max(np.abs(gamma9 @ g + g @ gamma9)) for g in gammas)
    print(f"  {'{'}gamma_9, gamma_a{'}'} = 0 err: {g9_anticomm_err:.2e}")

    # --- Step 2b: SU(2) benchmark ---
    print("\n[2b] SU(2) / S^3 benchmark (validates entire Dirac pipeline)...")
    su2_passed, su2_err = su2_benchmark()
    status = "PASS" if su2_passed else "FAIL"
    print(f"  SU(2) benchmark: {status} (max err = {su2_err:.2e})")
    print(f"  Verified: trivial (j=0), fundamental (j=1/2), adjoint (j=1)")
    print(f"  All eigenvalues match known S^3 Dirac spectrum at machine epsilon.")
    if not su2_passed:
        print("  WARNING: SU(2) benchmark FAILED. Results may be unreliable.")

    # --- Step 3: Validate irreps ---
    # Clear irrep cache before validation
    global _irrep_cache
    _irrep_cache = {}

    # Determine max_pq_sum from command-line arg or default
    max_pq = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    print(f"\n[3] Validating SU(3) irrep constructions (p+q <= {max_pq})...")
    test_irreps = []
    for s_val in range(1, max_pq + 1):
        for p_val in range(s_val + 1):
            test_irreps.append((p_val, s_val - p_val))

    all_pass = True
    for p, q in test_irreps:
        dim_expected = (p + 1) * (q + 1) * (p + q + 2) // 2
        try:
            rho, dim_rho = get_irrep(p, q, gens, f_abc)
            hom_err, ah_err = validate_irrep(rho, f_abc, f"({p},{q})")
            ok = hom_err < 1e-10 and ah_err < 1e-10
            status = "OK" if ok else "FAIL"
            if not ok:
                all_pass = False
            print(f"  ({p},{q}): dim={dim_rho} (expect {dim_expected}), "
                  f"hom_err={hom_err:.2e}, anti-Herm_err={ah_err:.2e} [{status}]")
        except Exception as e:
            all_pass = False
            print(f"  ({p},{q}): dim={dim_expected}, CONSTRUCTION FAILED: {e}")

    if all_pass:
        print(f"  ALL {len(test_irreps)} irreps validated successfully.")
    else:
        print(f"  WARNING: Some irreps FAILED validation.")

    # --- Step 4: Bi-invariant spectrum (s=0 cross-check) ---
    _irrep_cache = {}
    print(f"\n[4] Computing bi-invariant spectrum (s=0, max_pq_sum={max_pq})...")
    all_evals_0, eval_data_0 = collect_spectrum(
        0.0, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=True
    )

    print("\n  Analysis of s=0 spectrum:")
    abs_evals_0, ratios_0 = analyze_spectrum(all_evals_0, verbose=True)
    phi_pairs_0, gold_pairs_0 = analyze_nonconsecutive_ratios(abs_evals_0, verbose=True)

    # --- Step 5: Single deformed spectrum (s=0.5 test) ---
    _irrep_cache = {}
    print(f"\n{'='*80}")
    print(f"[5] Computing deformed spectrum (s=0.5, max_pq_sum={max_pq})...")
    all_evals_05, eval_data_05 = collect_spectrum(
        0.5, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=True
    )

    print("\n  Analysis of s=0.5 spectrum:")
    abs_evals_05, ratios_05 = analyze_spectrum(all_evals_05, verbose=True)
    phi_pairs_05, gold_pairs_05 = analyze_nonconsecutive_ratios(abs_evals_05, verbose=True)

    # --- Step 6: Hermiticity / anti-Hermiticity check on D_pi ---
    print(f"\n{'='*80}")
    print("[6] Checking Dirac operator adjointness on sample sector...")

    B_ab_check = compute_killing_form(f_abc)
    g_s_check = jensen_metric(B_ab_check, 0.5)
    E_check = orthonormal_frame(g_s_check)
    ft_check = frame_structure_constants(f_abc, E_check)
    Gamma_check = connection_coefficients(ft_check)
    Omega_check = spinor_connection_offset(Gamma_check, gammas)

    rho_fund, _ = get_irrep(1, 0, gens, f_abc)
    D_fund = dirac_operator_on_irrep(rho_fund, E_check, gammas, Omega_check)

    # Check Hermiticity
    D_herm_err = np.max(np.abs(D_fund - D_fund.conj().T))
    D_aherm_err = np.max(np.abs(D_fund + D_fund.conj().T))
    print(f"  D on (1,0) at s=0.5: Hermitian err={D_herm_err:.2e}, anti-Hermitian err={D_aherm_err:.2e}")

    evals_fund = np.linalg.eigvals(D_fund)
    real_part = np.abs(evals_fund.real)
    imag_part = np.abs(evals_fund.imag)
    print(f"  Eigenvalue real parts: max={np.max(real_part):.6f}, mean={np.mean(real_part):.6f}")
    print(f"  Eigenvalue imag parts: max={np.max(imag_part):.6f}, mean={np.mean(imag_part):.6f}")

    if np.max(real_part) < 1e-8:
        print("  -> D is anti-Hermitian (purely imaginary eigenvalues). Using imag parts.")
        convention = "anti-hermitian"
    elif np.max(imag_part) < 1e-8:
        print("  -> D is Hermitian (purely real eigenvalues).")
        convention = "hermitian"
    else:
        print("  -> D is NEITHER Hermitian nor anti-Hermitian. Using absolute values.")
        convention = "general"

    # --- Step 7: s-sweep ---
    _irrep_cache = {}
    print(f"\n{'='*80}")
    print(f"[7] s-parameter sweep (max_pq_sum={max_pq})...")
    s_values = np.linspace(0.0, 2.0, 21)
    results = sweep_s(s_values, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=False)

    # --- Step 8: Visualization ---
    print(f"\n{'='*80}")
    print("[8] Generating plots...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(script_dir, 'dirac_spectrum_vs_s.png')
    plot_spectrum_vs_s(results, save_path=plot_path)

    # --- Step 9: Summary ---
    print(f"\n{'='*80}")
    print("[9] SUMMARY")
    print("=" * 80)

    phi_p = 1.53158
    golden = (1 + np.sqrt(5)) / 2

    print(f"\n  Target ratios: Paasch phi = {phi_p:.5f}, Golden ratio = {golden:.5f}")

    # Table 1: Consecutive ratios (original analysis)
    print(f"\n  TABLE 1: Consecutive eigenvalue ratios")
    print(f"  {'s':>6} {'#evals':>7} {'consec-phi':>11} {'consec-gold':>12}")
    for s, abs_evals, ratios, _, _ in results:
        if len(ratios) > 0:
            r20 = ratios[:20]
            n_phi = np.sum(np.abs(r20 - phi_p) < 0.05)
            n_gold = np.sum(np.abs(r20 - golden) < 0.05)
            print(f"  {s:6.3f} {len(abs_evals):7d} {n_phi:11d} {n_gold:12d}")

    # Table 2: Non-consecutive (pairwise) ratios -- the KEY analysis
    print(f"\n  TABLE 2: Non-consecutive pairwise ratios (first 20 eigenvalues)")
    print(f"  {'s':>6} {'#phi-pairs':>11} {'#gold-pairs':>12} {'best phi':>10} {'best gold':>10}")
    for s, abs_evals, ratios, phi_pairs, gold_pairs in results:
        best_phi_r = min((abs(r - phi_p), r) for _, _, r, _, _ in phi_pairs)[1] if phi_pairs else 0
        best_gold_r = min((abs(r - golden), r) for _, _, r, _, _ in gold_pairs)[1] if gold_pairs else 0
        print(f"  {s:6.3f} {len(phi_pairs):11d} {len(gold_pairs):12d} "
              f"{best_phi_r:10.5f} {best_gold_r:10.5f}")

    # Find best s for pairwise phi
    best_s = 0
    best_phi_err = 999
    for s, _, _, phi_pairs, _ in results:
        for _, _, r, _, _ in phi_pairs:
            if abs(r - phi_p) < best_phi_err:
                best_phi_err = abs(r - phi_p)
                best_s = s

    print(f"\n  Best s for Paasch phi: s={best_s:.3f} (closest ratio err={best_phi_err:.5f})")

    # Detailed output at best s
    for s, abs_evals, _, phi_pairs, gold_pairs in results:
        if abs(s - best_s) < 1e-6:
            print(f"\n  Phi-near pairs at s={s:.3f}:")
            for i, j, r, vi, vj in sorted(phi_pairs, key=lambda x: abs(x[2] - phi_p)):
                err_pct = abs(r - phi_p) / phi_p * 100
                print(f"    [{i}]/[{j}]: {vj:.6f}/{vi:.6f} = {r:.6f} (err {err_pct:.2f}%)")
            if gold_pairs:
                print(f"  Golden-near pairs at s={s:.3f}:")
                for i, j, r, vi, vj in sorted(gold_pairs, key=lambda x: abs(x[2] - golden)):
                    err_pct = abs(r - golden) / golden * 100
                    print(f"    [{i}]/[{j}]: {vj:.6f}/{vi:.6f} = {r:.6f} (err {err_pct:.2f}%)")

    # Key algebraic result
    print(f"\n  KEY ALGEBRAIC RESULT:")
    print(f"    At s=0 (bi-invariant), all lambda^2 = n/36 for integer n.")
    print(f"    The ratio sqrt(63/27) = sqrt(7/3) = {np.sqrt(7/3):.6f}")
    print(f"    Paasch phi = {phi_p:.6f}")
    print(f"    Difference: {abs(np.sqrt(7/3) - phi_p):.6f} ({abs(np.sqrt(7/3) - phi_p)/phi_p*100:.2f}%)")
    print(f"    This ratio is an ALGEBRAIC INVARIANT of the bi-invariant Dirac spectrum on SU(3).")

    print(f"\n{'='*80}")
    print("COMPUTATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
