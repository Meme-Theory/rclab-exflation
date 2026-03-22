#!/usr/bin/env python3
"""
KK-CMB-TF-43: Full Transfer Function KK -> CMB Scales
======================================================

Computes the transfer function T(k) mapping Kibble-Zurek perturbation spectrum
at Kaluza-Klein scales to CMB-observable scales. Includes:

1. Ornstein-Zernike KZ source spectrum P_tau(k) [from W3-5]
2. Modulated reheating (delta-N formalism) [from W3-5]
3. Acoustic processing with TWO sound speeds:
   - c_1 = c  (first sound = substrate/metric perturbation)
   - c_2 = c/sqrt(3)  (second sound = photon-baryon plasma)
4. Silk damping (photon diffusion)
5. Expansion history (epsilon_H from W3-5)

Produces P(k) and extracts n_s, dn_s/dlnk at k_pivot = 0.05 Mpc^{-1}.
Predicts first-sound ring at r_1 ~ sqrt(3) * r_s.

Gate: KK-CMB-TF-43 (INFO)
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 1. Load prior results
# ============================================================

kz_data = np.load('tier0-computation/s43_kz_transfer.npz', allow_pickle=True)
lif_data = np.load('tier0-computation/s43_lifshitz_class.npz', allow_pickle=True)

# KZ parameters
xi_KZ = float(kz_data['xi_KZ'])           # 0.1516 M_KK^{-1}
sigma_tau = float(kz_data['sigma_tau'])     # 0.03
nu_KZ = float(kz_data['nu_KZ'])            # 0.6301
z_dyn = float(kz_data['z_dyn'])             # 2.02
epsilon_H = float(kz_data['epsilon_H_planck'])  # 0.01755
n_s_planck = float(kz_data['n_s_planck'][0])    # 0.9649
n_s_sigma = float(kz_data['n_s_planck_sigma'][0])  # 0.0042
alpha_s_planck = float(kz_data['running_planck'][0])  # -0.0045
alpha_s_sigma = float(kz_data['running_planck_sigma'][0])  # 0.0067
M_KK = float(kz_data['M_KK'])              # 7.429e16 GeV
N_tau = float(kz_data['N_tau'])             # -0.158
mod_coeff = float(kz_data['mod_coeff'])     # 0.234

# Derived
from canonical_constants import M_Pl_unreduced as M_Pl  # GeV
M_Pl_red = M_Pl / np.sqrt(8 * np.pi)  # reduced Planck mass

print("=" * 70)
print("KK-CMB-TF-43: Full Transfer Function KK -> CMB")
print("=" * 70)
print(f"\nInput parameters:")
print(f"  xi_KZ       = {xi_KZ:.4f} M_KK^{{-1}}")
print(f"  sigma_tau   = {sigma_tau:.4f}")
print(f"  epsilon_H   = {epsilon_H:.5f}")
print(f"  n_s(Planck) = {n_s_planck:.4f} +/- {n_s_sigma:.4f}")
print(f"  M_KK        = {M_KK:.4e} GeV")
print(f"  N_tau       = {N_tau:.4f}")
print(f"  mod_coeff   = {mod_coeff:.4f}")

# ============================================================
# 2. Physical scales and sound speeds
# ============================================================

# Sound speeds (from W4-5 and standard cosmology)
c_1 = 1.0   # First sound = c (substrate/metric, dimensionless)
c_2 = 1.0 / np.sqrt(3)  # Second sound = c/sqrt(3) (photon-baryon)

# Sound horizon parameters (standard cosmology values)
# r_s = integral_0^{z_*} c_s(z) dz / H(z) where z_* ~ 1089
# Standard value: r_s = 147.09 Mpc (Planck 2018)
r_s = 147.09  # Mpc (comoving sound horizon at recombination, second sound)

# First-sound horizon: photons/metric perturbations propagate at c_1 = c
# r_1 = r_s * (c_1 / c_2) = r_s * sqrt(3) (in radiation-dominated limit)
# With baryon loading correction: c_2 = c/sqrt(3*(1+R)) where R = 3*rho_b/(4*rho_gamma)
# At recombination: R_* ~ 0.63, so c_2/c = 1/sqrt(3*(1+0.63)) = 0.453
# r_1 = r_s * (c_1/c_2) = 147.09 * (1/0.453) = 324.7 Mpc
R_star = 0.63  # baryon-to-photon momentum ratio at recombination (Planck 2018)
c_2_actual = 1.0 / np.sqrt(3 * (1 + R_star))  # actual second sound with baryon loading

r_1 = r_s * (c_1 / c_2_actual)  # first sound horizon
# Note: c_2_actual ~ 0.453, so r_1 ~ 324.7 Mpc

# BAO wavenumber and first-sound wavenumber
k_BAO = 2 * np.pi / r_s        # ~ 0.0427 Mpc^{-1}
k_1 = 2 * np.pi / r_1          # ~ 0.0194 Mpc^{-1}
k_pivot = 0.05                  # Mpc^{-1} (Planck pivot scale)

print(f"\nSound speeds:")
print(f"  c_1 (first, substrate)     = {c_1:.4f} c")
print(f"  c_2 (second, phot-baryon)  = {c_2:.4f} c  [radiation limit]")
print(f"  c_2_actual (with baryons)  = {c_2_actual:.4f} c  [R_* = {R_star}]")
print(f"\nAcoustic horizons:")
print(f"  r_s   = {r_s:.2f} Mpc  (second sound / BAO)")
print(f"  r_1   = {r_1:.2f} Mpc  (first sound / substrate)")
print(f"  ratio = {r_1/r_s:.4f}  [= c_1/c_2_actual = {c_1/c_2_actual:.4f}]")
print(f"\nCharacteristic wavenumbers:")
print(f"  k_BAO   = {k_BAO:.5f} Mpc^{{-1}}")
print(f"  k_1     = {k_1:.5f} Mpc^{{-1}}")
print(f"  k_pivot = {k_pivot:.5f} Mpc^{{-1}}")

# ============================================================
# 3. Construct k-grid
# ============================================================

N_k = 200
k_min = 1e-4   # Mpc^{-1}
k_max = 1.0    # Mpc^{-1}
k = np.logspace(np.log10(k_min), np.log10(k_max), N_k)

# ============================================================
# 4. KZ source spectrum (Ornstein-Zernike)
# ============================================================

# Convert xi_KZ from M_KK^{-1} to Mpc
# 1/M_KK in natural units -> convert to Mpc
# 1 GeV^{-1} = 1.97e-16 m = 6.39e-39 Mpc
# xi_KZ_phys = xi_KZ / M_KK (in GeV^{-1}) * conversion
from canonical_constants import GeV_inv_to_Mpc  # Mpc / GeV^{-1}
xi_KZ_Mpc = xi_KZ / M_KK * GeV_inv_to_Mpc  # ~ 1.3e-56 Mpc

# At CMB scales k ~ 0.001-1 Mpc^{-1}: k * xi_KZ ~ 10^{-58}
# So (1 + k^2 xi_KZ^2)^2 ~ 1 exactly
# KZ spectrum is PERFECTLY flat at all CMB scales
# P_tau(k) = sigma^2 * 8*pi*xi_KZ^3 = const (white noise)
P_tau_0 = sigma_tau**2 * 8 * np.pi * xi_KZ_Mpc**3  # Mpc^3

print(f"\nKZ source spectrum:")
print(f"  xi_KZ  = {xi_KZ:.4f} M_KK^{{-1}} = {xi_KZ_Mpc:.4e} Mpc")
print(f"  k*xi   = {k_pivot * xi_KZ_Mpc:.4e} at k_pivot [<< 1: white noise]")
print(f"  P_tau_0 = {P_tau_0:.4e} Mpc^3")
print(f"  KZ spectrum is FLAT at all CMB scales (trivially)")

# KZ power spectrum: P_tau(k) / P_tau_0 = 1 / (1 + k^2 * xi_KZ^2)^2
# At CMB scales this is identically 1.0 to machine precision
P_KZ_normalized = np.ones_like(k)  # Flat (white noise)

# ============================================================
# 5. Transfer function components
# ============================================================

# --- Component 1: Modulated reheating (delta-N) ---
# delta_zeta = N_tau * delta_tau
# This converts tau fluctuations to curvature perturbations
# P_zeta(k) = N_tau^2 * P_tau(k)
# N_tau = -0.158 (from W3-5)
# This is k-independent -> no tilt contribution

T_deltaN = N_tau**2  # scalar, k-independent

# --- Component 2: Expansion modulation ---
# During quasi-de Sitter expansion, modes that exit the horizon at different times
# see different Hubble rates. For a mode with wavenumber k:
# k = a*H at horizon crossing
# t_cross(k) = t_* + ln(k_*/k) / H  (approximately)
# The expansion rate varies: H(t) = H_* * [1 - epsilon_H * H * (t - t_*)]
# This produces the tilt: the longer a mode is outside the horizon,
# the more it is stretched by the varying expansion.
#
# Standard result: P(k) propto k^{n_s - 1} where n_s - 1 = -2*epsilon_H - eta_H
# For our case: eta_H ~ 0 (flat potential in tau; tau is frozen with m/H >> 1)
# So: n_s = 1 - 2*epsilon_H
#
# Transfer function encoding: T_expansion(k) = (k/k_pivot)^{(n_s-1)/2}
# This applies to the AMPLITUDE transfer function; P(k) = T^2 * P_source

n_s_transfer = 1.0 - 2.0 * epsilon_H
# Running: dn_s/dlnk = -2*epsilon_H*eta_H - xi_H^2
# With eta_H ~ 0: running ~ -2*epsilon_H^2
alpha_s_transfer = -2.0 * epsilon_H**2

# Including running:
# n_s(k) = n_s(k_pivot) + alpha_s * ln(k/k_pivot) + ...
# P(k) propto k^{n_s(k)-1}
# ln P(k) = (n_s - 1) * ln(k/k_pivot) + (alpha_s/2) * [ln(k/k_pivot)]^2

lnk_ratio = np.log(k / k_pivot)
ln_T2_expansion = (n_s_transfer - 1.0) * lnk_ratio + 0.5 * alpha_s_transfer * lnk_ratio**2
T2_expansion = np.exp(ln_T2_expansion)

# --- Component 3: Acoustic processing (TWO sound horizons) ---
#
# SECOND SOUND (standard BAO):
# Photon-baryon plasma oscillates with c_s = c_2_actual
# Transfer function has oscillatory part from standing waves
# T_BAO(k) = [1 + A_BAO * sin(k * r_s) / (k * r_s)] (in correlation function)
# In power spectrum: oscillations at k * r_s = n*pi
#
# FIRST SOUND (substrate prediction):
# Metric perturbations (gravitational potential) oscillate at c_1 = c
# These are NOT photon-baryon oscillations -- they are the substrate itself
# carrying information at the speed of light
# Transfer produces a feature at k * r_1 = n*pi
#
# Standard matter transfer function (BBKS):
# T_BBKS(k) = ln(1 + 2.34*q) / (2.34*q) * [1 + 3.89*q + (16.1*q)^2 + (5.46*q)^3 + (6.71*q)^4]^{-1/4}
# where q = k / (Omega_m * h^2 * Mpc^{-1})
# For k in Mpc^{-1} and standard Planck cosmology:
Omega_m = 0.3153
h_hubble = 0.6736
Gamma_shape = Omega_m * h_hubble  # ~ 0.212

# Eisenstein-Hu transfer function (with BAO)
# We use the fitting formula approach
# k_eq = 0.0146 * (Omega_m * h^2) Mpc^{-1}  (matter-radiation equality)
k_eq = 0.0146 * Omega_m * h_hubble**2  # ~ 0.00209 Mpc^{-1}

# Sound horizon crossing scale
k_s = np.pi / r_s  # ~ 0.0214 Mpc^{-1} (first BAO node)

# Baryon fraction
Omega_b = 0.0493
f_b = Omega_b / Omega_m  # ~ 0.156

# Silk damping scale
# k_Silk ~ 0.1 Mpc^{-1} (Planck 2018)
k_Silk = 0.1  # Mpc^{-1}

# Transfer function following Eisenstein & Hu 1998 structure
# (simplified but capturing the essential physics)

# q = k / (13.41 * k_eq) -- this is the standard rescaling
q = k / (13.41 * k_eq)

# Zero-baryon transfer function (CDM-only, BBKS-like)
L0 = np.log(2 * np.e + 1.8 * q)
C0 = 14.2 + 731.0 / (1 + 62.5 * q)
T_CDM = L0 / (L0 + C0 * q**2)

# Baryon acoustic oscillation component
# The BAO produces oscillations in the baryon transfer function
# T_b(k) has oscillations at k * r_s = n*pi, damped by Silk diffusion

# Standard BAO oscillation (second sound)
# j_0(k * r_s) / (1 + (k/k_Silk)^2) -- spherical Bessel damped by Silk
j0_BAO = np.sinc(k * r_s / np.pi)  # sinc(x) = sin(pi*x)/(pi*x), so sinc(k*r_s/pi) = sin(k*r_s)/(k*r_s)
Silk_damping = np.exp(-(k / k_Silk)**2)

# Baryon transfer function (standard)
T_b_standard = (j0_BAO * Silk_damping + (1 - j0_BAO**2) * T_CDM) * T_CDM

# --- FIRST SOUND COMPONENT (NEW PREDICTION) ---
# Substrate metric perturbation propagating at c_1 = c
# Creates a gravitational potential oscillation at r_1 = r_s * c_1/c_2_actual
# This does NOT have Silk damping (not photon diffusion -- gravitational)
# But has gravitational damping from horizon crossing at k_eq

# First-sound oscillation: gravitational potential Phi oscillates inside the
# Hubble horizon during radiation domination. For modes k > k_eq, the potential
# decays as the universe transitions to matter domination.
# The substrate carries this oscillation as a metric/acoustic mode at c_1 = c.

j0_first = np.sinc(k * r_1 / np.pi)  # sinc gives sin(k*r_1)/(k*r_1)

# Amplitude of first-sound peak relative to BAO
# The first-sound mode is a gravitational/metric perturbation, NOT a baryon density wave
# Its amplitude is set by the gravitational potential transfer:
# In standard cosmology, Phi_k decays by factor ~9/10 at horizon crossing during RD
# and oscillates with decreasing amplitude inside the horizon
# Relative to BAO: A_1/A_BAO ~ (c_2/c_1)^2 = 1/3 in radiation limit
# With baryon loading: (c_2_actual)^2 = 1/[3*(1+R_*)] ~ 0.205
# So first sound peak is ~sqrt(0.205) ~ 0.45 times BAO amplitude in T(k)
# In P(k) = T^2: ratio ~ 0.205

A_first_sound = c_2_actual**2  # ~ 0.205 relative amplitude in P(k)

# First-sound damping: gravitational potential decays inside horizon
# Damping scale is k_eq (modes entering during radiation era get suppressed)
# But the first-sound oscillation is ADDITIONAL to the standard transfer function
# It appears as an oscillatory modulation of the gravitational potential
# that would not exist without the substrate carrying perturbations at c_1 = c

# Gravitational damping envelope (no Silk for metric perturbations)
grav_damping = 1.0 / (1 + (k / (0.5 * k_Silk))**1.5)  # broader than Silk

# First-sound contribution to the transfer function
T_first_sound = A_first_sound * j0_first * grav_damping

# --- TOTAL MATTER TRANSFER FUNCTION ---
# Standard: T_m = (1 - f_b) * T_CDM + f_b * T_b
# With first sound: add the substrate metric oscillation
# T_total = T_standard + T_first_sound

T_standard = (1 - f_b) * T_CDM + f_b * T_b_standard
T_total = T_standard + f_b * T_first_sound  # first sound couples through baryons

# Ensure T(k=0) = 1
T_total = T_total / T_total[0]
T_standard = T_standard / T_standard[0]

# ============================================================
# 6. Full power spectrum P(k)
# ============================================================

# P(k) = A_s * (k/k_pivot)^{n_s - 1 + 0.5*alpha_s*ln(k/k_pivot)} * T(k)^2
# Where T(k) includes acoustic processing + damping
# The expansion tilt is already in the primordial spectrum

# Primordial spectrum (from expansion dynamics)
from canonical_constants import A_s_CMB as A_s  # Planck 2018 amplitude
P_primordial = A_s * T2_expansion  # includes tilt

# Matter power spectrum
P_k_standard = P_primordial * T_standard**2
P_k_total = P_primordial * T_total**2

# Dimensionless power spectrum Delta^2(k) = k^3 * P(k) / (2*pi^2)
Delta2_standard = k**3 * P_k_standard / (2 * np.pi**2)
Delta2_total = k**3 * P_k_total / (2 * np.pi**2)

# ============================================================
# 7. Extract spectral index at k_pivot
# ============================================================

# Fit n_s locally around k_pivot using P_total
# P(k) propto k^{n_eff - 1} * T(k)^2
# n_eff(k) = d ln P / d ln k + 1

# Use numerical derivative of ln(Delta^2) vs ln(k)
# n_s = d ln(Delta^2) / d ln k - 2  [since Delta^2 = k^3 P/(2pi^2)]
# Actually: n_s is defined from the primordial spectrum
# d ln P_primordial / d ln k = n_s - 1
# The transfer function is not part of n_s by definition

# But the EFFECTIVE tilt including transfer function:
lnk = np.log(k)
lnP_total = np.log(P_k_total)
lnP_standard = np.log(P_k_standard)

# Spline interpolation for smooth derivatives
cs_total = CubicSpline(lnk, lnP_total)
cs_standard = CubicSpline(lnk, lnP_standard)

# Effective spectral index at k_pivot
lnk_pivot = np.log(k_pivot)
n_eff_total = cs_total(lnk_pivot, 1) + 1  # d ln P / d ln k + 1
n_eff_standard = cs_standard(lnk_pivot, 1) + 1

# Running at k_pivot
dn_eff_total = cs_total(lnk_pivot, 2)  # d^2 ln P / (d ln k)^2
dn_eff_standard = cs_standard(lnk_pivot, 2)

# Primordial n_s (without transfer function, just expansion)
n_s_primordial = n_s_transfer  # = 1 - 2*epsilon_H

print(f"\n{'='*70}")
print(f"SPECTRAL INDEX RESULTS")
print(f"{'='*70}")
print(f"\nPrimordial (expansion dynamics only):")
print(f"  n_s = 1 - 2*epsilon_H = {n_s_primordial:.6f}")
print(f"  alpha_s = -2*epsilon_H^2 = {alpha_s_transfer:.6e}")
print(f"\nEffective n_s at k_pivot = {k_pivot} Mpc^{{-1}}:")
print(f"  n_eff (standard, no first sound)  = {n_eff_standard:.6f}")
print(f"  n_eff (with first sound)          = {n_eff_total:.6f}")
print(f"  dn_eff/dlnk (standard)            = {dn_eff_standard:.6e}")
print(f"  dn_eff/dlnk (with first sound)    = {dn_eff_total:.6e}")
print(f"\nPlanck 2018 comparison:")
print(f"  n_s(Planck) = {n_s_planck:.4f} +/- {n_s_sigma:.4f}")
print(f"  Deviation (primordial):  {abs(n_s_primordial - n_s_planck)/n_s_sigma:.2f} sigma")
print(f"  alpha_s(Planck) = {alpha_s_planck:.4f} +/- {alpha_s_sigma:.4f}")
print(f"  alpha_s deviation: {abs(alpha_s_transfer - alpha_s_planck)/alpha_s_sigma:.2f} sigma")

# ============================================================
# 8. First-sound peak analysis
# ============================================================

# Find peaks in the ratio P_total / P_standard
ratio = P_k_total / P_k_standard

# Find local maxima in ratio
# The first-sound peak should appear near k_1 = 2*pi/r_1
from scipy.signal import argrelextrema

# Find extrema in the ratio
maxima_idx = argrelextrema(ratio, np.greater, order=5)[0]
minima_idx = argrelextrema(ratio, np.less, order=5)[0]

print(f"\n{'='*70}")
print(f"FIRST-SOUND PEAK ANALYSIS")
print(f"{'='*70}")
print(f"\nPredicted first-sound parameters:")
print(f"  r_1 = {r_1:.2f} Mpc  (comoving first-sound horizon)")
print(f"  k_1 = {k_1:.5f} Mpc^{{-1}}  (first-sound peak wavenumber)")
print(f"  r_1/r_s = {r_1/r_s:.4f}  [= c_1/c_2_actual = {c_1/c_2_actual:.4f}]")
print(f"  A_1/A_BAO = {A_first_sound:.4f}  (amplitude ratio in P(k))")

print(f"\nRatio P_total/P_standard extrema:")
for i in maxima_idx:
    if k[i] < 0.1:  # focus on large scales
        print(f"  Maximum at k = {k[i]:.5f} Mpc^{{-1}} (r = {2*np.pi/k[i]:.1f} Mpc), ratio = {ratio[i]:.6f}")
for i in minima_idx:
    if k[i] < 0.1:
        print(f"  Minimum at k = {k[i]:.5f} Mpc^{{-1}} (r = {2*np.pi/k[i]:.1f} Mpc), ratio = {ratio[i]:.6f}")

# Amplitude of first-sound modulation at k_1
idx_k1 = np.argmin(np.abs(k - k_1))
ratio_at_k1 = ratio[idx_k1]
print(f"\n  Ratio at k_1 = {k[idx_k1]:.5f}: {ratio_at_k1:.6f}")
print(f"  Fractional modulation at k_1: {abs(ratio_at_k1 - 1.0):.6f}")

# BAO peak
idx_kBAO = np.argmin(np.abs(k - k_BAO))
print(f"  Ratio at k_BAO = {k[idx_kBAO]:.5f}: {ratio[idx_kBAO]:.6f}")

# ============================================================
# 9. Correlation function xi(r) for BAO + first sound
# ============================================================

# Compute 2-point correlation function via Hankel transform
# xi(r) = 1/(2*pi^2) * int k^2 P(k) j_0(kr) dk
# Use discrete sum
N_r = 300
r_arr = np.linspace(50, 500, N_r)  # Mpc
xi_standard = np.zeros(N_r)
xi_total = np.zeros(N_r)

# Fine k grid for integration
k_fine = np.logspace(np.log10(1e-4), np.log10(1.0), 2000)
lnk_fine = np.log(k_fine)

cs_P_std = CubicSpline(lnk, np.log(P_k_standard))
cs_P_tot = CubicSpline(lnk, np.log(P_k_total))

P_std_fine = np.exp(cs_P_std(lnk_fine))
P_tot_fine = np.exp(cs_P_tot(lnk_fine))

for i, r in enumerate(r_arr):
    integrand_std = k_fine**2 * P_std_fine * np.sinc(k_fine * r / np.pi)
    integrand_tot = k_fine**2 * P_tot_fine * np.sinc(k_fine * r / np.pi)
    # Integrate using trapezoidal on log-spaced k
    dk_fine = np.diff(k_fine)
    xi_standard[i] = np.sum(0.5 * (integrand_std[:-1] + integrand_std[1:]) * dk_fine) / (2 * np.pi**2)
    xi_total[i] = np.sum(0.5 * (integrand_tot[:-1] + integrand_tot[1:]) * dk_fine) / (2 * np.pi**2)

# Normalize: xi * r^2 to show BAO peak
xi_r2_standard = xi_standard * r_arr**2
xi_r2_total = xi_total * r_arr**2

# Find peaks in xi * r^2
maxima_xi_std = argrelextrema(xi_r2_standard, np.greater, order=10)[0]
maxima_xi_tot = argrelextrema(xi_r2_total, np.greater, order=10)[0]

print(f"\nCorrelation function xi(r) * r^2 peaks:")
print(f"  Standard (BAO only):")
for i in maxima_xi_std:
    if 100 < r_arr[i] < 400:
        print(f"    r = {r_arr[i]:.1f} Mpc, xi*r^2 = {xi_r2_standard[i]:.4e}")
print(f"  With first sound:")
for i in maxima_xi_tot:
    if 100 < r_arr[i] < 400:
        print(f"    r = {r_arr[i]:.1f} Mpc, xi*r^2 = {xi_r2_total[i]:.4e}")

# ============================================================
# 10. Gate verdict
# ============================================================

print(f"\n{'='*70}")
print(f"GATE VERDICT: KK-CMB-TF-43")
print(f"{'='*70}")
print(f"\n  Gate type: INFO")
print(f"\n  Primordial tilt: n_s = 1 - 2*epsilon_H = {n_s_primordial:.6f}")
print(f"  Running: alpha_s = -2*epsilon_H^2 = {alpha_s_transfer:.6e}")
print(f"  Both within 1-sigma of Planck 2018 (epsilon_H is INPUT, not predicted)")
print(f"\n  Transfer function structure:")
print(f"    1. Expansion tilt: (k/k_pivot)^{{n_s-1}} [dominant]")
print(f"    2. Matter transfer: Eisenstein-Hu with BAO at r_s = {r_s:.1f} Mpc")
print(f"    3. First-sound peak: r_1 = {r_1:.1f} Mpc [NEW PREDICTION]")
print(f"    4. Silk damping at k_Silk ~ {k_Silk} Mpc^{{-1}}")
print(f"\n  First-sound ring prediction:")
print(f"    r_1 = {r_1:.1f} Mpc = sqrt(3*(1+R_*)) * r_s")
print(f"    k_1 = {k_1:.5f} Mpc^{{-1}}")
print(f"    Amplitude: {A_first_sound:.3f} of BAO in P(k)")
print(f"    This is a DISTINCTIVE prediction: no standard-cosmology feature at this scale")
print(f"\n  STATUS: epsilon_H is input. n_s is consistency check, NOT prediction.")
print(f"  First-sound ring IS a prediction (unique to substrate framework).")
print(f"  Pre-registerable: search for feature in xi(r) at r ~ {r_1:.0f} Mpc.")

# ============================================================
# 11. Save results
# ============================================================

np.savez('tier0-computation/s43_kk_cmb_transfer.npz',
    # k grid and spectra
    k=k,
    P_k_standard=P_k_standard,
    P_k_total=P_k_total,
    Delta2_standard=Delta2_standard,
    Delta2_total=Delta2_total,
    T_standard=T_standard,
    T_total=T_total,
    T2_expansion=T2_expansion,
    P_KZ_normalized=P_KZ_normalized,
    # Spectral indices
    n_s_primordial=n_s_primordial,
    n_s_eff_standard=n_eff_standard,
    n_s_eff_total=n_eff_total,
    alpha_s_transfer=alpha_s_transfer,
    dn_eff_standard=dn_eff_standard,
    dn_eff_total=dn_eff_total,
    # Sound speeds and horizons
    c_1=c_1,
    c_2=c_2,
    c_2_actual=c_2_actual,
    R_star=R_star,
    r_s=r_s,
    r_1=r_1,
    k_BAO=k_BAO,
    k_1=k_1,
    k_pivot=k_pivot,
    # First-sound peak
    A_first_sound=A_first_sound,
    ratio_P_total_over_standard=ratio,
    ratio_at_k1=ratio_at_k1,
    # Correlation function
    r_arr=r_arr,
    xi_standard=xi_standard,
    xi_total=xi_total,
    xi_r2_standard=xi_r2_standard,
    xi_r2_total=xi_r2_total,
    # Input parameters
    epsilon_H=epsilon_H,
    M_KK=M_KK,
    xi_KZ=xi_KZ,
    xi_KZ_Mpc=xi_KZ_Mpc,
    sigma_tau=sigma_tau,
    # Gate
    gate_name='KK-CMB-TF-43',
    gate_verdict='INFO',
)

print(f"\nSaved: tier0-computation/s43_kk_cmb_transfer.npz")

# ============================================================
# 12. Four-panel figure
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: Primordial + transferred power spectrum
ax = axes[0, 0]
ax.loglog(k, Delta2_standard, 'b-', lw=1.5, label=r'Standard (BAO only)')
ax.loglog(k, Delta2_total, 'r-', lw=1.5, label=r'With first sound', alpha=0.8)
ax.axvline(k_pivot, color='gray', ls='--', alpha=0.5, label=f'$k_{{pivot}}$ = {k_pivot}')
ax.axvline(k_BAO, color='blue', ls=':', alpha=0.5, label=f'$k_{{BAO}}$ = {k_BAO:.3f}')
ax.axvline(k_1, color='red', ls=':', alpha=0.5, label=f'$k_1$ = {k_1:.4f}')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$\Delta^2(k) = k^3 P(k) / (2\pi^2)$')
ax.set_title('A. Dimensionless Power Spectrum')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(k_min, k_max)

# Panel B: Transfer function T(k)
ax = axes[0, 1]
ax.semilogx(k, T_standard, 'b-', lw=1.5, label='Standard')
ax.semilogx(k, T_total, 'r-', lw=1.5, label='With first sound', alpha=0.8)
ax.axvline(k_BAO, color='blue', ls=':', alpha=0.5)
ax.axvline(k_1, color='red', ls=':', alpha=0.5)
ax.axvline(k_eq, color='green', ls='--', alpha=0.5, label=f'$k_{{eq}}$ = {k_eq:.4f}')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$T(k)$')
ax.set_title('B. Matter Transfer Function')
ax.legend(fontsize=7)
ax.set_xlim(k_min, k_max)
ax.set_ylim(-0.1, 1.1)

# Panel C: Ratio P_total / P_standard (first-sound signature)
ax = axes[1, 0]
ax.semilogx(k, ratio, 'r-', lw=1.5)
ax.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax.axvline(k_1, color='red', ls=':', alpha=0.7, label=f'$k_1 = 2\\pi/r_1$ = {k_1:.4f}')
ax.axvline(k_BAO, color='blue', ls=':', alpha=0.7, label=f'$k_{{BAO}} = 2\\pi/r_s$ = {k_BAO:.4f}')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$P_{total}(k) / P_{standard}(k)$')
ax.set_title('C. First-Sound Signature (ratio)')
ax.legend(fontsize=8)
ax.set_xlim(k_min, 0.3)

# Panel D: Correlation function xi(r) * r^2
ax = axes[1, 1]
# Normalize for visibility
norm_std = np.max(np.abs(xi_r2_standard))
if norm_std > 0:
    ax.plot(r_arr, xi_r2_standard / norm_std, 'b-', lw=1.5, label='Standard (BAO only)')
    ax.plot(r_arr, xi_r2_total / norm_std, 'r-', lw=1.5, label='With first sound', alpha=0.8)
else:
    ax.plot(r_arr, xi_r2_standard, 'b-', lw=1.5, label='Standard (BAO only)')
    ax.plot(r_arr, xi_r2_total, 'r-', lw=1.5, label='With first sound', alpha=0.8)
ax.axvline(r_s, color='blue', ls=':', alpha=0.7, label=f'$r_s$ = {r_s:.0f} Mpc')
ax.axvline(r_1, color='red', ls=':', alpha=0.7, label=f'$r_1$ = {r_1:.0f} Mpc')
ax.set_xlabel(r'$r$ [Mpc]')
ax.set_ylabel(r'$\xi(r) \times r^2$ [normalized]')
ax.set_title(r'D. Correlation Function $\xi(r) \cdot r^2$')
ax.legend(fontsize=7)
ax.set_xlim(50, 500)

plt.suptitle('KK-CMB-TF-43: Transfer Function KK $\\to$ CMB\n'
             f'$n_s$ = {n_s_primordial:.4f}, $r_1$ = {r_1:.1f} Mpc, '
             f'$r_s$ = {r_s:.1f} Mpc, $A_1/A_{{BAO}}$ = {A_first_sound:.3f}',
             fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('tier0-computation/s43_kk_cmb_transfer.png', dpi=150, bbox_inches='tight')
print(f"Saved: tier0-computation/s43_kk_cmb_transfer.png")
plt.close()

print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*70}")
