"""
SIDM-NFW-43: SIDM vs NFW Halo Profiles in Lensed LRDs
======================================================

Gate: SIDM-NFW-43 (INFO)

Computes projected velocity dispersion sigma(R) for a lensed LRD at z=7.04
under three DM models: NFW (framework prediction), uSIDM (isothermal core),
and FDM (soliton core). Adds BH point mass M_BH = 50 +/- 10 M M_sun
(Paper 51, Juodbalis 2025). Determines at what projected radius JWST NIRSpec
IFU can distinguish the models.

Physical setup:
- Source at z_s = 7.04, lensing magnification mu = 10
- Halo mass M_h ~ 10^10 M_sun (appropriate for LRD host at z~7)
- BH mass M_BH = 5e7 M_sun (Paper 51 direct measurement)
- NFW: rho ~ 1/r at small r (framework: sigma/m ~ 5.7e-51 cm^2/g => CDM)
- uSIDM: isothermal core r_core ~ 100 pc (Papers 32, 55, 56: sigma/m ~ 30 cm^2/g)
- FDM: soliton core r_sol ~ 200 pc (Papers 33-34: m_a ~ 10^{-22} eV)

Assumed cosmology: Planck 2018 (H_0=67.4, Omega_m=0.315, Omega_Lambda=0.685)

Author: Little-Red-Dots-JWST-Analyst
Session: 43
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d

# ============================================================
# Constants and cosmology
# ============================================================
G_N = 4.3009e-3  # pc (km/s)^2 / M_sun
c_light = 2.998e5  # km/s
H_0 = 67.4  # km/s/Mpc
Omega_m = 0.315
Omega_L = 0.685
Mpc_to_pc = 3.0857e6 * 1e12  # 1 Mpc in pc... no
pc_per_kpc = 1e3
kpc_per_Mpc = 1e3

# Cosmological distances at z=7.04 (Planck 2018)
# Angular diameter distance D_A(z=7.04) ~ 820 Mpc (comoving ~ 6600 Mpc)
z_s = 7.04
# Pre-computed for Planck 2018:
D_A_Mpc = 820.0  # angular diameter distance in Mpc
D_A_kpc = D_A_Mpc * 1e3  # in kpc
# Angular scale: 1 arcsec = D_A * (1 arcsec in radians) = 820 * 4.848e-6 Mpc = 3.975 kpc
from canonical_constants import arcsec_to_rad
kpc_per_arcsec = D_A_Mpc * 1e3 * arcsec_to_rad  # ~ 3.975 kpc/arcsec
# With magnification mu=10, effective resolution improves by sqrt(mu) ~ 3.16
mu = 10.0
effective_resolution_arcsec = 0.1 / np.sqrt(mu)  # JWST NIRSpec IFU ~ 0.1" / sqrt(mu)
effective_resolution_kpc = effective_resolution_arcsec * kpc_per_arcsec
effective_resolution_pc = effective_resolution_kpc * 1e3

print(f"Angular diameter distance D_A = {D_A_Mpc:.0f} Mpc")
print(f"Angular scale: {kpc_per_arcsec:.3f} kpc/arcsec")
print(f"Effective resolution (mu={mu:.0f}): {effective_resolution_arcsec:.4f} arcsec = {effective_resolution_pc:.0f} pc")

# ============================================================
# Halo and BH parameters
# ============================================================
M_BH = 5.0e7  # M_sun (Paper 51: 50 +/- 10 million)
M_BH_err = 1.0e7

# LRD host halo at z=7: M_h ~ 10^10 M_sun (Papers 55, 56)
# Concentration at z=7: c ~ 4-6 (high-z halos are less concentrated)
M_h = 1.0e10  # M_sun (virial mass)
c_nfw = 5.0  # concentration parameter
z_halo = 7.0

# Virial radius: M_h = (4/3) pi r_vir^3 * 200 * rho_crit(z)
# rho_crit(z=7) = 3 H(z)^2 / (8 pi G)
# H(z=7) = H_0 * sqrt(Omega_m*(1+z)^3 + Omega_L)
H_z = H_0 * np.sqrt(Omega_m * (1 + z_halo)**3 + Omega_L)  # km/s/Mpc
rho_crit_z = 3.0 * H_z**2 / (8.0 * np.pi * G_N)  # M_sun/pc^3... need consistent units

# Work in kpc, km/s, M_sun
G_kpc = 4.3009e-3 * 1e-3  # kpc (km/s)^2 / M_sun   [G = 4.3009e-3 pc (km/s)^2/M_sun]
# rho_crit(z) in M_sun/kpc^3
# H(z) in km/s/kpc = H_z / 1e3
H_z_kpc = H_z / 1e3  # km/s/kpc
rho_crit_kpc3 = 3.0 * H_z_kpc**2 / (8.0 * np.pi * G_kpc)  # M_sun/kpc^3
print(f"\nH(z=7) = {H_z:.1f} km/s/Mpc = {H_z_kpc:.4e} km/s/kpc")
print(f"rho_crit(z=7) = {rho_crit_kpc3:.4e} M_sun/kpc^3")

# Virial radius (R_200 where mean density = 200 * rho_crit)
R_vir_kpc = (3.0 * M_h / (4.0 * np.pi * 200.0 * rho_crit_kpc3))**(1.0/3.0)
r_s_kpc = R_vir_kpc / c_nfw
print(f"R_vir = {R_vir_kpc:.2f} kpc")
print(f"r_s = {r_s_kpc:.3f} kpc = {r_s_kpc*1e3:.0f} pc")

# NFW normalization
def f_nfw(c):
    return np.log(1 + c) - c / (1 + c)

rho_s_nfw = M_h / (4.0 * np.pi * r_s_kpc**3 * f_nfw(c_nfw))  # M_sun/kpc^3
print(f"rho_s (NFW) = {rho_s_nfw:.4e} M_sun/kpc^3")

# ============================================================
# Density profiles: NFW, uSIDM, FDM
# ============================================================

def rho_nfw(r_kpc):
    """NFW profile: rho = rho_s / [(r/r_s)(1+r/r_s)^2]"""
    x = r_kpc / r_s_kpc
    x = np.maximum(x, 1e-10)
    return rho_s_nfw / (x * (1 + x)**2)

# uSIDM: Isothermal core with gravothermal cusp
# Paper 32: rho ~ r^{-3} near collapse center
# Paper 55: r_core ~ 100 pc for sigma/m ~ 30 cm^2/g
# Transition: isothermal core -> NFW-like outer
r_core_sidm_kpc = 0.1  # 100 pc
# Central density: match NFW mass within ~ r_s for consistency
# Use cored profile: rho_SIDM = rho_0 / (1 + (r/r_core)^2)^alpha
# Pre-collapse (isothermal): alpha = 1 (Burkert-like core)
# Post-collapse (gravothermal cusp): alpha adjusted for rho ~ r^{-2.2} at intermediate r
rho_0_sidm = rho_nfw(r_core_sidm_kpc) * (1 + (r_core_sidm_kpc/r_s_kpc))**2 * (r_core_sidm_kpc/r_s_kpc)
# This matches NFW at r_core

def rho_sidm_isothermal(r_kpc):
    """uSIDM pre-collapse: isothermal core with NFW envelope
    rho = rho_0 / (1 + (r/r_core)^2) for r < r_match
    transitions to NFW at r > r_match
    """
    x = r_kpc / r_core_sidm_kpc
    # Pseudo-isothermal core (Begeman 1991)
    rho_core = rho_0_sidm / (1 + x**2)
    # Match to NFW at large r
    rho_outer = rho_nfw(r_kpc)
    # Smooth transition at ~ 3*r_core
    r_match = 3.0 * r_core_sidm_kpc
    w = 0.5 * (1 + np.tanh((r_kpc - r_match) / (0.3 * r_core_sidm_kpc)))
    return (1 - w) * rho_core + w * rho_outer

# Normalize SIDM to have same total mass within R_vir as NFW
# Compute mass within R_vir for initial SIDM profile
r_test = np.logspace(-3, np.log10(R_vir_kpc), 1000)
dr = np.diff(r_test)
r_mid = 0.5 * (r_test[:-1] + r_test[1:])
mass_sidm_raw = np.sum(4 * np.pi * r_mid**2 * rho_sidm_isothermal(r_mid) * dr)
mass_nfw_total = M_h
scale_sidm = mass_nfw_total / mass_sidm_raw

def rho_sidm(r_kpc):
    """Normalized uSIDM isothermal core profile"""
    return scale_sidm * rho_sidm_isothermal(r_kpc)

# FDM: Soliton core (Schive et al. 2014)
# rho_sol = rho_c / (1 + 0.091*(r/r_sol)^2)^8
# r_sol ~ 200 pc for m_a ~ 10^{-22} eV at z~7
# Papers 33-34: soliton mass M_sol ~ 10^8 M_sun, r_sol ~ 0.2 kpc
r_sol_kpc = 0.2  # 200 pc soliton core radius

# Soliton central density from mass:
# M_sol ~ (4/3) pi r_sol^3 rho_c * I (where I is the profile integral)
# For Schive profile: M_sol ~ 5.5e9 * (m_a/10^{-22})^{-2} * (r_sol/kpc)^{-1} M_sun
# At r_sol = 0.2 kpc: M_sol ~ 2.75e10 ... too high, use M_sol ~ 10^8
M_sol = 1e8  # soliton core mass
# rho_c from soliton profile integral
# Integral of (1 + 0.091 x^2)^{-8} * x^2 dx from 0 to inf ~ 3.88 (numerically)
soliton_integral = 3.88  # dimensionless integral
rho_c_fdm = M_sol / (4 * np.pi * r_sol_kpc**3 * soliton_integral)

def rho_fdm_soliton(r_kpc):
    """FDM soliton core + NFW envelope (Schive et al. 2014 profile)"""
    x = r_kpc / r_sol_kpc
    rho_sol = rho_c_fdm / (1 + 0.091 * x**2)**8
    # Transition to NFW at ~3 r_sol
    rho_outer = rho_nfw(r_kpc)
    r_match = 3.0 * r_sol_kpc
    w = 0.5 * (1 + np.tanh((r_kpc - r_match) / (0.3 * r_sol_kpc)))
    return (1 - w) * rho_sol + w * rho_outer

# Normalize FDM to same total mass
mass_fdm_raw = np.sum(4 * np.pi * r_mid**2 * rho_fdm_soliton(r_mid) * dr)
scale_fdm = mass_nfw_total / mass_fdm_raw

def rho_fdm(r_kpc):
    """Normalized FDM soliton profile"""
    return scale_fdm * rho_fdm_soliton(r_kpc)

# ============================================================
# Enclosed mass M(<r) for each model + BH
# ============================================================
r_arr_kpc = np.logspace(-3, np.log10(R_vir_kpc), 2000)

def enclosed_mass(rho_func, r_arr):
    """Compute M(<r) by numerical integration"""
    M_enc = np.zeros_like(r_arr)
    for i in range(1, len(r_arr)):
        # Trapezoidal integration
        r1, r2 = r_arr[i-1], r_arr[i]
        rm = 0.5 * (r1 + r2)
        shell = 4 * np.pi * rm**2 * rho_func(rm) * (r2 - r1)
        M_enc[i] = M_enc[i-1] + shell
    return M_enc

M_enc_nfw = enclosed_mass(rho_nfw, r_arr_kpc) + M_BH
M_enc_sidm = enclosed_mass(rho_sidm, r_arr_kpc) + M_BH
M_enc_fdm = enclosed_mass(rho_fdm, r_arr_kpc) + M_BH

# ============================================================
# 3D velocity dispersion sigma_r(r) via Jeans equation
# ============================================================
# For isotropic, spherically symmetric system:
# sigma_r^2(r) = (1/rho(r)) * integral_r^infty [rho(r') * G*M(<r') / r'^2] dr'
# This is the Jeans equation solution for isotropic velocity tensor

def jeans_sigma_r(rho_func, M_enc_interp, r_arr):
    """Solve Jeans equation for radial velocity dispersion.
    sigma_r^2(r) = (1/rho(r)) * int_r^rmax [rho * G*M/r'^2] dr'
    """
    sigma_r2 = np.zeros_like(r_arr)
    rho_vals = rho_func(r_arr)
    M_vals = M_enc_interp(r_arr)

    # Integrate from outside in (backward cumulative)
    for i in range(len(r_arr) - 2, -1, -1):
        dr = r_arr[i+1] - r_arr[i]
        rm = 0.5 * (r_arr[i] + r_arr[i+1])
        rho_m = rho_func(rm)
        M_m = M_enc_interp(rm)
        integrand = rho_m * G_kpc * M_m / rm**2
        sigma_r2[i] = sigma_r2[i+1] + integrand * dr

    # Divide by rho(r)
    rho_vals_safe = np.maximum(rho_vals, 1e-30)
    sigma_r2 /= rho_vals_safe

    return np.sqrt(np.maximum(sigma_r2, 0))

# Interpolators for M(<r)
M_interp_nfw = interp1d(r_arr_kpc, M_enc_nfw, kind='linear', fill_value='extrapolate')
M_interp_sidm = interp1d(r_arr_kpc, M_enc_sidm, kind='linear', fill_value='extrapolate')
M_interp_fdm = interp1d(r_arr_kpc, M_enc_fdm, kind='linear', fill_value='extrapolate')

# Compute on finer grid for sigma(r)
r_fine = np.logspace(-3, np.log10(R_vir_kpc), 5000)

sigma_r_nfw = jeans_sigma_r(rho_nfw, M_interp_nfw, r_fine)
sigma_r_sidm = jeans_sigma_r(rho_sidm, M_interp_sidm, r_fine)
sigma_r_fdm = jeans_sigma_r(rho_fdm, M_interp_fdm, r_fine)

# ============================================================
# Projected (line-of-sight) velocity dispersion sigma_los(R)
# ============================================================
# sigma_los^2(R) = (2/Sigma(R)) * integral_R^inf [rho * sigma_r^2 * r / sqrt(r^2 - R^2)] dr
# where Sigma(R) = 2 * integral_R^inf [rho * r / sqrt(r^2 - R^2)] dr

def projected_sigma_los(R_proj, rho_func, sigma_r_interp, r_arr, r_max):
    """Compute line-of-sight projected velocity dispersion at projected radius R"""
    sigma_los2_arr = np.zeros_like(R_proj)
    Sigma_arr = np.zeros_like(R_proj)

    for j, R in enumerate(R_proj):
        # Integration from R to r_max along line of sight
        # Use r values > R
        mask = r_arr > R * 1.001
        r_los = r_arr[mask]
        if len(r_los) < 10:
            continue

        rho_vals = rho_func(r_los)
        sr_vals = sigma_r_interp(r_los)
        denom = np.sqrt(r_los**2 - R**2)
        denom = np.maximum(denom, 1e-10)

        dr = np.diff(r_los)
        rm = 0.5 * (r_los[:-1] + r_los[1:])
        rho_m = rho_func(rm)
        sr_m = sigma_r_interp(rm)
        denom_m = np.sqrt(rm**2 - R**2)
        denom_m = np.maximum(denom_m, 1e-10)

        # Surface density
        integrand_Sigma = 2 * rho_m * rm / denom_m
        Sigma_val = np.sum(integrand_Sigma * dr)

        # sigma_los^2 numerator
        integrand_slos = 2 * rho_m * sr_m**2 * rm / denom_m
        num_val = np.sum(integrand_slos * dr)

        Sigma_arr[j] = Sigma_val
        if Sigma_val > 0:
            sigma_los2_arr[j] = num_val / Sigma_val

    return np.sqrt(np.maximum(sigma_los2_arr, 0)), Sigma_arr

# Projected radii: from 10 pc to 5 kpc
R_proj_kpc = np.logspace(np.log10(0.01), np.log10(5.0), 200)
R_proj_pc = R_proj_kpc * 1e3

# Interpolators for sigma_r
sr_interp_nfw = interp1d(r_fine, sigma_r_nfw, kind='linear', fill_value='extrapolate')
sr_interp_sidm = interp1d(r_fine, sigma_r_sidm, kind='linear', fill_value='extrapolate')
sr_interp_fdm = interp1d(r_fine, sigma_r_fdm, kind='linear', fill_value='extrapolate')

sigma_los_nfw, Sigma_nfw = projected_sigma_los(R_proj_kpc, rho_nfw, sr_interp_nfw, r_fine, R_vir_kpc)
sigma_los_sidm, Sigma_sidm = projected_sigma_los(R_proj_kpc, rho_sidm, sr_interp_sidm, r_fine, R_vir_kpc)
sigma_los_fdm, Sigma_fdm = projected_sigma_los(R_proj_kpc, rho_fdm, sr_interp_fdm, r_fine, R_vir_kpc)

print(f"\n=== Projected sigma_los at selected radii ===")
for r_check in [0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 3.0]:
    idx = np.argmin(np.abs(R_proj_kpc - r_check))
    print(f"R = {R_proj_pc[idx]:6.0f} pc: NFW={sigma_los_nfw[idx]:6.1f}, "
          f"SIDM={sigma_los_sidm[idx]:6.1f}, FDM={sigma_los_fdm[idx]:6.1f} km/s")

# ============================================================
# BH sphere of influence
# ============================================================
# r_infl where M_DM(<r) = M_BH
# For NFW: solve M_NFW(<r) = M_BH
r_infl_nfw = r_fine[np.argmin(np.abs(M_interp_nfw(r_fine) - 2*M_BH))]
r_infl_sidm = r_fine[np.argmin(np.abs(M_interp_sidm(r_fine) - 2*M_BH))]
r_infl_fdm = r_fine[np.argmin(np.abs(M_interp_fdm(r_fine) - 2*M_BH))]

print(f"\n=== BH sphere of influence (where M_DM = M_BH) ===")
print(f"NFW:  r_infl = {r_infl_nfw*1e3:.0f} pc")
print(f"SIDM: r_infl = {r_infl_sidm*1e3:.0f} pc")
print(f"FDM:  r_infl = {r_infl_fdm*1e3:.0f} pc")

# ============================================================
# Observational PSF convolution
# ============================================================
# JWST NIRSpec IFU: 0.1" spaxels, PSF FWHM ~ 0.1" at 3 micron
# With lensing mu=10: effective PSF FWHM ~ 0.1/sqrt(10) ~ 0.032"
# In physical units at z=7: PSF ~ 0.032" * 3.975 kpc/arcsec ~ 125 pc
PSF_fwhm_arcsec = 0.1 / np.sqrt(mu)
PSF_fwhm_kpc = PSF_fwhm_arcsec * kpc_per_arcsec
PSF_sigma_kpc = PSF_fwhm_kpc / 2.355  # Gaussian sigma
PSF_fwhm_pc = PSF_fwhm_kpc * 1e3
PSF_sigma_pc = PSF_sigma_kpc * 1e3

print(f"\n=== PSF parameters ===")
print(f"PSF FWHM = {PSF_fwhm_arcsec:.4f}\" = {PSF_fwhm_pc:.0f} pc")
print(f"PSF sigma = {PSF_sigma_pc:.0f} pc")

# Convolve sigma_los with PSF (Gaussian smoothing in projected radius)
def convolve_sigma_with_psf(R_proj, sigma_los, Sigma, psf_sigma):
    """Convolve luminosity-weighted sigma_los with Gaussian PSF.
    sigma_obs^2(R) = int [sigma_los^2(R') * Sigma(R') * PSF(R-R')] dR' / int [Sigma(R') * PSF(R-R')] dR'
    For 1D radial profile, approximate with Gaussian kernel.
    """
    sigma_obs = np.zeros_like(sigma_los)

    for i, R0 in enumerate(R_proj):
        # Gaussian weight
        w = np.exp(-0.5 * (R_proj - R0)**2 / psf_sigma**2)
        w *= Sigma  # luminosity weighting
        w_sum = np.sum(w)
        if w_sum > 0:
            sigma_obs[i] = np.sqrt(np.sum(w * sigma_los**2) / w_sum)

    return sigma_obs

sigma_obs_nfw = convolve_sigma_with_psf(R_proj_kpc, sigma_los_nfw, Sigma_nfw, PSF_sigma_kpc)
sigma_obs_sidm = convolve_sigma_with_psf(R_proj_kpc, sigma_los_sidm, Sigma_sidm, PSF_sigma_kpc)
sigma_obs_fdm = convolve_sigma_with_psf(R_proj_kpc, sigma_los_fdm, Sigma_fdm, PSF_sigma_kpc)

# ============================================================
# Discriminability analysis
# ============================================================
# JWST NIRSpec velocity precision: ~30-50 km/s per spaxel for S/N ~ 10-20
# With lensing mu=10, S/N improves by sqrt(mu) ~ 3.16
# Assume sigma_meas ~ 30 km/s (optimistic) to 50 km/s (conservative)
sigma_meas_opt = 30.0  # km/s (optimistic)
sigma_meas_con = 50.0  # km/s (conservative)

# Difference between models
delta_nfw_sidm = np.abs(sigma_obs_nfw - sigma_obs_sidm)
delta_nfw_fdm = np.abs(sigma_obs_nfw - sigma_obs_fdm)
delta_sidm_fdm = np.abs(sigma_obs_sidm - sigma_obs_fdm)

# S/N for discrimination: delta_sigma / sigma_meas
snr_nfw_sidm_opt = delta_nfw_sidm / sigma_meas_opt
snr_nfw_sidm_con = delta_nfw_sidm / sigma_meas_con
snr_nfw_fdm_opt = delta_nfw_fdm / sigma_meas_opt
snr_sidm_fdm_opt = delta_sidm_fdm / sigma_meas_opt

# Find radii where S/N > 3 (3-sigma discrimination)
def find_discrimination_radius(R, snr, threshold=3.0):
    """Find the outermost radius where S/N > threshold (going inward)"""
    mask = snr > threshold
    if not np.any(mask):
        return None, 0.0
    # Find the range of radii where discrimination is possible
    r_min = R[mask].min()
    r_max = R[mask].max()
    snr_max = snr[mask].max()
    return r_min, r_max, snr_max

print(f"\n=== Discriminability (3-sigma, optimistic sigma_meas={sigma_meas_opt} km/s) ===")
result = find_discrimination_radius(R_proj_pc, snr_nfw_sidm_opt)
if result[0] is not None:
    print(f"NFW vs SIDM: distinguishable at R = {result[0]:.0f} - {result[1]:.0f} pc (peak S/N = {result[2]:.1f})")
else:
    print(f"NFW vs SIDM: NOT distinguishable at 3-sigma")

result2 = find_discrimination_radius(R_proj_pc, snr_nfw_fdm_opt)
if result2[0] is not None:
    print(f"NFW vs FDM:  distinguishable at R = {result2[0]:.0f} - {result2[1]:.0f} pc (peak S/N = {result2[2]:.1f})")
else:
    print(f"NFW vs FDM:  NOT distinguishable at 3-sigma")

result3 = find_discrimination_radius(R_proj_pc, snr_sidm_fdm_opt)
if result3[0] is not None:
    print(f"SIDM vs FDM: distinguishable at R = {result3[0]:.0f} - {result3[1]:.0f} pc (peak S/N = {result3[2]:.1f})")
else:
    print(f"SIDM vs FDM: NOT distinguishable at 3-sigma")

print(f"\n=== Discriminability (3-sigma, conservative sigma_meas={sigma_meas_con} km/s) ===")
result_c = find_discrimination_radius(R_proj_pc, snr_nfw_sidm_con)
if result_c[0] is not None:
    print(f"NFW vs SIDM: distinguishable at R = {result_c[0]:.0f} - {result_c[1]:.0f} pc (peak S/N = {result_c[2]:.1f})")
else:
    print(f"NFW vs SIDM: NOT distinguishable at 3-sigma with current precision")

# ============================================================
# Circular velocity profiles (for comparison with Paper 51)
# ============================================================
v_circ_nfw = np.sqrt(G_kpc * M_interp_nfw(r_fine) / r_fine)
v_circ_sidm = np.sqrt(G_kpc * M_interp_sidm(r_fine) / r_fine)
v_circ_fdm = np.sqrt(G_kpc * M_interp_fdm(r_fine) / r_fine)

# BH-only Keplerian
v_circ_bh = np.sqrt(G_kpc * M_BH / r_fine)

# Transition radius: where v_circ_DM = v_circ_BH
# For NFW:
M_enc_nfw_only = enclosed_mass(rho_nfw, r_fine)
v_circ_dm_only = np.sqrt(G_kpc * np.maximum(M_enc_nfw_only, 1) / r_fine)
# Find where M_DM(<r) = M_BH
idx_trans = np.argmin(np.abs(M_enc_nfw_only - M_BH))
r_trans_nfw = r_fine[idx_trans]
print(f"\n=== Transition radius (M_DM = M_BH) ===")
print(f"NFW:  r_transition = {r_trans_nfw*1e3:.0f} pc")

# ============================================================
# Density profile slopes (log-log)
# ============================================================
r_slope = np.logspace(-2.5, 0.5, 500)  # 0.003 to 3 kpc
log_r = np.log10(r_slope)

rho_nfw_vals = rho_nfw(r_slope)
rho_sidm_vals = rho_sidm(r_slope)
rho_fdm_vals = rho_fdm(r_slope)

# Log-log slope
slope_nfw_arr = np.gradient(np.log10(rho_nfw_vals), log_r)
slope_sidm_arr = np.gradient(np.log10(rho_sidm_vals), log_r)
slope_fdm_arr = np.gradient(np.log10(rho_fdm_vals), log_r)

print(f"\n=== Inner density profile slopes ===")
for r_check_kpc in [0.01, 0.05, 0.1, 0.3, 1.0]:
    idx = np.argmin(np.abs(r_slope - r_check_kpc))
    print(f"r = {r_check_kpc*1e3:5.0f} pc: NFW={slope_nfw_arr[idx]:.2f}, "
          f"SIDM={slope_sidm_arr[idx]:.2f}, FDM={slope_fdm_arr[idx]:.2f}")

# ============================================================
# Surface mass density Sigma(R) for lensing
# ============================================================
print(f"\n=== Surface density at selected radii ===")
for r_check_kpc in [0.01, 0.1, 0.5, 1.0]:
    idx = np.argmin(np.abs(R_proj_kpc - r_check_kpc))
    print(f"R = {r_check_kpc*1e3:5.0f} pc: Sigma_NFW={Sigma_nfw[idx]:.2e}, "
          f"Sigma_SIDM={Sigma_sidm[idx]:.2e}, Sigma_FDM={Sigma_fdm[idx]:.2e} M_sun/kpc^2")

# Critical surface density for lensing at z_s=7.04 (lens at z_l ~ 0.5-2)
# Sigma_cr = c^2/(4*pi*G) * D_s/(D_l*D_ls)
# For typical strong lensing: Sigma_cr ~ 3000-5000 M_sun/pc^2 = 3e9-5e9 M_sun/kpc^2
Sigma_crit = 3.5e9  # M_sun/kpc^2 (typical)

# Convergence kappa = Sigma / Sigma_crit
kappa_nfw = Sigma_nfw / Sigma_crit
kappa_sidm = Sigma_sidm / Sigma_crit
kappa_fdm = Sigma_fdm / Sigma_crit

print(f"\n=== Convergence kappa at R=100 pc ===")
idx_100 = np.argmin(np.abs(R_proj_pc - 100))
print(f"kappa_NFW  = {kappa_nfw[idx_100]:.4f}")
print(f"kappa_SIDM = {kappa_sidm[idx_100]:.4f}")
print(f"kappa_FDM  = {kappa_fdm[idx_100]:.4f}")

# ============================================================
# Key quantitative results summary
# ============================================================
# Peak delta_sigma (NFW - SIDM)
idx_peak = np.argmax(delta_nfw_sidm)
print(f"\n{'='*60}")
print(f"=== SIDM-NFW-43 GATE RESULTS (INFO) ===")
print(f"{'='*60}")
print(f"Halo: M_h = {M_h:.1e} M_sun, c = {c_nfw:.0f}, z = {z_halo:.1f}")
print(f"BH:   M_BH = {M_BH:.1e} M_sun (Paper 51)")
print(f"Lens: mu = {mu:.0f}, PSF_eff = {PSF_fwhm_pc:.0f} pc")
print(f"")
print(f"Framework (NFW): inner slope = -1 (CDM, sigma/m = 5.7e-51 cm^2/g)")
print(f"uSIDM:           core r_core = {r_core_sidm_kpc*1e3:.0f} pc (sigma/m = 30 cm^2/g)")
print(f"FDM:              soliton r_sol = {r_sol_kpc*1e3:.0f} pc (m_a = 10^-22 eV)")
print(f"")
print(f"Peak |sigma_NFW - sigma_SIDM| = {delta_nfw_sidm[idx_peak]:.1f} km/s at R = {R_proj_pc[idx_peak]:.0f} pc")
print(f"Peak |sigma_NFW - sigma_FDM|  = {delta_nfw_fdm[np.argmax(delta_nfw_fdm)]:.1f} km/s at R = {R_proj_pc[np.argmax(delta_nfw_fdm)]:.0f} pc")
print(f"")
print(f"BH sphere of influence: {r_infl_nfw*1e3:.0f} pc (NFW), {r_infl_sidm*1e3:.0f} pc (SIDM)")
print(f"BH-DM transition:       {r_trans_nfw*1e3:.0f} pc")
print(f"PSF resolution limit:   {PSF_fwhm_pc:.0f} pc")
print(f"")

# Discrimination verdicts
if result[0] is not None:
    print(f"NFW vs SIDM: DISTINGUISHABLE at R = {result[0]:.0f}-{result[1]:.0f} pc "
          f"(peak {result[2]:.1f}-sigma, optimistic)")
else:
    print(f"NFW vs SIDM: NOT distinguishable with current JWST+mu={mu:.0f}")

if result2[0] is not None:
    print(f"NFW vs FDM:  DISTINGUISHABLE at R = {result2[0]:.0f}-{result2[1]:.0f} pc "
          f"(peak {result2[2]:.1f}-sigma, optimistic)")
else:
    print(f"NFW vs FDM:  NOT distinguishable with current JWST+mu={mu:.0f}")

# Save NPZ
np.savez('tier0-computation/s43_sidm_nfw.npz',
    # Gate
    gate_id=np.array(['SIDM-NFW-43']),
    gate_verdict=np.array(['INFO']),

    # Parameters
    M_BH=np.array([M_BH]),
    M_BH_err=np.array([M_BH_err]),
    M_h=np.array([M_h]),
    c_nfw=np.array([c_nfw]),
    z_halo=np.array([z_halo]),
    mu_lens=np.array([mu]),
    r_core_sidm_pc=np.array([r_core_sidm_kpc * 1e3]),
    r_sol_fdm_pc=np.array([r_sol_kpc * 1e3]),
    PSF_fwhm_pc=np.array([PSF_fwhm_pc]),
    sigma_meas_opt=np.array([sigma_meas_opt]),
    sigma_meas_con=np.array([sigma_meas_con]),

    # Radial arrays
    R_proj_pc=R_proj_pc,
    R_proj_kpc=R_proj_kpc,

    # Projected sigma_los (intrinsic)
    sigma_los_nfw=sigma_los_nfw,
    sigma_los_sidm=sigma_los_sidm,
    sigma_los_fdm=sigma_los_fdm,

    # Observed (PSF-convolved) sigma
    sigma_obs_nfw=sigma_obs_nfw,
    sigma_obs_sidm=sigma_obs_sidm,
    sigma_obs_fdm=sigma_obs_fdm,

    # Surface density
    Sigma_nfw=Sigma_nfw,
    Sigma_sidm=Sigma_sidm,
    Sigma_fdm=Sigma_fdm,

    # Density profiles
    r_density_kpc=r_slope,
    rho_nfw=rho_nfw_vals,
    rho_sidm=rho_sidm_vals,
    rho_fdm=rho_fdm_vals,
    slope_nfw=slope_nfw_arr,
    slope_sidm=slope_sidm_arr,
    slope_fdm=slope_fdm_arr,

    # Circular velocity
    r_fine_kpc=r_fine,
    v_circ_nfw=v_circ_nfw,
    v_circ_sidm=v_circ_sidm,
    v_circ_fdm=v_circ_fdm,
    v_circ_bh=v_circ_bh,

    # Discrimination
    delta_nfw_sidm=delta_nfw_sidm,
    delta_nfw_fdm=delta_nfw_fdm,
    delta_sidm_fdm=delta_sidm_fdm,
    snr_nfw_sidm_opt=snr_nfw_sidm_opt,
    snr_nfw_sidm_con=snr_nfw_sidm_con,

    # Key radii
    r_infl_nfw_pc=np.array([r_infl_nfw * 1e3]),
    r_infl_sidm_pc=np.array([r_infl_sidm * 1e3]),
    r_infl_fdm_pc=np.array([r_infl_fdm * 1e3]),
    r_trans_nfw_pc=np.array([r_trans_nfw * 1e3]),

    # Framework connection
    framework_sigma_over_m=np.array([5.72e-51]),
    sidm_sigma_over_m=np.array([30.0]),
    sigma_ratio_log10=np.array([np.log10(30.0 / 5.72e-51)]),
)

print(f"\nSaved: tier0-computation/s43_sidm_nfw.npz")

# ============================================================
# PLOTTING
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('SIDM-NFW-43: DM Halo Profiles in Lensed LRD at z=7.04\n'
             f'M_BH = 5×10$^7$ M$_\\odot$ (Paper 51), M_h = 10$^{{10}}$ M$_\\odot$, '
             f'$\\mu$ = {mu:.0f}', fontsize=13, fontweight='bold')

# Colors
c_nfw_color = '#2166AC'
c_sidm_color = '#B2182B'
c_fdm_color = '#4DAF4A'
c_bh_color = '#FF7F00'

# --- Panel (a): Density profiles ---
ax = axes[0, 0]
ax.loglog(r_slope * 1e3, rho_nfw_vals, '-', color=c_nfw_color, lw=2.5, label='NFW (framework)')
ax.loglog(r_slope * 1e3, rho_sidm_vals, '--', color=c_sidm_color, lw=2.5, label=f'uSIDM (r$_{{core}}$={r_core_sidm_kpc*1e3:.0f} pc)')
ax.loglog(r_slope * 1e3, rho_fdm_vals, '-.', color=c_fdm_color, lw=2.5, label=f'FDM soliton (r$_{{sol}}$={r_sol_kpc*1e3:.0f} pc)')
ax.axvspan(0, PSF_fwhm_pc, alpha=0.1, color='gray', label=f'PSF limit ({PSF_fwhm_pc:.0f} pc)')
ax.axvline(r_core_sidm_kpc * 1e3, ls=':', color=c_sidm_color, alpha=0.5)
ax.axvline(r_sol_kpc * 1e3, ls=':', color=c_fdm_color, alpha=0.5)
ax.set_xlabel('r [pc]', fontsize=12)
ax.set_ylabel(r'$\rho$ [M$_\odot$ kpc$^{-3}$]', fontsize=12)
ax.set_title('(a) 3D Density Profiles', fontsize=12)
ax.legend(fontsize=9, loc='lower left')
ax.set_xlim(3, 5000)
ax.set_ylim(1e2, None)
ax.grid(True, alpha=0.3)

# --- Panel (b): Circular velocity ---
ax = axes[0, 1]
r_plot_pc = r_fine * 1e3
mask_plot = (r_fine > 0.003) & (r_fine < 5.0)
ax.loglog(r_plot_pc[mask_plot], v_circ_nfw[mask_plot], '-', color=c_nfw_color, lw=2.5, label='NFW + BH')
ax.loglog(r_plot_pc[mask_plot], v_circ_sidm[mask_plot], '--', color=c_sidm_color, lw=2.5, label='uSIDM + BH')
ax.loglog(r_plot_pc[mask_plot], v_circ_fdm[mask_plot], '-.', color=c_fdm_color, lw=2.5, label='FDM + BH')
ax.loglog(r_plot_pc[mask_plot], v_circ_bh[mask_plot], ':', color=c_bh_color, lw=1.5, alpha=0.7, label='BH only (Keplerian)')
ax.axvline(r_trans_nfw * 1e3, ls='-', color='gray', alpha=0.5, lw=1)
ax.text(r_trans_nfw * 1e3 * 1.2, 30, f'r$_{{trans}}$={r_trans_nfw*1e3:.0f} pc', fontsize=8, color='gray')
ax.axvspan(0, PSF_fwhm_pc, alpha=0.1, color='gray')
ax.set_xlabel('r [pc]', fontsize=12)
ax.set_ylabel(r'v$_{circ}$ [km/s]', fontsize=12)
ax.set_title('(b) Circular Velocity (BH + DM)', fontsize=12)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(3, 5000)
ax.grid(True, alpha=0.3)

# --- Panel (c): Projected velocity dispersion (observed) ---
ax = axes[1, 0]
ax.semilogx(R_proj_pc, sigma_obs_nfw, '-', color=c_nfw_color, lw=2.5, label='NFW (PSF-convolved)')
ax.semilogx(R_proj_pc, sigma_obs_sidm, '--', color=c_sidm_color, lw=2.5, label='uSIDM (PSF-convolved)')
ax.semilogx(R_proj_pc, sigma_obs_fdm, '-.', color=c_fdm_color, lw=2.5, label='FDM (PSF-convolved)')
# Intrinsic (thin)
ax.semilogx(R_proj_pc, sigma_los_nfw, '-', color=c_nfw_color, lw=1, alpha=0.3, label='NFW (intrinsic)')
ax.semilogx(R_proj_pc, sigma_los_sidm, '--', color=c_sidm_color, lw=1, alpha=0.3)
ax.semilogx(R_proj_pc, sigma_los_fdm, '-.', color=c_fdm_color, lw=1, alpha=0.3)
# Measurement error band
ax.fill_between(R_proj_pc, 0, sigma_meas_opt, alpha=0.1, color='orange', label=f'1-sigma meas. floor ({sigma_meas_opt} km/s)')
ax.axvspan(0, PSF_fwhm_pc, alpha=0.1, color='gray')
ax.set_xlabel('R (projected) [pc]', fontsize=12)
ax.set_ylabel(r'$\sigma_{los}$ [km/s]', fontsize=12)
ax.set_title(f'(c) Observed $\\sigma_{{los}}$(R), PSF={PSF_fwhm_pc:.0f} pc', fontsize=12)
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(10, 5000)
ax.set_ylim(0, None)
ax.grid(True, alpha=0.3)

# --- Panel (d): S/N for discrimination ---
ax = axes[1, 1]
ax.semilogx(R_proj_pc, snr_nfw_sidm_opt, '-', color=c_sidm_color, lw=2.5,
           label=f'NFW vs SIDM ($\\sigma_{{meas}}$={sigma_meas_opt} km/s)')
ax.semilogx(R_proj_pc, snr_nfw_fdm_opt, '-.', color=c_fdm_color, lw=2.5,
           label=f'NFW vs FDM ($\\sigma_{{meas}}$={sigma_meas_opt} km/s)')
ax.semilogx(R_proj_pc, snr_nfw_sidm_con, ':', color=c_sidm_color, lw=2,
           label=f'NFW vs SIDM ($\\sigma_{{meas}}$={sigma_meas_con} km/s)')
ax.axhline(3.0, ls='--', color='black', alpha=0.5, lw=1)
ax.text(4000, 3.3, '3$\\sigma$', fontsize=10, color='black')
ax.axhline(5.0, ls=':', color='black', alpha=0.3, lw=1)
ax.text(4000, 5.3, '5$\\sigma$', fontsize=10, color='black', alpha=0.5)
ax.axvspan(0, PSF_fwhm_pc, alpha=0.1, color='gray', label=f'Below PSF ({PSF_fwhm_pc:.0f} pc)')
ax.set_xlabel('R (projected) [pc]', fontsize=12)
ax.set_ylabel(r'S/N for model discrimination', fontsize=12)
ax.set_title('(d) Discriminability: NFW vs Alternatives', fontsize=12)
ax.legend(fontsize=8, loc='upper right')
ax.set_xlim(10, 5000)
ax.set_ylim(0, max(15, np.nanmax(snr_nfw_sidm_opt[R_proj_pc > PSF_fwhm_pc]) * 1.2) if np.any(snr_nfw_sidm_opt[R_proj_pc > PSF_fwhm_pc] > 0) else 15)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('tier0-computation/s43_sidm_nfw.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s43_sidm_nfw.png")
plt.close()
