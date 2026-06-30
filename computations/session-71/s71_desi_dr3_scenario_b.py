#!/usr/bin/env python3
"""
s71_desi_dr3_scenario_b.py -- DESI-DR3-SCENARIO-B-PRECISE-71: Fisher Forecast
===============================================================================
Gate: DESI-DR3-SCENARIO-B-PRECISE-71
  INFO: Report expected sigma(w_0), framework tension in sigma, P(framework|DR3).

Physics:
  The framework predicts w_0 = -0.918 from the Volovik relaxation mechanism.
  The canonical prediction is w_a = 0 (structural protection from integrability
  + block-diagonal structure). The task specifies w_a = 0.066 as a "Scenario B"
  framework value; this is treated as a small higher-order correction.

  DESI DR2 measured w_0 = -0.752 +/- 0.065, w_a = -0.73 +/- 0.25 (task values).
  DR3 approximately doubles effective volume => sigma_DR3 ~ sigma_DR2 / sqrt(2).

  This computation:
    1. Constructs the DR3 Fisher matrix from DR2 by volume scaling.
    2. Evaluates framework tension under Scenario B (DR3 center: w_0=-0.90, w_a=-0.30).
    3. Computes DR3 center-shift sensitivity (what if DR3 shifts toward framework?).
    4. Derives posterior probability P(framework | DR3) via Savage-Dickey density ratio.
    5. Compares w_a discrimination: framework (0.066) vs DESI DR2 (-0.73).

Author: Katie Mack (Cosmic Bridge)
Session: 71, Task DESI-DR3-SCENARIO-B-PRECISE-71
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy import stats
from scipy.integrate import quad

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, c_light_km_s,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s71_desi_dr3_scenario_b_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("DESI-DR3-SCENARIO-B-PRECISE-71: Fisher Forecast for Scenario B")
pr("=" * 72)

# =============================================================================
# 1. Cosmological Parameters (from canonical_constants)
# =============================================================================
Om_m = Omega_m           # 0.315
Om_b = Omega_b           # 0.0493
Om_r = Omega_r           # 9.15e-5
Om_DE = 1.0 - Om_m - Om_r
h = H_0_km_s_Mpc / 100.0
H_0 = H_0_km_s_Mpc

pr(f"\nCosmological parameters (Planck 2018, from canonical_constants):")
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

d70 = np.load(os.path.join(SCRIPT_DIR, 's70_desi_dr3_update.npz'), allow_pickle=True)

# Framework predictions (from upstream)
w0_fw = float(d70['w0_fw'])          # -0.918
wa_fw_canonical = float(d70['wa_fw'])  # 0.0 (canonical)
wa_fw_scenB = 0.066                    # Task-specified Scenario B value  # (local)

# DESI DR2 measurements (task values)
w0_desi_dr2 = float(d70['w0_desi_dr2'])   # -0.752
wa_desi_dr2 = float(d70['wa_desi_dr2'])   # -0.73
w0_desi_dr2_err = 0.065                    # Task-specified DR2 error  # (local)
wa_desi_dr2_err = 0.25                     # DESI DR2 w_a error (from S67)  # (local)
rho_desi = float(d70['rho_desi'])         # -0.85 (w_0-w_a correlation)

# LCDM
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# DESI DR3 Scenario B center (from S60/S68 pre-registration)
w0_scenB = -0.90    # DR3 shifts toward more negative w_0  # (local)
wa_scenB = -0.30    # DR3 w_a less negative than DR2  # (local)

# Upstream DR3 projections from S70 (for cross-check)
sigma_w0_dr3_5x = float(d70['sigma_w0_dr3_5x'])    # S70: 5x DR1 volume
sigma_wa_dr3_5x = float(d70['sigma_wa_dr3_5x'])
sigma_w0_dr3_s68 = float(d70['sigma_w0_dr3_s68'])  # S68 Fisher
sigma_wa_dr3_s68 = float(d70['sigma_wa_dr3_s68'])

pr(f"\n  Framework prediction:")
pr(f"    w_0 = {w0_fw:.4f}")
pr(f"    w_a = {wa_fw_canonical:.4f} (canonical, Volovik protection)")
pr(f"    w_a = {wa_fw_scenB:.4f} (Scenario B, task-specified)")
pr(f"\n  DESI DR2 measurement (task values):")
pr(f"    w_0 = {w0_desi_dr2} +/- {w0_desi_dr2_err}")
pr(f"    w_a = {wa_desi_dr2} +/- {wa_desi_dr2_err}")
pr(f"    rho(w_0, w_a) = {rho_desi}")
pr(f"\n  LCDM: w_0 = {w0_lcdm}, w_a = {wa_lcdm}")
pr(f"\n  Scenario B (DR3 center):")
pr(f"    w_0 = {w0_scenB}, w_a = {wa_scenB}")
pr(f"\n  S70 DR3 projections (cross-check):")
pr(f"    sigma(w_0)_5x = {sigma_w0_dr3_5x:.4f}")
pr(f"    sigma(w_a)_5x = {sigma_wa_dr3_5x:.4f}")
pr(f"    sigma(w_0)_s68 = {sigma_w0_dr3_s68:.4f}")
pr(f"    sigma(w_a)_s68 = {sigma_wa_dr3_s68:.4f}")

# =============================================================================
# 3. DR3 Fisher Matrix from Volume Scaling
# =============================================================================
pr(f"\n{'='*72}")
pr("DR3 Fisher Matrix Construction")
pr(f"{'='*72}")

# Task: V_DR3/V_DR2 ~ 2.0, sigma scales as 1/sqrt(V)
V_ratio = 2.0   # DR3/DR2 effective volume ratio (task specification)  # (local)
sigma_w0_dr3 = w0_desi_dr2_err / np.sqrt(V_ratio)
sigma_wa_dr3 = wa_desi_dr2_err / np.sqrt(V_ratio)

pr(f"\n  Volume ratio V_DR3/V_DR2 = {V_ratio:.1f}")
pr(f"  sigma(w_0)_DR3 = {w0_desi_dr2_err:.3f} / sqrt({V_ratio}) = {sigma_w0_dr3:.4f}")
pr(f"  sigma(w_a)_DR3 = {wa_desi_dr2_err:.3f} / sqrt({V_ratio}) = {sigma_wa_dr3:.4f}")
pr(f"  rho = {rho_desi} (assumed unchanged)")

# Build covariance and Fisher matrices
def build_cov(sigma_w0, sigma_wa, rho):
    """2x2 covariance matrix for (w_0, w_a)."""
    return np.array([
        [sigma_w0**2,                 rho * sigma_w0 * sigma_wa],
        [rho * sigma_w0 * sigma_wa,   sigma_wa**2]
    ])

def chi2_2d(w0_test, wa_test, w0_cen, wa_cen, cov):
    """Chi^2 for point (w0_test, wa_test) relative to center."""
    dw = np.array([w0_test - w0_cen, wa_test - wa_cen])
    F = np.linalg.inv(cov)
    return float(dw @ F @ dw)

def sigma_from_chi2(chi2_val, ndof=2):
    """Convert chi^2 to equivalent Gaussian sigma."""
    p_val = 1.0 - stats.chi2.cdf(chi2_val, df=ndof)
    p_val = max(p_val, 1e-300)
    return stats.norm.isf(p_val / 2.0)

# DR2 covariance (for reference)
cov_dr2 = build_cov(w0_desi_dr2_err, wa_desi_dr2_err, rho_desi)
F_dr2 = np.linalg.inv(cov_dr2)

# DR3 covariance (task: 2x volume)
cov_dr3 = build_cov(sigma_w0_dr3, sigma_wa_dr3, rho_desi)
F_dr3 = np.linalg.inv(cov_dr3)

pr(f"\n  DR2 Covariance:")
pr(f"    [[{cov_dr2[0,0]:.6e}, {cov_dr2[0,1]:.6e}],")
pr(f"     [{cov_dr2[1,0]:.6e}, {cov_dr2[1,1]:.6e}]]")
pr(f"  DR2 Fisher:")
pr(f"    [[{F_dr2[0,0]:.4f}, {F_dr2[0,1]:.4f}],")
pr(f"     [{F_dr2[1,0]:.4f}, {F_dr2[1,1]:.4f}]]")
pr(f"\n  DR3 Covariance:")
pr(f"    [[{cov_dr3[0,0]:.6e}, {cov_dr3[0,1]:.6e}],")
pr(f"     [{cov_dr3[1,0]:.6e}, {cov_dr3[1,1]:.6e}]]")
pr(f"  DR3 Fisher:")
pr(f"    [[{F_dr3[0,0]:.4f}, {F_dr3[0,1]:.4f}],")
pr(f"     [{F_dr3[1,0]:.4f}, {F_dr3[1,1]:.4f}]]")

# Cross-check: Fisher scales linearly with volume
pr(f"\n  Cross-check: F_DR3 / F_DR2 ratios:")
for i in range(2):
    for j in range(2):
        ratio = F_dr3[i,j] / F_dr2[i,j] if F_dr2[i,j] != 0 else 0
        pr(f"    F_DR3[{i},{j}] / F_DR2[{i},{j}] = {ratio:.4f} (expect {V_ratio:.1f})")

# =============================================================================
# 4. Framework Tension Under Scenario B
# =============================================================================
pr(f"\n{'='*72}")
pr("SCENARIO B: Framework Tension Forecast")
pr(f"{'='*72}")

# 4a. If DR3 center stays at DR2 values (no shift)
chi2_fw_dr2cen_dr3err = chi2_2d(w0_fw, wa_fw_scenB, w0_desi_dr2, wa_desi_dr2, cov_dr3)
sig_fw_dr2cen_dr3err = sigma_from_chi2(chi2_fw_dr2cen_dr3err, ndof=2)

pr(f"\n  If DR3 center = DR2 center ({w0_desi_dr2}, {wa_desi_dr2}):")
pr(f"    FW ({w0_fw}, {wa_fw_scenB}): chi^2 = {chi2_fw_dr2cen_dr3err:.3f}, "
   f"{sig_fw_dr2cen_dr3err:.2f}-sigma")

# 4b. Under Scenario B center (w_0 = -0.90, w_a = -0.30)
chi2_fw_scenB = chi2_2d(w0_fw, wa_fw_scenB, w0_scenB, wa_scenB, cov_dr3)
sig_fw_scenB = sigma_from_chi2(chi2_fw_scenB, ndof=2)

chi2_lcdm_scenB = chi2_2d(w0_lcdm, wa_lcdm, w0_scenB, wa_scenB, cov_dr3)
sig_lcdm_scenB = sigma_from_chi2(chi2_lcdm_scenB, ndof=2)

chi2_fw_canon_scenB = chi2_2d(w0_fw, wa_fw_canonical, w0_scenB, wa_scenB, cov_dr3)
sig_fw_canon_scenB = sigma_from_chi2(chi2_fw_canon_scenB, ndof=2)

pr(f"\n  Scenario B center ({w0_scenB}, {wa_scenB}) with DR3 errors:")
pr(f"    FW (w_a = {wa_fw_scenB}):")
pr(f"      chi^2 = {chi2_fw_scenB:.3f}, tension = {sig_fw_scenB:.2f}-sigma")
pr(f"    FW (w_a = {wa_fw_canonical}, canonical):")
pr(f"      chi^2 = {chi2_fw_canon_scenB:.3f}, tension = {sig_fw_canon_scenB:.2f}-sigma")
pr(f"    LCDM:")
pr(f"      chi^2 = {chi2_lcdm_scenB:.3f}, tension = {sig_lcdm_scenB:.2f}-sigma")

# 4c. 1D marginal tensions
# Marginal tension in w_0 only
delta_w0 = abs(w0_fw - w0_scenB)
tension_w0_1d = delta_w0 / sigma_w0_dr3
pr(f"\n  1D marginal tensions (Scenario B center):")
pr(f"    w_0: |{w0_fw} - ({w0_scenB})| / {sigma_w0_dr3:.4f} = {tension_w0_1d:.2f}-sigma")

# Marginal tension in w_a
delta_wa_scenB = abs(wa_fw_scenB - wa_scenB)
delta_wa_canon = abs(wa_fw_canonical - wa_scenB)
tension_wa_scenB = delta_wa_scenB / sigma_wa_dr3
tension_wa_canon = delta_wa_canon / sigma_wa_dr3
pr(f"    w_a (ScB): |{wa_fw_scenB} - ({wa_scenB})| / {sigma_wa_dr3:.4f} = {tension_wa_scenB:.2f}-sigma")
pr(f"    w_a (canon): |{wa_fw_canonical} - ({wa_scenB})| / {sigma_wa_dr3:.4f} = {tension_wa_canon:.2f}-sigma")

# For the specific tension mentioned in the task:
# |(-0.918) - (-0.752)| / 0.046
task_tension = abs(w0_fw - w0_desi_dr2) / sigma_w0_dr3
pr(f"\n  Task cross-check:")
pr(f"    |(-0.918) - (-0.752)| / {sigma_w0_dr3:.3f} = {task_tension:.2f}-sigma (1D, DR2 center)")

# =============================================================================
# 5. DR3 Center-Shift Sensitivity
# =============================================================================
pr(f"\n{'='*72}")
pr("DR3 Center-Shift Sensitivity Analysis")
pr(f"{'='*72}")

# DR1 center: w_0 = -0.727, w_a = -1.05 (approximate, from DESI 2024 DR1)
# DR2 center: w_0 = -0.752, w_a = -0.73
# Trend: w_0 shifts more negative by ~0.025 per release, w_a shifts toward 0 by ~0.32
delta_w0_per_release = w0_desi_dr2 - (-0.727)  # = -0.025
delta_wa_per_release = wa_desi_dr2 - (-1.05)   # = +0.32

# Projected DR3 center if trend continues
w0_dr3_trend = w0_desi_dr2 + delta_w0_per_release   # -0.777
wa_dr3_trend = wa_desi_dr2 + delta_wa_per_release    # -0.41

pr(f"\n  Observed DR1 -> DR2 shifts:")
pr(f"    delta(w_0) = {delta_w0_per_release:.3f} per release")
pr(f"    delta(w_a) = {delta_wa_per_release:+.3f} per release")
pr(f"  Extrapolated DR3 center (if trend continues):")
pr(f"    w_0 = {w0_dr3_trend:.3f}, w_a = {wa_dr3_trend:.3f}")

# Compute tension for a range of DR3 center shifts
w0_shifts = np.linspace(-0.10, 0.10, 41)  # shift from DR2 w_0
wa_shifts = np.linspace(-0.3, 0.5, 41)    # shift from DR2 w_a

# Compute P(|w_FW - w_DR3| < 2*sigma_DR3) for each shifted DR3 center
pr(f"\n  P(framework within 2-sigma of DR3) as function of DR3 center shift:")
pr(f"  {'delta_w0':>10s}  {'w0_DR3':>8s}  {'w_0 1D tension':>15s}  {'P(<2sig, 1D)':>12s}")
pr(f"  {'-'*10}  {'-'*8}  {'-'*15}  {'-'*12}")

results_shift = []
for dw0 in [-0.05, -0.025, 0.0, 0.025, 0.05, 0.075, 0.10]:
    w0_dr3_shifted = w0_desi_dr2 + dw0
    tension_1d = abs(w0_fw - w0_dr3_shifted) / sigma_w0_dr3
    p_within_2sig = 2.0 * stats.norm.cdf(-tension_1d + 2.0) if tension_1d > 2.0 else \
                    2.0 * stats.norm.cdf(2.0) - 1.0  # ~0.9545 if tension < 2
    # More precisely: P(|w_FW - w_DR3_measured| < 2*sigma) where w_DR3_measured ~ N(w0_dr3_shifted, sigma^2)
    # = P(w0_dr3_shifted - 2*sigma < w_DR3_measured < w0_dr3_shifted + 2*sigma)
    # = Phi((w_FW - w0_shifted + 2*sigma)/sigma) - Phi((w_FW - w0_shifted - 2*sigma)/sigma)
    # where w_DR3_measured ~ N(w0_shifted, sigma^2)
    # The probability that the measured DR3 value falls within 2*sigma of w_FW:
    p_fw_in_2sig = stats.norm.cdf((w0_fw - w0_dr3_shifted + 2.0*sigma_w0_dr3) / sigma_w0_dr3) - \
                   stats.norm.cdf((w0_fw - w0_dr3_shifted - 2.0*sigma_w0_dr3) / sigma_w0_dr3)
    pr(f"  {dw0:+10.3f}  {w0_dr3_shifted:8.3f}  {tension_1d:15.2f}  {p_fw_in_2sig:12.4f}")
    results_shift.append((dw0, w0_dr3_shifted, tension_1d, p_fw_in_2sig))

results_shift = np.array(results_shift)

# =============================================================================
# 6. Full 2D Sensitivity Scan
# =============================================================================
pr(f"\n{'='*72}")
pr("2D Sensitivity: Framework Tension vs DR3 Center")
pr(f"{'='*72}")

# Scan DR3 center over a grid
n_scan = 51
w0_scan = np.linspace(-1.05, -0.65, n_scan)
wa_scan = np.linspace(-1.2, 0.2, n_scan)
W0_grid, WA_grid = np.meshgrid(w0_scan, wa_scan)

sig_fw_grid = np.zeros_like(W0_grid)
sig_lcdm_grid = np.zeros_like(W0_grid)

for i in range(n_scan):
    for j in range(n_scan):
        chi2_f = chi2_2d(w0_fw, wa_fw_scenB, W0_grid[i,j], WA_grid[i,j], cov_dr3)
        sig_fw_grid[i,j] = sigma_from_chi2(chi2_f, ndof=2)
        chi2_l = chi2_2d(w0_lcdm, wa_lcdm, W0_grid[i,j], WA_grid[i,j], cov_dr3)
        sig_lcdm_grid[i,j] = sigma_from_chi2(chi2_l, ndof=2)

# Find the DR3 center where FW has exactly 2-sigma tension
# (the boundary of the "viable" region)
from scipy.ndimage import label as ndlabel

viable_mask = sig_fw_grid < 2.0
n_viable = np.sum(viable_mask)
n_total = n_scan * n_scan
frac_viable = n_viable / n_total

pr(f"\n  2D scan: {n_scan}x{n_scan} grid over w_0 in [{w0_scan[0]:.2f}, {w0_scan[-1]:.2f}], "
   f"w_a in [{wa_scan[0]:.2f}, {wa_scan[-1]:.2f}]")
pr(f"  Framework viable (< 2-sigma): {n_viable}/{n_total} = {frac_viable*100:.1f}%")
pr(f"  Framework excluded (> 3-sigma): {np.sum(sig_fw_grid > 3.0)}/{n_total} = "
   f"{np.sum(sig_fw_grid > 3.0)/n_total*100:.1f}%")

# Compare: where does FW do better than LCDM?
fw_better = sig_fw_grid < sig_lcdm_grid
pr(f"  FW preferred over LCDM: {np.sum(fw_better)}/{n_total} = {np.sum(fw_better)/n_total*100:.1f}%")

# =============================================================================
# 7. w_a Discrimination: Framework vs DESI
# =============================================================================
pr(f"\n{'='*72}")
pr("w_a Discrimination Forecast")
pr(f"{'='*72}")

# Framework w_a predictions:
# Canonical: w_a = 0.0 (structural protection)
# Scenario B: w_a = 0.066 (task specification)
# DESI DR2: w_a = -0.73 +/- 0.25
# Scenario B center: w_a = -0.30

# 1D tension in w_a between framework and Scenario B center
delta_wa_fw_canon_to_scenB = abs(wa_fw_canonical - wa_scenB)
delta_wa_fw_scenB_to_scenB = abs(wa_fw_scenB - wa_scenB)
delta_wa_fw_to_dr2 = abs(wa_fw_scenB - wa_desi_dr2)

tension_wa_fw_canon_scenB = delta_wa_fw_canon_to_scenB / sigma_wa_dr3
tension_wa_fw_scenB_scenB = delta_wa_fw_scenB_to_scenB / sigma_wa_dr3
tension_wa_fw_dr2 = delta_wa_fw_to_dr2 / wa_desi_dr2_err

pr(f"\n  w_a discrimination (1D):")
pr(f"    FW (w_a=0) vs Scenario B center (w_a=-0.30): "
   f"|0 - (-0.30)| / {sigma_wa_dr3:.4f} = {tension_wa_fw_canon_scenB:.2f}-sigma")
pr(f"    FW (w_a=0.066) vs Scenario B center (w_a=-0.30): "
   f"|0.066 - (-0.30)| / {sigma_wa_dr3:.4f} = {tension_wa_fw_scenB_scenB:.2f}-sigma")
pr(f"    FW (w_a=0.066) vs DR2 (w_a=-0.73): "
   f"|0.066 - (-0.73)| / {wa_desi_dr2_err:.3f} = {tension_wa_fw_dr2:.2f}-sigma (current)")

# Task step 5: w_a = 0.066 vs w_a ~ -1.0 (DESI DR2 -- note: DR2 actual is -0.73, not -1.0)
# Using actual DR2 value:
pr(f"\n  Cross-reference: DESI DR2 w_a = {wa_desi_dr2} (actual), not -1.0 (task text)")
pr(f"    Using actual DR2 value for tension calculation.")

# =============================================================================
# 8. Posterior Probability via Savage-Dickey Density Ratio
# =============================================================================
pr(f"\n{'='*72}")
pr("Posterior Probability P(framework | DR3 Scenario B)")
pr(f"{'='*72}")

# The Savage-Dickey density ratio: for a point hypothesis H_0: (w_0, w_a) = (w_0^FW, w_a^FW)
# vs composite alternative H_1: (w_0, w_a) free,
# the Bayes factor is B_01 = pi(w_0^FW, w_a^FW | D) / pi(w_0^FW, w_a^FW)
# where pi(...|D) is the posterior and pi(...) is the prior.
#
# Under a Gaussian posterior centered on DR3 center with covariance cov_dr3,
# and a flat prior over the prior range:

# Prior range (CPL prior volume)
w0_prior_range = 1.0    # w_0 in [-1.5, -0.5] (typical DESI prior)  # (local)
wa_prior_range = 4.0    # w_a in [-3.0, 1.0] (typical DESI prior)  # (local)
prior_density = 1.0 / (w0_prior_range * wa_prior_range)

# Posterior density at framework point under Scenario B
# p(w_FW | D) = (2*pi)^{-1} |cov_dr3|^{-1/2} exp(-chi^2/2)
det_cov_dr3 = np.linalg.det(cov_dr3)
posterior_fw_at_scenB = (1.0 / (2.0 * np.pi * np.sqrt(det_cov_dr3))) * \
                        np.exp(-chi2_fw_scenB / 2.0)
posterior_fw_canon_at_scenB = (1.0 / (2.0 * np.pi * np.sqrt(det_cov_dr3))) * \
                              np.exp(-chi2_fw_canon_scenB / 2.0)

# Savage-Dickey Bayes factor
BF_scenB = posterior_fw_at_scenB / prior_density
BF_canon_scenB = posterior_fw_canon_at_scenB / prior_density

# Convert to posterior probability with equal prior odds: P = BF / (1 + BF)
p_fw_scenB = BF_scenB / (1.0 + BF_scenB)
p_fw_canon_scenB = BF_canon_scenB / (1.0 + BF_canon_scenB)

# Also compute for LCDM
posterior_lcdm_at_scenB = (1.0 / (2.0 * np.pi * np.sqrt(det_cov_dr3))) * \
                           np.exp(-chi2_lcdm_scenB / 2.0)
BF_lcdm_scenB = posterior_lcdm_at_scenB / prior_density
p_lcdm_scenB = BF_lcdm_scenB / (1.0 + BF_lcdm_scenB)

pr(f"\n  Prior: flat over w_0 x w_a = [{w0_prior_range}] x [{wa_prior_range}]")
pr(f"  Prior density = {prior_density:.4f}")
pr(f"  |Sigma_DR3| = {det_cov_dr3:.6e}")
pr(f"\n  Savage-Dickey at Scenario B center (w_0={w0_scenB}, w_a={wa_scenB}):")
pr(f"    Framework (w_a={wa_fw_scenB}):")
pr(f"      chi^2 = {chi2_fw_scenB:.3f}")
pr(f"      posterior density = {posterior_fw_at_scenB:.6e}")
pr(f"      Bayes factor B_01 = {BF_scenB:.4f}")
pr(f"      P(FW | DR3, ScB) = {p_fw_scenB:.4f}")
pr(f"    Framework (w_a=0, canonical):")
pr(f"      chi^2 = {chi2_fw_canon_scenB:.3f}")
pr(f"      posterior density = {posterior_fw_canon_at_scenB:.6e}")
pr(f"      Bayes factor B_01 = {BF_canon_scenB:.4f}")
pr(f"      P(FW_canon | DR3, ScB) = {p_fw_canon_scenB:.4f}")
pr(f"    LCDM:")
pr(f"      chi^2 = {chi2_lcdm_scenB:.3f}")
pr(f"      posterior density = {posterior_lcdm_at_scenB:.6e}")
pr(f"      Bayes factor B_01 = {BF_lcdm_scenB:.4f}")
pr(f"      P(LCDM | DR3, ScB) = {p_lcdm_scenB:.4f}")

# =============================================================================
# 9. Comparison Across All Three Scenarios (from S68/S70)
# =============================================================================
pr(f"\n{'='*72}")
pr("Cross-Check: Framework Tension Across All Three Scenarios")
pr(f"{'='*72}")

# Scenario definitions from S68
scenario_w0_all = np.array([-0.75, -0.90, -0.65])
scenario_wa_all = np.array([-0.73, -0.30, -1.00])
scenario_labels = ['A (confirms DR2)', 'B (toward LCDM)', 'C (more dyn DE)']

pr(f"\n  {'Scenario':>25s}  {'w_0':>6s}  {'w_a':>6s}  {'FW sig':>8s}  {'FW_c sig':>8s}  "
   f"{'LCDM sig':>9s}  {'FW class':>12s}")
pr(f"  {'-'*25}  {'-'*6}  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*9}  {'-'*12}")

for i in range(3):
    w0_sc = scenario_w0_all[i]
    wa_sc = scenario_wa_all[i]
    chi2_f = chi2_2d(w0_fw, wa_fw_scenB, w0_sc, wa_sc, cov_dr3)
    sig_f = sigma_from_chi2(chi2_f, ndof=2)
    chi2_fc = chi2_2d(w0_fw, wa_fw_canonical, w0_sc, wa_sc, cov_dr3)
    sig_fc = sigma_from_chi2(chi2_fc, ndof=2)
    chi2_l = chi2_2d(w0_lcdm, wa_lcdm, w0_sc, wa_sc, cov_dr3)
    sig_l = sigma_from_chi2(chi2_l, ndof=2)
    cls = "EXCLUDED" if sig_f > 3.0 else ("TENSION" if sig_f > 2.0 else "VIABLE")
    pr(f"  {scenario_labels[i]:>25s}  {w0_sc:6.2f}  {wa_sc:6.2f}  {sig_f:8.2f}  "
       f"{sig_fc:8.2f}  {sig_l:9.2f}  {cls:>12s}")

# Compare with S70 stored values (5x DR1 volume, different from 2x DR2)
pr(f"\n  S70 values for reference (5x DR1 volume, different scaling):")
sig_fw_s70 = np.array(d70['sig_fw_scenarios'])
sig_lcdm_s70 = np.array(d70['sig_lcdm_scenarios'])
for i in range(3):
    pr(f"    Sc.{scenario_labels[i]}: FW {sig_fw_s70[i]:.2f}-sig (S70), LCDM {sig_lcdm_s70[i]:.2f}-sig (S70)")

# =============================================================================
# 10. Summary Table
# =============================================================================
pr(f"\n{'='*72}")
pr("SUMMARY: DESI-DR3-SCENARIO-B-PRECISE-71")
pr(f"{'='*72}")

pr(f"\n  DESI DR3 Fisher Forecast (2x DR2 volume):")
pr(f"    sigma(w_0)_DR3 = {sigma_w0_dr3:.4f}")
pr(f"    sigma(w_a)_DR3 = {sigma_wa_dr3:.4f}")
pr(f"    rho(w_0, w_a)  = {rho_desi}")
pr(f"\n  Scenario B Tension (DR3 center = (-0.90, -0.30)):")
pr(f"    FW (w_a=0.066):   {sig_fw_scenB:.2f}-sigma (2D)")
pr(f"    FW (w_a=0):       {sig_fw_canon_scenB:.2f}-sigma (2D)")
pr(f"    LCDM:             {sig_lcdm_scenB:.2f}-sigma (2D)")
pr(f"\n  1D w_0 tension (FW vs DR2 center):")
pr(f"    |(-0.918) - (-0.752)| / {sigma_w0_dr3:.3f} = {task_tension:.2f}-sigma")
pr(f"\n  w_a discrimination (1D, Scenario B center):")
pr(f"    FW (w_a=0) vs -0.30:     {tension_wa_fw_canon_scenB:.2f}-sigma")
pr(f"    FW (w_a=0.066) vs -0.30: {tension_wa_fw_scenB_scenB:.2f}-sigma")
pr(f"\n  Posterior probability P(model | DR3, Scenario B):")
pr(f"    P(FW, w_a=0.066)  = {p_fw_scenB:.4f}  (BF = {BF_scenB:.4f})")
pr(f"    P(FW, w_a=0)      = {p_fw_canon_scenB:.4f}  (BF = {BF_canon_scenB:.4f})")
pr(f"    P(LCDM)           = {p_lcdm_scenB:.4f}  (BF = {BF_lcdm_scenB:.4f})")

# Classification
if sig_fw_scenB > 3.0:
    gate_class = "Scenario B EXCLUDES framework (> 3-sigma)"
elif sig_fw_scenB > 2.0:
    gate_class = "Scenario B creates TENSION with framework (2-3 sigma)"
else:
    gate_class = "Scenario B is CONSISTENT with framework (< 2-sigma)"

pr(f"\n  Gate classification: {gate_class}")

# =============================================================================
# 11. Save Results
# =============================================================================
outpath = os.path.join(SCRIPT_DIR, "s71_desi_dr3_scenario_b.npz")
np.savez(outpath,
    # DR3 Fisher
    sigma_w0_dr3=sigma_w0_dr3,
    sigma_wa_dr3=sigma_wa_dr3,
    rho_dr3=rho_desi,
    V_ratio=V_ratio,
    cov_dr3=cov_dr3,
    F_dr3=F_dr3,
    # Framework
    w0_fw=w0_fw,
    wa_fw_canonical=wa_fw_canonical,
    wa_fw_scenB=wa_fw_scenB,
    # DR2
    w0_desi_dr2=w0_desi_dr2,
    wa_desi_dr2=wa_desi_dr2,
    w0_desi_dr2_err=w0_desi_dr2_err,
    wa_desi_dr2_err=wa_desi_dr2_err,
    # Scenario B
    w0_scenB=w0_scenB,
    wa_scenB=wa_scenB,
    chi2_fw_scenB=chi2_fw_scenB,
    sig_fw_scenB=sig_fw_scenB,
    chi2_fw_canon_scenB=chi2_fw_canon_scenB,
    sig_fw_canon_scenB=sig_fw_canon_scenB,
    chi2_lcdm_scenB=chi2_lcdm_scenB,
    sig_lcdm_scenB=sig_lcdm_scenB,
    # 1D tensions
    tension_w0_1d_dr2cen=task_tension,
    tension_w0_1d_scenB=tension_w0_1d,
    tension_wa_scenB_1d=tension_wa_fw_scenB_scenB,
    tension_wa_canon_1d=tension_wa_fw_canon_scenB,
    # Posterior probabilities
    BF_fw_scenB=BF_scenB,
    BF_fw_canon_scenB=BF_canon_scenB,
    BF_lcdm_scenB=BF_lcdm_scenB,
    p_fw_scenB=p_fw_scenB,
    p_fw_canon_scenB=p_fw_canon_scenB,
    p_lcdm_scenB=p_lcdm_scenB,
    # Shift sensitivity
    shift_results=results_shift,
    # All-scenario comparison
    scenario_w0=scenario_w0_all,
    scenario_wa=scenario_wa_all,
    # DR2-center with DR3 errors
    chi2_fw_dr2cen_dr3err=chi2_fw_dr2cen_dr3err,
    sig_fw_dr2cen_dr3err=sig_fw_dr2cen_dr3err,
    # 2D scan
    sig_fw_grid=sig_fw_grid,
    sig_lcdm_grid=sig_lcdm_grid,
    w0_scan=w0_scan,
    wa_scan=wa_scan,
    frac_viable=frac_viable,
    # Gate
    gate_name=np.array(['DESI-DR3-SCENARIO-B-PRECISE-71']),
    gate_verdict=np.array(['INFO']),
    gate_class=np.array([gate_class]),
)
pr(f"\n  Saved: {outpath}")
pr(f"  Keys: {35}")

# =============================================================================
# 12. Diagnostic Plot
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: w_0-w_a plane with contours
ax = axes[0]
ax.set_title('DESI DR3 Scenario B: w$_0$-w$_a$ Plane', fontsize=11)

# DR3 Scenario B ellipse (2-sigma)
eigvals, eigvecs = np.linalg.eigh(cov_dr3)
angle = np.degrees(np.arctan2(eigvecs[1,0], eigvecs[0,0]))
for nsig, alpha_val in [(1, 0.3), (2, 0.15), (3, 0.07)]:
    ell = Ellipse(xy=(w0_scenB, wa_scenB),
                  width=2*nsig*np.sqrt(eigvals[0]),  # (local)
                  height=2*nsig*np.sqrt(eigvals[1]),
                  angle=angle, facecolor='steelblue', alpha=alpha_val,
                  edgecolor='steelblue', linewidth=1.5)
    ax.add_patch(ell)

# Plot model points
ax.plot(w0_fw, wa_fw_scenB, 'r*', markersize=14, label=f'FW (w$_a$={wa_fw_scenB})', zorder=5)
ax.plot(w0_fw, wa_fw_canonical, 'ro', markersize=10, label=f'FW (w$_a$=0, canon)', zorder=5)
ax.plot(w0_lcdm, wa_lcdm, 'ks', markersize=10, label='$\\Lambda$CDM', zorder=5)
ax.plot(w0_desi_dr2, wa_desi_dr2, 'g^', markersize=10, label='DESI DR2', zorder=5)
ax.plot(w0_scenB, wa_scenB, 'b+', markersize=14, markeredgewidth=2, label='Sc.B center', zorder=5)

ax.set_xlabel('w$_0$', fontsize=12)
ax.set_ylabel('w$_a$', fontsize=12)
ax.set_xlim(-1.15, -0.55)
ax.set_ylim(-1.5, 0.5)
ax.axhline(0, color='gray', ls='--', alpha=0.5)
ax.axvline(-1, color='gray', ls='--', alpha=0.5)
ax.legend(fontsize=8, loc='upper left')

# Annotate tensions
ax.annotate(f'FW: {sig_fw_scenB:.1f}$\\sigma$',
            xy=(w0_fw, wa_fw_scenB), xytext=(w0_fw+0.05, wa_fw_scenB+0.15),
            fontsize=9, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=0.8))
ax.annotate(f'$\\Lambda$CDM: {sig_lcdm_scenB:.1f}$\\sigma$',
            xy=(w0_lcdm, wa_lcdm), xytext=(w0_lcdm+0.05, wa_lcdm+0.15),
            fontsize=9, color='black',
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8))

# Right panel: 2D tension heatmap
ax2 = axes[1]
ax2.set_title('FW Tension vs DR3 Center (2D $\\sigma$)', fontsize=11)
im = ax2.contourf(W0_grid, WA_grid, sig_fw_grid,
                   levels=[0, 1, 2, 3, 5, 8, 12],
                   cmap='RdYlGn_r')
ax2.contour(W0_grid, WA_grid, sig_fw_grid,
            levels=[2, 3, 5], colors='k', linewidths=[1, 1.5, 0.5])
plt.colorbar(im, ax=ax2, label='FW tension ($\\sigma$)')

# Mark scenario centers
for i, (w0c, wac, lbl) in enumerate(zip(scenario_w0_all, scenario_wa_all, ['A','B','C'])):
    ax2.plot(w0c, wac, 'w+', markersize=12, markeredgewidth=2)
    ax2.annotate(lbl, xy=(w0c, wac), xytext=(w0c+0.02, wac+0.05),
                 fontsize=10, color='white', fontweight='bold')
ax2.plot(w0_fw, wa_fw_scenB, 'r*', markersize=14, zorder=5)
ax2.plot(w0_lcdm, wa_lcdm, 'ks', markersize=10, zorder=5)

ax2.set_xlabel('DR3 center w$_0$', fontsize=12)
ax2.set_ylabel('DR3 center w$_a$', fontsize=12)

plt.tight_layout()
pngpath = os.path.join(SCRIPT_DIR, "s71_desi_dr3_scenario_b.png")
plt.savefig(pngpath, dpi=150, bbox_inches='tight')
pr(f"  Plot: {pngpath}")

pr("\nDone.")
log.close()
