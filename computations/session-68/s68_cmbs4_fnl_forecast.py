#!/usr/bin/env python3
"""
CMBS4-FNL-FORECAST-68: Fisher Forecast for f_NL = 1.03 Folded Shape
=====================================================================

Gate: CMBS4-FNL-FORECAST-68 (INFO -- forecast, no pass/fail)

Computes Fisher matrix forecast for the framework's bispectrum prediction
against CMB-S4, Simons Observatory, and LiteBIRD projected sensitivities.

Framework predictions (from s67_gge_bispectrum.npz):
  f_NL^{equil} = 0.853 (from c_BLV = 0.485, functional-independent)
  f_NL^{folded} = 0.129 (from GGE diagonal Poisson, pair momentum conservation)
  f_NL^{multi} = 0.56  (squeezed, scheme-dependent)
  f_NL^{total} = 1.03  (quadrature sum)

Method:
  Step 1: Anchor equilateral sigma to literature values:
    - Planck: sigma(equil) = 47  (Planck 2019 IX, Table 8, T+E)
    - CMB-S4: sigma(equil) = 5   (CMB-S4 Science Book 2016)
  Step 2: Scale folded sigma using the Planck-measured ratio:
    - Planck: sigma(folded) = 64  (Planck 2019 IX, Table 9, enfolded, T)
    - sigma(folded)/sigma(equil) = 64/47 = 1.362 at Planck
  Step 3: Compute the noise-weighted mode-count RATIO between equilateral
    and folded at each experiment to determine how the ratio changes:
    - N_eff^{fold} / N_eff^{equil} varies with noise model
    - This gives the shape-dependent scaling correction
  Step 4: sigma(folded, exp) = sigma(equil, exp) * [sigma(fo)/sigma(eq)]_Planck
           * correction(exp)

  This approach uses ONLY observationally measured sigmas as anchors and
  a Fisher-derived correction for the relative shape sensitivity.

References:
  Planck 2019 IX (arXiv:1905.05697): Tables 8-9
  CMB-S4 Science Book (2016, arXiv:1610.02743)
  Meerburg et al. 2009 (arXiv:0901.4044): folded bispectrum
  Babich et al. 2004 (arXiv:0405356): bispectrum estimator
  Munchmeyer et al. 2015 (arXiv:1412.3461): folded forecasts

Session: S68
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    A_s_CMB, T_CMB, PI, H_0_km_s_Mpc, Omega_m, Omega_b, Omega_Lambda,
    n_pairs, c_light_km_s
)

# ==============================================================================
# Load S67 bispectrum results
# ==============================================================================
data_dir = os.path.dirname(os.path.abspath(__file__))
bis_data = np.load(os.path.join(data_dir, 's67_gge_bispectrum.npz'), allow_pickle=True)

f_NL_equil = float(bis_data['f_NL_equil'])       # 0.853
f_NL_folded = float(bis_data['f_NL_diag_CLT'])   # 0.129
f_NL_multi = float(bis_data['f_NL_multi_best'])   # 0.560
f_NL_total = float(bis_data['f_NL_total_uncorr']) # 1.028
cos_eq_fold = float(bis_data['cos_eq_fold'])       # 0.003
c_BLV = float(bis_data['c_BLV'])                   # 0.485

print("=" * 72)
print("CMBS4-FNL-FORECAST-68: Fisher Forecast for f_NL Bispectrum Templates")
print("=" * 72)
print()
print(f"Framework predictions (from S67 GGE-BISPECTRUM-67):")
print(f"  f_NL^{{equil}}  = {f_NL_equil:.4f}  (c_BLV = {c_BLV})")
print(f"  f_NL^{{folded}} = {f_NL_folded:.4f}  (GGE diagonal Poisson)")
print(f"  f_NL^{{multi}}  = {f_NL_multi:.4f}  (sudden transit)")
print(f"  f_NL^{{total}}  = {f_NL_total:.4f}  (quadrature sum)")
print(f"  cos(equil, folded) = {cos_eq_fold:.4f}  (orthogonal)")
print()

# ==============================================================================
# Literature constraints
# ==============================================================================
# Planck 2019 IX (arXiv:1905.05697):
#   Table 8 (T+E, KSW+Modal):
#     f_NL^{equil} = -26 +/- 47
#     f_NL^{ortho} = -38 +/- 24
#   Table 9 (SMICA, T only):
#     f_NL^{enfolded} = 22 +/- 64

sigma_eq_Planck = 47.0      # T+E  # (local)
sigma_fo_Planck = 64.0      # T only, enfolded  # (local)
sigma_eq_CMBS4_lit = 5.0    # CMB-S4 Science Book  # (local)

# The T+E combination reduces sigma by ~1.3-1.5x relative to T-only
# (Planck 2019 IX, comparing Tables 8 and 9).
# The enfolded sigma=64 is T-only. A T+E analysis would likely give
# sigma(enfolded, T+E) ~ 64 / 1.35 ~ 47. But this is uncertain.
# We use the CONSERVATIVE T-only value of 64 as our anchor.

ratio_fo_eq_Planck = sigma_fo_Planck / sigma_eq_Planck  # = 1.362

# CMB-S4 equilateral improvement: 47/5 = 9.4x
# This improvement factor includes: more modes (l_max 2500->3000),
# much lower noise (45->1 muK-arcmin), smaller beam (5->1 arcmin).

print("Literature anchors:")
print(f"  Planck sigma(equil) = {sigma_eq_Planck}  (T+E, Table 8)")
print(f"  Planck sigma(folded) = {sigma_fo_Planck}  (T only, enfolded, Table 9)")
print(f"  sigma(fo)/sigma(eq) at Planck = {ratio_fo_eq_Planck:.3f}")
print(f"  CMB-S4 sigma(equil) = {sigma_eq_CMBS4_lit}  (Science Book)")
print(f"  Improvement factor Planck->CMB-S4 (equil): {sigma_eq_Planck/sigma_eq_CMBS4_lit:.1f}x")
print()

# ==============================================================================
# Experimental specifications
# ==============================================================================
experiments = {
    'Planck': {
        'theta_FWHM': 5.0,    # arcmin
        'sigma_T': 45.0,      # muK-arcmin
        'l_max': 2500,
        'l_min': 2,
        'f_sky': 0.75,
        'sigma_eq_lit': sigma_eq_Planck,  # literature value
    },
    'Simons Observatory': {
        'theta_FWHM': 1.4,
        'sigma_T': 6.0,
        'l_max': 3000,
        'l_min': 30,
        'f_sky': 0.4,
        'sigma_eq_lit': None,
    },
    'CMB-S4': {
        'theta_FWHM': 1.0,
        'sigma_T': 1.0,
        'l_max': 3000,
        'l_min': 30,
        'f_sky': 0.4,
        'sigma_eq_lit': sigma_eq_CMBS4_lit,
    },
    'LiteBIRD': {
        'theta_FWHM': 30.0,
        'sigma_T': 2.5,
        'l_max': 200,
        'l_min': 2,
        'f_sky': 0.7,
        'sigma_eq_lit': None,
    },
}

# ==============================================================================
# Noise model
# ==============================================================================
def noise_cl(l, sigma_T, theta_FWHM):
    """Noise N_l in muK^2."""
    sigma_b = theta_FWHM * (PI / 10800.0) / np.sqrt(8.0 * np.log(2.0))
    sigma_T_rad = sigma_T * (PI / 10800.0)
    return sigma_T_rad**2 * np.exp(l * (l + 1) * sigma_b**2)

def cl_cmb(l):
    """Approximate unlensed TT C_l (muK^2), smooth envelope."""
    l = np.asarray(l, dtype=float)
    A_peak = 5800.0  # (local)
    l_peak = 220.0  # (local)
    l_damp = 1350.0  # (local)
    n_s = 0.9649  # (local)
    D_l = A_peak * (l / l_peak)**(n_s - 1) * np.exp(-(l / l_damp)**1.2)
    D_l = np.where(l < 30, 1050.0, D_l)
    D_l = np.maximum(D_l, 1.0)
    return D_l * 2.0 * PI / (l * (l + 1.0))

def cl_total(l, sigma_T, theta_FWHM):
    """C_l^tot = C_l^CMB + N_l."""
    return cl_cmb(l) + noise_cl(l, sigma_T, theta_FWHM)


# ==============================================================================
# Noise-weighted mode counting
# ==============================================================================
# The Fisher information for a bispectrum shape is:
#   F_shape = f_sky * sum |b_shape|^2 / (C_l1_tot C_l2_tot C_l3_tot * Delta)
#
# For the RATIO F_shape(exp_A)/F_shape(exp_B), the bispectrum template
# cancels and we get a noise-dependent ratio. But the triangle weighting
# differs between equilateral and folded shapes because collapsed
# triangles (l1+l2=l3) probe different l-combinations than equilateral
# triangles (l1=l2=l3).
#
# We compute N_eff = f_sky * sum r_l1 * r_l2 * r_l3 * W_shape(l1,l2,l3) / Delta
# where r_l = C_l^CMB / C_l^tot (noise suppression factor)
# and W_shape is the shape-dependent weight.

def compute_mode_ratio(specs, l_step=4):
    """
    Compute noise-weighted mode count for equilateral and folded shapes.

    Equilateral weight: W_eq ~ 1 (uniform over all triangles)
    Folded weight: W_fold peaks at collapsed triangles l1+l2=l3
      - Use Gaussian weight: exp(-alpha * [(l3-l1-l2)/l3]^2)
      - alpha = 2 gives moderate concentration at the folded limit

    Returns: N_eq, N_fo, l_arr, N_eq_cum, N_fo_cum
    """
    l_max = specs['l_max']
    l_min = max(specs['l_min'], 2)
    f_sky = specs['f_sky']
    sigma_T = specs['sigma_T']
    theta_FWHM = specs['theta_FWHM']

    l_arr = np.arange(l_min, l_max + 1, l_step)
    n_l = len(l_arr)

    C_cmb = cl_cmb(l_arr)
    C_tot = cl_total(l_arr, sigma_T, theta_FWHM)
    r = C_cmb / C_tot  # noise suppression

    N_eq = 0.0
    N_fo = 0.0
    N_eq_by_l3 = np.zeros(n_l)
    N_fo_by_l3 = np.zeros(n_l)

    for i1 in range(n_l):
        l1 = int(l_arr[i1])
        r1 = r[i1]

        for i2 in range(i1, n_l):
            l2 = int(l_arr[i2])
            r2 = r[i2]

            l3_lo = max(l2, abs(l1 - l2), l_min)
            l3_hi = min(l1 + l2, l_max)
            if l3_lo > l3_hi:
                continue

            i3_lo = max(0, (l3_lo - l_min + l_step - 1) // l_step)
            i3_hi = min(n_l - 1, (l3_hi - l_min) // l_step)
            if i3_lo > i3_hi:
                continue

            l3_vals = l_arr[i3_lo:i3_hi+1]
            mask = ((l3_vals >= l2) &
                    (l3_vals >= abs(l1 - l2)) &
                    (l3_vals <= l1 + l2) &
                    ((l1 + l2 + l3_vals) % 2 == 0))

            if not np.any(mask):
                continue

            i3_valid = np.arange(i3_lo, i3_hi+1)[mask]
            l3_v = l_arr[i3_valid].astype(float)
            r3 = r[i3_valid]

            delta = np.full(len(l3_v), 6.0)
            delta[l3_v == l2] = 2.0
            if l1 == l2:
                delta[:] = 2.0
                delta[l3_v == l1] = 1.0

            # Base: noise-weighted contribution
            base = r1 * r2 * r3 / delta

            # Folded weight: peaks at l1+l2=l3
            collapse = (l3_v - l1 - l2)**2 / (l3_v**2 + 1.0)
            w_fold = np.exp(-2.0 * collapse)

            N_eq += np.sum(base)
            N_fo += np.sum(base * w_fold)

            for k, i3 in enumerate(i3_valid):
                N_eq_by_l3[i3] += base[k]
                N_fo_by_l3[i3] += base[k] * w_fold[k]

    corr = f_sky * l_step**3
    N_eq *= corr
    N_fo *= corr
    N_eq_by_l3 *= corr
    N_fo_by_l3 *= corr

    return N_eq, N_fo, l_arr, np.cumsum(N_eq_by_l3), np.cumsum(N_fo_by_l3)


# ==============================================================================
# Compute for all experiments
# ==============================================================================
print("=" * 72)
print("Computing noise-weighted mode counts...")
print("=" * 72)

mode_data = {}
for name, specs in experiments.items():
    print(f"\n  {name}: beam={specs['theta_FWHM']}', noise={specs['sigma_T']} muK', "
          f"l_max={specs['l_max']}, f_sky={specs['f_sky']}")

    l_step = 2 if specs['l_max'] <= 300 else 4
    N_eq, N_fo, l_arr, N_eq_cum, N_fo_cum = compute_mode_ratio(specs, l_step)

    print(f"    N_eff(equil) = {N_eq:.6e}")
    print(f"    N_eff(fold)  = {N_fo:.6e}")
    print(f"    N_fo/N_eq    = {N_fo/N_eq:.4f}" if N_eq > 0 else "    N_fo/N_eq = inf")

    mode_data[name] = {
        'N_eq': N_eq, 'N_fo': N_fo,
        'l_arr': l_arr, 'N_eq_cum': N_eq_cum, 'N_fo_cum': N_fo_cum,
    }

# ==============================================================================
# Scale sigma for each experiment
# ==============================================================================
print(f"\n{'=' * 72}")
print("Forecasted sigma values")
print("=" * 72)

# Strategy for equilateral:
#   sigma_eq(exp) = sigma_eq(Planck) * sqrt(N_eq(Planck) / N_eq(exp))
#   Then calibrate so that CMB-S4 matches the literature value of 5.0.
# Strategy for folded:
#   At Planck: sigma_fo/sigma_eq = 64/47 = 1.362.
#   At other experiments: sigma_fo/sigma_eq = 1.362 * [R(Planck)/R(exp)]
#   where R = N_fo/N_eq is the shape-dependent mode ratio.

N_eq_pk = mode_data['Planck']['N_eq']
N_fo_pk = mode_data['Planck']['N_fo']
R_pk = N_fo_pk / N_eq_pk  # shape ratio at Planck

# Equilateral: scale from Planck, then recalibrate to CMB-S4 literature
sigma_eq_raw = {}
for name in experiments:
    ratio = mode_data[name]['N_eq'] / N_eq_pk if N_eq_pk > 0 else 1.0
    sigma_eq_raw[name] = sigma_eq_Planck / np.sqrt(ratio)

# Calibration: CMB-S4 should give 5.0
eq_calib = sigma_eq_CMBS4_lit / sigma_eq_raw['CMB-S4']

results = {}
for name in experiments:
    md = mode_data[name]
    R_exp = md['N_fo'] / md['N_eq'] if md['N_eq'] > 0 else R_pk

    # Calibrated equilateral
    sig_eq = sigma_eq_raw[name] * eq_calib

    # Folded: scale from the Planck ratio, corrected for shape-dependent noise
    # sigma_fo(exp) = sig_eq * ratio_fo_eq_Planck * (R_pk / R_exp)
    # The (R_pk / R_exp) correction accounts for how the folded shape is
    # relatively more/less noise-suppressed in different experiments.
    sig_fo = sig_eq * ratio_fo_eq_Planck * (R_pk / R_exp)

    # Detection significance
    SNR_eq = f_NL_equil / sig_eq
    SNR_fo = f_NL_folded / sig_fo
    SNR_joint = np.sqrt(SNR_eq**2 + SNR_fo**2)  # orthogonal shapes

    # Minimum detectable
    fNL_2s_eq = 2 * sig_eq
    fNL_3s_eq = 3 * sig_eq
    fNL_2s_fo = 2 * sig_fo
    fNL_3s_fo = 3 * sig_fo

    results[name] = {
        'sigma_eq': sig_eq,
        'sigma_fo': sig_fo,
        'R': R_exp,
        'SNR_eq': SNR_eq,
        'SNR_fo': SNR_fo,
        'SNR_joint': SNR_joint,
        'fNL_2s_eq': fNL_2s_eq,
        'fNL_3s_eq': fNL_3s_eq,
        'fNL_2s_fo': fNL_2s_fo,
        'fNL_3s_fo': fNL_3s_fo,
    }

# Print table
print(f"\n  {'Experiment':<25s} {'sig_eq':>8s} {'sig_fo':>8s} {'R_fo/eq':>8s} "
      f"{'SNR_eq':>8s} {'SNR_fo':>8s} {'SNR_jt':>8s}")
print("  " + "-" * 74)
for name in ['Planck', 'Simons Observatory', 'CMB-S4', 'LiteBIRD']:
    r = results[name]
    print(f"  {name:<25s} {r['sigma_eq']:>8.2f} {r['sigma_fo']:>8.2f} {r['R']:>8.4f} "
          f"{r['SNR_eq']:>8.4f} {r['SNR_fo']:>8.4f} {r['SNR_joint']:>8.4f}")

print(f"\n  Framework: f_NL^eq = {f_NL_equil:.3f}, f_NL^fo = {f_NL_folded:.3f}, "
      f"f_NL^tot = {f_NL_total:.3f}")

# ==============================================================================
# Cross-checks
# ==============================================================================
print(f"\n{'=' * 72}")
print("Cross-Checks")
print("=" * 72)

r_pk = results['Planck']
r_s4 = results['CMB-S4']

print(f"\n  Planck (with calibration):")
print(f"    sigma(equil) = {r_pk['sigma_eq']:.2f}  (literature: {sigma_eq_Planck})")
print(f"    sigma(folded) = {r_pk['sigma_fo']:.2f}  (literature: {sigma_fo_Planck})")
print(f"    sigma_fo/sigma_eq = {r_pk['sigma_fo']/r_pk['sigma_eq']:.3f}  "
      f"(literature: {ratio_fo_eq_Planck:.3f})")

print(f"\n  CMB-S4:")
print(f"    sigma(equil) = {r_s4['sigma_eq']:.2f}  (literature: {sigma_eq_CMBS4_lit})")
print(f"    sigma(folded) = {r_s4['sigma_fo']:.2f}")
print(f"    sigma_fo/sigma_eq = {r_s4['sigma_fo']/r_s4['sigma_eq']:.3f}")

# The Planck calibrated equilateral won't match 47 exactly because the
# calibration targets CMB-S4 = 5.0. The Fisher scaling ratio between
# Planck and CMB-S4 from our approximate model may differ from reality.
# This is a known limitation of using an approximate C_l model.
print(f"\n  NOTE: Planck sigma(equil) = {r_pk['sigma_eq']:.1f} differs from 47 because")
print(f"  the calibration targets CMB-S4 = 5.0 specifically. The Fisher")
print(f"  scaling from our approximate C_l model gives a Planck/CMB-S4")
print(f"  improvement factor of {np.sqrt(mode_data['CMB-S4']['N_eq']/N_eq_pk):.2f}x,")
print(f"  vs the literature value of {sigma_eq_Planck/sigma_eq_CMBS4_lit:.1f}x.")
print(f"  The folded sigma is anchored to the Planck RATIO, which is more")
print(f"  robust than the absolute value.")

# Simons Observatory literature comparison
# SO baseline: sigma(equil) ~ 15 (Ade et al. 2019, Table 2)
r_so = results['Simons Observatory']
print(f"\n  Simons Observatory:")
print(f"    sigma(equil) = {r_so['sigma_eq']:.2f}  (literature: ~15 from Ade+ 2019)")
print(f"    sigma(folded) = {r_so['sigma_fo']:.2f}")

# ==============================================================================
# Detailed CMB-S4 analysis
# ==============================================================================
print(f"\n{'=' * 72}")
print("CMB-S4 Detailed Analysis")
print("=" * 72)

r4 = results['CMB-S4']
print(f"\n  sigma(f_NL^equil)  = {r4['sigma_eq']:.2f}")
print(f"  sigma(f_NL^folded) = {r4['sigma_fo']:.2f}")
print(f"  sigma(folded)/sigma(equil) = {r4['sigma_fo']/r4['sigma_eq']:.3f}")

print(f"\n  Framework prediction detectability:")
print(f"    f_NL^equil  = {f_NL_equil:.3f}: {r4['SNR_eq']:.3f} sigma  -- NOT detectable")
print(f"    f_NL^folded = {f_NL_folded:.3f}: {r4['SNR_fo']:.4f} sigma -- NOT detectable")
print(f"    Joint (orthogonal): {r4['SNR_joint']:.4f} sigma -- NOT detectable")

print(f"\n  Minimum detectable f_NL:")
print(f"    Equilateral: {r4['fNL_2s_eq']:.1f} (2-sig), {r4['fNL_3s_eq']:.1f} (3-sig)")
print(f"    Folded:      {r4['fNL_2s_fo']:.1f} (2-sig), {r4['fNL_3s_fo']:.1f} (3-sig)")

improve_eq = r4['sigma_eq'] / f_NL_equil
improve_fo = r4['sigma_fo'] / f_NL_folded
print(f"\n  Required improvement beyond CMB-S4:")
print(f"    f_NL^equil: {improve_eq:.1f}x for 1-sigma")
print(f"    f_NL^folded: {improve_fo:.1f}x for 1-sigma")

# l_max scaling (bispectrum S/N ~ l_max^3 modes, sigma ~ l_max^{-3/2})
l_max_eq_1s = 3000 * improve_eq**(2./3.)
l_max_fo_1s = 3000 * improve_fo**(2./3.)
l_max_fo_2s = 3000 * (2*improve_fo)**(2./3.)
l_max_fo_3s = 3000 * (3*improve_fo)**(2./3.)
print(f"\n  l_max needed (sigma ~ l_max^{{-3/2}} scaling):")
print(f"    f_NL^equil  1-sig: l_max ~ {l_max_eq_1s:.0f}")
print(f"    f_NL^folded 1-sig: l_max ~ {l_max_fo_1s:.0f}")
print(f"    f_NL^folded 2-sig: l_max ~ {l_max_fo_2s:.0f}")
print(f"    f_NL^folded 3-sig: l_max ~ {l_max_fo_3s:.0f}")
print(f"    CMB Silk damping: ~3000-5000")
print(f"    21cm tomography: ~10^5 (HERA/SKA)")

# sigma(folded) ~ 0.1 needed for 1-sigma detection
needed = 0.1
improve_01 = r4['sigma_fo'] / needed
l_max_01 = 3000 * improve_01**(2./3.)
print(f"\n  To reach sigma(folded) = {needed}:")
print(f"    Improvement: {improve_01:.0f}x")
print(f"    l_max ~ {l_max_01:.0f}")

# ==============================================================================
# Future experiments
# ==============================================================================
print(f"\n{'=' * 72}")
print("Future Experiment Considerations")
print("=" * 72)

# 21cm intensity mapping
l_max_21cm = 1e5  # optimistic
improve_21cm = (l_max_21cm / 3000)**1.5
sig_eq_21cm = r4['sigma_eq'] / improve_21cm
sig_fo_21cm = r4['sigma_fo'] / improve_21cm
snr_eq_21 = f_NL_equil / sig_eq_21cm
snr_fo_21 = f_NL_folded / sig_fo_21cm

print(f"\n  21cm Intensity Mapping (HERA, SKA):")
print(f"    l_max ~ {l_max_21cm:.0e} (optimistic)")
print(f"    Improvement over CMB-S4: {improve_21cm:.0f}x")
print(f"    sigma(equil): {sig_eq_21cm:.4f}")
print(f"    sigma(folded): {sig_fo_21cm:.4f}")
print(f"    f_NL^equil = {f_NL_equil:.3f}: {snr_eq_21:.1f} sigma -- DETECTABLE")
print(f"    f_NL^folded = {f_NL_folded:.3f}: {snr_fo_21:.1f} sigma -- "
      f"{'DETECTABLE' if snr_fo_21 >= 2 else 'MARGINAL' if snr_fo_21 >= 1 else 'NOT detectable'}")

# Conservative 21cm
l_max_21cm_cons = 3e4
improve_21cm_cons = (l_max_21cm_cons / 3000)**1.5
sig_fo_21cm_cons = r4['sigma_fo'] / improve_21cm_cons
snr_fo_21_cons = f_NL_folded / sig_fo_21cm_cons
print(f"\n  21cm conservative (l_max ~ {l_max_21cm_cons:.0e}):")
print(f"    Improvement: {improve_21cm_cons:.0f}x")
print(f"    sigma(folded): {sig_fo_21cm_cons:.3f}")
print(f"    f_NL^folded: {snr_fo_21_cons:.2f} sigma")

print(f"\n  LSS Bispectrum (Euclid, Roman, SPHEREx):")
print(f"    Galaxy bispectrum best for local shape (scale-dependent bias).")
print(f"    Folded triangles washed out by projection and nonlinear coupling.")
print(f"    No planned LSS survey constrains folded bispectrum at O(1).")

print(f"\n  mu-Distortion (PIXIE/Voyage 2050):")
print(f"    Probes squeezed limit (local), not folded. Not useful here.")

# ==============================================================================
# Save
# ==============================================================================
print(f"\n{'=' * 72}")
print("Saving outputs...")
print("=" * 72)

save_dict = {
    # Framework inputs
    'f_NL_equil': f_NL_equil,
    'f_NL_folded': f_NL_folded,
    'f_NL_multi': f_NL_multi,
    'f_NL_total': f_NL_total,
    'cos_eq_fold': cos_eq_fold,
    'c_BLV': c_BLV,
    # Anchors
    'sigma_eq_Planck_anchor': sigma_eq_Planck,
    'sigma_fo_Planck_anchor': sigma_fo_Planck,
    'sigma_eq_CMBS4_lit': sigma_eq_CMBS4_lit,
    'ratio_fo_eq_Planck': ratio_fo_eq_Planck,
    'eq_calib_factor': eq_calib,
    # Gate
    'gate_name': 'CMBS4-FNL-FORECAST-68',
    'gate_verdict': 'INFO',
}

for name in ['Planck', 'Simons Observatory', 'CMB-S4', 'LiteBIRD']:
    prefix = name.replace(' ', '_')
    r = results[name]
    save_dict[f'{prefix}_sigma_eq'] = r['sigma_eq']
    save_dict[f'{prefix}_sigma_fo'] = r['sigma_fo']
    save_dict[f'{prefix}_SNR_eq'] = r['SNR_eq']
    save_dict[f'{prefix}_SNR_fo'] = r['SNR_fo']
    save_dict[f'{prefix}_SNR_joint'] = r['SNR_joint']
    save_dict[f'{prefix}_R_fo_eq'] = r['R']

save_dict['sigma_eq_21cm'] = sig_eq_21cm
save_dict['sigma_fo_21cm'] = sig_fo_21cm
save_dict['SNR_eq_21cm'] = snr_eq_21
save_dict['SNR_fo_21cm'] = snr_fo_21

# Cumulative
save_dict['CMBS4_l_arr'] = mode_data['CMB-S4']['l_arr']
save_dict['CMBS4_N_eq_cum'] = mode_data['CMB-S4']['N_eq_cum']
save_dict['CMBS4_N_fo_cum'] = mode_data['CMB-S4']['N_fo_cum']

out_npz = os.path.join(data_dir, 's68_cmbs4_fnl_forecast.npz')
np.savez(out_npz, **save_dict)
print(f"  Data: {out_npz}")

# ==============================================================================
# Plot
# ==============================================================================
print("  Generating plot...")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# LEFT: sigma vs l_max for CMB-S4
ax1 = axes[0]
l_arr = mode_data['CMB-S4']['l_arr']
N_eq_cum = mode_data['CMB-S4']['N_eq_cum']
N_fo_cum = mode_data['CMB-S4']['N_fo_cum']

# Scale cumulative: sigma(l) = sigma_final * sqrt(N_final / N_cum(l))
N_eq_final = N_eq_cum[-1]
N_fo_final = N_fo_cum[-1]

sigma_eq_l = r4['sigma_eq'] * np.sqrt(N_eq_final / np.maximum(N_eq_cum, 1e-30))
sigma_fo_l = r4['sigma_fo'] * np.sqrt(N_fo_final / np.maximum(N_fo_cum, 1e-30))

mask_eq = N_eq_cum > 0
mask_fo = N_fo_cum > 0

ax1.semilogy(l_arr[mask_eq], sigma_eq_l[mask_eq], 'b-', linewidth=2,
             label=rf'Equilateral ($\sigma \to {r4["sigma_eq"]:.1f}$)')
ax1.semilogy(l_arr[mask_fo], sigma_fo_l[mask_fo], 'r-', linewidth=2,
             label=rf'Folded ($\sigma \to {r4["sigma_fo"]:.1f}$)')

ax1.axhline(y=f_NL_equil, color='b', linestyle=':', alpha=0.4,
            label=rf'$f_{{\rm NL}}^{{\rm eq}} = {f_NL_equil:.2f}$')
ax1.axhline(y=f_NL_folded, color='r', linestyle=':', alpha=0.4,
            label=rf'$f_{{\rm NL}}^{{\rm fo}} = {f_NL_folded:.3f}$')
ax1.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3, label=r'$f_{\rm NL} = 1$')

ax1.set_xlabel(r'$\ell_{\max}$', fontsize=14)
ax1.set_ylabel(r'$\sigma(f_{\rm NL})$', fontsize=14)
ax1.set_title('CMB-S4: Sensitivity vs $\\ell_{\\max}$', fontsize=14)
ax1.legend(fontsize=9, loc='upper right')
ax1.set_xlim(30, 3000)
ax1.set_ylim(0.05, 1000)
ax1.grid(True, alpha=0.3)

# RIGHT: SNR bar chart
ax2 = axes[1]
names = ['Planck', 'Simons Observatory', 'CMB-S4', 'LiteBIRD']
shorts = ['Planck', 'SO', 'CMB-S4', 'LiteBIRD']

snr_eq = [results[n]['SNR_eq'] for n in names]
snr_fo = [results[n]['SNR_fo'] for n in names]
snr_jt = [results[n]['SNR_joint'] for n in names]

x = np.arange(len(shorts))
w = 0.25  # (local)

ax2.bar(x - w, snr_eq, w,
        label=rf'Equilateral ($f_{{\rm NL}}={f_NL_equil:.2f}$)', color='steelblue')
ax2.bar(x, snr_fo, w,
        label=rf'Folded ($f_{{\rm NL}}={f_NL_folded:.3f}$)', color='firebrick')
ax2.bar(x + w, snr_jt, w,
        label=rf'Joint ($f_{{\rm NL}}={f_NL_total:.2f}$)', color='forestgreen')

ax2.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label=r'$1\sigma$')

ax2.set_xlabel('Experiment', fontsize=14)
ax2.set_ylabel(r'Detection significance ($\sigma$)', fontsize=14)
ax2.set_title('Framework Bispectrum Detectability', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(shorts)
ax2.legend(fontsize=9, loc='upper right')
ymax = max(max(snr_eq), max(snr_fo), max(snr_jt))
ax2.set_ylim(0, max(ymax * 1.5, 0.5))
ax2.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
out_png = os.path.join(data_dir, 's68_cmbs4_fnl_forecast.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"  Plot: {out_png}")

# ==============================================================================
# GATE VERDICT
# ==============================================================================
print(f"\n{'=' * 72}")
print("GATE VERDICT: CMBS4-FNL-FORECAST-68")
print("=" * 72)

r4 = results['CMB-S4']
so = results['Simons Observatory']
lb = results['LiteBIRD']
pk = results['Planck']

gate_detail = (
    f"sigma(equil)={r4['sigma_eq']:.2f}, sigma(folded)={r4['sigma_fo']:.2f} for CMB-S4. "
    f"f_NL^equil={f_NL_equil:.3f} at {r4['SNR_eq']:.3f}-sigma, "
    f"f_NL^folded={f_NL_folded:.3f} at {r4['SNR_fo']:.4f}-sigma. "
    f"NOT detectable by any planned CMB experiment. "
    f"21cm (l_max~1e5): sigma(equil)~{sig_eq_21cm:.4f}, "
    f"sigma(folded)~{sig_fo_21cm:.4f}. "
    f"Folded shape unique to Bogoliubov pair creation."
)

print(f"""
Gate: CMBS4-FNL-FORECAST-68
Type: INFO (forecast, no pass/fail)

Method: Noise-weighted bispectrum mode counting with Planck-anchored scaling.
  Equilateral: Planck sigma={sigma_eq_Planck} -> CMB-S4 sigma={r4['sigma_eq']:.1f}
    (calibrated to CMB-S4 Science Book value of 5.0)
  Folded: Planck sigma={sigma_fo_Planck} (enfolded) -> CMB-S4 sigma={r4['sigma_fo']:.1f}
    (scaled using Planck ratio 64/47 = {ratio_fo_eq_Planck:.3f} + noise correction)
  Primordial shape orthogonality: cos(equil, folded) = {cos_eq_fold:.4f}

RESULTS:

| Experiment       | sigma(equil) | sigma(folded) | SNR(eq) | SNR(fo) | SNR(joint) |
|:-----------------|:-------------|:--------------|:--------|:--------|:-----------|
| Planck           | {pk['sigma_eq']:>12.1f} | {pk['sigma_fo']:>13.1f} | {pk['SNR_eq']:>7.4f} | {pk['SNR_fo']:>7.4f} | {pk['SNR_joint']:>10.4f} |
| Simons Obs.      | {so['sigma_eq']:>12.1f} | {so['sigma_fo']:>13.1f} | {so['SNR_eq']:>7.4f} | {so['SNR_fo']:>7.4f} | {so['SNR_joint']:>10.4f} |
| CMB-S4           | {r4['sigma_eq']:>12.1f} | {r4['sigma_fo']:>13.1f} | {r4['SNR_eq']:>7.4f} | {r4['SNR_fo']:>7.4f} | {r4['SNR_joint']:>10.4f} |
| LiteBIRD         | {lb['sigma_eq']:>12.1f} | {lb['sigma_fo']:>13.1f} | {lb['SNR_eq']:>7.4f} | {lb['SNR_fo']:>7.4f} | {lb['SNR_joint']:>10.4f} |

Framework: f_NL^equil = {f_NL_equil:.3f}, f_NL^folded = {f_NL_folded:.3f}, f_NL^total = {f_NL_total:.3f}

CMB-S4 minimum detectable f_NL:
  Equilateral: {r4['fNL_2s_eq']:.1f} (2-sigma), {r4['fNL_3s_eq']:.1f} (3-sigma)
  Folded:      {r4['fNL_2s_fo']:.1f} (2-sigma), {r4['fNL_3s_fo']:.1f} (3-sigma)

21cm tomography (l_max ~ 10^5, optimistic):
  sigma(equil) ~ {sig_eq_21cm:.4f}, sigma(folded) ~ {sig_fo_21cm:.4f}
  f_NL^equil: {snr_eq_21:.1f} sigma -- DETECTABLE
  f_NL^folded: {snr_fo_21:.1f} sigma -- {'DETECTABLE' if snr_fo_21 >= 2 else 'MARGINAL'}

ASSESSMENT:
  The framework predicts f_NL = 1.03 total, with a unique folded component
  f_NL^folded = 0.129 from Bogoliubov pair momentum conservation. Both
  channels are undetectable by CMB-S4 (SNR = {r4['SNR_eq']:.2f} equil, {r4['SNR_fo']:.3f} folded).
  The equilateral channel becomes detectable with 21cm tomography at
  l_max ~ 10^5. The folded channel requires l_max ~ {l_max_fo_1s:.0f} for
  1-sigma, making it a next-next-generation target. No single-field
  inflation model produces the folded shape -- detection would be
  a smoking gun for non-Bunch-Davies vacuum (Bogoliubov pair creation).
""")

print(f"gate_detail: {gate_detail}")
print("\nDONE.")
