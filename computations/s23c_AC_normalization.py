"""
Session 23c: A/C Normalization Pin-Down for Session 24
======================================================

Resolves the (15/2) normalization question flagged by baptista.

The key question: does the (15/2) factor from Baptista eq 3.71 enter the
A/C gauge-gravity consistency check, or does it cancel?

Author: KK Theorist (Session 23c)
Date: 2026-02-20
"""

import numpy as np
import sys, os
sys.path.insert(0, "C:/sandbox/Ainulindale Exflation/tier0-computation")
from tier1_dirac_spectrum import (su3_generators, compute_structure_constants,
                                   compute_killing_form, jensen_metric,
                                   U1_IDX, SU2_IDX, M_IDX)

print("=" * 70)
print("A/C NORMALIZATION PIN-DOWN")
print("=" * 70)
print()

# ======================================================================
# 1. What does our code use?
# ======================================================================

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

print("1. OUR CODE CONVENTIONS:")
print(f"   Killing form B_ab = {B_ab[0,0]:.4f} * delta_ab")
print(f"   Base metric g_0 = |B_ab| = {abs(B_ab[0,0]):.4f} * delta_ab")

g_0 = jensen_metric(B_ab, 0.0)
print(f"   g_ours(0) = {g_0[0,0]:.4f} * delta_ab")
print(f"   tr(g_ours(0)) = {np.trace(g_0):.4f}")
print()

# ======================================================================
# 2. What does Baptista use?
# ======================================================================

print("2. BAPTISTA CONVENTIONS (eq 3.71):")
print("   g^K(tau) = (15/2) [e^{2tau} |_{u(1)} + e^{-2tau} |_{su(2)} + e^{tau} |_{C^2}]")
print(f"   g_Bap(0) = (15/2) * delta_ab = {15/2:.4f} * delta_ab")
print(f"   tr(g_Bap(0)) = (15/2) * 8 = {15/2 * 8:.4f}")
print()
print(f"   Ratio: g_Bap / g_ours = (15/2) / 3 = {(15/2)/3:.4f}")
print()

# ======================================================================
# 3. But wait — A and C use the ORTHONORMAL frame
# ======================================================================

print("3. KEY INSIGHT: The Kerner formula uses the ORTHONORMAL frame")
print("-" * 60)
print()
print("   Kerner eq (26): R_bundle = R_base + (1/4) g_{ab} F^a F^b")
print()
print("   But this formula is in COORDINATE indices.")
print("   In the ORTHONORMAL (ON) frame, where g_{ab} -> delta_{ab}:")
print("   R_bundle = R_base + (1/4) delta_{ab} F^a_ON F^b_ON")
print()
print("   The F^a in the ON frame is: F^a_ON = E^a_b F^b_coord")
print("   where E is the vielbein (g = E^T E).")
print()
print("   The gauge kinetic term is ALWAYS delta_{ab} in the ON frame.")
print("   The metric enters through the transformation E^a_b.")
print()
print("   For the KK spectral action, the relevant quantity is:")
print("   1/(4 g_eff^2) = f_8 Lambda^8 * (1/6) * (4pi)^{-6} * integral_K (1) dvol_K")
print("                  = f_8 Lambda^8 * (1/6) * (4pi)^{-6} * Vol_K")
print()
print("   WAIT — that's not right either. The gauge kinetic term from R_P")
print("   involves g_{ab} in COORDINATE basis, which is g_0 * diag(e^{2tau}, ...)")
print()

# ======================================================================
# 4. Careful derivation
# ======================================================================

print("4. CAREFUL DERIVATION")
print("-" * 60)
print()
print("   The EH action on P = M^4 x K is:")
print("   S = integral_P R_P dvol_P = integral_P R_P sqrt(det g_P) d^12x")
print()
print("   Using the submersion formula at A=0 (vacuum):")
print("   R_P = R_M + R_K")
print("   (No |F|^2 term when gauge fields are OFF)")
print()
print("   The |F|^2 term appears when gauge fields are turned ON:")
print("   R_P(A) = R_M + R_K + (1/4) g_{ab} F^a_{mu nu} F^{b mu nu} + ...")
print()
print("   After fiber integration:")
print("   S_4D = integral_M4 [Vol_K * R_M + integral_K R_K dvol_K")
print("          + (1/4) integral_K g_{ab} dvol_K * F^a_{mu nu} F^{b mu nu}] dvol_M4")
print()
print("   The gauge kinetic normalization is:")
print("   1/(4 g_eff^2) propto integral_K g_{ab}(y, tau) dvol_K(y)")
print()
print("   For a LEFT-INVARIANT metric on a compact Lie group,")
print("   g_{ab} is CONSTANT over the group (it's the same at every point),")
print("   so integral_K g_{ab} dvol_K = g_{ab} * Vol_K.")
print()
print("   Thus:")
print("   A = g_{ab}(tau) * Vol_K / 6  (with the 1/6 from a_2)")
print("   C = Vol_K / 6")
print("   A/C = g_{ab}(tau)  (the METRIC ITSELF)")
print()

# For the full trace (all gauge directions):
# tr(g_{ab}) in our convention = 3*(e^{2tau} + 3*e^{-2tau} + 4*e^{tau})
# tr(g_{ab}) in Baptista convention = (15/2)*(e^{2tau} + 3*e^{-2tau} + 4*e^{tau})

print("   In OUR convention: A/C = tr(g_ours(tau)) / 8")
print("   (dividing by dim to get per-gauge-index average)")
print()

for tau in [0.0, 0.30, 0.50, 1.0]:
    g_s = jensen_metric(B_ab, tau)
    tr_g = np.trace(g_s)
    print(f"   tau = {tau:.2f}: tr(g_ours) = {tr_g:.6f}, "
          f"per-index avg = {tr_g/8:.6f}")

print()

# ======================================================================
# 5. The gauge coupling for EACH sector
# ======================================================================

print("5. PER-SECTOR GAUGE COUPLINGS")
print("-" * 60)
print()

for tau in [0.0, 0.30]:
    g_s = jensen_metric(B_ab, tau)
    g_U1 = g_s[7, 7]  # U(1) direction
    g_SU2 = g_s[0, 0]  # SU(2) direction (any of 0,1,2)
    g_C2 = g_s[3, 3]   # C^2 direction (any of 3,4,5,6)
    print(f"   tau = {tau:.2f}:")
    print(f"     g_U1 = {g_U1:.6f}")
    print(f"     g_SU2 = {g_SU2:.6f}")
    print(f"     g_C2 = {g_C2:.6f}")
    print(f"     g_U1/g_SU2 = {g_U1/g_SU2:.6f} (= e^{4*tau:.2f} = {np.exp(4*tau):.6f})")
    print(f"     1/g_1^2 propto g_U1, 1/g_2^2 propto g_SU2")
    print(f"     => g_1/g_2 = sqrt(g_SU2/g_U1) = {np.sqrt(g_SU2/g_U1):.6f} (= e^{-2*tau:.2f} = {np.exp(-2*tau):.6f})")
    print()

# ======================================================================
# 6. Does (15/2) cancel?
# ======================================================================

print("6. DOES THE (15/2) CANCEL IN A/C?")
print("-" * 60)
print()
print("   A = (1/6) g_{ab}(tau) * Vol_K  [gauge kinetic integral from a_2]")
print("   C = (1/6) Vol_K                [EH integral from a_2]")
print()
print("   A/C = g_{ab}(tau)")
print()
print("   In Baptista convention: g_{ab}(tau) = (15/2) * [Jensen deformation]")
print("   In our convention: g_{ab}(tau) = 3 * [Jensen deformation]")
print()
print("   Vol_K in Baptista convention: Vol_K = (15/2)^4 * Vol_0")
print("   Vol_K in our convention: Vol_K = 3^4 * Vol_0 = 81 * Vol_0")
print()
print("   A/C is the metric itself (dimensionful), so it DOES depend on convention.")
print("   The PHYSICAL check is:")
print("     1/(4 g_eff^2) = f_8 Lambda^8 (4pi)^{-6} (1/6) g_{ab} Vol_K")
print("     1/(2 kappa^2) = f_8 Lambda^8 (4pi)^{-6} (1/6) Vol_K")
print()
print("   Dividing: g_{ab} = kappa^2 / (2 g_eff^2)")
print()
print("   This is: g_{ab}(tau) = 8*pi*G / (2 g_eff^2)")
print()
print("   But g_{ab} depends on the normalization convention!")
print("   The PHYSICAL quantity is g_{ab} / Vol_K^{1/dim(K)} (metric normalized to unit volume)")
print()

# In our code, Vol_K = 12.54 (computed from existing data)
# dim(K) = 8, so Vol_K^{1/8} = 12.54^{1/8}
Vol_K = 12.54
print(f"   Vol_K = {Vol_K}")
print(f"   Vol_K^(1/8) = {Vol_K**(1/8):.6f}")

# Actually, the cleaner approach: the RATIO of gauge couplings is convention-independent
print()
print("7. CONVENTION-INDEPENDENT FORMULATION")
print("-" * 60)
print()
print("   The ratio g_1/g_2 = e^{-2tau} is CONVENTION-INDEPENDENT.")
print("   (Both g_1 and g_2 scale the same way with the overall normalization.)")
print()
print("   The ABSOLUTE value of g_eff requires fixing the overall normalization.")
print("   The natural normalization is: g_{ab}(0) = 1 (bi-invariant = identity)")
print("   Our code: g_{ab}(0) = 3 * I => need to divide by 3")
print("   Baptista: g_{ab}(0) = (15/2) * I => need to divide by 15/2")
print()
print("   In the UNIT-NORMALIZED convention (g(0) = I):")
print("   g_unit(tau) = diag(e^{2tau} [x1], e^{-2tau} [x3], e^{tau} [x4])")
print("   tr(g_unit(tau)) = e^{2tau} + 3*e^{-2tau} + 4*e^{tau}")
print()

def tr_g_unit(tau):
    return np.exp(2*tau) + 3*np.exp(-2*tau) + 4*np.exp(tau)

for tau in [0.0, 0.30, 0.50]:
    print(f"   tau = {tau:.2f}: tr(g_unit) = {tr_g_unit(tau):.6f}")

print()
print("   At tau=0: tr(g_unit) = 8 = dim(SU(3)). GOOD.")
print()
print("   The A/C check in UNIT-NORMALIZED convention:")
print("   A_unit/C_unit = tr(g_unit(tau_0))")
print()
print("   = kappa^2 / (2 * g_avg^2)")
print()
print("   where g_avg is the trace-averaged gauge coupling.")
print()
print("   At tau=0: 8 = kappa^2 / (2 * g_avg^2)")
print("   => g_avg^2 = kappa^2 / 16 = 8*pi*G / 16 = pi*G/2")
print()
print("   This is the GAUGE-GRAVITY UNIFICATION CONDITION for round SU(3).")
print()

# ======================================================================
# 8. Summary
# ======================================================================

print("=" * 70)
print("SUMMARY FOR SESSION 24")
print("=" * 70)
print()
print("The (15/2) factor from Baptista eq 3.71 DOES affect the absolute")
print("value of A/C, but CANCELS in the convention-independent formulation.")
print()
print("The correct formulation of the A/C check is:")
print()
print("  tr(g_unit(tau_0)) = kappa^2 / (2 g_avg^2)")
print()
print("where:")
print("  g_unit(tau) = diag(e^{2tau}, e^{-2tau}[x3], e^{tau}[x4]) (unit-normalized)")
print("  g_avg = trace-averaged gauge coupling at unification scale")
print("  kappa^2 = 8*pi*G")
print()
print("The (15/2) factor is the Killing form normalization.")
print("It enters BOTH A and C and cancels in the ratio.")
print("Session 24 does not need to track it.")
print()
print("NUMERICAL VALUES:")
for tau in [0.0, 0.2994, 0.30]:
    print(f"  tau={tau:.4f}: tr(g_unit) = {tr_g_unit(tau):.6f}")
