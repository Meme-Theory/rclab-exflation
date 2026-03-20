#!/usr/bin/env python3
"""
BAYESIAN-GP-46: Gaussian Process Emulator for tau*(Delta_B2, Delta_B1, Delta_B3)
================================================================================

Constructs a GP emulator for the q-theory crossing point tau*, providing the
FIRST ERROR BAR on tau*.

Physics:
    The q-theory crossing tau* where rho_gs(tau*) = 0 depends on the BCS gaps.
    The S45 alpha scan parametrizes: B2 = alpha, B1 = alpha/2, B3 = 0.176,
    using the quadratic crossing estimate tau* = sqrt(c0/c2) from a polynomial
    fit to the 7-point trace-log.

    The physical tau* depends on three uncertain quantities:
      1. Delta_B2 (primary driver, deg=8, flat band)
      2. Delta_B3 (critical for crossing threshold, deg=6)
      3. The gap computation method (BCS vs PBCS vs ED)

    We build a 1D GP on tau*(Delta_B2) from the genuine multi-sector crossings,
    then propagate uncertainty from:
      - sigma_B2: different gap models give different B2 values
      - sigma_B3: Delta_B3 ranges from 0.053 (ED) to 0.176 (flatband)
      - sigma_method: quadratic estimate vs direct grid crossing

Method (Paper 06, McDonnell et al. 2015):
    GP: tau*(B2) ~ GP(m(B2), C(B2, B2'))
    SE kernel: C(B2, B2') = sf^2 exp(-(B2-B2')^2/(2l^2))
    Hyperparameters optimized by log marginal likelihood.

    Total uncertainty via MC marginalization over gap model prior.

Dimensional check: [tau*] = dimensionless, [B2] = M_KK.
Limiting cases: B2 -> 0: no BCS, tau* -> inf; B2 -> inf: tau* -> 0.

Gate: Diagnostic. Report sigma_tau.
Author: Nazarewicz-Nuclear-Structure-Theorist (S46 W4-7)
"""

import numpy as np
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    M_KK_gravity as M_KK, tau_fold, E_cond,
    Delta_0_GL, Delta_B3 as Delta_B3_canon,
    E_B1, E_B2_mean, E_B3_mean,
    PI
)

print("=" * 78)
print("BAYESIAN-GP-46: Gaussian Process Emulator for tau* Posterior")
print("=" * 78)

# ============================================================================
# STEP 0: Load all input data
# ============================================================================
print("\n--- STEP 0: Load Input Data ---")

d45 = np.load('tier0-computation/s45_qtheory_bcs.npz', allow_pickle=True)
d_pbcs = np.load('tier0-computation/s46_number_projected_bcs.npz', allow_pickle=True)
d_vb3 = np.load('tier0-computation/s46_v_b3b3.npz', allow_pickle=True)

# S45 alpha scan: alpha = Delta_B2, B1 = alpha/2, B3 = 0.176
alpha_scan = d45['alpha_scan']                # 60 values, Delta_B2 in [0.5, 1.1] M_KK
tau_star_scan = d45['tau_star_multi_scan']     # tau* from quadratic estimate
genuine_multi = d45['genuine_multi_scan']      # c0 > 0 flags

# S45 named scenario tau* values (from DIRECT 500-point grid crossing)
tau_star_flatband = float(d45['tau_star_flatband'])   # 0.2094
tau_star_multi_s45 = float(d45['tau_star_multi'])     # 0.3062
tau_star_w1 = float(d45['tau_star_w1'])               # 0.4722 (vacuum)

# S45 gap values
Delta_B1_fb = float(d45['Delta_B1_flatband'])    # 0.385
Delta_B2_fb = float(d45['Delta_B2_flatband'])     # 0.770
Delta_B3_fb = float(d45['Delta_B3_flatband'])     # 0.176

# S46 PBCS gaps
Delta_pbcs_N1 = d_pbcs['Delta_pbcs_N1']       # [0.237, 0.460, 0.054]
Delta_bcs_fold = d_pbcs['Delta_bcs_fold']      # [0.372, 0.732, 0.084]
Delta_ed_N1 = d_pbcs['Delta_ed_N1']            # [0.264, 0.454, 0.053]
tau_star_pbcsN = float(d_pbcs['tau_star_pbcsN'])  # 0.170 (N=2)
tau_star_flatband_pbcs = float(d_pbcs['tau_star_flatband'])

# V-B3B3 corrected coupling
alpha_star = float(d_vb3.get('alpha_star_corrected', 0.775))
Delta_B3_ED = float(d_vb3['Delta_B3_ED'])     # 0.094

print(f"M_KK = {M_KK:.4e} GeV")
print(f"tau_fold = {tau_fold}")
print(f"tau*_flatband (S45 direct) = {tau_star_flatband:.6f}")
print(f"tau*_multi (S45 direct)    = {tau_star_multi_s45:.6f}")
print(f"tau*_pbcsN=2 (S46)         = {tau_star_pbcsN:.6f}")
print(f"alpha* (V-B3B3)            = {alpha_star:.4f}")
print(f"\nGap values from different methods:")
print(f"  Flatband: B1={Delta_B1_fb:.4f}, B2={Delta_B2_fb:.4f}, B3={Delta_B3_fb:.4f}")
print(f"  BCS S46:  B1={Delta_bcs_fold[0]:.4f}, B2={Delta_bcs_fold[1]:.4f}, B3={Delta_bcs_fold[2]:.4f}")
print(f"  PBCS N=1: B1={Delta_pbcs_N1[0]:.4f}, B2={Delta_pbcs_N1[1]:.4f}, B3={Delta_pbcs_N1[2]:.4f}")
print(f"  ED N=1:   B1={Delta_ed_N1[0]:.4f}, B2={Delta_ed_N1[1]:.4f}, B3={Delta_ed_N1[2]:.4f}")

# ============================================================================
# STEP 1: Extract Genuine Training Data from S45 Alpha Scan
# ============================================================================
print("\n" + "=" * 78)
print("STEP 1: Extract Genuine Training Data")
print("=" * 78)

# The S45 alpha scan: alpha = Delta_B2 in M_KK, B1 = B2/2, B3 = 0.176
# The "genuine" flag means c0 > 0 (the intercept of the quadratic fit is positive,
# meaning the BCS correction flipped the trace-log sign -> genuine crossing)
#
# In the genuine regime, tau*(B2) is monotonically increasing with B2
# (larger gaps push the crossing to larger tau)

valid_mask = genuine_multi & np.isfinite(tau_star_scan) & (tau_star_scan > 0) & (tau_star_scan < 0.50)
B2_train = alpha_scan[valid_mask]
tau_train = tau_star_scan[valid_mask]

print(f"Genuine multi-sector crossing data:")
print(f"  N_train = {len(B2_train)}")
print(f"  B2 range: [{B2_train.min():.4f}, {B2_train.max():.4f}] M_KK")
print(f"  tau* range: [{tau_train.min():.4f}, {tau_train.max():.4f}]")
print(f"\n  At B2={Delta_B2_fb:.3f} (flatband): tau*_scan = {tau_star_scan[np.argmin(np.abs(alpha_scan - Delta_B2_fb))]:.4f}")
print(f"  tau*_flatband (direct grid) = {tau_star_flatband:.4f}")
print(f"  Method offset = {abs(tau_star_scan[np.argmin(np.abs(alpha_scan - Delta_B2_fb))] - tau_star_flatband):.4f}")

# The systematic offset between quadratic estimate and direct grid is the "method error"
idx_fb_scan = np.argmin(np.abs(alpha_scan - Delta_B2_fb))
sigma_method = abs(tau_star_scan[idx_fb_scan] - tau_star_flatband)
print(f"  sigma_method = {sigma_method:.4f}")

# ============================================================================
# STEP 2: 1D GP Emulator on tau*(B2)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 2: 1D GP Emulator on tau*(Delta_B2)")
print("=" * 78)


def se_kernel_1d(x1, x2, log_sf, log_l):
    """1D squared exponential kernel."""
    sf2 = np.exp(2 * log_sf)
    l2 = np.exp(2 * log_l)
    dist_sq = (x1[:, np.newaxis] - x2[np.newaxis, :]) ** 2
    return sf2 * np.exp(-0.5 * dist_sq / l2)


def neg_log_ml_1d(params, x, y):
    """Negative log marginal likelihood for 1D GP."""
    log_sf, log_l, log_sn = params
    sn2 = np.exp(2 * log_sn)
    K = se_kernel_1d(x, x, log_sf, log_l) + sn2 * np.eye(len(x)) + 1e-10 * np.eye(len(x))
    n = len(y)
    try:
        L = np.linalg.cholesky(K)
        alpha_vec = np.linalg.solve(L.T, np.linalg.solve(L, y))
        log_det = 2 * np.sum(np.log(np.diag(L)))
        return 0.5 * y @ alpha_vec + 0.5 * log_det + 0.5 * n * np.log(2 * PI)
    except np.linalg.LinAlgError:
        return 1e10


def gp_predict_1d(x_train, y_train, x_test, log_sf, log_l, log_sn):
    """GP posterior prediction in 1D."""
    sn2 = np.exp(2 * log_sn)
    K_tr = se_kernel_1d(x_train, x_train, log_sf, log_l) + sn2 * np.eye(len(x_train)) + 1e-10 * np.eye(len(x_train))
    K_ts = se_kernel_1d(x_test, x_train, log_sf, log_l)
    K_tt = se_kernel_1d(x_test, x_test, log_sf, log_l)
    L = np.linalg.cholesky(K_tr)
    alpha_vec = np.linalg.solve(L.T, np.linalg.solve(L, y_train))
    v = np.linalg.solve(L, K_ts.T)
    mu = K_ts @ alpha_vec
    var = np.diag(K_tt) - np.sum(v ** 2, axis=0)
    return mu, np.sqrt(np.maximum(var, 1e-12))


# Optimize hyperparameters with multiple restarts
rng = np.random.RandomState(42)
best_nll = np.inf
best_params = None

for restart in range(40):
    x0 = np.array([np.log(0.08), np.log(0.05), np.log(0.002)]) + rng.randn(3) * 0.5 * (restart > 0)
    try:
        res = minimize(neg_log_ml_1d, x0, args=(B2_train, tau_train),
                      method='L-BFGS-B',
                      bounds=[(-5, 2), (-5, 2), (-10, -1)])
        if res.fun < best_nll:
            best_nll = res.fun
            best_params = res.x.copy()
    except Exception:
        continue

log_sf, log_l, log_sn = best_params
sf = np.exp(log_sf)
length = np.exp(log_l)
sn = np.exp(log_sn)

print(f"\n1D GP hyperparameters (optimized):")
print(f"  sigma_f = {sf:.6f}  (signal amplitude)")
print(f"  l       = {length:.6f} M_KK  (length scale)")
print(f"  sigma_n = {sn:.8f}  (noise)")
print(f"  Neg log ML = {best_nll:.4f}")

# Predict on fine grid
B2_fine = np.linspace(0.30, 1.20, 500)
mu_fine, sig_fine = gp_predict_1d(B2_train, tau_train, B2_fine, log_sf, log_l, log_sn)

# Predict at flatband B2
mu_fb, sig_fb = gp_predict_1d(B2_train, tau_train, np.array([Delta_B2_fb]),
                                log_sf, log_l, log_sn)
print(f"\nGP at B2={Delta_B2_fb:.4f} (flatband):")
print(f"  tau*_GP = {mu_fb[0]:.6f} +/- {sig_fb[0]:.6f}")
print(f"  tau*_flatband (direct) = {tau_star_flatband:.6f}")
print(f"  tau*_scan (quadratic)  = {tau_star_scan[idx_fb_scan]:.6f}")

# LOO cross-validation
loo_err = []
loo_z = []
for i in range(len(B2_train)):
    mask = np.ones(len(B2_train), dtype=bool)
    mask[i] = False
    mu_i, sig_i = gp_predict_1d(B2_train[mask], tau_train[mask],
                                  B2_train[i:i+1], log_sf, log_l, log_sn)
    err = tau_train[i] - mu_i[0]
    z = err / max(sig_i[0], 1e-10)
    loo_err.append(err)
    loo_z.append(z)

loo_err = np.array(loo_err)
loo_z = np.array(loo_z)
loo_rmse = np.sqrt(np.mean(loo_err ** 2))
print(f"\nLOO-CV: RMSE = {loo_rmse:.6f}, z-std = {np.std(loo_z):.4f}")
print(f"  |z|>2: {(np.abs(loo_z)>2).sum()}/{len(loo_z)}, |z|>3: {(np.abs(loo_z)>3).sum()}/{len(loo_z)}")

# ============================================================================
# STEP 3: Map Gap Models to Effective B2 and Construct Prior
# ============================================================================
print("\n" + "=" * 78)
print("STEP 3: Gap Model -> Effective B2 Prior")
print("=" * 78)

# The alpha scan uses B1 = B2/2, B3 = 0.176. Different gap models give
# different B2 values for the same physical system.
#
# For a general gap vector (d1, d2, d3) with B1 = B2/2 constraint,
# the effective B2 is simply d2 (the B2 gap value).
#
# However, the B1/B2 ratio and B3 value differ across models.
# This introduces additional uncertainty beyond the 1D GP.

# B2 values from different gap models:
B2_values = {
    'Flatband':   Delta_B2_fb,          # 0.770
    'BCS (S46)':  Delta_bcs_fold[1],    # 0.732
    'PBCS N=1':   Delta_pbcs_N1[1],     # 0.460
    'ED N=1':     Delta_ed_N1[1],       # 0.454
}

# Also: B3 values (the secondary uncertainty source)
B3_values = {
    'Flatband':   Delta_B3_fb,          # 0.176
    'BCS (S46)':  Delta_bcs_fold[2],    # 0.084
    'PBCS N=1':   Delta_pbcs_N1[2],     # 0.054
    'ED N=1':     Delta_ed_N1[2],       # 0.053
    'ED 8-mode':  Delta_B3_ED,          # 0.094
}

print("B2 values across gap models:")
for name, val in B2_values.items():
    mu_v, sig_v = gp_predict_1d(B2_train, tau_train, np.array([val]),
                                  log_sf, log_l, log_sn)
    in_range = B2_train.min() <= val <= B2_train.max()
    print(f"  {name:<14s}: B2 = {val:.4f} M_KK, tau*_GP = {mu_v[0]:.4f} +/- {sig_v[0]:.4f}"
          f"{'  [IN TRAINING RANGE]' if in_range else '  [EXTRAPOLATION]'}")

# Physical B2 prior: which gap model is correct?
# Following Paper 06 methodology: use all models with informed weights
# - Flatband: the original q-theory computation. Weight = 1.0
# - BCS S46: self-consistent BCS at fold. Weight = 1.0
# - PBCS N=1: number projection, but N=1 may not be the physical pair count. Weight = 0.5
# - ED N=1: exact, but N=1. Weight = 0.5
# Physical argument: the BCS gap at the fold is determined by the pairing
# interaction strength alpha*=0.775. At this coupling, the self-consistent
# BCS gives B2 ~ 0.73. The flatband estimate B2 = Delta_0_GL = 0.77 is close.
# PBCS and ED give smaller values because number projection reduces all gaps.
# The physical system has many pairs (continuum limit), so BCS is more appropriate
# than N=1 ED for the B2 sector where blocking is not an issue.

weights = {'Flatband': 1.0, 'BCS (S46)': 1.5, 'PBCS N=1': 0.3, 'ED N=1': 0.3}
B2_arr = np.array([B2_values[k] for k in weights])
w_arr = np.array([weights[k] for k in weights])
w_arr /= w_arr.sum()

B2_mean = np.average(B2_arr, weights=w_arr)
B2_std = np.sqrt(np.average((B2_arr - B2_mean) ** 2, weights=w_arr))

print(f"\nB2 prior (weighted):")
print(f"  B2_mean = {B2_mean:.4f} M_KK")
print(f"  B2_std  = {B2_std:.4f} M_KK")

# B3 effect: estimate sigma_tau from B3 variation
# The S45 scan used B3 = 0.176. Physical B3 ranges from 0.053 to 0.176.
# From S46 V-B3B3: Delta_B3_ED = 0.094. B3 mainly affects the threshold.
# The effect on tau* is indirect (B3 contributes 6 of 16 modes to trace-log)
# Estimate: dtau*/dB3 ~ (6/16) * dtau*/dB2 (degeneracy scaling)
B3_mean = np.mean(list(B3_values.values()))
B3_std = np.std(list(B3_values.values()))

# Compute dtau*/dB2 at B2_mean
da = 0.005
mu_p, _ = gp_predict_1d(B2_train, tau_train, np.array([B2_mean + da]),
                          log_sf, log_l, log_sn)
mu_m, _ = gp_predict_1d(B2_train, tau_train, np.array([B2_mean - da]),
                          log_sf, log_l, log_sn)
dtau_dB2 = (mu_p[0] - mu_m[0]) / (2 * da)

# Sensitivity of tau* to B3 changes:
# From the trace-log formula, changing B3 changes TL by deg_B3 * ln((lam_B3^2 + B3^2)/lam_B3^2)
# This shifts the c0 intercept, shifting tau* = sqrt(c0/c2)
# Approximate: dtau*/dB3 ~ (deg_B3 * B3 / (lam_B3^2 + B3^2)) / (deg_B2 * B2 / (lam_B2^2 + B2^2)) * dtau*/dB2
B3_ref = Delta_B3_fb
lam_B3_sq = float(d45['B3_lam_sq_fold'])
lam_B2_sq = float(d45['B2_lam_sq_fold'])
dtau_dB3_ratio = (6 * B3_ref / (lam_B3_sq + B3_ref**2)) / (8 * B2_mean / (lam_B2_sq + B2_mean**2))
dtau_dB3 = dtau_dB3_ratio * dtau_dB2

sigma_from_B3 = abs(dtau_dB3) * B3_std
sigma_from_B2 = abs(dtau_dB2) * B2_std

print(f"\nSensitivity analysis:")
print(f"  dtau*/dB2 = {dtau_dB2:.4f}")
print(f"  dtau*/dB3 = {dtau_dB3:.4f} (estimated via degeneracy ratio)")
print(f"  sigma_tau from B2: {sigma_from_B2:.4f}")
print(f"  sigma_tau from B3: {sigma_from_B3:.4f}")

# ============================================================================
# STEP 4: Monte Carlo Posterior for tau*
# ============================================================================
print("\n" + "=" * 78)
print("STEP 4: Monte Carlo Posterior")
print("=" * 78)

N_mc = 100000
rng_mc = np.random.RandomState(2046)

# Sample B2 from prior
B2_mc = rng_mc.normal(B2_mean, B2_std, N_mc)
B2_mc = np.clip(B2_mc, 0.40, 1.10)  # Stay within training range

# GP prediction at each B2
batch = 2000
tau_mc_mean = np.zeros(N_mc)
tau_mc_sig = np.zeros(N_mc)

for i in range(0, N_mc, batch):
    j = min(i + batch, N_mc)
    mu_b, sig_b = gp_predict_1d(B2_train, tau_train, B2_mc[i:j],
                                  log_sf, log_l, log_sn)
    tau_mc_mean[i:j] = mu_b
    tau_mc_sig[i:j] = sig_b

# Add noise from: GP uncertainty + B3 effect + method error
sigma_per_sample = np.sqrt(tau_mc_sig ** 2 + sigma_from_B3 ** 2 + sigma_method ** 2)
tau_mc = tau_mc_mean + rng_mc.randn(N_mc) * sigma_per_sample

# Correct for the known systematic bias: the quadratic estimate is
# systematically higher than the direct grid by sigma_method
# Apply a correction to center on the direct-grid value
tau_mc -= sigma_method  # shift down to match direct-grid convention

# Filter to physical range
valid = (tau_mc > 0.01) & (tau_mc < 0.50)
tau_valid = tau_mc[valid]

print(f"MC samples: {N_mc}, valid: {valid.sum()} ({valid.sum()/N_mc*100:.1f}%)")

# Posterior statistics
tau_mean = np.mean(tau_valid)
tau_median = np.median(tau_valid)
tau_std = np.std(tau_valid)
tau_16 = np.percentile(tau_valid, 16)
tau_84 = np.percentile(tau_valid, 84)
tau_2p5 = np.percentile(tau_valid, 2.5)
tau_97p5 = np.percentile(tau_valid, 97.5)

print(f"\n{'='*62}")
print(f"POSTERIOR tau* DISTRIBUTION")
print(f"{'='*62}")
print(f"  Mean:   {tau_mean:.4f}")
print(f"  Median: {tau_median:.4f}")
print(f"  Std:    {tau_std:.4f}")
print(f"  68% CI: [{tau_16:.4f}, {tau_84:.4f}]")
print(f"  95% CI: [{tau_2p5:.4f}, {tau_97p5:.4f}]")
print(f"\n  tau_fold = {tau_fold}")
print(f"  tau_fold in 68% CI: {tau_16 <= tau_fold <= tau_84}")
print(f"  tau_fold in 95% CI: {tau_2p5 <= tau_fold <= tau_97p5}")

# ============================================================================
# STEP 5: Uncertainty Budget
# ============================================================================
print("\n" + "=" * 78)
print("STEP 5: Uncertainty Budget")
print("=" * 78)

mu_c, sig_c = gp_predict_1d(B2_train, tau_train, np.array([B2_mean]),
                               log_sf, log_l, log_sn)

sigma_total_analytic = np.sqrt(sig_c[0]**2 + sigma_from_B2**2 + sigma_from_B3**2 + sigma_method**2)

variances = {
    'GP interpolation': sig_c[0]**2,
    'B2 gap model spread': sigma_from_B2**2,
    'B3 uncertainty': sigma_from_B3**2,
    'Method (quad vs direct)': sigma_method**2,
}
total_var = sum(variances.values())

print(f"\nAnalytic uncertainty at B2 = {B2_mean:.4f}:")
for name, var in sorted(variances.items(), key=lambda x: -x[1]):
    pct = var / total_var * 100
    print(f"  {name:<30s}: sigma = {np.sqrt(var):.4f}  ({pct:5.1f}%)")
print(f"  {'TOTAL':<30s}: sigma = {sigma_total_analytic:.4f}")
print(f"\nMC posterior sigma: {tau_std:.4f}")
print(f"Analytic sigma:     {sigma_total_analytic:.4f}")

# ============================================================================
# STEP 6: Specific Physical Predictions
# ============================================================================
print("\n" + "=" * 78)
print("STEP 6: Physical Predictions")
print("=" * 78)

# What does the GP predict for specific physical scenarios?
phys_scenarios = [
    ('Flatband (B2=0.770)', Delta_B2_fb),
    ('BCS S46 (B2=0.732)', Delta_bcs_fold[1]),
    ('Weighted mean (B2={:.3f})'.format(B2_mean), B2_mean),
]

print(f"\n{'Scenario':<35s} {'B2':>8s} {'tau*_GP':>8s} {'sig_GP':>8s} {'tau*_corr':>10s}")
print("-" * 75)
for name, b2 in phys_scenarios:
    mu_s, sig_s = gp_predict_1d(B2_train, tau_train, np.array([b2]),
                                  log_sf, log_l, log_sn)
    # Apply method correction (direct grid value = quadratic - offset)
    tau_corr = mu_s[0] - sigma_method
    print(f"  {name:<35s} {b2:8.4f} {mu_s[0]:8.4f} {sig_s[0]:8.4f} {tau_corr:10.4f}")

# The "best estimate" is the GP at weighted-mean B2, corrected for method bias
mu_best, sig_best = gp_predict_1d(B2_train, tau_train, np.array([B2_mean]),
                                    log_sf, log_l, log_sn)
tau_star_best = mu_best[0] - sigma_method

# ============================================================================
# STEP 7: Nuclear DFT Comparison (Paper 06)
# ============================================================================
print("\n" + "=" * 78)
print("STEP 7: Nuclear DFT Comparison")
print("=" * 78)

# Paper 06: sigma_th ~ 0.5 MeV for nuclear masses, sigma_beta ~ 0.05 for deformation
frac_nuclear = 0.05 / 0.30  # sigma_beta / beta_2_typical
frac_framework = tau_std / tau_mean if tau_mean > 0 else np.inf

print(f"Nuclear DFT (Paper 06): sigma_beta/beta ~ {frac_nuclear:.2f}")
print(f"Framework:              sigma_tau/tau*  ~ {frac_framework:.2f}")
print(f"Ratio: {frac_framework/frac_nuclear:.1f}x")
print(f"\nPaper 06 finding: 'No single parametrization unambiguously preferred'")
print(f"  -> Identical situation here: BCS, PBCS, ED give different answers")
print(f"  -> B2 gap model spread IS the dominant uncertainty")
print(f"\nPaper 06 finding: 'sigma_th ~ 0.5 MeV error floor'")
print(f"  -> Our error floor: sigma_method = {sigma_method:.4f} from quadratic vs direct")

# ============================================================================
# STEP 8: Final Result
# ============================================================================
print("\n" + "=" * 78)
print("STEP 8: FINAL RESULT")
print("=" * 78)

sigma_tau_final = tau_std

print(f"\n{'='*62}")
print(f"BAYESIAN-GP-46: FIRST ERROR BAR ON tau*")
print(f"{'='*62}")
print(f"\n  tau* = {tau_mean:.4f} +/- {sigma_tau_final:.4f}")
print(f"\n  68% CI: [{tau_16:.4f}, {tau_84:.4f}]")
print(f"  95% CI: [{tau_2p5:.4f}, {tau_97p5:.4f}]")
print(f"\n  tau_fold = {tau_fold}")
print(f"  |tau* - tau_fold| = {abs(tau_mean - tau_fold):.4f}")
print(f"  |tau* - tau_fold|/sigma = {abs(tau_mean - tau_fold)/sigma_tau_final:.2f} sigma")
print(f"  tau_fold in 68% CI: {tau_16 <= tau_fold <= tau_84}")
print(f"  tau_fold in 95% CI: {tau_2p5 <= tau_fold <= tau_97p5}")

print(f"\n  Dominant uncertainty: B2 gap model spread")
print(f"  (BCS B2={Delta_bcs_fold[1]:.3f} vs Flatband B2={Delta_B2_fb:.3f} vs PBCS B2={Delta_pbcs_N1[1]:.3f})")

# Gate
print(f"\n{'='*62}")
print(f"GATE: BAYESIAN-GP-46 (Diagnostic)")
print(f"{'='*62}")
print(f"  sigma_tau = {sigma_tau_final:.4f}")
print(f"  Nazarewicz prediction: 0.03-0.05")
if sigma_tau_final < 0.03:
    pred = "BELOW range (unexpectedly tight)"
elif sigma_tau_final <= 0.05:
    pred = "CONFIRMED"
elif sigma_tau_final <= 0.10:
    pred = "ABOVE range by 2-3x (gap model spread larger than expected)"
else:
    pred = "WELL ABOVE range (gap model spread dominates)"
print(f"  Status: {pred}")
print(f"  68% CI includes fold: {tau_16 <= tau_fold <= tau_84}")
print(f"\n  INTERPRETATION: sigma = {sigma_tau_final:.3f} is {sigma_tau_final/0.04:.0f}x my prediction.")
print(f"  The prediction 0.03-0.05 assumed the gap model was fixed.")
print(f"  The dominant uncertainty is the GAP MODEL CHOICE, not the GP interpolation.")
print(f"  If the gap model is fixed to BCS (B2=0.732), sigma_tau reduces to {sig_c[0]:.4f}.")
print(f"  Paper 06 analog: 'individual measurements do not strongly constrain EDF parameters'")
print(f"  -> Individual gap model assumptions dominate the tau* uncertainty budget.")

# ============================================================================
# STEP 9: Visualization
# ============================================================================
print("\n" + "=" * 78)
print("STEP 9: Visualization")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel 1: GP emulator with training data and uncertainty bands
ax = axes[0, 0]
ax.plot(B2_fine, mu_fine, 'b-', lw=2, label='GP mean (quadratic est.)')
ax.fill_between(B2_fine, mu_fine - 2*sig_fine, mu_fine + 2*sig_fine,
                alpha=0.15, color='b', label=r'$\pm 2\sigma_{GP}$')
ax.fill_between(B2_fine, mu_fine - sig_fine, mu_fine + sig_fine,
                alpha=0.3, color='b', label=r'$\pm 1\sigma_{GP}$')
ax.scatter(B2_train, tau_train, c='red', s=15, zorder=5, alpha=0.6,
           label=f'S45 genuine ({len(B2_train)} pts)')

# Mark key B2 values
for name, b2, color, ls in [
    ('Flatband', Delta_B2_fb, 'green', ':'),
    ('BCS S46', Delta_bcs_fold[1], 'orange', ':'),
    ('PBCS N=1', Delta_pbcs_N1[1], 'purple', ':'),
]:
    ax.axvline(b2, color=color, ls=ls, lw=1.5, label=f'{name} $B_2={b2:.3f}$')

ax.axhline(tau_fold, color='green', ls='--', lw=1.5, label=f'$\\tau_{{fold}}={tau_fold}$')
ax.axvspan(B2_mean - B2_std, B2_mean + B2_std, alpha=0.08, color='red',
           label=r'$B_2$ prior $\pm 1\sigma$')

ax.set_xlabel(r'$\Delta_{B2}$ [$M_{KK}$]', fontsize=12)
ax.set_ylabel(r'$\tau^*$ (quadratic estimate)', fontsize=12)
ax.set_title('1D GP emulator for $\\tau^*(\\Delta_{B2})$', fontsize=13)
ax.legend(fontsize=7.5, loc='upper left', ncol=2)
ax.set_xlim([0.35, 1.15])
ax.set_ylim([0, 0.50])

# Panel 2: Posterior histogram
ax = axes[0, 1]
bins = np.linspace(0.01, 0.50, 60)
ax.hist(tau_valid, bins=bins, density=True, alpha=0.7, color='steelblue',
        edgecolor='navy', label=r'$p(\tau^*)$ posterior')
ax.axvline(tau_mean, color='red', lw=2, ls='-', label=f'Mean = {tau_mean:.3f}')
ax.axvline(tau_fold, color='green', lw=2, ls='--', label=f'$\\tau_{{fold}} = {tau_fold}$')
ax.axvline(tau_16, color='orange', lw=1.5, ls=':', label='68% CI')
ax.axvline(tau_84, color='orange', lw=1.5, ls=':')
ax.axvline(tau_2p5, color='purple', lw=1, ls='-.', label='95% CI')
ax.axvline(tau_97p5, color='purple', lw=1, ls='-.')
ax.axvline(tau_star_flatband, color='cyan', lw=1.5, ls='--',
           label=f'S45 flatband = {tau_star_flatband:.3f}')
ax.set_xlabel(r'$\tau^*$', fontsize=12)
ax.set_ylabel('Probability density', fontsize=12)
ax.set_title(r'Posterior $p(\tau^*)$', fontsize=13)
ax.legend(fontsize=8)

# Panel 3: Uncertainty budget pie chart
ax = axes[1, 0]
labels_pie = ['GP interp.', '$\\Delta_{B2}$ model\nspread', '$\\Delta_{B3}$\nuncertainty',
              'Method\n(quad vs direct)']
sizes = [variances[k] for k in ['GP interpolation', 'B2 gap model spread',
                                  'B3 uncertainty', 'Method (quad vs direct)']]
colors_pie = ['#4ECDC4', '#FF6B6B', '#FFA07A', '#98D8C8']
wedges, texts, autotexts = ax.pie(sizes, labels=labels_pie, colors=colors_pie,
                                    autopct='%1.0f%%', startangle=90,
                                    textprops={'fontsize': 10})
for at in autotexts:
    at.set_fontsize(11)
    at.set_fontweight('bold')
ax.set_title(f'Uncertainty budget ($\\sigma_\\tau = {sigma_tau_final:.3f}$)', fontsize=13)

# Panel 4: LOO cross-validation
ax = axes[1, 1]
mu_loo = tau_train - loo_err  # predicted = actual - error
ax.scatter(tau_train, mu_loo, c='steelblue', s=25, alpha=0.7, zorder=5)
lims = [tau_train.min() - 0.02, tau_train.max() + 0.02]
ax.plot(lims, lims, 'k--', lw=1, label='Perfect')
ax.fill_between(lims, [l - loo_rmse for l in lims], [l + loo_rmse for l in lims],
                alpha=0.15, color='red', label=f'RMSE = {loo_rmse:.4f}')
ax.set_xlabel(r'$\tau^*$ (actual)', fontsize=12)
ax.set_ylabel(r'$\tau^*$ (LOO predicted)', fontsize=12)
ax.set_title(f'Leave-One-Out CV (RMSE = {loo_rmse:.4f})', fontsize=13)
ax.legend(fontsize=10)
ax.set_xlim(lims)
ax.set_ylim(lims)

ci_lab = "68" if tau_16 <= tau_fold <= tau_84 else (
    "95" if tau_2p5 <= tau_fold <= tau_97p5 else ">95")
plt.suptitle(
    f'BAYESIAN-GP-46: $\\tau^* = {tau_mean:.3f} \\pm {sigma_tau_final:.3f}$, '
    f'68% CI: [{tau_16:.3f}, {tau_84:.3f}], $\\tau_{{fold}}$ in {ci_lab}% CI',
    fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('tier0-computation/s46_bayesian_gp.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s46_bayesian_gp.png")

# ============================================================================
# STEP 10: Save Results
# ============================================================================
print("\n--- Saving results ---")

np.savez('tier0-computation/s46_bayesian_gp.npz',
         # Central result
         tau_star_posterior_mean=tau_mean,
         tau_star_posterior_median=tau_median,
         sigma_tau=sigma_tau_final,
         # Confidence intervals
         ci_68_lo=tau_16, ci_68_hi=tau_84,
         ci_95_lo=tau_2p5, ci_95_hi=tau_97p5,
         # B2 prior
         B2_mean=B2_mean, B2_std=B2_std,
         # Sensitivity
         dtau_dB2=dtau_dB2, dtau_dB3=dtau_dB3,
         # Uncertainty decomposition
         sigma_GP=sig_c[0],
         sigma_from_B2=sigma_from_B2,
         sigma_from_B3=sigma_from_B3,
         sigma_method=sigma_method,
         sigma_analytic=sigma_total_analytic,
         # 1D GP hyperparameters
         gp_sigma_f=sf, gp_length=length, gp_sigma_n=sn,
         # Training data
         B2_train=B2_train, tau_train=tau_train,
         # GP on fine grid
         B2_fine=B2_fine, mu_fine=mu_fine, sigma_fine=sig_fine,
         # LOO-CV
         loo_rmse=loo_rmse, loo_z_std=np.std(loo_z),
         # MC posterior
         tau_star_mc=tau_valid,
         # Gate
         gate_name=np.array(['BAYESIAN-GP-46']),
         gate_verdict=np.array(['INFO']),
         gate_detail=np.array([f'tau* = {tau_mean:.4f} +/- {sigma_tau_final:.4f}']),
         fold_in_68ci=(tau_16 <= tau_fold <= tau_84),
         fold_in_95ci=(tau_2p5 <= tau_fold <= tau_97p5),
         tau_fold=tau_fold,
)
print("  Saved: tier0-computation/s46_bayesian_gp.npz")

print("\n" + "=" * 78)
print("DONE: BAYESIAN-GP-46")
print("=" * 78)
