#!/usr/bin/env python3
"""
LITEB-R-FORECAST-68: LiteBIRD Detectability of Framework Tensor Sector
========================================================================

Gate: INFO (forecast, no pass/fail)

Framework predictions:
  - CMB scales (k=0.05 Mpc^{-1}): r = 0.024, n_T = -3.02e-3
  - Transit scale (k ~ M_KK):      r = 0.0071, n_T = +0.468 (BLUE)
  - Transfer: 54 decades separate transit from CMB. Blue tilt localized.

Experiments:
  - LiteBIRD: sigma(r) = 0.001 (official target, 3-year, 15 bands, foreground marg.)
  - CMB-S4: sigma(r) ~ 0.003 (ground-based, foreground-limited)
  - BICEP/Keck (current): r < 0.036 (95% CL)

Computation:
  1. BB power spectrum for framework (r, n_T) prediction
  2. LiteBIRD Fisher matrix for r and n_T
  3. Detection significance for r = 0.024
  4. Distinguishability from slow-roll consistency (n_T = -r/8)
  5. CMB-S4 forecast
  6. Intermediate-scale blue tilt: which experiments probe it?

Sources:
  - s66_tensor_transfer.npz (CMB-scale r, n_T)
  - s67_acoustic_tensor.npz (transit-scale r, n_T)
  - LiteBIRD Collaboration (2022), PTEP 2023, 042F01: sigma(r) = 0.001
  - BICEP/Keck (BK18), Ade et al. 2021: r < 0.036 (95%)
  - CMB-S4 Science Book (2016): sigma(r) ~ 0.003
"""

import sys
sys.path.insert(0, "computations")
from canonical_constants import (, k_pivot_planck
    A_s_CMB, H_0_km_s_Mpc, PI, M_Pl_reduced, M_Pl_unreduced,
    M_KK_gravity, M_KK, hbar_c_GeV_m, Mpc_to_m, l_Planck,
    T_CMB, k_B_SI, c_light, hbar_SI
)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

# =============================================================================
# SECTION 1: Load prior results
# =============================================================================

print("=" * 72)
print("LITEB-R-FORECAST-68: LiteBIRD Detectability of Framework Tensor Sector")
print("=" * 72)

# Load S66 tensor transfer results
d66 = np.load("computations/session-66/s66_tensor_transfer.npz", allow_pickle=True)
r_CMB = float(d66["r_CMB_standard"])       # 0.0242
nT_CMB = float(d66["n_T_CMB_scenario_A"])  # -3.02e-3
nT_transit = float(d66["n_T_transit"])      # +0.468
eps_H_far = float(d66["eps_H_far"])         # 0.00151
k_transit_Mpc = float(d66["k_transit_Mpc"]) # 5.53e52
decades_sep = float(d66["decades_separation"])  # 54.0

# Load S67 acoustic tensor results
d67 = np.load("computations/session-67/s67_acoustic_tensor.npz", allow_pickle=True)
r_transit = float(d67["r_at_transit"])      # 0.0071
nT_plateau = float(d67["nT_plateau"])       # 2.375

print(f"\n--- Input from prior computations ---")
print(f"  r(CMB)        = {r_CMB:.4f}  (S66 TENSOR-TRANSFER-66)")
print(f"  n_T(CMB)      = {nT_CMB:.6f} (S66 scenario A: -2*eps_H(far))")
print(f"  r(transit)    = {r_transit:.4e}  (S67 ACOUSTIC-TENSOR-67)")
print(f"  n_T(transit)  = {nT_transit:.4f}  (S66, +0.468 BLUE)")
print(f"  k_transit     = {k_transit_Mpc:.3e} Mpc^-1")
print(f"  Decades sep.  = {decades_sep:.1f}")

# Slow-roll consistency relation at CMB
nT_SR = -r_CMB / 8.0
print(f"\n  Slow-roll consistency: n_T = -r/8 = {nT_SR:.6f}")
print(f"  Framework CMB n_T:              = {nT_CMB:.6f}")
print(f"  Difference |n_T(FW) - n_T(SR)| = {abs(nT_CMB - nT_SR):.6f}")
print(f"  --> Framework COINCIDES with slow-roll at CMB scales (diff = {abs(nT_CMB - nT_SR):.1e})")

# =============================================================================
# SECTION 2: BB Power Spectrum Model
# =============================================================================
# The CMB B-mode power spectrum from primordial tensors:
#   C_l^BB = integral of P_T(k) * [transfer function]^2 dk
#
# For the BB spectrum from tensors, the standard result (Kamionkowski & Kovetz 2016):
#   C_l^BB ~ r * A_s * f(l), peaking at l ~ 80
#
# We use the standard analytic approximation for the tensor BB transfer function.
# The primordial tensor power spectrum:
#   P_T(k) = r * A_s * (k / k_pivot)^{n_T}
# where k_pivot = 0.05 Mpc^{-1}.

k_pivot = k_pivot_planck  # canonical alias (was: = 0.05)

# Multipole range for BB spectrum
ell = np.arange(2, 201)

# Tensor BB transfer function: analytic fit from Zaldarriaga & Seljak (1997)
# The BB spectrum from tensors peaks at l ~ 80 and falls off for l > 150.
#
# C_l^BB (tensor) ~ r * A_s * T_l^{BB}
#
# We use the functional form from the literature:
#   C_l^BB = r * A_s * (l*(l+1)) / (2*pi) * Delta_BB(l)
# where Delta_BB(l) encodes the transfer function.
#
# A practical parametric fit (Smith et al. 2006, eq. 4; Zhao & Baskaran 2009):
#   D_l^BB = l(l+1)C_l/(2pi) ~ 0.024 * r * (l/80)^2 / (1 + (l/80)^4.2) * exp(-(l/500)^2) [uK^2]
#
# More precisely, we compute the BB spectrum using the standard integral.
# For a power-law tensor spectrum P_T(k) = r * A_s * (k/k_pivot)^{n_T},
# the BB power spectrum is well approximated by scaling the n_T = 0 spectrum.

def BB_spectrum_nT0(ells):
    """
    Tensor BB D_l = l(l+1)C_l/(2pi) in uK^2 for r=1, n_T=0.
    Parametric fit to CAMB output (Kamionkowski & Kovetz 2016, Fig. 2).
    Peak at l~80, amplitude ~0.024 uK^2 for r=1.
    """
    x = ells / 80.0
    # Fit to standard tensor BB (recombination bump only, no reionization bump)
    # Reionization bump at l < 10 adds ~5% of signal for tau_reion = 0.054
    D_reion = 0.0037 * np.exp(-((ells - 4.0) / 3.0)**2)  # reionization bump
    D_recomb = 0.022 * x**2 / (1.0 + x**4.0) * np.exp(-(ells / 400.0)**2)  # recombination bump
    return D_reion + D_recomb

def BB_spectrum(ells, r_val, nT_val, k_piv=0.05):
    """
    Tensor BB D_l = l(l+1)C_l/(2pi) in uK^2 for given r and n_T.
    The n_T correction modifies the shape via the k-l relation k ~ l/r_*
    where r_* ~ 144 Mpc (comoving sound horizon at decoupling).
    For small n_T, D_l(n_T) ~ D_l(0) * (l/l_pivot)^{n_T} where l_pivot ~ k_piv * r_*.
    """
    r_star = 144.43  # Mpc, comoving sound horizon at last scattering (Planck 2018)
    l_pivot = k_piv * r_star  # ~ 7.2
    D0 = BB_spectrum_nT0(ells)
    # Scale correction for n_T != 0
    # Each multipole l probes k ~ l / r_*, so (k/k_pivot)^{n_T} = (l / l_pivot)^{n_T}
    nT_correction = (ells / l_pivot) ** nT_val
    return r_val * D0 * nT_correction

# =============================================================================
# SECTION 3: LiteBIRD Noise Specification
# =============================================================================
# LiteBIRD (JAXA, launch ~2032):
#   - 15 frequency bands: 40-402 GHz
#   - 3 years full-sky
#   - Official target: sigma(r) = 0.001 (including foreground marginalization)
#   - Effective BB noise: N_l^BB ~ (2 uK-arcmin)^2 * exp(l(l+1)/l_beam^2)
#     where FWHM ~ 30 arcmin for cosmological channels
#
# For the Fisher forecast we use the effective noise after component separation.
# LiteBIRD Collaboration (PTEP 2023, 042F01) quotes:
#   - sigma(r) = 0.001 as total budget (stat + sys + foreground)
#   - Statistical-only: sigma(r) ~ 6e-4 for r=0
#
# We compute the Fisher matrix to verify consistency with sigma(r) = 0.001.

# LiteBIRD effective noise parameters (after component separation)
# These are from the LiteBIRD design: ~2 uK-arcmin white noise, 30' beam
noise_uKarcmin = 2.16  # uK-arcmin (effective, after combining 15 bands)  # (local)
beam_fwhm_arcmin = 30.0  # arcmin (effective beam for tensor analysis)  # (local)

# Convert to N_l^BB
beam_sigma_rad = beam_fwhm_arcmin * (PI / 180.0 / 60.0) / np.sqrt(8.0 * np.log(2.0))
noise_rad = noise_uKarcmin * (PI / 180.0 / 60.0)  # uK-rad

N_l_BB = noise_rad**2 * np.exp(ell * (ell + 1) * beam_sigma_rad**2)

# Lensing B-mode foreground (cannot be removed perfectly)
# C_l^{BB,lens} ~ 5e-6 uK^2 at l~80 (Planck lensing template)
# Parametric fit from Smith et al. 2012
D_l_lens = 5.0e-6 * (ell / 1000.0)**0.5 * (1.0 + (ell / 60.0)**2)**(-0.1)
# Convert D_l to C_l for noise calculation
C_l_lens = D_l_lens * 2.0 * PI / (ell * (ell + 1))

# After delensing (LiteBIRD can achieve ~50% delensing with internal + Planck lensing)
delensing_fraction = 0.5  # Residual lensing after delensing  # (local)
C_l_lens_residual = delensing_fraction * C_l_lens

# Sky fraction (LiteBIRD is full-sky, but Galactic mask reduces to ~70%)
f_sky = 0.70  # (local)

# =============================================================================
# SECTION 4: Fisher Matrix for (r, n_T)
# =============================================================================
# F_ij = sum_l (2l+1)*f_sky / 2 * dC_l/dp_i * Cov^{-1} * dC_l/dp_j
# where Cov = (C_l^{BB,signal} + C_l^{BB,lens,residual} + N_l^{BB})^2 / ((2l+1)*f_sky)
#
# For a 2-parameter fit (r, n_T):

def compute_fisher(r_fid, nT_fid, ells, f_sky_val, N_l, C_l_lens_res):
    """
    Fisher matrix for (r, n_T) from BB spectrum.
    Returns 2x2 Fisher matrix.
    """
    # Fiducial signal
    D_l_sig = BB_spectrum(ells, r_fid, nT_fid)
    C_l_sig = D_l_sig * 2.0 * PI / (ells * (ells + 1))

    # Total C_l
    C_l_tot = C_l_sig + C_l_lens_res + N_l

    # Derivatives
    dr = 1e-4  # (local)
    dnT = 1e-5

    # dC/dr
    D_plus = BB_spectrum(ells, r_fid + dr, nT_fid)
    D_minus = BB_spectrum(ells, r_fid - dr, nT_fid)
    dCl_dr = (D_plus - D_minus) / (2 * dr) * 2.0 * PI / (ells * (ells + 1))

    # dC/dn_T
    D_plus_nT = BB_spectrum(ells, r_fid, nT_fid + dnT)
    D_minus_nT = BB_spectrum(ells, r_fid, nT_fid - dnT)
    dCl_dnT = (D_plus_nT - D_minus_nT) / (2 * dnT) * 2.0 * PI / (ells * (ells + 1))

    # Fisher matrix
    F = np.zeros((2, 2))
    for i_l, l in enumerate(ells):
        weight = (2 * l + 1) * f_sky_val / (2.0 * C_l_tot[i_l]**2)
        F[0, 0] += weight * dCl_dr[i_l]**2
        F[0, 1] += weight * dCl_dr[i_l] * dCl_dnT[i_l]
        F[1, 0] += weight * dCl_dnT[i_l] * dCl_dr[i_l]
        F[1, 1] += weight * dCl_dnT[i_l]**2

    return F

# Compute Fisher for LiteBIRD at framework fiducial
print("\n" + "=" * 72)
print("SECTION 4: LiteBIRD Fisher Forecast")
print("=" * 72)

Fisher_LB = compute_fisher(r_CMB, nT_CMB, ell, f_sky, N_l_BB, C_l_lens_residual)
Cov_LB = np.linalg.inv(Fisher_LB)
sigma_r_LB = np.sqrt(Cov_LB[0, 0])
sigma_nT_LB = np.sqrt(Cov_LB[1, 1])
rho_r_nT_LB = Cov_LB[0, 1] / (sigma_r_LB * sigma_nT_LB)

print(f"\nFisher matrix (LiteBIRD, f_sky={f_sky}, delensing={1-delensing_fraction:.0%}):")
print(f"  F_rr   = {Fisher_LB[0,0]:.3e}")
print(f"  F_rnT  = {Fisher_LB[0,1]:.3e}")
print(f"  F_nTnT = {Fisher_LB[1,1]:.3e}")
print(f"\nCovariance:")
print(f"  sigma(r)   = {sigma_r_LB:.4f}")
print(f"  sigma(n_T) = {sigma_nT_LB:.4f}")
print(f"  rho(r,nT)  = {rho_r_nT_LB:.3f}")

# Compare to official LiteBIRD target
print(f"\n  Official LiteBIRD target: sigma(r) = 0.001")
print(f"  Our Fisher estimate:     sigma(r) = {sigma_r_LB:.4f}")
# Note: our simplified Fisher typically gives sigma ~ 5e-4 stat-only.
# The official 0.001 includes systematic and foreground budget.
# We adopt the OFFICIAL value for all subsequent calculations.

sigma_r_LB_official = 0.001  # LiteBIRD official target  # (local)

# =============================================================================
# SECTION 5: Detection Significance
# =============================================================================

print("\n" + "=" * 72)
print("SECTION 5: Detection Significance")
print("=" * 72)

# LiteBIRD
SNR_LB = r_CMB / sigma_r_LB_official
print(f"\n  LiteBIRD (sigma_r = {sigma_r_LB_official}):")
print(f"    r(CMB)    = {r_CMB:.4f}")
print(f"    SNR       = r / sigma_r = {SNR_LB:.1f}")
print(f"    Detection = {SNR_LB:.1f}-sigma")
print(f"    --> DEFINITIVE detection if r = {r_CMB:.3f}")

# CMB-S4
sigma_r_S4 = 0.003  # CMB-S4 target (foreground-marginalized, ground-based)  # (local)
SNR_S4 = r_CMB / sigma_r_S4
print(f"\n  CMB-S4 (sigma_r = {sigma_r_S4}):")
print(f"    r(CMB)    = {r_CMB:.4f}")
print(f"    SNR       = r / sigma_r = {SNR_S4:.1f}")
print(f"    Detection = {SNR_S4:.1f}-sigma")
print(f"    --> Strong detection if r = {r_CMB:.3f}")

# BICEP/Keck (current BK18)
# r < 0.036 (95% CL), which corresponds to sigma_r ~ 0.018 (assuming Gaussian)
sigma_r_BK18 = 0.036 / 1.96  # 95% CL -> 1-sigma (one-sided)
SNR_BK18 = r_CMB / sigma_r_BK18
print(f"\n  BICEP/Keck BK18 (current, sigma_r ~ {sigma_r_BK18:.3f}):")
print(f"    r(CMB)    = {r_CMB:.4f}")
print(f"    SNR       = r / sigma_r = {SNR_BK18:.2f}")
print(f"    --> r = {r_CMB:.3f} is {SNR_BK18:.1f}-sigma: {'detected' if SNR_BK18 > 3 else 'not yet detectable'}")
print(f"    --> Below 95% CL upper bound of r < 0.036: CONSISTENT")

# =============================================================================
# SECTION 6: n_T Measurement and Slow-Roll Distinguishability
# =============================================================================

print("\n" + "=" * 72)
print("SECTION 6: Tensor Tilt Distinguishability")
print("=" * 72)

# The framework predicts n_T(CMB) = -3.02e-3 at CMB scales.
# Slow-roll consistency: n_T = -r/8 = -0.024/8 = -0.003.
# These COINCIDE to remarkable precision.

print(f"\n  Framework:           n_T(CMB) = {nT_CMB:.6f}")
print(f"  Slow-roll (n_T=-r/8):  n_T(SR) = {nT_SR:.6f}")
print(f"  Difference:            delta    = {abs(nT_CMB - nT_SR):.6f}")

# Can LiteBIRD measure n_T?
# Using the Fisher-derived sigma(n_T):
print(f"\n  LiteBIRD sigma(n_T) [Fisher, stat-only]: {sigma_nT_LB:.3f}")

# More realistic: LiteBIRD + CMB-S4 combined lever arm
# The tensor tilt is constrained by the shape of the BB spectrum.
# With r ~ 0.02, the constraint on n_T is driven by the l-range [2, 200].
# The lever arm is ln(l_max / l_min) ~ ln(200/2) = 4.6.
# sigma(n_T) ~ sigma(r) / (r * Delta_ln_l) * correction
# For LiteBIRD: sigma(n_T) ~ 0.5 (very weak constraint from CMB alone)

# Official projections (Campeti et al. 2019, Tristram et al. 2022):
# sigma(n_T) ~ 0.4-0.5 for LiteBIRD alone at r ~ 0.02
# sigma(n_T) ~ 0.1-0.2 for LiteBIRD + CMB-S4 combined

sigma_nT_LB_realistic = 0.50  # LiteBIRD alone, realistic  # (local)
sigma_nT_LBS4 = 0.15          # LiteBIRD + CMB-S4 combined  # (local)

print(f"  LiteBIRD sigma(n_T) [realistic, incl. foregrounds]: ~ {sigma_nT_LB_realistic:.2f}")
print(f"  LiteBIRD + CMB-S4 sigma(n_T) [projected]:          ~ {sigma_nT_LBS4:.2f}")

# delta_chi2 for n_T = -0.003 vs n_T = 0
delta_nT = abs(nT_CMB)  # 0.003
print(f"\n  Delta(chi2) for n_T = {nT_CMB:.4f} vs n_T = 0:")
print(f"    LiteBIRD alone:      ({delta_nT}/{sigma_nT_LB_realistic})^2 = {(delta_nT/sigma_nT_LB_realistic)**2:.4f}")
print(f"    LiteBIRD + CMB-S4:   ({delta_nT}/{sigma_nT_LBS4})^2 = {(delta_nT/sigma_nT_LBS4)**2:.4f}")
print(f"    --> n_T = -0.003 is INDISTINGUISHABLE from n_T = 0 at CMB scales")

# Distinguishability from slow-roll
delta_nT_FW_SR = abs(nT_CMB - nT_SR)
print(f"\n  Framework vs slow-roll at CMB:")
print(f"    |n_T(FW) - n_T(SR)| = {delta_nT_FW_SR:.6f}")
print(f"    LiteBIRD sigma(n_T) = {sigma_nT_LB_realistic:.2f}")
print(f"    Tension             = {delta_nT_FW_SR/sigma_nT_LB_realistic:.4f} sigma")
print(f"    --> ZERO distinguishability: framework IS slow-roll at CMB scales")

# =============================================================================
# SECTION 7: Comparison Scenarios
# =============================================================================

print("\n" + "=" * 72)
print("SECTION 7: Model Comparison at CMB Scales")
print("=" * 72)

# Scenario A: Framework (r=0.024, n_T=-0.003)
# Scenario B: Slow-roll model with same r (r=0.024, n_T=-0.003) -- IDENTICAL
# Scenario C: LCDM with r = 0 (no tensors)
# Scenario D: Starobinsky R^2 (r ~ 0.004, n_T ~ -5e-4)

models = {
    "Framework":       {"r": r_CMB,  "nT": nT_CMB, "color": "C0", "ls": "-"},
    "Slow-roll (same r)": {"r": r_CMB,  "nT": nT_SR, "color": "C1", "ls": "--"},
    "LCDM (r=0)":      {"r": 0.0,    "nT": 0.0, "color": "C2", "ls": ":"},
    "Starobinsky R^2":  {"r": 0.004,  "nT": -0.0005, "color": "C3", "ls": "-."},
}

print(f"\n  {'Model':<22s}  {'r':>8s}  {'n_T':>10s}  {'LiteBIRD SNR':>12s}  {'S4 SNR':>8s}")
print(f"  {'-'*22}  {'-'*8}  {'-'*10}  {'-'*12}  {'-'*8}")
for name, m in models.items():
    snr_lb = m["r"] / sigma_r_LB_official if m["r"] > 0 else 0.0
    snr_s4 = m["r"] / sigma_r_S4 if m["r"] > 0 else 0.0
    print(f"  {name:<22s}  {m['r']:8.4f}  {m['nT']:10.6f}  {snr_lb:12.1f}  {snr_s4:8.1f}")

# Framework vs r=0: Bayes factor / sigma
print(f"\n  Framework (r={r_CMB:.3f}) vs r=0:")
print(f"    LiteBIRD: {r_CMB/sigma_r_LB_official:.1f}-sigma exclusion of r=0")
print(f"    CMB-S4:   {r_CMB/sigma_r_S4:.1f}-sigma exclusion of r=0")

# Framework vs Starobinsky
r_star = 0.004
delta_r = abs(r_CMB - r_star)
print(f"\n  Framework (r={r_CMB:.3f}) vs Starobinsky (r={r_star:.3f}):")
print(f"    delta_r = {delta_r:.3f}")
print(f"    LiteBIRD: {delta_r/sigma_r_LB_official:.1f}-sigma separation")
print(f"    CMB-S4:   {delta_r/sigma_r_S4:.1f}-sigma separation")

# =============================================================================
# SECTION 8: Intermediate-Scale Blue Tilt Observability
# =============================================================================

print("\n" + "=" * 72)
print("SECTION 8: Observability of Blue n_T at Intermediate Scales")
print("=" * 72)

# The blue tilt n_T = +0.468 is at the transit scale:
#   k_transit = 5.53e52 Mpc^{-1} = 3.54e14 GeV
#   f_transit = k_transit * c / (2*pi) -- but this is comoving k
#
# The corresponding GW frequency today depends on how k maps to f_GW:
#   f_GW = k * c / (2*pi) for comoving k in Mpc^{-1}, if k is in proper units
#
# Actually: f_GW = c * k / (2*pi) where k is in m^{-1}
# k_transit in m^{-1} = k_transit_Mpc * (1 Mpc / m) = 5.53e52 / 3.086e22 = 1.79e30 m^{-1}
#
# f_GW = c * k / (2*pi) = 3e8 * 1.79e30 / (2*pi) = 8.55e37 Hz
#
# This is ABSURDLY high. No conceivable detector can reach these frequencies.

k_transit_m = k_transit_Mpc / Mpc_to_m  # Mpc^{-1} -> m^{-1}
f_transit_Hz = c_light * k_transit_m / (2.0 * PI)

# CMB scale for reference
k_CMB_m = 0.05 / Mpc_to_m  # 0.05 Mpc^{-1} in m^{-1}
f_CMB_Hz = c_light * k_CMB_m / (2.0 * PI)

print(f"\n  Transit scale:")
print(f"    k_transit = {k_transit_Mpc:.3e} Mpc^-1 = {k_transit_m:.3e} m^-1")
print(f"    f_transit = {f_transit_Hz:.3e} Hz")
print(f"    --> {np.log10(f_transit_Hz):.1f} decades above CMB ({f_CMB_Hz:.3e} Hz)")
print(f"    --> {np.log10(f_transit_Hz) - np.log10(f_CMB_Hz):.1f} decades above CMB pivot")

# GW detector frequency ranges:
detectors = {
    "CMB (LiteBIRD)":   (1e-18, 1e-16, "BB power spectrum"),
    "PTA (NANOGrav)":    (1e-9,  1e-7,  "Pulsar timing"),
    "LISA":              (1e-4,  1e-1,  "Space interferometer"),
    "DECIGO/BBO":        (1e-2,  1e1,   "Space interferometer"),
    "LIGO/Virgo/KAGRA":  (1e1,   1e4,   "Ground interferometer"),
    "Einstein Telescope": (1e0,   1e4,   "3rd gen ground"),
    "Cosmic Explorer":   (5e0,   5e4,   "3rd gen ground"),
}

print(f"\n  GW detector ranges vs transit frequency ({f_transit_Hz:.1e} Hz):")
print(f"  {'Detector':<25s}  {'f_min [Hz]':>12s}  {'f_max [Hz]':>12s}  {'Gap [decades]':>14s}")
print(f"  {'-'*25}  {'-'*12}  {'-'*12}  {'-'*14}")
for name, (fmin, fmax, desc) in detectors.items():
    gap = np.log10(f_transit_Hz) - np.log10(fmax)
    print(f"  {name:<25s}  {fmin:12.1e}  {fmax:12.1e}  {gap:14.1f}")

print(f"\n  --> The blue tilt at the transit scale is {np.log10(f_transit_Hz) - np.log10(1e4):.0f} decades")
print(f"      above the highest-frequency planned GW detector.")
print(f"  --> NO conceivable experiment can probe n_T = +0.468 at k_transit.")
print(f"  --> The framework's UNIQUE tensor prediction (blue tilt) is UNOBSERVABLE.")
print(f"  --> The OBSERVABLE tensor prediction (r=0.024, n_T=-0.003) is indistinguishable from slow-roll.")

# =============================================================================
# SECTION 9: Summary Table
# =============================================================================

print("\n" + "=" * 72)
print("SECTION 9: Summary")
print("=" * 72)

print(f"""
LITEB-R-FORECAST-68: INFO

  CMB-Scale Predictions:
    r(CMB)    = {r_CMB:.4f}
    n_T(CMB)  = {nT_CMB:.6f}
    n_T(SR)   = {nT_SR:.6f}  (slow-roll, for same r)

  Detection Significance:
    LiteBIRD (sigma_r=0.001): {r_CMB/sigma_r_LB_official:.1f}-sigma detection of r
    CMB-S4   (sigma_r=0.003): {r_CMB/sigma_r_S4:.1f}-sigma detection of r
    BK18 current:              r = {r_CMB:.3f} below upper limit r < 0.036

  Distinguishability:
    Framework vs slow-roll (n_T): {delta_nT_FW_SR:.6f} difference -> 0.00 sigma (IDENTICAL at CMB)
    Framework vs r=0:              {r_CMB/sigma_r_LB_official:.1f}-sigma (LiteBIRD)
    Framework vs Starobinsky:      {delta_r/sigma_r_LB_official:.1f}-sigma (LiteBIRD)

  Blue Tilt Observability:
    n_T(transit)  = +{nT_transit:.3f} at k = {k_transit_Mpc:.2e} Mpc^-1 (f = {f_transit_Hz:.1e} Hz)
    Gap to nearest detector: {np.log10(f_transit_Hz) - np.log10(1e4):.0f} decades above LIGO/ET
    --> UNOBSERVABLE by any planned or conceivable experiment

  Key Conclusion:
    If the framework is correct, LiteBIRD WILL detect r = 0.024 at 24-sigma.
    But this detection CANNOT distinguish the framework from any slow-roll model
    predicting the same r, because n_T(CMB) = -r/8 to within 0.0001.
    The framework's unique signature (blue tilt) is at inaccessible frequencies.
""")

# =============================================================================
# SECTION 10: Save Data
# =============================================================================

# Compute BB spectra for plot
D_l_FW = BB_spectrum(ell, r_CMB, nT_CMB)
D_l_SR = BB_spectrum(ell, r_CMB, nT_SR)
D_l_star = BB_spectrum(ell, 0.004, -0.0005)

# LiteBIRD noise as D_l
D_l_noise_LB = N_l_BB * ell * (ell + 1) / (2.0 * PI)
D_l_lens_full = D_l_lens  # Already D_l
D_l_lens_res = delensing_fraction * D_l_lens

save_path = "computations/session-68/s68_liteb_r_forecast.npz"
np.savez(save_path,
    # Input
    r_CMB=r_CMB,
    nT_CMB=nT_CMB,
    nT_SR=nT_SR,
    r_transit=r_transit,
    nT_transit=nT_transit,
    k_transit_Mpc=k_transit_Mpc,
    f_transit_Hz=f_transit_Hz,
    decades_separation=decades_sep,
    # LiteBIRD specs
    sigma_r_LB_official=sigma_r_LB_official,
    sigma_r_LB_fisher=sigma_r_LB,
    sigma_nT_LB_fisher=sigma_nT_LB,
    sigma_nT_LB_realistic=sigma_nT_LB_realistic,
    sigma_nT_LBS4=sigma_nT_LBS4,
    f_sky=f_sky,
    delensing_fraction=delensing_fraction,
    # CMB-S4 specs
    sigma_r_S4=sigma_r_S4,
    # Fisher matrix
    Fisher_LB=Fisher_LB,
    Cov_LB=Cov_LB,
    # Detection significance
    SNR_r_LiteBIRD=r_CMB / sigma_r_LB_official,
    SNR_r_S4=r_CMB / sigma_r_S4,
    SNR_r_BK18=SNR_BK18,
    # Distinguishability
    delta_nT_FW_SR=delta_nT_FW_SR,
    delta_r_FW_Starobinsky=delta_r,
    sigma_FW_vs_Starobinsky_LB=delta_r / sigma_r_LB_official,
    sigma_FW_vs_r0_LB=r_CMB / sigma_r_LB_official,
    # Spectra for plot
    ell=ell,
    D_l_FW=D_l_FW,
    D_l_SR=D_l_SR,
    D_l_Starobinsky=D_l_star,
    D_l_noise_LB=D_l_noise_LB,
    D_l_lens=D_l_lens_full,
    D_l_lens_residual=D_l_lens_res,
    # Gate
    gate_name="LITEB-R-FORECAST-68",
    gate_verdict="INFO",
    gate_detail=f"r(CMB)={r_CMB:.4f}, n_T(CMB)={nT_CMB:.6f}. LiteBIRD {r_CMB/sigma_r_LB_official:.0f}-sigma detection. "
                f"Indistinguishable from slow-roll (delta_n_T = {delta_nT_FW_SR:.1e}). "
                f"Blue tilt at {f_transit_Hz:.1e} Hz ({np.log10(f_transit_Hz)-np.log10(1e4):.0f} decades above LIGO). "
                f"CMB-S4 {r_CMB/sigma_r_S4:.0f}-sigma. Starobinsky excluded at {delta_r/sigma_r_LB_official:.0f}-sigma by LiteBIRD.",
)
print(f"Data saved: {save_path}")

# =============================================================================
# SECTION 11: Plot
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Panel A: BB Power Spectrum ---
ax = axes[0]

# Signal spectra
ax.semilogy(ell, D_l_FW, 'C0-', lw=2.0, label=f'Framework (r={r_CMB:.3f}, n$_T$={nT_CMB:.4f})')
ax.semilogy(ell, D_l_SR, 'C1--', lw=1.5, label=f'Slow-roll (r={r_CMB:.3f}, n$_T$={nT_SR:.4f})')
ax.semilogy(ell, D_l_star, 'C3-.', lw=1.5, label=f'Starobinsky R$^2$ (r=0.004)')

# Noise / foreground
ax.semilogy(ell, D_l_lens_full, color='gray', ls=':', lw=1.0, label='Lensing BB (no delensing)')
ax.semilogy(ell, D_l_lens_res, color='gray', ls='--', lw=1.0, label=f'Lensing BB ({1-delensing_fraction:.0%} delensed)')
ax.semilogy(ell, D_l_noise_LB, 'k:', lw=0.8, alpha=0.5, label='LiteBIRD noise')

# LiteBIRD sensitivity band
# sigma(D_l) ~ sqrt(2/(2l+1)/f_sky) * (C_l_tot) * l(l+1)/(2pi)
C_l_FW = D_l_FW * 2.0 * PI / (ell * (ell + 1))
C_l_tot = C_l_FW + C_l_lens_residual + N_l_BB
sigma_D_l = np.sqrt(2.0 / ((2*ell + 1) * f_sky)) * C_l_tot * ell * (ell + 1) / (2.0 * PI)
ax.fill_between(ell, np.maximum(D_l_FW - sigma_D_l, 1e-8), D_l_FW + sigma_D_l,
                alpha=0.15, color='C0', label='LiteBIRD 1-$\\sigma$ band')  # (local)

ax.set_xlim(2, 200)
ax.set_ylim(1e-7, 1e-1)
ax.set_xlabel('Multipole $\\ell$', fontsize=12)
ax.set_ylabel('$D_\\ell^{BB}$ [$\\mu$K$^2$]', fontsize=12)
ax.set_title('CMB B-mode Power Spectrum', fontsize=13)
ax.legend(fontsize=7.5, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel B: Detection Significance Bar Chart ---
ax2 = axes[1]

experiments = ['BK18\n(current)', 'CMB-S4', 'LiteBIRD']
sigma_r_vals = [sigma_r_BK18, sigma_r_S4, sigma_r_LB_official]
snr_vals = [r_CMB / s for s in sigma_r_vals]
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

bars = ax2.bar(experiments, snr_vals, color=colors, edgecolor='black', linewidth=0.8)

# Reference lines
ax2.axhline(y=3, color='orange', ls='--', lw=1.0, alpha=0.7, label='3-$\\sigma$')
ax2.axhline(y=5, color='red', ls='--', lw=1.0, alpha=0.7, label='5-$\\sigma$ discovery')

# Annotate bars
for bar, snr in zip(bars, snr_vals):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{snr:.1f}$\\sigma$', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax2.set_ylabel('Detection significance ($\\sigma$)', fontsize=12)
ax2.set_title(f'r = {r_CMB:.3f}: Detection by Experiment', fontsize=13)
ax2.legend(fontsize=9, loc='upper left')
ax2.set_ylim(0, 30)
ax2.grid(True, axis='y', alpha=0.3)

# Add text box with key result
textstr = (f'Framework: r = {r_CMB:.3f}, n$_T$ = {nT_CMB:.4f}\n'
           f'Slow-roll: n$_T$ = $-$r/8 = {nT_SR:.4f}\n'
           f'$\\Delta$n$_T$ = {delta_nT_FW_SR:.1e} (indistinguishable)\n'
           f'Blue tilt at f = {f_transit_Hz:.0e} Hz (unobservable)')
props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
ax2.text(0.98, 0.55, textstr, transform=ax2.transAxes, fontsize=8,
         verticalalignment='top', horizontalalignment='right', bbox=props)

plt.tight_layout()
plot_path = "computations/session-68/s68_liteb_r_forecast.png"
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")

plt.close()

print("\n" + "=" * 72)
print("LITEB-R-FORECAST-68: COMPLETE")
print("=" * 72)
