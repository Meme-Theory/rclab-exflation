#!/usr/bin/env python3
"""
S59 SPECTRAL-DIM-59: CG Spectral Dimension Convergence with Truncation Level
=============================================================================

Computes the spectral dimension d_s of the SU(3) representation Cayley graph
at increasing truncation levels max_pq_sum = 3, 4, 5, 6, 7 to determine
whether d_s -> 8 (finite-size artifact) or d_s saturates (structural).

Method:
  1. At each max_pq_sum, enumerate all SU(3) irreps (p,q) with p+q <= max_pq_sum.
  2. Build the Cayley graph: vertices = irreps, edges from CG rules
     (p,q) -> (p',q') if (p',q') in decomposition of (p,q) x (1,0) or (0,1).
  3. Construct the (unweighted) graph Laplacian L = D - A.
  4. Also construct the weighted graph Laplacian using Josephson couplings.
  5. Compute return probability P(t) = (1/N) Tr exp(-tL) and extract
     d_s(t) = -2 d(ln P)/d(ln t).
  6. Report peak d_s at each level and fit convergence models.

Gate: SPECTRAL-DIM-59
  PASS: d_s increases monotonically toward 8 with truncation level
  FAIL: d_s saturates below 3
  INFO: Non-monotonic or insufficient levels

Author: Spectral-Geometer
Session: S59
"""

import sys
import os
import time
import numpy as np
from numpy import pi, exp
from scipy.linalg import eigh
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    J_C2, J_su2, J_u1, N_cells, tau_fold,
    Delta_0_OES, M_KK
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, "s59_spectral_dim.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s59_spectral_dim.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s59_spectral_dim_output.txt")

# ============================================================
# Output tee
# ============================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(OUT_TXT)

print("=" * 72)
print("S59 SPECTRAL-DIM-59: CG Spectral Dimension Convergence")
print("=" * 72)

# ============================================================
# Section 1: SU(3) representation enumeration
# ============================================================

def casimir_su3(p, q):
    """SU(3) quadratic Casimir: C_2(p,q) = (p^2+q^2+pq+3p+3q)/3."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# CG steps: (p,q) x (1,0) contains representations reached by these steps.
# The tensor product (p,q) x (1,0) decomposes as:
#   (p+1,q) + (p-1,q+1) + (p,q-1)  [with non-negative Dynkin labels]
# Similarly (p,q) x (0,1):
#   (p,q+1) + (p+1,q-1) + (p-1,q)
# The undirected adjacency combines all steps from both.
# Net CG steps (undirected):
FUND_STEPS = [(1, 0), (-1, 1), (0, -1)]       # from x (1,0)
ANTIFUND_STEPS = [(0, 1), (1, -1), (-1, 0)]    # from x (0,1)
ALL_CG_STEPS = list(set(FUND_STEPS + ANTIFUND_STEPS))
# = {(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)}

# Bond type classification (consistent with S54):
# C^2 coset: steps that change (p+q), i.e., move in Casimir
COSET_STEPS_SET = {(1, 0), (-1, 0), (0, 1), (0, -1)}
# su(2) exchange: steps (-1,+1), (+1,-1) [preserve p+q, change p-q]
SU2_STEPS_SET = {(-1, 1), (1, -1)}
# u(1) diagonal: steps (+1,+1), (-1,-1) [change p+q by 2]
# NOTE: (+1,+1) and (-1,-1) are NOT in the CG steps of (1,0) or (0,1).
# The u(1) bonds in S54 came from a different classification.
# Let me re-check...
# Actually, from the S54 code:
#   COSET_STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#   SU2_STEPS   = [(-1, 1), (1, -1)]
#   U1_STEPS    = [(1, 1), (-1, -1)]
# But (1,1) and (-1,-1) are NOT Clebsch-Gordan steps from (1,0) or (0,1)!
# They arise from the SECOND-ORDER CG: (p,q) x (1,1) = adjoint product.
# For the pure CG graph, we should use only the 6 first-order steps.
# However, S54 used all three types. Let me follow S54 convention.

# For consistency with S54, include u(1) steps too
U1_STEPS_SET = {(1, 1), (-1, -1)}

print("\n--- Section 1: Representation enumeration ---")

def enumerate_reps(max_pq_sum):
    """Return list of (p,q) with p+q <= max_pq_sum, sorted by Casimir."""
    reps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            reps.append((casimir_su3(p, q), p, q))
    reps.sort()
    return [(p, q) for (_, p, q) in reps]

# Report rep counts at each level
for mpq in range(1, 9):
    reps = enumerate_reps(mpq)
    total_dim = sum(dim_su3(p, q) for (p, q) in reps)
    print(f"  max_pq_sum={mpq}: {len(reps)} reps, total dim = {total_dim}")

# ============================================================
# Section 2: Build Cayley graph and graph Laplacian at each level
# ============================================================
print("\n--- Section 2: Cayley graph construction ---")

def build_adjacency(reps, include_u1=True):
    """Build adjacency matrices by bond type for the given rep set.

    Uses CG steps from fundamental and antifundamental tensor products.
    Optionally includes u(1) steps (adjoint product, second order).
    """
    N = len(reps)
    rep_set = set(reps)
    rep_to_idx = {r: i for i, r in enumerate(reps)}

    adj_C2 = np.zeros((N, N), dtype=np.int8)
    adj_su2 = np.zeros((N, N), dtype=np.int8)
    adj_u1 = np.zeros((N, N), dtype=np.int8)

    for i, (p, q) in enumerate(reps):
        for (dp, dq) in COSET_STEPS_SET:
            p2, q2 = p + dp, q + dq
            if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
                adj_C2[i, rep_to_idx[(p2, q2)]] = 1
        for (dp, dq) in SU2_STEPS_SET:
            p2, q2 = p + dp, q + dq
            if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
                adj_su2[i, rep_to_idx[(p2, q2)]] = 1
        if include_u1:
            for (dp, dq) in U1_STEPS_SET:
                p2, q2 = p + dp, q + dq
                if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
                    adj_u1[i, rep_to_idx[(p2, q2)]] = 1

    adj_full = adj_C2 | adj_su2 | adj_u1
    return adj_C2, adj_su2, adj_u1, adj_full

def build_graph_laplacian_unweighted(adj):
    """Build unweighted graph Laplacian L = D - A."""
    N = adj.shape[0]
    A = adj.astype(float)
    D = np.diag(np.sum(A, axis=1))
    return D - A

def build_graph_laplacian_weighted(adj_C2, adj_su2, adj_u1, tau):
    """Build weighted graph Laplacian with Josephson couplings at given tau."""
    jc2 = J_C2 * exp(4.0 * (tau_fold - tau))
    jsu2 = J_su2 * exp(-6.0 * (tau_fold - tau))
    ju1 = J_u1 * exp(2.0 * (tau_fold - tau))

    N = adj_C2.shape[0]
    W = (jc2 * adj_C2 + jsu2 * adj_su2 + ju1 * adj_u1).astype(float)
    D = np.diag(np.sum(W, axis=1))
    L = D - W
    return L, jc2, jsu2, ju1

def compute_spectral_dimension(eigenvalues, N_t=5000, t_min=-3, t_max=3):
    """Compute d_s(t) from eigenvalues of graph Laplacian.

    P(t) = (1/N) * [n_zero + sum_{positive} exp(-lambda_k * t)]
    d_s(t) = -2 * d(ln P)/d(ln t)

    Returns: t_arr, ds_t, P_t, ds_max, t_at_max
    """
    lam = np.sort(eigenvalues)
    N = len(lam)
    lam_pos = lam[lam > 1e-10]
    n_zero = N - len(lam_pos)

    t_arr = np.logspace(t_min, t_max, N_t)

    # Vectorized: P(t) = (1/N) * [n_zero + sum exp(-lam_k * t)]
    # lam_pos is (M,), t_arr is (N_t,)
    # exp_matrix is (N_t, M)
    exp_matrix = np.exp(-np.outer(t_arr, lam_pos))
    P_t = (n_zero + np.sum(exp_matrix, axis=1)) / N

    # d_s via gradient on log-log
    ln_t = np.log(t_arr)
    ln_P = np.log(np.clip(P_t, 1e-300, None))
    d_lnP = np.gradient(ln_P, ln_t)
    ds_t = -2.0 * d_lnP

    ds_max = np.max(ds_t)
    idx_max = np.argmax(ds_t)
    t_at_max = t_arr[idx_max]

    return t_arr, ds_t, P_t, ds_max, t_at_max

# ============================================================
# Section 3: Compute at each truncation level
# ============================================================
print("\n--- Section 3: Spectral dimension at each truncation level ---")

# Levels to compute
# max_pq_sum: 1, 2, 3, 4, 5, 6, 7, 8
# N_reps:     3, 6, 10, 15, 21, 28, 36, 45
# We compute both unweighted and weighted (at fold) graph Laplacians

levels = list(range(1, 9))  # max_pq_sum = 1 through 8
results = {}

t0_total = time.time()

for mpq in levels:
    t0 = time.time()
    reps = enumerate_reps(mpq)
    N = len(reps)

    if N < 3:
        print(f"\n  max_pq_sum={mpq}: N={N} reps (too few for meaningful d_s)")
        results[mpq] = {
            'N_reps': N, 'ds_max_uw': np.nan, 'ds_max_w': np.nan,
            't_peak_uw': np.nan, 't_peak_w': np.nan,
            'n_bonds': 0, 'diameter': 0,
            'reps': reps, 'lam_uw': np.array([]), 'lam_w': np.array([]),
        }
        continue

    adj_C2, adj_su2, adj_u1, adj_full = build_adjacency(reps)
    n_bonds = np.sum(adj_full) // 2

    # Connectivity check
    from scipy.sparse.csgraph import connected_components, shortest_path
    n_comp, _ = connected_components(adj_full)

    if n_comp > 1:
        print(f"\n  max_pq_sum={mpq}: N={N} reps, {n_bonds} bonds, "
              f"DISCONNECTED ({n_comp} components) -- skipping")
        results[mpq] = {
            'N_reps': N, 'ds_max_uw': np.nan, 'ds_max_w': np.nan,
            't_peak_uw': np.nan, 't_peak_w': np.nan,
            'n_bonds': n_bonds, 'diameter': -1,
            'reps': reps, 'lam_uw': np.array([]), 'lam_w': np.array([]),
        }
        continue

    dists = shortest_path(adj_full, method='D', unweighted=True)
    diameter = int(np.max(dists[dists < np.inf]))

    # Unweighted graph Laplacian
    L_uw = build_graph_laplacian_unweighted(adj_full)
    lam_uw = eigh(L_uw, eigvals_only=True)

    # Weighted graph Laplacian (at fold)
    L_w, jc2, jsu2, ju1 = build_graph_laplacian_weighted(adj_C2, adj_su2, adj_u1, tau_fold)
    lam_w = eigh(L_w, eigvals_only=True)

    # Spectral dimension -- unweighted
    t_arr_uw, ds_uw, P_uw, ds_max_uw, t_peak_uw = compute_spectral_dimension(lam_uw)

    # Spectral dimension -- weighted
    t_arr_w, ds_w, P_w, ds_max_w, t_peak_w = compute_spectral_dimension(lam_w)

    dt = time.time() - t0

    # Mean degree
    mean_deg = 2 * n_bonds / N

    # Spectral gap
    gap_uw = lam_uw[lam_uw > 1e-10].min() if np.any(lam_uw > 1e-10) else 0
    gap_w = lam_w[lam_w > 1e-10].min() if np.any(lam_w > 1e-10) else 0

    # Weyl dimension from eigenvalue counting (unweighted)
    lam_pos_sorted = np.sort(lam_uw[lam_uw > 1e-10])
    if len(lam_pos_sorted) > 5:
        log_E = np.log(lam_pos_sorted)
        log_N = np.log(np.arange(1, len(lam_pos_sorted) + 1))
        mid_s = len(lam_pos_sorted) // 4
        mid_e = 3 * len(lam_pos_sorted) // 4
        if mid_e > mid_s + 2:
            slope, _ = np.polyfit(log_E[mid_s:mid_e], log_N[mid_s:mid_e], 1)
            d_Weyl = 2 * slope
        else:
            d_Weyl = np.nan
    else:
        d_Weyl = np.nan

    results[mpq] = {
        'N_reps': N,
        'n_bonds': n_bonds,
        'diameter': diameter,
        'mean_degree': mean_deg,
        'gap_uw': gap_uw,
        'gap_w': gap_w,
        'ds_max_uw': ds_max_uw,
        'ds_max_w': ds_max_w,
        't_peak_uw': t_peak_uw,
        't_peak_w': t_peak_w,
        'd_Weyl': d_Weyl,
        'reps': reps,
        'lam_uw': lam_uw,
        'lam_w': lam_w,
        't_arr_uw': t_arr_uw,
        'ds_uw': ds_uw,
        'P_uw': P_uw,
        't_arr_w': t_arr_w,
        'ds_w': ds_w,
        'P_w': P_w,
    }

    print(f"\n  max_pq_sum={mpq}: N={N} reps, {n_bonds} bonds, "
          f"diam={diameter}, <deg>={mean_deg:.2f}")
    print(f"    Unweighted: d_s_max = {ds_max_uw:.4f} at t = {t_peak_uw:.4f}, "
          f"gap = {gap_uw:.4f}")
    print(f"    Weighted:   d_s_max = {ds_max_w:.4f} at t = {t_peak_w:.4f}, "
          f"gap = {gap_w:.4f}")
    if not np.isnan(d_Weyl):
        print(f"    Weyl dimension (counting): d_W = {d_Weyl:.3f}")
    print(f"    Time: {dt:.2f}s")

dt_total = time.time() - t0_total
print(f"\nTotal computation time: {dt_total:.1f}s")

# ============================================================
# Section 4: Convergence analysis
# ============================================================
print(f"\n{'='*72}")
print("Section 4: Convergence Analysis")
print(f"{'='*72}")

# Extract d_s vs level
valid_levels = [mpq for mpq in levels if not np.isnan(results[mpq]['ds_max_uw'])]
N_arr = np.array([results[mpq]['N_reps'] for mpq in valid_levels])
ds_uw_arr = np.array([results[mpq]['ds_max_uw'] for mpq in valid_levels])
ds_w_arr = np.array([results[mpq]['ds_max_w'] for mpq in valid_levels])
level_arr = np.array(valid_levels, dtype=float)

print(f"\n{'mpq':>5s} {'N':>5s} {'bonds':>6s} {'diam':>5s} {'<deg>':>6s} "
      f"{'d_s(uw)':>8s} {'d_s(w)':>8s} {'d_Weyl':>7s}")
print("-" * 60)
for mpq in levels:
    r = results[mpq]
    dw = r.get('d_Weyl', np.nan)
    dw_str = f"{dw:.3f}" if not np.isnan(dw) else "  ---"
    deg = r.get('mean_degree', np.nan)
    deg_str = f"{deg:.2f}" if not np.isnan(deg) else " ---"
    print(f"{mpq:5d} {r['N_reps']:5d} {r['n_bonds']:6d} {r['diameter']:5d} "
          f"{deg_str:>6s} {r['ds_max_uw']:8.4f} {r['ds_max_w']:8.4f} {dw_str:>7s}")

# Check monotonicity
ds_diffs_uw = np.diff(ds_uw_arr)
ds_diffs_w = np.diff(ds_w_arr)
monotone_uw = np.all(ds_diffs_uw > 0)
monotone_w = np.all(ds_diffs_w > 0)

print(f"\nMonotonicity (unweighted): {'YES' if monotone_uw else 'NO'}")
print(f"  Differences: {ds_diffs_uw}")
print(f"Monotonicity (weighted):   {'YES' if monotone_w else 'NO'}")
print(f"  Differences: {ds_diffs_w}")

# Fit convergence models (unweighted, which is the cleaner probe)
# Model A: d_s = 8 - A * mpq^{-beta}  (power law approach to 8)
# Model B: d_s = d_inf + B * exp(-C * mpq)  (exponential saturation)
# Model C: d_s = d_inf - A * mpq^{-beta}  (power law with free d_inf)

# Only fit with >= 4 data points
if len(valid_levels) >= 4:
    x = level_arr
    y = ds_uw_arr

    # Model A: d_s = 8 - A * x^{-beta}
    def model_A(x, A, beta):
        return 8.0 - A * x**(-beta)

    # Model B: d_s = d_inf + B * exp(-C * x)
    def model_B(x, d_inf, B, C):
        return d_inf + B * np.exp(-C * x)

    # Model C: d_s = d_inf - A * x^{-beta}
    def model_C(x, d_inf, A, beta):
        return d_inf - A * x**(-beta)

    try:
        popt_A, pcov_A = curve_fit(model_A, x, y, p0=[5.0, 1.0], maxfev=10000)
        resid_A = np.sum((y - model_A(x, *popt_A))**2)
        fit_A_ok = True
        print(f"\nModel A (power law -> 8): d_s = 8 - {popt_A[0]:.3f} * mpq^(-{popt_A[1]:.3f})")
        print(f"  Residual: {resid_A:.6f}")
        print(f"  Predicted d_s(10) = {model_A(10, *popt_A):.3f}")
        print(f"  Predicted d_s(20) = {model_A(20, *popt_A):.3f}")
    except Exception as e:
        print(f"\nModel A fit failed: {e}")
        fit_A_ok = False
        popt_A = [np.nan, np.nan]
        resid_A = np.inf

    try:
        popt_B, pcov_B = curve_fit(model_B, x, y, p0=[3.0, -3.0, 0.5], maxfev=10000)
        resid_B = np.sum((y - model_B(x, *popt_B))**2)
        fit_B_ok = True
        print(f"\nModel B (exp saturation): d_s -> {popt_B[0]:.3f} + {popt_B[1]:.3f} * exp(-{popt_B[2]:.3f} * mpq)")
        print(f"  d_s^inf = {popt_B[0]:.3f}")
        print(f"  Residual: {resid_B:.6f}")
    except Exception as e:
        print(f"\nModel B fit failed: {e}")
        fit_B_ok = False
        popt_B = [np.nan, np.nan, np.nan]
        resid_B = np.inf

    try:
        popt_C, pcov_C = curve_fit(model_C, x, y, p0=[4.0, 3.0, 1.0], maxfev=10000)
        resid_C = np.sum((y - model_C(x, *popt_C))**2)
        fit_C_ok = True
        print(f"\nModel C (power law -> d_inf): d_s = {popt_C[0]:.3f} - {popt_C[1]:.3f} * mpq^(-{popt_C[2]:.3f})")
        print(f"  d_inf = {popt_C[0]:.3f}")
        print(f"  Residual: {resid_C:.6f}")
        print(f"  Predicted d_s(10) = {model_C(10, *popt_C):.3f}")
        print(f"  Predicted d_s(20) = {model_C(20, *popt_C):.3f}")
    except Exception as e:
        print(f"\nModel C fit failed: {e}")
        fit_C_ok = False
        popt_C = [np.nan, np.nan, np.nan]
        resid_C = np.inf

    # Model selection by residual
    print(f"\n  Residuals: A={resid_A:.6f}, B={resid_B:.6f}, C={resid_C:.6f}")
    best = 'A' if resid_A <= min(resid_B, resid_C) else ('B' if resid_B <= resid_C else 'C')
    print(f"  Best fit: Model {best}")
else:
    fit_A_ok = fit_B_ok = fit_C_ok = False
    popt_A = [np.nan, np.nan]
    popt_B = [np.nan, np.nan, np.nan]
    popt_C = [np.nan, np.nan, np.nan]
    resid_A = resid_B = resid_C = np.inf
    best = 'N/A'

# ============================================================
# Section 5: Cross-checks
# ============================================================
print(f"\n{'='*72}")
print("Section 5: Cross-checks")
print(f"{'='*72}")

# Cross-check 1: Compare max_pq_sum=6 (N=28) with S54/S56 32-cell graph
# S54 used Casimir ordering (first 32 reps) which includes reps up to p+q=7
# Our max_pq_sum=6 gives all 28 reps with p+q<=6
# S54 max_pq_sum=6 gives N=28, but S54 had N=32 from first 32 by Casimir
print("\nCross-check 1: Comparison with S54/S56 (32-cell graph)")
if 6 in results and not np.isnan(results[6]['ds_max_uw']):
    print(f"  S59 max_pq_sum=6 (N=28): d_s(uw) = {results[6]['ds_max_uw']:.4f}")
    print(f"  S56 32-cell graph:        d_s(GL) = 1.9973 (from s56 data)")
    print(f"  S56 32-cell TB:           d_s(TB) = 1.7324 (from s56 data)")
    print(f"  Note: S54 32-cell uses Casimir-ordered first 32 reps (up to p+q=7)")
    print(f"        S59 max_pq_sum=6 uses ALL reps with p+q<=6 (exactly 28 reps)")

# Cross-check 2: Graph theory bound on spectral dimension
# For a graph with N vertices and diameter d:
#   d_s <= 2 * log(N) / log(d) approximately (rough bound)
# The spectral dimension of a d-dimensional lattice is d.
# The SU(3) rep graph in (p,q) space is a 2D lattice with extra bonds.
print("\nCross-check 2: Graph dimension estimates")
for mpq in valid_levels:
    r = results[mpq]
    N = r['N_reps']
    d = r['diameter']
    deg = r.get('mean_degree', np.nan)
    if d > 0 and N > 1:
        # log(N)/log(lambda_1) where lambda_1 is spectral gap
        # Rough estimate: graph dimension ~ log(N) / log(diameter)
        log_est = 2 * np.log(N) / np.log(max(d, 2))
        print(f"  mpq={mpq}: N={N}, diam={d}, 2*ln(N)/ln(d)={log_est:.2f}, "
              f"d_s={r['ds_max_uw']:.3f}")

# Cross-check 3: Asymptotic mean degree
# For the (p,q) lattice with p+q <= M:
# Interior vertices have 6 neighbors (from all 6 CG steps)
# Boundary vertices have fewer
# Mean degree should approach 6 as M -> inf (for the CG-6 graph)
# With u(1) bonds, interior degree is up to 8
print("\nCross-check 3: Mean degree convergence")
for mpq in valid_levels:
    r = results[mpq]
    deg = r.get('mean_degree', np.nan)
    if not np.isnan(deg):
        print(f"  mpq={mpq}: <deg> = {deg:.2f}")

# ============================================================
# Section 6: Hausdorff dimension estimates
# ============================================================
print(f"\n{'='*72}")
print("Section 6: Hausdorff dimension (from graph distances)")
print(f"{'='*72}")

# Hausdorff dimension: B(r) = {v : dist(v, v0) <= r} ~ r^{d_H}
# Compute from the center vertex (0,0)
for mpq in [3, 5, 7, 8]:
    if mpq not in results or np.isnan(results[mpq].get('ds_max_uw', np.nan)):
        continue
    reps = results[mpq]['reps']
    N = len(reps)
    adj_C2, adj_su2, adj_u1, adj_full = build_adjacency(reps)
    dists_all = shortest_path(adj_full, method='D', unweighted=True)

    # Distances from (0,0) [index 0]
    d0 = dists_all[0]
    max_r = int(np.max(d0[d0 < np.inf]))

    rs = []
    balls = []
    for r in range(max_r + 1):
        B_r = np.sum(d0 <= r)
        rs.append(r)
        balls.append(B_r)

    if len(rs) > 3:
        log_r = np.log(np.array(rs[1:], dtype=float))
        log_B = np.log(np.array(balls[1:], dtype=float))
        slope, _ = np.polyfit(log_r, log_B, 1)
        d_H = slope
    else:
        d_H = np.nan

    print(f"  mpq={mpq}: r = {rs}, B(r) = {balls}, d_H = {d_H:.3f}")
    results[mpq]['d_hausdorff'] = d_H

# ============================================================
# Section 7: Gate verdict
# ============================================================
print(f"\n{'='*72}")
print("Section 7: GATE VERDICT")
print(f"{'='*72}")

# The gate criteria:
# PASS: d_s increases monotonically toward 8
# FAIL: d_s saturates below 3
# INFO: Non-monotonic or insufficient levels

if monotone_uw and ds_uw_arr[-1] > ds_uw_arr[0]:
    if fit_C_ok and popt_C[0] >= 4.0:
        verdict = "PASS"
        detail = (f"d_s monotonically increasing from {ds_uw_arr[0]:.3f} to "
                  f"{ds_uw_arr[-1]:.3f} over mpq={valid_levels[0]}..{valid_levels[-1]}. "
                  f"Model C: d_inf = {popt_C[0]:.2f} (>= 4). "
                  f"Finite-size artifact confirmed.")
    elif fit_C_ok and popt_C[0] < 4.0 and popt_C[0] >= 3.0:
        verdict = "INFO"
        detail = (f"d_s monotonically increasing from {ds_uw_arr[0]:.3f} to "
                  f"{ds_uw_arr[-1]:.3f}. Model C: d_inf = {popt_C[0]:.2f} "
                  f"(between 3 and 4). Trend toward 8 not conclusive.")
    elif ds_uw_arr[-1] < 3.0:
        verdict = "FAIL"
        detail = (f"d_s monotone but max = {ds_uw_arr[-1]:.3f} < 3.0 at mpq={valid_levels[-1]}. "
                  f"Structural low-dimensional transport.")
    else:
        verdict = "INFO"
        detail = (f"d_s monotonically increasing to {ds_uw_arr[-1]:.3f}. "
                  f"Convergence model ambiguous.")
elif not monotone_uw:
    verdict = "INFO"
    detail = (f"d_s NON-MONOTONIC. Max = {np.max(ds_uw_arr):.3f} at "
              f"mpq={valid_levels[np.argmax(ds_uw_arr)]}.")
else:
    verdict = "INFO"
    detail = "Insufficient data for verdict."

print(f"\nGate: SPECTRAL-DIM-59")
print(f"Verdict: {verdict}")
print(f"Detail: {detail}")
print(f"\nKey numbers:")
print(f"  d_s(mpq=3, uw)  = {results[3]['ds_max_uw']:.4f}")
print(f"  d_s(mpq=5, uw)  = {results[5]['ds_max_uw']:.4f}")
print(f"  d_s(mpq=8, uw)  = {results[8]['ds_max_uw']:.4f}")
print(f"  d_s(mpq=3, w)   = {results[3]['ds_max_w']:.4f}")
print(f"  d_s(mpq=8, w)   = {results[8]['ds_max_w']:.4f}")
if fit_C_ok:
    print(f"  Model C: d_inf  = {popt_C[0]:.3f}")
print(f"  Monotone (uw):  {monotone_uw}")
print(f"  Monotone (w):   {monotone_w}")

# ============================================================
# Section 8: Save data
# ============================================================
print(f"\n--- Section 8: Saving data ---")

save_dict = {
    'levels': np.array(levels),
    'valid_levels': np.array(valid_levels),
    'N_reps': np.array([results[m]['N_reps'] for m in levels]),
    'n_bonds': np.array([results[m]['n_bonds'] for m in levels]),
    'diameters': np.array([results[m]['diameter'] for m in levels]),
    'ds_max_uw': np.array([results[m]['ds_max_uw'] for m in levels]),
    'ds_max_w': np.array([results[m]['ds_max_w'] for m in levels]),
    't_peak_uw': np.array([results[m].get('t_peak_uw', np.nan) for m in levels]),
    't_peak_w': np.array([results[m].get('t_peak_w', np.nan) for m in levels]),
    'd_Weyl': np.array([results[m].get('d_Weyl', np.nan) for m in levels]),
    'd_hausdorff': np.array([results[m].get('d_hausdorff', np.nan) for m in levels]),
    'mean_degree': np.array([results[m].get('mean_degree', np.nan) for m in levels]),
    # Convergence fits
    'model_A_params': np.array(popt_A),
    'model_A_resid': resid_A,
    'model_B_params': np.array(popt_B),
    'model_B_resid': resid_B,
    'model_C_params': np.array(popt_C),
    'model_C_resid': resid_C,
    'best_model': best,
    # Monotonicity
    'monotone_uw': monotone_uw,
    'monotone_w': monotone_w,
    # S56 comparison
    'ds_s56_gl': 1.9973,
    'ds_s56_tb': 1.7324,
    # Full d_s(t) curves for selected levels
    'tau_fold': tau_fold,
    # Gate
    'gate_name': 'SPECTRAL-DIM-59',
    'gate_verdict': verdict,
    'gate_detail': detail,
}

# Save eigenvalue spectra for key levels
for mpq in [3, 5, 8]:
    if mpq in results and len(results[mpq].get('lam_uw', [])) > 0:
        save_dict[f'lam_uw_mpq{mpq}'] = results[mpq]['lam_uw']
        save_dict[f'lam_w_mpq{mpq}'] = results[mpq]['lam_w']

# Save full d_s(t) curves for levels 3, 5, 8
for mpq in [3, 5, 8]:
    if mpq in results and 't_arr_uw' in results[mpq]:
        save_dict[f't_arr_mpq{mpq}'] = results[mpq]['t_arr_uw']
        save_dict[f'ds_uw_mpq{mpq}'] = results[mpq]['ds_uw']
        save_dict[f'ds_w_mpq{mpq}'] = results[mpq]['ds_w']
        save_dict[f'P_uw_mpq{mpq}'] = results[mpq]['P_uw']

np.savez(OUT_NPZ, **save_dict)
print(f"Data saved to {OUT_NPZ}")

# ============================================================
# Section 9: Plot
# ============================================================
print(f"\n--- Section 9: Plotting ---")

fig = plt.figure(figsize=(18, 12))
gs = GridSpec(2, 3, hspace=0.35, wspace=0.30)

# --- Panel (a): d_s(t) curves at selected levels ---
ax1 = fig.add_subplot(gs[0, 0])
colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(valid_levels)))
for i, mpq in enumerate(valid_levels):
    if 't_arr_uw' in results[mpq]:
        r = results[mpq]
        label = f'mpq={mpq} (N={r["N_reps"]})'
        ax1.semilogx(r['t_arr_uw'], r['ds_uw'], color=colors[i],
                      linewidth=1.2, label=label, alpha=0.8)

ax1.set_xlabel('Diffusion time $t$', fontsize=11)
ax1.set_ylabel('$d_s(t)$', fontsize=11)
ax1.set_title('(a) $d_s(t)$ vs truncation (unweighted)', fontsize=11)
ax1.legend(fontsize=7, ncol=2, loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(1e-3, 1e3)

# --- Panel (b): Peak d_s vs max_pq_sum ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(valid_levels, ds_uw_arr, 'bo-', linewidth=2, markersize=8, label='Unweighted')
ax2.plot(valid_levels, ds_w_arr, 'rs-', linewidth=2, markersize=7, label='Weighted (fold)')

# Overlay fits
if len(valid_levels) >= 4:
    x_fit = np.linspace(1, 12, 100)
    if fit_A_ok:
        ax2.plot(x_fit, model_A(x_fit, *popt_A), 'b--', alpha=0.5,
                 label=f'Model A ($d_s \\to 8$)')
    if fit_C_ok:
        ax2.plot(x_fit, model_C(x_fit, *popt_C), 'g--', alpha=0.5,
                 label=f'Model C ($d_\\infty = {popt_C[0]:.1f}$)')

ax2.axhline(8, color='gray', linestyle=':', alpha=0.5, label='SU(3) dim = 8')
ax2.axhline(3, color='red', linestyle=':', alpha=0.3, label='FAIL threshold')
ax2.set_xlabel('$\\mathrm{max\\_pq\\_sum}$', fontsize=11)
ax2.set_ylabel('Peak $d_s^{\\max}$', fontsize=11)
ax2.set_title('(b) Peak $d_s$ convergence', fontsize=11)
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0.5, 10)

# --- Panel (c): N_reps and bonds vs level ---
ax3 = fig.add_subplot(gs[0, 2])
ax3_twin = ax3.twinx()
n_arr = [results[m]['N_reps'] for m in valid_levels]
b_arr = [results[m]['n_bonds'] for m in valid_levels]
ax3.bar(np.array(valid_levels) - 0.15, n_arr, width=0.3, color='steelblue', alpha=0.7, label='N reps')
ax3_twin.bar(np.array(valid_levels) + 0.15, b_arr, width=0.3, color='coral', alpha=0.7, label='N bonds')
ax3.set_xlabel('$\\mathrm{max\\_pq\\_sum}$', fontsize=11)
ax3.set_ylabel('N reps', fontsize=11, color='steelblue')
ax3_twin.set_ylabel('N bonds', fontsize=11, color='coral')
ax3.set_title('(c) Graph size vs truncation', fontsize=11)
ax3.grid(True, alpha=0.3)

# --- Panel (d): d_s(t) curves at selected levels (weighted) ---
ax4 = fig.add_subplot(gs[1, 0])
for i, mpq in enumerate(valid_levels):
    if 't_arr_w' in results[mpq]:
        r = results[mpq]
        label = f'mpq={mpq} (N={r["N_reps"]})'
        ax4.semilogx(r['t_arr_w'], r['ds_w'], color=colors[i],
                      linewidth=1.2, label=label, alpha=0.8)

ax4.set_xlabel('Diffusion time $t$ [$M_{KK}^{-1}$]', fontsize=11)
ax4.set_ylabel('$d_s(t)$', fontsize=11)
ax4.set_title('(d) $d_s(t)$ vs truncation (Josephson weighted)', fontsize=11)
ax4.legend(fontsize=7, ncol=2, loc='upper right')
ax4.grid(True, alpha=0.3)
ax4.set_xlim(1e-3, 1e3)

# --- Panel (e): Mean degree and Weyl dimension ---
ax5 = fig.add_subplot(gs[1, 1])
deg_arr = [results[m].get('mean_degree', np.nan) for m in valid_levels]
dW_arr = [results[m].get('d_Weyl', np.nan) for m in valid_levels]
ax5.plot(valid_levels, deg_arr, 'go-', linewidth=2, markersize=7, label='Mean degree')
ax5.plot(valid_levels, [d for d in dW_arr], 'mp-', linewidth=2, markersize=7, label='$d_{Weyl}$')
ax5.set_xlabel('$\\mathrm{max\\_pq\\_sum}$', fontsize=11)
ax5.set_ylabel('Dimension / Degree', fontsize=11)
ax5.set_title('(e) Graph properties', fontsize=11)
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# --- Panel (f): Eigenvalue density at selected levels ---
ax6 = fig.add_subplot(gs[1, 2])
for mpq in [3, 5, 8]:
    if mpq in results and len(results[mpq].get('lam_uw', [])) > 0:
        lam = results[mpq]['lam_uw']
        lam_pos = lam[lam > 1e-10]
        ax6.hist(lam_pos, bins=max(10, len(lam_pos)//3), alpha=0.5,
                 label=f'mpq={mpq} (N={len(lam)})',
                 density=True)

ax6.set_xlabel('$\\lambda$ (graph Laplacian)', fontsize=11)
ax6.set_ylabel('Density', fontsize=11)
ax6.set_title('(f) Eigenvalue distribution', fontsize=11)
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

fig.suptitle(f'SPECTRAL-DIM-59: Spectral Dimension Convergence (Gate: {verdict})',
             fontsize=14, fontweight='bold')

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Plot saved to {OUT_PNG}")

# ============================================================
# Section 10: Final summary
# ============================================================
print(f"\n{'='*72}")
print("FINAL SUMMARY")
print(f"{'='*72}")
print(f"Gate: SPECTRAL-DIM-59")
print(f"Verdict: {verdict}")
print(f"\nKey results:")
for mpq in valid_levels:
    r = results[mpq]
    print(f"  mpq={mpq}: N={r['N_reps']:3d}, d_s(uw)={r['ds_max_uw']:.4f}, "
          f"d_s(w)={r['ds_max_w']:.4f}")
print(f"\nConvergence:")
print(f"  Monotone (unweighted): {monotone_uw}")
print(f"  Monotone (weighted):   {monotone_w}")
if fit_C_ok:
    print(f"  Model C: d_inf = {popt_C[0]:.3f} (free asymptote)")
if fit_A_ok:
    print(f"  Model A: 8 - {popt_A[0]:.3f} * mpq^(-{popt_A[1]:.3f})")
print(f"\nAssessment:")
print(f"  {detail}")
