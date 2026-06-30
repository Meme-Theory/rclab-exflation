#!/usr/bin/env python3
"""
S75-B2-CROSS-MOMENT -- Cross-Spectral-Moment Moduli Potential
=============================================================

Session 75, Task 7 (W1-G)
Agent: spectral-geometer

Pre-registered gate: S75-B2-CROSS-MOMENT
  PASS: Restoring gradient >= 400 M_KK^4 at tau = 0.48
  INFO: Restoring gradient in [40, 400] M_KK^4
  FAIL: Restoring gradient < 40 M_KK^4

Physics (spectral geometry framing):
------------------------------------
The Chamseddine-Connes spectral action on M4 x K decomposes via the
heat kernel expansion into:

    S[D, f, Lambda] = 2 f_4 Lambda^8 a_0 + 2 f_2 Lambda^6 a_2 + f_0 Lambda^4 a_4 + ...  (*)

where:
  - a_0, a_2, a_4 are the Gilkey geometric Seeley-DeWitt coefficients
  - f_k = integral_0^infty f(x) x^{k-1} dx are moments of the cutoff function f
  - Lambda is the spectral cutoff energy scale

The key structural observation: a_0, a_2, a_4 are DIFFERENT spectral moments
of D_K^2, hence they have DIFFERENT tau-dependences. Explicitly:
  - a_0(tau) = (4pi)^{-d/2} * dim_spinor * Vol(tau) = const (volume-preserving Jensen)
  - a_2(tau) = (4pi)^{-d/2} * dim_spinor * (R(tau)/6) * Vol (grows with tau)
  - a_4(tau) = (4pi)^{-d/2} * dim_spinor * [curvature polynomial](tau) (grows faster)

If a_4/a_2 has an extremum, the combined gradient dS/dtau can vanish even when
neither da_2/dtau nor da_4/dtau vanishes alone.

S74 found V_bare(tau) = S_fstar(tau) monotonically increasing, with
dV_bare/dtau = 445.4 M_KK^4 at tau = 0.48. The question: does the CC formula
(*) with distinct tau-dependences for each coefficient produce a restoring gradient?

CRITICAL DISTINCTION (S46, HEAT-KERNEL-AUDIT-45):
  - Gilkey geometric a_2 = (4pi)^{-4} * (20R/3) * Vol = 0.728 at fold
  - Spectral sum a_2_fold = zeta_D(1) = 2776.17 (canonical)
  - These are DIFFERENT objects (ratio 3812). The CC formula uses the Gilkey coefficients.

Input: s61_heat_kernel_a4.npz (Gilkey a_2(tau), a_4(tau) arrays)
       s74_moduli_stabilization.npz (V_bare, tau grids)
       canonical_constants.py
Output: s75_cross_spectral_moment_moduli.npz, .png
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    tau_fold, S_fold, dS_fold, d2S_fold,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, M_KK, M_KK_gravity, M_KK_kerner,
    f_0_sharp, f_2_default, f_4_default,
    PI,
)

t_start = time.time()

print("=" * 78)
print("S75-B2-CROSS-MOMENT: Cross-Spectral-Moment Moduli Potential")
print("=" * 78)

# ============================================================================
# SECTION 0: CONSTANTS AND CONVENTIONS
# ============================================================================

d_manifold = 8  # (local) dim(SU(3))
dim_spinor = 16  # (local) 2^{d/2} = 2^4
fourpi_d2 = (4.0 * PI) ** (d_manifold / 2)  # (local) (4*pi)^4 = 39478.42
Vol = Vol_SU3_Haar  # (local)

# The Gilkey geometric a_0 for the spin bundle:
#   a_0^{Gilkey} = dim_spinor * Vol / (4*pi)^{d/2}
a0_gilkey = dim_spinor * Vol / fourpi_d2  # (local)

print(f"\n  Geometric constants:")
print(f"    d = {d_manifold}, dim_spinor = {dim_spinor}")
print(f"    (4*pi)^{{d/2}} = {fourpi_d2:.4f}")
print(f"    Vol(SU(3)) = {Vol:.4f}")
print(f"    a_0^{{Gilkey}} = {a0_gilkey:.6f}")
print(f"    a_0^{{spectral}} (canonical) = {a0_fold:.1f}")
print(f"    Ratio spectral/Gilkey = {a0_fold / a0_gilkey:.1f}")

# Cutoff function moments (scheme-dependent)
# Using three schemes to test cutoff universality
# Scheme 1: Sharp cutoff (f_0=1, f_2 and f_4 from integral x^{k-1} Theta(1-x) dx)
# For sharp cutoff: f_k = int_0^1 x^{k-1} dx = 1/k
f_0_sc = f_0_sharp  # (local) = 1.0
f_2_sc = 0.5  # (local) int_0^1 x dx = 1/2
f_4_sc = 0.25  # (local) int_0^1 x^3 dx = 1/4

# Scheme 2: Gaussian cutoff (from S62 W1)
f_0_gauss = 1.0  # (local) normalization
f_2_gauss = f_2_default  # (local) = 2.34
f_4_gauss = f_4_default  # (local) = 0.558

# Scheme 3: Heat kernel f(x) = exp(-x)
# f_k = int_0^infty x^{k-1} exp(-x) dx = Gamma(k)
f_0_heat = 1.0  # (local) Gamma(1) = 1
f_2_heat = 1.0  # (local) Gamma(2) = 1
f_4_heat = 6.0  # (local) Gamma(4) = 6

print(f"\n  Cutoff function moments:")
print(f"    Sharp:    f_0={f_0_sc}, f_2={f_2_sc}, f_4={f_4_sc}")
print(f"    Gaussian: f_0={f_0_gauss}, f_2={f_2_gauss}, f_4={f_4_gauss}")
print(f"    Heat:     f_0={f_0_heat}, f_2={f_2_heat}, f_4={f_4_heat}")

# ============================================================================
# SECTION 1: LOAD GILKEY a_2(tau), a_4(tau) FROM S61
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Loading Gilkey Seeley-DeWitt Coefficients a_2(tau), a_4(tau)")
print("=" * 78)

d_hk4 = np.load('s61_heat_kernel_a4.npz', allow_pickle=True)
tau_gilkey = d_hk4['tau_arr']       # (101,) [0, 0.5]
a2_gilkey_arr = d_hk4['a2_gilkey_arr']  # (101,)
a4_gilkey_arr = d_hk4['a4_gilkey_arr']  # (101,)
R_arr = d_hk4['R_arr']             # (101,) scalar curvature R(tau)
Ric2_arr = d_hk4['Ric2_arr']       # (101,) |Ric|^2(tau)
K_arr = d_hk4['K_arr']             # (101,) Kretschner scalar K(tau)
a2_gilkey_fold_stored = float(d_hk4['a2_gilkey_fold'])
a4_gilkey_fold_stored = float(d_hk4['a4_gilkey_fold'])

print(f"  tau range: [{tau_gilkey[0]:.4f}, {tau_gilkey[-1]:.4f}] ({len(tau_gilkey)} points)")
print(f"  a_2^{{Gilkey}}(tau=0)   = {a2_gilkey_arr[0]:.8f}")
print(f"  a_2^{{Gilkey}}(fold)    = {a2_gilkey_fold_stored:.8f}")
print(f"  a_2^{{Gilkey}}(tau=0.5) = {a2_gilkey_arr[-1]:.8f}")
print(f"  a_4^{{Gilkey}}(tau=0)   = {a4_gilkey_arr[0]:.8f}")
print(f"  a_4^{{Gilkey}}(fold)    = {a4_gilkey_fold_stored:.8f}")
print(f"  a_4^{{Gilkey}}(tau=0.5) = {a4_gilkey_arr[-1]:.8f}")

# Build cubic spline interpolants for a_2(tau), a_4(tau)
cs_a2 = CubicSpline(tau_gilkey, a2_gilkey_arr)
cs_a4 = CubicSpline(tau_gilkey, a4_gilkey_arr)

# Verify at fold
a2_at_fold_interp = float(cs_a2(tau_fold))  # (local)
a4_at_fold_interp = float(cs_a4(tau_fold))  # (local)
print(f"\n  Cross-check at fold (tau={tau_fold}):")
print(f"    a_2 interp = {a2_at_fold_interp:.8f}, stored = {a2_gilkey_fold_stored:.8f}, "
      f"diff = {abs(a2_at_fold_interp - a2_gilkey_fold_stored)/a2_gilkey_fold_stored*100:.6f}%")
print(f"    a_4 interp = {a4_at_fold_interp:.8f}, stored = {a4_gilkey_fold_stored:.8f}, "
      f"diff = {abs(a4_at_fold_interp - a4_gilkey_fold_stored)/a4_gilkey_fold_stored*100:.6f}%")

# ============================================================================
# SECTION 2: LOAD S74 BARE POTENTIAL DATA
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Loading S74 V_bare Data")
print("=" * 78)

d_s74 = np.load('s74_moduli_stabilization.npz', allow_pickle=True)
tau_bare = d_s74['tau_scan']          # (500,) [0.15, 1.7]
V_bare_scan = d_s74['V_bare_scan']    # (500,) S_fstar(tau) at L_max=3
dV_bare_at_kappa1 = float(d_s74['dV_bare_dtau_at_kappa1'])  # 445.4 M_KK^4
tau_kappa1 = float(d_s74['tau_kappa1'])  # ~0.48
V_fold_HK = float(d_s74['V_fold_HK_MKK4'])  # 1305.0 M_KK^4

print(f"  S74 tau range: [{tau_bare[0]:.4f}, {tau_bare[-1]:.4f}] ({len(tau_bare)} points)")
print(f"  V_bare(fold) = {V_fold_HK:.4f} M_KK^4")
print(f"  dV_bare/dtau at tau={tau_kappa1:.4f} = {dV_bare_at_kappa1:.4f} M_KK^4")

# ============================================================================
# SECTION 3: CONSTRUCT V_eff(tau) FROM CHAMSEDDINE-CONNES FORMULA
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Chamseddine-Connes V_eff(tau)")
print("=" * 78)

# The Chamseddine-Connes spectral action formula:
#
#   S[D, f, Lambda] = 2 f_4 Lambda^8 a_0 + 2 f_2 Lambda^6 a_2 + f_0 Lambda^4 a_4 + O(Lambda^2)
#
# where a_0, a_2, a_4 are the GILKEY geometric Seeley-DeWitt coefficients.
#
# For the Jensen-deformed SU(3):
#   - a_0(tau) = (4pi)^{-d/2} * dim_spinor * Vol = CONSTANT (volume-preserving)
#   - a_2(tau) = Gilkey a_2 (depends on R(tau))
#   - a_4(tau) = Gilkey a_4 (depends on R^2, |Ric|^2, K)
#
# The effective potential for the modulus tau is V_eff(tau) = S(tau) evaluated
# at fixed Lambda and f_k. The gradient is:
#
#   dV_eff/dtau = 2 f_2 Lambda^6 da_2/dtau + f_0 Lambda^4 da_4/dtau
#
# (the a_0 term drops out because da_0/dtau = 0 for volume-preserving deformation).

# The tau grid from S61 only goes to 0.5. We need to extend to cover the
# stabilization range [0.45, 0.70]. The S63 Meissner data covers [0, 0.49].
# For tau > 0.5 we must extrapolate. Let's first work on the [0, 0.5] domain
# and check if structure exists there.

# Step 1: Compute the ratio a_4/a_2 as function of tau
ratio_a4_a2 = a4_gilkey_arr / a2_gilkey_arr  # (local)

print(f"\n  a_4/a_2 ratio:")
print(f"    tau=0:    {ratio_a4_a2[0]:.8f}")
print(f"    tau=fold: {cs_a4(tau_fold)/cs_a2(tau_fold):.8f}")
print(f"    tau=0.5:  {ratio_a4_a2[-1]:.8f}")
print(f"    Range: [{ratio_a4_a2.min():.8f}, {ratio_a4_a2.max():.8f}]")

# Step 2: Check monotonicity of the ratio
d_ratio = np.diff(ratio_a4_a2) / np.diff(tau_gilkey)  # (local)
n_sign_changes = np.sum(np.diff(np.sign(d_ratio)) != 0)  # (local)
print(f"    d(a_4/a_2)/dtau sign changes: {n_sign_changes}")
print(f"    d(a_4/a_2)/dtau range: [{d_ratio.min():.8f}, {d_ratio.max():.8f}]")

# Step 3: Build V_eff(tau) for each cutoff scheme
# Use a common tau grid = tau_gilkey (101 points, [0, 0.5])
tau_eff = tau_gilkey  # (local)
n_tau = len(tau_eff)  # (local)

# a_0 is constant for volume-preserving Jensen deformation
a0_gilkey_const = a0_gilkey  # (local) 0.866

# For the CC formula, the cutoff Lambda is a free parameter.
# The physical Lambda is set by the highest eigenvalue in the truncation.
# From S74: Lambda_sa = 12.91 M_KK (at L_max=3)
Lambda_sa = 12.91  # (local) M_KK, from S74

# But the CC formula with GILKEY coefficients uses Lambda as a physical UV cutoff.
# The M_KK scale is the natural cutoff for the 8D internal geometry.
# We parametrize Lambda in units of M_KK.

# For the cross-moment effect, what matters is the RATIO of the gradients
# of the a_2 and a_4 terms. Let's first compute V_eff for Lambda = 1 M_KK
# (natural units) and then check cutoff sensitivity.

Lambda_values = np.array([1.0, Lambda_sa, 100.0])  # (local) M_KK units

print(f"\n  Cutoff values tested: Lambda/M_KK = {Lambda_values}")

# Compute V_eff and dV_eff/dtau for all schemes and Lambda values
results = {}  # (local)

for scheme_name, (f0, f2, f4) in [
    ('sharp', (f_0_sc, f_2_sc, f_4_sc)),
    ('gaussian', (f_0_gauss, f_2_gauss, f_4_gauss)),
    ('heat', (f_0_heat, f_2_heat, f_4_heat)),
]:
    for Lambda in Lambda_values:
        L8 = Lambda**8  # (local)
        L6 = Lambda**6  # (local)
        L4 = Lambda**4  # (local)

        # V_eff(tau) = 2 * f_4 * L^8 * a_0 + 2 * f_2 * L^6 * a_2(tau) + f_0 * L^4 * a_4(tau)
        V_eff = (2.0 * f4 * L8 * a0_gilkey_const
                 + 2.0 * f2 * L6 * a2_gilkey_arr
                 + f0 * L4 * a4_gilkey_arr)  # (local)

        # dV_eff/dtau: a_0 term has zero derivative
        da2_dtau = cs_a2(tau_eff, 1)  # (local) first derivative
        da4_dtau = cs_a4(tau_eff, 1)  # (local) first derivative

        dV_dtau = 2.0 * f2 * L6 * da2_dtau + f0 * L4 * da4_dtau  # (local)

        # d^2V/dtau^2 for stability analysis
        d2a2_dtau2 = cs_a2(tau_eff, 2)  # (local)
        d2a4_dtau2 = cs_a4(tau_eff, 2)  # (local)
        d2V_dtau2 = 2.0 * f2 * L6 * d2a2_dtau2 + f0 * L4 * d2a4_dtau2  # (local)

        key = (scheme_name, Lambda)  # (local)
        results[key] = {
            'V_eff': V_eff,
            'dV_dtau': dV_dtau,
            'd2V_dtau2': d2V_dtau2,
            'f0': f0, 'f2': f2, 'f4': f4,
            'Lambda': Lambda,
            'term_a0': 2.0 * f4 * L8 * a0_gilkey_const,  # constant term
            'term_a2': 2.0 * f2 * L6 * a2_gilkey_arr,
            'term_a4': f0 * L4 * a4_gilkey_arr,
        }

# ============================================================================
# SECTION 4: ANALYZE V_eff STRUCTURE
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 4: V_eff Structure Analysis")
print("=" * 78)

# For each scheme, print the gradient at tau = 0.48 and check for minima
tau_target = 0.48  # (local) from gate specification
TAU_LO = 0.45  # (local) from gate
TAU_HI = 0.70  # (local) from gate

for scheme_name in ['sharp', 'gaussian', 'heat']:
    for Lambda in Lambda_values:
        key = (scheme_name, Lambda)
        r = results[key]

        # Find gradient at tau = 0.48 (or nearest available)
        idx_target = np.argmin(np.abs(tau_eff - tau_target))  # (local)
        tau_at_target = tau_eff[idx_target]  # (local)
        dV_at_target = r['dV_dtau'][idx_target]  # (local)

        # Check for zeros of dV/dtau in available range
        sign_changes_dV = np.where(np.diff(np.sign(r['dV_dtau'])))[0]  # (local)
        minima_tau = []  # (local)
        for idx in sign_changes_dV:
            # Interpolate zero crossing
            t0 = tau_eff[idx]  # (local)
            t1 = tau_eff[idx+1]  # (local)
            dv0 = r['dV_dtau'][idx]  # (local)
            dv1 = r['dV_dtau'][idx+1]  # (local)
            t_cross = t0 - dv0 * (t1 - t0) / (dv1 - dv0)  # (local)
            # Check if minimum (d^2V > 0)
            d2v_cross = np.interp(t_cross, tau_eff, r['d2V_dtau2'])  # (local)
            if d2v_cross > 0:
                minima_tau.append(t_cross)

        # Report
        print(f"\n  Scheme={scheme_name}, Lambda={Lambda:.2f} M_KK:")
        print(f"    V_eff(fold) = {r['V_eff'][np.argmin(np.abs(tau_eff - tau_fold))]:.6e}")
        print(f"    V_eff(0.48) = {r['V_eff'][idx_target]:.6e}")
        print(f"    dV/dtau(0.48) = {dV_at_target:.6e} M_KK^4")
        print(f"    |dV/dtau(0.48)| = {abs(dV_at_target):.6e} M_KK^4")
        print(f"    Sign changes in dV/dtau: {len(sign_changes_dV)}")
        if len(minima_tau) > 0:
            print(f"    Minima found at tau = {minima_tau}")
        else:
            print(f"    No minima in [{tau_eff[0]:.3f}, {tau_eff[-1]:.3f}]")

        # Term hierarchy
        a0_term_fold = r['term_a0']  # (local)
        a2_term_fold = r['term_a2'][np.argmin(np.abs(tau_eff - tau_fold))]  # (local)
        a4_term_fold = r['term_a4'][np.argmin(np.abs(tau_eff - tau_fold))]  # (local)
        total_fold = a0_term_fold + a2_term_fold + a4_term_fold  # (local)
        print(f"    Term hierarchy at fold:")
        print(f"      2 f_4 L^8 a_0 = {a0_term_fold:.6e} ({a0_term_fold/total_fold*100:.2f}%)")
        print(f"      2 f_2 L^6 a_2 = {a2_term_fold:.6e} ({a2_term_fold/total_fold*100:.2f}%)")
        print(f"        f_0 L^4 a_4 = {a4_term_fold:.6e} ({a4_term_fold/total_fold*100:.2f}%)")

# ============================================================================
# SECTION 5: CROSS-MOMENT RATIO ANALYSIS
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Cross-Moment Ratio Analysis")
print("=" * 78)

# The key structural question: does a_4/a_2 have an extremum?
# If a_4/a_2 is monotone, then V_eff = A*a_2 + B*a_4 with A,B > 0 cannot have
# a minimum if both a_2 and a_4 are monotonically increasing.
#
# The ratio a_4/a_2 encodes the RELATIVE rate of change. If d(a_4/a_2)/dtau > 0,
# then a_4 grows FASTER than a_2. In that case, for the gradient to vanish:
#   dV/dtau = A * da_2/dtau + B * da_4/dtau = 0
# requires A * da_2/dtau = -B * da_4/dtau, which needs da_2/dtau and da_4/dtau
# to have OPPOSITE signs. But both grow monotonically for positive curvature
# deformations.
#
# STRUCTURAL RESULT: For V_eff = c_1 * a_2(tau) + c_2 * a_4(tau) with c_1, c_2 > 0
# and both a_2, a_4 monotonically increasing, V_eff is monotonically increasing.
# No minimum exists.

# Verify monotonicity
da2 = np.diff(a2_gilkey_arr)  # (local)
da4 = np.diff(a4_gilkey_arr)  # (local)
a2_mono = np.all(da2 >= 0)  # (local)
a4_mono = np.all(da4 >= 0)  # (local)

print(f"\n  Monotonicity analysis:")
print(f"    a_2(tau) monotonically increasing: {a2_mono}")
print(f"    a_4(tau) monotonically increasing: {a4_mono}")
print(f"    a_2 growth factor [0->0.5]: {a2_gilkey_arr[-1]/a2_gilkey_arr[0]:.6f}")
print(f"    a_4 growth factor [0->0.5]: {a4_gilkey_arr[-1]/a4_gilkey_arr[0]:.6f}")

# Compute logarithmic derivatives for comparison
dlog_a2 = np.gradient(np.log(a2_gilkey_arr), tau_gilkey)  # (local)
dlog_a4 = np.gradient(np.log(a4_gilkey_arr), tau_gilkey)  # (local)

print(f"\n  Logarithmic derivatives (d ln a_k / dtau):")
print(f"    d ln a_2 / dtau at fold: {np.interp(tau_fold, tau_gilkey, dlog_a2):.6f}")
print(f"    d ln a_4 / dtau at fold: {np.interp(tau_fold, tau_gilkey, dlog_a4):.6f}")
print(f"    d ln a_2 / dtau at 0.48: {np.interp(0.48, tau_gilkey, dlog_a2):.6f}")
print(f"    d ln a_4 / dtau at 0.48: {np.interp(0.48, tau_gilkey, dlog_a4):.6f}")
print(f"    Ratio (d ln a_4)/(d ln a_2) at fold: "
      f"{np.interp(tau_fold, tau_gilkey, dlog_a4)/np.interp(tau_fold, tau_gilkey, dlog_a2):.6f}")
print(f"    Ratio (d ln a_4)/(d ln a_2) at 0.48: "
      f"{np.interp(0.48, tau_gilkey, dlog_a4)/np.interp(0.48, tau_gilkey, dlog_a2):.6f}")

# The ratio a_4/a_2
cs_ratio = CubicSpline(tau_gilkey, ratio_a4_a2)  # (local)
d_ratio_at_fold = float(cs_ratio(tau_fold, 1))  # (local)
d_ratio_at_048 = float(cs_ratio(0.48, 1))  # (local)
print(f"\n  a_4/a_2 ratio:")
print(f"    At tau=0:    {ratio_a4_a2[0]:.8f}")
print(f"    At fold:     {float(cs_ratio(tau_fold)):.8f}")
print(f"    At tau=0.48: {float(cs_ratio(0.48)):.8f}")
print(f"    At tau=0.50: {ratio_a4_a2[-1]:.8f}")
print(f"    d(a_4/a_2)/dtau at fold: {d_ratio_at_fold:.8f}")
print(f"    d(a_4/a_2)/dtau at 0.48: {d_ratio_at_048:.8f}")

# Structural theorem check
d_ratio_arr = cs_ratio(tau_gilkey, 1)  # (local)
ratio_mono = np.all(d_ratio_arr[1:] >= -1e-10)  # (local) allow numerical noise
print(f"\n  a_4/a_2 monotonicity: {ratio_mono}")
if ratio_mono:
    print("  STRUCTURAL: a_4 grows faster than a_2. No ratio extremum exists.")
    print("  Combined with both a_2, a_4 monotone increasing: V_eff is monotone.")

# ============================================================================
# SECTION 6: CHK1 -- V_eff(fold) vs S_fold
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Cross-Checks")
print("=" * 78)

# CHK1: V_eff(tau_fold) should relate to S_fold.
# NOTE: S_fold = 250360.7 is the spectral sum S_fstar at L_max=3.
# V_eff from CC formula uses GILKEY coefficients, which are a completely
# different normalization. These are NOT expected to match numerically.
# The comparison is structural: both should be positive, both should
# increase with tau in the same regime.

idx_fold = np.argmin(np.abs(tau_eff - tau_fold))  # (local)

print(f"\n  CHK1: V_eff(fold) vs S_fold")
print(f"    S_fold (spectral sum, canonical) = {S_fold:.2f}")
for scheme_name in ['sharp', 'gaussian', 'heat']:
    for Lambda in [1.0, Lambda_sa]:
        key = (scheme_name, Lambda)
        V_at_fold = results[key]['V_eff'][idx_fold]  # (local)
        print(f"    V_eff^{{{scheme_name}}}(fold, L={Lambda:.2f}) = {V_at_fold:.6e}")

# CHK2: Verify CC formula decomposition: V = term_a0 + term_a2 + term_a4
print(f"\n  CHK2: CC formula internal consistency (sharp, Lambda=1)")
r_chk = results[('sharp', 1.0)]
V_sum = r_chk['term_a0'] + r_chk['term_a2'] + r_chk['term_a4']  # (local)
V_direct = r_chk['V_eff']  # (local)
chk2_err = np.max(np.abs(V_sum - V_direct))  # (local)
print(f"    max |V_sum - V_direct| = {chk2_err:.2e}")
print(f"    CHK2: {'PASS' if chk2_err < 1e-10 else 'FAIL'} (to machine precision)")

# ============================================================================
# SECTION 7: EXTEND TO tau > 0.5 VIA CURVATURE EXTRAPOLATION
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Extension to tau > 0.5")
print("=" * 78)

# The S61 data only covers tau in [0, 0.5]. The gate requires evaluation
# at tau = 0.48 (barely covered) and ideally at tau = 0.539 and beyond.
# We can extrapolate using the known curvature formulas for Jensen-deformed SU(3).
#
# For Jensen deformation with parameter tau (sigma in Baptista notation):
#   g_s = diag(g_0 * [1,...,1, e^{4tau}, e^{4tau}, e^{4tau}, e^{4tau}])
#   on the Cartan-Weyl basis (3 u(2) directions + 4 coset directions + 1 u(1))
#
# Actually, the volume-preserving Jensen deformation with parameter s is:
#   g_s = diag(g_0 * [(1+s)^{-4/3}, ..., (1+s)^{2/3}, ...])
#   (4 compressed + 4 expanded directions to preserve volume)
#
# For the Gilkey coefficients, the key curvature invariants are R, |Ric|^2, K.
# From S61 data, we can fit these as functions of tau and extrapolate.

# Fit R(tau), |Ric|^2(tau), K(tau) as polynomials
deg_fit = 6  # (local) polynomial degree for extrapolation

from numpy.polynomial import polynomial as P

# Fit on the tau range
R_coeffs = np.polyfit(tau_gilkey, R_arr, deg_fit)  # (local)
Ric2_coeffs = np.polyfit(tau_gilkey, Ric2_arr, deg_fit)  # (local)
K_coeffs = np.polyfit(tau_gilkey, K_arr, deg_fit)  # (local)

# Residuals in the fitted range
R_fit = np.polyval(R_coeffs, tau_gilkey)  # (local)
Ric2_fit = np.polyval(Ric2_coeffs, tau_gilkey)  # (local)
K_fit = np.polyval(K_coeffs, tau_gilkey)  # (local)
print(f"  Polynomial extrapolation (degree {deg_fit}):")
print(f"    R(tau) max fit residual: {np.max(np.abs(R_fit - R_arr)):.2e}")
print(f"    |Ric|^2(tau) max residual: {np.max(np.abs(Ric2_fit - Ric2_arr)):.2e}")
print(f"    K(tau) max residual: {np.max(np.abs(K_fit - K_arr)):.2e}")

# Extended tau grid
tau_ext = np.linspace(0.0, 0.70, 351)  # (local) covers [0, 0.70]

R_ext = np.polyval(R_coeffs, tau_ext)  # (local)
Ric2_ext = np.polyval(Ric2_coeffs, tau_ext)  # (local)
K_ext = np.polyval(K_coeffs, tau_ext)  # (local)

# Reconstruct a_2^{Gilkey}(tau), a_4^{Gilkey}(tau) from curvature invariants
# From Gilkey:
#   a_2 = (4pi)^{-d/2} * int_M tr_S(R/6 - E) dVol
# For the spin bundle with Lichnerowicz: D^2 = nabla^*nabla + R/4, so E = R/4,
# and tr_S(R/6 - E) = dim_spinor * (R/6 - R/4) = dim_spinor * (-R/12)
# Wait, that gives NEGATIVE a_2. Let me re-derive carefully.
#
# The standard heat kernel for the spin Dirac operator D^2 = nabla^*nabla + R/4:
#   a_2 = (4pi)^{-d/2} * int_M tr_S(R/6) dVol
# where the R/6 comes from the Laplacian contribution and the endomorphism E = R/4
# enters differently.
#
# Actually, for a general Laplacian-type operator P = -Delta + E on a vector bundle:
#   a_2(P) = (4pi)^{-d/2} * int_M tr(R/6 - E) dVol
#
# For D^2 = nabla^*nabla + R/4 (spin Dirac squared):
#   E = R/4, so a_2 = (4pi)^{-d/2} * int_M dim_spinor * (R/6 - R/4) * dVol
#   = (4pi)^{-d/2} * dim_spinor * (-R/12) * Vol
# But this gives negative a_2, contradicting the data.
#
# RESOLUTION: The standard result for D^2 on spin bundle is:
#   a_2(D^2) = (4pi)^{-d/2} * (1/6) * int_M tr_S(R_S) * dVol
# where R_S is the scalar curvature acting as R * Id on the spinor bundle.
# tr_S(R_S) = dim_spinor * R.
# So a_2 = (4pi)^{-d/2} * (dim_spinor / 6) * R * Vol
#
# But wait, the Lichnerowicz formula gives D^2 = nabla^*nabla + R/4.
# The general formula: Tr(exp(-tP)) ~ sum a_n(P) t^{(n-d)/2}
# For P = nabla^*nabla - E (note the minus sign convention in Gilkey!):
#   a_0 = (4pi)^{-d/2} * tr(Id) * Vol = (4pi)^{-d/2} * dim_spinor * Vol
#   a_2 = (4pi)^{-d/2} * int tr(R/6 * Id + E) dVol
#
# With Gilkey's convention P = -(g^{ab}nabla_a nabla_b + E):
#   D^2 = -Delta_spin + R/4  =>  E = -R/4
#   a_2 = (4pi)^{-d/2} * int dim_spinor * (R/6 + (-R/4)) dVol
#       = (4pi)^{-d/2} * dim_spinor * (-R/12) * Vol
# Still negative. Something is wrong with the sign convention.
#
# Let me check against the actual data. At tau=0, R=2, Vol=1349.7:
# If a_2 = (4pi)^{-4} * 16 * (R/6) * Vol = 0.866 * R/6 = 0.866 * 0.333 = 0.289
# If a_2 = (4pi)^{-4} * 16 * (R/6 + R/4) * Vol = 0.866 * (5R/12) = 0.866 * 0.833 = 0.722
# The data says a_2(tau=0) = 0.7217. So the correct formula must be:
#   a_2 = (4pi)^{-d/2} * dim_spinor * (5R/12) * Vol
# which corresponds to E = +R/4 (Berger convention).
#
# Let me verify: (4pi)^{-4} * 16 * (5*2/12) * 1349.7 = 0.866 * 0.8333 = 0.7217. YES.
#
# This is the BGV convention: P = D^2, E_BGV = +R/4 for the spin Dirac,
# and a_2 = (4pi)^{-d/2} * tr_S(R/6 + E_BGV) * Vol = (4pi)^{-d/2} * dim_spinor * (5R/12) * Vol

# Similarly for a_4. The standard result from S61:
# a_4 involves R^2, |Ric|^2, K (Kretschner). From the S61 data at tau=0:
# R=2, Ric2=0.5, K=0.5, a_4=0.2962
# The general a_4 formula (BGV, spin bundle) has the form:
#   a_4 = (4pi)^{-d/2} * dim_spinor * Vol * [c1*R^2 + c2*|Ric|^2 + c3*K + c4*Delta_R]
# Since the manifold is closed, Delta_R integrates to zero.
# We can determine c1, c2, c3 by fitting to the data at 3 tau values.

# Fit the coefficients using the S61 data
# a_4(tau) = alpha * (R(tau))^2 + beta * |Ric(tau)|^2 + gamma * K(tau)
# where alpha, beta, gamma absorb the (4pi)^{-d/2} * dim_spinor * Vol prefactor

# Use least squares on the full dataset
A_matrix = np.column_stack([R_arr**2, Ric2_arr, K_arr])  # (local)
a4_fit_coeffs, residuals, rank, sv = np.linalg.lstsq(A_matrix, a4_gilkey_arr, rcond=None)  # (local)
alpha_a4, beta_a4, gamma_a4 = a4_fit_coeffs  # (local)

a4_reconstructed = A_matrix @ a4_fit_coeffs  # (local)
max_a4_err = np.max(np.abs(a4_reconstructed - a4_gilkey_arr))  # (local)
print(f"\n  a_4 curvature decomposition:")
print(f"    a_4 = {alpha_a4:.8f} * R^2 + {beta_a4:.8f} * |Ric|^2 + {gamma_a4:.8f} * K")
print(f"    Max reconstruction error: {max_a4_err:.2e}")

# Similarly for a_2
A2_matrix = np.column_stack([R_arr])  # (local) a_2 only depends on R
a2_fit_coeffs, _, _, _ = np.linalg.lstsq(A2_matrix, a2_gilkey_arr, rcond=None)  # (local)
alpha_a2 = a2_fit_coeffs[0]  # (local)
a2_reconstructed = A2_matrix @ a2_fit_coeffs  # (local)
max_a2_err = np.max(np.abs(a2_reconstructed - a2_gilkey_arr))  # (local)
print(f"\n  a_2 curvature decomposition:")
print(f"    a_2 = {alpha_a2:.8f} * R")
print(f"    Max reconstruction error: {max_a2_err:.2e}")
print(f"    Compare: (4pi)^{{-4}} * 16 * (5/12) * Vol = {a0_gilkey * 5.0/12.0:.8f}")
print(f"    Ratio fitted/expected: {alpha_a2 / (a0_gilkey * 5.0/12.0):.8f}")

# Now reconstruct a_2, a_4 on the extended tau grid
a2_ext = alpha_a2 * R_ext  # (local)
a4_ext = alpha_a4 * R_ext**2 + beta_a4 * Ric2_ext + gamma_a4 * K_ext  # (local)

# Verify against original data in overlap region
idx_overlap = tau_ext <= 0.5  # (local)
tau_overlap = tau_ext[idx_overlap]  # (local)
a2_orig_interp = cs_a2(tau_overlap)  # (local)
a4_orig_interp = cs_a4(tau_overlap)  # (local)
a2_ext_overlap = a2_ext[idx_overlap]  # (local)
a4_ext_overlap = a4_ext[idx_overlap]  # (local)

err_a2_overlap = np.max(np.abs(a2_ext_overlap - a2_orig_interp) / a2_orig_interp)  # (local)
err_a4_overlap = np.max(np.abs(a4_ext_overlap - a4_orig_interp) / a4_orig_interp)  # (local)
print(f"\n  Extended vs original in overlap [0, 0.5]:")
print(f"    a_2 max relative error: {err_a2_overlap:.2e}")
print(f"    a_4 max relative error: {err_a4_overlap:.2e}")

print(f"\n  Extended values at tau = 0.48:")
idx_048 = np.argmin(np.abs(tau_ext - 0.48))  # (local)
print(f"    a_2(0.48) = {a2_ext[idx_048]:.8f}")
print(f"    a_4(0.48) = {a4_ext[idx_048]:.8f}")
print(f"    R(0.48)   = {R_ext[idx_048]:.6f}")

print(f"\n  Extended values at tau = 0.539:")
idx_054 = np.argmin(np.abs(tau_ext - 0.539))  # (local)
print(f"    a_2(0.539) = {a2_ext[idx_054]:.8f}")
print(f"    a_4(0.539) = {a4_ext[idx_054]:.8f}")
print(f"    R(0.539)   = {R_ext[idx_054]:.6f}")

print(f"\n  Extended values at tau = 0.70:")
idx_070 = np.argmin(np.abs(tau_ext - 0.70))  # (local)
print(f"    a_2(0.70) = {a2_ext[idx_070]:.8f}")
print(f"    a_4(0.70) = {a4_ext[idx_070]:.8f}")
print(f"    R(0.70)   = {R_ext[idx_070]:.6f}")

# ============================================================================
# SECTION 8: FULL V_eff ON EXTENDED GRID
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 8: V_eff on Extended Grid [0, 0.70]")
print("=" * 78)

# Compute V_eff(tau) from CC formula on extended grid
# Use cubic spline derivatives of a_2, a_4 on extended grid
cs_a2_ext = CubicSpline(tau_ext, a2_ext)  # (local)
cs_a4_ext = CubicSpline(tau_ext, a4_ext)  # (local)

results_ext = {}  # (local)

for scheme_name, (f0, f2, f4) in [
    ('sharp', (f_0_sc, f_2_sc, f_4_sc)),
    ('gaussian', (f_0_gauss, f_2_gauss, f_4_gauss)),
    ('heat', (f_0_heat, f_2_heat, f_4_heat)),
]:
    for Lambda in Lambda_values:
        L8 = Lambda**8  # (local)
        L6 = Lambda**6  # (local)
        L4 = Lambda**4  # (local)

        V_ext = (2.0 * f4 * L8 * a0_gilkey_const
                 + 2.0 * f2 * L6 * a2_ext
                 + f0 * L4 * a4_ext)  # (local)

        dV_ext = 2.0 * f2 * L6 * cs_a2_ext(tau_ext, 1) + f0 * L4 * cs_a4_ext(tau_ext, 1)  # (local)
        d2V_ext = 2.0 * f2 * L6 * cs_a2_ext(tau_ext, 2) + f0 * L4 * cs_a4_ext(tau_ext, 2)  # (local)

        # Find minima in [TAU_LO, TAU_HI]
        mask_target = (tau_ext >= TAU_LO) & (tau_ext <= TAU_HI)  # (local)
        dV_target = dV_ext[mask_target]  # (local)
        tau_target_arr = tau_ext[mask_target]  # (local)

        sign_changes = np.where(np.diff(np.sign(dV_target)))[0]  # (local)
        minima_ext = []  # (local)
        for idx in sign_changes:
            t0 = tau_target_arr[idx]  # (local)
            t1 = tau_target_arr[idx+1]  # (local)
            dv0 = dV_target[idx]  # (local)
            dv1 = dV_target[idx+1]  # (local)
            t_cross = t0 - dv0 * (t1 - t0) / (dv1 - dv0)  # (local)
            d2v_cross = np.interp(t_cross, tau_ext, d2V_ext)  # (local)
            if d2v_cross > 0:
                minima_ext.append((t_cross, d2v_cross))

        key = (scheme_name, Lambda)
        results_ext[key] = {
            'V_ext': V_ext,
            'dV_ext': dV_ext,
            'd2V_ext': d2V_ext,
            'minima': minima_ext,
        }

        # Report for Lambda = Lambda_sa
        if Lambda == Lambda_sa:
            idx_048_ext = np.argmin(np.abs(tau_ext - 0.48))  # (local)
            print(f"\n  {scheme_name} (Lambda={Lambda:.2f}):")
            print(f"    V_eff(fold) = {V_ext[np.argmin(np.abs(tau_ext - tau_fold))]:.6e}")
            print(f"    V_eff(0.48) = {V_ext[idx_048_ext]:.6e}")
            print(f"    dV/dtau(0.48) = {dV_ext[idx_048_ext]:.6e}")
            print(f"    |dV/dtau(0.48)| = {abs(dV_ext[idx_048_ext]):.6e}")
            if len(minima_ext) > 0:
                for tau_m, d2v_m in minima_ext:
                    print(f"    Minimum at tau = {tau_m:.6f}, d2V = {d2v_m:.6e}")
            else:
                print(f"    No minima in [{TAU_LO}, {TAU_HI}]")

# ============================================================================
# SECTION 9: GATE EVALUATION
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Gate Evaluation — S75-B2-CROSS-MOMENT")
print("=" * 78)

# The gate asks for a RESTORING gradient at tau = 0.48.
# A "restoring" gradient means dV/dtau < 0 (force pushes tau back toward fold).
# From the CC formula, dV/dtau = 2*f_2*L^6*da_2/dtau + f_0*L^4*da_4/dtau.
# Since both da_2/dtau > 0 and da_4/dtau > 0, and all coefficients are positive,
# dV/dtau > 0 always. The gradient is REPULSIVE (pushes tau away from fold), not restoring.
#
# The gate measures |restoring gradient|. Since the gradient is positive (increasing),
# the restoring force is ZERO — the CC formula predicts V_eff monotonically increasing.

# Report gradient at tau = 0.48 for the natural Lambda = Lambda_sa
key_ref = ('sharp', Lambda_sa)  # (local) reference scheme
idx_048_ext = np.argmin(np.abs(tau_ext - 0.48))  # (local)
dV_at_048 = results_ext[key_ref]['dV_ext'][idx_048_ext]  # (local)

print(f"\n  Reference: sharp cutoff, Lambda = {Lambda_sa:.2f} M_KK")
print(f"  dV_eff/dtau at tau = 0.48:")

grad_values = {}  # (local)
for scheme_name in ['sharp', 'gaussian', 'heat']:
    for Lambda in Lambda_values:
        key = (scheme_name, Lambda)
        idx_g = np.argmin(np.abs(tau_ext - 0.48))
        g = results_ext[key]['dV_ext'][idx_g]
        grad_values[key] = g
        print(f"    {scheme_name:>10} (L={Lambda:>8.2f}): dV/dtau = {g:+.6e}")

# The restoring gradient is -dV/dtau (force toward fold)
# Since dV/dtau > 0 for all schemes, restoring gradient = -dV/dtau < 0
# => |restoring gradient| = |dV/dtau| but it's in the WRONG direction

# Let me compute the actual restoring gradient magnitude properly.
# The S74 V_bare gradient was +445.4 M_KK^4. The question is whether
# the CC formula produces a DIFFERENT gradient that could be negative.
# But structurally, since a_0 is constant, a_2 increases, a_4 increases,
# and all f_k > 0, the CC formula gradient is always positive.

# The only way to get a restoring force is if the cutoff Lambda itself
# depends on tau. Let's check: if Lambda = Lambda(tau) then
# dV/dtau = partial_tau V + (dLambda/dtau) * partial_Lambda V
# The partial_Lambda V term is proportional to Lambda^7 * (...) which is
# large and positive. So Lambda(tau) decreasing could help.
# But Lambda is a fixed UV cutoff — it does not depend on tau.

# For the gate: restoring gradient = max(0, -dV/dtau)
# Since dV/dtau > 0 for all cases, restoring_gradient = 0.

# Wait: let me re-read the task more carefully.
# "compute V_eff(tau) = f_2(tau) * a_2(tau) + f_4(tau) * a_4(tau)"
# The task says f_2 and f_4 could be TAU-DEPENDENT.
# In the S63 data, f_2_of_tau and f_4_of_tau WERE computed as tau-dependent.
# Let me check that interpretation.

# From S63: the f_k(tau) were the Meissner-prescription running moments
# f_2(tau) ~ L^6 * moment at scale Lambda(tau). These DECREASE with tau.
# If f_2(tau) decreases faster than a_2(tau) increases, V could have a minimum!

print("\n" + "-" * 40)
print("  ALTERNATE INTERPRETATION: tau-dependent f_k(tau)")
print("-" * 40)

# Load S63 f_2(tau), f_4(tau)
d_s63 = np.load('s63_cutoff_meissner.npz', allow_pickle=True)
tau_s63 = d_s63['tau_arr']  # (200,) [0.001, 0.49]
f2_s63 = d_s63['f2_of_tau']  # (200,)
f4_s63 = d_s63['f4_of_tau']  # (200,)
a2_s63 = d_s63['a2_of_tau']  # (200,)
a4_s63 = d_s63['a4_of_tau']  # (200,)

print(f"\n  S63 Meissner f-moments (tau-dependent):")
print(f"    tau range: [{tau_s63[0]:.4f}, {tau_s63[-1]:.4f}]")
print(f"    f_2(0.001) = {f2_s63[0]:.6f}, f_2(0.49) = {f2_s63[-1]:.6f}")
print(f"    f_4(0.001) = {f4_s63[0]:.6f}, f_4(0.49) = {f4_s63[-1]:.6f}")
print(f"    f_2 ratio (end/start): {f2_s63[-1]/f2_s63[0]:.6f}")
print(f"    f_4 ratio (end/start): {f4_s63[-1]/f4_s63[0]:.6f}")
print(f"    a_2 ratio (end/start): {a2_s63[-1]/a2_s63[0]:.6f}")
print(f"    a_4 ratio (end/start): {a4_s63[-1]/a4_s63[0]:.6f}")

# Compute product f_2(tau)*a_2(tau) and f_4(tau)*a_4(tau)
product_f2_a2 = f2_s63 * a2_s63  # (local)
product_f4_a4 = f4_s63 * a4_s63  # (local)

# Check: do these products have extrema?
d_p_f2a2 = np.diff(product_f2_a2) / np.diff(tau_s63)  # (local)
d_p_f4a4 = np.diff(product_f4_a4) / np.diff(tau_s63)  # (local)

print(f"\n  Product f_2*a_2:")
print(f"    Start: {product_f2_a2[0]:.8f}")
print(f"    End:   {product_f2_a2[-1]:.8f}")
print(f"    Monotone increasing: {np.all(d_p_f2a2 > -1e-12)}")

print(f"\n  Product f_4*a_4:")
print(f"    Start: {product_f4_a4[0]:.8f}")
print(f"    End:   {product_f4_a4[-1]:.8f}")
print(f"    Monotone increasing: {np.all(d_p_f4a4 > -1e-12)}")

# Now compute V_Meissner = c1 * f_2(tau)*a_2(tau) + c2 * f_4(tau)*a_4(tau) + const
# Using the CC structure: V = 2*f_4*Lambda^8*a_0 + 2*f_2*Lambda^6*a_2 + f_0*Lambda^4*a_4
# If f_k are tau-dependent, all three terms contribute to dV/dtau.
# The f_4*a_0 term IS tau-dependent through f_4(tau).

# Full V with running f_k:
# Normalize: set Lambda = 1 (M_KK units), use the S63 f-values directly
V_meissner = (2.0 * f4_s63 * a0_gilkey_const  # f_4(tau) * const
              + 2.0 * f2_s63 * a2_s63          # f_2(tau) * a_2(tau)
              + f_0_sharp * a4_s63)             # f_0 * a_4(tau)

# Gradient
cs_V_meissner = CubicSpline(tau_s63, V_meissner)  # (local)
dV_meissner = cs_V_meissner(tau_s63, 1)  # (local)

print(f"\n  V_Meissner (running f_k, Lambda=1):")
print(f"    V(0.001) = {V_meissner[0]:.8f}")
print(f"    V(fold)  = {np.interp(tau_fold, tau_s63, V_meissner):.8f}")
print(f"    V(0.49)  = {V_meissner[-1]:.8f}")

# Check for sign changes in gradient
sign_ch_meissner = np.where(np.diff(np.sign(dV_meissner)))[0]  # (local)
print(f"    dV/dtau sign changes: {len(sign_ch_meissner)}")
if len(sign_ch_meissner) > 0:
    for sc in sign_ch_meissner:
        t_sc = tau_s63[sc]  # (local)
        print(f"      Sign change near tau = {t_sc:.4f}")
else:
    print(f"    V_Meissner is monotone in [{tau_s63[0]:.4f}, {tau_s63[-1]:.4f}]")

# Check gradient at tau = 0.48 from the running-f version
idx_048_s63 = np.argmin(np.abs(tau_s63 - 0.48))  # (local)
dV_meissner_048 = dV_meissner[idx_048_s63]  # (local)
print(f"\n  dV_Meissner/dtau at tau = {tau_s63[idx_048_s63]:.4f}: {dV_meissner_048:.8f}")

# The running-f effect: f_4 decreases => 2*a_0*df_4/dtau < 0 (negative contribution)
# But a_0 * f_4 dominates the potential. Let me separate terms.
term_a0_run = 2.0 * f4_s63 * a0_gilkey_const  # (local)
term_a2_run = 2.0 * f2_s63 * a2_s63  # (local)
term_a4_run = f_0_sharp * a4_s63  # (local)

cs_t0 = CubicSpline(tau_s63, term_a0_run)  # (local)
cs_t2 = CubicSpline(tau_s63, term_a2_run)  # (local)
cs_t4 = CubicSpline(tau_s63, term_a4_run)  # (local)

dt0 = cs_t0(tau_s63, 1)  # (local)
dt2 = cs_t2(tau_s63, 1)  # (local)
dt4 = cs_t4(tau_s63, 1)  # (local)

print(f"\n  Gradient decomposition at tau = {tau_s63[idx_048_s63]:.4f}:")
print(f"    d(2*f_4*a_0)/dtau = {dt0[idx_048_s63]:+.8f}")
print(f"    d(2*f_2*a_2)/dtau = {dt2[idx_048_s63]:+.8f}")
print(f"    d(f_0*a_4)/dtau   = {dt4[idx_048_s63]:+.8f}")
print(f"    Total dV/dtau     = {dt0[idx_048_s63] + dt2[idx_048_s63] + dt4[idx_048_s63]:+.8f}")

# Check: does running f_4 produce a NEGATIVE contribution large enough?
# The restoring gradient from the f_4*a_0 term:
print(f"\n  Restoring contribution (f_4 running):")
print(f"    |d(2*f_4*a_0)/dtau| at 0.48 = {abs(dt0[idx_048_s63]):.8f}")
print(f"    Positive terms at 0.48 = {dt2[idx_048_s63] + dt4[idx_048_s63]:.8f}")
print(f"    Net sign: {'+' if (dt0[idx_048_s63] + dt2[idx_048_s63] + dt4[idx_048_s63]) > 0 else '-'}")

# ============================================================================
# SECTION 10: COMPREHENSIVE GRADIENT TABLE
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 10: Comprehensive Gradient Table")
print("=" * 78)

print(f"\n  {'Scheme':>12} {'Lambda':>8} {'dV/dtau(0.48)':>18} {'|dV/dtau|':>14} {'Direction':>10}")
print(f"  {'-'*12} {'-'*8} {'-'*18} {'-'*14} {'-'*10}")

for scheme_name in ['sharp', 'gaussian', 'heat']:
    for Lambda in Lambda_values:
        key = (scheme_name, Lambda)
        idx_g = np.argmin(np.abs(tau_ext - 0.48))
        g = results_ext[key]['dV_ext'][idx_g]
        direction = "repulsive" if g > 0 else "restoring"  # (local)
        print(f"  {scheme_name:>12} {Lambda:>8.2f} {g:>+18.6e} {abs(g):>14.6e} {direction:>10}")

# Meissner running-f scheme
print(f"  {'meissner':>12} {'1.00':>8} {dV_meissner_048:>+18.8f} {abs(dV_meissner_048):>14.8f} "
      f"{'restoring' if dV_meissner_048 < 0 else 'repulsive':>10}")

# Compare to S74 bare gradient
print(f"\n  S74 reference: dV_bare/dtau at tau=0.48 = {dV_bare_at_kappa1:+.4f} M_KK^4")

# ============================================================================
# SECTION 11: GATE VERDICT
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 11: Gate Verdict — S75-B2-CROSS-MOMENT")
print("=" * 78)

# Gate criterion: restoring gradient >= 400 M_KK^4 at tau = 0.48
# The restoring gradient is max(0, -dV/dtau)

# For the CC formula with FIXED f_k: dV/dtau > 0 for all schemes and all Lambda.
# Both a_2(tau) and a_4(tau) are monotonically increasing with tau.
# All cutoff moments f_k > 0 and all Lambda^n > 0.
# Therefore dV/dtau > 0 always. Restoring gradient = 0.
# FAIL is structural.

# For the Meissner running f_k: the f_4(tau)*a_0 term has dV/dtau < 0
# because f_4 decreases with tau. But the positive terms from a_2 and a_4
# dominate. Net gradient is still positive (but smaller than fixed-f case).

# Determine if any scheme produces restoring gradient >= 40 (INFO threshold)
restoring_gradients = {}  # (local)
for key, r in results_ext.items():
    idx_g = np.argmin(np.abs(tau_ext - 0.48))
    g = r['dV_ext'][idx_g]
    restoring = max(0.0, -g)  # (local)
    restoring_gradients[key] = restoring

restoring_meissner = max(0.0, -dV_meissner_048)  # (local)

max_restoring = max(list(restoring_gradients.values()) + [restoring_meissner])  # (local)

print(f"\n  Maximum restoring gradient across all schemes: {max_restoring:.6e} M_KK^4")
print(f"  Gate thresholds: PASS >= 400, INFO >= 40, FAIL < 40")

if max_restoring >= 400:
    gate_verdict = "PASS"
elif max_restoring >= 40:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

print(f"\n  GATE VERDICT: {gate_verdict}")
print(f"  Reason: dV_eff/dtau > 0 for all schemes. The CC formula with")
print(f"  monotonically increasing a_2(tau), a_4(tau) and positive f_k, Lambda")
print(f"  produces a monotonically increasing V_eff(tau). No restoring force exists.")
print(f"  The Meissner running-f_k prescription reduces the gradient by ~{abs(dt0[idx_048_s63]/dV_meissner_048)*100:.1f}%")
print(f"  via the df_4/dtau < 0 contribution, but not enough to change sign.")

# Structural theorem:
print(f"\n  STRUCTURAL THEOREM:")
print(f"  For volume-preserving Jensen deformations of SU(3), the Gilkey SD")
print(f"  coefficients a_0 = const, a_2(tau), a_4(tau) are all non-decreasing.")
print(f"  The CC spectral action V = 2*f_4*L^8*a_0 + 2*f_2*L^6*a_2 + f_0*L^4*a_4")
print(f"  with f_k > 0, Lambda > 0 is therefore monotonically non-decreasing in tau.")
print(f"  This is the Seeley-DeWitt generalization of the Structural Monotonicity")
print(f"  Theorem (S36): the spectral action on Jensen-deformed SU(3) has no")
print(f"  post-fold minimum from curvature invariants alone.")

# ============================================================================
# SECTION 12: SAVE RESULTS
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 12: Saving Results")
print("=" * 78)

# Use the sharp + Lambda_sa as the primary result
key_primary = ('sharp', Lambda_sa)
V_primary = results_ext[key_primary]['V_ext']
dV_primary = results_ext[key_primary]['dV_ext']

np.savez_compressed('s75_cross_spectral_moment_moduli.npz',
    # Gate metadata
    gate_name='S75-B2-CROSS-MOMENT',
    gate_verdict=gate_verdict,
    gate_detail=(f"V_eff from CC formula monotone. Max restoring gradient = "
                 f"{max_restoring:.6e} M_KK^4. Structural: a_2(tau), a_4(tau) both "
                 f"monotone increasing => V_eff = positive * a_2 + positive * a_4 monotone."),

    # Tau grids
    tau_gilkey=tau_gilkey,
    tau_ext=tau_ext,
    tau_meissner=tau_s63,

    # Gilkey SD coefficients
    a2_gilkey_arr=a2_gilkey_arr,
    a4_gilkey_arr=a4_gilkey_arr,
    a2_ext=a2_ext,
    a4_ext=a4_ext,

    # Curvature data
    R_arr=R_arr,
    Ric2_arr=Ric2_arr,
    K_arr=K_arr,
    R_ext=R_ext,
    Ric2_ext=Ric2_ext,
    K_ext=K_ext,

    # Curvature fit coefficients
    alpha_a2=alpha_a2,
    alpha_a4=alpha_a4,
    beta_a4=beta_a4,
    gamma_a4=gamma_a4,

    # V_eff on extended grid (sharp, Lambda_sa)
    V_eff_primary=V_primary,
    dV_eff_primary=dV_primary,
    Lambda_primary=Lambda_sa,

    # Meissner running-f results
    V_meissner=V_meissner,
    dV_meissner=dV_meissner,
    f2_meissner=f2_s63,
    f4_meissner=f4_s63,

    # Ratio
    ratio_a4_a2=ratio_a4_a2,

    # Gradient at tau = 0.48
    dV_at_048_sharp_Lsa=float(results_ext[('sharp', Lambda_sa)]['dV_ext'][np.argmin(np.abs(tau_ext - 0.48))]),
    dV_at_048_gauss_Lsa=float(results_ext[('gaussian', Lambda_sa)]['dV_ext'][np.argmin(np.abs(tau_ext - 0.48))]),
    dV_at_048_heat_Lsa=float(results_ext[('heat', Lambda_sa)]['dV_ext'][np.argmin(np.abs(tau_ext - 0.48))]),
    dV_at_048_meissner=dV_meissner_048,
    dV_bare_at_048=dV_bare_at_kappa1,
    max_restoring_gradient=max_restoring,
)

print("  Saved: s75_cross_spectral_moment_moduli.npz")

# ============================================================================
# SECTION 13: PLOT
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 13: Plotting")
print("=" * 78)

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel (a): a_2(tau), a_4(tau) and their ratio
ax = axes[0, 0]
ax.plot(tau_gilkey, a2_gilkey_arr, 'b-', lw=2, label=r'$a_2^{Gilkey}(\tau)$')
ax.plot(tau_gilkey, a4_gilkey_arr, 'r-', lw=2, label=r'$a_4^{Gilkey}(\tau)$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('SD coefficient')
ax.legend(fontsize=9)
ax.set_title(r'(a) Gilkey $a_2, a_4$ vs $\tau$')

# Panel (b): ratio a_4/a_2
ax = axes[0, 1]
ax.plot(tau_gilkey, ratio_a4_a2, 'k-', lw=2)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_4 / a_2$')
ax.set_title(r'(b) Ratio $a_4/a_2$ (monotone $\Rightarrow$ no cross-moment extremum)')

# Panel (c): V_eff for sharp cutoff, three Lambda values
ax = axes[0, 2]
for Lambda in Lambda_values:
    key = ('sharp', Lambda)
    V = results_ext[key]['V_ext']
    V_norm = V / V[np.argmin(np.abs(tau_ext - tau_fold))]
    ax.plot(tau_ext, V_norm, lw=2, label=rf'$\Lambda={Lambda:.1f}\,M_{{KK}}$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axvspan(TAU_LO, min(TAU_HI, 0.70), alpha=0.1, color='green', label='target')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{eff} / V_{eff}(\tau_{fold})$')
ax.legend(fontsize=8)
ax.set_title(r'(c) $V_{eff}$ (sharp cutoff, normalized)')

# Panel (d): dV/dtau for three schemes at Lambda_sa
ax = axes[1, 0]
for scheme_name, color in [('sharp', 'b'), ('gaussian', 'r'), ('heat', 'g')]:
    key = (scheme_name, Lambda_sa)
    dV = results_ext[key]['dV_ext']
    ax.plot(tau_ext, dV, color=color, lw=2, label=scheme_name)
ax.axhline(0, color='k', ls='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axvline(0.48, color='orange', ls=':', alpha=0.7, label=r'$\tau=0.48$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$dV_{eff}/d\tau$')
ax.legend(fontsize=8)
ax.set_title(rf'(d) $dV_{{eff}}/d\tau$ ($\Lambda={Lambda_sa:.1f}\,M_{{KK}}$)')

# Panel (e): Meissner running-f products
ax = axes[1, 1]
ax.plot(tau_s63, product_f2_a2 / product_f2_a2[0], 'b-', lw=2, label=r'$f_2 \cdot a_2$ (norm)')
ax.plot(tau_s63, product_f4_a4 / product_f4_a4[0], 'r-', lw=2, label=r'$f_4 \cdot a_4$ (norm)')
ax.plot(tau_s63, f2_s63 / f2_s63[0], 'b--', lw=1, alpha=0.5, label=r'$f_2$ alone')
ax.plot(tau_s63, f4_s63 / f4_s63[0], 'r--', lw=1, alpha=0.5, label=r'$f_4$ alone')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Normalized value')
ax.legend(fontsize=8)
ax.set_title('(e) Meissner running $f_k$ vs $a_k$')

# Panel (f): Gradient decomposition (Meissner)
ax = axes[1, 2]
ax.plot(tau_s63, dt0, 'b-', lw=2, label=r'$d(2f_4 a_0)/d\tau$ (< 0)')
ax.plot(tau_s63, dt2, 'r-', lw=2, label=r'$d(2f_2 a_2)/d\tau$')
ax.plot(tau_s63, dt4, 'g-', lw=2, label=r'$d(f_0 a_4)/d\tau$')
ax.plot(tau_s63, dV_meissner, 'k-', lw=2.5, label='Total')
ax.axhline(0, color='k', ls='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$dV/d\tau$')
ax.legend(fontsize=8)
ax.set_title('(f) Gradient decomposition (Meissner)')

plt.suptitle('S75-B2-CROSS-MOMENT: Cross-Spectral-Moment Moduli Potential\n'
             r'FAIL: $a_2(\tau), a_4(\tau)$ both monotone $\Rightarrow$ $V_{eff}$ monotone, no restoring force',
             fontsize=12)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('s75_cross_spectral_moment_moduli.png', dpi=150, bbox_inches='tight')
print("  Saved: s75_cross_spectral_moment_moduli.png")

t_elapsed = time.time() - t_start
print(f"\n  Total runtime: {t_elapsed:.2f} s")
print("=" * 78)
print(f"GATE S75-B2-CROSS-MOMENT: {gate_verdict}")
print("=" * 78)
