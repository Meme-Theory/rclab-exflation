#!/usr/bin/env python3
"""
s61_pairing_chain.py — Nuclear Pairing Chain Attenuation (PAIRING-CHAIN-61)
===========================================================================

Gate: PAIRING-CHAIN-61 (INFO)
Pre-registered criterion: Monotonic decrease of Delta/E_F across inheritance
    levels = inheritance support. Non-monotonic = no pattern.

Computes Delta/E_F at three inheritance levels:
    Level 0: Substrate (M4 x SU(3) BCS, 8-mode system)
    Level 3: Nuclear matter (neutron 1S0 pairing)
    Level 5: Superfluid 3He-B (p-wave BCS)

References:
    - Papers 02, 03, 08, 15, 17 from researchers/Nazarewicz/
    - Gezerlis et al., PRC 81 (2010) 025803 (neutron matter gap)
    - Greywall, PRA 33 (1986) 3059 (3He Fermi liquid parameters)
    - Vollhardt & Woelfle, "The Superfluid Phases of Helium 3" (1990)

Session 61 | 2026-03-28
"""

import numpy as np
import matplotlib.pyplot as plt
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    Delta_0_GL, Delta_0_OES, E_cond, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_BCS_over_BW, k_B, Delta_B3
)

# =============================================================================
# LEVEL 0: Substrate (M4 x SU(3) BCS system)
# =============================================================================
# The 8-mode BCS system has sectors B1 (1 mode), B2 (4 modes), B3 (3 modes)
# with single-particle energies at the fold (tau = 0.19).
#
# B2 bandwidth: xi_BCS / BW = 13.95, xi_BCS = 0.808 M_KK
# => BW = xi_BCS / xi_BCS_over_BW
BW_B2 = xi_BCS / xi_BCS_over_BW  # B2 bandwidth in M_KK

# The full single-particle spectrum spans from E_B1 to E_B3_mean.
# Total bandwidth: E_B3 - E_B1
BW_total = E_B3_mean - E_B1  # = 0.978 - 0.819 = 0.159 M_KK

# For the Fermi energy scale, multiple definitions are physically meaningful:
#
# Definition 1: E_F = E_B2_mean (chemical potential ~ center of occupied band)
#   This is the natural choice: mu sits near the B2 sector center at half-filling.
#   Delta/E_F = Delta_0_GL / E_B2_mean
#
# Definition 2: E_F = BW_total/2 (half-bandwidth, standard tight-binding convention)
#   Delta/E_F = Delta_0_GL / (BW_total/2)
#
# Definition 3: E_F = |E_cond| (condensation energy as the relevant scale)
#   This is a DIFFERENT quantity — not a Fermi energy but the binding energy.
#
# We use Definition 1 (chemical potential) as primary, report all three.

# Gap values
Delta_GL = Delta_0_GL       # = 0.770 M_KK (GL gap, order parameter amplitude)
Delta_OES = Delta_0_OES     # = 0.464 M_KK (odd-even staggering gap)

# Fermi energy definitions
E_F_chem = E_B2_mean        # Chemical potential ~ B2 center = 0.845 M_KK
E_F_halfBW = BW_total / 2   # Half-bandwidth = 0.080 M_KK
E_F_cond = abs(E_cond)      # |E_cond| = 0.137 M_KK

# Primary ratio: Delta_GL / E_F(chemical potential)
ratio_L0_primary = Delta_GL / E_F_chem
# Using OES gap instead:
ratio_L0_OES = Delta_OES / E_F_chem
# Using half-bandwidth:
ratio_L0_halfBW = Delta_GL / E_F_halfBW
# Using condensation energy:
ratio_L0_cond = Delta_GL / E_F_cond

print("=" * 70)
print("LEVEL 0: Substrate BCS (M4 x SU(3), 8-mode system)")
print("=" * 70)
print(f"  Delta_GL     = {Delta_GL:.4f} M_KK")
print(f"  Delta_OES    = {Delta_OES:.4f} M_KK")
print(f"  Delta_B3     = {Delta_B3:.3f} M_KK (B3 sector gap)")
print(f"  E_B1         = {E_B1:.4f} M_KK")
print(f"  E_B2_mean    = {E_B2_mean:.4f} M_KK")
print(f"  E_B3_mean    = {E_B3_mean:.4f} M_KK")
print(f"  BW_B2        = {BW_B2:.4f} M_KK")
print(f"  BW_total     = {BW_total:.4f} M_KK")
print(f"  |E_cond|     = {abs(E_cond):.4f} M_KK")
print()
print(f"  Delta/E_F (chemical potential) = {ratio_L0_primary:.4f}")
print(f"  Delta/E_F (OES gap, chem pot)  = {ratio_L0_OES:.4f}")
print(f"  Delta/E_F (half-bandwidth)     = {ratio_L0_halfBW:.4f}")
print(f"  Delta/E_F (condensation energy)= {ratio_L0_cond:.4f}")

# =============================================================================
# LEVEL 3: Nuclear Matter (neutron 1S0 pairing)
# =============================================================================
# Standard nuclear matter values from BCS calculations:
#   - Free neutron gas at saturation density: k_F ~ 1.33 fm^{-1}
#   - E_F(neutron) = hbar^2 k_F^2 / (2m_n) ~ 37 MeV
#   - Gap peaks at subnuclear density: Delta_n ~ 1-3 MeV
#     (peak near k_F ~ 0.85 fm^{-1}, E_F ~ 15 MeV)
#
# There are TWO distinct nuclear pairing regimes:
#
# (a) Finite nuclei: Delta ~ 12/sqrt(A) MeV (empirical). For A ~ 120:
#     Delta ~ 1.1 MeV. E_F ~ 37 MeV (well depth - separation energy).
#     This is what Papers 02, 03, 08, 17 treat.
#
# (b) Infinite nuclear matter: neutron 1S0 gap peaks at k_F ~ 0.85 fm^{-1}
#     where Delta_max ~ 2.5 MeV and E_F ~ 15 MeV.
#     At saturation k_F=1.33: Delta ~ 1 MeV, E_F ~ 37 MeV.
#
# We report both. The finite nucleus case is the better analog (finite system).

# Finite nuclei
Delta_nucleus_low = 1.0     # MeV (heavy nuclei, A ~ 200)  # (local)
Delta_nucleus_mid = 1.5     # MeV (medium mass, A ~ 100)  # (local)
Delta_nucleus_high = 2.5    # MeV (light nuclei near peak, A ~ 30)  # (local)
E_F_nucleus = 37.0          # MeV (Fermi energy, well-depth convention)  # (local)

# Neutron matter at peak (k_F ~ 0.85 fm^{-1})
Delta_nm_peak = 2.5         # MeV (1S0 gap peak, Gezerlis et al.)  # (local)
E_F_nm_peak = 15.0          # MeV (at peak density)  # (local)

# Neutron matter at saturation (k_F = 1.33 fm^{-1})
Delta_nm_sat = 1.0          # MeV (at saturation, declining from peak)  # (local)
E_F_nm_sat = 37.0           # MeV  # (local)

ratio_L3_finite_low = Delta_nucleus_low / E_F_nucleus
ratio_L3_finite_mid = Delta_nucleus_mid / E_F_nucleus
ratio_L3_finite_high = Delta_nucleus_high / E_F_nucleus
ratio_L3_nm_peak = Delta_nm_peak / E_F_nm_peak
ratio_L3_nm_sat = Delta_nm_sat / E_F_nm_sat

print()
print("=" * 70)
print("LEVEL 3: Nuclear Matter (neutron 1S0 BCS pairing)")
print("=" * 70)
print(f"  Finite nuclei:")
print(f"    Delta = {Delta_nucleus_low}-{Delta_nucleus_high} MeV, E_F = {E_F_nucleus} MeV")
print(f"    Delta/E_F = {ratio_L3_finite_low:.4f} - {ratio_L3_finite_high:.4f}")
print(f"    Central value: {ratio_L3_finite_mid:.4f}")
print(f"  Neutron matter (peak, k_F ~ 0.85 fm^{{-1}}):")
print(f"    Delta = {Delta_nm_peak} MeV, E_F = {E_F_nm_peak} MeV")
print(f"    Delta/E_F = {ratio_L3_nm_peak:.4f}")
print(f"  Neutron matter (saturation, k_F = 1.33 fm^{{-1}}):")
print(f"    Delta = {Delta_nm_sat} MeV, E_F = {E_F_nm_sat} MeV")
print(f"    Delta/E_F = {ratio_L3_nm_sat:.4f}")

# =============================================================================
# LEVEL 5: Superfluid 3He-B (p-wave BCS)
# =============================================================================
# 3He-B is a p-wave (L=1, S=1, J=0) BCS superfluid.
# T_c ~ 2.5 mK at SVP (saturated vapor pressure, P=0 bar).
# At melting pressure (P=34.4 bar), T_c ~ 2.6 mK.
#
# Gap: Delta(T=0) = 1.764 * k_B * T_c (weak-coupling BCS)
# Strong-coupling corrections increase this by ~10-20%.
#
# Fermi energy: E_F = k_B * T_F, where T_F ~ 1.5 K at SVP.
# This uses the effective mass m* ~ 3.05 m_3.
# With bare mass: T_F ~ 4.9 K.
#
# We use the quasiparticle (effective mass) convention for consistency
# with the BCS framework, where pairing occurs at the Fermi surface
# of dressed quasiparticles.

T_c_3He = 2.5e-3             # K (SVP)  # (local)
T_F_3He = 1.5                # K (effective mass, SVP)  # (local)
T_F_3He_bare = 4.9           # K (bare mass, SVP)  # (local)

# Weak-coupling BCS gap
Delta_3He_wc = 1.764 * k_B * T_c_3He  # eV
# Strong-coupling corrected (factor ~1.15)
Delta_3He_sc = 1.15 * Delta_3He_wc    # eV

E_F_3He_eff = k_B * T_F_3He           # eV (effective mass)
E_F_3He_bare = k_B * T_F_3He_bare     # eV (bare mass)

ratio_L5_wc_eff = Delta_3He_wc / E_F_3He_eff
ratio_L5_sc_eff = Delta_3He_sc / E_F_3He_eff
ratio_L5_wc_bare = Delta_3He_wc / E_F_3He_bare
ratio_L5_sc_bare = Delta_3He_sc / E_F_3He_bare

# Also express in absolute units
print()
print("=" * 70)
print("LEVEL 5: Superfluid 3He-B (p-wave BCS)")
print("=" * 70)
print(f"  T_c          = {T_c_3He*1e3:.1f} mK")
print(f"  T_F (eff)    = {T_F_3He:.1f} K")
print(f"  T_F (bare)   = {T_F_3He_bare:.1f} K")
print(f"  Delta (w.c.) = {Delta_3He_wc:.4e} eV = {Delta_3He_wc/k_B*1e3:.3f} mK")
print(f"  Delta (s.c.) = {Delta_3He_sc:.4e} eV = {Delta_3He_sc/k_B*1e3:.3f} mK")
print(f"  E_F (eff)    = {E_F_3He_eff:.4e} eV = {E_F_3He_eff/k_B:.2f} K")
print(f"  E_F (bare)   = {E_F_3He_bare:.4e} eV = {E_F_3He_bare/k_B:.2f} K")
print()
print(f"  Delta/E_F (w.c., eff mass)  = {ratio_L5_wc_eff:.4e}")
print(f"  Delta/E_F (s.c., eff mass)  = {ratio_L5_sc_eff:.4e}")
print(f"  Delta/E_F (w.c., bare mass) = {ratio_L5_wc_bare:.4e}")
print(f"  Delta/E_F (s.c., bare mass) = {ratio_L5_sc_bare:.4e}")

# =============================================================================
# COMPARISON AND ATTENUATION FIT
# =============================================================================
# Use central values for each level:
#   L0: Delta_GL / E_B2_mean (primary)
#   L3: Delta_nucleus_mid / E_F_nucleus = 1.5/37 (finite nuclei central)
#   L5: Delta_3He_sc / E_F_3He_eff (strong-coupling, effective mass)

levels = np.array([0, 3, 5])
ratios_central = np.array([ratio_L0_primary, ratio_L3_finite_mid, ratio_L5_sc_eff])

# Log-linear fit: log10(Delta/E_F) = a - b * level
log_ratios = np.log10(ratios_central)
coeffs = np.polyfit(levels, log_ratios, 1)
slope = coeffs[0]           # = -b (attenuation per level)
intercept = coeffs[1]       # = a (log10 ratio at level 0)
A_attenuation = 10**(-slope)  # Attenuation factor per level

# Fit quality
log_fit = np.polyval(coeffs, levels)
residuals = log_ratios - log_fit
rms_residual = np.sqrt(np.mean(residuals**2))

# Check monotonicity
is_monotone = all(ratios_central[i] > ratios_central[i+1] for i in range(len(ratios_central)-1))

# Span in decades
total_span = log_ratios[0] - log_ratios[-1]
span_0_to_3 = log_ratios[0] - log_ratios[1]
span_3_to_5 = log_ratios[1] - log_ratios[2]

print()
print("=" * 70)
print("INHERITANCE CHAIN COMPARISON")
print("=" * 70)
print()
print(f"  Level  System              Delta/E_F         log10")
print(f"  -----  ------------------  ----------------  ------")
print(f"  0      Substrate (BCS)     {ratios_central[0]:.4f}            {log_ratios[0]:+.3f}")
print(f"  3      Nuclear (finite)    {ratios_central[1]:.4f}            {log_ratios[1]:+.3f}")
print(f"  5      3He-B (p-wave)      {ratios_central[2]:.4e}       {log_ratios[2]:+.3f}")
print()
print(f"  Monotonic decrease: {is_monotone}")
print(f"  Total span: {total_span:.2f} decades (L0 to L5)")
print(f"  L0->L3 span: {span_0_to_3:.2f} decades")
print(f"  L3->L5 span: {span_3_to_5:.2f} decades")
print()
print(f"  Log-linear fit: log10(Delta/E_F) = {intercept:.3f} + ({slope:.3f}) * level")
print(f"  Attenuation factor A = 10^{{-slope}} = {A_attenuation:.2f} per level")
print(f"  (Delta/E_F ~ {A_attenuation:.1f}^{{-level}})")
print(f"  RMS residual: {rms_residual:.4f} decades")
print()

# =============================================================================
# UNCERTAINTY BAND: Report ranges, not just central values
# =============================================================================
# Level 0: Delta_OES vs Delta_GL, and different E_F definitions
L0_range = [Delta_OES / E_B2_mean, Delta_GL / E_F_halfBW]  # conservative to liberal
L0_central = ratio_L0_primary

# Level 3: Low to peak nuclear matter
L3_range = [ratio_L3_nm_sat, ratio_L3_nm_peak]
L3_central = ratio_L3_finite_mid

# Level 5: weak-coupling/bare to strong-coupling/effective
L5_range = [ratio_L5_wc_bare, ratio_L5_sc_eff]
L5_central = ratio_L5_sc_eff

print("UNCERTAINTY ASSESSMENT:")
print(f"  L0 range: [{L0_range[0]:.3f}, {L0_range[1]:.3f}] (OES/chem to GL/half-BW)")
print(f"  L3 range: [{L3_range[0]:.4f}, {L3_range[1]:.4f}] (sat. to peak)")
print(f"  L5 range: [{L5_range[0]:.4e}, {L5_range[1]:.4e}] (wc/bare to sc/eff)")
print()

# Check if monotonicity holds across ENTIRE uncertainty band
# Worst case: L0 min, L3 max, L5 max
worst_mono = (min(L0_range) > max(L3_range)) and (min(L3_range) > max(L5_range))
print(f"  Monotonicity across full uncertainty band: {worst_mono}")

# =============================================================================
# NUCLEAR-SPECIFIC PHYSICS ASSESSMENT (Nazarewicz perspective)
# =============================================================================
print()
print("=" * 70)
print("NUCLEAR PHYSICS ASSESSMENT")
print("=" * 70)
print()
print("  The substrate BCS system has Delta/E_F ~ 0.91 (using GL gap / mu).")
print("  This places it firmly in the BCS-BEC CROSSOVER regime, not weak-coupling")
print("  BCS. For comparison:")
print()
print("  System               Delta/E_F   Regime")
print("  -------------------  ---------   ------")
print(f"  Substrate (L0)       {ratio_L0_primary:.3f}       BCS-BEC crossover")
print(f"  Nuclear (peak, L3)   {ratio_L3_nm_peak:.3f}       Moderate BCS (crossover edge)")
print(f"  Nuclear (sat., L3)   {ratio_L3_nm_sat:.4f}      Weak-coupling BCS")
print(f"  3He-B (L5)           {ratio_L5_sc_eff:.2e}   Deep weak-coupling BCS")
print(f"  Metallic SC          ~1e-4       Deep weak-coupling BCS")
print(f"  Ultracold atoms      ~1-10       BEC side")
print()
print("  The nuclear pairing gap at PEAK density (k_F~0.85 fm^{-1}) has")
print("  Delta/E_F ~ 0.17, which is at the BCS-BEC crossover boundary.")
print("  This is consistent with Nazarewicz Paper 15 (Richardson-Gaudin exact")
print("  solution) showing nuclear pairing at the edge of the crossover.")
print()
print("  CRITICAL: The substrate Delta/E_F ~ 0.91 means the gap is comparable")
print("  to the Fermi energy. This is NOT weak-coupling BCS. The Bogoliubov")
print("  quasiparticle picture remains valid (as confirmed by S53 coherence")
print("  factors: Z_k = 0.250 for B1 mode), but the system is in the unitary")
print("  regime where mean-field BCS requires beyond-BCS corrections.")
print("  Paper 17 (ultrasmall BCS) and Paper 15 (Richardson-Gaudin) show that")
print("  exact methods are essential in this regime.")

# =============================================================================
# ATTENUATION RATE PHYSICS
# =============================================================================
print()
print("=" * 70)
print("ATTENUATION RATE ANALYSIS")
print("=" * 70)
print()
print(f"  The log-linear fit gives {-slope:.3f} decades per inheritance level.")
print(f"  Attenuation factor A = {A_attenuation:.1f}x per level.")
print()
print("  Decomposition of the attenuation:")
print(f"    L0 -> L3 (3 levels): {span_0_to_3:.2f} decades = {span_0_to_3/3:.2f} per level")
print(f"    L3 -> L5 (2 levels): {span_3_to_5:.2f} decades = {span_3_to_5/2:.2f} per level")
print()

# The rates per level are NOT equal — check
rate_03 = span_0_to_3 / 3
rate_35 = span_3_to_5 / 2
rate_ratio = rate_35 / rate_03
print(f"  Rate ratio (L3-L5)/(L0-L3) = {rate_ratio:.2f}")
print(f"  {'Attenuation ACCELERATES' if rate_ratio > 1 else 'Attenuation DECELERATES'} from L3 to L5.")
print()
if abs(rate_ratio - 1.0) < 0.3:
    print("  The attenuation rate is approximately constant (within 30%).")
    print("  This supports a GEOMETRIC attenuation model: each inheritance level")
    print("  reduces Delta/E_F by the same multiplicative factor.")
else:
    print(f"  The attenuation rate varies by {abs(rate_ratio-1)*100:.0f}% between segments.")
    print("  This suggests the attenuation is NOT purely geometric.")
    print("  Physical interpretation: different inheritance levels involve")
    print("  different pairing mechanisms (s-wave nuclear vs p-wave 3He).")

# =============================================================================
# GATE VERDICT
# =============================================================================
print()
print("=" * 70)
print("GATE VERDICT: PAIRING-CHAIN-61")
print("=" * 70)
print()
verdict = "INFO"
if is_monotone:
    print(f"  Delta/E_F is MONOTONICALLY DECREASING across all three levels.")
    print(f"  L0 ({ratios_central[0]:.3f}) > L3 ({ratios_central[1]:.4f}) > L5 ({ratios_central[2]:.2e})")
    print(f"  Monotonicity holds across full uncertainty band: {worst_mono}")
    if worst_mono:
        print(f"  Inheritance pattern SUPPORTED (robust to parameter choices).")
    else:
        print(f"  Inheritance pattern supported for central values only.")
        print(f"  Uncertainty bands may overlap at L0-L3 boundary.")
else:
    print(f"  Delta/E_F is NOT monotonically decreasing.")
    print(f"  No systematic inheritance pattern found.")

print(f"\n  Verdict: {verdict}")
print(f"  (Pre-registered: monotonic = inheritance support; non-monotonic = no pattern)")

# =============================================================================
# SAVE DATA
# =============================================================================
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s61_pairing_chain.npz")
np.savez(save_path,
    # Levels
    levels=levels,
    ratios_central=ratios_central,
    log_ratios=log_ratios,
    # Level 0
    Delta_GL=Delta_GL,
    Delta_OES=Delta_OES,
    E_F_chem=E_F_chem,
    E_F_halfBW=E_F_halfBW,
    E_F_cond=E_F_cond,
    BW_B2=BW_B2,
    BW_total=BW_total,
    ratio_L0_primary=ratio_L0_primary,
    ratio_L0_OES=ratio_L0_OES,
    ratio_L0_halfBW=ratio_L0_halfBW,
    ratio_L0_cond=ratio_L0_cond,
    # Level 3
    Delta_nucleus_mid=Delta_nucleus_mid,
    E_F_nucleus=E_F_nucleus,
    ratio_L3_finite_low=ratio_L3_finite_low,
    ratio_L3_finite_mid=ratio_L3_finite_mid,
    ratio_L3_finite_high=ratio_L3_finite_high,
    ratio_L3_nm_peak=ratio_L3_nm_peak,
    ratio_L3_nm_sat=ratio_L3_nm_sat,
    # Level 5
    Delta_3He_wc=Delta_3He_wc,
    Delta_3He_sc=Delta_3He_sc,
    E_F_3He_eff=E_F_3He_eff,
    E_F_3He_bare=E_F_3He_bare,
    ratio_L5_wc_eff=ratio_L5_wc_eff,
    ratio_L5_sc_eff=ratio_L5_sc_eff,
    ratio_L5_wc_bare=ratio_L5_wc_bare,
    ratio_L5_sc_bare=ratio_L5_sc_bare,
    # Fit
    slope=slope,
    intercept=intercept,
    A_attenuation=A_attenuation,
    rms_residual=rms_residual,
    is_monotone=is_monotone,
    worst_mono=worst_mono,
    # Ranges
    L0_range=L0_range,
    L3_range=L3_range,
    L5_range=L5_range,
    # Verdict
    verdict=verdict
)
print(f"\n  Data saved: {save_path}")

# =============================================================================
# PLOT
# =============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Main comparison ---
# Central values with error bars
L0_err = [[ratio_L0_primary - L0_range[0]], [L0_range[1] - ratio_L0_primary]]
L3_err = [[ratio_L3_finite_mid - L3_range[0]], [L3_range[1] - ratio_L3_finite_mid]]
L5_err = [[ratio_L5_sc_eff - L5_range[0]], [L5_range[1] - ratio_L5_sc_eff]]

ax1.errorbar(levels, ratios_central, yerr=[
    [ratio_L0_primary - L0_range[0], ratio_L3_finite_mid - L3_range[0], ratio_L5_sc_eff - L5_range[0]],
    [L0_range[1] - ratio_L0_primary, L3_range[1] - ratio_L3_finite_mid, L5_range[1] - ratio_L5_sc_eff]
], fmt='s', markersize=10, color='navy', ecolor='steelblue', elinewidth=2,
   capsize=5, capthick=2, label='Central values', zorder=5)

# Fit line
levels_fine = np.linspace(-0.5, 5.5, 100)
fit_line = 10**(intercept + slope * levels_fine)
ax1.plot(levels_fine, fit_line, '--', color='firebrick', linewidth=1.5,
         label=f'Fit: $A^{{-\\ell}}$, A={A_attenuation:.1f}')

ax1.set_yscale('log')
ax1.set_xlabel('Inheritance Level', fontsize=13)
ax1.set_ylabel(r'$\Delta / E_F$', fontsize=14)
ax1.set_title('Pairing Chain Attenuation\n(PAIRING-CHAIN-61)', fontsize=13, fontweight='bold')
ax1.set_xticks([0, 3, 5])
ax1.set_xticklabels(['L0\nSubstrate', 'L3\nNuclear', 'L5\n$^3$He-B'], fontsize=11)
ax1.set_xlim(-0.5, 5.8)
ax1.legend(fontsize=10, loc='upper right')
ax1.grid(True, alpha=0.3, which='both')

# Annotate values
for i, (lev, rat) in enumerate(zip(levels, ratios_central)):
    if rat > 0.01:
        ax1.annotate(f'{rat:.3f}', (lev + 0.15, rat), fontsize=10, color='navy')
    else:
        ax1.annotate(f'{rat:.2e}', (lev + 0.15, rat), fontsize=10, color='navy')

# --- Right panel: BCS regime classification ---
# Show where each system falls on the BCS-BEC crossover diagram
systems = ['Substrate\n(L0)', 'Nuclear\npeak (L3)', 'Nuclear\nsat. (L3)', '$^3$He-B\n(L5)',
           'Metallic\nSC', 'Ultracold\natoms']
ratios_all = [ratio_L0_primary, ratio_L3_nm_peak, ratio_L3_nm_sat,
              ratio_L5_sc_eff, 1e-4, 3.0]
colors = ['darkred', 'darkorange', 'goldenrod', 'steelblue', 'gray', 'purple']

ax2.barh(range(len(systems)), ratios_all, color=colors, height=0.6, alpha=0.8)
ax2.set_xscale('log')
ax2.set_yticks(range(len(systems)))
ax2.set_yticklabels(systems, fontsize=10)
ax2.set_xlabel(r'$\Delta / E_F$', fontsize=14)
ax2.set_title('BCS-BEC Crossover Classification', fontsize=13, fontweight='bold')
ax2.axvline(x=0.1, color='red', linestyle=':', linewidth=1.5, label='BCS-BEC boundary')
ax2.axvline(x=1e-2, color='green', linestyle=':', linewidth=1.5, label='Weak-coupling limit')
ax2.legend(fontsize=9, loc='lower right')
ax2.grid(True, alpha=0.3, which='both', axis='x')

# Annotate bars
for i, rat in enumerate(ratios_all):
    if rat > 0.01:
        ax2.text(rat * 1.3, i, f'{rat:.3f}', va='center', fontsize=9)
    else:
        ax2.text(rat * 1.5, i, f'{rat:.1e}', va='center', fontsize=9)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s61_pairing_chain.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")
plt.close()

print("\n  DONE.")
