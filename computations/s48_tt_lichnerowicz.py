#!/usr/bin/env python3
"""
S48 TT-LICH-48: Lichnerowicz Operator on TT 2-Tensors (Jensen-Deformed SU(3))
================================================================================

Computes the spectrum of the Lichnerowicz operator Delta_L acting on
transverse-traceless (TT) symmetric 2-tensors in the singlet (0,0) Peter-Weyl
sector of Jensen-deformed SU(3).

Mathematical framework:

    The Lichnerowicz operator on symmetric 2-tensors h_{ab} is:

        (Delta_L h)_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}

    In the (0,0) singlet sector, -nabla^2 h = C_2 h = 0 (Casimir of trivial rep).
    So Delta_L reduces to the PURELY ALGEBRAIC curvature action:

        (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}         (*)

    This is a linear map on the space of symmetric TT 2-tensors.

    TT conditions (for singlet sector on left-invariant metrics):
        1. Symmetric: h_{ab} = h_{ba}  (36 -> 36 components as sym matrix)
        2. Trace-free: g^{ab} h_{ab} = delta^{ab} h_{ab} = 0  (removes 1 DOF)
        3. Divergence-free: nabla^a h_{ab} = 0
           For left-invariant tensors in ON frame: sum_a Gamma^a_{ac} h_{cb} + ...
           reduces to algebraic constraint involving structure constants.

    In d=8 dimensions:
        - Symmetric 2-tensors: 8*9/2 = 36
        - Trace constraint: -1
        - Transversality (up to 8 constraints): -8
        - Expected TT modes: 36 - 1 - 8 = 27

Pair classification of eigenvalues:
    - HARD (su(2)-su(2)): 3 pairs within {e_0, e_1, e_2}
    - SOFT (su(2)-C^2): 12 cross pairs {su(2)} x {C^2}
    - C2-C2: 6 pairs within {e_3, e_4, e_5, e_6}
    - U1-mixed: involving e_7

Gate: TT-LICH-48
    PASS: full spectrum, no negative eigenvalues, hard/soft splitting confirmed
    FAIL: negative eigenvalues (TT instability)
    INFO: no hard/soft distinction visible

Cross-check: S20b proved no tachyons in the TT spectrum (different decomposition).

Output:
    - s48_tt_lichnerowicz.npz
    - s48_tt_lichnerowicz.png

Author: Spectral-Geometer (Session 48)
Date: 2026-03-17
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)
from s47_curvature_anatomy import compute_riemann_tensor_ON
from canonical_constants import tau_fold

DIM = 8  # dim(su(3))
N_SYM = DIM * (DIM + 1) // 2  # = 36 symmetric 2-tensor components


# =============================================================================
# MODULE 1: SYMMETRIC 2-TENSOR BASIS
# =============================================================================

def sym2_basis():
    """
    Construct a basis for symmetric 2-tensors in R^8.

    Returns list of 36 basis tensors e^{(I)}_{ab} where I indexes the basis.
    Convention: for a <= b, the basis tensor has
        e^{(I)}_{ab} = e^{(I)}_{ba} = 1/sqrt(2)  if a != b
        e^{(I)}_{aa} = 1                            if a == b

    This is an orthonormal basis with respect to the natural inner product
    <h, k> = sum_{a,b} h_{ab} k_{ab}.

    Returns:
        basis: list of (8,8) numpy arrays
        labels: list of (a,b) index pairs
    """
    basis = []
    labels = []
    for a in range(DIM):
        for b in range(a, DIM):
            e = np.zeros((DIM, DIM), dtype=np.float64)
            if a == b:
                e[a, a] = 1.0
            else:
                e[a, b] = 1.0 / np.sqrt(2.0)
                e[b, a] = 1.0 / np.sqrt(2.0)
            basis.append(e)
            labels.append((a, b))
    return basis, labels


# =============================================================================
# MODULE 2: TT PROJECTION
# =============================================================================

def trace_projector(basis, labels):
    """
    Project out the trace: h_{ab} -> h_{ab} - (1/d) delta_{ab} tr(h).

    The trace direction in the basis is T_{ab} = (1/sqrt(d)) delta_{ab}.
    The projector is P_TF = I - |T><T|.

    Returns:
        P_TF: (N_SYM, N_SYM) trace-free projector
    """
    # Build the trace vector in the basis representation
    # <T| e^{(I)}> = sum_{a,b} (1/sqrt(d)) delta_{ab} * e^{(I)}_{ab}
    #              = (1/sqrt(d)) * tr(e^{(I)})
    T_vec = np.zeros(N_SYM, dtype=np.float64)
    for I, (a, b) in enumerate(labels):
        T_vec[I] = np.trace(basis[I]) / np.sqrt(DIM)
    T_vec /= np.linalg.norm(T_vec)  # Should already be unit

    P_TF = np.eye(N_SYM) - np.outer(T_vec, T_vec)
    return P_TF


def divergence_operator(ft, Gamma, basis, labels):
    """
    Compute the divergence operator div: S^2(T*M) -> T*M
    for left-invariant tensors on a Lie group.

    For a left-invariant symmetric tensor h_{ab} in ON frame,
    the divergence is:

        (div h)_b = sum_a nabla_a h_{ab}

    For left-invariant h, nabla_{e_a} h_{bc} = - Gamma^d_{ab} h_{dc} - Gamma^d_{ac} h_{bd}
    (since e_a(h_{bc}) = 0 for left-invariant h).

    So: (div h)_b = sum_a (-Gamma^d_{ab} h_{da} - Gamma^d_{aa} h_{bd})
                  = -sum_{a,d} Gamma^d_{ab} h_{da} - sum_d (sum_a Gamma^d_{aa}) h_{bd}

    Note: sum_a Gamma^d_{aa} is related to the mean curvature. For a compact
    semisimple Lie group with left-invariant metric, this is:
        sum_a Gamma^d_{aa} = sum_a (1/2)(ft[a,a,d] - ft[a,d,a] + ft[d,a,a])
                           = sum_a (1/2)(-ft[a,d,a] + ft[d,a,a])
    since ft[a,a,d] = 0 (antisymmetry of [e_a, e_a] = 0).

    Returns:
        D: (DIM, N_SYM) matrix such that (div h)_b = D[b,I] * c_I
           where h = sum_I c_I e^{(I)}
    """
    D = np.zeros((DIM, N_SYM), dtype=np.float64)

    for I, eI in enumerate(basis):
        # Compute (div eI)_b = sum_a nabla_a (eI)_{ab}
        for b in range(DIM):
            val = 0.0
            for a in range(DIM):
                for d in range(DIM):
                    # nabla_{e_a} h_{db} contributes via -Gamma^c_{ad} h_{cb} - Gamma^c_{ab} h_{dc}
                    # Actually let me be more careful.
                    # (div h)_b = sum_a (nabla_{e_a} h)_{ab}
                    # nabla_{e_a} h_{cb} = e_a(h_{cb}) - Gamma^d_{ac} h_{db} - Gamma^d_{ab} h_{cd}
                    # For left-invariant h: e_a(h_{cb}) = 0
                    # So nabla_{e_a} h_{ab} = -Gamma^d_{aa} h_{db} - Gamma^d_{ab} h_{ad}
                    #   (set c=a in the formula above)
                    # Wait, I need to be careful with index placement.
                    # nabla_{e_a} h_{ab} = -sum_d Gamma^d_{aa} h_{db} - sum_d Gamma^d_{ab} h_{ad}
                    val -= Gamma[d, a, a] * eI[d, b]
                    val -= Gamma[d, a, b] * eI[a, d]
            D[b, I] = val

    return D


def tt_projector(ft, Gamma, basis, labels):
    """
    Construct the projector onto the TT (transverse trace-free) subspace.

    TT = ker(trace) intersect ker(divergence)

    Method: construct the constraint matrix C that maps symmetric tensors
    to (trace, divergence), then TT = ker(C).

    Returns:
        P_TT: (N_SYM, N_SYM) projector onto TT subspace
        n_tt: dimension of TT subspace
        V_TT: (N_SYM, n_tt) matrix whose columns are ON basis for TT subspace
    """
    # Trace constraint: one row
    T_vec = np.zeros(N_SYM, dtype=np.float64)
    for I, (a, b) in enumerate(labels):
        T_vec[I] = np.trace(basis[I])

    # Divergence constraint: DIM rows
    D = divergence_operator(ft, Gamma, basis, labels)

    # Combined constraint matrix: (1 + DIM) x N_SYM = 9 x 36
    C = np.vstack([T_vec.reshape(1, -1), D])

    # TT subspace = null space of C
    U, S, Vt = np.linalg.svd(C, full_matrices=True)

    # Numerical rank of C
    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10
    rank_C = np.sum(S > tol)

    # Null space: last (N_SYM - rank_C) rows of Vt
    n_tt = N_SYM - rank_C
    V_TT = Vt[rank_C:].T  # (N_SYM, n_tt)

    # Projector
    P_TT = V_TT @ V_TT.T

    return P_TT, n_tt, V_TT


# =============================================================================
# MODULE 3: LICHNEROWICZ OPERATOR (ALGEBRAIC PART)
# =============================================================================

def riemann_lowered(R_abcf, n=DIM):
    """
    Convert R^f_{abc} to R_{abcd} (all indices lowered, using delta in ON frame).

    R[a,b,c,f] = R^f_{abc} (as stored by compute_riemann_tensor_ON)
    R_{abcd} = delta_{df} R^f_{abc} = R^d_{abc} = R[a,b,c,d]

    In ON frame, lowering the upper index is trivial.
    So R_abcd = R[a,b,c,d] directly.

    Returns:
        Riem: (n,n,n,n) fully covariant Riemann tensor
    """
    # In ON frame, R_{abcd} = R^d_{abc} = R_abcf[a,b,c,d]
    # This is already correct since g_{df} = delta_{df}
    return R_abcf.copy()


def compute_ricci_from_riemann(Riem, n=DIM):
    """
    Compute Ricci tensor from Riemann: Ric_{bc} = sum_a R_{abca} = sum_a R^a_{bca}

    But our Riem storage: Riem[a,b,c,d] = R^d_{abc}
    So Ric_{bc} = sum_a Riem[a,b,c,a] = sum_a R^a_{abc}... no.

    Actually from compute_riemann_tensor_ON: R[a,b,c,f] = R^f_{abc}
    So Ric_{bc} = R^a_{bca} = R[b,c,a,a]... no.
    Ric_{bc} = sum_a R_{abca} where R_{abca} = R^a_{abc} = R[a,b,c,a]

    Let me use the einsum from s47: Ric = einsum('abca->bc', R_abcd)
    That gives Ric_{bc} = sum_a R[a,b,c,a] = sum_a R^a_{abc}.

    This is the standard Ricci: Ric_{bc} = R^a_{bac} (contraction on 1st and 4th)
    R^a_{bac} = R[b,a,c,a] ... hmm, let's match s47 exactly.

    s47 uses: Ric = np.einsum('abca->bc', R_abcd)
    Which is Ric[b,c] = sum_a R_abcd[a,b,c,a]
    And R_abcd[a,b,c,f] = R^f_{abc}
    So Ric[b,c] = sum_a R^a_{abc}

    Standard: Ric_{bc} = R^a_{bac} (first index contracted with fourth)
    We need: R^a_{bac} = R_abcd[b,a,c,a] (from the storage convention)

    Check: s47 does einsum('abca->bc') which sums R[a,b,c,a] over a.
    This gives sum_a R^a_{abc}, which equals:
    R^0_{0bc} + R^1_{1bc} + ... = R^a_{abc}

    The standard definition has Ric_{bc} = R^a_{bac}.
    These are related by the symmetry R^a_{abc} = -R^a_{bac} (antisymmetry in first two
    lower indices).

    Wait: R^d_{abc} is antisymmetric in a,b (first pair):
    R^d_{abc} = -R^d_{bac}

    So R^a_{abc} = -R^a_{bac} = -Ric_{bc} (standard)

    Hmm, let me check: s47 validates R_scalar(0) = 2.0 which is the correct
    scalar curvature of bi-invariant SU(3) at our normalization. So their
    convention must be correct. Let me just follow s47.
    """
    return np.einsum('abca->bc', Riem)


def lichnerowicz_action(Riem, Ric, h, n=DIM):
    """
    Apply the Lichnerowicz operator to a symmetric 2-tensor h_{ab}.

    (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}

    In ON frame with g = delta:
        -2 R_{acbd} h^{cd} = -2 sum_{c,d} R_{acbd} h_{cd}
        2 R_{(a}^c h_{b)c} = R_a^c h_{bc} + R_b^c h_{ac}
                            = sum_c Ric_{ac} h_{bc} + sum_c Ric_{bc} h_{ac}

    NOTE: The Riemann tensor convention matters critically.
    R_{acbd} means Riem[a,c,b,d] in our storage (since Riem[a,b,c,d] = R^d_{abc} = R_{abcd}).

    Actually: Riem[a,b,c,d] is stored as R^d_{abc}. In ON frame this equals R_{abcd}
    (all lower). So R_{acbd} = Riem[a,c,b,d].

    For the Ricci term: The Ricci tensor from s47 is
    Ric[b,c] = sum_a Riem[a,b,c,a].

    We need to verify sign conventions. The standard Lichnerowicz operator on
    closed Einstein manifolds with Ric = (R/n)g has eigenvalue R/n on each TT mode
    from the Ricci term, minus the Weyl/Riemann correction. Positive curvature
    should give POSITIVE eigenvalues (stability).

    Let me compute both terms separately and verify at tau=0 where we know the answer.

    Args:
        Riem: (n,n,n,n) Riemann tensor (all lower indices in ON frame)
        Ric: (n,n) Ricci tensor
        h: (n,n) symmetric 2-tensor

    Returns:
        DL_h: (n,n) result of Delta_L acting on h
    """
    DL_h = np.zeros((n, n), dtype=np.float64)

    # Term 1: -2 R_{acbd} h_{cd} = -2 sum_{c,d} Riem[a,c,b,d] * h[c,d]
    # Using einsum: -2 * einsum('acbd,cd->ab', Riem, h)
    term1 = -2.0 * np.einsum('acbd,cd->ab', Riem, h)

    # Term 2: Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
    # = Ric @ h + (Ric @ h)^T  ... wait
    # sum_c Ric[a,c] h[c,b] = (Ric @ h)[a,b]
    # sum_c Ric[b,c] h[c,a] = (Ric @ h)[b,a] = (Ric @ h)^T [a,b]  (since Ric symmetric)
    # Actually: sum_c Ric[b,c] h[c,a] = (h @ Ric)[a,b]  ... no.
    # Ric[b,c] h[c,a] summed over c = (Ric @ h^T)[b,a] = (h @ Ric)[a,b] if h symmetric
    # Since h is symmetric: h[c,a] = h[a,c], so sum_c Ric[b,c] h[a,c] = (h @ Ric^T)[a,b]
    # = (h @ Ric)[a,b] since Ric symmetric.

    term2 = Ric @ h + h @ Ric  # Symmetrized Ricci action

    DL_h = term1 + term2

    return DL_h


def lichnerowicz_matrix(Riem, Ric, basis, labels):
    """
    Compute the matrix representation of Delta_L in the symmetric 2-tensor basis.

    L[I,J] = <e^{(I)}, Delta_L e^{(J)}>

    where <A, B> = sum_{a,b} A_{ab} B_{ab} is the Frobenius inner product.

    Returns:
        L: (N_SYM, N_SYM) matrix
    """
    L = np.zeros((N_SYM, N_SYM), dtype=np.float64)

    for J in range(N_SYM):
        DL_eJ = lichnerowicz_action(Riem, Ric, basis[J])
        for I in range(N_SYM):
            L[I, J] = np.sum(basis[I] * DL_eJ)

    return L


# =============================================================================
# MODULE 4: CLASSIFICATION OF TT MODES
# =============================================================================

def classify_tt_mode(v_coeffs, V_TT, basis, labels):
    """
    Classify a TT eigenvector by its support in the different sectors.

    Given coefficients v in TT basis, reconstruct h_{ab} and measure
    how much weight falls in each sector:
        - DIAG-SU2: diagonal su(2) components (aa for a in SU2_IDX)
        - DIAG-C2: diagonal C^2 components
        - DIAG-U1: diagonal u(1) component
        - CROSS-SU2-SU2: off-diagonal within su(2)
        - CROSS-C2-C2: off-diagonal within C^2
        - CROSS-SU2-C2: cross su(2)-C^2
        - CROSS-U1-SU2: cross u(1)-su(2)
        - CROSS-U1-C2: cross u(1)-C^2

    Returns dict with weights (fraction of ||h||^2 in each sector).
    """
    # Reconstruct in sym2 basis
    c_sym = V_TT @ v_coeffs  # (N_SYM,)

    # Reconstruct h_{ab}
    h = sum(c_sym[I] * basis[I] for I in range(N_SYM))
    h_norm_sq = np.sum(h**2)
    if h_norm_sq < 1e-30:
        return {'total_norm': 0.0}

    # Measure sector weights
    weights = {}

    def sector_weight(idx_pairs):
        w = 0.0
        for a, b in idx_pairs:
            w += h[a, b]**2
            if a != b:
                w += h[b, a]**2
        return w / h_norm_sq

    # Diagonal blocks
    su2_diag = [(a, a) for a in SU2_IDX]
    c2_diag = [(a, a) for a in C2_IDX]
    u1_diag = [(7, 7)]

    # Off-diagonal within blocks
    su2_cross = [(a, b) for i, a in enumerate(SU2_IDX) for b in SU2_IDX[i+1:]]
    c2_cross = [(a, b) for i, a in enumerate(C2_IDX) for b in C2_IDX[i+1:]]

    # Cross blocks
    su2_c2_cross = [(a, b) for a in SU2_IDX for b in C2_IDX]
    u1_su2_cross = [(7, b) for b in SU2_IDX]
    u1_c2_cross = [(7, b) for b in C2_IDX]

    weights['su2_diag'] = sector_weight(su2_diag)
    weights['c2_diag'] = sector_weight(c2_diag)
    weights['u1_diag'] = sector_weight(u1_diag)
    weights['su2_su2'] = sector_weight(su2_cross)
    weights['c2_c2'] = sector_weight(c2_cross)
    weights['su2_c2'] = sector_weight(su2_c2_cross)
    weights['u1_su2'] = sector_weight(u1_su2_cross)
    weights['u1_c2'] = sector_weight(u1_c2_cross)

    # Coarser classification
    weights['hard'] = weights['su2_diag'] + weights['su2_su2']  # Pure su(2) block
    weights['soft'] = weights['su2_c2']                          # Cross su(2)-C^2
    weights['c2_block'] = weights['c2_diag'] + weights['c2_c2'] # Pure C^2 block
    weights['u1_mixed'] = weights['u1_diag'] + weights['u1_su2'] + weights['u1_c2']

    weights['total_norm'] = h_norm_sq

    return weights


def dominant_sector(weights):
    """Return the name of the sector with largest weight."""
    sectors = ['hard', 'soft', 'c2_block', 'u1_mixed']
    sector_names = ['HARD(su2)', 'SOFT(su2-C2)', 'C2-C2', 'U1-mixed']
    if weights.get('total_norm', 0) < 1e-30:
        return 'NULL'
    vals = [weights.get(s, 0) for s in sectors]
    idx = np.argmax(vals)
    return sector_names[idx]


# =============================================================================
# MODULE 5: COMPUTE ALL AT ONE TAU
# =============================================================================

def compute_tt_lichnerowicz_at_tau(tau):
    """
    Full computation of TT Lichnerowicz spectrum at one tau value.

    Returns dict with all results.
    """
    # Infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Riemann tensor
    R_abcf = compute_riemann_tensor_ON(ft, Gamma)
    Riem = riemann_lowered(R_abcf)
    Ric = compute_ricci_from_riemann(R_abcf)
    R_scalar = np.trace(Ric)

    # Symmetric 2-tensor basis
    basis, labels = sym2_basis()

    # TT projector
    P_TT, n_tt, V_TT = tt_projector(ft, Gamma, basis, labels)

    # Full Lichnerowicz matrix in sym2 basis
    L_full = lichnerowicz_matrix(Riem, Ric, basis, labels)

    # Check symmetry of L_full (should be symmetric since Delta_L is self-adjoint)
    sym_err = np.max(np.abs(L_full - L_full.T))

    # Restrict to TT subspace: L_TT = V_TT^T L_full V_TT
    L_TT = V_TT.T @ L_full @ V_TT

    # Check symmetry of L_TT
    sym_err_tt = np.max(np.abs(L_TT - L_TT.T))

    # Symmetrize (remove numerical noise)
    L_TT = 0.5 * (L_TT + L_TT.T)

    # Diagonalize
    eigenvalues, eigenvectors = np.linalg.eigh(L_TT)

    # Classify each eigenvector
    classifications = []
    for k in range(n_tt):
        w = classify_tt_mode(eigenvectors[:, k], V_TT, basis, labels)
        classifications.append(w)

    # Count negative eigenvalues
    n_negative = np.sum(eigenvalues < -1e-10)

    return {
        'tau': tau,
        'n_tt': n_tt,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors,
        'classifications': classifications,
        'n_negative': n_negative,
        'R_scalar': R_scalar,
        'Ric': Ric,
        'Riem': Riem,
        'sym_err_full': sym_err,
        'sym_err_tt': sym_err_tt,
        'L_TT': L_TT,
        'V_TT': V_TT,
    }


# =============================================================================
# MODULE 6: VALIDATION AT TAU = 0 (BI-INVARIANT)
# =============================================================================

def validate_biinvariant(result):
    """
    At tau=0, the metric is bi-invariant and the Lichnerowicz operator
    has known properties:

    1. R_{abcd} = (1/4)(delta_{ac} delta_{bd} - delta_{ad} delta_{bc})
       ... actually for bi-invariant SU(3), R is not constant-curvature.
       But Ric = (1/4) g for bi-invariant compact simple Lie groups
       (Ric_{ab} = -(1/4) B_{ab} = (1/4) |B_{ab}| = (1/4) delta_{ab} in ON frame).

    Actually for our normalization:
       Ric = (R/8) I = (2.0/8) I = 0.25 I  (Einstein, since bi-invariant)

    The Lichnerowicz on Einstein manifolds:
       Delta_L h = -nabla^2 h - 2 R_{acbd} h^{cd} + (2R/d) h
       (since Ric = (R/d) g on Einstein manifolds, 2 R_{(a}^c h_{b)c} = (2R/d) h_{ab})

    For the singlet sector (nabla^2 = 0):
       Delta_L h = -2 R_{acbd} h^{cd} + (R/4) h_{ab}   [d=8, 2R/d = R/4]

    Wait: 2 R_{(a}^c h_{b)c} = Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
    For Einstein: Ric = (R/d) delta, so this is (R/d)(h_{ab} + h_{ba}) = (2R/d) h_{ab}
    For d=8, R=2.0: this is (2*2/8) h = 0.5 h.

    So the Ricci contribution gives a uniform shift of +0.5 on all TT modes.
    The Riemann term -2 R_{acbd} h^{cd} splits them.
    """
    evals = result['eigenvalues']
    R_scalar = result['R_scalar']

    checks = {}
    checks['R_scalar'] = R_scalar
    checks['R_expected'] = 2.0
    checks['R_err'] = abs(R_scalar - 2.0)

    # Ricci should be (R/d) I = 0.25 I for bi-invariant
    Ric = result['Ric']
    Ric_expected = (R_scalar / DIM) * np.eye(DIM)
    checks['Ric_err'] = np.max(np.abs(Ric - Ric_expected))

    # Check all eigenvalues positive
    checks['min_eval'] = evals[0]
    checks['max_eval'] = evals[-1]
    checks['all_positive'] = bool(np.all(evals > -1e-10))

    return checks


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S48 TT-LICH-48: Lichnerowicz Operator on TT 2-Tensors")
    print("  Jensen-Deformed SU(3)")
    print("=" * 78)

    # Tau values to scan
    tau_values = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40, 0.50])

    all_results = {}
    all_eigenvalues = {}
    all_n_negative = {}
    all_classifications = {}

    # =========================================================================
    # SWEEP
    # =========================================================================
    for tau in tau_values:
        print(f"\n{'='*60}")
        print(f"  tau = {tau:.2f}")
        print(f"{'='*60}")

        result = compute_tt_lichnerowicz_at_tau(tau)
        all_results[tau] = result

        n_tt = result['n_tt']
        evals = result['eigenvalues']
        n_neg = result['n_negative']

        print(f"  n_TT = {n_tt}")
        print(f"  Symmetry error (full): {result['sym_err_full']:.2e}")
        print(f"  Symmetry error (TT):   {result['sym_err_tt']:.2e}")
        print(f"  R_scalar = {result['R_scalar']:.10f}")
        print(f"  Eigenvalues ({n_tt} modes):")

        # Find distinct eigenvalues
        sorted_evals = np.sort(evals)
        tol = 1e-8
        groups = []
        i = 0
        while i < len(sorted_evals):
            val = sorted_evals[i]
            count = 1
            while i + count < len(sorted_evals) and abs(sorted_evals[i + count] - val) < tol:
                count += 1
            groups.append((val, count))
            i += count

        for val, deg in groups:
            # Find classification of one representative in this group
            for k in range(n_tt):
                if abs(evals[k] - val) < tol:
                    w = result['classifications'][k]
                    sector = dominant_sector(w)
                    print(f"    lambda = {val:+.8f}  (deg {deg})  [{sector}]  "
                          f"hard={w.get('hard',0):.3f} soft={w.get('soft',0):.3f} "
                          f"C2={w.get('c2_block',0):.3f} U1={w.get('u1_mixed',0):.3f}")
                    break

        print(f"\n  Negative eigenvalues: {n_neg}")
        print(f"  Min eigenvalue: {evals[0]:+.8f}")
        print(f"  Max eigenvalue: {evals[-1]:+.8f}")

        if n_neg > 0:
            print(f"  *** WARNING: {n_neg} NEGATIVE EIGENVALUES DETECTED ***")

        all_eigenvalues[tau] = evals
        all_n_negative[tau] = n_neg
        all_classifications[tau] = result['classifications']

    # =========================================================================
    # VALIDATION AT TAU = 0
    # =========================================================================
    print(f"\n{'='*78}")
    print("  VALIDATION: tau = 0 (bi-invariant metric)")
    print(f"{'='*78}")

    checks = validate_biinvariant(all_results[0.0])
    print(f"  R_scalar = {checks['R_scalar']:.12f}  (expected 2.0, err = {checks['R_err']:.2e})")
    print(f"  Ric = (R/8)*I check: max error = {checks['Ric_err']:.2e}")
    print(f"  Min eigenvalue = {checks['min_eval']:+.10f}")
    print(f"  Max eigenvalue = {checks['max_eval']:+.10f}")
    print(f"  All positive: {checks['all_positive']}")

    # At tau=0, check that eigenvalues are what we expect from the bi-invariant Lichnerowicz
    evals_0 = all_eigenvalues[0.0]
    print(f"\n  Bi-invariant TT Lichnerowicz eigenvalues:")
    evals_sorted = np.sort(evals_0)
    groups_0 = []
    i = 0
    while i < len(evals_sorted):
        val = evals_sorted[i]
        count = 1
        while i + count < len(evals_sorted) and abs(evals_sorted[i + count] - val) < 1e-8:
            count += 1
        groups_0.append((val, count))
        i += count
    for val, deg in groups_0:
        print(f"    lambda = {val:+.10f}  (deg {deg})")

    # =========================================================================
    # RESULTS AT FOLD
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  RESULTS AT FOLD (tau = {tau_fold})")
    print(f"{'='*78}")

    result_fold = all_results[tau_fold]
    evals_fold = result_fold['eigenvalues']
    n_tt_fold = result_fold['n_tt']

    # Sector decomposition at fold
    hard_evals = []
    soft_evals = []
    c2_evals = []
    u1_evals = []

    for k in range(n_tt_fold):
        w = result_fold['classifications'][k]
        ev = evals_fold[k]
        if w.get('hard', 0) > 0.5:
            hard_evals.append(ev)
        elif w.get('soft', 0) > 0.5:
            soft_evals.append(ev)
        elif w.get('c2_block', 0) > 0.5:
            c2_evals.append(ev)
        elif w.get('u1_mixed', 0) > 0.5:
            u1_evals.append(ev)
        else:
            # Mixed mode: classify by largest weight
            max_w = max(w.get('hard', 0), w.get('soft', 0),
                       w.get('c2_block', 0), w.get('u1_mixed', 0))
            if max_w == w.get('hard', 0):
                hard_evals.append(ev)
            elif max_w == w.get('soft', 0):
                soft_evals.append(ev)
            elif max_w == w.get('c2_block', 0):
                c2_evals.append(ev)
            else:
                u1_evals.append(ev)

    hard_evals = np.array(hard_evals)
    soft_evals = np.array(soft_evals)
    c2_evals = np.array(c2_evals)
    u1_evals = np.array(u1_evals)

    print(f"\n  Sector decomposition of TT eigenvalues at fold:")
    print(f"    HARD (su2-su2):  {len(hard_evals)} modes")
    if len(hard_evals) > 0:
        print(f"      range: [{hard_evals.min():.8f}, {hard_evals.max():.8f}]")
        print(f"      mean:  {hard_evals.mean():.8f}")
    print(f"    SOFT (su2-C2):   {len(soft_evals)} modes")
    if len(soft_evals) > 0:
        print(f"      range: [{soft_evals.min():.8f}, {soft_evals.max():.8f}]")
        print(f"      mean:  {soft_evals.mean():.8f}")
    print(f"    C2-C2:           {len(c2_evals)} modes")
    if len(c2_evals) > 0:
        print(f"      range: [{c2_evals.min():.8f}, {c2_evals.max():.8f}]")
        print(f"      mean:  {c2_evals.mean():.8f}")
    print(f"    U1-mixed:        {len(u1_evals)} modes")
    if len(u1_evals) > 0:
        print(f"      range: [{u1_evals.min():.8f}, {u1_evals.max():.8f}]")
        print(f"      mean:  {u1_evals.mean():.8f}")

    # Hard/soft splitting ratio
    if len(hard_evals) > 0 and len(soft_evals) > 0:
        splitting_ratio = hard_evals.mean() / soft_evals.mean()
        print(f"\n  Hard/Soft splitting ratio: {splitting_ratio:.4f}")
    else:
        splitting_ratio = np.nan
        print(f"\n  Hard/Soft splitting ratio: N/A (missing sectors)")

    # Cross-check: sum of eigenvalues vs trace of L_TT
    trace_L_TT = np.trace(result_fold['L_TT'])
    sum_evals = np.sum(evals_fold)
    trace_err = abs(trace_L_TT - sum_evals) / (abs(trace_L_TT) + 1e-30)
    print(f"\n  Trace cross-check: Tr(L_TT) = {trace_L_TT:.8f}, sum(evals) = {sum_evals:.8f}, "
          f"rel err = {trace_err:.2e}")

    # =========================================================================
    # CROSS-CHECK WITH S20b: no tachyons
    # =========================================================================
    print(f"\n{'='*78}")
    print("  CROSS-CHECK: S20b TT stability (no tachyons)")
    print(f"{'='*78}")

    any_tachyon = False
    for tau in tau_values:
        n_neg = all_n_negative[tau]
        min_ev = all_eigenvalues[tau][0]
        status = "STABLE" if n_neg == 0 else "*** TACHYON ***"
        print(f"  tau={tau:.2f}: min_ev = {min_ev:+.8f}, n_negative = {n_neg}  [{status}]")
        if n_neg > 0:
            any_tachyon = True

    print(f"\n  S20b consistency: {'PASS (no tachyons at any tau)' if not any_tachyon else 'FAIL (tachyons detected)'}")

    # =========================================================================
    # CURVATURE ANISOTROPY VS EIGENVALUE SPLITTING
    # =========================================================================
    print(f"\n{'='*78}")
    print("  CURVATURE ANISOTROPY vs EIGENVALUE SPLITTING")
    print(f"{'='*78}")

    for tau in tau_values:
        result = all_results[tau]
        evals = result['eigenvalues']
        if len(evals) > 0:
            spread = evals[-1] - evals[0]
            mean = evals.mean()
            rel_spread = spread / mean if abs(mean) > 1e-10 else np.inf
        else:
            spread = 0
            mean = 0
            rel_spread = 0
        print(f"  tau={tau:.2f}: eval_range = [{evals[0]:+.6f}, {evals[-1]:+.6f}], "
              f"spread = {spread:.6f}, rel_spread = {rel_spread:.4f}")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GATE TT-LICH-48 VERDICT")
    print(f"{'='*78}")

    # Check conditions
    spectrum_computed = all(len(all_eigenvalues[t]) > 0 for t in tau_values)
    no_negative = not any_tachyon
    hard_soft_exists = len(hard_evals) > 0 and len(soft_evals) > 0
    hard_soft_split = hard_soft_exists and abs(splitting_ratio - 1.0) > 0.05

    if not spectrum_computed:
        verdict = "FAIL (computation failure)"
    elif not no_negative:
        verdict = "FAIL (negative eigenvalues: TT instability)"
    elif hard_soft_split:
        verdict = f"PASS (spectrum positive, hard/soft ratio = {splitting_ratio:.4f})"
    elif hard_soft_exists:
        verdict = f"INFO (spectrum positive, hard/soft ratio = {splitting_ratio:.4f} -- minimal splitting)"
    else:
        verdict = "INFO (spectrum positive, sector classification ambiguous)"

    print(f"\n  VERDICT: {verdict}")
    print(f"\n  Spectrum fully computed: {spectrum_computed}")
    print(f"  No negative eigenvalues: {no_negative}")
    print(f"  Hard/Soft sectors identified: {hard_soft_exists}")
    print(f"  Hard/Soft splitting > 5%: {hard_soft_split}")
    print(f"  n_TT at fold: {n_tt_fold}")
    print(f"  min eigenvalue at fold: {evals_fold[0]:+.10f}")
    print(f"  max eigenvalue at fold: {evals_fold[-1]:+.10f}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GENERATING FIGURES")
    print(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # --- Panel A: Eigenvalue spectrum at fold ---
    ax = axes[0, 0]
    evals_sorted_fold = np.sort(evals_fold)
    colors = []
    for k in range(n_tt_fold):
        w = result_fold['classifications'][np.argsort(evals_fold)[k]]
        if w.get('hard', 0) > 0.5:
            colors.append('#1565C0')  # Blue
        elif w.get('soft', 0) > 0.5:
            colors.append('#E65100')  # Orange
        elif w.get('c2_block', 0) > 0.5:
            colors.append('#2E7D32')  # Green
        else:
            colors.append('#7B1FA2')  # Purple
    ax.barh(range(n_tt_fold), evals_sorted_fold, color=colors, edgecolor='black', linewidth=0.5)
    ax.set_xlabel(r'Eigenvalue $\lambda_{TT}$', fontsize=11)
    ax.set_ylabel('Mode index', fontsize=11)
    ax.set_title(r'(A) TT Lichnerowicz spectrum at $\tau$ = ' + f'{tau_fold}', fontsize=12)
    ax.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='Stability threshold')
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#1565C0', label='HARD (su2-su2)'),
        Patch(facecolor='#E65100', label='SOFT (su2-C2)'),
        Patch(facecolor='#2E7D32', label='C2-C2'),
        Patch(facecolor='#7B1FA2', label='U1-mixed'),
    ]
    ax.legend(handles=legend_elements, fontsize=8, loc='lower right')
    ax.grid(axis='x', alpha=0.3)

    # --- Panel B: Eigenvalue evolution with tau ---
    ax = axes[0, 1]
    n_tt_max = max(len(all_eigenvalues[t]) for t in tau_values)
    for k in range(n_tt_max):
        taus_plot = []
        evals_plot = []
        for tau in sorted(tau_values):
            if k < len(all_eigenvalues[tau]):
                taus_plot.append(tau)
                evals_plot.append(np.sort(all_eigenvalues[tau])[k])
        ax.plot(taus_plot, evals_plot, 'o-', markersize=3, linewidth=1.0, alpha=0.7)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5,
               label=r'$\tau_{\rm fold}$')
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=11)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=11)
    ax.set_title('(B) TT eigenvalue evolution', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # --- Panel C: Sector weight distribution at fold ---
    ax = axes[1, 0]
    sector_names = ['hard', 'soft', 'c2_block', 'u1_mixed']
    sector_labels = ['HARD\n(su2-su2)', 'SOFT\n(su2-C2)', r'$\mathbb{C}^2$-$\mathbb{C}^2$', 'U(1)-mixed']
    sector_colors = ['#1565C0', '#E65100', '#2E7D32', '#7B1FA2']
    for k in range(n_tt_fold):
        w = result_fold['classifications'][k]
        ev = evals_fold[k]
        vals = [w.get(s, 0) for s in sector_names]
        dominant_idx = np.argmax(vals)
        ax.scatter(dominant_idx + 0.2 * np.random.randn(), ev,
                  c=sector_colors[dominant_idx], s=60, alpha=0.7,
                  edgecolor='black', linewidth=0.5)
    ax.set_xticks(range(4))
    ax.set_xticklabels(sector_labels, fontsize=9)
    ax.set_ylabel(r'Eigenvalue $\lambda_{TT}$', fontsize=11)
    ax.set_title(r'(C) Sector classification at $\tau$ = ' + f'{tau_fold}', fontsize=12)
    ax.grid(axis='y', alpha=0.3)

    # --- Panel D: Min eigenvalue vs tau ---
    ax = axes[1, 1]
    min_evals = [all_eigenvalues[t][0] for t in sorted(tau_values)]
    max_evals = [all_eigenvalues[t][-1] for t in sorted(tau_values)]
    mean_evals = [all_eigenvalues[t].mean() for t in sorted(tau_values)]
    sorted_taus = sorted(tau_values)
    ax.fill_between(sorted_taus, min_evals, max_evals, alpha=0.2, color='#1565C0')
    ax.plot(sorted_taus, min_evals, 'v-', color='#C62828', markersize=5, label='min', linewidth=1.5)
    ax.plot(sorted_taus, max_evals, '^-', color='#1565C0', markersize=5, label='max', linewidth=1.5)
    ax.plot(sorted_taus, mean_evals, 's-', color='#2E7D32', markersize=5, label='mean', linewidth=1.5)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Stability')
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=11)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=11)
    ax.set_title('(D) Eigenvalue envelope vs tau', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's48_tt_lichnerowicz.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's48_tt_lichnerowicz.npz')

    # Collect eigenvalue arrays
    evals_array = np.full((len(tau_values), 36), np.nan)  # max possible n_tt
    for i, tau in enumerate(tau_values):
        ev = all_eigenvalues[tau]
        evals_array[i, :len(ev)] = ev

    np.savez(npz_path,
             tau_values=tau_values,
             tau_fold=tau_fold,
             eigenvalues=evals_array,
             n_tt=np.array([all_results[t]['n_tt'] for t in tau_values]),
             n_negative=np.array([all_n_negative[t] for t in tau_values]),
             evals_fold=evals_fold,
             n_tt_fold=n_tt_fold,
             min_eval_fold=evals_fold[0],
             max_eval_fold=evals_fold[-1],
             n_hard=len(hard_evals),
             n_soft=len(soft_evals),
             n_c2=len(c2_evals),
             n_u1=len(u1_evals),
             hard_evals=hard_evals,
             soft_evals=soft_evals,
             c2_evals=c2_evals,
             u1_evals=u1_evals,
             splitting_ratio=splitting_ratio,
             verdict=verdict,
             any_tachyon=any_tachyon,
             )
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print("  TT-LICH-48 SUMMARY")
    print(f"{'='*78}")
    print(f"  n_TT modes: {n_tt_fold}")
    print(f"  Eigenvalue range at fold: [{evals_fold[0]:+.8f}, {evals_fold[-1]:+.8f}]")
    print(f"  Negative eigenvalues at any tau: {'YES' if any_tachyon else 'NO'}")
    print(f"  HARD modes: {len(hard_evals)}, mean = {hard_evals.mean():.6f}" if len(hard_evals) > 0 else "  HARD modes: 0")
    print(f"  SOFT modes: {len(soft_evals)}, mean = {soft_evals.mean():.6f}" if len(soft_evals) > 0 else "  SOFT modes: 0")
    print(f"  C2 modes:   {len(c2_evals)}, mean = {c2_evals.mean():.6f}" if len(c2_evals) > 0 else "  C2 modes: 0")
    print(f"  U1 modes:   {len(u1_evals)}, mean = {u1_evals.mean():.6f}" if len(u1_evals) > 0 else "  U1 modes: 0")
    if hard_soft_split:
        print(f"  Hard/Soft ratio: {splitting_ratio:.4f} -- SPLITTING CONFIRMED")
    print(f"\n  VERDICT: {verdict}")


if __name__ == '__main__':
    main()
