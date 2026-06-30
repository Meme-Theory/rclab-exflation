#!/usr/bin/env python3
"""
s77_r1_tau_trajectory.py -- R1-TAU-TRAJECTORY (S77-B6-R1-TRAJECTORY)
====================================================================

Gate: S77-B6-R1-TRAJECTORY (INFO characterization)
  Task: Map R_1(tau) = a_0(tau)*a_4(tau)/a_2(tau)^2 across tau in [0, 0.5].
  Key question: is R_1 stationary at the fold (tau=0.190)?

Physics (substrate framing):
-----------------------------
R_1 is the dimensionless ratio of spectral-action moments whose Weyl
exponents cancel (alpha_net = 0 per S76 R-Protection Theorem).  At the
fold tau=0.190, canonical value R_1 = 1.128655 (S74, verified to 6 sig
figs).  S76 WS5 established drift 0.34% across L_max = 3..9.

This computation maps the FULL tau trajectory [0, 0.5] at L_max=3 to
determine:
  1. Is R_1(tau) monotonic?  Does it have extrema?
  2. Is R_1 stationary (dR_1/dtau = 0) at the fold?
  3. What is the total variation of R_1 across [0, 0.5]?

Method:
  For each tau, compute D_K eigenvalues via Peter-Weyl at max_pq_sum=3,
  extract a_0, a_2, a_4 in S73B half-spectrum convention, form R_1.
  Numerical derivative via centered finite differences on a dense grid.

Agent: Spectral-Geometer (Session 77, Wave 2, W2-F)
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

# CANONICAL CONSTANTS import
from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    R_protected_fold,
)

# tier1 infrastructure
from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    collect_spectrum,
    build_cliff8,
)

# ============================================================================
# CONFIGURATION
# ============================================================================

print("=" * 78)
print("S77-B6-R1-TRAJECTORY: R_1(tau) across [0, 0.5]")
print("=" * 78)
print()

# Tau grid: sparse primary grid + dense near fold for derivative
TAU_PRIMARY = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50])  # (local)

# Dense grid near fold for accurate derivative
TAU_FOLD_DENSE = np.array([0.180, 0.185, 0.190, 0.195, 0.200])  # (local)

# Combine and sort, removing duplicates
TAU_ALL = np.unique(np.concatenate([TAU_PRIMARY, TAU_FOLD_DENSE]))  # (local)

MAX_PQ_SUM = 3  # (local) L_max=3, same as S74 canonical computation
EVAL_CUTOFF = 0.01  # (local) exclude near-zero eigenvalues, same as S74

print(f"  tau_fold (canonical) = {tau_fold}")
print(f"  R_protected_fold (canonical) = {R_protected_fold:.6f}")
print(f"  L_max (max_pq_sum) = {MAX_PQ_SUM}")
print(f"  Eigenvalue cutoff = {EVAL_CUTOFF}")
print(f"  Tau grid: {len(TAU_ALL)} values in [{TAU_ALL[0]:.3f}, {TAU_ALL[-1]:.3f}]")
print(f"  Grid: {TAU_ALL}")
print()

# ============================================================================
# STEP 1: BUILD ALGEBRAIC INFRASTRUCTURE (once)
# ============================================================================

print("=" * 78)
print("STEP 1: ALGEBRAIC INFRASTRUCTURE")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

print(f"  8 su(3) generators, structure constants, 8 Clifford generators built")
print()

# ============================================================================
# STEP 2: COMPUTE SPECTRUM AND MOMENTS AT EACH TAU
# ============================================================================

print("=" * 78)
print("STEP 2: SWEEP TAU AND COMPUTE SPECTRAL MOMENTS")
print("=" * 78)


def compute_moments_at_tau(tau_val):
    """Compute a_0, a_2, a_4 in S73B convention at given tau.

    S73B convention:
      a_k = 0.5 * sum_{n: |lam_n| > cutoff} d_n * |lam_n|^{-k}
    where d_n = dim(p,q) is the Peter-Weyl degeneracy.

    Returns dict with a0, a2, a4, n_evals, lam_min.
    """
    all_evals, eval_data = collect_spectrum(
        tau_val, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False
    )

    # Extract absolute values and multiplicities
    abs_vals = []  # (local)
    mults = []  # (local)
    for ev, mult in all_evals:
        aev = abs(ev)  # (local)
        if aev > EVAL_CUTOFF:
            abs_vals.append(aev)
            mults.append(mult)

    abs_vals = np.array(abs_vals)  # (local)
    mults = np.array(mults, dtype=np.float64)  # (local)

    # S73B half-spectrum convention: factor 0.5
    a0 = 0.5 * float(np.sum(mults))  # (local)
    a2 = 0.5 * float(np.sum(mults / abs_vals**2))  # (local)
    a4 = 0.5 * float(np.sum(mults / abs_vals**4))  # (local)

    return {
        'tau': tau_val,
        'a0': a0,
        'a2': a2,
        'a4': a4,
        'n_evals': len(abs_vals),
        'lam_min': float(np.min(abs_vals)) if len(abs_vals) > 0 else np.nan,
        'lam_max': float(np.max(abs_vals)) if len(abs_vals) > 0 else np.nan,
    }


# Run sweep
results = []  # (local)
t_start = time.time()  # (local)

for i, tau_val in enumerate(TAU_ALL):
    t0 = time.time()  # (local)
    r = compute_moments_at_tau(tau_val)  # (local)
    dt = time.time() - t0  # (local)
    results.append(r)
    R1_val = r['a0'] * r['a4'] / r['a2']**2  # (local)
    print(f"  [{i+1:2d}/{len(TAU_ALL)}] tau={tau_val:.4f}: "
          f"a0={r['a0']:.1f}, a2={r['a2']:.3f}, a4={r['a4']:.4f}, "
          f"R_1={R1_val:.6f}, "
          f"lam_range=[{r['lam_min']:.3f}, {r['lam_max']:.3f}], "
          f"n={r['n_evals']}, dt={dt:.1f}s")

t_total = time.time() - t_start  # (local)
print(f"\n  Total computation time: {t_total:.1f}s")
print()

# ============================================================================
# STEP 3: FORM R_1(tau) AND ANALYZE
# ============================================================================

print("=" * 78)
print("STEP 3: R_1(tau) TRAJECTORY ANALYSIS")
print("=" * 78)

tau_arr = np.array([r['tau'] for r in results])  # (local)
a0_arr = np.array([r['a0'] for r in results])  # (local)
a2_arr = np.array([r['a2'] for r in results])  # (local)
a4_arr = np.array([r['a4'] for r in results])  # (local)
R1_arr = a0_arr * a4_arr / a2_arr**2  # (local)

print(f"\n  tau       a_0         a_2          a_4          R_1")
print(f"  " + "-" * 72)
for i in range(len(tau_arr)):
    marker = " <-- FOLD" if abs(tau_arr[i] - tau_fold) < 0.005 else ""
    print(f"  {tau_arr[i]:.4f}  {a0_arr[i]:>9.1f}  {a2_arr[i]:>12.4f}  {a4_arr[i]:>12.6f}  {R1_arr[i]:.6f}{marker}")

# R_1 statistics
R1_min = np.min(R1_arr)  # (local)
R1_max = np.max(R1_arr)  # (local)
R1_range = R1_max - R1_min  # (local)
R1_mean = np.mean(R1_arr)  # (local)
idx_min = np.argmin(R1_arr)  # (local)
idx_max = np.argmax(R1_arr)  # (local)
total_var_pct = 100 * R1_range / R1_mean  # (local)

print(f"\n  R_1 statistics:")
print(f"    min = {R1_min:.6f} at tau = {tau_arr[idx_min]:.4f}")
print(f"    max = {R1_max:.6f} at tau = {tau_arr[idx_max]:.4f}")
print(f"    range = {R1_range:.6f}")
print(f"    mean = {R1_mean:.6f}")
print(f"    total variation = {total_var_pct:.3f}%")

# Monotonicity check
diffs = np.diff(R1_arr)  # (local)
n_increasing = np.sum(diffs > 0)  # (local)
n_decreasing = np.sum(diffs < 0)  # (local)
is_monotone = (n_increasing == 0) or (n_decreasing == 0)  # (local)
print(f"\n  Monotonicity: {n_increasing} increasing steps, {n_decreasing} decreasing steps")
print(f"    Monotonic: {'YES' if is_monotone else 'NO'}")
if not is_monotone:
    # Find local extrema
    for i in range(1, len(R1_arr) - 1):
        if R1_arr[i] > R1_arr[i-1] and R1_arr[i] > R1_arr[i+1]:
            print(f"    LOCAL MAX at tau = {tau_arr[i]:.4f}, R_1 = {R1_arr[i]:.6f}")
        if R1_arr[i] < R1_arr[i-1] and R1_arr[i] < R1_arr[i+1]:
            print(f"    LOCAL MIN at tau = {tau_arr[i]:.4f}, R_1 = {R1_arr[i]:.6f}")

# ============================================================================
# STEP 4: DERIVATIVE dR_1/dtau AT FOLD
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 4: dR_1/dtau AT THE FOLD")
print("=" * 78)

# Use centered finite differences on the dense grid near tau=0.190
# Need points at tau=0.185 and tau=0.195
idx_185 = np.argmin(np.abs(tau_arr - 0.185))  # (local)
idx_190 = np.argmin(np.abs(tau_arr - 0.190))  # (local)
idx_195 = np.argmin(np.abs(tau_arr - 0.195))  # (local)

if abs(tau_arr[idx_185] - 0.185) < 0.001 and abs(tau_arr[idx_195] - 0.195) < 0.001:
    dR1_dtau_fold = (R1_arr[idx_195] - R1_arr[idx_185]) / (tau_arr[idx_195] - tau_arr[idx_185])  # (local)
    print(f"  Centered FD: dR_1/dtau at fold = {dR1_dtau_fold:.6f}")
    print(f"    using tau = [{tau_arr[idx_185]:.4f}, {tau_arr[idx_195]:.4f}]")
    print(f"    R_1 = [{R1_arr[idx_185]:.6f}, {R1_arr[idx_195]:.6f}]")
else:
    # Fallback: use nearest available points
    idx_lo = np.argmin(np.abs(tau_arr - (tau_fold - 0.01)))  # (local)
    idx_hi = np.argmin(np.abs(tau_arr - (tau_fold + 0.01)))  # (local)
    dR1_dtau_fold = (R1_arr[idx_hi] - R1_arr[idx_lo]) / (tau_arr[idx_hi] - tau_arr[idx_lo])  # (local)
    print(f"  Forward FD: dR_1/dtau at fold = {dR1_dtau_fold:.6f}")

# Also compute second derivative
idx_180 = np.argmin(np.abs(tau_arr - 0.180))  # (local)
idx_200 = np.argmin(np.abs(tau_arr - 0.200))  # (local)
if abs(tau_arr[idx_180] - 0.180) < 0.001 and abs(tau_arr[idx_200] - 0.200) < 0.001:
    # 5-point stencil for first derivative at each neighbor, then FD of those
    dR1_lo = (R1_arr[idx_190] - R1_arr[idx_180]) / (tau_arr[idx_190] - tau_arr[idx_180])  # (local)
    dR1_hi = (R1_arr[idx_200] - R1_arr[idx_190]) / (tau_arr[idx_200] - tau_arr[idx_190])  # (local)
    d2R1_fold = (dR1_hi - dR1_lo) / (0.5 * (tau_arr[idx_200] - tau_arr[idx_180]))  # (local)
    print(f"\n  Second derivative: d^2 R_1/dtau^2 at fold = {d2R1_fold:.4f}")
    print(f"    dR_1/dtau(left)  = {dR1_lo:.6f}")
    print(f"    dR_1/dtau(right) = {dR1_hi:.6f}")

# Stationarity assessment
stationary_thresh = 0.01  # (local) |dR_1/dtau| < this => "effectively stationary"
is_stationary = abs(dR1_dtau_fold) < stationary_thresh  # (local)
print(f"\n  Stationarity at fold: |dR_1/dtau| = {abs(dR1_dtau_fold):.6f}")
print(f"    Threshold: {stationary_thresh}")
print(f"    STATIONARY: {'YES' if is_stationary else 'NO'}")

# R_1(fold) vs canonical
idx_fold = np.argmin(np.abs(tau_arr - tau_fold))  # (local)
R1_fold_computed = R1_arr[idx_fold]  # (local)
R1_fold_error_pct = 100 * abs(R1_fold_computed - R_protected_fold) / R_protected_fold  # (local)
print(f"\n  Cross-check: R_1(fold) = {R1_fold_computed:.6f} vs canonical {R_protected_fold:.6f}")
print(f"    Deviation: {R1_fold_error_pct:.4f}%")

# ============================================================================
# STEP 5: INDIVIDUAL MOMENT TRAJECTORIES
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 5: MOMENT TRAJECTORIES (for context)")
print("=" * 78)

# Compute normalized variations of each moment
a0_rel = a0_arr / a0_arr[idx_fold]  # (local)
a2_rel = a2_arr / a2_arr[idx_fold]  # (local)
a4_rel = a4_arr / a4_arr[idx_fold]  # (local)

print(f"\n  Moment variations relative to fold value:")
print(f"  tau       a0/a0(fold)  a2/a2(fold)  a4/a4(fold)  R_1/R_1(fold)")
print(f"  " + "-" * 66)
for i in range(len(tau_arr)):
    R1_rel = R1_arr[i] / R1_arr[idx_fold]  # (local)
    print(f"  {tau_arr[i]:.4f}  {a0_rel[i]:>11.6f}  {a2_rel[i]:>11.6f}  {a4_rel[i]:>11.6f}  {R1_rel:>12.6f}")

# Range of each moment
a0_var = 100 * (np.max(a0_arr) - np.min(a0_arr)) / np.mean(a0_arr)  # (local)
a2_var = 100 * (np.max(a2_arr) - np.min(a2_arr)) / np.mean(a2_arr)  # (local)
a4_var = 100 * (np.max(a4_arr) - np.min(a4_arr)) / np.mean(a4_arr)  # (local)
print(f"\n  Total variation across [0, 0.5]:")
print(f"    a_0: {a0_var:.2f}%")
print(f"    a_2: {a2_var:.2f}%")
print(f"    a_4: {a4_var:.2f}%")
print(f"    R_1: {total_var_pct:.3f}%  (<<< cancellation ratio: {min(a0_var, a2_var, a4_var)/max(0.001, total_var_pct):.1f}x)")

# ============================================================================
# STEP 6: SAVE DATA
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 6: SAVE DATA")
print("=" * 78)

save_path = 's77_r1_tau_trajectory.npz'  # (local)
np.savez(save_path,
         tau=tau_arr,
         a0=a0_arr,
         a2=a2_arr,
         a4=a4_arr,
         R1=R1_arr,
         R1_fold_computed=R1_fold_computed,
         dR1_dtau_fold=dR1_dtau_fold,
         R1_min=R1_min,
         R1_max=R1_max,
         R1_range=R1_range,
         total_var_pct=total_var_pct,
         is_stationary=is_stationary,
         max_pq_sum=MAX_PQ_SUM,
         eval_cutoff=EVAL_CUTOFF)
print(f"  Saved to {save_path}")

# ============================================================================
# STEP 7: PLOT
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 7: PLOT")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'$R_1(\tau) = a_0 a_4 / a_2^2$ Trajectory on Jensen-deformed SU(3)',
             fontsize=14, fontweight='bold')

# Panel 1: R_1(tau) main trajectory
ax1 = axes[0, 0]
ax1.plot(tau_arr, R1_arr, 'b.-', linewidth=2, markersize=8, label=r'$R_1(\tau)$')
ax1.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label=f'fold (tau={tau_fold})')
ax1.axhline(R_protected_fold, color='gray', linestyle=':', alpha=0.5, label=f'canonical {R_protected_fold:.4f}')
ax1.set_xlabel(r'$\tau$ (Jensen parameter)')
ax1.set_ylabel(r'$R_1 = a_0 a_4 / a_2^2$')
ax1.set_title(r'$R_1(\tau)$ trajectory')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: Zoomed near fold
ax2 = axes[0, 1]
mask_fold = (tau_arr >= 0.10) & (tau_arr <= 0.30)  # (local)
ax2.plot(tau_arr[mask_fold], R1_arr[mask_fold], 'b.-', linewidth=2, markersize=8)
ax2.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label='fold')
ax2.set_xlabel(r'$\tau$')
ax2.set_ylabel(r'$R_1$')
ax2.set_title(r'$R_1(\tau)$ near fold (zoom)')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Individual moments (relative)
ax3 = axes[1, 0]
ax3.plot(tau_arr, a0_rel, 'r.-', linewidth=1.5, markersize=6, label=r'$a_0/a_0^{\mathrm{fold}}$')
ax3.plot(tau_arr, a2_rel, 'g.-', linewidth=1.5, markersize=6, label=r'$a_2/a_2^{\mathrm{fold}}$')
ax3.plot(tau_arr, a4_rel, 'b.-', linewidth=1.5, markersize=6, label=r'$a_4/a_4^{\mathrm{fold}}$')
ax3.axvline(tau_fold, color='red', linestyle='--', alpha=0.3)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel('Relative value (fold = 1)')
ax3.set_title('Individual moments (normalized)')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Numerical derivative
ax4 = axes[1, 1]
# Compute centered differences at each interior point
dR1_dtau = np.zeros_like(tau_arr)  # (local)
for i in range(1, len(tau_arr) - 1):
    dR1_dtau[i] = (R1_arr[i+1] - R1_arr[i-1]) / (tau_arr[i+1] - tau_arr[i-1])
# Forward/backward at endpoints
dR1_dtau[0] = (R1_arr[1] - R1_arr[0]) / (tau_arr[1] - tau_arr[0])
dR1_dtau[-1] = (R1_arr[-1] - R1_arr[-2]) / (tau_arr[-1] - tau_arr[-2])

ax4.plot(tau_arr, dR1_dtau, 'k.-', linewidth=1.5, markersize=6)
ax4.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax4.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label='fold')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$dR_1/d\tau$')
ax4.set_title(r'Numerical derivative $dR_1/d\tau$')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = 's77_r1_tau_trajectory.png'  # (local)
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved to {plot_path}")

# ============================================================================
# STEP 8: GATE VERDICT
# ============================================================================

print(f"\n{'=' * 78}")
print("GATE VERDICT: S77-B6-R1-TRAJECTORY (INFO)")
print("=" * 78)

print(f"\n  R_1(tau) profile across [0, 0.5]:")
print(f"    Total variation: {total_var_pct:.3f}%")
print(f"    R_1 at fold (tau={tau_fold}): {R1_fold_computed:.6f}")
print(f"    Canonical match: {R1_fold_error_pct:.4f}% deviation")
print(f"    Monotonic: {'YES' if is_monotone else 'NO'}")
print(f"    Stationary at fold: {'YES' if is_stationary else 'NO'} (|dR_1/dtau| = {abs(dR1_dtau_fold):.6f})")
print(f"    R_1 min/max: {R1_min:.6f} / {R1_max:.6f}")
print(f"    min at tau = {tau_arr[idx_min]:.4f}, max at tau = {tau_arr[idx_max]:.4f}")

# R-protection context
print(f"\n  R-protection context:")
print(f"    Individual moment variations: a_0={a0_var:.2f}%, a_2={a2_var:.2f}%, a_4={a4_var:.2f}%")
print(f"    R_1 variation: {total_var_pct:.3f}% (cancellation ratio: {min(a0_var, a2_var, a4_var)/max(0.001, total_var_pct):.1f}x)")
print(f"    R_1 is {'STRONGLY' if total_var_pct < 1.0 else 'WEAKLY'} protected across entire tau domain")

print(f"\n  Gate status: INFO (characterization, no pass/fail criterion)")
print(f"\n  Key finding: {'R_1 is stationary at the fold' if is_stationary else 'R_1 is NOT stationary at the fold -- derivative is ' + f'{dR1_dtau_fold:.6f}'}")

print(f"\n{'=' * 78}")
print("COMPUTATION COMPLETE")
print(f"{'=' * 78}")
