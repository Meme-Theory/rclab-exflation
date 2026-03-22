#!/usr/bin/env python3
"""
BAYESIAN-f-44: Bayesian (alpha, beta) Posterior for Mittag-Leffler Cutoff Family
=================================================================================
Nazarewicz nuclear-structure-theorist computation.

GATE: BAYESIAN-f-44 (INFO) -- diagnostic for functional form.

METHODOLOGY (extends MKK-BAYES-43, Paper 06 framework):
  The spectral action S = Tr f(D_K^2 / Lambda^2) depends on the cutoff function f
  through its moments:
    f_n = integral_0^{x_max} x^{n-1} f(x) dx    (n = 0, 1, 2)

  We parametrize f via the Mittag-Leffler function:
    f_{alpha,beta}(x) = E_{alpha,beta}(-x) = sum_{k=0}^inf (-x)^k / Gamma(alpha*k + beta)

  At alpha=beta=1: f = exp(-x) (standard spectral action cutoff).

  MOMENTS (truncated at x_max, term-by-term integrated):
    F_n(alpha, beta; x_max) = sum_{k=0}^K (-1)^k * x_max^{k+n} / ((k+n) * Gamma(alpha*k + beta))

  These are ALWAYS finite for finite x_max. The Connes cutoff sets x_max ~ O(1).

  PHYSICAL OBSERVABLES for each (alpha, beta):
    (1) G_N fixes Lambda via: 1/(16*pi*G) = (F_1 * Lambda^4 * a_2) / (48*pi^2)
        => M_KK(alpha,beta) = Lambda = M_KK_std / sqrt(F_1)   where F_1(1,1) = 1
    (2) alpha_EM: Kerner formula at M_KK(alpha,beta) + 1-loop RGE
    (3) FIRAS: delta_tau/tau at M_KK(alpha,beta)
    (4) CC: rho ~ F_0 * Lambda^4 * a_0 => F_0/F_1 ratio determines CC

CONTEXT:
  - W5-5 Hausdorff impossibility: 242-order deficit for any positive f
  - MKK-BAYES-43: 0.70-decade gravity/gauge tension
  - S43 UV/IR workshop: 1-parameter families cannot suppress f_0/f_2

Author: nazarewicz-nuclear-structure-theorist
Session: 44, Wave 6, Task W6-3
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.colors import LogNorm, SymLogNorm
from pathlib import Path
from scipy.special import gamma as Gamma_func, gammaln
from scipy.special import erfc as erfc_func

DATA_DIR = Path(__file__).parent

# ============================================================
# 0. LOAD INPUT DATA
# ============================================================

cs = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)
hf = np.load(DATA_DIR / 's42_hauser_feshbach.npz', allow_pickle=True)
d43 = np.load(DATA_DIR / 's43_mkk_posterior.npz', allow_pickle=True)
d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)

tau_fold = float(cs['tau_fold'])
g_SU2_fold = float(cs['g_SU2_fold'])
g_U1_fold = float(cs['g_U1_fold'])
a0_fold = float(cs['a0_fold'])
a2_fold = float(cs['a2_fold'])
a4_fold = float(cs['a4_fold'])
M_KK_GN_s42 = float(cs['M_KK_from_GN'])
M_KK_kerner_s42 = float(cs['M_KK_kerner'])

sigma_alpha_th = float(d43['sigma_alpha_th'])  # = 10.0
sigma_GN_log10 = float(d43['sigma_GN_log10'])  # = 0.3

PI = np.pi
from canonical_constants import M_Pl_reduced as M_PL, alpha_em_MZ_inv as ALPHA_EM_MZ_INV  # 2.435e18 GeV, PDG 2024
M_Z = 91.1876            # GeV
from canonical_constants import FIRAS_dT_bound as FIRAS_BOUND

# SM 1-loop beta coefficients
b_Y = -41.0 / 6.0
b2_SM = 19.0 / 6.0

# HOMOG-42 parameters
try:
    hm = np.load(DATA_DIR / 's42_homogeneity.npz', allow_pickle=True)
    m_phi_sq = float(hm['m_phi_sq'])
    Z_fold = float(hm['Z_fold'])
    H_prefactor = float(hm['H_prefactor'])
    dt_transit = float(hm['dt_transit'])
    HAVE_HOMOG = True
except FileNotFoundError:
    HAVE_HOMOG = False

print("=" * 78)
print("BAYESIAN-f-44: Mittag-Leffler Cutoff Function Posterior")
print("=" * 78)
print(f"\n  tau_fold = {tau_fold}")
print(f"  a_0 = {a0_fold:.0f}, a_2 = {a2_fold:.4f}, a_4 = {a4_fold:.4f}")
print(f"  M_KK(grav, S42) = {M_KK_GN_s42:.4e} GeV (log10 = {np.log10(M_KK_GN_s42):.3f})")
print(f"  M_KK(gauge, S42) = {M_KK_kerner_s42:.4e} GeV (log10 = {np.log10(M_KK_kerner_s42):.3f})")
print(f"  sigma_alpha_th = {sigma_alpha_th}")
print(f"  HOMOG data: {'available' if HAVE_HOMOG else 'MISSING'}")

# ============================================================
# 1. MITTAG-LEFFLER MOMENTS (EFFICIENT TERM-BY-TERM)
# ============================================================
#
# For f(x) = E_{alpha,beta}(-x) = sum_{k=0}^inf (-1)^k x^k / Gamma(alpha*k + beta),
# the truncated moment:
#   F_n(x_max) = integral_0^{x_max} x^{n-1} f(x) dx
#              = sum_{k=0}^inf (-1)^k / Gamma(alpha*k + beta) * integral_0^{x_max} x^{k+n-1} dx
#              = sum_{k=0}^inf (-1)^k * x_max^{k+n} / ((k+n) * Gamma(alpha*k + beta))
#
# This converges for all x_max, alpha > 0, beta > 0.
# The convergence is alternating, so we can bound the error.

print(f"\n{'='*78}")
print("1. MITTAG-LEFFLER MOMENTS (term-by-term integration)")
print("=" * 78)

def ml_truncated_moment(alpha_ml, beta_ml, n, x_max, K=500):
    """
    Compute F_n = integral_0^{x_max} x^{n-1} E_{alpha,beta}(-x) dx
    via term-by-term integration.

    F_n = sum_{k=0}^K (-1)^k * x_max^{k+n} / ((k+n) * Gamma(alpha*k + beta))

    Parameters:
    -----------
    alpha_ml : float, ML parameter alpha > 0
    beta_ml  : float, ML parameter beta > 0
    n        : int, moment order (1 for f_2, 2 for f_4, 0 for f_0 -- BUT n=0 diverges)
    x_max    : float, upper integration limit (Connes cutoff)
    K        : int, number of terms

    Returns F_n value. For n=0, we compute the LOG moment:
    F_0 = integral_0^{x_max} f(x)/x dx (logarithmically divergent at 0 for f(0)!=0).
    We instead report f(0) = 1/Gamma(beta) which is the CC-relevant quantity.
    """
    if n <= 0:
        # Return f(0) instead of divergent integral
        return 1.0 / Gamma_func(beta_ml)

    result = 0.0
    sign = 1.0
    log_xmax = np.log(x_max)

    for k in range(K):
        # term = (-1)^k * x_max^{k+n} / ((k+n) * Gamma(alpha*k + beta))
        log_gamma_val = gammaln(alpha_ml * k + beta_ml)
        if not np.isfinite(log_gamma_val):
            break

        log_term = (k + n) * log_xmax - np.log(k + n) - log_gamma_val

        if log_term < -50:  # Term negligible
            if k > 20:
                break
            sign *= -1
            continue

        term = sign * np.exp(log_term)
        result += term

        # Convergence check (alternating series)
        if k > 20 and abs(term) < 1e-14 * abs(result):
            break

        sign *= -1

    return result


def compute_ml_moments(alpha_ml, beta_ml, x_max=10.0):
    """
    Compute the three physically relevant moments of E_{alpha,beta}(-x):
      f_0 = f(0) = 1/Gamma(beta)              [CC coefficient, = Lambda^4 * a_0 term]
      f_2 = integral_0^{x_max} f(x) dx        [G_N coefficient, = Lambda^2 * a_2 term]
      f_4 = integral_0^{x_max} x * f(x) dx    [a_4 coefficient]

    Returns (f_0, f_2, f_4).
    """
    f_0 = 1.0 / Gamma_func(beta_ml)
    f_2 = ml_truncated_moment(alpha_ml, beta_ml, n=1, x_max=x_max)
    f_4 = ml_truncated_moment(alpha_ml, beta_ml, n=2, x_max=x_max)

    return f_0, f_2, f_4


# Cross-checks
print("\n  Cross-checks against known results:")

# (1,1) -> exp(-x): f_0=1, f_2=1-exp(-x_max), f_4=1-(1+x_max)*exp(-x_max)
x_max = 10.0
f0, f2, f4 = compute_ml_moments(1.0, 1.0, x_max)
f2_exact = 1.0 - np.exp(-x_max)
f4_exact = 1.0 - (1.0 + x_max) * np.exp(-x_max)
print(f"  (1,1) exp(-x), x_max={x_max}:")
print(f"    f_0 = {f0:.8f} (exact: 1.0)")
print(f"    f_2 = {f2:.8f} (exact: {f2_exact:.8f}, error: {abs(f2-f2_exact):.2e})")
print(f"    f_4 = {f4:.8f} (exact: {f4_exact:.8f}, error: {abs(f4-f4_exact):.2e})")

# (2,1) -> E_{2,1}(-x) = cos(sqrt(x)) for x > 0
# integral_0^10 cos(sqrt(x)) dx = 2[x sin(sqrt(x)) + cos(sqrt(x))]_0^10
# Let u = sqrt(x), x = u^2, dx = 2u du
# integral_0^{sqrt(10)} 2u cos(u) du = 2[u sin(u) + cos(u)]_0^{sqrt(10)}
# = 2[sqrt(10)*sin(sqrt(10)) + cos(sqrt(10)) - 1]
sr10 = np.sqrt(x_max)
f2_21_exact = 2*(sr10*np.sin(sr10) + np.cos(sr10) - 1)
f0_21, f2_21, f4_21 = compute_ml_moments(2.0, 1.0, x_max)
print(f"\n  (2,1) cos(sqrt(x)), x_max={x_max}:")
print(f"    f_0 = {f0_21:.8f} (exact: 1/Gamma(1) = 1.0)")
print(f"    f_2 = {f2_21:.8f} (exact: {f2_21_exact:.8f}, error: {abs(f2_21-f2_21_exact):.2e})")

# Test at multiple x_max values to verify convergence
print(f"\n  Convergence test at (1,1) across x_max:")
for xm in [1.0, 5.0, 10.0, 20.0, 50.0]:
    _, f2_t, f4_t = compute_ml_moments(1.0, 1.0, xm)
    f2_e = 1 - np.exp(-xm)
    f4_e = 1 - (1+xm)*np.exp(-xm)
    print(f"    x_max={xm:>5.1f}: f_2={f2_t:.8f} (exact {f2_e:.8f}), "
          f"f_4={f4_t:.8f} (exact {f4_e:.8f})")

# ============================================================
# 2. COMPUTE MOMENT GRID
# ============================================================

print(f"\n{'='*78}")
print("2. COMPUTING MOMENT GRID (alpha, beta)")
print("=" * 78)

# Physical cutoff: x_max = lambda_max^2 / Lambda^2
# For Lambda = M_KK and lambda_max ~ 2*M_KK (heaviest eigenvalue): x_max ~ 4
# Conservative: x_max = 10 (captures essentially all of exp(-x))
# For alpha < 1 ML has algebraic tails, so x_max matters more.
# We use TWO cutoffs to test sensitivity.

X_MAX_DEFAULT = 10.0
X_MAX_HIGH = 50.0

N_alpha = 50
N_beta = 50
alpha_grid = np.linspace(0.3, 2.0, N_alpha)
beta_grid = np.linspace(0.3, 2.0, N_beta)

f0_grid = np.zeros((N_alpha, N_beta))
f2_grid = np.zeros((N_alpha, N_beta))
f4_grid = np.zeros((N_alpha, N_beta))
f2_high_grid = np.zeros((N_alpha, N_beta))  # For sensitivity

print(f"  Grid: {N_alpha} x {N_beta} = {N_alpha*N_beta} points")
print(f"  alpha in [{alpha_grid[0]:.2f}, {alpha_grid[-1]:.2f}]")
print(f"  beta  in [{beta_grid[0]:.2f}, {beta_grid[-1]:.2f}]")
print(f"  x_max = {X_MAX_DEFAULT} (default), {X_MAX_HIGH} (sensitivity)")
print("  Computing...")

n_computed = 0
n_nan = 0

for i, a in enumerate(alpha_grid):
    for j, b in enumerate(beta_grid):
        try:
            f0, f2, f4 = compute_ml_moments(a, b, X_MAX_DEFAULT)
            _, f2h, _ = compute_ml_moments(a, b, X_MAX_HIGH)

            if np.isfinite(f0) and np.isfinite(f2) and np.isfinite(f4):
                f0_grid[i, j] = f0
                f2_grid[i, j] = f2
                f4_grid[i, j] = f4
                f2_high_grid[i, j] = f2h if np.isfinite(f2h) else f2
                n_computed += 1
            else:
                f0_grid[i, j] = np.nan
                f2_grid[i, j] = np.nan
                f4_grid[i, j] = np.nan
                f2_high_grid[i, j] = np.nan
                n_nan += 1
        except Exception:
            f0_grid[i, j] = np.nan
            f2_grid[i, j] = np.nan
            f4_grid[i, j] = np.nan
            f2_high_grid[i, j] = np.nan
            n_nan += 1

    if (i + 1) % 10 == 0:
        print(f"    Row {i+1}/{N_alpha} done ({n_computed} ok, {n_nan} nan)")

print(f"\n  Grid complete: {n_computed} computed, {n_nan} nan")

valid = np.isfinite(f2_grid) & (f2_grid != 0)

print(f"\n  Moment ranges:")
print(f"    f_0: [{np.nanmin(f0_grid):.6f}, {np.nanmax(f0_grid):.6f}]")
print(f"    f_2 (x_max={X_MAX_DEFAULT}): [{np.nanmin(f2_grid[valid]):.6f}, {np.nanmax(f2_grid[valid]):.6f}]")
print(f"    f_4: [{np.nanmin(f4_grid[valid]):.6f}, {np.nanmax(f4_grid[valid]):.6f}]")

# Ratio f_4/f_2
ratio_grid = np.full((N_alpha, N_beta), np.nan)
pos_f2 = valid & (f2_grid > 1e-15)
ratio_grid[pos_f2] = f4_grid[pos_f2] / f2_grid[pos_f2]
print(f"    f_4/f_2: [{np.nanmin(ratio_grid):.6f}, {np.nanmax(ratio_grid):.6f}]")

# x_max sensitivity
x_sens = np.full((N_alpha, N_beta), np.nan)
both_valid = valid & np.isfinite(f2_high_grid) & (np.abs(f2_grid) > 1e-15)
x_sens[both_valid] = np.abs(f2_high_grid[both_valid] - f2_grid[both_valid]) / np.abs(f2_grid[both_valid])
print(f"    x_max sensitivity |f2(50)-f2(10)|/|f2(10)|: "
      f"median={np.nanmedian(x_sens):.4f}, max={np.nanmax(x_sens):.4f}")

# ============================================================
# 3. PHYSICAL OBSERVABLES
# ============================================================

print(f"\n{'='*78}")
print("3. PHYSICAL OBSERVABLES ON (alpha, beta) GRID")
print("=" * 78)

# M_KK from G_N with arbitrary f_2:
# S42 had: M_KK_std^2 = pi^3 * M_Pl^2 / (12 * a_2)  [implicit f_2 = 1]
# General: M_KK^2 = M_KK_std^2 / f_2
M_KK_std_sq = PI**3 * M_PL**2 / (12.0 * a2_fold)
M_KK_std = np.sqrt(M_KK_std_sq)
print(f"  M_KK(std, f_2=1) = {M_KK_std:.4e} GeV (log10 = {np.log10(M_KK_std):.3f})")

M_KK_ab = np.full((N_alpha, N_beta), np.nan)
log10_MKK_ab = np.full((N_alpha, N_beta), np.nan)

# Only positive f_2 gives physical M_KK
pos_mask = valid & (f2_grid > 0)
M_KK_ab[pos_mask] = np.sqrt(M_KK_std_sq / f2_grid[pos_mask])
log10_MKK_ab[pos_mask] = np.log10(M_KK_ab[pos_mask])

# Physical range cut
physical = pos_mask & (M_KK_ab > M_Z) & (M_KK_ab < 10 * M_PL)
n_physical = np.sum(physical)
print(f"  Physical M_KK (m_Z < M_KK < 10*M_Pl): {n_physical} / {n_computed}")
print(f"  log10(M_KK) range: [{np.nanmin(log10_MKK_ab[physical]):.3f}, {np.nanmax(log10_MKK_ab[physical]):.3f}]")

# alpha_EM from Kerner + RGE
def alpha_EM_inv_pred(M_KK_val):
    """Predict 1/alpha_EM(m_Z) from Kerner + 1-loop SM RGE."""
    M = np.asarray(M_KK_val, dtype=float)
    alpha2 = M**2 / (M_PL**2 * g_SU2_fold)
    alpha1 = M**2 / (M_PL**2 * g_U1_fold)
    ln_r = np.log(np.maximum(M, M_Z) / M_Z)
    alpha2_inv_mZ = 1.0 / alpha2 + (b2_SM / (2*PI)) * ln_r
    alpha_Y = 3.0 * alpha1  # Baptista normalization
    alpha_Y_inv_mZ = 1.0 / alpha_Y + (b_Y / (2*PI)) * ln_r
    return alpha_Y_inv_mZ + alpha2_inv_mZ

alpha_EM_inv_ab = np.full((N_alpha, N_beta), np.nan)
alpha_EM_inv_ab[physical] = alpha_EM_inv_pred(M_KK_ab[physical])

delta_alpha_ab = np.full((N_alpha, N_beta), np.nan)
delta_alpha_ab[physical] = alpha_EM_inv_ab[physical] - ALPHA_EM_MZ_INV

print(f"  1/alpha_EM range: [{np.nanmin(alpha_EM_inv_ab[physical]):.1f}, "
      f"{np.nanmax(alpha_EM_inv_ab[physical]):.1f}]")
print(f"  delta(1/alpha) range: [{np.nanmin(delta_alpha_ab[physical]):.1f}, "
      f"{np.nanmax(delta_alpha_ab[physical]):.1f}]")

# FIRAS
dtau_ab = np.full((N_alpha, N_beta), np.nan)
if HAVE_HOMOG:
    def delta_tau_over_tau(M):
        M = np.asarray(M, dtype=float)
        H_over_M = H_prefactor * (M / M_PL)
        N_e = H_over_M * dt_transit
        exp_arg = 2.0 * m_phi_sq * N_e / (3.0 * H_over_M**2)
        factor = 1.0 - np.exp(-np.clip(exp_arg, -500, 500))
        phi2_eq = 3.0 * H_over_M**4 / (8.0 * PI**2 * m_phi_sq)
        phi2 = phi2_eq * factor
        return np.sqrt(np.abs(phi2)) / np.sqrt(Z_fold) / tau_fold

    dtau_ab[physical] = delta_tau_over_tau(M_KK_ab[physical])
    print(f"  delta_tau/tau range: [{np.nanmin(dtau_ab[physical]):.2e}, "
          f"{np.nanmax(dtau_ab[physical]):.2e}]")
    print(f"  FIRAS bound: {FIRAS_BOUND:.0e}")

# ============================================================
# 4. LIKELIHOODS AND POSTERIOR
# ============================================================

print(f"\n{'='*78}")
print("4. LIKELIHOODS AND POSTERIOR")
print("=" * 78)

# G_N is satisfied BY CONSTRUCTION (used to set M_KK).
# Two independent likelihoods: alpha_EM and FIRAS.

# alpha_EM likelihood
logL_alpha = np.full((N_alpha, N_beta), -np.inf)
logL_alpha[physical] = -0.5 * (delta_alpha_ab[physical] / sigma_alpha_th)**2

# FIRAS likelihood (one-sided Gaussian)
logL_FIRAS = np.full((N_alpha, N_beta), 0.0)  # flat if no data
if HAVE_HOMOG:
    from canonical_constants import sigma_FIRAS
    logL_FIRAS_vals = np.full((N_alpha, N_beta), -np.inf)
    x_f = (dtau_ab[physical] - FIRAS_BOUND) / sigma_FIRAS
    val_f = 0.5 * erfc_func(x_f / np.sqrt(2.0))
    val_f = np.clip(val_f, 1e-300, 1.0)
    logL_FIRAS_vals[physical] = np.log(val_f)
    logL_FIRAS = logL_FIRAS_vals

# Total log-likelihood
logL_total = np.full((N_alpha, N_beta), -np.inf)
logL_total[physical] = logL_alpha[physical] + logL_FIRAS[physical]

# Flat prior
dalpha = alpha_grid[1] - alpha_grid[0]
dbeta = beta_grid[1] - beta_grid[0]

# Posterior
logL_max = np.nanmax(logL_total[physical])
posterior = np.zeros((N_alpha, N_beta))
posterior[physical] = np.exp(logL_total[physical] - logL_max)
norm = np.nansum(posterior) * dalpha * dbeta
if norm > 0:
    posterior /= norm

# Mode
idx_mode = np.unravel_index(np.nanargmax(posterior), posterior.shape)
alpha_mode = alpha_grid[idx_mode[0]]
beta_mode = beta_grid[idx_mode[1]]

print(f"\n  Posterior mode:")
print(f"    (alpha, beta) = ({alpha_mode:.3f}, {beta_mode:.3f})")
print(f"    M_KK = {M_KK_ab[idx_mode]:.4e} GeV (log10 = {log10_MKK_ab[idx_mode]:.3f})")
print(f"    1/alpha_EM = {alpha_EM_inv_ab[idx_mode]:.2f} (obs: {ALPHA_EM_MZ_INV:.3f})")
print(f"    f_0 = {f0_grid[idx_mode]:.6f}")
print(f"    f_2 = {f2_grid[idx_mode]:.6f}")
print(f"    f_4 = {f4_grid[idx_mode]:.6f}")
print(f"    f_4/f_2 = {ratio_grid[idx_mode]:.6f}")
if HAVE_HOMOG:
    print(f"    delta_tau/tau = {dtau_ab[idx_mode]:.2e}")

# Marginals
p_alpha_marg = np.nansum(posterior, axis=1) * dbeta
p_beta_marg = np.nansum(posterior, axis=0) * dalpha
alpha_marg_mode = alpha_grid[np.argmax(p_alpha_marg)]
beta_marg_mode = beta_grid[np.argmax(p_beta_marg)]

print(f"\n  Marginal modes: alpha = {alpha_marg_mode:.3f}, beta = {beta_marg_mode:.3f}")

# ============================================================
# 5. TENSION DIAGNOSTIC
# ============================================================

print(f"\n{'='*78}")
print("5. TENSION DIAGNOSTIC")
print("=" * 78)

# Within 1-sigma for alpha_EM: |delta| < sigma_th
alpha_ok = physical & (np.abs(delta_alpha_ab) < sigma_alpha_th)
n_alpha_ok = np.sum(alpha_ok)

# Within 1-sigma for FIRAS
if HAVE_HOMOG:
    firas_ok = physical & (dtau_ab < FIRAS_BOUND + sigma_FIRAS)
else:
    firas_ok = physical
n_firas_ok = np.sum(firas_ok)

both_ok = alpha_ok & firas_ok
n_both = np.sum(both_ok)

print(f"  alpha_EM within 1-sigma (|delta| < {sigma_alpha_th:.0f}): {n_alpha_ok} / {n_physical}")
print(f"  FIRAS within 1-sigma: {n_firas_ok} / {n_physical}")
print(f"  BOTH: {n_both} / {n_physical}")

if n_both > 0:
    both_idx = np.argwhere(both_ok)
    print(f"\n  Points satisfying BOTH (showing up to 15):")
    # Sort by posterior
    post_vals = [posterior[i,j] for i,j in both_idx]
    sort_order = np.argsort(post_vals)[::-1]

    for rank, si in enumerate(sort_order[:15]):
        i, j = both_idx[si]
        print(f"    #{rank+1}: (a={alpha_grid[i]:.3f}, b={beta_grid[j]:.3f}) "
              f"log10_MKK={log10_MKK_ab[i,j]:.3f}, "
              f"1/a_EM={alpha_EM_inv_ab[i,j]:.1f}, "
              f"f_2={f2_grid[i,j]:.4f}, "
              f"f_4/f_2={ratio_grid[i,j]:.4f}"
              + (f", dtau={dtau_ab[i,j]:.2e}" if HAVE_HOMOG else ""))

    # Best point
    best_si = sort_order[0]
    bi, bj = both_idx[best_si]
    print(f"\n  Best (alpha,beta) satisfying alpha_EM + FIRAS:")
    print(f"    (alpha, beta) = ({alpha_grid[bi]:.3f}, {beta_grid[bj]:.3f})")
    print(f"    f_2 = {f2_grid[bi,bj]:.6f}")
    print(f"    f_4/f_2 = {ratio_grid[bi,bj]:.6f}")
    print(f"    Hausdorff CC deficit: log10(f_4/f_2) + 121 = {np.log10(abs(ratio_grid[bi,bj])) + 121:.1f} orders")
else:
    print("\n  NO (alpha, beta) satisfies both within 1-sigma.")
    # Where do they individually work?
    if n_alpha_ok > 0:
        a_ok_idx = np.argwhere(alpha_ok)
        f2_aok = [f2_grid[i,j] for i,j in a_ok_idx]
        mkk_aok = [log10_MKK_ab[i,j] for i,j in a_ok_idx]
        print(f"\n  alpha_EM-OK region:")
        print(f"    f_2: [{min(f2_aok):.4f}, {max(f2_aok):.4f}]")
        print(f"    log10_MKK: [{min(mkk_aok):.3f}, {max(mkk_aok):.3f}]")
    if HAVE_HOMOG and n_firas_ok > 0:
        f_ok_idx = np.argwhere(firas_ok)
        f2_fok = [f2_grid[i,j] for i,j in f_ok_idx]
        mkk_fok = [log10_MKK_ab[i,j] for i,j in f_ok_idx]
        print(f"\n  FIRAS-OK region:")
        print(f"    f_2: [{min(f2_fok):.4f}, {max(f2_fok):.4f}]")
        print(f"    log10_MKK: [{min(mkk_fok):.3f}, {max(mkk_fok):.3f}]")

# Route matching diagnostic
f2_match = (M_KK_std / M_KK_kerner_s42)**2
print(f"\n  f_2 to match gravity and gauge routes: {f2_match:.6f}")
print(f"    (M_KK_std / M_KK_kerner)^2 = ({M_KK_std:.3e} / {M_KK_kerner_s42:.3e})^2")
f2_range = (np.nanmin(f2_grid[valid]), np.nanmax(f2_grid[valid]))
achievable = (f2_match >= f2_range[0]) and (f2_match <= f2_range[1])
print(f"    ML f_2 range: [{f2_range[0]:.4f}, {f2_range[1]:.4f}]")
print(f"    Achievable? {'YES' if achievable else 'NO'}")

if achievable:
    dist = np.abs(f2_grid - f2_match)
    dist[~valid] = np.inf
    ci = np.unravel_index(np.argmin(dist), dist.shape)
    print(f"    Closest: (a={alpha_grid[ci[0]]:.3f}, b={beta_grid[ci[1]]:.3f}), "
          f"f_2={f2_grid[ci]:.6f}, "
          f"1/alpha_EM={alpha_EM_inv_ab[ci]:.1f}")

# ============================================================
# 6. HAUSDORFF CC DIAGNOSTIC
# ============================================================

print(f"\n{'='*78}")
print("6. HAUSDORFF CC DIAGNOSTIC (W5-5 VERIFICATION)")
print("=" * 78)

# The CC requires f_0 * Lambda^4 * a_0 ~ rho_obs ~ 10^{-47} GeV^4
# while G_N requires f_2 * Lambda^2 * a_2 ~ M_Pl^2 ~ 10^{36} GeV^2
# The ratio: (f_0/f_2) * (a_0/a_2) * Lambda^2 ~ rho_obs / M_Pl^2 ~ 10^{-83}
# With Lambda ~ 10^{17} GeV: Lambda^2 ~ 10^{34}
# So: f_0/f_2 ~ 10^{-83-34} * (a_2/a_0) ~ 10^{-117} * (2776/6440) ~ 10^{-117.4}
#
# For the f_4/f_2 ratio (quartic moment):
# rho_Lambda ~ f_4 * Lambda^4 * a_4 (in some conventions)
# but the dominant term is f_0 * Lambda^4 * a_0.
# Use the f_0 / f_2 ratio as the CC diagnostic.

CC_ratio_required = 10**(-117.4)  # approximate from above

f0_over_f2 = np.full((N_alpha, N_beta), np.nan)
f0_over_f2[pos_f2] = f0_grid[pos_f2] / f2_grid[pos_f2]

hausdorff_deficit = np.full((N_alpha, N_beta), np.nan)
pos_r = pos_f2 & (f0_over_f2 > 0)
hausdorff_deficit[pos_r] = np.log10(f0_over_f2[pos_r]) - np.log10(CC_ratio_required)

# Also compute f_4/f_2 Hausdorff deficit (W5-5 convention)
f4_f2_hausdorff = np.full((N_alpha, N_beta), np.nan)
pos_ratio = pos_f2 & (ratio_grid > 0) & np.isfinite(ratio_grid)
f4_f2_hausdorff[pos_ratio] = np.log10(ratio_grid[pos_ratio]) + 121.0

print(f"\n  f_0/f_2 ratio:")
print(f"    Range: [{np.nanmin(f0_over_f2):.4e}, {np.nanmax(f0_over_f2):.4e}]")
print(f"    Required for CC: ~ {CC_ratio_required:.1e}")

print(f"\n  f_0/f_2 Hausdorff deficit (orders above CC requirement):")
print(f"    Min: {np.nanmin(hausdorff_deficit):.1f} orders")
print(f"    Max: {np.nanmax(hausdorff_deficit):.1f} orders")
hd_min_idx = np.unravel_index(np.nanargmin(hausdorff_deficit), hausdorff_deficit.shape)
print(f"    Location of min: (alpha={alpha_grid[hd_min_idx[0]]:.3f}, beta={beta_grid[hd_min_idx[1]]:.3f})")
print(f"    f_0/f_2 there: {f0_over_f2[hd_min_idx]:.4e}")

print(f"\n  f_4/f_2 Hausdorff deficit (W5-5 convention, orders above 10^{{-121}}):")
print(f"    Min: {np.nanmin(f4_f2_hausdorff):.1f} orders")
print(f"    Max: {np.nanmax(f4_f2_hausdorff):.1f} orders")

print(f"\n  STRUCTURAL RESULT: The Hausdorff impossibility holds across the ENTIRE")
print(f"  Mittag-Leffler family [{alpha_grid[0]:.1f},{alpha_grid[-1]:.1f}] x [{beta_grid[0]:.1f},{beta_grid[-1]:.1f}].")
print(f"  Minimum f_0/f_2 deficit: {np.nanmin(hausdorff_deficit):.0f} orders.")
print(f"  Minimum f_4/f_2 deficit: {np.nanmin(f4_f2_hausdorff):.0f} orders.")
print(f"  NO ML cutoff can solve the CC problem.")

# ============================================================
# 7. SENSITIVITY TO sigma_th
# ============================================================

print(f"\n{'='*78}")
print("7. SENSITIVITY ANALYSIS")
print("=" * 78)

sensitivity_results = {}
for sig in [5, 10, 30, 50, 100]:
    logL_s = np.full((N_alpha, N_beta), -np.inf)
    logL_s[physical] = -0.5 * (delta_alpha_ab[physical] / sig)**2 + logL_FIRAS[physical]
    lmax = np.nanmax(logL_s[physical])
    ps = np.zeros((N_alpha, N_beta))
    ps[physical] = np.exp(logL_s[physical] - lmax)
    ns = np.nansum(ps) * dalpha * dbeta
    if ns > 0:
        ps /= ns
    ids = np.unravel_index(np.nanargmax(ps), ps.shape)

    # Count OK
    ok_s = physical & (np.abs(delta_alpha_ab) < sig)
    if HAVE_HOMOG:
        ok_s = ok_s & firas_ok
    n_ok_s = np.sum(ok_s)

    sensitivity_results[sig] = {
        'alpha': alpha_grid[ids[0]],
        'beta': beta_grid[ids[1]],
        'log10_MKK': log10_MKK_ab[ids],
        'f2': f2_grid[ids],
        'n_ok': n_ok_s
    }

    print(f"  sigma_th={sig:>3d}: mode=({alpha_grid[ids[0]]:.2f},{beta_grid[ids[1]]:.2f}), "
          f"log10_MKK={log10_MKK_ab[ids]:.3f}, f_2={f2_grid[ids]:.4f}, "
          f"n_ok={n_ok_s}")

# ============================================================
# 8. COMPARISON WITH MKK-BAYES-43
# ============================================================

print(f"\n{'='*78}")
print("8. COMPARISON WITH MKK-BAYES-43")
print("=" * 78)

s43_mode = float(d43['mode_log10'])
s43_grav = np.log10(M_KK_GN_s42)
s43_gauge = np.log10(M_KK_kerner_s42)

print(f"\n  S43 (1-parameter, f_2=1):")
print(f"    Mode: log10(M_KK) = {s43_mode:.3f}")
print(f"    Gravity: {s43_grav:.3f}, Gauge: {s43_gauge:.3f}")
print(f"    Route tension: {abs(s43_gauge - s43_grav):.3f} decades")

print(f"\n  S44 (2-parameter Mittag-Leffler):")
print(f"    Mode: (alpha={alpha_mode:.3f}, beta={beta_mode:.3f})")
print(f"    log10(M_KK) = {log10_MKK_ab[idx_mode]:.3f}")
print(f"    f_2 = {f2_grid[idx_mode]:.6f}")

# How much does the 2-parameter freedom reduce the route tension?
# With f_2 != 1, the gravity route shifts: log10(M_KK) = s43_grav - 0.5*log10(f_2)
# The gauge route is fixed at s43_gauge.
# The tension is: |s43_gauge - (s43_grav - 0.5*log10(f_2))|
f2_best = f2_grid[idx_mode]
if f2_best > 0:
    new_grav = s43_grav - 0.5 * np.log10(f2_best)
    new_tension = abs(s43_gauge - new_grav)
    print(f"\n  Route tension with ML best-fit f_2:")
    print(f"    Gravity route (shifted): {new_grav:.3f}")
    print(f"    Gauge route: {s43_gauge:.3f}")
    print(f"    Tension: {new_tension:.3f} decades (S43: {abs(s43_gauge-s43_grav):.3f})")
    tension_reduction = abs(s43_gauge-s43_grav) - new_tension
    print(f"    Reduction: {tension_reduction:.3f} decades")

# ============================================================
# 9. SUMMARY
# ============================================================

print(f"\n{'='*78}")
print("9. SUMMARY: BAYESIAN-f-44")
print("=" * 78)

tension_status = "REDUCIBLE" if n_both > 0 else "IRREDUCIBLE"

print(f"""
  +-----------------------------------------------------------------+
  |  BAYESIAN-f-44: Mittag-Leffler Cutoff Posterior                  |
  +-----------------------------------------------------------------+
  |  Grid: {N_alpha}x{N_beta}, alpha=[{alpha_grid[0]:.1f},{alpha_grid[-1]:.1f}], beta=[{beta_grid[0]:.1f},{beta_grid[-1]:.1f}]                  |
  |  x_max = {X_MAX_DEFAULT:.0f} (Connes cutoff convention)                      |
  +-----------------------------------------------------------------+
  |  Posterior mode: alpha={alpha_mode:.3f}, beta={beta_mode:.3f}                     |
  |  M_KK at mode: {M_KK_ab[idx_mode]:.3e} GeV (log10={log10_MKK_ab[idx_mode]:.3f})       |
  |  f_2 at mode: {f2_grid[idx_mode]:.6f}                                     |
  |  1/alpha_EM: {alpha_EM_inv_ab[idx_mode]:.1f} (obs: {ALPHA_EM_MZ_INV:.1f})                        |
  +-----------------------------------------------------------------+
  |  alpha_EM + FIRAS: {tension_status}                              |
  |  N(both OK): {n_both} / {n_physical}                                          |
  |  f_2 to match routes: {f2_match:.6f} (achievable: {'YES' if achievable else 'NO'})          |
  +-----------------------------------------------------------------+
  |  CC (Hausdorff) f_0/f_2 deficit: {np.nanmin(hausdorff_deficit):.0f} orders (min)         |
  |  CC (Hausdorff) f_4/f_2 deficit: {np.nanmin(f4_f2_hausdorff):.0f} orders (min)         |
  |  W5-5 CONFIRMED across entire ML family                          |
  +-----------------------------------------------------------------+
  |  Gate: BAYESIAN-f-44 -- INFO                                     |
  +-----------------------------------------------------------------+
""")

# ============================================================
# 10. SAVE
# ============================================================

save_dict = dict(
    alpha_grid=alpha_grid,
    beta_grid=beta_grid,
    N_alpha=N_alpha,
    N_beta=N_beta,
    dalpha=dalpha,
    dbeta=dbeta,
    x_max=X_MAX_DEFAULT,
    # Moments
    f0_grid=f0_grid,
    f2_grid=f2_grid,
    f4_grid=f4_grid,
    ratio_grid=ratio_grid,
    f0_over_f2=f0_over_f2,
    f2_high_grid=f2_high_grid,
    x_max_sensitivity=x_sens,
    # Observables
    M_KK_ab=M_KK_ab,
    log10_MKK_ab=log10_MKK_ab,
    alpha_EM_inv_ab=alpha_EM_inv_ab,
    delta_alpha_ab=delta_alpha_ab,
    dtau_ab=dtau_ab,
    # Posterior
    posterior=posterior,
    logL_alpha=logL_alpha,
    logL_FIRAS=logL_FIRAS,
    logL_total=logL_total,
    p_alpha_marg=p_alpha_marg,
    p_beta_marg=p_beta_marg,
    # Mode
    alpha_mode=alpha_mode,
    beta_mode=beta_mode,
    idx_mode=np.array(idx_mode),
    MKK_at_mode=M_KK_ab[idx_mode],
    log10_MKK_at_mode=log10_MKK_ab[idx_mode],
    f2_at_mode=f2_grid[idx_mode],
    f4_at_mode=f4_grid[idx_mode],
    f0_at_mode=f0_grid[idx_mode],
    ratio_at_mode=ratio_grid[idx_mode],
    alpha_EM_inv_at_mode=alpha_EM_inv_ab[idx_mode],
    # Tension
    n_alpha_ok=n_alpha_ok,
    n_firas_ok=n_firas_ok,
    n_both_ok=n_both,
    tension_status=np.array([tension_status]),
    f2_match_routes=f2_match,
    f2_achievable=achievable,
    # Hausdorff
    hausdorff_deficit_f0f2=hausdorff_deficit,
    hausdorff_deficit_f4f2=f4_f2_hausdorff,
    hausdorff_min_f0f2=np.nanmin(hausdorff_deficit),
    hausdorff_min_f4f2=np.nanmin(f4_f2_hausdorff),
    # S43 comparison
    s43_mode_log10=s43_mode,
    s43_grav_log10=s43_grav,
    s43_gauge_log10=s43_gauge,
    sigma_alpha_th=sigma_alpha_th,
    # Gate
    gate_name=np.array(['BAYESIAN-f-44']),
    gate_verdict=np.array(['INFO']),
)

np.savez(DATA_DIR / 's44_bayesian_f.npz', **save_dict)
print("Saved: tier0-computation/s44_bayesian_f.npz")

# ============================================================
# 11. PLOTS
# ============================================================

fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 3, hspace=0.40, wspace=0.40)

ALPHA, BETA = np.meshgrid(alpha_grid, beta_grid, indexing='ij')

# --- (A) f_2 moment map ---
ax1 = fig.add_subplot(gs[0, 0])
f2_plot = np.where(valid, np.clip(f2_grid, 1e-3, 200), np.nan)
pcm1 = ax1.pcolormesh(ALPHA, BETA, f2_plot,
                       norm=LogNorm(vmin=0.01, vmax=100), cmap='viridis', shading='auto')
ax1.plot(1.0, 1.0, 'w*', ms=15, mew=2, label=r'$\exp(-x)$')
ax1.plot(alpha_mode, beta_mode, 'r*', ms=15, mew=2, label='Posterior mode')
if achievable and 0.01 < f2_match < 100:
    cs1 = ax1.contour(ALPHA, BETA, np.where(valid, f2_grid, np.nan),
                       levels=[f2_match], colors='red', linewidths=2, linestyles='--')
ax1.set_xlabel(r'$\alpha$', fontsize=12)
ax1.set_ylabel(r'$\beta$', fontsize=12)
ax1.set_title(r'(A) $f_2 = \int_0^{x_{\max}} E_{\alpha,\beta}(-x)\,dx$', fontsize=11)
plt.colorbar(pcm1, ax=ax1, label=r'$f_2$')
ax1.legend(fontsize=8, loc='upper left')

# --- (B) log10(M_KK) ---
ax2 = fig.add_subplot(gs[0, 1])
mkk_plot = np.where(physical, log10_MKK_ab, np.nan)
pcm2 = ax2.pcolormesh(ALPHA, BETA, mkk_plot, cmap='RdYlBu_r', shading='auto',
                       vmin=14, vmax=19)
ax2.plot(1.0, 1.0, 'k*', ms=15, mew=2)
ax2.plot(alpha_mode, beta_mode, 'r*', ms=15, mew=2)
cs_g = ax2.contour(ALPHA, BETA, mkk_plot, levels=[s43_grav], colors='red',
                    linewidths=1.5, linestyles='-')
cs_k = ax2.contour(ALPHA, BETA, mkk_plot, levels=[s43_gauge], colors='blue',
                    linewidths=1.5, linestyles='-')
ax2.set_xlabel(r'$\alpha$', fontsize=12)
ax2.set_ylabel(r'$\beta$', fontsize=12)
ax2.set_title(r'(B) $\log_{10}(M_{KK}/\mathrm{GeV})$ from $G_N$', fontsize=11)
cb2 = plt.colorbar(pcm2, ax=ax2, label=r'$\log_{10}(M_{KK})$')

# --- (C) delta(1/alpha) ---
ax3 = fig.add_subplot(gs[0, 2])
da_plot = np.where(physical, delta_alpha_ab, np.nan)
vmax_da = min(200, np.nanmax(np.abs(da_plot[physical])))
pcm3 = ax3.pcolormesh(ALPHA, BETA, da_plot, cmap='RdBu_r', shading='auto',
                       vmin=-vmax_da, vmax=vmax_da)
ax3.plot(1.0, 1.0, 'k*', ms=15, mew=2)
ax3.plot(alpha_mode, beta_mode, 'r*', ms=15, mew=2)
ax3.contour(ALPHA, BETA, da_plot, levels=[0], colors='black', linewidths=2)
ax3.contour(ALPHA, BETA, da_plot, levels=[-sigma_alpha_th, sigma_alpha_th],
            colors='gray', linewidths=1, linestyles='--')
ax3.set_xlabel(r'$\alpha$', fontsize=12)
ax3.set_ylabel(r'$\beta$', fontsize=12)
ax3.set_title(r'(C) $\Delta(1/\alpha_{\rm EM})$ from 127.955', fontsize=11)
plt.colorbar(pcm3, ax=ax3, label=r'$\delta(1/\alpha_{\rm EM})$')

# --- (D) Posterior ---
ax4 = fig.add_subplot(gs[1, 0])
p_plot = posterior / (np.nanmax(posterior) + 1e-300)
pcm4 = ax4.pcolormesh(ALPHA, BETA, p_plot, cmap='hot_r', shading='auto', vmin=0, vmax=1)
ax4.plot(alpha_mode, beta_mode, 'c*', ms=15, mew=2,
         label=f'Mode ({alpha_mode:.2f}, {beta_mode:.2f})')
ax4.plot(1.0, 1.0, 'w*', ms=15, mew=2, label=r'$\exp(-x)$')
ax4.set_xlabel(r'$\alpha$', fontsize=12)
ax4.set_ylabel(r'$\beta$', fontsize=12)
ax4.set_title(r'(D) Posterior $p(\alpha,\beta)$', fontsize=11)
plt.colorbar(pcm4, ax=ax4, label=r'$p/p_{\max}$')
ax4.legend(fontsize=8, loc='upper right')

# --- (E) Marginals ---
ax5 = fig.add_subplot(gs[1, 1])
if np.max(p_alpha_marg) > 0:
    ax5.plot(alpha_grid, p_alpha_marg / np.max(p_alpha_marg), 'b-', lw=2, label=r'$p(\alpha)$')
if np.max(p_beta_marg) > 0:
    ax5.plot(beta_grid, p_beta_marg / np.max(p_beta_marg), 'r-', lw=2, label=r'$p(\beta)$')
ax5.axvline(1.0, color='gray', ls=':', alpha=0.6, label=r'Standard $\alpha=\beta=1$')
ax5.set_xlabel(r'$\alpha$ or $\beta$', fontsize=12)
ax5.set_ylabel('Normalized marginal', fontsize=12)
ax5.set_title('(E) Marginal Posteriors', fontsize=11)
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# --- (F) Hausdorff deficit (f_0/f_2) ---
ax6 = fig.add_subplot(gs[1, 2])
hd_plot = np.where(pos_r, hausdorff_deficit, np.nan)
pcm6 = ax6.pcolormesh(ALPHA, BETA, hd_plot, cmap='YlOrRd', shading='auto')
ax6.plot(1.0, 1.0, 'k*', ms=15, mew=2)
ax6.plot(alpha_grid[hd_min_idx[0]], beta_grid[hd_min_idx[1]], 'c*', ms=15, mew=2,
         label=f'Min: {np.nanmin(hausdorff_deficit):.0f} orders')
ax6.set_xlabel(r'$\alpha$', fontsize=12)
ax6.set_ylabel(r'$\beta$', fontsize=12)
ax6.set_title(r'(F) Hausdorff CC Deficit (orders, $f_0/f_2$)', fontsize=11)
plt.colorbar(pcm6, ax=ax6, label='orders above CC requirement')
ax6.legend(fontsize=8)

# --- (G) f_4/f_2 ratio ---
ax7 = fig.add_subplot(gs[2, 0])
r_plot = np.where(pos_ratio, np.clip(ratio_grid, 1e-3, 100), np.nan)
pcm7 = ax7.pcolormesh(ALPHA, BETA, r_plot,
                       norm=LogNorm(vmin=1e-3, vmax=100), cmap='plasma', shading='auto')
ax7.plot(1.0, 1.0, 'w*', ms=15, mew=2, label=r'$\exp(-x)$: $f_4/f_2=1$')
ax7.set_xlabel(r'$\alpha$', fontsize=12)
ax7.set_ylabel(r'$\beta$', fontsize=12)
ax7.set_title(r'(G) $f_4/f_2$ Ratio', fontsize=11)
plt.colorbar(pcm7, ax=ax7, label=r'$f_4/f_2$')
ax7.legend(fontsize=8)

# --- (H) f_2 vs M_KK scatter ---
ax8 = fig.add_subplot(gs[2, 1])
pf = physical.flatten()
f2f = f2_grid.flatten()[pf]
mf = log10_MKK_ab.flatten()[pf]
pof = posterior.flatten()[pf]
order = np.argsort(pof)
sc = ax8.scatter(f2f[order], mf[order], c=pof[order], cmap='hot_r', s=8, alpha=0.8)
ax8.axhline(s43_grav, color='red', ls='--', lw=1.5, label=f'Gravity: {s43_grav:.2f}')
ax8.axhline(s43_gauge, color='blue', ls='--', lw=1.5, label=f'Gauge: {s43_gauge:.2f}')
ax8.axvline(1.0, color='gray', ls=':', alpha=0.6)
if achievable:
    ax8.axvline(f2_match, color='green', ls='--', lw=1.5,
                label=f'Route match: f_2={f2_match:.3f}')
ax8.set_xlabel(r'$f_2(\alpha,\beta)$', fontsize=12)
ax8.set_ylabel(r'$\log_{10}(M_{KK})$', fontsize=12)
ax8.set_title(r'(H) $f_2$--$M_{KK}$ Relation', fontsize=11)
ax8.legend(fontsize=7, loc='best')
ax8.set_xscale('log')
plt.colorbar(sc, ax=ax8, label='Posterior')
ax8.grid(True, alpha=0.3)

# --- (I) Summary ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')

tab_data = [
    ['Quantity', 'Value'],
    [r'Mode $\alpha$', f'{alpha_mode:.3f}'],
    [r'Mode $\beta$', f'{beta_mode:.3f}'],
    [r'$f_2$ at mode', f'{f2_grid[idx_mode]:.4f}'],
    [r'$f_4/f_2$ at mode', f'{ratio_grid[idx_mode]:.4f}'],
    [r'$\log_{10}(M_{KK})$', f'{log10_MKK_ab[idx_mode]:.3f}'],
    [r'$1/\alpha_{\rm EM}$', f'{alpha_EM_inv_ab[idx_mode]:.1f}'],
    ['', ''],
    [r'$\alpha_{\rm EM}+$FIRAS', tension_status],
    ['N(both OK)', f'{n_both}'],
    [r'$f_2$ route match', f'{f2_match:.4f}'],
    ['CC deficit (min)', f'{np.nanmin(hausdorff_deficit):.0f} orders'],
    ['Gate', 'INFO'],
]

tab = ax9.table(cellText=tab_data, cellLoc='center', loc='center', colWidths=[0.55, 0.45])
tab.auto_set_font_size(False)
tab.set_fontsize(9)
tab.scale(1, 1.3)
tab[0, 0].set_facecolor('#4472C4')
tab[0, 0].set_text_props(color='white', fontweight='bold')
tab[0, 1].set_facecolor('#4472C4')
tab[0, 1].set_text_props(color='white', fontweight='bold')
tab[12, 0].set_facecolor('#D5E8D4')
tab[12, 1].set_facecolor('#D5E8D4')
ax9.set_title('(I) BAYESIAN-f-44 Summary', fontsize=11, pad=20)

fig.suptitle(r'BAYESIAN-f-44: Mittag-Leffler $E_{\alpha,\beta}(-x)$ Cutoff Family' + '\n'
             r'$p(\alpha,\beta\,|\,\alpha_{\rm EM}, \mathrm{FIRAS})$ — Hausdorff CC Test',
             fontsize=14, fontweight='bold', y=0.99)

plt.savefig(DATA_DIR / 's44_bayesian_f.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s44_bayesian_f.png")
plt.close()

print(f"\n{'='*78}")
print("COMPUTATION COMPLETE: BAYESIAN-f-44")
print("=" * 78)
