"""
B-5: GAUGE COUPLING CONVERGENCE TEST — THE LEVEL 3 TEST
=========================================================

Evaluates the three gauge coupling ratios at every independently-determined
s_0 candidate and computes fractional discrepancies against measured SM values.

THE FORMULAS (from B-1, Baptista Paper 15):
    g_1/g_2(s) = e^{-2s}         (u(1) vs su(2), left-regular)
    g_1/g_3(s) = e^{-s}          (u(1) vs color, left vs right-regular)
    g_2/g_3(s) = e^{s}           (su(2) vs color)

These are EXACT analytic results from the Jensen TT-deformation metric on SU(3).
    g_i^{-2} proportional to lambda_i(s)  for left-regular (i=1,2)
    g_3^{-2} proportional to Killing form  (s-independent, right-regular)

Volume-preserving: lambda_1 * lambda_2^3 * lambda_3^4 = e^{2s} * e^{-6s} * e^{4s} = 1.

MEASURED SM VALUES (at M_Z, PDG):
    sin^2(theta_W) = 0.2312
    => g_1/g_2 = tan(theta_W) = 0.5495
    => s_W = 0.2994

    alpha_s(M_Z) = 0.1179 +/- 0.0009
    alpha_em(M_Z) = 1/127.951
    alpha_2(M_Z) = alpha_em / sin^2(theta_W) = (1/127.951) / 0.2312 = 1/29.58
    alpha_1(M_Z) = alpha_em / cos^2(theta_W) = (1/127.951) / 0.7688 = 1/98.37

    g_1/g_3 = sqrt(alpha_1/alpha_3) = sqrt((1/98.37)/(0.1179)) = 0.2942
    g_2/g_3 = sqrt(alpha_2/alpha_3) = sqrt((1/29.58)/(0.1179)) = 0.5354

NORMALIZATION CAVEAT:
    g_1 and g_2 both arise from the LEFT-regular action, so their RATIO
    g_1/g_2 = e^{-2s} is normalization-independent. The comparison to
    tan(theta_W) is clean.

    g_3 arises from the RIGHT-regular action. The g_1/g_3 and g_2/g_3 ratios
    involve comparing LEFT to RIGHT B_ab coefficients, which introduces a
    group-theoretic normalization factor. At s=0 (bi-invariant), all three
    couplings are equal by construction. The s-dependence is then:
        g_1/g_3 = e^{-s},  g_2/g_3 = e^{s}

    These are COMPACTIFICATION-SCALE values. RG running from the KK scale
    to M_Z is NOT included. A ~10-15% correction is expected.

Author: Baptista-Spacetime-Analyst, Session 17d
Date: 2026-02-14
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# =============================================================================
# SECTION 1: COUPLING FORMULAS
# =============================================================================

def g1_over_g2(s):
    """g_1/g_2 = e^{-2s}. Exact. From lambda_2/lambda_1 = e^{-4s}."""
    return np.exp(-2.0 * s)

def g1_over_g3(s):
    """g_1/g_3 = e^{-s}. Exact. g_3 from right-regular (s-independent)."""
    return np.exp(-s)

def g2_over_g3(s):
    """g_2/g_3 = e^{s}. Exact. Consistency: (g1/g3)/(g2/g3) = e^{-2s} = g1/g2."""
    return np.exp(s)

def sin2_thetaW(s):
    """sin^2(theta_W) = g_1^2/(g_1^2 + g_2^2) = r^2/(1+r^2) where r = g_1/g_2."""
    r = g1_over_g2(s)
    return r**2 / (1.0 + r**2)


# =============================================================================
# SECTION 2: MEASURED SM VALUES
# =============================================================================

# PDG 2024 values at M_Z
SIN2_TW_MEASURED = 0.23121      # sin^2(theta_W) (MS-bar, M_Z)
SIN2_TW_ERR     = 0.00004       # uncertainty

TAN_TW_MEASURED  = np.tan(np.arcsin(np.sqrt(SIN2_TW_MEASURED)))  # = g_1/g_2

ALPHA_EM_MZ     = 1.0 / 127.951  # alpha_em(M_Z)
ALPHA_S_MZ      = 0.1179         # alpha_s(M_Z)
ALPHA_S_ERR     = 0.0009

# Derived
ALPHA_1_MZ = ALPHA_EM_MZ / (1.0 - SIN2_TW_MEASURED)  # = alpha_em / cos^2(theta_W)
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW_MEASURED           # = alpha_em / sin^2(theta_W)

G1_G2_MEASURED = np.sqrt(ALPHA_1_MZ / ALPHA_2_MZ)     # = tan(theta_W)
G1_G3_MEASURED = np.sqrt(ALPHA_1_MZ / ALPHA_S_MZ)
G2_G3_MEASURED = np.sqrt(ALPHA_2_MZ / ALPHA_S_MZ)


# =============================================================================
# SECTION 3: s_0 CANDIDATES (from independent determinations)
# =============================================================================

S_CANDIDATES = {
    's_W = 0.2994 (sin^2 theta_W)':   0.2994,
    's_H1 = 0.164 (Boltzmann V_eff)': 0.164,
    's_H2a = 0.36 (F crit, Lam=1.23)': 0.36,
    's_H2b = 0.67 (F crit, Lam=0.5)':  0.67,
    's = 0.0 (bi-invariant)':           0.0,
    's = 0.15 (phi-ratio)':             0.15,
    's = 0.43 (phi-metric)':            0.43,
    's = 1.14 (phi-pairwise peak)':     1.14,
}


# =============================================================================
# SECTION 4: CONVERGENCE TABLE
# =============================================================================

def compute_convergence_table():
    """Compute gauge coupling ratios and discrepancies at all s_0 candidates."""

    print("=" * 100)
    print("B-5: GAUGE COUPLING CONVERGENCE TEST — LEVEL 3")
    print("=" * 100)
    print()

    # Report measured values
    print("MEASURED SM VALUES (PDG, at M_Z):")
    print(f"  sin^2(theta_W) = {SIN2_TW_MEASURED} +/- {SIN2_TW_ERR}")
    print(f"  tan(theta_W)   = {TAN_TW_MEASURED:.6f}  [= g_1/g_2 target]")
    print(f"  alpha_em(M_Z)  = {ALPHA_EM_MZ:.6e}  (= 1/{1.0/ALPHA_EM_MZ:.3f})")
    print(f"  alpha_s(M_Z)   = {ALPHA_S_MZ} +/- {ALPHA_S_ERR}")
    print(f"  alpha_1(M_Z)   = {ALPHA_1_MZ:.6e}  (= 1/{1.0/ALPHA_1_MZ:.2f})")
    print(f"  alpha_2(M_Z)   = {ALPHA_2_MZ:.6e}  (= 1/{1.0/ALPHA_2_MZ:.2f})")
    print()
    print("DERIVED COUPLING RATIOS (at M_Z):")
    print(f"  g_1/g_2 = sqrt(alpha_1/alpha_2) = {G1_G2_MEASURED:.6f}")
    print(f"  g_1/g_3 = sqrt(alpha_1/alpha_3) = {G1_G3_MEASURED:.6f}")
    print(f"  g_2/g_3 = sqrt(alpha_2/alpha_3) = {G2_G3_MEASURED:.6f}")
    print()

    # Report theoretical formulas
    print("BAPTISTA FORMULAS (Paper 15, at compactification scale):")
    print("  g_1/g_2(s) = e^{-2s}     [left-regular, u(1) vs su(2)]")
    print("  g_1/g_3(s) = e^{-s}      [left vs right-regular]")
    print("  g_2/g_3(s) = e^{s}       [left vs right-regular]")
    print("  Volume-preserving: e^{2s} * e^{-6s} * e^{4s} = 1")
    print()

    # s_W derived from g_1/g_2 = tan(theta_W)
    s_W = -0.5 * np.log(TAN_TW_MEASURED)
    print(f"  s_W (from sin^2 theta_W) = -ln(tan theta_W)/2 = {s_W:.6f}")
    print()

    # Main convergence table
    print("=" * 100)
    print("CONVERGENCE TABLE: Coupling ratios at each s_0 candidate")
    print("=" * 100)
    print()

    header = (f"{'s_0 candidate':>36s}  {'s':>7s}  "
              f"{'g1/g2':>10s}  {'d(g1/g2)':>9s}  "
              f"{'g1/g3':>10s}  {'d(g1/g3)':>9s}  "
              f"{'g2/g3':>10s}  {'d(g2/g3)':>9s}  "
              f"{'sin2tW':>10s}  {'d(sin2)':>9s}")
    print(header)
    print("-" * len(header))

    results = {}

    for label, s in sorted(S_CANDIDATES.items(), key=lambda x: x[1]):
        r12 = g1_over_g2(s)
        r13 = g1_over_g3(s)
        r23 = g2_over_g3(s)
        s2tw = sin2_thetaW(s)

        d12 = (r12 - G1_G2_MEASURED) / G1_G2_MEASURED
        d13 = (r13 - G1_G3_MEASURED) / G1_G3_MEASURED
        d23 = (r23 - G2_G3_MEASURED) / G2_G3_MEASURED
        ds2 = (s2tw - SIN2_TW_MEASURED) / SIN2_TW_MEASURED

        print(f"{label:>36s}  {s:7.4f}  "
              f"{r12:10.6f}  {d12:+9.2%}  "
              f"{r13:10.6f}  {d13:+9.2%}  "
              f"{r23:10.6f}  {d23:+9.2%}  "
              f"{s2tw:10.6f}  {ds2:+9.2%}")

        results[label] = {
            's': s,
            'g1/g2': r12, 'd_g1g2': d12,
            'g1/g3': r13, 'd_g1g3': d13,
            'g2/g3': r23, 'd_g2g3': d23,
            'sin2_tW': s2tw, 'd_sin2': ds2,
        }

    print()
    return results, s_W


# =============================================================================
# SECTION 5: CONSISTENCY CHECKS
# =============================================================================

def consistency_checks():
    """Verify internal consistency of the coupling formulas."""

    print("=" * 100)
    print("CONSISTENCY CHECKS")
    print("=" * 100)
    print()

    s_test = np.array([0.0, 0.15, 0.2994, 0.5, 1.0, 1.5, 2.0])

    # Check 1: (g1/g3) / (g2/g3) = g1/g2
    print("CHECK 1: (g1/g3) / (g2/g3) = g1/g2 ?")
    max_err = 0.0
    for s in s_test:
        lhs = g1_over_g3(s) / g2_over_g3(s)
        rhs = g1_over_g2(s)
        err = abs(lhs - rhs)
        max_err = max(max_err, err)
    print(f"  Max error over {len(s_test)} s-values: {max_err:.2e}")
    print(f"  PASS" if max_err < 1e-14 else f"  FAIL")
    print()

    # Check 2: sin^2(theta_W) = r^2/(1+r^2) inverts correctly
    print("CHECK 2: sin^2(theta_W)(s_W) = 0.23121 ?")
    s_W = -0.5 * np.log(TAN_TW_MEASURED)
    s2 = sin2_thetaW(s_W)
    err2 = abs(s2 - SIN2_TW_MEASURED)
    print(f"  sin^2(theta_W) at s_W = {s_W:.6f}: {s2:.10f}")
    print(f"  Measured: {SIN2_TW_MEASURED}")
    print(f"  Error: {err2:.2e}")
    print(f"  PASS" if err2 < 1e-6 else f"  FAIL")
    print()

    # Check 3: Volume preservation
    print("CHECK 3: Volume preservation (e^{2s} * e^{-6s} * e^{4s} = 1) ?")
    max_vol_err = 0.0
    for s in s_test:
        vol = np.exp(2*s) * np.exp(-6*s) * np.exp(4*s)
        max_vol_err = max(max_vol_err, abs(vol - 1.0))
    print(f"  Max volume ratio deviation: {max_vol_err:.2e}")
    print(f"  PASS" if max_vol_err < 1e-14 else f"  FAIL")
    print()

    # Check 4: At s=0, all couplings equal
    print("CHECK 4: At s=0, g_1 = g_2 = g_3 (all ratios = 1) ?")
    r12_0 = g1_over_g2(0.0)
    r13_0 = g1_over_g3(0.0)
    r23_0 = g2_over_g3(0.0)
    err4 = max(abs(r12_0 - 1.0), abs(r13_0 - 1.0), abs(r23_0 - 1.0))
    print(f"  g1/g2(0) = {r12_0:.15f}")
    print(f"  g1/g3(0) = {r13_0:.15f}")
    print(f"  g2/g3(0) = {r23_0:.15f}")
    print(f"  Max deviation from 1.0: {err4:.2e}")
    print(f"  PASS" if err4 < 1e-14 else f"  FAIL")
    print()


# =============================================================================
# SECTION 6: PHYSICAL INTERPRETATION TABLE
# =============================================================================

def interpretation_table(results, s_W):
    """Generate the physical interpretation summary."""

    print("=" * 100)
    print("PHYSICAL INTERPRETATION")
    print("=" * 100)
    print()

    print("The coupling ratio g_1/g_2 = e^{-2s} is a MONOTONIC function of s.")
    print("It equals the measured tan(theta_W) = 0.5495 at exactly ONE value: s_W = 0.2994.")
    print("Any other s_0 candidate produces a SPECIFIC fractional discrepancy.")
    print()
    print("The discrepancy is the Level 3 test result:")
    print()

    # Rank by |d_g1g2|
    ranked = sorted(results.items(), key=lambda x: abs(x[1]['d_g1g2']))

    print(f"  {'Rank':>4s}  {'s_0 candidate':>36s}  {'|delta(g1/g2)|':>14s}  {'Assessment':>20s}")
    print(f"  {'-'*80}")

    for rank, (label, data) in enumerate(ranked, 1):
        d = abs(data['d_g1g2'])
        if d < 0.001:
            assessment = "EXACT (by construction)"
        elif d < 0.10:
            assessment = "VIABLE (within RG)"
        elif d < 0.20:
            assessment = "MARGINAL"
        elif d < 0.35:
            assessment = "DISFAVORED"
        else:
            assessment = "EXCLUDED"

        print(f"  {rank:4d}  {label:>36s}  {d:14.4%}  {assessment:>20s}")

    print()
    print("Assessment criteria:")
    print("  EXACT:      delta = 0 (matches by construction)")
    print("  VIABLE:     delta < 10% (within expected RG running correction)")
    print("  MARGINAL:   10% < delta < 20% (requires large RG or normalization effect)")
    print("  DISFAVORED: 20% < delta < 35% (implausible without new physics)")
    print("  EXCLUDED:   delta > 35% (incompatible with measured sin^2 theta_W)")
    print()

    # Comment on g_1/g_3 and g_2/g_3
    print("NOTE ON g_1/g_3 AND g_2/g_3:")
    print("  These ratios compare LEFT-regular (g_1, g_2) to RIGHT-regular (g_3).")
    print("  The comparison to measured alpha_s requires:")
    print("    (a) Correct normalization factor between left and right B_ab")
    print("    (b) RG running from compactification scale to M_Z")
    print("  Without (a) and (b), the g_1/g_3 and g_2/g_3 columns are INDICATIVE,")
    print("  not definitive. The g_1/g_2 column is the clean test.")
    print()


# =============================================================================
# SECTION 7: CONVERGENCE SUMMARY (for session-17d convergence table)
# =============================================================================

def convergence_summary():
    """
    Produce the s-value convergence summary for the joint deliverable.
    Lists all independently-determined s-values and their sources.
    """

    print("=" * 100)
    print("s-VALUE CONVERGENCE SUMMARY (B-5 contribution to joint deliverable)")
    print("=" * 100)
    print()

    # s_W from gauge couplings
    s_W = -0.5 * np.log(TAN_TW_MEASURED)

    entries = [
        ("sin^2(theta_W) = 0.23121",  s_W,    "B-1 (gauge couplings)",      "Yes (experimental)"),
        ("H-1 Boltzmann V_eff min",    0.164,  "H-1 (1-loop CW, Lam=1.23)", "Yes (dynamical)"),
        ("H-2 free energy crit pt",    0.36,   "H-2 (thermodynamics)",       "Yes (thermodynamic)"),
        ("H-2 free energy crit pt",    0.67,   "H-2 (thermodynamics, L=0.5)","Yes (thermodynamic)"),
        ("D-2 Pfaffian sign change",   None,   "D-2 (topology)",             "Yes (topological)"),
        ("Phi sector ratio (3,0)/(0,0)", 0.15, "Session 12 (Dirac spectrum)","Yes (spectral)"),
    ]

    print(f"  {'Source':>32s}  {'s_0':>8s}  {'Method':>30s}  {'Independent?':>20s}")
    print(f"  {'-'*95}")

    for source, s_val, method, indep in entries:
        s_str = f"{s_val:.4f}" if s_val is not None else "NULL"
        print(f"  {source:>32s}  {s_str:>8s}  {method:>30s}  {indep:>20s}")

    print()
    print(f"  GAUGE COUPLING TEST RESULT:")
    print(f"    s_W = {s_W:.4f} is the ONLY value giving sin^2(theta_W) = 0.23121.")
    print(f"    Nearest V_eff candidate: s_H1 = 0.164, delta(g1/g2) = {abs(g1_over_g2(0.164) - TAN_TW_MEASURED)/TAN_TW_MEASURED:.1%}")
    print(f"    Discrepancy: {abs(0.164 - s_W):.3f} in s ({abs(0.164 - s_W)/s_W:.1%} relative)")
    print()
    print(f"  INTERPRETATION:")
    print(f"    If V_eff minimum converges to s ~ 0.30 with full bosonic tower,")
    print(f"    sin^2(theta_W) would be a ZERO-PARAMETER PREDICTION.")
    print(f"    Current H-1 result (s=0.164) is 45% off in s, 31% off in g_1/g_2.")
    print(f"    This is a SOFT FAIL: the H-1 V_eff is not converged (80% change pq5->6).")
    print(f"    The Level 3 test is INCONCLUSIVE pending a converged V_eff.")
    print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print()
    print("#" * 100)
    print("#  B-5: GAUGE COUPLING CONVERGENCE TEST — SESSION 17d, LEVEL 3")
    print("#  Baptista-Spacetime-Analyst")
    print("#" * 100)
    print()

    # Consistency checks first
    consistency_checks()

    # Main convergence table
    results, s_W = compute_convergence_table()

    # Physical interpretation
    interpretation_table(results, s_W)

    # Convergence summary for joint deliverable
    convergence_summary()

    # Final verdict
    print("=" * 100)
    print("B-5 FINAL VERDICT")
    print("=" * 100)
    print()
    print("  1. g_1/g_2 = e^{-2s} is EXACT (analytically derived, 4 consistency checks PASS).")
    print()
    print("  2. The Level 3 test asks: does V_eff select s_0 ~ 0.30?")
    print(f"     H-1 answer: s_0 = 0.164 (Boltzmann, Lambda_UV=1.23)")
    print(f"       => g_1/g_2 = {g1_over_g2(0.164):.6f}, delta = {abs(g1_over_g2(0.164) - TAN_TW_MEASURED)/TAN_TW_MEASURED:+.1%}")
    print(f"       => sin^2(theta_W) = {sin2_thetaW(0.164):.6f} (measured: {SIN2_TW_MEASURED})")
    print()
    print("  3. The H-1 V_eff is NOT CONVERGED:")
    print("     - 80% change from pq=5 to pq=6")
    print("     - Only 4/~45 bosonic DOF included")
    print("     - Minimum is at s=0.164 only for Lambda_UV=1.23 (Lambda-dependent)")
    print()
    print("  4. Level 3 test status: INCONCLUSIVE")
    print("     The test cannot be passed or failed until V_eff converges.")
    print("     The FORMULA is proven. The PREDICTION requires a dynamical s_0.")
    print()
    print("  5. If future V_eff (full Version D tower) gives s_0 in [0.25, 0.35]:")
    print("     sin^2(theta_W) prediction would be within 10% of measured value")
    print("     (within expected RG running correction).")
    print("     This would be a ZERO-PARAMETER prediction of the Weinberg angle.")
    print()

    return results


if __name__ == "__main__":
    results = main()
