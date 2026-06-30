#!/usr/bin/env python3
"""
ALPHA-S-BAYESIAN-SHADOW-71 — Maximum Systematic Error in a_0/a_2 from Pantheon+
================================================================================

The framework extracts a_0/a_2 from the spectral action, which determines the
cosmological constant and the dark energy equation of state w_0. The Pantheon+
supernova dataset constrains the expansion history and hence provides an
observational bound on a_0/a_2 systematics.

Chain of inference:
  1. a_0/a_2 sets the vacuum-to-gravity spectral moment ratio
  2. This ratio enters the Volovik partition which determines the effacement
     residual and hence w_0 = -0.918
  3. w_0 determines H(z) via the Friedmann equation (flat wCDM)
  4. H(z) determines d_L(z) and hence the Pantheon+ chi^2
  5. Any error delta(a_0/a_2) propagates through this chain

Method:
  1. Load the S70 Pantheon+ fit (s70_full_cov_pantheon.npz)
  2. Parametrize: delta(a_0/a_2) -> delta(w_0) via the effacement mechanism
  3. Compute chi^2(w_0 + delta_w) at each shifted w_0
  4. Find max delta(a_0/a_2) such that delta(chi^2) < 1 (1-sigma) and < 4 (2-sigma)
  5. Compare to spectral zeta truncation uncertainty (10.2% from W1-A)

The effacement relation:
  w_0 = -1 + (1 - Gamma)
  Gamma = 1 - (a_0 / a_2) * f_partition
  So: dw_0 / d(a_0/a_2) = -f_partition = -(1 - Gamma) / (a_0/a_2)

At the fold: a_0/a_2 = 6440.0 / 2776.17 = 2.3196
And w_0 = -0.918 => 1 - Gamma = 0.082 => f_partition = 0.082 / 2.3196 = 0.03535

Gate: ALPHA-S-BAYESIAN-SHADOW-71
  INFO: Report max systematic and compare to spectral zeta uncertainty (10.2%)

Output: s71_alpha_s_bayesian_shadow.npz, s71_alpha_s_bayesian_shadow.png
"""

import numpy as np
from scipy import integrate, optimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_Lambda, c_light_km_s,
    a0_fold, a2_fold, Omega_r
)

out_dir = Path(__file__).parent

# ==============================================================================
#  SECTION 1: Load S70 Pantheon+ Fit Results
# ==============================================================================

print("=" * 65)
print("  ALPHA-S-BAYESIAN-SHADOW-71")
print("  Maximum Systematic Error in a_0/a_2 from Pantheon+")
print("=" * 65)

t0 = time.time()

# Load the S70 results
d = np.load(out_dir / 's70_full_cov_pantheon.npz', allow_pickle=True)

# Extract key quantities
chi2_FW_ref = float(d['chi2_FW_full'])    # Framework chi^2 at w_0 = -0.918
chi2_LCDM = float(d['chi2_LCDM_full'])    # LCDM chi^2 at w_0 = -1.0
w0_FW = float(d['w0_FW'])                  # = -0.918
w0_LCDM = float(d['w0_LCDM'])              # = -1.0
H0 = float(d['H0'])                        # = 67.4 km/s/Mpc
Om = float(d['Omega_m_val'])               # = 0.315
N_valid = int(d['N_valid'])                 # = 1701
z_bin = d['z_bin']
mb_bin = d['mb_bin']
err_bin = d['err_bin']
mu_FW_bin = d['mu_FW_bin']
mu_LCDM_bin = d['mu_LCDM_bin']
N_bins = int(d['N_bins'])
MB_FW = float(d['MB_FW_full'])             # Best-fit M_B for FW

delta_chi2_FW_LCDM = float(d['delta_chi2_full'])

print(f"\n  S70 Pantheon+ reference values:")
print(f"    chi^2_FW (w_0={w0_FW}) = {chi2_FW_ref:.3f}  (N_SNe = {N_valid})")
print(f"    chi^2_LCDM (w_0=-1)    = {chi2_LCDM:.3f}")
print(f"    Delta chi^2 (FW-LCDM)  = {delta_chi2_FW_LCDM:.3f}")
print(f"    H_0 = {H0} km/s/Mpc, Omega_m = {Om}")

# ==============================================================================
#  SECTION 2: Framework Connection: a_0/a_2 -> w_0
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 2: a_0/a_2 -> w_0 Connection")
print("=" * 65)

# Spectral action coefficients at the fold
alpha_SA = a0_fold / a2_fold  # a_0 / a_2 ratio
print(f"\n  a_0 (fold) = {a0_fold}")
print(f"  a_2 (fold) = {a2_fold:.4f}")
print(f"  alpha_SA = a_0/a_2 = {alpha_SA:.6f}")

# The framework derives w_0 from the effacement residual:
#   w_0 = -1 + (1 - Gamma)
#   where Gamma is the vacuum tracking efficiency
#   At the fold: w_0 = -0.918 => (1 - Gamma) = 0.082
#
# The connection to a_0/a_2:
#   The spectral action vacuum energy is proportional to a_0 * Lambda^4
#   The gravitational coupling is proportional to a_2 * Lambda^2
#   The ratio a_0/a_2 determines how much vacuum energy remains after
#   the Volovik partition subtracts the tracked component.
#
# Linearized sensitivity:
#   delta(w_0) / delta(alpha_SA) = dw_0/d(alpha_SA)
#
# We compute this numerically by varying w_0 and finding chi^2.
# The mapping delta(alpha_SA)/alpha_SA -> delta(w_0) uses:
#   w_0 = -1 + f(alpha_SA)
#   where f encodes the effacement mechanism
#   delta(w_0) = f'(alpha_SA) * delta(alpha_SA)
#   f'(alpha_SA) = (1 - Gamma) / alpha_SA  (chain rule through partition)

delta_w_FW = w0_FW - (-1.0)  # = 0.082 (deviation from CC)
f_partition = delta_w_FW / alpha_SA  # df/d(alpha_SA) at the reference point

print(f"\n  w_0 = {w0_FW} => delta_w = w_0 - (-1) = {delta_w_FW:.4f}")
print(f"  f_partition = delta_w / alpha_SA = {f_partition:.6f}")
print(f"  Sensitivity: dw_0/d(alpha_SA) = {f_partition:.6f}")
print(f"  Inverse: d(alpha_SA)/dw_0 = {1.0/f_partition:.4f}")

# Fractional sensitivity:
# delta(w_0) / |w_0| per delta(alpha_SA) / alpha_SA
frac_sens = f_partition * alpha_SA / abs(w0_FW)
print(f"\n  Fractional sensitivity: delta(w_0)/|w_0| / [delta(alpha)/alpha] = {frac_sens:.4f}")

# ==============================================================================
#  SECTION 3: chi^2 Profile as Function of w_0
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 3: chi^2 Profile vs w_0")
print("=" * 65)

# We need to compute chi^2(w_0) for a range of w_0 values around -0.918.
# Using the binned data from S70 to avoid redownloading Pantheon+ raw data.
# The binned data has z_bin, mb_bin, err_bin for 37 bins.

def H_wCDM(z, H0_val, Om_val, w0):
    """Hubble parameter for flat wCDM (late-time, neglect radiation)."""
    ODE = 1.0 - Om_val
    return H0_val * np.sqrt(Om_val * (1 + z)**3 + ODE * (1 + z)**(3 * (1 + w0)))


def distance_modulus_array(z_arr, H0_val, Om_val, w0):
    """
    Distance modulus mu(z) = 5 * log10(d_L / 10 pc) for flat wCDM.
    d_L(z) = (1+z) * (c/H0) * integral_0^z dz'/E(z')
    """
    mu = np.zeros(len(z_arr))
    for j, zi in enumerate(z_arr):
        def integrand(zp):
            return 1.0 / H_wCDM(zp, H0_val, Om_val, w0)
        result, _ = integrate.quad(integrand, 0, zi, limit=100)
        dl_Mpc = (1 + zi) * c_light_km_s * result
        mu[j] = 5.0 * np.log10(dl_Mpc) + 25.0
    return mu


def chi2_binned(w0, z_bins, mb_bins, err_bins, H0_val, Om_val):
    """
    Compute chi^2 for binned Pantheon+ data at a given w_0.
    Analytically marginalizes over M_B offset.
    """
    mu_model = distance_modulus_array(z_bins, H0_val, Om_val, w0)

    # Residuals before M_B marginalization
    delta = mb_bins - mu_model
    w = 1.0 / err_bins**2  # (local)

    # Analytic marginalization over M_B:
    # chi^2 = sum w_i (delta_i - M_B)^2
    # Minimize over M_B: M_B = sum(w_i * delta_i) / sum(w_i)
    MB_best = np.sum(w * delta) / np.sum(w)

    # chi^2 with marginalized M_B
    chi2 = np.sum(w * (delta - MB_best)**2)
    return chi2, MB_best


# Compute chi^2 profile over a range of w_0 values
# We scan from -1.1 to -0.7 to map the full profile
w0_scan = np.linspace(-1.10, -0.70, 201)
chi2_scan = np.zeros(len(w0_scan))
MB_scan = np.zeros(len(w0_scan))

print(f"\n  Scanning chi^2(w_0) over {len(w0_scan)} values...")
print(f"  w_0 range: [{w0_scan[0]:.3f}, {w0_scan[-1]:.3f}]")

t1 = time.time()
for i, w0_val in enumerate(w0_scan):
    chi2_scan[i], MB_scan[i] = chi2_binned(w0_val, z_bin, mb_bin, err_bin, H0, Om)
t_scan = time.time() - t1
print(f"  Scan completed in {t_scan:.1f}s")

# Find the minimum chi^2 and the best-fit w_0
idx_min = np.argmin(chi2_scan)
w0_best = w0_scan[idx_min]
chi2_min = chi2_scan[idx_min]

print(f"\n  chi^2 profile results:")
print(f"    Best-fit w_0 (binned)  = {w0_best:.4f}")
print(f"    chi^2_min (binned)     = {chi2_min:.3f}")
print(f"    chi^2(w_0={w0_FW:.3f}) (binned) = {chi2_scan[np.argmin(np.abs(w0_scan - w0_FW))]:.3f}")
print(f"    chi^2(w_0=-1.000)     = {chi2_scan[np.argmin(np.abs(w0_scan - (-1.0)))]:.3f}")

# Refine the minimum with a parabolic fit near the minimum
mask_near = np.abs(w0_scan - w0_best) < 0.05
if np.sum(mask_near) >= 3:
    coeffs = np.polyfit(w0_scan[mask_near], chi2_scan[mask_near], 2)
    w0_best_refined = -coeffs[1] / (2 * coeffs[0])
    chi2_min_refined = np.polyval(coeffs, w0_best_refined)
    # Second derivative gives the curvature
    d2chi2_dw2 = 2 * coeffs[0]
    sigma_w0 = np.sqrt(2.0 / d2chi2_dw2) if d2chi2_dw2 > 0 else np.inf

    print(f"\n  Parabolic refinement:")
    print(f"    w_0_best (refined)     = {w0_best_refined:.6f}")
    print(f"    chi^2_min (refined)    = {chi2_min_refined:.3f}")
    print(f"    d^2(chi^2)/dw_0^2      = {d2chi2_dw2:.2f}")
    print(f"    sigma(w_0) (1-sigma)   = {sigma_w0:.6f}")
else:
    w0_best_refined = w0_best
    chi2_min_refined = chi2_min
    d2chi2_dw2 = 0
    sigma_w0 = np.inf

# ==============================================================================
#  SECTION 4: Maximum Systematic Error in a_0/a_2
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 4: Maximum Systematic Error in a_0/a_2")
print("=" * 65)

# Method: Find delta(w_0) such that chi^2(w_0_FW + delta_w) - chi^2(w_0_FW) = threshold
# Then convert to delta(a_0/a_2)

# chi^2 at the framework's predicted w_0
chi2_FW_binned = chi2_scan[np.argmin(np.abs(w0_scan - w0_FW))]

# Also compute precisely at w_0 = -0.918
chi2_at_FW, MB_at_FW = chi2_binned(w0_FW, z_bin, mb_bin, err_bin, H0, Om)

print(f"\n  chi^2 at w_0 = {w0_FW}: {chi2_at_FW:.4f}")
print(f"  chi^2_min:            {chi2_min_refined:.4f}")
print(f"  Delta chi^2 (FW - min): {chi2_at_FW - chi2_min_refined:.4f}")

# For the systematic error bound, we ask:
# Starting from the framework's w_0 = -0.918, how far can we shift w_0
# before chi^2 increases by delta_chi2_threshold?
#
# We use the parabolic approximation:
# chi^2(w_0) ≈ chi^2_min + (1/2) * d2chi2 * (w_0 - w0_best)^2
# chi^2(w_0_FW + delta_w) - chi^2(w_0_FW) = d2chi2 * (w0_FW - w0_best) * delta_w
#                                            + (1/2) * d2chi2 * delta_w^2
#
# For chi^2 worsening by 1 (1-sigma) or 4 (2-sigma):

thresholds = {
    '1-sigma': 1.0,
    '2-sigma': 4.0,
}

results = {}

for label, dchi2_thresh in thresholds.items():
    # Solve: chi^2(w_0_FW + delta_w) - chi^2(w_0_FW) = dchi2_thresh
    # Using numerical root-finding on the chi^2 profile

    # Interpolate chi^2(w_0) from the scan
    from scipy.interpolate import interp1d
    chi2_interp = interp1d(w0_scan, chi2_scan, kind='cubic', fill_value='extrapolate')

    # Find delta_w in both directions
    delta_w_results = []

    for direction in [+1, -1]:
        def objective(delta_w):
            w0_shifted = w0_FW + direction * abs(delta_w)
            if w0_shifted < w0_scan[0] or w0_shifted > w0_scan[-1]:
                return 100.0  # out of range
            return chi2_interp(w0_shifted) - chi2_at_FW - dchi2_thresh

        # Bracket search
        try:
            dw_max = optimize.brentq(objective, 0.001, 0.30)
            delta_w_results.append(direction * dw_max)
        except ValueError:
            # If chi^2 doesn't reach threshold in this range, the bound is very loose
            delta_w_results.append(direction * 0.30)

    # Take the tighter bound (smaller |delta_w|)
    delta_w_tight = min(abs(delta_w_results[0]), abs(delta_w_results[1]))
    delta_w_loose = max(abs(delta_w_results[0]), abs(delta_w_results[1]))

    # Convert to delta(a_0/a_2) using the chain rule
    # delta(alpha_SA) = delta_w / f_partition
    delta_alpha_tight = delta_w_tight / abs(f_partition)
    delta_alpha_loose = delta_w_loose / abs(f_partition)

    # Fractional systematic error
    frac_sys_tight = delta_alpha_tight / alpha_SA
    frac_sys_loose = delta_alpha_loose / alpha_SA

    results[label] = {
        'delta_w_pos': delta_w_results[0],
        'delta_w_neg': delta_w_results[1],
        'delta_w_tight': delta_w_tight,
        'delta_w_loose': delta_w_loose,
        'delta_alpha_tight': delta_alpha_tight,
        'delta_alpha_loose': delta_alpha_loose,
        'frac_sys_tight': frac_sys_tight,
        'frac_sys_loose': frac_sys_loose,
    }

    print(f"\n  {label} (Delta chi^2 = {dchi2_thresh}):")
    print(f"    delta(w_0): +{abs(delta_w_results[0]):.6f} / {delta_w_results[1]:.6f}")
    print(f"    |delta(w_0)|_tight = {delta_w_tight:.6f}")
    print(f"    |delta(a_0/a_2)|_tight = {delta_alpha_tight:.6f}")
    print(f"    fractional systematic_tight = {frac_sys_tight*100:.2f}%")
    print(f"    |delta(a_0/a_2)|_loose = {delta_alpha_loose:.6f}")
    print(f"    fractional systematic_loose = {frac_sys_loose*100:.2f}%")

# ==============================================================================
#  SECTION 5: Comparison to Spectral Zeta Truncation Uncertainty
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 5: Comparison to Spectral Zeta Truncation (W1-A)")
print("=" * 65)

# W1-A found S_inf = 2.353 with 10.2% truncation uncertainty
spectral_zeta_uncertainty = 0.102  # 10.2%  # (local)

print(f"\n  Spectral zeta truncation uncertainty (W1-A): {spectral_zeta_uncertainty*100:.1f}%")
print(f"\n  Pantheon+ bounds on fractional a_0/a_2 systematic:")
print(f"    1-sigma (tighter): {results['1-sigma']['frac_sys_tight']*100:.2f}%")
print(f"    2-sigma (tighter): {results['2-sigma']['frac_sys_tight']*100:.2f}%")

# Which is tighter?
ratio_1sig = results['1-sigma']['frac_sys_tight'] / spectral_zeta_uncertainty
ratio_2sig = results['2-sigma']['frac_sys_tight'] / spectral_zeta_uncertainty

print(f"\n  Ratio (Pantheon+ 1-sig / spectral zeta): {ratio_1sig:.3f}")
print(f"  Ratio (Pantheon+ 2-sig / spectral zeta): {ratio_2sig:.3f}")

if ratio_1sig < 1.0:
    print(f"\n  RESULT: Pantheon+ 1-sigma bound ({results['1-sigma']['frac_sys_tight']*100:.2f}%) is TIGHTER")
    print(f"          than spectral zeta truncation ({spectral_zeta_uncertainty*100:.1f}%).")
    print(f"          Pantheon+ provides an independent, observational constraint on a_0/a_2.")
elif ratio_2sig < 1.0:
    print(f"\n  RESULT: Pantheon+ 2-sigma bound ({results['2-sigma']['frac_sys_tight']*100:.2f}%) is TIGHTER")
    print(f"          than spectral zeta truncation ({spectral_zeta_uncertainty*100:.1f}%).")
    print(f"          Pantheon+ provides a moderate constraint at 2-sigma.")
else:
    print(f"\n  RESULT: Spectral zeta truncation ({spectral_zeta_uncertainty*100:.1f}%) is TIGHTER")
    print(f"          than both Pantheon+ bounds.")
    print(f"          The spectral computation is the binding constraint on a_0/a_2.")

# Also report w_0 sensitivity
print(f"\n  For reference:")
print(f"    10.2% change in a_0/a_2 -> delta(w_0) = {0.102 * alpha_SA * abs(f_partition):.4f}")
print(f"    This would shift w_0 from -0.918 to {w0_FW + 0.102 * alpha_SA * f_partition:.4f}")

# ==============================================================================
#  SECTION 6: Asymmetry Analysis
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 6: Asymmetry of chi^2 Profile")
print("=" * 65)

# The chi^2 profile is generally asymmetric around the best fit.
# This matters because a_0/a_2 can only shift w_0 in one direction
# if the spectral action truncation is systematic (not random).

# Report asymmetry
for label in ['1-sigma', '2-sigma']:
    r = results[label]
    asym = (abs(r['delta_w_pos']) - abs(r['delta_w_neg'])) / (abs(r['delta_w_pos']) + abs(r['delta_w_neg']))
    print(f"\n  {label} asymmetry: {asym:.4f}")
    print(f"    Allows larger shift toward w_0 -> {'more negative' if abs(r['delta_w_neg']) > abs(r['delta_w_pos']) else 'less negative'}")

# ==============================================================================
#  SECTION 7: Summary and Gate Verdict
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 7: Gate Verdict")
print("=" * 65)

print(f"""
  Gate: ALPHA-S-BAYESIAN-SHADOW-71
  Verdict: INFO

  KEY NUMBERS:
    a_0/a_2 (fold)            = {alpha_SA:.4f}
    w_0 (framework)           = {w0_FW}
    w_0 (best-fit Pantheon+)  = {w0_best_refined:.4f}
    chi^2(FW) binned          = {chi2_at_FW:.2f}
    chi^2_min (binned)        = {chi2_min_refined:.2f}
    d^2(chi^2)/dw_0^2         = {d2chi2_dw2:.2f}
    sigma(w_0) from Pantheon+ = {sigma_w0:.4f}

  MAXIMUM SYSTEMATIC ERROR IN a_0/a_2:
    1-sigma: {results['1-sigma']['frac_sys_tight']*100:.2f}% (delta(a_0/a_2) = {results['1-sigma']['delta_alpha_tight']:.4f})
    2-sigma: {results['2-sigma']['frac_sys_tight']*100:.2f}% (delta(a_0/a_2) = {results['2-sigma']['delta_alpha_tight']:.4f})

  COMPARISON TO SPECTRAL ZETA TRUNCATION:
    Spectral zeta uncertainty (W1-A): {spectral_zeta_uncertainty*100:.1f}%
    Pantheon+ 1-sigma / zeta:         {ratio_1sig:.3f}
    Pantheon+ 2-sigma / zeta:         {ratio_2sig:.3f}
    Binding constraint: {'Pantheon+' if ratio_1sig < 1.0 else 'Spectral zeta' if ratio_2sig >= 1.0 else 'Comparable'}
""")

# ==============================================================================
#  SECTION 8: Save Results and Plot
# ==============================================================================

print("  Saving results...")

np.savez(
    out_dir / 's71_alpha_s_bayesian_shadow.npz',
    # Reference values
    alpha_SA=alpha_SA,
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    w0_FW=w0_FW,
    w0_best_refined=w0_best_refined,
    chi2_min_refined=chi2_min_refined,
    chi2_at_FW=chi2_at_FW,
    d2chi2_dw2=d2chi2_dw2,
    sigma_w0=sigma_w0,
    f_partition=f_partition,
    # Scan data
    w0_scan=w0_scan,
    chi2_scan=chi2_scan,
    # 1-sigma results
    delta_w_1sig_pos=results['1-sigma']['delta_w_pos'],
    delta_w_1sig_neg=results['1-sigma']['delta_w_neg'],
    delta_alpha_1sig=results['1-sigma']['delta_alpha_tight'],
    frac_sys_1sig=results['1-sigma']['frac_sys_tight'],
    # 2-sigma results
    delta_w_2sig_pos=results['2-sigma']['delta_w_pos'],
    delta_w_2sig_neg=results['2-sigma']['delta_w_neg'],
    delta_alpha_2sig=results['2-sigma']['delta_alpha_tight'],
    frac_sys_2sig=results['2-sigma']['frac_sys_tight'],
    # Comparison
    spectral_zeta_uncertainty=spectral_zeta_uncertainty,
    ratio_1sig=ratio_1sig,
    ratio_2sig=ratio_2sig,
    # Metadata
    verdict=np.array('INFO'),
)

print(f"  Saved: s71_alpha_s_bayesian_shadow.npz")

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel 1: chi^2 profile vs w_0
ax1 = axes[0]
ax1.plot(w0_scan, chi2_scan - chi2_min_refined, 'b-', linewidth=1.5, label=r'$\chi^2(w_0) - \chi^2_{\rm min}$')
ax1.axvline(w0_FW, color='red', linestyle='--', linewidth=1.2, label=f'FW: $w_0={w0_FW}$')
ax1.axvline(w0_best_refined, color='green', linestyle=':', linewidth=1.2, label=f'Best: $w_0={w0_best_refined:.3f}$')
ax1.axvline(-1.0, color='gray', linestyle='-.', linewidth=1.0, label=r'$\Lambda$CDM: $w_0=-1$')
ax1.axhline(1.0, color='orange', linestyle='--', alpha=0.6, linewidth=0.8)
ax1.axhline(4.0, color='orange', linestyle=':', alpha=0.6, linewidth=0.8)
ax1.text(w0_scan[-1] - 0.02, 1.2, r'$1\sigma$', fontsize=9, color='orange')
ax1.text(w0_scan[-1] - 0.02, 4.4, r'$2\sigma$', fontsize=9, color='orange')
ax1.set_xlabel(r'$w_0$', fontsize=12)
ax1.set_ylabel(r'$\Delta\chi^2$', fontsize=12)
ax1.set_title(r'Pantheon+ $\chi^2$ Profile', fontsize=12)
ax1.set_ylim(-0.5, 20)
ax1.legend(fontsize=9, loc='upper right')
ax1.grid(alpha=0.3)

# Panel 2: Systematic error as function of delta(a_0/a_2)
ax2 = axes[1]

# Convert w_0 scan to alpha_SA fractional shift
delta_alpha_frac = (w0_scan - w0_FW) / (f_partition * alpha_SA)
delta_chi2_from_FW = chi2_scan - chi2_at_FW

ax2.plot(delta_alpha_frac * 100, delta_chi2_from_FW, 'b-', linewidth=1.5)
ax2.axhline(1.0, color='orange', linestyle='--', linewidth=0.8, label=r'$\Delta\chi^2 = 1$ (1$\sigma$)')
ax2.axhline(4.0, color='red', linestyle='--', linewidth=0.8, label=r'$\Delta\chi^2 = 4$ (2$\sigma$)')
ax2.axvline(0, color='green', linestyle=':', linewidth=1.0, alpha=0.5)

# Mark the spectral zeta uncertainty
ax2.axvline(spectral_zeta_uncertainty * 100, color='purple', linestyle='--', linewidth=1.2,
            label=f'Spectral zeta ({spectral_zeta_uncertainty*100:.1f}%)')
ax2.axvline(-spectral_zeta_uncertainty * 100, color='purple', linestyle='--', linewidth=1.2)

ax2.set_xlabel(r'$\delta(a_0/a_2) / (a_0/a_2)$ [%]', fontsize=12)
ax2.set_ylabel(r'$\Delta\chi^2$ from FW', fontsize=12)
ax2.set_title(r'Pantheon+ Constraint on $a_0/a_2$ Systematic', fontsize=12)
ax2.set_xlim(-25, 25)
ax2.set_ylim(-1, 15)
ax2.legend(fontsize=9)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(out_dir / 's71_alpha_s_bayesian_shadow.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s71_alpha_s_bayesian_shadow.png")

t_total = time.time() - t0
print(f"\n  Total runtime: {t_total:.1f}s")
print("\n  DONE.")
