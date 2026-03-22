#!/usr/bin/env python3
"""
SIGMA8-OZ-50: sigma_8 from the O-Z Rigid Prediction alpha_s = n_s^2 - 1.

Physics:
  The O-Z identity gives alpha_s = n_s^2 - 1 = -0.069 (rigid, structural).
  S50 W1 confirmed this survives all tested escape routes (3-pole propagator,
  running mass, Bogoliubov imprint, eikonal damping).

  A large negative running alpha_s = dn_s/d(ln k) SUPPRESSES small-scale power
  relative to the no-running case, because the effective spectral index becomes
  MORE RED at scales smaller than the pivot (k > k_pivot).

  This computation documents the precise sigma_8 this prediction gives.

Method:
  1. Primordial power spectrum with running:
     P_R(k) = A_s * (k/k_pivot)^{n_s - 1 + (1/2)*alpha_s*ln(k/k_pivot)}
  2. Transfer function: Eisenstein-Hu (1998) with baryons
  3. Matter power spectrum: P_m(k) = T^2(k) * P_R(k) * (k in h/Mpc)
  4. sigma_8 from integral with top-hat window at R = 8 h^{-1} Mpc

Gate: SIGMA8-OZ-50
  PASS: sigma_8 in [0.740, 0.820]
  FAIL: sigma_8 outside [0.640, 0.920]
  INFO: sigma_8 outside desired range but within 3-sigma of at least one dataset

Session: S50 W2-F
Author: gen-physicist
"""

import sys
import os
import time
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

t0 = time.time()

# --- Import canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    A_s_CMB, Omega_m, Omega_b, Omega_Lambda, H_0_km_s_Mpc,
    T_CMB, sigma_8 as sigma_8_planck, PI
)

# Load S49 Bayesian posterior for alpha_s
data_dir = os.path.dirname(os.path.abspath(__file__))
s49_data = np.load(os.path.join(data_dir, 's49_alpha_s_bayes.npz'), allow_pickle=True)
alpha_s_oz_median = float(s49_data['alpha_s_median'])
alpha_s_oz_mean = float(s49_data['alpha_s_mean'])
alpha_s_oz_std = float(s49_data['alpha_s_std'])
alpha_s_oz_ci95_lo = float(s49_data['ci_95_lo'])
alpha_s_oz_ci95_hi = float(s49_data['ci_95_hi'])
alpha_s_samples = s49_data['alpha_s_samples']  # 10000 MC samples

print("=" * 78)
print("SIGMA8-OZ-50: sigma_8 from O-Z Rigid Prediction alpha_s = n_s^2 - 1")
print("=" * 78)

# ===========================================================================
# PARAMETERS
# ===========================================================================

# Planck 2018 cosmological parameters
n_s = 0.9649        # Planck 2018
A_s = A_s_CMB       # 2.1e-9
h = H_0_km_s_Mpc / 100.0   # 0.674
omega_m = Omega_m * h**2    # physical matter density = 0.143
omega_b = Omega_b * h**2    # physical baryon density = 0.0224
omega_c = omega_m - omega_b # physical CDM density
Omega_c = omega_c / h**2
k_pivot = 0.05      # Mpc^{-1} (Planck pivot scale)
T_cmb = T_CMB        # 2.7255 K
R_8 = 8.0            # h^{-1} Mpc (top-hat radius for sigma_8)

# Three alpha_s cases
alpha_s_zero = 0.0
alpha_s_oz = n_s**2 - 1.0                  # = -0.06896... (analytic O-Z)
alpha_s_lattice = -0.038                     # S48 lattice value (superseded)

# Observational sigma_8 values
sigma_8_planck_val = 0.811
sigma_8_planck_err = 0.006
sigma_8_lensing_val = 0.766
sigma_8_lensing_err = 0.020

print(f"\n--- Cosmological Parameters ---")
print(f"  n_s       = {n_s}")
print(f"  A_s       = {A_s:.2e}")
print(f"  h         = {h}")
print(f"  Omega_m   = {Omega_m}")
print(f"  Omega_b   = {Omega_b}")
print(f"  Omega_c   = {Omega_c:.4f}")
print(f"  omega_m   = {omega_m:.5f}")
print(f"  omega_b   = {omega_b:.5f}")
print(f"  omega_c   = {omega_c:.5f}")
print(f"  k_pivot   = {k_pivot} Mpc^-1")
print(f"  R_8       = {R_8} h^-1 Mpc")
print(f"  T_CMB     = {T_cmb} K")

print(f"\n--- alpha_s Cases ---")
print(f"  (a) LCDM standard:   alpha_s = {alpha_s_zero}")
print(f"  (b) O-Z rigid:       alpha_s = n_s^2 - 1 = {alpha_s_oz:.6f}")
print(f"  (c) S48 lattice:     alpha_s = {alpha_s_lattice}")
print(f"  S49 Bayesian median: alpha_s = {alpha_s_oz_median:.6f} +/- {alpha_s_oz_std:.6f}")

# ===========================================================================
# STEP 1: EISENSTEIN-HU TRANSFER FUNCTION (1998, with baryons)
# ===========================================================================
print(f"\n--- Step 1: Eisenstein-Hu Transfer Function ---")

# Reference: Eisenstein & Hu, ApJ 496, 605 (1998)
# This is the full baryon + CDM fitting formula, equations (2)-(31).

def eisenstein_hu_transfer(k_h_Mpc, omega_m_phys, omega_b_phys, h_val, T_cmb_K=2.7255):
    """
    Eisenstein-Hu (1998) transfer function with baryon oscillations.

    Parameters:
        k_h_Mpc: wavenumber in h/Mpc
        omega_m_phys: Omega_m * h^2
        omega_b_phys: Omega_b * h^2
        h_val: dimensionless Hubble parameter
        T_cmb_K: CMB temperature in K

    Returns:
        T(k): transfer function (normalized to 1 at k -> 0)
    """
    # Abbreviations
    om = omega_m_phys
    ob = omega_b_phys
    oc = om - ob
    fb = ob / om   # baryon fraction
    fc = oc / om   # CDM fraction
    theta = T_cmb_K / 2.7  # CMB temperature in units of 2.7 K

    # Redshift of matter-radiation equality (eq. 2)
    z_eq = 2.50e4 * om * theta**(-4)

    # Redshift of baryon drag epoch (eq. 4)
    b1 = 0.313 * om**(-0.419) * (1.0 + 0.607 * om**0.674)
    b2 = 0.238 * om**0.223
    z_d = 1291.0 * om**0.251 / (1.0 + 0.659 * om**0.828) * (1.0 + b1 * ob**b2)

    # Sound horizon at drag epoch (eq. 6)
    R_eq = 31.5e3 * ob * theta**(-4) / z_eq     # R at z_eq (eq. 5)
    R_d = 31.5e3 * ob * theta**(-4) / z_d       # R at z_d (eq. 5)
    s = (2.0 / (3.0 * np.sqrt(6.0 / R_eq))) * np.sqrt(1.0 + R_d) * np.log(
        (np.sqrt(1.0 + R_d) + np.sqrt(R_d + R_eq)) / (1.0 + np.sqrt(R_eq))
    ) / np.sqrt(om)
    # s is in units of h^{-1} Mpc when om = Omega_m * h^2

    # Silk damping scale (eq. 7)
    k_silk = 1.6 * ob**0.52 * om**0.73 * (1.0 + (10.4 * om)**(-0.95))

    # CDM transfer function (eqs. 11-12)
    a1 = (46.9 * om)**0.670 * (1.0 + (32.1 * om)**(-0.532))
    a2 = (12.0 * om)**0.424 * (1.0 + (45.0 * om)**(-0.582))
    alpha_c = a1**(-fb) * a2**(-fb**3)

    b1_c = 0.944 / (1.0 + (458.0 * om)**(-0.708))
    b2_c = (0.395 * om)**(-0.0266)
    beta_c = 1.0 / (1.0 + b1_c * ((fc)**b2_c - 1.0))

    # q parameter (eq. 10)
    k_eq = 7.46e-2 * om * theta**(-2)  # in h/Mpc
    q = k_h_Mpc / (13.41 * k_eq)

    def T_tilde(k_h, alpha_val, beta_val):
        """Eq. (17)-(20) CDM transfer function piece."""
        q_local = k_h / (13.41 * k_eq)
        C = 14.2 / alpha_val + 386.0 / (1.0 + 69.9 * q_local**1.08)
        T0 = np.log(np.e + 1.8 * beta_val * q_local)
        T0 = T0 / (T0 + C * q_local**2)
        return T0

    # f function (eq. 18) -- interpolation between beta_c=1 and beta_c != 1
    f_val = 1.0 / (1.0 + (k_h_Mpc * s / 5.4)**4)
    Tc = f_val * T_tilde(k_h_Mpc, 1.0, beta_c) + (1.0 - f_val) * T_tilde(k_h_Mpc, alpha_c, 1.0)

    # Baryon transfer function (eqs. 21-24)
    y = z_eq / z_d
    G_y = y * (-6.0 * np.sqrt(1.0 + y) + (2.0 + 3.0 * y) * np.log(
        (np.sqrt(1.0 + y) + 1.0) / (np.sqrt(1.0 + y) - 1.0)
    ))

    alpha_b = 2.07 * k_eq * s * (1.0 + R_d)**(-3.0/4.0) * G_y

    beta_node = 8.41 * om**0.435
    beta_b = 0.5 + fb + (3.0 - 2.0 * fb) * np.sqrt((17.2 * om)**2 + 1.0)

    # s_tilde (eq. 22)
    # Note: this uses the Silk damping
    s_tilde = s / (1.0 + (beta_node / (k_h_Mpc * s))**3)**(1.0/3.0)

    # Baryon transfer function (eq. 21)
    j0_ks = np.sinc(k_h_Mpc * s_tilde / PI)  # np.sinc(x) = sin(pi*x)/(pi*x)
    Tb = (T_tilde(k_h_Mpc, 1.0, 1.0) / (1.0 + (k_h_Mpc * s / 5.2)**2) +
          alpha_b / (1.0 + (beta_b / (k_h_Mpc * s))**3) *
          np.exp(-(k_h_Mpc / k_silk)**1.4)) * j0_ks

    # Total transfer function (eq. 16)
    T_total = fb * Tb + fc * Tc

    return T_total


# Quick verification: compute at a few k values
k_test = np.array([0.001, 0.01, 0.1, 1.0, 10.0])
T_test = eisenstein_hu_transfer(k_test, omega_m, omega_b, h, T_cmb)
print(f"  Eisenstein-Hu T(k) check (k in h/Mpc):")
for ki, Ti in zip(k_test, T_test):
    print(f"    k = {ki:8.4f} h/Mpc -> T(k) = {Ti:.6f}")

# ===========================================================================
# STEP 2: PRIMORDIAL POWER SPECTRUM WITH RUNNING
# ===========================================================================
print(f"\n--- Step 2: Primordial Power Spectrum ---")

def primordial_PR(k_Mpc_inv, n_s_val, alpha_s_val, A_s_val, k_piv=0.05):
    """
    Primordial curvature power spectrum with running.

    P_R(k) = A_s * (k/k_pivot)^{n_s - 1 + (1/2)*alpha_s*ln(k/k_pivot)}

    Parameters:
        k_Mpc_inv: wavenumber in Mpc^{-1}
        n_s_val: scalar spectral index
        alpha_s_val: running of spectral index dn_s/d(ln k)
        A_s_val: scalar amplitude at pivot
        k_piv: pivot scale in Mpc^{-1}

    Returns:
        P_R(k): dimensionless primordial power spectrum
    """
    x = np.log(k_Mpc_inv / k_piv)
    # Exponent: (n_s - 1)*x + (1/2)*alpha_s*x^2
    exponent = (n_s_val - 1.0) * x + 0.5 * alpha_s_val * x**2
    return A_s_val * np.exp(exponent)


# Show running effect at key scales
print(f"  P_R ratio (running/no-running) at key scales:")
k_scales = {'k=0.001 Mpc^-1 (very large scales)': 0.001,
             'k=0.01 Mpc^-1 (BAO scales)': 0.01,
             'k=0.05 Mpc^-1 (pivot)': 0.05,
             'k=0.1 Mpc^-1': 0.1,
             'k=0.5 Mpc^-1': 0.5,
             'k=1.0 Mpc^-1 (sigma_8 scales)': 1.0,
             'k=10 Mpc^-1 (small scales)': 10.0}

for label, k_val in k_scales.items():
    PR_run = primordial_PR(k_val, n_s, alpha_s_oz, A_s)
    PR_norun = primordial_PR(k_val, n_s, 0.0, A_s)
    ratio = PR_run / PR_norun
    print(f"    {label:45s}: ratio = {ratio:.6f}  ({100*(ratio-1):+.2f}%)")

# ===========================================================================
# STEP 3: MATTER POWER SPECTRUM P(k) AND sigma_8
# ===========================================================================
print(f"\n--- Step 3: Matter Power Spectrum and sigma_8 ---")

def matter_power_spectrum(k_h_Mpc, n_s_val, alpha_s_val, A_s_val, h_val,
                          omega_m_phys, omega_b_phys, T_cmb_K, k_piv=0.05):
    """
    Linear matter power spectrum P(k) in (h^{-1} Mpc)^3.

    P(k) = (2*pi^2 / k^3) * Delta^2(k)
    where Delta^2(k) = (4/25) * (k/(a_0*H_0))^4 * T^2(k) * P_R(k)
         (in matter domination, Poisson equation gives delta ~ k^2 * Phi)

    But for sigma_8 the standard normalization uses:
    P(k) = A_s * (k*h/k_pivot)^{n_s - 1 + ...} * T^2(k) * k * (2*pi^2 / k_pivot^{n_s-1+...})

    Actually, the cleanest formulation is:
    P(k) [in (h^-1 Mpc)^3] = (2*pi^2) * (2*c^2/(5*Omega_m*H_0^2))^2 * k * T^2(k) * P_R(k/h)

    But for sigma_8 what matters is the RATIO between cases, since A_s is the same.
    The absolute normalization comes from matching to Planck sigma_8 at alpha_s = 0.

    We use the standard formulation:
    P(k) = N * k^{n_s + alpha_s*ln(k*h/k_pivot)/2} * T^2(k) * delta_H^2

    Actually the simplest correct approach: compute sigma_8 as an integral and
    normalize so that alpha_s=0 gives sigma_8 = 0.811 (Planck).
    Then the running cases give shifted sigma_8 values.
    """
    # k_h_Mpc is in h/Mpc. Convert to Mpc^{-1} for primordial spectrum
    k_Mpc = k_h_Mpc * h_val

    # Primordial power spectrum
    PR = primordial_PR(k_Mpc, n_s_val, alpha_s_val, A_s_val, k_piv)

    # Transfer function
    T_k = eisenstein_hu_transfer(k_h_Mpc, omega_m_phys, omega_b_phys, h_val, T_cmb_K)

    # The matter power spectrum is proportional to k * T^2(k) * P_R(k)
    # (the k factor comes from the relationship between P_R and P_m in LCDM)
    # P(k) = (2*pi^2) * delta_H^2 * (c*k/(H_0))^{n_eff} * T^2(k) / k^3
    # In terms of k in h/Mpc:
    # P(k) propto k * T^2(k) * (k*h/k_pivot)^{n_s - 1 + alpha_s/2 * ln(k*h/k_pivot)}

    # Since we're normalizing to Planck sigma_8, we just need the k-dependent part:
    P_k = k_h_Mpc * T_k**2 * PR

    return P_k


def compute_sigma_R(R_val, n_s_val, alpha_s_val, A_s_val, h_val,
                    omega_m_phys, omega_b_phys, T_cmb_K, k_piv=0.05):
    """
    Compute sigma(R) = sqrt{ (1/2*pi^2) * integral k^2 P(k) W^2(kR) dk }

    where W(x) = 3*(sin(x) - x*cos(x))/x^3 is the top-hat window function,
    R is in h^{-1} Mpc, and k is in h/Mpc.

    Since P(k) is unnormalized (proportional), this returns the unnormalized
    integral. We normalize by requiring alpha_s=0 -> sigma_8 = 0.811.
    """
    def integrand(lnk):
        k = np.exp(lnk)
        x = k * R_val
        # Top-hat window function
        if x < 1e-6:
            W = 1.0  # Taylor expansion: W ~ 1 - x^2/10 + ...
        else:
            W = 3.0 * (np.sin(x) - x * np.cos(x)) / x**3

        Pk = matter_power_spectrum(k, n_s_val, alpha_s_val, A_s_val, h_val,
                                   omega_m_phys, omega_b_phys, T_cmb_K, k_piv)

        # d(ln k) integral: integrand = k^3 * P(k) * W^2(kR) / (2*pi^2)
        return k**3 * Pk * W**2 / (2.0 * PI**2)

    # Integrate over ln(k) from k_min to k_max
    # sigma_8 is dominated by k ~ 0.01 - 1 h/Mpc, but we go wider for accuracy
    lnk_min = np.log(1e-5)  # k = 1e-5 h/Mpc
    lnk_max = np.log(1e2)   # k = 100 h/Mpc

    result, error = quad(integrand, lnk_min, lnk_max, limit=500, epsrel=1e-8)

    return np.sqrt(result), error


# Vectorized version for faster sigma_8 computation
def compute_sigma8_fast(n_s_val, alpha_s_val, A_s_val, h_val,
                        omega_m_phys, omega_b_phys, T_cmb_K,
                        R_val=8.0, k_piv=0.05, N_k=10000):
    """
    Compute sigma(R) using trapezoidal rule on a fine log-spaced grid.
    Faster than quad for many evaluations.
    """
    lnk = np.linspace(np.log(1e-5), np.log(1e2), N_k)
    k = np.exp(lnk)
    dlnk = lnk[1] - lnk[0]

    x = k * R_val
    # Top-hat window function (vectorized)
    W = np.where(x < 1e-6, 1.0, 3.0 * (np.sin(x) - x * np.cos(x)) / x**3)

    # Primordial spectrum
    k_Mpc = k * h_val
    PR = primordial_PR(k_Mpc, n_s_val, alpha_s_val, A_s_val, k_piv)

    # Transfer function
    T_k = eisenstein_hu_transfer(k, omega_m_phys, omega_b_phys, h_val, T_cmb_K)

    # P(k) proportional piece
    Pk = k * T_k**2 * PR

    # Integrand for sigma^2
    integrand = k**3 * Pk * W**2 / (2.0 * PI**2)

    # Trapezoidal integration in ln(k)
    sigma_sq = np.trapezoid(integrand, dx=dlnk)

    return np.sqrt(sigma_sq)


# ===========================================================================
# STEP 4: COMPUTE sigma_8 FOR THREE CASES
# ===========================================================================
print(f"\n--- Step 4: sigma_8 Computation (3 Cases) ---")

# First, compute with quad for accuracy
print(f"\n  Using scipy.integrate.quad (high accuracy):")

sigma8_raw_norun, err_norun = compute_sigma_R(
    R_8, n_s, alpha_s_zero, A_s, h, omega_m, omega_b, T_cmb)
print(f"  (a) alpha_s = 0:     sigma_8_raw = {sigma8_raw_norun:.8f}")

sigma8_raw_oz, err_oz = compute_sigma_R(
    R_8, n_s, alpha_s_oz, A_s, h, omega_m, omega_b, T_cmb)
print(f"  (b) alpha_s = {alpha_s_oz:.4f}: sigma_8_raw = {sigma8_raw_oz:.8f}")

sigma8_raw_lat, err_lat = compute_sigma_R(
    R_8, n_s, alpha_s_lattice, A_s, h, omega_m, omega_b, T_cmb)
print(f"  (c) alpha_s = {alpha_s_lattice}:  sigma_8_raw = {sigma8_raw_lat:.8f}")

# Normalize: alpha_s = 0 should give Planck sigma_8 = 0.811
# The normalization factor accounts for all the physics we computed proportionally
norm = sigma_8_planck_val / sigma8_raw_norun
print(f"\n  Normalization: sigma_8(Planck) / sigma_8_raw(alpha_s=0) = {norm:.8f}")

sigma8_norun = sigma8_raw_norun * norm
sigma8_oz = sigma8_raw_oz * norm
sigma8_lat = sigma8_raw_lat * norm

print(f"\n  NORMALIZED sigma_8 VALUES:")
print(f"  {'Case':<35s} {'alpha_s':>10s} {'sigma_8':>10s} {'Delta':>10s} {'Shift':>10s}")
print(f"  {'-'*75}")
print(f"  {'(a) LCDM (no running)':<35s} {alpha_s_zero:>10.4f} {sigma8_norun:>10.6f} {'(ref)':>10s} {'---':>10s}")
print(f"  {'(b) O-Z rigid (n_s^2 - 1)':<35s} {alpha_s_oz:>10.4f} {sigma8_oz:>10.6f} {sigma8_oz - sigma8_norun:>+10.6f} {100*(sigma8_oz/sigma8_norun - 1):>+9.2f}%")
print(f"  {'(c) S48 lattice (superseded)':<35s} {alpha_s_lattice:>10.4f} {sigma8_lat:>10.6f} {sigma8_lat - sigma8_norun:>+10.6f} {100*(sigma8_lat/sigma8_norun - 1):>+9.2f}%")

# Cross-check with fast method
sigma8_fast_norun = compute_sigma8_fast(n_s, alpha_s_zero, A_s, h, omega_m, omega_b, T_cmb) * norm
sigma8_fast_oz = compute_sigma8_fast(n_s, alpha_s_oz, A_s, h, omega_m, omega_b, T_cmb) * norm
print(f"\n  Cross-check (trapezoidal, N=10000):")
print(f"    alpha_s=0:   sigma_8 = {sigma8_fast_norun:.6f}  (quad: {sigma8_norun:.6f}, diff = {abs(sigma8_fast_norun - sigma8_norun):.2e})")
print(f"    alpha_s=OZ:  sigma_8 = {sigma8_fast_oz:.6f}  (quad: {sigma8_oz:.6f}, diff = {abs(sigma8_fast_oz - sigma8_oz):.2e})")

# ===========================================================================
# STEP 5: S_8 AND TENSION ANALYSIS
# ===========================================================================
print(f"\n--- Step 5: S_8 and Tension Analysis ---")

# S_8 = sigma_8 * sqrt(Omega_m / 0.3)
S8_factor = np.sqrt(Omega_m / 0.3)
S8_norun = sigma8_norun * S8_factor
S8_oz = sigma8_oz * S8_factor
S8_lat = sigma8_lat * S8_factor

print(f"\n  S_8 = sigma_8 * sqrt(Omega_m/0.3) [Omega_m = {Omega_m}]:")
print(f"  S_8 factor = sqrt({Omega_m}/0.3) = {S8_factor:.6f}")
print(f"  {'Case':<35s} {'sigma_8':>10s} {'S_8':>10s}")
print(f"  {'-'*55}")
print(f"  {'(a) LCDM (no running)':<35s} {sigma8_norun:>10.6f} {S8_norun:>10.6f}")
print(f"  {'(b) O-Z rigid':<35s} {sigma8_oz:>10.6f} {S8_oz:>10.6f}")
print(f"  {'(c) S48 lattice':<35s} {sigma8_lat:>10.6f} {S8_lat:>10.6f}")

# Observational values for comparison
# Planck CMB: sigma_8 = 0.811 +/- 0.006, S_8 = 0.832 +/- 0.013
# DES Y3: S_8 = 0.776 +/- 0.017
# KiDS-1000: S_8 = 0.759 +/- 0.024 (combined with spectroscopy)
# DES Y3 + KiDS: sigma_8 ~ 0.766 +/- 0.020 (approximate combined)
# Planck 2018 S_8 from their chains: 0.832 +/- 0.013
S8_planck = 0.832
S8_planck_err = 0.013
S8_des = 0.776
S8_des_err = 0.017
S8_kids = 0.759
S8_kids_err = 0.024

print(f"\n  OBSERVATIONAL COMPARISON:")
print(f"  {'Observable':<40s} {'Value':>10s} {'Error':>10s}")
print(f"  {'-'*60}")
print(f"  {'Planck 2018 sigma_8':<40s} {sigma_8_planck_val:>10.3f} {sigma_8_planck_err:>10.3f}")
print(f"  {'Lensing combined sigma_8':<40s} {sigma_8_lensing_val:>10.3f} {sigma_8_lensing_err:>10.3f}")
print(f"  {'Planck 2018 S_8':<40s} {S8_planck:>10.3f} {S8_planck_err:>10.3f}")
print(f"  {'DES Y3 S_8':<40s} {S8_des:>10.3f} {S8_des_err:>10.3f}")
print(f"  {'KiDS-1000 S_8':<40s} {S8_kids:>10.3f} {S8_kids_err:>10.3f}")

# Tension calculations
print(f"\n  TENSION ANALYSIS (O-Z rigid prediction):")

# sigma_8 tensions
tension_planck_sig8 = abs(sigma8_oz - sigma_8_planck_val) / sigma_8_planck_err
tension_lensing_sig8 = abs(sigma8_oz - sigma_8_lensing_val) / sigma_8_lensing_err

print(f"\n  sigma_8 = {sigma8_oz:.4f}:")
print(f"    vs Planck ({sigma_8_planck_val} +/- {sigma_8_planck_err}): "
      f"{tension_planck_sig8:.2f} sigma {'TENSION' if tension_planck_sig8 > 2 else 'OK'}")
print(f"    vs Lensing ({sigma_8_lensing_val} +/- {sigma_8_lensing_err}): "
      f"{tension_lensing_sig8:.2f} sigma {'TENSION' if tension_lensing_sig8 > 2 else 'OK'}")

# S_8 tensions
tension_planck_S8 = abs(S8_oz - S8_planck) / S8_planck_err
tension_des_S8 = abs(S8_oz - S8_des) / S8_des_err
tension_kids_S8 = abs(S8_oz - S8_kids) / S8_kids_err

print(f"\n  S_8 = {S8_oz:.4f}:")
print(f"    vs Planck ({S8_planck} +/- {S8_planck_err}): "
      f"{tension_planck_S8:.2f} sigma {'TENSION' if tension_planck_S8 > 2 else 'OK'}")
print(f"    vs DES Y3 ({S8_des} +/- {S8_des_err}): "
      f"{tension_des_S8:.2f} sigma {'TENSION' if tension_des_S8 > 2 else 'OK'}")
print(f"    vs KiDS ({S8_kids} +/- {S8_kids_err}): "
      f"{tension_kids_S8:.2f} sigma {'TENSION' if tension_kids_S8 > 2 else 'OK'}")

# Is sigma_8 closer to Planck or lensing?
closer_to = "Planck" if abs(sigma8_oz - sigma_8_planck_val) < abs(sigma8_oz - sigma_8_lensing_val) else "Lensing"
print(f"\n  O-Z sigma_8 = {sigma8_oz:.4f} is closer to: {closer_to}")
print(f"    Midpoint Planck/Lensing: {(sigma_8_planck_val + sigma_8_lensing_val)/2:.4f}")

# ===========================================================================
# STEP 6: PROPAGATE alpha_s UNCERTAINTY TO sigma_8
# ===========================================================================
print(f"\n--- Step 6: sigma_8 Uncertainty from alpha_s Posterior ---")

# Use fast computation for MC samples from S49
# The sigma_8 depends on alpha_s through the primordial spectrum.
# We propagate the full S49 posterior.

# Sample a subset (computing sigma_8 for each is somewhat expensive with quad)
N_prop = 500  # propagate 500 samples
rng_prop = np.random.RandomState(50)
idx_prop = rng_prop.choice(len(alpha_s_samples), size=N_prop, replace=False)
alpha_s_prop = alpha_s_samples[idx_prop]

sigma8_prop = np.zeros(N_prop)
for i in range(N_prop):
    sigma8_prop[i] = compute_sigma8_fast(
        n_s, alpha_s_prop[i], A_s, h, omega_m, omega_b, T_cmb) * norm

sigma8_prop_median = np.median(sigma8_prop)
sigma8_prop_mean = np.mean(sigma8_prop)
sigma8_prop_std = np.std(sigma8_prop)
sigma8_prop_ci68 = np.percentile(sigma8_prop, [16, 84])
sigma8_prop_ci95 = np.percentile(sigma8_prop, [2.5, 97.5])

S8_prop = sigma8_prop * S8_factor
S8_prop_median = np.median(S8_prop)
S8_prop_std = np.std(S8_prop)
S8_prop_ci95 = np.percentile(S8_prop, [2.5, 97.5])

print(f"  Propagated {N_prop} alpha_s samples -> sigma_8:")
print(f"    sigma_8 median = {sigma8_prop_median:.6f}")
print(f"    sigma_8 mean   = {sigma8_prop_mean:.6f}")
print(f"    sigma_8 std    = {sigma8_prop_std:.6f}")
print(f"    sigma_8 68% CI = [{sigma8_prop_ci68[0]:.6f}, {sigma8_prop_ci68[1]:.6f}]")
print(f"    sigma_8 95% CI = [{sigma8_prop_ci95[0]:.6f}, {sigma8_prop_ci95[1]:.6f}]")
print(f"    S_8 median     = {S8_prop_median:.6f} +/- {S8_prop_std:.6f}")
print(f"    S_8 95% CI     = [{S8_prop_ci95[0]:.6f}, {S8_prop_ci95[1]:.6f}]")

# ===========================================================================
# STEP 7: SENSITIVITY ANALYSIS -- WHERE DOES sigma_8 COME FROM?
# ===========================================================================
print(f"\n--- Step 7: Scale Decomposition of sigma_8 ---")

# Show cumulative sigma_8^2 as a function of k to see which scales dominate
k_fine = np.logspace(-4, 2, 5000)
dlnk = np.log(k_fine[1]/k_fine[0])

def sigma8_integrand(k_arr, alpha_s_val):
    """Return the integrand d(sigma_8^2)/d(ln k) for an array of k in h/Mpc."""
    x = k_arr * R_8
    W = np.where(x < 1e-6, 1.0, 3.0 * (np.sin(x) - x * np.cos(x)) / x**3)
    k_Mpc = k_arr * h
    PR = primordial_PR(k_Mpc, n_s, alpha_s_val, A_s, k_pivot)
    Tk = eisenstein_hu_transfer(k_arr, omega_m, omega_b, h, T_cmb)
    Pk = k_arr * Tk**2 * PR
    return k_arr**3 * Pk * W**2 / (2.0 * PI**2)

integ_norun = sigma8_integrand(k_fine, 0.0)
integ_oz = sigma8_integrand(k_fine, alpha_s_oz)
integ_lat = sigma8_integrand(k_fine, alpha_s_lattice)

# Cumulative sigma_8^2
cum_norun = np.cumsum(integ_norun) * dlnk
cum_oz = np.cumsum(integ_oz) * dlnk
cum_lat = np.cumsum(integ_lat) * dlnk

# Ratio of integrands
ratio_oz_norun = integ_oz / np.maximum(integ_norun, 1e-300)
ratio_lat_norun = integ_lat / np.maximum(integ_norun, 1e-300)

# Find peak of integrand
k_peak_norun = k_fine[np.argmax(integ_norun)]
k_peak_oz = k_fine[np.argmax(integ_oz)]
print(f"  Peak of sigma_8 integrand:")
print(f"    alpha_s = 0:   k_peak = {k_peak_norun:.4f} h/Mpc")
print(f"    alpha_s = OZ:  k_peak = {k_peak_oz:.4f} h/Mpc")

# sigma_8 contribution from different scale ranges
for k_lo, k_hi, label in [(1e-4, 0.01, 'k < 0.01 (large scales)'),
                            (0.01, 0.1, '0.01 < k < 0.1'),
                            (0.1, 1.0, '0.1 < k < 1.0 (sigma_8 core)'),
                            (1.0, 10.0, '1.0 < k < 10.0'),
                            (10.0, 100.0, 'k > 10 (small scales)')]:
    mask = (k_fine >= k_lo) & (k_fine < k_hi)
    frac_norun = np.sum(integ_norun[mask]) * dlnk / cum_norun[-1] * 100
    frac_oz = np.sum(integ_oz[mask]) * dlnk / cum_oz[-1] * 100
    ratio_frac = frac_oz / frac_norun if frac_norun > 0 else 0
    print(f"    {label:35s}: norun {frac_norun:6.2f}%, OZ {frac_oz:6.2f}%")

# ===========================================================================
# STEP 8: GATE VERDICT
# ===========================================================================
print(f"\n{'='*78}")
print(f"GATE VERDICT: SIGMA8-OZ-50")
print(f"{'='*78}")

print(f"\n  sigma_8 (O-Z rigid, alpha_s = {alpha_s_oz:.5f})")
print(f"    = {sigma8_oz:.4f}")
print(f"    with alpha_s uncertainty: {sigma8_prop_median:.4f} +/- {sigma8_prop_std:.4f}")
print(f"    95% CI: [{sigma8_prop_ci95[0]:.4f}, {sigma8_prop_ci95[1]:.4f}]")

print(f"\n  S_8 (O-Z rigid)")
print(f"    = {S8_oz:.4f}")
print(f"    with alpha_s uncertainty: {S8_prop_median:.4f} +/- {S8_prop_std:.4f}")

# Gate criteria
sigma8_pass_lo, sigma8_pass_hi = 0.740, 0.820
sigma8_fail_lo, sigma8_fail_hi = 0.640, 0.920

in_pass = sigma8_pass_lo <= sigma8_oz <= sigma8_pass_hi
in_fail = sigma8_oz < sigma8_fail_lo or sigma8_oz > sigma8_fail_hi

if in_pass:
    verdict = "PASS"
    detail = f"sigma_8 = {sigma8_oz:.4f} in [{sigma8_pass_lo}, {sigma8_pass_hi}]"
elif in_fail:
    verdict = "FAIL"
    detail = f"sigma_8 = {sigma8_oz:.4f} outside [{sigma8_fail_lo}, {sigma8_fail_hi}]"
else:
    verdict = "INFO"
    # Check if within 3-sigma of either dataset
    within_planck_3sig = abs(sigma8_oz - sigma_8_planck_val) < 3 * sigma_8_planck_err
    within_lensing_3sig = abs(sigma8_oz - sigma_8_lensing_val) < 3 * sigma_8_lensing_err
    detail = (f"sigma_8 = {sigma8_oz:.4f} outside [{sigma8_pass_lo}, {sigma8_pass_hi}] but "
              f"within 3-sigma of {'Planck' if within_planck_3sig else ''}"
              f"{' and ' if within_planck_3sig and within_lensing_3sig else ''}"
              f"{'Lensing' if within_lensing_3sig else ''}")

print(f"\n  GATE: {verdict}")
print(f"  Detail: {detail}")
print(f"\n  Pass band:  [{sigma8_pass_lo}, {sigma8_pass_hi}]")
print(f"  Fail band:  sigma_8 < {sigma8_fail_lo} or sigma_8 > {sigma8_fail_hi}")

print(f"\n  SUMMARY TABLE:")
print(f"  {'Quantity':<25s} {'O-Z Value':>12s} {'Planck':>12s} {'Lensing':>12s} {'Tension':>10s}")
print(f"  {'-'*71}")
print(f"  {'sigma_8':<25s} {sigma8_oz:>12.4f} {sigma_8_planck_val:>12.4f} {sigma_8_lensing_val:>12.4f} {tension_planck_sig8:>9.1f}s (P)")
print(f"  {'S_8':<25s} {S8_oz:>12.4f} {S8_planck:>12.4f} {S8_des:>12.4f} {tension_planck_S8:>9.1f}s (P)")
print(f"  {'shift from no-run (%)':<25s} {100*(sigma8_oz/sigma8_norun - 1):>+12.2f}% {'(ref)':>12s} {'':>12s}")

# ===========================================================================
# STEP 9: SAVE DATA
# ===========================================================================
print(f"\n--- Saving Data ---")

np.savez(os.path.join(data_dir, 's50_sigma8_oz.npz'),
    # Gate
    gate_name='SIGMA8-OZ-50',
    gate_verdict=verdict,
    gate_detail=detail,
    # Input parameters
    n_s=n_s,
    A_s=A_s,
    h=h,
    Omega_m=Omega_m,
    Omega_b=Omega_b,
    k_pivot=k_pivot,
    R_8=R_8,
    # alpha_s cases
    alpha_s_zero=alpha_s_zero,
    alpha_s_oz=alpha_s_oz,
    alpha_s_lattice=alpha_s_lattice,
    alpha_s_oz_median=alpha_s_oz_median,
    alpha_s_oz_std=alpha_s_oz_std,
    # sigma_8 results
    sigma8_norun=sigma8_norun,
    sigma8_oz=sigma8_oz,
    sigma8_lat=sigma8_lat,
    sigma8_prop_median=sigma8_prop_median,
    sigma8_prop_mean=sigma8_prop_mean,
    sigma8_prop_std=sigma8_prop_std,
    sigma8_prop_ci68=sigma8_prop_ci68,
    sigma8_prop_ci95=sigma8_prop_ci95,
    # S_8 results
    S8_oz=S8_oz,
    S8_norun=S8_norun,
    S8_prop_median=S8_prop_median,
    S8_prop_std=S8_prop_std,
    S8_prop_ci95=S8_prop_ci95,
    # Tensions
    tension_planck_sig8=tension_planck_sig8,
    tension_lensing_sig8=tension_lensing_sig8,
    tension_planck_S8=tension_planck_S8,
    tension_des_S8=tension_des_S8,
    tension_kids_S8=tension_kids_S8,
    # Shift
    sigma8_shift_percent=100*(sigma8_oz/sigma8_norun - 1),
    # Scale decomposition (save sparse for plotting)
    k_fine=k_fine,
    integ_norun=integ_norun,
    integ_oz=integ_oz,
    integ_lat=integ_lat,
    cum_norun=cum_norun,
    cum_oz=cum_oz,
    cum_lat=cum_lat,
    # MC propagation
    sigma8_prop_samples=sigma8_prop,
    alpha_s_prop_samples=alpha_s_prop,
    # Normalization
    norm_factor=norm,
    # Timing
    elapsed_s=time.time() - t0,
)
print(f"  Saved: s50_sigma8_oz.npz")

# ===========================================================================
# STEP 10: PLOT
# ===========================================================================
print(f"\n--- Generating Plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.30, wspace=0.30)

# Panel 1: sigma_8 integrand d(sigma_8^2)/d(ln k)
ax1 = fig.add_subplot(gs[0, 0])
ax1.loglog(k_fine, integ_norun * norm**2, 'k-', lw=2, label=r'$\alpha_s = 0$ (LCDM)')
ax1.loglog(k_fine, integ_oz * norm**2, 'r-', lw=2, label=fr'$\alpha_s = {alpha_s_oz:.4f}$ (O-Z)')
ax1.loglog(k_fine, integ_lat * norm**2, 'b--', lw=1.5, label=fr'$\alpha_s = {alpha_s_lattice}$ (S48)')
ax1.axvline(1.0/R_8, color='gray', ls=':', lw=1, label=r'$k = 1/R_8$')
ax1.set_xlabel(r'$k$ [$h$ Mpc$^{-1}$]', fontsize=12)
ax1.set_ylabel(r'$d\sigma_8^2 / d\ln k$ (normalized)', fontsize=12)
ax1.set_title(r'$\sigma_8$ Integrand', fontsize=13)
ax1.legend(fontsize=9, loc='upper right')
ax1.set_xlim(1e-4, 10)
ax1.grid(True, alpha=0.3)

# Panel 2: Cumulative sigma_8
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogx(k_fine, np.sqrt(cum_norun) * norm, 'k-', lw=2, label=r'$\alpha_s = 0$')
ax2.semilogx(k_fine, np.sqrt(cum_oz) * norm, 'r-', lw=2, label=fr'$\alpha_s = {alpha_s_oz:.4f}$')
ax2.semilogx(k_fine, np.sqrt(cum_lat) * norm, 'b--', lw=1.5, label=fr'$\alpha_s = {alpha_s_lattice}$')
ax2.axhline(sigma_8_planck_val, color='gold', ls='-', lw=2, label=f'Planck $\\sigma_8$ = {sigma_8_planck_val}')
ax2.axhspan(sigma_8_planck_val - sigma_8_planck_err, sigma_8_planck_val + sigma_8_planck_err,
            color='gold', alpha=0.2)
ax2.axhline(sigma_8_lensing_val, color='green', ls='-', lw=2, label=f'Lensing $\\sigma_8$ = {sigma_8_lensing_val}')
ax2.axhspan(sigma_8_lensing_val - sigma_8_lensing_err, sigma_8_lensing_val + sigma_8_lensing_err,
            color='green', alpha=0.2)
ax2.set_xlabel(r'$k$ [$h$ Mpc$^{-1}$]', fontsize=12)
ax2.set_ylabel(r'Cumulative $\sigma(R_8, k_{\rm max})$', fontsize=12)
ax2.set_title(r'Cumulative $\sigma_8$ vs Integration Limit', fontsize=13)
ax2.legend(fontsize=8, loc='lower right')
ax2.set_xlim(1e-4, 10)
ax2.set_ylim(0, 0.95)
ax2.grid(True, alpha=0.3)

# Panel 3: sigma_8 comparison bar chart with error bands
ax3 = fig.add_subplot(gs[1, 0])
labels = ['LCDM\n($\\alpha_s=0$)', f'O-Z rigid\n($\\alpha_s={alpha_s_oz:.3f}$)',
          f'S48 lattice\n($\\alpha_s={alpha_s_lattice}$)']
vals = [sigma8_norun, sigma8_oz, sigma8_lat]
colors = ['gray', 'red', 'blue']
x_pos = [0, 1, 2]

bars = ax3.bar(x_pos, vals, color=colors, alpha=0.7, width=0.6)
# O-Z error bar from MC propagation
ax3.errorbar(1, sigma8_prop_median, yerr=sigma8_prop_std, fmt='none', ecolor='darkred',
             capsize=8, capthick=2, lw=2)

# Planck band
ax3.axhspan(sigma_8_planck_val - sigma_8_planck_err, sigma_8_planck_val + sigma_8_planck_err,
            color='gold', alpha=0.3, label=f'Planck $\\sigma_8$')
ax3.axhline(sigma_8_planck_val, color='goldenrod', ls='-', lw=1.5)

# Lensing band
ax3.axhspan(sigma_8_lensing_val - sigma_8_lensing_err, sigma_8_lensing_val + sigma_8_lensing_err,
            color='green', alpha=0.2, label=f'Lensing $\\sigma_8$')
ax3.axhline(sigma_8_lensing_val, color='darkgreen', ls='-', lw=1.5)

ax3.set_xticks(x_pos)
ax3.set_xticklabels(labels, fontsize=10)
ax3.set_ylabel(r'$\sigma_8$', fontsize=12)
ax3.set_title(r'$\sigma_8$ Comparison', fontsize=13)
ax3.legend(fontsize=9, loc='upper right')
ax3.set_ylim(0.70, 0.85)
ax3.grid(True, axis='y', alpha=0.3)

# Annotate values on bars
for xp, val in zip(x_pos, vals):
    ax3.text(xp, val + 0.003, f'{val:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Panel 4: P(k) ratio showing running effect
ax4 = fig.add_subplot(gs[1, 1])
# Primordial ratio
k_pr = np.logspace(-4, 2, 2000)
PR_norun_arr = primordial_PR(k_pr * h, n_s, 0.0, A_s, k_pivot)
PR_oz_arr = primordial_PR(k_pr * h, n_s, alpha_s_oz, A_s, k_pivot)
PR_lat_arr = primordial_PR(k_pr * h, n_s, alpha_s_lattice, A_s, k_pivot)

ax4.semilogx(k_pr, PR_oz_arr / PR_norun_arr, 'r-', lw=2, label=fr'$\alpha_s = {alpha_s_oz:.4f}$ (O-Z)')
ax4.semilogx(k_pr, PR_lat_arr / PR_norun_arr, 'b--', lw=1.5, label=fr'$\alpha_s = {alpha_s_lattice}$ (S48)')
ax4.axhline(1.0, color='k', ls=':', lw=1)
ax4.axvline(k_pivot / h, color='gray', ls=':', lw=1, label=r'$k_{\rm pivot}/h$')

# Shade the sigma_8-sensitive region
ax4.axvspan(0.03, 0.5, color='red', alpha=0.05, label=r'$\sigma_8$ window')

ax4.set_xlabel(r'$k$ [$h$ Mpc$^{-1}$]', fontsize=12)
ax4.set_ylabel(r'$\mathcal{P}_\mathcal{R}(\alpha_s) / \mathcal{P}_\mathcal{R}(0)$', fontsize=12)
ax4.set_title('Primordial Power Ratio (Running / No Running)', fontsize=13)
ax4.legend(fontsize=9, loc='lower left')
ax4.set_xlim(1e-4, 100)
ax4.set_ylim(0.5, 1.5)
ax4.grid(True, alpha=0.3)

# Add overall title with gate verdict
fig.suptitle(f'SIGMA8-OZ-50: $\\sigma_8$ from O-Z Rigid $\\alpha_s = n_s^2 - 1 = {alpha_s_oz:.4f}$\n'
             f'$\\sigma_8 = {sigma8_oz:.4f}$, Shift = {100*(sigma8_oz/sigma8_norun - 1):+.1f}%  |  '
             f'Gate: {verdict}',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig(os.path.join(data_dir, 's50_sigma8_oz.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s50_sigma8_oz.png")

elapsed = time.time() - t0
print(f"\n  Total elapsed: {elapsed:.1f}s")
print(f"\n{'='*78}")
print(f"DONE: SIGMA8-OZ-50")
print(f"  sigma_8(O-Z) = {sigma8_oz:.4f}")
print(f"  S_8(O-Z)     = {S8_oz:.4f}")
print(f"  Shift         = {100*(sigma8_oz/sigma8_norun - 1):+.2f}% from no-running")
print(f"  Gate:          {verdict}")
print(f"{'='*78}")
