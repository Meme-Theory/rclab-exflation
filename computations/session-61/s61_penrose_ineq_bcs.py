#!/usr/bin/env python3
"""
s61_penrose_ineq_bcs.py — Penrose Inequality Analog for BCS Sector
===================================================================
Session 61, Wave 5, Task SP-4.

Tests E_BCS >= C * sqrt(S_BCS) as a Penrose inequality analog.

In black hole physics, the Penrose inequality states:
    M_ADM >= sqrt(A / (16*pi*G))
i.e. the total mass-energy bounds below by the horizon area.

BCS analog: |E_BCS(N)| >= C * sqrt(S(N)) where S is an entropy measure
(Bekenstein, sector, or von Neumann).

The (0,0) sector (N=0) is the analog of an extremal black hole if it
SATURATES the bound (equality). Saturation = extremality = BPS-like state.

Gate: PENROSE-INEQ-BCS-61
  PASS if (0,0) saturates within 5%
  FAIL if violates by > 2x
  INFO if holds without saturation

Author: Schwarzschild-Penrose Geometer (S61)
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import M_KK_gravity as M_KK, tau_fold, PI

# =============================================================================
# SECTION 1: Load all data sources
# =============================================================================

stair = np.load(os.path.join(os.path.dirname(__file__), 's60_staircase_ext.npz'), allow_pickle=True)
bek   = np.load(os.path.join(os.path.dirname(__file__), 's60_bekenstein_pw.npz'), allow_pickle=True)
comp  = np.load(os.path.join(os.path.dirname(__file__), 's61_compound_staircase.npz'), allow_pickle=True)

# =============================================================================
# SECTION 2: Extract per-sector quantities (N = 0..4 pairs)
# =============================================================================

# Ground state energies (M_KK units)
E_GS_baseline = stair['E_GS_A']       # N=0..4, baseline BCS
E_GS_compound = comp['E_GS_compound'] # N=0..4, corrected (Penrose+Josephson)

# Entropy measures per N-pair sector
S_Bek_per_N   = comp['S_Bek_per_N']    # Bekenstein entropy per sector
S_sector_per_N = comp['S_sector_per_N'] # log(dim) sector entropy
dim_sector     = comp['dim_sector_per_N'] # Hilbert space dimension

# Level-based quantities (0..5 levels, different indexing)
E_BCS_level = bek['E_BCS_MKK']        # BCS energy by level
S_Bek_level = bek['S_Bekenstein']      # Bekenstein bound by level
S_Bek_Cas   = bek['S_Bek_Casimir']    # Casimir-corrected Bekenstein
S_vN_cons   = bek['S_vN_conservative'] # von Neumann conservative
S_vN_lib    = bek['S_vN_liberal']      # von Neumann liberal
S_max_ent   = bek['S_max_entropy']     # max entropy = log(dim)
n_modes     = bek['n_modes']           # number of modes per level

# S60 total Bekenstein for level 0
S_Bek_total_L0 = float(comp['S_Bek_level0_total'])  # 0.8607

# Single-cell BCS data at fold
eps_fold = stair['eps_fold']  # 8 single-particle levels
V_fold   = stair['V_fold']   # 8x8 pairing matrix

print("=" * 72)
print("PENROSE INEQUALITY ANALOG FOR BCS SECTOR")
print("=" * 72)

# =============================================================================
# SECTION 3: Construct the Penrose inequality — per-sector analysis
# =============================================================================
#
# The Penrose inequality in GR: M >= sqrt(A/(16*pi*G))
# Rewrite: M^2 >= A/(16*pi*G)
#
# BCS analog: E^2 >= C^2 * S
# or equivalently: E >= C * sqrt(S)
#
# For N=0: E_GS = 0, S = 0 (trivial vacuum). This is the "flat space" analog.
# The interesting test is for N >= 1 sectors.
#
# For the LEVEL-based data (multi-cell), level 0 has:
#   |E_BCS| = 0.137 M_KK, S_Bek = 0.861
# This is the (0,0) sector analog at the FABRIC level.

print("\n--- ANALYSIS 1: Level-based (multi-cell, N_levels=0..5) ---\n")

# Use absolute energies
E_abs_level = np.abs(E_BCS_level)

# Test 1: E >= C * sqrt(S_Bek)
# Find minimum C such that inequality holds for ALL levels
print("Test 1: |E_BCS| >= C * sqrt(S_Bekenstein)")
print(f"{'Level':>5} {'|E_BCS|':>12} {'S_Bek':>12} {'sqrt(S)':>12} {'E/sqrt(S)':>12}")
print("-" * 60)

ratios_bek = []
for i in range(len(E_BCS_level)):
    E = E_abs_level[i]  # (local)
    S = S_Bek_level[i]
    sqrtS = np.sqrt(S)
    ratio = E / sqrtS if sqrtS > 0 else np.inf
    ratios_bek.append(ratio)
    print(f"{i:>5d} {E:>12.4f} {S:>12.4f} {sqrtS:>12.4f} {ratio:>12.6f}")

C_opt_bek = min(ratios_bek)
C_opt_bek_idx = np.argmin(ratios_bek)
print(f"\nOptimal C (Bekenstein): {C_opt_bek:.6f}")
print(f"Saturating level: {C_opt_bek_idx}")

# Test 2: E >= C * sqrt(S_Bek_Casimir)
print("\nTest 2: |E_BCS| >= C * sqrt(S_Bek_Casimir)")
print(f"{'Level':>5} {'|E_BCS|':>12} {'S_BekCas':>12} {'sqrt(S)':>12} {'E/sqrt(S)':>12}")
print("-" * 60)

ratios_cas = []
for i in range(len(E_BCS_level)):
    E = E_abs_level[i]  # (local)
    S = S_Bek_Cas[i]
    sqrtS = np.sqrt(S)
    ratio = E / sqrtS if sqrtS > 0 else np.inf
    ratios_cas.append(ratio)
    print(f"{i:>5d} {E:>12.4f} {S:>12.4f} {sqrtS:>12.4f} {ratio:>12.6f}")

C_opt_cas = min(ratios_cas)
C_opt_cas_idx = np.argmin(ratios_cas)
print(f"\nOptimal C (Casimir): {C_opt_cas:.6f}")
print(f"Saturating level: {C_opt_cas_idx}")

# Test 3: E >= C * sqrt(S_vN_conservative)
print("\nTest 3: |E_BCS| >= C * sqrt(S_vN_conservative)")
print(f"{'Level':>5} {'|E_BCS|':>12} {'S_vN':>12} {'sqrt(S)':>12} {'E/sqrt(S)':>12}")
print("-" * 60)

ratios_vN = []
for i in range(len(E_BCS_level)):
    E = E_abs_level[i]  # (local)
    S = S_vN_cons[i]
    sqrtS = np.sqrt(S)
    ratio = E / sqrtS if sqrtS > 0 else np.inf
    ratios_vN.append(ratio)
    print(f"{i:>5d} {E:>12.4f} {S:>12.4f} {sqrtS:>12.4f} {ratio:>12.6f}")

C_opt_vN = min(ratios_vN)
C_opt_vN_idx = np.argmin(ratios_vN)
print(f"\nOptimal C (vN conservative): {C_opt_vN:.6f}")
print(f"Saturating level: {C_opt_vN_idx}")

# =============================================================================
# SECTION 4: Per-sector analysis (N=0..4 pairs, single cell)
# =============================================================================

print("\n--- ANALYSIS 2: Per-sector (single cell, N=0..4 pairs) ---\n")

# For N=0: E=0, S=0. Both zero => ratio undefined (0/0).
# This is the vacuum = flat spacetime analog. Trivially saturated.
# The nontrivial test starts at N=1.

# Use baseline energies (not compound-corrected, which shifted N=0 to E=0 exactly)
E_baseline = E_GS_baseline  # [0, -0.04642, 0.2676, 0.8749, 1.8502]
E_compound = E_GS_compound  # [0, 0.18202, 0.4496, 0.7981, 1.8898]

print("Baseline staircase (E_GS_A):")
print(f"{'N':>3} {'E_GS':>12} {'|E_GS|':>12} {'S_Bek':>12} {'S_sector':>12} {'dim':>6}")
print("-" * 60)
for i in range(5):
    print(f"{i:>3d} {E_baseline[i]:>12.6f} {abs(E_baseline[i]):>12.6f} "
          f"{S_Bek_per_N[i]:>12.6f} {S_sector_per_N[i]:>12.6f} {dim_sector[i]:>6d}")

print("\nCompound staircase (corrected):")
print(f"{'N':>3} {'E_GS':>12} {'|E_GS|':>12} {'S_Bek':>12} {'S_sector':>12} {'dim':>6}")
print("-" * 60)
for i in range(5):
    print(f"{i:>3d} {E_compound[i]:>12.6f} {abs(E_compound[i]):>12.6f} "
          f"{S_Bek_per_N[i]:>12.6f} {S_sector_per_N[i]:>12.6f} {dim_sector[i]:>6d}")

# For per-sector Penrose inequality, use S_sector (= log(dim)) as the entropy
# This is the microcanonical entropy: log of the number of states at that N
print("\nPenrose inequality test: |E_GS| >= C * sqrt(S_sector)")
print("(Using baseline staircase, N>=1)")
print(f"{'N':>3} {'|E_GS|':>12} {'sqrt(S_sec)':>12} {'ratio':>12}")
print("-" * 45)

ratios_sector_base = []
for i in range(1, 5):  # Skip N=0 (0/0)
    E = abs(E_baseline[i])
    S = S_sector_per_N[i]
    sqrtS = np.sqrt(S)
    ratio = E / sqrtS
    ratios_sector_base.append(ratio)
    print(f"{i:>3d} {E:>12.6f} {sqrtS:>12.6f} {ratio:>12.6f}")

C_opt_sector = min(ratios_sector_base)
C_opt_sector_idx = np.argmin(ratios_sector_base) + 1  # offset for N=0 skip
print(f"\nOptimal C (sector, baseline): {C_opt_sector:.6f}")
print(f"Saturating N: {C_opt_sector_idx}")

# =============================================================================
# SECTION 5: The (0,0) sector — extremality test
# =============================================================================

print("\n--- ANALYSIS 3: (0,0) Sector Extremality ---\n")

# The (0,0) sector at the FABRIC level has:
#   |E_BCS| = 0.13698 M_KK (level 0, from s60_bekenstein_pw.npz)
#   S_Bek = 0.86067 (Bekenstein bound)
#
# At the SINGLE-CELL level: N=0 has E=0, S=0 (trivially extremal).
# The meaningful test is the level-0 fabric sector.

E_00 = E_abs_level[0]  # |E_BCS(level 0)| = 0.13698
S_00_bek = S_Bek_level[0]  # S_Bek(level 0) = 0.86067

print(f"(0,0) sector (fabric level 0):")
print(f"  |E_BCS| = {E_00:.6f} M_KK")
print(f"  S_Bek   = {S_00_bek:.6f}")
print(f"  sqrt(S) = {np.sqrt(S_00_bek):.6f}")
print(f"  E/sqrt(S) = {E_00/np.sqrt(S_00_bek):.6f}")

# Check saturation with each optimal C
print(f"\nSaturation test with C_opt(Bek) = {C_opt_bek:.6f}:")
sat_bek = E_00 / (C_opt_bek * np.sqrt(S_00_bek))
print(f"  E / (C*sqrt(S)) = {sat_bek:.6f}")
print(f"  Deviation from saturation: {abs(sat_bek - 1)*100:.2f}%")

print(f"\nSaturation test with C_opt(Casimir) = {C_opt_cas:.6f}:")
S_00_cas = S_Bek_Cas[0]
sat_cas = E_00 / (C_opt_cas * np.sqrt(S_00_cas))
print(f"  E / (C*sqrt(S)) = {sat_cas:.6f}")
print(f"  Deviation from saturation: {abs(sat_cas - 1)*100:.2f}%")

print(f"\nSaturation test with C_opt(vN) = {C_opt_vN:.6f}:")
S_00_vN = S_vN_cons[0]
sat_vN = E_00 / (C_opt_vN * np.sqrt(S_00_vN))
print(f"  E / (C*sqrt(S)) = {sat_vN:.6f}")
print(f"  Deviation from saturation: {abs(sat_vN - 1)*100:.2f}%")

# =============================================================================
# SECTION 6: Power-law structure — is the inequality E ~ S^alpha?
# =============================================================================

print("\n--- ANALYSIS 4: Power-law structure ---\n")

# Fit log|E| = alpha * log(S) + log(A) for level data
# Using levels 0..5 with Bekenstein entropy
mask = (E_abs_level > 0) & (S_Bek_level > 0)
logE = np.log(E_abs_level[mask])
logS = np.log(S_Bek_level[mask])

if len(logE) >= 2:
    # Linear regression: logE = alpha * logS + logA
    coeffs = np.polyfit(logS, logE, 1)
    alpha_fit = coeffs[0]
    A_fit = np.exp(coeffs[1])

    # Residuals
    logE_pred = np.polyval(coeffs, logS)
    residuals = logE - logE_pred
    R2 = 1 - np.sum(residuals**2) / np.sum((logE - np.mean(logE))**2)

    print(f"Power-law fit: |E| = {A_fit:.6f} * S_Bek^{alpha_fit:.6f}")
    print(f"R^2 = {R2:.8f}")
    print(f"If alpha = 0.5 exactly, this IS the Penrose inequality.")
    print(f"Measured alpha = {alpha_fit:.6f}")
    print(f"Deviation from 0.5: {abs(alpha_fit - 0.5):.6f} ({abs(alpha_fit-0.5)/0.5*100:.2f}%)")

# Same fit with Casimir entropy
logS_cas = np.log(S_Bek_Cas[mask])
coeffs_cas = np.polyfit(logS_cas, logE, 1)
alpha_cas = coeffs_cas[0]
A_cas = np.exp(coeffs_cas[1])
logE_pred_cas = np.polyval(coeffs_cas, logS_cas)
res_cas = logE - logE_pred_cas
R2_cas = 1 - np.sum(res_cas**2) / np.sum((logE - np.mean(logE))**2)
print(f"\nCasimir fit: |E| = {A_cas:.6f} * S_Cas^{alpha_cas:.6f}, R^2={R2_cas:.8f}")

# Same fit with vN entropy
logS_vN = np.log(S_vN_cons[mask])
coeffs_vN = np.polyfit(logS_vN, logE, 1)
alpha_vN = coeffs_vN[0]
A_vN = np.exp(coeffs_vN[1])
logE_pred_vN = np.polyval(coeffs_vN, logS_vN)
res_vN = logE - logE_pred_vN
R2_vN = 1 - np.sum(res_vN**2) / np.sum((logE - np.mean(logE))**2)
print(f"vN fit: |E| = {A_vN:.6f} * S_vN^{alpha_vN:.6f}, R^2={R2_vN:.8f}")

# =============================================================================
# SECTION 7: Generalized Penrose inequality E^2 >= f(S)
# =============================================================================

print("\n--- ANALYSIS 5: Generalized bound E^2 vs S ---\n")

# Classical Penrose: M^2 >= A/(16*pi*G) where S = A/(4*G)
# So M^2 >= S/(4*pi). Test: E^2 >= S/(4*pi) analog.

print("Test: E^2 vs S/(4*pi) analog")
print(f"{'Level':>5} {'E^2':>14} {'S_Bek/(4pi)':>14} {'ratio':>10}")
print("-" * 50)

ratios_sq = []
for i in range(len(E_BCS_level)):
    E2 = E_abs_level[i]**2
    S4pi = S_Bek_level[i] / (4 * PI)
    ratio = E2 / S4pi if S4pi > 0 else np.inf
    ratios_sq.append(ratio)
    print(f"{i:>5d} {E2:>14.4f} {S4pi:>14.4f} {ratio:>10.4f}")

C_sq_opt = min(ratios_sq)
print(f"\nMinimum E^2 / (S/(4pi)): {C_sq_opt:.6f}")
print(f"Saturating level: {np.argmin(ratios_sq)}")

# Check: E^2 >= C_sq * S with optimized C_sq
C_sq = min(E_abs_level[i]**2 / S_Bek_level[i] for i in range(len(E_BCS_level)))
print(f"\nOptimal C_sq (E^2 >= C_sq * S): {C_sq:.8f}")
sat_00_sq = E_00**2 / (C_sq * S_00_bek) if C_sq > 0 else np.inf
print(f"(0,0) saturation (E^2 form): E^2/(C_sq*S) = {sat_00_sq:.6f}")

# =============================================================================
# SECTION 8: The n_modes scaling — area analog
# =============================================================================

print("\n--- ANALYSIS 6: Area analog (n_modes as horizon area) ---\n")

# In GR: A = 4*pi*r_+^2. The "area" of the BCS horizon could be n_modes
# (number of pairing channels = "surface area" of the condensate).
# Test: E >= C * sqrt(n_modes)

print("Test: |E| >= C * sqrt(n_modes)")
print(f"{'Level':>5} {'|E|':>12} {'n_modes':>10} {'sqrt(n)':>10} {'E/sqrt(n)':>12}")
print("-" * 55)

ratios_nmodes = []
for i in range(len(E_BCS_level)):
    E = E_abs_level[i]  # (local)
    n = n_modes[i]
    sqrtn = np.sqrt(n)
    ratio = E / sqrtn
    ratios_nmodes.append(ratio)
    print(f"{i:>5d} {E:>12.4f} {n:>10d} {sqrtn:>10.4f} {ratio:>12.6f}")

C_nmodes = min(ratios_nmodes)
C_nmodes_idx = np.argmin(ratios_nmodes)
print(f"\nOptimal C (n_modes): {C_nmodes:.6f}")
print(f"Saturating level: {C_nmodes_idx}")

# (0,0) saturation with n_modes
sat_00_nmodes = E_00 / (C_nmodes * np.sqrt(n_modes[0]))
print(f"(0,0) saturation: E/(C*sqrt(n)) = {sat_00_nmodes:.6f}")
print(f"Deviation: {abs(sat_00_nmodes - 1)*100:.2f}%")

# =============================================================================
# SECTION 9: Summary table
# =============================================================================

print("\n" + "=" * 72)
print("SUMMARY: PENROSE INEQUALITY ANALOGS")
print("=" * 72)

print(f"\n{'Entropy measure':<25} {'C_opt':>10} {'Saturates at':>15} {'alpha (PL)':>12} {'R^2':>10}")
print("-" * 75)
print(f"{'S_Bekenstein':<25} {C_opt_bek:>10.6f} {'level '+str(C_opt_bek_idx):>15} {alpha_fit:>12.6f} {R2:>10.8f}")
print(f"{'S_Bek_Casimir':<25} {C_opt_cas:>10.6f} {'level '+str(C_opt_cas_idx):>15} {alpha_cas:>12.6f} {R2_cas:>10.8f}")
print(f"{'S_vN_conservative':<25} {C_opt_vN:>10.6f} {'level '+str(C_opt_vN_idx):>15} {alpha_vN:>12.6f} {R2_vN:>10.8f}")
print(f"{'n_modes (area analog)':<25} {C_nmodes:>10.6f} {'level '+str(C_nmodes_idx):>15} {'N/A':>12} {'N/A':>10}")

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: PENROSE-INEQ-BCS-61")
print("=" * 72)

# The (0,0) sector at single-cell level: N=0 has E=0, S=0 => 0/0 (trivially extremal)
# The (0,0) sector at fabric level (level 0):
#   - With S_Bek: E/sqrt(S) = ratios_bek[0], optimal C from some other level
#   - Question: does level 0 saturate?

# Level 0 saturates if it achieves the MINIMUM ratio (i.e., it is the tightest constraint)
level0_is_saturator_bek = (C_opt_bek_idx == 0)
level0_is_saturator_cas = (C_opt_cas_idx == 0)
level0_is_saturator_vN = (C_opt_vN_idx == 0)
level0_is_saturator_nmodes = (C_nmodes_idx == 0)

# Even if not the exact saturator, check how close to saturation
dev_bek = abs(sat_bek - 1) * 100  # percent
dev_cas = abs(sat_cas - 1) * 100
dev_vN  = abs(sat_vN - 1) * 100
dev_nmodes = abs(sat_00_nmodes - 1) * 100

print(f"\n(0,0) sector saturation deviations:")
print(f"  S_Bekenstein:      {dev_bek:.2f}% (saturator: level {C_opt_bek_idx})")
print(f"  S_Bek_Casimir:     {dev_cas:.2f}% (saturator: level {C_opt_cas_idx})")
print(f"  S_vN_conservative: {dev_vN:.2f}% (saturator: level {C_opt_vN_idx})")
print(f"  n_modes:           {dev_nmodes:.2f}% (saturator: level {C_nmodes_idx})")

# Power law exponent: Penrose requires alpha = 0.5
dev_alpha_bek = abs(alpha_fit - 0.5) / 0.5 * 100
dev_alpha_vN  = abs(alpha_vN - 0.5) / 0.5 * 100

print(f"\nPower-law exponent (Penrose requires alpha=0.5):")
print(f"  S_Bekenstein: alpha = {alpha_fit:.6f} (dev {dev_alpha_bek:.1f}%)")
print(f"  S_Casimir:    alpha = {alpha_cas:.6f}")
print(f"  S_vN:         alpha = {alpha_vN:.6f} (dev {dev_alpha_vN:.1f}%)")

# Gate logic — STRUCTURAL ANALYSIS
#
# The saturation at level 0 is TAUTOLOGICAL for ALL entropy measures because:
# 1. S_Bek = 2*pi*|E|*R => E/sqrt(S) = sqrt(E/(2*pi*R)), monotone in E.
#    Level 0 has smallest E => smallest ratio => always saturates. QED.
# 2. S_max = log(dim) ~ n_modes. E ~ n_modes^2.49. So E/sqrt(S) ~ n^1.99.
#    Monotonically increasing => level 0 always saturates. QED.
# 3. S_vN ~ n_modes^1 (estimated). Same argument. Level 0 wins by floor.
#
# In GR, the Penrose inequality is nontrivial because M_ADM (at infinity) is
# independent of A (at horizon). Here, S_Bek is CONSTRUCTED from E, and S_max
# grows slower than E for all N. No independent "area" vs "mass" tension exists.
#
# Moreover, the (0,0) single-cell sector has E=0, S=0, dim=1.
# This is flat Minkowski space, not an extremal black hole.
# The level-0 fabric sector has S_max/S_Bek = 6.44 (SUPER-Bekenstein from S60).
# Super-entropic = sub-extremal in GR terms.
#
# VERDICT: The inequality HOLDS everywhere but is structurally tautological.
# Level 0 "saturates" by being the floor of a monotone sequence.
# This is not extremality.

any_saturates = any([level0_is_saturator_bek, level0_is_saturator_cas,
                     level0_is_saturator_vN, level0_is_saturator_nmodes])
min_dev = min(dev_bek, dev_cas, dev_vN, dev_nmodes)
max_violation = max(sat_bek, sat_cas, sat_vN, sat_00_nmodes)

# The inequality holds. Level 0 saturates. But it is tautological.
# E ~ N^2.49 >> sqrt(S) ~ N^0.5-1.0 for all measures.
# alpha_Bek = 1.000 (exact, S_Bek linear in E).
# alpha_vN = 2.729 (super-Penrose).
# Neither is 0.5. The Penrose form E >= C*sqrt(S) does not capture
# the BCS energy-entropy relationship.

verdict = "FAIL"
reason = (f"Inequality holds but saturation is TAUTOLOGICAL. "
          f"S_Bek linear in E (alpha=1.000, should be 0.5). "
          f"Level 0 saturates by floor effect (E~N^{float(bek['alpha_E']):.2f} >> sqrt(S)). "
          f"(0,0) single-cell: E=0,S=0 (vacuum, not extremal). "
          f"Level-0 fabric: S_max/S_Bek=6.44 (super-Bekenstein = sub-extremal).")

print(f"\n*** VERDICT: {verdict} ***")
print(f"*** REASON: {reason} ***")

# Additional structural analysis
print(f"\n--- Structural Analysis ---")
print(f"BCS energy scaling: |E| ~ N^{float(bek['alpha_E']):.4f}")
print(f"Bekenstein entropy: S_Bek ~ |E|*R (linear in E)")
print(f"Combined: S_Bek ~ N^{float(bek['alpha_E']):.4f}")
print(f"Penrose requires: E ~ S^0.5, i.e., S ~ E^2 ~ N^{2*float(bek['alpha_E']):.4f}")
print(f"Actual: S_Bek ~ E^1 ~ N^{float(bek['alpha_E']):.4f}")
print(f"The exponent mismatch ({alpha_fit:.4f} vs 0.500) is structural:")
print(f"  S_Bek = 2*pi*|E|*R scales linearly in E, not quadratically.")
print(f"  The Penrose inequality E >= sqrt(S) requires S ~ E^2.")
print(f"  Bekenstein bound S = 2*pi*E*R gives S ~ E^1 (for fixed R).")
print(f"  This means the correct comparison is E >= S (linear), not E >= sqrt(S).")
print(f"  => The 'Penrose inequality' for Bekenstein entropy is TRIVIALLY satisfied")
print(f"     because S_Bek is constructed from E itself.")

# =============================================================================
# SECTION 11: Save results
# =============================================================================

np.savez(
    os.path.join(os.path.dirname(__file__), 's61_penrose_ineq_bcs.npz'),
    # Level-based data
    E_abs_level=E_abs_level,
    S_Bek_level=S_Bek_level,
    S_Bek_Cas=S_Bek_Cas,
    S_vN_cons=S_vN_cons,
    n_modes=n_modes,
    # Optimal constants
    C_opt_bek=C_opt_bek,
    C_opt_cas=C_opt_cas,
    C_opt_vN=C_opt_vN,
    C_nmodes=C_nmodes,
    # Power-law fits
    alpha_bek=alpha_fit,
    alpha_cas=alpha_cas,
    alpha_vN=alpha_vN,
    A_bek=A_fit,
    A_cas=A_cas,
    A_vN=A_vN,
    R2_bek=R2,
    R2_cas=R2_cas,
    R2_vN=R2_vN,
    # Saturation ratios
    sat_00_bek=sat_bek,
    sat_00_cas=sat_cas,
    sat_00_vN=sat_vN,
    sat_00_nmodes=sat_00_nmodes,
    # Per-level ratios
    ratios_bek=np.array(ratios_bek),
    ratios_cas=np.array(ratios_cas),
    ratios_vN=np.array(ratios_vN),
    ratios_nmodes=np.array(ratios_nmodes),
    # Per-sector data
    E_baseline=E_baseline,
    E_compound=E_compound,
    S_Bek_per_N=S_Bek_per_N,
    S_sector_per_N=S_sector_per_N,
    dim_sector=dim_sector,
    # Gate
    gate_name='PENROSE-INEQ-BCS-61',
    gate_verdict=verdict,
    gate_reason=reason,
)

print(f"\nSaved: computations/session-61/s61_penrose_ineq_bcs.npz")
print(f"Gate: {verdict}")
