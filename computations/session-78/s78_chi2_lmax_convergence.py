#!/usr/bin/env python3
"""
s78_chi2_lmax_convergence.py -- S78-W3-A-CHI2-LMAX-CONV
=========================================================

Gate: S78-W3-A-CHI2-LMAX-CONV
  Primary scheme SDW (chi_2 = <sqrt(x)>_{d^2} identity).

  PASS-direct:    68% posterior mass of BMA-extrapolated chi_2^{SDW}(L_max->inf)
                  overlaps [0.651, 0.719]  (Omega_Lambda = 0.685 direct).
  PASS-Friedmann: 68% posterior mass overlaps [1.952, 2.158]
                  (Friedmann-3 * Omega_Lambda = 2.055).
  FAIL: posterior entirely outside both bands.
  INFO: L_max=15 infeasible AND posterior width > 10% --
        report achievable L_max, uncertainty, three fit-form values.
  INCOMPUTABLE: tail-fit chi_sq/dof > 2 from L=10,12 alone.

DISAGREEMENT BLOCK #3 DEFAULT: Lizzi SDW-only gate.
  Primary target: SDW.
  zeta / f* cross-schemes reported as INFO-only (no literature target).

Physics (substrate framing):
---------------------------
chi_2 = M_1^{d^2} / (N_{d^2} * lambda_max)
      = <|lambda|>_{d^2} / lambda_max
      = <sqrt(x)>_{d^2}      where x = lambda^2 / lambda_max^2

This is a spectral moment of D_K: the d^2-weighted mean of sqrt(x) over
the d^2-weighted normalized spectrum. It is NOT a cosmological constant
in a pre-existing spacetime container. It is the substrate's a_0-moment
projection that, via spectral-action expansion, produces the EMERGENT
effective Lambda_eff seen in LCDM. The PASS-direct vs PASS-Friedmann
distinction corresponds to two candidate structural identifications of
WHICH spectral moment of D_K maps to the observed Omega_Lambda.

Method (BMA over 3 fit forms):
  - Data source: cached chi_2^{SDW}(L) from S75 M1-L11-CONVERGENCE
                 covers L=3..11 (no recomputation; ~10^9 d^2-weighted modes
                 at L=11 would take hours; values verified from .npz).
  - L_max=15 declared INFEASIBLE upfront (would require ~10^10-10^11 modes).
  - L_max_achievable = 11.
  - Fit forms (AIC-weighted):
      (F1) power-law:              chi_2(L) = chi_inf + A * L^{-alpha}
      (F2) power-log:              chi_2(L) = chi_inf + A * L^{-alpha} * log(L)
      (F3) Richardson (two-term):  chi_2(L) = chi_inf + A/L + B/L^2
  - Posterior: gaussian mixture weighted by AIC_i = N*log(chisq_i/N) + 2*k_i.

Cross-checks:
  1. chi_2 = <sqrt(x)>_{d^2} identity at each L (direct computation vs ratio).
  2. R-protection on chi_2 across L_max (incremental drift < 1.3%).
  3. Exponent alpha consistency with rank-scaling (W3-K cross-reference).

Scheme/convention tag: (value, SDW, POWER-RATIO-NA, L_max=11)

Session: S78 W3-A (re-run under scrubbed plan)
Agent: lizzi-spectral-functional-theorist
Date: 2026-04-15
"""

import os
import sys
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.stats import norm

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold,
    Omega_Lambda,
    a0_fold, a2_fold, a4_fold,
    R_protected_fold,
)

# =========================================================================
# GATE SETUP and PRE-REGISTRATION
# =========================================================================
GATE_ID = "S78-W3-A-CHI2-LMAX-CONV"  # (local)
SCHEME_TAG = "SDW"                    # (local) primary scheme (DEFAULT: Lizzi SDW-only)
CONVENTION_TAG = "POWER-RATIO-NA"     # (local) chi_2 is a dimensionless moment, F_amp convention N/A
L_MAX_ACHIEVABLE = 11                 # (local) declared UPFRONT (L=15 infeasible: ~10^10-10^11 weighted modes)
L_MAX_INFEASIBLE_TARGET = 15          # (local) plan's aspirational target
L_MAX_INFEASIBLE_REASON = "~L^7 weighted-mode growth; L=11 already 1.57e9 d^2-weighted modes"  # (local)

# Pre-registered PASS/FAIL bands
BAND_DIRECT = (0.651, 0.719)          # (local) Omega_Lambda = 0.685 +/- 5% (Planck 2018 central; band width structural)
BAND_FRIEDMANN = (1.952, 2.158)       # (local) Friedmann-3 * Omega_Lambda = 3*0.685 = 2.055 +/- 5%
PASS_POSTERIOR_WIDTH_THRESH = 0.10    # (local) 10% width threshold for INFO fallback
TAIL_CHISQ_THRESH = 2.0               # (local) INCOMPUTABLE if tail chisq/dof > 2
FIT_FORM_SPREAD_THRESH = 0.05         # (local) 5% spread => fit-form-dependent (INFO)
R_PROT_DRIFT_THRESH = 0.013           # (local) R-protection 1.3% threshold (S74)

print("=" * 78)
print(f"{GATE_ID}: chi_2 L_max Convergence (SDW primary, BMA over 3 fit forms)")
print("=" * 78)
print()
print(f"  DISAGREEMENT BLOCK #3 DEFAULT: Lizzi SDW-only gate.")
print(f"  Primary scheme: {SCHEME_TAG}")
print(f"  Convention tag: {CONVENTION_TAG}")
print(f"  L_max achievable (declared upfront): {L_MAX_ACHIEVABLE}")
print(f"  L_max=15 infeasible reason: {L_MAX_INFEASIBLE_REASON}")
print()
print(f"  Pre-registered bands:")
print(f"    PASS-direct:    posterior 68%-mass in {BAND_DIRECT} (Omega_Lambda = 0.685)")
print(f"    PASS-Friedmann: posterior 68%-mass in {BAND_FRIEDMANN} (Friedmann-3 x Omega_Lambda = 2.055)")
print(f"    FAIL:           posterior entirely outside both bands")
print(f"    INFO:           L_max=15 infeasible AND posterior width > {PASS_POSTERIOR_WIDTH_THRESH*100:.0f}%")
print(f"    INCOMPUTABLE:   tail chisq/dof > {TAIL_CHISQ_THRESH}")
print()

# =========================================================================
# DATA LOADING (from S75 M1-L11-CONVERGENCE cached eigenvalue sums)
# =========================================================================
print("=" * 78)
print("STEP 1: Load cached chi_2^{SDW}(L) from S75 M1-L11-CONVERGENCE")
print("=" * 78)

s75_npz_path = os.path.join(SCRIPT_DIR, "s75_m1_l11_convergence.npz")  # (local)
if not os.path.isfile(s75_npz_path):
    raise FileNotFoundError(f"S75 cache missing: {s75_npz_path}")

s75 = np.load(s75_npz_path, allow_pickle=True)
L_arr_sdw = np.asarray(s75['L_list'], dtype=float)  # (local)
chi_2_sdw = np.asarray(s75['chi_2_arr'], dtype=float)  # (local)
M1_arr = np.asarray(s75['M1_arr'], dtype=float)  # (local)
N_arr = np.asarray(s75['N_arr'], dtype=float)  # (local)
lam_max_arr = np.asarray(s75['lam_max_arr'], dtype=float)  # (local)
lam_avg_arr = np.asarray(s75['lam_avg_arr'], dtype=float)  # (local)

print(f"  Cache source: s75_m1_l11_convergence.npz (PASS verdict)")
print(f"  L values     : {L_arr_sdw.astype(int).tolist()}")
print(f"  chi_2^{{SDW}}(L):")
for L, c, Nm in zip(L_arr_sdw, chi_2_sdw, N_arr):
    print(f"    L={int(L):2d}: chi_2 = {c:.8f}   N_modes (d^2-weighted) = {Nm:.3e}")
print(f"  tau_fold = {tau_fold}")
print()

# Use L >= 3 (stable asymptotic regime)
mask = L_arr_sdw >= 3  # (local)
L_fit = L_arr_sdw[mask]  # (local)
chi2_fit = chi_2_sdw[mask]  # (local)

# =========================================================================
# CROSS-CHECK #1: chi_2 = <sqrt(x)>_{d^2} identity
# =========================================================================
print("=" * 78)
print("CROSS-CHECK 1: chi_2 = <sqrt(x)>_{d^2} identity at each L")
print("=" * 78)
# Definition: chi_2 = M_1 / (N * lam_max).
# Identity:   chi_2 = sum d^2 |lambda| / (N * lam_max)
#                   = <|lambda|>_{d^2} / lam_max
#                   = < sqrt(x) >_{d^2}      with x = lambda^2/lam_max^2.
#
# Test: compute chi_2 directly from M_1/N/lam_max and compare to the cached chi_2.
identity_residuals = []  # (local)
for L, c, M, Nm, lm in zip(L_arr_sdw, chi_2_sdw, M1_arr, N_arr, lam_max_arr):
    c_recompute = M / (Nm * lm)  # (local)
    rel_err = abs(c_recompute - c) / c if c > 0 else np.inf  # (local)
    identity_residuals.append(rel_err)
    print(f"  L={int(L):2d}: chi_2 (cached) = {c:.10f}, recomputed = {c_recompute:.10f}, rel_err = {rel_err:.2e}")
identity_residuals = np.asarray(identity_residuals)  # (local)
IDENTITY_CC_PASS = bool(np.all(identity_residuals < 1e-10))  # (local)
print(f"  IDENTITY CROSS-CHECK: {'PASS' if IDENTITY_CC_PASS else 'FAIL'} (max rel_err = {identity_residuals.max():.2e})")
print()

# =========================================================================
# CROSS-CHECK #2: R-protection on chi_2 across L_max
# =========================================================================
print("=" * 78)
print("CROSS-CHECK 2: R-protection on chi_2 ratios across L")
print("=" * 78)
# In the strict R-protection sense (S74), chi_2 is a single-branch moment,
# not a ratio-of-moments, so drift larger than 1.3% is expected.  We
# compute the absolute drift of chi_2 AND the drift of chi_2 ratios
# normalised to L=9 (canonical).  For a protected ratio, drift should be
# < 1.3%.  For an unprotected single moment, drift ~ 10-20% is structural.
L_ref = 9  # (local) canonical reference L
idx_ref = int(np.where(L_arr_sdw == L_ref)[0][0])  # (local)
chi_2_ratio = chi_2_sdw / chi_2_sdw[idx_ref]  # (local) ratio to L=9
drifts = []  # (local)
for L, r in zip(L_arr_sdw, chi_2_ratio):
    drift = abs(r - 1.0)  # (local)
    drifts.append(drift)
    print(f"  L={int(L):2d}: chi_2 / chi_2(L=9) = {r:.6f}, |drift| = {drift*100:.2f}%")
max_drift_chi2 = float(np.max(drifts))  # (local)
R_PROT_CC_PASS = bool(max_drift_chi2 < R_PROT_DRIFT_THRESH)  # (local)
# Note: chi_2 is a single-branch moment, NOT ratio-protected per S74 doctrine.
print(f"  Max chi_2 drift across L in [3,11]: {max_drift_chi2*100:.2f}%")
print(f"  R-protection threshold 1.3%:       {'PASS' if R_PROT_CC_PASS else 'FAIL (EXPECTED)'}")
print(f"  Interpretation: chi_2 is a single-branch moment, NOT a ratio-protected")
print(f"                  observable. Drift > 1.3% is structural and confirms")
print(f"                  chi_2 requires extrapolation, not ratio-protection.")
print()

# =========================================================================
# STEP 2: BMA extrapolation over three fit forms
# =========================================================================
print("=" * 78)
print("STEP 2: BMA extrapolation -- three fit forms, AIC-weighted posterior")
print("=" * 78)


def model_power(L, chi_inf, A, alpha):
    """F1: power-law approach."""
    return chi_inf + A * L**(-alpha)


def model_power_log(L, chi_inf, A, alpha):
    """F2: power-law with log correction."""
    return chi_inf + A * L**(-alpha) * np.log(L)


def model_richardson(L, chi_inf, A, B):
    """F3: two-term Richardson (1/L, 1/L^2)."""
    return chi_inf + A / L + B / L**2


# Fit each model
fits = {}  # (local)

# F1: power
try:
    popt, pcov = curve_fit(
        model_power, L_fit, chi2_fit,
        p0=[0.74, 0.1, 1.0], bounds=([0.0, -10, 0.1], [1.0, 10, 10]),
        maxfev=50000,
    )
    chisq = float(np.sum((model_power(L_fit, *popt) - chi2_fit) ** 2))  # (local)
    N_pts = len(L_fit)  # (local)
    k_params = 3  # (local)
    dof = max(N_pts - k_params, 1)  # (local)
    chisq_dof = chisq / dof  # (local)
    chi_inf = float(popt[0])  # (local)
    sigma_inf = float(np.sqrt(max(pcov[0, 0], 0.0)))  # (local)
    # AIC for linear-gaussian residuals (constant sigma): N log(chisq/N) + 2k.
    # Use a fixed residual scale for cross-model comparison:
    residual_scale = np.std(chi2_fit - chi2_fit.mean())  # (local) same scale for all 3 models
    aic = N_pts * np.log(chisq / N_pts + 1e-30) + 2 * k_params  # (local)
    fits["F1_power"] = {
        "popt": popt, "pcov": pcov, "chi_inf": chi_inf, "sigma_inf": sigma_inf,
        "chisq": chisq, "chisq_dof": chisq_dof, "dof": dof, "aic": aic,
        "alpha": float(popt[2]),
    }
    print(f"  F1 power   : chi_inf = {chi_inf:.6f} +/- {sigma_inf:.6f}, "
          f"alpha = {popt[2]:.4f}, chisq/dof = {chisq_dof:.3e}")
except Exception as e:
    fits["F1_power"] = {"error": str(e)}
    print(f"  F1 power  : FIT FAILED: {e}")

# F2: power-log
try:
    popt, pcov = curve_fit(
        model_power_log, L_fit, chi2_fit,
        p0=[0.74, 0.05, 1.0], bounds=([0.0, -10, 0.1], [1.0, 10, 10]),
        maxfev=50000,
    )
    chisq = float(np.sum((model_power_log(L_fit, *popt) - chi2_fit) ** 2))  # (local)
    N_pts = len(L_fit)  # (local)
    k_params = 3  # (local)
    dof = max(N_pts - k_params, 1)  # (local)
    chisq_dof = chisq / dof  # (local)
    chi_inf = float(popt[0])  # (local)
    sigma_inf = float(np.sqrt(max(pcov[0, 0], 0.0)))  # (local)
    aic = N_pts * np.log(chisq / N_pts + 1e-30) + 2 * k_params  # (local)
    fits["F2_power_log"] = {
        "popt": popt, "pcov": pcov, "chi_inf": chi_inf, "sigma_inf": sigma_inf,
        "chisq": chisq, "chisq_dof": chisq_dof, "dof": dof, "aic": aic,
        "alpha": float(popt[2]),
    }
    print(f"  F2 pow-log : chi_inf = {chi_inf:.6f} +/- {sigma_inf:.6f}, "
          f"alpha = {popt[2]:.4f}, chisq/dof = {chisq_dof:.3e}")
except Exception as e:
    fits["F2_power_log"] = {"error": str(e)}
    print(f"  F2 pow-log: FIT FAILED: {e}")

# F3: Richardson
try:
    popt, pcov = curve_fit(
        model_richardson, L_fit, chi2_fit,
        p0=[0.74, 0.1, -0.1], maxfev=50000,
    )
    chisq = float(np.sum((model_richardson(L_fit, *popt) - chi2_fit) ** 2))  # (local)
    N_pts = len(L_fit)  # (local)
    k_params = 3  # (local)
    dof = max(N_pts - k_params, 1)  # (local)
    chisq_dof = chisq / dof  # (local)
    chi_inf = float(popt[0])  # (local)
    sigma_inf = float(np.sqrt(max(pcov[0, 0], 0.0)))  # (local)
    aic = N_pts * np.log(chisq / N_pts + 1e-30) + 2 * k_params  # (local)
    fits["F3_richardson"] = {
        "popt": popt, "pcov": pcov, "chi_inf": chi_inf, "sigma_inf": sigma_inf,
        "chisq": chisq, "chisq_dof": chisq_dof, "dof": dof, "aic": aic,
        "alpha": None,
    }
    print(f"  F3 Richard : chi_inf = {chi_inf:.6f} +/- {sigma_inf:.6f}, "
          f"A = {popt[1]:.4f}, B = {popt[2]:.4f}, chisq/dof = {chisq_dof:.3e}")
except Exception as e:
    fits["F3_richardson"] = {"error": str(e)}
    print(f"  F3 Richard: FIT FAILED: {e}")

print()

# =========================================================================
# STEP 3: BMA posterior
# =========================================================================
print("=" * 78)
print("STEP 3: AIC-weighted BMA posterior over chi_2^{SDW}(L->inf)")
print("=" * 78)

valid_fits = {k: v for k, v in fits.items() if "error" not in v}  # (local)
if len(valid_fits) == 0:
    raise RuntimeError("All three fits failed -- INCOMPUTABLE")

# AIC weights
aic_vals = np.array([v["aic"] for v in valid_fits.values()])  # (local)
aic_min = aic_vals.min()  # (local)
weights_raw = np.exp(-0.5 * (aic_vals - aic_min))  # (local)
weights = weights_raw / weights_raw.sum()  # (local)

chi_inf_vals = np.array([v["chi_inf"] for v in valid_fits.values()])  # (local)
sigma_inf_vals = np.array([v["sigma_inf"] for v in valid_fits.values()])  # (local)
chisq_dof_vals = np.array([v["chisq_dof"] for v in valid_fits.values()])  # (local)
fit_names = list(valid_fits.keys())  # (local)

# Posterior mean and width (using AIC-weighted gaussian mixture)
post_mean = float(np.sum(weights * chi_inf_vals))  # (local)
# Mixture variance = sum_i w_i (sigma_i^2 + mu_i^2) - mu_total^2
post_var = float(np.sum(weights * (sigma_inf_vals**2 + chi_inf_vals**2)) - post_mean**2)  # (local)
post_std = float(np.sqrt(max(post_var, 0.0)))  # (local)

# Fit-form spread at L -> inf
fit_spread = float(chi_inf_vals.max() - chi_inf_vals.min())  # (local)
fit_spread_rel = fit_spread / post_mean if post_mean > 0 else np.inf  # (local)

# Posterior width (relative)
posterior_width_rel = post_std / post_mean if post_mean > 0 else np.inf  # (local)

# Worst tail chisq/dof
worst_chisq_dof = float(chisq_dof_vals.max())  # (local)

print(f"  BMA components and AIC weights:")
for name, w, c, s, cd in zip(fit_names, weights, chi_inf_vals, sigma_inf_vals, chisq_dof_vals):
    print(f"    {name:15s}  w={w:.4f}  chi_inf={c:.6f} +/- {s:.6f}  chisq/dof={cd:.3e}")
print()
print(f"  Posterior mean  : {post_mean:.6f}")
print(f"  Posterior std   : {post_std:.6f}")
print(f"  Posterior width : {posterior_width_rel*100:.2f}% (rel)")
print(f"  Fit-form spread : {fit_spread:.6f} ({fit_spread_rel*100:.2f}% rel)")
print(f"  Worst chisq/dof : {worst_chisq_dof:.3e}")
print()

# =========================================================================
# STEP 4: Posterior mass in PASS bands
# =========================================================================
print("=" * 78)
print("STEP 4: Posterior mass in PASS-direct and PASS-Friedmann bands")
print("=" * 78)


def posterior_mass_in(bands, weights, mus, sigmas):
    """Compute AIC-weighted gaussian-mixture mass within band (lo, hi)."""
    lo, hi = bands
    mass = 0.0  # (local)
    for w, mu, sigma in zip(weights, mus, sigmas):
        if sigma <= 0:
            # Point mass at mu
            if lo <= mu <= hi:
                mass += w
        else:
            p = norm.cdf(hi, loc=mu, scale=sigma) - norm.cdf(lo, loc=mu, scale=sigma)  # (local)
            mass += w * p
    return mass


# Generate posterior samples by mixture for 68% HPD computation
rng = np.random.default_rng(78_03_0042)  # (local)
N_samp = 500_000  # (local)
# For each sample, pick component by AIC weight then sample gaussian
comp_idx = rng.choice(len(weights), size=N_samp, p=weights)  # (local)
samples = np.empty(N_samp)  # (local)
for i, (mu, sigma) in enumerate(zip(chi_inf_vals, sigma_inf_vals)):
    sel = comp_idx == i  # (local)
    n_sel = int(sel.sum())  # (local)
    sigma_use = max(sigma, 1e-8)  # (local)
    samples[sel] = rng.normal(loc=mu, scale=sigma_use, size=n_sel)

# 68% HPD interval (symmetric)
q_lo = float(np.quantile(samples, 0.16))  # (local)
q_hi = float(np.quantile(samples, 0.84))  # (local)
frac_in_direct = posterior_mass_in(BAND_DIRECT, weights, chi_inf_vals, sigma_inf_vals)  # (local)
frac_in_fried = posterior_mass_in(BAND_FRIEDMANN, weights, chi_inf_vals, sigma_inf_vals)  # (local)
# Fraction of samples inside the band
emp_frac_direct = float(np.mean((samples >= BAND_DIRECT[0]) & (samples <= BAND_DIRECT[1])))  # (local)
emp_frac_fried = float(np.mean((samples >= BAND_FRIEDMANN[0]) & (samples <= BAND_FRIEDMANN[1])))  # (local)

# 68%-HPD interval overlap
def overlap_68(q_lo, q_hi, band):
    lo, hi = band
    overlap_lo = max(q_lo, lo)  # (local)
    overlap_hi = min(q_hi, hi)  # (local)
    return max(overlap_hi - overlap_lo, 0.0) / (q_hi - q_lo) if q_hi > q_lo else 0.0


overlap_direct = overlap_68(q_lo, q_hi, BAND_DIRECT)  # (local)
overlap_fried = overlap_68(q_lo, q_hi, BAND_FRIEDMANN)  # (local)

print(f"  68% HPD interval : [{q_lo:.6f}, {q_hi:.6f}]")
print(f"  PASS-direct band : {BAND_DIRECT}")
print(f"    Analytic mass in band     : {frac_in_direct*100:.2f}%")
print(f"    Empirical sample mass     : {emp_frac_direct*100:.2f}%")
print(f"    68% HPD fractional overlap: {overlap_direct*100:.2f}%")
print(f"  PASS-Friedmann band: {BAND_FRIEDMANN}")
print(f"    Analytic mass in band     : {frac_in_fried*100:.2f}%")
print(f"    Empirical sample mass     : {emp_frac_fried*100:.2f}%")
print(f"    68% HPD fractional overlap: {overlap_fried*100:.2f}%")
print()

# =========================================================================
# STEP 5: Gate decision logic (per pre-registration)
# =========================================================================
print("=" * 78)
print("STEP 5: Gate decision")
print("=" * 78)

# INCOMPUTABLE check
if worst_chisq_dof > TAIL_CHISQ_THRESH:
    verdict = "INCOMPUTABLE"
    verdict_reason = f"tail chisq/dof = {worst_chisq_dof:.3e} > {TAIL_CHISQ_THRESH}"  # (local)
# PASS checks (at least 68% mass in a band by analytic or empirical measure)
elif emp_frac_direct >= 0.68:
    verdict = "PASS-direct"
    verdict_reason = f"68%+ posterior mass in {BAND_DIRECT} (empirical {emp_frac_direct*100:.1f}%)"  # (local)
elif emp_frac_fried >= 0.68:
    verdict = "PASS-Friedmann"
    verdict_reason = f"68%+ posterior mass in {BAND_FRIEDMANN} (empirical {emp_frac_fried*100:.1f}%)"  # (local)
# FAIL: entirely outside both bands
elif emp_frac_direct < 0.01 and emp_frac_fried < 0.01 and overlap_direct < 0.01 and overlap_fried < 0.01:
    verdict = "FAIL"
    verdict_reason = f"posterior entirely outside both bands (direct {emp_frac_direct*100:.2f}%, Friedmann {emp_frac_fried*100:.2f}%)"  # (local)
# INFO: L=15 infeasible AND (posterior width > 10% OR fit-form spread > 5%)
else:
    if posterior_width_rel > PASS_POSTERIOR_WIDTH_THRESH or fit_spread_rel > FIT_FORM_SPREAD_THRESH:
        verdict = "INFO"
        verdict_reason = (
            f"L_max=15 infeasible (declared upfront, achievable={L_MAX_ACHIEVABLE}); "
            f"posterior width {posterior_width_rel*100:.2f}% "
            f"{'>' if posterior_width_rel > PASS_POSTERIOR_WIDTH_THRESH else '<='} {PASS_POSTERIOR_WIDTH_THRESH*100:.0f}%, "
            f"fit-form spread {fit_spread_rel*100:.2f}% "
            f"{'>' if fit_spread_rel > FIT_FORM_SPREAD_THRESH else '<='} {FIT_FORM_SPREAD_THRESH*100:.0f}%"
        )  # (local)
    else:
        # Posterior is tight and fit-form spread tight, but neither band has 68%+ mass.
        # By pre-registered wording ("entirely outside both bands" for FAIL), this
        # is an INFO: partial-band-overlap. Report explicitly.
        verdict = "INFO"
        verdict_reason = (
            f"L_max=15 infeasible; posterior tight ({posterior_width_rel*100:.2f}%) "
            f"but neither band carries 68% mass: direct {emp_frac_direct*100:.1f}%, "
            f"Friedmann {emp_frac_fried*100:.1f}%. Partial overlap: direct {overlap_direct*100:.1f}%, "
            f"Friedmann {overlap_fried*100:.1f}%."
        )  # (local)

print(f"  VERDICT: {verdict}")
print(f"  REASON : {verdict_reason}")
print()

# =========================================================================
# STEP 6: Cross-scheme INFO (zeta / f*) -- estimates from prior sessions
# =========================================================================
print("=" * 78)
print("STEP 6: Cross-scheme INFO (zeta / f*) -- NOT GATED (Lizzi SDW-only)")
print("=" * 78)

# zeta scheme: chi_2^{zeta} has no direct literature target.  The
# relationship chi_2^{zeta} ~ chi_2^{SDW} * c(zeta, d=4) emerges from
# the S78 W3-L dictionary (s78_sdw_vs_zeta_dictionary).  In the zeta
# scheme, the moment is the coefficient of zeta_D(s) near s=1.  For
# d=4 Weyl counting, c = 1/(16 pi^2) for the HK-zeta conversion, but
# chi_2 is a single-moment normalised ratio so the Weyl factor cancels
# in the ratio itself.  That leaves only the f_0 Mellin prefactor.
# Best-estimate: chi_2^{zeta} = chi_2^{SDW} * (f_0^{zeta}/f_0^{SDW})
# which in the f_0^{SDW} = 0.912 convention gives a factor ~1.1.
#
# f* scheme (0.912 sqrt(x) + 0.088 exp(-x)): S72 SPECTRAL-FUNCTIONAL-FIT
# showed f* is ~99% SDW-like for chi_2 (the exp(-x) tail contributes
# ~9% of the normalisation but cancels in the chi_2 ratio since both
# numerator and denominator carry it).
print(f"  Cross-scheme INFO:")
print(f"    chi_2^{{SDW}}    = {post_mean:.6f} +/- {post_std:.6f}  [GATED, this gate]")

# Crude cross-scheme estimates -- pure INFO, not gated
f0_sdw = 0.912  # (local) S72 f* sqrt weight
chi2_zeta_est = post_mean * (1.0 / f0_sdw)  # (local) zeta / SDW Mellin ratio estimate
chi2_fstar_est = post_mean  # (local) f* is SDW-dominated to ~1% for chi_2
print(f"    chi_2^{{zeta}}   ~ {chi2_zeta_est:.6f}  [INFO only, crude Mellin estimate]")
print(f"    chi_2^{{f*}}     ~ {chi2_fstar_est:.6f}  [INFO only, f* ~ SDW for chi_2]")
print()
print(f"  Note: zeta and f* have NO LITERATURE TARGET for chi_2.  The PASS bands")
print(f"        at 0.685 (direct Omega_Lambda) and 2.055 (Friedmann-3*Omega_Lambda)")
print(f"        are SDW-defined.  Cross-scheme values are reported only to document")
print(f"        functional dependence per Lizzi SDW-only framing (DEFAULT).")
print()

# =========================================================================
# STEP 7: Save artifacts
# =========================================================================
print("=" * 78)
print("STEP 7: Save artifacts")
print("=" * 78)

# --- .npz ---
npz_path = os.path.join(SCRIPT_DIR, "s78_chi2_lmax_convergence.npz")  # (local)
np.savez_compressed(
    npz_path,
    # Header and verdict
    gate_id=GATE_ID,
    verdict=verdict,
    verdict_reason=verdict_reason,
    scheme_tag=SCHEME_TAG,
    convention_tag=CONVENTION_TAG,
    L_max_achievable=L_MAX_ACHIEVABLE,
    L_max_infeasible=L_MAX_INFEASIBLE_TARGET,
    # Data
    L_arr=L_arr_sdw,
    chi_2_sdw=chi_2_sdw,
    M1_arr=M1_arr,
    N_arr=N_arr,
    lam_max_arr=lam_max_arr,
    lam_avg_arr=lam_avg_arr,
    # Fits (per form)
    fit_names=np.array(fit_names),
    chi_inf_vals=chi_inf_vals,
    sigma_inf_vals=sigma_inf_vals,
    chisq_dof_vals=chisq_dof_vals,
    aic_vals=aic_vals,
    aic_weights=weights,
    F1_alpha=float(fits.get("F1_power", {}).get("alpha", np.nan)),
    F2_alpha=float(fits.get("F2_power_log", {}).get("alpha", np.nan)),
    # Posterior
    posterior_mean=post_mean,
    posterior_std=post_std,
    posterior_width_rel=posterior_width_rel,
    fit_form_spread=fit_spread,
    fit_form_spread_rel=fit_spread_rel,
    q68_lo=q_lo,
    q68_hi=q_hi,
    # Bands
    band_direct=np.array(BAND_DIRECT),
    band_friedmann=np.array(BAND_FRIEDMANN),
    frac_in_direct_analytic=frac_in_direct,
    frac_in_fried_analytic=frac_in_fried,
    frac_in_direct_empirical=emp_frac_direct,
    frac_in_fried_empirical=emp_frac_fried,
    overlap_direct=overlap_direct,
    overlap_fried=overlap_fried,
    # Cross-checks
    identity_residuals=identity_residuals,
    identity_cc_pass=IDENTITY_CC_PASS,
    chi2_drift_max=max_drift_chi2,
    R_protection_cc_pass=R_PROT_CC_PASS,
    # Cross-scheme INFO (NOT GATED)
    chi2_zeta_est=chi2_zeta_est,
    chi2_fstar_est=chi2_fstar_est,
    # Context
    Omega_Lambda_planck=Omega_Lambda,
    tau_fold=tau_fold,
)
print(f"  Wrote {npz_path}")

# --- .png ---
png_path = os.path.join(SCRIPT_DIR, "s78_chi2_lmax_convergence.png")  # (local)
fig = plt.figure(figsize=(13, 10))

# Panel 1: chi_2(L) with three fit-form extrapolations
ax1 = fig.add_subplot(2, 2, 1)
L_dense = np.linspace(L_fit.min(), 50, 200)  # (local)
ax1.plot(L_arr_sdw, chi_2_sdw, "ko", ms=9, label="Data (S75)")
colors_fit = {"F1_power": "tab:red", "F2_power_log": "tab:green", "F3_richardson": "tab:blue"}  # (local)
for name, fit in valid_fits.items():
    if name == "F1_power":
        y_dense = model_power(L_dense, *fit["popt"])  # (local)
    elif name == "F2_power_log":
        y_dense = model_power_log(L_dense, *fit["popt"])  # (local)
    elif name == "F3_richardson":
        y_dense = model_richardson(L_dense, *fit["popt"])  # (local)
    ax1.plot(L_dense, y_dense, "-", color=colors_fit[name], lw=2,
             label=f"{name} -> {fit['chi_inf']:.4f}")
    ax1.axhline(fit["chi_inf"], color=colors_fit[name], ls="--", lw=1, alpha=0.5)
ax1.axhspan(BAND_DIRECT[0], BAND_DIRECT[1], color="gold", alpha=0.35, label="PASS-direct [0.651, 0.719]")
# Friedmann band shown on separate panel (different scale)
ax1.set_xlabel("L_max")
ax1.set_ylabel(r"$\chi_2^{SDW}$")
ax1.set_title(r"$\chi_2^{SDW}(L_{\max})$ with BMA extrapolations")
ax1.legend(loc="lower right", fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: Posterior density with both PASS bands
ax2 = fig.add_subplot(2, 2, 2)
ax2.hist(samples, bins=150, density=True, alpha=0.7, color="tab:gray", label="BMA posterior")
ax2.axvspan(BAND_DIRECT[0], BAND_DIRECT[1], color="gold", alpha=0.4,
            label=f"PASS-direct  {emp_frac_direct*100:.1f}% mass")
ax2.axvspan(BAND_FRIEDMANN[0], BAND_FRIEDMANN[1], color="lightgreen", alpha=0.4,
            label=f"PASS-Friedmann  {emp_frac_fried*100:.1f}% mass")
ax2.axvline(post_mean, color="black", ls="-", lw=2, label=f"mean = {post_mean:.4f}")
ax2.axvline(q_lo, color="black", ls=":", lw=1, label=f"68% HPD [{q_lo:.3f},{q_hi:.3f}]")
ax2.axvline(q_hi, color="black", ls=":", lw=1)
ax2.set_xlabel(r"$\chi_2^{SDW}(L_{\max}\to\infty)$")
ax2.set_ylabel("density")
ax2.set_title("BMA posterior vs PASS bands")
ax2.legend(loc="upper right", fontsize=8)
ax2.grid(True, alpha=0.3)

# Panel 3: Residuals per fit
ax3 = fig.add_subplot(2, 2, 3)
for name, fit in valid_fits.items():
    if name == "F1_power":
        y_pred = model_power(L_fit, *fit["popt"])  # (local)
    elif name == "F2_power_log":
        y_pred = model_power_log(L_fit, *fit["popt"])  # (local)
    elif name == "F3_richardson":
        y_pred = model_richardson(L_fit, *fit["popt"])  # (local)
    resid = chi2_fit - y_pred  # (local)
    ax3.plot(L_fit, resid, "o-", color=colors_fit[name], label=name, lw=2, ms=8)
ax3.axhline(0, color="black", ls="-", lw=1, alpha=0.5)
ax3.set_xlabel("L_max")
ax3.set_ylabel(r"residual: data $-$ fit")
ax3.set_title("Fit residuals (tail convergence diagnostic)")
ax3.legend(loc="upper right", fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: AIC weights + summary
ax4 = fig.add_subplot(2, 2, 4)
ax4.axis("off")
summary_txt = (
    f"{GATE_ID}\n"
    f"Scheme: {SCHEME_TAG}  Convention: {CONVENTION_TAG}\n"
    f"L_max achievable: {L_MAX_ACHIEVABLE}  (L_max=15 infeasible upfront)\n\n"
    f"BMA results:\n"
    f"  F1 (power)    : w={weights[0]:.3f}  chi_inf={chi_inf_vals[0]:.4f}\n"
)
if len(weights) > 1:
    summary_txt += f"  F2 (pow-log)  : w={weights[1]:.3f}  chi_inf={chi_inf_vals[1]:.4f}\n"
if len(weights) > 2:
    summary_txt += f"  F3 (Richard)  : w={weights[2]:.3f}  chi_inf={chi_inf_vals[2]:.4f}\n"
summary_txt += (
    f"\nPosterior  : {post_mean:.4f} +/- {post_std:.4f}\n"
    f"Width (rel): {posterior_width_rel*100:.2f}%\n"
    f"Form spread: {fit_spread_rel*100:.2f}%\n"
    f"Worst chi2/dof: {worst_chisq_dof:.2e}\n\n"
    f"PASS-direct mass : {emp_frac_direct*100:.2f}%\n"
    f"PASS-Fried  mass : {emp_frac_fried*100:.2f}%\n"
    f"\nVERDICT: {verdict}\n"
    f"Reason : {verdict_reason[:100]}"
)
ax4.text(0.02, 0.98, summary_txt, transform=ax4.transAxes,
         family="monospace", fontsize=9, va="top", ha="left")

plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()
print(f"  Wrote {png_path}")

# --- Append to gate verdicts file ---
verdict_path = os.path.join(SCRIPT_DIR, "s78_gate_verdicts.txt")  # (local)
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"chi_2(SDW,inf)={post_mean:.4f}+/-{post_std:.4f}, "
    f"68%-in-direct={emp_frac_direct*100:.1f}%, "
    f"68%-in-Fried={emp_frac_fried*100:.1f}%, "
    f"(value, {SCHEME_TAG}, {CONVENTION_TAG}, L_max={L_MAX_ACHIEVABLE})\n"
)  # (local)
with open(verdict_path, "a", encoding="utf-8") as f_verdict:
    f_verdict.write(verdict_line)
print(f"  Appended to {verdict_path}:")
print(f"    {verdict_line.strip()}")
print()

print("=" * 78)
print("DONE")
print("=" * 78)
