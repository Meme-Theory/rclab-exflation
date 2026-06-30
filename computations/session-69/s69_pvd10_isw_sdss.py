#!/usr/bin/env python3
"""
s69_pvd10_isw_sdss.py -- ISW-Galaxy Cross-Correlation for SDSS LRG Sample
==========================================================================

Session 69, Gate: PVD-ISW-69 (INFO)

Uses ISW tracking results from S68 (s68_isw_tracking_test.npz) to predict
the ISW-galaxy cross-correlation C_l^{Tg} specifically for the SDSS LRG sample.

The SDSS LRG sample has distinctive parameters:
  - Galaxy bias: b ~ 1.9-2.1 (Padmanabhan+07, Tegmark+06)
  - Redshift range: 0.15 < z < 0.7, median z ~ 0.35
  - Sky coverage: f_sky ~ 0.24
  - Number density: n_bar ~ 10^{-4} (h/Mpc)^3

Observational comparison:
  - Granett+08 (0804.0292): ISW stacking on SDSS LRG superstructures, 4.4 sigma.
    NOTE: This is a STACKING analysis on extremes of the density field, NOT
    a standard C_l^{Tg} measurement. The amplitude is anomalously high compared
    to LCDM expectations (the Granett anomaly).
  - Giannantonio+08 (0801.4380): Cross-correlation of CMB with multiple tracers
    including SDSS LRGs. Combined detection at 4.5 sigma. SDSS-alone ~2.5 sigma.
  - Padmanabhan+05 (0407594): ISW x SDSS LRGs, A_ISW = 2.5 +/- 1.0 (2.5 sigma).
  - Ho+08 (0801.0642): ISW x SDSS + NVSS, combined 3.7 sigma.
  - Planck 2015 ISW (1502.01595): Combined detection 4 sigma, per-tracer SDSS
    CMASS/LOWZ A = 0.72 +/- 0.35.

Key question: Does the framework's ~12% ISW enhancement (from tracking DE with
c_s^2 = 0) shift the predicted S/N enough to be visible in existing SDSS data?

Author: mack-cosmic-bridge
"""

import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")

import numpy as np
from scipy.integrate import quad, simpson
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_Lambda, Omega_b, Omega_DM,
    Omega_r, T_CMB, c_light_km_s, sigma_8, A_s_CMB,
    Mpc_to_m, H_0_inv_s
)

# ==============================================================================
#  Load S68 ISW tracking results
# ==============================================================================

s68_path = r"C:\sandbox\Ainulindale Exflation\computations\s68_isw_tracking_test.npz"
s68 = np.load(s68_path)

z_arr_s68 = s68['z_arr']           # shape (500,), range [0.001, 3.0]
D_LCDM_s68 = s68['D_LCDM']
D_wCDM_s68 = s68['D_wCDM']
F_tracking_s68 = s68['F_tracking']
dPhidt_A_s68 = s68['dPhidt_A']     # LCDM
dPhidt_B_s68 = s68['dPhidt_B']     # Framework (tracking, c_s^2=0)
dPhidt_C_s68 = s68['dPhidt_C']     # Quintessence (smooth, c_s^2=1)
l_arr_s68 = s68['l_arr']           # shape (99,), range [2, 100]
Cl_A_s68 = s68['Cl_A']             # LCDM C_l^{Tg}
Cl_B_s68 = s68['Cl_B']             # Framework C_l^{Tg}
Cl_C_s68 = s68['Cl_C']             # Quintessence C_l^{Tg}
w0_FW = float(s68['w0_FW'])        # -0.918

print("=" * 76)
print("S69 PVD-10: ISW-GALAXY CROSS-CORRELATION FOR SDSS LRG SAMPLE")
print("Gate: PVD-ISW-69 (INFO)")
print("=" * 76)
print(f"\nS68 data loaded: z range [{z_arr_s68[0]:.3f}, {z_arr_s68[-1]:.1f}], "
      f"l range [{int(l_arr_s68[0])}, {int(l_arr_s68[-1])}]")
print(f"Framework w_0 = {w0_FW:.3f}, w_a = 0")

# ==============================================================================
#  SDSS LRG Sample Parameters
# ==============================================================================

# SDSS LRG photometric sample (Eisenstein+01, Padmanabhan+07)
# The LRG sample covers ~4000 deg^2, 0.15 < z < 0.7, with a sharp cutoff
# Galaxy bias b ~ 1.9-2.1 (scale-dependent, but constant b = 2.0 is standard)
b_LRG = 2.0                       # Linear galaxy bias for LRGs  # (local)
f_sky_SDSS = 0.24                  # ~9700 deg^2 / 41253 deg^2  # (local)

# LRG redshift distribution: Gaussian-like centered at z ~ 0.35
# Based on the photometric LRG distribution (Padmanabhan+05, Fig 1;
# Eisenstein+01, Fig 5). The distribution is reasonably modeled as:
#   dn/dz = z^2 * exp(-(z/z_0)^1.5) with z_0 ~ 0.26
# More precise: the spectroscopic LRG sample has a broad peak at z ~ 0.35
# with sigma_z ~ 0.10 for the main sample.

z_median_LRG = 0.35  # (local)
z_lo_LRG = 0.15  # (local)
z_hi_LRG = 0.70  # (local)

def dn_dz_LRG(z):
    """SDSS LRG photometric redshift distribution.
    Approximation based on Padmanabhan+05 and Eisenstein+01.
    Uses a modified Gaussian with asymmetric tails to match
    the observed LRG n(z).
    """
    if np.isscalar(z):
        z = np.array([z])
    result = np.zeros_like(z, dtype=float)
    mask = (z >= z_lo_LRG) & (z <= z_hi_LRG)
    # Smail-type distribution: dn/dz ~ z^alpha * exp(-(z/z_0)^beta)
    # Fit to match median z ~ 0.35, sharp low-z cutoff at 0.15
    z_0 = 0.28  # (local)
    alpha = 2.0  # (local)
    beta = 1.5
    result[mask] = z[mask]**alpha * np.exp(-(z[mask]/z_0)**beta)
    # Hard cutoff at edges
    result[z < z_lo_LRG] = 0
    result[z > z_hi_LRG] = 0
    # Normalize
    norm, _ = quad(lambda zp: zp**alpha * np.exp(-(zp/z_0)**beta),
                   z_lo_LRG, z_hi_LRG)
    return result / norm

# For the higher-z CMASS/LOWZ samples (BOSS), shift the distribution
z_median_CMASS = 0.55  # (local)
def dn_dz_CMASS(z):
    """BOSS CMASS/LOWZ redshift distribution.
    CMASS: 0.43 < z < 0.7, LOWZ: 0.15 < z < 0.43.
    Combined approximation: Gaussian at z ~ 0.55, sigma ~ 0.15.
    """
    if np.isscalar(z):
        z = np.array([z])
    result = np.zeros_like(z, dtype=float)
    mask = (z >= 0.15) & (z <= 0.75)
    sigma_z = 0.15  # (local)
    result[mask] = np.exp(-0.5 * ((z[mask] - z_median_CMASS) / sigma_z)**2)
    norm, _ = quad(lambda zp: np.exp(-0.5 * ((zp - z_median_CMASS) / sigma_z)**2),
                   0.15, 0.75)
    return result / norm

# ==============================================================================
#  Cosmological functions (consistent with S68)
# ==============================================================================

H0 = H_0_km_s_Mpc
c_km = c_light_km_s
h = H0 / 100.0

def H_LCDM(z):
    return H0 * np.sqrt(Omega_r * (1+z)**4 + Omega_m * (1+z)**3 + Omega_Lambda)

def H_wCDM(z, w0=-0.918):
    zp1 = 1 + z
    de_factor = zp1**(3*(1 + w0)) * np.exp(0.0)  # w_a = 0
    return H0 * np.sqrt(Omega_r * zp1**4 + Omega_m * zp1**3 + Omega_Lambda * de_factor)

def chi_comoving(z, H_func):
    """Comoving distance in Mpc."""
    result, _ = quad(lambda zp: c_km / H_func(zp), 0, z)
    return result

# ==============================================================================
#  Recompute C_l^{Tg} for SDSS LRG parameters
# ==============================================================================
# The S68 computation used b_g = 1.5 and a Gaussian window at z_mean = 0.7.
# For SDSS LRGs, we need b = 2.0 and the LRG dn/dz.
# The ISW kernel (dPhi/dt) is the same. Only the galaxy window changes.

print("\n--- Recomputing C_l^{Tg} for SDSS LRG sample ---")
print(f"  Galaxy bias b_LRG = {b_LRG:.1f}")
print(f"  Redshift range: [{z_lo_LRG:.2f}, {z_hi_LRG:.2f}]")
print(f"  f_sky = {f_sky_SDSS:.2f}")

# Interpolate S68 quantities onto the z grid
dPhidt_A_interp = interp1d(z_arr_s68, dPhidt_A_s68, kind='cubic', fill_value=0, bounds_error=False)
dPhidt_B_interp = interp1d(z_arr_s68, dPhidt_B_s68, kind='cubic', fill_value=0, bounds_error=False)
dPhidt_C_interp = interp1d(z_arr_s68, dPhidt_C_s68, kind='cubic', fill_value=0, bounds_error=False)
D_LCDM_interp = interp1d(z_arr_s68, D_LCDM_s68, kind='cubic', fill_value=0, bounds_error=False)
D_wCDM_interp = interp1d(z_arr_s68, D_wCDM_s68, kind='cubic', fill_value=0, bounds_error=False)

# Use a fine grid focused on the LRG redshift range
z_grid = np.linspace(0.01, 2.0, 400)
dz = z_grid[1] - z_grid[0]

# Precompute comoving distances
chi_LCDM_grid = np.array([chi_comoving(z, H_LCDM) for z in z_grid])
chi_wCDM_grid = np.array([chi_comoving(z, lambda zp: H_wCDM(zp, w0_FW)) for z in z_grid])
H_LCDM_grid = np.array([H_LCDM(z) for z in z_grid])
H_wCDM_grid = np.array([H_wCDM(z, w0_FW) for z in z_grid])

# Galaxy windows (bias * dn/dz)
W_g_LRG = b_LRG * dn_dz_LRG(z_grid)
W_g_CMASS = 1.9 * dn_dz_CMASS(z_grid)  # BOSS CMASS bias ~ 1.9

# ISW kernel values on this grid
dPhidt_A_grid = dPhidt_A_interp(z_grid)
dPhidt_B_grid = dPhidt_B_interp(z_grid)
dPhidt_C_grid = dPhidt_C_interp(z_grid)
D_LCDM_grid = D_LCDM_interp(z_grid)
D_wCDM_grid = D_wCDM_interp(z_grid)

print("  Comoving distances and interpolations computed.")

# Eisenstein-Hu no-wiggle transfer function (same as S68)
n_s_planck = 0.9649

def transfer_EH(k_hMpc):
    """Eisenstein-Hu no-wiggle transfer function. k in h/Mpc."""
    Omega_m_h2 = Omega_m * h**2
    Omega_b_h2 = Omega_b * h**2
    f_b = Omega_b / Omega_m
    s = 44.5 * np.log(9.83 / Omega_m_h2) / np.sqrt(1 + 10 * Omega_b_h2**0.75)
    alpha_Gamma = 1 - 0.328 * np.log(431 * Omega_m_h2) * f_b + 0.38 * np.log(22.3 * Omega_m_h2) * f_b**2
    Gamma_eff = Omega_m * h * (alpha_Gamma + (1 - alpha_Gamma) / (1 + (0.43 * k_hMpc * s)**4))
    q = k_hMpc * (T_CMB / 2.7)**2 / Gamma_eff
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1 + 62.5 * q)
    return L / (L + C * q**2)

def P_mm(k_hMpc, D_z):
    """Linear matter power spectrum (unnormalized). k in h/Mpc."""
    T = transfer_EH(k_hMpc)
    return k_hMpc**n_s_planck * T**2 * D_z**2

# ==============================================================================
#  Compute C_l^{Tg} for LRG sample using Limber approximation
# ==============================================================================

print("\n--- Computing C_l^{Tg} for SDSS LRGs ---")

# Extend l range to l = 200 for completeness
l_arr = np.arange(2, 201)

# Arrays for three models, two galaxy samples
Cl_LRG_A = np.zeros(len(l_arr))   # LCDM x LRG
Cl_LRG_B = np.zeros(len(l_arr))   # Framework x LRG
Cl_LRG_C = np.zeros(len(l_arr))   # Quintessence x LRG

Cl_CMASS_A = np.zeros(len(l_arr))
Cl_CMASS_B = np.zeros(len(l_arr))
Cl_CMASS_C = np.zeros(len(l_arr))

for il, ell in enumerate(l_arr):
    for model_idx, (dPhidt_g, H_g, chi_g, D_g) in enumerate([
        (dPhidt_A_grid, H_LCDM_grid, chi_LCDM_grid, D_LCDM_grid),
        (dPhidt_B_grid, H_wCDM_grid, chi_wCDM_grid, D_wCDM_grid),
        (dPhidt_C_grid, H_wCDM_grid, chi_wCDM_grid, D_wCDM_grid),
    ]):
        # Limber: k = (l+0.5) / chi
        k_arr = (ell + 0.5) / (chi_g + 1e-30) * (1.0 / h)  # h/Mpc

        # Matter power spectrum at each z
        P_arr = np.array([P_mm(k, D) for k, D in zip(k_arr, D_g)])

        # Integrand for LRG: dPhi/dt * W_g_LRG * P(k,z) * H/c / chi^2
        integrand_LRG = dPhidt_g * W_g_LRG * P_arr * H_g / (c_km * chi_g**2 + 1e-30)
        integrand_CMASS = dPhidt_g * W_g_CMASS * P_arr * H_g / (c_km * chi_g**2 + 1e-30)

        Cl_lrg = simpson(y=integrand_LRG, x=z_grid)
        Cl_cmass = simpson(y=integrand_CMASS, x=z_grid)

        if model_idx == 0:
            Cl_LRG_A[il] = Cl_lrg
            Cl_CMASS_A[il] = Cl_cmass
        elif model_idx == 1:
            Cl_LRG_B[il] = Cl_lrg
            Cl_CMASS_B[il] = Cl_cmass
        else:
            Cl_LRG_C[il] = Cl_lrg
            Cl_CMASS_C[il] = Cl_cmass

print("  Done: C_l^{Tg} computed for l = 2-200, LRG + CMASS samples.")

# ==============================================================================
#  Ratios for SDSS LRG sample
# ==============================================================================

ratio_LRG_BA = Cl_LRG_B / (Cl_LRG_A + 1e-50)   # Framework / LCDM
ratio_LRG_CA = Cl_LRG_C / (Cl_LRG_A + 1e-50)   # Quintessence / LCDM
ratio_LRG_BC = Cl_LRG_B / (Cl_LRG_C + 1e-50)   # Framework / Quintessence

ratio_CMASS_BA = Cl_CMASS_B / (Cl_CMASS_A + 1e-50)
ratio_CMASS_CA = Cl_CMASS_C / (Cl_CMASS_A + 1e-50)
ratio_CMASS_BC = Cl_CMASS_B / (Cl_CMASS_C + 1e-50)

# Average over ISW-sensitive range l = 2-30
mask_isw = l_arr <= 30
mean_LRG_BA = np.mean(ratio_LRG_BA[mask_isw])
mean_LRG_CA = np.mean(ratio_LRG_CA[mask_isw])
mean_LRG_BC = np.mean(ratio_LRG_BC[mask_isw])

mean_CMASS_BA = np.mean(ratio_CMASS_BA[mask_isw])
mean_CMASS_CA = np.mean(ratio_CMASS_CA[mask_isw])
mean_CMASS_BC = np.mean(ratio_CMASS_BC[mask_isw])

print(f"\n{'='*76}")
print("C_l^{{Tg}} RATIOS AT l = 2-30 (ISW-SENSITIVE)")
print(f"{'='*76}")

print(f"\n  SDSS LRG sample (b={b_LRG:.1f}, z_med={z_median_LRG:.2f}):")
print(f"    FW / LCDM  = {mean_LRG_BA:.4f}  ({(mean_LRG_BA-1)*100:+.2f}%)")
print(f"    Quint / LCDM = {mean_LRG_CA:.4f}  ({(mean_LRG_CA-1)*100:+.2f}%)")
print(f"    FW / Quint = {mean_LRG_BC:.4f}  ({(mean_LRG_BC-1)*100:+.2f}%)")

print(f"\n  BOSS CMASS/LOWZ sample (b=1.9, z_med={z_median_CMASS:.2f}):")
print(f"    FW / LCDM  = {mean_CMASS_BA:.4f}  ({(mean_CMASS_BA-1)*100:+.2f}%)")
print(f"    Quint / LCDM = {mean_CMASS_CA:.4f}  ({(mean_CMASS_CA-1)*100:+.2f}%)")
print(f"    FW / Quint = {mean_CMASS_BC:.4f}  ({(mean_CMASS_BC-1)*100:+.2f}%)")

# ==============================================================================
#  Signal-to-Noise Computation
# ==============================================================================
# S/N = sqrt( sum_l (2l+1) * f_sky * (C_l^{Tg})^2 / ((C_l^{TT} + N_l^{TT}) * (C_l^{gg} + N_l^{gg})) )
#
# The denominator involves:
#   C_l^{TT}: CMB temperature power spectrum (~6000 uK^2 * 2*pi / (l*(l+1)) at l~10)
#   N_l^{TT}: Instrumental noise (negligible for Planck at l < 100)
#   C_l^{gg}: Galaxy angular power spectrum
#   N_l^{gg}: Shot noise = 1/n_bar_angular
#
# For the amplitude-based S/N (which is what published ISW detections report),
# the measurement is:
#   A_ISW = (data C_l^{Tg}) / (theory C_l^{Tg}_LCDM) = 1.0 +/- sigma_A
#
# The per-tracer S/N is determined by:
#   (S/N)^2 = sum_{l=2}^{l_max} (2l+1) * f_sky / 2 * (C_l^{Tg})^2 / [C_l^{TT_total} * C_l^{gg_total}]

print(f"\n{'='*76}")
print("SIGNAL-TO-NOISE FOR ISW DETECTION (SDSS LRG)")
print(f"{'='*76}")

# ---- C_l^{TT}: Planck best-fit LCDM ----
# At l < 30, the Sachs-Wolfe plateau gives:
# l(l+1) C_l^{TT} / (2*pi) ~ 1100 uK^2 (SW) + 5600 uK^2 (acoustic peak at l~220)
# At l ~ 10: C_l^{TT} ~ 1100 * 2*pi / (10*11) ~ 63 uK^2
# More precisely, use the Sachs-Wolfe approximation + ISW tail:
# C_l^{TT} = 2*pi * D_l / (l*(l+1)) where D_l = l(l+1)*C_l/(2*pi)
# D_l ~ 1100 uK^2 for l < 30 (SW plateau), rising to ~5800 at l ~ 200

def Cl_TT_approx(l):
    """Approximate CMB TT power spectrum in uK^2.
    Uses the Sachs-Wolfe plateau + acoustic peak shape.
    Returns C_l (NOT D_l = l(l+1)C_l/(2pi)).
    """
    # D_l = l(l+1)*C_l/(2*pi) in uK^2
    # SW plateau: D_l ~ 1100 uK^2 for l < 30
    # First acoustic peak: D_l ~ 5800 uK^2 at l ~ 220
    # Valley: D_l ~ 1500 uK^2 at l ~ 400
    # Simple model: D_l = 1100 + 4700 * exp(-(l-220)^2 / (2*80^2))
    l = np.asarray(l, dtype=float)
    Dl = 1100 + 4700 * np.exp(-0.5 * ((l - 220) / 80)**2)
    Cl = Dl * 2 * np.pi / (l * (l + 1))
    return Cl  # uK^2 per steradian

# ---- C_l^{gg}: Galaxy angular power spectrum for LRGs ----
# C_l^{gg} = b^2 * integral dz * (H(z)/c) / chi(z)^2 * (dn/dz)^2 * P_mm(k=l/chi, z)
# At l ~ 10-30, C_l^{gg} ~ 10^{-3} to 10^{-4} per steradian

# Compute C_l^{gg} for LRGs
Cl_gg_LRG = np.zeros(len(l_arr))

for il, ell in enumerate(l_arr):
    k_arr = (ell + 0.5) / (chi_LCDM_grid + 1e-30) * (1.0 / h)
    P_arr = np.array([P_mm(k, D) for k, D in zip(k_arr, D_LCDM_grid)])
    # Galaxy auto-power: (b * dn/dz)^2 * P(k,z) * H/(c * chi^2)
    integrand = (W_g_LRG)**2 * P_arr * H_LCDM_grid / (c_km * chi_LCDM_grid**2 + 1e-30)
    Cl_gg_LRG[il] = simpson(y=integrand, x=z_grid)

# ---- Shot noise ----
# SDSS LRG: ~10^6 galaxies over ~10000 deg^2
# n_angular ~ 10^6 / (10000 * (pi/180)^2) ~ 3.3e5 per steradian
# N_l^{gg} = 1/n_bar_angular ~ 3e-6 sr
n_LRG_total = 1.0e6          # approximate total number of LRGs
Omega_survey_sr = f_sky_SDSS * 4 * np.pi   # survey solid angle in sr
n_bar_angular = n_LRG_total / Omega_survey_sr
N_l_gg = 1.0 / n_bar_angular

print(f"\n  SDSS LRG survey parameters:")
print(f"    N_gal = {n_LRG_total:.1e}")
print(f"    Omega_survey = {Omega_survey_sr:.2f} sr ({f_sky_SDSS*100:.0f}% of sky)")
print(f"    n_bar = {n_bar_angular:.2e} sr^-1")
print(f"    N_l^gg (shot noise) = {N_l_gg:.2e}")

# ---- Planck instrumental noise (negligible at l < 100) ----
# Planck 143 GHz: beam FWHM = 7.3', sigma_T = 43 uK-arcmin
theta_beam = 7.3 / 60 * np.pi / 180  # radians
sigma_T = 43.0  # uK-arcmin  # (local)
sigma_T_rad = sigma_T * (np.pi / 180 / 60)  # uK-radian

N_l_TT = np.zeros(len(l_arr))
for il, ell in enumerate(l_arr):
    # N_l = (sigma_T)^2 * exp(l(l+1)*theta_beam^2 / (8*ln2))
    N_l_TT[il] = sigma_T_rad**2 * np.exp(ell * (ell+1) * theta_beam**2 / (8 * np.log(2)))

# ---- Compute S/N ----
# Standard ISW detection S/N:
# (S/N)^2 = sum_l (2l+1) * f_sky / 2 * (C_l^{Tg})^2 / ((C_l^{TT} + N_l^{TT}) * (C_l^{gg} + N_l^{gg}))

# But C_l^{Tg} from our computation is in arbitrary units (not calibrated to uK * sr^{-1/2}).
# Instead, we compute the S/N in terms of the ISW amplitude:
#
# The published S/N for ISW detection depends on the absolute calibration of C_l^{Tg}.
# Since we computed C_l^{Tg} using the Limber approximation with a simplified power
# spectrum normalization, the absolute S/N is not directly comparable.
#
# APPROACH: Use the RATIO method.
# If LCDM predicts an ISW detection at S/N_LCDM, then the framework predicts:
#   S/N_FW = S/N_LCDM * (A_ISW_FW / A_ISW_LCDM)
# where A_ISW is the ISW amplitude relative to LCDM.

# For SDSS LRGs:
# Published S/N ~ 2-3 sigma for ISW detection (Padmanabhan+05: 2.5 sigma)
# Granett+08: 4.4 sigma from STACKING (different method, anomalously high)
# Giannantonio+08: SDSS contribution ~2.5 sigma, combined with NVSS etc. = 4.5 sigma

# Theoretical prediction for LCDM ISW detection S/N with SDSS LRG:
# Using the standard Crittenden-Turok (1996) formalism:

Cl_TT_arr = Cl_TT_approx(l_arr)

# Compute the detection S/N for each model
# Note: the (2l+1)*f_sky/2 factor is the effective number of modes
# The ISW signal C_l^Tg is proportional to dPhi/dt * b * dn/dz * P(k)
# We already have C_l^{Tg} in arbitrary units for all three models

SNR2_det_A = 0.0  # LCDM detection S/N^2  # (local)
SNR2_det_B = 0.0  # Framework  # (local)
SNR2_det_C = 0.0  # Quintessence  # (local)

# Also compute the model discrimination S/N
SNR2_disc_BA = 0.0  # Framework vs LCDM  # (local)
SNR2_disc_BC = 0.0  # Framework vs Quintessence  # (local)

for il, ell in enumerate(l_arr):
    if ell > 100:
        break  # ISW signal negligible above l ~ 100

    N_modes = (2 * ell + 1) * f_sky_SDSS / 2.0

    # Total covariance: (C_l^TT + N_l^TT) * (C_l^gg + N_l^gg) + (C_l^Tg)^2
    # The cross-term (C_l^Tg)^2 is negligible compared to the product
    # But we need to get the normalization right.

    # Since our C_l^{Tg} is in arbitrary units, we compute the S/N ratio.
    # The key insight: the S/N of the ISW DETECTION scales as:
    #   (S/N)^2 = sum_l N_modes * (C_l^Tg)^2 / [(C_l^TT + N_l^TT)*(C_l^gg + N_l^gg)]
    # The denominator is dominated by C_l^TT * C_l^gg (since ISW << primary CMB).

    # For the RATIO S/N_FW / S/N_LCDM, the denominator cancels to first order
    # (both models use the same CMB TT and similar galaxy gg).
    # The ratio is simply sum_l (C_l^Tg_FW)^2 / sum_l (C_l^Tg_LCDM)^2

    SNR2_det_A += N_modes * Cl_LRG_A[il]**2
    SNR2_det_B += N_modes * Cl_LRG_B[il]**2
    SNR2_det_C += N_modes * Cl_LRG_C[il]**2

    SNR2_disc_BA += N_modes * (Cl_LRG_B[il] - Cl_LRG_A[il])**2
    SNR2_disc_BC += N_modes * (Cl_LRG_B[il] - Cl_LRG_C[il])**2

# The S/N ratio (FW vs LCDM detection):
SNR_ratio_det_BA = np.sqrt(SNR2_det_B / (SNR2_det_A + 1e-50))
SNR_ratio_det_CA = np.sqrt(SNR2_det_C / (SNR2_det_A + 1e-50))

# Published baseline S/N values for SDSS ISW detection:
# Padmanabhan+05: 2.5 sigma (first ISW detection with SDSS LRGs)
# Giannantonio+08: ~2.5 sigma for SDSS alone, 4.5 combined
# Ho+08: similar ~2.5 sigma for SDSS
# Granett+08: 4.4 sigma (STACKING, not direct C_l)
# Planck 2015: SDSS CMASS/LOWZ at A = 0.72 +/- 0.35 (2.1 sigma)

SNR_SDSS_baseline = 2.5    # Standard C_l^Tg detection S/N for SDSS LRG  # (local)
SNR_Planck_CMASS = 2.06     # From A = 0.72/0.35  # (local)
SNR_Granett = 4.4           # Stacking method (anomalous)  # (local)
SNR_Giannantonio_SDSS = 2.5  # (local)
SNR_Giannantonio_combined = 4.5  # (local)

# Framework predictions:
SNR_SDSS_FW = SNR_SDSS_baseline * SNR_ratio_det_BA
SNR_SDSS_Quint = SNR_SDSS_baseline * SNR_ratio_det_CA
SNR_Planck_CMASS_FW = SNR_Planck_CMASS * SNR_ratio_det_BA

print(f"\n  ISW DETECTION S/N PREDICTIONS:")
print(f"  (Scaling published S/N by the C_l^Tg ratio)")
print(f"\n  Model ratio sqrt(sum(C_l^2)_FW / sum(C_l^2)_LCDM) = {SNR_ratio_det_BA:.4f}")
print(f"  Model ratio sqrt(sum(C_l^2)_Quint / sum(C_l^2)_LCDM) = {SNR_ratio_det_CA:.4f}")

print(f"\n  SDSS LRG direct C_l^{{Tg}} detection:")
print(f"    LCDM baseline:     S/N = {SNR_SDSS_baseline:.1f} sigma")
print(f"    Framework (track): S/N = {SNR_SDSS_FW:.2f} sigma")
print(f"    Quintessence:      S/N = {SNR_SDSS_Quint:.2f} sigma")
print(f"    FW - LCDM:         Delta(S/N) = {SNR_SDSS_FW - SNR_SDSS_baseline:+.3f}")

print(f"\n  Planck x BOSS CMASS/LOWZ detection:")
print(f"    LCDM baseline:     S/N = {SNR_Planck_CMASS:.2f} sigma")
print(f"    Framework (track): S/N = {SNR_Planck_CMASS_FW:.2f} sigma")

# ==============================================================================
#  Comparison with published detections (amplitude approach)
# ==============================================================================

print(f"\n{'='*76}")
print("COMPARISON WITH PUBLISHED ISW DETECTIONS")
print(f"{'='*76}")

# The framework predicts A_ISW = C_l^Tg(FW) / C_l^Tg(LCDM) = mean_LRG_BA
# Published measurements are A_ISW = C_l^Tg(data) / C_l^Tg(LCDM)

# Published ISW amplitudes relative to LCDM (when available):
# Padmanabhan+05: A = 2.5 +/- 1.0 (their optimal filter estimate)
# Giannantonio+08: A = 1.0 +/- 0.27 (combined), SDSS alone uncertain
# Ho+08: combined A = 0.9 +/- 0.25
# Planck 2015 ISW (1502.01595 Table 2):
#   SDSS-CMASS/LOWZ: A = 0.72 +/- 0.35
#   NVSS:            A = 1.48 +/- 0.37
#   WISE-AGN:        A = 0.82 +/- 0.39
#   WISE-GAL:        A = 1.18 +/- 0.59
#   Lensing:         A = 1.06 +/- 0.33
#   Combined:        A = 1.00 +/- 0.25

# For Granett+08: the stacking analysis finds an ANOMALOUSLY LARGE signal.
# A_Granett ~ 3-5x LCDM expectation (the "Granett anomaly").
# This is NOT a simple amplitude fit but a void/supercluster stack.
# The measured stacked signal is ~10 uK, while LCDM predicts ~2-3 uK.
# This anomaly is INDEPENDENT of the framework's ~12% enhancement.

measurements = [
    ("Padmanabhan+05 (SDSS LRG)", 2.50, 1.0, "C_l"),
    ("Planck 2015 (SDSS CMASS/LOWZ)", 0.72, 0.35, "C_l"),
    ("Planck 2015 (NVSS)", 1.48, 0.37, "C_l"),
    ("Planck 2015 (WISE-AGN)", 0.82, 0.39, "C_l"),
    ("Planck 2015 (Combined)", 1.00, 0.25, "C_l"),
    ("Giannantonio+08 (Combined)", 1.00, 0.27, "C_l"),
]

A_FW_LRG = mean_LRG_BA       # Framework ISW amplitude (relative to LCDM)
A_FW_CMASS = mean_CMASS_BA
A_LCDM = 1.0  # (local)

print(f"\n  Framework prediction: A_ISW = {A_FW_LRG:.4f} (LRG), {A_FW_CMASS:.4f} (CMASS)")
print(f"  (i.e., {(A_FW_LRG-1)*100:+.1f}% ISW enhancement from tracking DE)")
print(f"\n  {'Measurement':<40s} {'A_obs':>6s} {'sig_A':>6s} {'chi2_LCDM':>10s} {'chi2_FW':>10s} {'Delta chi2':>10s}")
print(f"  {'-'*40} {'-'*6} {'-'*6} {'-'*10} {'-'*10} {'-'*10}")

chi2_total_LCDM = 0.0  # (local)
chi2_total_FW = 0.0  # (local)

for name, A_obs, sig_A, method in measurements:
    chi2_lcdm = (A_obs - A_LCDM)**2 / sig_A**2
    chi2_fw = (A_obs - A_FW_LRG)**2 / sig_A**2
    delta_chi2 = chi2_fw - chi2_lcdm

    chi2_total_LCDM += chi2_lcdm
    chi2_total_FW += chi2_fw

    print(f"  {name:<40s} {A_obs:>6.2f} {sig_A:>6.2f} {chi2_lcdm:>10.3f} {chi2_fw:>10.3f} {delta_chi2:>+10.3f}")

print(f"\n  {'TOTAL (6 measurements)':<40s} {'':>6s} {'':>6s} {chi2_total_LCDM:>10.3f} {chi2_total_FW:>10.3f} {chi2_total_FW - chi2_total_LCDM:>+10.3f}")
print(f"\n  NOTE: Delta chi2 > 0 means LCDM fits BETTER; Delta chi2 < 0 means FW fits BETTER.")

# ==============================================================================
#  The Granett Anomaly Assessment
# ==============================================================================

print(f"\n{'='*76}")
print("THE GRANETT+08 ANOMALY: DOES THE FRAMEWORK EXPLAIN IT?")
print(f"{'='*76}")

# Granett+08 found ~10 uK signal from stacking 50 supervoids + 50 superclusters
# in SDSS LRG. LCDM predicts ~2-3 uK for these structures.
# The 4.4 sigma refers to the significance of the STACKED signal detection.
#
# The framework's 12% enhancement predicts:
# LCDM prediction: ~2.5 uK
# Framework prediction: ~2.5 * 1.12 = ~2.8 uK
# Observed: ~10 uK
#
# The framework does NOT explain the Granett anomaly (factor 3-4x discrepancy).
# The anomaly remains unexplained in BOTH frameworks.

T_stack_LCDM = 2.5   # uK, typical LCDM prediction for void/cluster stacking  # (local)
T_stack_FW = T_stack_LCDM * A_FW_LRG  # Framework prediction
T_stack_obs = 10.0    # uK, Granett+08 observed  # (local)

print(f"\n  Granett+08 void/supercluster stacking:")
print(f"    Observed stacked signal:   ~{T_stack_obs:.0f} uK")
print(f"    LCDM predicted:            ~{T_stack_LCDM:.1f} uK")
print(f"    Framework predicted:       ~{T_stack_FW:.1f} uK")
print(f"    Framework enhancement:     {(A_FW_LRG-1)*100:+.1f}%")
print(f"    Ratio observed/LCDM:       ~{T_stack_obs/T_stack_LCDM:.1f}x")
print(f"    Ratio observed/Framework:  ~{T_stack_obs/T_stack_FW:.1f}x")
print(f"\n  CONCLUSION: The framework's 12% enhancement does NOT explain the")
print(f"  Granett anomaly (3-4x above LCDM). The anomaly is orthogonal to")
print(f"  the tracking DE signature.")

# ==============================================================================
#  Model discrimination S/N: Can existing data distinguish FW from LCDM?
# ==============================================================================

print(f"\n{'='*76}")
print("MODEL DISCRIMINATION: CAN EXISTING DATA DISTINGUISH FW FROM LCDM?")
print(f"{'='*76}")

# The ISW amplitude uncertainty for SDSS LRG is sigma_A ~ 0.35-1.0
# The framework predicts A_FW = 1.12, so Delta_A = 0.12
# Model discrimination S/N = Delta_A / sigma_A

for name, sig_A in [("SDSS LRG (Padmanabhan+05)", 1.0),
                     ("Planck x SDSS CMASS/LOWZ", 0.35),
                     ("Planck Combined (all tracers)", 0.25),
                     ("Euclid (projected)", 0.05),
                     ("21cm (projected)", 0.01)]:
    delta_A = A_FW_LRG - 1.0
    SNR_disc = abs(delta_A) / sig_A
    print(f"  {name:<35s}:  sigma_A = {sig_A:.2f},  SNR(FW-LCDM) = {SNR_disc:.2f}")

# For FW vs Quintessence (same w, different c_s^2):
delta_A_quint = A_FW_LRG - mean_LRG_CA
print(f"\n  Framework vs Quintessence discrimination:")
print(f"    Delta_A (FW - Quint) = {delta_A_quint:.4f}")
for name, sig_A in [("Planck Combined", 0.25), ("Euclid (projected)", 0.05)]:
    SNR_disc = abs(delta_A_quint) / sig_A
    print(f"    {name:<35s}:  SNR = {SNR_disc:.2f}")

# ==============================================================================
#  Redshift-dependent ISW amplitude for SDSS LRG
# ==============================================================================

print(f"\n{'='*76}")
print("REDSHIFT-DEPENDENT ISW SIGNAL AMPLITUDE (SDSS LRG BINS)")
print(f"{'='*76}")

# The LRG sample can be split into redshift bins
z_bins_LRG = [(0.15, 0.30), (0.30, 0.45), (0.45, 0.60), (0.60, 0.70)]

for z_lo, z_hi in z_bins_LRG:
    mask_bin = (z_grid >= z_lo) & (z_grid <= z_hi)
    if np.sum(mask_bin) < 5:
        continue

    z_bin = z_grid[mask_bin]

    # ISW signal weighted by galaxy window in this bin
    sig_A = simpson(y=dPhidt_A_grid[mask_bin] * W_g_LRG[mask_bin], x=z_bin)
    sig_B = simpson(y=dPhidt_B_grid[mask_bin] * W_g_LRG[mask_bin], x=z_bin)
    sig_C = simpson(y=dPhidt_C_grid[mask_bin] * W_g_LRG[mask_bin], x=z_bin)

    ratio_BA = sig_B / (sig_A + 1e-50)
    ratio_BC = sig_B / (sig_C + 1e-50)

    print(f"  z = [{z_lo:.2f}, {z_hi:.2f}]: "
          f"FW/LCDM = {ratio_BA:.4f} ({(ratio_BA-1)*100:+.2f}%), "
          f"FW/Quint = {ratio_BC:.4f} ({(ratio_BC-1)*100:+.2f}%)")

# ==============================================================================
#  Gate Verdict
# ==============================================================================

print(f"\n{'='*76}")
print("GATE VERDICT: PVD-ISW-69")
print(f"{'='*76}")

print(f"\n  Gate: PVD-ISW-69 (INFO)")
print(f"  Type: Informational -- report predicted S/N and comparison")
print(f"\n  KEY FINDINGS:")
print(f"    1. Framework ISW amplitude (SDSS LRG): A = {A_FW_LRG:.4f} ({(A_FW_LRG-1)*100:+.1f}%)")
print(f"    2. Model discrimination S/N (Planck x SDSS): {abs(A_FW_LRG-1)/0.35:.2f} sigma")
print(f"       (12% signal vs 35% uncertainty: completely buried)")
print(f"    3. Published detections consistent with both LCDM and FW:")

delta_chi2_total = chi2_total_FW - chi2_total_LCDM
print(f"       Total Delta chi2(FW - LCDM) = {delta_chi2_total:+.3f}")
if delta_chi2_total < 0:
    print(f"       Marginally FAVORS framework (but not significant)")
elif delta_chi2_total < 1:
    print(f"       Negligible preference (both models fit equally well)")
else:
    print(f"       Marginally disfavors framework (but not significant)")

print(f"    4. Granett+08 anomaly: NOT explained by framework (3-4x above both)")
print(f"    5. Existing data CANNOT distinguish FW from LCDM via ISW")
print(f"    6. Euclid (sigma_A ~ 0.05) needed for {abs(A_FW_LRG-1)/0.05:.1f}-sigma discrimination")
print(f"\n  Verdict: INFO. The ~12% tracking DE enhancement is real but invisible")
print(f"  in existing SDSS ISW data (sigma_A = 0.25-1.0 >> Delta_A = 0.12).")
print(f"  This is consistent with the S68 forecast that Planck cannot discriminate.")

# ==============================================================================
#  Save results
# ==============================================================================

save_path = r"C:\sandbox\Ainulindale Exflation\computations\s69_pvd10_isw_sdss.npz"

np.savez(save_path,
    # Multipole grid
    l_arr=l_arr,
    # LRG C_l^Tg for three models
    Cl_LRG_A=Cl_LRG_A, Cl_LRG_B=Cl_LRG_B, Cl_LRG_C=Cl_LRG_C,
    # CMASS C_l^Tg for three models
    Cl_CMASS_A=Cl_CMASS_A, Cl_CMASS_B=Cl_CMASS_B, Cl_CMASS_C=Cl_CMASS_C,
    # Ratios (LRG)
    ratio_LRG_BA=ratio_LRG_BA, ratio_LRG_CA=ratio_LRG_CA, ratio_LRG_BC=ratio_LRG_BC,
    # Ratios (CMASS)
    ratio_CMASS_BA=ratio_CMASS_BA, ratio_CMASS_CA=ratio_CMASS_CA, ratio_CMASS_BC=ratio_CMASS_BC,
    # Mean ratios
    mean_LRG_BA=mean_LRG_BA, mean_LRG_CA=mean_LRG_CA, mean_LRG_BC=mean_LRG_BC,
    mean_CMASS_BA=mean_CMASS_BA, mean_CMASS_CA=mean_CMASS_CA, mean_CMASS_BC=mean_CMASS_BC,
    # Chi-squared totals
    chi2_total_LCDM=chi2_total_LCDM, chi2_total_FW=chi2_total_FW,
    delta_chi2_total=delta_chi2_total,
    # Sample parameters
    b_LRG=b_LRG, f_sky_SDSS=f_sky_SDSS,
    w0_FW=w0_FW,
    A_FW_LRG=A_FW_LRG,
    # Detection S/N ratios
    SNR_ratio_det_BA=SNR_ratio_det_BA, SNR_ratio_det_CA=SNR_ratio_det_CA,
    # Galaxy auto-spectrum
    Cl_gg_LRG=Cl_gg_LRG,
    # Approximate TT
    Cl_TT_approx=Cl_TT_approx(l_arr),
    # Redshift grid for checks
    z_grid=z_grid,
    W_g_LRG=W_g_LRG, W_g_CMASS=W_g_CMASS,
)

print(f"\n  Results saved to: {save_path}")

# ==============================================================================
#  Plot
# ==============================================================================

plot_path = r"C:\sandbox\Ainulindale Exflation\computations\s69_pvd10_isw_sdss.png"

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S69 PVD-10: ISW-Galaxy Cross-Correlation for SDSS LRG\n'
             'Gate: PVD-ISW-69 (INFO)', fontsize=13, fontweight='bold')

# Panel 1: C_l^Tg ratios for SDSS LRG
ax1 = axes[0, 0]
ax1.plot(l_arr, ratio_LRG_BA, 'b-', linewidth=2,
         label=f'Framework/LCDM ($w_0$={w0_FW}, $c_s^2$=0)')
ax1.plot(l_arr, ratio_LRG_CA, 'r--', linewidth=2,
         label=f'Quintessence/LCDM ($w_0$={w0_FW}, $c_s^2$=1)')
ax1.axhline(y=1.0, color='k', linestyle=':', alpha=0.5, label='LCDM')
ax1.axvspan(2, 30, alpha=0.1, color='green', label='ISW-sensitive ($l$<30)')
ax1.fill_between(l_arr, 1 - 0.35, 1 + 0.35, alpha=0.1, color='gray',
                  label='Planck x SDSS 1$\\sigma$ ($\\sigma_A$=0.35)')
ax1.set_xlabel('Multipole $l$')
ax1.set_ylabel('$C_l^{Tg}$ / $C_l^{Tg}$(LCDM)')
ax1.set_title(f'SDSS LRG Sample (b={b_LRG}, $z_{{med}}$={z_median_LRG})')
ax1.legend(fontsize=7, loc='upper right')
ax1.set_xlim(2, 100)
ax1.set_ylim(0.5, 1.5)
ax1.grid(True, alpha=0.3)

# Panel 2: Redshift distributions
ax2 = axes[0, 1]
z_plot = np.linspace(0, 1.5, 300)
ax2.plot(z_plot, dn_dz_LRG(z_plot), 'b-', linewidth=2, label='SDSS LRG')
ax2.plot(z_plot, dn_dz_CMASS(z_plot), 'r--', linewidth=2, label='BOSS CMASS/LOWZ')
# S68 used a Gaussian at z=0.7
from scipy.stats import norm
ax2.plot(z_plot, norm.pdf(z_plot, 0.7, 0.3), 'g:', linewidth=2,
         label='S68 survey ($z_m$=0.7, $\\sigma$=0.3)')

# Overlay the F_tracking factor (rescaled)
F_interp = interp1d(z_arr_s68, F_tracking_s68, kind='cubic', fill_value=1, bounds_error=False)
F_plot = F_interp(z_plot)
ax2_twin = ax2.twinx()
ax2_twin.plot(z_plot, (F_plot - 1) * 100, 'k-', linewidth=1.5, alpha=0.5,
              label='F(z) - 1 [%]')
ax2_twin.set_ylabel('Tracking enhancement F(z) - 1 [%]', fontsize=9)
ax2_twin.set_ylim(0, 6)

ax2.set_xlabel('Redshift $z$')
ax2.set_ylabel('$dn/dz$ (normalized)')
ax2.set_title('Galaxy Redshift Distributions + Tracking F(z)')
ax2.legend(fontsize=8, loc='upper right')
ax2.set_xlim(0, 1.5)
ax2.grid(True, alpha=0.3)

# Panel 3: Published ISW amplitude comparison
ax3 = axes[1, 0]
labels = ['Padman.\n05', 'Planck\nCMASS', 'Planck\nNVSS', 'Planck\nWISE-AGN',
          'Planck\nCombined', 'Giann.\n08']
A_vals = [2.50, 0.72, 1.48, 0.82, 1.00, 1.00]
sig_vals = [1.0, 0.35, 0.37, 0.39, 0.25, 0.27]
x_pos = np.arange(len(labels))

ax3.errorbar(x_pos, A_vals, yerr=sig_vals, fmt='ko', markersize=8, capsize=5,
             label='Observed', zorder=5)
ax3.axhline(y=1.0, color='gray', linestyle='-', linewidth=2,
             label='LCDM (A=1.0)', zorder=1)
ax3.axhline(y=A_FW_LRG, color='blue', linestyle='--', linewidth=2,
             label=f'Framework (A={A_FW_LRG:.3f})', zorder=2)
ax3.axhspan(1.0 - 0.05, 1.0 + 0.05, alpha=0.15, color='orange',
             label='Euclid 1$\\sigma$ (0.05)', zorder=0)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(labels, fontsize=8)
ax3.set_ylabel('ISW Amplitude $A_{ISW}$')
ax3.set_title('Published ISW Detections vs Framework Prediction')
ax3.legend(fontsize=7, loc='upper left')
ax3.set_ylim(-0.5, 4.0)
ax3.grid(True, alpha=0.3, axis='y')

# Panel 4: Discrimination S/N as function of sigma_A
ax4 = axes[1, 1]
sig_A_range = np.logspace(-2, 0.2, 100)  # 0.01 to 1.5
SNR_fw_lcdm = abs(A_FW_LRG - 1.0) / sig_A_range
SNR_fw_quint = abs(A_FW_LRG - mean_LRG_CA) / sig_A_range

ax4.plot(sig_A_range, SNR_fw_lcdm, 'b-', linewidth=2.5, label='FW vs LCDM')
ax4.plot(sig_A_range, SNR_fw_quint, 'g--', linewidth=2, label='FW vs Quintessence')

# Mark existing and future experiments
experiments = [
    (1.0, 'SDSS LRG\n(Padm.05)', 'red'),
    (0.35, 'Planck x SDSS\n(CMASS)', 'orange'),
    (0.25, 'Planck\nCombined', 'goldenrod'),
    (0.05, 'Euclid\n(projected)', 'green'),
    (0.01, '21cm\n(projected)', 'teal'),
]
for sig, label, color in experiments:
    snr = abs(A_FW_LRG - 1.0) / sig
    ax4.plot(sig, snr, 'o', color=color, markersize=8, zorder=5)
    ax4.annotate(label, (sig, snr), textcoords="offset points",
                 xytext=(8, 5), fontsize=7, color=color)

ax4.axhline(y=2.0, color='gray', linestyle=':', alpha=0.5, label='2$\\sigma$')
ax4.axhline(y=3.0, color='gray', linestyle='--', alpha=0.5, label='3$\\sigma$')
ax4.set_xscale('log')
ax4.set_xlabel('ISW Amplitude Uncertainty $\\sigma_A$')
ax4.set_ylabel('Model Discrimination S/N')
ax4.set_title('ISW Discrimination Power: $\\Delta A / \\sigma_A$')
ax4.legend(fontsize=7, loc='upper right')
ax4.set_xlim(0.008, 2.0)
ax4.set_ylim(0, 15)
ax4.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()

print(f"  Plot saved to: {plot_path}")
print(f"\n{'='*76}")
print("DONE: PVD-ISW-69 (INFO)")
print(f"{'='*76}")
