#!/usr/bin/env python3
"""
S55 LICHNEROWICZ-55: Lichnerowicz Stability at the Jensen Fold
===============================================================

Compute the spectrum of the Lichnerowicz Laplacian Delta_L on G-invariant
TT (transverse-traceless) symmetric 2-tensors at the Jensen metric fold
on SU(3).

Mathematical framework:
    The Lichnerowicz operator on symmetric 2-tensors h_{ab} is:

        (Delta_L h)_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 Ric_{(a}^c h_{b)c}

    In the (0,0) singlet Peter-Weyl sector, -nabla^2 h = C_2(0,0) h = 0
    (Casimir of trivial representation). So Delta_L reduces to the purely
    ALGEBRAIC curvature action:

        (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}

    The space of G-invariant TT tensors on SU(3) with Jensen metric g_tau:
        - dim(Sym^2(R^8)) = 36
        - trace constraint: -1
        - transversality: -8 (generically)
        => n_TT = 27 (generically)

    Stability: all eigenvalues >= 0 => STABLE (no tachyonic TT modes)

Cross-references:
    - S20b: "TT stability: no tachyons at any tau" (different decomposition)
    - S43: 2x2 U(2)-invariant sector, eigenvalues [1.0, 1.0] at tau=0
    - S48: Full 27-dim TT sector, no negatives found
    - Lauret (Paper 37): Universal Lichnerowicz formula
    - Schwahn (Paper 39): Casimir-based formula for normal homogeneous spaces

Gate: LICHNEROWICZ-55
    INFO: stability classification (stable/unstable) and spectrum of Delta_L

Output:
    - s55_lichnerowicz.npz
    - s55_lichnerowicz.png

Author: Baptista Spacetime Analyst (Session 55)
Date: 2026-03-22
"""

import numpy as np
import sys
import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Import from computations
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import tau_fold, PI

# Import from computations/_shared (infrastructure lives there)
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, ARCHIVE_DIR)

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    U1_IDX, SU2_IDX, C2_IDX,
)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
    scalar_curvature_our_metric,
)

DIM = 8  # dim(su(3)) (local)
N_SYM = 36   # dim(Sym^2(R^8)) = 8*9/2


# =============================================================================
# MODULE 1: SYMMETRIC 2-TENSOR BASIS (orthonormal under Frobenius)
# =============================================================================

def sym2_basis():
    """
    Construct an orthonormal basis for Sym^2(R^8) under the Frobenius
    inner product <A, B> = sum_{a,b} A_{ab} B_{ab}.

    For a <= b:
        e_{(a,a)} = delta_{ij} delta_{ia}     (diagonal: norm = 1)
        e_{(a,b)} = (delta_{ia}delta_{jb} + delta_{ib}delta_{ja})/sqrt(2)  (off-diag: norm = 1)

    Returns:
        basis: list of 36 (8,8) arrays
        labels: list of (a,b) pairs
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
# MODULE 2: TT PROJECTION (trace-free + divergence-free)
# =============================================================================

def divergence_operator_matrix(ft, Gamma, basis, labels):
    """
    Compute the divergence operator div: Sym^2 -> R^8 for left-invariant
    tensors on a Lie group in ON frame.

    For left-invariant h, (div h)_b = sum_a nabla_{e_a} h_{ab}.
    Since e_a(h_{bc}) = 0 for left-invariant h:
        nabla_{e_a} h_{ab} = -sum_d Gamma^d_{aa} h_{db} - sum_d Gamma^d_{ab} h_{ad}

    Returns:
        D: (DIM, N_SYM) matrix, (div h)_b = D[b, I] * c_I
    """
    D = np.zeros((DIM, N_SYM), dtype=np.float64)
    for I, eI in enumerate(basis):
        for b in range(DIM):
            val = 0.0  # (local)
            for a in range(DIM):
                for d in range(DIM):
                    val -= Gamma[d, a, a] * eI[d, b]
                    val -= Gamma[d, a, b] * eI[a, d]
            D[b, I] = val
    return D


def tt_projector(ft, Gamma, basis, labels):
    """
    Construct the projector onto the TT (transverse, trace-free) subspace.

    TT = ker(trace) ∩ ker(divergence)

    Returns:
        P_TT: (N_SYM, N_SYM) projector
        n_tt: dimension of TT subspace
        V_TT: (N_SYM, n_tt) ON basis columns for TT subspace
    """
    # Trace constraint vector
    T_vec = np.zeros(N_SYM, dtype=np.float64)
    for I, (a, b) in enumerate(labels):
        T_vec[I] = np.trace(basis[I])

    # Divergence constraint matrix
    D = divergence_operator_matrix(ft, Gamma, basis, labels)

    # Combined constraint: (1 + DIM) x N_SYM = 9 x 36
    C = np.vstack([T_vec.reshape(1, -1), D])

    # TT = null space of C
    U, S, Vt = np.linalg.svd(C, full_matrices=True)
    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10  # (local)
    rank_C = np.sum(S > tol)
    n_tt = N_SYM - rank_C
    V_TT = Vt[rank_C:].T  # (N_SYM, n_tt)

    return V_TT @ V_TT.T, n_tt, V_TT


# =============================================================================
# MODULE 3: LICHNEROWICZ OPERATOR
# =============================================================================

def lichnerowicz_action(Riem, Ric, h):
    """
    Apply the Lichnerowicz operator to symmetric 2-tensor h_{ab}
    (in the singlet sector where nabla^2 = 0).

    (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}

    In ON frame h^{cd} = h_{cd}, so:
        term1_{ab} = -2 * sum_{c,d} R_{acbd} h_{cd}
        term2_{ab} = (Ric @ h + h @ Ric)_{ab}

    Convention: Riem[a,b,c,d] = R_{abcd} from r20a.
    So R_{acbd} = Riem[a,c,b,d].

    Returns:
        DL_h: (DIM, DIM) result
    """
    # Term 1: -2 R_{acbd} h_{cd} = -2 * einsum('acbd,cd->ab', Riem, h)
    term1 = -2.0 * np.einsum('acbd,cd->ab', Riem, h)

    # Term 2: Ric @ h + h @ Ric (symmetrized Ricci coupling)
    term2 = Ric @ h + h @ Ric

    return term1 + term2


def lichnerowicz_matrix(Riem, Ric, basis):
    """
    Matrix representation of Delta_L in the Sym^2 basis.
    L[I,J] = <e_I, Delta_L e_J> = Tr(e_I^T . Delta_L e_J)
    """
    N = len(basis)
    L = np.zeros((N, N), dtype=np.float64)
    for J in range(N):
        DL_eJ = lichnerowicz_action(Riem, Ric, basis[J])
        for I in range(N):
            L[I, J] = np.sum(basis[I] * DL_eJ)
    return L


# =============================================================================
# MODULE 4: SECTOR CLASSIFICATION
# =============================================================================

def classify_tt_eigenvector(v_coeffs, V_TT, basis):
    """
    Classify a TT eigenvector by its support in the three sectors:
        su(2) block (indices 0,1,2)
        C^2 block   (indices 3,4,5,6)
        u(1) block  (index 7)

    Returns dict with fractional weights in each sector-pair.
    """
    c_sym = V_TT @ v_coeffs
    h = sum(c_sym[I] * basis[I] for I in range(len(basis)))
    h_norm_sq = np.sum(h**2)
    if h_norm_sq < 1e-30:
        return {'total_norm': 0.0, 'sector': 'NULL'}

    def weight(idx_a, idx_b):
        w = 0.0  # (local)
        for a in idx_a:
            for b in idx_b:
                w += h[a, b]**2
                if a != b or idx_a is not idx_b:
                    w += h[b, a]**2
        return w / h_norm_sq

    w_su2_su2 = sum(h[a, b]**2 for a in SU2_IDX for b in SU2_IDX) / h_norm_sq
    w_c2_c2 = sum(h[a, b]**2 for a in C2_IDX for b in C2_IDX) / h_norm_sq
    w_su2_c2 = sum(h[a, b]**2 for a in SU2_IDX for b in C2_IDX) / h_norm_sq
    w_su2_c2 += sum(h[a, b]**2 for a in C2_IDX for b in SU2_IDX) / h_norm_sq
    w_u1 = sum(h[7, b]**2 + h[b, 7]**2 for b in range(DIM)) / h_norm_sq
    # Avoid double counting h[7,7]
    w_u1 -= h[7, 7]**2 / h_norm_sq

    sectors = {'su2': w_su2_su2, 'c2': w_c2_c2, 'cross': w_su2_c2, 'u1': w_u1}
    dominant = max(sectors, key=sectors.get)
    sector_names = {'su2': 'HARD(su2)', 'c2': 'C2-C2', 'cross': 'SOFT(su2-C2)', 'u1': 'U1-mixed'}

    return {
        'su2': w_su2_su2,
        'c2': w_c2_c2,
        'cross': w_su2_c2,
        'u1': w_u1,
        'sector': sector_names[dominant],
        'total_norm': h_norm_sq,
    }


# =============================================================================
# MODULE 5: FULL COMPUTATION AT ONE TAU
# =============================================================================

def compute_lichnerowicz_at_tau(tau, gens=None, f_abc=None, B_ab=None):
    """
    Full Lichnerowicz spectrum on G-invariant TT 2-tensors at one tau.

    Returns dict with eigenvalues, classifications, and diagnostics.
    """
    if gens is None:
        gens = su3_generators()
    if f_abc is None:
        f_abc = compute_structure_constants(gens)
    if B_ab is None:
        B_ab = compute_killing_form(f_abc)

    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Curvature
    Riem = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(Riem)
    R_scalar = np.trace(Ric)

    # Ricci by sector
    Ric_u1 = np.mean([Ric[i, i] for i in U1_IDX])
    Ric_su2 = np.mean([Ric[i, i] for i in SU2_IDX])
    Ric_c2 = np.mean([Ric[i, i] for i in C2_IDX])

    # Sym^2 basis
    basis, labels = sym2_basis()

    # TT projection
    _, n_tt, V_TT = tt_projector(ft, Gamma, basis, labels)

    # Full Lichnerowicz matrix in Sym^2 basis
    L_full = lichnerowicz_matrix(Riem, Ric, basis)

    # Check self-adjointness
    sym_err = np.max(np.abs(L_full - L_full.T))

    # Restrict to TT subspace
    L_TT = V_TT.T @ L_full @ V_TT
    sym_err_tt = np.max(np.abs(L_TT - L_TT.T))
    L_TT = 0.5 * (L_TT + L_TT.T)  # enforce symmetry

    # Diagonalize
    eigenvalues, eigenvectors = np.linalg.eigh(L_TT)

    # Classify each eigenvector
    classifications = []
    for k in range(n_tt):
        w = classify_tt_eigenvector(eigenvectors[:, k], V_TT, basis)
        classifications.append(w)

    n_negative = int(np.sum(eigenvalues < -1e-10))

    return {
        'tau': tau,
        'n_tt': n_tt,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors,
        'classifications': classifications,
        'n_negative': n_negative,
        'R_scalar': R_scalar,
        'Ric_u1': Ric_u1,
        'Ric_su2': Ric_su2,
        'Ric_c2': Ric_c2,
        'sym_err_full': sym_err,
        'sym_err_tt': sym_err_tt,
        'L_TT': L_TT,
        'V_TT': V_TT,
    }


# =============================================================================
# MODULE 6: BI-INVARIANT VALIDATION (tau=0)
# =============================================================================

def validate_biinvariant(result):
    """
    At tau=0, SU(3) with bi-invariant metric is Einstein:
        Ric = (R/8) I = 0.25 I   (R = 2.0 for our normalization)

    The Lichnerowicz on Einstein manifolds in singlet sector:
        Delta_L h = -2 R_{acbd} h^{cd} + (2R/d) h

    For the bi-invariant case R = 2.0, d = 8:
        Ricci contribution = 2 * (R/d) = 2 * 0.25 = 0.5 uniformly
        Total eigenvalue = 0.5 + (Riemann contribution)

    Known: for bi-invariant compact simple Lie group, all TT eigenvalues = 1.0
    (from Schwahn formula / direct computation).

    Returns dict of validation checks.
    """
    evals = result['eigenvalues']
    R_scalar = result['R_scalar']

    checks = {}
    checks['R_scalar'] = R_scalar
    checks['R_expected'] = 2.0
    checks['R_err'] = abs(R_scalar - 2.0)
    checks['Ric_u1'] = result['Ric_u1']
    checks['Ric_su2'] = result['Ric_su2']
    checks['Ric_c2'] = result['Ric_c2']
    checks['Ric_isotropic_err'] = max(
        abs(result['Ric_u1'] - 0.25),
        abs(result['Ric_su2'] - 0.25),
        abs(result['Ric_c2'] - 0.25),
    )
    checks['min_eval'] = float(evals[0])
    checks['max_eval'] = float(evals[-1])
    checks['all_unit'] = bool(np.max(np.abs(evals - 1.0)) < 1e-8)
    checks['n_tt'] = result['n_tt']

    return checks


# =============================================================================
# MODULE 7: EIGENVALUE GROUPING (degeneracy detection)
# =============================================================================

def group_eigenvalues(evals, tol=1e-8):
    """Group eigenvalues by approximate equality. Returns list of (value, degeneracy)."""
    sorted_evals = np.sort(evals)
    groups = []
    i = 0
    while i < len(sorted_evals):
        val = sorted_evals[i]
        count = 1  # (local)
        while i + count < len(sorted_evals) and abs(sorted_evals[i + count] - val) < tol:
            count += 1
        groups.append((float(val), count))
        i += count
    return groups


# =============================================================================
# MAIN
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 78)
    print("  S55 LICHNEROWICZ-55: Lichnerowicz Stability at the Jensen Fold")
    print("  Full TT spectrum on G-invariant 2-tensors, SU(3)")
    print("=" * 78)

    # Precompute shared infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    # Dense tau sweep with extra resolution near the fold
    tau_coarse = np.array([0.00, 0.05, 0.10, 0.12, 0.14, 0.16, 0.17, 0.18])
    tau_fold_region = np.array([0.185, 0.19, 0.195, 0.20, 0.205, 0.21])
    tau_post = np.array([0.22, 0.24, 0.26, 0.285, 0.30, 0.35, 0.40, 0.50])
    tau_values = np.concatenate([tau_coarse, tau_fold_region, tau_post])

    # Storage
    all_results = {}
    all_eigenvalues = {}
    all_n_negative = {}

    # =========================================================================
    # TAU SWEEP
    # =========================================================================
    print(f"\n{'tau':>6s}  {'n_TT':>5s}  {'min_eval':>12s}  {'max_eval':>12s}  "
          f"{'n_neg':>5s}  {'sym_err':>10s}  {'R_scalar':>10s}")
    print("-" * 78)

    for tau in tau_values:
        result = compute_lichnerowicz_at_tau(tau, gens, f_abc, B_ab)
        all_results[tau] = result
        evals = result['eigenvalues']
        n_neg = result['n_negative']
        all_eigenvalues[tau] = evals
        all_n_negative[tau] = n_neg

        print(f"{tau:6.3f}  {result['n_tt']:5d}  {evals[0]:+12.8f}  {evals[-1]:+12.8f}  "
              f"{n_neg:5d}  {result['sym_err_tt']:.2e}  {result['R_scalar']:10.6f}")

    # =========================================================================
    # VALIDATION AT TAU = 0
    # =========================================================================
    print(f"\n{'='*78}")
    print("  VALIDATION: tau = 0 (bi-invariant metric)")
    print(f"{'='*78}")

    checks = validate_biinvariant(all_results[0.0])
    print(f"  R_scalar = {checks['R_scalar']:.12f}  (expected 2.0, err = {checks['R_err']:.2e})")
    print(f"  Ric isotropy error: {checks['Ric_isotropic_err']:.2e}")
    print(f"  n_TT = {checks['n_tt']}")
    print(f"  Eigenvalue range: [{checks['min_eval']:+.10f}, {checks['max_eval']:+.10f}]")
    print(f"  All eigenvalues = 1.0: {checks['all_unit']}")

    evals_0 = all_eigenvalues[0.0]
    groups_0 = group_eigenvalues(evals_0)
    print(f"\n  Eigenvalue groups at tau=0:")
    for val, deg in groups_0:
        print(f"    lambda = {val:+.10f}  (degeneracy {deg})")

    # =========================================================================
    # DETAILED FOLD ANALYSIS
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  FOLD ANALYSIS (tau = {tau_fold})")
    print(f"{'='*78}")

    result_fold = all_results[tau_fold]
    evals_fold = result_fold['eigenvalues']
    n_tt_fold = result_fold['n_tt']

    print(f"  n_TT = {n_tt_fold}")
    print(f"  R_scalar = {result_fold['R_scalar']:.10f}")
    print(f"  Ric_u1 = {result_fold['Ric_u1']:.10f}")
    print(f"  Ric_su2 = {result_fold['Ric_su2']:.10f}")
    print(f"  Ric_C2 = {result_fold['Ric_c2']:.10f}")
    print(f"  Symmetry error: {result_fold['sym_err_tt']:.2e}")

    # Eigenvalue groups at fold
    groups_fold = group_eigenvalues(evals_fold)
    print(f"\n  Eigenvalue groups at fold:")
    for val, deg in groups_fold:
        # Find sector of representative
        for k in range(n_tt_fold):
            if abs(evals_fold[k] - val) < 1e-8:
                sector = result_fold['classifications'][k]['sector']
                break
        print(f"    lambda = {val:+.10f}  (deg {deg})  [{sector}]")

    # Sector decomposition at fold
    sector_evals = {'HARD(su2)': [], 'SOFT(su2-C2)': [], 'C2-C2': [], 'U1-mixed': []}
    for k in range(n_tt_fold):
        w = result_fold['classifications'][k]
        ev = evals_fold[k]
        sector_evals[w['sector']].append(ev)

    print(f"\n  Sector decomposition:")
    for sector_name in ['HARD(su2)', 'SOFT(su2-C2)', 'C2-C2', 'U1-mixed']:
        evs = np.array(sector_evals[sector_name])
        if len(evs) > 0:
            print(f"    {sector_name:15s}: {len(evs)} modes, "
                  f"range [{evs.min():.8f}, {evs.max():.8f}], mean = {evs.mean():.8f}")
        else:
            print(f"    {sector_name:15s}: 0 modes")

    # Hard/Soft ratio
    hard_evs = np.array(sector_evals['HARD(su2)'])
    soft_evs = np.array(sector_evals['SOFT(su2-C2)'])
    if len(hard_evs) > 0 and len(soft_evs) > 0:
        splitting_ratio = hard_evs.mean() / soft_evs.mean()
        print(f"\n  Hard/Soft splitting ratio: {splitting_ratio:.6f}")
    else:
        splitting_ratio = np.nan

    # =========================================================================
    # STABILITY CLASSIFICATION ACROSS ALL TAU
    # =========================================================================
    print(f"\n{'='*78}")
    print("  STABILITY CLASSIFICATION")
    print(f"{'='*78}")

    any_tachyon = False
    for tau in tau_values:
        n_neg = all_n_negative[tau]
        evals = all_eigenvalues[tau]
        status = "STABLE" if n_neg == 0 else "*** TACHYON ***"
        print(f"  tau={tau:.3f}: min_ev = {evals[0]:+.8f}, "
              f"max_ev = {evals[-1]:+.8f}, n_neg = {n_neg}  [{status}]")
        if n_neg > 0:
            any_tachyon = True

    print(f"\n  Overall stability: {'ALL STABLE (no tachyons at any tau)' if not any_tachyon else 'TACHYONIC (instability detected)'}")

    # =========================================================================
    # EIGENVALUE EVOLUTION TRACKING
    # =========================================================================
    print(f"\n{'='*78}")
    print("  EIGENVALUE EVOLUTION (min, mean, max)")
    print(f"{'='*78}")

    for tau in sorted(tau_values):
        evals = all_eigenvalues[tau]
        print(f"  tau={tau:.3f}: min={evals[0]:+.8f}, mean={evals.mean():.8f}, "
              f"max={evals[-1]:+.8f}, spread={evals[-1]-evals[0]:.8f}")

    # =========================================================================
    # CROSS-CHECK: RICCI EIGENVALUES
    # =========================================================================
    print(f"\n{'='*78}")
    print("  RICCI EIGENVALUE EVOLUTION")
    print(f"{'='*78}")

    for tau in sorted(tau_values):
        r = all_results[tau]
        print(f"  tau={tau:.3f}: Ric_u1={r['Ric_u1']:.8f}, "
              f"Ric_su2={r['Ric_su2']:.8f}, Ric_C2={r['Ric_c2']:.8f}, "
              f"R={r['R_scalar']:.8f}")

    # =========================================================================
    # U(2)-INVARIANT SECTOR EXTRACTION
    # =========================================================================
    print(f"\n{'='*78}")
    print("  U(2)-INVARIANT SECTOR (diagonal TT modes)")
    print(f"{'='*78}")
    print("  These are the 2 diagonal modes parametrizing the Jensen deformation.")
    print("  h_1 ~ (su2 vs u1) contrast, h_2 ~ (su2+u1 vs C^2) contrast.")
    print("  S43 found eigenvalues [1.0, 1.0] at tau=0.")
    print()

    # Construct U(2)-invariant basis
    h_1 = np.diag([-1., -1., -1., 0., 0., 0., 0., 3.])
    h_1 /= np.sqrt(np.sum(h_1**2))
    h_2_raw = np.diag([-4., -4., -4., 3., 3., 3., 3., 0.])
    h_2_raw /= np.sqrt(np.sum(h_2_raw**2))
    overlap = np.sum(h_1 * h_2_raw)
    h_2 = h_2_raw - overlap * h_1
    h_2 /= np.sqrt(np.sum(h_2**2))

    for tau in sorted(tau_values):
        Riem = compute_riemann_tensor_ON_fast(tau)
        Ric = ricci_from_riemann(Riem)

        DL_h1 = lichnerowicz_action(Riem, Ric, h_1)
        DL_h2 = lichnerowicz_action(Riem, Ric, h_2)

        # 2x2 matrix
        M = np.array([
            [np.sum(h_1 * DL_h1), np.sum(h_1 * DL_h2)],
            [np.sum(h_2 * DL_h1), np.sum(h_2 * DL_h2)],
        ])
        lam = np.sort(np.linalg.eigvalsh(M))
        print(f"  tau={tau:.3f}: lambda_U2 = [{lam[0]:+.8f}, {lam[1]:+.8f}]")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GATE LICHNEROWICZ-55 VERDICT")
    print(f"{'='*78}")

    spectrum_computed = all(len(all_eigenvalues[t]) > 0 for t in tau_values)
    no_tachyon = not any_tachyon
    n_tau_points = len(tau_values)

    min_global = min(all_eigenvalues[t][0] for t in tau_values)
    tau_of_min = min(tau_values, key=lambda t: all_eigenvalues[t][0])

    print(f"  Spectrum computed at {n_tau_points} tau values: {spectrum_computed}")
    print(f"  Global minimum eigenvalue: {min_global:+.10f} (at tau={tau_of_min:.3f})")
    print(f"  Tachyonic modes detected: {any_tachyon}")
    print(f"  n_TT at fold: {n_tt_fold}")
    print(f"  Eigenvalue range at fold: [{evals_fold[0]:+.10f}, {evals_fold[-1]:+.10f}]")

    if not spectrum_computed:
        verdict = "FAIL (computation incomplete)"
    elif any_tachyon:
        verdict = f"INFO: UNSTABLE — {sum(all_n_negative[t] for t in tau_values)} tachyonic modes detected"
    else:
        if checks['all_unit']:
            verdict = (f"INFO: STABLE — all TT eigenvalues positive across tau in [0, {tau_values[-1]:.2f}]. "
                      f"Global min = {min_global:+.8f} at tau={tau_of_min:.3f}. "
                      f"Bi-invariant validation PASS (all evals = 1.0 at tau=0). "
                      f"Consistent with S20b (no tachyons).")
        else:
            verdict = (f"INFO: STABLE but bi-invariant validation issues — "
                      f"global min = {min_global:+.8f}")

    print(f"\n  VERDICT: {verdict}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Panel A: TT spectrum at the fold
    ax = axes[0, 0]
    sorted_idx = np.argsort(evals_fold)
    colors_map = {'HARD(su2)': '#1565C0', 'SOFT(su2-C2)': '#E65100',
                  'C2-C2': '#2E7D32', 'U1-mixed': '#7B1FA2', 'NULL': '#888'}
    colors = [colors_map.get(result_fold['classifications'][sorted_idx[k]]['sector'], '#888')
              for k in range(n_tt_fold)]
    ax.barh(range(n_tt_fold), evals_fold[sorted_idx], color=colors,
            edgecolor='black', linewidth=0.5)
    ax.set_xlabel(r'Eigenvalue $\lambda_{\mathrm{TT}}$', fontsize=11)
    ax.set_ylabel('Mode index', fontsize=11)
    ax.set_title(r'(A) TT Lichnerowicz spectrum at $\tau$ = ' + f'{tau_fold}', fontsize=12)
    ax.axvline(x=0, color='red', linestyle='--', alpha=0.5)
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#1565C0', label='HARD (su2-su2)'),
        Patch(facecolor='#E65100', label='SOFT (su2-C2)'),
        Patch(facecolor='#2E7D32', label='C2-C2'),
        Patch(facecolor='#7B1FA2', label='U1-mixed'),
    ]
    ax.legend(handles=legend_elements, fontsize=8, loc='lower right')
    ax.grid(axis='x', alpha=0.3)

    # Panel B: Eigenvalue evolution with tau
    ax = axes[0, 1]
    n_tt_max = max(len(all_eigenvalues[t]) for t in tau_values)
    for k in range(n_tt_max):
        taus_plot = []
        evals_plot = []
        for tau in sorted(tau_values):
            ev = np.sort(all_eigenvalues[tau])
            if k < len(ev):
                taus_plot.append(tau)
                evals_plot.append(ev[k])
        ax.plot(taus_plot, evals_plot, '-', linewidth=0.8, alpha=0.6)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5,
               label=r'$\tau_{\mathrm{fold}}$')
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=11)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=11)
    ax.set_title('(B) TT eigenvalue evolution', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel C: Min eigenvalue and envelope
    ax = axes[1, 0]
    sorted_taus = sorted(tau_values)
    min_evals = [all_eigenvalues[t][0] for t in sorted_taus]
    max_evals = [all_eigenvalues[t][-1] for t in sorted_taus]
    mean_evals = [all_eigenvalues[t].mean() for t in sorted_taus]
    ax.fill_between(sorted_taus, min_evals, max_evals, alpha=0.15, color='#1565C0')
    ax.plot(sorted_taus, min_evals, 'v-', color='#C62828', markersize=4,
            label='min', linewidth=1.5)
    ax.plot(sorted_taus, max_evals, '^-', color='#1565C0', markersize=4,
            label='max', linewidth=1.5)
    ax.plot(sorted_taus, mean_evals, 's-', color='#2E7D32', markersize=4,
            label='mean', linewidth=1.5)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Stability')
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=11)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=11)
    ax.set_title('(C) Eigenvalue envelope vs tau', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel D: U(2)-invariant sector eigenvalues
    ax = axes[1, 1]
    lam1_arr = []
    lam2_arr = []
    for tau in sorted_taus:
        Riem = compute_riemann_tensor_ON_fast(tau)
        Ric_loc = ricci_from_riemann(Riem)
        DL_h1 = lichnerowicz_action(Riem, Ric_loc, h_1)
        DL_h2 = lichnerowicz_action(Riem, Ric_loc, h_2)
        M_u2 = np.array([
            [np.sum(h_1 * DL_h1), np.sum(h_1 * DL_h2)],
            [np.sum(h_2 * DL_h1), np.sum(h_2 * DL_h2)],
        ])
        lam_u2 = np.sort(np.linalg.eigvalsh(M_u2))
        lam1_arr.append(lam_u2[0])
        lam2_arr.append(lam_u2[1])

    ax.plot(sorted_taus, lam1_arr, 'o-', color='#1565C0', markersize=4,
            label=r'$\lambda_1^{U(2)}$', linewidth=1.5)
    ax.plot(sorted_taus, lam2_arr, 's-', color='#E65100', markersize=4,
            label=r'$\lambda_2^{U(2)}$', linewidth=1.5)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=11)
    ax.set_ylabel(r'U(2)-invariant eigenvalue', fontsize=11)
    ax.set_title('(D) U(2)-invariant Lichnerowicz sector', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(SCRIPT_DIR, 's55_lichnerowicz.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"\n  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    npz_path = os.path.join(SCRIPT_DIR, 's55_lichnerowicz.npz')

    # Collect eigenvalue arrays
    n_tt_max = max(len(all_eigenvalues[t]) for t in tau_values)
    evals_array = np.full((len(tau_values), n_tt_max), np.nan)
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
             min_eval_fold=float(evals_fold[0]),
             max_eval_fold=float(evals_fold[-1]),
             min_global=float(min_global),
             tau_of_min=float(tau_of_min),
             splitting_ratio=float(splitting_ratio) if not np.isnan(splitting_ratio) else 0.0,
             verdict=verdict,
             any_tachyon=any_tachyon,
             lam1_u2=np.array(lam1_arr),
             lam2_u2=np.array(lam2_arr),
             )
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    elapsed = time.time() - t_start
    print(f"\n{'='*78}")
    print("  LICHNEROWICZ-55 SUMMARY")
    print(f"{'='*78}")
    print(f"  Runtime: {elapsed:.1f}s")
    print(f"  Tau values scanned: {len(tau_values)}")
    print(f"  n_TT modes: {n_tt_fold}")
    print(f"  Global min eigenvalue: {min_global:+.10f} (at tau={tau_of_min:.3f})")
    print(f"  Fold eigenvalue range: [{evals_fold[0]:+.10f}, {evals_fold[-1]:+.10f}]")
    print(f"  Tachyonic modes anywhere: {'YES' if any_tachyon else 'NO'}")
    print(f"  Hard/Soft ratio at fold: {splitting_ratio:.6f}" if not np.isnan(splitting_ratio) else "  Hard/Soft ratio: N/A")
    print(f"\n  VERDICT: {verdict}")


if __name__ == '__main__':
    main()
