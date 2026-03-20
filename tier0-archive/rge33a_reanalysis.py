#!/usr/bin/env python3
"""
RGE-33a REANALYSIS: Definitive assessment of the "wrong-sign hierarchy" claim.

The question: Does Baptista's framework give g_1 < g_2 (wrong sign) or g_1 < g_2
(right sign) at M_KK?

Key issue: The mapping between Baptista's Lie algebra blocks and SM couplings,
and the normalization factor that arises from the different trace norms of the
hypercharge generator Y vs the SU(2) generator T3.

References:
  - Paper 14 eq 2.85: g'/2 = 3 * sqrt(2M / <Y,Y>)
  - Paper 14 eq 2.88: g/2  = sqrt(2M / <T3,T3>)
  - Paper 14 eq 2.93: g'/2 = sqrt(3/lambda_1), g/2 = sqrt(1/lambda_2)
  - Paper 13 eq 5.21: same as 2.93
  - Paper 15 eq 3.68: Jensen metric lambda_1 = alpha*e^{2s}, lambda_2 = alpha*e^{-2s}
  - gauge_coupling_derivation.py: g_1/g_2 = e^{-2s} (MISSING sqrt(3) factor)

Author: Baptista-Spacetime-Analyst, reanalysis
Date: 2026-03-07
"""

import numpy as np
from scipy.optimize import brentq

print("=" * 70)
print("DEFINITIVE ANALYSIS: SM GAUGE COUPLING HIERARCHY")
print("=" * 70)

# =====================================================================
# PART 1: SM experimental values at M_Z
# =====================================================================

sin2_W = 0.23122
alpha_em_inv = 127.951
alpha_em = 1.0 / alpha_em_inv

# SM convention (NO GUT normalization):
# sin^2(theta_W) = g'^2 / (g^2 + g'^2)
# tan(theta_W) = g'/g
tan_W = np.sqrt(sin2_W / (1 - sin2_W))

print("\n--- SM experimental values at M_Z ---")
print(f"sin^2(theta_W) = {sin2_W}")
print(f"tan(theta_W) = g'/g = {tan_W:.6f}")
print(f"g' < g at M_Z (since tan(theta_W) < 1)")

# GUT normalization
g1_GUT_over_g2 = tan_W * np.sqrt(5.0/3.0)
print(f"\nGUT normalization: g_1_GUT/g_2 = tan(theta_W)*sqrt(5/3) = {g1_GUT_over_g2:.6f}")
print("g_1_GUT/g_2 < 1 at M_Z (it crosses 1 only near M_GUT ~ 10^15 GeV)")

# Alpha values at M_Z
alpha_Y_MZ = alpha_em / (1.0 - sin2_W)  # hypercharge coupling
alpha_2_MZ = alpha_em / sin2_W           # SU(2) coupling
alpha_1_GUT_MZ = (5.0/3.0) * alpha_Y_MZ

print(f"\nalpha_Y(M_Z) = {alpha_Y_MZ:.6f} = 1/{1.0/alpha_Y_MZ:.2f}")
print(f"alpha_2(M_Z) = {alpha_2_MZ:.6f} = 1/{1.0/alpha_2_MZ:.2f}")
print(f"alpha_1_GUT(M_Z) = {alpha_1_GUT_MZ:.6f} = 1/{1.0/alpha_1_GUT_MZ:.2f}")

g_prime_MZ = np.sqrt(4*np.pi*alpha_Y_MZ)
g_SU2_MZ = np.sqrt(4*np.pi*alpha_2_MZ)
g1_GUT_MZ = np.sqrt(4*np.pi*alpha_1_GUT_MZ)

print(f"\ng'(M_Z) = {g_prime_MZ:.6f}")
print(f"g(M_Z) = {g_SU2_MZ:.6f}")
print(f"g_1_GUT(M_Z) = {g1_GUT_MZ:.6f}")
print(f"\ng'/g(M_Z) = {g_prime_MZ/g_SU2_MZ:.6f} = tan(theta_W)")
print(f"g_1_GUT/g(M_Z) = {g1_GUT_MZ/g_SU2_MZ:.6f}")

print("\n" + "=" * 70)
print("KEY SM FACT: g' < g at ALL scales below M_GUT.")
print("The U(1)_Y coupling is SMALLER than the SU(2) coupling.")
print("=" * 70)

# =====================================================================
# PART 2: What Baptista actually says
# =====================================================================

print("\n" + "=" * 70)
print("PART 2: BAPTISTA'S COUPLING FORMULAS")
print("=" * 70)

print("""
From Paper 14, eqs 2.85 and 2.88:

  The hypercharge generator is Y = diag(-2i, i, i) in su(3).
  Its metric norm is <Y, Y> = 6*lambda_1  (from the u(1) block).

  The SU(2) generator is T3 = diag(0, i/2, -i/2) embedded in su(3).
  Its metric norm is <T3, T3> = 2*lambda_2  (from the su(2) block).

  g'/2 = 3 * sqrt(2*M_Pl / <Y,Y>) = 3 * sqrt(2*M_Pl / (6*lambda_1))
  g/2  = sqrt(2*M_Pl / <T3,T3>) = sqrt(2*M_Pl / (2*lambda_2))

In Planck units (M_Pl = 1), from eq 2.93 / eq 5.21:

  g'/2 = sqrt(3 / lambda_1)
  g/2  = sqrt(1 / lambda_2)

Therefore:
  g'/g = sqrt(3 * lambda_2 / lambda_1)

For the Jensen metric (eq 3.68 of Paper 15):
  lambda_1(s) = alpha * e^{2s}   (u(1) block)
  lambda_2(s) = alpha * e^{-2s}  (su(2) block)

Therefore:
  g'/g = sqrt(3 * e^{-2s} / e^{2s}) = sqrt(3) * e^{-2s}
""")

# =====================================================================
# PART 3: The normalization error in gauge_coupling_derivation.py
# =====================================================================

print("=" * 70)
print("PART 3: THE NORMALIZATION ERROR")
print("=" * 70)

print("""
gauge_coupling_derivation.py (line 78) states:
  g_1/g_2 = e^{-2s}

This formula treats all generators as having EQUAL Killing norm.
It defines g_i ~ lambda_i^{-1/2} democratically.

But Baptista's eq 2.93 gives:
  g'/g = sqrt(3 * lambda_2 / lambda_1) = sqrt(3) * e^{-2s}

The factor of sqrt(3) comes from:
  <Y, Y> / <T3, T3> = 6*lambda_1 / (2*lambda_2)

  But the coupling ratio involves the INVERSE:
  (g'/g)^2 = [3/<Y,Y>] / [1/<T3,T3>] = 3*<T3,T3>/<Y,Y>
           = 3 * 2*lambda_2 / (6*lambda_1) = lambda_2/lambda_1

  Wait -- let me recompute directly from eq 2.93:
  g'/2 = sqrt(3/lambda_1)  =>  g' = 2*sqrt(3/lambda_1)
  g/2  = sqrt(1/lambda_2)  =>  g  = 2*sqrt(1/lambda_2)

  g'/g = sqrt(3/lambda_1) / sqrt(1/lambda_2) = sqrt(3*lambda_2/lambda_1)
""")

# Verify numerically
for s in [0.0, 0.15, 0.190, 0.30, 0.50, 0.576]:
    L1 = np.exp(2*s)
    L2 = np.exp(-2*s)
    gprime_over_g = np.sqrt(3.0 * L2 / L1)
    g1_over_g2_code = np.exp(-2*s)
    sin2_formulaB = 3*L2 / (L1 + 3*L2)
    sin2_formulaA = L2 / (L1 + L2)  # = 1/(1+e^{4s})
    print(f"s={s:.3f}: g'/g = sqrt(3)*e^{{-2s}} = {gprime_over_g:.6f} | "
          f"code g1/g2 = e^{{-2s}} = {g1_over_g2_code:.6f} | "
          f"sin2_B = {sin2_formulaB:.6f} | sin2_A = {sin2_formulaA:.6f}")

# =====================================================================
# PART 4: sin^2(theta_W) from Baptista -- Formula B
# =====================================================================

print("\n" + "=" * 70)
print("PART 4: WEINBERG ANGLE -- FORMULA A vs FORMULA B")
print("=" * 70)

print("""
Formula A (used in gauge_coupling_derivation.py, line 287):
  sin^2(theta_W) = g_1^2 / (g_1^2 + g_2^2) = 1/(1 + e^{4s})
  This uses the WRONG coupling ratio g_1/g_2 = e^{-2s}.

Formula B (Baptista eq 2.93, correct):
  sin^2(theta_W) = g'^2 / (g'^2 + g^2)
                  = (3/lambda_1) / (3/lambda_1 + 1/lambda_2)
                  = 3*lambda_2 / (lambda_1 + 3*lambda_2)
                  = 3*L_2 / (L_1 + 3*L_2)

At s=0: Formula A gives 1/2 = 0.500; Formula B gives 3/4 = 0.750.
These are DIFFERENT. Formula B is the one derived by Baptista.
""")

# Find s_0 from Formula B
def sin2_B(s):
    return 3*np.exp(-2*s) / (np.exp(2*s) + 3*np.exp(-2*s))

s_target_B = brentq(lambda s: sin2_B(s) - sin2_W, 0, 2)
print(f"Formula B: sin^2 = 0.2312 requires s_0 = {s_target_B:.6f}")
print(f"  g'/g at s_0 = {np.sqrt(3)*np.exp(-2*s_target_B):.6f}")
print(f"  SM target g'/g = {tan_W:.6f}")

# Find s_0 from Formula A
def sin2_A(s):
    return 1.0 / (1.0 + np.exp(4*s))

s_target_A = brentq(lambda s: sin2_A(s) - sin2_W, 0, 2)
print(f"\nFormula A: sin^2 = 0.2312 requires s_0 = {s_target_A:.6f}")
print(f"  g_1/g_2 at s_0 = e^{{-2*{s_target_A:.4f}}} = {np.exp(-2*s_target_A):.6f}")
print(f"  SM target g'/g = {tan_W:.6f}")

# =====================================================================
# PART 5: RGE running -- THE CORRECT ANALYSIS
# =====================================================================

print("\n" + "=" * 70)
print("PART 5: RGE RUNNING (CORRECT NORMALIZATION)")
print("=" * 70)

M_Z = 91.1876
M_KK = 1e16
L = np.log(M_KK / M_Z)

# Non-GUT beta coefficients for alpha_Y and alpha_2
# d(1/alpha_Y)/d(ln mu) = -b_Y/(2*pi)
# d(1/alpha_2)/d(ln mu) = -b_2/(2*pi)
# b_Y = 41/6 (non-GUT hypercharge)
# b_2 = -19/6

b_Y = 41.0 / 6.0
b_2_coeff = -19.0 / 6.0

# Run UP from M_Z to M_KK
inv_aY_KK = 1.0/alpha_Y_MZ - b_Y/(2*np.pi) * L
inv_a2_KK = 1.0/alpha_2_MZ - b_2_coeff/(2*np.pi) * L

alpha_Y_KK = 1.0/inv_aY_KK
alpha_2_KK = 1.0/inv_a2_KK

gprime_g_KK_SM = np.sqrt(alpha_Y_KK / alpha_2_KK)
sin2_KK_SM = alpha_Y_KK / (alpha_Y_KK + alpha_2_KK)

print(f"SM running to M_KK = 10^16 GeV (non-GUT normalization):")
print(f"  alpha_Y(M_KK)  = {alpha_Y_KK:.6f} = 1/{1/alpha_Y_KK:.2f}")
print(f"  alpha_2(M_KK)  = {alpha_2_KK:.6f} = 1/{1/alpha_2_KK:.2f}")
print(f"  g'/g(M_KK)     = {gprime_g_KK_SM:.6f}")
print(f"  sin^2(M_KK)    = {sin2_KK_SM:.6f}")

# Baptista prediction at the dump point
s_dump = 0.190
gprime_g_baptista = np.sqrt(3.0) * np.exp(-2*s_dump)
sin2_baptista = sin2_B(s_dump)

print(f"\nBaptista at s = {s_dump}:")
print(f"  g'/g = sqrt(3)*e^{{-2*{s_dump}}} = {gprime_g_baptista:.6f}")
print(f"  sin^2(theta_W) = {sin2_baptista:.6f}")

print(f"\nComparison at M_KK:")
print(f"  SM requires:    g'/g = {gprime_g_KK_SM:.6f}")
print(f"  Baptista gives: g'/g = {gprime_g_baptista:.6f}")
print(f"  Ratio predicted/required = {gprime_g_baptista/gprime_g_KK_SM:.4f}")
print(f"  Deviation: {abs(gprime_g_baptista-gprime_g_KK_SM)/gprime_g_KK_SM*100:.1f}%")

# Now: does g' < g? YES, because sqrt(3)*e^{-0.380} = 1.184
# Wait, sqrt(3) ~ 1.732, e^{-0.380} ~ 0.684, product ~ 1.184
# That means g' > g at s=0.190! That's WRONG.

print("\n" + "=" * 70)
print("PART 6: THE ACTUAL HIERARCHY CHECK")
print("=" * 70)

print(f"\nAt s = {s_dump}:")
print(f"  g'/g = {gprime_g_baptista:.6f}")
if gprime_g_baptista > 1:
    print("  g' > g  --  hypercharge coupling LARGER than SU(2)")
    print("  SM requires g' < g at ALL scales below M_GUT")
    print("  THIS IS INDEED A WRONG-SIGN HIERARCHY (but not for the reason the gate claims)")
else:
    print("  g' < g  -- correct sign")

print(f"\nAt s = {s_target_B} (where sin^2 = 0.2312 under Formula B):")
gprime_g_at_target = np.sqrt(3) * np.exp(-2*s_target_B)
print(f"  g'/g = {gprime_g_at_target:.6f}")
print(f"  SM target: {tan_W:.6f}")

# Let's check: at what s does g'/g = SM value at M_KK?
s_for_SM = brentq(lambda s: np.sqrt(3)*np.exp(-2*s) - gprime_g_KK_SM, 0, 5)
print(f"\ng'/g = {gprime_g_KK_SM:.4f} (SM at M_KK) requires s = {s_for_SM:.6f}")
sin2_at_s_for_SM = sin2_B(s_for_SM)
print(f"  sin^2(theta_W)_tree at that s = {sin2_at_s_for_SM:.6f}")

# =====================================================================
# PART 7: RECHECK THE s33a GATE LOGIC
# =====================================================================

print("\n" + "=" * 70)
print("PART 7: WHAT THE s33a GATE GOT WRONG AND RIGHT")
print("=" * 70)

print("""
The s33a_rge_gate.py made the following chain:

1. Used B-1 identity: g_1/g_2 = e^{-2*tau} = 0.684 at M_KK
   WHERE g_1 = u(1) coupling, g_2 = su(2) coupling
   with EQUAL Killing-form normalization for all generators.

2. Applied GUT normalization: g_1_GUT = sqrt(5/3) * g'
   with beta coefficient b_1 = 41/10 (GUT normalized).

3. Concluded: g_1 < g_2 at M_KK, and RGE makes it worse,
   so "wrong-sign hierarchy".

THE ERRORS:

Error 1: The identification g_1/g_2 = e^{-2s} uses democratic
   normalization. But Baptista's OWN derivation (eq 2.93) gives
   g'/g = sqrt(3/lambda_1) / sqrt(1/lambda_2) = sqrt(3*lambda_2/lambda_1)
        = sqrt(3) * e^{-2s}
   The factor sqrt(3) is MISSING from the code.

Error 2: GUT normalization (sqrt(5/3)) is WRONG here.
   Baptista's U(1) comes from the su(3) Lie algebra with
   Killing form normalization, NOT from SU(5) embedding.
   The correct normalization factor is sqrt(3) from the
   trace ratio <Y,Y>/<T3,T3> = 6*lambda_1 / (2*lambda_2).

Error 3: The "wrong-sign hierarchy" claim says g_1 < g_2.
   But in the SM, g' < g at ALL sub-GUT scales!
   The hypercharge coupling IS smaller than the SU(2) coupling.
   So g_1 < g_2 (in Baptista's democratic normalization)
   has the RIGHT SIGN for the coupling ordering.

HOWEVER: There IS a remaining problem.
   g'/g = sqrt(3)*e^{-2*0.190} = 1.184 at the dump point.
   This gives g' > g, which IS wrong-sign at M_KK.
   But at s = 0.576, g'/g = 0.549, matching the SM at M_Z.
   The question is whether s_dump = 0.190 is the right value
   to evaluate the gauge couplings.
""")

# =====================================================================
# PART 8: The two formulas and their different s_0 values
# =====================================================================

print("=" * 70)
print("PART 8: RECONCILIATION")
print("=" * 70)

print(f"""
Three different s_0 values appear:

1. s_dump = 0.190 (from the spectral action / modulus stabilization)
   g'/g = sqrt(3)*e^{{-0.380}} = {np.sqrt(3)*np.exp(-0.380):.4f}
   sin^2_B = {sin2_B(0.190):.4f}

2. s_0 = {s_target_A:.4f} (Formula A: sin^2 = 1/(1+e^{{4s}}) = 0.2312)
   This uses the WRONG formula (missing sqrt(3)).
   g_1/g_2 = e^{{-2*{s_target_A:.4f}}} = {np.exp(-2*s_target_A):.4f} = tan(theta_W)

3. s_0 = {s_target_B:.4f} (Formula B: sin^2 = 3L2/(L1+3L2) = 0.2312)
   This is the CORRECT Baptista formula.
   g'/g = sqrt(3)*e^{{-2*{s_target_B:.4f}}} = {np.sqrt(3)*np.exp(-2*s_target_B):.4f}

The gauge coupling derivation code used Formula A and found s_0 ~ 0.30.
This accidentally gave a reasonable answer because:
  e^{{-2*0.30}} = 0.549 ~ tan(theta_W) = 0.549
But this was the wrong formula.

The CORRECT Formula B gives s_0 ~ {s_target_B:.3f}.
At this s, g'/g = {np.sqrt(3)*np.exp(-2*s_target_B):.4f} = tan(theta_W)  [by construction]

So: sin^2(theta_W) = 0.231 is achievable in Baptista's framework
if s_0 ~ {s_target_B:.3f}. But the dump point is s = 0.190.
""")

# =====================================================================
# PART 9: The actual hierarchy at s_dump vs required
# =====================================================================

print("=" * 70)
print("PART 9: DEFINITIVE ASSESSMENT")
print("=" * 70)

s_dump = 0.190
gprime_g_dump = np.sqrt(3) * np.exp(-2*s_dump)
sin2_dump_B = sin2_B(s_dump)

# What the SM needs at M_KK
gprime_g_SM_KK = gprime_g_KK_SM

print(f"""
FACT 1: Baptista's correct coupling formula (eq 2.93) gives
  g'/g = sqrt(3) * e^{{-2s}}

FACT 2: At s = 0 (bi-invariant): g'/g = sqrt(3) = 1.732
  This means g' > g at the symmetric point.
  sin^2(theta_W) = 3/4 = 0.75 at s = 0.

FACT 3: As s increases from 0, g'/g decreases monotonically.
  It crosses g'/g = 1 at s = ln(3)/4 = {np.log(3)/4:.4f}.
  It reaches the SM value tan(theta_W) = 0.549 at s = {s_target_B:.4f}.

FACT 4: At the dump point s = {s_dump}:
  g'/g = {gprime_g_dump:.4f}
  sin^2_B = {sin2_dump_B:.4f}
  This gives g' > g (WRONG sign for M_KK ~ 10^16 GeV,
  where the SM requires g'/g ~ {gprime_g_SM_KK:.4f}).

FACT 5: The SM requires g'/g to INCREASE from UV to IR
  (g' has positive beta function, g has negative).
  At M_Z: g'/g = {tan_W:.4f}
  At M_KK: g'/g = {gprime_g_SM_KK:.4f}
  So at M_KK, the SM needs g' < g (i.e., g'/g < 1).

FACT 6: Baptista at s = {s_dump} gives g'/g = {gprime_g_dump:.4f} > 1.
  The SM at M_KK ~ 10^16 gives g'/g = {gprime_g_SM_KK:.4f} < 1.
  This IS a wrong-sign hierarchy IF s_dump is identified as the
  value at M_KK.

CONCLUSION:
  The RGE-33a FAIL verdict is CORRECT in its conclusion (the
  gauge coupling hierarchy is wrong at s_dump = 0.190) but
  WRONG in its reasoning:

  - It used g_1/g_2 = e^{{-2s}} = 0.684 (missing sqrt(3) factor)
  - It applied GUT normalization sqrt(5/3) (inapplicable here)
  - It claimed "g_1 < g_2" is wrong-sign (but g' < g IS the right sign!)

  The CORRECT statement is:
  - g'/g = sqrt(3)*e^{{-2s}} = {gprime_g_dump:.4f} at s_dump = {s_dump}
  - This gives g' > g (hypercharge LARGER than SU(2))
  - The SM requires g' < g at M_KK
  - So the hierarchy IS wrong, but for the OPPOSITE reason
    from what the gate claims.

  The gate says: "g_1 < g_2 is wrong, need g_1 > g_2"
  Reality says: "g' > g is wrong, need g' < g"

  The ratio e^{{-2s}} < 1 (g_1 < g_2) is actually the RIGHT direction
  for making g' < g. The problem is that sqrt(3)*e^{{-2s}} > 1 at
  s = 0.190, so the sqrt(3) factor pushes it back to wrong-sign.

  Need s > ln(3)/4 = {np.log(3)/4:.4f} to get g' < g.
  s_dump = 0.190 < {np.log(3)/4:.4f}, so the hierarchy is wrong.

  BUT: the gate's claim that "e^{{-2s}} < 1 is wrong-sign" is ITSELF
  wrong. e^{{-2s}} < 1 means g_1 < g_2 in democratic normalization,
  which HELPS make g' < g. The problem is not enough suppression.
""")

# =====================================================================
# PART 10: Has the mapping been consistent across sessions?
# =====================================================================

print("=" * 70)
print("PART 10: HISTORICAL CONSISTENCY OF BLOCK-COUPLING MAPPING")
print("=" * 70)

print("""
Session 16, Round 3a (line 330):
  "g_1^2 ~ 1/g_{u(1)} = e^{-2s}"
  "g_2^2 ~ 1/g_{su(2)} = e^{2s}"
  => g_1/g_2 = e^{-2s}
  MAPPING: g_1 = U(1), g_2 = SU(2)

Session 16, Round 3b (line 187-188):
  "g_1 (U(1) coupling) ~ e^{-s_0}"
  "g_2 (SU(2) coupling) ~ e^{s_0}"
  => g_1/g_2 = e^{-2s_0}
  NOTE: These expressions g_1 ~ e^{-s} are WRONG. They confuse
  g_i ~ lambda_i^{-1/2} with g_i ~ e^{+/-s}. The correct formulas
  from B-1 are g_1 ~ e^{-s} (lambda_1 = e^{2s}, so lambda_1^{-1/2} = e^{-s}).
  But this means g_1/g_2 = e^{-s}/e^{s} = e^{-2s}. Consistent.

Session 17a B-1 (gauge_coupling_derivation.py):
  g_1/g_2 = e^{-2s}
  g_1 = u(1), g_2 = su(2)
  USES: democratic Killing normalization (all generators equal)
  MISSING: sqrt(3) factor from Baptista eq 2.93.

Session 30b (s30b_rge_running.py, line 27-28):
  "Formula B (correct, Baptista Paper 14 eq 2.93):
   sin^2(theta_W) = 3*L2 / (L1 + 3*L2)"
  NOTE: Session 30 KNEW Formula B was correct!
  But then used alpha_1_GUT/alpha_2 = 5*L2/L1 (line 214-215)
  which mixes GUT normalization with Baptista normalization.

Session 33a (s33a_rge_gate.py):
  Used g_1/g_2 = e^{-2*0.190} = 0.684
  Applied GUT normalization b_1 = 41/10
  Used sin^2 = alpha_1/(alpha_1 + (5/3)*alpha_2)
  VERDICT: "wrong-sign hierarchy"

CONCLUSION ON CONSISTENCY:
  The block-to-coupling mapping (g_1 = u(1), g_2 = su(2)) has been
  CONSISTENT across all sessions. Nobody ever swapped them.

  BUT: the normalization has been INCONSISTENT. The sqrt(3) factor
  from Baptista eq 2.93 was known in Session 30 (Formula B) but
  was NOT incorporated into the B-1 identity or the RGE gate.

  Session 30 correctly identified Formula B as the right formula,
  but then Session 33a reverted to using g_1/g_2 = e^{-2s} WITHOUT
  the sqrt(3) correction, combined with GUT normalization.
""")

# =====================================================================
# FINAL VERDICT
# =====================================================================

print("=" * 70)
print("FINAL VERDICT")
print("=" * 70)

print("""
Q1: Which block maps to which coupling?
  u(1) -> U(1)_Y (hypercharge, g')
  su(2) -> SU(2)_L (weak, g)
  This has been CONSISTENT across all sessions and matches Baptista.

Q2: Is GUT normalization appropriate?
  NO. Baptista's U(1) comes from su(3) with Killing form, not SU(5).
  The correct normalization factor is sqrt(3) from <Y,Y>/<T3,T3> = 3,
  NOT sqrt(5/3) from SU(5) embedding. Using GUT normalization here
  is a CATEGORY ERROR.

Q3: Formula A vs Formula B?
  Formula B (sin^2 = 3*L2/(L1+3*L2)) is Baptista's result (eq 2.93).
  Formula A (sin^2 = 1/(1+e^{4s})) uses the WRONG coupling ratio.
  Session 30 correctly identified this. Session 33a regressed.

Q4: Is g_1/g_2 = e^{-2s} < 1 the "right ordering"?
  In DEMOCRATIC normalization: g_1 < g_2 means the u(1) direction
  is more stretched (larger lambda_1), giving smaller coupling.

  In PHYSICAL normalization: g'/g = sqrt(3)*e^{-2s}, which is > 1
  for s < ln(3)/4 = 0.275. So at s_dump = 0.190, g' > g (WRONG).
  The factor sqrt(3) > 1 overwhelms the e^{-2s} < 1 suppression.

  The user is PARTIALLY RIGHT: in democratic normalization,
  g_1 < g_2 is indeed the right direction (helps make g' < g).
  But it is not sufficient -- the sqrt(3) factor from the trace
  normalization difference pushes g'/g > 1 at s = 0.190.

Q5: Has the mapping been consistent?
  YES for the block identification.
  NO for the normalization -- sqrt(3) was lost between Session 30
  and Session 33a.

OVERALL: The "wrong-sign hierarchy" claim is PARTIALLY WRONG.
  - The SIGN of the ratio e^{-2s} < 1 is the RIGHT direction.
  - The user is correct that agents flip-flopped on normalization.
  - The MAGNITUDE is wrong (need more suppression at s = 0.190).
  - The verdict FAIL is correct but for DIFFERENT reasons than stated.
  - The correct statement is: at s_dump = 0.190, g'/g = 1.184 > 1,
    while the SM requires g'/g < 1 at M_KK. The hierarchy reversal
    happens at s = 0.275, not at s = 0.
  - The gate should have used Formula B throughout.
  - The GUT normalization should NOT have been applied.
""")
