#!/usr/bin/env python3
"""
s65_desi_dr3_prep.py — DESI-DR3-65: Pre-Registered DR3 Predictions
====================================================================
Gate: DESI-DR3-65 (to be resolved when DR3 data arrives)
  Pre-registered: framework chi^2(DR3) < LCDM chi^2(DR3)
  STRONG PASS:   delta_chi^2 > 4  (framework favored at > 2-sigma)
  MARGINAL PASS: 0 < delta_chi^2 < 4
  FAIL:          delta_chi^2 < 0  (LCDM closer)

Physics:
  Extends S64 DESI-DV-64 (model-independent BAO comparison) into a full
  DR3 pre-registration at 7 EVENLY-SPACED redshift bins z = {0.3, 0.5,
  0.7, 0.9, 1.1, 1.3, 1.5}.

  Framework model: w_0 = -0.918, w_a = -0.645 (substrate compaction from
  S59 TIMESCAPE-WA-59, combined Josephson+GGE + KZ tau-variance).

  DR3 precision: sigma_DR3 ~ sigma_DR1/sqrt(3). DESI DR1 fractional BAO
  precision is ~1-2% per bin; DR3 gains from 3x sky area give sqrt(3)
  improvement. We also compute f*sigma_8(z) at each bin using the
  linear growth ODE from S59 GROWTH-FACTOR-59.

  The key observable test: does DR3 data land closer to the framework's
  D_V(z) predictions or to LCDM's? The framework predicts SHORTER
  distances than LCDM across all z (direction matching DESI DR2 pull).

Upstream:
  - s64_desi_dv.npz: D_V(z)/r_d, sigma_DV_frac, model parameters
  - s59_growth_factor.npz: sigma_8 for framework, growth ratio
  - canonical_constants.py: Omega_m, H_0, sigma_8, etc.

Author: Katie Mack (Cosmic Bridge)
Session: 65, Task DESI-DR3-65
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import interp1d

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, c_light_km_s, T_CMB,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s65_desi_dr3_prep_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 76)
pr("DESI-DR3-65: Pre-Registered DR3 Predictions")
pr("=" * 76)

# =============================================================================
# 1. Cosmological parameters
# =============================================================================
Om_m = Omega_m          # 0.315
Om_b = Omega_b          # 0.0493
Om_r = Omega_r          # 9.15e-5
Om_DE = 1.0 - Om_m - Om_r
h = H_0_km_s_Mpc / 100.0
H_0 = H_0_km_s_Mpc

pr(f"\nCosmological parameters (Planck 2018 baseline):")
pr(f"  Omega_m  = {Om_m}")
pr(f"  Omega_b  = {Om_b}")
pr(f"  Omega_r  = {Om_r}")
pr(f"  Omega_DE = {Om_DE:.6f}")
pr(f"  h        = {h}")
pr(f"  H_0      = {H_0} km/s/Mpc")
pr(f"  sigma_8  = {sigma_8}")

# =============================================================================
# 2. Load upstream data
# =============================================================================
pr(f"\n{'='*76}")
pr("Loading Upstream Data")
pr(f"{'='*76}")

# S64 DESI-DV data
try:
    d64 = np.load(os.path.join(SCRIPT_DIR, 's64_desi_dv.npz'), allow_pickle=True)
    z_eff_dr2 = d64['z_eff']
    sigma_DV_frac_dr2 = d64['sigma_DV_frac']
    w0_fw = float(d64['w0_fw'])
    wa_fw = float(d64['wa_fw'])
    w0_comp = float(d64['w0_comp'])
    wa_comp = float(d64['wa_comp'])
    r_d_Mpc_s64 = float(d64['r_d_Mpc'])
    chi2_fw_dr2 = float(d64['chi2_Framework_vs_LCDM'])
    chi2_lcdm_dr2 = float(d64['chi2_DESI_vs_LCDM'])
    pr(f"  Loaded s64_desi_dv.npz")
    pr(f"  DR2 z_eff = {z_eff_dr2}")
    pr(f"  DR2 sigma_DV_frac = {sigma_DV_frac_dr2}")
    pr(f"  w0_fw = {w0_fw:.6f}, wa_fw = {wa_fw:.6f}")
    pr(f"  w0_comp = {w0_comp:.6f}, wa_comp = {wa_comp:.6f}")
    pr(f"  S64 chi2_FW(vs LCDM) = {chi2_fw_dr2:.3f}")
except Exception as e:
    pr(f"  WARNING: Could not load S64 data: {e}")
    pr(f"  Using hardcoded fallback values")
    # w0_fw = -0.918  # S72: now imported from canonical_constants
    w0_fw = w0_FW  # S72: alias for downstream use
    wa_fw = -0.000575  # (local)
    w0_comp = -0.924  # (local)
    wa_comp = -0.645  # (local)

# S59 growth factor data
try:
    d59 = np.load(os.path.join(SCRIPT_DIR, 's59_growth_factor.npz'), allow_pickle=True)
    sigma8_fw = float(d59['sigma8_wCDM'])
    growth_ratio = float(d59['growth_ratio'])
    gamma_lcdm = float(d59['gamma_LCDM'])
    gamma_wcdm = float(d59['gamma_wCDM'])
    pr(f"  Loaded s59_growth_factor.npz")
    pr(f"  sigma8_fw = {sigma8_fw:.6f} (LCDM: {sigma_8})")
    pr(f"  growth_ratio = {growth_ratio:.6f}")
    pr(f"  gamma_LCDM = {gamma_lcdm}, gamma_wCDM = {gamma_wcdm:.6f}")
except Exception as e:
    pr(f"  WARNING: Could not load S59 data: {e}")
    sigma8_fw = 0.793  # (local)
    growth_ratio = 0.978  # (local)
    gamma_lcdm = 0.55  # (local)
    gamma_wcdm = 0.554  # (local)

# =============================================================================
# 3. Pre-registered redshift bins
# =============================================================================
# Task specifies 7 evenly-spaced bins
z_bins = np.array([0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5])
n_bins = len(z_bins)

pr(f"\n{'='*76}")
pr("Pre-Registered Redshift Bins (DR3)")
pr(f"{'='*76}")
pr(f"  z = {z_bins}")
pr(f"  N_bins = {n_bins}")

# =============================================================================
# 4. DR3 precision estimate
# =============================================================================
# DESI DR1 approximate fractional precision on D_V/r_d per bin
# DR1 had ~5M galaxies across all tracers; DR2 ~11M; DR3 projected ~15-18M
# DR1 precision: BGS ~2.5%, LRG ~1.5-2%, ELG ~1.5%, QSO ~2%, Lya ~2%
# For our evenly-spaced bins we interpolate from DR2 data
# DR3 ~ 3x DR1 sky coverage => sigma_DR3 ~ sigma_DR1 / sqrt(3)

# Interpolate DR2 fractional precision to our bins
# DR2 effective bins: [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330]
# DR2 fractional errors: [0.019, 0.013, 0.009, 0.008, 0.010, 0.015, 0.015]
sigma_dr2_interp = interp1d(
    [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330],
    [0.019, 0.013, 0.009, 0.008, 0.010, 0.015, 0.015],
    kind='linear', fill_value='extrapolate'
)

# DR1 precision is approximately sqrt(2) worse than DR2 (DR2 ~ 2x DR1 data)
sigma_dr1_frac = sigma_dr2_interp(z_bins) * np.sqrt(2)

# DR3 precision: sigma_DR1 / sqrt(3)
sigma_dr3_frac = sigma_dr1_frac / np.sqrt(3)

# Cross-check: this is equivalent to sigma_DR2 * sqrt(2/3)
sigma_dr3_from_dr2 = sigma_dr2_interp(z_bins) * np.sqrt(2.0/3.0)
assert np.allclose(sigma_dr3_frac, sigma_dr3_from_dr2, rtol=1e-10), \
    "DR3 precision cross-check failed"

pr(f"\n  DR3 precision estimate (sigma_DR1/sqrt(3) = sigma_DR2 * sqrt(2/3)):")
pr(f"  {'z':>5s}  {'DR1 frac':>10s}  {'DR2 frac':>10s}  {'DR3 frac':>10s}")
for i in range(n_bins):
    dr2_val = sigma_dr2_interp(z_bins[i])
    pr(f"  {z_bins[i]:5.1f}  {sigma_dr1_frac[i]*100:9.3f}%  {dr2_val*100:9.3f}%  "
       f"{sigma_dr3_frac[i]*100:9.3f}%")

# =============================================================================
# 5. Cosmological distance functions (from S64, reproduced here)
# =============================================================================
def rho_de_ratio_cpl(a, w0, wa):
    """rho_DE(a)/rho_DE(a=1) for CPL parameterization w(a) = w0 + wa*(1-a)"""
    return a**(-3.0*(1.0 + w0 + wa)) * np.exp(-3.0*wa*(1.0 - a))

def E_squared(a, w0, wa):
    """(H(a)/H_0)^2"""
    return Om_r/a**4 + Om_m/a**3 + Om_DE * rho_de_ratio_cpl(a, w0, wa)

def E_of_z(z, w0, wa):
    """H(z)/H_0"""
    a = 1.0 / (1.0 + z)
    return np.sqrt(np.maximum(E_squared(a, w0, wa), 1e-30))

# Sound horizon (Eisenstein & Hu 1998)
omega_b = Om_b * h**2
omega_m = Om_m * h**2
N_eff_std = 3.044
r_d_Mpc = 147.05 * (omega_b/0.02236)**(-0.13) * \
                     (omega_m/0.1432)**(-0.23) * \
                     (N_eff_std/3.04)**(-0.10)
pr(f"\n  Sound horizon: r_d = {r_d_Mpc:.3f} Mpc")

def comoving_dist_Mpc(z, w0, wa):
    """D_M(z) in Mpc (comoving distance for flat cosmology)"""
    prefactor = c_light_km_s / H_0
    integrand = lambda zp: 1.0 / E_of_z(zp, w0, wa)
    result, _ = quad(integrand, 0, z, limit=200, epsrel=1e-10)
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
    """D_V(z)/r_d (dimensionless)"""
    return DV_Mpc(z, w0, wa) / r_d_Mpc

# =============================================================================
# 6. Compute D_V(z)/r_d at pre-registered bins
# =============================================================================
pr(f"\n{'='*76}")
pr("D_V(z)/r_d Predictions at Pre-Registered DR3 Bins")
pr(f"{'='*76}")

# Framework: w_0 = -0.918, w_a = -0.645 (substrate compaction)
# The task specifies these combined parameters
# w0_pre = -0.918  # S72: now imported as w0_FW from canonical_constants
w0_pre = w0_FW  # S72: alias for downstream use
wa_pre = -0.645  # substrate compaction — NOT canonical wa_FW (which is 0.0)  # (local)

# LCDM: w_0 = -1.0, w_a = 0.0
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# DESI DR2 best-fit
w0_desi = -0.752
wa_desi = -0.73

pr(f"\n  Three models:")
pr(f"    Framework (substrate compaction): w_0 = {w0_pre:.3f}, w_a = {wa_pre:.3f}")
pr(f"    LCDM:                            w_0 = {w0_lcdm:.3f}, w_a = {wa_lcdm:.3f}")
pr(f"    DESI DR2 best-fit:               w_0 = {w0_desi:.3f}, w_a = {wa_desi:.2f}")

DV_fw = np.array([DV_over_rd(z, w0_pre, wa_pre) for z in z_bins])
DV_lcdm = np.array([DV_over_rd(z, w0_lcdm, wa_lcdm) for z in z_bins])
DV_desi = np.array([DV_over_rd(z, w0_desi, wa_desi) for z in z_bins])

# Also compute D_M and D_H separately
DM_fw = np.array([comoving_dist_Mpc(z, w0_pre, wa_pre)/r_d_Mpc for z in z_bins])
DM_lcdm = np.array([comoving_dist_Mpc(z, w0_lcdm, wa_lcdm)/r_d_Mpc for z in z_bins])
DH_fw = np.array([hubble_dist_Mpc(z, w0_pre, wa_pre)/r_d_Mpc for z in z_bins])
DH_lcdm = np.array([hubble_dist_Mpc(z, w0_lcdm, wa_lcdm)/r_d_Mpc for z in z_bins])

pr(f"\n  {'z':>5s}  {'DV_FW':>10s}  {'DV_LCDM':>10s}  {'DV_DESI':>10s}  "
   f"{'FW-LCDM%':>10s}  {'DESI-LCDM%':>10s}")
pr(f"  {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

frac_fw = (DV_fw - DV_lcdm) / DV_lcdm
frac_desi = (DV_desi - DV_lcdm) / DV_lcdm

for i in range(n_bins):
    pr(f"  {z_bins[i]:5.1f}  {DV_fw[i]:10.4f}  {DV_lcdm[i]:10.4f}  "
       f"{DV_desi[i]:10.4f}  {frac_fw[i]*100:+9.3f}%  {frac_desi[i]*100:+9.3f}%")

# =============================================================================
# 7. Discriminating power: (D_V^FW - D_V^LCDM) / sigma_DR3
# =============================================================================
pr(f"\n{'='*76}")
pr("Discriminating Power: Per-Bin (D_V^FW - D_V^LCDM) / sigma_DR3(z)")
pr(f"{'='*76}")

# Absolute error in D_V/r_d at each bin
sigma_abs_dr3 = sigma_dr3_frac * DV_lcdm

# Framework vs LCDM separation in sigma
nsig_fw_lcdm = (DV_fw - DV_lcdm) / sigma_abs_dr3
nsig_desi_lcdm = (DV_desi - DV_lcdm) / sigma_abs_dr3
nsig_fw_desi = (DV_fw - DV_desi) / sigma_abs_dr3

pr(f"\n  {'z':>5s}  {'sigma_DR3':>10s}  {'FW-LCDM':>10s}  {'DESI-LCDM':>10s}  "
   f"{'FW-DESI':>10s}  {'|FW-LCDM|':>10s}")
pr(f"  {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

for i in range(n_bins):
    pr(f"  {z_bins[i]:5.1f}  {sigma_abs_dr3[i]:10.4f}  {nsig_fw_lcdm[i]:+9.2f}s  "
       f"{nsig_desi_lcdm[i]:+9.2f}s  {nsig_fw_desi[i]:+9.2f}s  "
       f"{abs(nsig_fw_lcdm[i]):9.2f}s")

# =============================================================================
# 8. Predicted chi^2 for DR3
# =============================================================================
pr(f"\n{'='*76}")
pr("Predicted Combined chi^2 for DR3")
pr(f"{'='*76}")

# chi^2 of framework relative to LCDM reference
# If DR3 data matches LCDM exactly: chi2_fw = sum((DV_fw - DV_lcdm)/sigma)^2
chi2_fw_vs_lcdm = np.sum(nsig_fw_lcdm**2)

# chi^2 of LCDM relative to DESI best-fit (if DR3 lands near DR2 best-fit)
chi2_lcdm_vs_desi = np.sum(nsig_desi_lcdm**2)

# chi^2 of framework relative to DESI best-fit
chi2_fw_vs_desi = np.sum(nsig_fw_desi**2)

pr(f"\n  Scenario 1: DR3 data matches LCDM")
pr(f"    chi2_FW(ref=LCDM)  = {chi2_fw_vs_lcdm:.2f} ({np.sqrt(chi2_fw_vs_lcdm):.2f}-sigma)")
pr(f"    chi2_LCDM(ref=LCDM) = 0.00 (by definition)")
pr(f"    delta_chi2 = {0.0 - chi2_fw_vs_lcdm:.2f} (LCDM wins)")
pr(f"    => FAIL")

pr(f"\n  Scenario 2: DR3 data matches DESI DR2 best-fit")
pr(f"    chi2_FW(ref=DESI)  = {chi2_fw_vs_desi:.2f} ({np.sqrt(chi2_fw_vs_desi):.2f}-sigma)")
pr(f"    chi2_LCDM(ref=DESI) = {chi2_lcdm_vs_desi:.2f} ({np.sqrt(chi2_lcdm_vs_desi):.2f}-sigma)")
delta_chi2_sc2 = chi2_lcdm_vs_desi - chi2_fw_vs_desi
pr(f"    delta_chi2 = chi2_LCDM - chi2_FW = {delta_chi2_sc2:.2f}")
if delta_chi2_sc2 > 4:
    pr(f"    => STRONG PASS (delta > 4)")
elif delta_chi2_sc2 > 0:
    pr(f"    => MARGINAL PASS (0 < delta < 4)")
else:
    pr(f"    => FAIL (delta < 0)")

# Scenario 3: DR3 midway between LCDM and DESI best-fit
DV_mid = (DV_lcdm + DV_desi) / 2.0
nsig_fw_mid = (DV_fw - DV_mid) / sigma_abs_dr3
nsig_lcdm_mid = (DV_lcdm - DV_mid) / sigma_abs_dr3
chi2_fw_mid = np.sum(nsig_fw_mid**2)
chi2_lcdm_mid = np.sum(nsig_lcdm_mid**2)
delta_chi2_sc3 = chi2_lcdm_mid - chi2_fw_mid

pr(f"\n  Scenario 3: DR3 midway between LCDM and DESI best-fit")
pr(f"    chi2_FW(ref=mid)   = {chi2_fw_mid:.2f} ({np.sqrt(chi2_fw_mid):.2f}-sigma)")
pr(f"    chi2_LCDM(ref=mid) = {chi2_lcdm_mid:.2f} ({np.sqrt(chi2_lcdm_mid):.2f}-sigma)")
pr(f"    delta_chi2 = {delta_chi2_sc3:.2f}")
if delta_chi2_sc3 > 4:
    pr(f"    => STRONG PASS (delta > 4)")
elif delta_chi2_sc3 > 0:
    pr(f"    => MARGINAL PASS (0 < delta < 4)")
else:
    pr(f"    => FAIL (delta < 0)")

# =============================================================================
# 9. Identify pivotal redshift bin
# =============================================================================
pr(f"\n{'='*76}")
pr("Pivotal Redshift Bin (Maximum |FW-LCDM|/sigma_DR3)")
pr(f"{'='*76}")

abs_nsig = np.abs(nsig_fw_lcdm)
pivot_idx = np.argmax(abs_nsig)

pr(f"\n  Pivotal bin: z = {z_bins[pivot_idx]:.1f}")
pr(f"    |FW - LCDM|/sigma = {abs_nsig[pivot_idx]:.2f}")
pr(f"    DV_FW/r_d  = {DV_fw[pivot_idx]:.4f}")
pr(f"    DV_LCDM/r_d = {DV_lcdm[pivot_idx]:.4f}")
pr(f"    sigma_DR3 (abs) = {sigma_abs_dr3[pivot_idx]:.4f}")
pr(f"    Fractional deviation: {frac_fw[pivot_idx]*100:+.3f}%")
pr(f"    DR3 fractional precision: {sigma_dr3_frac[pivot_idx]*100:.3f}%")

pr(f"\n  Full ranking:")
rank = np.argsort(-abs_nsig)
for j, i in enumerate(rank):
    pr(f"    #{j+1}: z = {z_bins[i]:.1f}, |n_sigma| = {abs_nsig[i]:.2f}, "
       f"frac = {frac_fw[i]*100:+.3f}%, DR3 err = {sigma_dr3_frac[i]*100:.3f}%")

# =============================================================================
# 10. f*sigma_8(z) computation
# =============================================================================
pr(f"\n{'='*76}")
pr("f*sigma_8(z) at Pre-Registered DR3 Bins")
pr(f"{'='*76}")

# Growth ODE: D'' + [3/a + (1/2)(dE2/da)/E2] D' - (3/2) Om_m / (a^5 E2) D = 0
# We solve for both LCDM and framework (w_0=-0.918, w_a=-0.645)

def E2_model(a, w0, wa):
    """(H(a)/H_0)^2 with CPL dark energy"""
    return Om_r/a**4 + Om_m/a**3 + Om_DE * rho_de_ratio_cpl(a, w0, wa)

def dE2_da_model(a, w0, wa):
    """d(E^2)/da for CPL"""
    # d(Om_r/a^4)/da = -4 Om_r / a^5
    # d(Om_m/a^3)/da = -3 Om_m / a^4
    # For DE: rho_DE(a) = Om_DE * a^p * exp(-3*wa*(1-a)) where p = -3*(1+w0+wa)
    # d(rho_DE)/da = rho_DE * [p/a + 3*wa]
    p = -3.0*(1.0 + w0 + wa)  # (local)
    rho_de = Om_DE * rho_de_ratio_cpl(a, w0, wa)
    return -4.0*Om_r/a**5 - 3.0*Om_m/a**4 + rho_de*(p/a + 3.0*wa)

def growth_rhs(a, y, w0, wa):
    """RHS of growth ODE in scale factor"""
    D, Dp = y
    e2 = E2_model(a, w0, wa)
    de2 = dE2_da_model(a, w0, wa)
    Dpp = -(3.0/a + 0.5*de2/e2)*Dp + 1.5*Om_m/(a**5 * e2)*D
    return [Dp, Dpp]

a_init = 0.001  # (local)
a_final = 1.0  # (local)
y0 = [a_init, 1.0]  # Matter domination: D=a, dD/da=1
a_eval = np.linspace(a_init, a_final, 10000)

# Solve LCDM
sol_L = solve_ivp(lambda a, y: growth_rhs(a, y, -1.0, 0.0),
                  [a_init, a_final], y0, t_eval=a_eval,
                  method='RK45', rtol=1e-10, atol=1e-12)
assert sol_L.success, f"LCDM growth integration failed: {sol_L.message}"

D_L = sol_L.y[0]
Dp_L = sol_L.y[1]
a_arr = sol_L.t
D_L_norm = D_L / D_L[-1]
Dp_L_norm = Dp_L / D_L[-1]
f_L = a_arr * Dp_L_norm / D_L_norm
fsig8_L = f_L * sigma_8 * D_L_norm

# Solve framework (w_0=-0.918, w_a=-0.645)
sol_F = solve_ivp(lambda a, y: growth_rhs(a, y, w0_pre, wa_pre),
                  [a_init, a_final], y0, t_eval=a_eval,
                  method='RK45', rtol=1e-10, atol=1e-12)
assert sol_F.success, f"Framework growth integration failed: {sol_F.message}"

D_F = sol_F.y[0]
Dp_F = sol_F.y[1]
a_F = sol_F.t

# sigma_8 for framework: same primordial A_s => sigma_8 scales by D(1) ratio
growth_ratio_comp = D_F[-1] / D_L[-1]
sigma8_comp = sigma_8 * growth_ratio_comp

D_F_norm = D_F / D_F[-1]
Dp_F_norm = Dp_F / D_F[-1]
f_F = a_F * Dp_F_norm / D_F_norm
fsig8_F = f_F * sigma8_comp * D_F_norm

pr(f"\n  Growth computation:")
pr(f"    D(a=1) ratio [FW/LCDM] = {growth_ratio_comp:.6f}")
pr(f"    sigma_8(LCDM) = {sigma_8:.4f}")
pr(f"    sigma_8(FW)   = {sigma8_comp:.4f} (same A_s assumption)")

# Interpolate to our bins
a_bins = 1.0/(1.0 + z_bins)
iL_fsig8 = interp1d(a_arr, fsig8_L, kind='cubic')
iF_fsig8 = interp1d(a_F, fsig8_F, kind='cubic')
iL_f = interp1d(a_arr, f_L, kind='cubic')
iF_f = interp1d(a_F, f_F, kind='cubic')

fsig8_L_bins = iL_fsig8(a_bins)
fsig8_F_bins = iF_fsig8(a_bins)
f_L_bins = iL_f(a_bins)
f_F_bins = iF_f(a_bins)

frac_fsig8 = (fsig8_F_bins - fsig8_L_bins) / fsig8_L_bins

# Approximate f*sigma_8 errors for DESI DR3
# DESI DR1 f*sig8 precision per bin: ~4-8% (from DESI KP-VII)
# Map approximate errors per bin
# Low z (BGS, z~0.3): ~5%, Mid z (LRG/ELG, z~0.5-1.0): ~4%, High z (ELG, z~1.1-1.5): ~6-8%
# DR3 improvement: sqrt(3) from DR1
fsig8_err_dr1 = np.array([0.025, 0.020, 0.018, 0.018, 0.022, 0.028, 0.035])
fsig8_err_dr3 = fsig8_err_dr1 / np.sqrt(3)

abs_diff_fsig8 = fsig8_F_bins - fsig8_L_bins
nsig_fsig8 = np.abs(abs_diff_fsig8) / fsig8_err_dr3

pr(f"\n  f*sigma_8(z) comparison:")
pr(f"  {'z':>5s}  {'f*sig8_FW':>12s}  {'f*sig8_LCDM':>12s}  {'frac_diff':>10s}  "
   f"{'DR3 err':>10s}  {'n_sigma':>8s}")
pr(f"  {'-'*5}  {'-'*12}  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*8}")

for i in range(n_bins):
    pr(f"  {z_bins[i]:5.1f}  {fsig8_F_bins[i]:12.6f}  {fsig8_L_bins[i]:12.6f}  "
       f"{frac_fsig8[i]*100:+9.3f}%  {fsig8_err_dr3[i]:10.4f}  {nsig_fsig8[i]:7.2f}s")

chi2_fsig8 = np.sum(nsig_fsig8**2)
pr(f"\n  Combined f*sigma_8 chi2 (FW vs LCDM): {chi2_fsig8:.2f} "
   f"({np.sqrt(chi2_fsig8):.2f}-sigma)")

# =============================================================================
# 11. Combined BAO + f*sigma_8 discriminating power
# =============================================================================
pr(f"\n{'='*76}")
pr("Combined BAO + f*sigma_8 Discriminating Power")
pr(f"{'='*76}")

# Total chi2 combining D_V and f*sigma_8 (treating as independent)
chi2_total = chi2_fw_vs_lcdm + chi2_fsig8
pr(f"\n  D_V chi2 (7 bins):        {chi2_fw_vs_lcdm:.2f}")
pr(f"  f*sigma_8 chi2 (7 bins):  {chi2_fsig8:.2f}")
pr(f"  Combined chi2 (14 dof):   {chi2_total:.2f} ({np.sqrt(chi2_total):.2f}-sigma)")
pr(f"\n  The BAO distance channel dominates: {chi2_fw_vs_lcdm/chi2_total*100:.1f}% of total chi2")

# =============================================================================
# 12. Summary table
# =============================================================================
pr(f"\n{'='*76}")
pr("PRE-REGISTERED PREDICTIONS SUMMARY TABLE")
pr(f"{'='*76}")

pr(f"\n### Framework model: w_0 = {w0_pre}, w_a = {wa_pre}")
pr(f"### DR3 precision: sigma_DR1/sqrt(3)")
pr(f"### Pivotal bin: z = {z_bins[pivot_idx]:.1f}")
pr(f"")
pr(f"| z   | DV_FW/r_d | DV_LCDM/r_d | FW-LCDM [%] | sigma_DR3 | n_sig | "
   f"f*sig8_FW | f*sig8_LCDM | f*sig8 diff [%] |")
pr(f"|:----|:----------|:------------|:------------|:----------|:------|"
   f":----------|:------------|:----------------|")
for i in range(n_bins):
    pr(f"| {z_bins[i]:.1f} | {DV_fw[i]:.4f} | {DV_lcdm[i]:.4f} | "
       f"{frac_fw[i]*100:+.3f} | {sigma_dr3_frac[i]*100:.3f}% | "
       f"{abs(nsig_fw_lcdm[i]):.2f} | "
       f"{fsig8_F_bins[i]:.4f} | {fsig8_L_bins[i]:.4f} | "
       f"{frac_fsig8[i]*100:+.3f} |")

pr(f"\n### Predicted chi^2 (DR3 precision)")
pr(f"| Scenario | chi2_FW | chi2_LCDM | delta_chi2 | Verdict |")
pr(f"|:---------|:--------|:----------|:-----------|:--------|")
pr(f"| Data = LCDM | {chi2_fw_vs_lcdm:.1f} | 0.0 | "
   f"{-chi2_fw_vs_lcdm:.1f} | FAIL |")
sc2_v = "STRONG PASS" if delta_chi2_sc2 > 4 else ("MARGINAL PASS" if delta_chi2_sc2 > 0 else "FAIL")
pr(f"| Data = DESI bf | {chi2_fw_vs_desi:.1f} | {chi2_lcdm_vs_desi:.1f} | "
   f"{delta_chi2_sc2:+.1f} | {sc2_v} |")
sc3_v = "STRONG PASS" if delta_chi2_sc3 > 4 else ("MARGINAL PASS" if delta_chi2_sc3 > 0 else "FAIL")
pr(f"| Data = midpoint | {chi2_fw_mid:.1f} | {chi2_lcdm_mid:.1f} | "
   f"{delta_chi2_sc3:+.1f} | {sc3_v} |")

# =============================================================================
# 13. Structural assessment
# =============================================================================
pr(f"\n{'='*76}")
pr("STRUCTURAL ASSESSMENT")
pr(f"{'='*76}")

pr(f"""
The substrate compaction model (w_0 = {w0_pre}, w_a = {wa_pre}) introduces
redshift-dependent dark energy that is STRONGER than LCDM at low z (less
DE => shorter distances) and WEAKER at high z (more DE in the past).

Direction comparison with DESI:
- DESI DR2 best-fit (w_0 = {w0_desi}, w_a = {wa_desi}) also has w > -1
  at low z and w < -1 at high z (Quintom B crossing).
- The framework's w(z) = w_0 + w_a*(1-a) also produces a crossing,
  but from a different physical mechanism (fiber tau tracking density).

Key structural constraint (from S64):
- The framework's D_V deviations are monotonically shorter than LCDM.
- DESI best-fit deviations show a z-dependent pattern with diminishing
  deficit at high z.
- The framework is CLOSER to DESI than LCDM is at all redshifts below
  z ~ 1, but the pattern correlation is weak (r = -0.04 at DR2 bins).

DR3 discriminating power:
- BAO distances: {np.sqrt(chi2_fw_vs_lcdm):.1f}-sigma separation FW vs LCDM.
- f*sigma_8: {np.sqrt(chi2_fsig8):.1f}-sigma separation (growth rate).
- Combined: {np.sqrt(chi2_total):.1f}-sigma ({n_bins*2} effective dof).
- Pivotal bin: z = {z_bins[pivot_idx]:.1f} (highest discriminating power).

The gate resolves as follows:
- If DR3 confirms DESI direction (w_0 > -1, w_a < 0):
  LCDM is FURTHER from data than substrate FW, but substrate FW is even
  FURTHER (distances go LONGER, not shorter). Both lose to DESI.
  delta_chi2 = {delta_chi2_sc2:+.1f} => {sc2_v}.
- If DR3 reverts to w = -1 (LCDM): substrate FW is FURTHER from data.
  delta_chi2 = {-chi2_fw_vs_lcdm:.1f} => FAIL.
- If DR3 lands midway: delta_chi2 = {delta_chi2_sc3:+.1f} => {sc3_v}.
NOTE: The PURE framework (w_a=0, w_0=-0.918) was CLOSER to DESI than
LCDM (S64 chi2: FW=14.2 vs LCDM=21.7). The w_a=-0.645 reverses this.
""")

# =============================================================================
# 14. Gate verdict (pre-registered, awaiting DR3)
# =============================================================================
pr(f"\n{'='*76}")
pr("GATE VERDICT: DESI-DR3-65")
pr(f"{'='*76}")

verdict = "PRE-REGISTERED"
detail = (
    f"Pre-registered D_V(z)/r_d and f*sig_8(z) at 7 bins z=0.3-1.5 "
    f"with w_0={w0_pre}, w_a={wa_pre}. "
    f"FW-LCDM separation: {np.sqrt(chi2_fw_vs_lcdm):.1f}-sig (BAO), "
    f"{np.sqrt(chi2_fsig8):.1f}-sig (growth). "
    f"Pivotal bin: z={z_bins[pivot_idx]:.1f}. "
    f"Decision: chi2_LCDM - chi2_FW > 4 => STRONG PASS. "
    f"If DESI-like: delta={delta_chi2_sc2:+.1f}. "
    f"If LCDM-like: delta={-chi2_fw_vs_lcdm:.1f}."
)

pr(f"\n  Gate: DESI-DR3-65")
pr(f"  Status: {verdict}")
pr(f"  Detail: {detail}")

# =============================================================================
# 15. Save outputs
# =============================================================================
out = {
    # Bins
    'z_bins': z_bins,
    'n_bins': np.array(n_bins),

    # Framework model parameters
    'w0_pre': np.array(w0_pre),
    'wa_pre': np.array(wa_pre),

    # DR3 precision
    'sigma_dr1_frac': sigma_dr1_frac,
    'sigma_dr3_frac': sigma_dr3_frac,
    'sigma_abs_dr3': sigma_abs_dr3,

    # D_V predictions
    'DV_fw': DV_fw,
    'DV_lcdm': DV_lcdm,
    'DV_desi': DV_desi,
    'DM_fw': DM_fw,
    'DM_lcdm': DM_lcdm,
    'DH_fw': DH_fw,
    'DH_lcdm': DH_lcdm,
    'r_d_Mpc': np.array(r_d_Mpc),

    # Fractional deviations
    'frac_DV_fw': frac_fw,
    'frac_DV_desi': frac_desi,

    # Per-bin significance
    'nsig_fw_lcdm': nsig_fw_lcdm,
    'nsig_desi_lcdm': nsig_desi_lcdm,
    'nsig_fw_desi': nsig_fw_desi,

    # Chi-squared (BAO)
    'chi2_fw_vs_lcdm': np.array(chi2_fw_vs_lcdm),
    'chi2_lcdm_vs_desi': np.array(chi2_lcdm_vs_desi),
    'chi2_fw_vs_desi': np.array(chi2_fw_vs_desi),
    'chi2_fw_mid': np.array(chi2_fw_mid),
    'chi2_lcdm_mid': np.array(chi2_lcdm_mid),
    'delta_chi2_sc2': np.array(delta_chi2_sc2),
    'delta_chi2_sc3': np.array(delta_chi2_sc3),

    # Pivotal bin
    'pivot_idx': np.array(pivot_idx),
    'pivot_z': np.array(z_bins[pivot_idx]),
    'pivot_nsig': np.array(abs_nsig[pivot_idx]),

    # f*sigma_8
    'fsig8_F_bins': fsig8_F_bins,
    'fsig8_L_bins': fsig8_L_bins,
    'frac_fsig8': frac_fsig8,
    'fsig8_err_dr3': fsig8_err_dr3,
    'nsig_fsig8': nsig_fsig8,
    'chi2_fsig8': np.array(chi2_fsig8),
    'sigma8_comp': np.array(sigma8_comp),
    'growth_ratio_comp': np.array(growth_ratio_comp),

    # Combined
    'chi2_total': np.array(chi2_total),

    # Growth functions (full arrays for future use)
    'f_L_bins': f_L_bins,
    'f_F_bins': f_F_bins,

    # Gate
    'gate_name': np.array(['DESI-DR3-65']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
}

npz_path = os.path.join(SCRIPT_DIR, 's65_desi_dr3_prep.npz')
np.savez(npz_path, **out)
pr(f"\n  Saved: {npz_path}")

# =============================================================================
# 16. Plot
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# --- Top left: D_V/r_d predictions ---
ax = axes[0, 0]
z_fine = np.linspace(0.1, 1.8, 200)

DV_fw_fine = np.array([DV_over_rd(z, w0_pre, wa_pre) for z in z_fine])
DV_lcdm_fine = np.array([DV_over_rd(z, -1.0, 0.0) for z in z_fine])
DV_desi_fine = np.array([DV_over_rd(z, w0_desi, wa_desi) for z in z_fine])

ax.plot(z_fine, DV_lcdm_fine, 'b-', lw=2, label=r'$\Lambda$CDM')
ax.plot(z_fine, DV_fw_fine, 'r--', lw=2,
        label=f'Framework ($w_0$={w0_pre}, $w_a$={wa_pre})')
ax.plot(z_fine, DV_desi_fine, 'm:', lw=2,
        label=f'DESI DR2 bf ($w_0$={w0_desi}, $w_a$={wa_desi})')

# DR3 error bars on LCDM
DV_lcdm_err = sigma_dr3_frac * DV_lcdm
ax.errorbar(z_bins, DV_lcdm, yerr=DV_lcdm_err, fmt='ko', capsize=4,
            markersize=5, zorder=5, label='LCDM + DR3 precision')

ax.set_ylabel(r'$D_V(z)/r_d$', fontsize=13)
ax.set_title('DESI-DR3-65: Pre-Registered BAO Predictions', fontsize=13)
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(0.1, 1.7)
ax.grid(True, alpha=0.3)

# --- Top right: Fractional deviations from LCDM ---
ax = axes[0, 1]
frac_fw_fine = (DV_fw_fine - DV_lcdm_fine)/DV_lcdm_fine * 100
frac_desi_fine = (DV_desi_fine - DV_lcdm_fine)/DV_lcdm_fine * 100

ax.plot(z_fine, frac_fw_fine, 'r--', lw=2, label=f'Framework')
ax.plot(z_fine, frac_desi_fine, 'm:', lw=2, label=f'DESI DR2 bf')
ax.fill_between(z_bins, -sigma_dr3_frac*100, sigma_dr3_frac*100,
                alpha=0.15, color='blue', label='DR3 1-$\\sigma$')  # (local)
ax.axhline(0, color='k', lw=0.5)

# Mark pivotal bin
ax.axvline(z_bins[pivot_idx], color='gold', lw=2, ls='--', alpha=0.7,
           label=f'Pivotal: z={z_bins[pivot_idx]:.1f}')

ax.set_xlabel('Redshift $z$', fontsize=13)
ax.set_ylabel(r'$(D_V - D_V^{\Lambda{\rm CDM}})/D_V^{\Lambda{\rm CDM}}$ [%]', fontsize=11)
ax.set_title('Fractional Deviation from LCDM', fontsize=13)
ax.set_xlim(0.1, 1.7)
ax.set_ylim(-4, 2)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Bottom left: Per-bin significance ---
ax = axes[1, 0]
x = np.arange(n_bins)
width = 0.35  # (local)
bars1 = ax.bar(x - width/2, np.abs(nsig_fw_lcdm), width, color='red',
               alpha=0.7, label='FW - LCDM')  # (local)
bars2 = ax.bar(x + width/2, np.abs(nsig_desi_lcdm), width, color='purple',
               alpha=0.7, label='DESI bf - LCDM')  # (local)

ax.axhline(2.0, color='orange', ls='--', lw=1, label='2-sigma')
ax.axhline(3.0, color='red', ls='--', lw=1, label='3-sigma')

ax.set_xticks(x)
ax.set_xticklabels([f'{z:.1f}' for z in z_bins])
ax.set_xlabel('Redshift $z$', fontsize=13)
ax.set_ylabel('$|\\Delta D_V|/\\sigma_{\\rm DR3}$', fontsize=13)
ax.set_title('Per-Bin Discriminating Power (DR3)', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# --- Bottom right: f*sigma_8 ---
ax = axes[1, 1]

# Full curves
z_for_fsig = np.linspace(0.1, 1.7, 200)
a_for_fsig = 1.0/(1.0 + z_for_fsig)
iL_full = interp1d(a_arr, fsig8_L, kind='cubic')
iF_full = interp1d(a_F, fsig8_F, kind='cubic')

# Only interpolate where a is in range
mask = (a_for_fsig >= a_init) & (a_for_fsig <= a_final)
fsig8_L_full = iL_full(a_for_fsig[mask])
fsig8_F_full = iF_full(a_for_fsig[mask])

ax.plot(z_for_fsig[mask], fsig8_L_full, 'b-', lw=2, label=r'$\Lambda$CDM')
ax.plot(z_for_fsig[mask], fsig8_F_full, 'r--', lw=2, label='Framework')
ax.errorbar(z_bins, fsig8_L_bins, yerr=fsig8_err_dr3, fmt='ko', capsize=4,
            markersize=5, zorder=5, label='LCDM + DR3 err')
ax.errorbar(z_bins, fsig8_F_bins, yerr=fsig8_err_dr3, fmt='rs', capsize=4,
            markersize=5, zorder=5, alpha=0.7, label='FW + DR3 err')

ax.set_xlabel('Redshift $z$', fontsize=13)
ax.set_ylabel(r'$f\sigma_8(z)$', fontsize=13)
ax.set_title(r'Growth Rate $f\sigma_8(z)$ Predictions', fontsize=13)
ax.set_xlim(0.1, 1.7)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.suptitle('DESI-DR3-65: Pre-Registered Predictions for DESI DR3',
             fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's65_desi_dr3_prep.png'),
            dpi=150, bbox_inches='tight')
pr(f"  Saved: s65_desi_dr3_prep.png")

pr(f"\n{'='*76}")
pr("DONE")
pr(f"{'='*76}")

log.close()
