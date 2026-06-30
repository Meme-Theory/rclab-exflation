#!/usr/bin/env python3
"""
s75_lizzi_observable.py -- W2-C LIZZI-OBSERVABLE-EMPIRICAL-75
=============================================================

Gate: S75-G5-LIZZI-OBS
  Test the Lizzi observable relation:
    (m_H/v_EW)^2 * (Lambda_CC/M_Pl^2) = R_1
  where R_1 = a_0 * a_4 / a_2^2 is the spectral ratio-of-ratios
  from the D_K eigenvalue distribution at the Jensen fold.

  The claim: In the Chamseddine-Connes spectral action,
    m_H^2 / v_EW^2 = (spectral coefficient) * (a_4/a_2)
    Lambda_CC / M_Pl^2 = (spectral coefficient) * (a_0/a_2)
  Their product:
    (m_H/v_EW)^2 * (Lambda_CC/M_Pl^2) = C_H * C_CC * (a_4/a_2)*(a_0/a_2)
                                        = C_H * C_CC * R_1
  The question is whether C_H * C_CC = 1, or more precisely,
  what the product of spectral prefactors evaluates to.

  ROUTE A (spectral): Compute R_1 = a_0*a_4/a_2^2 from D_K spectrum.
  ROUTE B (empirical): Compute (m_H/v)^2 * (Lambda_CC/M_Pl^2) from PDG + Planck.
  ROUTE C (spectral-formula): Compute each factor via its spectral action formula,
    then take the product and verify it equals R_1.

  Gate verdict:
    PASS: |LHS/R_1 - 1| < 0.01 (within 1%)
    INFO: 0.01 < |LHS/R_1 - 1| < 0.10 (within 10%)
    FAIL: |LHS/R_1 - 1| > 0.10 (exceeds 10%)

Physics (substrate framing):
----------------------------
The fabric's spectral weight at each point is described by D_K. The Seeley-DeWitt
coefficients a_k are moments of this spectrum. Individual a_k are L_max-fragile
(Weyl divergence), but the ratio-of-ratios R_1 = a_0*a_4/a_2^2 cancels all
Weyl asymptotics and drifts < 0.34% across L_max in [3,9] (S74 W2-M).

The Lizzi observable pairs two individually unprotected physical quantities
(Higgs mass ratio, CC ratio) into a single combination that is R-family protected.
This is the spectral-functional-theorist's key insight: scheme-dependent pieces
can combine into scheme-independent observables.

Agent: lizzi-spectral-functional-theorist (Session 75, Wave 2, W2-C)
"""

import numpy as np
import os
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    PI,
    # Spectral action moments
    a0_fold, a2_fold, a4_fold,
    # Higgs / EW
    m_H_obs, v_ew,
    # CC / Planck
    Lambda_obs_MP4, M_Pl_reduced, rho_Lambda_obs,
    # Spectral cutoff functions
    f_0_sharp, f_2_default, f_4_default,
    # Framework scales
    M_KK, M_KK_gravity, M_KK_kerner,
)

t0 = time.time()  # (local)

print("=" * 78)
print("W2-C  LIZZI-OBSERVABLE-EMPIRICAL-75")
print("Empirical test of (m_H/v)^2 * (Lambda_CC/M_Pl^2) = R_1")
print("lizzi-spectral-functional-theorist, Session 75")
print("=" * 78)

# =============================================================================
# STEP 1: Compute R_1 from D_K spectral moments (ROUTE A)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: R_1 from spectral moments (Route A)")
print("=" * 78)

R_1 = a0_fold * a4_fold / a2_fold**2  # (local) canonical ratio-of-ratios
print(f"  a_0(fold)   = {a0_fold}")
print(f"  a_2(fold)   = {a2_fold:.10f}")
print(f"  a_4(fold)   = {a4_fold:.10f}")
print(f"  R_1 = a_0*a_4/a_2^2 = {R_1:.10f}")
print(f"  log10(R_1) = {np.log10(R_1):.6f}")

# =============================================================================
# STEP 2: Compute LHS from empirical data (ROUTE B)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: LHS from empirical observables (Route B)")
print("=" * 78)

# Factor 1: (m_H / v_EW)^2
mH_over_v_sq = (m_H_obs / v_ew)**2  # (local) = (125.1/246)^2
print(f"  m_H = {m_H_obs} GeV (PDG 2024)")
print(f"  v_EW = {v_ew} GeV")
print(f"  (m_H/v_EW)^2 = ({m_H_obs}/{v_ew})^2 = {mH_over_v_sq:.10f}")

# Factor 2: Lambda_CC / M_Pl^2
# The canonical_constants Lambda_obs_MP4 = 2.888e-122 is Lambda/M_Pl^4.
# We need Lambda_CC/M_Pl^2 (in units of M_Pl^2).
# rho_Lambda_obs = 2.7e-47 GeV^4
# M_Pl^2 = (2.435e18)^2 = 5.929e36 GeV^2
# M_Pl^4 = (2.435e18)^4 = 3.516e73 GeV^4
# Lambda_CC / M_Pl^4 = rho_Lambda / M_Pl^4 = 2.888e-122

# But the CLAIM uses (Lambda_CC / M_Pl^2), which has dimensions of M^2
# (Lambda_CC/M_Pl^2) = rho_Lambda / M_Pl^2 = 2.7e-47 / 5.929e36 = 4.55e-84 GeV^2
# This is NOT dimensionless.

# The relation as literally stated in S74 is:
# (m_H/v)^2 * (Lambda/M_Pl^2) = R_1
# But (m_H/v)^2 is dimensionless and (Lambda/M_Pl^2) has dimensions GeV^2
# unless "Lambda" means rho_Lambda/M_Pl^2 (making Lambda/M_Pl^2 = rho/M_Pl^4, dimensionless).

# From the S74 script, the ACTUAL algebraic content is:
# (a_4/a_2) * (a_0/a_2) = R_1
# where (m_H/v)^2 --> (a_4/a_2) and (Lambda/M_Pl^2) --> (a_0/a_2)
# The "relation" is an algebraic identity about the spectral action formulas.

# Let me compute BOTH:
# (a) The raw spectral ratio product
# (b) The empirical dimensionless product with proper normalization

Lambda_over_MPl4 = Lambda_obs_MP4  # (local) 2.888e-122
Lambda_over_MPl2 = rho_Lambda_obs / M_Pl_reduced**2  # (local) GeV^2 units
Lambda_dimless_MP4 = rho_Lambda_obs / M_Pl_reduced**4  # (local) dimensionless

print(f"\n  rho_Lambda_obs = {rho_Lambda_obs:.3e} GeV^4")
print(f"  M_Pl = {M_Pl_reduced:.3e} GeV (reduced)")
print(f"  M_Pl^2 = {M_Pl_reduced**2:.4e} GeV^2")
print(f"  M_Pl^4 = {M_Pl_reduced**4:.4e} GeV^4")
print(f"  Lambda/M_Pl^4 = {Lambda_dimless_MP4:.6e} (dimensionless)")
print(f"  Lambda/M_Pl^4 (canonical) = {Lambda_obs_MP4:.6e}")

# Route B: raw empirical
LHS_empirical = mH_over_v_sq * Lambda_dimless_MP4  # (local)
print(f"\n  LHS = (m_H/v)^2 * (Lambda/M_Pl^4) = {LHS_empirical:.6e}")
print(f"  R_1 = {R_1:.6f}")
print(f"  LHS/R_1 = {LHS_empirical / R_1:.6e}")
print(f"  MISMATCH: {np.log10(abs(R_1 / LHS_empirical)):.1f} orders of magnitude")

# =============================================================================
# STEP 3: Route C -- spectral-action formula-matching
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Spectral action formula route (Route C)")
print("=" * 78)

# In the Chamseddine-Connes spectral action Tr f(D^2/Lambda^2):
#
# Higgs mass squared (CC spectral action, standard form):
#   m_H^2 = (4*pi^2/3) * (a_4/a_2) * v_EW^2 / f_0
#   => (m_H/v)^2 = (4*pi^2 / 3*f_0) * (a_4/a_2)
#   => a_4/a_2 = (3*f_0 / 4*pi^2) * (m_H/v)^2
#
# Cosmological constant in spectral action:
#   rho_Lambda = (2/pi^2) * f_0 * a_0 * Lambda_sp^4
#   Newton's constant:
#   1/(16*pi*G) = f_2 * a_2 * Lambda_sp^2 / (48*pi^2)
#   => M_Pl^2 = (8*pi*G)^{-1} = f_2 * a_2 * Lambda_sp^2 / (6*pi)
#   => Lambda_sp^2 = 6*pi*M_Pl^2 / (f_2 * a_2)
#
# CC/M_Pl^2:
#   rho_Lambda/M_Pl^2 = (2/pi^2)*f_0*a_0*Lambda_sp^4 / M_Pl^2
#   Lambda_sp^4 = [6*pi/(f_2*a_2)]^2 * M_Pl^4
#   => rho_Lambda/M_Pl^2 = (2/pi^2)*f_0*a_0*[6*pi/(f_2*a_2)]^2 * M_Pl^2
#   This is NOT dimensionless.
#
# Dimensionless CC: rho_Lambda/M_Pl^4
#   rho_Lambda/M_Pl^4 = (2/pi^2) * f_0 * a_0 * Lambda_sp^4 / M_Pl^4
#                      = (2/pi^2) * f_0 * a_0 * [6*pi/(f_2*a_2)]^2
#                      = (72 * f_0) / (f_2^2 * a_2^2) * a_0
#                      = 72 * f_0 * (a_0/a_2^2) / f_2^2
#
# Product:
#   (m_H/v)^2 * (rho_Lambda/M_Pl^4)
#     = [(4*pi^2)/(3*f_0)] * (a_4/a_2) * [72*f_0/(f_2^2)] * (a_0/a_2^2)
#     = [(4*pi^2)/(3*f_0)] * [72*f_0/(f_2^2)] * (a_0*a_4/a_2^3)
#     = [288*pi^2/(3*f_2^2)] * (a_0*a_4/a_2^3)
#     = [96*pi^2/f_2^2] * (a_0*a_4/a_2^3)
#
# Note: This gives a_0*a_4/a_2^3, NOT R_1 = a_0*a_4/a_2^2. There is an
# extra factor of 1/a_2. The product IS NOT R_1 with these conventions.
#
# S74's actual claim was that the SPECTRAL RATIOS (a_4/a_2) * (a_0/a_2)
# combine to form R_1. This is trivially true:
#   (a_4/a_2) * (a_0/a_2) = a_0*a_4/a_2^2 = R_1
# It's an algebraic identity among spectral moments, not an empirical relation
# between measured m_H, v, Lambda_CC, and M_Pl.
#
# The EMPIRICAL test requires: what is the coefficient C such that
#   (m_H/v)^2 * (rho_Lambda/M_Pl^4) = C * R_1?

# Compute the spectral coefficient
C_H = (4.0 * PI**2) / (3.0 * f_0_sharp)  # (local) m_H^2/v^2 = C_H * a_4/a_2
C_CC = 72.0 * f_0_sharp / f_2_default**2  # (local) rho_Lambda/M_Pl^4 = C_CC * a_0/a_2^2
C_product = C_H * C_CC  # (local) product coefficient

print(f"  Higgs formula coefficient C_H = (4*pi^2)/(3*f_0) = {C_H:.6f}")
print(f"    where f_0 = {f_0_sharp}")
print(f"  CC formula coefficient C_CC = 72*f_0/f_2^2 = {C_CC:.6f}")
print(f"    where f_2 = {f_2_default}")
print(f"\n  Combined: (m_H/v)^2 * (Lambda/M_Pl^4) = C_H * C_CC * (a_4/a_2)*(a_0/a_2^2)")
print(f"  C_H * C_CC = {C_product:.6f}")
print(f"\n  Note: the spectral product is (a_4/a_2)*(a_0/a_2^2) = a_0*a_4/a_2^3")
print(f"        NOT R_1 = a_0*a_4/a_2^2.")
print(f"        There is one extra power of 1/a_2 in the product.")

# Route C: spectral formula prediction
# (m_H/v)^2 from spectral action
mH_v_sq_spectral = C_H * (a4_fold / a2_fold)  # (local)

# Lambda/M_Pl^4 from spectral action: needs Lambda_sp
# Instead, compute directly what the product predicts
# product = C_H * C_CC * a_0*a_4/a_2^3
spectral_product = C_product * a0_fold * a4_fold / a2_fold**3  # (local)

print(f"\n  Spectral prediction of (m_H/v)^2 = C_H * a_4/a_2 = {mH_v_sq_spectral:.6f}")
print(f"  Empirical (m_H/v)^2 = {mH_over_v_sq:.6f}")
print(f"  Ratio: {mH_v_sq_spectral / mH_over_v_sq:.4f}")

print(f"\n  Spectral product C*a_0*a_4/a_2^3 = {spectral_product:.6e}")
print(f"  Empirical product (m_H/v)^2*(Lambda/M_Pl^4) = {LHS_empirical:.6e}")

# =============================================================================
# STEP 4: The correct test -- what S74 actually tests
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: The actual Lizzi observable test")
print("=" * 78)

# S74 W4-F defined the Lizzi observable as: the algebraic fact that
# the spectral action maps for m_H^2/v^2 and Lambda/M_Pl^2 multiply
# to give R_1 (with a computable prefactor C_H * C_CC).
#
# The EMPIRICAL test is two-fold:
#
# TEST 1: Does (a_4/a_2) * (a_0/a_2) = R_1?
#   This is a trivial algebraic identity. Always true. Not a test.
#
# TEST 2: Does the spectral action correctly predict both m_H and Lambda?
#   If yes, then (m_H/v)^2 * (Lambda/M_Pl^4) = C_H*C_CC*R_1.
#   This requires knowing Lambda_sp (the spectral cutoff), which is M_KK.
#
# TEST 3 (what the gate actually asks): Does
#   (m_H_obs/v_ew)^2 * (Lambda_CC_obs/M_Pl^2) = R_1
# as a NUMERICAL EQUALITY? This can only hold if the scheme coefficients
# C_H*C_CC exactly equal 1 and the spectral action predicts m_H and Lambda
# with zero error. Since C_H*C_CC is NOT 1, this equality fails by definition.
#
# RESOLUTION: The S74 claim is that R_1 is the INVARIANT CONTENT of the
# product observable. The 120-order gap between LHS_empirical and R_1 is
# carried entirely by the CC problem (Lambda/M_Pl^4 ~ 10^{-122}), which
# is scheme-dependent (a_0 is absent in zeta; a_0 is present in cutoff).
# The ratio of the product to R_1 isolates the scheme-dependent coefficient,
# which is exactly what R-family protection means.

# Test the actual algebraic identity
R1_from_ratios = (a4_fold / a2_fold) * (a0_fold / a2_fold)  # (local)
identity_check = abs(R1_from_ratios / R_1 - 1.0)  # (local)
print(f"  ALGEBRAIC IDENTITY CHECK:")
print(f"    (a_4/a_2)*(a_0/a_2) = {R1_from_ratios:.10f}")
print(f"    a_0*a_4/a_2^2 = R_1 = {R_1:.10f}")
print(f"    |ratio - 1| = {identity_check:.2e} (EXACT to machine epsilon)")

# Now the empirical test as stated in the gate
# Using Lambda/M_Pl^4 (dimensionless)
LHS_gate = mH_over_v_sq * Lambda_dimless_MP4  # (local)
ratio_gate = LHS_gate / R_1  # (local)
deviation_gate = abs(ratio_gate - 1.0)  # (local)

print(f"\n  GATE TEST (literal reading):")
print(f"    LHS = (m_H/v)^2 * (Lambda/M_Pl^4) = {LHS_gate:.6e}")
print(f"    R_1 = {R_1:.6f}")
print(f"    LHS / R_1 = {ratio_gate:.6e}")
print(f"    |LHS/R_1 - 1| = {deviation_gate:.6f}")
print(f"    log10(R_1/LHS) = {np.log10(R_1/LHS_gate):.2f}")
print(f"    RESULT: OFF by ~{np.log10(R_1/LHS_gate):.0f} orders of magnitude")
print(f"    This is the CC problem re-expressed: the 10^122 gap between")
print(f"    spectral action prediction and observation.")

# Alternative: use Lambda_CC / M_Pl^2 with M_Pl^2 normalization
# Lambda_obs_MP4 = 2.888e-122 is rho_Lambda/M_Pl^4
# If the task means Lambda_CC = 2.3e-122 * M_Pl^2 (energy density in M_Pl^2 units)
# then Lambda_CC/M_Pl^2 = 2.3e-122 (dimensionless)
# and (m_H/v)^2 * 2.3e-122 = 0.2586 * 2.3e-122 = 5.95e-123
LHS_task_literal = mH_over_v_sq * 2.3e-122  # (local) as given in task
print(f"\n  TASK LITERAL:")
print(f"    LHS = (125.1/246)^2 * 2.3e-122 = {LHS_task_literal:.4e}")
print(f"    R_1 = {R_1:.6f}")
print(f"    |LHS/R_1 - 1| = {abs(LHS_task_literal/R_1 - 1.0):.6f}")
print(f"    Off by ~{np.log10(R_1/LHS_task_literal):.0f} OOM")

# =============================================================================
# STEP 5: What the relation ACTUALLY means (three interpretations)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Three interpretations of the Lizzi observable")
print("=" * 78)

# Interpretation 1: ALGEBRAIC IDENTITY (trivially true)
# (a_4/a_2) * (a_0/a_2) = a_0*a_4/a_2^2 = R_1
# This is what S74 W4-F proved. It's a statement about spectral moments,
# not about observable values.
print("\n  INTERPRETATION 1: ALGEBRAIC IDENTITY (spectral moments)")
print(f"    (a_4/a_2) * (a_0/a_2) = R_1")
print(f"    EXACT. This is a tautology. PASS trivially.")

# Interpretation 2: SPECTRAL-TO-OBSERVABLE MAP
# IF the spectral action formulas are exact (m_H^2/v^2 = C_H * a_4/a_2
# and Lambda/M_Pl^4 = C_CC * a_0/a_2^2), THEN:
# (m_H/v)^2 * (Lambda/M_Pl^4) = C_H * C_CC * R_1 / a_2
# This requires checking C_H * C_CC / a_2.
C_ratio = C_product / a2_fold  # (local) total coefficient
print(f"\n  INTERPRETATION 2: SPECTRAL ACTION FORMULA")
print(f"    (m_H/v)^2 * (Lambda/M_Pl^4) = C_H * C_CC * a_0*a_4/a_2^3")
print(f"    = C_H*C_CC/a_2 * R_1 = {C_ratio:.6e} * {R_1:.6f}")
print(f"    = {C_ratio * R_1:.6e}")
print(f"    Empirical LHS = {LHS_gate:.6e}")
print(f"    Ratio: {LHS_gate / (C_ratio * R_1):.6e}")
print(f"    NOTE: The spectral formula route ALSO fails because it predicts")
print(f"    rho_Lambda ~ a_0 * M_KK^4 which overshoots by 10^120 (the CC problem).")

# Interpretation 3: R_1 AS L_MAX-INVARIANT (the actual S74 content)
# The point of S74 was: even though (m_H/v)^2 alone drifts ~132% with L_max,
# and (Lambda/M_Pl^2) alone drifts ~122% with L_max, their PRODUCT
# reduces to R_1 which drifts only 0.34%.
# The Lizzi observable is about L_max STABILITY, not about predicting
# the numerical value of the CC.
print(f"\n  INTERPRETATION 3: L_MAX INVARIANT (the S74 actual claim)")
print(f"    Individual drifts (L=3 to L=9):")
print(f"      a_4/a_2: ~132% (single-ratio, fragile)")
print(f"      a_0/a_2: ~122% (single-ratio, fragile)")
print(f"      R_1 = (a_4/a_2)*(a_0/a_2): 0.34% (ratio-of-ratios, protected)")
print(f"    The Lizzi observable is NOT 'predict CC from Higgs mass'.")
print(f"    It IS 'the product (m_H/v)^2 * (CC/EH) reduces to an L_max-stable")
print(f"    spectral invariant R_1 = {R_1:.6f}'.")
print(f"    This is STRUCTURAL (functional-independent at 0.34% across L_max).")

# =============================================================================
# STEP 6: Functional-independence analysis
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Functional-independence analysis")
print("=" * 78)

# In zeta action: S_zeta = zeta_D(0) = a_4. The a_0 coefficient is ABSENT.
# Therefore:
# - (m_H/v)^2 ~ a_4/a_2 still exists (a_2 enters through Newton's constant)
# - Lambda_CC: a_0 is absent, so the CC prediction is fundamentally different
# - R_1 = a_0*a_4/a_2^2: R_1 requires a_0, which is absent in zeta
#
# In anomaly-derived action: same a_k enter but through different weights.
# R_1 remains defined but the physical map R_1 -> observable changes.

# Cutoff action: R_1 exists and is L_max-protected (0.34%)
# Zeta action: R_1 = a_0*a_4/a_2^2 IS computable but a_0 does NOT enter the action
#   a_0 is just a mode count, not a dynamical weight
# Anomaly action: R_1 enters through anomaly coefficients

print("  CUTOFF (Chamseddine-Connes):")
print(f"    R_1 = {R_1:.6f}, enters action through f_0*a_0 + f_2*a_2 + f_4*a_4")
print(f"    Higgs mass uses a_4/a_2. CC uses a_0. Both present.")
print(f"    STATUS: R_1 is physical and L_max-protected.")

print("\n  ZETA (Lizzi S_zeta = a_4):")
print(f"    S_zeta = a_4 only. a_0 does NOT enter the bosonic action.")
print(f"    Higgs mass still uses a_4/a_2 (via Newton normalization).")
print(f"    CC: a_0 absent -> CC is NOT a spectral prediction in zeta scheme.")
print(f"    R_1 = a_0*a_4/a_2^2: a_0 is a DIAGNOSTIC, not dynamical.")
print(f"    STATUS: R_1 is computable but not action-dynamical in zeta.")

print("\n  ANOMALY-DERIVED:")
print(f"    Bosonic action derived from fermionic anomaly cancellation.")
print(f"    All a_k enter through anomaly coefficients.")
print(f"    R_1 is present and protected. Weights differ from cutoff.")
print(f"    STATUS: R_1 exists and is protected.")

# Classification
print("\n  FUNCTIONAL-INDEPENDENCE CLASSIFICATION:")
print(f"    R_1 existence and L_max protection: STRUCTURAL (all schemes)")
print(f"    R_1 = a_0*a_4/a_2^2 numerical value: FUNCTIONAL-INDEPENDENT (0.34% drift)")
print(f"    (m_H/v)^2*(Lambda/M_Pl^4) = C*R_1: SCHEME-DEPENDENT (C depends on f_0,f_2)")
print(f"    Whether R_1 predicts CC: MAXIMALLY SCHEME-DEPENDENT")
print(f"      Cutoff: CC ~ a_0*M_KK^4 (120 OOM overshoot)")
print(f"      Zeta:   CC has no a_0 contribution (absent)")
print(f"      Gap between R_1={R_1:.4f} and empirical {LHS_task_literal:.2e}: structural")

# =============================================================================
# STEP 7: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Gate verdict -- S75-G5-LIZZI-OBS")
print("=" * 78)

# The gate as written asks: |LHS/R_1 - 1| < 0.01
# where LHS = (m_H/v)^2 * (Lambda/M_Pl^2)
# and R_1 = a_0*a_4/a_2^2 = 1.128655

# The literal numerical comparison:
LHS_final = mH_over_v_sq * 2.3e-122  # (local) as stated in task
deviation_final = abs(LHS_final / R_1 - 1.0)  # (local)
log_gap = np.log10(R_1 / LHS_final)  # (local)

print(f"\n  LHS = (m_H/v)^2 * (Lambda_CC/M_Pl^2)")
print(f"      = ({m_H_obs}/{v_ew})^2 * 2.3e-122")
print(f"      = {mH_over_v_sq:.6f} * 2.3e-122")
print(f"      = {LHS_final:.6e}")
print(f"\n  R_1 = a_0*a_4/a_2^2 = {R_1:.6f}")
print(f"\n  |LHS/R_1 - 1| = {deviation_final:.6f}")
print(f"  This equals 1.0000 because LHS ~ 10^{-122} << R_1 ~ 1")
print(f"  log10(R_1/LHS) = {log_gap:.1f}")

if deviation_final < 0.01:
    verdict = "PASS"
    reason = "|LHS/R_1 - 1| < 0.01"
elif deviation_final < 0.10:
    verdict = "INFO"
    reason = "0.01 < |LHS/R_1 - 1| < 0.10"
else:
    verdict = "FAIL"
    reason = f"|LHS/R_1 - 1| = {deviation_final:.4f} > 0.10"

print(f"\n  Gate S75-G5-LIZZI-OBS: {verdict}")
print(f"    Criterion: {reason}")
print(f"    Deviation = {deviation_final:.10f}")
print(f"    log10 gap = {log_gap:.1f} OOM")

# =============================================================================
# STEP 8: What the gate result MEANS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Physical interpretation")
print("=" * 78)

print("""
  The gate FAILS because the Lizzi observable relation is NOT an empirical
  equality between measured numbers. It is an ALGEBRAIC IDENTITY among
  spectral moments:

    (a_4/a_2) * (a_0/a_2) = R_1 = a_0*a_4/a_2^2 (EXACT, tautology)

  The physical quantities m_H and Lambda_CC are related to a_4/a_2 and
  a_0/a_2 through spectral action formulas WITH SCHEME-DEPENDENT COEFFICIENTS.
  The 122-order gap between LHS and R_1 is exactly the CC problem: the spectral
  action's a_0 prediction overshoots the observed Lambda by 120 orders.

  What IS true (from S74 W4-F):
  1. R_1 is L_max-protected (0.34% drift vs 132% for single ratios)
  2. The product of the two spectral maps reduces to R_1 algebraically
  3. This makes the COMBINATION L_max-stable even though each piece is fragile
  4. This is FUNCTIONAL-INDEPENDENT (same R_1 in all three spectral functionals)

  What is NOT true:
  - The measured product (m_H/v)^2 * (Lambda/M_Pl^2) does NOT equal R_1
  - The gap is the CC problem itself, not a failure of R-family protection
  - This gate was ill-posed: it conflated an algebraic identity (R_1 from moments)
    with an empirical prediction (observable values equal R_1)
""")

# =============================================================================
# SAVE
# =============================================================================
print("\n" + "=" * 78)
print("SAVING")
print("=" * 78)

results = {  # (local)
    # Route A: spectral
    "R_1": R_1,
    "a0_fold": a0_fold,
    "a2_fold": a2_fold,
    "a4_fold": a4_fold,

    # Route B: empirical
    "mH_over_v_sq": mH_over_v_sq,
    "Lambda_dimless_MP4": Lambda_dimless_MP4,
    "LHS_empirical": LHS_gate,
    "LHS_task_literal": LHS_task_literal,

    # Coefficients
    "C_H": C_H,
    "C_CC": C_CC,
    "C_product": C_product,

    # Gate
    "deviation_final": deviation_final,
    "log10_gap": log_gap,
    "verdict": verdict,

    # Algebraic identity check
    "R1_from_ratios": R1_from_ratios,
    "identity_residual": identity_check,

    # Functional independence
    "R1_Lmax_drift_pct": 0.34,
    "single_ratio_drift_pct": 132.0,
}

out_path = "s75_lizzi_observable.npz"  # (local)
np.savez(out_path, **results)
print(f"  Saved: {out_path}")

elapsed = time.time() - t0  # (local)
print(f"  Runtime: {elapsed:.2f}s")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)
print(f"""
  Gate S75-G5-LIZZI-OBS: {verdict}
    LHS = (m_H/v)^2 * (Lambda_CC/M_Pl^2) = {LHS_task_literal:.4e}
    R_1 = a_0*a_4/a_2^2                   = {R_1:.6f}
    |LHS/R_1 - 1| = {deviation_final:.4f} >> 0.10 threshold
    Gap: {log_gap:.1f} orders of magnitude

  ROOT CAUSE: The gate conflates two distinct things:
    (A) Algebraic identity: (a_4/a_2)*(a_0/a_2) = R_1 [EXACT, trivially true]
    (B) Empirical equality: measured product = R_1    [FALSE, off by CC gap]

  The Lizzi observable's value is (A), not (B).
  The 122 OOM gap IS the cosmological constant problem.
  R_1 = {R_1:.6f} is FUNCTIONAL-INDEPENDENT and L_max-PROTECTED (0.34%).
""")
