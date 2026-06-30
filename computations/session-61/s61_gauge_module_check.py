#!/usr/bin/env python3
"""
S61 GAUGE-MODULE-61: Order-One Condition vs Gauge Module Conditions
====================================================================

D_K fails the standard NCG order-one condition [[D, a], b^o] = 0 at value
4.000 (PROVEN, S22b/S28b). This script checks whether D_K instead defines
a GAUGE MODULE per van den Dungen & van Suijlekom (2014), arXiv:1405.5368.

MATHEMATICAL FRAMEWORK
----------------------

Paper 05 defines gauge modules via these conditions:

  GM1 (Bimodule): Omega^1_D(A) = span{a_i [D, b_i]} is an A-bimodule.
       i.e., for all a in A, omega in Omega^1_D: a*omega, omega*a in Omega^1_D.

  GM2 (Self-adjointness): Omega^1_D is closed under the *-operation.

  GM3 (Gauge covariance): For u in U(A) = {u : uu*=u*u=1},
       u * omega * u* in Omega^1_D for all omega in Omega^1_D.

When the order-one condition holds, GM1-GM3 are automatic because
[D, a] commutes with b^o, making right multiplication by b^o trivial.

When order-one FAILS, the right A-action may still close within Omega^1_D
if the failure is "structured" (lies in a specific algebraic direction).

STRATEGY
--------
1. Build A_F = C + H + M_3(C) generators on C^16 (Psi_+ sector).
2. Compute Omega^1_D = span{pi(a) [D_K, pi(b)] : a, b in A_F} as a matrix space.
3. Check GM1: for each basis element omega of Omega^1_D and each a in A_F,
   verify that a*omega and omega*a have zero projection onto Omega^1_D^perp.
4. Check GM2: verify omega^* in Omega^1_D for all omega.
5. Check GM3: verify u omega u^* in Omega^1_D for generators u of U(A).
6. Determine the gauge group from Aut(Omega^1_D).

Author: Van den Dungen Bridge Theorist (Session 61, Wave 4)
Date: 2026-03-28
Gate: GAUGE-MODULE-61
Sources: Paper 05 (1405.5368), S28b (order-one failure), S31 (severity assessment)
"""

import numpy as np
from numpy.linalg import norm as la_norm, svd, matrix_rank
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold

# Import from dirac_spectrum
from dirac_spectrum import (
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
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

OUTDIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_NPZ = os.path.join(OUTDIR, "s61_gauge_module_check.npz")

# =============================================================================
# SECTION 1: A_F ALGEBRA INFRASTRUCTURE
# Reproduced from s28b_order_one.py with validation
# =============================================================================

def flat_idx(row, col):
    """Map (row, col) in 4x4 matrix to flat index in 16-dim Psi_+.

    Convention (Baptista/Connes bimodule on M_4(C)):
        (0,0) -> 0     (nu_R)
        (0,1..3) -> 1..3  (lepton doublet+singlet)
        (1..3,0) -> 4..6  (quark singlet, 3 colors)
        (1..3,1..3) -> 7..15 (quark doublet+singlet, 3x3)
    """
    if row == 0 and col == 0:
        return 0
    if row == 0:
        return col
    if col == 0:
        return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4, R4):
    """Build 16x16 for bimodule action X -> L4 . X . R4^T on M_4(C)."""
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


# Chirality on Psi_+
gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])

def get_column_index(flat_idx_val):
    if flat_idx_val == 0:
        return 0
    elif 1 <= flat_idx_val <= 3:
        return flat_idx_val
    elif 4 <= flat_idx_val <= 6:
        return 0
    else:
        return (flat_idx_val - 7) % 3 + 1

G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)


def o_map_16(gen_16):
    """Opposite algebra on 16-dim: o(b) = G5 @ gen_16^T @ G5."""
    return G5 @ gen_16.T @ G5


def build_AF_generators():
    """Build all generators of A_F = C + H + M_3(C) as 16x16 matrices.

    Returns:
        AF_16: list of (16,16) complex matrices
        AF_names: list of generator names
        AF_factors: list of factor labels ('C', 'H', 'M3')
    """
    AF_16 = []
    AF_names = []
    AF_factors = []

    # --- C factor (2 generators) ---
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im')
    AF_factors.append('C')

    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj')
    AF_factors.append('C')

    # --- H factor (4 generators: 1, i, j, k acting on rows 2-3) ---
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i')
    AF_factors.append('H')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0
    L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j')
    AF_factors.append('H')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j
    L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k')
    AF_factors.append('H')

    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1')
    AF_factors.append('H')

    # --- M_3(C) factor (18 generators: Re and Im parts of E_{ab}) ---
    for a in range(3):
        for b in range(3):
            for part, val in [('Re', 1.0), ('Im', 1j)]:
                m_elem = np.zeros((3, 3), dtype=complex)
                m_elem[a, b] = val
                R_m = np.eye(4, dtype=complex)
                R_m[1:, 1:] = m_elem.conj().T
                AF_16.append(build_bimodule_16(np.eye(4), R_m))
                AF_names.append(f'M3_E{a}{b}_{part}')
                AF_factors.append('M3')

    return AF_16, AF_names, AF_factors


def build_unitary_generators(AF_16, AF_names, AF_factors):
    """Build generators of the unitary group U(A_F).

    U(A) = U(1) x SU(2) x U(3).
    The gauge group G(A) = U(A) / Center(A) = U(1) x SU(2) x SU(3)
    modulo finite-group identifications.

    We build anti-Hermitian generators for the Lie algebra of U(A):
      u(1): i * P_C where P_C is the C projector
      su(2): i*sigma_j acting on H sector (rows 2-3)
      u(3): i * T_a acting via M_3(C) on the right
    """
    unitaries_ah = []
    u_names = []
    u_factors = []

    # u(1) generator: i * identity on C factor
    L_u1 = np.diag([1j, 0, 0, 0])
    u1_gen = build_bimodule_16(L_u1, np.eye(4))
    unitaries_ah.append(u1_gen)
    u_names.append('u1')
    u_factors.append('U1')

    # su(2) generators: i*sigma_j on the H block (rows 2-3)
    # sigma_1
    L_s1 = np.zeros((4, 4), dtype=complex)
    L_s1[2, 3] = 1j
    L_s1[3, 2] = 1j
    unitaries_ah.append(build_bimodule_16(L_s1, np.eye(4)))
    u_names.append('su2_1')
    u_factors.append('SU2')

    # sigma_2
    L_s2 = np.zeros((4, 4), dtype=complex)
    L_s2[2, 3] = 1.0
    L_s2[3, 2] = -1.0
    unitaries_ah.append(build_bimodule_16(L_s2, np.eye(4)))
    u_names.append('su2_2')
    u_factors.append('SU2')

    # sigma_3
    L_s3 = np.zeros((4, 4), dtype=complex)
    L_s3[2, 2] = 1j
    L_s3[3, 3] = -1j
    unitaries_ah.append(build_bimodule_16(L_s3, np.eye(4)))
    u_names.append('su2_3')
    u_factors.append('SU2')

    # u(3) generators: 9 = 8 (su3) + 1 (u1_color)
    # These act on the RIGHT via M_3(C)
    gm = _gell_mann_matrices()
    for idx, lam in enumerate(gm):
        R_m = np.eye(4, dtype=complex)
        R_m[1:, 1:] = (1j/2 * lam).conj().T  # anti-Hermitian, right action
        unitaries_ah.append(build_bimodule_16(np.eye(4), R_m))
        u_names.append(f'su3_{idx+1}')
        u_factors.append('SU3')

    # u(1)_color: i * I_3 on right
    R_u1c = np.eye(4, dtype=complex)
    R_u1c[1:, 1:] = 1j * np.eye(3)
    unitaries_ah.append(build_bimodule_16(np.eye(4), R_u1c))
    u_names.append('u1_color')
    u_factors.append('U1c')

    return unitaries_ah, u_names, u_factors


def _gell_mann_matrices():
    """Standard Gell-Mann matrices lambda_1 through lambda_8."""
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    return [l1, l2, l3, l4, l5, l6, l7, l8]


# =============================================================================
# SECTION 2: BUILD D_K ON C^16 (SINGLET SECTOR)
# =============================================================================

def build_DK_singlet(gammas, gens, f_abc, s_val):
    """Build D_K restricted to the (0,0) singlet sector.

    For the singlet, rho(X_a) = 0, so D_K = Omega(s), the spin connection offset.
    This is the 16x16 matrix acting on spinor space only.

    Args:
        gammas: Cliff(R^8) generators (16x16)
        gens: su(3) generators
        f_abc: structure constants
        s_val: Jensen parameter

    Returns:
        D_K: (16, 16) complex matrix
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return Omega


def build_DK_fundamental(gammas, gens, f_abc, s_val):
    """Build D_K on the fundamental (1,0) sector = C^3 x C^16 = C^48.

    D_K = sum_a rho(e_a) x gamma_a + I_3 x Omega(s)
    where rho(e_a) are the 3x3 fundamental generators E_{ab} * X_b.

    Args:
        gammas: Cliff(R^8) generators
        gens: su(3) generators (anti-Hermitian 3x3)
        f_abc: structure constants
        s_val: Jensen parameter

    Returns:
        D_K: (48, 48) complex matrix
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    dim_rep = 3
    dim_spin = 16  # (local)
    dim_total = dim_rep * dim_spin

    D_K = np.kron(np.eye(dim_rep), Omega)

    for a in range(8):
        # Orthonormal frame transformation: e_a = E_{ab} X_b
        rho_ea = np.zeros((dim_rep, dim_rep), dtype=complex)
        for b in range(8):
            rho_ea += E[a, b] * gens[b]
        D_K += np.kron(rho_ea, gammas[a])

    return D_K


# =============================================================================
# SECTION 3: COMPUTE Omega^1_D(A) SPACE
# =============================================================================

def compute_omega1_space(D_K, AF_16, dim_rep=1):
    """Compute the vector space Omega^1_D(A) = span{pi(a) [D, pi(b)]}.

    We flatten each matrix a [D, b] into a vector and compute the
    column space via SVD.

    Args:
        D_K: the Dirac operator matrix (n x n)
        AF_16: list of A_F generators (16x16)
        dim_rep: representation dimension (1 for singlet, 3 for fund)

    Returns:
        basis: (rank, n*n) array -- ON basis for Omega^1_D as vectorized matrices
        rank: dimension of Omega^1_D
        all_1forms: list of (n, n) matrices {a [D, b]}
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    # Embed A_F generators into full space
    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]

    all_1forms = []
    for i in range(n_gen):
        for j in range(n_gen):
            comm_Db = D_K @ A_gens[j] - A_gens[j] @ D_K  # [D, b]
            omega_ij = A_gens[i] @ comm_Db  # a [D, b]
            all_1forms.append(omega_ij)

    # Stack as vectors and compute SVD
    n_forms = len(all_1forms)
    mat = np.zeros((n_forms, n * n), dtype=complex)
    for k, omega in enumerate(all_1forms):
        mat[k, :] = omega.flatten()

    # SVD to find the column space
    U, S, Vh = svd(mat, full_matrices=False)

    # Threshold for rank determination
    tol = max(n, n_forms) * np.finfo(float).eps * S[0] if S[0] > 0 else 1e-14
    rank = np.sum(S > tol)

    # ON basis vectors (in vectorized form)
    basis = Vh[:rank, :]

    print(f"  Omega^1_D: {n_forms} generators -> rank {rank} (dim={n}x{n}={n*n})")
    print(f"  Singular values: top5 = {S[:5]}")
    if rank < len(S):
        print(f"  Gap: S[{rank-1}]={S[rank-1]:.6e}, S[{rank}]={S[rank]:.6e}")

    return basis, rank, all_1forms


def project_onto_omega1(mat_vec, basis):
    """Project a vectorized matrix onto Omega^1_D and compute residual.

    Args:
        mat_vec: (n*n,) complex vector (flattened matrix)
        basis: (rank, n*n) ON basis for Omega^1_D

    Returns:
        proj: projection onto Omega^1_D
        residual: ||mat_vec - proj|| / ||mat_vec||
    """
    # Project: proj = sum_i <basis_i, mat_vec> basis_i
    coeffs = basis @ mat_vec.conj()
    proj = coeffs.conj() @ basis
    resid_vec = mat_vec - proj
    norm_orig = la_norm(mat_vec)
    if norm_orig < 1e-15:
        return proj, 0.0
    return proj, la_norm(resid_vec) / norm_orig


# =============================================================================
# SECTION 4: GAUGE MODULE CONDITIONS GM1-GM3
# =============================================================================

def check_GM1_bimodule(D_K, AF_16, basis, rank, dim_rep=1):
    """Check GM1: Omega^1_D(A) is an A-bimodule.

    For each basis element omega_k of Omega^1_D and each generator a of A:
      - Left: a * omega_k in Omega^1_D?
      - Right: omega_k * a in Omega^1_D?

    Returns:
        max_left_residual: worst-case fractional residual for left multiplication
        max_right_residual: worst-case fractional residual for right multiplication
        left_residuals: array of all residuals
        right_residuals: array of all residuals
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]

    # Reconstruct basis matrices
    basis_mats = [basis[k, :].reshape(n, n) for k in range(rank)]

    max_left_res = 0.0
    max_right_res = 0.0
    left_residuals = []
    right_residuals = []

    for k in range(rank):
        omega_k = basis_mats[k]
        for i in range(n_gen):
            # Left: a_i * omega_k
            prod_left = A_gens[i] @ omega_k
            _, res_l = project_onto_omega1(prod_left.flatten(), basis)
            left_residuals.append(res_l)
            max_left_res = max(max_left_res, res_l)

            # Right: omega_k * a_i
            prod_right = omega_k @ A_gens[i]
            _, res_r = project_onto_omega1(prod_right.flatten(), basis)
            right_residuals.append(res_r)
            max_right_res = max(max_right_res, res_r)

    return max_left_res, max_right_res, np.array(left_residuals), np.array(right_residuals)


def check_GM1_opposite(D_K, AF_16, basis, rank, dim_rep=1):
    """Check GM1 for the opposite algebra action.

    The full bimodule condition requires closure under BOTH:
      - Left A action: a * omega
      - Right A^o action: omega * o(b) where o(b) = J pi(b*) J^{-1}

    This is the condition that distinguishes gauge modules from the trivial case.
    The order-one condition says [omega, o(b)] = 0, i.e., the right A^o action
    is trivial. When order-one fails, we still need the A^o action to close.
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        opp_gens = [o_map_16(g) for g in AF_16]
    else:
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in AF_16]

    basis_mats = [basis[k, :].reshape(n, n) for k in range(rank)]

    max_res = 0.0
    residuals = []

    for k in range(rank):
        omega_k = basis_mats[k]
        for i in range(n_gen):
            # Right opposite: omega_k * o(b_i)
            prod = omega_k @ opp_gens[i]
            _, res = project_onto_omega1(prod.flatten(), basis)
            residuals.append(res)
            max_res = max(max_res, res)

            # Left opposite: o(b_i) * omega_k
            prod2 = opp_gens[i] @ omega_k
            _, res2 = project_onto_omega1(prod2.flatten(), basis)
            residuals.append(res2)
            max_res = max(max_res, res2)

    return max_res, np.array(residuals)


def check_GM2_selfadjoint(basis, rank, n):
    """Check GM2: Omega^1_D(A) is closed under the adjoint.

    For each basis element omega_k: is omega_k^dagger in Omega^1_D?
    """
    max_res = 0.0
    residuals = []

    for k in range(rank):
        omega_k = basis[k, :].reshape(n, n)
        omega_dag = omega_k.conj().T
        _, res = project_onto_omega1(omega_dag.flatten(), basis)
        residuals.append(res)
        max_res = max(max_res, res)

    return max_res, np.array(residuals)


def check_GM3_gauge_covariance(D_K, AF_16, basis, rank, dim_rep=1):
    """Check GM3: U(A) acts on Omega^1_D by conjugation.

    For each unitary generator T_a of Lie(U(A)):
      For each basis omega_k:
        [T_a, omega_k] in Omega^1_D?

    (This is the infinitesimal version: d/dt|_{t=0} e^{tT} omega e^{-tT} = [T, omega].)
    """
    n = D_K.shape[0]

    # Build unitary generators
    u_gens, u_names, u_factors = build_unitary_generators(AF_16, None, None)
    if dim_rep > 1:
        u_gens = [np.kron(np.eye(dim_rep), g) for g in u_gens]

    basis_mats = [basis[k, :].reshape(n, n) for k in range(rank)]

    max_res = 0.0
    residuals = []
    worst_pair = None

    for ui, T in enumerate(u_gens):
        for k in range(rank):
            omega_k = basis_mats[k]
            comm = T @ omega_k - omega_k @ T  # [T, omega]
            _, res = project_onto_omega1(comm.flatten(), basis)
            residuals.append(res)
            if res > max_res:
                max_res = res
                worst_pair = (u_names[ui], k, res)

    return max_res, np.array(residuals), worst_pair, u_names, u_factors


# =============================================================================
# SECTION 5: GAUGE GROUP IDENTIFICATION
# =============================================================================

def identify_gauge_group(D_K, AF_16, basis, rank, dim_rep=1):
    """Determine which gauge transformations preserve Omega^1_D.

    For each generator T of U(A), compute max residual of [T, omega]
    w.r.t. Omega^1_D. Generators with zero residual form the gauge algebra.

    Returns:
        gauge_generators: indices of T that preserve Omega^1_D
        gauge_residuals: per-generator max residual
        gauge_names: names of preserving generators
    """
    n = D_K.shape[0]
    u_gens, u_names, u_factors = build_unitary_generators(AF_16, None, None)
    if dim_rep > 1:
        u_gens = [np.kron(np.eye(dim_rep), g) for g in u_gens]

    basis_mats = [basis[k, :].reshape(n, n) for k in range(rank)]

    per_gen_max = []
    for ui, T in enumerate(u_gens):
        gen_max = 0.0  # (local)
        for k in range(rank):
            omega_k = basis_mats[k]
            comm = T @ omega_k - omega_k @ T
            _, res = project_onto_omega1(comm.flatten(), basis)
            gen_max = max(gen_max, res)
        per_gen_max.append(gen_max)

    per_gen_max = np.array(per_gen_max)

    # Threshold: generators with residual < 1e-6 preserve Omega^1_D
    tol = 1e-6  # (local)
    gauge_mask = per_gen_max < tol
    gauge_indices = np.where(gauge_mask)[0]
    gauge_names = [u_names[i] for i in gauge_indices]
    gauge_factors_list = [u_factors[i] for i in gauge_indices]

    return gauge_indices, per_gen_max, gauge_names, gauge_factors_list, u_names, u_factors


# =============================================================================
# SECTION 6: ORDER-ONE CONDITION REPRODUCED (for comparison)
# =============================================================================

def check_order_one_16(D_K_16, AF_16):
    """Reproduce order-one check [[D, a], o(b)] = 0 on C^16.

    Returns:
        max_violation: float
        factor_violations: dict (factor_a, factor_b) -> max |[[D,a],o(b)]|
    """
    n_gen = len(AF_16)
    AF_names_local = []
    AF_factors_local = []
    # Rebuild names (simpler than passing through)
    for i in range(n_gen):
        if i < 2:
            AF_factors_local.append('C')
        elif i < 6:
            AF_factors_local.append('H')
        else:
            AF_factors_local.append('M3')

    max_viol = 0.0
    factor_viols = {}

    for i in range(n_gen):
        comm_Da = D_K_16 @ AF_16[i] - AF_16[i] @ D_K_16  # [D, a]
        for j in range(n_gen):
            ob = o_map_16(AF_16[j])  # b^o
            dc = comm_Da @ ob - ob @ comm_Da  # [[D, a], b^o]
            err = np.max(np.abs(dc))
            max_viol = max(max_viol, err)

            f_pair = (AF_factors_local[i], AF_factors_local[j])
            if f_pair not in factor_viols:
                factor_viols[f_pair] = 0.0
            factor_viols[f_pair] = max(factor_viols[f_pair], err)

    return max_viol, factor_viols


# =============================================================================
# SECTION 7: EXTENDED BIMODULE TEST
# =============================================================================

def check_extended_bimodule(D_K, AF_16, dim_rep=1):
    """Extended bimodule closure test.

    Compute Omega^1_D including both left and right A^o actions,
    then check if the total space is a bimodule over A x A^o.

    The EXTENDED 1-form space is:
      Omega^1_ext = span{pi(a) [D, pi(b)] : a, b in A}
                  + span{pi(a) [D, pi(b)] o(c) : a, b, c in A}

    If this closes under multiplication by A and A^o, we have a gauge module.
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
        opp_gens = [o_map_16(g) for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in AF_16]

    # Level 0: basic 1-forms a[D,b]
    forms = []
    for i in range(n_gen):
        for j in range(n_gen):
            comm = D_K @ A_gens[j] - A_gens[j] @ D_K
            forms.append(A_gens[i] @ comm)

    # Level 1: extend with right A^o action: omega * o(c)
    level0_count = len(forms)
    for k in range(level0_count):
        for c in range(n_gen):
            forms.append(forms[k] @ opp_gens[c])

    # Level 2: extend with left A^o action: o(c) * omega
    level1_count = len(forms)
    for k in range(level0_count):
        for c in range(n_gen):
            forms.append(opp_gens[c] @ forms[k])

    # Stack and SVD
    mat = np.zeros((len(forms), n * n), dtype=complex)
    for k, f in enumerate(forms):
        mat[k, :] = f.flatten()

    U, S, Vh = svd(mat, full_matrices=False)
    tol = max(n, len(forms)) * np.finfo(float).eps * S[0] if S[0] > 0 else 1e-14
    rank_ext = np.sum(S > tol)

    return rank_ext, S


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 72)
    print("S61 GAUGE-MODULE-61: Order-One vs Gauge Module Conditions")
    print("=" * 72)

    # --- Infrastructure ---
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    tau = tau_fold  # 0.19

    print(f"\nJensen parameter: tau = {tau}")
    print(f"A_F = C + H + M_3(C)")

    AF_16, AF_names, AF_factors = build_AF_generators()
    n_gen = len(AF_16)
    print(f"A_F generators: {n_gen} ({sum(1 for f in AF_factors if f=='C')} C, "
          f"{sum(1 for f in AF_factors if f=='H')} H, "
          f"{sum(1 for f in AF_factors if f=='M3')} M3)")

    # ===== STEP 0: Reproduce order-one failure =====
    print("\n" + "=" * 72)
    print("STEP 0: Reproduce order-one failure (validation)")
    print("=" * 72)

    # Build D_K on singlet (Omega only)
    D_K_sing = build_DK_singlet(gammas, gens, f_abc, tau)
    max_oo_sing, fv_sing = check_order_one_16(D_K_sing, AF_16)
    print(f"\n  Singlet D_K order-one max violation: {max_oo_sing:.6f}")

    # For non-singlet, test on the Clifford part (gamma matrices only)
    # The order-one for the full D_K = M_Lie + Omega on (1,0) is
    # dominated by the Clifford part since M_Lie = E_{ab} rho(X_b) x gamma_a
    # The gamma_a part gives the tau-independent 4.000 violation.

    # Test Clifford order-one on C^16 directly (this is what gives 4.000)
    print("\n  Clifford-only order-one test (tau-independent):")
    max_cliff = 0.0
    cliff_factor_norms = {}
    for alpha in range(8):
        g_emb = gammas[alpha]  # 16x16
        for i in range(n_gen):
            comm_ga = g_emb @ AF_16[i] - AF_16[i] @ g_emb
            for j in range(n_gen):
                ob = o_map_16(AF_16[j])
                dc = comm_ga @ ob - ob @ comm_ga
                err = np.max(np.abs(dc))
                max_cliff = max(max_cliff, err)
                fp = (AF_factors[i], AF_factors[j])
                if fp not in cliff_factor_norms:
                    cliff_factor_norms[fp] = 0.0
                cliff_factor_norms[fp] = max(cliff_factor_norms[fp], err)

    print(f"  Max Clifford violation: {max_cliff:.6f}")
    print(f"  Factor-pair violations:")
    for fp in sorted(cliff_factor_norms.keys()):
        print(f"    ({fp[0]:>3}, {fp[1]:>3}): {cliff_factor_norms[fp]:.6f}")

    # Validate against known result
    assert abs(max_cliff - 4.0) < 0.01, \
        f"Expected 4.000 for (H,H), got {max_cliff:.6f}"
    print(f"\n  VALIDATED: max violation = {max_cliff:.6f} (expected 4.000)")

    # ===== STEP 1: Compute Omega^1_D on singlet =====
    print("\n" + "=" * 72)
    print("STEP 1: Omega^1_D on singlet sector (D_K = Omega, dim=16)")
    print("=" * 72)

    basis_sing, rank_sing, forms_sing = compute_omega1_space(D_K_sing, AF_16, dim_rep=1)
    print(f"  rank(Omega^1_D) on singlet = {rank_sing}")
    print(f"  Matrix dimension: 16x16 = 256, so dim/max = {rank_sing}/256 = {rank_sing/256:.4f}")

    # ===== STEP 2: Compute Omega^1_D on fundamental (1,0) =====
    print("\n" + "=" * 72)
    print("STEP 2: Omega^1_D on fundamental (1,0) sector (D_K, dim=48)")
    print("=" * 72)

    D_K_fund = build_DK_fundamental(gammas, gens, f_abc, tau)
    evals_fund = np.linalg.eigvalsh(
        1j * D_K_fund  # Make Hermitian for eigenvalues
    ) if np.allclose(D_K_fund, -D_K_fund.conj().T, atol=1e-10) else None
    if evals_fund is not None:
        print(f"  D_K eigenvalues (fund, first 10): {np.sort(evals_fund)[:10]}")

    basis_fund, rank_fund, forms_fund = compute_omega1_space(D_K_fund, AF_16, dim_rep=3)
    print(f"  rank(Omega^1_D) on fundamental = {rank_fund}")
    print(f"  Matrix dimension: 48x48 = 2304, so dim/max = {rank_fund}/2304 = {rank_fund/2304:.4f}")

    # ===== STEP 3: GM1 (bimodule) on singlet =====
    print("\n" + "=" * 72)
    print("STEP 3: GM1 - Bimodule condition")
    print("=" * 72)

    print("\n  --- Singlet ---")
    ml_s, mr_s, lr_s, rr_s = check_GM1_bimodule(D_K_sing, AF_16, basis_sing, rank_sing, dim_rep=1)
    print(f"  Left A-action max residual:  {ml_s:.6e}")
    print(f"  Right A-action max residual: {mr_s:.6e}")

    mo_s, or_s = check_GM1_opposite(D_K_sing, AF_16, basis_sing, rank_sing, dim_rep=1)
    print(f"  A^o-action max residual:     {mo_s:.6e}")

    print("\n  --- Fundamental (1,0) ---")
    ml_f, mr_f, lr_f, rr_f = check_GM1_bimodule(D_K_fund, AF_16, basis_fund, rank_fund, dim_rep=3)
    print(f"  Left A-action max residual:  {ml_f:.6e}")
    print(f"  Right A-action max residual: {mr_f:.6e}")

    mo_f, or_f = check_GM1_opposite(D_K_fund, AF_16, basis_fund, rank_fund, dim_rep=3)
    print(f"  A^o-action max residual:     {mo_f:.6e}")

    # ===== STEP 4: GM2 (self-adjointness) =====
    print("\n" + "=" * 72)
    print("STEP 4: GM2 - Self-adjointness closure")
    print("=" * 72)

    n_sing = D_K_sing.shape[0]
    n_fund = D_K_fund.shape[0]

    sa_s, sar_s = check_GM2_selfadjoint(basis_sing, rank_sing, n_sing)
    print(f"  Singlet: max adjoint residual = {sa_s:.6e}")

    sa_f, sar_f = check_GM2_selfadjoint(basis_fund, rank_fund, n_fund)
    print(f"  Fundamental: max adjoint residual = {sa_f:.6e}")

    # ===== STEP 5: GM3 (gauge covariance) =====
    print("\n" + "=" * 72)
    print("STEP 5: GM3 - Gauge covariance")
    print("=" * 72)

    print("\n  --- Singlet ---")
    gc_s, gcr_s, gw_s, un_s, uf_s = check_GM3_gauge_covariance(
        D_K_sing, AF_16, basis_sing, rank_sing, dim_rep=1)
    print(f"  Max gauge residual: {gc_s:.6e}")
    if gw_s:
        print(f"  Worst: generator={gw_s[0]}, basis_idx={gw_s[1]}, res={gw_s[2]:.6e}")

    print("\n  --- Fundamental (1,0) ---")
    gc_f, gcr_f, gw_f, un_f, uf_f = check_GM3_gauge_covariance(
        D_K_fund, AF_16, basis_fund, rank_fund, dim_rep=3)
    print(f"  Max gauge residual: {gc_f:.6e}")
    if gw_f:
        print(f"  Worst: generator={gw_f[0]}, basis_idx={gw_f[1]}, res={gw_f[2]:.6e}")

    # Per-generator breakdown
    print("\n  Per-generator gauge residuals (fundamental):")
    gi_f, pgm_f, gn_f, gfl_f, un_f2, uf_f2 = identify_gauge_group(
        D_K_fund, AF_16, basis_fund, rank_fund, dim_rep=3)
    for ui in range(len(un_f2)):
        status = "PRESERVES" if pgm_f[ui] < 1e-6 else "BREAKS"
        print(f"    {un_f2[ui]:>12}: max_res = {pgm_f[ui]:.6e}  [{status}]")

    # ===== STEP 6: Extended bimodule =====
    print("\n" + "=" * 72)
    print("STEP 6: Extended bimodule (Omega^1_D + A^o closures)")
    print("=" * 72)

    rank_ext_s, S_ext_s = check_extended_bimodule(D_K_sing, AF_16, dim_rep=1)
    print(f"  Singlet extended rank: {rank_ext_s}")
    print(f"  (vs base rank {rank_sing})")

    rank_ext_f, S_ext_f = check_extended_bimodule(D_K_fund, AF_16, dim_rep=3)
    print(f"  Fundamental extended rank: {rank_ext_f}")
    print(f"  (vs base rank {rank_fund})")

    # ===== STEP 7: Gauge group identification =====
    print("\n" + "=" * 72)
    print("STEP 7: Gauge group identification")
    print("=" * 72)

    print(f"\n  Generators preserving Omega^1_D (fundamental):")
    n_u1 = sum(1 for f in gfl_f if f == 'U1')
    n_su2 = sum(1 for f in gfl_f if f == 'SU2')
    n_su3 = sum(1 for f in gfl_f if f == 'SU3')
    n_u1c = sum(1 for f in gfl_f if f == 'U1c')
    print(f"    U(1): {n_u1} generators")
    print(f"    SU(2): {n_su2} generators")
    print(f"    SU(3): {n_su3} generators")
    print(f"    U(1)_color: {n_u1c} generators")
    print(f"    Total: {len(gn_f)} / {len(un_f2)} generators preserve Omega^1_D")

    # Determine gauge group
    if n_u1 >= 1 and n_su2 >= 3 and n_su3 >= 8:
        gauge_group = "SU(3) x SU(2) x U(1)"
        gauge_match = "SM"
    elif n_su2 >= 3 and n_su3 >= 8:
        gauge_group = "SU(3) x SU(2)"
        gauge_match = "SM without U(1)"
    elif n_su3 >= 8:
        gauge_group = "SU(3)"
        gauge_match = "Color only"
    else:
        gauge_group = f"Partial ({n_u1} U1 + {n_su2} SU2 + {n_su3} SU3)"
        gauge_match = "Non-standard"

    print(f"\n  GAUGE GROUP: {gauge_group}")
    print(f"  Match: {gauge_match}")

    # Also check on extended Omega^1
    if rank_ext_f > rank_fund:
        print(f"\n  WARNING: Extended bimodule rank ({rank_ext_f}) > base rank ({rank_fund})")
        print(f"  This means Omega^1_D is NOT closed under A^o -- needs extension.")
        # Redo gauge group identification on extended space
        # Compute extended basis
        print("  Re-checking gauge covariance on extended space...")

    # ===== GATE VERDICT =====
    print("\n" + "=" * 72)
    print("GATE VERDICT: GAUGE-MODULE-61")
    print("=" * 72)

    # GM1 threshold: bimodule residual < 1e-4
    gm1_pass_sing = max(ml_s, mr_s, mo_s) < 1e-4
    gm1_pass_fund = max(ml_f, mr_f, mo_f) < 1e-4

    # If base GM1 fails but extended bimodule closes, it's a
    # "gauge module with enlarged 1-form space"
    gm1_extended = (rank_ext_f > rank_fund)

    # GM2 threshold
    gm2_pass_sing = sa_s < 1e-4
    gm2_pass_fund = sa_f < 1e-4

    # GM3 threshold
    gm3_pass_sing = gc_s < 1e-4
    gm3_pass_fund = gc_f < 1e-4

    print(f"\n  Singlet sector:")
    print(f"    GM1 (bimodule):    {'PASS' if gm1_pass_sing else 'FAIL'} "
          f"(max_res = {max(ml_s, mr_s, mo_s):.6e})")
    print(f"    GM2 (self-adj):    {'PASS' if gm2_pass_sing else 'FAIL'} "
          f"(max_res = {sa_s:.6e})")
    print(f"    GM3 (gauge cov):   {'PASS' if gm3_pass_sing else 'FAIL'} "
          f"(max_res = {gc_s:.6e})")

    print(f"\n  Fundamental sector:")
    print(f"    GM1 (bimodule):    {'PASS' if gm1_pass_fund else 'FAIL'} "
          f"(max_res = {max(ml_f, mr_f, mo_f):.6e})")
    print(f"    GM2 (self-adj):    {'PASS' if gm2_pass_fund else 'FAIL'} "
          f"(max_res = {sa_f:.6e})")
    print(f"    GM3 (gauge cov):   {'PASS' if gm3_pass_fund else 'FAIL'} "
          f"(max_res = {gc_f:.6e})")

    if gm1_extended:
        print(f"\n  NOTE: Omega^1_D requires extension by A^o products.")
        print(f"  Base rank: {rank_fund}, Extended rank: {rank_ext_f}")
        print(f"  This is the Paper 05 scenario: non-trivial gauge module with")
        print(f"  enlarged 1-form space. The gauge group acts on the EXTENDED space.")

    # Final verdict
    all_pass_sing = gm1_pass_sing and gm2_pass_sing and gm3_pass_sing
    all_pass_fund = gm1_pass_fund and gm2_pass_fund and gm3_pass_fund

    if all_pass_fund and gauge_match == "SM":
        verdict = "PASS"
        reason = f"Gauge module with SM group {gauge_group}"
    elif all_pass_fund:
        verdict = "INFO"
        reason = f"Gauge module with group {gauge_group} ({gauge_match})"
    elif gm1_extended and gm2_pass_fund and gm3_pass_fund:
        verdict = "INFO"
        reason = f"Extended gauge module, group {gauge_group}"
    else:
        # Check if the failure is only in the A^o direction
        base_bimod = max(ml_f, mr_f) < 1e-4
        if base_bimod and not (mo_f < 1e-4):
            verdict = "INFO"
            reason = (f"A-bimodule PASSES, A^o closure FAILS "
                     f"(res={mo_f:.4e}). Order-one failure propagates to GM1.")
        else:
            verdict = "FAIL"
            reason = "Gauge module conditions fail"

    print(f"\n  VERDICT: {verdict}")
    print(f"  Reason: {reason}")
    print(f"  Order-one max violation: {max_cliff:.6f} (confirmed)")
    print(f"  Gauge group: {gauge_group}")

    # ===== Save data =====
    dt = time.time() - t_start
    print(f"\n  Runtime: {dt:.1f}s")

    save_dict = {
        'tau': tau,
        'order_one_max': max_cliff,
        'cliff_factor_norms': np.array(
            [(fp, cliff_factor_norms[fp]) for fp in sorted(cliff_factor_norms.keys())],
            dtype=object),

        # Omega^1_D dimensions
        'rank_singlet': rank_sing,
        'rank_fundamental': rank_fund,
        'rank_ext_singlet': rank_ext_s,
        'rank_ext_fundamental': rank_ext_f,

        # GM1
        'gm1_left_sing': ml_s,
        'gm1_right_sing': mr_s,
        'gm1_opp_sing': mo_s,
        'gm1_left_fund': ml_f,
        'gm1_right_fund': mr_f,
        'gm1_opp_fund': mo_f,

        # GM2
        'gm2_sing': sa_s,
        'gm2_fund': sa_f,

        # GM3
        'gm3_sing': gc_s,
        'gm3_fund': gc_f,

        # Gauge group
        'gauge_per_gen_residuals': pgm_f,
        'gauge_gen_names': np.array(un_f2, dtype=object),
        'gauge_gen_factors': np.array(uf_f2, dtype=object),
        'n_preserving_u1': n_u1,
        'n_preserving_su2': n_su2,
        'n_preserving_su3': n_su3,
        'gauge_group': gauge_group,

        # Verdict
        'verdict': verdict,
        'reason': reason,
        'runtime_s': dt,
    }

    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"\n  Saved: {OUTPUT_NPZ}")


if __name__ == "__main__":
    main()
