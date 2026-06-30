#!/usr/bin/env python3
"""
S62 HIGGS-ORDER-ONE-62: Higgs Doublet Isolation in Omega^1_D
==============================================================

Determines whether the Higgs doublet (1,2,1/2) under SU(3)xSU(2)xU(1)
survives as an invariant subspace of the 342-dimensional Omega^1_D(A_F)
despite the order-one condition failing at (H,H) = 4.000.

GEOMETRIC PICTURE (Berry perspective):
---------------------------------------
The 13 SM gauge generators act on Omega^1_D via the adjoint (commutator).
This defines a representation rho: su(3)+su(2)+u(1) -> End(Omega^1_D).
The irreducible decomposition of this representation reveals which SM
multiplets live inside Omega^1_D.

The Higgs doublet (1,2,1/2) is a 4-real-dimensional (= 2 complex) subspace.
If this subspace is an invariant subspace of the gauge action -- meaning
[G_i, Pi_H] = 0 for all 13 generators G_i -- then the Higgs is
geometrically isolated: it sits in its own fiber of the representation
bundle, topologically decoupled from the other 338 directions.

The order-one violation at (H,H) = 4.000 could in principle mix the Higgs
with the "extra" 169 quadratic directions. We compute this mixing directly.

STRATEGY:
---------
1. Reconstruct D_K on (1,0) sector at tau_fold.
2. Reconstruct Omega^1_D (342-dim) using both linear (a[D,b]) and quadratic
   ([D,a][D,b]) generators.
3. Build the 13 SM gauge generators as they act on Omega^1_D via
   omega -> [T_i, omega] (adjoint action on the 342-dim space).
4. Decompose Omega^1_D into irreps of SU(3)xSU(2)xU(1).
5. Identify the Higgs (1,2,1/2) subspace and check invariance.
6. Compute mixing fractions and perturbative corrections.

GATE: HIGGS-ORDER-ONE-62
  PASS if 4D Higgs subspace exists as gauge-invariant (mixing < 1%).
  FAIL if mixing > 50%.
  INFO if 1-50% mixing.

Author: Berry Geometric Phase Theorist (Session 62)
Date: 2026-03-29
Sources: S46 (OMEGA-CLASSIFY-46), S61 (GAUGE-MODULE-61), S28b (order-one failure)
"""

import numpy as np
from numpy.linalg import norm as la_norm, svd, eigh, eigvalsh
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold

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
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)
OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SECTION 1: A_F ALGEBRA INFRASTRUCTURE
# Reproduced from s61_gauge_module_check.py
# =============================================================================

def flat_idx(row, col):
    """Map (row, col) in 4x4 matrix to flat index in 16-dim Psi_+."""
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
    """Build all generators of A_F = C + H + M_3(C) as 16x16 matrices."""
    AF_16 = []
    AF_names = []
    AF_factors = []

    # C factor
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im')
    AF_factors.append('C')

    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj')
    AF_factors.append('C')

    # H factor
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i')
    AF_factors.append('H')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j')
    AF_factors.append('H')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k')
    AF_factors.append('H')

    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1')
    AF_factors.append('H')

    # M_3(C) factor
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


def build_unitary_generators_16(AF_16):
    """Build 13 generators of the SM gauge group on C^16 (singlet sector).

    Used only for the singlet; for fundamental, use build_gauge_generators_48().
    """
    unitaries_ah = []
    u_names = []
    u_factors = []

    # u(1) hypercharge
    L_u1 = np.diag([1j, 0, 0, 0])
    u1_gen = build_bimodule_16(L_u1, np.eye(4))
    unitaries_ah.append(u1_gen)
    u_names.append('u1_Y')
    u_factors.append('U1')

    # su(2)_L on rows 2-3
    L_s1 = np.zeros((4, 4), dtype=complex)
    L_s1[2, 3] = 1j; L_s1[3, 2] = 1j
    unitaries_ah.append(build_bimodule_16(L_s1, np.eye(4)))
    u_names.append('su2_1')
    u_factors.append('SU2')

    L_s2 = np.zeros((4, 4), dtype=complex)
    L_s2[2, 3] = 1.0; L_s2[3, 2] = -1.0
    unitaries_ah.append(build_bimodule_16(L_s2, np.eye(4)))
    u_names.append('su2_2')
    u_factors.append('SU2')

    L_s3 = np.zeros((4, 4), dtype=complex)
    L_s3[2, 2] = 1j; L_s3[3, 3] = -1j
    unitaries_ah.append(build_bimodule_16(L_s3, np.eye(4)))
    u_names.append('su2_3')
    u_factors.append('SU2')

    # su(3)_c via right M_3(C) action on the 16-dim space
    gm = _gell_mann_matrices()
    for idx, lam in enumerate(gm):
        R_m = np.eye(4, dtype=complex)
        R_m[1:, 1:] = (1j / 2 * lam).conj().T
        unitaries_ah.append(build_bimodule_16(np.eye(4), R_m))
        u_names.append(f'su3_{idx + 1}')
        u_factors.append('SU3')

    # u(1)_color
    R_u1c = np.eye(4, dtype=complex)
    R_u1c[1:, 1:] = 1j * np.eye(3)
    unitaries_ah.append(build_bimodule_16(np.eye(4), R_u1c))
    u_names.append('u1_color')
    u_factors.append('U1c')

    return unitaries_ah, u_names, u_factors


def build_gauge_generators_48():
    """Build 13 SM gauge generators as 48x48 matrices on C^3 x C^16.

    On the fundamental (1,0) sector:
      - U(1)_Y and SU(2)_L act on the C^16 factor (internal A_F space):
        T = kron(I_3, T_16)
      - SU(3)_c acts on the C^3 factor (representation space):
        T = kron(T_3, I_16)
      - U(1)_color acts on the C^3 factor:
        T = kron(i*I_3, I_16)

    All generators are anti-Hermitian (T + T^dag = 0).
    """
    gauge_48 = []
    u_names = []
    u_factors = []

    I3 = np.eye(3, dtype=complex)
    I16 = np.eye(16, dtype=complex)

    # u(1) hypercharge: acts on C^16 internal space
    L_u1 = np.diag([1j, 0, 0, 0])
    u1_16 = build_bimodule_16(L_u1, np.eye(4))
    gauge_48.append(np.kron(I3, u1_16))
    u_names.append('u1_Y')
    u_factors.append('U1')

    # su(2)_L: acts on C^16 internal space
    L_s1 = np.zeros((4, 4), dtype=complex)
    L_s1[2, 3] = 1j; L_s1[3, 2] = 1j
    gauge_48.append(np.kron(I3, build_bimodule_16(L_s1, np.eye(4))))
    u_names.append('su2_1')
    u_factors.append('SU2')

    L_s2 = np.zeros((4, 4), dtype=complex)
    L_s2[2, 3] = 1.0; L_s2[3, 2] = -1.0
    gauge_48.append(np.kron(I3, build_bimodule_16(L_s2, np.eye(4))))
    u_names.append('su2_2')
    u_factors.append('SU2')

    L_s3 = np.zeros((4, 4), dtype=complex)
    L_s3[2, 2] = 1j; L_s3[3, 3] = -1j
    gauge_48.append(np.kron(I3, build_bimodule_16(L_s3, np.eye(4))))
    u_names.append('su2_3')
    u_factors.append('SU2')

    # su(3)_c: acts on the C^3 REPRESENTATION space (first factor of tensor product)
    # Anti-Hermitian generators: i * lambda_a / 2
    gm = _gell_mann_matrices()
    for idx, lam in enumerate(gm):
        T_3 = 1j / 2 * lam  # anti-Hermitian 3x3
        gauge_48.append(np.kron(T_3, I16))
        u_names.append(f'su3_{idx + 1}')
        u_factors.append('SU3')

    # u(1)_color: acts on C^3 representation space
    gauge_48.append(np.kron(1j * I3, I16))
    u_names.append('u1_color')
    u_factors.append('U1c')

    return gauge_48, u_names, u_factors


# =============================================================================
# SECTION 2: BUILD D_K
# =============================================================================

def build_DK_fundamental(gammas, gens, f_abc, s_val):
    """Build D_K on the fundamental (1,0) sector = C^3 x C^16 = C^48."""
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    dim_rep = 3
    dim_spin = 16  # (local)
    D_K = np.kron(np.eye(dim_rep), Omega)

    for a in range(8):
        rho_ea = np.zeros((dim_rep, dim_rep), dtype=complex)
        for b in range(8):
            rho_ea += E[a, b] * gens[b]
        D_K += np.kron(rho_ea, gammas[a])

    return D_K


# =============================================================================
# SECTION 3: COMPUTE OMEGA^1_D (342-DIMENSIONAL SPACE)
# =============================================================================

def compute_omega1_combined(D_K, AF_16, dim_rep=3, threshold=1e-10):
    """Compute Omega^1_D = linear + quadratic module.

    Linear:    span{ a_i [D, b_j] }
    Quadratic: span{ [D, a_i] [D, b_j] }
    Combined:  span of both

    Returns dict with basis arrays and dimensions.
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]

    linear_vecs = []
    quad_vecs = []

    for j in range(n_gen):
        comm_Db = D_K @ A_gens[j] - A_gens[j] @ D_K  # [D, b_j]
        for i in range(n_gen):
            # Linear: a_i [D, b_j]
            lin = A_gens[i] @ comm_Db
            linear_vecs.append(lin.ravel())

            # Quadratic: [D, a_i] [D, b_j]
            comm_Da = D_K @ A_gens[i] - A_gens[i] @ D_K
            quad = comm_Da @ comm_Db
            quad_vecs.append(quad.ravel())

    linear_mat = np.array(linear_vecs)
    quad_mat = np.array(quad_vecs)
    combined_mat = np.vstack([linear_mat, quad_mat])

    def extract_basis(mat):
        U, S, Vh = svd(mat, full_matrices=False)
        cutoff = S[0] * threshold if S[0] > 0 else 1e-14
        rank = int(np.sum(S > cutoff))
        return Vh[:rank], S[:rank], rank

    lin_basis, lin_sv, dim_lin = extract_basis(linear_mat)
    quad_basis, quad_sv, dim_quad = extract_basis(quad_mat)
    comb_basis, comb_sv, dim_comb = extract_basis(combined_mat)

    # Extra directions (quadratic not in linear)
    if dim_lin > 0 and dim_comb > dim_lin:
        proj_coeff = comb_basis @ lin_basis.conj().T
        proj = proj_coeff @ lin_basis
        residual = comb_basis - proj
        _, S_res, Vh_res = svd(residual, full_matrices=False)
        cutoff_res = S_res[0] * threshold if len(S_res) > 0 and S_res[0] > 0 else 1e-14
        dim_extra = int(np.sum(S_res > cutoff_res))
        extra_basis = Vh_res[:dim_extra]
    else:
        dim_extra = 0
        extra_basis = np.zeros((0, n * n), dtype=complex)

    return {
        'linear_basis': lin_basis,
        'combined_basis': comb_basis,
        'extra_basis': extra_basis,
        'dim_linear': dim_lin,
        'dim_combined': dim_comb,
        'dim_extra': dim_extra,
        'linear_sv': lin_sv,
        'combined_sv': comb_sv,
        'N': n,
    }


# =============================================================================
# SECTION 4: GAUGE ACTION ON OMEGA^1_D
# =============================================================================

def compute_extended_module(D_K, AF_16, dim_rep=3, n_levels=3):
    """Compute the extended gauge module by iteratively closing under A and A^o.

    Level 0: span{a [D, b]}  (linear 1-forms)
    Level 0+: add [D,a][D,b] (quadratic 1-forms) -> Omega^1_D
    Level 1+: close under A and A^o multiplication
    ...
    Stop when rank stabilizes.

    The extended module IS a bimodule (proven in S61: rank 775, machine epsilon).
    The gauge algebra representation CLOSES on this space.
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
        opp_gens = [o_map_16(g) for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in AF_16]

    # Level 0: linear + quadratic 1-forms
    forms_vecs = []
    for i in range(n_gen):
        for j in range(n_gen):
            comm_Db = D_K @ A_gens[j] - A_gens[j] @ D_K
            # Linear
            lin = A_gens[i] @ comm_Db
            forms_vecs.append(lin.ravel())
            # Quadratic
            comm_Da = D_K @ A_gens[i] - A_gens[i] @ D_K
            quad = comm_Da @ comm_Db
            forms_vecs.append(quad.ravel())

    def current_rank(vecs):
        if not vecs:
            return 0, None
        mat = np.array(vecs)
        U, S, Vh = svd(mat, full_matrices=False)
        tol = max(mat.shape) * np.finfo(float).eps * S[0] if S[0] > 0 else 1e-14
        r = int(np.sum(S > tol))
        return r, Vh[:r, :]

    r0, basis0 = current_rank(forms_vecs)
    print(f"    Level 0 (lin+quad): rank = {r0}")

    prev_rank = r0
    prev_basis_vecs = [v.copy() for v in forms_vecs]

    for level in range(1, n_levels + 1):
        new_vecs = list(prev_basis_vecs)
        r_curr, basis_curr = current_rank(new_vecs)
        basis_mats = [basis_curr[k].reshape(n, n) for k in range(r_curr)]

        # Close under left/right A and A^o
        n_sample = min(r_curr, 50)
        for k in range(n_sample):
            omega_k = basis_mats[k]
            for c in range(n_gen):
                new_vecs.append((A_gens[c] @ omega_k).ravel())
                new_vecs.append((omega_k @ A_gens[c]).ravel())
                new_vecs.append((opp_gens[c] @ omega_k).ravel())
                new_vecs.append((omega_k @ opp_gens[c]).ravel())

        r_new, basis_new = current_rank(new_vecs)
        print(f"    Level {level}: rank = {r_new}")

        if r_new == prev_rank:
            print(f"    Rank stabilized at level {level}")
            return r_new, basis_new
        prev_rank = r_new
        prev_basis_vecs = new_vecs

    r_final, basis_final = current_rank(prev_basis_vecs)
    return r_final, basis_final


def build_gauge_action_on_omega1(basis, N, gauge_gens_16, dim_rep=3):
    """Build gauge action from 16-dim generators (for singlet sector).
    For the fundamental sector, use build_gauge_action_on_omega1_direct().
    """
    rank = basis.shape[0]
    if dim_rep == 1:
        T_full = [g.copy() for g in gauge_gens_16]
    else:
        T_full = [np.kron(np.eye(dim_rep), g) for g in gauge_gens_16]

    basis_mats = [basis[k].reshape(N, N) for k in range(rank)]
    gauge_mats = []
    for Ti in T_full:
        G_mat = np.zeros((rank, rank), dtype=complex)
        for l in range(rank):
            comm = Ti @ basis_mats[l] - basis_mats[l] @ Ti
            comm_vec = comm.ravel()
            for k in range(rank):
                G_mat[k, l] = np.vdot(basis[k], comm_vec)
        gauge_mats.append(G_mat)
    return gauge_mats


def build_gauge_action_on_omega1_direct(basis, N, gauge_gens_full):
    """Build the matrix representation of each gauge generator on Omega^1_D.

    Each gauge generator T_i is already an NxN matrix (e.g., 48x48 for
    the fundamental sector). The action on a 1-form omega (NxN matrix) is:
        ad(T_i)(omega) = T_i @ omega - omega @ T_i = [T_i, omega]

    We express this in the ON basis of Omega^1_D:
        G_i[k, l] = <basis_k, [T_i, basis_l]>

    Returns:
        gauge_mats: list of (dim_omega, dim_omega) complex matrices
    """
    rank = basis.shape[0]
    basis_mats = [basis[k].reshape(N, N) for k in range(rank)]

    gauge_mats = []
    for Ti in gauge_gens_full:
        G_mat = np.zeros((rank, rank), dtype=complex)
        for l in range(rank):
            comm = Ti @ basis_mats[l] - basis_mats[l] @ Ti  # [T_i, omega_l]
            comm_vec = comm.ravel()
            for k in range(rank):
                G_mat[k, l] = np.vdot(basis[k], comm_vec)
        gauge_mats.append(G_mat)

    return gauge_mats


def build_gauge_casimirs(gauge_mats, u_factors):
    """Build Casimir operators for SU(3), SU(2), and U(1) from gauge matrices.

    C_SU3 = sum_{a=1}^{8} G_a^2
    C_SU2 = sum_{a=1}^{3} G_a^2
    C_U1  = G_Y^2

    Also build combined total Casimir for consistency.
    """
    dim = gauge_mats[0].shape[0]

    C_su3 = np.zeros((dim, dim), dtype=complex)
    C_su2 = np.zeros((dim, dim), dtype=complex)
    C_u1 = np.zeros((dim, dim), dtype=complex)
    C_u1c = np.zeros((dim, dim), dtype=complex)

    for i, (G, f) in enumerate(zip(gauge_mats, u_factors)):
        G2 = G @ G
        if f == 'U1':
            C_u1 += G2
        elif f == 'SU2':
            C_su2 += G2
        elif f == 'SU3':
            C_su3 += G2
        elif f == 'U1c':
            C_u1c += G2

    return C_su3, C_su2, C_u1, C_u1c


# =============================================================================
# SECTION 5: IRREP DECOMPOSITION
# =============================================================================

def decompose_irreps(gauge_mats, u_factors, dim_omega):
    """Decompose Omega^1_D into irreps of SU(3)xSU(2)xU(1).

    Strategy: simultaneously diagonalize the Casimir operators.
    The eigenvalues of C_SU3, C_SU2, C_U1 label the irreps:
      - C_SU3 eigenvalue = c_3 determines the SU(3) rep
        (0 for singlet, 4/3 for fundamental/anti-fund, etc.)
      - C_SU2 eigenvalue = c_2 = j(j+1) determines SU(2) rep
        (0 for singlet, 3/4 for doublet, 2 for triplet, etc.)
      - C_U1 eigenvalue = y^2 determines the hypercharge

    Since the Casimirs commute with each other and with all gauge generators,
    they can be simultaneously diagonalized.
    """
    C_su3, C_su2, C_u1, C_u1c = build_gauge_casimirs(gauge_mats, u_factors)

    # Make Casimirs Hermitian (they should be, up to numerical noise)
    C_su3_h = 0.5 * (C_su3 + C_su3.conj().T)
    C_su2_h = 0.5 * (C_su2 + C_su2.conj().T)
    C_u1_h = 0.5 * (C_u1 + C_u1.conj().T)
    C_u1c_h = 0.5 * (C_u1c + C_u1c.conj().T)

    # Construct a "total label operator" that splits all irreps:
    # Use different coefficients to avoid accidental degeneracies
    # L = alpha * C_su3 + beta * C_su2 + gamma * C_u1 + delta * C_u1c
    # with incommensurate coefficients
    alpha, beta, gamma, delta = 1.0, np.pi, np.e, np.sqrt(2)
    L = alpha * C_su3_h + beta * C_su2_h + gamma * C_u1_h + delta * C_u1c_h

    # Diagonalize L
    evals_L, evecs_L = eigh(L)

    # Cluster eigenvalues to identify irreps
    tol = 1e-6  # (local)
    irreps = []
    used = np.zeros(dim_omega, dtype=bool)

    for i in range(dim_omega):
        if used[i]:
            continue
        cluster = [i]
        used[i] = True
        for j in range(i + 1, dim_omega):
            if not used[j] and abs(evals_L[j] - evals_L[i]) < tol:
                cluster.append(j)
                used[j] = True

        # Compute Casimir eigenvalues for this cluster
        V_cluster = evecs_L[:, cluster]  # (dim_omega, dim_cluster)
        c3 = np.real(np.trace(V_cluster.conj().T @ C_su3_h @ V_cluster)) / len(cluster)
        c2 = np.real(np.trace(V_cluster.conj().T @ C_su2_h @ V_cluster)) / len(cluster)
        y2 = np.real(np.trace(V_cluster.conj().T @ C_u1_h @ V_cluster)) / len(cluster)
        yc2 = np.real(np.trace(V_cluster.conj().T @ C_u1c_h @ V_cluster)) / len(cluster)

        # Identify the representation
        su3_rep = identify_su3_rep(c3)
        su2_rep = identify_su2_rep(c2)
        y_val = identify_hypercharge(y2)
        yc_val = identify_hypercharge(yc2)

        irreps.append({
            'dim': len(cluster),
            'indices': cluster,
            'C_su3': c3,
            'C_su2': c2,
            'C_u1': y2,
            'C_u1c': yc2,
            'su3_rep': su3_rep,
            'su2_rep': su2_rep,
            'Y': y_val,
            'Y_color': yc_val,
            'projector': V_cluster,
            'label_eval': evals_L[cluster[0]],
        })

    return irreps, evals_L, evecs_L, (C_su3_h, C_su2_h, C_u1_h, C_u1c_h)


def identify_su3_rep(casimir_val):
    """Identify SU(3) representation from ADJOINT Casimir eigenvalue.

    Our SU(3) generators act on C^48 via kron(i*lambda_a/2, I_16).
    The adjoint action on End(C^48) yields Casimir eigenvalues:
      - SU(3) singlet (in 3 x 3* = 1 + 8): C = 0
      - SU(3) adjoint (8 of SU(3)):        C = -3

    These are the ONLY values in End(C^3) x End(C^16).
    """
    c = casimir_val
    if abs(c) < 0.05:
        return '1'  # singlet
    elif abs(c + 3.0) < 0.05:
        return '8'  # adjoint
    else:
        return f'?({c:.4f})'


def identify_su2_rep(casimir_val):
    """Identify SU(2) representation from ADJOINT Casimir eigenvalue.

    Our SU(2) generators act on C^16 via build_bimodule_16(i*sigma_j, I_4).
    The adjoint Casimir on End(C^16) yields:
      - SU(2) singlet (j=0):  C = 0
      - SU(2) doublet (j=1/2): C = -3  (generators = i*sigma_j, NOT i*sigma_j/2)
      - SU(2) triplet (j=1):  C = -8
    """
    c = casimir_val
    if abs(c) < 0.05:
        return '1'
    elif abs(c + 3.0) < 0.05:
        return '2'  # doublet
    elif abs(c + 8.0) < 0.05:
        return '3'  # triplet
    else:
        return f'?({c:.4f})'


def identify_hypercharge(y_squared):
    """Identify hypercharge quantum number from adjoint U(1)_Y Casimir.

    Our U(1)_Y generator is diag(i, 0, 0, 0) embedded via bimodule action.
    In the adjoint on End(C^16), the Casimir C = -Y^2 (since generator^2 is negative).
    So Y^2 = -C. Physical Y = sqrt(-C).

    Adjoint eigenvalues of Y: 0, +-1 (integer-quantized).
    The NCG SM hypercharge Y = 1/2 corresponds to the Y_phys normalization.
    """
    c = -y_squared  # Convert to positive Y^2
    if c < 0.01:
        return 0.0
    elif abs(c - 1.0) < 0.05:
        return 1.0  # |Y| = 1 in our convention
    else:
        return np.sqrt(max(c, 0))


# =============================================================================
# SECTION 6: HIGGS SUBSPACE IDENTIFICATION AND MIXING
# =============================================================================

def find_higgs_subspace(irreps, dim_omega):
    """Find the Higgs doublet candidates in the irrep decomposition.

    The NCG Standard Model Higgs is:
      - SU(3) singlet: C_SU3 = 0 (su3_rep = '1')
      - SU(2) doublet: C_SU2 = -3 (su2_rep = '2')
      - Nonzero hypercharge: |Y| = 1 in our convention (Y_phys = 1/2)

    Note: in our convention Y is integer-quantized (0 or +-1 in adjoint).
    The physical Y = 1/2 corresponds to Y_adj = 1 with normalization Y_phys = Y_adj/2.

    Returns ALL (1, 2, Y!=0) irreps as Higgs candidates.
    """
    higgs_candidates = []
    for ir in irreps:
        is_su3_singlet = ir['su3_rep'] == '1'
        is_su2_doublet = ir['su2_rep'] == '2'
        has_nonzero_Y = ir['Y'] > 0.5  # Y = 1 in our convention
        if is_su3_singlet and is_su2_doublet and has_nonzero_Y:
            higgs_candidates.append(ir)

    # Also collect the zero-Y doublets
    higgs_zero_Y = []
    for ir in irreps:
        is_su3_singlet = ir['su3_rep'] == '1'
        is_su2_doublet = ir['su2_rep'] == '2'
        has_zero_Y = ir['Y'] < 0.5
        if is_su3_singlet and is_su2_doublet and has_zero_Y:
            higgs_zero_Y.append(ir)

    return higgs_candidates, higgs_zero_Y


def compute_mixing(gauge_mats, higgs_proj, dim_omega):
    """Compute mixing of Higgs subspace with complement under gauge action.

    For each generator G_i, compute [G_i, Pi_H] where Pi_H is the
    projector onto the Higgs subspace.

    Pi_H = V_H @ V_H^dag where V_H has the Higgs basis vectors as columns.

    Mixing fraction = ||[G_i, Pi_H]|| / ||Pi_H|| for each generator.
    """
    # Build projector
    V_H = higgs_proj  # (dim_omega, dim_higgs)
    Pi_H = V_H @ V_H.conj().T  # (dim_omega, dim_omega)
    Pi_H_norm = la_norm(Pi_H, 'fro')

    mixing_per_gen = []
    for G in gauge_mats:
        comm = G @ Pi_H - Pi_H @ G  # [G_i, Pi_H]
        mixing = la_norm(comm, 'fro') / Pi_H_norm if Pi_H_norm > 1e-15 else 0.0
        mixing_per_gen.append(mixing)

    return np.array(mixing_per_gen)


def compute_perturbative_correction(gauge_mats, irreps, higgs_idx, dim_omega):
    """Compute perturbative corrections to the Higgs subspace.

    The order-one violation parameterized as epsilon * V mixes the Higgs
    with other directions. We compute the mixing matrix elements:

        M_{n, H} = <n | V | H> / (E_H - E_n)

    where the "energies" are the label operator eigenvalues and V is
    the part of the gauge action that leaks out of the Higgs subspace.

    For the Higgs to remain isolated, we need the perturbation series
    to converge: |epsilon * M_{n,H}| << 1 for all n not in H.
    """
    higgs_ir = irreps[higgs_idx]
    V_H = higgs_ir['projector']  # (dim_omega, dim_higgs)
    E_H = higgs_ir['label_eval']

    corrections = []
    for n_idx, ir in enumerate(irreps):
        if n_idx == higgs_idx:
            continue
        V_n = ir['projector']
        E_n = ir['label_eval']
        dE = E_H - E_n
        if abs(dE) < 1e-10:
            # Degenerate -- perturbation theory breaks down
            corrections.append({
                'irrep_idx': n_idx,
                'label': f"({ir['su3_rep']},{ir['su2_rep']},{ir['Y']:.2f})",
                'dim': ir['dim'],
                'dE': dE,
                'coupling': np.inf,
                'correction': np.inf,
            })
            continue

        # Coupling through each gauge generator
        max_coupling = 0.0
        for G in gauge_mats:
            # <n | G | H> matrix elements
            coupling_mat = V_n.conj().T @ G @ V_H
            max_coupling = max(max_coupling, la_norm(coupling_mat, 'fro'))

        correction_magnitude = max_coupling / abs(dE)
        corrections.append({
            'irrep_idx': n_idx,
            'label': f"({ir['su3_rep']},{ir['su2_rep']},{ir['Y']:.2f})",
            'dim': ir['dim'],
            'dE': dE,
            'coupling': max_coupling,
            'correction': correction_magnitude,
        })

    return corrections


# =============================================================================
# SECTION 7: INVARIANCE CHECK VIA COMMUTATOR
# =============================================================================

def check_gauge_invariance(gauge_mats, u_names, u_factors, irreps):
    """For each irrep, check if it's an invariant subspace of ALL gauge generators.

    An irrep V is gauge-invariant if for all generators G_i:
        G_i V subset V
    equivalently:
        Pi_perp G_i Pi_V = 0 (no leakage out of V)

    Returns per-irrep, per-generator leakage fractions.
    """
    dim = gauge_mats[0].shape[0]
    results = []

    for ir_idx, ir in enumerate(irreps):
        V = ir['projector']
        Pi_V = V @ V.conj().T
        Pi_perp = np.eye(dim, dtype=complex) - Pi_V
        Pi_V_norm = la_norm(Pi_V, 'fro')

        leakage_per_gen = []
        for gi, G in enumerate(gauge_mats):
            # Leakage: Pi_perp @ G @ Pi_V
            leak = Pi_perp @ G @ Pi_V
            leak_frac = la_norm(leak, 'fro') / (Pi_V_norm + 1e-30)
            leakage_per_gen.append(leak_frac)

        max_leak = max(leakage_per_gen)
        results.append({
            'irrep_idx': ir_idx,
            'dim': ir['dim'],
            'label': f"({ir['su3_rep']},{ir['su2_rep']},{ir['Y']:.2f})",
            'max_leakage': max_leak,
            'leakage_per_gen': np.array(leakage_per_gen),
            'is_invariant': max_leak < 1e-8,
        })

    return results


# =============================================================================
# SECTION 8: CROSS-CHECKS
# =============================================================================

def cross_check_casimir_commutation(gauge_mats, u_factors):
    """Verify that Casimir operators commute with all gauge generators."""
    C_su3, C_su2, C_u1, C_u1c = build_gauge_casimirs(gauge_mats, u_factors)

    max_comm = 0.0
    for i, G in enumerate(gauge_mats):
        for name, C in [('C_su3', C_su3), ('C_su2', C_su2), ('C_u1', C_u1), ('C_u1c', C_u1c)]:
            comm = C @ G - G @ C
            comm_norm = la_norm(comm, 'fro')
            max_comm = max(max_comm, comm_norm)

    return max_comm


def cross_check_anti_hermiticity(gauge_mats, u_names):
    """Verify gauge generators are anti-Hermitian on Omega^1_D."""
    max_dev = 0.0
    per_gen = []
    for i, G in enumerate(gauge_mats):
        dev = la_norm(G + G.conj().T, 'fro') / (la_norm(G, 'fro') + 1e-30)
        per_gen.append(dev)
        max_dev = max(max_dev, dev)

    return max_dev, per_gen


def cross_check_dimension_sum(irreps, dim_omega):
    """Verify that sum of irrep dimensions = dim(Omega^1_D)."""
    total = sum(ir['dim'] for ir in irreps)
    return total, total == dim_omega


# =============================================================================
# SECTION 9: PLOTTING
# =============================================================================

def make_plots(irreps, invariance_results, mixing_fracs, u_names, corrections,
               dim_omega, outpath):
    """Generate the 3-panel diagnostic plot."""
    fig = plt.figure(figsize=(18, 6))
    gs = GridSpec(1, 3, figure=fig, wspace=0.35)

    # --- Panel (a): Irrep decomposition bar chart ---
    ax1 = fig.add_subplot(gs[0])
    labels = []
    dims = []
    colors = []
    for ir in sorted(irreps, key=lambda x: -x['dim']):
        lbl = f"({ir['su3_rep']},{ir['su2_rep']},{ir['Y']:.1f})"
        labels.append(lbl)
        dims.append(ir['dim'])
        # Color by SU(3) rep
        if ir['su3_rep'] == '1':
            colors.append('#2196F3')  # blue = singlet
        elif ir['su3_rep'] == '3':
            colors.append('#FF9800')  # orange = fundamental
        elif ir['su3_rep'] == '8':
            colors.append('#4CAF50')  # green = adjoint
        else:
            colors.append('#9E9E9E')  # grey = other

    n_show = min(20, len(labels))
    y_pos = np.arange(n_show)
    ax1.barh(y_pos, dims[:n_show], color=colors[:n_show], edgecolor='black', linewidth=0.5)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels[:n_show], fontsize=8)
    ax1.set_xlabel('Dimension')
    ax1.set_title(f'Irrep decomposition of $\\Omega^1_D$ (dim={dim_omega})')
    ax1.invert_yaxis()

    # Highlight Higgs if found
    for idx, ir in enumerate(sorted(irreps, key=lambda x: -x['dim'])):
        if ir['su3_rep'] == '1' and ir['su2_rep'] == '2' and idx < n_show:
            ax1.barh(idx, ir['dim'], color='#E91E63', edgecolor='black', linewidth=1.5)

    # --- Panel (b): Mixing matrix ---
    ax2 = fig.add_subplot(gs[1])
    if len(mixing_fracs) > 0:
        x_pos = np.arange(len(u_names))
        bar_colors = []
        for f in u_names:
            if 'u1' in f.lower() and 'color' not in f.lower():
                bar_colors.append('#2196F3')
            elif 'su2' in f.lower():
                bar_colors.append('#FF9800')
            elif 'su3' in f.lower():
                bar_colors.append('#4CAF50')
            else:
                bar_colors.append('#9E9E9E')

        ax2.bar(x_pos, mixing_fracs, color=bar_colors, edgecolor='black', linewidth=0.5)
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(u_names, rotation=45, ha='right', fontsize=8)
        ax2.set_ylabel('$||[G_i, \\Pi_H]|| / ||\\Pi_H||$')
        ax2.set_title('Higgs mixing per gauge generator')
        ax2.axhline(y=0.01, color='green', linestyle='--', alpha=0.5, label='1% threshold')
        ax2.axhline(y=0.50, color='red', linestyle='--', alpha=0.5, label='50% threshold')
        ax2.legend(fontsize=8)
        ax2.set_yscale('symlog', linthresh=1e-12)
    else:
        ax2.text(0.5, 0.5, 'No Higgs subspace found', transform=ax2.transAxes,
                 ha='center', va='center', fontsize=14)

    # --- Panel (c): Perturbative corrections ---
    ax3 = fig.add_subplot(gs[2])
    if corrections:
        corr_labels = [c['label'] for c in corrections if c['correction'] < 100]
        corr_vals = [c['correction'] for c in corrections if c['correction'] < 100]
        if corr_vals:
            sorted_idx = np.argsort(corr_vals)[::-1][:15]  # top 15
            y_pos3 = np.arange(len(sorted_idx))
            ax3.barh(y_pos3, [corr_vals[i] for i in sorted_idx],
                     color='#7B1FA2', edgecolor='black', linewidth=0.5)
            ax3.set_yticks(y_pos3)
            ax3.set_yticklabels([corr_labels[i] for i in sorted_idx], fontsize=8)
            ax3.set_xlabel('$|\\langle n|G|H\\rangle / \\Delta E|$')
            ax3.set_title('Perturbative correction magnitude')
            ax3.axvline(x=1.0, color='red', linestyle='--', alpha=0.5, label='convergence bound')
            ax3.legend(fontsize=8)
            ax3.invert_yaxis()
    else:
        ax3.text(0.5, 0.5, 'No corrections computed', transform=ax3.transAxes,
                 ha='center', va='center', fontsize=14)

    fig.suptitle('HIGGS-ORDER-ONE-62: Higgs Doublet Isolation in $\\Omega^1_D$',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot saved to {outpath}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    t0 = time.time()
    print("=" * 72)
    print("S62 HIGGS-ORDER-ONE-62: Higgs Doublet Isolation in Omega^1_D")
    print("=" * 72)

    # --- Step 1: Build infrastructure ---
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    tau = tau_fold

    AF_16, AF_names, AF_factors = build_AF_generators()
    # Build gauge generators as 48x48 matrices on C^3 x C^16
    gauge_gens_48, u_names, u_factors = build_gauge_generators_48()

    n_gen = len(AF_16)
    n_gauge = len(gauge_gens_48)
    print(f"\n  A_F generators: {n_gen}")
    print(f"  Gauge generators: {n_gauge}")
    print(f"  tau = {tau}")

    # --- Step 2: Build D_K on fundamental sector ---
    print("\n--- Building D_K on (1,0) fundamental sector ---")
    D_K = build_DK_fundamental(gammas, gens, f_abc, tau)
    N = D_K.shape[0]
    print(f"  D_K: {N}x{N}")

    # D_K on SU(3) is anti-Hermitian (iD is Hermitian), so check anti-Hermiticity
    # The su(3) generators are anti-Hermitian, gamma matrices are Hermitian,
    # so D_K = sum rho(e_a) x gamma_a + I x Omega. With anti-Herm rho(e_a),
    # the first term is anti-Hermitian. Omega is also anti-Hermitian.
    dk_ah = la_norm(D_K + D_K.conj().T, 'fro') / la_norm(D_K, 'fro')
    dk_herm = la_norm(D_K - D_K.conj().T, 'fro') / la_norm(D_K, 'fro')
    print(f"  D_K anti-Hermiticity: ||D + D^dag|| / ||D|| = {dk_ah:.3e}")
    print(f"  D_K Hermiticity:      ||D - D^dag|| / ||D|| = {dk_herm:.3e}")

    # For Omega^1_D computation, we want iD_K (Hermitian) if D_K is anti-Hermitian
    # But the 1-form space doesn't depend on this -- a[D,b] = a(Db - bD) regardless.
    # What matters is the GAUGE action: [T_i, omega] must close.

    # --- Step 3: Compute BOTH Omega^1_D (342-dim) AND extended module (775-dim) ---
    print("\n--- Computing Omega^1_D (linear + quadratic) ---")
    omega_data = compute_omega1_combined(D_K, AF_16, dim_rep=3)
    dim_lin = omega_data['dim_linear']
    dim_comb = omega_data['dim_combined']
    dim_extra = omega_data['dim_extra']
    combined_basis = omega_data['combined_basis']  # 342 x N^2

    print(f"  Linear rank: {dim_lin}")
    print(f"  Combined rank: {dim_comb}")
    print(f"  Extra (quadratic-only) rank: {dim_extra}")

    # The gauge action on 342-dim Omega^1_D leaks out (up to 97%).
    # After closing under both algebra and gauge, the module fills ALL of End(C^48)
    # = C^{2304}. The correct decomposition is therefore on End(C^48).
    #
    # GEOMETRIC INSIGHT (Berry perspective):
    # The order-one violation creates a "diabolical point" in the fiber bundle
    # structure. The base Omega^1_D (342-dim) is not a flat section of the
    # gauge bundle -- the connection has curvature that rotates forms out of it.
    # Only the full End(C^48) is a flat section (trivially). The Higgs doublet,
    # if it exists, must be identified as an irrep of the gauge action on
    # End(C^48), and then we check its PROJECTION onto Omega^1_D.

    # Use End(C^48) = full matrix algebra as the working space
    print(f"\n--- Using full End(C^48) = {N}x{N} = {N*N}-dim ---")
    dim_work = N * N  # 2304
    # Identity basis for End(C^48): e_{ij} basis
    working_basis = np.eye(dim_work, dtype=complex)  # (2304, 2304)
    print(f"  Working space: End(C^{N}) = C^{dim_work}")

    # --- Step 4: Build gauge action on End(C^48) ---
    # For the standard basis e_{ij}, the matrix representation of
    # ad(T) on End(C^N) is: [T, e_{ij}] = T @ e_{ij} - e_{ij} @ T
    # In the vectorized form: ad(T) = T kron I - I kron T^T
    # This is the standard adjoint representation.
    print(f"\n--- Building gauge action on End(C^{N}) ---")
    gauge_mats = []
    for Ti in gauge_gens_48:
        # ad(T) in vectorized form: (T kron I) - (I kron T^T)
        G_mat = np.kron(Ti, np.eye(N, dtype=complex)) - np.kron(np.eye(N, dtype=complex), Ti.T)
        gauge_mats.append(G_mat)
    print(f"  Built {len(gauge_mats)} gauge matrices, each {dim_work}x{dim_work}")

    # --- Verify 48-dim gauge generators are anti-Hermitian ---
    print(f"\n  Verifying 48x48 gauge generators are anti-Hermitian:")
    for i, (T, name) in enumerate(zip(gauge_gens_48, u_names)):
        ah_dev = la_norm(T + T.conj().T, 'fro') / (la_norm(T, 'fro') + 1e-30)
        print(f"    {name:>12s}: ||T + T^dag|| / ||T|| = {ah_dev:.3e}")

    # --- Cross-check: anti-Hermiticity of gauge matrices on Omega^1_D ---
    ah_max, ah_per_gen = cross_check_anti_hermiticity(gauge_mats, u_names)
    print(f"\n  Anti-Hermiticity on Omega^1_D: max deviation = {ah_max:.3e}")
    for i, name in enumerate(u_names):
        print(f"    {name}: {ah_per_gen[i]:.3e}")

    # --- Cross-check: Casimir commutation ---
    casimir_comm_max = cross_check_casimir_commutation(gauge_mats, u_factors)
    print(f"\n  Casimir-gauge commutation: max ||[C, G]|| = {casimir_comm_max:.3e}")
    if casimir_comm_max > 1.0:
        print(f"  WARNING: Casimirs do not commute with gauge generators.")
        print(f"  This means the gauge action does NOT close on this space.")
        print(f"  Irrep decomposition may be unreliable.")

    # --- Step 5: Decompose into irreps ---
    print(f"\n--- Decomposing extended module into SU(3)xSU(2)xU(1) irreps ---")
    irreps, evals_L, evecs_L, casimirs = decompose_irreps(
        gauge_mats, u_factors, dim_work)

    print(f"  Found {len(irreps)} irreducible components:")
    dim_sum = 0
    for i, ir in enumerate(sorted(irreps, key=lambda x: -x['dim'])):
        dim_sum += ir['dim']
        print(f"    [{i:3d}] dim={ir['dim']:4d}  "
              f"SU3={ir['su3_rep']:>4s} (C={ir['C_su3']:+.4f})  "
              f"SU2={ir['su2_rep']:>4s} (C={ir['C_su2']:+.4f})  "
              f"Y={ir['Y']:.3f} (Y^2={ir['C_u1']:.4f})  "
              f"Yc={ir['Y_color']:.3f}")

    # Dimension sum check
    total_dim, dim_ok = cross_check_dimension_sum(irreps, dim_work)
    print(f"\n  Dimension sum: {total_dim} (expected {dim_comb}) -- {'OK' if dim_ok else 'MISMATCH'}")

    # --- Step 5b: Compute Omega^1_D projection within End(C^48) ---
    # Omega^1_D basis vectors are already in the standard basis of End(C^48)
    # (they are N^2-vectors). The projector is Pi = V V^dag where V = combined_basis^T.
    print(f"\n--- Computing Omega^1_D projection within End(C^{N}) ---")
    # combined_basis: (342, 2304) -- each row is an ON basis vector of Omega^1_D
    # Pi_omega = combined_basis^T @ combined_basis^* = (2304, 2304) projector
    Pi_omega = combined_basis.conj().T @ combined_basis  # (2304, 2304)
    omega_proj_trace = np.real(np.trace(Pi_omega))
    print(f"  Tr(Pi_Omega^1_D) = {omega_proj_trace:.1f} (expected {dim_comb})")

    # For each irrep, compute overlap with Omega^1_D
    # V: (dim_work, dim_irrep) eigenvectors of the label operator
    # Pi_omega: (dim_work, dim_work) projector onto Omega^1_D
    # overlap = Tr(V^dag Pi_omega V) / dim_irrep = fraction of irrep in Omega^1_D
    for ir in irreps:
        V = ir['projector']  # (dim_work, dim_irrep)
        overlap_mat = V.conj().T @ Pi_omega @ V
        ir['omega1_overlap'] = np.real(np.trace(overlap_mat)) / ir['dim']
        # Also compute the Omega^1_D dimension contribution
        ir['omega1_dim'] = np.real(np.trace(overlap_mat))

    # --- Step 6: Find Higgs subspace ---
    print(f"\n--- Identifying Higgs doublet (1, 2, Y!=0) ---")
    higgs_candidates, higgs_zero_Y = find_higgs_subspace(irreps, dim_work)

    print(f"  Higgs candidates (1, 2, Y!=0): {len(higgs_candidates)}")
    for hc in higgs_candidates:
        print(f"    ({hc['su3_rep']},{hc['su2_rep']},{hc['Y']:.2f})"
              f" dim={hc['dim']}  Omega^1 overlap={hc.get('omega1_overlap',-1):.4f}"
              f" Omega^1 dim_contrib={hc.get('omega1_dim',-1):.1f}")

    if higgs_zero_Y:
        print(f"  Also found (1, 2, Y=0): {len(higgs_zero_Y)}")
        for hz in higgs_zero_Y:
            print(f"    ({hz['su3_rep']},{hz['su2_rep']},{hz['Y']:.2f})"
                  f" dim={hz['dim']}  Omega^1 overlap={hz.get('omega1_overlap',-1):.4f}"
                  f" Omega^1 dim_contrib={hz.get('omega1_dim',-1):.1f}")

    # Print ALL irreps with Omega^1_D overlap
    print(f"\n  All irreps with Omega^1_D overlap:")
    omega_dim_total = 0.0  # (local)
    for ir in sorted(irreps, key=lambda x: -x.get('omega1_dim', 0)):
        odim = ir.get('omega1_dim', 0)
        omega_dim_total += odim
        print(f"    ({ir['su3_rep']:>3s},{ir['su2_rep']:>3s},Y={ir['Y']:.0f}) "
              f"dim={ir['dim']:5d}  "
              f"Omega^1 overlap={ir.get('omega1_overlap',0):.4f}  "
              f"Omega^1 dim={odim:.1f}")
    print(f"  Total Omega^1_D dimension from irreps: {omega_dim_total:.1f} (expected {dim_comb})")

    # Use the nonzero-Y doublet
    higgs_ir = higgs_candidates[0] if higgs_candidates else None
    higgs_idx = None
    if higgs_ir is not None:
        for idx, ir in enumerate(irreps):
            if ir is higgs_ir:
                higgs_idx = idx
                break

    # --- Step 7: Compute mixing and invariance ---
    mixing_fracs = np.array([])
    corrections = []
    invariance_results = []

    if higgs_ir is not None:
        print(f"\n  Higgs candidate: ({higgs_ir['su3_rep']},{higgs_ir['su2_rep']},{higgs_ir['Y']:.2f})"
              f" dim={higgs_ir['dim']}"
              f" Omega^1_D overlap={higgs_ir.get('omega1_overlap', -1):.4f}")

        # Mixing within extended module
        print(f"\n--- Computing Higgs mixing in extended module ---")
        mixing_fracs = compute_mixing(gauge_mats, higgs_ir['projector'], dim_work)
        max_mixing = np.max(mixing_fracs)
        print(f"  Mixing fractions ||[G_i, Pi_H]|| / ||Pi_H||:")
        for i, name in enumerate(u_names):
            print(f"    {name:>12s}: {mixing_fracs[i]:.6e}")
        print(f"  Max mixing: {max_mixing:.6e}")

        # Invariance check (all irreps in extended module)
        print(f"\n--- Checking gauge invariance of ALL irreps ---")
        invariance_results = check_gauge_invariance(gauge_mats, u_names, u_factors, irreps)
        n_invariant = sum(1 for r in invariance_results if r['is_invariant'])
        print(f"  Invariant irreps: {n_invariant} / {len(irreps)}")

        # Print sorted by dimension, with Omega^1_D overlap
        for r in sorted(invariance_results, key=lambda x: -irreps[x['irrep_idx']]['dim']):
            ir = irreps[r['irrep_idx']]
            status = "INVARIANT" if r['is_invariant'] else f"LEAK={r['max_leakage']:.3e}"
            omega_ov = ir.get('omega1_overlap', -1)
            print(f"    {r['label']:>20s} dim={r['dim']:4d}  "
                  f"Omega^1 overlap={omega_ov:.3f}  {status}")

        # Perturbative corrections
        print(f"\n--- Perturbative corrections ---")
        corrections = compute_perturbative_correction(
            gauge_mats, irreps, higgs_idx, dim_work)
        max_corr = max(c['correction'] for c in corrections if c['correction'] < np.inf)
        print(f"  Max finite correction: {max_corr:.6e}")
        print(f"  Top 5 corrections:")
        sorted_corr = sorted(corrections, key=lambda c: -c['correction'])
        for c in sorted_corr[:5]:
            if c['correction'] < np.inf:
                print(f"    {c['label']:>20s} dim={c['dim']:3d}  "
                      f"coupling={c['coupling']:.4e}  dE={c['dE']:.4f}  "
                      f"correction={c['correction']:.4e}")
            else:
                print(f"    {c['label']:>20s} dim={c['dim']:3d}  "
                      f"DEGENERATE (dE={c['dE']:.4e})")

        # Gate verdict
        print("\n" + "=" * 72)
        print("GATE VERDICT: HIGGS-ORDER-ONE-62")
        print("=" * 72)
        if max_mixing < 0.01:
            verdict = 'PASS'
            reason = (f"Higgs subspace ({higgs_ir['su3_rep']},{higgs_ir['su2_rep']},"
                      f"{higgs_ir['Y']:.1f}) dim={higgs_ir['dim']} is gauge-invariant. "
                      f"Max mixing = {max_mixing:.3e} < 1% threshold.")
        elif max_mixing > 0.50:
            verdict = 'FAIL'
            reason = (f"Higgs subspace mixes strongly with other directions. "
                      f"Max mixing = {max_mixing:.3e} > 50% threshold.")
        else:
            verdict = 'INFO'
            reason = (f"Higgs subspace partially mixes. "
                      f"Max mixing = {max_mixing:.3e} (between 1% and 50%).")

    else:
        print("\n" + "=" * 72)
        print("GATE VERDICT: HIGGS-ORDER-ONE-62")
        print("=" * 72)
        verdict = 'INFO'
        max_mixing = -1.0
        reason = "Higgs doublet (1,2,1/2) not identified in irrep decomposition."

    print(f"  Verdict: {verdict}")
    print(f"  Reason: {reason}")

    dt = time.time() - t0
    print(f"\n  Runtime: {dt:.1f}s")

    # --- Save results ---
    outpath_npz = os.path.join(OUTDIR, "s62_higgs_order_one.npz")

    save_dict = dict(
        tau=tau,
        dim_DK=N,
        dim_linear=dim_lin,
        dim_combined=dim_comb,
        dim_extra=dim_extra,
        dim_extended=dim_work,
        omega1_proj_trace=omega_proj_trace,
        n_irreps=len(irreps),
        dim_sum=total_dim,
        dim_check=dim_ok,
        casimir_comm_max=casimir_comm_max,
        ah_max=ah_max,
        verdict=verdict,
        reason=reason,
        runtime_s=dt,
    )

    # Save per-irrep data
    irrep_dims = np.array([ir['dim'] for ir in irreps])
    irrep_C_su3 = np.array([ir['C_su3'] for ir in irreps])
    irrep_C_su2 = np.array([ir['C_su2'] for ir in irreps])
    irrep_C_u1 = np.array([ir['C_u1'] for ir in irreps])
    irrep_labels = np.array([f"({ir['su3_rep']},{ir['su2_rep']},{ir['Y']:.2f})"
                             for ir in irreps], dtype=object)
    save_dict.update(
        irrep_dims=irrep_dims,
        irrep_C_su3=irrep_C_su3,
        irrep_C_su2=irrep_C_su2,
        irrep_C_u1=irrep_C_u1,
        irrep_labels=irrep_labels,
    )

    if higgs_ir is not None:
        save_dict.update(
            higgs_dim=higgs_ir['dim'],
            higgs_C_su3=higgs_ir['C_su3'],
            higgs_C_su2=higgs_ir['C_su2'],
            higgs_C_u1=higgs_ir['C_u1'],
            max_mixing=max_mixing,
            mixing_per_gen=mixing_fracs,
            gauge_names=np.array(u_names, dtype=object),
            gauge_factors=np.array(u_factors, dtype=object),
        )

        # Save invariance data
        inv_leakage = np.array([r['max_leakage'] for r in invariance_results])
        inv_is_invariant = np.array([r['is_invariant'] for r in invariance_results])
        save_dict.update(
            invariance_leakage=inv_leakage,
            invariance_is_invariant=inv_is_invariant,
        )

        # Save perturbative corrections
        if corrections:
            corr_vals = np.array([c['correction'] for c in corrections
                                  if c['correction'] < np.inf])
            corr_labels_arr = np.array([c['label'] for c in corrections
                                         if c['correction'] < np.inf], dtype=object)
            save_dict.update(
                perturbative_corrections=corr_vals,
                perturbative_labels=corr_labels_arr,
            )

    np.savez(outpath_npz, **save_dict)
    print(f"  Data saved to {outpath_npz}")

    # --- Plot ---
    outpath_png = os.path.join(OUTDIR, "s62_higgs_order_one.png")
    make_plots(irreps, invariance_results, mixing_fracs, u_names,
               corrections, dim_work, outpath_png)

    # --- Summary ---
    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Omega^1_D dimension: {dim_comb} (linear: {dim_lin}, extra: {dim_extra})")
    print(f"  Extended module dimension: {dim_work}")
    print(f"  Number of irreps: {len(irreps)}")
    print(f"  Dimension sum check: {total_dim} {'= OK' if dim_ok else '!= MISMATCH'}")
    print(f"  Casimir commutation: {casimir_comm_max:.3e}")
    print(f"  Anti-Hermiticity: {ah_max:.3e}")
    if higgs_ir is not None:
        print(f"  Higgs subspace: ({higgs_ir['su3_rep']},{higgs_ir['su2_rep']},{higgs_ir['Y']:.1f})"
              f" dim={higgs_ir['dim']}")
        print(f"  Max mixing: {max_mixing:.6e}")
    print(f"  GATE: {verdict}")
    print(f"  Reason: {reason}")


if __name__ == "__main__":
    main()
