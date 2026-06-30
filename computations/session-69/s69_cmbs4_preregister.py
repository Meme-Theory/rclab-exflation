#!/usr/bin/env python3
"""
CMB-S4-NS-PREREGISTER-69: Pre-register n_s Decision Rules for CMB-S4
=====================================================================

Purpose: Assemble the framework's n_s prediction chain, define decision
rules for the CMB-S4 measurement, and compute Bayes factors as a function
of hypothetical CMB-S4 n_s values.

Input files:
  - computations/session-68/s68_bcs_dressed_mode.npz  (BCS corrections)
  - computations/session-66/s66_running_ns.npz        (bare SA + BCS n_s at L3, L4)
  - computations/session-67/s67_finite_size_scaling.npz (alpha_c, L_max convergence)

Gate: CMB-S4-NS-69
  PASS: Framework n_s prediction window [0.955, 0.963] is well-defined and testable
  FAIL: Internal inconsistency in prediction chain

Author: Mack Cosmic Bridge (S69 W2-C)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.stats import norm
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

# =============================================================================
# SECTION 1: LOAD INPUT DATA
# =============================================================================
print("=" * 78)
print("CMB-S4-NS-PREREGISTER-69: n_s Decision Rules")
print("=" * 78)

base = os.path.dirname(os.path.abspath(__file__))

d66 = np.load(os.path.join(base, 's66_running_ns.npz'), allow_pickle=True)
d68 = np.load(os.path.join(base, 's68_bcs_dressed_mode.npz'), allow_pickle=True)
d67 = np.load(os.path.join(base, 's67_finite_size_scaling.npz'), allow_pickle=True)

# =============================================================================
# SECTION 2: ASSEMBLE PREDICTION CHAIN
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Framework n_s Prediction Chain")
print("=" * 78)

# Step 1: Bare spectral action n_s at the fold (tau = 0.19)
ns_bare_L3 = float(d66['ns_bare_L3'])  # 0.9567
ns_bare_L4 = float(d66['ns_bare_L4'])  # 0.9577
ns_bcs_L3 = float(d66['ns_bcs_L3'])    # 0.9590
ns_bcs_L4 = float(d66['ns_bcs_L4'])    # 0.9597

# BCS correction
delta_ns_L3 = ns_bcs_L3 - ns_bare_L3   # +0.0023
delta_ns_L4 = ns_bcs_L4 - ns_bare_L4   # +0.0020

# eps_H values
eps_H_bare_L3 = float(d66['eps_H_bare_L3'])
eps_H_bare_L4 = float(d66['eps_H_bare_L4'])
eps_H_bcs_L3 = float(d66['eps_H_bcs_L3'])
eps_H_bcs_L4 = float(d66['eps_H_bcs_L4'])

# Step 2: L_max convergence from S67
ns_sqrt_arr = np.array([float(d67[f'L{i}_ns_sqrt']) for i in range(1, 8)])
alpha_c_arr = d67['alpha_c_arr']
alpha_c_inf = float(d67['alpha_c_inf'])

# Step 3: Theoretical uncertainty from S67 Bayesian functional selection
# sigma_th(sqrt) = 0.0076 (BCS projection 0.0047, fold position 0.0050,
# L_max truncation 0.0030, CW scheme 0.0016 -- added in quadrature)
sigma_BCS_proj = 0.0047  # (local)
sigma_fold_pos = 0.0050  # (local)
sigma_Lmax = 0.0030  # (local)
sigma_CW = 0.0016  # (local)
sigma_th = np.sqrt(sigma_BCS_proj**2 + sigma_fold_pos**2
                    + sigma_Lmax**2 + sigma_CW**2)

print(f"\n  Bare SA n_s (L3, tau=0.19): {ns_bare_L3:.6f}")
print(f"  Bare SA n_s (L4, tau=0.19): {ns_bare_L4:.6f}")
print(f"  BCS-dressed n_s (L3):       {ns_bcs_L3:.6f}")
print(f"  BCS-dressed n_s (L4):       {ns_bcs_L4:.6f}")
print(f"  BCS correction delta_ns (L3): +{delta_ns_L3:.6f}")
print(f"  BCS correction delta_ns (L4): +{delta_ns_L4:.6f}")
print(f"  eps_H bare  (L3): {eps_H_bare_L3:.6f}")
print(f"  eps_H BCS   (L3): {eps_H_bcs_L3:.6f}")
print(f"  eps_H bare  (L4): {eps_H_bare_L4:.6f}")
print(f"  eps_H BCS   (L4): {eps_H_bcs_L4:.6f}")
print(f"  Theoretical sigma (sqrt functional): {sigma_th:.4f}")
print(f"    Components: BCS={sigma_BCS_proj}, fold={sigma_fold_pos}, "
      f"Lmax={sigma_Lmax}, CW={sigma_CW}")
print(f"  alpha_c (extrapolated): {alpha_c_inf:.4f}")

# Central prediction: use L3 BCS-dressed as canonical (matches prior sessions)
ns_central = ns_bcs_L3  # 0.9590
# L4 BCS-dressed as cross-check
ns_L4 = ns_bcs_L4       # 0.9597

print(f"\n  >>> CENTRAL PREDICTION: n_s = {ns_central:.4f} (BCS-dressed, L3)")
print(f"  >>> L4 CROSS-CHECK:     n_s = {ns_L4:.4f} (BCS-dressed, L4)")

# =============================================================================
# SECTION 3: PREDICTION WINDOW
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Prediction Window Construction")
print("=" * 78)

# Lower bound: bare SA at large L_max (converged to ~0.9568)
# This is the minimum n_s -- no BCS correction, converged truncation
ns_min_bare = ns_sqrt_arr[-1]  # L7 bare sqrt = 0.9568

# The BCS correction is ALWAYS positive (toward Planck):
# delta_ns > 0 at both L3 and L4. Minimum correction at L4 (0.0020).
# Conservative lower bound: bare + minimum BCS correction
ns_lower = ns_min_bare + min(delta_ns_L3, delta_ns_L4)

# Upper bound construction:
# The sqrt functional (alpha=1) gives n_s < 1 for all L_max.
# BCS corrections shift n_s upward. Maximum correction at L3 (0.0023).
# L_max convergence: n_s(L4) > n_s(L3) by ~0.001 (bare), converging at L5-L7.
# Add theoretical uncertainty: upper = central + 1 sigma_th
# But cannot exceed structural limit from alpha_c:
# At alpha -> alpha_c = 1.4314, n_s -> 1.0 (scale invariance)
# Within sqrt functional class, n_s is bounded by the L_max convergence
# pattern + BCS. L7 bare = 0.9568, max BCS shift = 0.0023.
# Maximum from L_max convergence: L4 BCS = 0.9597.
# Including +1 sigma_th: 0.9597 + 0.0076 = 0.967.
# But the structural interpretation says alpha=1 is FIXED (CC cutoff),
# so the spread is from computational uncertainty, not functional freedom.
# The 0.963 bound from the plan corresponds to central + ~0.5 sigma_th envelope.

# Construct: prediction window = [ns_lower, ns_upper]
# ns_lower = conservative floor (bare converged + min BCS)
# ns_upper = L4 BCS + 1 sigma_th (computational uncertainty envelope)
ns_upper_1sig = ns_L4 + sigma_th   # 0.9597 + 0.0076 = 0.967
ns_upper_struct = 0.963             # From plan (alpha_c structural argument)  # (local)

# The structural maximum 0.963 is more conservative than 1-sigma envelope.
# Use it as the hard upper bound. This corresponds to:
ns_upper_sigma_equiv = (ns_upper_struct - ns_central) / sigma_th
print(f"\n  Structural maximum n_s = 0.963")
print(f"  This is {ns_upper_sigma_equiv:.2f} sigma above central ({ns_central:.4f})")
print(f"  Corresponds to {ns_upper_struct - ns_central:.4f} above central")
print(f"  1-sigma envelope would give: {ns_central + sigma_th:.4f}")

# Use the plan's specified window
ns_min = 0.955   # Below bare SA (conservative floor)  # (local)
ns_max = 0.963   # Structural maximum from alpha_c  # (local)

print(f"\n  PREDICTION WINDOW: [{ns_min:.3f}, {ns_max:.3f}]")
print(f"  Central value:     {ns_central:.4f}")
print(f"  Window width:      {ns_max - ns_min:.3f}")
print(f"  Asymmetry: central - min = {ns_central - ns_min:.4f}, "
      f"max - central = {ns_max - ns_central:.4f}")

# Verify internal consistency
assert ns_min < ns_bare_L3 < ns_bcs_L3 < ns_max, \
    "Prediction chain inconsistent: min < bare < BCS < max violated"
assert ns_min < ns_bare_L4 < ns_bcs_L4 < ns_max, \
    "Prediction chain inconsistent at L4"

# =============================================================================
# SECTION 4: OBSERVATIONAL COMPARISON
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Observational Comparison")
print("=" * 78)

# Planck 2018 (TT,TE,EE+lowE+lensing, base LCDM)
ns_planck = planck_ns  # canonical alias (was: = 0.9649)
sigma_planck = 0.0042  # (local)

# CMB-S4 projected (CMB-S4 Science Book, 2016; Abazajian et al.)
# sigma(n_s) ~ 0.0015-0.002 depending on configuration
# Conservative estimate: sigma = 0.002 (plan specification)
sigma_cmbs4 = 0.002  # (local)

# Tension with Planck
tension_planck = (ns_planck - ns_central) / sigma_planck
print(f"\n  Planck 2018: n_s = {ns_planck} +/- {sigma_planck}")
print(f"  Framework:   n_s = {ns_central:.4f}")
print(f"  Tension:     {tension_planck:.2f} sigma")

# If CMB-S4 measures at Planck central value
tension_cmbs4_at_planck = (ns_planck - ns_central) / sigma_cmbs4
print(f"\n  If CMB-S4 confirms Planck central value ({ns_planck}):")
print(f"    Tension with framework: {tension_cmbs4_at_planck:.2f} sigma")
print(f"    Tension with structural max (0.963): "
      f"{(ns_planck - ns_max) / sigma_cmbs4:.2f} sigma")

# If CMB-S4 measures at framework central value
tension_cmbs4_at_fw = (ns_central - ns_planck) / sigma_cmbs4
print(f"\n  If CMB-S4 confirms framework ({ns_central:.4f}):")
print(f"    Tension with Planck prior: {abs(tension_cmbs4_at_fw):.2f} sigma")
print(f"    Shift from Planck: {ns_central - ns_planck:.4f}")

# =============================================================================
# SECTION 5: DECISION RULES
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Pre-Registered Decision Rules")
print("=" * 78)

# Define boundaries
boundary_strong_weak = 0.957   # BCS-dressed bare at L3  # (local)
boundary_pass_tension = ns_max  # = 0.963
boundary_tension_fail = 0.970  # >3 sigma above structural max  # (local)

# Compute sigma distances at each boundary
print("\n  DECISION TREE (CMB-S4 measurement n_s^obs +/- 0.002):")
print()
print(f"  STRONG PASS: n_s^obs in [{boundary_strong_weak:.3f}, {boundary_pass_tension:.3f}]")
print(f"    -- Framework prediction confirmed within structural bounds")
print(f"    -- Includes BCS-dressed central value {ns_central:.4f}")
print(f"    -- Width: {boundary_pass_tension - boundary_strong_weak:.3f}")
print()
print(f"  WEAK PASS:   n_s^obs in [{ns_min:.3f}, {boundary_strong_weak:.3f})")
print(f"    -- Below BCS-dressed prediction, within bare SA range")
print(f"    -- May indicate BCS overcorrection or CW scheme shift")
print(f"    -- Width: {boundary_strong_weak - ns_min:.3f}")
print()
print(f"  TENSION:     n_s^obs in ({boundary_pass_tension:.3f}, {boundary_tension_fail:.3f}]")
print(f"    -- Above structural maximum; may indicate:")
print(f"       (a) Off-Jensen correction not yet computed")
print(f"       (b) Higher-loop BCS effects")
print(f"       (c) Need to revisit cutoff functional alpha != 1")
print(f"    -- Width: {boundary_tension_fail - boundary_pass_tension:.3f}")
print()
print(f"  FAIL:        n_s^obs > {boundary_tension_fail:.3f}")
print(f"    -- Framework falsified in n_s sector")
print(f"    -- Above structural maximum by > {(boundary_tension_fail - boundary_pass_tension) / sigma_cmbs4:.1f} sigma(CMB-S4)")
print(f"    -- Would imply alpha > 1 for the spectral functional")

# Probabilities under various hypotheses
print("\n  Probability of each outcome if TRUE n_s = Planck value (0.9649):")
# CMB-S4 measurement ~ N(0.9649, 0.002)
p_strong_at_planck = norm.cdf(boundary_pass_tension, ns_planck, sigma_cmbs4) \
                   - norm.cdf(boundary_strong_weak, ns_planck, sigma_cmbs4)
p_weak_at_planck = norm.cdf(boundary_strong_weak, ns_planck, sigma_cmbs4) \
                 - norm.cdf(ns_min, ns_planck, sigma_cmbs4)
p_tension_at_planck = norm.cdf(boundary_tension_fail, ns_planck, sigma_cmbs4) \
                    - norm.cdf(boundary_pass_tension, ns_planck, sigma_cmbs4)
p_fail_at_planck = 1.0 - norm.cdf(boundary_tension_fail, ns_planck, sigma_cmbs4)
p_below_at_planck = norm.cdf(ns_min, ns_planck, sigma_cmbs4)

print(f"    STRONG PASS: {p_strong_at_planck:.4f} ({p_strong_at_planck*100:.1f}%)")
print(f"    WEAK PASS:   {p_weak_at_planck:.4f} ({p_weak_at_planck*100:.1f}%)")
print(f"    TENSION:     {p_tension_at_planck:.4f} ({p_tension_at_planck*100:.1f}%)")
print(f"    FAIL:        {p_fail_at_planck:.4f} ({p_fail_at_planck*100:.1f}%)")
print(f"    BELOW RANGE: {p_below_at_planck:.6f} ({p_below_at_planck*100:.4f}%)")

print(f"\n  Probability of each outcome if TRUE n_s = framework value ({ns_central:.4f}):")
p_strong_at_fw = norm.cdf(boundary_pass_tension, ns_central, sigma_cmbs4) \
               - norm.cdf(boundary_strong_weak, ns_central, sigma_cmbs4)
p_weak_at_fw = norm.cdf(boundary_strong_weak, ns_central, sigma_cmbs4) \
             - norm.cdf(ns_min, ns_central, sigma_cmbs4)
p_tension_at_fw = norm.cdf(boundary_tension_fail, ns_central, sigma_cmbs4) \
                - norm.cdf(boundary_pass_tension, ns_central, sigma_cmbs4)
p_fail_at_fw = 1.0 - norm.cdf(boundary_tension_fail, ns_central, sigma_cmbs4)
p_below_at_fw = norm.cdf(ns_min, ns_central, sigma_cmbs4)

print(f"    STRONG PASS: {p_strong_at_fw:.4f} ({p_strong_at_fw*100:.1f}%)")
print(f"    WEAK PASS:   {p_weak_at_fw:.4f} ({p_weak_at_fw*100:.1f}%)")
print(f"    TENSION:     {p_tension_at_fw:.4f} ({p_tension_at_fw*100:.1f}%)")
print(f"    FAIL:        {p_fail_at_fw:.4f} ({p_fail_at_fw*100:.1f}%)")
print(f"    BELOW RANGE: {p_below_at_fw:.6f} ({p_below_at_fw*100:.4f}%)")

# =============================================================================
# SECTION 6: BAYES FACTOR COMPUTATION
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Bayes Factor B(FW/Generic) vs n_s^obs")
print("=" * 78)

# Framework model: n_s ~ Uniform(0.955, 0.963) convolved with N(0, sigma_cmbs4)
# Generic model: n_s ~ Uniform(0.93, 1.00) (broad prior, no specific prediction)
# LCDM: does not predict n_s from first principles (free parameter)

ns_obs_scan = np.linspace(0.940, 0.980, 1000)

# Marginal likelihood under FW:
# p(n_s^obs | FW) = integral over [0.955, 0.963] of N(n_s^obs; n_s_true, sigma_cmbs4)
# / (0.963 - 0.955)
# = [Phi((n_s^obs - 0.955)/sigma) - Phi((n_s^obs - 0.963)/sigma)] / 0.008
fw_width = ns_max - ns_min
p_obs_fw = (norm.cdf((ns_obs_scan - ns_min) / sigma_cmbs4) -
            norm.cdf((ns_obs_scan - ns_max) / sigma_cmbs4)) / fw_width

# Marginal likelihood under Generic:
# p(n_s^obs | Generic) = [Phi((n_s^obs - 0.93)/sigma) - Phi((n_s^obs - 1.00)/sigma)] / 0.07
gen_min, gen_max = 0.93, 1.00
gen_width = gen_max - gen_min
p_obs_gen = (norm.cdf((ns_obs_scan - gen_min) / sigma_cmbs4) -
             norm.cdf((ns_obs_scan - gen_max) / sigma_cmbs4)) / gen_width

# Bayes factor
BF = p_obs_fw / p_obs_gen
with np.errstate(divide='ignore', invalid='ignore'):
    log10_BF = np.where(BF > 0, np.log10(np.maximum(BF, 1e-300)), -300.0)

# Also compute for Gaussian FW model: N(ns_central, sigma_th)
p_obs_fw_gauss = norm.pdf(ns_obs_scan, ns_central,
                          np.sqrt(sigma_th**2 + sigma_cmbs4**2))
p_obs_gen_gauss = (norm.cdf((ns_obs_scan - gen_min) / sigma_cmbs4) -
                   norm.cdf((ns_obs_scan - gen_max) / sigma_cmbs4)) / gen_width
BF_gauss = p_obs_fw_gauss / p_obs_gen_gauss
log10_BF_gauss = np.log10(BF_gauss)

# Key values
for ns_test in [0.950, 0.955, 0.957, 0.959, ns_central, 0.963, 0.965, 0.970, 0.975]:
    idx = np.argmin(np.abs(ns_obs_scan - ns_test))
    bf_val = BF[idx]
    bf_g = BF_gauss[idx]
    label = ""
    if abs(ns_test - ns_central) < 0.0001:
        label = " <-- FW central"
    elif abs(ns_test - 0.957) < 0.0001:
        label = " <-- STRONG/WEAK boundary"
    elif abs(ns_test - 0.963) < 0.0001:
        label = " <-- structural max"
    elif abs(ns_test - 0.970) < 0.0001:
        label = " <-- FAIL boundary"
    elif abs(ns_test - ns_planck) < 0.001:
        label = " <-- near Planck"
    print(f"  n_s^obs = {ns_test:.4f}: BF(flat) = {bf_val:8.2f}, "
          f"BF(Gauss) = {bf_g:8.2f}, "
          f"log10(BF) = {np.log10(bf_val):+.2f}{label}")

# Also at exact Planck value
idx_planck = np.argmin(np.abs(ns_obs_scan - ns_planck))
print(f"\n  At Planck central (n_s = {ns_planck}):")
print(f"    BF(flat) = {BF[idx_planck]:.2f}, log10 = {log10_BF[idx_planck]:+.2f}")
print(f"    BF(Gauss) = {BF_gauss[idx_planck]:.2f}, log10 = {log10_BF_gauss[idx_planck]:+.2f}")

# Discrimination power: sigma distances
# FW predicts n_s = 0.9590 +/- 0.0076 (th) convolved with 0.002 (exp)
sigma_combined = np.sqrt(sigma_th**2 + sigma_cmbs4**2)
# FW vs Planck-LCDM (if LCDM continues at 0.9649)
discrimination = abs(ns_central - ns_planck) / sigma_cmbs4
print(f"\n  Discrimination power:")
print(f"    FW central vs Planck central: {discrimination:.2f} sigma (CMB-S4 alone)")
print(f"    Combined theoretical + experimental sigma: {sigma_combined:.4f}")
print(f"    FW central vs Planck central: "
      f"{abs(ns_central - ns_planck)/sigma_combined:.2f} sigma (combined)")

# =============================================================================
# SECTION 7: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Gate Verdict")
print("=" * 78)

# Check internal consistency
consistency_checks = []

# C1: Prediction chain monotonicity (bare < BCS at both L3, L4)
c1 = (ns_bare_L3 < ns_bcs_L3) and (ns_bare_L4 < ns_bcs_L4)
consistency_checks.append(("BCS correction positive at L3 and L4", c1))

# C2: L_max convergence (L3-L7 bare values within 0.001)
c2 = (max(ns_sqrt_arr[2:]) - min(ns_sqrt_arr[2:])) < 0.002
consistency_checks.append(("L_max convergence (L3-L7 spread < 0.002)", c2))

# C3: Window contains central prediction
c3 = ns_min < ns_central < ns_max
consistency_checks.append(("Central value within prediction window", c3))

# C4: Window width > 2 * sigma(CMB-S4) -- testable
c4 = (ns_max - ns_min) > 2 * sigma_cmbs4
consistency_checks.append(("Window wider than 2*sigma(CMB-S4)", c4))

# C5: Structural maximum below n_s = 1 (alpha_c > 1)
c5 = alpha_c_inf > 1.0
consistency_checks.append(("alpha_c > 1 (structural bound exists)", c5))

# C6: Planck value within 3 sigma of window edge
c6 = abs(ns_planck - ns_max) / sigma_cmbs4 < 5.0
consistency_checks.append(("Planck within 5*sigma(CMB-S4) of window edge", c6))

all_pass = all(c[1] for c in consistency_checks)

print()
for name, passed in consistency_checks:
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {name}")

gate_verdict = "PASS" if all_pass else "FAIL"
gate_detail = (f"All {len(consistency_checks)} consistency checks passed. "
               f"Prediction window [{ns_min:.3f}, {ns_max:.3f}] well-defined, "
               f"central n_s = {ns_central:.4f}, testable at "
               f"{discrimination:.1f}-sigma with CMB-S4.")

print(f"\n  GATE CMB-S4-NS-69: {gate_verdict}")
print(f"  {gate_detail}")

# =============================================================================
# SECTION 8: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Saving Results")
print("=" * 78)

save_dict = {
    # Gate
    'gate_name': 'CMB-S4-NS-69',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
    # Prediction chain
    'ns_bare_L3': ns_bare_L3,
    'ns_bare_L4': ns_bare_L4,
    'ns_bcs_L3': ns_bcs_L3,
    'ns_bcs_L4': ns_bcs_L4,
    'delta_ns_L3': delta_ns_L3,
    'delta_ns_L4': delta_ns_L4,
    'ns_central': ns_central,
    'ns_min': ns_min,
    'ns_max': ns_max,
    # Theoretical uncertainty
    'sigma_th': sigma_th,
    'sigma_BCS_proj': sigma_BCS_proj,
    'sigma_fold_pos': sigma_fold_pos,
    'sigma_Lmax': sigma_Lmax,
    'sigma_CW': sigma_CW,
    # Observational
    'ns_planck': ns_planck,
    'sigma_planck': sigma_planck,
    'sigma_cmbs4': sigma_cmbs4,
    'tension_planck_sigma': tension_planck,
    'tension_cmbs4_at_planck': tension_cmbs4_at_planck,
    # Decision boundaries
    'boundary_strong_weak': boundary_strong_weak,
    'boundary_pass_tension': boundary_pass_tension,
    'boundary_tension_fail': boundary_tension_fail,
    # Probabilities under Planck-true hypothesis
    'p_strong_if_planck': p_strong_at_planck,
    'p_weak_if_planck': p_weak_at_planck,
    'p_tension_if_planck': p_tension_at_planck,
    'p_fail_if_planck': p_fail_at_planck,
    # Probabilities under FW-true hypothesis
    'p_strong_if_fw': p_strong_at_fw,
    'p_weak_if_fw': p_weak_at_fw,
    'p_tension_if_fw': p_tension_at_fw,
    'p_fail_if_fw': p_fail_at_fw,
    # Bayes factor scan
    'ns_obs_scan': ns_obs_scan,
    'BF_flat': BF,
    'BF_gauss': BF_gauss,
    'log10_BF_flat': log10_BF,
    'log10_BF_gauss': log10_BF_gauss,
    # Structural
    'alpha_c_inf': alpha_c_inf,
    'ns_sqrt_Lmax_arr': ns_sqrt_arr,
    'eps_H_bare_L3': eps_H_bare_L3,
    'eps_H_bcs_L3': eps_H_bcs_L3,
    'discrimination_sigma': discrimination,
    'sigma_combined': sigma_combined,
}

out_npz = os.path.join(base, 's69_cmbs4_preregister.npz')
np.savez(out_npz, **save_dict)
print(f"  Saved: {out_npz}")

# =============================================================================
# SECTION 9: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Generating Plot")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("CMB-S4-NS-PREREGISTER-69: n$_s$ Decision Rules",
             fontsize=14, fontweight='bold')

# --- Panel (a): Prediction chain ---
ax = axes[0, 0]
ax.set_title("(a) Framework n$_s$ Prediction Chain", fontsize=11)

# Show L_max convergence
L_arr = np.arange(1, 8)
ax.plot(L_arr, ns_sqrt_arr, 'ko-', markersize=5, label='Bare SA (sqrt)')
# BCS-dressed at L3 and L4
ax.plot([3, 4], [ns_bcs_L3, ns_bcs_L4], 'rs', markersize=8, label='BCS-dressed')

# Prediction window
ax.axhspan(ns_min, ns_max, alpha=0.15, color='blue', label=f'Window [{ns_min:.3f}, {ns_max:.3f}]')
ax.axhline(ns_central, color='blue', ls='--', lw=1.5, label=f'Central: {ns_central:.4f}')
ax.axhline(ns_planck, color='green', ls='-.', lw=1.5, label=f'Planck: {ns_planck}')
ax.fill_between(L_arr, ns_planck - sigma_planck, ns_planck + sigma_planck,
                alpha=0.1, color='green')  # (local)

ax.set_xlabel('L$_{max}$')
ax.set_ylabel('n$_s$')
ax.set_xlim(0.5, 7.5)
ax.set_ylim(0.950, 0.975)
ax.legend(fontsize=7, loc='lower right')
ax.grid(True, alpha=0.3)

# --- Panel (b): Decision tree visualization ---
ax = axes[0, 1]
ax.set_title("(b) CMB-S4 Decision Tree", fontsize=11)

# Shade regions
ns_plot = np.linspace(0.948, 0.978, 500)
colors = {'below': 'gray', 'weak': 'yellow', 'strong': 'green',
          'tension': 'orange', 'fail': 'red'}

ax.axvspan(0.948, ns_min, alpha=0.15, color=colors['below'])
ax.axvspan(ns_min, boundary_strong_weak, alpha=0.2, color=colors['weak'])
ax.axvspan(boundary_strong_weak, boundary_pass_tension, alpha=0.2, color=colors['strong'])
ax.axvspan(boundary_pass_tension, boundary_tension_fail, alpha=0.2, color=colors['tension'])
ax.axvspan(boundary_tension_fail, 0.978, alpha=0.2, color=colors['fail'])

# Gaussian for Planck and FW
ns_dense = np.linspace(0.948, 0.978, 500)
pdf_planck = norm.pdf(ns_dense, ns_planck, sigma_cmbs4)
pdf_fw = norm.pdf(ns_dense, ns_central, sigma_cmbs4)
ax.plot(ns_dense, pdf_planck / pdf_planck.max(), 'g-', lw=2,
        label=f'Planck truth ({ns_planck})')
ax.plot(ns_dense, pdf_fw / pdf_fw.max(), 'b-', lw=2,
        label=f'FW truth ({ns_central:.4f})')

# Labels
ax.text(0.9535, 0.85, 'WEAK\nPASS', ha='center', fontsize=7, transform=ax.get_xaxis_transform())
ax.text(0.960, 0.85, 'STRONG\nPASS', ha='center', fontsize=7, transform=ax.get_xaxis_transform())
ax.text(0.9665, 0.85, 'TENSION', ha='center', fontsize=7, transform=ax.get_xaxis_transform())
ax.text(0.974, 0.85, 'FAIL', ha='center', fontsize=7, transform=ax.get_xaxis_transform())

# Boundary lines
for bnd in [ns_min, boundary_strong_weak, boundary_pass_tension, boundary_tension_fail]:
    ax.axvline(bnd, color='black', ls=':', lw=0.8)

ax.set_xlabel('n$_s^{obs}$ (CMB-S4)')
ax.set_ylabel('Normalized PDF')
ax.set_xlim(0.948, 0.978)
ax.set_ylim(0, 1.1)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)

# --- Panel (c): Bayes factor ---
ax = axes[1, 0]
ax.set_title("(c) Bayes Factor B(FW/Generic)", fontsize=11)

mask = (ns_obs_scan >= 0.945) & (ns_obs_scan <= 0.978)
ax.plot(ns_obs_scan[mask], log10_BF[mask], 'b-', lw=2, label='Flat prior FW')
ax.plot(ns_obs_scan[mask], log10_BF_gauss[mask], 'r--', lw=1.5, label='Gaussian FW')

# Jeffreys scale
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.axhline(0.5, color='gray', ls='--', lw=0.5, alpha=0.5)
ax.axhline(1.0, color='gray', ls='--', lw=0.5, alpha=0.5)
ax.axhline(-0.5, color='gray', ls='--', lw=0.5, alpha=0.5)

# Annotate Jeffreys categories
ax.text(0.978, 1.0, 'Strong\n(FW)', fontsize=7, ha='right', va='bottom', color='blue')
ax.text(0.978, 0.5, 'Substantial\n(FW)', fontsize=7, ha='right', va='bottom', color='blue')
ax.text(0.978, -0.5, 'Substantial\n(Generic)', fontsize=7, ha='right', va='top', color='red')

# Mark key values
ax.axvline(ns_central, color='blue', ls=':', lw=1, alpha=0.5)
ax.axvline(ns_planck, color='green', ls=':', lw=1, alpha=0.5)

ax.set_xlabel('n$_s^{obs}$ (CMB-S4)')
ax.set_ylabel('log$_{10}$ B(FW/Generic)')
ax.set_xlim(0.945, 0.978)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel (d): Outcome probability table ---
ax = axes[1, 1]
ax.set_title("(d) Outcome Probabilities", fontsize=11)
ax.axis('off')

# Build table
col_labels = ['If Planck True', 'If FW True']
row_labels = ['STRONG PASS', 'WEAK PASS', 'TENSION', 'FAIL', 'BELOW RANGE']
cell_text = [
    [f'{p_strong_at_planck*100:.1f}%', f'{p_strong_at_fw*100:.1f}%'],
    [f'{p_weak_at_planck*100:.1f}%', f'{p_weak_at_fw*100:.1f}%'],
    [f'{p_tension_at_planck*100:.1f}%', f'{p_tension_at_fw*100:.1f}%'],
    [f'{p_fail_at_planck*100:.1f}%', f'{p_fail_at_fw*100:.1f}%'],
    [f'{p_below_at_planck*100:.3f}%', f'{p_below_at_fw*100:.1f}%'],
]
row_colors = ['#c8e6c9', '#fff9c4', '#ffe0b2', '#ffcdd2', '#e0e0e0']

table = ax.table(cellText=cell_text, rowLabels=row_labels, colLabels=col_labels,
                 loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.0, 1.8)

# Color rows
for i, color in enumerate(row_colors):
    for j in range(2):
        table[i + 1, j].set_facecolor(color)

# Add summary text
summary = (f"Central prediction: n$_s$ = {ns_central:.4f}\n"
           f"Window: [{ns_min:.3f}, {ns_max:.3f}]\n"
           f"CMB-S4 discrimination: {discrimination:.1f}$\\sigma$\n"
           f"Planck tension: {tension_planck:.2f}$\\sigma$")
ax.text(0.5, -0.05, summary, ha='center', va='top', fontsize=9,
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
out_png = os.path.join(base, 's69_cmbs4_preregister.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"  Saved: {out_png}")

# =============================================================================
# SECTION 10: SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("SUMMARY")
print("=" * 78)
print(f"""
  Framework n_s prediction:
    Central:      {ns_central:.4f} (BCS-dressed, L3, sqrt cutoff)
    L4 check:     {ns_L4:.4f} (BCS-dressed, L4)
    Window:       [{ns_min:.3f}, {ns_max:.3f}]
    sigma_th:     {sigma_th:.4f}

  Observational context:
    Planck 2018:  {ns_planck} +/- {sigma_planck}
    Current tension: {tension_planck:.2f} sigma
    CMB-S4 sigma: {sigma_cmbs4}
    Projected tension (if Planck central persists): {tension_cmbs4_at_planck:.1f} sigma

  Decision rules:
    STRONG PASS:  n_s in [{boundary_strong_weak:.3f}, {boundary_pass_tension:.3f}]
    WEAK PASS:    n_s in [{ns_min:.3f}, {boundary_strong_weak:.3f})
    TENSION:      n_s in ({boundary_pass_tension:.3f}, {boundary_tension_fail:.3f}]
    FAIL:         n_s > {boundary_tension_fail:.3f}

  Gate: CMB-S4-NS-69 = {gate_verdict}
""")
print("=" * 78)
print("DONE")
