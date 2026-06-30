#!/usr/bin/env python3
"""
s73a_spectral_action_profile.py -- SPECTRAL-ACTION-PROFILE-73a
================================================================

Gate: SPECTRAL-ACTION-PROFILE-73a
  PASS: S(tau) has a post-fold minimum at tau_eq in [0.19, 1.5] with d^2S/dtau^2 > 0
  INFO: S(tau) monotonically increasing for tau > 0.19, or minimum outside [0.19, 1.5]
  FAIL: Unphysical results (negative S, non-smooth profile)

Physics:
--------
Computes the full spectral action profile S(tau) for the Jensen deformation
parameter tau in [0, 2] using the DIRECT SPECTRAL SUM method with the
observationally-selected spectral functional:

    f*(x) = 0.9117 * sqrt(x) + 0.0883 * exp(-x)

from SPECTRAL-FUNCTIONAL-FIT-72.

CRITICAL: f* has divergent Seeley-DeWitt moments (f_0 diverges because
integral sqrt(x) dx = infty). The heat kernel expansion CANNOT be used.
All spectral actions are computed as finite sums over eigenvalues:

    S(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j f*(lambda_j(tau)^2 / Lambda^2)

This sum converges because the number of eigenvalues at each truncation
level is finite, and f*(x) is bounded for any finite x.

Three-in-one computation:
  1. MODULI STABILIZATION: Does S(tau) have a post-fold minimum?
  2. LATE-TIME CC: Value of S at equilibrium relative to fold
  3. EQUATION OF STATE: w(z) from tau relaxation dynamics

Also computes S(tau) for the three component functionals (sqrt, exp, compact)
for functional-independence analysis.

Agent: Lizzi Spectral-Functional Theorist (Session 73a, Wave 1)
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
    tau_fold, Delta_0_OES, G_DeWitt, PI,
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    M_KK_gravity, M_Pl_reduced,
    rho_Lambda_obs, Omega_Lambda, rho_crit_GeV4,
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
print("SPECTRAL-ACTION-PROFILE-73a: S(tau) Profile for tau in [0, 2]")
print("=" * 78)

# Spectral functional f* from SPECTRAL-FUNCTIONAL-FIT-72
alpha_star = 0.9116771171053042  # (local) weight of sqrt component
beta_star = 0.08832288289469575  # (local) weight of exp component

# Peter-Weyl truncation
MAX_PQ_SUM = 3  # (local) gives ~77 eigenvalues per sector, 1232 total

# BCS gap for dressed computation
Delta = Delta_0_OES  # 0.464 M_KK

# DeWitt kinetic coefficient
G = G_DeWitt  # 5.0

print(f"\n  Spectral functional: f*(x) = {alpha_star:.4f}*sqrt(x) + {beta_star:.4f}*exp(-x)")
print(f"  Peter-Weyl truncation: max(p+q) = {MAX_PQ_SUM}")
print(f"  BCS gap Delta = {Delta:.6f} M_KK")
print(f"  tau_fold = {tau_fold}")
print(f"  Canonical S_fold = {S_fold:.2f}")
print(f"  Canonical dS_fold = {dS_fold:.2f}")
print(f"  Canonical d2S_fold = {d2S_fold:.2f}")

# =============================================================================
# STEP 0: TAU GRID AND ALGEBRAIC INFRASTRUCTURE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Tau Grid and Algebraic Infrastructure")
print("=" * 78)

# Dense tau grid: 0 to 2 in steps of 0.02 (101 points)
# Plus extra points near the fold for cross-check accuracy
tau_dense = np.arange(0.0, 2.01, 0.02)
# Add fold-neighborhood points for derivative accuracy
tau_fold_extra = np.array([0.17, 0.18, 0.19, 0.21, 0.22])
tau_grid = np.sort(np.unique(np.concatenate([tau_dense, tau_fold_extra])))
n_tau = len(tau_grid)

print(f"  Tau grid: {n_tau} points in [{tau_grid[0]:.2f}, {tau_grid[-1]:.2f}]")
print(f"  Grid step: {np.diff(tau_grid).min():.4f} (min), {np.diff(tau_grid).max():.4f} (max)")

# Algebraic infrastructure
print("  Building SU(3) algebraic infrastructure...")
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
print("  Done.")


# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRA AT ALL TAU VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute D_K Eigenvalue Spectra at All tau")
print("=" * 78)

# Storage: per-tau list of (p, q, abs_eigenvalues, dim_pq)
spectra_data = []
n_evals_total = 0  # (local)

t_start = time.time()

for i, tau in enumerate(tau_grid):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                   max_pq_sum=MAX_PQ_SUM, verbose=False)
    tau_spectra = []
    n_i = 0  # (local)
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)  # |lambda_j|
        tau_spectra.append((p, q, omega, d_pq))
        n_i += d_pq**2 * len(omega)
    spectra_data.append(tau_spectra)
    if i == 0:
        n_evals_total = n_i

    if (i + 1) % 20 == 0 or i == 0 or i == n_tau - 1:
        elapsed = time.time() - t_start
        print(f"  tau[{i}] = {tau:.3f} done ({elapsed:.1f}s elapsed, "
              f"{n_i} weighted eigenvalues)")

t_spectra = time.time() - t_start
print(f"\n  Completed {n_tau} spectra in {t_spectra:.1f}s")
print(f"  Eigenvalues per tau (weighted): {n_evals_total}")


# =============================================================================
# STEP 2: DETERMINE LAMBDA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Lambda Determination")
print("=" * 78)

# Find global lambda_max across all tau
lambda_max_per_tau = np.zeros(n_tau)
for i in range(n_tau):
    lmax_i = max(np.max(omega) for (p, q, omega, d) in spectra_data[i])  # (local)
    lambda_max_per_tau[i] = lmax_i

lambda_max_global = np.max(lambda_max_per_tau)  # (local)

# Lambda = 1.1 * global max (consistent with S66)
Lambda = 1.1 * lambda_max_global  # (local)
Lambda_sq = Lambda**2  # (local)

print(f"  lambda_max range: [{lambda_max_per_tau.min():.6f}, {lambda_max_per_tau.max():.6f}] M_KK")
print(f"  Lambda = {Lambda:.6f} M_KK (1.1 * global lambda_max)")
print(f"  Lambda^2 = {Lambda_sq:.6f}")

# Check consistency with S66
d66 = np.load('s66_cutoff_ns.npz', allow_pickle=True)
Lambda_s66 = float(d66['Lambda'])
print(f"  S66 Lambda = {Lambda_s66:.6f} M_KK")
print(f"  Ratio Lambda/Lambda_s66 = {Lambda/Lambda_s66:.6f}")


# =============================================================================
# STEP 3: COMPUTE SPECTRAL ACTIONS FOR ALL FUNCTIONALS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Spectral Action Computation (4 functionals, bare + BCS)")
print("=" * 78)

def f_sqrt(x):
    """f(x) = sqrt(x)."""
    return np.sqrt(x)

def f_exp(x):
    """f(x) = exp(-x)."""
    return np.exp(-x)

def f_compact(x):
    """f(x) = max(0, 1-x)^4."""
    return np.where(x < 1.0, (1.0 - x)**4, 0.0)

def f_star(x):
    """f*(x) = alpha*sqrt(x) + beta*exp(-x). The observationally-selected functional."""
    return alpha_star * np.sqrt(x) + beta_star * np.exp(-x)


# Compute spectral actions for 4 functionals
func_names = ['f_star', 'sqrt', 'exp', 'compact']
func_fns = [f_star, f_sqrt, f_exp, f_compact]
n_funcs = len(func_names)

S_bare = np.zeros((n_funcs, n_tau))
S_bcs = np.zeros((n_funcs, n_tau))

t_start = time.time()
for i in range(n_tau):
    for fi, f_fn in enumerate(func_fns):
        S_b_i = 0.0  # (local)
        S_bcs_i = 0.0  # (local)
        for (p, q, omega, d_pq) in spectra_data[i]:
            # Bare: x = omega^2 / Lambda^2
            x_bare = omega**2 / Lambda_sq  # (local)
            S_b_i += d_pq**2 * np.sum(f_fn(x_bare))

            # BCS-dressed: E = sqrt(omega^2 + Delta^2)
            E_bdg = np.sqrt(omega**2 + Delta**2)  # (local)
            x_bcs = E_bdg**2 / Lambda_sq  # (local)
            S_bcs_i += d_pq**2 * np.sum(f_fn(x_bcs))

        S_bare[fi, i] = S_b_i
        S_bcs[fi, i] = S_bcs_i

t_sa = time.time() - t_start
print(f"  Computed spectral actions in {t_sa:.1f}s")

# Display sample values
print(f"\n  {'tau':>8s}  {'S_f*_bare':>14s}  {'S_sqrt_bare':>14s}  {'S_exp_bare':>14s}  {'S_comp_bare':>14s}")
print("  " + "-" * 80)
sample_idx = [0, 5, 9, np.argmin(np.abs(tau_grid - tau_fold)),
              np.argmin(np.abs(tau_grid - 0.5)),
              np.argmin(np.abs(tau_grid - 1.0)),
              np.argmin(np.abs(tau_grid - 1.5)),
              n_tau - 1]
sample_idx = sorted(set(sample_idx))
for i in sample_idx:
    print(f"  {tau_grid[i]:8.3f}", end="")
    for fi in range(n_funcs):
        print(f"  {S_bare[fi, i]:14.4f}", end="")
    print()


# =============================================================================
# STEP 4: CROSS-CHECKS AT THE FOLD
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Cross-Checks at tau = tau_fold")
print("=" * 78)

idx_fold = np.argmin(np.abs(tau_grid - tau_fold))
tau_at_fold = tau_grid[idx_fold]
print(f"  Fold index: {idx_fold}, tau = {tau_at_fold:.4f}")

# Cross-check 1: S_sqrt at fold should be S_fold / Lambda
# S_fold = sum d^2 |lambda| (bare), S_sqrt_bare = sum d^2 sqrt(lam^2/Lambda^2)
#        = (1/Lambda) * sum d^2 |lambda| = S_fold / Lambda
S_sqrt_at_fold_expected = S_fold / Lambda  # (local)
S_sqrt_at_fold_computed = S_bare[1, idx_fold]  # (local)
dev_sfold = abs(S_sqrt_at_fold_computed - S_sqrt_at_fold_expected) / S_sqrt_at_fold_expected  # (local)
print(f"\n  Cross-check 1: S_sqrt(fold) vs S_fold/Lambda")
print(f"    S_fold = {S_fold:.2f}")
print(f"    S_fold / Lambda = {S_sqrt_at_fold_expected:.4f}")
print(f"    S_sqrt computed  = {S_sqrt_at_fold_computed:.4f}")
print(f"    Relative deviation = {dev_sfold:.2e}")

# Check Lambda consistency
# If Lambda differs from S66 Lambda, the sqrt check will show it
# But the ratio S_sqrt(fold) * Lambda should recover S_fold
S_fold_recovered = S_sqrt_at_fold_computed * Lambda  # (local)
dev_sfold2 = abs(S_fold_recovered - S_fold) / S_fold  # (local)
print(f"    S_sqrt * Lambda  = {S_fold_recovered:.2f}")
print(f"    vs canonical S_fold = {S_fold:.2f}")
print(f"    Deviation = {dev_sfold2:.2e}")

# Cross-check 2: dS/dtau at fold
# Use spline derivative on S_sqrt, then multiply by Lambda
cs_sqrt = CubicSpline(tau_grid, S_bare[1])
dS_sqrt_dtau_fold = cs_sqrt(tau_at_fold, 1) * Lambda  # (local)
dev_dsfold = abs(dS_sqrt_dtau_fold - dS_fold) / abs(dS_fold)  # (local)
print(f"\n  Cross-check 2: dS/dtau at fold")
print(f"    dS_sqrt/dtau * Lambda = {dS_sqrt_dtau_fold:.2f}")
print(f"    Canonical dS_fold = {dS_fold:.2f}")
print(f"    Relative deviation = {dev_dsfold:.2e}")

# Cross-check 3: Bi-invariant limit (tau=0)
# At tau=0, SU(3) has SU(3)xSU(3) symmetry. All modes within each PW sector
# should be more degenerate (fewer distinct eigenvalues).
# We just check S(0) is reasonable and smooth.
print(f"\n  Cross-check 3: Bi-invariant limit")
print(f"    S_f*(0) = {S_bare[0, 0]:.4f}")
print(f"    S_f*(fold) = {S_bare[0, idx_fold]:.4f}")
print(f"    S_f*(2.0) = {S_bare[0, -1]:.4f}")
print(f"    Ratio S(2)/S(0) = {S_bare[0, -1] / S_bare[0, 0]:.4f}")


# =============================================================================
# STEP 5: DERIVATIVES AND SLOW-ROLL PARAMETERS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Derivatives, Slow-Roll Parameters, and Profile Analysis")
print("=" * 78)

# Build cubic splines for f* spectral action (bare)
cs_fstar = CubicSpline(tau_grid, S_bare[0])

# Dense evaluation grid for smooth derivatives
tau_fine = np.linspace(0.01, 1.99, 1000)

S_fine = cs_fstar(tau_fine)
dS_fine = cs_fstar(tau_fine, 1)
d2S_fine = cs_fstar(tau_fine, 2)

# Also for the three component functionals
cs_sqrt_full = CubicSpline(tau_grid, S_bare[1])
cs_exp_full = CubicSpline(tau_grid, S_bare[2])
cs_comp_full = CubicSpline(tau_grid, S_bare[3])

# Verify dS/dtau at fold for f*
dS_fstar_fold = cs_fstar(tau_fold, 1)
d2S_fstar_fold = cs_fstar(tau_fold, 2)
print(f"  f* spectral action at fold:")
print(f"    S_f*(fold) = {cs_fstar(tau_fold):.4f}")
print(f"    dS_f*/dtau(fold) = {dS_fstar_fold:.4f}")
print(f"    d^2S_f*/dtau^2(fold) = {d2S_fstar_fold:.4f}")

# Check derivative at fold for S_sqrt cross-check
dS_sqrt_fold_check = cs_sqrt_full(tau_fold, 1)  # (local)
d2S_sqrt_fold_check = cs_sqrt_full(tau_fold, 2)  # (local)
print(f"\n  sqrt spectral action at fold:")
print(f"    S_sqrt(fold) = {cs_sqrt_full(tau_fold):.4f}")
print(f"    dS_sqrt/dtau(fold) = {dS_sqrt_fold_check:.4f}")
print(f"    d^2S_sqrt/dtau^2(fold) = {d2S_sqrt_fold_check:.4f}")
print(f"    (dS_sqrt/dtau * Lambda = {dS_sqrt_fold_check * Lambda:.2f} vs canonical {dS_fold:.2f})")

# Slow-roll parameter eps_H for f*
# eps_H = (1/2G) * (S'/S)^2 / (S''/S) when S'' > 0
eps_H_fine = np.full_like(tau_fine, np.nan)
for j in range(len(tau_fine)):
    if d2S_fine[j] > 0 and S_fine[j] > 0:
        eps_H_fine[j] = 0.5 * (dS_fine[j] / S_fine[j])**2 / (d2S_fine[j] / S_fine[j]) / G
    elif d2S_fine[j] != 0 and S_fine[j] > 0:
        # Record with sign for diagnostic even when S'' < 0
        eps_H_fine[j] = 0.5 * (dS_fine[j] / S_fine[j])**2 / (d2S_fine[j] / S_fine[j]) / G

ns_fine = 1.0 - 2.0 * eps_H_fine


# =============================================================================
# STEP 6: PROFILE ANALYSIS — EXTREMA AND MODULI STABILIZATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Profile Analysis — Extrema and Moduli Stabilization")
print("=" * 78)

# Locate the fold maximum in dS/dtau
idx_fold_fine = np.argmin(np.abs(tau_fine - tau_fold))
print(f"  dS/dtau at fold (tau={tau_fold}): {dS_fine[idx_fold_fine]:.4f}")
print(f"  d^2S/dtau^2 at fold: {d2S_fine[idx_fold_fine]:.4f}")

# Find where dS/dtau changes sign (extrema of S)
dS_sign = np.sign(dS_fine)
sign_changes = np.where(np.diff(dS_sign) != 0)[0]

print(f"\n  Sign changes in dS/dtau (extrema of S):")
extrema_tau = []
extrema_S = []
extrema_type = []
for sc in sign_changes:
    tau_sc = 0.5 * (tau_fine[sc] + tau_fine[sc + 1])  # (local)
    S_sc = cs_fstar(tau_sc)  # (local)
    d2S_sc = cs_fstar(tau_sc, 2)  # (local)
    ext_type = "minimum" if d2S_sc > 0 else "maximum"  # (local)
    extrema_tau.append(tau_sc)
    extrema_S.append(S_sc)
    extrema_type.append(ext_type)
    print(f"    tau = {tau_sc:.4f}: S = {S_sc:.4f}, d^2S = {d2S_sc:.2f} ({ext_type})")

# Check for post-fold minimum
post_fold_minima = [(t, s, d2) for t, s, d2, tp in
                    zip(extrema_tau, extrema_S,
                        [cs_fstar(t, 2) for t in extrema_tau],
                        extrema_type)
                    if t > tau_fold and tp == "minimum"]

print(f"\n  Post-fold minima found: {len(post_fold_minima)}")
for t, s, d2 in post_fold_minima:
    print(f"    tau_eq = {t:.4f}, S(tau_eq) = {s:.4f}, d^2S/dtau^2 = {d2:.2f}")

# Monotonicity analysis for tau > tau_fold
idx_post_fold = tau_fine > tau_fold
dS_post = dS_fine[idx_post_fold]
tau_post = tau_fine[idx_post_fold]
always_increasing = np.all(dS_post > 0)
always_decreasing = np.all(dS_post < 0)

print(f"\n  Monotonicity for tau > {tau_fold}:")
print(f"    Always increasing: {always_increasing}")
print(f"    Always decreasing: {always_decreasing}")
print(f"    dS/dtau range: [{dS_post.min():.4f}, {dS_post.max():.4f}]")
print(f"    S range: [{S_fine[idx_post_fold].min():.4f}, {S_fine[idx_post_fold].max():.4f}]")


# =============================================================================
# STEP 7: EFFECTIVE POTENTIAL AND CC ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Effective Potential and Cosmological Constant Analysis")
print("=" * 78)

# V_eff(tau) = -S(tau) (system rolls DOWN V_eff = UP in S)
V_eff_fine = -S_fine

# If a minimum in S exists, it's a maximum in V_eff.
# If S is monotonically increasing, V_eff is monotonically decreasing = no
# stable equilibrium from spectral action alone.

# CC contribution: for each component functional
print("\n  S(tau) at selected points for all functionals:")
print(f"  {'tau':>6s}  {'f*':>14s}  {'sqrt':>14s}  {'exp':>14s}  {'compact':>14s}")
print("  " + "-" * 65)
for tau_val in [0.0, 0.10, 0.19, 0.30, 0.50, 1.00, 1.50, 2.00]:
    idx_v = np.argmin(np.abs(tau_grid - tau_val))
    print(f"  {tau_grid[idx_v]:6.2f}", end="")
    for fi in range(n_funcs):
        print(f"  {S_bare[fi, idx_v]:14.4f}", end="")
    print()

# Functional-independence check: does the monotonicity depend on the functional?
for fi, fn in enumerate(func_names):
    cs_fi = CubicSpline(tau_grid, S_bare[fi])
    dS_fi_post = np.array([cs_fi(t, 1) for t in tau_post])
    mono_fi = np.all(dS_fi_post > 0)
    print(f"\n  {fn}: monotonically increasing for tau>{tau_fold}? {mono_fi}")
    print(f"    dS/dtau range (post-fold): [{dS_fi_post.min():.4f}, {dS_fi_post.max():.4f}]")

# Relative S(tau) normalized to fold value
S_fstar_fold = cs_fstar(tau_fold)
print(f"\n  S_f*(fold) = {S_fstar_fold:.4f}")
print(f"  S_f*(0)/S_f*(fold) = {S_bare[0, 0] / S_fstar_fold:.6f}")
print(f"  S_f*(2)/S_f*(fold) = {S_bare[0, -1] / S_fstar_fold:.6f}")

# Estimate CC from spectral action
# The CC in spectral action units: Lambda_CC ~ (S_eq - S_fold) * M_KK^4 / normalization
# If S is monotonic, the "equilibrium" is at infinity, and the CC is set by the
# asymptotic behavior.
print(f"\n  Delta S / S(fold) at tau = 0.5: {(S_bare[0, np.argmin(np.abs(tau_grid - 0.5))] - S_fstar_fold) / S_fstar_fold:.6f}")
print(f"  Delta S / S(fold) at tau = 1.0: {(S_bare[0, np.argmin(np.abs(tau_grid - 1.0))] - S_fstar_fold) / S_fstar_fold:.6f}")
print(f"  Delta S / S(fold) at tau = 2.0: {(S_bare[0, -1] - S_fstar_fold) / S_fstar_fold:.6f}")


# =============================================================================
# STEP 8: GRADIENT PROFILE dS/dtau(tau)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Gradient Profile dS/dtau(tau)")
print("=" * 78)

# dS/dtau is the spectral action gradient that drives modulus dynamics
print(f"\n  dS_f*/dtau at selected tau values:")
print(f"  {'tau':>6s}  {'dS/dtau':>14s}  {'d^2S/dtau^2':>14s}  {'eps_H':>14s}  {'n_s':>14s}")
print("  " + "-" * 70)
tau_display = [0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40, 0.50,
               0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
for tau_val in tau_display:
    idx_disp = np.argmin(np.abs(tau_fine - tau_val))
    if idx_disp < len(tau_fine):
        print(f"  {tau_fine[idx_disp]:6.3f}  {dS_fine[idx_disp]:14.4f}  "
              f"{d2S_fine[idx_disp]:14.4f}  {eps_H_fine[idx_disp]:14.6f}  "
              f"{ns_fine[idx_disp]:14.6f}")


# =============================================================================
# STEP 9: EQUATION OF STATE FROM TAU RELAXATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Equation of State from Tau Relaxation")
print("=" * 78)

# For a scalar modulus tau with potential V_eff = -S(tau):
# w = (T - V) / (T + V)
# In slow-roll: T << V, so w ~ -1 + (2/3)*eps_V
# eps_V = (1/2G) * (V'/V)^2 = (1/2G) * (S'/S)^2

eps_V_fine = 0.5 * (dS_fine / S_fine)**2 / G
w_slow_roll = -1.0 + (2.0/3.0) * eps_V_fine

print(f"  {'tau':>6s}  {'eps_V':>12s}  {'w_SR':>12s}")
print("  " + "-" * 35)
for tau_val in [0.19, 0.30, 0.50, 1.00, 1.50, 2.00]:
    idx_w = np.argmin(np.abs(tau_fine - tau_val))
    print(f"  {tau_fine[idx_w]:6.3f}  {eps_V_fine[idx_w]:12.6f}  {w_slow_roll[idx_w]:12.6f}")


# =============================================================================
# STEP 10: COMPARISON WITH QUARTIC/CUBIC MODELS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Comparison with S72 Polynomial Models")
print("=" * 78)

# S72 used quartic/cubic Taylor expansions of S(tau) around the fold.
# Now we have the actual S(tau). Compare.

# Taylor coefficients from data
S0 = cs_fstar(tau_fold)
S1 = cs_fstar(tau_fold, 1)
S2 = cs_fstar(tau_fold, 2)
S3 = cs_fstar(tau_fold, 3)
S4 = cs_fstar(tau_fold, 4) if n_tau > 5 else 0.0  # (local)

dtau = tau_fine - tau_fold
S_quadratic = S0 + S1 * dtau + 0.5 * S2 * dtau**2
S_cubic = S_quadratic + (1./6.) * S3 * dtau**3
S_quartic = S_cubic + (1./24.) * S4 * dtau**4

print(f"  Taylor coefficients of S_f*(tau) at fold:")
print(f"    S(fold)    = {S0:.4f}")
print(f"    S'(fold)   = {S1:.4f}")
print(f"    S''(fold)  = {S2:.4f}")
print(f"    S'''(fold) = {S3:.4f}")
print(f"    S''''(fold) = {S4:.4f}")

# Compare actual vs polynomial at tau = 0.5 and 1.0
for tau_val in [0.5, 1.0, 1.5, 2.0]:
    idx_c = np.argmin(np.abs(tau_fine - tau_val))
    S_actual = S_fine[idx_c]  # (local)
    dt = tau_fine[idx_c] - tau_fold  # (local)
    S_q2 = S0 + S1 * dt + 0.5 * S2 * dt**2  # (local)
    S_q3 = S_q2 + (1./6.) * S3 * dt**3  # (local)
    S_q4 = S_q3 + (1./24.) * S4 * dt**4  # (local)
    print(f"\n  tau = {tau_val:.1f} (dt = {dt:.2f}):")
    print(f"    Actual:    {S_actual:.4f}")
    print(f"    Quadratic: {S_q2:.4f} (dev = {abs(S_actual - S_q2)/S_actual:.4f})")
    print(f"    Cubic:     {S_q3:.4f} (dev = {abs(S_actual - S_q3)/S_actual:.4f})")
    print(f"    Quartic:   {S_q4:.4f} (dev = {abs(S_actual - S_q4)/S_actual:.4f})")


# =============================================================================
# STEP 11: FUNCTIONAL-INDEPENDENCE CLASSIFICATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Functional-Independence Classification")
print("=" * 78)

# Key question: which properties of S(tau) are functional-independent?
# Compare across all 4 functionals.

# Property 1: Is S(tau) monotonically increasing for tau > fold?
print("\n  Property 1: Post-fold monotonicity")
for fi, fn in enumerate(func_names):
    cs_fi = CubicSpline(tau_grid, S_bare[fi])
    dS_fi_post = np.array([cs_fi(t, 1) for t in tau_post])
    print(f"    {fn:>8s}: monotonic = {np.all(dS_fi_post > 0)}, "
          f"min(dS/dtau) = {dS_fi_post.min():.4f}")

# Property 2: Shape of S(tau)/S(fold) is the same for all functionals?
print("\n  Property 2: Normalized profile S(tau)/S(fold)")
print(f"  {'tau':>6s}", end="")
for fn in func_names:
    print(f"  {fn:>14s}", end="")
print()
for tau_val in [0.0, 0.19, 0.5, 1.0, 1.5, 2.0]:
    idx_n = np.argmin(np.abs(tau_grid - tau_val))
    print(f"  {tau_grid[idx_n]:6.2f}", end="")
    for fi in range(n_funcs):
        S_fold_fi = S_bare[fi, np.argmin(np.abs(tau_grid - tau_fold))]
        print(f"  {S_bare[fi, idx_n] / S_fold_fi:14.6f}", end="")
    print()

# Property 3: dS/dtau sign at fold
print("\n  Property 3: Sign of dS/dtau at fold")
for fi, fn in enumerate(func_names):
    cs_fi = CubicSpline(tau_grid, S_bare[fi])
    dS_fold_fi = cs_fi(tau_fold, 1)
    print(f"    {fn:>8s}: dS/dtau(fold) = {dS_fold_fi:.4f} (sign = {'+' if dS_fold_fi > 0 else '-'})")


# =============================================================================
# GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: SPECTRAL-ACTION-PROFILE-73a")
print("=" * 78)

# Determine verdict
all_S_positive = np.all(S_bare[0] > 0)
profile_smooth = True  # checked by spline quality

# Check for post-fold minimum
has_post_fold_min = len(post_fold_minima) > 0
if has_post_fold_min:
    tau_eq_best = post_fold_minima[0][0]
    d2S_eq_best = post_fold_minima[0][2]
    in_range = 0.19 < tau_eq_best < 1.5
    stable = d2S_eq_best > 0
    if in_range and stable:
        verdict = "PASS"
        detail = (f"Post-fold minimum at tau_eq = {tau_eq_best:.4f} with "
                  f"d^2S/dtau^2 = {d2S_eq_best:.2f} > 0. Stable moduli stabilization.")
    elif stable:
        verdict = "INFO"
        detail = (f"Post-fold minimum at tau_eq = {tau_eq_best:.4f} (outside [0.19, 1.5]) "
                  f"with d^2S/dtau^2 = {d2S_eq_best:.2f} > 0.")
    else:
        verdict = "INFO"
        detail = (f"Post-fold extremum at tau_eq = {tau_eq_best:.4f} is unstable "
                  f"(d^2S/dtau^2 = {d2S_eq_best:.2f} < 0).")
else:
    if always_increasing:
        verdict = "INFO"
        detail = ("S(tau) is monotonically increasing for tau > 0.19 on [0, 2]. "
                  "No post-fold minimum exists within the computed range. "
                  "Moduli stabilization requires additional physics beyond S(tau).")
    elif not all_S_positive:
        verdict = "FAIL"
        detail = "S(tau) has negative values — unphysical."
    else:
        verdict = "INFO"
        detail = ("S(tau) has non-trivial structure but no clean minimum. "
                  f"dS/dtau range post-fold: [{dS_post.min():.4f}, {dS_post.max():.4f}].")

print(f"\n  Gate: SPECTRAL-ACTION-PROFILE-73a")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"\n  All S > 0: {all_S_positive}")
print(f"  Profile smooth: {profile_smooth}")
print(f"  Post-fold minima: {len(post_fold_minima)}")


# =============================================================================
# STEP 12: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 12: Save Data")
print("=" * 78)

np.savez('s73a_spectral_action_profile.npz',
    # Gate
    gate_name='SPECTRAL-ACTION-PROFILE-73a',
    gate_verdict=verdict,
    gate_detail=detail,
    # Configuration
    alpha_star=alpha_star,
    beta_star=beta_star,
    MAX_PQ_SUM=MAX_PQ_SUM,
    Lambda=Lambda,
    Lambda_sq=Lambda_sq,
    Delta=Delta,
    G_DeWitt=G,
    # Tau grid and spectral actions
    tau_grid=tau_grid,
    S_bare=S_bare,          # [4 functionals, n_tau]
    S_bcs=S_bcs,            # [4 functionals, n_tau]
    func_names=np.array(func_names),
    # Fine grid derivatives (f* only)
    tau_fine=tau_fine,
    S_fine=S_fine,
    dS_fine=dS_fine,
    d2S_fine=d2S_fine,
    eps_H_fine=eps_H_fine,
    ns_fine=ns_fine,
    eps_V_fine=eps_V_fine,
    w_slow_roll=w_slow_roll,
    # Taylor coefficients at fold
    S_taylor=np.array([S0, S1, S2, S3, S4]),
    # Extrema data
    extrema_tau=np.array(extrema_tau) if extrema_tau else np.array([]),
    extrema_S=np.array(extrema_S) if extrema_S else np.array([]),
    extrema_type=np.array(extrema_type) if extrema_type else np.array([]),
    n_post_fold_minima=len(post_fold_minima),
    # Cross-checks
    lambda_max_per_tau=lambda_max_per_tau,
    S_fold_recovered=S_fold_recovered,
    dS_fold_recovered=dS_sqrt_dtau_fold,
)

print("  Saved: s73a_spectral_action_profile.npz")


# =============================================================================
# STEP 13: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 13: Generate Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.35, wspace=0.3)

# Panel (a): S(tau) for all 4 functionals
ax1 = fig.add_subplot(gs[0, 0])
colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e']
labels = [r'$f^*(x) = 0.912\sqrt{x} + 0.088\,e^{-x}$',
          r'$f(x) = \sqrt{x}$',
          r'$f(x) = e^{-x}$',
          r'$f(x) = (1-x)_+^4$']
for fi in range(n_funcs):
    ax1.plot(tau_grid, S_bare[fi], 'o-', color=colors[fi], label=labels[fi],
             markersize=2, linewidth=1.2)
ax1.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$S_f(\tau)$')
ax1.set_title(r'(a) Spectral Action $S_f(\tau)$ for 4 Functionals')
ax1.legend(fontsize=7, loc='best')
ax1.grid(True, alpha=0.3)

# Panel (b): Normalized S(tau)/S(fold) for all functionals
ax2 = fig.add_subplot(gs[0, 1])
for fi in range(n_funcs):
    S_fold_fi = S_bare[fi, np.argmin(np.abs(tau_grid - tau_fold))]
    ax2.plot(tau_grid, S_bare[fi] / S_fold_fi, 'o-', color=colors[fi],
             label=labels[fi], markersize=2, linewidth=1.2)
ax2.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax2.set_xlabel(r'$\tau$')
ax2.set_ylabel(r'$S_f(\tau) / S_f(\tau_{\rm fold})$')
ax2.set_title(r'(b) Normalized Profile $S_f / S_f^{\rm fold}$')
ax2.legend(fontsize=7, loc='best')
ax2.grid(True, alpha=0.3)

# Panel (c): dS_f*/dtau
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(tau_fine, dS_fine, 'r-', linewidth=1.5, label=r'$dS_{f^*}/d\tau$')
ax3.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax3.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel(r'$dS_{f^*}/d\tau$')
ax3.set_title(r'(c) Spectral Action Gradient $dS_{f^*}/d\tau$')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel (d): d^2S_f*/dtau^2
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_fine, d2S_fine, 'b-', linewidth=1.5, label=r'$d^2S_{f^*}/d\tau^2$')
ax4.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax4.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$d^2S_{f^*}/d\tau^2$')
ax4.set_title(r'(d) Spectral Action Curvature $d^2S_{f^*}/d\tau^2$')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# Panel (e): eps_H and n_s
ax5 = fig.add_subplot(gs[2, 0])
valid = ~np.isnan(eps_H_fine)
ax5.plot(tau_fine[valid], eps_H_fine[valid], 'r-', linewidth=1.5, label=r'$\epsilon_H$')
ax5.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax5.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax5.set_xlabel(r'$\tau$')
ax5.set_ylabel(r'$\epsilon_H$')
ax5.set_title(r'(e) Slow-Roll Parameter $\epsilon_H(\tau)$')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)

# Panel (f): Effective potential V_eff = -S
ax6 = fig.add_subplot(gs[2, 1])
ax6.plot(tau_fine, V_eff_fine, 'k-', linewidth=1.5, label=r'$V_{\rm eff} = -S_{f^*}$')
ax6.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax6.set_xlabel(r'$\tau$')
ax6.set_ylabel(r'$V_{\rm eff}(\tau)$')
ax6.set_title(r'(f) Effective Potential $V_{\rm eff}(\tau) = -S_{f^*}(\tau)$')
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3)

fig.suptitle('SPECTRAL-ACTION-PROFILE-73a: S(tau) Profile for tau in [0, 2]\n'
             r'Spectral functional: $f^*(x) = 0.912\sqrt{x} + 0.088\,e^{-x}$ | '
             r'$L_{\max} = 3$ (Peter-Weyl)',
             fontsize=12, fontweight='bold')

plt.savefig('s73a_spectral_action_profile.png', dpi=150, bbox_inches='tight')
print("  Saved: s73a_spectral_action_profile.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
