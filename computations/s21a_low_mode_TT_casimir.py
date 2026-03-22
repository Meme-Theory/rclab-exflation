"""
Session 21a: Low-Mode TT Casimir Diagnostic (A-1)
===================================================

Tesla-Resonance Agent — Resonance Reinterpretation of the Perturbative CLOSED
Core hypothesis: The constant-ratio trap is a HIGH-MODE phenomenon (Weyl's law).
Low modes couple to cavity shape (boundary conditions, curvature corrections).
If the low-mode contribution to E_TT has different tau-dependence than the
full sum, there exists a frequency scale below which curvature coupling matters.

Diagnostics:
  1. E_TT_low(tau) for lowest N_cut = 50, 100, 200 eigenvalues
  2. R_low(tau) = E_fermion_low / E_boson_low for low modes
  3. Ratio of low-mode to full-mode E_TT at each tau
  4. Spectral action with Schwinger cutoff: f(x) = x * exp(-x)

Data source: recompute from l20_lichnerowicz.py infrastructure
(NPZ only stores aggregates, need individual eigenvalues)

Author: Tesla-Resonance (Session 21a, A-1)
Date: 2026-02-19
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from l20_lichnerowicz import (
    collect_TT_spectrum,
    casimir_energy_from_evals,
    cw_energy_from_evals,
)
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
)
from b6_scalar_vector_laplacian import (
    collect_scalar_spectrum,
    collect_vector_spectrum,
    dim_pq,
)

# Also load fermionic data for R_low computation
def load_fermionic_evals(tau, s19a_path=None):
    """Load individual fermionic eigenvalues at a given tau."""
    if s19a_path is None:
        s19a_path = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')
    data = np.load(s19a_path, allow_pickle=True)
    tau_values = data['tau_values']
    idx = np.argmin(np.abs(tau_values - tau))
    if np.abs(tau_values[idx] - tau) > 0.01:
        print(f"  WARNING: tau={tau:.2f} not in s19a data (closest {tau_values[idx]:.2f})")
        return [], []
    evals = data['eigenvalues'][idx]
    mults = data['multiplicities'][idx]
    return evals, mults


def low_mode_analysis(tau, N_cuts, gens, f_abc, max_pq_sum=6):
    """
    Compute E_TT for lowest N_cut eigenvalues at given tau.

    Returns dict with:
        'all_evals_sorted': sorted (eigenvalue, multiplicity) pairs
        'E_TT_low': dict mapping N_cut -> E_TT using only lowest N_cut modes
        'E_TT_full': E_TT from all modes
        'total_dof': total TT DOF
    """
    tt_result = collect_TT_spectrum(tau, max_pq_sum=max_pq_sum, gens=gens, f_abc=f_abc)

    # Sort all eigenvalue-multiplicity pairs by eigenvalue
    evals_mult = sorted(tt_result['all_evals_with_mult'], key=lambda x: x[0])

    E_TT_full = casimir_energy_from_evals(tt_result['all_evals_with_mult'])

    E_TT_low = {}
    for N_cut in N_cuts:
        # Take the lowest N_cut distinct eigenvalue-multiplicity pairs
        subset = evals_mult[:N_cut]
        E_TT_low[N_cut] = casimir_energy_from_evals(subset)

    return {
        'all_evals_sorted': evals_mult,
        'E_TT_low': E_TT_low,
        'E_TT_full': E_TT_full,
        'total_dof': tt_result['total_TT_dof'],
    }


def schwinger_spectral_action(evals_mult, Lambda):
    """
    Compute spectral action with Schwinger cutoff: f(x) = x * exp(-x).

    S(Lambda, tau) = Sum_n mult_n * f(lambda_n / Lambda^2)
                   = Sum_n mult_n * (lambda_n/Lambda^2) * exp(-lambda_n/Lambda^2)

    This peaks at lambda_n = Lambda^2 and decays for lambda >> Lambda^2.
    """
    S = 0.0
    for ev, mult in evals_mult:
        if ev <= 0:
            continue
        x = ev / Lambda**2
        S += mult * x * np.exp(-x)
    return S


def main():
    print("=" * 72)
    print("  Session 21a A-1: LOW-MODE TT CASIMIR DIAGNOSTIC")
    print("  Tesla-Resonance — Resonance Reinterpretation")
    print("=" * 72)

    t_start = time.time()
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)

    # Use fewer tau values for this diagnostic (recomputing eigenvalues is expensive)
    tau_values = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0])
    N_cuts = [20, 50, 100, 200]
    max_pq_sum = 6

    # Storage
    results = {}

    print(f"\n  Tau values: {tau_values}")
    print(f"  N_cuts: {N_cuts}")
    print(f"  max_pq_sum: {max_pq_sum}")

    # =========================================================================
    # PHASE 1: Low-mode TT Casimir sweep
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 1: LOW-MODE TT CASIMIR SWEEP")
    print("=" * 72)

    for tau in tau_values:
        t0 = time.time()
        print(f"\n  tau = {tau:.2f}...")
        result = low_mode_analysis(tau, N_cuts, gens, f_abc, max_pq_sum)
        results[tau] = result
        dt = time.time() - t0

        print(f"    Total DOF: {result['total_dof']}")
        print(f"    E_TT_full: {result['E_TT_full']:.6e}")
        for N_cut in N_cuts:
            frac = result['E_TT_low'][N_cut] / max(result['E_TT_full'], 1e-30)
            print(f"    E_TT_low(N={N_cut}): {result['E_TT_low'][N_cut]:.6e} "
                  f"({frac*100:.2f}% of full)")
        print(f"    Time: {dt:.1f}s")

    # =========================================================================
    # PHASE 2: Low-mode ratio analysis
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 2: LOW-MODE RATIO ANALYSIS")
    print("=" * 72)

    # Compute E_TT_low / E_TT_full ratio vs tau for each N_cut
    print(f"\n  {'tau':>6}", end="")
    for N in N_cuts:
        print(f"  {'R(N='+str(N)+')':>10}", end="")
    print(f"  {'E_full':>12}")

    for tau in tau_values:
        r = results[tau]
        print(f"  {tau:6.2f}", end="")
        for N in N_cuts:
            ratio = r['E_TT_low'][N] / max(r['E_TT_full'], 1e-30)
            print(f"  {ratio:10.6f}", end="")
        print(f"  {r['E_TT_full']:12.4e}")

    # =========================================================================
    # PHASE 3: Growth rate analysis
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 3: GROWTH RATE ANALYSIS")
    print("  (Is the tau-dependence of low-mode energy different from full?)")
    print("=" * 72)

    # Normalize each series to its value at tau=0
    E_full_norm = np.array([results[tau]['E_TT_full'] for tau in tau_values])
    E_full_norm = E_full_norm / E_full_norm[0]

    print(f"\n  {'tau':>6}  {'E_full/E_full(0)':>16}", end="")
    for N in N_cuts:
        print(f"  {'E_low(N='+str(N)+')/E0':>16}", end="")
    print()

    for i, tau in enumerate(tau_values):
        r = results[tau]
        print(f"  {tau:6.2f}  {E_full_norm[i]:16.6f}", end="")
        for N in N_cuts:
            E_low_0 = results[0.0]['E_TT_low'][N]
            if E_low_0 > 0:
                E_low_norm = r['E_TT_low'][N] / E_low_0
            else:
                E_low_norm = 0.0
            print(f"  {E_low_norm:16.6f}", end="")
        print()

    # =========================================================================
    # PHASE 4: Eigenvalue spectrum structure at selected tau
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 4: EIGENVALUE SPECTRUM STRUCTURE")
    print("=" * 72)

    for tau in [0.0, 0.3, 1.0]:
        r = results[tau]
        evals = [ev for ev, m in r['all_evals_sorted'][:50]]
        print(f"\n  tau = {tau:.2f}: lowest 20 TT eigenvalues:")
        for j in range(min(20, len(evals))):
            ev, mult = r['all_evals_sorted'][j]
            print(f"    [{j:3d}] mu = {ev:10.6f}, mult = {mult}")

    # =========================================================================
    # PHASE 5: Schwinger cutoff spectral action
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 5: SCHWINGER CUTOFF SPECTRAL ACTION")
    print("  f(x) = x * exp(-x), peaked at lambda = Lambda^2")
    print("=" * 72)

    # Sweep Lambda values to find scale where ratio might vary
    Lambda_values = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0])

    print(f"\n  {'Lambda':>8}", end="")
    for tau in tau_values:
        print(f"  {'tau='+str(tau):>10}", end="")
    print()

    S_data = {}  # S_data[Lambda] = array over tau
    for Lambda in Lambda_values:
        S_vals = []
        for tau in tau_values:
            r = results[tau]
            S = schwinger_spectral_action(r['all_evals_sorted'], Lambda)
            S_vals.append(S)
        S_data[Lambda] = np.array(S_vals)
        # Print normalized to tau=0 value
        S0 = S_data[Lambda][0]
        print(f"  {Lambda:8.1f}", end="")
        for S in S_data[Lambda]:
            if S0 > 0:
                print(f"  {S/S0:10.4f}", end="")
            else:
                print(f"  {'---':>10}", end="")
        print()

    # =========================================================================
    # PHASE 6: PLOTTING
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 6: PLOTS")
    print("=" * 72)

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    # Panel 1: E_TT_low vs tau for different N_cuts
    ax = axes[0, 0]
    for N in N_cuts:
        E_low = [results[tau]['E_TT_low'][N] for tau in tau_values]
        ax.plot(tau_values, E_low, '-o', ms=5, label=f'N_cut = {N}')
    E_full = [results[tau]['E_TT_full'] for tau in tau_values]
    ax.plot(tau_values, E_full, 'k--s', ms=6, lw=2, label='Full TT')
    ax.set_xlabel('tau')
    ax.set_ylabel('E_TT (Casimir proxy)')
    ax.set_title('TT Casimir Energy: Low-Mode vs Full')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Normalized growth rates
    ax = axes[0, 1]
    E_full_series = np.array([results[tau]['E_TT_full'] for tau in tau_values])
    ax.plot(tau_values, E_full_series / E_full_series[0], 'k--s', ms=6, lw=2, label='Full')
    for N in N_cuts:
        E_low = np.array([results[tau]['E_TT_low'][N] for tau in tau_values])
        E0 = results[0.0]['E_TT_low'][N]
        if E0 > 0:
            ax.plot(tau_values, E_low / E0, '-o', ms=5, label=f'N = {N}')
    ax.set_xlabel('tau')
    ax.set_ylabel('E(tau) / E(0)')
    ax.set_title('Normalized Growth Rate: Low vs Full')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Low-mode fraction vs tau
    ax = axes[0, 2]
    for N in N_cuts:
        fracs = [results[tau]['E_TT_low'][N] / max(results[tau]['E_TT_full'], 1e-30)
                 for tau in tau_values]
        ax.plot(tau_values, fracs, '-o', ms=5, label=f'N = {N}')
    ax.set_xlabel('tau')
    ax.set_ylabel('E_TT_low / E_TT_full')
    ax.set_title('Low-Mode Fraction vs tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Eigenvalue histogram at tau=0, 0.3, 1.0
    ax = axes[1, 0]
    for tau_plot, color in [(0.0, 'blue'), (0.3, 'red'), (1.0, 'green')]:
        r = results[tau_plot]
        evals = [ev for ev, m in r['all_evals_sorted'][:200]]
        ax.hist(evals, bins=40, alpha=0.5, color=color, label=f'tau={tau_plot}')
    ax.set_xlabel('TT eigenvalue mu')
    ax.set_ylabel('Count (lowest 200)')
    ax.set_title('TT Eigenvalue Distribution (Low Modes)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 5: Schwinger spectral action vs tau at different Lambda
    ax = axes[1, 1]
    for Lambda in [1.0, 3.0, 5.0, 10.0]:
        S_norm = S_data[Lambda] / max(S_data[Lambda][0], 1e-30)
        ax.plot(tau_values, S_norm, '-o', ms=5, label=f'Lambda = {Lambda:.0f}')
    ax.set_xlabel('tau')
    ax.set_ylabel('S(Lambda, tau) / S(Lambda, 0)')
    ax.set_title('Schwinger Spectral Action (normalized)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 6: Lowest eigenvalue vs tau
    ax = axes[1, 2]
    for k in range(min(5, len(results[0.0]['all_evals_sorted']))):
        ev_track = []
        for tau in tau_values:
            r = results[tau]
            if k < len(r['all_evals_sorted']):
                ev_track.append(r['all_evals_sorted'][k][0])
            else:
                ev_track.append(np.nan)
        ax.plot(tau_values, ev_track, '-o', ms=5, label=f'Mode {k}')
    ax.set_xlabel('tau')
    ax.set_ylabel('TT eigenvalue mu')
    ax.set_title('Lowest 5 TT Eigenvalues vs tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', ls='--', alpha=0.5)

    plt.suptitle('Session 21a A-1: Low-Mode TT Casimir Diagnostic\n'
                 '(Tesla-Resonance — Resonance Reinterpretation)',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    out_path = os.path.join(SCRIPT_DIR, 's21a_low_mode_TT.png')
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"  Saved plot: {out_path}")

    # =========================================================================
    # PHASE 7: VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("  DIAGNOSTIC VERDICT")
    print("=" * 72)

    # Check if low-mode growth rate differs from full by > 5%
    E_full_ratio_2 = results[2.0]['E_TT_full'] / results[0.0]['E_TT_full']

    deviation_found = False
    for N in N_cuts:
        E_low_0 = results[0.0]['E_TT_low'][N]
        E_low_2 = results[2.0]['E_TT_low'][N]
        if E_low_0 > 0:
            E_low_ratio_2 = E_low_2 / E_low_0
            dev = abs(E_low_ratio_2 - E_full_ratio_2) / E_full_ratio_2 * 100
            print(f"  N={N}: E_low(2)/E_low(0) = {E_low_ratio_2:.4f}, "
                  f"E_full(2)/E_full(0) = {E_full_ratio_2:.4f}, "
                  f"deviation = {dev:.2f}%")
            if dev > 5.0:
                deviation_found = True
                print(f"    ** DIFFERENT TAU-DEPENDENCE at N={N} (>{dev:.1f}%) **")

    # Schwinger cutoff check
    print(f"\n  Schwinger cutoff analysis:")
    for Lambda in Lambda_values:
        S_ratio = S_data[Lambda][-1] / max(S_data[Lambda][0], 1e-30)
        print(f"    Lambda={Lambda:.1f}: S(tau=2)/S(tau=0) = {S_ratio:.4f}")

    if deviation_found:
        print(f"\n  VERDICT: LOW-MODE DIVERGENCE DETECTED")
        print(f"  The constant-ratio trap does NOT extend to all mode cutoffs.")
        print(f"  Curvature corrections dominate at low mode number.")
        print(f"  A physical cutoff function weighting low modes could break the trap.")
    else:
        print(f"\n  VERDICT: LOW-MODE CONVERGENT")
        print(f"  The constant-ratio behavior extends even to low modes.")
        print(f"  The trap is deeper than Weyl's law alone — it extends to the")
        print(f"  curvature-coupling regime.")

    t_total = time.time() - t_start
    print(f"\n  Total runtime: {t_total:.1f}s")

    # Save data
    save_path = os.path.join(SCRIPT_DIR, 's21a_low_mode_TT.npz')
    np.savez_compressed(
        save_path,
        tau_values=tau_values,
        N_cuts=np.array(N_cuts),
        E_full=np.array([results[tau]['E_TT_full'] for tau in tau_values]),
        **{f'E_low_{N}': np.array([results[tau]['E_TT_low'][N] for tau in tau_values])
           for N in N_cuts},
        **{f'S_Lambda_{Lambda:.0f}': S_data[Lambda] for Lambda in Lambda_values},
    )
    print(f"  Data saved: {save_path}")

    return results, S_data


if __name__ == "__main__":
    results, S_data = main()
