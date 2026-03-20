#!/usr/bin/env python3
"""
Session 28b-2: L-3 Relaxation Times near BCS Transition
=========================================================

Gate L-3 (Diagnostic): Re-entrant (2,0) sector with two tau_LK divergences
= dynamical tau-trapping window.

Method:
-------
Near the BCS transition M_max = 1, the relaxation time in mean-field BCS
theory scales as:

    tau_LK ~ 1 / |M_max - 1|

with critical exponent z*nu = 1. This divergence signals critical slowing
down at the normal-superconductor boundary.

For each sector at mu = lambda_min (the physically relevant chemical
potential), we:
  1. Compute M_max(tau) from the s27 multi-sector BCS data
  2. Identify tau_c where M_max crosses 1 (critical tau values)
  3. Compute tau_LK(tau) = 1 / |M_max(tau) - 1|
  4. Check for re-entrant behavior in the (2,0)/(0,2) sectors

Data:
-----
  s27_multisector_bcs.npz: M_max[sector, tau, mu] with 9 sectors, 9 tau, 12 mu
  s28a_torsionful_bcs.npz: M_max_K, M_max_can for D_K and D_can connections
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent
S27_FILE = DATA_DIR / 's27_multisector_bcs.npz'
S28A_FILE = DATA_DIR / 's28a_torsionful_bcs.npz'
OUT_NPZ = DATA_DIR / 's28b_relaxation_times.npz'
OUT_PNG = DATA_DIR / 's28b_relaxation_times.png'

# Fine tau grid for interpolation
TAU_FINE = np.linspace(0.0, 0.50, 500)


def find_crossings(tau_arr: np.ndarray, mmax_arr: np.ndarray, threshold: float = 1.0):
    """
    Find tau values where M_max crosses `threshold` using linear interpolation.

    Returns:
        list of (tau_cross, direction): direction = +1 for subcrit->supercrit, -1 for super->sub
    """
    crossings = []
    for i in range(len(tau_arr) - 1):
        delta_lo = mmax_arr[i] - threshold
        delta_hi = mmax_arr[i + 1] - threshold
        if delta_lo * delta_hi < 0:
            # Linear interpolation
            tau_cross = tau_arr[i] + (-delta_lo) / (delta_hi - delta_lo) * (tau_arr[i + 1] - tau_arr[i])
            direction = +1 if delta_hi > 0 else -1
            crossings.append((tau_cross, direction))
    return crossings


def compute_relaxation_times(tau_arr, mmax_arr, tau_fine):
    """
    Compute tau_LK(tau) = 1 / |M_max(tau) - 1| on fine grid using cubic spline.

    Parameters:
        tau_arr: shape (n_tau,) raw tau grid
        mmax_arr: shape (n_tau,) M_max values
        tau_fine: shape (n_fine,) fine evaluation grid

    Returns:
        mmax_fine: interpolated M_max on fine grid
        tau_lk: relaxation time 1/|M_max - 1| on fine grid (capped at 1e6)
    """
    cs = CubicSpline(tau_arr, mmax_arr)
    mmax_fine = cs(tau_fine)
    # Relaxation time: diverges at M_max = 1
    distance = np.abs(mmax_fine - 1.0)
    tau_lk = np.where(distance > 1e-6, 1.0 / distance, 1e6)  # cap at 1e6
    return mmax_fine, tau_lk


def refine_crossing(tau_arr, mmax_arr, tau_fine):
    """
    Find precise crossings on the fine grid via cubic spline.

    Returns list of (tau_cross, direction) tuples.
    """
    cs = CubicSpline(tau_arr, mmax_arr)
    mmax_fine = cs(tau_fine)
    crossings = find_crossings(tau_fine, mmax_fine, threshold=1.0)
    return crossings


def main():
    # ─── Load s27 data ───────────────────────────────────────────────────────
    d27 = np.load(S27_FILE, allow_pickle=True)
    tau_values = d27['tau_values']       # (9,)
    mu_ratios = d27['mu_ratios']         # (12,)
    sectors = d27['sectors']             # (9, 4): p, q, dim, mult
    M_max = d27['M_max']                 # (9, 9, 12)

    # mu/lambda_min = 1.0 index
    mu_idx_10 = int(np.where(mu_ratios == 1.0)[0][0])

    n_sectors = sectors.shape[0]
    sector_labels = [f'({sectors[i,0]},{sectors[i,1]})' for i in range(n_sectors)]

    print("=" * 72)
    print("L-3 RELAXATION TIMES: BCS Critical Slowing Down Analysis")
    print("=" * 72)
    print(f"tau grid: {tau_values}")
    print(f"mu/lambda_min = 1.0 (index {mu_idx_10})")
    print()

    # ─── Per-sector analysis at mu = lambda_min ──────────────────────────────
    results = {}

    print("─── M_max(tau) at mu = lambda_min ───")
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        mmax_tau = M_max[si, :, mu_idx_10]

        # Raw crossings
        raw_crossings = find_crossings(tau_values, mmax_tau)
        # Refined crossings via cubic spline
        refined_crossings = refine_crossing(tau_values, mmax_tau, TAU_FINE)

        # Fine-grid relaxation time
        mmax_fine, tau_lk_fine = compute_relaxation_times(tau_values, mmax_tau, TAU_FINE)

        # Classification
        always_super = np.all(mmax_tau > 1.0)
        always_sub = np.all(mmax_tau < 1.0)
        is_reentrant = len(refined_crossings) >= 2

        status = "ALWAYS SUPERCRITICAL" if always_super else \
                 "ALWAYS SUBCRITICAL" if always_sub else \
                 f"RE-ENTRANT ({len(refined_crossings)} crossings)" if is_reentrant else \
                 f"SINGLE TRANSITION ({len(refined_crossings)} crossing)"

        print(f"\n  Sector ({p},{q}): {status}")
        print(f"    M_max range: [{mmax_tau.min():.4f}, {mmax_tau.max():.4f}]")
        for tc, dirn in refined_crossings:
            arrow = "sub->super" if dirn > 0 else "super->sub"
            print(f"    tau_c = {tc:.5f} ({arrow})")

        # Peak tau_LK (maximum relaxation time in accessible range)
        peak_idx = np.argmax(tau_lk_fine)
        peak_tau_lk = tau_lk_fine[peak_idx]
        peak_tau = TAU_FINE[peak_idx]
        if peak_tau_lk < 1e6:
            print(f"    Peak tau_LK = {peak_tau_lk:.2f} at tau = {peak_tau:.4f}")

        results[f'mmax_{p}_{q}'] = mmax_tau
        results[f'mmax_fine_{p}_{q}'] = mmax_fine
        results[f'tau_lk_{p}_{q}'] = tau_lk_fine
        results[f'crossings_{p}_{q}'] = np.array([(tc, d) for tc, d in refined_crossings]) if refined_crossings else np.array([])

    # ─── Specific (2,0) re-entrant analysis ──────────────────────────────────
    print()
    print("=" * 72)
    print("KEY DIAGNOSTIC: (2,0) Sector Re-Entrant Behavior")
    print("=" * 72)

    # (2,0) is sector index 4
    si_20 = 4
    mmax_20 = M_max[si_20, :, mu_idx_10]
    crossings_20 = refine_crossing(tau_values, mmax_20, TAU_FINE)

    print(f"  M_max(tau) for (2,0) at mu = lambda_min:")
    for ti in range(len(tau_values)):
        marker = " <-- SUPERCRITICAL" if mmax_20[ti] > 1.0 else ""
        print(f"    tau={tau_values[ti]:.2f}: M_max = {mmax_20[ti]:.6f}{marker}")

    if len(crossings_20) >= 2:
        tau_c1, dir1 = crossings_20[0]
        tau_c2, dir2 = crossings_20[1]
        window = tau_c2 - tau_c1
        print(f"\n  RE-ENTRANT CONFIRMED:")
        print(f"    tau_c1 = {tau_c1:.5f} ({('sub->super' if dir1 > 0 else 'super->sub')})")
        print(f"    tau_c2 = {tau_c2:.5f} ({('sub->super' if dir2 > 0 else 'super->sub')})")
        print(f"    Subcritical window: [{tau_c1:.4f}, {tau_c2:.4f}] (width = {window:.4f})")
        print(f"    Interpretation: (2,0) is supercritical at tau=0, drops below 1 near tau~{tau_c1:.2f},")
        print(f"    stays subcritical through the bulk of the deformation, then re-enters")
        print(f"    supercritical phase at tau~{tau_c2:.2f}.")

        results['reentrant_20_tau_c1'] = tau_c1
        results['reentrant_20_tau_c2'] = tau_c2
        results['reentrant_20_window'] = window
    else:
        print(f"\n  WARNING: Expected 2 crossings, found {len(crossings_20)}")
        for tc, d in crossings_20:
            print(f"    tau_c = {tc:.5f}")

    # ─── Also check (0,2) (conjugate sector) ────────────────────────────────
    si_02 = 5
    mmax_02 = M_max[si_02, :, mu_idx_10]
    crossings_02 = refine_crossing(tau_values, mmax_02, TAU_FINE)
    print(f"\n  (0,2) conjugate sector: {len(crossings_02)} crossings")
    for tc, d in crossings_02:
        print(f"    tau_c = {tc:.5f}")

    # ─── Torsionful (D_can) comparison ───────────────────────────────────────
    print()
    print("=" * 72)
    print("TORSIONFUL (D_can) COMPARISON")
    print("=" * 72)

    has_torsion = S28A_FILE.exists()
    if has_torsion:
        d28a = np.load(S28A_FILE, allow_pickle=True)
        tau_28a = d28a['tau_values']
        mu_28a = d28a['mu_ratios']
        sectors_28a = d28a['sectors']
        M_max_K = d28a['M_max_K']     # (8, 10, 5)
        M_max_can = d28a['M_max_can']  # (8, 10, 5)

        # mu/lambda_min = 1.0 in this dataset
        mu_idx_28a = int(np.where(mu_28a == 1.0)[0][0]) if 1.0 in mu_28a else None

        if mu_idx_28a is not None:
            print(f"  tau grid (10 pts): {tau_28a}")
            print(f"  mu/lambda_min = 1.0 at index {mu_idx_28a}")

            tau_fine_28a = np.linspace(tau_28a[0], tau_28a[-1], 500)

            for si in range(sectors_28a.shape[0]):
                p, q = sectors_28a[si, 0], sectors_28a[si, 1]
                mmax_K = M_max_K[si, :, mu_idx_28a]
                mmax_can = M_max_can[si, :, mu_idx_28a]

                cross_K = refine_crossing(tau_28a, mmax_K, tau_fine_28a)
                cross_can = refine_crossing(tau_28a, mmax_can, tau_fine_28a)

                print(f"\n  ({p},{q}):")
                print(f"    D_K:   M_max range [{mmax_K.min():.4f}, {mmax_K.max():.4f}], {len(cross_K)} crossings", end="")
                for tc, d in cross_K:
                    print(f" tau_c={tc:.4f}", end="")
                print()
                print(f"    D_can: M_max range [{mmax_can.min():.4f}, {mmax_can.max():.4f}], {len(cross_can)} crossings", end="")
                for tc, d in cross_can:
                    print(f" tau_c={tc:.4f}", end="")
                print()

                # Enhancement
                ratio = mmax_can / np.maximum(mmax_K, 1e-10)
                print(f"    D_can/D_K enhancement: [{ratio.min():.2f}, {ratio.max():.2f}]")

                results[f'mmax_K_{p}_{q}'] = mmax_K
                results[f'mmax_can_{p}_{q}'] = mmax_can
        else:
            print("  mu=1.0 not found in s28a data")
    else:
        print("  s28a_torsionful_bcs.npz not found -- skipping")

    # ─── Summary table ───────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("SUMMARY: Sector Classification at mu = lambda_min")
    print("=" * 72)
    print(f"{'Sector':<10} {'M_max range':<25} {'#Cross':<8} {'Type':<30}")
    print("-" * 72)
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        mmax_tau = M_max[si, :, mu_idx_10]
        crossings = refine_crossing(tau_values, mmax_tau, TAU_FINE)
        mlo, mhi = mmax_tau.min(), mmax_tau.max()
        nc = len(crossings)
        if np.all(mmax_tau > 1.0):
            stype = "ALWAYS SUPERCRITICAL"
        elif np.all(mmax_tau < 1.0):
            stype = "ALWAYS SUBCRITICAL"
        elif nc >= 2:
            stype = f"RE-ENTRANT (tau in [{crossings[0][0]:.3f},{crossings[1][0]:.3f}])"
        elif nc == 1:
            stype = f"TRANSITION at tau={crossings[0][0]:.3f}"
        else:
            stype = "MARGINAL"
        print(f"({p},{q}){'':<6} [{mlo:.4f}, {mhi:.4f}]{'':<4} {nc:<8} {stype}")

    # ─── Gate Verdict ────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("GATE L-3 VERDICT")
    print("=" * 72)

    crossings_20_final = refine_crossing(tau_values, M_max[4, :, mu_idx_10], TAU_FINE)
    has_reentrant = len(crossings_20_final) >= 2

    if has_reentrant:
        print("  L-3: PASS (DIAGNOSTIC)")
        print(f"  (2,0) sector shows re-entrant behavior with 2 divergences.")
        print(f"  Subcritical window defines a dynamical tau-trapping region.")
        verdict = "PASS"
    else:
        print("  L-3: FAIL")
        print(f"  (2,0) sector does NOT show expected re-entrant behavior.")
        verdict = "FAIL"

    # ─── Save ────────────────────────────────────────────────────────────────
    results['tau_values'] = tau_values
    results['tau_fine'] = TAU_FINE
    results['mu_ratios'] = mu_ratios
    results['sectors'] = sectors
    results['verdict'] = verdict
    if has_torsion:
        results['tau_values_28a'] = tau_28a

    np.savez_compressed(OUT_NPZ, **results)
    print(f"\n  Saved: {OUT_NPZ}")

    # ─── Plot ────────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('L-3: BCS Relaxation Times near Transition ($\\mu = \\lambda_{\\min}$)', fontsize=14)

    # Panel (a): M_max(tau) for all sectors
    ax = axes[0, 0]
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        mmax_fine, _ = compute_relaxation_times(tau_values, M_max[si, :, mu_idx_10], TAU_FINE)
        ax.plot(TAU_FINE, mmax_fine, label=f'({p},{q})')
    ax.axhline(y=1.0, color='k', linestyle='--', alpha=0.5, label='$M_{\\max}=1$ (transition)')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$M_{\\max}$')
    ax.set_title('(a) BCS coupling strength')
    ax.set_ylim(0, 10)
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel (b): tau_LK(tau) = 1/|M_max - 1| for sectors that cross 1
    ax = axes[0, 1]
    crossing_sectors = []
    for si in range(n_sectors):
        mmax_tau = M_max[si, :, mu_idx_10]
        if np.any(mmax_tau > 1.0) and np.any(mmax_tau < 1.0):
            crossing_sectors.append(si)

    for si in crossing_sectors:
        p, q = sectors[si, 0], sectors[si, 1]
        _, tau_lk = compute_relaxation_times(tau_values, M_max[si, :, mu_idx_10], TAU_FINE)
        ax.semilogy(TAU_FINE, tau_lk, label=f'({p},{q})')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$\\tau_{LK} = 1/|M_{\\max} - 1|$')
    ax.set_title('(b) Relaxation time (crossing sectors)')
    ax.set_ylim(1, 1e6)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (c): (2,0) re-entrant detail
    ax = axes[1, 0]
    si_20 = 4
    mmax_fine_20, tau_lk_20 = compute_relaxation_times(tau_values, M_max[si_20, :, mu_idx_10], TAU_FINE)
    ax.plot(TAU_FINE, mmax_fine_20, 'b-', linewidth=2, label='$M_{\\max}$')
    ax.axhline(y=1.0, color='r', linestyle='--', alpha=0.7)
    ax.fill_between(TAU_FINE, 0, 2, where=(mmax_fine_20 < 1.0), alpha=0.15, color='blue',
                    label='Subcritical window')
    for tc, d in crossings_20_final:
        ax.axvline(x=tc, color='red', linestyle=':', alpha=0.7)
        ax.annotate(f'$\\tau_c={tc:.3f}$', xy=(tc, 1.0), fontsize=9,
                    xytext=(tc + 0.02, 1.3), arrowprops=dict(arrowstyle='->', color='red'))
    ax.scatter(tau_values, M_max[si_20, :, mu_idx_10], color='blue', zorder=5, s=30)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$M_{\\max}$')
    ax.set_title('(c) (2,0) sector: Re-entrant behavior')
    ax.set_ylim(0, 2.0)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (d): Torsionful comparison for (2,0)
    ax = axes[1, 1]
    if has_torsion and mu_idx_28a is not None:
        # Find (2,0) in s28a sectors
        si_20_28a = None
        for si in range(sectors_28a.shape[0]):
            if sectors_28a[si, 0] == 2 and sectors_28a[si, 1] == 0:
                si_20_28a = si
                break

        if si_20_28a is not None:
            tau_fine_28a = np.linspace(tau_28a[0], tau_28a[-1], 500)
            mmax_K_20 = M_max_K[si_20_28a, :, mu_idx_28a]
            mmax_can_20 = M_max_can[si_20_28a, :, mu_idx_28a]

            cs_K = CubicSpline(tau_28a, mmax_K_20)
            cs_can = CubicSpline(tau_28a, mmax_can_20)

            ax.plot(tau_fine_28a, cs_K(tau_fine_28a), 'b-', linewidth=2, label='$D_K$ (Kosmann)')
            ax.plot(tau_fine_28a, cs_can(tau_fine_28a), 'r-', linewidth=2, label='$D_{can}$ (canonical)')
            ax.scatter(tau_28a, mmax_K_20, color='blue', zorder=5, s=25)
            ax.scatter(tau_28a, mmax_can_20, color='red', zorder=5, s=25)
            ax.axhline(y=1.0, color='k', linestyle='--', alpha=0.5)
            ax.set_title('(d) (2,0): Kosmann vs Canonical')
        else:
            ax.text(0.5, 0.5, '(2,0) not in torsionful data', ha='center', va='center',
                    transform=ax.transAxes)
    else:
        ax.text(0.5, 0.5, 'No torsionful data', ha='center', va='center',
                transform=ax.transAxes)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$M_{\\max}$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_PNG}")
    plt.close()


if __name__ == '__main__':
    main()
