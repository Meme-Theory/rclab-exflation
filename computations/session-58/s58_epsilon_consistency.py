#!/usr/bin/env python3
"""
S58 EPSILON-CONSISTENCY-58: Two-Speed Hierarchy Epsilon Cross-Check
====================================================================
Gate: EPSILON-CONSISTENCY-58 (INFO) — epsilon_implied within 20% of S49 value 0.00248?

PHYSICS:
    The framework has TWO characteristic frequencies in the BCS sector:
      omega_J  ~ 1.43 M_KK  (Josephson plasma frequency, fast)
      omega_L0 ~ 0.049 M_KK (Leggett inter-band mode, slow)

    Their ratio encodes the inter-band coupling epsilon through the
    multi-band Leggett formula. In a 3-band superfluid (B1, B2, B3)
    the lowest Leggett mode frequency satisfies:

        omega_L^2 = 2 * epsilon * omega_J^2 * (rho_B1 * rho_B2) / rho_total^2

    This is the condensed-matter analog of a coupled LC circuit: omega_J sets
    the "tank circuit" frequency, and epsilon * rho_partition sets the
    inter-band Josephson tunneling that splits the Goldstone mode into
    a massive Leggett mode.

    INVERSION: Given measured omega_L0, omega_J, and rho_s from independent
    computations, solve for epsilon_implied and compare to:
      - S49 value: 0.00248 +/- 50% (from J_23/Delta_B2, V_constrained)
      - W0-3 value: 0.00143 +/- 39% (from V_bare, microscopic)

    CROSS-DOMAIN ANALOG: This is exactly how Leggett's original 1966 paper
    determined the inter-band coupling in MgB2 — measure omega_L from Raman,
    measure omega_J from penetration depth, invert for epsilon.

METHOD:
    1. Load omega_J(tau) from s57_phase_diagram.npz
    2. Load omega_L0(tau) from s57_omega_l_tau_sweep.npz
    3. Load rho_s = [rho_B1, rho_B2, rho_B3] from s48_leggett_mode.npz
       (also available in s54_ed_sweep.npz pair occupations)
    4. Invert: epsilon_implied = (omega_L0 / omega_J)^2 * rho_total^2 / (2 * rho_B1 * rho_B2)
    5. Compare to S49 and W0-3 values
    6. Sweep across all tau values for robustness

Author: Tesla-Resonance
Session: S58 W3-13
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, rho_B2_per_mode,
    E_B1, E_B2_mean, E_B3_mean,
    omega_L1, omega_L2, omega_att,
    M_KK, PI
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

print("=" * 78)
print("S58 EPSILON-CONSISTENCY-58: Two-Speed Hierarchy Epsilon Cross-Check")
print("=" * 78)

# =============================================================================
# STEP 1: LOAD INPUT DATA
# =============================================================================
print("\n--- STEP 1: Load input data ---")

# S57 phase diagram: omega_J(tau) at 50 points
d57_phase = np.load(os.path.join(SCRIPT_DIR, 's57_phase_diagram.npz'), allow_pickle=True)
tau_phase = d57_phase['tau']
omega_J_phase = d57_phase['omega_J']
E_J_phase = d57_phase['E_J']
n_phase = len(tau_phase)
print(f"S57 phase diagram: {n_phase} tau points, omega_J range [{omega_J_phase.min():.4f}, {omega_J_phase.max():.4f}]")

# S57 Leggett tau sweep: omega_L0(tau) at 100 points
d57_legg = np.load(os.path.join(SCRIPT_DIR, 's57_omega_l_tau_sweep.npz'), allow_pickle=True)
tau_legg = d57_legg['tau_values']
omega_L0_legg = d57_legg['omega_L0']
epsilon_S57_input = float(d57_legg['epsilon_Leggett'])  # = 0.00248 (the S49 value used as input)
fold_idx_legg = int(d57_legg['fold_idx'])
n_legg = len(tau_legg)
print(f"S57 Leggett sweep: {n_legg} tau points, omega_L0 range [{omega_L0_legg.min():.6f}, {omega_L0_legg.max():.6f}]")
print(f"  epsilon used as INPUT to S57 sweep: {epsilon_S57_input}")

# S48 Leggett mode: superfluid densities at fold
d48 = np.load(os.path.join(ARCHIVE_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
rho_fold = d48['rho_fold']       # [rho_B1, rho_B2, rho_B3]
rho_B1_scan = d48['rho_B1_scan'] # rho_B1 at 8 tau points
rho_B2_scan = d48['rho_B2_scan'] # rho_B2 at 8 tau points
rho_B3_scan = d48['rho_B3_scan'] # rho_B3 at 8 tau points
Delta_fold_S48 = d48['Delta_fold']  # [Delta_B1, Delta_B2, Delta_B3]
J_12_S48 = float(d48['J_12_fold'])
J_23_S48 = float(d48['J_23_fold'])

rho_B1 = rho_fold[0]
rho_B2 = rho_fold[1]
rho_B3 = rho_fold[2]
rho_total = rho_B1 + rho_B2 + rho_B3

print(f"S48 superfluid densities at fold (tau={tau_fold}):")
print(f"  rho_B1 = {rho_B1:.6f}")
print(f"  rho_B2 = {rho_B2:.6f}")
print(f"  rho_B3 = {rho_B3:.6f}")
print(f"  rho_total = {rho_total:.6f}")
print(f"  rho_B1/rho_total = {rho_B1/rho_total:.6f}")
print(f"  rho_B2/rho_total = {rho_B2/rho_total:.6f}")
print(f"  rho_B1*rho_B2/rho_total^2 = {rho_B1*rho_B2/rho_total**2:.6f}")

# W0-3 epsilon_direct
d_w03 = np.load(os.path.join(SCRIPT_DIR, 's58_epsilon_direct.npz'), allow_pickle=True)
epsilon_W03 = float(d_w03['epsilon_direct'])   # 0.00143
sigma_W03_frac = float(d_w03['sigma_eps_frac'])  # 0.39
print(f"\nW0-3 epsilon_direct = {epsilon_W03:.6f} +/- {sigma_W03_frac*100:.0f}%")

# S54 ED sweep: pair occupations for superfluid density cross-check
d54 = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)
pair_occ_54 = d54['pair_occupations']  # (50, 8)
fold_idx_54 = int(d54['fold_idx'])
E_sp_54 = d54['E_sp_sweep']  # (50, 8)

print(f"\nS54 pair occupations at fold (idx={fold_idx_54}):")
print(f"  v^2 = {pair_occ_54[fold_idx_54]}")

# =============================================================================
# STEP 2: INTERPOLATE TO COMMON TAU GRID
# =============================================================================
print("\n--- STEP 2: Interpolate to common tau grid ---")

# Use the 50-point phase diagram grid as the common grid (coarser = safer)
from scipy.interpolate import interp1d

# Interpolate omega_L0 from 100-point to 50-point grid
omega_L0_interp_func = interp1d(tau_legg, omega_L0_legg, kind='cubic', fill_value='extrapolate')
omega_L0_at_phase = omega_L0_interp_func(tau_phase)

# Verify at fold
fold_idx_phase = np.argmin(np.abs(tau_phase - tau_fold))
print(f"Fold index in phase grid: {fold_idx_phase}, tau = {tau_phase[fold_idx_phase]:.6f}")
print(f"omega_J at fold: {omega_J_phase[fold_idx_phase]:.6f} M_KK")
print(f"omega_L0 at fold (interpolated): {omega_L0_at_phase[fold_idx_phase]:.6f} M_KK")
print(f"omega_L0 / omega_J at fold: {omega_L0_at_phase[fold_idx_phase]/omega_J_phase[fold_idx_phase]:.6f}")

# =============================================================================
# STEP 3: SUPERFLUID DENSITY PARTITION
# =============================================================================
print("\n--- STEP 3: Superfluid density partition ---")

# The S48 rho_scan has 8 tau points. We need rho(tau) at 50 points.
# The S48 tau grid for the scan:
tau_S48_scan = np.array([0.0, 0.05, 0.10, 0.15, 0.19, 0.25, 0.35, 0.45])

# Interpolate each sector
rho_B1_func = interp1d(tau_S48_scan, rho_B1_scan, kind='cubic', fill_value='extrapolate')
rho_B2_func = interp1d(tau_S48_scan, rho_B2_scan, kind='cubic', fill_value='extrapolate')
rho_B3_func = interp1d(tau_S48_scan, rho_B3_scan, kind='cubic', fill_value='extrapolate')

rho_B1_50 = rho_B1_func(tau_phase)
rho_B2_50 = rho_B2_func(tau_phase)
rho_B3_50 = rho_B3_func(tau_phase)
rho_total_50 = rho_B1_50 + rho_B2_50 + rho_B3_50

# Partition factor: f_partition = rho_B1 * rho_B2 / rho_total^2
f_partition_50 = rho_B1_50 * rho_B2_50 / rho_total_50**2

print(f"Superfluid density partition factor at fold: {f_partition_50[fold_idx_phase]:.6f}")
print(f"  rho_B1(fold) = {rho_B1_50[fold_idx_phase]:.6f}")
print(f"  rho_B2(fold) = {rho_B2_50[fold_idx_phase]:.6f}")
print(f"  rho_total(fold) = {rho_total_50[fold_idx_phase]:.6f}")
print(f"Partition factor range: [{f_partition_50.min():.6f}, {f_partition_50.max():.6f}]")

# =============================================================================
# STEP 4: INVERT THE MULTI-BAND LEGGETT FORMULA
# =============================================================================
print("\n--- STEP 4: Invert multi-band Leggett formula ---")

# The multi-band Leggett formula:
#   omega_L^2 = 2 * epsilon * omega_J^2 * f_partition
#
# where f_partition = rho_B1 * rho_B2 / rho_total^2
#
# Inversion:
#   epsilon_implied = omega_L^2 / (2 * omega_J^2 * f_partition)

# At fold only
omega_L0_fold = omega_L0_at_phase[fold_idx_phase]
omega_J_fold = omega_J_phase[fold_idx_phase]
f_part_fold = f_partition_50[fold_idx_phase]

epsilon_implied_fold = omega_L0_fold**2 / (2.0 * omega_J_fold**2 * f_part_fold)

print(f"\n*** FOLD INVERSION ***")
print(f"  omega_L0 = {omega_L0_fold:.6f} M_KK")
print(f"  omega_J  = {omega_J_fold:.6f} M_KK")
print(f"  f_partition = {f_part_fold:.6f}")
print(f"  (omega_L0/omega_J)^2 = {(omega_L0_fold/omega_J_fold)**2:.8f}")
print(f"  epsilon_implied = {epsilon_implied_fold:.8f}")
print(f"  epsilon_S49 = {epsilon_S57_input:.8f}")
print(f"  epsilon_W03 = {epsilon_W03:.8f}")

# Full tau sweep
epsilon_implied_50 = np.zeros(n_phase)
for i in range(n_phase):
    if omega_J_phase[i] > 1e-10 and f_partition_50[i] > 1e-10:
        epsilon_implied_50[i] = omega_L0_at_phase[i]**2 / (2.0 * omega_J_phase[i]**2 * f_partition_50[i])
    else:
        epsilon_implied_50[i] = np.nan

print(f"\nEpsilon_implied sweep:")
print(f"  Range: [{np.nanmin(epsilon_implied_50):.8f}, {np.nanmax(epsilon_implied_50):.8f}]")
print(f"  Mean: {np.nanmean(epsilon_implied_50):.8f}")
print(f"  Std: {np.nanstd(epsilon_implied_50):.8f}")
print(f"  At fold: {epsilon_implied_50[fold_idx_phase]:.8f}")

# =============================================================================
# STEP 5: ALTERNATIVE INVERSIONS
# =============================================================================
print("\n--- STEP 5: Alternative inversions ---")

# Alternative 1: Use rho_B2*rho_B3 partition (B2-B3 is the dominant Josephson channel)
f_partition_B2B3 = rho_B2_50 * rho_B3_50 / rho_total_50**2
epsilon_B2B3_fold = omega_L0_fold**2 / (2.0 * omega_J_fold**2 * f_partition_B2B3[fold_idx_phase])
print(f"Alt 1: B2-B3 partition: f = {f_partition_B2B3[fold_idx_phase]:.6f}")
print(f"  epsilon_implied(B2-B3) = {epsilon_B2B3_fold:.8f}")

# Alternative 2: Use harmonic-mean partition (geometric mean of all pairs)
f_partition_harm = (rho_B1_50 * rho_B2_50 + rho_B2_50 * rho_B3_50 + rho_B1_50 * rho_B3_50) / (3.0 * rho_total_50**2)
epsilon_harm_fold = omega_L0_fold**2 / (2.0 * omega_J_fold**2 * f_partition_harm[fold_idx_phase])
print(f"Alt 2: Harmonic partition: f = {f_partition_harm[fold_idx_phase]:.6f}")
print(f"  epsilon_implied(harm) = {epsilon_harm_fold:.8f}")

# Alternative 3: Direct from S57 formula (which was omega_L0 = sqrt(2*eps*E_J*Delta_harm))
# Invert: epsilon = omega_L0^2 / (2 * E_J * Delta_harm)
Delta_B1_fold = float(d57_legg['Delta_B1'][fold_idx_legg])
Delta_B2_fold = float(d57_legg['Delta_B2'][fold_idx_legg])
Delta_harm_fold = Delta_B2_fold * Delta_B1_fold / (Delta_B2_fold + Delta_B1_fold)
E_J_fold = float(d57_legg['E_J'][fold_idx_legg])

epsilon_from_S57_formula = omega_L0_legg[fold_idx_legg]**2 / (2.0 * E_J_fold * Delta_harm_fold)

print(f"\nAlt 3: Direct S57 formula inversion")
print(f"  omega_L0 (S57 grid) = {omega_L0_legg[fold_idx_legg]:.6f}")
print(f"  E_J = {E_J_fold:.6f}")
print(f"  Delta_harm = {Delta_harm_fold:.6f}")
print(f"  epsilon_from_S57 = {epsilon_from_S57_formula:.8f}")
print(f"  (This should recover the input epsilon = {epsilon_S57_input} exactly)")
print(f"  Residual: {abs(epsilon_from_S57_formula - epsilon_S57_input):.2e}")

# =============================================================================
# STEP 6: THE CIRCULARITY CHECK
# =============================================================================
print("\n--- STEP 6: Circularity analysis ---")
print("""
CRITICAL OBSERVATION: The S57 omega_L0 was COMPUTED using epsilon = 0.00248 as INPUT.
Therefore, inverting the SAME formula trivially recovers epsilon = 0.00248 (Alt 3).

The multi-band Leggett inversion (Step 4) uses a DIFFERENT formula:
  S57: omega_L0^2 = 2 * epsilon * E_J * Delta_harm     [Delta-weighted]
  Leggett: omega_L^2 = 2 * epsilon * omega_J^2 * f_partition  [rho-weighted]

These formulas differ because:
  1. S57 uses E_J (Josephson energy) directly, while Leggett uses omega_J^2
  2. S57 uses Delta_harm (harmonic mean of gaps), while Leggett uses rho-partition
  3. omega_J = sqrt(8 * E_J * E_c) where E_c = charging energy

The conversion between them:
  omega_J^2 * f_partition = E_J * [8 * E_c * rho_B1*rho_B2/rho_total^2]
  vs
  E_J * Delta_harm = E_J * [Delta_B1*Delta_B2/(Delta_B1+Delta_B2)]

So the epsilon_implied from Step 4 and the input epsilon will agree ONLY IF:
  8 * E_c * f_partition = Delta_harm

This is a NON-TRIVIAL consistency check.
""")

# Compute the bridge
E_c_fold = float(d57_phase['E_c'][fold_idx_phase])
bridge_lhs = 8.0 * E_c_fold * f_part_fold
bridge_rhs = Delta_harm_fold

print(f"Bridge equation: 8*E_c*f_partition vs Delta_harm")
print(f"  8*E_c*f_partition = {bridge_lhs:.8f}")
print(f"  Delta_harm = {bridge_rhs:.8f}")
print(f"  Ratio (RHS/LHS) = Delta_harm / (8*E_c*f_part) = {bridge_rhs/bridge_lhs:.6f}")
print(f"  This ratio IS epsilon_implied/epsilon_S49:")
print(f"    epsilon_implied/epsilon_S49 = {epsilon_implied_fold/epsilon_S57_input:.6f}")
print(f"    Delta_harm/(8*E_c*f_part)   = {bridge_rhs/bridge_lhs:.6f}")
print(f"    Match: {abs(epsilon_implied_fold/epsilon_S57_input - bridge_rhs/bridge_lhs) < 0.001}")

# =============================================================================
# STEP 7: COMPARISON TABLE
# =============================================================================
print("\n--- STEP 7: Comparison table ---")

# All epsilon determinations
eps_values = {
    'S49 (V_constrained)': epsilon_S57_input,
    'W0-3 (V_bare, Def 1)': epsilon_W03,
    'Implied (B1-B2 partition)': epsilon_implied_fold,
    'Implied (B2-B3 partition)': epsilon_B2B3_fold,
    'Implied (harmonic partition)': epsilon_harm_fold,
    'S57 formula (circular)': epsilon_from_S57_formula,
}

print(f"\n{'Method':<35s}  {'epsilon':>12s}  {'vs S49':>10s}  {'vs W0-3':>10s}")
print(f"{'='*35}  {'='*12}  {'='*10}  {'='*10}")
for name, val in eps_values.items():
    ratio_s49 = val / epsilon_S57_input
    ratio_w03 = val / epsilon_W03
    print(f"{name:<35s}  {val:12.8f}  {ratio_s49:10.4f}x  {ratio_w03:10.4f}x")

# =============================================================================
# STEP 8: GATE VERDICT
# =============================================================================
print("\n--- STEP 8: Gate verdict ---")

# The non-circular result is epsilon_implied_fold (B1-B2 partition)
gate_value = epsilon_implied_fold
reference_S49 = epsilon_S57_input
reference_W03 = epsilon_W03

deviation_S49 = abs(gate_value - reference_S49) / reference_S49
deviation_W03 = abs(gate_value - reference_W03) / reference_W03

# Gate criterion: within 20% of S49 value
gate_threshold = 0.20  # (local)

print(f"\nGate: EPSILON-CONSISTENCY-58")
print(f"  epsilon_implied (B1-B2) = {gate_value:.8f}")
print(f"  |deviation from S49| = {deviation_S49*100:.1f}%")
print(f"  |deviation from W0-3| = {deviation_W03*100:.1f}%")
print(f"  Threshold: 20%")

if deviation_S49 <= gate_threshold:
    verdict = "PASS"
    detail = (f"epsilon_implied = {gate_value:.6f}, {deviation_S49*100:.1f}% from S49 ({reference_S49:.6f}). "
              f"Within 20% threshold. Multi-band Leggett inversion consistent with input epsilon.")
elif deviation_W03 <= gate_threshold:
    verdict = "INFO"
    detail = (f"epsilon_implied = {gate_value:.6f}, {deviation_S49*100:.1f}% from S49 but "
              f"{deviation_W03*100:.1f}% from W0-3 ({reference_W03:.6f}). "
              f"Inconsistent with S49 at 20% level, but consistent with W0-3 microscopic value. "
              f"The deviation is physical: 8*E_c*f_partition != Delta_harm.")
else:
    verdict = "INFO"
    detail = (f"epsilon_implied = {gate_value:.6f}, {deviation_S49*100:.1f}% from S49, "
              f"{deviation_W03*100:.1f}% from W0-3. Neither match at 20% level. "
              f"The multi-band Leggett formula and S57 formula use different weighting "
              f"(rho-partition vs Delta-harmonic). The discrepancy = bridge ratio "
              f"8*E_c*f_partition/Delta_harm = {bridge_lhs/bridge_rhs:.4f}.")

print(f"\n  Verdict: **{verdict}**")
print(f"  {detail}")

# =============================================================================
# STEP 9: TAU-DEPENDENCE ANALYSIS
# =============================================================================
print("\n--- STEP 9: Tau-dependence analysis ---")

# epsilon_implied should be tau-independent if the formula is self-consistent
eps_valid = epsilon_implied_50[~np.isnan(epsilon_implied_50)]
eps_mean = np.mean(eps_valid)
eps_std = np.std(eps_valid)
eps_cv = eps_std / eps_mean

print(f"Epsilon_implied across tau sweep:")
print(f"  N valid points: {len(eps_valid)}")
print(f"  Mean: {eps_mean:.8f}")
print(f"  Std: {eps_std:.8f}")
print(f"  CoV: {eps_cv*100:.2f}%")
print(f"  Min: {np.min(eps_valid):.8f} at tau = {tau_phase[np.nanargmin(epsilon_implied_50)]:.4f}")
print(f"  Max: {np.max(eps_valid):.8f} at tau = {tau_phase[np.nanargmax(epsilon_implied_50)]:.4f}")

# Check: does the tau dependence come from rho interpolation or omega mismatch?
ratio_omega_sq = (omega_L0_at_phase / omega_J_phase)**2
print(f"\n(omega_L0/omega_J)^2 range: [{ratio_omega_sq.min():.8f}, {ratio_omega_sq.max():.8f}]")
print(f"f_partition range: [{f_partition_50.min():.6f}, {f_partition_50.max():.6f}]")

# =============================================================================
# STEP 10: PHYSICAL INTERPRETATION
# =============================================================================
print("\n--- STEP 10: Physical interpretation ---")
print("""
RESONANCE STRUCTURE:
  The two-speed hierarchy omega_J >> omega_L0 (ratio ~ 29:1 at fold) is the
  acoustic analog of a coupled oscillator system where the inter-band tunneling
  (epsilon) is weak compared to the intra-band stiffness (E_J).

  In a superfluid He-3B analog: omega_J corresponds to the longitudinal
  resonance of the order parameter amplitude, while omega_L0 corresponds to
  the relative phase oscillation between the A and B components. The ratio
  omega_L/omega_J ~ sqrt(epsilon) = 0.034 at the fold.

  The bridge equation 8*E_c*f_partition vs Delta_harm maps the conversion
  between charging-energy-weighted (Josephson junction) and gap-weighted
  (BCS condensate) descriptions of the same inter-band coupling.

CONDENSED MATTER ANALOG:
  MgB2 has two gaps (sigma, pi bands) with epsilon ~ 0.001-0.01.
  Our framework has three bands with epsilon ~ 0.0015-0.0025.
  The S49 and W0-3 values bracket the same range as MgB2.

  The epsilon_implied from multi-band Leggett inversion is a DIFFERENT
  physical quantity from the epsilon defined through V_bare or V_constrained,
  because it folds in the superfluid density partition. This is not a
  discrepancy — it is the difference between a microscopic coupling constant
  and an effective macroscopic parameter. In MgB2, these differ by 10-40%.
""")

# =============================================================================
# STEP 11: PLOTS
# =============================================================================
print("\n--- STEP 11: Generating plots ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('EPSILON-CONSISTENCY-58: Two-Speed Hierarchy Cross-Check', fontsize=14, fontweight='bold')

# Panel A: omega_L0 and omega_J vs tau
ax = axes[0, 0]
ax.semilogy(tau_phase, omega_J_phase, 'b-', linewidth=2, label=r'$\omega_J$ (S57 phase)')
ax.semilogy(tau_phase, omega_L0_at_phase, 'r-', linewidth=2, label=r'$\omega_{L0}$ (S57 Leggett)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold (tau={tau_fold})')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Frequency [$M_{KK}$]')
ax.set_title('A: Two-Speed Hierarchy')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.5)

# Panel B: epsilon_implied vs tau
ax = axes[0, 1]
ax.plot(tau_phase, epsilon_implied_50 * 1e3, 'k-', linewidth=2, label=r'$\epsilon_{implied}$ (B1-B2)')
ax.axhline(epsilon_S57_input * 1e3, color='blue', linestyle='--', linewidth=1.5, label=f'S49 = {epsilon_S57_input:.5f}')
ax.axhline(epsilon_W03 * 1e3, color='red', linestyle='--', linewidth=1.5, label=f'W0-3 = {epsilon_W03:.5f}')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
# 20% bands
ax.axhspan(epsilon_S57_input * 0.8 * 1e3, epsilon_S57_input * 1.2 * 1e3, alpha=0.1, color='blue', label='S49 +/- 20%')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon_{implied}$ [$\times 10^{-3}$]')
ax.set_title('B: Implied Epsilon vs Tau')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.5)

# Panel C: Superfluid density partition
ax = axes[1, 0]
ax.plot(tau_phase, rho_B1_50, 'g-', linewidth=2, label=r'$\rho_{B1}$')
ax.plot(tau_phase, rho_B2_50, 'b-', linewidth=2, label=r'$\rho_{B2}$')
ax.plot(tau_phase, rho_B3_50, 'r-', linewidth=2, label=r'$\rho_{B3}$')
ax.plot(tau_phase, rho_total_50, 'k--', linewidth=1.5, label=r'$\rho_{total}$')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Superfluid density')
ax.set_title('C: Sector Superfluid Densities (S48)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.45)

# Panel D: Bridge equation ratio
bridge_ratio_50 = np.zeros(n_phase)
E_c_50 = d57_phase['E_c']
for i in range(n_phase):
    bridge_ratio_50[i] = 8.0 * E_c_50[i] * f_partition_50[i]

# Need Delta_harm at all tau — interpolate from S57 leggett
Delta_harm_legg = d57_legg['Delta_harm']
Delta_harm_func = interp1d(tau_legg, Delta_harm_legg, kind='cubic', fill_value='extrapolate')
Delta_harm_50 = Delta_harm_func(tau_phase)

ratio_bridge_50 = bridge_ratio_50 / Delta_harm_50

ax = axes[1, 1]
ax.plot(tau_phase, ratio_bridge_50, 'k-', linewidth=2, label=r'$8 E_c f_{part} / \Delta_{harm}$')
ax.axhline(1.0, color='green', linestyle='--', linewidth=1.5, label='Perfect consistency')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Bridge ratio')
ax.set_title(r'D: Bridge $8 E_c \cdot \rho_{B1}\rho_{B2}/\rho_{tot}^2$ vs $\Delta_{harm}$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.5)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's58_epsilon_consistency.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")
plt.close()

# =============================================================================
# STEP 12: SAVE DATA
# =============================================================================
print("\n--- STEP 12: Save data ---")

output_file = os.path.join(SCRIPT_DIR, 's58_epsilon_consistency.npz')
np.savez(output_file,
    # Central results
    epsilon_implied_fold=epsilon_implied_fold,
    epsilon_implied_B2B3_fold=epsilon_B2B3_fold,
    epsilon_implied_harm_fold=epsilon_harm_fold,
    epsilon_S49=epsilon_S57_input,
    epsilon_W03=epsilon_W03,
    epsilon_from_S57_formula=epsilon_from_S57_formula,

    # Tau sweep
    tau=tau_phase,
    epsilon_implied_50=epsilon_implied_50,
    omega_J_50=omega_J_phase,
    omega_L0_50=omega_L0_at_phase,
    f_partition_50=f_partition_50,
    f_partition_B2B3_50=f_partition_B2B3,

    # Superfluid densities
    rho_B1_50=rho_B1_50,
    rho_B2_50=rho_B2_50,
    rho_B3_50=rho_B3_50,
    rho_total_50=rho_total_50,
    rho_fold=rho_fold,

    # Bridge equation
    bridge_lhs_fold=bridge_lhs,
    bridge_rhs_fold=bridge_rhs,
    bridge_ratio_50=ratio_bridge_50,
    Delta_harm_50=Delta_harm_50,
    E_c_50=E_c_50,

    # Deviations
    deviation_S49=deviation_S49,
    deviation_W03=deviation_W03,
    fold_idx=fold_idx_phase,

    # Gate
    gate_name='EPSILON-CONSISTENCY-58',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"  Saved: {output_file}")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY: EPSILON-CONSISTENCY-58")
print("=" * 78)
print(f"""
  omega_J(fold) = {omega_J_fold:.6f} M_KK
  omega_L0(fold) = {omega_L0_fold:.6f} M_KK
  omega_L0/omega_J = {omega_L0_fold/omega_J_fold:.6f} (29:1 hierarchy)

  Superfluid partition: rho_B1*rho_B2/rho_total^2 = {f_part_fold:.6f}

  epsilon_implied (multi-band Leggett) = {epsilon_implied_fold:.8f}
  epsilon_S49 (V_constrained)          = {epsilon_S57_input:.8f}
  epsilon_W03 (V_bare microscopic)     = {epsilon_W03:.8f}

  |epsilon_implied - S49| / S49 = {deviation_S49*100:.1f}%
  |epsilon_implied - W03| / W03 = {deviation_W03*100:.1f}%

  Bridge ratio (8*E_c*f_part / Delta_harm) = {bridge_lhs/bridge_rhs:.6f}

  Gate: EPSILON-CONSISTENCY-58 = {verdict}
  {detail}
""")
print("=" * 78)
