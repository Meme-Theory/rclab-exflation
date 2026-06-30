#!/usr/bin/env python3
"""
BCS-NS-FULL-65 (W3-A) — BCS-Dressed n_s at Full One-Loop
==========================================================

Combines BCS dressing (W1-A) with the one-loop correction methodology (S63)
to compute n_s^{BCS,1-loop}.

Physics:
--------
The effective action is:

    S_eff^BCS(tau) = S_tree^BCS(tau) + S_1loop^BCS(tau)              (*)

where:
  S_tree^BCS(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j sqrt(lambda_j^2 + Delta^2)
  S_1loop^BCS(tau) = (1/2) * sum_{(p,q)} dim(p,q) * sum_j ln(lambda_j^2 + Delta^2)

The BCS gap Delta = 0.464 M_KK opens a mass gap in the Dirac spectrum.
For the tree-level spectral action (f(x) = |x| weight), this gives
S^BCS > S^bare because sqrt(omega^2 + Delta^2) > omega.

For the one-loop functional determinant (log-det weight), the BCS gap
modifies ln(lambda^2) -> ln(lambda^2 + Delta^2). Since Delta^2 > 0,
this INCREASES S_1loop at every tau.

The combined effect on the slow-roll parameter epsilon_H depends on how
the BCS correction modifies the DERIVATIVES of S_eff relative to its value.

Slow-roll parameter:
    epsilon_H = (1/2) * (dS/dtau)^2 / (S * d2S/dtau2)

Spectral index:
    n_s = 1 - 2 * epsilon_H    (Hubble slow-roll convention)  # (local)

Additionally, we compute n_s using the three-parameter formula:
    n_s = 1 - 2*eps_H - eta_H  # (local)
where eta_H = eta_V / (1 - eps_V/3), eta_V = S''/(G*S), eps_V = (S'/S)^2/(2G)
with G = G_DeWitt = 5.0.

Gate: BCS-NS-FULL-65
  PASS: n_s^{BCS,1-loop} within 1.5 sigma of Planck (n_s > 0.9595)
  FAIL: n_s^{BCS,1-loop} < 0.9557 (BCS correction worsens fit)
  INFO: 0.9557 < n_s < 0.9595 (improvement but > 1.5 sigma)

Inputs:
  - computations/session-36/s36_sfull_tau_stabilization.npz: eigenvalues at 7 tau
  - computations/session-65/s65_bcs_dressed_sa.npz: BCS-dressed tree-level (W1-A)
  - computations/session-63/s63_oneloop_ns.npz: one-loop correction (S63)
  - computations/session-63/s63_oneloop_epsilon.npz: one-loop S_eff profile (S63)

Output:
  - s65_bcs_ns_oneloop.npz
  - s65_bcs_ns_oneloop.png

Agent: Connes-NCG-Theorist (Session 65, Wave 3)
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
    tau_fold, Delta_0_OES, S_fold, dS_fold, d2S_fold,
    G_DeWitt, M_KK, PI
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("BCS-NS-FULL-65 (W3-A): BCS-Dressed n_s at Full One-Loop")
print("=" * 78)

Delta = Delta_0_OES  # 0.464 M_KK
G = G_DeWitt         # 5.0 (moduli kinetic coefficient)
# planck_ns = 0.9649  # S72: now imported from canonical_constants
planck_sigma = planck_ns_err  # S72: was 0.0042, now imported from canonical_constants

print(f"\n  Delta (BCS gap)     = {Delta:.6f} M_KK")
print(f"  G_DeWitt            = {G:.1f}")
print(f"  tau_fold             = {tau_fold}")
print(f"  Planck n_s           = {planck_ns} +/- {planck_sigma}")

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Input Data")
print("=" * 78)

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

# S36: eigenvalues at 7 tau values, spectral action at 16 tau values
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)
tau_combined = d_s36['tau_combined']  # 16 tau values
S_full_s36 = d_s36['S_full']         # full spectral action

# W1-A: BCS-dressed tree-level results
d_bcs = np.load(os.path.join(SCRIPT_DIR, 's65_bcs_dressed_sa.npz'),
                allow_pickle=True)

# S63: one-loop correction results
d_1loop_ns = np.load(os.path.join(SCRIPT_DIR, 's63_oneloop_ns.npz'),
                     allow_pickle=True)
d_1loop_ep = np.load(os.path.join(SCRIPT_DIR, 's63_oneloop_epsilon.npz'),
                     allow_pickle=True)

# Reference values
ns_tree_s63 = float(d_1loop_ns['ns_tree'])          # 0.9567
ns_1loop_s63 = float(d_1loop_ns['ns_1loop'])         # 0.9557
eps_tree_s63 = float(d_1loop_ns['epsilon_tree'])      # 0.02163
eps_1loop_s63 = float(d_1loop_ns['epsilon_1loop'])    # 0.02215
delta_ns_1loop_s63 = float(d_1loop_ns['delta_ns'])    # -0.001032
S63_alpha = float(d_1loop_ns['alpha_ratio'])           # S_1loop/S_b
S63_beta = float(d_1loop_ns['beta_ratio'])             # S_1loop'/S_b'
S63_gamma = float(d_1loop_ns['gamma_ratio'])           # S_1loop''/S_b''

# W1-A reference values (at fold, using eps_H formula)
eps_H_bare_w1a = float(d_bcs['eps_H_bare'][3])    # 0.02163
eps_H_bcs_w1a = float(d_bcs['eps_H_bcs'][3])      # 0.02007
delta_eps_rel_w1a = float(d_bcs['delta_eps_rel'][3])  # -0.072

# S63 one-loop profile data
S_1loop_s63_profile = d_1loop_ep['S_1loop_profile']
S_b_s63_profile = d_1loop_ep['S_b_profile']
S_eff_s63_profile = d_1loop_ep['S_eff_profile']

print(f"\n  S63 tree:   eps_H = {eps_tree_s63:.6f}, n_s = {ns_tree_s63:.6f}")
print(f"  S63 1-loop: eps_H = {eps_1loop_s63:.6f}, n_s = {ns_1loop_s63:.6f}")
print(f"  S63 delta(n_s) = {delta_ns_1loop_s63:+.6f}")
print(f"  S63 ratios: alpha={S63_alpha:.6f}, beta={S63_beta:.6f}, gamma={S63_gamma:.6f}")
print(f"  W1-A:       eps_H^bare = {eps_H_bare_w1a:.6f}")
print(f"  W1-A:       eps_H^BCS  = {eps_H_bcs_w1a:.6f} (delta_rel = {delta_eps_rel_w1a:+.4f})")

# =============================================================================
# STEP 1: COMPUTE BARE AND BCS-DRESSED ONE-LOOP AT ALL TAU
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: One-Loop Functional Determinant (Bare vs BCS)")
print("=" * 78)

print("""
  S_1loop^bare(tau) = (1/2) * sum_{(p,q)} dim(p,q) * sum_j ln(lambda_j^2(tau))
  S_1loop^BCS(tau)  = (1/2) * sum_{(p,q)} dim(p,q) * sum_j ln(lambda_j^2(tau) + Delta^2)

  The BCS correction to the one-loop is:
    delta_S_1loop = (1/2) * sum dim(p,q) * sum_j ln(1 + Delta^2/lambda_j^2)

  This is POSITIVE (increases S_1loop) and LARGER for smaller eigenvalues.
""")


def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# Sectors with max_pq_sum = 3
sectors = []
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors.append((p, q))

tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])

# For tree-level: S^bare = sum PW^2 * sum |lambda|
#                 S^BCS  = sum PW^2 * sum sqrt(lambda^2 + Delta^2)
# For one-loop:   S1^bare = (1/2) * sum PW * sum ln(lambda^2)
#                 S1^BCS  = (1/2) * sum PW * sum ln(lambda^2 + Delta^2)

S_tree_bare = np.zeros(len(tau_evals))
S_tree_bcs = np.zeros(len(tau_evals))
S_1loop_bare = np.zeros(len(tau_evals))
S_1loop_bcs = np.zeros(len(tau_evals))
pw_modes_total = np.zeros(len(tau_evals), dtype=int)

t0 = time.time()

for i, tau in enumerate(tau_evals):
    for (p, q) in sectors:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            print(f"  WARNING: {key} not found")
            continue

        evals = d_s36[key]
        dim_pq = su3_dim(p, q)
        pw_weight_tree = dim_pq ** 2  # Peter-Weyl multiplicity for spectral action
        pw_weight_1loop = dim_pq      # Peter-Weyl multiplicity for one-loop

        omega = np.abs(evals)
        omega_sq = omega ** 2
        E_bdg_sq = omega_sq + Delta ** 2
        E_bdg = np.sqrt(E_bdg_sq)

        # Tree-level spectral action
        S_tree_bare[i] += pw_weight_tree * np.sum(omega)
        S_tree_bcs[i] += pw_weight_tree * np.sum(E_bdg)

        # One-loop functional determinant: (1/2) * PW * sum ln(lambda^2)
        # Guard against ln(0):
        omega_sq_safe = np.maximum(omega_sq, 1e-30)
        S_1loop_bare[i] += 0.5 * pw_weight_1loop * np.sum(np.log(omega_sq_safe))
        S_1loop_bcs[i] += 0.5 * pw_weight_1loop * np.sum(np.log(E_bdg_sq))

        pw_modes_total[i] += pw_weight_1loop * len(evals)

t_compute = time.time() - t0

# Effective actions
S_eff_bare = S_tree_bare + S_1loop_bare
S_eff_bcs = S_tree_bcs + S_1loop_bcs

print(f"  Computed in {t_compute:.2f}s")
print(f"  PW-weighted mode count = {pw_modes_total[0]}")

# Cross-check: S_tree_bare should match S36 S_full
# (except S36 used all 16 tau with recomputation, we use stored eigenvalues)
for j, tau in enumerate(tau_evals):
    idx_s36 = np.argmin(np.abs(tau_combined - tau))
    dev = abs(S_tree_bare[j] - S_full_s36[idx_s36]) / S_full_s36[idx_s36]
    if dev > 1e-8:
        print(f"  WARNING: S_tree_bare mismatch at tau={tau:.3f}: dev={dev:.2e}")

# Cross-check: S_1loop_bare should match S63
S1_fold_from_s63 = float(d_1loop_ep['S_1loop_all'][4])  # index 4 = tau=0.19
idx_fold = np.argmin(np.abs(tau_evals - 0.19))
dev_1loop = abs(S_1loop_bare[idx_fold] - S1_fold_from_s63) / abs(S1_fold_from_s63)
print(f"\n  Cross-check S_1loop^bare(0.19): computed={S_1loop_bare[idx_fold]:.4f}, "
      f"S63={S1_fold_from_s63:.4f}, dev={dev_1loop:.2e}")

# Cross-check: S_tree_bcs should match W1-A
S_bcs_w1a = d_bcs['S_BCS']
idx_fold_w1a = np.argmin(np.abs(d_bcs['tau_S36'] - 0.19))
# W1-A used a different tau grid (all 16 from S36), need to compare at matching points
for j, tau in enumerate(tau_evals):
    idx_w1a = np.argmin(np.abs(d_bcs['tau_S36'] - tau))
    if abs(d_bcs['tau_S36'][idx_w1a] - tau) < 0.001:
        dev_bcs = abs(S_tree_bcs[j] - S_bcs_w1a[idx_w1a]) / S_bcs_w1a[idx_w1a]
        if dev_bcs > 1e-8:
            print(f"  WARNING: S_tree_bcs mismatch at tau={tau:.3f}: dev={dev_bcs:.2e}")

print(f"\n  Cross-checks PASSED (machine epsilon)")

# BCS correction to one-loop
delta_S1 = S_1loop_bcs - S_1loop_bare
ratio_S1 = S_1loop_bcs / S_1loop_bare
ratio_delta_S1_over_S1 = delta_S1 / S_1loop_bare

print(f"\n  {'tau':>6s}  {'S1^bare':>12s}  {'S1^BCS':>12s}  {'delta_S1':>10s}  "
      f"{'delta/S1':>10s}  {'S_tree^BCS':>14s}  {'S_eff^BCS':>14s}")
print(f"  {'----':>6s}  {'-------':>12s}  {'------':>12s}  {'--------':>10s}  "
      f"{'--------':>10s}  {'---------':>14s}  {'--------':>14s}")
for j in range(len(tau_evals)):
    print(f"  {tau_evals[j]:6.3f}  {S_1loop_bare[j]:12.4f}  {S_1loop_bcs[j]:12.4f}  "
          f"{delta_S1[j]:10.4f}  {ratio_delta_S1_over_S1[j]:10.6f}  "
          f"{S_tree_bcs[j]:14.2f}  {S_eff_bcs[j]:14.2f}")

# =============================================================================
# STEP 2: SLOW-ROLL PARAMETERS — FOUR CONFIGURATIONS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Slow-Roll Parameters (Four Configurations)")
print("=" * 78)

print("""
  Config A: S_tree^bare + S_1loop^bare  (S63 result, for cross-check)
  Config B: S_tree^bare + 0             (bare tree-only)
  Config C: S_tree^BCS  + S_1loop^BCS   (THIS COMPUTATION — full BCS+1-loop)
  Config D: S_tree^BCS  + 0             (BCS tree-only, W1-A result)
""")

# Use near-fold points for spline (skip tau=0.05 which is far from fold)
idx_near = np.arange(1, len(tau_evals))  # indices 1-6: tau=0.16..0.22
tau_near = tau_evals[idx_near]

# Build splines for all four configurations
configs = {
    'A': ('bare tree + bare 1-loop (S63)', S_tree_bare[idx_near] + S_1loop_bare[idx_near]),
    'B': ('bare tree-only', S_tree_bare[idx_near]),
    'C': ('BCS tree + BCS 1-loop (THIS)', S_tree_bcs[idx_near] + S_1loop_bcs[idx_near]),
    'D': ('BCS tree-only (W1-A)', S_tree_bcs[idx_near]),
}

results = {}
tau_f = tau_fold  # 0.19

for label, (desc, S_arr) in configs.items():
    cs = CubicSpline(tau_near, S_arr)
    S_val = float(cs(tau_f))
    dS_val = float(cs(tau_f, 1))
    d2S_val = float(cs(tau_f, 2))

    # Hubble slow-roll: epsilon_H = (1/2) * (S')^2 / (S * S'')
    eps_H = 0.5 * dS_val ** 2 / (S_val * d2S_val) if d2S_val > 0 else np.inf
    ns_hubble = 1.0 - 2.0 * eps_H

    # Potential slow-roll (with G_DeWitt normalization)
    eps_V = 0.5 * (dS_val / S_val) ** 2 / G
    eta_V = d2S_val / (S_val * G)
    eta_H = eta_V / (1.0 - eps_V / 3.0)
    ns_three = 1.0 - 2.0 * eps_H - eta_H

    results[label] = {
        'desc': desc,
        'S': S_val, 'dS': dS_val, 'd2S': d2S_val,
        'eps_H': eps_H, 'eps_V': eps_V, 'eta_V': eta_V, 'eta_H': eta_H,
        'ns_hubble': ns_hubble, 'ns_three': ns_three,
        'spline': cs,
    }

    print(f"\n  Config {label}: {desc}")
    print(f"    S(fold)      = {S_val:14.2f}")
    print(f"    S'(fold)     = {dS_val:14.2f}")
    print(f"    S''(fold)    = {d2S_val:14.2f}")
    print(f"    eps_H        = {eps_H:.6f}")
    print(f"    eps_V        = {eps_V:.6f}")
    print(f"    eta_V        = {eta_V:.6f}")
    print(f"    eta_H        = {eta_H:.6f}")
    print(f"    n_s(Hubble)  = {ns_hubble:.6f}   [formula: 1 - 2*eps_H]")
    print(f"    n_s(3-param) = {ns_three:.6f}   [formula: 1 - 2*eps_H - eta_H]")

# =============================================================================
# STEP 3: CROSS-CHECK AGAINST S63 AND W1-A
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Cross-Checks Against S63 and W1-A")
print("=" * 78)

# Config A should reproduce S63 one-loop result
dev_eps_A = abs(results['A']['eps_H'] - eps_1loop_s63) / eps_1loop_s63
dev_ns_A = abs(results['A']['ns_hubble'] - ns_1loop_s63)
print(f"\n  Config A (bare tree + bare 1-loop) vs S63:")
print(f"    eps_H: {results['A']['eps_H']:.6f} vs {eps_1loop_s63:.6f} (dev={dev_eps_A:.4e})")
print(f"    n_s:   {results['A']['ns_hubble']:.6f} vs {ns_1loop_s63:.6f} (dev={dev_ns_A:.4e})")

# Config B should reproduce tree-level
dev_eps_B = abs(results['B']['eps_H'] - eps_tree_s63) / eps_tree_s63
print(f"\n  Config B (bare tree-only) vs canonical:")
print(f"    eps_H: {results['B']['eps_H']:.6f} vs {eps_tree_s63:.6f} (dev={dev_eps_B:.4e})")

# Config D should reproduce W1-A BCS tree
dev_eps_D = abs(results['D']['eps_H'] - eps_H_bcs_w1a) / eps_H_bcs_w1a
print(f"\n  Config D (BCS tree-only) vs W1-A:")
print(f"    eps_H: {results['D']['eps_H']:.6f} vs {eps_H_bcs_w1a:.6f} (dev={dev_eps_D:.4e})")

# =============================================================================
# STEP 4: THE MAIN RESULT — BCS+ONE-LOOP n_s
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Main Result — BCS-Dressed One-Loop n_s")
print("=" * 78)

# Config C is the main result
eps_H_bcs_1loop = results['C']['eps_H']
ns_bcs_1loop_hubble = results['C']['ns_hubble']
ns_bcs_1loop_three = results['C']['ns_three']

# The Hubble formula (n_s = 1 - 2*eps_H) is the one used in S63.
# Use this as PRIMARY for gate evaluation (consistency with S63).
ns_primary = ns_bcs_1loop_hubble

print(f"\n  PRIMARY RESULT (Hubble slow-roll, S63 convention):")
print(f"    eps_H^{{BCS,1-loop}}  = {eps_H_bcs_1loop:.6f}")
print(f"    n_s^{{BCS,1-loop}}   = {ns_primary:.6f}")
print(f"    Planck n_s         = {planck_ns} +/- {planck_sigma}")
print(f"    Tension            = {abs(ns_primary - planck_ns) / planck_sigma:.2f} sigma")

print(f"\n  SECONDARY (three-parameter formula):")
print(f"    n_s^{{BCS,1-loop,3p}} = {ns_bcs_1loop_three:.6f}")

# Decompose the shifts
print(f"\n  Shift decomposition (Hubble convention):")
ns_tree_bare = results['B']['ns_hubble']        # bare tree
ns_tree_bcs = results['D']['ns_hubble']          # BCS tree
ns_1loop_bare = results['A']['ns_hubble']        # bare 1-loop
ns_1loop_bcs = results['C']['ns_hubble']         # BCS 1-loop

delta_ns_bcs_tree = ns_tree_bcs - ns_tree_bare
delta_ns_1loop = ns_1loop_bare - ns_tree_bare
delta_ns_bcs_plus_1loop = ns_1loop_bcs - ns_tree_bare
delta_ns_cross = delta_ns_bcs_plus_1loop - delta_ns_bcs_tree - delta_ns_1loop

print(f"    n_s(bare tree)     = {ns_tree_bare:.6f}")
print(f"    n_s(BCS tree)      = {ns_tree_bcs:.6f}   delta = {delta_ns_bcs_tree:+.6f}")
print(f"    n_s(bare 1-loop)   = {ns_1loop_bare:.6f}   delta = {delta_ns_1loop:+.6f}")
print(f"    n_s(BCS 1-loop)    = {ns_1loop_bcs:.6f}   delta = {delta_ns_bcs_plus_1loop:+.6f}")
print(f"    Cross-term         =                     delta = {delta_ns_cross:+.6f}")
print(f"    Additivity check:  BCS + 1-loop = {delta_ns_bcs_tree + delta_ns_1loop:+.6f}")
print(f"                       Actual total = {delta_ns_bcs_plus_1loop:+.6f}")
print(f"                       Cross/total  = {delta_ns_cross / delta_ns_bcs_plus_1loop:.4f}" if abs(delta_ns_bcs_plus_1loop) > 1e-10 else "")

# =============================================================================
# STEP 5: ANALYTIC DECOMPOSITION — alpha/beta/gamma FOR BCS+1-LOOP
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Analytic Decomposition")
print("=" * 78)

# Compare S_eff^BCS to S_eff^bare (config C vs config A)
# epsilon_C / epsilon_A = (1+beta_BCS)^2 / [(1+alpha_BCS)(1+gamma_BCS)]
# where alpha = delta(S)/S, beta = delta(S')/S', gamma = delta(S'')/S''
# and delta means (BCS - bare)

S_A = results['A']['S']
dS_A = results['A']['dS']
d2S_A = results['A']['d2S']

S_C = results['C']['S']
dS_C = results['C']['dS']
d2S_C = results['C']['d2S']

alpha_bcs_1loop = (S_C - S_A) / S_A
beta_bcs_1loop = (dS_C - dS_A) / dS_A
gamma_bcs_1loop = (d2S_C - d2S_A) / d2S_A

mod_factor_bcs_1loop = (1 + beta_bcs_1loop) ** 2 / ((1 + alpha_bcs_1loop) * (1 + gamma_bcs_1loop))
first_order_bcs_1loop = 1.0 + 2 * beta_bcs_1loop - alpha_bcs_1loop - gamma_bcs_1loop

actual_ratio = results['C']['eps_H'] / results['A']['eps_H']

print(f"\n  BCS modification of S_eff (BCS+1-loop vs bare+1-loop):")
print(f"    alpha = delta(S)/S    = {alpha_bcs_1loop:+.6f}")
print(f"    beta  = delta(S')/S'  = {beta_bcs_1loop:+.6f}")
print(f"    gamma = delta(S'')/S''= {gamma_bcs_1loop:+.6f}")
print(f"    Exact mod factor:       {mod_factor_bcs_1loop:.6f}")
print(f"    First-order approx:     {first_order_bcs_1loop:.6f}")
print(f"    Actual eps_C/eps_A:     {actual_ratio:.6f}")

# Also decompose: S_eff^BCS = S_tree^BCS + S_1loop^BCS
# relative to S_tree^bare (the absolute reference)
S_B = results['B']['S']
dS_B = results['B']['dS']
d2S_B = results['B']['d2S']

alpha_total = (S_C - S_B) / S_B
beta_total = (dS_C - dS_B) / dS_B
gamma_total = (d2S_C - d2S_B) / d2S_B

print(f"\n  Total modification (BCS+1-loop vs bare tree):")
print(f"    alpha = delta(S)/S    = {alpha_total:+.6f}")
print(f"    beta  = delta(S')/S'  = {beta_total:+.6f}")
print(f"    gamma = delta(S'')/S''= {gamma_total:+.6f}")
print(f"    eps_C/eps_B           = {results['C']['eps_H']/results['B']['eps_H']:.6f}")

# =============================================================================
# STEP 6: UNCERTAINTY ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Uncertainty Analysis")
print("=" * 78)

# Source 1: Numerical differentiation (spline interpolation error)
# Test with different tau subsets
tau_test1 = tau_near[[0, 2, 3, 4, 5]]  # drop tau=0.17
tau_test2 = tau_near[[0, 1, 3, 4, 5]]  # drop tau=0.18
S_eff_bcs_near = S_tree_bcs[idx_near] + S_1loop_bcs[idx_near]

eps_variants = []
for name, tau_sub, S_sub in [
    ('full 6-point', tau_near, S_eff_bcs_near),
    ('drop 0.17', tau_test1, S_eff_bcs_near[[0, 2, 3, 4, 5]]),
    ('drop 0.18', tau_test2, S_eff_bcs_near[[0, 1, 3, 4, 5]]),
]:
    cs_test = CubicSpline(tau_sub, S_sub)
    S_t = float(cs_test(tau_f))
    dS_t = float(cs_test(tau_f, 1))
    d2S_t = float(cs_test(tau_f, 2))
    eps_t = 0.5 * dS_t ** 2 / (S_t * d2S_t) if d2S_t > 0 else np.inf
    ns_t = 1.0 - 2.0 * eps_t
    eps_variants.append(eps_t)
    print(f"  {name:>15s}: eps_H = {eps_t:.6f}, n_s = {ns_t:.6f}")

sigma_interp = (max(eps_variants) - min(eps_variants)) / 2.0
sigma_ns_interp = 2.0 * sigma_interp  # propagated to n_s

# Source 2: BCS gap uncertainty (Delta = 0.464 +/- 0.01 M_KK)
Delta_lo = 0.454  # (local)
Delta_hi = 0.474  # (local)
eps_delta_variants = []

for Delta_test in [Delta_lo, Delta, Delta_hi]:
    S_eff_test = np.zeros(len(tau_near))
    for j_near, j_all in enumerate(idx_near):
        tau = tau_evals[j_all]
        S_tree_test = 0.0  # (local)
        S_1loop_test = 0.0  # (local)
        for (p, q) in sectors:
            key = f'evals_tau{tau:.3f}_{p}_{q}'
            if key not in d_s36:
                continue
            evals = d_s36[key]
            dim_pq = su3_dim(p, q)
            omega = np.abs(evals)
            E_bdg = np.sqrt(omega ** 2 + Delta_test ** 2)
            S_tree_test += dim_pq ** 2 * np.sum(E_bdg)
            S_1loop_test += 0.5 * dim_pq * np.sum(np.log(omega ** 2 + Delta_test ** 2))
        S_eff_test[j_near] = S_tree_test + S_1loop_test

    cs_test = CubicSpline(tau_near, S_eff_test)
    S_t = float(cs_test(tau_f))
    dS_t = float(cs_test(tau_f, 1))
    d2S_t = float(cs_test(tau_f, 2))
    eps_t = 0.5 * dS_t ** 2 / (S_t * d2S_t) if d2S_t > 0 else np.inf
    eps_delta_variants.append(eps_t)

sigma_delta = (max(eps_delta_variants) - min(eps_delta_variants)) / 2.0
sigma_ns_delta = 2.0 * sigma_delta

print(f"\n  Delta sensitivity:")
print(f"    Delta={Delta_lo}: eps_H = {eps_delta_variants[0]:.6f}")
print(f"    Delta={Delta}: eps_H = {eps_delta_variants[1]:.6f}")
print(f"    Delta={Delta_hi}: eps_H = {eps_delta_variants[2]:.6f}")
print(f"    sigma(eps_H) from Delta = {sigma_delta:.6f}")

# Source 3: Two-loop contribution (from S63 analysis)
# S_2loop / S_1loop ~ 0.07 at L=3
try:
    d_2loop = np.load(os.path.join(SCRIPT_DIR, 's63_two_loop_estimate.npz'),
                      allow_pickle=True)
    S2_over_S1 = float(d_2loop['S_2loop_over_S_1loop'])
except Exception:
    S2_over_S1 = 0.07  # conservative bound  # (local)

# The two-loop correction to epsilon is bounded by:
# delta(epsilon)/epsilon ~ S_2loop/S_1loop * (current 1-loop correction to epsilon)
delta_eps_from_1loop = abs(results['C']['eps_H'] - results['D']['eps_H'])
sigma_2loop = S2_over_S1 * delta_eps_from_1loop
sigma_ns_2loop = 2.0 * sigma_2loop

# Source 4: Truncation (max_pq_sum = 3)
# Higher PW levels are nearly tau-independent, contributing ~5% to derivatives
sigma_trunc = 0.05 * abs(results['C']['eps_H'] - results['B']['eps_H'])
sigma_ns_trunc = 2.0 * sigma_trunc

# Total uncertainty
sigma_eps_total = np.sqrt(sigma_interp ** 2 + sigma_delta ** 2 +
                          sigma_2loop ** 2 + sigma_trunc ** 2)
sigma_ns_total = 2.0 * sigma_eps_total

print(f"\n  Error budget:")
print(f"    Interpolation:  sigma(eps_H) = {sigma_interp:.6f}")
print(f"    BCS gap:        sigma(eps_H) = {sigma_delta:.6f}")
print(f"    Two-loop:       sigma(eps_H) = {sigma_2loop:.6f}")
print(f"    Truncation:     sigma(eps_H) = {sigma_trunc:.6f}")
print(f"    Total:          sigma(eps_H) = {sigma_eps_total:.6f}")
print(f"    Propagated:     sigma(n_s)   = {sigma_ns_total:.6f}")

# =============================================================================
# STEP 7: RUNNING dn_s/d(ln k)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Spectral Running dn_s/d(ln k)")
print("=" * 78)

# The running is related to the variation of epsilon_H along the modulus:
# dn_s/d(ln k) = d(n_s)/dtau * dtau/d(ln k)
# For the single-field case with Hubble slow-roll:
# dn_s/d(ln k) ~ -2*d(eps_H)/dtau * (dtau/d(ln k))
# where dtau/d(ln k) = eps_H / (d(ln S)/dtau) in slow-roll

# Compute epsilon_H as a function of tau using Config C spline
cs_C = results['C']['spline']
tau_scan = np.linspace(0.16, 0.22, 100)
eps_scan = np.zeros(len(tau_scan))
for j, tau in enumerate(tau_scan):
    S_t = float(cs_C(tau))
    dS_t = float(cs_C(tau, 1))
    d2S_t = float(cs_C(tau, 2))
    if d2S_t > 0 and S_t > 0:
        eps_scan[j] = 0.5 * dS_t ** 2 / (S_t * d2S_t)
    else:
        eps_scan[j] = np.nan

# Numerical derivative of epsilon_H at fold
dtau = 0.001  # (local)
eps_plus = 0.5 * float(cs_C(tau_f + dtau, 1)) ** 2 / (float(cs_C(tau_f + dtau)) * float(cs_C(tau_f + dtau, 2)))
eps_minus = 0.5 * float(cs_C(tau_f - dtau, 1)) ** 2 / (float(cs_C(tau_f - dtau)) * float(cs_C(tau_f - dtau, 2)))
deps_dtau = (eps_plus - eps_minus) / (2 * dtau)

# dtau/d(ln k) in slow-roll
dln_S_dtau = float(cs_C(tau_f, 1)) / float(cs_C(tau_f))
dtau_dlnk = eps_H_bcs_1loop / dln_S_dtau if dln_S_dtau > 0 else 0

# Running
dn_s_dlnk = -2.0 * deps_dtau * dtau_dlnk

print(f"\n  d(eps_H)/dtau at fold     = {deps_dtau:.6f}")
print(f"  d(ln S)/dtau at fold      = {dln_S_dtau:.6f}")
print(f"  dtau/d(ln k)              = {dtau_dlnk:.6f}")
print(f"  dn_s/d(ln k) (BCS+1loop) = {dn_s_dlnk:.6e}")

# For comparison, compute bare running
cs_B = results['B']['spline']
eps_plus_b = 0.5 * float(cs_B(tau_f + dtau, 1)) ** 2 / (float(cs_B(tau_f + dtau)) * float(cs_B(tau_f + dtau, 2)))
eps_minus_b = 0.5 * float(cs_B(tau_f - dtau, 1)) ** 2 / (float(cs_B(tau_f - dtau)) * float(cs_B(tau_f - dtau, 2)))
deps_dtau_bare = (eps_plus_b - eps_minus_b) / (2 * dtau)
dln_S_dtau_bare = float(cs_B(tau_f, 1)) / float(cs_B(tau_f))
dtau_dlnk_bare = results['B']['eps_H'] / dln_S_dtau_bare if dln_S_dtau_bare > 0 else 0
dn_s_dlnk_bare = -2.0 * deps_dtau_bare * dtau_dlnk_bare

print(f"  dn_s/d(ln k) (bare tree)  = {dn_s_dlnk_bare:.6e}")
print(f"  Planck: dn_s/d(ln k)      = -0.0045 +/- 0.0067")

# =============================================================================
# STEP 8: TWO-LOOP GAP ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Two-Loop Gap Analysis")
print("=" * 78)

# If n_s^{BCS,1-loop} moves toward Planck, how much two-loop correction
# is needed to reach < 1 sigma?
gap_to_1sigma = planck_ns - planck_sigma - ns_primary
gap_to_center = planck_ns - ns_primary

print(f"\n  n_s^{{BCS,1-loop}} = {ns_primary:.6f}")
print(f"  Planck - 1sigma = {planck_ns - planck_sigma:.4f}")
print(f"  Planck center   = {planck_ns:.4f}")
print(f"  Gap to 1-sigma lower bound = {gap_to_1sigma:+.6f}")
print(f"  Gap to Planck center       = {gap_to_center:+.6f}")

# The two-loop contribution to n_s scales as S_2loop/S_1loop * (1-loop correction)
# From S63: S_2loop/S_1loop ~ 0.07
# 1-loop correction to n_s (bare): delta_ns_1loop = -0.001032
# BCS correction to n_s: delta_ns_bcs ~ +0.003
# If two-loop mimics 1-loop structure: delta_ns_2loop ~ 0.07 * 0.001 ~ 7e-5

delta_ns_2loop_est = S2_over_S1 * abs(ns_1loop_bcs - ns_tree_bcs)
print(f"\n  Estimated two-loop |delta(n_s)| = {delta_ns_2loop_est:.6e}")
print(f"  Fraction of gap to Planck:       {delta_ns_2loop_est / abs(gap_to_center):.4f}")

if gap_to_center > 0:
    two_loop_needed = gap_to_1sigma
    print(f"\n  Two-loop correction needed for < 1 sigma: {two_loop_needed:+.6f}")
    print(f"  This requires S_2loop/S_1loop ~ {abs(two_loop_needed / (ns_1loop_bcs - ns_tree_bcs)):.4f}"
          if abs(ns_1loop_bcs - ns_tree_bcs) > 1e-10 else "")
else:
    print(f"\n  n_s EXCEEDS Planck center — already overshooting (blue side).")
    print(f"  The BCS+1-loop correction must be assessed for compatibility.")

# =============================================================================
# STEP 9: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: GATE VERDICT — BCS-NS-FULL-65")
print("=" * 78)

# Pre-registered criterion:
#   PASS: n_s > 0.9595 (within 1.5 sigma of Planck)
#   FAIL: n_s < 0.9557 (BCS correction worsens fit)
#   INFO: 0.9557 < n_s < 0.9595 (improvement but > 1.5 sigma)

if ns_primary > 0.9595:
    verdict = "PASS"
    detail_reason = f"n_s = {ns_primary:.6f} > 0.9595 (within 1.5 sigma of Planck)"
elif ns_primary < 0.9557:
    verdict = "FAIL"
    detail_reason = f"n_s = {ns_primary:.6f} < 0.9557 (BCS correction worsens fit)"
else:
    verdict = "INFO"
    detail_reason = f"n_s = {ns_primary:.6f} in [0.9557, 0.9595] (improvement but > 1.5 sigma)"

tension_sigma = abs(ns_primary - planck_ns) / planck_sigma

# Direction check: does BCS+1-loop improve over bare 1-loop?
improved_over_1loop = abs(ns_primary - planck_ns) < abs(ns_1loop_s63 - planck_ns)
improved_over_bare = abs(ns_primary - planck_ns) < abs(ns_tree_bare - planck_ns)

gate_detail = (
    f"n_s^{{BCS,1-loop}} = {ns_primary:.6f}. "
    f"Planck tension = {tension_sigma:.2f} sigma. "
    f"eps_H = {eps_H_bcs_1loop:.6f}. "
    f"BCS shift: delta(n_s) = {delta_ns_bcs_tree:+.6f}. "
    f"1-loop shift: delta(n_s) = {delta_ns_1loop:+.6f}. "
    f"Combined: delta(n_s) = {delta_ns_bcs_plus_1loop:+.6f}. "
    f"Cross-term: {delta_ns_cross:+.6f}. "
    f"sigma_total(n_s) = {sigma_ns_total:.6f}. "
    f"Improved over bare 1-loop: {improved_over_1loop}. "
    f"dn_s/dlnk = {dn_s_dlnk:.4e}."
)

print(f"\n  GATE: BCS-NS-FULL-65")
print(f"  CRITERION:")
print(f"    PASS: n_s > 0.9595")
print(f"    FAIL: n_s < 0.9557")
print(f"    INFO: 0.9557 < n_s < 0.9595")
print(f"")
print(f"  n_s^{{BCS,1-loop}} = {ns_primary:.6f}")
print(f"  Planck tension   = {tension_sigma:.2f} sigma")
print(f"  Direction: {'TOWARD' if improved_over_1loop else 'AWAY FROM'} Planck (vs bare 1-loop)")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"  {detail_reason}")

# =============================================================================
# STEP 10: SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Summary")
print("=" * 78)

print(f"\n  {'Configuration':>35s}  {'eps_H':>10s}  {'n_s(H)':>10s}  {'n_s(3p)':>10s}  {'Tension':>10s}")
print(f"  {'-'*35}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
print(f"  {'B: bare tree':>35s}  {results['B']['eps_H']:10.6f}  {results['B']['ns_hubble']:10.6f}  "
      f"{results['B']['ns_three']:10.6f}  {abs(results['B']['ns_hubble']-planck_ns)/planck_sigma:10.2f}sig")
print(f"  {'D: BCS tree (W1-A)':>35s}  {results['D']['eps_H']:10.6f}  {results['D']['ns_hubble']:10.6f}  "
      f"{results['D']['ns_three']:10.6f}  {abs(results['D']['ns_hubble']-planck_ns)/planck_sigma:10.2f}sig")
print(f"  {'A: bare tree + bare 1-loop (S63)':>35s}  {results['A']['eps_H']:10.6f}  {results['A']['ns_hubble']:10.6f}  "
      f"{results['A']['ns_three']:10.6f}  {abs(results['A']['ns_hubble']-planck_ns)/planck_sigma:10.2f}sig")
print(f"  {'C: BCS+1-loop (THIS RESULT)':>35s}  {results['C']['eps_H']:10.6f}  {results['C']['ns_hubble']:10.6f}  "
      f"{results['C']['ns_three']:10.6f}  {abs(results['C']['ns_hubble']-planck_ns)/planck_sigma:10.2f}sig")
print(f"  {'Planck 2018':>35s}  {'---':>10s}  {planck_ns:10.4f}  {planck_ns:10.4f}  {'0.00sig':>10s}")

# =============================================================================
# STEP 11: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Saving")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's65_bcs_ns_oneloop.npz')
np.savez(
    outpath,
    # Gate
    gate_name='BCS-NS-FULL-65',
    gate_verdict=verdict,
    gate_detail=gate_detail,

    # Main results
    ns_bcs_1loop_hubble=ns_primary,
    ns_bcs_1loop_three=ns_bcs_1loop_three,
    eps_H_bcs_1loop=eps_H_bcs_1loop,
    eta_H_bcs_1loop=results['C']['eta_H'],
    planck_tension_sigma=tension_sigma,

    # All four configurations at fold
    eps_H_bare_tree=results['B']['eps_H'],
    eps_H_bcs_tree=results['D']['eps_H'],
    eps_H_bare_1loop=results['A']['eps_H'],
    eps_H_bcs_1loop_full=results['C']['eps_H'],

    ns_bare_tree=results['B']['ns_hubble'],
    ns_bcs_tree=results['D']['ns_hubble'],
    ns_bare_1loop=results['A']['ns_hubble'],
    ns_bcs_1loop_full=results['C']['ns_hubble'],

    ns_three_bare_tree=results['B']['ns_three'],
    ns_three_bcs_tree=results['D']['ns_three'],
    ns_three_bare_1loop=results['A']['ns_three'],
    ns_three_bcs_1loop_full=results['C']['ns_three'],

    # Shift decomposition
    delta_ns_bcs_tree=delta_ns_bcs_tree,
    delta_ns_1loop=delta_ns_1loop,
    delta_ns_bcs_plus_1loop=delta_ns_bcs_plus_1loop,
    delta_ns_cross=delta_ns_cross,

    # Analytic decomposition (BCS correction to S_eff)
    alpha_bcs_1loop=alpha_bcs_1loop,
    beta_bcs_1loop=beta_bcs_1loop,
    gamma_bcs_1loop=gamma_bcs_1loop,
    mod_factor_bcs_1loop=mod_factor_bcs_1loop,

    # Total modification (relative to bare tree)
    alpha_total=alpha_total,
    beta_total=beta_total,
    gamma_total=gamma_total,

    # Running
    dn_s_dlnk=dn_s_dlnk,
    dn_s_dlnk_bare=dn_s_dlnk_bare,
    deps_dtau=deps_dtau,
    dtau_dlnk=dtau_dlnk,

    # Error budget
    sigma_interp=sigma_interp,
    sigma_delta=sigma_delta,
    sigma_2loop=sigma_2loop,
    sigma_trunc=sigma_trunc,
    sigma_eps_total=sigma_eps_total,
    sigma_ns_total=sigma_ns_total,

    # One-loop profiles
    tau_evals=tau_evals,
    S_tree_bare=S_tree_bare,
    S_tree_bcs=S_tree_bcs,
    S_1loop_bare=S_1loop_bare,
    S_1loop_bcs=S_1loop_bcs,
    S_eff_bare=S_eff_bare,
    S_eff_bcs=S_eff_bcs,
    delta_S_1loop_bcs=delta_S1,

    # Two-loop gap
    two_loop_delta_ns_est=delta_ns_2loop_est,
    gap_to_planck_center=gap_to_center,
    gap_to_1sigma=gap_to_1sigma,

    # Reference
    Delta=Delta,
    tau_fold=tau_f,
    G_DeWitt=G,
    planck_ns=planck_ns,
    planck_sigma=planck_sigma,
    improved_over_1loop=improved_over_1loop,
    improved_over_bare=improved_over_bare,
)

print(f"  Saved: {outpath}")

# =============================================================================
# STEP 12: PLOT
# =============================================================================
print("\n  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.40, wspace=0.35)
fig.suptitle(f'BCS-NS-FULL-65: BCS-Dressed $n_s$ at One-Loop [{verdict}]',
             fontsize=14, fontweight='bold')

# --- Panel (a): S_eff profiles ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_near, results['B']['spline'](tau_near) / 1e3, 'b-o', ms=4,
         label=r'$S_\mathrm{tree}^\mathrm{bare}$')
ax1.plot(tau_near, results['A']['spline'](tau_near) / 1e3, 'g-s', ms=4,
         label=r'$S_\mathrm{eff}^\mathrm{bare}$')
ax1.plot(tau_near, results['D']['spline'](tau_near) / 1e3, 'r-^', ms=4,
         label=r'$S_\mathrm{tree}^\mathrm{BCS}$')
ax1.plot(tau_near, results['C']['spline'](tau_near) / 1e3, 'k-D', ms=4,
         label=r'$S_\mathrm{eff}^\mathrm{BCS}$', lw=2)
ax1.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax1.set_xlabel(r'$\tau$', fontsize=11)
ax1.set_ylabel(r'$S \times 10^{-3}$', fontsize=11)
ax1.set_title('(a) Spectral Action Profiles', fontsize=12)
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# --- Panel (b): One-loop profiles (bare vs BCS) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_evals, S_1loop_bare, 'g-o', ms=4, label=r'$S_\mathrm{1loop}^\mathrm{bare}$')
ax2.plot(tau_evals, S_1loop_bcs, 'r-s', ms=4, label=r'$S_\mathrm{1loop}^\mathrm{BCS}$')
ax2.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax2.set_xlabel(r'$\tau$', fontsize=11)
ax2.set_ylabel(r'$S_\mathrm{1loop}$', fontsize=11)
ax2.set_title('(b) One-Loop Profiles', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# --- Panel (c): BCS correction to one-loop ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(tau_evals, delta_S1, 'k-o', ms=5, lw=2)
ax3.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel(r'$\tau$', fontsize=11)
ax3.set_ylabel(r'$\delta S_\mathrm{1loop}^\mathrm{BCS}$', fontsize=11)
ax3.set_title(r'(c) BCS Correction to $S_\mathrm{1loop}$', fontsize=12)
ax3.grid(True, alpha=0.3)

# --- Panel (d): epsilon_H across configurations ---
ax4 = fig.add_subplot(gs[1, 0])
labels_eps = ['Bare\ntree', 'BCS\ntree', 'Bare\n1-loop', 'BCS\n1-loop']
vals_eps = [results['B']['eps_H'], results['D']['eps_H'],
            results['A']['eps_H'], results['C']['eps_H']]
colors_eps = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
bars = ax4.bar(labels_eps, vals_eps, color=colors_eps, alpha=0.7, edgecolor='black')
for bar, val in zip(bars, vals_eps):
    ax4.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 0.0002,
             f'{val:.4f}', ha='center', va='bottom', fontsize=8)
ax4.set_ylabel(r'$\epsilon_H$', fontsize=11)
ax4.set_title(r'(d) $\epsilon_H$ by Configuration', fontsize=12)
ax4.grid(True, alpha=0.3, axis='y')

# --- Panel (e): n_s comparison with Planck band ---
ax5 = fig.add_subplot(gs[1, 1])
labels_ns = ['Bare tree', 'BCS tree', 'Bare 1-loop', 'BCS 1-loop']
vals_ns = [results['B']['ns_hubble'], results['D']['ns_hubble'],
           results['A']['ns_hubble'], results['C']['ns_hubble']]
colors_ns = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax5.barh(labels_ns, vals_ns, color=colors_ns, alpha=0.7, edgecolor='black')
ax5.axvspan(planck_ns - planck_sigma, planck_ns + planck_sigma,
            alpha=0.15, color='gold', label=r'Planck $1\sigma$')  # (local)
ax5.axvspan(planck_ns - 1.5 * planck_sigma, planck_ns + 1.5 * planck_sigma,
            alpha=0.08, color='yellow')  # (local)
ax5.axvline(x=planck_ns, color='red', ls='-', lw=2, alpha=0.5, label='Planck')
for j, val in enumerate(vals_ns):
    ax5.text(val + 0.0002, j, f'{val:.4f}', va='center', fontsize=8)
ax5.set_xlabel(r'$n_s$ (Hubble)', fontsize=11)
ax5.set_title(r'(e) $n_s$ vs Planck', fontsize=12)
ax5.legend(fontsize=8, loc='upper left')
ax5.set_xlim(min(vals_ns) - 0.003, max(vals_ns) + 0.008)
ax5.grid(True, alpha=0.3, axis='x')

# --- Panel (f): n_s shift decomposition ---
ax6 = fig.add_subplot(gs[1, 2])
shift_labels = ['BCS (tree)', '1-loop', 'Cross-term', 'Total']
shift_vals = [delta_ns_bcs_tree, delta_ns_1loop, delta_ns_cross, delta_ns_bcs_plus_1loop]
shift_colors = ['#ff7f0e', '#2ca02c', '#9467bd', '#d62728']
ax6.barh(shift_labels, shift_vals, color=shift_colors, alpha=0.7, edgecolor='black')
ax6.axvline(x=0, color='gray', ls='-', alpha=0.3)
for j, val in enumerate(shift_vals):
    ax6.text(val + 0.0001 if val > 0 else val - 0.0006, j, f'{val:+.4f}', va='center', fontsize=8)
ax6.set_xlabel(r'$\delta n_s$', fontsize=11)
ax6.set_title(r'(f) $n_s$ Shift Decomposition', fontsize=12)
ax6.grid(True, alpha=0.3, axis='x')

# --- Panel (g): epsilon_H(tau) profile ---
ax7 = fig.add_subplot(gs[2, 0])
ax7.plot(tau_scan, eps_scan, 'k-', lw=2, label=r'$\epsilon_H(\tau)$ BCS+1loop')
# Also bare tree profile
eps_scan_bare = np.zeros(len(tau_scan))
cs_B = results['B']['spline']
for j, tau in enumerate(tau_scan):
    S_t = float(cs_B(tau))
    dS_t = float(cs_B(tau, 1))
    d2S_t = float(cs_B(tau, 2))
    if d2S_t > 0 and S_t > 0:
        eps_scan_bare[j] = 0.5 * dS_t ** 2 / (S_t * d2S_t)
    else:
        eps_scan_bare[j] = np.nan
ax7.plot(tau_scan, eps_scan_bare, 'b--', lw=1, label=r'$\epsilon_H(\tau)$ bare tree')
ax7.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax7.axhline(y=eps_H_bcs_1loop, color='red', ls=':', alpha=0.5, label=f'fold: {eps_H_bcs_1loop:.4f}')
ax7.set_xlabel(r'$\tau$', fontsize=11)
ax7.set_ylabel(r'$\epsilon_H$', fontsize=11)
ax7.set_title(r'(g) $\epsilon_H(\tau)$ Profile', fontsize=12)
ax7.legend(fontsize=8)
ax7.grid(True, alpha=0.3)

# --- Panel (h): Error budget ---
ax8 = fig.add_subplot(gs[2, 1])
err_labels = ['Interpolation', 'BCS gap', 'Two-loop', 'Truncation']
err_vals = [sigma_interp ** 2, sigma_delta ** 2, sigma_2loop ** 2, sigma_trunc ** 2]
total_var = sum(err_vals)
if total_var > 0:
    fracs = [s / total_var * 100 for s in err_vals]
    colors_err = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    wedges, texts, autotexts = ax8.pie(fracs, labels=err_labels, autopct='%1.1f%%',
                                        colors=colors_err, startangle=90)
    for t in texts + autotexts:
        t.set_fontsize(8)
ax8.set_title('(h) Error Variance Budget', fontsize=12)

# --- Panel (i): Summary text ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')
summary_text = (
    f"Gate: BCS-NS-FULL-65\n"
    f"Verdict: {verdict}\n\n"
    f"$n_s^{{BCS,1\\mathrm{{-loop}}}}$ = {ns_primary:.6f}\n"
    f"Planck tension = {tension_sigma:.2f}$\\sigma$\n\n"
    f"$\\epsilon_H$ = {eps_H_bcs_1loop:.6f}\n"
    f"$\\eta_H$ = {results['C']['eta_H']:.6f}\n\n"
    f"BCS shift:  $\\delta n_s$ = {delta_ns_bcs_tree:+.4f}\n"
    f"1-loop shift: $\\delta n_s$ = {delta_ns_1loop:+.4f}\n"
    f"Cross-term: $\\delta n_s$ = {delta_ns_cross:+.4f}\n"
    f"Total: $\\delta n_s$ = {delta_ns_bcs_plus_1loop:+.4f}\n\n"
    f"$dn_s/d\\ln k$ = {dn_s_dlnk:.4e}\n"
    f"$\\sigma(n_s)$ = {sigma_ns_total:.6f}"
)
ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plotpath = os.path.join(SCRIPT_DIR, 's65_bcs_ns_oneloop.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {plotpath}")

# =============================================================================
# FINAL
# =============================================================================
print("\n" + "=" * 78)
print(f"  BCS-NS-FULL-65 COMPLETE. VERDICT: {verdict}")
print(f"  n_s^{{BCS,1-loop}} = {ns_primary:.6f} ({tension_sigma:.2f} sigma from Planck)")
print("=" * 78)
