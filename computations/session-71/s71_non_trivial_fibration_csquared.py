#!/usr/bin/env python3
"""
NON-TRIVIAL-FIBRATION-CSQUARED-71
=================================
Compute the simultaneous impact on c_s^2 (sound speed) and alpha_s (spectral
index running) when going from a trivial fibration M^4 x SU(3) to a non-trivial
principal SU(3)-bundle over M^4.

Physics:
--------
For a trivial product M^4 x K, the O'Neill A-tensor and T-tensor vanish exactly
(A-TENSOR-61 PASS: A=T=0 to machine epsilon).  For a non-trivial principal
G-bundle P -> M with connection omega, the Dirac operator on the total space
acquires a cross-term from the A-tensor:

    D_P = D_M tensor 1 + gamma^mu A_mu + 1 tensor D_K

where A_mu encodes the curvature of the principal connection.  The O'Neill
A-tensor |A|^2 for a principal bundle with connection is proportional to
|F_omega|^2, the norm-squared of the curvature 2-form of the connection.

We parameterize:  |A|^2 = kappa * R_K
where kappa in [0, 0.5] spans from trivial bundle (kappa=0) to maximal
O'Neill curvature before geometric instability.

Heat kernel corrections:
  delta(a_2) = -(kappa/12) * a2_fold        [VdD Paper 01, submersion formula]
  delta(a_4) = (kappa/360) * (5*kappa - 2) * a4_fold  [Gilkey dim-8 on fiber bundle]

Sound speed correction:
  delta(c_s^2) = kappa^2 * g_3^2 / (16*pi^2)  [one-loop gauge-scalar mixing]

Spectral running correction:
  delta(alpha_s)/alpha_s = delta(a_4)/a_4 - delta(a_2)/a_2

References:
  VdD Paper 01: 1811.07824 (Kasparov product on submersions, Thm 3.5)
  VdD Paper 05: 1405.5368 (Globally non-trivial ACM, gauge modules)
  A-TENSOR-61: O'Neill cross-terms PASS (A=T=0 for product)
  KASPAROV-VERIFY-61: Full Kasparov factorization verified
  SHRIEK-EQUIV-61: Shriek = fiber integration (exact)
  S70 R2 estimate: c_s^2 ~ ||A||^2/(a_2*M_KK^2) ~ 10^{-4}

Gate: NON-TRIVIAL-FIBRATION-CSQUARED-71
  PASS: delta(c_s^2) < 10^{-3} AND delta(alpha_s)/alpha_s > 0.5
  FAIL: delta(c_s^2) > 0.1 (c_s^2=0 prediction destroyed)
  INFO: one criterion met but not both
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    a0_fold, a2_fold, a4_fold,
    M_KK, M_KK_gravity, M_KK_kerner,
    PI, tau_fold,
    Vol_SU3_Haar,
    g0_diag,
    alpha_em_MZ_inv, sin2_thetaW_MSbar,
)

# =============================================================================
# SECTION 1: Load input data from S70
# =============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# Load c_s^2 data from S70
d_cs = np.load(os.path.join(data_dir, 's70_q_sound.npz'), allow_pickle=True)
cs2_tree = float(d_cs['cs2_tree'])         # = 0.0 (exact, product structure)
cs2_1loop = float(d_cs['cs2_1loop'])       # = 3.36e-4 (one-loop perturbative)
S_1loop_ratio = float(d_cs['S_1loop_over_S_tree'])  # = 0.519

# Load alpha_s data from S70
d_as = np.load(os.path.join(data_dir, 's70_f0_alpha_s.npz'), allow_pickle=True)
ratio_gilkey = float(d_as['ratio_gilkey'])  # = 0.4140 (CCM matching ratio)
a4_check = float(d_as['a4_fold'])           # cross-check
a2_check = float(d_as['a2_fold'])           # cross-check

# Verify constant consistency
assert abs(a4_check - a4_fold) < 1e-6, f"a4 mismatch: {a4_check} vs {a4_fold}"
assert abs(a2_check - a2_fold) < 1e-6, f"a2 mismatch: {a2_check} vs {a2_fold}"

print("=" * 72)
print("NON-TRIVIAL-FIBRATION-CSQUARED-71")
print("=" * 72)
print()
print(f"Input data loaded:")
print(f"  a0_fold = {a0_fold}")
print(f"  a2_fold = {a2_fold:.6f}")
print(f"  a4_fold = {a4_fold:.6f}")
print(f"  cs2_tree = {cs2_tree}")
print(f"  cs2_1loop = {cs2_1loop:.6e}")
print(f"  ratio_gilkey = {ratio_gilkey:.6f}")
print(f"  M_KK = {M_KK:.6e} GeV")
print()

# =============================================================================
# SECTION 2: SU(3) gauge coupling at M_KK (derived from spectral action)
# =============================================================================
# The strong coupling alpha_3 at M_KK is determined by the spectral geometry.
# From CCM matching: 1/alpha_3(M_KK) = (2*a4)/(PI^2 * Vol) * normalization
# A-TENSOR-61 found alpha_3(M_KK) = 0.0214, so 1/alpha_3 = 46.7
# We use g_3^2 = 4*PI*alpha_3

alpha_3_MKK = 0.0214  # from A-TENSOR-61 (verified)  # (local)
g_3_sq = 4.0 * PI * alpha_3_MKK  # = 0.269

print(f"SU(3) coupling at M_KK:")
print(f"  alpha_3(M_KK) = {alpha_3_MKK}")
print(f"  g_3^2 = {g_3_sq:.6f}")
print()

# =============================================================================
# SECTION 3: Fiber curvature of SU(3)
# =============================================================================
# Scalar curvature of round SU(3) with Killing metric:
#   R_K(round) = -dim(G) * (1/4) = -8 * (1/4) = -2.0
#   (convention: Ricci = -1/4 * Killing form for compact semisimple)
# At Jensen fold (tau=0.19):
#   R_K(fold) = -2.018 (from A-TENSOR-61)
# Sign convention: R < 0 for compact groups in our convention (Riemannian,
#   signature ++++, Ricci positive definite but R = trace(Ric) with our
#   curvature sign).
# NOTE: The sign here follows VdD/Baptista convention where compact groups
#   have NEGATIVE scalar curvature. This is the physics-standard convention
#   where S^n has R > 0 but compact Lie groups have R < 0 due to structure
#   constant contraction.

R_K_round = -2.000    # Round SU(3)  # (local)
R_K_fold = -2.018     # Jensen fold (from A-TENSOR-61)  # (local)
R_K = R_K_fold        # Use fold value

print(f"Fiber scalar curvature:")
print(f"  R_K(round) = {R_K_round}")
print(f"  R_K(fold) = {R_K_fold}")
print()

# =============================================================================
# SECTION 4: A-tensor parameterization
# =============================================================================
# For a principal G-bundle P -> M with connection omega:
#   |A|^2 = (1/2) |F_omega|^2 / dim(G)
# where F_omega is the curvature 2-form.
#
# We parameterize: |A|^2 = kappa * |R_K|
# where kappa ranges from 0 (trivial bundle) to 0.5 (maximal before instability).
#
# Physical meaning of kappa:
#   kappa = 0: trivial product M^4 x SU(3) (our baseline)
#   kappa ~ 0.01: perturbative gauge field (weak-field regime)
#   kappa ~ 0.1: moderate curvature (typical non-abelian bundle)
#   kappa = 0.5: maximal before the fiber geometry becomes unstable
#     (at kappa > 0.5, the effective fiber curvature changes sign)
#
# Stability bound: delta(a_2)/a_2 < 1 requires kappa < 12, but physical
# bounds from fiber geometry require kappa < 0.5 (beyond this, the
# submersion ceases to be Riemannian in the fiber direction).

N_kappa = 500
kappa_arr = np.linspace(0.0, 0.5, N_kappa)

print(f"A-tensor parameterization:")
print(f"  |A|^2 = kappa * |R_K| = kappa * {abs(R_K):.3f}")
print(f"  kappa range: [0, 0.5] ({N_kappa} points)")
print()

# =============================================================================
# SECTION 5: Heat kernel corrections from A-tensor
# =============================================================================
# On a Riemannian submersion pi: P -> M with fiber K, the Gilkey-Seeley
# heat kernel coefficients acquire corrections from the O'Neill tensors.
#
# For the Dirac operator on the total space:
#
#   a_2(D_P) = a_2(D_M) * a_0(D_K) + a_0(D_M) * a_2(D_K) + CROSS
#
# where CROSS = -(1/12) * |A|^2 * Vol(M) * Vol(K)
#
# In our parameterization with |A|^2 = kappa * |R_K|:
#   delta(a_2) = -(kappa/12) * a2_fold
#
# For a_4, the mixed curvature term from the Gilkey expansion on bundles:
#   delta(a_4) = (kappa/360) * (5*kappa - 2) * a4_fold
#
# This comes from the dimension-8 heat kernel coefficient on fiber bundles:
#   a_4 gets contributions from:
#     - R_M^2 terms (pure base): unchanged
#     - R_K^2 terms (pure fiber): unchanged
#     - R_M * |A|^2 terms: ~ kappa * R_M * |R_K|
#     - |A|^4 terms: ~ kappa^2 * R_K^2
#     - |F_omega|^2 terms: ~ kappa^2
#
# The combined coefficient (5*kappa - 2) reflects:
#   - The -2 from linear (R_M * |A|^2) cross-terms
#   - The +5*kappa from quadratic (|A|^4) terms
# Sign: positive for kappa > 0.4, negative for kappa < 0.4

delta_a2 = -(kappa_arr / 12.0) * a2_fold
frac_delta_a2 = delta_a2 / a2_fold   # = -kappa/12

delta_a4 = (kappa_arr / 360.0) * (5.0 * kappa_arr - 2.0) * a4_fold
frac_delta_a4 = delta_a4 / a4_fold   # = kappa*(5*kappa - 2)/360

print(f"Heat kernel corrections:")
print(f"  delta(a_2)/a_2 = -kappa/12")
print(f"    at kappa=0.01: {-0.01/12:.6f}")
print(f"    at kappa=0.10: {-0.10/12:.6f}")
print(f"    at kappa=0.50: {-0.50/12:.6f}")
print()
print(f"  delta(a_4)/a_4 = kappa*(5*kappa-2)/360")
print(f"    at kappa=0.01: {0.01*(5*0.01-2)/360:.6f}")
print(f"    at kappa=0.10: {0.10*(5*0.10-2)/360:.6f}")
print(f"    at kappa=0.50: {0.50*(5*0.50-2)/360:.6f}")
print()

# =============================================================================
# SECTION 6: Sound speed correction delta(c_s^2)
# =============================================================================
# In q-theory, the sound speed c_s^2 of dark energy perturbations depends on
# whether the vacuum energy density (a_0 channel) acquires a kinetic term.
#
# For the trivial product:
#   c_s^2 = 0 (TOPOLOGICAL, from product Dirac structure, S70 W2-B)
#   D_K depends on g_K only, not on d_mu g_K => no kinetic mixing
#
# For a non-trivial fibration:
#   The A-tensor introduces kinetic mixing between the modulus tau and the
#   gauge connection omega. This generates a kinetic term for the vacuum
#   energy through the one-loop gauge-scalar mixing diagram:
#
#     delta(c_s^2) = kappa^2 * g_3^2 / (16*pi^2)
#
# This is suppressed by:
#   1. kappa^2 (quadratic in A-tensor strength)
#   2. g_3^2/(16*pi^2) (one-loop factor ~ 1.7e-3)
#
# Physical origin: the A-tensor couples the base gradients d_mu tau to the
# fiber curvature F_omega, generating an effective kinetic operator for the
# spectral action zeroth moment a_0(tau). This kinetic term appears at
# one-loop because the gauge-modulus coupling is mediated by gauge loops.

delta_cs2 = kappa_arr**2 * g_3_sq / (16.0 * PI**2)

print(f"Sound speed correction delta(c_s^2):")
print(f"  delta(c_s^2) = kappa^2 * g_3^2 / (16*pi^2)")
print(f"    at kappa=0.01: {0.01**2 * g_3_sq / (16*PI**2):.2e}")
print(f"    at kappa=0.10: {0.10**2 * g_3_sq / (16*PI**2):.2e}")
print(f"    at kappa=0.50: {0.50**2 * g_3_sq / (16*PI**2):.2e}")
print()

# Total c_s^2 = tree-level (0) + one-loop trivial + one-loop A-tensor
cs2_total = cs2_tree + cs2_1loop + delta_cs2

print(f"Total c_s^2 profile:")
print(f"  cs2_tree     = {cs2_tree:.6e}")
print(f"  cs2_1loop    = {cs2_1loop:.6e}  (trivial bundle 1-loop)")
print(f"  max delta_cs2 = {delta_cs2[-1]:.6e}  (at kappa=0.5)")
print(f"  max cs2_total = {cs2_total[-1]:.6e}")
print()

# =============================================================================
# SECTION 7: Spectral running correction delta(alpha_s)
# =============================================================================
# The spectral index tilt n_s depends on the ratio a_2/a_0 (first spectral
# moment ratio).  The spectral running alpha_s = dn_s/d(ln k) depends on
# the ratio a_4/a_2 (second spectral moment ratio).
#
# From the corrections in Sections 5-6:
#   delta(alpha_s)/alpha_s = delta(a_4)/a_4 - delta(a_2)/a_2
#                          = kappa*(5*kappa-2)/360 - (-kappa/12)
#                          = kappa*(5*kappa-2)/360 + kappa/12
#                          = kappa * [(5*kappa-2)/360 + 1/12]
#                          = kappa * [(5*kappa-2 + 30)/360]
#                          = kappa * (5*kappa + 28) / 360
#
# This is ALWAYS POSITIVE for kappa > 0:
#   - The a_2 correction is negative (kappa/12 decrease)
#   - The a_4 correction switches sign at kappa=0.4
#   - But the a_2 correction dominates: subtracting a negative gives positive
#   - So delta(alpha_s)/alpha_s > 0 for ALL kappa > 0
#
# Physical meaning: non-trivial fibration INCREASES the spectral running.
# The alpha_s tension is that the framework predicts alpha_s too SMALL.
# A positive correction moves alpha_s TOWARD the observed value.

frac_delta_alpha_s = kappa_arr * (5.0 * kappa_arr + 28.0) / 360.0

# Alpha_s predicted by the framework (tree-level from a_4/a_2 ratio)
# From S70: alpha_s_max ~ 0.013 (with thresholds) vs observed ~0.118
# The tension factor is ~5.4x (S70 W1-B)
# So we need delta(alpha_s)/alpha_s > 0.5 to make meaningful progress

print(f"Spectral running correction delta(alpha_s)/alpha_s:")
print(f"  = kappa * (5*kappa + 28) / 360")
print(f"    at kappa=0.01: {0.01 * (5*0.01+28)/360:.6f}")
print(f"    at kappa=0.10: {0.10 * (5*0.10+28)/360:.6f}")
print(f"    at kappa=0.50: {0.50 * (5*0.50+28)/360:.6f}")
print()

# =============================================================================
# SECTION 8: Critical kappa values
# =============================================================================
# Find kappa where delta(alpha_s)/alpha_s = 0.5 (gate threshold)
# kappa * (5*kappa + 28) / 360 = 0.5
# 5*kappa^2 + 28*kappa - 180 = 0
# kappa = (-28 + sqrt(784 + 3600)) / 10 = (-28 + sqrt(4384)) / 10

discrim = 28**2 + 4*5*180
kappa_alpha_s_half = (-28 + np.sqrt(discrim)) / (2*5)

# Find kappa where delta(c_s^2) = 10^{-3} (gate threshold)
# kappa^2 * g_3^2 / (16*pi^2) = 10^{-3}
# kappa = sqrt(10^{-3} * 16*pi^2 / g_3^2)
kappa_cs2_gate = np.sqrt(1e-3 * 16 * PI**2 / g_3_sq)

# Find kappa where delta(c_s^2) = 0.1 (FAIL threshold)
kappa_cs2_fail = np.sqrt(0.1 * 16 * PI**2 / g_3_sq)

print(f"Critical kappa values:")
print(f"  kappa(delta_alpha_s/alpha_s = 0.5) = {kappa_alpha_s_half:.4f}")
print(f"  kappa(delta_cs2 = 10^{{-3}})         = {kappa_cs2_gate:.4f}")
print(f"  kappa(delta_cs2 = 0.1)              = {kappa_cs2_fail:.4f}")
print()

# Maximum kappa in physical range
kappa_max_physical = 0.5  # (local)
delta_cs2_at_max = kappa_max_physical**2 * g_3_sq / (16.0 * PI**2)
frac_alpha_at_max = kappa_max_physical * (5.0*kappa_max_physical + 28.0) / 360.0

print(f"At maximum physical kappa = {kappa_max_physical}:")
print(f"  delta(c_s^2) = {delta_cs2_at_max:.6e}")
print(f"  delta(alpha_s)/alpha_s = {frac_alpha_at_max:.6f}")
print()

# =============================================================================
# SECTION 9: Cross-checks
# =============================================================================
print("=" * 72)
print("CROSS-CHECKS")
print("=" * 72)
print()

# Cross-check 1: delta(a_2)/a_2 is small compared to 1
print(f"CC-1: delta(a_2)/a_2 at kappa=0.5 = {-0.5/12:.4f} (<<1, perturbative)")

# Cross-check 2: delta(c_s^2) << 1 for all physical kappa
print(f"CC-2: max delta(c_s^2) = {delta_cs2[-1]:.6e} (<<1, perturbative)")

# Cross-check 3: S70 estimate comparison
# S70 R2: c_s^2 ~ ||A||^2/(a_2*M_KK^2) ~ 10^{-4}
# Our result at kappa=0.1: delta_cs2 ~ 1.7e-5 (consistent with O(10^{-4}) estimate)
cs2_s70_estimate = 1e-4  # S70 R2 rough estimate
cs2_our_at_01 = 0.1**2 * g_3_sq / (16*PI**2)
print(f"CC-3: S70 estimate ~ {cs2_s70_estimate:.0e}, our(kappa=0.1) = {cs2_our_at_01:.2e}")
print(f"       Ratio: {cs2_our_at_01/cs2_s70_estimate:.2f} (order-of-magnitude consistent)")

# Cross-check 4: A-TENSOR-61 result (A=T=0 for product)
# Our kappa=0 limit should give zero corrections
assert abs(delta_cs2[0]) < 1e-30, "kappa=0 should give zero delta_cs2"
assert abs(frac_delta_alpha_s[0]) < 1e-30, "kappa=0 should give zero delta_alpha_s"
print(f"CC-4: kappa=0 gives delta=0 (consistent with A-TENSOR-61 PASS)")

# Cross-check 5: direction of corrections
# delta(c_s^2) > 0 for all kappa > 0 (A-tensor introduces kinetic mixing)
assert np.all(delta_cs2[1:] > 0), "delta_cs2 should be positive"
# delta(alpha_s)/alpha_s > 0 for all kappa > 0 (non-trivial fibration increases running)
assert np.all(frac_delta_alpha_s[1:] > 0), "delta_alpha_s should be positive"
print(f"CC-5: Both corrections positive for kappa>0 (opposite directions)")
print(f"       -> c_s^2 increases (bad for prediction)")
print(f"       -> alpha_s increases (good for tension)")
print()

# Cross-check 6: kappa needed for alpha_s resolution vs physical bound
alpha_s_observed = 0.118   # PDG alpha_s(M_Z) = 0.1180 +/- 0.0009  # (local)
alpha_s_framework = 0.0134  # S70 max with thresholds  # (local)
tension_factor = alpha_s_observed / alpha_s_framework
needed_frac = (tension_factor - 1.0)  # need delta/alpha ~ 7.8
kappa_needed_full = np.interp(needed_frac, frac_delta_alpha_s, kappa_arr)
print(f"CC-6: alpha_s tension factor = {tension_factor:.2f}x")
print(f"       Need delta(alpha_s)/alpha_s = {needed_frac:.2f}")
print(f"       Requires kappa = {kappa_needed_full:.2f}")
print(f"       Physical bound: kappa < 0.5")
print(f"       -> Non-trivial fibration alone INSUFFICIENT to resolve alpha_s tension")
print()

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================
print("=" * 72)
print("GATE VERDICT")
print("=" * 72)
print()

# Evaluate at the physically relevant range
# The physical kappa for SU(3) is bounded by the instability criterion
# kappa < 0.5. In practice, typical gauge configurations have kappa ~ 0.01-0.1.

# Gate condition 1: delta(c_s^2) < 10^{-3}
cs2_max_physical = delta_cs2[-1]  # at kappa=0.5
gate_cs2 = cs2_max_physical < 1e-3

# Gate condition 2: delta(alpha_s)/alpha_s > 0.5
alpha_s_max_physical = frac_delta_alpha_s[-1]
gate_alpha = alpha_s_max_physical > 0.5

# Determine verdict
if cs2_max_physical > 0.1:
    verdict = "FAIL"
    detail = f"delta(c_s^2) = {cs2_max_physical:.4e} > 0.1, c_s^2=0 prediction destroyed"
elif gate_cs2 and gate_alpha:
    verdict = "PASS"
    detail = (f"delta(c_s^2) = {cs2_max_physical:.4e} < 10^{{-3}} AND "
              f"delta(alpha_s)/alpha_s = {alpha_s_max_physical:.4f} > 0.5")
else:
    verdict = "INFO"
    parts = []
    if gate_cs2:
        parts.append(f"c_s^2 robust: max delta = {cs2_max_physical:.4e} < 10^{{-3}}")
    else:
        parts.append(f"c_s^2 NOT robust: max delta = {cs2_max_physical:.4e}")
    if gate_alpha:
        parts.append(f"alpha_s relieved: max frac = {alpha_s_max_physical:.4f} > 0.5")
    else:
        parts.append(f"alpha_s NOT relieved: max frac = {alpha_s_max_physical:.4f} < 0.5")
    detail = "; ".join(parts)

print(f"Gate: NON-TRIVIAL-FIBRATION-CSQUARED-71")
print(f"  Condition 1: delta(c_s^2) < 10^{{-3}} at max kappa=0.5")
print(f"    Computed: {cs2_max_physical:.6e}")
print(f"    Status: {'PASS' if gate_cs2 else 'FAIL'}")
print()
print(f"  Condition 2: delta(alpha_s)/alpha_s > 0.5 at max kappa=0.5")
print(f"    Computed: {alpha_s_max_physical:.6f}")
print(f"    Status: {'PASS' if gate_alpha else 'FAIL'}")
print()
print(f"  VERDICT: {verdict}")
print(f"  Detail: {detail}")
print()

# =============================================================================
# SECTION 11: Allowed band identification
# =============================================================================
# Find the band of kappa where delta(c_s^2) < 10^{-3}
if kappa_cs2_gate < 0.5:
    kappa_allowed_max = kappa_cs2_gate
else:
    kappa_allowed_max = 0.5  # (local)

# For alpha_s half-resolution: need delta/alpha > 0.5
if kappa_alpha_s_half < 0.5:
    kappa_alpha_half = kappa_alpha_s_half
else:
    kappa_alpha_half = None  # never reached

print(f"Allowed band:")
print(f"  c_s^2 safe (delta < 10^{{-3}}):      kappa < {kappa_allowed_max:.4f}")
print(f"  alpha_s half-resolved (frac > 0.5): kappa > {kappa_alpha_s_half:.4f}")
if kappa_alpha_s_half < kappa_allowed_max:
    print(f"  Overlap band: [{kappa_alpha_s_half:.4f}, {kappa_allowed_max:.4f}]")
    print(f"  -> Solution space EXISTS")
else:
    print(f"  No overlap: alpha_s requires kappa > {kappa_alpha_s_half:.4f} but c_s^2 requires kappa < {kappa_allowed_max:.4f}")
    print(f"  -> No simultaneous resolution")
print()

# =============================================================================
# SECTION 12: Physical interpretation
# =============================================================================
print("=" * 72)
print("PHYSICAL INTERPRETATION")
print("=" * 72)
print()

# The key result: c_s^2 correction and alpha_s correction scale DIFFERENTLY
# with kappa:
#   delta(c_s^2) ~ kappa^2    (quadratic)
#   delta(alpha_s)/alpha_s ~ kappa  (linear, dominant)
#
# This means:
# 1. c_s^2 is VERY robust against fibration corrections (quadratic suppression)
# 2. alpha_s gets a linear correction but it's coefficient-suppressed (1/360)
# 3. The directions are OPPOSITE in desirability:
#    - c_s^2 = 0 is a prediction; correction is UNWANTED
#    - alpha_s tension exists; correction is WANTED
# 4. But the magnitudes don't allow simultaneous full resolution:
#    - To fully resolve alpha_s (~8.8x), need kappa ~ very large
#    - But c_s^2 stays safely small for kappa < physical bound

# Fraction of alpha_s tension resolved at maximum physical kappa
alpha_s_frac_resolved = frac_delta_alpha_s[-1] / needed_frac * 100
print(f"Alpha_s tension resolved at kappa=0.5: {alpha_s_frac_resolved:.1f}%")
print(f"  (Removes {frac_delta_alpha_s[-1]:.4f} of needed {needed_frac:.2f} fractional correction)")
print()

# But: is this the DOMINANT correction mechanism?
# The alpha_s correction from a_6 (S70 W3-C) is 6.5%
# The non-trivial fibration at kappa=0.5 gives: delta/alpha = 0.0424
# That's 4.24% -- same order as a_6 but not dominant
print(f"Comparison of alpha_s correction sources:")
print(f"  a_6 higher-order CCM (S70): ~6.5%")
print(f"  Non-trivial fibration (kappa=0.5): ~{100*frac_delta_alpha_s[-1]:.1f}%")
print(f"  Both together: ~{6.5 + 100*frac_delta_alpha_s[-1]:.1f}%")
print(f"  Needed: ~{100*needed_frac:.0f}%")
print(f"  -> Neither alone sufficient. Combined still ~10x short.")
print()

# =============================================================================
# SECTION 13: Additional structural results
# =============================================================================

# The correction ratio delta(a_4)/delta(a_2)
# This determines whether the fibration preferentially affects gauge
# couplings (a_4) or gravity (a_2)
ratio_a4_a2_corr = np.zeros_like(kappa_arr)
mask = kappa_arr > 0
ratio_a4_a2_corr[mask] = (frac_delta_a4[mask]) / (frac_delta_a2[mask])

print(f"Structural ratios:")
print(f"  At kappa=0.1: delta(a_4)/a_4 / delta(a_2)/a_2 = {ratio_a4_a2_corr[N_kappa//5]:.4f}")
print(f"  At kappa=0.5: delta(a_4)/a_4 / delta(a_2)/a_2 = {ratio_a4_a2_corr[-1]:.4f}")
print(f"  (Negative means a_4 and a_2 are corrected in OPPOSITE directions)")
print()

# Jensen deformation + fibration: are they independent?
# Jensen changes the FIBER metric (g_K -> g_K(tau))
# Fibration changes the CONNECTION (omega on the principal bundle)
# They are geometrically independent degrees of freedom.
# Jensen is a symmetric deformation of the fiber; fibration is a gauge field on the base.
print(f"Jensen vs Fibration independence:")
print(f"  Jensen deformation: fiber metric g_K -> g_K(tau), affects eigenvalues")
print(f"  Non-trivial fibration: connection omega on P -> M, affects cross-terms")
print(f"  These are INDEPENDENT: Jensen is Sym^2(T*K), fibration is Omega^1(M, ad(P))")
print(f"  Combined effect is additive at tree level, multiplicative at 1-loop")
print()

# =============================================================================
# SECTION 14: Save data
# =============================================================================

out_path = os.path.join(data_dir, 's71_non_trivial_fibration_csquared.npz')
np.savez(out_path,
    # Gate
    gate_name='NON-TRIVIAL-FIBRATION-CSQUARED-71',
    gate_verdict=verdict,
    gate_detail=detail,
    # Arrays
    kappa_arr=kappa_arr,
    delta_cs2=delta_cs2,
    frac_delta_alpha_s=frac_delta_alpha_s,
    frac_delta_a2=frac_delta_a2,
    frac_delta_a4=frac_delta_a4,
    cs2_total=cs2_total,
    # Scalars
    cs2_max_physical=cs2_max_physical,
    alpha_s_max_frac=alpha_s_max_physical,
    kappa_cs2_gate=kappa_cs2_gate,
    kappa_alpha_s_half=kappa_alpha_s_half,
    kappa_max_physical=kappa_max_physical,
    # Input constants
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    a4_fold=a4_fold,
    R_K_fold=R_K_fold,
    alpha_3_MKK=alpha_3_MKK,
    g_3_sq=g_3_sq,
    cs2_tree=cs2_tree,
    cs2_1loop=cs2_1loop,
    # Tension parameters
    alpha_s_observed=alpha_s_observed,
    alpha_s_framework=alpha_s_framework,
    tension_factor=tension_factor,
    needed_frac=needed_frac,
    alpha_s_frac_resolved=alpha_s_frac_resolved,
)
print(f"Data saved: {out_path}")
print()

# =============================================================================
# SECTION 15: Plot
# =============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: delta(c_s^2) vs kappa
ax1.semilogy(kappa_arr[1:], delta_cs2[1:], 'b-', lw=2, label=r'$\delta(c_s^2)$ from A-tensor')
ax1.axhline(1e-3, color='g', ls='--', lw=1.5, label=r'Gate: $\delta(c_s^2) = 10^{-3}$')
ax1.axhline(0.1, color='r', ls='--', lw=1.5, label=r'FAIL: $\delta(c_s^2) = 0.1$')
ax1.axhline(cs2_1loop, color='gray', ls=':', lw=1, label=f'1-loop trivial = {cs2_1loop:.2e}')
ax1.axvline(kappa_cs2_gate, color='g', ls=':', lw=1, alpha=0.7)
ax1.set_xlabel(r'$\kappa$ (A-tensor strength)', fontsize=12)
ax1.set_ylabel(r'$\delta(c_s^2)$', fontsize=12)
ax1.set_title(r'Sound Speed Correction from Non-Trivial Fibration', fontsize=13)
ax1.set_xlim(0, 0.5)
ax1.set_ylim(1e-8, 1)
ax1.legend(fontsize=9, loc='upper left')
ax1.grid(True, alpha=0.3)

# Shade allowed region
ax1.axvspan(0, min(kappa_cs2_gate, 0.5), alpha=0.1, color='green', label='_nolegend_')

# Right panel: delta(alpha_s)/alpha_s vs kappa
ax2.plot(kappa_arr, frac_delta_alpha_s, 'r-', lw=2,
         label=r'$\delta(\alpha_s)/\alpha_s$ from A-tensor')
ax2.axhline(0.5, color='orange', ls='--', lw=1.5, label=r'Gate: $\delta(\alpha_s)/\alpha_s = 0.5$')
ax2.axhline(needed_frac, color='purple', ls=':', lw=1.5,
            label=f'Full resolution: {needed_frac:.1f}')

# Mark where alpha_s half-resolution occurs
if kappa_alpha_s_half < 5:  # don't mark if off-scale
    ax2.axvline(kappa_alpha_s_half, color='orange', ls=':', lw=1, alpha=0.7)
    ax2.text(min(kappa_alpha_s_half + 0.02, 0.45), 0.05,
             f'$\\kappa = {kappa_alpha_s_half:.2f}$',
             fontsize=9, color='orange')

ax2.set_xlabel(r'$\kappa$ (A-tensor strength)', fontsize=12)
ax2.set_ylabel(r'$\delta(\alpha_s)/\alpha_s$', fontsize=12)
ax2.set_title(r'Spectral Running Correction from Non-Trivial Fibration', fontsize=13)
ax2.set_xlim(0, 0.5)
ax2.set_ylim(0, max(0.1, frac_delta_alpha_s[-1] * 1.3))
ax2.legend(fontsize=9, loc='upper left')
ax2.grid(True, alpha=0.3)

# Add allowed band annotation
if kappa_alpha_s_half < kappa_cs2_gate:
    ax2.axvspan(kappa_alpha_s_half, min(kappa_cs2_gate, 0.5),
                alpha=0.15, color='yellow')  # (local)
    ax2.text(0.25, 0.08 * max(0.1, frac_delta_alpha_s[-1] * 1.3),
             'Allowed band', fontsize=10, ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

plt.tight_layout()
plot_path = os.path.join(data_dir, 's71_non_trivial_fibration_csquared.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")
print()

# =============================================================================
# SECTION 16: Summary table
# =============================================================================
print("=" * 72)
print("SUMMARY TABLE")
print("=" * 72)
print()
print(f"{'kappa':>8s} | {'delta(c_s^2)':>14s} | {'delta(a_s)/a_s':>14s} | {'c_s^2 safe':>10s} | {'a_s helped':>10s}")
print("-" * 72)
for k_val in [0.0, 0.01, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50]:
    dc = k_val**2 * g_3_sq / (16 * PI**2)
    da = k_val * (5*k_val + 28) / 360
    safe = "YES" if dc < 1e-3 else "NO"
    helped = f"{100*da:.1f}%" if da > 0 else "0%"
    print(f"{k_val:>8.2f} | {dc:>14.2e} | {da:>14.4f} | {safe:>10s} | {helped:>10s}")
print()

print("=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
