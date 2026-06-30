#!/usr/bin/env python3
"""
s74_self_consistency.py -- SELF-CONSISTENCY-74: Fixed-Point Iteration (T_b, tau)
=================================================================================
Gate: SELF-CONSISTENCY-74
  PASS if a unique fixed-point is found (all 3 initial conditions converge).
  INFO if multiple fixed points exist.
  FAIL if no fixed point (diverges) OR if W1-A or W1-B FAIL (prerequisite).

  CURRENT STATUS: W1-B FAILED (no V_eff minimum in [0.45, 0.70] at any L_max).
  The gate therefore FAILs by prerequisite. This script documents the failure
  and probes whether the LOCAL saddle at tau = 0.19 (per W2-D) acts as a
  transient attractor even though the GLOBAL V_eff is runaway.

Substrate framing:
  The transfer function T_b(k) depends on the branch horizon-crossing times,
  which depend on the modulus value tau. The modulus minimum tau_min depends
  on the back-reaction from the GGE quasiparticles, which depends on T_b via
  the GGE state. This creates a self-consistency loop:

      (T_b, tau_min) = fixed-point of the joint (W1-A, W1-B) system.

  The fabric is NOT in space — tau is the Jensen deformation coordinate within
  the internal geometry, and T_b(k) is the overlap-weighted mode transfer through
  the spectral action gradient. Iteration means asking: given T_b, what does the
  back-reacted V_eff prefer for tau? And given that tau, what is T_b?

Method:
  1. Load W1-A (T_b(k) pipeline), W1-B (V_eff(tau) runaway), W2-D (Hessian at fold).
  2. Verify W1-B prerequisite failure by inspecting its gate_verdict and minima lists.
  3. Build a LOCAL V_eff model around tau_fold = 0.19 using W2-D's curvature 84.89:
        V_local(tau) = V_bcs(tau_fold) + 0.5 * curv_jensen_bcs * (tau - tau_fold)^2
     PLUS the global runaway slope dV_bare/dtau at tau_fold from W1-B.
  4. Fixed-point map F(tau) = tau - eta * (dV_local/dtau + dV_bare_global/dtau),
     where the gradient includes BOTH local convexity and global runaway.
  5. Iterate from three initial conditions: tau_0 in {0.19, 0.25, 0.48}.
  6. Record trajectory, convergence/divergence, and LOCAL vs GLOBAL attractor.
  7. Compare tau* to the Planck target 0.539 (W1-B TAU_TARGET).

Cross-checks:
  - Convergence rate should be linear if a fixed point exists.
  - The local curvature 84.89 defines a local basin; the runaway slope defines escape.
  - If local curvature dominates the local slope in a neighborhood, there is a
    transient attractor; otherwise the global runaway wins.

Dependencies:
  - W1-A: computations/session-74/s74_transfer_function.npz (T_b(k), tau_cross_B{1,2,3})
  - W1-B: computations/session-74/s74_moduli_stabilization.npz (V_bare, V_GGE, V_bcs, minima)
  - W2-D: computations/session-74/s74_bdi_morse_stability.npz (curv_jensen_bcs = 84.89)

Author: Hawking-Theorist (Session 74, Wave 2, Batch 3)
Gate:   SELF-CONSISTENCY-74 (W2-L)
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from numpy import sqrt, log, pi, exp, abs as npabs

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    M_KK, tau_fold, dS_fold, d2S_fold, dt_transit, S_fold, planck_ns,
)

# -----------------------------------------------------------------------------
# 1. LOAD PREREQUISITE DATA
# -----------------------------------------------------------------------------
print("=" * 78)
print("SELF-CONSISTENCY-74 (W2-L): Fixed-Point Iteration (T_b, tau)")
print("=" * 78)

t0 = time.time()

W1A = np.load('computations/session-74/s74_transfer_function.npz', allow_pickle=True)
W1B = np.load('computations/session-74/s74_moduli_stabilization.npz', allow_pickle=True)
W2D = np.load('computations/session-74/s74_bdi_morse_stability.npz', allow_pickle=True)

W1A_verdict = str(W1A['gate_verdict'])
W1B_verdict = str(W1B['gate_verdict'])
W2D_verdict = str(W2D['gate_verdict'])

print(f"\nW1-A TRANSFER-FUNCTION-74   verdict: {W1A_verdict}")
print(f"W1-B MODULI-STABILIZATION-74 verdict: {W1B_verdict}")
print(f"W2-D BDI-MORSE-STABILITY-74  verdict: {W2D_verdict}")

# W1-A: transfer function pipeline numbers
tau_cross_B1 = float(W1A['tau_cross_B1'])
tau_cross_B2 = float(W1A['tau_cross_B2'])
tau_cross_B3 = float(W1A['tau_cross_B3'])
c_B1 = float(W1A['c_B1'])
c_B2 = float(W1A['c_B2'])
c_B3 = float(W1A['c_B3'])
n_s_pivot_W1A = float(W1A['n_s_pivot'])
alpha_s_pivot_W1A = float(W1A['alpha_s_pivot'])

# W1-B: runaway V_eff scan
tau_scan = W1B['tau_scan']
V_bare_scan = W1B['V_bare_scan']
V_bcs_scan = W1B['V_bcs_scan']
V_GGE_scan = W1B['V_GGE_scan']
V_dressed_b = W1B['V_dressed_b']  # BCS-dressed V
V_dressed_c = W1B['V_dressed_c']  # GGE-dressed V
minima_b = W1B['minima_b']
minima_c = W1B['minima_c']
TAU_TARGET = float(W1B['TAU_TARGET'])  # 0.539
TAU_LO = float(W1B['TAU_LO'])          # 0.45
TAU_HI = float(W1B['TAU_HI'])          # 0.70
tau_kappa1 = float(W1B['tau_kappa1'])  # 0.4804 (instanton boundary)

# W2-D: local Hessian curvature at fold
curv_jensen_bcs = float(W2D['curv_jensen_bcs'])    # 84.89
curv_jensen_bare = float(W2D['curv_jensen_bare'])  # 95.93
d2S_classical_fold = float(W2D['d2S_classical_fold'])  # 21825.53
morse_idx_bcs = int(W2D['morse_idx_bcs_36'])       # 0 => local minimum

print(f"\nW1-A transfer function:")
print(f"  tau_cross B1={tau_cross_B1:.3f}  B2={tau_cross_B2:.3f}  B3={tau_cross_B3:.3f}")
print(f"  c_B1={c_B1:.4f}  c_B2={c_B2:.4f}  c_B3={c_B3:.4f}")
print(f"  n_s_pivot={n_s_pivot_W1A:.6f}  alpha_s_pivot={alpha_s_pivot_W1A:.3e}")

print(f"\nW1-B moduli stabilization:")
print(f"  minima_b (BCS dressed): {list(minima_b)}")
print(f"  minima_c (GGE dressed): {list(minima_c)}")
print(f"  TAU_TARGET={TAU_TARGET:.3f}  band=[{TAU_LO:.3f}, {TAU_HI:.3f}]")
print(f"  tau_kappa1={tau_kappa1:.4f}")

print(f"\nW2-D Hessian at fold (tau=0.19):")
print(f"  curv_jensen_bcs  = +{curv_jensen_bcs:.4f}")
print(f"  curv_jensen_bare = +{curv_jensen_bare:.4f}")
print(f"  d2S_classical    = +{d2S_classical_fold:.2f}")
print(f"  Morse index BCS = {morse_idx_bcs}  (0 => local minimum in the 36D Sym^2(su(3)) basis)")

# -----------------------------------------------------------------------------
# 2. VERIFY W1-B PREREQUISITE FAILURE
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 1: Verify W1-B prerequisite failure")
print("-" * 78)

prereq_failed = (W1B_verdict == "FAIL") or (len(minima_b) == 0 and len(minima_c) == 0)
print(f"  W1-B verdict == FAIL: {W1B_verdict == 'FAIL'}")
print(f"  minima_b empty:       {len(minima_b) == 0}")
print(f"  minima_c empty:       {len(minima_c) == 0}")
print(f"  PREREQUISITE FAILED:  {prereq_failed}")

# Gradient of V_bare (to check runaway direction)
dV_bare_dtau = np.gradient(V_bare_scan, tau_scan)
dV_GGE_dtau = np.gradient(V_GGE_scan, tau_scan)
dV_bcs_dtau = np.gradient(V_bcs_scan, tau_scan)

idx_fold = int(np.argmin(np.abs(tau_scan - tau_fold)))
dV_bare_fold = float(dV_bare_dtau[idx_fold])
dV_GGE_fold = float(dV_GGE_dtau[idx_fold])
dV_bcs_fold = float(dV_bcs_dtau[idx_fold])

# V at fold
V_bare_fold = float(V_bare_scan[idx_fold])
V_bcs_fold = float(V_bcs_scan[idx_fold])
V_GGE_fold = float(V_GGE_scan[idx_fold])

print(f"\n  Global runaway gradients at tau_fold={tau_fold}:")
print(f"    dV_bare/dtau  = {dV_bare_fold:+.4e}   (M_KK^4)")
print(f"    dV_bcs/dtau   = {dV_bcs_fold:+.4e}")
print(f"    dV_GGE/dtau   = {dV_GGE_fold:+.4e}")
print(f"  All positive => V_total increases with tau => runaway direction is tau -> inf")

# -----------------------------------------------------------------------------
# 3. LOCAL V_eff AROUND tau_fold (Hessian curvature + runaway slope)
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 2: Build local V_eff around tau_fold (W2-D + global runaway slope)")
print("-" * 78)

# Global V_eff gradient at fold (used by all three W1-B dressings)
# Choose the BCS-dressed curve as primary (closest to transit physics)
dV_global_fold = dV_bcs_fold   # global runaway slope (positive)

# Local curvature from W2-D Hessian (positive => local minimum in 36D moduli space)
k_local = curv_jensen_bcs      # (M_KK^2)

# Local V_eff model:
#   V_local(tau) = V_bcs_fold + dV_global_fold * (tau - tau_fold)
#                             + 0.5 * k_local * (tau - tau_fold)^2
# This is a tilted parabola. The tilt comes from the global runaway slope
# measured at tau_fold. The curvature comes from the W2-D Hessian.
#
# dV_local/dtau = dV_global_fold + k_local * (tau - tau_fold)
# Setting this to zero gives the LOCAL critical point:
#   tau_local_crit = tau_fold - dV_global_fold / k_local

def V_local(tau):
    return V_bcs_fold + dV_global_fold * (tau - tau_fold) + 0.5 * k_local * (tau - tau_fold) ** 2

def dV_local(tau):
    return dV_global_fold + k_local * (tau - tau_fold)

tau_local_crit = tau_fold - dV_global_fold / k_local
V_local_crit = V_local(tau_local_crit)

print(f"  V_local(tau) = {V_bcs_fold:+.4e} + {dV_global_fold:+.4e} * (tau - {tau_fold})")
print(f"                                 + 0.5 * {k_local:.4f} * (tau - {tau_fold})^2")
print(f"  dV_local/dtau = {dV_global_fold:+.4e} + {k_local:.4f} * (tau - {tau_fold})")
print(f"  tau_local_crit = {tau_local_crit:.4f}  (where dV_local = 0)")
print(f"  V_local_crit   = {V_local_crit:+.4e}")
print(f"  Shift from fold: Delta_tau = {tau_local_crit - tau_fold:+.4f}")

# Is tau_local_crit to the LEFT or RIGHT of tau_fold?
# dV_global_fold > 0 (runaway increases with tau) => -dV_global_fold/k_local < 0
# So tau_local_crit < tau_fold. The "local critical point" is at tau < 0.19.
# This is OUTSIDE the transit regime (tau starts at 0).
# The local minimum of the tilted parabola is LEFT of the fold — still "downhill"
# from the standpoint of monotone spectral action increase.

if tau_local_crit < tau_scan.min():
    print(f"  WARNING: tau_local_crit = {tau_local_crit:.4f} < tau_scan.min() = {tau_scan.min():.4f}")
    print(f"  The tilted-parabola minimum is BELOW the scan range — not physical.")

# -----------------------------------------------------------------------------
# 4. FIXED-POINT ITERATION — three initial conditions
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 3: Fixed-point iteration F(tau) = tau - eta * dV_local/dtau")
print("-" * 78)

# Gradient descent with step size eta.
# eta = 1/k_local would give one-step convergence for a pure quadratic.
# We use eta = 0.5 / k_local for a cautious stable descent.
eta = 0.5 / k_local  # (local)
print(f"  Step size: eta = 0.5 / k_local = {eta:.6f}")

def fixed_point_map(tau):
    """F(tau) = tau - eta * dV_local/dtau(tau)."""
    return tau - eta * dV_local(tau)

def iterate(tau0, max_iter=200, tol=1e-10):
    """Return trajectory (list of tau values) and convergence flag."""
    traj = [tau0]
    converged = False
    diverged = False
    for k in range(max_iter):
        tau_next = fixed_point_map(traj[-1])
        if not np.isfinite(tau_next) or npabs(tau_next) > 1e6:
            diverged = True
            traj.append(tau_next)
            break
        traj.append(tau_next)
        if npabs(tau_next - traj[-2]) < tol:
            converged = True
            break
    return np.array(traj), converged, diverged

# Three initial conditions, per gate spec
init_conditions = {
    'IC_a_fold':     0.19,   # (a) tau = 0.19 fold
    'IC_b_postfold': 0.25,   # (b) tau = 0.25 post-fold small shift
    'IC_c_kappa1':   0.48,   # (c) tau = 0.48 instanton boundary (tau_kappa1 from W1-B)
}

results = {}
for name, tau0 in init_conditions.items():
    traj, conv, div = iterate(tau0)
    tau_star = float(traj[-1])
    n_iter = len(traj) - 1
    results[name] = {
        'tau0': tau0,
        'trajectory': traj,
        'tau_star': tau_star,
        'n_iter': n_iter,
        'converged': conv,
        'diverged': div,
    }
    label = "CONVERGED" if conv else ("DIVERGED" if div else "MAX_ITER")
    print(f"  {name}: tau0={tau0:.4f} -> tau*={tau_star:.6f}  ({n_iter} steps, {label})")

# -----------------------------------------------------------------------------
# 5. CONVERGENCE RATE (contraction mapping test)
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 4: Convergence rate diagnostics (contraction mapping)")
print("-" * 78)

# F'(tau) = 1 - eta * k_local  (constant for our tilted parabola)
F_prime = 1.0 - eta * k_local
print(f"  F'(tau) = 1 - eta * k_local = 1 - {eta:.6f} * {k_local:.4f} = {F_prime:.6f}")
print(f"  |F'| < 1 => contraction mapping => fixed point is attractive if it exists")
print(f"  |F'| = {npabs(F_prime):.6f}  (must be < 1 for linear convergence)")

# Empirical convergence rate from trajectory (a)
traj_a = results['IC_a_fold']['trajectory']
if len(traj_a) >= 3:
    # Ratio of successive differences -- should match |F'|
    diffs = np.diff(traj_a)
    nonzero_diffs = diffs[npabs(diffs) > 1e-15]
    if len(nonzero_diffs) >= 2:
        ratios = nonzero_diffs[1:] / nonzero_diffs[:-1]
        emp_rate = float(np.mean(ratios[npabs(ratios) < 10]))
        print(f"  Empirical rate (IC_a mean ratio) = {emp_rate:.6f}")

# -----------------------------------------------------------------------------
# 6. LOCAL VS GLOBAL ATTRACTOR TEST
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 5: Local vs global attractor analysis")
print("-" * 78)

# Check: does the iteration converge to tau_local_crit, or does it escape?
tau_star_a = results['IC_a_fold']['tau_star']
tau_star_b = results['IC_b_postfold']['tau_star']
tau_star_c = results['IC_c_kappa1']['tau_star']

# All three should converge to the same tau_local_crit (since it's a
# strictly convex tilted parabola; any IC converges to the same minimum).
common_fixed_point = (
    npabs(tau_star_a - tau_local_crit) < 1e-3 and
    npabs(tau_star_b - tau_local_crit) < 1e-3 and
    npabs(tau_star_c - tau_local_crit) < 1e-3
)
print(f"  tau_star (fold)     = {tau_star_a:.6f}")
print(f"  tau_star (post-fold)= {tau_star_b:.6f}")
print(f"  tau_star (kappa1)   = {tau_star_c:.6f}")
print(f"  tau_local_crit       = {tau_local_crit:.6f}")
print(f"  All three converge to same point: {common_fixed_point}")

# Now: is tau_local_crit in a "physical" region?
# tau must be >= 0 and tau must be in the tau_scan range.
physical_crit = (
    tau_local_crit > 0.0 and
    tau_scan.min() <= tau_local_crit <= tau_scan.max()
)
print(f"  tau_local_crit in [0, tau_scan.max()]: {physical_crit}")

# Is tau_local_crit in the Planck target band [TAU_LO, TAU_HI]?
in_target_band = (TAU_LO <= tau_local_crit <= TAU_HI)
print(f"  tau_local_crit in Planck target band [{TAU_LO}, {TAU_HI}]: {in_target_band}")

# Distance from Planck target
dist_from_planck = npabs(tau_local_crit - TAU_TARGET)
print(f"  Distance from TAU_TARGET={TAU_TARGET}: |Delta| = {dist_from_planck:.4f}")

# -----------------------------------------------------------------------------
# 7. STRUCTURAL DIAGNOSTIC: balance of curvature vs runaway slope
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 6: Curvature vs runaway balance -- does local convexity dominate?")
print("-" * 78)

# Scale of curvature in tau-units:
# A curvature k_local (dimensions M_KK^2) with a slope dV_global_fold (M_KK^4)
# means the "local basin half-width" where convexity wins over slope is:
#   delta_tau_balance = dV_global_fold / k_local
# Beyond this shift, the slope dominates and the runaway takes over.
delta_tau_balance = dV_global_fold / k_local
print(f"  delta_tau_balance = dV_bcs_fold / k_local = {dV_global_fold:.4e} / {k_local:.4f}")
print(f"                    = {delta_tau_balance:.6f}")
print(f"  This is the shift where local convexity EXACTLY BALANCES global runaway slope.")
print(f"  For |tau - tau_fold| > delta_tau_balance, the tilted parabola slope is dominated by")
print(f"  local curvature contribution; for |tau - tau_fold| < delta_tau_balance, runaway wins.")

# Does delta_tau_balance match what we found for tau_local_crit?
print(f"  Consistency: tau_fold - delta_tau_balance = {tau_fold - delta_tau_balance:.6f}")
print(f"  (should equal tau_local_crit = {tau_local_crit:.6f})")

# Dimensionless ratio: curvature / (slope / typical_tau_width)
typical_width = 0.1  # (local)
curv_over_slope_scaled = (k_local * typical_width) / dV_global_fold
print(f"  Ratio (k_local * 0.1) / dV_bcs_fold = {curv_over_slope_scaled:.4f}")
if curv_over_slope_scaled < 1.0:
    print(f"  => Over a 0.1 tau width, slope dominates curvature. Global runaway wins.")
else:
    print(f"  => Over a 0.1 tau width, curvature dominates slope. Local basin captures.")

# -----------------------------------------------------------------------------
# 8. COMPARE TO PLANCK TARGET
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 7: n_s / Planck comparison")
print("-" * 78)

# The gate target is tau_local_crit close to TAU_TARGET = 0.539 (Planck n_s band).
# In the phonon-first framework, tau -> n_s through the spectral action gradient.
# We don't have an explicit tau->n_s map here (that comes from W1-A P_s(k) pipeline)
# but we can state the gap from the Planck-preferred tau.
print(f"  Planck-preferred tau (from W1-B):  TAU_TARGET = {TAU_TARGET}")
print(f"  Local critical tau (W2-L):         tau_local_crit = {tau_local_crit:.6f}")
print(f"  Signed gap: tau_local_crit - TAU_TARGET = {tau_local_crit - TAU_TARGET:+.6f}")
print(f"  |Gap|: {npabs(tau_local_crit - TAU_TARGET):.4f}")

# -----------------------------------------------------------------------------
# 9. GATE VERDICT
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("GATE VERDICT: SELF-CONSISTENCY-74")
print("=" * 78)

# Pre-registered gate:
#   PASS if unique fixed-point found (all 3 ICs converge to same tau*)
#        AND W1-A, W1-B both PASSed.
#   INFO if multiple fixed points exist.
#   FAIL if no fixed point OR W1-A/W1-B FAILed (prerequisite).

if prereq_failed:
    gate_verdict = "FAIL"
    gate_reason = (
        f"Prerequisite failure: W1-B MODULI-STABILIZATION-74 returned FAIL "
        f"(no V_eff minimum in the target band [{TAU_LO}, {TAU_HI}] at any L_max in {{3,5,7}}). "
        f"The joint (T_b, tau_min) fixed-point has no tau_min input to iterate against. "
        f"Local fixed-point probe at W2-D Hessian (curv_bcs={k_local:.2f}) yields "
        f"tau_local_crit={tau_local_crit:.4f}, outside the Planck target band "
        f"[{TAU_LO}, {TAU_HI}] by |{tau_local_crit - TAU_TARGET:+.4f}|. "
        f"The tilted-parabola 'local fixed point' is LEFT of tau_fold and outside "
        f"the physical transit regime."
    )
else:
    if common_fixed_point:
        gate_verdict = "PASS"
        gate_reason = f"Unique fixed-point tau*={tau_star_a:.6f}, all 3 ICs converge."
    else:
        gate_verdict = "INFO"
        gate_reason = "Multiple fixed points or non-unique convergence."

print(f"\n  Verdict: {gate_verdict}")
print(f"  Reason:  {gate_reason}")

# Structural note on local attractor character
print("\n" + "-" * 78)
print("STRUCTURAL ASSESSMENT")
print("-" * 78)
print(f"  Morse index at fold (W2-D, BCS): {morse_idx_bcs}")
print(f"  Interpretation: In the 36D moduli space, the fold is a LOCAL MINIMUM of the")
print(f"  BCS-dressed effective action (all 36 Hessian eigenvalues > 0). However, this")
print(f"  local minimum is in Sym^2(su(3)) fluctuations, NOT in the tau direction per se.")
print(f"  The Jensen (tau) direction has curv_bcs = {k_local:.2f} (positive), but the")
print(f"  GLOBAL shape of V_bcs(tau) has a positive slope {dV_global_fold:+.4e} at the fold,")
print(f"  which dominates the local curvature across any finite tau width.")
print(f"  ")
print(f"  The tilted parabola V_local = V_0 + slope*(tau-tau_fold) + 0.5*curv*(tau-tau_fold)^2")
print(f"  has a critical point at tau = {tau_local_crit:.4f}, which is LEFT of tau_fold.")
print(f"  This is a LOCAL MINIMUM of the quadratic approximation, but it is OUTSIDE the")
print(f"  physical transit regime (the substrate only evolves tau forward through the fold,")
print(f"  per the exflation orientation).")
print(f"  ")
print(f"  The local saddle at tau_fold therefore does NOT act as a transient attractor in the")
print(f"  physical direction. W1-B's GLOBAL runaway dominates the W2-D local convexity over")
print(f"  any macroscopic tau interval. Result: no self-consistent (T_b, tau_min) fixed-point")
print(f"  exists in the Planck target band.")

# -----------------------------------------------------------------------------
# 10. SAVE DATA
# -----------------------------------------------------------------------------
print("\n" + "-" * 78)
print("STEP 8: Save data and plot")
print("-" * 78)

out_path = 'computations/session-74/s74_self_consistency.npz'

# Pad trajectories to the same length for storage
max_len = max(len(r['trajectory']) for r in results.values())
def pad(traj, n):
    out = np.full(n, np.nan)
    out[: len(traj)] = traj
    return out

np.savez(
    out_path,
    gate_name='SELF-CONSISTENCY-74',
    gate_verdict=gate_verdict,
    gate_reason=gate_reason,
    # Inputs
    W1A_verdict=W1A_verdict,
    W1B_verdict=W1B_verdict,
    W2D_verdict=W2D_verdict,
    prereq_failed=prereq_failed,
    # Local V_eff parameters
    tau_fold=tau_fold,
    k_local=k_local,
    dV_global_fold=dV_global_fold,
    dV_bare_fold=dV_bare_fold,
    dV_bcs_fold=dV_bcs_fold,
    dV_GGE_fold=dV_GGE_fold,
    V_bare_fold=V_bare_fold,
    V_bcs_fold=V_bcs_fold,
    V_GGE_fold=V_GGE_fold,
    tau_local_crit=tau_local_crit,
    V_local_crit=V_local_crit,
    delta_tau_balance=delta_tau_balance,
    curv_over_slope_scaled=curv_over_slope_scaled,
    # Fixed-point iteration
    eta=eta,  # (local)
    F_prime=F_prime,
    # Trajectories
    traj_a=pad(results['IC_a_fold']['trajectory'], max_len),
    traj_b=pad(results['IC_b_postfold']['trajectory'], max_len),
    traj_c=pad(results['IC_c_kappa1']['trajectory'], max_len),
    tau0_a=results['IC_a_fold']['tau0'],
    tau0_b=results['IC_b_postfold']['tau0'],
    tau0_c=results['IC_c_kappa1']['tau0'],
    tau_star_a=tau_star_a,
    tau_star_b=tau_star_b,
    tau_star_c=tau_star_c,
    n_iter_a=results['IC_a_fold']['n_iter'],
    n_iter_b=results['IC_b_postfold']['n_iter'],
    n_iter_c=results['IC_c_kappa1']['n_iter'],
    conv_a=results['IC_a_fold']['converged'],
    conv_b=results['IC_b_postfold']['converged'],
    conv_c=results['IC_c_kappa1']['converged'],
    common_fixed_point=common_fixed_point,
    # Targets
    TAU_TARGET=TAU_TARGET,
    TAU_LO=TAU_LO,
    TAU_HI=TAU_HI,
    tau_kappa1=tau_kappa1,
    gap_from_target=tau_local_crit - TAU_TARGET,
    in_target_band=in_target_band,
    # Cross-reference (W1-A)
    tau_cross_B1=tau_cross_B1,
    tau_cross_B2=tau_cross_B2,
    tau_cross_B3=tau_cross_B3,
    c_B1=c_B1, c_B2=c_B2, c_B3=c_B3,
    # Cross-reference (W2-D)
    curv_jensen_bcs=curv_jensen_bcs,
    curv_jensen_bare=curv_jensen_bare,
    d2S_classical_fold=d2S_classical_fold,
    morse_idx_bcs=morse_idx_bcs,
    # W1-B scan (for plotting)
    tau_scan=tau_scan,
    V_bare_scan=V_bare_scan,
    V_bcs_scan=V_bcs_scan,
    V_GGE_scan=V_GGE_scan,
)

print(f"  Saved: {out_path}")

# -----------------------------------------------------------------------------
# 11. PLOT
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(12, 9))

# (a) Local V_eff vs global V_bcs scan
ax1 = fig.add_subplot(2, 2, 1)
tau_plot = np.linspace(0.15, 0.70, 200)
V_local_plot = np.array([V_local(t) for t in tau_plot])
ax1.plot(tau_scan, V_bcs_scan, 'b-', lw=2, label='V_bcs global (W1-B)')
ax1.plot(tau_plot, V_local_plot, 'r--', lw=2, label='V_local tilted parabola')
ax1.axvline(tau_fold, color='k', linestyle=':', alpha=0.5, label=f'tau_fold={tau_fold}')
ax1.axvline(TAU_TARGET, color='g', linestyle=':', alpha=0.5, label=f'TAU_TARGET={TAU_TARGET}')
ax1.axvline(tau_local_crit, color='orange', linestyle='--', alpha=0.7,
            label=f'tau_local_crit={tau_local_crit:.3f}')
ax1.set_xlabel('tau')
ax1.set_ylabel('V_eff (M_KK^4)')
ax1.set_title('Global V_bcs vs local tilted parabola')
ax1.legend(fontsize=8, loc='best')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0.15, 0.70)

# (b) Fixed-point trajectories
ax2 = fig.add_subplot(2, 2, 2)
colors = {'IC_a_fold': 'red', 'IC_b_postfold': 'blue', 'IC_c_kappa1': 'green'}
labels = {'IC_a_fold': 'IC (a) tau0=0.19 (fold)',
          'IC_b_postfold': 'IC (b) tau0=0.25 (post-fold)',
          'IC_c_kappa1': 'IC (c) tau0=0.48 (kappa1)'}
for name, r in results.items():
    ax2.plot(r['trajectory'], '-o', ms=3, color=colors[name], label=labels[name])
ax2.axhline(tau_local_crit, color='orange', linestyle='--', alpha=0.7,
            label=f'tau_local_crit={tau_local_crit:.4f}')
ax2.axhline(tau_fold, color='k', linestyle=':', alpha=0.5, label=f'tau_fold={tau_fold}')
ax2.axhline(TAU_TARGET, color='g', linestyle=':', alpha=0.5, label=f'TAU_TARGET={TAU_TARGET}')
ax2.set_xlabel('Iteration k')
ax2.set_ylabel('tau^(k)')
ax2.set_title('Fixed-point iteration trajectories')
ax2.legend(fontsize=7, loc='best')
ax2.grid(True, alpha=0.3)

# (c) Convergence (log |tau - tau*|) for IC (a)
ax3 = fig.add_subplot(2, 2, 3)
traj_a_vals = results['IC_a_fold']['trajectory']
err_a = npabs(traj_a_vals - tau_local_crit) + 1e-16
ax3.semilogy(err_a, 'r-o', ms=3, label='|tau^(k) - tau*_local|')
traj_b_vals = results['IC_b_postfold']['trajectory']
err_b = npabs(traj_b_vals - tau_local_crit) + 1e-16
ax3.semilogy(err_b, 'b-o', ms=3, label='IC (b)')
traj_c_vals = results['IC_c_kappa1']['trajectory']
err_c = npabs(traj_c_vals - tau_local_crit) + 1e-16
ax3.semilogy(err_c, 'g-o', ms=3, label='IC (c)')
ax3.set_xlabel('Iteration k')
ax3.set_ylabel('|tau^(k) - tau*_local|')
ax3.set_title(f'Convergence (|F\'|={npabs(F_prime):.4f})')
ax3.legend(fontsize=7)
ax3.grid(True, alpha=0.3, which='both')

# (d) Summary
ax4 = fig.add_subplot(2, 2, 4)
ax4.axis('off')
summary_lines = [
    f"SELF-CONSISTENCY-74 (W2-L)",
    f"Gate: {gate_verdict}",
    f"",
    f"Prerequisite:",
    f"  W1-A verdict: {W1A_verdict}",
    f"  W1-B verdict: {W1B_verdict} (prerequisite failed)",
    f"  W2-D verdict: {W2D_verdict}",
    f"",
    f"Local parameters at tau_fold={tau_fold}:",
    f"  curv_jensen_bcs  = +{k_local:.2f} (M_KK^2)",
    f"  dV_bcs/dtau      = {dV_global_fold:+.3e} (M_KK^4)",
    f"  delta_tau_balance = {delta_tau_balance:.4f}",
    f"",
    f"Fixed-point map F(tau) = tau - eta*dV_local/dtau",
    f"  eta     = {eta:.6f}",
    f"  |F'|    = {npabs(F_prime):.6f}",
    f"",
    f"Trajectories:",
    f"  IC(a) 0.19 -> {tau_star_a:.6f}  ({results['IC_a_fold']['n_iter']} iter)",
    f"  IC(b) 0.25 -> {tau_star_b:.6f}  ({results['IC_b_postfold']['n_iter']} iter)",
    f"  IC(c) 0.48 -> {tau_star_c:.6f}  ({results['IC_c_kappa1']['n_iter']} iter)",
    f"",
    f"Common fixed point: {common_fixed_point}",
    f"tau_local_crit = {tau_local_crit:.4f}",
    f"TAU_TARGET     = {TAU_TARGET:.4f}",
    f"Gap            = {tau_local_crit - TAU_TARGET:+.4f}",
    f"In target band: {in_target_band}",
]
ax4.text(0.02, 0.98, "\n".join(summary_lines), transform=ax4.transAxes,
         fontfamily='monospace', fontsize=7.5, va='top', ha='left')

plt.tight_layout()
plot_path = 'computations/session-74/s74_self_consistency.png'
plt.savefig(plot_path, dpi=120)
plt.close()
print(f"  Saved: {plot_path}")

print("\n" + "=" * 78)
print(f"COMPLETE: SELF-CONSISTENCY-74 verdict {gate_verdict}  ({time.time() - t0:.2f} sec)")
print("=" * 78)
