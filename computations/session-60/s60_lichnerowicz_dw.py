#!/usr/bin/env python3
"""
S60 LICHNEROWICZ-DW-60: Lichnerowicz TT Eigenvalue Tracking at Domain Wall
============================================================================

Track all 31 Lichnerowicz TT eigenvalues through tau_DW = 0.113 with fine
resolution (Delta_tau = 0.001). A zero-crossing = domain wall soft mode.

Mathematical framework:
    The Lichnerowicz operator on symmetric 2-tensors h_{ab} is:

        (Delta_L h)_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 Ric_{(a}^c h_{b)c}

    In the (0,0) singlet Peter-Weyl sector, -nabla^2 h = C_2(0,0) h = 0,
    so Delta_L reduces to the purely ALGEBRAIC curvature action:

        (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}

    The space of G-invariant TT tensors on SU(3) with Jensen metric g_tau:
        dim(Sym^2(R^8)) = 36, minus trace = 35, minus divergence ~ 31
        (35 at tau=0 due to enhanced symmetry; 31 for tau > 0)

    Domain wall context:
        S58: E_DW changes sign at tau ~ 0.1135
        S59: Ricci anisotropy A_crit = 0.673, sec_min ~ 0 at tau_DW
        S55: All TT eigenvalues positive (coarse grid), global min ~ 0.157

    This script resolves the fine structure near tau_DW to check whether
    any eigenvalue develops a zero-crossing or significant minimum there.

Gate: LICHNEROWICZ-DW-60
    PASS: Specific eigenvalue crosses zero at tau_DW
    FAIL: All positive through tau_DW
    INFO: Eigenvalue minimum near tau_DW but no crossing

Cross-references:
    - S55: Full Lichnerowicz TT spectrum (coarse grid)
    - S59: Ricci DW (Ricci anisotropy, sectional curvature)
    - S20b: TT stability (no tachyons at any tau)

Output:
    - s60_lichnerowicz_dw.npz
    - s60_lichnerowicz_dw.png

Author: Baptista Spacetime Analyst (Session 60)
Date: 2026-03-27
"""

import numpy as np
import sys
import os
import time
import traceback

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

DIM = 8  # dim(su(3)) (local)
N_SYM = 36   # dim(Sym^2(R^8)) = 8*9/2

# Load tau_DW from S59 data
try:
    d59 = np.load(os.path.join(SCRIPT_DIR, 's59_ricci_dw.npz'), allow_pickle=True)
    TAU_DW = float(d59['tau_dw_geom'])
except Exception:
    TAU_DW = 0.1135  # fallback  # (local)

LOG_PATH = os.path.join(SCRIPT_DIR, 's60_lichnerowicz_dw_log.txt')
LOG = open(LOG_PATH, 'w')

def log(msg):
    LOG.write(msg + '\n')
    LOG.flush()
    print(msg)

log("=" * 78)
log("  S60 LICHNEROWICZ-DW-60: Lichnerowicz TT Eigenvalue Tracking at Domain Wall")
log("=" * 78)
log(f"  tau_DW (from S59) = {TAU_DW:.8f}")
log(f"  tau_fold           = {tau_fold}")
log(f"  g0_diag (alpha)    = {g0_diag}")

# ===========================================================================
#  MODULE 1: SYMMETRIC 2-TENSOR BASIS
# ===========================================================================

def sym2_basis():
    """
    Orthonormal basis for Sym^2(R^8) under Frobenius inner product.
    Returns list of 36 (8,8) arrays and (a,b) labels.
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

# ===========================================================================
#  MODULE 2: TT PROJECTION
# ===========================================================================

def divergence_operator_matrix(ft, Gamma, basis, labels):
    """
    Divergence operator div: Sym^2 -> R^8 for left-invariant tensors.
    (div h)_b = sum_a nabla_{e_a} h_{ab}
    Since e_a(h_{bc})=0 for left-invariant h:
        nabla_{e_a} h_{ab} = -sum_d Gamma^d_{aa} h_{db} - sum_d Gamma^d_{ab} h_{ad}
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
    Projector onto TT (transverse, trace-free) subspace.
    TT = ker(trace) intersection ker(divergence).
    Returns P_TT, n_tt, V_TT.
    """
    T_vec = np.zeros(N_SYM, dtype=np.float64)
    for I, (a, b) in enumerate(labels):
        T_vec[I] = np.trace(basis[I])

    D = divergence_operator_matrix(ft, Gamma, basis, labels)
    C = np.vstack([T_vec.reshape(1, -1), D])

    U, S, Vt = np.linalg.svd(C, full_matrices=True)
    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10  # (local)
    rank_C = np.sum(S > tol)
    n_tt = N_SYM - rank_C
    V_TT = Vt[rank_C:].T  # (N_SYM, n_tt)

    return V_TT @ V_TT.T, n_tt, V_TT

# ===========================================================================
#  MODULE 3: LICHNEROWICZ OPERATOR
# ===========================================================================

def lichnerowicz_action(Riem, Ric, h):
    """
    Apply Lichnerowicz to symmetric 2-tensor h (singlet sector: nabla^2 = 0).
    (Delta_L h)_{ab} = -2 R_{acbd} h^{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
    Convention: Riem[a,b,c,d] = R_{abcd}.  Need R_{acbd} = Riem[a,c,b,d].
    """
    term1 = -2.0 * np.einsum('acbd,cd->ab', Riem, h)
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

# ===========================================================================
#  MODULE 4: SECTOR CLASSIFICATION
# ===========================================================================

def classify_tt_eigenvector(v_coeffs, V_TT, basis):
    """
    Classify a TT eigenvector by support in su(2), C^2, u(1) sectors.
    """
    c_sym = V_TT @ v_coeffs
    h = sum(c_sym[I] * basis[I] for I in range(len(basis)))
    h_norm_sq = np.sum(h**2)
    if h_norm_sq < 1e-30:
        return {'total_norm': 0.0, 'sector': 'NULL'}

    w_su2 = sum(h[a, b]**2 for a in SU2_IDX for b in SU2_IDX) / h_norm_sq
    w_c2  = sum(h[a, b]**2 for a in C2_IDX for b in C2_IDX) / h_norm_sq
    w_cross = sum(h[a, b]**2 for a in SU2_IDX for b in C2_IDX) / h_norm_sq
    w_cross += sum(h[a, b]**2 for a in C2_IDX for b in SU2_IDX) / h_norm_sq
    w_u1 = sum(h[7, b]**2 + h[b, 7]**2 for b in range(DIM)) / h_norm_sq
    w_u1 -= h[7, 7]**2 / h_norm_sq

    sectors = {'su2': w_su2, 'c2': w_c2, 'cross': w_cross, 'u1': w_u1}
    dominant = max(sectors, key=sectors.get)
    sector_names = {'su2': 'HARD(su2)', 'c2': 'C2-C2', 'cross': 'SOFT(su2-C2)', 'u1': 'U1-mixed'}

    return {
        'su2': w_su2, 'c2': w_c2, 'cross': w_cross, 'u1': w_u1,
        'sector': sector_names[dominant],
        'total_norm': h_norm_sq,
    }

# ===========================================================================
#  MODULE 5: FULL COMPUTATION AT ONE TAU
# ===========================================================================

def compute_lichnerowicz_at_tau(tau, gens, f_abc, B_ab):
    """
    Full Lichnerowicz spectrum on G-invariant TT 2-tensors at one tau.
    Returns dict with eigenvalues, eigenvectors, classifications, diagnostics.
    """
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    Riem = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(Riem)
    R_scalar = np.trace(Ric)

    Ric_u1  = np.mean([Ric[i, i] for i in U1_IDX])
    Ric_su2 = np.mean([Ric[i, i] for i in SU2_IDX])
    Ric_c2  = np.mean([Ric[i, i] for i in C2_IDX])

    basis, labels = sym2_basis()
    _, n_tt, V_TT = tt_projector(ft, Gamma, basis, labels)

    L_full = lichnerowicz_matrix(Riem, Ric, basis)
    sym_err = np.max(np.abs(L_full - L_full.T))

    L_TT = V_TT.T @ L_full @ V_TT
    sym_err_tt = np.max(np.abs(L_TT - L_TT.T))
    L_TT = 0.5 * (L_TT + L_TT.T)

    eigenvalues, eigenvectors = np.linalg.eigh(L_TT)
    n_negative = int(np.sum(eigenvalues < -1e-10))

    classifications = []
    for k in range(n_tt):
        w = classify_tt_eigenvector(eigenvectors[:, k], V_TT, basis)
        classifications.append(w)

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
    }

# ===========================================================================
#  MODULE 6: ADIABATIC EIGENVALUE TRACKING
# ===========================================================================

def track_eigenvalues(all_results, tau_values):
    """
    Track eigenvalues with adiabatic continuity using eigenvector overlap.

    At each step, match eigenvalues to the previous step by maximizing
    |<v_i(tau), v_j(tau + dtau)>|^2 (Hungarian-style greedy matching).

    Returns:
        tracked: (n_tau, n_tt) array of tracked eigenvalues
        tracked_sectors: (n_tau, n_tt) list of sector labels
    """
    n_tau = len(tau_values)
    n_tt = all_results[tau_values[0]]['n_tt']

    tracked = np.zeros((n_tau, n_tt))
    tracked_sectors = []

    # Initialize with first tau
    r0 = all_results[tau_values[0]]
    tracked[0] = r0['eigenvalues']
    tracked_sectors.append([c['sector'] for c in r0['classifications']])
    prev_vecs = r0['eigenvectors']

    for step in range(1, n_tau):
        r = all_results[tau_values[step]]
        curr_vecs = r['eigenvectors']
        curr_evals = r['eigenvalues']
        curr_n = r['n_tt']

        if curr_n != n_tt:
            # Dimension mismatch -- fall back to sorted ordering
            log(f"  WARNING: n_tt changed at tau={tau_values[step]:.4f}: {n_tt} -> {curr_n}")
            tracked[step, :min(curr_n, n_tt)] = curr_evals[:min(curr_n, n_tt)]
            tracked_sectors.append([c['sector'] for c in r['classifications']][:n_tt])
            prev_vecs = curr_vecs
            continue

        # Overlap matrix: O[i,j] = |<prev_i, curr_j>|^2
        overlap = np.abs(prev_vecs.T @ curr_vecs)**2

        # Greedy matching: for each prev mode, find best current match
        used = set()
        perm = np.zeros(n_tt, dtype=int)
        for i in range(n_tt):
            # Find best available match for prev mode i
            best_j = -1
            best_val = -1.0  # (local)
            for j in range(curr_n):
                if j not in used and overlap[i, j] > best_val:
                    best_val = overlap[i, j]
                    best_j = j
            perm[i] = best_j
            used.add(best_j)

        tracked[step] = curr_evals[perm]
        sectors_step = [r['classifications'][perm[k]]['sector'] for k in range(n_tt)]
        tracked_sectors.append(sectors_step)

        # Update prev_vecs in matched order
        prev_vecs = curr_vecs[:, perm]

    return tracked, tracked_sectors

# ===========================================================================
#  MODULE 7: ZERO-CROSSING AND INFLECTION DETECTION
# ===========================================================================

def find_zero_crossings(tau_values, tracked):
    """
    Find zero-crossings for each tracked eigenvalue.
    Returns list of (mode_index, tau_crossing, type) tuples.
    """
    n_tau, n_modes = tracked.shape
    crossings = []

    for k in range(n_modes):
        for i in range(n_tau - 1):
            if tracked[i, k] * tracked[i+1, k] < 0:
                # Linear interpolation for crossing location
                t0, t1 = tau_values[i], tau_values[i+1]
                v0, v1 = tracked[i, k], tracked[i+1, k]
                tau_cross = t0 - v0 * (t1 - t0) / (v1 - v0)
                crossings.append((k, tau_cross, 'ZERO_CROSSING'))
    return crossings


def find_inflections_and_minima(tau_values, tracked):
    """
    Find inflection points and local minima for each tracked eigenvalue.
    """
    n_tau, n_modes = tracked.shape
    features = []

    for k in range(n_modes):
        vals = tracked[:, k]
        # Local minima (interior points only)
        for i in range(1, n_tau - 1):
            if vals[i] < vals[i-1] and vals[i] < vals[i+1]:
                features.append((k, tau_values[i], vals[i], 'LOCAL_MIN'))

        # Inflection points via second derivative sign change
        if n_tau >= 3:
            dt = tau_values[1] - tau_values[0]
            d2v = np.diff(vals, n=2) / dt**2
            for i in range(len(d2v) - 1):
                if d2v[i] * d2v[i+1] < 0:
                    tau_infl = 0.5 * (tau_values[i+1] + tau_values[i+2])
                    features.append((k, tau_infl, vals[i+1], 'INFLECTION'))

    return features

# ===========================================================================
#  MAIN COMPUTATION
# ===========================================================================

def main():
    t_start = time.time()

    log(f"\n{'='*78}")
    log("  STEP 0: Precompute SU(3) infrastructure")
    log(f"{'='*78}")

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    log(f"  SU(3) generators: {len(gens)}")
    log(f"  Killing form diagonal: {np.diag(B_ab)[:4]}...")

    # -----------------------------------------------------------------------
    #  STEP 1: Fine tau grid around tau_DW
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 1: Fine tau grid [0.093, 0.133], Delta_tau = 0.001")
    log(f"{'='*78}")

    tau_fine = np.arange(0.093, 0.1335, 0.001)  # 41 points
    n_tau = len(tau_fine)
    log(f"  Grid: {n_tau} points, tau in [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}]")
    log(f"  tau_DW = {TAU_DW:.6f} falls between grid points "
        f"{tau_fine[np.searchsorted(tau_fine, TAU_DW)-1]:.3f} and "
        f"{tau_fine[min(np.searchsorted(tau_fine, TAU_DW), n_tau-1)]:.3f}")

    # -----------------------------------------------------------------------
    #  STEP 2: Compute Lichnerowicz at each tau
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 2: Full Lichnerowicz TT spectrum at each tau")
    log(f"{'='*78}")

    all_results = {}
    log(f"\n  {'tau':>8s}  {'n_TT':>5s}  {'min_eval':>12s}  {'max_eval':>12s}  "
        f"{'n_neg':>5s}  {'sym_err':>10s}  {'R_scalar':>10s}")
    log("  " + "-" * 74)

    for idx, tau in enumerate(tau_fine):
        result = compute_lichnerowicz_at_tau(tau, gens, f_abc, B_ab)
        all_results[tau] = result
        evals = result['eigenvalues']

        log(f"  {tau:8.4f}  {result['n_tt']:5d}  {evals[0]:+12.8f}  {evals[-1]:+12.8f}  "
            f"{result['n_negative']:5d}  {result['sym_err_tt']:.2e}  {result['R_scalar']:10.6f}")

    t_sweep = time.time()
    log(f"\n  Sweep completed in {t_sweep - t_start:.1f}s")

    # -----------------------------------------------------------------------
    #  STEP 3: Adiabatic eigenvalue tracking
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 3: Adiabatic Eigenvalue Tracking (eigenvector overlap)")
    log(f"{'='*78}")

    tracked, tracked_sectors = track_eigenvalues(all_results, tau_fine)
    n_tt = all_results[tau_fine[0]]['n_tt']
    log(f"  Tracked {n_tt} modes across {n_tau} tau values")

    # Verify tracking quality: eigenvalue sums should match
    for idx, tau in enumerate(tau_fine):
        sorted_evals = np.sort(all_results[tau]['eigenvalues'])
        sorted_tracked = np.sort(tracked[idx])
        sum_err = abs(np.sum(sorted_evals[:n_tt]) - np.sum(sorted_tracked))
        if sum_err > 1e-10:
            log(f"  WARNING: tracking sum error at tau={tau:.4f}: {sum_err:.2e}")

    # Print tracked eigenvalue table (selected modes)
    log(f"\n  Tracked eigenvalue evolution (lowest 5 modes + highest):")
    log(f"  {'tau':>8s}" + "".join([f"  {'lam_'+str(k):>10s}" for k in range(5)]) + f"  {'lam_'+str(n_tt-1):>10s}")
    for idx in range(n_tau):
        row = f"  {tau_fine[idx]:8.4f}"
        for k in range(5):
            row += f"  {tracked[idx, k]:10.6f}"
        row += f"  {tracked[idx, n_tt-1]:10.6f}"
        log(row)

    # -----------------------------------------------------------------------
    #  STEP 4: Zero-crossings and inflection points
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 4: Zero-Crossing and Inflection Point Detection")
    log(f"{'='*78}")

    crossings = find_zero_crossings(tau_fine, tracked)
    if crossings:
        log(f"\n  ZERO-CROSSINGS FOUND: {len(crossings)}")
        for mode, tau_c, ctype in crossings:
            sector = tracked_sectors[0][mode]
            log(f"    Mode {mode} [{sector}]: crosses zero at tau = {tau_c:.6f}")
    else:
        log(f"\n  No zero-crossings detected. All eigenvalues remain positive.")

    features = find_inflections_and_minima(tau_fine, tracked)
    minima = [f for f in features if f[3] == 'LOCAL_MIN']
    inflections = [f for f in features if f[3] == 'INFLECTION']

    if minima:
        log(f"\n  LOCAL MINIMA: {len(minima)}")
        for mode, tau_m, val, _ in sorted(minima, key=lambda x: x[2]):
            sector = tracked_sectors[0][mode]
            log(f"    Mode {mode} [{sector}]: min = {val:.8f} at tau = {tau_m:.4f}")
    else:
        log(f"\n  No local minima detected in the fine grid.")

    if inflections:
        log(f"\n  INFLECTION POINTS: {len(inflections)}")
        for mode, tau_i, val, _ in sorted(inflections, key=lambda x: x[1])[:20]:
            log(f"    Mode {mode}: inflection at tau = {tau_i:.4f}, value = {val:.6f}")

    # -----------------------------------------------------------------------
    #  STEP 5: Lichnerowicz gap lambda_min(tau) analysis
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 5: Lichnerowicz Gap lambda_min(tau)")
    log(f"{'='*78}")

    lambda_min = np.min(tracked, axis=1)
    lambda_max = np.max(tracked, axis=1)
    lambda_mean = np.mean(tracked, axis=1)

    # Find global minimum in the fine grid
    idx_min = np.argmin(lambda_min)
    tau_of_min = tau_fine[idx_min]
    val_of_min = lambda_min[idx_min]

    log(f"\n  Global min(lambda) = {val_of_min:+.10f} at tau = {tau_of_min:.4f}")
    log(f"  lambda_min range: [{lambda_min.min():.10f}, {lambda_min.max():.10f}]")
    log(f"  lambda_max range: [{lambda_max.min():.10f}, {lambda_max.max():.10f}]")

    # Evaluate at tau_DW specifically
    idx_dw = np.argmin(np.abs(tau_fine - TAU_DW))
    tau_nearest_dw = tau_fine[idx_dw]
    lambda_min_dw = lambda_min[idx_dw]
    lambda_max_dw = lambda_max[idx_dw]

    log(f"\n  At tau nearest to DW (tau={tau_nearest_dw:.4f}):")
    log(f"    lambda_min = {lambda_min_dw:+.10f}")
    log(f"    lambda_max = {lambda_max_dw:+.10f}")
    log(f"    All eigenvalues: {np.sort(tracked[idx_dw])}")

    # Derivative of lambda_min near tau_DW
    dlambda_dtau = np.gradient(lambda_min, tau_fine)
    d2lambda_dtau2 = np.gradient(dlambda_dtau, tau_fine)

    log(f"\n  d(lambda_min)/d(tau) at DW: {dlambda_dtau[idx_dw]:.6f}")
    log(f"  d2(lambda_min)/d(tau)2 at DW: {d2lambda_dtau2[idx_dw]:.4f}")

    # Check if gap is monotonic
    is_monotonic_dec = np.all(np.diff(lambda_min) <= 1e-12)
    is_monotonic_inc = np.all(np.diff(lambda_min) >= -1e-12)
    log(f"\n  lambda_min monotonic decreasing: {is_monotonic_dec}")
    log(f"  lambda_min monotonic increasing: {is_monotonic_inc}")

    # -----------------------------------------------------------------------
    #  STEP 6: Sector decomposition at tau_DW
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 6: Sector Decomposition at tau_DW")
    log(f"{'='*78}")

    r_dw = all_results[tau_nearest_dw]
    evals_dw = tracked[idx_dw]
    sectors_dw = tracked_sectors[idx_dw]

    sector_evals = {'HARD(su2)': [], 'SOFT(su2-C2)': [], 'C2-C2': [], 'U1-mixed': []}
    for k in range(n_tt):
        s = sectors_dw[k]
        if s in sector_evals:
            sector_evals[s].append(evals_dw[k])

    log(f"\n  Sector decomposition at tau = {tau_nearest_dw:.4f}:")
    for sname in ['HARD(su2)', 'SOFT(su2-C2)', 'C2-C2', 'U1-mixed']:
        evs = np.array(sector_evals[sname])
        if len(evs) > 0:
            log(f"    {sname:15s}: {len(evs)} modes, "
                f"range [{evs.min():.8f}, {evs.max():.8f}], mean = {evs.mean():.8f}")
        else:
            log(f"    {sname:15s}: 0 modes")

    # Which sector has the minimum eigenvalue?
    min_mode_idx = np.argmin(evals_dw)
    min_sector = sectors_dw[min_mode_idx]
    log(f"\n  Minimum eigenvalue mode: index {min_mode_idx}, sector {min_sector}")
    log(f"  Value: {evals_dw[min_mode_idx]:.10f}")

    # -----------------------------------------------------------------------
    #  STEP 7: Eigenvalue spacing and level repulsion near tau_DW
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 7: Eigenvalue Spacing and Level Repulsion")
    log(f"{'='*78}")

    sorted_evals_dw = np.sort(evals_dw)
    spacings_dw = np.diff(sorted_evals_dw)
    min_spacing = np.min(spacings_dw)
    log(f"\n  Min eigenvalue spacing at DW: {min_spacing:.10f}")
    log(f"  Mean spacing: {np.mean(spacings_dw):.10f}")
    log(f"  Spacing ratio (min/mean): {min_spacing / np.mean(spacings_dw):.6f}")

    # Check for near-degeneracies (potential avoided crossings)
    degen_threshold = 1e-4
    near_degen = [(i, spacings_dw[i]) for i in range(len(spacings_dw)) if spacings_dw[i] < degen_threshold]
    if near_degen:
        log(f"\n  Near-degeneracies (spacing < {degen_threshold}):")
        for idx_s, s in near_degen:
            log(f"    Between modes {idx_s} and {idx_s+1}: spacing = {s:.2e}")
    else:
        log(f"\n  No near-degeneracies (all spacings > {degen_threshold})")

    # -----------------------------------------------------------------------
    #  STEP 8: Gate Verdict
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 8: Gate Verdict — LICHNEROWICZ-DW-60")
    log(f"{'='*78}")

    gate_name = "LICHNEROWICZ-DW-60"
    has_crossing = len(crossings) > 0
    has_minimum_near_dw = any(abs(f[1] - TAU_DW) < 0.01 for f in minima) if minima else False
    all_positive = np.all(tracked > -1e-10)
    global_min_near_dw = abs(tau_of_min - TAU_DW) < 0.01

    if has_crossing:
        gate_verdict = "PASS"
        crossing_modes = [(m, t) for m, t, _ in crossings]
        gate_detail = (f"Zero-crossing detected: {len(crossings)} mode(s). "
                      + "; ".join([f"Mode {m} [{tracked_sectors[0][m]}] at tau={t:.6f}" for m, t in crossing_modes])
                      + f". Domain wall soft mode confirmed.")
    elif all_positive:
        gate_verdict = "FAIL"
        gate_detail = (f"All {n_tt} TT eigenvalues remain positive through tau_DW={TAU_DW:.4f}. "
                      f"Global min = {val_of_min:+.8f} at tau = {tau_of_min:.4f}. "
                      f"lambda_min(DW) = {lambda_min_dw:+.8f}. "
                      f"Min sector: {min_sector}. "
                      f"No domain wall soft mode.")
        if has_minimum_near_dw or global_min_near_dw:
            gate_verdict = "INFO"
            gate_detail += (f" However, eigenvalue minimum near DW: "
                          f"global min at tau={tau_of_min:.4f} "
                          f"(distance from DW: {abs(tau_of_min - TAU_DW):.4f}).")
    else:
        gate_verdict = "INFO"
        n_neg_total = int(np.sum(tracked < -1e-10))
        gate_detail = (f"Some eigenvalues appear negative (n_neg = {n_neg_total}), "
                      f"but no clean zero-crossing at tau_DW. Investigate numerical artifacts.")

    log(f"\n  GATE: {gate_name}")
    log(f"  VERDICT: {gate_verdict}")
    log(f"  DETAIL: {gate_detail}")

    # -----------------------------------------------------------------------
    #  STEP 9: Save data
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 9: Save data")
    log(f"{'='*78}")

    out_path = os.path.join(SCRIPT_DIR, 's60_lichnerowicz_dw.npz')
    np.savez(out_path,
        tau_fine=tau_fine,
        tracked_eigenvalues=tracked,
        lambda_min=lambda_min,
        lambda_max=lambda_max,
        lambda_mean=lambda_mean,
        dlambda_dtau=dlambda_dtau,
        d2lambda_dtau2=d2lambda_dtau2,
        n_tt=np.int64(n_tt),
        tau_DW=np.float64(TAU_DW),
        tau_of_min=np.float64(tau_of_min),
        val_of_min=np.float64(val_of_min),
        lambda_min_dw=np.float64(lambda_min_dw),
        lambda_max_dw=np.float64(lambda_max_dw),
        spacings_dw=spacings_dw,
        gate_name=np.array([gate_name]),
        gate_verdict=np.array([gate_verdict]),
        gate_detail=np.array([gate_detail]),
    )
    log(f"  Saved: {out_path}")

    # -----------------------------------------------------------------------
    #  STEP 10: Plots
    # -----------------------------------------------------------------------
    log(f"\n{'='*78}")
    log(f"  STEP 10: Generate plots")
    log(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(f'S60 LICHNEROWICZ-DW-60: TT Eigenvalue Tracking at Domain Wall\n'
                 f'$\\tau_{{DW}}$ = {TAU_DW:.4f}, verdict: {gate_verdict}',
                 fontsize=13, fontweight='bold')

    # Panel A: All tracked eigenvalues vs tau
    ax = axes[0, 0]
    sector_colors = {
        'HARD(su2)': '#1565C0', 'SOFT(su2-C2)': '#E65100',
        'C2-C2': '#2E7D32', 'U1-mixed': '#7B1FA2', 'NULL': '#888',
    }
    for k in range(n_tt):
        sector = tracked_sectors[0][k]
        color = sector_colors.get(sector, '#888')
        ax.plot(tau_fine, tracked[:, k], '-', color=color, linewidth=0.8, alpha=0.7)

    ax.axhline(y=0, color='red', linestyle='--', linewidth=1.0, alpha=0.5, label='Zero')
    ax.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1.0, alpha=0.7,
               label=f'$\\tau_{{DW}}$ = {TAU_DW:.4f}')
    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=12)
    ax.set_title(f'(A) All {n_tt} tracked TT eigenvalues', fontsize=11)
    from matplotlib.patches import Patch
    legend_patches = [
        Patch(facecolor='#1565C0', label='HARD(su2)'),
        Patch(facecolor='#E65100', label='SOFT(su2-C2)'),
        Patch(facecolor='#2E7D32', label='C2-C2'),
        Patch(facecolor='#7B1FA2', label='U1-mixed'),
    ]
    ax.legend(handles=legend_patches, fontsize=8, loc='upper right')
    ax.grid(alpha=0.3)

    # Panel B: Zoom on lowest eigenvalues
    ax = axes[0, 1]
    # Plot lowest 8 modes
    n_show = min(8, n_tt)
    for k in range(n_show):
        sector = tracked_sectors[0][k]
        color = sector_colors.get(sector, '#888')
        ax.plot(tau_fine, tracked[:, k], 'o-', color=color, linewidth=1.2,
                markersize=2, label=f'Mode {k} [{sector[:4]}]' if k < 6 else None)

    ax.axhline(y=0, color='red', linestyle='--', linewidth=1.0, alpha=0.5)
    ax.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1.0, alpha=0.7)

    # Mark crossings if any
    for mode, tau_c, _ in crossings:
        if mode < n_show:
            ax.axvline(x=tau_c, color='magenta', linestyle=':', alpha=0.8)
            ax.annotate(f'Mode {mode}\n$\\tau$={tau_c:.4f}',
                       xy=(tau_c, 0), fontsize=7, color='magenta',
                       ha='center', va='bottom')

    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'TT eigenvalue $\lambda$', fontsize=12)
    ax.set_title(f'(B) Lowest {n_show} modes (zoom)', fontsize=11)
    ax.legend(fontsize=7, loc='best')
    ax.grid(alpha=0.3)

    # Panel C: Gap lambda_min(tau) and derivatives
    ax = axes[1, 0]
    ax.plot(tau_fine, lambda_min, 'r-', linewidth=2, label=r'$\lambda_{\min}(\tau)$')
    ax.fill_between(tau_fine, lambda_min, lambda_max, alpha=0.1, color='blue')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.axvline(x=TAU_DW, color='k', linestyle='--', linewidth=1.0, alpha=0.7,
               label=f'$\\tau_{{DW}}$')

    # Mark global minimum
    ax.plot(tau_of_min, val_of_min, 'rv', markersize=8,
            label=f'Global min = {val_of_min:.6f}')

    ax.set_xlabel(r'$\tau$', fontsize=12)
    ax.set_ylabel(r'Eigenvalue', fontsize=12)
    ax.set_title(r'(C) Lichnerowicz gap $\lambda_{\min}(\tau)$', fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel D: Eigenvalue spacing distribution at tau_DW
    ax = axes[1, 1]
    ax.bar(range(len(spacings_dw)), spacings_dw, color='steelblue', edgecolor='black', linewidth=0.3)
    ax.axhline(y=np.mean(spacings_dw), color='red', linestyle='--', alpha=0.5,
               label=f'Mean = {np.mean(spacings_dw):.6f}')
    ax.set_xlabel('Pair index (sorted eigenvalues)', fontsize=12)
    ax.set_ylabel('Spacing', fontsize=12)
    ax.set_title(f'(D) Eigenvalue spacings at $\\tau$ = {tau_nearest_dw:.4f}', fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    fig_path = os.path.join(SCRIPT_DIR, 's60_lichnerowicz_dw.png')
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    log(f"  Saved: {fig_path}")

    t_end = time.time()
    log(f"\n  Total runtime: {t_end - t_start:.1f}s")
    log(f"\n{'='*78}")
    log(f"  DONE")
    log(f"{'='*78}")

    LOG.close()
    return gate_verdict


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log(f"\nERROR: {e}")
        traceback.print_exc()
        LOG.close()
        sys.exit(1)
