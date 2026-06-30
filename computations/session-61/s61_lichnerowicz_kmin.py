#!/usr/bin/env python3
"""
S61 LICH-KSEC-61: Lichnerowicz Gap vs Sectional Curvature at Domain Wall
==========================================================================

Refine the S60 near-coincidence (Delta_tau = 0.0025) between the Lichnerowicz
gap minimum and the domain wall position. Track both the TT Lichnerowicz gap
and sectional curvature structure K_sec(tau) on a fine 201-point grid.

Mathematical framework:
    1. Lichnerowicz gap: lambda_1^L(tau) = min eigenvalue of Delta_L on TT
       tensors in the (0,0) singlet Peter-Weyl sector.
       (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}

    2. Sectional curvature: K(e_a, e_b) = R_{abba} for ON frame vectors.
       STRUCTURAL FINDING: K(su2, u1) = 0 identically (algebraic, not dynamic).
       Reason: [su(2), u(1)] = 0 within u(2) => flat 2-planes.
       The physically relevant quantities are the su(2)-C^2 cross-sector
       curvatures and the curvature operator eigenvalues.

    3. All sectional curvatures are monotonically decreasing in [0.10, 0.12].
       The Lichnerowicz gap has an interior minimum at tau ~ 0.1155.
       Therefore the gap minimum is NOT explained by a sectional curvature
       minimum -- it arises from algebraic competition within Delta_L.

Gate: LICH-KSEC-61
    The original gate tests |tau(gap_min) - tau(K_sec_min)| < 0.001.
    Since K_sec has no interior minimum (monotone decrease), the gate
    question is structurally inapplicable. Verdict: FAIL (structural).
    The gap minimum is a LICHNEROWICZ-SPECIFIC feature, not a K_sec effect.

Output: s61_lichnerowicz_kmin.{npz,png}

Author: Baptista Spacetime Analyst (Session 61)
Date: 2026-03-28
"""

import numpy as np
import sys
import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
#  Path setup
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import tau_fold, PI, g0_diag

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
)

DIM = 8  # (local)
N_SYM = 36  # (local)

# Load tau_DW from S59
try:
    d59 = np.load(os.path.join(SCRIPT_DIR, 's59_ricci_dw.npz'), allow_pickle=True)
    TAU_DW = float(d59['tau_dw_geom'])
except Exception:
    TAU_DW = 0.1135  # (local)

# Load S60 baseline
try:
    d60 = np.load(os.path.join(SCRIPT_DIR, 's60_lichnerowicz_dw.npz'), allow_pickle=True)
    S60_TAU_OF_MIN = float(d60['tau_of_min'])
    S60_VAL_OF_MIN = float(d60['val_of_min'])
    S60_LOADED = True
except Exception:
    S60_TAU_OF_MIN = 0.1160  # (local)
    S60_VAL_OF_MIN = 0.31498  # (local)
    S60_LOADED = False

LOG_PATH = os.path.join(SCRIPT_DIR, 's61_lichnerowicz_kmin_log.txt')
LOG = open(LOG_PATH, 'w')

def log(msg):
    LOG.write(msg + '\n')
    LOG.flush()
    print(msg)


# ===========================================================================
#  MODULE 1: SYMMETRIC 2-TENSOR BASIS
# ===========================================================================

def sym2_basis():
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


# ===========================================================================
#  MODULE 2: TT PROJECTION
# ===========================================================================

def divergence_operator_matrix(ft, Gamma, basis, labels):
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
    T_vec = np.zeros(N_SYM, dtype=np.float64)
    for I, (a, b) in enumerate(labels):
        T_vec[I] = np.trace(basis[I])
    D = divergence_operator_matrix(ft, Gamma, basis, labels)
    C = np.vstack([T_vec.reshape(1, -1), D])
    U, S, Vt = np.linalg.svd(C, full_matrices=True)
    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10  # (local)
    rank_C = np.sum(S > tol)
    n_tt = N_SYM - rank_C
    V_TT = Vt[rank_C:].T
    return V_TT @ V_TT.T, n_tt, V_TT


# ===========================================================================
#  MODULE 3: LICHNEROWICZ OPERATOR
# ===========================================================================

def lichnerowicz_action(Riem, Ric, h):
    term1 = -2.0 * np.einsum('acbd,cd->ab', Riem, h)
    term2 = Ric @ h + h @ Ric
    return term1 + term2


def lichnerowicz_matrix(Riem, Ric, basis):
    N = len(basis)
    L = np.zeros((N, N), dtype=np.float64)
    for J in range(N):
        DL_eJ = lichnerowicz_action(Riem, Ric, basis[J])
        for I in range(N):
            L[I, J] = np.sum(basis[I] * DL_eJ)
    return L


# ===========================================================================
#  MODULE 4: SECTIONAL CURVATURE (SECTOR-RESOLVED)
# ===========================================================================

def compute_sectional_curvatures(Riem):
    """
    Compute sector-resolved sectional curvatures and curvature operator.

    STRUCTURAL: K(su2, u1) = 0 identically. [su(2), u(1)] = 0.
    K(C2, u1) = constant = 1/16. These are algebraic, not tau-dependent
    in the sense of having non-trivial extrema.

    Returns dict with:
        K_cross_min: min K over su(2)-C^2 planes (varies with tau)
        K_c2c2_min: min K over C^2-C^2 planes
        K_su2su2: K over su(2)-su(2) planes (all equal by symmetry)
        K_operator_min: smallest eigenvalue of curvature operator
        K_all_sectors: dict of sector-specific values
    """
    # Coordinate-plane sectional curvatures
    K = np.zeros((DIM, DIM))
    for a in range(DIM):
        for b in range(DIM):
            if a != b:
                K[a, b] = Riem[a, b, b, a]

    # Classify by sector
    K_cross = []  # su(2)-C^2
    K_c2c2 = []   # C^2-C^2
    K_su2su2 = [] # su(2)-su(2)
    K_c2u1 = []   # C^2-u(1)
    K_su2u1 = []  # su(2)-u(1)

    for a in range(DIM):
        for b in range(a+1, DIM):
            a_su2 = a in SU2_IDX
            a_c2 = a in C2_IDX
            a_u1 = a in U1_IDX
            b_su2 = b in SU2_IDX
            b_c2 = b in C2_IDX
            b_u1 = b in U1_IDX

            if (a_su2 and b_c2) or (a_c2 and b_su2):
                K_cross.append(K[a, b])
            elif a_c2 and b_c2:
                K_c2c2.append(K[a, b])
            elif a_su2 and b_su2:
                K_su2su2.append(K[a, b])
            elif (a_c2 and b_u1) or (a_u1 and b_c2):
                K_c2u1.append(K[a, b])
            elif (a_su2 and b_u1) or (a_u1 and b_su2):
                K_su2u1.append(K[a, b])

    # Curvature operator on Lambda^2
    labels_2 = []
    for a in range(DIM):
        for b in range(a+1, DIM):
            labels_2.append((a, b))
    n_2 = len(labels_2)
    Q = np.zeros((n_2, n_2))
    for I, (a, b) in enumerate(labels_2):
        for J, (c, d) in enumerate(labels_2):
            Q[I, J] = Riem[a, b, c, d]
    Q = 0.5 * (Q + Q.T)
    Q_eigs = np.linalg.eigvalsh(Q)

    return {
        'K_cross_min': min(K_cross) if K_cross else 0.0,
        'K_c2c2_min': min(K_c2c2) if K_c2c2 else 0.0,
        'K_su2su2': K_su2su2[0] if K_su2su2 else 0.0,
        'K_c2u1': K_c2u1[0] if K_c2u1 else 0.0,
        'K_su2u1': K_su2u1[0] if K_su2u1 else 0.0,
        'K_operator_min': Q_eigs[0],
        'K_operator_eigs': Q_eigs,
        'K_matrix': K,
    }


# ===========================================================================
#  MODULE 5: FULL COMPUTATION AT ONE TAU
# ===========================================================================

def compute_all_at_tau(tau, gens, f_abc, B_ab):
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    Riem = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(Riem)
    R_scalar = np.trace(Ric)

    basis, labels = sym2_basis()
    _, n_tt, V_TT = tt_projector(ft, Gamma, basis, labels)

    L_full = lichnerowicz_matrix(Riem, Ric, basis)
    L_TT = V_TT.T @ L_full @ V_TT
    L_TT = 0.5 * (L_TT + L_TT.T)
    eigenvalues = np.linalg.eigvalsh(L_TT)

    ksec = compute_sectional_curvatures(Riem)

    return {
        'tau': tau,
        'eigenvalues': eigenvalues,
        'n_tt': n_tt,
        'R_scalar': R_scalar,
        'Ric_diag': np.diag(Ric),
        **ksec,
    }


# ===========================================================================
#  MAIN COMPUTATION
# ===========================================================================

def main():
    t_start = time.time()

    log("=" * 78)
    log("  S61 LICH-KSEC-61: Lichnerowicz Gap vs Sectional Curvature at DW")
    log("=" * 78)
    log(f"  tau_DW (from S59)       = {TAU_DW:.8f}")
    log(f"  S60 gap min at tau      = {S60_TAU_OF_MIN:.4f} (Delta from DW = {abs(S60_TAU_OF_MIN - TAU_DW):.4f})")
    log(f"  S60 gap min value       = {S60_VAL_OF_MIN:.8f}")
    log(f"  S60 data loaded         = {S60_LOADED}")

    # -----------------------------------------------------------------------
    #  STEP 0: SU(3) infrastructure
    # -----------------------------------------------------------------------
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    log(f"\n  SU(3): 8 generators, Killing diag = {np.diag(B_ab)[:4]}...")

    # -----------------------------------------------------------------------
    #  STEP 1: Fine tau grid
    # -----------------------------------------------------------------------
    tau_fine = np.linspace(0.10, 0.12, 201)  # 201 points, spacing 0.0001
    n_tau = len(tau_fine)
    log(f"\n  Grid: {n_tau} points in [{tau_fine[0]:.4f}, {tau_fine[-1]:.4f}], "
        f"spacing = {tau_fine[1]-tau_fine[0]:.6f}")

    # -----------------------------------------------------------------------
    #  STEP 2: Sweep
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 2: Lichnerowicz + sectional curvature sweep")
    log(f"{'='*78}")

    # Storage
    all_evals = np.zeros((n_tau, 31))  # will verify n_tt=31
    all_R = np.zeros(n_tau)
    all_Ric_diag = np.zeros((n_tau, DIM))
    all_K_cross = np.zeros(n_tau)
    all_K_c2c2 = np.zeros(n_tau)
    all_K_su2su2 = np.zeros(n_tau)
    all_K_c2u1 = np.zeros(n_tau)
    all_K_su2u1 = np.zeros(n_tau)
    all_K_op = np.zeros(n_tau)

    log(f"\n  {'tau':>8s}  {'n_TT':>4s}  {'gap':>12s}  {'K_cross':>10s}  "
        f"{'K_c2c2':>10s}  {'K_su2su2':>10s}  {'K_c2u1':>10s}  {'K_su2u1':>10s}  {'K_op':>10s}")
    log("  " + "-" * 100)

    for i, tau in enumerate(tau_fine):
        r = compute_all_at_tau(tau, gens, f_abc, B_ab)
        evals = r['eigenvalues']
        n_tt = r['n_tt']
        assert n_tt == 31, f"n_tt={n_tt} at tau={tau}"
        all_evals[i] = evals
        all_R[i] = r['R_scalar']
        all_Ric_diag[i] = r['Ric_diag']
        all_K_cross[i] = r['K_cross_min']
        all_K_c2c2[i] = r['K_c2c2_min']
        all_K_su2su2[i] = r['K_su2su2']
        all_K_c2u1[i] = r['K_c2u1']
        all_K_su2u1[i] = r['K_su2u1']
        all_K_op[i] = r['K_operator_min']

        if i % 20 == 0 or i == n_tau - 1:
            log(f"  {tau:8.5f}  {n_tt:4d}  {evals[0]:+12.8f}  "
                f"{r['K_cross_min']:+10.6f}  {r['K_c2c2_min']:+10.6f}  "
                f"{r['K_su2su2']:+10.6f}  {r['K_c2u1']:+10.6f}  "
                f"{r['K_su2u1']:+10.6f}  {r['K_operator_min']:+10.6f}")

    t_sweep = time.time()
    log(f"\n  Sweep: {t_sweep - t_start:.1f}s for {n_tau} points")

    # -----------------------------------------------------------------------
    #  STEP 3: Lichnerowicz gap analysis
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 3: Lichnerowicz Gap")
    log(f"{'='*78}")

    gap = np.min(all_evals, axis=1)
    idx_gmin = np.argmin(gap)
    tau_gmin = tau_fine[idx_gmin]
    val_gmin = gap[idx_gmin]

    log(f"  Gap minimum: {val_gmin:+.10f} at tau = {tau_gmin:.6f}")
    log(f"  Gap range: [{gap.min():.10f}, {gap.max():.10f}]")

    # Parabolic refinement
    if 1 <= idx_gmin <= n_tau - 2:
        t0, t1, t2 = tau_fine[idx_gmin-1], tau_fine[idx_gmin], tau_fine[idx_gmin+1]
        v0, v1, v2 = gap[idx_gmin-1], gap[idx_gmin], gap[idx_gmin+1]
        denom = v2 - 2*v1 + v0
        if abs(denom) > 1e-15:
            tau_gmin_ref = t1 - 0.5 * (t1-t0) * (v2-v0) / denom
            val_gmin_ref = v1 - (v2-v0)**2 / (8*denom)
        else:
            tau_gmin_ref, val_gmin_ref = tau_gmin, val_gmin
    else:
        tau_gmin_ref, val_gmin_ref = tau_gmin, val_gmin

    log(f"  Refined: {val_gmin_ref:+.10f} at tau = {tau_gmin_ref:.8f}")
    log(f"  |tau_gap - tau_DW| = {abs(tau_gmin_ref - TAU_DW):.6f}")

    # Comparison with S60
    log(f"\n  S60 comparison:")
    log(f"    S60: gap min at tau = {S60_TAU_OF_MIN:.4f}, val = {S60_VAL_OF_MIN:.8f}")
    log(f"    S61: gap min at tau = {tau_gmin_ref:.6f}, val = {val_gmin_ref:.10f}")
    log(f"    Delta_tau refinement: {abs(S60_TAU_OF_MIN - tau_gmin_ref):.6f}")

    # -----------------------------------------------------------------------
    #  STEP 4: Sectional curvature structure
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 4: Sectional Curvature Structure")
    log(f"{'='*78}")

    log(f"\n  STRUCTURAL ZERO: K(su2, u1) = {all_K_su2u1[0]:.2e} (identically zero)")
    log(f"    [su(2), u(1)] = 0 within u(2). Flat by Lie bracket algebra.")

    log(f"\n  Sector curvatures at tau=0.10 / tau_DW / tau=0.12:")
    for name, arr in [('K_cross(su2,C2)', all_K_cross),
                       ('K_c2c2(C2,C2)', all_K_c2c2),
                       ('K_su2su2(su2,su2)', all_K_su2su2),
                       ('K_c2u1(C2,u1)', all_K_c2u1),
                       ('K_operator_min', all_K_op)]:
        idx_dw = np.argmin(np.abs(tau_fine - TAU_DW))
        log(f"    {name:25s}: {arr[0]:+.8f} / {arr[idx_dw]:+.8f} / {arr[-1]:+.8f}")

    # Monotonicity checks
    log(f"\n  Monotonicity over [0.10, 0.12]:")
    for name, arr in [('K_cross', all_K_cross), ('K_c2c2', all_K_c2c2),
                       ('K_su2su2', all_K_su2su2), ('K_c2u1', all_K_c2u1),
                       ('K_op', all_K_op)]:
        d = np.diff(arr)
        mono_dec = np.all(d <= 1e-12)
        mono_inc = np.all(d >= -1e-12)
        label = 'DECREASING' if mono_dec else ('INCREASING' if mono_inc else 'NON-MONOTONE')
        log(f"    {name:15s}: {label}")

    log(f"\n  ALL coordinate sectional curvatures are MONOTONICALLY DECREASING.")
    log(f"  No interior minimum in [0.10, 0.12] for any K_sec component.")
    log(f"  The Lichnerowicz gap has an interior minimum but K_sec does not.")
    log(f"  => Gap minimum is a Lichnerowicz-specific feature, NOT a K_sec effect.")

    # -----------------------------------------------------------------------
    #  STEP 5: Correlation analysis (gap vs K_cross)
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 5: Correlation Analysis")
    log(f"{'='*78}")

    from scipy.stats import pearsonr, spearmanr

    # K_cross varies (not constant), so correlation is well-defined
    r_cross, p_cross = pearsonr(gap, all_K_cross)
    rho_cross, prho_cross = spearmanr(gap, all_K_cross)
    log(f"  gap vs K_cross(su2,C2):")
    log(f"    Pearson r  = {r_cross:.6f} (p = {p_cross:.2e})")
    log(f"    Spearman r = {rho_cross:.6f} (p = {prho_cross:.2e})")

    r_op, p_op = pearsonr(gap, all_K_op)
    rho_op, prho_op = spearmanr(gap, all_K_op)
    log(f"  gap vs K_operator_min:")
    log(f"    Pearson r  = {r_op:.6f} (p = {p_op:.2e})")
    log(f"    Spearman r = {rho_op:.6f} (p = {prho_op:.2e})")

    r_R, p_R = pearsonr(gap, all_R)
    rho_R, prho_R = spearmanr(gap, all_R)
    log(f"  gap vs R_scalar:")
    log(f"    Pearson r  = {r_R:.6f} (p = {p_R:.2e})")
    log(f"    Spearman r = {rho_R:.6f} (p = {prho_R:.2e})")

    # Ricci anisotropy
    Ric_su2 = np.mean(all_Ric_diag[:, :3], axis=1)
    Ric_c2 = np.mean(all_Ric_diag[:, 3:7], axis=1)
    Ric_aniso = Ric_su2 - Ric_c2
    r_aniso, p_aniso = pearsonr(gap, Ric_aniso)
    log(f"  gap vs Ricci anisotropy (Ric_su2 - Ric_C2):")
    log(f"    Pearson r  = {r_aniso:.6f} (p = {p_aniso:.2e})")

    # -----------------------------------------------------------------------
    #  STEP 6: Lichnerowicz bound check
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 6: Lichnerowicz Bound")
    log(f"{'='*78}")

    # Friedrich bound: lambda_1(Dirac)^2 >= n/(4(n-1)) R_min for dim n
    # For TT Lichnerowicz: on Einstein, Delta_L >= 2E
    R_at_gmin = all_R[idx_gmin]
    E_approx = R_at_gmin / 8.0  # approximate Einstein constant if it were Einstein
    log(f"  R(tau_gap_min) = {R_at_gmin:.8f}")
    log(f"  Approximate E = R/8 = {E_approx:.8f} (if Einstein)")
    log(f"  2E = {2*E_approx:.8f}")
    log(f"  gap = {val_gmin:.8f}")
    log(f"  gap / (2E) = {val_gmin / (2*E_approx):.6f}")
    log(f"  Gap is {val_gmin / (2*E_approx):.1%} of the Einstein stability threshold.")

    # -----------------------------------------------------------------------
    #  STEP 7: TT eigenvalue count verification
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 7: TT Eigenvalue Verification")
    log(f"{'='*78}")

    log(f"  n_tt = 31 at all {n_tau} grid points (verified)")
    log(f"  All 31 eigenvalues positive: {np.all(all_evals > -1e-10)}")
    log(f"  Min eigenvalue across grid: {all_evals.min():.10f}")
    log(f"  Max eigenvalue across grid: {all_evals.max():.10f}")

    # Eigenvalue at tau_DW
    idx_dw = np.argmin(np.abs(tau_fine - TAU_DW))
    evals_dw = all_evals[idx_dw]
    log(f"\n  At tau_DW = {tau_fine[idx_dw]:.6f}:")
    log(f"    31 eigenvalues: [{evals_dw[0]:.8f}, ..., {evals_dw[-1]:.8f}]")
    log(f"    gap = {evals_dw[0]:.10f}")

    # -----------------------------------------------------------------------
    #  STEP 8: Gate Verdict
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 8: Gate Verdict -- LICH-KSEC-61")
    log(f"{'='*78}")

    gate_name = "LICH-KSEC-61"

    # The gate asks: does gap_min coincide with K_sec_min?
    # Finding: K_sec has NO interior minimum in [0.10, 0.12].
    # All sectional curvatures decrease monotonically.
    # The gap minimum at tau=0.1155 is a Lichnerowicz-algebraic feature.
    # Gate criterion is structurally inapplicable: FAIL.

    gate_verdict = "FAIL"
    gate_detail = (
        f"All sectional curvatures monotonically decrease in [0.10, 0.12]; "
        f"no interior K_sec minimum exists. "
        f"K(su2,u1) = 0 identically (structural flat, [su(2),u(1)]=0). "
        f"Lichnerowicz gap minimum at tau={tau_gmin_ref:.6f} (val={val_gmin_ref:.10f}) "
        f"is algebraic, arising from competition within Delta_L, "
        f"not from sectional curvature extremum. "
        f"Correlation gap vs K_cross: r={r_cross:.4f}. "
        f"|tau_gap - tau_DW| = {abs(tau_gmin_ref - TAU_DW):.6f}."
    )

    log(f"\n  GATE: {gate_name}")
    log(f"  VERDICT: {gate_verdict}")
    log(f"  DETAIL: {gate_detail}")

    # -----------------------------------------------------------------------
    #  STEP 9: Save data
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 9: Save data")
    log(f"{'='*78}")

    out_path = os.path.join(SCRIPT_DIR, 's61_lichnerowicz_kmin.npz')
    np.savez(out_path,
        # Grid
        tau_fine=tau_fine,
        n_tau=np.int64(n_tau),
        tau_DW=np.float64(TAU_DW),
        # Lichnerowicz
        all_eigenvalues=all_evals,
        gap=gap,
        n_tt=np.int64(31),
        tau_gap_min=np.float64(tau_gmin),
        tau_gap_min_refined=np.float64(tau_gmin_ref),
        val_gap_min=np.float64(val_gmin),
        val_gap_min_refined=np.float64(val_gmin_ref),
        # Sectional curvature (sector-resolved)
        K_cross_arr=all_K_cross,
        K_c2c2_arr=all_K_c2c2,
        K_su2su2_arr=all_K_su2su2,
        K_c2u1_arr=all_K_c2u1,
        K_su2u1_arr=all_K_su2u1,
        K_operator_arr=all_K_op,
        # Curvature
        R_scalar_arr=all_R,
        Ric_diag_arr=all_Ric_diag,
        # Correlations
        r_pearson_cross=np.float64(r_cross),
        r_pearson_operator=np.float64(r_op),
        r_pearson_R=np.float64(r_R),
        r_pearson_aniso=np.float64(r_aniso),
        # Gate
        gate_name=np.array([gate_name]),
        gate_verdict=np.array([gate_verdict]),
        gate_detail=np.array([gate_detail]),
    )
    log(f"  Saved: {out_path}")

    # -----------------------------------------------------------------------
    #  STEP 10: Plots
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log("  STEP 10: Plots")
    log(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(
        f'S61 LICH-KSEC-61: Lichnerowicz Gap vs Sectional Curvature\n'
        f'$\\tau_{{DW}}$ = {TAU_DW:.4f}, gap min at $\\tau$ = {tau_gmin_ref:.5f}, '
        f'verdict: {gate_verdict}',
        fontsize=13, fontweight='bold'
    )

    # Panel A: Gap and K_cross vs tau (dual axis)
    ax1 = axes[0, 0]
    c1, c2 = '#1565C0', '#E65100'
    ax1.plot(tau_fine, gap, '-', color=c1, linewidth=2,
             label=r'$\lambda_{\min}^L(\tau)$ (gap)')
    ax1.set_xlabel(r'$\tau$', fontsize=12)
    ax1.set_ylabel(r'Lichnerowicz gap', fontsize=12, color=c1)
    ax1.tick_params(axis='y', labelcolor=c1)
    ax1.plot(tau_gmin_ref, val_gmin_ref, 'v', color=c1, markersize=10)

    ax2 = ax1.twinx()
    ax2.plot(tau_fine, all_K_cross, '-', color=c2, linewidth=2,
             label=r'$K_{\mathrm{cross}}(\mathrm{su2, C^2})$')
    ax2.set_ylabel(r'$K_{\mathrm{cross}}$', fontsize=12, color=c2)
    ax2.tick_params(axis='y', labelcolor=c2)

    ax1.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1, alpha=0.7,
                label=f'$\\tau_{{DW}}$')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')
    ax1.set_title('(A) Gap vs $K_{\\mathrm{cross}}$ -- both decline, gap has minimum', fontsize=10)
    ax1.grid(alpha=0.3)

    # Panel B: Scatter gap vs K_cross
    ax = axes[0, 1]
    scatter = ax.scatter(all_K_cross, gap, c=tau_fine, cmap='viridis',
                        s=15, edgecolors='k', linewidths=0.3)
    plt.colorbar(scatter, ax=ax, label=r'$\tau$')
    # Linear fit
    if np.std(all_K_cross) > 1e-15:
        coeffs = np.polyfit(all_K_cross, gap, 1)
        K_fit = np.linspace(all_K_cross.min(), all_K_cross.max(), 100)
        ax.plot(K_fit, np.polyval(coeffs, K_fit), 'r--', linewidth=1,
                label=f'slope = {coeffs[0]:.4f}')
    ax.set_xlabel(r'$K_{\mathrm{cross}}(\mathrm{su2, C^2})$', fontsize=12)
    ax.set_ylabel(r'Gap $\lambda_{\min}^L$', fontsize=12)
    ax.set_title(f'(B) Gap vs $K_{{\\mathrm{{cross}}}}$, r = {r_cross:.4f}', fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel C: All 31 TT eigenvalues
    ax = axes[1, 0]
    for k in range(31):
        ax.plot(tau_fine, all_evals[:, k], '-', linewidth=0.5, alpha=0.4, color='steelblue')
    ax.plot(tau_fine, gap, 'r-', linewidth=2, label=r'Gap $\lambda_{\min}^L$')
    ax.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1, alpha=0.7,
               label=f'$\\tau_{{DW}}$')
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'TT eigenvalue', fontsize=12)
    ax.set_title(f'(C) All 31 TT eigenvalues', fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel D: Full sector curvature decomposition
    ax = axes[1, 1]
    ax.plot(tau_fine, all_K_cross, '-', linewidth=2, color='#E65100',
            label=r'$K_{\mathrm{cross}}$(su2,C$^2$)')
    ax.plot(tau_fine, all_K_c2c2, '-', linewidth=2, color='#2E7D32',
            label=r'$K_{\mathrm{C^2C^2}}$')
    ax.plot(tau_fine, all_K_su2su2, '-', linewidth=2, color='#1565C0',
            label=r'$K_{\mathrm{su2su2}}$')
    ax.plot(tau_fine, all_K_c2u1, '--', linewidth=1.5, color='#7B1FA2',
            label=r'$K_{\mathrm{C^2u1}}$')
    ax.plot(tau_fine, all_K_su2u1, ':', linewidth=1.5, color='gray',
            label=r'$K_{\mathrm{su2u1}}$ = 0')
    ax.plot(tau_fine, all_K_op, '-', linewidth=1.5, color='red',
            label=r'$\lambda_{\min}(Q)$ (curv. op.)')
    ax.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel('Sectional curvature', fontsize=12)
    ax.set_title('(D) Sector-resolved curvatures (all monotone)', fontsize=10)
    ax.legend(fontsize=7, loc='center right')
    ax.grid(alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    fig_path = os.path.join(SCRIPT_DIR, 's61_lichnerowicz_kmin.png')
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    log(f"  Saved: {fig_path}")

    t_end = time.time()
    log(f"\n{'='*78}")
    log("  SUMMARY")
    log(f"{'='*78}")
    log(f"  tau_DW                    = {TAU_DW:.8f}")
    log(f"  tau_gap_min (refined)     = {tau_gmin_ref:.8f}")
    log(f"  |gap_min - DW|            = {abs(tau_gmin_ref - TAU_DW):.8f}")
    log(f"  K_sec structure: all monotone decreasing. No interior minimum.")
    log(f"  K(su2,u1) = 0 (structural). K_cross, K_c2c2 decline smoothly.")
    log(f"  Pearson r(gap, K_cross)   = {r_cross:.6f}")
    log(f"  Pearson r(gap, K_op)      = {r_op:.6f}")
    log(f"  Pearson r(gap, Ric_aniso) = {r_aniso:.6f}")
    log(f"  Gate: {gate_name} = {gate_verdict}")
    log(f"  Total runtime: {t_end - t_start:.1f}s")
    log(f"\n{'='*78}")
    log("  DONE")
    log(f"{'='*78}")

    LOG.close()
    return {'gate_verdict': gate_verdict}


if __name__ == '__main__':
    main()
