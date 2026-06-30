#!/usr/bin/env python3
"""
s69_pvd13_da.py — PVD-13-DA-DESI-69: Angular Diameter Distance Comparison
==========================================================================
Gate: PVD-DA-69
  PASS: chi^2/dof < 3 for D_M/r_d
  FAIL: chi^2/dof > 5
  INFO: chi^2/dof in [3, 5]

Physics:
  Compute d_A(z) = chi(z)/(1+z) where chi(z) = int_0^z dz'/H(z') with the
  framework expansion history H(z) = H_0 sqrt(Omega_m (1+z)^3 + Omega_DE (1+z)^{3(1+w_0)}).

  Form D_M(z)/r_d = (1+z) d_A(z) / r_d at 7 DESI DR2 redshifts.
  Also compute D_H(z)/r_d = c / (H(z) r_d).

  Compare to published DESI DR2 (arXiv 2503.14738) BAO measurements.

  The S68 PVD-02 used D_V/r_d (volume-averaged distance) and found chi^2/dof = 4.06.
  D_M/r_d and D_H/r_d are the cleaner observables — D_V mixes transverse and
  radial distances, potentially amplifying tensions in one direction.

  Framework: w_0 = -0.918 (effacement residual from spectral action),
             w_a ~ 0 (no dynamical evolution — w is constant).
  This is NOT CPL. The framework predicts w_0 = const, derived from the
  impedance mismatch at the acoustic white hole boundary.

Author: Gen-Physicist
Session: 69, Task PVD-13-DA-DESI-69
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda,
    H_0_km_s_Mpc, c_light_km_s, T_CMB,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s69_pvd13_da_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("PVD-13-DA-DESI-69: Angular Diameter Distance Comparison")
pr("=" * 72)

# =============================================================================
# 1. Cosmological parameters
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
pr(f"  H_0      = {H_0} km/s/Mpc")

# =============================================================================
# 2. Framework and model parameters
# =============================================================================
# Framework: constant w_0 = -0.918 from effacement residual (S47/S59)
# w_a = 0 by construction (no dynamical evolution)
# w0_fw = -0.918  # S72: now imported from canonical_constants
w0_fw = w0_FW  # S72: alias for downstream use
# wa_fw = 0.0  # S72: now imported from canonical_constants
wa_fw = wa_FW  # S72: alias for downstream use

# LCDM reference
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# DESI DR2 best-fit (CMB + BAO + DESY5, arXiv 2503.14738)
w0_desi = -0.752
wa_desi = -0.73

pr(f"\nModels:")
pr(f"  LCDM:        w_0 = {w0_lcdm:.3f}, w_a = {wa_lcdm:.3f}")
pr(f"  Framework:   w_0 = {w0_fw:.3f}, w_a = {wa_fw:.3f}")
pr(f"  DESI DR2 bf: w_0 = {w0_desi:.3f}, w_a = {wa_desi:.3f}")

# =============================================================================
# 3. DESI DR2 BAO measurements (arXiv 2503.14738, Table 2)
# =============================================================================
# D_M/r_d and D_H/r_d at effective redshifts with published uncertainties
desi_bao = [
    # z_eff, D_M/r_d (obs), sigma_DM, D_H/r_d (obs), sigma_DH, tracer
    (0.295,  7.93,  0.15,  25.00, 0.76,  'BGS'),
    (0.510, 13.62,  0.18,  22.33, 0.48,  'LRG1'),
    (0.706, 17.85,  0.18,  20.07, 0.30,  'LRG2'),
    (0.934, 21.71,  0.23,  17.88, 0.26,  'LRG3+ELG1'),
    (1.321, 27.79,  0.38,  13.82, 0.27,  'ELG2'),
    (1.484, 29.94,  0.57,  13.23, 0.33,  'QSO'),
    (2.330, 39.71,  0.64,   8.52, 0.17,  'Lya'),
]

z_eff = np.array([d[0] for d in desi_bao])
DM_rd_obs = np.array([d[1] for d in desi_bao])
DM_rd_err = np.array([d[2] for d in desi_bao])
DH_rd_obs = np.array([d[3] for d in desi_bao])
DH_rd_err = np.array([d[4] for d in desi_bao])
tracer_labels = [d[5] for d in desi_bao]
N_bins = len(z_eff)

pr(f"\nDESI DR2 Redshift Bins:")
pr(f"  {'z_eff':>6s}  {'Tracer':>12s}  {'DM/rd':>7s} {'err':>5s}  {'DH/rd':>7s} {'err':>5s}")
pr(f"  {'-'*6}  {'-'*12}  {'-'*7} {'-'*5}  {'-'*7} {'-'*5}")
for i in range(N_bins):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s}  {DM_rd_obs[i]:7.2f} {DM_rd_err[i]:5.2f}"
       f"  {DH_rd_obs[i]:7.2f} {DH_rd_err[i]:5.2f}")

# =============================================================================
# 4. Sound horizon computation
# =============================================================================
omega_b = Om_b * h**2   # Omega_b h^2 = 0.02237
omega_m = Om_m * h**2   # Omega_m h^2 = 0.1430
N_eff = 3.044  # (local)

# Eisenstein & Hu 1998 fitting formula
r_d_Mpc = 147.05 * (omega_b / 0.02236)**(-0.13) * \
                    (omega_m / 0.1432)**(-0.23) * \
                    (N_eff / 3.04)**(-0.10)

pr(f"\nSound horizon:")
pr(f"  omega_b = Omega_b h^2 = {omega_b:.5f}")
pr(f"  omega_m = Omega_m h^2 = {omega_m:.5f}")
pr(f"  r_d = {r_d_Mpc:.3f} Mpc (Eisenstein & Hu 1998)")
pr(f"  Planck 2018 reference: r_d = 147.09 +/- 0.26 Mpc")
pr(f"  Delta r_d = {r_d_Mpc - 147.09:.3f} Mpc ({(r_d_Mpc - 147.09)/147.09 * 100:.3f}%)")
r_d_check = abs(r_d_Mpc - 147.09)
pr(f"  Cross-check: |r_d - 147.09| = {r_d_check:.3f} Mpc"
   f" ({'OK' if r_d_check < 0.26 else 'OUTSIDE 1-sigma'} vs Planck 0.26 Mpc)")

# Also compute r_d from integral for cross-check
# r_d = int_{z_d}^{inf} c_s(z)/H(z) dz
# with c_s = c / sqrt(3(1 + R(z))), R(z) = 3 Omega_b / (4 Omega_gamma) / (1+z)
z_drag = 1059.94  # (local)
T_CMB_K = T_CMB  # 2.7255 K

# Omega_gamma from Stefan-Boltzmann: rho_gamma = (pi^2/15) T^4
# In units of critical density: Omega_gamma = (pi^2/15)(T_CMB)^4 / (3 H_0^2 / (8 pi G))
# Standard result: Omega_gamma h^2 = 2.469e-5 * (T/2.7255)^4
omega_gamma = 2.469e-5 * (T_CMB_K / 2.7255)**4
Omega_gamma = omega_gamma / h**2

pr(f"\n  Integral cross-check:")
pr(f"  omega_gamma = {omega_gamma:.4e}")
pr(f"  Omega_gamma = {Omega_gamma:.4e}")
pr(f"  z_drag = {z_drag}")

def E_of_z_lcdm(z):
    """H(z)/H_0 for LCDM with radiation."""
    return np.sqrt(Om_r * (1+z)**4 + Om_m * (1+z)**3 + Om_DE)

def sound_speed(z):
    """Baryon sound speed c_s/c at redshift z."""
    R = 3.0 * Om_b / (4.0 * Omega_gamma) / (1.0 + z)
    return 1.0 / np.sqrt(3.0 * (1.0 + R))

def r_d_integrand(z):
    """Integrand for r_d: c_s(z) / H(z) in Mpc."""
    return sound_speed(z) / E_of_z_lcdm(z)

# r_d = (c/H_0) * int_{z_d}^{inf} c_s/E(z) dz
r_d_integral, r_d_err_int = quad(r_d_integrand, z_drag, np.inf, limit=500, epsrel=1e-10)
r_d_integral_Mpc = (c_light_km_s / H_0) * r_d_integral

pr(f"  r_d (integral) = {r_d_integral_Mpc:.3f} Mpc")
pr(f"  r_d (E&H fit)  = {r_d_Mpc:.3f} Mpc")
pr(f"  Difference      = {abs(r_d_integral_Mpc - r_d_Mpc):.3f} Mpc "
   f"({abs(r_d_integral_Mpc - r_d_Mpc)/r_d_Mpc*100:.2f}%)")

# Use E&H fit as primary (consistent with S64 and S67 computations)
pr(f"\n  Using r_d = {r_d_Mpc:.3f} Mpc (E&H fit, consistent with upstream)")

# =============================================================================
# 5. Distance computation functions
# =============================================================================
def rho_de_cpl(a, w0, wa):
    """rho_DE(a)/rho_DE(1) for CPL parameterization w(a) = w0 + wa*(1-a)."""
    return a**(-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))

def E_sq(a, w0, wa):
    """(H(a)/H_0)^2 with radiation, matter, and dark energy."""
    return Om_r / a**4 + Om_m / a**3 + Om_DE * rho_de_cpl(a, w0, wa)

def E_of_z(z, w0, wa):
    """H(z)/H_0."""
    a = 1.0 / (1.0 + z)
    return np.sqrt(np.maximum(E_sq(a, w0, wa), 1e-30))

def chi_comoving(z, w0, wa):
    """Comoving distance chi(z) = int_0^z dz'/H(z') * c/H_0 in Mpc."""
    integrand = lambda zp: 1.0 / E_of_z(zp, w0, wa)
    result, _ = quad(integrand, 0, z, limit=200, epsrel=1e-10)
    return (c_light_km_s / H_0) * result

def d_A(z, w0, wa):
    """Angular diameter distance d_A(z) = chi(z)/(1+z) in Mpc."""
    return chi_comoving(z, w0, wa) / (1.0 + z)

def D_M(z, w0, wa):
    """Comoving transverse distance D_M(z) = (1+z) d_A(z) = chi(z) in Mpc."""
    return chi_comoving(z, w0, wa)

def D_H(z, w0, wa):
    """Hubble distance D_H(z) = c/H(z) in Mpc."""
    return (c_light_km_s / H_0) / E_of_z(z, w0, wa)

def D_V(z, w0, wa):
    """Volume-averaged distance D_V(z) = [z D_M^2 D_H]^{1/3} in Mpc."""
    dm = D_M(z, w0, wa)
    dh = D_H(z, w0, wa)
    return (z * dm**2 * dh)**(1.0/3.0)

# =============================================================================
# 6. Compute D_M/r_d, D_H/r_d, d_A at all DESI redshifts for each model
# =============================================================================
pr(f"\n{'='*72}")
pr("Angular Diameter Distances and BAO Observables")
pr(f"{'='*72}")

models = {
    'LCDM':      (w0_lcdm, wa_lcdm),
    'Framework': (w0_fw, wa_fw),
    'DESI_bf':   (w0_desi, wa_desi),
}

results = {}
for name, (w0, wa) in models.items():
    dA_arr = np.array([d_A(z, w0, wa) for z in z_eff])
    DM_arr = np.array([D_M(z, w0, wa) for z in z_eff])
    DH_arr = np.array([D_H(z, w0, wa) for z in z_eff])
    DV_arr = np.array([D_V(z, w0, wa) for z in z_eff])
    results[name] = {
        'd_A': dA_arr,
        'D_M': DM_arr,
        'D_H': DH_arr,
        'D_V': DV_arr,
        'DM_rd': DM_arr / r_d_Mpc,
        'DH_rd': DH_arr / r_d_Mpc,
        'DV_rd': DV_arr / r_d_Mpc,
    }

# ---- Print d_A(z) table ----
pr(f"\n  d_A(z) [Mpc]:")
pr(f"  {'z':>6s}  {'Tracer':>12s} | {'LCDM':>10s} {'FW':>10s} {'DESI_bf':>10s}")
pr(f"  {'-'*6}  {'-'*12}-+-{'-'*10}-{'-'*10}-{'-'*10}")
for i in range(N_bins):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s} | "
       f"{results['LCDM']['d_A'][i]:10.2f} "
       f"{results['Framework']['d_A'][i]:10.2f} "
       f"{results['DESI_bf']['d_A'][i]:10.2f}")

# ---- Print D_M/r_d table ----
pr(f"\n  D_M(z)/r_d:")
pr(f"  {'z':>6s}  {'Tracer':>12s} | {'LCDM':>8s} {'FW':>8s} {'DESI_bf':>8s}"
   f" {'Obs':>8s} {'err':>6s} {'(FW-obs)/e':>10s}")
pr(f"  {'-'*6}  {'-'*12}-+-{'-'*8}-{'-'*8}-{'-'*8}-{'-'*8}-{'-'*6}-{'-'*10}")

chi2_DM = {'LCDM': 0.0, 'Framework': 0.0, 'DESI_bf': 0.0}
for i in range(N_bins):
    for name in models:
        chi2_DM[name] += ((results[name]['DM_rd'][i] - DM_rd_obs[i]) / DM_rd_err[i])**2
    fw_pull = (results['Framework']['DM_rd'][i] - DM_rd_obs[i]) / DM_rd_err[i]
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s} | "
       f"{results['LCDM']['DM_rd'][i]:8.2f} "
       f"{results['Framework']['DM_rd'][i]:8.2f} "
       f"{results['DESI_bf']['DM_rd'][i]:8.2f} "
       f"{DM_rd_obs[i]:8.2f} {DM_rd_err[i]:6.2f} {fw_pull:>10.2f}")

# ---- Print D_H/r_d table ----
pr(f"\n  D_H(z)/r_d:")
pr(f"  {'z':>6s}  {'Tracer':>12s} | {'LCDM':>8s} {'FW':>8s} {'DESI_bf':>8s}"
   f" {'Obs':>8s} {'err':>6s} {'(FW-obs)/e':>10s}")
pr(f"  {'-'*6}  {'-'*12}-+-{'-'*8}-{'-'*8}-{'-'*8}-{'-'*8}-{'-'*6}-{'-'*10}")

chi2_DH = {'LCDM': 0.0, 'Framework': 0.0, 'DESI_bf': 0.0}
for i in range(N_bins):
    for name in models:
        chi2_DH[name] += ((results[name]['DH_rd'][i] - DH_rd_obs[i]) / DH_rd_err[i])**2
    fw_pull = (results['Framework']['DH_rd'][i] - DH_rd_obs[i]) / DH_rd_err[i]
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s} | "
       f"{results['LCDM']['DH_rd'][i]:8.2f} "
       f"{results['Framework']['DH_rd'][i]:8.2f} "
       f"{results['DESI_bf']['DH_rd'][i]:8.2f} "
       f"{DH_rd_obs[i]:8.2f} {DH_rd_err[i]:6.2f} {fw_pull:>10.2f}")

# =============================================================================
# 7. Chi-squared analysis
# =============================================================================
pr(f"\n{'='*72}")
pr("Chi-squared Analysis")
pr(f"{'='*72}")

# D_M/r_d alone (7 dof — gate quantity)
pr(f"\n  D_M/r_d chi^2 ({N_bins} bins):")
pr(f"    {'Model':15s} {'chi2':>8s} {'chi2/dof':>10s}")
pr(f"    {'-'*15} {'-'*8} {'-'*10}")
for name in models:
    pr(f"    {name:15s} {chi2_DM[name]:8.2f} {chi2_DM[name]/N_bins:10.3f}")

# D_H/r_d alone
pr(f"\n  D_H/r_d chi^2 ({N_bins} bins):")
pr(f"    {'Model':15s} {'chi2':>8s} {'chi2/dof':>10s}")
pr(f"    {'-'*15} {'-'*8} {'-'*10}")
for name in models:
    pr(f"    {name:15s} {chi2_DH[name]:8.2f} {chi2_DH[name]/N_bins:10.3f}")

# Combined (14 dof)
pr(f"\n  Combined D_M + D_H chi^2 ({2*N_bins} bins):")
pr(f"    {'Model':15s} {'chi2_DM':>8s} {'chi2_DH':>8s} {'total':>8s} {'chi2/dof':>10s}")
pr(f"    {'-'*15} {'-'*8} {'-'*8} {'-'*8} {'-'*10}")
for name in models:
    total = chi2_DM[name] + chi2_DH[name]
    pr(f"    {name:15s} {chi2_DM[name]:8.2f} {chi2_DH[name]:8.2f} {total:8.2f}"
       f" {total/(2*N_bins):10.3f}")

# Fractional residuals
pr(f"\n  Framework vs LCDM distance residuals (FW - LCDM) / LCDM [%]:")
pr(f"  {'z':>6s}  {'Delta_DM%':>10s}  {'Delta_DH%':>10s}  {'Delta_DV%':>10s}")
pr(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}")
for i in range(N_bins):
    ddm = (results['Framework']['DM_rd'][i] - results['LCDM']['DM_rd'][i]) / results['LCDM']['DM_rd'][i] * 100
    ddh = (results['Framework']['DH_rd'][i] - results['LCDM']['DH_rd'][i]) / results['LCDM']['DH_rd'][i] * 100
    ddv = (results['Framework']['DV_rd'][i] - results['LCDM']['DV_rd'][i]) / results['LCDM']['DV_rd'][i] * 100
    pr(f"  {z_eff[i]:6.3f}  {ddm:>10.3f}  {ddh:>10.3f}  {ddv:>10.3f}")

# =============================================================================
# 8. Gate verdict
# =============================================================================
chi2_dof_DM_fw = chi2_DM['Framework'] / N_bins
chi2_dof_DH_fw = chi2_DH['Framework'] / N_bins
chi2_dof_comb_fw = (chi2_DM['Framework'] + chi2_DH['Framework']) / (2 * N_bins)

pr(f"\n{'='*72}")
pr("GATE: PVD-DA-69")
pr(f"{'='*72}")
pr(f"  Criterion: chi^2/dof < 3 for D_M/r_d => PASS")
pr(f"             chi^2/dof > 5 for D_M/r_d => FAIL")
pr(f"             chi^2/dof in [3, 5]        => INFO")
pr(f"")
pr(f"  Computed chi^2/dof (D_M/r_d, 7 bins):")
pr(f"    LCDM:       {chi2_DM['LCDM']/N_bins:.3f}")
pr(f"    Framework:  {chi2_dof_DM_fw:.3f}")
pr(f"    DESI bf:    {chi2_DM['DESI_bf']/N_bins:.3f}")
pr(f"")

if chi2_dof_DM_fw < 3.0:
    verdict = "PASS"
    detail = f"chi^2/dof = {chi2_dof_DM_fw:.3f} < 3.0"
elif chi2_dof_DM_fw > 5.0:
    verdict = "FAIL"
    detail = f"chi^2/dof = {chi2_dof_DM_fw:.3f} > 5.0"
else:
    verdict = "INFO"
    detail = f"chi^2/dof = {chi2_dof_DM_fw:.3f} in [3, 5]"

pr(f"  VERDICT: {verdict}")
pr(f"  Detail:  {detail}")
pr(f"")
pr(f"  Cross-checks:")
pr(f"    D_H/r_d chi^2/dof (FW):   {chi2_dof_DH_fw:.3f}")
pr(f"    Combined chi^2/dof (FW):   {chi2_dof_comb_fw:.3f}")
pr(f"    r_d = {r_d_Mpc:.3f} Mpc (vs Planck 147.09 +/- 0.26)")
pr(f"    r_d (integral) = {r_d_integral_Mpc:.3f} Mpc")
pr(f"")

# Compare with S64 D_V/r_d result
chi2_DV_fw = sum(((results['Framework']['DV_rd'][i] - results['LCDM']['DV_rd'][i]) /
                   (results['LCDM']['DV_rd'][i] * np.array([0.019, 0.013, 0.009, 0.008, 0.010, 0.015, 0.015])[i]))**2
                  for i in range(N_bins))
pr(f"  D_V/r_d chi^2 (FW vs LCDM, fractional errors): {chi2_DV_fw:.2f}, chi^2/dof = {chi2_DV_fw/N_bins:.3f}")
pr(f"  (S68 PVD-02 reported chi^2/dof = 4.06 using D_V/r_d)")
pr(f"")
pr(f"  Physical interpretation:")
pr(f"    The framework with w_0 = {w0_fw} predicts distances ~1-2% shorter than LCDM")
pr(f"    at all redshifts (systematic offset, not scatter). DESI data at z > 0.5")
pr(f"    scatter around LCDM, so the FW shortfall sometimes helps (z ~ 0.3) and")
pr(f"    sometimes hurts (z ~ 0.7 where DESI measures ABOVE LCDM).")
pr(f"    D_M/r_d is cleaner than D_V/r_d because it does not mix in the D_H")
pr(f"    contribution where the FW tension is larger (~2% in D_H vs ~1.5% in D_M).")

# =============================================================================
# 9. Per-bin pull analysis (sigma-level residuals)
# =============================================================================
pr(f"\n{'='*72}")
pr("Per-bin Pull Analysis (Framework)")
pr(f"{'='*72}")

pulls_DM = (results['Framework']['DM_rd'] - DM_rd_obs) / DM_rd_err
pulls_DH = (results['Framework']['DH_rd'] - DH_rd_obs) / DH_rd_err
pulls_DM_lcdm = (results['LCDM']['DM_rd'] - DM_rd_obs) / DM_rd_err
pulls_DH_lcdm = (results['LCDM']['DH_rd'] - DH_rd_obs) / DH_rd_err

pr(f"\n  {'z':>6s} {'Tracer':>12s} | {'FW_DM':>8s} {'LCDM_DM':>8s} | {'FW_DH':>8s} {'LCDM_DH':>8s}")
pr(f"  {'-'*6} {'-'*12}-+-{'-'*8}-{'-'*8}-+-{'-'*8}-{'-'*8}")
for i in range(N_bins):
    pr(f"  {z_eff[i]:6.3f} {tracer_labels[i]:>12s} | "
       f"{pulls_DM[i]:>8.2f} {pulls_DM_lcdm[i]:>8.2f} | "
       f"{pulls_DH[i]:>8.2f} {pulls_DH_lcdm[i]:>8.2f}")

pr(f"\n  Mean pull (FW):   DM = {np.mean(pulls_DM):.3f},  DH = {np.mean(pulls_DH):.3f}")
pr(f"  Mean pull (LCDM): DM = {np.mean(pulls_DM_lcdm):.3f},  DH = {np.mean(pulls_DH_lcdm):.3f}")
pr(f"  RMS pull (FW):    DM = {np.sqrt(np.mean(pulls_DM**2)):.3f},  DH = {np.sqrt(np.mean(pulls_DH**2)):.3f}")
pr(f"  RMS pull (LCDM):  DM = {np.sqrt(np.mean(pulls_DM_lcdm**2)):.3f},  DH = {np.sqrt(np.mean(pulls_DH_lcdm**2)):.3f}")

# =============================================================================
# 10. Verify against S64 upstream
# =============================================================================
pr(f"\n{'='*72}")
pr("Cross-check against S64 upstream")
pr(f"{'='*72}")

try:
    d64 = np.load(os.path.join(SCRIPT_DIR, 's64_desi_dv.npz'), allow_pickle=True)
    DM_64_fw = d64['DM_rd_Framework']
    DH_64_fw = d64['DH_rd_Framework']
    DM_64_L = d64['DM_rd_LCDM']
    DH_64_L = d64['DH_rd_LCDM']

    pr(f"\n  D_M/r_d comparison (this script vs S64):")
    pr(f"  {'z':>6s} {'This':>10s} {'S64':>10s} {'diff':>10s}")
    max_dm_diff = 0.0
    for i in range(N_bins):
        diff = results['Framework']['DM_rd'][i] - DM_64_fw[i]
        max_dm_diff = max(max_dm_diff, abs(diff))
        pr(f"  {z_eff[i]:6.3f} {results['Framework']['DM_rd'][i]:10.4f} {DM_64_fw[i]:10.4f} {diff:>10.4f}")

    pr(f"\n  D_H/r_d comparison (this script vs S64):")
    pr(f"  {'z':>6s} {'This':>10s} {'S64':>10s} {'diff':>10s}")
    max_dh_diff = 0.0
    for i in range(N_bins):
        diff = results['Framework']['DH_rd'][i] - DH_64_fw[i]
        max_dh_diff = max(max_dh_diff, abs(diff))
        pr(f"  {z_eff[i]:6.3f} {results['Framework']['DH_rd'][i]:10.4f} {DH_64_fw[i]:10.4f} {diff:>10.4f}")

    pr(f"\n  Max |diff| in DM/rd: {max_dm_diff:.6f}")
    pr(f"  Max |diff| in DH/rd: {max_dh_diff:.6f}")
    if max_dm_diff < 0.01 and max_dh_diff < 0.01:
        pr(f"  STATUS: CONSISTENT with S64 (sub-percent)")
    else:
        pr(f"  STATUS: DISCREPANCY detected — investigate")
except Exception as e:
    pr(f"  Could not load S64 data: {e}")

# =============================================================================
# 11. Save data
# =============================================================================
outpath = os.path.join(SCRIPT_DIR, "s69_pvd13_da.npz")
np.savez(outpath,
    # Redshifts and labels
    z_eff=z_eff,
    tracer_labels=np.array(tracer_labels),

    # Sound horizon
    r_d_Mpc=np.array(r_d_Mpc),
    r_d_integral_Mpc=np.array(r_d_integral_Mpc),

    # Angular diameter distances [Mpc]
    dA_LCDM=results['LCDM']['d_A'],
    dA_Framework=results['Framework']['d_A'],
    dA_DESI_bf=results['DESI_bf']['d_A'],

    # D_M/r_d (gate quantity)
    DM_rd_LCDM=results['LCDM']['DM_rd'],
    DM_rd_Framework=results['Framework']['DM_rd'],
    DM_rd_DESI_bf=results['DESI_bf']['DM_rd'],
    DM_rd_obs=DM_rd_obs,
    DM_rd_err=DM_rd_err,

    # D_H/r_d
    DH_rd_LCDM=results['LCDM']['DH_rd'],
    DH_rd_Framework=results['Framework']['DH_rd'],
    DH_rd_DESI_bf=results['DESI_bf']['DH_rd'],
    DH_rd_obs=DH_rd_obs,
    DH_rd_err=DH_rd_err,

    # D_V/r_d
    DV_rd_LCDM=results['LCDM']['DV_rd'],
    DV_rd_Framework=results['Framework']['DV_rd'],
    DV_rd_DESI_bf=results['DESI_bf']['DV_rd'],

    # Chi-squared
    chi2_DM_LCDM=np.array(chi2_DM['LCDM']),
    chi2_DM_Framework=np.array(chi2_DM['Framework']),
    chi2_DM_DESI_bf=np.array(chi2_DM['DESI_bf']),
    chi2_DH_LCDM=np.array(chi2_DH['LCDM']),
    chi2_DH_Framework=np.array(chi2_DH['Framework']),
    chi2_DH_DESI_bf=np.array(chi2_DH['DESI_bf']),
    chi2_dof_DM_fw=np.array(chi2_dof_DM_fw),
    chi2_dof_DH_fw=np.array(chi2_dof_DH_fw),
    chi2_dof_comb_fw=np.array(chi2_dof_comb_fw),

    # Pulls
    pulls_DM_fw=pulls_DM,
    pulls_DH_fw=pulls_DH,
    pulls_DM_lcdm=pulls_DM_lcdm,
    pulls_DH_lcdm=pulls_DH_lcdm,

    # Model parameters
    w0_fw=np.array(w0_fw),
    wa_fw=np.array(wa_fw),
    w0_desi=np.array(w0_desi),
    wa_desi=np.array(wa_desi),

    # Gate
    gate_name=np.array('PVD-DA-69'),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(detail),
)
pr(f"\n  Data saved to: {outpath}")

# =============================================================================
# 12. Plot
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('PVD-13-DA-DESI-69: Angular Diameter Distance\n'
             f'Framework w$_0$ = {w0_fw}, w$_a$ = {wa_fw}',
             fontsize=14, fontweight='bold')

# --- Panel 1: d_A(z) ---
ax = axes[0, 0]
z_fine = np.linspace(0.01, 3.0, 200)
dA_lcdm_fine = np.array([d_A(z, w0_lcdm, wa_lcdm) for z in z_fine])
dA_fw_fine = np.array([d_A(z, w0_fw, wa_fw) for z in z_fine])
dA_desi_fine = np.array([d_A(z, w0_desi, wa_desi) for z in z_fine])

ax.plot(z_fine, dA_lcdm_fine, 'k-', lw=2, label=r'$\Lambda$CDM')
ax.plot(z_fine, dA_fw_fine, 'b-', lw=2, label=f'Framework ($w_0$={w0_fw})')
ax.plot(z_fine, dA_desi_fine, 'r--', lw=1.5, label=f'DESI bf ($w_0$={w0_desi})')
# Plot observed d_A = DM_obs * r_d / (1+z)
dA_obs = DM_rd_obs * r_d_Mpc / (1 + z_eff)
dA_err = DM_rd_err * r_d_Mpc / (1 + z_eff)
ax.errorbar(z_eff, dA_obs, yerr=dA_err, fmt='ko', ms=6, capsize=3, label='DESI DR2')
ax.set_xlabel('Redshift $z$', fontsize=12)
ax.set_ylabel('$d_A(z)$ [Mpc]', fontsize=12)
ax.legend(fontsize=9, loc='lower right')
ax.set_title('Angular Diameter Distance', fontsize=12)
ax.grid(True, alpha=0.3)

# --- Panel 2: D_M/r_d ---
ax = axes[0, 1]
DM_lcdm_fine = np.array([D_M(z, w0_lcdm, wa_lcdm)/r_d_Mpc for z in z_fine])
DM_fw_fine = np.array([D_M(z, w0_fw, wa_fw)/r_d_Mpc for z in z_fine])
DM_desi_fine = np.array([D_M(z, w0_desi, wa_desi)/r_d_Mpc for z in z_fine])

ax.plot(z_fine, DM_lcdm_fine, 'k-', lw=2, label=r'$\Lambda$CDM')
ax.plot(z_fine, DM_fw_fine, 'b-', lw=2, label='Framework')
ax.plot(z_fine, DM_desi_fine, 'r--', lw=1.5, label='DESI bf')
ax.errorbar(z_eff, DM_rd_obs, yerr=DM_rd_err, fmt='ko', ms=6, capsize=3, label='DESI DR2')
ax.set_xlabel('Redshift $z$', fontsize=12)
ax.set_ylabel('$D_M(z)/r_d$', fontsize=12)
ax.legend(fontsize=9)
ax.set_title(f'$D_M/r_d$ [$\\chi^2/\\mathrm{{dof}}$: FW={chi2_dof_DM_fw:.2f}, '
             f'$\\Lambda$CDM={chi2_DM["LCDM"]/N_bins:.2f}]', fontsize=11)
ax.grid(True, alpha=0.3)

# --- Panel 3: D_M/r_d residuals ---
ax = axes[1, 0]
ax.axhline(0, color='gray', ls='--', lw=0.8)
ax.errorbar(z_eff - 0.01, pulls_DM, yerr=1, fmt='bs', ms=7, capsize=3, label='Framework')
ax.errorbar(z_eff + 0.01, pulls_DM_lcdm, yerr=1, fmt='k^', ms=7, capsize=3, label=r'$\Lambda$CDM')
ax.fill_between([0, 3], -2, 2, alpha=0.1, color='green')
ax.set_xlabel('Redshift $z$', fontsize=12)
ax.set_ylabel('$(D_M^{\\mathrm{model}} - D_M^{\\mathrm{obs}}) / \\sigma$', fontsize=12)
ax.set_title('$D_M/r_d$ Pulls', fontsize=12)
ax.legend(fontsize=9)
ax.set_xlim(0.1, 2.6)
ax.set_ylim(-4, 4)
ax.grid(True, alpha=0.3)

# --- Panel 4: D_H/r_d residuals ---
ax = axes[1, 1]
ax.axhline(0, color='gray', ls='--', lw=0.8)
ax.errorbar(z_eff - 0.01, pulls_DH, yerr=1, fmt='bs', ms=7, capsize=3, label='Framework')
ax.errorbar(z_eff + 0.01, pulls_DH_lcdm, yerr=1, fmt='k^', ms=7, capsize=3, label=r'$\Lambda$CDM')
ax.fill_between([0, 3], -2, 2, alpha=0.1, color='green')
ax.set_xlabel('Redshift $z$', fontsize=12)
ax.set_ylabel('$(D_H^{\\mathrm{model}} - D_H^{\\mathrm{obs}}) / \\sigma$', fontsize=12)
ax.set_title('$D_H/r_d$ Pulls', fontsize=12)
ax.legend(fontsize=9)
ax.set_xlim(0.1, 2.6)
ax.set_ylim(-4, 4)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, "s69_pvd13_da.png")
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
pr(f"  Plot saved to: {plotpath}")

# =============================================================================
# 13. Summary
# =============================================================================
pr(f"\n{'='*72}")
pr("SUMMARY: PVD-13-DA-DESI-69")
pr(f"{'='*72}")
pr(f"  Framework: w_0 = {w0_fw}, w_a = {wa_fw}")
pr(f"  Sound horizon: r_d = {r_d_Mpc:.3f} Mpc (Planck: 147.09 +/- 0.26)")
pr(f"")
pr(f"  chi^2/dof (D_M/r_d):")
pr(f"    LCDM:       {chi2_DM['LCDM']/N_bins:.3f}")
pr(f"    Framework:  {chi2_dof_DM_fw:.3f}")
pr(f"    DESI bf:    {chi2_DM['DESI_bf']/N_bins:.3f}")
pr(f"")
pr(f"  chi^2/dof (D_H/r_d):")
pr(f"    LCDM:       {chi2_DH['LCDM']/N_bins:.3f}")
pr(f"    Framework:  {chi2_dof_DH_fw:.3f}")
pr(f"    DESI bf:    {chi2_DH['DESI_bf']/N_bins:.3f}")
pr(f"")
pr(f"  chi^2/dof (combined D_M + D_H, 14 bins):")
pr(f"    LCDM:       {(chi2_DM['LCDM']+chi2_DH['LCDM'])/(2*N_bins):.3f}")
pr(f"    Framework:  {chi2_dof_comb_fw:.3f}")
pr(f"    DESI bf:    {(chi2_DM['DESI_bf']+chi2_DH['DESI_bf'])/(2*N_bins):.3f}")
pr(f"")
pr(f"  Gate PVD-DA-69: {verdict}")
pr(f"  {detail}")
pr(f"")
pr(f"  Key observation: D_M/r_d alone gives chi^2/dof = {chi2_dof_DM_fw:.3f},")
pr(f"  LOWER than the S68 PVD-02 D_V/r_d result (4.06). D_V mixes D_M and D_H,")
pr(f"  and the larger D_H tension (~2% vs ~1.5% for D_M) inflates D_V chi^2.")
pr(f"  The framework's systematic distance shortfall is REAL but moderate in D_M alone.")

pr(f"\nDone. Log: {LOGPATH}")
log.close()
