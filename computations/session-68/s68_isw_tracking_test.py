#!/usr/bin/env python3
"""
s68_isw_tracking_test.py — ISW Tracking Signature Test
========================================================

Session 68, Gate: ISW-TRACKING-68 (INFO)

Computes the ISW-galaxy cross-correlation C_l^{Tg} for three dark energy models:
  Model A: LCDM (w=-1, no DE perturbations)
  Model B: Framework (w_0=-0.918, w_a=0, c_s^2_DE=0, tracking vacuum)
  Model C: Quintessence (w_0=-0.918, w_a=0, c_s^2_DE=1, smooth DE)

Physics:
  The Volovik tracking vacuum (rho_vac = chi * H^2) produces INDUCED dark energy
  perturbations with effective sound speed c_s^2_DE = 0. This means DE clusters
  with matter on sub-horizon scales: delta_DE = (1+w)/(1-3w) * delta_m.
  Standard LCDM has no DE perturbations. Standard quintessence has c_s^2_DE = 1.
  The clustering modifies the ISW-galaxy cross-correlation at l < 30 by changing
  the time derivative of the gravitational potential.

Pre-registration (from S68 Volovik-Mack workshop):
  PASS if Delta(C_l^Tg)/C_l^Tg > 5% at l < 30 (above Euclid threshold)
  FAIL if Delta < 1% (below cosmic variance floor)
  INFO otherwise

Observational comparison:
  Planck 2015 ISW (1502.01595): A_ISW = 1.00 +/- 0.25 (ISW-lensing)
  ISW detection at 4-sigma combining all tracers (NVSS, SDSS, WISE, lensing)

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
#  Framework parameters
# ==============================================================================
# w0_FW = -0.918       # Framework w_0 from Volovik vacuum + effacement (S68)  # S72: now imported from canonical_constants
# wa_FW = 0.0          # w_a = 0 locked (four-fold protection, S68 workshop)  # S72: now imported from canonical_constants

# Planck ISW measurement (1502.01595v2)
# A_ISW = amplitude relative to LCDM prediction
# From ISW-lensing bispectrum: A_ISW = 1.0 +/- 0.25
# From combined ISW-galaxy (all tracers): detection at ~4 sigma
# Per-tracer amplitudes (Table 2 of Planck 2015 ISW paper):
#   NVSS:     A = 1.48 +/- 0.37
#   SDSS-CMASS/LOWZ: A = 0.72 +/- 0.35
#   SDSS-MphG: A = 0.93 +/- 0.44
#   WISE-AGN: A = 0.82 +/- 0.39
#   WISE-GAL: A = 1.18 +/- 0.59
#   Lensing:  A = 1.06 +/- 0.33
A_ISW_planck = 1.00       # Combined ISW amplitude (relative to LCDM)  # (local)
sigma_A_ISW = 0.25         # 1-sigma uncertainty (ISW-lensing bispectrum)  # (local)

# For the cross-correlation measurement per tracer, the uncertainties on
# individual multipoles are much larger. We use the overall amplitude.

# ==============================================================================
#  Cosmological functions
# ==============================================================================

H0 = H_0_km_s_Mpc  # km/s/Mpc
c = c_light_km_s    # km/s

def H_LCDM(z):
    """Hubble parameter for flat LCDM in km/s/Mpc."""
    return H0 * np.sqrt(Omega_r * (1+z)**4 + Omega_m * (1+z)**3 + Omega_Lambda)

def H_wCDM(z, w0, wa=0.0):
    """Hubble parameter for flat w0waCDM in km/s/Mpc.
    DE density: Omega_DE(z) = Omega_Lambda * (1+z)^(3(1+w0+wa)) * exp(-3*wa*z/(1+z))
    """
    zp1 = 1 + z
    de_factor = zp1**(3*(1 + w0 + wa)) * np.exp(-3 * wa * z / zp1)
    return H0 * np.sqrt(Omega_r * zp1**4 + Omega_m * zp1**3 + Omega_Lambda * de_factor)

def comoving_distance(z, H_func, **kwargs):
    """Comoving distance chi(z) in Mpc/h, integrating c*dz/H(z)."""
    result, _ = quad(lambda zp: c / H_func(zp, **kwargs), 0, z)
    return result  # Mpc (not Mpc/h since H0 in km/s/Mpc)

def Omega_m_of_z(z, H_func, **kwargs):
    """Matter density parameter as function of redshift."""
    Hz = H_func(z, **kwargs)
    return Omega_m * (1+z)**3 * (H0/Hz)**2

def Omega_DE_of_z(z, w0, wa=0.0):
    """Dark energy density parameter as function of redshift."""
    zp1 = 1 + z
    de_factor = zp1**(3*(1 + w0 + wa)) * np.exp(-3 * wa * z / zp1)
    Hz = H_wCDM(z, w0, wa)
    return Omega_Lambda * de_factor * (H0/Hz)**2

def growth_factor_integrand(z, H_func, **kwargs):
    """Integrand for the growth factor D(z) using the Heath (1977) integral."""
    Hz = H_func(z, **kwargs)
    return (1 + z) / (Hz/H0)**3

def growth_factor(z, H_func, **kwargs):
    """Linear growth factor D(z), normalized to D(0) = 1.
    Uses Heath (1977): D(z) proportional to H(z) * integral_z^inf dz'*(1+z')/(H(z')/H0)^3
    """
    # Compute the integral from z to a large redshift
    z_max = 1000.0
    result_z, _ = quad(growth_factor_integrand, z, z_max, args=(H_func,), **kwargs)
    result_0, _ = quad(growth_factor_integrand, 0, z_max, args=(H_func,), **kwargs)

    Hz = H_func(z, **kwargs)
    H0_val = H_func(0, **kwargs)

    D_z = (Hz / H0) * result_z
    D_0 = (H0_val / H0) * result_0

    return D_z / D_0

# ==============================================================================
#  Precompute growth factors for all three models
# ==============================================================================

print("=" * 72)
print("S68 ISW TRACKING SIGNATURE TEST")
print("Gate: ISW-TRACKING-68 (INFO)")
print("=" * 72)

# Redshift grid (focus on z < 3 where ISW effect is significant)
z_arr = np.linspace(0.001, 3.0, 500)

print("\nComputing growth factors...")

# Growth factor for LCDM
D_LCDM = np.zeros_like(z_arr)
for i, z in enumerate(z_arr):
    z_max_int = 1000.0  # (local)
    res_z, _ = quad(lambda zp: (1+zp) / (H_LCDM(zp)/H0)**3, z, z_max_int)
    res_0, _ = quad(lambda zp: (1+zp) / (H_LCDM(zp)/H0)**3, 0, z_max_int)
    D_LCDM[i] = (H_LCDM(z)/H0 * res_z) / (H_LCDM(0)/H0 * res_0)

# Growth factor for wCDM (w0=-0.918, wa=0)
D_wCDM = np.zeros_like(z_arr)
for i, z in enumerate(z_arr):
    res_z, _ = quad(lambda zp: (1+zp) / (H_wCDM(zp, w0_FW)/H0)**3, z, 1000.0)
    res_0, _ = quad(lambda zp: (1+zp) / (H_wCDM(zp, w0_FW)/H0)**3, 0, 1000.0)
    D_wCDM[i] = (H_wCDM(z, w0_FW)/H0 * res_z) / (H_wCDM(0, w0_FW)/H0 * res_0)

print("  Growth factors computed for LCDM and wCDM.")

# ==============================================================================
#  Growth rate f(z) = dln(D)/dln(a) and Phi evolution
# ==============================================================================

# Interpolate growth factors
D_LCDM_interp = interp1d(z_arr, D_LCDM, kind='cubic', fill_value='extrapolate')
D_wCDM_interp = interp1d(z_arr, D_wCDM, kind='cubic', fill_value='extrapolate')

# Numerical derivative: f(z) = -dln(D)/dln(1+z) = -(1+z)/D * dD/dz
dz = z_arr[1] - z_arr[0]
f_LCDM = -(1 + z_arr) / D_LCDM * np.gradient(D_LCDM, dz)
f_wCDM = -(1 + z_arr) / D_wCDM * np.gradient(D_wCDM, dz)

print("  Growth rates f(z) computed.")

# ==============================================================================
#  ISW kernel W_ISW(z)
# ==============================================================================

def isw_kernel_lcdm(z):
    """ISW kernel for LCDM: W_ISW = 3 * Omega_m * H0^2 / (c^2 * k^2) * d(D*a)/dt * (decay factor)

    In LCDM, Phi proportional to D(z)/(1+z).
    dPhi/dt = H * (f - 1) * Phi

    ISW kernel (in angular power spectrum formulation using Limber):
    W_ISW(chi) = -2 * T_CMB * dPhi/dt / c^2

    We compute the POTENTIAL DECAY RATE: g(z) = D(z) * (1+z)^{-1} (Phi proportional to g)
    dg/dz = D'/(1+z) - D/(1+z)^2
    dg/dt = dg/dz * dz/dt = -dg/dz * (1+z) * H(z)
    """
    pass  # We'll use the direct approach below

# The ISW effect arises from the time derivative of the gravitational potential Phi.
# In the Poisson equation (sub-horizon):
#   k^2 Phi = -4*pi*G * a^2 * sum_i(rho_i * delta_i)
#
# For LCDM: only matter perturbations contribute (delta_DE = 0)
#   k^2 Phi = -4*pi*G * a^2 * rho_m * delta_m
#   Phi proportional to D(z) / (1+z) [since rho_m * a^2 = rho_m0 / (1+z)]
#
# For tracking DE (c_s^2 = 0): DE perturbations track matter
#   delta_DE = [(1+w)/(1-3w)] * delta_m   (sub-horizon, adiabatic)
#   k^2 Phi = -4*pi*G * a^2 * [rho_m + rho_DE * (1+w)/(1-3w)] * delta_m
#
# For smooth DE (c_s^2 = 1): DE perturbations are negligible on sub-horizon scales
#   k^2 Phi = -4*pi*G * a^2 * rho_m * delta_m  (same as LCDM structure but different D(z))

# Define the effective potential Phi(z) for each model.
# Phi is proportional to [effective source] * D(z) / k^2
# For the ISW effect, what matters is dPhi/dt, i.e. the time derivative.

# Phi(z) = -3/2 * (H0/c)^2 * Omega_m * D(z) / (1+z) * F(z)
# where F(z) encodes the DE clustering enhancement:
#   F = 1 for LCDM (no DE perturbations)
#   F = 1 for smooth wCDM (c_s^2 = 1, sub-horizon)
#   F = 1 + [rho_DE/rho_m * (1+w)/(1-3w)] for tracking DE (c_s^2 = 0)

def F_tracking(z, w0):
    """Enhancement factor from tracking DE perturbations (c_s^2 = 0).
    delta_DE = (1+w)/(1-3w) * delta_m
    F = 1 + (rho_DE/rho_m) * (1+w)/(1-3w)
    """
    Omega_DE_z = Omega_DE_of_z(z, w0)
    Omega_m_z = Omega_m * (1+z)**3 * (H0 / H_wCDM(z, w0))**2

    w = w0  # For constant w (w_a = 0)

    # Avoid division by zero when 1 - 3w = 0 (w = 1/3)
    if abs(1 - 3*w) < 1e-10:
        return 1.0

    ratio = (1 + w) / (1 - 3*w)
    return 1 + (Omega_DE_z / Omega_m_z) * ratio

# Vectorize F_tracking
F_tracking_arr = np.array([F_tracking(z, w0_FW) for z in z_arr])

print("\n--- Enhancement factor F(z) from tracking DE perturbations ---")
print(f"  F(z=0.0) = {F_tracking(0.001, w0_FW):.4f}")
print(f"  F(z=0.5) = {F_tracking(0.5, w0_FW):.4f}")
print(f"  F(z=1.0) = {F_tracking(1.0, w0_FW):.4f}")
print(f"  F(z=2.0) = {F_tracking(2.0, w0_FW):.4f}")

# ==============================================================================
#  Compute dPhi/dz for each model (Phi proportional to relevant D(z) * stuff)
# ==============================================================================

# Model A: LCDM
# Phi_A ~ D_LCDM(z) / (1+z)
Phi_A = D_LCDM / (1 + z_arr)
dPhidz_A = np.gradient(Phi_A, dz)

# Model B: Framework (w0=-0.918, c_s^2=0, tracking DE)
# Phi_B ~ D_wCDM(z) * F_tracking(z) / (1+z)
# Note: D_wCDM already reflects modified expansion history.
# The tracking factor F modifies the Poisson equation source.
Phi_B = D_wCDM * F_tracking_arr / (1 + z_arr)
dPhidz_B = np.gradient(Phi_B, dz)

# Model C: Quintessence (w0=-0.918, c_s^2=1, smooth DE)
# Phi_C ~ D_wCDM(z) / (1+z)  (same growth as B but F=1)
Phi_C = D_wCDM / (1 + z_arr)
dPhidz_C = np.gradient(Phi_C, dz)

# Convert to dPhi/dt = dPhi/dz * dz/dt = -(1+z) * H(z) * dPhi/dz
# The ISW kernel is proportional to dPhi/dt

H_LCDM_arr = np.array([H_LCDM(z) for z in z_arr])
H_wCDM_arr = np.array([H_wCDM(z, w0_FW) for z in z_arr])

dPhidt_A = -(1 + z_arr) * H_LCDM_arr * dPhidz_A  # LCDM
dPhidt_B = -(1 + z_arr) * H_wCDM_arr * dPhidz_B  # Framework (tracking)
dPhidt_C = -(1 + z_arr) * H_wCDM_arr * dPhidz_C  # Quintessence (smooth)

# Normalize: Phi_0 at z=0 is the same for all models (set by sigma_8)
# We care about RATIOS, so normalization cancels in C_l^Tg ratios

print("\n--- dPhi/dt at key redshifts (arbitrary units, relative) ---")
for z_test in [0.3, 0.5, 0.8, 1.0, 1.5]:
    idx = np.argmin(np.abs(z_arr - z_test))
    print(f"  z={z_test:.1f}: LCDM={dPhidt_A[idx]:.6f}, "
          f"FW(track)={dPhidt_B[idx]:.6f}, "
          f"Quint(smooth)={dPhidt_C[idx]:.6f}")

# ==============================================================================
#  Galaxy window function W_g(z)
# ==============================================================================

def galaxy_window(z, z_mean=0.7, sigma_z=0.3):
    """Gaussian galaxy redshift distribution centered at z_mean.
    This represents a typical photometric survey distribution.
    Normalized to integrate to 1.
    """
    return np.exp(-0.5 * ((z - z_mean) / sigma_z)**2) / (sigma_z * np.sqrt(2 * np.pi))

# Also define the galaxy bias (simplistic constant bias)
b_g = 1.5  # Typical galaxy bias for NVSS/WISE-like surveys  # (local)

# ==============================================================================
#  Compute C_l^{Tg} using Limber approximation
# ==============================================================================

# C_l^{Tg} = integral dz/chi^2 * W_ISW(z) * W_g(z) * P(k=l/chi, z)
#
# W_ISW is proportional to dPhi/dt / H(z)  [the ISW integrand per unit chi]
# The galaxy window W_g(z) = b_g * dn/dz * delta_m(z)
#
# In the Limber approximation:
# C_l^{Tg} = integral_0^inf dchi * W_ISW(chi) * W_g(chi) / chi^2 * P_mm(k=l/chi)
#           = integral dz * (H(z)/c) * W_ISW(z) * W_g(z) * P_mm(k=l/chi(z), z) / chi(z)^2
#
# We compute the RATIO C_l^{Tg}(model) / C_l^{Tg}(LCDM), where the matter power
# spectrum and galaxy window cancel to first order (they're the same for all models
# on sub-horizon scales). The key difference is in the ISW kernel.

print("\nComputing comoving distances...")

# Precompute comoving distances
chi_LCDM = np.zeros_like(z_arr)
chi_wCDM = np.zeros_like(z_arr)
for i, z in enumerate(z_arr):
    chi_LCDM[i], _ = quad(lambda zp: c / H_LCDM(zp), 0, z)
    chi_wCDM[i], _ = quad(lambda zp: c / H_wCDM(zp, w0_FW), 0, z)

print("  Done.")

# Linear matter power spectrum (Eisenstein-Hu fitting formula, no wiggles)
# P(k, z) = A_s * (k/k_pivot)^(n_s - 1) * T^2(k) * D^2(z) * (2*pi^2 / k^3) * (k/H0*c)^4
# For RATIOS between models, we only need D(z) differences.
# The transfer function T(k) and A_s cancel in the ratio.

# Simplified: P(k,z) proportional to D^2(z) * k^(n_s) * T^2(k)
# In the ratio, T(k) and k-dependent parts cancel if we integrate over the same k.

# For the ISW-galaxy cross-correlation RATIO, the key quantity is:
# R(l) = integral dz * [dPhi/dt]_model * W_g(z) * D(z)_model / (H_model * chi_model^2)
#       / integral dz * [dPhi/dt]_LCDM * W_g(z) * D(z)_LCDM / (H_LCDM * chi_LCDM^2)

# This is because C_l^Tg ~ integral dz * dPhi/dt * b_g * dn/dz * D(z) * P_lin(k=l/chi) / chi^2
# and in the Limber approx, the z-integral evaluates the power spectrum at k=l/chi.

# For the ABSOLUTE signal we need the full power spectrum. For RATIOS, the form simplifies.

# ==============================================================================
#  ISW-galaxy cross-power spectrum integrands
# ==============================================================================

# The Limber-approximated C_l^{Tg} for multipole l:
#   C_l^{Tg} = integral dz/c * H(z)/chi(z)^2 * K_ISW(z) * K_g(z) * P_mm(l/chi(z), z)
# where K_ISW(z) proportional to dPhi/dt / H^2  and K_g(z) = b_g * dn/dz
#
# For the RATIO between models at fixed l, P_mm(k,z) cancels if we assume
# the matter power spectrum shape is the same (reasonable for small w differences).
# What differs: dPhi/dt, H(z), chi(z), and D(z) in P_mm.

# More precisely, P_mm(k,z) = P_mm(k,0) * [D(z)]^2, so:
# C_l^{Tg} proportional to integral dz * [dPhi/dt(z)] * W_g(z) * [D(z)]^2 * H(z) / chi(z)^2

# But dPhi/dt already contains D(z) (through Phi ~ D/(1+z) * F), so the integrand is:
# I(z) = dPhi/dt(z) * W_g(z) * D(z) * H(z) / chi(z)^2
# (one factor of D from P_mm, the other is inside dPhi/dt)

# Let's compute this integrand for all three models:

W_g_arr = galaxy_window(z_arr, z_mean=0.7, sigma_z=0.3) * b_g

# Model A: LCDM
I_A = dPhidt_A * W_g_arr * D_LCDM * H_LCDM_arr / (chi_LCDM**2 + 1e-30)

# Model B: Framework (tracking, c_s^2=0)
I_B = dPhidt_B * W_g_arr * D_wCDM * H_wCDM_arr / (chi_wCDM**2 + 1e-30)

# Model C: Quintessence (smooth, c_s^2=1)
I_C = dPhidt_C * W_g_arr * D_wCDM * H_wCDM_arr / (chi_wCDM**2 + 1e-30)

# Integrate
C_Tg_A = simpson(y=I_A, x=z_arr)
C_Tg_B = simpson(y=I_B, x=z_arr)
C_Tg_C = simpson(y=I_C, x=z_arr)

# ==============================================================================
#  Now compute l-dependent C_l^{Tg} properly
# ==============================================================================

# For the l-dependence, we need to account for the fact that at each l,
# the Limber approximation evaluates k = (l + 0.5) / chi(z).
# The matter power spectrum P(k) introduces scale dependence.
# We use the Eisenstein-Hu no-wiggle transfer function.

n_s_planck = 0.9649  # Planck 2018

def transfer_EH(k_hMpc):
    """Eisenstein-Hu no-wiggle transfer function.
    k in h/Mpc. Returns T(k).
    Fitting formula from Eisenstein & Hu 1998, Eq. 29.
    """
    h = H_0_km_s_Mpc / 100.0
    Omega_m_h2 = Omega_m * h**2
    Omega_b_h2 = Omega_b * h**2
    f_b = Omega_b / Omega_m

    # Sound horizon
    s = 44.5 * np.log(9.83 / Omega_m_h2) / np.sqrt(1 + 10 * Omega_b_h2**0.75)

    # Gamma_eff
    alpha_Gamma = 1 - 0.328 * np.log(431 * Omega_m_h2) * f_b + 0.38 * np.log(22.3 * Omega_m_h2) * f_b**2
    Gamma_eff = Omega_m * h * (alpha_Gamma + (1 - alpha_Gamma) / (1 + (0.43 * k_hMpc * s)**4))

    q = k_hMpc / (13.41 * Gamma_eff / h)  # Note: this has h factors
    # Correct: q = k * Theta^2 / Gamma where Theta = T_CMB/2.7
    q = k_hMpc * (T_CMB / 2.7)**2 / Gamma_eff

    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1 + 62.5 * q)
    T = L / (L + C * q**2)
    return T

def P_mm(k_hMpc, z, D_z):
    """Linear matter power spectrum P(k,z) in (Mpc/h)^3.
    Normalized to sigma_8 at z=0.
    """
    T = transfer_EH(k_hMpc)
    # P(k) proportional to k^ns * T^2(k) * D^2(z)
    # We normalize using sigma_8 later. For ratios, normalization cancels.
    return k_hMpc**n_s_planck * T**2 * D_z**2

# Compute sigma_8 normalization factor
# sigma_8^2 = 1/(2*pi^2) * integral dk * k^2 * P(k,0) * W_TH^2(k*8)
# where W_TH(x) = 3*(sin(x) - x*cos(x))/x^3
def W_tophat(x):
    """Top-hat window function in Fourier space."""
    x = np.asarray(x)
    result = np.ones_like(x)
    mask = np.abs(x) > 1e-6
    result[mask] = 3 * (np.sin(x[mask]) - x[mask] * np.cos(x[mask])) / x[mask]**3
    return result

# We don't need absolute normalization for RATIOS, but let's compute it for chi^2
# against absolute Planck ISW amplitude

print("\n--- Computing l-dependent C_l^{Tg} ---")

l_arr = np.arange(2, 101)  # Multipoles l = 2 to 100
h = H_0_km_s_Mpc / 100.0

# For each l, integrate the full Limber expression:
# C_l = integral dz * (H(z)/c) / chi(z)^2 * K_ISW(z) * K_g(z) * P_mm(k=(l+0.5)/chi, z)

Cl_A = np.zeros(len(l_arr))
Cl_B = np.zeros(len(l_arr))
Cl_C = np.zeros(len(l_arr))

for il, l in enumerate(l_arr):
    for model_idx, (dPhidt, H_arr, chi_arr, D_arr) in enumerate([
        (dPhidt_A, H_LCDM_arr, chi_LCDM, D_LCDM),
        (dPhidt_B, H_wCDM_arr, chi_wCDM, D_wCDM),
        (dPhidt_C, H_wCDM_arr, chi_wCDM, D_wCDM)
    ]):
        # k = (l + 0.5) / chi in Mpc^{-1}, convert to h/Mpc
        k_arr = (l + 0.5) / (chi_arr + 1e-30) * (1.0/h)  # h/Mpc

        # Matter power spectrum at each z
        P_arr = np.array([P_mm(k, z, D) for k, z, D in zip(k_arr, z_arr, D_arr)])

        # Integrand: dPhi/dt * W_g * P(k,z) * H/c / chi^2
        integrand = dPhidt * W_g_arr * P_arr * H_arr / (c * chi_arr**2 + 1e-30)

        Cl = simpson(y=integrand, x=z_arr)
        if model_idx == 0:
            Cl_A[il] = Cl
        elif model_idx == 1:
            Cl_B[il] = Cl
        else:
            Cl_C[il] = Cl

print("  Done.")

# ==============================================================================
#  Compute ratios and discriminants
# ==============================================================================

# Ratio: Framework / LCDM
ratio_BA = Cl_B / (Cl_A + 1e-50)  # Framework (tracking) / LCDM
ratio_CA = Cl_C / (Cl_A + 1e-50)  # Quintessence (smooth) / LCDM
ratio_BC = Cl_B / (Cl_C + 1e-50)  # Framework / Quintessence

print("\n" + "=" * 72)
print("RESULTS: ISW-Galaxy Cross-Correlation Ratios")
print("=" * 72)

# Average ratios over l = 2-30 (ISW-sensitive range)
mask_isw = l_arr <= 30
mean_ratio_BA = np.mean(ratio_BA[mask_isw])
mean_ratio_CA = np.mean(ratio_CA[mask_isw])
mean_ratio_BC = np.mean(ratio_BC[mask_isw])

print(f"\n  l = 2-30 (ISW-sensitive multipoles):")
print(f"    C_l^Tg(Framework) / C_l^Tg(LCDM) = {mean_ratio_BA:.4f}")
print(f"    C_l^Tg(Quintessence) / C_l^Tg(LCDM) = {mean_ratio_CA:.4f}")
print(f"    C_l^Tg(Framework) / C_l^Tg(Quintessence) = {mean_ratio_BC:.4f}")
print(f"    Delta(Framework-LCDM)/LCDM = {(mean_ratio_BA - 1)*100:.2f}%")
print(f"    Delta(Quint-LCDM)/LCDM = {(mean_ratio_CA - 1)*100:.2f}%")
print(f"    Delta(Framework-Quint)/Quint = {(mean_ratio_BC - 1)*100:.2f}%")

# Average over l = 2-100
mask_all = l_arr <= 100
mean_ratio_BA_all = np.mean(ratio_BA[mask_all])
mean_ratio_CA_all = np.mean(ratio_CA[mask_all])
mean_ratio_BC_all = np.mean(ratio_BC[mask_all])

print(f"\n  l = 2-100 (extended range):")
print(f"    C_l^Tg(Framework) / C_l^Tg(LCDM) = {mean_ratio_BA_all:.4f}")
print(f"    C_l^Tg(Quintessence) / C_l^Tg(LCDM) = {mean_ratio_CA_all:.4f}")
print(f"    C_l^Tg(Framework) / C_l^Tg(Quintessence) = {mean_ratio_BC_all:.4f}")

# ==============================================================================
#  Chi-squared against Planck ISW amplitude
# ==============================================================================

# Planck measures A_ISW = C_l^Tg(data) / C_l^Tg(LCDM theory) = 1.00 +/- 0.25
# For each model, the predicted amplitude relative to LCDM is the ratio we computed.
# chi^2 = (A_model - A_obs)^2 / sigma^2

A_model_LCDM = 1.0  # By definition  # (local)
A_model_FW = mean_ratio_BA  # Framework/LCDM
A_model_quint = mean_ratio_CA  # Quintessence/LCDM

chi2_LCDM = (A_model_LCDM - A_ISW_planck)**2 / sigma_A_ISW**2
chi2_FW = (A_model_FW - A_ISW_planck)**2 / sigma_A_ISW**2
chi2_quint = (A_model_quint - A_ISW_planck)**2 / sigma_A_ISW**2

print(f"\n" + "=" * 72)
print("CHI-SQUARED AGAINST PLANCK ISW AMPLITUDE")
print(f"  Planck: A_ISW = {A_ISW_planck:.2f} +/- {sigma_A_ISW:.2f}")
print("=" * 72)

print(f"\n  Model A (LCDM):        A = {A_model_LCDM:.4f},  chi^2 = {chi2_LCDM:.4f},  sigma = {np.sqrt(chi2_LCDM):.2f}")
print(f"  Model B (Framework):   A = {A_model_FW:.4f},  chi^2 = {chi2_FW:.4f},  sigma = {np.sqrt(chi2_FW):.2f}")
print(f"  Model C (Quintessence):A = {A_model_quint:.4f},  chi^2 = {chi2_quint:.4f},  sigma = {np.sqrt(chi2_quint):.2f}")

# ==============================================================================
#  Signal-to-noise for discriminating Framework from LCDM and Quintessence
# ==============================================================================

# With Planck (sigma = 0.25):
SNR_FW_vs_LCDM_planck = abs(A_model_FW - A_model_LCDM) / sigma_A_ISW
SNR_FW_vs_quint_planck = abs(A_model_FW - A_model_quint) / sigma_A_ISW

# With Euclid (projected sigma ~ 0.05 for tomographic ISW-galaxy cross-correlation)
sigma_euclid = 0.05  # (local)
SNR_FW_vs_LCDM_euclid = abs(A_model_FW - A_model_LCDM) / sigma_euclid
SNR_FW_vs_quint_euclid = abs(A_model_FW - A_model_quint) / sigma_euclid

# With future 21cm (projected sigma ~ 0.01)
sigma_21cm = 0.01  # (local)
SNR_FW_vs_LCDM_21cm = abs(A_model_FW - A_model_LCDM) / sigma_21cm
SNR_FW_vs_quint_21cm = abs(A_model_FW - A_model_quint) / sigma_21cm

print(f"\n" + "=" * 72)
print("SIGNAL-TO-NOISE FOR MODEL DISCRIMINATION")
print("=" * 72)

print(f"\n  Framework vs LCDM:")
print(f"    |Delta A| = {abs(A_model_FW - A_model_LCDM):.4f}")
print(f"    Planck (sigma=0.25):  SNR = {SNR_FW_vs_LCDM_planck:.2f}")
print(f"    Euclid (sigma=0.05):  SNR = {SNR_FW_vs_LCDM_euclid:.2f}")
print(f"    21cm   (sigma=0.01):  SNR = {SNR_FW_vs_LCDM_21cm:.2f}")

print(f"\n  Framework vs Quintessence (same w, different c_s^2):")
print(f"    |Delta A| = {abs(A_model_FW - A_model_quint):.4f}")
print(f"    Planck (sigma=0.25):  SNR = {SNR_FW_vs_quint_planck:.2f}")
print(f"    Euclid (sigma=0.05):  SNR = {SNR_FW_vs_quint_euclid:.2f}")
print(f"    21cm   (sigma=0.01):  SNR = {SNR_FW_vs_quint_21cm:.2f}")

# ==============================================================================
#  Cumulative S/N from multipole-by-multipole measurement
# ==============================================================================

# For Planck, the per-multipole uncertainty on C_l^Tg is dominated by
# cosmic variance of the temperature field (since ISW is subdominant to primary CMB).
# sigma(C_l^Tg) ~ C_l^TT / sqrt((2l+1) * f_sky * C_l^gg)
#
# A rough estimate: at l < 30, the ISW signal is ~10-20% of total C_l^TT.
# The S/N per multipole is ~0.5-0.8, giving cumulative S/N ~ sqrt(29) * 0.6 ~ 3.2
# (consistent with the Planck ~4sigma detection combining all tracers).
#
# For model discrimination, we need the fractional difference to exceed
# the per-multipole noise.

# Compute cumulative S/N using Fisher formalism
# F = sum_l (2l+1)/2 * f_sky * [dC_l/dp]^2 / Var(C_l)
# For the ISW amplitude A: dC_l/dA = C_l^Tg_LCDM, Var(C_l^Tg) ~ C_l^TT * C_l^gg / (2l+1)

f_sky = 0.70  # Planck usable sky fraction (local)

# Approximate C_l^TT / C_l^Tg ratio (ISW is ~10% of primary at l < 30)
# This means sigma(A) ~ 1/(S/N per l) ~ 10 at l=10, cumulative ~ 10/sqrt(29) ~ 1.9
# Planck achieves sigma(A) ~ 0.25 with optimal combination of tracers

# The model discrimination S/N is:
# SNR_cumul^2 = sum_{l=2}^{l_max} (2l+1)*f_sky * [C_l^Tg(B) - C_l^Tg(A)]^2 / (sigma_l)^2
# where sigma_l^2 = C_l^TT * C_l^gg / (2l+1) (approximately)

# We estimate sigma_l from the overall Planck ISW amplitude uncertainty:
# sigma(A)^2 = 1 / sum_l (2l+1)*f_sky / sigma_l^2 * [C_l^Tg(LCDM)]^2
# => sigma_l^2 ~ (2l+1)*f_sky * [C_l^Tg(LCDM)]^2 / sigma(A)^{-2}

# For a simpler estimate: the fractional uncertainty per multipole is
# sigma_frac(l) ~ sigma(A) * sqrt(N_modes) / sqrt(N_eff_per_l)
# With 29 ISW-sensitive modes and sigma(A)=0.25, the "effective" per-mode
# noise is sigma(A)*sqrt(29) ~ 1.35

# The cumulative difference:
delta_Cl_BA = Cl_B - Cl_A  # Framework - LCDM
delta_Cl_BC = Cl_B - Cl_C  # Framework - Quintessence

# Fractional difference per multipole
frac_diff_BA = delta_Cl_BA / (np.abs(Cl_A) + 1e-50)
frac_diff_BC = delta_Cl_BC / (np.abs(Cl_C) + 1e-50)

print(f"\n" + "=" * 72)
print("PER-MULTIPOLE FRACTIONAL DIFFERENCES (l = 2-30)")
print("=" * 72)

for l_show in [2, 5, 10, 15, 20, 25, 30]:
    idx = l_show - 2  # l_arr starts at 2
    if idx < len(l_arr):
        print(f"  l = {l_show:3d}: "
              f"FW/LCDM = {ratio_BA[idx]:.4f} ({frac_diff_BA[idx]*100:+.2f}%), "
              f"FW/Quint = {ratio_BC[idx]:.4f} ({frac_diff_BC[idx]*100:+.2f}%)")

# ==============================================================================
#  Redshift-dependent ISW signal comparison
# ==============================================================================

# The ISW effect peaks at z ~ 0.3-1.0 (transition from matter to DE domination)
# For different redshift bins (Euclid-like tomography):

print(f"\n" + "=" * 72)
print("REDSHIFT-DEPENDENT ISW SIGNAL (Euclid tomographic bins)")
print("=" * 72)

z_bins = [(0.2, 0.5), (0.5, 0.8), (0.8, 1.1), (1.1, 1.5), (1.5, 2.0)]

for z_lo, z_hi in z_bins:
    mask_bin = (z_arr >= z_lo) & (z_arr <= z_hi)
    if np.sum(mask_bin) < 5:
        continue

    z_bin = z_arr[mask_bin]

    # ISW signal in this bin (integrate dPhi/dt)
    sig_A = simpson(y=dPhidt_A[mask_bin], x=z_bin)
    sig_B = simpson(y=dPhidt_B[mask_bin], x=z_bin)
    sig_C = simpson(y=dPhidt_C[mask_bin], x=z_bin)

    ratio_bin_BA = sig_B / (sig_A + 1e-50)
    ratio_bin_BC = sig_B / (sig_C + 1e-50)

    print(f"  z = [{z_lo:.1f}, {z_hi:.1f}]: "
          f"FW/LCDM = {ratio_bin_BA:.4f} ({(ratio_bin_BA-1)*100:+.2f}%), "
          f"FW/Quint = {ratio_bin_BC:.4f} ({(ratio_bin_BC-1)*100:+.2f}%)")

# ==============================================================================
#  Comparison with workshop estimate
# ==============================================================================

print(f"\n" + "=" * 72)
print("COMPARISON WITH WORKSHOP ESTIMATE")
print("=" * 72)

# Workshop (S68 Volovik-Mack R2) estimated:
# Delta C_l^ISW / C_l^ISW ~ 2 * (1+w0) * f_DE(z) / (1 - f_DE(z)) ~ 20% at z~0.5
# Our computation gives a more careful integration

workshop_estimate = 0.20  # 20%  # (local)
computed_FW_vs_LCDM = abs(mean_ratio_BA - 1.0)
computed_FW_vs_quint = abs(mean_ratio_BC - 1.0)

print(f"  Workshop order-of-magnitude estimate (FW vs LCDM): {workshop_estimate*100:.1f}%")
print(f"  Computed Delta(FW-LCDM)/LCDM (l=2-30):            {computed_FW_vs_LCDM*100:.2f}%")
print(f"  Computed Delta(FW-Quint)/Quint (l=2-30):           {computed_FW_vs_quint*100:.2f}%")

# The discriminant is the c_s^2 = 0 vs c_s^2 = 1 difference:
print(f"\n  KEY DISCRIMINANT (tracking vs smooth, same w_0):")
print(f"    This is the substrate-specific signature.")
print(f"    FW (c_s^2=0) vs Quint (c_s^2=1): {computed_FW_vs_quint*100:.2f}%")

# ==============================================================================
#  Gate Verdict
# ==============================================================================

print(f"\n" + "=" * 72)
print("GATE VERDICT: ISW-TRACKING-68")
print("=" * 72)

# Pre-registration:
# PASS if Delta > 5% at l < 30 (above Euclid threshold)
# FAIL if Delta < 1% (below cosmic variance floor)
# INFO otherwise

delta_pct = computed_FW_vs_quint * 100

if delta_pct > 5.0:
    verdict = "PASS"
    verdict_msg = (f"Delta(FW-Quint)/Quint = {delta_pct:.2f}% > 5% threshold. "
                   f"ISW tracking signature EXCEEDS Euclid sensitivity threshold.")
elif delta_pct < 1.0:
    verdict = "FAIL"
    verdict_msg = (f"Delta(FW-Quint)/Quint = {delta_pct:.2f}% < 1% threshold. "
                   f"ISW tracking signature BELOW cosmic variance floor.")
else:
    verdict = "INFO"
    verdict_msg = (f"Delta(FW-Quint)/Quint = {delta_pct:.2f}% (between 1% and 5%). "
                   f"ISW tracking signature detectable but marginal.")

print(f"  Pre-registered threshold: PASS > 5%, FAIL < 1%, INFO otherwise")
print(f"  Computed: Delta(c_s^2=0 vs c_s^2=1) at l=2-30 = {delta_pct:.2f}%")
print(f"  Verdict: {verdict}")
print(f"  {verdict_msg}")
print(f"\n  FW vs LCDM (expansion + clustering): {computed_FW_vs_LCDM*100:.2f}%")
print(f"  FW vs Quint (clustering only, same w): {computed_FW_vs_quint*100:.2f}%")
print(f"\n  Planck constraint: all models consistent (sigma_A = 0.25)")
print(f"  Euclid forecast: FW vs LCDM at {SNR_FW_vs_LCDM_euclid:.1f}-sigma, "
      f"FW vs Quint at {SNR_FW_vs_quint_euclid:.1f}-sigma")

# ==============================================================================
#  Save results
# ==============================================================================

save_path = r"C:\sandbox\Ainulindale Exflation\computations\s68_isw_tracking_test.npz"

np.savez(save_path,
    # Redshift grid
    z_arr=z_arr,
    # Growth factors
    D_LCDM=D_LCDM, D_wCDM=D_wCDM,
    # Enhancement factor
    F_tracking=F_tracking_arr,
    # Potential time derivatives
    dPhidt_A=dPhidt_A, dPhidt_B=dPhidt_B, dPhidt_C=dPhidt_C,
    # Power spectra
    l_arr=l_arr,
    Cl_A=Cl_A, Cl_B=Cl_B, Cl_C=Cl_C,
    # Ratios
    ratio_BA=ratio_BA, ratio_CA=ratio_CA, ratio_BC=ratio_BC,
    # Chi-squared
    chi2_LCDM=chi2_LCDM, chi2_FW=chi2_FW, chi2_quint=chi2_quint,
    # Model parameters
    w0_FW=w0_FW, wa_FW=wa_FW,
    A_ISW_planck=A_ISW_planck, sigma_A_ISW=sigma_A_ISW,
    # SNR
    SNR_FW_vs_LCDM_planck=SNR_FW_vs_LCDM_planck,
    SNR_FW_vs_quint_planck=SNR_FW_vs_quint_planck,
    SNR_FW_vs_LCDM_euclid=SNR_FW_vs_LCDM_euclid,
    SNR_FW_vs_quint_euclid=SNR_FW_vs_quint_euclid,
    # Mean ratios
    mean_ratio_BA=mean_ratio_BA, mean_ratio_CA=mean_ratio_CA,
    mean_ratio_BC=mean_ratio_BC
)

print(f"\n  Results saved to: {save_path}")

# ==============================================================================
#  Plot
# ==============================================================================

plot_path = r"C:\sandbox\Ainulindale Exflation\computations\s68_isw_tracking_test.png"

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S68 ISW Tracking Signature Test (ISW-TRACKING-68)', fontsize=14, fontweight='bold')

# Panel 1: C_l^Tg ratios vs l
ax1 = axes[0, 0]
ax1.plot(l_arr, ratio_BA, 'b-', linewidth=2, label=f'Framework/LCDM (w={w0_FW}, $c_s^2$=0)')
ax1.plot(l_arr, ratio_CA, 'r--', linewidth=2, label=f'Quintessence/LCDM (w={w0_FW}, $c_s^2$=1)')
ax1.axhline(y=1.0, color='k', linestyle=':', alpha=0.5, label='LCDM')
ax1.axvspan(2, 30, alpha=0.1, color='green', label='ISW-sensitive (l<30)')
ax1.fill_between(l_arr, 1 - sigma_A_ISW, 1 + sigma_A_ISW, alpha=0.15, color='gray',
                  label=f'Planck ISW 1-sigma (A={A_ISW_planck}$\\pm${sigma_A_ISW})')
ax1.set_xlabel('Multipole l')
ax1.set_ylabel('$C_l^{Tg}$ / $C_l^{Tg}$(LCDM)')
ax1.set_title('ISW-Galaxy Cross-Correlation Ratio')
ax1.legend(fontsize=8, loc='upper right')
ax1.set_xlim(2, 100)
ax1.grid(True, alpha=0.3)

# Panel 2: Framework/Quintessence ratio (c_s^2 = 0 vs 1 discriminant)
ax2 = axes[0, 1]
ax2.plot(l_arr, ratio_BC, 'g-', linewidth=2.5, label='Framework/Quintessence ($c_s^2$=0 vs 1)')
ax2.axhline(y=1.0, color='k', linestyle=':', alpha=0.5)
ax2.axvspan(2, 30, alpha=0.1, color='green')
ax2.fill_between(l_arr, 1 - sigma_euclid, 1 + sigma_euclid, alpha=0.15, color='orange',
                  label=f'Euclid 1-sigma ($\\sigma$={sigma_euclid})')
ax2.set_xlabel('Multipole l')
ax2.set_ylabel('$C_l^{Tg}$(FW) / $C_l^{Tg}$(Quint)')
ax2.set_title('Substrate Discriminant: $c_{s,DE}^2$=0 vs $c_{s,DE}^2$=1')
ax2.legend(fontsize=9)
ax2.set_xlim(2, 100)
ax2.grid(True, alpha=0.3)

# Panel 3: dPhi/dt(z) for all three models
ax3 = axes[1, 0]
# Normalize to peak of LCDM
norm = np.max(np.abs(dPhidt_A))
ax3.plot(z_arr, dPhidt_A / norm, 'k-', linewidth=2, label='LCDM (w=-1)')
ax3.plot(z_arr, dPhidt_B / norm, 'b-', linewidth=2, label=f'Framework ($c_s^2$=0)')
ax3.plot(z_arr, dPhidt_C / norm, 'r--', linewidth=2, label=f'Quintessence ($c_s^2$=1)')
ax3.set_xlabel('Redshift z')
ax3.set_ylabel('$d\\Phi/dt$ (normalized)')
ax3.set_title('ISW Kernel: Potential Decay Rate')
ax3.legend(fontsize=9)
ax3.set_xlim(0, 2.5)
ax3.grid(True, alpha=0.3)

# Panel 4: Enhancement factor F(z) and Omega_DE(z)
ax4 = axes[1, 1]
Omega_DE_arr = np.array([Omega_DE_of_z(z, w0_FW) for z in z_arr])
Omega_m_z_arr = Omega_m * (1 + z_arr)**3 * (H0 / H_wCDM_arr)**2

ax4_twin = ax4.twinx()
ax4.plot(z_arr, F_tracking_arr, 'b-', linewidth=2.5, label='F(z) tracking enhancement')
ax4_twin.plot(z_arr, Omega_DE_arr, 'r--', linewidth=1.5, label='$\\Omega_{DE}(z)$', alpha=0.7)
ax4_twin.plot(z_arr, Omega_m_z_arr, 'g-.', linewidth=1.5, label='$\\Omega_m(z)$', alpha=0.7)

ax4.set_xlabel('Redshift z')
ax4.set_ylabel('F(z) = 1 + ($\\rho_{DE}/\\rho_m$)$\\cdot$(1+w)/(1-3w)', color='b')
ax4_twin.set_ylabel('$\\Omega(z)$', color='r')
ax4.set_title('Tracking Enhancement Factor')
ax4.set_xlim(0, 2.5)
ax4.grid(True, alpha=0.3)

# Add legend combining both axes
lines1, labels1 = ax4.get_legend_handles_labels()
lines2, labels2 = ax4_twin.get_legend_handles_labels()
ax4.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc='upper right')

plt.tight_layout(rect=[0, 0.02, 1, 0.96])

# Add text box with summary
fig.text(0.02, 0.005,
         f'Gate: ISW-TRACKING-68 | w_0={w0_FW}, w_a={wa_FW} | '
         f'FW/LCDM={mean_ratio_BA:.4f} | FW/Quint={mean_ratio_BC:.4f} | '
         f'Planck A_ISW=1.00+/-0.25 | '
         f'chi2: LCDM={chi2_LCDM:.3f}, FW={chi2_FW:.3f}, Quint={chi2_quint:.3f}',
         fontsize=7, style='italic', alpha=0.7)

plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {plot_path}")

print(f"\n{'=' * 72}")
print("COMPUTATION COMPLETE")
print(f"{'=' * 72}")
