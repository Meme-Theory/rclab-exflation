#!/usr/bin/env python3
"""
BAYESIAN-PENROSE-60: Bayesian Error Propagation for Penrose Threshold
=====================================================================
Gate: PASS if P(alpha_total > alpha_crit) > 0.90
      FAIL if P(alpha_total > alpha_crit) < 0.50
      INFO if P in [0.50, 0.90]

Physics:
  PENROSE-ACCESS-59 reported alpha_total = 0.555, only 6.1% above threshold
  alpha_crit = 0.5227. The overlap parameter omega = 0.70 was a modeling
  choice, not a derived quantity. This computation propagates uncertainty
  in omega (and in the input alpha components) through the combination
  formula to determine whether the PASS verdict is robust.

  Combination formula (from s59_penrose_access.py):
    alpha_additive  = alpha_mp + alpha_Andreev
    alpha_quadrature = sqrt(alpha_mp^2 + alpha_Andreev^2)
    alpha_total(omega) = omega * alpha_additive + (1-omega) * alpha_quadrature

  This is a continuous interpolation between:
    omega = 1: channels perfectly aligned (additive)
    omega = 0: channels perfectly orthogonal (quadrature)

  Nuclear analog (Paper 06, Dobaczewski et al.): In nuclear DFT, theoretical
  uncertainties from model parameters (coupling constants, pairing strengths)
  are propagated through the HFB equations to observables. The methodology
  is identical: identify the uncertain parameters, define priors, sample,
  compute posterior on observables.

  Here omega is the analog of the poorly-constrained pairing functional
  form in nuclear DFT -- its value is physically motivated but not
  uniquely determined.

  EXTENDED UNCERTAINTY MODEL:
  Beyond omega, alpha_mp and alpha_Andreev themselves carry uncertainty:
  - alpha_mp = 0.181: derived from r_npair3 = 0.412, which has ED finite-size
    error. N_pair=3 in 8 modes gives limited statistics. Conservative estimate:
    sigma(r) ~ 0.02 (typical for level spacing ratios at this dimension).
  - alpha_Andreev = 0.417: derived from r_Andreev = 0.446, same mapping.
    sigma(r) ~ 0.02.
  These propagate through alpha = (r - r_Poisson) / (r_GOE - r_Poisson).

Session: S60, Gate: BAYESIAN-PENROSE-60
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
import os
import sys

# Change to project root
os.chdir("C:/sandbox/Ainulindale Exflation")
sys.path.insert(0, "computations")
from canonical_constants import *

# ==============================================================================
# STEP 0: Load S59 Penrose access data
# ==============================================================================

data = np.load("computations/session-59/s59_penrose_access.npz", allow_pickle=True)

alpha_mp_central    = float(data['alpha_multipair'])    # 0.181
alpha_And_central   = float(data['alpha_Andreev'])      # 0.417
alpha_crit          = float(data['alpha_crit'])         # 0.5227
omega_central       = float(data['overlap_factor'])     # 0.70
alpha_total_central = float(data['alpha_total'])        # 0.555

r_npair3   = float(data['r_npair3'])    # 0.412
r_Andreev  = float(data['r_Andreev'])   # 0.446
r_Poisson  = float(data['r_Poisson'])   # 0.386
r_GOE      = float(data['r_GOE'])       # 0.530

print("=" * 72)
print("BAYESIAN-PENROSE-60: Bayesian Error Propagation")
print("=" * 72)
print(f"  alpha_mp (central)   = {alpha_mp_central:.6f}")
print(f"  alpha_And (central)  = {alpha_And_central:.6f}")
print(f"  alpha_crit           = {alpha_crit:.4f}")
print(f"  omega (central)      = {omega_central:.2f}")
print(f"  alpha_total (S59)    = {alpha_total_central:.6f}")
print(f"  r_npair3             = {r_npair3:.4f}")
print(f"  r_Andreev            = {r_Andreev:.4f}")

# ==============================================================================
# STEP 1: Define priors on uncertain parameters
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 1: Prior definitions")
print("=" * 72)

N_samples = 100_000  # Large sample for converged posteriors
rng = np.random.default_rng(seed=20260327)

# --- Prior on omega ---
# Physical bounds: omega in [0, 1] (interpolation parameter).
# omega = 1: channels perfectly aligned (same Penrose direction).
# omega = 0: channels perfectly orthogonal (independent directions).
# Physical argument: both channels affect B3 occupation through B2->B3
# transfer, so they are partially aligned. But "70% alignment" is an
# estimate, not a measurement.
# Prior: Uniform on [0.3, 1.0]. The lower bound 0.3 reflects that
# SOME alignment exists (both channels drive B3). No alignment at all
# (omega = 0) would mean the channels are perfectly orthogonal, which
# contradicts the shared B3 involvement.
omega_lo, omega_hi = 0.30, 1.00
omega_samples = rng.uniform(omega_lo, omega_hi, size=N_samples)
print(f"  omega prior: Uniform[{omega_lo}, {omega_hi}]")
print(f"  omega mean = {0.5*(omega_lo+omega_hi):.3f}, width = {omega_hi-omega_lo:.2f}")

# --- Prior on level spacing ratios ---
# sigma(r) from ED finite-size effects. In random matrix theory,
# the standard deviation of the mean level spacing ratio for N levels
# is approximately sigma_r ~ C / sqrt(N) where C ~ 0.1-0.2.
# For N_pair=3 in 8 modes: Fock space dim = C(8,3) = 56 levels.
# After symmetry reduction, ~20-30 useful levels.
# sigma_r ~ 0.15 / sqrt(25) ~ 0.03. Use sigma_r = 0.025 (moderate).

sigma_r = 0.025  # Standard deviation on mean level spacing ratio  # (local)

# r_npair3: Gaussian prior centered on measured value, truncated to [r_Poisson, r_GOE]
r_mp_samples = rng.normal(r_npair3, sigma_r, size=N_samples)
r_mp_samples = np.clip(r_mp_samples, r_Poisson, r_GOE)

# r_Andreev: same treatment
r_And_samples = rng.normal(r_Andreev, sigma_r, size=N_samples)
r_And_samples = np.clip(r_And_samples, r_Poisson, r_GOE)

print(f"  sigma_r = {sigma_r:.3f} (ED finite-size uncertainty)")
print(f"  r_npair3 prior: N({r_npair3:.3f}, {sigma_r:.3f}^2) truncated to [{r_Poisson:.3f}, {r_GOE:.3f}]")
print(f"  r_Andreev prior: N({r_Andreev:.3f}, {sigma_r:.3f}^2) truncated to [{r_Poisson:.3f}, {r_GOE:.3f}]")

# Convert r samples to alpha samples
alpha_mp_samples = (r_mp_samples - r_Poisson) / (r_GOE - r_Poisson)
alpha_And_samples = (r_And_samples - r_Poisson) / (r_GOE - r_Poisson)

print(f"\n  alpha_mp posterior: median = {np.median(alpha_mp_samples):.4f}, "
      f"68% CI = [{np.percentile(alpha_mp_samples, 16):.4f}, {np.percentile(alpha_mp_samples, 84):.4f}]")
print(f"  alpha_And posterior: median = {np.median(alpha_And_samples):.4f}, "
      f"68% CI = [{np.percentile(alpha_And_samples, 16):.4f}, {np.percentile(alpha_And_samples, 84):.4f}]")

# ==============================================================================
# STEP 2: Forward propagation -- compute alpha_total for each sample
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 2: Forward propagation (N = {})".format(N_samples))
print("=" * 72)

alpha_add_samples = alpha_mp_samples + alpha_And_samples
alpha_quad_samples = np.sqrt(alpha_mp_samples**2 + alpha_And_samples**2)

alpha_total_samples = omega_samples * alpha_add_samples + (1 - omega_samples) * alpha_quad_samples

# ==============================================================================
# STEP 3: Posterior on alpha_total
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 3: Posterior on alpha_total")
print("=" * 72)

alpha_median = np.median(alpha_total_samples)
alpha_mean = np.mean(alpha_total_samples)
alpha_std = np.std(alpha_total_samples)
alpha_p16, alpha_p84 = np.percentile(alpha_total_samples, [16, 84])
alpha_p025, alpha_p975 = np.percentile(alpha_total_samples, [2.5, 97.5])
alpha_p05, alpha_p95 = np.percentile(alpha_total_samples, [5, 95])

print(f"  Mean   = {alpha_mean:.6f}")
print(f"  Median = {alpha_median:.6f}")
print(f"  Std    = {alpha_std:.6f}")
print(f"  68% CI = [{alpha_p16:.6f}, {alpha_p84:.6f}]")
print(f"  90% CI = [{alpha_p05:.6f}, {alpha_p95:.6f}]")
print(f"  95% CI = [{alpha_p025:.6f}, {alpha_p975:.6f}]")

# ==============================================================================
# STEP 4: P(alpha_total > alpha_crit)
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 4: P(alpha_total > alpha_crit)")
print("=" * 72)

P_above = np.mean(alpha_total_samples > alpha_crit)
P_above_err = np.sqrt(P_above * (1 - P_above) / N_samples)  # Binomial error

print(f"  P(alpha_total > {alpha_crit:.4f}) = {P_above:.4f} +/- {P_above_err:.4f}")
print(f"  N_above = {np.sum(alpha_total_samples > alpha_crit)} / {N_samples}")

# ==============================================================================
# STEP 5: Critical omega (omega at which alpha_total = alpha_crit)
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 5: Critical omega")
print("=" * 72)

# At fixed (central) alpha_mp and alpha_And:
# alpha_total(omega) = omega * alpha_add + (1 - omega) * alpha_quad = alpha_crit
# omega * (alpha_add - alpha_quad) + alpha_quad = alpha_crit
# omega_crit = (alpha_crit - alpha_quad_central) / (alpha_add_central - alpha_quad_central)

alpha_add_central = alpha_mp_central + alpha_And_central
alpha_quad_central = np.sqrt(alpha_mp_central**2 + alpha_And_central**2)

denom = alpha_add_central - alpha_quad_central
if abs(denom) > 1e-15:
    omega_crit_central = (alpha_crit - alpha_quad_central) / denom
else:
    omega_crit_central = np.nan

print(f"  alpha_additive (central)   = {alpha_add_central:.6f}")
print(f"  alpha_quadrature (central) = {alpha_quad_central:.6f}")
print(f"  omega_crit (central alphas) = {omega_crit_central:.6f}")
print(f"  omega_crit is in prior [{omega_lo}, {omega_hi}]? {omega_lo <= omega_crit_central <= omega_hi}")

# Also compute omega_crit distribution (one per sample)
denom_samples = alpha_add_samples - alpha_quad_samples
valid = np.abs(denom_samples) > 1e-15
omega_crit_samples = np.full(N_samples, np.nan)
omega_crit_samples[valid] = (alpha_crit - alpha_quad_samples[valid]) / denom_samples[valid]

# Clip to physically meaningful range
omega_crit_valid = omega_crit_samples[np.isfinite(omega_crit_samples)]
omega_crit_valid = omega_crit_valid[(omega_crit_valid >= 0) & (omega_crit_valid <= 1)]

print(f"  omega_crit distribution (from alpha uncertainty):")
print(f"    median = {np.median(omega_crit_valid):.4f}")
print(f"    68% CI = [{np.percentile(omega_crit_valid, 16):.4f}, {np.percentile(omega_crit_valid, 84):.4f}]")
print(f"    95% CI = [{np.percentile(omega_crit_valid, 2.5):.4f}, {np.percentile(omega_crit_valid, 97.5):.4f}]")
print(f"    P(omega_crit < omega_lo={omega_lo}) = {np.mean(omega_crit_valid < omega_lo):.4f}")
print(f"    P(omega_crit > omega_hi={omega_hi}) = {np.mean(omega_crit_valid > omega_hi):.4f}")

# ==============================================================================
# STEP 6: Sensitivity decomposition -- which parameter dominates?
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 6: Sensitivity decomposition")
print("=" * 72)

# Variance decomposition via conditional expectation
# Var(alpha_total) = Var_omega[E[alpha|omega]] + E_omega[Var[alpha|omega]]
# The first term is from omega uncertainty, the second from r uncertainty.

# Method: fix omega at central, vary r's; fix r's at central, vary omega
# omega-only contribution
alpha_omega_only = omega_samples * alpha_add_central + (1 - omega_samples) * alpha_quad_central
var_omega = np.var(alpha_omega_only)

# r-only contribution (fix omega at central)
alpha_r_only = omega_central * alpha_add_samples + (1 - omega_central) * alpha_quad_samples
var_r = np.var(alpha_r_only)

var_total = np.var(alpha_total_samples)

# These don't sum to var_total exactly due to correlation, but give the decomposition
print(f"  Var(alpha_total)     = {var_total:.6e}")
print(f"  Var(omega-only)      = {var_omega:.6e} ({var_omega/var_total*100:.1f}%)")
print(f"  Var(r-only)          = {var_r:.6e} ({var_r/var_total*100:.1f}%)")
print(f"  Cross/interaction    = {var_total - var_omega - var_r:.6e} ({(var_total-var_omega-var_r)/var_total*100:.1f}%)")

# Also: P(PASS) under omega-only and r-only
P_omega_only = np.mean(alpha_omega_only > alpha_crit)
P_r_only = np.mean(alpha_r_only > alpha_crit)
print(f"  P(PASS | omega-only) = {P_omega_only:.4f}")
print(f"  P(PASS | r-only)     = {P_r_only:.4f}")

# ==============================================================================
# STEP 7: Alternative prior sensitivity (robustness check)
# ==============================================================================

print("\n" + "=" * 72)
print("STEP 7: Prior sensitivity analysis")
print("=" * 72)

# Test different omega priors
omega_priors = {
    'Uniform[0.0, 1.0]': rng.uniform(0.0, 1.0, size=N_samples),
    'Uniform[0.3, 1.0]': omega_samples,  # baseline
    'Uniform[0.5, 1.0]': rng.uniform(0.5, 1.0, size=N_samples),
    'Beta(3,2) on [0,1]': rng.beta(3, 2, size=N_samples),
    'Beta(5,2) on [0,1]': rng.beta(5, 2, size=N_samples),
    'Gaussian(0.7, 0.15)': np.clip(rng.normal(0.7, 0.15, size=N_samples), 0, 1),
}

# Test different sigma_r values
sigma_r_values = [0.010, 0.015, 0.020, 0.025, 0.030, 0.040]

print("\n  --- Omega prior sensitivity (sigma_r = 0.025 fixed) ---")
for name, omega_s in omega_priors.items():
    a_add = alpha_mp_samples + alpha_And_samples
    a_quad = np.sqrt(alpha_mp_samples**2 + alpha_And_samples**2)
    a_tot = omega_s * a_add + (1 - omega_s) * a_quad
    p = np.mean(a_tot > alpha_crit)
    med = np.median(a_tot)
    print(f"  {name:30s}: P(PASS) = {p:.4f}, median = {med:.4f}")

print(f"\n  --- sigma_r sensitivity (omega ~ Uniform[0.3, 1.0] fixed) ---")
for sr in sigma_r_values:
    r_mp_s = np.clip(rng.normal(r_npair3, sr, size=N_samples), r_Poisson, r_GOE)
    r_And_s = np.clip(rng.normal(r_Andreev, sr, size=N_samples), r_Poisson, r_GOE)
    a_mp_s = (r_mp_s - r_Poisson) / (r_GOE - r_Poisson)
    a_And_s = (r_And_s - r_Poisson) / (r_GOE - r_Poisson)
    a_add_s = a_mp_s + a_And_s
    a_quad_s = np.sqrt(a_mp_s**2 + a_And_s**2)
    omega_s = rng.uniform(omega_lo, omega_hi, size=N_samples)
    a_tot_s = omega_s * a_add_s + (1 - omega_s) * a_quad_s
    p = np.mean(a_tot_s > alpha_crit)
    print(f"  sigma_r = {sr:.3f}: P(PASS) = {p:.4f}")

# ==============================================================================
# STEP 8: Gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: BAYESIAN-PENROSE-60")
print("=" * 72)

if P_above > 0.90:
    verdict = "PASS"
elif P_above < 0.50:
    verdict = "FAIL"
else:
    verdict = "INFO"

print(f"  P(alpha_total > alpha_crit) = {P_above:.4f} +/- {P_above_err:.4f}")
print(f"  Gate thresholds: PASS > 0.90, FAIL < 0.50, INFO in [0.50, 0.90]")
print(f"  VERDICT: {verdict}")
print(f"  omega_crit = {omega_crit_central:.4f} (at central alphas)")

if verdict == "INFO":
    print(f"  The S59 PASS verdict is NOT robust under parameter uncertainty.")
    print(f"  omega_crit = {omega_crit_central:.4f} falls INSIDE the prior range.")
    print(f"  The Penrose channel accessibility depends on knowing omega to")
    print(f"  better precision than currently available.")
elif verdict == "FAIL":
    print(f"  The S59 PASS verdict is OVERTURNED by uncertainty propagation.")
    print(f"  The majority of prior-consistent parameter space gives alpha < alpha_crit.")
elif verdict == "PASS":
    print(f"  The S59 PASS verdict is ROBUST under parameter uncertainty.")
    print(f"  P > 0.90 means the Penrose channel is accessible for nearly all")
    print(f"  prior-consistent parameter choices.")

# ==============================================================================
# SAVE RESULTS
# ==============================================================================

print("\n" + "=" * 72)
print("Saving results...")
print("=" * 72)

results = {
    # Gate
    'gate_name': np.array('BAYESIAN-PENROSE-60'),
    'gate_verdict': np.array(verdict),

    # Input (from S59)
    'alpha_mp_central': np.float64(alpha_mp_central),
    'alpha_And_central': np.float64(alpha_And_central),
    'alpha_crit': np.float64(alpha_crit),
    'omega_central': np.float64(omega_central),
    'alpha_total_s59': np.float64(alpha_total_central),

    # Priors
    'omega_prior_lo': np.float64(omega_lo),
    'omega_prior_hi': np.float64(omega_hi),
    'sigma_r': np.float64(sigma_r),
    'N_samples': np.int64(N_samples),

    # Posterior on alpha_total
    'alpha_total_mean': np.float64(alpha_mean),
    'alpha_total_median': np.float64(alpha_median),
    'alpha_total_std': np.float64(alpha_std),
    'alpha_total_ci68_lo': np.float64(alpha_p16),
    'alpha_total_ci68_hi': np.float64(alpha_p84),
    'alpha_total_ci90_lo': np.float64(alpha_p05),
    'alpha_total_ci90_hi': np.float64(alpha_p95),
    'alpha_total_ci95_lo': np.float64(alpha_p025),
    'alpha_total_ci95_hi': np.float64(alpha_p975),

    # Gate probability
    'P_above_crit': np.float64(P_above),
    'P_above_crit_err': np.float64(P_above_err),

    # Critical omega
    'omega_crit_central': np.float64(omega_crit_central),
    'omega_crit_median': np.float64(np.median(omega_crit_valid)),
    'omega_crit_ci68_lo': np.float64(np.percentile(omega_crit_valid, 16)),
    'omega_crit_ci68_hi': np.float64(np.percentile(omega_crit_valid, 84)),

    # Variance decomposition
    'var_total': np.float64(var_total),
    'var_omega_frac': np.float64(var_omega / var_total),
    'var_r_frac': np.float64(var_r / var_total),

    # P(PASS) under partial uncertainties
    'P_pass_omega_only': np.float64(P_omega_only),
    'P_pass_r_only': np.float64(P_r_only),

    # Posterior samples (for downstream use)
    'alpha_total_samples': alpha_total_samples.astype(np.float32),
    'omega_crit_samples': omega_crit_valid.astype(np.float32),
}

np.savez("computations/session-60/s60_bayesian_penrose.npz", **results)
print("  Saved s60_bayesian_penrose.npz")

# ==============================================================================
# PLOT
# ==============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('BAYESIAN-PENROSE-60: Uncertainty Propagation for Penrose Threshold',
             fontsize=15, fontweight='bold')

# --- Panel 1: alpha_total posterior histogram ---
ax = axes[0, 0]
counts, bins, patches = ax.hist(alpha_total_samples, bins=200, density=True,
                                 color='steelblue', alpha=0.7, edgecolor='none')
ax.axvline(alpha_crit, color='red', linewidth=2, linestyle='--',
           label=f'$\\alpha_{{crit}}$ = {alpha_crit:.4f}')
ax.axvline(alpha_median, color='green', linewidth=2, linestyle='-',
           label=f'Median = {alpha_median:.4f}')
ax.axvspan(alpha_p16, alpha_p84, alpha=0.15, color='green', label='68% CI')
ax.axvspan(alpha_p025, alpha_p975, alpha=0.08, color='blue', label='95% CI')

# Shade P(PASS) region
bin_centers = 0.5 * (bins[:-1] + bins[1:])
for i, (patch_obj, bc) in enumerate(zip(patches, bin_centers)):
    if bc > alpha_crit:
        patch_obj.set_facecolor('indianred')
        patch_obj.set_alpha(0.8)

ax.set_xlabel('$\\alpha_{total}$', fontsize=13)
ax.set_ylabel('Posterior density', fontsize=13)
ax.set_title(f'$P(\\alpha > \\alpha_{{crit}})$ = {P_above:.3f}', fontsize=13)
ax.legend(fontsize=9, loc='upper left')

# --- Panel 2: omega_crit distribution ---
ax = axes[0, 1]
ax.hist(omega_crit_valid, bins=150, density=True, color='darkorange',
        alpha=0.7, edgecolor='none')  # (local)
ax.axvspan(omega_lo, omega_hi, alpha=0.1, color='green', label=f'$\\omega$ prior [{omega_lo}, {omega_hi}]')
ax.axvline(omega_crit_central, color='red', linewidth=2, linestyle='--',
           label=f'$\\omega_{{crit}}$ = {omega_crit_central:.3f}')
ax.axvline(omega_central, color='blue', linewidth=2, linestyle=':',
           label=f'$\\omega_{{S59}}$ = {omega_central:.2f}')
ax.set_xlabel('$\\omega_{crit}$', fontsize=13)
ax.set_ylabel('Density', fontsize=13)
ax.set_title('Critical Overlap Distribution', fontsize=13)
ax.legend(fontsize=9)
ax.set_xlim(0, 1)

# --- Panel 3: alpha_total vs omega (functional dependence) ---
ax = axes[0, 2]
omega_grid = np.linspace(0, 1, 500)
# Central curve
alpha_add_c = alpha_mp_central + alpha_And_central
alpha_quad_c = np.sqrt(alpha_mp_central**2 + alpha_And_central**2)
alpha_vs_omega_c = omega_grid * alpha_add_c + (1 - omega_grid) * alpha_quad_c

ax.plot(omega_grid, alpha_vs_omega_c, 'b-', linewidth=2, label='Central ($\\alpha_{mp}$, $\\alpha_{And}$ fixed)')

# Envelope from alpha uncertainty (Monte Carlo)
alpha_vs_omega_lo = np.zeros_like(omega_grid)
alpha_vs_omega_hi = np.zeros_like(omega_grid)
for i, om in enumerate(omega_grid):
    a_add_s = alpha_mp_samples + alpha_And_samples
    a_quad_s = np.sqrt(alpha_mp_samples**2 + alpha_And_samples**2)
    a_s = om * a_add_s + (1 - om) * a_quad_s
    alpha_vs_omega_lo[i] = np.percentile(a_s, 16)
    alpha_vs_omega_hi[i] = np.percentile(a_s, 84)

ax.fill_between(omega_grid, alpha_vs_omega_lo, alpha_vs_omega_hi,
                alpha=0.2, color='blue', label='68% band ($\\alpha$ uncertainty)')  # (local)

ax.axhline(alpha_crit, color='red', linewidth=2, linestyle='--',
           label=f'$\\alpha_{{crit}}$ = {alpha_crit:.4f}')
ax.axvline(omega_crit_central, color='red', linewidth=1.5, linestyle=':',
           label=f'$\\omega_{{crit}}$ = {omega_crit_central:.3f}', alpha=0.7)
ax.axvspan(omega_lo, omega_hi, alpha=0.08, color='green', label='$\\omega$ prior')
ax.set_xlabel('$\\omega$ (overlap parameter)', fontsize=13)
ax.set_ylabel('$\\alpha_{total}$', fontsize=13)
ax.set_title('$\\alpha_{total}(\\omega)$ with uncertainty', fontsize=13)
ax.legend(fontsize=8, loc='upper left')

# --- Panel 4: Variance decomposition ---
ax = axes[1, 0]
labels_pie = ['$\\omega$ uncertainty', '$r$ uncertainty', 'Cross-term']
fracs = [var_omega/var_total*100, var_r/var_total*100,
         max(0, (var_total-var_omega-var_r)/var_total*100)]
# Handle potential negative cross-term
if fracs[2] < 0:
    fracs = [var_omega/var_total*100, var_r/var_total*100, 0]
    fracs = [f/sum(fracs)*100 for f in fracs]
colors_pie = ['#FF9800', '#2196F3', '#9E9E9E']
wedges, texts, autotexts = ax.pie(fracs, labels=labels_pie, autopct='%1.1f%%',
                                   colors=colors_pie, startangle=90)
for t in autotexts:
    t.set_fontsize(11)
    t.set_fontweight('bold')
ax.set_title('Variance Decomposition', fontsize=13)

# --- Panel 5: Prior sensitivity ---
ax = axes[1, 1]
# Compute P(PASS) for a sweep of omega priors (varying the lower bound)
lo_grid = np.linspace(0.0, 0.7, 50)
P_pass_vs_lo = []
for lo in lo_grid:
    omega_s = rng.uniform(lo, 1.0, size=N_samples)
    r_mp_s = np.clip(rng.normal(r_npair3, sigma_r, size=N_samples), r_Poisson, r_GOE)
    r_And_s = np.clip(rng.normal(r_Andreev, sigma_r, size=N_samples), r_Poisson, r_GOE)
    a_mp_s = (r_mp_s - r_Poisson) / (r_GOE - r_Poisson)
    a_And_s = (r_And_s - r_Poisson) / (r_GOE - r_Poisson)
    a_add_s = a_mp_s + a_And_s
    a_quad_s = np.sqrt(a_mp_s**2 + a_And_s**2)
    a_tot_s = omega_s * a_add_s + (1 - omega_s) * a_quad_s
    P_pass_vs_lo.append(np.mean(a_tot_s > alpha_crit))

ax.plot(lo_grid, P_pass_vs_lo, 'b-', linewidth=2)
ax.axhline(0.90, color='green', linestyle='--', linewidth=1.5, label='PASS threshold (0.90)')
ax.axhline(0.50, color='red', linestyle='--', linewidth=1.5, label='FAIL threshold (0.50)')
ax.axvline(omega_lo, color='orange', linestyle=':', linewidth=1.5,
           label=f'Baseline $\\omega_{{lo}}$ = {omega_lo}')
ax.set_xlabel('$\\omega_{lower}$ (prior lower bound)', fontsize=13)
ax.set_ylabel('$P(\\alpha > \\alpha_{crit})$', fontsize=13)
ax.set_title('Prior Sensitivity: $P(PASS)$ vs $\\omega$ prior', fontsize=13)
ax.legend(fontsize=9)
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)

# --- Panel 6: 2D joint posterior (omega, alpha_total) ---
ax = axes[1, 2]
# Subsample for scatter
idx = rng.choice(N_samples, size=min(5000, N_samples), replace=False)
scatter_colors = ['indianred' if a > alpha_crit else 'steelblue'
                  for a in alpha_total_samples[idx]]
ax.scatter(omega_samples[idx], alpha_total_samples[idx], c=scatter_colors,
           alpha=0.3, s=2, rasterized=True)  # (local)
ax.axhline(alpha_crit, color='red', linewidth=2, linestyle='--',
           label=f'$\\alpha_{{crit}}$ = {alpha_crit:.4f}')
ax.axvline(omega_crit_central, color='red', linewidth=1.5, linestyle=':',
           alpha=0.7)  # (local)
ax.set_xlabel('$\\omega$', fontsize=13)
ax.set_ylabel('$\\alpha_{total}$', fontsize=13)
ax.set_title(f'Joint posterior (blue: FAIL, red: PASS)', fontsize=13)
ax.legend(fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("computations/session-60/s60_bayesian_penrose.png", dpi=150, bbox_inches='tight')
print("  Saved s60_bayesian_penrose.png")

# ==============================================================================
# SUMMARY
# ==============================================================================

print("\n" + "=" * 72)
print("SUMMARY: BAYESIAN-PENROSE-60")
print("=" * 72)
print(f"  S59 central: alpha_total = {alpha_total_central:.4f} at omega = {omega_central:.2f}")
print(f"  Posterior: alpha_total = {alpha_median:.4f} +/- {alpha_std:.4f} (median +/- std)")
print(f"  68% CI: [{alpha_p16:.4f}, {alpha_p84:.4f}]")
print(f"  95% CI: [{alpha_p025:.4f}, {alpha_p975:.4f}]")
print(f"  P(alpha > alpha_crit) = {P_above:.4f} +/- {P_above_err:.4f}")
print(f"  omega_crit = {omega_crit_central:.4f}")
print(f"  Dominant uncertainty: {'omega' if var_omega > var_r else 'r'} ({max(var_omega,var_r)/var_total*100:.0f}% of variance)")
print(f"  VERDICT: {verdict}")
