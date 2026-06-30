#!/usr/bin/env python3
"""
s68_desi_dr3_forecast.py -- DESI-DR3-FORECAST-68: Fisher Matrix w0-wa Forecast
================================================================================
Gate: DESI-DR3-FORECAST-68
  INFO: Forecast; no pass/fail. Report exclusion sigma under each scenario.

Physics:
  The framework predicts w_0 = -0.918, w_a = 0 from the Volovik relaxation
  mechanism (confirmed DESI-VOLOVIK-67). This is a STATIC dark energy analog:
  the spectral action zeroth moment generates an effective cosmological
  constant with w_0 slightly above -1 (effacement residual) and NO time
  variation (w_a = 0, protected by integrability + block-diagonal structure).

  DESI DR2 measures w_0 = -0.752 +/- 0.057, w_a = -0.73 +/- 0.25 (2.9-sigma
  from framework in 1D, 4.1-sigma in 2D per DESI-VOLOVIK-67). This script
  constructs a Fisher matrix forecast for projected DR3 sensitivity and
  evaluates the framework prediction under three pre-registered scenarios.

  Three scenarios (from DR3-PREREGISTER-60):
    A: DR3 confirms DR2 (w_0=-0.75, w_a=-0.73) -- framework excluded
    B: DR3 shifts toward LCDM (w_0=-0.90, w_a=-0.30) -- tension zone
    C: DR3 increases dynamical DE evidence (w_0=-0.65, w_a=-1.0) -- both excluded

  We also compute D_V(z)/r_d at each DESI bin for the framework prediction
  with projected DR3 error bars (sqrt(2) improvement over DR2).

Author: Katie Mack (Cosmic Bridge)
Session: 68, Task DESI-DR3-FORECAST-68
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy.integrate import quad
from scipy import stats

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, c_light_km_s,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s68_desi_dr3_forecast_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("DESI-DR3-FORECAST-68: Fisher Matrix w_0-w_a Forecast")
pr("=" * 72)

# =============================================================================
# 1. Cosmological Parameters (Planck 2018 baseline)
# =============================================================================
Om_m = Omega_m          # 0.315
Om_b = Omega_b          # 0.0493
Om_r = Omega_r          # 9.15e-5
Om_DE = 1.0 - Om_m - Om_r  # ~0.685
h = H_0_km_s_Mpc / 100.0   # 0.674
H_0 = H_0_km_s_Mpc         # 67.4 km/s/Mpc

pr(f"\nCosmological parameters (Planck 2018):")
pr(f"  Omega_m  = {Om_m}")
pr(f"  Omega_b  = {Om_b}")
pr(f"  Omega_r  = {Om_r}")
pr(f"  Omega_DE = {Om_DE:.6f}")
pr(f"  h        = {h}")

# =============================================================================
# 2. Load Upstream Data
# =============================================================================
pr(f"\n{'='*72}")
pr("Loading Upstream Data")
pr(f"{'='*72}")

# S67 Volovik results (authoritative for framework w_0, w_a)
d67 = np.load(os.path.join(SCRIPT_DIR, 's67_desi_volovik.npz'), allow_pickle=True)
w0_fw = float(d67['w0_fw'])        # -0.918
wa_fw = float(d67['wa_fw'])        # 0.0
w0_desi_dr2 = float(d67['w0_desi'])     # -0.752
wa_desi_dr2 = float(d67['wa_desi'])     # -0.73
w0_desi_err = float(d67['w0_desi_err']) # 0.057
wa_desi_err = float(d67['wa_desi_err']) # 0.25

# S59 error propagation (framework uncertainties, DR3 projections)
d59 = np.load(os.path.join(SCRIPT_DIR, 's59_wa_error_prop.npz'), allow_pickle=True)
sigma_w0_fw = float(d59['sigma_w0_fw'])    # 0.0366
sigma_wa_fw = float(d59['sigma_wa_fw'])    # 0.000273
rho_desi = float(d59['rho_desi'])          # -0.85

# S64 D_V data (BAO comparison at 7 bins)
d64 = np.load(os.path.join(SCRIPT_DIR, 's64_desi_dv.npz'), allow_pickle=True)
z_eff = np.array(d64['z_eff'])
sigma_DV_frac_dr2 = np.array(d64['sigma_DV_frac'])
tracer_labels = list(d64['tracer_labels'])

pr(f"\n  Framework (DESI-VOLOVIK-67):  w_0 = {w0_fw:.4f}, w_a = {wa_fw:.6f}")
pr(f"  DESI DR2 best-fit:           w_0 = {w0_desi_dr2} +/- {w0_desi_err}")
pr(f"                               w_a = {wa_desi_dr2} +/- {wa_desi_err}")
pr(f"  DESI DR2 correlation:        rho = {rho_desi}")
pr(f"  Framework theory error:      sigma(w_0) = {sigma_w0_fw:.4f}, sigma(w_a) = {sigma_wa_fw:.6f}")
pr(f"  LCDM:                        w_0 = -1.0, w_a = 0.0")

# LCDM parameters
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# =============================================================================
# 3. Sound Horizon
# =============================================================================
omega_b = Om_b * h**2
omega_m = Om_m * h**2
N_eff = 3.044  # (local)

# Eisenstein & Hu 1998 fitting formula
r_d_Mpc = 147.05 * (omega_b / 0.02236)**(-0.13) * \
                    (omega_m / 0.1432)**(-0.23) * \
                    (N_eff / 3.04)**(-0.10)

pr(f"\n  Sound horizon: r_d = {r_d_Mpc:.3f} Mpc (E&H 1998)")

# =============================================================================
# 4. DR3 Projected Sensitivities
# =============================================================================
# DR3 doubles the effective volume => sqrt(2) improvement in errors
sqrt2 = np.sqrt(2.0)
sigma_w0_dr3 = w0_desi_err / sqrt2      # 0.0403
sigma_wa_dr3 = wa_desi_err / sqrt2      # 0.1768
sigma_DV_frac_dr3 = sigma_DV_frac_dr2 / sqrt2

# Correlation coefficient: DESI DR2 reports rho = -0.85.
# For the Fisher forecast, we use rho = 0.45 as specified in the task
# (estimated from the DR2 contour shape in the positive-definite sense).
# Note: the DESI likelihood contour is elongated with NEGATIVE correlation
# in (w_0, w_a) space. The task specifies rho = 0.45 for the Fisher matrix;
# this is the correlation in the INVERSE Fisher (covariance) matrix.
# HOWEVER: checking against S59/S60 which used rho = -0.85 from DESI,
# we should use the DESI-measured correlation rho = -0.85 for consistency.
# The task specification of rho = 0.45 appears to be an unsigned estimate.
# We will compute with BOTH and report.
rho_fisher_pos = 0.45     # task specification  # (local)
rho_fisher_neg = rho_desi # = -0.85, DESI measured

pr(f"\n{'='*72}")
pr("DR3 Projected Sensitivities")
pr(f"{'='*72}")
pr(f"  sigma(w_0) = {sigma_w0_dr3:.4f}  (DR2: {w0_desi_err:.3f})")
pr(f"  sigma(w_a) = {sigma_wa_dr3:.4f}  (DR2: {wa_desi_err:.3f})")
pr(f"  rho (DESI) = {rho_fisher_neg}")
pr(f"  rho (task) = {rho_fisher_pos}")
pr(f"  D_V/r_d fractional errors: DR3 = DR2/sqrt(2)")
for i in range(len(z_eff)):
    pr(f"    z={z_eff[i]:.3f} ({tracer_labels[i]:>12s}): "
       f"DR2 {sigma_DV_frac_dr2[i]*100:.1f}% -> DR3 {sigma_DV_frac_dr3[i]*100:.2f}%")

# =============================================================================
# 5. Fisher Matrix Construction
# =============================================================================
pr(f"\n{'='*72}")
pr("Fisher Matrix / Covariance Construction")
pr(f"{'='*72}")

def build_cov(sigma_w0, sigma_wa, rho):
    """Build 2x2 covariance matrix for (w_0, w_a)."""
    return np.array([
        [sigma_w0**2,                 rho * sigma_w0 * sigma_wa],
        [rho * sigma_w0 * sigma_wa,   sigma_wa**2]
    ])

def chi2_2d(w0_test, wa_test, w0_cen, wa_cen, cov):
    """Compute chi^2 for a point (w0_test, wa_test) relative to center (w0_cen, wa_cen)."""
    dw = np.array([w0_test - w0_cen, wa_test - wa_cen])
    F = np.linalg.inv(cov)
    return float(dw @ F @ dw)

def sigma_from_chi2(chi2_val, ndof=2):
    """Convert chi^2 to sigma (Gaussian equivalent significance) for ndof degrees of freedom."""
    p_val = 1.0 - stats.chi2.cdf(chi2_val, df=ndof)
    # Clip p-value for numerical stability
    p_val = max(p_val, 1e-300)
    return stats.norm.isf(p_val / 2.0)  # two-tailed

def contour_overlap_fraction(w0_1, wa_1, cov_1, w0_2, wa_2, cov_2, n_mc=500000):
    """Monte Carlo estimate of 95% contour overlap fraction."""
    # chi2 threshold for 95% (2 DOF)
    chi2_95 = stats.chi2.ppf(0.95, df=2)  # = 5.991

    # Sample from distribution 1
    samples = np.random.multivariate_normal([w0_1, wa_1], cov_1, size=n_mc)

    # Check how many fall within 95% contour of distribution 2
    dw = samples - np.array([w0_2, wa_2])
    F2 = np.linalg.inv(cov_2)
    chi2_vals = np.sum(dw @ F2 * dw, axis=1)
    n_inside = np.sum(chi2_vals <= chi2_95)

    return float(n_inside) / float(n_mc)

# Build covariance matrices for DR3 scenarios
# Using DESI-measured correlation rho = -0.85 (primary)
cov_dr3_primary = build_cov(sigma_w0_dr3, sigma_wa_dr3, rho_fisher_neg)
F_dr3_primary = np.linalg.inv(cov_dr3_primary)

# Using task-specified rho = 0.45 (cross-check)
cov_dr3_task = build_cov(sigma_w0_dr3, sigma_wa_dr3, rho_fisher_pos)
F_dr3_task = np.linalg.inv(cov_dr3_task)

# Framework covariance (extremely tight -- effectively a point)
cov_fw = build_cov(sigma_w0_fw, sigma_wa_fw, 0.0)

pr(f"\n  DR3 Covariance (rho = {rho_fisher_neg}):")
pr(f"    {cov_dr3_primary}")
pr(f"  Fisher (rho = {rho_fisher_neg}):")
pr(f"    {F_dr3_primary}")
pr(f"\n  DR3 Covariance (rho = {rho_fisher_pos}):")
pr(f"    {cov_dr3_task}")
pr(f"  Fisher (rho = {rho_fisher_pos}):")
pr(f"    {F_dr3_task}")
pr(f"\n  Framework Covariance:")
pr(f"    {cov_fw}")
pr(f"    (effectively a delta function in the w_0-w_a plane)")

# =============================================================================
# 6. Three DR3 Scenarios
# =============================================================================
pr(f"\n{'='*72}")
pr("SCENARIO ANALYSIS")
pr(f"{'='*72}")

# Scenario definitions from S60 pre-registration
# Task specifies: A: (w0=-0.75, wa=-0.73), B: (w0=-0.90, wa=-0.30), C: (w0=-0.65, wa=-1.0)
scenarios = {
    'A': {
        'label': 'DR3 confirms DR2',
        'w0': -0.75, 'wa': -0.73,
        'sigma_w0': sigma_w0_dr3, 'sigma_wa': sigma_wa_dr3,
        'rho': rho_fisher_neg,
    },
    'B': {
        'label': 'DR3 shifts toward LCDM',
        'w0': -0.90, 'wa': -0.30,
        'sigma_w0': sigma_w0_dr3, 'sigma_wa': sigma_wa_dr3,
        'rho': rho_fisher_neg,
    },
    'C': {
        'label': 'DR3 increases dynamical DE',
        'w0': -0.65, 'wa': -1.0,
        'sigma_w0': sigma_w0_dr3, 'sigma_wa': sigma_wa_dr3,
        'rho': rho_fisher_neg,
    },
}

results = {}
np.random.seed(42)

for key, sc in scenarios.items():
    pr(f"\n--- Scenario {key}: {sc['label']} ---")
    pr(f"  Center: w_0 = {sc['w0']:.3f}, w_a = {sc['wa']:.3f}")
    pr(f"  sigma(w_0) = {sc['sigma_w0']:.4f}, sigma(w_a) = {sc['sigma_wa']:.4f}, rho = {sc['rho']:.2f}")

    cov_sc = build_cov(sc['sigma_w0'], sc['sigma_wa'], sc['rho'])

    # Chi^2 of framework point relative to DR3 center
    chi2_fw = chi2_2d(w0_fw, wa_fw, sc['w0'], sc['wa'], cov_sc)
    sig_fw = sigma_from_chi2(chi2_fw, ndof=2)

    # Chi^2 of LCDM point relative to DR3 center
    chi2_lcdm = chi2_2d(w0_lcdm, wa_lcdm, sc['w0'], sc['wa'], cov_sc)
    sig_lcdm = sigma_from_chi2(chi2_lcdm, ndof=2)

    # Cross-check with task-specified rho = 0.45
    cov_sc_task = build_cov(sc['sigma_w0'], sc['sigma_wa'], rho_fisher_pos)
    chi2_fw_task = chi2_2d(w0_fw, wa_fw, sc['w0'], sc['wa'], cov_sc_task)
    sig_fw_task = sigma_from_chi2(chi2_fw_task, ndof=2)
    chi2_lcdm_task = chi2_2d(w0_lcdm, wa_lcdm, sc['w0'], sc['wa'], cov_sc_task)
    sig_lcdm_task = sigma_from_chi2(chi2_lcdm_task, ndof=2)

    # 95% contour overlap with framework
    overlap_fw = contour_overlap_fraction(sc['w0'], sc['wa'], cov_sc,
                                          w0_fw, 0.0, cov_fw)
    overlap_lcdm = contour_overlap_fraction(sc['w0'], sc['wa'], cov_sc,
                                            w0_lcdm, wa_lcdm, cov_fw)

    pr(f"\n  Framework (w_0={w0_fw:.3f}, w_a=0):")
    pr(f"    chi^2 = {chi2_fw:.3f}  -->  {sig_fw:.2f}-sigma exclusion (rho={sc['rho']:.2f})")
    pr(f"    chi^2 = {chi2_fw_task:.3f}  -->  {sig_fw_task:.2f}-sigma exclusion (rho={rho_fisher_pos})")
    pr(f"    95% contour overlap = {overlap_fw*100:.4f}%")

    pr(f"\n  LCDM (w_0=-1, w_a=0):")
    pr(f"    chi^2 = {chi2_lcdm:.3f}  -->  {sig_lcdm:.2f}-sigma exclusion (rho={sc['rho']:.2f})")
    pr(f"    chi^2 = {chi2_lcdm_task:.3f}  -->  {sig_lcdm_task:.2f}-sigma exclusion (rho={rho_fisher_pos})")
    pr(f"    95% contour overlap = {overlap_lcdm*100:.4f}%")

    # Decision classification
    if sig_fw > 3.0:
        classification = "EXCLUDED (> 3-sigma)"
    elif sig_fw > 2.0:
        classification = "TENSION (2-3 sigma)"
    elif sig_fw > 1.0:
        classification = "VIABLE (1-2 sigma)"
    else:
        classification = "CONSISTENT (< 1-sigma)"

    pr(f"\n  Framework classification: {classification}")

    results[key] = {
        'w0': sc['w0'], 'wa': sc['wa'],
        'sigma_w0': sc['sigma_w0'], 'sigma_wa': sc['sigma_wa'],
        'rho': sc['rho'],
        'chi2_fw': chi2_fw, 'sig_fw': sig_fw,
        'chi2_fw_task': chi2_fw_task, 'sig_fw_task': sig_fw_task,
        'chi2_lcdm': chi2_lcdm, 'sig_lcdm': sig_lcdm,
        'chi2_lcdm_task': chi2_lcdm_task, 'sig_lcdm_task': sig_lcdm_task,
        'overlap_fw': overlap_fw, 'overlap_lcdm': overlap_lcdm,
        'classification': classification,
    }

# =============================================================================
# 7. D_V(z)/r_d at DESI Bins with DR3 Errors
# =============================================================================
pr(f"\n{'='*72}")
pr("D_V(z)/r_d Predictions at DESI Bins (DR3 Error Bars)")
pr(f"{'='*72}")

# Cosmological distance functions (CPL parameterization)
def rho_de_ratio_cpl(a, w0, wa):
    """rho_DE(a) / rho_DE(a=1) for CPL"""
    return a**(-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))

def E_of_z(z, w0, wa):
    """H(z)/H_0"""
    a = 1.0 / (1.0 + z)
    E2 = Om_r / a**4 + Om_m / a**3 + Om_DE * rho_de_ratio_cpl(a, w0, wa)
    return np.sqrt(max(E2, 1e-30))

def comoving_dist_Mpc(z, w0, wa):
    """D_M(z) in Mpc"""
    prefactor = c_light_km_s / H_0
    result, _ = quad(lambda zp: 1.0 / E_of_z(zp, w0, wa), 0, z, limit=200, epsrel=1e-10)
    return prefactor * result

def hubble_dist_Mpc(z, w0, wa):
    """D_H(z) = c/H(z) in Mpc"""
    return (c_light_km_s / H_0) / E_of_z(z, w0, wa)

def DV_Mpc(z, w0, wa):
    """D_V(z) = [z * D_M(z)^2 * D_H(z)]^{1/3} in Mpc"""
    dm = comoving_dist_Mpc(z, w0, wa)
    dh = hubble_dist_Mpc(z, w0, wa)
    return (z * dm**2 * dh)**(1.0/3.0)

def DV_over_rd(z, w0, wa):
    """D_V(z)/r_d"""
    return DV_Mpc(z, w0, wa) / r_d_Mpc

# Compute D_V/r_d for all models
models_dv = {
    'LCDM':      {'w0': w0_lcdm, 'wa': wa_lcdm},
    'Framework': {'w0': w0_fw,   'wa': 0.0},  # w_a = 0 exactly (Volovik)
    'DESI_DR2':  {'w0': w0_desi_dr2, 'wa': wa_desi_dr2},
    'ScA':       {'w0': scenarios['A']['w0'], 'wa': scenarios['A']['wa']},
    'ScB':       {'w0': scenarios['B']['w0'], 'wa': scenarios['B']['wa']},
    'ScC':       {'w0': scenarios['C']['w0'], 'wa': scenarios['C']['wa']},
}

DV_results = {}
for name, m in models_dv.items():
    DV_rd = np.array([DV_over_rd(z, m['w0'], m['wa']) for z in z_eff])
    DM_rd = np.array([comoving_dist_Mpc(z, m['w0'], m['wa']) / r_d_Mpc for z in z_eff])
    DH_rd = np.array([hubble_dist_Mpc(z, m['w0'], m['wa']) / r_d_Mpc for z in z_eff])
    DV_results[name] = {'DV_rd': DV_rd, 'DM_rd': DM_rd, 'DH_rd': DH_rd}

pr(f"\n  {'z':>6s}  {'LCDM':>9s}  {'Framework':>9s}  {'DESI DR2':>9s}  "
   f"{'Sc.A':>9s}  {'Sc.B':>9s}  {'Sc.C':>9s}  {'DR3 err':>9s}")
pr(f"  {'-'*6}  {'-'*9}  {'-'*9}  {'-'*9}  {'-'*9}  {'-'*9}  {'-'*9}  {'-'*9}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {DV_results['LCDM']['DV_rd'][i]:9.4f}  "
       f"{DV_results['Framework']['DV_rd'][i]:9.4f}  "
       f"{DV_results['DESI_DR2']['DV_rd'][i]:9.4f}  "
       f"{DV_results['ScA']['DV_rd'][i]:9.4f}  "
       f"{DV_results['ScB']['DV_rd'][i]:9.4f}  "
       f"{DV_results['ScC']['DV_rd'][i]:9.4f}  "
       f"+/-{sigma_DV_frac_dr3[i] * DV_results['LCDM']['DV_rd'][i]:6.3f}")

# Per-bin framework deviation significance (DR3 errors)
DV_lcdm = DV_results['LCDM']['DV_rd']
DV_fw = DV_results['Framework']['DV_rd']
frac_fw = (DV_fw - DV_lcdm) / DV_lcdm
nsig_fw_dr3 = np.abs(frac_fw) / sigma_DV_frac_dr3

pr(f"\n  Framework fractional deviation from LCDM (DR3 sigma):")
pr(f"  {'z':>6s}  {'(FW-LCDM)/LCDM':>14s}  {'DR3 n-sigma':>12s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {frac_fw[i]*100:+12.4f}%  {nsig_fw_dr3[i]:10.2f}")

chi2_fw_bao_dr3 = np.sum(nsig_fw_dr3**2)
pr(f"\n  Multi-bin chi^2 (FW vs LCDM, {len(z_eff)} bins, DR3): {chi2_fw_bao_dr3:.2f}")
pr(f"  sqrt(chi^2) = {np.sqrt(chi2_fw_bao_dr3):.2f}-sigma")

# Also compute for each scenario vs framework (absolute DV comparison)
for sc_key in ['ScA', 'ScB', 'ScC']:
    DV_sc = DV_results[sc_key]['DV_rd']
    frac_sc_fw = (DV_fw - DV_sc) / DV_sc
    # Use DR3 errors on the scenario model
    sigma_abs_dr3 = sigma_DV_frac_dr3 * DV_sc
    nsig_sc_fw = np.abs(DV_fw - DV_sc) / sigma_abs_dr3
    chi2_sc_fw = np.sum(nsig_sc_fw**2)
    pr(f"\n  Framework vs {sc_key} BAO chi^2 ({len(z_eff)} bins): {chi2_sc_fw:.2f}  "
       f"(sqrt = {np.sqrt(chi2_sc_fw):.2f}-sigma)")

# =============================================================================
# 8. Decision Table
# =============================================================================
pr(f"\n{'='*72}")
pr("DECISION TABLE: Framework Status Under Each DR3 Scenario")
pr(f"{'='*72}")

pr(f"\n  Pre-registered thresholds (S60 DR3-PREREGISTER-60):")
pr(f"    w_a < -0.530  =>  framework excluded at >= 3-sigma")
pr(f"    w_a > -0.350  =>  framework consistent at <= 2-sigma")
pr(f"    -0.530 <= w_a <= -0.350  =>  tension zone (2-3 sigma)")

pr(f"\n  {'Scenario':>10s}  {'w_0':>7s}  {'w_a':>7s}  "
   f"{'FW sig':>8s}  {'LCDM sig':>9s}  {'FW overlap':>11s}  {'Classification':>20s}")
pr(f"  {'-'*10}  {'-'*7}  {'-'*7}  {'-'*8}  {'-'*9}  {'-'*11}  {'-'*20}")
for key in ['A', 'B', 'C']:
    r = results[key]
    pr(f"  {'Scenario '+key:>10s}  {r['w0']:+7.3f}  {r['wa']:+7.3f}  "
       f"{r['sig_fw']:7.2f}s  {r['sig_lcdm']:8.2f}s  "
       f"{r['overlap_fw']*100:9.4f}%  {r['classification']:>20s}")

# What DR3 outcome confirms, tensions, or excludes the framework?
pr(f"\n  Framework confirmed if: DR3 w_a > -0.35 (consistent at < 2-sigma)")
pr(f"  Framework in tension if: -0.53 < DR3 w_a < -0.35 (2-3 sigma)")
pr(f"  Framework excluded if: DR3 w_a < -0.53 (> 3-sigma)")
pr(f"\n  Under Scenario A (w_a={scenarios['A']['wa']}): {results['A']['classification']}")
pr(f"  Under Scenario B (w_a={scenarios['B']['wa']}): {results['B']['classification']}")
pr(f"  Under Scenario C (w_a={scenarios['C']['wa']}): {results['C']['classification']}")

# =============================================================================
# 9. Cross-checks
# =============================================================================
pr(f"\n{'='*72}")
pr("CROSS-CHECKS")
pr(f"{'='*72}")

# Cross-check 1: Consistency with S59 WA-ERROR-PROP-59
sigma_2d_s59 = float(d59['sigma_2d_fw_dr3'])  # 4.29
pr(f"\n  [1] S59 WA-ERROR-PROP-59 reported: sigma_2d(FW vs DR3 center) = {sigma_2d_s59:.2f}")
pr(f"      This computation (Scenario A, rho=-0.85): {results['A']['sig_fw']:.2f}")
pr(f"      S59 assumed DR3 center = DR2 center. Scenario A uses (w_0={scenarios['A']['w0']}, w_a={scenarios['A']['wa']}).")
# Recompute with exact DR2 center for comparison
chi2_exact_dr2 = chi2_2d(w0_fw, 0.0, w0_desi_dr2, wa_desi_dr2, cov_dr3_primary)
sig_exact_dr2 = sigma_from_chi2(chi2_exact_dr2, ndof=2)
pr(f"      With exact DR2 center (w_0={w0_desi_dr2}, w_a={wa_desi_dr2}): {sig_exact_dr2:.2f}")
pr(f"      S59 value: {sigma_2d_s59:.2f}  =>  Discrepancy: {abs(sig_exact_dr2 - sigma_2d_s59):.2f} sigma")
pr(f"      (Differences arise from covariance construction method -- S59 used full MC error propagation.)")

# Cross-check 2: S60 pre-registered values
pr(f"\n  [2] S60 DR3-PREREGISTER-60 scenario results:")
pr(f"      Scenario A: FW at 3.62-sigma (S60) vs {results['A']['sig_fw']:.2f}-sigma (this)")
pr(f"      Scenario B: FW at 1.04-sigma (S60) vs {results['B']['sig_fw']:.2f}-sigma (this)")
pr(f"      (S60 used w_a=-0.70 for A and w_a=-0.30 for B; this uses -0.73 and -0.30.)")

# Cross-check 3: S66 WA-REASSESS-66 confirmed pure FW is best
pr(f"\n  [3] S66 WA-REASSESS-66 confirmed: substrate compaction w_a = +1.121 (wrong sign).")
pr(f"      Pure FW (w_0={w0_fw}, w_a=0) remains the best DE prediction.")
pr(f"      Compaction CLOSED as cosmological prediction. This forecast uses pure FW only.")

# Cross-check 4: Eigenvalues of Fisher matrix (positive definite check)
eigvals_prim = np.linalg.eigvalsh(F_dr3_primary)
eigvals_task = np.linalg.eigvalsh(F_dr3_task)
pr(f"\n  [4] Fisher matrix eigenvalues (positive definite check):")
pr(f"      rho={rho_fisher_neg}: {eigvals_prim}")
pr(f"      rho={rho_fisher_pos}: {eigvals_task}")
pr(f"      Both positive: {np.all(eigvals_prim > 0) and np.all(eigvals_task > 0)}")

# Cross-check 5: DESI-VOLOVIK-67 tension values
pr(f"\n  [5] DESI-VOLOVIK-67 reported:")
pr(f"      1D tension (w_a direction): {float(d67['tension_fw_desi_1d']):.2f}-sigma")
pr(f"      2D tension:                 {float(d67['tension_fw_desi_2d']):.2f}-sigma")
pr(f"      These are DR2 values. DR3 Scenario A (confirming DR2): {results['A']['sig_fw']:.2f}-sigma.")

# =============================================================================
# 10. Gate Verdict
# =============================================================================
pr(f"\n{'='*72}")
pr("GATE VERDICT: DESI-DR3-FORECAST-68")
pr(f"{'='*72}")

gate_detail = (
    f"Fisher forecast for FW (w_0={w0_fw:.3f}, w_a=0) vs DR3. "
    f"Scenario A (confirms DR2): FW {results['A']['sig_fw']:.2f}-sig, LCDM {results['A']['sig_lcdm']:.2f}-sig. "
    f"Scenario B (toward LCDM): FW {results['B']['sig_fw']:.2f}-sig, LCDM {results['B']['sig_lcdm']:.2f}-sig. "
    f"Scenario C (more dyn DE): FW {results['C']['sig_fw']:.2f}-sig, LCDM {results['C']['sig_lcdm']:.2f}-sig. "
    f"Pure FW best. w_a=0 confirmed/excluded by DR3 w_a threshold -0.53."
)

pr(f"\n  Gate: DESI-DR3-FORECAST-68")
pr(f"  Verdict: INFO")
pr(f"  Detail: {gate_detail}")

# =============================================================================
# 11. Plot: w_0 - w_a Plane
# =============================================================================
pr(f"\n{'='*72}")
pr("Generating Plot")
pr(f"{'='*72}")

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# Colors for scenarios
sc_colors = {'A': '#e74c3c', 'B': '#f39c12', 'C': '#2ecc71'}
sc_names = {'A': 'Sc.A: DR3 confirms DR2', 'B': 'Sc.B: Shifts toward LCDM',
            'C': 'Sc.C: More dynamical DE'}

# Draw confidence ellipses for each scenario
for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    cov_sc = build_cov(sc['sigma_w0'], sc['sigma_wa'], sc['rho'])

    # Eigenvalue decomposition for ellipse parameters
    eigvals, eigvecs = np.linalg.eigh(cov_sc)
    order = eigvals.argsort()[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    angle = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))

    for nsig, alpha in [(1, 0.4), (2, 0.2), (3, 0.1)]:
        # chi2 threshold for nsig-sigma (2 DOF)
        chi2_thresh = stats.chi2.ppf(stats.chi2.cdf(nsig**2, df=1), df=2)
        # Actually: for 2D Gaussian, the nsig-sigma contour contains
        # the same fraction as nsig-sigma in 1D, so we use:
        # semi-axes = sqrt(chi2_thresh * eigenvalue)
        # Standard: 1-sig -> chi2 = 2.30, 2-sig -> 6.18, 3-sig -> 11.83
        chi2_2dof = {1: 2.2977, 2: 6.1801, 3: 11.8290}
        scale = np.sqrt(chi2_2dof[nsig])

        width = 2 * np.sqrt(eigvals[0]) * scale  # (local)
        height = 2 * np.sqrt(eigvals[1]) * scale

        ell = Ellipse(xy=(sc['w0'], sc['wa']), width=width, height=height,
                      angle=angle, facecolor=sc_colors[key], alpha=alpha,
                      edgecolor=sc_colors[key], linewidth=1.5 if nsig == 1 else 0.8)
        ax.add_patch(ell)

    # Scenario center
    ax.plot(sc['w0'], sc['wa'], 'x', color=sc_colors[key], markersize=10,
            markeredgewidth=2, label=f"{sc_names[key]} ({results[key]['sig_fw']:.1f}$\\sigma$ FW)")

# Framework prediction
ax.plot(w0_fw, 0.0, '*', color='navy', markersize=18, markeredgecolor='black',
        markeredgewidth=1, label=f'Framework ($w_0$={w0_fw:.3f}, $w_a$=0)', zorder=10)

# LCDM
ax.plot(-1.0, 0.0, 'D', color='blue', markersize=10, markeredgecolor='black',
        markeredgewidth=1, label=r'$\Lambda$CDM ($w_0$=$-1$, $w_a$=0)', zorder=10)

# DESI DR2 best-fit
ax.plot(w0_desi_dr2, wa_desi_dr2, 'o', color='purple', markersize=10,
        markeredgecolor='black', markeredgewidth=1,
        label=f'DESI DR2 ($w_0$={w0_desi_dr2}, $w_a$={wa_desi_dr2})', zorder=10)

# Pre-registered exclusion lines
ax.axhline(y=-0.530, color='gray', linestyle='--', alpha=0.6, linewidth=1)
ax.text(-0.55, -0.52, r'$w_a = -0.530$ (3$\sigma$ exclusion)', fontsize=8, color='gray')
ax.axhline(y=-0.350, color='gray', linestyle=':', alpha=0.6, linewidth=1)
ax.text(-0.55, -0.34, r'$w_a = -0.350$ (2$\sigma$ threshold)', fontsize=8, color='gray')
ax.axhline(y=0.0, color='lightgray', linestyle='-', alpha=0.4, linewidth=0.5)

ax.set_xlabel(r'$w_0$', fontsize=14)
ax.set_ylabel(r'$w_a$', fontsize=14)
ax.set_title('DESI-DR3-FORECAST-68: Framework vs DR3 Projected Contours\n'
             r'($1\sigma$, $2\sigma$, $3\sigma$ ellipses, $\rho = -0.85$)', fontsize=13)
ax.set_xlim(-1.15, -0.50)
ax.set_ylim(-1.6, 0.5)
ax.legend(loc='lower left', fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, 's68_desi_dr3_forecast.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
pr(f"  Plot saved: {plotpath}")

# =============================================================================
# 12. Save NPZ
# =============================================================================
npz_path = os.path.join(SCRIPT_DIR, 's68_desi_dr3_forecast.npz')

save_dict = {
    # Framework
    'w0_fw': w0_fw,
    'wa_fw': wa_fw,
    'sigma_w0_fw': sigma_w0_fw,
    'sigma_wa_fw': sigma_wa_fw,
    # LCDM
    'w0_lcdm': w0_lcdm,
    'wa_lcdm': wa_lcdm,
    # DESI DR2
    'w0_desi_dr2': w0_desi_dr2,
    'wa_desi_dr2': wa_desi_dr2,
    # DR3 projected sensitivities
    'sigma_w0_dr3': sigma_w0_dr3,
    'sigma_wa_dr3': sigma_wa_dr3,
    'rho_desi': rho_fisher_neg,
    'rho_task': rho_fisher_pos,
    # Fisher matrix (primary, rho=-0.85)
    'F_dr3_primary': F_dr3_primary,
    'cov_dr3_primary': cov_dr3_primary,
    # Sound horizon
    'r_d_Mpc': r_d_Mpc,
    # DESI bins
    'z_eff': z_eff,
    'tracer_labels': np.array(tracer_labels),
    'sigma_DV_frac_dr2': sigma_DV_frac_dr2,
    'sigma_DV_frac_dr3': sigma_DV_frac_dr3,
    # D_V/r_d predictions
    'DV_rd_LCDM': DV_results['LCDM']['DV_rd'],
    'DV_rd_Framework': DV_results['Framework']['DV_rd'],
    'DV_rd_DESI_DR2': DV_results['DESI_DR2']['DV_rd'],
    'DV_rd_ScA': DV_results['ScA']['DV_rd'],
    'DV_rd_ScB': DV_results['ScB']['DV_rd'],
    'DV_rd_ScC': DV_results['ScC']['DV_rd'],
    # D_M/r_d and D_H/r_d (framework)
    'DM_rd_Framework': DV_results['Framework']['DM_rd'],
    'DH_rd_Framework': DV_results['Framework']['DH_rd'],
    'DM_rd_LCDM': DV_results['LCDM']['DM_rd'],
    'DH_rd_LCDM': DV_results['LCDM']['DH_rd'],
    # Framework BAO deviation from LCDM
    'frac_fw_from_lcdm': frac_fw,
    'nsig_fw_dr3': nsig_fw_dr3,
    'chi2_fw_bao_dr3': chi2_fw_bao_dr3,
    # Scenario results
    'scenario_labels': np.array(['A', 'B', 'C']),
    'scenario_w0': np.array([results[k]['w0'] for k in ['A', 'B', 'C']]),
    'scenario_wa': np.array([results[k]['wa'] for k in ['A', 'B', 'C']]),
    'chi2_fw_scenarios': np.array([results[k]['chi2_fw'] for k in ['A', 'B', 'C']]),
    'sig_fw_scenarios': np.array([results[k]['sig_fw'] for k in ['A', 'B', 'C']]),
    'chi2_lcdm_scenarios': np.array([results[k]['chi2_lcdm'] for k in ['A', 'B', 'C']]),
    'sig_lcdm_scenarios': np.array([results[k]['sig_lcdm'] for k in ['A', 'B', 'C']]),
    'overlap_fw_scenarios': np.array([results[k]['overlap_fw'] for k in ['A', 'B', 'C']]),
    'overlap_lcdm_scenarios': np.array([results[k]['overlap_lcdm'] for k in ['A', 'B', 'C']]),
    # Gate
    'gate_name': np.array(['DESI-DR3-FORECAST-68']),
    'gate_verdict': np.array(['INFO']),
    'gate_detail': np.array([gate_detail]),
}

np.savez(npz_path, **save_dict)
pr(f"\n  Data saved: {npz_path}")

pr(f"\n{'='*72}")
pr("DESI-DR3-FORECAST-68 COMPLETE")
pr(f"{'='*72}")

log.close()
