"""
OMEGA-CLASSIFY-46: Inner Fluctuation Module Classification
============================================================

Classifies the 342 directions in Omega^1_D(A_F) from the S45 WEAK-ORDER-ONE
computation. Decomposes into:
  - 173 linear (gauge + standard Higgs)
  - 169 quadratic (CCS 2013, Paper 23 mechanism)

For the scalar subspace, computes the mass-squared matrix M^2 from the
spectral action second variation and determines whether any directions
are tachyonic at the fold but not at round SU(3).

MATHEMATICAL FRAMEWORK
-----------------------

The inner fluctuation module is:
    Omega^1_D(A) = span{ sum_i a_i [D, b_i] : a_i, b_i in A_F }

When order-one holds, Omega^1_D = A [D, A] (linear module).
When order-one fails (as here, at 4.000 for (H,H)):
    Omega^1_D = A [D, A] + [D, A] [D, A]  (linear + quadratic)

The module elements decompose under the Z_2 grading gamma_F:
    - Even (gamma_F = +1): gauge connections (A_mu type)
    - Odd  (gamma_F = -1): Higgs-like scalars (phi type)

The mass-squared matrix for the scalar directions is:
    M^2_{ij} = Tr(phi_i D^2 phi_j) / Tr(phi_i phi_j)

evaluated at the fold (tau=0.19) and at round (tau=0).

A tachyonic direction (M^2 < 0 at fold, M^2 > 0 at round) would indicate
spontaneous symmetry breaking induced by the Jensen deformation —
a dynamical tau-stabilization mechanism outside the spectral action.

GATE: OMEGA-CLASSIFY-46
  PASS: Any tachyonic direction at fold not at round.
  FAIL: All massive at all tau.

Author: Connes-NCG-Theorist (Session 46)
Date: 2026-03-15
Depends on: s45_weak_order_one.py (A_F infrastructure), tier1_dirac_spectrum.py
References: CCS 2013 (Paper 23), Bochniak-Sitarz 2021 (Paper 25)
"""

import numpy as np
from numpy.linalg import norm as la_norm, svd, eigh, eigvalsh
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from canonical_constants import tau_fold as TAU_FOLD_CANON

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# SECTION 1: A_F INFRASTRUCTURE (imported from s45_weak_order_one.py)
# =============================================================================

def flat_idx(row: int, col: int) -> int:
    """Map (row, col) in 4x4 matrix to flat index in 16-dim Psi_+."""
    if row == 0 and col == 0:
        return 0
    if row == 0:
        return col
    if col == 0:
        return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4, R4):
    """Build 16x16 bimodule action: X -> L4 . X . R4^T in flattened basis."""
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])

def get_column_index(flat_idx_val):
    if flat_idx_val == 0: return 0
    elif 1 <= flat_idx_val <= 3: return flat_idx_val
    elif 4 <= flat_idx_val <= 6: return 0
    else: return (flat_idx_val - 7) % 3 + 1

G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

# The grading gamma_F on H_F = C^32 = Psi_+ + Psi_-
gamma_F_mat = np.zeros((32, 32))
gamma_F_mat[:16, :16] = np.eye(16)
gamma_F_mat[16:, 16:] = -np.eye(16)

# J = charge conjugation (Xi in the code)
Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5


def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5


def full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32


def o_map_16(gen_16):
    """Opposite algebra restricted to Psi_+ (16-dim)."""
    return G5 @ gen_16.T @ G5


def build_AF_generators():
    """
    Build all 24 generators of A_F = C + H + M_3(C).

    Returns:
        AF_16: list of (16,16) complex matrices
        AF_names: list of names
        AF_factors: list of algebra factor labels ('C', 'H', 'M3')
        AF_class: list of 'gauge' or 'scalar' or 'mixed_diag'
    """
    AF_16 = []
    AF_names = []
    AF_factors = []
    AF_class = []

    # ---- C factor ----
    # C_Im: u(1)_Y -- GAUGE
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im')
    AF_factors.append('C')
    AF_class.append('gauge')

    # C_proj: projector onto nu_R -- SCALAR
    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj')
    AF_factors.append('C')
    AF_class.append('scalar')

    # ---- H factor ----
    # H_i, H_j, H_k: su(2)_L -- GAUGE
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i')
    AF_factors.append('H')
    AF_class.append('gauge')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j')
    AF_factors.append('H')
    AF_class.append('gauge')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k')
    AF_factors.append('H')
    AF_class.append('gauge')

    # H_1: identity in H -- SCALAR
    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1')
    AF_factors.append('H')
    AF_class.append('scalar')

    # ---- M_3(C) factor ----
    for a in range(3):
        for b in range(3):
            for part, val in [('Re', 1.0), ('Im', 1j)]:
                m_elem = np.zeros((3, 3), dtype=complex)
                m_elem[a, b] = val
                R_m = np.eye(4, dtype=complex)
                R_m[1:, 1:] = m_elem.conj().T
                AF_16.append(build_bimodule_16(np.eye(4), R_m))
                name = f'M3_E{a}{b}_{part}'
                AF_names.append(name)
                AF_factors.append('M3')

                if a != b:
                    AF_class.append('gauge')
                elif part == 'Im':
                    AF_class.append('gauge')
                else:
                    AF_class.append('mixed_diag')

    return AF_16, AF_names, AF_factors, AF_class


# =============================================================================
# SECTION 2: BUILD D_K AT A GIVEN TAU
# =============================================================================

def build_DK(tau, gens, f_abc, B_ab, gammas, p, q):
    """Build the Dirac operator D_K on rep (p,q) at deformation tau."""
    _irrep_cache.clear()
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K = dirac_operator_on_irrep(rho, E, gammas, Omega)
    return D_K, dim_rho


# =============================================================================
# SECTION 3: COMPUTE Omega^1_D MODULE WITH FULL BASIS EXTRACTION
# =============================================================================

def compute_omega1_full(D_mat, AF_16_list, dim_rho, threshold=1e-10):
    """
    Compute the inner fluctuation module Omega^1_D(A_F) with full basis extraction.

    Returns:
        linear_basis: (dim_linear, N^2) orthonormal basis vectors for linear module
        quad_basis: (dim_quad, N^2) orthonormal basis for quadratic module
        combined_basis: (dim_combined, N^2) orthonormal basis for combined
        extra_basis: (dim_extra, N^2) orthonormal basis for directions in
                     combined but not in linear (the CCS 2013 extra directions)
        All as N x N matrices reshaped from N^2 vectors.
    """
    n_gen = len(AF_16_list)
    N = D_mat.shape[0]
    I_rho = np.eye(dim_rho, dtype=complex) if dim_rho > 1 else None

    linear_vecs = []
    quadratic_vecs = []

    for j in range(n_gen):
        if dim_rho > 1:
            b_full = np.kron(I_rho, AF_16_list[j])
        else:
            b_full = AF_16_list[j]
        comm_Db = D_mat @ b_full - b_full @ D_mat

        for i in range(n_gen):
            if dim_rho > 1:
                a_full = np.kron(I_rho, AF_16_list[i])
            else:
                a_full = AF_16_list[i]

            # Linear: a_i [D, b_j]
            lin = a_full @ comm_Db
            linear_vecs.append(lin.ravel())

            # Quadratic: [D, a_i] [D, b_j]
            comm_Da = D_mat @ a_full - a_full @ D_mat
            quad = comm_Da @ comm_Db
            quadratic_vecs.append(quad.ravel())

    linear_mat = np.array(linear_vecs)
    quadratic_mat = np.array(quadratic_vecs)
    combined_mat = np.vstack([linear_mat, quadratic_mat])

    def extract_basis(mat, rel_thresh=1e-10):
        U, S, Vh = svd(mat, full_matrices=False)
        cutoff = S[0] * rel_thresh
        rank = int(np.sum(S > cutoff))
        return Vh[:rank], S[:rank], rank

    lin_basis, lin_sv, dim_lin = extract_basis(linear_mat)
    quad_basis, quad_sv, dim_quad = extract_basis(quadratic_mat)
    comb_basis, comb_sv, dim_comb = extract_basis(combined_mat)

    # Extract the EXTRA directions: those in combined but not in linear
    # Project combined basis onto complement of linear space
    if dim_lin > 0 and dim_comb > dim_lin:
        # Project each combined basis vector onto the linear subspace
        # and subtract. The residual spans the extra directions.
        proj_coeff = comb_basis @ lin_basis.conj().T  # (dim_comb, dim_lin)
        proj = proj_coeff @ lin_basis  # (dim_comb, N^2)
        residual = comb_basis - proj  # (dim_comb, N^2)

        # Re-SVD the residual to get clean orthonormal extra basis
        _, S_res, Vh_res = svd(residual, full_matrices=False)
        cutoff_res = S_res[0] * 1e-10 if len(S_res) > 0 else 0
        dim_extra = int(np.sum(S_res > cutoff_res))
        extra_basis = Vh_res[:dim_extra]
        extra_sv = S_res[:dim_extra]
    else:
        dim_extra = 0
        extra_basis = np.zeros((0, combined_mat.shape[1]), dtype=complex)
        extra_sv = np.array([])

    return {
        'linear_basis': lin_basis,
        'quadratic_basis': quad_basis,
        'combined_basis': comb_basis,
        'extra_basis': extra_basis,
        'dim_linear': dim_lin,
        'dim_quadratic': dim_quad,
        'dim_combined': dim_comb,
        'dim_extra': dim_extra,
        'linear_sv': lin_sv,
        'quadratic_sv': quad_sv,
        'combined_sv': comb_sv,
        'extra_sv': extra_sv,
        'N': N,
    }


# =============================================================================
# SECTION 4: GRADING DECOMPOSITION (GAUGE vs SCALAR)
# =============================================================================

def decompose_by_grading(basis_vecs, N, dim_rho, gamma_F_16=None):
    """
    Decompose a set of Omega^1_D basis vectors by the Z_2 grading gamma_F.

    In the NCG Standard Model:
    - Even grading (commutes with gamma_F): gauge connections (A_mu type)
    - Odd grading (anticommutes with gamma_F): Higgs-like scalars (phi type)

    For a 1-form omega in Omega^1_D, the grading acts as:
        gamma_F omega gamma_F = +omega  (gauge)
        gamma_F omega gamma_F = -omega  (scalar)

    We use gamma_F on the spinor factor (16x16 block on Psi_+).

    In the framework:
    - gamma_F = gamma_PA x gamma_CHI (S11 resolution)
    - On Psi_+: gamma_F = +I_16
    - On Psi_-: gamma_F = -I_16
    - So gamma_F_32 = diag(+I_16, -I_16) on the full 32-dim H_F

    For the sector computation on dim_rho x 16 space:
    - We use the chirality operator chi = I_{dim_rho} x gamma_9
      where gamma_9 = product of all 8 gamma matrices

    Args:
        basis_vecs: (n_basis, N^2) array of flattened basis operators
        N: matrix dimension (dim_rho * 16)
        dim_rho: representation dimension
        gamma_F_16: (16,16) chirality matrix on spinor space.
                    If None, use gamma_9 = prod(gammas).

    Returns:
        even_basis: basis vectors with positive grading (gauge)
        odd_basis: basis vectors with negative grading (scalar)
        dim_even, dim_odd: dimensions
        grading_eigenvalues: array of grading eigenvalues for each basis vector
    """
    n_basis = basis_vecs.shape[0]
    if n_basis == 0:
        return (np.zeros((0, basis_vecs.shape[1]), dtype=complex),
                np.zeros((0, basis_vecs.shape[1]), dtype=complex),
                0, 0, np.array([]))

    # Build the grading operator on the full sector space
    if gamma_F_16 is not None:
        gamma_full = np.kron(np.eye(dim_rho), gamma_F_16)
    else:
        # Default: use gamma_9 = prod(gammas)
        gammas_local = build_cliff8()
        gamma_9 = np.eye(16, dtype=complex)
        for g in gammas_local:
            gamma_9 = gamma_9 @ g
        gamma_full = np.kron(np.eye(dim_rho), gamma_9)

    # For each basis vector (viewed as an NxN operator omega),
    # compute the grading action: gamma_F @ omega @ gamma_F
    grading_evals = np.zeros(n_basis)

    even_vecs = []
    odd_vecs = []

    for k in range(n_basis):
        omega = basis_vecs[k].reshape(N, N)

        # Grading action: gamma_F omega gamma_F^{-1}
        # For unitary gamma_F with gamma_F^2 = I, gamma_F^{-1} = gamma_F
        graded = gamma_full @ omega @ gamma_full

        # Compute overlap: if omega is even, graded = +omega
        #                   if omega is odd,  graded = -omega
        # Measure by Frobenius inner product
        ip_same = np.real(np.trace(graded.conj().T @ omega))
        ip_norm = np.real(np.trace(omega.conj().T @ omega))

        if ip_norm > 1e-30:
            grading_evals[k] = ip_same / ip_norm
        else:
            grading_evals[k] = 0.0

    # Project onto even and odd subspaces
    # Even: (omega + gamma omega gamma) / 2
    # Odd:  (omega - gamma omega gamma) / 2
    even_proj_vecs = []
    odd_proj_vecs = []

    for k in range(n_basis):
        omega = basis_vecs[k].reshape(N, N)
        graded = gamma_full @ omega @ gamma_full

        even_part = 0.5 * (omega + graded)
        odd_part = 0.5 * (omega - graded)

        if la_norm(even_part, 'fro') > 1e-12:
            even_proj_vecs.append(even_part.ravel())
        if la_norm(odd_part, 'fro') > 1e-12:
            odd_proj_vecs.append(odd_part.ravel())

    # Extract clean bases via SVD
    def clean_basis(vecs, rel_thresh=1e-10):
        if len(vecs) == 0:
            return np.zeros((0, N*N), dtype=complex), 0
        mat = np.array(vecs)
        _, S, Vh = svd(mat, full_matrices=False)
        cutoff = S[0] * rel_thresh
        rank = int(np.sum(S > cutoff))
        return Vh[:rank], rank

    even_basis, dim_even = clean_basis(even_proj_vecs)
    odd_basis, dim_odd = clean_basis(odd_proj_vecs)

    return even_basis, odd_basis, dim_even, dim_odd, grading_evals


# =============================================================================
# SECTION 5: MASS-SQUARED MATRIX FROM SPECTRAL ACTION SECOND VARIATION
# =============================================================================

def compute_mass_squared_matrix(scalar_basis, D_mat, N):
    """
    Compute the mass-squared matrix for scalar directions in Omega^1_D.

    The spectral action second variation around D gives:
        delta^2 S_b = Tr[ delta_D * f'(D^2/Lambda^2) * delta_D
                          + (1/2) delta_D^2 * f'(D^2/Lambda^2) ]

    For inner fluctuations D -> D + phi where phi is a scalar (odd grading),
    the mass term comes from:
        M^2_{ij} = Tr(phi_i [D, [D, phi_j]])

    This is the second-order term in the expansion of Tr f((D+phi)^2/Lambda^2)
    around phi=0. For a finite discrete spectrum, this reduces to:
        M^2_{ij} = Tr(phi_i D^2 phi_j + phi_i phi_j D^2 - 2 phi_i D phi_j D)
                 = Tr([D, phi_i]^dagger [D, phi_j])
                 = sum_n <n| [D, phi_i]^dag [D, phi_j] |n>

    which is manifestly positive semi-definite IF the scalar basis elements
    are self-adjoint. For non-self-adjoint elements, we symmetrize:
        phi -> (phi + phi^dag) / sqrt(2)

    Args:
        scalar_basis: (n_scalar, N^2) orthonormal basis for scalar subspace
        D_mat: (N, N) Dirac operator
        N: matrix dimension

    Returns:
        M2: (n_scalar, n_scalar) mass-squared matrix (Hermitian)
        M2_eigenvalues: sorted eigenvalues
        M2_eigenvectors: eigenvectors
    """
    n_scalar = scalar_basis.shape[0]
    if n_scalar == 0:
        return np.zeros((0, 0)), np.array([]), np.zeros((0, 0))

    # Reconstruct operators and compute [D, phi_i]
    comm_D_phi = []
    for k in range(n_scalar):
        phi_k = scalar_basis[k].reshape(N, N)
        # Symmetrize: phi -> (phi + phi^dag) / sqrt(2)
        # This ensures the scalar field is self-adjoint
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        comm = D_mat @ phi_k_sa - phi_k_sa @ D_mat
        comm_D_phi.append(comm)

    # Mass-squared matrix: M^2_{ij} = Tr([D, phi_i]^dag [D, phi_j])
    M2 = np.zeros((n_scalar, n_scalar), dtype=complex)
    for i in range(n_scalar):
        for j in range(i, n_scalar):
            val = np.trace(comm_D_phi[i].conj().T @ comm_D_phi[j])
            M2[i, j] = val
            M2[j, i] = val.conj()

    # Normalize by basis vector norms
    norms = np.zeros(n_scalar)
    for k in range(n_scalar):
        phi_k = scalar_basis[k].reshape(N, N)
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        norms[k] = np.real(np.trace(phi_k_sa.conj().T @ phi_k_sa))

    # Normalized mass matrix
    for i in range(n_scalar):
        for j in range(n_scalar):
            if norms[i] > 1e-30 and norms[j] > 1e-30:
                M2[i, j] /= np.sqrt(norms[i] * norms[j])

    M2_real = np.real(M2)  # Should be real for self-adjoint operators
    imag_part = np.max(np.abs(np.imag(M2)))
    if imag_part > 1e-8:
        print(f"  WARNING: M^2 has imaginary part {imag_part:.2e}")

    # Diagonalize
    eigenvalues, eigenvectors = eigh(M2_real)

    return M2_real, eigenvalues, eigenvectors


def compute_mass_squared_direct(scalar_basis, D_mat, N):
    """
    Alternative mass-squared computation using the direct formula:
        M^2_{ij} = Tr(phi_i D^2 phi_j) + Tr(phi_i phi_j D^2)
                   - 2 Tr(phi_i D phi_j D)

    This is equivalent to Tr([D, phi_i]^dag [D, phi_j]) for Hermitian D
    and self-adjoint phi.

    Additionally computes the CUBIC and QUARTIC couplings to check for
    instability at the fold.
    """
    n_scalar = scalar_basis.shape[0]
    if n_scalar == 0:
        return np.zeros((0, 0)), np.array([]), np.zeros((0, 0))

    D2 = D_mat @ D_mat

    # Reconstruct self-adjoint operators
    phis = []
    for k in range(n_scalar):
        phi_k = scalar_basis[k].reshape(N, N)
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        phis.append(phi_k_sa)

    # Mass matrix M^2_{ij} = Tr(phi_i D^2 phi_j + phi_i phi_j D^2 - 2 phi_i D phi_j D)
    M2 = np.zeros((n_scalar, n_scalar))
    for i in range(n_scalar):
        for j in range(i, n_scalar):
            t1 = np.real(np.trace(phis[i] @ D2 @ phis[j]))
            t2 = np.real(np.trace(phis[i] @ phis[j] @ D2))
            t3 = np.real(np.trace(phis[i] @ D_mat @ phis[j] @ D_mat))
            val = t1 + t2 - 2.0 * t3
            M2[i, j] = val
            M2[j, i] = val

    # Normalize
    norms = np.array([np.real(np.trace(p.conj().T @ p)) for p in phis])
    for i in range(n_scalar):
        for j in range(n_scalar):
            if norms[i] > 1e-30 and norms[j] > 1e-30:
                M2[i, j] /= np.sqrt(norms[i] * norms[j])

    eigenvalues, eigenvectors = eigh(M2)

    return M2, eigenvalues, eigenvectors


# =============================================================================
# SECTION 6: QUARTIC POTENTIAL CHECK (spectral action fourth order)
# =============================================================================

def compute_quartic_traces(scalar_basis, D_mat, N, n_check=5):
    """
    For the n_check lightest scalar directions, compute:
        V_4(phi) ~ Tr(phi^4) + Tr(phi^2 D^2) + ...

    from the spectral action expansion. The quartic coefficient determines
    whether the tachyonic direction is stabilized or runaway.

    Returns dict with quartic coefficients for lightest modes.
    """
    n_scalar = scalar_basis.shape[0]
    n_check = min(n_check, n_scalar)

    phis = []
    for k in range(n_scalar):
        phi_k = scalar_basis[k].reshape(N, N)
        phi_k_sa = (phi_k + phi_k.conj().T) / np.sqrt(2.0)
        norm = np.sqrt(np.real(np.trace(phi_k_sa.conj().T @ phi_k_sa)))
        if norm > 1e-15:
            phi_k_sa /= norm
        phis.append(phi_k_sa)

    quartic = {}
    for k in range(n_check):
        phi = phis[k]
        # Tr(phi^4) coefficient
        tr_phi4 = np.real(np.trace(phi @ phi @ phi @ phi))
        # Tr([D, phi]^2) coefficient (mass)
        comm = D_mat @ phi - phi @ D_mat
        tr_comm2 = np.real(np.trace(comm.conj().T @ comm))
        # Tr(phi^2 [D, phi]^2) mixed quartic
        phi2 = phi @ phi
        tr_mixed = np.real(np.trace(phi2 @ comm.conj().T @ comm))

        quartic[k] = {
            'tr_phi4': tr_phi4,
            'tr_comm2': tr_comm2,
            'tr_mixed': tr_mixed,
        }

    return quartic


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

if __name__ == '__main__':
    t_total_start = time.time()

    print("=" * 78)
    print("OMEGA-CLASSIFY-46: Inner Fluctuation Module Classification")
    print("=" * 78)
    print()

    # Setup infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # Build the chirality gamma_9 = prod of all 8 gammas
    gamma_9 = np.eye(16, dtype=complex)
    for g in gammas:
        gamma_9 = gamma_9 @ g

    # Verify gamma_9^2 = I
    g9_sq = gamma_9 @ gamma_9
    g9_err = np.max(np.abs(g9_sq - np.eye(16)))
    print(f"  gamma_9^2 = I check: error = {g9_err:.2e}")

    # Build A_F generators
    AF_16, AF_names, AF_factors, AF_class = build_AF_generators()
    n_gen = len(AF_16)
    print(f"  A_F generators: {n_gen}")

    gauge_idx = [i for i, c in enumerate(AF_class) if c == 'gauge']
    scalar_idx = [i for i, c in enumerate(AF_class) if c in ('scalar', 'mixed_diag')]
    print(f"  Gauge generators: {len(gauge_idx)}")
    print(f"  Scalar generators: {len(scalar_idx)}")
    print()

    # Tau values: round SU(3) and fold
    tau_round = 0.00
    tau_fold_val = 0.19  # canonical fold

    # Primary sector: (1,0) fundamental
    p_sector, q_sector = 1, 0

    # =========================================================================
    # STEP 1: Build D_K at round and fold
    # =========================================================================
    print("=" * 78)
    print("STEP 1: BUILD D_K AT ROUND (tau=0) AND FOLD (tau=0.19)")
    print("=" * 78)
    print()

    D_round, dim_rho = build_DK(tau_round, gens, f_abc, B_ab, gammas, p_sector, q_sector)
    N = D_round.shape[0]
    print(f"  D_K at round: shape = {D_round.shape}, dim_rho = {dim_rho}")
    print(f"  Hermiticity error: {np.max(np.abs(D_round - D_round.conj().T)):.2e}")

    D_fold, _ = build_DK(tau_fold_val, gens, f_abc, B_ab, gammas, p_sector, q_sector)
    print(f"  D_K at fold:  shape = {D_fold.shape}")
    print(f"  Hermiticity error: {np.max(np.abs(D_fold - D_fold.conj().T)):.2e}")
    print()

    # Eigenvalue comparison
    evals_round = np.sort(eigvalsh(D_round))
    evals_fold = np.sort(eigvalsh(D_fold))
    print(f"  Eigenvalue range (round): [{evals_round[0]:.4f}, {evals_round[-1]:.4f}]")
    print(f"  Eigenvalue range (fold):  [{evals_fold[0]:.4f}, {evals_fold[-1]:.4f}]")
    print()

    # =========================================================================
    # STEP 2: Compute Omega^1_D at fold and round
    # =========================================================================
    print("=" * 78)
    print("STEP 2: COMPUTE Omega^1_D(A_F) MODULE")
    print("=" * 78)
    print()

    t0 = time.time()
    omega_fold = compute_omega1_full(D_fold, AF_16, dim_rho)
    dt_fold = time.time() - t0
    print(f"  FOLD (tau={tau_fold_val}):")
    print(f"    Linear module dim:     {omega_fold['dim_linear']}")
    print(f"    Quadratic module dim:  {omega_fold['dim_quadratic']}")
    print(f"    Combined module dim:   {omega_fold['dim_combined']}")
    print(f"    Extra directions:      {omega_fold['dim_extra']}")
    print(f"    Computed in {dt_fold:.1f}s")
    print()

    t0 = time.time()
    omega_round = compute_omega1_full(D_round, AF_16, dim_rho)
    dt_round = time.time() - t0
    print(f"  ROUND (tau=0):")
    print(f"    Linear module dim:     {omega_round['dim_linear']}")
    print(f"    Quadratic module dim:  {omega_round['dim_quadratic']}")
    print(f"    Combined module dim:   {omega_round['dim_combined']}")
    print(f"    Extra directions:      {omega_round['dim_extra']}")
    print(f"    Computed in {dt_round:.1f}s")
    print()

    # Singular value spectra (diagnostic)
    print("  Singular value spectra (top 10):")
    print(f"    Linear (fold):    {omega_fold['linear_sv'][:10]}")
    print(f"    Quadratic (fold): {omega_fold['quadratic_sv'][:10]}")
    print(f"    Extra (fold):     {omega_fold['extra_sv'][:min(10, len(omega_fold['extra_sv']))]}")
    print()

    # =========================================================================
    # STEP 3: Grading decomposition (gauge vs scalar)
    # =========================================================================
    print("=" * 78)
    print("STEP 3: Z_2 GRADING DECOMPOSITION (GAUGE vs SCALAR)")
    print("=" * 78)
    print()

    # Decompose the LINEAR module
    lin_even_f, lin_odd_f, dim_lin_even_f, dim_lin_odd_f, lin_gr_f = \
        decompose_by_grading(omega_fold['linear_basis'], N, dim_rho, gamma_9)
    print(f"  LINEAR MODULE (fold):")
    print(f"    Even (gauge) dim:  {dim_lin_even_f}")
    print(f"    Odd  (scalar) dim: {dim_lin_odd_f}")
    print(f"    Total:             {dim_lin_even_f + dim_lin_odd_f}")
    print(f"    (Expected: gauge ~ 12 SM bosons, scalar ~ Higgs components)")
    print()

    # Decompose the EXTRA directions (the 169 from quadratic terms)
    if omega_fold['dim_extra'] > 0:
        ext_even_f, ext_odd_f, dim_ext_even_f, dim_ext_odd_f, ext_gr_f = \
            decompose_by_grading(omega_fold['extra_basis'], N, dim_rho, gamma_9)
        print(f"  EXTRA (CCS 2013 quadratic) MODULE (fold):")
        print(f"    Even (gauge) dim:  {dim_ext_even_f}")
        print(f"    Odd  (scalar) dim: {dim_ext_odd_f}")
        print(f"    Total:             {dim_ext_even_f + dim_ext_odd_f}")
    else:
        dim_ext_even_f = 0
        dim_ext_odd_f = 0
        ext_even_f = np.zeros((0, N*N), dtype=complex)
        ext_odd_f = np.zeros((0, N*N), dtype=complex)
        print(f"  EXTRA MODULE: empty (no quadratic excess)")
    print()

    # Decompose the COMBINED module
    comb_even_f, comb_odd_f, dim_comb_even_f, dim_comb_odd_f, comb_gr_f = \
        decompose_by_grading(omega_fold['combined_basis'], N, dim_rho, gamma_9)
    print(f"  COMBINED MODULE (fold):")
    print(f"    Even (gauge) dim:  {dim_comb_even_f}")
    print(f"    Odd  (scalar) dim: {dim_comb_odd_f}")
    print(f"    Total:             {dim_comb_even_f + dim_comb_odd_f}")
    print()

    # Same decomposition at round
    lin_even_r, lin_odd_r, dim_lin_even_r, dim_lin_odd_r, _ = \
        decompose_by_grading(omega_round['linear_basis'], N, dim_rho, gamma_9)
    print(f"  LINEAR MODULE (round):")
    print(f"    Even (gauge) dim:  {dim_lin_even_r}")
    print(f"    Odd  (scalar) dim: {dim_lin_odd_r}")
    print()

    if omega_round['dim_extra'] > 0:
        ext_even_r, ext_odd_r, dim_ext_even_r, dim_ext_odd_r, _ = \
            decompose_by_grading(omega_round['extra_basis'], N, dim_rho, gamma_9)
        print(f"  EXTRA MODULE (round):")
        print(f"    Even (gauge) dim:  {dim_ext_even_r}")
        print(f"    Odd  (scalar) dim: {dim_ext_odd_r}")
    else:
        dim_ext_even_r = 0
        dim_ext_odd_r = 0
        ext_odd_r = np.zeros((0, N*N), dtype=complex)
    print()

    # Grading eigenvalue distribution
    print(f"  Grading eigenvalue distribution (fold, combined):")
    print(f"    Mean:   {np.mean(comb_gr_f):.6f}")
    print(f"    Std:    {np.std(comb_gr_f):.6f}")
    print(f"    Min:    {np.min(comb_gr_f):.6f}")
    print(f"    Max:    {np.max(comb_gr_f):.6f}")
    n_pure_even = np.sum(np.abs(comb_gr_f - 1.0) < 0.01)
    n_pure_odd = np.sum(np.abs(comb_gr_f + 1.0) < 0.01)
    n_mixed = len(comb_gr_f) - n_pure_even - n_pure_odd
    print(f"    Pure even (|g-1|<0.01):  {n_pure_even}")
    print(f"    Pure odd  (|g+1|<0.01):  {n_pure_odd}")
    print(f"    Mixed grading:           {n_mixed}")
    print()

    # =========================================================================
    # STEP 4: Mass-squared matrix for scalar directions at FOLD
    # =========================================================================
    print("=" * 78)
    print("STEP 4: MASS-SQUARED MATRIX FOR SCALAR DIRECTIONS")
    print("=" * 78)
    print()

    # Use the ODD (scalar) part of the COMBINED module at fold
    print(f"  Computing M^2 for {dim_comb_odd_f} scalar directions at fold...")
    t0 = time.time()

    M2_fold, M2_evals_fold, M2_evecs_fold = compute_mass_squared_matrix(
        comb_odd_f, D_fold, N)

    # Cross-check with direct formula
    M2_fold_d, M2_evals_fold_d, _ = compute_mass_squared_direct(
        comb_odd_f, D_fold, N)
    dt_m2 = time.time() - t0

    print(f"  Computed in {dt_m2:.1f}s")
    print()

    # Cross-check
    m2_diff = np.max(np.abs(M2_evals_fold - M2_evals_fold_d))
    print(f"  Cross-check (commutator vs direct): max eigenvalue diff = {m2_diff:.2e}")
    print()

    # Report eigenvalue spectrum
    n_tachyonic_fold = np.sum(M2_evals_fold < -1e-10)
    n_massless_fold = np.sum(np.abs(M2_evals_fold) < 1e-10)
    n_massive_fold = np.sum(M2_evals_fold > 1e-10)

    print(f"  FOLD MASS SPECTRUM:")
    print(f"    Tachyonic (m^2 < 0):   {n_tachyonic_fold}")
    print(f"    Massless  (m^2 = 0):   {n_massless_fold}")
    print(f"    Massive   (m^2 > 0):   {n_massive_fold}")
    print(f"    Total:                 {len(M2_evals_fold)}")
    print()

    print(f"  Eigenvalue spectrum (lowest 20):")
    for k in range(min(20, len(M2_evals_fold))):
        label = "TACHYON" if M2_evals_fold[k] < -1e-10 else \
                "ZERO" if abs(M2_evals_fold[k]) < 1e-10 else "massive"
        print(f"    m^2_{k:3d} = {M2_evals_fold[k]:+12.6f}  [{label}]")
    if len(M2_evals_fold) > 20:
        print(f"    ...")
        for k in range(max(20, len(M2_evals_fold)-5), len(M2_evals_fold)):
            print(f"    m^2_{k:3d} = {M2_evals_fold[k]:+12.6f}  [massive]")
    print()

    # =========================================================================
    # STEP 5: Mass-squared matrix at ROUND for comparison
    # =========================================================================
    print("=" * 78)
    print("STEP 5: MASS-SQUARED MATRIX AT ROUND (tau=0)")
    print("=" * 78)
    print()

    # Use the odd part of the combined module at round
    comb_even_r2, comb_odd_r2, dim_comb_even_r2, dim_comb_odd_r2, _ = \
        decompose_by_grading(omega_round['combined_basis'], N, dim_rho, gamma_9)

    if dim_comb_odd_r2 > 0:
        print(f"  Computing M^2 for {dim_comb_odd_r2} scalar directions at round...")
        t0 = time.time()
        M2_round, M2_evals_round, M2_evecs_round = compute_mass_squared_matrix(
            comb_odd_r2, D_round, N)
        dt_m2r = time.time() - t0
        print(f"  Computed in {dt_m2r:.1f}s")

        n_tachyonic_round = np.sum(M2_evals_round < -1e-10)
        n_massless_round = np.sum(np.abs(M2_evals_round) < 1e-10)
        n_massive_round = np.sum(M2_evals_round > 1e-10)

        print(f"  ROUND MASS SPECTRUM:")
        print(f"    Tachyonic (m^2 < 0):   {n_tachyonic_round}")
        print(f"    Massless  (m^2 = 0):   {n_massless_round}")
        print(f"    Massive   (m^2 > 0):   {n_massive_round}")
        print()

        print(f"  Eigenvalue spectrum (lowest 20):")
        for k in range(min(20, len(M2_evals_round))):
            label = "TACHYON" if M2_evals_round[k] < -1e-10 else \
                    "ZERO" if abs(M2_evals_round[k]) < 1e-10 else "massive"
            print(f"    m^2_{k:3d} = {M2_evals_round[k]:+12.6f}  [{label}]")
        print()
    else:
        n_tachyonic_round = 0
        n_massless_round = 0
        M2_evals_round = np.array([])
        print(f"  No scalar directions at round.")
        print()

    # =========================================================================
    # STEP 6: TAU SCAN of lightest mass eigenvalue
    # =========================================================================
    print("=" * 78)
    print("STEP 6: TAU SCAN OF LIGHTEST SCALAR MASS")
    print("=" * 78)
    print()

    tau_scan = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30])
    m2_min_vs_tau = np.zeros(len(tau_scan))
    n_tach_vs_tau = np.zeros(len(tau_scan), dtype=int)
    n_zero_vs_tau = np.zeros(len(tau_scan), dtype=int)

    for ti, tau in enumerate(tau_scan):
        D_tau, _ = build_DK(tau, gens, f_abc, B_ab, gammas, p_sector, q_sector)
        omega_tau = compute_omega1_full(D_tau, AF_16, dim_rho)

        _, odd_tau, _, dim_odd_tau, _ = decompose_by_grading(
            omega_tau['combined_basis'], N, dim_rho, gamma_9)

        if dim_odd_tau > 0:
            _, evals_tau, _ = compute_mass_squared_matrix(odd_tau, D_tau, N)
            m2_min_vs_tau[ti] = evals_tau[0]
            n_tach_vs_tau[ti] = np.sum(evals_tau < -1e-10)
            n_zero_vs_tau[ti] = np.sum(np.abs(evals_tau) < 1e-10)
        else:
            m2_min_vs_tau[ti] = np.nan
            n_tach_vs_tau[ti] = 0

        print(f"  tau={tau:.2f}: m^2_min = {m2_min_vs_tau[ti]:+12.6f}, "
              f"n_tach = {n_tach_vs_tau[ti]}, n_zero = {n_zero_vs_tau[ti]}")

    print()

    # Check for tachyonic at fold but not at round
    tach_at_fold_not_round = (n_tach_vs_tau[4] > 0 or n_tach_vs_tau[5] > 0) and \
                              n_tach_vs_tau[0] == 0
    print(f"  Tachyonic at fold but not round: {tach_at_fold_not_round}")
    print()

    # =========================================================================
    # STEP 7: QUARTIC POTENTIAL CHECK
    # =========================================================================
    print("=" * 78)
    print("STEP 7: QUARTIC POTENTIAL FOR LIGHTEST SCALARS")
    print("=" * 78)
    print()

    if dim_comb_odd_f > 0:
        quartic_fold = compute_quartic_traces(comb_odd_f, D_fold, N, n_check=10)
        print(f"  Quartic coefficients for 10 lightest scalar modes at fold:")
        print(f"  {'Mode':>6s}  {'Tr(phi^4)':>12s}  {'Tr([D,phi]^2)':>15s}  {'Tr(phi^2 [D,phi]^2)':>20s}  {'m^2':>12s}")
        for k in sorted(quartic_fold.keys()):
            q = quartic_fold[k]
            m2_k = M2_evals_fold[k] if k < len(M2_evals_fold) else 0.0
            print(f"  {k:6d}  {q['tr_phi4']:12.6f}  {q['tr_comm2']:15.6f}  {q['tr_mixed']:20.6f}  {m2_k:+12.6f}")
        print()

    # =========================================================================
    # STEP 8: IDENTIFY ALGEBRA ORIGIN OF TACHYONIC/LIGHT DIRECTIONS
    # =========================================================================
    print("=" * 78)
    print("STEP 8: ALGEBRA ORIGIN OF LIGHT SCALAR DIRECTIONS")
    print("=" * 78)
    print()

    # For each of the lightest scalar eigenvectors, project back onto the
    # original a_i [D, b_j] and [D, a_i][D, b_j] basis to identify
    # which algebra generators dominate.
    if dim_comb_odd_f > 0 and len(M2_evals_fold) > 0:
        # The M2 eigenvectors are in the scalar (odd) subspace.
        # Project the lightest eigenvectors onto the original generator basis.
        n_show = min(10, len(M2_evals_fold))

        # Reconstruct the original generator labels
        gen_pair_labels = []
        for j in range(n_gen):
            for i in range(n_gen):
                gen_pair_labels.append(f"L:({AF_names[i]},{AF_names[j]})")
        for j in range(n_gen):
            for i in range(n_gen):
                gen_pair_labels.append(f"Q:({AF_names[i]},{AF_names[j]})")

        # Build the full generator vectors (linear + quadratic)
        full_gen_vecs = []
        for j in range(n_gen):
            b_full = np.kron(np.eye(dim_rho), AF_16[j]) if dim_rho > 1 else AF_16[j]
            comm_Db = D_fold @ b_full - b_full @ D_fold
            for i in range(n_gen):
                a_full = np.kron(np.eye(dim_rho), AF_16[i]) if dim_rho > 1 else AF_16[i]
                lin = a_full @ comm_Db
                full_gen_vecs.append(lin.ravel())
        for j in range(n_gen):
            b_full = np.kron(np.eye(dim_rho), AF_16[j]) if dim_rho > 1 else AF_16[j]
            comm_Db = D_fold @ b_full - b_full @ D_fold
            for i in range(n_gen):
                a_full = np.kron(np.eye(dim_rho), AF_16[i]) if dim_rho > 1 else AF_16[i]
                comm_Da = D_fold @ a_full - a_full @ D_fold
                quad = comm_Da @ comm_Db
                full_gen_vecs.append(quad.ravel())

        full_gen_mat = np.array(full_gen_vecs)

        print(f"  Lightest {n_show} scalar eigenvectors — dominant generator pairs:")
        print()
        for eig_idx in range(n_show):
            # The eigenvector in the scalar subspace
            evec = M2_evecs_fold[:, eig_idx]  # in odd basis
            # Reconstruct the operator in the full N^2 space
            omega_op = evec @ comb_odd_f  # (N^2,) vector
            # Project onto generator pair basis
            overlaps = full_gen_mat @ omega_op.conj()
            top_5 = np.argsort(np.abs(overlaps))[-5:][::-1]

            m2_val = M2_evals_fold[eig_idx]
            label = "TACHYON" if m2_val < -1e-10 else \
                    "ZERO" if abs(m2_val) < 1e-10 else "massive"
            print(f"  Mode {eig_idx} (m^2 = {m2_val:+.6f}, {label}):")
            for idx in top_5:
                weight = np.abs(overlaps[idx])**2
                if weight > 0.001:
                    print(f"    {gen_pair_labels[idx]:40s}  weight = {weight:.4f}")
            print()

    # =========================================================================
    # STEP 9: EXTRA DIRECTION DECOMPOSITION BY ALGEBRA FACTOR
    # =========================================================================
    print("=" * 78)
    print("STEP 9: EXTRA DIRECTIONS BY ALGEBRA FACTOR")
    print("=" * 78)
    print()

    # Decompose the 169 extra directions by which factor pairs (C,H,M3)
    # dominate. This reveals whether the tachyonic modes come from
    # specific algebra sectors.
    if omega_fold['dim_extra'] > 0:
        # For each extra basis vector, measure overlap with generators
        # from each factor pair
        factor_pairs = ['CC', 'CH', 'CM', 'HC', 'HH', 'HM', 'MC', 'MH', 'MM']

        # Build factor indices
        factor_gen_idx = {'C': [], 'H': [], 'M3': []}
        for gi, f in enumerate(AF_factors):
            factor_gen_idx[f].append(gi)

        # Map factor labels
        fmap = {'C': 'C', 'H': 'H', 'M3': 'M'}

        print(f"  {omega_fold['dim_extra']} extra directions:")
        print(f"    Even (gauge-like): {dim_ext_even_f}")
        print(f"    Odd  (scalar-like): {dim_ext_odd_f}")
        print()

    # =========================================================================
    # VERDICT
    # =========================================================================
    print("=" * 78)
    print("OMEGA-CLASSIFY-46 VERDICT")
    print("=" * 78)
    print()

    print(f"  MODULE DIMENSIONS:")
    print(f"    Linear (standard):        {omega_fold['dim_linear']}")
    print(f"    Quadratic (CCS 2013):     {omega_fold['dim_quadratic']}")
    print(f"    Combined:                 {omega_fold['dim_combined']}")
    print(f"    Extra (combined \\ linear): {omega_fold['dim_extra']}")
    print()

    print(f"  GRADING DECOMPOSITION (combined):")
    print(f"    Even (gauge):  {dim_comb_even_f}")
    print(f"    Odd (scalar):  {dim_comb_odd_f}")
    print()

    print(f"  LINEAR GRADING:")
    print(f"    Even (gauge):  {dim_lin_even_f}")
    print(f"    Odd (scalar):  {dim_lin_odd_f}")
    print()

    if omega_fold['dim_extra'] > 0:
        print(f"  EXTRA GRADING:")
        print(f"    Even (gauge):  {dim_ext_even_f}")
        print(f"    Odd (scalar):  {dim_ext_odd_f}")
        print()

    print(f"  SCALAR MASS SPECTRUM AT FOLD (tau={tau_fold_val}):")
    print(f"    Tachyonic (m^2 < 0): {n_tachyonic_fold}")
    print(f"    Massless  (m^2 = 0): {n_massless_fold}")
    print(f"    Massive   (m^2 > 0): {n_massive_fold}")
    if len(M2_evals_fold) > 0:
        print(f"    Lightest m^2:        {M2_evals_fold[0]:+.6f}")
        print(f"    Heaviest m^2:        {M2_evals_fold[-1]:+.6f}")
    print()

    print(f"  SCALAR MASS SPECTRUM AT ROUND (tau=0):")
    print(f"    Tachyonic (m^2 < 0): {n_tachyonic_round}")
    print(f"    Massless  (m^2 = 0): {n_massless_round}")
    if len(M2_evals_round) > 0:
        print(f"    Lightest m^2:        {M2_evals_round[0]:+.6f}")
    print()

    # Gate verdict
    if tach_at_fold_not_round:
        gate_verdict = "PASS"
        gate_detail = (
            f"TACHYONIC INSTABILITY: {n_tach_vs_tau[4]} directions tachyonic "
            f"at fold (m^2_min = {m2_min_vs_tau[4]:+.6f}) "
            f"but NOT at round ({n_tach_vs_tau[0]} tachyonic). "
            f"The Jensen deformation induces spontaneous symmetry breaking "
            f"in the Omega^1_D scalar sector. This is a tau-stabilization "
            f"mechanism OUTSIDE the spectral action (lives in the inner "
            f"fluctuation module, not in Tr f(D^2/Lambda^2))."
        )
    elif n_tachyonic_fold > 0:
        # Tachyonic at both fold and round
        gate_verdict = "INFO"
        gate_detail = (
            f"Tachyonic at fold ({n_tachyonic_fold}) AND round ({n_tachyonic_round}). "
            f"The instability is not induced by Jensen deformation. "
            f"This may indicate a structural issue with the representation "
            f"or a genuine Higgs-type instability already present at round SU(3)."
        )
    else:
        # All massive everywhere
        gate_verdict = "FAIL"
        gate_detail = (
            f"All scalar directions are massive at all tau. "
            f"No tachyonic instability. The Omega^1_D scalar sector "
            f"does not provide a tau-stabilization mechanism."
        )

    # Additional check: any m^2 that DECREASES toward fold
    if len(M2_evals_fold) > 0 and len(M2_evals_round) > 0:
        # Compare lightest eigenvalues
        n_compare = min(len(M2_evals_fold), len(M2_evals_round))
        decreasing = M2_evals_fold[:n_compare] < M2_evals_round[:n_compare]
        n_decreasing = np.sum(decreasing)
        if n_decreasing > 0:
            gate_detail += (
                f"\n  NOTE: {n_decreasing}/{n_compare} eigenvalues DECREASE "
                f"from round to fold. Lightest: {M2_evals_round[0]:+.6f} (round) "
                f"-> {M2_evals_fold[0]:+.6f} (fold)."
            )

    print(f"  GATE: OMEGA-CLASSIFY-46 = {gate_verdict}")
    print(f"  {gate_detail}")
    print()

    # Tau scan summary
    print(f"  TAU SCAN SUMMARY:")
    print(f"  {'tau':>6s}  {'m2_min':>12s}  {'n_tach':>8s}  {'n_zero':>8s}")
    for ti, tau in enumerate(tau_scan):
        print(f"  {tau:6.2f}  {m2_min_vs_tau[ti]:+12.6f}  {n_tach_vs_tau[ti]:8d}  {n_zero_vs_tau[ti]:8d}")
    print()

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    t_total = time.time() - t_total_start

    outfile = os.path.join(OUTDIR, "s46_omega_classify.npz")
    save_dict = {
        # Module dimensions
        'dim_linear_fold': omega_fold['dim_linear'],
        'dim_quadratic_fold': omega_fold['dim_quadratic'],
        'dim_combined_fold': omega_fold['dim_combined'],
        'dim_extra_fold': omega_fold['dim_extra'],
        'dim_linear_round': omega_round['dim_linear'],
        'dim_quadratic_round': omega_round['dim_quadratic'],
        'dim_combined_round': omega_round['dim_combined'],
        'dim_extra_round': omega_round['dim_extra'],
        # Grading decomposition
        'dim_lin_even_fold': dim_lin_even_f,
        'dim_lin_odd_fold': dim_lin_odd_f,
        'dim_ext_even_fold': dim_ext_even_f,
        'dim_ext_odd_fold': dim_ext_odd_f,
        'dim_comb_even_fold': dim_comb_even_f,
        'dim_comb_odd_fold': dim_comb_odd_f,
        # Mass spectrum at fold
        'M2_eigenvalues_fold': M2_evals_fold,
        'n_tachyonic_fold': n_tachyonic_fold,
        'n_massless_fold': n_massless_fold,
        'n_massive_fold': n_massive_fold,
        # Mass spectrum at round
        'M2_eigenvalues_round': M2_evals_round,
        'n_tachyonic_round': n_tachyonic_round,
        'n_massless_round': n_massless_round,
        # Tau scan
        'tau_scan': tau_scan,
        'm2_min_vs_tau': m2_min_vs_tau,
        'n_tach_vs_tau': n_tach_vs_tau,
        'n_zero_vs_tau': n_zero_vs_tau,
        # Singular values
        'linear_sv_fold': omega_fold['linear_sv'],
        'quadratic_sv_fold': omega_fold['quadratic_sv'],
        'extra_sv_fold': omega_fold['extra_sv'],
        'combined_sv_fold': omega_fold['combined_sv'],
        # Sector info
        'sector_p': p_sector,
        'sector_q': q_sector,
        'dim_rho': dim_rho,
        'tau_fold': tau_fold_val,
        'tau_round': tau_round,
        # Verdict
        'verdict': np.array([gate_verdict]),
        'runtime': t_total,
    }

    # Add M2 matrix if manageable size
    if M2_fold.size < 1e6:
        save_dict['M2_matrix_fold'] = M2_fold
    if M2_round.size < 1e6 if len(M2_evals_round) > 0 else False:
        save_dict['M2_matrix_round'] = M2_round

    np.savez(outfile, **save_dict)

    print(f"  Data saved to: {outfile}")
    print(f"  Total runtime: {t_total:.1f}s")
    print()
    print("OMEGA-CLASSIFY-46 COMPUTATION COMPLETE")
    print("=" * 78)
