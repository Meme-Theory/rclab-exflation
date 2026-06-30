#!/usr/bin/env python3
"""
s67_dissipative_as.py — Dissipative A_s: Noise-Dominated Power Spectrum Normalization
======================================================================================

Gate: DISSIPATIVE-AS-67
  PASS: Dissipative A_s within 1 OOM of Planck (2.1e-9)
  FAIL: Dissipative A_s still > 2 OOM from Planck
  INFO: Dissipative correction is O(1) but insufficient alone

PHYSICS:
    The transit through the van Hove fold at tau=0.19 is strongly dissipative:
    P_exc = 1.000 (all modes excited), acoustic impedance mismatch Gamma = 0.99970.
    If the effective dissipation rate gamma_eff >> H, the Bunch-Davies vacuum
    contribution to the power spectrum is exponentially suppressed as
    exp(-gamma_eff/H), and the spectrum is dominated by pair-creation noise
    (Lopez Nacir et al., dissipative EFT of inflation, Paper [09] in S66 library).

    Standard Garriga-Mukhanov (slow-roll vacuum fluctuations):
        P_zeta^{std} = H^2 / (8 pi^2 epsilon c_s M_Pl^2)            [Eq. 1]

    Dissipative noise-dominated regime (Lopez Nacir et al. Eq. 43-44):
        P_zeta^{diss} = (H^2 gamma_eff) / (4 pi^2 epsilon c_s^3 M_Pl^2)  [Eq. 2]

    The ratio:
        P_diss / P_std = 2 gamma_eff / c_s^2                         [Eq. 3]

    Three estimates of the microscopic dissipation rate gamma:
    (A) gamma ~ M_KK * (1 - Gamma) ~ 3e-4 M_KK  [impedance-mismatch energy loss]
    (B) gamma ~ M_KK                              [natural scale, P_exc = 1]
    (C) gamma ~ v_terminal * dS/dtau / S          [spectral action gradient friction]

    The duty-cycle correction for the impulsive transit:
        gamma_eff = gamma * N_e / (2 pi)                              [Eq. 4]

    If gamma_eff >> H: noise dominates. If gamma_eff << H: Bunch-Davies dominates.

Session: S67 W2-E
Author: einstein-theorist
Depends on: S64 (sound_speed, epsilon_profile, ne_selfconsist), S65 (ab_mode_as)
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
    G_DeWitt, H_fold, Z_fold, v_terminal, dt_transit,
    A_s_CMB, PI, M_KK, M_KK_gravity, M_Pl_reduced,
    P_exc_kz, Kapitza_ratio,
    c_fabric,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s67_dissipative_as.npz"
OUT_PNG = SCRIPT_DIR / "s67_dissipative_as.png"

t_start = time.time()

print("=" * 78)
print("S67 DISSIPATIVE-AS-67: Noise-Dominated Amplitude Normalization")
print("=" * 78)

# =============================================================================
# SECTION 1: Load input data from S64 and S65
# =============================================================================
print("\n--- Section 1: Load input data ---")

# S64: Sound speed
d_sound = np.load(SCRIPT_DIR / "s64_sound_speed.npz", allow_pickle=True)
c_BA = float(d_sound['c_BA_S56'])          # 0.399
c_BLV = float(d_sound['c_BLV'])            # 0.485
c_mod = float(d_sound['c_mod'])             # 1.0
Mach_fric = float(d_sound['Mach_fric'])     # 13.75
v_fric = float(d_sound['v_fric'])           # 6.669

# S64: N_e self-consistent
d_ne = np.load(SCRIPT_DIR / "s64_ne_selfconsist.npz", allow_pickle=True)
Ne_primary = float(d_ne['Ne_primary'])       # 3.7281e-3
Ne_range_lo = float(d_ne['Ne_range_lo'])     # 4.47e-4
Ne_range_hi = float(d_ne['Ne_range_hi'])     # 6.76e-3
H_phys_fold_MKK = float(d_ne['H_phys_fold_MKK'])  # 0.396
H_phys_fold_GeV = float(d_ne['H_phys_fold_GeV'])   # 2.94e16

# S65: AB mode A_s data
d_ab = np.load(SCRIPT_DIR / "s65_ab_mode_as.npz", allow_pickle=True)
H_phys = float(d_ab['H_phys'])              # 0.404 M_KK
H_phys_sq = float(d_ab['H_phys_sq'])        # 0.163 M_KK^2
M_Pl_sq = float(d_ab['M_Pl_sq'])            # 5.860 M_KK^2
eps_H_fold = float(d_ab['eps_H_fold'])       # 0.0216
gap_revised_S64 = float(d_ab['gap_revised_S64'])   # 3.165 OOM (PW route)
gap_occ = float(d_ab['gap_occ'])             # 6.891 OOM (occupation-weighted)
beta_sq_universal = float(d_ab['beta_sq_universal'])  # 1.015

print(f"Physical Hubble:")
print(f"  H_phys = {H_phys:.6f} M_KK = {H_phys_fold_GeV:.4e} GeV")
print(f"  H_fold (SA) = {H_fold:.4f} M_KK (spectral action H)")
print(f"Spectral Planck mass:")
print(f"  M_Pl^2 = {M_Pl_sq:.6f} M_KK^2  =>  M_Pl = {np.sqrt(M_Pl_sq):.6f} M_KK")
print(f"  M_KK / M_Pl = {1.0/np.sqrt(M_Pl_sq):.6f}")
print(f"Slow-roll parameter:")
print(f"  eps_H = {eps_H_fold:.6f}")
print(f"Sound speeds:")
print(f"  c_BA = {c_BA} (AB mode)")
print(f"  c_BLV = {c_BLV:.4f} (fabric)")
print(f"  c_mod = {c_mod} (modulus/tensor)")
print(f"Transit parameters:")
print(f"  N_e = {Ne_primary:.6e} (primary, 5 methods)")
print(f"  N_e range: [{Ne_range_lo:.4e}, {Ne_range_hi:.4e}]")
print(f"  v_terminal = {v_terminal:.4f} M_KK")
print(f"  v_friction = {v_fric:.4f} M_KK")
print(f"  dt_transit = {dt_transit:.6e} M_KK^{-1}")
print(f"  Mach = {Mach_fric:.4f}")
print(f"Prior gaps:")
print(f"  gap_occ (c_s=1) = {gap_occ:.4f} OOM")
print(f"  gap_PW (S64) = {gap_revised_S64:.4f} OOM")

# =============================================================================
# SECTION 2: Standard Garriga-Mukhanov normalization (baseline)
# =============================================================================
print("\n--- Section 2: Standard Garriga-Mukhanov normalization ---")

# Standard formula: P_zeta^{std} = H^2 / (8 pi^2 eps c_s M_Pl^2)     [Eq. 1]
# We compute for c_s = 1 (modulus), c_BLV (fabric), c_BA (AB mode)

sound_speeds = {'c_mod': c_mod, 'c_BLV': c_BLV, 'c_BA': c_BA}

print(f"\n  Garriga-Mukhanov formula: P_zeta = H^2 / (8 pi^2 eps c_s M_Pl^2)")
print(f"  H^2 = {H_phys_sq:.6f},  eps = {eps_H_fold:.6f},  M_Pl^2 = {M_Pl_sq:.6f}")
print(f"  Denominator (c_s=1): 8 pi^2 eps M_Pl^2 = {8*PI**2*eps_H_fold*M_Pl_sq:.6f}")

P_std = {}
gap_std = {}
for name, cs in sound_speeds.items():
    P = H_phys_sq / (8.0 * PI**2 * eps_H_fold * cs * M_Pl_sq)
    g = np.log10(P / A_s_CMB)
    P_std[name] = P
    gap_std[name] = g
    print(f"  {name:>6s}: c_s = {cs:.4f}, P_std = {P:.6e}, gap = {g:.4f} OOM")

print(f"\n  Reference: Planck A_s = {A_s_CMB:.1e}")
print(f"  S64 PW-route gap = {gap_revised_S64:.4f} OOM (best prior estimate)")
print(f"  This computation's baseline gap (c_s=1) = {gap_std['c_mod']:.4f} OOM")

# =============================================================================
# SECTION 3: Microscopic dissipation rate gamma — three estimates
# =============================================================================
print("\n--- Section 3: Microscopic dissipation rate gamma ---")

# The transit IS strongly dissipative: P_exc = 1.000, every mode excited.
# The question: what is the effective friction coefficient gamma?
#
# Physical picture: the spectral reorganization at the fold transfers
# energy from the coherent tau motion into quasiparticle pairs. This is
# the analog of a friction force on the "inflaton" (= tau parameter).
#
# Three estimates, each capturing a different aspect:

# --- Estimate A: Impedance mismatch ---
# The acoustic impedance mismatch coefficient Gamma = 0.99970 (reflection).
# Energy transmitted per crossing: (1 - Gamma) = 3e-4.
# Rate: gamma_A = (1 - Gamma) * M_KK = 3e-4 M_KK
# This is the energy loss rate from acoustic mismatch at the fold boundary.
Gamma_impedance = 0.99970    # Acoustic impedance reflection coefficient  # (local)
gamma_A = (1.0 - Gamma_impedance)  # in M_KK units (M_KK = 1)
print(f"  Estimate A (impedance mismatch):")
print(f"    Gamma_impedance = {Gamma_impedance}")
print(f"    1 - Gamma = {1-Gamma_impedance:.4e}")
print(f"    gamma_A = (1 - Gamma) * M_KK = {gamma_A:.4e} M_KK")

# --- Estimate B: Natural scale (maximal dissipation) ---
# P_exc = 1.000 means every available mode is excited. The dissipation
# rate saturates at the natural scale: gamma_B = M_KK.
# This is the upper bound on microscopic friction.
gamma_B = 1.0  # M_KK units  # (local)
print(f"  Estimate B (natural scale, P_exc=1):")
print(f"    gamma_B = M_KK = {gamma_B:.4f} M_KK")

# --- Estimate C: Spectral action gradient friction ---
# The spectral action gradient dS/dtau = +58,673 acts as a force on tau.
# The friction-limited terminal velocity is v_terminal = F / gamma_C,
# where F = dS/dtau / (2 * G_DeWitt * S).
# Solving: gamma_C = dS/dtau / (2 * G_DeWitt * S * v_terminal)
# But this is the friction that PRODUCES the terminal velocity, not an
# external dissipation. We compute it for completeness.
#
# More physically: the power dissipated into pair creation is
# P_diss = gamma * v^2. The total energy transferred into pairs is
# E_exc = n_pairs * omega_mode ~ 60 * M_KK ~ 60 M_KK (in M_KK units).
# Over the transit: E_exc = gamma_C * v_terminal^2 * dt_transit
# => gamma_C = E_exc / (v_terminal^2 * dt_transit)

# Use E_exc from canonical: 60.625 M_KK (from canonical_constants)
from canonical_constants import E_exc, n_pairs
gamma_C = E_exc / (v_terminal**2 * dt_transit)
print(f"  Estimate C (energy balance: E_exc = gamma * v^2 * dt):")
print(f"    E_exc = {E_exc:.4f} M_KK")
print(f"    v_terminal = {v_terminal:.4f} M_KK")
print(f"    dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"    gamma_C = E_exc / (v^2 dt) = {gamma_C:.4f} M_KK")

# --- Estimate D: Kapitza ratio ---
# The Kapitza ratio (thermal boundary resistance) measures the fraction of
# energy transmitted across the BCS gap boundary:
# gamma_D = Kapitza_ratio * M_KK
gamma_D = Kapitza_ratio
print(f"  Estimate D (Kapitza ratio):")
print(f"    Kapitza_ratio = {Kapitza_ratio:.6f}")
print(f"    gamma_D = {gamma_D:.6f} M_KK")

gammas = {
    'A (impedance)': gamma_A,
    'B (natural)': gamma_B,
    'C (energy balance)': gamma_C,
    'D (Kapitza)': gamma_D,
}

print(f"\n  Summary of microscopic gamma estimates (M_KK units):")
for name, g in gammas.items():
    print(f"    {name:>22s}: gamma = {g:.6e} M_KK")

# =============================================================================
# SECTION 4: Effective dissipation rate gamma_eff
# =============================================================================
print("\n--- Section 4: Effective dissipation rate gamma_eff ---")

# The Lopez Nacir formalism assumes continuous friction during many e-folds.
# The exflation transit is impulsive (N_e ~ 3.73e-3, Mach 13.8).
# The effective dissipation is duty-cycle corrected:
#
#   gamma_eff = gamma * N_e / (2*pi)                              [Eq. 4]
#
# This accounts for the fact that the friction acts only during the
# brief transit, not over a full Hubble time 1/H.
#
# ALTERNATIVE: The more physical quantity is gamma_eff / H, the number
# of dissipation timescales per Hubble time. If gamma_eff >> H, the
# Bunch-Davies vacuum is exponentially suppressed.
#
# ALSO: Since the transit is impulsive, we should also consider the
# direct comparison gamma * dt_transit vs 1/H:
#   gamma * dt_transit = number of dissipation timescales during transit
#   If >> 1: dissipation dominates during transit
#   If << 1: dissipation negligible during transit

print(f"  N_e (primary) = {Ne_primary:.6e}")
print(f"  H_phys = {H_phys:.6f} M_KK")

print(f"\n  {'Estimate':>22s}  {'gamma':>12s}  {'gamma_eff':>12s}  {'gamma_eff/H':>12s}  {'gamma*dt':>12s}  {'Regime':>20s}")
print(f"  {'--------':>22s}  {'-----':>12s}  {'---------':>12s}  {'-----------':>12s}  {'--------':>12s}  {'------':>20s}")

gamma_eff_dict = {}
for name, g in gammas.items():
    g_eff = g * Ne_primary / (2.0 * PI)
    ratio_H = g_eff / H_phys
    g_dt = g * dt_transit
    if ratio_H > 1.0:
        regime = "DISSIPATIVE (>>H)"
    elif ratio_H > 0.1:
        regime = "MARGINAL (~H)"
    else:
        regime = "VACUUM-DOMINATED"
    gamma_eff_dict[name] = {
        'gamma': g,
        'gamma_eff': g_eff,
        'ratio_H': ratio_H,
        'g_dt': g_dt,
        'regime': regime,
    }
    print(f"  {name:>22s}  {g:12.4e}  {g_eff:12.4e}  {ratio_H:12.4e}  {g_dt:12.4e}  {regime:>20s}")

# Identify the physically relevant estimate.
# Estimate C (energy balance) is the most directly constrained by data,
# since it uses the known excitation energy and transit kinematics.
gamma_primary = gamma_C
gamma_eff_primary = gamma_C * Ne_primary / (2.0 * PI)
ratio_primary = gamma_eff_primary / H_phys

print(f"\n  PRIMARY ESTIMATE: C (energy balance)")
print(f"    gamma = {gamma_primary:.4f} M_KK")
print(f"    gamma_eff = {gamma_eff_primary:.6e} M_KK")
print(f"    gamma_eff / H = {ratio_primary:.6e}")
print(f"    exp(-gamma_eff/H) = {np.exp(-ratio_primary):.6e}")

# Also compute for estimate B (natural scale) as upper bound
gamma_eff_B = gamma_B * Ne_primary / (2.0 * PI)
ratio_B = gamma_eff_B / H_phys
print(f"\n  UPPER BOUND: B (natural scale)")
print(f"    gamma = {gamma_B:.4f} M_KK")
print(f"    gamma_eff = {gamma_eff_B:.6e} M_KK")
print(f"    gamma_eff / H = {ratio_B:.6e}")
print(f"    exp(-gamma_eff/H) = {np.exp(-ratio_B):.6e}")

# =============================================================================
# SECTION 5: Dissipative power spectrum (Lopez Nacir formula)
# =============================================================================
print("\n--- Section 5: Dissipative power spectrum ---")

# Lopez Nacir et al. dissipative EFT formula:
#   P_zeta^{diss} = (H^2 * gamma_eff) / (4 pi^2 * eps * c_s^3 * M_Pl^2)  [Eq. 2]
#
# The ratio to Garriga-Mukhanov:
#   P_diss / P_std = 2 * gamma_eff / c_s^2                       [Eq. 3]
#
# IMPORTANT: This ratio can be > 1 or < 1 depending on gamma_eff vs c_s^2/2.
# If gamma_eff < c_s^2 / 2, the dissipative formula gives SMALLER P_zeta,
# which would CLOSE the gap (since P_std is already too large).
# If gamma_eff > c_s^2 / 2, it gives LARGER P_zeta, WORSENING the gap.

print(f"  Lopez Nacir formula: P_diss = H^2 gamma_eff / (4 pi^2 eps c_s^3 M_Pl^2)")
print(f"  Ratio to standard:  P_diss / P_std = 2 gamma_eff / c_s^2")
print(f"")

print(f"  {'Gamma est':>22s}  {'c_s':>6s}  {'gamma_eff':>12s}  {'2g_eff/c_s^2':>12s}  {'P_diss':>12s}  {'gap_diss':>10s}  {'direction':>12s}")
print(f"  {'--------':>22s}  {'---':>6s}  {'---------':>12s}  {'------------':>12s}  {'------':>12s}  {'--------':>10s}  {'---------':>12s}")

results = {}
for gname, gdata in gamma_eff_dict.items():
    g_eff = gdata['gamma_eff']
    for csname, cs in sound_speeds.items():
        # Dissipative power spectrum
        P_diss = (H_phys_sq * g_eff) / (4.0 * PI**2 * eps_H_fold * cs**3 * M_Pl_sq)
        gap_diss = np.log10(P_diss / A_s_CMB) if P_diss > 0 else float('nan')

        # Ratio to standard
        ratio = 2.0 * g_eff / cs**2
        direction = "WORSENS" if ratio > 1 else "IMPROVES"

        key = f"{gname}|{csname}"
        results[key] = {
            'gamma_name': gname,
            'cs_name': csname,
            'cs': cs,
            'gamma_eff': g_eff,
            'ratio_to_std': ratio,
            'P_diss': P_diss,
            'gap_diss': gap_diss,
            'direction': direction,
        }
        print(f"  {gname:>22s}  {cs:6.4f}  {g_eff:12.4e}  {ratio:12.4e}  {P_diss:12.4e}  {gap_diss:10.4f}  {direction:>12s}")

# =============================================================================
# SECTION 6: Focused analysis — primary estimate with each sound speed
# =============================================================================
print("\n--- Section 6: Primary estimate (C, energy balance) detailed ---")

g_eff_C = gamma_eff_dict['C (energy balance)']['gamma_eff']

print(f"  gamma_C = {gamma_C:.4f} M_KK")
print(f"  gamma_eff_C = {g_eff_C:.6e} M_KK")
print(f"  gamma_eff_C / H = {g_eff_C/H_phys:.6e}")
print(f"")

for csname, cs in sound_speeds.items():
    P_std_cs = P_std[csname]
    P_diss_cs = (H_phys_sq * g_eff_C) / (4.0 * PI**2 * eps_H_fold * cs**3 * M_Pl_sq)
    ratio_cs = 2.0 * g_eff_C / cs**2
    gap_std_cs = gap_std[csname]
    gap_diss_cs = np.log10(P_diss_cs / A_s_CMB)
    delta_gap = gap_diss_cs - gap_std_cs

    print(f"  {csname}: c_s = {cs:.4f}")
    print(f"    P_std = {P_std_cs:.6e},  gap_std = {gap_std_cs:.4f} OOM")
    print(f"    P_diss = {P_diss_cs:.6e},  gap_diss = {gap_diss_cs:.4f} OOM")
    print(f"    Ratio P_diss/P_std = {ratio_cs:.6e}")
    print(f"    Delta_gap = {delta_gap:+.4f} OOM  ({'WORSENS' if delta_gap > 0 else 'IMPROVES'})")
    print()

# =============================================================================
# SECTION 7: The decisive comparison — what WOULD gamma_eff need to be?
# =============================================================================
print("\n--- Section 7: Required gamma_eff for gap closure ---")

# For the dissipative formula to match A_s_CMB:
# A_s_CMB = H^2 gamma_eff^{req} / (4 pi^2 eps c_s^3 M_Pl^2)
# => gamma_eff^{req} = A_s_CMB * 4 pi^2 eps c_s^3 M_Pl^2 / H^2

print(f"  Required gamma_eff to match Planck A_s = {A_s_CMB:.1e}:")
print(f"  From: A_s = H^2 gamma_eff / (4 pi^2 eps c_s^3 M_Pl^2)")
print(f"  => gamma_eff^req = A_s * 4 pi^2 eps c_s^3 M_Pl^2 / H^2")
print(f"")

for csname, cs in sound_speeds.items():
    g_eff_req = A_s_CMB * 4.0 * PI**2 * eps_H_fold * cs**3 * M_Pl_sq / H_phys_sq
    ratio_to_C = g_eff_req / g_eff_C if g_eff_C > 0 else float('inf')
    gamma_req = g_eff_req * 2.0 * PI / Ne_primary  # invert duty cycle
    print(f"  {csname}: c_s = {cs:.4f}")
    print(f"    gamma_eff^req = {g_eff_req:.6e} M_KK")
    print(f"    gamma^req (microscopic) = {gamma_req:.6e} M_KK")
    print(f"    Ratio gamma_eff^req / gamma_eff_C = {ratio_to_C:.6e}")
    print(f"    log10(ratio) = {np.log10(ratio_to_C):.4f} OOM")
    print()

# =============================================================================
# SECTION 8: Bunch-Davies suppression factor
# =============================================================================
print("\n--- Section 8: Bunch-Davies suppression ---")

# In the dissipative regime, the Bunch-Davies contribution is suppressed
# by exp(-2 gamma_eff / H) relative to the noise contribution.
# If this factor is << 1, the standard Garriga-Mukhanov normalization
# is irrelevant — the noise from pair creation dominates.

print(f"  Bunch-Davies suppression factor: exp(-2 gamma_eff / H)")
print(f"  H_phys = {H_phys:.6f} M_KK")
print(f"")

for gname, gdata in gamma_eff_dict.items():
    g_eff = gdata['gamma_eff']
    supp = np.exp(-2.0 * g_eff / H_phys)
    print(f"  {gname:>22s}: gamma_eff = {g_eff:.4e}, exp(-2g/H) = {supp:.6e}")
    if supp < 1e-10:
        print(f"    => Bunch-Davies EXPONENTIALLY SUPPRESSED")
    elif supp < 0.1:
        print(f"    => Bunch-Davies SUPPRESSED")
    else:
        print(f"    => Bunch-Davies NOT SUPPRESSED (vacuum-dominated)")

# =============================================================================
# SECTION 9: Dissipative correction WITH Bogoliubov enhancement
# =============================================================================
print("\n--- Section 9: Dissipative + Bogoliubov ---")

# The Bogoliubov enhancement (1 + 2|beta|^2)^2 applies to the noise
# spectrum as well, since the pair creation amplifies the noise modes.
enhancement = (1.0 + 2.0 * beta_sq_universal)**2
log_enh = np.log10(enhancement)
print(f"  Bogoliubov enhancement = {enhancement:.4f} (log10 = {log_enh:.4f})")

# Combined: P_total = P_diss * enhancement
# Gap = log10(P_total / A_s)

print(f"\n  Primary estimate C, with Bogoliubov:")
for csname, cs in sound_speeds.items():
    P_diss_cs = (H_phys_sq * g_eff_C) / (4.0 * PI**2 * eps_H_fold * cs**3 * M_Pl_sq)
    P_total = P_diss_cs * enhancement
    gap_total = np.log10(P_total / A_s_CMB)
    print(f"  {csname}: P_diss+Bog = {P_total:.6e}, gap = {gap_total:.4f} OOM")

# =============================================================================
# SECTION 10: Sensitivity scan — gamma_eff vs gap
# =============================================================================
print("\n--- Section 10: Gamma_eff sensitivity scan ---")

# Scan over gamma_eff from 1e-8 to 1e2 in M_KK units
# to map out where A_s matches Planck for each sound speed
g_eff_scan = np.logspace(-8, 2, 1000)
cs_primary = c_BLV  # fabric sound speed as the physically relevant one

P_diss_scan = (H_phys_sq * g_eff_scan) / (4.0 * PI**2 * eps_H_fold * cs_primary**3 * M_Pl_sq)
gap_diss_scan = np.log10(P_diss_scan / A_s_CMB)

# Find gamma_eff where gap = 0
idx_zero = np.argmin(np.abs(gap_diss_scan))
g_eff_zero = g_eff_scan[idx_zero]
print(f"  At c_s = c_BLV = {cs_primary:.4f}:")
print(f"    gamma_eff for gap = 0: {g_eff_zero:.6e} M_KK")
print(f"    Corresponding gamma (micro) = {g_eff_zero * 2*PI/Ne_primary:.6e} M_KK")
print(f"    Required gamma_eff / actual gamma_eff_C = {g_eff_zero/g_eff_C:.6e}")

# =============================================================================
# SECTION 11: The structural assessment
# =============================================================================
print("\n--- Section 11: Structural assessment ---")

# The dissipative correction introduces a factor 2*gamma_eff/c_s^2 in the
# power spectrum. For the primary estimate (C, energy balance):
# - gamma_eff_C ~ 4.8e-4 M_KK
# - c_BLV^2 ~ 0.235
# - 2*gamma_eff/c_BLV^2 ~ 4.1e-3
#
# This is a SMALL correction (0.4% of the standard amplitude).
# The dissipative correction REDUCES P_zeta by a factor of ~0.004
# relative to the standard formula (since gamma_eff << c_s^2/2).
#
# This means the noise-dominated regime is NOT reached: the transit
# is too brief (N_e ~ 3.7e-3) for the dissipation to overwhelm the
# Bunch-Davies vacuum, even though the microscopic dissipation rate
# is large (gamma ~ 76 M_KK for the energy-balance estimate).
#
# The duty-cycle correction N_e/(2*pi) ~ 5.9e-4 is the bottleneck.

ratio_decisive = 2.0 * g_eff_C / c_BLV**2
print(f"  Decisive ratio: 2 * gamma_eff_C / c_BLV^2 = {ratio_decisive:.6e}")
print(f"  This means: P_diss = {ratio_decisive:.6e} * P_std")
print(f"  The dissipative correction is a FACTOR {1.0/ratio_decisive:.0f}x SUPPRESSION")
print(f"  This HELPS (reduces overprediction) but by ONLY {-np.log10(ratio_decisive):.2f} OOM")
print(f"")
print(f"  WHY the dissipative regime is not reached:")
print(f"  - Microscopic gamma_C = {gamma_C:.4f} M_KK (LARGE)")
print(f"  - But N_e = {Ne_primary:.4e} (transit is too BRIEF)")
print(f"  - gamma_eff = gamma * N_e/(2pi) = {g_eff_C:.4e} M_KK (SMALL)")
print(f"  - gamma_eff / H = {g_eff_C/H_phys:.4e} << 1")
print(f"  - The duty cycle kills the dissipative enhancement")
print(f"")
print(f"  For the dissipative regime to be reached with gamma_C:")
print(f"  Need N_e > 2*pi * c_BLV^2 * H / (2 * gamma_C) = {PI*c_BLV**2*H_phys/gamma_C:.4f}")
print(f"  Actual N_e = {Ne_primary:.4e} — shortfall {PI*c_BLV**2*H_phys/gamma_C/Ne_primary:.0f}x")

# =============================================================================
# SECTION 12: Cross-check — direct comparison of formulas
# =============================================================================
print("\n--- Section 12: Cross-checks ---")

# Cross-check 1: Verify ratio formula
P_std_BLV = H_phys_sq / (8.0 * PI**2 * eps_H_fold * c_BLV * M_Pl_sq)
P_diss_BLV = (H_phys_sq * g_eff_C) / (4.0 * PI**2 * eps_H_fold * c_BLV**3 * M_Pl_sq)
ratio_check = P_diss_BLV / P_std_BLV
ratio_formula = 2.0 * g_eff_C / c_BLV**2
print(f"  Cross-check 1: P_diss/P_std")
print(f"    Direct ratio: {ratio_check:.6e}")
print(f"    Formula 2*g_eff/c_s^2: {ratio_formula:.6e}")
print(f"    Agreement: {abs(ratio_check - ratio_formula)/ratio_formula * 100:.6f}%")

# Cross-check 2: Dimensional consistency
# P_zeta is dimensionless. H^2 * gamma_eff has dimensions [M_KK^3].
# (4 pi^2 eps c_s^3 M_Pl^2) has dimensions [M_KK^2] * [1] = [M_KK^2]
# Wait — need to check units.
# In M_KK = 1 units: H^2 [M_KK^2], gamma_eff [M_KK], eps [1], c_s [1], M_Pl^2 [M_KK^2]
# Numerator: H^2 * gamma_eff = M_KK^3
# Denominator: 4 pi^2 * eps * c_s^3 * M_Pl^2 = M_KK^2
# P = M_KK^3 / M_KK^2 = M_KK ... NOT dimensionless!
#
# The Lopez Nacir formula as stated in the task must include M_Pl^2 in denominator.
# Let's re-examine: The standard Garriga-Mukhanov P = H^2/(8pi^2 eps c_s M_Pl^2)
# is dimensionless since H^2/M_Pl^2 is dimensionless.
# For dissipative: P_diss = H^2 gamma_eff / (4 pi^2 eps c_s^3 M_Pl^2)
# has [M^3]/[M^2] = [M], which is NOT dimensionless.
#
# The correct Lopez Nacir formula must be:
# P_diss = H * gamma_eff / (4 pi^2 eps c_s^3 M_Pl^2)  [if gamma_eff has dimensions of M]
# OR
# P_diss = (gamma_eff/H) * H^2 / (4 pi^2 eps c_s^3 M_Pl^2)
# The latter makes the ratio P_diss/P_std = 2 * gamma_eff / (c_s^2 * H) dimensionless.
#
# CORRECTION: Re-reading the task specification more carefully.
# The task says: P_diss = (H^2 * gamma_eff) / (eps * c_s^3 * 4 pi^2)
# Note: NO M_Pl^2 in the task formula, but that can't be right dimensionally.
# The actual Lopez Nacir formula is (their Eq. 43):
#   Delta^2_s = (gamma_eff / c_s^2) * H^2 / (4 pi^2 eps M_Pl^2)
# where gamma_eff is dimensionless (friction rate in units of H).
#
# So gamma_eff = gamma / H (dimensionless), and:
#   P_diss = (gamma/H) * H^2 / (4 pi^2 eps c_s^2 M_Pl^2)
#         = gamma * H / (4 pi^2 eps c_s^2 M_Pl^2)
#
# OR equivalently, if gamma has dimensions of mass:
#   P_diss = (gamma_eff/H) * H^2 / (4 pi^2 eps c_s^2 M_Pl^2)
#         = gamma_eff * H / (4 pi^2 eps c_s^2 M_Pl^2)

# Let me recalculate with the CORRECT dimensionally consistent formula.
# The task says ratio = gamma_eff / c_s^2, but dimensional analysis demands:
#   P_diss / P_std = 2 * gamma_eff / (c_s^2 * H)  [if gamma_eff has dim mass]
# or equivalently:
#   P_diss / P_std = 2 * (gamma/H) / c_s^2  [if gamma/H is dimensionless]

print(f"\n  Cross-check 2: Dimensional analysis")
print(f"    Standard: P = H^2 / (8 pi^2 eps c_s M_Pl^2)  [dimensionless: M^2/M^2]")
print(f"    Dissipative (CORRECTED): P = (gamma_eff * H) / (4 pi^2 eps c_s^2 M_Pl^2)")
print(f"    [dimensionless: M * M / M^2]")
print(f"    Ratio: P_diss/P_std = 2 * gamma_eff / (c_s * H)")
print(f"")
print(f"    IMPORTANT: The task formula P = H^2 gamma_eff / (4pi^2 eps c_s^3 M_Pl^2)")
print(f"    is dimensionally incorrect if gamma_eff has dimensions [mass].")
print(f"    Correcting to: P = gamma_eff * H / (4 pi^2 eps c_s^2 M_Pl^2)")
print(f"    OR equivalently: P = (gamma_eff/H) * [H^2 / (4 pi^2 eps c_s^2 M_Pl^2)]")

# =============================================================================
# SECTION 13: CORRECTED dissipative formulas
# =============================================================================
print("\n--- Section 13: Corrected dissipative power spectrum ---")

# Two interpretations of "gamma_eff":
#
# Interpretation I: gamma_eff has dimensions of mass (Hz), as in the task.
#   gamma_eff = gamma * N_e / (2*pi)  [Eq. 4, task definition]
#   Then the dimensionally correct dissipative formula is:
#     P_diss = (gamma_eff / H) * H^2 / (4 pi^2 eps c_s^2 M_Pl^2)
#            = gamma_eff * H / (4 pi^2 eps c_s^2 M_Pl^2)              [Eq. 5]
#   Ratio: P_diss / P_std = 2 * gamma_eff / (c_s * H)                 [Eq. 6]
#
# Interpretation II: gamma_eff is dimensionless (= gamma/H).
#   Then the formula as written in the task is correct with M_Pl^2:
#     P_diss = H^2 * (gamma_eff) / (4 pi^2 eps c_s^3 M_Pl^2)
#   But this requires gamma_eff dimensionless AND c_s^3 in denominator.
#   This gives ratio: P_diss/P_std = 2 * gamma_eff / c_s^2             [Eq. 7]
#
# I will compute BOTH and compare.

print(f"  Interpretation I: gamma_eff dimensional (mass), corrected formula")
print(f"  P_diss^I = gamma_eff * H / (4 pi^2 eps c_s^2 M_Pl^2)")
print(f"  Ratio: P_diss^I / P_std = 2 * gamma_eff / (c_s * H)")

print(f"\n  Interpretation II: gamma_eff = gamma / H (dimensionless)")
print(f"  P_diss^II = H^2 (gamma_eff/H) / (4 pi^2 eps c_s^2 M_Pl^2)")
print(f"  [Same as I: they're equivalent when gamma_eff is defined properly]")
print(f"")

# The key question: what is the CORRECT formula from Lopez Nacir et al.?
# Their main result (Eq. 43-44) in the strong-dissipation limit:
#   Delta^2_zeta ~ (T_noise / c_s^2) * H / (eps * M_Pl^2)
# where T_noise is the noise temperature, related to gamma by the
# fluctuation-dissipation relation: T_noise = (2 T_eff) / (2*pi*c_s^2)
# with T_eff the effective temperature of the dissipative medium.
#
# For our transit, the "temperature" is the Bogoliubov excitation energy:
#   T_eff ~ T_acoustic = 0.112 M_KK (from canonical_constants)
#
# The correct formula is thus:
#   P_diss = (T_eff * gamma) / (4 pi^2 eps c_s^4 M_Pl^2)           [Eq. 8]
# (via fluctuation-dissipation, the noise power = 2*T_eff*gamma)
#
# But there is an alternative form using only gamma_eff:
#   In the large gamma/H limit, Delta^2 ~ (gamma/H) * (H^2)/(8pi^2 eps c_s M_Pl^2) / c_s^2
#   = (gamma/(c_s^2 * H)) * P_standard
#
# Let me use the CLEANEST statement: the ratio to standard is
#   P_diss / P_std = 2 * gamma_eff / (c_s * H)   [Eq. 6]

print(f"  DEFINITIVE COMPUTATION:")
print(f"  Using ratio formula: P_diss / P_std = 2 * gamma_eff / (c_s * H)")
print(f"")
print(f"  {'Gamma est':>22s}  {'c_s':>6s}  {'2g_eff/(c_s H)':>14s}  {'P_diss':>12s}  {'gap_diss':>10s}  {'vs PW gap':>10s}")
print(f"  {'--------':>22s}  {'---':>6s}  {'--------------':>14s}  {'------':>12s}  {'--------':>10s}  {'---------':>10s}")

results_corrected = {}
for gname, gdata in gamma_eff_dict.items():
    g_eff = gdata['gamma_eff']
    for csname, cs in sound_speeds.items():
        # Corrected ratio
        ratio_corr = 2.0 * g_eff / (cs * H_phys)
        # Dissipative P_zeta
        P_diss_corr = P_std[csname] * ratio_corr
        # Gap
        gap_diss_corr = np.log10(P_diss_corr / A_s_CMB) if P_diss_corr > 0 else float('nan')
        # Comparison to PW route
        delta_PW = gap_diss_corr - gap_revised_S64

        key = f"{gname}|{csname}"
        results_corrected[key] = {
            'ratio': ratio_corr,
            'P_diss': P_diss_corr,
            'gap_diss': gap_diss_corr,
            'delta_PW': delta_PW,
        }
        print(f"  {gname:>22s}  {cs:6.4f}  {ratio_corr:14.4e}  {P_diss_corr:12.4e}  {gap_diss_corr:10.4f}  {delta_PW:+10.4f}")

# =============================================================================
# SECTION 14: The TWO formula interpretations — clean comparison
# =============================================================================
print("\n--- Section 14: Formula comparison (task vs corrected) ---")

# Task formula: P = H^2 gamma_eff / (4 pi^2 eps c_s^3 M_Pl^2)
# Has extra H in numerator compared to corrected.
# If gamma_eff is dimensional [mass]:
#   Task ratio: P_task / P_std = 2 * gamma_eff / c_s^2   [dim: mass, WRONG]
#   Corrected ratio: P_corr / P_std = 2 * gamma_eff / (c_s * H) [dim: 1, CORRECT]
#
# These differ by a factor of H/c_s. Since H ~ 0.4 and c_s ~ 0.5:
# the difference is a factor H/c_s ~ 0.8, which is O(1).
#
# HOWEVER, looking at the task statement again, it says:
#   "The extra factor of gamma_eff/c_s^2 can be O(1) or larger"
# This suggests the task intends gamma_eff to be dimensionless (= gamma/H).
# With that reading:
#   P_diss = (gamma/H) * H^2 / (4 pi^2 eps c_s^2 M_Pl^2)
#          = gamma * H / (4 pi^2 eps c_s^2 M_Pl^2)

# For the definitive computation, I will present BOTH:
cs_def = c_BLV  # physically relevant sound speed

# Case 1: Task formula as written (gamma_eff dimensional)
P_task_C = (H_phys_sq * g_eff_C) / (4.0 * PI**2 * eps_H_fold * cs_def**3 * M_Pl_sq)
gap_task_C = np.log10(P_task_C / A_s_CMB)

# Case 2: Corrected formula (dimensionally consistent)
ratio_corr_C = 2.0 * g_eff_C / (cs_def * H_phys)
P_corr_C = P_std['c_BLV'] * ratio_corr_C
gap_corr_C = np.log10(P_corr_C / A_s_CMB)

# Case 3: gamma_eff/H interpretation (gamma_eff = gamma/H, dimensionless)
gamma_eff_dimless_C = g_eff_C / H_phys
P_dimless_C = (H_phys_sq * gamma_eff_dimless_C) / (4.0 * PI**2 * eps_H_fold * cs_def**2 * M_Pl_sq)
gap_dimless_C = np.log10(P_dimless_C / A_s_CMB)

print(f"  At c_BLV = {cs_def:.4f}, gamma_C = {gamma_C:.4f}, gamma_eff_C = {g_eff_C:.4e}:")
print(f"")
print(f"  Case 1 (task formula, gamma_eff dim): P = {P_task_C:.4e}, gap = {gap_task_C:.4f}")
print(f"  Case 2 (corrected, ratio method):     P = {P_corr_C:.4e}, gap = {gap_corr_C:.4f}")
print(f"  Case 3 (gamma_eff/H dimensionless):   P = {P_dimless_C:.4e}, gap = {gap_dimless_C:.4f}")
print(f"")
print(f"  Cases 2 and 3 agree (both dimensionally consistent): {abs(gap_corr_C - gap_dimless_C) < 0.01}")
print(f"  Case 1 differs from 2,3 by: {gap_task_C - gap_corr_C:.4f} OOM")
print(f"  (Difference = log10(H/c_s) = log10({H_phys/cs_def:.4f}) = {np.log10(H_phys/cs_def):.4f})")
print(f"")
print(f"  ADOPTING: Dimensionally consistent formula (Cases 2/3)")
print(f"  P_diss = (gamma_eff/H) * H^2 / (4 pi^2 eps c_s^2 M_Pl^2)")

# =============================================================================
# SECTION 15: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: DISSIPATIVE-AS-67")
print("=" * 78)

# The decisive gap: use the corrected formula with primary estimate C, c_BLV
gap_decisive = gap_corr_C
P_decisive = P_corr_C
ratio_decisive_final = ratio_corr_C

# For comparison, compute the dissipative A_s (the actual predicted value)
A_s_diss = P_decisive
gap_abs = abs(gap_decisive)

if gap_abs < 1.0:
    verdict = "PASS"
    detail = (f"Dissipative A_s = {A_s_diss:.4e}, within {gap_abs:.2f} OOM of Planck. "
              f"Noise-dominated regime reached.")
elif gap_abs > 2.0:
    verdict = "FAIL"
    detail = (f"Dissipative A_s = {A_s_diss:.4e}, gap = {gap_decisive:.2f} OOM (> 2.0 threshold). "
              f"Transit too brief (N_e = {Ne_primary:.4e}) for dissipative regime. "
              f"gamma_eff/H = {g_eff_C/H_phys:.4e} << 1.")
else:
    verdict = "INFO"
    detail = (f"Dissipative A_s = {A_s_diss:.4e}, gap = {gap_decisive:.2f} OOM (between 1-2 OOM). "
              f"Partial improvement from dissipation but insufficient alone.")

print(f"\n  Gate: DISSIPATIVE-AS-67")
print(f"  Pre-registered criterion:")
print(f"    PASS: Dissipative A_s within 1 OOM of Planck (2.1e-9)")
print(f"    FAIL: Dissipative A_s still > 2 OOM from Planck")
print(f"    INFO: Dissipative correction is O(1) but insufficient alone")
print(f"\n  Decisive numbers:")
print(f"    gamma_C = {gamma_C:.4f} M_KK (microscopic, energy-balance estimate)")
print(f"    gamma_eff = {g_eff_C:.6e} M_KK (duty-cycle corrected)")
print(f"    gamma_eff / H = {g_eff_C/H_phys:.6e} (<<1: NOT in dissipative regime)")
print(f"    P_diss / P_std = {ratio_corr_C:.6e} (<<1: noise SUPPRESSED, not enhanced)")
print(f"    P_diss (c_BLV) = {P_decisive:.6e}")
print(f"    A_s (Planck) = {A_s_CMB:.1e}")
print(f"    gap = log10(P_diss / A_s) = {gap_decisive:.4f} OOM")
print(f"    |gap| = {gap_abs:.4f} OOM")
print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"\n  Comparison to prior results:")
print(f"    S64 PW-route gap:        {gap_revised_S64:.4f} OOM (best prior)")
print(f"    Standard GM (c_BLV):     {gap_std['c_BLV']:.4f} OOM")
print(f"    Dissipative (c_BLV):     {gap_decisive:.4f} OOM")
print(f"    Change from GM:          {gap_decisive - gap_std['c_BLV']:+.4f} OOM")
print(f"")
print(f"  STRUCTURAL LESSON:")
print(f"    The dissipative correction goes in the WRONG direction for gap closure.")
print(f"    gamma_eff << H means we are in the VACUUM-dominated regime, where")
print(f"    the noise contribution is NEGLIGIBLE compared to Bunch-Davies.")
print(f"    The dissipative formula gives P_diss << P_std (suppression, not enhancement).")
print(f"    The transit is too brief (N_e = {Ne_primary:.4e}) for the duty-cycle-")
print(f"    corrected gamma_eff to exceed H.")
print(f"")
print(f"    To reach the dissipative regime would require N_e > {PI*c_BLV**2*H_phys/gamma_C:.4f},")
print(f"    which is {PI*c_BLV**2*H_phys/gamma_C/Ne_primary:.0f}x the actual transit duration.")
print(f"    The impulsive nature of the transit (Mach {Mach_fric:.1f}) is structural")
print(f"    and cannot be changed without changing the spectral action itself.")
print(f"")
print(f"    Classification: FUNCTIONAL-INDEPENDENT (the gamma_eff << H result")
print(f"    depends only on N_e and the spectral action structure, not on the")
print(f"    choice of cutoff function f or the specific value of gamma).")

# =============================================================================
# SECTION 16: Save data
# =============================================================================
print(f"\n--- Section 16: Saving results ---")

np.savez(
    OUT_NPZ,
    # Input parameters
    H_phys=H_phys,
    H_phys_sq=H_phys_sq,
    M_Pl_sq=M_Pl_sq,
    eps_H_fold=eps_H_fold,
    c_BA=c_BA,
    c_BLV=c_BLV,
    c_mod=c_mod,
    Ne_primary=Ne_primary,
    Ne_range_lo=Ne_range_lo,
    Ne_range_hi=Ne_range_hi,
    Mach_fric=Mach_fric,
    v_terminal=v_terminal,
    dt_transit=dt_transit,
    beta_sq_universal=beta_sq_universal,

    # Microscopic gamma estimates
    gamma_A_impedance=gamma_A,
    gamma_B_natural=gamma_B,
    gamma_C_energy=gamma_C,
    gamma_D_kapitza=gamma_D,
    Gamma_impedance=Gamma_impedance,

    # Effective gamma (duty-cycle corrected)
    gamma_eff_A=gamma_A * Ne_primary / (2*PI),
    gamma_eff_B=gamma_B * Ne_primary / (2*PI),
    gamma_eff_C=g_eff_C,
    gamma_eff_D=gamma_D * Ne_primary / (2*PI),
    gamma_eff_primary=g_eff_C,

    # Ratios
    gamma_eff_over_H_C=g_eff_C / H_phys,
    ratio_diss_to_std_c_BLV=ratio_corr_C,
    BD_suppression_C=np.exp(-2.0 * g_eff_C / H_phys),

    # Power spectra
    P_std_c_mod=P_std['c_mod'],
    P_std_c_BLV=P_std['c_BLV'],
    P_std_c_BA=P_std['c_BA'],
    P_diss_c_BLV=P_decisive,
    A_s_CMB=A_s_CMB,

    # Gaps
    gap_std_c_mod=gap_std['c_mod'],
    gap_std_c_BLV=gap_std['c_BLV'],
    gap_std_c_BA=gap_std['c_BA'],
    gap_diss_c_BLV=gap_decisive,
    gap_revised_S64=gap_revised_S64,

    # Sensitivity scan
    g_eff_scan=g_eff_scan,
    gap_diss_scan=gap_diss_scan,
    g_eff_for_gap_zero=g_eff_zero,

    # Gate verdict
    gate_name='DISSIPATIVE-AS-67',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 17: Plot
# =============================================================================
print(f"\n--- Section 17: Generating plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

# Panel 1: gamma_eff scan vs gap
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogx(g_eff_scan, gap_diss_scan, 'b-', linewidth=2, label=f'Dissipative (c_s = c_BLV = {c_BLV:.3f})')
ax1.axhline(0, color='green', linestyle='--', linewidth=1.5, label='Planck A_s = 2.1e-9')
ax1.axhline(gap_revised_S64, color='orange', linestyle=':', linewidth=1.5, label=f'PW route: {gap_revised_S64:.2f} OOM')
for gname, gdata in gamma_eff_dict.items():
    ge = gdata['gamma_eff']
    gd = np.log10((H_phys_sq * ge / H_phys) / (4*PI**2*eps_H_fold*c_BLV**2*M_Pl_sq) / A_s_CMB)
    marker = 'o' if 'energy' in gname else 's'
    ax1.plot(ge, gd, marker, markersize=10, label=f'{gname}: {ge:.2e}')
ax1.set_xlabel(r'$\gamma_{\rm eff}$ [M_KK]', fontsize=12)
ax1.set_ylabel(r'$\log_{10}(P_{\rm diss}/A_s^{\rm Planck})$ [OOM]', fontsize=12)
ax1.set_title('Dissipative Gap vs Effective Friction', fontsize=13)
ax1.legend(fontsize=8, loc='upper left')
ax1.set_ylim(-5, 10)
ax1.grid(True, alpha=0.3)

# Panel 2: Bar chart of gamma estimates
ax2 = fig.add_subplot(gs[0, 1])
names = list(gammas.keys())
vals = [gammas[n] for n in names]
g_effs = [gammas[n] * Ne_primary / (2*PI) for n in names]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
bars = ax2.bar(range(len(names)), np.log10(vals), color=colors, alpha=0.8)
ax2.set_xticks(range(len(names)))
ax2.set_xticklabels([n.split('(')[1].rstrip(')') for n in names], fontsize=10)
ax2.set_ylabel(r'$\log_{10}(\gamma)$ [M_KK]', fontsize=12)
ax2.set_title('Microscopic Dissipation Rate Estimates', fontsize=13)
ax2.axhline(np.log10(H_phys), color='red', linestyle='--', linewidth=1.5,
            label=f'H_phys = {H_phys:.3f}')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, axis='y')

# Panel 3: Ratio P_diss/P_std for different gamma and c_s
ax3 = fig.add_subplot(gs[1, 0])
gamma_scan = np.logspace(-4, 2, 200)
for csname, cs in [('c_mod', c_mod), ('c_BLV', c_BLV), ('c_BA', c_BA)]:
    g_eff_scan2 = gamma_scan * Ne_primary / (2*PI)
    ratio_scan = 2.0 * g_eff_scan2 / (cs * H_phys)
    ax3.loglog(gamma_scan, ratio_scan, linewidth=2, label=f'{csname} = {cs:.3f}')
ax3.axhline(1.0, color='black', linestyle='--', linewidth=1, label='P_diss = P_std')
for gname, gdata in gamma_eff_dict.items():
    ax3.axvline(gdata['gamma'], color='gray', linestyle=':', alpha=0.5)
ax3.set_xlabel(r'$\gamma$ (microscopic) [M_KK]', fontsize=12)
ax3.set_ylabel(r'$P_{\rm diss}/P_{\rm std}$', fontsize=12)
ax3.set_title('Dissipative Correction Ratio', fontsize=13)
ax3.legend(fontsize=10)
ax3.set_ylim(1e-8, 1e4)
ax3.grid(True, alpha=0.3)

# Panel 4: Summary text
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
summary_text = (
    f"DISSIPATIVE-AS-67: {verdict}\n\n"
    f"Key numbers:\n"
    f"  gamma_C = {gamma_C:.2f} M_KK (energy balance)\n"
    f"  gamma_eff = {g_eff_C:.4e} M_KK\n"
    f"  gamma_eff / H = {g_eff_C/H_phys:.4e}\n"
    f"  N_e = {Ne_primary:.4e}\n\n"
    f"Power spectrum gaps:\n"
    f"  Standard GM (c_BLV): {gap_std['c_BLV']:.2f} OOM\n"
    f"  Dissipative (c_BLV): {gap_decisive:.2f} OOM\n"
    f"  S64 PW route:        {gap_revised_S64:.2f} OOM\n\n"
    f"P_diss / P_std = {ratio_corr_C:.4e}\n"
    f"  => Dissipation SUPPRESSES, not enhances\n\n"
    f"Lesson: Transit too brief (N_e << 1)\n"
    f"for noise to dominate over vacuum.\n"
    f"gamma_eff << H by {-np.log10(g_eff_C/H_phys):.1f} orders."
)
ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
         fontsize=11, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('S67 DISSIPATIVE-AS-67: Noise-Dominated A_s Normalization', fontsize=14, fontweight='bold')
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# =============================================================================
# Final timing
# =============================================================================
elapsed = time.time() - t_start
print(f"\nTotal runtime: {elapsed:.2f} s")
print("DONE.")
