"""
S83 mack (workshop) verification calculations for w_0 regulator adjudication.

This script numerically verifies three things referenced in the Round 1 Mack sections:

(1) Rectangle-containment probabilities for the two candidate framework predictions
    w_0_pred_A = -0.918 (zeta baseline, S58 canonical, W3-G42 pre-registered)
    w_0_pred_B = -0.998 (Zubarev-E-weighted, W3-G51 substrate-canonical)
    under each of the three DR3 scenarios (A=LCDM-null, B=Liu+ Scenario-B-like, C=evolving)
    using the projected DR3 covariance sigma(w_0)=0.046, sigma(w_a)=0.177, rho=-0.85.

(2) Half-widths of the pre-registered rectangle R = [-1.05, -0.85] x [-0.2, 0.2]
    in units of projected DR3 1-sigma; distance-from-framework offsets for each prediction.

(3) Falsifiability rank -- i.e., under how many of the 3 DR3 scenarios the rectangle
    would FAIL given the framework point. A prediction that FAILs more often under the
    plausible DR3 scenarios is MORE falsifiable. A prediction that PASSes in all three
    regardless is NOT falsifiable.

All three DR3 scenario centrals are PRE-REGISTERED from S60 / S71:
    Scenario A (null/LCDM):     (-1.000, 0.000)     (LCDM fiducial)
    Scenario B (Liu+ hardening): (-0.827, -0.300)    (per prompt spec)
    Scenario C (evolving):      (-0.752, -0.730)    (DESI DR2 ~ central extrapolated)

Projected covariance (S83 W3-G42):
    sigma(w_0) = 0.046
    sigma(w_a) = 0.177
    rho(w_0, w_a) = -0.85

NO framework constants are hardcoded -- we import from canonical_constants.
All local scan / scenario / threshold values are tagged (local).

No verdict is appended -- this is a workshop verification script.
"""
import sys
import os
import numpy as np
from scipy.stats import multivariate_normal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import w0_FW, wa_FW

# ---- PRE-REGISTERED RECTANGLE (S83 W3-G42) ----
R_w0_lo = -1.05                                 # (local) rectangle lower bound on w_0
R_w0_hi = -0.85                                 # (local) rectangle upper bound on w_0
R_wa_lo = -0.20                                 # (local) rectangle lower bound on w_a
R_wa_hi = +0.20                                 # (local) rectangle upper bound on w_a

# ---- PROJECTED DR3 COVARIANCE (S83 W3-G42, npz; matches S71) ----
sig_w0 = 0.046                                   # (local) projected sigma(w_0), DR3
sig_wa = 0.177                                   # (local) projected sigma(w_a), DR3
rho    = -0.85                                   # (local) DR3 w_0 / w_a correlation

cov = np.array([
    [sig_w0**2,            rho*sig_w0*sig_wa],
    [rho*sig_w0*sig_wa,    sig_wa**2         ],
])                                               # (local) 2x2 Fisher-projected covariance

# ---- TWO FRAMEWORK CANDIDATES ----
# Candidate A: zeta baseline, S58 canonical, currently in W3-G42 pre-registration
w0_cand_A = -0.918                               # (local) = w0_FW (canonical_constants line 807)
wa_cand_A = 0.000                                # (local) = wa_FW (four-fold lock, canonical)

# Candidate B: Zubarev-E-weighted, W3-G51 substrate-canonical prediction
w0_cand_B = -0.998                               # (local) W3-G51 verdict value -0.998116
wa_cand_B = 0.000                                # (local) structural -- same four-fold lock

# Verify Candidate A matches canonical constants
assert abs(w0_cand_A - w0_FW) < 1e-9, f"w0_cand_A mismatch vs canonical: {w0_cand_A} vs {w0_FW}"
assert abs(wa_cand_A - wa_FW) < 1e-9, f"wa_cand_A mismatch vs canonical: {wa_cand_A} vs {wa_FW}"

# ---- THREE DR3 SCENARIOS (pre-registered centrals from S60/S71 + task prompt) ----
scenarios = {
    "A_null_LCDM":           (-1.000, +0.000),   # (local)
    "B_Liu_hardening":       (-0.827, -0.300),   # (local) -- per prompt
    "C_DR2_extrapolate":     (-0.752, -0.730),   # (local) -- DESI DR2 full CPL
}

def in_rectangle(w0, wa):
    """Binary containment rule for R (W3-G42 closure)."""
    return (R_w0_lo <= w0 <= R_w0_hi) and (R_wa_lo <= wa <= R_wa_hi)

# ---- Step 1: distance from each candidate to rectangle midpoint, in units of sigma ----
midpoint_w0 = 0.5 * (R_w0_lo + R_w0_hi)          # (local) = -0.95
midpoint_wa = 0.5 * (R_wa_lo + R_wa_hi)          # (local) = 0.0
halfw_w0    = 0.5 * (R_w0_hi - R_w0_lo)          # (local) = 0.10
halfw_wa    = 0.5 * (R_wa_hi - R_wa_lo)          # (local) = 0.20

print("=" * 74)
print("S83 mack workshop verification -- w_0 regulator adjudication")
print("=" * 74)
print()
print("Rectangle R = [%.2f, %.2f] x [%.2f, %.2f]" % (R_w0_lo, R_w0_hi, R_wa_lo, R_wa_hi))
print("  midpoint  = (%.3f, %.3f), half-widths (%.3f, %.3f)" % (midpoint_w0, midpoint_wa, halfw_w0, halfw_wa))
print("  in units of projected DR3 sigma: halfw_w0/sig_w0 = %.3f, halfw_wa/sig_wa = %.3f" %
      (halfw_w0/sig_w0, halfw_wa/sig_wa))
print()
print("Framework candidate A (zeta canonical / S58):    (%.3f, %.3f)" % (w0_cand_A, wa_cand_A))
print("Framework candidate B (Zubarev / W3-G51):         (%.3f, %.3f)" % (w0_cand_B, wa_cand_B))
print()
print("Candidate A in rectangle? %s (offset from midpoint: +%.3f in w_0)" %
      (in_rectangle(w0_cand_A, wa_cand_A), w0_cand_A - midpoint_w0))
print("Candidate B in rectangle? %s (offset from midpoint: %+.3f in w_0)" %
      (in_rectangle(w0_cand_B, wa_cand_B), w0_cand_B - midpoint_w0))
print()

# ---- Step 2: under each DR3 scenario, compute P(DR3 central lands in R) and
#              Mahalanobis distance of each framework point to the scenario central ----
print("-" * 74)
print("Scenario-by-scenario analysis")
print("-" * 74)
print()

# Rectangle-containment probability under each scenario (integrating the MVN over R)
# Use scipy.stats.multivariate_normal.cdf for rectangle integration (built-in)
for name, (w0_c, wa_c) in scenarios.items():
    # Define a MVN centered at the scenario central with the DR3 covariance
    mvn = multivariate_normal(mean=[w0_c, wa_c], cov=cov)
    # Rectangle probability: P(DR3 realization inside R)
    # Use the 2D CDF construction:
    # P(R) = CDF(hi_w0, hi_wa) - CDF(lo_w0, hi_wa) - CDF(hi_w0, lo_wa) + CDF(lo_w0, lo_wa)
    P_R = (
        mvn.cdf([R_w0_hi, R_wa_hi])
        - mvn.cdf([R_w0_lo, R_wa_hi])
        - mvn.cdf([R_w0_hi, R_wa_lo])
        + mvn.cdf([R_w0_lo, R_wa_lo])
    )                                             # (local)
    # Mahalanobis distance from each candidate to scenario central
    for label, (w0_p, wa_p) in [("A (zeta)", (w0_cand_A, wa_cand_A)),
                                ("B (Zub) ", (w0_cand_B, wa_cand_B))]:
        d = np.array([w0_p - w0_c, wa_p - wa_c])  # (local) delta vector
        maha = float(np.sqrt(d @ np.linalg.inv(cov) @ d.T))  # (local)
        # Also compute 1D tensions for diagnostic
        t_w0 = abs(w0_p - w0_c) / sig_w0          # (local)
        t_wa = abs(wa_p - wa_c) / sig_wa          # (local)
        print(f"  Scenario {name}: central=({w0_c:+.3f}, {wa_c:+.3f}), P(in R)={P_R:.4f}")
        print(f"    vs cand {label}:  Mahalanobis={maha:.3f} sigma, 1D: w_0 {t_w0:.2f}, w_a {t_wa:.2f}")
    print()

# ---- Step 3: summary table of PASS/FAIL for each (candidate, scenario) pair ----
print("-" * 74)
print("Rectangle PASS/FAIL (if DR3 central IS the scenario central) for each candidate")
print("-" * 74)
print()
print(f"{'Scenario':<22} {'Central':<22} {'In-R':<7} {'vs-A offset':<14} {'vs-B offset':<14}")
for name, (w0_c, wa_c) in scenarios.items():
    inR = in_rectangle(w0_c, wa_c)
    off_A_w0 = w0_c - w0_cand_A                   # (local)
    off_B_w0 = w0_c - w0_cand_B                   # (local)
    off_A_wa = wa_c - wa_cand_A                   # (local)
    off_B_wa = wa_c - wa_cand_B                   # (local)
    print(f"{name:<22} ({w0_c:+.3f}, {wa_c:+.3f})    {str(inR):<7} "
          f"({off_A_w0:+.3f},{off_A_wa:+.3f}) ({off_B_w0:+.3f},{off_B_wa:+.3f})")
print()

# ---- Step 4: Falsifiability tally ----
# A prediction is MORE falsifiable if its rectangle can be FALSIFIED by more of the
# observationally plausible DR3 scenarios.
# The rectangle is built AROUND a candidate. If we recenter the rectangle on each candidate
# (preserving half-widths), how many of the 3 scenarios fall outside?
print("-" * 74)
print("Falsifiability tally (rectangle recentered on candidate, fixed half-widths)")
print("-" * 74)
print()
print("A rectangle more often outside = candidate is more falsifiable.\n")

for label, (w0_p, wa_p) in [("A (zeta, -0.918)", (w0_cand_A, wa_cand_A)),
                              ("B (Zubarev, -0.998)", (w0_cand_B, wa_cand_B))]:
    # Recentered rectangle half-widths preserved
    rA_w0 = (w0_p - halfw_w0, w0_p + halfw_w0)    # (local)
    rA_wa = (wa_p - halfw_wa, wa_p + halfw_wa)    # (local)
    print(f"Candidate {label}: recentered R = [{rA_w0[0]:.3f}, {rA_w0[1]:.3f}] x [{rA_wa[0]:.3f}, {rA_wa[1]:.3f}]")
    n_fail = 0                                     # (local)
    for name, (w0_c, wa_c) in scenarios.items():
        inside = (rA_w0[0] <= w0_c <= rA_w0[1]) and (rA_wa[0] <= wa_c <= rA_wa[1])
        verdict = "PASS" if inside else "FAIL"
        if not inside:
            n_fail += 1
        print(f"  Scenario {name} central ({w0_c:+.3f}, {wa_c:+.3f}): {verdict}")
    print(f"  -> FAILs on {n_fail}/3 scenarios")
    print()

# ---- Step 5: Probability DR3 lands in the PRE-REGISTERED rectangle R (fixed) under each scenario ----
# This is what the workshop actually asks about: given R is the LOCKED pre-registration,
# and given each scenario as a possible DR3 realization, what's P(DR3 realization in R)?
# The rectangle is FIXED at [-1.05, -0.85] x [-0.2, 0.2] by W3-G42.
# Candidate A (-0.918, 0) is inside; Candidate B (-0.998, 0) is ALSO inside R (-1.05 < -0.998 < -0.85).
# So the RECTANGLE does not distinguish the two candidates -- both pass rectangle containment.
# The ADJUDICATION is about which candidate's prediction is MORE FALSIFIABLE under the three scenarios.

# Compute: under each scenario central treated as the DR3 realization (assumed), is the
# EXISTING rectangle containing it? (determines PENDING-EVENT -> PASS/FAIL)
print("-" * 74)
print("Existing PRE-REGISTERED rectangle R: PASS/FAIL under each scenario-as-realization")
print("-" * 74)
print("Recall: rectangle R is LOCKED in W3-G42 regardless of which candidate wins.")
print("The question is whether R catches each scenario.")
print()
for name, (w0_c, wa_c) in scenarios.items():
    inR = in_rectangle(w0_c, wa_c)
    print(f"  Scenario {name} central ({w0_c:+.3f}, {wa_c:+.3f}): {'PASS' if inR else 'FAIL'}")
print()

# ---- Step 6: If we MIGRATE the framework prediction to -0.998 (Zubarev), does the
#              rectangle need to be re-registered? Under what rectangle would -0.998 be inside?
#              Also: compute the MINIMUM half-width needed for the rectangle to exclude Scenario B. ----
print("-" * 74)
print("Rectangle re-registration analysis for Candidate B")
print("-" * 74)
print()
print("If framework adopts Candidate B = -0.998 as canonical, current R = [-1.05, -0.85] still")
print("contains it (since -1.05 < -0.998 < -0.85). So rectangle containment is preserved.")
print("But the MIDPOINT offset becomes:")
offset_B_mid = w0_cand_B - midpoint_w0            # (local)
print(f"  midpoint -0.95, candidate B -0.998 -> offset = {offset_B_mid:+.3f} (below midpoint)")
print(f"  candidate A -0.918, offset = {w0_cand_A - midpoint_w0:+.3f} (above midpoint)")
print("  So the current R is slightly MORE asymmetric toward candidate A.")
print()
# What rectangle width would be needed to EXCLUDE a Scenario-B-like central (w_0=-0.827)
# centered on candidate B = -0.998?
# We need |w_0^B_cand - (-0.827)| > halfw_w0 for exclusion.
# |-0.998 - (-0.827)| = 0.171 > 0.10 -> already excluded for Candidate B.
# For Candidate A: |-0.918 - (-0.827)| = 0.091 < 0.10 -> NOT excluded at half-width 0.10.
dB_to_SB = abs(w0_cand_B - scenarios["B_Liu_hardening"][0])   # (local)
dA_to_SB = abs(w0_cand_A - scenarios["B_Liu_hardening"][0])   # (local)
print(f"  |Cand B (-0.998) - Scen B w_0 (-0.827)| = {dB_to_SB:.4f}")
print(f"  |Cand A (-0.918) - Scen B w_0 (-0.827)| = {dA_to_SB:.4f}")
print(f"  At half-width 0.10:")
print(f"    Candidate B would EXCLUDE Scenario B w_0 (0.171 > 0.10): {dB_to_SB > halfw_w0}")
print(f"    Candidate A would NOT exclude Scenario B w_0 (0.091 < 0.10): {dA_to_SB > halfw_w0}")
print()

# ---- Print Python verification tags ----
print("=" * 74)
print("VERIFICATION COMPLETE")
print("=" * 74)
print("Values above are the ground truth for the Mack workshop sections.")
