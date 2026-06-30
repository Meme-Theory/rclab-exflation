#!/usr/bin/env python3
"""
s65_vanhove_as.py — Van Hove Enhancement of A_s Transfer Function
=================================================================

Gate: VANHOVE-AS-65 = INFO
  Report van Hove enhancement factor and revised A_s gap in OOM.

PHYSICS — RESONANCE STRUCTURE:
    The phonon density of states (DOS) on the M4 x SU(3) fabric has van Hove
    singularities (VHS) wherever the group velocity vanishes: dE/dk = 0.
    At these frequencies the cavity mode density diverges (in 1D, as
    |E - E_VH|^{-1/2}). The B2[0] flat band has the slowest group velocity
    (c_L = 0.019-0.032 M_KK, from S64) and therefore the strongest VHS.

    For the scalar amplitude A_s, the relevant modes are the (0,0) Peter-Weyl
    sector — the ONLY singlet modes that project to 4D scalar perturbations.
    These modes have discrete energies at omega_00 = {0.820, 0.845, 0.971} M_KK
    (from S64 transfer computation).

    The van Hove enhancement enters A_s through TWO channels:

    Channel 1 — DOS enhancement of tunneling:
        The Bogoliubov transmission through hybridization gaps depends on the
        local DOS. The effective bandwidth W_eff ~ g(E) * W_bare. Higher DOS
        means better transmission:
            |T_j|^2 = 1 / (1 + (Delta_j / W_eff)^2 * pi^2/4)

    Channel 2 — Mode density enhancement of perturbation amplitude:
        A_s ~ |delta phi|^2 ~ (spectral weight at E) * (DOS at E)
        The DOS enters quadratically because both the perturbation source
        and the propagator are enhanced by the mode density.

    The enhancement factor is:
        R_VH = g(E_00) / g_avg
    where g(E_00) is the DOS at the (0,0) sector energies and g_avg is the
    spectrum-averaged DOS.

    The QUADRATIC entry means:
        A_s^{enh} = A_s^{bare} * R_VH^2

    This is the standard Fermi golden rule enhancement: transition rate
    goes as matrix element squared TIMES final-state DOS. For perturbation
    spectra, both the emission and absorption amplitudes see the DOS.

    CONDENSED MATTER ANALOG:
        This is identical to the van Hove enhancement of the BCS critical
        temperature in materials with flat bands. In twisted bilayer graphene,
        the flat band DOS enhancement leads to T_c ~ g(E_F)^2 * V^2,
        where g(E_F)/g_avg can reach 10-100x. In our phononic crystal, the
        B2[0] flat band provides an analogous enhancement, but the (0,0) sector
        energies must COINCIDE with the VHS for this to matter.

    TESLA TEST:
        Can you build it? — Yes: compute g(E)/g_avg from the S63 phonon DOS.
        Can you measure it? — Yes: A_s^{enh} modifies the A_s gap in OOM.
        Does it resonate? — Yes: the VHS IS a resonance condition (standing wave
        at the BZ boundary where the group velocity vanishes).

Session: S65 W5-E
Author: tesla-resonance
Depends on: S63 phonon_dos, S64 transfer_bogoliubov, S64 linewidth_hierarchy
"""

import sys
import os
import time
import numpy as np
from pathlib import Path
from scipy.integrate import trapezoid
from scipy.signal import find_peaks

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, M_KK, M_KK_gravity,
    A_s_CMB, PI, Delta_0_OES, E_cond,
    Vol_SU3_Haar, G_DeWitt, E_B1, E_B2_mean, E_B3_mean,
    Delta_B3, rho_B2_per_mode,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s65_vanhove_as.npz"
OUT_PNG = SCRIPT_DIR / "s65_vanhove_as.png"

t0 = time.time()
print("=" * 78)
print("VANHOVE-AS-65: Van Hove Enhancement of A_s Transfer Function")
print("=" * 78)

# =============================================================================
# SECTION 1: Load input data
# =============================================================================
print("\n--- Section 1: Load input data ---")

# Phonon DOS from S63
dos_data = np.load(SCRIPT_DIR / "s63_phonon_dos.npz", allow_pickle=True)
omega_grid = dos_data['omega_grid']
g_narrow = dos_data['g_narrow']         # Total DOS, narrow smoothing (sigma=0.03)
g_broad = dos_data['g_broad']           # Total DOS, broad smoothing (sigma=0.10)
g_B_narrow = dos_data['g_B_narrow']     # B-sector DOS, narrow
g_B_broad = dos_data['g_B_broad']       # B-sector DOS, broad
g_A_narrow = dos_data['g_A_narrow']     # A-sector DOS, narrow
g_C_narrow = dos_data['g_C_narrow']     # C-sector DOS, narrow
vhs_omega = dos_data['vhs_omega']
vhs_type = dos_data['vhs_type']
vhs_band = dos_data['vhs_band']
vhs_sector = dos_data['vhs_sector']
vhs_curvature = dos_data['vhs_curvature']
bandwidths = dos_data['bandwidths']

# Bogoliubov transfer from S64
tf_data = np.load(SCRIPT_DIR / "s64_transfer_bogoliubov.npz", allow_pickle=True)
omega_00 = tf_data['omega_00']          # (0,0) sector mode energies
v2_00 = tf_data['v2_00']               # Bogoliubov v^2 coefficients
S_occ_00 = float(tf_data['S_occ_00'])  # (0,0) sector spectral occupation
S_occ_total = float(tf_data['S_occ_total'])  # Total spectral occupation
gap_occ_orig = float(tf_data['gap_occ_orig'])  # Original A_s gap (6.89 OOM)
gap_revised = float(tf_data['gap_revised'])     # Revised gap after transfer (3.16 OOM)
tight_gaps = tf_data['tight_gaps']
tight_detunings = tf_data['tight_detunings']
N_gaps = int(tf_data['N_gaps'])
beta_Gaussian_seq = float(tf_data['beta_Gaussian_seq'])

# Linewidth hierarchy from S64
lw_data = np.load(SCRIPT_DIR / "s64_linewidth_hierarchy.npz", allow_pickle=True)
E_qp = lw_data['E_qp']                 # Quasiparticle energies
labels = lw_data['labels']
Gamma_1loop = lw_data['Gamma_1loop']

print(f"  Loaded S63 phonon DOS: {len(omega_grid)} grid points, {len(vhs_omega)} VHS")
print(f"  Loaded S64 transfer: {N_gaps} gaps, gap_revised = {gap_revised:.4f} OOM")
print(f"  Loaded S64 linewidth: {len(E_qp)} quasiparticle modes")

# =============================================================================
# SECTION 2: Identify the resonance structure
# =============================================================================
print("\n--- Section 2: Resonance structure identification ---")
print("  WHAT OSCILLATES: Spectral action perturbations in the (0,0) Peter-Weyl sector")
print("  WHAT IS THE CAVITY: The 45-mode phonon crystal on deformed SU(3)")
print("  BOUNDARY CONDITIONS: Born-von Karman on the 32-cell Voronoi tessellation")
print("  NORMAL MODES: 45 bands, each with van Hove singularities at BZ boundaries")
print("  SELECTION RULE: Only (0,0) singlet modes project to 4D scalar perturbations")
print("  STANDING WAVE CONDITION: v_g = 0 at VHS => maximal mode density")

# =============================================================================
# SECTION 3: Compute average DOS quantities
# =============================================================================
print("\n--- Section 3: Average DOS quantities ---")

# Average DOS across full spectrum
omega_range = omega_grid[-1] - omega_grid[0]
g_avg_total_narrow = trapezoid(g_narrow, omega_grid) / omega_range
g_avg_total_broad = trapezoid(g_broad, omega_grid) / omega_range
g_avg_B_narrow = trapezoid(g_B_narrow, omega_grid) / omega_range
g_avg_B_broad = trapezoid(g_B_broad, omega_grid) / omega_range
g_avg_A_narrow = trapezoid(g_A_narrow, omega_grid) / omega_range

# Total mode count (integral of g gives N_modes)
N_modes_total = trapezoid(g_narrow, omega_grid)  # Should be ~ 45
N_modes_B = trapezoid(g_B_narrow, omega_grid)    # Should be ~ 9
N_modes_A = trapezoid(g_A_narrow, omega_grid)    # Should be ~ 27

print(f"  Total modes (integral of g): {N_modes_total:.2f} (expected: 45)")
print(f"  B-sector modes: {N_modes_B:.2f} (expected: 9)")
print(f"  A-sector modes: {N_modes_A:.2f} (expected: 27)")
print(f"  Average DOS: g_avg_total = {g_avg_total_narrow:.6f} (narrow), {g_avg_total_broad:.6f} (broad)")
print(f"  Average DOS: g_avg_B = {g_avg_B_narrow:.6f} (narrow), {g_avg_B_broad:.6f} (broad)")

# =============================================================================
# SECTION 4: DOS at (0,0) sector energies
# =============================================================================
print("\n--- Section 4: DOS at (0,0) sector energies ---")

# The (0,0) sector has 16 modes at 3 unique energies
# Note: omega_00 has floating-point noise at ~1e-15 level; round to 6 digits for grouping
unique_E00 = np.unique(np.round(omega_00, 6))
multiplicities = np.array([np.sum(np.abs(omega_00 - E) < 1e-4) for E in unique_E00])

print(f"  (0,0) sector unique energies: {unique_E00}")
print(f"  Multiplicities: {multiplicities}")

# DOS at each (0,0) energy for both smoothings
g_at_E00_narrow = np.zeros(len(unique_E00))
g_at_E00_broad = np.zeros(len(unique_E00))
g_B_at_E00_narrow = np.zeros(len(unique_E00))
g_B_at_E00_broad = np.zeros(len(unique_E00))

for i, E in enumerate(unique_E00):
    idx = np.argmin(np.abs(omega_grid - E))
    g_at_E00_narrow[i] = g_narrow[idx]
    g_at_E00_broad[i] = g_broad[idx]
    g_B_at_E00_narrow[i] = g_B_narrow[idx]
    g_B_at_E00_broad[i] = g_B_broad[idx]

print(f"\n  {'Energy (M_KK)':<15} {'mult':<6} {'g_total(nar)':<14} {'g_total(brd)':<14} {'g_B(nar)':<12} {'g_B(brd)':<12}")
for i, E in enumerate(unique_E00):
    print(f"  {E:<15.4f} {multiplicities[i]:<6d} {g_at_E00_narrow[i]:<14.4f} {g_at_E00_broad[i]:<14.4f} "
          f"{g_B_at_E00_narrow[i]:<12.4f} {g_B_at_E00_broad[i]:<12.4f}")

# =============================================================================
# SECTION 5: Van Hove enhancement factors
# =============================================================================
print("\n--- Section 5: Van Hove enhancement factors ---")

# Method 1: Enhancement at each (0,0) energy relative to average
# Use TOTAL DOS (all sectors contribute to the perturbation propagator)
R_VH_narrow = g_at_E00_narrow / g_avg_total_narrow
R_VH_broad = g_at_E00_broad / g_avg_total_broad

print(f"  Enhancement R_VH = g(E_00)/g_avg:")
for i, E in enumerate(unique_E00):
    print(f"    E = {E:.4f}: R_VH = {R_VH_narrow[i]:.4f} (narrow), {R_VH_broad[i]:.4f} (broad)")

# Method 2: Weighted average over (0,0) modes by their v^2 (Bogoliubov weight)
# Each mode contributes proportional to its spectral weight
v2_unique = np.array([np.mean(v2_00[np.abs(omega_00 - E) < 1e-6]) for E in unique_E00])

# Spectral-weight-weighted average enhancement
weight_v2 = multiplicities * v2_unique
weight_v2 /= weight_v2.sum()

R_VH_weighted_narrow = np.sum(weight_v2 * R_VH_narrow)
R_VH_weighted_broad = np.sum(weight_v2 * R_VH_broad)

print(f"\n  v^2 weights at each energy: {v2_unique}")
print(f"  Normalized spectral weights: {weight_v2}")
print(f"  Weighted R_VH = {R_VH_weighted_narrow:.6f} (narrow), {R_VH_weighted_broad:.6f} (broad)")

# Method 3: Compare B-sector DOS at (0,0) energies to B-sector average
R_VH_B_narrow = g_B_at_E00_narrow / g_avg_B_narrow
R_VH_B_broad = g_B_at_E00_broad / g_avg_B_broad
R_VH_B_weighted_narrow = np.sum(weight_v2 * R_VH_B_narrow)
R_VH_B_weighted_broad = np.sum(weight_v2 * R_VH_B_broad)

print(f"\n  B-sector enhancement R_VH_B = g_B(E_00)/g_avg_B:")
for i, E in enumerate(unique_E00):
    print(f"    E = {E:.4f}: R_VH_B = {R_VH_B_narrow[i]:.4f} (narrow), {R_VH_B_broad[i]:.4f} (broad)")
print(f"  Weighted R_VH_B = {R_VH_B_weighted_narrow:.6f} (narrow), {R_VH_B_weighted_broad:.6f} (broad)")

# =============================================================================
# SECTION 6: Nearest van Hove singularity analysis
# =============================================================================
print("\n--- Section 6: Nearest van Hove singularities to (0,0) modes ---")

b_mask = vhs_sector == 'B'
b_vhs_omega = vhs_omega[b_mask]
b_vhs_band = vhs_band[b_mask]
b_vhs_type = vhs_type[b_mask]
b_vhs_curv = vhs_curvature[b_mask]

for E in unique_E00:
    dist = np.abs(b_vhs_omega - E)
    nearest = np.argsort(dist)[:3]
    print(f"  E_00 = {E:.4f}:")
    for n in nearest:
        print(f"    VHS at omega={b_vhs_omega[n]:.4f} (band {b_vhs_band[n]}, type {b_vhs_type[n]}, "
              f"curv={b_vhs_curv[n]:.3e}, distance={dist[n]:.4f})")

# =============================================================================
# SECTION 7: Maximum possible van Hove enhancement in B-sector
# =============================================================================
print("\n--- Section 7: Maximum possible VHS enhancement ---")

# Find the largest B-sector DOS peak in the low-energy region (< 5 M_KK)
mask_low = omega_grid < 5.0
g_B_low_narrow = g_B_narrow[mask_low]
omega_low = omega_grid[mask_low]

peaks_idx, peak_props = find_peaks(g_B_low_narrow, height=0.1, distance=5)
peak_omegas = omega_low[peaks_idx]
peak_heights = g_B_low_narrow[peaks_idx]

# Sort by height descending
sort_idx = np.argsort(peak_heights)[::-1]
print(f"  Top 5 B-sector DOS peaks (omega < 5 M_KK, narrow smoothing):")
for i in range(min(5, len(sort_idx))):
    j = sort_idx[i]
    enh = peak_heights[j] / g_avg_B_narrow
    print(f"    omega={peak_omegas[j]:.4f}, g_B={peak_heights[j]:.4f}, enhancement={enh:.2f}x")

# Maximum enhancement if (0,0) modes were EXACTLY at the VHS
R_VH_max_B = g_B_low_narrow.max() / g_avg_B_narrow
R_VH_max_total = g_narrow[mask_low].max() / g_avg_total_narrow
print(f"\n  Maximum possible enhancement (if E_00 = E_VHS exactly):")
print(f"    B-sector: R_VH_max = {R_VH_max_B:.2f}x")
print(f"    Total:    R_VH_max = {R_VH_max_total:.2f}x")

# =============================================================================
# SECTION 8: 1D van Hove singularity structure near (0,0) energies
# =============================================================================
print("\n--- Section 8: 1D van Hove divergence structure ---")

# In 1D, the DOS near a van Hove singularity at E_VH goes as:
#   g(E) ~ 1/sqrt(|E - E_VH|)  (for M0/M1 type, parabolic dispersion)
#   g(E) ~ delta(E - E_VH)     (for a flat band, exactly)
#
# The broadening sigma = 0.03 (narrow) or 0.10 (broad) regularizes the divergence.
# The peak height is g_peak ~ 1/(sigma * sqrt(2*pi)) for the narrowest features.
#
# For the B2[0] flat band with bandwidth BW:
#   The DOS is concentrated in a window of width ~ BW
#   Peak DOS ~ N_modes_band / BW (if all modes pile up)

# B2[0] is part of band 1 in the B-sector (the one starting at omega=0.014)
# It has bandwidth:
BW_B_bands = bandwidths[:9]  # First 9 = B-sector
print(f"  B-sector bandwidths: {BW_B_bands}")

# The B2 flat band (band index 1 in B-sector) has the narrowest feature
# But the actual bandwidth is not tiny - the "flat" refers to the GROUP VELOCITY
# being small, not the bandwidth being zero.

# The correct way to model the VHS enhancement for A_s:
# The DOS at the (0,0) energies is what it is - already computed in Section 4.
# The question is whether the nearby VHS creates an enhancement RELATIVE to
# the no-VHS baseline (Debye model).

# Debye model: uniform DOS g_D = N_modes / omega_max
omega_max_B = BW_B_bands.sum()  # Total B-sector bandwidth
g_Debye_B = 9.0 / omega_max_B
print(f"\n  Debye model B-sector DOS: g_D_B = {g_Debye_B:.6f}")
print(f"  Actual g_avg_B (narrow): {g_avg_B_narrow:.6f}")
print(f"  Ratio (actual/Debye): {g_avg_B_narrow / g_Debye_B:.4f}")

# Enhancement of (0,0) modes relative to Debye:
R_VH_Debye = np.array([g_B_at_E00_narrow[i] / g_Debye_B for i in range(len(unique_E00))])
R_VH_Debye_weighted = np.sum(weight_v2 * R_VH_Debye)
print(f"\n  R_VH vs Debye (narrow):")
for i, E in enumerate(unique_E00):
    print(f"    E = {E:.4f}: R_VH_Debye = {R_VH_Debye[i]:.4f}")
print(f"  Weighted R_VH_Debye = {R_VH_Debye_weighted:.6f}")

# =============================================================================
# SECTION 9: Enhanced A_s computation
# =============================================================================
print("\n--- Section 9: Enhanced A_s computation ---")

# The A_s gap from S64 is 3.164 OOM (using Gaussian sequential transfer).
# The van Hove enhancement modifies this as:
#   A_s^{enh} = A_s^{bare} * R_VH^2
#   gap^{enh} = gap^{bare} - 2 * log10(R_VH)

# We compute for BOTH smoothings and BOTH reference DOS (total and B-sector)
print(f"  Starting gap (S64 revised): {gap_revised:.4f} OOM")
print()

# Primary result: use broad smoothing (physical — modes have finite lifetime)
# and total DOS (all sectors contribute to the propagator)
R_VH_primary = R_VH_weighted_broad  # 0.307
delta_gap_primary = -2.0 * np.log10(max(R_VH_primary, 1e-10))

# If R_VH < 1, the enhancement is actually a SUPPRESSION (gap increases)
# If R_VH > 1, the gap decreases
gap_enhanced_primary = gap_revised + delta_gap_primary

print(f"  === PRIMARY RESULT (broad smoothing, total DOS, v^2-weighted) ===")
print(f"  R_VH = {R_VH_primary:.6f}")
print(f"  R_VH^2 = {R_VH_primary**2:.6f}")
print(f"  delta_gap = -2*log10(R_VH) = {delta_gap_primary:+.4f} OOM")
print(f"  Enhanced gap = {gap_revised:.4f} + ({delta_gap_primary:+.4f}) = {gap_enhanced_primary:.4f} OOM")

# Secondary: narrow smoothing
R_VH_secondary = R_VH_weighted_narrow
delta_gap_secondary = -2.0 * np.log10(max(R_VH_secondary, 1e-10))
gap_enhanced_secondary = gap_revised + delta_gap_secondary

print(f"\n  === SECONDARY (narrow smoothing, total DOS, v^2-weighted) ===")
print(f"  R_VH = {R_VH_secondary:.6f}")
print(f"  delta_gap = -2*log10(R_VH) = {delta_gap_secondary:+.4f} OOM")
print(f"  Enhanced gap = {gap_revised:.4f} + ({delta_gap_secondary:+.4f}) = {gap_enhanced_secondary:.4f} OOM")

# Tertiary: B-sector only
delta_gap_B = -2.0 * np.log10(max(R_VH_B_weighted_broad, 1e-10))
gap_enhanced_B = gap_revised + delta_gap_B

print(f"\n  === TERTIARY (broad smoothing, B-sector DOS, v^2-weighted) ===")
print(f"  R_VH_B = {R_VH_B_weighted_broad:.6f}")
print(f"  delta_gap = -2*log10(R_VH_B) = {delta_gap_B:+.4f} OOM")
print(f"  Enhanced gap = {gap_revised:.4f} + ({delta_gap_B:+.4f}) = {gap_enhanced_B:.4f} OOM")

# Maximum possible (if modes sat exactly at VHS)
R_VH_max_scenario = R_VH_max_B
delta_gap_max = -2.0 * np.log10(max(R_VH_max_scenario, 1e-10))
gap_max_enhanced = gap_revised + delta_gap_max

print(f"\n  === BEST CASE (modes exactly at B-sector VHS maximum) ===")
print(f"  R_VH_max = {R_VH_max_scenario:.2f}")
print(f"  delta_gap = {delta_gap_max:+.4f} OOM")
print(f"  Enhanced gap = {gap_revised:.4f} + ({delta_gap_max:+.4f}) = {gap_max_enhanced:.4f} OOM")

# =============================================================================
# SECTION 10: DOS-enhanced tunneling through hybridization gaps
# =============================================================================
print("\n--- Section 10: DOS-enhanced tunneling through hybridization gaps ---")

# The Bogoliubov transmission through gap j is:
#   |T_j|^2 = 1 / (1 + (Delta_j / W_eff_j)^2 * pi^2/4)
# where W_eff_j is the effective bandwidth seen by the mode.
#
# If the DOS at the gap energy is enhanced by R_VH, then:
#   W_eff_j = W_bare_j * R_VH(E_j)
# and the transmission improves.
#
# From S64: the bandwidth used was 1.665 M_KK (constant for all gaps).
# The enhanced bandwidth: W_eff_j = 1.665 * R_VH(E_gap_j)

W_bare = float(tf_data['bandwidths'][0])

# The gap energies are approximately at the (0,0) sector energies
# Use the v^2-weighted average enhancement
P_trans_bare = float(tf_data['P_trans_per_gap_Gaussian'].prod())

# Enhanced transmission: replace W -> W * R_VH at each gap
# But we need the DOS at each gap's energy, not just the (0,0) average
# The 16 gaps in the phonon crystal are at various energies.
# For each gap, find the local DOS enhancement.

# The gap energies aren't stored directly, but the (0,0) mode energies
# tell us where the relevant gaps are. Use the broad-smoothed DOS.
gap_energies = omega_00  # 16 values, one per gap
R_VH_per_gap = np.zeros(N_gaps)
for j in range(N_gaps):
    idx = np.argmin(np.abs(omega_grid - gap_energies[j]))
    R_VH_per_gap[j] = g_broad[idx] / g_avg_total_broad

print(f"  Bare bandwidth: W = {W_bare:.6f} M_KK")
print(f"  Per-gap R_VH (broad): {R_VH_per_gap}")

# Enhanced transmission per gap
P_trans_enhanced = np.zeros(N_gaps)
for j in range(N_gaps):
    W_eff = W_bare * max(R_VH_per_gap[j], 0.01)  # Floor to avoid division issues
    P_trans_enhanced[j] = 1.0 / (1.0 + (tight_gaps[j] / W_eff)**2 * PI**2 / 4)

P_total_enhanced = P_trans_enhanced.prod()
P_total_bare = float(tf_data['P_trans_per_gap_Gaussian'].prod())

log_P_bare = np.log10(max(P_total_bare, 1e-300))
log_P_enhanced = np.log10(max(P_total_enhanced, 1e-300))
delta_from_tunneling = log_P_enhanced - log_P_bare

print(f"\n  Product of transmissions (bare): P_bare = {P_total_bare:.6e}")
print(f"  Product of transmissions (enhanced): P_enh = {P_total_enhanced:.6e}")
print(f"  log10(P_bare) = {log_P_bare:.4f}")
print(f"  log10(P_enh) = {log_P_enhanced:.4f}")
print(f"  Delta from enhanced tunneling: {delta_from_tunneling:+.4f} OOM")

# =============================================================================
# SECTION 11: Combined enhancement (DOS + tunneling)
# =============================================================================
print("\n--- Section 11: Combined van Hove enhancement ---")

# Total enhancement has two independent contributions:
# 1. Direct DOS enhancement of perturbation amplitude: R_VH^2
# 2. Enhanced tunneling through gaps: P_enh/P_bare
#
# These are multiplicative:
#   A_s^{total_enh} = A_s^{bare} * R_VH^2 * (P_enh/P_bare)
#
# In OOM:
#   gap^{total} = gap_revised + delta_DOS + delta_tunneling

delta_DOS = delta_gap_primary  # From Section 9
delta_tunnel = delta_from_tunneling

gap_total_enhanced = gap_revised + delta_DOS + delta_tunnel

print(f"  Gap decomposition:")
print(f"    S64 revised gap:           {gap_revised:+.4f} OOM")
print(f"    DOS enhancement (R_VH^2):  {delta_DOS:+.4f} OOM")
print(f"    Tunneling enhancement:     {delta_tunnel:+.4f} OOM")
print(f"    ────────────────────────────────────────")
print(f"    Total enhanced gap:        {gap_total_enhanced:+.4f} OOM")
print(f"    Change from S64:           {gap_total_enhanced - gap_revised:+.4f} OOM")

# =============================================================================
# SECTION 12: Physical interpretation — the anti-enhancement
# =============================================================================
print("\n--- Section 12: Physical interpretation ---")

if R_VH_primary < 1.0:
    print(f"  CRITICAL RESULT: R_VH = {R_VH_primary:.4f} < 1")
    print(f"  The (0,0) sector modes sit in a DOS TROUGH, not at a VHS peak.")
    print(f"  The van Hove singularity SUPPRESSES A_s, not enhances it.")
    print(f"  This WIDENS the A_s gap by {abs(delta_DOS):.4f} OOM.")
    print()
    print(f"  Physical reason: The (0,0) modes at E ~ 0.82-0.97 M_KK fall")
    print(f"  BETWEEN B-sector van Hove singularities. The nearest B-VHS is at")
    print(f"  omega = 0.896 (band 6, M0 type), separated by 0.05-0.08 M_KK.")
    print(f"  The DOS at these energies is below the B-sector average because")
    print(f"  the modes are in the 'gap' between VHS peaks — precisely where")
    print(f"  the DOS has a local minimum.")
    print()
    print(f"  CONDENSED MATTER ANALOG: This is the anti-enhancement seen in")
    print(f"  conventional BCS superconductors when E_F falls in a pseudo-gap")
    print(f"  rather than at the van Hove peak. The critical temperature T_c")
    print(f"  is suppressed by the pseudo-gap just as A_s is suppressed here.")
elif R_VH_primary > 1.0:
    print(f"  R_VH = {R_VH_primary:.4f} > 1: van Hove ENHANCEMENT active")
    print(f"  The (0,0) modes coincide with elevated DOS.")
    print(f"  Gap reduced by {abs(delta_DOS):.4f} OOM.")
else:
    print(f"  R_VH = {R_VH_primary:.4f} ~ 1: no significant van Hove effect")

# =============================================================================
# SECTION 13: Sensitivity to smoothing and reference DOS
# =============================================================================
print("\n--- Section 13: Sensitivity analysis ---")

# Collect all enhancement scenarios
scenarios = {
    'Total DOS, narrow': (R_VH_weighted_narrow, gap_revised - 2*np.log10(max(R_VH_weighted_narrow, 1e-10))),
    'Total DOS, broad': (R_VH_weighted_broad, gap_revised - 2*np.log10(max(R_VH_weighted_broad, 1e-10))),
    'B-sector, narrow': (R_VH_B_weighted_narrow, gap_revised - 2*np.log10(max(R_VH_B_weighted_narrow, 1e-10))),
    'B-sector, broad': (R_VH_B_weighted_broad, gap_revised - 2*np.log10(max(R_VH_B_weighted_broad, 1e-10))),
    'Max possible (B-VHS)': (R_VH_max_B, gap_revised - 2*np.log10(max(R_VH_max_B, 1e-10))),
}

print(f"  {'Scenario':<25} {'R_VH':<10} {'R_VH^2':<12} {'Gap (OOM)':<12} {'Delta':<10}")
print(f"  {'─'*25} {'─'*10} {'─'*12} {'─'*12} {'─'*10}")
for name, (R, gap) in scenarios.items():
    delta = gap - gap_revised
    print(f"  {name:<25} {R:<10.4f} {R**2:<12.6f} {gap:<12.4f} {delta:+10.4f}")

# =============================================================================
# SECTION 14: How large would R_VH need to be?
# =============================================================================
print("\n--- Section 14: Required enhancement to close the gap ---")

# To close the 3.16 OOM gap entirely through DOS enhancement:
# gap_revised - 2*log10(R_required) = 0
# R_required = 10^(gap_revised/2)
R_required = 10**(gap_revised / 2)
print(f"  Current gap: {gap_revised:.4f} OOM")
print(f"  Required R_VH to close gap: {R_required:.2f}")
print(f"  Required R_VH^2: {R_required**2:.2e}")
print(f"  Actual R_VH (primary): {R_VH_primary:.4f}")
print(f"  Shortfall: {R_required / R_VH_primary:.1f}x")

# Even the maximum B-sector VHS is far short:
print(f"  Maximum B-sector VHS R_VH: {R_VH_max_B:.2f}")
print(f"  Would close: {-2*np.log10(R_VH_max_B):.4f} OOM of {gap_revised:.4f} OOM gap")

# =============================================================================
# SECTION 15: Gate verdict
# =============================================================================
print("\n--- Section 15: Gate verdict ---")

gate_name = "VANHOVE-AS-65"
gate_verdict = "INFO"

# Collect the decisive numbers
enhancement_primary = R_VH_primary
gap_change = delta_DOS + delta_tunnel
gap_final = gap_total_enhanced

if enhancement_primary < 1.0:
    direction = "ANTI-ENHANCEMENT (gap widened)"
else:
    direction = "ENHANCEMENT (gap narrowed)"

gate_detail = (
    f"Van Hove enhancement R_VH = {enhancement_primary:.4f} (v^2-weighted, broad DOS). "
    f"Direction: {direction}. "
    f"DOS effect: {delta_DOS:+.4f} OOM. "
    f"Tunneling effect: {delta_tunnel:+.4f} OOM. "
    f"Combined: {gap_change:+.4f} OOM. "
    f"A_s gap: {gap_revised:.4f} -> {gap_final:.4f} OOM. "
    f"Required R_VH to close gap: {R_required:.1f} (actual {enhancement_primary:.3f}, "
    f"max possible {R_VH_max_B:.1f}). "
    f"Van Hove enhancement is structurally negligible for the A_s transfer function."
)

print(f"\n  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# SECTION 16: Save data
# =============================================================================
print("\n--- Section 16: Save data ---")

np.savez(
    OUT_NPZ,
    # Input references
    omega_grid=omega_grid,
    unique_E00=unique_E00,
    multiplicities=multiplicities,
    omega_00=omega_00,
    v2_00=v2_00,

    # DOS at (0,0) energies
    g_at_E00_narrow=g_at_E00_narrow,
    g_at_E00_broad=g_at_E00_broad,
    g_B_at_E00_narrow=g_B_at_E00_narrow,
    g_B_at_E00_broad=g_B_at_E00_broad,

    # Average DOS
    g_avg_total_narrow=g_avg_total_narrow,
    g_avg_total_broad=g_avg_total_broad,
    g_avg_B_narrow=g_avg_B_narrow,
    g_avg_B_broad=g_avg_B_broad,

    # Enhancement factors
    R_VH_narrow=R_VH_narrow,
    R_VH_broad=R_VH_broad,
    R_VH_weighted_narrow=R_VH_weighted_narrow,
    R_VH_weighted_broad=R_VH_weighted_broad,
    R_VH_B_weighted_narrow=R_VH_B_weighted_narrow,
    R_VH_B_weighted_broad=R_VH_B_weighted_broad,
    R_VH_max_B=R_VH_max_B,
    R_VH_per_gap=R_VH_per_gap,

    # Gap results
    gap_revised_input=gap_revised,
    delta_gap_DOS=delta_DOS,
    delta_gap_tunneling=delta_tunnel,
    gap_total_enhanced=gap_total_enhanced,
    R_required=R_required,

    # Tunneling
    P_total_bare=P_total_bare,
    P_total_enhanced=P_total_enhanced,

    # Gate
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 17: Plot
# =============================================================================
print("\n--- Section 17: Plotting ---")

fig = plt.figure(figsize=(18, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: DOS with (0,0) sector energies marked
ax1 = fig.add_subplot(gs[0, 0])
mask_plot = omega_grid < 3.0
ax1.plot(omega_grid[mask_plot], g_narrow[mask_plot], 'b-', alpha=0.5, linewidth=0.8, label='Total')
ax1.plot(omega_grid[mask_plot], g_B_narrow[mask_plot], 'r-', linewidth=1.2, label='B-sector')
ax1.axhline(g_avg_total_narrow, color='b', linestyle='--', alpha=0.5, label=f'g_avg={g_avg_total_narrow:.3f}')
ax1.axhline(g_avg_B_narrow, color='r', linestyle='--', alpha=0.5, label=f'g_avg_B={g_avg_B_narrow:.3f}')
for E in unique_E00:
    ax1.axvline(E, color='green', linestyle=':', alpha=0.7, linewidth=1.5)
ax1.axvline(unique_E00[0], color='green', linestyle=':', alpha=0.7, linewidth=1.5, label='(0,0) energies')
ax1.set_xlabel('Energy (M_KK)')
ax1.set_ylabel('DOS')
ax1.set_title('Phonon DOS near (0,0) sector')
ax1.legend(fontsize=7, loc='upper right')
ax1.set_xlim(0, 3.0)

# Panel 2: B-sector VHS locations
ax2 = fig.add_subplot(gs[0, 1])
b_mask_low = (vhs_sector == 'B') & (vhs_omega < 3.0)
b_vhs_low = vhs_omega[b_mask_low]
b_types_low = vhs_type[b_mask_low]
colors_vhs = ['blue' if t == 'M0' else ('red' if t == 'M1' else ('cyan' if 'M0' in t else 'orange'))
              for t in b_types_low]
ax2.scatter(b_vhs_low, np.arange(len(b_vhs_low)), c=colors_vhs, s=50, zorder=5)
for E in unique_E00:
    ax2.axvline(E, color='green', linestyle=':', alpha=0.7, linewidth=2)
ax2.set_xlabel('Energy (M_KK)')
ax2.set_ylabel('VHS index')
ax2.set_title('B-sector Van Hove singularities')
# Custom legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='M0 (band min)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='M1 (band max)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='cyan', markersize=8, label='M0_int (interior)'),
    Line2D([0], [0], color='green', linestyle=':', linewidth=2, label='(0,0) energies'),
]
ax2.legend(handles=legend_elements, fontsize=7)

# Panel 3: Enhancement factor per (0,0) energy
ax3 = fig.add_subplot(gs[0, 2])
x_pos = np.arange(len(unique_E00))
width = 0.2  # (local)
bars1 = ax3.bar(x_pos - 1.5*width, R_VH_narrow, width, label='Total, narrow', color='steelblue')
bars2 = ax3.bar(x_pos - 0.5*width, R_VH_broad, width, label='Total, broad', color='cornflowerblue')
bars3 = ax3.bar(x_pos + 0.5*width, R_VH_B_narrow, width, label='B-sector, narrow', color='salmon')
bars4 = ax3.bar(x_pos + 1.5*width, R_VH_B_broad, width, label='B-sector, broad', color='indianred')
ax3.axhline(1.0, color='black', linestyle='--', linewidth=1, label='R_VH = 1 (no enhancement)')
ax3.set_xticks(x_pos)
ax3.set_xticklabels([f'{E:.3f}' for E in unique_E00], fontsize=8)
ax3.set_xlabel('(0,0) sector energy (M_KK)')
ax3.set_ylabel('R_VH = g(E)/g_avg')
ax3.set_title('Van Hove Enhancement Factor')
ax3.legend(fontsize=6, loc='upper right')

# Panel 4: A_s gap waterfall
ax4 = fig.add_subplot(gs[1, 0])
labels_wf = ['S64 gap\n(revised)', 'DOS\nenhance.', 'Tunneling\nenhance.', 'Final\ngap']
values_wf = [gap_revised, delta_DOS, delta_tunnel, gap_total_enhanced]
colors_wf = ['steelblue', 'red' if delta_DOS > 0 else 'green',
             'red' if delta_tunnel > 0 else 'green', 'darkblue']
ax4.barh(range(len(labels_wf)), values_wf, color=colors_wf, height=0.6)
for i, v in enumerate(values_wf):
    ha = 'left' if v >= 0 else 'right'
    ax4.text(v + 0.05 * np.sign(v), i, f'{v:+.4f}' if i in [1, 2] else f'{v:.4f}',
             ha=ha, va='center', fontsize=9, fontweight='bold')
ax4.set_yticks(range(len(labels_wf)))
ax4.set_yticklabels(labels_wf, fontsize=9)
ax4.set_xlabel('A_s gap (OOM)')
ax4.set_title(f'A_s Gap: {gap_revised:.2f} -> {gap_total_enhanced:.2f} OOM')
ax4.axvline(0, color='gray', linestyle='-', alpha=0.3)

# Panel 5: Sensitivity analysis
ax5 = fig.add_subplot(gs[1, 1])
scenario_names = list(scenarios.keys())
scenario_gaps = [scenarios[n][1] for n in scenario_names]
colors_sc = ['steelblue', 'cornflowerblue', 'salmon', 'indianred', 'gold']
ax5.barh(range(len(scenario_names)), scenario_gaps, color=colors_sc, height=0.6)
ax5.axvline(gap_revised, color='black', linestyle='--', linewidth=1, label=f'S64 gap = {gap_revised:.2f}')
for i, v in enumerate(scenario_gaps):
    ax5.text(v + 0.03, i, f'{v:.3f}', ha='left', va='center', fontsize=8)
ax5.set_yticks(range(len(scenario_names)))
ax5.set_yticklabels(scenario_names, fontsize=8)
ax5.set_xlabel('Enhanced A_s gap (OOM)')
ax5.set_title('Sensitivity to DOS Reference')
ax5.legend(fontsize=8)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary_text = (
    f"VANHOVE-AS-65: INFO\n"
    f"{'='*40}\n\n"
    f"Van Hove Enhancement of A_s\n\n"
    f"(0,0) sector energies:\n"
    f"  E = {unique_E00[0]:.4f}, {unique_E00[1]:.4f}, {unique_E00[2]:.4f} M_KK\n\n"
    f"Enhancement (v^2-weighted, broad):\n"
    f"  R_VH = {R_VH_primary:.4f}\n"
    f"  R_VH^2 = {R_VH_primary**2:.6f}\n\n"
    f"A_s gap changes:\n"
    f"  DOS effect:     {delta_DOS:+.4f} OOM\n"
    f"  Tunneling eff.: {delta_tunnel:+.4f} OOM\n"
    f"  Combined:       {delta_DOS + delta_tunnel:+.4f} OOM\n\n"
    f"Gap: {gap_revised:.2f} -> {gap_total_enhanced:.2f} OOM\n\n"
    f"Required R_VH = {R_required:.0f}\n"
    f"Max possible   = {R_VH_max_B:.1f}\n\n"
    f"VERDICT: Van Hove enhancement\n"
    f"structurally negligible.\n"
    f"(0,0) modes sit in DOS trough."
)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         verticalalignment='top', fontfamily='monospace', fontsize=9.5)

fig.suptitle('VANHOVE-AS-65: Van Hove Enhancement of A_s Transfer Function',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {OUT_PNG}")

# =============================================================================
# SECTION 18: Final summary
# =============================================================================
elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"VANHOVE-AS-65 COMPLETE ({elapsed:.1f}s)")
print(f"  Enhancement: R_VH = {R_VH_primary:.4f} (ANTI-enhancement: modes in DOS trough)")
print(f"  A_s gap: {gap_revised:.4f} -> {gap_total_enhanced:.4f} OOM")
print(f"  Change: {gap_total_enhanced - gap_revised:+.4f} OOM (gap WIDENED)")
print(f"  Required to close: R_VH = {R_required:.0f} (shortfall: {R_required/R_VH_primary:.0f}x)")
print(f"  VERDICT: {gate_verdict}")
print(f"{'='*78}")
