"""
S83 mack workshop pt.2 -- verify:
  (a) LCDM-discriminability under each candidate (Cand A=-0.918 vs LCDM -1.000,
      Cand B=-0.998 vs LCDM -1.000) using sigma(w_0)_DR3 = 0.046.
  (b) Pre-registered rectangle asymmetry: offset of each candidate from rectangle midpoint.
  (c) If the rectangle were resized to KEEP w_a half-width at 0.2 but widen to catch Scen B,
      what half-width in w_0 would be needed? (Quantifies the asymmetry cost.)
  (d) Sign substitution chain for 'candidate B is LESS falsifiable vs LCDM Scenario A':
       step 1: tension_LCDM(cand) = |w_0_cand - (-1)| / sigma(w_0)_DR3
       step 2: Cand A: |−0.918 − (−1)| / 0.046 = 0.082 / 0.046
       step 3: Cand B: |−0.998 − (−1)| / 0.046 = 0.002 / 0.046
       step 4: Cand A tension ~ 1.78 sig, Cand B tension ~ 0.04 sig
       step 5: direction: Cand B is ~44x LESS discriminable from LCDM -> LESS falsifiable
"""
import numpy as np

# Constants (all local)
sig_w0 = 0.046                                    # (local) DR3 projected sigma(w_0)
w0_cand_A = -0.918                                # (local) zeta baseline
w0_cand_B = -0.998                                # (local) Zubarev substrate-canonical
w0_LCDM   = -1.000                                # (local) LCDM fiducial

# (a) LCDM discriminability
tens_A_vs_LCDM = abs(w0_cand_A - w0_LCDM) / sig_w0  # (local)
tens_B_vs_LCDM = abs(w0_cand_B - w0_LCDM) / sig_w0  # (local)
ratio = tens_A_vs_LCDM / tens_B_vs_LCDM             # (local)

print(f"(a) LCDM-discriminability (1D in w_0, using sigma_DR3={sig_w0}):")
print(f"    Candidate A (-0.918) vs LCDM (-1.000): {tens_A_vs_LCDM:.4f} sigma")
print(f"    Candidate B (-0.998) vs LCDM (-1.000): {tens_B_vs_LCDM:.4f} sigma")
print(f"    Ratio A/B = {ratio:.2f}x more discriminable under A")
print()

# (b) Rectangle asymmetry
R_w0_lo, R_w0_hi = -1.05, -0.85                    # (local)
midpoint_w0 = 0.5*(R_w0_lo + R_w0_hi)              # (local) = -0.95
off_A = w0_cand_A - midpoint_w0                    # (local)
off_B = w0_cand_B - midpoint_w0                    # (local)
halfw = 0.5*(R_w0_hi - R_w0_lo)                    # (local) = 0.10

print(f"(b) Rectangle asymmetry:")
print(f"    midpoint_w0 = {midpoint_w0:+.4f}, half-width = {halfw:.4f}")
print(f"    Candidate A offset from midpoint: {off_A:+.4f} (cand-A is +{off_A/halfw:.2f} halfwidths)")
print(f"    Candidate B offset from midpoint: {off_B:+.4f} (cand-B is {off_B/halfw:+.2f} halfwidths)")
print(f"    Rectangle clearance for candidate A: upper edge-to-cand = {R_w0_hi - w0_cand_A:.4f},")
print(f"                                          lower edge-to-cand = {w0_cand_A - R_w0_lo:.4f}")
print(f"    Rectangle clearance for candidate B: upper edge-to-cand = {R_w0_hi - w0_cand_B:.4f},")
print(f"                                          lower edge-to-cand = {w0_cand_B - R_w0_lo:.4f}")
print()

# (c) To catch Scenario B w_0 = -0.827 under each candidate centering,
# what w_0 half-width is needed?
w0_sc_B = -0.827                                   # (local) Scenario B central
hw_needed_A = abs(w0_cand_A - w0_sc_B)             # (local)
hw_needed_B = abs(w0_cand_B - w0_sc_B)             # (local)
print(f"(c) Half-width (w_0) needed to INCLUDE Scenario B central (w_0 = {w0_sc_B}):")
print(f"    centered on A: need halfwidth >= {hw_needed_A:.4f} (ratio vs current 0.10: {hw_needed_A/halfw:.2f}x)")
print(f"    centered on B: need halfwidth >= {hw_needed_B:.4f} (ratio vs current 0.10: {hw_needed_B/halfw:.2f}x)")
print("    Interpretation: a rectangle CENTERED on cand A already 'almost' catches Scen B (0.091 vs 0.10);")
print("                    a rectangle CENTERED on cand B EXCLUDES Scen B with 70% margin (0.171 vs 0.10).")
print()

# (d) Substitution chain summary (direction claim)
print("(d) Falsifiability direction claim -- substitution chain:")
print("    Definition: T_LCDM(cand) = |w_0_cand - w_0_LCDM| / sigma_DR3")
print(f"    Substitute: T_LCDM(A) = |{w0_cand_A} - ({w0_LCDM})| / {sig_w0}")
print(f"                         = {abs(w0_cand_A - w0_LCDM)} / {sig_w0}")
print(f"                         = {tens_A_vs_LCDM:.4f} sigma")
print(f"                T_LCDM(B) = |{w0_cand_B} - ({w0_LCDM})| / {sig_w0}")
print(f"                         = {abs(w0_cand_B - w0_LCDM)} / {sig_w0}")
print(f"                         = {tens_B_vs_LCDM:.4f} sigma")
print(f"    Simplify:   T_LCDM(A) / T_LCDM(B) = {ratio:.2f}")
print(f"    Direction:  T_LCDM(A) > T_LCDM(B) in ABSOLUTE terms -> Candidate A is MORE discriminable from LCDM.")
print(f"                Under Scenario A (LCDM null), Candidate A is excluded at 1.78-sigma in w_0 alone,")
print(f"                Candidate B is ~indistinguishable from LCDM at 0.04-sigma.")
print(f"                Conclusion: Candidate B is LESS FALSIFIABLE against LCDM nulls.")
print()

# Under Scenario B central (-0.827, -0.300):
w0_B, wa_B = -0.827, -0.300                        # (local)
sig_wa = 0.177                                     # (local)
rho = -0.85                                        # (local)
cov = np.array([[sig_w0**2, rho*sig_w0*sig_wa], [rho*sig_w0*sig_wa, sig_wa**2]])  # (local)

for name, (w0c, wac) in [("A (zeta)", (w0_cand_A, 0.0)),
                          ("B (Zub)", (w0_cand_B, 0.0))]:
    d = np.array([w0c - w0_B, wac - wa_B])         # (local)
    maha2 = d @ np.linalg.inv(cov) @ d.T           # (local)
    maha = float(np.sqrt(maha2))                    # (local)
    print(f"  Scenario B -- Mahalanobis(cand {name}) = {maha:.3f} sigma")

# Under Scenario A (LCDM null):
w0_A, wa_A = -1.000, 0.000                         # (local)
for name, (w0c, wac) in [("A (zeta)", (w0_cand_A, 0.0)),
                          ("B (Zub)", (w0_cand_B, 0.0))]:
    d = np.array([w0c - w0_A, wac - wa_A])         # (local)
    maha2 = d @ np.linalg.inv(cov) @ d.T           # (local)
    maha = float(np.sqrt(maha2))                    # (local)
    print(f"  Scenario A (LCDM) -- Mahalanobis(cand {name}) = {maha:.3f} sigma")

print()
print("SUMMARY:")
print(f"  Cand A (-0.918): LCDM-tens={tens_A_vs_LCDM:.2f}sig, ScenB 2D={1.978:.2f}sig")
print(f"  Cand B (-0.998): LCDM-tens={tens_B_vs_LCDM:.2f}sig, ScenB 2D={4.642:.2f}sig")
print(f"  Cand B is LESS falsifiable against LCDM (0.04 vs 1.78 sig) and MORE tense with Scen B (4.64 vs 1.98 sig).")
