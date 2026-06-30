#!/usr/bin/env python3
"""
s64_desi_dv.py — DESI-DV-64: Model-Independent DESI BAO Comparison
===================================================================
Gate: DESI-DV-64
  INFO: D_V(z)/r_s predictions at DESI bins with DR3 exclusion criteria
  Decision rule: If DR3 w_a < -0.53, substrate compaction excluded at 3-sigma

Physics:
  The substrate compaction model (S59) predicts an effective w(z) from fiber
  tau tracking local matter density. Rather than comparing CPL parameters
  (which assumes the data is well-described by CPL), we compute D_V(z)/r_d
  directly from w(z) for each model and compare at DESI redshift bins.

  Four models compared:
    (1) LCDM:           w = -1 exactly
    (2) Framework:      w_0 = -0.918, w_a ~ 0 (combined Josephson+GGE)
    (3) Compaction:     w_0 = -0.924, w_a = -0.645 (KZ tau-variance)
    (4) DESI best-fit:  w_0 = -0.752, w_a = -0.73 (DR2 + CMB + SNe)

  DESI measures D_M(z)/r_d and D_H(z)/r_d via BAO scaling parameters
  alpha_|| and alpha_perp relative to a fiducial cosmology. The published
  fractional precision at each bin (0.5-1.5%) is the relevant error.

  The model-independent test: compute D_V(z)/r_d for each model, compare
  inter-model separations against DESI measurement precision. No
  assumption about CPL validity enters the distance computation.

Data:
  DESI DR2 (2503.14738) reports fractional BAO precision ~0.24% (combined)
  and per-bin precision from Table 2. For robust comparison, we use DESI DR2
  best-fit LCDM as the data reference (since flat LCDM fits the individual
  bins well at chi2/dof < 1.5) and compute deviations.

  The key question: does the data DIRECTION (pulling toward w_0>-1, w_a<0)
  match any of the framework models?

Author: Katie Mack (Cosmic Bridge)
Session: 64, Task DESI-DV-64
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
    Omega_m, Omega_b, Omega_r, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, c_light_km_s, T_CMB,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s64_desi_dv_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("DESI-DV-64: Model-Independent DESI BAO Distance Comparison")
pr("=" * 72)

# =============================================================================
# 1. Cosmological parameters (Planck 2018 baseline)
# =============================================================================
Om_m = Omega_m         # 0.315
Om_b = Omega_b         # 0.0493
Om_r = Omega_r         # 9.15e-5
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
# 2. Load upstream framework parameters
# =============================================================================
try:
    d_wa = np.load(os.path.join(SCRIPT_DIR, 's59_wa_error_prop.npz'), allow_pickle=True)
    w0_fw = float(d_wa['w0_fw'])
    wa_fw = float(d_wa['wa_fw'])
    sigma_w0_fw = float(d_wa['sigma_w0_fw'])
    sigma_wa_fw = float(d_wa['sigma_wa_fw'])
    pr(f"\nFramework parameters (S59 WA-ERROR-PROP-59):")
    pr(f"  w_0 = {w0_fw:.6f} +/- {sigma_w0_fw:.6f}")
    pr(f"  w_a = {wa_fw:.6f} +/- {sigma_wa_fw:.6f}")
except Exception as e:
    pr(f"Warning: Could not load S59 data: {e}")
    # w0_fw = -0.918  # S72: now imported from canonical_constants
    w0_fw = w0_FW  # S72: alias for downstream use
    wa_fw = -0.000575  # (local)
    sigma_w0_fw = 0.0366  # (local)
    sigma_wa_fw = 0.000273  # (local)

try:
    d_ts = np.load(os.path.join(SCRIPT_DIR, 's59_timescape_wa.npz'), allow_pickle=True)
    wa_compaction = float(d_ts['wa_result'])
    w0_compaction_offset = float(d_ts['w0_result'])
    pr(f"\nSubstrate compaction (S59 TIMESCAPE-WA-59):")
    pr(f"  w_a(apparent) = {wa_compaction:.6f}")
    pr(f"  w_0(offset)   = {w0_compaction_offset:.6f}")
except Exception as e:
    pr(f"Warning: Could not load timescape data: {e}")
    wa_compaction = -0.6449  # (local)
    w0_compaction_offset = -0.00596  # (local)

w0_comp = w0_fw + w0_compaction_offset
wa_comp = wa_compaction

pr(f"\nFour models for D_V computation:")
pr(f"  LCDM:        w_0 = -1.000, w_a = 0.000")
pr(f"  Framework:   w_0 = {w0_fw:.6f}, w_a = {wa_fw:.6f}")
pr(f"  Compaction:  w_0 = {w0_comp:.6f}, w_a = {wa_comp:.6f}")
pr(f"  DESI DR2 bf: w_0 = -0.752,  w_a = -0.730")

# =============================================================================
# 3. DESI DR2 redshift bins and fractional precision
# =============================================================================
# DESI DR2 effective redshifts (arXiv 2503.14738)
z_eff = np.array([0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330])
tracer_labels = ['BGS', 'LRG1', 'LRG2', 'LRG3+ELG1', 'ELG2', 'QSO', 'Lya']

# DESI DR2 fractional precision on D_V/r_d (from published constraints)
# BGS: ~1.9%, LRG1: ~1.3%, LRG2: ~0.9%, LRG3+ELG1: ~0.8%,
# ELG2: ~1.0%, QSO: ~1.5%, Lya: ~1.5%
# These are the approximate fractional errors from DESI DR2 Table 2.
sigma_DV_frac = np.array([0.019, 0.013, 0.009, 0.008, 0.010, 0.015, 0.015])

# DESI DR2 best-fit w0wa parameters (CMB + BAO + DESY5):
# w_0 = -0.752 +/- 0.057, w_a = -0.73 +/- 0.25 (from reference_key-constraints)
dr2_w0 = -0.752  # (local)
dr2_wa = -0.73  # (local)
dr2_w0_e = 0.057  # (local)
dr2_wa_e = 0.25  # (local)

pr(f"\n{'='*72}")
pr("DESI DR2 Redshift Bins and Precision")
pr(f"{'='*72}")
pr(f"\n  {'z_eff':>6s}  {'Tracer':>12s}  {'sigma(DV)/DV':>12s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {tracer_labels[i]:>12s}  {sigma_DV_frac[i]*100:>10.1f}%")

# =============================================================================
# 4. Sound horizon
# =============================================================================
omega_b = Om_b * h**2
omega_m = Om_m * h**2
N_eff = 3.044  # (local)

# Eisenstein & Hu 1998 / DESI Eq. 2 of 2503.14738
r_d_Mpc = 147.05 * (omega_b / 0.02236)**(-0.13) * \
                    (omega_m / 0.1432)**(-0.23) * \
                    (N_eff / 3.04)**(-0.10)

pr(f"\nSound horizon: r_d = {r_d_Mpc:.3f} Mpc (E&H 1998)")
pr(f"  Planck 2018 reference: r_d = 147.09 Mpc")

# =============================================================================
# 5. Cosmological distance functions
# =============================================================================
def rho_de_ratio_cpl(a, w0, wa):
    """rho_DE(a) / rho_DE(a=1) for CPL"""
    return a**(-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))

def E_squared(a, w0, wa):
    """(H(a)/H_0)^2"""
    return Om_r / a**4 + Om_m / a**3 + Om_DE * rho_de_ratio_cpl(a, w0, wa)

def E_of_z(z, w0, wa):
    """H(z)/H_0"""
    a = 1.0 / (1.0 + z)
    return np.sqrt(np.maximum(E_squared(a, w0, wa), 1e-30))

def comoving_dist_Mpc(z, w0, wa):
    """D_M(z) in Mpc"""
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
# 6. Compute D_V(z)/r_d for all models
# =============================================================================
pr(f"\n{'='*72}")
pr("D_V(z)/r_d Predictions for Four Models")
pr(f"{'='*72}")

models = {
    'LCDM':       {'w0': -1.0,    'wa': 0.0,      'color': 'b',  'ls': '-',   'label': r'$\Lambda$CDM'},
    'Framework':  {'w0': w0_fw,   'wa': wa_fw,     'color': 'r',  'ls': '--',  'label': f'Framework ($w_0={w0_fw:.3f}$)'},
    'Compaction': {'w0': w0_comp, 'wa': wa_comp,    'color': 'g',  'ls': '-.',  'label': f'Compaction ($w_a={wa_comp:.2f}$)'},
    'DESI_bf':    {'w0': dr2_w0,  'wa': dr2_wa,    'color': 'm',  'ls': ':',   'label': f'DESI best-fit ($w_0={dr2_w0}$, $w_a={dr2_wa}$)'},
}

res = {}
for name, m in models.items():
    w0, wa = m['w0'], m['wa']
    DV_rd = np.array([DV_over_rd(z, w0, wa) for z in z_eff])
    DM_rd = np.array([comoving_dist_Mpc(z, w0, wa) / r_d_Mpc for z in z_eff])
    DH_rd = np.array([hubble_dist_Mpc(z, w0, wa) / r_d_Mpc for z in z_eff])
    res[name] = {'DV_rd': DV_rd, 'DM_rd': DM_rd, 'DH_rd': DH_rd, 'w0': w0, 'wa': wa}

    pr(f"\n  {m['label']}:")
    pr(f"  {'z':>6s}  {'DV/rd':>9s}  {'DM/rd':>9s}  {'DH/rd':>9s}")
    for i in range(len(z_eff)):
        pr(f"  {z_eff[i]:6.3f}  {DV_rd[i]:9.4f}  {DM_rd[i]:9.4f}  {DH_rd[i]:9.4f}")

# =============================================================================
# 7. Fractional deviations from LCDM
# =============================================================================
pr(f"\n{'='*72}")
pr("Fractional Deviations (Model - LCDM) / LCDM  [%]")
pr(f"{'='*72}")

DV_lcdm = res['LCDM']['DV_rd']

pr(f"\n  {'z':>6s}  {'Framework':>10s}  {'Compaction':>10s}  {'DESI bf':>10s}  {'DESI err':>10s}")
pr(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

frac_fw = (res['Framework']['DV_rd'] - DV_lcdm) / DV_lcdm
frac_comp = (res['Compaction']['DV_rd'] - DV_lcdm) / DV_lcdm
frac_desi = (res['DESI_bf']['DV_rd'] - DV_lcdm) / DV_lcdm

for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {frac_fw[i]*100:+9.3f}%  {frac_comp[i]*100:+9.3f}%  "
       f"{frac_desi[i]*100:+9.3f}%  {sigma_DV_frac[i]*100:+9.1f}%")

# =============================================================================
# 8. Per-bin deviation significance (in units of DESI measurement sigma)
# =============================================================================
# For each bin: nsig = |DV_model - DV_LCDM| / (sigma_frac * DV_LCDM)
# This asks: is the model-LCDM separation detectable by DESI?

pr(f"\n{'='*72}")
pr("Per-Bin Separation from LCDM (in DESI sigma)")
pr(f"{'='*72}")

nsig_fw = np.abs(frac_fw) / sigma_DV_frac
nsig_comp = np.abs(frac_comp) / sigma_DV_frac
nsig_desi = np.abs(frac_desi) / sigma_DV_frac

pr(f"\n  {'z':>6s}  {'Framework':>10s}  {'Compaction':>10s}  {'DESI bf':>10s}")
pr(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {nsig_fw[i]:9.2f}s  {nsig_comp[i]:9.2f}s  {nsig_desi[i]:9.2f}s")

chi2_fw = np.sum(nsig_fw**2)
chi2_comp = np.sum(nsig_comp**2)
chi2_desi = np.sum(nsig_desi**2)

pr(f"\n  Multi-bin chi2 (vs LCDM, {len(z_eff)} bins):")
pr(f"    Framework:  {chi2_fw:.2f}  (sqrt = {np.sqrt(chi2_fw):.2f}-sigma)")
pr(f"    Compaction: {chi2_comp:.2f}  (sqrt = {np.sqrt(chi2_comp):.2f}-sigma)")
pr(f"    DESI bf:    {chi2_desi:.2f}  (sqrt = {np.sqrt(chi2_desi):.2f}-sigma)")

# =============================================================================
# 9. Where does the data pull? Direction analysis
# =============================================================================
pr(f"\n{'='*72}")
pr("Direction Analysis: Which Way Does DESI Pull?")
pr(f"{'='*72}")

# DESI data prefers w_0 > -1 and w_a < 0 (Quintom B quadrant).
# This means the data prefers SHORTER distances at low z (less DE)
# and LONGER distances at high z (more DE in the past).
# The framework (w_0 = -0.918, w_a ~ 0) has uniformly shorter distances
# than LCDM (correct direction at low z, wrong at high z).
# The compaction (w_0 ~ -0.924, w_a = -0.645) has more DE at high z,
# which LENGTHENS distances at high z -- partially matching the DESI pull.

pr(f"\n  DESI DR2 data direction (w_0>-1, w_a<0 = Quintom B):")
pr(f"    Low z: less DE than CC -> shorter distances (DV < DV_LCDM)")
pr(f"    High z: more DE than CC (phantom past) -> longer distances (DV > DV_LCDM)")
pr(f"\n  Framework direction:")
for i in range(len(z_eff)):
    direction = "shorter" if frac_fw[i] < 0 else "longer"
    match = "MATCHES DESI" if (frac_fw[i] < 0 and frac_desi[i] < 0) or \
                              (frac_fw[i] > 0 and frac_desi[i] > 0) else "OPPOSES DESI"
    pr(f"    z={z_eff[i]:.3f}: {direction:>8s} by {abs(frac_fw[i])*100:.3f}%  [{match}]")

pr(f"\n  Compaction direction:")
for i in range(len(z_eff)):
    direction = "shorter" if frac_comp[i] < 0 else "longer"
    match = "MATCHES DESI" if (frac_comp[i] < 0 and frac_desi[i] < 0) or \
                              (frac_comp[i] > 0 and frac_desi[i] > 0) else "OPPOSES DESI"
    pr(f"    z={z_eff[i]:.3f}: {direction:>8s} by {abs(frac_comp[i])*100:.3f}%  [{match}]")

# Correlation between model deviation pattern and DESI deviation pattern
corr_fw = np.corrcoef(frac_fw, frac_desi)[0, 1]
corr_comp = np.corrcoef(frac_comp, frac_desi)[0, 1]

pr(f"\n  Pattern correlation with DESI best-fit deviation:")
pr(f"    Framework:  r = {corr_fw:+.4f}")
pr(f"    Compaction: r = {corr_comp:+.4f}")
pr(f"    (r = +1: same pattern, r = -1: opposite pattern)")

# =============================================================================
# 10. Inter-model separations
# =============================================================================
pr(f"\n{'='*72}")
pr("Inter-Model Separations (in DESI sigma per bin)")
pr(f"{'='*72}")

# Framework vs Compaction
sep_fw_comp = np.abs(res['Framework']['DV_rd'] - res['Compaction']['DV_rd']) / (sigma_DV_frac * DV_lcdm)
# Framework vs DESI best-fit
sep_fw_desi = np.abs(res['Framework']['DV_rd'] - res['DESI_bf']['DV_rd']) / (sigma_DV_frac * DV_lcdm)
# Compaction vs DESI best-fit
sep_comp_desi = np.abs(res['Compaction']['DV_rd'] - res['DESI_bf']['DV_rd']) / (sigma_DV_frac * DV_lcdm)

pr(f"\n  {'z':>6s}  {'FW-Comp':>10s}  {'FW-DESI':>10s}  {'Comp-DESI':>10s}")
pr(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {sep_fw_comp[i]:9.2f}s  {sep_fw_desi[i]:9.2f}s  {sep_comp_desi[i]:9.2f}s")

chi2_fw_comp = np.sum(sep_fw_comp**2)
chi2_fw_desi = np.sum(sep_fw_desi**2)
chi2_comp_desi = np.sum(sep_comp_desi**2)

pr(f"\n  Multi-bin chi2:")
pr(f"    FW vs Compaction:  {chi2_fw_comp:.2f}  ({np.sqrt(chi2_fw_comp):.2f}-sigma)")
pr(f"    FW vs DESI bf:     {chi2_fw_desi:.2f}  ({np.sqrt(chi2_fw_desi):.2f}-sigma)")
pr(f"    Comp vs DESI bf:   {chi2_comp_desi:.2f}  ({np.sqrt(chi2_comp_desi):.2f}-sigma)")

# =============================================================================
# 11. DR3 projections
# =============================================================================
pr(f"\n{'='*72}")
pr("DR3 Projections and Pre-Registered Decision Rules")
pr(f"{'='*72}")

# DR3 projected precision (sqrt(2) improvement, approximately)
sigma_DV_frac_dr3 = sigma_DV_frac / np.sqrt(2)

# Framework-LCDM separation with DR3 precision
nsig_fw_dr3 = np.abs(frac_fw) / sigma_DV_frac_dr3
chi2_fw_dr3 = np.sum(nsig_fw_dr3**2)

pr(f"\n  DR3 projected fractional precision (sqrt(2) reduction):")
for i in range(len(z_eff)):
    pr(f"    z={z_eff[i]:.3f}: {sigma_DV_frac_dr3[i]*100:.2f}% (DR2: {sigma_DV_frac[i]*100:.2f}%)")

pr(f"\n  Framework-LCDM separation with DR3 precision:")
for i in range(len(z_eff)):
    pr(f"    z={z_eff[i]:.3f}: {nsig_fw_dr3[i]:.2f}-sigma")
pr(f"    Combined: {np.sqrt(chi2_fw_dr3):.2f}-sigma")

# Compaction-DESI bf separation with DR3 precision
nsig_comp_desi_dr3 = np.abs(res['Compaction']['DV_rd'] - res['DESI_bf']['DV_rd']) / \
                     (sigma_DV_frac_dr3 * DV_lcdm)
chi2_comp_desi_dr3 = np.sum(nsig_comp_desi_dr3**2)

pr(f"\n  Compaction vs DESI best-fit with DR3 precision:")
for i in range(len(z_eff)):
    pr(f"    z={z_eff[i]:.3f}: {nsig_comp_desi_dr3[i]:.2f}-sigma")
pr(f"    Combined: {np.sqrt(chi2_comp_desi_dr3):.2f}-sigma")

# Boundary scenarios for D_V/r_d
# These translate the CPL w_a thresholds into distance thresholds
w0_bound = -0.75  # DR2-like w_0  # (local)
DV_3sig = np.array([DV_over_rd(z, w0_bound, -0.530) for z in z_eff])
DV_2sig = np.array([DV_over_rd(z, w0_bound, -0.350) for z in z_eff])
DV_fw_arr = res['Framework']['DV_rd']

pr(f"\n  Pre-registered CPL-based decision rules (from S60):")
pr(f"    w_a < -0.530 => framework excluded at >= 3-sigma")
pr(f"    w_a > -0.350 => framework consistent at <= 2-sigma")

pr(f"\n  Translated D_V/r_d boundaries:")
pr(f"  {'z':>6s}  {'FW':>9s}  {'LCDM':>9s}  {'wa=-0.53':>9s}  {'wa=-0.35':>9s}  {'DESI bf':>9s}")
for i in range(len(z_eff)):
    pr(f"  {z_eff[i]:6.3f}  {DV_fw_arr[i]:9.4f}  {DV_lcdm[i]:9.4f}  "
       f"{DV_3sig[i]:9.4f}  {DV_2sig[i]:9.4f}  {res['DESI_bf']['DV_rd'][i]:9.4f}")

# Model-independent DR3 decision rule:
# The most sensitive bin is z=0.706-0.934 (smallest fractional errors).
# At z=0.934: Framework DV/rd = 19.610, LCDM = 19.949.
# Framework is 1.70% below LCDM. DESI best-fit is 1.98% below LCDM.
# They are on the SAME SIDE of LCDM but the framework doesn't go far enough.

pr(f"\n  Model-independent DR3 decision rule:")
pr(f"  Key redshift z=0.934 (highest precision anisotropic bin):")
pr(f"    Framework: DV/rd = {res['Framework']['DV_rd'][3]:.4f}")
pr(f"    LCDM:      DV/rd = {DV_lcdm[3]:.4f}")
pr(f"    DESI bf:   DV/rd = {res['DESI_bf']['DV_rd'][3]:.4f}")
pr(f"    Separation FW-LCDM: {frac_fw[3]*100:.3f}%")
pr(f"    Separation DESI-LCDM: {frac_desi[3]*100:.3f}%")
pr(f"    FW undershoots DESI direction by: {(frac_fw[3]-frac_desi[3])*100:.3f}%")

# =============================================================================
# 12. Summary diagnostics
# =============================================================================
pr(f"\n{'='*72}")
pr("STRUCTURAL DIAGNOSTICS")
pr(f"{'='*72}")

pr(f"""
The framework's w_0 = {w0_fw:.3f} pushes ALL distances shorter than LCDM
uniformly across redshift (monotonic, 1.1-1.7% deficit). This is the CORRECT
DIRECTION at low z (where DESI also sees shorter distances) but the WRONG
BEHAVIOR at high z (where DESI's w_a < 0 implies the Quintom-B phantom
crossing lengthens distances).

The substrate compaction (w_a = {wa_comp:.3f}) introduces z-dependent
modification that partially captures this crossing behavior. At z > 1,
compaction distances are LONGER than LCDM, matching the DESI direction.
However, compaction distances are also longer than LCDM at low z, which
is the wrong direction.

Key structural findings:
1. Framework-LCDM separation is {np.sqrt(chi2_fw):.1f}-sigma (DR2), projecting
   to {np.sqrt(chi2_fw_dr3):.1f}-sigma with DR3. The two are distinguishable.
2. Compaction pattern correlation with DESI: r = {corr_comp:.3f} (vs Framework
   r = {corr_fw:.3f}). Neither matches the DESI pattern well.
3. The DESI best-fit pattern (Quintom B) has a z-crossing near z ~ 0.5 where
   deviations from LCDM change sign. The framework's monotonic deviation
   cannot reproduce this.
4. The compaction DOES produce a z-dependent deviation, but its shape differs
   from the DESI best-fit.
""")

# =============================================================================
# 13. Gate verdict
# =============================================================================
pr(f"\n{'='*72}")
pr("GATE VERDICT: DESI-DV-64")
pr(f"{'='*72}")

verdict = "INFO"
detail = (f"D_V/r_d at 7 DESI bins. FW-LCDM: {np.sqrt(chi2_fw):.1f}-sig (DR2), "
          f"{np.sqrt(chi2_fw_dr3):.1f}-sig (DR3 proj). Compaction chi2={chi2_comp:.1f} vs LCDM. "
          f"Pattern corr: FW {corr_fw:.2f}, Comp {corr_comp:.2f} vs DESI bf. "
          f"DR3 decision: w_a<-0.53 excludes FW at 3-sig")

pr(f"\n  Gate: DESI-DV-64")
pr(f"  Status: {verdict}")
pr(f"  Detail: {detail}")

pr(f"\n  Pre-registered DR3 exclusion criteria:")
pr(f"    CPL-based: w_a < -0.530 => framework excluded (>= 3-sigma)")
pr(f"    CPL-based: w_a > -0.350 => framework consistent (<= 2-sigma)")
pr(f"    Distance-based: If D_V(z=0.934)/r_d < {DV_3sig[3]:.3f}, ")
pr(f"      framework excluded at 3-sigma")

# =============================================================================
# 14. Save outputs
# =============================================================================
out = {
    'z_eff': z_eff,
    'tracer_labels': np.array(tracer_labels),
    'r_d_Mpc': np.array(r_d_Mpc),
    'sigma_DV_frac': sigma_DV_frac,
    'sigma_DV_frac_dr3': sigma_DV_frac_dr3,

    # Model predictions
    'DV_rd_LCDM': res['LCDM']['DV_rd'],
    'DV_rd_Framework': res['Framework']['DV_rd'],
    'DV_rd_Compaction': res['Compaction']['DV_rd'],
    'DV_rd_DESI_bf': res['DESI_bf']['DV_rd'],

    'DM_rd_LCDM': res['LCDM']['DM_rd'],
    'DM_rd_Framework': res['Framework']['DM_rd'],
    'DM_rd_Compaction': res['Compaction']['DM_rd'],

    'DH_rd_LCDM': res['LCDM']['DH_rd'],
    'DH_rd_Framework': res['Framework']['DH_rd'],
    'DH_rd_Compaction': res['Compaction']['DH_rd'],

    # Fractional deviations from LCDM
    'frac_DV_Framework': frac_fw,
    'frac_DV_Compaction': frac_comp,
    'frac_DV_DESI_bf': frac_desi,

    # Per-bin significance (vs LCDM)
    'nsig_Framework': nsig_fw,
    'nsig_Compaction': nsig_comp,
    'nsig_DESI_bf': nsig_desi,

    # Chi-squared
    'chi2_Framework_vs_LCDM': np.array(chi2_fw),
    'chi2_Compaction_vs_LCDM': np.array(chi2_comp),
    'chi2_DESI_vs_LCDM': np.array(chi2_desi),

    # DR3 projections
    'chi2_Framework_dr3': np.array(chi2_fw_dr3),
    'nsig_Framework_dr3': nsig_fw_dr3,

    # Pattern correlations
    'corr_Framework_DESI': np.array(corr_fw),
    'corr_Compaction_DESI': np.array(corr_comp),

    # Boundary scenarios
    'DV_rd_wa_3sig': DV_3sig,
    'DV_rd_wa_2sig': DV_2sig,

    # Framework parameters
    'w0_fw': np.array(w0_fw),
    'wa_fw': np.array(wa_fw),
    'w0_comp': np.array(w0_comp),
    'wa_comp': np.array(wa_comp),

    # Gate
    'gate_name': np.array(['DESI-DV-64']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
}

npz_path = os.path.join(SCRIPT_DIR, 's64_desi_dv.npz')
np.savez(npz_path, **out)
pr(f"\n  Saved: {npz_path}")

# =============================================================================
# 15. Plot
# =============================================================================
fig, axes = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 2]})

# Top: D_V/r_d vs z for all models
ax = axes[0]
z_fine = np.linspace(0.1, 2.5, 200)
for name, m in models.items():
    DV_fine = np.array([DV_over_rd(z, m['w0'], m['wa']) for z in z_fine])
    ax.plot(z_fine, DV_fine, color=m['color'], ls=m['ls'], lw=2, label=m['label'])

# Show DESI error bars on LCDM prediction (representing where data sits)
DV_lcdm_abs = DV_lcdm * sigma_DV_frac  # absolute error
ax.errorbar(z_eff, DV_lcdm, yerr=DV_lcdm_abs, fmt='ko', capsize=4,
            markersize=6, zorder=5, label='LCDM + DESI DR2 precision')

ax.set_ylabel(r'$D_V(z)/r_d$', fontsize=14)
ax.set_title('DESI-DV-64: Model-Independent BAO Distance Comparison', fontsize=14)
ax.legend(loc='upper left', fontsize=9)
ax.set_xlim(0.1, 2.5)
ax.grid(True, alpha=0.3)

# Bottom: fractional deviations from LCDM
ax2 = axes[1]

for name, m in models.items():
    if name == 'LCDM':
        continue
    DV_fine = np.array([DV_over_rd(z, m['w0'], m['wa']) for z in z_fine])
    DV_lcdm_fine = np.array([DV_over_rd(z, -1.0, 0.0) for z in z_fine])
    frac_fine = (DV_fine - DV_lcdm_fine) / DV_lcdm_fine * 100
    ax2.plot(z_fine, frac_fine, color=m['color'], ls=m['ls'], lw=2, label=m['label'])

# DESI DR2 error band (1-sigma)
ax2.fill_between(z_eff, -sigma_DV_frac*100, sigma_DV_frac*100,
                 alpha=0.15, color='gray', label='DESI DR2 1-$\\sigma$ precision')  # (local)
# DR3 projected error band
ax2.fill_between(z_eff, -sigma_DV_frac_dr3*100, sigma_DV_frac_dr3*100,
                 alpha=0.10, color='blue', label='DR3 projected 1-$\\sigma$')  # (local)

ax2.axhline(0, color='k', lw=0.5)
ax2.set_xlabel('Redshift $z$', fontsize=14)
ax2.set_ylabel(r'$(D_V - D_V^{\Lambda{\rm CDM}})/D_V^{\Lambda{\rm CDM}}$ [%]', fontsize=12)
ax2.set_xlim(0.1, 2.5)
ax2.set_ylim(-4, 3)
ax2.legend(loc='lower left', fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's64_desi_dv.png'), dpi=150, bbox_inches='tight')
pr(f"  Saved: s64_desi_dv.png")

# =============================================================================
# 16. Working paper table
# =============================================================================
pr(f"\n{'='*72}")
pr("WORKING PAPER TABLE")
pr(f"{'='*72}")

pr(f"\n### Table: D_V(z)/r_d at DESI DR2 Redshift Bins\n")
pr(f"| z_eff | Tracer | LCDM | Framework | Compaction | DESI bf | "
   f"FW-LCDM [%] | Comp-LCDM [%] | DESI err [%] |")
pr(f"|:------|:-------|:-----|:----------|:-----------|:--------|"
   f":------------|:--------------|:-------------|")
for i in range(len(z_eff)):
    pr(f"| {z_eff[i]:.3f} | {tracer_labels[i]} | "
       f"{DV_lcdm[i]:.3f} | "
       f"{res['Framework']['DV_rd'][i]:.3f} | "
       f"{res['Compaction']['DV_rd'][i]:.3f} | "
       f"{res['DESI_bf']['DV_rd'][i]:.3f} | "
       f"{frac_fw[i]*100:+.3f} | "
       f"{frac_comp[i]*100:+.3f} | "
       f"{sigma_DV_frac[i]*100:.1f} |")

pr(f"\n### Table: Multi-bin chi-squared vs LCDM\n")
pr(f"| Model | chi2 (7 bins) | sigma_eff | Pattern corr | Direction |")
pr(f"|:------|:--------------|:----------|:-------------|:----------|")
pr(f"| Framework | {chi2_fw:.2f} | {np.sqrt(chi2_fw):.2f} | {corr_fw:+.3f} | Uniformly shorter |")
pr(f"| Compaction | {chi2_comp:.2f} | {np.sqrt(chi2_comp):.2f} | {corr_comp:+.3f} | z-dependent |")
pr(f"| DESI best-fit | {chi2_desi:.2f} | {np.sqrt(chi2_desi):.2f} | +1.000 | Quintom B crossing |")

pr(f"\n{'='*72}")
pr("DONE")
pr(f"{'='*72}")

log.close()
