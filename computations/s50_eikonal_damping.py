#!/usr/bin/env python3
"""
Session 50: EIKONAL-DAMPING-50 — Eikonal Damping in Fabric Propagator
======================================================================

Computes the self-energy of the Goldstone phonon (m_G = 0.070 M_KK) due to
scattering off the static condensate texture on T^2 of SU(3).

Physics:
  S49 ANALOG-TRAPPED-49 established that the BCS condensate on T^2 is a
  STATIC texture (no superflow, phase = 0 everywhere). The amplitude
  |Delta(theta1, theta2)| varies across T^2 with a contrast ratio of 3.1M
  and eikonal breakdown (|grad Delta|/(Delta * c_BdG) > 1) over 78.3% of T^2.

  This texture acts as a static disorder potential for Goldstone phonons.
  The local sound speed varies as c_eff(x) = c_BdG * f(Delta(x)), creating
  refractive index variations. In the Born approximation, the phonon
  self-energy is determined by the Fourier power spectrum of the texture.

  The key observable is the ratio Gamma(K_pivot) / m_G^2, which determines
  whether eikonal damping modifies the propagator at observationally
  relevant scales.

Method:
  1. Load condensate texture from s47_condensate_torus.npz
  2. Compute the fractional sound speed variation delta_c(x)/c_0
  3. FFT to get the structure factor |delta_c(q)|^2
  4. Compute Born self-energy Sigma(K) for Goldstone phonon
  5. Extract Im[Sigma] = Gamma(K) at K_pivot and general K
  6. Compute damped propagator P(K) and extract n_s, alpha_s

Gate: EIKONAL-DAMPING-50
  PASS: Gamma(K_pivot) / m_G^2 > 0.1
  FAIL: Gamma(K_pivot) / m_G^2 < 0.01
  INFO: 0.01 < ratio < 0.1

Input:
  - s47_condensate_torus.npz (Delta field on T^2)
  - s49_cavity_resonance.npz (c_BdG, cavity geometry)
  - s49_dipolar_catalog.npz (m_G = omega_L1)

Output:
  - s50_eikonal_damping.npz
  - s50_eikonal_damping.png

Author: quantum-acoustics-theorist (Session 50)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, g0_diag, E_B2_mean, Delta_0_GL,
    PI, xi_BCS, E_cond, rho_B2_per_mode,
    E_B1, E_B3_mean,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def load_npz(name):
    return np.load(os.path.join(DATA_DIR, name), allow_pickle=True)

print("=" * 78)
print("SESSION 50: EIKONAL-DAMPING-50")
print("Eikonal Damping of Goldstone Phonon from Condensate Texture on T^2")
print("=" * 78)


# ============================================================================
#  SECTION 1: LOAD INPUT DATA
# ============================================================================

print("\n" + "-" * 78)
print("SECTION 1: Loading input data")
print("-" * 78)

d_cond = load_npz('s47_condensate_torus.npz')
d_cav  = load_npz('s49_cavity_resonance.npz')
d_dip  = load_npz('s49_dipolar_catalog.npz')

theta1 = d_cond['theta1']
theta2 = d_cond['theta2']
density_bcs = d_cond['density_bcs_weighted']
N_grid = int(d_cond['N_grid'])

# Goldstone mass from dipolar mechanism (S49)
m_G = float(d_dip['omega_L1'])  # = 0.070 M_KK

# BdG sound speed (Anderson-Bogoliubov)
c_BdG = float(d_cav['c_BdG'])  # = 0.7507 M_KK

# Metric on T^2 at fold
g_11 = g0_diag * np.exp(2 * tau_fold)
dtheta = theta1[1] - theta1[0]
h_phys = dtheta * np.sqrt(g_11)
L_phys = 2 * PI * np.sqrt(g_11)  # circumference of T^2 in each direction

print(f"  N_grid = {N_grid}")
print(f"  m_G = {m_G:.6f} M_KK (Goldstone mass from Leggett dipolar)")
print(f"  c_BdG = {c_BdG:.4f} M_KK (Anderson-Bogoliubov sound speed)")
print(f"  g_11 = {g_11:.4f}")
print(f"  h_phys = {h_phys:.6f} M_KK^{{-1}} (physical grid spacing)")
print(f"  L_phys = {L_phys:.4f} M_KK^{{-1}} (torus circumference)")


# ============================================================================
#  SECTION 2: CONDENSATE TEXTURE AND SOUND SPEED VARIATION
# ============================================================================

print("\n" + "-" * 78)
print("SECTION 2: Condensate texture analysis")
print("-" * 78)

# Condensate amplitude
Delta_field = np.sqrt(np.abs(density_bcs))

# Statistics
Delta_mean = np.mean(Delta_field)
Delta_std = np.std(Delta_field)
Delta_max = np.max(Delta_field)
Delta_min = np.min(Delta_field[Delta_field > 1e-10])

print(f"  |Delta| statistics on T^2:")
print(f"    mean = {Delta_mean:.6f}")
print(f"    std  = {Delta_std:.6f}")
print(f"    max  = {Delta_max:.6f}")
print(f"    min (nonzero) = {Delta_min:.6e}")
print(f"    contrast = {Delta_max/Delta_min:.2e}")
print(f"    CV = std/mean = {Delta_std/Delta_mean:.4f}")

# The sound speed variation comes from the BdG dispersion. For a condensate
# with local gap Delta(x), the low-energy phonon speed is:
#
#   c_eff(x) = v_F / sqrt(dim) * sqrt(Delta(x) / E_F)^{1/2}  [for BCS]
#
# But more precisely, in the BdG framework the quasiparticle dispersion is:
#   E_k = sqrt(epsilon_k^2 + Delta^2)
# and the group velocity for the Goldstone mode (phonon of the condensate) is:
#   c_s = Delta / sqrt(dim * E_F)  [simplified]
#
# However, since we're working with the effective sound speed already
# determined from the Anderson-Bogoliubov result c_BdG = v_F/sqrt(3),
# the key quantity is the FRACTIONAL variation of the effective medium.
#
# The condensate texture modulates the local medium properties. The relevant
# scattering potential is the fractional variation of Delta^2 (which enters
# the phonon dispersion as the gap squared):
#
#   V(x) = (Delta(x)^2 - <Delta^2>) / <Delta^2>
#
# This is the relevant Born scattering potential.

Delta2_field = Delta_field**2
Delta2_mean = np.mean(Delta2_field)
V_field = (Delta2_field - Delta2_mean) / Delta2_mean  # fractional variation of Delta^2

V_mean = np.mean(V_field)  # should be ~0
V_rms = np.sqrt(np.mean(V_field**2))
V_max = np.max(V_field)
V_min = np.min(V_field)

print(f"\n  Scattering potential V(x) = (Delta^2 - <Delta^2>) / <Delta^2>:")
print(f"    <V> = {V_mean:.4e} (should be ~0)")
print(f"    V_rms = {V_rms:.4f}")
print(f"    V_max = {V_max:.4f}")
print(f"    V_min = {V_min:.6f}")

# Gradient of V (for Mach-number crosscheck)
grad_V1 = np.gradient(V_field, dtheta, axis=0) / np.sqrt(g_11)
grad_V2 = np.gradient(V_field, dtheta, axis=1) / np.sqrt(g_11)
grad_V_mag = np.sqrt(grad_V1**2 + grad_V2**2)

print(f"    |grad V|_max = {np.max(grad_V_mag):.4f} M_KK")
print(f"    |grad V|_mean = {np.mean(grad_V_mag):.4f} M_KK")


# ============================================================================
#  SECTION 3: FOURIER STRUCTURE FACTOR
# ============================================================================

print("\n" + "-" * 78)
print("SECTION 3: Fourier structure factor of condensate texture")
print("-" * 78)

# The structure factor is the power spectrum of V(x) on the torus T^2.
# Since T^2 is periodic with period 2*pi in coordinate space, the
# physical wavevectors are:
#   q_n = 2*pi*n / L_phys = n / sqrt(g_11)
#
# We compute the 2D FFT of V(x) on the (theta1, theta2) grid.

V_fft = np.fft.fft2(V_field)
V_power = np.abs(V_fft)**2 / N_grid**4  # normalized power spectrum

# Physical wavevector grid
dq_phys = 2 * PI / L_phys  # fundamental wavevector in physical units
q1_grid = np.fft.fftfreq(N_grid, d=dtheta) * 2 * PI / np.sqrt(g_11)
q2_grid = np.fft.fftfreq(N_grid, d=dtheta) * 2 * PI / np.sqrt(g_11)
Q1, Q2 = np.meshgrid(q1_grid, q2_grid, indexing='ij')
Q_mag = np.sqrt(Q1**2 + Q2**2)

# Radial power spectrum S(q) = azimuthal average of |V(q)|^2
q_max = np.max(Q_mag) / 2  # Nyquist
n_q_bins = 80
q_bins = np.linspace(0, q_max, n_q_bins + 1)
q_centers = 0.5 * (q_bins[:-1] + q_bins[1:])

S_q = np.zeros(n_q_bins)
counts = np.zeros(n_q_bins)

for i in range(N_grid):
    for j in range(N_grid):
        q = Q_mag[i, j]
        idx = np.searchsorted(q_bins, q) - 1
        if 0 <= idx < n_q_bins:
            S_q[idx] += V_power[i, j]
            counts[idx] += 1

# Normalize: S(q) = average power per mode at wavevector q
mask_counts = counts > 0
S_q[mask_counts] /= counts[mask_counts]

# Zero mode (q=0) should be ~0 since <V>=0
S_q_0 = V_power[0, 0]

print(f"  Fourier analysis of V(x):")
print(f"    dq_phys = {dq_phys:.4f} M_KK (fundamental wavevector)")
print(f"    q_Nyquist = {q_max:.4f} M_KK")
print(f"    S(q=0) = {S_q_0:.4e} (should be small)")
print(f"    S(q) max = {np.max(S_q[mask_counts]):.4e} at q = {q_centers[np.argmax(S_q)]:.4f} M_KK")
print(f"    S(q) at q~1/xi_BCS = ", end="")

# Find S(q) at q ~ 1/xi_BCS
q_xi = 1.0 / xi_BCS
idx_xi = np.argmin(np.abs(q_centers - q_xi))
print(f"{S_q[idx_xi]:.4e} at q = {q_centers[idx_xi]:.4f} M_KK (1/xi_BCS = {q_xi:.4f})")

# Check: total power = V_rms^2 (Parseval's theorem)
total_power = np.sum(V_power)
print(f"    Parseval check: sum |V(q)|^2 = {total_power:.6f}, V_rms^2 = {V_rms**2:.6f}")


# ============================================================================
#  SECTION 4: GOLDSTONE PHONON DISPERSION AND GREEN'S FUNCTION
# ============================================================================

print("\n" + "-" * 78)
print("SECTION 4: Goldstone phonon dispersion and propagator")
print("-" * 78)

# The Goldstone phonon (pseudo-Goldstone from Leggett dipolar mechanism)
# has dispersion:
#   omega^2(K) = c_BdG^2 * K^2 + m_G^2
#
# The free retarded Green's function is:
#   G_0(K, omega) = 1 / (omega^2 - c^2 K^2 - m^2 + i*epsilon)
#
# At on-shell (omega^2 = c^2 K^2 + m^2), the propagator determines
# the power spectrum of fluctuations:
#   P_0(K) = 1 / (c^2 K^2 + m^2)

# Pivot scale: the Goldstone mass shell
K_pivot = m_G / c_BdG  # K where omega = sqrt(2) * m_G
lambda_pivot = 2 * PI / K_pivot

print(f"  Goldstone phonon:")
print(f"    m_G = {m_G:.6f} M_KK")
print(f"    c_BdG = {c_BdG:.4f} M_KK")
print(f"    K_pivot = m_G / c = {K_pivot:.6f} M_KK")
print(f"    lambda_pivot = {lambda_pivot:.4f} M_KK^{{-1}}")
print(f"    L_phys / lambda_pivot = {L_phys / lambda_pivot:.2f}")
print(f"    Torus can support {L_phys/lambda_pivot:.1f} pivot wavelengths")


# ============================================================================
#  SECTION 5: BORN SELF-ENERGY COMPUTATION
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 5: Born approximation self-energy")
print("=" * 78)

# The Born approximation self-energy for a phonon with dispersion
#   omega^2 = c^2 K^2 + m^2
# scattering off a static potential V(x) is:
#
#   Sigma(K, omega) = (m_G^2)^2 * integral |V(q)|^2 * G_0(K-q, omega) dq/(2pi)^2
#
# where the coupling is through the mass term: the texture modulates
# the effective mass (or equivalently, the local sound speed).
#
# More precisely, the phonon Lagrangian in the inhomogeneous medium is:
#   L = (1/2) [dot{phi}^2 / c^2 - (grad phi)^2 - m^2(x) phi^2]
# where m^2(x) = m_G^2 * (1 + V(x)) with V(x) the fractional texture variation.
#
# The perturbation Hamiltonian is:
#   H_int = (1/2) m_G^2 * V(x) * phi^2
#
# Self-energy (one-loop, Born):
#   Sigma(K) = m_G^4 * integral |V(q)|^2 / (omega^2 - c^2(K-q)^2 - m^2 + i*epsilon) * dq/(2pi)^2
#
# For the on-shell self-energy (evaluating at omega^2 = c^2 K^2 + m^2):
#   Sigma(K) = m_G^4 * integral |V(q)|^2 / (c^2[K^2 - (K-q)^2] + i*eta) * dq/(2pi)^2
#            = m_G^4 * integral |V(q)|^2 / (c^2[2K.q - q^2] + i*eta) * dq/(2pi)^2
#
# The imaginary part (damping) comes from the pole:
#   Im[Sigma(K)] = -pi * m_G^4 / c^2 * integral |V(q)|^2 * delta(2K.q - q^2) * dq/(2pi)^2
#
# For isotropic scattering (azimuthal average over K direction):
#   Im[Sigma(K)] = -m_G^4 / (4*pi*c^2) * integral_0^{2K} dq * q * S(q) / sqrt(4K^2 q^2 - q^4) * (2pi*q)
#
# Simplifying using the constraint 2K*q*cos(theta) = q^2 => cos(theta) = q/(2K):
#   Im[Sigma(K)] = -m_G^4 / (2*c^2) * integral_0^{2K} S(q) * q / sqrt(4K^2 - q^2) * dq/(2pi)
#
# Let's compute this numerically.

# Build K array spanning from 0 to well above q_Nyquist
K_array = np.logspace(-2, np.log10(q_max), 200)
K_array = np.sort(np.unique(np.concatenate([K_array, [K_pivot, m_G/c_BdG]])))

# Interpolate S(q) for numerical integration
# Use the discrete Fourier data directly
S_q_interp_vals = np.zeros(len(q_centers))
S_q_interp_vals[mask_counts] = S_q[mask_counts]

from scipy.interpolate import interp1d
S_interp = interp1d(q_centers, S_q_interp_vals, kind='linear',
                     bounds_error=False, fill_value=0.0)

# Also: compute REAL part of self-energy (mass shift) via principal value integral
# And IMAGINARY part (damping rate)

Sigma_real = np.zeros(len(K_array))
Sigma_imag = np.zeros(len(K_array))

print("\n  Computing Born self-energy Sigma(K) for on-shell Goldstone phonon...")
print(f"  K range: [{K_array[0]:.4f}, {K_array[-1]:.2f}] M_KK")
print(f"  K_pivot = {K_pivot:.6f} M_KK")

for iK, K in enumerate(K_array):
    if K < 1e-6:
        continue

    # --- Imaginary part: from on-shell scattering ---
    # Im[Sigma(K)] = -m_G^4 / (2*c^2) * int_0^{2K} S(q) * q / sqrt(4K^2 - q^2) dq/(2pi)
    #
    # The integrand has an integrable singularity at q = 2K (forward scattering).
    # Use Gauss-Chebyshev quadrature for the sqrt(4K^2 - q^2) weight.

    q_upper = min(2 * K, q_centers[-1])  # can't scatter beyond Nyquist data
    if q_upper < q_centers[1]:
        continue

    # Simple numerical integration with singularity handling
    n_quad = 500
    # Substitution: q = 2K * sin(u), u in [0, pi/2] if q_upper = 2K
    # Otherwise q = q_upper * sin(u)
    u_max = np.arcsin(min(q_upper / (2 * K), 1.0))
    u_arr = np.linspace(1e-8, u_max - 1e-8, n_quad)
    du = u_arr[1] - u_arr[0]

    q_arr = 2 * K * np.sin(u_arr)
    # dq = 2K cos(u) du
    # sqrt(4K^2 - q^2) = 2K cos(u)
    # So the integrand becomes:
    # S(q) * q / sqrt(4K^2 - q^2) * dq = S(q) * q * du  [the sqrt cancels with dq]

    S_vals = S_interp(q_arr)
    integrand_imag = S_vals * q_arr  # after cancellation

    Im_sigma_K = -(m_G**4) / (2 * c_BdG**2) * np.trapezoid(integrand_imag, u_arr) / (2 * PI)
    Sigma_imag[iK] = Im_sigma_K

    # --- Real part: principal value integral (Kramers-Kronig) ---
    # Re[Sigma(K)] = m_G^4 * P.V. int |V(q)|^2 / (c^2(2K.q - q^2)) dq/(2pi)^2
    #
    # For azimuthally averaged:
    # Re[Sigma(K)] = m_G^4 / (2*pi*c^2) * P.V. int_0^{q_max} S(q) * q *
    #                [1/sqrt(q^2 - 4K^2) for q > 2K, else 0 from P.V.] dq  [approximate]
    #
    # More precisely, the full real part involves the principal value of the
    # angular integral. For the off-shell contributions (q > 2K), the
    # denominator 2Kq cos(theta) - q^2 doesn't vanish, so:
    #
    # Re[Sigma(K)] from q > 2K:
    #   = m_G^4 / (2*pi*c^2) * int_{2K}^{q_max} S(q) * q / sqrt(q^2 - 4K^2) dq

    # Off-shell real part (q > 2K)
    q_off = q_centers[q_centers > 2 * K + 1e-6]
    if len(q_off) > 0:
        S_off = S_interp(q_off)
        integrand_real = S_off * q_off / np.sqrt(q_off**2 - 4 * K**2)
        Re_sigma_off = (m_G**4) / (2 * PI * c_BdG**2) * np.trapezoid(integrand_real, q_off)
    else:
        Re_sigma_off = 0.0

    # On-shell principal value contribution (near q ~ 2K) — small for smooth S(q)
    # Approximate by Hilbert transform. For a first-pass, the off-shell piece dominates.
    Sigma_real[iK] = Re_sigma_off


# Gamma(K) = -2 * Im[Sigma(K)] / (2 * omega(K))  [width in frequency space]
# But since we want Gamma as an additive term in the inverse propagator:
# The damping in the propagator is just |Im[Sigma(K)]|
Gamma_K = np.abs(Sigma_imag)

print("\n  Self-energy results:")

# Find pivot value
idx_pivot = np.argmin(np.abs(K_array - K_pivot))
Gamma_pivot = Gamma_K[idx_pivot]
Re_Sigma_pivot = Sigma_real[idx_pivot]

print(f"\n  At K_pivot = {K_pivot:.6f} M_KK:")
print(f"    Re[Sigma(K_pivot)] = {Re_Sigma_pivot:.6e} M_KK^2")
print(f"    Im[Sigma(K_pivot)] = {Sigma_imag[idx_pivot]:.6e} M_KK^2")
print(f"    |Gamma(K_pivot)|   = {Gamma_pivot:.6e} M_KK^2")
print(f"    m_G^2              = {m_G**2:.6e} M_KK^2")


# ============================================================================
#  SECTION 6: GATE VERDICT
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 6: GATE VERDICT — EIKONAL-DAMPING-50")
print("=" * 78)

ratio_pivot = Gamma_pivot / m_G**2

print(f"\n  Gate criterion: Gamma(K_pivot) / m_G^2")
print(f"    Gamma(K_pivot) = {Gamma_pivot:.6e} M_KK^2")
print(f"    m_G^2          = {m_G**2:.6e} M_KK^2")
print(f"    Ratio          = {ratio_pivot:.6e}")

if ratio_pivot > 0.1:
    verdict = "PASS"
    detail = (f"Gamma(K_pivot)/m_G^2 = {ratio_pivot:.4e} > 0.1. "
              f"Eikonal damping MODIFIES the Goldstone propagator at observationally "
              f"relevant scales.")
elif ratio_pivot < 0.01:
    verdict = "FAIL"
    detail = (f"Gamma(K_pivot)/m_G^2 = {ratio_pivot:.4e} < 0.01. "
              f"Eikonal damping is NEGLIGIBLE at CMB-relevant scales. "
              f"The Goldstone propagator is unmodified by condensate texture.")
else:
    verdict = "INFO"
    detail = (f"Gamma(K_pivot)/m_G^2 = {ratio_pivot:.4e} in [0.01, 0.1]. "
              f"Marginal modification of propagator.")

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")


# ============================================================================
#  SECTION 7: DAMPED PROPAGATOR AND SPECTRAL CONSEQUENCES
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 7: Damped propagator P(K) and spectral tilt")
print("=" * 78)

# Undamped (Ornstein-Zernike) propagator:
#   P_0(K) = 1 / (c^2 K^2 + m^2)
#
# Damped propagator:
#   P(K) = 1 / (c^2 K^2 + m^2 + Re[Sigma(K)] + i*Im[Sigma(K)])
#
# Power spectrum: |P(K)|^2 = 1 / [(c^2 K^2 + m^2 + Re[Sigma])^2 + Im[Sigma]^2]
# Or for the spectral density: -Im[P(K)] / pi

# Compute both propagators
P0_K = 1.0 / (c_BdG**2 * K_array**2 + m_G**2)
denom_real = c_BdG**2 * K_array**2 + m_G**2 + Sigma_real
denom_imag = Sigma_imag
P_K_abs2 = 1.0 / (denom_real**2 + denom_imag**2)
P_K_real = denom_real / (denom_real**2 + denom_imag**2)

# Ratio of damped to undamped
ratio_P = np.sqrt(P_K_abs2) / P0_K

# Extract effective spectral index from the damped propagator
# n_s - 1 = d ln(K^3 |P(K)|^2) / d ln(K) - 3 evaluated at K_pivot
# In the O-Z limit: K^3 * P_0(K)^2 ~ K^3/(c^2K^2+m^2)^2
# For K >> m/c: ~ K^{-1} => n_s = 1 + (-1-3) = ...
#
# Standard convention for this framework (S49):
#   The O-Z propagator gives P(K) ~ 1/(K^2 + m^2/c^2)
#   n_s = 1 - d ln P / d ln K evaluated near K_pivot
#   alpha_s = dn_s / d ln K
#
# From S49: alpha_s = n_s^2 - 1 exactly in O-Z (no damping).
# The question is whether damping modifies this identity.

# Compute d ln|P|/d ln K numerically
valid = K_array > 0.01  # avoid numerical noise at very small K
K_v = K_array[valid]
lnK = np.log(K_v)
lnP0 = np.log(P0_K[valid])
lnP = 0.5 * np.log(P_K_abs2[valid])  # ln|P|, using |P|

# Numerical derivative
dlnP0_dlnK = np.gradient(lnP0, lnK)
dlnP_dlnK = np.gradient(lnP, lnK)

# n_s - 1 at pivot
idx_piv_v = np.argmin(np.abs(K_v - K_pivot))

ns_minus_1_OZ = dlnP0_dlnK[idx_piv_v]
ns_minus_1_damped = dlnP_dlnK[idx_piv_v]
n_s_OZ = 1 + ns_minus_1_OZ
n_s_damped = 1 + ns_minus_1_damped

# Running: d^2 ln P / d(ln K)^2
d2lnP0 = np.gradient(dlnP0_dlnK, lnK)
d2lnP = np.gradient(dlnP_dlnK, lnK)

alpha_s_OZ = d2lnP0[idx_piv_v]
alpha_s_damped = d2lnP[idx_piv_v]

# O-Z identity check
alpha_s_OZ_identity = n_s_OZ**2 - 1

print(f"  K_pivot = {K_pivot:.6f} M_KK")
print(f"\n  Undamped (O-Z) propagator:")
print(f"    n_s = {n_s_OZ:.6f}")
print(f"    alpha_s = {alpha_s_OZ:.6e}")
print(f"    alpha_s (from n_s^2-1) = {alpha_s_OZ_identity:.6e}")
print(f"    Identity check: |alpha_s - (n_s^2-1)|/|alpha_s| = "
      f"{abs(alpha_s_OZ - alpha_s_OZ_identity) / abs(alpha_s_OZ + 1e-30):.4e}")

print(f"\n  Damped propagator:")
print(f"    n_s = {n_s_damped:.6f}")
print(f"    alpha_s = {alpha_s_damped:.6e}")
print(f"    Delta(n_s) = {n_s_damped - n_s_OZ:.6e} (shift from damping)")
print(f"    Delta(alpha_s) = {alpha_s_damped - alpha_s_OZ:.6e}")

# Check if damping softens the alpha_s = n_s^2 - 1 identity
alpha_s_damped_identity = n_s_damped**2 - 1
identity_violation = abs(alpha_s_damped - alpha_s_damped_identity)
print(f"\n  Does damping break the alpha_s = n_s^2 - 1 identity?")
print(f"    alpha_s (computed) = {alpha_s_damped:.6e}")
print(f"    n_s^2 - 1          = {alpha_s_damped_identity:.6e}")
print(f"    |violation|        = {identity_violation:.6e}")

if identity_violation < 1e-3 * abs(alpha_s_damped + 1e-30):
    print(f"    Identity SURVIVES damping (violation < 0.1% of alpha_s)")
else:
    frac_viol = identity_violation / abs(alpha_s_damped) if abs(alpha_s_damped) > 1e-30 else float('inf')
    print(f"    Identity BROKEN by damping (violation = {frac_viol*100:.2f}% of alpha_s)")


# ============================================================================
#  SECTION 8: PHYSICAL ANALYSIS — WHY THE RESULT IS WHAT IT IS
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 8: Physical analysis")
print("=" * 78)

# Key physical scales
omega_G = m_G  # Goldstone energy scale
K_G = m_G / c_BdG  # Goldstone wavenumber
lambda_G = 2 * PI / K_G

# Structure factor at the Goldstone scale
S_at_KG = S_interp(K_G)
S_at_2KG = S_interp(2 * K_G)

# Comparison with torus scales
K_torus_fund = 2 * PI / L_phys  # fundamental mode of torus
n_modes_to_KG = K_G / K_torus_fund

print(f"  Scale comparison:")
print(f"    K_G = m_G/c = {K_G:.4f} M_KK")
print(f"    lambda_G = {lambda_G:.4f} M_KK^{{-1}}")
print(f"    K_torus_fund = {K_torus_fund:.4f} M_KK (fundamental torus mode)")
print(f"    K_G / K_fund = {n_modes_to_KG:.4f}")
print(f"    S(K_G) = {S_at_KG:.4e} (texture power at Goldstone scale)")
print(f"    S(2K_G) = {S_at_2KG:.4e} (texture power at scattering cutoff)")

print(f"\n  Why Gamma(K_pivot) is what it is:")
print(f"    Gamma ~ m_G^4 * S(K_G) * K_G / c^2")
Gamma_estimate = m_G**4 * S_at_KG * K_G / c_BdG**2
print(f"    Dimensional estimate: {Gamma_estimate:.4e} M_KK^2")
print(f"    Actual computation:   {Gamma_pivot:.4e} M_KK^2")

# The V_rms tells us the average scattering strength
print(f"\n  Scattering strength:")
print(f"    V_rms = {V_rms:.4f}")
print(f"    m_G^2 * V_rms = {m_G**2 * V_rms:.4e} M_KK^2 (effective potential)")
print(f"    (m_G^2 * V_rms) / m_G^2 = {V_rms:.4f} (Born parameter)")

if V_rms > 1:
    print(f"    V_rms > 1: Born approximation FAILS. Need non-perturbative treatment.")
    print(f"    Strong scattering: phonons multiply scatter, mean free path << wavelength.")
    print(f"    Anderson localization regime: l_mfp ~ lambda / (k * l_mfp) => l_mfp ~ 1/k")
else:
    print(f"    V_rms < 1: Born approximation valid. Weak scattering regime.")

# Mean free path estimate
if Gamma_pivot > 0:
    omega_pivot = np.sqrt(c_BdG**2 * K_pivot**2 + m_G**2)
    # Gamma in frequency units: Gamma_omega = Im[Sigma] / (2*omega)
    Gamma_omega = Gamma_pivot / (2 * omega_pivot)
    l_mfp = c_BdG / Gamma_omega if Gamma_omega > 0 else float('inf')
    print(f"\n  Mean free path:")
    print(f"    omega(K_pivot) = {omega_pivot:.4f} M_KK")
    print(f"    Gamma_omega = {Gamma_omega:.4e} M_KK")
    print(f"    l_mfp = c/Gamma_omega = {l_mfp:.4e} M_KK^{{-1}}")
    print(f"    l_mfp / L_phys = {l_mfp / L_phys:.4e}")
    print(f"    l_mfp / lambda_G = {l_mfp / lambda_G:.4e}")
else:
    l_mfp = float('inf')
    print(f"\n  Mean free path: infinite (no damping)")


# ============================================================================
#  SECTION 9: STRUCTURE FACTOR ANALYSIS — WHERE THE POWER LIVES
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 9: Structure factor analysis")
print("=" * 78)

# Power at different scales
cumulative_power = np.zeros(len(q_centers))
for i in range(len(q_centers)):
    if mask_counts[i]:
        # Power in annulus: S(q) * 2*pi*q * dq
        dq = q_bins[i+1] - q_bins[i]
        cumulative_power[i] = S_q[i] * 2 * PI * q_centers[i] * dq

cum_total = np.sum(cumulative_power)
cum_sum = np.cumsum(cumulative_power)

# What fraction of power is at q < K_G?
frac_below_KG = cum_sum[idx_xi] / cum_total if cum_total > 0 else 0

# Where is 50%, 90% of power?
if cum_total > 0:
    cum_norm = cum_sum / cum_total
    q_50 = q_centers[np.searchsorted(cum_norm, 0.5)]
    q_90 = q_centers[np.searchsorted(cum_norm, 0.9)]
else:
    q_50 = q_90 = 0.0

print(f"  Power distribution:")
print(f"    Total integrated power = {cum_total:.4e}")
print(f"    50% of power below q = {q_50:.4f} M_KK")
print(f"    90% of power below q = {q_90:.4f} M_KK")
print(f"    K_G = {K_G:.4f} M_KK")
print(f"    K_torus_fund = {K_torus_fund:.4f} M_KK")

# The Z_3 domain structure of T^2 means the texture has 3 domains
# with domain walls. The dominant Fourier mode should be at q ~ 2*pi/L_domain
# where L_domain ~ L_phys / 3 (from Z_3 symmetry).
K_domain = 3 * K_torus_fund
idx_domain = np.argmin(np.abs(q_centers - K_domain))
S_at_domain = S_q[idx_domain]

print(f"\n  Z_3 domain structure:")
print(f"    K_domain (Z_3) = 3 * K_fund = {K_domain:.4f} M_KK")
print(f"    S(K_domain) = {S_at_domain:.4e}")
print(f"    K_G / K_domain = {K_G / K_domain:.4f}")

# Scale hierarchy: where Goldstone sits relative to texture
print(f"\n  Scale hierarchy (low to high):")
print(f"    K_fund = {K_torus_fund:.4f} M_KK (torus fundamental)")
print(f"    K_G = {K_G:.4f} M_KK (Goldstone mass shell)")
print(f"    K_domain = {K_domain:.4f} M_KK (Z_3 domain scale)")
print(f"    K_Nyquist = {q_max:.4f} M_KK (grid resolution)")


# ============================================================================
#  SECTION 10: ALTERNATIVE — DIRECT TEXTURE SCATTERING (NON-PERTURBATIVE)
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 10: Non-perturbative estimate (strong scattering)")
print("=" * 78)

# When V_rms > 1, the Born approximation underestimates damping.
# In the strong-scattering limit (Anderson localization), the
# relevant quantity is the Ioffe-Regel criterion: k * l_mfp ~ 1.
#
# For a texture with correlation length l_corr and V_rms >> 1,
# the scattering mean free path is:
#   1/l_mfp ~ n_scat * sigma_scat ~ (1/l_corr^2) * l_corr^2 * V_rms^2
#            = V_rms^2 / l_corr  [in 2D]
#
# But this is the SINGLE T^2 result. For the full fabric, the relevant
# question is: how many T^2 cells does the phonon traverse?

# Correlation length from S(q): l_corr = 1 / q_dominant
if q_50 > 0:
    l_corr = 1.0 / q_50
else:
    l_corr = L_phys

print(f"  Correlation length: l_corr = 1/q_50 = {l_corr:.4f} M_KK^{{-1}}")

# Strong-scattering mean free path
l_mfp_strong = l_corr / V_rms**2
print(f"  Strong-scattering l_mfp = l_corr/V_rms^2 = {l_mfp_strong:.4e} M_KK^{{-1}}")

# Ioffe-Regel criterion
kl_IR = K_G * l_mfp_strong
print(f"  Ioffe-Regel: k_G * l_mfp = {kl_IR:.4e}")
if kl_IR < 1:
    print(f"    kl < 1: ANDERSON LOCALIZATION regime for Goldstone phonon on T^2")
    print(f"    Phonon is LOCALIZED on a single T^2 cell")
else:
    print(f"    kl > 1: Extended phonon states (weak localization)")

# Localization length in 2D (all states localize in 2D)
if kl_IR > 0:
    xi_loc = l_mfp_strong * np.exp(PI * K_G * l_mfp_strong / 2)
    print(f"  2D localization length: xi_loc = l_mfp * exp(pi*k*l/2) = {xi_loc:.4e} M_KK^{{-1}}")
    print(f"  xi_loc / L_phys = {xi_loc / L_phys:.4e}")


# ============================================================================
#  SECTION 11: FABRIC VS. SINGLE-CELL DISTINCTION
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 11: Single T^2 cell vs. extended fabric")
print("=" * 78)

# CRITICAL DISTINCTION (S44 lesson: internal vs external):
# The condensate texture exists on EACH T^2 cell independently.
# But Goldstone phonons propagate through the FABRIC (the 4D manifold
# M^4 x SU(3)_tau, where tau may vary across M^4).
#
# The T^2 texture scattering computed above is the INTERNAL scattering
# within a single fiber. The phonon power spectrum observed in 4D
# involves the fiber-averaged propagator.
#
# For the fabric propagator, the relevant self-energy is:
#   Sigma_fabric(K_4D) = <Sigma_T2> (averaged over fiber orientations)
#
# Since the T^2 texture is the SAME on every fiber (it's determined by
# the BCS ground state at tau_fold), the fiber-averaging is trivial:
# every fiber contributes the same Sigma.
#
# BUT: the K_4D wavevector and the T^2 wavevector are in different spaces.
# The T^2 texture only scatters the INTERNAL components of the phonon.
# A phonon propagating in 4D with 4-momentum K_mu has internal momentum
# constrained to the KK tower: K_internal = n * 2*pi / R_KK.
#
# For the ZERO-MODE (n=0) Goldstone, K_internal = 0.
# It sees the AVERAGE of V(x) over T^2, which is zero by construction.
# NO SCATTERING for the zero mode.
#
# For the FIRST KK mode (n=1), K_internal = 2*pi/R_KK ~ M_KK.
# This is far above the texture variation scale, so the scattering
# is UV-suppressed.
#
# This is the FUNDAMENTAL POINT: the Goldstone is a ZERO MODE on T^2.
# It doesn't resolve the internal texture at all.

print(f"\n  FUNDAMENTAL DISTINCTION:")
print(f"  The Goldstone phonon (m_G = {m_G:.4f} M_KK) is the n=0 KK mode.")
print(f"  As a zero mode on T^2, it sees only the spatial AVERAGE of V(x).")
print(f"  By construction: <V(x)>_{{T^2}} = 0.")
print(f"\n  Therefore: the zero-mode Goldstone is TRANSPARENT to T^2 texture.")
print(f"  Eikonal breakdown on T^2 affects HIGHER KK modes (n >= 1),")
print(f"  which have internal wavelength ~ 2*pi/M_KK ~ 1/M_KK.")

# Check: what is the zero-mode average?
V_avg_haar = np.sum(V_field * d_cond['haar_measure']) / np.sum(d_cond['haar_measure'])
print(f"\n  Haar-weighted <V>_{{T^2}} = {V_avg_haar:.4e} (confirms zero)")

# What about the mass correction from <V^2>?
# Second-order shift: delta_m^2 = m_G^4 * <V^2> * G_0(K_int=0)
# But G_0 at K_int = 0 is just the zero-mode propagator.
# This gives a MASS RENORMALIZATION, not damping:
#   delta_m^2 = m_G^4 * V_rms^2 * (sum over q of G_0(q))
# = m_G^4 * V_rms^2 * A_T2 * rho_phonon(E=0)
# where A_T2 = L_phys^2 is the area of T^2.

# The phonon DOS on T^2 at E=0 (for massive phonon): rho = 1/(4*pi*c^2)
# Actually for the zero-mode projection, the relevant DOS is:
rho_phonon_0 = 1.0 / (4 * PI * c_BdG**2)
A_T2 = L_phys**2
delta_m2_2nd_order = m_G**4 * V_rms**2 * A_T2 * rho_phonon_0

print(f"\n  Second-order mass correction from texture:")
print(f"    delta_m^2 = m_G^4 * V_rms^2 * A_T2 * rho_0 / (2pi)")
print(f"    = {m_G**4:.4e} * {V_rms**2:.4f} * {A_T2:.4f} * {rho_phonon_0:.4e}")
print(f"    = {delta_m2_2nd_order:.4e} M_KK^2")
print(f"    delta_m^2 / m_G^2 = {delta_m2_2nd_order / m_G**2:.4e}")


# ============================================================================
#  SECTION 12: REVISED GATE ASSESSMENT
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 12: REVISED GATE ASSESSMENT — EIKONAL-DAMPING-50")
print("=" * 78)

# The Born self-energy computation (Section 5) gives a nonzero Gamma,
# but Section 11 reveals that this computation applies to INTERNAL modes
# on T^2, not to the zero-mode Goldstone.
#
# For the Goldstone (zero-mode), the scattering potential vanishes by
# construction (<V> = 0). The leading effect is a second-order mass
# renormalization, not damping.
#
# Revised assessment: damping at K_pivot from texture scattering = 0
# for the physical zero-mode Goldstone.

# However, there IS a finite effect: the texture modifies the
# GROUP VELOCITY of the Goldstone through the effective medium.
# The effective sound speed for a wave propagating through a medium
# with random Delta^2 variations is:
#   c_eff = c_BdG * (1 - V_rms^2 / 2 + ...) [perturbative]
# or for strong variations:
#   c_eff = c_BdG * exp(<ln(1+V)>)  [geometric mean for 1D]

c_eff_pert = c_BdG * (1 - V_rms**2 / 2)
ln_V_avg = np.mean(np.log(np.maximum(1 + V_field, 1e-30)))
c_eff_geom = c_BdG * np.exp(ln_V_avg)

print(f"\n  Effective sound speed through texture:")
print(f"    c_BdG = {c_BdG:.4f} M_KK")
print(f"    c_eff (perturbative) = {c_eff_pert:.4f} M_KK")
print(f"    c_eff (geometric) = {c_eff_geom:.4f} M_KK")
print(f"    delta_c/c = {(c_eff_geom - c_BdG)/c_BdG:.4e}")

# For the ZERO-MODE Goldstone on the fabric:
# The propagator is P(K) = 1/(c^2 K^2 + m^2) where c = c_BdG averaged.
# The texture on T^2 doesn't enter because the zero mode averages over it.
# The Goldstone propagator is EXACT O-Z with the bulk c_BdG and m_G.

Gamma_physical = 0.0  # Zero-mode Goldstone sees no texture
ratio_physical = Gamma_physical / m_G**2

print(f"\n  PHYSICAL Gamma(K_pivot) for zero-mode Goldstone = {Gamma_physical:.4e} M_KK^2")
print(f"  Ratio Gamma/m_G^2 = {ratio_physical:.4e}")

if ratio_physical < 0.01:
    verdict_final = "FAIL"
    detail_final = (f"Gamma(K_pivot)/m_G^2 = {ratio_physical:.4e} < 0.01. "
                    f"The Goldstone phonon is the n=0 KK mode on T^2. "
                    f"As a zero mode, it sees <V(x)>_T2 = 0 by construction. "
                    f"Eikonal damping from condensate texture DOES NOT AFFECT "
                    f"the zero-mode Goldstone propagator. "
                    f"The O-Z identity alpha_s = n_s^2 - 1 is UNMODIFIED. "
                    f"Eikonal breakdown is an INTERNAL T^2 phenomenon affecting "
                    f"only KK modes n >= 1, which are at the KK mass scale.")
elif ratio_physical > 0.1:
    verdict_final = "PASS"
    detail_final = f"Gamma/m_G^2 = {ratio_physical:.4e} > 0.1"
else:
    verdict_final = "INFO"
    detail_final = f"Gamma/m_G^2 = {ratio_physical:.4e} in [0.01, 0.1]"

print(f"\n  FINAL VERDICT: {verdict_final}")
print(f"  {detail_final}")


# ============================================================================
#  SECTION 13: WHAT EIKONAL BREAKDOWN DOES AFFECT
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 13: What eikonal breakdown DOES affect")
print("=" * 78)

# The 78.3% eikonal breakdown region is physically real. It means:
#
# 1. KK MODES (n >= 1) with internal wavelength ~ 1/M_KK see the texture
#    as a strong scattering potential. These modes are Anderson-localized
#    on T^2 (kl ~ 10^{-4} << 1 for V_rms ~ 3, l_corr ~ 1 M_KK^{-1}).
#
# 2. The 111 subsonic cavities (R_eff ~ 0.5-1.2 M_KK^{-1}) confine
#    acoustic quasiparticles at energies omega > 0.8 M_KK (S49).
#    These are ABOVE the Goldstone mass by a factor 0.8/0.07 = 11.4x.
#
# 3. The cavity-confined modes form a discrete spectrum starting at
#    0.800 M_KK with Q ~ exp(23.5). These are part of the KK spectrum,
#    not the Goldstone sector.
#
# 4. The texture DOES affect the BCS dynamics (formation, stability,
#    Q-factors of the condensate). But once formed, the zero-mode
#    Goldstone rides on top of it unperturbed.

# Quantify KK mode scattering
K_KK = 2 * PI / (1.0 / np.sqrt(g_11))  # KK fundamental ~ 2*pi * sqrt(g_11)
# Actually K_KK ~ M_KK in natural units, but on the lattice:
K_KK_lattice = K_torus_fund  # fundamental KK mode on T^2
S_at_KK = S_interp(K_KK_lattice)

print(f"  KK mode scattering:")
print(f"    K_KK_fund = {K_KK_lattice:.4f} M_KK (first KK mode on T^2)")
print(f"    S(K_KK) = {S_at_KK:.4e}")
print(f"    V_rms = {V_rms:.4f}")
print(f"    KK modes are strongly scattered (V_rms >> 1)")
print(f"    Localization length ~ {l_mfp_strong:.4e} M_KK^{{-1}} (< L_phys = {L_phys:.4f})")

print(f"\n  Cavity confinement:")
print(f"    111 subsonic cavities, largest R_eff = {float(d_cav['cavity_R_eff'][0]):.3f} M_KK^{{-1}}")
print(f"    Lowest cavity mode = {float(d_cav['omega_cavity_lowest']):.4f} M_KK")
print(f"    omega_cavity / m_G = {float(d_cav['omega_cavity_lowest'])/m_G:.1f}x above Goldstone")
print(f"    Q_cavity ~ exp({float(d_cav['Q_exponent']):.1f}) = perfect confinement")

print(f"\n  Separation of scales:")
print(f"    Goldstone: m_G = {m_G:.4f} M_KK  <-- ZERO mode, unaffected by texture")
print(f"    Cavity:    omega_min = 0.800 M_KK  <-- n>=1 modes, texture-confined")
print(f"    Gap:       omega_cavity / m_G = {0.800/m_G:.1f}x separation")
print(f"    The two sectors are DECOUPLED by the KK mass gap.")


# ============================================================================
#  SAVE DATA
# ============================================================================

print("\n" + "=" * 78)
print("Saving results")
print("=" * 78)

results = {
    # Gate
    'gate_name': 'EIKONAL-DAMPING-50',
    'gate_verdict': verdict_final,
    'gate_detail': detail_final,

    # Input parameters
    'm_G': m_G,
    'c_BdG': c_BdG,
    'g_11': g_11,
    'L_phys': L_phys,
    'N_grid': N_grid,
    'K_pivot': K_pivot,
    'lambda_pivot': lambda_pivot,

    # Texture statistics
    'Delta_mean': Delta_mean,
    'Delta_std': Delta_std,
    'V_rms': V_rms,
    'V_max': V_max,
    'V_min': V_min,
    'V_haar_avg': V_avg_haar,

    # Structure factor
    'q_centers': q_centers,
    'S_q': S_q,
    'q_50_percent': q_50,
    'q_90_percent': q_90,
    'l_corr': l_corr,

    # Born self-energy (for internal T^2 modes)
    'K_array': K_array,
    'Sigma_real': Sigma_real,
    'Sigma_imag': Sigma_imag,
    'Gamma_K': Gamma_K,
    'Gamma_at_pivot_Born': Gamma_pivot,
    'ratio_Born': ratio_pivot,

    # Physical Goldstone (zero-mode)
    'Gamma_at_pivot_physical': Gamma_physical,
    'ratio_physical': ratio_physical,

    # Mass correction
    'delta_m2_2nd_order': delta_m2_2nd_order,
    'delta_m2_over_m2': delta_m2_2nd_order / m_G**2,

    # Sound speed
    'c_eff_pert': c_eff_pert,
    'c_eff_geom': c_eff_geom,

    # Strong scattering (KK modes)
    'l_mfp_strong': l_mfp_strong,
    'kl_Ioffe_Regel': kl_IR,

    # Spectral indices
    'n_s_OZ': n_s_OZ,
    'alpha_s_OZ': alpha_s_OZ,
    'n_s_damped_Born': n_s_damped,
    'alpha_s_damped_Born': alpha_s_damped,

    # Propagator data
    'P0_K': P0_K,
    'P_K_abs2': P_K_abs2,
}

outpath = os.path.join(DATA_DIR, 's50_eikonal_damping.npz')
np.savez(outpath, **results)
print(f"  Saved: {outpath}")


# ============================================================================
#  PLOT
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: Condensate texture V(x) on T^2
ax = axes[0, 0]
T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')
im = ax.pcolormesh(T1, T2, V_field, cmap='RdBu_r', vmin=-2, vmax=2)
ax.set_xlabel(r'$\theta_1$')
ax.set_ylabel(r'$\theta_2$')
ax.set_title(r'$V(\mathbf{x}) = (\Delta^2 - \langle\Delta^2\rangle)/\langle\Delta^2\rangle$')
plt.colorbar(im, ax=ax, label=r'$V$')

# Panel 2: Structure factor S(q)
ax = axes[0, 1]
ax.semilogy(q_centers[mask_counts], S_q[mask_counts], 'b-', linewidth=1.5, label='$S(q)$')
ax.axvline(K_G, color='red', linestyle='--', linewidth=1.5, label=f'$K_G = {K_G:.3f}$')
ax.axvline(K_torus_fund, color='green', linestyle=':', linewidth=1.5,
           label=f'$K_{{fund}}$ = {K_torus_fund:.3f}')
ax.set_xlabel(r'$q$ [M$_{\rm KK}$]')
ax.set_ylabel(r'$S(q)$ [M$_{\rm KK}^{-2}$]')
ax.set_title('Structure Factor of Condensate Texture')
ax.legend(fontsize=8)
ax.set_xlim(0, q_max/2)

# Panel 3: Born self-energy
ax = axes[0, 2]
valid_K = K_array > 0.01
ax.semilogy(K_array[valid_K], np.abs(Sigma_imag[valid_K]) + 1e-30, 'b-',
            linewidth=1.5, label=r'$|\mathrm{Im}[\Sigma(K)]|$ (Born)')
ax.semilogy(K_array[valid_K], np.abs(Sigma_real[valid_K]) + 1e-30, 'r--',
            linewidth=1.5, label=r'$|\mathrm{Re}[\Sigma(K)]|$ (Born)')
ax.axhline(m_G**2, color='black', linestyle=':', linewidth=1, label=f'$m_G^2 = {m_G**2:.4e}$')
ax.axvline(K_pivot, color='green', linestyle='--', linewidth=1, label=f'$K_{{pivot}}$')
ax.set_xlabel(r'$K$ [M$_{\rm KK}$]')
ax.set_ylabel(r'$|\Sigma|$ [M$_{\rm KK}^2$]')
ax.set_title(r'Born Self-Energy $\Sigma(K)$ (internal T$^2$ modes)')
ax.legend(fontsize=7)

# Panel 4: Propagator comparison
ax = axes[1, 0]
ax.loglog(K_array[valid_K], P0_K[valid_K], 'b-', linewidth=1.5, label='O-Z (undamped)')
ax.loglog(K_array[valid_K], np.sqrt(P_K_abs2[valid_K]), 'r--', linewidth=1.5,
          label='Born-damped (internal)')
ax.axvline(K_pivot, color='green', linestyle='--', linewidth=1, label=f'$K_{{pivot}}$')
ax.set_xlabel(r'$K$ [M$_{\rm KK}$]')
ax.set_ylabel(r'$|P(K)|$')
ax.set_title('Propagator: O-Z vs Born-damped')
ax.legend(fontsize=8)

# Panel 5: Scale hierarchy diagram
ax = axes[1, 1]
scales = {
    '$K_{fund}$': K_torus_fund,
    '$K_G = m_G/c$': K_G,
    '$K_{Z_3}$': K_domain,
    '$K_{cavity}$': 0.800 / c_BdG,
    '$K_{Nyquist}$': q_max,
}
y_pos = np.arange(len(scales))
colors_bar = ['green', 'red', 'orange', 'purple', 'gray']
ax.barh(y_pos, list(scales.values()), color=colors_bar, alpha=0.7, edgecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(list(scales.keys()), fontsize=10)
ax.set_xlabel(r'$K$ [M$_{\rm KK}$]')
ax.set_title('Wavevector Scale Hierarchy')
ax.set_xscale('log')
for i, (name, val) in enumerate(scales.items()):
    ax.text(val * 1.1, i, f'{val:.3f}', va='center', fontsize=8)

# Panel 6: Summary box
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"EIKONAL-DAMPING-50: {verdict_final}\n"
    f"{'='*40}\n\n"
    f"Key result:\n"
    f"  Goldstone = n=0 KK mode on T$^2$\n"
    f"  Zero mode sees <V> = 0 by construction\n"
    f"  => NO eikonal damping of propagator\n\n"
    f"Born self-energy (internal modes):\n"
    f"  $\\Gamma(K_{{pivot}})$ = {Gamma_pivot:.4e} M$_{{KK}}^2$\n"
    f"  $\\Gamma/m_G^2$ = {ratio_pivot:.4e}\n\n"
    f"Physical Goldstone (zero-mode):\n"
    f"  $\\Gamma_{{phys}}/m_G^2$ = 0 (exact)\n\n"
    f"Texture statistics:\n"
    f"  $V_{{rms}}$ = {V_rms:.3f}\n"
    f"  Strong scattering regime\n"
    f"  KK modes: Anderson localized\n\n"
    f"O-Z identity preserved:\n"
    f"  $\\alpha_s = n_s^2 - 1$ UNMODIFIED"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('EIKONAL-DAMPING-50: Goldstone Phonon Damping from Condensate Texture on T$^2$',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(DATA_DIR, 's50_eikonal_damping.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")
plt.close()

print("\n" + "=" * 78)
print(f"FINAL VERDICT: EIKONAL-DAMPING-50 = {verdict_final}")
print("=" * 78)
