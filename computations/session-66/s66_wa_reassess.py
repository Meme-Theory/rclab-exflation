#!/usr/bin/env python3
"""
s66_wa_reassess.py — WA-REASSESS-66: CPL vs Actual w(z) from Substrate Compaction
==================================================================================
Gate: WA-REASSESS-66
  PASS: Framework w(z) consistent with DESI DR1 at 2 sigma
  FAIL: Inconsistent at > 3 sigma
  INFO: 2-3 sigma, or CPL inadequate (beyond-CPL needed)

Physics:
  S60 derived w_0 = -0.918 from the Volovik combined Josephson+GGE interpretation.
  S59 TIMESCAPE-WA-59 derived w_a = -0.645 from KZ tau-variance between tessellation
  cells: the fiber's Jensen parameter tau varies spatially with local matter density
  (substrate compaction). This creates a Wiltshire-type lapse variance that appears
  as dynamical dark energy.

  The S59 correction to D_H has the form:
    D_H_corrected(z) = D_H_fw(z) * [1 + corr_factor * (1+z)^alpha]
  where corr_factor = f_void * delta_N/N = -0.200, alpha = 0.3.

  This is NOT the CPL form. CPL assumes rho_DE(a) ~ a^{-3(1+w0+wa)} * exp(-3*wa*(1-a)).
  The (1+z)^alpha correction to the lapse is a power law in (1+z), which maps to a
  different w(z) trajectory.

  This computation:
  1. Computes w(z) from the substrate compaction physics at z = {0, 0.5, 1, 1.5, 2, 2.5, 3}
  2. Fits to CPL: w(a) = w_0 + w_a*(1-a). Extracts best-fit w_0 and w_a.
  3. Measures CPL residual: max|w(z) - w_CPL(z)|.
  4. Compares to DESI DR1: w_0 = -0.55 +/- 0.21, w_a = -1.32 +/- 0.70.

  The w(z) from substrate compaction is derived from the effective energy density:
    rho_DE_eff(z) = rho_DE_fw * f(z)
  where f(z) encodes the lapse variance. The effective w(z) is:
    w(z) = -1 + (1+z)/(3*rho_DE_eff) * d(rho_DE_eff)/dz

Author: Katie Mack (Cosmic Bridge)
Session: 66, Task WA-REASSESS-66
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import curve_fit

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    Omega_m, Omega_b, Omega_r, Omega_Lambda,
    H_0_km_s_Mpc, c_light_km_s,
    tau_fold, a2_fold, N_cells, dt_transit, v_terminal,
)

LOGPATH = os.path.join(SCRIPT_DIR, "s66_wa_reassess_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    print(str(msg))
    log.write(str(msg) + "\n")
    log.flush()

pr("=" * 72)
pr("WA-REASSESS-66: CPL vs Actual w(z) from Substrate Compaction")
pr("=" * 72)

# =============================================================================
# 1. Load upstream data
# =============================================================================
Om_m = Omega_m       # 0.315
Om_r = Omega_r       # 9.15e-5
Om_DE = 1.0 - Om_m - Om_r  # ~0.685
H_0 = H_0_km_s_Mpc  # 67.4
h = H_0 / 100.0

pr(f"\nCosmological parameters (Planck 2018):")
pr(f"  Omega_m  = {Om_m}")
pr(f"  Omega_r  = {Om_r}")
pr(f"  Omega_DE = {Om_DE:.6f}")
pr(f"  H_0      = {H_0} km/s/Mpc")

# Load S64 data for cross-reference
try:
    d64 = np.load(os.path.join(SCRIPT_DIR, "s64_desi_dv.npz"), allow_pickle=True)
    w0_fw_s64 = float(d64['w0_fw'])
    wa_fw_s64 = float(d64['wa_fw'])
    w0_comp_s64 = float(d64['w0_comp'])
    wa_comp_s64 = float(d64['wa_comp'])
    pr(f"\nS64 reference values:")
    pr(f"  Pure FW:     w_0={w0_fw_s64:.6f}, w_a={wa_fw_s64:.6f}")
    pr(f"  Compaction:  w_0={w0_comp_s64:.6f}, w_a={wa_comp_s64:.6f}")
except Exception as e:
    pr(f"Warning: Could not load S64: {e}")
    w0_fw_s64 = -0.918  # (local)
    wa_fw_s64 = -0.000575  # (local)
    w0_comp_s64 = -0.924  # (local)
    wa_comp_s64 = -0.645  # (local)

# Load S59 timescape data
try:
    d59 = np.load(os.path.join(SCRIPT_DIR, "s59_timescape_wa.npz"), allow_pickle=True)
    corr_factor_s59 = float(d59['corr_factor'])
    delta_G_over_G = float(d59['delta_G_over_G'])
    sigma_tau_s59 = float(d59['sigma_tau'])
    pr(f"\nS59 timescape parameters:")
    pr(f"  corr_factor = {corr_factor_s59:.6f}")
    pr(f"  delta_G/G   = {delta_G_over_G:.6f}")
    pr(f"  sigma_tau   = {sigma_tau_s59:.6f}")
except Exception as e:
    pr(f"Warning: Could not load S59: {e}")
    corr_factor_s59 = -0.200  # (local)
    delta_G_over_G = -0.526  # (local)
    sigma_tau_s59 = 0.00530  # (local)

# Framework intrinsic w_0
w0_fw = w0_fw_s64  # -0.918 (from Volovik combined Josephson+GGE)

# Substrate compaction parameters from S59 timescape
f_void = 0.76  # Wiltshire 2007  # (local)
alpha_z = 0.3  # Best-fit exponent from S59  # (local)

pr(f"\nSubstrate compaction model:")
pr(f"  w_0 (intrinsic) = {w0_fw:.6f}")
pr(f"  f_void           = {f_void}")
pr(f"  alpha_z          = {alpha_z}")
pr(f"  corr_factor      = {corr_factor_s59:.6f}")

# =============================================================================
# 2. Derive w(z) from substrate compaction physics
# =============================================================================
# The substrate compaction modifies the Hubble rate through a lapse variance:
#   H_eff(z) = H_fw(z) / [1 + eta * (1+z)^alpha]
# where eta = corr_factor = f_void * delta_N/N
#
# This is equivalent to modifying the dark energy density:
#   rho_DE_eff(z) = rho_DE_fw(z) * g(z)
# where g(z) absorbs the lapse correction into an effective DE density.
#
# From the Friedmann equation:
#   H^2(z) = H_0^2 [Om_m*(1+z)^3 + Om_r*(1+z)^4 + Om_DE * rho_DE_eff(z)/rho_DE_0]
#
# For the pure framework with w_0 = -0.918, w_a ~ 0:
#   rho_DE_fw(z)/rho_DE_0 = (1+z)^{3*(1+w0_fw)} = (1+z)^{0.246}
#
# The substrate compaction correction modifies H(z):
#   H_corr(z) = H_fw(z) / [1 + eta*(1+z)^alpha]
# So H_corr^2 = H_fw^2 / [1 + eta*(1+z)^alpha]^2
#
# This means:
#   Om_DE * rho_DE_eff/rho_DE_0 = H_corr^2/H_0^2 - Om_m*(1+z)^3 - Om_r*(1+z)^4

pr(f"\n{'='*72}")
pr("Step 2: Computing w(z) from substrate compaction physics")
pr(f"{'='*72}")

z_eval = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

def E_sq_fw(z):
    """(H_fw/H_0)^2 with constant w = w0_fw"""
    a = 1.0 / (1.0 + z)
    rho_de = a**(-3.0 * (1.0 + w0_fw))  # = (1+z)^{3*(1+w0_fw)}
    return Om_r * (1+z)**4 + Om_m * (1+z)**3 + Om_DE * rho_de

def E_sq_compaction(z):
    """(H_compaction/H_0)^2 including lapse correction"""
    esq_fw = E_sq_fw(z)
    lapse_corr = 1.0 + corr_factor_s59 * (1.0 + z)**alpha_z
    # H_corr = H_fw / lapse_corr, so H_corr^2 = H_fw^2 / lapse_corr^2
    return esq_fw / lapse_corr**2

def rho_DE_eff_over_rho0(z):
    """Effective DE density ratio from compaction-corrected Hubble"""
    esq_comp = E_sq_compaction(z)
    matter_rad = Om_r * (1+z)**4 + Om_m * (1+z)**3
    rho_de_eff = (esq_comp - matter_rad) / Om_DE
    return rho_de_eff

def w_eff_from_rho(z, dz=1e-4):
    """
    Effective equation of state from:
      w(z) = -1 + (1+z)/(3*rho_DE_eff) * d(rho_DE_eff)/dz
    using numerical derivative.
    """
    rho = rho_DE_eff_over_rho0(z)
    rho_p = rho_DE_eff_over_rho0(z + dz)
    rho_m = rho_DE_eff_over_rho0(z - dz) if z > dz else rho_DE_eff_over_rho0(0.0)

    if z > dz:
        drho_dz = (rho_p - rho_m) / (2 * dz)
    else:
        drho_dz = (rho_p - rho) / dz

    if abs(rho) < 1e-30:
        return -1.0

    return -1.0 + (1.0 + z) / (3.0 * rho) * drho_dz

# Compute w(z) at evaluation points
w_z_compaction = np.array([w_eff_from_rho(z) for z in z_eval])

pr(f"\nEffective w(z) from substrate compaction:")
pr(f"  {'z':>5s}  {'w(z)':>10s}  {'rho_DE_eff/rho_0':>16s}")
rho_de_values = np.array([rho_DE_eff_over_rho0(z) for z in z_eval])
for i, z in enumerate(z_eval):
    pr(f"  {z:5.1f}  {w_z_compaction[i]:10.6f}  {rho_de_values[i]:16.6f}")

# =============================================================================
# 3. Fit to CPL: w(a) = w_0 + w_a * (1 - a)
# =============================================================================
pr(f"\n{'='*72}")
pr("Step 3: CPL fit")
pr(f"{'='*72}")

def w_CPL(z, w0, wa):
    a = 1.0 / (1.0 + z)
    return w0 + wa * (1.0 - a)

# Fit using all 7 points
try:
    popt, pcov = curve_fit(w_CPL, z_eval, w_z_compaction, p0=[-0.92, -0.6])
    w0_fit = popt[0]
    wa_fit = popt[1]
    perr = np.sqrt(np.diag(pcov))
    pr(f"\nCPL fit result:")
    pr(f"  w_0 = {w0_fit:.6f} +/- {perr[0]:.6f}")
    pr(f"  w_a = {wa_fit:.6f} +/- {perr[1]:.6f}")
except Exception as e:
    pr(f"CPL fit failed: {e}")
    w0_fit = w0_fw
    wa_fit = 0.0  # (local)
    perr = np.array([0, 0])

# Compute CPL prediction at evaluation points
w_CPL_values = w_CPL(z_eval, w0_fit, wa_fit)

# =============================================================================
# 4. CPL residual analysis
# =============================================================================
pr(f"\n{'='*72}")
pr("Step 4: CPL residual")
pr(f"{'='*72}")

residual = w_z_compaction - w_CPL_values
max_residual = np.max(np.abs(residual))
rms_residual = np.sqrt(np.mean(residual**2))

pr(f"\n  {'z':>5s}  {'w(z)':>10s}  {'w_CPL(z)':>10s}  {'Residual':>10s}")
for i, z in enumerate(z_eval):
    pr(f"  {z:5.1f}  {w_z_compaction[i]:10.6f}  {w_CPL_values[i]:10.6f}  {residual[i]:10.6f}")

pr(f"\n  Max |residual| = {max_residual:.6f}")
pr(f"  RMS residual   = {rms_residual:.6f}")

if max_residual < 0.01:
    cpl_verdict = "ADEQUATE"
    pr(f"\n  CPL verdict: ADEQUATE (max residual {max_residual:.4f} < 0.01)")
elif max_residual > 0.05:
    cpl_verdict = "BEYOND-CPL"
    pr(f"\n  CPL verdict: BEYOND-CPL NEEDED (max residual {max_residual:.4f} > 0.05)")
else:
    cpl_verdict = "MARGINAL"
    pr(f"\n  CPL verdict: MARGINAL (0.01 < max residual {max_residual:.4f} < 0.05)")

# =============================================================================
# 5. Also compute w(z) for pure framework (no compaction)
# =============================================================================
pr(f"\n{'='*72}")
pr("Step 5: Pure framework w(z) for comparison")
pr(f"{'='*72}")

# Pure framework: constant w = w0_fw (w_a ~ 0)
w_z_pure = np.full_like(z_eval, w0_fw)

pr(f"\n  Pure framework: w(z) = {w0_fw:.6f} (constant)")
pr(f"  This is a CPL model with w_0={w0_fw:.6f}, w_a=0.0")

# =============================================================================
# 6. Comparison with DESI DR1
# =============================================================================
pr(f"\n{'='*72}")
pr("Step 6: DESI DR1 comparison")
pr(f"{'='*72}")

# DESI DR1 constraints (BAO + CMB + SNe Ia)
desi_dr1_w0 = -0.55  # (local)
desi_dr1_w0_err = 0.21  # (local)
desi_dr1_wa = -1.32  # (local)
desi_dr1_wa_err = 0.70  # (local)

# Also include DESI DR2 for completeness
desi_dr2_w0 = -0.752  # (local)
desi_dr2_w0_err = 0.057  # (local)
desi_dr2_wa = -0.73  # (local)
desi_dr2_wa_err = 0.25  # (local)

pr(f"\nDESI DR1 (BAO+CMB+SNe): w_0 = {desi_dr1_w0} +/- {desi_dr1_w0_err}, w_a = {desi_dr1_wa} +/- {desi_dr1_wa_err}")
pr(f"DESI DR2 (BAO+CMB+SNe): w_0 = {desi_dr2_w0} +/- {desi_dr2_w0_err}, w_a = {desi_dr2_wa} +/- {desi_dr2_wa_err}")

# --- Model A: Pure framework (w_0=-0.918, w_a~0) ---
delta_w0_A_dr1 = w0_fw - desi_dr1_w0
delta_wa_A_dr1 = 0.0 - desi_dr1_wa
nsig_w0_A_dr1 = abs(delta_w0_A_dr1) / desi_dr1_w0_err
nsig_wa_A_dr1 = abs(delta_wa_A_dr1) / desi_dr1_wa_err

# 2D tension: (Delta/sigma)^T * Sigma^{-1} * (Delta/sigma) for diagonal covariance
# For uncorrelated: sqrt(nsig_w0^2 + nsig_wa^2)
nsig_2d_A_dr1 = np.sqrt(nsig_w0_A_dr1**2 + nsig_wa_A_dr1**2)

pr(f"\n--- Model A: Pure Framework (w_0={w0_fw:.3f}, w_a=0.000) ---")
pr(f"  vs DESI DR1:")
pr(f"    Delta w_0 = {delta_w0_A_dr1:+.3f} ({nsig_w0_A_dr1:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_A_dr1:+.3f} ({nsig_wa_A_dr1:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_A_dr1:.2f} sigma")

delta_w0_A_dr2 = w0_fw - desi_dr2_w0
delta_wa_A_dr2 = 0.0 - desi_dr2_wa
nsig_w0_A_dr2 = abs(delta_w0_A_dr2) / desi_dr2_w0_err
nsig_wa_A_dr2 = abs(delta_wa_A_dr2) / desi_dr2_wa_err
nsig_2d_A_dr2 = np.sqrt(nsig_w0_A_dr2**2 + nsig_wa_A_dr2**2)

pr(f"  vs DESI DR2:")
pr(f"    Delta w_0 = {delta_w0_A_dr2:+.3f} ({nsig_w0_A_dr2:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_A_dr2:+.3f} ({nsig_wa_A_dr2:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_A_dr2:.2f} sigma")

# --- Model B: Compaction CPL fit ---
delta_w0_B_dr1 = w0_fit - desi_dr1_w0
delta_wa_B_dr1 = wa_fit - desi_dr1_wa
nsig_w0_B_dr1 = abs(delta_w0_B_dr1) / desi_dr1_w0_err
nsig_wa_B_dr1 = abs(delta_wa_B_dr1) / desi_dr1_wa_err
nsig_2d_B_dr1 = np.sqrt(nsig_w0_B_dr1**2 + nsig_wa_B_dr1**2)

pr(f"\n--- Model B: Substrate Compaction CPL fit (w_0={w0_fit:.3f}, w_a={wa_fit:.3f}) ---")
pr(f"  vs DESI DR1:")
pr(f"    Delta w_0 = {delta_w0_B_dr1:+.3f} ({nsig_w0_B_dr1:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_B_dr1:+.3f} ({nsig_wa_B_dr1:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_B_dr1:.2f} sigma")

delta_w0_B_dr2 = w0_fit - desi_dr2_w0
delta_wa_B_dr2 = wa_fit - desi_dr2_wa
nsig_w0_B_dr2 = abs(delta_w0_B_dr2) / desi_dr2_w0_err
nsig_wa_B_dr2 = abs(delta_wa_B_dr2) / desi_dr2_wa_err
nsig_2d_B_dr2 = np.sqrt(nsig_w0_B_dr2**2 + nsig_wa_B_dr2**2)

pr(f"  vs DESI DR2:")
pr(f"    Delta w_0 = {delta_w0_B_dr2:+.3f} ({nsig_w0_B_dr2:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_B_dr2:+.3f} ({nsig_wa_B_dr2:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_B_dr2:.2f} sigma")

# --- LCDM reference ---
delta_w0_L_dr1 = -1.0 - desi_dr1_w0
delta_wa_L_dr1 = 0.0 - desi_dr1_wa
nsig_w0_L_dr1 = abs(delta_w0_L_dr1) / desi_dr1_w0_err
nsig_wa_L_dr1 = abs(delta_wa_L_dr1) / desi_dr1_wa_err
nsig_2d_L_dr1 = np.sqrt(nsig_w0_L_dr1**2 + nsig_wa_L_dr1**2)

pr(f"\n--- Reference: LCDM (w_0=-1.000, w_a=0.000) ---")
pr(f"  vs DESI DR1:")
pr(f"    Delta w_0 = {delta_w0_L_dr1:+.3f} ({nsig_w0_L_dr1:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_L_dr1:+.3f} ({nsig_wa_L_dr1:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_L_dr1:.2f} sigma")

delta_w0_L_dr2 = -1.0 - desi_dr2_w0
delta_wa_L_dr2 = 0.0 - desi_dr2_wa
nsig_w0_L_dr2 = abs(delta_w0_L_dr2) / desi_dr2_w0_err
nsig_wa_L_dr2 = abs(delta_wa_L_dr2) / desi_dr2_wa_err
nsig_2d_L_dr2 = np.sqrt(nsig_w0_L_dr2**2 + nsig_wa_L_dr2**2)

pr(f"  vs DESI DR2:")
pr(f"    Delta w_0 = {delta_w0_L_dr2:+.3f} ({nsig_w0_L_dr2:.2f} sigma)")
pr(f"    Delta w_a = {delta_wa_L_dr2:+.3f} ({nsig_wa_L_dr2:.2f} sigma)")
pr(f"    2D tension = {nsig_2d_L_dr2:.2f} sigma")

# =============================================================================
# 7. Finer w(z) curve for residual analysis and plotting
# =============================================================================
z_fine = np.linspace(0.0, 3.0, 301)
w_fine_compaction = np.array([w_eff_from_rho(z) for z in z_fine])
w_fine_CPL = w_CPL(z_fine, w0_fit, wa_fit)
w_fine_pure = np.full_like(z_fine, w0_fw)
w_fine_LCDM = np.full_like(z_fine, -1.0)
w_fine_dr1 = w_CPL(z_fine, desi_dr1_w0, desi_dr1_wa)
w_fine_dr2 = w_CPL(z_fine, desi_dr2_w0, desi_dr2_wa)

# Fine residual
residual_fine = w_fine_compaction - w_fine_CPL
max_residual_fine = np.max(np.abs(residual_fine))

pr(f"\n{'='*72}")
pr("Fine-grained residual analysis (301 points, z in [0, 3])")
pr(f"{'='*72}")
pr(f"  Max |residual| (fine) = {max_residual_fine:.6f}")

# =============================================================================
# 8. Structural analysis: why CPL fits or doesn't
# =============================================================================
pr(f"\n{'='*72}")
pr("Step 8: Structural analysis")
pr(f"{'='*72}")

# The substrate compaction correction has the form:
#   H_corr(z) = H_fw(z) / [1 + eta*(1+z)^alpha]
# For small eta, this is approximately:
#   H_corr(z) ~ H_fw(z) * [1 - eta*(1+z)^alpha]
# The effective DE density becomes:
#   rho_DE_eff(z) ~ rho_DE_fw(z) - 2*eta*(1+z)^alpha * [H_fw(z)/H_0]^2 * Om_DE
# This is NOT a simple power-law in (1+z), so it departs from CPL.

# The key physics: the substrate's lapse correction is a power law in (1+z),
# but DE energy density is already a power law. Adding these creates a
# mixed functional form that CPL can only approximate.

# Check: how does w(z) evolve with z?
dw_dz_at_0 = (w_z_compaction[1] - w_z_compaction[0]) / (z_eval[1] - z_eval[0])
dw_dz_at_1 = (w_z_compaction[3] - w_z_compaction[1]) / (z_eval[3] - z_eval[1])
dw_dz_at_2 = (w_z_compaction[5] - w_z_compaction[3]) / (z_eval[5] - z_eval[3])

pr(f"\n  dw/dz at z~0:   {dw_dz_at_0:.6f}")
pr(f"  dw/dz at z~1:   {dw_dz_at_1:.6f}")
pr(f"  dw/dz at z~2:   {dw_dz_at_2:.6f}")

# CPL predicts dw/dz = wa/(1+z)^2 = constant w_a at z=0
dw_dz_CPL_0 = wa_fit
pr(f"  CPL dw/dz at z=0: {dw_dz_CPL_0:.6f}")
pr(f"  Mismatch at z=0: {abs(dw_dz_at_0 - dw_dz_CPL_0):.6f}")

# Check if w(z) crosses w=-1 (phantom crossing)
w_at_z0 = w_z_compaction[0]
w_at_z3 = w_z_compaction[-1]
crosses_phantom = (w_at_z0 + 1) * (w_at_z3 + 1) < 0

pr(f"\n  w(z=0) = {w_at_z0:.6f}")
pr(f"  w(z=3) = {w_at_z3:.6f}")
pr(f"  Phantom crossing (w crosses -1): {crosses_phantom}")
if crosses_phantom:
    # Find crossing redshift
    for i in range(len(z_fine) - 1):
        if (w_fine_compaction[i] + 1) * (w_fine_compaction[i+1] + 1) < 0:
            z_cross = z_fine[i] + (z_fine[i+1] - z_fine[i]) * abs(w_fine_compaction[i] + 1) / abs(w_fine_compaction[i+1] - w_fine_compaction[i])
            pr(f"  Phantom crossing at z = {z_cross:.3f}")
            break

# =============================================================================
# 9. Gate verdict
# =============================================================================
pr(f"\n{'='*72}")
pr("GATE VERDICT: WA-REASSESS-66")
pr(f"{'='*72}")

# Primary gate: DESI DR1 comparison (as specified in task)
# Use 2D tension for the compaction model
nsig_gate = nsig_2d_B_dr1

pr(f"\n  Framework w(z) from substrate compaction:")
pr(f"    CPL best-fit: w_0 = {w0_fit:.4f}, w_a = {wa_fit:.4f}")
pr(f"    Max CPL residual: {max_residual:.4f} (fine: {max_residual_fine:.4f})")
pr(f"    CPL adequacy: {cpl_verdict}")
pr(f"  DESI DR1 comparison (2D): {nsig_gate:.2f} sigma")
pr(f"  DESI DR2 comparison (2D): {nsig_2d_B_dr2:.2f} sigma")

if nsig_gate <= 2.0:
    verdict = "PASS"
    detail = f"Compaction CPL (w_0={w0_fit:.3f}, w_a={wa_fit:.3f}) at {nsig_gate:.2f}-sigma from DESI DR1 (<= 2)"
elif nsig_gate > 3.0:
    verdict = "FAIL"
    detail = f"Compaction CPL (w_0={w0_fit:.3f}, w_a={wa_fit:.3f}) at {nsig_gate:.2f}-sigma from DESI DR1 (> 3)"
else:
    verdict = "INFO"
    detail = f"Compaction CPL (w_0={w0_fit:.3f}, w_a={wa_fit:.3f}) at {nsig_gate:.2f}-sigma from DESI DR1 (2-3)"

if cpl_verdict != "ADEQUATE":
    verdict = "INFO"
    detail += f"; CPL {cpl_verdict} (residual {max_residual_fine:.4f})"

pr(f"\n  Gate WA-REASSESS-66: {verdict}")
pr(f"  Detail: {detail}")

# =============================================================================
# 10. Summary table
# =============================================================================
pr(f"\n{'='*72}")
pr("SUMMARY TABLE")
pr(f"{'='*72}")
pr(f"\n{'Model':<25s} {'w_0':>8s} {'w_a':>8s} {'DR1 2D-sig':>10s} {'DR2 2D-sig':>10s}")
pr(f"{'-'*25} {'-'*8} {'-'*8} {'-'*10} {'-'*10}")
pr(f"{'Pure FW':<25s} {w0_fw:8.3f} {'0.000':>8s} {nsig_2d_A_dr1:10.2f} {nsig_2d_A_dr2:10.2f}")
pr(f"{'Compaction (CPL fit)':<25s} {w0_fit:8.3f} {wa_fit:8.3f} {nsig_2d_B_dr1:10.2f} {nsig_2d_B_dr2:10.2f}")
pr(f"{'LCDM':<25s} {'-1.000':>8s} {'0.000':>8s} {nsig_2d_L_dr1:10.2f} {nsig_2d_L_dr2:10.2f}")
pr(f"{'DESI DR1 bf':<25s} {desi_dr1_w0:8.3f} {desi_dr1_wa:8.3f} {'---':>10s} {'---':>10s}")
pr(f"{'DESI DR2 bf':<25s} {desi_dr2_w0:8.3f} {desi_dr2_wa:8.3f} {'---':>10s} {'---':>10s}")

# =============================================================================
# 11. Save data
# =============================================================================
outpath = os.path.join(SCRIPT_DIR, "s66_wa_reassess.npz")
np.savez(outpath,
    # Evaluation grid
    z_eval=z_eval,
    w_z_compaction=w_z_compaction,
    w_CPL_values=w_CPL_values,
    rho_de_values=rho_de_values,
    residual=residual,
    # CPL fit
    w0_fit=np.array(w0_fit),
    wa_fit=np.array(wa_fit),
    w0_fit_err=np.array(perr[0]),
    wa_fit_err=np.array(perr[1]),
    max_residual=np.array(max_residual),
    max_residual_fine=np.array(max_residual_fine),
    rms_residual=np.array(rms_residual),
    cpl_verdict=np.array([cpl_verdict]),
    # Fine curves
    z_fine=z_fine,
    w_fine_compaction=w_fine_compaction,
    w_fine_CPL=w_fine_CPL,
    w_fine_pure=w_fine_pure,
    w_fine_LCDM=w_fine_LCDM,
    w_fine_dr1=w_fine_dr1,
    w_fine_dr2=w_fine_dr2,
    residual_fine=residual_fine,
    # DESI comparison
    nsig_2d_A_dr1=np.array(nsig_2d_A_dr1),
    nsig_2d_A_dr2=np.array(nsig_2d_A_dr2),
    nsig_2d_B_dr1=np.array(nsig_2d_B_dr1),
    nsig_2d_B_dr2=np.array(nsig_2d_B_dr2),
    nsig_2d_L_dr1=np.array(nsig_2d_L_dr1),
    nsig_2d_L_dr2=np.array(nsig_2d_L_dr2),
    # Pure FW reference
    w0_fw=np.array(w0_fw),
    # Structural
    dw_dz_at_0=np.array(dw_dz_at_0),
    dw_dz_at_1=np.array(dw_dz_at_1),
    dw_dz_at_2=np.array(dw_dz_at_2),
    # Gate
    gate_name=np.array(["WA-REASSESS-66"]),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
pr(f"\nData saved: {outpath}")

# =============================================================================
# 12. Plot
# =============================================================================
figpath = os.path.join(SCRIPT_DIR, "s66_wa_reassess.png")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: w(z) trajectories
ax = axes[0, 0]
ax.plot(z_fine, w_fine_LCDM, 'k--', lw=1.5, label=r'$\Lambda$CDM ($w=-1$)')
ax.plot(z_fine, w_fine_pure, 'b-', lw=1.5, label=f'Pure FW ($w_0$={w0_fw:.3f})')
ax.plot(z_fine, w_fine_compaction, 'r-', lw=2, label='Substrate compaction')
ax.plot(z_fine, w_fine_CPL, 'r--', lw=1.5, alpha=0.7, label=f'CPL fit ($w_0$={w0_fit:.3f}, $w_a$={wa_fit:.3f})')
ax.plot(z_fine, w_fine_dr1, 'g-.', lw=1.5, alpha=0.7, label=f'DESI DR1 ($w_0$={desi_dr1_w0}, $w_a$={desi_dr1_wa})')
ax.plot(z_fine, w_fine_dr2, 'm:', lw=1.5, alpha=0.7, label=f'DESI DR2 ($w_0$={desi_dr2_w0}, $w_a$={desi_dr2_wa})')
ax.scatter(z_eval, w_z_compaction, c='red', s=40, zorder=5, marker='o')
ax.axhline(-1, color='gray', lw=0.5, ls=':')
ax.set_xlabel('Redshift z')
ax.set_ylabel('w(z)')
ax.set_title('Dark Energy Equation of State')
ax.legend(fontsize=7, loc='best')
ax.set_xlim(0, 3)

# Panel B: CPL residual
ax = axes[0, 1]
ax.plot(z_fine, residual_fine, 'r-', lw=2)
ax.axhline(0, color='k', lw=0.5)
ax.axhline(0.01, color='green', ls='--', alpha=0.5, label='CPL adequate (<0.01)')
ax.axhline(-0.01, color='green', ls='--', alpha=0.5)
ax.axhline(0.05, color='orange', ls='--', alpha=0.5, label='Beyond-CPL (>0.05)')
ax.axhline(-0.05, color='orange', ls='--', alpha=0.5)
ax.fill_between(z_fine, -0.01, 0.01, alpha=0.1, color='green')
ax.set_xlabel('Redshift z')
ax.set_ylabel(r'$w_{\rm comp}(z) - w_{\rm CPL}(z)$')
ax.set_title(f'CPL Residual (max={max_residual_fine:.4f})')
ax.legend(fontsize=8)
ax.set_xlim(0, 3)

# Panel C: rho_DE_eff/rho_0
ax = axes[1, 0]
rho_fine_comp = np.array([rho_DE_eff_over_rho0(z) for z in z_fine])
a_fine = 1.0 / (1.0 + z_fine)
rho_fine_fw = a_fine**(-3.0 * (1.0 + w0_fw))
rho_fine_LCDM = np.ones_like(z_fine)
rho_fine_CPL_fit = a_fine**(-3.0 * (1.0 + w0_fit + wa_fit)) * np.exp(-3.0 * wa_fit * (1.0 - a_fine))

ax.plot(z_fine, rho_fine_LCDM, 'k--', lw=1.5, label=r'$\Lambda$CDM')
ax.plot(z_fine, rho_fine_fw, 'b-', lw=1.5, label='Pure FW')
ax.plot(z_fine, rho_fine_comp, 'r-', lw=2, label='Substrate compaction')
ax.plot(z_fine, rho_fine_CPL_fit, 'r--', lw=1.5, alpha=0.7, label='CPL fit')
ax.set_xlabel('Redshift z')
ax.set_ylabel(r'$\rho_{\rm DE}(z) / \rho_{\rm DE}(0)$')
ax.set_title('Effective DE Energy Density')
ax.legend(fontsize=8)
ax.set_xlim(0, 3)

# Panel D: Summary text
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"WA-REASSESS-66: Gate {verdict}\n"
    f"{'='*45}\n\n"
    f"Substrate compaction w(z):\n"
    f"  w(z=0) = {w_z_compaction[0]:.4f}\n"
    f"  w(z=1) = {w_z_compaction[2]:.4f}\n"
    f"  w(z=3) = {w_z_compaction[-1]:.4f}\n\n"
    f"CPL fit:  w_0 = {w0_fit:.4f}, w_a = {wa_fit:.4f}\n"
    f"Max |residual| = {max_residual_fine:.4f}\n"
    f"CPL adequacy: {cpl_verdict}\n\n"
    f"DESI DR1 comparison (2D):\n"
    f"  Pure FW:       {nsig_2d_A_dr1:.2f}-sigma\n"
    f"  Compaction:    {nsig_2d_B_dr1:.2f}-sigma\n"
    f"  LCDM:          {nsig_2d_L_dr1:.2f}-sigma\n\n"
    f"DESI DR2 comparison (2D):\n"
    f"  Pure FW:       {nsig_2d_A_dr2:.2f}-sigma\n"
    f"  Compaction:    {nsig_2d_B_dr2:.2f}-sigma\n"
    f"  LCDM:          {nsig_2d_L_dr2:.2f}-sigma\n"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle('WA-REASSESS-66: CPL vs Substrate Compaction w(z)', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(figpath, dpi=150, bbox_inches='tight')
pr(f"Plot saved: {figpath}")

log.close()
print(f"\nDone. Log: {LOGPATH}")
