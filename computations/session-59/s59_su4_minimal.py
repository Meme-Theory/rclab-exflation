#!/usr/bin/env python3
"""
S59 SU(4) Minimal Viability Test (SU4-MINIMAL-59)
===================================================

Tests whether SU(4) satisfies three necessary conditions for the phonon-exflation
framework: (1) KO-dim = 6, (2) SM quantum numbers from branching, (3) van Hove
singularity in the Dirac spectrum.

SU(4): dim = 15, rank = 3, root system A_3.
Spinor space: Cliff(R^15) => dim = 2^7 = 128 (even dim=15, so 2^{floor(15/2)} = 128).

Wait: Cliff(R^n) for n odd has unique irrep of dim 2^{(n-1)/2}.
For n=15: 2^7 = 128. This is the correct spinor dimension.

The computation follows the SU(3) pipeline in dirac_spectrum.py but generalized
to SU(4).

Author: Baptista Spacetime Analyst (Session 59)
Date: 2026-03-24

Pre-registered gate: SU4-MINIMAL-59
  PASS: All three conditions met (KO-dim = 6, SM quantum numbers, van Hove fold)
  FAIL: KO-dim != 6 or SM quantum numbers absent
  INFO: KO-dim = 6 but SM quantum numbers differ, or computation incomplete
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, eigvals, cholesky, inv, norm
import sys
import os
import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# Add computation paths
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, str(_x2_shared_dir()))

from canonical_constants import *

# =============================================================================
# SECTION 1: SU(4) LIE ALGEBRA — 15 GENERATORS
# =============================================================================

def su4_generators():
    """
    Construct 15 anti-Hermitian generators of su(4) in the fundamental (4x4) rep.

    Convention: e_a = -i/2 * Lambda_a, where Lambda_a are the Gell-Mann-like
    generalized matrices for SU(4).

    Normalization: Tr(e_a e_b) = -1/2 delta_{ab}.

    The 15 generators span:
    - 3 diagonal (Cartan subalgebra): lambda_3, lambda_8, lambda_15
    - 12 off-diagonal (root vectors)

    Construction: SU(4) generalized Gell-Mann matrices.
    For SU(N), the generators are:
    - Symmetric off-diagonal: (E_{ij} + E_{ji}) for i < j
    - Antisymmetric off-diagonal: -i(E_{ij} - E_{ji}) for i < j
    - Diagonal: normalized from first k+1 entries

    Returns:
        list of 15 complex (4,4) anti-Hermitian matrices
    """
    N = 4
    lambdas = []

    # Off-diagonal generators (symmetric and antisymmetric)
    for i in range(N):
        for j in range(i + 1, N):
            # Symmetric: (E_ij + E_ji)
            lam_s = np.zeros((N, N), dtype=complex)
            lam_s[i, j] = 1.0
            lam_s[j, i] = 1.0
            lambdas.append(lam_s)

            # Antisymmetric: -i(E_ij - E_ji)
            lam_a = np.zeros((N, N), dtype=complex)
            lam_a[i, j] = -1j
            lam_a[j, i] = 1j
            lambdas.append(lam_a)

    # Diagonal generators
    for k in range(1, N):
        lam_d = np.zeros((N, N), dtype=complex)
        norm_factor = np.sqrt(2.0 / (k * (k + 1)))
        for i in range(k):
            lam_d[i, i] = norm_factor
        lam_d[k, k] = -k * norm_factor
        lambdas.append(lam_d)

    assert len(lambdas) == N**2 - 1, f"Expected {N**2-1} generators, got {len(lambdas)}"

    # Verify trace normalization: Tr(Lambda_a Lambda_b) = 2 delta_{ab}
    for a in range(len(lambdas)):
        for b in range(len(lambdas)):
            tr = np.trace(lambdas[a] @ lambdas[b]).real
            expected = 2.0 if a == b else 0.0
            assert abs(tr - expected) < 1e-12, \
                f"Tr(Lambda_{a} Lambda_{b}) = {tr}, expected {expected}"

    # Anti-Hermitian generators: e_a = -i/2 * Lambda_a
    # Normalization: Tr(e_a e_b) = Tr((-i/2 Lambda_a)(-i/2 Lambda_b))
    #              = -1/4 Tr(Lambda_a Lambda_b) = -1/4 * 2 delta_{ab} = -1/2 delta_{ab}
    gens = [-1j / 2.0 * lam for lam in lambdas]

    return gens


def compute_structure_constants_general(gens):
    """
    Compute structure constants f_{abc} from [e_a, e_b] = f_{abc} e_c.
    Uses trace formula: f_{abc} = -2 Tr([e_a, e_b] e_c).

    Args:
        gens: list of n anti-Hermitian matrices
    Returns:
        f_abc: real (n, n, n) array
    """
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a + 1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                val = -2.0 * np.trace(comm @ gens[c])  # (local)
                f[a, b, c] = val.real
                f[b, a, c] = -val.real
    return f


def compute_killing_form_general(f_abc):
    """Killing form B_{ab} = sum_{c,d} f_{acd} f_{bcd}."""
    return np.einsum('acd,bcd->ab', f_abc, f_abc)


# =============================================================================
# SECTION 2: ROOT SYSTEM AND WEYL GROUP
# =============================================================================

def analyze_root_system(gens, f_abc):
    """
    Analyze the root system of su(4) = A_3.

    Identify:
    - Cartan subalgebra (maximal torus)
    - Roots and root vectors
    - Weyl group order

    For A_3: rank = 3, |W| = 4! = 24, #roots = 12, dim = 15 = 12 + 3.
    """
    n = len(gens)
    N = 4  # SU(4)

    # Killing form
    B = compute_killing_form_general(f_abc)

    # The Cartan generators are the diagonal ones (indices 12, 13, 14 in our ordering)
    # In our ordering: first 12 are off-diagonal (6 pairs), then 3 diagonal
    # Check: diagonal generators are at indices n-3, n-2, n-1 = 12, 13, 14

    # Find Cartan generators by checking commutativity
    # Diagonal generators should commute with each other
    cartan_indices = []
    for a in range(n):
        is_diag = True
        # Check if generator is diagonal (real diagonal matrix)
        mat = gens[a]
        off_diag = np.max(np.abs(mat - np.diag(np.diag(mat))))
        if off_diag < 1e-12:
            cartan_indices.append(a)

    rank = len(cartan_indices)

    # Compute roots: eigenvalues of ad(H_i) on root spaces
    # For each Cartan generator H_i, compute ad(H_i) on the Lie algebra
    # Root vectors are common eigenvectors of all ad(H_i)

    # Build adjoint action of Cartan generators
    ad_H = []
    for idx in cartan_indices:
        ad = np.zeros((n, n), dtype=complex)
        for b in range(n):
            for c in range(n):
                ad[c, b] = f_abc[idx, b, c]
        ad_H.append(ad)

    # Simultaneous diagonalization of Cartan adjoint actions
    # Since they commute, they can be simultaneously diagonalized
    # Compute eigenvalues of ad(H_1) first

    roots = []
    root_vectors = []

    # Use simultaneous eigenvalue approach
    # For each non-Cartan generator direction, compute the root
    for a in range(n):
        if a in cartan_indices:
            continue
        root = []
        for idx in cartan_indices:
            # [H_i, e_a] = sum_c f_{i,a,c} e_c
            # If e_a is a root vector, [H_i, e_a] = alpha_i e_a
            # So f_{i,a,a} should give the root component... but only for
            # actual root vectors, not linear combinations.
            # Better: compute eigenvalues directly
            pass
        root_vec = np.array([f_abc[idx, a, a] for idx in cartan_indices])
        # This is only correct if e_a happens to be a root vector already
        # For our construction, the off-diagonal generators ARE root vectors
        roots.append(root_vec)

    # For SU(4), the 12 off-diagonal generators correspond to 6 positive and 6 negative roots
    # Actually, our generators come in pairs (symmetric, antisymmetric) for each (i,j) pair
    # The root vectors are e_{ij} = (symmetric - i*antisymmetric)/2 and conjugate

    # Instead of the above (which is fragile), let's compute roots properly
    # via the weight system of the adjoint representation

    # Build the Cartan matrix of ad(H) on the full algebra
    # Use the complexified approach: find eigenvectors of ad(H_1)

    results = {
        'rank': rank,
        'cartan_indices': cartan_indices,
        'killing_form': B,
        'dim': n,
        'n_roots_expected': n - rank,  # 12 for A_3
        'weyl_order_expected': 24,  # |S_4| = 24
        'root_system': 'A_3',
    }

    # Verify Killing form eigenvalues
    B_evals = eigvalsh(B)
    results['killing_eigenvalues'] = B_evals

    # For su(4), B_{ab} = -C delta_{ab} with C = 2*N = 8
    # (with our normalization Tr(e_a e_b) = -1/2 delta_{ab})
    # Actually: B_{ab} = sum f_{acd} f_{bcd}. For su(N) with Tr(T_a T_b) = 1/2 delta,
    # the structure constants give f_{abc} f_{abc} = 2N for each pair.
    # With our normalization: f_{abc} with Tr = -1/2, the Killing form
    # B_{ab} = -N delta_{ab} for su(N).
    # For SU(4): B_{ab} = -4 * delta_{ab}... let me check with the Casimir eigenvalue.
    # C_2(adj) for A_3 = N = 4. With Tr(e_a e_b) = -1/2 delta,
    # B_{ab} = -2*N * delta_{ab} = -8 delta_{ab}.
    # Hmm, let me just check numerically.
    results['killing_diagonal'] = B[0, 0]

    return results


# =============================================================================
# SECTION 3: JENSEN-LIKE METRIC ON SU(4)
# =============================================================================

def su4_decomposition_indices():
    """
    Decomposition su(4) = su(3) + u(1) + C^3 + (C^3)^*

    Under SU(3) x U(1) maximal subgroup:
    - su(3): generators acting within the upper-left 3x3 block (8 generators)
    - u(1): the diagonal generator proportional to diag(1,1,1,-3) (1 generator)
    - C^3: off-diagonal generators connecting 3 <-> 1 (6 generators = 3 complex dims)

    Total: 8 + 1 + 6 = 15. Check.

    In our generator ordering:
    - Off-diagonal generators are ordered by (i,j) pairs:
      (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
      Each pair has 2 generators (symmetric, antisymmetric), giving indices:
      (0,1): 0,1  (0,2): 2,3  (0,3): 4,5  (1,2): 6,7  (1,3): 8,9  (2,3): 10,11
    - Diagonal generators: 12, 13, 14

    su(3) generators: those acting within {0,1,2} block
      = (0,1): 0,1  (0,2): 2,3  (1,2): 6,7  plus diag_1: 12, diag_2: 13
      Total: 8 generators. Check.

    u(1) generator: diag_3 = 14 (proportional to diag(1,1,1,-3))

    C^3 generators: those connecting {0,1,2} with {3}
      = (0,3): 4,5  (1,3): 8,9  (2,3): 10,11
      Total: 6 generators. Check.
    """
    SU3_IDX = [0, 1, 2, 3, 6, 7, 12, 13]  # su(3) subalgebra (8 generators)
    U1_IDX = [14]  # u(1) factor (1 generator)
    C3_IDX = [4, 5, 8, 9, 10, 11]  # C^3 coset (6 generators)

    STABILIZER_IDX = SU3_IDX + U1_IDX  # su(3) + u(1) = u(3) stabilizer (9 generators)
    COSET_IDX = C3_IDX  # complement (6 generators)

    return {
        'su3': SU3_IDX,
        'u1': U1_IDX,
        'c3': C3_IDX,
        'stabilizer': STABILIZER_IDX,
        'coset': COSET_IDX,
    }


def jensen_metric_su4(B_ab, tau):
    """
    Construct a Jensen-like deformed metric on SU(4).

    Decomposition: su(4) = u(3) + C^3
    with u(3) = su(3) + u(1) as the stabilizer of SU(3) x U(1) subset SU(4).

    Metric: g(tau) = L_stab * g_0|_{u(3)} + L_coset * g_0|_{C^3}

    For volume-preserving: L_stab^{9/2} * L_coset^{6/2} = 1
    i.e., L_stab^{9} * L_coset^{6} = 1 (exponents = dimensions of subspaces)

    Wait, the volume is det(g)^{1/2}. For a diagonal metric:
    Vol ~ product of sqrt(g_{aa}) = product of L_a^{1/2}
    So Vol ~ L_stab^{9/2} * L_coset^{6/2} where 9 and 6 are the multiplicities.

    Volume-preserving Jensen curve: L_stab = exp(2*alpha*tau), L_coset = exp(2*beta*tau)
    with 9*alpha + 6*beta = 0, so beta = -3*alpha/2.

    Choose alpha = 1: L_stab = exp(2*tau), L_coset = exp(-3*tau).
    Check: 9*(2*tau) + 6*(-3*tau) = 18*tau - 18*tau = 0. Volume-preserving.

    This is the direct analog of the SU(3) Jensen metric where:
    su(3) = u(2) + C^2, L_{u2} = exp(-2s), L_{C2} = exp(s), with 4*(-2s)+4*(s) = ...
    Actually SU(3) Jensen uses L1*L2^3*L3^4 = 1.

    For SU(4) we want a one-parameter family. Let me parameterize as:
    L_stab = exp(2*a*tau), L_coset = exp(-3*a*tau)
    with a chosen so that tau = 0.19 gives comparable deformation to SU(3).

    For simplicity, set a = 1 (can always rescale tau).

    Args:
        B_ab: (15,15) Killing form
        tau: deformation parameter
    Returns:
        g: (15,15) positive definite metric
    """
    decomp = su4_decomposition_indices()

    g0 = np.abs(B_ab)  # Positive definite base metric
    g = np.zeros_like(g0)

    L_stab = np.exp(2.0 * tau)
    L_coset = np.exp(-3.0 * tau)

    # Stabilizer block (u(3) = su(3) + u(1))
    for a in decomp['stabilizer']:
        for b in decomp['stabilizer']:
            g[a, b] = g0[a, b] * L_stab

    # Coset block (C^3)
    for a in decomp['coset']:
        for b in decomp['coset']:
            g[a, b] = g0[a, b] * L_coset

    return g


def verify_volume_preserving(tau):
    """Verify the volume factor is 1."""
    L_stab = np.exp(2.0 * tau)
    L_coset = np.exp(-3.0 * tau)
    # 9 stabilizer directions, 6 coset directions
    vol = L_stab**(9.0/2) * L_coset**(6.0/2)
    return vol


# =============================================================================
# SECTION 4: CLIFFORD ALGEBRA Cl(R^15)
# =============================================================================

def build_cliff15():
    """
    Construct generators gamma_1, ..., gamma_15 of Cliff(R^15).

    For n = 15 (odd), the unique irreducible representation has dimension
    2^{(n-1)/2} = 2^7 = 128.

    Construction via tensor products of Pauli matrices.
    For n = 2k generators, we build 2^k-dim matrices:
      gamma_{2j-1} = sigma_3^{j-1} tensor sigma_1 tensor I^{k-j}
      gamma_{2j}   = sigma_3^{j-1} tensor sigma_2 tensor I^{k-j}

    For n = 15 = 2*7 + 1, we first build 14 generators (dim 2^7 = 128),
    then the 15th is gamma_15 = i^7 * gamma_1 * ... * gamma_14.

    Wait: for Cliff(R^{2k}), dim = 2^k. For Cliff(R^{2k+1}), the irrep is still 2^k.
    The extra generator is gamma_{2k+1} = c * gamma_1 * ... * gamma_{2k}
    where c is chosen to get gamma_{2k+1}^2 = +I.

    For R^{2k}: chirality = i^k * gamma_1 ... gamma_{2k}, satisfies chi^2 = I.
    For R^{2k+1}: gamma_{2k+1} = i^k * gamma_1 ... gamma_{2k} = chirality of R^{2k}.
    Then gamma_{2k+1}^2 = I and {gamma_{2k+1}, gamma_j} = 0 for j <= 2k.

    For n=15, k=7: build 14 generators in 128 dim, then gamma_15 = i^7 * prod(gamma_1..14).

    Returns:
        gammas: list of 15 Hermitian (128, 128) complex matrices
    """
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    k = 7  # 2k = 14 generators first, then 15th from chirality
    dim = 2**k  # 128

    gammas = []

    for j in range(1, k + 1):
        # gamma_{2j-1} = sigma_3^{(j-1)} tensor sigma_1 tensor I^{(k-j)}
        # gamma_{2j}   = sigma_3^{(j-1)} tensor sigma_2 tensor I^{(k-j)}

        parts_1 = []
        parts_2 = []
        for m in range(k):
            if m < j - 1:
                parts_1.append(s3)
                parts_2.append(s3)
            elif m == j - 1:
                parts_1.append(s1)
                parts_2.append(s2)
            else:
                parts_1.append(I2)
                parts_2.append(I2)

        # Build tensor product
        mat_1 = parts_1[0]
        mat_2 = parts_2[0]
        for m in range(1, k):
            mat_1 = np.kron(mat_1, parts_1[m])
            mat_2 = np.kron(mat_2, parts_2[m])

        gammas.append(mat_1)
        gammas.append(mat_2)

    assert len(gammas) == 14, f"Built {len(gammas)} generators, expected 14"

    # 15th generator: gamma_15 = i^k * gamma_1 * ... * gamma_14
    # i^7 = i^4 * i^3 = 1 * (-i) = -i
    chi = np.eye(dim, dtype=complex)
    for g in gammas:
        chi = chi @ g
    gamma_15 = (1j)**k * chi  # i^7 = -i
    gammas.append(gamma_15)

    return gammas


def validate_clifford_general(gammas, tol=1e-10):
    """Verify {gamma_a, gamma_b} = 2 delta_{ab} I."""
    n = len(gammas)
    dim = gammas[0].shape[0]
    max_err = 0.0  # (local)
    for a in range(n):
        for b in range(a, n):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(dim, dtype=complex)
            err = np.max(np.abs(anticomm - target))
            max_err = max(max_err, err)
    return max_err


# =============================================================================
# SECTION 5: KO-DIMENSION ANALYSIS
# =============================================================================

def check_ko_dimension(gammas, dim_algebra):
    """
    Check KO-dimension for the spectral geometry on SU(4).

    The KO-dimension n mod 8 determines the signs:
      J^2 = epsilon, JD = epsilon' DJ, Jgamma = epsilon'' gamma J

    Table (Connes):
      n mod 8: 0  1  2  3  4  5  6  7
      epsilon: +  +  -  -  -  -  +  +
      epsilon':-  +  +  +  -  +  +  +  (for even dim; odd dim has no gamma)
      epsilon'':+  -  +  -  (for even n only)

    Wait, KO-dim = 6 requires: J^2 = +1, JD = DJ, Jgamma = -gamma J.

    Actually, for n=6: epsilon = +1, epsilon' = +1, epsilon'' = -1.

    For a compact Lie group G of dimension d:
    - The manifold M = G is d-dimensional
    - The spin structure exists if G is simply connected (SU(N) is)
    - KO-dim = d mod 8

    For SU(4): dim = 15, so KO-dim = 15 mod 8 = 7.

    BUT: this is the KO-dim of the MANIFOLD. In the framework, we care about
    the FINITE SPECTRAL TRIPLE associated with the internal space.

    In NCG, the product geometry M4 x F has KO-dim = (4 + n_F) mod 8.
    For the SM: KO-dim(F) = 6, so total = (4 + 6) mod 8 = 2.

    For the internal space G, the relevant KO-dim depends on what role G plays.
    If G = SU(4) is the internal space in M4 x SU(4), then:
    KO-dim(internal) = dim(G) mod 8 = 15 mod 8 = 7.

    For the product: (4 + 7) mod 8 = 3.

    Alternatively, in the Kaluza-Klein picture a la Baptista, the relevant
    quantity is the KO-dim of the TOTAL space. For M4 x G:
    KO-dim(total) = 4 + dim(G) = 4 + 15 = 19 => 19 mod 8 = 3.

    For M4 x SU(3): 4 + 8 = 12 => 12 mod 8 = 4. But the framework established
    KO-dim = 6 for M4 x SU(3) through a different route (the finite spectral triple).

    Let me think more carefully. The KO-dim = 6 for SU(3) was established in
    Sessions 7-8 NOT as dim(SU(3)) mod 8 (which would be 0), but through the
    structure of the finite spectral triple (A_F, H_F, D_F, J_F, gamma_F).

    The relevant question is: what is the KO-dim of the SPECTRAL GEOMETRY
    on G, treated as a Riemannian manifold with its spin structure?

    For a spin manifold of dimension d:
    - If d is even: there is a Z/2 grading gamma (chirality) and J (charge conjugation)
    - If d is odd: there is J but NO grading gamma

    For d = 15 (odd): KO-dim = 15 mod 8 = 7.
    Signs: J^2 = +1, JD = DJ (no gamma since d is odd).

    For d = 8 (even, SU(3)): KO-dim = 8 mod 8 = 0.
    Signs: J^2 = +1, Jgamma = +gamma J, JD = -DJ.

    BUT WAIT: KO-dim = 0 for SU(3) as a manifold is NOT the same as the
    KO-dim = 6 that was established for the framework. The KO-dim = 6 comes
    from the FINITE spectral triple in the NCG product, not from the manifold.

    So the question is really: can we build a finite spectral triple with
    KO-dim = 6 from SU(4) structure?

    In the Chamseddine-Connes approach:
    - A_F = C + H + M_3(C) gives the SM with KO-dim(F) = 6
    - A_F = H_R + H_L + M_4(C) gives Pati-Salam with KO-dim(F) = 6

    Both have KO-dim(F) = 6 by construction! The Pati-Salam model uses SU(4)
    and still achieves KO-dim = 6 because the finite spectral triple is designed
    to have the right signs.

    So the answer is: KO-dim = 6 is achievable with SU(4), because the
    Chamseddine-Connes-van Suijlekom spectral Pati-Salam model explicitly
    does this. The KO-dim is a property of the finite spectral triple (A_F, H_F, D_F),
    not of the Lie group manifold.

    For our framework (Baptista's KK approach), the situation is different.
    The internal space IS the Lie group manifold. KO-dim is then dim(G) mod 8:
    - SU(3): 8 mod 8 = 0
    - SU(4): 15 mod 8 = 7

    The framework's KO-dim = 6 was achieved NOT from 8 mod 8 = 0, but from
    the structure of the spinor representation on SU(3). Let me check this
    by computing the J and gamma operators directly.

    For a spin manifold of even dimension d = 2m:
    gamma = i^m * gamma_1 * ... * gamma_d (chirality, gamma^2 = 1, {gamma, D} = 0)
    J = C * complex_conjugation (charge conjugation, C is a matrix)

    For d = 15 (odd): NO chirality operator. The Clifford algebra Cl(15) has a
    single irrep of dim 128. There is no Z/2 grading.

    This means: epsilon'' (the sign in J*gamma = epsilon'' * gamma * J) does not
    exist because gamma does not exist.

    For the framework's KO-dim = 6 condition (J^2 = +1, Jgamma = -gamma*J, JD = DJ),
    the Jgamma = -gamma*J condition REQUIRES gamma to exist. Since dim(SU(4)) = 15
    is odd, there is no gamma, and KO-dim = 6 CANNOT be satisfied in the same way.

    This is a STRUCTURAL obstruction.

    However, we should still compute what we can. The J operator exists:
    For Cliff(R^n), the charge conjugation operator B satisfies:
    B * gamma_a * B^{-1} = +-gamma_a^T

    For n = 15 mod 8 = 7: B * gamma_a * B^{-1} = +gamma_a^T (B-type)
    and J = B * K (K = complex conjugation), J^2 = +1.
    JD = DJ (epsilon' = +1 for n mod 8 = 7).

    So for d = 15: J^2 = +1, JD = +DJ. But no gamma.
    KO-dim = 7 (NOT 6).

    Args:
        gammas: Clifford generators
        dim_algebra: dimension of the Lie algebra

    Returns:
        dict with KO-dim analysis
    """
    d = dim_algebra
    dim_spin = gammas[0].shape[0]

    ko_manifold = d % 8
    is_even = (d % 2 == 0)

    # Charge conjugation signs from the table
    # n mod 8:  0  1  2  3  4  5  6  7
    # J^2:      +  +  -  -  -  -  +  +
    epsilon_table = {0: +1, 1: +1, 2: -1, 3: -1, 4: -1, 5: -1, 6: +1, 7: +1}
    # JD = eps' DJ
    # n mod 8: 0  1  2  3  4  5  6  7
    epsprime_table = {0: +1, 1: -1, 2: +1, 3: +1, 4: +1, 5: -1, 6: +1, 7: +1}
    # Jgamma = eps'' gamma J (only for even d)
    # n mod 8: 0  2  4  6
    epsdp_table = {0: +1, 2: -1, 4: -1, 6: +1}

    epsilon = epsilon_table[ko_manifold]
    epsilon_prime = epsprime_table[ko_manifold]

    results = {
        'dim': d,
        'dim_spin': dim_spin,
        'ko_manifold': ko_manifold,
        'is_even': is_even,
        'has_chirality': is_even,
        'J_squared': epsilon,
        'JD_sign': epsilon_prime,
    }

    if is_even:
        m = d // 2
        results['chirality_sign'] = epsdp_table[ko_manifold]
        results['J_gamma_sign'] = epsdp_table[ko_manifold]
    else:
        results['chirality_sign'] = None
        results['J_gamma_sign'] = None

    # For KO-dim = 6 we need: J^2 = +1, JD = +DJ, Jgamma = -gamma*J
    ko6_check = {
        'J_sq_match': (epsilon == +1),
        'JD_match': (epsilon_prime == +1),
        'Jgamma_match': (results.get('J_gamma_sign') == -1) if is_even else False,
        'Jgamma_exists': is_even,
    }
    results['ko6_check'] = ko6_check
    results['ko6_pass'] = all([ko6_check['J_sq_match'], ko6_check['JD_match'],
                                ko6_check['Jgamma_match']])

    return results


# =============================================================================
# SECTION 6: SM QUANTUM NUMBERS FROM BRANCHING
# =============================================================================

def branching_su4_to_su3_u1(gens, f_abc):
    """
    Decompose SU(4) representations under SU(3) x U(1).

    SU(4) -> SU(3) x U(1): the fundamental 4 decomposes as
      4 = 3_{+1} + 1_{-3}

    where the subscript is the U(1) charge (with normalization convention).

    Key branching rules for SM content:

    Adjoint (15):
      15 = 8_0 + 3_{+4} + 3bar_{-4} + 1_0
      (In Pati-Salam: gluons + leptoquark gauge bosons + B-L gauge boson)

    Fundamental (4):
      4 = 3_{+1} + 1_{-3}
      (quark triplet + lepton singlet)

    Anti-fundamental (4bar):
      4bar = 3bar_{-1} + 1_{+3}

    6 = Lambda^2(4):
      6 = 3_{+2} + 3bar_{-2}

    10 = Sym^2(4):
      10 = 6_{+2} + 3_{-2} + 1_{-6}

    Spinor representation (the NCG finite Hilbert space):
    In Pati-Salam, fermions are in (2_L, 1_R, 4) + (1_L, 2_R, 4) = 4+4 = 8
    Per family: 16 Weyl fermions total.

    Under SU(4) -> SU(3) x U(1):
    - (u_L^{1,2,3}, nu_L) -> 3_{+1} + 1_{-3} from the (2_L, 1_R, 4)
    - (d_L^{1,2,3}, e_L) -> 3_{+1} + 1_{-3} from the other component
    - (u_R^{1,2,3}, nu_R) -> 3_{+1} + 1_{-3}
    - (d_R^{1,2,3}, e_R) -> 3_{+1} + 1_{-3}

    So: all quarks are color triplets, all leptons are color singlets.
    This IS the SM quantum number structure (with right-handed neutrinos).

    The crucial point: SU(4) treats lepton number as the fourth color
    (Pati-Salam lepton-quark unification). Under SU(3)_color x U(1)_{B-L}:
    quarks carry B = 1/3, leptons carry L = 1.

    Returns:
        dict with branching analysis
    """
    # Compute U(1) charges of the fundamental under SU(3) x U(1) decomposition
    # The U(1) generator is (up to normalization) diag(1, 1, 1, -3)/sqrt(24)
    # In our basis, this is generator index 14 (the last diagonal generator)

    N = 4
    decomp = su4_decomposition_indices()
    u1_gen = gens[decomp['u1'][0]]  # The U(1) generator

    # Diagonalize u1_gen on the fundamental representation
    u1_matrix = u1_gen  # 4x4 matrix
    u1_eigenvalues = np.linalg.eigvalsh(1j * u1_matrix)  # -i * (anti-Hermitian) is Hermitian
    u1_eigenvalues = np.sort(u1_eigenvalues)

    # Check: should be proportional to (+1, +1, +1, -3)
    # The actual eigenvalues of i*e_15 where e_15 = -i/2 * Lambda_15
    # Lambda_15 = sqrt(2/(3*4)) * diag(1,1,1,-3) = (1/sqrt(6)) * diag(1,1,1,-3)
    # So e_15 = -i/(2*sqrt(6)) * diag(1,1,1,-3)
    # i * e_15 = 1/(2*sqrt(6)) * diag(1,1,1,-3)
    # Eigenvalues: 1/(2*sqrt(6)) * (1, 1, 1, -3)

    results = {
        'u1_eigenvalues_fund': u1_eigenvalues,
        'u1_generator_index': decomp['u1'][0],
    }

    # Branching of fundamental: 4 -> 3 + 1
    # Under SU(3): first 3 components form a triplet, 4th is a singlet
    # U(1) charges: triplet has charge +q, singlet has charge -3q (where q = 1/(2*sqrt(6)))

    q = u1_eigenvalues[0]  # charge of the triplet
    q_singlet = u1_eigenvalues[-1]  # charge of the singlet

    results['fundamental_branching'] = {
        'triplet_charge': q,
        'singlet_charge': q_singlet,
        'ratio': q_singlet / q if abs(q) > 1e-15 else None,
        'expected_ratio': -3.0,  # Pati-Salam: singlet charge = -3 * triplet charge
    }

    # SM quantum numbers check
    # In Pati-Salam SU(4)_C, the branching gives:
    # - quarks = color triplets (3 of SU(3))
    # - leptons = color singlets (1 of SU(3))
    # - B-L quantum number = U(1) charge (up to normalization)

    # The SM requires:
    # 1. Color SU(3) with quarks as triplets -> YES (from branching)
    # 2. Electroweak SU(2)_L x U(1)_Y -> NOT from SU(4) alone
    #    (needs the SU(2)_L x SU(2)_R factor from the full Pati-Salam group)
    # 3. Hypercharge Y = I_{3R} + (B-L)/2 -> requires both SU(2)_R and U(1)_{B-L}

    results['sm_content'] = {
        'color_triplet_quarks': True,
        'color_singlet_leptons': True,
        'BL_quantum_number': True,
        'full_SM_from_SU4_alone': False,  # Need SU(2)_L x SU(2)_R in addition
        'pati_salam_viable': True,
        'lepton_as_4th_color': True,
    }

    # Adjoint decomposition: 15 -> 8 + 3 + 3bar + 1
    # This contains: gluons (8), leptoquark bosons (3 + 3bar), B-L boson (1)

    # Build adjoint representation and decompose under U(1)
    rho_adj = []
    for a in range(15):
        M = np.zeros((15, 15), dtype=complex)
        for b in range(15):
            for c in range(15):
                M[c, b] = f_abc[a, b, c]
        rho_adj.append(M)

    # U(1) charges of adjoint
    u1_adj = rho_adj[decomp['u1'][0]]
    u1_adj_evals = eigvalsh(1j * u1_adj)
    u1_adj_evals_sorted = np.sort(u1_adj_evals)

    # Group by charge
    tol = 1e-10  # (local)
    charge_groups = {}
    for ev in u1_adj_evals_sorted:
        found = False
        for key in charge_groups:
            if abs(ev - key) < tol:
                charge_groups[key] += 1
                found = True
                break
        if not found:
            charge_groups[ev] = 1

    results['adjoint_branching'] = {
        'charge_multiplicities': {f"{k:.6f}": v for k, v in sorted(charge_groups.items())},
        'expected': '8_0 + 3_{+q} + 3bar_{-q} + 1_0 -> charges 0(9), +q(3), -q(3)',
    }

    # The spinor of the Dirac operator on SU(4): Cliff(R^15), dim = 128
    # Under SU(3) x U(1), this 128-dim spinor representation decomposes.
    # This is a DIFFERENT question from the NCG finite Hilbert space.
    #
    # In the Baptista KK framework, the internal spinor space IS the
    # spinor bundle on the internal manifold. For SU(3) (dim 8, even),
    # the spinor space Psi_+ = C^16 gives the SM particle content.
    # For SU(4) (dim 15, odd), the spinor space is C^128 with no chirality.

    results['spinor_analysis'] = {
        'dim_spinor': 128,
        'has_chirality': False,  # dim 15 is odd
        'chiral_decomposition': 'N/A (odd dimension)',
        'comparison_su3': 'SU(3): dim_spinor = 16, chiral 8+8, gives SM exactly',
    }

    return results


# =============================================================================
# SECTION 7: DIRAC SPECTRUM (FEASIBILITY CHECK)
# =============================================================================

def estimate_dirac_cost():
    """
    Estimate computational cost of Dirac spectrum on SU(4).

    Spinor dim = 128 (vs 16 for SU(3)).

    For irrep (p,q,r) of SU(4) [Dynkin labels], the dimension is:
    dim(p,q,r) = (p+1)(q+1)(r+1)(p+q+2)(q+r+2)(p+q+r+3) / 12

    For the trivial (0,0,0): dim = 1. Dirac matrix: 1*128 = 128. Feasible.
    For the fundamental (1,0,0): dim = 4. Dirac matrix: 4*128 = 512. Feasible.
    For adjoint (0,1,0) in A_3: dim = 15. Dirac matrix: 15*128 = 1920. Feasible.
    For (1,0,1): dim = 20. Matrix: 20*128 = 2560. Still OK.
    For (2,0,0): dim = 10. Matrix: 1280. OK.

    But for higher reps, this grows fast. (1,1,0): dim = 20, matrix 2560.
    (0,0,2): dim = 10, matrix 1280.

    With max sum of Dynkin labels = 2:
    Irreps: (0,0,0), (1,0,0), (0,1,0), (0,0,1), (2,0,0), (0,2,0), (0,0,2),
            (1,1,0), (1,0,1), (0,1,1)
    Total: 10 irreps

    Largest matrix: dim(0,2,0) = 84, so 84*128 = 10752. That's a 10752x10752
    eigenvalue problem. Feasible with numpy (takes ~minutes).

    Actually wait: (0,2,0) for A_3 has dim:
    d = (0+1)(2+1)(0+1)(0+2+2)(2+0+2)(0+2+0+3)/12 = 1*3*1*4*4*5/12 = 240/12 = 20
    Let me recalculate. For SU(4), the dimension formula for Dynkin labels [a1,a2,a3] is:

    dim = (a1+1)(a2+1)(a3+1)(a1+a2+2)(a2+a3+2)(a1+a2+a3+3) / (1*1*1*2*2*3)
        = (a1+1)(a2+1)(a3+1)(a1+a2+2)(a2+a3+2)(a1+a2+a3+3) / 12

    Let me compute for each:
    """
    irreps = []
    max_sum = 2

    for a1 in range(max_sum + 1):
        for a2 in range(max_sum + 1 - a1):
            for a3 in range(max_sum + 1 - a1 - a2):
                d = ((a1+1)*(a2+1)*(a3+1)*(a1+a2+2)*(a2+a3+2)*(a1+a2+a3+3)) // 12
                matrix_size = d * 128
                irreps.append((a1, a2, a3, d, matrix_size))

    return irreps


def su4_irrep_dim(a1, a2, a3):
    """Dimension of SU(4) irrep with Dynkin labels [a1, a2, a3]."""
    return ((a1+1)*(a2+1)*(a3+1)*(a1+a2+2)*(a2+a3+2)*(a1+a2+a3+3)) // 12


def build_su4_irreps(gens, f_abc, max_dynkin_sum=1):
    """
    Build SU(4) irreps up to given Dynkin label sum.

    Uses tensor product + Casimir projection method.

    For SU(4), the quadratic Casimir for Dynkin labels [a1, a2, a3] is:
    C_2 = (a1^2 + a2^2 + a3^2 + a1*a2 + a2*a3 + 2*a1*a2 + ... ) / ...

    Actually, for SU(N) with highest weight lambda = sum m_i omega_i (omega_i fundamental weights),
    the Casimir is:
    C_2(lambda) = (lambda, lambda + 2*rho) / (2*I_adj)

    where rho = sum omega_i (Weyl vector), (,) is the Killing inner product,
    and I_adj is a normalization.

    For our anti-Hermitian generators with Tr(e_a e_b) = -1/2 delta_{ab}:
    C_op = sum_a rho(e_a)^2 has eigenvalue C_op = -C_2/2 (negative definite).

    For SU(4) with Dynkin labels [a1, a2, a3]:
    C_2 = (3*a1^2 + 4*a1*a2 + 2*a1*a3 + 3*a2^2 + 4*a2*a3 + 3*a3^2 +
           12*a1 + 16*a2 + 12*a3) / 8

    Actually let me just compute it numerically for each irrep.

    Returns:
        dict mapping (a1,a2,a3) -> (rho, dim)
    """
    n_gen = len(gens)
    I_N = np.eye(gens[0].shape[0], dtype=complex)

    irreps = {}

    # Trivial
    irreps[(0,0,0)] = ([np.zeros((1,1), dtype=complex) for _ in range(n_gen)], 1)

    # Fundamental (1,0,0) = 4
    irreps[(1,0,0)] = ([g.copy() for g in gens], 4)

    # Anti-fundamental (0,0,1) = 4bar
    irreps[(0,0,1)] = ([-g.T for g in gens], 4)

    if max_dynkin_sum < 1:
        return irreps

    # Adjoint (0,1,0) = 15, from structure constants
    rho_adj = []
    for a in range(n_gen):
        M = np.zeros((n_gen, n_gen), dtype=complex)
        for b in range(n_gen):
            for c in range(n_gen):
                M[c, b] = f_abc[a, b, c]
        rho_adj.append(M)
    irreps[(0,1,0)] = (rho_adj, 15)

    if max_dynkin_sum < 2:
        return irreps

    # For max_dynkin_sum = 2, need:
    # (2,0,0) = Sym^2(4) = 10
    # (0,0,2) = Sym^2(4bar) = 10
    # (1,1,0) = 4 tensor 4 -> extract 20-dim piece (actually 4 x 4 = 10 + 6)
    # Wait, 4 x 4 = Sym^2(4) + Lambda^2(4) = 10 + 6.
    # (1,1,0) is NOT in 4 x 4. Let me be more careful.

    # SU(4) tensor product rules (Dynkin labels):
    # (1,0,0) x (1,0,0) = (2,0,0) + (0,1,0) [= 10 + 6, but wait: 4x4 = 16 = 10 + 6]
    # Hmm: (0,1,0) for SU(4) is 15-dim (adjoint), not 6.
    #
    # Let me reconsider. For SU(4):
    # 4 x 4 = 10_s + 6_a where 10 = Sym^2(4) = [2,0,0] and 6 = Lambda^2(4) = [0,1,0]
    # But [0,1,0] is the adjoint (dim 15)! That can't be right.
    #
    # The issue: Lambda^2(C^4) has dim = 6. For SU(4), this is the [0,1,0] representation
    # which has dim = (0+1)(1+1)(0+1)(0+1+2)(1+0+2)(0+1+0+3)/12 = 1*2*1*2*3*4/12 = 48/12 = 4.
    # That's wrong too.
    #
    # Let me recalculate. [0,1,0] for SU(4):
    # (a1+1)(a2+1)(a3+1) = 1*2*1 = 2
    # (a1+a2+2) = 3
    # (a2+a3+2) = 3
    # (a1+a2+a3+3) = 4
    # Product = 2*3*3*4 = 72, divide by 12 = 6. OK!
    #
    # So [0,1,0] = Lambda^2(4) = 6-dimensional. This is NOT the adjoint!
    # The adjoint of SU(4) is 15-dimensional. What Dynkin label is the adjoint?
    # dim = 15. We need (a1+1)(a2+1)(a3+1)(a1+a2+2)(a2+a3+2)(a1+a2+a3+3)/12 = 15.
    #
    # [1,0,1]: (2)(1)(2)(2)(2)(4)/12 = 64/12... not integer. Hmm.
    # Wait: (2*1*2*2*2*5)/12 = 80/12... also wrong. Let me recompute.
    # [1,0,1]: a1=1, a2=0, a3=1.
    # (a1+1)=2, (a2+1)=1, (a3+1)=2, (a1+a2+2)=3, (a2+a3+2)=3, (a1+a2+a3+3)=5
    # Product: 2*1*2*3*3*5 = 180, / 12 = 15. Yes!
    #
    # So the adjoint of SU(4) has Dynkin labels [1,0,1]. This is because
    # the adjoint of SU(N) is [1,0,...,0,1] (fundamental x anti-fundamental, traceless).
    #
    # So my adjoint computation above (from structure constants) gives [1,0,1], not [0,1,0].

    # Let me fix the irrep dictionary
    del irreps[(0,1,0)]
    irreps[(1,0,1)] = (rho_adj, 15)  # Adjoint = [1,0,1]

    # Now build more irreps:
    # [2,0,0] = Sym^2(4) = 10
    rho_fund = irreps[(1,0,0)][0]
    dim_fund = 4

    # Sym^2(C^4): dim = 10
    I4 = np.eye(4, dtype=complex)
    sym_vecs = []
    for i in range(4):
        v = np.zeros(16, dtype=complex)
        v[4*i + i] = 1.0
        sym_vecs.append(v)
    for i in range(4):
        for j in range(i+1, 4):
            v = np.zeros(16, dtype=complex)
            v[4*i + j] = 1.0/np.sqrt(2)
            v[4*j + i] = 1.0/np.sqrt(2)
            sym_vecs.append(v)
    P_sym = np.column_stack(sym_vecs)  # 16 x 10

    rho_sym2 = []
    for a in range(n_gen):
        rho_16 = np.kron(rho_fund[a], I4) + np.kron(I4, rho_fund[a])
        rho_sym2.append(P_sym.conj().T @ rho_16 @ P_sym)
    irreps[(2,0,0)] = (rho_sym2, 10)

    # [0,0,2] = Sym^2(4bar) = 10bar
    rho_antifund = irreps[(0,0,1)][0]
    rho_sym2_bar = []
    for a in range(n_gen):
        rho_16 = np.kron(rho_antifund[a], I4) + np.kron(I4, rho_antifund[a])
        rho_sym2_bar.append(P_sym.conj().T @ rho_16 @ P_sym)
    irreps[(0,0,2)] = (rho_sym2_bar, 10)

    # [0,1,0] = Lambda^2(4) = 6
    asym_vecs = []
    for i in range(4):
        for j in range(i+1, 4):
            v = np.zeros(16, dtype=complex)
            v[4*i + j] = 1.0/np.sqrt(2)
            v[4*j + i] = -1.0/np.sqrt(2)
            asym_vecs.append(v)
    P_asym = np.column_stack(asym_vecs)  # 16 x 6

    rho_lambda2 = []
    for a in range(n_gen):
        rho_16 = np.kron(rho_fund[a], I4) + np.kron(I4, rho_fund[a])
        rho_lambda2.append(P_asym.conj().T @ rho_16 @ P_asym)
    irreps[(0,1,0)] = (rho_lambda2, 6)

    # [0,0,0] already done (trivial)

    # [1,1,0] = in 4 x 6, extract 20-dim piece
    # 4 x 6 = 4 + 20... wait. Dynkin: [1,0,0] x [0,1,0]
    # = [1,1,0] + [0,0,1]. Dimensions: dim[1,1,0] + 4 = 20 + 4 = 24 = 4*6. Check.
    # dim[1,1,0] = (2*2*1*3*3*4)/12 = 144/12 = 12. Hmm, that's not 20.
    #
    # Let me recalculate dim[1,1,0]: a1=1, a2=1, a3=0
    # (2)(2)(1)(3)(3)(4)/12 = 144/12 = 12. Hmm.
    # But 4*6 = 24 and 4 + 12 = 16, not 24. So there must be other pieces.
    #
    # [1,0,0] x [0,1,0] decomposes as:
    # Weights add. Actually for SU(4): 4 x 6 = ?
    # Use the Casimir approach instead.

    # Build Casimir on 4 x 6 product
    rho_4 = rho_fund
    rho_6 = rho_lambda2
    dim_24 = 4 * 6

    C2_24 = np.zeros((dim_24, dim_24), dtype=complex)
    for a in range(n_gen):
        rho_a = np.kron(rho_4[a], np.eye(6, dtype=complex)) + np.kron(np.eye(4, dtype=complex), rho_6[a])
        C2_24 += rho_a @ rho_a

    evals_24 = eigvalsh(C2_24)

    # Group eigenvalues
    tol = 1e-8  # (local)
    groups = {}
    for ev in evals_24:
        found = False
        for key in groups:
            if abs(ev - key) < tol:
                groups[key] += 1
                found = True
                break
        if not found:
            groups[ev] = 1

    # We expect decomposition into irreps with total dim = 24
    # The pieces should correspond to known SU(4) irreps

    for c2_val, mult in sorted(groups.items()):
        # Project onto this eigenspace
        all_evals, all_evecs = np.linalg.eigh(C2_24)
        mask = np.abs(all_evals - c2_val) < tol
        P_proj = all_evecs[:, mask]

        if P_proj.shape[1] == mult:
            rho_sub = []
            for a in range(n_gen):
                rho_a = np.kron(rho_4[a], np.eye(6, dtype=complex)) + np.kron(np.eye(4, dtype=complex), rho_6[a])
                rho_sub.append(P_proj.conj().T @ rho_a @ P_proj)

            # Identify which irrep this is by dimension
            if mult == 4:
                # Could be (0,0,1) = 4bar or (1,0,0) = 4
                # Check Casimir to distinguish
                irreps[('4x6_piece_4', )] = (rho_sub, mult)
            elif mult == 20:
                irreps[(1,1,0)] = (rho_sub, mult)

    # [0,1,1] = conjugate of [1,1,0]
    if (1,1,0) in irreps:
        rho_110 = irreps[(1,1,0)][0]
        dim_110 = irreps[(1,1,0)][1]
        rho_011 = [-r.T for r in rho_110]
        irreps[(0,1,1)] = (rho_011, dim_110)

    # [0,2,0] = 20' (from 6 x 6 symmetric)
    # dim[0,2,0] = (1*3*1*3*5*5)/12 = 225/12 = ... not integer?
    # (1)(3)(1)(2+2)(2+2)(0+2+0+3) = 1*3*1*4*4*5 = 240/12 = 20
    # Hmm, let me recompute: a1=0,a2=2,a3=0
    # (0+1)(2+1)(0+1)(0+2+2)(2+0+2)(0+2+0+3) = 1*3*1*4*4*5 = 240/12 = 20
    # So [0,2,0] is 20-dimensional. This comes from Sym^2(Lambda^2(4)).

    # For feasibility, let's stop at the irreps we have and build the Dirac operator
    # for the ones that are manageable

    return irreps


def orthonormal_frame_general(g):
    """Orthonormal frame from Cholesky decomposition."""
    L = cholesky(g)
    return inv(L)


def frame_structure_constants_general(f_abc, E):
    """Structure constants in the orthonormal frame."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)


def connection_coefficients_general(ft):
    """Levi-Civita connection in ON frame."""
    n = ft.shape[0]
    Gamma = np.zeros((n, n, n), dtype=np.float64)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])
    return Gamma


def spinor_connection_offset_general(Gamma, gammas):
    """Compute Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c."""
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * (gammas[a] @ gammas[b] @ gammas[c])

    Omega *= 0.25
    return Omega


def dirac_on_irrep_general(rho, E, gammas, Omega):
    """
    D_pi = sum_{a,b} E_{ab} rho[b] tensor gamma_a + I tensor Omega
    """
    n_gen = len(gammas)
    dim_rho = rho[0].shape[0]
    dim_spin = gammas[0].shape[0]
    dim_total = dim_rho * dim_spin

    D = np.zeros((dim_total, dim_total), dtype=complex)

    for a in range(n_gen):
        for b in range(n_gen):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])

    D += np.kron(np.eye(dim_rho, dtype=complex), Omega)

    return D


# =============================================================================
# SECTION 8: MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 70)
    print("S59 SU(4) MINIMAL VIABILITY TEST (SU4-MINIMAL-59)")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Step 1: SU(4) Lie Algebra
    # -------------------------------------------------------------------------
    print("\n--- STEP 1: SU(4) Lie Algebra ---")
    gens = su4_generators()
    f_abc = compute_structure_constants_general(gens)
    B_ab = compute_killing_form_general(f_abc)

    print(f"  Generators: {len(gens)} (expected 15)")
    print(f"  Generator dimension: {gens[0].shape}")

    # Verify structure constants antisymmetry
    asym_err = np.max(np.abs(f_abc + f_abc.transpose(1, 0, 2)))
    print(f"  Structure constants antisymmetry error: {asym_err:.2e}")

    # Killing form
    B_diag = np.diag(B_ab)
    print(f"  Killing form diagonal (should be constant): min={B_diag.min():.4f}, max={B_diag.max():.4f}")
    B_offdiag = B_ab - np.diag(B_diag)
    print(f"  Killing form off-diagonal max: {np.max(np.abs(B_offdiag)):.2e}")

    # For su(4) with Tr(e_a e_b) = -1/2 delta: B_ab should be -C * delta_ab
    # where C = 2*N = 8 (using f_{abc} f_{dbc} = 2N delta_{ad} in physicist normalization)
    # Let me check: B_ab = sum_{c,d} f_{acd} f_{bcd}
    # With our normalization, B_{aa} should be = -2*N = -8 for SU(4)
    print(f"  Expected B_aa for su(4): -8.000 (got {B_diag[0]:.4f})")

    # -------------------------------------------------------------------------
    # Step 2: Root System Analysis
    # -------------------------------------------------------------------------
    print("\n--- STEP 2: Root System A_3 ---")
    root_analysis = analyze_root_system(gens, f_abc)
    print(f"  Rank: {root_analysis['rank']} (expected 3)")
    print(f"  Cartan indices: {root_analysis['cartan_indices']}")
    print(f"  Root system: {root_analysis['root_system']}")
    print(f"  Weyl group order (expected): {root_analysis['weyl_order_expected']}")
    print(f"  Killing eigenvalues range: [{root_analysis['killing_eigenvalues'][0]:.4f}, "
          f"{root_analysis['killing_eigenvalues'][-1]:.4f}]")

    # -------------------------------------------------------------------------
    # Step 3: Jensen-like Metric
    # -------------------------------------------------------------------------
    print("\n--- STEP 3: Jensen Metric on SU(4) ---")
    tau = 0.19  # Compare with SU(3) fold

    # Verify volume-preservation
    vol = verify_volume_preserving(tau)
    print(f"  Volume factor at tau={tau}: {vol:.6f} (should be 1.000)")

    g_s = jensen_metric_su4(B_ab, tau)
    print(f"  Metric size: {g_s.shape}")
    print(f"  Metric positive definite: {np.all(eigvalsh(g_s) > 0)}")
    print(f"  Metric eigenvalues: [{eigvalsh(g_s).min():.4f}, {eigvalsh(g_s).max():.4f}]")

    decomp = su4_decomposition_indices()
    print(f"  Stabilizer indices (u(3)): {decomp['stabilizer']} ({len(decomp['stabilizer'])} generators)")
    print(f"  Coset indices (C^3): {decomp['coset']} ({len(decomp['coset'])} generators)")

    # -------------------------------------------------------------------------
    # Step 4: Clifford Algebra Cl(15)
    # -------------------------------------------------------------------------
    print("\n--- STEP 4: Clifford Algebra Cl(15) ---")
    gammas = build_cliff15()
    cliff_err = validate_clifford_general(gammas)
    print(f"  Generators: {len(gammas)} (expected 15)")
    print(f"  Spinor dimension: {gammas[0].shape[0]} (expected 128)")
    print(f"  Clifford relation error: {cliff_err:.2e}")

    # Hermiticity check
    herm_err = max(np.max(np.abs(g - g.conj().T)) for g in gammas)
    print(f"  Hermiticity error: {herm_err:.2e}")

    # -------------------------------------------------------------------------
    # Step 5: KO-Dimension
    # -------------------------------------------------------------------------
    print("\n--- STEP 5: KO-Dimension Analysis ---")
    ko_results = check_ko_dimension(gammas, 15)
    print(f"  Manifold dimension: {ko_results['dim']}")
    print(f"  KO-dim (manifold): {ko_results['ko_manifold']} (= 15 mod 8 = 7)")
    print(f"  Has chirality: {ko_results['has_chirality']} (even dim required)")
    print(f"  J^2 = {'+1' if ko_results['J_squared'] == 1 else '-1'}")
    print(f"  JD sign: {'+1' if ko_results['JD_sign'] == 1 else '-1'}")
    if ko_results['has_chirality']:
        print(f"  J*gamma sign: {'+1' if ko_results['J_gamma_sign'] == 1 else '-1'}")
    else:
        print(f"  J*gamma sign: N/A (no chirality for odd dim)")
    print(f"  KO-dim = 6 test:")
    ko6 = ko_results['ko6_check']
    print(f"    J^2 = +1: {ko6['J_sq_match']}")
    print(f"    JD = +DJ: {ko6['JD_match']}")
    print(f"    J*gamma = -gamma*J: {ko6['Jgamma_match']} (requires gamma to exist: {ko6['Jgamma_exists']})")
    print(f"  *** KO-dim = 6: {'PASS' if ko_results['ko6_pass'] else 'FAIL'} ***")
    print(f"  STRUCTURAL OBSTRUCTION: dim(SU(4)) = 15 is ODD -> no chirality -> KO-dim = 7, not 6")

    # -------------------------------------------------------------------------
    # Step 6: SM Quantum Numbers (Branching)
    # -------------------------------------------------------------------------
    print("\n--- STEP 6: SM Quantum Numbers (Branching SU(4) -> SU(3) x U(1)) ---")
    branch = branching_su4_to_su3_u1(gens, f_abc)

    fb = branch['fundamental_branching']
    print(f"  Fundamental 4 -> 3 + 1:")
    print(f"    Triplet U(1) charge: {fb['triplet_charge']:.6f}")
    print(f"    Singlet U(1) charge: {fb['singlet_charge']:.6f}")
    print(f"    Singlet/Triplet ratio: {fb['ratio']:.4f} (expected -3.0)")

    print(f"  Adjoint 15 -> 8_0 + 3_q + 3bar_(-q) + 1_0:")
    for charge, mult in sorted(branch['adjoint_branching']['charge_multiplicities'].items()):
        print(f"    charge = {charge}: multiplicity = {mult}")

    sm = branch['sm_content']
    print(f"  SM content check:")
    print(f"    Color triplet quarks: {sm['color_triplet_quarks']}")
    print(f"    Color singlet leptons: {sm['color_singlet_leptons']}")
    print(f"    B-L quantum number: {sm['BL_quantum_number']}")
    print(f"    Full SM from SU(4) alone: {sm['full_SM_from_SU4_alone']}")
    print(f"    Pati-Salam viable: {sm['pati_salam_viable']}")
    print(f"    Lepton as 4th color: {sm['lepton_as_4th_color']}")

    spinor = branch['spinor_analysis']
    print(f"  Spinor analysis:")
    print(f"    dim(spinor) = {spinor['dim_spinor']} (vs 16 for SU(3))")
    print(f"    Has chirality: {spinor['has_chirality']}")
    print(f"    SU(3) comparison: {spinor['comparison_su3']}")

    # -------------------------------------------------------------------------
    # Step 7: Dirac Spectrum (Feasibility + Partial Computation)
    # -------------------------------------------------------------------------
    print("\n--- STEP 7: Dirac Spectrum ---")

    # Cost estimate
    print("  Feasibility estimate (max_dynkin_sum = 2):")
    irr_costs = estimate_dirac_cost()
    total_evals = 0  # (local)
    for a1, a2, a3, d, ms in irr_costs:
        print(f"    [{a1},{a2},{a3}]: dim = {d:4d}, matrix size = {ms:6d}x{ms:6d}")
        total_evals += ms
    print(f"  Total eigenvalues at max_sum=2: {total_evals}")

    # Build geometric infrastructure
    print("\n  Building geometric infrastructure...")
    E = orthonormal_frame_general(g_s)
    ft = frame_structure_constants_general(f_abc, E)
    Gamma = connection_coefficients_general(ft)

    # Validate connection
    n_gen = 15
    mc_err = 0.0  # (local)
    for a in range(n_gen):
        for b in range(n_gen):
            for c in range(n_gen):
                mc_err = max(mc_err, abs(Gamma[c, a, b] + Gamma[b, a, c]))
    print(f"  Connection metric compatibility error: {mc_err:.2e}")

    # Build Omega (this takes a while with 15^3 triple loop)
    print("  Computing spinor connection offset Omega (15^3 = 3375 terms)...")
    t_omega = time.time()
    Omega = spinor_connection_offset_general(Gamma, gammas)
    print(f"  Omega computed in {time.time() - t_omega:.1f}s")

    # Check Omega properties
    herm_err_O = np.max(np.abs(Omega - Omega.conj().T))
    aherm_err_O = np.max(np.abs(Omega + Omega.conj().T))
    print(f"  Omega Hermitian error: {herm_err_O:.2e}")
    print(f"  Omega anti-Hermitian error: {aherm_err_O:.2e}")

    # Build irreps
    print("\n  Building SU(4) irreps (max_dynkin_sum = 2)...")
    irreps = build_su4_irreps(gens, f_abc, max_dynkin_sum=2)
    print(f"  Built {len(irreps)} irreps")

    # Validate irreps
    for label, (rho, dim_r) in irreps.items():
        if isinstance(label, tuple) and len(label) == 3 and all(isinstance(x, int) for x in label):
            hom_err = 0.0  # (local)
            for a in range(n_gen):
                for b in range(a+1, n_gen):
                    comm = rho[a] @ rho[b] - rho[b] @ rho[a]
                    target = sum(f_abc[a, b, c] * rho[c] for c in range(n_gen))
                    hom_err = max(hom_err, np.max(np.abs(comm - target)))
            ah_err = max(np.max(np.abs(rho[a] + rho[a].conj().T)) for a in range(n_gen))
            print(f"    [{label}] dim={dim_r}: homomorphism err={hom_err:.2e}, anti-Herm err={ah_err:.2e}")

    # Compute Dirac spectrum on available irreps
    print("\n  Computing Dirac spectrum on available irreps...")
    all_eigenvalues = []
    eval_data = []

    for label, (rho, dim_r) in sorted(irreps.items(), key=lambda x: x[1][1]):
        if not (isinstance(label, tuple) and len(label) == 3 and all(isinstance(x, int) for x in label)):
            continue

        matrix_size = dim_r * 128
        print(f"    [{label}] dim={dim_r}, Dirac matrix {matrix_size}x{matrix_size}...", end=" ", flush=True)

        t_d = time.time()
        D_pi = dirac_on_irrep_general(rho, E, gammas, Omega)
        evals_pi = eigvals(D_pi)
        dt = time.time() - t_d

        # Check: eigenvalues should be purely imaginary (D is anti-Hermitian)
        real_parts = np.abs(evals_pi.real)
        imag_parts = evals_pi.imag
        max_real = np.max(real_parts)

        print(f"done in {dt:.1f}s. max|Re(lambda)| = {max_real:.2e}, "
              f"|Im| range = [{np.min(np.abs(imag_parts)):.4f}, {np.max(np.abs(imag_parts)):.4f}]")

        eval_data.append({
            'label': label,
            'dim': dim_r,
            'eigenvalues': evals_pi,
            'pw_multiplicity': dim_r**2 if label != (0,0,0) else 1,
        })

        for ev in evals_pi:
            all_eigenvalues.append((ev.imag, dim_r**2 if label != (0,0,0) else 1))

    # Collect DOS
    all_imag = np.array([x[0] for x in all_eigenvalues])
    all_mult = np.array([x[1] for x in all_eigenvalues])

    # Sort by absolute value
    abs_imag = np.abs(all_imag)
    sorted_idx = np.argsort(abs_imag)

    print(f"\n  Total distinct eigenvalues: {len(all_imag)}")
    print(f"  Eigenvalue range (|Im|): [{abs_imag.min():.4f}, {abs_imag.max():.4f}]")

    # Van Hove analysis: look for DOS accumulation
    # Create histogram
    n_bins = 50  # (local)
    hist, bin_edges = np.histogram(abs_imag, bins=n_bins, weights=all_mult.astype(float))
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Find peak(s) in DOS
    if len(hist) > 0:
        peak_idx = np.argmax(hist)
        peak_energy = bin_centers[peak_idx]
        peak_dos = hist[peak_idx]
        print(f"  DOS peak at |lambda| = {peak_energy:.4f}, count = {peak_dos:.0f}")

    # Check for van Hove singularity: need DOS -> infinity at some energy
    # With truncated spectrum, can only look for accumulation
    print("  Van Hove analysis: INCOMPLETE (limited irreps computed)")

    # -------------------------------------------------------------------------
    # Step 8: Comparison with SU(3)
    # -------------------------------------------------------------------------
    print("\n--- STEP 8: Comparison with SU(3) ---")
    print(f"  {'Property':<30} {'SU(3)':<20} {'SU(4)':<20}")
    print(f"  {'-'*30} {'-'*20} {'-'*20}")
    print(f"  {'Dimension':<30} {'8':<20} {'15':<20}")
    print(f"  {'Rank':<30} {'2':<20} {'3':<20}")
    print(f"  {'Root system':<30} {'A_2':<20} {'A_3':<20}")
    print(f"  {'Spinor dim':<30} {'16':<20} {'128':<20}")
    print(f"  {'Has chirality':<30} {'Yes (dim even)':<20} {'No (dim odd)':<20}")
    print(f"  {'KO-dim (manifold)':<30} {'0 (=8 mod 8)':<20} {'7 (=15 mod 8)':<20}")
    print(f"  {'KO-dim = 6 possible':<30} {'Framework: YES':<20} {'NO (no gamma)':<20}")
    print(f"  {'SM content':<30} {'Exact (Psi+)':<20} {'Partial (no EW)':<20}")
    print(f"  {'Weyl group':<30} {'S_3 (|W|=6)':<20} {'S_4 (|W|=24)':<20}")

    # -------------------------------------------------------------------------
    # GATE VERDICT
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("GATE VERDICT: SU4-MINIMAL-59")
    print("=" * 70)

    ko_pass = ko_results['ko6_pass']
    sm_pass = sm['color_triplet_quarks'] and sm['color_singlet_leptons'] and sm['BL_quantum_number']
    sm_full = sm['full_SM_from_SU4_alone']
    vh_complete = False  # Van Hove analysis incomplete

    score = 0
    if ko_pass:
        score += 1
    if sm_pass:
        score += 1  # Partial SM content (Pati-Salam viable but not full SM alone)
    if vh_complete:
        score += 1

    # Gate classification
    if ko_pass and sm_full and vh_complete:
        verdict = "PASS"
    elif not ko_pass or not sm_pass:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    print(f"\n  Condition 1 — KO-dim = 6: {'PASS' if ko_pass else 'FAIL'}")
    print(f"    dim(SU(4)) = 15 (odd) => no chirality operator => KO-dim = 7, not 6")
    print(f"    STRUCTURAL OBSTRUCTION: The Jgamma = -gammaJ condition requires a Z/2 grading")
    print(f"    which exists only for even-dimensional manifolds.")

    print(f"\n  Condition 2 — SM quantum numbers: {'PARTIAL' if sm_pass else 'FAIL'}")
    print(f"    SU(4) -> SU(3) x U(1) branching gives:")
    print(f"    - 4 = 3_(+q) + 1_(-3q): quarks as color triplets, leptons as singlets (Pati-Salam)")
    print(f"    - 15 = 8_0 + 3_(+4q) + 3bar_(-4q) + 1_0: gluons + leptoquarks + B-L boson")
    print(f"    However: FULL SM requires SU(2)_L x SU(2)_R in addition to SU(4)")
    print(f"    SU(4) alone lacks electroweak structure")

    print(f"\n  Condition 3 — Van Hove singularity: INCOMPLETE")
    print(f"    Dirac spectrum computed for {len(eval_data)} irreps at tau = {tau}")
    print(f"    van Hove analysis requires more irreps (convergence not tested)")

    print(f"\n  *** GATE VERDICT: {verdict} (score {score}/3) ***")
    print(f"  KO-dim = 7 is a STRUCTURAL FAILURE — no chirality on odd-dimensional manifolds")
    print(f"  Even NCG Pati-Salam achieves KO-dim = 6 via FINITE spectral triple,")
    print(f"  not from the manifold. In Baptista's KK framework, the internal space IS")
    print(f"  the manifold, so this obstruction is real.")

    # -------------------------------------------------------------------------
    # Save results
    # -------------------------------------------------------------------------
    t_total = time.time() - t_start
    print(f"\n  Total computation time: {t_total:.1f}s")

    # Collect data for saving
    save_dict = {
        # Lie algebra
        'n_generators': 15,
        'killing_diagonal': B_diag[0],
        'structure_const_antisym_err': asym_err,
        'killing_form': B_ab,

        # Root system
        'rank': root_analysis['rank'],
        'cartan_indices': np.array(root_analysis['cartan_indices']),

        # KO dimension
        'ko_dim_manifold': ko_results['ko_manifold'],
        'ko_dim_6_pass': ko_results['ko6_pass'],
        'has_chirality': ko_results['has_chirality'],
        'J_squared': ko_results['J_squared'],
        'JD_sign': ko_results['JD_sign'],

        # Metric
        'tau': tau,
        'volume_factor': vol,
        'metric': g_s,
        'metric_eigenvalues': eigvalsh(g_s),

        # Clifford
        'spinor_dim': 128,
        'clifford_err': cliff_err,

        # Branching
        'u1_eigenvalues_fund': np.array(branch['u1_eigenvalues_fund']),
        'fund_triplet_charge': fb['triplet_charge'],
        'fund_singlet_charge': fb['singlet_charge'],
        'charge_ratio': fb['ratio'],

        # Dirac spectrum
        'n_irreps_computed': len(eval_data),
        'all_eigenvalues_imag': all_imag,
        'all_multiplicities': all_mult,
        'connection_metric_compat_err': mc_err,
        'omega_herm_err': herm_err_O,
        'omega_aherm_err': aherm_err_O,

        # Gate
        'gate_verdict': verdict,
        'score': score,
        'computation_time': t_total,
    }

    # Save per-irrep eigenvalues
    for i, ed in enumerate(eval_data):
        label = ed['label']
        save_dict[f'irrep_{label}_eigenvalues'] = ed['eigenvalues']
        save_dict[f'irrep_{label}_dim'] = ed['dim']
        save_dict[f'irrep_{label}_pw_mult'] = ed['pw_multiplicity']

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_su4_minimal.npz')
    np.savez(outpath, **save_dict)
    print(f"\n  Saved: {outpath}")

    # -------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('SU(4) Minimal Viability Test (SU4-MINIMAL-59)', fontsize=14, fontweight='bold')

        # Panel 1: Metric eigenvalues vs tau
        ax = axes[0, 0]
        taus = np.linspace(0, 0.4, 50)
        stab_evals = []
        coset_evals = []
        for t in taus:
            g_t = jensen_metric_su4(B_ab, t)
            ev = eigvalsh(g_t)
            stab_evals.append(ev[decomp['stabilizer'][0]])
            coset_evals.append(ev[decomp['coset'][0]])
        ax.plot(taus, stab_evals, 'b-', label='Stabilizer (u(3))')
        ax.plot(taus, coset_evals, 'r-', label='Coset (C^3)')
        ax.axvline(tau, color='k', linestyle='--', alpha=0.5, label=f'tau = {tau}')
        ax.set_xlabel('tau')
        ax.set_ylabel('Metric eigenvalue')
        ax.set_title('Jensen-like metric on SU(4)')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Panel 2: Dirac eigenvalue spectrum
        ax = axes[0, 1]
        if len(all_imag) > 0:
            ax.hist(np.abs(all_imag), bins=40, weights=all_mult.astype(float),
                    color='steelblue', edgecolor='navy', alpha=0.7)
            ax.set_xlabel('|lambda| (Dirac eigenvalue)')
            ax.set_ylabel('Weighted count (with PW mult)')
            ax.set_title(f'Dirac DOS on SU(4), tau={tau}')
        ax.grid(True, alpha=0.3)

        # Panel 3: KO-dimension comparison
        ax = axes[1, 0]
        groups = ['SU(2)', 'SU(3)', 'SU(4)', 'G_2']
        dims = [3, 8, 15, 14]
        ko_dims = [d % 8 for d in dims]
        colors = ['green' if ko == 6 or (d == 8 and ko == 0) else 'red' for d, ko in zip(dims, ko_dims)]
        # Override: SU(3) KO-dim=6 was achieved via framework (not mod 8)
        colors[1] = 'green'  # SU(3) passes
        bars = ax.bar(groups, ko_dims, color=colors, edgecolor='black', alpha=0.7)
        ax.axhline(6, color='blue', linestyle='--', label='Target KO-dim = 6')
        ax.set_ylabel('KO-dim (= dim mod 8)')
        ax.set_title('KO-dimension by group')
        ax.legend()
        ax.set_ylim(0, 8)
        for bar, kd in zip(bars, ko_dims):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    str(kd), ha='center', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')

        # Panel 4: Branching content summary
        ax = axes[1, 1]
        ax.axis('off')
        summary_text = (
            "SU(4) Viability Summary\n"
            "=" * 40 + "\n\n"
            f"Gate: SU4-MINIMAL-59 = {verdict}\n"
            f"Score: {score}/3\n\n"
            "Condition 1 (KO-dim = 6): FAIL\n"
            "  dim(SU(4)) = 15 (odd)\n"
            "  No chirality operator\n"
            "  KO-dim = 7 (structural)\n\n"
            "Condition 2 (SM content): PARTIAL\n"
            "  4 -> 3 + 1 (quarks + leptons)\n"
            "  Pati-Salam viable\n"
            "  Missing: SU(2)_L x SU(2)_R\n\n"
            "Condition 3 (van Hove): INCOMPLETE\n"
            f"  {len(eval_data)} irreps computed\n"
            "  Convergence not tested\n\n"
            "CONCLUSION:\n"
            "SU(4) ALONE cannot replace SU(3)\n"
            "in the Baptista KK framework.\n"
            "Odd dimension = no chirality = no KO-6."
        )
        ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
                fontsize=9, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        plt.tight_layout()
        plotpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's59_su4_minimal.png')
        plt.savefig(plotpath, dpi=150, bbox_inches='tight')
        print(f"  Plot saved: {plotpath}")
        plt.close()
    except Exception as e:
        print(f"  Plot failed: {e}")

    return verdict, score


if __name__ == '__main__':
    verdict, score = main()
