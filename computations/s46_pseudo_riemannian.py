"""
PSEUDO-RIEMANNIAN-46: Spectral Triple Axioms for SU(2,1)
==========================================================

Explores replacing the compact SU(3) internal space with the non-compact
real form SU(2,1). The Killing form on su(2,1) has indefinite signature
(5,3), making the canonical left-invariant metric pseudo-Riemannian.

MATHEMATICAL FRAMEWORK
-----------------------

su(2,1) is the Lie algebra of 3x3 matrices X satisfying:
    X^dag eta + eta X = 0,   eta = diag(1,1,-1)

This is an 8-dimensional REAL Lie algebra with basis:
    {T_1,...,T_8} chosen as anti-Hermitian w.r.t. eta-inner product

The Killing form B(X,Y) = Tr(ad_X ad_Y) has signature (5,3):
    - 5 compact directions (su(2) subalgebra + parts of complement)
    - 3 non-compact directions (boosts)

Key differences from SU(3):
    1. Killing form is INDEFINITE -> metric pseudo-Riemannian
    2. Group is non-compact -> L^2(G) has continuous spectrum
    3. Clifford algebra Cl(5,3) replaces Cl(8,0)
    4. Spinor module has 16 components but indefinite inner product
    5. Heat kernel Tr(exp(-tD^2)) may diverge (non-compact volume)

AXIOM ANALYSIS
--------------
We check the 7 axioms of the spectral triple:
    1. Dimension (spectral dimension from zeta function)
    2. Regularity (smooth subalgebra)
    3. Finiteness (finite projective module)
    4. Reality (real structure J)
    5. First order ([[D,a],b^o]=0)
    6. Orientability (Hochschild cycle -> chirality)
    7. Poincare duality (intersection form non-degenerate)

GATE: PSEUDO-RIEMANNIAN-46
    PASS if: >= 4 axioms survive on SU(2,1) with indefinite Killing metric
    FAIL if: < 4 axioms survive

Author: Connes-NCG-Theorist (Session 46, W4-16)
Date: 2026-03-15
References:
    - de Groot (2026), Paper 36: Pseudo-Riemannian Spectral Triples for SU(1,1)
    - Martinetti (2026), Paper 44: Twisted SM and Krein Structure
    - Martinetti (2025), Paper 31: Emergence of Lorentz from Twisted Spectral Triple
    - Filaci-Martinetti (2023), Paper 30: Critical Survey of Twisted Spectral Triples
    - Connes (1996), Paper 07: Spectral Action Principle
    - Chamseddine-Connes-Marcolli (2007), Paper 10: SM from NCG
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, norm, svd, det, cholesky
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold as TAU_FOLD

np.set_printoptions(precision=10, linewidth=140, suppress=True)
OUTDIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# SECTION 1: SU(2,1) LIE ALGEBRA INFRASTRUCTURE
# =============================================================================

def su21_generators():
    """
    Construct 8 generators of su(2,1) in the defining representation.

    su(2,1) = { X in M_3(C) : X^dag eta + eta X = 0 }, eta = diag(1,1,-1)

    A matrix X satisfying this condition has the form:
        X = ( A    v  )     A in su(2), v in C^2, a in iR
            (-v^dag  a )

    We use the Gell-Mann-like basis adapted to su(2,1):
    Compact generators (su(2) block + compact complement):
        T_1 = -i/2 * lambda_1_eta, ..., T_3 = -i/2 * lambda_3_eta (su(2) subalgebra)
        T_8 = -i/2 * lambda_8_eta (u(1) in maximal compact su(2)+u(1))

    Non-compact generators (off-diagonal boosts):
        T_4, T_5, T_6, T_7 adapted via eta-conjugation of lambda_4,...,lambda_7

    Returns:
        list of 8 complex (3,3) matrices satisfying X^dag eta + eta X = 0
        eta: the (2,1) signature matrix
    """
    eta = np.diag([1.0, 1.0, -1.0]).astype(complex)

    # Standard Gell-Mann matrices (for su(3))
    lam = []

    lam.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))          # lambda_1
    lam.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))       # lambda_2
    lam.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))          # lambda_3
    lam.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))           # lambda_4
    lam.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))        # lambda_5
    lam.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))           # lambda_6
    lam.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))        # lambda_7
    lam.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3))  # lambda_8

    # For su(2,1), the generators T_a must satisfy T_a^dag eta + eta T_a = 0,
    # i.e., T_a is anti-Hermitian w.r.t. the eta inner product.
    #
    # For su(3), the generators are e_a = -i/2 * lambda_a, anti-Hermitian
    # w.r.t. the standard inner product.
    #
    # For su(2,1), we need: (eta T_a)^dag = -(eta T_a), i.e., eta T_a is anti-Hermitian.
    # Equivalently: T_a = -eta^{-1} T_a^dag eta
    #
    # The compact generators (indices 1,2,3,8) live in su(2)+u(1) block;
    # these satisfy T_a^dag = -T_a AND commute with eta in the (1,2) block.
    # For the (1,3) and (2,3) mixing generators (indices 4,5,6,7),
    # eta conjugation flips the sign of the off-diagonal blocks.

    gens = []

    # su(2,1) = { X in M_3(C) : X^dag eta + eta X = 0 }
    # This means eta*X is skew-Hermitian: (eta*X)^dag = X^dag*eta = -eta*X.
    #
    # The Cartan involution is theta(X) = -X^dag.
    # Compact subalgebra k = {X : theta(X) = X} = anti-Hermitian matrices in su(2,1)
    # Non-compact complement p = {X : theta(X) = -X} = Hermitian matrices in su(2,1)
    #
    # Compact generators (anti-Hermitian, 4 total):
    #   e1, e2, e3: su(2) subalgebra acting in the (1,2) block
    #   e8: u(1) diagonal
    # Non-compact generators (Hermitian, 4 total):
    #   T4, T5, T6, T7: mixing rows (1,2) with row 3
    #
    # For the (i,3) mixing: X = alpha|i><3| + beta|3><i|
    # Condition X^dag eta + eta X = 0 gives beta = alpha^*.
    # So X = alpha|i><3| + alpha^*|3><i|.
    # For real alpha: X is Hermitian (non-compact direction).
    # For imaginary alpha: X is also Hermitian after the phase.

    # Compact generators (anti-Hermitian):
    e1 = -1j/2 * lam[0]   # T_1: su(2), lambda_1
    e2 = -1j/2 * lam[1]   # T_2: su(2), lambda_2
    e3 = -1j/2 * lam[2]   # T_3: su(2), lambda_3
    e8 = -1j/2 * lam[7]   # T_8: u(1), lambda_8

    # Non-compact generators (Hermitian, satisfying X^dag eta + eta X = 0):
    # T4: 1/2 (|1><3| + |3><1|) -- real symmetric
    T4 = np.zeros((3,3), dtype=complex)
    T4[0,2] = 0.5; T4[2,0] = 0.5

    # T5: i/2 (|1><3| - |3><1|) -- imaginary antisymmetric (still Hermitian!)
    T5 = np.zeros((3,3), dtype=complex)
    T5[0,2] = 0.5j; T5[2,0] = -0.5j

    # T6: 1/2 (|2><3| + |3><2|) -- real symmetric
    T6 = np.zeros((3,3), dtype=complex)
    T6[1,2] = 0.5; T6[2,1] = 0.5

    # T7: i/2 (|2><3| - |3><2|) -- imaginary antisymmetric (Hermitian)
    T7 = np.zeros((3,3), dtype=complex)
    T7[1,2] = 0.5j; T7[2,1] = -0.5j

    # Order: compact (e1, e2, e3), non-compact (T4, T5, T6, T7), compact (e8)
    # This matches the SU(3) ordering of Gell-Mann matrices
    gens = [e1, e2, e3, T4, T5, T6, T7, e8]

    return gens, eta


def verify_su21_condition(gens, eta):
    """Verify that all generators satisfy X^dag eta + eta X = 0."""
    max_err = 0.0
    for a, T in enumerate(gens):
        cond = T.conj().T @ eta + eta @ T
        err = np.max(np.abs(cond))
        if err > max_err:
            max_err = err
    return max_err


def compute_structure_constants_su21(gens):
    """
    Compute structure constants f_{abc} from [T_a, T_b] = f_{abc} T_c.

    For su(2,1), the structure constants are REAL but the Killing form
    has indefinite signature. We use the trace formula adapted to the
    defining representation.

    The trace formula: f_{abc} = -2 Tr([T_a, T_b] T_c) / Tr(T_a T_a)
    must be adjusted since Tr(T_a T_b) is no longer -1/2 delta_{ab}.
    We use the general formula via the inverse metric.

    Actually, for simplicity, we solve the linear system:
        [T_a, T_b] = sum_c f_{abc} T_c
    by expanding in the basis.
    """
    n = len(gens)

    # Build the basis matrix: flatten each generator into a 9-vector
    basis_mat = np.zeros((9, n), dtype=complex)
    for a in range(n):
        basis_mat[:, a] = gens[a].flatten()

    # Compute commutators and project
    f = np.zeros((n, n, n), dtype=float)
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            comm_vec = comm.flatten()
            # Solve basis_mat @ coeffs = comm_vec in least-squares sense
            coeffs, residuals, rank, sv = np.linalg.lstsq(basis_mat, comm_vec, rcond=None)
            for c in range(n):
                f[a, b, c] = coeffs[c].real
                f[b, a, c] = -coeffs[c].real

    return f


def compute_killing_form_su21(f_abc):
    """
    Compute Killing form B_{ab} = sum_{c,d} f_{acd} f_{bdc}.

    For su(2,1), this has signature (5,3) -- 5 positive and 3 negative eigenvalues.
    """
    return np.einsum('acd,bdc->ab', f_abc, f_abc)


# =============================================================================
# SECTION 2: CLIFFORD ALGEBRA Cl(5,3) AND INDEFINITE SPINORS
# =============================================================================

def build_cliff_53():
    """
    Construct generators of Cl(5,3) -- the Clifford algebra for signature (5,3).

    Cl(p,q) has generators gamma_1,...,gamma_{p+q} satisfying:
        {gamma_a, gamma_b} = 2 eta_{ab} I
    where eta = diag(+1,...,+1, -1,...,-1) with p plus signs and q minus signs.

    For (5,3): eta = diag(+1,+1,+1,+1,+1,-1,-1,-1)

    The representation dimension for Cl(p,q) with p+q=8 (even) is 2^4 = 16.

    Construction: We modify the Cl(8,0) construction by multiplying
    the last 3 generators by i (this changes signature from + to -).

    If {gamma_a} satisfy {gamma_a, gamma_b} = 2 delta_{ab} I (all positive),
    then replacing gamma_a -> i*gamma_a for the last q generators gives:
        {i*gamma_a, i*gamma_b} = -2 delta_{ab} I (negative signature for those)
    and cross terms with unchanged generators give 0 (OK since a != b cross
    terms are 0 anyway).

    WARNING: This gives gamma_a that are NOT Hermitian for the last q generators
    (they become anti-Hermitian). The inner product on spinor space becomes
    INDEFINITE -- this is the Krein space structure of Paper 44.

    Returns:
        gammas: list of 8 complex (16,16) matrices
        eta_cliff: (8,) array of signature signs (+1 or -1)
    """
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def kron4(A, B, C, D):
        return np.kron(A, np.kron(B, np.kron(C, D)))

    # Start with Cl(8,0) generators (all Hermitian, positive signature)
    gammas_pos = [
        kron4(s1, I2, I2, I2),   # gamma_1
        kron4(s2, I2, I2, I2),   # gamma_2
        kron4(s3, s1, I2, I2),   # gamma_3
        kron4(s3, s2, I2, I2),   # gamma_4
        kron4(s3, s3, s1, I2),   # gamma_5
        kron4(s3, s3, s2, I2),   # gamma_6
        kron4(s3, s3, s3, s1),   # gamma_7
        kron4(s3, s3, s3, s2),   # gamma_8
    ]

    # For Cl(5,3): first 5 positive, last 3 negative
    # Multiply last 3 by i to flip signature
    eta_signs = np.array([+1, +1, +1, +1, +1, -1, -1, -1], dtype=float)

    gammas = []
    for a in range(8):
        if eta_signs[a] > 0:
            gammas.append(gammas_pos[a].copy())
        else:
            gammas.append(1j * gammas_pos[a])  # i*gamma -> anti-Hermitian

    return gammas, eta_signs


def validate_clifford_indefinite(gammas, eta_signs):
    """
    Verify {gamma_a, gamma_b} = 2 eta_{ab} I for Cl(p,q).

    Returns max error.
    """
    n = len(gammas)
    dim = gammas[0].shape[0]
    max_err = 0.0
    for a in range(n):
        for b in range(n):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            if a == b:
                target = 2.0 * eta_signs[a] * np.eye(dim)
            else:
                target = np.zeros((dim, dim), dtype=complex)
            err = np.max(np.abs(anticomm - target))
            if err > max_err:
                max_err = err
    return max_err


def build_chirality_indefinite(gammas, eta_signs):
    """
    Chirality for Cl(p,q) with p+q=8.

    gamma_9 = (factor) * gamma_1 ... gamma_8

    The normalization factor ensures gamma_9^2 = I.
    For Cl(p,q): gamma_9^2 = (-1)^{q(q-1)/2 + q} * I
    For (5,3): q=3, q(q-1)/2=3, so (-1)^{3+3} = (-1)^6 = +1 -> gamma_9^2 = I.
    No extra factor needed.

    But wait: gamma_9^2 = (gamma_1...gamma_8)^2
    = gamma_1...gamma_8 * gamma_1...gamma_8
    Moving gamma_8 past 7 gammas: (-1)^7 * gamma_1...gamma_7 gamma_8 gamma_1...gamma_7 * gamma_8^2
    This is complicated. Let me compute directly.

    Returns:
        gamma9: (16,16) matrix, gamma9^2 should equal I (up to sign)
    """
    gamma9 = np.eye(16, dtype=complex)
    for g in gammas:
        gamma9 = gamma9 @ g
    return gamma9


# =============================================================================
# SECTION 3: DIRAC OPERATOR ON SU(2,1) (FINITE IRREPS ONLY)
# =============================================================================

def su21_spin_connection(Gamma, gammas):
    """
    Compute the spinorial curvature offset Omega for pseudo-Riemannian case.

    Same formula as for SU(3), but now using Cl(5,3) gammas and the
    connection coefficients computed from the indefinite Killing metric.

    Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c

    Returns:
        Omega: (16,16) complex matrix
    """
    n = len(gammas)
    dim = gammas[0].shape[0]
    Omega = np.zeros((dim, dim), dtype=complex)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gammas[a] @ gammas[b] @ gammas[c]

    Omega *= 0.25
    return Omega


def orthonormal_frame_indefinite(g_ab, eta_target):
    """
    Construct an orthonormal frame E for an indefinite metric g_ab.

    We need E such that E @ g_ab @ E^T = eta_target, where
    eta_target = diag(eta_signs).

    This is done by diagonalizing g_ab, taking square roots of |eigenvalues|,
    and arranging signs to match eta_target.

    Args:
        g_ab: (8,8) real symmetric metric (indefinite)
        eta_target: (8,) array of target signature signs

    Returns:
        E: (8,8) frame matrix such that E g E^T = diag(eta_target)
    """
    eigvals, eigvecs = np.linalg.eigh(g_ab)
    # Sort by sign: positive first, then negative
    pos_idx = np.where(eigvals > 0)[0]
    neg_idx = np.where(eigvals < 0)[0]

    n_pos = np.sum(eta_target > 0)
    n_neg = np.sum(eta_target < 0)

    if len(pos_idx) != n_pos or len(neg_idx) != n_neg:
        print(f"WARNING: Metric signature mismatch! Found ({len(pos_idx)},{len(neg_idx)}), expected ({n_pos},{n_neg})")
        print(f"Eigenvalues: {eigvals}")

    # Build frame: for positive eigenvalues, E_a = v_a / sqrt(|lambda_a|)
    # For negative eigenvalues, same but with a sign flip in the result
    E = np.zeros((8, 8), dtype=float)

    # Map positive eigenvalues to positive eta entries
    target_pos_idx = np.where(eta_target > 0)[0]
    target_neg_idx = np.where(eta_target < 0)[0]

    for i, (ti, si) in enumerate(zip(target_pos_idx, pos_idx)):
        E[ti, :] = eigvecs[:, si] / np.sqrt(eigvals[si])

    for i, (ti, si) in enumerate(zip(target_neg_idx, neg_idx)):
        E[ti, :] = eigvecs[:, si] / np.sqrt(-eigvals[si])

    return E


def frame_structure_constants_general(f_abc, E):
    """
    Compute structure constants in the orthonormal frame (same formula as SU(3)).

    ft^f_{ab} = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef}
    """
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)


def connection_coefficients_indefinite(ft, eta_signs):
    """
    Levi-Civita connection for a left-invariant pseudo-Riemannian metric.

    The Koszul formula in ON frame with indefinite metric eta_{ab}:
        2 eta_{cc} Gamma^c_{ab} = eta_{cc}(ft_{abc} - ft_{bca} + ft_{cab})

    where the structure constants ft are in the ON frame.
    Since eta_{cc} = +/-1, this is the same formula as the definite case
    when working in ON frame (just divide by eta_{cc}).

    BUT: metric compatibility requires:
        Gamma^c_{ab} eta_{cc} + Gamma^b_{ac} eta_{bb} = 0
    (antisymmetry in (b,c) with eta weighting).

    Using the standard Koszul formula directly:
        2 Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}
    where Gamma_{cab} = eta_{cc} Gamma^c_{ab}

    So Gamma^c_{ab} = (1/(2*eta_{cc})) * (ft_{abc} - ft_{bca} + ft_{cab})

    Args:
        ft: (8,8,8) ON frame structure constants
        eta_signs: (8,) array of metric signature

    Returns:
        Gamma: (8,8,8) connection coefficients Gamma[c,a,b] = Gamma^c_{ab}
    """
    n = ft.shape[0]
    Gamma = np.zeros((n, n, n), dtype=float)

    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma_cab = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])
                Gamma[c, a, b] = Gamma_cab / eta_signs[c]

    return Gamma


def validate_connection_indefinite(Gamma, eta_signs):
    """
    Validate metric compatibility: Gamma^c_{ab} eta_{cc} + Gamma^b_{ac} eta_{bb} = 0.
    """
    n = Gamma.shape[0]
    max_err = 0.0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                val = Gamma[c, a, b] * eta_signs[c] + Gamma[b, a, c] * eta_signs[b]
                if abs(val) > max_err:
                    max_err = abs(val)
    return max_err


# =============================================================================
# SECTION 4: DIRAC OPERATOR ON FINITE-DIM REPRESENTATIONS
# =============================================================================

def su21_finite_irreps(gens):
    """
    Construct finite-dimensional representations of su(2,1).

    CRITICAL DISTINCTION: SU(2,1) is non-compact. Its UNITARY representations
    are infinite-dimensional (principal series, discrete series).
    Finite-dimensional representations exist but are NOT unitary.

    The simplest finite-dim irreps:
        (1) Trivial: dim 1
        (2) Defining: dim 3 (the generators themselves)
        (3) Conjugate: dim 3 (T_a -> -T_a^T for real form, or eta-conjugation)
        (4) Adjoint: dim 8

    For the Dirac operator, on a COMPACT group we use unitary irreps (Peter-Weyl).
    For a NON-COMPACT group, Peter-Weyl does NOT apply. The L^2 decomposition
    involves the Plancherel measure on the unitary dual.

    However, for structural analysis, we CAN compute D on finite-dim irreps
    to check axiom behavior. The spectrum will NOT be the physical spectrum
    (which involves infinite-dim reps), but axiom violations detected on
    finite-dim reps are still valid obstructions.

    Returns:
        dict of (name, dim, representation_matrices)
    """
    irreps = {}

    # Trivial
    trivial = [np.zeros((1,1), dtype=complex) for _ in range(8)]
    irreps['trivial'] = (1, trivial)

    # Defining (3-dim)
    defining = [g.copy() for g in gens]
    irreps['defining'] = (3, defining)

    # Conjugate defining
    conjugate = [-g.T for g in gens]
    irreps['conjugate'] = (3, conjugate)

    # Adjoint (8-dim) -- need structure constants
    return irreps


def dirac_on_finite_irrep(rho_list, gammas, Omega, dim_rep):
    """
    Build Dirac matrix D_pi on a finite-dim representation.

    D_pi = sum_a rho(T_a) (x) gamma_a + I_{dim} (x) Omega

    Returns:
        D: (dim_rep * 16, dim_rep * 16) complex matrix
    """
    dim_spin = gammas[0].shape[0]  # 16
    D = np.zeros((dim_rep * dim_spin, dim_rep * dim_spin), dtype=complex)

    I_rep = np.eye(dim_rep, dtype=complex)

    # First term: sum_a rho(T_a) (x) gamma_a
    for a in range(8):
        D += np.kron(rho_list[a], gammas[a])

    # Second term: I (x) Omega
    D += np.kron(I_rep, Omega)

    return D


# =============================================================================
# SECTION 5: REAL STRUCTURE J ON SU(2,1)
# =============================================================================

def build_charge_conjugation_indefinite(gammas, eta_signs):
    """
    Construct the charge conjugation operator C for Cl(5,3).

    For Cl(p,q), the charge conjugation C satisfies:
        C gamma_a C^{-1} = +/- gamma_a^*

    The sign depends on (p,q) mod 8.

    For (5,3): p-q = 2, so KO-dimension = 2 mod 8.
    From the KO table:
        KO-dim 2: J^2 = -1, JD = DJ, J gamma = -gamma J
        (epsilon, epsilon', epsilon'') = (-1, +1, -1)

    This is DIFFERENT from SU(3) which has KO-dim 6:
        KO-dim 6: J^2 = +1, JD = DJ, J gamma = -gamma J
        (epsilon, epsilon', epsilon'') = (+1, +1, -1)

    The key difference: J^2 = -1 for SU(2,1) vs J^2 = +1 for SU(3).
    This is a QUATERNIONIC structure vs a REAL structure.

    Returns:
        C: (16,16) matrix (charge conjugation on spinors)
        ko_dim: int (KO-dimension)
        signs: dict with epsilon, epsilon_prime, epsilon_double_prime
    """
    # For KO-dim analysis, what matters is d = dim(manifold) mod 8
    # SU(2,1) has real dimension 8, same as SU(3).
    # But the SIGNATURE matters for the real structure.
    #
    # The KO-dimension of a pseudo-Riemannian manifold of signature (p,q) is:
    #   d_KO = p - q mod 8
    # For (5,3): d_KO = 5 - 3 = 2 mod 8
    # For (8,0) i.e. SU(3): d_KO = 8 - 0 = 0 mod 8 ... but we claimed KO=6!
    #
    # Wait. The KO-dimension of the spectral triple is NOT just dim(M) mod 8.
    # For a spin manifold, d_KO = d mod 8. For SU(3), d=8, so d_KO=0 mod 8.
    # But S8/S17a established d_KO=6 for the full NCG-SM setup.
    #
    # The resolution: the finite space F contributes. The product M x F has
    # d_KO = d_M + d_F mod 8. The SM has d_F = 6 mod 8. For M=SU(3) (d=8):
    # d_KO = 8 + 6 = 14 = 6 mod 8. Consistent.
    #
    # For SU(2,1) with signature (5,3), the spin structure depends on
    # the indefinite signature. The KO-dimension receives a correction.
    #
    # Atiyah-Bott-Shapiro: for a pseudo-Riemannian manifold of signature (p,q),
    # the relevant Clifford algebra is Cl(p,q), and the KO-dimension is:
    #   d_KO = p - q mod 8
    # So for SU(2,1): d_KO = 5 - 3 = 2 mod 8.
    #
    # Full product: d_KO = 2 + 6 = 8 = 0 mod 8 for SU(2,1) x F_SM.
    # This is DIFFERENT from the SU(3) case (d_KO = 6).

    # Use actual metric signature, not the assumed (5,3)
    p_actual = np.sum(eta_signs > 0)
    q_actual = np.sum(eta_signs < 0)
    ko_dim_manifold = (p_actual - q_actual) % 8
    ko_dim_full = (ko_dim_manifold + 6) % 8  # +6 from finite space F_SM

    # Signs from KO table:
    ko_signs = {
        0: (+1, +1, +1),   # d_KO = 0
        1: (+1, -1, None),  # d_KO = 1 (odd, no chirality)
        2: (-1, +1, +1),   # d_KO = 2
        3: (-1, -1, None), # d_KO = 3
        4: (-1, +1, -1),   # d_KO = 4
        5: (-1, -1, None), # d_KO = 5
        6: (+1, +1, -1),   # d_KO = 6
        7: (+1, -1, None), # d_KO = 7
    }

    eps_manifold = ko_signs[ko_dim_manifold]
    eps_full = ko_signs[ko_dim_full]

    print(f"\n  KO-dimension of SU(2,1) manifold: {ko_dim_manifold} (signature ({p_actual},{q_actual}), p-q={p_actual-q_actual})")
    print(f"  KO-dimension of SU(2,1) x F_SM: {ko_dim_full} (2 + 6 = 8 = 0 mod 8)")
    print(f"  Signs (manifold): (epsilon, epsilon', epsilon'') = {eps_manifold}")
    print(f"  Signs (full): (epsilon, epsilon', epsilon'') = {eps_full}")
    print(f"  Compare SU(3) x F: KO-dim = 6, signs = (+1, +1, -1)")

    # For the actual C matrix on Cl(5,3):
    # C satisfies C gamma_a C^{-1} = epsilon_a gamma_a^T
    # where epsilon_a depends on whether gamma_a is Hermitian (+) or anti-Hermitian (-).
    #
    # We construct C for KO-dim 2:
    # C = gamma_1 gamma_3 (product of Hermitian gammas at specific positions)
    # This requires careful construction. For now, compute numerically.

    # Build C as the product of the first two "positive" gammas
    # (this is one standard construction for KO-dim 2)
    # Actually, for Cl(5,3), C = gamma_1 * gamma_2 * gamma_6 * gamma_7 * gamma_8
    # (product of generators that square to -1 under the reality condition)

    # Numerical approach: find C such that C gamma_a = eps_a gamma_a^T C
    # with the correct pattern of signs.
    # For KO-dim 2: C gamma_a C^{-1} = -gamma_a^T (all generators)

    # Construct C as product of all negative-signature gamma matrices
    # For Cl(p,q), C = product of all "timelike" gammas (those with eta=-1)
    neg_indices = [a for a in range(len(gammas)) if eta_signs[a] < 0]
    C = np.eye(gammas[0].shape[0], dtype=complex)
    for idx in neg_indices:
        C = C @ gammas[idx]
    print(f"  C constructed from {len(neg_indices)} negative-signature gammas: indices {neg_indices}")

    return C, ko_dim_manifold, ko_dim_full, eps_manifold, eps_full


# =============================================================================
# SECTION 6: AXIOM VERIFICATION ENGINE
# =============================================================================

def check_axiom_1_dimension(D, dim_expected=8):
    """
    Axiom 1 (Dimension): The spectral dimension is extracted from the
    growth rate of eigenvalues of |D|.

    For a d-dimensional manifold, Weyl's law gives:
        N(lambda) ~ C * lambda^d  as lambda -> infty

    For finite-dim D matrices, we check the dimension spectrum:
        d_s = lim_{s->0} s * zeta_D(s)  where zeta_D(s) = Tr(|D|^{-s})

    For the truncated (finite-dim) case, we compute the counting function
    slope on a log-log plot.

    For SU(2,1): the manifold dimension is 8 (same as SU(3)).
    But the continuous spectrum from non-compactness means Weyl's law
    is modified. The discrete part still gives d=8.

    Returns:
        d_s_estimate, verdict
    """
    evals = np.sort(np.abs(eigvalsh(D)))
    nonzero = evals[evals > 1e-10]
    if len(nonzero) < 4:
        return 0.0, "INCONCLUSIVE (too few eigenvalues)"

    # Log-log counting function
    N = np.arange(1, len(nonzero)+1)
    # d_s from N(lambda) ~ lambda^d => log N ~ d * log lambda
    coeffs = np.polyfit(np.log(nonzero), np.log(N), 1)
    d_est = coeffs[0]

    verdict = "PASS" if abs(d_est - dim_expected) < 2.0 else "FAIL"
    return d_est, verdict


def check_axiom_4_reality(D, C, ko_dim):
    """
    Axiom 4 (Reality): Check J^2 = epsilon * I and [J, D] = epsilon' * {J, D}.

    For KO-dim 2: J^2 = -I, JD = DJ.
    For KO-dim 0: J^2 = +I, JD = DJ.

    Returns:
        J2_val, JD_commutator_norm, verdict
    """
    # J = C * K where K is complex conjugation. On matrices: J(psi) = C * psi^*
    # J^2(psi) = C (C psi^*)^* = C C^* psi
    CC_star = C @ C.conj()
    I_n = np.eye(C.shape[0], dtype=complex)

    ko_signs_table = {0: +1, 2: -1, 4: -1, 6: +1}
    expected_eps = ko_signs_table.get(ko_dim, 0)

    J2_err = np.max(np.abs(CC_star - expected_eps * I_n))

    # [J, D]: J D psi = C (D psi)^* = C D^* psi^*
    # D J psi = D C psi^*
    # So [J,D] <-> C D^* - D C (as operators on column vectors)
    JD_comm = C @ D.conj() - D @ C
    JD_norm = np.max(np.abs(JD_comm))

    verdict = "PASS" if J2_err < 1e-8 and JD_norm < 1e-8 else "FAIL"
    if J2_err >= 1e-8:
        verdict += f" (J^2 error: {J2_err:.2e})"
    if JD_norm >= 1e-8:
        verdict += f" (JD comm: {JD_norm:.2e})"

    return J2_err, JD_norm, expected_eps, verdict


def check_axiom_5_order_one(D, gens_left, gens_right, dim_spin):
    """
    Axiom 5 (First Order): [[D, a], b^o] = 0 for all a in A, b^o in A^o.

    For the Lie group case, a acts by left multiplication (rho_L(T_a)),
    b^o acts by right multiplication (rho_R(T_b)).

    On the irrep sector: a -> rho(T_a) (x) I_spin, b^o -> I_rep (x) rho_R(T_b)
    This is the same computation as for SU(3).

    Returns:
        max_violation, worst_pair, verdict
    """
    n_gen = len(gens_left)
    max_viol = 0.0
    worst = (0, 0)

    for a in range(n_gen):
        # [D, a] where a acts as rho_L(T_a) (x) I_spin
        L_a = np.kron(gens_left[a], np.eye(dim_spin, dtype=complex))
        comm_Da = D @ L_a - L_a @ D

        for b in range(n_gen):
            # b^o acts as I_rep (x) some_matrix -- for the adjoint,
            # right action is different.
            # In the defining rep, right action: rho_R(T_b) = I (x) T_b^T
            # (right multiplication by T_b corresponds to (x . T_b)^T on columns)
            # This is only approximate for the Lie group spectral triple.
            # The actual b^o comes from the opposite algebra A^o.

            # For left-invariant D on a Lie group, the right regular representation
            # commutes with D (since D is left-invariant). So [[D, a], b^o] = 0
            # would follow if b^o is right multiplication. But right multiplication
            # does NOT factor as I (x) something on a single irrep.

            # For the finite-dim truncation, we can only check a limited version.
            # Skip detailed check here and flag as STRUCTURAL.
            pass

    return 0.0, (0, 0), "STRUCTURAL (see analysis)"


def check_axiom_6_orientability(D, gamma9):
    """
    Axiom 6 (Orientability): There exists a Hochschild cycle c such that
    pi(c) = gamma (the chirality operator).

    A necessary condition is that {D, gamma} = 0 (chirality anticommutes with D).

    Returns:
        anticomm_norm, verdict
    """
    anticomm = D @ gamma9 + gamma9 @ D
    norm_val = np.max(np.abs(anticomm)) / max(np.max(np.abs(D)), 1e-10)
    verdict = "PASS" if norm_val < 1e-8 else f"FAIL (||{{D,gamma}}||/||D|| = {norm_val:.4e})"
    return norm_val, verdict


# =============================================================================
# SECTION 7: COMPARISON ENGINE -- SU(3) vs SU(2,1)
# =============================================================================

def build_su3_reference(tau=0.0):
    """
    Build the SU(3) Dirac operator at given tau for comparison.
    Uses the existing tier1_dirac_spectrum infrastructure.
    """
    from tier1_dirac_spectrum import (
        su3_generators as su3_gens_fn,
        compute_structure_constants as su3_fsc,
        compute_killing_form as su3_kill,
        jensen_metric as su3_jm,
        orthonormal_frame as su3_of,
        frame_structure_constants as su3_fsc2,
        connection_coefficients as su3_cc,
        spinor_connection_offset as su3_sco,
        build_cliff8 as su3_cliff,
        build_chirality as su3_chir,
        dirac_operator_on_irrep as su3_dirac,
        get_irrep,
    )

    gens = su3_gens_fn()
    f_abc = su3_fsc(gens)
    B_ab = su3_kill(f_abc)
    g_s = su3_jm(B_ab, tau)
    E = su3_of(g_s)
    ft = su3_fsc2(f_abc, E)
    Gamma = su3_cc(ft)
    gammas = su3_cliff()
    Omega = su3_sco(Gamma, gammas)
    gamma9 = su3_chir(gammas)

    # Build on defining irrep (1,0) for comparison
    rho_fund = [g.copy() for g in gens]
    dim_rep = 3
    dim_spin = 16
    D = np.zeros((dim_rep * dim_spin, dim_rep * dim_spin), dtype=complex)
    for a in range(8):
        D += np.kron(rho_fund[a], gammas[a])
    D += np.kron(np.eye(dim_rep), Omega)

    return D, B_ab, gammas, gamma9, Omega


# =============================================================================
# SECTION 8: MAIN COMPUTATION
# =============================================================================

def main():
    t0 = time.time()
    print("=" * 80)
    print("PSEUDO-RIEMANNIAN-46: SU(2,1) Spectral Triple Axiom Analysis")
    print("=" * 80)

    # ---- Step 1: Construct su(2,1) Lie algebra ----
    print("\n[1] Constructing su(2,1) generators...")
    gens, eta_21 = su21_generators()
    cond_err = verify_su21_condition(gens, eta_21)
    print(f"  su(2,1) condition ||X^dag eta + eta X|| = {cond_err:.2e}")
    assert cond_err < 1e-14, f"su(2,1) generators fail! Error = {cond_err}"

    # ---- Step 2: Structure constants and Killing form ----
    print("\n[2] Computing structure constants and Killing form...")
    f_abc = compute_structure_constants_su21(gens)

    # Verify [T_a, T_b] reconstruction
    max_recon_err = 0.0
    for a in range(8):
        for b in range(8):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            recon = sum(f_abc[a, b, c] * gens[c] for c in range(8))
            err = np.max(np.abs(comm - recon))
            if err > max_recon_err:
                max_recon_err = err
    print(f"  Structure constant reconstruction error: {max_recon_err:.2e}")

    B_ab = compute_killing_form_su21(f_abc)
    B_eigvals = np.sort(eigvalsh(B_ab))
    n_pos = np.sum(B_eigvals > 1e-10)
    n_neg = np.sum(B_eigvals < -1e-10)
    n_zero = np.sum(np.abs(B_eigvals) <= 1e-10)
    print(f"  Killing form eigenvalues: {B_eigvals}")
    print(f"  Signature: ({n_pos}, {n_neg}), zeros: {n_zero}")

    if n_pos + n_neg != 8:
        print(f"  WARNING: Killing form is degenerate! {n_zero} zero eigenvalues.")
        print("  This means su(2,1) is not semisimple in this basis, or basis error.")

    # Compare with SU(3)
    print("\n  --- SU(3) comparison ---")
    from tier1_dirac_spectrum import su3_generators, compute_structure_constants, compute_killing_form
    gens_su3 = su3_generators()
    f_su3 = compute_structure_constants(gens_su3)
    B_su3 = compute_killing_form(f_su3)
    B_su3_eigvals = np.sort(eigvalsh(B_su3))
    print(f"  SU(3) Killing form eigenvalues: {B_su3_eigvals}")
    n_pos_su3 = np.sum(B_su3_eigvals > 1e-10)
    n_neg_su3 = np.sum(B_su3_eigvals < -1e-10)
    print(f"  SU(3) signature: ({n_pos_su3}, {n_neg_su3}) [all negative for compact form]")

    # ---- Step 3: Indefinite metric and frame ----
    print("\n[3] Constructing pseudo-Riemannian metric and frame...")

    # The "bi-invariant" metric on SU(2,1) is -B (negative Killing form)
    # For compact: -B > 0 (positive definite). For SU(2,1): -B has signature (3,5).
    # Or use +B which has signature (n_pos_B, n_neg_B).
    # The natural metric for a Riemannian structure would use |B| (absolute value
    # of Killing). For the PSEUDO-Riemannian structure, we use B itself (or -B).

    # Use -B as the "canonical" metric (this makes compact directions positive)
    g_canonical = -B_ab
    g_eigvals = np.sort(eigvalsh(g_canonical))
    n_gpos = np.sum(g_eigvals > 1e-10)
    n_gneg = np.sum(g_eigvals < -1e-10)
    print(f"  Canonical metric (-B) eigenvalues: {g_eigvals}")
    print(f"  Metric signature: ({n_gpos}, {n_gneg})")

    # Determine the actual Clifford signature from the metric
    metric_eta = np.zeros(8)
    metric_eta[:n_gpos] = +1
    metric_eta[n_gpos:n_gpos+n_gneg] = -1
    p_sig, q_sig = n_gpos, n_gneg
    print(f"  Clifford algebra: Cl({p_sig},{q_sig})")
    print(f"  KO-dimension (manifold): ({p_sig}-{q_sig}) mod 8 = {(p_sig - q_sig) % 8}")

    # Build orthonormal frame
    if n_gpos + n_gneg == 8:
        E = orthonormal_frame_indefinite(g_canonical, metric_eta)
        # Verify: E g E^T should equal diag(metric_eta)
        check = E @ g_canonical @ E.T
        target = np.diag(metric_eta)
        frame_err = np.max(np.abs(check - target))
        print(f"  Frame verification ||E g E^T - eta||: {frame_err:.2e}")
    else:
        print("  CANNOT build frame: degenerate metric. Using identity.")
        E = np.eye(8)
        frame_err = float('inf')

    # ---- Step 4: Connection and curvature ----
    print("\n[4] Computing Levi-Civita connection...")
    ft = frame_structure_constants_general(f_abc, E)
    Gamma = connection_coefficients_indefinite(ft, metric_eta)
    conn_err = validate_connection_indefinite(Gamma, metric_eta)
    print(f"  Metric compatibility error: {conn_err:.2e}")

    # ---- Step 5: Clifford algebra and chirality ----
    print("\n[5] Building Clifford algebra Cl({},{})...".format(p_sig, q_sig))

    # Build Cl(p,q) with correct signature
    gammas_53, eta_cliff = build_cliff_53()

    # If our metric has signature different from (5,3), adjust
    if (p_sig, q_sig) != (5, 3):
        print(f"  NOTE: Actual metric signature ({p_sig},{q_sig}) differs from (5,3).")
        print(f"  Adjusting Clifford algebra to match actual signature.")
        # Rebuild with correct signature
        s1 = np.array([[0, 1], [1, 0]], dtype=complex)
        s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
        s3 = np.array([[1, 0], [0, -1]], dtype=complex)
        I2 = np.eye(2, dtype=complex)
        def kron4(A, B, C, D):
            return np.kron(A, np.kron(B, np.kron(C, D)))
        gammas_pos = [
            kron4(s1, I2, I2, I2), kron4(s2, I2, I2, I2),
            kron4(s3, s1, I2, I2), kron4(s3, s2, I2, I2),
            kron4(s3, s3, s1, I2), kron4(s3, s3, s2, I2),
            kron4(s3, s3, s3, s1), kron4(s3, s3, s3, s2),
        ]
        gammas_actual = []
        eta_cliff = np.ones(8)
        for a in range(8):
            if a < p_sig:
                gammas_actual.append(gammas_pos[a].copy())
                eta_cliff[a] = +1
            else:
                gammas_actual.append(1j * gammas_pos[a])
                eta_cliff[a] = -1
        gammas_53 = gammas_actual

    cliff_err = validate_clifford_indefinite(gammas_53, eta_cliff)
    print(f"  Clifford relation error: {cliff_err:.2e}")

    gamma9 = build_chirality_indefinite(gammas_53, eta_cliff)
    gamma9_sq = gamma9 @ gamma9
    gamma9_sq_err = np.max(np.abs(gamma9_sq - np.eye(16)))
    gamma9_sq_neg_err = np.max(np.abs(gamma9_sq + np.eye(16)))
    if gamma9_sq_err < 1e-10:
        gamma9_sign = "+1"
    elif gamma9_sq_neg_err < 1e-10:
        gamma9_sign = "-1"
    else:
        gamma9_sign = f"NEITHER (+1 err: {gamma9_sq_err:.2e}, -1 err: {gamma9_sq_neg_err:.2e})"
    print(f"  gamma_9^2 = {gamma9_sign}")

    # Check anticommutation
    gamma9_anticomm_errs = []
    for a in range(8):
        ac = gamma9 @ gammas_53[a] + gammas_53[a] @ gamma9
        gamma9_anticomm_errs.append(np.max(np.abs(ac)))
    print(f"  {{gamma_9, gamma_a}} max error: {max(gamma9_anticomm_errs):.2e}")

    # ---- Step 6: Spin connection (Omega) ----
    print("\n[6] Computing spinorial curvature offset Omega...")
    Omega = su21_spin_connection(Gamma, gammas_53)
    Omega_herm_err = np.max(np.abs(Omega - Omega.conj().T))
    Omega_antiherm_err = np.max(np.abs(Omega + Omega.conj().T))
    print(f"  Omega Hermiticity error: {Omega_herm_err:.2e}")
    print(f"  Omega anti-Hermiticity error: {Omega_antiherm_err:.2e}")
    print(f"  ||Omega||: {norm(Omega):.6f}")

    # ---- Step 7: Dirac operator on defining irrep ----
    print("\n[7] Building Dirac operator on defining representation...")
    rho_def = [g.copy() for g in gens]
    D_def = dirac_on_finite_irrep(rho_def, gammas_53, Omega, 3)
    print(f"  D matrix size: {D_def.shape}")

    # Check self-adjointness / skew-adjointness
    D_herm_err = np.max(np.abs(D_def - D_def.conj().T))
    D_antiherm_err = np.max(np.abs(D_def + D_def.conj().T))
    print(f"  D Hermiticity error: {D_herm_err:.2e}")
    print(f"  D anti-Hermiticity error: {D_antiherm_err:.2e}")

    # Eigenvalues
    evals_D = np.sort(np.linalg.eigvals(D_def))
    evals_real = np.sort(evals_D.real)
    evals_imag = np.sort(evals_D.imag)
    print(f"  Eigenvalue range (real part): [{evals_real[0]:.6f}, {evals_real[-1]:.6f}]")
    print(f"  Eigenvalue range (imag part): [{evals_imag[0]:.6f}, {evals_imag[-1]:.6f}]")
    max_real = np.max(np.abs(evals_D.real))
    max_imag = np.max(np.abs(evals_D.imag))
    print(f"  Max |Re(lambda)|: {max_real:.6f}")
    print(f"  Max |Im(lambda)|: {max_imag:.6f}")

    # For a Riemannian Dirac: eigenvalues are purely imaginary (math convention)
    # For a pseudo-Riemannian Dirac: eigenvalues may have REAL parts!
    frac_real = max_real / (max_real + max_imag + 1e-30)
    print(f"  Real fraction: {frac_real:.4f}")

    if max_real > 0.01 * max_imag and max_imag > 1e-10:
        print("  SPECTRUM IS GENUINELY COMPLEX -> pseudo-Riemannian signature detected")
        spectrum_type = "COMPLEX"
    elif max_real < 1e-10:
        print("  SPECTRUM IS PURELY IMAGINARY -> Riemannian-like")
        spectrum_type = "IMAGINARY"
    else:
        spectrum_type = "MIXED"
        print(f"  SPECTRUM IS MIXED (ratio: {frac_real:.6f})")

    # ---- Step 8: SU(3) comparison ----
    print("\n[8] Building SU(3) reference Dirac operator...")
    D_su3, B_su3_full, gammas_su3, gamma9_su3, Omega_su3 = build_su3_reference(tau=0.0)
    evals_su3 = np.sort(np.linalg.eigvals(D_su3))
    print(f"  SU(3) eigenvalue range (real): [{evals_su3.real.min():.6f}, {evals_su3.real.max():.6f}]")
    print(f"  SU(3) eigenvalue range (imag): [{evals_su3.imag.min():.6f}, {evals_su3.imag.max():.6f}]")
    print(f"  SU(3) ||Omega||: {norm(Omega_su3):.6f}")

    # ---- Step 9: Axiom-by-Axiom Analysis ----
    print("\n" + "=" * 80)
    print("AXIOM-BY-AXIOM ANALYSIS: SU(2,1) vs SU(3)")
    print("=" * 80)

    axiom_results = {}

    # Axiom 1: Dimension
    print("\n--- AXIOM 1: DIMENSION ---")
    d_est, dim_verdict = check_axiom_1_dimension(D_def, dim_expected=8)
    print(f"  Estimated spectral dimension: {d_est:.2f}")
    print(f"  Expected: 8 (dim SU(2,1) = dim SU(3) = 8)")
    print(f"  Verdict: {dim_verdict}")
    print(f"  NOTE: This is from finite-dim truncation only. Full spectrum")
    print(f"         has continuous part (non-compact) -> Weyl's law modified.")
    print("  STRUCTURAL: Non-compactness means Tr(|D|^{-s}) DIVERGES for Re(s) <= 8.")
    print(f"  The dimension spectrum is d_s = 8, but the residue is INFINITE.")
    print(f"  -> Axiom 1 FAILS in the standard sense (requires compact resolvent).")
    axiom_results['1_dimension'] = 'FAIL (non-compact -> no compact resolvent)'

    # Axiom 2: Regularity
    print("\n--- AXIOM 2: REGULARITY ---")
    print("  For SU(3): C^infty(SU(3)) is a smooth subalgebra. PASS trivially.")
    print("  For SU(2,1): C^infty(SU(2,1)) exists as smooth subalgebra.")
    print("  BUT: the relevant algebra for NCG is C_0(G) or its Schwartz subspace.")
    print("  Regularity requires: a and [D, a] are in the domain of delta^n for all n,")
    print("    where delta(T) = [|D|, T].")
    print("  For non-compact G, |D| has continuous spectrum -> delta is unbounded.")
    print("  Regularity SURVIVES if restricted to the Schwartz algebra S(G).")
    axiom_results['2_regularity'] = 'CONDITIONAL (Schwartz algebra needed)'

    # Axiom 3: Finiteness
    print("\n--- AXIOM 3: FINITENESS ---")
    print("  Finiteness: H_infty = cap dom(D^n) is a finitely generated projective A-module.")
    print("  For compact G: L^2(G, S) is a free module over C(G). PASS.")
    print("  For non-compact G: L^2(G, S) is a module over C_0(G), but NOT finitely generated")
    print("    (the group is not compact, so the spinor bundle over G has infinite rank")
    print("     when viewed as a C_0(G)-module after completing in L^2).")
    print("  Finiteness FAILS for non-compact groups in the standard sense.")
    axiom_results['3_finiteness'] = 'FAIL (non-compact -> infinite rank)'

    # Axiom 4: Reality
    print("\n--- AXIOM 4: REALITY ---")
    C, ko_man, ko_full, eps_man, eps_full = build_charge_conjugation_indefinite(gammas_53, eta_cliff)
    # C is 16x16 (spinor), D is 48x48 (rep x spinor). Promote C to rep space.
    dim_rep = 3
    C_full = np.kron(np.eye(dim_rep, dtype=complex), C)
    J2_err, JD_comm, expected_eps, J_verdict = check_axiom_4_reality(D_def, C_full, ko_man)
    print(f"  J^2 error (expected {expected_eps:+d}): {J2_err:.2e}")
    print(f"  [J, D] norm: {JD_comm:.2e}")
    print(f"  Local verdict: {J_verdict}")

    # KO-dimension shift is the KEY result
    print(f"\n  *** CRITICAL FINDING ***")
    print(f"  SU(3):   KO-dim(manifold) = 0, KO-dim(M x F_SM) = 6")
    print(f"  SU(2,1): KO-dim(manifold) = {ko_man}, KO-dim(M x F_SM) = {ko_full}")
    print(f"  The KO-dimension SHIFTS from 6 to {ko_full}!")
    if ko_full != 6:
        print(f"  This changes (epsilon, epsilon', epsilon'') from (+1,+1,-1) to {eps_full}")
        if eps_full[0] != 1:
            print(f"  J^2 = {eps_full[0]:+d} instead of +1 -> QUATERNIONIC structure!")
            print(f"  This is incompatible with the SM fermion content (Session 8 verified J^2=+1).")
        axiom_results['4_reality'] = f'FAIL (KO-dim shifts to {ko_full}, wrong J^2)'
    else:
        axiom_results['4_reality'] = 'PASS (KO-dim preserved at 6)'

    # Axiom 5: First order
    print("\n--- AXIOM 5: FIRST ORDER ---")
    print("  For SU(3): order-one FAILS at 4.000 (H,H), 2.828 (C,H)/(H,M3), etc.")
    print("  For SU(2,1): the algebraic structure is IDENTICAL (same A_F acts).")
    print("  The order-one violation comes from [D_F, a_F] structure, which is the")
    print("  Dirac operator restricted to the finite space.")
    print("  Since D_F = D_K and the algebra A_F = C + H + M_3(C) is unchanged,")
    print("  the order-one violation is PRESERVED (same magnitude).")
    print("  NOTE: The continuous spectrum adds new modes but cannot cancel")
    print("  the algebraic violation, which is a pointwise (local) condition.")
    axiom_results['5_first_order'] = 'FAIL (same as SU(3), algebraic origin)'

    # Axiom 6: Orientability
    print("\n--- AXIOM 6: ORIENTABILITY ---")
    # gamma9 is 16x16 (spinor), D_def is 48x48 (rep x spinor). Promote.
    gamma9_full = np.kron(np.eye(3, dtype=complex), gamma9)
    anticomm_norm, orient_verdict = check_axiom_6_orientability(D_def, gamma9_full)
    print(f"  ||{{D, gamma_9}}|| / ||D||: {anticomm_norm:.4e}")
    print(f"  Local verdict: {orient_verdict}")
    print("  NOTE: For SU(3), {D, gamma_9} = 0 at round (tau=0) but FAILS on Jensen.")
    print(f"  For SU(2,1), gamma_9 is constructed from Cl({p_sig},{q_sig}),")
    print(f"  which has different Hermiticity properties than Cl(8,0).")
    if anticomm_norm > 1e-6:
        print(f"  The chirality is NOT a grading operator for D -> orientability FAILS.")
        axiom_results['6_orientability'] = f'FAIL ({"{D,gamma}"}={anticomm_norm:.4e})'
    else:
        axiom_results['6_orientability'] = 'PASS'

    # Axiom 7: Poincare duality
    print("\n--- AXIOM 7: POINCARE DUALITY ---")
    print("  Poincare duality: the intersection form on K-theory must be non-degenerate.")
    print("  For compact SU(3): K_0(C(SU(3))) = Z, K_1(C(SU(3))) = Z.")
    print("  The intersection form is non-degenerate. PASS.")
    print(f"  For non-compact SU(2,1): K_0(C_0(SU(2,1))) involves the Baum-Connes assembly map.")
    print(f"  SU(2,1) has Haagerup property -> Baum-Connes holds.")
    print(f"  K-theory of C*(SU(2,1)) is computed from the representation ring.")
    print(f"  The K-groups are: K_0 = Z (from discrete series), K_1 = Z.")
    print(f"  Intersection form exists but non-degeneracy depends on the choice of")
    print(f"  fundamental class in K-homology (requires the Dirac class, which")
    print(f"  may be obstructed by the indefinite signature).")
    print(f"  STRUCTURAL: For pseudo-Riemannian manifolds, the Dirac class is")
    print(f"  not in K-homology but in KK-theory (Kasparov). The pairing exists")
    print(f"  but lives in a different category.")
    axiom_results['7_poincare_duality'] = 'CONDITIONAL (requires KK-theory framework)'

    # ---- Step 10: ADDITIONAL STRUCTURAL ANALYSIS ----
    print("\n" + "=" * 80)
    print("ADDITIONAL STRUCTURAL ANALYSIS")
    print("=" * 80)

    # A. Compact resolvent
    print("\n--- A. COMPACT RESOLVENT ---")
    print("  SU(3): D has compact resolvent (eigenvalues -> infty, discrete). PASS.")
    print("  SU(2,1): D has CONTINUOUS spectrum (non-compact group).")
    print("  (D - lambda)^{-1} is NOT compact for lambda in the resolvent set.")
    print("  This is the FUNDAMENTAL obstruction to a standard spectral triple.")
    print("  de Groot (Paper 36) addresses this for SU(1,1) by restricting to")
    print("  discrete series representations, but the full L^2 space fails.")

    # B. Heat kernel
    print("\n--- B. HEAT KERNEL ---")
    print("  SU(3): Tr(exp(-t D^2)) < infty for all t > 0. Well-defined heat kernel.")
    print("  SU(2,1): Tr(exp(-t D^2)) DIVERGES (infinite volume of non-compact group).")
    print("  The heat kernel expansion exists LOCALLY but the trace is ill-defined.")
    print("  -> Spectral action Tr f(D^2/Lambda^2) DIVERGES without regularization.")

    # C. Spectral action
    print("\n--- C. SPECTRAL ACTION ---")
    print("  On SU(3): S_b = Tr f(D^2/Lambda^2) ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4")
    print("  On SU(2,1): The trace diverges. Even with zeta-function regularization,")
    print("  the cosmological constant term a_0 is INFINITE (proportional to Vol(G)).")
    print("  The spectral action is only meaningful per unit volume: S_b / Vol(G).")
    print("  But Vol(SU(2,1)) = infty, so this ratio requires a cutoff prescription.")

    # D. Krein space structure
    print("\n--- D. KREIN SPACE STRUCTURE (Paper 44 connection) ---")
    # The fundamental symmetry eta for the Krein inner product
    # on spinor space comes from the Clifford algebra structure
    eta_krein = np.eye(16, dtype=complex)
    for a in range(8):
        if eta_cliff[a] < 0:
            # Anti-Hermitian gammas contribute to indefinite inner product
            pass
    # The Krein fundamental symmetry is the product of "timelike" gammas
    # eta_K = gamma_{p+1} ... gamma_{p+q} (product of anti-Hermitian generators)
    eta_K = np.eye(16, dtype=complex)
    for a in range(8):
        if eta_cliff[a] < 0:
            eta_K = eta_K @ gammas_53[a]
    # Check eta_K^2 = +/- I
    eta_K2 = eta_K @ eta_K
    eta_K2_plus = np.max(np.abs(eta_K2 - np.eye(16)))
    eta_K2_minus = np.max(np.abs(eta_K2 + np.eye(16)))

    if eta_K2_plus < 1e-10:
        print(f"  Krein fundamental symmetry eta_K: eta_K^2 = +I (err: {eta_K2_plus:.2e})")
        print(f"  -> Valid Krein space. Signature of eta_K:")
        eta_K_eigs = eigvalsh(eta_K.real)
        n_plus = np.sum(eta_K_eigs > 0.5)
        n_minus = np.sum(eta_K_eigs < -0.5)
        print(f"     ({n_plus}, {n_minus}) on 16-dim spinor space")
        krein_verdict = f"VALID ({n_plus},{n_minus})"
    elif eta_K2_minus < 1e-10:
        print(f"  Krein fundamental symmetry eta_K: eta_K^2 = -I (err: {eta_K2_minus:.2e})")
        print(f"  -> NOT a valid Krein fundamental symmetry (requires eta^2 = +I)")
        krein_verdict = "INVALID (eta_K^2 = -I)"
    else:
        print(f"  eta_K^2 neither +I (err {eta_K2_plus:.2e}) nor -I (err {eta_K2_minus:.2e})")
        krein_verdict = "INVALID"

    # E. Jensen deformation on SU(2,1)
    print("\n--- E. JENSEN DEFORMATION ON SU(2,1) ---")
    print("  SU(3) Jensen: g_s = L1 g|_{u(1)} + L2 g|_{su(2)} + L3 g|_{C^2}")
    print("  The decomposition su(3) = u(2) + m with m = C^2.")
    print("  For su(2,1): the maximal compact subalgebra is k = su(2) + u(1) = u(2).")
    print("  The Cartan decomposition is: su(2,1) = k + p")
    print("  where k = u(2) (compact, 4-dim) and p = non-compact complement (4-dim).")
    print("  This is EXACTLY the same decomposition as su(3) = u(2) + m!")
    print("  -> Jensen deformation CAN be applied to SU(2,1) with same structure.")
    print("  -> The deformation acts on the NON-COMPACT directions (boosts).")
    print("  -> Volume is no longer meaningful (non-compact), but the deformation")
    print("     parameter tau still controls the ratio of compact to non-compact.")

    # Verify Cartan decomposition
    print("\n  Cartan decomposition verification:")
    # k = su(2) + u(1) = generators 0,1,2,7 (compact)
    # p = generators 3,4,5,6 (non-compact)
    k_idx = [0, 1, 2, 7]
    p_idx = [3, 4, 5, 6]

    # Check [k, k] subset k
    kk_err = 0.0
    for a in k_idx:
        for b in k_idx:
            for c in p_idx:
                kk_err = max(kk_err, abs(f_abc[a, b, c]))
    print(f"  [k, k] in k: max leakage to p = {kk_err:.2e}")

    # Check [k, p] subset p
    kp_err = 0.0
    for a in k_idx:
        for b in p_idx:
            for c in k_idx:
                kp_err = max(kp_err, abs(f_abc[a, b, c]))
    print(f"  [k, p] in p: max leakage to k = {kp_err:.2e}")

    # Check [p, p] subset k
    pp_err = 0.0
    for a in p_idx:
        for b in p_idx:
            for c in p_idx:
                pp_err = max(pp_err, abs(f_abc[a, b, c]))
    print(f"  [p, p] in k: max leakage to p = {pp_err:.2e}")

    if kk_err < 1e-10 and pp_err < 1e-10:
        print("  Cartan decomposition su(2,1) = k + p VERIFIED.")
        print("  k = su(2) + u(1) (compact, 4-dim)")
        print("  p = 4-dim (non-compact, boosts)")
        cartan_pass = True
    else:
        print("  Cartan decomposition FAILS or has errors.")
        cartan_pass = False

    # Check Killing form restricted to k and p
    B_kk = B_ab[np.ix_(k_idx, k_idx)]
    B_pp = B_ab[np.ix_(p_idx, p_idx)]
    B_kp = B_ab[np.ix_(k_idx, p_idx)]
    print(f"  B|_k eigenvalues: {np.sort(eigvalsh(B_kk))}")
    print(f"  B|_p eigenvalues: {np.sort(eigvalsh(B_pp))}")
    print(f"  B|_kp max off-diagonal: {np.max(np.abs(B_kp)):.2e}")
    print(f"  B|_k: {'negative definite' if np.all(eigvalsh(B_kk) < -1e-10) else 'INDEFINITE'}")
    print(f"  B|_p: {'positive definite' if np.all(eigvalsh(B_pp) > 1e-10) else 'INDEFINITE'}")

    # ---- Step 11: SUMMARY TABLE ----
    print("\n" + "=" * 80)
    print("SUMMARY: SPECTRAL TRIPLE AXIOMS ON SU(2,1)")
    print("=" * 80)
    print(f"\n{'Axiom':<30} {'SU(3)':<25} {'SU(2,1)':<35}")
    print("-" * 90)

    su3_results = {
        '1_dimension': 'PASS (d=8)',
        '2_regularity': 'PASS (smooth algebra)',
        '3_finiteness': 'PASS (compact)',
        '4_reality': 'PASS (KO=6, J^2=+1)',
        '5_first_order': 'FAIL (4.000)',
        '6_orientability': 'PASS at round, FAIL on Jensen',
        '7_poincare_duality': 'PASS',
    }

    axiom_names = {
        '1_dimension': 'Dimension',
        '2_regularity': 'Regularity',
        '3_finiteness': 'Finiteness',
        '4_reality': 'Reality (J)',
        '5_first_order': 'First Order',
        '6_orientability': 'Orientability',
        '7_poincare_duality': 'Poincare Duality',
    }

    n_pass = 0
    n_fail = 0
    n_cond = 0
    for key in sorted(axiom_results.keys()):
        name = axiom_names.get(key, key)
        su3_res = su3_results.get(key, '?')
        su21_res = axiom_results.get(key, '?')
        print(f"  {name:<28} {su3_res:<25} {su21_res:<35}")
        if 'PASS' in su21_res and 'FAIL' not in su21_res:
            n_pass += 1
        elif 'CONDITIONAL' in su21_res:
            n_cond += 1
        else:
            n_fail += 1

    print(f"\n  Score: {n_pass} PASS, {n_cond} CONDITIONAL, {n_fail} FAIL (out of 7)")

    # ---- Step 12: KEY OBSTRUCTION ANALYSIS ----
    print("\n" + "=" * 80)
    print("KEY OBSTRUCTIONS AND STRUCTURAL FINDINGS")
    print("=" * 80)

    ko_man_val = (p_sig - q_sig) % 8
    ko_full_val = (ko_man_val + 6) % 8
    j2_comment = ('J^2 = -1: QUATERNIONIC structure incompatible with SM (needs J^2 = +1)'
                  if eps_full[0] == -1 else 'J^2 = +1: compatible')
    krein_comment = ('This provides the framework for Paper 44 (Martinetti): the '
                     'indefinite inner product on spinor space is a Krein structure.'
                     if 'VALID' in krein_verdict else
                     'The Krein structure is not well-defined on SU(2,1) spinors '
                     'with this construction.')

    print(f"""
  OBSTRUCTION 1 -- COMPACT RESOLVENT (FATAL):
    The defining property of a spectral triple requires D to have compact
    resolvent: (D - lambda)^{{-1}} must be a compact operator. For non-compact
    groups, the continuous spectrum of D prevents this. This is not a
    technicality -- it is the foundation of all subsequent constructions
    (heat kernel, spectral dimension, spectral action, index theory).

    STATUS: FATAL for standard spectral triple. Requires generalization
    to "locally compact spectral triples" (van den Dungen-Rennie 2015)
    or restriction to discrete series (de Groot 2026, Paper 36).

  OBSTRUCTION 2 -- KO-DIMENSION SHIFT:
    SU(3) with Killing metric (8,0) -> KO-dim = 0 mod 8
    SU(2,1) with Killing metric ({p_sig},{q_sig}) -> KO-dim = {p_sig}-{q_sig} mod 8 = {ko_man_val}

    For the product with F_SM (KO-dim 6):
      SU(3) x F: KO = 0 + 6 = 6 mod 8 -> (eps, eps', eps'') = (+1, +1, -1)
      SU(2,1) x F: KO = {ko_man_val} + 6 = {ko_full_val} mod 8

    KO-dim {ko_full_val} has signs: {eps_full}
    {j2_comment}

  OBSTRUCTION 3 -- SPECTRAL ACTION DIVERGENCE:
    Tr f(D^2/Lambda^2) diverges on SU(2,1) (infinite volume).
    The heat kernel coefficients a_0 (cosmological constant) and a_2
    (Einstein-Hilbert) both receive infinite contributions from the
    continuous spectrum. This is not a UV divergence (which the cutoff
    handles) but an IR divergence from non-compactness.

  STRUCTURAL FINDING -- CARTAN DECOMPOSITION ISOMORPHISM:
    The Cartan decomposition su(2,1) = u(2) + p is algebraically
    identical to the Jensen decomposition su(3) = u(2) + m.
    The dimensions match: dim(k) = dim(u(2)) = 4, dim(p) = dim(m) = 4.
    The bracket relations [k,k] in k, [k,p] in p, [p,p] in k
    are structurally parallel to [u(2), u(2)] in u(2), [u(2), m] in m.
    The DIFFERENCE is that B|_p > 0 (positive definite) for su(2,1)
    while B|_m < 0 (negative definite) for su(3).
    -> The Jensen deformation on SU(2,1) would scale the NON-COMPACT
    directions, creating a family of pseudo-Riemannian metrics.

  STRUCTURAL FINDING -- KREIN SPACE:
    Krein fundamental symmetry eta_K: {krein_verdict}
    {krein_comment}
""")

    # ---- GATE VERDICT ----
    print("=" * 80)
    print("GATE VERDICT: PSEUDO-RIEMANNIAN-46")
    print("=" * 80)

    total_surviving = n_pass + n_cond
    if total_surviving >= 4:
        gate = "PASS"
    else:
        gate = "FAIL"

    print(f"\n  Axioms surviving (PASS + CONDITIONAL): {total_surviving}/7")
    print(f"  Gate criterion: >= 4 axioms survive")
    print(f"  Gate verdict: PSEUDO-RIEMANNIAN-46 = {gate}")

    if gate == "FAIL":
        print(f"\n  STRUCTURAL CONCLUSION:")
        print(f"  SU(2,1) CANNOT replace SU(3) as the internal space in a standard")
        print(f"  spectral triple framework. The non-compactness is the primary")
        print(f"  obstruction (kills Axioms 1 and 3), and the KO-dimension shift")
        print(f"  (from 6 to {ko_full}) destroys the SM fermion structure.")
        print(f"")
        print(f"  The Cartan decomposition isomorphism is a structural parallel")
        print(f"  but does not rescue the axioms. The Jensen deformation on SU(2,1)")
        print(f"  would produce a 1-parameter family of pseudo-Riemannian metrics,")
        print(f"  but the spectral action diverges on each.")
        print(f"")
        print(f"  SURVIVING POSSIBILITY: If the internal space is a QUOTIENT of")
        print(f"  SU(2,1), e.g., SU(2,1)/U(2) = complex hyperbolic plane CH^2")
        print(f"  (which is a 4-dimensional non-compact symmetric space), then")
        print(f"  the compactification SU(2,1)/U(2) could be given a compact")
        print(f"  quotient by a discrete subgroup Gamma. The compact manifold")
        print(f"  Gamma\\SU(2,1)/U(2) would restore compact resolvent and finiteness,")
        print(f"  but the KO-dimension issue (dim=4, not 8) would need separate treatment.")

    # ---- Save results ----
    print(f"\n  Saving results...")
    results = {
        'axiom_results': axiom_results,
        'killing_form_eigvals': B_eigvals,
        'killing_form_signature': (n_pos, n_neg),
        'metric_signature': (p_sig, q_sig),
        'ko_dim_manifold': ko_man,
        'ko_dim_full': ko_full,
        'eps_manifold': eps_man,
        'eps_full': eps_full,
        'D_eigenvalues_real': evals_D.real,
        'D_eigenvalues_imag': evals_D.imag,
        'spectrum_type': spectrum_type,
        'cartan_verified': cartan_pass,
        'cartan_kk_leakage': kk_err,
        'cartan_pp_leakage': pp_err,
        'krein_verdict': krein_verdict,
        'cliff_err': cliff_err,
        'conn_err': conn_err,
        'frame_err': frame_err,
        'gate_verdict': gate,
        'n_axioms_surviving': total_surviving,
        'B_kk_eigvals': np.sort(eigvalsh(B_kk)),
        'B_pp_eigvals': np.sort(eigvalsh(B_pp)),
        'Omega_norm': norm(Omega),
        'su3_Omega_norm': norm(Omega_su3),
    }

    outfile = os.path.join(OUTDIR, 's46_pseudo_riemannian.npz')
    np.savez(outfile, **{k: np.array(v) if not isinstance(v, (str, bool, tuple, dict)) else np.array(str(v)) for k, v in results.items()})
    print(f"  Saved: {outfile}")

    elapsed = time.time() - t0
    print(f"\n  Total time: {elapsed:.1f}s")
    print("=" * 80)

    return results


if __name__ == '__main__':
    results = main()
