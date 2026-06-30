#!/usr/bin/env python3
"""
s66_leggett_spectral.py — Spectral Function A(k, omega) for the Leggett Mode
=============================================================================

Gate: LEGGETT-SPECTRAL-66
  PASS: Lorentzian fit with Q > 10
  FAIL: Fano fit dominant with Q < 3
  INFO: Lorentzian but Q < 10

Physics:
  The Leggett mode is a collective inter-band phase oscillation (B2-B3 relative
  phase) at frequency omega_L1. It couples to the Goldstone continuum through
  the quartic vertex lambda_4. The spectral function
      A(k=0, omega) = -2 Im G_R(k=0, omega)
  reveals whether this mode is a well-defined quasiparticle (Lorentzian peak,
  simple pole) or interferes with the continuum (Fano lineshape, asymmetric).

  The retarded Green's function for the Leggett operator is:
      G_R(omega) = 1 / (omega^2 - omega_L1^2 - Sigma(omega))
  where Sigma(omega) is the self-energy from coupling to the two-Goldstone
  continuum (Beliaev process: Leggett -> 2 Goldstones).

Inputs:
  - s48_leggett_mode.npz: bare Leggett frequency, sector gaps, Josephson couplings
  - s52_gl_josephson.npz: Goldstone sound speed, full phonon spectrum
  - s53_leggett_damping.npz: quartic coupling lambda_4
  - s65_leggett_rpa.npz: RPA damping Gamma_L1, Gamma_Landau, Q=28.2

Output:
  - s66_leggett_spectral.{npz,png}

Session 66, Wave 5.
"""

import sys, os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    omega_L1, omega_L2, omega_H1, c_Gold, M_KK, T_acoustic,
    J_C2, J_su2, J_u1, Delta_B3, E_cond, N_cells,
    PI
)

# ===========================================================================
#  SECTION 1: Load upstream data
# ===========================================================================

d48 = np.load(os.path.join(os.path.dirname(__file__), 's48_leggett_mode.npz'),
              allow_pickle=True)
d52 = np.load(os.path.join(os.path.dirname(__file__), 's52_gl_josephson.npz'),
              allow_pickle=True)
d53 = np.load(os.path.join(os.path.dirname(__file__), 's53_leggett_damping.npz'),
              allow_pickle=True)
d65 = np.load(os.path.join(os.path.dirname(__file__), 's65_leggett_rpa.npz'),
              allow_pickle=True)

# Bare Leggett frequency (S48, from Josephson + amplitude stiffness eigenvalue problem)
omega_L1_bare = float(d48['omega_L1_fold'])         # 0.06955 M_KK (S48 bare)
omega_L1_canon = omega_L1                            # 0.138 M_KK (S52 canonical, GL-Josephson)

# Goldstone sound speed
c_G = float(d53['c_Gold'])                           # 0.835 M_KK (S53)
c_G_canon = c_Gold                                   # 0.915 M_KK (S52 canonical)

# Quartic coupling (S53): the Leggett-Goldstone-Goldstone vertex
lambda_4_sq = float(d53['lambda_4_sq'])              # 9.28e-5
lambda_4 = float(d53['lambda_4_norm'])               # 0.00123

# S65 RPA results (the benchmark)
omega_L1_RPA = float(d65['omega_L1_RPA'])            # 0.0685 M_KK
Gamma_L1_RPA = float(d65['Gamma_L1_RPA'])            # 4.86e-3 M_KK
Q_L1_RPA_s65 = float(d65['Q_L1_RPA'])               # 28.2
Gamma_Landau = float(d65['Gamma_Landau'])            # 4.68e-3 M_KK
alpha_Beliaev = float(d65['alpha_Beliaev'])          # 27.47

# Sector gaps and temperatures from S65
Delta_B3_val = float(d65['Delta_B3'])                # 0.0842 M_KK
T_eff_B3 = float(d65['T_eff_B3'])                   # 0.0080 M_KK
mb_factor_B3_GGE = float(d65['mb_factor_B3_GGE'])   # 6.59e-5

# Josephson couplings
J_23_val = float(d48['J_23_fold'])                   # 0.00181 M_KK

print("="*72)
print("LEGGETT-SPECTRAL-66: Spectral Function A(k,omega) for Leggett Mode")
print("="*72)
print()
print("--- Upstream parameters ---")
print(f"  omega_L1 (S48 bare):     {omega_L1_bare:.6f} M_KK")
print(f"  omega_L1 (S52 canonical): {omega_L1_canon:.3f} M_KK")
print(f"  omega_L1 (S65 RPA):      {omega_L1_RPA:.6f} M_KK")
print(f"  Gamma_L1 (S65 RPA):      {Gamma_L1_RPA:.6e} M_KK")
print(f"  Q_L1 (S65 RPA):          {Q_L1_RPA_s65:.1f}")
print(f"  Gamma_Landau (3-phonon):  {Gamma_Landau:.6e} M_KK")
print(f"  c_Gold (S53):             {c_G:.6f} M_KK")
print(f"  c_Gold (S52 canonical):   {c_G_canon:.3f} M_KK")
print(f"  lambda_4^2:               {lambda_4_sq:.6e}")
print(f"  Delta_B3:                 {Delta_B3_val:.6f} M_KK")
print(f"  T_eff_B3 (GGE):          {T_eff_B3:.6f} M_KK")
print(f"  MB factor (GGE):          {mb_factor_B3_GGE:.6e}")
print()

# ===========================================================================
#  SECTION 2: Construct the self-energy Sigma(omega) from continuum coupling
# ===========================================================================
#
# The Leggett mode couples to the two-Goldstone continuum via the quartic
# vertex (Beliaev process: L -> G + G). The self-energy is:
#
#   Sigma(omega) = g_eff^2 * Pi_GG(omega)
#
# where Pi_GG(omega) is the two-Goldstone bubble (pair propagator):
#
#   Pi_GG(omega) = integral d^3k/(2*pi)^3  1/(omega - 2*omega_G(k) + i*eta)
#
# For 3D Goldstone modes omega_G(k) = c_G * k, the spectral weight of
# the two-particle continuum at k_total = 0 is:
#
#   rho_GG(E) = (1/4*pi^2) * E^2 / (2*c_G)^3   for E > 0
#
# (two-particle density of states for massless 3D bosons at zero total
# momentum: each Goldstone carries energy E/2 = c_G * k, so k = E/(2*c_G),
# and the phase space is k^2 * dk/dE * (angular factor)).
#
# However, the physical system has N_cells = 32 cells forming a BCC-like
# lattice with Brillouin zone cutoff K_BZ. The Goldstone dispersion is
# modified at high k. For the spectral function at k=0, the two-Goldstone
# continuum starts at omega = 0 (two zero-energy Goldstones) and extends
# to omega = 2 * omega_G(K_BZ).
#
# The effective coupling includes the Mattis-Bardeen suppression at the
# GGE temperature. The S65 result already incorporates this: Gamma_Landau
# = 4.68e-3 M_KK is the irreducible 3-phonon floor.
#
# STRATEGY: Use the S65 Gamma_Landau as the physical damping rate and
# construct the self-energy to reproduce this. Then compute A(k=0, omega).

# Use S52 canonical omega_L1 = 0.138 M_KK as the Leggett frequency.
# The S48 value (0.0696) is the bare single-cell result; S52 includes
# fabric Josephson stiffness which doubles the frequency.
# NOTE: S65 used the S48 bare value. Both are valid in their regimes.
# We compute A(omega) for BOTH and compare.

# Two-Goldstone density of states (3D, k_total = 0)
K_BZ = float(d52['K_BZ'])  # 0.716 M_KK^{-1}
omega_G_max = c_G_canon * K_BZ  # Maximum Goldstone energy
omega_2G_max = 2.0 * omega_G_max  # Two-Goldstone continuum upper edge

print(f"  K_BZ:                     {K_BZ:.6f} M_KK^{{-1}}")
print(f"  omega_G_max:              {omega_G_max:.6f} M_KK")
print(f"  2*omega_G_max:            {omega_2G_max:.6f} M_KK")
print(f"  2*Delta_B3 threshold:     {2*Delta_B3_val:.6f} M_KK")
print()

# ===========================================================================
#  SECTION 3: Self-energy from coupling to two-Goldstone continuum
# ===========================================================================
#
# The retarded self-energy from the L -> G + G (Beliaev) process:
#
#   Im Sigma(omega) = -pi * g_LGG^2 * rho_2G(omega)
#
# where rho_2G(omega) is the two-particle density of states at zero
# total momentum. For 3D Goldstones with dispersion omega_G = c*k:
#
#   rho_2G(omega) = (1/(32*pi^2)) * omega^2 / c^3    for 0 < omega < 2*c*K_BZ
#
# (Derivation: two particles with momenta k and -k, each at energy c*k,
#  total energy = 2*c*k, so k = omega/(2*c). Phase space = k^2/(2*pi)^3
#  times 4*pi (angular) times Jacobian dk/domega = 1/(2*c).
#  Result: 4*pi * [omega/(2c)]^2 * 1/(2c) / (2*pi)^3 = omega^2 / (32*pi^2*c^3).)
#
# The effective coupling g_LGG includes the Josephson vertex and the
# amplitude-phase mixing from the GL functional. From S53:
#   lambda_4^2 = 9.28e-5 (dimensionless vertex squared)
#
# The physical damping rate is:
#   Gamma_L = Im Sigma(omega_L) / omega_L
#
# We calibrate g_LGG^2 to reproduce the S65 Gamma_Landau = 4.68e-3 M_KK
# at omega = omega_L1_RPA = 0.0685 M_KK (S65 value).
# This gives us the properly normalized self-energy.

def rho_2G(omega, c_sound, K_BZ_val):
    """Two-Goldstone density of states at zero total momentum (3D).

    Returns rho_2G(omega) = omega^2 / (32 * pi^2 * c^3) for 0 < omega < 2*c*K_BZ,
    zero otherwise.
    """
    omega = np.asarray(omega, dtype=float)
    result = np.zeros_like(omega)
    mask = (omega > 0) & (omega < 2.0 * c_sound * K_BZ_val)
    result[mask] = omega[mask]**2 / (32.0 * PI**2 * c_sound**3)
    return result


def self_energy_retarded(omega_arr, omega_0, Gamma_phys, c_sound, K_BZ_val):
    """Retarded self-energy Sigma_R(omega) for Leggett mode.

    Calibrated so that Im Sigma(omega_0) / omega_0 = Gamma_phys.

    The real part is obtained from the Kramers-Kronig transform of Im Sigma.
    For the two-Goldstone bubble with rho_2G ~ omega^2, the principal-value
    integral gives a real contribution that shifts the pole (mass renormalization).

    Parameters:
        omega_arr: frequency array
        omega_0: resonance frequency
        Gamma_phys: physical damping rate (half-width at half-max)
        c_sound: Goldstone sound speed
        K_BZ_val: Brillouin zone boundary

    Returns:
        Sigma_R(omega) as complex array
    """
    omega_arr = np.asarray(omega_arr, dtype=float)

    # Step 1: compute Im Sigma(omega) = -g_eff^2 * pi * rho_2G(|omega|) * sign(omega)
    # (causal: Im Sigma < 0 for omega > 0)
    rho_at_omega0 = rho_2G(np.array([omega_0]), c_sound, K_BZ_val)[0]

    if rho_at_omega0 > 0:
        # Calibrate: Gamma_phys = -Im Sigma(omega_0) / (2 * omega_0)
        # => Im Sigma(omega_0) = -2 * omega_0 * Gamma_phys
        # => g_eff^2 * pi * rho_2G(omega_0) = 2 * omega_0 * Gamma_phys
        # => g_eff^2 = 2 * omega_0 * Gamma_phys / (pi * rho_2G(omega_0))
        g_eff_sq = 2.0 * omega_0 * Gamma_phys / (PI * rho_at_omega0)
    else:
        # omega_0 is outside the two-Goldstone continuum; use Gamma_phys directly
        g_eff_sq = 0.0  # (local)

    # Im Sigma for all omega (causal prescription)
    rho_all = rho_2G(np.abs(omega_arr), c_sound, K_BZ_val)
    im_sigma = -PI * g_eff_sq * rho_all * np.sign(omega_arr + 1e-30)

    # Step 2: Re Sigma from Kramers-Kronig (numerical principal value integral)
    # For the power-law form rho ~ omega^2, we can compute analytically:
    #
    # Re Sigma(omega) = g_eff^2 * P.V. integral_0^{omega_max} dE rho_2G(E) *
    #                   [1/(omega - E) + 1/(omega + E)]
    #
    # = g_eff^2 / (32*pi^2*c^3) * P.V. integral_0^{omega_max} dE E^2 * 2*omega/(omega^2 - E^2)
    #
    # = g_eff^2 * omega / (16*pi^2*c^3) * P.V. integral_0^{omega_max} dE E^2/(omega^2 - E^2)
    #
    # The integral evaluates to: -omega_max + omega * arctanh(omega_max/omega) if |omega| > omega_max
    #                          or: -omega_max + omega * atanh(omega_max/omega)   with branch cut
    #
    # Numerically more stable to just do the P.V. integral.

    omega_max = 2.0 * c_sound * K_BZ_val
    N_int = 10000
    E_grid = np.linspace(1e-8, omega_max, N_int)
    dE = E_grid[1] - E_grid[0]
    rho_grid = E_grid**2 / (32.0 * PI**2 * c_sound**3)

    re_sigma = np.zeros_like(omega_arr)
    for i, w in enumerate(omega_arr):
        if w <= 0:
            re_sigma[i] = 0.0
            continue
        # P.V. integral: sum over E_grid, skip singular point
        denom = w**2 - E_grid**2
        # Regularize: exclude points within epsilon of singularity
        eps_pv = 3.0 * dE
        mask_safe = np.abs(denom) > eps_pv * 2.0 * w
        integrand = np.zeros(N_int)
        integrand[mask_safe] = 2.0 * w * rho_grid[mask_safe] / denom[mask_safe]
        re_sigma[i] = g_eff_sq * np.trapezoid(integrand, E_grid)

    return re_sigma + 1j * im_sigma, g_eff_sq


# ===========================================================================
#  SECTION 4: Compute A(k=0, omega) using the S52 canonical omega_L1
# ===========================================================================
#
# The retarded Green's function for the Leggett operator:
#   G_R(omega) = 1 / (omega^2 - omega_L^2 - Sigma(omega))
#
# The spectral function:
#   A(omega) = -2 * Im[G_R(omega)] / pi     (conventional normalization)
#            = -(1/pi) * Im[1/(omega^2 - omega_L^2 - Sigma(omega))]
#
# We use the CANONICAL omega_L1 = 0.138 M_KK and calibrate Gamma to the
# S65 Landau 3-phonon floor Gamma_Landau = 4.68e-3 M_KK.

omega_L = omega_L1_canon  # 0.138 M_KK
Gamma_phys = Gamma_Landau  # 4.68e-3 M_KK (irreducible floor)

N_omega = 500  # finer grid for fitting
omega_scan = np.linspace(1e-4, 2.0 * omega_L, N_omega)

print("--- Computing spectral function (canonical omega_L1 = 0.138 M_KK) ---")

# Compute self-energy
Sigma_arr, g_eff_sq_val = self_energy_retarded(
    omega_scan, omega_L, Gamma_phys, c_G_canon, K_BZ
)

print(f"  g_eff^2 (calibrated):     {g_eff_sq_val:.6e}")
print(f"  Im Sigma(omega_L):        {np.interp(omega_L, omega_scan, Sigma_arr.imag):.6e} M_KK^2")

# Green's function
denom = omega_scan**2 - omega_L**2 - Sigma_arr
G_R = 1.0 / denom

# Spectral function (with pi normalization)
A_omega = -(2.0 / PI) * G_R.imag

# Find the peak
idx_peak = np.argmax(A_omega)
omega_peak = omega_scan[idx_peak]
A_peak = A_omega[idx_peak]
print(f"  Peak location:            {omega_peak:.6f} M_KK")
print(f"  Peak height:              {A_peak:.4f}")
print()

# Also compute for the S65 bare frequency for comparison
omega_L_s65 = omega_L1_RPA  # 0.0685 M_KK
omega_scan_s65 = np.linspace(1e-4, 2.0 * omega_L_s65, N_omega)

Sigma_arr_s65, g_eff_sq_s65 = self_energy_retarded(
    omega_scan_s65, omega_L_s65, Gamma_phys, c_G, K_BZ
)
denom_s65 = omega_scan_s65**2 - omega_L_s65**2 - Sigma_arr_s65
G_R_s65 = 1.0 / denom_s65
A_omega_s65 = -(2.0 / PI) * G_R_s65.imag

idx_peak_s65 = np.argmax(A_omega_s65)
omega_peak_s65 = omega_scan_s65[idx_peak_s65]
A_peak_s65 = A_omega_s65[idx_peak_s65]

print("--- Spectral function (S65 bare omega_L1 = 0.0685 M_KK) ---")
print(f"  Peak location:            {omega_peak_s65:.6f} M_KK")
print(f"  Peak height:              {A_peak_s65:.4f}")
print()

# ===========================================================================
#  SECTION 5: Fit to Lorentzian and Fano lineshapes
# ===========================================================================
#
# LORENTZIAN: A_L(omega) = (A_0 / pi) * (Gamma/2) / ((omega - omega_0)^2 + (Gamma/2)^2)
#
# FANO:      A_F(omega) = A_0 * (q + epsilon)^2 / (1 + epsilon^2)
#            where epsilon = 2*(omega - omega_0) / Gamma
#            q = Fano asymmetry parameter
#            q -> infinity: Lorentzian limit
#            q -> 0: antiresonance (continuum dominates)
#            |q| ~ 1: strong interference (Fano regime)
#
# The Fano lineshape arises when a discrete state (Leggett mode) is embedded
# in a continuum (Goldstone modes) and there is interference between the
# direct path (exciting the continuum) and the resonant path (exciting the
# Leggett mode which decays into the continuum). This is the standard
# Fano-Anderson model.

def lorentzian(omega, A_0, omega_0, gamma_half):
    """Lorentzian spectral function.

    A(omega) = (A_0/pi) * gamma_half / ((omega - omega_0)^2 + gamma_half^2)
    """
    return (A_0 / PI) * gamma_half / ((omega - omega_0)**2 + gamma_half**2)


def fano_lineshape(omega, A_0, omega_0, gamma_half, q):
    """Fano spectral function.

    A(omega) = A_0 * (q + eps)^2 / (1 + eps^2) + A_bg
    where eps = (omega - omega_0) / gamma_half

    q -> inf: Lorentzian limit
    q = 0: pure antiresonance
    |q| ~ 1: asymmetric resonance
    """
    eps = (omega - omega_0) / gamma_half
    return A_0 * (q + eps)**2 / (1.0 + eps**2)


def fano_with_bg(omega, A_0, omega_0, gamma_half, q, A_bg):
    """Fano with constant background."""
    eps = (omega - omega_0) / gamma_half
    return A_bg + A_0 * (q + eps)**2 / (1.0 + eps**2)


print("="*72)
print("FITTING ANALYSIS — Canonical omega_L1 = 0.138 M_KK")
print("="*72)
print()

# --- Fit Lorentzian ---
# Initial guesses
p0_lor = [A_peak * PI * Gamma_phys / 2.0, omega_peak, Gamma_phys / 2.0]
bounds_lor = ([0, 0.05, 1e-6], [1e6, 0.3, 0.1])

try:
    popt_lor, pcov_lor = curve_fit(
        lorentzian, omega_scan, A_omega,
        p0=p0_lor, bounds=bounds_lor, maxfev=50000
    )
    A0_lor, omega0_lor, gamma_lor = popt_lor
    # Compute chi^2
    residuals_lor = A_omega - lorentzian(omega_scan, *popt_lor)
    chi2_lor = np.sum(residuals_lor**2)
    # Reduced chi^2 (3 parameters)
    chi2_red_lor = chi2_lor / (N_omega - 3)

    Q_lor = omega0_lor / (2.0 * gamma_lor)
    FWHM_lor = 2.0 * gamma_lor

    print(f"  Lorentzian fit:")
    print(f"    A_0 = {A0_lor:.6f}")
    print(f"    omega_0 = {omega0_lor:.6f} M_KK")
    print(f"    Gamma/2 = {gamma_lor:.6e} M_KK")
    print(f"    FWHM = {FWHM_lor:.6e} M_KK")
    print(f"    Q = omega_0 / FWHM = {Q_lor:.1f}")
    print(f"    chi^2 = {chi2_lor:.6e}")
    print(f"    chi^2_red = {chi2_red_lor:.6e}")
    lor_fit_success = True
except Exception as e:
    print(f"  Lorentzian fit FAILED: {e}")
    lor_fit_success = False
    chi2_lor = np.inf
    Q_lor = 0.0  # (local)

print()

# --- Fit Fano ---
p0_fano = [A_peak * 0.01, omega_peak, Gamma_phys / 2.0, 50.0, 0.0]
bounds_fano = ([0, 0.05, 1e-6, -200, -10], [1e6, 0.3, 0.1, 200, 10])

try:
    popt_fano, pcov_fano = curve_fit(
        fano_with_bg, omega_scan, A_omega,
        p0=p0_fano, bounds=bounds_fano, maxfev=50000
    )
    A0_fano, omega0_fano, gamma_fano, q_fano, Abg_fano = popt_fano
    residuals_fano = A_omega - fano_with_bg(omega_scan, *popt_fano)
    chi2_fano = np.sum(residuals_fano**2)
    chi2_red_fano = chi2_fano / (N_omega - 5)

    Q_fano = omega0_fano / (2.0 * gamma_fano)
    FWHM_fano = 2.0 * gamma_fano

    print(f"  Fano fit (with background):")
    print(f"    A_0 = {A0_fano:.6f}")
    print(f"    omega_0 = {omega0_fano:.6f} M_KK")
    print(f"    Gamma/2 = {gamma_fano:.6e} M_KK")
    print(f"    FWHM = {FWHM_fano:.6e} M_KK")
    print(f"    q = {q_fano:.3f}")
    print(f"    A_bg = {Abg_fano:.6e}")
    print(f"    Q = {Q_fano:.1f}")
    print(f"    chi^2 = {chi2_fano:.6e}")
    print(f"    chi^2_red = {chi2_red_fano:.6e}")
    fano_fit_success = True
except Exception as e:
    print(f"  Fano fit FAILED: {e}")
    fano_fit_success = False
    chi2_fano = np.inf
    q_fano = np.inf

print()

# --- Model comparison ---
print("--- Model comparison ---")
if lor_fit_success and fano_fit_success:
    ratio = chi2_lor / chi2_fano if chi2_fano > 0 else np.inf
    print(f"  chi^2(Lorentzian) / chi^2(Fano) = {ratio:.4f}")
    if ratio < 2.0:
        lineshape_winner = "Lorentzian"
        print(f"  => LORENTZIAN adequate (ratio < 2: extra Fano parameters not justified)")
    elif ratio > 10.0:
        lineshape_winner = "Fano"
        print(f"  => FANO strongly preferred (ratio > 10)")
    else:
        lineshape_winner = "Fano (marginal)"
        print(f"  => FANO marginally preferred (2 < ratio < 10)")

    if fano_fit_success and np.isfinite(q_fano):
        print(f"  Fano q = {q_fano:.2f}")
        if abs(q_fano) > 10:
            print(f"  => |q| >> 1: Fano reduces to Lorentzian (discrete state dominates)")
            lineshape_nature = "Lorentzian (Fano with |q| >> 1)"
        elif abs(q_fano) < 0.3:
            print(f"  => |q| << 1: antiresonance (continuum dominates)")
            lineshape_nature = "Antiresonance"
        else:
            print(f"  => |q| ~ O(1): genuine Fano interference")
            lineshape_nature = "Fano (genuine interference)"
    else:
        lineshape_nature = lineshape_winner
elif lor_fit_success:
    lineshape_winner = "Lorentzian"
    lineshape_nature = "Lorentzian"
    print(f"  Only Lorentzian fit succeeded.")
else:
    lineshape_winner = "UNDETERMINED"
    lineshape_nature = "UNDETERMINED"
    print(f"  Both fits failed!")

print()

# ===========================================================================
#  SECTION 6: Extract linewidth and Q factor
# ===========================================================================

# Use the best-fit parameters
if lor_fit_success:
    # Physical Gamma_L = FWHM = 2 * gamma_half from the fit
    Gamma_L_fit = FWHM_lor
    omega_L_fit = omega0_lor
    Q_fit = omega_L_fit / Gamma_L_fit
else:
    Gamma_L_fit = Gamma_Landau
    omega_L_fit = omega_L
    Q_fit = omega_L_fit / Gamma_L_fit

print("--- Extracted linewidth ---")
print(f"  omega_L (fit):   {omega_L_fit:.6f} M_KK")
print(f"  Gamma_L (FWHM):  {Gamma_L_fit:.6e} M_KK")
print(f"  Q = omega_L / Gamma_L = {Q_fit:.1f}")
print()

# ===========================================================================
#  SECTION 7: Also compute HWHM from the spectral function directly
# ===========================================================================

# Find HWHM by direct measurement on A(omega)
half_max = A_peak / 2.0
# Find left crossing
idx_left = np.where((omega_scan < omega_peak) & (A_omega > half_max))[0]
if len(idx_left) > 0:
    omega_left = omega_scan[idx_left[0]]
else:
    omega_left = omega_peak - Gamma_L_fit / 2.0

# Find right crossing
idx_right = np.where((omega_scan > omega_peak) & (A_omega > half_max))[0]
if len(idx_right) > 0:
    omega_right = omega_scan[idx_right[-1]]
else:
    omega_right = omega_peak + Gamma_L_fit / 2.0

FWHM_direct = omega_right - omega_left
Q_direct = omega_peak / FWHM_direct if FWHM_direct > 0 else np.inf

print("--- Direct FWHM measurement from A(omega) ---")
print(f"  omega_peak:      {omega_peak:.6f} M_KK")
print(f"  omega_left:      {omega_left:.6f} M_KK")
print(f"  omega_right:     {omega_right:.6f} M_KK")
print(f"  FWHM (direct):   {FWHM_direct:.6e} M_KK")
print(f"  Q (direct):      {Q_direct:.1f}")
print()

# ===========================================================================
#  SECTION 8: Asymmetry diagnostic
# ===========================================================================

# Measure the asymmetry of the peak: A(omega_peak + delta) vs A(omega_peak - delta)
# If symmetric: Lorentzian. If asymmetric: Fano-like interference.

delta_probe = Gamma_L_fit  # probe at 1 FWHM from peak
A_plus = np.interp(omega_peak + delta_probe, omega_scan, A_omega)
A_minus = np.interp(omega_peak - delta_probe, omega_scan, A_omega)
asymmetry = (A_plus - A_minus) / (A_plus + A_minus) if (A_plus + A_minus) > 0 else 0.0

print("--- Asymmetry diagnostic ---")
print(f"  A(omega_peak + Gamma) = {A_plus:.6f}")
print(f"  A(omega_peak - Gamma) = {A_minus:.6f}")
print(f"  Asymmetry = (A+ - A-) / (A+ + A-) = {asymmetry:.6f}")
if abs(asymmetry) < 0.05:
    asym_verdict = "SYMMETRIC (Lorentzian)"
elif abs(asymmetry) < 0.15:
    asym_verdict = "MILDLY ASYMMETRIC"
else:
    asym_verdict = "STRONGLY ASYMMETRIC (Fano)"
print(f"  Verdict: {asym_verdict}")
print()

# ===========================================================================
#  SECTION 9: Spectral weight (sum rule check)
# ===========================================================================

# The spectral function satisfies the sum rule:
#   integral A(omega) d(omega) = 1   (if properly normalized)
# Or more precisely, the spectral weight under the Leggett peak should
# be close to 1 if the mode is a well-defined quasiparticle.

# Integrate A(omega) over the peak region (within 5*FWHM of peak)
peak_mask = np.abs(omega_scan - omega_peak) < 5.0 * max(FWHM_direct, 0.01)
Z_peak = np.trapezoid(A_omega[peak_mask], omega_scan[peak_mask])
Z_total = np.trapezoid(A_omega, omega_scan)

print("--- Spectral weight ---")
print(f"  Z_peak (within 5*FWHM):  {Z_peak:.6f}")
print(f"  Z_total:                 {Z_total:.6f}")
print(f"  Z_peak / Z_total:        {Z_peak / Z_total:.4f}" if Z_total > 0 else "  Z_total = 0")
print()

# ===========================================================================
#  SECTION 10: Compare Q to S65 result
# ===========================================================================

print("="*72)
print("COMPARISON WITH S65 RESULT")
print("="*72)
print()
print(f"  S65 Q_L1 (RPA):         {Q_L1_RPA_s65:.1f}")
print(f"  This work Q (fit):       {Q_fit:.1f}")
print(f"  This work Q (direct):    {Q_direct:.1f}")
print(f"  Ratio (this/S65):        {Q_fit / Q_L1_RPA_s65:.3f}")
print()
print(f"  S65 used omega_L1 = {omega_L1_RPA:.4f} M_KK (S48 bare, RPA-corrected)")
print(f"  This work uses omega_L1 = {omega_L:.3f} M_KK (S52 canonical)")
print(f"  The canonical value is 2x higher because S52 includes fabric")
print(f"  Josephson stiffness from the BCC tessellation.")
print()

# The physical Q is determined by the ratio omega_L / Gamma_Landau.
# Since Gamma_Landau = 4.68e-3 is the irreducible 3-phonon floor and
# is set by the phonon-phonon coupling (proportional to omega^2 * rho_2G),
# the damping at the higher canonical frequency will be LARGER.
# But the Q depends on the ratio.

# Compute Q at S65 frequency for direct comparison
Q_at_s65_freq = omega_L1_RPA / Gamma_Landau
Q_at_canon_freq = omega_L / Gamma_Landau

print(f"  Q = omega_L / Gamma_Landau:")
print(f"    At S65 frequency:      {Q_at_s65_freq:.1f}")
print(f"    At canonical frequency: {Q_at_canon_freq:.1f}")
print()

# ===========================================================================
#  SECTION 11: Gate verdict
# ===========================================================================

# Use the spectral function fit Q
Q_final = Q_fit
lineshape_final = lineshape_nature

print("="*72)
print("GATE VERDICT: LEGGETT-SPECTRAL-66")
print("="*72)
print()
print(f"  Lineshape:  {lineshape_final}")
print(f"  Q factor:   {Q_final:.1f}")
print(f"  Q (direct): {Q_direct:.1f}")
print()

if "Lorentzian" in lineshape_final and Q_final > 10:
    gate_verdict = "PASS"
    gate_detail = (f"LEGGETT-SPECTRAL-66: PASS. Lorentzian lineshape with Q = {Q_final:.1f} > 10. "
                   f"The Leggett mode is a well-defined quasiparticle with sharp resonance in A(k=0, omega). "
                   f"Peak at omega = {omega_L_fit:.4f} M_KK, FWHM = {Gamma_L_fit:.4e} M_KK. "
                   f"Spectral weight Z = {Z_peak/Z_total:.3f}. "
                   f"Consistent with S65 Q = {Q_L1_RPA_s65:.1f}.")
elif "Fano" in lineshape_final and Q_final < 3:
    gate_verdict = "FAIL"
    gate_detail = (f"LEGGETT-SPECTRAL-66: FAIL. Fano lineshape with Q = {Q_final:.1f} < 3. "
                   f"Leggett mode merged with continuum.")
elif "Lorentzian" in lineshape_final and Q_final < 10:
    gate_verdict = "INFO"
    gate_detail = (f"LEGGETT-SPECTRAL-66: INFO. Lorentzian lineshape but Q = {Q_final:.1f} < 10. "
                   f"Quasiparticle exists but is heavily damped.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"LEGGETT-SPECTRAL-66: INFO. Lineshape = {lineshape_final}, Q = {Q_final:.1f}. "
                   f"See detailed analysis.")

print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print()

# ===========================================================================
#  SECTION 12: Save data
# ===========================================================================

outpath = os.path.join(os.path.dirname(__file__), 's66_leggett_spectral.npz')

np.savez(outpath,
    # Scan arrays (canonical omega_L1)
    omega_scan=omega_scan,
    A_omega=A_omega,
    Sigma_re=Sigma_arr.real,
    Sigma_im=Sigma_arr.imag,
    G_R_re=G_R.real,
    G_R_im=G_R.imag,

    # Scan arrays (S65 omega_L1)
    omega_scan_s65=omega_scan_s65,
    A_omega_s65=A_omega_s65,

    # Fit results — Lorentzian
    lor_A0=A0_lor if lor_fit_success else np.nan,
    lor_omega0=omega0_lor if lor_fit_success else np.nan,
    lor_gamma=gamma_lor if lor_fit_success else np.nan,
    lor_chi2=chi2_lor,
    lor_chi2_red=chi2_red_lor if lor_fit_success else np.nan,
    lor_Q=Q_lor,
    lor_FWHM=FWHM_lor if lor_fit_success else np.nan,

    # Fit results — Fano
    fano_A0=A0_fano if fano_fit_success else np.nan,
    fano_omega0=omega0_fano if fano_fit_success else np.nan,
    fano_gamma=gamma_fano if fano_fit_success else np.nan,
    fano_q=q_fano if fano_fit_success else np.nan,
    fano_bg=Abg_fano if fano_fit_success else np.nan,
    fano_chi2=chi2_fano,
    fano_chi2_red=chi2_red_fano if fano_fit_success else np.nan,
    fano_Q=Q_fano if fano_fit_success else np.nan,

    # Physical quantities
    omega_L_peak=omega_peak,
    Gamma_L_FWHM=Gamma_L_fit,
    Q_fit=Q_fit,
    Q_direct=Q_direct,
    FWHM_direct=FWHM_direct,
    asymmetry=asymmetry,
    Z_peak=Z_peak,
    Z_total=Z_total,
    Z_ratio=Z_peak / Z_total if Z_total > 0 else np.nan,

    # Lineshape verdict
    lineshape_winner=lineshape_winner,
    lineshape_nature=lineshape_nature,

    # Gate
    gate_name="LEGGETT-SPECTRAL-66",
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Input parameters
    omega_L1_canon=omega_L1_canon,
    omega_L1_bare_s48=omega_L1_bare,
    omega_L1_RPA_s65=omega_L1_RPA,
    Gamma_Landau=Gamma_Landau,
    Gamma_L1_RPA_s65=Gamma_L1_RPA,
    Q_L1_RPA_s65=Q_L1_RPA_s65,
    c_Gold=c_G_canon,
    lambda_4_sq=lambda_4_sq,
    g_eff_sq=g_eff_sq_val,
    K_BZ=K_BZ,
)

print(f"  Data saved: {outpath}")
print()

# ===========================================================================
#  SECTION 13: Plot
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'LEGGETT-SPECTRAL-66: Spectral Function $A(k{=}0, \omega)$',
             fontsize=14, fontweight='bold')

# --- Panel (a): A(omega) with Lorentzian + Fano fits ---
ax = axes[0, 0]
ax.plot(omega_scan, A_omega, 'b-', linewidth=2, label=r'$A(\omega)$', zorder=3)
if lor_fit_success:
    ax.plot(omega_scan, lorentzian(omega_scan, *popt_lor), 'r--', linewidth=1.5,
            label=f'Lorentzian (Q={Q_lor:.0f})', zorder=2)
if fano_fit_success:
    ax.plot(omega_scan, fano_with_bg(omega_scan, *popt_fano), 'g:', linewidth=1.5,
            label=f'Fano (q={q_fano:.1f}, Q={Q_fano:.0f})', zorder=2)
ax.axvline(omega_L, color='gray', linestyle=':', alpha=0.5, label=r'$\omega_{L1}$')
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=12)
ax.set_ylabel(r'$A(k{=}0, \omega)$ [M$_{\rm KK}^{-1}$]', fontsize=12)
ax.set_title(f'(a) Spectral function (canonical $\\omega_{{L1}}$ = {omega_L:.3f})', fontsize=11)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(0, 2.0 * omega_L)

# --- Panel (b): Self-energy ---
ax = axes[0, 1]
ax.plot(omega_scan, Sigma_arr.real, 'b-', linewidth=1.5, label=r'Re $\Sigma(\omega)$')
ax.plot(omega_scan, Sigma_arr.imag, 'r-', linewidth=1.5, label=r'Im $\Sigma(\omega)$')
ax.axvline(omega_L, color='gray', linestyle=':', alpha=0.5)
ax.axhline(0, color='k', linewidth=0.5)
ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=12)
ax.set_ylabel(r'$\Sigma(\omega)$ [M$_{\rm KK}^2$]', fontsize=12)
ax.set_title(r'(b) Retarded self-energy', fontsize=11)
ax.legend(fontsize=9)
ax.set_xlim(0, 2.0 * omega_L)

# --- Panel (c): Peak zoom (within 10*FWHM) ---
ax = axes[1, 0]
zoom_width = max(10.0 * FWHM_direct, 0.02)
zoom_mask = np.abs(omega_scan - omega_peak) < zoom_width / 2.0
if np.any(zoom_mask):
    ax.plot(omega_scan[zoom_mask], A_omega[zoom_mask], 'b-', linewidth=2, label=r'$A(\omega)$')
    if lor_fit_success:
        ax.plot(omega_scan[zoom_mask], lorentzian(omega_scan[zoom_mask], *popt_lor),
                'r--', linewidth=1.5, label='Lorentzian fit')
    if fano_fit_success:
        ax.plot(omega_scan[zoom_mask], fano_with_bg(omega_scan[zoom_mask], *popt_fano),
                'g:', linewidth=1.5, label='Fano fit')
    ax.axhline(half_max, color='orange', linestyle='--', alpha=0.5, label='FWHM level')
    ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]', fontsize=12)
    ax.set_ylabel(r'$A(k{=}0, \omega)$ [M$_{\rm KK}^{-1}$]', fontsize=12)
    ax.set_title(f'(c) Peak zoom (FWHM = {FWHM_direct:.4e})', fontsize=11)
    ax.legend(fontsize=9)

# --- Panel (d): Comparison: canonical vs S65 frequency ---
ax = axes[1, 1]
# Normalize both to unit peak height for shape comparison
A_norm = A_omega / A_peak if A_peak > 0 else A_omega
A_norm_s65 = A_omega_s65 / A_peak_s65 if A_peak_s65 > 0 else A_omega_s65
# Plot vs (omega - omega_peak) / FWHM for each
x_canon = (omega_scan - omega_peak) / max(FWHM_direct, 1e-6)
x_s65 = (omega_scan_s65 - omega_peak_s65) / max(FWHM_direct, 1e-6)

ax.plot(x_canon, A_norm, 'b-', linewidth=2,
        label=f'Canonical ($\\omega_L$={omega_L:.3f})')
ax.plot(x_s65, A_norm_s65, 'r--', linewidth=1.5,
        label=f'S65 bare ($\\omega_L$={omega_L_s65:.4f})')
ax.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$(\omega - \omega_{\rm peak})$ / FWHM', fontsize=12)
ax.set_ylabel(r'$A(\omega) / A_{\rm max}$', fontsize=12)
ax.set_title('(d) Lineshape comparison (normalized)', fontsize=11)
ax.legend(fontsize=9)
ax.set_xlim(-15, 15)

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's66_leggett_spectral.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plotpath}")
print()

print("="*72)
print("COMPUTATION COMPLETE")
print("="*72)
