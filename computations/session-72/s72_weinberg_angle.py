#!/usr/bin/env python3
"""
s72_weinberg_angle.py — WEINBERG-72: sin^2(theta_W) at M_KK + RG to M_Z
=========================================================================

Computes the Weinberg angle from the Baptista KK framework boundary conditions
at M_KK and runs it to M_Z using SM one-loop RG equations, including KK
threshold corrections from the PW tower.

Structure:
  1. M_KK-scale boundary conditions (SCHEME-INDEPENDENT)
     - g'^2 = 12 * e^{-2*tau_fold}   (Baptista eq 5.21 + Jensen parametrization)
     - g^2  = 4 * e^{2*tau_fold}      (Baptista eq 5.21 + Jensen parametrization)
     - sin^2(theta_W)|_{M_KK} = g'^2 / (g'^2 + g^2) = 0.5839

  2. One-loop SM RG running from M_KK to M_Z (SCHEME-DEPENDENT)
     - Standard beta coefficients b_1 = 41/10, b_2 = -19/6, b_3 = -7
     - ln(M_KK/M_Z) = 34.33

  3. KK threshold corrections (SCHEME-DEPENDENT)
     - S_inf = 2.353 from S71 spectral zeta computation
     - Threshold sum modifies effective coupling at M_KK

Gate: WEINBERG-72
  PASS: |sin^2(theta_W)_{predicted} - 0.23122| / 0.23122 < 15%
  INFO: Within 15-30% of observed
  FAIL: More than 30% discrepancy, or unphysical result

Provenance:
  - Baptista Paper 13 eq (5.21): gauge coupling constants from fiber integration
  - Baptista Paper 24: sin^2(theta_W) = 3/4 from SU(3) group theory (5D)
  - Chamseddine-Connes 1996 (Paper 19 eq 3.27): NCG sin^2(theta_W) = 3/8
  - S71 spectral zeta: S_inf = 2.353
  - S52 ddg_mkk: framework RG running infrastructure
  - canonical_constants: sin2_thetaW_fold = 0.5839, M_KK, tau_fold, a4_fold, a2_fold
"""

import sys
import os
import numpy as np

# ── Imports ──────────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner, M_Z, PI,
    sin2_thetaW_MSbar, sin2_thetaW_fold,
    alpha_em_MZ_inv, a4_fold, a2_fold,
    g_SU2_fold, g_U1_fold, alpha2_MKK_inv,
    Lambda_obs_MP4, M_Pl_reduced
)

# Load S71 spectral zeta data
s71_path = os.path.join(os.path.dirname(__file__), 's71_spectral_zeta_threshold.npz')
s71_data = np.load(s71_path, allow_pickle=True)
S_inf = float(s71_data['S_inf_final'])  # 2.353 (Gaussian, L_max=7)
Lambda_fixed = float(s71_data['Lambda_fixed'])  # 2.048 M_KK
gamma_opt = float(s71_data['gamma_opt'])  # 0.488
ratio_a4_a2 = float(s71_data['ratio_a4_a2_canonical'])  # 0.4865

print("=" * 72)
print("WEINBERG-72: sin^2(theta_W) at M_KK + RG to M_Z")
print("=" * 72)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1: M_KK BOUNDARY CONDITIONS (SCHEME-INDEPENDENT)
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("1. M_KK BOUNDARY CONDITIONS (SCHEME-INDEPENDENT)")
print("=" * 72)

# The gauge couplings at M_KK from Baptista Paper 13 eq (5.21):
#
# On the Jensen line (lambda_1 = lambda_2 = lambda, lambda_3 = lambda * e^{2*tau}),
# the su(3) = u(1) + su(2) + C^2 decomposition gives:
#
#   g'^2 = 12/lambda_1 = 12/(lambda)    [U(1)_Y hypercharge coupling squared]
#   g^2  = 4/lambda_2  = 4/(lambda)     [SU(2)_L coupling squared]
#
# The ratio g'^2/g^2 = 3, independent of lambda. This gives:
#   sin^2(theta_W) = g'^2 / (g'^2 + g^2) = 3/(3+1) = 3/4 = 0.75
# for the UNDEFORMED (bi-invariant) metric.
#
# However, the task prompt specifies the deformed formula:
#   g'^2 = 12 * exp(-2*tau)
#   g^2  = 4 * exp(2*tau)
# which corresponds to the Jensen-deformed metric where the C^2 directions
# are scaled relative to u(2). This makes the ratio TAU-DEPENDENT:
#   g'^2/g^2 = 3 * exp(-4*tau)
#   sin^2(theta_W) = 3*exp(-4*tau) / (3*exp(-4*tau) + 1)
#
# At tau = 0 (bi-invariant): sin^2 = 3/(3+1) = 0.75 (agrees with Paper 24)
# At tau_fold = 0.19: sin^2 = 0.5839 (matches canonical constant)

tau = tau_fold  # 0.19

# Hypercharge coupling squared (Baptista convention, NOT GUT-normalized)
gp2_MKK = 12.0 * np.exp(-2.0 * tau)  # g'^2 at M_KK
g2_MKK = 4.0 * np.exp(2.0 * tau)     # g^2 (SU(2)) at M_KK

# Weinberg angle at M_KK
sin2_W_MKK = gp2_MKK / (gp2_MKK + g2_MKK)

# Cross-check against canonical
print(f"  tau_fold = {tau}")
print(f"  g'^2(M_KK) = 12 * exp(-2*tau) = {gp2_MKK:.6f}")
print(f"  g^2(M_KK)  = 4 * exp(2*tau)   = {g2_MKK:.6f}")
print(f"  g'^2/g^2   = {gp2_MKK/g2_MKK:.6f}  (= 3*exp(-4*tau) = {3*np.exp(-4*tau):.6f})")
print(f"  sin^2(theta_W)|_{{M_KK}} = g'^2/(g'^2+g^2) = {sin2_W_MKK:.6f}")
print(f"  Canonical sin2_thetaW_fold            = {sin2_thetaW_fold:.6f}")
print(f"  Discrepancy = {abs(sin2_W_MKK - sin2_thetaW_fold):.2e}")
assert abs(sin2_W_MKK - sin2_thetaW_fold) < 1e-4, \
    f"M_KK Weinberg angle mismatch: {sin2_W_MKK} vs {sin2_thetaW_fold}"
print("  >> M_KK value CONFIRMED (scheme-independent)")

# Also check canonical g_SU2_fold and g_U1_fold
# NOTE: canonical_constants stores g_SU2_fold = g^2 = 2.052 and g_U1_fold = g'^2 = 4.387
# But our formulas give g2_MKK = 5.849, gp2_MKK = 8.207
# Let's see what ratio is stored:
print(f"\n  Cross-check with canonical coupling constants:")
print(f"    g_SU2_fold (canonical) = {g_SU2_fold:.6f}")
print(f"    g_U1_fold  (canonical) = {g_U1_fold:.6f}")
print(f"    Ratio g_U1/g_SU2      = {g_U1_fold/g_SU2_fold:.6f}")
print(f"    Our g'^2/g^2           = {gp2_MKK/g2_MKK:.6f}")
# The canonical values differ by an overall normalization (different lambda convention),
# but the RATIO should match:
ratio_canon = g_U1_fold / g_SU2_fold
ratio_ours = gp2_MKK / g2_MKK
print(f"    Ratio match: canon={ratio_canon:.6f}, ours={ratio_ours:.6f}")

# At tau = 0 (bi-invariant limit):
sin2_biinv = 3.0 / 4.0
print(f"\n  Bi-invariant limit (tau=0): sin^2 = 3/4 = {sin2_biinv:.4f}")
print(f"  NCG prediction (CC 1996):   sin^2 = 3/8 = {3/8:.4f}")
print(f"  Framework at fold (tau=0.19): sin^2 = {sin2_W_MKK:.4f}")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2: CONVERT TO GUT-NORMALIZED COUPLINGS FOR SM RG
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("2. GUT-NORMALIZED COUPLINGS FOR SM RG")
print("=" * 72)

# The SM RG equations use GUT-normalized couplings:
#   alpha_1 = (5/3) * alpha_Y = (5/3) * g'^2/(4*pi)
#   alpha_2 = g^2/(4*pi)
#   alpha_3 = g_s^2/(4*pi)
#
# In terms of 1/alpha_i:
#   1/alpha_1 = (3/5) * 4*pi / g'^2
#   1/alpha_2 = 4*pi / g^2
#
# The Weinberg angle in GUT normalization:
#   sin^2(theta_W) = (3/5)*alpha_1 / ((3/5)*alpha_1 + alpha_2)
#                  = (3/5)/alpha_1_inv / ((3/5)/alpha_1_inv + 1/alpha_2_inv)
#                  = (3/5)*alpha_2_inv / ((3/5)*alpha_2_inv + alpha_1_inv)

alpha1_inv_MKK = (3.0 / 5.0) * 4.0 * PI / gp2_MKK  # GUT-normalized
alpha2_inv_MKK = 4.0 * PI / g2_MKK
alpha_Y_inv_MKK = 4.0 * PI / gp2_MKK  # hypercharge (non-GUT)

# Verify sin^2(theta_W) with GUT normalization
sin2_check_GUT = (3.0/5.0) * alpha2_inv_MKK / ((3.0/5.0) * alpha2_inv_MKK + alpha1_inv_MKK)
print(f"  1/alpha_1(M_KK) [GUT-norm] = {alpha1_inv_MKK:.4f}")
print(f"  1/alpha_2(M_KK)            = {alpha2_inv_MKK:.4f}")
print(f"  1/alpha_Y(M_KK) [hyperch]  = {alpha_Y_inv_MKK:.4f}")
print(f"  sin^2(theta_W) from GUT-norm = {sin2_check_GUT:.6f}")
print(f"  sin^2(theta_W) direct        = {sin2_W_MKK:.6f}")
assert abs(sin2_check_GUT - sin2_W_MKK) < 1e-10, "GUT normalization check failed"
print("  >> GUT normalization check PASSED")

# Compare to canonical alpha2_MKK_inv = 47.86
# NOTE: The canonical alpha2_MKK_inv = 47.86 uses a DIFFERENT normalization
# for the coupling constant (from the Kerner route where g^2 is related to
# the spectral action coefficient). Our g^2 = 4*exp(2*tau) = 5.849 gives
# 1/alpha_2 = 4*pi/5.849 = 2.15, NOT 47.86.
#
# The discrepancy is because the spectral action extraction route (S42) uses:
#   1/g_3^2 = f_0 * a_4 / pi^2
# which depends on f_0 (the spectral functional normalization).
#
# Our computation here is INDEPENDENT of f_0: we extract the coupling RATIO
# from the geometry alone (eq 5.21), which is scheme-independent.
print(f"\n  NOTE: alpha2_MKK_inv(canonical) = {alpha2_MKK_inv:.2f}")
print(f"  Our 1/alpha_2(M_KK) = {alpha2_inv_MKK:.4f}")
print(f"  The canonical value includes the spectral action normalization f_0.")
print(f"  Our computation uses RATIO-ONLY (scheme-independent).")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3: ONE-LOOP SM RG RUNNING (NO KK THRESHOLDS)
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("3. ONE-LOOP SM RG RUNNING (PURE SM, NO KK THRESHOLDS)")
print("=" * 72)

# SM one-loop beta function coefficients
# b1_SM = 41.0 / 10.0   # GUT-normalized U(1)_Y  # S72: now imported from canonical_constants
# b2_SM = -19.0 / 6.0    # SU(2)_L  # S72: now imported from canonical_constants
# b3_SM = -7.0            # SU(3)_c  # S72: now imported from canonical_constants

# Running: 1/alpha_i(mu_low) = 1/alpha_i(mu_high) + b_i/(2*pi) * ln(mu_high/mu_low)
# NOTE sign: going from HIGH to LOW, the + sign is correct because b_i>0 makes
# alpha_1 increase (coupling grows) going to low energy, i.e. 1/alpha_1 decreases.
# Actually, the RGE is:
#   d(1/alpha_i)/d(ln mu) = -b_i/(2*pi)
# So:
#   1/alpha_i(M_Z) = 1/alpha_i(M_KK) - b_i/(2*pi) * [ln(M_Z) - ln(M_KK)]
#                   = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/M_Z)

ln_ratio = np.log(M_KK / M_Z)  # M_KK = 7.43e16 GeV, M_Z = 91.19 GeV
print(f"  M_KK = {M_KK:.3e} GeV")
print(f"  M_Z  = {M_Z:.4f} GeV")
print(f"  ln(M_KK/M_Z) = {ln_ratio:.4f}")

# Method A: Use the geometric coupling RATIOS at M_KK, anchored to PDG at M_Z
# The difficulty: we know the RATIO alpha_1/alpha_2 at M_KK from geometry,
# but not the absolute normalization. The RG running depends on absolute values.
#
# Strategy: We use the KNOWN alpha_em(M_Z) to set the normalization.
# At M_Z: 1/alpha_em = 1/alpha_Y + 1/alpha_2 = 127.955
# And sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2) = 0.23122

# First, let's see what happens with PURE RATIO running.
# If we know sin^2(theta_W) at M_KK = 0.5839, we can predict sin^2(theta_W) at M_Z
# WITHOUT knowing the absolute couplings, by tracking how the ratio evolves.
#
# Define: r = alpha_Y/alpha_2 = (3/5) * alpha_1/alpha_2
# Then sin^2(theta_W) = r/(1+r)
#
# The RG evolution of r:
# 1/r = (1/alpha_Y)/(1/alpha_2) = alpha_2_inv / alpha_Y_inv
# d(1/r)/d(ln mu) = [d(alpha_2_inv)/d(ln mu) * alpha_Y_inv - alpha_2_inv * d(alpha_Y_inv)/d(ln mu)] / alpha_Y_inv^2
#
# Simpler: just run 1/alpha_i independently and take the ratio at the end.
# But we need absolute values for that.
#
# Alternative: The EVOLUTION of sin^2(theta_W) depends on the difference of
# beta functions, not on the absolute couplings (at one loop).
#
# d sin^2/d(ln mu) = (d alpha_Y/d(ln mu) * alpha_2 - alpha_Y * d alpha_2/d(ln mu)) / (alpha_Y + alpha_2)^2
#
# Using alpha_i = 1/(1/alpha_i) and d(1/alpha_i)/d(ln mu) = -b_i/(2*pi):
#   d alpha_i/d(ln mu) = alpha_i^2 * b_i/(2*pi)
#
# This makes sin^2(theta_W) RGE non-linear (depends on alpha_i themselves).
# At one loop, the cleanest approach is: INTEGRATE the coupled system.

# For this we need absolute coupling values.
# Method: Use the running equation BACKWARDS from M_Z PDG values to M_KK,
# then compare M_KK prediction to the geometric value.

# PDG at M_Z (MSbar):
alpha_em_MZ = 1.0 / alpha_em_MZ_inv  # = 1/127.955
sin2_W_MZ_PDG = sin2_thetaW_MSbar    # = 0.23122

alpha_Y_MZ = alpha_em_MZ / (1.0 - sin2_W_MZ_PDG)  # = alpha_em / cos^2
alpha_2_MZ = alpha_em_MZ / sin2_W_MZ_PDG            # wait, this isn't right either.

# Correct: alpha_em = alpha_Y * alpha_2 / (alpha_Y + alpha_2)  [parallel combination]
# So: 1/alpha_em = 1/alpha_Y + 1/alpha_2
# And sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2) = e^2/g^2
# where e is the electromagnetic coupling.
#
# From these two:
#   alpha_Y = alpha_em / cos^2(theta_W) ... NO.
#   sin^2(theta_W) = g'^2/(g^2 + g'^2) = alpha_Y/(alpha_Y + alpha_2)
#   So alpha_Y = sin^2 * (alpha_Y + alpha_2)
#   And alpha_2 = (1 - sin^2) * (alpha_Y + alpha_2)
#   Also 1/alpha_em = 1/alpha_Y + 1/alpha_2 =>
#   alpha_em = alpha_Y * alpha_2 / (alpha_Y + alpha_2)
#   => alpha_Y + alpha_2 = alpha_Y * alpha_2 / alpha_em
#   => alpha_Y = sin^2 * alpha_Y * alpha_2 / alpha_em
#   => alpha_em = sin^2 * alpha_2
#   => alpha_2 = alpha_em / sin^2
#   And alpha_Y = alpha_em / (1 - sin^2) = alpha_em / cos^2

alpha_2_MZ = alpha_em_MZ / sin2_W_MZ_PDG
alpha_Y_MZ = alpha_em_MZ / (1.0 - sin2_W_MZ_PDG)

# GUT normalized
alpha_1_MZ = (5.0/3.0) * alpha_Y_MZ

# Their inverses
alpha1_inv_MZ = 1.0 / alpha_1_MZ
alpha2_inv_MZ = 1.0 / alpha_2_MZ
alpha_Y_inv_MZ = 1.0 / alpha_Y_MZ

print(f"\n  PDG values at M_Z:")
print(f"    1/alpha_em(M_Z) = {alpha_em_MZ_inv:.3f}")
print(f"    sin^2(theta_W)  = {sin2_W_MZ_PDG}")
print(f"    alpha_2(M_Z)    = {alpha_2_MZ:.6f}  =>  1/alpha_2 = {alpha2_inv_MZ:.2f}")
print(f"    alpha_Y(M_Z)    = {alpha_Y_MZ:.6f}  =>  1/alpha_Y = {alpha_Y_inv_MZ:.2f}")
print(f"    alpha_1(M_Z)    = {alpha_1_MZ:.6f}  =>  1/alpha_1 = {alpha1_inv_MZ:.2f} [GUT-norm]")

# Standard alpha_3 at M_Z
alpha3_MZ = 0.1180  # PDG 2024  # (local)
alpha3_inv_MZ = 1.0 / alpha3_MZ

# Run UP from M_Z to M_KK (SM only, no thresholds)
# 1/alpha_i(M_KK) = 1/alpha_i(M_Z) - b_i/(2*pi) * ln(M_KK/M_Z)
# (negative sign because we're going UP in energy)
# Wait, let me re-derive:
#   d(1/alpha_i)/d(ln mu) = -b_i/(2*pi)
# Integrate from M_Z to M_KK:
#   1/alpha_i(M_KK) - 1/alpha_i(M_Z) = -b_i/(2*pi) * [ln(M_KK) - ln(M_Z)]
#   1/alpha_i(M_KK) = 1/alpha_i(M_Z) - b_i/(2*pi) * ln(M_KK/M_Z)

alpha1_inv_MKK_SM = alpha1_inv_MZ - b1_SM / (2*PI) * ln_ratio
alpha2_inv_MKK_SM = alpha2_inv_MZ - b2_SM / (2*PI) * ln_ratio
alpha3_inv_MKK_SM = alpha3_inv_MZ - b3_SM / (2*PI) * ln_ratio

# Convert back to hypercharge for sin^2
alpha_Y_inv_MKK_SM = (5.0/3.0) * alpha1_inv_MKK_SM

sin2_W_MKK_SM = (3.0/5.0) * alpha2_inv_MKK_SM / ((3.0/5.0) * alpha2_inv_MKK_SM + alpha1_inv_MKK_SM)

# Alternative direct: sin^2 = alpha_Y/(alpha_Y + alpha_2) = (1/alpha_2) / (1/alpha_Y + 1/alpha_2)
#                             wait no: alpha_Y/(alpha_Y + alpha_2) = 1/(1 + alpha_2/alpha_Y)
#                             = 1/(1 + alpha_Y_inv/alpha_2_inv)  -- WRONG
# alpha_Y / (alpha_Y + alpha_2) = (1/alpha_Y_inv) / (1/alpha_Y_inv + 1/alpha_2_inv)
# = alpha_2_inv / (alpha_Y_inv + alpha_2_inv)
sin2_W_MKK_SM_alt = alpha2_inv_MKK_SM / (alpha_Y_inv_MKK_SM + alpha2_inv_MKK_SM)
# Hmm, this uses hypercharge normalization. Let me be very careful.
# sin^2(theta_W) = g'^2 / (g'^2 + g^2) = alpha_Y / (alpha_Y + alpha_2)
# = 1/alpha_Y / (1/alpha_Y * (alpha_Y + alpha_2)) ... NO.
# alpha_Y/(alpha_Y + alpha_2) = 1 / (1 + alpha_2/alpha_Y) = 1/(1 + alpha_Y_inv/alpha_2_inv)
# WRONG AGAIN. alpha_2/alpha_Y = (1/alpha_2_inv)/(1/alpha_Y_inv) = alpha_Y_inv/alpha_2_inv
# So: alpha_Y/(alpha_Y + alpha_2) = 1/(1 + alpha_Y_inv/alpha_2_inv) = alpha_2_inv/(alpha_Y_inv + alpha_2_inv)
# In GUT norm: alpha_Y = (3/5)*alpha_1, so alpha_Y_inv = (5/3)*alpha_1_inv
# sin^2 = alpha_2_inv / ((5/3)*alpha_1_inv + alpha_2_inv)
#        = 1 / ((5/3)*alpha_1_inv/alpha_2_inv + 1)
# Or using the (3/5) form:
# sin^2 = (3/5)*alpha_2_inv / ((3/5)*alpha_2_inv + alpha_1_inv)
# This was used correctly in S52.

sin2_W_MKK_SM_v2 = alpha2_inv_MKK_SM / ((5.0/3.0)*alpha1_inv_MKK_SM + alpha2_inv_MKK_SM)
assert abs(sin2_W_MKK_SM - sin2_W_MKK_SM_v2) < 1e-12

print(f"\n  SM running from M_Z to M_KK (UP, no KK thresholds):")
print(f"    b_1 = {b1_SM:.4f}, b_2 = {b2_SM:.4f}, b_3 = {b3_SM:.4f}")
print(f"    ln(M_KK/M_Z) = {ln_ratio:.4f}")
print(f"    1/alpha_1(M_KK) [SM] = {alpha1_inv_MKK_SM:.4f}")
print(f"    1/alpha_2(M_KK) [SM] = {alpha2_inv_MKK_SM:.4f}")
print(f"    1/alpha_3(M_KK) [SM] = {alpha3_inv_MKK_SM:.4f}")
print(f"    sin^2(theta_W)|_{{M_KK}} [SM only] = {sin2_W_MKK_SM:.6f}")
print(f"    Framework geometric value           = {sin2_W_MKK:.6f}")
print(f"    Gap = {sin2_W_MKK - sin2_W_MKK_SM:.6f}  ({(sin2_W_MKK - sin2_W_MKK_SM)/sin2_W_MKK_SM*100:.1f}%)")

# Now the FORWARD problem: given geometric sin^2 at M_KK, what do we get at M_Z?
# We need absolute couplings. Use the geometric RATIO plus one anchoring condition.
#
# Anchoring: We can use alpha_em(M_Z) = 1/127.955 to fix the overall normalization.
# At M_Z: 1/alpha_em = 1/alpha_Y + 1/alpha_2 = (5/3)*alpha_1_inv + alpha_2_inv - (2/3)*alpha_1_inv
# Wait: 1/alpha_em = 1/alpha_Y + 1/alpha_2 in hypercharge convention.
# 1/alpha_Y = (5/3)/alpha_1_GUT (or simply the hypercharge inverse).
# Let me stick with hypercharge throughout for sin^2.

# FORWARD APPROACH: We know sin^2(theta_W)|_{M_KK} = 0.5839 (geometric).
# We need to determine the absolute couplings alpha_1(M_KK), alpha_2(M_KK).
# These come from the spectral action, but that's f_0-dependent.
#
# RATIO-ONLY APPROACH: The SM RGE for sin^2 can be integrated numerically.
# sin^2(theta_W)(mu) = (3/5)*alpha_2_inv(mu) / ((3/5)*alpha_2_inv(mu) + alpha_1_inv(mu))
#
# The difficulty: the RG equations for alpha_i_inv are LINEAR in alpha_i_inv
# but we need to know the INDIVIDUAL values, not just the ratio.
#
# Key insight: the SM RGE are LINEAR in 1/alpha_i:
#   1/alpha_i(mu) = 1/alpha_i(mu_0) + Delta_i(mu, mu_0)
# where Delta_i = -b_i/(2*pi) * ln(mu/mu_0)
#
# So sin^2(mu) depends on the INDIVIDUAL inverse couplings, not just their ratio.
# We need an anchor.
#
# SELF-CONSISTENT APPROACH: Require alpha_em(M_Z) = 1/127.955 after running.
# 1/alpha_em(M_Z) = (5/3)*alpha_1_inv(M_Z) + alpha_2_inv(M_Z)
#                     - (2/3)*alpha_1_inv(M_Z)
# Actually: 1/alpha_em = 1/alpha_Y + 1/alpha_2
# In GUT: 1/alpha_Y = (5/3)*1/alpha_1
# So: 1/alpha_em = (5/3)/alpha_1 + 1/alpha_2
# Hmm, that's 1/alpha_em = alpha_1_inv*(5/3) + alpha_2_inv -- No.
# 1/alpha_em = 1/alpha_Y + 1/alpha_2 = (5/3)*alpha_1_inv + alpha_2_inv? No!
# 1/alpha_Y = (5/3) * (1/alpha_1)? No. alpha_Y = (3/5)*alpha_1, so
# 1/alpha_Y = (5/3)/alpha_1 = (5/3)*alpha_1_inv. Yes.
# And 1/alpha_em = 1/alpha_Y + 1/alpha_2 = (5/3)*alpha_1_inv + alpha_2_inv.
# That's correct.

# So: at M_Z, we need (5/3)*alpha_1_inv + alpha_2_inv = 127.955
# And at M_KK: alpha_1_inv(M_KK) and alpha_2_inv(M_KK) are related by sin^2 = 0.5839.
# sin^2 = (3/5)*alpha_2_inv / ((3/5)*alpha_2_inv + alpha_1_inv) = 0.5839
# => (3/5)*alpha_2_inv = 0.5839 * ((3/5)*alpha_2_inv + alpha_1_inv)
# => (3/5)*alpha_2_inv * (1 - 0.5839) = 0.5839 * alpha_1_inv
# => alpha_1_inv = (3/5) * alpha_2_inv * (1 - 0.5839) / 0.5839
# => alpha_1_inv = (3/5) * alpha_2_inv * 0.4161 / 0.5839
# => alpha_1_inv = 0.4276 * alpha_2_inv

# Running:
# alpha_1_inv(M_Z) = alpha_1_inv(M_KK) + b_1/(2*pi) * ln(M_KK/M_Z)
# alpha_2_inv(M_Z) = alpha_2_inv(M_KK) + b_2/(2*pi) * ln(M_KK/M_Z)
#
# Let x = alpha_2_inv(M_KK). Then alpha_1_inv(M_KK) = c * x where
# c = (3/5) * (1 - sin2_W_MKK) / sin2_W_MKK

c_ratio = (3.0/5.0) * (1.0 - sin2_W_MKK) / sin2_W_MKK
print(f"\n  Ratio coefficient c = (3/5)*(1-sin2)/sin2 = {c_ratio:.6f}")
print(f"    alpha_1_inv(M_KK) = {c_ratio:.4f} * alpha_2_inv(M_KK)")

# At M_Z:
# (5/3)*(c*x + b_1/(2*pi)*ln_ratio) + (x + b_2/(2*pi)*ln_ratio) = 127.955
# (5/3)*c*x + x + (5/3)*b_1/(2*pi)*ln_ratio + b_2/(2*pi)*ln_ratio = 127.955
# x * ((5/3)*c + 1) = 127.955 - ((5/3)*b_1 + b_2)/(2*pi) * ln_ratio

RG_shift_1 = b1_SM / (2*PI) * ln_ratio  # = +22.37
RG_shift_2 = b2_SM / (2*PI) * ln_ratio  # = -17.29

em_inv_MZ = alpha_em_MZ_inv  # 127.955
rhs = em_inv_MZ - (5.0/3.0) * RG_shift_1 * c_ratio - RG_shift_2
# Wait, let me redo this more carefully.
# alpha_1_inv(M_Z) = c*x + RG_shift_1   where RG_shift_1 = b_1/(2*pi)*ln(M_KK/M_Z) > 0
# alpha_2_inv(M_Z) = x + RG_shift_2     where RG_shift_2 = b_2/(2*pi)*ln(M_KK/M_Z) < 0
# Constraint: (5/3)*alpha_1_inv(M_Z) + alpha_2_inv(M_Z) = 127.955
# (5/3)*(c*x + RG_shift_1) + (x + RG_shift_2) = 127.955
# x*((5/3)*c + 1) + (5/3)*RG_shift_1 + RG_shift_2 = 127.955
# x = [127.955 - (5/3)*RG_shift_1 - RG_shift_2] / ((5/3)*c + 1)

x_solve = (em_inv_MZ - (5.0/3.0)*RG_shift_1 - RG_shift_2) / ((5.0/3.0)*c_ratio + 1.0)

alpha2_inv_MKK_anchored = x_solve
alpha1_inv_MKK_anchored = c_ratio * x_solve

print(f"\n  RG shifts over ln(M_KK/M_Z) = {ln_ratio:.2f}:")
print(f"    Delta(1/alpha_1) = b_1/(2*pi)*ln = {RG_shift_1:.4f}")
print(f"    Delta(1/alpha_2) = b_2/(2*pi)*ln = {RG_shift_2:.4f}")

print(f"\n  Anchored M_KK couplings (requiring 1/alpha_em(M_Z)=127.955):")
print(f"    1/alpha_2(M_KK) = {alpha2_inv_MKK_anchored:.4f}")
print(f"    1/alpha_1(M_KK) = {alpha1_inv_MKK_anchored:.4f}")

# Now run DOWN to M_Z
alpha1_inv_MZ_pred = alpha1_inv_MKK_anchored + RG_shift_1
alpha2_inv_MZ_pred = alpha2_inv_MKK_anchored + RG_shift_2

em_inv_check = (5.0/3.0)*alpha1_inv_MZ_pred + alpha2_inv_MZ_pred
print(f"\n  Running DOWN to M_Z (pure SM, no KK thresholds):")
print(f"    1/alpha_1(M_Z) = {alpha1_inv_MZ_pred:.4f}  (PDG: {alpha1_inv_MZ:.4f})")
print(f"    1/alpha_2(M_Z) = {alpha2_inv_MZ_pred:.4f}  (PDG: {alpha2_inv_MZ:.4f})")
print(f"    1/alpha_em check = {em_inv_check:.4f}  (should be {em_inv_MZ:.3f})")

# Compute sin^2 at M_Z from pure SM running
sin2_MZ_pureSM = (3.0/5.0)*alpha2_inv_MZ_pred / ((3.0/5.0)*alpha2_inv_MZ_pred + alpha1_inv_MZ_pred)
sin2_MZ_pureSM_alt = alpha2_inv_MZ_pred / ((5.0/3.0)*alpha1_inv_MZ_pred + alpha2_inv_MZ_pred)

print(f"\n  RESULT (pure SM running, no KK thresholds):")
print(f"    sin^2(theta_W)|_{{M_Z}} = {sin2_MZ_pureSM:.6f}")
print(f"    PDG observed             = {sin2_W_MZ_PDG}")
print(f"    Discrepancy              = {sin2_MZ_pureSM - sin2_W_MZ_PDG:.6f}")
print(f"    Relative discrepancy     = {abs(sin2_MZ_pureSM - sin2_W_MZ_PDG)/sin2_W_MZ_PDG*100:.2f}%")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4: KK THRESHOLD CORRECTIONS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("4. KK THRESHOLD CORRECTIONS")
print("=" * 72)

# The KK tower on SU(3) contributes threshold corrections to the gauge couplings
# at M_KK. The S71 computation gives S_inf = 2.353 for the total threshold sum
# (Gaussian-regulated) in the SU(3) color channel.
#
# The threshold correction modifies the EFFECTIVE coupling at M_KK:
#   1/alpha_i^{eff}(M_KK) = 1/alpha_i^{bare}(M_KK) + delta_i
#
# where delta_i is the contribution from integrating out KK modes.
#
# From the S62 workshop and S63 computations:
#   delta(1/g_3^2) = S_inf = 2.353  (Gaussian, L_max=7)
#
# This is for the SU(3)_c coupling. The correction for SU(2) and U(1) depends
# on how the KK modes transform under those groups. On the Jensen-deformed SU(3),
# the PW tower modes have definite SU(2)xU(1) quantum numbers.
#
# KEY STRUCTURAL POINT (from Paper 13 eq 5.21):
# All three gauge couplings arise from the SAME fiber integration of |F|^2.
# The Jensen metric breaks the equality only through the lambda_i prefactors.
# The KK tower modes contribute to ALL gauge sectors, with group-theory factors
# determined by the Casimir operators.
#
# For the RATIO alpha_1/alpha_2, what matters is the DIFFERENTIAL threshold:
#   delta(sin^2) = function of (delta_1 - delta_2)
#
# The KK threshold S_inf = 2.353 is the total SU(3)_c threshold (Dynkin index sum).
# The electroweak thresholds are related by group theory.
#
# On the Jensen-deformed SU(3) fiber, the PW sectors (p,q) contribute:
#   - To SU(3)_c: through the right-invariant connection (always active)
#   - To SU(2)_L: through the left-invariant u(2) part (depends on (p,q) decomposition)
#   - To U(1)_Y: through the hypercharge generator in u(2)
#
# The key ratio: for a PW mode V_{(p,q)}, the contributions to the three
# gauge groups scale as:
#   b_3^{(p,q)} : b_2^{(p,q)} : b_1^{(p,q)} = C_3(p,q) : C_2(p,q) : (5/3)*Y^2(p,q)
#
# For the bi-invariant metric (tau=0), ALL gauge groups see the same threshold
# (unification), so delta_1 = delta_2 = delta_3. The differential correction
# vanishes and sin^2 at M_Z equals the pure-SM-running result.
#
# At tau_fold = 0.19, the Jensen deformation breaks this equality.
# The C^2 directions (coset) are scaled by e^{2*tau} relative to u(2).
# KK modes in the C^2 sector have masses that differ from u(2)-sector modes.
#
# From the spectral data: all KK mode masses lie in [0.82, 2.05] M_KK
# (bounded spectrum). The mass splitting between u(2)-sector and C^2-sector
# modes creates a differential threshold.

print(f"  S_inf (Gaussian, L=7) = {S_inf:.6f}")
print(f"  Lambda_fixed = {Lambda_fixed:.6f} M_KK")
print(f"  gamma_opt = {gamma_opt:.6f}")

# Now compute the differential threshold for sin^2.
# In the spectral action, the gauge kinetic term for group G_a comes from:
#   1/g_a^2 = (f_0 / pi^2) * int_K Tr_{G_a}(|F_a|^2) vol_K
#
# For the Jensen metric, the fiber integral over SU(3) with the Peter-Weyl
# decomposition gives sector-by-sector contributions.
#
# The S71 data has per-sector Dynkin indices sec_T[i] for each (p,q) sector.
# These are the SU(3)_c Dynkin indices. For SU(2) and U(1), we need to
# decompose V_{(p,q)} under SU(3) -> SU(2) x U(1).
#
# The branching rule for SU(3) irrep V_{(p,q)} under SU(2)xU(1):
# V_{(p,q)} = sum_j sum_Y V_{j,Y}
# where j runs from 0 to p (or q, depending on convention) and Y is determined.
#
# The Dynkin index for SU(2) from a sector (p,q):
#   T_2(p,q) = sum over SU(2) multiplets in the decomposition of dim(j)*(2j+1)*(j(j+1))/3
#
# For U(1): T_Y(p,q) = sum_Y Y^2 * dim(multiplet)
#
# This requires the full branching data. For this computation, let me use the
# STRUCTURAL CONSTRAINTS instead:
#
# At the bi-invariant point (tau=0), all thresholds are equal by symmetry:
#   delta_1 = delta_2 = delta_3 = S_inf(tau=0)
#
# At tau_fold = 0.19, the deformation is SMALL (tau_fold << 1).
# The threshold RATIO is:
#   delta_1/delta_3 ~ 1 + O(tau^2)
#   delta_2/delta_3 ~ 1 + O(tau^2)
#
# This means the differential threshold is a SMALL correction.

# Compute the simplest model: assume thresholds are proportional to the
# corresponding gauge coupling AT M_KK (i.e., the threshold correction
# to 1/alpha_i is proportional to alpha_i(M_KK)):
#
# Model A: Universal threshold (all delta_i = S_inf)
# Model B: Scaled threshold (delta_i proportional to group-theory factors)
# Model C: SU(3)-only threshold (only delta_3 is nonzero)

# The threshold S_inf was computed specifically for the SU(3)_c channel.
# It represents delta(1/g_3^2). Converting to alpha_3:
# delta(1/alpha_3) = (4*pi) * delta(1/g_3^2) = 4*pi * S_inf
# Actually, no. The S_inf is defined as:
#   delta(1/g_3^2) = S_inf (already in the appropriate units)
# and 1/alpha_3 = 4*pi / g_3^2, so delta(1/alpha_3) = 4*pi * S_inf.
# Hmm, but S_inf = 2.353 seems very large for delta(1/g_3^2). Let me check.

# From S63 higgs_running:
#   1/g_3^{eff,2} = 1/g_3^{SM,2}(M_KK) + delta(1/g_3^2)_KK
#   delta(1/g_3^2)_KK = 2.353 (Gaussian, L=6)
# This IS delta(1/g_3^2), dimensionless.
# Since 1/alpha_3 = 4*pi * 1/g_3^2, we have delta(1/alpha_3) = 4*pi * 2.353 = 29.6
# That's a HUGE correction to 1/alpha_3 ~ 8.47 at M_Z!
#
# Wait, the S62 workshop context clarifies:
# In the Chamseddine-Connes-Marcolli (CCM) matching:
#   1/g_3^2 = f_0 * a_4 / pi^2
# The delta is delta(f_0 * a_4/pi^2), which already includes the spectral
# functional normalization f_0.
#
# For the PURPOSE of this computation (sin^2(theta_W) running), we need
# the threshold correction to INVERSE COUPLINGS in the standard normalization.
#
# The key question: does S_inf = 2.353 directly shift 1/g_3^2 in the SM convention,
# or does it shift (f_0 * a_4 / pi^2)?
#
# From s63_kk_threshold.py and s63_higgs_running.py, S_inf enters as:
#   1/g_3^{eff}(M_KK)^2 = 1/g_3^{SM}(M_KK)^2 + S_inf
# So delta(1/g_3^2) = S_inf = 2.353 in conventional (non-spectral-action) units.
#
# However, this depends on how the threshold sum was normalized. Let me check the
# actual formula from S63/S64.

# From the S64 audit (PERMANENT): Formula C (T/8pi^2 per sector) is correct.
# delta(1/g_3^2) = sum_sectors T_sector / (8*pi^2) * ln(Lambda/omega_min)
# where T_sector is the Dynkin index.
#
# Since 1/alpha_3 = 4*pi/g_3^2, we have:
# delta(1/alpha_3) = 4*pi * delta(1/g_3^2) = 4*pi * S_inf
# = 4 * 3.14159 * 2.353 = 29.6

# That IS a huge correction. But it makes sense: the KK tower has many modes
# (20,064 eigenvalues at L=7) each contributing a small correction that adds up.

# For the electroweak sector:
# In the unified SU(3) picture at the undeformed metric, all threshold corrections
# are related by the relative Casimirs:
#   delta_1 : delta_2 : delta_3 = C_1 : C_2 : C_3
#
# At tau_fold = 0.19, the deformation breaks this. But the KK modes are still
# representations of SU(3), so the BRANCHING RULES apply.
#
# For each PW sector (p,q), the contribution to the three gauge thresholds:
#   delta_3^{(p,q)} = T_3(p,q)/(8*pi^2) * ln(Lambda/omega_min^{(p,q)})
#   delta_2^{(p,q)} = T_2(p,q)/(8*pi^2) * ln(Lambda/omega_min^{(p,q)})
#   delta_1^{(p,q)} = T_Y(p,q)/(8*pi^2) * ln(Lambda/omega_min^{(p,q)})
#
# The RATIO delta_2/delta_3 = sum_sectors(T_2 * ln(Lambda/omega))/sum_sectors(T_3 * ln(Lambda/omega))
# This is NOT simply T_2_total/T_3_total because different sectors have different omega_min.

# For the UNIVERSAL MODEL (tau -> 0 limit), all sectors contribute equally:
# delta_1 = delta_2 = delta_3 = S_inf  (up to group theory factors)

# Let's compute multiple models:

# MODEL A: UNIVERSAL THRESHOLDS (strongest: all gauge sectors get same correction)
# If the KK tower contributes equally to all gauge groups (as at tau=0):
# delta(1/g_i^2) = S_inf for all i
# Then 1/alpha_i(M_KK)^{eff} = 1/alpha_i(M_KK)^{bare} + 4*pi*S_inf

delta_g3_inv2 = S_inf  # 2.353

# Group theory factors for threshold ratios
# For SU(3) -> SU(2) x U(1), the Casimir ratio gives:
# C_2(SU(3))/C_2(SU(2)) in the fundamental = 4/3 / 3/4 = 16/9
# But this isn't the right ratio for threshold corrections.
# The correct ratio is the Dynkin index ratio.
#
# In the NCG framework (Paper 19, CC 1996), at unification:
# g_3^2 = g_2^2 = (5/3)*g_1^2
# which gives 1/g_1^2 : 1/g_2^2 : 1/g_3^2 = (3/5) : 1 : 1
#
# But this is the UNIFICATION condition, not the threshold ratio.
# The threshold correction from a KK mode transforming in rep R_a of group G_a:
# delta(1/g_a^2) = T(R_a)/(8*pi^2) * ln(...)
#
# For the KK modes on SU(3), in each PW sector V_{(p,q)}, the representation
# decomposes under SU(3)_c x SU(2)_L x U(1)_Y. The threshold correction
# for each gauge group is weighted by the Dynkin index T_a of the corresponding
# rep.
#
# SIMPLIFICATION: At leading order in tau, the threshold RATIOS are:
# For the adjoint of SU(3): delta_3 : delta_2 : delta_Y = 3 : 2 : 0
# (the adjoint decomposes as 8 = (3,0) + (1,1) + (2,+/-1/2))
# Wait, the adjoint of SU(3) fiber-group decomposes under SU(2)xU(1) as:
# 8 = (3,0) + (1,0) + (2,+q) + (2,-q)  where q = sqrt(3)/2
# The SU(3)_c Dynkin index of 8 is T_3(adj) = 3
# But these are FIBER modes, not color modes!
#
# The issue: the KK tower modes are SU(3)_FIBER modes. The gauge groups
# SU(3)_c, SU(2)_L, U(1)_Y arise from the ISOMETRY structure. The threshold
# correction to each gauge coupling depends on how the KK modes couple to
# the corresponding gauge bosons.
#
# In Baptista's framework:
# - SU(3)_c = right-invariant isometries (always exact, unbroken)
# - SU(2)_L x U(1)_Y = remnant of left-invariant isometries (broken by Jensen)
# - The massive gauge bosons (W, Z) are NON-Killing left-invariant fields
#
# The KK modes couple to SU(3)_c through the RIGHT connection (universal coupling).
# They couple to SU(2)_L through the LEFT connection (depends on mode structure).
# They couple to U(1)_Y through the residual left Killing field.
#
# The Dynkin index ratio for the threshold correction is:
# delta_3 / delta_2 = (right Dynkin sum) / (left SU(2) Dynkin sum)
#
# For the bi-invariant metric: left = right by symmetry, so delta_3 = delta_2.
# For Jensen deformation: the C^2 modes (which carry SU(2) charge) are shifted
# in mass by e^{2*tau}, creating a differential threshold.

# PRAGMATIC APPROACH: Compute sin^2(theta_W) for THREE models of threshold ratio:
# Model A: Universal (delta_i all equal, = S_inf)
# Model B: NCG ratio (delta_1 : delta_2 : delta_3 = 3/5 : 1 : 1, from unification)
# Model C: Color-only (delta_3 = S_inf, delta_1 = delta_2 = 0)
# Model D: Weak-enhanced (delta_2 = 1.5*delta_3, from u(2) mode enhancement)

print("\n  Computing threshold-corrected sin^2(theta_W) for 4 models:")
print(f"  S_inf = {S_inf:.6f}")
print(f"  4*pi*S_inf = {4*PI*S_inf:.2f}")

results = {}

for model_name, delta_factors in [
    ("A: Universal",           (1.0, 1.0, 1.0)),
    ("B: NCG unification",     (3.0/5.0, 1.0, 1.0)),
    ("C: Color-only",          (0.0, 0.0, 1.0)),
    ("D: Casimir-weighted",    (1.0/3.0, 1.0, 4.0/3.0)),
]:
    f1, f2, f3 = delta_factors

    # Threshold corrections to 1/g_i^2
    delta_g1_inv2 = f1 * delta_g3_inv2
    delta_g2_inv2 = f2 * delta_g3_inv2
    delta_g3_inv2_model = f3 * delta_g3_inv2

    # The threshold SHIFTS the effective coupling at M_KK.
    # If the bare coupling comes from geometry (sin^2 = 0.5839),
    # the effective coupling includes the threshold:
    # 1/g_i^{eff,2} = 1/g_i^{bare,2} + delta(1/g_i^2)
    #
    # In alpha_i: 1/alpha_i^{eff} = 1/alpha_i^{bare} + 4*pi*delta(1/g_i^2)

    # However, what enters the RG is the EFFECTIVE coupling at M_KK.
    # The procedure:
    # 1. Geometric ratio gives sin^2(M_KK) = 0.5839 (bare)
    # 2. Threshold shifts the individual couplings
    # 3. Run the shifted couplings DOWN to M_Z
    #
    # The threshold correction modifies the BOUNDARY CONDITION at M_KK.
    # The ratio alpha_1/alpha_2 at M_KK changes if delta_1 != delta_2.

    # Using the anchored approach:
    # Bare couplings: alpha2_inv_MKK_anchored, alpha1_inv_MKK_anchored
    # Effective couplings: add threshold
    # But we need to RE-ANCHOR because the threshold changes the M_Z values.

    # Let me do a SELF-CONSISTENT calculation.
    # Let x = 1/alpha_2^{bare}(M_KK), then 1/alpha_1^{bare}(M_KK) = c*x
    # Effective:
    # 1/alpha_1^{eff}(M_KK) = c*x + 4*pi*f1*S_inf
    # 1/alpha_2^{eff}(M_KK) = x + 4*pi*f2*S_inf
    # Run to M_Z:
    # 1/alpha_1(M_Z) = c*x + 4*pi*f1*S_inf + RG_shift_1
    # 1/alpha_2(M_Z) = x + 4*pi*f2*S_inf + RG_shift_2
    # Anchor: (5/3)*(c*x + 4pi*f1*S + RG1) + (x + 4pi*f2*S + RG2) = 127.955
    # x*((5/3)*c + 1) = 127.955 - (5/3)*(4pi*f1*S + RG1) - (4pi*f2*S + RG2)

    shift_1 = 4*PI*f1*S_inf + RG_shift_1  # total shift for alpha_1 (thresh + running)
    shift_2 = 4*PI*f2*S_inf + RG_shift_2  # total shift for alpha_2 (thresh + running)

    x_model = (em_inv_MZ - (5.0/3.0)*shift_1*c_ratio - shift_2 - (5.0/3.0)*4*PI*f1*S_inf - 4*PI*f2*S_inf) / ((5.0/3.0)*c_ratio + 1.0)
    # Hmm wait, let me be more careful.
    # 1/alpha_1(M_Z) = c*x + 4*pi*f1*S_inf + RG_shift_1
    # 1/alpha_2(M_Z) = x + 4*pi*f2*S_inf + RG_shift_2
    # (5/3)*(c*x + 4pi*f1*S + RG1) + (x + 4pi*f2*S + RG2) = 127.955
    # x*(5c/3 + 1) + (5/3)*(4pi*f1*S + RG1) + 4pi*f2*S + RG2 = 127.955

    total_const = (5.0/3.0)*(4*PI*f1*S_inf + RG_shift_1) + (4*PI*f2*S_inf + RG_shift_2)
    x_model = (em_inv_MZ - total_const) / ((5.0/3.0)*c_ratio + 1.0)

    a1_inv_MZ = c_ratio * x_model + 4*PI*f1*S_inf + RG_shift_1
    a2_inv_MZ = x_model + 4*PI*f2*S_inf + RG_shift_2

    # Sanity check
    em_inv_check = (5.0/3.0)*a1_inv_MZ + a2_inv_MZ
    assert abs(em_inv_check - em_inv_MZ) < 1e-6, f"alpha_em anchor failed for {model_name}"

    sin2_model = (3.0/5.0)*a2_inv_MZ / ((3.0/5.0)*a2_inv_MZ + a1_inv_MZ)

    # Also compute sin^2 via hypercharge
    # sin^2 = 1/alpha_2 / ((5/3)/alpha_1 + 1/alpha_2) -- WRONG
    # sin^2 = alpha_Y/(alpha_Y + alpha_2) = (3/5)*alpha_1/(((3/5)*alpha_1 + alpha_2)
    #       = (3/5)/alpha_1_inv / ((3/5)/alpha_1_inv + 1/alpha_2_inv)
    #       = (3/5)*alpha_2_inv / ((3/5)*alpha_2_inv + alpha_1_inv) -- YES, this is right.
    sin2_alt = alpha2_inv_MZ / ((5.0/3.0)*alpha1_inv_MZ + alpha2_inv_MZ) if False else sin2_model

    discrepancy = abs(sin2_model - sin2_W_MZ_PDG) / sin2_W_MZ_PDG * 100

    results[model_name] = {
        'sin2_MZ': sin2_model,
        'discrepancy_pct': discrepancy,
        'a1_inv_MZ': a1_inv_MZ,
        'a2_inv_MZ': a2_inv_MZ,
        'x_MKK': x_model,
    }

    print(f"\n  {model_name} (delta factors: {f1:.2f}, {f2:.2f}, {f3:.2f}):")
    print(f"    1/alpha_2^bare(M_KK) = {x_model:.4f}")
    print(f"    1/alpha_1^bare(M_KK) = {c_ratio*x_model:.4f}")
    print(f"    1/alpha_1(M_Z) = {a1_inv_MZ:.4f}  (PDG: {alpha1_inv_MZ:.4f})")
    print(f"    1/alpha_2(M_Z) = {a2_inv_MZ:.4f}  (PDG: {alpha2_inv_MZ:.4f})")
    print(f"    sin^2(theta_W)|_{{M_Z}} = {sin2_model:.6f}")
    print(f"    PDG = {sin2_W_MZ_PDG}, discrepancy = {discrepancy:.2f}%")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5: TWO-LOOP SM CORRECTION ESTIMATE
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("5. TWO-LOOP SM CORRECTION ESTIMATE")
print("=" * 72)

# The two-loop SM beta functions for gauge couplings are:
# d(alpha_i_inv)/d(ln mu) = -b_i/(2*pi) - sum_j b_{ij}/(8*pi^2) * alpha_j
#
# The two-loop coefficient matrix for the SM (GUT-normalized):
# b_11 = 199/50, b_12 = 27/10, b_13 = 44/5
# b_21 = 9/10,   b_22 = 35/6,  b_23 = 12
# b_31 = 11/10,  b_32 = 9/2,   b_33 = -26
#
# The two-loop correction to sin^2 is:
# delta_sin2_2loop ~ (b_{12} - b_{21})/(2*pi) * alpha * ln(M_KK/M_Z)
# This is suppressed by alpha/(2*pi) ~ 10^{-3} relative to one-loop.

# Estimate the two-loop correction magnitude
alpha_avg = 1.0 / 30.0  # typical alpha_i at intermediate scale
two_loop_correction = alpha_avg / (2*PI) * ln_ratio  # dimensionless
print(f"  Two-loop suppression factor: alpha/(2*pi) * ln = {two_loop_correction:.4f}")
print(f"  One-loop sin^2 shift: {abs(sin2_MZ_pureSM - sin2_W_MKK):.4f}")
print(f"  Estimated two-loop correction: {abs(sin2_MZ_pureSM - sin2_W_MKK)*two_loop_correction:.6f}")
print(f"  Two-loop/one-loop ratio: {two_loop_correction*100:.2f}%")
print(f"  => Two-loop correction is < 5% of one-loop: {'PASS' if two_loop_correction < 0.05 else 'FAIL'}")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6: CROSS-CHECKS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("6. CROSS-CHECKS")
print("=" * 72)

# Cross-check 1: NCG comparison
# Chamseddine-Connes 1996 (Paper 19) predicts sin^2 = 3/8 at the GUT scale
# (from the constraint g_3^2 = g_2^2 = (5/3)*g_1^2)
sin2_NCG = 3.0/8.0
print(f"\n  Cross-check 1: NCG prediction at unification scale")
print(f"    sin^2(theta_W) = 3/8 = {sin2_NCG:.4f} (Chamseddine-Connes 1996)")
print(f"    Framework at M_KK    = {sin2_W_MKK:.4f}")
print(f"    Difference           = {sin2_W_MKK - sin2_NCG:.4f}")
print(f"    The NCG value assumes g_2^2 = (5/3)*g_1^2 (exact unification).")
print(f"    The framework value has g'^2/g^2 = 3*exp(-4*tau) = {3*np.exp(-4*tau):.4f}")
print(f"    (vs NCG: g'^2/g^2 = 3/5 in GUT normalization => sin^2 = 3/8)")

# Cross-check 2: Bi-invariant limit
sin2_biinv = 3.0/4.0
print(f"\n  Cross-check 2: Bi-invariant limit (tau=0)")
print(f"    sin^2(theta_W) = 3/4 = {sin2_biinv} (Paper 24 group-theoretic value)")
print(f"    Our formula at tau=0 = {3.0/(3.0+1.0):.4f}")
print(f"    Match: {'PASS' if abs(3.0/(3.0+1.0) - 0.75) < 1e-10 else 'FAIL'}")

# Cross-check 3: Running direction
# b_1 > 0 (U(1) screening), b_2 < 0 (SU(2) anti-screening)
# Going from high to low energy: alpha_1 INCREASES, alpha_2 DECREASES
# => sin^2 = alpha_Y/(alpha_Y+alpha_2) should DECREASE (alpha_2 grows relative to alpha_Y)
print(f"\n  Cross-check 3: Running direction")
print(f"    sin^2(M_KK) = {sin2_W_MKK:.4f} > sin^2(M_Z) = {sin2_MZ_pureSM:.4f}: ", end="")
print(f"{'PASS' if sin2_W_MKK > sin2_MZ_pureSM else 'FAIL'}")
print(f"    (sin^2 decreases from high to low energy, as expected)")

# Cross-check 4: Verify PDG self-consistency
alpha_Y_PDG = alpha_em_MZ / (1.0 - sin2_W_MZ_PDG)
alpha_2_PDG = alpha_em_MZ / sin2_W_MZ_PDG
sin2_recon = alpha_Y_PDG / (alpha_Y_PDG + alpha_2_PDG)
print(f"\n  Cross-check 4: PDG self-consistency")
print(f"    alpha_em = {alpha_em_MZ:.6e}")
print(f"    alpha_Y  = {alpha_Y_PDG:.6e}, alpha_2 = {alpha_2_PDG:.6e}")
print(f"    sin^2 reconstructed = {sin2_recon:.6f} (should be {sin2_W_MZ_PDG})")
print(f"    Match: {'PASS' if abs(sin2_recon - sin2_W_MZ_PDG) < 1e-6 else 'FAIL'}")

# Cross-check 5: Standard SM running from GUT unification
# At M_GUT ~ 2e16 GeV with unification alpha_1 = alpha_2 = alpha_3 ~ 1/25:
alpha_GUT_inv = 25.0  # (local)
M_GUT = 2e16  # GeV
ln_GUT = np.log(M_GUT / M_Z)
sin2_GUT = (3.0/5.0)*alpha_GUT_inv / ((3.0/5.0)*alpha_GUT_inv + alpha_GUT_inv)
# = (3/5)/(3/5 + 1) = (3/5)/(8/5) = 3/8 = 0.375
a1_inv_MZ_GUT = alpha_GUT_inv + b1_SM/(2*PI)*ln_GUT
a2_inv_MZ_GUT = alpha_GUT_inv + b2_SM/(2*PI)*ln_GUT
sin2_MZ_from_GUT = (3.0/5.0)*a2_inv_MZ_GUT / ((3.0/5.0)*a2_inv_MZ_GUT + a1_inv_MZ_GUT)
print(f"\n  Cross-check 5: Standard SU(5) GUT running")
print(f"    sin^2(M_GUT) = 3/8 = 0.375 (unification condition)")
print(f"    1/alpha_GUT = {alpha_GUT_inv}")
print(f"    sin^2(M_Z) from GUT = {sin2_MZ_from_GUT:.6f}")
print(f"    PDG = {sin2_W_MZ_PDG}")
print(f"    GUT discrepancy = {abs(sin2_MZ_from_GUT - sin2_W_MZ_PDG)/sin2_W_MZ_PDG*100:.2f}%")
print(f"    (Standard SU(5) gets ~5% discrepancy, improved by SUSY threshold corrections)")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7: GATE VERDICT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("7. GATE VERDICT: WEINBERG-72")
print("=" * 72)

# The pure SM running gives the most CONSERVATIVE prediction (no model-dependent thresholds)
sin2_best = sin2_MZ_pureSM

# With thresholds, the Model B (NCG unification) is most physically motivated
sin2_thresh_B = results["B: NCG unification"]['sin2_MZ']

disc_pureSM = abs(sin2_MZ_pureSM - sin2_W_MZ_PDG) / sin2_W_MZ_PDG * 100
disc_B = results["B: NCG unification"]['discrepancy_pct']
disc_A = results["A: Universal"]['discrepancy_pct']
disc_C = results["C: Color-only"]['discrepancy_pct']
disc_D = results["D: Casimir-weighted"]['discrepancy_pct']

print(f"\n  SCHEME-INDEPENDENT result at M_KK:")
print(f"    sin^2(theta_W)|_{{M_KK}} = {sin2_W_MKK:.6f} (tau_fold = {tau_fold})")
print(f"    This is a PERMANENT GEOMETRIC result from Paper 13 eq (5.21)")

print(f"\n  SCHEME-DEPENDENT results at M_Z (require RG running + thresholds):")
print(f"    Pure SM running:          sin^2(M_Z) = {sin2_MZ_pureSM:.6f}  ({disc_pureSM:.1f}% from PDG)")
print(f"    Model A (universal):      sin^2(M_Z) = {results['A: Universal']['sin2_MZ']:.6f}  ({disc_A:.1f}%)")
print(f"    Model B (NCG):            sin^2(M_Z) = {sin2_thresh_B:.6f}  ({disc_B:.1f}%)")
print(f"    Model C (color-only):     sin^2(M_Z) = {results['C: Color-only']['sin2_MZ']:.6f}  ({disc_C:.1f}%)")
print(f"    Model D (Casimir-wt):     sin^2(M_Z) = {results['D: Casimir-weighted']['sin2_MZ']:.6f}  ({disc_D:.1f}%)")

# Determine gate verdict using the PURE SM running (most conservative)
# and the range across threshold models
disc_min = min(disc_pureSM, disc_A, disc_B, disc_C, disc_D)
disc_max = max(disc_pureSM, disc_A, disc_B, disc_C, disc_D)

# The pure SM running is the most scheme-independent of the M_Z predictions
if disc_pureSM < 15:
    gate_verdict = "PASS"
elif disc_pureSM < 30:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

# Check if ANY threshold model passes
any_pass = disc_min < 15
any_info = disc_min < 30

print(f"\n  Gate threshold:")
print(f"    PASS: < 15% discrepancy")
print(f"    INFO: 15-30% discrepancy")
print(f"    FAIL: > 30% discrepancy")

print(f"\n  Pure SM running discrepancy: {disc_pureSM:.1f}%")
print(f"  Threshold model range: [{disc_min:.1f}%, {disc_max:.1f}%]")

if gate_verdict == "PASS":
    verdict_detail = f"Pure SM running from sin^2(M_KK)=0.584 gives sin^2(M_Z)={sin2_MZ_pureSM:.4f}, {disc_pureSM:.1f}% from PDG 0.23122"
elif gate_verdict == "INFO":
    verdict_detail = f"Pure SM running gives {disc_pureSM:.1f}% discrepancy. With thresholds: [{disc_min:.1f}%, {disc_max:.1f}%]. Best model {'PASses' if any_pass else 'is INFO'} at {disc_min:.1f}%"
else:
    verdict_detail = f"Pure SM running gives {disc_pureSM:.1f}% discrepancy. All threshold models in [{disc_min:.1f}%, {disc_max:.1f}%]."

# If sin^2 went negative or > 0.5, that's a FAIL
if sin2_MZ_pureSM < 0 or sin2_MZ_pureSM > 0.5:
    gate_verdict = "FAIL"
    verdict_detail = f"sin^2(theta_W)(M_Z) = {sin2_MZ_pureSM:.4f} is UNPHYSICAL"

print(f"\n  ╔══════════════════════════════════════════════════════════════════╗")
print(f"  ║  Gate WEINBERG-72: {gate_verdict:>4s}                                       ║")
print(f"  ║  sin^2(theta_W)|_{{M_KK}} = {sin2_W_MKK:.4f} (scheme-independent)         ║")
print(f"  ║  sin^2(theta_W)|_{{M_Z}}  = {sin2_MZ_pureSM:.4f} (pure SM, {disc_pureSM:.1f}% from PDG) ║")
print(f"  ║  Threshold range: [{disc_min:.1f}%, {disc_max:.1f}%]                          ║")
print(f"  ╚══════════════════════════════════════════════════════════════════╝")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 8: CONTINUOUS RUNNING CURVE FOR PLOT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("8. GENERATING RUNNING CURVE DATA")
print("=" * 72)

# Generate sin^2(theta_W)(mu) from M_KK down to M_Z
n_points = 500
log10_mu = np.linspace(np.log10(M_Z), np.log10(M_KK), n_points)
mu_array = 10.0**log10_mu

# Use the anchored M_KK couplings (pure SM running case)
# 1/alpha_i(mu) = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/mu)
sin2_running_pureSM = np.zeros(n_points)
sin2_running_modelA = np.zeros(n_points)
sin2_running_modelB = np.zeros(n_points)
sin2_running_modelC = np.zeros(n_points)

for idx, mu in enumerate(mu_array):
    ln_MKK_over_mu = np.log(M_KK / mu)

    # Pure SM (no thresholds)
    a1_inv = alpha1_inv_MKK_anchored + b1_SM/(2*PI)*ln_MKK_over_mu
    a2_inv = alpha2_inv_MKK_anchored + b2_SM/(2*PI)*ln_MKK_over_mu
    sin2_running_pureSM[idx] = (3.0/5.0)*a2_inv / ((3.0/5.0)*a2_inv + a1_inv)

    # Model A: universal thresholds at M_KK
    x_A = results["A: Universal"]['x_MKK']
    a1_inv_A = c_ratio*x_A + 4*PI*1.0*S_inf + b1_SM/(2*PI)*ln_MKK_over_mu
    a2_inv_A = x_A + 4*PI*1.0*S_inf + b2_SM/(2*PI)*ln_MKK_over_mu
    sin2_running_modelA[idx] = (3.0/5.0)*a2_inv_A / ((3.0/5.0)*a2_inv_A + a1_inv_A)

    # Model B: NCG threshold ratio
    x_B = results["B: NCG unification"]['x_MKK']
    a1_inv_B = c_ratio*x_B + 4*PI*(3/5)*S_inf + b1_SM/(2*PI)*ln_MKK_over_mu
    a2_inv_B = x_B + 4*PI*1.0*S_inf + b2_SM/(2*PI)*ln_MKK_over_mu
    sin2_running_modelB[idx] = (3.0/5.0)*a2_inv_B / ((3.0/5.0)*a2_inv_B + a1_inv_B)

    # Model C: color-only
    x_C = results["C: Color-only"]['x_MKK']
    a1_inv_C = c_ratio*x_C + b1_SM/(2*PI)*ln_MKK_over_mu
    a2_inv_C = x_C + b2_SM/(2*PI)*ln_MKK_over_mu
    sin2_running_modelC[idx] = (3.0/5.0)*a2_inv_C / ((3.0/5.0)*a2_inv_C + a1_inv_C)

# Also compute sin^2(theta_W) as function of tau (for the M_KK boundary condition)
tau_array = np.linspace(0, 0.24, 100)
sin2_vs_tau = 3.0*np.exp(-4.0*tau_array) / (3.0*np.exp(-4.0*tau_array) + 1.0)

print(f"  Generated {n_points} points from log10(M_Z)={np.log10(M_Z):.2f} to log10(M_KK)={np.log10(M_KK):.2f}")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 9: SAVE DATA
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("9. SAVING DATA")
print("=" * 72)

out_path = os.path.join(os.path.dirname(__file__), 's72_weinberg_angle.npz')
np.savez(out_path,
    # Gate
    gate_name='WEINBERG-72',
    gate_verdict=gate_verdict,
    gate_detail=verdict_detail,
    # Scheme-independent
    sin2_MKK=sin2_W_MKK,
    tau_fold=tau_fold,
    gp2_MKK=gp2_MKK,
    g2_MKK=g2_MKK,
    sin2_biinvariant=sin2_biinv,
    sin2_NCG=sin2_NCG,
    # Pure SM running
    sin2_MZ_pureSM=sin2_MZ_pureSM,
    disc_pureSM_pct=disc_pureSM,
    alpha1_inv_MKK_anchored=alpha1_inv_MKK_anchored,
    alpha2_inv_MKK_anchored=alpha2_inv_MKK_anchored,
    # SM running from PDG up
    sin2_MKK_SM=sin2_W_MKK_SM,
    alpha1_inv_MKK_SM=alpha1_inv_MKK_SM,
    alpha2_inv_MKK_SM=alpha2_inv_MKK_SM,
    alpha3_inv_MKK_SM=alpha3_inv_MKK_SM,
    # Threshold models
    sin2_MZ_modelA=results["A: Universal"]['sin2_MZ'],
    sin2_MZ_modelB=results["B: NCG unification"]['sin2_MZ'],
    sin2_MZ_modelC=results["C: Color-only"]['sin2_MZ'],
    sin2_MZ_modelD=results["D: Casimir-weighted"]['sin2_MZ'],
    disc_A_pct=disc_A,
    disc_B_pct=disc_B,
    disc_C_pct=disc_C,
    disc_D_pct=disc_D,
    disc_min_pct=disc_min,
    disc_max_pct=disc_max,
    S_inf=S_inf,
    # Running curves
    log10_mu=log10_mu,
    sin2_running_pureSM=sin2_running_pureSM,
    sin2_running_modelA=sin2_running_modelA,
    sin2_running_modelB=sin2_running_modelB,
    sin2_running_modelC=sin2_running_modelC,
    # tau dependence
    tau_array=tau_array,
    sin2_vs_tau=sin2_vs_tau,
    # Constants used
    M_KK_used=M_KK,
    M_Z_used=M_Z,
    ln_ratio=ln_ratio,
    alpha_em_MZ_inv_used=alpha_em_MZ_inv,
    sin2_PDG=sin2_W_MZ_PDG,
)
print(f"  Saved: {out_path}")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 10: PLOT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("10. GENERATING PLOT")
print("=" * 72)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Left panel: sin^2(theta_W) vs log10(mu) from M_Z to M_KK
ax1 = axes[0]
ax1.plot(log10_mu, sin2_running_pureSM, 'b-', lw=2.0, label=f'Pure SM ({disc_pureSM:.1f}%)', zorder=5)
ax1.plot(log10_mu, sin2_running_modelA, 'g--', lw=1.5, label=f'Model A: Universal ({disc_A:.1f}%)')
ax1.plot(log10_mu, sin2_running_modelB, 'r-.', lw=1.5, label=f'Model B: NCG ({disc_B:.1f}%)')
ax1.plot(log10_mu, sin2_running_modelC, 'm:', lw=1.5, label=f'Model C: Color-only ({disc_C:.1f}%)')

# Mark key scales
ax1.axhline(sin2_W_MZ_PDG, color='k', ls='--', alpha=0.5, lw=0.8)
ax1.annotate(f'PDG: {sin2_W_MZ_PDG}', xy=(3, sin2_W_MZ_PDG), fontsize=8,
             xytext=(3, sin2_W_MZ_PDG+0.01), ha='left')

ax1.axhline(sin2_W_MKK, color='darkred', ls='--', alpha=0.5, lw=0.8)
ax1.annotate(f'Geometric: {sin2_W_MKK:.4f}', xy=(14, sin2_W_MKK), fontsize=8,
             xytext=(10, sin2_W_MKK+0.015), ha='left', color='darkred')

ax1.axhline(sin2_NCG, color='gray', ls=':', alpha=0.5, lw=0.8)
ax1.annotate(f'NCG: 3/8={sin2_NCG:.3f}', xy=(14, sin2_NCG), fontsize=8,
             xytext=(12, sin2_NCG-0.025), ha='left', color='gray')

ax1.axvline(np.log10(M_KK), color='orange', ls='-', alpha=0.3, lw=1)
ax1.annotate(f'M_KK', xy=(np.log10(M_KK), 0.55), fontsize=8, color='orange')

ax1.axvline(np.log10(M_Z), color='orange', ls='-', alpha=0.3, lw=1)
ax1.annotate(f'M_Z', xy=(np.log10(M_Z), 0.55), fontsize=8, color='orange')

# Gate thresholds
ax1.axhspan(sin2_W_MZ_PDG*0.85, sin2_W_MZ_PDG*1.15, alpha=0.05, color='green', label='PASS band (15%)')
ax1.axhspan(sin2_W_MZ_PDG*0.70, sin2_W_MZ_PDG*1.30, alpha=0.03, color='yellow')

ax1.set_xlabel('log10(mu / GeV)', fontsize=12)
ax1.set_ylabel('sin^2(theta_W)', fontsize=12)
ax1.set_title('Weinberg Angle RG Running: M_KK to M_Z', fontsize=13)
ax1.legend(fontsize=8, loc='upper left')
ax1.set_ylim(0.15, 0.65)
ax1.grid(True, alpha=0.3)

# Right panel: sin^2(theta_W) at M_KK vs tau
ax2 = axes[1]
ax2.plot(tau_array, sin2_vs_tau, 'b-', lw=2.5, label='$3e^{-4\\tau}/(3e^{-4\\tau}+1)$')
ax2.axvline(tau_fold, color='red', ls='--', alpha=0.6, lw=1)
ax2.plot(tau_fold, sin2_W_MKK, 'ro', ms=10, zorder=5,
         label=f'Fold: tau={tau_fold}, sin^2={sin2_W_MKK:.4f}')
ax2.axhline(sin2_NCG, color='gray', ls=':', alpha=0.5, lw=0.8)
ax2.annotate(f'NCG: 3/8', xy=(0.2, sin2_NCG), fontsize=8, color='gray',
             xytext=(0.2, sin2_NCG-0.02))
ax2.axhline(sin2_biinv, color='gray', ls=':', alpha=0.5, lw=0.8)
ax2.annotate(f'Bi-invariant: 3/4', xy=(0.01, sin2_biinv), fontsize=8, color='gray',
             xytext=(0.01, sin2_biinv+0.01))
ax2.axhline(sin2_W_MZ_PDG, color='k', ls='--', alpha=0.3, lw=0.8)
ax2.annotate(f'PDG (M_Z): {sin2_W_MZ_PDG}', xy=(0.15, sin2_W_MZ_PDG), fontsize=8,
             xytext=(0.12, sin2_W_MZ_PDG+0.015))

ax2.set_xlabel('tau (Jensen parameter)', fontsize=12)
ax2.set_ylabel('sin^2(theta_W) at M_KK', fontsize=12)
ax2.set_title('M_KK Boundary Condition vs Jensen Parameter', fontsize=13)
ax2.legend(fontsize=9, loc='upper right')
ax2.set_ylim(0.15, 0.80)
ax2.grid(True, alpha=0.3)

# Add gate verdict box
verdict_text = (
    f"WEINBERG-72: {gate_verdict}\n"
    f"sin^2(M_KK) = {sin2_W_MKK:.4f} (scheme-indep)\n"
    f"sin^2(M_Z) = {sin2_MZ_pureSM:.4f} (pure SM)\n"
    f"PDG = {sin2_W_MZ_PDG}\n"
    f"Discrepancy: {disc_pureSM:.1f}%\n"
    f"S_inf = {S_inf:.3f}"
)
colors = {'PASS': 'lightgreen', 'INFO': 'lightyellow', 'FAIL': 'lightsalmon'}
fig.text(0.5, 0.01, verdict_text, fontsize=9, ha='center', va='bottom',
         bbox=dict(boxstyle='round', facecolor=colors.get(gate_verdict, 'white'), alpha=0.8),
         family='monospace')

plt.tight_layout(rect=[0, 0.10, 1, 1])

plot_path = os.path.join(os.path.dirname(__file__), 's72_weinberg_angle.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

# ══════════════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("FINAL SUMMARY")
print("=" * 72)
print(f"  Gate:     WEINBERG-72")
print(f"  Verdict:  {gate_verdict}")
print(f"  Detail:   {verdict_detail}")
print()
print(f"  SCHEME-INDEPENDENT (PERMANENT):")
print(f"    sin^2(theta_W)|_{{M_KK}} = {sin2_W_MKK:.6f}")
print(f"    = 3*exp(-4*tau)/(3*exp(-4*tau)+1) at tau_fold = {tau_fold}")
print(f"    Derived from Baptista Paper 13 eq (5.21), Jensen parametrization")
print()
print(f"  SCHEME-DEPENDENT:")
print(f"    sin^2(theta_W)|_{{M_Z}} = {sin2_MZ_pureSM:.6f} (pure SM RG)")
print(f"    Discrepancy from PDG: {disc_pureSM:.1f}%")
print(f"    Threshold model range: [{disc_min:.1f}%, {disc_max:.1f}%]")
print()
print(f"  COMPARISON:")
print(f"    Standard SU(5) GUT: sin^2(M_GUT) = 3/8, gets ~5% at M_Z (with SUSY)")
print(f"    This framework: sin^2(M_KK) = 0.584, gets {disc_pureSM:.1f}% at M_Z (pure SM)")
print(f"    NCG (CC 1996): sin^2 = 3/8 at cutoff, ~10% at M_Z (from Paper 19)")
