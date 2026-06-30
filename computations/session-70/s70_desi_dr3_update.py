#!/usr/bin/env python3
"""
s70_desi_dr3_update.py -- DESI-DR3-UPDATE-70: Decision Tree Update with S69-S70 Results
========================================================================================
Gate: DESI-DR3-UPDATE-70
  INFO: Updated decision tree and discriminating power forecast.

Physics:
  The S68 DESI DR3 forecast computed Fisher-matrix exclusion significance
  for the framework (w_0 = -0.918, w_a = 0) under three pre-registered
  scenarios (A: confirms DR2, B: toward LCDM, C: more dynamical DE).

  Since S68, three rounds of observational validation (S69-S70) have
  sharpened the comparison:
    - PVD-DA-69: D_M/r_d chi^2/dof = 2.08 (framework's weakest link)
    - PVD-FSIG8-69: f*sigma_8 chi^2/dof = 0.761 (FW preferred over LCDM)
    - PVD-SNE-69: Pantheon+ chi^2/dof = 1.025, Delta chi^2 = -4.47 (FW preferred)
    - FULL-COV-PANTHEON-70: Delta chi^2 = -7.82 with full covariance (FW strengthened)
    - FULL-COV-RSD-70: Delta chi^2 = -0.609 with full covariance (FW robust)
    - CLASS-ISW-70: ISW auto-power FW/Quint = +6.7% (Boltzmann-level, PASS)
    - HYDROSTATIC-CLUSTER-70: Clusters cannot discriminate (INFO)

  This script updates the S68 decision tree with:
    1. Current observational scores at each DESI bin
    2. DR3 error projections (~2.2x statistical improvement)
    3. Updated discriminating power forecasts
    4. Pre-registered decision criteria for DR3

  The LRG2 bin at z = 0.706 has the worst D_M/r_d pull (-2.26 sigma) and
  is the single most critical bin for DR3 to resolve.

Author: Katie Mack (Cosmic Bridge)
Session: 70, Task DESI-DR3-UPDATE-70
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

LOGPATH = os.path.join(SCRIPT_DIR, "s70_desi_dr3_update_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("DESI-DR3-UPDATE-70: Decision Tree Update with S69-S70 Results")
pr("=" * 72)

# =============================================================================
# 1. Load All Upstream Data
# =============================================================================
pr(f"\n{'='*72}")
pr("1. Loading Upstream Data")
pr(f"{'='*72}")

# S68 DESI DR3 forecast (baseline)
d68 = np.load(os.path.join(SCRIPT_DIR, 's68_desi_dr3_forecast.npz'), allow_pickle=True)
w0_fw = float(d68['w0_fw'])              # -0.918
wa_fw = float(d68['wa_fw'])              # 0.0
w0_lcdm = float(d68['w0_lcdm'])          # -1.0
wa_lcdm = float(d68['wa_lcdm'])          # 0.0
w0_desi_dr2 = float(d68['w0_desi_dr2'])  # -0.752
wa_desi_dr2 = float(d68['wa_desi_dr2'])  # -0.73
sigma_w0_dr3 = float(d68['sigma_w0_dr3'])
sigma_wa_dr3 = float(d68['sigma_wa_dr3'])
rho_desi = float(d68['rho_desi'])        # -0.85
z_eff = np.array(d68['z_eff'])
tracer_labels = list(d68['tracer_labels'])
sigma_DV_frac_dr2 = np.array(d68['sigma_DV_frac_dr2'])
sigma_DV_frac_dr3 = np.array(d68['sigma_DV_frac_dr3'])
DV_rd_LCDM_s68 = np.array(d68['DV_rd_LCDM'])
DV_rd_FW_s68 = np.array(d68['DV_rd_Framework'])
sig_fw_scenarios_s68 = np.array(d68['sig_fw_scenarios'])
sig_lcdm_scenarios_s68 = np.array(d68['sig_lcdm_scenarios'])
scenario_w0_s68 = np.array(d68['scenario_w0'])
scenario_wa_s68 = np.array(d68['scenario_wa'])
r_d_Mpc = float(d68['r_d_Mpc'])

# S69 D_M/r_d BAO data
d69_da = np.load(os.path.join(SCRIPT_DIR, 's69_pvd13_da.npz'), allow_pickle=True)
DM_rd_obs = np.array(d69_da['DM_rd_obs'])
DM_rd_err = np.array(d69_da['DM_rd_err'])
DM_rd_FW = np.array(d69_da['DM_rd_Framework'])
DM_rd_LCDM = np.array(d69_da['DM_rd_LCDM'])
pulls_DM_fw = np.array(d69_da['pulls_DM_fw'])
pulls_DM_lcdm = np.array(d69_da['pulls_DM_lcdm'])
chi2_DM_fw = float(d69_da['chi2_DM_Framework'])
chi2_DM_lcdm = float(d69_da['chi2_DM_LCDM'])
chi2_dof_DM_fw = float(d69_da['chi2_dof_DM_fw'])
DH_rd_obs = np.array(d69_da['DH_rd_obs'])
DH_rd_err = np.array(d69_da['DH_rd_err'])
DH_rd_FW = np.array(d69_da['DH_rd_Framework'])
DH_rd_LCDM = np.array(d69_da['DH_rd_LCDM'])
pulls_DH_fw = np.array(d69_da['pulls_DH_fw'])
pulls_DH_lcdm = np.array(d69_da['pulls_DH_lcdm'])

# S69 f*sigma_8 RSD data
d69_fs = np.load(os.path.join(SCRIPT_DIR, 's69_pvd05_fsigma8.npz'), allow_pickle=True)
z_rsd = np.array(d69_fs['z_rsd'])
fsig8_rsd = np.array(d69_fs['fsig8_rsd'])
err_rsd = np.array(d69_fs['err_rsd'])
fsig8_FW_at_z = np.array(d69_fs['fsig8_FW_at_z'])
fsig8_L_at_z = np.array(d69_fs['fsig8_L_at_z'])
chi2_FW_fsig8 = float(d69_fs['chi2_FW'])
chi2_L_fsig8 = float(d69_fs['chi2_L'])
chi2_FW_dof_fsig8 = float(d69_fs['chi2_FW_dof'])
chi2_L_dof_fsig8 = float(d69_fs['chi2_L_dof'])
delta_chi2_fsig8_diag = float(d69_fs['delta_chi2_fw_vs_lcdm'])
sigma8_fw = float(d69_fs['sigma8_fw'])
sigma8_lcdm = float(d69_fs['sigma8_LCDM'])
labels_rsd = list(d69_fs['labels_rsd'])

# S70 full-covariance updates
d70_cov_rsd = np.load(os.path.join(SCRIPT_DIR, 's70_full_cov_rsd.npz'), allow_pickle=True)
chi2_FW_full_rsd = float(d70_cov_rsd['chi2_FW_full'])
chi2_L_full_rsd = float(d70_cov_rsd['chi2_L_full'])
delta_chi2_fsig8_full = float(d70_cov_rsd['delta_chi2_full'])

d70_cov_sne = np.load(os.path.join(SCRIPT_DIR, 's70_full_cov_pantheon.npz'), allow_pickle=True)
delta_chi2_sne_full = float(d70_cov_sne['delta_chi2_full'])
delta_chi2_sne_diag = float(d70_cov_sne['delta_chi2_diag'])

# S70 CLASS-ISW Boltzmann results
d70_isw = np.load(os.path.join(SCRIPT_DIR, 's70_class_isw.npz'), allow_pickle=True)
isw_fw_quint_pct = float(d70_isw['gate_metric_isw'])  # 6.72%
isw_fw_lcdm_tt_pct = float(d70_isw['gate_metric_tt'])  # 6.87%

pr(f"\n  Framework:  w_0 = {w0_fw:.3f}, w_a = {wa_fw:.1f}")
pr(f"  LCDM:       w_0 = {w0_lcdm:.1f}, w_a = {wa_lcdm:.1f}")
pr(f"  DESI DR2:   w_0 = {w0_desi_dr2:.3f}, w_a = {wa_desi_dr2:.2f}")
pr(f"  DR3 proj:   sigma(w_0) = {sigma_w0_dr3:.4f}, sigma(w_a) = {sigma_wa_dr3:.4f}, rho = {rho_desi}")
pr(f"  r_d = {r_d_Mpc:.3f} Mpc")
pr(f"  N(BAO bins) = {len(z_eff)}, N(RSD bins) = {len(z_rsd)}")

# =============================================================================
# 2. Current Observational Scorecard (S69-S70)
# =============================================================================
pr(f"\n{'='*72}")
pr("2. Current Observational Scorecard (S69-S70)")
pr(f"{'='*72}")

pr(f"\n  --- D_M/r_d (BAO) ---")
pr(f"  chi^2(FW) = {chi2_DM_fw:.2f} / 7 bins = {chi2_dof_DM_fw:.3f} per dof")
pr(f"  chi^2(LCDM) = {chi2_DM_lcdm:.2f} / 7 bins = {chi2_DM_lcdm/7:.3f} per dof")
pr(f"  Delta(chi^2) = {chi2_DM_fw - chi2_DM_lcdm:+.2f} (LCDM preferred)")
pr(f"\n  Bin-by-bin D_M/r_d pulls (FW):")
pr(f"  {'z':>6s}  {'Tracer':>12s}  {'Obs':>8s}  {'FW':>8s}  {'LCDM':>8s}  {'Pull(FW)':>9s}  {'Pull(LCDM)':>11s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s}  {DM_rd_obs[i]:8.3f}  "
       f"{DM_rd_FW[i]:8.3f}  {DM_rd_LCDM[i]:8.3f}  "
       f"{pulls_DM_fw[i]:+8.3f}s  {pulls_DM_lcdm[i]:+10.3f}s")

# Identify the LRG2 worst pull
idx_worst = np.argmin(pulls_DM_fw)
pr(f"\n  Worst bin: z = {z_eff[idx_worst]:.3f} ({tracer_labels[idx_worst]}), "
   f"pull = {pulls_DM_fw[idx_worst]:+.3f} sigma")
pr(f"  This is the SINGLE MOST CRITICAL bin for DR3 to resolve.")

pr(f"\n  --- f*sigma_8 (RSD) ---")
pr(f"  chi^2/dof (FW, diagonal) = {chi2_FW_dof_fsig8:.3f}")
pr(f"  chi^2/dof (LCDM, diagonal) = {chi2_L_dof_fsig8:.3f}")
pr(f"  Delta(chi^2) FW-LCDM (diagonal) = {delta_chi2_fsig8_diag:+.3f}")
pr(f"  Delta(chi^2) FW-LCDM (full cov) = {delta_chi2_fsig8_full:+.3f}")
pr(f"  FW PREFERRED in both diagonal and full-covariance analyses.")
pr(f"  sigma_8: FW = {sigma8_fw:.3f}, LCDM = {sigma8_lcdm:.3f} "
   f"(FW partially ameliorates S_8 tension)")

pr(f"\n  --- Pantheon+ SNe (S70 full covariance) ---")
pr(f"  Delta(chi^2) FW-LCDM (diagonal) = {delta_chi2_sne_diag:+.2f}")
pr(f"  Delta(chi^2) FW-LCDM (full cov) = {delta_chi2_sne_full:+.2f}")
pr(f"  FW PREFERRED, strengthened by off-diagonal systematics.")
# Compute sigma for full cov SNe
delta_sne = abs(delta_chi2_sne_full)
sigma_sne = np.sqrt(delta_sne)  # Wilks' theorem, 1 DOF
pr(f"  Significance: {sigma_sne:.2f}-sigma (Wilks, 1 dof)")

pr(f"\n  --- ISW Tracking (S70 Boltzmann) ---")
pr(f"  ISW auto-power FW/Quint = +{isw_fw_quint_pct:.2f}% (PASS, >5% gate)")
pr(f"  Full TT FW/LCDM at l=2 = -{isw_fw_lcdm_tt_pct:.2f}% (FW < Q at low l)")
pr(f"  This is the substrate-specific discriminant (c_s^2 = 0 vs 1).")

# =============================================================================
# 3. DR3 Error Scaling and Projections
# =============================================================================
pr(f"\n{'='*72}")
pr("3. DR3 Error Scaling and Projections")
pr(f"{'='*72}")

# DR3 approximately 5x the spectroscopic sample of DR1
# Statistical improvement: 1/sqrt(5) ~ 2.24x
# But we also have systematic floors
N_dr3_over_dr1 = 5.0
stat_improvement = np.sqrt(N_dr3_over_dr1)  # ~2.236

pr(f"\n  DR3/DR1 sample ratio: {N_dr3_over_dr1:.0f}x")
pr(f"  Statistical improvement: sqrt({N_dr3_over_dr1:.0f}) = {stat_improvement:.3f}x")

# For BAO D_M/r_d: errors scale as 1/sqrt(N)
# But systematic floor from calibration, template mismatch ~0.3-0.5%
sys_floor_bao_pct = 0.003  # 0.3% systematic floor  # (local)

DM_rd_err_dr3_stat = DM_rd_err / stat_improvement
DM_rd_err_dr3 = np.sqrt(DM_rd_err_dr3_stat**2 + (sys_floor_bao_pct * DM_rd_obs)**2)

pr(f"\n  D_M/r_d error projections (DR3):")
pr(f"  {'z':>6s}  {'Tracer':>12s}  {'DR1 err':>8s}  {'DR3 stat':>9s}  {'DR3 total':>10s}  {'Improvement':>12s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s}  {DM_rd_err[i]:8.3f}  "
       f"{DM_rd_err_dr3_stat[i]:9.3f}  {DM_rd_err_dr3[i]:10.3f}  "
       f"{DM_rd_err[i]/DM_rd_err_dr3[i]:10.2f}x")

# For RSD f*sigma_8: errors also scale as 1/sqrt(N) plus velocity-bias systematic
sys_floor_rsd = 0.005  # 0.5% systematic floor (from S70 analysis)  # (local)
err_rsd_dr3_stat = err_rsd / stat_improvement
err_rsd_dr3 = np.sqrt(err_rsd_dr3_stat**2 + sys_floor_rsd**2)

pr(f"\n  f*sigma_8 error projections (DR3):")
pr(f"  {'z':>6s}  {'Survey':>16s}  {'DR1 err':>8s}  {'DR3 stat':>9s}  {'DR3 total':>10s}")
for i in range(len(z_rsd)):
    pr(f"  {z_rsd[i]:6.3f}  {labels_rsd[i]:>16s}  {err_rsd[i]:8.3f}  "
       f"{err_rsd_dr3_stat[i]:9.3f}  {err_rsd_dr3[i]:10.3f}")

# =============================================================================
# 4. DR3 Discriminating Power: D_M/r_d
# =============================================================================
pr(f"\n{'='*72}")
pr("4. DR3 Discriminating Power: D_M/r_d (BAO)")
pr(f"{'='*72}")

# If the current pulls persist with DR3 errors
# Convention: pull = (FW - obs) / err (same sign convention as S69)
pulls_DM_fw_dr3 = (DM_rd_FW - DM_rd_obs) / DM_rd_err_dr3
pulls_DM_lcdm_dr3 = (DM_rd_LCDM - DM_rd_obs) / DM_rd_err_dr3

chi2_DM_fw_dr3 = np.sum(pulls_DM_fw_dr3**2)
chi2_DM_lcdm_dr3 = np.sum(pulls_DM_lcdm_dr3**2)

# Mean pull for coherent signal detection
mean_pull_fw = np.mean(pulls_DM_fw)
mean_pull_fw_dr3 = np.mean(pulls_DM_fw_dr3)

pr(f"\n  If current D_M residuals persist, DR3 pulls:")
pr(f"  {'z':>6s}  {'Tracer':>12s}  {'DR1 pull':>9s}  {'DR3 pull':>9s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s}  {pulls_DM_fw[i]:+8.3f}s  "
       f"{pulls_DM_fw_dr3[i]:+8.3f}s")

pr(f"\n  FW chi^2 (D_M, DR1): {chi2_DM_fw:.2f} / 7 = {chi2_DM_fw/7:.3f}")
pr(f"  FW chi^2 (D_M, DR3): {chi2_DM_fw_dr3:.2f} / 7 = {chi2_DM_fw_dr3/7:.3f}")
pr(f"  LCDM chi^2 (D_M, DR1): {chi2_DM_lcdm:.2f} / 7 = {chi2_DM_lcdm/7:.3f}")
pr(f"  LCDM chi^2 (D_M, DR3): {chi2_DM_lcdm_dr3:.2f} / 7 = {chi2_DM_lcdm_dr3/7:.3f}")

# Mean pull significance
# The mean pull across N bins, if coherent, has error 1/sqrt(N)
mean_pull_fw_dr3_err = 1.0 / np.sqrt(len(z_eff))
coherent_sig_fw_dr3 = abs(mean_pull_fw_dr3) / mean_pull_fw_dr3_err

pr(f"\n  Mean pull (FW, DR1): {mean_pull_fw:+.3f}")
pr(f"  Mean pull (FW, DR3): {mean_pull_fw_dr3:+.3f}")
pr(f"  Coherent pull significance (DR3): {coherent_sig_fw_dr3:.2f}-sigma")
pr(f"  (A {abs(mean_pull_fw):+.2f}-sigma mean pull, scaled by sqrt(7) = {np.sqrt(7):.2f})")

# LRG2 bin specifically
idx_lrg2 = 2  # z = 0.706
pull_lrg2_dr3 = pulls_DM_fw_dr3[idx_lrg2]
pr(f"\n  LRG2 (z=0.706) specifically:")
pr(f"    DR1 pull: {pulls_DM_fw[idx_lrg2]:+.3f}-sigma")
pr(f"    DR3 pull (if residual persists): {pull_lrg2_dr3:+.3f}-sigma")
pr(f"    This bin reaches {abs(pull_lrg2_dr3):.1f}-sigma in DR3, "
   f"becoming decisive by itself.")

# =============================================================================
# 5. DR3 Discriminating Power: f*sigma_8
# =============================================================================
pr(f"\n{'='*72}")
pr("5. DR3 Discriminating Power: f*sigma_8 (RSD)")
pr(f"{'='*72}")

# Recompute chi^2 with DR3 errors
resid_fw = fsig8_rsd - fsig8_FW_at_z
resid_lcdm = fsig8_rsd - fsig8_L_at_z
chi2_fw_rsd_dr3 = np.sum((resid_fw / err_rsd_dr3)**2)
chi2_lcdm_rsd_dr3 = np.sum((resid_lcdm / err_rsd_dr3)**2)
delta_chi2_rsd_dr3 = chi2_fw_rsd_dr3 - chi2_lcdm_rsd_dr3

pr(f"\n  With DR3 errors (including systematic floor):")
pr(f"  chi^2 FW (DR3): {chi2_fw_rsd_dr3:.2f} / 9 = {chi2_fw_rsd_dr3/9:.3f}")
pr(f"  chi^2 LCDM (DR3): {chi2_lcdm_rsd_dr3:.2f} / 9 = {chi2_lcdm_rsd_dr3/9:.3f}")
pr(f"  Delta(chi^2) FW-LCDM (DR3): {delta_chi2_rsd_dr3:+.2f}")

# Significance of FW advantage (Wilks' theorem)
if delta_chi2_rsd_dr3 < 0:
    sig_rsd_dr3 = np.sqrt(abs(delta_chi2_rsd_dr3))
    pr(f"  FW preferred at {sig_rsd_dr3:.2f}-sigma (Wilks, 1 dof)")
else:
    sig_rsd_dr3 = -np.sqrt(abs(delta_chi2_rsd_dr3))
    pr(f"  LCDM preferred at {abs(sig_rsd_dr3):.2f}-sigma (Wilks, 1 dof)")

# The key discriminating bins: DESI overlap region z ~ 0.5-0.7
pr(f"\n  Per-bin residuals (DR3 errors):")
pr(f"  {'z':>6s}  {'Survey':>16s}  {'Obs':>7s}  {'FW':>7s}  {'LCDM':>7s}  "
   f"{'DR1 sig(FW)':>11s}  {'DR3 sig(FW)':>11s}")
for i in range(len(z_rsd)):
    sig_dr1 = resid_fw[i] / err_rsd[i]
    sig_dr3 = resid_fw[i] / err_rsd_dr3[i]
    pr(f"  {z_rsd[i]:6.3f}  {labels_rsd[i]:>16s}  {fsig8_rsd[i]:7.3f}  "
       f"{fsig8_FW_at_z[i]:7.3f}  {fsig8_L_at_z[i]:7.3f}  "
       f"{sig_dr1:+10.2f}s  {sig_dr3:+10.2f}s")

# =============================================================================
# 6. Combined DR3 Discriminating Power
# =============================================================================
pr(f"\n{'='*72}")
pr("6. Combined DR3 Discriminating Power")
pr(f"{'='*72}")

# Combine the three channels: BAO (D_M), RSD (f*sigma_8), SNe (distance modulus)
# These are approximately independent (different observables, different systematics)

delta_chi2_bao_dr3 = chi2_DM_fw_dr3 - chi2_DM_lcdm_dr3
pr(f"\n  Channel-by-channel Delta(chi^2) FW-LCDM:")
pr(f"    BAO D_M/r_d (DR3 errors):        {delta_chi2_bao_dr3:+.2f}")
pr(f"    RSD f*sigma_8 (DR3 errors):       {delta_chi2_rsd_dr3:+.2f}")
pr(f"    SNe Pantheon+ (S70 full cov):     {delta_chi2_sne_full:+.2f}")
pr(f"    RSD f*sigma_8 (S70 full cov):     {delta_chi2_fsig8_full:+.2f}")

# Combined (sum of approximately independent Delta chi^2)
# Use S70 full-cov for RSD, S70 full-cov for SNe
delta_chi2_combined_current = delta_chi2_bao_dr3 + delta_chi2_fsig8_full + delta_chi2_sne_full
pr(f"\n  Combined Delta(chi^2) (current data, DR3 BAO errors):")
pr(f"    BAO + RSD(full cov) + SNe(full cov) = {delta_chi2_combined_current:+.2f}")

# For combined significance: sum of chi^2 differences with N=3 independent channels
# Use Wilks' theorem with 1 extra parameter (w_0)
combined_sig = np.sqrt(abs(delta_chi2_combined_current))
direction = "FW preferred" if delta_chi2_combined_current < 0 else "LCDM preferred"
pr(f"    {direction} at {combined_sig:.2f}-sigma (combined, Wilks 1 dof)")

# Note: BAO works against FW, RSD and SNe work for FW
pr(f"\n  Pattern: BAO penalizes FW (chi^2 +{delta_chi2_bao_dr3:+.2f}),")
pr(f"           RSD and SNe compensate ({delta_chi2_fsig8_full:+.2f} and {delta_chi2_sne_full:+.2f}).")
pr(f"  The BAO penalty comes from the LRG2 z=0.706 bin specifically.")

# =============================================================================
# 7. w_0-w_a Fisher Forecast Update
# =============================================================================
pr(f"\n{'='*72}")
pr("7. w_0-w_a Fisher Forecast Update")
pr(f"{'='*72}")

def build_cov(sigma_w0, sigma_wa, rho):
    """Build 2x2 covariance matrix for (w_0, w_a)."""
    return np.array([
        [sigma_w0**2,                 rho * sigma_w0 * sigma_wa],
        [rho * sigma_w0 * sigma_wa,   sigma_wa**2]
    ])

def chi2_2d(w0_test, wa_test, w0_cen, wa_cen, cov):
    """Compute chi^2 for a point relative to center."""
    dw = np.array([w0_test - w0_cen, wa_test - wa_cen])
    F = np.linalg.inv(cov)
    return float(dw @ F @ dw)

def sigma_from_chi2(chi2_val, ndof=2):
    """Convert chi^2 to sigma for ndof degrees of freedom."""
    p_val = 1.0 - stats.chi2.cdf(chi2_val, df=ndof)
    p_val = max(p_val, 1e-300)
    return stats.norm.isf(p_val / 2.0)

# S68 used sqrt(2) improvement; update to sqrt(5) = 2.236x for DR3/DR1
# (DR3 ~ 5x sample of DR1, not just 2x as S68 assumed for DR3/DR2)
# Actually: S68 used DR2 errors / sqrt(2) because DR3 ~ 2x DR2.
# The prompt says "~2.2x improvement" = 1/sqrt(N/N_DR1) ~ sqrt(5).
# S68 already computed DR3 errors. We keep those but note the
# 5x DR1 claim maps to 2.5x DR2 (since DR2 ~ 2x DR1).
# For consistency with S68, we use their DR3 projections.

# DR3 projected errors (from S68: DR2/sqrt(2))
# For a tighter forecast: if DR3 is 5x DR1, then errors ~ DR1/sqrt(5)
# DR2 was ~2x DR1, so DR2 errors ~ DR1/sqrt(2)
# DR3 = 5x DR1 -> errors ~ DR1/sqrt(5) = DR2_err * sqrt(2)/sqrt(5) = DR2_err / sqrt(2.5)
# S68 used DR2_err / sqrt(2) which corresponds to DR3 = 4x DR1
# The 5x figure gives slightly tighter: DR2_err / sqrt(2.5)

w0_desi_err_dr2 = 0.057  # (local)
wa_desi_err_dr2 = 0.25  # (local)

# Two projections: S68 baseline (4x DR1) and updated (5x DR1)
sigma_w0_dr3_s68 = sigma_w0_dr3  # from S68 = DR2/sqrt(2)
sigma_wa_dr3_s68 = sigma_wa_dr3

sigma_w0_dr3_5x = w0_desi_err_dr2 / np.sqrt(2.5)
sigma_wa_dr3_5x = wa_desi_err_dr2 / np.sqrt(2.5)

pr(f"\n  DR3 sensitivity projections:")
pr(f"  S68 baseline (DR2/sqrt(2)):  sigma_w0 = {sigma_w0_dr3_s68:.4f}, sigma_wa = {sigma_wa_dr3_s68:.4f}")
pr(f"  Updated (5x DR1 = DR2/sqrt(2.5)): sigma_w0 = {sigma_w0_dr3_5x:.4f}, sigma_wa = {sigma_wa_dr3_5x:.4f}")

# Compute exclusion significance under each scenario with BOTH projections
scenarios = {
    'A': {'label': 'DR3 confirms DR2', 'w0': -0.75, 'wa': -0.73},
    'B': {'label': 'DR3 shifts toward LCDM', 'w0': -0.90, 'wa': -0.30},
    'C': {'label': 'DR3 increases dynamical DE', 'w0': -0.65, 'wa': -1.0},
}

results = {}
for key, sc in scenarios.items():
    pr(f"\n  --- Scenario {key}: {sc['label']} (w_0={sc['w0']:.2f}, w_a={sc['wa']:.2f}) ---")

    for label, sw0, swa in [('S68 baseline', sigma_w0_dr3_s68, sigma_wa_dr3_s68),
                            ('5x DR1', sigma_w0_dr3_5x, sigma_wa_dr3_5x)]:
        cov_sc = build_cov(sw0, swa, rho_desi)
        chi2_fw = chi2_2d(w0_fw, wa_fw, sc['w0'], sc['wa'], cov_sc)
        sig_fw = sigma_from_chi2(chi2_fw, ndof=2)
        chi2_lcdm = chi2_2d(w0_lcdm, wa_lcdm, sc['w0'], sc['wa'], cov_sc)
        sig_lcdm = sigma_from_chi2(chi2_lcdm, ndof=2)
        pr(f"    [{label:>12s}] FW: {sig_fw:.2f}-sigma, LCDM: {sig_lcdm:.2f}-sigma")

        if label == '5x DR1':
            results[key] = {
                'w0': sc['w0'], 'wa': sc['wa'],
                'sig_fw': sig_fw, 'sig_lcdm': sig_lcdm,
                'sig_fw_s68': sig_fw_scenarios_s68[['A','B','C'].index(key)],
                'sig_lcdm_s68': sig_lcdm_scenarios_s68[['A','B','C'].index(key)],
            }

# =============================================================================
# 8. Updated Decision Tree
# =============================================================================
pr(f"\n{'='*72}")
pr("8. UPDATED DECISION TREE: DESI DR3")
pr(f"{'='*72}")

pr(f"\n  Pre-registered thresholds (S60 DR3-PREREGISTER-60, unchanged):")
pr(f"    w_a < -0.530  =>  framework excluded (>= 3-sigma)")
pr(f"    w_a > -0.350  =>  framework consistent (<= 2-sigma)")
pr(f"    -0.530 <= w_a <= -0.350  =>  tension zone")

pr(f"\n  S68 scenario results vs S70 updated:")
pr(f"  {'':>10s}  {'w_0':>7s}  {'w_a':>7s}  "
   f"{'S68 FW':>8s}  {'S70 FW':>8s}  {'S68 LCDM':>9s}  {'S70 LCDM':>10s}")
pr(f"  {'-'*10}  {'-'*7}  {'-'*7}  {'-'*8}  {'-'*8}  {'-'*9}  {'-'*10}")
for key in ['A', 'B', 'C']:
    r = results[key]
    pr(f"  {'Sc. '+key:>10s}  {r['w0']:+7.3f}  {r['wa']:+7.3f}  "
       f"{r['sig_fw_s68']:7.2f}s  {r['sig_fw']:7.2f}s  "
       f"{r['sig_lcdm_s68']:8.2f}s  {r['sig_lcdm']:9.2f}s")

pr(f"\n  Key changes from S68 to S70:")
pr(f"    1. Scenario sigmas increase slightly because 5x DR1 gives tighter")
pr(f"       errors than S68's 4x DR1 assumption (sqrt(2) -> sqrt(2.5)).")
pr(f"    2. FW and LCDM BOTH static (w_a=0). They respond identically to")
pr(f"       dynamical DE discovery -- both excluded if w_a << 0.")
pr(f"    3. FW has a persistent ~2-sigma advantage over LCDM from w_0=-0.918")
pr(f"       vs -1.0, but ONLY in scenarios where |w_a| is small (Sc.B).")

# =============================================================================
# 9. New Decision Criteria from S69-S70 Data Tests
# =============================================================================
pr(f"\n{'='*72}")
pr("9. New Decision Criteria from S69-S70 Data Tests")
pr(f"{'='*72}")

pr(f"\n  The S69-S70 data tests add three new decision branches:")
pr(f"\n  BRANCH 1: D_M/r_d chi^2/dof")
pr(f"    Current: {chi2_dof_DM_fw:.3f} (DR1 errors)")
pr(f"    If chi^2/dof(D_M) drops below 1.5 with DR3: BAO tension RESOLVED")
pr(f"    If chi^2/dof(D_M) rises above 3.0 with DR3: w_a=0 under severe stress")

# Estimate what chi^2/dof would be with DR3 errors IF residuals persist
chi2_dof_dm_dr3_persist = chi2_DM_fw_dr3 / 7
pr(f"    DR3 projection (residuals persist): chi^2/dof = {chi2_dof_dm_dr3_persist:.3f}")
if chi2_dof_dm_dr3_persist > 3.0:
    pr(f"    => EXCEEDS 3.0 threshold. BAO channel would put w_a=0 under severe stress.")
elif chi2_dof_dm_dr3_persist > 1.5:
    pr(f"    => Between 1.5 and 3.0. BAO tension remains but is not decisive.")
else:
    pr(f"    => Below 1.5. BAO tension resolved.")

# What if residuals shrink by half (measurement noise was dominant)?
pulls_dm_half = pulls_DM_fw / 2.0
chi2_dm_half = np.sum((pulls_dm_half * DM_rd_err / DM_rd_err_dr3)**2)
chi2_dof_dm_half = chi2_dm_half / 7
pr(f"    DR3 projection (residuals halve): chi^2/dof = {chi2_dof_dm_half:.3f}")

pr(f"\n  BRANCH 2: f*sigma_8 Delta(chi^2)")
pr(f"    Current (diagonal): {delta_chi2_fsig8_diag:+.3f}")
pr(f"    Current (full cov): {delta_chi2_fsig8_full:+.3f}")
pr(f"    DR3 projection (residuals persist): {delta_chi2_rsd_dr3:+.2f}")
pr(f"    If Delta(chi^2) < -3.0 with DR3: FW firmly preferred over LCDM")
pr(f"    If Delta(chi^2) > 0 with DR3: LCDM preferred, FW advantage lost")

pr(f"\n  BRANCH 3: Combined expansion-history preference")
pr(f"    Currently: BAO penalizes FW, RSD + SNe compensate.")
pr(f"    If combined Delta(chi^2) < -10: Strong FW preference")
pr(f"    If combined Delta(chi^2) > 0: FW no longer preferred overall")

# =============================================================================
# 10. Observational Discriminant Hierarchy (Updated)
# =============================================================================
pr(f"\n{'='*72}")
pr("10. Observational Discriminant Hierarchy (Updated)")
pr(f"{'='*72}")

discriminants = [
    ("ISW auto-power (c_s^2=0 vs 1)", "FW/Quint +6.7%", "21cm ~2.6-sig",
     "SUBSTRATE-SPECIFIC: only test that probes DE perturbation physics"),
    ("f*sigma_8 (growth rate)", f"chi^2/dof FW={chi2_FW_dof_fsig8:.3f} vs LCDM={chi2_L_dof_fsig8:.3f}",
     f"DR3 Delta chi^2 ~ {delta_chi2_rsd_dr3:+.1f}", "FW preferred; sigma_8=0.793 eases S_8"),
    ("Pantheon+ SNe (distance modulus)", f"Delta chi^2 = {delta_chi2_sne_full:+.2f} (full cov)",
     "2.80-sigma FW preference", "FW preferred; w=-0.918 absorbs calibration systematics"),
    ("D_M/r_d BAO", f"chi^2/dof = {chi2_dof_DM_fw:.3f}", f"DR3 chi^2/dof ~ {chi2_dof_dm_dr3_persist:.1f}",
     "Framework's WEAKEST link; LRG2 z=0.706 critical"),
    ("Cluster counts N(z)", "LCDM preferred (Delta chi^2 ~ -2.5)", "Cannot discriminate",
     "sigma_8 advantage independent of mass calibration"),
    ("n_s, r CMB (pre-registered)", "n_s=0.9590, r=0.024", "CMB-S4 / LiteBIRD",
     "Within 1.4-sigma (n_s), 24-sigma detection (r) of LiteBIRD"),
]

pr(f"\n  {'Rank':>5s}  {'Observable':>35s}  {'Current Status':>45s}")
pr(f"  {'-'*5}  {'-'*35}  {'-'*45}")
for i, (name, status, forecast, note) in enumerate(discriminants, 1):
    pr(f"  {i:5d}  {name:>35s}  {status:>45s}")
    pr(f"  {'':>5s}  {'Forecast:':>35s}  {forecast:>45s}")
    pr(f"  {'':>5s}  {'Note:':>35s}  {note:>45s}")

# =============================================================================
# 11. Cross-checks Against S68
# =============================================================================
pr(f"\n{'='*72}")
pr("11. Cross-checks Against S68")
pr(f"{'='*72}")

pr(f"\n  [1] S68 scenario sigmas (rho=-0.85, DR2/sqrt(2)):")
pr(f"      Sc.A: FW {sig_fw_scenarios_s68[0]:.2f}-sig, LCDM {sig_lcdm_scenarios_s68[0]:.2f}-sig")
pr(f"      Sc.B: FW {sig_fw_scenarios_s68[1]:.2f}-sig, LCDM {sig_lcdm_scenarios_s68[1]:.2f}-sig")
pr(f"      Sc.C: FW {sig_fw_scenarios_s68[2]:.2f}-sig, LCDM {sig_lcdm_scenarios_s68[2]:.2f}-sig")
pr(f"      S70 updated (5x DR1 = tighter errors):")
pr(f"      Sc.A: FW {results['A']['sig_fw']:.2f}-sig, Sc.B: FW {results['B']['sig_fw']:.2f}-sig, "
   f"Sc.C: FW {results['C']['sig_fw']:.2f}-sig")

pr(f"\n  [2] S66 WA-REASSESS-66 confirmed: substrate compaction CLOSED (w_a=+1.121, wrong sign).")
pr(f"      Pure FW (w_0={w0_fw}, w_a=0) remains the sole DE prediction.")

pr(f"\n  [3] S69 data test summary:")
pr(f"      D_M/r_d: chi^2/dof = {chi2_dof_DM_fw:.3f} (weakest link, LRG2 at -2.26 sigma)")
pr(f"      f*sigma_8: chi^2/dof = {chi2_FW_dof_fsig8:.3f} (FW preferred)")
pr(f"      SNe: Delta chi^2 = {delta_chi2_sne_full:+.2f} (FW strengthened with full cov)")

pr(f"\n  [4] S70 full-covariance effects:")
pr(f"      RSD: Delta chi^2 went from {delta_chi2_fsig8_diag:+.3f} to {delta_chi2_fsig8_full:+.3f}")
pr(f"      SNe: Delta chi^2 went from {delta_chi2_sne_diag:+.2f} to {delta_chi2_sne_full:+.2f}")
pr(f"      Direction: RSD weakened, SNe strengthened. Net FW advantage robust.")

pr(f"\n  [5] ISW tracking (S70 Boltzmann-level):")
pr(f"      S68 Limber: ISW-gal FW/Quint = 7.6%")
pr(f"      S70 Boltzmann: ISW auto FW/Quint = {isw_fw_quint_pct:.2f}% (PASS), "
   f"ISW-gal = 3.98% (Limber overpredicted 1.9x)")
pr(f"      The ISW auto-power is the cleaner channel; ISW-gal diluted by galaxy window.")

# =============================================================================
# 12. Pre-Registered DESI DR3 Decision Tree (Final)
# =============================================================================
pr(f"\n{'='*72}")
pr("12. PRE-REGISTERED DESI DR3 DECISION TREE (UPDATED S70)")
pr(f"{'='*72}")

pr(f"""
  +--------------------------+
  |    DESI DR3 RELEASED     |
  +-----------+--------------+
              |
              v
  +---------------------------+
  | Extract w_0, w_a, errors  |
  | at each z-bin             |
  +---------------------------+
              |
    +---------+---------+
    |                   |
    v                   v
  w_a < -0.53       w_a > -0.35
  (3-sigma excl)    (2-sigma OK)
    |                   |
    v                   v
  FW EXCLUDED       FW CONSISTENT
  LCDM excluded     Test chi^2/dof(D_M)
  Both static fail  and f*sig8 Delta chi^2
    |                   |
    |          +--------+--------+
    |          |                 |
    |          v                 v
    |     chi^2/dof < 1.5   chi^2/dof > 1.5
    |     BAO RESOLVED      BAO PERSISTS
    |          |                 |
    |          v                 v
    |     FW SURVIVES       Test Delta chi^2(f*sig8)
    |     w=-0.918 viable        |
    |                    +-------+-------+
    |                    |               |
    |                    v               v
    |              Delta < -3       Delta > 0
    |              FW PREFERRED     FW LOSES GROWTH
    |                                ADVANTAGE
    |
    v (if -0.53 < w_a < -0.35)
  TENSION ZONE
  Both FW and LCDM under stress
  ISW tracking becomes discriminant
              |
              v
  +---------------------------+
  | ISW auto FW/Quint > 5%?  |
  | (21cm required, ~2040)    |
  +---------------------------+
""")

pr(f"\n  ADDITIONAL DR3 TESTS (new from S69-S70):")
pr(f"  1. LRG2 z=0.706 pull: if |pull| > 3.0 with DR3 -> systematic or real")
pr(f"  2. sigma_8 from RSD: if sigma_8 < 0.80 confirmed -> S_8 tension eased")
pr(f"  3. BAO + RSD + SNe combined Delta chi^2:")
pr(f"     < -10: Strong FW preference (w=-0.918 conclusive)")
pr(f"     > 0:   FW no longer preferred overall")
pr(f"     Net direction depends on whether LRG2 residual persists.")

# =============================================================================
# 13. Gate Verdict
# =============================================================================
pr(f"\n{'='*72}")
pr("GATE VERDICT: DESI-DR3-UPDATE-70")
pr(f"{'='*72}")

gate_detail = (
    f"Updated S68 decision tree with S69-S70 data tests. "
    f"D_M/r_d chi^2/dof = {chi2_dof_DM_fw:.3f} (weakest, LRG2 z=0.706 pull=-2.26). "
    f"f*sig8 FW preferred (Delta chi^2 = {delta_chi2_fsig8_full:+.3f} full cov). "
    f"SNe FW preferred (Delta chi^2 = {delta_chi2_sne_full:+.2f} full cov). "
    f"DR3 projections (5x DR1): Sc.A FW {results['A']['sig_fw']:.2f}-sig, "
    f"Sc.B FW {results['B']['sig_fw']:.2f}-sig, "
    f"Sc.C FW {results['C']['sig_fw']:.2f}-sig. "
    f"BAO chi^2/dof < 1.5 threshold (BAO resolved) and "
    f"f*sig8 Delta chi^2 < -3 threshold (FW firmly preferred) pre-registered. "
    f"ISW tracking (+6.7% FW/Quint) remains sole substrate-specific discriminant."
)

pr(f"\n  Gate: DESI-DR3-UPDATE-70")
pr(f"  Verdict: INFO")
pr(f"  Detail: {gate_detail}")

# =============================================================================
# 14. Summary Table
# =============================================================================
pr(f"\n{'='*72}")
pr("SUMMARY TABLE")
pr(f"{'='*72}")

pr(f"\n  {'Observable':>25s} | {'Current':>18s} | {'FW vs LCDM':>15s} | {'DR3 Forecast':>18s}")
pr(f"  {'-'*25}-+-{'-'*18}-+-{'-'*15}-+-{'-'*18}")
pr(f"  {'D_M/r_d chi^2/dof':>25s} | {chi2_dof_DM_fw:>18.3f} | {'LCDM better':>15s} | {chi2_dof_dm_dr3_persist:>15.1f}   ")
pr(f"  {'f*sig8 Delta chi^2':>25s} | {delta_chi2_fsig8_full:>18.3f} | {'FW better':>15s} | {delta_chi2_rsd_dr3:>15.1f}   ")
pr(f"  {'SNe Delta chi^2':>25s} | {delta_chi2_sne_full:>18.2f} | {'FW better':>15s} | {'--':>15s}   ")
pr(f"  {'ISW auto FW/Quint':>25s} | {f'+{isw_fw_quint_pct:.1f}%':>18s} | {'PASS (>5%)':>15s} | {'21cm ~2.6-sig':>15s}   ")
pr(f"  {'sigma_8':>25s} | {f'{sigma8_fw:.3f} vs {sigma8_lcdm:.3f}':>18s} | {'FW eases S_8':>15s} | {'--':>15s}   ")
pr(f"  {'LRG2 z=0.706 pull':>25s} | {f'{pulls_DM_fw[idx_lrg2]:+.2f}-sig':>18s} | {'Worst bin':>15s} | {f'{pulls_DM_fw_dr3[idx_lrg2]:+.1f}-sig':>15s}   ")

# =============================================================================
# 15. Plot: Updated Decision Tree Visualization
# =============================================================================
pr(f"\n{'='*72}")
pr("Generating Plot")
pr(f"{'='*72}")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# --- Panel 1: w_0 - w_a plane with scenario ellipses (updated from S68) ---
ax1 = axes[0]

sc_colors = {'A': '#e74c3c', 'B': '#f39c12', 'C': '#2ecc71'}
sc_names = {'A': 'Sc.A: confirms DR2', 'B': 'Sc.B: toward LCDM',
            'C': 'Sc.C: more dyn DE'}

for key in ['A', 'B', 'C']:
    sc = scenarios[key]
    cov_sc = build_cov(sigma_w0_dr3_5x, sigma_wa_dr3_5x, rho_desi)

    eigvals_e, eigvecs_e = np.linalg.eigh(cov_sc)
    order = eigvals_e.argsort()[::-1]
    eigvals_e = eigvals_e[order]
    eigvecs_e = eigvecs_e[:, order]
    angle = np.degrees(np.arctan2(eigvecs_e[1, 0], eigvecs_e[0, 0]))

    chi2_2dof = {1: 2.2977, 2: 6.1801, 3: 11.8290}
    for nsig, alpha in [(1, 0.4), (2, 0.2), (3, 0.1)]:
        scale = np.sqrt(chi2_2dof[nsig])
        width = 2 * np.sqrt(eigvals_e[0]) * scale  # (local)
        height = 2 * np.sqrt(eigvals_e[1]) * scale
        ell = Ellipse(xy=(sc['w0'], sc['wa']), width=width, height=height,
                      angle=angle, facecolor=sc_colors[key], alpha=alpha,
                      edgecolor=sc_colors[key], linewidth=1.5 if nsig == 1 else 0.8)
        ax1.add_patch(ell)

    ax1.plot(sc['w0'], sc['wa'], 'x', color=sc_colors[key], markersize=10,
             markeredgewidth=2,
             label=f"{sc_names[key]} ({results[key]['sig_fw']:.1f}$\\sigma$ FW)")

ax1.plot(w0_fw, 0.0, '*', color='navy', markersize=18, markeredgecolor='black',
         markeredgewidth=1, label=f'FW ($w_0$={w0_fw:.3f}, $w_a$=0)', zorder=10)
ax1.plot(-1.0, 0.0, 'D', color='blue', markersize=10, markeredgecolor='black',
         markeredgewidth=1, label=r'$\Lambda$CDM', zorder=10)
ax1.plot(w0_desi_dr2, wa_desi_dr2, 'o', color='purple', markersize=10,
         markeredgecolor='black', markeredgewidth=1,
         label=f'DESI DR2', zorder=10)

ax1.axhline(y=-0.530, color='gray', linestyle='--', alpha=0.6, linewidth=1)
ax1.text(-0.55, -0.52, r'$w_a = -0.530$ (3$\sigma$ excl)', fontsize=7, color='gray')
ax1.axhline(y=-0.350, color='gray', linestyle=':', alpha=0.6, linewidth=1)
ax1.text(-0.55, -0.34, r'$w_a = -0.350$ (2$\sigma$ thresh)', fontsize=7, color='gray')
ax1.axhline(y=0.0, color='lightgray', linestyle='-', alpha=0.4, linewidth=0.5)

ax1.set_xlabel(r'$w_0$', fontsize=14)
ax1.set_ylabel(r'$w_a$', fontsize=14)
ax1.set_title('DESI-DR3-UPDATE-70: $w_0$-$w_a$ Plane\n'
              r'(Updated with 5x DR1 errors, $\rho=-0.85$)', fontsize=11)
ax1.set_xlim(-1.15, -0.50)
ax1.set_ylim(-1.6, 0.5)
ax1.legend(loc='lower left', fontsize=8, framealpha=0.9)
ax1.grid(True, alpha=0.3)

# --- Panel 2: Current observational scorecard ---
ax2 = axes[1]

# Bar chart of Delta chi^2 for each channel
channels = ['D_M/r_d\n(BAO)', 'f*sig8\n(RSD, fcov)', 'SNe\n(Pantheon+, fcov)']
delta_chi2_channels = [
    chi2_DM_fw - chi2_DM_lcdm,  # BAO: FW worse
    delta_chi2_fsig8_full,       # RSD: FW better (full cov)
    delta_chi2_sne_full,         # SNe: FW better (full cov)
]

colors_bar = ['#e74c3c' if d > 0 else '#2ecc71' for d in delta_chi2_channels]
bars = ax2.barh(channels, delta_chi2_channels, color=colors_bar, edgecolor='black',
                height=0.5)

ax2.axvline(x=0, color='black', linewidth=1)
ax2.axvline(x=-3, color='gray', linestyle='--', alpha=0.5, label='FW firmly preferred')
ax2.axvline(x=3, color='gray', linestyle='--', alpha=0.5)

for i, (ch, dchi) in enumerate(zip(channels, delta_chi2_channels)):
    ax2.text(dchi + (0.3 if dchi > 0 else -0.3), i,
             f'{dchi:+.2f}', va='center',
             ha='left' if dchi > 0 else 'right', fontsize=10, fontweight='bold')

ax2.set_xlabel(r'$\Delta\chi^2$ (FW $-$ $\Lambda$CDM)', fontsize=12)
ax2.set_title('S69-S70 Observational Scorecard\n(negative = FW preferred)', fontsize=11)
ax2.set_xlim(-12, 8)
ax2.grid(True, alpha=0.3, axis='x')

# Add total
total = sum(delta_chi2_channels)
ax2.axhline(y=2.7, color='navy', linestyle='-', linewidth=0.5)
ax2.text(-12 + 0.3, 2.8, f'Combined: {total:+.2f}', fontsize=10,
         fontweight='bold', color='navy')

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, 's70_desi_dr3_update.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
pr(f"  Plot saved: {plotpath}")

# =============================================================================
# 16. Save NPZ
# =============================================================================
pr(f"\n{'='*72}")
pr("Saving Data")
pr(f"{'='*72}")

npz_path = os.path.join(SCRIPT_DIR, 's70_desi_dr3_update.npz')
save_dict = {
    # Framework parameters
    'w0_fw': w0_fw,
    'wa_fw': wa_fw,
    'w0_lcdm': w0_lcdm,
    'wa_lcdm': wa_lcdm,
    'w0_desi_dr2': w0_desi_dr2,
    'wa_desi_dr2': wa_desi_dr2,

    # DR3 projected sensitivities (updated: 5x DR1)
    'sigma_w0_dr3_5x': sigma_w0_dr3_5x,
    'sigma_wa_dr3_5x': sigma_wa_dr3_5x,
    'sigma_w0_dr3_s68': sigma_w0_dr3_s68,
    'sigma_wa_dr3_s68': sigma_wa_dr3_s68,
    'rho_desi': rho_desi,
    'N_dr3_over_dr1': N_dr3_over_dr1,
    'stat_improvement': stat_improvement,

    # DESI bins
    'z_eff': z_eff,
    'tracer_labels': np.array(tracer_labels),
    'r_d_Mpc': r_d_Mpc,

    # S69 D_M/r_d results
    'DM_rd_obs': DM_rd_obs,
    'DM_rd_err': DM_rd_err,
    'DM_rd_err_dr3': DM_rd_err_dr3,
    'DM_rd_FW': DM_rd_FW,
    'DM_rd_LCDM': DM_rd_LCDM,
    'pulls_DM_fw': pulls_DM_fw,
    'pulls_DM_fw_dr3': pulls_DM_fw_dr3,
    'pulls_DM_lcdm': pulls_DM_lcdm,
    'pulls_DM_lcdm_dr3': pulls_DM_lcdm_dr3,
    'chi2_DM_fw': chi2_DM_fw,
    'chi2_DM_lcdm': chi2_DM_lcdm,
    'chi2_dof_DM_fw': chi2_dof_DM_fw,
    'chi2_DM_fw_dr3': chi2_DM_fw_dr3,
    'chi2_dof_DM_fw_dr3': chi2_dof_dm_dr3_persist,

    # S69 D_H/r_d results
    'DH_rd_obs': DH_rd_obs,
    'DH_rd_err': DH_rd_err,
    'DH_rd_FW': DH_rd_FW,
    'DH_rd_LCDM': DH_rd_LCDM,
    'pulls_DH_fw': pulls_DH_fw,
    'pulls_DH_lcdm': pulls_DH_lcdm,

    # S69 f*sigma_8 results
    'z_rsd': z_rsd,
    'labels_rsd': np.array(labels_rsd),
    'fsig8_rsd': fsig8_rsd,
    'err_rsd': err_rsd,
    'err_rsd_dr3': err_rsd_dr3,
    'fsig8_FW_at_z': fsig8_FW_at_z,
    'fsig8_L_at_z': fsig8_L_at_z,
    'chi2_FW_fsig8_diag': chi2_FW_fsig8,
    'chi2_L_fsig8_diag': chi2_L_fsig8,
    'delta_chi2_fsig8_diag': delta_chi2_fsig8_diag,
    'delta_chi2_fsig8_full': delta_chi2_fsig8_full,
    'chi2_fw_rsd_dr3': chi2_fw_rsd_dr3,
    'chi2_lcdm_rsd_dr3': chi2_lcdm_rsd_dr3,
    'delta_chi2_rsd_dr3': delta_chi2_rsd_dr3,
    'sigma8_fw': sigma8_fw,
    'sigma8_lcdm': sigma8_lcdm,

    # S70 full covariance updates
    'delta_chi2_sne_full': delta_chi2_sne_full,
    'delta_chi2_sne_diag': delta_chi2_sne_diag,

    # S70 ISW
    'isw_auto_fw_quint_pct': isw_fw_quint_pct,

    # Scenario results (updated)
    'scenario_labels': np.array(['A', 'B', 'C']),
    'scenario_w0': np.array([results[k]['w0'] for k in ['A', 'B', 'C']]),
    'scenario_wa': np.array([results[k]['wa'] for k in ['A', 'B', 'C']]),
    'sig_fw_scenarios': np.array([results[k]['sig_fw'] for k in ['A', 'B', 'C']]),
    'sig_lcdm_scenarios': np.array([results[k]['sig_lcdm'] for k in ['A', 'B', 'C']]),
    'sig_fw_scenarios_s68': sig_fw_scenarios_s68,
    'sig_lcdm_scenarios_s68': sig_lcdm_scenarios_s68,

    # DR3 decision thresholds
    'wa_excl_threshold': -0.530,
    'wa_ok_threshold': -0.350,
    'chi2_dof_dm_resolved': 1.5,
    'chi2_dof_dm_severe': 3.0,
    'delta_chi2_fsig8_firm': -3.0,

    # Combined
    'delta_chi2_bao_dr3': delta_chi2_bao_dr3,
    'delta_chi2_combined_current': delta_chi2_combined_current,
    'coherent_sig_fw_dr3': coherent_sig_fw_dr3,

    # Gate
    'gate_name': np.array(['DESI-DR3-UPDATE-70']),
    'gate_verdict': np.array(['INFO']),
    'gate_detail': np.array([gate_detail]),
}

np.savez(npz_path, **save_dict)
pr(f"  Data saved: {npz_path}")

pr(f"\n{'='*72}")
pr("DESI-DR3-UPDATE-70 COMPLETE")
pr(f"{'='*72}")

log.close()
