#!/usr/bin/env python3
"""
s77_a2_overshoot.py -- A2-OVERSHOOT (S77-C4-A2-OVERSHOOT)
============================================================

Gate: S77-C4-A2-OVERSHOOT
  PASS:  |delta_G/G| < 0.5 at ALL overshoot tau values
  FAIL:  |delta_G/G| > 5.0 at tau = 1.614
  INFO:  0.5 < |delta_G/G| < 5.0 (moderate variation)

Physics (substrate framing):
-----------------------------
G_N ~ 1/a_2 where a_2 is the second spectral moment (zeta_D(1) in half-
spectrum convention).  The modulus overshoots to tau ~ 1.614 after the
fold transit.  This computation maps a_2(tau) across [0, 1.614] to
determine how much Newton's constant varies during the overshoot epoch.

Context from prior sessions:
  - W2-F (R1-TAU-TRAJECTORY-77): a_0(tau) = 6440 = const (topological).
    R_1(tau) strictly monotone increasing, 11% variation across [0, 0.5].
  - W2-I: No oscillation (N_osc=0), modulus slides at terminal velocity.
  - S73B/S74: a_2(fold) = 2776.17, R_protected = 1.128655.

Method:
  For each tau in a grid covering [0, 1.614], compute D_K eigenvalues
  via Peter-Weyl at max_pq_sum=3, extract a_0, a_2, a_4, R_1.
  Compute delta_G/G = [a_2(fold) - a_2(tau)] / a_2(fold).

Agent: Spectral-Geometer (Session 77, Wave 3, W3-D)
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
print("S77-C4-A2-OVERSHOOT: a_2(tau) at Post-Fold Overshoot Values")
print("=" * 78)
print()

# Gate tau values (from task spec)
TAU_GATE = np.array([0.5, 1.0, 1.5, 1.614])  # (local) gate evaluation points

# Full grid: reference points + intermediate for smooth plot + gate points
TAU_GRID = np.array([
    0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45,
    0.50, 0.60, 0.70, 0.80, 0.90,
    1.00, 1.10, 1.20, 1.30, 1.40,
    1.50, 1.55, 1.60, 1.614,
])  # (local)

# Remove duplicates and sort
TAU_ALL = np.unique(TAU_GRID)  # (local)

MAX_PQ_SUM = 3  # (local) L_max=3, consistent with S74/S77-W2-F
EVAL_CUTOFF = 0.01  # (local) exclude near-zero eigenvalues

# Gate thresholds
PASS_THRESH = 0.5  # (local) |delta_G/G| < 0.5 = PASS
FAIL_THRESH = 5.0  # (local) |delta_G/G| > 5.0 at tau=1.614 = FAIL

print(f"  tau_fold (canonical) = {tau_fold}")
print(f"  a2_fold (canonical) = {a2_fold:.6f}")
print(f"  R_protected_fold (canonical) = {R_protected_fold:.6f}")
print(f"  L_max (max_pq_sum) = {MAX_PQ_SUM}")
print(f"  Eigenvalue cutoff = {EVAL_CUTOFF}")
print(f"  Tau grid: {len(TAU_ALL)} values in [{TAU_ALL[0]:.3f}, {TAU_ALL[-1]:.3f}]")
print(f"  Gate tau values: {TAU_GATE}")
print(f"  Gate: PASS if |delta_G/G| < {PASS_THRESH} at all tau")
print(f"         FAIL if |delta_G/G| > {FAIL_THRESH} at tau=1.614")
print(f"         INFO if {PASS_THRESH} < |delta_G/G| < {FAIL_THRESH}")
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
    """Compute a_0, a_2, a_4 in S73B half-spectrum convention at given tau.

    S73B convention:
      a_k = 0.5 * sum_{n: |lam_n| > cutoff} d_n * |lam_n|^{-k}
    where d_n = dim(p,q) is the Peter-Weyl degeneracy.

    Returns dict with a0, a2, a4, n_evals, lam_min, lam_max.
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
    delta_G = (a2_fold - r['a2']) / a2_fold  # (local)
    print(f"  [{i+1:2d}/{len(TAU_ALL)}] tau={tau_val:.4f}: "
          f"a0={r['a0']:.1f}, a2={r['a2']:.4f}, a4={r['a4']:.6f}, "
          f"R_1={R1_val:.6f}, delta_G/G={delta_G:+.4f}, "
          f"lam=[{r['lam_min']:.3f},{r['lam_max']:.3f}], "
          f"n={r['n_evals']}, dt={dt:.1f}s")

t_total = time.time() - t_start  # (local)
print(f"\n  Total computation time: {t_total:.1f}s")
print()

# ============================================================================
# STEP 3: EXTRACT ARRAYS AND COMPUTE DERIVED QUANTITIES
# ============================================================================

print("=" * 78)
print("STEP 3: a_2(tau) ANALYSIS AND DELTA_G/G")
print("=" * 78)

tau_arr = np.array([r['tau'] for r in results])  # (local)
a0_arr = np.array([r['a0'] for r in results])  # (local)
a2_arr = np.array([r['a2'] for r in results])  # (local)
a4_arr = np.array([r['a4'] for r in results])  # (local)
R1_arr = a0_arr * a4_arr / a2_arr**2  # (local)
delta_G_arr = (a2_fold - a2_arr) / a2_fold  # (local)  delta_G/G = [a2(fold) - a2(tau)] / a2(fold)

# Full table
print(f"\n  {'tau':>6}  {'a_0':>9}  {'a_2':>12}  {'a_4':>14}  {'R_1':>10}  {'delta_G/G':>11}  {'|dG/G|':>8}")
print(f"  " + "-" * 80)
for i in range(len(tau_arr)):
    marker = ""  # (local)
    if abs(tau_arr[i] - tau_fold) < 0.005:
        marker = " <-- FOLD"
    elif tau_arr[i] in TAU_GATE:
        marker = " <-- GATE"
    print(f"  {tau_arr[i]:6.3f}  {a0_arr[i]:>9.1f}  {a2_arr[i]:>12.4f}  {a4_arr[i]:>14.6f}  "
          f"{R1_arr[i]:10.6f}  {delta_G_arr[i]:+11.6f}  {abs(delta_G_arr[i]):8.4f}{marker}")

# ============================================================================
# STEP 4: CROSS-CHECKS
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 4: CROSS-CHECKS")
print("=" * 78)

# Cross-check 1: a_0 = const (topological, confirmed by W2-F)
a0_min = np.min(a0_arr)  # (local)
a0_max = np.max(a0_arr)  # (local)
a0_var_pct = 100 * (a0_max - a0_min) / np.mean(a0_arr)  # (local)
print(f"\n  [CC1] a_0 constancy: min={a0_min:.1f}, max={a0_max:.1f}, variation={a0_var_pct:.4f}%")
if a0_var_pct < 0.01:
    print(f"    PASS: a_0 = {np.mean(a0_arr):.1f} = const (topological invariant)")
else:
    print(f"    WARNING: a_0 varies by {a0_var_pct:.4f}% -- check eigenvalue counting")

# Cross-check 2: a_2 > 0 everywhere (positive Newton's constant)
a2_positive = np.all(a2_arr > 0)  # (local)
print(f"\n  [CC2] a_2 > 0 everywhere: {'PASS' if a2_positive else 'FAIL'}")
if a2_positive:
    print(f"    a_2 range: [{np.min(a2_arr):.4f}, {np.max(a2_arr):.4f}]")
else:
    print(f"    STRUCTURAL FAILURE: a_2 < 0 implies negative G_N")

# Cross-check 3: a_2 smoothness (no jumps > 20% between adjacent grid points)
a2_diffs = np.abs(np.diff(a2_arr) / a2_arr[:-1])  # (local)
max_jump = np.max(a2_diffs)  # (local)
smooth = max_jump < 0.20  # (local)
print(f"\n  [CC3] a_2 smoothness: max relative jump = {max_jump:.4f} ({100*max_jump:.2f}%)")
print(f"    {'PASS' if smooth else 'WARNING'}: a_2 is {'smooth' if smooth else 'discontinuous'}")

# Cross-check 4: R_1 consistency with W2-F at tau=0.5
idx_05 = np.argmin(np.abs(tau_arr - 0.5))  # (local)
if abs(tau_arr[idx_05] - 0.5) < 0.01:
    R1_at_05 = R1_arr[idx_05]  # (local)
    R1_w2f_05 = 1.237  # (local) from W2-F result: R_1(0.5) = 1.237
    R1_dev = abs(R1_at_05 - R1_w2f_05) / R1_w2f_05  # (local)
    print(f"\n  [CC4] R_1(0.5) consistency with W2-F:")
    print(f"    This computation: R_1(0.5) = {R1_at_05:.6f}")
    print(f"    W2-F result:      R_1(0.5) = {R1_w2f_05:.3f}")
    print(f"    Deviation: {100*R1_dev:.3f}% -- {'PASS' if R1_dev < 0.01 else 'CHECK'}")

# Cross-check 5: a_2 at fold matches canonical
idx_fold = np.argmin(np.abs(tau_arr - tau_fold))  # (local)
a2_at_fold = a2_arr[idx_fold]  # (local)
a2_fold_dev = abs(a2_at_fold - a2_fold) / a2_fold  # (local)
print(f"\n  [CC5] a_2(fold) matches canonical:")
print(f"    Computed: a_2(fold) = {a2_at_fold:.6f}")
print(f"    Canonical: a2_fold = {a2_fold:.6f}")
print(f"    Deviation: {100*a2_fold_dev:.4f}% -- {'PASS' if a2_fold_dev < 0.001 else 'CHECK'}")

# ============================================================================
# STEP 5: GATE EVALUATION
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 5: GATE EVALUATION -- S77-C4-A2-OVERSHOOT")
print("=" * 78)

print(f"\n  Gate definition:")
print(f"    PASS:  |delta_G/G| < {PASS_THRESH} at ALL gate tau values")
print(f"    FAIL:  |delta_G/G| > {FAIL_THRESH} at tau = 1.614")
print(f"    INFO:  {PASS_THRESH} < |delta_G/G| < {FAIL_THRESH}")

# Evaluate at gate points
gate_results = []  # (local)
print(f"\n  Gate tau  |  a_2(tau)     |  delta_G/G    |  |delta_G/G|")
print(f"  " + "-" * 60)
for tau_g in TAU_GATE:
    idx = np.argmin(np.abs(tau_arr - tau_g))  # (local)
    a2_g = a2_arr[idx]  # (local)
    dG_g = delta_G_arr[idx]  # (local)
    gate_results.append((tau_g, a2_g, dG_g))
    print(f"  {tau_g:>6.3f}  |  {a2_g:>12.4f}  |  {dG_g:+12.6f}  |  {abs(dG_g):10.6f}")

# Determine verdict
max_abs_dG = max(abs(dG) for _, _, dG in gate_results)  # (local)
dG_at_1614 = abs(gate_results[-1][2])  # (local) last entry is tau=1.614

if max_abs_dG < PASS_THRESH:
    verdict = "PASS"
    verdict_detail = f"|delta_G/G|_max = {max_abs_dG:.4f} < {PASS_THRESH}"
elif dG_at_1614 > FAIL_THRESH:
    verdict = "FAIL"
    verdict_detail = f"|delta_G/G|(1.614) = {dG_at_1614:.4f} > {FAIL_THRESH}"
else:
    verdict = "INFO"
    verdict_detail = f"|delta_G/G|_max = {max_abs_dG:.4f}, in [{PASS_THRESH}, {FAIL_THRESH}]"

print(f"\n  VERDICT: {verdict}")
print(f"    {verdict_detail}")
print(f"    Physical meaning: G_N varies by factor {1/(1-max_abs_dG) if max_abs_dG < 1 else 'INF':}")
print(f"    a_2(fold)/a_2(1.614) = {a2_fold / gate_results[-1][1]:.4f}")

# ============================================================================
# STEP 6: STRUCTURAL ANALYSIS
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 6: STRUCTURAL ANALYSIS")
print("=" * 78)

# a_2 behavior: monotonic?
a2_diffs_signed = np.diff(a2_arr)  # (local)
n_inc = np.sum(a2_diffs_signed > 0)  # (local)
n_dec = np.sum(a2_diffs_signed < 0)  # (local)
a2_monotone = (n_inc == 0) or (n_dec == 0)  # (local)
direction = "DECREASING" if n_dec > n_inc else "INCREASING"  # (local)

print(f"\n  a_2(tau) monotonicity: {n_inc} increasing, {n_dec} decreasing steps")
print(f"    {'MONOTONE ' + direction if a2_monotone else 'NON-MONOTONE'}")

# R_1 behavior across full range
R1_min = np.min(R1_arr)  # (local)
R1_max = np.max(R1_arr)  # (local)
R1_var_pct = 100 * (R1_max - R1_min) / np.mean(R1_arr)  # (local)
print(f"\n  R_1(tau) across [0, 1.614]:")
print(f"    min = {R1_min:.6f} at tau = {tau_arr[np.argmin(R1_arr)]:.3f}")
print(f"    max = {R1_max:.6f} at tau = {tau_arr[np.argmax(R1_arr)]:.3f}")
print(f"    total variation = {R1_var_pct:.2f}%")

# lambda_min behavior (smallest eigenvalue)
lam_min_arr = np.array([r['lam_min'] for r in results])  # (local)
print(f"\n  lambda_min(tau) across [0, 1.614]:")
print(f"    min = {np.min(lam_min_arr):.6f} at tau = {tau_arr[np.argmin(lam_min_arr)]:.3f}")
print(f"    max = {np.max(lam_min_arr):.6f} at tau = {tau_arr[np.argmax(lam_min_arr)]:.3f}")

# Jensen metric scale factors at tau=1.614 for context
tau_max = 1.614  # (local)
L1_max = np.exp(2 * tau_max)  # (local)
L2_max = np.exp(-2 * tau_max)  # (local)
L3_max = np.exp(tau_max)  # (local)
print(f"\n  Jensen scale factors at tau = {tau_max}:")
print(f"    L1(u(1))  = e^{{2*{tau_max}}} = {L1_max:.4f}")
print(f"    L2(su(2)) = e^{{-2*{tau_max}}} = {L2_max:.6f}")
print(f"    L3(C^2)   = e^{{{tau_max}}} = {L3_max:.4f}")
print(f"    su(2) shrinks by factor {L2_max:.2e}, C^2 expands by {L3_max:.2f}")
print(f"    L1*L2^3*L3^4 = {L1_max * L2_max**3 * L3_max**4:.6f} (volume-preserving check)")

# ============================================================================
# STEP 7: SAVE DATA
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 7: SAVE DATA")
print("=" * 78)

outfile = os.path.join(SCRIPT_DIR, 's77_a2_overshoot.npz')  # (local)
np.savez(outfile,
         tau=tau_arr,
         a0=a0_arr,
         a2=a2_arr,
         a4=a4_arr,
         R1=R1_arr,
         delta_G=delta_G_arr,
         lam_min=lam_min_arr,
         gate_tau=np.array([g[0] for g in gate_results]),
         gate_a2=np.array([g[1] for g in gate_results]),
         gate_dG=np.array([g[2] for g in gate_results]),
         verdict=np.array([verdict]),
         # Metadata
         a2_fold_canonical=np.array([a2_fold]),
         max_pq_sum=np.array([MAX_PQ_SUM]),
         eval_cutoff=np.array([EVAL_CUTOFF]),
         )
print(f"  Saved: {outfile}")

# ============================================================================
# STEP 8: PLOTS
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 8: PLOTS")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: a_2(tau)
ax = axes[0, 0]
ax.plot(tau_arr, a2_arr, 'b-o', markersize=4, label='$a_2(\\tau)$')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label=f'fold ($\\tau={tau_fold}$)')
ax.axhline(a2_fold, color='gray', linestyle=':', alpha=0.5, label=f'$a_2$(fold)={a2_fold:.1f}')
for tau_g in TAU_GATE:
    idx = np.argmin(np.abs(tau_arr - tau_g))
    ax.plot(tau_arr[idx], a2_arr[idx], 'rv', markersize=8)
ax.set_xlabel('$\\tau$ (Jensen parameter)')
ax.set_ylabel('$a_2(\\tau)$')
ax.set_title('$a_2(\\tau)$ -- Second Spectral Moment ($G_N \\sim 1/a_2$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: delta_G/G
ax = axes[0, 1]
ax.plot(tau_arr, delta_G_arr, 'r-o', markersize=4, label='$\\delta G/G$')
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axhline(PASS_THRESH, color='green', linestyle='--', alpha=0.5, label=f'PASS threshold ({PASS_THRESH})')
ax.axhline(-PASS_THRESH, color='green', linestyle='--', alpha=0.5)
ax.axhline(FAIL_THRESH, color='red', linestyle='--', alpha=0.5, label=f'FAIL threshold ({FAIL_THRESH})')
ax.axhline(-FAIL_THRESH, color='red', linestyle='--', alpha=0.5)
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label=f'fold')
for tau_g in TAU_GATE:
    idx = np.argmin(np.abs(tau_arr - tau_g))
    ax.plot(tau_arr[idx], delta_G_arr[idx], 'kv', markersize=8)
ax.set_xlabel('$\\tau$ (Jensen parameter)')
ax.set_ylabel('$\\delta G/G = [a_2(\\mathrm{fold}) - a_2(\\tau)] / a_2(\\mathrm{fold})$')
ax.set_title(f'$\\delta G/G$ -- Gate: {verdict}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: R_1(tau) full range
ax = axes[1, 0]
ax.plot(tau_arr, R1_arr, 'g-o', markersize=4, label='$R_1(\\tau)$')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label=f'fold')
ax.axhline(R_protected_fold, color='gray', linestyle=':', alpha=0.5, label=f'$R_1$(fold)={R_protected_fold:.4f}')
ax.set_xlabel('$\\tau$ (Jensen parameter)')
ax.set_ylabel('$R_1 = a_0 a_4 / a_2^2$')
ax.set_title('$R_1(\\tau)$ -- R-Protected Ratio (full range)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: a_0, a_2, a_4 together (normalized)
ax = axes[1, 1]
ax.plot(tau_arr, a0_arr / a0_fold, 'k-', linewidth=2, label='$a_0/a_0^{\\mathrm{fold}}$ (topological)')
ax.plot(tau_arr, a2_arr / a2_fold, 'b-o', markersize=3, label='$a_2/a_2^{\\mathrm{fold}}$ (gravity)')
ax.plot(tau_arr, a4_arr / a4_fold, 'r-s', markersize=3, label='$a_4/a_4^{\\mathrm{fold}}$ (gauge)')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.7, label='fold')
ax.set_xlabel('$\\tau$ (Jensen parameter)')
ax.set_ylabel('$a_k(\\tau) / a_k(\\mathrm{fold})$')
ax.set_title('Spectral Moments (Normalized to Fold)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(f'S77-C4-A2-OVERSHOOT: $a_2(\\tau)$ at Post-Fold Overshoot [Gate: {verdict}]',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotfile = os.path.join(SCRIPT_DIR, 's77_a2_overshoot.png')  # (local)
plt.savefig(plotfile, dpi=150)
print(f"  Saved: {plotfile}")
plt.close()

# ============================================================================
# STEP 9: SUMMARY
# ============================================================================

print(f"\n{'=' * 78}")
print("STEP 9: SUMMARY")
print("=" * 78)

print(f"\n  GATE: S77-C4-A2-OVERSHOOT")
print(f"  VERDICT: {verdict}")
print(f"  {verdict_detail}")
print()
print(f"  Key results:")
for tau_g, a2_g, dG_g in gate_results:
    print(f"    tau = {tau_g:.3f}: a_2 = {a2_g:.4f}, delta_G/G = {dG_g:+.6f} ({abs(dG_g)*100:.2f}%)")
print()
print(f"  a_0 = {np.mean(a0_arr):.1f} = const (confirmed topological)")
print(f"  a_2 direction: {direction}")
print(f"  a_2 range: [{np.min(a2_arr):.4f}, {np.max(a2_arr):.4f}]")
print(f"  R_1 range: [{R1_min:.6f}, {R1_max:.6f}] ({R1_var_pct:.2f}% variation)")
print(f"  G_N(fold)/G_N(1.614) = a_2(1.614)/a_2(fold) = {gate_results[-1][1]/a2_fold:.4f}")
print()
print(f"  Files: s77_a2_overshoot.npz, s77_a2_overshoot.png")
print(f"\n{'=' * 78}")
print("COMPUTATION COMPLETE")
print("=" * 78)
