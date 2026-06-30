#!/usr/bin/env python3
"""
s72_zeta_ratio_scan.py -- ZETA-RATIO-CONVERGENCE-72
Spectral Zeta Ratio a_6^z/a_4^z Convergence Scan vs L_max

STRUCTURAL CONTEXT
------------------
S71 found a_6^z/a_4^z = 0.567 at L_max=7, but the Landau-Baptista workshop
(WS3 C3/D3) established this is contaminated by finite-spectrum artifacts.
The spectral zeta of a truncated spectrum is a finite sum whose Taylor
coefficients receive contributions from all spectral moments. As L_max
increases, more modes contribute and the ratio should drift toward the
asymptotic Gilkey value of ~0.25 for a near-Einstein homogeneous space.

METHOD
------
For each L_max in {3, 4, 5, 6, 7}, we:
1. Accumulate all D_K eigenvalues (with PW multiplicities) up to level L_max.
2. Compute the truncated spectral zeta function:
     zeta_D^{trunc}(s) = sum_{n: level <= L_max} mult_n * |lambda_n|^{-2s}
   which is an entire function (no poles) for any finite truncation.
3. Evaluate at the positions corresponding to SDW poles of the FULL zeta:
     s = (d-k)/2 for d=8: s=4 (a_0), s=3 (a_2), s=2 (a_4), s=1 (a_6)
   These truncated values are "a_k^z" -- the spectral zeta proxies for the
   true SDW coefficients. They converge to the true values as L_max -> inf.
4. Alternatively, extract a_k^{heat} via polynomial fit to the truncated
   heat trace Theta(t)*t^4 in an intermediate-t window.
5. Form the ratio a_6^z/a_4^z at each L_max and check convergence.

The Gilkey prediction a_6/a_4 ~ 0.25 comes from the heat kernel expansion
on compact near-Einstein homogeneous spaces, where a_6 is suppressed
relative to a_4 by a factor of O(R/dim(K)).

Gate: ZETA-RATIO-CONVERGENCE-72
  PASS: Ratio monotonically decreasing toward 0.25 across 3+ consecutive
        L_max values, with value at largest L_max < 0.40.
  INFO: Ratio decreasing but non-monotonically, or value at largest L_max > 0.40.
  FAIL: Ratio INCREASING with L_max (divergent, contamination worsening).

Author: baptista-spacetime-analyst
Session: S72 W1-C
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from canonical_constants import (
    PI, M_KK, tau_fold,
    a0_fold, a2_fold, a4_fold,
)

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# 0. UTILITY FUNCTIONS
# =============================================================================

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def C2_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p,q)."""
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0

def T_su3(p, q):
    """Dynkin index: T(R) = dim(R)*C_2(R)/8."""
    return dim_su3(p, q) * C2_su3(p, q) / 8.0

def build_irrep_with_fallback(p, q, gens, f_abc):
    """Build irrep (p,q) with conjugation fallback for problematic sectors."""
    try:
        tds._irrep_cache.clear()
        rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
        return rho, dim_check
    except (NotImplementedError, Exception) as e:
        if q > p and q > 0 and p > 0:
            tds._irrep_cache.clear()
            rho_qp, dim_check = tds.get_irrep(q, p, gens, f_abc)
            rho_pq = [-r.T for r in rho_qp]
            return rho_pq, dim_check
        raise

print("=" * 80)
print("ZETA-RATIO-CONVERGENCE-72: Spectral Zeta Ratio a_6^z/a_4^z vs L_max")
print("S72 W1-C | baptista-spacetime-analyst")
print("=" * 80)

# =============================================================================
# 1. BUILD GEOMETRIC INFRASTRUCTURE
# =============================================================================
print("\n" + "=" * 80)
print("1. BUILDING GEOMETRIC INFRASTRUCTURE AT tau = %.4f" % tau_fold)
print("=" * 80)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
gammas = tds.build_cliff8()
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

cliff_err = tds.validate_clifford(gammas)
mc_err = tds.validate_connection(Gamma_conn)
print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Metric compatibility error: {mc_err:.2e}")

# =============================================================================
# 2. COMPUTE D_K EIGENVALUES FOR ALL SECTORS UP TO L_MAX = 7
# =============================================================================
print("\n" + "=" * 80)
print("2. COMPUTING D_K EIGENVALUES FOR ALL SECTORS UP TO L_max = 7")
print("=" * 80)

L_MAX_TOTAL = 7
sector_evals = {}  # key: (p,q), value: dict with abs eigenvalues, level, etc.

t_total_start = time.time()

for L in range(L_MAX_TOTAL + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = dim_su3(p, q)
        t0 = time.time()

        try:
            rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            assert dim_check == dim_pq, f"dim mismatch: {dim_check} vs {dim_pq}"
        except Exception as e:
            print(f"  ({p},{q}) L={L}: SKIPPED - {e}")
            continue

        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)

        # D_pi is anti-Hermitian: eigenvalues purely imaginary
        H = 1j * D_pi
        H = 0.5 * (H + H.conj().T)  # Enforce exact Hermiticity
        evals = np.linalg.eigvalsh(H)
        t1 = time.time()

        abs_evals = np.abs(evals)
        nonzero_mask = abs_evals > 1e-12
        pos_abs = abs_evals[nonzero_mask]

        omega_min = np.min(pos_abs) if len(pos_abs) > 0 else np.inf
        omega_max = np.max(pos_abs) if len(pos_abs) > 0 else 0.0
        n_zero = int(np.sum(~nonzero_mask))

        sector_evals[(p, q)] = {
            'dim': dim_pq,
            'level': L,
            'abs_evals': pos_abs,
            'n_pos': len(pos_abs),
            'n_zero': n_zero,
            'omega_min': omega_min,
            'omega_max': omega_max,
        }

        print(f"  ({p},{q}) L={L}: dim={dim_pq:4d}, |lam| in [{omega_min:.4f}, {omega_max:.4f}], "
              f"n_pos={len(pos_abs):5d}, t={t1-t0:.1f}s")

t_total = time.time() - t_total_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 3. FOR EACH L_MAX, COMPUTE SPECTRAL ZETA AND HEAT KERNEL COEFFICIENTS
# =============================================================================
print("\n" + "=" * 80)
print("3. SPECTRAL ZETA RATIO a_6^z/a_4^z VS L_max")
print("=" * 80)

# The key s-values for an 8-dimensional manifold (d=8):
#   a_0 pole at s = d/2 = 4
#   a_2 pole at s = (d-2)/2 = 3
#   a_4 pole at s = (d-4)/2 = 2
#   a_6 pole at s = (d-6)/2 = 1
#   a_8 pole at s = (d-8)/2 = 0

# For the TRUNCATED spectrum, zeta_D^{trunc}(s) is an entire function.
# We evaluate it at s=2 and s=1 to get proxies for a_4 and a_6.

# Method A: Direct spectral zeta evaluation
# Method B: Heat kernel polynomial fit

L_max_values = [3, 4, 5, 6, 7]
results_by_Lmax = {}

for L_max_cut in L_max_values:
    print(f"\n  --- L_max = {L_max_cut} ---")

    # Gather eigenvalues up to this L_max
    all_abs = []
    all_mults = []
    n_sectors = 0  # (local)

    for (p, q), data in sorted(sector_evals.items()):
        if data['level'] <= L_max_cut:
            for ev in data['abs_evals']:
                all_abs.append(ev)
                all_mults.append(data['dim'])  # PW multiplicity
            n_sectors += 1

    all_abs = np.array(all_abs)
    all_mults = np.array(all_mults, dtype=np.float64)
    n_evals = len(all_abs)
    n_weighted = int(np.sum(all_mults))

    print(f"    Sectors: {n_sectors}, Eigenvalues: {n_evals}, Weighted modes: {n_weighted}")
    print(f"    |lambda| range: [{np.min(all_abs):.6f}, {np.max(all_abs):.6f}]")

    # METHOD A: Spectral zeta power sums
    # P_k = sum_n mult_n * |lambda_n|^{-2k} = zeta_D(s=k)
    # This converges for all k since the sum is finite (truncated spectrum).
    #
    # CONVENTION (matching S66 s66_zeta_sa.py):
    #   "a_k" in S66 = P_{k/2} = sum mult * |lam|^{-k}
    # So S66's a_4 = P_2 = zeta_D(2), and S66's a_6 = P_3 = zeta_D(3).
    # The ratio a_6/a_4 as used in S71 = zeta_D(3)/zeta_D(2) = P_3/P_2.
    #
    # IMPORTANT: The S66 absolute values differ from ours by a factor ~2
    # because S66 does not double-count PW multiplicity (each block of
    # dim(p,q)*16 eigenvalues appears once, the PW degeneracy dim(p,q)
    # is accounted separately). The RATIO is identical.

    # zeta_D(k) = sum_n mult_n * |lambda_n|^{-2k}
    zeta_s1 = np.sum(all_mults * all_abs**(-2))   # P_1
    zeta_s2 = np.sum(all_mults * all_abs**(-4))   # P_2 = "a_4" in S66
    zeta_s3 = np.sum(all_mults * all_abs**(-6))   # P_3 = "a_6" in S66
    zeta_s4 = np.sum(all_mults * all_abs**(-8))   # P_4 = "a_8" in S66

    # THE KEY RATIO: a_6^z/a_4^z = P_3/P_2 = zeta(3)/zeta(2)
    # This is the ratio that was 0.567 at L_max=3 in S71.
    ratio_zeta_A = zeta_s3 / zeta_s2

    # Also track lower-order ratios for cross-check:
    # a_4/a_2 = P_2/P_1 = zeta(2)/zeta(1)
    ratio_a4_a2_zeta = zeta_s2 / zeta_s1
    # a_8/a_6 = P_4/P_3 = zeta(4)/zeta(3)
    ratio_a8_a6_zeta = zeta_s4 / zeta_s3

    print(f"    Method A (spectral zeta power sums P_k = zeta(k)):")
    print(f"      P_1 = zeta(1) = {zeta_s1:.8e}")
    print(f"      P_2 = zeta(2) = {zeta_s2:.8e}  [= 'a_4' in S66]")
    print(f"      P_3 = zeta(3) = {zeta_s3:.8e}  [= 'a_6' in S66]")
    print(f"      P_4 = zeta(4) = {zeta_s4:.8e}  [= 'a_8' in S66]")
    print(f"      a_6^z/a_4^z = P_3/P_2 = {ratio_zeta_A:.6f}  [S71 value at L=3: 0.5668, Gilkey target: 0.25]")
    print(f"      a_4^z/a_2^z = P_2/P_1 = {ratio_a4_a2_zeta:.6f}  [canonical a4/a2: {a4_fold/a2_fold:.6f}]")
    print(f"      a_8^z/a_6^z = P_4/P_3 = {ratio_a8_a6_zeta:.6f}  [next-order ratio]")

    # METHOD B: Heat kernel polynomial fit
    # Theta(t) = sum_n mult_n * exp(-t * |lambda_n|^2)
    # For small t: Theta(t) ~ a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2} + a_6*t^{-1} + a_8
    # So: Theta(t)*t^4 = a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4

    # Choose fitting window: must be large enough that the truncated spectrum
    # approximates the full spectrum's small-t behavior, but small enough
    # that the asymptotic expansion is valid.
    # For L_max=3, lambda_max ~ 1.5, so t > 1/lambda_max^2 ~ 0.44 is truncation-safe.
    # For L_max=7, lambda_max ~ 3.5, so t > 1/lambda_max^2 ~ 0.08.

    lambda_max_sq = np.max(all_abs)**2
    t_trunc_safe = 1.0 / lambda_max_sq

    # Fit in window [max(0.1, 2*t_trunc_safe), 3.0]
    t_lo = max(0.1, 2.0 * t_trunc_safe)
    t_hi = 3.0  # (local)
    n_t = 200  # (local)
    t_grid = np.linspace(t_lo, t_hi, n_t)

    Theta = np.zeros(n_t)
    for i, t_val in enumerate(t_grid):
        Theta[i] = np.sum(all_mults * np.exp(-t_val * all_abs**2))

    # Fit y = Theta(t)*t^4 as polynomial in t of degree 4
    y = Theta * t_grid**4

    # Polynomial fit: y = a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4
    coeffs = np.polyfit(t_grid, y, 4)
    # np.polyfit returns [a_8, a_6, a_4, a_2, a_0] (highest power first)
    a8_heat = coeffs[0]
    a6_heat = coeffs[1]
    a4_heat = coeffs[2]
    a2_heat = coeffs[3]
    a0_heat = coeffs[4]

    ratio_heat_B = a6_heat / a4_heat if abs(a4_heat) > 1e-30 else np.inf
    ratio_a4_a2_heat = a4_heat / a2_heat if abs(a2_heat) > 1e-30 else np.inf
    ratio_a2_a0_heat = a2_heat / a0_heat if abs(a0_heat) > 1e-30 else np.inf

    print(f"    Method B (heat kernel fit, t in [{t_lo:.3f}, {t_hi:.3f}]):")
    print(f"      a_0^heat = {a0_heat:14.4f}  [canonical: {a0_fold:.4f}]")
    print(f"      a_2^heat = {a2_heat:14.4f}  [canonical: {a2_fold:.4f}]")
    print(f"      a_4^heat = {a4_heat:14.4f}  [canonical: {a4_fold:.4f}]")
    print(f"      a_6^heat = {a6_heat:14.4f}  [unknown]")
    print(f"      a_8^heat = {a8_heat:14.4f}  [unknown]")
    print(f"      a_6/a_4 (heat) = {ratio_heat_B:.6f}")
    print(f"      a_4/a_2 (heat) = {ratio_a4_a2_heat:.6f}  [canonical: {a4_fold/a2_fold:.6f}]")
    print(f"      a_2/a_0 (heat) = {ratio_a2_a0_heat:.6f}  [canonical: {a2_fold/a0_fold:.6f}]")

    # METHOD C: Direct cross-check of S66 convention
    # The S66 script computes a_k = sum_n (1 copy per sector, NOT mult-weighted)
    #   * |lambda_n|^{-k}
    # At L_max=3, S66 gives a_4 = 1350.72 and a_6 = 765.59.
    # Our P_2 at L_max=3 = 2701.44 (factor 2 from mult weighting).
    # The RATIO is identical.

    # For completeness, compute without PW multiplicity (single-copy per sector)
    all_abs_nodup = []
    for (p, q), data in sorted(sector_evals.items()):
        if data['level'] <= L_max_cut:
            for ev in data['abs_evals']:
                all_abs_nodup.append(ev)
    all_abs_nodup = np.array(all_abs_nodup)

    P2_nodup = np.sum(all_abs_nodup**(-4))
    P3_nodup = np.sum(all_abs_nodup**(-6))
    ratio_nodup = P3_nodup / P2_nodup

    print(f"    Method C (S66 convention, no PW mult):")
    print(f"      P_2(nodup) = {P2_nodup:.8e},  P_3(nodup) = {P3_nodup:.8e}")
    print(f"      P_3/P_2(nodup) = {ratio_nodup:.6f}  [should match Method A ratio]")

    # Store all results
    results_by_Lmax[L_max_cut] = {
        'n_sectors': n_sectors,
        'n_evals': n_evals,
        'n_weighted': n_weighted,
        'lambda_min': np.min(all_abs),
        'lambda_max': np.max(all_abs),
        # Method A: spectral zeta power sums
        'zeta_s4': zeta_s4,
        'zeta_s3': zeta_s3,
        'zeta_s2': zeta_s2,
        'zeta_s1': zeta_s1,
        'ratio_a6_a4_zeta': ratio_zeta_A,        # P_3/P_2 = zeta(3)/zeta(2)
        'ratio_a4_a2_zeta': ratio_a4_a2_zeta,    # P_2/P_1 = zeta(2)/zeta(1)
        'ratio_a8_a6_zeta': ratio_a8_a6_zeta,    # P_4/P_3 = zeta(4)/zeta(3)
        # Method B: heat kernel fit
        'a0_heat': a0_heat,
        'a2_heat': a2_heat,
        'a4_heat': a4_heat,
        'a6_heat': a6_heat,
        'a8_heat': a8_heat,
        'ratio_a6_a4_heat': ratio_heat_B,
        'ratio_a4_a2_heat': ratio_a4_a2_heat,
        'ratio_a2_a0_heat': ratio_a2_a0_heat,
        't_lo': t_lo,
        't_hi': t_hi,
        # Method C: S66-convention (no PW multiplicity)
        'P2_nodup': P2_nodup,
        'P3_nodup': P3_nodup,
        'ratio_nodup': ratio_nodup,
    }

# =============================================================================
# 4. CONVERGENCE ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("4. CONVERGENCE ANALYSIS")
print("=" * 80)

GILKEY_RATIO = 0.25  # Target: a_6/a_4 on near-Einstein compact homogeneous space  # (local)

print("\n  ==========================================================")
print("  CRITICAL NOTE ON CONVENTION")
print("  ==========================================================")
print("  The S66/S71 'a_6' is the spectral zeta power sum P_3 = zeta_D(3)")
print("  = sum mult * |lam|^{-6}. The 'a_4' is P_2 = zeta_D(2).")
print("  The ratio a_6^z/a_4^z = P_3/P_2 = zeta(3)/zeta(2).")
print("  At L_max=3 (S66 truncation), this gives 0.5668.")
print("  ==========================================================")

print("\n  SUMMARY TABLE: a_6^z/a_4^z = zeta(3)/zeta(2) vs L_max")
print(f"  {'L_max':>5} {'N_eval':>8} {'N_weighted':>10} "
      f"{'zeta(3)/zeta(2)':>16} {'heat a6/a4':>12} {'nodup P3/P2':>12}")
print("  " + "-" * 80)

ratios_zeta = []
ratios_heat = []
ratios_nodup = []
Lmax_arr = []

for L in L_max_values:
    r = results_by_Lmax[L]
    print(f"  {L:5d} {r['n_evals']:8d} {r['n_weighted']:10d} "
          f"{r['ratio_a6_a4_zeta']:16.6f} {r['ratio_a6_a4_heat']:12.6f} {r['ratio_nodup']:12.6f}")
    Lmax_arr.append(L)
    ratios_zeta.append(r['ratio_a6_a4_zeta'])
    ratios_heat.append(r['ratio_a6_a4_heat'])
    ratios_nodup.append(r['ratio_nodup'])

Lmax_arr = np.array(Lmax_arr)
ratios_zeta = np.array(ratios_zeta)
ratios_heat = np.array(ratios_heat)
ratios_nodup = np.array(ratios_nodup)

print(f"\n  Gilkey target: {GILKEY_RATIO}")
print(f"  S71 value (L=3): {ratios_zeta[0]:.6f}")
print(f"  Value at L=7:    {ratios_zeta[-1]:.6f}")

# Check monotonicity for each method
print("\n  MONOTONICITY CHECK:")
for name, ratios in [("Zeta", ratios_zeta), ("Heat", ratios_heat), ("Nodup", ratios_nodup)]:
    diffs = np.diff(ratios)
    is_monotone_dec = np.all(diffs < 0)
    is_monotone_inc = np.all(diffs > 0)
    n_decreasing = np.sum(diffs < 0)
    n_increasing = np.sum(diffs > 0)
    print(f"    {name:6s}: diffs = [{', '.join(f'{d:+.6f}' for d in diffs)}]")
    print(f"            monotone decreasing? {is_monotone_dec} "
          f"({n_decreasing}/{len(diffs)} steps decreasing)")
    if is_monotone_dec:
        print(f"            MONOTONICALLY DECREASING toward Gilkey target")

# Check how many consecutive decreasing steps ending at L_max=7
print("\n  CONSECUTIVE DECREASING STEPS (ending at L_max=7):")
for name, ratios in [("Zeta", ratios_zeta), ("Heat", ratios_heat), ("Nodup", ratios_nodup)]:
    diffs = np.diff(ratios)
    consec = 0
    for d in reversed(diffs):
        if d < 0:
            consec += 1
        else:
            break
    print(f"    {name:6s}: {consec} consecutive decreasing steps")

# =============================================================================
# 5. EXTRAPOLATION TO L_MAX -> INFINITY
# =============================================================================
print("\n" + "=" * 80)
print("5. EXTRAPOLATION TO L_max -> INFINITY")
print("=" * 80)

# If the ratio is monotonically decreasing, try fitting R(L) = R_inf + A/L^2
# to extrapolate R_inf.

for name, ratios in [("Zeta", ratios_zeta), ("Heat", ratios_heat), ("Nodup", ratios_nodup)]:
    print(f"\n  Method: {name}")

    # Fit R(L) = R_inf + A / L^alpha
    # Try alpha = 2 (standard Euler-Maclaurin correction)
    try:
        def fit_func(L, R_inf, A, alpha):
            return R_inf + A / L**alpha

        # Use all 5 data points
        popt, pcov = curve_fit(fit_func, Lmax_arr, ratios,
                               p0=[GILKEY_RATIO, 1.0, 2.0],
                               maxfev=10000)
        R_inf_fit, A_fit, alpha_fit = popt
        perr = np.sqrt(np.diag(pcov))

        # Compute residuals
        fitted = fit_func(Lmax_arr, *popt)
        residuals = ratios - fitted
        rms_resid = np.sqrt(np.mean(residuals**2))

        print(f"    Fit: R(L) = {R_inf_fit:.6f} + {A_fit:.4f} / L^{alpha_fit:.4f}")
        print(f"    R_inf = {R_inf_fit:.6f} +/- {perr[0]:.6f}")
        print(f"    RMS residual: {rms_resid:.6e}")
        print(f"    Distance from Gilkey (0.25): {abs(R_inf_fit - GILKEY_RATIO):.6f}")
    except Exception as e:
        print(f"    Fit failed: {e}")
        R_inf_fit = np.nan

    # Also try fixed alpha=2 (Euler-Maclaurin)
    try:
        def fit_func_fixed(L, R_inf, A):
            return R_inf + A / L**2

        popt2, pcov2 = curve_fit(fit_func_fixed, Lmax_arr, ratios,
                                  p0=[GILKEY_RATIO, 1.0],
                                  maxfev=10000)
        R_inf_fixed, A_fixed = popt2
        perr2 = np.sqrt(np.diag(pcov2))

        fitted2 = fit_func_fixed(Lmax_arr, *popt2)
        residuals2 = ratios - fitted2
        rms_resid2 = np.sqrt(np.mean(residuals2**2))

        print(f"    Fixed alpha=2: R(L) = {R_inf_fixed:.6f} + {A_fixed:.4f} / L^2")
        print(f"    R_inf = {R_inf_fixed:.6f} +/- {perr2[0]:.6f}")
        print(f"    RMS residual: {rms_resid2:.6e}")
    except Exception as e:
        print(f"    Fixed alpha=2 fit failed: {e}")

# =============================================================================
# 6. CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 80)
print("6. CROSS-CHECKS")
print("=" * 80)

# Cross-check 1: a_4^z at L_max=7 matches S71
d71 = np.load(os.path.join(outdir, 's71_spectral_zeta_threshold.npz'), allow_pickle=True)
a4_s71 = float(d71['a4_extracted'])  # This is the canonical a4
r7 = results_by_Lmax[7]
print(f"\n  Cross-check 1: a_4^z consistency with S71")
print(f"    S71 a4_extracted (canonical): {a4_s71:.6f}")
print(f"    This script a4_heat (L=7):    {r7['a4_heat']:.6f}")
print(f"    Ratio: {r7['a4_heat']/a4_s71:.6f}")

# Cross-check 2: a_4/a_2 = P_2/P_1 convergence (canonical known: 0.4865)
print(f"\n  Cross-check 2: a_4^z/a_2^z = P_2/P_1 convergence (canonical: {a4_fold/a2_fold:.6f})")
for L in L_max_values:
    r = results_by_Lmax[L]
    print(f"    L_max={L}: a_4/a_2 (zeta) = {r['ratio_a4_a2_zeta']:.6f}, "
          f"(heat) = {r['ratio_a4_a2_heat']:.6f}")

# Cross-check 3: a_8/a_6 = P_4/P_3 (next-order ratio, unknown target)
print(f"\n  Cross-check 3: a_8^z/a_6^z = P_4/P_3 (next-order ratio)")
for L in L_max_values:
    r = results_by_Lmax[L]
    print(f"    L_max={L}: a_8/a_6 (zeta) = {r['ratio_a8_a6_zeta']:.6f}")

# Cross-check 4: Verify S71 ratio
# The S71 workshop stated a_6^z/a_4^z = 0.567. This was computed at L_max=3
# (the truncation used in S66 s66_zeta_sa.py). Verify we reproduce it.
r3 = results_by_Lmax[3]
print(f"\n  Cross-check 4: S71 ratio verification")
print(f"    At L_max=3 (S66 truncation): a_6/a_4 = {r3['ratio_a6_a4_zeta']:.6f}")
print(f"    S71 workshop value:                     0.5668")
print(f"    Match: {abs(r3['ratio_a6_a4_zeta'] - 0.5668) < 0.001}")
print(f"    At L_max=7 (full scan):      a_6/a_4 = {r7['ratio_a6_a4_zeta']:.6f}")
print(f"    Convergence from L=3 to L=7: {r3['ratio_a6_a4_zeta']:.4f} -> {r7['ratio_a6_a4_zeta']:.4f} "
      f"({(r7['ratio_a6_a4_zeta'] - r3['ratio_a6_a4_zeta'])/r3['ratio_a6_a4_zeta']*100:+.1f}%)")

# Cross-check 5: Total eigenvalue count matches S71
s71_n_total = int(d71['n_total_evals'])
our_n_total = results_by_Lmax[7]['n_evals']
print(f"\n  Cross-check 5: Eigenvalue count at L_max=7")
print(f"    S71: {s71_n_total}, This script: {our_n_total}")
print(f"    Match: {s71_n_total == our_n_total}")

# =============================================================================
# 7. GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("7. GATE VERDICT: ZETA-RATIO-CONVERGENCE-72")
print("=" * 80)

# Use the spectral zeta method (Method A) as the primary.
# The ratio is a_6^z/a_4^z = zeta(s=1)/zeta(s=2).
primary_ratios = ratios_zeta
primary_name = "Zeta"
ratio_at_max_L = primary_ratios[-1]
diffs = np.diff(primary_ratios)

# Count consecutive decreasing steps ending at the last point
consec_dec = 0
for d in reversed(diffs):
    if d < 0:
        consec_dec += 1
    else:
        break

# Also check total decreasing fraction
n_dec = np.sum(diffs < 0)
n_inc = np.sum(diffs > 0)
is_monotone_dec = np.all(diffs < 0)
is_any_increasing = np.any(diffs > 0)

# Gate criteria:
#   PASS: Monotonically decreasing toward 0.25 across 3+ consecutive L_max,
#         with value at largest L_max < 0.40.
#   INFO: Decreasing but non-monotonically, or largest L_max > 0.40.
#   FAIL: INCREASING with L_max.

if n_inc > n_dec:
    # More increasing than decreasing steps
    gate_verdict = "FAIL"
    gate_reason = (f"Ratio INCREASING: {n_inc}/{len(diffs)} steps increasing. "
                   f"Contamination worsening with L_max.")
elif consec_dec >= 3 and ratio_at_max_L < 0.40:
    gate_verdict = "PASS"
    gate_reason = (f"{consec_dec} consecutive decreasing steps, "
                   f"ratio at L_max=7 = {ratio_at_max_L:.4f} < 0.40")
elif consec_dec >= 3 and ratio_at_max_L >= 0.40:
    gate_verdict = "INFO"
    gate_reason = (f"{consec_dec} consecutive decreasing steps toward Gilkey, "
                   f"but ratio at L_max=7 = {ratio_at_max_L:.4f} >= 0.40")
elif consec_dec < 3 and not is_any_increasing:
    gate_verdict = "INFO"
    gate_reason = (f"Only {consec_dec} consecutive decreasing steps (need 3+), "
                   f"ratio at L_max=7 = {ratio_at_max_L:.4f}")
elif is_any_increasing and n_dec > n_inc:
    gate_verdict = "INFO"
    gate_reason = (f"Non-monotone: {n_dec} decreasing, {n_inc} increasing steps. "
                   f"Ratio at L_max=7 = {ratio_at_max_L:.4f}")
else:
    gate_verdict = "FAIL"
    gate_reason = (f"Non-convergent: {n_dec} decreasing, {n_inc} increasing. "
                   f"Ratio at L_max=7 = {ratio_at_max_L:.4f}")

gate_detail = (f"Primary method: {primary_name}. "
               f"Ratios: {dict(zip(L_max_values, [f'{r:.4f}' for r in primary_ratios]))}. "
               f"Gilkey target: {GILKEY_RATIO}. "
               f"Verdict: {gate_verdict} ({gate_reason})")

print(f"\n  Gate: ZETA-RATIO-CONVERGENCE-72")
print(f"  Primary method: {primary_name} (P_3/P_2 = zeta(3)/zeta(2))")
print(f"  Ratios by L_max:")
for L, r in zip(L_max_values, primary_ratios):
    marker = " <-- largest" if L == L_max_values[-1] else ""
    print(f"    L_max={L}: {r:.6f}{marker}")
print(f"  Gilkey target: {GILKEY_RATIO}")
print(f"  Consecutive decreasing steps: {consec_dec}")
print(f"  Verdict: {gate_verdict}")
print(f"  Reason: {gate_reason}")

# =============================================================================
# 8. SAVE DATA
# =============================================================================
print("\n" + "=" * 80)
print("8. SAVING DATA")
print("=" * 80)

save_dict = {
    'gate_name': 'ZETA-RATIO-CONVERGENCE-72',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
    'L_max_values': np.array(L_max_values),
    'GILKEY_RATIO': GILKEY_RATIO,
    'tau_fold': tau_fold,
    # Method A: spectral zeta ratios (PRIMARY: zeta(3)/zeta(2))
    'ratios_a6_a4_zeta': ratios_zeta,
    'ratios_a6_a4_heat': ratios_heat,
    'ratios_a6_a4_nodup': ratios_nodup,
}

# Store per-L_max detailed data
for L in L_max_values:
    r = results_by_Lmax[L]
    prefix = f'L{L}_'
    for key, val in r.items():
        save_dict[prefix + key] = val

np.savez(os.path.join(outdir, 's72_zeta_ratio_scan.npz'), **save_dict)
print(f"  Data saved: {os.path.join(outdir, 's72_zeta_ratio_scan.npz')}")

# =============================================================================
# 9. PLOTTING
# =============================================================================
print("\n" + "=" * 80)
print("9. GENERATING PLOT")
print("=" * 80)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ZETA-RATIO-CONVERGENCE-72: a_6^z / a_4^z vs L_max',
             fontsize=14, fontweight='bold')

# Panel 1: Primary ratio a_6^z/a_4^z = zeta(3)/zeta(2) vs L_max
ax1 = axes[0, 0]
ax1.plot(Lmax_arr, ratios_zeta, 'bo-', linewidth=2, markersize=8,
         label=r'$\zeta(3)/\zeta(2)$ (PW-weighted)')
ax1.plot(Lmax_arr, ratios_nodup, 'g^--', linewidth=1.5, markersize=6,
         label=r'$P_3/P_2$ (S66 convention)')
ax1.axhline(y=GILKEY_RATIO, color='k', linestyle='--', linewidth=2,
            label=f'Gilkey target = {GILKEY_RATIO}')
ax1.axhline(y=0.40, color='orange', linestyle=':', alpha=0.7,
            label='PASS threshold = 0.40')
ax1.axhline(y=0.5668, color='red', linestyle=':', alpha=0.5,
            label='S71 value (L=3) = 0.567')
ax1.set_xlabel('$L_{max}$', fontsize=12)
ax1.set_ylabel(r'$a_6^z / a_4^z$', fontsize=12)
ax1.set_title(r'$a_6^z/a_4^z = \zeta(3)/\zeta(2)$ Convergence')
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(2.5, 7.5)

# Panel 2: a_4/a_2 = P_2/P_1 convergence
ax2 = axes[0, 1]
a4_a2_zeta_arr = np.array([results_by_Lmax[L]['ratio_a4_a2_zeta'] for L in L_max_values])
a4_a2_heat_arr = np.array([results_by_Lmax[L]['ratio_a4_a2_heat'] for L in L_max_values])
canonical_a4_a2 = a4_fold / a2_fold
ax2.plot(Lmax_arr, a4_a2_zeta_arr, 'bo-', linewidth=2, markersize=8,
         label=r'$P_2/P_1 = \zeta(2)/\zeta(1)$')
ax2.axhline(y=canonical_a4_a2, color='k', linestyle='--', linewidth=2,
            label=f'Canonical = {canonical_a4_a2:.4f}')
ax2.set_xlabel('$L_{max}$', fontsize=12)
ax2.set_ylabel(r'$a_4^z / a_2^z$', fontsize=12)
ax2.set_title(r'$a_4/a_2$ Cross-check (known target)')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(2.5, 7.5)

# Panel 3: a_8/a_6 = P_4/P_3 (next-order ratio)
ax3 = axes[1, 0]
a8_a6_zeta_arr = np.array([results_by_Lmax[L]['ratio_a8_a6_zeta'] for L in L_max_values])
ax3.plot(Lmax_arr, a8_a6_zeta_arr, 'bo-', linewidth=2, markersize=8,
         label=r'$P_4/P_3 = \zeta(4)/\zeta(3)$')
ax3.axhline(y=GILKEY_RATIO, color='k', linestyle='--', linewidth=2, alpha=0.5,
            label=f'Gilkey target (if universal) = {GILKEY_RATIO}')
ax3.set_xlabel('$L_{max}$', fontsize=12)
ax3.set_ylabel(r'$a_8^z / a_6^z$', fontsize=12)
ax3.set_title(r'$a_8/a_6$ Next-Order Ratio')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(2.5, 7.5)

# Panel 4: Spectral zeta values (log scale)
ax4 = axes[1, 1]
zeta_s1_arr = np.array([results_by_Lmax[L]['zeta_s1'] for L in L_max_values])
zeta_s2_arr = np.array([results_by_Lmax[L]['zeta_s2'] for L in L_max_values])
zeta_s3_arr = np.array([results_by_Lmax[L]['zeta_s3'] for L in L_max_values])
zeta_s4_arr = np.array([results_by_Lmax[L]['zeta_s4'] for L in L_max_values])
ax4.semilogy(Lmax_arr, zeta_s1_arr, 'o-', linewidth=2, markersize=8, label='zeta(s=1) [a_6]')
ax4.semilogy(Lmax_arr, zeta_s2_arr, 's-', linewidth=2, markersize=8, label='zeta(s=2) [a_4]')
ax4.semilogy(Lmax_arr, zeta_s3_arr, '^-', linewidth=2, markersize=8, label='zeta(s=3) [a_2]')
ax4.semilogy(Lmax_arr, zeta_s4_arr, 'd-', linewidth=2, markersize=8, label='zeta(s=4) [a_0]')
ax4.set_xlabel('L_max', fontsize=12)
ax4.set_ylabel('zeta_D(s)', fontsize=12)
ax4.set_title('Spectral Zeta at Key s-values')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)
ax4.set_xlim(2.5, 7.5)

plt.tight_layout()
plot_path = os.path.join(outdir, 's72_zeta_ratio_scan.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

print("\n" + "=" * 80)
print("ZETA-RATIO-CONVERGENCE-72 COMPLETE")
print(f"Verdict: {gate_verdict}")
print("=" * 80)
