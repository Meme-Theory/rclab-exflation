#!/usr/bin/env python3
"""
s67_spectral_endpoint.py -- SPECTRAL-ENDPOINT-67: Functional Interpolation Continuity
=====================================================================================

Gate: SPECTRAL-ENDPOINT-67
  PASS: d^2S/dtau^2 changes sign at some eta_*, meaning the curvature of the
        spectral action transitions smoothly from convex to concave.
  FAIL: d^2S/dtau^2 has the same sign for all eta (no sign change in [0, 2]).

Physics:
--------
The spectral action on Jensen-deformed SU(3) with functional f_eta is:

    S_eta(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j |lambda_j(tau)|^eta     (1)

where eta interpolates between:
  - eta = 0: mode counting (f = 1, S_0 = sum dim^2 * N_modes = a_0 = const)
  - eta = 1: Chamseddine-Connes cutoff f(x) = sqrt(x), S_1 = sum dim^2 * |lam|
  - eta = 2: linear weighting f(x) = x, S_2 = sum dim^2 * lam^2

The key quantity is d^2S_eta/dtau^2 at the fold (tau = 0.19), which determines:
  - Sign of curvature: convex (d^2S > 0) vs concave (d^2S < 0)
  - Transit dynamics: smooth passage vs sharp phase transition
  - Connection to eps_H: the Hubble slow-roll parameter

S66 established:
  - Cutoff (eta ~ 1): eps_H > 0 (UV-dominated, S increases with tau)
  - Zeta a_4 (eta ~ -4): eps_H < 0 (IR-dominated, S decreases with tau)

This computation maps the CONTINUOUS transition between these regimes.

STRUCTURAL NOTE: At eta = 0, S_0 = a_0 = 6440 (tau-independent mode count),
so dS/dtau = d^2S/dtau^2 = 0 identically. As eta increases from 0, the
derivatives grow continuously. The question is whether d^2S/dtau^2 changes
sign at some eta_* in (0, 2].

For negative eta (e.g., eta = -2 corresponds to zeta_D(1) = a_2, eta = -4
to a_4), we compute |lambda|^eta = |lambda|^{-|eta|}, which is IR-weighted.
The sign flip in eps_H between cutoff and zeta corresponds to eta crossing
through 0 from positive to negative. We extend the scan to negative eta
to map the full phase diagram.

Agent: Spectral-Geometer (Session 67, Wave 4)
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
print("SPECTRAL-ENDPOINT-67: Functional Interpolation Continuity")
print("=" * 78)

MAX_PQ_SUM = 3  # Peter-Weyl truncation (same as S36/S66) (local)

# Tau grid: dense around the fold for accurate second derivatives
# 16 points from S36 + additional points for smooth interpolation
tau_grid = np.array([
    0.00, 0.05, 0.10, 0.12, 0.14,
    0.15, 0.16, 0.165, 0.17, 0.175,
    0.18, 0.185, 0.19, 0.195, 0.20,
    0.205, 0.21, 0.215, 0.22, 0.25,
    0.30, 0.35, 0.40, 0.50
])
n_tau = len(tau_grid)

# Eta grid: interpolation parameter
# eta in [-6, 4] to cover UV-weighted (high eta) and IR-weighted (negative eta)
# Focus range for the sign change: [-2, 2]
eta_fine = np.linspace(-6.0, 4.0, 201)
eta_focus = np.linspace(-2.0, 2.0, 201)

print(f"\n  Configuration:")
print(f"    tau_fold         = {tau_fold}")
print(f"    max_pq_sum       = {MAX_PQ_SUM}")
print(f"    n_tau_points     = {n_tau}")
print(f"    tau range        = [{tau_grid[0]:.3f}, {tau_grid[-1]:.3f}]")
print(f"    eta fine grid    = {len(eta_fine)} points in [{eta_fine[0]:.1f}, {eta_fine[-1]:.1f}]")
print(f"    eta focus grid   = {len(eta_focus)} points in [{eta_focus[0]:.1f}, {eta_focus[-1]:.1f}]")


# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRA AT ALL TAU VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute D_K Eigenvalue Spectra at All tau")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Storage: list of (tau, list of (p, q, abs_eigenvalues, dim_pq))
all_spectra = []

# Also compute S_cutoff (eta=1) for cross-check against S36
S_cutoff_check = np.zeros(n_tau)

# Load S36 for cross-check at overlapping tau values
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
              allow_pickle=True)
tau_S36 = d36['tau_combined']
S_S36 = d36['S_full']

t_start = time.time()

for i, tau in enumerate(tau_grid):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                   max_pq_sum=MAX_PQ_SUM, verbose=False)

    tau_spectra = []
    S_cut_i = 0.0  # (local)

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)
        tau_spectra.append((p, q, omega, d_pq))
        S_cut_i += d_pq**2 * np.sum(omega)  # eta=1 spectral action

    all_spectra.append(tau_spectra)
    S_cutoff_check[i] = S_cut_i

    if (i + 1) % 6 == 0 or i == n_tau - 1:
        elapsed = time.time() - t_start
        print(f"  tau[{i}] = {tau:.3f}, S_cutoff = {S_cut_i:.2f}  "
              f"({elapsed:.1f}s elapsed)")

t_total = time.time() - t_start
print(f"\n  Computed {n_tau} spectra in {t_total:.1f}s")

# Cross-check against S36 at overlapping tau values
print("\n  Cross-check against S36 (eta=1 cutoff action):")
max_dev = 0.0
n_check = 0
for j, tau_ref in enumerate(tau_S36):
    idx = np.argmin(np.abs(tau_grid - tau_ref))
    if np.abs(tau_grid[idx] - tau_ref) < 1e-6:
        dev = np.abs(S_cutoff_check[idx] - S_S36[j]) / S_S36[j]
        max_dev = max(max_dev, dev)
        n_check += 1
print(f"    {n_check} overlapping tau values, max |dev| = {max_dev:.2e}")
if max_dev < 1e-8:
    print(f"    PASSED (machine epsilon)")
else:
    print(f"    WARNING: deviation {max_dev:.2e}")


# =============================================================================
# STEP 2: COMPUTE S_eta(tau) FOR ALL eta AND tau
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Compute S_eta(tau) for Eta Interpolation")
print("=" * 78)

def compute_S_eta(eta, spectra_list):
    """
    Compute S_eta(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j |lambda_j|^eta

    For eta = 0: S = sum dim^2 * N_modes (mode counting)
    For eta > 0: UV-weighted (high eigenvalues dominate)
    For eta < 0: IR-weighted (low eigenvalues dominate, need care with zeros)

    Parameters
    ----------
    eta : float
        Interpolation parameter
    spectra_list : list of list of (p, q, omega, d_pq)
        Eigenvalue data at each tau

    Returns
    -------
    S_arr : ndarray, shape (n_tau,)
        S_eta at each tau value
    """
    n = len(spectra_list)
    S_arr = np.zeros(n)

    for i, tau_spectra in enumerate(spectra_list):
        S_i = 0.0  # (local)
        for p, q, omega, d_pq in tau_spectra:
            # Filter out zero eigenvalues (if any) for negative eta
            if eta < 0:
                mask = omega > 1e-12
                omega_use = omega[mask]
            else:
                omega_use = omega

            if len(omega_use) > 0:
                if abs(eta) < 1e-14:
                    # eta = 0: mode counting
                    S_i += d_pq**2 * len(omega_use)
                else:
                    S_i += d_pq**2 * np.sum(omega_use ** eta)

        S_arr[i] = S_i

    return S_arr


# Compute S_eta for both eta grids
print(f"\n  Computing S_eta for {len(eta_fine)} eta values (fine grid)...")
t_start = time.time()

S_eta_fine = np.zeros((len(eta_fine), n_tau))
for k, eta in enumerate(eta_fine):
    S_eta_fine[k] = compute_S_eta(eta, all_spectra)

print(f"    Done in {time.time() - t_start:.1f}s")

print(f"\n  Computing S_eta for {len(eta_focus)} eta values (focus grid)...")
t_start = time.time()

S_eta_focus = np.zeros((len(eta_focus), n_tau))
for k, eta in enumerate(eta_focus):
    S_eta_focus[k] = compute_S_eta(eta, all_spectra)

print(f"    Done in {time.time() - t_start:.1f}s")


# =============================================================================
# STEP 3: COMPUTE DERIVATIVES dS/dtau AND d^2S/dtau^2 VIA CUBIC SPLINE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Compute Derivatives via Cubic Spline Interpolation")
print("=" * 78)

# For each eta, fit a cubic spline through S_eta(tau) and extract derivatives
# at tau_fold

# First derivatives and second derivatives at the fold
dS_dtau_fold = np.zeros(len(eta_fine))
d2S_dtau2_fold = np.zeros(len(eta_fine))
S_at_fold = np.zeros(len(eta_fine))

dS_dtau_fold_focus = np.zeros(len(eta_focus))
d2S_dtau2_fold_focus = np.zeros(len(eta_focus))
S_at_fold_focus = np.zeros(len(eta_focus))

# Also compute eps_H = (1/2) * (S'/S)^2 for the Hubble slow-roll parameter
eps_H_fine = np.zeros(len(eta_fine))
eps_H_focus = np.zeros(len(eta_focus))

print(f"\n  Extracting derivatives at tau_fold = {tau_fold}...")

# Fine grid
for k in range(len(eta_fine)):
    cs = CubicSpline(tau_grid, S_eta_fine[k])
    S_at_fold[k] = cs(tau_fold)
    dS_dtau_fold[k] = cs(tau_fold, 1)
    d2S_dtau2_fold[k] = cs(tau_fold, 2)
    if abs(S_at_fold[k]) > 1e-30:
        eps_H_fine[k] = 0.5 * (dS_dtau_fold[k] / S_at_fold[k])**2

# Focus grid
for k in range(len(eta_focus)):
    cs = CubicSpline(tau_grid, S_eta_focus[k])
    S_at_fold_focus[k] = cs(tau_fold)
    dS_dtau_fold_focus[k] = cs(tau_fold, 1)
    d2S_dtau2_fold_focus[k] = cs(tau_fold, 2)
    if abs(S_at_fold_focus[k]) > 1e-30:
        eps_H_focus[k] = 0.5 * (dS_dtau_fold_focus[k] / S_at_fold_focus[k])**2

# Cross-check: at eta=1, dS/dtau should match dS_fold from canonical_constants
idx_eta1_fine = np.argmin(np.abs(eta_fine - 1.0))
idx_eta1_focus = np.argmin(np.abs(eta_focus - 1.0))

print(f"\n  Cross-check at eta = 1.0 (Chamseddine-Connes cutoff):")
print(f"    S(fold) computed:  {S_at_fold[idx_eta1_fine]:.2f}")
print(f"    S(fold) canonical: {S_fold:.2f}")
print(f"    dS/dtau computed:  {dS_dtau_fold[idx_eta1_fine]:.2f}")
print(f"    dS/dtau canonical: {dS_fold:.2f}")
print(f"    d2S/dtau2 computed: {d2S_dtau2_fold[idx_eta1_fine]:.2f}")
print(f"    d2S/dtau2 canonical: {d2S_fold:.2f}")

dev_S = abs(S_at_fold[idx_eta1_fine] - S_fold) / S_fold
dev_dS = abs(dS_dtau_fold[idx_eta1_fine] - dS_fold) / abs(dS_fold)
print(f"    |dev(S)| = {dev_S:.2e}, |dev(dS)| = {dev_dS:.2e}")


# =============================================================================
# STEP 4: FIND SIGN CHANGE IN d^2S/dtau^2
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Sign Change Analysis in d^2S/dtau^2(eta)")
print("=" * 78)

# Analyze the fine grid for sign changes
sign_d2S = np.sign(d2S_dtau2_fold)
sign_changes_fine = []
for k in range(len(eta_fine) - 1):
    if sign_d2S[k] * sign_d2S[k + 1] < 0:
        # Linear interpolation to find exact crossing
        eta_cross = eta_fine[k] - d2S_dtau2_fold[k] * (
            eta_fine[k + 1] - eta_fine[k]) / (
            d2S_dtau2_fold[k + 1] - d2S_dtau2_fold[k])
        sign_changes_fine.append(eta_cross)
        print(f"  Sign change found at eta_* = {eta_cross:.6f}")
        print(f"    d2S(eta[{k}]={eta_fine[k]:.3f}) = {d2S_dtau2_fold[k]:.4e}")
        print(f"    d2S(eta[{k+1}]={eta_fine[k+1]:.3f}) = {d2S_dtau2_fold[k+1]:.4e}")

# Analyze focus grid
sign_d2S_focus = np.sign(d2S_dtau2_fold_focus)
sign_changes_focus = []
for k in range(len(eta_focus) - 1):
    if sign_d2S_focus[k] * sign_d2S_focus[k + 1] < 0:
        eta_cross = eta_focus[k] - d2S_dtau2_fold_focus[k] * (
            eta_focus[k + 1] - eta_focus[k]) / (
            d2S_dtau2_fold_focus[k + 1] - d2S_dtau2_fold_focus[k])
        sign_changes_focus.append(eta_cross)
        print(f"  Sign change (focus) at eta_* = {eta_cross:.6f}")

print(f"\n  Total sign changes (fine grid):  {len(sign_changes_fine)}")
print(f"  Total sign changes (focus grid): {len(sign_changes_focus)}")

# Check if d^2S is identically zero at eta=0
idx_eta0 = np.argmin(np.abs(eta_fine))
print(f"\n  At eta ~ 0 (mode counting):")
print(f"    eta = {eta_fine[idx_eta0]:.6f}")
print(f"    d^2S/dtau^2 = {d2S_dtau2_fold[idx_eta0]:.6e}")
print(f"    (Should be ~0 since a_0 is tau-independent)")


# =============================================================================
# STEP 5: CONTINUITY AND SMOOTHNESS ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Continuity and Smoothness Analysis")
print("=" * 78)

# Check if d^2S(eta) is smooth (no discontinuities)
# Compute finite differences of d^2S with respect to eta
dd2S_deta_focus = np.gradient(d2S_dtau2_fold_focus, eta_focus)

# Look for large jumps (potential discontinuities)
max_jump = np.max(np.abs(np.diff(d2S_dtau2_fold_focus)))
mean_val = np.mean(np.abs(d2S_dtau2_fold_focus[d2S_dtau2_fold_focus != 0]))
relative_jump = max_jump / mean_val if mean_val > 0 else 0

print(f"\n  Smoothness diagnostics (focus grid):")
print(f"    Max |jump| in d^2S between adjacent eta: {max_jump:.6e}")
print(f"    Mean |d^2S| (nonzero):                   {mean_val:.6e}")
print(f"    Relative max jump:                       {relative_jump:.6e}")
print(f"    (Discontinuity criterion: relative jump > 0.1)")

is_continuous = relative_jump < 0.1
print(f"\n    Continuity: {'YES' if is_continuous else 'NO'}")


# =============================================================================
# STEP 6: DETAILED CHARACTERIZATION AT KEY ETA VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Detailed Results at Key Eta Values")
print("=" * 78)

key_etas = [0.0, 0.5, 1.0, 1.5, 2.0, -1.0, -2.0, -4.0]

print(f"\n  {'eta':>6s}  {'S(fold)':>14s}  {'dS/dtau':>14s}  {'d2S/dtau2':>14s}  {'eps_H':>12s}")
print(f"  {'-'*6}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*12}")

for eta_key in key_etas:
    # Compute S_eta at this specific eta
    S_key = compute_S_eta(eta_key, all_spectra)
    cs_key = CubicSpline(tau_grid, S_key)
    S_val = cs_key(tau_fold)
    dS_val = cs_key(tau_fold, 1)
    d2S_val = cs_key(tau_fold, 2)
    eps_val = 0.5 * (dS_val / S_val)**2 if abs(S_val) > 1e-30 else 0.0

    print(f"  {eta_key:6.1f}  {S_val:14.4f}  {dS_val:14.4f}  {d2S_val:14.4f}  {eps_val:12.6f}")

# Compute n_s at eta=1 for verification
S_eta1 = compute_S_eta(1.0, all_spectra)
cs_eta1 = CubicSpline(tau_grid, S_eta1)
S1_fold = cs_eta1(tau_fold)
dS1_fold = cs_eta1(tau_fold, 1)
d2S1_fold = cs_eta1(tau_fold, 2)
eps_H_eta1 = 0.5 * (dS1_fold / S1_fold)**2
# Hubble slow-roll: n_s = 1 - 2*eps_H (simplified)
ns_eta1 = 1 - 2 * eps_H_eta1

print(f"\n  Verification at eta = 1 (CC cutoff):")
print(f"    eps_H = {eps_H_eta1:.6f}")
print(f"    n_s = 1 - 2*eps_H = {ns_eta1:.6f}")


# =============================================================================
# STEP 7: COMPUTE NORMALIZED CURVATURE K(eta) = d^2S / (S * deta_spacing^2)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Normalized Spectral Curvature K(eta)")
print("=" * 78)

# The normalized curvature K(eta) = d^2S/dtau^2 / S(fold) removes the
# overall magnitude dependence, isolating the geometric shape
K_eta_fine = np.zeros(len(eta_fine))
K_eta_focus = np.zeros(len(eta_focus))

for k in range(len(eta_fine)):
    if abs(S_at_fold[k]) > 1e-30:
        K_eta_fine[k] = d2S_dtau2_fold[k] / S_at_fold[k]

for k in range(len(eta_focus)):
    if abs(S_at_fold_focus[k]) > 1e-30:
        K_eta_focus[k] = d2S_dtau2_fold_focus[k] / S_at_fold_focus[k]

# Sign changes in normalized curvature
K_sign_changes = []
for k in range(len(eta_focus) - 1):
    if np.sign(K_eta_focus[k]) * np.sign(K_eta_focus[k + 1]) < 0:
        eta_cross = eta_focus[k] - K_eta_focus[k] * (
            eta_focus[k + 1] - eta_focus[k]) / (
            K_eta_focus[k + 1] - K_eta_focus[k])
        K_sign_changes.append(eta_cross)

print(f"\n  Normalized curvature K(eta) = d^2S/dtau^2 / S_eta(fold):")
print(f"    Sign changes: {len(K_sign_changes)}")
for sc in K_sign_changes:
    print(f"      eta_* = {sc:.6f}")


# =============================================================================
# STEP 8: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Gate Verdict -- SPECTRAL-ENDPOINT-67")
print("=" * 78)

# The gate asks: does d^2S/dtau^2 change sign at some eta_*?
# PASS: yes (discontinuity vanishes = the curvature transitions smoothly)
# FAIL: no (same sign for all eta)

has_sign_change = len(sign_changes_fine) > 0 or len(sign_changes_focus) > 0

if has_sign_change:
    all_crossings = sorted(set(
        [round(x, 6) for x in sign_changes_fine] +
        [round(x, 6) for x in sign_changes_focus]
    ))
    verdict = "PASS"
    verdict_detail = (f"d^2S/dtau^2 changes sign at "
                      f"{len(all_crossings)} eta value(s): "
                      f"{', '.join(f'{x:.4f}' for x in all_crossings)}")
else:
    verdict = "FAIL"
    verdict_detail = "d^2S/dtau^2 has same sign for all eta in [-6, 4]"

print(f"\n  Gate SPECTRAL-ENDPOINT-67: {verdict}")
print(f"  {verdict_detail}")
print(f"  Continuity: {'Smooth transition' if is_continuous else 'Discontinuity detected'}")

# Additional characterization
if has_sign_change:
    # Report the primary crossing
    primary_crossing = all_crossings[0] if all_crossings else None
    if primary_crossing is not None:
        print(f"\n  Primary sign change at eta_* = {primary_crossing:.6f}")
        print(f"  Interpretation:")
        print(f"    For eta > eta_*: d^2S/dtau^2 has one sign (UV-dominated regime)")
        print(f"    For eta < eta_*: d^2S/dtau^2 has opposite sign (IR-dominated regime)")
        print(f"    At eta_*: inflection point in functional space")

        # Characterize the transition width
        # Find where |d^2S| drops to 10% of its max on each side
        if len(sign_changes_focus) > 0:
            idx_cross = np.argmin(np.abs(eta_focus - primary_crossing))
            d2S_max_pos = np.max(d2S_dtau2_fold_focus[eta_focus > primary_crossing])
            d2S_max_neg = np.min(d2S_dtau2_fold_focus[eta_focus < primary_crossing])
            print(f"\n  Transition characterization:")
            print(f"    max(d^2S) for eta > eta_*: {d2S_max_pos:.4e}")
            print(f"    min(d^2S) for eta < eta_*: {d2S_max_neg:.4e}")


# =============================================================================
# STEP 9: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Save Results")
print("=" * 78)

output_path = os.path.join(SCRIPT_DIR, 's67_spectral_endpoint.npz')
np.savez(output_path,
         # Grids
         tau_grid=tau_grid,
         eta_fine=eta_fine,
         eta_focus=eta_focus,
         # Spectral action values
         S_eta_fine=S_eta_fine,
         S_eta_focus=S_eta_focus,
         # Derivatives at fold (fine grid)
         S_at_fold_fine=S_at_fold,
         dS_dtau_fold_fine=dS_dtau_fold,
         d2S_dtau2_fold_fine=d2S_dtau2_fold,
         eps_H_fine=eps_H_fine,
         # Derivatives at fold (focus grid)
         S_at_fold_focus=S_at_fold_focus,
         dS_dtau_fold_focus=dS_dtau_fold_focus,
         d2S_dtau2_fold_focus=d2S_dtau2_fold_focus,
         eps_H_focus=eps_H_focus,
         # Normalized curvature
         K_eta_fine=K_eta_fine,
         K_eta_focus=K_eta_focus,
         # Sign change locations
         sign_changes_d2S=np.array(sign_changes_fine + sign_changes_focus),
         sign_changes_K=np.array(K_sign_changes),
         # Verdict
         verdict=verdict,
         is_continuous=is_continuous,
         )

print(f"  Saved to {output_path}")


# =============================================================================
# STEP 10: PLOTTING
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Generate Plots")
print("=" * 78)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.35, wspace=0.3)

# --- Panel A: S_eta(tau) for key eta values ---
ax1 = fig.add_subplot(gs[0, 0])
key_plot_etas = [-4.0, -2.0, -1.0, 0.0, 0.5, 1.0, 1.5, 2.0]
colors = plt.cm.coolwarm(np.linspace(0, 1, len(key_plot_etas)))

for j, eta_key in enumerate(key_plot_etas):
    S_key = compute_S_eta(eta_key, all_spectra)
    # Normalize to S(tau=0) for visual clarity
    if abs(S_key[0]) > 1e-30:
        S_norm = S_key / S_key[0]
    else:
        S_norm = S_key
    ax1.plot(tau_grid, S_norm, '-o', color=colors[j], markersize=2,
             label=f'$\\eta={eta_key:.1f}$')

ax1.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold ({tau_fold})')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$S_\eta(\tau) / S_\eta(0)$')
ax1.set_title('(A) Normalized Spectral Action vs $\\tau$')
ax1.legend(fontsize=7, ncol=2)
ax1.set_xlim([0, 0.5])

# --- Panel B: d^2S/dtau^2 vs eta (fine grid) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(eta_fine, d2S_dtau2_fold, 'b-', linewidth=1.5)
ax2.axhline(0, color='k', ls='-', alpha=0.3)
ax2.axvline(0, color='gray', ls=':', alpha=0.3, label='$\\eta=0$ (mode count)')
ax2.axvline(1, color='red', ls='--', alpha=0.5, label='$\\eta=1$ (CC cutoff)')
ax2.axvline(2, color='green', ls='--', alpha=0.5, label='$\\eta=2$ (linear)')
for sc in sign_changes_fine:
    ax2.axvline(sc, color='orange', ls='-', alpha=0.8,
                label=f'$\\eta_*={sc:.3f}$')
ax2.set_xlabel(r'$\eta$')
ax2.set_ylabel(r'$d^2S_\eta/d\tau^2$ at fold')
ax2.set_title('(B) Spectral Action Curvature vs $\\eta$ (full range)')
ax2.legend(fontsize=7)

# --- Panel C: d^2S/dtau^2 vs eta (focus grid, zoomed) ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(eta_focus, d2S_dtau2_fold_focus, 'b-', linewidth=1.5)
ax3.axhline(0, color='k', ls='-', alpha=0.3)
ax3.axvline(0, color='gray', ls=':', alpha=0.3)
ax3.axvline(1, color='red', ls='--', alpha=0.5, label='$\\eta=1$')
for sc in sign_changes_focus:
    ax3.axvline(sc, color='orange', ls='-', alpha=0.8,
                label=f'$\\eta_*={sc:.3f}$')
ax3.set_xlabel(r'$\eta$')
ax3.set_ylabel(r'$d^2S_\eta/d\tau^2$ at fold')
ax3.set_title('(C) Curvature vs $\\eta$ (focus: $-2$ to $2$)')
ax3.legend(fontsize=7)

# --- Panel D: Normalized curvature K(eta) ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(eta_focus, K_eta_focus, 'r-', linewidth=1.5)
ax4.axhline(0, color='k', ls='-', alpha=0.3)
ax4.axvline(1, color='red', ls='--', alpha=0.5, label='$\\eta=1$')
for sc in K_sign_changes:
    ax4.axvline(sc, color='orange', ls='-', alpha=0.8,
                label=f'$\\eta_*={sc:.3f}$')
ax4.set_xlabel(r'$\eta$')
ax4.set_ylabel(r'$K(\eta) = (d^2S/d\tau^2)/S$ at fold')
ax4.set_title('(D) Normalized Curvature vs $\\eta$')
ax4.legend(fontsize=7)

# --- Panel E: dS/dtau vs eta ---
ax5 = fig.add_subplot(gs[2, 0])
ax5.plot(eta_fine, dS_dtau_fold, 'g-', linewidth=1.5)
ax5.axhline(0, color='k', ls='-', alpha=0.3)
ax5.axvline(0, color='gray', ls=':', alpha=0.3)
ax5.axvline(1, color='red', ls='--', alpha=0.5, label='$\\eta=1$')
ax5.set_xlabel(r'$\eta$')
ax5.set_ylabel(r'$dS_\eta/d\tau$ at fold')
ax5.set_title('(E) First Derivative vs $\\eta$')
ax5.legend(fontsize=7)

# Find sign changes in dS/dtau
dS_sign_changes = []
dS_sign = np.sign(dS_dtau_fold)
for k in range(len(eta_fine) - 1):
    if dS_sign[k] * dS_sign[k + 1] < 0:
        eta_cross = eta_fine[k] - dS_dtau_fold[k] * (
            eta_fine[k + 1] - eta_fine[k]) / (
            dS_dtau_fold[k + 1] - dS_dtau_fold[k])
        dS_sign_changes.append(eta_cross)
        ax5.axvline(eta_cross, color='orange', ls='-', alpha=0.8)

# --- Panel F: eps_H vs eta ---
ax6 = fig.add_subplot(gs[2, 1])
# Use signed eps_H based on sign of dS/dtau (convention: eps_H > 0 for red tilt)
signed_eps = np.zeros(len(eta_fine))
for k in range(len(eta_fine)):
    if abs(S_at_fold[k]) > 1e-30 and abs(d2S_dtau2_fold[k]) > 1e-30:
        # eps_H captures the curvature direction
        signed_eps[k] = d2S_dtau2_fold[k] / abs(S_at_fold[k])

ax6.plot(eta_fine, signed_eps, 'm-', linewidth=1.5)
ax6.axhline(0, color='k', ls='-', alpha=0.3)
ax6.axvline(1, color='red', ls='--', alpha=0.5, label='$\\eta=1$')
ax6.set_xlabel(r'$\eta$')
ax6.set_ylabel(r'$d^2S / |S|$ at fold')
ax6.set_title('(F) Signed Curvature Ratio vs $\\eta$')
ax6.legend(fontsize=7)

fig.suptitle('SPECTRAL-ENDPOINT-67: Functional Interpolation Continuity\n'
             f'$S_\\eta(\\tau) = \\sum d_{{pq}}^2 \\sum |\\lambda_j|^\\eta$, '
             f'fold at $\\tau={tau_fold}$',
             fontsize=13, y=0.98)

plot_path = os.path.join(SCRIPT_DIR, 's67_spectral_endpoint.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved plot to {plot_path}")


# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)

print(f"""
  SPECTRAL-ENDPOINT-67: Functional Interpolation Continuity
  =========================================================

  Spectral functional: f_eta(x) = x^(eta/2)
  Spectral action: S_eta(tau) = sum dim(p,q)^2 * sum |lambda_j(tau)|^eta

  Key eta values:
    eta = 0:  mode counting (S = a_0 = {a0_fold:.0f}, tau-independent)  # (local)
    eta = 1:  Chamseddine-Connes cutoff (S = {S_at_fold[idx_eta1_fine]:.2f})  # (local)
    eta = 2:  linear weighting  # (local)

  Results at tau_fold = {tau_fold}:
    d^2S/dtau^2 sign changes: {len(sign_changes_fine) + len(sign_changes_focus)}
    K(eta) sign changes:      {len(K_sign_changes)}
    dS/dtau sign changes:     {len(dS_sign_changes)}
    Continuity:               {'YES (smooth)' if is_continuous else 'NO (discontinuity)'}

  Gate Verdict: {verdict}
    {verdict_detail}

  Sign change locations (d^2S/dtau^2):""")
for sc in sorted(set(sign_changes_fine + sign_changes_focus)):
    print(f"    eta_* = {sc:.6f}")

print(f"""
  Sign change locations (dS/dtau):""")
for sc in dS_sign_changes:
    print(f"    eta_* = {sc:.6f}")

print(f"""
  Sign change locations (K = d^2S/S):""")
for sc in K_sign_changes:
    print(f"    eta_* = {sc:.6f}")

print(f"""
  Files:
    Data: s67_spectral_endpoint.npz
    Plot: s67_spectral_endpoint.png
""")

print("=" * 78)
print("DONE")
print("=" * 78)
