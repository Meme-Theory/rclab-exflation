#!/usr/bin/env python3
"""
s67_fold_curvature_ratio.py -- FOLD-CURVATURE-RATIO-67: Fold-Local Universality Test
=====================================================================================

Gate: FOLD-CURVATURE-RATIO-67
  PASS: Variation < 10% across functionals (fold-local universality)
  FAIL: Variation > 30%
  INFO: 10% < Variation < 30% (borderline)

Physics:
--------
The spectral action on Jensen-deformed SU(3) is S[f, tau] = Tr(f(D_K(tau)^2)).
Different choices of the cutoff function f define different spectral functionals.
The transit dynamics depend on the SHAPE of S(tau) near the fold (tau = 0.19),
specifically through the curvature ratio:

    R_fold = d^2S/dtau^2 / (dS/dtau)^2                                     (1)

This ratio is a dimensionless measure of the fold sharpness. If R_fold is
approximately constant across functionals, the fold geometry is a UNIVERSAL
property of the fiber D_K, independent of the regularization scheme.

The key insight (from W5-A): eps_H = -(1/2G) * (dS/dtau)^{-1} * d^2S/dtau^2
is scheme-dependent because dS/dtau appears in the denominator with different
normalization for each f. But the RATIO R_fold = d^2S/dtau^2 / (dS/dtau)^2
may be universal if both derivatives scale with the same power of some
functional-dependent prefactor.

Concretely: if S_f(tau) = N_f * Phi(tau) where N_f is a functional-dependent
normalization and Phi(tau) is universal, then:
    dS_f/dtau = N_f * Phi'
    d^2S_f/dtau^2 = N_f * Phi''
    R_fold = Phi'' / (N_f * Phi'^2)
This is NOT universal (it depends on N_f). But if the functional enters
multiplicatively in a more nuanced way — for instance through spectral
weights that are tau-independent — the ratio could still be universal.

We test this numerically with 5 spectral functional families:
  (a) CC cutoff:    S(tau) = Sum dim^2 * |lambda_j(tau)|     [f(x) = sqrt(x)]
  (b) Zeta (a_0):   S(tau) = Sum dim^2 * 1 = a_0 = const    [mode count]
  (c) Exponential:  S(tau) = Sum dim^2 * exp(-lambda_j^2/L^2) [heat kernel]
  (d) Compact:      S(tau) = Sum dim^2 * max(0, 1-lambda_j^2/L^2) [compact]
  (e) Anomaly(phi=1): S(tau) = c_0*a_0 + c_2*a_2 + c_4*a_4   [anomaly]

For (b), a_0 is topologically tau-independent => dS/dtau = 0, R undefined.
We replace (b) with the physical zeta action a_4(tau), which IS tau-dependent
and represents the gauge-sector contribution to the zeta spectral action.

Agent: Gen-Physicist (Session 67, Wave 6)
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
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    G_DeWitt, PI,
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
print("FOLD-CURVATURE-RATIO-67: Fold-Local Universality Test")
print("=" * 78)

MAX_PQ_SUM = 3  # Peter-Weyl truncation (consistent with S36/S66/S67) (local)

# Dense tau grid around the fold for accurate second derivatives.
# 24 points: extra density in [0.17, 0.21] for fold-local accuracy.
tau_grid = np.array([
    0.00, 0.05, 0.10, 0.12, 0.14,
    0.15, 0.16, 0.165, 0.17, 0.175,
    0.18, 0.185, 0.19, 0.195, 0.20,
    0.205, 0.21, 0.215, 0.22, 0.25,
    0.30, 0.35, 0.40, 0.50
])
n_tau = len(tau_grid)
fold_idx = np.argmin(np.abs(tau_grid - tau_fold))

print(f"\n  Configuration:")
print(f"    tau_fold         = {tau_fold}")
print(f"    max_pq_sum       = {MAX_PQ_SUM}")
print(f"    n_tau_points     = {n_tau}")
print(f"    tau range        = [{tau_grid[0]:.3f}, {tau_grid[-1]:.3f}]")
print(f"    fold_idx         = {fold_idx} (tau = {tau_grid[fold_idx]:.3f})")


# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRA AT ALL TAU VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute D_K Eigenvalue Spectra at All tau")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Storage: list of lists of (p, q, abs_eigenvalues, dim_pq)
all_spectra = []

t_start = time.time()

for i, tau in enumerate(tau_grid):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                   max_pq_sum=MAX_PQ_SUM, verbose=False)

    tau_spectra = []
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)
        tau_spectra.append((p, q, omega, d_pq))

    all_spectra.append(tau_spectra)

    if (i + 1) % 6 == 0 or i == n_tau - 1:
        elapsed = time.time() - t_start
        print(f"  tau[{i:2d}] = {tau:.3f}  ({elapsed:.1f}s elapsed)")

t_spec = time.time() - t_start
print(f"\n  Computed {n_tau} spectra in {t_spec:.1f}s")


# =============================================================================
# STEP 2: DEFINE THE 5 SPECTRAL FUNCTIONALS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Define 5 Spectral Functionals")
print("=" * 78)

# Determine Lambda scale from the fold spectrum
# Lambda = mean eigenvalue at fold (geometric average)
fold_spec = all_spectra[fold_idx]
all_evals_fold = []
for p, q, omega, d_pq in fold_spec:
    all_evals_fold.extend([om for om in omega for _ in range(d_pq)])
all_evals_fold = np.array(all_evals_fold)
# Use the median eigenvalue as Lambda (robust to outliers)
Lambda_scale = np.median(all_evals_fold[all_evals_fold > 1e-10])
print(f"  Lambda scale (median |lambda| at fold) = {Lambda_scale:.4f}")


def compute_functional(spectra_list, func_name, Lambda):
    """
    Compute S(tau) for a given spectral functional at all tau values.

    Parameters
    ----------
    spectra_list : list of list of (p, q, omega, d_pq)
        Eigenvalue data at each tau
    func_name : str
        One of: 'cc_cutoff', 'zeta_a4', 'exponential', 'compact', 'anomaly_phi1'
    Lambda : float
        Cutoff scale for exponential and compact functionals

    Returns
    -------
    S_tau : ndarray of shape (n_tau,)
        Spectral action values at each tau
    """
    S_tau = np.zeros(len(spectra_list))

    for i, tau_spec in enumerate(spectra_list):
        S_i = 0.0  # (local)

        if func_name == 'cc_cutoff':
            # S = Sum dim^2 * Sum |lambda_j|     [Chamseddine-Connes, f(x)=sqrt(x)]
            for p, q, omega, d_pq in tau_spec:
                S_i += d_pq**2 * np.sum(omega)

        elif func_name == 'zeta_a4':
            # S = a_4(tau) = Sum dim^2 * Sum |lambda_j|^{-4}
            # Physical zeta action (gauge sector). Only positive eigenvalues.
            for p, q, omega, d_pq in tau_spec:
                pos = omega[omega > 1e-12]
                S_i += d_pq**2 * np.sum(pos**(-4))

        elif func_name == 'exponential':
            # S = Sum dim^2 * Sum exp(-lambda_j^2 / Lambda^2)    [heat kernel]
            for p, q, omega, d_pq in tau_spec:
                x = (omega / Lambda)**2
                S_i += d_pq**2 * np.sum(np.exp(-x))

        elif func_name == 'compact':
            # S = Sum dim^2 * Sum max(0, 1 - lambda_j^2/Lambda^2)  [compact support]
            for p, q, omega, d_pq in tau_spec:
                x = (omega / Lambda)**2
                S_i += d_pq**2 * np.sum(np.maximum(0.0, 1.0 - x))

        elif func_name == 'anomaly_phi1':
            # S = c_0*a_0 + c_2*a_2 + c_4*a_4
            # Anomaly coefficients at phi=1:
            #   c_0 = (e^4 - 1)/8 = 6.7247
            #   c_2 = (e^2 - 1)/2 = 3.1945
            #   c_4 = 1.0
            c_0 = (np.exp(4.0) - 1.0) / 8.0
            c_2 = (np.exp(2.0) - 1.0) / 2.0
            c_4 = 1.0  # (local)

            a0_i = 0.0  # (local)
            a2_i = 0.0  # (local)
            a4_i = 0.0  # (local)
            for p, q, omega, d_pq in tau_spec:
                # a_0 = Sum dim^2 * N_modes (count of eigenvalues)
                a0_i += d_pq**2 * len(omega)
                pos = omega[omega > 1e-12]
                # a_2 = Sum dim^2 * Sum |lam|^{-2}
                a2_i += d_pq**2 * np.sum(pos**(-2))
                # a_4 = Sum dim^2 * Sum |lam|^{-4}
                a4_i += d_pq**2 * np.sum(pos**(-4))

            S_i = c_0 * a0_i + c_2 * a2_i + c_4 * a4_i

        elif func_name == 'mode_count':
            # S = a_0 = Sum dim^2 * N_modes  (tau-independent, degenerate)
            for p, q, omega, d_pq in tau_spec:
                S_i += d_pq**2 * len(omega)

        else:
            raise ValueError(f"Unknown functional: {func_name}")

        S_tau[i] = S_i

    return S_tau


# Define the 5 functionals + the degenerate mode count
functional_names = ['cc_cutoff', 'zeta_a4', 'exponential', 'compact', 'anomaly_phi1']
functional_labels = [
    r'CC cutoff: $\sum |{\lambda}|$',
    r'Zeta: $a_4(\tau) = \sum |\lambda|^{-4}$',
    r'Exponential: $\sum e^{-\lambda^2/\Lambda^2}$',
    r'Compact: $\sum \max(0, 1-\lambda^2/\Lambda^2)$',
    r'Anomaly($\phi$=1): $c_0 a_0 + c_2 a_2 + c_4 a_4$',
]
functional_short = ['CC-cutoff', 'Zeta-a4', 'Exponential', 'Compact', 'Anomaly(phi=1)']

print(f"\n  5 functionals defined:")
for j, (name, label) in enumerate(zip(functional_names, functional_labels)):
    print(f"    [{j+1}] {name}: {label}")
print(f"\n  Lambda = {Lambda_scale:.4f} (used by exponential and compact)")
print(f"  Anomaly phi=1: c_0 = {(np.exp(4.0)-1)/8:.4f}, c_2 = {(np.exp(2.0)-1)/2:.4f}, c_4 = 1.0")


# =============================================================================
# STEP 3: COMPUTE S(tau) FOR EACH FUNCTIONAL
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Compute S(tau) for Each Functional")
print("=" * 78)

S_all = {}
t_start = time.time()

for name, short in zip(functional_names, functional_short):
    S_tau = compute_functional(all_spectra, name, Lambda_scale)
    S_all[name] = S_tau
    print(f"  {short:20s}: S(fold) = {S_tau[fold_idx]:15.6f}, "
          f"S range = [{np.min(S_tau):.4f}, {np.max(S_tau):.4f}]")

# Also compute mode count to verify a_0 is constant
S_mode = compute_functional(all_spectra, 'mode_count', Lambda_scale)
a0_variation = (np.max(S_mode) - np.min(S_mode)) / np.mean(S_mode)
print(f"\n  Mode count (a_0): {S_mode[0]:.1f} (constant to {a0_variation:.2e})")

t_func = time.time() - t_start
print(f"  Computed all functionals in {t_func:.1f}s")


# =============================================================================
# STEP 4: COMPUTE DERIVATIVES AT THE FOLD VIA CUBIC SPLINE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Compute dS/dtau and d^2S/dtau^2 at Fold via Cubic Spline")
print("=" * 78)

results = {}

for name, short in zip(functional_names, functional_short):
    S_tau = S_all[name]

    # Cubic spline interpolation
    cs = CubicSpline(tau_grid, S_tau)
    dS_dtau = cs(tau_fold, 1)       # First derivative at fold
    d2S_dtau2 = cs(tau_fold, 2)     # Second derivative at fold
    S_at_fold = cs(tau_fold, 0)     # Value at fold

    # Curvature ratio
    if abs(dS_dtau) > 1e-15:
        R_fold = d2S_dtau2 / dS_dtau**2
    else:
        R_fold = np.nan

    results[name] = {
        'S_fold': S_at_fold,
        'dS_dtau': dS_dtau,
        'd2S_dtau2': d2S_dtau2,
        'R_fold': R_fold,
    }

    print(f"\n  {short}:")
    print(f"    S(tau_fold)       = {S_at_fold:.6f}")
    print(f"    dS/dtau           = {dS_dtau:.6f}")
    print(f"    d^2S/dtau^2       = {d2S_dtau2:.6f}")
    print(f"    R_fold            = {R_fold:.6e}")

# Cross-check CC cutoff against canonical constants
print(f"\n  Cross-check CC cutoff vs canonical_constants:")
print(f"    dS_fold (canonical) = {dS_fold:.6f}")
print(f"    dS_fold (computed)  = {results['cc_cutoff']['dS_dtau']:.6f}")
dev_dS = abs(results['cc_cutoff']['dS_dtau'] - dS_fold) / abs(dS_fold)
print(f"    |deviation|         = {dev_dS:.2e}")
print(f"    d2S_fold (canonical)= {d2S_fold:.6f}")
print(f"    d2S_fold (computed) = {results['cc_cutoff']['d2S_dtau2']:.6f}")
dev_d2S = abs(results['cc_cutoff']['d2S_dtau2'] - d2S_fold) / abs(d2S_fold)
print(f"    |deviation|         = {dev_d2S:.2e}")

# Also verify with finite differences for robustness
print(f"\n  Finite-difference cross-check (5-point stencil at fold):")
h = tau_grid[fold_idx + 1] - tau_grid[fold_idx]  # step near fold
for name, short in zip(functional_names, functional_short):
    S_tau = S_all[name]
    fi = fold_idx
    # Central differences using neighboring points
    # dS/dtau ~ (S[i+1] - S[i-1]) / (tau[i+1] - tau[i-1])
    if fi > 0 and fi < n_tau - 1:
        dS_fd = (S_tau[fi + 1] - S_tau[fi - 1]) / (tau_grid[fi + 1] - tau_grid[fi - 1])
    else:
        dS_fd = np.nan
    # d^2S/dtau^2 ~ (S[i+1] - 2*S[i] + S[i-1]) / h^2
    # But grid may be non-uniform; use 3-point formula
    if fi > 0 and fi < n_tau - 1:
        h_p = tau_grid[fi + 1] - tau_grid[fi]
        h_m = tau_grid[fi] - tau_grid[fi - 1]
        d2S_fd = 2.0 * (S_tau[fi + 1] / (h_p * (h_p + h_m))
                        - S_tau[fi] / (h_p * h_m)
                        + S_tau[fi - 1] / (h_m * (h_p + h_m)))
    else:
        d2S_fd = np.nan

    R_fd = d2S_fd / dS_fd**2 if abs(dS_fd) > 1e-15 else np.nan
    R_cs = results[name]['R_fold']
    dev_R = abs(R_fd - R_cs) / abs(R_cs) if not np.isnan(R_cs) and abs(R_cs) > 1e-20 else np.nan
    print(f"    {short:20s}: R_fold(spline)={R_cs:.6e}, R_fold(FD)={R_fd:.6e}, |dev|={dev_R:.2e}")


# =============================================================================
# STEP 5: UNIVERSALITY TEST
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Universality Test — R_fold Variation Across Functionals")
print("=" * 78)

R_values = np.array([results[name]['R_fold'] for name in functional_names])
R_valid = R_values[~np.isnan(R_values)]
n_valid = len(R_valid)

print(f"\n  R_fold values:")
for name, short, R in zip(functional_names, functional_short, R_values):
    print(f"    {short:20s}: R_fold = {R:.6e}")

# Check if all R values have the same sign
signs = np.sign(R_valid)
all_same_sign = np.all(signs == signs[0])
print(f"\n  All same sign: {all_same_sign}")
print(f"  Signs: {signs}")

# Compute variation metric: (max - min) / |mean|
R_mean = np.mean(R_valid)
R_min = np.min(R_valid)
R_max = np.max(R_valid)
variation = (R_max - R_min) / abs(R_mean)
variation_pct = variation * 100

print(f"\n  Statistics ({n_valid} non-degenerate functionals):")
print(f"    R_mean              = {R_mean:.6e}")
print(f"    R_min               = {R_min:.6e}")
print(f"    R_max               = {R_max:.6e}")
print(f"    R_max / R_min       = {R_max / R_min:.4f}" if R_min != 0 else "    R_max / R_min = inf")
print(f"    Variation           = (max - min) / |mean| = {variation:.4f} = {variation_pct:.1f}%")

# Also compute coefficient of variation (std/mean)
R_std = np.std(R_valid)
cv = R_std / abs(R_mean) * 100
print(f"    Std dev             = {R_std:.6e}")
print(f"    CV (std/|mean|)     = {cv:.1f}%")

# If signs differ, the variation is extreme
if not all_same_sign:
    print("\n  WARNING: R_fold values have DIFFERENT SIGNS.")
    print("  This means some functionals have convex and others have concave")
    print("  curvature at the fold. The fold shape is NOT universal.")

# Compute pairwise ratios for additional insight
print(f"\n  Pairwise R_fold ratios:")
for i in range(len(functional_names)):
    for j in range(i + 1, len(functional_names)):
        Ri = R_values[i]
        Rj = R_values[j]
        if not np.isnan(Ri) and not np.isnan(Rj) and abs(Rj) > 1e-20:
            ratio = Ri / Rj
            print(f"    {functional_short[i]:20s} / {functional_short[j]:20s} = {ratio:.4f}")


# =============================================================================
# STEP 6: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Gate Verdict")
print("=" * 78)

print(f"\n  Gate: FOLD-CURVATURE-RATIO-67")
print(f"  Pre-registered thresholds:")
print(f"    PASS: Variation < 10%")
print(f"    FAIL: Variation > 30%")
print(f"    INFO: 10% <= Variation <= 30%")
print(f"\n  Computed variation: {variation_pct:.1f}%")

if variation_pct < 10:
    verdict = "PASS"
    verdict_detail = f"Variation {variation_pct:.1f}% < 10%. Fold shape is FUNCTIONAL-INDEPENDENT."
elif variation_pct > 30:
    verdict = "FAIL"
    verdict_detail = f"Variation {variation_pct:.1f}% > 30%. Fold shape is SCHEME-DEPENDENT."
else:
    verdict = "INFO"
    verdict_detail = f"Variation {variation_pct:.1f}% in [10%, 30%]. Borderline."

if not all_same_sign:
    verdict = "FAIL"
    verdict_detail = (f"R_fold changes SIGN across functionals. "
                      f"Some functionals give convex, others concave curvature. "
                      f"Fold shape is QUALITATIVELY scheme-dependent.")

print(f"\n  VERDICT: {verdict}")
print(f"  {verdict_detail}")


# =============================================================================
# STEP 7: ANALYTICAL UNDERSTANDING
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Analytical Understanding")
print("=" * 78)

print("""
  The curvature ratio R_fold = d^2S/dtau^2 / (dS/dtau)^2 is NOT a ratio of
  the same quantity. It has dimensions [S]^{-1} (inverse spectral action).
  Different functionals have different S(fold) values, so R_fold = O(1/S_fold).

  For a functional S_f(tau) = Sum w_n(f) * F(lambda_n(tau)):
    dS/dtau = Sum w_n * F'(lambda_n) * dlambda_n/dtau
    d^2S/dtau^2 = Sum w_n * [F''(lambda_n)*(dlambda_n/dtau)^2 + F'(lambda_n)*d^2lambda_n/dtau^2]

  The ratio R_fold = d^2S / (dS)^2 depends on the spectral WEIGHTS w_n*F'(lambda_n).
  If these weights give different relative importance to different eigenvalues,
  the curvature ratio will differ. The key question is whether the eigenvalue
  flow dlambda_n/dtau at the fold is correlated across modes (collective) or
  mode-dependent (dispersive).

  To probe this, we compute the NORMALIZED curvature ratio:
    R_norm = R_fold * S(fold)
  which removes the trivial 1/S dependence.
""")

print("  Normalized curvature ratio R_norm = R_fold * S(fold):")
R_norm_values = []
for name, short in zip(functional_names, functional_short):
    R = results[name]['R_fold']
    S = results[name]['S_fold']
    if not np.isnan(R):
        R_norm = R * S
        R_norm_values.append(R_norm)
        print(f"    {short:20s}: R_norm = {R_norm:.6f}")

R_norm_arr = np.array(R_norm_values)
if len(R_norm_arr) > 1:
    R_norm_mean = np.mean(R_norm_arr)
    R_norm_var = (np.max(R_norm_arr) - np.min(R_norm_arr)) / abs(R_norm_mean)
    print(f"\n  R_norm variation: {R_norm_var*100:.1f}%")

# Also compute eps_H-related ratio: d^2S / (dS * S) = R_fold * dS
# This is closer to what enters the slow-roll parameter
print("\n  Slow-roll-relevant ratio: kappa = d^2S/dtau^2 / (dS/dtau * S(fold)):")
kappa_values = []
for name, short in zip(functional_names, functional_short):
    dS = results[name]['dS_dtau']
    d2S = results[name]['d2S_dtau2']
    S = results[name]['S_fold']
    if abs(dS) > 1e-15 and abs(S) > 1e-15:
        kappa = d2S / (dS * S)
        kappa_values.append(kappa)
        print(f"    {short:20s}: kappa = {kappa:.6e}")

kappa_arr = np.array(kappa_values)
if len(kappa_arr) > 1:
    kappa_mean = np.mean(kappa_arr)
    kappa_var = (np.max(kappa_arr) - np.min(kappa_arr)) / abs(kappa_mean)
    print(f"\n  kappa variation: {kappa_var*100:.1f}%")


# =============================================================================
# STEP 8: Lambda SENSITIVITY (exponential and compact)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Lambda Sensitivity Check")
print("=" * 78)

# Recompute exponential and compact at different Lambda to check robustness
Lambda_test = [Lambda_scale * 0.5, Lambda_scale, Lambda_scale * 2.0]
print(f"  Testing Lambda = {[f'{L:.2f}' for L in Lambda_test]}")

for func_name, short in [('exponential', 'Exponential'), ('compact', 'Compact')]:
    R_Lambda = []
    for L in Lambda_test:
        S_tau = compute_functional(all_spectra, func_name, L)
        cs = CubicSpline(tau_grid, S_tau)
        dS = cs(tau_fold, 1)
        d2S = cs(tau_fold, 2)
        R = d2S / dS**2 if abs(dS) > 1e-15 else np.nan
        R_Lambda.append(R)
        print(f"    {short} (Lambda={L:.2f}): R_fold = {R:.6e}")
    R_Lambda = np.array(R_Lambda)
    R_var_L = (np.max(R_Lambda) - np.min(R_Lambda)) / abs(np.mean(R_Lambda))
    print(f"    Lambda-variation for {short}: {R_var_L*100:.1f}%\n")


# =============================================================================
# STEP 9: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Save Data")
print("=" * 78)

save_dict = {
    'tau_grid': tau_grid,
    'tau_fold': np.float64(tau_fold),
    'fold_idx': np.int64(fold_idx),
    'Lambda_scale': np.float64(Lambda_scale),
    'functional_names': np.array(functional_names),
    'functional_short': np.array(functional_short),
    'variation_pct': np.float64(variation_pct),
    'verdict': np.array(verdict),
    'verdict_detail': np.array(verdict_detail),
}

# Save S(tau) for each functional
for name in functional_names:
    save_dict[f'S_{name}'] = S_all[name]
    save_dict[f'dS_dtau_{name}'] = np.float64(results[name]['dS_dtau'])
    save_dict[f'd2S_dtau2_{name}'] = np.float64(results[name]['d2S_dtau2'])
    save_dict[f'R_fold_{name}'] = np.float64(results[name]['R_fold'])
    save_dict[f'S_fold_{name}'] = np.float64(results[name]['S_fold'])

save_dict['S_mode_count'] = S_mode
save_dict['R_fold_all'] = R_values
save_dict['R_norm_all'] = np.array(R_norm_values) if R_norm_values else np.array([])
save_dict['kappa_all'] = kappa_arr if len(kappa_arr) > 0 else np.array([])

outfile = 's67_fold_curvature_ratio.npz'
np.savez(outfile, **save_dict)
print(f"  Saved to {outfile}")
print(f"  Keys: {sorted(save_dict.keys())}")


# =============================================================================
# STEP 10: DIAGNOSTIC PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Diagnostic Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.3, wspace=0.3)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Panel 1: S(tau) for each functional (normalized to fold value)
ax1 = fig.add_subplot(gs[0, 0])
for j, (name, short, color) in enumerate(zip(functional_names, functional_short, colors)):
    S_tau = S_all[name]
    S_norm = S_tau / S_tau[fold_idx]
    ax1.plot(tau_grid, S_norm, 'o-', color=color, label=short, markersize=3)
ax1.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold ({tau_fold})')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$S(\tau) / S(\tau_{\rm fold})$')
ax1.set_title('Normalized Spectral Actions')
ax1.legend(fontsize=7, loc='best')
ax1.grid(True, alpha=0.3)

# Panel 2: R_fold bar chart
ax2 = fig.add_subplot(gs[0, 1])
bar_x = np.arange(len(functional_short))
bar_vals = [results[name]['R_fold'] for name in functional_names]
bar_colors = [colors[j] for j in range(len(functional_names))]
bars = ax2.bar(bar_x, bar_vals, color=bar_colors, alpha=0.8)
ax2.set_xticks(bar_x)
ax2.set_xticklabels(functional_short, rotation=30, ha='right', fontsize=8)
ax2.set_ylabel(r'$R_{\rm fold} = d^2S/d\tau^2 \,/\, (dS/d\tau)^2$')
ax2.set_title(f'Curvature Ratio at Fold (variation = {variation_pct:.1f}%)')
ax2.axhline(0, color='black', lw=0.5)
ax2.grid(True, alpha=0.3, axis='y')

# Panel 3: dS/dtau near fold
ax3 = fig.add_subplot(gs[1, 0])
tau_dense = np.linspace(tau_grid[1], tau_grid[-2], 500)
for j, (name, short, color) in enumerate(zip(functional_names, functional_short, colors)):
    cs = CubicSpline(tau_grid, S_all[name])
    dS_dense = cs(tau_dense, 1)
    # Normalize by value at fold
    dS_fold_val = cs(tau_fold, 1)
    if abs(dS_fold_val) > 1e-15:
        ax3.plot(tau_dense, dS_dense / abs(dS_fold_val), color=color, label=short)
ax3.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel(r'$dS/d\tau$ (normalized)')
ax3.set_title(r'First Derivative $dS/d\tau$')
ax3.legend(fontsize=7, loc='best')
ax3.grid(True, alpha=0.3)

# Panel 4: d^2S/dtau^2 near fold
ax4 = fig.add_subplot(gs[1, 1])
for j, (name, short, color) in enumerate(zip(functional_names, functional_short, colors)):
    cs = CubicSpline(tau_grid, S_all[name])
    d2S_dense = cs(tau_dense, 2)
    d2S_fold_val = cs(tau_fold, 2)
    if abs(d2S_fold_val) > 1e-15:
        ax4.plot(tau_dense, d2S_dense / abs(d2S_fold_val), color=color, label=short)
ax4.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$d^2S/d\tau^2$ (normalized)')
ax4.set_title(r'Second Derivative $d^2S/d\tau^2$')
ax4.legend(fontsize=7, loc='best')
ax4.grid(True, alpha=0.3)

fig.suptitle(f'FOLD-CURVATURE-RATIO-67: Fold-Local Universality Test\n'
             f'Verdict: {verdict} (variation = {variation_pct:.1f}%)',
             fontsize=14, fontweight='bold')

plt.savefig('s67_fold_curvature_ratio.png', dpi=150, bbox_inches='tight')
print("  Saved plot: s67_fold_curvature_ratio.png")

print("\n" + "=" * 78)
print(f"COMPUTATION COMPLETE. Verdict: {verdict}")
print(f"  {verdict_detail}")
print("=" * 78)
