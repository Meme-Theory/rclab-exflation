#!/usr/bin/env python3
"""
BETTI-FISHER-70: Persistent Betti Number Forecast for FW vs LCDM
==================================================================
Session 70, Wave 4-F | Agent: Cosmic-Web-Theorist
Gate: BETTI-FISHER-70 — INFO: Report SNR for FW/LCDM discrimination

Computes the expected persistent Betti numbers beta_k(nu) for Gaussian
random fields with LCDM and framework power spectra, then derives the
Fisher information for discriminating the two cosmologies using a
Euclid-like survey volume.

The framework predicts sigma_8 = 0.793 (vs 0.811), n_s = 0.9595 (vs 0.9649),
and w_0 = -0.918 (vs -1.0).  The power spectrum is suppressed by
(sigma_8^FW / sigma_8^LCDM)^2 = 0.955 at fixed shape.

Method:
  1. Feldbrugge+2019 / Adler-Taylor (2007) / Pranav+2019 scaling:
     Expected Betti number densities for a 3D Gaussian random field
     smoothed at scale R:

       beta_k(nu; R) = A_k(R) * H_{d-k-1}(nu) * phi(nu)

     where nu = delta/sigma_0 is the density threshold in sigma units,
     phi(nu) = exp(-nu^2/2)/sqrt(2*pi) is the Gaussian PDF,
     H_n is the Hermite polynomial (probabilist's convention),
     and the amplitude A_k(R) depends on spectral moments
     sigma_j^2 = integral k^{2j} P(k) W^2(kR) dk.

  2. For k=0 (peaks/components), k=1 (tunnels), k=2 (voids) in d=3:
       beta_0(nu) ~ (sigma_2/sigma_1)^3 * (nu^2 - 1) * phi(nu)  [2-saddles ≈ peaks]
       beta_1(nu) ~ (sigma_1/sigma_0)^2 * (sigma_2/sigma_1) * nu * phi(nu)
       beta_2(nu) ~ (sigma_0/sigma_1)^0 * (sigma_1/sigma_2) * phi(nu)  [voids]

     More precisely, the Gaussian Kinematic Formula gives the Euler
     characteristic density:

       chi(nu) = beta_0 - beta_1 + beta_2

     and the individual Betti numbers are obtained from the Morse
     inequalities and the critical point density decomposition
     (Feldbrugge+2019, Pranav+2019 Sec. 4):

       n_max(nu)    = A_3 * (nu^3 - 3*nu) * phi(nu)  [local maxima → peaks]
       n_saddle2(nu) = A_3 * 3*(nu - nu^3/3) * phi(nu)  [2-saddles]
       n_saddle1(nu) = A_3 * 3*(nu^3/3 - nu) * phi(nu)  [1-saddles]
       n_min(nu)    = A_3 * (3*nu - nu^3) * phi(nu)  [local minima → voids]

     where A_3 = (1/(2*pi)^2) * (sigma_2 / (3*sigma_0))^{3/2}
     is the Kac-Rice density normalization for 3D.

     The Betti numbers relate to critical point counts via Morse theory:
       beta_0(nu) ≈ n_max(nu)  for nu >> 0 (high thresholds, isolated peaks)
       beta_2(nu) ≈ n_min(-nu) for nu << 0 (low thresholds, isolated voids)
     with corrections from the Morse-Smale complex at intermediate thresholds.

  3. Fisher information for sigma_8 discrimination:
     F = V_survey * integral d(nu) [d(beta)/d(sigma_8)]^2 / Var(beta)

  4. SNR = sqrt(F) * |sigma_8^FW - sigma_8^LCDM|

References:
  - Adler & Taylor, "Random Fields and Geometry" (2007), Ch. 11-12
  - Feldbrugge, "Topological Data Analysis of the Cosmic Web" (2019, PhD thesis)
  - Pranav et al., "Topology of the Cosmic Web" (2017, MNRAS) [Pr28]
  - Matsubara, "Statistics of Smoothed Cosmic Fields" (2003, ApJ 584, 1)
  - Doroshkevich (1970): original Gaussian field extremum statistics
  - Bardeen, Bond, Kaiser, Efstathiou (1986) [BBKS]: peak statistics formalism
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.special import erfc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (, k_pivot_planck, ns_framework, planck_ns
    Omega_m, Omega_b, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, PI, Omega_r
)

# NumPy 2.x compatibility: trapz -> trapezoid
if hasattr(np, 'trapezoid'):
    _trapz = np.trapezoid
else:
    _trapz = _trapz

# ============================================================================
#  Section 1: Cosmological Parameters
# ============================================================================

n_s_LCDM = planck_ns  # canonical alias (was: = 0.9649)
n_s_FW = ns_framework  # canonical alias (was: = 0.9595)
k_pivot = k_pivot_planck  # canonical alias (was: = 0.05)
h = H_0_km_s_Mpc / 100.0   # = 0.674

# Framework cosmology
# w0_FW = -0.918              # Volovik effacement residual (S58 W0-4)  # S72: now imported from canonical_constants
sigma8_FW = 0.793           # Framework sigma_8 (S69 W2-D)  # (local)

# LCDM cosmology
# w0_LCDM = -1.0  # S72: now imported from canonical_constants
sigma8_LCDM = sigma_8       # Planck 2018 = 0.811

# Survey parameters
V_survey_Gpc3 = 10.0        # Euclid-like survey volume (10 Gpc^3 comoving)  # (local)
V_survey_hmpc3 = V_survey_Gpc3 * (1e3 * h)**3  # h^{-3} Mpc^3

# Smoothing scales to probe (h^{-1} Mpc)
R_smooth_arr = np.array([5.0, 10.0, 15.0, 20.0, 30.0])  # h^{-1} Mpc

print("=" * 72)
print("BETTI-FISHER-70: Persistent Betti Number Forecast")
print("=" * 72)
print(f"  LCDM: sigma_8 = {sigma8_LCDM}, n_s = {n_s_LCDM}, w = {w0_LCDM}")
print(f"  FW:   sigma_8 = {sigma8_FW},   n_s = {n_s_FW},   w_0 = {w0_FW}")
print(f"  (sigma_8^FW / sigma_8^LCDM)^2 = {(sigma8_FW/sigma8_LCDM)**2:.4f}")
print(f"  Survey volume: {V_survey_Gpc3} Gpc^3 = {V_survey_hmpc3:.3e} (h^-1 Mpc)^3")
print()

# ============================================================================
#  Section 2: Power Spectrum and Spectral Moments
# ============================================================================

def eisenstein_hu_no_wiggle(k_hmpc, Omega_m_val, Omega_b_val, h_val, n_s_val):
    """
    Eisenstein & Hu (1998) no-wiggle transfer function.
    k_hmpc: wavenumber in h/Mpc
    Returns: T(k)^2 * k^{n_s} * (k/k_pivot_hmpc)^0 as dimensionless P(k) shape
    """
    theta_CMB = 2.7255 / 2.7  # T_CMB / 2.7
    Omega_m_h2 = Omega_m_val * h_val**2
    Omega_b_h2 = Omega_b_val * h_val**2

    # Sound horizon
    s = 44.5 * np.log(9.83 / Omega_m_h2) / np.sqrt(1 + 10 * Omega_b_h2**0.75)

    # Shape parameter
    alpha_Gamma = 1 - 0.328 * np.log(431 * Omega_m_h2) * (Omega_b_val / Omega_m_val) \
                  + 0.38 * np.log(22.3 * Omega_m_h2) * (Omega_b_val / Omega_m_val)**2
    Gamma_eff = Omega_m_val * h_val * (alpha_Gamma + (1 - alpha_Gamma) / (1 + (0.43 * k_hmpc * s)**4))

    # Transfer function (Eq. 29 of EH98)
    q = k_hmpc * theta_CMB**2 / Gamma_eff
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731 / (1 + 62.5 * q)
    T0 = L / (L + C * q**2)

    return T0


def compute_Pk_shape(k_arr, Omega_m_val, Omega_b_val, h_val, n_s_val):
    """
    Compute P(k) shape (unnormalized) including primordial tilt.
    k_arr: in h/Mpc
    Returns: P(k) proportional to A_s * k^{n_s} * T(k)^2
    """
    k_pivot_hmpc = k_pivot / h_val  # Convert Mpc^{-1} to h/Mpc
    T = eisenstein_hu_no_wiggle(k_arr, Omega_m_val, Omega_b_val, h_val, n_s_val)
    # Primordial power spectrum * transfer function squared
    Pk = (k_arr / k_pivot_hmpc)**(n_s_val - 1) * k_arr * T**2
    return Pk


def sigma_R_squared(R, Omega_m_val, Omega_b_val, h_val, n_s_val, j=0):
    """
    Compute the j-th spectral moment sigma_j^2(R) = integral k^{2j} P(k) W^2(kR) dk / (2pi^2).
    W(x) = 3*(sin(x) - x*cos(x))/x^3 is the top-hat window.
    j=0: sigma_0^2 (variance)
    j=1: sigma_1^2 (first spectral moment)
    j=2: sigma_2^2 (second spectral moment)
    """
    def integrand(lnk):
        k = np.exp(lnk)
        x = k * R
        if x < 1e-6:
            W = 1.0 - x**2 / 10.0  # (local)
        else:
            W = 3 * (np.sin(x) - x * np.cos(x)) / x**3  # (local)
        Pk = compute_Pk_shape(np.array([k]), Omega_m_val, Omega_b_val, h_val, n_s_val)[0]
        return k**(2*j) * Pk * W**2 * k  # k from d(lnk) = dk/k

    lnk_min = np.log(1e-4)
    lnk_max = np.log(1e2)
    result, _ = quad(integrand, lnk_min, lnk_max, limit=500, epsrel=1e-6)
    return result / (2 * PI**2)


def normalize_sigma8(R8, Omega_m_val, Omega_b_val, h_val, n_s_val, target_sigma8):
    """
    Find the normalization constant A such that sigma(R=8 h^{-1} Mpc) = target_sigma8.
    Returns A (multiply unnormalized P(k) by A to get physical P(k)).
    """
    sigma0_sq_unnorm = sigma_R_squared(R8, Omega_m_val, Omega_b_val, h_val, n_s_val, j=0)
    A = target_sigma8**2 / sigma0_sq_unnorm
    return A


# ============================================================================
#  Section 3: Betti Number Densities (Gaussian Random Field)
# ============================================================================

def phi_gauss(nu):
    """Standard Gaussian PDF."""
    return np.exp(-nu**2 / 2) / np.sqrt(2 * PI)


def compute_betti_densities(nu_arr, sigma0, sigma1, sigma2):
    """
    Compute expected Betti number densities for a 3D Gaussian random field.

    Uses the Gaussian Kinematic Formula decomposition (Adler & Taylor 2007)
    and Morse theory critical point densities (Bardeen+1986, Feldbrugge 2019).

    The spectral parameter gamma = sigma_1^2 / (sigma_0 * sigma_2) controls
    the shape.  For gamma -> 1 (narrow spectrum), peaks are well-separated.

    The Kac-Rice formula for the expected number density of critical points
    of a 3D isotropic Gaussian field at level nu:

      n_crit(nu) = (1/(2*pi)^2) * (sigma_2/(3*sigma_0))^{3/2} *
                   |det(H)| averaged over Hessian eigenvalues

    For practical Betti number computation, we use the decomposition into
    critical point types (Pranav+2019, Feldbrugge 2019):

      n_{index-k}(nu) = A_3 * f_k(nu) * phi(nu)

    where A_3 = (1/(2pi)^2) * (sigma_2 / (3*sigma_0))^{3/2} is the
    overall density normalization, and f_k(nu) encodes the threshold
    dependence for each critical point type.

    For the superlevel set filtration:
      beta_0(nu): counts connected components above threshold nu
      beta_1(nu): counts 1-cycles (tunnels/loops) above threshold nu
      beta_2(nu): counts 2-cycles (enclosed voids) above threshold nu

    At high positive nu: beta_0 ~ n_max (isolated peaks)
    At low negative nu: beta_2 ~ n_min (isolated voids)

    The Feldbrugge+2019 scaling (simplified for forecasting):
      beta_0(nu) ~ A_3 * gamma^3 * H_2(nu) * phi(nu) * Theta(nu)
      beta_1(nu) ~ A_3 * gamma * (1 - gamma^2) * |nu| * phi(nu)
      beta_2(nu) ~ A_3 * (1-gamma^2)^{3/2}/gamma^3 * H_2(-nu) * phi(-nu) * Theta(-nu)

    where H_2(x) = x^2 - 1 is the 2nd Hermite polynomial and
    Theta is a smoothed Heaviside capturing the threshold behavior.

    For Fisher forecasting, the key is the DERIVATIVE d(beta_k)/d(sigma_8),
    which enters through the spectral moments sigma_j.
    """
    gamma = sigma1**2 / (sigma0 * sigma2)  # spectral parameter

    # Kac-Rice normalization for 3D
    A3 = (1.0 / (2*PI)**2) * (sigma2 / (3*sigma0))**(1.5)

    # Hermite polynomial H_2(x) = x^2 - 1
    H2_nu = nu_arr**2 - 1
    H2_mnu = nu_arr**2 - 1  # H_2(-nu) = H_2(nu) since H_2 is even

    phi_nu = phi_gauss(nu_arr)

    # --- beta_0: connected components (superlevel set) ---
    # Dominated by peaks at high nu.  The superlevel set filtration
    # gives beta_0(nu) = cumulative peak count above threshold nu.
    # For Gaussian fields, the expected density scales as:
    #   beta_0(nu) ≈ A_3 * gamma^3 * (nu^2 - 1) * phi(nu) for nu > 0
    # This follows from the BBKS peak density with the spectral
    # parameter encoding the correlation between field value and curvature.
    beta_0 = np.zeros_like(nu_arr)
    mask_pos = nu_arr > 0
    beta_0[mask_pos] = A3 * gamma**3 * np.maximum(H2_nu[mask_pos], 0) * phi_nu[mask_pos]

    # --- beta_1: tunnels/loops ---
    # The 1-cycles peak at intermediate thresholds (near nu = 0).
    # From Morse theory: beta_1 ≈ cumulative (2-saddles - mergers).
    # For Gaussian fields, the density peaks near nu = 0 and scales as:
    #   beta_1(nu) ≈ A_3 * gamma * (1 - gamma^2) * exp(-nu^2/2) / sqrt(2*pi)
    # with a broad maximum at nu ~ 0.
    # More precisely (Pranav+2019 Fig. 6, Feldbrugge 2019 Sec. 4.3):
    beta_1 = A3 * gamma * (1 - gamma**2) * phi_nu * (1 + 0.5 * nu_arr**2)
    # The (1 + 0.5*nu^2) correction captures the observed broadening
    # relative to a pure Gaussian envelope.
    beta_1 = np.maximum(beta_1, 0)

    # --- beta_2: enclosed voids ---
    # Dominated by field minima at low nu (nu << 0).
    # Symmetric to beta_0 under nu -> -nu reflection:
    #   beta_2(nu) ≈ A_3 * (1-gamma^2)^{3/2}/gamma^3 * (nu^2-1) * phi(nu)  for nu < 0
    # but for the superlevel set, voids appear as threshold drops below minima:
    beta_2 = np.zeros_like(nu_arr)
    mask_neg = nu_arr < 0
    beta_2[mask_neg] = A3 * ((1 - gamma**2)**(1.5) / gamma**3) * \
                       np.maximum(H2_mnu[mask_neg], 0) * phi_nu[mask_neg]

    # Units: A3 has dimensions of [length]^{-3} (from sigma_2/sigma_0 ratio).
    # To get dimensionless number per (h^{-1} Mpc)^3, sigma_j must be in
    # consistent h/Mpc units.  We handle normalization via the sigma_j inputs.

    return beta_0, beta_1, beta_2, A3, gamma


# ============================================================================
#  Section 4: Persistence Diagram (Birth-Death Pairs)
# ============================================================================

def compute_persistence_diagram(nu_arr, beta_0, beta_1, beta_2):
    """
    Compute a simplified persistence diagram from Betti curves.

    The persistence diagram consists of (birth, death) pairs for each
    topological feature.  For a Gaussian field with known Betti curves,
    we model the persistence distribution statistically:

    - beta_0 features: born at nu_birth ~ Gaussian(nu_peak, sigma_persist)
      and die at nu_death < nu_birth (merging into larger component)
    - beta_2 features: born at nu_birth (threshold rises above void minimum)
      and die at nu_death > nu_birth (void fills in)

    For Fisher forecasting, the key quantity is the TOTAL persistence
    (sum of all |birth - death| values), which scales with the number
    of topological features and their characteristic lifetimes.

    Returns: persistence statistics for each Betti number.
    """
    # Integrate Betti curves to get total feature counts
    dnu = nu_arr[1] - nu_arr[0]

    # Total expected number of features per unit volume is the
    # integral of the Betti curve over threshold
    N_beta0 = _trapz(beta_0, nu_arr)
    N_beta1 = _trapz(beta_1, nu_arr)
    N_beta2 = _trapz(beta_2, nu_arr)

    # Mean persistence (birth-death interval) scales with sigma_0 / sigma_2
    # (the characteristic width of the Betti curves).
    # For a Gaussian field smoothed at R, the typical persistence is
    # Delta_nu ~ 1 (in sigma units) for well-resolved features.

    # The RMS persistence for index-k features:
    # <(b-d)^2>^{1/2} ~ sigma_0 * integral(nu^2 * beta_k(nu)) / integral(beta_k(nu))
    if N_beta0 > 0:
        nu_mean_0 = _trapz(nu_arr * beta_0, nu_arr) / N_beta0
        nu_rms_0 = np.sqrt(_trapz((nu_arr - nu_mean_0)**2 * beta_0, nu_arr) / N_beta0)
    else:
        nu_mean_0, nu_rms_0 = 0, 0

    if N_beta1 > 0:
        nu_mean_1 = _trapz(nu_arr * beta_1, nu_arr) / N_beta1
        nu_rms_1 = np.sqrt(_trapz((nu_arr - nu_mean_1)**2 * beta_1, nu_arr) / N_beta1)
    else:
        nu_mean_1, nu_rms_1 = 0, 0

    if N_beta2 > 0:
        nu_mean_2 = _trapz(nu_arr * beta_2, nu_arr) / N_beta2
        nu_rms_2 = np.sqrt(_trapz((nu_arr - nu_mean_2)**2 * beta_2, nu_arr) / N_beta2)
    else:
        nu_mean_2, nu_rms_2 = 0, 0

    return {
        'N_beta0': N_beta0, 'N_beta1': N_beta1, 'N_beta2': N_beta2,
        'nu_mean_0': nu_mean_0, 'nu_rms_0': nu_rms_0,
        'nu_mean_1': nu_mean_1, 'nu_rms_1': nu_rms_1,
        'nu_mean_2': nu_mean_2, 'nu_rms_2': nu_rms_2,
    }


# ============================================================================
#  Section 5: Fisher Information for FW/LCDM Discrimination
# ============================================================================

def fisher_betti(R, nu_arr, cosmo_fid, cosmo_alt, V_survey):
    """
    Compute Fisher information for discriminating two cosmologies
    using persistent Betti number statistics.

    cosmo_fid, cosmo_alt: dicts with keys {Omega_m, Omega_b, h, n_s, sigma8}
    V_survey: survey volume in (h^{-1} Mpc)^3

    KEY PHYSICAL POINT: Betti numbers are measured at fixed PHYSICAL
    density threshold delta (e.g., delta = 1, 2, 3...), not at fixed nu.
    When sigma_8 changes, sigma_0(R) changes, so the same physical delta
    maps to a DIFFERENT nu = delta / sigma_0.  This is where sigma_8
    sensitivity enters.

    For cosmology A with sigma_0^A, the Betti density at physical
    threshold delta is:
      beta_k(delta; A) = beta_k(nu = delta / sigma_0^A; spectral shape A)

    Two cosmologies differ at the same physical delta because:
      1. sigma_0 differs (sigma_8 shift): different nu at same delta
      2. Spectral shape differs (n_s shift): different gamma, different
         functional form of beta_k(nu)

    The Fisher information in physical-delta space:
      F_k = V * integral d(delta) [Delta(beta_k)]^2 / beta_k_fid
    where Delta(beta_k) = beta_k(delta; alt) - beta_k(delta; fid).
    """
    # Compute spectral moments for fiducial cosmology
    A_fid = normalize_sigma8(8.0, cosmo_fid['Omega_m'], cosmo_fid['Omega_b'],
                             cosmo_fid['h'], cosmo_fid['n_s'], cosmo_fid['sigma8'])

    sigma0_fid_sq = A_fid * sigma_R_squared(R, cosmo_fid['Omega_m'], cosmo_fid['Omega_b'],
                                             cosmo_fid['h'], cosmo_fid['n_s'], j=0)
    sigma1_fid_sq = A_fid * sigma_R_squared(R, cosmo_fid['Omega_m'], cosmo_fid['Omega_b'],
                                             cosmo_fid['h'], cosmo_fid['n_s'], j=1)
    sigma2_fid_sq = A_fid * sigma_R_squared(R, cosmo_fid['Omega_m'], cosmo_fid['Omega_b'],
                                             cosmo_fid['h'], cosmo_fid['n_s'], j=2)

    sigma0_fid = np.sqrt(sigma0_fid_sq)
    sigma1_fid = np.sqrt(sigma1_fid_sq)
    sigma2_fid = np.sqrt(sigma2_fid_sq)

    # Compute spectral moments for alternative cosmology
    A_alt = normalize_sigma8(8.0, cosmo_alt['Omega_m'], cosmo_alt['Omega_b'],
                             cosmo_alt['h'], cosmo_alt['n_s'], cosmo_alt['sigma8'])

    sigma0_alt_sq = A_alt * sigma_R_squared(R, cosmo_alt['Omega_m'], cosmo_alt['Omega_b'],
                                             cosmo_alt['h'], cosmo_alt['n_s'], j=0)
    sigma1_alt_sq = A_alt * sigma_R_squared(R, cosmo_alt['Omega_m'], cosmo_alt['Omega_b'],
                                             cosmo_alt['h'], cosmo_alt['n_s'], j=1)
    sigma2_alt_sq = A_alt * sigma_R_squared(R, cosmo_alt['Omega_m'], cosmo_alt['Omega_b'],
                                             cosmo_alt['h'], cosmo_alt['n_s'], j=2)

    sigma0_alt = np.sqrt(sigma0_alt_sq)
    sigma1_alt = np.sqrt(sigma1_alt_sq)
    sigma2_alt = np.sqrt(sigma2_alt_sq)

    # --- Betti numbers in NU space (for plotting) ---
    b0_fid, b1_fid, b2_fid, A3_fid, gamma_fid = compute_betti_densities(
        nu_arr, sigma0_fid, sigma1_fid, sigma2_fid)
    b0_alt, b1_alt, b2_alt, A3_alt, gamma_alt = compute_betti_densities(
        nu_arr, sigma0_alt, sigma1_alt, sigma2_alt)

    # Persistence statistics (in nu space)
    persist_fid = compute_persistence_diagram(nu_arr, b0_fid, b1_fid, b2_fid)
    persist_alt = compute_persistence_diagram(nu_arr, b0_alt, b1_alt, b2_alt)

    # --- Fisher information in PHYSICAL DELTA space ---
    # Use a grid of physical density contrast delta
    delta_arr = np.linspace(-3.0 * sigma0_fid, 4.0 * sigma0_fid, 1001)
    ddelta = delta_arr[1] - delta_arr[0]

    # Convert to nu for each cosmology
    nu_fid_arr = delta_arr / sigma0_fid
    nu_alt_arr = delta_arr / sigma0_alt  # DIFFERENT nu at same delta!

    # Betti densities at physical delta (evaluated at cosmology-specific nu)
    b0_fid_phys, b1_fid_phys, b2_fid_phys, _, _ = compute_betti_densities(
        nu_fid_arr, sigma0_fid, sigma1_fid, sigma2_fid)
    b0_alt_phys, b1_alt_phys, b2_alt_phys, _, _ = compute_betti_densities(
        nu_alt_arr, sigma0_alt, sigma1_alt, sigma2_alt)

    F_beta0 = 0.0  # (local)
    F_beta1 = 0.0  # (local)
    F_beta2 = 0.0  # (local)
    eps_floor = 1e-30

    for i in range(len(delta_arr)):
        # beta_0 contribution
        if b0_fid_phys[i] > eps_floor:
            db0 = b0_alt_phys[i] - b0_fid_phys[i]
            # Variance: Poisson-like, Var(N) ~ N in volume V * ddelta
            # N_expected = beta_k * V * ddelta (number of features in
            # threshold bin ddelta)
            # Var(N) ~ N -> Var(beta_k * V * ddelta) ~ beta_k * V * ddelta
            # -> Var(beta_k) ~ beta_k / (V * ddelta)
            # chi^2 contribution = V * ddelta * db0^2 / b0_fid
            F_beta0 += V_survey * ddelta * db0**2 / (b0_fid_phys[i] + eps_floor)

        # beta_1 contribution
        if b1_fid_phys[i] > eps_floor:
            db1 = b1_alt_phys[i] - b1_fid_phys[i]
            F_beta1 += V_survey * ddelta * db1**2 / (b1_fid_phys[i] + eps_floor)

        # beta_2 contribution
        if b2_fid_phys[i] > eps_floor:
            db2 = b2_alt_phys[i] - b2_fid_phys[i]
            F_beta2 += V_survey * ddelta * db2**2 / (b2_fid_phys[i] + eps_floor)

    F_total = F_beta0 + F_beta1 + F_beta2

    return {
        'F_beta0': F_beta0, 'F_beta1': F_beta1, 'F_beta2': F_beta2,
        'F_total': F_total,
        'SNR_beta0': np.sqrt(F_beta0), 'SNR_beta1': np.sqrt(F_beta1),
        'SNR_beta2': np.sqrt(F_beta2), 'SNR_total': np.sqrt(F_total),
        'sigma0_fid': sigma0_fid, 'sigma1_fid': sigma1_fid, 'sigma2_fid': sigma2_fid,
        'sigma0_alt': sigma0_alt, 'sigma1_alt': sigma1_alt, 'sigma2_alt': sigma2_alt,
        'A3_fid': A3_fid, 'gamma_fid': gamma_fid,
        'A3_alt': A3_alt, 'gamma_alt': gamma_alt,
        'b0_fid': b0_fid, 'b1_fid': b1_fid, 'b2_fid': b2_fid,
        'b0_alt': b0_alt, 'b1_alt': b1_alt, 'b2_alt': b2_alt,
        'persist_fid': persist_fid, 'persist_alt': persist_alt,
    }


# ============================================================================
#  Section 6: Main Computation
# ============================================================================

# Threshold array
nu_arr = np.linspace(-4.0, 4.0, 1001)

# Cosmology dicts
cosmo_LCDM = {
    'Omega_m': Omega_m, 'Omega_b': Omega_b, 'h': h,
    'n_s': n_s_LCDM, 'sigma8': sigma8_LCDM
}
cosmo_FW = {
    'Omega_m': Omega_m, 'Omega_b': Omega_b, 'h': h,
    'n_s': n_s_FW, 'sigma8': sigma8_FW
}

# Run Fisher analysis at each smoothing scale
print("=" * 72)
print("  SPECTRAL MOMENTS AND BETTI NUMBER ANALYSIS")
print("=" * 72)

results_all = {}
snr_table = []

for R in R_smooth_arr:
    print(f"\n--- R = {R:.1f} h^-1 Mpc ---")

    res = fisher_betti(R, nu_arr, cosmo_LCDM, cosmo_FW, V_survey_hmpc3)
    results_all[R] = res

    print(f"  LCDM spectral moments at R={R}:")
    print(f"    sigma_0 = {res['sigma0_fid']:.6f}")
    print(f"    sigma_1 = {res['sigma1_fid']:.6f}")
    print(f"    sigma_2 = {res['sigma2_fid']:.6f}")
    print(f"    gamma   = {res['gamma_fid']:.6f}")
    print(f"    A_3     = {res['A3_fid']:.6e} (h/Mpc)^3")

    print(f"  FW spectral moments at R={R}:")
    print(f"    sigma_0 = {res['sigma0_alt']:.6f}")
    print(f"    sigma_1 = {res['sigma1_alt']:.6f}")
    print(f"    sigma_2 = {res['sigma2_alt']:.6f}")
    print(f"    gamma   = {res['gamma_alt']:.6f}")
    print(f"    A_3     = {res['A3_alt']:.6e} (h/Mpc)^3")

    # Fractional shifts
    dsig0 = (res['sigma0_alt'] - res['sigma0_fid']) / res['sigma0_fid']
    dsig1 = (res['sigma1_alt'] - res['sigma1_fid']) / res['sigma1_fid']
    dsig2 = (res['sigma2_alt'] - res['sigma2_fid']) / res['sigma2_fid']
    dA3 = (res['A3_alt'] - res['A3_fid']) / res['A3_fid']
    dgam = (res['gamma_alt'] - res['gamma_fid']) / res['gamma_fid']
    print(f"  Fractional shifts (FW - LCDM) / LCDM:")
    print(f"    delta(sigma_0) = {dsig0:+.4f} ({dsig0*100:+.2f}%)")
    print(f"    delta(sigma_1) = {dsig1:+.4f} ({dsig1*100:+.2f}%)")
    print(f"    delta(sigma_2) = {dsig2:+.4f} ({dsig2*100:+.2f}%)")
    print(f"    delta(A_3)     = {dA3:+.4f} ({dA3*100:+.2f}%)")
    print(f"    delta(gamma)   = {dgam:+.6f} ({dgam*100:+.4f}%)")

    # Persistence statistics
    pf = res['persist_fid']
    pa = res['persist_alt']
    print(f"  Persistence stats (LCDM):")
    print(f"    N_beta0 = {pf['N_beta0']:.6e}, N_beta1 = {pf['N_beta1']:.6e}, N_beta2 = {pf['N_beta2']:.6e}")
    print(f"  Persistence stats (FW):")
    print(f"    N_beta0 = {pa['N_beta0']:.6e}, N_beta1 = {pa['N_beta1']:.6e}, N_beta2 = {pa['N_beta2']:.6e}")

    # Fisher / SNR
    print(f"  Fisher information (V = {V_survey_Gpc3} Gpc^3):")
    print(f"    F_beta0 = {res['F_beta0']:.4e}")
    print(f"    F_beta1 = {res['F_beta1']:.4e}")
    print(f"    F_beta2 = {res['F_beta2']:.4e}")
    print(f"    F_total = {res['F_total']:.4e}")
    print(f"  SNR for FW/LCDM discrimination:")
    print(f"    SNR(beta_0) = {res['SNR_beta0']:.3f}")
    print(f"    SNR(beta_1) = {res['SNR_beta1']:.3f}")
    print(f"    SNR(beta_2) = {res['SNR_beta2']:.3f}")
    print(f"    SNR(total)  = {res['SNR_total']:.3f}")

    snr_table.append({
        'R': R,
        'SNR_beta0': res['SNR_beta0'],
        'SNR_beta1': res['SNR_beta1'],
        'SNR_beta2': res['SNR_beta2'],
        'SNR_total': res['SNR_total'],
        'gamma_fid': res['gamma_fid'],
        'dsig0_pct': dsig0 * 100,
    })


# Combined SNR across all scales (independent scales)
F_combined = sum(results_all[R]['F_total'] for R in R_smooth_arr)
SNR_combined = np.sqrt(F_combined)

print("\n" + "=" * 72)
print("  COMBINED RESULTS ACROSS ALL SMOOTHING SCALES")
print("=" * 72)
print(f"\n  {'R (h/Mpc)':>10s} {'SNR(b0)':>10s} {'SNR(b1)':>10s} {'SNR(b2)':>10s} {'SNR(tot)':>10s} {'gamma':>8s} {'dsig0%':>8s}")
print("  " + "-" * 66)
for row in snr_table:
    print(f"  {row['R']:10.1f} {row['SNR_beta0']:10.3f} {row['SNR_beta1']:10.3f} {row['SNR_beta2']:10.3f} {row['SNR_total']:10.3f} {row['gamma_fid']:8.4f} {row['dsig0_pct']:+8.2f}")
print("  " + "-" * 66)
print(f"  {'Combined':>10s} {'':>10s} {'':>10s} {'':>10s} {SNR_combined:10.3f}")

# Decompose SNR by parameter
# sigma_8 contribution vs n_s contribution
# Run with only sigma_8 shifted (n_s held at LCDM)
cosmo_FW_sig8_only = {
    'Omega_m': Omega_m, 'Omega_b': Omega_b, 'h': h,
    'n_s': n_s_LCDM, 'sigma8': sigma8_FW
}
cosmo_FW_ns_only = {
    'Omega_m': Omega_m, 'Omega_b': Omega_b, 'h': h,
    'n_s': n_s_FW, 'sigma8': sigma8_LCDM
}

print("\n" + "=" * 72)
print("  PARAMETER DECOMPOSITION: sigma_8 vs n_s contributions")
print("=" * 72)

R_ref = 10.0  # Reference scale for decomposition  # (local)
res_sig8 = fisher_betti(R_ref, nu_arr, cosmo_LCDM, cosmo_FW_sig8_only, V_survey_hmpc3)
res_ns = fisher_betti(R_ref, nu_arr, cosmo_LCDM, cosmo_FW_ns_only, V_survey_hmpc3)
res_both = results_all[R_ref]

print(f"\n  At R = {R_ref} h^-1 Mpc:")
print(f"    sigma_8 only (0.811 -> 0.793): SNR = {res_sig8['SNR_total']:.3f}")
print(f"    n_s only     (0.9649 -> 0.9595): SNR = {res_ns['SNR_total']:.3f}")
print(f"    Both shifts:                     SNR = {res_both['SNR_total']:.3f}")
print(f"    Quadrature sum:                  SNR = {np.sqrt(res_sig8['SNR_total']**2 + res_ns['SNR_total']**2):.3f}")

# ============================================================================
#  Section 7: Plotting
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('BETTI-FISHER-70: Persistent Betti Number Forecast\n'
             f'LCDM ($\\sigma_8$={sigma8_LCDM}, $n_s$={n_s_LCDM}) vs '
             f'FW ($\\sigma_8$={sigma8_FW}, $n_s$={n_s_FW})',
             fontsize=13, fontweight='bold')

# --- Panel 1: Betti curves at R = 10 h^{-1} Mpc ---
ax = axes[0, 0]
R_plot = 10.0  # (local)
res = results_all[R_plot]
ax.plot(nu_arr, res['b0_fid'], 'b-', lw=1.5, label=r'$\beta_0$ LCDM')
ax.plot(nu_arr, res['b0_alt'], 'b--', lw=1.5, label=r'$\beta_0$ FW')
ax.plot(nu_arr, res['b1_fid'], 'r-', lw=1.5, label=r'$\beta_1$ LCDM')
ax.plot(nu_arr, res['b1_alt'], 'r--', lw=1.5, label=r'$\beta_1$ FW')
ax.plot(nu_arr, res['b2_fid'], 'g-', lw=1.5, label=r'$\beta_2$ LCDM')
ax.plot(nu_arr, res['b2_alt'], 'g--', lw=1.5, label=r'$\beta_2$ FW')
ax.set_xlabel(r'$\nu = \delta / \sigma_0$', fontsize=12)
ax.set_ylabel(r'$\beta_k(\nu)$ density [(h/Mpc)$^3$]', fontsize=11)
ax.set_title(f'Betti Number Densities (R = {R_plot} h$^{{-1}}$ Mpc)', fontsize=11)
ax.legend(fontsize=8, ncol=2)
ax.set_yscale('log')
ymin_pos = min(res['b0_fid'][res['b0_fid'] > 0].min() if np.any(res['b0_fid'] > 0) else 1e-20,
               res['b1_fid'][res['b1_fid'] > 0].min() if np.any(res['b1_fid'] > 0) else 1e-20,
               res['b2_fid'][res['b2_fid'] > 0].min() if np.any(res['b2_fid'] > 0) else 1e-20)
ax.set_ylim(bottom=max(ymin_pos * 0.1, 1e-20))
ax.grid(True, alpha=0.3)

# --- Panel 2: Fractional difference (FW - LCDM) / LCDM ---
ax = axes[0, 1]
for R_plot in [5.0, 10.0, 20.0]:
    res = results_all[R_plot]
    # beta_1 fractional difference (most informative: spans all thresholds)
    mask = res['b1_fid'] > 1e-20
    if np.any(mask):
        frac_diff = (res['b1_alt'][mask] - res['b1_fid'][mask]) / res['b1_fid'][mask]
        ax.plot(nu_arr[mask], frac_diff * 100, label=f'R = {R_plot} h$^{{-1}}$ Mpc')
ax.set_xlabel(r'$\nu = \delta / \sigma_0$', fontsize=12)
ax.set_ylabel(r'$\Delta\beta_1 / \beta_1$ [%]', fontsize=11)
ax.set_title(r'Fractional $\beta_1$ Difference (FW $-$ LCDM)', fontsize=11)
ax.axhline(0, color='k', ls=':', lw=0.5)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel 3: SNR vs smoothing scale ---
ax = axes[1, 0]
R_arr_plot = [row['R'] for row in snr_table]
snr_b0 = [row['SNR_beta0'] for row in snr_table]
snr_b1 = [row['SNR_beta1'] for row in snr_table]
snr_b2 = [row['SNR_beta2'] for row in snr_table]
snr_tot = [row['SNR_total'] for row in snr_table]
ax.plot(R_arr_plot, snr_b0, 'bo-', label=r'SNR($\beta_0$)')
ax.plot(R_arr_plot, snr_b1, 'rs-', label=r'SNR($\beta_1$)')
ax.plot(R_arr_plot, snr_b2, 'g^-', label=r'SNR($\beta_2$)')
ax.plot(R_arr_plot, snr_tot, 'kD-', lw=2, label='SNR(total)')
ax.axhline(1.0, color='gray', ls='--', lw=1, label='SNR = 1')
ax.axhline(3.0, color='gray', ls=':', lw=1, label='SNR = 3')
ax.set_xlabel(r'Smoothing Scale R [h$^{-1}$ Mpc]', fontsize=12)
ax.set_ylabel('Signal-to-Noise Ratio', fontsize=11)
ax.set_title('FW/LCDM Discrimination SNR vs Scale', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel 4: Persistence diagram (schematic) ---
ax = axes[1, 1]
R_plot = 10.0  # (local)
res = results_all[R_plot]
pf = res['persist_fid']
pa = res['persist_alt']

# Draw schematic persistence diagram
# beta_0: peaks are born at high nu, die at lower nu
# beta_2: voids are born at low nu, die at higher nu
# The diagonal line represents zero persistence
ax.plot([-4, 4], [-4, 4], 'k-', lw=0.5, alpha=0.3)

# Schematic birth-death scatter from LCDM (Pranav+2017 style)
np.random.seed(42)
n_pts = 50  # (local)

# beta_0 features (peaks): born at high nu, die at lower nu
if pf['N_beta0'] > 0:
    births_0 = np.random.normal(pf['nu_mean_0'], pf['nu_rms_0'] * 0.5, n_pts)
    persist_0 = np.abs(np.random.exponential(pf['nu_rms_0'] * 0.3, n_pts))
    deaths_0 = births_0 - persist_0
    ax.scatter(births_0, deaths_0, c='blue', s=15, alpha=0.5, label=r'$\beta_0$ LCDM (peaks)')

# beta_2 features (voids): born at low nu, die at higher nu
if pf['N_beta2'] > 0:
    births_2 = np.random.normal(pf['nu_mean_2'], pf['nu_rms_2'] * 0.5, n_pts)
    persist_2 = np.abs(np.random.exponential(pf['nu_rms_2'] * 0.3, n_pts))
    deaths_2 = births_2 + persist_2
    ax.scatter(births_2, deaths_2, c='green', s=15, alpha=0.5, label=r'$\beta_2$ LCDM (voids)')

# Mark the shift for FW
if pa['N_beta0'] > 0:
    ax.axvline(pa['nu_mean_0'], color='blue', ls='--', lw=1, alpha=0.4, label=f'FW mean birth ($\\beta_0$)')
if pa['N_beta2'] > 0:
    ax.axvline(pa['nu_mean_2'], color='green', ls='--', lw=1, alpha=0.4, label=f'FW mean birth ($\\beta_2$)')

ax.set_xlabel(r'Birth threshold $\nu$', fontsize=12)
ax.set_ylabel(r'Death threshold $\nu$', fontsize=12)
ax.set_title(f'Schematic Persistence Diagram (R = {R_plot})', fontsize=11)
ax.legend(fontsize=8, loc='upper left')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.grid(True, alpha=0.3)

plt.tight_layout()
outdir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(outdir, 's70_betti_fisher.png'), dpi=150, bbox_inches='tight')
print(f"\nPlot saved: {os.path.join(outdir, 's70_betti_fisher.png')}")

# ============================================================================
#  Section 8: Gate Verdict and Summary
# ============================================================================

print("\n" + "=" * 72)
print("  GATE VERDICT: BETTI-FISHER-70")
print("=" * 72)

# Best single scale
best_R = max(snr_table, key=lambda x: x['SNR_total'])
print(f"\n  Best single-scale SNR: {best_R['SNR_total']:.3f} at R = {best_R['R']} h^-1 Mpc")
print(f"  Combined multi-scale SNR: {SNR_combined:.3f}")

print(f"\n  Interpretation:")
if SNR_combined >= 3.0:
    print(f"    Persistent Betti numbers at a Euclid-like survey ({V_survey_Gpc3} Gpc^3)")
    print(f"    CAN discriminate FW from LCDM at >{SNR_combined:.1f}-sigma.")
    print(f"    The topological statistics add independent constraining power.")
elif SNR_combined >= 1.0:
    print(f"    Persistent Betti numbers at a Euclid-like survey ({V_survey_Gpc3} Gpc^3)")
    print(f"    provide MARGINAL discrimination ({SNR_combined:.1f}-sigma).")
    print(f"    Useful as supporting evidence but not standalone.")
else:
    print(f"    Persistent Betti numbers at a Euclid-like survey ({V_survey_Gpc3} Gpc^3)")
    print(f"    CANNOT discriminate FW from LCDM (SNR = {SNR_combined:.2f}).")
    print(f"    The 2.2% sigma_8 shift and 0.56% n_s shift are too small for")
    print(f"    topological statistics to detect with this survey volume.")

print(f"\n  Key physics:")
print(f"    - sigma_8 shift: 0.811 -> 0.793 ({(sigma8_FW/sigma8_LCDM - 1)*100:+.2f}%)")
print(f"    - n_s shift: 0.9649 -> 0.9595 ({(n_s_FW/n_s_LCDM - 1)*100:+.4f}%)")
print(f"    - Power spectrum suppression: {(sigma8_FW/sigma8_LCDM)**2:.4f} at all k")
print(f"    - Both shifts reduce structure formation -> fewer/weaker topological features")

print(f"\n  INFO: SNR = {SNR_combined:.3f} for FW/LCDM discrimination using persistent Betti numbers")
print(f"        at V = {V_survey_Gpc3} Gpc^3 (Euclid-like).")

# ============================================================================
#  Section 9: Save Data
# ============================================================================

save_path = os.path.join(outdir, 's70_betti_fisher.npz')

# Collect per-scale data
save_dict = {
    'nu_arr': nu_arr,
    'R_smooth_arr': R_smooth_arr,
    'V_survey_Gpc3': V_survey_Gpc3,
    'V_survey_hmpc3': V_survey_hmpc3,
    'sigma8_LCDM': sigma8_LCDM,
    'sigma8_FW': sigma8_FW,
    'n_s_LCDM': n_s_LCDM,
    'n_s_FW': n_s_FW,
    'w0_LCDM': w0_LCDM,
    'w0_FW': w0_FW,
    'SNR_combined': SNR_combined,
    'SNR_sig8_only': res_sig8['SNR_total'],
    'SNR_ns_only': res_ns['SNR_total'],
}

for R in R_smooth_arr:
    res = results_all[R]
    prefix = f'R{R:.0f}_'
    save_dict[prefix + 'b0_fid'] = res['b0_fid']
    save_dict[prefix + 'b1_fid'] = res['b1_fid']
    save_dict[prefix + 'b2_fid'] = res['b2_fid']
    save_dict[prefix + 'b0_alt'] = res['b0_alt']
    save_dict[prefix + 'b1_alt'] = res['b1_alt']
    save_dict[prefix + 'b2_alt'] = res['b2_alt']
    save_dict[prefix + 'SNR_total'] = res['SNR_total']
    save_dict[prefix + 'SNR_beta0'] = res['SNR_beta0']
    save_dict[prefix + 'SNR_beta1'] = res['SNR_beta1']
    save_dict[prefix + 'SNR_beta2'] = res['SNR_beta2']
    save_dict[prefix + 'sigma0_fid'] = res['sigma0_fid']
    save_dict[prefix + 'sigma1_fid'] = res['sigma1_fid']
    save_dict[prefix + 'sigma2_fid'] = res['sigma2_fid']
    save_dict[prefix + 'sigma0_alt'] = res['sigma0_alt']
    save_dict[prefix + 'sigma1_alt'] = res['sigma1_alt']
    save_dict[prefix + 'sigma2_alt'] = res['sigma2_alt']
    save_dict[prefix + 'gamma_fid'] = res['gamma_fid']
    save_dict[prefix + 'gamma_alt'] = res['gamma_alt']
    save_dict[prefix + 'A3_fid'] = res['A3_fid']
    save_dict[prefix + 'A3_alt'] = res['A3_alt']

np.savez(save_path, **save_dict)
print(f"\nData saved: {save_path}")

print("\n" + "=" * 72)
print("  BETTI-FISHER-70 COMPLETE")
print("=" * 72)
