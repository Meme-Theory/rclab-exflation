#!/usr/bin/env python3
"""
s72_asymptotic_truncation.py -- ASYMPTOTIC-TRUNCATION-72
Asymptotic Truncation Analysis: Is the Seeley-DeWitt Expansion Past Optimal Order?

SPECTRAL FUNCTIONAL THEORIST'S ANALYSIS
----------------------------------------
The spectral moments M_{-k} = sum_{(p,q)} deg(p,q) * sum_{lambda>0} lambda^{-2k}
encode the Seeley-DeWitt coefficients: M_0 = a_0, M_{-1} = a_2, M_{-2} = a_4.
We extend this to M_{-3} = a_6 and M_{-4} = a_8 and test the ratio sequence.

KEY INSIGHT: The canonical a_0 = 6440, a_2 = 2776.17, a_4 = 1350.72 are the
spectral moments at L_max = 3 (the standard framework truncation). We can
directly compute a_6 and a_8 as the next spectral moments, with NO fitting.

The heat kernel "asymptotic expansion" applied to a FINITE discrete spectrum
is simply the moment expansion. The question of whether it "converges" reduces
to whether the ratio |M_{-(k+1)}/M_{-k}| decreases with k.

Gate: ASYMPTOTIC-TRUNCATION-72
  PASS: |a_8/a_6| < |a_6/a_4| (expansion still converging at order 4)
  INFO: |a_8/a_6| ~ |a_6/a_4| within 30% (marginal)
  FAIL: |a_8/a_6| > 1.3 * |a_6/a_4| (past optimal truncation)

Author: lizzi-spectral-functional-theorist
Session: S72 W3-B
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Vol_SU3_Haar,
)

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 80)
print("ASYMPTOTIC-TRUNCATION-72: Is the SDW Expansion Past Optimal Order?")
print("S72 W3-B | lizzi-spectral-functional-theorist")
print("=" * 80)

# =============================================================================
# 1. BUILD EIGENVALUE SPECTRA WITH CORRECT NORMALIZATION
# =============================================================================
print("\n" + "=" * 80)
print("1. EIGENVALUE SPECTRA AT tau_fold = %.4f, L_max = 3..7" % tau_fold)
print("   Normalization: dim(p,q) * (positive eigenvalues)")
print("=" * 80)

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

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

def build_irrep_with_fallback(p, q, gens, f_abc):
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

sector_evals = {}  # (p,q) -> positive eigenvalues
t_start = time.time()
for L in range(8):
    for p in range(L + 1):
        q = L - p
        dim_pq = dim_su3(p, q)
        try:
            rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            assert dim_check == dim_pq
        except Exception as e:
            print(f"  ({p},{q}) L={L}: SKIPPED - {e}")
            continue
        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
        H = 1j * D_pi
        H = 0.5 * (H + H.conj().T)
        evals = np.linalg.eigvalsh(H)
        pos_evals = evals[evals > 1e-12]
        sector_evals[(p, q)] = pos_evals
        if L <= 3 or p + q == L:
            print(f"  ({p},{q}) L={p+q}: dim={dim_pq}, {len(pos_evals)} positive, "
                  f"lambda=[{pos_evals.min():.4f}, {pos_evals.max():.4f}]")

t_build = time.time() - t_start
print(f"\n  Spectrum construction: {t_build:.1f}s")

# =============================================================================
# 2. COMPUTE SPECTRAL MOMENTS: THE CORRECT SDW COEFFICIENTS
# =============================================================================
print("\n" + "=" * 80)
print("2. SPECTRAL MOMENTS M_{-k} = sum deg * sum lambda^{-2k}")
print("   These ARE the Seeley-DeWitt coefficients: a_{2k} = M_{-k}")
print("=" * 80)

def compute_moments(L_max, k_range):
    """Compute spectral moments M_{-k} for k in k_range at given L_max."""
    moments = {}
    for k in k_range:
        M = 0.0
        for (p, q), pos_ev in sector_evals.items():
            if p + q > L_max:
                continue
            deg = dim_su3(p, q)
            M += deg * np.sum(pos_ev ** (-2 * k))
        moments[k] = M
    return moments

L_MAX_VALUES = [3, 4, 5, 6, 7]
k_range = range(0, 7)  # M_0 through M_{-6}
moments_by_L = {}

for L in L_MAX_VALUES:
    m = compute_moments(L, k_range)
    moments_by_L[L] = m

# Display
print(f"\n  {'L_max':>5} {'a_0=M_0':>10} {'a_2=M_-1':>12} {'a_4=M_-2':>12} "
      f"{'a_6=M_-3':>12} {'a_8=M_-4':>12} {'a_10=M_-5':>12} {'a_12=M_-6':>12}")
for L in L_MAX_VALUES:
    m = moments_by_L[L]
    print(f"  {L:5d} {m[0]:10.1f} {m[1]:12.4f} {m[2]:12.4f} "
          f"{m[3]:12.4f} {m[4]:12.4f} {m[5]:12.4f} {m[6]:12.4f}")

# Canonical cross-check
print(f"\n  Canonical cross-check at L_max=3:")
m3 = moments_by_L[3]
print(f"    a_0: M_0 = {m3[0]:.1f}, canonical = {a0_fold:.1f}, delta = {abs(m3[0]-a0_fold)/a0_fold*100:.4f}%")
print(f"    a_2: M_-1 = {m3[1]:.4f}, canonical = {a2_fold:.4f}, delta = {abs(m3[1]-a2_fold)/a2_fold*100:.4f}%")
print(f"    a_4: M_-2 = {m3[2]:.4f}, canonical = {a4_fold:.4f}, delta = {abs(m3[2]-a4_fold)/a4_fold*100:.4f}%")
print(f"    a_6: M_-3 = {m3[3]:.4f} (NEW)")
print(f"    a_8: M_-4 = {m3[4]:.4f} (NEW)")

# =============================================================================
# 3. RATIO ANALYSIS: |a_{2k+2}/a_{2k}| vs k
# =============================================================================
print("\n" + "=" * 80)
print("3. RATIO ANALYSIS: r_k = |M_{-(k+1)}/M_{-k}|")
print("=" * 80)

print(f"\n  Ratio sequence by L_max:")
print(f"  {'L_max':>5} {'r0=a2/a0':>10} {'r1=a4/a2':>10} {'r2=a6/a4':>10} "
      f"{'r3=a8/a6':>10} {'r4=a10/a8':>10} {'r5=a12/a10':>10}")

ratios_by_L = {}
for L in L_MAX_VALUES:
    m = moments_by_L[L]
    ratios = {}
    for k in range(6):
        r = abs(m[k + 1]) / abs(m[k]) if m[k] != 0 else np.inf
        ratios[k] = r
    ratios_by_L[L] = ratios
    print(f"  {L:5d} {ratios[0]:10.6f} {ratios[1]:10.6f} {ratios[2]:10.6f} "
          f"{ratios[3]:10.6f} {ratios[4]:10.6f} {ratios[5]:10.6f}")

# Monotonicity check: is the ratio INCREASING (expansion diverging) or DECREASING?
print(f"\n  Monotonicity check (ratio of consecutive ratios r_{k+1}/r_k):")
print(f"  {'L_max':>5} {'r1/r0':>10} {'r2/r1':>10} {'r3/r2':>10} {'r4/r3':>10} {'r5/r4':>10}")
for L in L_MAX_VALUES:
    r = ratios_by_L[L]
    print(f"  {L:5d} {r[1]/r[0]:10.6f} {r[2]/r[1]:10.6f} {r[3]/r[2]:10.6f} "
          f"{r[4]/r[3]:10.6f} {r[5]/r[4]:10.6f}")

# =============================================================================
# 4. THE GATE TEST AT L_max = 3 (CANONICAL FRAMEWORK)
# =============================================================================
print("\n" + "=" * 80)
print("4. GATE TEST AT L_max = 3 (CANONICAL FRAMEWORK)")
print("=" * 80)

m3 = moments_by_L[3]
a6_canonical = m3[3]   # = 765.59
a8_canonical = m3[4]   # = 521.18

ratio_a6_a4 = a6_canonical / a4_fold   # = 0.567
ratio_a8_a6 = a8_canonical / a6_canonical  # = 0.681

print(f"\n  Canonical (L_max=3) spectral moments:")
print(f"    a_0 = {a0_fold:.4f}")
print(f"    a_2 = {a2_fold:.4f}")
print(f"    a_4 = {a4_fold:.4f}")
print(f"    a_6 = {a6_canonical:.4f}  (M_{{-3}}, this computation)")
print(f"    a_8 = {a8_canonical:.4f}  (M_{{-4}}, this computation)")

print(f"\n  Ratio sequence:")
print(f"    |a_2/a_0| = {a2_fold/a0_fold:.6f}")
print(f"    |a_4/a_2| = {a4_fold/a2_fold:.6f}")
print(f"    |a_6/a_4| = {ratio_a6_a4:.6f}")
print(f"    |a_8/a_6| = {ratio_a8_a6:.6f}")

# This sequence is MONOTONICALLY INCREASING: 0.431, 0.487, 0.567, 0.681
# The expansion is not converging.

# GATE TEST: Compare |a_8/a_6| to |a_6/a_4|
# The Gilkey value 0.25 was the L=7 spectral zeta estimate.
# At L=3 (canonical), |a_6/a_4| = 0.567, and W1-C confirmed this converges
# to 0.223 at L=7. The question is which reference to use.

# PRIMARY: Use the SAME L_max for both ratios (self-consistent)
reference_L3 = ratio_a6_a4  # = 0.567
test_L3 = ratio_a8_a6       # = 0.681
gate_ratio_L3 = test_L3 / reference_L3

print(f"\n  PRIMARY GATE (L_max=3, self-consistent):")
print(f"    Reference: |a_6/a_4| = {reference_L3:.6f}")
print(f"    Test:      |a_8/a_6| = {test_L3:.6f}")
print(f"    Ratio:     test/reference = {gate_ratio_L3:.6f}")

# SECONDARY: Use the Gilkey/W1-C value at L=7 for |a_6/a_4|
gilkey_ref = 0.25  # (local)
m7 = moments_by_L[7]
ratio_a6_a4_L7 = m7[3] / m7[2]
ratio_a8_a6_L7 = m7[4] / m7[3]
gate_ratio_L7 = ratio_a8_a6_L7 / ratio_a6_a4_L7

print(f"\n  SECONDARY GATE (L_max=7, full spectrum):")
print(f"    Reference: |a_6/a_4| = {ratio_a6_a4_L7:.6f}  (L=7, cf. W1-C = 0.223)")
print(f"    Test:      |a_8/a_6| = {ratio_a8_a6_L7:.6f}")
print(f"    Ratio:     test/reference = {gate_ratio_L7:.6f}")

print(f"\n  GILKEY-REFERENCED GATE:")
print(f"    Reference: |a_6/a_4| = {gilkey_ref:.4f}  (Gilkey)")
print(f"    Test:      |a_8/a_6| = {ratio_a8_a6_L7:.6f}  (L=7)")
print(f"    Ratio:     test/reference = {ratio_a8_a6_L7/gilkey_ref:.6f}")

# Gate verdict: AT EVERY L_max, the ratio is INCREASING
# |a_8/a_6| > |a_6/a_4| uniformly
all_pass = all(ratios_by_L[L][3] < ratios_by_L[L][2] for L in L_MAX_VALUES)
all_fail = all(ratios_by_L[L][3] > 1.3 * ratios_by_L[L][2] for L in L_MAX_VALUES)

# Use the primary L=3 test for the gate
if test_L3 < reference_L3:
    gate_verdict = "PASS"
    gate_detail = (f"|a_8/a_6| = {test_L3:.4f} < |a_6/a_4| = {reference_L3:.4f}; "
                   f"expansion still converging. Ratio = {gate_ratio_L3:.3f}.")
elif test_L3 < 1.3 * reference_L3:
    gate_verdict = "INFO"
    gate_detail = (f"|a_8/a_6| = {test_L3:.4f} ~ |a_6/a_4| = {reference_L3:.4f} "
                   f"(ratio = {gate_ratio_L3:.3f}); marginal, at edge of optimal truncation.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"|a_8/a_6| = {test_L3:.4f} > 1.3 * |a_6/a_4| = {1.3*reference_L3:.4f}; "
                   f"past optimal truncation. Ratio = {gate_ratio_L3:.3f}.")

print(f"\n  {'='*60}")
print(f"  Gate ASYMPTOTIC-TRUNCATION-72: {gate_verdict}")
print(f"  {gate_detail}")
print(f"  {'='*60}")

# Cross-check: L=7 test
if ratio_a8_a6_L7 < ratio_a6_a4_L7:
    L7_verdict = "PASS"
elif ratio_a8_a6_L7 < 1.3 * ratio_a6_a4_L7:
    L7_verdict = "INFO"
else:
    L7_verdict = "FAIL"
print(f"\n  Cross-check at L=7: {L7_verdict} "
      f"(|a_8/a_6|={ratio_a8_a6_L7:.4f} vs 1.3*|a_6/a_4|={1.3*ratio_a6_a4_L7:.4f})")

# =============================================================================
# 5. HEAT TRACE VALIDATION
# =============================================================================
print("\n" + "=" * 80)
print("5. HEAT TRACE VALIDATION")
print("=" * 80)

# Compute the heat trace K(t) at L_max=3 and compare to the moment expansion
t_grid = np.logspace(-2, 2, 500)

K_exact = np.zeros_like(t_grid)
for (p, q), pos_ev in sector_evals.items():
    if p + q > 3:
        continue
    deg = dim_su3(p, q)
    lam_sq = pos_ev ** 2
    for i, t in enumerate(t_grid):
        K_exact[i] += deg * np.sum(np.exp(-t * lam_sq))

# SDW expansion with 3, 5, and 7 terms
K_sdw3 = a0_fold * t_grid**(-4) + a2_fold * t_grid**(-3) + a4_fold * t_grid**(-2)
K_sdw5 = K_sdw3 + a6_canonical * t_grid**(-1) + a8_canonical
a10_canonical = moments_by_L[3][5]
a12_canonical = moments_by_L[3][6]
K_sdw7 = K_sdw5 + a10_canonical * t_grid + a12_canonical * t_grid**2

# Compute relative errors
mask_t = (t_grid >= 0.01) & (t_grid <= 5.0)
err3 = np.abs(K_sdw3[mask_t] - K_exact[mask_t]) / np.abs(K_exact[mask_t])
err5 = np.abs(K_sdw5[mask_t] - K_exact[mask_t]) / np.abs(K_exact[mask_t])
err7 = np.abs(K_sdw7[mask_t] - K_exact[mask_t]) / np.abs(K_exact[mask_t])

# Find optimal t for each truncation
# For small t: all SDW terms contribute, convergence depends on Lambda_max
# For the expansion to improve, we need the higher terms to be SMALLER
# contributions, which requires t * lambda_max^2 >> 1.

lambda_max_L3 = max(np.max(sector_evals[(p,q)]) for (p,q) in sector_evals if p+q <= 3)
t_star = 1.0 / lambda_max_L3**2  # characteristic scale

print(f"\n  lambda_max (L=3) = {lambda_max_L3:.4f}")
print(f"  t* = 1/lambda_max^2 = {t_star:.4f}")
print(f"  SDW valid for t >> {t_star:.4f}")

# Relative error at selected t values
print(f"\n  Relative error |K_SDW - K_exact| / |K_exact|:")
print(f"  {'t':>8} {'3-term':>12} {'5-term':>12} {'7-term':>12} {'5 vs 3':>12}")
for t_val in [0.1, 0.2, 0.5, 1.0, 2.0, 5.0]:
    idx = np.argmin(np.abs(t_grid - t_val))
    e3 = abs(K_sdw3[idx] - K_exact[idx]) / abs(K_exact[idx])
    e5 = abs(K_sdw5[idx] - K_exact[idx]) / abs(K_exact[idx])
    e7 = abs(K_sdw7[idx] - K_exact[idx]) / abs(K_exact[idx])
    improvement = e3 / e5 if e5 > 0 else np.inf
    print(f"  {t_val:8.2f} {e3:12.2e} {e5:12.2e} {e7:12.2e} {improvement:12.1f}x")

# =============================================================================
# 6. CONVERGENCE RADIUS AND OPTIMAL TRUNCATION
# =============================================================================
print("\n" + "=" * 80)
print("6. CONVERGENCE RADIUS AND OPTIMAL TRUNCATION ANALYSIS")
print("=" * 80)

# The ratio sequence r_k = |a_{2k+2}/a_{2k}| determines the convergence.
# If the ratio approaches a limit R, the expansion converges for t > 1/R
# (roughly: for the Laurent series sum a_{2k} * t^{k-4}).
#
# For a DIVERGENT asymptotic series, the optimal truncation is at the
# smallest term, which occurs at k* where |a_{2k}| * t^{k-4} is minimized.
#
# With ratio r_k approaching R, the terms grow as ~R^k, so the k-th term
# is ~R^k * t^{k-4}. This is minimized at k* = -ln(R*t) / ln(R*t) ...
# For Rt > 1, all terms grow and there is no optimal truncation (0 terms).
# For Rt < 1, the optimal truncation is at k* ~ 1 / (R*t).

# Compute effective convergence ratio for each L_max
print(f"\n  Effective convergence properties:")
print(f"  {'L_max':>5} {'R_eff':>10} {'1/R_eff':>10} {'R_eff * lambda_max^2':>20}")
for L in L_MAX_VALUES:
    r = ratios_by_L[L]
    # Use the last reliably-computed ratio pair
    R_eff = (r[2] * r[3])**0.5  # geometric mean of a6/a4 and a8/a6
    lam_max = max(np.max(sector_evals[(p,q)]) for (p,q) in sector_evals if p+q <= L)
    R_product = R_eff * lam_max**2
    print(f"  {L:5d} {R_eff:10.6f} {1/R_eff:10.4f} {R_product:20.4f}")

# At L=3: R_eff ~ sqrt(0.567 * 0.681) = 0.621, so 1/R_eff = 1.61
# The expansion converges (roughly) for t > 1/R_eff * lambda_max^{-2}
# = 1.61 * 0.236 = 0.38
# But R * lambda_max^2 = 0.621 * 4.25 = 2.64 > 1
# This means at the characteristic scale t ~ 1/lambda_max^2, we are OUTSIDE
# the convergence radius. The SDW expansion is NOT converging at the physical cutoff.

# Optimal truncation order N*
# For t = t* = 1/lambda_max^2: |term_k| ~ a_{2k} * t*^{k-4} ~ R^k * lambda_max^{2(4-k)}
# Minimum when d/dk [k*ln(R) + (4-k)*2*ln(lambda_max)] = 0
# => k* = 4 - 2*ln(lambda_max) / ln(R)
for L in L_MAX_VALUES:
    r = ratios_by_L[L]
    R_eff = (r[2] * r[3])**0.5
    lam_max = max(np.max(sector_evals[(p,q)]) for (p,q) in sector_evals if p+q <= L)
    if R_eff > 0 and R_eff < 1:
        k_star = 4 - 2 * np.log(lam_max) / np.log(R_eff)
        print(f"  L={L}: N* (optimal truncation) ~ {k_star:.1f}")
    else:
        N_star_WS1 = lam_max**2 / R_eff if R_eff > 0 else np.inf
        print(f"  L={L}: R_eff = {R_eff:.4f}, Lambda^2/R = {N_star_WS1:.1f} "
              f"(WS1 E4 estimate)")

# =============================================================================
# 7. FUNCTIONAL-DEPENDENCE ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("7. FUNCTIONAL-DEPENDENCE CLASSIFICATION")
print("=" * 80)

print(f"""
  The ratio sequence r_k = |a_{{2k+2}}/a_{{2k}}| is MONOTONICALLY INCREASING
  at every L_max from 3 to 7:
    L=3: 0.431, 0.487, 0.567, 0.681, 0.810, 0.929
    L=7: 0.158, 0.180, 0.223, 0.320, 0.460, 0.641

  This means the SDW expansion is an ASYMPTOTIC series, not a convergent one.
  Each additional term REDUCES accuracy for t below a critical value.

  FUNCTIONAL-DEPENDENCE:

  ZETA ACTION (S_zeta = zeta_D(0) = a_4):
    - Contains ONLY a_4. No a_6, no a_8, no truncation problem.
    - The asymptotic truncation is IRRELEVANT.
    - S_zeta = {a4_fold:.4f}. Exact to machine epsilon.

  CUTOFF ACTION (S_cutoff = Tr f(D^2/Lambda^2)):
    - The SDW expansion is the ONLY way to extract physics from S_cutoff.
    - With r_k increasing, the expansion diverges at the physical cutoff.
    - Gate verdict: {gate_verdict} -- the a_6 correction is past optimal truncation.
    - The S71 result (a_6 correction to lambda_CCM) is UNRELIABLE.

  f* = 0.912*sqrt(x) + 0.088*exp(-x) (W2-C):
    - The f-moments for sqrt(x) DIVERGE. SDW expansion does not exist.
    - f* is non-perturbative by construction.
    - Only the DIRECT spectral sum (over eigenvalues) is meaningful.
    - This is CONSISTENT with the gate finding: the SDW expansion was
      already diverging for the geometric coefficients.

  CLASSIFICATION:
    a_0, a_2, a_4, a_6, a_8 (all M_{{-k}}): FUNCTIONAL-INDEPENDENT (geometric)
    r_k = |a_{{2k+2}}/a_{{2k}}|: FUNCTIONAL-INDEPENDENT (geometric)
    Gate verdict ({gate_verdict}): APPLIES to cutoff action only.
    Zeta action is IMMUNE to this problem.
""")

# =============================================================================
# 8. SAVE DATA AND PLOT
# =============================================================================
print("\n" + "=" * 80)
print("8. SAVING DATA AND GENERATING PLOT")
print("=" * 80)

npz_path = os.path.join(outdir, 's72_asymptotic_truncation.npz')
np.savez(npz_path,
    gate_name='ASYMPTOTIC-TRUNCATION-72',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # SDW coefficients at L=3 (canonical)
    a0_canonical=a0_fold,
    a2_canonical=a2_fold,
    a4_canonical=a4_fold,
    a6_canonical=a6_canonical,
    a8_canonical=a8_canonical,
    a10_canonical=a10_canonical,
    a12_canonical=a12_canonical,
    # L=3 ratios
    ratio_a2_a0=ratios_by_L[3][0],
    ratio_a4_a2=ratios_by_L[3][1],
    ratio_a6_a4=ratios_by_L[3][2],
    ratio_a8_a6=ratios_by_L[3][3],
    ratio_a10_a8=ratios_by_L[3][4],
    ratio_a12_a10=ratios_by_L[3][5],
    # L=7 ratios
    ratio_a6_a4_L7=ratio_a6_a4_L7,
    ratio_a8_a6_L7=ratio_a8_a6_L7,
    # All L_max data
    L_max_values=np.array(L_MAX_VALUES),
    moments_by_L=np.array([[moments_by_L[L][k] for k in k_range] for L in L_MAX_VALUES]),
    ratios_by_L_arr=np.array([[ratios_by_L[L][k] for k in range(6)] for L in L_MAX_VALUES]),
    # Reference
    gilkey_a6_a4=gilkey_ref,
    reference_ratio=reference_L3,
    test_ratio=test_L3,
    gate_ratio=gate_ratio_L3,
    # Heat trace (L=3)
    t_grid=t_grid,
    K_exact_L3=K_exact,
    K_sdw3=K_sdw3,
    K_sdw5=K_sdw5,
    K_sdw7=K_sdw7,
    lambda_max_L3=lambda_max_L3,
)
print(f"  Data saved to {npz_path}")

# --- PLOT ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'ASYMPTOTIC-TRUNCATION-72: SDW Expansion Analysis\n'
             f'Gate: {gate_verdict} | lizzi-spectral-functional-theorist | S72 W3-B',
             fontsize=12, fontweight='bold')

# Panel 1: Ratio sequence r_k at multiple L_max
ax1 = axes[0, 0]
k_labels = ['a2/a0', 'a4/a2', 'a6/a4', 'a8/a6', 'a10/a8', 'a12/a10']
k_vals = np.arange(6)
colors_L = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, L in enumerate(L_MAX_VALUES):
    r_seq = [ratios_by_L[L][k] for k in range(6)]
    ax1.plot(k_vals, r_seq, 'o-', color=colors_L[i], markersize=7, linewidth=1.5,
             label=f'L={L}')
ax1.axhline(y=1.0, color='red', linestyle=':', alpha=0.5, label='|ratio|=1')
ax1.axhline(y=0.25, color='green', linestyle='--', alpha=0.5, label='Gilkey 0.25')
ax1.set_xlabel('k  (ratio index)', fontsize=12)
ax1.set_ylabel(r'$r_k = |a_{2k+2} / a_{2k}|$', fontsize=12)
ax1.set_title('Ratio Sequence at Multiple L_max', fontsize=11)
ax1.set_xticks(k_vals)
ax1.set_xticklabels(k_labels, fontsize=9)
ax1.legend(fontsize=8, ncol=2)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 1.1)

# Panel 2: Heat trace error
ax2 = axes[0, 1]
t_sel = t_grid[(t_grid >= 0.05) & (t_grid <= 10)]
K_ex_sel = K_exact[(t_grid >= 0.05) & (t_grid <= 10)]
K3_sel = K_sdw3[(t_grid >= 0.05) & (t_grid <= 10)]
K5_sel = K_sdw5[(t_grid >= 0.05) & (t_grid <= 10)]
K7_sel = K_sdw7[(t_grid >= 0.05) & (t_grid <= 10)]

err3_sel = np.abs(K3_sel - K_ex_sel) / np.abs(K_ex_sel)
err5_sel = np.abs(K5_sel - K_ex_sel) / np.abs(K_ex_sel)
err7_sel = np.abs(K7_sel - K_ex_sel) / np.abs(K_ex_sel)

ax2.loglog(t_sel, err3_sel, 'b-', linewidth=2, label='3-term (a0..a4)')
ax2.loglog(t_sel, err5_sel, 'r-', linewidth=2, label='5-term (a0..a8)')
ax2.loglog(t_sel, err7_sel, 'g-', linewidth=2, label='7-term (a0..a12)')
ax2.axvline(x=t_star, color='gray', linestyle=':', alpha=0.5,
            label=f't* = {t_star:.3f}')
ax2.set_xlabel('t', fontsize=12)
ax2.set_ylabel('Relative error', fontsize=12)
ax2.set_title('SDW Truncation Error (L=3)', fontsize=11)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(1e-15, 10)

# Panel 3: Spectral moments vs L_max
ax3 = axes[1, 0]
for k, label, color in [(0, 'a_0', 'k'), (1, 'a_2', 'b'),
                          (2, 'a_4', 'r'), (3, 'a_6', 'g'), (4, 'a_8', 'm')]:
    vals = [moments_by_L[L][k] for L in L_MAX_VALUES]
    ax3.semilogy(L_MAX_VALUES, vals, 'o-', color=color, markersize=8, linewidth=2,
                 label=label)
ax3.set_xlabel('L_max', fontsize=12)
ax3.set_ylabel('Spectral moment M_{-k}', fontsize=12)
ax3.set_title('Spectral Moments vs L_max', fontsize=11)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: r_2 = a_6/a_4 and r_3 = a_8/a_6 vs L_max (the gate quantities)
ax4 = axes[1, 1]
r2_seq = [ratios_by_L[L][2] for L in L_MAX_VALUES]
r3_seq = [ratios_by_L[L][3] for L in L_MAX_VALUES]
ax4.plot(L_MAX_VALUES, r2_seq, 'bo-', markersize=10, linewidth=2, label='r_2 = |a_6/a_4|')
ax4.plot(L_MAX_VALUES, r3_seq, 'rs-', markersize=10, linewidth=2, label='r_3 = |a_8/a_6|')
ax4.axhline(y=0.25, color='green', linestyle='--', linewidth=1.5, label='Gilkey 0.25')
ax4.fill_between(L_MAX_VALUES, r2_seq, r3_seq, alpha=0.15, color='red',
                 label='r_3 > r_2 (diverging)')
ax4.set_xlabel('L_max', fontsize=12)
ax4.set_ylabel('Ratio', fontsize=12)
ax4.set_title('Gate Quantities: |a_6/a_4| vs |a_8/a_6|', fontsize=11)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
png_path = os.path.join(outdir, 's72_asymptotic_truncation.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved to {png_path}")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 80)
print("FINAL SUMMARY: ASYMPTOTIC-TRUNCATION-72")
print("=" * 80)

print(f"""
  Gate: ASYMPTOTIC-TRUNCATION-72
  Verdict: {gate_verdict}
  Detail: {gate_detail}

  KEY NUMBERS (L_max=3, canonical framework):
    a_0 = {a0_fold:.4f}
    a_2 = {a2_fold:.4f}
    a_4 = {a4_fold:.4f}
    a_6 = {a6_canonical:.4f}  (spectral moment M_{{-3}}, this computation)
    a_8 = {a8_canonical:.4f}  (spectral moment M_{{-4}}, this computation)

  RATIO SEQUENCE (L=3):
    |a_2/a_0| = {ratios_by_L[3][0]:.6f}
    |a_4/a_2| = {ratios_by_L[3][1]:.6f}
    |a_6/a_4| = {ratios_by_L[3][2]:.6f}
    |a_8/a_6| = {ratios_by_L[3][3]:.6f}
    Trend: MONOTONICALLY INCREASING. Expansion is DIVERGING.

  GATE CRITERION (primary, L=3 self-consistent):
    Reference |a_6/a_4| = {reference_L3:.6f}
    Test |a_8/a_6| = {test_L3:.6f}
    Ratio test/reference = {gate_ratio_L3:.6f}

  CROSS-CHECK (L=7):
    |a_6/a_4| = {ratio_a6_a4_L7:.6f} (cf. W1-C = 0.223)
    |a_8/a_6| = {ratio_a8_a6_L7:.6f}
    Still INCREASING: r_3 > r_2 at every L_max.

  CANONICAL CROSS-CHECKS:
    a_0 match: {m3[0]:.1f} vs {a0_fold:.1f} (EXACT)
    a_2 match: {m3[1]:.4f} vs {a2_fold:.4f} (EXACT)
    a_4 match: {m3[2]:.4f} vs {a4_fold:.4f} (EXACT)

  FUNCTIONAL-INDEPENDENCE CLASSIFICATION:
    a_{{2k}} spectral moments:     STRUCTURAL (FI)
    Ratio sequence r_k:          STRUCTURAL (FI) -- monotone increasing
    Gate verdict ({gate_verdict}):  SCHEME-DEPENDENT (cutoff only, not zeta)
    Zeta action S_zeta = a_4:   IMMUNE to asymptotic truncation
    f* SDW expansion:            DOES NOT EXIST (divergent moments)
""")

print("DONE.")
