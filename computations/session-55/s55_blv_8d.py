#!/usr/bin/env python3
"""
s55_blv_8d.py -- BLV Acoustic Scale Factor in d=8 Dimensions
=============================================================

Gate: BLV-8D-55 (INFO)
Purpose: Compute the Barcelo-Liberati-Visser conformal factor in d=8 dimensions
         and compare to the 4D result from S53.

Physics:
  The BLV acoustic metric for an irrotational barotropic fluid at rest
  in d spacetime dimensions (Barcelo, Liberati, Visser, gr-qc/0505065):

    g_{mu nu} = (rho / c_s)^{2/(d-1)} * diag(-c_s^2, 1, ..., 1)    ... (1)

  For d=4 (standard 3+1):  exponent = 2/3, a_BLV ~ (rho/c_s)^{1/3}
  For d=8 (M^4 x SU(3)):   exponent = 2/7, a_BLV ~ (rho/c_s)^{1/7}

  The spatial part of the metric gives the acoustic scale factor:
    g_{ij} = (rho/c_s)^{2/(d-1)} * delta_{ij}
    => a_acoustic^2 = (rho/c_s)^{2/(d-1)}
    => a_acoustic = (rho/c_s)^{1/(d-1)}

  For constant rho:
    a_acoustic = const * c_s^{-1/(d-1)}

  Therefore:
    N_e = ln(a_f/a_i) = -1/(d-1) * ln(c_s_f/c_s_i)
        = 1/(d-1) * ln(c_s_i/c_s_f)                                  ... (2)

  With c_s_i = c_fabric = 209.97 M_KK and c_s_f = c_Gold = 0.915 M_KK:
    c_s ratio = c_fabric/c_Gold = 229.48

Dimensional analysis:
  d=4: N_e = (1/3)*ln(229.48) = 1.81   [but S53 used (1/2)*ln, see below]
  d=8: N_e = (1/7)*ln(229.48) = 0.78

IMPORTANT SUBTLETY: The S53 computation used the 4D BLV formula:
  g_{mu nu} = (rho/c_s) * diag(-c_s^2, 1, 1, 1)
  => g_{ij} = (rho/c_s) * delta_{ij}
  => a^2 = rho/c_s
  => a = sqrt(rho/c_s)
  => N_e = (1/2)*ln(c_s_i/c_s_f)

This is because in 4D, (rho/c_s)^{2/(d-1)} = (rho/c_s)^{2/3}. But the
acoustic metric line element is:

  ds^2 = (rho/c_s)^{2/(d-1)} [-c_s^2 dt^2 + dx_i dx^i]

For the FRW comparison ds^2 = -N^2 dt^2 + a^2 dx^2, we identify:
  a^2 = (rho/c_s)^{2/(d-1)}
  => a = (rho/c_s)^{1/(d-1)}

The S53 result N_e = 2.72 used a = sqrt(rho/c_s). Let me verify:
  sqrt(rho/c_s) = (rho/c_s)^{1/2}
  (rho/c_s)^{1/(d-1)} with d=4 gives (rho/c_s)^{1/3}

RESOLUTION: The S53 formula a = sqrt(rho/c_s) is for the OVERALL conformal
prefactor in d=4. In 4D specifically:
  g_{mu nu} = (rho/c_s) * diag(-c_s^2, 1, 1, 1)
  The overall conformal factor is (rho/c_s). The spatial metric is:
  g_{ij} = (rho/c_s) * delta_{ij}
  So a^2 = (rho/c_s), i.e., a = (rho/c_s)^{1/2}

But in general d dimensions, BLV eq (2.12) generalizes to:
  g_{mu nu} = (rho/c_s)^{2/(d-1)} * diag(-c_s^2, 1, ..., 1)
  g_{ij} = (rho/c_s)^{2/(d-1)} * delta_{ij}
  a^2 = (rho/c_s)^{2/(d-1)}
  a = (rho/c_s)^{1/(d-1)}

Verification for d=4: a = (rho/c_s)^{1/3} ... but S53 got (rho/c_s)^{1/2}!

The discrepancy is because the ACTUAL BLV metric in d=4 is:
  g_{mu nu} = (rho^2/(c_s))^{1/(d-1)} * diag(-c_s^2, 1, 1, 1)  [Visser 1998]

Actually, let me be precise. From BLV (gr-qc/0505065) eq (2.12), the
d-dimensional acoustic metric for an irrotational barotropic fluid is:

  g_{mu nu}^acoustic = [rho^{d-1}/(c_s^{d-3})]^{1/(d-1)} * ...

No. Let me derive from first principles.

The action for the perturbation theta_1 of the velocity potential in a
barotropic fluid in d spacetime dimensions (1 time + n space, d = n+1):

  S = integral d^d x sqrt(-g_eff) g_eff^{mu nu} partial_mu theta_1 partial_nu theta_1

The effective metric is (Visser 1998, Barcelo+2005 Living Reviews eq 4):

  g_{mu nu}^eff = (rho/c_s) * | -(c_s^2 - v^2)   -v_j  |
                                |    -v_i         delta_ij|

This is SPECIFICALLY for d=4 (3+1). The conformal prefactor rho/c_s arises
from the normalization of the scalar field action.

In general d = n+1 dimensions (n spatial), the effective metric is:

  g_{mu nu}^eff = C(rho, c_s) * | -(c_s^2 - v^2)   -v_j  |
                                  |    -v_i         delta_ij|

where C is dimension-dependent. From the action principle:

  S propto integral d^d x rho/c_s^2 * [(partial_t theta_1)^2 - c_s^2 (nabla theta_1)^2]

  = integral d^d x rho/c_s^2 * g_eff^{mu nu} partial_mu theta_1 partial_nu theta_1 * sqrt(-g_eff)

For the massless scalar field equation, we need:

  partial_mu (sqrt(-g) g^{mu nu} partial_nu theta_1) = 0

The physical equation of motion is:

  rho/c_s^2 * partial_t^2 theta_1 - rho * nabla^2 theta_1 = 0

This must match:

  partial_mu (sqrt(-g_eff) g_eff^{mu nu} partial_nu theta_1) = 0

For v=0 homogeneous:
  -sqrt(-g_eff) g_eff^{00} = rho/c_s^2
  sqrt(-g_eff) g_eff^{ii} = rho

In d = n+1 dimensions with v=0:
  g^{00} = g_{00}^{-1}, g^{ii} = g_{ii}^{-1}, sqrt(-g) = sqrt(-g_{00}) * prod(g_{ii})^{1/2}

Let g_{00} = -A, g_{ii} = B (all spatial components equal). Then:
  g^{00} = -1/A, g^{ii} = 1/B
  sqrt(-g) = sqrt(A) * B^{n/2}

Conditions:
  sqrt(A) * B^{n/2} * (1/A) = rho/c_s^2  =>  B^{n/2}/sqrt(A) = rho/c_s^2   ... (I)
  sqrt(A) * B^{n/2} * (1/B) = rho          =>  sqrt(A) * B^{(n-2)/2} = rho   ... (II)

From (II): sqrt(A) = rho / B^{(n-2)/2}
Sub into (I): B^{n/2} * B^{(n-2)/2} / rho = rho/c_s^2
  => B^{(2n-2)/2} = rho^2/c_s^2
  => B^{n-1} = rho^2/c_s^2
  => B = (rho^2/c_s^2)^{1/(n-1)} = (rho/c_s)^{2/(n-1)} * c_s^0 ... wait

  B = (rho^2 / c_s^2)^{1/(n-1)}

From (II): sqrt(A) = rho / B^{(n-2)/2}
  B^{(n-2)/2} = (rho^2/c_s^2)^{(n-2)/(2(n-1))}
  sqrt(A) = rho / (rho^2/c_s^2)^{(n-2)/(2(n-1))}
           = rho * (c_s^2/rho^2)^{(n-2)/(2(n-1))}
           = rho^{1 - (n-2)/(n-1)} * c_s^{(n-2)/(n-1)}
           = rho^{1/(n-1)} * c_s^{(n-2)/(n-1)}
  A = rho^{2/(n-1)} * c_s^{2(n-2)/(n-1)}

Check: g_{00} = -A = -rho^{2/(n-1)} * c_s^{2(n-2)/(n-1)}

Verify for n=3 (d=4):
  B = (rho^2/c_s^2)^{1/2} = rho/c_s  ✓ (matches g_{ij} = rho/c_s)
  A = rho^{2/2} * c_s^{2*1/2} = rho * c_s  ✓ (matches g_{00} = -rho*c_s)

Now the acoustic scale factor:
  a^2 = B = (rho^2/c_s^2)^{1/(n-1)}
  a = (rho/c_s)^{1/(n-1)} * |rho/c_s|^0 ... let me be more careful:
  a = (rho^2/c_s^2)^{1/(2(n-1))} = (rho/c_s)^{1/(n-1)}

For constant rho:
  a propto c_s^{-1/(n-1)}
  N_e = -1/(n-1) * ln(c_s_f/c_s_i) = 1/(n-1) * ln(c_s_i/c_s_f)

For d=4 (n=3): N_e = (1/2)*ln(ratio) ✓ (matches S53)
For d=8 (n=7): N_e = (1/6)*ln(ratio)

Wait -- n is spatial dimensions, d = n+1 is spacetime dimensions.
d=8 means n=7 spatial dimensions. N_e = 1/(n-1) = 1/6.

But the task says 1/(d-1) = 1/7. Let me re-examine.

The task says: "the conformal factor is a^{2/(d-1)}" which gives 2/7 for d=8.
That would mean a = (...)^{1/(d-1)} = (...)^{1/7}.

My derivation gives a = (rho/c_s)^{1/(n-1)} where n = d-1. So:
  1/(n-1) = 1/(d-2).

For d=4: 1/(d-2) = 1/2 ✓
For d=8: 1/(d-2) = 1/6

The task prompt's formula 1/(d-1) = 1/7 appears to use a different convention.
Let me check what the BLV paper actually says for general dimensions.

The issue is: does the BLV metric prefactor go as (rho/c_s)^{2/(d-1)} or as
(rho/c_s)^{2/(d-2)}? My derivation from the wave equation gives B = (rho/c_s)^{2/(d-2)}.

I will compute BOTH conventions and report which is correct from first principles.

Session: S55
Author: Tesla-Resonance
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'computations')
from canonical_constants import *

print("=" * 72)
print("BLV-8D-55: 8D BLV Acoustic Scale Factor")
print("=" * 72)

# ================================================================
# PART 1: Sound Speed Data from S53
# ================================================================

print("\n--- PART 1: Input Data ---\n")

# From canonical_constants
cs_ratio = c_fabric / c_Gold
ln_ratio = np.log(cs_ratio)

print(f"c_fabric        = {c_fabric:.5f} M_KK")
print(f"c_Gold          = {c_Gold:.3f} M_KK")
print(f"c_fabric/c_Gold = {cs_ratio:.4f}")
print(f"ln(c_fabric/c_Gold) = {ln_ratio:.6f}")
print()

# S53 reference result
Ne_S53_4D = 0.5 * ln_ratio  # (1/2)*ln(229.48)
print(f"S53 reference: N_e^4D = (1/2)*ln({cs_ratio:.2f}) = {Ne_S53_4D:.4f}")
print(f"S53 reported:  N_e^4D = 2.7179")

# ================================================================
# PART 2: BLV Metric in General Dimension -- Derivation
# ================================================================

print("\n" + "=" * 72)
print("PART 2: BLV Metric Derivation in d Spacetime Dimensions")
print("=" * 72)
print()
print("Starting from the wave equation for perturbation theta_1 in a")
print("barotropic irrotational fluid at rest (v=0, homogeneous):")
print()
print("  rho/c_s^2 * d_t^2 theta_1 - rho * nabla^2 theta_1 = 0")
print()
print("In d = n+1 spacetime dimensions (n spatial), the acoustic metric")
print("is ds^2 = -A*dt^2 + B*dx_i*dx^i, with A and B determined by:")
print()
print("  Condition I:   B^{n/2}/sqrt(A) = rho/c_s^2")
print("  Condition II:  sqrt(A) * B^{(n-2)/2} = rho")
print()
print("Solution:")
print("  B = (rho^2/c_s^2)^{1/(n-1)}")
print("  A = rho^{2/(n-1)} * c_s^{2(n-2)/(n-1)}")
print()
print("Acoustic scale factor: a^2 = B = (rho/c_s)^{2/(n-1)}")
print("                       a   = (rho/c_s)^{1/(n-1)}")
print()
print("For constant rho:")
print("  a propto c_s^{-1/(n-1)}")
print("  N_e = 1/(n-1) * ln(c_s_i/c_s_f)")
print()
print("Since n = d-1 (spatial dims = spacetime dims - 1):")
print("  N_e = 1/(d-2) * ln(c_s_i/c_s_f)")
print()

# Numerical verification of the derivation for d=4
print("--- Verification for d=4 (n=3) ---")
n4 = 3
d4 = 4
rho_test = 1.5  # (local)
cs_test = np.array([0.5, 1.0, 2.0, 5.0])

print(f"  n=3, d=4: exponent = 1/(n-1) = 1/{n4-1} = {1/(n4-1):.4f}")
print(f"  Matches S53 formula a = sqrt(rho/c_s) = (rho/c_s)^{{1/2}}: YES")
print()

for cs in cs_test:
    B = (rho_test**2 / cs**2)**(1/(n4-1))
    A = rho_test**(2/(n4-1)) * cs**(2*(n4-2)/(n4-1))
    sqrtA = np.sqrt(A)
    # Check condition I: B^{n/2}/sqrt(A) = rho/cs^2
    lhs_I = B**(n4/2) / sqrtA
    rhs_I = rho_test / cs**2
    # Check condition II: sqrt(A) * B^{(n-2)/2} = rho
    lhs_II = sqrtA * B**((n4-2)/2)
    rhs_II = rho_test
    print(f"  c_s={cs:.1f}: B={B:.6f}, A={A:.6f}, "
          f"Cond_I: {abs(lhs_I - rhs_I):.2e}, Cond_II: {abs(lhs_II - rhs_II):.2e}")

print()
print("--- Verification for d=8 (n=7) ---")
n8 = 7
d8 = 8
print(f"  n=7, d=8: exponent = 1/(n-1) = 1/{n8-1} = {1/(n8-1):.6f}")
print()

for cs in cs_test:
    B = (rho_test**2 / cs**2)**(1/(n8-1))
    A = rho_test**(2/(n8-1)) * cs**(2*(n8-2)/(n8-1))
    sqrtA = np.sqrt(A)
    lhs_I = B**(n8/2) / sqrtA
    rhs_I = rho_test / cs**2
    lhs_II = sqrtA * B**((n8-2)/2)
    rhs_II = rho_test
    print(f"  c_s={cs:.1f}: B={B:.6f}, A={A:.6f}, "
          f"Cond_I: {abs(lhs_I - rhs_I):.2e}, Cond_II: {abs(lhs_II - rhs_II):.2e}")

# ================================================================
# PART 3: N_e Across Dimensions
# ================================================================

print("\n" + "=" * 72)
print("PART 3: Acoustic E-folds Across Dimensions")
print("=" * 72)
print()

dims_d = np.array([4, 5, 6, 7, 8, 9, 10])
dims_n = dims_d - 1  # spatial dimensions

# Correct exponent: 1/(n-1) = 1/(d-2)
exponents_correct = 1.0 / (dims_n - 1)
Ne_correct = exponents_correct * ln_ratio

# Task-prompt exponent: 1/(d-1)
exponents_prompt = 1.0 / (dims_d - 1)
Ne_prompt = exponents_prompt * ln_ratio

print(f"Sound speed ratio: c_fabric/c_Gold = {cs_ratio:.4f}")
print(f"ln(ratio) = {ln_ratio:.6f}")
print()
print("CORRECT formula from first principles: N_e = [1/(d-2)] * ln(ratio)")
print("  (derived from BLV wave equation in d spacetime dimensions)")
print()

print(f"{'d':>3s}  {'n=d-1':>5s}  {'1/(d-2)':>8s}  {'N_e':>10s}  {'N_e/N_e(4D)':>12s}")
print("-" * 48)
for i, d in enumerate(dims_d):
    ratio = Ne_correct[i] / Ne_correct[0] if Ne_correct[0] != 0 else 0
    print(f"{d:3d}  {dims_n[i]:5d}  {exponents_correct[i]:8.5f}  {Ne_correct[i]:10.4f}  {ratio:12.4f}")

print()
print("COMPARISON: Task-prompt formula N_e = [1/(d-1)] * ln(ratio)")
print()
print(f"{'d':>3s}  {'1/(d-1)':>8s}  {'N_e(d-1)':>10s}  {'1/(d-2)':>8s}  {'N_e(d-2)':>10s}  {'Difference':>10s}")
print("-" * 60)
for i, d in enumerate(dims_d):
    diff = Ne_prompt[i] - Ne_correct[i]
    print(f"{d:3d}  {exponents_prompt[i]:8.5f}  {Ne_prompt[i]:10.4f}  "
          f"{exponents_correct[i]:8.5f}  {Ne_correct[i]:10.4f}  {diff:+10.4f}")

# ================================================================
# PART 4: Physical Interpretation
# ================================================================

print("\n" + "=" * 72)
print("PART 4: The 8D Result and Its Physics")
print("=" * 72)
print()

Ne_4D = Ne_correct[0]  # d=4
Ne_8D = Ne_correct[4]  # d=8

print(f"4D result (d=4, n=3): N_e = (1/2)*ln({cs_ratio:.2f}) = {Ne_4D:.4f}")
print(f"8D result (d=8, n=7): N_e = (1/6)*ln({cs_ratio:.2f}) = {Ne_8D:.4f}")
print(f"Ratio: N_e(8D) / N_e(4D) = {Ne_8D/Ne_4D:.4f}")
print(f"  = (d_4D-2)/(d_8D-2) = 2/6 = {2/6:.4f}")
print()

# If using the task-prompt formula instead
Ne_8D_prompt = Ne_prompt[4]
print(f"Task-prompt formula gives N_e(8D) = (1/7)*ln({cs_ratio:.2f}) = {Ne_8D_prompt:.4f}")
print()

print("RESOLUTION OF EXPONENT AMBIGUITY:")
print("-" * 40)
print()
print("The BLV paper (Barcelo, Liberati, Visser 2005) writes the acoustic")
print("metric with an overall conformal factor. In d=n+1 spacetime dimensions:")
print()
print("  g_{mu nu} = [rho^n / c_s^{n-2}]^{1/(n-1)} * core metric")
print()
print("For v=0, the spatial part gives:")
print("  a^2 = [rho^n / c_s^{n-2}]^{1/(n-1)} / c_s^0  ... (spatial conformal)")
print("  = rho^{n/(n-1)} / c_s^{(n-2)/(n-1)}")
print()
print("For constant rho:")
print("  a propto c_s^{-(n-2)/(2(n-1))}   ... WRONG, this is the lapse part")
print()
print("Let me be VERY explicit. The acoustic line element for v=0 homogeneous:")
print("  ds^2 = -A dt^2 + B (dx_1^2 + ... + dx_n^2)")
print()
print("The scale factor is a = B^{1/2}.")
print("From my derivation: B = (rho^2/c_s^2)^{1/(n-1)}")
print("For constant rho: B propto c_s^{-2/(n-1)}")
print("                  a = B^{1/2} propto c_s^{-1/(n-1)}")
print()
print("This gives N_e = [1/(n-1)] * ln(c_s_i/c_s_f)")
print("         = [1/(d-2)] * ln(ratio)")
print()
print(f"For d=4: 1/(d-2) = 1/2   =>  N_e = {0.5*ln_ratio:.4f}  [matches S53 exactly]")
print(f"For d=8: 1/(d-2) = 1/6   =>  N_e = {ln_ratio/6:.4f}")
print()

# The S53 result (1/2)*ln(229) = 2.72 serves as the anchor check
print("ANCHOR CHECK: S53 computed N_e = (1/2)*ln(229.48) = 2.7179")
print(f"My formula:  (1/(4-2))*ln({cs_ratio:.2f}) = {ln_ratio/(4-2):.4f}")
print(f"Match: {abs(Ne_4D - 2.7179) < 0.001}")

# ================================================================
# PART 5: Dimensional Dependence Table (Final)
# ================================================================

print("\n" + "=" * 72)
print("PART 5: Final Results — Acoustic E-folds vs Dimension")
print("=" * 72)
print()
print(f"c_s ratio = {cs_ratio:.4f}")
print(f"ln(ratio) = {ln_ratio:.6f}")
print()
print(f"{'d':>3s}  {'n':>3s}  {'Exponent':>10s}  {'N_e':>10s}  {'N_e/N_e(4D)':>12s}  {'Physical interpretation':>35s}")
print("-" * 80)

interpretations = {
    4: "Standard 3+1 spacetime",
    5: "Kaluza-Klein 5D",
    6: "String theory compactification",
    7: "M-theory 11D -> 7D effective",
    8: "M^4 x SU(3) phonon-exflation",
    9: "9D (hypothetical)",
    10: "10D string / IIA/IIB"
}

for i, d in enumerate(dims_d):
    n = dims_n[i]
    exp = exponents_correct[i]
    ne = Ne_correct[i]
    ratio = ne / Ne_4D
    interp = interpretations.get(d, "")
    print(f"{d:3d}  {n:3d}  1/{d-2:<7d}  {ne:10.4f}  {ratio:12.4f}  {interp:>35s}")

# ================================================================
# PART 6: Why 8D Kills the Sound Speed Channel
# ================================================================

print("\n" + "=" * 72)
print("PART 6: The Dimensionality Problem")
print("=" * 72)
print()
print("The S53 result N_e = 2.89 (with geometry) was already marginal")
print(f"(short of 3.1 by 0.21 e-folds). In 8D, the sound speed channel")
print(f"contributes only N_e = {Ne_8D:.4f} instead of {Ne_4D:.4f}.")
print()
print(f"Full acoustic e-fold budget in 8D:")
print(f"  N_e^geom     = 0.1734  (unchanged — geometric e-folds)")
print(f"  N_e^sound(8D)= {Ne_8D:.4f}  (was {Ne_4D:.4f} in 4D)")
Ne_acoustic_8D = 0.1734 + Ne_8D
Ne_acoustic_4D = 0.1734 + Ne_4D
print(f"  N_e^density  = 0.0000  (cancels, P_exc=1.000)")
print(f"  ---------------------------------")
print(f"  N_e^acoustic(8D) = {Ne_acoustic_8D:.4f}")
print(f"  N_e^acoustic(4D) = {Ne_acoustic_4D:.4f}  (S53 result: 2.8913)")
print()
print(f"Reduction factor: {Ne_acoustic_8D/Ne_acoustic_4D:.4f}")
print()

print("PHYSICAL INTERPRETATION:")
print()
print("In a higher-dimensional superfluid, the acoustic scale factor is")
print("LESS sensitive to sound speed changes. The conformal factor")
print("distributes the effect across more spatial dimensions.")
print()
print("Superfluid analog: In 3He-B (3D), a change in c_s produces")
print("a ~ c_s^{-1/2} (the 4D BLV result). In a 7D superfluid,")
print("the same c_s change produces a ~ c_s^{-1/6} — the 'spring'")
print("of expansion is stiffer because there are more dimensions to absorb it.")
print()
print("This is a geometric DILUTION of the acoustic expansion effect.")
print("The 229x sound speed hierarchy, which provided 2.72 e-folds in 4D,")
print(f"provides only {Ne_8D:.4f} e-folds in 8D.")

# ================================================================
# PART 7: Critical Question — Which Dimension Applies?
# ================================================================

print("\n" + "=" * 72)
print("PART 7: Which Effective Dimension Applies?")
print("=" * 72)
print()
print("The answer depends on what the phonon 'sees'.")
print()
print("Case A: Phonon propagates in full M^4 x SU(3) (d_eff = 8)")
print(f"  N_e^sound = {Ne_8D:.4f}")
print(f"  The phonon sees ALL 7 spatial dimensions. Scale factor a lives")
print(f"  in the 7D spatial slice. Expansion is diluted.")
print()

# For M4 only, phonon confined to 4D
print("Case B: Phonon confined to M^4 (d_eff = 4)")
print(f"  N_e^sound = {Ne_4D:.4f}")
print(f"  The phonon only propagates in the 3 spatial dimensions of M^4.")
print(f"  SU(3) fiber enters only through c_s (which depends on KK geometry).")
print(f"  This is the S53 calculation.")
print()

# Intermediate: phonon has some KK excitation
print("Case C: Phonon has partial KK momentum (d_eff between 4 and 8)")
print("  N_e interpolates between the two cases.")
print("  The effective dimension depends on the phonon's KK momentum.")
print()

# For the acoustic Goldstone mode specifically
print("For the Goldstone mode (c_Gold = 0.915 M_KK):")
print("  This is a collective mode of the BCS condensate on SU(3).")
print("  Its wavefunction lives on SU(3) (it IS a fiber excitation).")
print("  But the EXPANSION is of M^4 (the geometric e-folds are 4D).")
print()
print("  The correct treatment is Case B: the phonon's dispersion relation")
print("  omega^2 = c_Gold^2 * k^2 refers to 3-momenta k on M^4.")
print("  The SU(3) structure determines c_Gold's VALUE but the metric")
print("  that describes expansion is the 4D FRW metric.")
print()
print("  This is EXACTLY the superfluid analog: in He-3 on a torus,")
print("  the sound speed depends on the internal structure (anisotropy),")
print("  but the effective spacetime seen by phonons is 3+1 dimensional.")

# ================================================================
# PART 8: Summary Table
# ================================================================

print("\n" + "=" * 72)
print("PART 8: Summary")
print("=" * 72)
print()
print("BLV-8D-55 RESULT:")
print()
print(f"  Sound speed ratio: {cs_ratio:.4f}")
print()
print(f"  d=4 (3+1):  N_e^sound = (1/2)*ln({cs_ratio:.2f}) = {Ne_4D:.4f}")
print(f"  d=5 (4+1):  N_e^sound = (1/3)*ln({cs_ratio:.2f}) = {Ne_correct[1]:.4f}")
print(f"  d=6 (5+1):  N_e^sound = (1/4)*ln({cs_ratio:.2f}) = {Ne_correct[2]:.4f}")
print(f"  d=7 (6+1):  N_e^sound = (1/5)*ln({cs_ratio:.2f}) = {Ne_correct[3]:.4f}")
print(f"  d=8 (7+1):  N_e^sound = (1/6)*ln({cs_ratio:.2f}) = {Ne_8D:.4f}")
print(f"  d=9 (8+1):  N_e^sound = (1/7)*ln({cs_ratio:.2f}) = {Ne_correct[5]:.4f}")
print(f"  d=10 (9+1): N_e^sound = (1/8)*ln({cs_ratio:.2f}) = {Ne_correct[6]:.4f}")
print()
print(f"  Correct exponent: 1/(d-2)  [NOT 1/(d-1)]")
print(f"  Task prompt had 1/(d-1)=1/7; correct is 1/(d-2)=1/6")
print(f"  Difference for d=8: {Ne_8D:.4f} vs {Ne_8D_prompt:.4f}")
print()
print(f"  N_e(8D)/N_e(4D) = {Ne_8D/Ne_4D:.4f} = 1/3")
print()
print(f"  Including geometry: N_e^acoustic(8D) = {Ne_acoustic_8D:.4f}")
print(f"  Including geometry: N_e^acoustic(4D) = {Ne_acoustic_4D:.4f}")
print()
print("  PHYSICAL CONCLUSION:")
print("  If phonons propagate in all 8 dimensions, the sound speed channel")
print("  is diluted by a factor of 3 relative to the 4D case.")
print("  However, for the phonon-exflation framework, the correct effective")
print("  dimension is d=4 (Case B): the Goldstone mode's dispersion involves")
print("  M^4 momenta, and expansion is a 4D phenomenon. SU(3) determines")
print("  the value of c_s but not the dimensionality of the acoustic metric.")

# ================================================================
# PART 9: Plot
# ================================================================

dims_full = np.arange(4, 21)
Ne_full = ln_ratio / (dims_full - 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left: N_e vs dimension
ax1.plot(dims_full, Ne_full, 'b-o', markersize=6, label=r'$N_e = \frac{1}{d-2}\ln(c_i/c_f)$')
ax1.axhline(y=Ne_4D, color='green', ls='--', alpha=0.6, label=f'4D: {Ne_4D:.2f}')
ax1.axhline(y=Ne_8D, color='red', ls='--', alpha=0.6, label=f'8D: {Ne_8D:.2f}')
ax1.axhline(y=3.1, color='orange', ls=':', alpha=0.6, label='Target: 3.1')
ax1.scatter([4], [Ne_4D], color='green', s=150, zorder=5, marker='*')
ax1.scatter([8], [Ne_8D], color='red', s=150, zorder=5, marker='*')
ax1.set_xlabel('Spacetime dimension d', fontsize=13)
ax1.set_ylabel(r'$N_e^{\rm sound}$', fontsize=13)
ax1.set_title(f'BLV Acoustic E-folds vs Dimension\n(c_s ratio = {cs_ratio:.1f})', fontsize=13)
ax1.legend(fontsize=10)
ax1.set_xlim(3.5, 20.5)
ax1.set_ylim(0, 3.5)
ax1.grid(True, alpha=0.3)

# Right: exponent vs dimension
ax2.plot(dims_full, 1.0/(dims_full - 2), 'r-s', markersize=6, label=r'$\frac{1}{d-2}$ (correct)')
ax2.plot(dims_full, 1.0/(dims_full - 1), 'b--^', markersize=6, label=r'$\frac{1}{d-1}$ (task prompt)')
ax2.scatter([4], [0.5], color='green', s=150, zorder=5, marker='*', label='d=4 anchor')
ax2.set_xlabel('Spacetime dimension d', fontsize=13)
ax2.set_ylabel('Exponent in N_e formula', fontsize=13)
ax2.set_title('BLV Conformal Exponent vs Dimension', fontsize=13)
ax2.legend(fontsize=10)
ax2.set_xlim(3.5, 20.5)
ax2.set_ylim(0, 0.6)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_blv_8d.png', dpi=150, bbox_inches='tight')
print("\nSaved: computations/session-55/s55_blv_8d.png")

# ================================================================
# PART 10: Save Data
# ================================================================

np.savez('computations/session-55/s55_blv_8d.npz',
         dims_d=dims_d,
         dims_n=dims_n,
         exponents_correct=exponents_correct,
         Ne_correct=Ne_correct,
         exponents_prompt=exponents_prompt,
         Ne_prompt=Ne_prompt,
         cs_ratio=cs_ratio,
         ln_ratio=ln_ratio,
         Ne_4D=Ne_4D,
         Ne_8D=Ne_8D,
         Ne_acoustic_4D=Ne_acoustic_4D,
         Ne_acoustic_8D=Ne_acoustic_8D,
         gate_name='BLV-8D-55',
         gate_verdict='INFO')

print("Saved: computations/session-55/s55_blv_8d.npz")

# ================================================================
# GATE VERDICT
# ================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: BLV-8D-55")
print("=" * 72)
print()
print("INFO: Acoustic e-folds computed across d = 4 through 10.")
print()
print(f"  d=4:  N_e^sound = {Ne_4D:.4f}  [S53 anchor, verified]")
print(f"  d=8:  N_e^sound = {Ne_8D:.4f}  [M^4 x SU(3)]")
print(f"  Ratio N_e(8D)/N_e(4D) = {Ne_8D/Ne_4D:.4f}")
print()
print("  Correct BLV exponent: 1/(d-2), NOT 1/(d-1)")
print(f"  Task prompt gave 1/7 = {1/7:.4f}; correct is 1/6 = {1/6:.4f}")
print(f"  Corrected N_e(8D) = {Ne_8D:.4f} (vs prompt's {Ne_8D_prompt:.4f})")
print()
print("  CLASSIFICATION: GEOMETRIC (dimensionality of acoustic metric)")
print()
print("  For phonon-exflation: d_eff = 4 is the physical choice.")
print("  The Goldstone mode disperses in M^4 momenta; SU(3) sets c_Gold's")
print("  value but does not add spatial dimensions to the acoustic metric.")
print("  The 8D calculation is an upper bound on the dilution effect IF")
print("  phonons had KK momentum — but they do not (B2 mode is a fiber mode).")
print()
print("=" * 72)
print(f"BLV-8D-55 COMPLETE: INFO (N_e_8D = {Ne_8D:.4f}, N_e_4D = {Ne_4D:.4f})")
print("=" * 72)
