#!/usr/bin/env python3
"""
s74_f_star_joint.py -- F-STAR-JOINT-74 (Session 74 Wave 2)
==========================================================

Gate: F-STAR-JOINT-74
  PASS: chi^2/dof < 1 AND best-fit c_i has one dominant component > 0.9
  INFO: chi^2/dof in [1, 3] OR category-4 lock partial
  FAIL: chi^2/dof > 3

Physics:
--------
This is the S73B W1-C follow-up. W1-C showed that no SINGLE-particle spectral
functional (pure sqrt / pure exp / pure compact) satisfies (n_s, m_H) jointly.
F-STAR-JOINT-74 tests the 4-PARAMETER family:

    f(x) = c_0 + c_1 * sqrt(x) + c_2 * exp(-x) + c_3 * (1-x)_+^4

against the 5-observable scorecard (n_s, m_H, r, w_0, alpha_s), jointly.

Question: does there exist a single (c_0, c_1, c_2, c_3) with chi^2/dof < 1?

W1-A result: alpha_s = 8.4e-15 (FUNCTIONAL-INDEPENDENT structure).
W1-I result: n_s 1-loop correction ~ 10^-5 (negligible, use tree-level).
W1-J result: w_0 Volovik partition gives -0.918 (FUNCTIONAL-INDEPENDENT).

Spectral action (LINEARITY in f):
    S_f(tau) = c_0 * N_modes + c_1 * S_sqrt(tau) + c_2 * S_exp(tau) + c_3 * S_comp(tau)

Each observable as function of (c_0, c_1, c_2, c_3):
    eps_H(c) = 0.5 * (dS_f/dtau)^2 / (S_f * d^2S_f/dtau^2)
    n_s(c)   = 1 - 2 * eps_H(c)
    r(c)     = 16 * eps_H(c)  [formal; substrate says INAPPLICABLE]
    f(0)     = c_0 + c_2 + c_3  (sqrt(0)=0, exp(0)=1, compact(0)=1)
    m_H(c)   = m_H_ref * sqrt(f(0))  where m_H_ref = 127.46 GeV (S67, L=5)
    w_0(c)   = -0.918  (FUNCTIONAL-INDEPENDENT)
    alpha_s(c) = 8.4e-15  (FUNCTIONAL-INDEPENDENT via W1-A transfer function)

Constraint: sum c_i = 1 (normalization) and c_i >= 0 (positivity).

Agent: Lizzi Spectral-Functional Theorist (Session 74, Wave 2 Batch 2)
"""

import numpy as np
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import minimize, differential_evolution
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, G_DeWitt, PI,
    a0_fold, a2_fold, a4_fold,
    M_KK_gravity, M_Pl_reduced,
    A_s_CMB, m_H_obs, w0_FW, planck_ns,
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("F-STAR-JOINT-74: 4-Parameter Spectral Functional Joint Fit")
print("=" * 78)

# Observational scorecard with 1-sigma uncertainties
ns_target = 0.9649      # Planck 2018 TT,TE,EE+lowE+lensing (local)
ns_sigma = 0.0042                                                    # (local)

mH_target_val = 125.1   # PDG 2024 central (local)
mH_sigma = 0.17                                                      # (local)

r_target = 0.033        # BICEP/Keck + Planck 2022 current best upper-ish (local)
r_sigma = 0.025                                                      # (local)

w0_target = -0.918      # Framework prediction (FI, Volovik) (local)
w0_sigma = 0.06                                                      # (local)

alphas_target = -0.0045  # Planck 2018 running of scalar tilt (local)
alphas_sigma = 0.0067                                                # (local)

print("\n  Observational scorecard (5 observables, 1-sigma):")
print(f"    n_s     = {ns_target}  +/- {ns_sigma}")
print(f"    m_H     = {mH_target_val}    +/- {mH_sigma}  GeV")
print(f"    r       = {r_target}  +/- {r_sigma}")
print(f"    w_0     = {w0_target} +/- {w0_sigma}")
print(f"    alpha_s = {alphas_target} +/- {alphas_sigma}")

# =============================================================================
# LOAD S66 SPECTRAL ACTION DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Load S66 Spectral Action Basis")
print("=" * 78)

d66 = np.load('s66_cutoff_ns.npz', allow_pickle=True)
tau_S36 = d66['tau_S36']
S_bare = d66['S_bare']        # [3 cutoffs, 16 tau], order = sqrt, exp, compact
cutoff_names = d66['cutoff_names']
N_modes_s66 = float(d66['a0_computed'])   # 155984 (total eigenmode count)

S_sqrt = S_bare[0]    # [16] spectral action with f(x) = sqrt(x)
S_exp = S_bare[1]     # [16] spectral action with f(x) = exp(-x)
S_comp = S_bare[2]    # [16] spectral action with f(x) = (1-x)_+^4

print(f"  Basis loaded: sqrt, exp, compact on tau_S36 = [{tau_S36[0]:.3f}, {tau_S36[-1]:.3f}]")
print(f"  N_modes (S66 max_pq_sum=3) = {N_modes_s66:.0f}")
print(f"  S_sqrt(fold) = {CubicSpline(tau_S36, S_sqrt)(tau_fold):.2f}")
print(f"  S_exp(fold)  = {CubicSpline(tau_S36, S_exp)(tau_fold):.2f}")
print(f"  S_comp(fold) = {CubicSpline(tau_S36, S_comp)(tau_fold):.2f}")

# =============================================================================
# LOAD W1-A ALPHA_S (FUNCTIONAL-INDEPENDENT)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Load W1-A Transfer Function (alpha_s FI)")
print("=" * 78)

d74a = np.load('s74_transfer_function.npz', allow_pickle=True)
alpha_s_FI = float(d74a['alpha_s_pivot'])   # 8.4e-15 (local)
ns_pivot_FI = float(d74a['n_s_pivot'])      # 1.0000 (uniform transfer limit) (local)

print(f"  W1-A verdict: {d74a['gate_verdict']}")
print(f"  alpha_s(pivot) = {alpha_s_FI:.6e}  [FUNCTIONAL-INDEPENDENT]")
print(f"  Note: alpha_s_FI is NOT the S73B naive +0.833 but the B1/B2/B3 mixed pivot value")
print(f"  The framework prediction alpha_s = {alpha_s_FI:.3e} is the same for all c_i")

# =============================================================================
# S67 HIGGS MASS REFERENCE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Higgs Mass Reference (S67/S73B)")
print("=" * 78)

# S67 HIGGS-ZETA-67: m_H(cutoff, L=5) = 127.46 GeV for f(0)=1
# m_H scales as m_H = m_H_ref * sqrt(f(0)) (quartic coupling weighting)
# For f(x) = c_0 + c_1*sqrt(x) + c_2*exp(-x) + c_3*(1-x)_+^4:
#   f(0) = c_0 + 0 + c_2 + c_3 = c_0 + c_2 + c_3
mH_ref = 127.46  # GeV, S67 L=5 cutoff reference (f(0)=1) (local)
print(f"  m_H reference: m_H_ref = {mH_ref} GeV at f(0) = 1 (S67 L=5)")
print(f"  Scaling law:   m_H(c) = m_H_ref * sqrt(f(0))")
print(f"                 f(0)   = c_0 + c_2 + c_3  (sqrt(0) = 0)")

# =============================================================================
# OBSERVABLE FUNCTIONS (c_i) -> (n_s, m_H, r, w_0, alpha_s)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Build Observable Functions")
print("=" * 78)


def S_f_of_tau(c, tau_arr):
    """
    Full spectral action on tau grid, given c = (c_0, c_1, c_2, c_3).
    S_f(tau) = c_0 * N_modes + c_1 * S_sqrt(tau) + c_2 * S_exp(tau) + c_3 * S_comp(tau)
    (constant c_0 contributes c_0 * N_modes to S for every tau.)
    """
    c0, c1, c2, c3 = c
    return c0 * N_modes_s66 + c1 * S_sqrt + c2 * S_exp + c3 * S_comp


def eps_H_at_fold(c):
    """
    eps_H = 0.5 * (dS/dtau)^2 / (S * d^2S/dtau^2) at tau = tau_fold.
    """
    S_combo = S_f_of_tau(c, tau_S36)
    try:
        cs = CubicSpline(tau_S36, S_combo)
    except Exception:
        return np.nan
    S_val = cs(tau_fold)
    dS = cs(tau_fold, 1)
    d2S = cs(tau_fold, 2)
    if abs(d2S) < 1e-30 or abs(S_val) < 1e-30:
        return np.nan
    return 0.5 * dS**2 / (S_val * d2S)


def n_s_of_c(c):
    """n_s = 1 - 2 * eps_H(c)  (tree-level; W1-I showed 1-loop ~ 10^-5)"""
    eps_H = eps_H_at_fold(c)
    return 1.0 - 2.0 * eps_H


def r_of_c(c):
    """r = 16 * eps_H(c) (formal single-field slow-roll; substrate says INAPPLICABLE)"""
    return 16.0 * eps_H_at_fold(c)


def m_H_of_c(c):
    """m_H = m_H_ref * sqrt(f(0))  where f(0) = c_0 + c_2 + c_3"""
    c0, c1, c2, c3 = c
    f0 = c0 + c2 + c3
    if f0 < 0:
        return np.nan
    return mH_ref * np.sqrt(f0)


def w_0_of_c(c):
    """w_0 is FUNCTIONAL-INDEPENDENT (Volovik partition, S58/W1-J)"""
    return w0_FW  # = -0.918


def alpha_s_of_c(c):
    """alpha_s is FUNCTIONAL-INDEPENDENT (W1-A transfer function)"""
    return alpha_s_FI  # ~ 8.4e-15


# Sanity-check baseline: c = (0, 0.9117, 0.0883, 0) should reproduce S72/W1-C values
c_baseline = np.array([0.0, 0.9116771171053042, 0.08832288289469575, 0.0])
print("\n  Baseline check at c = (0, 0.9117, 0.0883, 0)  [S72 best fit]:")
print(f"    n_s     = {n_s_of_c(c_baseline):.10f}  (expected 0.9649)")
print(f"    m_H     = {m_H_of_c(c_baseline):.4f} GeV  (expected ~37.9 from sqrt(0.0883))")
print(f"    r       = {r_of_c(c_baseline):.6f}  (formal)")
print(f"    w_0     = {w_0_of_c(c_baseline):.6f}  (FI)")
print(f"    alpha_s = {alpha_s_of_c(c_baseline):.6e}  (FI)")
print(f"    sum c_i = {c_baseline.sum():.6f}  (check normalization)")

# =============================================================================
# CHI^2 AND GRADIENTS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Chi-Squared Functional")
print("=" * 78)

# Assemble targets and sigmas into arrays
targets = np.array([ns_target, mH_target_val, r_target, w0_target, alphas_target])
sigmas = np.array([ns_sigma, mH_sigma, r_sigma, w0_sigma, alphas_sigma])
obs_labels = ['n_s', 'm_H', 'r', 'w_0', 'alpha_s']


def observables(c):
    """Return 5-vector of observable predictions."""
    return np.array([
        n_s_of_c(c),
        m_H_of_c(c),
        r_of_c(c),
        w_0_of_c(c),
        alpha_s_of_c(c),
    ])


def chi_squared(c):
    """chi^2 = sum ((obs - target)^2 / sigma^2)"""
    pred = observables(c)
    if np.any(np.isnan(pred)):
        return 1e20
    residual = (pred - targets) / sigmas
    return np.sum(residual**2)


def chi2_free_only(c):
    """
    chi^2 over observables that DEPEND on c_i (n_s, m_H, r).
    w_0 and alpha_s are FI -- they cannot be affected by c_i, so including them
    in the optimization adds a constant floor but gives no steering.
    Use this for optimization diagnostics.
    """
    pred = observables(c)
    if np.any(np.isnan(pred)):
        return 1e20
    residual = (pred - targets) / sigmas
    # Keep only n_s, m_H, r components (indices 0, 1, 2)
    return np.sum(residual[:3]**2)


# Evaluate chi^2 at baseline
chi2_base = chi_squared(c_baseline)
print(f"\n  chi^2 at baseline (0, 0.9117, 0.0883, 0) = {chi2_base:.4f}")
print(f"  dof = 5 observables - 4 parameters = 1")
print(f"  chi^2/dof baseline = {chi2_base / 1.0:.4f}")

# =============================================================================
# CONSTRAINED OPTIMIZATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Constrained Joint Optimization")
print("=" * 78)

# Strategy:
# 1. Constraint: sum c_i = 1 (normalization)
# 2. Bounds: c_i >= 0 (positivity)
# 3. Use scipy.optimize.minimize with SLSQP for the constrained problem

# SLSQP handles both linear equality constraints and box bounds
# Constraint: sum(c) - 1 = 0
constraint_eq = {'type': 'eq', 'fun': lambda c: np.sum(c) - 1.0}
bounds_ci = [(0.0, 1.0)] * 4

print("  Stage 1: SLSQP local minimization from baseline")
print("    Initial: c = (0, 0.9117, 0.0883, 0)")
result_slsqp = minimize(
    chi_squared,
    c_baseline,
    method='SLSQP',
    bounds=bounds_ci,
    constraints=[constraint_eq],
    options={'ftol': 1e-14, 'maxiter': 500, 'disp': False},
)
print(f"    converged: {result_slsqp.success}")
print(f"    message: {result_slsqp.message}")
print(f"    c* (SLSQP): {result_slsqp.x}")
print(f"    chi^2 (SLSQP): {result_slsqp.fun:.6e}")
print(f"    sum c_i: {result_slsqp.x.sum():.8f}")

# Stage 2: Multi-start local searches from 10 random initial points on the simplex
print("\n  Stage 2: Multi-start SLSQP (10 random simplex draws)")
rng = np.random.default_rng(74)  # (local)
best_result = result_slsqp
best_chi2 = result_slsqp.fun
results_pool = [result_slsqp]

for trial in range(10):
    # Draw from Dirichlet(1,1,1,1) to get uniform samples on the simplex
    c0_trial = rng.dirichlet([1.0, 1.0, 1.0, 1.0])  # (local)
    res = minimize(
        chi_squared,
        c0_trial,
        method='SLSQP',
        bounds=bounds_ci,
        constraints=[constraint_eq],
        options={'ftol': 1e-14, 'maxiter': 500, 'disp': False},
    )
    results_pool.append(res)
    if res.success and res.fun < best_chi2:
        best_chi2 = res.fun
        best_result = res

print(f"    Best chi^2 found: {best_chi2:.6e}")
print(f"    Best c* = {best_result.x}")
print(f"    Best sum c_i: {best_result.x.sum():.8f}")

# Stage 3: Global differential_evolution with the same constraint
# SLSQP may miss multi-modal minima -- DE finds global
print("\n  Stage 3: Differential Evolution (global, with sum-constraint)")


def chi2_penalty(c):
    """Chi^2 with soft penalty for sum(c)=1 (DE does not handle equality constraints)."""
    penalty = 1e6 * (np.sum(c) - 1.0)**2  # (local)
    return chi_squared(c) + penalty


de_result = differential_evolution(
    chi2_penalty,
    bounds=bounds_ci,
    seed=74,
    maxiter=300,
    tol=1e-12,  # (local)
    polish=True,
    init='sobol',
)
# Project back onto simplex (rescale)
c_de = de_result.x / de_result.x.sum() if de_result.x.sum() > 0 else de_result.x
chi2_de = chi_squared(c_de)
print(f"    DE raw  : c = {de_result.x}, sum = {de_result.x.sum():.6f}")
print(f"    DE proj : c = {c_de}, chi^2 = {chi2_de:.6e}")

if chi2_de < best_chi2:
    best_chi2 = chi2_de
    best_result = de_result
    best_result.x = c_de
    print(f"    DE wins; best chi^2 = {best_chi2:.6e}")

# Stage 4: Polish with a final SLSQP starting from DE's projected minimum
print("\n  Stage 4: Final polish SLSQP from best candidate")
polish = minimize(
    chi_squared,
    best_result.x,
    method='SLSQP',
    bounds=bounds_ci,
    constraints=[constraint_eq],
    options={'ftol': 1e-15, 'maxiter': 1000, 'disp': False},
)
print(f"    polish chi^2: {polish.fun:.6e}")
print(f"    polish c*:    {polish.x}")
print(f"    polish sum:   {polish.x.sum():.8f}")
if polish.fun < best_chi2:
    best_chi2 = polish.fun
    best_result = polish

# =============================================================================
# FINAL BEST-FIT RESULT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Best-Fit Summary")
print("=" * 78)

c_star = best_result.x
chi2_star = best_chi2
n_obs = len(targets)

# Pre-registered dof: 5 observables - 4 parameters = 1 (per task specification).
# This is the gate-defining dof. The normalization constraint sum c_i = 1
# would reduce effective free params to 3, giving dof = 2 -- we report both.
dof = 1  # pre-registered (5 obs - 4 params) (local)
dof_with_norm = 2  # 5 obs - 3 free after sum-constraint (local)
chi2_per_dof = chi2_star / dof   # gate-defining (local)
chi2_per_dof_norm = chi2_star / dof_with_norm  # alternative accounting (local)

print(f"\n  c*  = ({c_star[0]:.8f}, {c_star[1]:.8f}, {c_star[2]:.8f}, {c_star[3]:.8f})")
print(f"  sum = {c_star.sum():.10f}")
print(f"  chi^2   = {chi2_star:.6e}")
print(f"  dof (pre-registered) = {dof}  (5 obs - 4 params)")
print(f"  chi^2/dof            = {chi2_per_dof:.6e}    [GATE-DEFINING]")

print(f"\n  Alternative (sum-constrained) accounting:")
print(f"    dof = {dof_with_norm}  (5 obs - 3 free after sum constraint)")
print(f"    chi^2/dof = {chi2_per_dof_norm:.6e}")

# Observable predictions at c_star
pred_star = observables(c_star)
print("\n  Observable predictions at c*:")
for i, label in enumerate(obs_labels):
    sigma_dev = (pred_star[i] - targets[i]) / sigmas[i]
    print(f"    {label:>8s}: pred = {pred_star[i]:+.6e}, target = {targets[i]:+.6e}, "
          f"sigma-dev = {sigma_dev:+.3f}")

# =============================================================================
# CATEGORY-4 LOCK TEST
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Category-4 Lock Test")
print("=" * 78)

# Category-4 lock: one c_i > 0.9 (the spectral functional is essentially
# single-component).
max_c = np.max(c_star)
max_idx = np.argmax(c_star)
basis_names = ['constant (c_0)', 'sqrt (c_1)', 'exp (c_2)', 'compact (c_3)']

print(f"  max(c_i) = {max_c:.6f}  (component: {basis_names[max_idx]})")
print(f"  Category-4 lock threshold: c_i > 0.9")

category4_lock = max_c > 0.9
print(f"  Category-4 lock: {'YES' if category4_lock else 'NO'}")

if category4_lock:
    print(f"  -> Dominant component: {basis_names[max_idx]} at {max_c:.4f}")
    print(f"  -> Functional is essentially single-particle (category-4)")
else:
    print(f"  -> NO dominant component. Mixture is genuinely multi-functional.")
    # Report fractional weights
    print(f"  -> Fractional weights: {c_star / c_star.sum()}")

# =============================================================================
# GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Gate Verdict -- F-STAR-JOINT-74")
print("=" * 78)

# Gate: PASS if chi^2/dof < 1 AND category-4 lock
#       INFO if chi^2/dof in [1, 3] or category-4 lock partial
#       FAIL if chi^2/dof > 3
chi2dof_pass = chi2_per_dof < 1.0
chi2dof_info = 1.0 <= chi2_per_dof < 3.0

if chi2dof_pass and category4_lock:
    gate_verdict = "PASS"
    gate_reason = (
        f"chi^2/dof = {chi2_per_dof:.4e} < 1 AND category-4 lock confirmed "
        f"(dominant c_{max_idx} = {max_c:.4f} > 0.9, {basis_names[max_idx]})"
    )
elif chi2dof_pass and not category4_lock:
    gate_verdict = "INFO"
    gate_reason = (
        f"chi^2/dof = {chi2_per_dof:.4e} < 1 BUT category-4 lock fails "
        f"(max c_i = {max_c:.4f}). Genuine multi-functional mixture required."
    )
elif chi2dof_info:
    gate_verdict = "INFO"
    gate_reason = (
        f"chi^2/dof = {chi2_per_dof:.4e} in [1, 3]. Marginal joint fit. "
        f"Category-4 lock: {'yes' if category4_lock else 'no'}."
    )
else:
    gate_verdict = "FAIL"
    gate_reason = (
        f"chi^2/dof = {chi2_per_dof:.4e} > 3. 4-parameter family cannot "
        f"jointly match (n_s, m_H, r, w_0, alpha_s) scorecard."
    )

print(f"\n  GATE F-STAR-JOINT-74: {gate_verdict}")
print(f"  Reason: {gate_reason}")

# =============================================================================
# DIAGNOSTIC: IS THE FI STRUCTURE SWAMPING THE FIT?
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Diagnostic -- Functional-Independent Observable Contributions")
print("=" * 78)

# Break down chi^2 by observable to see which terms are fixed (FI) and which move
pred_star = observables(c_star)
chi2_components = ((pred_star - targets) / sigmas)**2
print("\n  chi^2 component breakdown at c*:")
for i, label in enumerate(obs_labels):
    print(f"    {label:>8s}: ((pred - target)/sigma)^2 = {chi2_components[i]:.6e}")
print(f"    TOTAL: {chi2_components.sum():.6e}")

# Which observables depend on c_i?
print("\n  Observable dependence on c_i:")
print("    n_s     : SCHEME-DEPENDENT  (through S_f shape at fold)")
print("    m_H     : SCHEME-DEPENDENT  (through f(0) = c_0 + c_2 + c_3)")
print("    r       : SCHEME-DEPENDENT  (r = 16 * eps_H, linked to n_s)")
print("    w_0     : FUNCTIONAL-INDEPENDENT  (Volovik partition, W1-J)")
print("    alpha_s : FUNCTIONAL-INDEPENDENT  (W1-A transfer function)")

# The structural limit: the FI contributions to chi^2 cannot be reduced by any choice of c
# Compute them once
c_fake = np.array([0.25, 0.25, 0.25, 0.25])  # any normalized c -> same FI obs
fi_pred_w0 = w_0_of_c(c_fake)
fi_pred_as = alpha_s_of_c(c_fake)
chi2_fi_floor_w0 = ((fi_pred_w0 - w0_target) / w0_sigma)**2  # (local)
chi2_fi_floor_as = ((fi_pred_as - alphas_target) / alphas_sigma)**2  # (local)
chi2_fi_floor = chi2_fi_floor_w0 + chi2_fi_floor_as  # (local)

print(f"\n  Chi^2 floor from FI observables (cannot be reduced by c):")
print(f"    w_0    : ({fi_pred_w0} - {w0_target})^2 / {w0_sigma}^2 = {chi2_fi_floor_w0:.6e}")
print(f"    alpha_s: ({fi_pred_as:.3e} - {alphas_target})^2 / {alphas_sigma}^2 = {chi2_fi_floor_as:.6e}")
print(f"    TOTAL FI floor: {chi2_fi_floor:.6e}")

# Chi^2 that CAN be reduced by choice of c (from n_s, m_H, r)
chi2_reducible = chi2_star - chi2_fi_floor
print(f"\n  Chi^2 reducible component (n_s, m_H, r): {chi2_reducible:.6e}")
print(f"  chi^2/dof (reducible only, dof=3-3=0): UNDEFINED  [saturated fit]")
print(f"  (The reducible part has 3 free params vs 3 scheme-dependent obs.)")

# =============================================================================
# STEP 11: UNPACK WHY chi^2 BEHAVES THIS WAY
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Structural Interpretation")
print("=" * 78)

# The n_s,m_H bifurcation from W1-C:
# - n_s matching wants c_1 ~ 0.9, c_2 ~ 0.088 (shape-dominated by sqrt)
# - m_H matching wants f(0) = (125.1/127.46)^2 = 0.963 (boundary value ~ 1)
# With 4 parameters and a normalization constraint, the fit has exactly
# the freedom to match 3 scheme-dependent observables.
# But w_0 and alpha_s are FI and CANNOT be changed by any c.
#
# So the minimum chi^2 IS the FI floor -- anything above is the residual
# in the scheme-dependent (n_s, m_H, r) triangle.

chi2_nsMHr = chi2_components[:3].sum()
print(f"\n  chi^2 breakdown:")
print(f"    FI floor (w_0, alpha_s)   : {chi2_fi_floor:.6e}")
print(f"    SD residual (n_s, m_H, r) : {chi2_nsMHr:.6e}")
print(f"    Total                      : {chi2_star:.6e}")

# At the mH-matching point: c_0 + c_2 + c_3 ~ 0.963 (from m_H = 125.1)
# At the ns-matching point: c_1 ~ 0.912, c_2 ~ 0.088 (from n_s = 0.9649)
# These are compatible IF c_0 ~ 0.875, c_1 ~ 0.125, c_2 ~ 0.088, c_3 ~ 0
# But sum = 1.088 violates normalization.
# With sum = 1 enforced: need to trade off.
# The fit chooses: keep n_s very close, sacrifice m_H (or vice versa).
# The category-4 lock test will tell us which.

# =============================================================================
# STEP 12: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 12: Save Data")
print("=" * 78)

np.savez('s74_f_star_joint.npz',
    gate_name='F-STAR-JOINT-74',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    c_star=c_star,
    c_labels=np.array(basis_names),
    chi2_star=chi2_star,
    chi2_per_dof=chi2_per_dof,
    dof=dof,
    dof_with_norm=dof_with_norm,
    chi2_per_dof_with_norm=chi2_per_dof_norm,
    category4_lock=category4_lock,
    max_c=max_c,
    max_idx=max_idx,
    dominant_component=basis_names[max_idx],
    pred_star=pred_star,
    targets=targets,
    sigmas=sigmas,
    obs_labels=np.array(obs_labels),
    chi2_components=chi2_components,
    chi2_fi_floor=chi2_fi_floor,
    chi2_reducible=chi2_reducible,
    c_baseline=c_baseline,
    chi2_baseline=chi2_base,
    mH_ref=mH_ref,
    alpha_s_FI=alpha_s_FI,
    w0_FI=w0_FW,
    N_modes_s66=N_modes_s66,
    n_s_target=ns_target,
    m_H_target=mH_target_val,
    r_target=r_target,
    w0_target=w0_target,
    alphas_target=alphas_target,
)
print("  Saved s74_f_star_joint.npz")

# =============================================================================
# STEP 13: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 13: Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: Best-fit c* bar chart
ax1 = fig.add_subplot(gs[0, 0])
colors_c = ['#a83232', '#3265a8', '#32a832', '#a8a832']  # (local)
bars = ax1.bar(range(4), c_star, color=colors_c, alpha=0.85, edgecolor='black', linewidth=1)
ax1.axhline(0.9, color='red', linestyle='--', alpha=0.7, label='cat-4 lock')
ax1.set_xticks(range(4))
ax1.set_xticklabels(['c_0\n(const)', 'c_1\n(sqrt)', 'c_2\n(exp)', 'c_3\n(comp)'], fontsize=10)
ax1.set_ylabel('c_i (best-fit)', fontsize=12)
ax1.set_title(f'F-STAR-JOINT-74: Best-Fit c*\nsum c = {c_star.sum():.4f}', fontsize=12)
ax1.set_ylim(-0.05, 1.05)
ax1.legend(fontsize=10)
for i, v in enumerate(c_star):
    ax1.text(i, v + 0.02, f'{v:.3f}', ha='center', fontsize=9)

# Panel 2: chi^2 components
ax2 = fig.add_subplot(gs[0, 1])
comp_colors = ['blue', 'red', 'green', 'purple', 'orange']  # (local)
bars2 = ax2.bar(range(5), chi2_components, color=comp_colors, alpha=0.85, edgecolor='black')
ax2.set_xticks(range(5))
ax2.set_xticklabels(obs_labels, fontsize=10)
ax2.set_ylabel('chi^2 component', fontsize=12)
ax2.set_yscale('log')
ax2.set_title(f'chi^2 decomposition\ntotal = {chi2_star:.2e}, dof={dof}', fontsize=12)
for i, v in enumerate(chi2_components):
    label = f'{v:.2e}'
    ax2.text(i, v * 1.5, label, ha='center', fontsize=8, rotation=45)

# Panel 3: Sigma deviations
ax3 = fig.add_subplot(gs[0, 2])
sigma_devs = (pred_star - targets) / sigmas
bars3 = ax3.bar(range(5), sigma_devs, color=comp_colors, alpha=0.85, edgecolor='black')
ax3.set_xticks(range(5))
ax3.set_xticklabels(obs_labels, fontsize=10)
ax3.set_ylabel('(pred - target) / sigma', fontsize=12)
ax3.set_title('Sigma-deviation per observable', fontsize=12)
ax3.axhline(0, color='black', linewidth=1)
ax3.axhline(1, color='red', linestyle='--', alpha=0.5, label='1 sigma')
ax3.axhline(-1, color='red', linestyle='--', alpha=0.5)
ax3.legend(fontsize=9)
for i, v in enumerate(sigma_devs):
    ax3.text(i, v + 0.05*np.sign(v) if abs(v) > 0.1 else 0.1,
             f'{v:+.2f}', ha='center', fontsize=9)

# Panel 4: Best-fit f*(x) vs basis
ax4 = fig.add_subplot(gs[1, 0])
x_plot = np.linspace(0.001, 5.0, 500)
f_star_best = (c_star[0]
               + c_star[1] * np.sqrt(x_plot)
               + c_star[2] * np.exp(-x_plot)
               + c_star[3] * np.where(x_plot < 1.0, (1.0 - x_plot)**4, 0.0))
ax4.plot(x_plot, np.sqrt(x_plot), 'b--', alpha=0.3, label='sqrt')
ax4.plot(x_plot, np.exp(-x_plot), 'r--', alpha=0.3, label='exp')
ax4.plot(x_plot, np.where(x_plot < 1.0, (1.0 - x_plot)**4, 0.0), 'g--', alpha=0.3,
         label='(1-x)_+^4')
ax4.plot(x_plot, np.ones_like(x_plot), 'y--', alpha=0.3, label='constant')
ax4.plot(x_plot, f_star_best, 'k-', linewidth=2.5,
         label=f'f*(x) [c={c_star.round(3)}]')
ax4.set_xlabel('x = lambda^2 / Lambda^2', fontsize=11)
ax4.set_ylabel('f(x)', fontsize=11)
ax4.set_title('Best-fit spectral functional f*(x)', fontsize=12)
ax4.set_xlim(0, 4)
ax4.set_ylim(-0.1, 2.5)
ax4.legend(fontsize=8, loc='upper left')
ax4.grid(alpha=0.3)

# Panel 5: chi^2 landscape along the sum-constraint simplex slice (c_1, c_2)
ax5 = fig.add_subplot(gs[1, 1])
# Fix c_0 = c_star[0], c_3 = c_star[3], scan c_1 and c_2 with sum constraint c_1+c_2 = 1 - c_0 - c_3
total_free = 1.0 - c_star[0] - c_star[3]  # (local)
if total_free > 0:
    c1_grid = np.linspace(0, total_free, 80)
    c2_grid = total_free - c1_grid
    chi2_slice = np.zeros_like(c1_grid)
    for k in range(len(c1_grid)):
        c_try = np.array([c_star[0], c1_grid[k], c2_grid[k], c_star[3]])
        chi2_slice[k] = chi_squared(c_try)
    ax5.semilogy(c1_grid, chi2_slice, 'b-', linewidth=2)
    ax5.axvline(c_star[1], color='red', linestyle='--', label=f'c_1* = {c_star[1]:.3f}')
    ax5.axhline(chi2_star, color='green', linestyle=':', label=f'chi^2* = {chi2_star:.2e}')
    ax5.set_xlabel(f'c_1 (with c_0={c_star[0]:.3f}, c_3={c_star[3]:.3f} fixed)', fontsize=10)
    ax5.set_ylabel('chi^2', fontsize=11)
    ax5.set_title('Chi^2 slice along c_1/c_2 trade-off', fontsize=12)
    ax5.legend(fontsize=9)
    ax5.grid(alpha=0.3)

# Panel 6: Category-4 lock summary
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary = (
    f'F-STAR-JOINT-74 RESULT\n'
    f'{"="*35}\n\n'
    f'Best-fit c*:\n'
    f'  c_0 (const)  = {c_star[0]:.6f}\n'
    f'  c_1 (sqrt)   = {c_star[1]:.6f}\n'
    f'  c_2 (exp)    = {c_star[2]:.6f}\n'
    f'  c_3 (comp)   = {c_star[3]:.6f}\n'
    f'  sum c_i      = {c_star.sum():.6f}\n\n'
    f'chi^2 = {chi2_star:.4e}\n'
    f'dof   = {dof} (pre-registered, 5-4)\n'
    f'chi^2/dof = {chi2_per_dof:.4e}\n\n'
    f'Category-4 lock: {"YES" if category4_lock else "NO"}\n'
    f'max c_i = {max_c:.4f}\n'
    f'dominant: {basis_names[max_idx]}\n\n'
    f'GATE VERDICT: {gate_verdict}\n\n'
    f'chi^2 floor (FI):     {chi2_fi_floor:.3e}\n'
    f'chi^2 reducible:      {chi2_reducible:.3e}\n'
    f'  n_s   : {chi2_components[0]:.3e}\n'
    f'  m_H   : {chi2_components[1]:.3e}\n'
    f'  r     : {chi2_components[2]:.3e}\n'
    f'  w_0   : {chi2_components[3]:.3e} (FI)\n'
    f'  alpha_s: {chi2_components[4]:.3e} (FI)\n'
)
ax6.text(0.01, 0.99, summary, transform=ax6.transAxes,
         fontsize=9, family='monospace', verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.suptitle('F-STAR-JOINT-74: 4-Parameter Spectral Functional Joint Fit',
             fontsize=14, fontweight='bold', y=0.995)

plt.savefig('s74_f_star_joint.png', dpi=150, bbox_inches='tight')
print("  Saved s74_f_star_joint.png")

# =============================================================================
# FINAL
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)
print(f"  Gate: F-STAR-JOINT-74")
print(f"  Verdict: {gate_verdict}")
print(f"  c* = ({c_star[0]:.4f}, {c_star[1]:.4f}, {c_star[2]:.4f}, {c_star[3]:.4f})")
print(f"  sum c_i = {c_star.sum():.6f}")
print(f"  chi^2 = {chi2_star:.4e}")
print(f"  chi^2/dof (dof=1, pre-registered) = {chi2_per_dof:.4e}")
print(f"  chi^2/dof (dof=2, with sum constraint) = {chi2_per_dof_norm:.4e}")
print(f"  Category-4 lock: {'YES' if category4_lock else 'NO'} (max c_i = {max_c:.4f})")
print(f"  Dominant: {basis_names[max_idx]}")
print("=" * 78)
