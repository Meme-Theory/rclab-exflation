#!/usr/bin/env python3
"""
NS-1LOOP-SPECTRAL-74 (W1-I, Session 74 Wave 1 Batch 2)
=======================================================

1-Loop Coleman-Weinberg correction to d^2 S / dtau^2 at the fold with a
tau-dependent BCS gap Delta(tau), and the resulting shift in n_s.

Physics
-------
The substrate picture: n_s is the logarithmic derivative of the spectral
action at the fold, NOT a curvature perturbation tuned by an inflaton
potential. The tree-level spectral action S_tree(tau) gives n_s = 0.9567.
The 1-loop Coleman-Weinberg correction V_CW(tau) comes from the BCS gap
Delta(tau) opening at the fold. The KEY difference from S66 BCS-CW:

    S66: Fixed Delta = Delta_0_OES = 0.464 M_KK for all tau
    THIS: Delta(tau) = -0.2441*tau + 0.5118 M_KK (from S73A JJ-KAPPA-MAP)

The tau-dependent Delta introduces an additional contribution in
d^2 V_CW / dtau^2 through (dDelta/dtau)^2 and higher derivatives. This is
precisely the spectral-action-specific 1-loop correction requested by
framework chapter sec 10.5.

The standard 4D Coleman-Weinberg (MSbar):
    V_CW(tau) = (1/(64*pi^2)) * sum_n d_n * M_n^4(tau) * (ln(M_n^2(tau)/mu^2) - 3/2)
where:
    M_n^2(tau) = lambda_n^2(tau) + Delta(tau)^2
    d_n = dim(p,q)^2 (Peter-Weyl degeneracy)
    mu = M_KK (renormalization scale)

Then:
    S_1loop(tau) = S_tree(tau) + V_CW(tau)
    n_s^{1loop} = 1 - 2*eps_H where eps_H = (1/2)*(S')^2/(S*S'')

Pre-registered gate (NS-1LOOP-SPECTRAL-74)
-------------------------------------------
PASS: 1-loop n_s in [0.9607, 0.9691] (Planck 1-sigma)
INFO: 1-loop n_s in [0.9565, 0.9733] (2-sigma)
FAIL: 1-loop correction moves n_s away from Planck or leaves it outside 2-sigma

Cross-reference W1-A (TRANSFER-FUNCTION-74): returned n_s(k_pivot) = 1.000000,
which means the red tilt of Planck n_s = 0.9649 CANNOT come from the transfer
function. This computation is the PRIMARY SURVIVING ROUTE for generating the
red tilt.

Cross-reference W1-C (L-MAX-ZETA-REGULARIZATION-74): closed the direct spectral
sum route. This script uses the a_k canonical values from S42/S66, not Route A
zeta values.

Agent: Connes-NCG-Theorist (Session 74, Wave 1 Batch 2)
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
    G_DeWitt, M_KK, PI, planck_ns, planck_ns_err,
    a0_fold, a2_fold, a4_fold,
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("NS-1LOOP-SPECTRAL-74 (W1-I): Spectral-Action 1-Loop at Fold")
print("=" * 78)

# Renormalization scale (in M_KK units)
mu_central = 1.0  # (local) mu = M_KK

# Renormalization scale variations for scheme uncertainty
mu_low = 0.5  # (local)
mu_high = 2.0  # (local)

print(f"\n  tau_fold            = {tau_fold}")
print(f"  Planck n_s          = {planck_ns} +/- {planck_ns_err}")
print(f"  Renormalization mu  = {mu_central} M_KK (central)")
print(f"  Tree-level targets  : S_fold={S_fold:.2f}, dS_fold={dS_fold:.2f}, d2S_fold={d2S_fold:.2f}")
print(f"  Canonical a_k       : a0={a0_fold}, a2={a2_fold:.2f}, a4={a4_fold:.2f}")

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Input Data")
print("=" * 78)

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

# S36 eigenvalues (same source S66 used): tau in {0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22}
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)

# S73a tree-level spectral action profile
d_s73a = np.load(os.path.join(SCRIPT_DIR, 's73a_spectral_action_profile.npz'),
                 allow_pickle=True)

# S73a JJ-KAPPA-MAP with Delta(tau) slope/intercept
d_jjk = np.load(os.path.join(SCRIPT_DIR, 's73a_jj_kappa_map.npz'),
                allow_pickle=True)
slope_Delta_tau = float(d_jjk['slope_Delta'])          # -0.2441
intercept_Delta_tau = float(d_jjk['intercept_Delta'])  # 0.5118

# S66 BCS-CW result for comparison
d_s66 = np.load(os.path.join(SCRIPT_DIR, 's66_bcs_cw.npz'), allow_pickle=True)
ns_s66_bcs_cw = float(d_s66['ns_cw_hubble'])  # 0.9595
delta_ns_cw_s66 = float(d_s66['delta_ns_cw_only'])  # -0.000352

# Tree-level n_s from prior computations
ns_tree_s63 = 0.9567  # (local) canonical bare tree n_s
eps_tree_s63 = 0.02163  # (local) canonical eps_H tree

print(f"  Delta(tau) profile (S73A JJ-KAPPA-MAP):")
print(f"    slope     = {slope_Delta_tau:+.6f} M_KK / unit tau")
print(f"    intercept = {intercept_Delta_tau:+.6f} M_KK")
print(f"    Delta(fold=0.19) = {intercept_Delta_tau + slope_Delta_tau*tau_fold:.6f} M_KK")
print(f"    Comparison: Delta_0_OES = {Delta_0_OES:.6f} M_KK (static gap)")
print(f"  S73a tree-level S_fold_recovered = {float(d_s73a['S_fold_recovered']):.2f}")
print(f"  S66 BCS-CW reference: n_s = {ns_s66_bcs_cw:.6f} (fixed Delta, INFO)")
print(f"  S63 bare tree reference: n_s = {ns_tree_s63} (tree-level)")


def Delta_of_tau(tau):
    """BCS gap as a linear function of tau (S73A JJ-KAPPA-MAP).

    Delta(tau) = intercept_Delta_tau + slope_Delta_tau * tau
               = 0.5118 - 0.2441 * tau  [in M_KK units]
    """
    return intercept_Delta_tau + slope_Delta_tau * tau


def dDelta_dtau(tau):
    """First derivative of Delta(tau). Constant = slope."""
    return slope_Delta_tau


# =============================================================================
# STEP 1: BUILD SPECTRA AND COMPUTE TREE + 1-LOOP CONTRIBUTIONS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Tree-Level Spectral Action + Coleman-Weinberg at 7 tau points")
print("=" * 78)

def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Sectors at max_pq_sum = 3 (matches S36/S66)
sectors = []
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors.append((p, q))
print(f"  Sectors (max_pq_sum=3): {sectors}")

tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])
n_tau = len(tau_evals)

# Arrays for all contributions
S_tree_bare = np.zeros(n_tau)         # sum d_n |lambda_n| (bare)
V_CW_tau_dep = np.zeros(n_tau)        # CW with tau-dependent Delta (MAIN)
V_CW_static = np.zeros(n_tau)         # CW with static Delta=Delta_0_OES (S66 reference)
V_CW_tau_dep_mu_low = np.zeros(n_tau)  # mu=0.5 scheme variant
V_CW_tau_dep_mu_high = np.zeros(n_tau) # mu=2.0 scheme variant

# Total mode counts
total_pw_modes = np.zeros(n_tau, dtype=int)

CW_prefactor = 1.0 / (64.0 * PI**2)

t0 = time.time()

for i, tau in enumerate(tau_evals):
    Delta_val = Delta_of_tau(tau)      # tau-dependent gap
    Delta_val_sq = Delta_val ** 2

    for (p, q) in sectors:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            print(f"  WARNING: {key} not found")
            continue

        evals = d_s36[key]
        dim_pq = su3_dim(p, q)
        pw_weight = dim_pq ** 2  # Peter-Weyl multiplicity

        omega = np.abs(evals)
        omega_sq = omega ** 2

        # Tree-level bare action
        S_tree_bare[i] += pw_weight * np.sum(omega)

        # -------- MAIN: V_CW with tau-dependent Delta(tau) --------
        M_sq_tau = omega_sq + Delta_val_sq
        V_CW_tau_dep[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_tau**2 * (np.log(M_sq_tau / mu_central**2) - 1.5)
        )

        # -------- REFERENCE: V_CW with STATIC Delta = Delta_0_OES --------
        M_sq_static = omega_sq + Delta_0_OES**2
        V_CW_static[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_static**2 * (np.log(M_sq_static / mu_central**2) - 1.5)
        )

        # -------- Scheme variants (main, tau-dependent) --------
        V_CW_tau_dep_mu_low[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_tau**2 * (np.log(M_sq_tau / mu_low**2) - 1.5)
        )
        V_CW_tau_dep_mu_high[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_tau**2 * (np.log(M_sq_tau / mu_high**2) - 1.5)
        )

        total_pw_modes[i] += pw_weight * len(evals)

t_compute = time.time() - t0
print(f"  Computed in {t_compute:.2f}s  (total PW modes = {total_pw_modes[0]})")

# Cross-check: S_tree_bare should match the S36 full spectral action
tau_combined = d_s36['tau_combined']
S_full_s36 = d_s36['S_full']
idx_fold_36 = int(np.argmin(np.abs(tau_combined - tau_fold)))
dev_tree_fold = abs(S_tree_bare[4] - S_full_s36[idx_fold_36]) / S_full_s36[idx_fold_36]
print(f"  CrossCheck S_tree_bare(fold)={S_tree_bare[4]:.2f}  vs S36 S_full={S_full_s36[idx_fold_36]:.2f}  dev={dev_tree_fold:.2e}")

# Delta(tau) profile at each tau
Delta_profile = np.array([Delta_of_tau(t) for t in tau_evals])
print(f"\n  {'tau':>6s}  {'Delta(tau)':>12s}  {'V_CW_tau-dep':>15s}  {'V_CW_static':>15s}  {'delta_CW':>12s}")
for j in range(n_tau):
    dC = V_CW_tau_dep[j] - V_CW_static[j]
    print(f"  {tau_evals[j]:6.3f}  {Delta_profile[j]:12.6f}  "
          f"{V_CW_tau_dep[j]:15.4f}  {V_CW_static[j]:15.4f}  {dC:+12.4f}")

# =============================================================================
# STEP 2: S_1loop = S_tree + V_CW AT 7 tau POINTS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Form S_1loop and Extract Derivatives via Cubic Spline")
print("=" * 78)

# Tree-level spectral action at 7 tau (exact spline source)
# We use S_tree_bare from the same eigenvalue data to ensure consistency
S_tree = S_tree_bare.copy()

# S_1loop with tau-dependent Delta (MAIN)
S_1loop_main = S_tree + V_CW_tau_dep

# S_1loop with static Delta (S66-like reference)
S_1loop_static_ref = S_tree + V_CW_static

# Scheme variants
S_1loop_mu_low = S_tree + V_CW_tau_dep_mu_low
S_1loop_mu_high = S_tree + V_CW_tau_dep_mu_high

# Use near-fold points (skip tau=0.05) for spline: 6 points
idx_near = np.arange(1, n_tau)
tau_near = tau_evals[idx_near]

# Function: Hubble slow-roll from arbitrary spline source
def hubble_slow_roll(tau_arr, S_arr, tau_eval):
    """Return (S, dS, d2S, eps_H, n_s_Hubble) at tau_eval."""
    cs = CubicSpline(tau_arr, S_arr)
    Sv = float(cs(tau_eval))
    dSv = float(cs(tau_eval, 1))
    d2Sv = float(cs(tau_eval, 2))
    if d2Sv > 0 and Sv > 0:
        eps = 0.5 * dSv**2 / (Sv * d2Sv)
    else:
        eps = np.inf
    ns = 1.0 - 2.0 * eps
    return Sv, dSv, d2Sv, eps, ns

# A: bare tree
S_A, dS_A, d2S_A, eps_A, ns_A = hubble_slow_roll(tau_near, S_tree[idx_near], tau_fold)
# B: S_1loop with tau-dependent Delta (MAIN)
S_B, dS_B, d2S_B, eps_B, ns_B = hubble_slow_roll(tau_near, S_1loop_main[idx_near], tau_fold)
# C: S_1loop with static Delta (S66 reference)
S_C, dS_C, d2S_C, eps_C, ns_C = hubble_slow_roll(tau_near, S_1loop_static_ref[idx_near], tau_fold)
# D: S_1loop tau-dep at mu=0.5
S_D, dS_D, d2S_D, eps_D, ns_D = hubble_slow_roll(tau_near, S_1loop_mu_low[idx_near], tau_fold)
# E: S_1loop tau-dep at mu=2.0
S_E, dS_E, d2S_E, eps_E, ns_E = hubble_slow_roll(tau_near, S_1loop_mu_high[idx_near], tau_fold)

print(f"\n  Configuration                         {'S(fold)':>14s}  {'dS/dtau':>12s}  {'d2S/dtau2':>14s}  {'eps_H':>10s}  {'n_s':>10s}")
print(f"  " + "-" * 96)
print(f"  A: bare tree                          {S_A:14.4f}  {dS_A:12.4f}  {d2S_A:14.4f}  {eps_A:10.6f}  {ns_A:10.6f}")
print(f"  B: 1-loop CW (tau-dep Delta, mu=M_KK) {S_B:14.4f}  {dS_B:12.4f}  {d2S_B:14.4f}  {eps_B:10.6f}  {ns_B:10.6f}")
print(f"  C: 1-loop CW (static Delta, mu=M_KK)  {S_C:14.4f}  {dS_C:12.4f}  {d2S_C:14.4f}  {eps_C:10.6f}  {ns_C:10.6f}")
print(f"  D: 1-loop CW (tau-dep, mu=0.5)        {S_D:14.4f}  {dS_D:12.4f}  {d2S_D:14.4f}  {eps_D:10.6f}  {ns_D:10.6f}")
print(f"  E: 1-loop CW (tau-dep, mu=2.0)        {S_E:14.4f}  {dS_E:12.4f}  {d2S_E:14.4f}  {eps_E:10.6f}  {ns_E:10.6f}")

# Deltas
delta_ns_main = ns_B - ns_A
delta_ns_static = ns_C - ns_A
delta_ns_tau_dep_only = ns_B - ns_C  # ADDITIONAL effect of tau-dependence in Delta

print(f"\n  Shifts relative to bare tree:")
print(f"    delta n_s (1-loop, tau-dep Delta)   = {delta_ns_main:+.8f}")
print(f"    delta n_s (1-loop, static Delta)    = {delta_ns_static:+.8f}")
print(f"    delta n_s (tau-dep only, vs static) = {delta_ns_tau_dep_only:+.8f}")

# =============================================================================
# STEP 3: CROSS-CHECK — S_1loop / S_tree RATIO
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Cross-check S_1loop / S_tree ratio (chapter sec 5.6 ~ 51.9%)")
print("=" * 78)

ratio_1loop_tree_main = V_CW_tau_dep / S_tree
ratio_1loop_tree_static = V_CW_static / S_tree

print(f"\n  {'tau':>6s}  {'S_tree':>14s}  {'V_CW (tau-dep)':>16s}  {'ratio tau-dep':>14s}  {'ratio static':>14s}")
for j in range(n_tau):
    print(f"  {tau_evals[j]:6.3f}  {S_tree[j]:14.2f}  "
          f"{V_CW_tau_dep[j]:16.4f}  {ratio_1loop_tree_main[j]:14.6f}  {ratio_1loop_tree_static[j]:14.6f}")

ratio_at_fold = ratio_1loop_tree_main[4]
print(f"\n  V_CW / S_tree at fold (tau-dep)    = {ratio_at_fold:.6f}")
print(f"  V_CW / S_tree at fold (static)     = {ratio_1loop_tree_static[4]:.6f}")
print(f"  Chapter 5.6 estimate               = 0.519")
print(f"  NOTE: Chapter 5.6 is the MODULI-INTEGRATED partition function ratio,")
print(f"        not the Coleman-Weinberg ratio. The two are distinct one-loop")
print(f"        quantities. The chapter value serves as a qualitative benchmark.")

# =============================================================================
# STEP 4: LIMITING-CASE CHECK — Delta -> 0
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Limiting Case Delta -> 0 (should give V_CW -> bare, n_s -> tree)")
print("=" * 78)

V_CW_zero = np.zeros(n_tau)
for i, tau in enumerate(tau_evals):
    for (p, q) in sectors:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            continue
        evals = d_s36[key]
        dim_pq = su3_dim(p, q)
        pw_weight = dim_pq ** 2
        omega_sq = np.abs(evals) ** 2
        omega_sq_safe = np.maximum(omega_sq, 1e-30)
        V_CW_zero[i] += CW_prefactor * pw_weight * np.sum(
            omega_sq_safe**2 * (np.log(omega_sq_safe / mu_central**2) - 1.5)
        )

S_1loop_zero_gap = S_tree + V_CW_zero
S_zg, dS_zg, d2S_zg, eps_zg, ns_zg = hubble_slow_roll(
    tau_near, S_1loop_zero_gap[idx_near], tau_fold)

print(f"\n  Delta -> 0 limit (V_CW with bare masses):")
print(f"    V_CW(fold, Delta=0) = {V_CW_zero[4]:.4f}")
print(f"    n_s(Delta=0)        = {ns_zg:.8f}")
print(f"    n_s(tree)           = {ns_A:.8f}")
print(f"    Difference          = {ns_zg - ns_A:+.8f}  (CW shift at Delta=0)")
print(f"    Note: 'V_CW -> 0' would require ALL masses -> 0. At finite lambda_n,")
print(f"          V_CW(Delta=0) is non-zero but contains no Delta contribution.")

# =============================================================================
# STEP 5: DIAGNOSTIC — CW-ONLY CONTRIBUTION TO d^2 S / dtau^2
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Diagnostic — CW-only Contribution to d^2 S / dtau^2 at Fold")
print("=" * 78)

# Isolate the CW-only term by splining V_CW alone
cs_VCW_main = CubicSpline(tau_near, V_CW_tau_dep[idx_near])
V_CW_fold = float(cs_VCW_main(tau_fold))
dV_CW_fold = float(cs_VCW_main(tau_fold, 1))
d2V_CW_fold = float(cs_VCW_main(tau_fold, 2))

cs_VCW_static = CubicSpline(tau_near, V_CW_static[idx_near])
V_CW_static_fold = float(cs_VCW_static(tau_fold))
dV_CW_static_fold = float(cs_VCW_static(tau_fold, 1))
d2V_CW_static_fold = float(cs_VCW_static(tau_fold, 2))

# CW contribution from tau-dependence of Delta alone
cs_VCW_tau_only = CubicSpline(tau_near, (V_CW_tau_dep - V_CW_static)[idx_near])
delta_CW_fold = float(cs_VCW_tau_only(tau_fold))
d_delta_CW_fold = float(cs_VCW_tau_only(tau_fold, 1))
d2_delta_CW_fold = float(cs_VCW_tau_only(tau_fold, 2))

print(f"\n  V_CW at fold (tau-dep Delta):")
print(f"    V_CW(fold)       = {V_CW_fold:.4f}")
print(f"    dV_CW/dtau(fold) = {dV_CW_fold:+.4f}")
print(f"    d2V_CW/dtau2(fold)={d2V_CW_fold:+.4f}")
print(f"\n  V_CW at fold (static Delta = Delta_0_OES = {Delta_0_OES:.4f}):")
print(f"    V_CW(fold)       = {V_CW_static_fold:.4f}")
print(f"    dV_CW/dtau(fold) = {dV_CW_static_fold:+.4f}")
print(f"    d2V_CW/dtau2(fold)={d2V_CW_static_fold:+.4f}")
print(f"\n  Delta of CW from tau-dependence alone (main - static):")
print(f"    delta V_CW(fold)        = {delta_CW_fold:+.4f}")
print(f"    d(delta V_CW)/dtau(fold)= {d_delta_CW_fold:+.4f}")
print(f"    d2(delta V_CW)/dtau2    = {d2_delta_CW_fold:+.4f}")

# Compare to tree derivatives
cs_Stree = CubicSpline(tau_near, S_tree[idx_near])
S_tree_val = float(cs_Stree(tau_fold))
dS_tree_val = float(cs_Stree(tau_fold, 1))
d2S_tree_val = float(cs_Stree(tau_fold, 2))

print(f"\n  Tree at fold:")
print(f"    S_tree(fold)        = {S_tree_val:.4f}")
print(f"    dS_tree/dtau(fold)  = {dS_tree_val:+.4f}")
print(f"    d2S_tree/dtau2(fold)= {d2S_tree_val:+.4f}")
print(f"\n  Relative contribution of CW:")
print(f"    V_CW / S_tree          = {V_CW_fold/S_tree_val:+.6f}")
print(f"    dV_CW/dS_tree          = {dV_CW_fold/dS_tree_val:+.6f}")
print(f"    d2V_CW/d2S_tree        = {d2V_CW_fold/d2S_tree_val:+.6f}")

# =============================================================================
# STEP 6: SCHEME DEPENDENCE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Renormalization Scale Dependence (mu variation)")
print("=" * 78)

ns_spread = max(ns_B, ns_D, ns_E) - min(ns_B, ns_D, ns_E)
print(f"\n  mu = 0.5 M_KK:   n_s = {ns_D:.8f}")
print(f"  mu = 1.0 M_KK:   n_s = {ns_B:.8f}")
print(f"  mu = 2.0 M_KK:   n_s = {ns_E:.8f}")
print(f"  Spread in n_s:         {ns_spread:.8f}")
print(f"  Spread / Planck sigma: {ns_spread/planck_ns_err:.4f}")

# =============================================================================
# STEP 7: DENSE GRID FOR PLOTTING (interpolate V_CW and S_1loop)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Dense Grid via Spline Evaluation")
print("=" * 78)

tau_dense = np.linspace(tau_near.min(), tau_near.max(), 400)
V_CW_dense = cs_VCW_main(tau_dense)
S_tree_dense = cs_Stree(tau_dense)
S_1loop_dense = S_tree_dense + V_CW_dense
cs_S1loop_main = CubicSpline(tau_near, S_1loop_main[idx_near])
eps_dense = np.zeros_like(tau_dense)
ns_dense = np.zeros_like(tau_dense)
for k, tt in enumerate(tau_dense):
    Sv = float(cs_S1loop_main(tt))
    dSv = float(cs_S1loop_main(tt, 1))
    d2Sv = float(cs_S1loop_main(tt, 2))
    if d2Sv > 0 and Sv > 0:
        eps_dense[k] = 0.5 * dSv**2 / (Sv * d2Sv)
    else:
        eps_dense[k] = np.inf
    ns_dense[k] = 1.0 - 2.0 * eps_dense[k]

print(f"  Dense grid: {len(tau_dense)} points in [{tau_dense[0]:.3f}, {tau_dense[-1]:.3f}]")

# =============================================================================
# STEP 8: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: GATE VERDICT — NS-1LOOP-SPECTRAL-74")
print("=" * 78)

# Pre-registered criterion:
#   PASS: n_s^{1loop} in [0.9607, 0.9691] (Planck 1-sigma)
#   INFO: n_s^{1loop} in [0.9565, 0.9733] (2-sigma)
#   FAIL: 1-loop correction moves n_s away from Planck or leaves n_s outside 2-sigma

ns_1loop = ns_B  # MAIN result: tau-dependent Delta, mu=M_KK
ns_target_lo_1sigma = planck_ns - planck_ns_err      # 0.9607
ns_target_hi_1sigma = planck_ns + planck_ns_err      # 0.9691
ns_target_lo_2sigma = planck_ns - 2 * planck_ns_err  # 0.9565
ns_target_hi_2sigma = planck_ns + 2 * planck_ns_err  # 0.9733

in_1sigma = (ns_target_lo_1sigma <= ns_1loop <= ns_target_hi_1sigma)
in_2sigma = (ns_target_lo_2sigma <= ns_1loop <= ns_target_hi_2sigma)

# Direction check: does 1-loop move toward or away from Planck?
dist_tree = abs(ns_A - planck_ns)
dist_1loop = abs(ns_1loop - planck_ns)
moved_toward = dist_1loop < dist_tree

if in_1sigma:
    verdict = "PASS"
    reason = f"n_s^{{1loop}} = {ns_1loop:.6f} in [0.9607, 0.9691] (Planck 1-sigma)"
elif in_2sigma and moved_toward:
    verdict = "INFO"
    reason = (f"n_s^{{1loop}} = {ns_1loop:.6f} in [0.9565, 0.9733] (2-sigma), "
              f"moved TOWARD Planck")
elif not moved_toward:
    verdict = "FAIL"
    reason = (f"n_s^{{1loop}} = {ns_1loop:.6f}. "
              f"Moved AWAY from Planck (dist: {dist_tree:.6f} -> {dist_1loop:.6f})")
else:
    verdict = "FAIL"
    reason = f"n_s^{{1loop}} = {ns_1loop:.6f} outside 2-sigma Planck band"

tension_sigma = abs(ns_1loop - planck_ns) / planck_ns_err

gate_detail = (
    f"n_s^{{1loop}} (tau-dep Delta, mu=M_KK) = {ns_1loop:.6f}. "
    f"Planck tension = {tension_sigma:.2f} sigma. "
    f"eps_H = {eps_B:.6f}. "
    f"Tree n_s = {ns_A:.6f}. "
    f"delta n_s (total 1-loop, tau-dep) = {delta_ns_main:+.6f}. "
    f"delta n_s (static-Delta reference) = {delta_ns_static:+.6f}. "
    f"delta n_s (tau-dep effect alone)   = {delta_ns_tau_dep_only:+.6f}. "
    f"V_CW/S_tree at fold = {ratio_at_fold:.4f}. "
    f"Chapter 5.6 reference = 0.519. "
    f"Scheme spread = {ns_spread:.6f}. "
    f"Direction: {'TOWARD' if moved_toward else 'AWAY FROM'} Planck. "
    f"S66 BCS-CW comparison: n_s = {ns_s66_bcs_cw:.6f}, this = {ns_1loop:.6f}, "
    f"diff = {ns_1loop - ns_s66_bcs_cw:+.6f}."
)

print(f"\n  GATE: NS-1LOOP-SPECTRAL-74")
print(f"  CRITERION:")
print(f"    PASS: n_s in [{ns_target_lo_1sigma:.4f}, {ns_target_hi_1sigma:.4f}] (1-sigma)")
print(f"    INFO: n_s in [{ns_target_lo_2sigma:.4f}, {ns_target_hi_2sigma:.4f}] (2-sigma, TOWARD Planck)")
print(f"    FAIL: outside 2-sigma OR moved away from Planck")
print(f"")
print(f"  n_s^{{1loop}}     = {ns_1loop:.6f}")
print(f"  Planck tension   = {tension_sigma:.2f} sigma")
print(f"  Direction vs tree: {'TOWARD' if moved_toward else 'AWAY FROM'} Planck")
print(f"  S66 comparison:    static-Delta CW gave {ns_s66_bcs_cw:.6f}")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"  {reason}")

# =============================================================================
# STEP 9: SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Summary Table")
print("=" * 78)

print(f"\n  {'Configuration':>46s}  {'eps_H':>12s}  {'n_s':>12s}  {'sigma':>10s}")
print(f"  " + "-" * 84)
for lbl, desc, e, ns in [
    ('A', 'bare tree', eps_A, ns_A),
    ('B', '1-loop CW (tau-dep Delta, mu=M_KK) MAIN', eps_B, ns_B),
    ('C', '1-loop CW (static Delta, mu=M_KK) S66 ref', eps_C, ns_C),
    ('D', '1-loop CW (tau-dep, mu=0.5)', eps_D, ns_D),
    ('E', '1-loop CW (tau-dep, mu=2.0)', eps_E, ns_E),
]:
    sig = abs(ns - planck_ns) / planck_ns_err
    print(f"  {lbl}: {desc:>42s}  {e:12.8f}  {ns:12.6f}  {sig:8.2f}sig")
print(f"  {'S66 BCS-CW (static Delta, reference)':>46s}  {'---':>12s}  {ns_s66_bcs_cw:12.6f}  "
      f"{abs(ns_s66_bcs_cw-planck_ns)/planck_ns_err:8.2f}sig")
print(f"  {'Planck 2018':>46s}  {'---':>12s}  {planck_ns:12.6f}  {'0.00sig':>10s}")

# =============================================================================
# STEP 10: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Saving Data")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's74_ns_1loop_spectral.npz')
np.savez(
    outpath,
    gate_name='NS-1LOOP-SPECTRAL-74',
    gate_verdict=verdict,
    gate_detail=gate_detail,
    # Inputs
    tau_evals=tau_evals,
    Delta_profile=Delta_profile,
    slope_Delta_tau=slope_Delta_tau,
    intercept_Delta_tau=intercept_Delta_tau,
    Delta_0_OES=Delta_0_OES,
    mu_central=mu_central,
    tau_fold=tau_fold,
    # Tree
    S_tree=S_tree,
    S_tree_fold=S_A,
    dS_tree_fold=dS_A,
    d2S_tree_fold=d2S_A,
    eps_H_tree=eps_A,
    ns_tree=ns_A,
    # V_CW arrays
    V_CW_tau_dep=V_CW_tau_dep,
    V_CW_static=V_CW_static,
    V_CW_tau_dep_mu_low=V_CW_tau_dep_mu_low,
    V_CW_tau_dep_mu_high=V_CW_tau_dep_mu_high,
    V_CW_zero_gap=V_CW_zero,
    # V_CW at fold (from spline)
    V_CW_fold=V_CW_fold,
    dV_CW_fold=dV_CW_fold,
    d2V_CW_fold=d2V_CW_fold,
    V_CW_static_fold=V_CW_static_fold,
    d2V_CW_static_fold=d2V_CW_static_fold,
    delta_CW_fold_tau_dep=delta_CW_fold,
    d2_delta_CW_fold=d2_delta_CW_fold,
    # S_1loop
    S_1loop_main=S_1loop_main,
    S_1loop_static_ref=S_1loop_static_ref,
    S_1loop_zero_gap=S_1loop_zero_gap,
    # Main result
    ns_1loop=ns_1loop,
    eps_H_1loop=eps_B,
    dS_1loop_fold=dS_B,
    d2S_1loop_fold=d2S_B,
    # Shifts
    delta_ns_main=delta_ns_main,
    delta_ns_static_ref=delta_ns_static,
    delta_ns_tau_dep_only=delta_ns_tau_dep_only,
    # Configs
    config_A=np.array([eps_A, ns_A]),
    config_B=np.array([eps_B, ns_B]),
    config_C=np.array([eps_C, ns_C]),
    config_D=np.array([eps_D, ns_D]),
    config_E=np.array([eps_E, ns_E]),
    # Scheme
    ns_mu_low=ns_D,
    ns_mu_high=ns_E,
    ns_scheme_spread=ns_spread,
    # Cross-check
    ratio_1loop_tree_main=ratio_1loop_tree_main,
    ratio_1loop_tree_static=ratio_1loop_tree_static,
    chapter_56_ratio_estimate=0.519,
    ratio_at_fold_main=ratio_at_fold,
    # S66 reference
    ns_s66_bcs_cw_reference=ns_s66_bcs_cw,
    delta_ns_cw_s66=delta_ns_cw_s66,
    # Dense grid for plotting
    tau_dense=tau_dense,
    V_CW_dense=V_CW_dense,
    S_tree_dense=S_tree_dense,
    S_1loop_dense=S_1loop_dense,
    ns_dense=ns_dense,
    eps_dense=eps_dense,
    # Planck
    planck_ns=planck_ns,
    planck_ns_err=planck_ns_err,
    ns_target_lo_1sigma=ns_target_lo_1sigma,
    ns_target_hi_1sigma=ns_target_hi_1sigma,
    ns_target_lo_2sigma=ns_target_lo_2sigma,
    ns_target_hi_2sigma=ns_target_hi_2sigma,
    planck_tension_sigma=tension_sigma,
)
print(f"  Saved: {outpath}")

# =============================================================================
# STEP 11: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Plot")
print("=" * 78)

fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.32, wspace=0.32)

# Panel 1: V_CW(tau) and tau-dependence of Delta
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_dense, V_CW_dense, 'b-', lw=2, label='V_CW (tau-dep Delta)')
ax1.plot(tau_near, V_CW_tau_dep[idx_near], 'bo', ms=7)
ax1.plot(tau_near, V_CW_static[idx_near], 'r^', ms=7,
         label=f'V_CW (static Delta={Delta_0_OES:.3f})')
ax1.axvline(tau_fold, color='k', ls='--', alpha=0.5, label=f'tau_fold = {tau_fold}')
ax1.set_xlabel('tau')
ax1.set_ylabel('V_CW [M_KK^4 units]')
ax1.set_title('Coleman-Weinberg Potential V_CW(tau)')
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# Panel 2: Delta(tau)
ax2 = fig.add_subplot(gs[0, 1])
Delta_dense = intercept_Delta_tau + slope_Delta_tau * tau_dense
ax2.plot(tau_dense, Delta_dense, 'g-', lw=2, label='Delta(tau) = -0.2441*tau + 0.5118')
ax2.axhline(Delta_0_OES, color='r', ls='--', alpha=0.6,
            label=f'Delta_0_OES = {Delta_0_OES:.4f} (static)')
ax2.axvline(tau_fold, color='k', ls='--', alpha=0.5, label=f'tau_fold = {tau_fold}')
ax2.set_xlabel('tau')
ax2.set_ylabel('Delta(tau) [M_KK]')
ax2.set_title('BCS gap profile (S73A JJ-KAPPA-MAP)')
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)

# Panel 3: V_CW/S_tree ratio
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(tau_near, ratio_1loop_tree_main[idx_near], 'bo-', ms=7, lw=2,
         label='tau-dep Delta')
ax3.plot(tau_near, ratio_1loop_tree_static[idx_near], 'r^-', ms=7, lw=2,
         label='static Delta')
ax3.axhline(0.519, color='purple', ls=':', label='chapter 5.6 ref 0.519')
ax3.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax3.set_xlabel('tau')
ax3.set_ylabel('V_CW / S_tree')
ax3.set_title('1-loop / tree ratio')
ax3.legend(fontsize=8)
ax3.grid(alpha=0.3)

# Panel 4: n_s(tau)
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(tau_dense, ns_dense, 'b-', lw=2, label='n_s^{1loop} (tau-dep Delta)')
ax4.axhline(ns_A, color='g', ls='--', alpha=0.6, label=f'tree n_s = {ns_A:.4f}')
ax4.axhline(planck_ns, color='r', ls='--', alpha=0.6, label=f'Planck = {planck_ns}')
ax4.fill_between(tau_dense, planck_ns - planck_ns_err, planck_ns + planck_ns_err,
                 color='red', alpha=0.15, label='Planck 1-sigma')
ax4.fill_between(tau_dense, planck_ns - 2*planck_ns_err, planck_ns + 2*planck_ns_err,
                 color='red', alpha=0.08)
ax4.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax4.set_xlabel('tau')
ax4.set_ylabel('n_s')
ax4.set_title(f'Spectral index: tree {ns_A:.4f}, 1-loop {ns_1loop:.4f}')
ax4.legend(fontsize=8, loc='best')
ax4.grid(alpha=0.3)
ax4.set_ylim(0.94, 1.02)

# Panel 5: S_tree and S_1loop
ax5 = fig.add_subplot(gs[1, 1])
ax5.plot(tau_dense, S_tree_dense, 'g-', lw=2, label='S_tree')
ax5.plot(tau_dense, S_1loop_dense, 'b-', lw=2, label='S_1loop (tau-dep Delta)')
ax5.plot(tau_near, S_tree[idx_near], 'go', ms=6)
ax5.plot(tau_near, S_1loop_main[idx_near], 'bo', ms=6)
ax5.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax5.set_xlabel('tau')
ax5.set_ylabel('S')
ax5.set_title('Tree vs 1-loop spectral action')
ax5.legend(fontsize=8)
ax5.grid(alpha=0.3)

# Panel 6: n_s comparison bar chart
ax6 = fig.add_subplot(gs[1, 2])
labels = ['Planck', 'tree\n(bare)', 'S66\nBCS-CW', 'this 1-loop\n(tau-dep)', 'mu=0.5', 'mu=2.0']
values = [planck_ns, ns_A, ns_s66_bcs_cw, ns_B, ns_D, ns_E]
colors = ['red', 'gray', 'orange', 'blue', 'lightblue', 'lightblue']
bars = ax6.bar(labels, values, color=colors, alpha=0.8, edgecolor='black')
ax6.axhline(planck_ns, color='red', ls='--', alpha=0.6)
ax6.fill_between([-0.5, len(labels)-0.5],
                 planck_ns - planck_ns_err, planck_ns + planck_ns_err,
                 color='red', alpha=0.15)
ax6.set_ylabel('n_s')
ax6.set_title(f'Gate: {verdict}')
ax6.set_ylim(0.94, 0.98)
for bar, val in zip(bars, values):
    ax6.text(bar.get_x() + bar.get_width()/2, val + 0.001,
             f'{val:.4f}', ha='center', fontsize=8)
ax6.grid(alpha=0.3, axis='y')
plt.setp(ax6.get_xticklabels(), rotation=15, fontsize=8)

plt.suptitle(
    f'NS-1LOOP-SPECTRAL-74 (W1-I): 1-Loop CW with tau-dependent Delta(tau)  '
    f'[{verdict}]', fontsize=13, fontweight='bold')

outpath_plot = os.path.join(SCRIPT_DIR, 's74_ns_1loop_spectral.png')
plt.savefig(outpath_plot, dpi=130, bbox_inches='tight')
plt.close()
print(f"  Saved: {outpath_plot}")

print("\n" + "=" * 78)
print(f"NS-1LOOP-SPECTRAL-74 COMPLETE  --  VERDICT: {verdict}")
print("=" * 78)
