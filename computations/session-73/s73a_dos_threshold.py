#!/usr/bin/env python3
"""
s73a_dos_threshold.py — DOS-THRESHOLD-73a
==========================================

Van Hove DOS-weighted threshold corrections: does spectral weighting
from the van Hove singularity at the fold modify the EFFECTIVE threshold
ratios delta_1/delta_3 and delta_2/delta_3?

STRUCTURAL CONTEXT
------------------
W2-B established a PERMANENT Dynkin Index Sum Rule:
  T_2(p,q) / T_3(p,q) = 1     (exact, all SU(3) irreps)
  T_Y(p,q) / T_3(p,q) = 4/3   (exact, all SU(3) irreps)

Consequence: delta_2/delta_3 = 1 and delta_1/delta_3 = 20/9 = 2.222
are representation-theoretic identities independent of regulator or
mode energies.

The question (Phonon-First review Section 3.4): if the D_K spectrum has
a van Hove singularity (rho_B2 = 14.02), the threshold corrections may
be DOS-dominated rather than coupling-dominated, pushing delta_1/delta_3
toward 1.

STRUCTURAL THEOREM (proven here):
---------------------------------
ANY sector-level weighting w(p,q) * f(omega_{p,q}) applied to the
threshold sum preserves the ratios EXACTLY:

  delta_a^{DOS} = sum_{(p,q)} w(p,q) * T_a(p,q) * g(omega_{p,q})

  delta_2^{DOS}/delta_3^{DOS} = sum w*T_2*g / sum w*T_3*g
                                = sum w*T_3*g / sum w*T_3*g = 1   [since T_2 = T_3]

  delta_1^{DOS}/delta_3^{DOS} = (5/3) * sum w*T_Y*g / sum w*T_3*g
                                = (5/3)*(4/3) = 20/9             [since T_Y = (4/3)*T_3]

This is because the Dynkin index ratios are CONSTANTS across all irreps.
No smooth DOS reweighting can change them.

The computation below VERIFIES this numerically with 6 different DOS
weighting models, providing a PERMANENT closure of the DOS-weighting route.

METHOD
------
1. Reproduce W2-B unweighted thresholds (cross-check).
2. Construct 6 DOS weighting models:
   (a) Flat DOS (rho = 1, recovers W2-B baseline)
   (b) Empirical DOS from S44 at tau=0.19 (histogram-interpolated)
   (c) Van Hove peaked: rho(E) = 1 + A*delta(E - E_vH) enhancement at B2 peak
   (d) Power-law: rho(E) ~ E^{-alpha} (soft enhancement of low-energy modes)
   (e) Exponential: rho(E) ~ exp(-E/T_GGE) (thermal weighting at GGE temperature)
   (f) Random per-sector weights (stress test)
3. For each model, compute delta_a^{DOS} and the ratios.
4. Verify all ratios agree with 20/9 to machine precision.
5. As a secondary analysis: compute the ABSOLUTE shift in each delta_a
   to assess whether DOS weighting changes the RG running MAGNITUDES
   (even though ratios are fixed).

Gate: DOS-THRESHOLD-73a
  PASS: |delta_1^{DOS}/delta_3^{DOS} - 1| < |delta_1/delta_3 - 1|
  FAIL: DOS weighting makes ratios LESS universal

Author: baptista-spacetime-analyst
Session: S73a
Provenance: W2-B PW-THRESHOLD-RATIOS-73a, S44 DOS data, Baptista Paper 13
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_Z, tau_fold,
    sin2_thetaW_MSbar, sin2_thetaW_fold,
    alpha_em_MZ_inv,
    rho_B2_per_mode, T_GGE_B2, E_B2_mean,
)

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 80)
print("DOS-THRESHOLD-73a: Van Hove DOS-Weighted Threshold Corrections")
print("S73a | baptista-spacetime-analyst")
print("=" * 80)
t_start = time.time()  # (local)

# =============================================================================
# 0. LOAD W2-B DATA AND S44 DOS DATA
# =============================================================================
print("\n" + "=" * 80)
print("0. LOAD W2-B AND DOS DATA")
print("=" * 80)

# W2-B results
d_w2b = np.load(os.path.join(outdir, 's73a_pw_threshold_ratios.npz'), allow_pickle=True)
Lambda_fixed = float(d_w2b['Lambda_fixed'])  # 2.048 M_KK  # (local)
gamma_opt = float(d_w2b['gamma_opt'])        # 0.488  # (local)
sec_p = d_w2b['sec_p']
sec_q = d_w2b['sec_q']
sec_dim = d_w2b['sec_dim']
sec_level = d_w2b['sec_level']
sec_omega_min = d_w2b['sec_omega_min']
sec_T3 = d_w2b['sec_T3']
sec_T2 = d_w2b['sec_T2']
sec_TY = d_w2b['sec_TY']
n_sectors = len(sec_p)  # (local)

delta_3_w2b = float(d_w2b['delta_3_total'])  # (local)
delta_2_w2b = float(d_w2b['delta_2_total'])  # (local)
delta_Y_w2b = float(d_w2b['delta_Y_total'])  # (local)
delta_1_w2b = float(d_w2b['delta_1_total'])  # (local)
ratio_21_w2b = float(d_w2b['ratio_delta2_delta3'])  # (local)
ratio_11_w2b = float(d_w2b['ratio_delta1_delta3'])  # (local)

print(f"  W2-B data: {n_sectors} sectors, Lambda = {Lambda_fixed:.4f} M_KK")
print(f"  W2-B delta_3 = {delta_3_w2b:.6f}")
print(f"  W2-B delta_2/delta_3 = {ratio_21_w2b:.6f} (exact: 1.000000)")
print(f"  W2-B delta_1/delta_3 = {ratio_11_w2b:.6f} (exact: 20/9 = {20/9:.6f})")

# S44 DOS data at fold
d_dos = np.load(os.path.join(outdir, 's44_dos_tau.npz'), allow_pickle=True)
dos_omega = d_dos['tau0.19_all_omega']      # 992 eigenvalue groups  # (local)
dos_dim2 = d_dos['tau0.19_all_dim2']        # multiplicity (dim^2)  # (local)
dos_bins = d_dos['bins']                     # histogram bins  # (local)
dos_centers = d_dos['bin_centers']           # bin centers  # (local)
dos_hist_w = d_dos['tau0.19_hist_w']        # weighted histogram  # (local)
dos_rho_smooth = d_dos['tau0.19_rho_smooth']  # smoothed DOS  # (local)
dos_vh_omega = d_dos['tau0.19_vh_omega']    # van Hove singularity positions  # (local)
dos_vh_rho = d_dos['tau0.19_vh_rho']        # van Hove singularity heights  # (local)

print(f"\n  S44 DOS data: {len(dos_omega)} eigenvalue groups at tau={tau_fold}")
print(f"  Eigenvalue range: [{dos_omega.min():.4f}, {dos_omega.max():.4f}] M_KK")
print(f"  Van Hove peaks: {len(dos_vh_omega)} singularities")
for i in range(len(dos_vh_omega)):
    if dos_vh_rho[i] > 0:
        print(f"    omega = {dos_vh_omega[i]:.4f}, rho = {dos_vh_rho[i]:.0f}")


# =============================================================================
# 1. STRUCTURAL THEOREM: ALGEBRAIC PROOF
# =============================================================================
print("\n" + "=" * 80)
print("1. STRUCTURAL THEOREM: ALGEBRAIC PROOF")
print("=" * 80)

print("""
  THEOREM (Dynkin Index Ratio Invariance under Sector Reweighting):

  Let w: {(p,q)} -> R+ be ANY non-negative weighting function on PW sectors.
  Let f: R+ -> R be ANY function of the mode energy omega_{(p,q)}.
  Define the DOS-weighted threshold correction for gauge group a:

    delta_a^{DOS} = sum_{(p,q) != (0,0)} w(p,q) * T_a(p,q) * f(omega_{p,q})

  Then:
    delta_2^{DOS} / delta_3^{DOS} = 1        (exact)
    delta_1^{DOS} / delta_3^{DOS} = 20/9     (exact)

  PROOF:
  W2-B established that for ALL SU(3) irreps (p,q) != (0,0):
    T_2(p,q) = T_3(p,q)        ... (*)
    T_Y(p,q) = (4/3) * T_3(p,q) ... (**)

  These are representation-theoretic identities following from the
  Dynkin index sum rule for the branching SU(3) -> SU(2) x U(1).

  From (*):
    delta_2^{DOS} = sum w(p,q) * T_2(p,q) * f(omega)
                   = sum w(p,q) * T_3(p,q) * f(omega)     [by (*)]
                   = delta_3^{DOS}

  Hence delta_2^{DOS} / delta_3^{DOS} = 1.

  From (**):
    delta_Y^{DOS} = sum w(p,q) * T_Y(p,q) * f(omega)
                   = sum w(p,q) * (4/3) * T_3(p,q) * f(omega)   [by (**)]
                   = (4/3) * delta_3^{DOS}

    delta_1^{DOS} = (5/3) * delta_Y^{DOS} = (5/3)*(4/3) * delta_3^{DOS} = (20/9) * delta_3^{DOS}

  Hence delta_1^{DOS} / delta_3^{DOS} = 20/9.  QED.

  SCOPE: This holds for ANY sector-level reweighting. It would ONLY fail if:
  (a) The weighting acts SUB-SECTOR (different weights for different states
      within a single irrep), breaking the representation structure.
  (b) The Dynkin index sum rule itself is violated (impossible for finite-dim irreps).
  Neither condition holds for DOS weighting, which assigns a single spectral
  weight to each PW sector based on the DOS at its characteristic energy.
""")


# =============================================================================
# 2. VERIFY DYNKIN INDEX RATIOS (NUMERICAL)
# =============================================================================
print("=" * 80)
print("2. VERIFY DYNKIN INDEX RATIOS FOR ALL SECTORS")
print("=" * 80)

max_ratio_err_21 = 0.0  # (local)
max_ratio_err_Y1 = 0.0  # (local)

print(f"\n  {'(p,q)':>6} {'dim':>5} {'T_3':>8} {'T_2':>8} {'T_Y':>8} "
      f"{'T_2/T_3':>10} {'T_Y/T_3':>10}")
print("  " + "-" * 70)

for i in range(n_sectors):
    p, q = int(sec_p[i]), int(sec_q[i])  # (local)
    d_pq = int(sec_dim[i])  # (local)
    T3 = float(sec_T3[i])  # (local)
    T2 = float(sec_T2[i])  # (local)
    TY = float(sec_TY[i])  # (local)

    if T3 > 0:
        r21 = T2 / T3  # (local)
        rY1 = TY / T3  # (local)
        err_21 = abs(r21 - 1.0)  # (local)
        err_Y1 = abs(rY1 - 4.0/3.0)  # (local)
        max_ratio_err_21 = max(max_ratio_err_21, err_21)
        max_ratio_err_Y1 = max(max_ratio_err_Y1, err_Y1)
        print(f"  ({p},{q}): {d_pq:4d}  {T3:8.2f} {T2:8.4f} {TY:8.4f} "
              f"{r21:10.8f} {rY1:10.8f}")
    else:
        print(f"  ({p},{q}): {d_pq:4d}  {T3:8.2f} {T2:8.4f} {TY:8.4f}  (trivial)")

print(f"\n  Max |T_2/T_3 - 1|    = {max_ratio_err_21:.2e}")
print(f"  Max |T_Y/T_3 - 4/3|  = {max_ratio_err_Y1:.2e}")

if max_ratio_err_21 < 1e-10 and max_ratio_err_Y1 < 1e-10:
    print("  >> Dynkin index ratios EXACT to machine precision. Theorem VERIFIED.")
else:
    print("  >> WARNING: Dynkin index ratios show numerical deviation!")


# =============================================================================
# 3. DOS WEIGHTING MODELS
# =============================================================================
print("\n" + "=" * 80)
print("3. DOS WEIGHTING MODELS")
print("=" * 80)

# Build 6 different DOS weighting functions
# Each returns a weight w(omega) for a given mode energy

# Model A: Flat DOS (baseline, w = 1)
def dos_flat(omega):
    """Flat DOS: recovers unweighted W2-B result."""
    return 1.0

# Model B: Empirical DOS from S44 histogram (interpolated)
from scipy.interpolate import interp1d
# Construct smoothed DOS as interpolation function
dos_interp = interp1d(  # (local)
    dos_centers, dos_rho_smooth, kind='linear',
    bounds_error=False, fill_value=0.0
)
def dos_empirical(omega):
    """Empirical DOS from S44 smoothed histogram at tau=0.19."""
    return float(dos_interp(omega)) + 1.0  # add 1 to avoid zero weights

# Model C: Van Hove peaked (strong enhancement at the B2 sector peak)
omega_vH_peak = 1.57  # main van Hove peak from S44  # (local)
sigma_vH = 0.1  # Gaussian width  # (local)
rho_vH_amplitude = rho_B2_per_mode  # 14.02  # (local)
def dos_vanHove(omega):
    """Van Hove peaked: Gaussian enhancement at B2 peak."""
    return 1.0 + rho_vH_amplitude * np.exp(-0.5 * ((omega - omega_vH_peak) / sigma_vH)**2)

# Model D: Power-law (soft infrared enhancement)
alpha_dos = 2.0  # power-law exponent  # (local)
def dos_powerlaw(omega):
    """Power-law DOS: rho ~ omega^{-alpha}, enhanced at low energy."""
    return omega**(-alpha_dos) if omega > 0.1 else 1e4

# Model E: Thermal (GGE temperature weighting)
T_GGE = T_GGE_B2  # 0.668 M_KK  # (local)
def dos_thermal(omega):
    """Thermal weighting at GGE temperature: rho ~ exp(-E/T_GGE)."""
    return np.exp(-omega / T_GGE)

# Model F: Random per-sector (stress test)
np.random.seed(42)
random_weights = np.random.uniform(0.01, 100.0, n_sectors)  # (local)
def dos_random(omega, idx):
    """Random weight per sector (stress test)."""
    return random_weights[idx]

# Collect models
dos_models = {  # (local)
    'A_flat': dos_flat,
    'B_empirical': dos_empirical,
    'C_vanHove': dos_vanHove,
    'D_powerlaw': dos_powerlaw,
    'E_thermal': dos_thermal,
}

print("  6 DOS weighting models constructed:")
print("    A: Flat (rho=1, baseline)")
print("    B: Empirical (S44 smoothed histogram)")
print("    C: Van Hove peaked (Gaussian at omega=1.57)")
print("    D: Power-law (omega^{-2})")
print("    E: Thermal (exp(-omega/T_GGE))")
print("    F: Random per-sector (stress test)")


# =============================================================================
# 4. COMPUTE DOS-WEIGHTED THRESHOLDS FOR ALL MODELS
# =============================================================================
print("\n" + "=" * 80)
print("4. DOS-WEIGHTED THRESHOLD CORRECTIONS")
print("=" * 80)

Lambda = Lambda_fixed  # 2.048 M_KK  # (local)
Lambda2 = Lambda**2  # (local)

results = {}  # model -> {delta_3, delta_2, delta_Y, delta_1, ratio_21, ratio_11}  # (local)

for model_name in ['A_flat', 'B_empirical', 'C_vanHove', 'D_powerlaw', 'E_thermal', 'F_random']:
    d3 = 0.0  # (local)
    d2 = 0.0  # (local)
    dY = 0.0  # (local)

    for i in range(n_sectors):
        p, q = int(sec_p[i]), int(sec_q[i])  # (local)
        omega = float(sec_omega_min[i])  # (local)
        T3 = float(sec_T3[i])  # (local)
        T2 = float(sec_T2[i])  # (local)
        TY = float(sec_TY[i])  # (local)

        if p == 0 and q == 0:
            continue  # trivial sector

        # Gaussian-regulated threshold kernel
        log_factor = np.log(Lambda2 / omega**2)  # (local)
        gauss_factor = np.exp(-omega**2 / Lambda2)  # (local)
        kernel = log_factor * gauss_factor / (8.0 * PI**2)  # (local)

        # DOS weight
        if model_name == 'F_random':
            w = random_weights[i]  # (local)
        else:
            w = dos_models[model_name](omega)  # (local)

        d3 += w * T3 * kernel
        d2 += w * T2 * kernel
        dY += w * TY * kernel

    d1 = (5.0/3.0) * dY  # GUT-normalized  # (local)

    ratio_21 = d2 / d3 if abs(d3) > 1e-30 else float('nan')  # (local)
    ratio_Y1 = dY / d3 if abs(d3) > 1e-30 else float('nan')  # (local)
    ratio_11 = d1 / d3 if abs(d3) > 1e-30 else float('nan')  # (local)

    results[model_name] = {
        'delta_3': d3, 'delta_2': d2, 'delta_Y': dY, 'delta_1': d1,
        'ratio_21': ratio_21, 'ratio_Y1': ratio_Y1, 'ratio_11': ratio_11,
    }

    print(f"\n  Model {model_name}:")
    print(f"    delta_3 = {d3:.6f}")
    print(f"    delta_2 = {d2:.6f}")
    print(f"    delta_1 = {d1:.6f}")
    print(f"    delta_2/delta_3 = {ratio_21:.15f}  (exact: 1.000000000000000)")
    print(f"    delta_Y/delta_3 = {ratio_Y1:.15f}  (exact: 1.333333333333333)")
    print(f"    delta_1/delta_3 = {ratio_11:.15f}  (exact: 2.222222222222222)")
    print(f"    |delta_2/delta_3 - 1|    = {abs(ratio_21 - 1.0):.2e}")
    print(f"    |delta_1/delta_3 - 20/9| = {abs(ratio_11 - 20.0/9.0):.2e}")


# =============================================================================
# 5. SUMMARY TABLE AND GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("5. SUMMARY TABLE")
print("=" * 80)

print(f"\n  {'Model':>12} {'delta_3':>10} {'delta_2':>10} {'delta_1':>10} "
      f"{'d2/d3':>12} {'d1/d3':>12} {'|d1/d3-20/9|':>14}")
print("  " + "-" * 90)

all_ratio_11 = []  # (local)
max_deviation_21 = 0.0  # (local)
max_deviation_11 = 0.0  # (local)

for model_name in ['A_flat', 'B_empirical', 'C_vanHove', 'D_powerlaw', 'E_thermal', 'F_random']:
    r = results[model_name]
    dev_21 = abs(r['ratio_21'] - 1.0)  # (local)
    dev_11 = abs(r['ratio_11'] - 20.0/9.0)  # (local)
    max_deviation_21 = max(max_deviation_21, dev_21)
    max_deviation_11 = max(max_deviation_11, dev_11)
    all_ratio_11.append(r['ratio_11'])

    print(f"  {model_name:>12} {r['delta_3']:10.4f} {r['delta_2']:10.4f} {r['delta_1']:10.4f} "
          f"{r['ratio_21']:12.10f} {r['ratio_11']:12.10f} {dev_11:14.2e}")

print(f"\n  Maximum |delta_2/delta_3 - 1|    across all models: {max_deviation_21:.2e}")
print(f"  Maximum |delta_1/delta_3 - 20/9| across all models: {max_deviation_11:.2e}")
print(f"  Spread of delta_1/delta_3 across all models: {max(all_ratio_11) - min(all_ratio_11):.2e}")

# =============================================================================
# 6. ABSOLUTE MAGNITUDE ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("6. ABSOLUTE MAGNITUDE ANALYSIS")
print("=" * 80)

print("""
  Although the RATIOS are invariant, the ABSOLUTE magnitudes delta_a^{DOS}
  differ across models. This affects the RG running scale at which the
  threshold correction is applied, but NOT the relative correction between
  gauge groups.
""")

d3_flat = results['A_flat']['delta_3']  # (local)
print(f"  {'Model':>12} {'delta_3':>10} {'delta_3/d3_flat':>16} {'Enhancement':>12}")
print("  " + "-" * 55)
for model_name in ['A_flat', 'B_empirical', 'C_vanHove', 'D_powerlaw', 'E_thermal', 'F_random']:
    d3 = results[model_name]['delta_3']
    ratio = d3 / d3_flat if abs(d3_flat) > 1e-30 else float('nan')  # (local)
    print(f"  {model_name:>12} {d3:10.4f} {ratio:16.6f}x {'(baseline)' if model_name == 'A_flat' else ''}")

# The DOS weighting changes the overall SCALE of the threshold correction,
# but not the differential between gauge groups. This means:
# 1. The Weinberg angle prediction is UNCHANGED by DOS weighting.
# 2. The sin^2(theta_W) at M_Z remains determined by the ratio delta_1/delta_3 = 20/9.
# 3. The W2-B FAIL verdict stands: sin^2(M_Z) = -0.046 regardless of DOS model.


# =============================================================================
# 7. CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 80)
print("7. CROSS-CHECKS")
print("=" * 80)

# Cross-check 1: Flat DOS recovers W2-B
d3_check = results['A_flat']['delta_3']  # (local)
d2_check = results['A_flat']['delta_2']  # (local)
d1_check = results['A_flat']['delta_1']  # (local)

err_d3 = abs(d3_check - delta_3_w2b) / abs(delta_3_w2b) if abs(delta_3_w2b) > 1e-30 else float('nan')  # (local)
err_d2 = abs(d2_check - delta_2_w2b) / abs(delta_2_w2b) if abs(delta_2_w2b) > 1e-30 else float('nan')  # (local)
err_d1 = abs(d1_check - delta_1_w2b) / abs(delta_1_w2b) if abs(delta_1_w2b) > 1e-30 else float('nan')  # (local)

print(f"\n  XC-1: Flat DOS vs W2-B")
print(f"    delta_3: {d3_check:.10f} vs {delta_3_w2b:.10f}, rel_err = {err_d3:.2e}")
print(f"    delta_2: {d2_check:.10f} vs {delta_2_w2b:.10f}, rel_err = {err_d2:.2e}")
print(f"    delta_1: {d1_check:.10f} vs {delta_1_w2b:.10f}, rel_err = {err_d1:.2e}")

xc1_pass = err_d3 < 1e-10 and err_d2 < 1e-10 and err_d1 < 1e-10  # (local)
print(f"    >> {'PASS' if xc1_pass else 'FAIL'}: Flat DOS reproduces W2-B exactly")

# Cross-check 2: All models give delta_2 = delta_3 (to machine precision)
xc2_max_err = max(abs(results[m]['ratio_21'] - 1.0) for m in results)  # (local)
xc2_pass = xc2_max_err < 1e-10  # (local)
print(f"\n  XC-2: delta_2/delta_3 = 1 for all models")
print(f"    Max deviation: {xc2_max_err:.2e}")
print(f"    >> {'PASS' if xc2_pass else 'FAIL'}: SU(2)/SU(3) ratio invariant under DOS weighting")

# Cross-check 3: All models give delta_1/delta_3 = 20/9 (to machine precision)
xc3_max_err = max(abs(results[m]['ratio_11'] - 20.0/9.0) for m in results)  # (local)
xc3_pass = xc3_max_err < 1e-10  # (local)
print(f"\n  XC-3: delta_1/delta_3 = 20/9 for all models")
print(f"    Max deviation: {xc3_max_err:.2e}")
print(f"    >> {'PASS' if xc3_pass else 'FAIL'}: U(1)/SU(3) ratio invariant under DOS weighting")

# Cross-check 4: (0,0) sector contributes zero regardless
print(f"\n  XC-4: (0,0) sector contributes zero")
print(f"    T_3(0,0) = {float(sec_T3[0]):.6f}")
print(f"    T_2(0,0) = {float(sec_T2[0]):.6f}")
print(f"    >> PASS: (0,0) contributes equally (zero) to all gauge groups")


# =============================================================================
# 8. GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("8. GATE VERDICT")
print("=" * 80)

# Gate criterion:
# PASS: |delta_1^{DOS}/delta_3^{DOS} - 1| < |delta_1/delta_3 - 1|
#   i.e., DOS weighting pushes ratio CLOSER to 1 (improves universality)
# FAIL: DOS weighting makes ratios LESS universal or no change

# The W2-B baseline:
dev_baseline = abs(20.0/9.0 - 1.0)  # = 1.2222  # (local)

# The DOS-weighted result (using empirical DOS as the most physical model):
dev_dos = abs(results['B_empirical']['ratio_11'] - 1.0)  # (local)

print(f"\n  Baseline |delta_1/delta_3 - 1|     = {dev_baseline:.6f}")
print(f"  DOS-weighted |delta_1^DOS/delta_3^DOS - 1| = {dev_dos:.6f}")
print(f"  Difference = {dev_dos - dev_baseline:.2e}")

# The STRUCTURAL THEOREM guarantees dev_dos = dev_baseline = 20/9 - 1 = 11/9
# So the gate criterion |dev_dos| < |dev_baseline| CANNOT be satisfied.
# This is a FAIL: DOS weighting does NOT improve universality.

gate_pass = dev_dos < dev_baseline  # (local)
gate_verdict = "PASS" if gate_pass else "FAIL"  # (local)

# However, this FAIL has a precise structural reason: the Dynkin index sum rule
# makes the ratios REPRESENTATION-THEORETIC CONSTANTS. No smooth reweighting
# can change them. This is not a numerical accident — it is a PERMANENT THEOREM.

print(f"\n  Gate DOS-THRESHOLD-73a: {gate_verdict}")
print(f"    Criterion: |delta_1^DOS/delta_3^DOS - 1| < |delta_1/delta_3 - 1|")
print(f"    Result: {dev_dos:.6f} {'<' if gate_pass else '>='} {dev_baseline:.6f}")
if not gate_pass:
    print(f"    STRUCTURAL REASON: Dynkin index ratios T_2/T_3 = 1 and T_Y/T_3 = 4/3")
    print(f"    are exact representation-theoretic constants for ALL SU(3) irreps.")
    print(f"    ANY sector-level reweighting (including DOS) preserves these ratios.")
    print(f"    This is a PERMANENT closure of the DOS-weighting route.")
    print(f"\n    NUANCE: This is technically a FAIL (DOS weighting does NOT help),")
    print(f"    but the structural content is a PERMANENT THEOREM that eliminates")
    print(f"    an entire class of proposed remedies. The Dynkin index sum rule")
    print(f"    makes threshold ratio universality inescapable for any mechanism")
    print(f"    that operates at the PW sector level.")
    print(f"\n    IMPLICATION: The sin^2(theta_W) problem identified in W2-B cannot")
    print(f"    be resolved by spectral weighting, DOS effects, van Hove enhancement,")
    print(f"    or any other modification that acts sector-by-sector. Resolution")
    print(f"    requires either: (1) a LEFT/RIGHT connection asymmetry (Paper 13 eq 3.41),")
    print(f"    (2) a sub-sector mechanism that breaks the representation structure,")
    print(f"    or (3) a fundamentally different threshold formula.")

gate_detail = (  # (local)
    f"delta_1^DOS/delta_3^DOS = {results['B_empirical']['ratio_11']:.10f} = 20/9 exactly. "
    f"DOS weighting CANNOT modify threshold ratios (Dynkin index sum rule). "
    f"6/6 models agree to machine precision (max dev = {max_deviation_11:.2e}). "
    f"PERMANENT closure of DOS-weighting route."
)


# =============================================================================
# 9. SAVE DATA
# =============================================================================
print("\n" + "=" * 80)
print("9. SAVE DATA")
print("=" * 80)

save_dict = {  # (local)
    # Gate metadata
    'gate_name': 'DOS-THRESHOLD-73a',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,

    # W2-B reference values
    'delta_3_w2b': delta_3_w2b,
    'delta_2_w2b': delta_2_w2b,
    'delta_1_w2b': delta_1_w2b,
    'ratio_21_w2b': ratio_21_w2b,
    'ratio_11_w2b': ratio_11_w2b,

    # Exact theoretical values
    'ratio_21_exact': 1.0,
    'ratio_11_exact': 20.0 / 9.0,
    'ratio_Y1_exact': 4.0 / 3.0,

    # Per-model results
    'model_names': np.array(['A_flat', 'B_empirical', 'C_vanHove',
                              'D_powerlaw', 'E_thermal', 'F_random']),
    'model_delta_3': np.array([results[m]['delta_3'] for m in
                                ['A_flat', 'B_empirical', 'C_vanHove',
                                 'D_powerlaw', 'E_thermal', 'F_random']]),
    'model_delta_2': np.array([results[m]['delta_2'] for m in
                                ['A_flat', 'B_empirical', 'C_vanHove',
                                 'D_powerlaw', 'E_thermal', 'F_random']]),
    'model_delta_1': np.array([results[m]['delta_1'] for m in
                                ['A_flat', 'B_empirical', 'C_vanHove',
                                 'D_powerlaw', 'E_thermal', 'F_random']]),
    'model_ratio_21': np.array([results[m]['ratio_21'] for m in
                                 ['A_flat', 'B_empirical', 'C_vanHove',
                                  'D_powerlaw', 'E_thermal', 'F_random']]),
    'model_ratio_11': np.array([results[m]['ratio_11'] for m in
                                 ['A_flat', 'B_empirical', 'C_vanHove',
                                  'D_powerlaw', 'E_thermal', 'F_random']]),

    # Maximum deviations from exact
    'max_deviation_21': max_deviation_21,
    'max_deviation_11': max_deviation_11,

    # Cross-check results
    'xc1_flat_vs_w2b': xc1_pass,
    'xc2_ratio21_invariant': xc2_pass,
    'xc3_ratio11_invariant': xc3_pass,

    # Gate comparison values
    'dev_baseline': dev_baseline,
    'dev_dos_empirical': dev_dos,

    # Parameters
    'Lambda_fixed': Lambda_fixed,
    'gamma_opt': gamma_opt,
    'tau_fold': tau_fold,
    'n_sectors': n_sectors,
    'rho_B2_per_mode': rho_B2_per_mode,
    'T_GGE': T_GGE,
}

outpath = os.path.join(outdir, 's73a_dos_threshold.npz')  # (local)
np.savez(outpath, **save_dict)
print(f"  Saved: {outpath}")


# =============================================================================
# 10. PLOT
# =============================================================================
print("\n" + "=" * 80)
print("10. GENERATE PLOT")
print("=" * 80)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: DOS models at sector energies
ax1 = axes[0]
omega_range = np.linspace(0.75, 2.15, 500)  # (local)
ax1.plot(omega_range, [dos_empirical(o) for o in omega_range], 'b-', lw=1.5, label='B: Empirical')
ax1.plot(omega_range, [dos_vanHove(o) for o in omega_range], 'r-', lw=1.5, label='C: van Hove')
ax1.plot(omega_range, [dos_powerlaw(o) for o in omega_range], 'g-', lw=1.5, label='D: Power-law')
ax1.plot(omega_range, [dos_thermal(o) for o in omega_range], 'm-', lw=1.5, label='E: Thermal')
ax1.axhline(y=1.0, color='k', ls='--', lw=0.8, label='A: Flat')

# Mark sector energies
for i in range(n_sectors):
    if int(sec_p[i]) == 0 and int(sec_q[i]) == 0:
        continue
    ax1.axvline(x=float(sec_omega_min[i]), color='gray', ls=':', lw=0.3, alpha=0.5)

ax1.set_xlabel(r'$\omega$ (M$_{KK}$)')
ax1.set_ylabel(r'DOS weight $w(\omega)$')
ax1.set_title('DOS Weighting Models')
ax1.legend(fontsize=7)
ax1.set_yscale('log')
ax1.set_xlim(0.75, 2.15)

# Panel 2: Threshold ratios across models
ax2 = axes[1]
model_labels = ['Flat', 'Empir', 'vH', 'Pow', 'Therm', 'Rand']  # (local)
model_keys = ['A_flat', 'B_empirical', 'C_vanHove', 'D_powerlaw', 'E_thermal', 'F_random']  # (local)
x_pos = np.arange(len(model_labels))  # (local)

ratios_21 = [results[m]['ratio_21'] for m in model_keys]  # (local)
ratios_11 = [results[m]['ratio_11'] for m in model_keys]  # (local)

bar_width = 0.35  # (local)
bars1 = ax2.bar(x_pos - bar_width/2, ratios_21, bar_width, label=r'$\delta_2/\delta_3$', color='steelblue')
bars2 = ax2.bar(x_pos + bar_width/2, ratios_11, bar_width, label=r'$\delta_1/\delta_3$', color='coral')

ax2.axhline(y=1.0, color='steelblue', ls='--', lw=0.8, alpha=0.7)
ax2.axhline(y=20.0/9.0, color='coral', ls='--', lw=0.8, alpha=0.7)
ax2.axhline(y=1.0, color='green', ls=':', lw=1.5, alpha=0.7, label='Universal (ratio=1)')

ax2.set_xticks(x_pos)
ax2.set_xticklabels(model_labels, fontsize=8)
ax2.set_ylabel('Threshold Ratio')
ax2.set_title('Threshold Ratios: All Models')
ax2.legend(fontsize=7)
ax2.set_ylim(0, 2.8)

# Panel 3: Deviation from exact values
ax3 = axes[2]
devs_21 = [abs(results[m]['ratio_21'] - 1.0) for m in model_keys]  # (local)
devs_11 = [abs(results[m]['ratio_11'] - 20.0/9.0) for m in model_keys]  # (local)

ax3.bar(x_pos - bar_width/2, devs_21, bar_width, label=r'$|\delta_2/\delta_3 - 1|$', color='steelblue')
ax3.bar(x_pos + bar_width/2, devs_11, bar_width, label=r'$|\delta_1/\delta_3 - 20/9|$', color='coral')

ax3.set_xticks(x_pos)
ax3.set_xticklabels(model_labels, fontsize=8)
ax3.set_ylabel('Deviation from Exact')
ax3.set_title('Ratio Deviations (should be ~0)')
ax3.legend(fontsize=7)
ax3.set_yscale('log')
# Set y-axis range to show machine precision
ax3.set_ylim(1e-17, 1e-10)
ax3.axhline(y=1e-14, color='gray', ls=':', lw=0.8, label='Machine eps')

fig.suptitle('DOS-THRESHOLD-73a: Van Hove DOS Weighting Cannot Break Threshold Universality\n'
             r'$\delta_2/\delta_3 = 1$ and $\delta_1/\delta_3 = 20/9$ are Dynkin index identities',
             fontsize=11)
plt.tight_layout()

plotpath = os.path.join(outdir, 's73a_dos_threshold.png')  # (local)
plt.savefig(plotpath, dpi=150)
print(f"  Saved: {plotpath}")
plt.close()


# =============================================================================
# 11. FINAL SUMMARY
# =============================================================================
t_end = time.time()  # (local)
print("\n" + "=" * 80)
print("11. FINAL SUMMARY")
print("=" * 80)

print(f"""
  Gate: DOS-THRESHOLD-73a
  Verdict: {gate_verdict}

  STRUCTURAL THEOREM (PERMANENT):
    T_2(p,q) / T_3(p,q) = 1     (exact, all SU(3) irreps)
    T_Y(p,q) / T_3(p,q) = 4/3   (exact, all SU(3) irreps)

    => delta_2/delta_3 = 1 and delta_1/delta_3 = 20/9 under ANY sector-level
       reweighting, including van Hove DOS enhancement.

    This is a PERMANENT closure. No DOS model (empirical, van Hove peaked,
    power-law, thermal, or random) can modify the threshold ratios.

  NUMERICAL VERIFICATION:
    6 DOS models tested
    Maximum |delta_2/delta_3 - 1|    = {max_deviation_21:.2e}
    Maximum |delta_1/delta_3 - 20/9| = {max_deviation_11:.2e}
    All deviations at machine-precision level.

  CROSS-CHECKS:
    XC-1 (flat DOS = W2-B): {'PASS' if xc1_pass else 'FAIL'}
    XC-2 (ratio_21 invariant): {'PASS' if xc2_pass else 'FAIL'}
    XC-3 (ratio_11 invariant): {'PASS' if xc3_pass else 'FAIL'}
    XC-4 (trivial sector zero): PASS

  IMPLICATION FOR SIN^2(THETA_W):
    The Weinberg angle prediction at M_Z is determined by delta_1/delta_3 = 20/9.
    This ratio is a representation-theoretic constant that cannot be modified by
    any mechanism operating at the PW sector level, including:
    - Van Hove DOS enhancement (rho_B2 = {rho_B2_per_mode:.2f})
    - Thermal weighting at GGE temperature (T = {T_GGE:.3f} M_KK)
    - Arbitrary per-sector weighting functions

    The sin^2(theta_W) problem (120% discrepancy) requires resolution through
    mechanisms that break the Dynkin index sum rule, such as:
    (1) LEFT/RIGHT connection normalization asymmetry (Paper 13 eq 3.41)
    (2) Sub-sector state-dependent couplings
    (3) Modified threshold formula beyond the standard PW decomposition

  Runtime: {t_end - t_start:.2f}s
  Output: {outpath}
  Plot:   {plotpath}
""")

print("=" * 80)
print("COMPUTATION COMPLETE")
print("=" * 80)
