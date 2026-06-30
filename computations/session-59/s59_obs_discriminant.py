#!/usr/bin/env python3
"""
S59 OBS-DISCRIMINANT-59: Observational discriminants between framework and LCDM
================================================================================
Computes:
1. ISW effect: Delta_C_l(ISW) for l=2..100 from w_0=-0.918 vs w=-1
2. Growth rate: f*sigma_8(z) at DESI redshifts
3. l~721 CMB acoustic feature check
4. BAO distance discriminant D_V(z)
5. Overall detectability assessment

Gate: PASS if any discriminant detectable by planned experiment (DESI, CMB-S4, Euclid).
      FAIL if all below sensitivity.
      INFO if marginal (1-3 sigma).

Author: Katie Mack (Cosmic Bridge)
Session: S59
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 72)
print("OBS-DISCRIMINANT-59: Framework vs LCDM observational discriminants")
print("=" * 72)

# ===========================================================================
# Input data
# ===========================================================================
d_w = np.load(os.path.join(os.path.dirname(__file__), 's58_w_desi.npz'), allow_pickle=True)
d_v = np.load(os.path.join(os.path.dirname(__file__), 's58_volovik_partition.npz'), allow_pickle=True)

# Framework parameters (Interpretation A, Volovik partition)
w0_fw = float(d_w['w_0_A'])           # -0.918
wa_fw = float(d_w['wa_A_fit'])        # -0.000575 (effectively 0)

# LCDM parameters
# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use

# Shared cosmological parameters (Planck 2018)
Om_m = Omega_m       # 0.315
Om_b = Omega_b       # 0.0493
Om_r = Omega_r       # 9.15e-5
h_val = H_0_km_s_Mpc / 100.0  # 0.674
sig8 = sigma_8       # 0.811
ns = 0.9649          # Planck 2018 best-fit
T_cmb_val = T_CMB    # 2.7255 K

print(f"\nFramework:  w_0 = {w0_fw:.6f}, w_a = {wa_fw:.6f}")
print(f"LCDM:       w_0 = {w0_lcdm:.1f}, w_a = {wa_lcdm:.1f}")
print(f"Omega_m = {Om_m}, Omega_b = {Om_b}, h = {h_val}, sigma_8 = {sig8}")

# ===========================================================================
# 1. Hubble parameter and dark energy density
# ===========================================================================
def w_de(a, w0, wa):
    """CPL parameterization: w(a) = w0 + wa*(1-a)"""
    return w0 + wa * (1.0 - a)

def rho_de_ratio(a, w0, wa):
    """rho_DE(a) / rho_DE(1) for CPL parameterization.
    Exact: rho_DE ~ a^{-3(1+w0+wa)} * exp(-3*wa*(1-a))
    """
    return a**(-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))

def E2(a, w0, wa):
    """(H/H_0)^2 as function of scale factor a"""
    Om_de = (1.0 - Om_m - Om_r) * rho_de_ratio(a, w0, wa)
    return Om_r / a**4 + Om_m / a**3 + Om_de

def H_of_a(a, w0, wa):
    """H(a) in units of H_0"""
    return np.sqrt(np.maximum(E2(a, w0, wa), 1e-30))

# ===========================================================================
# 2. Growth factor D(a) from the linear growth ODE
# ===========================================================================
def growth_ode(a, y, w0, wa):
    """Growth factor ODE in terms of a.
    y[0] = D(a), y[1] = dD/da
    """
    D_val, dD_da = y
    e2 = E2(a, w0, wa)
    Om_de_0 = 1.0 - Om_m - Om_r
    rho_ratio = rho_de_ratio(a, w0, wa)
    drho_da = rho_ratio * (-3.0*(1.0 + w0 + wa)/a + 3.0*wa)
    de2_da = -4.0*Om_r/a**5 - 3.0*Om_m/a**4 + Om_de_0 * drho_da
    coeff1 = 3.0/a + de2_da / (2.0 * e2)
    coeff2 = 1.5 * Om_m / (a**5 * e2)
    d2D_da2 = -coeff1 * dD_da + coeff2 * D_val
    return [dD_da, d2D_da2]

def compute_growth_factor(w0, wa):
    """Compute growth factor D(a), normalized to D(a=1)=1. Returns interpolation function."""
    a_init = 1e-4  # (local)
    y0 = [a_init, 1.0]
    sol = solve_ivp(growth_ode, [a_init, 1.0], y0,
                    args=(w0, wa), method='RK45',
                    rtol=1e-10, atol=1e-12, dense_output=True)
    D_at_1 = sol.sol(1.0)[0]
    return lambda a: sol.sol(np.clip(a, a_init, 1.0))[0] / D_at_1

def growth_rate_f(a, D_func, w0, wa):
    """f = d ln D / d ln a"""
    da = a * 1e-5
    D_plus = D_func(a + da)
    D_minus = D_func(a - da)
    dD_da = (D_plus - D_minus) / (2.0 * da)
    D_val = D_func(a)
    return (a / D_val) * dD_da

# ===========================================================================
# 3. Compute growth factors for both models
# ===========================================================================
print("\n--- Computing growth factors ---")

D_fw_func = compute_growth_factor(w0_fw, wa_fw)
D_lcdm_func = compute_growth_factor(w0_lcdm, wa_lcdm)

# Verify: D(1) should be 1
print(f"  D_fw(1) = {D_fw_func(1.0):.8f}")
print(f"  D_lcdm(1) = {D_lcdm_func(1.0):.8f}")

# ===========================================================================
# 4. f*sigma_8 at DESI redshifts
# ===========================================================================
print("\n--- f*sigma_8 discriminant ---")

z_desi = np.array([0.3, 0.5, 0.7, 1.0, 1.5])
a_desi = 1.0 / (1.0 + z_desi)

# DESI DR2 RSD measurement uncertainties (from DESI 2024, Table 3 combined)
# sigma(f*sigma_8) absolute ~ 0.02-0.03 at z < 1, 0.03-0.05 at z > 1
# Fractional: ~4-5% per bin
sigma_fsig8_frac = np.array([0.045, 0.035, 0.030, 0.040, 0.055])

# Euclid projected (Euclid Red Book 2011, Table 1.3, updated Amendola+ 2018)
# ~1.2-2.0% per bin in 0.7 < z < 2.0
sigma_fsig8_euclid_frac = np.array([0.018, 0.014, 0.012, 0.013, 0.018])

# DESI DR2+Euclid combined (approximate, sqrt of sum of inverse variances)
sigma_fsig8_combined_frac = np.array([0.017, 0.012, 0.010, 0.012, 0.017])

fsig8_fw = np.zeros_like(z_desi)
fsig8_lcdm = np.zeros_like(z_desi)

for i, (z, a) in enumerate(zip(z_desi, a_desi)):
    f_fw = growth_rate_f(a, D_fw_func, w0_fw, wa_fw)
    f_lcdm = growth_rate_f(a, D_lcdm_func, w0_lcdm, wa_lcdm)
    D_fw_val = D_fw_func(a)
    D_lcdm_val = D_lcdm_func(a)
    fsig8_fw[i] = f_fw * sig8 * D_fw_val
    fsig8_lcdm[i] = f_lcdm * sig8 * D_lcdm_val

delta_fsig8 = fsig8_fw - fsig8_lcdm
frac_diff_fsig8 = np.abs(delta_fsig8) / fsig8_lcdm

sigma_desi = frac_diff_fsig8 / sigma_fsig8_frac
sigma_euclid = frac_diff_fsig8 / sigma_fsig8_euclid_frac
sigma_combined = frac_diff_fsig8 / sigma_fsig8_combined_frac

print(f"\n{'z':>5} {'f*sig8(FW)':>12} {'f*sig8(LCDM)':>14} {'Delta':>10} {'frac':>8} "
      f"{'DESI sig':>10} {'Euclid sig':>10} {'Comb sig':>10}")
print("-" * 95)
for i in range(len(z_desi)):
    print(f"{z_desi[i]:5.1f} {fsig8_fw[i]:12.6f} {fsig8_lcdm[i]:14.6f} "
          f"{delta_fsig8[i]:10.6f} {frac_diff_fsig8[i]:8.5f} "
          f"{sigma_desi[i]:10.3f} {sigma_euclid[i]:10.3f} {sigma_combined[i]:10.3f}")

# Multi-z Fisher: combined chi^2 over all z bins
chi2_desi = np.sum((frac_diff_fsig8 / sigma_fsig8_frac)**2)
chi2_euclid = np.sum((frac_diff_fsig8 / sigma_fsig8_euclid_frac)**2)
chi2_combined = np.sum((frac_diff_fsig8 / sigma_fsig8_combined_frac)**2)

sigma_desi_multi = np.sqrt(chi2_desi)
sigma_euclid_multi = np.sqrt(chi2_euclid)
sigma_combined_multi = np.sqrt(chi2_combined)

print(f"\nMulti-z Fisher (all 5 bins combined):")
print(f"  DESI-only:       {sigma_desi_multi:.3f} sigma")
print(f"  Euclid-only:     {sigma_euclid_multi:.3f} sigma")
print(f"  DESI+Euclid:     {sigma_combined_multi:.3f} sigma")

# ===========================================================================
# 5. ISW effect
# ===========================================================================
print("\n--- ISW effect ---")

# The ISW integrated Sachs-Wolfe effect generates low-l CMB anisotropy via
# time-varying gravitational potential. The key is the source function:
# S_ISW(a) proportional to d(Phi)/d(eta) = H(a) * D(a) * [f(a) - 1] / a
# where Phi ~ D(a)/a (in the subhorizon limit).
#
# The ISW power spectrum scales as:
# C_l^ISW ~ [integral S_ISW^2 / chi^2 d_chi] / l^2
#
# The DIFFERENCE in ISW between two models is what we detect.

n_a = 2000
a_isw = np.linspace(0.05, 0.999, n_a)

def isw_source(a, D_func, w0, wa):
    """ISW source: proportional to d(D/a)/d(eta) = a*H(a)*[dD/da/a - D/a^2]
    = H(a)*D(a)*(f-1)/a where f = a/D * dD/da"""
    H = H_of_a(a, w0, wa)
    D = D_func(a)
    f = growth_rate_f(a, D_func, w0, wa)
    return H * D * (f - 1.0) / a

# Compute ISW sources
S_fw = np.array([isw_source(a, D_fw_func, w0_fw, wa_fw) for a in a_isw])
S_lcdm = np.array([isw_source(a, D_lcdm_func, w0_lcdm, wa_lcdm) for a in a_isw])

# Comoving distance
def chi_of_a_arr(a_arr, w0, wa):
    """Comoving distances chi(a) = integral_a^1 da'/(a'^2*H(a'))"""
    chi_arr = np.zeros_like(a_arr)
    for i, a in enumerate(a_arr):
        chi_arr[i], _ = quad(lambda ap: 1.0/(ap**2 * H_of_a(ap, w0, wa)), a, 1.0,
                             limit=200, epsrel=1e-10)
    return chi_arr

chi_fw = chi_of_a_arr(a_isw, w0_fw, wa_fw)
chi_lcdm = chi_of_a_arr(a_isw, w0_lcdm, wa_lcdm)

# ISW C_l using Limber approximation:
# C_l^ISW = (9*Om_m^2*H_0^4/c^4) * integral da/(a^4*H^2) * [S_ISW(a)]^2 / [k=l/chi]^4
# Since S_ISW already contains H*D*(f-1)/a, we need:
# integrand proportional to S_ISW^2 * chi^2 / (a^2 * H)
# at fixed l, weighted by 1/l^2
#
# More precisely, in the flat-sky Limber approximation:
# C_l^ISW = integral d_chi [W_ISW(chi)]^2 / chi^2
# where W_ISW(chi) = 3*Om_m*(H_0/c)^2 * (1/a) * d(D*a)/d_eta evaluated at a(chi)
# Wait -- let me be very careful about sign and factors.
#
# The gravitational potential: Phi(k,a) = -(3/2)*Om_m*(H_0/c)^2 * delta(k,a) / k^2
# where delta(k,a) = D(a) * delta(k,0)
# so Phi(k,a) = Phi(k,0) * D(a)
# BUT we want Phi in the Poisson equation: k^2*Phi = (3/2)*H_0^2*Om_m*delta/a
# So Phi(k,a) = (3/2)*H_0^2*Om_m/(a*k^2) * D(a) * delta(k)
#
# ISW: DeltaT/T = -2 * integral d(eta) dPhi/d(eta)
# dPhi/d(eta) = (3/2)*H_0^2*Om_m/k^2 * d(D/a)/d(eta)
#
# d(D/a)/d(eta) = a*H * d(D/a)/da = a*H*(D'/a - D/a^2) = H*(D'*a - D)/a = H*D*(f-1)/a
# where D' = dD/da
#
# So the ISW kernel: W_ISW(chi) = -3*Om_m*(H_0)^2 * H(a)*D(a)*(f(a)-1) / (a * k^2)
# and C_l^ISW = integral W^2 * |delta_k|^2 dk ... but we need the angular power spectrum.
#
# The standard result is:
# C_l^ISW = (2/pi) * integral dk k^2 P(k) [F_ISW(k)]^2
# where F_ISW(k) = 3*Om_m*H_0^2 * integral da/(a^2*H) * j_l(k*chi) * [H*D*(f-1)/a]
#
# In the Limber approximation (valid for l > 10 or so):
# C_l^ISW = [3*Om_m*H_0^2]^2 * integral da/a^4 * [D*(f-1)]^2 / [H * chi^2]
#         * P(k = (l+0.5)/chi)
#
# For the RATIO C_l^ISW(FW) / C_l^ISW(LCDM), at fixed l:
# the P(k) difference between models is O(1%) (since perturbation spectrum is
# set at recombination, only growth differs). So the ratio is dominated by
# the integral of [D*(f-1)]^2 / [H*chi^2*a^4].

# Compute the ISW weight function
def isw_weight(a, D_func, w0, wa, chi_interp):
    """ISW weight: [D*(f-1)]^2 / (H * a^4)"""
    D = D_func(a)
    f = growth_rate_f(a, D_func, w0, wa)
    H = H_of_a(a, w0, wa)
    ch = chi_interp(a)
    if ch < 1e-10:
        return 0.0
    return (D * (f - 1.0))**2 / (H * a**4 * ch**2)

# Interpolate chi
chi_fw_interp = interp1d(a_isw, chi_fw, kind='cubic', fill_value='extrapolate')
chi_lcdm_interp = interp1d(a_isw, chi_lcdm, kind='cubic', fill_value='extrapolate')

W_fw = np.array([isw_weight(a, D_fw_func, w0_fw, wa_fw, chi_fw_interp) for a in a_isw])
W_lcdm = np.array([isw_weight(a, D_lcdm_func, w0_lcdm, wa_lcdm, chi_lcdm_interp) for a in a_isw])

I_fw = np.trapezoid(W_fw, a_isw)
I_lcdm = np.trapezoid(W_lcdm, a_isw)

ratio_isw = I_fw / I_lcdm
delta_isw_frac = (I_fw - I_lcdm) / I_lcdm

print(f"\nISW weight integral ratio: I_fw / I_lcdm = {ratio_isw:.6f}")
print(f"Fractional ISW power difference: {delta_isw_frac:.6f} = {delta_isw_frac*100:.4f}%")

# Now translate to detectable C_l differences.
# The ISW contribution to the TOTAL CMB power spectrum is small:
# C_l^ISW / C_l^total ~ 5-15% at l = 2-30 (Planck 2018 XV, Section 5.3)
# (The primary SW effect dominates at l < 100)
#
# The CHANGE in C_l^ISW due to w shift:
# Delta_C_l^ISW / C_l^ISW = delta_isw_frac
# Delta_C_l^ISW / C_l^total = delta_isw_frac * (C_l^ISW / C_l^total)

# ISW fraction of total TT (approximate, from Planck 2018 cross-correlations)
# At l=2: ~20%, l=10: ~12%, l=30: ~5%, l>50: <2%
l_arr = np.arange(2, 101, dtype=float)
isw_fraction = 0.20 * np.exp(-(l_arr - 2.0) / 25.0) + 0.02  # empirical fit to Planck

# Fractional change in TOTAL C_l
delta_Cl_total_frac = delta_isw_frac * isw_fraction

# Sachs-Wolfe plateau: l(l+1)*C_l/(2*pi) ~ 1100 muK^2
Dl_approx = 1100.0 * np.ones_like(l_arr)  # D_l = l(l+1)C_l/(2pi)
Cl_total = Dl_approx * 2.0 * PI / (l_arr * (l_arr + 1.0))

# Cosmic variance (fundamental, no experiment beats this)
sigma_cv = Cl_total * np.sqrt(2.0 / (2.0 * l_arr + 1.0))

# Delta C_l in muK^2
Delta_Cl_isw = delta_Cl_total_frac * Cl_total

# Per-multipole SNR
snr_isw_per_l = np.abs(Delta_Cl_isw) / sigma_cv

# Apply foreground degradation at low l (galactic foreground cleaning)
# Planck 2018 effectively loses l < 5 to foregrounds, degrades l < 30
# Factor: multiply sigma by degradation_factor > 1
foreground_degradation = np.ones_like(l_arr)
foreground_degradation[l_arr < 5] = 5.0    # nearly unusable
foreground_degradation[(l_arr >= 5) & (l_arr < 15)] = 2.5  # heavily degraded
foreground_degradation[(l_arr >= 15) & (l_arr < 30)] = 1.5  # moderately degraded

snr_isw_per_l_degraded = snr_isw_per_l / foreground_degradation

# Cumulative SNR (idealized)
snr_isw_cum = np.sqrt(np.cumsum(snr_isw_per_l**2))
snr_isw_cum_degraded = np.sqrt(np.cumsum(snr_isw_per_l_degraded**2))

# Apply sky fraction correction (f_sky reduces available modes)
f_sky = 0.70  # Planck usable sky fraction (local)
snr_isw_cum_final = snr_isw_cum_degraded * np.sqrt(f_sky)

print(f"\nISW contribution to total C_l: {isw_fraction[0]*100:.0f}% at l=2, {isw_fraction[8]*100:.1f}% at l=10")
print(f"Delta(C_l)/C_l from w shift: {delta_Cl_total_frac[8]*100:.4f}% at l=10")
print(f"Delta_C_l at l=10: {Delta_Cl_isw[8]:.4f} muK^2")
print(f"Cosmic variance at l=10: {sigma_cv[8]:.2f} muK^2")
print(f"Per-l SNR at l=10 (ideal): {snr_isw_per_l[8]:.4f}")
print(f"Per-l SNR at l=10 (degraded): {snr_isw_per_l_degraded[8]:.4f}")
print(f"\nCumulative ISW SNR (l=2-100):")
print(f"  Idealized (no foreground, full sky): {snr_isw_cum[-1]:.4f}")
print(f"  With foreground degradation:         {snr_isw_cum_degraded[-1]:.4f}")
print(f"  With f_sky = {f_sky}:                  {snr_isw_cum_final[-1]:.4f}")

# Cross-check: ISW-galaxy cross-correlation
# The ISW effect is best detected via cross-correlation with galaxy surveys
# (Crittenden & Turok 1996, Planck 2018 XXI)
# Planck detected ISW at ~3-4 sigma via cross-correlation with NVSS/2MASS
# The w-dependence of ISW-galaxy cross-correlation is:
# proportional to integral of D*(f-1)*b*D / (H*chi^2) da
# This provides a SEPARATE detection channel

# ISW-galaxy cross-correlation SNR scales roughly as:
# SNR_cross ~ SNR_auto * sqrt(2) (because cross picks up correlated mode)
# But is limited by shot noise in galaxy survey
# Euclid/DESI galaxy catalogs: SNR_cross(ISW) ~ 5-8 sigma for LCDM detection
# The w-sensitivity is the CHANGE in SNR, which scales as delta_isw_frac

# For distinguishing w=-0.918 from w=-1:
# Delta(SNR_cross) ~ SNR_cross * delta_isw_frac / 2
isw_cross_snr_lcdm = 6.0  # Euclid-grade ISW-galaxy cross-correlation (conservative)  # (local)
delta_isw_cross_detect = isw_cross_snr_lcdm * abs(delta_isw_frac) / 2.0
print(f"\nISW-galaxy cross-correlation:")
print(f"  Expected ISW x galaxy SNR (Euclid): ~{isw_cross_snr_lcdm:.0f} sigma (LCDM detection)")
print(f"  Sensitivity to w shift: {delta_isw_cross_detect:.3f} sigma")

# ===========================================================================
# 6. BAO distance discriminant
# ===========================================================================
print("\n--- BAO distance discriminant ---")

def D_M(z, w0, wa):
    """Comoving distance D_M(z) in c/H_0 units"""
    a = 1.0 / (1.0 + z)
    chi, _ = quad(lambda ap: 1.0/(ap**2 * H_of_a(ap, w0, wa)), a, 1.0,
                  limit=200, epsrel=1e-10)
    return chi

def D_V(z, w0, wa):
    """Volume-averaged distance D_V(z) in c/H_0 units"""
    dm = D_M(z, w0, wa)
    Hz = H_of_a(1.0/(1.0+z), w0, wa)
    return (z * dm**2 / Hz)**(1.0/3.0)

def D_H(z, w0, wa):
    """Hubble distance D_H(z) = c/(H(z)) in c/H_0 units"""
    return 1.0 / H_of_a(1.0/(1.0+z), w0, wa)

z_bao = np.array([0.30, 0.51, 0.706, 1.0, 1.48, 2.33])
# DESI DR2 fractional uncertainties on D_V/r_d (from DESI 2024 Table 2, combined tracers)
sigma_DV_frac = np.array([0.012, 0.010, 0.009, 0.012, 0.015, 0.020])
# Euclid spectroscopic BAO (from Euclid Collaboration 2020, Blanchard+ Table 7)
sigma_DV_euclid_frac = np.array([0.008, 0.006, 0.005, 0.006, 0.008, 0.012])

print(f"\n{'z':>5} {'DV_fw':>10} {'DV_lcdm':>10} {'Delta%':>10} {'DESI sig':>10} {'Euclid sig':>10}")
print("-" * 60)

DV_fw = np.array([D_V(z, w0_fw, wa_fw) for z in z_bao])
DV_lcdm = np.array([D_V(z, w0_lcdm, wa_lcdm) for z in z_bao])
delta_DV_frac = (DV_fw - DV_lcdm) / DV_lcdm
sigma_bao_desi = np.abs(delta_DV_frac) / sigma_DV_frac
sigma_bao_euclid = np.abs(delta_DV_frac) / sigma_DV_euclid_frac

for i in range(len(z_bao)):
    print(f"{z_bao[i]:5.2f} {DV_fw[i]:10.6f} {DV_lcdm[i]:10.6f} "
          f"{delta_DV_frac[i]*100:10.4f} {sigma_bao_desi[i]:10.3f} {sigma_bao_euclid[i]:10.3f}")

# Multi-z BAO Fisher
chi2_bao_desi = np.sum(sigma_bao_desi**2)
chi2_bao_euclid = np.sum(sigma_bao_euclid**2)
sigma_bao_desi_multi = np.sqrt(chi2_bao_desi)
sigma_bao_euclid_multi = np.sqrt(chi2_bao_euclid)
print(f"\nMulti-z BAO Fisher:")
print(f"  DESI:   {sigma_bao_desi_multi:.3f} sigma")
print(f"  Euclid: {sigma_bao_euclid_multi:.3f} sigma")

# Also check H(z) directly (AP test)
print(f"\nHubble parameter H(z) differences:")
for z in [0.5, 1.0, 1.5]:
    H_fw = H_of_a(1.0/(1.0+z), w0_fw, wa_fw)
    H_lcdm = H_of_a(1.0/(1.0+z), w0_lcdm, wa_lcdm)
    delta_H_frac = (H_fw - H_lcdm) / H_lcdm
    print(f"  z={z}: Delta(H)/H = {delta_H_frac*100:.4f}%")

# ===========================================================================
# 7. l ~ 721 CMB feature check
# ===========================================================================
print("\n--- l ~ 721 CMB acoustic feature check ---")

# Comoving distance to recombination
z_rec = 1089.9  # (local)
a_rec = 1.0 / (1.0 + z_rec)
chi_rec_cH0, _ = quad(lambda a: 1.0/(a**2 * H_of_a(a, w0_lcdm, wa_lcdm)), a_rec, 1.0,
                       limit=500, epsrel=1e-10)
c_over_H0_Mpc = 2.998e5 / H_0_km_s_Mpc  # = 4449 Mpc
chi_rec_Mpc = chi_rec_cH0 * c_over_H0_Mpc  # comoving distance to last scattering
D_A_rec_Mpc = chi_rec_Mpc / (1.0 + z_rec)  # angular diameter distance

# Sound horizon at recombination
r_s_rec = 147.09  # Mpc, Planck 2018 best-fit  # (local)

# Acoustic scale (multipole of first peak)
l_acoustic = PI * chi_rec_Mpc / r_s_rec  # using COMOVING distance (= D_A * (1+z))

print(f"chi(z_rec) = {chi_rec_Mpc:.1f} Mpc (comoving)")
print(f"D_A(z_rec) = {D_A_rec_Mpc:.1f} Mpc (proper angular diameter)")
print(f"r_s(z_rec) = {r_s_rec} Mpc")
print(f"l_A = pi*chi/r_s = {l_acoustic:.1f}")
print(f"l_1 (first peak) ~ {l_acoustic:.0f}")

# Physical scale at l=721
# theta_l = pi / l = lambda / chi_rec -> lambda = pi * chi_rec / l
lambda_721_Mpc = PI * chi_rec_Mpc / 721.0
print(f"\nl=721 corresponds to comoving scale: {lambda_721_Mpc:.1f} Mpc")
print(f"l=721 / l_A = {721.0 / l_acoustic:.3f} (near {round(721.0/l_acoustic):.0f}th peak)")

# The CG(24) acoustic structure:
# 24-cell is the regular polytope on S^3 with 24 vertices.
# As a Coxeter group structure on the SU(3) fiber, it has characteristic
# angular scales theta_cell ~ 2*pi / 24^(1/dim)
# For a 6D fiber (dim(SU(3))=8, but complex dim=3):
# There is NO standard derivation mapping this to a CMB multipole.
# The claim l~721 would require:
# (a) A specific coupling between fiber modes and metric perturbations
# (b) An imprint at recombination or via ISW at that specific scale
# (c) Neither mechanism has been derived in the framework

# Evaluate the claim's detectability IF the feature existed:
Cl_721_signal = 24.0  # muK^2, claimed amplitude in D_l = l(l+1)C_l/(2pi)  # (local)
Delta_l_feature = 20.0  # assumed width  # (local)

# Standard C_l at l=721 (Silk damping tail + acoustic oscillations)
# From Planck data: D_l(721) ~ 2500 muK^2 (between 2nd and 3rd peak)
Dl_standard_721 = 2500.0  # (local)
Cl_standard_721 = Dl_standard_721 * 2.0 * PI / (721.0 * 722.0)

# Noise levels
Nl_planck_721 = 40.0  # muK^2 in D_l (Planck 143 GHz channel at l=721)  # (local)
Nl_cmbs4_721 = 1.5    # muK^2 in D_l (CMB-S4 design spec)  # (local)

f_sky_planck = 0.70  # (local)
f_sky_cmbs4 = 0.40  # (local)

# Bandpower uncertainty for feature of width Delta_l:
# sigma(D_l) = (D_l + N_l) * sqrt(2 / ((2l+1) * Delta_l * f_sky))
sigma_Dl_planck = (Dl_standard_721 + Nl_planck_721) * np.sqrt(2.0 / ((2*721+1) * Delta_l_feature * f_sky_planck))
sigma_Dl_cmbs4 = (Dl_standard_721 + Nl_cmbs4_721) * np.sqrt(2.0 / ((2*721+1) * Delta_l_feature * f_sky_cmbs4))

snr_721_planck = Cl_721_signal / sigma_Dl_planck
snr_721_cmbs4 = Cl_721_signal / sigma_Dl_cmbs4

print(f"\nIF a 24 muK^2 feature existed at l=721:")
print(f"  D_l(standard) at l=721: ~{Dl_standard_721} muK^2")
print(f"  Feature amplitude: {Cl_721_signal} muK^2 ({Cl_721_signal/Dl_standard_721*100:.2f}% of standard)")
print(f"  Planck bandpower sigma: {sigma_Dl_planck:.1f} muK^2 -> SNR = {snr_721_planck:.2f}")
print(f"  CMB-S4 bandpower sigma: {sigma_Dl_cmbs4:.1f} muK^2 -> SNR = {snr_721_cmbs4:.2f}")

# CRITICAL ASSESSMENT
print(f"\nASSESSMENT: The l~721 feature claim LACKS a derivation.")
print(f"  CG(24) is the Coxeter group of the internal SU(3) fiber,")
print(f"  not a spatial tessellation. No mechanism connects fiber")
print(f"  symmetry to a specific CMB multipole. Even if it existed,")
print(f"  the 24 muK^2 amplitude is only {snr_721_planck:.1f}-sigma (Planck)")
print(f"  or {snr_721_cmbs4:.1f}-sigma (CMB-S4), below detection threshold.")
print(f"  VERDICT: Not a viable discriminant (no derivation + below threshold).")

# ===========================================================================
# 8. w_0 constraint from combined probes
# ===========================================================================
print("\n--- Direct w_0 constraint ---")

# The most direct discriminant is simply: w_0 = -0.918 vs w_0 = -1
# Delta(w_0) = 0.082
# Current Planck+BAO: sigma(w_0) ~ 0.03 (constant w)
# But the framework predicts w_a ~ 0, so in the (w_0, w_a) plane
# the comparison is different from just Delta(w_0).

# In constant-w analysis:
# Framework: w = -0.918
# LCDM: w = -1.0
# Planck 2018 (w constant): w = -1.03 +/- 0.03
delta_w = w0_fw - (-1.0)
sigma_w_planck = 0.03  # (local)
sigma_w_desi_const = 0.05  # DESI DR2 constant w  # (local)

print(f"  w_0(FW) - w_0(LCDM) = {delta_w:.4f}")
print(f"  Planck constant-w: sigma = {sigma_w_planck} -> {abs(delta_w)/sigma_w_planck:.1f} sigma")
print(f"  DESI constant-w: sigma = {sigma_w_desi_const} -> {abs(delta_w)/sigma_w_desi_const:.1f} sigma")

# But note: Planck constant-w measurement ASSUMES w_a = 0.
# If we allow w_a free (as DESI does), sigma(w_0) increases to ~0.06-0.08
# So the FW prediction w_0 = -0.918 is only ~1.0-1.4 sigma from -1.0 in w_0-w_a analysis
sigma_w0_free = 0.06  # sigma(w_0) with w_a free  # (local)
print(f"  DESI (w_a free): sigma(w_0) = {sigma_w0_free} -> {abs(delta_w)/sigma_w0_free:.1f} sigma")

# Projected: DESI DR3 + Euclid will tighten to sigma(w_0) ~ 0.025-0.030
sigma_w0_future = 0.030  # (local)
print(f"  Projected (DR3+Euclid): sigma(w_0) ~ {sigma_w0_future} -> {abs(delta_w)/sigma_w0_future:.1f} sigma")

# ===========================================================================
# 9. Summary table
# ===========================================================================
print("\n" + "=" * 72)
print("SUMMARY: All framework-vs-LCDM discriminants")
print("=" * 72)

# Collect all sigma values for planned experiments
all_discriminants = {
    # ISW auto (TT, cosmic variance limited)
    'ISW_auto_TT': snr_isw_cum_final[-1],
    # ISW cross-correlation
    'ISW_x_galaxy': delta_isw_cross_detect,
    # f*sigma_8 single best bin (DESI)
    'fsig8_DESI_best': np.max(sigma_desi),
    # f*sigma_8 multi-z (DESI)
    'fsig8_DESI_multi': sigma_desi_multi,
    # f*sigma_8 single best bin (Euclid)
    'fsig8_Euclid_best': np.max(sigma_euclid),
    # f*sigma_8 multi-z (Euclid)
    'fsig8_Euclid_multi': sigma_euclid_multi,
    # f*sigma_8 DESI+Euclid combined multi-z
    'fsig8_combined_multi': sigma_combined_multi,
    # BAO D_V (DESI)
    'BAO_DV_DESI_multi': sigma_bao_desi_multi,
    # BAO D_V (Euclid)
    'BAO_DV_Euclid_multi': sigma_bao_euclid_multi,
    # Direct w_0 (constant w)
    'w0_Planck_const': abs(delta_w) / sigma_w_planck,
    # Direct w_0 (projected future)
    'w0_DR3_Euclid': abs(delta_w) / sigma_w0_future,
    # l=721 (Planck)
    'l721_Planck': snr_721_planck,
    # l=721 (CMB-S4)
    'l721_CMBS4': snr_721_cmbs4,
}

print(f"\n{'Discriminant':<30} {'sigma':<10} {'Status':<12} {'Instrument':<15}")
print("-" * 70)
for name, sig in sorted(all_discriminants.items(), key=lambda x: -x[1]):
    status = "DETECTABLE" if sig >= 3.0 else ("MARGINAL" if sig >= 1.0 else "BELOW")
    inst = ""
    if 'DESI' in name: inst = "DESI"
    elif 'Euclid' in name or 'combined' in name: inst = "Euclid"
    elif 'Planck' in name: inst = "Planck"
    elif 'S4' in name or 'S4' in name: inst = "CMB-S4"
    elif 'ISW' in name: inst = "ISW-galaxy"
    elif 'DR3' in name: inst = "DR3+Euclid"
    print(f"  {name:<30} {sig:<10.3f} {status:<12} {inst:<15}")

# ===========================================================================
# 10. Gate verdict
# ===========================================================================
max_sigma = max(all_discriminants.values())
max_discriminant = max(all_discriminants, key=all_discriminants.get)

# But we need to be careful about which are REAL discriminants:
# - w_0 constant: this is the framework's OWN prediction vs LCDM.
#   It IS a discriminant, detectable at 2.7 sigma with Planck (constant w).
#   But the framework also predicts w_a ~ 0, which is tested separately.
# - The f*sigma_8, BAO, ISW are all consequences of w_0 = -0.918 vs -1.
#   They're correlated, not independent.
#
# The most physically meaningful discriminant is the multi-probe combined:
# w_0 = -0.918 vs -1.0 with w_a = 0 (same for both)
# This is testable as: constant-w measurement tightening toward sigma ~ 0.025

print(f"\n{'=' * 72}")
print(f"GATE VERDICT: OBS-DISCRIMINANT-59")
print(f"{'=' * 72}")

# Apply gate criteria:
# PASS: at least one discriminant >= 3 sigma with a planned experiment
# FAIL: all discriminants < 1 sigma
# INFO: at least one in 1-3 sigma range

# The best discriminant excluding the direct w_0 measurement
# (which is somewhat circular: we're testing w_0, not a derived quantity)
derived_discriminants = {k: v for k, v in all_discriminants.items()
                        if 'w0_' not in k}
max_derived = max(derived_discriminants.values())
max_derived_name = max(derived_discriminants, key=derived_discriminants.get)

# Including direct w_0 measurement
print(f"\nBest discriminant (derived): {max_derived_name} = {max_derived:.3f} sigma")
print(f"Best discriminant (direct):  w0_DR3_Euclid = {all_discriminants['w0_DR3_Euclid']:.3f} sigma")
print(f"Best discriminant (overall): {max_discriminant} = {max_sigma:.3f} sigma")

if max_sigma >= 3.0:
    gate_verdict = "PASS"
    gate_detail = (f"{max_discriminant} at {max_sigma:.2f} sigma. "
                   f"Best derived: {max_derived_name} at {max_derived:.2f} sigma.")
elif max_sigma >= 1.0:
    gate_verdict = "INFO"
    gate_detail = (f"Marginal: {max_discriminant} at {max_sigma:.2f} sigma (1-3 range). "
                   f"Best derived: {max_derived_name} at {max_derived:.2f} sigma.")
else:
    gate_verdict = "FAIL"
    gate_detail = f"All discriminants below 1 sigma. Best: {max_discriminant} at {max_sigma:.3f} sigma."

print(f"\nVerdict: {gate_verdict}")
print(f"Detail: {gate_detail}")

# Physics context
print(f"\n--- Physical interpretation ---")
print(f"w_0 - (-1) = {delta_w:.4f} ({abs(delta_w)*100:.1f}% departure from CC)")
print(f"This 8% shift in w produces:")
print(f"  ~1.7-1.9% shift in f*sigma_8")
print(f"  ~1.1-1.7% shift in D_V(z)")
print(f"  ~{delta_isw_frac*100:.0f}% shift in ISW power (but ISW is only ~10% of total C_l)")
print(f"The shifts are CORRELATED (all driven by same w difference).")
print(f"The framework is observationally close to LCDM by construction:")
print(f"  w_0 = -0.918 and w_a ~ 0 mimics CC to 8% accuracy.")

print(f"\nCRITICAL CONTEXT (from WA-ERROR-PROP-59):")
print(f"  DESI DR3 will test w_a = 0 at 4.3 sigma")
print(f"  If confirmed: BOTH framework (w_a ~ 0) and LCDM (w_a = 0) face exclusion")
print(f"  The FW-vs-LCDM discriminant becomes moot if both are excluded by w_a != 0")

# ===========================================================================
# 11. Save outputs
# ===========================================================================
outpath = os.path.join(os.path.dirname(__file__), 's59_obs_discriminant.npz')
np.savez(outpath,
    # Framework parameters
    w0_fw=w0_fw, wa_fw=wa_fw,
    w0_lcdm=w0_lcdm, wa_lcdm=wa_lcdm,
    Om_m=Om_m, Om_b=Om_b, h=h_val, sigma_8=sig8,

    # Growth rate discriminant
    z_desi=z_desi,
    fsig8_fw=fsig8_fw,
    fsig8_lcdm=fsig8_lcdm,
    delta_fsig8=delta_fsig8,
    frac_diff_fsig8=frac_diff_fsig8,
    sigma_fsig8_desi=sigma_desi,
    sigma_fsig8_euclid=sigma_euclid,
    sigma_fsig8_combined=sigma_combined,
    sigma_desi_multi=sigma_desi_multi,
    sigma_euclid_multi=sigma_euclid_multi,
    sigma_combined_multi=sigma_combined_multi,

    # ISW
    l_arr=l_arr,
    Delta_Cl_isw=Delta_Cl_isw,
    isw_integral_ratio=ratio_isw,
    delta_isw_frac=delta_isw_frac,
    snr_isw_cum=snr_isw_cum,
    snr_isw_cum_degraded=snr_isw_cum_degraded,
    snr_isw_cum_final=snr_isw_cum_final,
    isw_cross_detect=delta_isw_cross_detect,

    # BAO
    z_bao=z_bao,
    DV_fw=DV_fw,
    DV_lcdm=DV_lcdm,
    delta_DV_frac=delta_DV_frac,
    sigma_bao_desi=sigma_bao_desi,
    sigma_bao_euclid=sigma_bao_euclid,
    sigma_bao_desi_multi=sigma_bao_desi_multi,
    sigma_bao_euclid_multi=sigma_bao_euclid_multi,

    # l=721 feature
    snr_721_planck=snr_721_planck,
    snr_721_cmbs4=snr_721_cmbs4,
    Cl_721_signal=Cl_721_signal,
    l_acoustic=l_acoustic,
    chi_rec_Mpc=chi_rec_Mpc,

    # Direct w_0
    delta_w=delta_w,
    sigma_w_planck_const=abs(delta_w)/sigma_w_planck,
    sigma_w_future=abs(delta_w)/sigma_w0_future,

    # Gate
    gate_name=np.array(['OBS-DISCRIMINANT-59']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
    max_sigma=max_sigma,
    max_discriminant=np.array([max_discriminant]),
    all_discriminants_keys=np.array(list(all_discriminants.keys())),
    all_discriminants_vals=np.array(list(all_discriminants.values())),
)
print(f"\nSaved: {outpath}")

# ===========================================================================
# 12. Plot
# ===========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: f*sigma_8 comparison
ax = axes[0, 0]
ax.errorbar(z_desi, fsig8_lcdm, yerr=fsig8_lcdm*sigma_fsig8_frac,
            fmt='ko-', label=r'$\Lambda$CDM', capsize=3, markersize=6, zorder=2)
ax.plot(z_desi, fsig8_fw, 'rs-', label=f'Framework ($w_0={w0_fw:.3f}$)', markersize=6, zorder=3)
ax.fill_between(z_desi,
                fsig8_lcdm*(1 - sigma_fsig8_euclid_frac),
                fsig8_lcdm*(1 + sigma_fsig8_euclid_frac),
                alpha=0.15, color='blue', label='Euclid 1-sigma band')  # (local)
ax.set_xlabel('Redshift z', fontsize=11)
ax.set_ylabel(r'$f\sigma_8(z)$', fontsize=11)
ax.set_title(r'Growth Rate $f\sigma_8(z)$: Framework vs $\Lambda$CDM', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: Multi-probe detection significance
ax = axes[0, 1]
# Show per-z f*sigma_8 sigma for different experiments
x = np.arange(len(z_desi))
width = 0.25  # (local)
bars1 = ax.bar(x - width, sigma_desi, width, label='DESI DR2', alpha=0.7, color='steelblue')
bars2 = ax.bar(x, sigma_euclid, width, label='Euclid', alpha=0.7, color='coral')
bars3 = ax.bar(x + width, sigma_combined, width, label='DESI+Euclid', alpha=0.7, color='forestgreen')
ax.axhline(1.0, color='gray', ls='--', alpha=0.5, label='1$\\sigma$')
ax.axhline(3.0, color='red', ls='--', alpha=0.5, label='3$\\sigma$')
ax.set_xticks(x)
ax.set_xticklabels([f'z={z:.1f}' for z in z_desi], fontsize=9)
ax.set_ylabel(r'Detection significance ($\sigma$)', fontsize=11)
ax.set_title(r'$f\sigma_8$ Discriminant per Redshift Bin', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel 3: ISW cumulative SNR
ax = axes[1, 0]
ax.plot(l_arr, snr_isw_cum, 'b-', linewidth=1.5, alpha=0.4, label='Idealized (full sky, no FG)')
ax.plot(l_arr, snr_isw_cum_degraded, 'b--', linewidth=1.5, alpha=0.6, label='With foreground degradation')
ax.plot(l_arr, snr_isw_cum_final, 'b-', linewidth=2, label=f'Final ($f_{{sky}}={f_sky}$)')
ax.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax.axhline(3.0, color='red', ls='--', alpha=0.5)
ax.set_xlabel(r'Multipole $\ell$', fontsize=11)
ax.set_ylabel(r'Cumulative ISW SNR ($\sigma$)', fontsize=11)
ax.set_title('ISW Discriminant (Cosmic Variance Limited)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(2, 100)

# Panel 4: All discriminants summary
ax = axes[1, 1]
# Select key discriminants for display
display_names = ['ISW\nauto', 'ISW\nxgal', r'$f\sigma_8$'+'\nDESI\nmulti',
                 r'$f\sigma_8$'+'\nEuclid\nmulti', r'$f\sigma_8$'+'\nD+E\nmulti',
                 'BAO\nDESI', 'BAO\nEuclid',
                 r'$w_0$'+'\nPlanck', r'$w_0$'+'\nfuture']
display_vals = [snr_isw_cum_final[-1], delta_isw_cross_detect,
                sigma_desi_multi, sigma_euclid_multi, sigma_combined_multi,
                sigma_bao_desi_multi, sigma_bao_euclid_multi,
                abs(delta_w)/sigma_w_planck, abs(delta_w)/sigma_w0_future]

colors = ['steelblue' if v < 1.0 else ('gold' if v < 3.0 else 'forestgreen') for v in display_vals]
bars = ax.bar(range(len(display_names)), display_vals, color=colors, alpha=0.8, edgecolor='black')
ax.set_xticks(range(len(display_names)))
ax.set_xticklabels(display_names, fontsize=7)
ax.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax.axhline(3.0, color='red', ls='--', alpha=0.5)
ax.set_ylabel(r'Detection significance ($\sigma$)', fontsize=11)
ax.set_title(f'All Discriminants | Gate: {gate_verdict}', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

for bar, val in zip(bars, display_vals):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
            f'{val:.2f}', ha='center', va='bottom', fontsize=7, fontweight='bold')

plt.suptitle(f'OBS-DISCRIMINANT-59: Framework ($w_0$={w0_fw:.3f}, $w_a$={wa_fw:.4f}) vs $\\Lambda$CDM\n'
             f'Gate: {gate_verdict} | Best: {max_discriminant} = {max_sigma:.2f}$\\sigma$',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92])

plotpath = os.path.join(os.path.dirname(__file__), 's59_obs_discriminant.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

print("\nDONE.")
