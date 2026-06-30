#!/usr/bin/env python3
"""
ONELOOP-EPSILON-63 (W3-09) — One-Loop Effective Slow-Roll Parameter
====================================================================

Compute epsilon from S_eff(tau) = S_b(tau) + S_1loop(tau) where
  S_1loop(tau) = (1/2) sum_n d_n * ln(lambda_n^2(tau))
is the one-loop functional determinant of the Dirac operator D_K on
Jensen-deformed SU(3).

Background: Tree-level fold is MAXIMUM of S_b (36 negative Hessian
eigenvalues). One-loop correction flips all 36 signs (H_eff has all
positive eigenvalues). If S_eff is flatter near fold, epsilon_1loop
could be much smaller than epsilon_tree = 0.0216.

Gate: ONELOOP-EPSILON-63
  PASS if epsilon_1loop < 0.00225  (r < 0.036)
  FAIL if epsilon_1loop > 0.00625  (r > 0.1)
  INFO otherwise

Inputs:
  - s36_sfull_tau_stabilization.npz: S_b(tau) at 16 tau values,
    D_K eigenvalues at tau = {0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22}
  - s62_hessian_oneloop.npz: S_1loop at fold, H_eff eigenvalues
  - s62_kz_ns.npz: epsilon_tree = 0.0216
  - s63_two_loop_estimate.npz: g = 0.003, two-loop convergence

Method: Full spectral functional determinant at each tau value.
"""

import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *

# =============================================================================
# Step 0: Load all input data
# =============================================================================

archive = Path(__file__).parent.parent / 'computations/_shared'
script_dir = Path(__file__).parent

d_s36 = np.load(archive / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d_hess = np.load(script_dir / 's62_hessian_oneloop.npz', allow_pickle=True)
d_kz = np.load(script_dir / 's62_kz_ns.npz', allow_pickle=True)
d_2loop = np.load(script_dir / 's63_two_loop_estimate.npz', allow_pickle=True)

# Tree-level data
tau_combined = d_s36['tau_combined']
S_b_full = d_s36['S_full']  # S_b at 16 tau values
S_b_fold_val = float(d_s36['S_fold'][0])
dSb_fold_val = float(d_s36['dS_fold'][0])
d2Sb_fold_val = float(d_s36['d2S_fold'][0])

# One-loop data at fold
S1_fold_val = float(d_hess['S1_center'])  # S_1loop at fold = 5751.35
Lambda_sq = float(d_hess['Lambda_sq'])

# Cross-check
epsilon_tree = float(d_kz['epsilon_H_SA'])
g_coupling = float(d_2loop['g_avg'])
S1_over_Sb = float(d_2loop['S_1loop_over_S_b'])

print("=" * 70)
print("ONELOOP-EPSILON-63: One-Loop Effective Slow-Roll Parameter")
print("=" * 70)
print(f"\nInput cross-checks:")
print(f"  S_b(fold)    = {S_b_fold_val:.2f}")
print(f"  S_1loop(fold) = {S1_fold_val:.2f}")
print(f"  S_1loop/S_b   = {S1_fold_val/S_b_fold_val:.6f}  (cf. {S1_over_Sb:.6f})")
print(f"  epsilon_tree  = {epsilon_tree:.6f}")
print(f"  g_coupling    = {g_coupling:.6f}")

# NOTE: S_b_fold_val = 250361 includes the spectral action with cutoff Lambda.
# S1_fold_val = 5751 is (1/2) * Tr ln D_K^2 = (1/2) sum d_n ln(lambda_n^2).
# BUT the spectral action S_b uses the CUTOFF function f(D^2/Lambda^2),
# while the one-loop S_1loop = (1/2) Tr ln(D_K^2) is the bare log-determinant.
# The issue: S_b ~ 250K but S_1loop ~ 5751, so S_1loop/S_b ~ 0.023.
# Actually from s63: S_1loop_fold = 5751, S_b_fold = 11092.
# Wait -- there are TWO S_b values:
#   S36: S_full = 250361 (full spectral action with cutoff)
#   S63: S_b_fold = 11092 (something else)
# Need to understand which is the correct potential.

# From s63_two_loop_estimate:
S_b_63 = float(d_2loop['S_b_fold'])  # = 11091.86
S_1loop_63 = float(d_2loop['S_1loop_fold'])  # = 5751.35
S_eff_63 = float(d_2loop['S_eff_fold'])  # = 16843.21

print(f"\n--- Two S_b definitions ---")
print(f"  S_b (S36 spectral action) = {S_b_fold_val:.2f}")
print(f"  S_b (S63 two-loop)        = {S_b_63:.2f}")
print(f"  S_1loop (S63)             = {S_1loop_63:.2f}")
print(f"  S_eff (S63)               = {S_eff_63:.2f}")

# The S36 S_full = 250361 is the FULL spectral action = f_0*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_4*a_4
# The S63 S_b_fold = 11092 appears to be the HESSIAN-relevant part
# For epsilon computation, what matters is: which S defines the potential?
#
# For inflation, the potential is S_full (the full spectral action).
# The one-loop correction is the functional determinant of fluctuations around the background.
# So S_eff = S_full + (1/2) Tr ln(D^2).
#
# Key question: does S_1loop = 5751 use the SAME normalization as S_full = 250361?
# Let's check: S_1loop = (1/2) sum d_n ln(lambda_n^2).
# The 992 eigenvalues (from S44 all_omega arrays) are |lambda_n| ~ 0.82 to 2.06,
# so ln(lambda_n^2) ~ ln(0.67) to ln(4.24) = -0.4 to 1.44.
# With 992 modes and PW degeneracies, sum ~ few thousand. That matches 5751.
#
# Meanwhile S_full = 250361 has the cutoff Lambda^4 * f_0 * a_0 which is huge.
# So S_1loop / S_full ~ 0.023 = 2.3%. This is the correct ratio.

# =============================================================================
# Step 1: Compute S_1loop(tau) at available tau values
# =============================================================================
# We have Dirac eigenvalues at tau = {0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22}
# Each tau has sectors (p,q) with p+q <= 3, giving eigenvalue arrays.

# Sectors and their Peter-Weyl degeneracies dim(p,q)^2
# For SU(3) irrep (p,q): dim = (p+1)(q+1)(p+q+2)/2
# PW degeneracy = dim^2

def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Sectors available in the data (max_pq_sum = 3 in the stored eigenvalues)
sectors = []
for p in range(4):
    for q in range(4):
        if p + q <= 3 and (p + q > 0 or (p == 0 and q == 0)):
            sectors.append((p, q))

tau_evals = [0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22]

print(f"\n--- Computing S_1loop(tau) from Dirac eigenvalues ---")
print(f"Sectors: {sectors}")
print(f"Tau values with eigenvalues: {tau_evals}")

def compute_S1loop(data, tau_val, sectors):
    """
    Compute S_1loop(tau) = (1/2) * sum_{sectors} [dim(p,q)^2 / n_evals] * sum_n ln(lambda_n^2)

    The eigenvalue arrays already include the spinor multiplicity (16 per mode),
    and the PW degeneracy is dim(p,q)^2. But the stored arrays have length
    = dim(p,q)^2 * (number of distinct eigenvalues per sector) already
    incorporating spinor structure.

    Actually: from the s36 data, evals_tau0.190_0_0 has length 16 = 1^2 * 16 (spinor).
    evals_tau0.190_1_0 has length 48 = 3^2 * (16/3)?? No: dim(1,0) = 3, PW = 9,
    but 48 = 3 * 16. So the convention is: each sector (p,q) stores
    dim(p,q) * 16 eigenvalues where dim(p,q) is the irrep dimension.
    Wait: (0,0): 16, (1,0): 48 = 3*16, (0,1): 48 = 3*16
    (1,1): 128 = 8*16, (2,0): 96 = 6*16, (0,2): 96 = 6*16
    (3,0): 160 = 10*16, (0,3): 160 = 10*16
    (2,1): 240 = 15*16, (1,2): 240 = 15*16

    So: n_evals = dim(p,q) * 16. The PW degeneracy is dim(p,q)^2.
    The 16 is the spinor rank (2^{d/2} = 2^4 = 16 for d=8).
    So each eigenvalue in the array should be counted with weight
    dim(p,q)^2 / (dim(p,q) * 16) = dim(p,q) / 16 per eigenvalue.

    Wait, that gives a PW weight. Let me think more carefully.

    On SU(3), the Dirac operator D_K decomposes by Peter-Weyl into blocks.
    The (p,q) sector has a Dirac matrix of size dim(p,q)*16 x dim(p,q)*16.
    Its eigenvalues are stored. The full trace is:

    Tr ln D_K^2 = sum_{(p,q)} dim(p,q) * sum_{n in sector} ln(lambda_{n,(p,q)}^2)

    where dim(p,q) is the PW multiplicity (each irrep appears dim times in
    L^2(SU(3))). So the weight per eigenvalue in the stored array is dim(p,q).

    Check: sector (0,0) has 16 eigenvalues, weight 1 per eigenvalue.
    Sector (1,0) has 48 eigenvalues, weight 3.
    Total PW-weighted count = 1*16 + 3*48 + 3*48 + 8*128 + 6*96 + 6*96 +
                              10*160 + 10*160 + 15*240 + 15*240
    = 16 + 144 + 144 + 1024 + 576 + 576 + 1600 + 1600 + 3600 + 3600
    = 12880

    But from s61: cum_N_pw at level 3 = 12880. So this is correct.
    """
    tau_key = f'{tau_val:.3f}'
    # Handle case where tau like 0.05 might be stored as 0.050
    # Actually the keys use format tau0.190 etc.

    S1 = 0.0  # (local)
    total_modes = 0  # (local)

    for (p, q) in sectors:
        key = f'evals_tau{tau_val:.3f}_{p}_{q}'
        if key not in data:
            # Try alternative format
            key = f'evals_tau{tau_val:.2f}0_{p}_{q}'
            if key not in data:
                print(f"  WARNING: key {key} not found")
                continue

        evals = data[key]
        dim_pq = su3_dim(p, q)
        pw_weight = dim_pq  # PW multiplicity

        # S_1loop contribution: (1/2) * pw_weight * sum ln(lambda^2)
        # lambda are Dirac eigenvalues, may be positive or negative
        lam_sq = evals**2
        # Avoid ln(0)
        lam_sq = np.maximum(lam_sq, 1e-30)

        contribution = 0.5 * pw_weight * np.sum(np.log(lam_sq))
        S1 += contribution
        total_modes += pw_weight * len(evals)

    return S1, total_modes

# Compute S_1loop at each tau
S1_values = {}
for tau in tau_evals:
    s1, nmodes = compute_S1loop(d_s36, tau, sectors)
    S1_values[tau] = s1
    print(f"  tau={tau:.3f}: S_1loop = {s1:.4f}  (PW-weighted modes: {nmodes})")

# Verify against s62 value at fold
print(f"\n  S_1loop(0.19) from this computation: {S1_values[0.19]:.4f}")
print(f"  S_1loop(0.19) from s62_hessian:      {S1_fold_val:.4f}")

# =============================================================================
# Step 2: Interpolate S_b(tau) at the eigenvalue tau values
# =============================================================================
# S_b is available at tau_combined. Interpolate to the eigenvalue tau grid.

from scipy.interpolate import CubicSpline

# Build cubic spline for S_b
cs_Sb = CubicSpline(tau_combined, S_b_full)

S_b_at_evals = {}
for tau in tau_evals:
    S_b_at_evals[tau] = float(cs_Sb(tau))

print(f"\n--- S_b(tau) interpolated ---")
for tau in tau_evals:
    print(f"  tau={tau:.3f}: S_b = {S_b_at_evals[tau]:.2f}")

# Cross-check at fold
print(f"  S_b(0.19) interpolated: {S_b_at_evals[0.19]:.2f}")
print(f"  S_b(0.19) from s36:     {S_b_fold_val:.2f}")

# =============================================================================
# Step 3: Build S_eff(tau) = S_b(tau) + S_1loop(tau)
# =============================================================================

# Use the tau values near the fold: 0.16, 0.17, 0.18, 0.19, 0.21, 0.22
# (skip 0.05 which is far from fold)
tau_near_fold = np.array([0.16, 0.17, 0.18, 0.19, 0.21, 0.22])
S_b_arr = np.array([S_b_at_evals[t] for t in tau_near_fold])
S1_arr = np.array([S1_values[t] for t in tau_near_fold])
S_eff_arr = S_b_arr + S1_arr

print(f"\n--- S_eff(tau) = S_b(tau) + S_1loop(tau) ---")
print(f"{'tau':>6s}  {'S_b':>14s}  {'S_1loop':>14s}  {'S_eff':>14s}  {'S_1loop/S_b':>12s}")
for i, tau in enumerate(tau_near_fold):
    print(f"{tau:6.3f}  {S_b_arr[i]:14.2f}  {S1_arr[i]:14.4f}  {S_eff_arr[i]:14.2f}  {S1_arr[i]/S_b_arr[i]:12.6f}")

# =============================================================================
# Step 4: Fit smooth interpolant and compute derivatives
# =============================================================================

# Cubic spline for S_eff
cs_eff = CubicSpline(tau_near_fold, S_eff_arr)

# Also fit S_b near fold for comparison
cs_Sb_near = CubicSpline(tau_near_fold, S_b_arr)

# Also fit S_1loop alone
cs_S1 = CubicSpline(tau_near_fold, S1_arr)

# Evaluate at fold tau = 0.19
tau_f = 0.19  # (local)

# S_eff and derivatives at fold
S_eff_fold = float(cs_eff(tau_f))
dSeff_dtau = float(cs_eff(tau_f, 1))  # first derivative
d2Seff_dtau2 = float(cs_eff(tau_f, 2))  # second derivative

# S_b and derivatives at fold (from spline, for cross-check)
S_b_fold_sp = float(cs_Sb_near(tau_f))
dSb_dtau_sp = float(cs_Sb_near(tau_f, 1))
d2Sb_dtau2_sp = float(cs_Sb_near(tau_f, 2))

# S_1loop and derivatives at fold
S1_fold_sp = float(cs_S1(tau_f))
dS1_dtau = float(cs_S1(tau_f, 1))
d2S1_dtau2 = float(cs_S1(tau_f, 2))

print(f"\n--- Derivatives at fold (tau = {tau_f}) ---")
print(f"{'':>12s}  {'Value':>14s}  {'dS/dtau':>14s}  {'d^2S/dtau^2':>14s}")
print(f"{'S_b':>12s}  {S_b_fold_sp:14.2f}  {dSb_dtau_sp:14.2f}  {d2Sb_dtau2_sp:14.2f}")
print(f"{'S_1loop':>12s}  {S1_fold_sp:14.4f}  {dS1_dtau:14.4f}  {d2S1_dtau2:14.4f}")
print(f"{'S_eff':>12s}  {S_eff_fold:14.2f}  {dSeff_dtau:14.2f}  {d2Seff_dtau2:14.2f}")
print(f"\nCross-check S_b derivatives:")
print(f"  dS_b/dtau at fold (spline):    {dSb_dtau_sp:.2f}")
print(f"  dS_b/dtau at fold (canonical): {dSb_fold_val:.2f}")
print(f"  d2S_b/dtau2 at fold (spline):    {d2Sb_dtau2_sp:.2f}")
print(f"  d2S_b/dtau2 at fold (canonical): {d2Sb_fold_val:.2f}")

# =============================================================================
# Step 5: Compute epsilon_1loop
# =============================================================================
# epsilon_H = (1/2) * (S_eff'/S_eff)^2 / (S_eff''/S_eff)
# This is the Hubble slow-roll parameter

epsilon_1loop = 0.5 * (dSeff_dtau / S_eff_fold)**2 / (d2Seff_dtau2 / S_eff_fold)
r_1loop = 16.0 * epsilon_1loop
ns_1loop = 1.0 - 2.0 * epsilon_1loop

# Recompute tree-level for comparison
epsilon_tree_recomp = 0.5 * (dSb_dtau_sp / S_b_fold_sp)**2 / (d2Sb_dtau2_sp / S_b_fold_sp)

print(f"\n{'='*70}")
print(f"SLOW-ROLL PARAMETERS")
print(f"{'='*70}")
print(f"\nTree-level (S_b only):")
print(f"  epsilon_tree = {epsilon_tree:.6f}  (from s62_kz_ns)")
print(f"  epsilon_tree = {epsilon_tree_recomp:.6f}  (recomputed from spline)")
print(f"  r_tree       = {16*epsilon_tree:.4f}")
print(f"  n_s,tree     = {1 - 2*epsilon_tree:.6f}")

print(f"\nOne-loop (S_eff = S_b + S_1loop):")
print(f"  epsilon_1loop = {epsilon_1loop:.6f}")
print(f"  r_1loop       = {r_1loop:.4f}")
print(f"  n_s,1loop     = {ns_1loop:.6f}")

print(f"\nRatios:")
print(f"  epsilon_1loop / epsilon_tree = {epsilon_1loop / epsilon_tree:.4f}")
print(f"  r_1loop / r_tree             = {r_1loop / (16*epsilon_tree):.4f}")

# =============================================================================
# Step 5b: Detailed derivative decomposition
# =============================================================================
# The key physics: how does S_1loop modify the slope and curvature?
#
# S_eff = S_b + S_1loop
# S_eff' = S_b' + S_1loop'
# S_eff'' = S_b'' + S_1loop''
#
# epsilon_eff = (1/2) * [(S_b' + S_1loop') / (S_b + S_1loop)]^2 /
#               [(S_b'' + S_1loop'') / (S_b + S_1loop)]
#
# If S_1loop' has opposite sign to S_b' (counterflow), the numerator shrinks.
# If S_1loop'' has same sign as S_b'' (curvature reinforcement), denominator grows.
# Both effects reduce epsilon.

print(f"\n--- Derivative decomposition ---")
print(f"  S_b'      = {dSb_dtau_sp:+14.4f}   (tree slope)")
print(f"  S_1loop'  = {dS1_dtau:+14.4f}   (one-loop slope)")
print(f"  Ratio S_1loop'/S_b' = {dS1_dtau/dSb_dtau_sp:+.6f}")
slope_sign = "SAME SIGN" if np.sign(dS1_dtau) == np.sign(dSb_dtau_sp) else "OPPOSITE SIGN"
print(f"  Slope relationship: {slope_sign}")
print(f"  Net slope S_eff' = {dSeff_dtau:+14.4f}")
print(f"  Slope reduction factor: {abs(dSeff_dtau/dSb_dtau_sp):.6f}")

print(f"\n  S_b''     = {d2Sb_dtau2_sp:+14.4f}   (tree curvature)")
print(f"  S_1loop'' = {d2S1_dtau2:+14.4f}   (one-loop curvature)")
print(f"  Ratio S_1loop''/S_b'' = {d2S1_dtau2/d2Sb_dtau2_sp:+.6f}")
curv_sign = "SAME SIGN" if np.sign(d2S1_dtau2) == np.sign(d2Sb_dtau2_sp) else "OPPOSITE SIGN"
print(f"  Curvature relationship: {curv_sign}")
print(f"  Net curvature S_eff'' = {d2Seff_dtau2:+14.4f}")

# =============================================================================
# Step 6: Richardson extrapolation for derivative accuracy
# =============================================================================
# The 6-point spline at tau spacing 0.01 near fold is adequate,
# but let's also compute epsilon via finite differences as cross-check.

print(f"\n--- Finite difference cross-check ---")
# 3-point central difference at fold using tau = 0.18, 0.19, 0.21
# (non-uniform spacing: h_left = 0.01, h_right = 0.02)
h1 = 0.19 - 0.18  # = 0.01
h2 = 0.21 - 0.19  # = 0.02
idx_18 = np.where(np.isclose(tau_near_fold, 0.18))[0][0]
idx_19 = np.where(np.isclose(tau_near_fold, 0.19))[0][0]
idx_21 = np.where(np.isclose(tau_near_fold, 0.21))[0][0]

f_m = S_eff_arr[idx_18]
f_0 = S_eff_arr[idx_19]
f_p = S_eff_arr[idx_21]

# Non-uniform finite differences
dSeff_fd = (f_p - f_m) / (h1 + h2)
# Second derivative (non-uniform)
d2Seff_fd = 2 * (h1*f_p - (h1+h2)*f_0 + h2*f_m) / (h1*h2*(h1+h2))

epsilon_fd = 0.5 * (dSeff_fd / f_0)**2 / (d2Seff_fd / f_0)

print(f"  S_eff at tau=0.18: {f_m:.4f}")
print(f"  S_eff at tau=0.19: {f_0:.4f}")
print(f"  S_eff at tau=0.21: {f_p:.4f}")
print(f"  dS_eff/dtau (FD):   {dSeff_fd:.4f}  (spline: {dSeff_dtau:.4f})")
print(f"  d2S_eff/dtau2 (FD): {d2Seff_fd:.4f}  (spline: {d2Seff_dtau2:.4f})")
print(f"  epsilon (FD):       {epsilon_fd:.6f}  (spline: {epsilon_1loop:.6f})")

# Also 5-point stencil using 0.17, 0.18, 0.19, 0.21, 0.22
idx_17 = np.where(np.isclose(tau_near_fold, 0.17))[0][0]
idx_22 = np.where(np.isclose(tau_near_fold, 0.22))[0][0]

# For uniform spacing with gap: use 0.17, 0.18, 0.19, 0.21, 0.22
# Actually spacing is not uniform (0.01, 0.01, 0.02, 0.01)
# Use polynomial fit for robustness
from numpy.polynomial import polynomial as P
tau_fit = tau_near_fold
S_fit = S_eff_arr
# Fit quartic polynomial
coeffs = np.polyfit(tau_fit - tau_f, S_fit, 4)  # centered at fold
# coeffs[0]*x^4 + coeffs[1]*x^3 + coeffs[2]*x^2 + coeffs[3]*x + coeffs[4]
S_eff_poly_fold = coeffs[4]
dSeff_poly = coeffs[3]
d2Seff_poly = 2 * coeffs[2]
epsilon_poly = 0.5 * (dSeff_poly / S_eff_poly_fold)**2 / (d2Seff_poly / S_eff_poly_fold)

print(f"\n  Quartic polynomial fit:")
print(f"  dS_eff/dtau (poly):   {dSeff_poly:.4f}")
print(f"  d2S_eff/dtau2 (poly): {d2Seff_poly:.4f}")
print(f"  epsilon (poly):       {epsilon_poly:.6f}")

# Use average of methods as best estimate
epsilon_methods = np.array([epsilon_1loop, epsilon_fd, epsilon_poly])
epsilon_best = np.median(epsilon_methods)
epsilon_spread = np.max(epsilon_methods) - np.min(epsilon_methods)

print(f"\n  Epsilon estimates: spline={epsilon_1loop:.6f}, FD={epsilon_fd:.6f}, poly={epsilon_poly:.6f}")
print(f"  Best estimate (median): {epsilon_best:.6f}")
print(f"  Spread: {epsilon_spread:.6f}")

# =============================================================================
# Step 7: Analytic understanding of the one-loop correction
# =============================================================================
# Why does epsilon change?
#
# At tree level:
#   epsilon_tree = (1/2) * (S_b'/S_b)^2 / (S_b''/S_b)
#
# Define:
#   alpha = S_1loop / S_b  (ratio at fold)
#   beta  = S_1loop' / S_b' (slope ratio)
#   gamma = S_1loop'' / S_b'' (curvature ratio)
#
# Then:
#   epsilon_eff = epsilon_tree * [(1+beta)/(1+alpha)]^2 / [(1+gamma)/(1+alpha)]
#               = epsilon_tree * (1+beta)^2 / [(1+alpha)(1+gamma)]

alpha = S1_fold_sp / S_b_fold_sp
beta = dS1_dtau / dSb_dtau_sp
gamma = d2S1_dtau2 / d2Sb_dtau2_sp

epsilon_analytic = epsilon_tree_recomp * (1 + beta)**2 / ((1 + alpha) * (1 + gamma))

print(f"\n--- Analytic decomposition ---")
print(f"  alpha = S_1loop/S_b         = {alpha:.6f}")
print(f"  beta  = S_1loop'/S_b'       = {beta:.6f}")
print(f"  gamma = S_1loop''/S_b''     = {gamma:.6f}")
print(f"  Modification factor:")
print(f"    (1+beta)^2 / [(1+alpha)(1+gamma)] = {(1+beta)**2 / ((1+alpha)*(1+gamma)):.6f}")
print(f"  epsilon_analytic = epsilon_tree * factor = {epsilon_analytic:.6f}")
print(f"  epsilon_spline   = {epsilon_1loop:.6f}")
print(f"  Consistency check: {abs(epsilon_analytic - epsilon_1loop)/epsilon_1loop*100:.4f}%")

# =============================================================================
# Step 8: Sensitivity analysis
# =============================================================================
# How sensitive is epsilon to the one-loop contribution?
# Scan S_1loop weight from 0 (tree) to 1 (full one-loop)

print(f"\n--- Sensitivity: epsilon vs one-loop weight ---")
print(f"{'weight':>8s}  {'epsilon':>12s}  {'r':>10s}  {'n_s':>10s}")
for w in [0.0, 0.25, 0.5, 0.75, 1.0]:
    S_test = S_b_arr + w * S1_arr
    cs_test = CubicSpline(tau_near_fold, S_test)
    S_val = float(cs_test(tau_f))
    dS_val = float(cs_test(tau_f, 1))
    d2S_val = float(cs_test(tau_f, 2))
    eps_test = 0.5 * (dS_val / S_val)**2 / (d2S_val / S_val)
    print(f"{w:8.2f}  {eps_test:12.6f}  {16*eps_test:10.4f}  {1-2*eps_test:10.6f}")

# =============================================================================
# Step 9: Extended tau range — include tau=0.05 for broader picture
# =============================================================================

tau_all = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])
S_b_all = np.array([float(cs_Sb(t)) for t in tau_all])
S1_all = np.array([S1_values[t] for t in tau_all])
S_eff_all = S_b_all + S1_all

print(f"\n--- Full S_eff profile ---")
print(f"{'tau':>6s}  {'S_b':>14s}  {'S_1loop':>14s}  {'S_eff':>14s}  {'S_1loop/S_eff':>14s}")
for i, tau in enumerate(tau_all):
    print(f"{tau:6.3f}  {S_b_all[i]:14.2f}  {S1_all[i]:14.4f}  {S_eff_all[i]:14.2f}  {S1_all[i]/S_eff_all[i]:14.6f}")

# =============================================================================
# Step 10: Gate verdict
# =============================================================================

r_final = 16.0 * epsilon_best
ns_final = 1.0 - 2.0 * epsilon_best

if epsilon_best < 0.00225:
    verdict = "PASS"
    detail = f"epsilon_1loop = {epsilon_best:.6f} < 0.00225. r = {r_final:.4f} < 0.036."
elif epsilon_best > 0.00625:
    verdict = "FAIL"
    detail = f"epsilon_1loop = {epsilon_best:.6f} > 0.00625. r = {r_final:.4f} > 0.1."
else:
    verdict = "INFO"
    detail = f"epsilon_1loop = {epsilon_best:.6f} in [0.00225, 0.00625]. r = {r_final:.4f} in [0.036, 0.1]."

print(f"\n{'='*70}")
print(f"GATE: ONELOOP-EPSILON-63")
print(f"VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print(f"{'='*70}")

print(f"\nKey results:")
print(f"  epsilon_tree  = {epsilon_tree:.6f}  (r_tree  = {16*epsilon_tree:.4f})")
print(f"  epsilon_1loop = {epsilon_best:.6f}  (r_1loop = {r_final:.4f})")
print(f"  n_s,1loop     = {ns_final:.6f}")
print(f"  Reduction factor: {epsilon_best/epsilon_tree:.4f}")
print(f"  One-loop slope ratio beta  = {beta:.6f}")
print(f"  One-loop curv ratio gamma  = {gamma:.6f}")
print(f"  One-loop value ratio alpha = {alpha:.6f}")

# =============================================================================
# Save output
# =============================================================================

outpath = script_dir / 's63_oneloop_epsilon.npz'
np.savez(
    outpath,
    # Gate
    gate_name='ONELOOP-EPSILON-63',
    gate_verdict=verdict,
    gate_detail=detail,

    # Profiles (near fold)
    tau_near_fold=tau_near_fold,
    S_b_profile=S_b_arr,
    S_1loop_profile=S1_arr,
    S_eff_profile=S_eff_arr,

    # Full profiles
    tau_all=tau_all,
    S_b_all=S_b_all,
    S_1loop_all=S1_all,
    S_eff_all=S_eff_all,

    # Derivatives at fold
    S_eff_fold=S_eff_fold,
    dSeff_dtau=dSeff_dtau,
    d2Seff_dtau2=d2Seff_dtau2,
    dSb_dtau=dSb_dtau_sp,
    d2Sb_dtau2=d2Sb_dtau2_sp,
    dS1_dtau=dS1_dtau,
    d2S1_dtau2=d2S1_dtau2,

    # Slow-roll parameters
    epsilon_tree=epsilon_tree,
    epsilon_1loop_spline=epsilon_1loop,
    epsilon_1loop_fd=epsilon_fd,
    epsilon_1loop_poly=epsilon_poly,
    epsilon_1loop=epsilon_best,
    r_tree=16.0 * epsilon_tree,
    r_1loop=r_final,
    ns_tree=1.0 - 2.0 * epsilon_tree,
    ns_1loop=ns_final,

    # Decomposition
    alpha_ratio=alpha,
    beta_ratio=beta,
    gamma_ratio=gamma,
    modification_factor=(1+beta)**2 / ((1+alpha)*(1+gamma)),

    # Method spread
    epsilon_methods=epsilon_methods,
    epsilon_spread=epsilon_spread,

    # Metadata
    tau_fold=tau_f,
    Lambda_sq=Lambda_sq,
    g_coupling=g_coupling,
    S1_over_Sb=S1_fold_sp / S_b_fold_sp,
    n_sectors=len(sectors),
    max_pq_sum=3,
)

print(f"\nOutput saved to: {outpath}")
print(f"File size: {outpath.stat().st_size} bytes")

# =============================================================================
# Plot
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ONELOOP-EPSILON-63: One-Loop Effective Slow-Roll', fontsize=14, fontweight='bold')

# Panel 1: S_b, S_1loop, S_eff vs tau
ax = axes[0, 0]
ax.plot(tau_near_fold, S_b_arr / 1e3, 'b-o', label=r'$S_b(\tau)$', markersize=4)
ax.plot(tau_near_fold, S_eff_arr / 1e3, 'r-s', label=r'$S_\mathrm{eff}(\tau)$', markersize=4)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S \times 10^{-3}$')
ax.set_title('Spectral Action Profiles')
ax.legend()
ax.axvline(x=0.19, color='gray', linestyle='--', alpha=0.5, label='fold')
ax.grid(True, alpha=0.3)

# Panel 2: S_1loop vs tau
ax = axes[0, 1]
ax.plot(tau_near_fold, S1_arr, 'g-^', label=r'$S_\mathrm{1loop}(\tau)$', markersize=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_\mathrm{1loop}$')
ax.set_title('One-Loop Correction')
ax.legend()
ax.axvline(x=0.19, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)

# Panel 3: epsilon vs one-loop weight
ax = axes[1, 0]
weights = np.linspace(0, 1, 50)
eps_vs_w = []
for w in weights:
    S_test = S_b_arr + w * S1_arr
    cs_test = CubicSpline(tau_near_fold, S_test)
    S_val = float(cs_test(tau_f))
    dS_val = float(cs_test(tau_f, 1))
    d2S_val = float(cs_test(tau_f, 2))
    eps_test = 0.5 * (dS_val / S_val)**2 / (d2S_val / S_val)
    eps_vs_w.append(eps_test)
eps_vs_w = np.array(eps_vs_w)

ax.semilogy(weights, eps_vs_w, 'k-', linewidth=2)
ax.axhline(y=0.00225, color='g', linestyle='--', alpha=0.7, label='PASS threshold')
ax.axhline(y=0.00625, color='r', linestyle='--', alpha=0.7, label='FAIL threshold')
ax.axhline(y=epsilon_tree, color='b', linestyle=':', alpha=0.7, label=f'tree: {epsilon_tree:.4f}')
ax.axvline(x=1.0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('One-loop weight')
ax.set_ylabel(r'$\epsilon$')
ax.set_title(r'$\epsilon$ vs One-Loop Weight')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Summary bar chart
ax = axes[1, 1]
categories = ['Tree', '1-loop\n(spline)', '1-loop\n(FD)', '1-loop\n(poly)', '1-loop\n(best)']
values = [epsilon_tree, epsilon_1loop, epsilon_fd, epsilon_poly, epsilon_best]
colors = ['blue', 'orange', 'orange', 'orange', 'red']
bars = ax.bar(categories, values, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(y=0.00225, color='g', linestyle='--', linewidth=2, label='PASS')
ax.axhline(y=0.00625, color='r', linestyle='--', linewidth=2, label='FAIL')
ax.set_ylabel(r'$\epsilon$')
ax.set_title(f'Epsilon Comparison (verdict: {verdict})')
ax.legend()
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.0005,
            f'{val:.4f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
pngpath = script_dir / 's63_oneloop_epsilon.png'
plt.savefig(pngpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {pngpath}")
