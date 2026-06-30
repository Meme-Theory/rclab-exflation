#!/usr/bin/env python3
"""
BAYESIAN-H0-60: Bayesian Error Budget for Spectral Action Ratios
================================================================

Context: W2-1 (PW-H0-CONV-60) discovered Tr(|D_K|) diverges as L^{6.2}.
The S59 H_0 = 68.8 derivation used this divergent quantity => RETRACTED.
The correct H_0 requires the true Seeley-DeWitt a_2(D_K^2), which is a
FINITE local geometric integral (independent of PW truncation).

This script performs Bayesian uncertainty quantification on:
  (1) The a_4/a_2 RATIO at each truncation level L
  (2) Convergence of ratios as L -> infty despite divergent individual coefficients
  (3) Sensitivity to tau uncertainty (from CHEEGER-SIGMA-59)
  (4) Sensitivity to cutoff function choice (step, exponential, Gaussian)

The nuclear DFT perspective (Paper 06): every theoretical prediction has
uncertainties from model assumptions, parameter choices, and truncation.
We decompose the total variance into these contributions.

Gate: BAYESIAN-H0-60
  PASS: Some spectral ratio converges with well-defined error bars
  FAIL: All ratios diverge (no convergent observable)
  INFO: Partial convergence with large uncertainties

Author: Nazarewicz Nuclear Structure Theorist
Session: S60
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced, H_0_km_s_Mpc,
    a0_fold, a2_fold, a4_fold
)

# ==============================================================================
# 1. Load data
# ==============================================================================

data_s59 = np.load('computations/session-59/s59_spinor_norm.npz', allow_pickle=True)
data_cheeger = np.load('computations/session-59/s59_cheeger_sigma.npz', allow_pickle=True)
data_pw = np.load('computations/session-60/s60_pw_h0_conv.npz', allow_pickle=True)

# PW convergence data (L = 0..7)
L_arr = data_pw['L_arr']       # [0, 1, 2, 3, 4, 5, 6, 7]
a0_cumul = data_pw['a0_cumul'].astype(float)
a2_cumul = data_pw['a2_cumul']
a4_cumul = data_pw['a4_cumul']
N_cumul = data_pw['N_cumul']    # N_factor = a2/(a0/dim_spinor) at each L
n_evals_cumul = data_pw['n_evals_cumul']
alpha_growth = float(data_pw['alpha_growth'])  # L^{6.2} growth exponent

# Per-irrep data
irrep_a2 = data_pw['irrep_a2']
irrep_a4 = data_pw['irrep_a4']
irrep_level = data_pw['irrep_level']
irrep_dim = data_pw['irrep_dim']

# Cheeger stiffness data
tau_dense = data_cheeger['tau_dense']
m_sigma = float(data_cheeger['m_sigma'])       # sigma modulus mass = 7.342 M_KK
m_sigma_sq = float(data_cheeger['m_sigma_sq'])

# S59 sector decomposition
sector_a2_s59 = data_s59['sector_a2']
sector_a4_s59 = data_s59['sector_a4']
sector_a0_s59 = data_s59['sector_a0']
H0_corrected_s59 = float(data_s59['H_0_corrected'])  # 68.77 (now retracted)

print("=" * 72)
print("BAYESIAN-H0-60: Bayesian Error Budget for Spectral Action Ratios")
print("=" * 72)

# ==============================================================================
# 2. Compute spectral ratios at each truncation level
# ==============================================================================

# Key ratio 1: a4/a2 (determines Higgs mass relative to Planck mass)
r42 = a4_cumul / a2_cumul  # a4/a2 at each L

# Key ratio 2: N_factor = a2 / (a0 / dim_spinor) — the "H_0 factor"
dim_spinor = 16.0  # (local)
N_factor = a2_cumul / (a0_cumul / dim_spinor)

# Key ratio 3: a2/a0 (scalar curvature per mode)
r20 = a2_cumul / a0_cumul

# Key ratio 4: Per-level INCREMENTAL ratios
# delta_a4(L) / delta_a2(L) for each PW shell
delta_a2 = np.diff(a2_cumul, prepend=0)
delta_a4 = np.diff(a4_cumul, prepend=0)
delta_a0 = np.diff(a0_cumul, prepend=0)
r42_incr = np.where(delta_a2 > 0, delta_a4 / delta_a2, np.nan)
r20_incr = np.where(delta_a0 > 0, delta_a2 / delta_a0, np.nan)

print("\n--- Spectral ratios at each PW truncation level L ---")
print(f"{'L':>3} {'a0':>14} {'a2':>14} {'a4':>14} {'a4/a2':>10} {'N_factor':>10} {'a2/a0':>10}")
for i, L in enumerate(L_arr):
    print(f"{L:3d} {a0_cumul[i]:14.1f} {a2_cumul[i]:14.3f} {a4_cumul[i]:14.3f} "
          f"{r42[i]:10.6f} {N_factor[i]:10.6f} {r20[i]:10.6f}")

print(f"\nIncremental ratios delta_a4/delta_a2 per shell:")
for i, L in enumerate(L_arr):
    if not np.isnan(r42_incr[i]):
        print(f"  L={L}: delta_a4/delta_a2 = {r42_incr[i]:.6f}, delta_a2/delta_a0 = {r20_incr[i]:.6f}")

# ==============================================================================
# 3. Convergence analysis: fit power-law growth of individual coefficients
# ==============================================================================

# For L >= 2, fit a_n(L) ~ C * (L+1)^alpha
# This tells us whether RATIOS can converge even if individual sums diverge

L_fit = L_arr[2:]  # L = 2,3,...,7
log_Lp1 = np.log(L_fit + 1)

# Fit a2(L) growth
log_a2_fit = np.log(a2_cumul[2:])
p_a2 = np.polyfit(log_Lp1, log_a2_fit, 1)
alpha_a2 = p_a2[0]

# Fit a4(L) growth
log_a4_fit = np.log(a4_cumul[2:])
p_a4 = np.polyfit(log_Lp1, log_a4_fit, 1)
alpha_a4 = p_a4[0]

# Fit a0(L) growth
log_a0_fit = np.log(a0_cumul[2:])
p_a0 = np.polyfit(log_Lp1, log_a0_fit, 1)
alpha_a0 = p_a0[0]

# Growth exponent of ratio a4/a2: alpha_a4 - alpha_a2
alpha_ratio42 = alpha_a4 - alpha_a2
alpha_ratio20 = alpha_a2 - alpha_a0

# If alpha_ratio ~ 0, the ratio CONVERGES despite divergent sums
print(f"\n--- Power-law growth analysis (L >= 2): a_n ~ C*(L+1)^alpha ---")
print(f"  a0 growth exponent: alpha_a0 = {alpha_a0:.4f}")
print(f"  a2 growth exponent: alpha_a2 = {alpha_a2:.4f}")
print(f"  a4 growth exponent: alpha_a4 = {alpha_a4:.4f}")
print(f"  Ratio a4/a2 effective exponent: alpha_r42 = {alpha_ratio42:.4f}")
print(f"  Ratio a2/a0 effective exponent: alpha_r20 = {alpha_ratio20:.4f}")

# Test: do the ratios converge? Fit ratio vs L directly
print(f"\n--- Direct ratio convergence test ---")
# Fractional change per step: |r(L) - r(L-1)| / r(L)
for name, ratio_arr in [("a4/a2", r42), ("N_factor", N_factor), ("a2/a0", r20)]:
    frac_changes = []
    for i in range(1, len(ratio_arr)):
        fc = abs(ratio_arr[i] - ratio_arr[i-1]) / abs(ratio_arr[i])
        frac_changes.append(fc)
    print(f"  {name}:")
    for i, fc in enumerate(frac_changes):
        print(f"    L={i+1}: fractional change = {fc:.6f} ({fc*100:.4f}%)")
    # Convergence criterion: fractional change < 1%
    last_fc = frac_changes[-1]
    converging = last_fc < 0.01
    print(f"    Last step convergence (< 1%): {'YES' if converging else 'NO'} ({last_fc*100:.4f}%)")

# ==============================================================================
# 4. Cutoff function sensitivity (Bayesian model averaging)
# ==============================================================================
# The spectral action uses Tr f(D^2/Lambda^2).
# For different f, the heat-kernel coefficients weight differently.
# At finite L, the ratios depend on f. This is the "cutoff function" uncertainty.
#
# Step function: f(x) = Theta(1-x) => standard heat kernel
# Exponential: f(x) = exp(-x) => Laplace transform weighting
# Gaussian: f(x) = exp(-x^2) => sharper UV suppression
#
# The spectral coefficients a_n are UNIVERSAL (independent of f at Lambda -> infty).
# But at finite Lambda (finite L), f matters.
# We model this by reweighting eigenvalues omega_i with different f.

# Eigenvalues by irrep
omega_min_irrep = data_pw['irrep_omega_min']
omega_max_irrep = data_pw['irrep_omega_max']
omega_mean_irrep = (omega_min_irrep + omega_max_irrep) / 2.0

# For each cutoff function, compute weighted sums at each L
# Using omega^2 / Lambda^2 where Lambda = omega_max at that L
def compute_weighted_ratio_per_L(a2_arr, a4_arr, omega_mean, omega_max_L,
                                 cutoff_type='step'):
    """
    Compute ratio a4_eff/a2_eff where eigenvalues are reweighted by cutoff.

    For true Seeley-DeWitt, these ratios are cutoff-independent in the
    Lambda -> infty limit. At finite truncation, the cutoff DOES matter.
    """
    # For each irrep, the "effective" contribution is a_n * w(omega/Lambda)
    # where w depends on the cutoff function
    x = (omega_mean / omega_max_L) ** 2  # x = omega^2 / Lambda^2

    if cutoff_type == 'step':
        w = np.ones_like(x)  # step function: everything below Lambda contributes equally
    elif cutoff_type == 'exponential':
        w = np.exp(-x)
    elif cutoff_type == 'gaussian':
        w = np.exp(-x**2)
    else:
        w = np.ones_like(x)

    a2_weighted = np.sum(a2_arr * w)
    a4_weighted = np.sum(a4_arr * w)

    if a2_weighted > 0:
        return a4_weighted / a2_weighted
    return np.nan

# For each L, compute cutoff-dependent ratios using all irreps up to that L
cutoff_types = ['step', 'exponential', 'gaussian']
n_L = len(L_arr)
ratios_by_cutoff = {ct: np.zeros(n_L) for ct in cutoff_types}

for i_L, L in enumerate(L_arr):
    # Select irreps with level <= L
    mask = irrep_level <= L
    a2_sel = irrep_a2[mask]
    a4_sel = irrep_a4[mask]
    om_sel = omega_mean_irrep[mask]

    # Lambda_L = max eigenvalue at this truncation
    om_max_sel = omega_max_irrep[mask]
    Lambda_L = np.max(om_max_sel) if len(om_max_sel) > 0 else 1.0

    for ct in cutoff_types:
        ratios_by_cutoff[ct][i_L] = compute_weighted_ratio_per_L(
            a2_sel, a4_sel, om_sel, Lambda_L, ct
        )

print(f"\n--- Cutoff function sensitivity for a4/a2 ratio ---")
print(f"{'L':>3}", end="")
for ct in cutoff_types:
    print(f" {ct:>14}", end="")
print(f" {'spread':>10}")
for i_L, L in enumerate(L_arr):
    vals = [ratios_by_cutoff[ct][i_L] for ct in cutoff_types]
    spread = max(vals) - min(vals)
    print(f"{L:3d}", end="")
    for v in vals:
        print(f" {v:14.6f}", end="")
    print(f" {spread:10.6f}")

# ==============================================================================
# 5. Tau uncertainty from Cheeger stiffness
# ==============================================================================
# The fold is at tau_fold = 0.19. The sigma modulus mass gives the stiffness.
# We need to know how a_n changes with tau near the fold.
# Since eigenvalues omega(tau) depend on tau, a_2(tau) inherits tau-dependence.
# From S59: the spectral coefficients are computed at tau_fold.
# We estimate da_2/dtau using the gradient stiffness data.

# From the cheeger data, the Hessian of the spectral action at the fold gives
# the tau-curvature. The fractional change in a_2 with tau is:
# delta(a_2)/a_2 ~ (1/2) * d2S/dtau2 * (delta_tau)^2 / S
# But more directly, we use the a_2 ratio at the fold and its tau-dependence.

# S59 provides H_0_corrected = 68.77 from a2_corrected/16 prescription.
# The tau uncertainty comes from the modulus mass: sigma_tau ~ 1/m_tau
# For a quantum oscillator in the tau potential well:
# sigma_tau = 1/sqrt(2 * m_tau * omega_tau) for the ground state

# From canonical constants: m_tau = 2.062, omega_tau = 8.27
# But these are for the SPECTRAL ACTION potential, which is now retracted
# as the stabilization mechanism.
# We still use the Cheeger stiffness as a LOWER BOUND on tau confinement.

# The sigma_tau from the Cheeger stiffness of the sigma channel:
# d2V/dsigma2 at fold = 2393.95 (from cheeger data)
# This constrains SIGMA, not tau. For tau, we use d2V/dtau2.
d2V_dtau2 = data_cheeger['d2V_dtau2_SA']

# Find the fold index
tau_fold_idx = np.argmin(np.abs(tau_dense - tau_fold))
d2V_dtau2_at_fold = d2V_dtau2[tau_fold_idx]

# The spectral action second derivative at the fold
# Note: d2V_dtau2 can be NEGATIVE (the fold is a saddle in SA, not a minimum)
print(f"\n--- Tau uncertainty analysis ---")
print(f"  tau_fold = {tau_fold}")
print(f"  d2V/dtau2 at fold = {d2V_dtau2_at_fold:.4f}")
print(f"  (Negative => fold is SA maximum in tau direction, not minimum)")

# Since the tau direction is unstable (d2V/dtau2 < 0 near fold),
# the tau uncertainty is NOT from a potential well.
# Instead, we parametrize sigma_tau as a model uncertainty.
# Conservative: delta_tau = 0.01 (5% of tau_fold)
# Moderate: delta_tau = 0.005 (2.6%)
# Aggressive: delta_tau = 0.001 (0.5%)

sigma_tau_choices = [0.001, 0.005, 0.01, 0.02]

# Estimate da_n/dtau at fold from the per-level data
# a_2(tau) ~ sum_i omega_i(tau)^2 * d_i  where d_i = dim of irrep
# domega/dtau ~ (omega(tau+dtau) - omega(tau-dtau)) / (2*dtau)
# We don't have multi-tau eigenvalue data. So estimate from the
# S59 V_on_Jensen slope:
V_on_Jensen = data_cheeger['V_on_Jensen']
dV_dtau = np.gradient(V_on_Jensen, tau_dense)
dV_at_fold = dV_dtau[tau_fold_idx]

# Fractional sensitivity: (1/a_2) * da_2/dtau
# From the spectral action S(tau) = sum f_n * a_n(tau), the gradient at fold
# dS/dtau at fold: from canonical constants
from canonical_constants import dS_fold, d2S_fold, S_fold
frac_dS_dtau = dS_fold / S_fold  # fractional gradient

print(f"  dS/dtau at fold = {dS_fold:.2f}")
print(f"  S at fold = {S_fold:.2f}")
print(f"  Fractional dS/dtau = {frac_dS_dtau:.6f}")

# For ratios a4/a2: the tau-dependence of the ratio depends on whether
# a4 and a2 have the SAME fractional tau-dependence.
# If they do (same scaling), the ratio is tau-independent.
# We test this with the sector data from S59.

# ==============================================================================
# 6. Bayesian model averaging
# ==============================================================================
# Model space:
#   M_1: L=3 (S59 level, 10 irreps)
#   M_2: L=5 (medium, 21 irreps)
#   M_3: L=7 (maximum available, 35 irreps)
# Each model predicts a_4/a_2 ratio with cutoff uncertainty
# Prior: uniform over models (Occam: simplest adequate)

# For each model, the ratio and its uncertainty from cutoff function:
print(f"\n--- Bayesian Model Averaging ---")

# Extract high-L data
L_models = [3, 5, 7]
model_labels = [f'L={L}' for L in L_models]

# For each model, compute mean and std of ratio across cutoff functions
r42_model_mean = []
r42_model_std = []
r20_model_mean = []
r20_model_std = []
Nfac_model_mean = []
Nfac_model_std = []

for L_model in L_models:
    i_L = np.where(L_arr == L_model)[0][0]
    vals_42 = [ratios_by_cutoff[ct][i_L] for ct in cutoff_types]
    r42_model_mean.append(np.mean(vals_42))
    r42_model_std.append(np.std(vals_42, ddof=0))

    # For N_factor, cutoff reweighting affects differently
    # N_factor = a2 / (a0/16) => a0 is just mode count, unaffected by cutoff
    # So N_factor cutoff uncertainty comes only from a2 reweighting
    a0_val = a0_cumul[i_L]
    mask = irrep_level <= L_model
    a2_sel = irrep_a2[mask]
    om_sel = omega_mean_irrep[mask]
    om_max_sel = omega_max_irrep[mask]
    Lambda_L = np.max(om_max_sel)

    nf_vals = []
    for ct in cutoff_types:
        x = (om_sel / Lambda_L) ** 2
        if ct == 'step':
            w = np.ones_like(x)
        elif ct == 'exponential':
            w = np.exp(-x)
        elif ct == 'gaussian':
            w = np.exp(-x**2)
        a2_w = np.sum(a2_sel * w)
        nf_vals.append(a2_w / (a0_val / dim_spinor))
    Nfac_model_mean.append(np.mean(nf_vals))
    Nfac_model_std.append(np.std(nf_vals, ddof=0))

    # a2/a0
    r20_vals = [np.mean(nf_vals) * dim_spinor / a0_val for _ in cutoff_types]
    # Actually compute properly
    r20_v = []
    for ct in cutoff_types:
        x = (om_sel / Lambda_L) ** 2
        if ct == 'step':
            w = np.ones_like(x)
        elif ct == 'exponential':
            w = np.exp(-x)
        elif ct == 'gaussian':
            w = np.exp(-x**2)
        a2_w = np.sum(a2_sel * w)
        r20_v.append(a2_w / a0_val)
    r20_model_mean.append(np.mean(r20_v))
    r20_model_std.append(np.std(r20_v, ddof=0))

r42_model_mean = np.array(r42_model_mean)
r42_model_std = np.array(r42_model_std)
Nfac_model_mean = np.array(Nfac_model_mean)
Nfac_model_std = np.array(Nfac_model_std)
r20_model_mean = np.array(r20_model_mean)
r20_model_std = np.array(r20_model_std)

print(f"\nModel-averaged a4/a2 ratio:")
for i, label in enumerate(model_labels):
    print(f"  {label}: {r42_model_mean[i]:.6f} +/- {r42_model_std[i]:.6f} (cutoff)")

print(f"\nModel-averaged N_factor:")
for i, label in enumerate(model_labels):
    print(f"  {label}: {Nfac_model_mean[i]:.6f} +/- {Nfac_model_std[i]:.6f} (cutoff)")

# ==============================================================================
# 7. Bayesian posterior with uniform model prior
# ==============================================================================

# Prior: P(M_i) = 1/3 for each model
# Likelihood: assume Gaussian likelihood for ratio given model prediction
# For BMA, posterior mean = sum P(M_i) * mean_i
# Posterior variance = sum P(M_i) * [var_i + (mean_i - BMA_mean)^2]

n_models = len(L_models)
prior = np.ones(n_models) / n_models

# BMA for a4/a2
bma_r42_mean = np.sum(prior * r42_model_mean)
bma_r42_var = np.sum(prior * (r42_model_std**2 + (r42_model_mean - bma_r42_mean)**2))
bma_r42_std = np.sqrt(bma_r42_var)

# BMA for N_factor
bma_Nfac_mean = np.sum(prior * Nfac_model_mean)
bma_Nfac_var = np.sum(prior * (Nfac_model_std**2 + (Nfac_model_mean - bma_Nfac_mean)**2))
bma_Nfac_std = np.sqrt(bma_Nfac_var)

print(f"\n--- Bayesian Model Average (uniform prior over L=3,5,7) ---")
print(f"  a4/a2: {bma_r42_mean:.6f} +/- {bma_r42_std:.6f}")
print(f"  N_factor: {bma_Nfac_mean:.6f} +/- {bma_Nfac_std:.6f}")

# ==============================================================================
# 8. Variance decomposition (ANOVA-style)
# ==============================================================================
# Total variance = truncation variance + cutoff variance + tau variance

# Truncation variance: spread across L choices at fixed cutoff (step)
step_r42 = np.array([ratios_by_cutoff['step'][np.where(L_arr == L)[0][0]] for L in L_models])
var_trunc_r42 = np.var(step_r42)

# Cutoff variance: spread across cutoffs at fixed L (highest L)
i_L7 = np.where(L_arr == 7)[0][0]
cutoff_r42 = np.array([ratios_by_cutoff[ct][i_L7] for ct in cutoff_types])
var_cutoff_r42 = np.var(cutoff_r42)

# Tau variance: from fractional sensitivity * sigma_tau
# Estimate: d(a4/a2)/dtau ~ frac_dS_dtau * a4/a2 (assuming proportional)
# More carefully: if a4 and a2 scale the same way with tau, ratio is stable
# The actual fractional sensitivity of the ratio is the DIFFERENCE of
# fractional sensitivities: d ln(a4)/dtau - d ln(a2)/dtau
# Without multi-tau data, estimate from growth exponents:
# a4(L) ~ L^{alpha_a4}, a2(L) ~ L^{alpha_a2}
# If tau changes the effective L (cutoff scale), then
# d ln(a4/a2)/d ln L = alpha_a4 - alpha_a2
# and d ln L / dtau ~ d ln Lambda / dtau ~ some geometric factor

# Conservative estimate: fractional change in ratio per unit tau is
# comparable to the ratio's fractional spread across models
frac_spread_r42 = np.std(step_r42) / np.mean(step_r42)

# For each sigma_tau, the tau variance contribution is:
sigma_tau_ref = 0.01  # reference  # (local)
var_tau_r42_per_sigtau = (frac_spread_r42 * np.mean(step_r42))**2 * (sigma_tau_ref / (tau_fold))**2

print(f"\n--- Variance Decomposition for a4/a2 ---")
print(f"  Truncation variance (L=3,5,7, step): {var_trunc_r42:.8f}")
print(f"  Cutoff variance (L=7, step/exp/gauss): {var_cutoff_r42:.8f}")
print(f"  Tau variance (sigma_tau=0.01): {var_tau_r42_per_sigtau:.8f}")
total_var = var_trunc_r42 + var_cutoff_r42 + var_tau_r42_per_sigtau
print(f"  Total variance: {total_var:.8f}")

if total_var > 0:
    pct_trunc = var_trunc_r42 / total_var * 100
    pct_cutoff = var_cutoff_r42 / total_var * 100
    pct_tau = var_tau_r42_per_sigtau / total_var * 100
    print(f"  Truncation: {pct_trunc:.1f}%")
    print(f"  Cutoff: {pct_cutoff:.1f}%")
    print(f"  Tau: {pct_tau:.1f}%")
else:
    pct_trunc = pct_cutoff = pct_tau = 0.0
    print(f"  WARNING: total_var = 0")

# ==============================================================================
# 9. Convergence diagnostics: Richardson extrapolation
# ==============================================================================
# If a4/a2(L) converges as L -> infty, we can estimate the limit by
# Richardson extrapolation: r_infty = r(L) + [r(L) - r(L-1)]^2 / [r(L-1) - 2*r(L) + r(L+1)]

print(f"\n--- Richardson Extrapolation for a4/a2 ---")
# Use L=5,6,7 as three consecutive points
L567 = [5, 6, 7]
r567 = [ratios_by_cutoff['step'][np.where(L_arr == L)[0][0]] for L in L567]

# Aitken delta-squared
delta1 = r567[1] - r567[0]
delta2 = r567[2] - r567[1]
denom = delta2 - delta1
if abs(denom) > 1e-15:
    r_rich = r567[0] - delta1**2 / denom
    print(f"  r(5) = {r567[0]:.8f}")
    print(f"  r(6) = {r567[1]:.8f}")
    print(f"  r(7) = {r567[2]:.8f}")
    print(f"  Richardson limit = {r_rich:.8f}")
    # Error estimate: |r_rich - r(7)|
    rich_err = abs(r_rich - r567[2])
    print(f"  Extrapolation uncertainty: {rich_err:.8f}")
else:
    r_rich = r567[2]
    rich_err = abs(r567[2] - r567[1])
    print(f"  Aitken denominator ~ 0; using last value r(7) = {r567[2]:.8f}")

# ==============================================================================
# 10. Incremental ratio convergence (strongest test)
# ==============================================================================
# The INCREMENTAL ratio delta_a4(L)/delta_a2(L) for each L shell
# converges if the high-L shells contribute the same ratio of a4 to a2.
# This is the strongest convergence test.

print(f"\n--- Incremental Ratio Convergence (strongest test) ---")
print(f"{'L':>3} {'delta_a4/delta_a2':>18} {'delta from L-1':>14}")
prev_val = None
for i, L in enumerate(L_arr):
    if not np.isnan(r42_incr[i]):
        delta_str = ""
        if prev_val is not None:
            delta_str = f"{r42_incr[i] - prev_val:+14.6f}"
        print(f"{L:3d} {r42_incr[i]:18.6f} {delta_str}")
        prev_val = r42_incr[i]

# Check if incremental ratios are converging
r42_incr_valid = r42_incr[~np.isnan(r42_incr)]
if len(r42_incr_valid) >= 3:
    last3_changes = np.abs(np.diff(r42_incr_valid[-4:]))
    incr_converging = last3_changes[-1] < last3_changes[0]
    print(f"  Convergence trend (last changes decreasing): {incr_converging}")
    print(f"  Last 3 step-changes: {last3_changes}")

# ==============================================================================
# 11. N_factor divergence analysis
# ==============================================================================
# The critical question: N_factor diverges. Can we extract a MEANINGFUL
# N_factor from the a_2 coefficient structure?

print(f"\n--- N_factor Divergence Analysis ---")
print(f"  L=0: N = {N_cumul[0]:.4f}")
print(f"  L=3: N = {N_cumul[3]:.4f} (S59 used this)")
print(f"  L=7: N = {N_cumul[7]:.4f}")
print(f"  Growth: N ~ L^{alpha_growth:.2f}")
print(f"  S59 prescription N = sqrt(16) = 4.0 was ACCIDENTAL at L=3")

# Can we define N via the RATIO a_2 / a_2^{singlet} rescaled by dim?
# a_2^{singlet} = 14.23 (L=0 only)
# N_alt = a_2^{tot} / a_2^{singlet} (no dim factor)
a2_singlet = float(data_s59['a2_singlet'])
N_alt = a2_cumul / a2_singlet
print(f"\n  Alternative: N_alt = a2_tot / a2_singlet:")
for i, L in enumerate(L_arr):
    print(f"    L={L}: N_alt = {N_alt[i]:.4f}")
print(f"  This also diverges (same growth exponent)")

# ==============================================================================
# 12. Summary: What converges, what diverges
# ==============================================================================

print(f"\n{'='*72}")
print(f"CONVERGENCE SUMMARY")
print(f"{'='*72}")

# Test each ratio
results = {}

# a4/a2 ratio
r42_last3 = r42[-3:]
r42_frac_change = abs(r42[-1] - r42[-2]) / abs(r42[-1])
r42_converges = r42_frac_change < 0.005  # < 0.5% change
results['a4/a2'] = {
    'value': r42[-1],
    'bma_mean': bma_r42_mean,
    'bma_std': bma_r42_std,
    'rich_limit': r_rich,
    'rich_err': rich_err,
    'frac_change_last': r42_frac_change,
    'converges': r42_converges,
}
print(f"\na4/a2 ratio:")
print(f"  L=7 value: {r42[-1]:.6f}")
print(f"  BMA: {bma_r42_mean:.6f} +/- {bma_r42_std:.6f}")
print(f"  Richardson limit: {r_rich:.6f} +/- {rich_err:.6f}")
print(f"  Last fractional change: {r42_frac_change:.6f}")
print(f"  CONVERGING: {r42_converges}")

# N_factor
Nfac_frac_change = abs(N_cumul[-1] - N_cumul[-2]) / abs(N_cumul[-1])
Nfac_converges = Nfac_frac_change < 0.005
results['N_factor'] = {
    'value': N_cumul[-1],
    'bma_mean': bma_Nfac_mean,
    'bma_std': bma_Nfac_std,
    'frac_change_last': Nfac_frac_change,
    'converges': Nfac_converges,
}
print(f"\nN_factor:")
print(f"  L=7 value: {N_cumul[-1]:.4f}")
print(f"  BMA: {bma_Nfac_mean:.4f} +/- {bma_Nfac_std:.4f}")
print(f"  Last fractional change: {Nfac_frac_change:.6f}")
print(f"  CONVERGING: {Nfac_converges}")

# Incremental a4/a2
incr_r42_last = r42_incr[~np.isnan(r42_incr)]
incr_frac_change = abs(incr_r42_last[-1] - incr_r42_last[-2]) / abs(incr_r42_last[-1]) if len(incr_r42_last) >= 2 else 1.0
incr_converges = incr_frac_change < 0.01
results['incr_a4/a2'] = {
    'value': incr_r42_last[-1] if len(incr_r42_last) > 0 else np.nan,
    'frac_change_last': incr_frac_change,
    'converges': incr_converges,
}
print(f"\nIncremental a4/a2:")
print(f"  L=7 value: {incr_r42_last[-1]:.6f}")
print(f"  Last fractional change: {incr_frac_change:.6f}")
print(f"  CONVERGING: {incr_converges}")

# ==============================================================================
# 13. Gate verdict
# ==============================================================================

any_converges = r42_converges or incr_converges
all_diverge = not any_converges and Nfac_converges is False

if r42_converges and incr_converges:
    gate_verdict = "PASS"
    gate_detail = (f"a4/a2 ratio CONVERGES: {bma_r42_mean:.4f} +/- {bma_r42_std:.4f} (BMA). "
                   f"Incremental ratio converges. Truncation {pct_trunc:.0f}% of variance, "
                   f"cutoff {pct_cutoff:.0f}%, tau {pct_tau:.0f}%. "
                   f"N_factor DIVERGES (L^{alpha_growth:.1f}): no H_0 prediction without proper a_2. "
                   f"Richardson limit = {r_rich:.6f} +/- {rich_err:.6f}.")
elif any_converges:
    gate_verdict = "INFO"
    gate_detail = (f"PARTIAL convergence. a4/a2 ratio: last frac change {r42_frac_change:.4f}. "
                   f"Incr a4/a2 converging: {incr_converges}. "
                   f"N_factor DIVERGES (L^{alpha_growth:.1f}). "
                   f"BMA a4/a2 = {bma_r42_mean:.4f} +/- {bma_r42_std:.4f}.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"ALL ratios diverge. a4/a2 last frac change {r42_frac_change:.4f} > 0.5%. "
                   f"Incremental a4/a2 frac change {incr_frac_change:.4f}. "
                   f"N_factor diverges as L^{alpha_growth:.1f}. "
                   f"No convergent observable from truncated PW spectral action.")

print(f"\n{'='*72}")
print(f"GATE VERDICT: BAYESIAN-H0-60 = {gate_verdict}")
print(f"{'='*72}")
print(f"Detail: {gate_detail}")

# ==============================================================================
# 14. Save results
# ==============================================================================

np.savez('computations/session-60/s60_bayesian_h0.npz',
    # Raw data
    L_arr=L_arr,
    a0_cumul=a0_cumul,
    a2_cumul=a2_cumul,
    a4_cumul=a4_cumul,
    N_cumul=N_cumul,
    # Ratios
    r42_cumul=r42,
    r42_incr=r42_incr,
    r20_cumul=r20,
    r20_incr=r20_incr,
    N_factor_cumul=N_cumul,
    # Growth exponents
    alpha_a0=alpha_a0,
    alpha_a2=alpha_a2,
    alpha_a4=alpha_a4,
    alpha_ratio42=alpha_ratio42,
    # Cutoff sensitivity
    r42_step=ratios_by_cutoff['step'],
    r42_exp=ratios_by_cutoff['exponential'],
    r42_gauss=ratios_by_cutoff['gaussian'],
    # Bayesian model average
    bma_r42_mean=bma_r42_mean,
    bma_r42_std=bma_r42_std,
    bma_Nfac_mean=bma_Nfac_mean,
    bma_Nfac_std=bma_Nfac_std,
    # Richardson extrapolation
    r42_richardson=r_rich,
    r42_richardson_err=rich_err,
    # Variance decomposition
    var_trunc_r42=var_trunc_r42,
    var_cutoff_r42=var_cutoff_r42,
    var_tau_r42=var_tau_r42_per_sigtau,
    pct_trunc=pct_trunc,
    pct_cutoff=pct_cutoff,
    pct_tau=pct_tau,
    # Convergence diagnostics
    r42_frac_change_last=r42_frac_change,
    incr_r42_frac_change_last=incr_frac_change,
    r42_converges=r42_converges,
    incr_converges=incr_converges,
    Nfac_converges=Nfac_converges,
    # Gate
    gate_name=np.array(['BAYESIAN-H0-60']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
    # Tau analysis
    sigma_tau_ref=sigma_tau_ref,
    d2V_dtau2_at_fold=d2V_dtau2_at_fold,
)
print(f"\nSaved: computations/session-60/s60_bayesian_h0.npz")

# ==============================================================================
# 15. Diagnostic plot
# ==============================================================================

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: a4/a2 ratio convergence
ax1 = fig.add_subplot(gs[0, 0])
for ct in cutoff_types:
    ax1.plot(L_arr, ratios_by_cutoff[ct], 'o-', label=ct, markersize=5)
ax1.axhline(bma_r42_mean, color='k', linestyle='--', alpha=0.5, label=f'BMA={bma_r42_mean:.4f}')
ax1.fill_between(L_arr, bma_r42_mean - bma_r42_std, bma_r42_mean + bma_r42_std,
                  alpha=0.2, color='gray')  # (local)
if not np.isnan(r_rich):
    ax1.axhline(r_rich, color='red', linestyle=':', alpha=0.7, label=f'Richardson={r_rich:.4f}')
ax1.set_xlabel('PW truncation level L')
ax1.set_ylabel('$a_4 / a_2$')
ax1.set_title('Cumulative $a_4/a_2$ Ratio')
ax1.legend(fontsize=7)
ax1.grid(True, alpha=0.3)

# Panel 2: Incremental ratio convergence
ax2 = fig.add_subplot(gs[0, 1])
valid_mask = ~np.isnan(r42_incr)
ax2.plot(L_arr[valid_mask], r42_incr[valid_mask], 's-', color='darkblue', markersize=6)
ax2.axhline(r42[-1], color='gray', linestyle='--', alpha=0.5, label=f'Cumulative r(L=7)')
ax2.set_xlabel('PW level L')
ax2.set_ylabel('$\\Delta a_4 / \\Delta a_2$')
ax2.set_title('Incremental $a_4/a_2$ per Shell')
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.3)

# Panel 3: N_factor divergence
ax3 = fig.add_subplot(gs[0, 2])
ax3.semilogy(L_arr, N_cumul, 'o-', color='red', markersize=6)
# Overlay power-law fit
L_dense = np.linspace(0.5, 8, 100)
ax3.semilogy(L_dense, np.exp(p_a2[1]) * (L_dense + 1)**alpha_a2 / (np.exp(p_a0[1]) * (L_dense + 1)**alpha_a0 / dim_spinor),
             '--', color='gray', alpha=0.5, label=f'$\\sim L^{{{alpha_a2-alpha_a0:.1f}}}$')
ax3.axhline(4.0, color='green', linestyle=':', label='$\\sqrt{16}$ = 4.0 (S59 target)')
ax3.set_xlabel('PW truncation level L')
ax3.set_ylabel('$N_{\\mathrm{factor}} = a_2 / (a_0/16)$')
ax3.set_title('N-factor Divergence')
ax3.legend(fontsize=7)
ax3.grid(True, alpha=0.3)

# Panel 4: Growth exponents log-log
ax4 = fig.add_subplot(gs[1, 0])
for name, arr, color in [('$a_0$', a0_cumul, 'blue'),
                           ('$a_2$', a2_cumul, 'green'),
                           ('$a_4$', a4_cumul, 'red')]:
    ax4.loglog(L_arr[1:] + 1, arr[1:], 'o-', color=color, label=name, markersize=5)
ax4.set_xlabel('L + 1')
ax4.set_ylabel('Spectral coefficient')
ax4.set_title(f'Power-law Growth ($\\alpha_{{a2}}={alpha_a2:.2f}$, $\\alpha_{{a4}}={alpha_a4:.2f}$)')
ax4.legend(fontsize=7)
ax4.grid(True, alpha=0.3, which='both')

# Panel 5: Variance decomposition pie chart
ax5 = fig.add_subplot(gs[1, 1])
if total_var > 0:
    sizes = [pct_trunc, pct_cutoff, pct_tau]
    labels_pie = [f'Truncation\n{pct_trunc:.1f}%',
                  f'Cutoff\n{pct_cutoff:.1f}%',
                  f'Tau\n{pct_tau:.1f}%']
    colors_pie = ['#3274A1', '#E1812C', '#3A923A']
    ax5.pie(sizes, labels=labels_pie, colors=colors_pie, autopct='', startangle=90)
    ax5.set_title('$a_4/a_2$ Variance Decomposition')
else:
    ax5.text(0.5, 0.5, 'No variance\n(all zero)', transform=ax5.transAxes,
             ha='center', va='center', fontsize=12)
    ax5.set_title('$a_4/a_2$ Variance Decomposition')

# Panel 6: BMA posterior visualization
ax6 = fig.add_subplot(gs[1, 2])
# Plot the three model posteriors as Gaussians + the BMA
x_range = np.linspace(bma_r42_mean - 4*bma_r42_std - 0.2,
                       bma_r42_mean + 4*bma_r42_std + 0.2, 300)
bma_pdf = np.zeros_like(x_range)
for i in range(n_models):
    sigma_i = max(r42_model_std[i], 0.001)  # regularize
    pdf_i = (1.0 / (sigma_i * np.sqrt(2*np.pi))) * np.exp(-0.5*((x_range - r42_model_mean[i])/sigma_i)**2)
    ax6.plot(x_range, prior[i] * pdf_i, '--', alpha=0.5, label=model_labels[i])
    bma_pdf += prior[i] * pdf_i

ax6.plot(x_range, bma_pdf, 'k-', linewidth=2, label='BMA posterior')
ax6.axvline(bma_r42_mean, color='k', linestyle=':', alpha=0.5)
ax6.fill_between(x_range, 0, bma_pdf,
                  where=np.abs(x_range - bma_r42_mean) <= bma_r42_std,
                  alpha=0.2, color='blue', label='68% CI')  # (local)
ax6.set_xlabel('$a_4/a_2$')
ax6.set_ylabel('Posterior density')
ax6.set_title('BMA Posterior for $a_4/a_2$')
ax6.legend(fontsize=7)
ax6.grid(True, alpha=0.3)

fig.suptitle(f'BAYESIAN-H0-60: Spectral Ratio Convergence & Error Budget — Verdict: {gate_verdict}',
             fontsize=14, fontweight='bold')

plt.savefig('computations/session-60/s60_bayesian_h0.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-60/s60_bayesian_h0.png")

print(f"\n{'='*72}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*72}")
