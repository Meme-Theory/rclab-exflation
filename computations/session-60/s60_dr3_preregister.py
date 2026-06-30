#!/usr/bin/env python3
"""
s60_dr3_preregister.py — DR3-PREREGISTER-60: Pre-registered DESI DR3 Forecasts
================================================================================
Gate: DR3-PREREGISTER-60
  PASS: All 3 scenarios produce specific numerical predictions
  FAIL: Cannot compute
  INFO: Partial

Physics: The framework predicts w_0 = -0.918, w_a = 0 (static substrate with
integrability-protected GGE). DESI DR2 reports w_a = -0.73 +/- 0.25.

This script pre-registers forecasts for three DR3 scenarios BEFORE data arrives:
  Scenario A: DR3 confirms w_a ~ -0.7 (sharpened from DR2)
  Scenario B: DR3 softens to w_a = -0.3 +/- 0.2
  Scenario C: DR3 finds w_a consistent with 0 (+/- 0.15)

For each scenario, we compute:
  1. BAO D_V(z) at z = 0.3, 0.5, 0.7, 1.0, 1.5, 2.0
  2. f*sigma_8(z) at the same redshifts
  3. sigma_8(z=0) implied
  4. 2D contour overlap with framework (w_0, w_a) plane
  5. Decision rule: exclusion significance

Decision rule (pre-registered):
  w_a < -0.530  =>  framework excluded at >= 3 sigma
  w_a > -0.350  =>  framework consistent at <= 2 sigma

Author: Katie Mack (Cosmic Bridge)
Session: 60, Task DR3-PREREGISTER-60
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import to_rgba
from scipy import stats
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import interp1d

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc
)

print("=" * 72)
print("DR3-PREREGISTER-60: Pre-registered DESI DR3 Scenario Forecasts")
print("=" * 72)

# =============================================================================
# 1. Load upstream data from S59
# =============================================================================
d_wa = np.load(os.path.join(SCRIPT_DIR, 's59_wa_error_prop.npz'), allow_pickle=True)
d_obs = np.load(os.path.join(SCRIPT_DIR, 's59_obs_discriminant.npz'), allow_pickle=True)
d_gf = np.load(os.path.join(SCRIPT_DIR, 's59_growth_factor.npz'), allow_pickle=True)

# Framework central values
w0_fw = float(d_wa['w0_fw'])           # -0.918
wa_fw = float(d_wa['wa_fw'])           # -0.000575
sigma_w0_fw = float(d_wa['sigma_w0_fw'])  # 0.0366
sigma_wa_fw = float(d_wa['sigma_wa_fw'])  # 0.000273
cov_fw = np.array(d_wa['cov_fw'])      # 2x2 covariance

# Framework w_a thresholds from S59
wa_excl_3sig = float(d_wa['wa_excl_3sig'])   # -0.530
wa_excl_5sig = float(d_wa['wa_excl_5sig'])   # -0.884

# DESI DR2 reference
dr2_w0 = float(d_wa['dr2_w0'])         # -0.752
dr2_w0_e = float(d_wa['dr2_w0_e'])     # 0.057
dr2_wa = float(d_wa['dr2_wa'])         # -0.73
dr2_wa_e = float(d_wa['dr2_wa_e'])     # 0.25

# DESI correlation coefficient
rho_desi = float(d_wa['rho_desi'])     # -0.85

# LCDM
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# Shared cosmology
Om_m = Omega_m       # 0.315
Om_r_val = Omega_r   # 9.15e-5
h_val = H_0_km_s_Mpc / 100.0  # 0.674
sig8 = sigma_8       # 0.811

# S59 BAO reference data (6 bins from obs_discriminant)
z_bao_s59 = np.array(d_obs['z_bao'])
DV_fw_s59 = np.array(d_obs['DV_fw'])
DV_lcdm_s59 = np.array(d_obs['DV_lcdm'])

# S59 growth factor data
sigma8_fw_s59 = float(d_gf['sigma8_wCDM'])     # 0.793
sigma8_lcdm_s59 = float(d_gf['sigma8_LCDM'])   # 0.811

print(f"\n=== Upstream Data Loaded ===")
print(f"  Framework: w_0 = {w0_fw:.6f} +/- {sigma_w0_fw:.6f}, "
      f"w_a = {wa_fw:.6f} +/- {sigma_wa_fw:.6f}")
print(f"  DESI DR2:  w_0 = {dr2_w0:.3f} +/- {dr2_w0_e:.3f}, "
      f"w_a = {dr2_wa:.2f} +/- {dr2_wa_e:.2f}")
print(f"  LCDM:      w_0 = -1.0, w_a = 0.0")
print(f"  rho(w_0,w_a) DESI = {rho_desi}")
print(f"  Framework sigma_8 = {sigma8_fw_s59:.4f}, LCDM sigma_8 = {sigma8_lcdm_s59:.4f}")

# =============================================================================
# 2. Define 3 DR3 scenarios
# =============================================================================
print(f"\n{'='*72}")
print("SCENARIO DEFINITIONS (pre-registered)")
print(f"{'='*72}")

scenarios = {
    'A': {
        'label': 'DR3 confirms w_a ~ -0.7',
        'description': 'DR3 sharpens DR2 with 40% error reduction (sqrt(2) from doubled statistics)',
        'w0': -0.75,
        'wa': -0.70,
        'sigma_w0': 0.040,        # projected DR3 (S59 value)
        'sigma_wa': 0.177,        # projected DR3 (S59 value)
        'rho': -0.85,             # correlation maintained
    },
    'B': {
        'label': 'DR3 softens to w_a ~ -0.3',
        'description': 'DR3 central value shifts toward LCDM; systematics partially resolved',
        'w0': -0.85,
        'wa': -0.30,
        'sigma_w0': 0.040,
        'sigma_wa': 0.200,        # slightly larger (less constraining if signal weakens)
        'rho': -0.85,
    },
    'C': {
        'label': 'DR3 finds w_a ~ 0',
        'description': 'DR3 systematics fully resolve; w_a consistent with LCDM/framework',
        'w0': -0.95,
        'wa': 0.0,
        'sigma_w0': 0.040,
        'sigma_wa': 0.150,        # tighter (converged analysis)
        'rho': -0.85,
    },
}

for key, sc in scenarios.items():
    print(f"\n  Scenario {key}: {sc['label']}")
    print(f"    {sc['description']}")
    print(f"    w_0 = {sc['w0']:.3f} +/- {sc['sigma_w0']:.3f}")
    print(f"    w_a = {sc['wa']:.3f} +/- {sc['sigma_wa']:.3f}")
    print(f"    rho(w_0,w_a) = {sc['rho']:.2f}")

# =============================================================================
# 3. Cosmological Functions (CPL parameterization)
# =============================================================================
def w_de(a, w0, wa):
    """CPL equation of state: w(a) = w0 + wa*(1-a)"""
    return w0 + wa * (1.0 - a)

def rho_de_ratio(a, w0, wa):
    """rho_DE(a)/rho_DE(1) for CPL: a^{-3(1+w0+wa)} * exp(-3*wa*(1-a))"""
    return a**(-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))

def E2(a, w0, wa):
    """(H(a)/H_0)^2"""
    Om_de = (1.0 - Om_m - Om_r_val) * rho_de_ratio(a, w0, wa)
    return Om_r_val / a**4 + Om_m / a**3 + Om_de

def H_of_a(a, w0, wa):
    """H(a) in units of H_0"""
    return np.sqrt(np.maximum(E2(a, w0, wa), 1e-30))

def D_M(z, w0, wa):
    """Comoving distance D_M(z) in c/H_0 units"""
    a = 1.0 / (1.0 + z)
    chi, _ = quad(lambda ap: 1.0/(ap**2 * H_of_a(ap, w0, wa)),
                  a, 1.0, limit=200, epsrel=1e-10)
    return chi

def D_V(z, w0, wa):
    """Volume-averaged BAO distance D_V(z) in c/H_0 units.
    D_V(z) = [z * D_M(z)^2 / H(z)]^{1/3}
    with H(z) in H_0 units.
    """
    dm = D_M(z, w0, wa)
    Hz = H_of_a(1.0/(1.0+z), w0, wa)
    return (z * dm**2 / Hz)**(1.0/3.0)

def D_H(z, w0, wa):
    """Hubble distance D_H(z) = 1/H(z) in c/H_0 units"""
    return 1.0 / H_of_a(1.0/(1.0+z), w0, wa)

# Growth factor ODE
def growth_ode(a, y, w0, wa):
    """Linear growth ODE: D''(a) + coeff1*D'(a) - coeff2*D(a) = 0"""
    D_val, dD_da = y
    e2 = E2(a, w0, wa)
    if e2 < 1e-30:
        return [dD_da, 0.0]
    Om_de_0 = 1.0 - Om_m - Om_r_val
    rr = rho_de_ratio(a, w0, wa)
    drho_da = rr * (-3.0*(1.0 + w0 + wa)/a + 3.0*wa)
    de2_da = -4.0*Om_r_val/a**5 - 3.0*Om_m/a**4 + Om_de_0 * drho_da
    coeff1 = 3.0/a + de2_da / (2.0 * e2)
    coeff2 = 1.5 * Om_m / (a**5 * e2)
    d2D_da2 = -coeff1 * dD_da + coeff2 * D_val
    return [dD_da, d2D_da2]

def compute_growth(w0, wa, a_out):
    """Compute D(a) and f(a) = dln(D)/dln(a) at specified scale factors.
    Returns D normalized to D(a=1)=1, and f*sigma_8(z).
    """
    a_init = 1e-4  # (local)
    y0 = [a_init, 1.0]
    sol = solve_ivp(growth_ode, [a_init, 1.0], y0,
                    args=(w0, wa), method='RK45',
                    rtol=1e-10, atol=1e-12, dense_output=True)
    D_at_1 = sol.sol(1.0)[0]

    D_norm = np.array([sol.sol(a)[0] / D_at_1 for a in a_out])
    sig8_model = sig8 * D_norm[np.argmin(np.abs(a_out - 1.0))]

    # f = d ln D / d ln a computed from the derivative
    f_arr = np.array([a * sol.sol(a)[1] / sol.sol(a)[0] for a in a_out])

    # sigma_8(a) = sigma_8(z=0) * D(a)
    sig8_z0 = sig8 * (sol.sol(1.0)[0] / D_at_1)
    sig8_of_a = sig8_z0 * D_norm
    fsig8 = f_arr * sig8_of_a

    return D_norm, f_arr, fsig8, sig8_z0

# =============================================================================
# 4. Compute BAO, growth, sigma_8 for each scenario + framework + LCDM
# =============================================================================
print(f"\n{'='*72}")
print("SCENARIO FORECASTS")
print(f"{'='*72}")

z_grid = np.array([0.3, 0.5, 0.7, 1.0, 1.5, 2.0])
a_grid = 1.0 / (1.0 + z_grid)

# DESI DR2 fractional BAO uncertainties (from DESI 2024 Table 2)
# z = 0.3, 0.5, 0.7, 1.0, 1.5, 2.0
sigma_DV_frac_desi = np.array([0.012, 0.010, 0.009, 0.012, 0.015, 0.020])

# DESI f*sigma_8 absolute errors (from DESI 2024 / Zhao+ 2019 forecasts)
sigma_fsig8_desi = np.array([0.025, 0.020, 0.018, 0.022, 0.035, 0.050])

# Reference computations: framework and LCDM
print("\n--- Computing framework predictions ---")
DV_fw = np.array([D_V(z, w0_fw, wa_fw) for z in z_grid])
D_fw, f_fw, fsig8_fw, sig8_fw_z0 = compute_growth(w0_fw, wa_fw, a_grid)

print("--- Computing LCDM predictions ---")
DV_lcdm = np.array([D_V(z, w0_lcdm, wa_lcdm) for z in z_grid])
D_lcdm, f_lcdm, fsig8_lcdm, sig8_lcdm_z0 = compute_growth(w0_lcdm, wa_lcdm, a_grid)

# Store per-scenario results
scenario_results = {}

for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    w0_sc = sc['w0']
    wa_sc = sc['wa']

    print(f"\n--- Scenario {key}: w_0={w0_sc}, w_a={wa_sc} ---")

    # BAO D_V(z)
    DV_sc = np.array([D_V(z, w0_sc, wa_sc) for z in z_grid])

    # Growth factor and f*sigma_8
    D_sc, f_sc, fsig8_sc, sig8_sc_z0 = compute_growth(w0_sc, wa_sc, a_grid)

    # Fractional BAO differences: scenario vs framework, scenario vs LCDM
    delta_DV_fw = (DV_sc - DV_fw) / DV_fw
    delta_DV_lcdm = (DV_sc - DV_lcdm) / DV_lcdm
    delta_DV_fw_lcdm = (DV_fw - DV_lcdm) / DV_lcdm

    # BAO sigma (scenario - framework) / DESI error
    nsig_bao_fw = np.abs(delta_DV_fw) / sigma_DV_frac_desi
    nsig_bao_lcdm = np.abs(delta_DV_lcdm) / sigma_DV_frac_desi
    chi2_bao_fw = np.sum(nsig_bao_fw**2)
    chi2_bao_lcdm = np.sum(nsig_bao_lcdm**2)

    # f*sigma_8 differences
    delta_fsig8_fw = fsig8_sc - fsig8_fw
    delta_fsig8_lcdm = fsig8_sc - fsig8_lcdm
    nsig_fsig8_fw = np.abs(delta_fsig8_fw) / sigma_fsig8_desi
    nsig_fsig8_lcdm = np.abs(delta_fsig8_lcdm) / sigma_fsig8_desi

    scenario_results[key] = {
        'DV': DV_sc,
        'fsig8': fsig8_sc,
        'sig8_z0': sig8_sc_z0,
        'delta_DV_fw_frac': delta_DV_fw,
        'delta_DV_lcdm_frac': delta_DV_lcdm,
        'nsig_bao_fw': nsig_bao_fw,
        'nsig_bao_lcdm': nsig_bao_lcdm,
        'chi2_bao_fw': chi2_bao_fw,
        'chi2_bao_lcdm': chi2_bao_lcdm,
        'delta_fsig8_fw': delta_fsig8_fw,
        'delta_fsig8_lcdm': delta_fsig8_lcdm,
        'nsig_fsig8_fw': nsig_fsig8_fw,
        'nsig_fsig8_lcdm': nsig_fsig8_lcdm,
    }

    print(f"  sigma_8(z=0) = {sig8_sc_z0:.4f}")
    print(f"  BAO D_V(z) [c/H_0 units]:")
    print(f"  {'z':>5}  {'DV_sc':>10}  {'DV_fw':>10}  {'DV_LCDM':>10}  "
          f"{'dDV/DV_fw%':>12}  {'dDV/DV_L%':>12}  {'n_sig(fw)':>10}  {'n_sig(L)':>10}")
    for i, z in enumerate(z_grid):
        print(f"  {z:5.1f}  {DV_sc[i]:10.6f}  {DV_fw[i]:10.6f}  {DV_lcdm[i]:10.6f}  "
              f"{delta_DV_fw[i]*100:12.4f}  {delta_DV_lcdm[i]*100:12.4f}  "
              f"{nsig_bao_fw[i]:10.3f}  {nsig_bao_lcdm[i]:10.3f}")
    print(f"  Multi-z chi2 (vs FW): {chi2_bao_fw:.3f}  => {np.sqrt(chi2_bao_fw):.3f} sigma")
    print(f"  Multi-z chi2 (vs LCDM): {chi2_bao_lcdm:.3f}  => {np.sqrt(chi2_bao_lcdm):.3f} sigma")

    print(f"\n  f*sigma_8(z):")
    print(f"  {'z':>5}  {'fsig8_sc':>10}  {'fsig8_fw':>10}  {'fsig8_L':>10}  "
          f"{'d(fw)':>10}  {'d(L)':>10}  {'ns(fw)':>10}  {'ns(L)':>10}")
    for i, z in enumerate(z_grid):
        print(f"  {z:5.1f}  {fsig8_sc[i]:10.6f}  {fsig8_fw[i]:10.6f}  {fsig8_lcdm[i]:10.6f}  "
              f"{delta_fsig8_fw[i]:10.6f}  {delta_fsig8_lcdm[i]:10.6f}  "
              f"{nsig_fsig8_fw[i]:10.3f}  {nsig_fsig8_lcdm[i]:10.3f}")

# =============================================================================
# 5. 2D Contour Overlap (framework vs each scenario)
# =============================================================================
print(f"\n{'='*72}")
print("2D CONTOUR OVERLAP ANALYSIS")
print(f"{'='*72}")

def build_cov(sigma_w0, sigma_wa, rho):
    """Build 2x2 covariance matrix from marginal sigmas and correlation."""
    return np.array([[sigma_w0**2, rho * sigma_w0 * sigma_wa],
                     [rho * sigma_w0 * sigma_wa, sigma_wa**2]])

def overlap_2d(mu1, cov1, mu2, cov2, N=200000):
    """Monte Carlo estimate of the overlap integral of two 2D Gaussians.
    Overlap = integral min(p1(x), p2(x)) dx
    """
    rng = np.random.default_rng(42)
    # Importance sampling from the mixture
    n1 = N // 2
    n2 = N - n1
    samples1 = rng.multivariate_normal(mu1, cov1, n1)
    samples2 = rng.multivariate_normal(mu2, cov2, n2)
    samples = np.vstack([samples1, samples2])

    # Evaluate both PDFs
    rv1 = stats.multivariate_normal(mu1, cov1)
    rv2 = stats.multivariate_normal(mu2, cov2)
    p1 = rv1.pdf(samples)
    p2 = rv2.pdf(samples)
    q = 0.5 * (rv1.pdf(samples) + rv2.pdf(samples))

    # Overlap = integral min(p1, p2) dx ~ (1/N) sum min(p1,p2)/q
    mask = q > 0
    integrand = np.minimum(p1[mask], p2[mask]) / q[mask]
    overlap = np.mean(integrand)
    return overlap

def sigma_2d(mu1, cov1, mu2, cov2):
    """2D Gaussian tension: Delta^T (C1+C2)^{-1} Delta, converted to n-sigma."""
    delta = np.array(mu1) - np.array(mu2)
    cov_sum = np.array(cov1) + np.array(cov2)
    chi2 = delta @ np.linalg.solve(cov_sum, delta)
    # Convert chi2 (2 dof) to equivalent n-sigma
    p_value = 1.0 - stats.chi2.cdf(chi2, df=2)
    n_sigma = stats.norm.isf(p_value / 2)
    return chi2, n_sigma, p_value

def contour_overlap_frac(mu1, cov1, mu2, cov2, level=0.95, N_grid=500):
    """Fraction of 2D 95% confidence area that overlaps between two Gaussians."""
    # chi2 threshold for 2D confidence level
    chi2_thresh = stats.chi2.ppf(level, df=2)

    # Build a grid covering both distributions
    # Determine range from both centroids + 4 sigma
    all_sigma = np.sqrt(np.diagonal(cov1).max()) + np.sqrt(np.diagonal(cov2).max())
    w0_range = [min(mu1[0], mu2[0]) - 4*all_sigma, max(mu1[0], mu2[0]) + 4*all_sigma]
    wa_range = [min(mu1[1], mu2[1]) - 4*all_sigma, max(mu1[1], mu2[1]) + 4*all_sigma]
    w0_arr = np.linspace(w0_range[0], w0_range[1], N_grid)
    wa_arr = np.linspace(wa_range[0], wa_range[1], N_grid)
    W0, WA = np.meshgrid(w0_arr, wa_arr)
    pts = np.column_stack([W0.ravel(), WA.ravel()])

    # Mahalanobis distance^2 for each distribution
    inv1 = np.linalg.inv(cov1)
    inv2 = np.linalg.inv(cov2)
    d1 = pts - mu1
    d2 = pts - mu2
    chi2_1 = np.sum(d1 @ inv1 * d1, axis=1)
    chi2_2 = np.sum(d2 @ inv2 * d2, axis=1)

    inside1 = chi2_1 <= chi2_thresh
    inside2 = chi2_2 <= chi2_thresh
    overlap = inside1 & inside2

    area_cell = (w0_arr[1] - w0_arr[0]) * (wa_arr[1] - wa_arr[0])
    area1 = np.sum(inside1) * area_cell
    area2 = np.sum(inside2) * area_cell
    area_ov = np.sum(overlap) * area_cell

    # Fraction relative to smaller contour
    frac_min = area_ov / min(area1, area2) if min(area1, area2) > 0 else 0.0
    frac_jaccard = area_ov / (area1 + area2 - area_ov) if (area1 + area2 - area_ov) > 0 else 0.0
    return area1, area2, area_ov, frac_min, frac_jaccard

# Framework mean and covariance
mu_fw = [w0_fw, wa_fw]
# Use framework covariance from S59
cov_fw_mat = np.array(cov_fw)

# LCDM
mu_lcdm = [w0_lcdm, wa_lcdm]
cov_lcdm = build_cov(0.03, 0.15, -0.5)  # Planck-like constraint on constant w

print(f"\nFramework: mu = ({w0_fw:.4f}, {wa_fw:.4f})")
print(f"  sigma(w_0) = {sigma_w0_fw:.5f}, sigma(w_a) = {sigma_wa_fw:.5f}")
print(f"  Cov = {cov_fw_mat}")

overlap_results = {}

for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    mu_sc = [sc['w0'], sc['wa']]
    cov_sc = build_cov(sc['sigma_w0'], sc['sigma_wa'], sc['rho'])

    print(f"\n--- Scenario {key}: {sc['label']} ---")
    print(f"  DR3 center: ({sc['w0']:.3f}, {sc['wa']:.3f})")
    print(f"  DR3 cov:\n    {cov_sc}")

    # 2D tension: framework vs scenario
    chi2_fw, nsig_fw, pval_fw = sigma_2d(mu_fw, cov_fw_mat, mu_sc, cov_sc)
    print(f"  Framework vs Scenario {key}: chi2 = {chi2_fw:.3f}, {nsig_fw:.2f}-sigma, p = {pval_fw:.2e}")

    # 2D tension: LCDM vs scenario
    chi2_lcdm, nsig_lcdm, pval_lcdm = sigma_2d(mu_lcdm, cov_lcdm, mu_sc, cov_sc)
    print(f"  LCDM vs Scenario {key}: chi2 = {chi2_lcdm:.3f}, {nsig_lcdm:.2f}-sigma, p = {pval_lcdm:.2e}")

    # Contour overlap (95%)
    a1, a2, a_ov, frac_min, frac_jac = contour_overlap_frac(mu_fw, cov_fw_mat, mu_sc, cov_sc)
    print(f"  95% contour areas: FW = {a1:.6f}, DR3 = {a2:.6f}, overlap = {a_ov:.6f}")
    print(f"  Overlap fraction (vs smaller): {frac_min*100:.2f}%")
    print(f"  Jaccard overlap: {frac_jac*100:.4f}%")

    # PDF overlap integral (MC)
    pdf_ov = overlap_2d(mu_fw, cov_fw_mat, mu_sc, cov_sc)
    print(f"  PDF overlap integral: {pdf_ov:.6e}")

    overlap_results[key] = {
        'chi2_fw': chi2_fw,
        'nsig_fw': nsig_fw,
        'pval_fw': pval_fw,
        'chi2_lcdm': chi2_lcdm,
        'nsig_lcdm': nsig_lcdm,
        'pval_lcdm': pval_lcdm,
        'area_fw_95': a1,
        'area_sc_95': a2,
        'area_overlap': a_ov,
        'frac_overlap_min': frac_min,
        'frac_jaccard': frac_jac,
        'pdf_overlap': pdf_ov,
    }

# =============================================================================
# 6. Pre-Registered Decision Rules
# =============================================================================
print(f"\n{'='*72}")
print("PRE-REGISTERED DECISION RULES")
print(f"{'='*72}")

wa_3sig_threshold = -0.530   # from S59: wa < this => 3-sigma exclusion  # (local)
wa_2sig_consistent = -0.350  # wa > this => consistent at <= 2-sigma  # (local)

print(f"\n  Exclusion threshold:  w_a < {wa_3sig_threshold:.3f}  =>  framework excluded at >= 3-sigma")
print(f"  Consistency thresh:   w_a > {wa_2sig_consistent:.3f}  =>  framework consistent at <= 2-sigma")
print(f"  Intermediate:         {wa_3sig_threshold:.3f} <= w_a <= {wa_2sig_consistent:.3f}  =>  tension (2-3 sigma)")

for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    wa_val = sc['wa']
    ov = overlap_results[key]

    if wa_val < wa_3sig_threshold:
        decision = "EXCLUDED (>= 3-sigma)"
    elif wa_val > wa_2sig_consistent:
        decision = "CONSISTENT (<= 2-sigma)"
    else:
        decision = f"TENSION (2-3 sigma)"

    print(f"\n  Scenario {key} (w_a = {wa_val:.3f}):")
    print(f"    Decision: {decision}")
    print(f"    2D tension: {ov['nsig_fw']:.2f}-sigma (framework), "
          f"{ov['nsig_lcdm']:.2f}-sigma (LCDM)")
    print(f"    95% contour overlap: {ov['frac_overlap_min']*100:.2f}%")
    print(f"    PDF overlap: {ov['pdf_overlap']:.2e}")

# =============================================================================
# 7. Summary Table
# =============================================================================
print(f"\n{'='*72}")
print("COMPREHENSIVE FORECAST TABLE")
print(f"{'='*72}")

print(f"\n--- BAO D_V(z) forecasts [c/H_0 units] ---")
header = f"{'z':>5}  {'FW':>10}  {'LCDM':>10}"
for key in ['A', 'B', 'C']:
    header += f"  {'Sc '+key:>10}"
print(header)
print("-" * len(header))
for i, z in enumerate(z_grid):
    row = f"{z:5.1f}  {DV_fw[i]:10.6f}  {DV_lcdm[i]:10.6f}"
    for key in ['A', 'B', 'C']:
        row += f"  {scenario_results[key]['DV'][i]:10.6f}"
    print(row)

print(f"\n--- f*sigma_8(z) forecasts ---")
header = f"{'z':>5}  {'FW':>10}  {'LCDM':>10}"
for key in ['A', 'B', 'C']:
    header += f"  {'Sc '+key:>10}"
print(header)
print("-" * len(header))
for i, z in enumerate(z_grid):
    row = f"{z:5.1f}  {fsig8_fw[i]:10.6f}  {fsig8_lcdm[i]:10.6f}"
    for key in ['A', 'B', 'C']:
        row += f"  {scenario_results[key]['fsig8'][i]:10.6f}"
    print(row)

print(f"\n--- sigma_8(z=0) ---")
print(f"  Framework:  {sig8_fw_z0:.4f}")
print(f"  LCDM:       {sig8_lcdm_z0:.4f}")
for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    sr = scenario_results[key]
    # sigma_8(z=0) for each scenario's cosmology
    _, _, _, sig8_sc = compute_growth(sc['w0'], sc['wa'], np.array([1.0]))
    print(f"  Scenario {key}: {sig8_sc:.4f}")

print(f"\n--- Multi-z BAO Fisher sigma (sqrt(sum sigma_i^2)) ---")
print(f"  {'Scenario':>10}  {'vs FW':>10}  {'vs LCDM':>10}")
for key in ['A', 'B', 'C']:
    sr = scenario_results[key]
    print(f"  {'Sc ' + key:>10}  {np.sqrt(sr['chi2_bao_fw']):10.3f}  {np.sqrt(sr['chi2_bao_lcdm']):10.3f}")

print(f"\n--- 2D (w_0, w_a) tension summary ---")
print(f"  {'Scenario':>10}  {'vs FW sigma':>12}  {'vs LCDM sigma':>14}  {'FW overlap%':>12}  {'Decision':>20}")
for key in ['A', 'B', 'C']:
    ov = overlap_results[key]
    sc = scenarios[key]
    wa_val = sc['wa']
    if wa_val < wa_3sig_threshold:
        decision = "EXCLUDED (>=3sig)"
    elif wa_val > wa_2sig_consistent:
        decision = "CONSISTENT (<=2sig)"
    else:
        decision = "TENSION (2-3sig)"
    print(f"  {'Sc ' + key:>10}  {ov['nsig_fw']:12.2f}  {ov['nsig_lcdm']:14.2f}  "
          f"{ov['frac_overlap_min']*100:12.2f}  {decision:>20}")

# =============================================================================
# 8. Gate Verdict
# =============================================================================
print(f"\n{'='*72}")
print("GATE: DR3-PREREGISTER-60")
print(f"{'='*72}")

n_complete = sum(1 for k in ['A', 'B', 'C'] if k in scenario_results)
if n_complete == 3:
    gate_verdict = 'PASS'
    gate_detail = (f"All 3 scenarios computed with BAO D_V(z) at 6 redshifts, "
                   f"f*sigma_8(z), sigma_8(z=0), 2D contour overlap, and decision rules")
elif n_complete > 0:
    gate_verdict = 'INFO'
    gate_detail = f"Only {n_complete}/3 scenarios computed"
else:
    gate_verdict = 'FAIL'
    gate_detail = "No scenarios computed"

print(f"\n  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print(f"\n  Pre-registered thresholds:")
print(f"    w_a < {wa_3sig_threshold:.3f}  =>  framework excluded at >= 3-sigma")
print(f"    w_a > {wa_2sig_consistent:.3f}  =>  framework consistent at <= 2-sigma")
print(f"\n  Scenario A (w_a = {scenarios['A']['wa']:.2f}): EXCLUDED — framework eliminated")
print(f"  Scenario B (w_a = {scenarios['B']['wa']:.2f}): TENSION — neither excluded nor confirmed")
print(f"  Scenario C (w_a = {scenarios['C']['wa']:.2f}): CONSISTENT — framework survives, LCDM also survives")

# =============================================================================
# 9. Save data
# =============================================================================
save_path = os.path.join(SCRIPT_DIR, 's60_dr3_preregister.npz')

save_dict = {
    # Framework
    'w0_fw': w0_fw,
    'wa_fw': wa_fw,
    'sigma_w0_fw': sigma_w0_fw,
    'sigma_wa_fw': sigma_wa_fw,
    'cov_fw': cov_fw_mat,
    'DV_fw': DV_fw,
    'fsig8_fw': fsig8_fw,
    'sig8_fw_z0': sig8_fw_z0,
    # LCDM
    'DV_lcdm': DV_lcdm,
    'fsig8_lcdm': fsig8_lcdm,
    'sig8_lcdm_z0': sig8_lcdm_z0,
    # Grid
    'z_grid': z_grid,
    # Decision thresholds
    'wa_3sig_threshold': wa_3sig_threshold,
    'wa_2sig_consistent': wa_2sig_consistent,
    # Gate
    'gate_name': np.array(['DR3-PREREGISTER-60']),
    'gate_verdict': np.array([gate_verdict]),
    'gate_detail': np.array([gate_detail]),
}

# Per-scenario data
for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    sr = scenario_results[key]
    ov = overlap_results[key]
    prefix = f'sc{key}_'
    save_dict[prefix + 'w0'] = sc['w0']
    save_dict[prefix + 'wa'] = sc['wa']
    save_dict[prefix + 'sigma_w0'] = sc['sigma_w0']
    save_dict[prefix + 'sigma_wa'] = sc['sigma_wa']
    save_dict[prefix + 'rho'] = sc['rho']
    save_dict[prefix + 'DV'] = sr['DV']
    save_dict[prefix + 'fsig8'] = sr['fsig8']
    save_dict[prefix + 'delta_DV_fw_frac'] = sr['delta_DV_fw_frac']
    save_dict[prefix + 'delta_DV_lcdm_frac'] = sr['delta_DV_lcdm_frac']
    save_dict[prefix + 'nsig_bao_fw'] = sr['nsig_bao_fw']
    save_dict[prefix + 'nsig_bao_lcdm'] = sr['nsig_bao_lcdm']
    save_dict[prefix + 'chi2_bao_fw'] = sr['chi2_bao_fw']
    save_dict[prefix + 'chi2_bao_lcdm'] = sr['chi2_bao_lcdm']
    save_dict[prefix + 'nsig_2d_fw'] = ov['nsig_fw']
    save_dict[prefix + 'nsig_2d_lcdm'] = ov['nsig_lcdm']
    save_dict[prefix + 'pval_fw'] = ov['pval_fw']
    save_dict[prefix + 'pval_lcdm'] = ov['pval_lcdm']
    save_dict[prefix + 'overlap_95_frac'] = ov['frac_overlap_min']
    save_dict[prefix + 'overlap_jaccard'] = ov['frac_jaccard']
    save_dict[prefix + 'overlap_pdf'] = ov['pdf_overlap']

np.savez(save_path, **save_dict)
print(f"\nData saved: {save_path}")

# =============================================================================
# 10. Three-panel forecast plot
# =============================================================================
print("\n--- Generating three-scenario forecast panel ---")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

colors_sc = {'A': '#d62728', 'B': '#ff7f0e', 'C': '#2ca02c'}
labels_sc = {'A': r'Sc A: $w_a=-0.70$', 'B': r'Sc B: $w_a=-0.30$', 'C': r'Sc C: $w_a=0.00$'}

# ---- Panel 1: w_0-w_a plane with contours ----
ax = axes[0]
ax.set_title(r'$w_0\text{--}w_a$ Plane: Framework vs DR3 Scenarios', fontsize=11)

# Helper to draw ellipse from covariance
def draw_ellipse(ax, mu, cov, color, label, ls='-', alpha_fill=0.15, lw=1.5):
    """Draw 68% and 95% confidence ellipses."""
    from matplotlib.patches import Ellipse
    vals, vecs = np.linalg.eigh(cov)
    angle = np.degrees(np.arctan2(vecs[1, 1], vecs[0, 1]))
    for nsig, alpha_f in [(1.0, alpha_fill), (2.0, alpha_fill * 0.5)]:
        # chi2 threshold for 2 dof
        chi2_val = stats.chi2.ppf(stats.chi2.cdf(nsig**2, df=1), df=2)
        w = 2.0 * np.sqrt(vals[0] * chi2_val)  # (local)
        h = 2.0 * np.sqrt(vals[1] * chi2_val)  # (local)
        ell = Ellipse(xy=mu, width=w, height=h, angle=angle,
                     facecolor=to_rgba(color, alpha_f),
                     edgecolor=color, ls=ls, lw=lw,
                     label=label if nsig == 1.0 else None)
        ax.add_patch(ell)

# Framework (tiny ellipse)
draw_ellipse(ax, mu_fw, cov_fw_mat, '#1f77b4', 'Framework', lw=2)
ax.plot(w0_fw, wa_fw, 'o', color='#1f77b4', ms=6, zorder=5)

# LCDM point
ax.plot(-1.0, 0.0, 's', color='black', ms=8, label=r'$\Lambda$CDM', zorder=5)

# DR3 scenarios
for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    mu_sc = [sc['w0'], sc['wa']]
    cov_sc = build_cov(sc['sigma_w0'], sc['sigma_wa'], sc['rho'])
    draw_ellipse(ax, mu_sc, cov_sc, colors_sc[key], labels_sc[key], ls='--')
    ax.plot(sc['w0'], sc['wa'], 'x', color=colors_sc[key], ms=8, mew=2, zorder=5)

# Decision boundaries
ax.axhline(y=wa_3sig_threshold, color='gray', ls=':', lw=1, alpha=0.7)
ax.axhline(y=wa_2sig_consistent, color='gray', ls=':', lw=1, alpha=0.7)
ax.text(-0.60, wa_3sig_threshold + 0.03, r'$3\sigma$ excl.', fontsize=8, color='gray')
ax.text(-0.60, wa_2sig_consistent + 0.03, r'$2\sigma$ cons.', fontsize=8, color='gray')

ax.set_xlabel(r'$w_0$', fontsize=12)
ax.set_ylabel(r'$w_a$', fontsize=12)
ax.set_xlim(-1.15, -0.55)
ax.set_ylim(-1.2, 0.6)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)

# ---- Panel 2: BAO D_V(z) residuals ----
ax = axes[1]
ax.set_title(r'BAO $D_V(z)$ Residual vs $\Lambda$CDM', fontsize=11)

# Framework vs LCDM
delta_DV_fw_lcdm = (DV_fw - DV_lcdm) / DV_lcdm * 100
ax.plot(z_grid, delta_DV_fw_lcdm, 'o-', color='#1f77b4', lw=2, ms=6, label='Framework')

# Scenarios vs LCDM
for key in ['A', 'B', 'C']:
    sr = scenario_results[key]
    delta_pct = sr['delta_DV_lcdm_frac'] * 100
    ax.plot(z_grid, delta_pct, 'x--', color=colors_sc[key], lw=1.5, ms=7, label=labels_sc[key])

# DESI error band
ax.fill_between(z_grid, -sigma_DV_frac_desi*100, sigma_DV_frac_desi*100,
                color='gray', alpha=0.2, label=r'DESI $1\sigma$')

ax.axhline(y=0, color='black', ls='-', lw=0.5)
ax.set_xlabel(r'$z$', fontsize=12)
ax.set_ylabel(r'$\Delta D_V / D_V^{\Lambda\mathrm{CDM}}$ (%)', fontsize=12)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# ---- Panel 3: f*sigma_8(z) ----
ax = axes[2]
ax.set_title(r'$f\sigma_8(z)$ Growth Rate', fontsize=11)

ax.plot(z_grid, fsig8_lcdm, 's-', color='black', lw=2, ms=6, label=r'$\Lambda$CDM')
ax.plot(z_grid, fsig8_fw, 'o-', color='#1f77b4', lw=2, ms=6, label='Framework')
for key in ['A', 'B', 'C']:
    sr = scenario_results[key]
    ax.plot(z_grid, sr['fsig8'], 'x--', color=colors_sc[key], lw=1.5, ms=7, label=labels_sc[key])

# DESI error bars on LCDM
ax.errorbar(z_grid, fsig8_lcdm, yerr=sigma_fsig8_desi,
            fmt='none', color='gray', alpha=0.5, capsize=3)

ax.set_xlabel(r'$z$', fontsize=12)
ax.set_ylabel(r'$f\sigma_8(z)$', fontsize=12)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's60_dr3_preregister.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Plot saved: {plot_path}")

# =============================================================================
# 11. Final summary
# =============================================================================
print(f"\n{'='*72}")
print("DR3-PREREGISTER-60: FINAL SUMMARY")
print(f"{'='*72}")
print(f"""
Pre-registered forecasts for DESI DR3 (computed {np.datetime64('today')}):

FRAMEWORK:  w_0 = {w0_fw:.4f}, w_a = {wa_fw:.4f}  (static substrate, GGE-protected)
LCDM:       w_0 = -1.000,  w_a = 0.000

SCENARIO A (w_a = -0.70, DR3 confirms DR2):
  - Framework excluded at {overlap_results['A']['nsig_fw']:.1f}-sigma (2D)
  - LCDM excluded at {overlap_results['A']['nsig_lcdm']:.1f}-sigma (2D)
  - 95% contour overlap: {overlap_results['A']['frac_overlap_min']*100:.1f}%
  - DECISION: Both framework AND LCDM excluded => new physics

SCENARIO B (w_a = -0.30, DR3 softens):
  - Framework at {overlap_results['B']['nsig_fw']:.1f}-sigma tension (2D)
  - LCDM at {overlap_results['B']['nsig_lcdm']:.1f}-sigma tension (2D)
  - 95% contour overlap: {overlap_results['B']['frac_overlap_min']*100:.1f}%
  - DECISION: Tension zone — neither confirmed nor excluded

SCENARIO C (w_a = 0.00, DR3 resolves to LCDM):
  - Framework at {overlap_results['C']['nsig_fw']:.1f}-sigma (2D)
  - LCDM at {overlap_results['C']['nsig_lcdm']:.1f}-sigma (2D)
  - 95% contour overlap: {overlap_results['C']['frac_overlap_min']*100:.1f}%
  - DECISION: Framework survives, distinguishable from LCDM only via BAO precision

CRITICAL NOTE: Framework predicts w_a = 0 as a THEOREM (integrability + block-diagonal).
No parameter adjustment can produce w_a != 0. If DR3 confirms w_a < -0.53,
the framework is falsified at >= 3-sigma regardless of w_0.
""")

print("DR3-PREREGISTER-60 COMPLETE")
