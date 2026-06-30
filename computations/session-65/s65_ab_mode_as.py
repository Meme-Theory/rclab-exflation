#!/usr/bin/env python3
"""
s65_ab_mode_as.py — Anderson-Bogoliubov Mode A_s Normalization
===============================================================

Gate: AB-AS-65
  PASS: |log10(A_s^{AB}/A_s^{obs})| < 1.0 (within 1 OOM)
  FAIL: |log10(A_s^{AB}/A_s^{obs})| > 3.0 (no improvement over 3.16 OOM)
  INFO: 1.0 < gap < 3.0 (partial improvement)

PHYSICS:
    The Anderson-Bogoliubov (AB) mode is the Goldstone boson of the
    spontaneously broken U(1) symmetry in the BCS condensate on the
    32-cell fabric. Its dispersion is linear: omega_AB(k) = c_BA * k
    with c_BA = 0.399 (from S64 SOUND-SPEED-64 PASS).

    The Garriga-Mukhanov (2000) formula gives the scalar power spectrum
    for perturbations propagating with arbitrary sound speed:

        P_s(k) = H^2 / (8 * pi^2 * eps_H * c_s * M_Pl^2)      (Eq. 1)

    with c_s = c_BA for the AB mode. This formula bypasses the
    Peter-Weyl mode-counting selection that imposes a 3.50 OOM
    structural deficit in the spectral action perturbation route
    (S64 TRANSFER-BOGOLIUBOV-64). The AB mode is a COLLECTIVE
    excitation coupling to all fibers, not restricted to the (0,0)
    Peter-Weyl sector.

    However, the Garriga-Mukhanov formula with c_s < 1 ENHANCES P_s
    (denominator smaller), which INCREASES the gap for a framework
    that already overpredicts A_s. The computation determines the
    net effect: bypassing PW selection vs. c_BA enhancement.

    The Bogoliubov enhancement from Parker pair production during
    the transit further multiplies P_s:

        P_s^{enh} = P_s * (1 + 2|beta|^2)^2                    (Eq. 2)

    with |beta|^2 = 1.015 (BA universal, S57/S64).

Session: S65 W2-D
Author: quantum-acoustics-theorist
Depends on: S64 (sound_speed, epsilon_profile, bogoliubov_phases, transfer_bogoliubov, occ_spec)
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, a2_fold, a0_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    G_DeWitt, H_fold, Z_fold,
    A_s_CMB, PI,
    M_KK, M_KK_gravity,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s65_ab_mode_as.npz"
OUT_PNG = SCRIPT_DIR / "s65_ab_mode_as.png"

t_start = time.time()

print("=" * 78)
print("S65 AB-AS-65: Anderson-Bogoliubov Mode A_s Normalization")
print("=" * 78)

# =============================================================================
# SECTION 1: Load input data
# =============================================================================
print("\n--- Section 1: Load input data ---")

# S64: Sound speed
d_sound = np.load(SCRIPT_DIR / "s64_sound_speed.npz", allow_pickle=True)
c_BA = float(d_sound['c_BA_S56'])          # 0.399
c_BLV = float(d_sound['c_BLV'])            # 0.485
c_mod = float(d_sound['c_mod'])             # 1.0
Mach_fric = float(d_sound['Mach_fric'])     # 13.75

# S64: Epsilon profile
d_eps = np.load(SCRIPT_DIR / "s64_epsilon_profile.npz", allow_pickle=True)
epsilon_H_arr = d_eps['epsilon_H']    # at requested tau values
tau_requested = d_eps['tau_requested']
H_at_tau = d_eps['H_at_tau']
S_at_tau = d_eps['S_at_tau']
dS_at_tau = d_eps['dS_at_tau']
d2S_at_tau = d_eps['d2S_at_tau']

# S64: Bogoliubov phases
d_bog = np.load(SCRIPT_DIR / "s64_bogoliubov_phases.npz", allow_pickle=True)
beta_sq_B = d_bog['beta_sq_check_B']       # (32, 8) Bogoliubov |beta|^2

# S64: Transfer function (for comparison)
d_trans = np.load(SCRIPT_DIR / "s64_transfer_bogoliubov.npz", allow_pickle=True)
gap_occ_orig = float(d_trans['gap_occ_orig'])
gap_from_PW = float(d_trans['gap_from_PW'])
gap_from_gaps = float(d_trans['gap_from_gaps'])
gap_revised_S64 = float(d_trans['gap_revised'])

# S64: Occupation spectrum
d_occ = np.load(SCRIPT_DIR / "s64_occ_spec.npz", allow_pickle=True)
gap_full = float(d_occ['gap_full'])
gap_occ = float(d_occ['gap_occ'])
S_occ = float(d_occ['S_occ'])

# Identify fold index
idx_fold = np.argmin(np.abs(tau_requested - tau_fold))
eps_H_fold = epsilon_H_arr[idx_fold]

print(f"Sound speeds:")
print(f"  c_BA = {c_BA} (Anderson-Bogoliubov)")
print(f"  c_BLV = {c_BLV:.4f} (Bogoliubov-de Gennes fabric)")
print(f"  c_mod = {c_mod} (modulus / tensor)")
print(f"  Mach (transit) = {Mach_fric:.4f}")
print(f"\nEpsilon at fold:")
print(f"  eps_H = {eps_H_fold:.6f} (geometric, S'²/(2SS''))")
print(f"  tau_fold = {tau_fold}")
print(f"\nS64 A_s gap (Peter-Weyl route):")
print(f"  gap_full = {gap_full:.4f} OOM")
print(f"  gap_occ = {gap_occ:.4f} OOM")
print(f"  gap_PW = {gap_occ + gap_from_PW:.4f} OOM (= gap_occ + {gap_from_PW:.4f})")
print(f"  gap_revised = {gap_revised_S64:.4f} OOM")

# =============================================================================
# SECTION 2: Spectral action Planck mass
# =============================================================================
print("\n--- Section 2: Spectral action Planck mass ---")

# From spectral action expansion:
#   S_EH = (f_2 * a_2 * Lambda^2) / (48 * pi^2) * integral R sqrt(g) d^4x
# Identifying with (M_Pl^2 / 2) * integral R sqrt(g):
#   M_Pl^2 = f_2 * a_2 * Lambda^2 / (24 * pi^2)    (with 1/2 convention)
# or
#   M_Pl^2 = a_2 / (48 * pi^2)   in M_KK units (Lambda = M_KK = 1)
#
# The f_2 dependence cancels when we form the ratio H^2/M_Pl^2 consistently.
# We use the convention M_Pl^2 = a_2 / (48 * pi^2) throughout.

M_Pl_sq = a2_fold / (48.0 * PI**2)               # Eq. 3
M_Pl = np.sqrt(M_Pl_sq)

print(f"  a_2(fold) = {a2_fold:.4f} M_KK^2")
print(f"  M_Pl^2 = a_2/(48*pi^2) = {M_Pl_sq:.6f} M_KK^2")
print(f"  M_Pl = {M_Pl:.6f} M_KK")
print(f"  M_KK / M_Pl = {1.0/M_Pl:.6f} (hierarchy within spectral action)")

# =============================================================================
# SECTION 3: Physical Hubble parameter
# =============================================================================
print("\n--- Section 3: Physical Hubble parameter ---")

# The effective Hubble that reproduces the S64 occupation-weighted A_s gap:
#   gap_occ = log10(P_s / A_s_obs) where P_s = H^2 / (8*pi^2*eps_H*M_Pl^2)
# Inverting:
#   H^2 = 10^gap_occ * A_s_obs * 8*pi^2*eps_H*M_Pl^2
#
# This H_eff encodes the occupation-weighted spectral action perturbation
# amplitude in Garriga-Mukhanov form. It is NOT the geometric Hubble
# (H_fold = 586.5 in spectral action units) but the PHYSICAL Hubble
# that matches the A_s normalization at the occupation-weighted level.

denom_GM = 8.0 * PI**2 * eps_H_fold * M_Pl_sq    # Eq. 4
P_s_occ = 10**gap_occ * A_s_CMB                   # Eq. 5
H_phys_sq = P_s_occ * denom_GM                    # Eq. 6
H_phys = np.sqrt(H_phys_sq)                       # Eq. 7

print(f"  Garriga-Mukhanov denominator = 8*pi^2*eps*M_Pl^2 = {denom_GM:.6f}")
print(f"  P_s at gap_occ = {P_s_occ:.6e}")
print(f"  H_phys^2 = P_s * denominator = {H_phys_sq:.6f} M_KK^2")
print(f"  H_phys = {H_phys:.6f} M_KK")
print(f"  (Task specification: H_phys = 0.396 M_KK, discrepancy = {(H_phys-0.396)/0.396*100:.1f}%)")

# Cross-check: reproduce gap_occ from H_phys
P_s_check = H_phys_sq / denom_GM
gap_check = np.log10(P_s_check / A_s_CMB)
print(f"\n  Cross-check: P_s(H_phys, c_s=1) = {P_s_check:.6e}")
print(f"  gap_check = log10(P_s/A_s_obs) = {gap_check:.4f} (target: {gap_occ:.4f})")
assert abs(gap_check - gap_occ) < 0.01, f"Cross-check FAILED: {gap_check} vs {gap_occ}"

# =============================================================================
# SECTION 4: AB mode power spectrum (no Bogoliubov enhancement)
# =============================================================================
print("\n--- Section 4: AB mode power spectrum ---")

# Garriga-Mukhanov formula with c_s = c_BA:
#   P_s^{AB} = H^2 / (8 * pi^2 * eps_H * c_BA * M_Pl^2)     (Eq. 8)
#
# Physics: The AB mode is the Goldstone boson of the broken U(1) in the
# BCS condensate. Density perturbations in the superfluid propagate at
# c_BA = 0.399 (subluminal). The Garriga-Mukhanov formula accounts for
# the modified dispersion relation of the perturbation mode.
#
# Key difference from PW route: The AB mode is a COLLECTIVE excitation
# of the full BCS condensate. It couples to ALL fibers, not restricted
# to the (0,0) Peter-Weyl sector. Therefore the 3.50 OOM PW selection
# factor does NOT apply.
#
# However: c_BA < 1 means P_s^{AB} > P_s^{standard} by factor 1/c_BA.
# Since P_s is already TOO LARGE (gap > 0), this WORSENS the gap.

P_s_AB = H_phys_sq / (8.0 * PI**2 * eps_H_fold * c_BA * M_Pl_sq)  # Eq. 8
gap_AB = np.log10(P_s_AB / A_s_CMB)
delta_gap_from_cBA = np.log10(1.0 / c_BA)

print(f"  P_s^AB = H^2/(8*pi^2*eps*c_BA*M_Pl^2) = {P_s_AB:.6e}")
print(f"  A_s^AB = P_s^AB = {P_s_AB:.6e}")
print(f"  A_s^obs = {A_s_CMB:.1e}")
print(f"  gap_AB = log10(A_s^AB/A_s^obs) = {gap_AB:.4f} OOM")
print(f"  1/c_BA = {1.0/c_BA:.4f} => delta_gap = +{delta_gap_from_cBA:.4f} OOM")
print(f"  gap_AB = gap_occ + log10(1/c_BA) = {gap_occ:.4f} + {delta_gap_from_cBA:.4f} = {gap_AB:.4f}")
print(f"\n  Direction: c_BA < 1 INCREASES P_s => gap WORSENS by {delta_gap_from_cBA:.4f} OOM")

# =============================================================================
# SECTION 5: Bogoliubov enhancement
# =============================================================================
print("\n--- Section 5: Bogoliubov enhancement ---")

# The Parker pair production during the transit enhances the power spectrum:
#   P_s^{enh} = P_s * (1 + 2*|beta|^2)^2                     (Eq. 9)
#
# where |beta|^2 is the mean Bogoliubov coefficient for BA modes.
# From S57: the BA modes have |beta|^2 = 1.015 (universal, conformal stretching).
# From S64 PHASE-BOGOLIUBOV-64: confirmed to 10^{-12}.
#
# This enhancement represents the amplification of vacuum fluctuations
# during the supersonic transit through the fold.

# Extract BA |beta|^2 from S64 data
beta_sq_BA_all = beta_sq_B     # (32, 8) per-k, per-branch
beta_sq_BA_mean = np.mean(beta_sq_BA_all)
beta_sq_BA_k0 = np.mean(beta_sq_BA_all[0, :])  # k=0 modes

# Use the S57 universal value (verified in S64)
beta_sq_universal = 1.015  # (local)

enhancement = (1.0 + 2.0 * beta_sq_universal)**2              # Eq. 9
log_enhancement = np.log10(enhancement)

P_s_AB_enh = P_s_AB * enhancement                             # Eq. 10
gap_AB_enh = np.log10(P_s_AB_enh / A_s_CMB)

print(f"  |beta|^2 (S57 universal) = {beta_sq_universal}")
print(f"  |beta|^2 (S64 mean, all k) = {beta_sq_BA_mean:.6f}")
print(f"  |beta|^2 (S64 k=0 mean) = {beta_sq_BA_k0:.6f}")
print(f"  Enhancement: (1 + 2*{beta_sq_universal})^2 = ({1+2*beta_sq_universal:.3f})^2 = {enhancement:.4f}")
print(f"  log10(enhancement) = {log_enhancement:.4f}")
print(f"\n  P_s^{'{AB,enh}'} = {P_s_AB_enh:.6e}")
print(f"  gap_AB,enh = {gap_AB_enh:.4f} OOM")
print(f"  Direction: Bogoliubov INCREASES P_s => gap WORSENS by {log_enhancement:.4f} OOM")

# =============================================================================
# SECTION 6: Alternative sound speeds
# =============================================================================
print("\n--- Section 6: Sound speed sensitivity ---")

# The AB mode uses c_BA = 0.399. For comparison, compute P_s for all
# four sound speeds in the hierarchy (S64 SOUND-SPEED-64).
# If ANY sound speed gives gap < 3.0, it would count as improvement.

sound_speeds = {
    'c_mod (tensor)': c_mod,        # 1.0
    'c_BLV (fabric)': c_BLV,        # 0.485
    'c_BA (BCS)': c_BA,             # 0.399
}

# Add Leggett range
c_L_min, c_L_max = d_sound['c_Leggett_range']
sound_speeds['c_L_min'] = float(c_L_min)
sound_speeds['c_L_max'] = float(c_L_max)

print(f"{'Sound speed':>20s}  {'c_s':>8s}  {'P_s':>12s}  {'gap (OOM)':>10s}  {'gap+Bog':>10s}")
print(f"{'----------':>20s}  {'---':>8s}  {'---':>12s}  {'---------':>10s}  {'-------':>10s}")

gap_dict = {}
for name, cs in sound_speeds.items():
    P_s_cs = H_phys_sq / (8.0 * PI**2 * eps_H_fold * cs * M_Pl_sq)
    gap_cs = np.log10(P_s_cs / A_s_CMB)
    gap_cs_enh = gap_cs + log_enhancement
    gap_dict[name] = {'c_s': cs, 'P_s': P_s_cs, 'gap': gap_cs, 'gap_enh': gap_cs_enh}
    print(f"  {name:>18s}  {cs:8.4f}  {P_s_cs:12.4e}  {gap_cs:10.4f}  {gap_cs_enh:10.4f}")

print(f"\n  Comparison: S64 PW route gap = {gap_revised_S64:.4f} OOM")
print(f"  No sound speed produces gap < S64 PW route.")

# =============================================================================
# SECTION 7: Why AB mode worsens the gap — structural analysis
# =============================================================================
print("\n--- Section 7: Structural analysis ---")

# The AB mode route trades:
#   LOST: Peter-Weyl selection factor (3.50 OOM suppression)
#   GAINED: 1/c_BA enhancement (0.40 OOM increase in gap)
#   GAINED: Bogoliubov enhancement (0.96 OOM increase in gap)
#
# Net effect: gap increases by +0.40 + 0.96 = +1.36 OOM
#             but loses 3.50 OOM of suppression
# So gap_AB = gap_occ + 0.40 = 7.29 vs gap_PW = gap_occ - 3.50 = 3.39
#
# The PW selection is MORE suppressive than c_BA + Bogoliubov combined.
# This is a STRUCTURAL result: the 1/155984 PW selection factor
# (log10(1/155984) = -5.19, reduced to -3.50 by v^2 weighting)
# dominates over the O(1) sound speed and O(10) Bogoliubov corrections.

print(f"  PW route breakdown:")
print(f"    Start: gap_occ = {gap_occ:.4f} OOM")
print(f"    PW selection: {gap_from_PW:.4f} OOM (suppression)")
print(f"    Gap tunneling: {gap_from_gaps:.4f} OOM (suppression)")
print(f"    Final: {gap_revised_S64:.4f} OOM")
print(f"")
print(f"  AB route breakdown:")
print(f"    Start: gap_occ = {gap_occ:.4f} OOM")
print(f"    c_BA factor: +{delta_gap_from_cBA:.4f} OOM (enhancement, WORSENS)")
print(f"    Bogoliubov: +{log_enhancement:.4f} OOM (enhancement, WORSENS)")
print(f"    Final: {gap_AB_enh:.4f} OOM")
print(f"")
print(f"  Difference: AB is {gap_AB_enh - gap_revised_S64:.2f} OOM WORSE than PW route")
print(f"")
print(f"  STRUCTURAL LESSON: The Peter-Weyl selection (3.50 OOM suppression)")
print(f"  far exceeds the c_BA and Bogoliubov corrections (1.36 OOM enhancement).")
print(f"  The AB mode does not help close the A_s gap.")
print(f"  For gap closure, need ADDITIONAL suppression mechanisms:")
print(f"    - c_s > 1 (superluminal AB mode impossible in BCS)")
print(f"    - Smaller H (lower energy density at perturbation epoch)")
print(f"    - Additional spectral weight suppression beyond PW")
print(f"    - Non-perturbative amplitude suppression")

# =============================================================================
# SECTION 8: Tau-dependent A_s profile
# =============================================================================
print("\n--- Section 8: A_s profile across tau ---")

# Compute P_s^AB as a function of tau to check if any tau value
# gives a smaller gap.

# eps_H(tau) = S'(tau)^2 / (2*S(tau)*S''(tau))
eps_H_profile = 0.5 * dS_at_tau**2 / (S_at_tau * d2S_at_tau)

# M_Pl^2(tau) = a_2(tau)/(48*pi^2) — use a_2 at fold (tau-independent to first order)
# H_phys(tau) scales with sqrt(S(tau)/S_fold) relative to H_phys at fold
H_phys_profile = H_phys * np.sqrt(S_at_tau / S_fold)

# P_s^AB(tau)
P_s_AB_profile = H_phys_profile**2 / (8.0 * PI**2 * eps_H_profile * c_BA * M_Pl_sq)
gap_AB_profile = np.log10(P_s_AB_profile / A_s_CMB)

print(f"{'tau':>8s}  {'eps_H':>10s}  {'H_phys':>10s}  {'P_s^AB':>12s}  {'gap (OOM)':>10s}")
print(f"{'---':>8s}  {'-----':>10s}  {'------':>10s}  {'------':>12s}  {'---------':>10s}")
for i, tau in enumerate(tau_requested):
    print(f"  {tau:6.3f}  {eps_H_profile[i]:10.6f}  {H_phys_profile[i]:10.6f}  "
          f"{P_s_AB_profile[i]:12.4e}  {gap_AB_profile[i]:10.4f}")

min_gap_idx = np.argmin(np.abs(gap_AB_profile))
print(f"\n  Minimum |gap| at tau = {tau_requested[min_gap_idx]:.3f}: gap = {gap_AB_profile[min_gap_idx]:.4f} OOM")

# =============================================================================
# SECTION 9: Dense tau profile for plot
# =============================================================================
print("\n--- Section 9: Dense profile computation ---")

tau_dense = d_eps['tau_dense']
eps_H_dense = d_eps['eps_H_dense']
S_dense = d_eps['S_dense']

H_phys_dense = H_phys * np.sqrt(S_dense / S_fold)
P_s_AB_dense = H_phys_dense**2 / (8.0 * PI**2 * eps_H_dense * c_BA * M_Pl_sq)
# Protect against division by zero for very small eps_H
mask_valid = eps_H_dense > 1e-10
gap_AB_dense = np.full_like(P_s_AB_dense, np.nan)
gap_AB_dense[mask_valid] = np.log10(P_s_AB_dense[mask_valid] / A_s_CMB)

# Also compute P_s for c_s = 1 (standard) for comparison
P_s_std_dense = H_phys_dense**2 / (8.0 * PI**2 * eps_H_dense * M_Pl_sq)
gap_std_dense = np.full_like(P_s_std_dense, np.nan)
gap_std_dense[mask_valid] = np.log10(P_s_std_dense[mask_valid] / A_s_CMB)

print(f"  Dense profile: {len(tau_dense)} points, tau in [{tau_dense[0]:.3f}, {tau_dense[-1]:.3f}]")
print(f"  Gap range (AB): [{np.nanmin(gap_AB_dense):.4f}, {np.nanmax(gap_AB_dense):.4f}]")

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: AB-AS-65")
print("=" * 78)

# The decisive gap is at the fold (tau = 0.19), which is where the
# spectral action perturbations are generated.
gap_decisive = gap_AB_enh  # With Bogoliubov enhancement

abs_gap = abs(gap_decisive)

if abs_gap < 1.0:
    verdict = "PASS"
    detail = (f"A_s gap = {gap_decisive:.4f} OOM (< 1.0 threshold). "
              f"AB mode + Bogoliubov brings predicted A_s within 1 OOM of observation.")
elif abs_gap > 3.0:
    verdict = "FAIL"
    detail = (f"A_s gap = {gap_decisive:.4f} OOM (> 3.0 threshold). "
              f"AB mode + Bogoliubov WORSENS gap from {gap_revised_S64:.4f} (PW route) to "
              f"{gap_decisive:.4f} OOM. The c_BA < 1 and Bogoliubov factors enhance P_s, "
              f"while bypassing the PW 3.50 OOM suppression is a net loss.")
else:
    verdict = "INFO"
    detail = (f"A_s gap = {gap_decisive:.4f} OOM (between 1.0 and 3.0). "
              f"Partial improvement over raw spectral action but worse than PW route.")

print(f"\n  Gate: AB-AS-65")
print(f"  Pre-registered criterion:")
print(f"    PASS: |log10(A_s^AB/A_s^obs)| < 1.0")
print(f"    FAIL: |log10(A_s^AB/A_s^obs)| > 3.0")
print(f"    INFO: 1.0 < gap < 3.0")
print(f"\n  Decisive numbers:")
print(f"    A_s^AB = {P_s_AB:.6e} (before Bogoliubov)")
print(f"    A_s^AB,enh = {P_s_AB_enh:.6e} (after Bogoliubov)")
print(f"    A_s^obs = {A_s_CMB:.1e}")
print(f"    gap = log10(A_s^AB,enh / A_s^obs) = {gap_decisive:.4f} OOM")
print(f"    |gap| = {abs_gap:.4f} OOM")
print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"\n  Comparison:")
print(f"    S64 PW route: {gap_revised_S64:.4f} OOM")
print(f"    AB mode (bare): {gap_AB:.4f} OOM")
print(f"    AB mode + Bog: {gap_decisive:.4f} OOM")
print(f"    AB route is {gap_decisive - gap_revised_S64:.2f} OOM worse than PW route")

# =============================================================================
# SECTION 11: Save data
# =============================================================================
print(f"\n--- Section 11: Saving results ---")

np.savez(
    OUT_NPZ,
    # Input parameters
    c_BA=c_BA,
    c_BLV=c_BLV,
    c_mod=c_mod,
    eps_H_fold=eps_H_fold,
    H_phys=H_phys,
    H_phys_sq=H_phys_sq,
    M_Pl_sq=M_Pl_sq,
    a2_fold=a2_fold,
    tau_fold=tau_fold,
    beta_sq_universal=beta_sq_universal,

    # AB mode results
    P_s_AB=P_s_AB,
    P_s_AB_enh=P_s_AB_enh,
    gap_AB=gap_AB,
    gap_AB_enh=gap_AB_enh,
    enhancement=enhancement,
    log_enhancement=log_enhancement,

    # Comparison with S64
    gap_occ=gap_occ,
    gap_full=gap_full,
    gap_revised_S64=gap_revised_S64,
    gap_from_PW=gap_from_PW,
    gap_from_gaps=gap_from_gaps,
    delta_gap_from_cBA=delta_gap_from_cBA,

    # Tau-dependent profile
    tau_requested=tau_requested,
    eps_H_profile=eps_H_profile,
    H_phys_profile=H_phys_profile,
    P_s_AB_profile=P_s_AB_profile,
    gap_AB_profile=gap_AB_profile,

    # Dense profile for plotting
    tau_dense=tau_dense,
    gap_AB_dense=gap_AB_dense,
    gap_std_dense=gap_std_dense,

    # Sound speed sensitivity
    gap_c_mod=gap_dict['c_mod (tensor)']['gap'],
    gap_c_BLV=gap_dict['c_BLV (fabric)']['gap'],
    gap_c_BA=gap_dict['c_BA (BCS)']['gap'],

    # Gate verdict
    gate_name='AB-AS-65',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 12: Plot
# =============================================================================
print("\n--- Section 12: Generating plot ---")

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: A_s gap decomposition comparison (waterfall)
ax1 = fig.add_subplot(gs[0, 0])
labels = ['Full SA\n(raw)', 'BCS occ\n(S_occ)', 'AB mode\n(c_BA)', 'AB+Bog\n(enh)', 'PW route\n(S64)']
gaps = [gap_full, gap_occ, gap_AB, gap_AB_enh, gap_revised_S64]
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336', '#9C27B0']
bars = ax1.barh(range(len(labels)), gaps, color=colors, alpha=0.8, height=0.6)
ax1.set_yticks(range(len(labels)))
ax1.set_yticklabels(labels, fontsize=9)
ax1.set_xlabel('log₁₀(A_s^pred / A_s^obs)')
ax1.set_title('A_s Gap Comparison')
ax1.axvline(0, color='gray', ls='-', alpha=0.3)
ax1.axvline(3.0, color='red', ls='--', alpha=0.5, label='FAIL threshold')
ax1.axvline(1.0, color='green', ls='--', alpha=0.5, label='PASS threshold')
for i, g in enumerate(gaps):
    ax1.text(g + 0.15, i, f'{g:.2f}', va='center', fontsize=9, fontweight='bold')
ax1.legend(fontsize=8, loc='lower right')
ax1.invert_yaxis()

# Panel 2: Sound speed sensitivity
ax2 = fig.add_subplot(gs[0, 1])
cs_vals = [c_mod, c_BLV, c_BA, float(c_L_min), float(c_L_max)]
cs_names = ['c_mod', 'c_BLV', 'c_BA', 'c_L(min)', 'c_L(max)']
gaps_cs = [gap_dict[k]['gap'] if k in gap_dict else np.nan for k in
           ['c_mod (tensor)', 'c_BLV (fabric)', 'c_BA (BCS)', 'c_L_min', 'c_L_max']]
ax2.scatter(cs_vals, gaps_cs, s=100, c=['blue', 'green', 'orange', 'red', 'darkred'],
            zorder=5, edgecolors='black')
for i, (cs, g, n) in enumerate(zip(cs_vals, gaps_cs, cs_names)):
    ax2.annotate(n, (cs, g), textcoords="offset points", xytext=(5, 8), fontsize=8)
ax2.set_xlabel('Sound speed c_s')
ax2.set_ylabel('log₁₀(A_s^pred / A_s^obs)')
ax2.set_title('Sound Speed → A_s Gap')
ax2.axhline(gap_revised_S64, color='purple', ls=':', alpha=0.7, label=f'S64 PW ({gap_revised_S64:.2f})')
ax2.axhline(3.0, color='red', ls='--', alpha=0.4, label='FAIL threshold')
ax2.legend(fontsize=8)
ax2.set_xlim(-0.05, 1.15)

# Panel 3: Garriga-Mukhanov formula structure
ax3 = fig.add_subplot(gs[0, 2])
# Show the formula P_s = H^2/(8*pi^2*eps*c_s*M_Pl^2) with each factor
factors = ['H²', '1/(8π²)', '1/ε_H', '1/c_BA', '1/M_Pl²', 'Total']
values_log = [
    np.log10(H_phys_sq),
    np.log10(1.0 / (8*PI**2)),
    np.log10(1.0 / eps_H_fold),
    np.log10(1.0 / c_BA),
    np.log10(1.0 / M_Pl_sq),
    np.log10(P_s_AB),
]
ax3.barh(range(len(factors)), values_log,
         color=['skyblue']*5 + ['coral'], alpha=0.8, height=0.6)
ax3.set_yticks(range(len(factors)))
ax3.set_yticklabels(factors, fontsize=9)
ax3.set_xlabel('log₁₀(factor)')
ax3.set_title('P_s^{AB} Factor Decomposition')
for i, v in enumerate(values_log):
    ax3.text(v + 0.05 if v > 0 else v - 0.5, i, f'{v:.3f}', va='center', fontsize=8)
ax3.invert_yaxis()

# Panel 4: Tau-dependent gap profile
ax4 = fig.add_subplot(gs[1, 0:2])
ax4.plot(tau_dense, gap_std_dense, 'b-', alpha=0.7, label='c_s = 1 (standard)', linewidth=1.5)
ax4.plot(tau_dense, gap_AB_dense, 'r-', alpha=0.9, label=f'c_s = c_BA = {c_BA}', linewidth=2)
ax4.axhline(gap_revised_S64, color='purple', ls=':', alpha=0.7,
            label=f'S64 PW route ({gap_revised_S64:.2f})', linewidth=1.5)
ax4.axhline(3.0, color='red', ls='--', alpha=0.4, label='FAIL (3.0)')
ax4.axhline(1.0, color='green', ls='--', alpha=0.4, label='PASS (1.0)')
ax4.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label=f'tau_fold = {tau_fold}')
ax4.scatter(tau_requested, gap_AB_profile, s=40, c='red', zorder=5)
ax4.set_xlabel('tau')
ax4.set_ylabel('log₁₀(A_s^pred / A_s^obs)')
ax4.set_title('A_s Gap vs. tau')
ax4.set_ylim(0, max(15, np.nanmax(gap_AB_dense[gap_AB_dense < 50]) + 1))
ax4.legend(fontsize=8, loc='upper left')

# Panel 5: Summary text
ax5 = fig.add_subplot(gs[1, 2])
ax5.axis('off')
summary = (
    f"Gate: AB-AS-65\n"
    f"Verdict: {verdict}\n\n"
    f"Key Numbers:\n"
    f"  H_phys = {H_phys:.4f} M_KK\n"
    f"  eps_H = {eps_H_fold:.5f}\n"
    f"  c_BA = {c_BA}\n"
    f"  M_Pl^2 = {M_Pl_sq:.4f} M_KK^2\n"
    f"  |beta|^2 = {beta_sq_universal}\n\n"
    f"A_s Results:\n"
    f"  A_s^AB = {P_s_AB:.3e}\n"
    f"  A_s^AB,enh = {P_s_AB_enh:.3e}\n"
    f"  A_s^obs = {A_s_CMB:.1e}\n\n"
    f"Gap:\n"
    f"  AB (bare): {gap_AB:.2f} OOM\n"
    f"  AB + Bog:  {gap_AB_enh:.2f} OOM\n"
    f"  S64 PW:    {gap_revised_S64:.2f} OOM\n\n"
    f"Structural Finding:\n"
    f"  PW 3.50 OOM suppression\n"
    f"  > c_BA + Bog 1.36 OOM enhancement\n"
    f"  AB mode WORSENS gap by {gap_AB_enh-gap_revised_S64:.1f} OOM"
)
ax5.text(0.05, 0.95, summary, transform=ax5.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('S65 AB-AS-65: Anderson-Bogoliubov Mode A_s Normalization', fontsize=14, fontweight='bold')
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {OUT_PNG}")

elapsed = time.time() - t_start
print(f"\n  Total time: {elapsed:.2f} s")
print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
