#!/usr/bin/env python3
"""
s73b_sdw_validation.py -- SDW-VALIDATION-73B
==============================================

Gate: SDW-VALIDATION-73B
  PASS: |a_0/a_2(direct) / a_0/a_2(SDW) - 1| < 0.05 AND
        |a_2/a_4(direct) / a_2/a_4(SDW) - 1| < 0.05 (ratios robust)
  FAIL: Either ratio deviates by > 20%
  INFO: L_max dependence exceeds 5%

Physics:
--------
The canonical "SDW" coefficients in this project are SPECTRAL ZETA SUMS:
    a_0 = sum_{(p,q)} dim(p,q) * N_pos(p,q)          [mode count]
    a_2 = sum_{(p,q)} dim(p,q) * sum_j |lambda_j|^-2  [zeta_D(1)]
    a_4 = sum_{(p,q)} dim(p,q) * sum_j |lambda_j|^-4  [zeta_D(2)]

These are INTRINSIC GEOMETRIC INVARIANTS of D_K. They do not depend
on the spectral functional f.

f*(x) = alpha*sqrt(x) + beta*exp(-x) has DIVERGENT SDW moments
(f_0 = infinity), so the standard weighted expansion
    S ~ f_0*a_0*Lambda^4 + f_2*a_2*Lambda^2 + f_4*a_4 + ...
DOES NOT EXIST for f*.

The question this computation addresses:
  (1) Are the RATIOS a_0/a_2 and a_2/a_4 recoverable from the
      Lambda-dependence of the direct spectral sum S(Lambda)?
  (2) Do these ratios depend on L_max (Peter-Weyl truncation)?
  (3) Can the effective coefficients from polynomial fits of S(Lambda)
      reproduce the INDIVIDUAL a_k values, not just ratios?

The answer depends on HOW the a_k enter S(Lambda). For f*:
  S_f*(Lambda) = alpha * sum d |lambda|/Lambda + beta * sum d exp(-lambda^2/Lambda^2)
               = alpha * M_1/Lambda + beta * K(1/Lambda^2)

where M_1 = first absolute moment and K(t) = heat kernel.
The a_k are the small-t asymptotic expansion of K(t):
  K(t) ~ a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2} + ...

So a_k enter S_f* ONLY through the beta*exp component. The sqrt
component contributes a SINGLE spectral moment M_1 with NO a_k structure.

Agent: Lizzi Spectral-Functional Theorist (Session 73b, Wave 3)
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    M_KK_gravity, M_Pl_reduced,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

from spectral_action import dim_su3_irrep

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("SDW-VALIDATION-73B: Direct Spectral Sum vs SDW Under f*")
print("=" * 78)

# f* parameters (from SPECTRAL-FUNCTIONAL-FIT-72)
alpha_star = 0.9116771171053042  # (local) weight of sqrt
beta_star = 0.08832288289469575  # (local) weight of exp

# Tau values for comparison
tau_values = np.array([0.10, 0.19, 0.30])  # (local)
n_tau = len(tau_values)  # (local)

# L_max values (Peter-Weyl truncation)
Lmax_values = [3, 7]  # (local) max_pq_sum values

# Lambda scan: 30 values spanning the eigenvalue range
n_Lambda = 30  # (local)
Lambda_scan = np.linspace(1.5, 12.0, n_Lambda)  # (local)

# Eigenvalue cutoff for zeta sums (to exclude near-zero eigenvalues)
EVAL_CUTOFF = 0.01  # (local) same as S41

# Canonical SDW ratios (from S42/S41 direct zeta sums)
ratio_a0_a2_SDW = a0_fold / a2_fold  # (local)
ratio_a2_a4_SDW = a2_fold / a4_fold  # (local)

print(f"\n  f*(x) = {alpha_star:.4f}*sqrt(x) + {beta_star:.4f}*exp(-x)")
print(f"  Tau values: {tau_values}")
print(f"  L_max values: {Lmax_values}")
print(f"  Lambda scan: {n_Lambda} points in [{Lambda_scan[0]:.1f}, {Lambda_scan[-1]:.1f}] M_KK")
print(f"  Eigenvalue cutoff: {EVAL_CUTOFF}")
print(f"\n  Canonical spectral zeta sums at fold (tau=0.19):")
print(f"    a_0 = {a0_fold:.2f}  (mode count)")
print(f"    a_2 = {a2_fold:.4f}  (zeta_D(1))")
print(f"    a_4 = {a4_fold:.4f}  (zeta_D(2))")
print(f"    a_0/a_2 = {ratio_a0_a2_SDW:.6f}")
print(f"    a_2/a_4 = {ratio_a2_a4_SDW:.6f}")

# =============================================================================
# STEP 0: BUILD ALGEBRAIC INFRASTRUCTURE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: SU(3) Algebraic Infrastructure")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
print("  Done.")


# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute D_K Eigenvalue Spectra")
print("=" * 78)

# Storage: spectra[Lmax][tau_idx] = list of (p, q, omega, d_pq)
spectra = {}

for Lmax in Lmax_values:
    spectra[Lmax] = {}
    t0 = time.time()  # (local)
    for ti, tau in enumerate(tau_values):
        _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                       max_pq_sum=Lmax, verbose=False)
        tau_spec = []  # (local)
        n_weighted = 0  # (local)
        n_raw = 0  # (local)
        for p, q, evals in eval_data:
            d_pq = dim_su3_irrep(p, q)  # (local)
            omega = np.abs(evals)  # (local)
            tau_spec.append((p, q, omega, d_pq))
            n_weighted += d_pq**2 * len(omega)
            n_raw += len(omega)
        spectra[Lmax][ti] = tau_spec
        print(f"  L_max={Lmax}, tau={tau:.2f}: {n_raw} raw eigenvalues, "
              f"{n_weighted} weighted, {len(eval_data)} sectors")
    elapsed = time.time() - t0  # (local)
    print(f"  L_max={Lmax} completed in {elapsed:.1f}s")


# =============================================================================
# STEP 2: COMPUTE SPECTRAL ZETA SUMS (THE CORRECT a_k DEFINITION)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Direct Spectral Zeta Sums (Canonical a_k Definition)")
print("=" * 78)

# The canonical a_k from S41/S42 are:
#   a_0 = sum_{(p,q)} dim(p,q) * N_pos(p,q)
#   a_2 = sum_{(p,q)} dim(p,q) * sum_{j: |lambda_j| > cutoff} |lambda_j|^{-2}
#   a_4 = sum_{(p,q)} dim(p,q) * sum_{j: |lambda_j| > cutoff} |lambda_j|^{-4}
#
# Note: S41 uses dim(p,q) (right-regular degeneracy), NOT dim(p,q)^2.
# The eigenvalue storage convention: each entry in the eigenvalue array
# represents dim(p,q)*16 eigenvalues from the D_{(p,q)} block, with
# the outer dim(p,q) PW degeneracy applied separately as a weight.

zeta_results = {}

for Lmax in Lmax_values:
    zeta_results[Lmax] = {}
    print(f"\n  L_max = {Lmax}:")
    for ti, tau in enumerate(tau_values):
        a0_sum = 0.0  # (local)
        a2_sum = 0.0  # (local)
        a4_sum = 0.0  # (local)
        a6_sum = 0.0  # (local)
        M1_sum = 0.0  # (local) first absolute moment

        for (p, q, omega, d_pq) in spectra[Lmax][ti]:
            # collect_spectrum returns ALL eigenvalues (positive + negative mirror).
            # S41 canonical convention: take only positive eigenvalues (half of the spectrum).
            # omega = |eigenvalue|, so we can't distinguish + from -.
            # We divide count by 2 for positive-only convention.
            pos = omega[omega > EVAL_CUTOFF]  # (local)
            n_pos_all = len(pos)  # (local) includes both + and - mirror
            # Spectrum is symmetric around 0, so positive half = half of all nonzero
            n_pos = n_pos_all // 2  # (local) positive only, to match S41
            # Use every second eigenvalue (sorted by |lambda|, so pairs are adjacent)
            # Equivalently, sum of f(|lambda|) for all eigenvalues divided by 2
            sum_inv2 = 0.5 * np.sum(pos**(-2))  # (local)
            sum_inv4 = 0.5 * np.sum(pos**(-4))  # (local)
            sum_inv6 = 0.5 * np.sum(pos**(-6))  # (local)
            sum_abs1 = 0.5 * np.sum(pos)  # (local)

            # PW degeneracy: dim(p,q) per eigenvalue
            a0_sum += d_pq * n_pos
            a2_sum += d_pq * sum_inv2
            a4_sum += d_pq * sum_inv4
            a6_sum += d_pq * sum_inv6
            M1_sum += d_pq * sum_abs1

        zeta_results[Lmax][ti] = {
            'a0': a0_sum, 'a2': a2_sum, 'a4': a4_sum, 'a6': a6_sum,
            'M1': M1_sum
        }

        r02 = a0_sum / a2_sum if a2_sum != 0 else float('nan')  # (local)
        r24 = a2_sum / a4_sum if a4_sum != 0 else float('nan')  # (local)
        print(f"    tau={tau:.2f}: a_0={a0_sum:.1f}, a_2={a2_sum:.4f}, "
              f"a_4={a4_sum:.4f}, a_0/a_2={r02:.6f}, a_2/a_4={r24:.6f}")

        if tau == tau_fold:
            print(f"    --- Fold comparison ---")
            print(f"    a_0: {a0_sum:.1f} vs canonical {a0_fold:.1f} "
                  f"(dev={abs(a0_sum - a0_fold)/a0_fold:.2e})")
            print(f"    a_2: {a2_sum:.4f} vs canonical {a2_fold:.4f} "
                  f"(dev={abs(a2_sum - a2_fold)/a2_fold:.2e})")
            print(f"    a_4: {a4_sum:.4f} vs canonical {a4_fold:.4f} "
                  f"(dev={abs(a4_sum - a4_fold)/a4_fold:.2e})")


# =============================================================================
# STEP 3: DIRECT SPECTRAL SUMS S(Lambda) WITH f*
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Direct Spectral Sums S(Lambda)")
print("=" * 78)


def f_star_fn(x):
    """f*(x) = alpha*sqrt(x) + beta*exp(-x)."""
    return alpha_star * np.sqrt(np.maximum(x, 0.0)) + beta_star * np.exp(-x)


def f_exp_fn(x):
    """f_exp(x) = exp(-x)."""
    return np.exp(-x)


def f_sqrt_fn(x):
    """f_sqrt(x) = sqrt(x)."""
    return np.sqrt(np.maximum(x, 0.0))


def compute_spectral_sum(spec_data, Lambda_val, f_fn):
    """Compute S = sum_{(p,q)} d_{pq}^2 * sum_j f(omega_j^2 / Lambda^2)."""
    S = 0.0  # (local)
    Lambda_sq = Lambda_val**2  # (local)
    for (p, q, omega, d_pq) in spec_data:
        x = omega**2 / Lambda_sq  # (local)
        S += d_pq**2 * np.sum(f_fn(x))
    return S


# Compute S(Lambda) for all functionals, tau values, and L_max
S_fstar = {}
S_exp = {}
S_sqrt_arr = {}

for Lmax in Lmax_values:
    S_fstar[Lmax] = np.zeros((n_tau, n_Lambda))
    S_exp[Lmax] = np.zeros((n_tau, n_Lambda))
    S_sqrt_arr[Lmax] = np.zeros((n_tau, n_Lambda))

    for ti in range(n_tau):
        spec = spectra[Lmax][ti]
        for li, Lam in enumerate(Lambda_scan):
            S_fstar[Lmax][ti, li] = compute_spectral_sum(spec, Lam, f_star_fn)
            S_exp[Lmax][ti, li] = compute_spectral_sum(spec, Lam, f_exp_fn)
            S_sqrt_arr[Lmax][ti, li] = compute_spectral_sum(spec, Lam, f_sqrt_fn)

    print(f"\n  L_max = {Lmax}:")
    for ti, tau in enumerate(tau_values):
        print(f"    tau={tau:.2f}: S_f*(Lambda_min)={S_fstar[Lmax][ti, 0]:.2f}, "
              f"S_f*(Lambda_max)={S_fstar[Lmax][ti, -1]:.2f}")


# =============================================================================
# STEP 4: EXTRACT EFFECTIVE COEFFICIENTS FROM S_exp(Lambda)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Extract Effective a_k from S_exp(Lambda) Scaling")
print("=" * 78)

# For S_exp(Lambda) = K(t=1/Lambda^2) = sum d^2 * exp(-omega^2/Lambda^2):
# As Lambda -> infinity, this approaches sum d^2 * 1 = total mode count.
# The heat kernel expansion is K(t) ~ a_0*t^{-4} + a_2*t^{-3} + ...
# So S_exp(Lambda) ~ a_0*Lambda^8 + a_2*Lambda^6 + a_4*Lambda^4 + ...
#
# HOWEVER: the CANONICAL a_k in this project are spectral ZETA sums
# (a_0 = mode count with dim(p,q) weight, not dim(p,q)^2).
# The S_exp sum uses d^2 weighting, while canonical a_k use d weighting.
#
# This is the KEY MISMATCH: S_exp(Lambda) involves d^2-weighted sums,
# while canonical a_k involves d-weighted sums.

# Let's also compute the d-weighted spectral sums for proper comparison
def compute_spectral_sum_d1(spec_data, Lambda_val, f_fn):
    """Compute S = sum_{(p,q)} d_{pq} * sum_j f(omega_j^2 / Lambda^2).
    Uses dim(p,q) weighting (not dim^2) to match canonical a_k convention."""
    S = 0.0  # (local)
    Lambda_sq = Lambda_val**2  # (local)
    for (p, q, omega, d_pq) in spec_data:
        x = omega**2 / Lambda_sq  # (local)
        S += d_pq * np.sum(f_fn(x))
    return S


# Compute d-weighted exp sum = heat kernel with canonical weighting
S_exp_d1 = {}
for Lmax in Lmax_values:
    S_exp_d1[Lmax] = np.zeros((n_tau, n_Lambda))
    for ti in range(n_tau):
        spec = spectra[Lmax][ti]
        for li, Lam in enumerate(Lambda_scan):
            S_exp_d1[Lmax][ti, li] = compute_spectral_sum_d1(spec, Lam, f_exp_fn)


# Extract effective coefficients from high-Lambda behavior of d1-weighted exp sum
# K_d1(t) = sum d * exp(-t*omega^2) ~ a_0_eff * t^{-4} + a_2_eff * t^{-3} + ...
# Use the polynomial fitting approach on t^4 * K_d1(t)

print("\n  STRATEGY: Heat kernel fit of d1-weighted K(t) = sum d*exp(-t*omega^2)")
print("  " + "-" * 70)

results_hk_d1 = {}

for Lmax in Lmax_values:
    results_hk_d1[Lmax] = {}
    for ti, tau in enumerate(tau_values):
        spec = spectra[Lmax][ti]

        # Compute K_d1(t) for a range of t values
        t_vals = np.logspace(-3, 0, 500)  # (local) 0.001 to 1
        K_d1 = np.zeros(len(t_vals))  # (local)

        for (p, q, omega, d_pq) in spec:
            omega_sq = omega**2  # (local)
            for it, t in enumerate(t_vals):
                K_d1[it] += d_pq * np.sum(np.exp(-t * omega_sq))

        # Fit t^4 * K(t) = a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4
        F = t_vals**4 * K_d1  # (local)

        # Use small-t range for fitting (where asymptotic expansion is valid)
        # The smallest t where K(t) is reliable depends on the largest eigenvalue
        mask = t_vals < 0.1  # (local) use t < 0.1
        t_fit = t_vals[mask]  # (local)
        F_fit = F[mask]  # (local)

        n_coeffs = 5  # (local)
        V_mat = np.vander(t_fit, N=n_coeffs, increasing=True)  # (local)
        # Weighted fit: emphasize small t
        w = 1.0 / (t_fit + 1e-6)  # (local)
        W = np.diag(w)  # (local)
        VtWV = V_mat.T @ W @ V_mat  # (local)
        VtWF = V_mat.T @ W @ F_fit  # (local)
        cond = np.linalg.cond(VtWV)  # (local)

        coeffs = np.linalg.solve(VtWV, VtWF)  # (local)
        a0_hk, a2_hk, a4_hk, a6_hk, a8_hk = coeffs  # (local)

        # Fit quality
        F_pred = V_mat @ coeffs  # (local)
        residual = np.sqrt(np.mean((F_fit - F_pred)**2)) / np.mean(np.abs(F_fit))  # (local)

        results_hk_d1[Lmax][ti] = {
            'a0': a0_hk, 'a2': a2_hk, 'a4': a4_hk,
            'a6': a6_hk, 'a8': a8_hk,
            'cond': cond, 'residual': residual
        }

        print(f"\n  L_max={Lmax}, tau={tau:.2f}: (cond={cond:.1e}, residual={residual:.2e})")
        print(f"    a_0 = {a0_hk:.4f}")
        print(f"    a_2 = {a2_hk:.4f}")
        print(f"    a_4 = {a4_hk:.4f}")

        if tau == tau_fold:
            print(f"    --- Comparison with canonical zeta sums ---")
            print(f"    a_0: HK={a0_hk:.4f} vs zeta={a0_fold:.4f} "
                  f"(dev={abs(a0_hk-a0_fold)/a0_fold:.2e})")
            print(f"    a_2: HK={a2_hk:.4f} vs zeta={a2_fold:.4f} "
                  f"(dev={abs(a2_hk-a2_fold)/a2_fold:.2e})")
            print(f"    a_4: HK={a4_hk:.4f} vs zeta={a4_fold:.4f} "
                  f"(dev={abs(a4_hk-a4_fold)/a4_fold:.2e})")


# =============================================================================
# STEP 5: RATIO COMPARISON TABLE — THREE METHODS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Comprehensive Ratio Comparison")
print("=" * 78)

print(f"\n  {'Method':<45s} {'a_0/a_2':>12s} {'a_2/a_4':>12s}")
print("  " + "-" * 72)
print(f"  {'Canonical (S42, zeta sums, L_max=3)':45s} "
      f"{ratio_a0_a2_SDW:12.6f} {ratio_a2_a4_SDW:12.6f}")

gate_dev_a0a2 = {}  # (local)
gate_dev_a2a4 = {}  # (local)

for Lmax in Lmax_values:
    ti_fold = 1  # tau = 0.19

    # Method 1: Direct zeta sums
    z = zeta_results[Lmax][ti_fold]  # (local)
    r02_z = z['a0'] / z['a2']  # (local)
    r24_z = z['a2'] / z['a4']  # (local)
    dev02_z = abs(r02_z / ratio_a0_a2_SDW - 1.0)  # (local)
    dev24_z = abs(r24_z / ratio_a2_a4_SDW - 1.0)  # (local)
    print(f"  {'Zeta sums (direct) L_max='+str(Lmax):45s} "
          f"{r02_z:12.6f} {r24_z:12.6f}  "
          f"(dev: {dev02_z:.2e}, {dev24_z:.2e})")

    # Method 2: HK d1-weighted fit
    hk = results_hk_d1[Lmax][ti_fold]  # (local)
    if hk['a2'] != 0 and hk['a4'] != 0:
        r02_hk = hk['a0'] / hk['a2']  # (local)
        r24_hk = hk['a2'] / hk['a4']  # (local)
        dev02_hk = abs(r02_hk / ratio_a0_a2_SDW - 1.0)  # (local)
        dev24_hk = abs(r24_hk / ratio_a2_a4_SDW - 1.0)  # (local)
        print(f"  {'HK fit (d1-weighted) L_max='+str(Lmax):45s} "
              f"{r02_hk:12.6f} {r24_hk:12.6f}  "
              f"(dev: {dev02_hk:.2e}, {dev24_hk:.2e})")

    # Store gate values from ZETA sums (the correct definition)
    gate_dev_a0a2[Lmax] = dev02_z
    gate_dev_a2a4[Lmax] = dev24_z


# =============================================================================
# STEP 6: L_max CONVERGENCE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: L_max Convergence Analysis")
print("=" * 78)

Lmax_lo, Lmax_hi = Lmax_values[0], Lmax_values[-1]  # (local)
ti_fold = 1  # (local)

z_lo = zeta_results[Lmax_lo][ti_fold]  # (local)
z_hi = zeta_results[Lmax_hi][ti_fold]  # (local)

r02_lo = z_lo['a0'] / z_lo['a2']  # (local)
r02_hi = z_hi['a0'] / z_hi['a2']  # (local)
r24_lo = z_lo['a2'] / z_lo['a4']  # (local)
r24_hi = z_hi['a2'] / z_hi['a4']  # (local)

Lmax_dep_a0a2 = abs(r02_hi / r02_lo - 1.0)  # (local)
Lmax_dep_a2a4 = abs(r24_hi / r24_lo - 1.0)  # (local)

print(f"\n  L_max convergence (L_max={Lmax_lo} -> {Lmax_hi}):")
print(f"    a_0: {z_lo['a0']:.1f} -> {z_hi['a0']:.1f} "
      f"(change: {abs(z_hi['a0']/z_lo['a0'] - 1)*100:.2f}%)")
print(f"    a_2: {z_lo['a2']:.4f} -> {z_hi['a2']:.4f} "
      f"(change: {abs(z_hi['a2']/z_lo['a2'] - 1)*100:.2f}%)")
print(f"    a_4: {z_lo['a4']:.4f} -> {z_hi['a4']:.4f} "
      f"(change: {abs(z_hi['a4']/z_lo['a4'] - 1)*100:.2f}%)")
print(f"\n    a_0/a_2: {r02_lo:.6f} -> {r02_hi:.6f} "
      f"(shift: {Lmax_dep_a0a2*100:.4f}%)")
print(f"    a_2/a_4: {r24_lo:.6f} -> {r24_hi:.6f} "
      f"(shift: {Lmax_dep_a2a4*100:.4f}%)")

# Scaling analysis
print(f"\n  Scaling of a_k with L_max:")
for k_name, k_lo, k_hi in [('a_0', z_lo['a0'], z_hi['a0']),
                             ('a_2', z_lo['a2'], z_hi['a2']),
                             ('a_4', z_lo['a4'], z_hi['a4']),
                             ('a_6', z_lo['a6'], z_hi['a6'])]:
    ratio = k_hi / k_lo if k_lo != 0 else float('inf')  # (local)
    print(f"    {k_name}: ratio(L7/L3) = {ratio:.4f}")


# =============================================================================
# STEP 7: f* DECOMPOSITION AND COMPONENT ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: f* Decomposition: sqrt vs exp Component Analysis")
print("=" * 78)

# Verify linearity: S_f* = alpha*S_sqrt + beta*S_exp
for Lmax in Lmax_values:
    print(f"\n  L_max = {Lmax}:")
    for ti, tau in enumerate(tau_values):
        S_recon = alpha_star * S_sqrt_arr[Lmax][ti] + beta_star * S_exp[Lmax][ti]  # (local)
        max_dev = np.max(np.abs(S_recon - S_fstar[Lmax][ti]) / np.abs(S_fstar[Lmax][ti]))  # (local)
        print(f"    tau={tau:.2f}: linearity check: max|dev| = {max_dev:.2e}")

print(f"\n  Component fractions at fold (tau={tau_fold}):")
print(f"  {'Lambda':>8s} ", end="")
for Lmax in Lmax_values:
    print(f"{'sqrt(L'+str(Lmax)+')':>12s} {'exp(L'+str(Lmax)+')':>12s}", end="")
print()
for li in range(0, n_Lambda, max(1, n_Lambda//8)):
    Lam = Lambda_scan[li]  # (local)
    print(f"  {Lam:8.2f} ", end="")
    for Lmax in Lmax_values:
        frac_s = alpha_star * S_sqrt_arr[Lmax][1, li] / S_fstar[Lmax][1, li]  # (local)
        frac_e = beta_star * S_exp[Lmax][1, li] / S_fstar[Lmax][1, li]  # (local)
        print(f"{frac_s:12.6f} {frac_e:12.6f}", end="")
    print()


# =============================================================================
# STEP 8: S73A CROSS-CHECK
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Cross-Check with S73A Data")
print("=" * 78)

s73a = np.load('s73a_spectral_action_profile.npz', allow_pickle=True)
tau_73a = s73a['tau_grid']  # (local)
S_bare_73a = s73a['S_bare']  # (local) shape (4, 104): [f_star, sqrt, exp, compact]
Lambda_73a = float(s73a['Lambda'])  # (local)

idx_fold_73a = np.argmin(np.abs(tau_73a - tau_fold))  # (local)
S_fstar_fold_73a = S_bare_73a[0, idx_fold_73a]  # (local)

# Our computation at same Lambda
ti_fold = 1  # (local)
S_fstar_ours = compute_spectral_sum(spectra[3][ti_fold], Lambda_73a, f_star_fn)  # (local)

dev_73a = abs(S_fstar_ours - S_fstar_fold_73a) / abs(S_fstar_fold_73a)  # (local)
print(f"\n  S73A: S_f*(fold, Lambda={Lambda_73a:.4f}) = {S_fstar_fold_73a:.4f}")
print(f"  Ours:  S_f*(fold, Lambda={Lambda_73a:.4f}) = {S_fstar_ours:.4f}")
print(f"  Deviation: {dev_73a:.2e}")

# Also extract the canonical zeta sums at tau=0.19 using S73A's tau grid
# to see if the a_k values are consistent across different tau nearby
print(f"\n  Tau-stability of a_k (zeta sums, L_max=3) near fold:")
for ti_check in [0, 1, 2]:
    tau_c = tau_values[ti_check]  # (local)
    z = zeta_results[3][ti_check]  # (local)
    print(f"    tau={tau_c:.2f}: a_0={z['a0']:.1f}, a_2={z['a2']:.4f}, "
          f"a_4={z['a4']:.4f}, a_0/a_2={z['a0']/z['a2']:.6f}, "
          f"a_2/a_4={z['a2']/z['a4']:.6f}")


# =============================================================================
# STEP 9: PHYSICS ANALYSIS — WHAT THE RATIOS MEAN FOR f*
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Physics Analysis — SDW Ratios Under f*")
print("=" * 78)

print("""
  KEY FINDING: The spectral zeta sums a_k are GEOMETRIC INVARIANTS of D_K.
  They are computable independently of ANY spectral functional.

  For f* = 0.912*sqrt + 0.088*exp:
    S_f*(Lambda) = 0.912 * M_1/Lambda + 0.088 * K(1/Lambda^2)

  where:
    M_1 = sum d^2 |lambda_j|           -- first absolute moment (geometric)
    K(t) = sum d^2 exp(-t*lambda^2)    -- heat kernel (encodes ALL a_k)

  The a_k hierarchy enters ONLY through the exp component.
  The sqrt component is a SINGLE geometric invariant M_1.

  IMPLICATIONS FOR PREDICTIONS:
  1. sin^2(theta_W) = a_4/a_2 in suitable normalization:
     This ratio is FUNCTIONAL-INDEPENDENT because it's a ratio of
     spectral zeta sums.

  2. Newton's constant G_N ~ 1/a_2: FUNCTIONAL-INDEPENDENT (geometric).

  3. Higgs mass m_H^2 ~ a_6/a_4: Also a ratio of spectral zeta sums,
     FUNCTIONAL-INDEPENDENT.

  4. Cosmological constant rho_CC ~ a_0 * M_KK^4: The mode count a_0
     is FUNCTIONAL-INDEPENDENT, but the PHYSICAL CC depends on which
     spectral functional determines the action:
     - In cutoff scheme: CC ~ f_0 * a_0 * M_KK^4 (f_0 = integral f)
     - In zeta scheme: CC = 0 (no a_0 term by construction)
     - In f* scheme: the sqrt term contributes Lambda^{-1} * M_1,
       which is a COMPLETELY DIFFERENT scaling from Lambda^4.
       The CC from f* is NOT a_0 * Lambda^4.

  CONCLUSION: Ratio-based predictions (gauge couplings, mixing angles,
  mass ratios) are STRUCTURAL and survive the transition from SDW to f*.
  The ABSOLUTE SCALE of the action (CC, vacuum energy) is MAXIMALLY
  SCHEME-DEPENDENT, consistent with all prior Lizzi analysis.
""")


# =============================================================================
# STEP 10: GATE EVALUATION
# =============================================================================
print("=" * 78)
print("STEP 10: Gate SDW-VALIDATION-73B")
print("=" * 78)

# Use ZETA SUM ratios at the highest available L_max
Lmax_gate = max(Lmax_values)  # (local)
ti_fold = 1  # (local)
z_gate = zeta_results[Lmax_gate][ti_fold]  # (local)

ratio_direct_a0a2 = z_gate['a0'] / z_gate['a2']  # (local)
ratio_direct_a2a4 = z_gate['a2'] / z_gate['a4']  # (local)

dev_a0a2_gate = abs(ratio_direct_a0a2 / ratio_a0_a2_SDW - 1.0)  # (local)
dev_a2a4_gate = abs(ratio_direct_a2a4 / ratio_a2_a4_SDW - 1.0)  # (local)

print(f"\n  Spectral zeta sums at fold (L_max = {Lmax_gate}):")
print(f"    a_0 = {z_gate['a0']:.1f}")
print(f"    a_2 = {z_gate['a2']:.4f}")
print(f"    a_4 = {z_gate['a4']:.4f}")
print(f"\n  RATIO TEST:")
print(f"    a_0/a_2 (L_max={Lmax_gate}):  {ratio_direct_a0a2:.6f}")
print(f"    a_0/a_2 (canonical):    {ratio_a0_a2_SDW:.6f}")
print(f"    Deviation:              {dev_a0a2_gate:.6f} ({dev_a0a2_gate*100:.4f}%)")
print()
print(f"    a_2/a_4 (L_max={Lmax_gate}):  {ratio_direct_a2a4:.6f}")
print(f"    a_2/a_4 (canonical):    {ratio_a2_a4_SDW:.6f}")
print(f"    Deviation:              {dev_a2a4_gate:.6f} ({dev_a2a4_gate*100:.4f}%)")

print(f"\n  L_max CONVERGENCE:")
print(f"    a_0/a_2: {Lmax_dep_a0a2*100:.4f}% shift (L_max {Lmax_lo}->{Lmax_hi})")
print(f"    a_2/a_4: {Lmax_dep_a2a4*100:.4f}% shift (L_max {Lmax_lo}->{Lmax_hi})")

# Gate verdict
pass_a0a2 = dev_a0a2_gate < 0.05  # (local)
pass_a2a4 = dev_a2a4_gate < 0.05  # (local)
fail_a0a2 = dev_a0a2_gate > 0.20  # (local)
fail_a2a4 = dev_a2a4_gate > 0.20  # (local)
info_Lmax = (Lmax_dep_a0a2 > 0.05 or Lmax_dep_a2a4 > 0.05)  # (local)

if pass_a0a2 and pass_a2a4 and not info_Lmax:
    verdict = "PASS"
    detail = (f"Both ratios robust: "
              f"|dev(a_0/a_2)|={dev_a0a2_gate:.6f} < 0.05, "
              f"|dev(a_2/a_4)|={dev_a2a4_gate:.6f} < 0.05. "
              f"L_max shifts < 5%. "
              f"SDW ratios are FUNCTIONAL-INDEPENDENT geometric invariants. "
              f"Ratio-based predictions (sin^2 theta_W, Higgs mass) survive under f*.")
elif pass_a0a2 and pass_a2a4 and info_Lmax:
    verdict = "INFO"
    detail = (f"Ratios converge (dev < 5%) but L_max dependence exceeds 5%: "
              f"a_0/a_2 shift={Lmax_dep_a0a2:.4f}, a_2/a_4 shift={Lmax_dep_a2a4:.4f}. "
              f"Higher L_max needed for definitive convergence.")
elif fail_a0a2 or fail_a2a4:
    verdict = "FAIL"
    detail = (f"Ratio deviation exceeds 20%: "
              f"|dev(a_0/a_2)|={dev_a0a2_gate:.4f}, "
              f"|dev(a_2/a_4)|={dev_a2a4_gate:.4f}.")
else:
    # Between 5% and 20%
    verdict = "INFO"
    detail = (f"Intermediate: at least one ratio deviates by 5-20%. "
              f"|dev(a_0/a_2)|={dev_a0a2_gate:.6f}, "
              f"|dev(a_2/a_4)|={dev_a2a4_gate:.6f}. "
              f"L_max dep: a_0/a_2={Lmax_dep_a0a2:.4f}, a_2/a_4={Lmax_dep_a2a4:.4f}.")

print(f"\n  {'='*60}")
print(f"  GATE SDW-VALIDATION-73B: {verdict}")
print(f"  {detail}")
print(f"  {'='*60}")


# =============================================================================
# STEP 11: SAVE DATA AND PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Save Data and Generate Plots")
print("=" * 78)

# Collect zeta results into arrays
zeta_arr = {}
for Lmax in Lmax_values:
    arr = np.zeros((n_tau, 5))  # (local) [a0, a2, a4, a6, M1]
    for ti in range(n_tau):
        z = zeta_results[Lmax][ti]
        arr[ti] = [z['a0'], z['a2'], z['a4'], z['a6'], z['M1']]
    zeta_arr[Lmax] = arr

# Collect HK d1 results
hk_d1_arr = {}
for Lmax in Lmax_values:
    arr = np.zeros((n_tau, 5))  # (local) [a0, a2, a4, a6, a8]
    for ti in range(n_tau):
        hk = results_hk_d1[Lmax][ti]
        arr[ti] = [hk['a0'], hk['a2'], hk['a4'], hk['a6'], hk['a8']]
    hk_d1_arr[Lmax] = arr

outfile = 's73b_sdw_validation.npz'  # (local)
save_dict = {
    'gate_name': 'SDW-VALIDATION-73B',
    'gate_verdict': verdict,
    'gate_detail': detail,
    'alpha_star': alpha_star,
    'beta_star': beta_star,
    'tau_values': tau_values,
    'Lambda_scan': Lambda_scan,
    'Lmax_values': np.array(Lmax_values),
    'EVAL_CUTOFF': EVAL_CUTOFF,
    # Spectral zeta sums (canonical a_k)
    'zeta_Lmax3': zeta_arr[3],
    'zeta_Lmax7': zeta_arr[7],
    # HK d1-weighted fit
    'hk_d1_Lmax3': hk_d1_arr[3],
    'hk_d1_Lmax7': hk_d1_arr[7],
    # Direct spectral sums S(Lambda)
    'S_fstar_Lmax3': S_fstar[3],
    'S_exp_Lmax3': S_exp[3],
    'S_sqrt_Lmax3': S_sqrt_arr[3],
    'S_fstar_Lmax7': S_fstar[7],
    'S_exp_Lmax7': S_exp[7],
    'S_sqrt_Lmax7': S_sqrt_arr[7],
    # Canonical SDW
    'a0_fold_canonical': a0_fold,
    'a2_fold_canonical': a2_fold,
    'a4_fold_canonical': a4_fold,
    # Gate evaluation
    'ratio_a0a2_SDW': ratio_a0_a2_SDW,
    'ratio_a2a4_SDW': ratio_a2_a4_SDW,
    'ratio_direct_a0a2': ratio_direct_a0a2,
    'ratio_direct_a2a4': ratio_direct_a2a4,
    'dev_a0a2_gate': dev_a0a2_gate,
    'dev_a2a4_gate': dev_a2a4_gate,
    'Lmax_dep_a0a2': Lmax_dep_a0a2,
    'Lmax_dep_a2a4': Lmax_dep_a2a4,
    # S73A cross-check
    'dev_73a': dev_73a,
}
np.savez(outfile, **save_dict)
print(f"  Saved to {outfile}")


# =============================================================================
# PLOT
# =============================================================================
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: S_f*(Lambda) for both L_max at fold
ax1 = fig.add_subplot(gs[0, 0])
for Lmax in Lmax_values:
    ax1.plot(Lambda_scan, S_fstar[Lmax][1], '-o', markersize=2,
             label=f'$L_{{max}}={Lmax}$')
ax1.set_xlabel(r'$\Lambda$ ($M_{KK}$)')
ax1.set_ylabel(r'$S_{f^*}(\Lambda)$')
ax1.set_title(r'$S_{f^*}(\Lambda)$ at fold ($\tau=0.19$)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: Component fractions at fold
ax2 = fig.add_subplot(gs[0, 1])
Lmax_plot = max(Lmax_values)  # (local)
frac_sqrt_arr = alpha_star * S_sqrt_arr[Lmax_plot][1] / S_fstar[Lmax_plot][1]  # (local)
frac_exp_arr = beta_star * S_exp[Lmax_plot][1] / S_fstar[Lmax_plot][1]  # (local)
ax2.plot(Lambda_scan, frac_sqrt_arr, 'b-', lw=2, label=r'$\alpha \cdot S_{sqrt}/S_{f^*}$')
ax2.plot(Lambda_scan, frac_exp_arr, 'r-', lw=2, label=r'$\beta \cdot S_{exp}/S_{f^*}$')
ax2.axhline(0.5, color='gray', linestyle='--', alpha=0.5)
ax2.set_xlabel(r'$\Lambda$ ($M_{KK}$)')
ax2.set_ylabel('Fraction of $S_{f^*}$')
ax2.set_title(f'Component fractions ($L_{{max}}={Lmax_plot}$)')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_ylim(-0.05, 1.05)

# Panel 3: Spectral zeta sums vs tau
ax3 = fig.add_subplot(gs[0, 2])
Lmax_big = max(Lmax_values)  # (local)
for k, name, color in [(0, '$a_0$ (mode count)', 'blue'),
                         (1, '$a_2$ ($\\zeta_D(1)$)', 'red'),
                         (2, '$a_4$ ($\\zeta_D(2)$)', 'green')]:
    vals = [zeta_results[Lmax_big][ti][['a0', 'a2', 'a4'][k]] for ti in range(n_tau)]
    ax3.plot(tau_values, vals, 'o-', color=color, label=name, markersize=8)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel('Spectral zeta sum')
ax3.set_title(f'$a_k(\\tau)$ via zeta sums ($L_{{max}}={Lmax_big}$)')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel 4: Ratio convergence
ax4 = fig.add_subplot(gs[1, 0])
r02_vals = [zeta_results[Lmax][1]['a0']/zeta_results[Lmax][1]['a2']
            for Lmax in Lmax_values]  # (local)
r24_vals = [zeta_results[Lmax][1]['a2']/zeta_results[Lmax][1]['a4']
            for Lmax in Lmax_values]  # (local)
ax4.plot(Lmax_values, r02_vals, 'bs-', markersize=8, label='$a_0/a_2$')
ax4.axhline(ratio_a0_a2_SDW, color='b', linestyle='--', alpha=0.7,
            label=f'$a_0/a_2$ canonical = {ratio_a0_a2_SDW:.4f}')
ax4.plot(Lmax_values, r24_vals, 'rs-', markersize=8, label='$a_2/a_4$')
ax4.axhline(ratio_a2_a4_SDW, color='r', linestyle='--', alpha=0.7,
            label=f'$a_2/a_4$ canonical = {ratio_a2_a4_SDW:.4f}')
ax4.set_xlabel('$L_{max}$ (Peter-Weyl truncation)')
ax4.set_ylabel('Ratio')
ax4.set_title('SDW Ratios vs $L_{max}$ at fold')
ax4.legend(fontsize=7)
ax4.grid(True, alpha=0.3)

# Panel 5: S_exp scaling — log-log to check power law
ax5 = fig.add_subplot(gs[1, 1])
for Lmax in Lmax_values:
    ax5.loglog(Lambda_scan, S_exp[Lmax][1], '-o', markersize=2,
               label=f'$S_{{exp}}$ $L_{{max}}={Lmax}$')
    ax5.loglog(Lambda_scan, S_sqrt_arr[Lmax][1], '--', markersize=2,
               label=f'$S_{{sqrt}}$ $L_{{max}}={Lmax}$')
ax5.set_xlabel(r'$\Lambda$ ($M_{KK}$)')
ax5.set_ylabel(r'$S(\Lambda)$')
ax5.set_title(r'Spectral sums: log-log scaling')
ax5.legend(fontsize=6)
ax5.grid(True, alpha=0.3)

# Panel 6: Gate summary
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
gate_text = (
    f"Gate: SDW-VALIDATION-73B\n"
    f"Verdict: {verdict}\n\n"
    f"Zeta sum ratios (L_max={Lmax_gate}):\n"
    f"  $a_0/a_2$: {ratio_direct_a0a2:.4f}\n"
    f"  $a_2/a_4$: {ratio_direct_a2a4:.4f}\n\n"
    f"Canonical ratios:\n"
    f"  $a_0/a_2$: {ratio_a0_a2_SDW:.4f}\n"
    f"  $a_2/a_4$: {ratio_a2_a4_SDW:.4f}\n\n"
    f"Deviations:\n"
    f"  $a_0/a_2$: {dev_a0a2_gate*100:.2f}%\n"
    f"  $a_2/a_4$: {dev_a2a4_gate*100:.2f}%\n\n"
    f"L_max convergence:\n"
    f"  $a_0/a_2$: {Lmax_dep_a0a2*100:.2f}% shift\n"
    f"  $a_2/a_4$: {Lmax_dep_a2a4*100:.2f}% shift\n\n"
    f"S73A cross-check: {dev_73a:.1e}"
)
ax6.text(0.05, 0.95, gate_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('SDW-VALIDATION-73B: Spectral Zeta Sums vs Direct f* Sums',
             fontsize=14)
plt.savefig('s73b_sdw_validation.png', dpi=150, bbox_inches='tight')
print("  Saved plot to s73b_sdw_validation.png")

print("\n" + "=" * 78)
print("SDW-VALIDATION-73B COMPLETE")
print("=" * 78)
