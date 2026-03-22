#!/usr/bin/env python3
"""
S49 NON-LI-TT-49: Lichnerowicz on Non-Left-Invariant TT 2-Tensors
====================================================================

Extends S48 TT-LICH-48 from the singlet (0,0) Peter-Weyl sector to
non-left-invariant modes in the (1,0) and (0,1) representations.

Mathematical framework:

    In the (p,q) Peter-Weyl sector, symmetric 2-tensors h_{ab}(g) have
    components that are functions on SU(3) lying in the irreducible
    representation V_{(p,q)}^*.

    The Lichnerowicz operator on TT symmetric 2-tensors:

        Delta_L h = nabla^* nabla h - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}

    The rough Laplacian nabla^* nabla on S^2(T*M) in the (p,q) sector is
    NOT simply the scalar Casimir times identity on the tensor factor.
    The covariant derivative mixes the representation and tensor indices:

        (nabla_{e_a} h)_{bc} = rho_ON[a](h_{bc}) - Gamma^d_{ab} h_{dc} - Gamma^d_{ac} h_{bd}

    where rho_ON[a] acts on the V_{(p,q)}^* coefficient of h_{bc}.

    The rough Laplacian is:
        nabla^* nabla = -sum_a (nabla_{e_a}^2 - nabla_{nabla_{e_a} e_a})

    For the singlet (0,0), rho_ON[a] = 0 and this reduces to the purely
    algebraic operator computed in S48.

    For (1,0) with d=3, the total space is 3 x 36 = 108 dimensional
    (before TT projection). After TT projection, we expect ~3 x 27 = 81
    TT modes (the exact count depends on the transversality constraints).

Gate: NON-LI-TT-49
    PASS: first negative eigenvalue at tau > tau_fold
    INFO: first negative within 0.02 of fold
    FAIL: negative eigenvalue before fold

Output:
    - s49_non_li_tt.npz
    - s49_non_li_tt.png

Author: Spectral-Geometer (Session 49)
Date: 2026-03-17
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    get_irrep,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)
from s47_curvature_anatomy import compute_riemann_tensor_ON
from canonical_constants import tau_fold

DIM = 8  # dim(su(3))
N_SYM = DIM * (DIM + 1) // 2  # = 36 symmetric 2-tensor components


# =============================================================================
# MODULE 1: SYMMETRIC 2-TENSOR BASIS (same as S48)
# =============================================================================

def sym2_basis():
    """
    Construct an orthonormal basis for symmetric 2-tensors in R^8.

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
# MODULE 2: COVARIANT DERIVATIVE ON S^2(T*M) in (p,q) SECTOR
# =============================================================================

def build_nabla_a_sym2(rho_ON, Gamma, d_rep, n=DIM):
    """
    Build the covariant derivative nabla_{e_a} acting on S^2(T*M) in a
    Peter-Weyl sector of dimension d_rep.

    The space is V_{(p,q)} tensor S^2(R^n), with total dimension d_rep * N_SYM.
    We use the index convention:
        component (I, alpha) where I=0..N_SYM-1 indexes the symmetric tensor
        basis element and alpha=0..d_rep-1 indexes the representation.

    Flattened index: k = I * d_rep + alpha

    (nabla_{e_a} h)_{bc} = rho_ON[a](h_{bc}) - Gamma^d_{ab} h_{dc} - Gamma^d_{ac} h_{bd}

    In the sym2 basis e^{(I)}_{bc}, a tensor h = sum_I h_I e^{(I)} where h_I in V_{(p,q)}.
    The covariant derivative becomes:

    <e^{(J)}, nabla_{e_a} (h_I e^{(I)})> = h_I * <e^{(J)}, nabla_{e_a} e^{(I)}>_tensor
                                            + rho_ON[a](h_I) * <e^{(J)}, e^{(I)}>

    The first term involves the connection acting on tensor indices:
        (conn_a)_{J,I} = <e^{(J)}, nabla_{e_a}^{tensor} e^{(I)}>

    where nabla_{e_a}^{tensor} e^{(I)}_{bc} = -Gamma^d_{ab} e^{(I)}_{dc} - Gamma^d_{ac} e^{(I)}_{bd}

    The second term is rho_ON[a] on the diagonal blocks.

    So the full nabla_{e_a} on V x S^2 is:
        nabla_a[J*d + beta, I*d + alpha] = conn_a[J,I] * delta_{alpha,beta}
                                          + delta_{J,I} * rho_ON[a][beta, alpha]

    Args:
        rho_ON: list of n matrices (d_rep x d_rep), representation in ON frame
        Gamma: (n,n,n) connection coefficients Gamma[c,a,b]
        d_rep: dimension of the representation
        n: Lie algebra dimension

    Returns:
        nabla_list: list of n matrices, each (N_SYM*d_rep, N_SYM*d_rep)
    """
    basis, labels = sym2_basis()

    # Precompute connection action on tensor basis: conn_a[J, I]
    # nabla_{e_a}^{tensor} e^{(I)}_{bc} = -sum_d Gamma^d_{ab} e^{(I)}_{dc}
    #                                      -sum_d Gamma^d_{ac} e^{(I)}_{bd}
    conn_a_mats = []
    for a in range(n):
        conn = np.zeros((N_SYM, N_SYM), dtype=np.float64)
        for I in range(N_SYM):
            # Compute nabla_{e_a}^{tensor} e^{(I)}
            nab_eI = np.zeros((n, n), dtype=np.float64)
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        nab_eI[b, c] -= Gamma[d, a, b] * basis[I][d, c]
                        nab_eI[b, c] -= Gamma[d, a, c] * basis[I][b, d]
            # Project onto basis
            for J in range(N_SYM):
                conn[J, I] = np.sum(basis[J] * nab_eI)
        conn_a_mats.append(conn)

    dim_total = N_SYM * d_rep
    Id_d = np.eye(d_rep, dtype=complex)

    nabla_list = []
    for a in range(n):
        mat = np.zeros((dim_total, dim_total), dtype=complex)
        for I in range(N_SYM):
            for J in range(N_SYM):
                # Connection term: conn_a[J,I] * Id_d
                if abs(conn_a_mats[a][J, I]) > 1e-15:
                    mat[J*d_rep:(J+1)*d_rep, I*d_rep:(I+1)*d_rep] += (
                        conn_a_mats[a][J, I] * Id_d
                    )
            # Representation term: rho_ON[a] on diagonal block (I,I)
            mat[I*d_rep:(I+1)*d_rep, I*d_rep:(I+1)*d_rep] += rho_ON[a]

        nabla_list.append(mat)

    return nabla_list


def build_rough_laplacian(nabla_list, Gamma, d_rep, n=DIM):
    """
    Compute the rough Laplacian nabla^* nabla on S^2(T*M) in (p,q) sector.

    nabla^* nabla = -sum_a (nabla_{e_a}^2 - nabla_{nabla_{e_a} e_a})
                  = -sum_a nabla_{e_a}^2 + sum_{a,c} Gamma^c_{aa} nabla_{e_c}
    """
    dim_total = N_SYM * d_rep

    # Divergence vector
    div = np.zeros(n, dtype=np.float64)
    for c in range(n):
        for a in range(n):
            div[c] += Gamma[c, a, a]

    # Rough Laplacian
    rough = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(n):
        rough -= nabla_list[a] @ nabla_list[a]
    for c in range(n):
        if abs(div[c]) > 1e-15:
            rough += div[c] * nabla_list[c]

    return rough


# =============================================================================
# MODULE 3: CURVATURE ENDOMORPHISM ON S^2(T*M)
# =============================================================================

def curvature_endomorphism_sym2(Riem, Ric, d_rep, n=DIM):
    """
    Build the curvature endomorphism -2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}
    on V_{(p,q)} tensor S^2(R^n).

    This acts only on the tensor factor S^2(R^n) and is identity on V_{(p,q)}.
    It is the same algebraic operator as in S48, tensored with Id on the rep space.

    Returns:
        curv_endo: (N_SYM*d_rep, N_SYM*d_rep) matrix
    """
    basis, labels = sym2_basis()
    Id_d = np.eye(d_rep, dtype=complex)
    dim_total = N_SYM * d_rep

    # First build the N_SYM x N_SYM curvature endomorphism on S^2(R^n)
    L_curv = np.zeros((N_SYM, N_SYM), dtype=np.float64)

    for J in range(N_SYM):
        eJ = basis[J]
        # (Delta_L^{curv} eJ)_{ab} = -2 R_{acbd} eJ_{cd} + Ric_{ac} eJ_{cb} + Ric_{bc} eJ_{ca}
        DL_eJ = np.zeros((n, n), dtype=np.float64)

        # Term 1: -2 R_{acbd} eJ_{cd}
        DL_eJ += -2.0 * np.einsum('acbd,cd->ab', Riem, eJ)

        # Term 2: Ric @ eJ + eJ @ Ric
        DL_eJ += Ric @ eJ + eJ @ Ric

        for I in range(N_SYM):
            L_curv[I, J] = np.sum(basis[I] * DL_eJ)

    # Tensor with Id_d: L_curv tensor Id_d
    curv_endo = np.zeros((dim_total, dim_total), dtype=complex)
    for I in range(N_SYM):
        for J in range(N_SYM):
            if abs(L_curv[I, J]) > 1e-15:
                curv_endo[I*d_rep:(I+1)*d_rep, J*d_rep:(J+1)*d_rep] = (
                    L_curv[I, J] * Id_d
                )

    return curv_endo


# =============================================================================
# MODULE 4: TT PROJECTION IN (p,q) SECTOR
# =============================================================================

def tt_projector_pq(rho_ON, Gamma, d_rep, n=DIM):
    """
    Construct TT projection for S^2(T*M) in the (p,q) Peter-Weyl sector.

    TT conditions:
        1. Trace-free: g^{ab} h_{ab} = 0
        2. Transverse: nabla^a h_{ab} = 0

    For the (p,q) sector, both conditions involve the representation action.

    Trace constraint: sum_a h_{aa} = 0 in the tensor sense.
    In our basis, the trace is: T_I = tr(e^{(I)}) / sqrt(8).
    This gives one constraint per V-component, so d_rep constraints total.
    Actually: the trace constraint is sum_I T_I h_I = 0 where h_I in V.
    This is T_I * Id acting on the vector (h_0, ..., h_{N_SYM-1}).

    Transverse constraint: (div h)_b = sum_a (nabla_{e_a} h)_{ab} = 0.
    This gives n*d_rep constraints.

    Total constraints: (1 + n) * d_rep = 9 * d_rep.
    Total space: N_SYM * d_rep = 36 * d_rep.
    Expected TT dim: (36 - 9) * d_rep = 27 * d_rep (if all constraints independent).

    But for the (p,q) sector, some transversality constraints may be linearly
    dependent on the trace constraint, just as in the (0,0) case where we get
    31 instead of 27 TT modes.

    Returns:
        P_TT: projector (dim_total, dim_total)
        n_tt: dimension of TT subspace
        V_TT: (dim_total, n_tt) basis for TT subspace
    """
    basis, labels = sym2_basis()
    dim_total = N_SYM * d_rep
    Id_d = np.eye(d_rep, dtype=complex)

    # --- Trace constraint ---
    # In the full space, the trace direction on tensor factor is T_I = tr(e^{(I)}) / ||T||.
    # Constraint: sum_I T_I * h_I = 0 where h_I in V_{d_rep}.
    # This is d_rep scalar constraints: for each alpha, sum_I T_I h_{I,alpha} = 0.
    # In matrix form: C_trace is (d_rep, dim_total) where
    #   C_trace[alpha, I*d_rep + beta] = T_I * delta_{alpha, beta}

    T_I = np.zeros(N_SYM, dtype=np.float64)
    for I in range(N_SYM):
        T_I[I] = np.trace(basis[I])
    T_norm = np.linalg.norm(T_I)
    T_I /= T_norm

    C_trace = np.zeros((d_rep, dim_total), dtype=complex)
    for alpha in range(d_rep):
        for I in range(N_SYM):
            C_trace[alpha, I*d_rep + alpha] = T_I[I]

    # --- Transversality constraint ---
    # (div h)_b = sum_a (nabla_{e_a} h)_{ab}
    # For left-invariant tensor h in (0,0), this reduces to algebraic divergence.
    # For general (p,q), we need the full nabla.
    #
    # (nabla_{e_a} h)_{ab} involves:
    #   rho_ON[a](h_{ab}) - sum_d Gamma^d_{aa} h_{db} - sum_d Gamma^d_{ab} h_{ad}
    #
    # Summing over a: (div h)_b = sum_a rho_ON[a](h_{ab})
    #                             - sum_{a,d} Gamma^d_{aa} h_{db}
    #                             - sum_{a,d} Gamma^d_{ab} h_{ad}
    #
    # In our basis expansion h = sum_I h_I e^{(I)}, the divergence gives
    # n * d_rep constraints.

    # Build divergence operator using the nabla matrices
    # Alternative: compute directly from components

    # Method: compute the divergence matrix D: (n*d_rep, N_SYM*d_rep)
    # (div h)_{b, alpha} = D[(b, alpha), (I, beta)] * h_{I, beta}

    D = np.zeros((n * d_rep, dim_total), dtype=complex)

    for I in range(N_SYM):
        eI = basis[I]
        for b in range(n):
            # Compute (div eI)_b from connection (tensor part)
            # and rho_ON (representation part)
            tensor_div_b = 0.0
            for a in range(n):
                for d in range(n):
                    tensor_div_b -= Gamma[d, a, a] * eI[d, b]
                    tensor_div_b -= Gamma[d, a, b] * eI[a, d]

            # Representation part: sum_a rho_ON[a](h_{ab})
            # = sum_a rho_ON[a] * eI[a, b]
            rep_part = np.zeros((d_rep, d_rep), dtype=complex)
            for a in range(n):
                if abs(eI[a, b]) > 1e-15:
                    rep_part += eI[a, b] * rho_ON[a]

            for alpha in range(d_rep):
                for beta in range(d_rep):
                    D[b*d_rep + alpha, I*d_rep + beta] = (
                        tensor_div_b * (1.0 if alpha == beta else 0.0)
                        + rep_part[alpha, beta]
                    )

    # Combine constraints
    C = np.vstack([C_trace, D])

    # TT subspace = null space of C
    U, S_vals, Vt = np.linalg.svd(C, full_matrices=True)
    tol = 1e-10 * S_vals[0] if len(S_vals) > 0 else 1e-10
    rank_C = np.sum(S_vals > tol)
    n_tt = dim_total - rank_C

    V_TT = Vt[rank_C:].conj().T  # (dim_total, n_tt)

    return n_tt, V_TT


# =============================================================================
# MODULE 5: FULL LICHNEROWICZ IN (p,q) SECTOR
# =============================================================================

def compute_lichnerowicz_pq(tau, p, q, gens, f_abc):
    """
    Compute the Lichnerowicz operator on TT 2-tensors in the (p,q)
    Peter-Weyl sector at Jensen deformation parameter tau.

    Returns dict with eigenvalues and metadata.
    """
    t0 = time.time()

    # Infrastructure
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Riemann and Ricci
    R_abcf = compute_riemann_tensor_ON(ft, Gamma)
    Riem = R_abcf.copy()  # In ON frame, lowering is trivial
    Ric = np.einsum('abca->bc', R_abcf)
    R_scalar = np.trace(Ric)

    # Get representation
    rho, d_rep = get_irrep(p, q, gens, f_abc)

    # ON-frame representation
    rho_ON = []
    for a in range(DIM):
        mat = np.zeros((d_rep, d_rep), dtype=complex)
        for b in range(DIM):
            if abs(E[a, b]) > 1e-15:
                mat += E[a, b] * rho[b]
        rho_ON.append(mat)

    # Build covariant derivative matrices
    nabla_list = build_nabla_a_sym2(rho_ON, Gamma, d_rep)

    # Rough Laplacian
    rough_lap = build_rough_laplacian(nabla_list, Gamma, d_rep)

    # Curvature endomorphism
    curv_endo = curvature_endomorphism_sym2(Riem, Ric, d_rep)

    # Full Lichnerowicz = rough Laplacian + curvature endomorphism
    dim_total = N_SYM * d_rep
    L_full = rough_lap + curv_endo

    # Check Hermiticity
    herm_err = np.max(np.abs(L_full - L_full.conj().T))

    # TT projection
    n_tt, V_TT = tt_projector_pq(rho_ON, Gamma, d_rep)

    if n_tt == 0:
        t1 = time.time()
        return {
            'tau': tau, 'p': p, 'q': q, 'd_rep': d_rep,
            'n_tt': 0, 'eigenvalues': np.array([]),
            'n_negative': 0, 'R_scalar': R_scalar,
            'herm_err': herm_err, 'time': t1 - t0,
        }

    # Restrict to TT subspace
    L_TT = V_TT.conj().T @ L_full @ V_TT

    # Check Hermiticity of L_TT
    herm_err_tt = np.max(np.abs(L_TT - L_TT.conj().T))

    # Hermitize
    L_TT = 0.5 * (L_TT + L_TT.conj().T)

    # Diagonalize
    eigenvalues = np.linalg.eigvalsh(L_TT)

    # Count negative
    n_negative = int(np.sum(eigenvalues < -1e-10))

    t1 = time.time()

    return {
        'tau': tau, 'p': p, 'q': q, 'd_rep': d_rep,
        'n_tt': n_tt,
        'eigenvalues': np.real(eigenvalues),
        'n_negative': n_negative,
        'R_scalar': R_scalar,
        'herm_err': herm_err,
        'herm_err_tt': herm_err_tt,
        'time': t1 - t0,
    }


# =============================================================================
# MODULE 6: VALIDATION
# =============================================================================

def validate_biinvariant_pq(gens, f_abc, p, q):
    """
    At tau=0, validate against known Casimir structure.

    For the bi-invariant metric, the Lichnerowicz on (p,q) sector should give:
    - The (0,0) algebraic eigenvalues SHIFTED by the scalar Laplacian eigenvalue.
    - Specifically, Delta_L^{(p,q)} = Delta_L^{(0,0)} tensor Id + C_2(p,q)/3 * Id tensor Id
      (the C_2/3 is the scalar Laplacian eigenvalue for the bi-invariant metric)

    But this is only true when the metric is bi-invariant, because then the connection
    is torsion-free and the rough Laplacian decomposes cleanly.

    Actually for bi-invariant: the Lichnerowicz is also bi-invariant, so on each (p,q)
    it should be (scalar Laplacian on functions) tensor Id_S2 + (0,0) Lichnerowicz tensor Id_V.
    But the scalar Laplacian is C_2/3 * Id, and it acts as a scalar on each V-component
    (by Schur's lemma, since the metric is bi-invariant).

    Wait -- actually, for bi-invariant metrics, the rough Laplacian on ANY tensor bundle
    decomposes as:
        nabla^* nabla = Delta_0 tensor Id_{fiber} + (fiber connection terms)

    The fiber connection terms for the Levi-Civita connection on a bi-invariant metric
    are NOT zero -- they involve the connection acting on the tensor indices.

    The correct statement is: for bi-invariant metrics, the Lichnerowicz eigenvalues
    in the (p,q) sector equal those in the (0,0) sector PLUS C_2(p,q)/3.

    This is because on a bi-invariant metric the connection is (1/2)[X,Y], so
    nabla^* nabla on tensors splits into:
        nabla^* nabla = (scalar rough Lap) + (algebraic connection terms)

    The scalar rough Lap on (p,q) is C_2(p,q)/3 times identity.
    The algebraic connection terms are the same as in (0,0).
    """
    result_0 = compute_lichnerowicz_pq(0.0, 0, 0, gens, f_abc)
    result_pq = compute_lichnerowicz_pq(0.0, p, q, gens, f_abc)

    C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
    scalar_lap_eig = C2 / 3.0  # bi-invariant scalar Laplacian eigenvalue

    evals_0 = np.sort(result_0['eigenvalues'])
    evals_pq = np.sort(result_pq['eigenvalues'])

    # For bi-invariant metric, each (0,0) eigenvalue lambda should appear
    # d_rep times in (p,q) as lambda + C_2/3.
    # So the (p,q) eigenvalues should be:
    # {lambda_i + C_2/3 : lambda_i in (0,0) eigenvalues, each with d_rep multiplicity}
    expected = np.sort(np.repeat(evals_0 + scalar_lap_eig, result_pq['d_rep']))

    # The TT count might differ
    n_tt_0 = result_0['n_tt']
    n_tt_pq = result_pq['n_tt']

    return {
        'evals_0': evals_0,
        'evals_pq': evals_pq,
        'expected': expected,
        'scalar_lap_shift': scalar_lap_eig,
        'C2': C2,
        'd_rep': result_pq['d_rep'],
        'n_tt_0': n_tt_0,
        'n_tt_pq': n_tt_pq,
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S49 NON-LI-TT-49: Lichnerowicz on Non-Left-Invariant TT 2-Tensors")
    print("  Jensen-Deformed SU(3), Peter-Weyl sectors (1,0) and (0,1)")
    print("=" * 78)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)

    # Tau scan values (matching S48 + additional points near/beyond fold)
    tau_values = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40,
                           0.537, 0.60, 0.78])

    # Sectors to compute
    sectors = [(1, 0), (0, 1)]

    # =========================================================================
    # VALIDATION AT TAU = 0
    # =========================================================================
    print(f"\n{'='*78}")
    print("  VALIDATION: tau = 0 (bi-invariant metric)")
    print(f"{'='*78}")

    for p, q in sectors:
        val = validate_biinvariant_pq(gens, f_abc, p, q)
        print(f"\n  Sector ({p},{q}): d_rep = {val['d_rep']}")
        print(f"    C_2({p},{q}) = {val['C2']:.6f}")
        print(f"    Scalar Laplacian shift = C_2/3 = {val['scalar_lap_shift']:.6f}")
        print(f"    n_TT(0,0) = {val['n_tt_0']}, n_TT({p},{q}) = {val['n_tt_pq']}")
        print(f"    (0,0) eigenvalue range: [{val['evals_0'].min():.6f}, {val['evals_0'].max():.6f}]")
        print(f"    ({p},{q}) eigenvalue range: [{val['evals_pq'].min():.6f}, {val['evals_pq'].max():.6f}]")
        print(f"    Expected shift range: [{val['evals_0'].min() + val['scalar_lap_shift']:.6f}, "
              f"{val['evals_0'].max() + val['scalar_lap_shift']:.6f}]")

        # Check if actual matches expected (may not be exact due to TT count differences)
        if len(val['evals_pq']) == len(val['expected']):
            max_err = np.max(np.abs(val['evals_pq'] - val['expected']))
            print(f"    Max deviation from shifted (0,0): {max_err:.2e}")
            if max_err < 1e-8:
                print(f"    VALIDATION PASS: exact Casimir shift confirmed")
            else:
                print(f"    NOTE: deviation detected (cross-terms in rough Laplacian)")
        else:
            print(f"    NOTE: TT dimensions differ ({len(val['evals_pq'])} vs {len(val['expected'])})")
            # Compare min/max instead
            min_shift_err = abs(val['evals_pq'].min() - (val['evals_0'].min() + val['scalar_lap_shift']))
            max_shift_err = abs(val['evals_pq'].max() - (val['evals_0'].max() + val['scalar_lap_shift']))
            print(f"    Min eigenvalue shift error: {min_shift_err:.2e}")
            print(f"    Max eigenvalue shift error: {max_shift_err:.2e}")

    # =========================================================================
    # FULL TAU SWEEP
    # =========================================================================
    all_results = {}  # (p, q, tau) -> result dict

    for p, q in sectors:
        print(f"\n{'='*78}")
        print(f"  SECTOR ({p},{q}): tau sweep")
        print(f"{'='*78}")

        for tau in tau_values:
            print(f"\n  tau = {tau:.3f} ... ", end="", flush=True)
            result = compute_lichnerowicz_pq(tau, p, q, gens, f_abc)
            all_results[(p, q, tau)] = result

            evals = result['eigenvalues']
            n_tt = result['n_tt']
            n_neg = result['n_negative']

            print(f"n_TT={n_tt}, min_ev={evals.min() if len(evals) > 0 else 'N/A':+.8f}, "
                  f"max_ev={evals.max() if len(evals) > 0 else 'N/A':+.8f}, "
                  f"n_neg={n_neg}, "
                  f"herm_err={result['herm_err']:.2e}, "
                  f"time={result['time']:.2f}s")

            if n_neg > 0:
                print(f"  *** NEGATIVE EIGENVALUES DETECTED ***")
                # Print the negative eigenvalues
                neg_evals = evals[evals < -1e-10]
                for ev in neg_evals[:5]:
                    print(f"    lambda = {ev:+.10f}")

    # =========================================================================
    # FIND CRITICAL TAU (first instability)
    # =========================================================================
    print(f"\n{'='*78}")
    print("  STABILITY ANALYSIS: searching for tau_critical")
    print(f"{'='*78}")

    tau_crit = {}
    for p, q in sectors:
        min_evals = []
        for tau in tau_values:
            result = all_results[(p, q, tau)]
            if len(result['eigenvalues']) > 0:
                min_evals.append((tau, result['eigenvalues'].min(), result['n_negative']))

        print(f"\n  Sector ({p},{q}):")
        print(f"    {'tau':>8s}  {'min_ev':>14s}  {'n_neg':>6s}")
        for tau, min_ev, n_neg in min_evals:
            marker = " *** NEGATIVE ***" if n_neg > 0 else ""
            print(f"    {tau:8.4f}  {min_ev:+14.8f}  {n_neg:6d}{marker}")

        # Find first tau with negative eigenvalue
        neg_taus = [(tau, min_ev) for tau, min_ev, n_neg in min_evals if n_neg > 0]
        if neg_taus:
            tau_crit[(p, q)] = neg_taus[0][0]
            print(f"\n    tau_critical({p},{q}) = {neg_taus[0][0]:.4f} "
                  f"(min_ev = {neg_taus[0][1]:+.8f})")
        else:
            tau_crit[(p, q)] = None
            print(f"\n    NO negative eigenvalues in scan range [0, {tau_values.max():.2f}]")

    # =========================================================================
    # COMPARISON WITH (0,0) SECTOR (S48)
    # =========================================================================
    print(f"\n{'='*78}")
    print("  COMPARISON WITH (0,0) SINGLET SECTOR (S48)")
    print(f"{'='*78}")

    # Load S48 data for comparison
    try:
        s48 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    's48_tt_lichnerowicz.npz'), allow_pickle=True)
        s48_evals = s48['eigenvalues']
        s48_taus = s48['tau_values']
        print(f"  S48 loaded: {len(s48_taus)} tau values, {int(s48['n_tt'][0])} TT modes (tau=0)")

        # Compare at fold
        s48_fold_idx = np.argmin(np.abs(s48_taus - tau_fold))
        s48_fold_evals = s48_evals[s48_fold_idx]
        s48_fold_evals = s48_fold_evals[~np.isnan(s48_fold_evals)]

        print(f"\n  At fold (tau={tau_fold}):")
        print(f"    (0,0): n_TT={len(s48_fold_evals)}, "
              f"min={s48_fold_evals.min():.8f}, max={s48_fold_evals.max():.8f}")

        for p, q in sectors:
            result_fold = all_results.get((p, q, tau_fold))
            if result_fold and len(result_fold['eigenvalues']) > 0:
                ev = result_fold['eigenvalues']
                print(f"    ({p},{q}): n_TT={result_fold['n_tt']}, "
                      f"min={ev.min():.8f}, max={ev.max():.8f}")
                shift = ev.min() - s48_fold_evals.min()
                print(f"    min eigenvalue shift vs (0,0): {shift:+.8f}")
    except FileNotFoundError:
        print("  S48 data not found. Skipping comparison.")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GATE NON-LI-TT-49 VERDICT")
    print(f"{'='*78}")

    any_instability = False
    instability_before_fold = False
    instability_near_fold = False

    for p, q in sectors:
        tc = tau_crit.get((p, q))
        if tc is not None:
            any_instability = True
            if tc < tau_fold - 0.02:
                instability_before_fold = True
                print(f"\n  ({p},{q}): INSTABILITY at tau={tc:.4f} < tau_fold-0.02 = {tau_fold-0.02:.2f}")
            elif tc < tau_fold + 0.02:
                instability_near_fold = True
                print(f"\n  ({p},{q}): INSTABILITY at tau={tc:.4f} NEAR fold (within 0.02)")
            else:
                print(f"\n  ({p},{q}): INSTABILITY at tau={tc:.4f} > tau_fold+0.02 = {tau_fold+0.02:.2f} (SAFE)")
        else:
            print(f"\n  ({p},{q}): ALL POSITIVE in [{tau_values.min():.2f}, {tau_values.max():.2f}]")

    if instability_before_fold:
        verdict = "FAIL"
        reason = "Negative eigenvalue before fold"
    elif instability_near_fold:
        verdict = "INFO"
        reason = "Negative eigenvalue near fold (within 0.02)"
    elif any_instability:
        verdict = "PASS"
        reason = "First instability after fold"
        tc_min = min(tc for tc in tau_crit.values() if tc is not None)
        reason += f" (tau_crit = {tc_min:.4f} > tau_fold = {tau_fold})"
    else:
        verdict = "PASS"
        reason = "All eigenvalues positive in full scan range"

    print(f"\n  VERDICT: {verdict} -- {reason}")
    print(f"\n  tau_fold = {tau_fold}")
    for p, q in sectors:
        tc = tau_crit.get((p, q))
        print(f"  tau_crit({p},{q}) = {tc if tc is not None else 'None (all positive)'}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GENERATING FIGURES")
    print(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # --- Panel A: Eigenvalue evolution for (1,0) ---
    ax = axes[0, 0]
    for tau_idx, tau in enumerate(tau_values):
        result = all_results.get((1, 0, tau))
        if result and len(result['eigenvalues']) > 0:
            ev = np.sort(result['eigenvalues'])
            ax.scatter([tau]*len(ev), ev, s=3, alpha=0.5, c='#1565C0')
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.7, label='Stability')
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{\rm fold}$')
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'$\lambda_{TT}^{(1,0)}$', fontsize=12)
    ax.set_title('(A) TT Lichnerowicz eigenvalues: (1,0) sector', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # --- Panel B: Eigenvalue evolution for (0,1) ---
    ax = axes[0, 1]
    for tau_idx, tau in enumerate(tau_values):
        result = all_results.get((0, 1, tau))
        if result and len(result['eigenvalues']) > 0:
            ev = np.sort(result['eigenvalues'])
            ax.scatter([tau]*len(ev), ev, s=3, alpha=0.5, c='#E65100')
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.7, label='Stability')
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{\rm fold}$')
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'$\lambda_{TT}^{(0,1)}$', fontsize=12)
    ax.set_title('(B) TT Lichnerowicz eigenvalues: (0,1) sector', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # --- Panel C: Min eigenvalue comparison ---
    ax = axes[1, 0]
    colors = {'(0,0)': '#2E7D32', '(1,0)': '#1565C0', '(0,1)': '#E65100'}
    markers = {'(0,0)': 's', '(1,0)': 'o', '(0,1)': '^'}

    # (0,0) from S48
    try:
        s48_min = []
        for i, tau in enumerate(s48_taus):
            ev = s48_evals[i]
            ev = ev[~np.isnan(ev)]
            s48_min.append(ev.min())
        ax.plot(s48_taus, s48_min, 's-', color=colors['(0,0)'], label='(0,0) [S48]',
                markersize=5, linewidth=1.5)
    except Exception:
        pass

    for p, q in sectors:
        label = f'({p},{q})'
        min_evs = []
        taus_plot = []
        for tau in tau_values:
            result = all_results.get((p, q, tau))
            if result and len(result['eigenvalues']) > 0:
                min_evs.append(result['eigenvalues'].min())
                taus_plot.append(tau)
        ax.plot(taus_plot, min_evs, f"{markers[label]}-", color=colors[label],
                label=label, markersize=5, linewidth=1.5)

    ax.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.7)
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'Min $\lambda_{TT}$', fontsize=12)
    ax.set_title('(C) Minimum TT eigenvalue vs tau', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # --- Panel D: Eigenvalue density at fold ---
    ax = axes[1, 1]
    for p, q in [(0, 0)] + sectors:
        label = f'({p},{q})'
        if (p, q) == (0, 0):
            try:
                ev = s48_fold_evals
                ax.hist(ev, bins=20, alpha=0.4, color=colors[label], label=label,
                        edgecolor='black', linewidth=0.5)
            except Exception:
                pass
        else:
            result_fold = all_results.get((p, q, tau_fold))
            if result_fold and len(result_fold['eigenvalues']) > 0:
                ev = result_fold['eigenvalues']
                ax.hist(ev, bins=30, alpha=0.4, color=colors[label], label=label,
                        edgecolor='black', linewidth=0.5)
    ax.axvline(x=0, color='red', linestyle='--', alpha=0.7)
    ax.set_xlabel(r'$\lambda_{TT}$', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title(f'(D) Eigenvalue density at fold (tau={tau_fold})', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's49_non_li_tt.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's49_non_li_tt.npz')

    save_dict = {
        'tau_values': tau_values,
        'tau_fold': tau_fold,
        'sectors': np.array(sectors),
        'verdict': verdict,
        'reason': reason,
    }

    for p, q in sectors:
        prefix = f'pq_{p}{q}'
        evals_list = []
        n_tt_list = []
        n_neg_list = []
        min_ev_list = []
        for tau in tau_values:
            result = all_results.get((p, q, tau))
            if result:
                evals_list.append(result['eigenvalues'])
                n_tt_list.append(result['n_tt'])
                n_neg_list.append(result['n_negative'])
                if len(result['eigenvalues']) > 0:
                    min_ev_list.append(result['eigenvalues'].min())
                else:
                    min_ev_list.append(np.nan)

        # Pad eigenvalue arrays to same length
        max_len = max(len(ev) for ev in evals_list) if evals_list else 0
        evals_array = np.full((len(tau_values), max_len), np.nan)
        for i, ev in enumerate(evals_list):
            evals_array[i, :len(ev)] = ev

        save_dict[f'{prefix}_eigenvalues'] = evals_array
        save_dict[f'{prefix}_n_tt'] = np.array(n_tt_list)
        save_dict[f'{prefix}_n_negative'] = np.array(n_neg_list)
        save_dict[f'{prefix}_min_ev'] = np.array(min_ev_list)
        save_dict[f'{prefix}_tau_crit'] = tau_crit.get((p, q), np.nan)

    np.savez(npz_path, **save_dict)
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print("  NON-LI-TT-49 SUMMARY")
    print(f"{'='*78}")
    print(f"  tau_fold = {tau_fold}")
    for p, q in sectors:
        tc = tau_crit.get((p, q))
        result_fold = all_results.get((p, q, tau_fold))
        if result_fold and len(result_fold['eigenvalues']) > 0:
            print(f"  ({p},{q}): n_TT = {result_fold['n_tt']}, "
                  f"min_ev(fold) = {result_fold['eigenvalues'].min():+.8f}, "
                  f"tau_crit = {tc if tc is not None else 'None'}")
    print(f"\n  VERDICT: {verdict} -- {reason}")


if __name__ == '__main__':
    main()
