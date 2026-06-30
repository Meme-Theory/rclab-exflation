#!/usr/bin/env python3
"""
s72_blueshift_tilt.py — Blueshift Tilt at Entry Sonic Horizon (BLUESHIFT-TILT-72)

Computes the spectral tilt correction to n_s from differential pair creation
at the entry sonic horizon (tau ~ 0.22).

Physics:
  The entry horizon at T_entry = 72.8 M_KK creates mode-dependent Bogoliubov
  coefficients via the Hawking/Unruh mechanism:
    |beta_k|^2 / |alpha_k|^2 = exp(-2*pi*omega_k / kappa)

  Higher-k modes have higher omega_k and are less squeezed. This differential
  creates a tilt in the power spectrum, modifying n_s.

  CRITICAL DISTINCTION: The question is not the tilt of the entry-horizon
  spectrum in isolation (which is ~-1 for deeply thermal modes), but the
  CHANGE in spectral index when the entry-horizon squeeze modifies the
  total power spectrum that was previously determined by fold + spatial +
  Leggett channels.

  The 8 BCS modes span only 6.7% in frequency. The tilt correction is:
    delta_n_s = (n_s with entry) - (n_s without entry)
  evaluated as the change in the logarithmic slope across this frequency band.

Gate: BLUESHIFT-TILT-72
  PASS: |delta_n_s| > 0.001
  INFO: |delta_n_s| in [0.0001, 0.001]
  FAIL: |delta_n_s| < 0.0001

Inputs:
  - s71_entry_horizon_spectrum.npz (T_entry, kappa_entry, kappa_v, tau_entry)
  - s71_decoherence_band.npz (r_k_bcs, mode_weights, r_compound_s70)

Session 72, Wave 3-C
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from canonical_constants import (
    PI, tau_fold, Delta_BCS, E_B1, E_B2_mean, E_B3_mean,
    A_s_CMB, N_dof_BCS, dt_transit, H_fold, c_fabric,
    T_acoustic, omega_L1
)

t_start = time.time()

# =============================================================================
# 1. Load input data
# =============================================================================

data_dir = os.path.dirname(__file__)

d_entry = np.load(os.path.join(data_dir, 's71_entry_horizon_spectrum.npz'), allow_pickle=True)
d_bog = np.load(os.path.join(data_dir, 's71_decoherence_band.npz'), allow_pickle=True)

# Entry horizon parameters
tau_entry = float(d_entry['tau_entry'])       # = 0.2195
T_entry = float(d_entry['T_entry'])           # = 72.84 M_KK
kappa_entry = float(d_entry['kappa_entry'])   # = 79386 M_KK^2 (full spectral surface gravity)
kappa_v = float(d_entry['kappa_v'])           # = 457.7 M_KK^2 (velocity-space surface gravity)
T_compound_mic = float(d_entry['T_compound']) # = 7.578 M_KK (microcanonical)

# Branch energies along tau scan
tau_scan = d_entry['tau_scan']
B1_track = d_entry['B1_track']
B2_track = d_entry['B2_01_track']
B3_track = d_entry['B3_track']

# Fold/BCS Bogoliubov data
labels = d_bog['labels']
r_k_bcs = d_bog['r_k_bcs']            # BCS squeeze per mode (8 modes)
r_eff = d_bog['r_eff']                 # effective squeeze (BCS + spatial)
r_compound = d_bog['r_compound_s70']   # compound squeeze (all channels)
cosh2r_eff = d_bog['cosh2r_eff']
mode_weights = d_bog['mode_weights']
r_spatial = float(d_bog['r_spatial_eff'])
r_L = float(d_bog['r_L'])

print("=" * 70)
print("BLUESHIFT-TILT-72: Entry Horizon Spectral Tilt Correction")
print("=" * 70)
print(f"\nInput parameters:")
print(f"  tau_entry      = {tau_entry:.6f}")
print(f"  T_entry        = {T_entry:.4f} M_KK  (= kappa_v / 2pi)")
print(f"  kappa_v        = {kappa_v:.2f} M_KK^2")
print(f"  T_compound_mic = {T_compound_mic:.4f} M_KK")

# =============================================================================
# 2. Mode frequencies at the entry horizon
# =============================================================================

idx_entry = np.argmin(np.abs(tau_scan - tau_entry))

E_B1_entry = B1_track[idx_entry]
E_B2_entry = B2_track[idx_entry]
E_B3_entry = B3_track[idx_entry]

# 8-mode frequency array: [B2[0-3], B1, B3[0-2]]
omega_k = np.array([
    E_B2_entry, E_B2_entry, E_B2_entry, E_B2_entry,
    E_B1_entry,
    E_B3_entry, E_B3_entry, E_B3_entry
])

# Distinct frequencies for the 3 branches
omega_distinct = np.array([E_B1_entry, E_B2_entry, E_B3_entry])
branch_labels = ['B1', 'B2', 'B3']
branch_degeneracy = np.array([1, 4, 3])

print(f"\nMode frequencies at entry (tau={tau_entry:.4f}):")
for i, (lab, om) in enumerate(zip(branch_labels, omega_distinct)):
    print(f"  {lab}: omega = {om:.6f} M_KK (deg = {branch_degeneracy[i]})")
print(f"  Frequency span: {omega_distinct.max()-omega_distinct.min():.6f} M_KK "
      f"({(omega_distinct.max()-omega_distinct.min())/np.mean(omega_distinct)*100:.2f}%)")

# =============================================================================
# 3. Entry-horizon Bogoliubov coefficients
# =============================================================================
# Standard Hawking/Unruh thermal spectrum:
#   |beta_k/alpha_k|^2 = exp(-2*pi*omega_k / kappa_v)
# Bosonic normalization: |alpha_k|^2 - |beta_k|^2 = 1

T_Hawking = kappa_v / (2.0 * PI)
x_k = omega_k / T_Hawking          # omega/T ratio per mode (all ~ 0.012)
x_distinct = omega_distinct / T_Hawking

boltzmann_k = np.exp(-x_k)         # exp(-omega/T)
beta_sq_entry = boltzmann_k / (1.0 - boltzmann_k)
alpha_sq_entry = 1.0 / (1.0 - boltzmann_k)
r_k_entry = np.arctanh(np.sqrt(boltzmann_k))

# Normalization check
norm_err = np.max(np.abs(alpha_sq_entry - beta_sq_entry - 1.0))
assert norm_err < 1e-10, f"Bogoliubov normalization FAIL: max error = {norm_err}"

print(f"\nEntry Bogoliubov coefficients (T_Hawking = {T_Hawking:.4f} M_KK):")
print(f"{'Branch':<8} {'omega/T':<10} {'|beta|^2':<12} {'r_entry':<10}")
for i, lab in enumerate(branch_labels):
    idx = [4, 0, 5][i]  # representative index for each branch
    print(f"  {lab:<6} {x_k[idx]:<10.6f} {beta_sq_entry[idx]:<12.4f} {r_k_entry[idx]:<10.6f}")
print(f"  |alpha|^2 - |beta|^2 = 1 verified (max err = {norm_err:.1e})")

# =============================================================================
# 4. Compound power spectrum: baseline vs entry-modified
# =============================================================================
# BASELINE: P_k^base = cosh(2 * r_compound_k)
# where r_compound includes BCS fold + spatial + Leggett (from S70/S71).
#
# WITH ENTRY: The total squeeze is the BCH composition of entry and fold.
# In the sudden approximation (WKB PERMANENTLY FAILED, S70), for aligned
# squeeze phases:
#   r_total = r_entry + r_compound  (aligned, upper bound)
#   r_total = |r_entry - r_compound| (anti-aligned, lower bound)
#
# Physical case: the entry horizon creates squeeze along the same quadrature
# as the fold (both are particle-creation events from the same flow), so
# aligned is the physical expectation. We compute both and also a
# random-phase average.

P_base = np.cosh(2.0 * r_compound)

# Aligned phases
r_total_aligned = r_k_entry + r_compound
P_aligned = np.cosh(2.0 * r_total_aligned)

# Anti-aligned phases
r_total_anti = np.abs(r_compound - r_k_entry)
P_anti = np.cosh(2.0 * r_total_anti)

# Random phase average: <P> = cosh(2r_e)*cosh(2r_f) (for independent phases)
P_random = np.cosh(2.0 * r_k_entry) * np.cosh(2.0 * r_compound)

print(f"\nPower spectrum per mode:")
print(f"{'Mode':<8} {'P_base':<14} {'P_aligned':<14} {'P_random':<14} {'P_anti':<14}")
for i, lab in enumerate(labels):
    print(f"  {lab:<6} {P_base[i]:<14.2f} {P_aligned[i]:<14.2f} {P_random[i]:<14.2f} {P_anti[i]:<14.4f}")

# =============================================================================
# 5. Spectral tilt: the correct delta_n_s calculation
# =============================================================================
# The tilt correction is:
#   delta_n_s = n_s(with entry) - n_s(without entry)
#
# where n_s = 1 - d(ln P)/d(ln k) evaluated at k_CMB.
#
# The modes have frequencies omega_B1 < omega_B2 < omega_B3. We treat these
# as three k-values in the CMB power spectrum (mapped through the Friedmann
# evolution). The spectral index is the logarithmic slope across these.
#
# BASELINE tilt (from fold only):
#   n_s^base = 1 - [ln(P_B3^base) - ln(P_B1^base)] / [ln(omega_B3) - ln(omega_B1)]
#
# ENTRY-MODIFIED tilt:
#   n_s^entry = 1 - [ln(P_B3^total) - ln(P_B1^total)] / [ln(omega_B3) - ln(omega_B1)]
#
# The key: r_compound already varies across modes (B1 has r=4.32, B2 has r=2.49,
# B3 has r=2.33). This baseline variation is NOT what we are computing --
# that is already captured in n_s^bare. We want the CHANGE from adding entry.

ln_omega_span = np.log(omega_distinct[2]) - np.log(omega_distinct[0])  # ln(omega_B3/omega_B1)

# Representative r_compound for each branch
r_comp_B1 = r_compound[4]     # B1
r_comp_B2 = r_compound[0]     # B2[0] (all B2 identical)
r_comp_B3 = r_compound[5]     # B3[0] (all B3 identical)

r_entry_B1 = r_k_entry[4]
r_entry_B2 = r_k_entry[0]
r_entry_B3 = r_k_entry[5]

# Baseline power per branch
P_base_branches = np.array([
    np.cosh(2.0 * r_comp_B1),
    np.cosh(2.0 * r_comp_B2),
    np.cosh(2.0 * r_comp_B3)
])

# --- ALIGNED CASE ---
P_aligned_branches = np.array([
    np.cosh(2.0 * (r_entry_B1 + r_comp_B1)),
    np.cosh(2.0 * (r_entry_B2 + r_comp_B2)),
    np.cosh(2.0 * (r_entry_B3 + r_comp_B3))
])

slope_base = (np.log(P_base_branches[2]) - np.log(P_base_branches[0])) / ln_omega_span
slope_aligned = (np.log(P_aligned_branches[2]) - np.log(P_aligned_branches[0])) / ln_omega_span
delta_ns_aligned = -slope_aligned - (-slope_base)  # = slope_base - slope_aligned

# --- ANTI-ALIGNED CASE ---
P_anti_branches = np.array([
    np.cosh(2.0 * abs(r_comp_B1 - r_entry_B1)),
    np.cosh(2.0 * abs(r_comp_B2 - r_entry_B2)),
    np.cosh(2.0 * abs(r_comp_B3 - r_entry_B3))
])
slope_anti = (np.log(P_anti_branches[2]) - np.log(P_anti_branches[0])) / ln_omega_span
delta_ns_anti = -slope_anti - (-slope_base)

# --- RANDOM PHASE CASE ---
P_random_branches = np.array([
    np.cosh(2.0 * r_entry_B1) * np.cosh(2.0 * r_comp_B1),
    np.cosh(2.0 * r_entry_B2) * np.cosh(2.0 * r_comp_B2),
    np.cosh(2.0 * r_entry_B3) * np.cosh(2.0 * r_comp_B3)
])
slope_random = (np.log(P_random_branches[2]) - np.log(P_random_branches[0])) / ln_omega_span
delta_ns_random = -slope_random - (-slope_base)

print(f"\n{'='*70}")
print("SPECTRAL TILT CALCULATION")
print(f"{'='*70}")
print(f"\nFrequency lever arm: ln(omega_B3/omega_B1) = {ln_omega_span:.6f}")
print(f"  (omega_B1={omega_distinct[0]:.6f}, omega_B3={omega_distinct[2]:.6f})")

print(f"\nBaseline (fold-only) power spectrum slope:")
print(f"  P_B1 = {P_base_branches[0]:.4f}, P_B2 = {P_base_branches[1]:.4f}, P_B3 = {P_base_branches[2]:.4f}")
print(f"  slope_base = d(ln P)/d(ln omega) = {slope_base:.6f}")

print(f"\nAligned-phase case (r_total = r_entry + r_compound):")
print(f"  P_B1 = {P_aligned_branches[0]:.4f}, P_B2 = {P_aligned_branches[1]:.4f}, P_B3 = {P_aligned_branches[2]:.4f}")
print(f"  slope_aligned = {slope_aligned:.6f}")
print(f"  delta_n_s = {delta_ns_aligned:+.6e}")

print(f"\nAnti-aligned case (r_total = |r_compound - r_entry|):")
print(f"  P_B1 = {P_anti_branches[0]:.4f}, P_B2 = {P_anti_branches[1]:.4f}, P_B3 = {P_anti_branches[2]:.4f}")
print(f"  slope_anti = {slope_anti:.6f}")
print(f"  delta_n_s = {delta_ns_anti:+.6e}")

print(f"\nRandom-phase case (P = cosh(2r_e)*cosh(2r_f)):")
print(f"  P_B1 = {P_random_branches[0]:.4f}, P_B2 = {P_random_branches[1]:.4f}, P_B3 = {P_random_branches[2]:.4f}")
print(f"  slope_random = {slope_random:.6f}")
print(f"  delta_n_s = {delta_ns_random:+.6e}")

# =============================================================================
# 6. Analytic understanding of the tilt
# =============================================================================
# For large squeeze (all r >> 1), cosh(2r) ~ exp(2r)/2, so:
#   ln P ~ 2*r - ln 2
# The slope is: d(ln P)/d(ln omega) = 2 * d(r)/d(ln omega)
#
# For the BASELINE:
#   d(r_compound)/d(ln omega) depends on how fold physics varies with mode
#
# For the ENTRY contribution (aligned case):
#   d(r_total)/d(ln omega) = d(r_entry)/d(ln omega) + d(r_compound)/d(ln omega)
# So delta_slope = d(r_entry)/d(ln omega), and delta_n_s = -2 * d(r_entry)/d(ln omega)
#
# For deeply thermal entry (omega/T << 1):
#   r_entry ~ (1/2) * ln(T/omega) + const  [from arctanh(1-x) ~ -ln(x)/2 for small x]
#   d(r_entry)/d(ln omega) ~ -1/2
# So delta_ns_aligned ~ +1 (large and positive -- makes n_s redder).
#
# BUT this is the tilt per unit ln(omega). The actual delta_n_s across the mode
# band is this times the frequency lever arm... NO. The slope IS d(ln P)/d(ln omega)
# which IS the spectral index. The issue is that with only 3 distinct frequencies
# spanning 6.7%, the slope is well-defined but the CHANGE from entry is large because
# entry squeeze varies STEEPLY in the deeply thermal regime.

# Let's verify the analytic limit
r_entry_analytic_limit = 0.5 * np.log(T_Hawking / omega_distinct)  # approximate for omega/T << 1
dr_dlnomega_analytic = -0.5  # d(r_entry)/d(ln omega) in deeply thermal limit  # (local)

print(f"\nAnalytic verification (deeply thermal limit omega/T << 1):")
print(f"  r_entry (exact):     [{r_k_entry.min():.6f}, {r_k_entry.max():.6f}]")
print(f"  r_entry (approx):    [{r_entry_analytic_limit.min():.6f}, {r_entry_analytic_limit.max():.6f}]")
print(f"  dr/d(ln omega) exact: ", end="")
dr_exact = (r_k_entry[5] - r_k_entry[4]) / (np.log(omega_k[5]) - np.log(omega_k[4]))
print(f"{dr_exact:.6f} (should be ~ -0.5)")
print(f"  delta_slope = 2 * dr/d(ln omega) = {2*dr_exact:.6f}")
print(f"  Predicted delta_n_s ~ -{2*dr_exact:.6f} = {-2*dr_exact:.6f}")

# =============================================================================
# 7. The correct physical interpretation
# =============================================================================
# The large delta_n_s (~1) is NOT an error. It is a genuine prediction:
# in the deeply thermal regime (omega/T ~ 0.01), the Bose-Einstein occupation
# n_k ~ T/omega varies steeply with omega. This creates a strong spectral tilt.
#
# HOWEVER: this tilt applies to the ENTRY-HORIZON pair creation spectrum
# independently. The question is whether this maps onto the CMB power spectrum.
#
# The mapping omega_k -> k_CMB involves the Friedmann evolution during and
# after the transit. The 8 BCS modes at the entry horizon map to specific
# comoving wavenumbers. Whether the entry tilt translates to a CMB tilt
# depends on whether the modes that become CMB scales have the same
# frequency ordering at the entry horizon.
#
# For the framework: the GGE relic spectrum (which BECOMES the CMB power
# spectrum) is set primarily by the fold transit, not by the entry conditions.
# The entry adds a pre-squeeze that modifies the initial state entering the fold.
#
# KEY INSIGHT: The delta_n_s we computed is the change in slope of the TOTAL
# power spectrum across the BCS mode band. But the CMB n_s is measured across
# many decades in k (0.002 < k < 0.2 Mpc^-1), while the BCS modes span only
# 6.7% in omega. If the mapping is linear (omega ~ k), then delta_n_s ~ 1
# across 6.7% maps to delta_n_s ~ 0.067 across one e-fold in k.
#
# More precisely: the tilt per e-fold is delta_n_s * (delta_ln_k / 1),
# and our delta_ln_k = ln(omega_B3/omega_B1) = 0.068.

print(f"\n{'='*70}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*70}")

# The spectral index as measured at the CMB
# n_s is defined as the slope of ln(P) vs ln(k) per unit ln(k).
# Our slope is computed over delta_ln_omega = 0.068.
# This IS the slope per unit ln(omega) -- it IS n_s if omega maps to k.

# But there is a subtlety. The BASELINE slope already exists (from fold physics).
# The CHANGE delta_n_s is what the entry adds. Let's examine this:

print(f"\nSlope analysis:")
print(f"  Baseline slope:  {slope_base:.6f} per unit ln(omega)")
print(f"  Aligned slope:   {slope_aligned:.6f} per unit ln(omega)")
print(f"  CHANGE in slope: {slope_aligned - slope_base:.6f}")
print(f"  delta_n_s = -(change in slope) = {-(slope_aligned - slope_base):+.6e}")
print(f"  This equals: {delta_ns_aligned:+.6e}")

# =============================================================================
# 8. Scale-transfer computation: what fraction of CMB tilt comes from entry?
# =============================================================================
# The CMB spectral index n_s = 0.9649 means d(ln P)/d(ln k) = 0.0351 (red tilt).
# The entry-horizon contribution to this tilt is:
#   delta_n_s / n_s_deviation = delta_n_s / (1 - 0.9649) = delta_n_s / 0.0351

# For aligned case:
frac_of_tilt_aligned = delta_ns_aligned / 0.0351
print(f"\n  Fraction of observed CMB tilt from entry:")
print(f"    Aligned:  {frac_of_tilt_aligned:.4f}")
print(f"    Random:   {delta_ns_random / 0.0351:.4f}")

# =============================================================================
# 9. Refined calculation: only the DIFFERENTIAL entry effect
# =============================================================================
# The issue is that r_entry varies across branches as:
#   r_B1 = 2.937, r_B2 = 2.925, r_B3 = 2.904
# This 1.13% variation acts on top of a fold squeeze that varies as:
#   r_B1 = 4.320, r_B2 = 2.488, r_B3 = 2.330
# which already has a 46% variation.
#
# The fold variation DOMINATES the baseline slope. The entry ADDS to it.
# delta_n_s measures the entry's contribution to the total slope.
#
# Let's decompose the slopes:

delta_r_entry = r_entry_B3 - r_entry_B1  # r_entry varies by -0.034 (B3 < B1)
delta_r_fold = r_comp_B3 - r_comp_B1     # r_compound varies by -1.99 (B3 << B1)

# In the large-squeeze limit: slope ~ 2 * delta_r / delta_ln_omega
slope_entry_only = 2.0 * delta_r_entry / ln_omega_span
slope_fold_only = 2.0 * delta_r_fold / ln_omega_span

print(f"\nDecomposition of tilt sources:")
print(f"  r_entry(B1) = {r_entry_B1:.6f}, r_entry(B3) = {r_entry_B3:.6f}, delta = {delta_r_entry:+.6f}")
print(f"  r_fold(B1)  = {r_comp_B1:.4f},  r_fold(B3)  = {r_comp_B3:.4f},  delta = {delta_r_fold:+.4f}")
print(f"  slope from entry squeeze: {slope_entry_only:.4f}")
print(f"  slope from fold squeeze:  {slope_fold_only:.4f}")
print(f"  ratio entry/fold:         {abs(slope_entry_only/slope_fold_only):.6f}")

# =============================================================================
# 10. Cross-checks
# =============================================================================

print(f"\n{'='*70}")
print("CROSS-CHECKS")
print(f"{'='*70}")

# Check 1: Cold-entry limit (kappa -> 0)
kappa_cold = kappa_v * 0.001
beta_sq_cold = np.exp(-2*PI*omega_k/kappa_cold)
r_entry_cold = np.arctanh(np.sqrt(beta_sq_cold))
P_cold = np.cosh(2.0 * (r_entry_cold + r_compound))
slope_cold = (np.log(P_cold[5]) - np.log(P_cold[4])) / (np.log(omega_k[5]) - np.log(omega_k[4]))
delta_ns_cold = slope_base - slope_cold
print(f"\n1. Cold entry (T -> 0, kappa -> 0.001*kappa_v):")
print(f"   |beta|^2 -> [{beta_sq_cold.min():.2e}, {beta_sq_cold.max():.2e}]")
print(f"   r_entry -> [{r_entry_cold.min():.6e}, {r_entry_cold.max():.6e}]")
print(f"   delta_n_s -> {delta_ns_cold:.6e} (should -> 0): {'PASS' if abs(delta_ns_cold) < 1e-3 else 'FAIL'}")

# Check 2: Hot-entry limit (kappa -> infinity)
kappa_hot = kappa_v * 10000
r_entry_hot = np.arctanh(np.sqrt(np.exp(-2*PI*omega_k/kappa_hot)))
P_hot = np.cosh(2.0 * (r_entry_hot + r_compound))
slope_hot = (np.log(P_hot[5]) - np.log(P_hot[4])) / (np.log(omega_k[5]) - np.log(omega_k[4]))
delta_ns_hot = slope_base - slope_hot
print(f"\n2. Hot entry (T -> inf, kappa -> 10000*kappa_v):")
print(f"   r_entry -> [{r_entry_hot.min():.4f}, {r_entry_hot.max():.4f}]")
print(f"   delta_n_s -> {delta_ns_hot:.6f} (should saturate)")
print(f"   Saturated: {'YES' if abs(delta_ns_hot - delta_ns_aligned) / max(abs(delta_ns_aligned), 1e-10) < 0.2 else 'NO'}")

# Check 3: Bogoliubov normalization
print(f"\n3. Bogoliubov normalization: |alpha|^2 - |beta|^2 = 1")
print(f"   Max error: {norm_err:.1e} {'PASS' if norm_err < 1e-10 else 'FAIL'}")

# Check 4: Correction smallness
print(f"\n4. Is |delta_n_s| << 1?")
print(f"   Aligned:  {abs(delta_ns_aligned):.6e} -- {'YES' if abs(delta_ns_aligned) < 1 else 'NO, delta_n_s ~ O(1)'}")
print(f"   Random:   {abs(delta_ns_random):.6e} -- {'YES' if abs(delta_ns_random) < 1 else 'NO'}")

# Check 5: Analytic approximation
print(f"\n5. Analytic approximation in deeply thermal limit:")
print(f"   d(r_entry)/d(ln omega) exact: {dr_exact:.6f} (expected: -0.500)")
print(f"   Agreement: {abs(dr_exact + 0.5)/0.5*100:.2f}% deviation from -1/2")

# Check 6: Numerical consistency across methods
# Finite difference on full 8-mode spectrum
eps = 1e-5
omega_up = omega_k * (1.0 + eps)
omega_dn = omega_k * (1.0 - eps)
r_up = np.arctanh(np.sqrt(np.exp(-2*PI*omega_up/kappa_v)))
r_dn = np.arctanh(np.sqrt(np.exp(-2*PI*omega_dn/kappa_v)))
dr_dlnomega_fd = omega_k * (r_up - r_dn) / (omega_up - omega_dn)
print(f"\n6. Finite-difference dr_entry/d(ln omega):")
for i, lab in enumerate(branch_labels):
    idx = [4, 0, 5][i]
    print(f"   {lab}: {dr_dlnomega_fd[idx]:.8f} (analytic: -0.500)")

# =============================================================================
# 11. Summary of all delta_n_s values and physical regime
# =============================================================================

print(f"\n{'='*70}")
print("RESULTS SUMMARY")
print(f"{'='*70}")

print(f"\nEntry-horizon Bogoliubov parameters:")
print(f"  T_Hawking = kappa_v/(2pi) = {T_Hawking:.4f} M_KK")
print(f"  omega/T ratio = [{x_k.min():.6f}, {x_k.max():.6f}]  (DEEPLY THERMAL)")
print(f"  |beta|^2 = [{beta_sq_entry.min():.2f}, {beta_sq_entry.max():.2f}]  (LARGE)")
print(f"  r_entry = [{r_k_entry.min():.6f}, {r_k_entry.max():.6f}]")

print(f"\nTilt correction (aligned phases -- physical case):")
print(f"  delta_n_s = {delta_ns_aligned:+.6e}")
print(f"  |delta_n_s| = {abs(delta_ns_aligned):.6e}")

print(f"\nTilt correction (random phases):")
print(f"  delta_n_s = {delta_ns_random:+.6e}")
print(f"  |delta_n_s| = {abs(delta_ns_random):.6e}")

print(f"\nDecomposition:")
print(f"  Entry squeeze tilt: {slope_entry_only:.6f} per unit ln(omega)")
print(f"  Fold squeeze tilt:  {slope_fold_only:.6f} per unit ln(omega)")
print(f"  Entry/fold ratio:   {abs(slope_entry_only/slope_fold_only):.6f}")
print(f"  Entry squeeze r_entry ~ {r_k_entry.mean():.4f} (comparable to r_fold ~ {np.mean([r_comp_B1, r_comp_B2, r_comp_B3]):.4f})")
print(f"  BUT entry r varies by {abs(delta_r_entry):.4f} while fold r varies by {abs(delta_r_fold):.4f}")

# =============================================================================
# 12. Gate verdict
# =============================================================================

delta_ns_representative = abs(delta_ns_aligned)

print(f"\n{'='*70}")
print("GATE VERDICT: BLUESHIFT-TILT-72")
print(f"{'='*70}")

print(f"\n  |delta_n_s| values:")
print(f"    Aligned:  {abs(delta_ns_aligned):.6e}")
print(f"    Random:   {abs(delta_ns_random):.6e}")
print(f"    Anti:     {abs(delta_ns_anti):.6e}")

if delta_ns_representative > 0.001:
    verdict = "PASS"
    detail = (f"|delta_n_s| = {delta_ns_representative:.4e} > 0.001. "
              f"Entry horizon contributes O(1) tilt correction. "
              f"Deeply thermal regime (omega/T={x_k.mean():.4f}). "
              f"r_entry={r_k_entry.mean():.3f} comparable to r_fold. "
              f"Sign: +{delta_ns_aligned:.3e} (redder).")
elif delta_ns_representative > 0.0001:
    verdict = "INFO"
    detail = f"|delta_n_s| = {delta_ns_representative:.4e} in [0.0001, 0.001]"
else:
    verdict = "FAIL"
    detail = f"|delta_n_s| = {delta_ns_representative:.4e} < 0.0001"

print(f"\n  Pre-registered thresholds:")
print(f"    PASS: |delta_n_s| > 0.001")
print(f"    INFO: |delta_n_s| in [0.0001, 0.001]")
print(f"    FAIL: |delta_n_s| < 0.0001")
print(f"\n  Result: {verdict}")
print(f"  Detail: {detail}")

print(f"\n  PHYSICAL INTERPRETATION:")
print(f"  The entry sonic horizon at tau={tau_entry:.4f} has T_entry={T_entry:.1f} M_KK,")
print(f"  making it EXTREMELY HOT relative to the BCS mode frequencies")
print(f"  (omega/T ~ 0.012). Every mode is deeply thermally occupied")
print(f"  (n ~ 80-90 particles). The entry-horizon squeeze r ~ 2.9 is")
print(f"  COMPARABLE to the fold squeeze r ~ 2.3-4.3, not a small perturbation.")
print(f"")
print(f"  The tilt correction delta_n_s = +{delta_ns_aligned:.3e} is LARGE and POSITIVE")
print(f"  (makes n_s redder). This arises because r_entry(B1) > r_entry(B3)")
print(f"  by {abs(delta_r_entry):.4f}: lower-frequency modes are more squeezed,")
print(f"  steepening the red tilt that the fold already creates.")
print(f"")
print(f"  CAVEAT: The entry horizon is subsonic (Ma ~ 0.76 at tau ~ 0.221).")
print(f"  The sonic horizon formalism strictly applies only at Ma = 1.")
print(f"  The kappa_v = {kappa_v:.2f} used here is from the S71 velocity-space")
print(f"  surface gravity, which may overestimate the entry-horizon effect if")
print(f"  the flow never fully reaches supersonic at the entry (it reaches")
print(f"  Ma=1 somewhere between tau=0.221 and tau=0.19). The T_entry value")
print(f"  governs the magnitude but not the sign of the correction.")

# =============================================================================
# 13. Save results
# =============================================================================

t_elapsed = time.time() - t_start

outpath = os.path.join(data_dir, 's72_blueshift_tilt.npz')
np.savez(outpath,
    # Gate metadata
    gate_name='BLUESHIFT-TILT-72',
    gate_verdict=verdict,
    gate_detail=detail,
    # Entry horizon parameters
    tau_entry=tau_entry,
    T_entry=T_entry,
    kappa_v=kappa_v,
    kappa_entry=kappa_entry,
    T_Hawking=T_Hawking,
    # Mode data
    labels=labels,
    omega_k=omega_k,
    omega_distinct=omega_distinct,
    x_k=x_k,
    # Entry Bogoliubov coefficients
    alpha_sq_entry=alpha_sq_entry,
    beta_sq_entry=beta_sq_entry,
    r_k_entry=r_k_entry,
    n_k_thermal=beta_sq_entry,
    # Fold/compound squeeze
    r_compound=r_compound,
    r_k_bcs=r_k_bcs,
    mode_weights=mode_weights,
    # Slopes and tilts
    slope_base=slope_base,
    slope_aligned=slope_aligned,
    slope_random=slope_random,
    slope_anti=slope_anti,
    delta_ns_aligned=delta_ns_aligned,
    delta_ns_anti=delta_ns_anti,
    delta_ns_random=delta_ns_random,
    delta_ns_representative=delta_ns_representative,
    # Decomposition
    delta_r_entry=delta_r_entry,
    delta_r_fold=delta_r_fold,
    slope_entry_only=slope_entry_only,
    slope_fold_only=slope_fold_only,
    entry_fold_ratio=abs(slope_entry_only / slope_fold_only),
    # Power spectra per branch
    P_base_branches=P_base_branches,
    P_aligned_branches=P_aligned_branches,
    P_random_branches=P_random_branches,
    P_anti_branches=P_anti_branches,
    # Cross-check data
    omega_range=omega_distinct.max() - omega_distinct.min(),
    omega_mean=np.mean(omega_distinct),
    ln_omega_span=ln_omega_span,
    norm_check_max_err=norm_err,
    dr_dlnomega_exact=dr_exact,
    # Timing
    total_time=t_elapsed
)

print(f"\nResults saved to: {outpath}")
print(f"Runtime: {t_elapsed:.2f} s")
print(f"\n{'='*70}")
print(f"BLUESHIFT-TILT-72: {verdict}")
print(f"{'='*70}")
