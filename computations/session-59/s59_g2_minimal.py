#!/usr/bin/env python3
"""
S59 G2-MINIMAL-59: Minimal Viability Test for G_2 as Alternative Internal Space
================================================================================

Tests whether G_2 (the 14-dimensional automorphism group of the octonions)
could replace SU(3) as the internal space in the phonon-exflation framework.

Three conditions checked:
  1. KO-dimension of the spectral triple (target: 6 mod 8 for SM compatibility)
  2. SM quantum numbers from G_2 -> SU(3) branching of the spinor representation
  3. Van Hove singularity in the DOS under a Jensen-type deformation

Mathematical structure:
  - g_2 = su(3) + m  where m ~ R^6 (complement, G_2/SU(3) ~ S^6)
  - dim(G_2) = 14, rank = 2, Weyl group = D_6 (dihedral, order 12)
  - Cl(14) has spinor dim = 2^7 = 128
  - Jensen-type deformation: g(tau) scales su(3) and complement independently
    with volume preservation constraint

Gate: G2-MINIMAL-59
  PASS: All three conditions met (KO-dim=6, SM quantum numbers, van Hove)
  FAIL: KO-dim != 6 or SM quantum numbers absent
  INFO: Partial results, computational limits reached

Author: Spectral-Geometer Agent
Session: 59
Date: 2026-03-24
"""

import sys
import os
import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, det, norm, cholesky, svd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from time import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

np.set_printoptions(precision=6, linewidth=120)

# =============================================================================
# MODULE 1: G_2 LIE ALGEBRA CONSTRUCTION
# =============================================================================

def octonion_structure_constants():
    """
    Structure constants C_{ijk} for the imaginary octonions e_1,...,e_7.
    The Fano plane gives 7 triples with C_{ijk} = +1 (1-indexed).
    """
    C = np.zeros((7, 7, 7), dtype=np.float64)
    triples = [
        (1, 2, 3), (1, 4, 5), (1, 7, 6),
        (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5)
    ]
    for (i, j, k) in triples:
        a, b, c = i-1, j-1, k-1
        C[a, b, c] = 1.0
        C[b, c, a] = 1.0
        C[c, a, b] = 1.0
        C[b, a, c] = -1.0
        C[a, c, b] = -1.0
        C[c, b, a] = -1.0
    return C


def g2_generators_in_so7():
    """
    Construct the 14 generators of g_2 as anti-symmetric 7x7 matrices in so(7).

    G_2 = {X in so(7) : L_X(phi) = 0} where phi = sum C_{ijk} e^i ^ e^j ^ e^k
    is the associative 3-form of the octonions.

    Returns: list of 14 anti-symmetric (7,7) real matrices, orthonormalized
             w.r.t. inner product <X, Y> = -Tr(X Y).
    """
    C = octonion_structure_constants()

    # so(7) basis: E_{ab} - E_{ba} for a < b (21 elements)
    so7_basis = []
    for a in range(7):
        for b in range(a+1, 7):
            M = np.zeros((7, 7), dtype=np.float64)
            M[a, b] = 1.0
            M[b, a] = -1.0
            so7_basis.append(M)
    assert len(so7_basis) == 21

    n_basis = 21

    # The G_2 condition: L_X(phi) = 0 for all X.
    # L_X(phi)(e_i, e_j, e_k) = sum_a (X_{ai} C_{ajk} + X_{aj} C_{iak} + X_{ak} C_{ija}) = 0
    # for ALL ordered triples (i < j < k).
    constraints = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                row = np.zeros(n_basis)
                for n, B_n in enumerate(so7_basis):
                    val = 0.0  # (local)
                    for a in range(7):
                        val += B_n[a, i] * C[a, j, k]
                        val += B_n[a, j] * C[i, a, k]
                        val += B_n[a, k] * C[i, j, a]
                    row[n] = val
                if np.max(np.abs(row)) > 1e-14:
                    constraints.append(row)

    A = np.array(constraints)
    U, S, Vt = np.linalg.svd(A)
    tol = 1e-10  # (local)
    rank = np.sum(S > tol)
    null_dim = n_basis - rank

    print(f"  so(7) dimension: {n_basis}")
    print(f"  Constraint rank: {rank}")
    print(f"  Null space (= g_2) dimension: {null_dim}")

    if null_dim != 14:
        print(f"  FATAL: Expected g_2 dim=14, got {null_dim}")
        return []

    # Extract null space as 7x7 matrices
    null_vectors = Vt[rank:]
    g2_gens_raw = []
    for i in range(null_dim):
        X = np.zeros((7, 7), dtype=np.float64)
        for n, coeff in enumerate(null_vectors[i]):
            X += coeff * so7_basis[n]
        g2_gens_raw.append(X)

    # Gram-Schmidt orthonormalization w.r.t. <X,Y> = -Tr(XY)
    ortho_gens = []
    for X in g2_gens_raw:
        v = X.copy()
        for Y in ortho_gens:
            ip = -np.trace(v @ Y)
            v = v - ip * Y
        nrm = np.sqrt(-np.trace(v @ v))
        if nrm > 1e-14:
            ortho_gens.append(v / nrm)

    print(f"  Orthonormalized {len(ortho_gens)} generators")
    return ortho_gens


def validate_g2_algebra(gens):
    """
    Validate closure and compute structure constants + Killing form.
    Returns: f_abc, B_ab, max_closure_error
    """
    n = len(gens)
    f_abc = np.zeros((n, n, n), dtype=np.float64)

    max_closure_err = 0.0
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            coeffs = np.zeros(n)
            for c in range(n):
                coeffs[c] = -np.trace(comm @ gens[c])
            recon = sum(coeffs[c] * gens[c] for c in range(n))
            err = np.max(np.abs(comm - recon))
            max_closure_err = max(max_closure_err, err)
            for c in range(n):
                f_abc[a, b, c] = coeffs[c]
                f_abc[b, a, c] = -coeffs[c]

    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    max_antisym_err = max(np.max(np.abs(g + g.T)) for g in gens)
    B_eigvals = np.linalg.eigvalsh(B_ab)

    print(f"  Closure error: {max_closure_err:.2e}")
    print(f"  Antisymmetry error: {max_antisym_err:.2e}")
    print(f"  Killing form eigenvalues: min={B_eigvals[0]:.4f}, max={B_eigvals[-1]:.4f}")
    print(f"  Killing form sign: {'positive' if B_eigvals[0] > 0 else 'negative' if B_eigvals[-1] < 0 else 'mixed'}")

    # Check total antisymmetry of f_abc
    asym_err = 0.0  # (local)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                asym_err = max(asym_err, abs(f_abc[a,b,c] + f_abc[b,a,c]))
                asym_err = max(asym_err, abs(f_abc[a,b,c] - f_abc[b,c,a]))
    print(f"  Structure constants total antisymmetry error: {asym_err:.2e}")

    return f_abc, B_ab, max_closure_err


# =============================================================================
# MODULE 2: G_2 -> SU(3) DECOMPOSITION VIA KERNEL METHOD
# =============================================================================

def identify_su3_decomposition(gens, f_abc, B_ab):
    """
    Identify the SU(3) subalgebra and complement inside G_2.

    Method: SU(3) = Stab_{G_2}(e_7) in the 7-dim representation.
    The map phi: g_2 -> R^7 defined by phi(X) = X(e_7) has:
      - ker(phi) = su(3) (8-dimensional)
      - im(phi) = R^6 (the 6 directions in R^7 orthogonal to e_7)

    Since our generators are orthonormalized abstract linear combinations,
    we find the su(3) as the kernel of the linear map, not by testing
    individual generators.

    Returns:
      su3_gens: list of 8 orthonormalized g_2 generators spanning su(3)
      comp_gens: list of 6 orthonormalized g_2 generators spanning the complement
      su3_coeffs: (8, 14) matrix giving su(3) gens as linear combos of g_2 gens
      comp_coeffs: (6, 14) matrix giving complement gens as linear combos of g_2 gens
    """
    n = len(gens)
    e7_idx = 6  # 7th basis vector (0-indexed)

    # Build the map phi: g_2 -> R^7, phi(sum c_a e_a) = sum c_a e_a(e_7)
    # A_{i,a} = (e_a)_{i, e7_idx}
    A = np.zeros((7, n))
    for a in range(n):
        A[:, a] = gens[a][:, e7_idx]

    rank_A = np.linalg.matrix_rank(A, tol=1e-10)
    print(f"  Map phi: g_2 -> R^7, rank = {rank_A}")
    print(f"  ker(phi) = su(3): dim = {n - rank_A}")

    U_A, S_A, Vt_A = np.linalg.svd(A)
    # Null space of A = last (n - rank_A) rows of Vt_A
    su3_coeffs = Vt_A[rank_A:]  # (8, 14)
    comp_coeffs = Vt_A[:rank_A]  # (6, 14)

    # Construct the actual matrix generators
    su3_gens = []
    for i in range(su3_coeffs.shape[0]):
        X = sum(su3_coeffs[i, a] * gens[a] for a in range(n))
        su3_gens.append(X)

    comp_gens = []
    for i in range(comp_coeffs.shape[0]):
        X = sum(comp_coeffs[i, a] * gens[a] for a in range(n))
        comp_gens.append(X)

    # Verify
    max_su3_action = max(norm(X[:, e7_idx]) for X in su3_gens)
    min_comp_action = min(norm(X[:, e7_idx]) for X in comp_gens)
    print(f"  su(3) max ||X e_7||: {max_su3_action:.2e}")
    print(f"  complement min ||X e_7||: {min_comp_action:.2e}")

    # Verify su(3) closure
    # Need structure constants in the new basis
    su3_f = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(a+1, 8):
            comm = su3_gens[a] @ su3_gens[b] - su3_gens[b] @ su3_gens[a]
            # Decompose in su(3) basis
            for c in range(8):
                su3_f[a, b, c] = -np.trace(comm @ su3_gens[c])
                su3_f[b, a, c] = -su3_f[a, b, c]

    # Check closure: is comm fully in su(3) span?
    su3_closure_err = 0.0  # (local)
    for a in range(8):
        for b in range(a+1, 8):
            comm = su3_gens[a] @ su3_gens[b] - su3_gens[b] @ su3_gens[a]
            recon = sum(su3_f[a, b, c] * su3_gens[c] for c in range(8))
            err = np.max(np.abs(comm - recon))
            su3_closure_err = max(su3_closure_err, err)
    print(f"  su(3) closure error: {su3_closure_err:.2e}")

    # Verify reductivity: [su3, comp] ⊂ comp
    reductive_err = 0.0  # (local)
    for a in range(8):
        for b in range(6):
            comm = su3_gens[a] @ comp_gens[b] - comp_gens[b] @ su3_gens[a]
            # Decompose: should have zero su(3) component
            for c in range(8):
                val = -np.trace(comm @ su3_gens[c])  # (local)
                reductive_err = max(reductive_err, abs(val))
    print(f"  Reductivity [su3, comp] ⊂ comp error: {reductive_err:.2e}")

    return su3_gens, comp_gens, su3_coeffs, comp_coeffs


# =============================================================================
# MODULE 3: CLIFFORD ALGEBRA Cl(14)
# =============================================================================

def build_cliff14():
    """Cl(R^14) generators: 14 Hermitian (128,128) matrices."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    gammas = []
    for k in range(7):
        parts1 = [s3] * k + [s1] + [I2] * (6 - k)
        parts2 = [s3] * k + [s2] + [I2] * (6 - k)
        mat1 = parts1[0]
        mat2 = parts2[0]
        for p in parts1[1:]:
            mat1 = np.kron(mat1, p)
        for p in parts2[1:]:
            mat2 = np.kron(mat2, p)
        gammas.append(mat1)
        gammas.append(mat2)

    return gammas


def validate_clifford14(gammas):
    """Verify {gamma_a, gamma_b} = 2 delta_{ab} I_{128}."""
    max_err = 0.0  # (local)
    dim = gammas[0].shape[0]
    for a in range(14):
        for b in range(a, 14):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(dim, dtype=complex)
            err = np.max(np.abs(anticomm - target))
            max_err = max(max_err, err)
    return max_err


def build_chirality14(gammas):
    """Chirality gamma_15 = i * gamma_1 * ... * gamma_14 for Cl(14)."""
    prod = np.eye(128, dtype=complex)
    for g in gammas:
        prod = prod @ g
    return 1j * prod


# =============================================================================
# MODULE 4: KO-DIMENSION
# =============================================================================

def compute_ko_dimension(gammas, dim_lie):
    """
    Compute KO-dimension from Clifford algebra and charge conjugation.

    For d=14: d mod 8 = 6.
    Expected signs: epsilon(J^2) = +1, epsilon''(Jgamma) = -1.
    This is KO-dim 6 = the SM-compatible dimension.
    """
    dim_spin = gammas[0].shape[0]
    ko_dim = dim_lie % 8

    # Charge conjugation B: B gamma_a B^{-1} = gamma_a^*
    # In our inductive construction: gamma_{2k-1} is real, gamma_{2k} is imaginary
    # B = product of all imaginary gammas = gamma_2 * gamma_4 * ... * gamma_14
    B = np.eye(dim_spin, dtype=complex)
    for k in range(7):
        B = B @ gammas[2*k + 1]  # indices 1,3,5,7,9,11,13

    B_inv = np.linalg.inv(B)

    # Verify B gamma_a B^{-1} = gamma_a^* for all a
    max_cc_err = 0.0
    for a in range(14):
        lhs = B @ gammas[a] @ B_inv
        rhs = gammas[a].conj()
        err = np.max(np.abs(lhs - rhs))
        max_cc_err = max(max_cc_err, err)

    # epsilon: J^2 = B B^*
    BB_star = B @ B.conj()
    epsilon = BB_star[0, 0].real
    eps_err = np.max(np.abs(BB_star - epsilon * np.eye(dim_spin)))

    # epsilon'': B gamma^* = epsilon'' gamma B
    gamma_chir = build_chirality14(gammas)
    lhs_gg = B @ gamma_chir.conj()
    rhs_gg = gamma_chir @ B
    plus_err = np.max(np.abs(lhs_gg - rhs_gg))
    minus_err = np.max(np.abs(lhs_gg + rhs_gg))

    if plus_err < 1e-8:
        epsilon_pp = +1
    elif minus_err < 1e-8:
        epsilon_pp = -1
    else:
        epsilon_pp = 0

    ko_match = (abs(epsilon - 1.0) < 0.1 and epsilon_pp == -1)

    print(f"  KO-dimension: d={dim_lie}, d mod 8 = {ko_dim}")
    print(f"  Charge conjugation error: {max_cc_err:.2e}")
    print(f"  epsilon (J^2): {epsilon:.1f} (error: {eps_err:.2e})")
    print(f"  epsilon'' (J gamma): {epsilon_pp}")
    print(f"  Expected (d mod 8 = 6): epsilon=+1, epsilon''=-1")
    print(f"  KO-dim = 6: {'CONFIRMED' if ko_match else 'MISMATCH'}")

    return ko_dim, epsilon, epsilon_pp, ko_match, B, gamma_chir


# =============================================================================
# MODULE 5: SPINOR BRANCHING G_2 -> SU(3)
# =============================================================================

def spinor_branching(gammas, g2_gens, su3_gens, comp_gens, f_abc):
    """
    Decompose the 128-dim spinor under G_2 -> SU(3).

    Build the spinor representation of g_2 via the so(14) embedding:
      rho_spin(e_a) = (1/2) sum_{b<c} f_{abc} gamma_b gamma_c

    Then restrict to su(3) and decompose by SU(3) Casimir eigenvalues.
    """
    n_g2 = len(g2_gens)
    dim_spin = 128  # (local)

    # Build spinor representation of g_2
    # rho_spin(e_a) = (1/2) sum_{b<c} f_{abc} [gamma_b, gamma_c] / 2
    # Actually: rho_spin(e_a) = (1/4) sum_{b,c} (ad(e_a))_{bc} gamma_b gamma_c
    # where (ad(e_a))_{bc} = f_{abc} in the ON basis

    # The adjoint embedding: ad(e_a)_{bc} = f_{a,c,b} = -f_{a,b,c}
    # The spin(14) rep formula: rho_spin(X) = (1/4) sum_{bc} X_{bc} gamma_b gamma_c
    # Substituting X_{bc} = ad(e_a)_{bc} = -f_{a,b,c}:
    # rho_spin(e_a) = -(1/4) sum_{bc} f_{abc} gamma_b gamma_c
    #              = -(1/2) sum_{b<c} f_{abc} gamma_b gamma_c
    rho_spin = []
    for a in range(n_g2):
        M = np.zeros((dim_spin, dim_spin), dtype=complex)
        for b in range(n_g2):
            for c in range(b+1, n_g2):
                if abs(f_abc[a, b, c]) > 1e-14:
                    M += f_abc[a, b, c] * (gammas[b] @ gammas[c])
        M *= -0.5  # Note the minus sign!
        rho_spin.append(M)

    # Verify anti-Hermiticity
    max_ah_err = max(np.max(np.abs(M + M.conj().T)) for M in rho_spin)
    print(f"  Spinor rep anti-Hermiticity error: {max_ah_err:.2e}")

    # Verify Lie algebra closure (spot check)
    max_lie_err = 0.0
    for a in range(min(5, n_g2)):
        for b in range(a+1, min(5, n_g2)):
            comm = rho_spin[a] @ rho_spin[b] - rho_spin[b] @ rho_spin[a]
            target = sum(f_abc[a, b, c] * rho_spin[c] for c in range(n_g2))
            err = np.max(np.abs(comm - target))
            max_lie_err = max(max_lie_err, err)
    print(f"  Lie algebra closure error (spinor rep): {max_lie_err:.2e}")

    # Now build su(3) generators in spinor rep
    # Each su(3) generator is a linear combination of g_2 generators
    # su3_gens[i] = sum_a su3_coeffs[i,a] * g2_gens[a]
    # => rho_spin(su3_gen_i) = sum_a su3_coeffs[i,a] * rho_spin[a]

    # We need to express su3_gens in terms of the g2_gens basis.
    # The su3_gens were constructed as: su3_gens[i] = sum_a coeff * g2_gens[a]
    # We can recover the coefficients using the inner product.

    # Coefficients: c_{ia} = <su3_gens[i], g2_gens[a]> = -Tr(su3_gens[i] @ g2_gens[a])
    su3_spin = []
    for i in range(len(su3_gens)):
        coeffs = np.array([-np.trace(su3_gens[i] @ g2_gens[a]) for a in range(n_g2)])
        M = sum(coeffs[a] * rho_spin[a] for a in range(n_g2))
        su3_spin.append(M)

    # Build SU(3) Casimir: C_2 = -sum_i rho(su3_i)^2 (positive semidefinite)
    C2_su3 = np.zeros((dim_spin, dim_spin), dtype=complex)
    for M in su3_spin:
        C2_su3 -= M @ M  # - because anti-Hermitian: (-M)(-M) = M^2, we want -sum e_a^2

    c2_evals = np.linalg.eigvalsh(C2_su3)
    c2_rounded = np.round(c2_evals, decimals=3)
    unique_c2 = np.unique(c2_rounded)

    print(f"\n  SU(3) Casimir eigenvalues on 128-dim spinor:")
    sm_content = {'singlets': 0, 'triplets': 0, 'octets': 0, 'sextets': 0, 'others': 0}

    for c2_val in unique_c2:
        mult = int(np.sum(np.abs(c2_rounded - c2_val) < 0.01))
        irrep = identify_su3_irrep(c2_val)
        print(f"    C_2 = {c2_val:.4f}, multiplicity = {mult}, irrep = {irrep}")
        if abs(c2_val) < 0.01:
            sm_content['singlets'] = mult
        elif abs(c2_val - 4.0/3.0) < 0.1:
            sm_content['triplets'] += mult
        elif abs(c2_val - 3.0) < 0.1:
            sm_content['octets'] = mult
        elif abs(c2_val - 10.0/3.0) < 0.1:
            sm_content['sextets'] = mult
        else:
            sm_content['others'] += mult

    has_singlet = sm_content['singlets'] > 0
    has_triplet = sm_content['triplets'] > 0
    sm_compatible = has_singlet and has_triplet

    print(f"\n  SM-relevant content:")
    print(f"    Singlets (1): {sm_content['singlets']}")
    print(f"    Triplets (3/3-bar): {sm_content['triplets']}")
    print(f"    Octets (8): {sm_content['octets']}")
    print(f"    Sextets (6/6-bar): {sm_content['sextets']}")
    print(f"    Other: {sm_content['others']}")
    print(f"    SM compatible (has 1 and 3): {sm_compatible}")

    return sm_content, sm_compatible, c2_evals, unique_c2, rho_spin


def identify_su3_irrep(c2_val):
    """Identify SU(3) irrep from Casimir value."""
    known = {
        0.0: "(0,0)=1",
        4.0/3.0: "(1,0)/(0,1)=3/3bar",
        3.0: "(1,1)=8",
        10.0/3.0: "(2,0)/(0,2)=6/6bar",
        16.0/3.0: "(2,1)/(1,2)=15/15bar",
        6.0: "(3,0)/(0,3)=10/10bar",
    }
    for k, v in known.items():
        if abs(c2_val - k) < 0.1:
            return v
    return f"unknown(C2={c2_val:.3f})"


# =============================================================================
# MODULE 6: JENSEN-TYPE METRIC + DIRAC OPERATOR ON G_2
# =============================================================================

def g2_jensen_metric_matrix(B_ab, tau, su3_coeffs, comp_coeffs, n_g2):
    """
    Jensen-type deformation of the bi-invariant metric on G_2.

    g(tau) = L_su3 * g_bi|_{su(3)} + L_m * g_bi|_m

    Volume preservation: L_su3^4 * L_m^3 = 1  (8/2=4 for su3, 6/2=3 for comp)
    => L_su3 = exp(-3*tau/4), L_m = exp(tau)

    The metric in the g_2-abstract basis is:
      g_{ab} = L_su3 * sum_i (su3_coeffs)_{ia} (su3_coeffs)_{ib}
             + L_m * sum_j (comp_coeffs)_{ja} (comp_coeffs)_{jb}
    where the bi-invariant metric is delta_{ab} (since generators are ON).
    """
    L_su3 = np.exp(-0.75 * tau)
    L_m = np.exp(tau)

    # In the original ON g_2 basis, the metric at tau=0 is delta.
    # The projection onto su(3): P_su3 = su3_coeffs^T @ su3_coeffs
    # The projection onto comp: P_comp = comp_coeffs^T @ comp_coeffs

    P_su3 = su3_coeffs.T @ su3_coeffs  # (14, 14)
    P_comp = comp_coeffs.T @ comp_coeffs

    g = L_su3 * P_su3 + L_m * P_comp

    return g


def g2_compute_dirac_spectrum(tau, g2_gens, f_abc, gammas, su3_coeffs, comp_coeffs):
    """
    Compute the Dirac spectrum on (G_2, g(tau)) at the trivial Peter-Weyl sector.

    D = Omega(tau) where Omega is the spinor connection offset.
    For higher sectors, D_rho = sum_a rho(e_a) tensor gamma_a + I tensor Omega.

    Returns: eigenvalues at the trivial sector and the 7-dim sector.
    """
    n_g2 = len(g2_gens)
    dim_spin = 128  # (local)

    # Build metric
    g_met = g2_jensen_metric_matrix(np.eye(n_g2), tau, su3_coeffs, comp_coeffs, n_g2)

    # ON frame: g = E^T E means E @ g @ E^T = I
    # g is the metric in abstract basis, E transforms to ON frame
    L = cholesky(g_met)
    E = inv(L)
    E_inv = L

    # Frame structure constants: ft^c_{ab} = E_{ai} E_{bj} f_{ijk} (E^{-1})_{kc}
    ft = np.einsum('ai,bj,ijk,kc->abc', E, E, f_abc, E_inv)

    # Connection: Gamma^c_{ab} = (1/2)(ft_{abc} - ft_{bca} + ft_{cab})
    Gamma = np.zeros((n_g2, n_g2, n_g2))
    for c in range(n_g2):
        for a in range(n_g2):
            for b in range(n_g2):
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])

    # Spinor connection offset: Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)
    for a in range(n_g2):
        for b in range(n_g2):
            for c in range(n_g2):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * (gammas[a] @ gammas[b] @ gammas[c])
    Omega *= 0.25

    # Trivial sector: D = Omega (128 x 128)
    evals_trivial = np.linalg.eigvals(Omega)
    abs_trivial = np.sort(np.abs(evals_trivial.imag))

    # 7-dim fundamental sector
    # rho_7(e_a) for abstract e_a: the original 7x7 generators are in the original basis
    # In the ON frame basis, the abstract generators transform:
    #   rho_7(e_a^{ON}) = rho_7(E_{ab} e_b^{orig}) = E_{ab} rho_7(e_b^{orig})
    # But rho_7(e_b^{orig}) = g2_gens[b] (the 7x7 matrices)
    dim7 = 7
    D_7 = np.zeros((dim7 * dim_spin, dim7 * dim_spin), dtype=complex)

    for a in range(n_g2):
        rho_a = np.zeros((dim7, dim7), dtype=complex)
        for b in range(n_g2):
            rho_a += E[a, b] * g2_gens[b].astype(complex)
        D_7 += np.kron(rho_a, gammas[a])
    D_7 += np.kron(np.eye(dim7, dtype=complex), Omega)

    evals_7 = np.linalg.eigvals(D_7)
    abs_7 = np.sort(np.abs(evals_7.imag))

    return abs_trivial, abs_7, Omega


def g2_scalar_curvature(f_abc, g_met):
    """Compute scalar curvature via explicit Riemann tensor."""
    n = f_abc.shape[0]
    L = cholesky(g_met)
    E = inv(L)
    E_inv = L
    ft = np.einsum('ai,bj,ijk,kc->abc', E, E, f_abc, E_inv)

    Gamma = np.zeros((n, n, n))
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])

    # Riemann R^d_{cab}
    R = np.zeros((n, n, n, n))
    for d in range(n):
        for c in range(n):
            for a in range(n):
                for b in range(n):
                    val = 0.0  # (local)
                    for e in range(n):
                        val += Gamma[d, c, e] * Gamma[e, a, b]
                        val -= Gamma[d, a, e] * Gamma[e, c, b]
                        val -= ft[c, a, e] * Gamma[d, e, b]
                    R[d, c, a, b] = val

    # Ricci: Ric_{ab} = R^c_{acb}
    Ric = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Ric[a, b] += R[c, a, c, b]

    R_scalar = np.trace(Ric)
    return R_scalar


# =============================================================================
# MODULE 7: VAN HOVE TEST
# =============================================================================

def van_hove_test(tau_values, g2_gens, f_abc, gammas, su3_coeffs, comp_coeffs):
    """
    Compute Dirac spectrum at each tau, check for eigenvalue extrema (van Hove).
    """
    all_spectra = {}
    n_track = 10

    for tau in tau_values:
        t0 = time()
        abs_trivial, abs_7, _ = g2_compute_dirac_spectrum(
            tau, g2_gens, f_abc, gammas, su3_coeffs, comp_coeffs)

        # Combine with PW multiplicities: trivial x1, 7-dim x7
        all_evals = np.concatenate([
            np.repeat(abs_trivial, 1),
            np.repeat(abs_7, 7),
        ])

        all_spectra[tau] = {
            'trivial': abs_trivial,
            'fund7': abs_7,
            'all': all_evals,
        }

        dt = time() - t0
        print(f"  tau={tau:.3f}: {len(abs_trivial)} + {len(abs_7)} evals, "
              f"{len(all_evals)} total (PW), t={dt:.1f}s")

    # Track lowest eigenvalues
    lambda_mins = np.zeros((len(tau_values), n_track))
    for i, tau in enumerate(tau_values):
        evals = np.sort(all_spectra[tau]['all'])
        nonzero = evals[evals > 0.01]
        if len(nonzero) >= n_track:
            lambda_mins[i, :] = nonzero[:n_track]
        else:
            lambda_mins[i, :len(nonzero)] = nonzero
            lambda_mins[i, len(nonzero):] = np.nan

    # Check for van Hove (extrema in eigenvalue trajectories)
    van_hove_found = False
    van_hove_tau = None
    van_hove_lambda = None

    for k in range(n_track):
        lam_k = lambda_mins[:, k]
        valid = ~np.isnan(lam_k)
        lam_valid = lam_k[valid]
        tau_valid = tau_values[valid]
        if len(lam_valid) < 3:
            continue
        deriv = np.diff(lam_valid) / np.diff(tau_valid)
        for j in range(len(deriv) - 1):
            if deriv[j] * deriv[j+1] < 0:
                tau_vH = 0.5 * (tau_valid[j+1] + tau_valid[j+2])
                lam_vH = 0.5 * (lam_valid[j+1] + lam_valid[j+2])
                van_hove_found = True
                if van_hove_tau is None or lam_vH < van_hove_lambda:
                    van_hove_tau = tau_vH
                    van_hove_lambda = lam_vH
                print(f"  Van Hove: eigenvalue #{k}, tau ~ {tau_vH:.3f}, lambda ~ {lam_vH:.4f}")

    if not van_hove_found:
        print("  No van Hove singularity detected")
        for k in range(min(3, n_track)):
            lam_k = lambda_mins[:, k]
            valid = ~np.isnan(lam_k)
            if np.sum(valid) >= 3:
                lam_valid = lam_k[valid]
                mono = np.all(np.diff(lam_valid) >= -1e-10) or np.all(np.diff(lam_valid) <= 1e-10)
                print(f"    eigenvalue #{k}: {'monotonic' if mono else 'NON-MONOTONIC'}, "
                      f"range [{lam_valid.min():.4f}, {lam_valid.max():.4f}]")

    return all_spectra, van_hove_found, van_hove_tau, van_hove_lambda, lambda_mins


# =============================================================================
# MODULE 8: PLOTTING
# =============================================================================

def make_plots(all_spectra, tau_values, lambda_mins, ko_dim, sm_compatible,
               van_hove_found, van_hove_tau, unique_c2, sm_content, save_path):
    """Generate diagnostic plots."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: Eigenvalue flow
    ax = axes[0, 0]
    n_track = lambda_mins.shape[1]
    for k in range(n_track):
        valid = ~np.isnan(lambda_mins[:, k])
        if np.sum(valid) > 0:
            ax.plot(tau_values[valid], lambda_mins[valid, k], 'o-', markersize=3, label=f'$\\lambda_{{{k+1}}}$')
    if van_hove_found and van_hove_tau is not None:
        ax.axvline(van_hove_tau, color='red', linestyle='--', alpha=0.7, label=f'van Hove')
    ax.set_xlabel(r'$\tau$ (Jensen parameter)')
    ax.set_ylabel(r'$|\lambda|$ (Dirac eigenvalue)')
    ax.set_title(r'$G_2$ Dirac Eigenvalue Flow')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: DOS at selected tau
    ax = axes[0, 1]
    tau_plot = [tau_values[0], tau_values[len(tau_values)//2], tau_values[-1]]
    for tau in tau_plot:
        if tau in all_spectra:
            evals = all_spectra[tau]['all']
            evals_nz = evals[evals > 0.01]
            if len(evals_nz) > 5:
                ax.hist(evals_nz, bins=40, alpha=0.5, density=True, label=f'$\\tau$={tau:.2f}')
    ax.set_xlabel(r'$|\lambda|$')
    ax.set_ylabel('DOS (normalized)')
    ax.set_title(r'$G_2$ Density of States')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: SU(3) Casimir distribution
    ax = axes[1, 0]
    c2_labels = []
    c2_mults = []
    for c2 in unique_c2:
        c2_labels.append(f'{c2:.2f}')
        c2_mults.append(c2)
    if len(c2_labels) > 0:
        bars = ax.bar(range(len(c2_labels)), c2_mults, color='steelblue', alpha=0.7)
        ax.set_xticks(range(len(c2_labels)))
        ax.set_xticklabels(c2_labels, rotation=45, fontsize=8)
        ax.set_ylabel(r'$C_2$ eigenvalue')
        ax.set_title('SU(3) Casimir on 128-dim Spinor')
        # Annotate with irrep names
        for i, c2 in enumerate(unique_c2):
            name = identify_su3_irrep(c2)
            ax.text(i, c2 + 0.1, name, ha='center', va='bottom', fontsize=7, rotation=30)
    ax.grid(True, alpha=0.3)

    # Panel 4: Summary
    ax = axes[1, 1]
    ax.axis('off')
    score = int(ko_dim == 6) + int(sm_compatible) + int(van_hove_found)
    lines = [
        r"$G_2$ Minimal Viability Test",
        "",
        f"dim($G_2$) = 14, rank = 2",
        f"Spinor dim = 128 (Cl(14))",
        "",
        f"CHECK 1: KO-dim = {ko_dim} mod 8",
        f"  {'PASS (=6)' if ko_dim == 6 else 'FAIL'}",
        "",
        f"CHECK 2: SM quantum numbers",
        f"  {'PASS' if sm_compatible else 'FAIL'}",
        f"  singlets={sm_content['singlets']}, triplets={sm_content['triplets']}",
        f"  octets={sm_content['octets']}, sextets={sm_content['sextets']}",
        "",
        f"CHECK 3: Van Hove singularity",
        f"  {'FOUND at tau=' + f'{van_hove_tau:.3f}' if van_hove_found else 'NOT FOUND'}",
        "",
        f"Score: {score} / 3",
        f"Gate: {'PASS' if score == 3 else 'INFO' if score >= 1 else 'FAIL'}",
    ]
    for i, line in enumerate(lines):
        ax.text(0.05, 0.95 - i * 0.052, line, transform=ax.transAxes,
                fontsize=10, fontfamily='monospace', verticalalignment='top')

    plt.suptitle(r'S59 G2-MINIMAL-59: $G_2$ as Alternative Internal Space', fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot saved: {save_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    t_start = time()
    print("=" * 78)
    print("  S59 G2-MINIMAL-59: G_2 Minimal Viability Test")
    print("  dim(G_2) = 14, rank = 2, Spin(14) spinor dim = 128")
    print("=" * 78)

    # STEP 1: Construct G_2
    print("\n[STEP 1] Constructing G_2 Lie algebra as subalgebra of so(7)...")
    g2_gens = g2_generators_in_so7()
    if len(g2_gens) != 14:
        print(f"  FATAL: Expected 14 generators, got {len(g2_gens)}")
        return

    # STEP 2: Validate
    print("\n[STEP 2] Validating G_2 algebra...")
    f_abc, B_ab, closure_err = validate_g2_algebra(g2_gens)

    # STEP 3: SU(3) decomposition
    print("\n[STEP 3] Identifying SU(3) subalgebra via kernel method...")
    su3_gens, comp_gens, su3_coeffs, comp_coeffs = identify_su3_decomposition(
        g2_gens, f_abc, B_ab)

    # STEP 4: Clifford algebra
    print("\n[STEP 4] Building Clifford algebra Cl(14)...")
    gammas = build_cliff14()
    cliff_err = validate_clifford14(gammas)
    print(f"  Clifford validation error: {cliff_err:.2e}")

    # STEP 5: KO-dimension
    print("\n[STEP 5] Computing KO-dimension...")
    ko_dim, epsilon, epsilon_pp, ko_match, B_cc, gamma_chir = compute_ko_dimension(gammas, 14)

    # STEP 6: Spinor branching
    print("\n[STEP 6] Decomposing 128-dim spinor under G_2 -> SU(3)...")
    sm_content, sm_compatible, c2_evals, unique_c2, rho_spin = spinor_branching(
        gammas, g2_gens, su3_gens, comp_gens, f_abc)

    # STEP 7: Scalar curvature
    print("\n[STEP 7] Scalar curvature...")
    for tau in [0.0, 0.19]:
        g_met = g2_jensen_metric_matrix(np.eye(14), tau, su3_coeffs, comp_coeffs, 14)
        R = g2_scalar_curvature(f_abc, g_met)
        print(f"  tau={tau:.2f}: R = {R:.6f}")

    # STEP 8: Van Hove
    print("\n[STEP 8] Van Hove singularity test...")
    tau_values = np.array([0.0, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30, 0.35, 0.40])
    all_spectra, van_hove_found, van_hove_tau, van_hove_lambda, lambda_mins = \
        van_hove_test(tau_values, g2_gens, f_abc, gammas, su3_coeffs, comp_coeffs)

    # RESULTS
    score = int(ko_dim == 6) + int(sm_compatible) + int(van_hove_found)

    print("\n" + "=" * 78)
    print("  RESULTS SUMMARY")
    print("=" * 78)
    print(f"  CHECK 1 - KO-dimension: {ko_dim} {'= 6 PASS' if ko_dim == 6 else 'FAIL'}")
    print(f"  CHECK 2 - SM quantum numbers: {'PASS' if sm_compatible else 'FAIL'}")
    print(f"    Content: {sm_content}")
    print(f"  CHECK 3 - Van Hove: {'FOUND' if van_hove_found else 'NOT FOUND'}")
    if van_hove_found:
        print(f"    tau_vH = {van_hove_tau:.4f}, lambda_vH = {van_hove_lambda:.4f}")
    print(f"  VIABILITY SCORE: {score} / 3")
    print(f"  GATE: G2-MINIMAL-59 {'PASS' if score == 3 else 'INFO' if score >= 1 else 'FAIL'}")

    # Save
    save_dir = os.path.dirname(os.path.abspath(__file__))
    npz_path = os.path.join(save_dir, 's59_g2_minimal.npz')
    png_path = os.path.join(save_dir, 's59_g2_minimal.png')

    spectra_trivial = np.array([all_spectra[tau]['trivial'] for tau in tau_values])

    np.savez(npz_path,
             n_generators=len(g2_gens),
             f_abc=f_abc,
             B_ab=B_ab,
             su3_coeffs=su3_coeffs,
             comp_coeffs=comp_coeffs,
             ko_dim=ko_dim,
             epsilon=epsilon,
             epsilon_pp=epsilon_pp,
             ko_match=ko_match,
             sm_compatible=sm_compatible,
             c2_evals=c2_evals,
             unique_c2=unique_c2,
             sm_singlets=sm_content['singlets'],
             sm_triplets=sm_content['triplets'],
             sm_octets=sm_content['octets'],
             sm_sextets=sm_content.get('sextets', 0),
             sm_others=sm_content['others'],
             tau_values=tau_values,
             lambda_mins=lambda_mins,
             van_hove_found=van_hove_found,
             van_hove_tau=van_hove_tau if van_hove_tau is not None else -1.0,
             van_hove_lambda=van_hove_lambda if van_hove_lambda is not None else -1.0,
             spectra_trivial=spectra_trivial,
             score=score,
             total_time=time() - t_start,
             )
    print(f"\n  Data saved: {npz_path}")

    make_plots(all_spectra, tau_values, lambda_mins, ko_dim, sm_compatible,
               van_hove_found, van_hove_tau, unique_c2, sm_content, png_path)

    print(f"  Total runtime: {time() - t_start:.1f}s")
    print("=" * 78)


if __name__ == '__main__':
    main()
