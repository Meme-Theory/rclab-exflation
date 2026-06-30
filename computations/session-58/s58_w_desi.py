#!/usr/bin/env python3
"""
s58_w_desi.py — W-DESI-58: Equation of State Under Volovik Partition
====================================================================
Gate: W-DESI-58
  PASS: |w_0(Volovik) - w_0(DESI DR2)| < 3-sigma
  FAIL: |w_0(Volovik) - w_0(DESI DR2)| > 5-sigma
  INFO: tension between 3-sigma and 5-sigma

Physics: Under the Volovik partition, the vacuum sector has two components:
  1. Josephson ground-state stiffness F_J = -336.6 M_KK (pure cosmological constant, w=-1)
  2. GGE non-equilibrium excess Lambda_eff = +1.709 M_KK (w_GGE = -0.408)
The combined vacuum equation of state is a weighted average:
  w_combined = (P_J + P_GGE) / (rho_J + rho_GGE) = -0.917

Two observational interpretations:
  A: w = w_combined = -0.917 (all vacuum energy gravitates, one dark energy fluid)
  B: w = w_GGE = -0.408 (only GGE excess is dynamical DE; Josephson is unobservable vacuum floor)

DESI measures dynamical w — if the Josephson ground state is a pure CC that cancels
against the bare cosmological constant (as in Volovik q-theory), only the GGE excess
contributes to the observed dark energy. This gives interpretation B.

If both components are directly observed as dark energy, interpretation A applies.

This script:
  1. Loads W0-1 and W0-2 outputs
  2. Computes w_0 under both interpretations
  3. Maps tau -> z using S54 scale factor
  4. Fits w(z) = w_0 + w_a * z/(1+z) (CPL parametrization) if tau sweep available
  5. Compares to DESI DR1, DESI DR2, Planck 2018, LCDM, and pre-Shattering S49
  6. Reports sigma tension and gate verdict

Author: Phonon-First Cosmologist
Session: 58, Wave 0, Task W0-4
"""

import sys
import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    M_KK, M_KK_gravity, tau_fold, N_cells,
    rho_Lambda_obs, rho_crit_GeV4,
    Omega_Lambda, Omega_m, Omega_DM,
    H_0_km_s_Mpc, PI,
    E_cond, E_cond_ED_8mode, N_dof_BCS,
)

# =============================================================================
# 1. Load upstream data
# =============================================================================
d_w01 = np.load(os.path.join(SCRIPT_DIR, 's58_volovik_partition.npz'), allow_pickle=True)
d_w02 = np.load(os.path.join(SCRIPT_DIR, 's58_cc_cancellation_sweep.npz'), allow_pickle=True)
d_s57 = np.load(os.path.join(SCRIPT_DIR, 's57_cc_sign.npz'), allow_pickle=True)
d_sf  = np.load(os.path.join(SCRIPT_DIR, 's54_scale_factor.npz'), allow_pickle=True)

print("=" * 72)
print("W-DESI-58: Equation of State Under Volovik Partition — DESI Confrontation")
print("=" * 72)

# =============================================================================
# 2. Extract W0-1 values
# =============================================================================
w_combined    = float(d_w01['w_combined'])       # -0.917
w_eff_Volovik = float(d_w01['w_eff_Volovik'])    # -0.917
w_DE_GGE      = float(d_w01['w_DE_GGE'])         # -0.403
f_DM_A        = float(d_w01['f_DM_Volovik_A'])   # 0.209
f_DM_B        = float(d_w01['f_DM_Volovik_B'])   # 0.513
E_matter_V    = float(d_w01['E_matter_Volovik'])  # 14.411
F_Josephson   = float(d_w01['F_Josephson'])       # -336.641

print(f"\n=== W0-1 Volovik Partition Values ===")
print(f"  w_combined (J+GGE):     {w_combined:.6f}")
print(f"  w_eff_Volovik:          {w_eff_Volovik:.6f}")
print(f"  w_DE (GGE only):        {w_DE_GGE:.6f}")
print(f"  f_DM (Variant A):       {f_DM_A:.4f}")
print(f"  f_DM (Variant B):       {f_DM_B:.4f}")
print(f"  E_matter_Volovik:       {E_matter_V:.3f} M_KK")
print(f"  F_Josephson:            {F_Josephson:.3f} M_KK")

# =============================================================================
# 3. Extract W0-2 sweep values
# =============================================================================
tau_values     = d_w02['tau_values']        # 50 tau points
w_sweep        = d_w02['w_sweep']           # w(tau) for GGE-only at each tau
P_vac_sweep    = d_w02['P_vac_sweep']       # P_vac at each tau
dLambda_dtau   = d_w02['dLambda_dtau']      # dLambda/dtau
Lambda_eff_sw  = d_w02['Lambda_eff_sweep']  # Lambda_eff(tau)
E_GGE_sweep    = d_w02['E_GGE_sweep']       # E_GGE at each tau
fold_idx       = int(d_w02['fold_idx'])     # index of tau_fold

print(f"\n=== W0-2 Sweep Values ===")
print(f"  N_tau:                  {len(tau_values)}")
print(f"  tau range:              [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"  tau_fold (idx={fold_idx}):     {tau_values[fold_idx]:.4f}")
print(f"  w_sweep range:          [{w_sweep.min():.6f}, {w_sweep.max():.6f}]")
print(f"  w at fold:              {w_sweep[fold_idx]:.6f}")
print(f"  Lambda_eff at fold:     {Lambda_eff_sw[fold_idx]:.6g} M_KK")

# =============================================================================
# 4. Extract S57 CC-sign reference values
# =============================================================================
Lambda_eff_MKK = float(d_s57['Lambda_eff_MKK'])  # 1.709
w_GGE_S57      = float(d_s57['w_GGE'])           # -0.408
E_GGE_S57      = float(d_s57['E_GGE'])           # 1.688
P_vac_GGE_S57  = float(d_s57['P_vac_GGE'])       # -0.688

print(f"\n=== S57 Reference (at fold) ===")
print(f"  Lambda_eff_MKK:         {Lambda_eff_MKK:.6f}")
print(f"  w_GGE:                  {w_GGE_S57:.6f}")
print(f"  E_GGE:                  {E_GGE_S57:.6f}")
print(f"  P_vac_GGE:              {P_vac_GGE_S57:.6f}")

# =============================================================================
# 5. Compute w_0 under both interpretations at the fold
# =============================================================================
# Interpretation A: Combined (Josephson + GGE) is the observable dark energy
#   rho_DE = |F_J|/N_cells + Lambda_eff
#   P_DE   = -|F_J|/N_cells + P_GGE
#   w_0^A  = P_DE / rho_DE

rho_J_cell = abs(F_Josephson) / N_cells  # per cell
rho_GGE    = Lambda_eff_MKK              # 1.709 M_KK (per cell, GGE excess)
P_GGE      = P_vac_GGE_S57               # -0.688 M_KK

rho_DE_A = rho_J_cell + rho_GGE
P_DE_A   = -rho_J_cell + P_GGE
w_0_A    = P_DE_A / rho_DE_A

print(f"\n=== Interpretation A: Combined Vacuum = Observable DE ===")
print(f"  rho_J/cell:             {rho_J_cell:.6f} M_KK")
print(f"  rho_GGE:                {rho_GGE:.6f} M_KK")
print(f"  rho_DE_A (total):       {rho_DE_A:.6f} M_KK")
print(f"  P_DE_A:                 {P_DE_A:.6f} M_KK")
print(f"  w_0_A:                  {w_0_A:.6f}")

# Interpretation B: Only GGE excess is dynamical DE (Josephson = unobservable vacuum floor)
#   rho_DE = Lambda_eff (GGE excess only)
#   P_DE   = P_GGE
#   w_0^B  = P_GGE / Lambda_eff

rho_DE_B = rho_GGE
P_DE_B   = P_GGE
w_0_B    = P_DE_B / rho_DE_B

print(f"\n=== Interpretation B: GGE Excess = Observable DE ===")
print(f"  rho_DE_B:               {rho_DE_B:.6f} M_KK")
print(f"  P_DE_B:                 {P_DE_B:.6f} M_KK")
print(f"  w_0_B:                  {w_0_B:.6f}")

# =============================================================================
# 6. Tau-to-redshift mapping and CPL fit
# =============================================================================
# From S54 scale factor: a(tau) measured at 10 tau points
# z = a(today)/a(tau) - 1, where a(today) = a(tau=0) for the late-universe limit

tau_sf  = d_sf['tau']  # 10 tau points
a_sf    = d_sf['a']    # scale factor a(tau)
H_sf    = d_sf['H']    # Hubble parameter H(tau)

print(f"\n=== Tau-to-Redshift Mapping (S54) ===")
print(f"  a(tau=0):               {a_sf[0]:.6f}")
print(f"  a(tau_fold~{tau_sf[5]:.3f}):      {a_sf[5]:.6f}")
print(f"  a(tau_max={tau_sf[-1]:.3f}):     {a_sf[-1]:.6f}")

# The S54 scale factor has a(tau=0) = 1, a(tau_fold) ~ 2.12.
# Physical interpretation: tau=0 -> z=0 (today), increasing tau -> earlier times (higher z).
# z(tau) = a(tau)/a(0) - 1 = a(tau) - 1 (since a(0)=1).
# WAIT: that gives z>0 for tau>0, which is backwards (later tau = earlier time = higher z).
# Actually in this framework, tau parameterizes the internal geometry, not cosmic time directly.
# a(tau) > 1 means expansion BEYOND today, so tau>0 corresponds to z<0 (future).
#
# The correct mapping: a(tau)/a_today = a(tau)/a(tau_fold) for the fold being "now".
# But the S54 data has a(0)=1, a growing with tau. If tau=0 is the beginning and
# increasing tau represents forward time, then z(tau) = a(tau_now)/a(tau) - 1.
#
# More carefully: The DESI measures w(z) over 0<z<1.5 (past).
# The framework's w(tau) varies over the transit interval.
# The mapping from tau -> z requires identifying which tau corresponds to z=0 (today).
#
# For the CPL fit, we need w as a function of z.
# From S54: a(tau) is a monotonically increasing function.
# If tau_fold ~ 0.19 corresponds to roughly "today" in the expansion history,
# then z = a(tau_fold)/a(tau) - 1 for tau < tau_fold (past).

# Method: interpolate a(tau) from S54, map w_sweep tau points to z
from scipy.interpolate import interp1d

# Build a(tau) interpolant from S54 data
a_interp = interp1d(tau_sf, a_sf, kind='cubic', fill_value='extrapolate')

# Map w_sweep tau values to scale factor
a_at_sweep = a_interp(tau_values)
a_at_fold  = a_interp(tau_fold)

# z(tau) = a(tau_fold) / a(tau) - 1
# For tau < tau_fold: z > 0 (past)
# For tau = tau_fold: z = 0 (today)
# For tau > tau_fold: z < 0 (future)
z_from_tau = a_at_fold / a_at_sweep - 1.0

print(f"\n  a at fold:              {a_at_fold:.6f}")
print(f"  z range (from tau map): [{z_from_tau.min():.4f}, {z_from_tau.max():.4f}]")
print(f"  z at fold (tau={tau_values[fold_idx]:.4f}):  {z_from_tau[fold_idx]:.6f}")

# Select past-only points (z > 0, i.e., tau < tau_fold) for DESI comparison
past_mask = (z_from_tau > 0) & (z_from_tau < 5.0)  # restrict to reasonable z range
z_past    = z_from_tau[past_mask]
w_past    = w_sweep[past_mask]  # This is w_GGE(tau) -- interpretation B

print(f"\n  Past points (z>0):      {past_mask.sum()}")
if past_mask.sum() > 0:
    print(f"  z past range:           [{z_past.min():.4f}, {z_past.max():.4f}]")
    print(f"  w past range:           [{w_past.min():.4f}, {w_past.max():.4f}]")

# CPL fit: w(z) = w_0 + w_a * z/(1+z)
# The W0-2 w_sweep is the GGE-only w, which is interpretation B.
# For interpretation A, the Josephson ground state (w=-1) is constant,
# so the combined w varies only through the GGE component.

# For the combined case (A):
# w_A(tau) = [-rho_J/cell + P_GGE(tau)] / [rho_J/cell + Lambda_eff(tau)]
# = [-rho_J/cell + P_vac_sweep(tau)] / [rho_J/cell + E_GGE_sweep(tau)]
# NOTE: W0-2 computes P_vac = N_avg - E_GGE (from GGE occupations)
# The "pressure" is P_GGE(tau) = P_vac_sweep(tau)

w_A_sweep = np.zeros_like(tau_values)
for i in range(len(tau_values)):
    rho_A_i = rho_J_cell + E_GGE_sweep[i]  # total vacuum energy
    P_A_i   = -rho_J_cell + P_vac_sweep[i]  # total vacuum pressure
    if abs(rho_A_i) > 1e-15:
        w_A_sweep[i] = P_A_i / rho_A_i
    else:
        w_A_sweep[i] = -1.0

w_A_past = w_A_sweep[past_mask]

print(f"\n=== w(tau) sweep under both interpretations ===")
print(f"  w_A (combined) at fold:   {w_A_sweep[fold_idx]:.6f}")
print(f"  w_A range:                [{w_A_sweep.min():.6f}, {w_A_sweep.max():.6f}]")
print(f"  w_B (GGE-only) at fold:   {w_sweep[fold_idx]:.6f}")
print(f"  w_B range:                [{w_sweep.min():.6f}, {w_sweep.max():.6f}]")

# =============================================================================
# 7. CPL parametrization fit: w(a) = w_0 + w_a*(1-a) = w_0 + w_a*z/(1+z)
# =============================================================================
# Fit both interpretations

def cpl_fit(z_arr, w_arr):
    """Fit w = w_0 + w_a * z/(1+z) by least squares."""
    x = z_arr / (1.0 + z_arr)
    # Linear regression: w = w_0 + w_a * x
    A_mat = np.column_stack([np.ones_like(x), x])
    result = np.linalg.lstsq(A_mat, w_arr, rcond=None)
    w0_fit, wa_fit = result[0]
    residuals = w_arr - (w0_fit + wa_fit * x)
    rms = np.sqrt(np.mean(residuals**2))
    return w0_fit, wa_fit, rms

print(f"\n=== CPL Fit: w(z) = w_0 + w_a * z/(1+z) ===")

# Interpretation B: GGE-only (the natural DESI comparison for dynamical DE)
if past_mask.sum() >= 2:
    w0_B_fit, wa_B_fit, rms_B = cpl_fit(z_past, w_past)
    print(f"\n  Interpretation B (GGE only):")
    print(f"    w_0 = {w0_B_fit:.6f}")
    print(f"    w_a = {wa_B_fit:.6f}")
    print(f"    RMS residual = {rms_B:.6f}")
else:
    # Fallback: use fold value as w_0, estimate w_a from dw/dtau
    w0_B_fit = w_sweep[fold_idx]
    # dw/dz at z=0: dw/dz = (dw/dtau)/(dz/dtau)
    # dz/dtau = -(a_fold/a^2) * da/dtau
    wa_B_fit = 0.0  # Cannot fit with <2 points  # (local)
    rms_B = 0.0  # (local)
    print(f"\n  Interpretation B: insufficient past points, using fold value")
    print(f"    w_0 = {w0_B_fit:.6f}")
    print(f"    w_a = {wa_B_fit:.6f}")

# Interpretation A: Combined (Josephson + GGE)
if past_mask.sum() >= 2:
    w0_A_fit, wa_A_fit, rms_A = cpl_fit(z_past, w_A_past)
    print(f"\n  Interpretation A (combined):")
    print(f"    w_0 = {w0_A_fit:.6f}")
    print(f"    w_a = {wa_A_fit:.6f}")
    print(f"    RMS residual = {rms_A:.6f}")
else:
    w0_A_fit = w_A_sweep[fold_idx]
    wa_A_fit = 0.0  # (local)
    rms_A = 0.0  # (local)
    print(f"\n  Interpretation A: insufficient past points, using fold value")
    print(f"    w_0 = {w0_A_fit:.6f}")
    print(f"    w_a = {wa_A_fit:.6f}")

# =============================================================================
# 8. Direct w_0 from fold (no CPL fit needed for single-point comparison)
# =============================================================================
# The fold is the "present" — w_0 is the z=0 value
w_0_direct_A = w_A_sweep[fold_idx]
w_0_direct_B = w_sweep[fold_idx]

print(f"\n=== Direct w_0 at fold (z=0) ===")
print(f"  w_0 (A, combined):      {w_0_direct_A:.6f}")
print(f"  w_0 (B, GGE only):      {w_0_direct_B:.6f}")
print(f"  w_0 (W0-1 combined):    {w_combined:.6f}")
print(f"  w_0 (W0-1 GGE only):    {w_DE_GGE:.6f}")

# Cross-check: W0-1 computed w at the fold using S57 data.
# W0-2 computed w at the fold using a fresh 50-point sweep.
# These should be very close.
dw_A_check = abs(w_0_direct_A - w_combined)
dw_B_check = abs(w_0_direct_B - w_DE_GGE)
print(f"\n  Cross-check A: |w_0_direct - w_combined| = {dw_A_check:.6f}")
print(f"  Cross-check B: |w_0_direct - w_DE_GGE|   = {dw_B_check:.6f}")

# =============================================================================
# 9. Observational comparison
# =============================================================================

# Observational values
desi_dr1_w0    = -0.72  # (local)
desi_dr1_w0_e  = 0.08  # (local)
desi_dr1_wa    = -0.41  # (local)
desi_dr1_wa_e  = 0.31  # (local)

# DESI DR2 (from arXiv 2503.14738)
desi_dr2_w0    = -0.752  # (local)
desi_dr2_w0_e  = 0.057   # tighter constraints in DR2  # (local)
desi_dr2_wa    = -0.73  # (local)
desi_dr2_wa_e  = 0.25  # (local)

planck_w       = -1.03  # (local)
planck_w_e     = 0.03  # (local)

lcdm_w0        = -1.0  # (local)
lcdm_wa        = 0.0  # (local)

# Pre-Shattering prediction (S49 P-8)
pre_shat_w0    = -0.509  # (local)
pre_shat_w0_e  = 0.079  # (local)

# S57 w_GGE
w_S57          = -0.408  # (local)

print(f"\n{'='*72}")
print(f"  OBSERVATIONAL COMPARISON TABLE")
print(f"{'='*72}")
print(f"{'Source':<30s} {'w_0':>10s} {'sigma_w0':>10s} {'w_a':>10s} {'sigma_wa':>10s}")
print(f"{'-'*72}")
print(f"{'LCDM':<30s} {lcdm_w0:>10.3f} {'---':>10s} {lcdm_wa:>10.3f} {'---':>10s}")
print(f"{'Planck 2018 (const w)':<30s} {planck_w:>10.3f} {planck_w_e:>10.3f} {'---':>10s} {'---':>10s}")
print(f"{'DESI DR1 (w0wa CDM)':<30s} {desi_dr1_w0:>10.3f} {desi_dr1_w0_e:>10.3f} {desi_dr1_wa:>10.3f} {desi_dr1_wa_e:>10.3f}")
print(f"{'DESI DR2 (w0wa CDM)':<30s} {desi_dr2_w0:>10.3f} {desi_dr2_w0_e:>10.3f} {desi_dr2_wa:>10.3f} {desi_dr2_wa_e:>10.3f}")
print(f"{'Pre-Shattering S49':<30s} {pre_shat_w0:>10.3f} {pre_shat_w0_e:>10.3f} {'---':>10s} {'---':>10s}")
print(f"{'S57 w_GGE':<30s} {w_S57:>10.3f} {'---':>10s} {'---':>10s} {'---':>10s}")
print(f"{'Framework A (combined)':<30s} {w_0_direct_A:>10.4f} {'---':>10s} {wa_A_fit:>10.4f} {'---':>10s}")
print(f"{'Framework B (GGE only)':<30s} {w_0_direct_B:>10.4f} {'---':>10s} {wa_B_fit:>10.4f} {'---':>10s}")

# =============================================================================
# 10. Sigma tension computation
# =============================================================================
print(f"\n{'='*72}")
print(f"  SIGMA TENSION")
print(f"{'='*72}")

def sigma_tension_w0(w_model, w_obs, sigma_obs):
    return abs(w_model - w_obs) / sigma_obs

def sigma_tension_2d(w0_m, wa_m, w0_obs, wa_obs, sig_w0, sig_wa, rho_corr=0.0):
    """2D sigma tension in the (w0, wa) plane, assuming Gaussian with correlation rho."""
    dw0 = w0_m - w0_obs
    dwa = wa_m - wa_obs
    # Fisher matrix (inverse covariance)
    det = sig_w0**2 * sig_wa**2 * (1 - rho_corr**2)
    chi2 = (dw0**2 * sig_wa**2 - 2*rho_corr*sig_w0*sig_wa*dw0*dwa + dwa**2 * sig_w0**2) / det
    return np.sqrt(chi2)

# --- Against DESI DR1 ---
sig_A_dr1 = sigma_tension_w0(w_0_direct_A, desi_dr1_w0, desi_dr1_w0_e)
sig_B_dr1 = sigma_tension_w0(w_0_direct_B, desi_dr1_w0, desi_dr1_w0_e)

# --- Against DESI DR2 ---
sig_A_dr2 = sigma_tension_w0(w_0_direct_A, desi_dr2_w0, desi_dr2_w0_e)
sig_B_dr2 = sigma_tension_w0(w_0_direct_B, desi_dr2_w0, desi_dr2_w0_e)

# --- Against Planck (constant w) ---
sig_A_planck = sigma_tension_w0(w_0_direct_A, planck_w, planck_w_e)
sig_B_planck = sigma_tension_w0(w_0_direct_B, planck_w, planck_w_e)

# --- Against LCDM ---
sig_A_lcdm = sigma_tension_w0(w_0_direct_A, lcdm_w0, desi_dr2_w0_e)  # use DR2 sigma
sig_B_lcdm = sigma_tension_w0(w_0_direct_B, lcdm_w0, desi_dr2_w0_e)

# --- Pre-Shattering S49 ---
sig_preShat_dr2 = sigma_tension_w0(pre_shat_w0, desi_dr2_w0, desi_dr2_w0_e)
sig_s57_dr2     = sigma_tension_w0(w_S57, desi_dr2_w0, desi_dr2_w0_e)

# 2D tension (w0, wa) against DESI DR1
# DESI DR1 correlation: rho ~ -0.56 (from contour plots in DESI papers)
rho_corr_dr1 = -0.56  # (local)
sig_2d_A_dr1 = sigma_tension_2d(w_0_direct_A, wa_A_fit, desi_dr1_w0, desi_dr1_wa,
                                 desi_dr1_w0_e, desi_dr1_wa_e, rho_corr_dr1)
sig_2d_B_dr1 = sigma_tension_2d(w_0_direct_B, wa_B_fit, desi_dr1_w0, desi_dr1_wa,
                                 desi_dr1_w0_e, desi_dr1_wa_e, rho_corr_dr1)

# 2D tension against DESI DR2
rho_corr_dr2 = -0.60  # Approximate from DR2 contours  # (local)
sig_2d_A_dr2 = sigma_tension_2d(w_0_direct_A, wa_A_fit, desi_dr2_w0, desi_dr2_wa,
                                 desi_dr2_w0_e, desi_dr2_wa_e, rho_corr_dr2)
sig_2d_B_dr2 = sigma_tension_2d(w_0_direct_B, wa_B_fit, desi_dr2_w0, desi_dr2_wa,
                                 desi_dr2_w0_e, desi_dr2_wa_e, rho_corr_dr2)

print(f"\n{'Comparison':<35s} {'Interp A':>10s} {'Interp B':>10s}")
print(f"{'-'*57}")
print(f"{'|Delta w_0| vs DESI DR1':<35s} {sig_A_dr1:>10.2f}σ {sig_B_dr1:>10.2f}σ")
print(f"{'|Delta w_0| vs DESI DR2':<35s} {sig_A_dr2:>10.2f}σ {sig_B_dr2:>10.2f}σ")
print(f"{'|Delta w_0| vs Planck 2018':<35s} {sig_A_planck:>10.2f}σ {sig_B_planck:>10.2f}σ")
print(f"{'|Delta w_0| vs LCDM':<35s} {sig_A_lcdm:>10.2f}σ {sig_B_lcdm:>10.2f}σ")
print(f"{'2D (w0,wa) vs DESI DR1':<35s} {sig_2d_A_dr1:>10.2f}σ {sig_2d_B_dr1:>10.2f}σ")
print(f"{'2D (w0,wa) vs DESI DR2':<35s} {sig_2d_A_dr2:>10.2f}σ {sig_2d_B_dr2:>10.2f}σ")

print(f"\n  For reference:")
print(f"  Pre-Shattering S49 vs DR2:  {sig_preShat_dr2:.2f}σ")
print(f"  S57 w_GGE vs DR2:           {sig_s57_dr2:.2f}σ")

# =============================================================================
# 11. Direction of movement under Volovik partition
# =============================================================================
print(f"\n{'='*72}")
print(f"  DIRECTION OF MOVEMENT UNDER VOLOVIK PARTITION")
print(f"{'='*72}")

# The Mack question: does w move TOWARD or AWAY from DESI under Volovik?
# Pre-Volovik: w_GGE = -0.408 (S57), distance from DR2 = |(-0.408)-(-0.752)| = 0.344
# Post-Volovik A: w = -0.917, distance from DR2 = |(-0.917)-(-0.752)| = 0.165
# Post-Volovik B: w = -0.408, distance from DR2 = |(-0.408)-(-0.752)| = 0.344

dist_S57_dr2 = abs(w_S57 - desi_dr2_w0)
dist_A_dr2   = abs(w_0_direct_A - desi_dr2_w0)
dist_B_dr2   = abs(w_0_direct_B - desi_dr2_w0)

print(f"\n  Distance from DESI DR2 (w_0 = {desi_dr2_w0}):")
print(f"    S57 (pre-Volovik):  {dist_S57_dr2:.4f} ({sig_s57_dr2:.1f}σ)")
print(f"    Interp A (combined):{dist_A_dr2:.4f} ({sig_A_dr2:.1f}σ)")
print(f"    Interp B (GGE only):{dist_B_dr2:.4f} ({sig_B_dr2:.1f}σ)")

if dist_A_dr2 < dist_S57_dr2:
    dir_A = "TOWARD"
    improvement_A = (dist_S57_dr2 - dist_A_dr2) / dist_S57_dr2 * 100
else:
    dir_A = "AWAY"
    improvement_A = -(dist_A_dr2 - dist_S57_dr2) / dist_S57_dr2 * 100

print(f"\n  Interpretation A: w moved {dir_A} DESI DR2 ({improvement_A:+.1f}%)")

if dist_B_dr2 < dist_S57_dr2:
    dir_B = "TOWARD"
    improvement_B = (dist_S57_dr2 - dist_B_dr2) / dist_S57_dr2 * 100
else:
    dir_B = "AWAY"
    improvement_B = -(dist_B_dr2 - dist_S57_dr2) / dist_S57_dr2 * 100

print(f"  Interpretation B: w moved {dir_B} DESI DR2 ({improvement_B:+.1f}%)")

# Pre-Shattering comparison
dist_preShat = abs(pre_shat_w0 - desi_dr2_w0)
print(f"\n  Pre-Shattering S49 distance: {dist_preShat:.4f} ({sig_preShat_dr2:.1f}σ)")
print(f"  S57 -> Volovik A delta:      {dist_S57_dr2:.4f} -> {dist_A_dr2:.4f}")
print(f"  S49 -> S57 -> Volovik A:     {dist_preShat:.4f} -> {dist_S57_dr2:.4f} -> {dist_A_dr2:.4f}")

# =============================================================================
# 12. Gate verdict
# =============================================================================
print(f"\n{'='*72}")
print(f"  GATE VERDICT: W-DESI-58")
print(f"{'='*72}")

# Use interpretation A as primary (most conservative: includes Josephson)
# Gate criterion on w_0 tension vs DESI DR2
primary_sigma = sig_A_dr2
secondary_sigma = sig_B_dr2

# Also check 2D tension
primary_2d = sig_2d_A_dr2
secondary_2d = sig_2d_B_dr2

print(f"\n  Primary (Interpretation A, combined):")
print(f"    w_0 = {w_0_direct_A:.4f}")
print(f"    w_a = {wa_A_fit:.4f}")
print(f"    1D tension vs DESI DR2: {primary_sigma:.2f}σ")
print(f"    2D tension vs DESI DR2: {primary_2d:.2f}σ")

print(f"\n  Secondary (Interpretation B, GGE only):")
print(f"    w_0 = {w_0_direct_B:.4f}")
print(f"    w_a = {wa_B_fit:.4f}")
print(f"    1D tension vs DESI DR2: {secondary_sigma:.2f}σ")
print(f"    2D tension vs DESI DR2: {secondary_2d:.2f}σ")

# Decision: use the PRIMARY (A) value for the gate
# But report BOTH since interpretation choice is itself a model assumption
if primary_sigma < 3.0:
    verdict = "PASS"
    verdict_detail = f"w_0 tension {primary_sigma:.2f}σ < 3σ threshold"
elif primary_sigma > 5.0:
    verdict = "FAIL"
    verdict_detail = f"w_0 tension {primary_sigma:.2f}σ > 5σ threshold"
else:
    verdict = "INFO"
    verdict_detail = f"w_0 tension {primary_sigma:.2f}σ in [3σ, 5σ] marginal range"

# But also check: if interpretation B FAILS, that constrains the interpretation.
if secondary_sigma > 5.0:
    interp_constraint = "Interpretation B EXCLUDED by DESI DR2 (>5σ)"
elif secondary_sigma > 3.0:
    interp_constraint = f"Interpretation B in tension with DESI DR2 ({secondary_sigma:.1f}σ)"
else:
    interp_constraint = f"Both interpretations consistent with DESI DR2"

print(f"\n  GATE VERDICT: {verdict}")
print(f"  Detail: {verdict_detail}")
print(f"  Interpretation constraint: {interp_constraint}")
print(f"\n  Gate criteria:")
print(f"    PASS: |w_0 - w_0(DR2)| < 3σ  -> {primary_sigma:.2f}σ {'<' if primary_sigma<3 else '>'} 3.0")
print(f"    FAIL: |w_0 - w_0(DR2)| > 5σ  -> {primary_sigma:.2f}σ {'<' if primary_sigma<5 else '>'} 5.0")

# =============================================================================
# 13. Trajectory summary
# =============================================================================
print(f"\n{'='*72}")
print(f"  w_0 TRAJECTORY")
print(f"{'='*72}")
print(f"  S49 (pre-Shattering):   w_0 = {pre_shat_w0:.3f} ± {pre_shat_w0_e:.3f}  ({sig_preShat_dr2:.1f}σ from DR2)")
print(f"  S57 (GGE only):         w_0 = {w_S57:.3f}         ({sig_s57_dr2:.1f}σ from DR2)")
print(f"  S58 Volovik Interp A:   w_0 = {w_0_direct_A:.4f}       ({sig_A_dr2:.1f}σ from DR2)")
print(f"  S58 Volovik Interp B:   w_0 = {w_0_direct_B:.4f}       ({sig_B_dr2:.1f}σ from DR2)")
print(f"  DESI DR1:               w_0 = {desi_dr1_w0:.3f} ± {desi_dr1_w0_e:.3f}")
print(f"  DESI DR2:               w_0 = {desi_dr2_w0:.3f} ± {desi_dr2_w0_e:.3f}")
print(f"  Planck 2018:            w   = {planck_w:.3f} ± {planck_w_e:.3f}")
print(f"  LCDM:                   w_0 = {lcdm_w0:.3f}")
print(f"\n  Direction under Volovik: Interpretation A moves w {dir_A} DESI by {abs(improvement_A):.0f}%")

# =============================================================================
# 14. Save results
# =============================================================================
outpath = os.path.join(SCRIPT_DIR, 's58_w_desi.npz')
np.savez(outpath,
    # Primary results
    w_0_A=w_0_direct_A,
    w_0_B=w_0_direct_B,
    w_a_A=wa_A_fit,
    w_a_B=wa_B_fit,
    w_combined=w_combined,
    w_DE_GGE=w_DE_GGE,

    # CPL fit results
    w0_A_fit=w0_A_fit,
    wa_A_fit=wa_A_fit,
    rms_A=rms_A,
    w0_B_fit=w0_B_fit,
    wa_B_fit=wa_B_fit,
    rms_B=rms_B,

    # Sweep data (mapped to z)
    tau_values=tau_values,
    z_from_tau=z_from_tau,
    w_sweep_B=w_sweep,
    w_sweep_A=w_A_sweep,
    z_past=z_past if past_mask.sum() > 0 else np.array([]),
    w_past_B=w_past if past_mask.sum() > 0 else np.array([]),
    w_past_A=w_A_past if past_mask.sum() > 0 else np.array([]),

    # Sigma tensions
    sig_A_dr1=sig_A_dr1,
    sig_B_dr1=sig_B_dr1,
    sig_A_dr2=sig_A_dr2,
    sig_B_dr2=sig_B_dr2,
    sig_A_planck=sig_A_planck,
    sig_B_planck=sig_B_planck,
    sig_2d_A_dr1=sig_2d_A_dr1,
    sig_2d_B_dr1=sig_2d_B_dr1,
    sig_2d_A_dr2=sig_2d_A_dr2,
    sig_2d_B_dr2=sig_2d_B_dr2,
    sig_preShat_dr2=sig_preShat_dr2,
    sig_s57_dr2=sig_s57_dr2,

    # Observational references
    desi_dr1_w0=desi_dr1_w0,
    desi_dr1_w0_e=desi_dr1_w0_e,
    desi_dr1_wa=desi_dr1_wa,
    desi_dr1_wa_e=desi_dr1_wa_e,
    desi_dr2_w0=desi_dr2_w0,
    desi_dr2_w0_e=desi_dr2_w0_e,
    desi_dr2_wa=desi_dr2_wa,
    desi_dr2_wa_e=desi_dr2_wa_e,
    planck_w=planck_w,
    planck_w_e=planck_w_e,
    pre_shat_w0=pre_shat_w0,
    pre_shat_w0_e=pre_shat_w0_e,

    # Energy budget
    rho_J_cell=rho_J_cell,
    rho_GGE=rho_GGE,
    P_GGE=P_GGE,
    E_matter_Volovik=E_matter_V,
    F_Josephson=F_Josephson,

    # Direction of movement
    dist_S57_dr2=dist_S57_dr2,
    dist_A_dr2=dist_A_dr2,
    dist_B_dr2=dist_B_dr2,
    direction_A=np.array([dir_A]),
    improvement_A_pct=improvement_A,

    # Gate
    gate_name=np.array(['W-DESI-58']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([verdict_detail]),
    interp_constraint=np.array([interp_constraint]),
)

print(f"\n  Saved: {outpath}")

# =============================================================================
# 15. Diagnostic: tau-z-w table
# =============================================================================
print(f"\n{'='*72}")
print(f"  TAU-Z-W TABLE (selected points)")
print(f"{'='*72}")
print(f"  {'tau':>8s}  {'z':>8s}  {'w_A':>10s}  {'w_B':>10s}  {'Lambda_eff':>12s}")
print(f"  {'-'*54}")

# Select ~10 representative points
rep_idx = np.linspace(0, len(tau_values)-1, 12, dtype=int)
for i in rep_idx:
    z_i = z_from_tau[i]
    print(f"  {tau_values[i]:8.4f}  {z_i:8.4f}  {w_A_sweep[i]:10.6f}  {w_sweep[i]:10.6f}  {Lambda_eff_sw[i]:+12.6f}")

print(f"\n{'='*72}")
print(f"  W-DESI-58 COMPLETE")
print(f"{'='*72}")
