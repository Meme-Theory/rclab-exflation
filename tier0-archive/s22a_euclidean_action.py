"""
SP-3: EUCLIDEAN ACTION I_E AT THREE MONOPOLES
===============================================

Session 22a -- Schwarzschild-Penrose-Geometer

Computes the Euclidean action I_E(tau) at the three Berry curvature monopoles
M0 (tau=0), M1 (tau~0.15), M2 (tau~1.55).

EQUATIONS:
    I_E(tau) = -(1/(16 pi G)) integral R_K(tau) dvol(tau)

    On volume-preserving Jensen deformation: Vol(K) = constant.
    So: I_E(tau) ~ -R_K(tau) * Vol(K) / (16 pi G)

    The ratio I_E(M1)/I_E(M0) = R_K(M1)/R_K(M0) (tau-independent factors cancel).

    Euclidean path integral weight: exp(-I_E) ~ exp(R_K/(16 pi G)).
    Higher R_K => lower I_E => EXPONENTIALLY PREFERRED.

DATA: R_K(tau) from exact analytical formula (SP-2, Baptista eq 3.70):
    R(s) = [2e^{2s} - 1 + 8e^{-s} - e^{-4s}] / 4

PRE-REGISTERED Constraint GateS (Hawking R2 collab):
    INTERESTING: I_E(M1) < I_E(M0)                       (+2-3 pp)
    COMPELLING:  exp(-delta I_E) > 10 (exponential M1)    (+5-8 pp)
    NEUTRAL:     I_E(M1) > I_E(M0) (M0 preferred)        (0 pp)
    CLOSED:        I_E identical at all three monopoles      (-2 pp)

Author: Schwarzschild-Penrose-Geometer (Session 22a)
Date: 2026-02-20
"""

import numpy as np
import os

data_dir = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# EXACT SCALAR CURVATURE
# ===========================================================================

def R_exact(s):
    """Scalar curvature R(s) -- exact (Baptista eq 3.70)."""
    f = 2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)
    return f / 4.0

def K_exact(s):
    """Kretschner scalar K(s) -- exact (SP-2)."""
    return (
        (23.0/96) * np.exp(-8*s)
        - 1.0 * np.exp(-5*s)
        + (5.0/16) * np.exp(-4*s)
        + (11.0/6) * np.exp(-2*s)
        - (3.0/2) * np.exp(-s)
        + 17.0/32
        + (1.0/12) * np.exp(4*s)
    )

print("=" * 78)
print("  SP-3: EUCLIDEAN ACTION I_E AT THREE MONOPOLES")
print("  Schwarzschild-Penrose-Geometer -- Session 22a")
print("=" * 78)

# ===========================================================================
# 1. SCALAR CURVATURE AT MONOPOLES
# ===========================================================================

print("\n  PART 1: SCALAR CURVATURE R(tau) AT MONOPOLE LOCATIONS")
print()

# Monopole locations
tau_M0 = 0.0
tau_M1 = 0.15   # (0,0)/(1,0) crossing
tau_M2 = 1.55   # (0,0) surrenders gap edge

monopoles = [
    ("M0", tau_M0, "Round metric, (0,0)/(1,1) exact degeneracy"),
    ("M1", tau_M1, "(0,0) takes over gap edge from (1,0)/(0,1)"),
    ("M2", tau_M2, "(0,0) surrenders gap edge back"),
]

for name, tau_val, desc in monopoles:
    R = R_exact(tau_val)
    K = K_exact(tau_val)
    print(f"  {name} (tau={tau_val:.2f}): R = {R:.10f}, K = {K:.10f}")
    print(f"    Description: {desc}")

# ===========================================================================
# 2. EUCLIDEAN ACTION RATIOS
# ===========================================================================

print("\n  PART 2: EUCLIDEAN ACTION I_E(tau)")
print()
print("  I_E(tau) ~ -R(tau) * Vol(K) / (16 pi G)")
print("  Vol(K) = constant (volume-preserving Jensen deformation)")
print("  I_E ratio = R(tau_1)/R(tau_2) (tau-independent factors cancel)")
print()

R_M0 = R_exact(tau_M0)
R_M1 = R_exact(tau_M1)
R_M2 = R_exact(tau_M2)

# I_E ~ -R, so lower I_E means more negative, which means higher R
# Higher R_K => lower I_E => more weight in path integral
# exp(-I_E) ~ exp(R/(16 pi G))

print(f"  R(M0) = {R_M0:.10f}")
print(f"  R(M1) = {R_M1:.10f}")
print(f"  R(M2) = {R_M2:.10f}")
print()
print(f"  R(M1)/R(M0) = {R_M1/R_M0:.10f}")
print(f"  R(M2)/R(M0) = {R_M2/R_M0:.10f}")
print(f"  R(M2)/R(M1) = {R_M2/R_M1:.10f}")
print()

# The Euclidean action difference
# delta I_E = I_E(M0) - I_E(M1) = -[R(M0) - R(M1)] * Vol / (16 pi G)
# If R(M1) > R(M0): delta I_E > 0, meaning I_E(M1) < I_E(M0), M1 preferred

print("  EUCLIDEAN PREFERENCE:")
print(f"  R(M1) > R(M0)? {R_M1 > R_M0} (R(M1) = {R_M1:.6f} vs R(M0) = {R_M0:.6f})")
print(f"  => I_E(M1) {'<' if R_M1 > R_M0 else '>'} I_E(M0)")
print(f"  => M1 is {'PREFERRED' if R_M1 > R_M0 else 'DISFAVORED'} in Euclidean path integral")
print()

print(f"  R(M2) > R(M0)? {R_M2 > R_M0} (R(M2) = {R_M2:.6f} vs R(M0) = {R_M0:.6f})")
print(f"  => I_E(M2) {'<' if R_M2 > R_M0 else '>'} I_E(M0)")
print(f"  => M2 is {'PREFERRED' if R_M2 > R_M0 else 'DISFAVORED'} in Euclidean path integral")
print()

# ===========================================================================
# 3. EXPONENTIAL DOMINANCE
# ===========================================================================

print("  PART 3: EXPONENTIAL DOMINANCE RATIO")
print()
print("  Path integral weight: w(tau) = exp(-I_E(tau)) ~ exp(alpha * R(tau))")
print("  where alpha = Vol(K)/(16 pi G) > 0")
print()
print("  The dominance ratio: w(M1)/w(M0) = exp(alpha * [R(M1) - R(M0)])")
print()

delta_R_M1_M0 = R_M1 - R_M0
delta_R_M2_M0 = R_M2 - R_M0
delta_R_M2_M1 = R_M2 - R_M1

print(f"  R(M1) - R(M0) = {delta_R_M1_M0:.10f}")
print(f"  R(M2) - R(M0) = {delta_R_M2_M0:.10f}")
print(f"  R(M2) - R(M1) = {delta_R_M2_M1:.10f}")
print()

# For the exponential dominance, we need alpha = Vol/(16 pi G)
# This involves the Planck mass scale. However, in KK reduction:
# G_4 ~ G_d / Vol(K), so alpha ~ 1/(16 pi) in natural units
# For a compact space with R ~ O(1), exp(R/(16 pi)) is close to 1

alpha_natural = 1.0 / (16 * np.pi)  # natural units where Vol = 1
print(f"  In natural units (alpha = 1/(16 pi) = {alpha_natural:.6f}):")
print(f"    w(M1)/w(M0) = exp({alpha_natural:.4f} * {delta_R_M1_M0:.6f}) = {np.exp(alpha_natural * delta_R_M1_M0):.6f}")
print(f"    w(M2)/w(M0) = exp({alpha_natural:.4f} * {delta_R_M2_M0:.6f}) = {np.exp(alpha_natural * delta_R_M2_M0):.6f}")
print()
print("  NOTE: The actual alpha depends on the KK mass scale M_KK.")
print("  For M_KK >> M_Planck: alpha >> 1 and exponential dominance is strong.")
print("  For M_KK ~ M_Planck: alpha ~ 1/(16 pi) and the effect is weak.")
print()

# Compute the alpha needed for dominance ratio > 10
if delta_R_M1_M0 > 0:
    alpha_dom_10 = np.log(10) / delta_R_M1_M0
    print(f"  For w(M1)/w(M0) > 10: need alpha > {alpha_dom_10:.4f}")
    print(f"  For w(M1)/w(M0) > 100: need alpha > {np.log(100)/delta_R_M1_M0:.4f}")
else:
    print("  R(M1) < R(M0): M0 is Euclidean-preferred over M1")

# ===========================================================================
# 4. FULL R(tau) PROFILE
# ===========================================================================

print("\n  PART 4: FULL R(tau) PROFILE")
print()

tau_full = np.linspace(0, 2.0, 201)
R_full = R_exact(tau_full)

print(f"  R(tau) range: [{np.min(R_full):.6f}, {np.max(R_full):.6f}]")
print(f"  R monotonically increasing: {np.all(np.diff(R_full) > 0)}")
print()

# R at grid points
tau_grid = np.arange(0, 2.1, 0.1)
print(f"  {'tau':>4}  {'R(tau)':>12}  {'R(tau)/R(0)':>12}  {'I_E pref vs M0':>14}")
print(f"  {'----':>4}  {'------':>12}  {'-----------':>12}  {'--------------':>14}")
for t in tau_grid:
    R = R_exact(t)
    ratio = R / R_M0
    pref = "M1 pref" if R > R_M0 else "M0 pref" if R < R_M0 else "equal"
    print(f"  {t:4.1f}  {R:12.6f}  {ratio:12.6f}  {pref:>14}")

# ===========================================================================
# 5. Constraint Gate ASSESSMENT
# ===========================================================================

print("\n  PART 5: Constraint Gate ASSESSMENT")
print()

# Check conditions
m1_preferred = R_M1 > R_M0  # Higher R => lower I_E => preferred
all_equal = abs(R_M0 - R_M1) < 1e-6 and abs(R_M0 - R_M2) < 1e-6

if all_equal:
    verdict = "CLOSED"
    verdict_detail = "I_E identical at all three monopoles (no saddle preference)"
    prob_shift = "-2 pp"
elif m1_preferred:
    # Check exponential dominance
    dom_ratio_natural = np.exp(alpha_natural * delta_R_M1_M0)
    if dom_ratio_natural > 10:
        verdict = "COMPELLING"
        verdict_detail = "I_E(M1) < I_E(M0) with exp(-delta I_E) > 10"
        prob_shift = "+5-8 pp"
    else:
        verdict = "INTERESTING"
        verdict_detail = "I_E(M1) < I_E(M0), M1 Euclidean-preferred"
        prob_shift = "+2-3 pp"
else:
    verdict = "NEUTRAL"
    verdict_detail = "I_E(M1) > I_E(M0), M0 preferred over M1"
    prob_shift = "0 pp"

print(f"  *** VERDICT: {verdict} ***")
print(f"  Detail: {verdict_detail}")
print(f"  Probability shift: {prob_shift}")
print()

# ===========================================================================
# 6. SUPPLEMENTARY: DNP STABILITY BOUND (SP-5, appended)
# ===========================================================================

print("  SUPPLEMENTARY: SP-5 DNP STABILITY BOUND lambda_L/m^2(tau)")
print()

# Load TT spectrum
try:
    tt_data = np.load(os.path.join(data_dir, 'l20_TT_spectrum.npz'), allow_pickle=True)
    tt_keys = list(tt_data.keys())
    print(f"  TT spectrum keys: {tt_keys}")

    # Check for eigenvalue data
    if 'tau' in tt_keys:
        tau_tt = tt_data['tau']
        # Find minimum TT eigenvalue
        for k in tt_keys:
            if 'eig' in k.lower() or 'lambda' in k.lower() or 'mu' in k.lower():
                print(f"  Found eigenvalue key: {k}, shape: {tt_data[k].shape}")

    print("  (Full SP-5 analysis would require extracting lambda_L_min at each tau)")
    print("  Deferring to SP-5 dedicated script if TT eigenvalue format is complex.")
except FileNotFoundError:
    print("  TT spectrum file not found. SP-5 deferred.")
except Exception as e:
    print(f"  Error loading TT data: {e}")
    print("  SP-5 deferred.")

# ===========================================================================
# 7. SUMMARY
# ===========================================================================

print("\n" + "=" * 78)
print("  SP-3 SUMMARY: EUCLIDEAN ACTION AT THREE MONOPOLES")
print("=" * 78)
print()
print(f"  R(M0, tau=0.00) = {R_M0:.10f}")
print(f"  R(M1, tau=0.15) = {R_M1:.10f}")
print(f"  R(M2, tau=1.55) = {R_M2:.10f}")
print()
print(f"  R(M1)/R(M0) = {R_M1/R_M0:.6f}")
print(f"  R(M2)/R(M0) = {R_M2/R_M0:.6f}")
print()
print(f"  R is monotonically increasing for tau > 0.")
print(f"  R(M1) > R(M0) => M1 is Euclidean-preferred over M0.")
print(f"  R(M2) >> R(M0) => M2 is strongly Euclidean-preferred.")
print()
print(f"  The Euclidean path integral selects the DEFORMED metric")
print(f"  over the round metric. Higher tau = lower I_E = more weight.")
print(f"  This is the OPPOSITE of the Weyl hypothesis (which selects tau=0).")
print()
print(f"  TENSION: Weyl hypothesis selects tau=0, Euclidean action selects tau->inf.")
print(f"  The framework needs a mechanism to SELECT a finite tau in [0.15, 0.55].")
print(f"  Neither Weyl minimization nor Euclidean maximization alone does this.")
print()
print(f"  *** VERDICT: {verdict} ***")
print(f"  {verdict_detail}")
print(f"  Probability shift: {prob_shift}")
print()
print("=" * 78)
