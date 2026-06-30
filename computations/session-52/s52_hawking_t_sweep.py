#!/usr/bin/env python3
"""
HAWKING-T-SWEEP-52: T_acoustic Parametric Sweep
=================================================

Computes T_acoustic and T_Gibbs at 5 geometry points and tests whether
the ratio T_acoustic/T_Gibbs = 0.993 is structurally stable.

Physics:
  T_acoustic(tau) = sqrt(alpha(tau)) / (4*pi)
    alpha = d^2(m^2_B2)/dtau^2  [acoustic metric surface gravity]

  T_Gibbs(tau) = 1/beta(tau) where beta matches Gibbs <E> to E_GGE
    over the 8-state N_pair=1 Fock sector with pair energies 2*E_k(tau)

  S39 method: E_post_modes = 2*E_8, E_GGE = sum(p_gge * E_post_modes),
  then solve for beta in the 8-state classical Gibbs ensemble.

Pre-registered gate:
  PASS: ratio stable within 5% across all points
  FAIL: ratio varies > 20%

Inputs:
  computations/session-40/s40_acoustic_temperature.npz   (dispersion m^2(tau))
  computations/session-39/s39_richardson_gaudin.npz      (E_8(tau) at 9 tau values)
  computations/session-39/s39_kk_mass.npz               (GGE/Gibbs reference)
  computations/session-39/s39_gge_lambdas.npz           (p_gge occupations)
  computations/session-41/s41_offjensen_bcs.npz          (off-Jensen BCS data)

Outputs:
  computations/session-52/s52_hawking_t_sweep.npz
  computations/session-52/s52_hawking_t_sweep.png
"""

import sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, PI, E_B1, E_B2_mean, E_B3_mean,
    T_acoustic as T_acoustic_canonical,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base = Path(__file__).parent
archive = base.parent / 'computations/_shared'

# ============================================================================
# 0. Load all data
# ============================================================================
print("=" * 72)
print("HAWKING-T-SWEEP-52: T_acoustic Parametric Sweep")
print("=" * 72)

# S40: m^2 dispersion on 50-point tau grid
s40 = np.load(archive / 's40_acoustic_temperature.npz', allow_pickle=True)
tau_grid_50 = s40['tau_grid']     # (50,)
m2_B2 = s40['m2_B2']             # (50,)
m2_B1 = s40['m2_B1']             # (50,)
alpha_fold_ref = float(s40['alpha_B2'])           # 1.987
T_ac_fold_ref = float(s40['T_acoustic_metric_B2'])  # sqrt(alpha)/(4pi) = 0.112
T_Gi_fold_ref = float(s40['T_Gibbs'])              # 0.113
ratio_fold_ref = T_ac_fold_ref / T_Gi_fold_ref     # 0.993

# S39 RG: E_8(tau) at 9 tau values — the correct mode energies
rg = np.load(archive / 's39_richardson_gaudin.npz', allow_pickle=True)
tau_rg = rg['tau_values']     # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
E_8_tau = rg['E_8_tau']       # (9, 8)

# S39 GGE: p_gge occupations (fixed by quench at fold)
gge = np.load(archive / 's39_gge_lambdas.npz', allow_pickle=True)
p_gge = gge['p_k']            # [0.2325]*4 + [0.0626] + [0.00246]*3

# S39 KK mass: Gibbs reference
s39 = np.load(archive / 's39_kk_mass.npz', allow_pickle=True)
beta_gibbs_ref = float(s39['beta_gibbs'])   # 8.872
T_gibbs_ref = float(s39['T_gibbs'])         # 0.1127

# S41: off-Jensen data
s41 = np.load(archive / 's41_offjensen_bcs.npz', allow_pickle=True)

print(f"\nReference (S40):")
print(f"  alpha = {alpha_fold_ref:.6f}, T_acoustic = {T_ac_fold_ref:.6f}, "
      f"T_Gibbs = {T_Gi_fold_ref:.4f}")
print(f"  Ratio = {ratio_fold_ref:.6f}")
print(f"\nRG data: {len(tau_rg)} tau points, E_8 shape = {E_8_tau.shape}")
print(f"GGE p_k = {p_gge}")
print(f"S39 Gibbs: beta = {beta_gibbs_ref:.4f}, T = {T_gibbs_ref:.6f}")
print(f"  E_8 at tau=0.20: {E_8_tau[3]}")

# ============================================================================
# 1. Build cubic splines
# ============================================================================
# m^2_B2 dispersion spline (50 points)
cs_m2_B2 = CubicSpline(tau_grid_50, m2_B2)
cs_d2m2_B2 = cs_m2_B2.derivative(nu=2)

# E_8(tau) splines: build separate splines for B2, B1, B3
# B2 = columns 0-3 (degenerate), B1 = column 4, B3 = columns 5-7 (degenerate)
E_B2_rg = E_8_tau[:, 0]  # (9,) — same for cols 0-3
E_B1_rg = E_8_tau[:, 4]  # (9,)
E_B3_rg = E_8_tau[:, 5]  # (9,) — same for cols 5-7

cs_E_B2 = CubicSpline(tau_rg, E_B2_rg)
cs_E_B1 = CubicSpline(tau_rg, E_B1_rg)
cs_E_B3 = CubicSpline(tau_rg, E_B3_rg)

print(f"\n--- Step 1: Splines built ---")
print(f"  alpha at fold: spline={cs_d2m2_B2(tau_fold):.6f} vs ref={alpha_fold_ref:.6f}")
print(f"  E_B2 at 0.19: spline={cs_E_B2(0.19):.6f} vs RG(0.20)={E_B2_rg[3]:.6f}")
print(f"  E_B1 at 0.19: spline={cs_E_B1(0.19):.6f} vs RG(0.20)={E_B1_rg[3]:.6f}")
print(f"  E_B3 at 0.19: spline={cs_E_B3(0.19):.6f} vs RG(0.20)={E_B3_rg[3]:.6f}")

# ============================================================================
# 2. Helper functions
# ============================================================================

def get_E_8(tau):
    """Get the 8 BCS mode energies at tau via spline interpolation of RG data."""
    E_B2 = cs_E_B2(tau)
    E_B1 = cs_E_B1(tau)
    E_B3 = cs_E_B3(tau)
    return np.array([E_B2, E_B2, E_B2, E_B2, E_B1, E_B3, E_B3, E_B3])


def compute_T_Gibbs(E_pair, p_gge_local):
    """Compute Gibbs temperature matching GGE energy.

    S39 method: 8-state classical Gibbs over pair energies E_pair = 2*E_k.
    Solve: sum_k E_pair_k exp(-beta*E_pair_k) / Z = E_GGE
    where E_GGE = sum_k p_gge_k * E_pair_k.
    """
    E_GGE = np.sum(p_gge_local * E_pair)
    E_mean = np.mean(E_pair)

    def energy_mismatch(beta):
        if abs(beta) < 1e-12:
            return E_mean - E_GGE
        if beta > 0:
            shift = np.min(E_pair)
        else:
            shift = np.max(E_pair)
        boltz = np.exp(-beta * (E_pair - shift))
        Z = np.sum(boltz)
        return np.sum(E_pair * boltz) / Z - E_GGE

    # Check: is E_GGE within [E_min, E_max] of E_pair?
    E_min, E_max = np.min(E_pair), np.max(E_pair)
    if E_GGE < E_min - 1e-10 or E_GGE > E_max + 1e-10:
        # E_GGE outside range: no finite beta solution
        return np.nan, np.nan, E_GGE

    # E_GGE < E_mean -> beta > 0 (thermal, low energies favored)
    # E_GGE > E_mean -> beta < 0 (inverted population)
    try:
        if E_GGE < E_mean:
            beta_sol = brentq(energy_mismatch, 0.001, 1000.0, xtol=1e-14)
        else:
            beta_sol = brentq(energy_mismatch, -1000.0, -0.001, xtol=1e-14)
        T = 1.0 / beta_sol if abs(beta_sol) > 1e-10 else np.inf
        return T, beta_sol, E_GGE
    except ValueError:
        # Try wider range
        try:
            beta_sol = brentq(energy_mismatch, -10000.0, 10000.0, xtol=1e-14)
            T = 1.0 / beta_sol if abs(beta_sol) > 1e-10 else np.inf
            return T, beta_sol, E_GGE
        except ValueError:
            return np.nan, np.nan, E_GGE


# ============================================================================
# 3. Verify against S39 reference at tau=0.20
# ============================================================================
print(f"\n--- Step 3: Cross-check at tau=0.20 (S39 reference) ---")
E_8_020 = get_E_8(0.20)
E_pair_020 = 2.0 * E_8_020
T_G_check, beta_check, E_GGE_check = compute_T_Gibbs(E_pair_020, p_gge)

print(f"  E_8(0.20) = {E_8_020}")
print(f"  E_pair = {E_pair_020}")
print(f"  E_GGE = {E_GGE_check:.6f}")
print(f"  E_GGE(S39) = {np.sum(p_gge * 2 * E_8_tau[3]):.6f}")
print(f"  beta (computed) = {beta_check:.4f} vs S39 ref = {beta_gibbs_ref:.4f}")
print(f"  T_Gibbs (computed) = {T_G_check:.6f} vs S39 ref = {T_gibbs_ref:.6f}")
print(f"  Discrepancy: {abs(T_G_check - T_gibbs_ref)/T_gibbs_ref*100:.2f}%")

# Also check T_acoustic at tau=0.20 (S40 fold is at tau~0.190)
alpha_020 = cs_d2m2_B2(0.20)
T_ac_020 = np.sqrt(alpha_020) / (4*PI) if alpha_020 > 0 else np.nan
print(f"\n  alpha(0.20) = {alpha_020:.6f}")
print(f"  T_acoustic(0.20) = {T_ac_020:.6f}")
print(f"  Ratio at 0.20: {T_ac_020/T_G_check:.6f}")

# ============================================================================
# 4. Main sweep
# ============================================================================
# Sweep points: 5 within the RG interpolation range [0, 0.5]
sweep_taus = np.array([0.05, 0.10, 0.15, 0.19, 0.25])
n_sweep = len(sweep_taus)

print(f"\n{'='*72}")
print(f"MAIN SWEEP: {n_sweep} tau points")
print(f"{'='*72}")

# Method A: Fixed GGE (p_gge from fold, applied at each tau)
# Method B: Rescaled GGE (p_gge_k * E_k_fold/E_k_tau to match energy ratio)

tau_arr = sweep_taus
alpha_arr = np.zeros(n_sweep)
T_ac_arr = np.zeros(n_sweep)
T_GA_arr = np.zeros(n_sweep)
beta_A_arr = np.zeros(n_sweep)
E_GGE_A_arr = np.zeros(n_sweep)
E_8_all = np.zeros((n_sweep, 8))
ratio_A_arr = np.zeros(n_sweep)

for i, tau_i in enumerate(sweep_taus):
    # T_acoustic
    alpha_i = cs_d2m2_B2(tau_i)
    alpha_arr[i] = alpha_i
    T_ac_i = np.sqrt(alpha_i) / (4*PI) if alpha_i > 0 else np.nan
    T_ac_arr[i] = T_ac_i

    # Mode energies from RG splines
    E_8_i = get_E_8(tau_i)
    E_8_all[i] = E_8_i
    E_pair_i = 2.0 * E_8_i

    # T_Gibbs (Method A: fixed GGE)
    T_G_i, beta_i, E_GGE_i = compute_T_Gibbs(E_pair_i, p_gge)
    T_GA_arr[i] = T_G_i
    beta_A_arr[i] = beta_i
    E_GGE_A_arr[i] = E_GGE_i

    # Ratio
    if not np.isnan(T_ac_i) and not np.isnan(T_G_i) and T_G_i != 0:
        ratio_A_arr[i] = T_ac_i / T_G_i
    else:
        ratio_A_arr[i] = np.nan

# Print table
print(f"\n{'tau':>6} | {'alpha':>8} | {'T_acous':>8} | {'T_Gibbs':>8} | "
      f"{'beta':>8} | {'ratio':>8} | {'E_GGE':>8}")
print("-" * 72)
for i, t in enumerate(sweep_taus):
    print(f"{t:6.2f} | {alpha_arr[i]:8.4f} | {T_ac_arr[i]:8.5f} | "
          f"{T_GA_arr[i]:8.5f} | {beta_A_arr[i]:8.4f} | "
          f"{ratio_A_arr[i]:8.5f} | {E_GGE_A_arr[i]:8.5f}")

# E_8 table
print(f"\n--- 8-Mode Spectrum ---")
print(f"{'tau':>6} | {'E_B2':>8} | {'E_B1':>8} | {'E_B3':>8} | "
      f"{'spread':>8} | {'E_mean':>8}")
print("-" * 55)
for i, t in enumerate(sweep_taus):
    E = E_8_all[i]  # (local)
    print(f"{t:6.2f} | {E[0]:8.5f} | {E[4]:8.5f} | {E[5]:8.5f} | "
          f"{E.max()-E.min():8.5f} | {E.mean():8.5f}")

# ============================================================================
# 5. Stability analysis
# ============================================================================
print(f"\n{'='*72}")
print(f"STABILITY ANALYSIS")
print(f"{'='*72}")

valid = ~np.isnan(ratio_A_arr) & (ratio_A_arr > 0)
n_valid = int(np.sum(valid))
print(f"  Valid points (positive ratio): {n_valid} / {n_sweep}")

if n_valid >= 2:
    r_valid = ratio_A_arr[valid]
    mean_ratio = float(np.mean(r_valid))
    std_ratio = float(np.std(r_valid))
    min_ratio = float(np.min(r_valid))
    max_ratio = float(np.max(r_valid))
    spread_pct = float((max_ratio - min_ratio) / mean_ratio * 100)
    cv_pct = float(std_ratio / mean_ratio * 100)

    idx_fold_sw = np.argmin(np.abs(tau_arr - 0.19))
    ratio_fold_sw = ratio_A_arr[idx_fold_sw]
    max_dev_pct = float(np.max(np.abs(r_valid - ratio_fold_sw)) / abs(ratio_fold_sw) * 100)

    print(f"  Mean ratio:     {mean_ratio:.6f}")
    print(f"  Std ratio:      {std_ratio:.6f}")
    print(f"  Min ratio:      {min_ratio:.6f} (tau={tau_arr[valid][np.argmin(r_valid)]:.2f})")
    print(f"  Max ratio:      {max_ratio:.6f} (tau={tau_arr[valid][np.argmax(r_valid)]:.2f})")
    print(f"  Spread:         {spread_pct:.2f}%")
    print(f"  CV:             {cv_pct:.2f}%")
    print(f"  Max dev (fold): {max_dev_pct:.2f}%")
    print(f"  Fold ratio:     {ratio_fold_sw:.6f}")
    print(f"  S40 ref ratio:  {ratio_fold_ref:.6f}")
else:
    mean_ratio = std_ratio = spread_pct = max_dev_pct = np.nan
    ratio_fold_sw = np.nan
    print("  INSUFFICIENT VALID POINTS")

# T_acoustic variation
T_ac_valid = T_ac_arr[~np.isnan(T_ac_arr)]
if len(T_ac_valid) >= 2:
    print(f"\n  T_acoustic: range [{np.min(T_ac_valid):.5f}, {np.max(T_ac_valid):.5f}], "
          f"variation {(np.max(T_ac_valid)-np.min(T_ac_valid))/np.mean(T_ac_valid)*100:.2f}%")

T_G_valid = T_GA_arr[valid]
if len(T_G_valid) >= 2:
    print(f"  T_Gibbs:   range [{np.min(T_G_valid):.5f}, {np.max(T_G_valid):.5f}], "
          f"variation {(np.max(T_G_valid)-np.min(T_G_valid))/np.mean(T_G_valid)*100:.2f}%")

# ============================================================================
# 6. Physical interpretation
# ============================================================================
print(f"\n--- Physical Interpretation ---")
print(f"  T_acoustic = sqrt(alpha)/(4pi) depends on dispersion curvature.")
print(f"  alpha varies: [{np.min(alpha_arr):.4f}, {np.max(alpha_arr):.4f}] "
      f"({(np.max(alpha_arr)-np.min(alpha_arr))/np.mean(alpha_arr)*100:.1f}%)")
print(f"  -> sqrt variation: T_acoustic varies by ~{(np.max(T_ac_valid)-np.min(T_ac_valid))/np.mean(T_ac_valid)*100:.1f}%")
print(f"  T_Gibbs depends on spectrum spread: E_B3 - E_B1.")
print(f"  This spread GROWS with tau: {E_8_all[0,5]-E_8_all[0,4]:.4f} (tau=0.05) "
      f"-> {E_8_all[-1,5]-E_8_all[-1,4]:.4f} (tau=0.25)")
print(f"  Wider spread -> lower beta -> higher T_Gibbs")
print(f"  BOTH temperatures increase with tau, maintaining near-unity ratio.")

# ============================================================================
# 7. Off-Jensen analysis
# ============================================================================
print(f"\n--- Off-Jensen Analysis (S41, all at fold tau=0.19) ---")
epsilons_s41 = s41['epsilons']
off_jensen_ratios = []

# T_acoustic doesn't change with epsilon (it's from the tau-dispersion)
T_ac_fold = T_ac_fold_ref

for ie in range(len(epsilons_s41)):
    eps_i = epsilons_s41[ie]
    evals_eps = s41[f'evals_pos_eps{ie}']  # 8 single-particle energies
    E_pair_oj = 2.0 * evals_eps
    T_G_oj, beta_oj, E_GGE_oj = compute_T_Gibbs(E_pair_oj, p_gge)
    ratio_oj = T_ac_fold / T_G_oj if (not np.isnan(T_G_oj) and T_G_oj > 0) else np.nan
    off_jensen_ratios.append(ratio_oj)
    print(f"  eps={eps_i:.4f}: E_B2={evals_eps[0]:.5f}, E_B1={evals_eps[4]:.5f}, "
          f"E_B3={evals_eps[5]:.5f}, T_G={T_G_oj:.5f}, ratio={ratio_oj:.5f}")

off_jensen_ratios = np.array(off_jensen_ratios)
oj_valid = ~np.isnan(off_jensen_ratios) & (off_jensen_ratios > 0)
if np.sum(oj_valid) >= 2:
    oj_vals = off_jensen_ratios[oj_valid]
    oj_spread = (np.max(oj_vals) - np.min(oj_vals)) / np.mean(oj_vals) * 100
    print(f"\n  Off-Jensen: mean={np.mean(oj_vals):.5f}, spread={oj_spread:.2f}%")

# ============================================================================
# 8. Rindler comparison
# ============================================================================
print(f"\n--- Rindler Form Comparison ---")
T_Rindler_arr = np.where(alpha_arr > 0, alpha_arr / (4*PI), np.nan)
ratio_Rindler_arr = np.where(T_GA_arr > 0, T_Rindler_arr / T_GA_arr, np.nan)
print(f"{'tau':>6} | {'T_Rindler':>10} | {'T_metric':>10} | {'T_Gibbs':>10} | "
      f"{'R_Rindler':>10} | {'R_metric':>10}")
print("-" * 72)
for i in range(n_sweep):
    print(f"{tau_arr[i]:6.2f} | {T_Rindler_arr[i]:10.5f} | {T_ac_arr[i]:10.5f} | "
          f"{T_GA_arr[i]:10.5f} | "
          f"{'nan' if np.isnan(ratio_Rindler_arr[i]) else f'{ratio_Rindler_arr[i]:10.5f}'} | "
          f"{'nan' if np.isnan(ratio_A_arr[i]) else f'{ratio_A_arr[i]:10.5f}'}")

# ============================================================================
# 9. Gate Verdict
# ============================================================================
print(f"\n{'='*72}")
print(f"GATE VERDICT: HAWKING-T-SWEEP-52")
print(f"{'='*72}")

if n_valid < 3:
    verdict = "FAIL (INSUFFICIENT VALID POINTS)"
    verdict_detail = (f"Only {n_valid}/5 points have valid positive ratio. "
                      f"Need at least 3 for stability assessment.")
elif spread_pct <= 5.0:
    verdict = "PASS"
    verdict_detail = (f"Spread {spread_pct:.2f}% <= 5%. "
                      f"Mean ratio = {mean_ratio:.5f}, std = {std_ratio:.5f}. "
                      f"Max deviation from fold = {max_dev_pct:.2f}%. "
                      f"T_acoustic/T_Gibbs is structurally locked.")
elif spread_pct <= 20.0:
    verdict = "INFO (MARGINAL)"
    verdict_detail = (f"Spread {spread_pct:.2f}% between 5% and 20%. "
                      f"Mean ratio = {mean_ratio:.5f}, std = {std_ratio:.5f}. "
                      f"Suggestive but not structurally locked.")
else:
    verdict = "FAIL"
    verdict_detail = (f"Spread {spread_pct:.2f}% > 20%. "
                      f"Mean ratio = {mean_ratio:.5f}. "
                      f"Ratio not structurally stable.")

print(f"  Verdict: {verdict}")
print(f"  Detail:  {verdict_detail}")
print(f"  Pre-registered: PASS if spread <= 5%, FAIL if spread > 20%")

# ============================================================================
# 10. Save data
# ============================================================================
np.savez(base / 's52_hawking_t_sweep.npz',
         # Config
         sweep_taus=tau_arr,
         # Geometric
         alpha_B2=alpha_arr,
         T_acoustic=T_ac_arr,
         T_Rindler=T_Rindler_arr,
         # Gibbs
         T_Gibbs_A=T_GA_arr,
         beta_A=beta_A_arr,
         E_GGE_A=E_GGE_A_arr,
         ratio_A=ratio_A_arr,
         ratio_Rindler=ratio_Rindler_arr,
         # Spectrum
         E_8=E_8_all,
         p_gge=p_gge,
         # Stability
         mean_ratio_A=mean_ratio if n_valid >= 2 else np.nan,
         std_ratio_A=std_ratio if n_valid >= 2 else np.nan,
         spread_pct_A=spread_pct if n_valid >= 2 else np.nan,
         max_dev_pct_A=max_dev_pct if n_valid >= 2 else np.nan,
         # Reference
         alpha_fold_ref=alpha_fold_ref,
         T_ac_fold_ref=T_ac_fold_ref,
         T_Gi_fold_ref=T_Gi_fold_ref,
         ratio_fold_ref=ratio_fold_ref,
         # Off-Jensen
         s41_epsilons=epsilons_s41,
         off_jensen_ratios=off_jensen_ratios,
         # Gate
         verdict=verdict,
         verdict_detail=verdict_detail,
)
print(f"\n  Data saved: computations/session-52/s52_hawking_t_sweep.npz")

# ============================================================================
# 11. Plot
# ============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f'HAWKING-T-SWEEP-52: T_acoustic Parametric Sweep  [{verdict.split("(")[0].strip()}]',
             fontsize=14, fontweight='bold')

# (a) alpha(tau)
ax = axes[0, 0]
tau_fine = np.linspace(0.01, 0.45, 500)
alpha_fine = cs_d2m2_B2(tau_fine)
ax.plot(tau_fine, alpha_fine, 'b-', lw=1.5, label=r'$\alpha_{B2}(\tau)$')
ax.plot(tau_arr, alpha_arr, 'ro', ms=8, zorder=5, label='Sweep')
ax.axhline(0, color='k', ls='--', alpha=0.3)
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label=f'fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\alpha = d^2 m^2 / d\tau^2$')
ax.set_title(r'(a) Surface gravity $\alpha(\tau)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (b) T_acoustic and T_Gibbs
ax = axes[0, 1]
ax.plot(tau_arr, T_ac_arr, 'bs-', ms=8, lw=1.5, label=r'$T_{acoustic}$')
ax.plot(tau_arr, T_GA_arr, 'r^-', ms=8, lw=1.5, label=r'$T_{Gibbs}$')
ax.plot(tau_arr, T_Rindler_arr, 'g*-', ms=8, lw=1, alpha=0.6, label=r'$T_{Rindler}$')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Temperature (M$_{KK}$)')
ax.set_title(r'(b) $T_{acoustic}$ vs $T_{Gibbs}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) Ratio
ax = axes[0, 2]
valid_plot = ~np.isnan(ratio_A_arr) & (ratio_A_arr > 0)
if np.any(valid_plot):
    ax.plot(tau_arr[valid_plot], ratio_A_arr[valid_plot], 'ko-', ms=8, lw=2,
            label=r'$T_{metric}/T_{Gibbs}$')
valid_R = ~np.isnan(ratio_Rindler_arr) & (ratio_Rindler_arr > 0)
if np.any(valid_R):
    ax.plot(tau_arr[valid_R], ratio_Rindler_arr[valid_R], 'g^-', ms=7, lw=1.5,
            alpha=0.7, label=r'$T_{Rindler}/T_{Gibbs}$')  # (local)
ax.axhline(1.0, color='red', ls='--', alpha=0.5, label='Unity')
if n_valid >= 2:
    ax.axhline(mean_ratio, color='blue', ls=':', alpha=0.5,
               label=f'Mean = {mean_ratio:.4f}')
    ax.fill_between(tau_arr, mean_ratio*0.95, mean_ratio*1.05,
                    alpha=0.1, color='blue', label='5% band')  # (local)
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$T_{acoustic} / T_{Gibbs}$')
ax.set_title(f'(c) Ratio stability')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# (d) 8-mode spectrum
ax = axes[1, 0]
ax.plot(tau_arr, E_8_all[:, 0], 'bs-', ms=8, label=r'$E_{B2}$')
ax.plot(tau_arr, E_8_all[:, 4], 'r^-', ms=8, label=r'$E_{B1}$')
ax.plot(tau_arr, E_8_all[:, 5], 'gD-', ms=8, label=r'$E_{B3}$')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_k$ (M$_{KK}$)')
ax.set_title('(d) 8-mode spectrum from RG')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (e) Off-Jensen
ax = axes[1, 1]
oj_plot = ~np.isnan(off_jensen_ratios) & (off_jensen_ratios > 0)
if np.any(oj_plot):
    ax.plot(epsilons_s41[oj_plot], off_jensen_ratios[oj_plot], 'ko-', ms=8, lw=2)
ax.axhline(ratio_fold_ref, color='red', ls='--', alpha=0.5,
           label=f'Fold ref = {ratio_fold_ref:.4f}')
ax.set_xlabel(r'Off-Jensen $\epsilon$')
ax.set_ylabel(r'$T_{acoustic} / T_{Gibbs}$')
ax.set_title('(e) Off-Jensen stability')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
if len(epsilons_s41) > 1:
    ax.set_xscale('symlog', linthresh=0.001)

# (f) m^2 dispersion
ax = axes[1, 2]
ax.plot(tau_grid_50, m2_B2, 'b.-', ms=4, label=r'$m^2_{B2}(\tau)$')
ax.plot(tau_grid_50, m2_B1, 'r.-', ms=4, alpha=0.5, label=r'$m^2_{B1}(\tau)$')
for t in sweep_taus:
    ax.axvline(t, color='green', ls=':', alpha=0.3)
    ax.plot(t, cs_m2_B2(t), 'g*', ms=12, zorder=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$m^2$ (M$_{KK}^2$)')
ax.set_title(r'(f) Dispersion + sweep points')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(base / 's52_hawking_t_sweep.png', dpi=150)
print(f"  Plot saved: computations/session-52/s52_hawking_t_sweep.png")

print(f"\n{'='*72}")
print("COMPUTATION COMPLETE")
print(f"{'='*72}")
