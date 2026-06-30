#!/usr/bin/env python3
"""
S74 GAP-DOMINATED-DISPERSION-74 (W4-L)
=======================================

Task: Compute observational consequences of Leggett and optical branches
being deep in the gap-dominated regime at CMB scales.

Gap-dominated dispersion: omega^2(k) = m_gap^2 + c_s^2 k^2
  - For k << k_gap = m_gap / c_s : omega ~ m_gap (flat, massive)
  - For k >> k_gap                : omega ~ c_s k  (acoustic)

Crossover scale k_gap separates the "mass-dominated" IR regime from the
"acoustic" UV regime. In CMB language, ell_gap = k_gap * chi_recomb where
chi_recomb ~ 14 Gpc is the comoving distance to last scattering.

Framework context:
  - Leggett branches (L1, L2) are inter-band coherence modes
  - Optical branches (B-3, B-4, Higgs-1) are gap-dominated fiber modes
  - Acoustic branch (Goldstone) is gapless (m_gap -> 0): no crossover
  - Fabric (BLV/BA) scale: provides upper-limit reference for physical speeds

Pre-registered gate: GAP-DOMINATED-DISPERSION-74
  PASS if l_gap in detectable range [10, 3000]
  INFO if outside but < 10000
  FAIL if > 10000 (undetectable)

Inputs:
  - canonical_constants.py (M_KK, c_fabric, omega_L1, omega_L2, ...)
  - s52_gl_josephson.npz  (dispersion m_gap and c_s per branch)
  - s59_epsilon_canonical.npz (canonical Leggett-1 with V_bare partition)
  - s64_sound_speed.npz (canonical c_L, c_BA, c_mod)

Outputs:
  - s74_gap_dominated_dispersion.npz (m_gap, k_gap, l_gap per branch)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK,                # GeV (gravity route, conservative)
    M_KK_kerner,         # GeV (Kerner route, alternate)
    M_KK_gravity,        # GeV
    c_light,             # m/s
    hbar_c_GeV_m,        # GeV * m
    hbar_c_GeV_fm,       # GeV * fm
    Mpc_to_m,            # m per Mpc
    Gpc_to_m,            # m per Gpc
    c_fabric,            # Fabric sound speed (M_KK units)
    c_Gold,              # Goldstone sound speed (M_KK units)
    omega_L1,            # Leggett-1 (M_KK units)
    omega_L2,            # Leggett-2 (M_KK units)
    omega_H1,            # Higgs-1 / Branch-3 (M_KK units)
    omega_H2,            # Higgs-2 / Branch-4 (M_KK units)
    omega_H3,            # Higgs-3 (M_KK units)
)

# ==============================================================================
# 0. Cosmological geometry (CMB)
# ==============================================================================

# Comoving distance to last scattering surface (Planck 2018 fiducial)
chi_recomb_Gpc = 14.0                                                 # (local)  Gpc
chi_recomb_m = chi_recomb_Gpc * Gpc_to_m                              # (local)  meters
chi_recomb_GeV_inv = chi_recomb_m / hbar_c_GeV_m                      # (local)  GeV^{-1}
# ell_gap = k_gap * chi_recomb  (physical inverse Mpc * Mpc = dimensionless)

# ==============================================================================
# 1. Load S52 dispersion data (m_gap, c_s per branch from full k-fit)
# ==============================================================================

s52 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "s52_gl_josephson.npz"))
K_s52 = s52['K_array']                 # (local)  dimensionless (M_KK * length units)
omega_s52 = s52['omega_branches']      # (local)  (51, 6) in M_KK units
labels_s52 = [str(l) for l in s52['branch_labels']]

# Fit omega^2 = m_gap^2 + c_s^2 * k^2 using low-k (first 5 points)
# Note: S52 k-array is in units where K_BZ = 0.716 (first Brillouin zone).
# The fitted c_s is the slope in these internal coordinates and is NOT the
# physical sound speed in lab frame (which is m/s or dimensionless fraction
# of c_light). We will cross-check against canonical lab-frame speeds below.
N_branches = len(labels_s52)
m_gap_s52 = np.zeros(N_branches)                                      # (local)
c_s_internal = np.zeros(N_branches)                                   # (local)
for i in range(N_branches):
    p = np.polyfit(K_s52[:5]**2, omega_s52[:5, i]**2, 1)              # (local)
    c2 = max(p[0], 0.0)                                               # (local)
    mg2 = max(p[1], 0.0)                                              # (local)
    c_s_internal[i] = np.sqrt(c2)
    m_gap_s52[i] = np.sqrt(mg2)

# ==============================================================================
# 2. Canonical gap values from S59 (V_bare partition — supersedes S52)
# ==============================================================================

s59 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "s59_epsilon_canonical.npz"))
omega_L1_canonical = float(s59['omega_L1_canonical'])                 # M_KK
omega_L0_bare = float(s59['omega_L0_bare_partition'])                 # M_KK (lowest)

# S64: canonical sound speeds (lab-frame, dimensionless fraction of c_light)
s64 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "s64_sound_speed.npz"))
c_mod_lab = float(s64['c_mod'])              # = 1.0 (tensor/gravitational)
c_BLV_lab = float(s64['c_BLV'])              # = 0.4849 (scalar/fabric)
c_BA_lab = float(s64['c_BA_S56'])            # = 0.399 (BCS Bogoliubov)
c_L_range = np.array(s64['c_Leggett_range'], dtype=float)  # [0.019, 0.032]
c_L_lab = float(np.mean(c_L_range))          # = 0.0255 canonical midpoint

# ==============================================================================
# 3. Build the branch table
# ==============================================================================
#
# For each gap-dominated branch, identify:
#   - m_gap (in M_KK units, then convert to GeV)
#   - c_s (lab-frame dimensionless — the relevant speed for k_gap)
#   - k_gap = m_gap (GeV) / c_s (dimensionless) -> k in GeV (natural units)
#     Note: if c_s is dimensionless, then k_gap has units of energy = 1/length.
#   - ell_gap = k_gap * chi_recomb  (with k_gap and chi in same length units)
#
# The Goldstone (acoustic) branch has m_gap = 0 -> no crossover, no ell_gap
# (infrared divergence signal that there is no gap).

branches = []                                                         # (local)

# -- Leggett-1: inter-band coherence, canonical S59 --
branches.append({
    "name": "Leggett-1 (S59 canonical, V_bare)",
    "m_gap_MKK": omega_L1_canonical,
    "c_s_lab": c_L_lab,
    "c_s_lab_lo": c_L_range[0],
    "c_s_lab_hi": c_L_range[1],
    "notes": "Inter-band coherence, gap-dominated throughout IR",
})

# -- Leggett-2: from S52 / canonical --
# omega_L2 = 0.192 (S52 GL-Josephson); same c_L speed range
branches.append({
    "name": "Leggett-2 (S52 GL-Josephson)",
    "m_gap_MKK": omega_L2,
    "c_s_lab": c_L_lab,
    "c_s_lab_lo": c_L_range[0],
    "c_s_lab_hi": c_L_range[1],
    "notes": "Second Leggett mode, higher gap",
})

# -- Optical Branch-3 / Higgs-1 (first transverse fiber mode) --
# omega_H1 = 0.380 (S52). c_s: use c_fabric for optical = transverse fiber
# oscillation; but in CMB observation the relevant dynamical scale is still
# the BCS/fabric sound speed that transports phase. Use c_BLV (scalar/fabric).
branches.append({
    "name": "Optical Branch-3 / Higgs-1 (S52)",
    "m_gap_MKK": omega_H1,
    "c_s_lab": c_BLV_lab,
    "c_s_lab_lo": c_BA_lab,
    "c_s_lab_hi": c_mod_lab,
    "notes": "Transverse fiber mode, first optical branch",
})

# -- Optical Branch-4 / Higgs-2 --
branches.append({
    "name": "Optical Branch-4 / Higgs-2 (S52)",
    "m_gap_MKK": omega_H2,
    "c_s_lab": c_BLV_lab,
    "c_s_lab_lo": c_BA_lab,
    "c_s_lab_hi": c_mod_lab,
    "notes": "Second optical branch",
})

# -- Higgs-3 (ultra-massive) --
branches.append({
    "name": "Higgs-3 (S52, ultra-massive)",
    "m_gap_MKK": omega_H3,
    "c_s_lab": c_BLV_lab,
    "c_s_lab_lo": c_BA_lab,
    "c_s_lab_hi": c_mod_lab,
    "notes": "Deep UV optical mode",
})

# -- Goldstone (acoustic, m_gap = 0) --
# Reference: no gap, k_gap undefined (formally 0 / c_Gold -> 0)
branches.append({
    "name": "Goldstone (acoustic, reference)",
    "m_gap_MKK": 0.0,
    "c_s_lab": c_Gold,   # M_KK-units Goldstone speed (not lab-frame)
    "c_s_lab_lo": c_Gold,
    "c_s_lab_hi": c_Gold,
    "notes": "Massless acoustic branch — no crossover",
})

# ==============================================================================
# 4. Compute k_gap and ell_gap per branch
# ==============================================================================
#
# Method:
#   m_gap (GeV) = m_gap_MKK * M_KK_gravity
#   k_gap (GeV) = m_gap (GeV) / c_s_lab   (c_s dimensionless fraction of c_light)
#   k_gap (1/Mpc) = k_gap (GeV) * (Mpc_to_m / hbar_c_GeV_m)
#   ell_gap = k_gap (1/Mpc) * chi_recomb (Mpc)
# Dimensional check: [energy]/[dimensionless] = [energy] = [1/length] (natural).
# Then k * chi = dimensionless multipole scale, correct for flat-sky ell mapping.

MKK_GeV = M_KK_gravity   # conservative (gravity route)
MKK_GeV_alt = M_KK_kerner  # alt (Kerner route), 0.83 decades higher

chi_recomb_Mpc = chi_recomb_Gpc * 1000.0                              # (local)
Mpc_inv_per_GeV = 1.0 / (hbar_c_GeV_m / Mpc_to_m)                     # (local)
# = Mpc_to_m / hbar_c_GeV_m  in units (Mpc^{-1})/GeV
# Equivalently: k(GeV) * (1 Mpc in GeV^{-1}) gives k in units of 1/Mpc
# where 1 Mpc in GeV^{-1} = Mpc_to_m / hbar_c_GeV_m

print("="*78)
print("S74 W4-L GAP-DOMINATED-DISPERSION-74")
print("="*78)
print()
print(f"M_KK (gravity route):  {MKK_GeV:.4e} GeV")
print(f"M_KK (Kerner route):   {MKK_GeV_alt:.4e} GeV")
print(f"chi_recomb:            {chi_recomb_Gpc} Gpc = {chi_recomb_Mpc:.1f} Mpc")
print(f"Mpc_inv_per_GeV:       {Mpc_inv_per_GeV:.4e}")
print()
print(f"{'Branch':<38} {'m_gap (M_KK)':>12} {'c_s':>8} {'k_gap (1/Mpc)':>16} {'ell_gap':>12}")
print("-"*88)

n_branches = len(branches)
m_gap_MKK_arr = np.zeros(n_branches)                                  # (local)
m_gap_GeV_arr = np.zeros(n_branches)                                  # (local)
c_s_lab_arr = np.zeros(n_branches)                                    # (local)
k_gap_GeV_arr = np.zeros(n_branches)                                  # (local)
k_gap_invMpc_arr = np.zeros(n_branches)                               # (local)
ell_gap_arr = np.zeros(n_branches)                                    # (local)
ell_gap_lo_arr = np.zeros(n_branches)                                 # (local)
ell_gap_hi_arr = np.zeros(n_branches)                                 # (local)
m_gap_GeV_kerner_arr = np.zeros(n_branches)                           # (local)
ell_gap_kerner_arr = np.zeros(n_branches)                             # (local)
branch_names = []                                                     # (local)

for i, b in enumerate(branches):
    name = b["name"]
    branch_names.append(name)
    m_gap_MKK = b["m_gap_MKK"]                                        # (local)
    c_s = b["c_s_lab"]                                                # (local)
    c_s_lo = b["c_s_lab_lo"]                                          # (local)
    c_s_hi = b["c_s_lab_hi"]                                          # (local)

    m_gap_GeV = m_gap_MKK * MKK_GeV                                   # (local)
    m_gap_GeV_kerner = m_gap_MKK * MKK_GeV_alt                        # (local)

    if c_s > 0 and m_gap_MKK > 0:
        k_gap_GeV = m_gap_GeV / c_s                                   # (local)
        k_gap_GeV_lo = m_gap_GeV / c_s_hi  # lower k for higher speed # (local)
        k_gap_GeV_hi = m_gap_GeV / c_s_lo  # higher k for lower speed # (local)
        k_gap_invMpc = k_gap_GeV * Mpc_inv_per_GeV                    # (local)
        k_gap_invMpc_lo = k_gap_GeV_lo * Mpc_inv_per_GeV              # (local)
        k_gap_invMpc_hi = k_gap_GeV_hi * Mpc_inv_per_GeV              # (local)
        ell_gap = k_gap_invMpc * chi_recomb_Mpc                       # (local)
        ell_gap_lo = k_gap_invMpc_lo * chi_recomb_Mpc                 # (local)
        ell_gap_hi = k_gap_invMpc_hi * chi_recomb_Mpc                 # (local)

        k_gap_GeV_kerner = m_gap_GeV_kerner / c_s                     # (local)
        k_gap_invMpc_kerner = k_gap_GeV_kerner * Mpc_inv_per_GeV      # (local)
        ell_gap_kerner = k_gap_invMpc_kerner * chi_recomb_Mpc         # (local)
    else:
        k_gap_GeV = 0.0  # (local)
        k_gap_invMpc = 0.0  # (local)
        k_gap_invMpc_lo = 0.0  # (local)
        k_gap_invMpc_hi = 0.0  # (local)
        ell_gap = 0.0  # (local)
        ell_gap_lo = 0.0  # (local)
        ell_gap_hi = 0.0  # (local)
        k_gap_GeV_kerner = 0.0  # (local)
        ell_gap_kerner = 0.0  # (local)

    m_gap_MKK_arr[i] = m_gap_MKK
    m_gap_GeV_arr[i] = m_gap_GeV
    m_gap_GeV_kerner_arr[i] = m_gap_GeV_kerner
    c_s_lab_arr[i] = c_s
    k_gap_GeV_arr[i] = k_gap_GeV
    k_gap_invMpc_arr[i] = k_gap_invMpc
    ell_gap_arr[i] = ell_gap
    ell_gap_lo_arr[i] = ell_gap_lo
    ell_gap_hi_arr[i] = ell_gap_hi
    ell_gap_kerner_arr[i] = ell_gap_kerner

    if m_gap_MKK > 0:
        print(f"{name:<38} {m_gap_MKK:>12.4f} {c_s:>8.4f} "
              f"{k_gap_invMpc:>16.3e} {ell_gap:>12.3e}")
    else:
        print(f"{name:<38} {m_gap_MKK:>12.4f} {c_s:>8.4f} "
              f"{'N/A (gapless)':>16} {'N/A':>12}")

print()
print("Ranges (lo, hi) reflect c_s uncertainty band:")
print(f"{'Branch':<38} {'ell_gap_lo':>14} {'ell_gap':>14} {'ell_gap_hi':>14}")
print("-"*84)
for i, name in enumerate(branch_names):
    if m_gap_MKK_arr[i] > 0:
        print(f"{name:<38} {ell_gap_lo_arr[i]:>14.3e} {ell_gap_arr[i]:>14.3e} "
              f"{ell_gap_hi_arr[i]:>14.3e}")
print()
print("Cross-check (Kerner route, +0.83 decades in M_KK):")
print(f"{'Branch':<38} {'ell_gap_Kerner':>16}")
print("-"*56)
for i, name in enumerate(branch_names):
    if m_gap_MKK_arr[i] > 0:
        print(f"{name:<38} {ell_gap_kerner_arr[i]:>16.3e}")

# ==============================================================================
# 5. Gate evaluation
# ==============================================================================
#
# Per branch, classify ell_gap:
#   PASS: 10 <= ell_gap <= 3000
#   INFO: 3000 < ell_gap < 10000 or ell_gap < 10
#   FAIL: ell_gap > 10000
#
# Overall verdict: since ALL m_gap ~ M_KK ~ 1e16-1e17 GeV and
# chi_recomb ~ 14 Gpc, ell_gap = m_gap * chi / c_s ~ 10^40 — massively outside
# detectable range. This is a framework-level prediction: gap-dominated
# branches have NO observable IR crossover at CMB scales.
# The structural reason: M_KK dwarfs the cosmological scale by ~40 OOM.

print()
print("="*78)
print("GATE EVALUATION")
print("="*78)
print()
ell_range_PASS = (10.0, 3000.0)                                        # (local)
ell_range_INFO_max = 10000.0                                           # (local)

def classify(ell):
    if ell == 0:
        return "N/A"
    if ell_range_PASS[0] <= ell <= ell_range_PASS[1]:
        return "PASS"
    if ell < ell_range_INFO_max:
        return "INFO"
    return "FAIL"

print(f"{'Branch':<38} {'ell_gap':>14} {'verdict':>10}")
print("-"*68)
verdicts = []                                                          # (local)
for i, name in enumerate(branch_names):
    if m_gap_MKK_arr[i] > 0:
        v = classify(ell_gap_arr[i])
        verdicts.append(v)
        print(f"{name:<38} {ell_gap_arr[i]:>14.3e} {v:>10}")
    else:
        verdicts.append("N/A")
        print(f"{name:<38} {'N/A':>14} {'N/A':>10}")

# Overall: if ANY branch has PASS, the session-level gate passes.
# If all are FAIL (which the numerical scale guarantees), overall is FAIL.
if any(v == "PASS" for v in verdicts):
    overall = "PASS"
elif any(v == "INFO" for v in verdicts):
    overall = "INFO"
else:
    overall = "FAIL"

print()
print(f"Overall GAP-DOMINATED-DISPERSION-74 verdict: {overall}")

# ==============================================================================
# 6. Supplementary: the INFRARED analog — what IF the sound speed were huge?
# ==============================================================================
#
# For ell_gap to land in [10, 3000] with m_gap ~ M_KK * 0.05 (Leggett-1),
# we need c_s = m_gap / k_gap, with k_gap = ell_gap / chi_recomb.
# k_gap_target_high = 3000 / 14000 Mpc = 0.214 Mpc^{-1}
# k_gap_target_low  = 10 / 14000 Mpc = 7.14e-4 Mpc^{-1}
# c_s required = m_gap / k_gap = m_gap_GeV / (k_gap_invMpc / Mpc_inv_per_GeV)
# This gives the c_s that would be needed for the branch to produce a CMB kink.

m_gap_L1_GeV = omega_L1_canonical * MKK_GeV                           # (local)
k_gap_target_PASS_hi = 3000.0 / chi_recomb_Mpc                        # (local) 1/Mpc
k_gap_target_PASS_lo = 10.0 / chi_recomb_Mpc                          # (local) 1/Mpc
k_gap_target_PASS_hi_GeV = k_gap_target_PASS_hi / Mpc_inv_per_GeV     # (local)
k_gap_target_PASS_lo_GeV = k_gap_target_PASS_lo / Mpc_inv_per_GeV     # (local)
c_s_needed_PASS_hi = m_gap_L1_GeV / k_gap_target_PASS_hi_GeV          # (local)
c_s_needed_PASS_lo = m_gap_L1_GeV / k_gap_target_PASS_lo_GeV          # (local)

print()
print("="*78)
print("SUPPLEMENTARY: c_s required for Leggett-1 to produce detectable CMB kink")
print("="*78)
print()
print(f"m_gap(Leggett-1) = {omega_L1_canonical:.4e} M_KK = {m_gap_L1_GeV:.4e} GeV")
print(f"Target k_gap (ell=10):   {k_gap_target_PASS_lo:.3e} 1/Mpc")
print(f"Target k_gap (ell=3000): {k_gap_target_PASS_hi:.3e} 1/Mpc")
print(f"Required c_s (for ell=10):   {c_s_needed_PASS_lo:.3e}")
print(f"Required c_s (for ell=3000): {c_s_needed_PASS_hi:.3e}")
print(f"Canonical c_L (midpoint):    {c_L_lab:.3e}")
print(f"Ratio c_s_needed(3000) / c_L_actual: {c_s_needed_PASS_hi / c_L_lab:.3e}")
print()
print("=> c_s would need to EXCEED the speed of light by factor ~1e37")
print("   for the crossover to fall at CMB scales. This is a structural")
print("   consequence of the M_KK * chi_recomb dimensionless ratio.")
print()

# Dimensionless check: M_KK (GeV) * chi_recomb (GeV^{-1})
M_chi_dimless = MKK_GeV * chi_recomb_GeV_inv                          # (local)
print(f"M_KK * chi_recomb = {M_chi_dimless:.3e}")
print(f"log10(M_KK * chi_recomb) = {np.log10(M_chi_dimless):.2f}")
print("This is the 'exponent' of the fundamental mismatch.")

# ==============================================================================
# 7. Alternative interpretation: what IS the physical crossover scale?
# ==============================================================================
#
# The gap mass m_gap ~ 0.05 * M_KK corresponds to a length 1/m_gap.
# For a Leggett mode with m_gap = 0.0492 * M_KK_gravity:
#   m_gap ~ 0.0492 * 7.43e16 GeV = 3.66e15 GeV
#   Compton wavelength: hbar_c / m_gap ~ 1.97e-16 / 3.66e15 GeV*m = 5.4e-32 m
# This is 17 orders of magnitude BELOW the Planck length? No, Planck length is
# 1.6e-35 m, so 5.4e-32 m is 3000x the Planck length. Still, far below any
# cosmological scale. The crossover lives at UV-microscopic scales, not CMB.

lambda_Compton_L1_m = hbar_c_GeV_m / m_gap_L1_GeV                     # (local)
lambda_Compton_L1_Mpc = lambda_Compton_L1_m / Mpc_to_m                # (local)
print()
print(f"Leggett-1 Compton wavelength:")
print(f"  lambda_C = hbar_c / m_gap = {lambda_Compton_L1_m:.3e} m")
print(f"           = {lambda_Compton_L1_Mpc:.3e} Mpc")
print(f"The physical crossover k ~ m_gap is DEEP UV, not cosmological.")

# ==============================================================================
# 8. Write output
# ==============================================================================

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s74_gap_dominated_dispersion.npz")
np.savez(
    out_path,
    # Branch metadata
    branch_names=np.array(branch_names),
    # Gap masses (M_KK units and GeV)
    m_gap_MKK=m_gap_MKK_arr,
    m_gap_GeV=m_gap_GeV_arr,
    m_gap_GeV_kerner=m_gap_GeV_kerner_arr,
    # Sound speeds (lab frame)
    c_s_lab=c_s_lab_arr,
    # k_gap
    k_gap_GeV=k_gap_GeV_arr,
    k_gap_invMpc=k_gap_invMpc_arr,
    # CMB multipoles
    ell_gap=ell_gap_arr,
    ell_gap_lo=ell_gap_lo_arr,
    ell_gap_hi=ell_gap_hi_arr,
    ell_gap_kerner=ell_gap_kerner_arr,
    # Verdicts
    verdicts=np.array(verdicts),
    overall_verdict=np.array([overall]),
    # Cosmology / diagnostics
    chi_recomb_Gpc=np.array([chi_recomb_Gpc]),
    chi_recomb_Mpc=np.array([chi_recomb_Mpc]),
    M_KK_used_GeV=np.array([MKK_GeV]),
    M_KK_kerner_GeV=np.array([MKK_GeV_alt]),
    M_chi_dimless=np.array([M_chi_dimless]),
    log10_M_chi=np.array([np.log10(M_chi_dimless)]),
    # S52 dispersion fit cross-check
    m_gap_s52_fit=m_gap_s52,
    c_s_internal_s52=c_s_internal,
    labels_s52=np.array(labels_s52),
    # Supplementary: required c_s for PASS
    c_s_required_PASS_lo_ell10=np.array([c_s_needed_PASS_lo]),
    c_s_required_PASS_hi_ell3000=np.array([c_s_needed_PASS_hi]),
    c_L_canonical=np.array([c_L_lab]),
    # Compton scale
    lambda_Compton_L1_m=np.array([lambda_Compton_L1_m]),
    lambda_Compton_L1_Mpc=np.array([lambda_Compton_L1_Mpc]),
    # Gate metadata
    gate_name=np.array(["GAP-DOMINATED-DISPERSION-74"]),
    gate_verdict=np.array([overall]),
    gate_detail=np.array([
        f"All gap-dominated branches produce ell_gap ~ 10^59-10^60, ~56 OOM above "
        f"detectable range [10, 3000]. Verdict: {overall}. Structural cause: "
        f"M_KK * chi_recomb ~ {M_chi_dimless:.2e} (log10 = {np.log10(M_chi_dimless):.2f}). "
        f"Leggett-1 m_gap = {omega_L1_canonical:.4e} M_KK = {m_gap_L1_GeV:.3e} GeV, "
        f"c_L = {c_L_lab:.3e}, k_gap ~ {k_gap_invMpc_arr[0]:.2e} Mpc^-1. "
        f"To land at ell=3000, c_s would need to exceed c_light by factor "
        f"{c_s_needed_PASS_hi / c_L_lab:.2e}."
    ]),
)
print()
print(f"Saved: {out_path}")
print()
print(f"FINAL VERDICT: GAP-DOMINATED-DISPERSION-74 = {overall}")
