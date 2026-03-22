#!/usr/bin/env python3
"""
s44_dissolution_scaling.py -- DISSOLUTION-SCALING-44
=====================================================

Test whether the spectral triple dissolution threshold epsilon_crossover
scales as 1/sqrt(N) with mode count, or differently.

=== PHYSICS ===

In DISSOLUTION-43, we found epsilon_crossover ~ 0.014 at max_pq_sum=2 (N=432).
The question: is this a finite-size artifact that vanishes as N -> infinity
(dissolving the spectral triple under any perturbation), or does a finite
threshold survive in the thermodynamic limit?

If epsilon_crossover ~ 1/sqrt(N):
  - Thermodynamic limit epsilon_c -> 0
  - ANY nonzero foam perturbation dissolves the spectral triple given enough modes
  - The spectral triple is emergent: it exists only at scales where mode count is finite

If epsilon_crossover ~ constant:
  - A finite threshold persists at N -> infinity
  - The spectral triple has intrinsic robustness against foam

If epsilon_crossover ~ 1/N or 1/ln(N):
  - Intermediate scenarios with distinct physical implications

=== METHOD ===

For each max_pq_sum in {1, 2, 3, 4, 5}:
  1. Build block-diagonal D_K at tau = 0.19 (fold)
  2. Binary search for epsilon_c where <r> crosses the Poisson-GOE midpoint
  3. Use M random perturbation samples at each epsilon trial
  4. Fit epsilon_c(N) to competing models: N^{-1/2}, N^{-1}, ln(N)^{-1}, constant

=== GATE ===
DISSOLUTION-SCALING-44: PASS if 1/sqrt(N) confirmed. FAIL if constant. INFO otherwise.

Author: quantum-foam-theorist, Session 44
"""

import numpy as np
from numpy.linalg import eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit, minimize_scalar
import os
import sys
import time

t_start = time.time()

# Add tier0 path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

# Import from tier1_dirac_spectrum
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    dirac_operator_on_irrep,
    get_irrep,
    validate_connection,
    validate_omega_hermitian,
)
from canonical_constants import tau_fold as TAU_FOLD

# ============================================================
# CONSTANTS
# ============================================================
R_POISSON = 2 * np.log(2) - 1   # 0.38629
R_GOE = 0.5307                    # Atas et al. 2013
R_MIDPOINT = (R_POISSON + R_GOE) / 2.0  # ~0.459
DEGENERACY_TOL = 1e-10

# Per truncation level: (max_pq_sum, n_samples, n_binary_steps)
# Larger matrices need fewer samples (better self-averaging) but cost more per sample
TRUNCATION_CONFIGS = [
    (1,  40, 12),   # N=112,   fast
    (2,  30, 12),   # N=432,   fast (S43 baseline)
    (3,  20, 10),   # N=1232,  moderate
    (4,  10, 8),    # N=2912,  slow
    (5,   5, 6),    # N=6048,  very slow -- lightweight probe
]

np.random.seed(42)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def ratio_statistic(evals):
    """
    Compute Oganesyan-Huse ratio statistic <r> from eigenvalues.
    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    Poisson: <r> = 0.386, GOE: <r> = 0.531
    """
    evals = np.sort(np.real(evals))
    # Remove degeneracies
    unique = [evals[0]]
    for e in evals[1:]:
        if abs(e - unique[-1]) > DEGENERACY_TOL:
            unique.append(e)
    evals = np.array(unique)

    if len(evals) < 4:
        return np.nan

    spacings = np.diff(evals)
    spacings = spacings[spacings > DEGENERACY_TOL]

    if len(spacings) < 3:
        return np.nan

    ratios = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i + 1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))

    if len(ratios) == 0:
        return np.nan

    return np.mean(ratios)


def build_block_diagonal_H(max_pq_sum, gens, f_abc, gammas, E, Omega, verbose=True):
    """
    Build the block-diagonal Hamiltonian H_0 = i*D_K for all sectors with p+q <= max_pq_sum.

    Returns:
        H0: (total_dim, total_dim) Hermitian matrix
        block_starts: list of starting indices for each sector
        sector_dims: list of block dimensions
        sector_labels: list of "(p,q)" labels
        total_dim: total matrix dimension
    """
    sectors = []
    sector_dims = []
    sector_D_matrices = []
    sector_labels = []

    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            label = f"({p},{q})"

            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == dim_pq

                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                H_pi = 1j * D_pi

                block_dim = dim_pq * 16
                sectors.append((p, q, dim_pq))
                sector_dims.append(block_dim)
                sector_D_matrices.append(H_pi)
                sector_labels.append(label)

            except (NotImplementedError, RuntimeError) as e:
                if verbose:
                    print(f"  {label}: SKIPPED ({e})")

    total_dim = sum(sector_dims)

    H0 = np.zeros((total_dim, total_dim), dtype=complex)
    block_starts = []
    offset = 0
    for i, H_pi in enumerate(sector_D_matrices):
        d = sector_dims[i]
        block_starts.append(offset)
        H0[offset:offset + d, offset:offset + d] = H_pi
        offset += d

    return H0, block_starts, sector_dims, sector_labels, total_dim


def measure_r_at_epsilon(H0, total_dim, H0_norm, epsilon, n_samples):
    """
    Measure <r> at a given epsilon, averaged over n_samples random perturbations.

    The perturbation V is a random Hermitian matrix with ||V||_F ~ epsilon * ||H_0||_F.
    """
    sigma = epsilon * H0_norm / total_dim
    r_values = []

    for _ in range(n_samples):
        V_real = np.random.randn(total_dim, total_dim) * sigma
        V_imag = np.random.randn(total_dim, total_dim) * sigma
        V = (V_real + 1j * V_imag)
        V = (V + V.conj().T) / 2.0

        H_pert = H0 + V
        evals_pert = eigvalsh(H_pert)
        r_val = ratio_statistic(evals_pert)
        if not np.isnan(r_val):
            r_values.append(r_val)

    if len(r_values) == 0:
        return np.nan, np.nan

    r_arr = np.array(r_values)
    return np.mean(r_arr), np.std(r_arr) / np.sqrt(len(r_arr))


def binary_search_crossover(H0, total_dim, H0_norm, n_samples, n_steps,
                             eps_lo=1e-4, eps_hi=0.5, verbose=True):
    """
    Binary search for epsilon_crossover where <r> crosses R_MIDPOINT.

    Returns:
        epsilon_c: crossover value
        r_at_crossover: <r> at the crossover
        scan_log: list of (epsilon, r_mean, r_std) from the search
    """
    scan_log = []

    # First check endpoints
    r_lo, r_lo_err = measure_r_at_epsilon(H0, total_dim, H0_norm, eps_lo, n_samples)
    r_hi, r_hi_err = measure_r_at_epsilon(H0, total_dim, H0_norm, eps_hi, n_samples)
    scan_log.append((eps_lo, r_lo, r_lo_err))
    scan_log.append((eps_hi, r_hi, r_hi_err))

    if verbose:
        print(f"    eps_lo={eps_lo:.5f}: <r>={r_lo:.4f} +/- {r_lo_err:.4f}")
        print(f"    eps_hi={eps_hi:.5f}: <r>={r_hi:.4f} +/- {r_hi_err:.4f}")

    # If the low end is already above midpoint, the crossover is below our range
    if r_lo > R_MIDPOINT:
        if verbose:
            print(f"    WARNING: <r> at eps_lo already > midpoint. Crossover below {eps_lo:.5f}")
        return eps_lo, r_lo, scan_log

    # If the high end is still below midpoint, crossover is above our range
    if r_hi < R_MIDPOINT:
        if verbose:
            print(f"    WARNING: <r> at eps_hi still < midpoint. Crossover above {eps_hi:.5f}")
        return eps_hi, r_hi, scan_log

    # Binary search in log space
    log_lo = np.log10(eps_lo)
    log_hi = np.log10(eps_hi)

    for step in range(n_steps):
        log_mid = (log_lo + log_hi) / 2.0
        eps_mid = 10**log_mid

        r_mid, r_mid_err = measure_r_at_epsilon(H0, total_dim, H0_norm, eps_mid, n_samples)
        scan_log.append((eps_mid, r_mid, r_mid_err))

        if verbose:
            direction = ">" if r_mid > R_MIDPOINT else "<"
            print(f"    step {step+1}/{n_steps}: eps={eps_mid:.5f}, <r>={r_mid:.4f} {direction} {R_MIDPOINT:.4f}")

        if r_mid > R_MIDPOINT:
            log_hi = log_mid
        else:
            log_lo = log_mid

    # Final estimate: midpoint of converged bracket
    eps_c = 10**((log_lo + log_hi) / 2.0)

    # Measure at final estimate with more samples for accuracy
    r_final, r_final_err = measure_r_at_epsilon(H0, total_dim, H0_norm, eps_c, n_samples * 2)
    scan_log.append((eps_c, r_final, r_final_err))

    if verbose:
        print(f"    FINAL: eps_c = {eps_c:.5f}, <r> = {r_final:.4f} +/- {r_final_err:.4f}")

    return eps_c, r_final, scan_log


# ============================================================
# FITTING MODELS
# ============================================================

def model_sqrt_N(N, a):
    """epsilon_c = a / sqrt(N)"""
    return a / np.sqrt(N)

def model_inv_N(N, a):
    """epsilon_c = a / N"""
    return a / N

def model_inv_logN(N, a):
    """epsilon_c = a / ln(N)"""
    return a / np.log(N)

def model_const(N, a):
    """epsilon_c = a (constant)"""
    return np.full_like(N, a, dtype=float)

def model_power(N, a, alpha):
    """epsilon_c = a * N^{-alpha}"""
    return a * N**(-alpha)


# ============================================================
# MAIN COMPUTATION
# ============================================================

print("=" * 70)
print("DISSOLUTION-SCALING-44: Dissolution Threshold vs Mode Count")
print("=" * 70)
print(f"\nTau = {TAU_FOLD:.3f}")
print(f"Midpoint criterion: <r> = {R_MIDPOINT:.4f}")
print(f"Poisson: {R_POISSON:.4f}, GOE: {R_GOE:.4f}")

# ============================================================
# Step 1: Build SU(3) infrastructure (shared across truncations)
# ============================================================
print("\n--- Step 1: Build SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU_FOLD)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
mc_err = validate_connection(Gamma)
Omega = spinor_connection_offset(Gamma, gammas)
_, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Connection metric-compatibility error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian error: {ah_err:.2e}")

# ============================================================
# Step 2: Loop over truncation levels
# ============================================================
print("\n--- Step 2: Sweep over truncation levels ---")

results_N = []       # total_dim at each level
results_eps_c = []   # epsilon_crossover at each level
results_r_at_c = []  # <r> at crossover
results_scan = []    # full scan log
results_max_pq = []  # max_pq_sum at each level
results_n_sectors = []

for max_pq, n_samples, n_binary in TRUNCATION_CONFIGS:
    t_level_start = time.time()

    # Mode count
    total_dim_expected = 0
    n_sec_expected = 0
    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            total_dim_expected += 16 * dim_pq
            n_sec_expected += 1

    print(f"\n{'='*50}")
    print(f"max_pq_sum = {max_pq}: N_expected = {total_dim_expected}, "
          f"n_sectors = {n_sec_expected}")
    print(f"  n_samples = {n_samples}, binary_steps = {n_binary}")
    print(f"{'='*50}")

    # Build block-diagonal H0
    print(f"  Building block-diagonal H0...")
    H0, block_starts, sector_dims, sector_labels, total_dim = \
        build_block_diagonal_H(max_pq, gens, f_abc, gammas, E, Omega, verbose=False)
    H0_norm = np.linalg.norm(H0, 'fro')

    print(f"  total_dim = {total_dim}, ||H0||_F = {H0_norm:.4f}")
    print(f"  Sector dims: {sector_dims}")

    # Unperturbed <r>
    evals_0 = eigvalsh(H0)
    r_0 = ratio_statistic(evals_0)
    print(f"  Unperturbed <r> = {r_0:.4f}")

    # Binary search for crossover
    print(f"  Binary search for epsilon_crossover...")
    eps_c, r_c, scan_log = binary_search_crossover(
        H0, total_dim, H0_norm, n_samples, n_binary,
        eps_lo=1e-4, eps_hi=0.5, verbose=True
    )

    t_level_end = time.time()
    dt = t_level_end - t_level_start

    results_N.append(total_dim)
    results_eps_c.append(eps_c)
    results_r_at_c.append(r_c)
    results_scan.append(scan_log)
    results_max_pq.append(max_pq)
    results_n_sectors.append(len(sector_labels))

    print(f"\n  RESULT: max_pq_sum={max_pq}, N={total_dim}, "
          f"epsilon_c={eps_c:.5f}, <r>={r_c:.4f}")
    print(f"  Time: {dt:.1f}s")

# ============================================================
# Step 3: Fit scaling models
# ============================================================
print("\n" + "=" * 70)
print("Step 3: Fit scaling models")
print("=" * 70)

N_arr = np.array(results_N, dtype=float)
eps_arr = np.array(results_eps_c)

print(f"\nData points:")
print(f"  {'max_pq':>7s}  {'N':>7s}  {'eps_c':>10s}")
print(f"  {'-'*30}")
for i in range(len(N_arr)):
    print(f"  {results_max_pq[i]:>7d}  {int(N_arr[i]):>7d}  {eps_arr[i]:>10.5f}")

# Fit each model (use all points with at least 2 for single-parameter fits)
fit_results = {}

# 1. 1/sqrt(N) model
try:
    popt, pcov = curve_fit(model_sqrt_N, N_arr, eps_arr, p0=[1.0])
    residuals = eps_arr - model_sqrt_N(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((eps_arr - np.mean(eps_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['1/sqrt(N)'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res}
    print(f"\n  1/sqrt(N): a = {popt[0]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"\n  1/sqrt(N) fit failed: {e}")

# 2. 1/N model
try:
    popt, pcov = curve_fit(model_inv_N, N_arr, eps_arr, p0=[10.0])
    residuals = eps_arr - model_inv_N(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((eps_arr - np.mean(eps_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['1/N'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res}
    print(f"  1/N:       a = {popt[0]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  1/N fit failed: {e}")

# 3. 1/ln(N) model
try:
    popt, pcov = curve_fit(model_inv_logN, N_arr, eps_arr, p0=[0.1])
    residuals = eps_arr - model_inv_logN(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((eps_arr - np.mean(eps_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['1/ln(N)'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res}
    print(f"  1/ln(N):   a = {popt[0]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  1/ln(N) fit failed: {e}")

# 4. Constant model
try:
    popt, pcov = curve_fit(model_const, N_arr, eps_arr, p0=[0.01])
    residuals = eps_arr - model_const(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((eps_arr - np.mean(eps_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['const'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res}
    print(f"  constant:  a = {popt[0]:.5f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  constant fit failed: {e}")

# 5. General power law: a * N^{-alpha}
try:
    popt, pcov = curve_fit(model_power, N_arr, eps_arr, p0=[1.0, 0.5],
                           bounds=([0, 0], [100, 3]))
    residuals = eps_arr - model_power(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((eps_arr - np.mean(eps_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['N^-alpha'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res}
    print(f"  N^-alpha:  a = {popt[0]:.4f}, alpha = {popt[1]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  N^-alpha fit failed: {e}")

# ============================================================
# Step 4: Model comparison
# ============================================================
print("\n" + "=" * 70)
print("Step 4: Model Comparison")
print("=" * 70)

# AIC-like comparison (with sum of squared residuals as proxy)
# For equal number of data points, lower ss_res wins
# Penalize more parameters (N^-alpha has 2, others have 1)
n_data = len(N_arr)
print(f"\n  {'Model':>12s}  {'R^2':>10s}  {'SS_res':>12s}  {'BIC':>10s}")
print(f"  {'-'*50}")

for name, res in sorted(fit_results.items(), key=lambda x: x[1]['ss_res']):
    k = len(res['params'])  # number of parameters
    ss = res['ss_res']
    # BIC = n*ln(ss/n) + k*ln(n)
    bic = n_data * np.log(ss / n_data + 1e-30) + k * np.log(n_data)
    res['BIC'] = bic
    print(f"  {name:>12s}  {res['R2']:>10.6f}  {ss:>12.2e}  {bic:>10.3f}")

# Best model
best_model = min(fit_results.items(), key=lambda x: x[1]['ss_res'])
print(f"\n  Best fit (lowest SS_res): {best_model[0]}")

# ============================================================
# Step 5: Extrapolation to N -> infinity
# ============================================================
print("\n" + "=" * 70)
print("Step 5: Extrapolation")
print("=" * 70)

N_extrap = np.array([1e4, 1e5, 1e6, 1e8, 1e10, np.inf])
print(f"\n  {'N':>12s}", end="")
for name in ['1/sqrt(N)', '1/N', '1/ln(N)', 'const']:
    print(f"  {name:>12s}", end="")
print()

for N_val in N_extrap:
    if np.isinf(N_val):
        print(f"  {'inf':>12s}", end="")
    else:
        print(f"  {N_val:>12.0e}", end="")
    for name in ['1/sqrt(N)', '1/N', '1/ln(N)', 'const']:
        if name in fit_results:
            p = fit_results[name]['params']
            if name == '1/sqrt(N)':
                val = p[0] / np.sqrt(N_val) if not np.isinf(N_val) else 0
            elif name == '1/N':
                val = p[0] / N_val if not np.isinf(N_val) else 0
            elif name == '1/ln(N)':
                val = p[0] / np.log(N_val) if not np.isinf(N_val) else 0
            elif name == 'const':
                val = p[0]
            print(f"  {val:>12.2e}", end="")
        else:
            print(f"  {'N/A':>12s}", end="")
    print()

# ============================================================
# Step 6: Gate verdict
# ============================================================
print("\n" + "=" * 70)
print("DISSOLUTION-SCALING-44: GATE VERDICT")
print("=" * 70)

# Check if 1/sqrt(N) is the best model
if 'N^-alpha' in fit_results:
    alpha_fit = fit_results['N^-alpha']['params'][1]
    alpha_err = np.sqrt(pcov[1, 1]) if pcov is not None else np.nan
    print(f"\n  Fitted power law: epsilon_c ~ N^{{-{alpha_fit:.3f}}}")

    # Is alpha consistent with 0.5 (1/sqrt(N))?
    if abs(alpha_fit - 0.5) < 0.15:
        verdict = "PASS"
        print(f"  alpha = {alpha_fit:.3f} is consistent with 0.5 (1/sqrt(N))")
    elif alpha_fit < 0.1:
        verdict = "FAIL"
        print(f"  alpha = {alpha_fit:.3f} ~ 0 => effectively constant threshold")
    else:
        verdict = "INFO"
        print(f"  alpha = {alpha_fit:.3f} is intermediate (not clearly 1/sqrt or constant)")
else:
    # Fall back to R^2 comparison
    r2_sqrt = fit_results.get('1/sqrt(N)', {}).get('R2', -1)
    r2_const = fit_results.get('const', {}).get('R2', -1)
    if r2_sqrt > r2_const and r2_sqrt > 0.9:
        verdict = "PASS"
    elif r2_const > r2_sqrt and r2_const > 0.9:
        verdict = "FAIL"
    else:
        verdict = "INFO"

print(f"\n  VERDICT: {verdict}")
print(f"  (PASS = 1/sqrt(N) confirmed, FAIL = constant, INFO = intermediate)")

# Physical interpretation
print(f"\n  Physical interpretation:")
if verdict == "PASS":
    print(f"  epsilon_crossover -> 0 as N -> infinity.")
    print(f"  The spectral triple dissolves under ANY nonzero foam perturbation")
    print(f"  in the thermodynamic limit. Block-diagonal structure is a finite-size")
    print(f"  artifact. The NCG spectral triple is EMERGENT -- it exists only at")
    print(f"  scales where the effective mode count is finite.")
    print(f"  This CONFIRMS W-FOAM-7: spectral triple is emergent, not fundamental.")
elif verdict == "FAIL":
    print(f"  epsilon_crossover -> const as N -> infinity.")
    print(f"  A finite threshold persists. The spectral triple has intrinsic")
    print(f"  robustness against generic perturbations. The block-diagonal theorem")
    print(f"  generalizes to a stability result beyond left-invariance.")
else:
    print(f"  Scaling is intermediate. More data points or larger N needed to")
    print(f"  distinguish 1/sqrt(N) from 1/ln(N) or other slow decay.")

# ============================================================
# Step 7: Save data
# ============================================================
print("\n--- Saving results ---")

save_data = {
    'tau': TAU_FOLD,
    'max_pq_sums': np.array(results_max_pq),
    'N_values': N_arr,
    'epsilon_crossover': eps_arr,
    'r_at_crossover': np.array(results_r_at_c),
    'n_sectors': np.array(results_n_sectors),
    'r_poisson': R_POISSON,
    'r_goe': R_GOE,
    'r_midpoint': R_MIDPOINT,
    'verdict': np.array([verdict]),
}

# Save fit results
for name, res in fit_results.items():
    safe_name = name.replace('/', '_').replace('^', '_').replace('(', '').replace(')', '')
    save_data[f'fit_{safe_name}_params'] = np.array(res['params'])
    save_data[f'fit_{safe_name}_R2'] = np.array([res['R2']])
    save_data[f'fit_{safe_name}_ss_res'] = np.array([res['ss_res']])

# Save scan logs
for i, scan_log in enumerate(results_scan):
    log_arr = np.array([(eps, r, rerr) for eps, r, rerr in scan_log])
    save_data[f'scan_log_pq{results_max_pq[i]}'] = log_arr

np.savez('tier0-computation/s44_dissolution_scaling.npz', **save_data)
print("  Saved: tier0-computation/s44_dissolution_scaling.npz")

# ============================================================
# Step 8: Plot
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.3)

# --- Panel 1: epsilon_c vs N (main result) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(N_arr, eps_arr, 'ko', markersize=10, zorder=5, label='Data')

# Plot fit curves
N_plot = np.logspace(np.log10(N_arr.min() * 0.5), np.log10(N_arr.max() * 5), 200)
colors = {'1/sqrt(N)': 'blue', '1/N': 'green', '1/ln(N)': 'orange', 'const': 'red', 'N^-alpha': 'purple'}
for name, res in fit_results.items():
    p = res['params']
    if name == '1/sqrt(N)':
        y = model_sqrt_N(N_plot, *p)
    elif name == '1/N':
        y = model_inv_N(N_plot, *p)
    elif name == '1/ln(N)':
        y = model_inv_logN(N_plot, *p)
    elif name == 'const':
        y = model_const(N_plot, *p)
    elif name == 'N^-alpha':
        y = model_power(N_plot, *p)
    else:
        continue
    label_str = f"{name}: R²={res['R2']:.3f}"
    if name == 'N^-alpha':
        label_str = f"N^{{-{p[1]:.2f}}}: R²={res['R2']:.3f}"
    ax1.plot(N_plot, y, '-', color=colors.get(name, 'gray'), linewidth=1.5,
             alpha=0.7, label=label_str)

ax1.set_xlabel('N (total Hilbert space dimension)', fontsize=12)
ax1.set_ylabel(r'$\epsilon_c$ (crossover)', fontsize=14)
ax1.set_title(r'Dissolution Threshold vs Mode Count', fontsize=13)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Annotate max_pq_sum values
for i, mpq in enumerate(results_max_pq):
    ax1.annotate(f'pq={mpq}', (N_arr[i], eps_arr[i]),
                 textcoords="offset points", xytext=(10, 5), fontsize=9)

# --- Panel 2: log-log scaling diagnostic ---
ax2 = fig.add_subplot(gs[0, 1])
log_N = np.log10(N_arr)
log_eps = np.log10(eps_arr)
ax2.plot(log_N, log_eps, 'ko', markersize=10, zorder=5)

# Linear fit in log-log space (= power law)
if len(log_N) >= 2:
    coeffs = np.polyfit(log_N, log_eps, 1)
    slope = coeffs[0]
    intercept = coeffs[1]
    ax2.plot(log_N, np.polyval(coeffs, log_N), 'r-', linewidth=2,
             label=f'slope = {slope:.3f} (expect -0.5 for 1/sqrt)')

    # Reference slopes
    x_ref = np.array([log_N.min(), log_N.max()])
    for ref_slope, ref_name, ref_color in [(-0.5, '1/sqrt(N)', 'blue'),
                                             (-1.0, '1/N', 'green'),
                                             (0.0, 'constant', 'gray')]:
        y_ref = ref_slope * (x_ref - log_N[0]) + log_eps[0]
        ax2.plot(x_ref, y_ref, '--', color=ref_color, linewidth=1, alpha=0.5,
                 label=f'slope={ref_slope} ({ref_name})')

ax2.set_xlabel(r'$\log_{10} N$', fontsize=12)
ax2.set_ylabel(r'$\log_{10} \epsilon_c$', fontsize=14)
ax2.set_title('Log-Log Scaling Diagnostic', fontsize=13)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# --- Panel 3: <r> vs epsilon for each truncation level ---
ax3 = fig.add_subplot(gs[1, 0])
colors_pq = plt.cm.viridis(np.linspace(0.1, 0.9, len(results_scan)))

for i, scan_log in enumerate(results_scan):
    log_arr = np.array([(eps, r, rerr) for eps, r, rerr in scan_log])
    log_arr = log_arr[log_arr[:, 0].argsort()]  # sort by epsilon
    ax3.errorbar(log_arr[:, 0], log_arr[:, 1], yerr=log_arr[:, 2],
                 fmt='o-', color=colors_pq[i], capsize=3, linewidth=1.5,
                 markersize=5, label=f'pq={results_max_pq[i]} (N={int(N_arr[i])})')

ax3.axhline(R_POISSON, color='blue', linestyle='--', linewidth=1, label=f'Poisson ({R_POISSON:.3f})')
ax3.axhline(R_GOE, color='red', linestyle='--', linewidth=1, label=f'GOE ({R_GOE:.3f})')
ax3.axhline(R_MIDPOINT, color='gray', linestyle=':', linewidth=1)
ax3.set_xlabel(r'$\epsilon$', fontsize=12)
ax3.set_ylabel(r'$\langle r \rangle$', fontsize=14)
ax3.set_title(r'$\langle r \rangle$ vs $\epsilon$ per truncation', fontsize=13)
ax3.set_xscale('log')
ax3.set_ylim(0.30, 0.62)
ax3.legend(fontsize=8, ncol=2, loc='lower right')
ax3.grid(True, alpha=0.3)

# --- Panel 4: Residual plot ---
ax4 = fig.add_subplot(gs[1, 1])
if 'N^-alpha' in fit_results:
    p = fit_results['N^-alpha']['params']
    eps_pred = model_power(N_arr, *p)
    residuals = (eps_arr - eps_pred) / eps_arr * 100  # percent
    ax4.bar(range(len(N_arr)), residuals, color='steelblue', alpha=0.7)
    ax4.set_xticks(range(len(N_arr)))
    ax4.set_xticklabels([f'pq={m}\nN={int(n)}' for m, n in zip(results_max_pq, N_arr)],
                        fontsize=8)
    ax4.set_ylabel('Residual (%)', fontsize=12)
    ax4.set_title(f'Residuals: $\\epsilon_c = {p[0]:.3f} \\cdot N^{{-{p[1]:.3f}}}$',
                  fontsize=13)
    ax4.axhline(0, color='k', linewidth=0.5)
    ax4.grid(True, alpha=0.3, axis='y')

fig.suptitle(f'DISSOLUTION-SCALING-44: Threshold Scaling at tau={TAU_FOLD}\n'
             f'Verdict: {verdict}',
             fontsize=14, fontweight='bold')

plt.savefig('tier0-computation/s44_dissolution_scaling.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s44_dissolution_scaling.png")

# ============================================================
# Final timing and summary
# ============================================================
t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s ({(t_end - t_start)/60:.1f}min)")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n  Dissolution threshold epsilon_c(N) measured at {len(N_arr)} truncation levels.")
print(f"  N range: [{int(N_arr.min())}, {int(N_arr.max())}]")
print(f"  epsilon_c range: [{eps_arr.min():.5f}, {eps_arr.max():.5f}]")
if 'N^-alpha' in fit_results:
    p = fit_results['N^-alpha']['params']
    print(f"\n  Best power law: epsilon_c = {p[0]:.4f} * N^(-{p[1]:.4f})")
    print(f"  R^2 = {fit_results['N^-alpha']['R2']:.6f}")
print(f"\n  Gate verdict: {verdict}")
print(f"\n  QF-79: epsilon_crossover(N) ~ N^{{-alpha}}")
if 'N^-alpha' in fit_results:
    print(f"         alpha = {fit_results['N^-alpha']['params'][1]:.3f}")
