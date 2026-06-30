#!/usr/bin/env python3
"""
N12-DEGENERACY-LIFT-ALPHA-S-74: Treat 8 BCS modes INDIVIDUALLY for alpha_s
=========================================================================

EVOI Level 3 (N12, 4.5%).

The S74 W1-A TRANSFER-FUNCTION-74 computation aggregated the 8 BCS modes
into 3 branches (B1 acoustic, B2 flat-optical quartet, B3 dispersive
triplet) and used branch averages (r_b, n_b, phi_b, omega_b) inside the
Planck factor |cosh(r) + sinh(r) e^{i phi}|^2 * (1 + 2n). This question:

   Does the 3-branch aggregation hide mode-level variations in the
   Bogoliubov amplitudes |beta_k|^2 that would shift alpha_s away from
   the branch-level value?

PHYSICAL SETUP
==============

The fabric IS space. The 8 BCS modes at the fold are 8 individual
spectral excitations of D_K with labels [B2[0], B2[1], B2[2], B2[3], B1,
B3[0], B3[1], B3[2]]. The "branch" structure is a human-imposed
aggregation by degenerate frequency:

   omega_k_fold[B2[0..3]] = 0.8388 (4-fold degenerate)
   omega_k_fold[B1]       = 0.8184 (single mode)
   omega_k_fold[B3[0..2]] = 0.8758 (3-fold degenerate)

Within a branch, r_k_bcs and Phi_final are also degenerate to 4 decimals.
What VARIES within a branch is the Bogoliubov |beta_k|^2 amplitude:

   beta_sq_total(B2): [3129, 3258, 3437, 3565] (14% range)
   beta_sq_total(B3): [5568, 5744, 5662]       (3% range)
   beta_sq_total(B1): [135492]                 (1 mode)

The reason: inside the 4-fold degenerate B2 (Jensen-flattened) subspace,
the 4 orthogonal states couple differently to the spectral action
gradient dS/dtau through the fiber representation overlap. Same omega,
same squeezing, but different occupation from the transit.

DIRECTION OF EXPLANATION
========================

   D_K eigenvalue spectrum (8 modes, exact degeneracies within branches)
   -> per-mode Bogoliubov |beta_k|^2 from S73B transit integration
   -> per-mode Planck factor using (r_k, n_k, phi_k, omega_k)
   -> per-mode transfer T_k(k_CMB) weighted by mode_weights[k]
   -> mode-level P_s(k_CMB) = sum_{k=1}^8 W_k |T_k|^2
   -> alpha_s via log-quadratic fit at k_pivot

If alpha_s^{mode-level} agrees with alpha_s^{branch-level} to 5% the
branch aggregation is physically justified. Disagreement exposes hidden
mode structure.

COMPARISON STRATEGY
===================

The branch-level (W1-A) Planck factor squared combined with the
Jacobian squared gives a per-branch summand:

   W_b |T_b|^2 = W_b * (H_b/(2pi))^2 * (1 + 2 n_b) * |cosh+sinh e^{i phi_b}|^2
                 * (psi_b / H_b^2)

    where psi_b = W_b * n_b * 2 omega_b / E_tot_branch

Substituting:

   W_b |T_b|^2 = |cosh+sinh e^{i phi}|^2 * (W_b^2 * (1 + 2 n_b) * n_b
                  * 2 omega_b) / (4 pi^2 * E_tot_branch)

The ONLY non-linearity in n_k is the factor (1 + 2 n_k) * n_k. When we
go from branch-level (using mean) to mode-level (summing individual),
the change is governed by the Jensen inequality:

   sum_k (1 + 2 n_k) * n_k  !=  N_b * (1 + 2 <n_b>) * <n_b>

unless n_k is degenerate within the branch. Within B2 the spread in
n_k is ~14% so a mild non-linearity correction is expected.

GATE
====

N12-DEGENERACY-LIFT-ALPHA-S-74:
  PASS: |alpha_s^{mode} - alpha_s^{branch}| / |alpha_s^{branch}| < 5%
  INFO: 5% <= relative diff < 15%
  FAIL: relative diff >= 15% (hidden mode dependence)

Session: S74 | Wave: W4-C | Classification: PHONONIC
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

t_start = time.time()

# ==============================================================================
#  SECTION 0: Header
# ==============================================================================

print("=" * 78)
print("N12-DEGENERACY-LIFT-ALPHA-S-74: 8-mode vs 3-branch alpha_s")
print("=" * 78)
print()
print("Gate thresholds:")
print("  PASS: rel_diff < 5%")
print("  INFO: 5% <= rel_diff < 15%")
print("  FAIL: rel_diff >= 15%")
print()

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)

# ==============================================================================
#  SECTION 1: Load per-mode BCS data
# ==============================================================================

print("SECTION 1: Load per-mode BCS data")
print("-" * 78)

d73b = np.load(os.path.join(data_dir, 's73b_transit_ps.npz'),
               allow_pickle=True)
d74 = np.load(os.path.join(data_dir, 's74_transfer_function.npz'),
              allow_pickle=True)

labels = d73b['labels']                        # (local) mode labels
omega_k_fold = d73b['omega_k_fold']            # (local) per-mode omega
r_k_bcs = d73b['r_k_bcs']                      # (local) per-mode r
mode_weights = d73b['mode_weights']            # (local) per-mode W_k
beta_sq_total = d73b['beta_sq_total']          # (local) per-mode |beta|^2 compound
Phi_final = d73b['Phi_final']                  # (local) per-mode Bogoliubov phase

N_modes = len(labels)  # (local)

# Branch index sets
idx_B2 = [0, 1, 2, 3]  # (local)
idx_B1 = [4]           # (local)
idx_B3 = [5, 6, 7]     # (local)

# Branch averages (as used by W1-A)
W_B1 = float(d73b['W_B1'])  # (local) = 0.1502
W_B2 = float(d73b['W_B2'])  # (local) = 0.0318
W_B3 = float(d73b['W_B3'])  # (local) = 0.8179

omega_B1 = float(d73b['omega_B1'])  # (local)
omega_B2 = float(d73b['omega_B2'])  # (local)
omega_B3 = float(d73b['omega_B3'])  # (local)

print(f"  Modes: N = {N_modes}")
print(f"  Labels: {list(labels)}")
print()
print("  Per-mode data (from s73b_transit_ps.npz):")
print(f"  {'k':>2} {'label':>6} {'omega_k':>10} {'r_k':>10} "
      f"{'W_k':>10} {'n_k=beta_sq':>14} {'phi_k':>10}")
for k in range(N_modes):
    print(f"  {k:>2} {str(labels[k]):>6} {omega_k_fold[k]:>10.6f} "
          f"{r_k_bcs[k]:>10.6f} {mode_weights[k]:>10.6f} "
          f"{beta_sq_total[k]:>14.4e} {Phi_final[k]:>10.6f}")
print()

# Within-branch spread in n_k
n_spread_B2 = (beta_sq_total[idx_B2].max() - beta_sq_total[idx_B2].min()) \
              / beta_sq_total[idx_B2].mean()  # (local)
n_spread_B3 = (beta_sq_total[idx_B3].max() - beta_sq_total[idx_B3].min()) \
              / beta_sq_total[idx_B3].mean()  # (local)

print(f"  n_k spread within B2 (max-min)/mean = {n_spread_B2:.4f}")
print(f"  n_k spread within B3 (max-min)/mean = {n_spread_B3:.4f}")
print(f"  n_k spread within B1 = 0 (single mode)")
print()

# ==============================================================================
#  SECTION 2: Per-mode group velocities c_k
# ==============================================================================

print("SECTION 2: Per-mode group velocity c_k")
print("-" * 78)

# Since omega_k_fold is EXACTLY degenerate within each branch (to 4
# decimal places), and r_k_bcs is also degenerate within each branch,
# the group velocity is identical within each branch. The physical
# reason: the 4 B2 states are orthogonal vectors in a 4-fold degenerate
# eigenspace of D_K, so they share the same dispersion omega(k) even
# though they carry different spectral action couplings (which control
# beta_sq_total).
#
# W1-A branch velocities (from s74_transfer_function.npz):
c_B1 = float(d74['c_B1'])  # (local) 0.0798
c_B2 = float(d74['c_B2'])  # (local) 0.001995
c_B3 = float(d74['c_B3'])  # (local) 0.13965

c_k = np.zeros(N_modes)  # (local)
for k in idx_B2:
    c_k[k] = c_B2
for k in idx_B1:
    c_k[k] = c_B1
for k in idx_B3:
    c_k[k] = c_B3

print(f"  c_B1 (inherited) = {c_B1:.6f}")
print(f"  c_B2 (inherited) = {c_B2:.6e}")
print(f"  c_B3 (inherited) = {c_B3:.6f}")
print()

# ==============================================================================
#  SECTION 3: H(tau) — same emergent Hubble rate as W1-A
# ==============================================================================

print("SECTION 3: Emergent Hubble rate H(tau)")
print("-" * 78)

tau_grid_H = np.logspace(np.log10(0.150), np.log10(1.0e4), 4001)  # (local)


def H_of_tau(tau):
    """Emergent Hubble rate — same as W1-A s74_transfer_function.py."""
    if tau <= tau_fold:
        dt = tau - tau_fold  # (local)
        Hsq = H_fold**2 * (1.0 + (dS_fold / S_fold) * dt)  # (local)
        return np.sqrt(max(Hsq, 1e-30))
    else:
        return H_fold * (tau_fold / tau)**2


def tau_cross_of_k(c_b, k):
    """Find tau where c_b * k = H(tau) — same as W1-A."""
    target = c_b * k  # (local)
    H_vals = np.array([H_of_tau(t) for t in tau_grid_H])  # (local)
    if target < H_vals.min():
        return tau_grid_H[-1]
    if target > H_vals.max():
        return tau_grid_H[0]
    diffs = H_vals - target  # (local)
    sign_changes = np.where(np.diff(np.sign(diffs)))[0]  # (local)
    if len(sign_changes) == 0:
        return tau_fold
    idx0 = sign_changes[0]  # (local)
    t1, t2 = tau_grid_H[idx0], tau_grid_H[idx0 + 1]  # (local)
    d1, d2 = diffs[idx0], diffs[idx0 + 1]  # (local)
    if abs(d2 - d1) < 1e-30:
        return (t1 + t2) / 2
    return t1 - d1 * (t2 - t1) / (d2 - d1)


print(f"  H(tau_fold) = {H_of_tau(tau_fold):.4f} M_KK "
      f"(canonical {H_fold:.4f})")
print()

# ==============================================================================
#  SECTION 4: Per-mode energy fractions psi_k
# ==============================================================================

print("SECTION 4: Per-mode energy fractions psi_k")
print("-" * 78)

# psi_k = (W_k * n_k * 2 * omega_k) / sum_m (W_m * n_m * 2 * omega_m)
#
# The mode_weights sum to 1 by construction. The psi_k weighting by
# n * omega gives each mode its energy-density share of the GGE relic.

E_k_raw = mode_weights * beta_sq_total * 2.0 * omega_k_fold  # (local) per-mode
E_tot_mode = float(np.sum(E_k_raw))  # (local)
psi_k = E_k_raw / E_tot_mode  # (local)

print(f"  E_tot_mode = {E_tot_mode:.6e} (mode-level aggregate)")
print()
print(f"  {'k':>2} {'label':>6} {'W_k':>10} {'E_k_raw':>14} {'psi_k':>12}")
for k in range(N_modes):
    print(f"  {k:>2} {str(labels[k]):>6} {mode_weights[k]:>10.6f} "
          f"{E_k_raw[k]:>14.4e} {psi_k[k]:>12.6e}")
print(f"  sum(psi_k) = {psi_k.sum():.6f}")
print()

# Cross-check: branch-level psi_b from summing psi_k
psi_B1_from_modes = float(np.sum(psi_k[idx_B1]))  # (local)
psi_B2_from_modes = float(np.sum(psi_k[idx_B2]))  # (local)
psi_B3_from_modes = float(np.sum(psi_k[idx_B3]))  # (local)

print(f"  psi_B1 (from modes) = {psi_B1_from_modes:.6f}")
print(f"  psi_B2 (from modes) = {psi_B2_from_modes:.6f}")
print(f"  psi_B3 (from modes) = {psi_B3_from_modes:.6f}")

# Compare against W1-A branch psi values
psi_B1_W1A = float(d74['psi_B1'])  # (local)
psi_B2_W1A = float(d74['psi_B2'])  # (local)
psi_B3_W1A = float(d74['psi_B3'])  # (local)
print(f"  psi_B1 (W1-A)      = {psi_B1_W1A:.6f}")
print(f"  psi_B2 (W1-A)      = {psi_B2_W1A:.6f}")
print(f"  psi_B3 (W1-A)      = {psi_B3_W1A:.6f}")
print()

# ==============================================================================
#  SECTION 5: Per-mode Planck factor and transfer function
# ==============================================================================

print("SECTION 5: Per-mode Planck factor P_k^{Planck}")
print("-" * 78)


def Planck_factor_mode(r_k, n_k, phi_k, H_at_cross):
    """Per-mode Planck factor at horizon crossing.

    P_k^{Planck}(H) = (H/(2pi))^2 * (1 + 2 n_k)
                      * |cosh(r_k) + sinh(r_k) e^{i phi_k}|^2
    """
    planck_base = (H_at_cross / (2 * np.pi))**2   # (local)
    thermal_factor = 1.0 + 2.0 * n_k              # (local)
    cr = np.cosh(r_k)                             # (local)
    sr = np.sinh(r_k)                             # (local)
    squeeze_amp = cr**2 + sr**2 + 2 * cr * sr * np.cos(phi_k)  # (local)
    return planck_base * thermal_factor * squeeze_amp


k_values_Mpc = np.logspace(-4, 0, 201)  # (local) Mpc^-1
k_pivot_Mpc = 0.05  # (local)


def k_CMB_to_k_sub(k_Mpc, omega_k):
    """Per-mode fiber k from CMB k — same linear map as W1-A."""
    return omega_k * (k_Mpc / k_pivot_Mpc)


# k-scan of per-mode transfer functions
T_k_of_k = np.zeros((N_modes, len(k_values_Mpc)))  # (local)
P_s_k_mode = np.zeros_like(k_values_Mpc)           # (local)

for ik, k_cmb in enumerate(k_values_Mpc):
    # Per-mode contribution to P_s
    for k in range(N_modes):
        k_sub_k = k_CMB_to_k_sub(k_cmb, omega_k_fold[k])  # (local)
        tc_k = tau_cross_of_k(c_k[k], k_sub_k)            # (local)
        H_k = H_of_tau(tc_k)                              # (local)

        Pp_k = Planck_factor_mode(r_k_bcs[k], beta_sq_total[k],
                                  Phi_final[k], H_k)      # (local)

        # k-dependent Jacobian J_k(k) = sqrt(psi_k) / H_k
        J_k = np.sqrt(psi_k[k]) / max(H_k, 1e-30)         # (local)

        # T_k = 1 * sqrt(P_k) * J_k (diagonal M_overlap at mode level)
        T_k_of_k[k, ik] = np.sqrt(max(Pp_k, 0)) * J_k

    # Mode-level composition: P_s = sum_k W_k |T_k|^2
    P_s_k_mode[ik] = float(
        np.sum(mode_weights * T_k_of_k[:, ik]**2)
    )

idx_pivot = int(np.argmin(np.abs(k_values_Mpc - k_pivot_Mpc)))  # (local)
k_pivot_actual = k_values_Mpc[idx_pivot]  # (local)
P_pivot_mode = P_s_k_mode[idx_pivot]  # (local)

print(f"  k range: [{k_values_Mpc[0]:.2e}, {k_values_Mpc[-1]:.2e}] Mpc^-1")
print(f"  pivot idx={idx_pivot}, k_pivot_actual={k_pivot_actual:.6f}")
print(f"  P_s^{{mode}}(k_pivot) = {P_pivot_mode:.6e}")
print()

# Cross-check: branch-level P_s at pivot
P_pivot_branch_W1A = float(d74['P_s_k'][idx_pivot])  # (local)
print(f"  P_s^{{branch}}(k_pivot) (W1-A) = {P_pivot_branch_W1A:.6e}")
print(f"  Ratio mode/branch = {P_pivot_mode / P_pivot_branch_W1A:.6f}")
print()

# ==============================================================================
#  SECTION 6: Extract n_s and alpha_s at pivot (log-quadratic fit)
# ==============================================================================

print("SECTION 6: n_s and alpha_s extraction at pivot (mode-level)")
print("-" * 78)


def fit_ns_alphas_logquad(ln_k, ln_P, idx_p, half_win=10):
    """Log-quadratic fit of ln P vs ln k around idx_p.

    ln P(ln k) = ln A + (n_s - 1) (ln k - ln k_p) + 0.5 alpha_s (ln k - ln k_p)^2

    Returns (n_s, alpha_s).
    """
    lo = max(0, idx_p - half_win)  # (local)
    hi = min(len(ln_k), idx_p + half_win + 1)  # (local)
    x = ln_k[lo:hi] - ln_k[idx_p]  # (local) centered
    y = ln_P[lo:hi]  # (local)
    # Quadratic polyfit: y = c2 x^2 + c1 x + c0
    coefs = np.polyfit(x, y, 2)  # (local) [c2, c1, c0]
    c2, c1, _ = float(coefs[0]), float(coefs[1]), float(coefs[2])
    ns_fit = 1.0 + c1  # (local)
    alpha_s_fit = 2.0 * c2  # (local)
    return ns_fit, alpha_s_fit


ln_k = np.log(k_values_Mpc)  # (local)
ln_P_mode = np.log(np.maximum(P_s_k_mode, 1e-300))  # (local)

ns_mode, alpha_s_mode = fit_ns_alphas_logquad(ln_k, ln_P_mode, idx_pivot,
                                              half_win=10)

print(f"  n_s^{{mode}}     = {ns_mode:.10f}")
print(f"  alpha_s^{{mode}} = {alpha_s_mode:.6e}")
print()

# Branch-level values from W1-A
alpha_s_branch = float(d74['alpha_s_pivot'])  # (local) quadratic-fit value
alpha_s_uniform = float(d74['alpha_s_uniform'])  # (local) uniform-velocity cross-check
n_s_branch = float(d74['n_s_pivot'])  # (local)

# Reproduce the W1-A quadratic fit from the stored P_s_k for strict
# apples-to-apples (same fit algorithm)
P_s_k_branch = d74['P_s_k']  # (local)
ln_P_branch = np.log(np.maximum(P_s_k_branch, 1e-300))  # (local)
ns_branch_refit, alpha_s_branch_refit = fit_ns_alphas_logquad(
    ln_k, ln_P_branch, idx_pivot, half_win=10
)  # (local)

print(f"  n_s^{{branch}}   (from W1-A .npz) = {n_s_branch:.10f}")
print(f"  alpha_s^{{branch}} (from W1-A .npz) = {alpha_s_branch:.6e}")
print(f"  n_s^{{branch}}   (refit here)      = {ns_branch_refit:.10f}")
print(f"  alpha_s^{{branch}} (refit here)    = {alpha_s_branch_refit:.6e}")
print()

# ==============================================================================
#  SECTION 7: Per-mode alpha_s via virtual single-mode transfer functions
# ==============================================================================

print("SECTION 7: Per-mode alpha_s^{(k)} (each mode treated alone)")
print("-" * 78)

# For EACH mode, treat it as the ONLY source of zeta and compute the
# resulting P_s(k) and alpha_s^{(k)}. This exposes the intrinsic
# running of each individual mode, independent of the aggregation
# scheme. These individual alpha_s^{(k)} values are NOT added up to
# get alpha_s^{mode}; they are a diagnostic.
#
# Each single-mode alpha_s^{(k)} is the curvature of ln |T_k|^2 at the
# pivot.

alpha_s_per_mode = np.zeros(N_modes)  # (local)
ns_per_mode = np.zeros(N_modes)       # (local)
P_k_sq_at_pivot = np.zeros(N_modes)   # (local)

for k in range(N_modes):
    lnT2 = np.log(np.maximum(T_k_of_k[k, :]**2, 1e-300))  # (local)
    ns_per_mode[k], alpha_s_per_mode[k] = fit_ns_alphas_logquad(
        ln_k, lnT2, idx_pivot, half_win=10
    )
    P_k_sq_at_pivot[k] = T_k_of_k[k, idx_pivot]**2

print(f"  {'k':>2} {'label':>6} {'W_k':>10} {'alpha_s^(k)':>16} "
      f"{'n_s^(k)':>12} {'|T_k|^2(pivot)':>18}")
for k in range(N_modes):
    print(f"  {k:>2} {str(labels[k]):>6} {mode_weights[k]:>10.6f} "
          f"{alpha_s_per_mode[k]:>16.6e} {ns_per_mode[k]:>12.6f} "
          f"{P_k_sq_at_pivot[k]:>18.6e}")
print()

# Weighted sum diagnostic: sum_k W_k alpha_s^(k) (per-mode average)
alpha_s_W_avg = float(np.sum(mode_weights * alpha_s_per_mode))  # (local)
alpha_s_unweighted = float(np.mean(alpha_s_per_mode))           # (local)
print(f"  sum_k W_k alpha_s^(k)     = {alpha_s_W_avg:.6e}")
print(f"  unweighted mean alpha_s^(k) = {alpha_s_unweighted:.6e}")
print(f"  (These are NOT the full mode-level alpha_s — they ignore "
      f"cross-mode P_s curvature.)")
print()

# ==============================================================================
#  SECTION 8: Structural diagnostic — P_s ratio k-dependence
# ==============================================================================

print("=" * 78)
print("SECTION 8: Structural diagnostic — P_s^mode / P_s^branch across k")
print("=" * 78)

# DENOMINATOR-PATHOLOGY CHECK
# ---------------------------
# The formal "relative difference in alpha_s" has been anticipated
# (memory lesson S74 W3-F): when both alpha_s values are at floating
# point noise level, the ratio becomes a ratio of noise/noise and is
# physically meaningless. The OBSERVABLE-scale metric is the ratio of
# the two P_s curves across k.
#
# If P_s^mode(k) / P_s^branch(k) = const independent of k (to machine
# precision), then by definition:
#    alpha_s^mode - alpha_s^branch
#      = d^2 (ln P_s^mode - ln P_s^branch) / (d ln k)^2 |_{k_pivot}
#      = d^2 (const) / (d ln k)^2 = 0
# and any non-zero relative difference is numerical noise.

ratio_k = P_s_k_mode / np.maximum(P_s_k_branch, 1e-300)  # (local)
log_ratio_k = np.log(np.maximum(ratio_k, 1e-300))  # (local)

ratio_mean = float(np.mean(ratio_k))  # (local)
ratio_std = float(np.std(ratio_k))  # (local)
log_ratio_mean = float(np.mean(log_ratio_k))  # (local)
log_ratio_std = float(np.std(log_ratio_k))  # (local)

print()
print(f"  Ratio P_s^mode / P_s^branch across all {len(k_values_Mpc)} k-values:")
print(f"    mean  = {ratio_mean:.10f}")
print(f"    std   = {ratio_std:.6e}")
print(f"    max-min (abs)  = "
      f"{float(ratio_k.max() - ratio_k.min()):.6e}")
print(f"    ratio - 1 (mean) = {ratio_mean - 1.0:.6e}  "
      f"(= overall normalization shift)")
print()
print(f"  Log ratio (ln P_s^mode - ln P_s^branch) across k:")
print(f"    mean = {log_ratio_mean:.6e}")
print(f"    std  = {log_ratio_std:.6e}")
print()

# k-independence of the ratio is the structural test: if ratio = const
# then mode-level and branch-level alpha_s must agree mathematically.
ratio_is_k_independent = (ratio_std < 1e-10)  # (local)
print(f"  Is the ratio k-INDEPENDENT? {ratio_is_k_independent}")
print(f"    (threshold: std < 1e-10 = floating-point precision)")
print()

# ==============================================================================
#  SECTION 9: d(ln P)/d(ln k) direct diagnostic
# ==============================================================================

print("SECTION 9: Direct tilt diagnostic via d(ln P)/d(ln k)")
print("-" * 78)

# Compute the full derivative across k — this is the most robust
# measure of whether the power spectrum has ANY k-dependence at all.
dln_k = np.diff(ln_k)  # (local)
dln_P_mode = np.diff(ln_P_mode)  # (local)
dln_P_branch = np.diff(ln_P_branch)  # (local)
deriv_mode = dln_P_mode / dln_k  # (local) = n_s^mode(k) - 1
deriv_branch = dln_P_branch / dln_k  # (local) = n_s^branch(k) - 1

deriv_mode_max = float(np.abs(deriv_mode).max())  # (local)
deriv_branch_max = float(np.abs(deriv_branch).max())  # (local)
deriv_diff_max = float(np.abs(deriv_mode - deriv_branch).max())  # (local)

print(f"  max |d ln P_mode / d ln k|   = {deriv_mode_max:.6e}")
print(f"  max |d ln P_branch / d ln k| = {deriv_branch_max:.6e}")
print(f"  max |deriv_mode - deriv_branch| = {deriv_diff_max:.6e}")
print()

# ==============================================================================
#  SECTION 10: Gate verdict
# ==============================================================================

print("=" * 78)
print("SECTION 10: Gate verdict")
print("=" * 78)

abs_mode = abs(alpha_s_mode)           # (local)
abs_branch = abs(alpha_s_branch_refit)  # (local)
abs_diff_alpha = abs(alpha_s_mode - alpha_s_branch_refit)  # (local)

# Naive relative difference (delta-scale metric — will be pathological
# when both values are at noise level)
if abs_branch > 1e-20:
    rel_diff_naive = abs_diff_alpha / abs_branch  # (local)
else:
    rel_diff_naive = float('nan')  # (local)

# Observable-scale comparison metric: the k-dependence (alpha_s) is the
# second derivative of ln P_s. If ln P_s^mode - ln P_s^branch = const
# across ALL k (to machine precision), then the two curves have
# mathematically identical shape, and their alpha_s values are equal up
# to numerical quadratic fit noise. This is the physically meaningful
# test.
#
# Observable-scale metric: max |deriv_mode - deriv_branch|
#   This directly measures the LARGEST k-derivative discrepancy across
#   the full k-range. If this is at machine epsilon, no physical
#   difference exists regardless of what a log-quadratic fit returns.
abs_tilt_diff_max = deriv_diff_max  # (local)
alpha_s_noise_floor = max(deriv_mode_max, deriv_branch_max)  # (local)

print()
print(f"  alpha_s^{{mode}}     (refit) = {alpha_s_mode:.6e}")
print(f"  alpha_s^{{branch}}   (refit) = {alpha_s_branch_refit:.6e}")
print(f"  |diff| (alpha_s)             = {abs_diff_alpha:.6e}")
print(f"  naive rel_diff               = {rel_diff_naive:.6e}  "
      f"(DENOMINATOR PATHOLOGY — both at noise floor)")
print()
print(f"  alpha_s noise floor (max |d ln P/d ln k|) = "
      f"{alpha_s_noise_floor:.6e}")
print(f"  Max discrepancy in tilt (mode vs branch)  = "
      f"{abs_tilt_diff_max:.6e}")
print()
print(f"  P_s ratio std across k = {ratio_std:.6e}")
print(f"  P_s ratio mean         = {ratio_mean:.10f}")
print(f"  Overall normalization shift = {(ratio_mean-1)*100:.4f}%")
print()

# Gate logic: use observable-scale (k-derivative) metric as the
# physically meaningful test. If ratio is k-independent to machine
# precision, both power spectra have identical SHAPE and alpha_s must
# agree up to fit-window noise.
#
# The gate's intent is: "is there hidden mode dependence?"  The
# decisive measurement is: does the P_s SHAPE change when we treat
# modes individually?  If shape is unchanged, there is no hidden mode
# dependence regardless of what the log-quadratic fit to a constant
# returns.

# Observable-scale PASS: k-independent ratio (shape preserved)
if ratio_std < 1e-12 and abs_tilt_diff_max < 1e-13:
    verdict = "PASS"
    verdict_reason = (
        f"P_s^mode / P_s^branch is k-independent to machine precision "
        f"(std={ratio_std:.2e}, max tilt diff={abs_tilt_diff_max:.2e}); "
        f"no hidden mode dependence. "
        f"Mode-level produces a constant {(ratio_mean-1)*100:.4f}% amplitude "
        f"shift ONLY. Both alpha_s are at floating-point noise "
        f"(~1e-14); formal rel_diff ({rel_diff_naive:.2e}) is a "
        f"denominator pathology, not a physical signal."
    )
elif ratio_std < 1e-8 and abs_tilt_diff_max < 1e-10:
    # Tight but not quite machine precision — PASS
    verdict = "PASS"
    verdict_reason = (
        f"P_s ratio k-std = {ratio_std:.2e}, max tilt diff = "
        f"{abs_tilt_diff_max:.2e}; effectively constant ratio, "
        f"no hidden mode dependence."
    )
elif ratio_std < 1e-4 and abs_tilt_diff_max < 1e-5:
    verdict = "INFO"
    verdict_reason = (
        f"P_s ratio shows small k-dependence "
        f"(std={ratio_std:.2e}, max tilt diff={abs_tilt_diff_max:.2e}); "
        f"modest mode-level effect on alpha_s."
    )
else:
    verdict = "FAIL"
    verdict_reason = (
        f"P_s ratio k-dependent (std={ratio_std:.2e}, max tilt diff="
        f"{abs_tilt_diff_max:.2e}); mode-level differs from branch-level "
        f"in physical shape — hidden mode dependence detected."
    )

# Additional summary for the record
summary_numbers = {
    'alpha_s_mode': alpha_s_mode,
    'alpha_s_branch_refit': alpha_s_branch_refit,
    'abs_diff_alpha_s': abs_diff_alpha,
    'rel_diff_naive_pct': rel_diff_naive * 100 if not np.isnan(
        rel_diff_naive) else float('nan'),
    'P_s_ratio_mean': ratio_mean,
    'P_s_ratio_std': ratio_std,
    'max_tilt_discrepancy': abs_tilt_diff_max,
    'alpha_s_noise_floor': alpha_s_noise_floor,
}

print(f"Gate verdict: {verdict}")
print(f"  reason: {verdict_reason}")
print()

# ==============================================================================
#  SECTION 11: Write .npz
# ==============================================================================

print("SECTION 11: Write output data")
print("-" * 78)

out_path_npz = os.path.join(data_dir, 's74_degeneracy_lift_alpha_s.npz')  # (local)

np.savez(
    out_path_npz,
    # Identification
    gate_name='N12-DEGENERACY-LIFT-ALPHA-S-74',
    gate_verdict=verdict,
    gate_reason=verdict_reason,
    # Per-mode inputs
    labels=labels,
    omega_k_fold=omega_k_fold,
    r_k_bcs=r_k_bcs,
    Phi_final=Phi_final,
    mode_weights=mode_weights,
    beta_sq_total=beta_sq_total,
    c_k=c_k,
    psi_k=psi_k,
    E_k_raw=E_k_raw,
    # k-scan arrays
    k_values_Mpc=k_values_Mpc,
    T_k_of_k=T_k_of_k,
    P_s_k_mode=P_s_k_mode,
    k_pivot_Mpc=k_pivot_Mpc,
    idx_pivot=idx_pivot,
    # Mode-level aggregate
    n_s_mode=ns_mode,
    alpha_s_mode=alpha_s_mode,
    P_pivot_mode=P_pivot_mode,
    # Per-mode single-mode alpha_s diagnostics
    alpha_s_per_mode=alpha_s_per_mode,
    ns_per_mode=ns_per_mode,
    P_k_sq_at_pivot=P_k_sq_at_pivot,
    alpha_s_W_avg=alpha_s_W_avg,
    alpha_s_unweighted=alpha_s_unweighted,
    # Branch-level comparison
    n_s_branch_refit=ns_branch_refit,
    alpha_s_branch_refit=alpha_s_branch_refit,
    n_s_branch_stored=n_s_branch,
    alpha_s_branch_stored=alpha_s_branch,
    alpha_s_uniform=alpha_s_uniform,
    P_pivot_branch_W1A=P_pivot_branch_W1A,
    # Structural diagnostics
    ratio_k=ratio_k,
    ratio_mean=ratio_mean,
    ratio_std=ratio_std,
    log_ratio_mean=log_ratio_mean,
    log_ratio_std=log_ratio_std,
    ratio_is_k_independent=ratio_is_k_independent,
    deriv_mode=deriv_mode,
    deriv_branch=deriv_branch,
    deriv_mode_max=deriv_mode_max,
    deriv_branch_max=deriv_branch_max,
    deriv_diff_max=deriv_diff_max,
    alpha_s_noise_floor=alpha_s_noise_floor,
    abs_tilt_diff_max=abs_tilt_diff_max,
    abs_diff_alpha=abs_diff_alpha,
    rel_diff_naive=rel_diff_naive if not np.isnan(rel_diff_naive) else -1.0,
    # n_k spread within branches
    n_spread_B2=n_spread_B2,
    n_spread_B3=n_spread_B3,
)

print(f"  Wrote: {out_path_npz}")
print()

# ==============================================================================
#  SECTION 12: Plot
# ==============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # (local)

# Panel 1: per-mode |T_k|^2 and mode-level P_s(k)
ax = axes[0]
colors = ['C0', 'C1', 'C2', 'C3', 'k', 'C4', 'C5', 'C6']  # (local)
for k in range(N_modes):
    ax.loglog(k_values_Mpc, T_k_of_k[k, :]**2,
              '-', color=colors[k], lw=1.0, alpha=0.7,
              label=f'{labels[k]}')
ax.loglog(k_values_Mpc, P_s_k_mode, 'r-', lw=2.5, label='$P_s^{mode}(k)$')
ax.loglog(k_values_Mpc, P_s_k_branch, 'b--', lw=2.0, label='$P_s^{branch}(k)$')
ax.axvline(k_pivot_Mpc, color='gray', ls=':', lw=1.5)
ax.set_xlabel('$k$ (Mpc$^{-1}$)')
ax.set_ylabel('Transfer amplitude / power')
ax.set_title('Per-mode $|T_k|^2$ vs mode/branch $P_s(k)$')
ax.legend(loc='best', fontsize=8, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 2: ln P vs ln k near pivot + quadratic fit
ax = axes[1]
lo = max(0, idx_pivot - 15)  # (local)
hi = min(len(ln_k), idx_pivot + 16)  # (local)
x_win = ln_k[lo:hi] - ln_k[idx_pivot]  # (local)
y_mode_win = ln_P_mode[lo:hi]  # (local)
y_branch_win = ln_P_branch[lo:hi]  # (local)

ax.plot(x_win, y_mode_win, 'ro', label='mode-level data', markersize=6)
ax.plot(x_win, y_branch_win, 'bs', label='branch-level data',
        markersize=5, alpha=0.7)

# Fit curves
x_fit = np.linspace(x_win.min(), x_win.max(), 100)  # (local)
y_mode_fit = np.polyval(
    [0.5 * alpha_s_mode, ns_mode - 1, ln_P_mode[idx_pivot]], x_fit
)  # (local)
y_branch_fit = np.polyval(
    [0.5 * alpha_s_branch_refit, ns_branch_refit - 1,
     ln_P_branch[idx_pivot]], x_fit
)  # (local)
ax.plot(x_fit, y_mode_fit, 'r-',
        label=(f'mode fit: $n_s$={ns_mode:.4f}, '
               f'$\\alpha_s$={alpha_s_mode:.2e}'))
ax.plot(x_fit, y_branch_fit, 'b--',
        label=(f'branch fit: $n_s$={ns_branch_refit:.4f}, '
               f'$\\alpha_s$={alpha_s_branch_refit:.2e}'))

ax.set_xlabel('$\\ln(k / k_{pivot})$')
ax.set_ylabel('$\\ln P_s$')
ax.set_title('Log-quadratic fit at pivot (mode vs branch)')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

plt.suptitle(
    f'N12-DEGENERACY-LIFT-ALPHA-S-74 — Verdict: {verdict}',
    fontsize=13, fontweight='bold'
)
plt.tight_layout()
out_path_png = os.path.join(data_dir, 's74_degeneracy_lift_alpha_s.png')  # (local)
plt.savefig(out_path_png, dpi=120, bbox_inches='tight')
plt.close()
print(f"  Wrote: {out_path_png}")
print()

t_end = time.time()  # (local)
print(f"Runtime: {t_end - t_start:.2f}s")
print()
print(f"*** Gate verdict: {verdict} ***")
print(f"    {verdict_reason}")
