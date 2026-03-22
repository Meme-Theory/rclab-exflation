#!/usr/bin/env python3
"""
DESI-DR3-PREP-49: Bayes factor framework vs LCDM at corrected alpha range.

Gate: DESI-DR3-PREP-49
  PASS: B > 1 (framework preferred over LCDM by DESI data)
  INFO: 1/10 < B < 1
  FAIL: B < 1/10 (framework decisively disfavored)

Physics:
  The framework predicts a SPECIFIC w_0 band from the GGE post-transit relic:
    w_0 = -1/(1+alpha), where alpha = E_total / P_Zubarev.
  S49 MULTI-T-FRIEDMANN revised the band:
    w_0(Zubarev GGE)   = -0.430  [multi-T corrected]
    w_0(Keldysh sigma)  = -0.588  [S48 upper bound]
  Framework predicts w_a ~ -0.009 (essentially zero).

  DESI DR2 (2025):
    w_0 = -0.752 +/- 0.058  (w0waCDM fit, BAO + CMB + SNe)
    w_a = -0.73  +/- 0.28

  LCDM: w_0 = -1.0, w_a = 0.0 (exactly).

  We compute:
    B_vs_LCDM = P(DESI|framework) / P(DESI|LCDM)
    B_vs_w0wa = P(DESI|framework) / P(DESI|w0waCDM best-fit)

  Then forecast DR3 (sigma_w0 ~ 0.035) and identify the exclusion threshold.

Method:
  1. Framework likelihood: Gaussian in w_0 centered on prediction with spread sigma_fw.
     Two scenarios: w_0 = -0.43 (Zubarev) and w_0 = -0.59 (Keldysh midpoint).
  2. DESI likelihood: Gaussian in (w_0, w_a) from DR2 posterior.
  3. LCDM is a delta function at (w_0, w_a) = (-1, 0).
  4. Bayes factor: analytic convolution of Gaussians.
  5. DR3 forecast: project sigma shrinkage and find exclusion contour.

Pre-registered predictions (falsifiable):
  Framework: w_0 in [-0.43, -0.59], w_a in [-0.01, 0.00].
  If DR3 measures w_0 < -0.65 at 3sigma, framework is excluded.
  If DR3 measures w_a < -0.3 at 3sigma, framework is excluded.

Author: Gen-Physicist
Session: 49
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_Lambda,
    rho_Lambda_obs, M_KK_gravity
)

np.set_printoptions(precision=10, linewidth=120)

print("=" * 78)
print("DESI-DR3-PREP-49: Bayes Factor Framework vs LCDM for DESI")
print("=" * 78)

# =============================================================================
# Step 1: Load upstream data
# =============================================================================

d_s48 = np.load('s48_dmde_refine.npz', allow_pickle=True)
d_s49 = np.load('s49_multi_t_friedmann.npz', allow_pickle=True)

# S48 band
w0_S48_lo = float(d_s48['w0_band_lo'])    # -0.465
w0_S48_hi = float(d_s48['w0_band_hi'])    # -0.589

# S49 multi-T corrected values
w0_GGE    = float(d_s49['w0_GGE'])        # -0.430 (Zubarev, multi-T)
w0_s46    = float(d_s49['w0_s46'])         # -0.468 (single-T, S46 occupations)
wa_free   = float(d_s49['wa_free_cpl'])    # -0.009

# DESI DR2 (2025) — w0waCDM fit
w0_desi   = float(d_s49['w0_desi_dr2'])    # -0.752
sig_w0    = float(d_s49['w0_desi_dr2_err']) # 0.058
wa_desi   = float(d_s49['wa_desi_dr2'])    # -0.73
sig_wa    = float(d_s49['wa_desi_dr2_err']) # 0.28

# DESI DR1 for comparison
w0_dr1    = float(d_s48['w0_desi_dr1'])    # -0.55
sig_w0_dr1 = float(d_s48['w0_desi_dr1_err']) # 0.21

print("\n--- Input Parameters ---")
print(f"  Framework w_0 (Zubarev GGE, multi-T): {w0_GGE:.4f}")
print(f"  Framework w_0 (S46 single-T):         {w0_s46:.4f}")
print(f"  Framework w_0 band (S48):              [{w0_S48_lo:.4f}, {w0_S48_hi:.4f}]")
print(f"  Framework w_a (free coupling):         {wa_free:.4f}")
print(f"  DESI DR2 w_0:                          {w0_desi:.3f} +/- {sig_w0:.3f}")
print(f"  DESI DR2 w_a:                          {wa_desi:.2f} +/- {sig_wa:.2f}")
print(f"  DESI DR1 w_0:                          {w0_dr1:.2f} +/- {sig_w0_dr1:.2f}")

# =============================================================================
# Step 2: Define framework parameter space
# =============================================================================
# The framework predicts a BAND in w_0 from the Z-K discrepancy (S48).
# Post-S49 multi-T correction, the band is:
#   w_0 in [-0.430 (Zubarev GGE), -0.588 (Keldysh sigma)]
# Model as a Gaussian centered on the band midpoint with sigma = half-width.

w0_fw_lo   = w0_GGE       # -0.430  (Zubarev limit)
w0_fw_hi   = w0_S48_hi    # -0.589  (Keldysh limit)
w0_fw_mid  = 0.5 * (w0_fw_lo + w0_fw_hi)   # -0.509
sig_fw     = 0.5 * abs(w0_fw_hi - w0_fw_lo)  # 0.079

wa_fw      = wa_free       # -0.009
sig_wa_fw  = 0.02          # Conservative: framework allows |w_a| < 0.02

print(f"\n--- Framework Prediction (pre-registered) ---")
print(f"  w_0: {w0_fw_mid:.4f} +/- {sig_fw:.4f}  (band: [{w0_fw_lo:.3f}, {w0_fw_hi:.3f}])")
print(f"  w_a: {wa_fw:.4f} +/- {sig_wa_fw:.4f}")

# =============================================================================
# Step 3: Bayes factor computation — analytic
# =============================================================================
# For two competing models evaluated against data D = (w0_obs +/- sigma_obs):
#
# Model M_fw: w_0 ~ N(mu_fw, sigma_fw^2)    [framework prediction band]
# Model M_LC: w_0 = -1.0 exactly             [LCDM delta function]
#
# DESI DR2 data: w_0 = w0_desi +/- sig_w0
#
# Likelihood for framework (marginalized over w_0):
#   P(D|M_fw) = integral N(w0_obs; w_0, sig_w0^2) * N(w_0; mu_fw, sig_fw^2) dw_0
#             = N(w0_obs; mu_fw, sig_w0^2 + sig_fw^2)
#
# Likelihood for LCDM:
#   P(D|M_LC) = N(w0_obs; -1.0, sig_w0^2)
#
# Bayes factor:
#   B = P(D|M_fw) / P(D|M_LC)

print("\n" + "=" * 78)
print("SECTION A: Bayes Factor in w_0 (1D, marginalized over w_a)")
print("=" * 78)

# --- In w_0 only (marginalizing w_a, since DESI constrains w_0 much tighter) ---

def log_bayes_factor_1d(w0_obs, sig_obs, w0_pred, sig_pred, w0_ref):
    """
    Log Bayes factor for framework (Gaussian prior on w_0) vs
    reference model (delta function at w0_ref).

    B = N(w0_obs; w0_pred, sig_obs^2 + sig_pred^2) / N(w0_obs; w0_ref, sig_obs^2)

    Returns ln(B).
    """
    sig_eff_sq = sig_obs**2 + sig_pred**2
    # Log-likelihood ratio
    lnB = (-0.5 * (w0_obs - w0_pred)**2 / sig_eff_sq
           + 0.5 * (w0_obs - w0_ref)**2 / sig_obs**2
           - 0.5 * np.log(sig_eff_sq / sig_obs**2))
    return lnB


# --- Scenario 1: w_0 = -0.430 (Zubarev GGE, multi-T) ---
# Framework uncertainty: sig_fw (Z-K band half-width)
lnB_zubarev = log_bayes_factor_1d(w0_desi, sig_w0, w0_GGE, sig_fw, -1.0)
B_zubarev = np.exp(lnB_zubarev)

# --- Scenario 2: w_0 = -0.509 (band midpoint) ---
lnB_mid = log_bayes_factor_1d(w0_desi, sig_w0, w0_fw_mid, sig_fw, -1.0)
B_mid = np.exp(lnB_mid)

# --- Scenario 3: w_0 = -0.589 (Keldysh limit) ---
lnB_keldysh = log_bayes_factor_1d(w0_desi, sig_w0, w0_fw_hi, 0.04, -1.0)
B_keldysh = np.exp(lnB_keldysh)

# --- Framework as uniform prior over [-0.43, -0.59] ---
def P_D_fw_uniform(w0_obs, sig_obs, w0_lo, w0_hi):
    """P(D|M_fw) with uniform prior on w_0 in [w0_lo, w0_hi].

    Integrates N(w0_obs; w_0, sig_obs^2) * (1/width) over the band.
    Uses sorted bounds to avoid sign errors from parameter ordering.
    """
    lo = min(w0_lo, w0_hi)
    hi = max(w0_lo, w0_hi)
    width = hi - lo
    return (norm.cdf(hi, loc=w0_obs, scale=sig_obs)
            - norm.cdf(lo, loc=w0_obs, scale=sig_obs)) / width

P_D_fw_uni = P_D_fw_uniform(w0_desi, sig_w0, w0_fw_lo, w0_fw_hi)
P_D_lcdm = norm.pdf(w0_desi, loc=-1.0, scale=sig_w0)
B_uniform = P_D_fw_uni / P_D_lcdm

# --- Framework vs w0waCDM best-fit (as reference) ---
# w0waCDM best-fit from DESI DR2: w_0 = -0.752, w_a = -0.73
# This IS the data peak, so P(D|w0waCDM) is maximal
P_D_w0wa_bestfit = norm.pdf(w0_desi, loc=w0_desi, scale=sig_w0)  # = 1/(sqrt(2pi)*sig_w0)
B_vs_w0wa = P_D_fw_uni / P_D_w0wa_bestfit

print(f"\n--- Bayes Factor Results (1D, w_0 only) ---")
print(f"  Against LCDM (w_0 = -1.0):")
print(f"    B(Zubarev, w_0={w0_GGE:.3f}):     {B_zubarev:.4e}  (ln B = {lnB_zubarev:.2f})")
print(f"    B(midpoint, w_0={w0_fw_mid:.3f}):  {B_mid:.4e}  (ln B = {lnB_mid:.2f})")
print(f"    B(Keldysh, w_0={w0_fw_hi:.3f}):    {B_keldysh:.4e}  (ln B = {lnB_keldysh:.2f})")
print(f"    B(uniform [{w0_fw_lo:.3f},{w0_fw_hi:.3f}]): {B_uniform:.4e}")
print(f"  Against w0waCDM best-fit:")
print(f"    B(uniform [{w0_fw_lo:.3f},{w0_fw_hi:.3f}]): {B_vs_w0wa:.4e}")

# Tension in sigma
tension_zubarev = abs(w0_desi - w0_GGE) / np.sqrt(sig_w0**2 + sig_fw**2)
tension_mid     = abs(w0_desi - w0_fw_mid) / np.sqrt(sig_w0**2 + sig_fw**2)
tension_keldysh = abs(w0_desi - w0_fw_hi) / sig_w0
tension_lcdm    = abs(w0_desi - (-1.0)) / sig_w0

print(f"\n--- Tension (sigma) ---")
print(f"  Framework (Zubarev) vs DESI:  {tension_zubarev:.2f} sigma")
print(f"  Framework (midpoint) vs DESI: {tension_mid:.2f} sigma")
print(f"  Framework (Keldysh) vs DESI:  {tension_keldysh:.2f} sigma")
print(f"  LCDM vs DESI DR2:             {tension_lcdm:.2f} sigma")

# =============================================================================
# Step 4: 2D Bayes factor (w_0, w_a jointly)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION B: 2D Bayes Factor (w_0, w_a jointly)")
print("=" * 78)

# DESI DR2 measures (w_0, w_a) with correlation.
# Published DR2 correlation coefficient rho ~ -0.7 to -0.8
# We use rho = -0.75 (standard for DESI-like analyses)
rho_corr = -0.75

def log_P_2d_gauss(w0, wa, w0_obs, wa_obs, sig0, siga, rho):
    """Log of bivariate Gaussian PDF."""
    dw0 = w0 - w0_obs
    dwa = wa - wa_obs
    det = 1.0 - rho**2
    chi2 = (dw0**2/sig0**2 - 2*rho*dw0*dwa/(sig0*siga) + dwa**2/siga**2) / det
    return -0.5 * chi2 - np.log(2*np.pi*sig0*siga*np.sqrt(det))

# P(D|LCDM) in 2D
lnP_lcdm_2d = log_P_2d_gauss(-1.0, 0.0, w0_desi, wa_desi, sig_w0, sig_wa, rho_corr)

# P(D|framework) in 2D — marginalize over framework prior
# Framework prior: N(w0_fw_mid, sig_fw^2) x N(wa_fw, sig_wa_fw^2)
# Marginalization = convolution of two Gaussians in each direction

sig_w0_eff = np.sqrt(sig_w0**2 + sig_fw**2)
sig_wa_eff = np.sqrt(sig_wa**2 + sig_wa_fw**2)

# Cross-correlation: only DESI has correlation, framework prior is diagonal
# After convolution, effective correlation:
rho_eff = rho_corr * sig_w0 * sig_wa / (sig_w0_eff * sig_wa_eff)

lnP_fw_2d = log_P_2d_gauss(w0_fw_mid, wa_fw, w0_desi, wa_desi,
                             sig_w0_eff, sig_wa_eff, rho_eff)
# Add the normalization correction for the wider effective sigma
# (already included in the Gaussian formula above)

lnB_2d = lnP_fw_2d - lnP_lcdm_2d
B_2d = np.exp(lnB_2d)

print(f"  ln P(D|LCDM, 2D):      {lnP_lcdm_2d:.4f}")
print(f"  ln P(D|framework, 2D): {lnP_fw_2d:.4f}")
print(f"  ln B(2D):               {lnB_2d:.4f}")
print(f"  B(2D) = P(D|fw)/P(D|LCDM): {B_2d:.4e}")

# Interpretation
print(f"\n  Interpretation:")
if B_2d > 1:
    print(f"    Framework PREFERRED over LCDM by factor {B_2d:.1f}")
elif B_2d > 0.1:
    print(f"    Inconclusive: B = {B_2d:.3f} (in [0.1, 1])")
else:
    print(f"    Framework DISFAVORED vs LCDM by factor {1/B_2d:.1f}")

# Key insight: the (w_0, w_a) anti-correlation in DESI helps the framework
# because framework predicts (w_0 ~ -0.5, w_a ~ 0) which is on the OPPOSITE
# side of the degeneracy line from (w_0 ~ -0.75, w_a ~ -0.73).
print(f"\n  Note: DESI (w_0, w_a) anti-correlation rho = {rho_corr:.2f}")
print(f"  Framework prediction ({w0_fw_mid:.2f}, {wa_fw:.3f}) is OFF the DESI")
print(f"  degeneracy direction. The 2D penalty may differ from 1D.")

# =============================================================================
# Step 5: DR3 Forecast
# =============================================================================

print("\n" + "=" * 78)
print("SECTION C: DR3 Forecast (sigma_w0 ~ 0.035)")
print("=" * 78)

sig_w0_dr3 = 0.035  # Expected DR3 precision
sig_wa_dr3 = 0.15   # Roughly proportional shrinkage

# Scan: at what DESI central value does B cross key thresholds?
w0_scan = np.linspace(-1.1, -0.3, 1000)

# For each hypothetical DR3 central value, compute B vs LCDM
B_scan_dr3 = np.zeros_like(w0_scan)
B_scan_dr2 = np.zeros_like(w0_scan)

for i, w0_hyp in enumerate(w0_scan):
    # DR3
    lnB_i = log_bayes_factor_1d(w0_hyp, sig_w0_dr3, w0_fw_mid, sig_fw, -1.0)
    B_scan_dr3[i] = np.exp(np.clip(lnB_i, -100, 100))
    # DR2 (current)
    lnB_i2 = log_bayes_factor_1d(w0_hyp, sig_w0, w0_fw_mid, sig_fw, -1.0)
    B_scan_dr2[i] = np.exp(np.clip(lnB_i2, -100, 100))

# Find crossings
def find_crossing(w0_arr, B_arr, threshold):
    """Find w_0 where B crosses threshold."""
    crossings = []
    for i in range(len(B_arr)-1):
        if (B_arr[i] - threshold) * (B_arr[i+1] - threshold) < 0:
            # Linear interpolation
            w0_cross = w0_arr[i] + (w0_arr[i+1] - w0_arr[i]) * (threshold - B_arr[i]) / (B_arr[i+1] - B_arr[i])
            crossings.append(w0_cross)
    return crossings

# Key thresholds
thresholds = {
    'B = 1 (equal)': 1.0,
    'B = 1/3 (weak against)': 1/3,
    'B = 1/10 (strong against)': 0.1,
    'B = 1/100 (decisive against)': 0.01,
    'B = 3 (weak for)': 3.0,
    'B = 10 (strong for)': 10.0,
}

print(f"\n  DR3 projected sigma_w0 = {sig_w0_dr3}")
print(f"  Framework prediction: w_0 = {w0_fw_mid:.3f} +/- {sig_fw:.3f}")
print(f"\n  Threshold crossings (w_0 value where B crosses):")
print(f"  {'Threshold':<35s} {'DR2 (sig=0.058)':<18s} {'DR3 (sig=0.035)':<18s}")
print(f"  {'-'*35} {'-'*18} {'-'*18}")

for label, thresh in thresholds.items():
    cross_dr2 = find_crossing(w0_scan, B_scan_dr2, thresh)
    cross_dr3 = find_crossing(w0_scan, B_scan_dr3, thresh)
    str_dr2 = ', '.join([f'{c:.3f}' for c in cross_dr2]) if cross_dr2 else 'no crossing'
    str_dr3 = ', '.join([f'{c:.3f}' for c in cross_dr3]) if cross_dr3 else 'no crossing'
    print(f"  {label:<35s} {str_dr2:<18s} {str_dr3:<18s}")

# At current DESI DR2 central value with DR3 precision
lnB_dr3_at_current = log_bayes_factor_1d(w0_desi, sig_w0_dr3, w0_fw_mid, sig_fw, -1.0)
B_dr3_at_current = np.exp(lnB_dr3_at_current)
tension_dr3 = abs(w0_desi - w0_fw_mid) / np.sqrt(sig_w0_dr3**2 + sig_fw**2)

print(f"\n  If DR3 confirms DR2 central value (w_0 = {w0_desi:.3f}):")
print(f"    B = {B_dr3_at_current:.4e}  (ln B = {lnB_dr3_at_current:.2f})")
print(f"    Tension: {tension_dr3:.2f} sigma")
print(f"    Verdict: {'DECISIVE EXCLUSION' if B_dr3_at_current < 0.01 else 'STRONG EXCLUSION' if B_dr3_at_current < 0.1 else 'INFO'}")

# Framework-favorable scenario: DR3 measures closer to framework
w0_dr3_favorable = -0.6  # Near Keldysh edge
lnB_favorable = log_bayes_factor_1d(w0_dr3_favorable, sig_w0_dr3, w0_fw_mid, sig_fw, -1.0)
B_favorable = np.exp(lnB_favorable)
tension_fav = abs(w0_dr3_favorable - w0_fw_mid) / np.sqrt(sig_w0_dr3**2 + sig_fw**2)
tension_fav_lcdm = abs(w0_dr3_favorable - (-1.0)) / sig_w0_dr3

print(f"\n  If DR3 shifts to w_0 = {w0_dr3_favorable:.2f} (framework-favorable):")
print(f"    B vs LCDM = {B_favorable:.2e}")
print(f"    Tension fw-DESI: {tension_fav:.2f} sigma")
print(f"    Tension LCDM-DESI: {tension_fav_lcdm:.2f} sigma")

# =============================================================================
# Step 6: Comparison with DR1
# =============================================================================

print("\n" + "=" * 78)
print("SECTION D: DR1 vs DR2 Evolution")
print("=" * 78)

lnB_dr1 = log_bayes_factor_1d(w0_dr1, sig_w0_dr1, w0_fw_mid, sig_fw, -1.0)
B_dr1 = np.exp(lnB_dr1)
tension_dr1 = abs(w0_dr1 - w0_fw_mid) / np.sqrt(sig_w0_dr1**2 + sig_fw**2)
tension_dr1_lcdm = abs(w0_dr1 - (-1.0)) / sig_w0_dr1

print(f"  DR1: w_0 = {w0_dr1:.2f} +/- {sig_w0_dr1:.2f}")
print(f"    B vs LCDM:     {B_dr1:.4e}  (ln B = {lnB_dr1:.2f})")
print(f"    Tension fw-DR1: {tension_dr1:.2f} sigma")
print(f"    Tension LCDM-DR1: {tension_dr1_lcdm:.2f} sigma")
print(f"\n  DR2: w_0 = {w0_desi:.3f} +/- {sig_w0:.3f}")
print(f"    B vs LCDM:     {B_uniform:.4e}")
print(f"    Tension fw-DR2: {tension_mid:.2f} sigma (midpoint)")
print(f"\n  Evolution DR1 -> DR2:")
print(f"    Central value shift: {w0_desi - w0_dr1:+.3f} (AWAY from framework)")
print(f"    Sigma shrinkage:     {sig_w0/sig_w0_dr1:.2f}x")

# =============================================================================
# Step 7: Pre-registered falsifiable predictions
# =============================================================================

print("\n" + "=" * 78)
print("SECTION E: Pre-Registered Predictions for DR3")
print("=" * 78)

print(f"""
  FALSIFIABLE PREDICTIONS (pre-registered):

  1. w_0 prediction:
     Central: {w0_fw_mid:.3f}
     Band:    [{w0_fw_lo:.3f}, {w0_fw_hi:.3f}]
     Sigma:   {sig_fw:.3f}

  2. w_a prediction:
     Central: {wa_fw:.4f}
     Bound:   |w_a| < 0.02

  3. Exclusion criterion:
     If DR3 measures w_0 < {w0_fw_hi - 3*sig_w0_dr3:.3f} (3-sigma below Keldysh edge + DR3 error):
       Framework EXCLUDED at > 3 sigma

     If DR3 measures w_a < -0.30 at 3 sigma:
       Framework EXCLUDED (w_a ~ 0 is structural)

  4. Confirmation criterion:
     If DR3 measures w_0 in [{w0_fw_lo + sig_w0_dr3:.3f}, {w0_fw_hi - sig_w0_dr3:.3f}]:
       Framework PREFERRED over LCDM (B > 10)

  5. Key discriminant:
     Framework and LCDM diverge maximally on w_a.
     LCDM: w_a = 0 exactly.
     Framework: w_a = {wa_fw:.4f} (essentially 0).
     DESI DR2: w_a = {wa_desi:.2f} +/- {sig_wa:.2f}.
     Both framework and LCDM predict w_a ~ 0.
     If DR3 confirms |w_a| > 0.3: BOTH framework and LCDM have a problem.
""")

# =============================================================================
# Step 8: Summary gate verdict
# =============================================================================

print("=" * 78)
print("SECTION F: Gate Verdict")
print("=" * 78)

# Use the uniform-prior B as the canonical result
B_canonical = B_uniform
gate_verdict = 'PASS' if B_canonical > 1 else ('INFO' if B_canonical > 0.1 else 'FAIL')

# Also compute: at what DR3 w0 does framework get B < 1/100?
exclusion_crossings = find_crossing(w0_scan, B_scan_dr3, 0.01)
exclusion_w0 = exclusion_crossings[0] if exclusion_crossings else None

print(f"\n  Canonical Bayes factor (uniform prior on w_0 band):")
print(f"    B vs LCDM = {B_canonical:.4e}")
print(f"    Gate verdict: {gate_verdict}")
print(f"\n  Summary table:")
print(f"  {'Model':<30s} {'B vs LCDM':<15s} {'Tension (sigma)':<15s}")
print(f"  {'-'*30} {'-'*15} {'-'*15}")
print(f"  {'Zubarev (w0=-0.43)':<30s} {B_zubarev:<15.4e} {tension_zubarev:<15.2f}")
print(f"  {'Midpoint (w0=-0.51)':<30s} {B_mid:<15.4e} {tension_mid:<15.2f}")
print(f"  {'Keldysh (w0=-0.59)':<30s} {B_keldysh:<15.4e} {tension_keldysh:<15.2f}")
print(f"  {'Uniform [-0.43,-0.59]':<30s} {B_uniform:<15.4e} {'':<15s}")
print(f"  {'2D (w0,wa) joint':<30s} {B_2d:<15.4e} {'':<15s}")
print(f"  {'LCDM (w0=-1)':<30s} {'1.000':<15s} {tension_lcdm:<15.2f}")

print(f"\n  DR3 exclusion threshold:")
if exclusion_w0 is not None:
    print(f"    B < 1/100 requires DR3 w_0 < {exclusion_w0:.3f}")
    print(f"    This is {abs(w0_desi - exclusion_w0)/sig_w0_dr3:.1f} sigma from current DR2 central value")
else:
    print(f"    B < 1/100 not reached in scan range")

# Physical interpretation
print(f"\n  Physical interpretation:")
print(f"    The framework predicts w_0 ~ -0.5 (DM/DE from GGE relic).")
print(f"    DESI DR2 measures w_0 = -0.75 -- between framework (-0.5) and LCDM (-1.0).")
print(f"    Framework is CLOSER to DESI than LCDM in w_0 space:")
print(f"      |fw - DESI| = {abs(w0_fw_mid - w0_desi):.3f}")
print(f"      |LCDM - DESI| = {abs(-1.0 - w0_desi):.3f}")
print(f"    Ratio: framework is {abs(-1.0 - w0_desi)/abs(w0_fw_mid - w0_desi):.1f}x closer.")
print(f"    But framework has intrinsic spread ({sig_fw:.3f}) while LCDM is a point.")
print(f"    The Bayes factor accounts for both distance and spread (Occam factor).")

# =============================================================================
# Step 9: Save results
# =============================================================================

results = {
    # Framework predictions (pre-registered)
    'w0_fw_lo': w0_fw_lo,
    'w0_fw_hi': w0_fw_hi,
    'w0_fw_mid': w0_fw_mid,
    'sig_fw': sig_fw,
    'wa_fw': wa_fw,
    'sig_wa_fw': sig_wa_fw,
    # DESI data
    'w0_desi_dr2': w0_desi,
    'sig_w0_dr2': sig_w0,
    'wa_desi_dr2': wa_desi,
    'sig_wa_dr2': sig_wa,
    'w0_desi_dr1': w0_dr1,
    'sig_w0_dr1': sig_w0_dr1,
    # Bayes factors (1D)
    'B_zubarev': B_zubarev,
    'B_midpoint': B_mid,
    'B_keldysh': B_keldysh,
    'B_uniform': B_uniform,
    'B_vs_w0wa_bestfit': B_vs_w0wa,
    # Bayes factor (2D)
    'B_2d': B_2d,
    'rho_corr': rho_corr,
    # Tensions
    'tension_zubarev_sigma': tension_zubarev,
    'tension_midpoint_sigma': tension_mid,
    'tension_keldysh_sigma': tension_keldysh,
    'tension_lcdm_sigma': tension_lcdm,
    # DR3 forecast
    'sig_w0_dr3': sig_w0_dr3,
    'sig_wa_dr3': sig_wa_dr3,
    'B_dr3_at_current_center': B_dr3_at_current,
    'tension_dr3_sigma': tension_dr3,
    'exclusion_w0_dr3': exclusion_w0 if exclusion_w0 is not None else np.nan,
    # DR1 comparison
    'B_dr1': B_dr1,
    'tension_dr1_sigma': tension_dr1,
    # Scan arrays
    'w0_scan': w0_scan,
    'B_scan_dr2': B_scan_dr2,
    'B_scan_dr3': B_scan_dr3,
    # Gate
    'gate_name': np.array(['DESI-DR3-PREP-49']),
    'gate_verdict': np.array([gate_verdict]),
    'B_canonical': B_canonical,
}

np.savez('s49_desi_dr3_prep.npz', **results)
print(f"\n  Saved: s49_desi_dr3_prep.npz")

# =============================================================================
# Step 10: Diagnostic plot
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- Panel (a): Bayes factor vs hypothetical w_0 ---
ax = axes[0, 0]
ax.semilogy(w0_scan, B_scan_dr2, 'b-', lw=2, label=f'DR2 ($\\sigma_{{w_0}}$={sig_w0})')
ax.semilogy(w0_scan, B_scan_dr3, 'r-', lw=2, label=f'DR3 ($\\sigma_{{w_0}}$={sig_w0_dr3})')
ax.axhline(1.0, color='k', ls='--', alpha=0.5, label='B = 1')
ax.axhline(0.1, color='gray', ls=':', alpha=0.5, label='B = 1/10')
ax.axhline(0.01, color='gray', ls='-.', alpha=0.5, label='B = 1/100')
ax.axvline(w0_desi, color='green', ls='--', alpha=0.7, label=f'DESI DR2 ({w0_desi:.3f})')
ax.axvspan(w0_fw_hi, w0_fw_lo, alpha=0.15, color='orange', label=f'Framework band')
ax.axvline(-1.0, color='purple', ls=':', alpha=0.7, label='$\\Lambda$CDM')
ax.set_xlabel('$w_0$ (hypothetical DESI measurement)')
ax.set_ylabel('Bayes factor $B$ (framework / $\\Lambda$CDM)')
ax.set_title('(a) Bayes Factor vs Observed $w_0$')
ax.set_xlim(-1.1, -0.3)
ax.set_ylim(1e-8, 1e8)
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, alpha=0.3)

# --- Panel (b): Tension scan ---
ax = axes[0, 1]
sigma_scan = np.array([0.21, 0.058, 0.035, 0.020, 0.010])
labels_scan = ['DR1', 'DR2', 'DR3', 'DR4?', 'DR5?']
B_at_current = []
for sig_i in sigma_scan:
    lnB_i = log_bayes_factor_1d(w0_desi, sig_i, w0_fw_mid, sig_fw, -1.0)
    B_at_current.append(np.exp(np.clip(lnB_i, -200, 200)))

ax.semilogy(sigma_scan, B_at_current, 'ko-', ms=8, lw=2)
for i, (sig_i, lab) in enumerate(zip(sigma_scan, labels_scan)):
    ax.annotate(lab, (sig_i, B_at_current[i]), textcoords="offset points",
                xytext=(5, 10), fontsize=9)
ax.axhline(1.0, color='k', ls='--', alpha=0.5)
ax.axhline(0.1, color='gray', ls=':', alpha=0.5)
ax.axhline(0.01, color='gray', ls='-.', alpha=0.5)
ax.set_xlabel('$\\sigma_{w_0}$ (measurement precision)')
ax.set_ylabel('$B$ at DESI DR2 central value')
ax.set_title(f'(b) B vs Precision (at $w_0$={w0_desi:.3f})')
ax.invert_xaxis()
ax.grid(True, alpha=0.3)

# --- Panel (c): Gaussian likelihood comparison ---
ax = axes[1, 0]
w0_plot = np.linspace(-1.3, -0.1, 500)
# Framework prior
P_fw = norm.pdf(w0_plot, loc=w0_fw_mid, scale=sig_fw)
P_fw /= P_fw.max()
# DESI DR2 likelihood
P_desi = norm.pdf(w0_plot, loc=w0_desi, scale=sig_w0)
P_desi /= P_desi.max()
# DESI DR3 projected
P_dr3 = norm.pdf(w0_plot, loc=w0_desi, scale=sig_w0_dr3)
P_dr3 /= P_dr3.max()
# LCDM
ax.axvline(-1.0, color='purple', ls='-', lw=3, alpha=0.8, label='$\\Lambda$CDM')

ax.fill_between(w0_plot, P_fw, alpha=0.3, color='orange', label='Framework prior')
ax.plot(w0_plot, P_fw, 'orange', lw=2)
ax.plot(w0_plot, P_desi, 'b-', lw=2, label='DESI DR2')
ax.plot(w0_plot, P_dr3, 'r--', lw=2, label='DESI DR3 (projected)')
ax.set_xlabel('$w_0$')
ax.set_ylabel('Normalized probability')
ax.set_title('(c) Framework vs DESI Likelihoods')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (d): DR3 decision map ---
ax = axes[1, 1]
# Color-code regions by verdict
w0_dr3_scan = np.linspace(-1.0, -0.3, 500)
B_dr3_map = np.zeros_like(w0_dr3_scan)
for i, w0_h in enumerate(w0_dr3_scan):
    lnB_h = log_bayes_factor_1d(w0_h, sig_w0_dr3, w0_fw_mid, sig_fw, -1.0)
    B_dr3_map[i] = np.exp(np.clip(lnB_h, -100, 100))

# Color regions
ax.fill_between(w0_dr3_scan, 0, 1, where=B_dr3_map < 0.01,
                alpha=0.2, color='red', label='Decisive exclusion (B<1/100)')
ax.fill_between(w0_dr3_scan, 0, 1, where=(B_dr3_map >= 0.01) & (B_dr3_map < 0.1),
                alpha=0.2, color='orange', label='Strong exclusion (B<1/10)')
ax.fill_between(w0_dr3_scan, 0, 1, where=(B_dr3_map >= 0.1) & (B_dr3_map < 1),
                alpha=0.2, color='yellow', label='INFO (1/10<B<1)')
ax.fill_between(w0_dr3_scan, 0, 1, where=B_dr3_map >= 1,
                alpha=0.2, color='green', label='Framework preferred (B>1)')

# Mark current DESI DR2 with error bar
ax.errorbar(w0_desi, 0.5, xerr=sig_w0, fmt='bs', ms=10, capsize=5,
            label=f'DR2 ({w0_desi:.3f}$\\pm${sig_w0:.3f})')
ax.errorbar(w0_desi, 0.3, xerr=sig_w0_dr3, fmt='r^', ms=10, capsize=5,
            label=f'DR3 projected ($\\pm${sig_w0_dr3})')

ax.set_xlabel('$w_0$ (DR3 measurement)')
ax.set_ylabel('')
ax.set_title('(d) DR3 Decision Map')
ax.set_yticks([])
ax.set_xlim(-1.0, -0.3)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('s49_desi_dr3_prep.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s49_desi_dr3_prep.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
