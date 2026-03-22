#!/usr/bin/env python3
"""
CC-HIERARCHY-CUBED-45: Is the CC gap = (hierarchy problem)^3?
=============================================================

Gate: CC-HIERARCHY-CUBED-45 (INFO)
Session: 45
Date: 2026-03-15

Hypothesis: The cosmological constant gap (~110 orders) is approximately the
electroweak hierarchy problem (~36 orders) applied THREE times, corresponding
to the three steps in the spectral action moment chain a_0 -> a_2 -> a_4.

Physical picture: The spectral action S = Tr f(D/Lambda) expands as
  S = f_0 Lambda^4 A_0 + f_2 Lambda^2 A_2 + f_4 A_4 + ...
where A_n = sum_k d_k (lambda_k / M_KK)^{2n} are dimensionless spectral
moments and f_n are cutoff-function moments. The CC is proportional to the
Lambda^4 term (a_0), Newton's constant to the Lambda^2 term (a_2), and gauge
kinetics to the Lambda^0 term (a_4).

Each step down in powers of Lambda introduces a factor ~Lambda^2 / (spectral
ratio), where Lambda = M_KK. If the spectral ratios A_0/A_2 and A_2/A_4 are
O(1), then each step is one factor of M_KK^2 / M_Pl^2 ~ 10^{36} — the
hierarchy problem. Three steps would give 10^{108}.

This computation tests whether this is structural or coincidental.

References:
- Connes-Chamseddine spectral action: a_n coefficients
- Gilkey (1975): heat kernel expansion
- canonical_constants.py: M_KK, rho_Lambda_obs

Input files:
  - tier0-computation/s45_unexpanded_sa.npz (forward moments, eigenvalues)
  - tier0-computation/s44_eih_grav.npz (singlet fractions)
  - tier0-computation/canonical_constants.py

Output: tier0-computation/s45_cc_hierarchy_cubed.npz
"""

import sys
import os

# Ensure project root for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from canonical_constants import (
    M_KK_gravity, M_KK_kerner, M_Pl_reduced, M_Pl_unreduced,
    rho_Lambda_obs, rho_crit_GeV4, Omega_Lambda,
    a0_fold, a2_fold, a4_fold,
    PI,
)

# ============================================================================
#  SECTION 1: Load spectral data
# ============================================================================

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

d45 = np.load(os.path.join(DATA_DIR, "s45_unexpanded_sa.npz"), allow_pickle=True)
d44 = np.load(os.path.join(DATA_DIR, "s44_eih_grav.npz"), allow_pickle=True)

# Forward spectral moments: A_n = sum_k d_k (lambda_k/M_KK)^{2n}
# These are DIMENSIONLESS — eigenvalues already in M_KK units
A_0 = float(d45['A_0'])    # = N_total = 6440 (total mode count with degeneracy)
A_2 = float(d45['A_2'])    # = sum d_k lambda_k^2 = 16448
A_4 = float(d45['A_4'])    # = sum d_k lambda_k^4 = 45426
A_6 = float(d45['A_6'])    # = sum d_k lambda_k^6 = 133871
A_8 = float(d45['A_8'])    # = sum d_k lambda_k^8 = 416676

# Zeta-function moments (inverse): Z_n = sum_k d_k / lambda_k^{2n}
Z_2 = float(d45['Z_2'])    # = 2776
Z_4 = float(d45['Z_4'])    # = 1351

# Eigenvalue data
lsq_unique = d45['lsq_unique']  # 121 unique eigenvalues^2
deg_unique = d45['deg_unique']   # their degeneracies

# Singlet sector data
singlet_frac_SA = float(d44['singlet_frac_SA'])      # = 0.00758
singlet_frac_sq = float(d44['singlet_frac_sq'])       # = 0.00432
singlet_frac_4th = float(d44['singlet_frac_4th'])     # = 0.00132
ratio_singlet_full = float(d44['ratio_singlet_to_full'])  # = 5.68e-5

print("=" * 78)
print("CC-HIERARCHY-CUBED-45: Is CC gap = (hierarchy)^3?")
print("=" * 78)

# ============================================================================
#  SECTION 2: Pure spectral ratios (cutoff-function independent)
# ============================================================================

print("\n--- SECTION 2: Pure spectral moment ratios (dimensionless, f-independent) ---\n")

# These ratios depend ONLY on the Dirac spectrum of D_K on SU(3)
# They are independent of the cutoff function f and the scale Lambda
R_spec_02 = A_0 / A_2    # N_total / sum d_k lambda_k^2
R_spec_24 = A_2 / A_4    # sum d_k lambda_k^2 / sum d_k lambda_k^4
R_spec_46 = A_4 / A_6    # sum d_k lambda_k^4 / sum d_k lambda_k^6
R_spec_68 = A_6 / A_8    # sum d_k lambda_k^6 / sum d_k lambda_k^8

print(f"A_0 (N_total)  = {A_0:.1f}")
print(f"A_2            = {A_2:.4f}")
print(f"A_4            = {A_4:.4f}")
print(f"A_6            = {A_6:.4f}")
print(f"A_8            = {A_8:.4f}")
print()
print(f"R_02 = A_0/A_2 = {R_spec_02:.6f}")
print(f"R_24 = A_2/A_4 = {R_spec_24:.6f}")
print(f"R_46 = A_4/A_6 = {R_spec_46:.6f}")
print(f"R_68 = A_6/A_8 = {R_spec_68:.6f}")
print()
print(f"R_02 * R_24    = {R_spec_02 * R_spec_24:.6f}  (A_0/A_4)")
print(f"R_24 * R_46    = {R_spec_24 * R_spec_46:.6f}  (A_2/A_6)")
print()

# For a "flat" spectrum (all eigenvalues equal), all ratios = 1/lambda^2.
# The fact that they differ from 1 encodes the eigenvalue SPREAD.
# Mean squared eigenvalue:
lam2_mean = A_2 / A_0
lam4_mean = A_4 / A_0
lam2_rms = np.sqrt(lam2_mean)
print(f"<lambda^2>        = A_2/A_0 = {lam2_mean:.6f}")
print(f"<lambda^4>        = A_4/A_0 = {lam4_mean:.6f}")
print(f"<lambda^4>/<lambda^2>^2 = {lam4_mean / lam2_mean**2:.6f}  (kurtosis-like)")
print(f"RMS eigenvalue    = sqrt(<lambda^2>) = {lam2_rms:.6f} M_KK")
print()

# KEY OBSERVATION: The spectral ratios are ALL O(1), approximately 0.35-0.39.
# This means the spectrum is NOT degenerate — there is genuine spread.
# The hierarchy comes ENTIRELY from Lambda^2 factors, not from spectral ratios.

print("KEY: Spectral ratios are O(1). Hierarchy comes from Lambda^2 factors alone.")

# ============================================================================
#  SECTION 3: Physical moment ratios with Lambda = M_KK
# ============================================================================

print("\n--- SECTION 3: Physical moment ratios (Lambda = M_KK) ---\n")

# The spectral action expansion (Chamseddine-Connes):
#   S = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 + ...
#
# where a_n are Seeley-DeWitt coefficients on S^3 x SU(3) / M^4 x fiber.
# For the INTERNAL (KK) part at a given tau:
#   a_0^{int} proportional to A_0  (volume)
#   a_2^{int} proportional to A_2  (curvature via zeta sum)
#   a_4^{int} proportional to A_4  (Gauss-Bonnet / gauge kinetics)
#
# The PHYSICAL energy densities (in the CC problem):
#   rho_CC  ~ (Lambda^4 / (8*pi^2)) * A_0    [vacuum energy from volume term]
#   1/G_N   ~ (Lambda^2 / (8*pi^2)) * Z_2    [Sakharov induced gravity]
#   gauge   ~ (1 / (8*pi^2)) * Z_4           [gauge kinetic terms]
#
# NOTE: The CC uses the FORWARD moment A_0, gravity uses the ZETA (inverse)
# moment Z_2 = sum d_k / lambda_k^2, and gauge uses Z_4 = sum d_k / lambda_k^4.
#
# For the hierarchy test, the relevant ratios are:
#   CC/gravity     = Lambda^2 * (A_0 / Z_2)
#   gravity/gauge  = Lambda^2 * (Z_2 / Z_4)
#   CC/gauge       = Lambda^4 * (A_0 / Z_4)

# Use both M_KK extractions
for M_KK_val, M_KK_name in [(M_KK_gravity, "gravity (7.43e16 GeV)"),
                              (M_KK_kerner, "Kerner (5.04e17 GeV)")]:

    print(f"  Lambda = M_KK_{M_KK_name}:")
    print(f"  M_KK = {M_KK_val:.4e} GeV")
    print(f"  M_KK / M_Pl_reduced = {M_KK_val / M_Pl_reduced:.6f}")
    print(f"  (M_KK / M_Pl_reduced)^2 = {(M_KK_val / M_Pl_reduced)**2:.4e}")
    print()

    # CC/gravity ratio: how much bigger is Lambda^4 * A_0 vs Lambda^2 * Z_2?
    R1 = (M_KK_val**2) * (A_0 / Z_2)
    log_R1 = np.log10(R1)

    # gravity/gauge ratio: how much bigger is Lambda^2 * Z_2 vs Z_4?
    R2 = (M_KK_val**2) * (Z_2 / Z_4)
    log_R2 = np.log10(R2)

    # Total CC/gauge ratio
    R_total = R1 * R2
    log_R_total = np.log10(R_total)

    # Each R should be ~hierarchy if the cubed hypothesis holds
    hierarchy_log = np.log10(M_Pl_reduced**2 / M_KK_val**2)

    print(f"  R1 (CC/gravity)  = {R1:.4e}   log10 = {log_R1:.4f}")
    print(f"  R2 (gravity/gauge) = {R2:.4e}   log10 = {log_R2:.4f}")
    print(f"  R_total (CC/gauge) = {R_total:.4e}   log10 = {log_R_total:.4f}")
    print()
    print(f"  Standard hierarchy = M_Pl^2 / M_KK^2 = {(M_Pl_reduced / M_KK_val)**2:.4e}")
    print(f"  log10(hierarchy) = {hierarchy_log:.4f}")
    print(f"  R1 / hierarchy = {log_R1 / hierarchy_log:.4f}")
    print(f"  R2 / hierarchy = {log_R2 / hierarchy_log:.4f}")
    print(f"  R_total / hierarchy^2 = {log_R_total / (2 * hierarchy_log):.4f}")
    print()

    # The spectral ratios A_0/Z_2 and Z_2/Z_4 shift R away from pure Lambda^2
    print(f"  Spectral correction to R1: A_0/Z_2 = {A_0 / Z_2:.4f}")
    print(f"  Spectral correction to R2: Z_2/Z_4 = {Z_2 / Z_4:.4f}")
    print(f"  log10(A_0/Z_2) = {np.log10(A_0 / Z_2):.4f} orders")
    print(f"  log10(Z_2/Z_4) = {np.log10(Z_2 / Z_4):.4f} orders")
    print()

# ============================================================================
#  SECTION 4: The CC gap decomposition
# ============================================================================

print("\n--- SECTION 4: CC gap decomposition into moment-chain factors ---\n")

# The observed CC gap:
#   rho_spectral / rho_obs ~ 10^{120}
#
# From the spectral action on M^4 x SU(3):
#   rho_CC = (2 / pi^2) * f_0 * Lambda^4 * A_0
#
# Using f_0 = 1 (normalization) and Lambda = M_KK:
rho_CC_grav = (2.0 / PI**2) * M_KK_gravity**4 * A_0
rho_CC_kern = (2.0 / PI**2) * M_KK_kerner**4 * A_0

gap_grav = np.log10(rho_CC_grav / rho_Lambda_obs)
gap_kern = np.log10(rho_CC_kern / rho_Lambda_obs)

print(f"rho_CC (gravity M_KK) = {rho_CC_grav:.4e} GeV^4")
print(f"rho_CC (Kerner M_KK)  = {rho_CC_kern:.4e} GeV^4")
print(f"rho_obs               = {rho_Lambda_obs:.2e} GeV^4")
print()
print(f"CC gap (gravity route) = {gap_grav:.2f} orders")
print(f"CC gap (Kerner route)  = {gap_kern:.2f} orders")
print()

# Now decompose the gap into contributions.
# rho_CC = (2/pi^2) * Lambda^4 * A_0
#        = (2/pi^2) * Lambda^4 * (A_0/Z_2) * (Z_2/Z_4) * Z_4
#
# The G_N term gives: 1/G_N ~ Lambda^2 * Z_2 / (48 * pi^2)
# So Lambda^2 ~ 48 * pi^2 / (G_N * Z_2) = 48 * pi^2 * M_Pl^2 / Z_2
# (using G_N = 1/M_Pl^2 in natural units)
#
# The "hierarchy" per step is not purely Lambda^2.
# Let's define the three layers:
#
# Layer 1: Lambda^4 contribution (CC scale)
# Layer 2: Lambda^2 contribution (gravity scale)
# Layer 3: Lambda^0 contribution (gauge scale)
#
# The actual hierarchy PER STEP depends on:
# Step a_0 -> a_2: factor = Lambda^2 * (A_0/A_2) or Lambda^2 * (A_0/Z_2)
# Step a_2 -> a_4: factor = Lambda^2 * (A_2/A_4) or Lambda^2 * (Z_2/Z_4)
#
# BUT: the correct physical decomposition uses DIFFERENT moment types:
# a_0 ~ Lambda^4 * A_0 (forward zeroth moment)
# a_2 ~ Lambda^2 * Z_2 (inverse second moment for gravity)
# a_4 ~ Z_4 (inverse fourth moment for gauge)

M_KK = M_KK_gravity  # Default route

# Step 1: a_0 / a_2 = Lambda^2 * (A_0 / Z_2)
step_02 = M_KK**2 * (A_0 / Z_2)
log_step_02 = np.log10(step_02)

# Step 2: a_2 / a_4 = Lambda^2 * (Z_2 / Z_4)
step_24 = M_KK**2 * (Z_2 / Z_4)
log_step_24 = np.log10(step_24)

# Total: a_0 / a_4 = Lambda^4 * (A_0 / Z_4)
total_04 = step_02 * step_24
log_total_04 = np.log10(total_04)

print("Decomposition of moment chain (gravity M_KK):")
print(f"  Step 1 (a_0/a_2): Lambda^2 * A_0/Z_2 = {step_02:.4e}  [{log_step_02:.2f} orders]")
print(f"  Step 2 (a_2/a_4): Lambda^2 * Z_2/Z_4 = {step_24:.4e}  [{log_step_24:.2f} orders]")
print(f"  Total  (a_0/a_4): Lambda^4 * A_0/Z_4 = {total_04:.4e}  [{log_total_04:.2f} orders]")
print()
print(f"  log10(Step 1) = {log_step_02:.4f}")
print(f"  log10(Step 2) = {log_step_24:.4f}")
print(f"  Average step  = {(log_step_02 + log_step_24) / 2:.4f}")
print()

# Compare to the hierarchy
hierarchy_grav = np.log10(M_Pl_reduced / M_KK)**2
log_hierarchy = np.log10((M_Pl_reduced / M_KK)**2)
print(f"  Hierarchy = (M_Pl/M_KK)^2 = {(M_Pl_reduced / M_KK)**2:.4e}  [{log_hierarchy:.2f} orders]")
print(f"  EW hierarchy = M_Pl/M_W ~ 10^{np.log10(M_Pl_reduced / 80.4):.1f}")
print(f"  E/M hierarchy = F_em/F_grav ~ 10^{36}")
print()

# The "standard" CC problem counting:
# rho_Planck / rho_obs ~ 10^{120} — this is Planck^4 / rho_obs
rho_Planck = M_Pl_reduced**4  # in natural units, rho_Planck = M_Pl^4
gap_Planck = np.log10(rho_Planck / rho_Lambda_obs)
print(f"  Planck gap: M_Pl^4 / rho_obs = 10^{gap_Planck:.2f}")
print(f"  EW hierarchy gap: (M_Pl/M_W)^2 = 10^{2 * np.log10(M_Pl_reduced / 80.4):.2f}")
print(f"  CC_gap / EW_hierarchy^2 = {gap_Planck / (2 * np.log10(M_Pl_reduced / 80.4)):.4f}")
print()

# ============================================================================
#  SECTION 5: The "cubed" test — direct
# ============================================================================

print("\n--- SECTION 5: The cubed test ---\n")

# Different ways to measure "the hierarchy"
hierarchy_EM_grav = 36.0  # log10(F_EM / F_grav) for proton
hierarchy_EW = np.log10(M_Pl_reduced / 80.4)  # M_Pl / M_W
hierarchy_KK = np.log10(M_Pl_reduced / M_KK)  # M_Pl / M_KK
hierarchy_Planck = np.log10(M_Pl_reduced / 1.0)  # M_Pl in GeV (= hierarchy from GeV scale)

# Different ways to measure "the CC gap"
cc_gap_Planck = gap_Planck   # M_Pl^4 / rho_obs
cc_gap_spectral_grav = gap_grav  # rho_SA(gravity) / rho_obs
cc_gap_spectral_kern = gap_kern  # rho_SA(Kerner) / rho_obs
cc_gap_conventional = 120.0      # The textbook "120 orders"

# The hypothesis: CC gap / hierarchy ~ 3 (cubed)
# But we must be careful about WHICH hierarchy and WHICH gap

print("CUBED RATIOS:")
print()
print("  (a) Standard CC problem (Planck units):")
print(f"      CC gap = log10(M_Pl^4 / rho_obs) = {cc_gap_Planck:.2f}")
print(f"      Hierarchy (EM/grav) = 36")
print(f"      Ratio = {cc_gap_Planck / 36:.4f}")
print(f"      Hierarchy (M_Pl/M_W) = {hierarchy_EW:.2f}")
print(f"      Ratio = {cc_gap_Planck / hierarchy_EW:.4f}")
print()

print("  (b) Spectral action CC (gravity M_KK):")
print(f"      CC gap = log10(rho_SA / rho_obs) = {cc_gap_spectral_grav:.2f}")
print(f"      Hierarchy (M_Pl/M_KK) = {hierarchy_KK:.2f}")
print(f"      Ratio = {cc_gap_spectral_grav / hierarchy_KK:.4f}")
print(f"      Ratio / 2 = {cc_gap_spectral_grav / (2 * hierarchy_KK):.4f}  (should be ~1 if gap = hierarchy^2)")
print()

print("  (c) Spectral action CC (Kerner M_KK):")
print(f"      CC gap = log10(rho_SA / rho_obs) = {cc_gap_spectral_kern:.2f}")
print(f"      Hierarchy (M_Pl/M_KK) = {np.log10(M_Pl_reduced / M_KK_kerner):.2f}")
print(f"      Ratio = {cc_gap_spectral_kern / np.log10(M_Pl_reduced / M_KK_kerner):.4f}")
print()

print("  (d) Direct moment chain (gravity M_KK):")
print(f"      Two-step chain: {log_step_02:.2f} + {log_step_24:.2f} = {log_total_04:.2f} orders")
print(f"      Each step ~ Lambda^2 = M_KK^2 = 10^{2 * np.log10(M_KK):.2f}")
print(f"      log10(M_KK^2) = {2 * np.log10(M_KK):.2f}")
print(f"      Number of M_KK^2 steps in CC gap: {cc_gap_spectral_grav / (2 * np.log10(M_KK)):.4f}")
print()

# ============================================================================
#  SECTION 6: PRECISE decomposition — what ACTUALLY produces the gap
# ============================================================================

print("\n--- SECTION 6: Precise decomposition of the CC gap ---\n")

# rho_CC = (2/pi^2) * M_KK^4 * A_0
# rho_obs = 2.7e-47 GeV^4
#
# gap = log10(rho_CC / rho_obs)
#     = log10(2/pi^2) + 4*log10(M_KK) + log10(A_0) - log10(rho_obs)

log_prefactor = np.log10(2.0 / PI**2)
log_MKK4 = 4 * np.log10(M_KK)
log_A0 = np.log10(A_0)
log_rho_obs = np.log10(rho_Lambda_obs)

print("gap = log10(2/pi^2) + 4*log10(M_KK) + log10(A_0) - log10(rho_obs)")
print()
print(f"  log10(2/pi^2)     = {log_prefactor:.4f}")
print(f"  4*log10(M_KK)     = {log_MKK4:.4f}   (M_KK = {M_KK:.4e} GeV)")
print(f"  log10(A_0)        = {log_A0:.4f}   (A_0 = {A_0:.0f})")
print(f"  -log10(rho_obs)   = {-log_rho_obs:.4f}   (rho_obs = {rho_Lambda_obs:.2e} GeV^4)")
print(f"  ---------------------------------")
gap_check = log_prefactor + log_MKK4 + log_A0 - log_rho_obs
# Note: log_rho_obs is negative, so -log_rho_obs is positive
print(f"  TOTAL gap         = {gap_check:.4f}   (check: {gap_grav:.4f})")
print()

# The "Lambda^4" contribution is 4*log10(M_KK) = 67.4 for gravity route.
# This is NOT the same as the hierarchy (M_Pl/M_KK)^2 = 10^{2.69}
# The point is: M_KK^4 = 10^{67.4}, rho_obs = 10^{-46.6}
# So the gap is 67.4 + 3.8 - 0.7 + 46.6 = 117.1

# The hierarchy problem asks: why is M_KK << M_Pl?
# M_Pl^4 = 10^{73.6} for reduced Planck mass
log_MPl4 = 4 * np.log10(M_Pl_reduced)
print(f"  4*log10(M_Pl)     = {log_MPl4:.4f}")
print(f"  4*log10(M_KK)     = {log_MKK4:.4f}")
print(f"  Difference        = {log_MPl4 - log_MKK4:.4f}  (= 4 * log10(M_Pl/M_KK) = 4 * {np.log10(M_Pl_reduced / M_KK):.4f})")
print()

# In terms of M_Pl^4:
print("ALTERNATIVE: CC gap in M_Pl units")
gap_from_Planck = np.log10(M_Pl_reduced**4 / rho_Lambda_obs)
print(f"  M_Pl^4 / rho_obs = 10^{gap_from_Planck:.2f}")
print(f"  This is the 'standard' CC problem (120 orders)")
print()
print(f"  The spectral action adds log10((2/pi^2) * A_0 * (M_KK/M_Pl)^4) = {log_prefactor + log_A0 + log_MKK4 - log_MPl4:.4f}")
print(f"  which is a SUPPRESSION of 10^{-(log_prefactor + log_A0 + log_MKK4 - log_MPl4):.2f} below M_Pl^4")
print()

# ============================================================================
#  SECTION 7: Factor-of-three test with HONEST counting
# ============================================================================

print("\n--- SECTION 7: Honest factor-of-three test ---\n")

# The claim: CC gap ~ 3 * hierarchy. Let's check every sensible definition.

# Definition 1: "hierarchy" = log10(M_Pl^2 / M_W^2) = 2 * log10(M_Pl/M_W)
h_EW = 2 * np.log10(M_Pl_reduced / 80.4)     # = 2 * 16.48 = 32.96
h_EM = 36.0                                     # electromagnetic: alpha * m_p^2 / (G_N * m_p^2)
h_KK = 2 * np.log10(M_Pl_reduced / M_KK)       # = 2 * 1.52 = 3.04 (M_KK close to M_Pl!)
h_MKK_sq = 2 * np.log10(M_KK)                   # = 33.7 (log10 of M_KK^2 in GeV^2)

print("Hierarchy definitions:")
print(f"  h_EW = 2*log10(M_Pl/M_W) = {h_EW:.2f}")
print(f"  h_EM = log10(F_EM/F_grav) = {h_EM:.2f}")
print(f"  h_KK = 2*log10(M_Pl/M_KK) = {h_KK:.2f}  (M_KK very close to M_Pl!)")
print(f"  h_MKK_sq = 2*log10(M_KK/GeV) = {h_MKK_sq:.2f}")
print()

print("CC gap definitions:")
print(f"  gap_Planck    = {gap_from_Planck:.2f}  (M_Pl^4 / rho_obs)")
print(f"  gap_spectral  = {gap_grav:.2f}  (rho_SA / rho_obs)")
print(f"  gap_textbook  = 120")
print()

print("RATIO MATRIX: gap / hierarchy")
print(f"{'':>20s}  {'h_EW':>8s}  {'h_EM':>8s}  {'h_KK':>8s}  {'h_MKK2':>8s}")
for gap_val, gap_name in [(gap_from_Planck, "gap_Planck"),
                           (gap_grav, "gap_SA(grav)"),
                           (gap_kern, "gap_SA(kern)"),
                           (120.0, "gap_textbook")]:
    r_EW = gap_val / h_EW
    r_EM = gap_val / h_EM
    r_KK = gap_val / h_KK
    r_MKK = gap_val / h_MKK_sq
    print(f"  {gap_name:>18s}  {r_EW:8.3f}  {r_EM:8.3f}  {r_KK:8.3f}  {r_MKK:8.3f}")

print()

# ============================================================================
#  SECTION 8: Singlet sector analysis
# ============================================================================

print("\n--- SECTION 8: Singlet sector moment ratios ---\n")

# The singlet (0,0) sector has 16 modes (spinor rep of SO(6), single SU(3) rep).
# At the fold (tau=0.19), the singlet eigenvalues are a subset of the full spectrum.
# From s44_eih_grav: singlet_frac_SA = 0.00758, singlet_frac_sq = 0.00432, etc.

# Reconstruct singlet moments from fractions.
# singlet_frac_SA = S_singlet / S_fold ≈ sum_singlet vs sum_all for polynomial SA
# singlet_frac_sq = (sum_singlet d_k lam^2) / (sum_all d_k lam^2) = A_2^{singlet} / A_2
# singlet_frac_4th = A_4^{singlet} / A_4

# Singlet mode count: N_singlet = 16 (the (0,0) rep has dim = 1, spinor has 16 components)
N_singlet = 16

# Singlet moments from fractions
A_0_singlet = N_singlet  # 16 modes
A_2_singlet = singlet_frac_sq * A_2    # sum_singlet d_k lam^2
A_4_singlet = singlet_frac_4th * A_4   # sum_singlet d_k lam^4

R_spec_02_singlet = A_0_singlet / A_2_singlet
R_spec_24_singlet = A_2_singlet / A_4_singlet

print(f"Singlet (0,0) sector:")
print(f"  N_singlet = {N_singlet}")
print(f"  A_2^singlet = {A_2_singlet:.4f}  (frac = {singlet_frac_sq:.6f})")
print(f"  A_4^singlet = {A_4_singlet:.4f}  (frac = {singlet_frac_4th:.6f})")
print()
print(f"  R_02^singlet = {R_spec_02_singlet:.6f}  (full: {R_spec_02:.6f})")
print(f"  R_24^singlet = {R_spec_24_singlet:.6f}  (full: {R_spec_24:.6f})")
print()
print(f"  <lam^2>_singlet = A_2/A_0 = {A_2_singlet / N_singlet:.6f}  (full: {lam2_mean:.6f})")
print()

# Singlet CC gap
rho_CC_singlet = (2.0 / PI**2) * M_KK**4 * A_0_singlet
gap_singlet = np.log10(rho_CC_singlet / rho_Lambda_obs)
print(f"  rho_CC (singlet only) = {rho_CC_singlet:.4e} GeV^4")
print(f"  CC gap (singlet) = {gap_singlet:.2f} orders")
print(f"  Suppression vs full: {gap_grav - gap_singlet:.2f} orders (= log10(A_0/N_singlet) = {np.log10(A_0 / N_singlet):.4f})")
print()

# ============================================================================
#  SECTION 9: Peter-Weyl degeneracy prediction
# ============================================================================

print("\n--- SECTION 9: Peter-Weyl degeneracy structure ---\n")

# On SU(3), the Peter-Weyl decomposition labels irreps by (p,q) with
# degeneracy d_{(p,q)} = ((p+1)(q+1)(p+q+2)/2)^2 (left x right regular rep).
# With spinor: multiply by 2^3 = 8 (Dirac on dim-6 manifold).
#
# The Casimir eigenvalue for rep (p,q) is:
#   C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3
#
# The Dirac eigenvalues on round SU(3) are:
#   lambda_{(p,q),j}^2 = C_2(p,q) + constant shifts (from Parthasarathy formula)
#
# For the moment sums:
#   A_n = sum_{(p,q)} d_{(p,q)} * (sum over j of lambda_{(p,q),j}^{2n})
#
# At large Casimir, d_{(p,q)} ~ C^4 (since d ~ (p+q)^4 ~ C^2).
# Wait: d_{(p,q)} = ((p+1)(q+1)(p+q+2)/2)^2. For p=q=n, d ~ n^6/4 ~ C^3.
# Actually C ~ n^2, so d ~ n^6 ~ C^3 for diagonal, but in general d ~ C^2 for fixed p/q ratio.
#
# Let's just COMPUTE the predicted ratios from the Weyl asymptotics.

# The Weyl asymptotic for the spectral action on a d-dimensional manifold:
#   sum_{lambda_n < Lambda} 1 ~ Lambda^d * Vol / (4*pi)^{d/2} * ...
#
# For SU(3) (dim=8 as manifold, but we have dim=6 fiber):
# The spectral dimension from the data:
d_weyl = float(d45['d_weyl'])  # from the actual spectrum fit
print(f"Fitted Weyl spectral dimension: d = {d_weyl:.4f}")
print(f"(Expected for SU(3): d = 8 as group manifold, but Dirac on 6-dim fiber)")
print()

# Compute moment ratios from truncated Peter-Weyl sum
print("Peter-Weyl moment sum (explicit computation):")
print()

# Build the representation list up to some cutoff
pmax = 20  # go up to (p,q) with p,q <= 20
pw_A0 = 0.0
pw_A2 = 0.0
pw_A4 = 0.0

# For each (p,q), the SU(3) Casimir is:
#   C2 = (p^2 + q^2 + pq + 3p + 3q) / 3
# The degeneracy in the regular representation is:
#   d = ((p+1)(q+1)(p+q+2)/2)^2
# For the DIRAC spectrum, the eigenvalues depend on tau.
# At round SU(3) (tau=0), the Dirac eigenvalues are:
#   lambda^2 = C2(p,q) + lower-order terms

# For the Weyl prediction, we want the ASYMPTOTIC ratio.
# In the large-C limit, lambda^2 ~ C2 and the sums are:
#   A_n^{Weyl} = sum_{(p,q)} d_{(p,q)} * C2^n * (# Dirac modes per rep)

for p in range(pmax + 1):
    for q in range(pmax + 1):
        d_rep_sq = ((p + 1) * (q + 1) * (p + q + 2) / 2.0)**2
        # Factor of 8 for spinor (Dirac on 6-dim), factor of 2 for ± eigenvalues
        # Actually the total multiplicity is d_rep^2 * (spinor multiplicity)
        # In the actual data, N=6440 corresponds to some truncation.
        # For the Weyl test, just use d_rep_sq.
        C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0
        if C2 == 0 and p == 0 and q == 0:
            # Singlet: Casimir = 0, but eigenvalues are NOT zero (shifted)
            # Use a small value to avoid division issues in ratios
            C2_eff = 0.672  # ~ smallest eigenvalue^2 from data
        else:
            C2_eff = C2

        pw_A0 += d_rep_sq
        pw_A2 += d_rep_sq * C2_eff
        pw_A4 += d_rep_sq * C2_eff**2

pw_R02 = pw_A0 / pw_A2
pw_R24 = pw_A2 / pw_A4

print(f"  Peter-Weyl sum (pmax={pmax}):")
print(f"    A_0^PW = {pw_A0:.1f}")
print(f"    A_2^PW = {pw_A2:.1f}")
print(f"    A_4^PW = {pw_A4:.1f}")
print(f"    R_02^PW = {pw_R02:.6f}")
print(f"    R_24^PW = {pw_R24:.6f}")
print()
print(f"  Exact (from data):")
print(f"    R_02 = {R_spec_02:.6f}")
print(f"    R_24 = {R_spec_24:.6f}")
print()

# How does the Weyl prediction compare?
# For large cutoff, the degeneracy growth d ~ C^{d/2 - 1} determines the
# moment ratios. The key insight: because d grows as a POWER of C,
# the moment sums are dominated by the HIGHEST modes.

# Asymptotic analysis: for d_{(p,q)} ~ (pq)^2 ~ C^2 at large C,
# A_n ~ sum C^2 * C^n ~ integral C^{n+2} * (density of states) dC
# The density of states on SU(3) goes as ~ C^{5/2} (from Weyl on dim-8)
# So A_n ~ integral_0^{C_max} C^{n+2} * C^{5/2} dC = C_max^{n + 11/2} / (n + 11/2)
# Then A_0/A_2 ~ 1/C_max^2 * (n+11/2) correction... this gives O(1) ONLY if
# we normalize by the cutoff.

# Actually, these are FINITE sums — the spectrum is bounded.
# The ratio A_0/A_2 = N_total / sum(d*lam^2) is finite and O(1).
# It does NOT scale with any power of the cutoff.

# The hierarchy comes from Lambda = M_KK in GeV, NOT from the spectral ratios.

# ============================================================================
#  SECTION 10: The structural verdict
# ============================================================================

print("\n--- SECTION 10: Structural verdict ---\n")

print("ANALYSIS:")
print()
print("  1. The CC gap from the spectral action is:")
print(f"     log10(rho_SA / rho_obs) = {gap_grav:.2f} orders (gravity M_KK)")
print()
print("  2. This gap decomposes as:")
print(f"     log10(2/pi^2) = {log_prefactor:.2f}  (geometric prefactor)")
print(f"     4*log10(M_KK) = {log_MKK4:.2f}  (cutoff scale)")
print(f"     log10(A_0)    = {log_A0:.2f}  (total mode count)")
print(f"     -log10(rho_obs) = {-log_rho_obs:.2f}  (observed CC)")
print(f"     TOTAL = {gap_check:.2f}")
print()
print("  3. The 'hierarchy problem' is the question: why is M_KK << M_Pl?")
print(f"     But M_KK = {M_KK:.2e} GeV vs M_Pl = {M_Pl_reduced:.2e} GeV")
print(f"     log10(M_Pl/M_KK) = {np.log10(M_Pl_reduced / M_KK):.2f}")
print(f"     This is NOT a 36-order hierarchy! M_KK is only {np.log10(M_Pl_reduced / M_KK):.1f} orders below M_Pl.")
print()
print("  4. The '36 orders' hierarchy is the ELECTROWEAK hierarchy: M_Pl/M_W.")
print(f"     log10(M_Pl/M_W) = {np.log10(M_Pl_reduced / 80.4):.2f}")
print(f"     That gives gap/hierarchy = {gap_from_Planck:.1f}/{2*np.log10(M_Pl_reduced/80.4):.1f} = {gap_from_Planck / (2*np.log10(M_Pl_reduced/80.4)):.2f}")
print()
print("  5. The moment chain test:")
print(f"     Step 1 (a0->a2): {log_step_02:.2f} orders")
print(f"     Step 2 (a2->a4): {log_step_24:.2f} orders")
print(f"     These are NOT equal to each other ({log_step_02:.2f} vs {log_step_24:.2f})")
print(f"     and NOT equal to the 'hierarchy' ({log_hierarchy:.2f}) unless hierarchy = M_KK^2 scale.")
print()

# The REAL question: each step is ~Lambda^2 * (spectral ratio).
# Lambda^2 = M_KK^2 = 10^{33.7}. The spectral ratios are O(1) corrections.
# So each step IS roughly Lambda^2, not the hierarchy (M_Pl/M_KK)^2.
print("  6. STRUCTURAL RESULT:")
print(f"     Each step in the moment chain = Lambda^2 * O(1) = M_KK^2 * O(1)")
print(f"     = 10^{2*np.log10(M_KK):.2f} * O(1)")
print()
print(f"     The CC gap = 2 * log10(M_KK^2) + corrections")
print(f"               = {2 * 2 * np.log10(M_KK):.2f} + {gap_grav - 4*np.log10(M_KK):.2f}")
print(f"               = {gap_grav:.2f}")
print()
print(f"     The 'cubed' observation {gap_grav:.1f}/36 = {gap_grav/36:.2f} is a")
print(f"     NUMERICAL COINCIDENCE arising from:")
print(f"       4*log10(M_KK) = {log_MKK4:.1f} ~ 2 * 36 = 72 ONLY because")
print(f"       log10(M_KK) ~ 16.9 ~ 36/2 ... and 36 ~ 2*log10(M_Pl/M_W)")
print()

# Is there deeper structure? Check if M_KK being close to M_GUT is structural
print("  7. IS THERE DEEPER STRUCTURE?")
print()
print("     The spectral action sets Lambda = M_KK (compactification scale).")
print("     The CC is rho_CC ~ Lambda^4 * A_0.")
print("     The gap is 4*log10(Lambda) + log10(A_0) - log10(rho_obs).")
print()
print("     For the gap to be 3 * hierarchy, we need:")
print("       4*log10(M_KK) + log10(A_0) - log10(rho_obs) = 3 * 2*log10(M_Pl/M_EW)")
print()
hierarchy_EW_val = 2 * np.log10(M_Pl_reduced / 80.4)
required_MKK = 10**((3 * hierarchy_EW_val - log_A0 + log_rho_obs - log_prefactor) / 4)
print(f"     Required M_KK for exact cubed: {required_MKK:.4e} GeV")
print(f"     Actual M_KK:                   {M_KK:.4e} GeV")
print(f"     log10(required/actual) = {np.log10(required_MKK / M_KK):.4f}")
print()

# The actual deep structure is simpler:
# The CC gap ≈ 4 * log10(M_KK) + 50 ≈ 4 * 16.9 + 50 = 117.6
# The hierarchy ≈ log10(M_Pl^2 / M_EW^2) ≈ 33
# The ratio ≈ 117/33 ≈ 3.55

# But the ACTUAL algebraic relationship is:
# gap = 4*log10(M_KK) + log10(A_0) + log10(2/pi^2) + 46.6
# hierarchy = 2*log10(M_Pl/M_EW)
# These have NO algebraic relationship unless M_KK is fixed by M_Pl and M_EW.

# ============================================================================
#  SECTION 11: What the spectral ratios DO tell us
# ============================================================================

print("\n--- SECTION 11: What the spectral ratios encode ---\n")

print("The spectral ratios A_n/A_{n+2} are fixed by the Peter-Weyl spectrum.")
print("They encode the SHAPE of the eigenvalue distribution, not the scale.")
print()
print("Moment ratios (pure spectral geometry):")
print(f"  R_02 = A_0/A_2 = {R_spec_02:.6f}")
print(f"  R_24 = A_2/A_4 = {R_spec_24:.6f}")
print(f"  R_46 = A_4/A_6 = {R_spec_46:.6f}")
print(f"  R_68 = A_6/A_8 = {R_spec_68:.6f}")
print()

# Check if ratios converge (Weyl-limited spectrum)
print(f"  R_02/R_24 = {R_spec_02 / R_spec_24:.6f}")
print(f"  R_24/R_46 = {R_spec_24 / R_spec_46:.6f}")
print(f"  R_46/R_68 = {R_spec_46 / R_spec_68:.6f}")
print()

# The ratios approach a limit determined by the maximum eigenvalue
lam_max_sq = float(d45['lam_max_sq'])
lam_min_sq = float(d45['lam_min_sq'])
print(f"  Eigenvalue range: lambda^2 in [{lam_min_sq:.4f}, {lam_max_sq:.4f}]")
print(f"  Condition number: lam_max/lam_min = {np.sqrt(lam_max_sq / lam_min_sq):.4f}")
print(f"  For sharp-cutoff, R -> 1/lam_max^2 = {1/lam_max_sq:.4f} (R_68 already = {R_spec_68:.4f})")
print()

# The key physical content: the ratios are UNIVERSAL for round SU(3),
# meaning they depend only on the group structure (and tau for deformed SU(3)).
# They are O(0.3-0.4), meaning the effective eigenvalue spread is modest.
# The hierarchy comes entirely from Lambda^2 = M_KK^2 being large in GeV.

# ============================================================================
#  SECTION 12: Forward / zeta moment comparison
# ============================================================================

print("\n--- SECTION 12: Forward vs zeta moments ---\n")

# The CC uses the FORWARD moment A_0 = sum d_k (counting).
# Newton's constant uses the ZETA moment Z_2 = sum d_k / lambda_k^2.
# Gauge kinetics uses Z_4 = sum d_k / lambda_k^4.
#
# The CORRECT hierarchy chain for physics is:
#   CC     ~ Lambda^4 * A_0
#   G_N^-1 ~ Lambda^2 * Z_2
#   gauge  ~ Z_4
#
# So the chain is Lambda^4 * A_0 -> Lambda^2 * Z_2 -> Z_4

print(f"Forward moments:  A_0 = {A_0:.1f},  A_2 = {A_2:.2f},  A_4 = {A_4:.2f}")
print(f"Zeta moments:     Z_2 = {Z_2:.2f},  Z_4 = {Z_4:.2f}")
print()
print(f"A_0 / Z_2 = {A_0 / Z_2:.4f}   (forward/zeta correction at level 0->2)")
print(f"Z_2 / Z_4 = {Z_2 / Z_4:.4f}   (zeta ratio 2->4)")
print(f"A_2 / A_4 = {A_2 / A_4:.4f}   (forward ratio 2->4)")
print()
print(f"A_0 * Z_4 / (Z_2^2) = {A_0 * Z_4 / Z_2**2:.6f}  (mixed moment cross-ratio)")
print()

# The CC/G_N ratio and G_N/gauge ratio:
print(f"Physical hierarchy chain:")
print(f"  CC / (1/G_N) = Lambda^2 * A_0 / Z_2 = M_KK^2 * {A_0/Z_2:.3f}")
print(f"              = {M_KK**2 * A_0 / Z_2:.4e}  [{np.log10(M_KK**2 * A_0 / Z_2):.2f} orders]")
print(f"  (1/G_N) / gauge = Lambda^2 * Z_2 / Z_4 = M_KK^2 * {Z_2/Z_4:.3f}")
print(f"                  = {M_KK**2 * Z_2 / Z_4:.4e}  [{np.log10(M_KK**2 * Z_2 / Z_4):.2f} orders]")
print()
print(f"  Sum of two steps: {np.log10(M_KK**2 * A_0 / Z_2) + np.log10(M_KK**2 * Z_2 / Z_4):.2f} orders")
print(f"  This is the CC/gauge ratio (two Lambda^2 factors, not three)")
print()

# ============================================================================
#  SECTION 13: GATE VERDICT
# ============================================================================

print("\n" + "=" * 78)
print("GATE: CC-HIERARCHY-CUBED-45 (INFO)")
print("=" * 78)
print()

# Assemble the verdict
is_cubed = abs(gap_grav / 36.0 - 3.0) < 0.5  # Within 0.5 of 3?
is_structural = False  # determined by analysis

print("QUESTION: Is the CC gap structurally = (hierarchy)^3?")
print()
print(f"NUMERICAL TEST:")
print(f"  CC gap (SA, gravity M_KK) = {gap_grav:.2f} orders")
print(f"  CC gap (Planck units)      = {gap_from_Planck:.2f} orders")
print(f"  EM hierarchy               = 36 orders")
print(f"  gap_SA / 36                = {gap_grav / 36:.3f}")
print(f"  gap_Pl / 36                = {gap_from_Planck / 36:.3f}")
print()

print("MOMENT CHAIN TEST:")
print(f"  Step 1 (CC -> gravity):    {log_step_02:.2f} orders  (Lambda^2 * A_0/Z_2)")
print(f"  Step 2 (gravity -> gauge): {log_step_24:.2f} orders  (Lambda^2 * Z_2/Z_4)")
print(f"  Total (2 steps):           {log_total_04:.2f} orders")
print(f"  Per step:                  {(log_step_02 + log_step_24)/2:.2f} orders")
print()
print(f"  The moment chain has TWO steps (a_0 -> a_2 -> a_4), not three.")
print(f"  Each step is ~Lambda^2 * O(1) = 10^{2*np.log10(M_KK):.1f} * O(1)")
print()

print("STRUCTURAL ANALYSIS:")
print()
print("  The spectral action moment chain a_0 -> a_2 -> a_4 has TWO Lambda^2")
print("  factors, giving CC/gauge ~ Lambda^4 ~ M_KK^4.")
print()
print(f"  The CC gap ~ 4*log10(M_KK) + O(1) = {4*np.log10(M_KK):.1f} + {gap_grav - 4*np.log10(M_KK):.1f} = {gap_grav:.1f}")
print(f"  The EM hierarchy = 36 = 2*log10(F_EM/F_grav)")
print(f"  The ratio {gap_grav:.1f}/36 = {gap_grav/36:.2f} ~ 3 is a numerical coincidence:")
print(f"    It requires 4*log10(M_KK) + {gap_grav - 4*np.log10(M_KK):.1f} ~ 3*36 = 108")
print(f"    i.e., log10(M_KK) ~ (108 - {gap_grav - 4*np.log10(M_KK):.1f})/4 ~ {(108 - (gap_grav - 4*np.log10(M_KK)))/4:.1f}")
print(f"    Actual log10(M_KK) = {np.log10(M_KK):.2f}")
print()
print(f"  The near-integer ratio arises because M_KK ~ M_GUT ~ 10^16-17 GeV,")
print(f"  and 4*16.9 = 67.6 happens to combine with log10(A_0) + offset ~ 50")
print(f"  to give ~117 ~ 3*36+9. The '3' is not a deep algebraic factor.")
print()

print("SPECTRAL GEOMETRY RESULT:")
print(f"  The pure spectral ratios A_n/A_{{n+2}} are O(0.3-0.4), encoding")
print(f"  the eigenvalue spread on SU(3). They are UNIVERSAL for the group")
print(f"  and contribute only ~0.4 orders to each step in the chain.")
print(f"  The singlet sector has similar ratios (R_02={R_spec_02_singlet:.3f}, R_24={R_spec_24_singlet:.3f})")
print(f"  vs full spectrum (R_02={R_spec_02:.3f}, R_24={R_spec_24:.3f}).")
print()

verdict = "COINCIDENCE"
print(f"VERDICT: {verdict}")
print()
print(f"  The approximate relation CC gap ~ 3 * (EM hierarchy) is a numerical")
print(f"  coincidence, not a structural identity. The spectral action has a")
print(f"  TWO-step moment chain (not three), each step contributes ~Lambda^2,")
print(f"  and the factor-of-3 appearance depends on the accidental proximity")
print(f"  of 4*log10(M_KK) + log10(A_0) + 46.6 to 3*36.")
print()
print(f"  The spectral ratios are structural (Peter-Weyl determined) but are")
print(f"  O(1) corrections that do not generate hierarchies. The hierarchy is")
print(f"  entirely in Lambda = M_KK, which enters as Lambda^4 (two powers of")
print(f"  Lambda^2, i.e., the hierarchy SQUARED, not cubed).")

# ============================================================================
#  SAVE RESULTS
# ============================================================================

results = {
    # Spectral moments
    "A_0": A_0,
    "A_2": A_2,
    "A_4": A_4,
    "A_6": A_6,
    "A_8": A_8,
    "Z_2": Z_2,
    "Z_4": Z_4,

    # Pure spectral ratios
    "R_spec_02": R_spec_02,
    "R_spec_24": R_spec_24,
    "R_spec_46": R_spec_46,
    "R_spec_68": R_spec_68,

    # Physical hierarchy steps
    "log_step_02": log_step_02,
    "log_step_24": log_step_24,
    "log_total_04": log_total_04,

    # CC gaps
    "gap_Planck": gap_from_Planck,
    "gap_spectral_grav": gap_grav,
    "gap_spectral_kern": gap_kern,
    "gap_singlet": gap_singlet,

    # Singlet moments
    "A_0_singlet": float(A_0_singlet),
    "A_2_singlet": A_2_singlet,
    "A_4_singlet": A_4_singlet,
    "R_spec_02_singlet": R_spec_02_singlet,
    "R_spec_24_singlet": R_spec_24_singlet,

    # Decomposition
    "log_prefactor": log_prefactor,
    "log_MKK4": log_MKK4,
    "log_A0": log_A0,
    "log_rho_obs": log_rho_obs,

    # Hierarchy comparisons
    "hierarchy_EW": h_EW,
    "hierarchy_EM": h_EM,
    "hierarchy_KK": h_KK,
    "ratio_gap_over_36": gap_grav / 36.0,
    "ratio_gap_Pl_over_36": gap_from_Planck / 36.0,

    # Peter-Weyl
    "pw_A0": pw_A0,
    "pw_A2": pw_A2,
    "pw_A4": pw_A4,
    "pw_R02": pw_R02,
    "pw_R24": pw_R24,

    # Eigenvalue statistics
    "lam2_mean": lam2_mean,
    "lam4_mean": lam4_mean,
    "lam_max_sq": lam_max_sq,
    "lam_min_sq": lam_min_sq,

    # Gate
    "gate_name": np.array(["CC-HIERARCHY-CUBED-45"]),
    "gate_verdict": np.array([verdict]),
    "gate_info": np.array(["CC gap ~ 3*hierarchy is numerical coincidence, not structural"]),
}

out_path = os.path.join(DATA_DIR, "s45_cc_hierarchy_cubed.npz")
np.savez(out_path, **results)
print(f"\nSaved: {out_path}")
print(f"  {len(results)} fields")
