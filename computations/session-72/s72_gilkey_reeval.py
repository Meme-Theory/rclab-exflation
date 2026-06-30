#!/usr/bin/env python3
"""
s72_gilkey_reeval.py — GILKEY-REEVAL-72
Re-evaluate the S71 HIGHER-ORDER-CCM-71 gate verdict using the geometric
Gilkey ratio a_6/a_4 = 0.25 instead of the spectral zeta ratio 0.567.

Physics
-------
S71 W1-B found delta(lambda_CCM)/lambda_CCM = 26.9% using the spectral zeta
ratio a_6^z/a_4^z = 0.567 from the L_max=7 truncated spectrum. The
Landau-Baptista workshop (WS3) established that this ratio is contaminated
by finite-spectrum artifacts: the spectral zeta of a truncated spectrum
conflates geometric Seeley-DeWitt coefficients with finite-spectrum
contributions.

The geometric (Gilkey) prediction is a_6/a_4 ~ 0.25 for the SU(3) fiber
(universal Lie group result from dimensional analysis: a_{2k} ~ Vol * R^k
where R is the scalar curvature, giving a_{2k+2}/a_{2k} ~ R/M_KK^2 ~ 0.25
for dim(K)=8).

This script re-computes the delta(lambda_CCM)/lambda_CCM using:
  - Central: a_6/a_4 = 0.25 (geometric Gilkey)
  - Lower:   a_6/a_4 = 0.15 (heat kernel decay on compact Lie groups)
  - Upper:   a_6/a_4 = 0.35 (allowing Jensen deformation effects)
  - S71 original: a_6/a_4 = 0.567 (spectral zeta, for comparison)

Gate: GILKEY-REEVAL-72
  PASS:  Revised delta > 25% (original verdict stands)
  INFO:  Revised delta in [5%, 25%] (downgraded from PASS to INFO)
  FAIL:  Revised delta < 5% (a_6 correction negligible with geometric ratio)

Author: lizzi-spectral-functional-theorist
Session: S72 W1-B
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Vol_SU3_Haar,
)

t0 = time.time()

print("=" * 80)
print("GILKEY-REEVAL-72: Re-evaluation with Geometric Gilkey Ratio a_6/a_4=0.25")
print("Spectral Functional Pluralism Analysis")
print("=" * 80)

# =============================================================================
# 1. LOAD UPSTREAM DATA
# =============================================================================
print("\n" + "=" * 80)
print("1. UPSTREAM DATA FROM S71 AND S70")
print("=" * 80)

# Load S71 higher-order CCM data
d_s71 = np.load(os.path.join(SCRIPT_DIR, 's71_higher_order_ccm.npz'),
                allow_pickle=True)

# Extract S71 values
gate_s71 = str(d_s71['gate_verdict'])
delta_s71_A = float(d_s71['delta_ratio_A'])       # 0.2071 (estimate A: prompt spec)
delta_s71_B = float(d_s71['delta_ratio_B'])        # 0.2690 (estimate B: spectral zeta)
delta_s71_gate = float(d_s71['delta_gate'])         # 0.2690 (max of A, B)
a6_est_A_s71 = float(d_s71['a6_estimate_A'])        # 0.1248 (Gilkey-conv)
a6_est_B_s71 = float(d_s71['a6_estimate_B'])        # 0.1709 (Gilkey-conv)
ratio_gilkey = float(d_s71['ratio_gilkey'])          # 0.41396 = a_4^G/a_2^G
ratio_zeta_s71 = float(d_s71['ratio_zeta_a6a4'])    # 0.5668 = a_6^zeta/a_4^zeta
a2_G = float(d_s71['a2_gilkey_fold'])                # 0.7282
a4_G = float(d_s71['a4_gilkey_fold'])                # 0.3015
a6_zeta_fold = float(d_s71['a6_zeta_fold'])          # 765.59
protection_s71 = float(d_s71['protection_factor'])   # 0.5860

# Load S70 ratio_gilkey document for curvature invariants
d_rg = np.load(os.path.join(SCRIPT_DIR, 's70_ratio_gilkey_document.npz'),
               allow_pickle=True)
R_fold = float(d_rg['R_fold'])
Ric2_fold = float(d_rg['Ric2_fold'])
K_fold = float(d_rg['K_fold'])

# Load S71 spectral zeta threshold for cross-check
d_szt = np.load(os.path.join(SCRIPT_DIR, 's71_spectral_zeta_threshold.npz'),
                allow_pickle=True)
ratio_a4_a2_canonical = float(d_szt['ratio_a4_a2_canonical'])
a4_canonical = float(d_szt['a4_canonical'])
a2_canonical = float(d_szt['a2_canonical'])

print(f"  S71 HIGHER-ORDER-CCM-71 results:")
print(f"    Gate verdict: {gate_s71}")
print(f"    delta(lambda_CCM)/lambda_CCM (estimate A, prompt): {delta_s71_A:.6f} ({delta_s71_A*100:.3f}%)")
print(f"    delta(lambda_CCM)/lambda_CCM (estimate B, zeta):   {delta_s71_B:.6f} ({delta_s71_B*100:.3f}%)")
print(f"    Gate metric (max of A,B): {delta_s71_gate:.6f} ({delta_s71_gate*100:.3f}%)")
print(f"    a_6/a_4 ratio used (spectral zeta): {ratio_zeta_s71:.6f}")
print()
print(f"  Gilkey heat kernel coefficients at fold:")
print(f"    a_2^G = {a2_G:.10f}")
print(f"    a_4^G = {a4_G:.10f}")
print(f"    ratio_gilkey (a_4^G/a_2^G) = {ratio_gilkey:.10f}")
print(f"    protection factor (a_2-a_4)/a_2 = {protection_s71:.6f}")
print()
print(f"  Curvature invariants at fold (tau = {tau_fold}):")
print(f"    R = {R_fold:.12f}")
print(f"    |Ric|^2 = {Ric2_fold:.12f}")
print(f"    K = {K_fold:.12f}")

# =============================================================================
# 2. CROSS-CHECK: a_4/a_2 RATIO CONSISTENCY
# =============================================================================
print("\n" + "=" * 80)
print("2. CROSS-CHECK: a_4/a_2 RATIO CONSISTENCY")
print("=" * 80)

# From canonical_constants.py: a4_fold/a2_fold
ratio_canonical = a4_fold / a2_fold
print(f"  From canonical_constants.py:")
print(f"    a4_fold = {a4_fold:.10f}")
print(f"    a2_fold = {a2_fold:.10f}")
print(f"    a4_fold / a2_fold = {ratio_canonical:.10f}")
print()
print(f"  From s71_spectral_zeta_threshold.npz:")
print(f"    ratio_a4_a2_canonical = {ratio_a4_a2_canonical:.10f}")
print(f"    a4_canonical = {a4_canonical:.10f}")
print(f"    a2_canonical = {a2_canonical:.10f}")
print()

# Cross-check: these should match
cc_delta = abs(ratio_canonical - ratio_a4_a2_canonical) / ratio_canonical
print(f"  Cross-check delta: {cc_delta:.2e}")
if cc_delta < 1e-10:
    print(f"  CROSS-CHECK PASSED: Ratios consistent to machine epsilon")
else:
    print(f"  CROSS-CHECK WARNING: Ratios differ by {cc_delta*100:.6f}%")

# Also verify task specification: a4_fold/a2_fold = 1350.72/2776.17 = 0.4865
ratio_spec = 1350.72 / 2776.17
print(f"\n  Task specification: 1350.72/2776.17 = {ratio_spec:.4f}")
print(f"  Canonical value:  {ratio_canonical:.4f}")
print(f"  Agreement: {abs(ratio_canonical - ratio_spec)/ratio_canonical*100:.4f}%")

# =============================================================================
# 3. DEFINE GILKEY RATIO RANGE
# =============================================================================
print("\n" + "=" * 80)
print("3. GILKEY a_6/a_4 RATIO VALUES")
print("=" * 80)

# The geometric (Gilkey) prediction for a_6/a_4 on compact Lie groups:
# a_{2k} ~ Vol * (4*pi)^{-d/2} * (curvature)^k / combinatorial
# So a_{2k+2}/a_{2k} ~ R / (characteristic scale)^2
# For dim(K)=8, the Gilkey ratio a_6/a_4 ~ 0.25

gilkey_ratios = {
    'lower (HK decay)':   0.15,  # Lower bound: heat kernel decay on compact groups
    'central (Gilkey)':   0.25,  # Central: geometric prediction from dim analysis
    'upper (Jensen)':     0.35,  # Upper: allowing Jensen deformation enhancement
    'S71 original (zeta)': ratio_zeta_s71,  # 0.5668: spectral zeta from truncated spectrum
    'S71 estimate A':     ratio_gilkey,     # 0.41396: prompt spec (a_4/a_2 ratio reused)
}

print(f"  Ratio values tested:")
for name, ratio in gilkey_ratios.items():
    print(f"    {name:30s}: a_6/a_4 = {ratio:.6f}")

print(f"\n  Physical basis for central value a_6/a_4 = 0.25:")
print(f"    On a d-dimensional Riemannian manifold with curvature R,")
print(f"    a_{{2k}} ~ (4*pi)^{{-d/2}} * Vol * R^k / (k! * d-dependent coefficients)")
print(f"    For SU(3) at the fold, R = {R_fold:.4f} in M_KK units.")
print(f"    The expansion parameter is R/d = {R_fold/8:.4f} (d=8).")
print(f"    The verified ratio a_4/a_2 = {ratio_gilkey:.4f} confirms this scaling.")
print(f"    Extrapolating: a_6/a_4 ~ R/d * (coefficient ratio) ~ 0.25.")

# =============================================================================
# 4. CORE COMPUTATION: FRACTIONAL SHIFT delta(ratio)/ratio
# =============================================================================
print("\n" + "=" * 80)
print("4. CORE COMPUTATION: delta(lambda_CCM)/lambda_CCM WITH GILKEY RATIOS")
print("=" * 80)

# The formula from S71 (exact, not first-order):
#
# lambda_CCM = (4/3) * g_3^2 * (a_4^G / a_2^G)      [leading order]
#
# With a_6 correction at xi = f_6/f_4 (spectral function moment ratio):
#   a_6^G = a_4^G * (a_6/a_4 ratio)
#   ratio_eff = (a_4^G + xi * a_6^G) / (a_2^G + xi * a_6^G)
#   delta(lambda_CCM)/lambda_CCM = |ratio_eff - ratio_0| / ratio_0
#
# The g_3^2 factor is ALSO modified by a_6 (through gauge kinetic normalization),
# but at the ratio level the dominant effect is the shift in a_4^G/a_2^G.

def delta_ratio_exact(a4, a2, a6_over_a4, xi):
    """Exact fractional change in a_4/a_2 when both shift by xi * a_6.

    a6_over_a4: the ratio a_6/a_4 (NOT the absolute a_6 value)
    """
    a6 = a4 * a6_over_a4
    ratio_0 = a4 / a2
    ratio_eff = (a4 + xi * a6) / (a2 + xi * a6)
    return (ratio_eff - ratio_0) / ratio_0


def delta_ratio_first_order(a4, a2, a6_over_a4, xi):
    """First-order approximation to the fractional change."""
    a6 = a4 * a6_over_a4
    return xi * a6 * (a2 - a4) / (a4 * a2)


# Canonical xi values (spectral function moment ratios)
xi_values = {
    'exp(-x) [xi=1]':    1.0,
    '(1-x)^2 [xi=2]':    2.0,
    '(1-x)^3 [xi=3]':    3.0,
    'Gaussian [xi=0]':    0.0,
    'zeta [xi=0]':        0.0,
    'alternating [xi=-1]': -1.0,
    'anomaly [xi=-1/3]':  -1.0/3.0,
}

# The PRIMARY computation: xi = 1 (canonical smooth cutoff f(x) = exp(-x))
# This is the reference used in S71 for the gate metric.
xi_primary = 1.0  # (local)

print(f"  PRIMARY: xi = {xi_primary} (canonical smooth cutoff)")
print()

# Compute delta for each a_6/a_4 ratio at xi = 1
print(f"  {'a_6/a_4 ratio':>30s} | {'delta (exact)':>14s} | {'delta (1st order)':>18s} | {'a_6^G value':>12s}")
print(f"  {'-'*30} | {'-'*14} | {'-'*18} | {'-'*12}")

results_xi1 = {}
for name, ratio_a6a4 in gilkey_ratios.items():
    delta_ex = delta_ratio_exact(a4_G, a2_G, ratio_a6a4, xi_primary)
    delta_1st = delta_ratio_first_order(a4_G, a2_G, ratio_a6a4, xi_primary)
    a6_val = a4_G * ratio_a6a4
    results_xi1[name] = {
        'ratio': ratio_a6a4,
        'delta_exact': delta_ex,
        'delta_1st': delta_1st,
        'a6_gilkey': a6_val,
    }
    print(f"  {name:>30s} | {delta_ex:14.6f} | {delta_1st:18.6f} | {a6_val:12.6f}")

# Extract the key results
delta_gilkey_025 = abs(results_xi1['central (Gilkey)']['delta_exact'])
delta_gilkey_015 = abs(results_xi1['lower (HK decay)']['delta_exact'])
delta_gilkey_035 = abs(results_xi1['upper (Jensen)']['delta_exact'])
delta_zeta_s71   = abs(results_xi1['S71 original (zeta)']['delta_exact'])

print(f"\n  KEY RESULTS AT xi = 1:")
print(f"    delta(lambda_CCM)/lambda_CCM:")
print(f"      Lower bound  (a_6/a_4=0.15): {delta_gilkey_015*100:.3f}%")
print(f"      Central      (a_6/a_4=0.25): {delta_gilkey_025*100:.3f}%")
print(f"      Upper bound  (a_6/a_4=0.35): {delta_gilkey_035*100:.3f}%")
print(f"      S71 original (a_6/a_4=0.567): {delta_zeta_s71*100:.3f}%")

# =============================================================================
# 5. FULL xi SCAN FOR THE CENTRAL GILKEY RATIO
# =============================================================================
print("\n" + "=" * 80)
print("5. xi SCAN FOR CENTRAL GILKEY RATIO a_6/a_4 = 0.25")
print("=" * 80)

gilkey_central = 0.25  # (local)

print(f"  {'xi description':>25s} | {'xi':>6s} | {'delta (exact)':>14s} | {'delta (%)':>10s}")
print(f"  {'-'*25} | {'-'*6} | {'-'*14} | {'-'*10}")

results_xi_scan = {}
for name, xi in xi_values.items():
    delta_ex = delta_ratio_exact(a4_G, a2_G, gilkey_central, xi)
    results_xi_scan[name] = {
        'xi': xi,
        'delta': delta_ex,
    }
    print(f"  {name:>25s} | {xi:+6.2f} | {delta_ex:14.6f} | {abs(delta_ex)*100:10.3f}")

# =============================================================================
# 6. COMPARISON: GILKEY vs SPECTRAL ZETA ACROSS ALL xi
# =============================================================================
print("\n" + "=" * 80)
print("6. COMPARISON TABLE: GILKEY (0.25) vs SPECTRAL ZETA (0.567)")
print("=" * 80)

print(f"  {'xi':>6s} | {'delta (Gilkey 0.25)':>20s} | {'delta (Zeta 0.567)':>20s} | {'Reduction factor':>18s}")
print(f"  {'-'*6} | {'-'*20} | {'-'*20} | {'-'*18}")

for name, xi in xi_values.items():
    if xi == 0.0 and 'Gaussian' in name:
        continue  # Skip duplicate zero entry
    d_gilkey = delta_ratio_exact(a4_G, a2_G, gilkey_central, xi)
    d_zeta = delta_ratio_exact(a4_G, a2_G, ratio_zeta_s71, xi)
    if abs(d_zeta) > 1e-15:
        reduction = abs(d_gilkey) / abs(d_zeta)
    else:
        reduction = float('nan')
    print(f"  {xi:+6.2f} | {abs(d_gilkey)*100:18.3f}% | {abs(d_zeta)*100:18.3f}% | {reduction:18.4f}")

# =============================================================================
# 7. PROTECTION MECHANISM WITH GILKEY RATIO
# =============================================================================
print("\n" + "=" * 80)
print("7. PROTECTION MECHANISM ANALYSIS")
print("=" * 80)

# The protection factor is structural: (a_2 - a_4)/a_2
# This is INDEPENDENT of the a_6/a_4 ratio.
pf = (a2_G - a4_G) / a2_G
print(f"  Protection factor (a_2 - a_4)/a_2 = {pf:.6f}")
print(f"  This is FUNCTIONAL-INDEPENDENT (structural geometry of SU(3) fiber).")
print()

# Demonstrate: individual shifts vs ratio shift
for name, ratio_a6a4 in [('Gilkey 0.25', 0.25), ('Zeta 0.567', ratio_zeta_s71)]:
    a6_val = a4_G * ratio_a6a4
    xi = 1.0
    shift_a4 = xi * a6_val / a4_G  # fractional shift in a_4 alone
    shift_a2 = xi * a6_val / a2_G  # fractional shift in a_2 alone
    shift_ratio = delta_ratio_exact(a4_G, a2_G, ratio_a6a4, xi)
    print(f"  {name} at xi=1:")
    print(f"    Individual a_4 shift: {shift_a4*100:.3f}%")
    print(f"    Individual a_2 shift: {shift_a2*100:.3f}%")
    print(f"    Actual ratio shift:   {abs(shift_ratio)*100:.3f}%")
    print(f"    Cancellation ratio:   {abs(shift_ratio)/shift_a4:.4f}")
    print()

# =============================================================================
# 8. ANOMALY-DERIVED ACTION WITH GILKEY RATIO
# =============================================================================
print("\n" + "=" * 80)
print("8. ANOMALY-DERIVED ACTION (xi = -1/3) WITH GILKEY RATIO")
print("=" * 80)

xi_anomaly = -1.0 / 3.0
delta_anomaly_gilkey = delta_ratio_exact(a4_G, a2_G, gilkey_central, xi_anomaly)
delta_anomaly_zeta = delta_ratio_exact(a4_G, a2_G, ratio_zeta_s71, xi_anomaly)

print(f"  xi_anomaly = c_3/c_2 = -1/3 (dimensional regularization of fermionic determinant)")
print(f"  delta (Gilkey 0.25): {delta_anomaly_gilkey*100:.3f}% (sign: {'positive' if delta_anomaly_gilkey > 0 else 'negative'})")
print(f"  delta (Zeta 0.567):  {delta_anomaly_zeta*100:.3f}% (sign: {'positive' if delta_anomaly_zeta > 0 else 'negative'})")
print(f"  S71 anomaly result:  {float(d_s71['delta_anomaly_A'])*100:.3f}% (estimate A)")
print(f"                       {float(d_s71['delta_anomaly_B'])*100:.3f}% (estimate B)")

# =============================================================================
# 9. ZETA SPECTRAL ACTION: delta = 0 BY CONSTRUCTION
# =============================================================================
print("\n" + "=" * 80)
print("9. ZETA SPECTRAL ACTION: UNCHANGED BY GILKEY RE-EVALUATION")
print("=" * 80)

print(f"  In the zeta spectral action S_zeta = zeta_D(0) = a_4:")
print(f"    delta(lambda_CCM)/lambda_CCM = 0 EXACTLY (no a_6 term)")
print(f"    This is INDEPENDENT of whether a_6/a_4 = 0.25 or 0.567.")
print(f"    The zeta result was and remains trivially exact.")

# =============================================================================
# 10. MAXIMAL SCHEME DEPENDENCE TABLE (REVISED)
# =============================================================================
print("\n" + "=" * 80)
print("10. SCHEME-DEPENDENCE TABLE (REVISED WITH GILKEY RATIO)")
print("=" * 80)

print(f"  {'Scheme':>30s} | {'a_6/a_4':>8s} | {'xi':>6s} | {'delta(%)':>10s} | {'S71 delta(%)':>12s}")
print(f"  {'-'*30} | {'-'*8} | {'-'*6} | {'-'*10} | {'-'*12}")

schemes = [
    ('Zeta (S_zeta = a_4)',           0.0,     0.0,   0.0),
    ('Cutoff, exp(-x), Gilkey',       0.25,    1.0,   None),
    ('Cutoff, exp(-x), Zeta ratio',   0.567,   1.0,   None),
    ('Cutoff, (1-x)^3, Gilkey',       0.25,    3.0,   None),
    ('Cutoff, (1-x)^3, Zeta ratio',   0.567,   3.0,   None),
    ('Anomaly, Gilkey',               0.25,   -1./3,  None),
    ('Anomaly, Zeta ratio',           0.567,  -1./3,  None),
]

scheme_results = {}
for name, r_a6a4, xi, forced_delta in schemes:
    if forced_delta is not None:
        d = forced_delta
    else:
        d = abs(delta_ratio_exact(a4_G, a2_G, r_a6a4, xi))

    # S71 comparison
    if xi == 0.0:
        s71_d = 0.0  # (local)
    elif xi == 1.0 and abs(r_a6a4 - ratio_zeta_s71) < 0.01:
        s71_d = delta_s71_B
    elif xi == 1.0 and abs(r_a6a4 - ratio_gilkey) < 0.01:
        s71_d = delta_s71_A
    else:
        s71_d = abs(delta_ratio_exact(a4_G, a2_G, ratio_zeta_s71, xi))

    scheme_results[name] = d
    print(f"  {name:>30s} | {r_a6a4:8.4f} | {xi:+6.2f} | {d*100:10.3f} | {s71_d*100:12.3f}")

# =============================================================================
# 11. FUNCTIONAL-INDEPENDENCE CLASSIFICATION
# =============================================================================
print("\n" + "=" * 80)
print("11. FUNCTIONAL-INDEPENDENCE CLASSIFICATION (REVISED)")
print("=" * 80)

print(f"""
  FUNCTIONAL-INDEPENDENT (structural, survives all spectral functionals):
  1. Protection factor (a_2 - a_4)/a_2 = {pf:.4f} — unchanged by Gilkey ratio
  2. f_0 anti-correlation PERSISTS — 1/g_3^2 ~ a_4_eff/(8*pi^3*f_0) + S_inf
     remains monotonically increasing in f_0 for ANY a_4_eff > 0
  3. In the zeta action, delta = 0 exactly (no a_6, no f_0)
  4. The anti-correlation CANNOT be broken by any finite a_6/a_4 ratio

  SCHEME-DEPENDENT (changes across spectral functionals AND ratios):
  1. Numerical delta ranges from 0% (zeta) to {delta_gilkey_025*100:.1f}% (Gilkey, xi=1)
     to {delta_zeta_s71*100:.1f}% (spectral zeta, xi=1) — S71 reported {delta_s71_gate*100:.1f}%
  2. The Gilkey ratio HALVES the S71 estimate:
     {delta_gilkey_025*100:.1f}% vs {delta_zeta_s71*100:.1f}% at xi=1
  3. Range with Gilkey bounds: [{delta_gilkey_015*100:.1f}%, {delta_gilkey_035*100:.1f}%] at xi=1
""")

# =============================================================================
# 12. GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("12. GATE VERDICT: GILKEY-REEVAL-72")
print("=" * 80)

# The gate metric: delta(lambda_CCM)/lambda_CCM using the geometric Gilkey
# ratio a_6/a_4 = 0.25 at xi = 1 (canonical smooth cutoff).

delta_gate_new = delta_gilkey_025  # Central Gilkey value at xi=1

# Determine verdict
if delta_gate_new > 0.25:
    gate_verdict = "PASS"
    verdict_detail = "Original PASS verdict stands even with geometric Gilkey ratio"
elif delta_gate_new < 0.05:
    gate_verdict = "FAIL"
    verdict_detail = "a_6 correction negligible with geometric ratio"
else:
    gate_verdict = "INFO"
    verdict_detail = "Original PASS downgraded to INFO with geometric Gilkey ratio"

gate_detail = (
    f"Revised delta(lambda_CCM)/lambda_CCM = {delta_gate_new:.6f} ({delta_gate_new*100:.3f}%) "
    f"at a_6/a_4 = 0.25 (geometric Gilkey), xi = 1. "
    f"Range with bounds: [{delta_gilkey_015*100:.3f}%, {delta_gilkey_035*100:.3f}%] "
    f"(a_6/a_4 in [0.15, 0.35]). "
    f"S71 original: {delta_s71_gate*100:.3f}% at a_6/a_4 = {ratio_zeta_s71:.4f}. "
    f"Reduction factor: {delta_gilkey_025/delta_zeta_s71:.4f}. "
    f"Protection factor: {pf:.4f} (FUNCTIONAL-INDEPENDENT). "
    f"Zeta action: delta = 0 exactly (unchanged). "
    f"Anomaly action: delta = {abs(delta_anomaly_gilkey)*100:.3f}% (unchanged sign, reduced magnitude)."
)

print(f"\n  Gate: GILKEY-REEVAL-72")
print(f"  Pre-registered criterion:")
print(f"    PASS:  delta > 25%  (original verdict stands)")
print(f"    INFO:  delta in [5%, 25%]  (downgraded from PASS to INFO)")
print(f"    FAIL:  delta < 5%  (a_6 correction negligible)")
print(f"")
print(f"  Computed:")
print(f"    delta (central, a_6/a_4=0.25): {delta_gate_new*100:.3f}%")
print(f"    delta (lower, a_6/a_4=0.15):   {delta_gilkey_015*100:.3f}%")
print(f"    delta (upper, a_6/a_4=0.35):   {delta_gilkey_035*100:.3f}%")
print(f"    delta (S71 original, 0.567):    {delta_zeta_s71*100:.3f}%")
print(f"")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {verdict_detail}")
print(f"")
print(f"  The S71 PASS at 26.9% becomes INFO at {delta_gate_new*100:.1f}% with the geometric ratio.")
print(f"  The entire Gilkey range [0.15, 0.35] maps to [{delta_gilkey_015*100:.1f}%, {delta_gilkey_035*100:.1f}%],")
print(f"  firmly within the INFO band [5%, 25%].")
print(f"  Only the UPPER bound at xi=3 could potentially reach PASS territory:")
delta_035_xi3 = abs(delta_ratio_exact(a4_G, a2_G, 0.35, 3.0))
print(f"    a_6/a_4=0.35, xi=3: delta = {delta_035_xi3*100:.3f}%")

# =============================================================================
# 13. SAVE DATA
# =============================================================================
print("\n" + "=" * 80)
print("13. SAVING DATA")
print("=" * 80)

elapsed = time.time() - t0

out_path = os.path.join(SCRIPT_DIR, 's72_gilkey_reeval.npz')
np.savez(
    out_path,
    # Gate
    gate_name=np.array('GILKEY-REEVAL-72'),
    gate_verdict=np.array(gate_verdict),
    gate_detail=np.array(gate_detail),
    # Central result
    delta_gilkey_025=np.float64(delta_gilkey_025),
    delta_gilkey_015=np.float64(delta_gilkey_015),
    delta_gilkey_035=np.float64(delta_gilkey_035),
    delta_zeta_s71=np.float64(delta_zeta_s71),
    delta_gate_new=np.float64(delta_gate_new),
    # Gilkey ratios
    gilkey_ratio_central=np.float64(0.25),
    gilkey_ratio_lower=np.float64(0.15),
    gilkey_ratio_upper=np.float64(0.35),
    spectral_zeta_ratio=np.float64(ratio_zeta_s71),
    # Reduction from S71
    reduction_factor=np.float64(delta_gilkey_025 / delta_zeta_s71),
    # Upstream Gilkey coefficients
    a2_gilkey_fold=np.float64(a2_G),
    a4_gilkey_fold=np.float64(a4_G),
    ratio_gilkey_a4_over_a2=np.float64(ratio_gilkey),
    protection_factor=np.float64(pf),
    # Anomaly results with Gilkey
    delta_anomaly_gilkey=np.float64(delta_anomaly_gilkey),
    delta_anomaly_zeta=np.float64(delta_anomaly_zeta),
    # Curvature invariants
    R_fold=np.float64(R_fold),
    Ric2_fold=np.float64(Ric2_fold),
    K_fold=np.float64(K_fold),
    # Cross-check
    ratio_a4_a2_canonical=np.float64(ratio_canonical),
    ratio_a4_a2_check=np.float64(ratio_a4_a2_canonical),
    crosscheck_delta=np.float64(cc_delta),
    # S71 comparison
    delta_s71_gate=np.float64(delta_s71_gate),
    gate_s71=np.array(gate_s71),
    # Canonical constants used
    a0_fold=np.float64(a0_fold),
    a2_fold=np.float64(a2_fold),
    a4_fold=np.float64(a4_fold),
    # Timing
    elapsed_s=np.float64(elapsed),
)

print(f"  Saved: {out_path}")
print(f"  Computation time: {elapsed:.2f}s")
print()
print("=" * 80)
print(f"GILKEY-REEVAL-72 GATE VERDICT: {gate_verdict}")
print(f"delta(lambda_CCM)/lambda_CCM = {delta_gate_new*100:.3f}% (Gilkey a_6/a_4=0.25, xi=1)")
print(f"S71 original: {delta_s71_gate*100:.3f}% (spectral zeta a_6/a_4=0.567)")
print(f"Range: [{delta_gilkey_015*100:.3f}%, {delta_gilkey_035*100:.3f}%]")
print("=" * 80)
print("DONE.")
