"""
WEAK-ORDER-ONE-45: Test the Bochniak-Sitarz Weak Order-One Condition
=====================================================================

Tests whether the framework's spectral triple (A_F, H_F, D_K) satisfies the
WEAK order-one condition from Bochniak-Sitarz (2021), Paper 25.

MATHEMATICAL FRAMEWORK
-----------------------

The FULL order-one condition requires:
    [[D, a], b^0] = 0   for ALL a, b in A_F

This FAILS at norm 4.000 for the (H,H) factor pair (Sessions 9-10, 22c, 28b-c).

The WEAK order-one condition (Bochniak-Sitarz) relaxes this to:
    [[D, g], h^0] = 0   for g, h in A_gauge (gauge subalgebra)

while allowing:
    [[D, s], t^0] != 0   for s, t involving the scalar sector

The key insight: not all elements of A_F produce gauge bosons. The decomposition
A_F = A_gauge + A_scalar separates generators whose commutators [D,a] produce
gauge connections (M_4 fluctuations) from those producing Higgs-like scalars
(F fluctuations).

For A_F = C + H + M_3(C):
  - Gauge generators: su(2)_L (from H) and su(3)_C (from M_3)
  - Scalar generators: the COMPLEMENT --- C projectors, H_1 (identity in H),
    M_3 diagonal, and any off-diagonal mixing C and H

The weak condition tests whether gauge-gauge double commutators vanish:
    [[D_K, su(2)_L], su(3)_C^0] = 0?
    [[D_K, su(2)_L], su(2)_L^0] = 0?
    [[D_K, su(3)_C], su(3)_C^0] = 0?

TESTS PERFORMED
----------------
1. Full order-one violation: all (a,b) pairs at fold tau=0.20 (reproduces S28b)
2. Gauge-gauge block: su(2)_L x su(2)_L, su(3) x su(3), su(2)_L x su(3)
3. Gauge-scalar and scalar-scalar blocks: quantify violation magnitude
4. Inner fluctuation module Omega^1_D(A_F): dimension count with/without order-one
5. Weak order-one ratio: ||gauge-gauge|| / ||full|| as measure of "how weak"
6. Tau dependence: test at multiple tau to check stability of classification

GATE: WEAK-ORDER-ONE-45
  INFO: Structural condition on the spectral triple
  Key metric: Does the gauge-gauge sector close?

Author: Connes-NCG-Theorist (Session 45)
Date: 2026-03-15
Depends on: s28b_order_one.py (A_F infrastructure), tier1_dirac_spectrum.py
"""

import numpy as np
from numpy.linalg import norm as la_norm
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

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
# SECTION 1: A_F ALGEBRA INFRASTRUCTURE (from s28b_order_one.py)
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


def build_bimodule_16(L4: np.ndarray, R4: np.ndarray) -> np.ndarray:
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

def get_column_index(flat_idx_val: int) -> int:
    if flat_idx_val == 0: return 0
    elif 1 <= flat_idx_val <= 3: return flat_idx_val
    elif 4 <= flat_idx_val <= 6: return 0
    else: return (flat_idx_val - 7) % 3 + 1

G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

gamma_F_mat = np.zeros((32, 32))
gamma_F_mat[:16, :16] = np.eye(16)
gamma_F_mat[16:, 16:] = -np.eye(16)


def rho_minus(rho_plus_v: np.ndarray) -> np.ndarray:
    return G5 @ np.conj(rho_plus_v) @ G5


def full_32(gen_16: np.ndarray) -> np.ndarray:
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32


def o_map(gen_32: np.ndarray) -> np.ndarray:
    """Opposite algebra: o(b) = J pi(b*) J^{-1} = Xi @ gen_32^T @ Xi."""
    return Xi @ gen_32.T @ Xi


def o_map_16(gen_16: np.ndarray) -> np.ndarray:
    """Opposite algebra restricted to Psi_+ (16-dim)."""
    return G5 @ gen_16.T @ G5


def embed_spinor_op_32(M_16: np.ndarray) -> np.ndarray:
    M_32 = np.zeros((32, 32), dtype=complex)
    M_32[:16, :16] = M_16
    M_32[16:, 16:] = rho_minus(M_16)
    return M_32


# =============================================================================
# SECTION 2: BUILD A_F GENERATORS WITH GAUGE/SCALAR CLASSIFICATION
# =============================================================================

def build_AF_generators_classified():
    """
    Build all generators of A_F = C + H + M_3(C) and classify each as
    gauge or scalar following the Bochniak-Sitarz decomposition.

    GAUGE generators:
      - su(2)_L: from H factor, traceless anti-Hermitian part = {H_i, H_j, H_k}
        These are i*sigma_1, i*sigma_2, i*sigma_3 on the (2,3) subspace of M_4.
      - u(1)_Y: from C factor, the hypercharge generator
        This is the traceless part of the C embedding = C_Im
      - su(3)_C: from M_3(C) factor, the 8 Gell-Mann generators (traceless anti-Hermitian)
        These are i*lambda_a/2 acting on the color (1,2,3) subspace.
        In our basis: all traceless combinations of M3_E{ab}_{Re/Im}.

    SCALAR generators:
      - C_proj: the projector onto the lepton singlet (not a gauge transformation)
      - H_1: the identity in H (scales, not a gauge rotation)
      - M3 diagonal trace: proportional to identity on color space
      - Any other elements of the center of A_F

    For the Bochniak-Sitarz test, the critical question is whether
    gauge-gauge double commutators vanish.

    Returns:
        AF_16: list of (16,16) complex matrices
        AF_32: list of (32,32) complex matrices
        AF_names: list of names
        AF_factors: list of algebra factor labels
        AF_class: list of 'gauge' or 'scalar' classifications
        gauge_indices: list of indices classified as gauge
        scalar_indices: list of indices classified as scalar
    """
    AF_16 = []
    AF_names = []
    AF_factors = []
    AF_class = []

    # ---- C factor ----
    # C_Im: hypercharge generator u(1)_Y -- GAUGE
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    AF_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    AF_names.append('C_Im')
    AF_factors.append('C')
    AF_class.append('gauge')  # u(1)_Y

    # C_proj: projector onto nu_R -- SCALAR (not unitary, not anti-Hermitian)
    L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
    AF_16.append(build_bimodule_16(L_CRe, np.eye(4)))
    AF_names.append('C_proj')
    AF_factors.append('C')
    AF_class.append('scalar')  # projector, not gauge

    # ---- H factor ----
    # H_i, H_j, H_k: su(2)_L generators -- GAUGE
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    AF_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    AF_names.append('H_i')
    AF_factors.append('H')
    AF_class.append('gauge')  # su(2)_L

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
    AF_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    AF_names.append('H_j')
    AF_factors.append('H')
    AF_class.append('gauge')  # su(2)_L

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
    AF_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    AF_names.append('H_k')
    AF_factors.append('H')
    AF_class.append('gauge')  # su(2)_L

    # H_1: identity in H -- SCALAR (center element, not a gauge generator)
    AF_16.append(build_bimodule_16(np.eye(4), np.eye(4)))
    AF_names.append('H_1')
    AF_factors.append('H')
    AF_class.append('scalar')  # identity, generates scalars

    # ---- M_3(C) factor ----
    # 8 Gell-Mann generators (traceless anti-Hermitian) -- GAUGE
    # 1 trace generator (proportional to identity) -- SCALAR
    # We build all 18 (Re/Im of each E_{ab}) then classify
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

                # Classify: off-diagonal and traceless diagonal are gauge
                # The trace part (sum of diag Re) is scalar
                if a != b:
                    AF_class.append('gauge')  # off-diagonal = su(3)
                elif part == 'Im':
                    AF_class.append('gauge')  # diagonal Im = su(3) Cartan
                else:
                    # Diagonal Re: need to distinguish traceless from trace
                    # E00_Re, E11_Re, E22_Re form a 3D space
                    # Traceless = 2D (gauge), trace = 1D (scalar)
                    # We'll handle this as: individual diag Re are MIXED,
                    # but we'll test them individually anyway
                    AF_class.append('mixed_diag')

    # Lift to 32-dim
    AF_32 = [full_32(g) for g in AF_16]

    # Build refined gauge/scalar index lists
    gauge_indices = [i for i, c in enumerate(AF_class) if c == 'gauge']
    scalar_indices = [i for i, c in enumerate(AF_class) if c in ('scalar', 'mixed_diag')]

    return AF_16, AF_32, AF_names, AF_factors, AF_class, gauge_indices, scalar_indices


def build_su3_gellmann_generators_on_AF():
    """
    Build the 8 Gell-Mann generators of su(3) as anti-Hermitian matrices
    on A_F's M_3(C) factor, properly embedded in the 16-dim Psi_+ space.

    These are the PURE GAUGE generators of the color sector.

    Returns:
        gm_16: list of 8 (16,16) complex matrices
        gm_names: list of names
    """
    gm_16 = []
    gm_names = []

    # Gell-Mann matrices lambda_1 through lambda_8 (Hermitian)
    # We use i*lambda_a as anti-Hermitian generators of su(3)

    # lambda_1 = [[0,1,0],[1,0,0],[0,0,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[0, 1] = 1j; m[1, 0] = 1j  # i*lambda_1
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_1')

    # lambda_2 = [[0,-i,0],[i,0,0],[0,0,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[0, 1] = 1.0; m[1, 0] = -1.0  # i*lambda_2
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_2')

    # lambda_3 = [[1,0,0],[0,-1,0],[0,0,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[0, 0] = 1j; m[1, 1] = -1j  # i*lambda_3
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_3')

    # lambda_4 = [[0,0,1],[0,0,0],[1,0,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[0, 2] = 1j; m[2, 0] = 1j
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_4')

    # lambda_5 = [[0,0,-i],[0,0,0],[i,0,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[0, 2] = 1.0; m[2, 0] = -1.0
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_5')

    # lambda_6 = [[0,0,0],[0,0,1],[0,1,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[1, 2] = 1j; m[2, 1] = 1j
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_6')

    # lambda_7 = [[0,0,0],[0,0,-i],[0,i,0]]
    m = np.zeros((3, 3), dtype=complex)
    m[1, 2] = 1.0; m[2, 1] = -1.0
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_7')

    # lambda_8 = diag(1,1,-2)/sqrt(3)
    m = np.zeros((3, 3), dtype=complex)
    m[0, 0] = 1j / np.sqrt(3); m[1, 1] = 1j / np.sqrt(3); m[2, 2] = -2j / np.sqrt(3)
    R = np.eye(4, dtype=complex); R[1:, 1:] = m.conj().T
    gm_16.append(build_bimodule_16(np.eye(4), R))
    gm_names.append('su3_8')

    return gm_16, gm_names


# =============================================================================
# SECTION 3: DOUBLE COMMUTATOR COMPUTATION ENGINE
# =============================================================================

def compute_double_comm_matrix(D_16, AF_16_list, AF_names, n_dim):
    """
    Compute the full matrix of double commutator norms:
        C[i,j] = max_{alpha=1..8} || [[gamma_alpha_full, a_i_full], o(b_j_full)] ||_inf

    where gamma_alpha acts on the spinor factor and a_i, b_j act on the A_F factor.

    For the full D_K on a rep sector, D_16 is the full D_K matrix on V_rep x C^16.
    We use the Clifford part only (gamma_alpha embedded in 16-dim spinor space).

    Args:
        D_16: (N,N) the Dirac operator matrix on the sector
        AF_16_list: list of (16,16) algebra generators
        AF_names: list of names
        n_dim: dimension of the representation (dim_rho)

    Returns:
        C: (n_gen, n_gen) matrix of double commutator norms
    """
    n_gen = len(AF_16_list)
    C = np.zeros((n_gen, n_gen))

    for i in range(n_gen):
        # a acts as I_rho x a_16
        if n_dim > 1:
            a_full = np.kron(np.eye(n_dim), AF_16_list[i])
        else:
            a_full = AF_16_list[i]
        comm_Da = D_16 @ a_full - a_full @ D_16

        for j in range(n_gen):
            ob_16 = o_map_16(AF_16_list[j])
            if n_dim > 1:
                ob_full = np.kron(np.eye(n_dim), ob_16)
            else:
                ob_full = ob_16
            dc = comm_Da @ ob_full - ob_full @ comm_Da
            C[i, j] = np.max(np.abs(dc))

    return C


def compute_pure_clifford_double_comm(gammas):
    """
    Compute the tau-independent pure Clifford double commutator on the 32-dim space.
    This is the structural core of the order-one violation.

    Returns:
        C_cliff: (n_gen, n_gen) matrix indexed by A_F generators
    """
    (AF_16, AF_32, AF_names, AF_factors,
     AF_class, gauge_idx, scalar_idx) = build_AF_generators_classified()
    n_gen = len(AF_32)
    gamma_32 = [embed_spinor_op_32(g) for g in gammas]

    C_cliff = np.zeros((n_gen, n_gen))
    for alpha in range(8):
        for i in range(n_gen):
            comm_Da = gamma_32[alpha] @ AF_32[i] - AF_32[i] @ gamma_32[alpha]
            for j in range(n_gen):
                ob = o_map(AF_32[j])
                dc = comm_Da @ ob - ob @ comm_Da
                err = np.max(np.abs(dc))
                C_cliff[i, j] = max(C_cliff[i, j], err)

    return C_cliff, AF_names, AF_factors, AF_class, gauge_idx, scalar_idx


# =============================================================================
# SECTION 4: WEAK ORDER-ONE TEST (Bochniak-Sitarz)
# =============================================================================

def test_weak_order_one(C_full, gauge_idx, scalar_idx, AF_names, AF_class):
    """
    Apply the Bochniak-Sitarz weak order-one decomposition to the full
    double commutator matrix C.

    The weak condition requires: C[i,j] = 0 for i,j BOTH in gauge_idx.
    It allows: C[i,j] != 0 when i or j is in scalar_idx.

    Returns:
        dict with:
          gauge_gauge_max: max norm in gauge-gauge block
          gauge_scalar_max: max norm in gauge-scalar block
          scalar_scalar_max: max norm in scalar-scalar block
          weak_satisfied: bool (gauge_gauge_max < threshold)
          detailed_blocks: per-subalgebra block norms
    """
    # Extract blocks
    gg = C_full[np.ix_(gauge_idx, gauge_idx)]
    gs = np.zeros(0)
    ss = np.zeros(0)
    if len(scalar_idx) > 0:
        gs_block = C_full[np.ix_(gauge_idx, scalar_idx)]
        sg_block = C_full[np.ix_(scalar_idx, gauge_idx)]
        ss_block = C_full[np.ix_(scalar_idx, scalar_idx)]
        gs = np.maximum(gs_block, sg_block.T)  # symmetric max
        ss = ss_block

    gg_max = np.max(gg) if gg.size > 0 else 0.0
    gs_max = np.max(gs) if gs.size > 0 else 0.0
    ss_max = np.max(ss) if ss.size > 0 else 0.0

    # Sub-decompose gauge block into su(2)_L, u(1)_Y, su(3)_C
    su2L_idx_in_gauge = []
    u1Y_idx_in_gauge = []
    su3C_idx_in_gauge = []

    for local_i, global_i in enumerate(gauge_idx):
        name = AF_names[global_i]
        if name.startswith('H_'):
            su2L_idx_in_gauge.append(local_i)
        elif name == 'C_Im':
            u1Y_idx_in_gauge.append(local_i)
        elif name.startswith('M3_') or name.startswith('su3_'):
            su3C_idx_in_gauge.append(local_i)

    blocks = {}
    for label, idx_set in [('su2L_su2L', (su2L_idx_in_gauge, su2L_idx_in_gauge)),
                            ('su2L_u1Y', (su2L_idx_in_gauge, u1Y_idx_in_gauge)),
                            ('su2L_su3C', (su2L_idx_in_gauge, su3C_idx_in_gauge)),
                            ('u1Y_u1Y', (u1Y_idx_in_gauge, u1Y_idx_in_gauge)),
                            ('u1Y_su3C', (u1Y_idx_in_gauge, su3C_idx_in_gauge)),
                            ('su3C_su3C', (su3C_idx_in_gauge, su3C_idx_in_gauge))]:
        idx_a, idx_b = idx_set
        if len(idx_a) > 0 and len(idx_b) > 0:
            block = gg[np.ix_(idx_a, idx_b)]
            blocks[label] = np.max(block)
        else:
            blocks[label] = 0.0

    threshold = 1e-10
    weak_satisfied = gg_max < threshold

    return {
        'gauge_gauge_max': gg_max,
        'gauge_scalar_max': gs_max,
        'scalar_scalar_max': ss_max,
        'weak_satisfied': weak_satisfied,
        'detailed_blocks': blocks,
        'gauge_gauge_matrix': gg,
        'gauge_names': [AF_names[i] for i in gauge_idx],
        'scalar_names': [AF_names[i] for i in scalar_idx],
    }


# =============================================================================
# SECTION 5: INNER FLUCTUATION MODULE Omega^1_D(A)
# =============================================================================

def compute_omega1_module(D_mat, AF_16_list, dim_rho, threshold=1e-10):
    """
    Compute the dimension of the inner fluctuation module Omega^1_D(A_F).

    Omega^1_D(A) = span{ sum_i a_i [D, b_i] : a_i, b_i in A }

    When order-one holds, dim(Omega^1_D) = dim(gauge bosons) + dim(Higgs).
    When order-one fails, the module can be LARGER due to quadratic terms.

    We compute:
    1. Linear module: span{a_i [D, b_j]} for all generator pairs
    2. Quadratic module: span{[D, a_i][D, b_j]} for all pairs
    3. Combined module: linear + quadratic

    Returns:
        dim_linear: rank of the linear fluctuation space
        dim_quadratic: rank of the quadratic fluctuation space
        dim_combined: rank of linear + quadratic combined
    """
    n_gen = len(AF_16_list)
    N = D_mat.shape[0]

    # Flatten each operator into a vector of length N^2
    linear_vecs = []
    quadratic_vecs = []

    I_rho = np.eye(dim_rho, dtype=complex) if dim_rho > 1 else None

    for j in range(n_gen):
        if dim_rho > 1:
            b_full = np.kron(I_rho, AF_16_list[j])
        else:
            b_full = AF_16_list[j]
        comm_Db = D_mat @ b_full - b_full @ D_mat  # [D, b_j]

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

    # Compute ranks
    sv_lin = np.linalg.svd(linear_mat, compute_uv=False)
    sv_quad = np.linalg.svd(quadratic_mat, compute_uv=False)
    sv_comb = np.linalg.svd(combined_mat, compute_uv=False)

    # Adaptive threshold: fraction of largest singular value
    def rank_from_sv(sv, rel_thresh=1e-10):
        if len(sv) == 0:
            return 0
        cutoff = sv[0] * rel_thresh
        return int(np.sum(sv > cutoff))

    dim_linear = rank_from_sv(sv_lin)
    dim_quadratic = rank_from_sv(sv_quad)
    dim_combined = rank_from_sv(sv_comb)

    return dim_linear, dim_quadratic, dim_combined


# =============================================================================
# SECTION 6: GELL-MANN PURE GAUGE TEST (strongest form of weak order-one)
# =============================================================================

def test_gellmann_gauge_closure(D_mat, dim_rho, gammas):
    """
    Test the weak order-one condition using the PHYSICAL gauge generators:
    - 3 su(2)_L generators (H_i, H_j, H_k on Psi_+)
    - 1 u(1)_Y generator (C_Im on Psi_+)
    - 8 su(3)_C generators (Gell-Mann on color indices)

    This is the most physically meaningful test: do the Standard Model
    gauge generators close under double commutation with D_K?

    Returns:
        norms: dict of block norms
        full_matrix: (12,12) double commutator matrix for the 12 gauge generators
    """
    # Build the 12 physical gauge generators on 16-dim Psi_+
    gauge_16 = []
    gauge_names = []

    # u(1)_Y
    L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
    gauge_16.append(build_bimodule_16(L_CIm, np.eye(4)))
    gauge_names.append('u1Y')

    # su(2)_L: H_i, H_j, H_k
    L_Hi = np.diag([1j, -1j, 1j, -1j])
    gauge_16.append(build_bimodule_16(L_Hi, np.eye(4)))
    gauge_names.append('su2L_1')

    L_Hj = np.zeros((4, 4), dtype=complex)
    L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
    gauge_16.append(build_bimodule_16(L_Hj, np.eye(4)))
    gauge_names.append('su2L_2')

    L_Hk = np.zeros((4, 4), dtype=complex)
    L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
    gauge_16.append(build_bimodule_16(L_Hk, np.eye(4)))
    gauge_names.append('su2L_3')

    # su(3)_C: 8 Gell-Mann on color factor
    gm_16, gm_names = build_su3_gellmann_generators_on_AF()
    gauge_16.extend(gm_16)
    gauge_names.extend(gm_names)

    n_gauge = len(gauge_16)  # should be 12

    # Compute double commutator matrix
    I_rho = np.eye(dim_rho, dtype=complex) if dim_rho > 1 else None
    C_gauge = np.zeros((n_gauge, n_gauge))

    for i in range(n_gauge):
        if dim_rho > 1:
            a_full = np.kron(I_rho, gauge_16[i])
        else:
            a_full = gauge_16[i]
        comm_Da = D_mat @ a_full - a_full @ D_mat

        for j in range(n_gauge):
            ob_16 = o_map_16(gauge_16[j])
            if dim_rho > 1:
                ob_full = np.kron(I_rho, ob_16)
            else:
                ob_full = ob_16
            dc = comm_Da @ ob_full - ob_full @ comm_Da
            C_gauge[i, j] = np.max(np.abs(dc))

    # Block decomposition
    u1_idx = [0]
    su2_idx = [1, 2, 3]
    su3_idx = list(range(4, 12))

    blocks = {}
    for label, (idx_a, idx_b) in [
        ('u1Y_u1Y', (u1_idx, u1_idx)),
        ('u1Y_su2L', (u1_idx, su2_idx)),
        ('u1Y_su3C', (u1_idx, su3_idx)),
        ('su2L_su2L', (su2_idx, su2_idx)),
        ('su2L_su3C', (su2_idx, su3_idx)),
        ('su3C_su3C', (su3_idx, su3_idx)),
    ]:
        block = C_gauge[np.ix_(idx_a, idx_b)]
        blocks[label] = {
            'max': np.max(block),
            'mean': np.mean(block),
            'block': block,
        }

    return {
        'norms': {k: v['max'] for k, v in blocks.items()},
        'means': {k: v['mean'] for k, v in blocks.items()},
        'full_matrix': C_gauge,
        'gauge_names': gauge_names,
        'blocks': blocks,
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    t_total_start = time.time()

    print("=" * 78)
    print("WEAK-ORDER-ONE-45: Bochniak-Sitarz Weak Order-One Condition")
    print("=" * 78)
    print()

    # Setup infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # Tau values: fold + neighborhood
    tau_fold = 0.20
    tau_values = np.array([0.00, 0.10, 0.20, 0.30, 0.40, 0.50])
    sectors = [(1, 0)]  # Use (1,0) fundamental rep as primary test sector
    sector_labels = ['(1,0)']

    # =========================================================================
    # TEST 1: Pure Clifford double commutator with gauge/scalar classification
    # =========================================================================
    print("=" * 78)
    print("TEST 1: PURE CLIFFORD DOUBLE COMMUTATOR (tau-independent, 32-dim)")
    print("         with Bochniak-Sitarz gauge/scalar decomposition")
    print("=" * 78)
    print()

    t0 = time.time()
    (C_cliff, AF_names, AF_factors, AF_class,
     gauge_idx, scalar_idx) = compute_pure_clifford_double_comm(gammas)
    dt = time.time() - t0

    print(f"  Computed in {dt:.1f}s")
    print(f"  Total generators: {len(AF_names)}")
    print(f"  Gauge generators ({len(gauge_idx)}): "
          f"{[AF_names[i] for i in gauge_idx]}")
    print(f"  Scalar generators ({len(scalar_idx)}): "
          f"{[AF_names[i] for i in scalar_idx]}")
    print()

    # Apply weak order-one test
    weak_result = test_weak_order_one(C_cliff, gauge_idx, scalar_idx,
                                       AF_names, AF_class)

    print("  BOCHNIAK-SITARZ DECOMPOSITION:")
    print(f"    Gauge-Gauge max norm:   {weak_result['gauge_gauge_max']:.6e}")
    print(f"    Gauge-Scalar max norm:  {weak_result['gauge_scalar_max']:.6e}")
    print(f"    Scalar-Scalar max norm: {weak_result['scalar_scalar_max']:.6e}")
    print()
    print(f"  Weak order-one SATISFIED? {weak_result['weak_satisfied']}")
    print()

    print("  Sub-block decomposition (within gauge sector):")
    for label, norm in sorted(weak_result['detailed_blocks'].items()):
        status = "PASS" if norm < 1e-10 else f"FAIL ({norm:.4e})"
        print(f"    {label:15s}: {status}")
    print()

    # Full factor pair table
    print("  Full A_F factor pair table (L_inf, Clifford):")
    factors_unique = ['C', 'H', 'M3']
    for f1 in factors_unique:
        for f2 in factors_unique:
            idx_f1 = [i for i, f in enumerate(AF_factors) if f == f1]
            idx_f2 = [i for i, f in enumerate(AF_factors) if f == f2]
            if len(idx_f1) > 0 and len(idx_f2) > 0:
                block = C_cliff[np.ix_(idx_f1, idx_f2)]
                mx = np.max(block)
                status = "PASS" if mx < 1e-10 else f"FAIL ({mx:.4e})"
                print(f"    ({f1:3s}, {f2:3s}): {status}")
    print()

    # =========================================================================
    # TEST 2: Full D_K double commutator at the fold (tau=0.20)
    # =========================================================================
    print("=" * 78)
    print("TEST 2: FULL D_K DOUBLE COMMUTATOR AT FOLD (tau=0.20)")
    print("         Bochniak-Sitarz weak order-one on (1,0) sector")
    print("=" * 78)
    print()

    _irrep_cache.clear()
    rho, dim_rho = get_irrep(1, 0, gens, f_abc)
    print(f"  Sector (1,0): dim_rho = {dim_rho}")

    (AF_16, AF_32, AF_names_full, AF_factors_full,
     AF_class_full, gauge_idx_full, scalar_idx_full
    ) = build_AF_generators_classified()

    for tau in [tau_fold]:
        t0 = time.time()
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)
        D_K = dirac_operator_on_irrep(rho, E, gammas, Omega)
        dt_build = time.time() - t0

        print(f"\n  tau = {tau:.2f} (D_K built in {dt_build:.2f}s)")
        print(f"  D_K shape: {D_K.shape}, Hermitian check: "
              f"{np.max(np.abs(D_K - D_K.conj().T)):.2e}")

        # Compute full double commutator matrix on sector space
        t0 = time.time()
        C_full_sector = compute_double_comm_matrix(
            D_K, AF_16, AF_names_full, dim_rho)
        dt_comm = time.time() - t0
        print(f"  Double commutator matrix computed in {dt_comm:.1f}s")

        # Apply weak order-one test
        weak_sector = test_weak_order_one(
            C_full_sector, gauge_idx_full, scalar_idx_full,
            AF_names_full, AF_class_full)

        print(f"\n  BOCHNIAK-SITARZ DECOMPOSITION (D_K on (1,0)):")
        print(f"    Gauge-Gauge max norm:   {weak_sector['gauge_gauge_max']:.6e}")
        print(f"    Gauge-Scalar max norm:  {weak_sector['gauge_scalar_max']:.6e}")
        print(f"    Scalar-Scalar max norm: {weak_sector['scalar_scalar_max']:.6e}")
        print(f"    FULL max norm:          {np.max(C_full_sector):.6e}")
        print()
        print(f"  Weak order-one SATISFIED? {weak_sector['weak_satisfied']}")
        print()

        print("  Sub-block decomposition:")
        for label, norm in sorted(weak_sector['detailed_blocks'].items()):
            status = "PASS" if norm < 1e-10 else f"FAIL ({norm:.4e})"
            print(f"    {label:15s}: {status}")

    # =========================================================================
    # TEST 3: Gell-Mann physical gauge test at the fold
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 3: PHYSICAL GAUGE GENERATORS (Gell-Mann + su(2)_L + u(1)_Y)")
    print("         12 gauge generators, D_K on (1,0) at fold")
    print("=" * 78)
    print()

    _irrep_cache.clear()
    rho, dim_rho = get_irrep(1, 0, gens, f_abc)
    g_s = jensen_metric(B_ab, tau_fold)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K_fold = dirac_operator_on_irrep(rho, E, gammas, Omega)

    t0 = time.time()
    gm_result = test_gellmann_gauge_closure(D_K_fold, dim_rho, gammas)
    dt_gm = time.time() - t0

    print(f"  Computed in {dt_gm:.1f}s")
    print()
    print("  Block norms (L_inf):")
    for label, norm in sorted(gm_result['norms'].items()):
        status = "PASS" if norm < 1e-10 else f"FAIL ({norm:.4e})"
        print(f"    {label:15s}: {status}")
    print()

    # Print the full 12x12 matrix
    print("  Full 12x12 gauge double commutator matrix:")
    print(f"  {'':15s}", end="")
    for name in gm_result['gauge_names']:
        print(f" {name:>8s}", end="")
    print()
    for i, name_i in enumerate(gm_result['gauge_names']):
        print(f"  {name_i:15s}", end="")
        for j in range(len(gm_result['gauge_names'])):
            val = gm_result['full_matrix'][i, j]
            if val < 1e-10:
                print(f"     {'0':>3s}", end="")
            else:
                print(f" {val:8.4f}", end="")
        print()
    print()

    # Overall gauge closure
    gauge_max = max(gm_result['norms'].values())
    print(f"  Overall gauge sector max: {gauge_max:.6e}")
    if gauge_max < 1e-10:
        print("  RESULT: Gauge sector CLOSES under Bochniak-Sitarz weak condition.")
    else:
        print("  RESULT: Gauge sector does NOT close. The violation is in:")
        for label, norm in sorted(gm_result['norms'].items()):
            if norm > 1e-10:
                print(f"    {label}: norm = {norm:.4e}")

    # =========================================================================
    # TEST 4: Tau scan of the gauge-gauge violation
    # =========================================================================
    print()
    print("=" * 78)
    print("TEST 4: TAU SCAN OF GAUGE-GAUGE VIOLATION")
    print("=" * 78)
    print()

    gg_vs_tau = np.zeros(len(tau_values))
    gs_vs_tau = np.zeros(len(tau_values))
    ss_vs_tau = np.zeros(len(tau_values))
    full_vs_tau = np.zeros(len(tau_values))
    gm_gg_vs_tau = np.zeros(len(tau_values))

    for ti, tau in enumerate(tau_values):
        _irrep_cache.clear()
        rho, dim_rho = get_irrep(1, 0, gens, f_abc)
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)
        D_K_tau = dirac_operator_on_irrep(rho, E, gammas, Omega)

        C_tau = compute_double_comm_matrix(
            D_K_tau, AF_16, AF_names_full, dim_rho)
        weak_tau = test_weak_order_one(
            C_tau, gauge_idx_full, scalar_idx_full,
            AF_names_full, AF_class_full)

        gg_vs_tau[ti] = weak_tau['gauge_gauge_max']
        gs_vs_tau[ti] = weak_tau['gauge_scalar_max']
        ss_vs_tau[ti] = weak_tau['scalar_scalar_max']
        full_vs_tau[ti] = np.max(C_tau)

        # Also physical gauge test
        gm_tau = test_gellmann_gauge_closure(D_K_tau, dim_rho, gammas)
        gm_gg_vs_tau[ti] = max(gm_tau['norms'].values())

        print(f"  tau={tau:.2f}: GG={gg_vs_tau[ti]:.4e}, "
              f"GS={gs_vs_tau[ti]:.4e}, SS={ss_vs_tau[ti]:.4e}, "
              f"Full={full_vs_tau[ti]:.4e}, GM_GG={gm_gg_vs_tau[ti]:.4e}")

    print()

    # =========================================================================
    # TEST 5: Inner fluctuation module dimension
    # =========================================================================
    print("=" * 78)
    print("TEST 5: INNER FLUCTUATION MODULE Omega^1_D(A_F)")
    print("=" * 78)
    print()

    _irrep_cache.clear()
    rho, dim_rho = get_irrep(1, 0, gens, f_abc)
    g_s = jensen_metric(B_ab, tau_fold)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K_fold = dirac_operator_on_irrep(rho, E, gammas, Omega)

    t0 = time.time()
    dim_lin, dim_quad, dim_comb = compute_omega1_module(
        D_K_fold, AF_16, dim_rho)
    dt_mod = time.time() - t0

    print(f"  Computed in {dt_mod:.1f}s")
    print(f"  D_K on (1,0) at tau={tau_fold:.2f}:")
    print(f"    Linear module dim:     {dim_lin}")
    print(f"    Quadratic module dim:  {dim_quad}")
    print(f"    Combined module dim:   {dim_comb}")
    print(f"    Quadratic excess:      {dim_comb - dim_lin}")
    print()

    # Expected: if order-one held, dim_combined = dim_linear
    # The excess measures the "new directions" opened by order-one violation
    if dim_comb > dim_lin:
        print(f"  ORDER-ONE VIOLATION OPENS {dim_comb - dim_lin} NEW DIRECTIONS")
        print("  in the inner fluctuation space. These are the quadratic")
        print("  fluctuations of Chamseddine-Connes-van Suijlekom (2013, Paper 23).")
    else:
        print("  No additional directions from quadratic fluctuations.")
    print()

    # Also test on (0,0) singlet for comparison
    print("  Singlet (0,0) for comparison:")
    g_s = jensen_metric(B_ab, tau_fold)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega_fold = spinor_connection_offset(Gamma, gammas)
    # On (0,0), D_K = Omega only (16x16)
    dim_lin_00, dim_quad_00, dim_comb_00 = compute_omega1_module(
        Omega_fold, AF_16, 1)
    print(f"    Linear module dim:     {dim_lin_00}")
    print(f"    Quadratic module dim:  {dim_quad_00}")
    print(f"    Combined module dim:   {dim_comb_00}")
    print(f"    Quadratic excess:      {dim_comb_00 - dim_lin_00}")
    print()

    # =========================================================================
    # TEST 6: Quantitative weak order-one ratio
    # =========================================================================
    print("=" * 78)
    print("TEST 6: WEAK ORDER-ONE RATIO (violation severity)")
    print("=" * 78)
    print()

    for ti, tau in enumerate(tau_values):
        full_max = full_vs_tau[ti]
        gg_max_val = gg_vs_tau[ti]
        if full_max > 0:
            ratio = gg_max_val / full_max
        else:
            ratio = 0.0
        print(f"  tau={tau:.2f}: ||GG|| / ||Full|| = {ratio:.6f}  "
              f"(GG={gg_max_val:.4e}, Full={full_max:.4e})")

    print()
    print("  If ratio = 0: weak condition satisfied perfectly")
    print("  If ratio = 1: full violation is entirely gauge-gauge")
    print("  If 0 < ratio < 1: partial satisfaction")
    print()

    # =========================================================================
    # CROSS-CHECK: Verify against s28b results
    # =========================================================================
    print("=" * 78)
    print("CROSS-CHECK: Consistency with s28b_order_one.txt")
    print("=" * 78)
    print()

    # s28b reported: Clifford 32-dim max = 4.000 at (H_i, H_i)
    # Our C_cliff max should match
    cliff_max = np.max(C_cliff)
    print(f"  Clifford 32-dim max (this script): {cliff_max:.6e}")
    print(f"  Expected (s28b):                   4.000000e+00")
    match_s28 = abs(cliff_max - 4.0) < 1e-6
    print(f"  Match: {'YES' if match_s28 else 'NO (DISCREPANCY!)'}")
    print()

    # Factor breakdown check
    print("  Factor breakdown (Clifford 32-dim):")
    for f1 in ['C', 'H', 'M3']:
        for f2 in ['C', 'H', 'M3']:
            idx1 = [i for i, f in enumerate(AF_factors) if f == f1]
            idx2 = [i for i, f in enumerate(AF_factors) if f == f2]
            if len(idx1) > 0 and len(idx2) > 0:
                block = C_cliff[np.ix_(idx1, idx2)]
                mx = np.max(block)
                print(f"    ({f1:3s}, {f2:3s}): {mx:.6e}")
    print()

    # =========================================================================
    # DIMENSIONAL CHECK
    # =========================================================================
    print("=" * 78)
    print("DIMENSIONAL CHECK")
    print("=" * 78)
    print()
    print("  All double commutators are dimensionless (operators on Hilbert space).")
    print("  The norm || [[D, a], b^0] || has units of [D] (energy) since")
    print("  a and b^0 are dimensionless algebra elements.")
    print("  We report absolute norms (not normalized by ||D||).")
    print()
    print("  For reference at tau=0.20:")
    evals = np.linalg.eigvalsh(D_K_fold)
    print(f"    ||D_K|| (operator norm) = {np.max(np.abs(evals)):.4f}")
    print(f"    ||D_K|| (Frobenius)     = {la_norm(D_K_fold, 'fro'):.4f}")
    print(f"    Order-one max / ||D_K|| = {full_vs_tau[2] / np.max(np.abs(evals)):.4f}")
    print()

    # =========================================================================
    # LIMITING CASE CHECK
    # =========================================================================
    print("=" * 78)
    print("LIMITING CASE: tau=0 (round SU(3))")
    print("=" * 78)
    print()
    print("  At tau=0, SU(3) has its bi-invariant (round) metric.")
    print("  The order-one violation is present even here because it is")
    print("  structural (Baptista-Connes representation mismatch).")
    print(f"  GG at tau=0: {gg_vs_tau[0]:.6e}")
    print(f"  Full at tau=0: {full_vs_tau[0]:.6e}")
    print()

    # =========================================================================
    # VERDICT
    # =========================================================================
    print("=" * 78)
    print("GATE WEAK-ORDER-ONE-45 VERDICT")
    print("=" * 78)
    print()

    gg_at_fold = gg_vs_tau[2]  # tau=0.20 is index 2
    full_at_fold = full_vs_tau[2]
    gm_at_fold = gm_gg_vs_tau[2]

    print(f"  At fold tau = {tau_fold:.2f}:")
    print(f"    Full order-one violation:  {full_at_fold:.6e}")
    print(f"    Gauge-gauge (classified):  {gg_at_fold:.6e}")
    print(f"    Gauge-gauge (Gell-Mann):   {gm_at_fold:.6e}")
    print(f"    Gauge-scalar:              {gs_vs_tau[2]:.6e}")
    print(f"    Scalar-scalar:             {ss_vs_tau[2]:.6e}")
    print()

    # Classify the result
    if gg_at_fold < 1e-10 and gm_at_fold < 1e-10:
        verdict = "PASS"
        detail = ("Weak order-one condition SATISFIED. The gauge-gauge sector "
                   "closes to machine precision. All order-one violation resides "
                   "in gauge-scalar and scalar-scalar sectors, consistent with "
                   "Bochniak-Sitarz weak condition for beyond-SM extensions.")
    elif gg_at_fold < 1e-10 and gm_at_fold > 1e-10:
        verdict = "PARTIAL"
        detail = ("Classified gauge-gauge passes but physical Gell-Mann test fails. "
                   "The classification depends on how generators are assigned.")
    elif gg_at_fold > 1e-10 and gg_at_fold < full_at_fold * 0.5:
        verdict = "PARTIAL"
        ratio_str = f"{gg_at_fold / full_at_fold:.2%}"
        detail = (f"Gauge-gauge violation ({gg_at_fold:.4e}) is {ratio_str} of "
                   f"full violation ({full_at_fold:.4e}). The weak condition is "
                   f"violated but the violation is concentrated in gauge-scalar "
                   f"interactions, suggesting partial closure.")
    else:
        verdict = "FAIL"
        ratio_str = f"{gg_at_fold / full_at_fold:.2%}" if full_at_fold > 0 else "N/A"
        detail = (f"Gauge-gauge violation ({gg_at_fold:.4e}) is {ratio_str} of "
                   f"full violation ({full_at_fold:.4e}). The weak order-one "
                   f"condition is NOT satisfied. The Baptista-Connes representation "
                   f"mismatch affects gauge generators as well as scalars.")

    print(f"  VERDICT: {verdict}")
    print(f"  {detail}")
    print()

    if dim_comb > dim_lin:
        print(f"  OMEGA^1_D module: {dim_comb - dim_lin} extra directions from "
              f"quadratic fluctuations.")
        print(f"  These correspond to {dim_comb - dim_lin} additional scalar fields")
        print(f"  beyond the standard Higgs sector (CCS 2013, Paper 23 mechanism).")
    print()

    print("  STRUCTURAL INTERPRETATION:")
    print("  " + "-" * 70)
    print()
    print("  The order-one violation ||[[D_K, a], b^0]|| = 4.000 at (H,H)")
    print("  is STRUCTURAL: it arises from the representation mismatch between")
    print("  the Clifford algebra Cl(R^8) and the bimodule structure of A_F.")
    print("  This mismatch affects ALL algebra factors, not just the scalar sector.")
    print()
    print("  Bochniak-Sitarz weak order-one requires the GAUGE sector to close.")
    print("  For the framework's spectral triple, this requires the su(2)_L and")
    print("  su(3)_C generators to commute (in the double-commutator sense)")
    print("  with the opposite algebra action through the Clifford structure.")
    print()
    print("  The result determines whether the inner fluctuation module")
    print("  Omega^1_D(A_F) is controlled by the standard SM gauge group")
    print("  or requires the full CCS (2013) quadratic extension.")

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    t_total = time.time() - t_total_start

    outfile = os.path.join(OUTDIR, "s45_weak_order_one.npz")
    np.savez(outfile,
             # Tau scan
             tau_values=tau_values,
             tau_fold=tau_fold,
             gg_vs_tau=gg_vs_tau,
             gs_vs_tau=gs_vs_tau,
             ss_vs_tau=ss_vs_tau,
             full_vs_tau=full_vs_tau,
             gm_gg_vs_tau=gm_gg_vs_tau,
             # Clifford structure (tau-independent)
             C_cliff=C_cliff,
             cliff_max=cliff_max,
             # Fold results
             gg_at_fold=gg_at_fold,
             full_at_fold=full_at_fold,
             gm_at_fold=gm_at_fold,
             # Omega^1 module dimensions
             dim_linear_10=dim_lin,
             dim_quadratic_10=dim_quad,
             dim_combined_10=dim_comb,
             dim_linear_00=dim_lin_00,
             dim_quadratic_00=dim_quad_00,
             dim_combined_00=dim_comb_00,
             # Gell-Mann gauge matrix at fold
             gm_matrix_fold=gm_result['full_matrix'],
             gm_gauge_names=np.array(gm_result['gauge_names']),
             # Metadata
             AF_names=np.array(AF_names),
             AF_factors=np.array(AF_factors),
             AF_class=np.array(AF_class),
             gauge_indices=np.array(gauge_idx),
             scalar_indices=np.array(scalar_idx),
             # Verdict
             verdict=np.array([verdict]),
             runtime=t_total)

    print()
    print(f"  Data saved to: {outfile}")
    print(f"  Total runtime: {t_total:.1f}s")
    print()
    print("WEAK-ORDER-ONE-45 COMPUTATION COMPLETE")
    print("=" * 78)
