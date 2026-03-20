#!/usr/bin/env python3
"""
Session 21c P0-4: Neutrino Fine-Grid R(tau) near tau = 1.6

Fine-grid computation of the neutrino mass-squared ratio
R(tau) = (lambda_3^2 - lambda_2^2) / (lambda_2^2 - lambda_1^2)
near the peak found at tau = 1.60 on the coarse grid.

Target: R = 32.6 (atmospheric/solar mass-squared ratio)
Berry found R_max = 31.94 at tau = 1.60 on Δτ = 0.10 grid.

Protocol:
  - Fine grid: tau = 1.50 to 1.70, Δτ = 0.02 (11 points)
  - Extract three lightest Dirac eigenvalues at each tau
  - Compute R(tau)
  - Check convergence at max_pq_sum = 7 and 8

Constraint Gates:
  PASS: R_max > 32.6
  SOFT MISS: R_max in [30, 32.6]
  HARD CLOSED: R_max < 30

Output: s21c_neutrino_fine_grid.npz, s21c_neutrino_R.png
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt

# Add tier0-computation to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

def compute_R(tau_val, gens, f_abc, gammas, max_pq_sum=6, verbose=False):
    """
    Compute the neutrino mass-squared ratio R at a given tau.

    Extracts the three lightest distinct |eigenvalue| from the Dirac spectrum
    and computes R = (lambda_3^2 - lambda_2^2) / (lambda_2^2 - lambda_1^2).

    Returns: (R, lambda_1, lambda_2, lambda_3, n_eigenvalues)
    """
    all_evals, eval_data = collect_spectrum(
        tau_val, gens, f_abc, gammas,
        max_pq_sum=max_pq_sum, verbose=verbose
    )

    # Collect all absolute eigenvalues weighted by multiplicity
    all_abs = []
    for p, q, evals_arr in eval_data:
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        for ev in evals_arr:
            abs_ev = abs(ev)
            if abs_ev > 1e-10:  # Exclude zero modes
                all_abs.append(abs_ev)

    # Sort and get unique (within tolerance)
    all_abs = np.array(sorted(set(np.round(np.array(all_abs), 10))))
    # Get three lightest
    lightest = all_abs[:3]

    if len(lightest) < 3:
        return np.nan, np.nan, np.nan, np.nan, len(all_abs)

    l1, l2, l3 = lightest[0], lightest[1], lightest[2]
    denom = l2**2 - l1**2
    if abs(denom) < 1e-15:
        return np.nan, l1, l2, l3, len(all_abs)

    R = (l3**2 - l2**2) / denom
    return R, l1, l2, l3, len(all_abs)


# ============================================================
# MAIN COMPUTATION
# ============================================================

if __name__ == '__main__':
    print("="*60)
    print("Session 21c P0-4: Neutrino Fine-Grid R(tau)")
    print("="*60)

    # Initialize infrastructure
    print("\nInitializing SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Fine grid
    tau_fine = np.arange(1.50, 1.71, 0.02)
    print(f"\nFine grid: {len(tau_fine)} tau values from {tau_fine[0]:.2f} to {tau_fine[-1]:.2f}")

    # max_pq_sum values for convergence check
    pq_sums = [6, 7, 8]

    results = {}
    for max_pq in pq_sums:
        print(f"\n--- max_pq_sum = {max_pq} ---")
        R_vals = np.zeros(len(tau_fine))
        l1_vals = np.zeros(len(tau_fine))
        l2_vals = np.zeros(len(tau_fine))
        l3_vals = np.zeros(len(tau_fine))
        n_eigs = np.zeros(len(tau_fine), dtype=int)

        for i, tau in enumerate(tau_fine):
            t0 = time.time()
            R, l1, l2, l3, n = compute_R(tau, gens, f_abc, gammas, max_pq_sum=max_pq)
            dt = time.time() - t0
            R_vals[i] = R
            l1_vals[i] = l1
            l2_vals[i] = l2
            l3_vals[i] = l3
            n_eigs[i] = n
            print(f"  tau={tau:.2f}: R={R:.2f}, l1={l1:.6f}, l2={l2:.6f}, l3={l3:.6f}, "
                  f"n_eig={n}, time={dt:.1f}s")

        results[max_pq] = {
            'R': R_vals,
            'lambda1': l1_vals,
            'lambda2': l2_vals,
            'lambda3': l3_vals,
            'n_eigs': n_eigs,
        }

    # ============================================================
    # Constraint Gate ANALYSIS
    # ============================================================
    print("\n" + "="*60)
    print("Constraint Gate ANALYSIS")
    print("="*60)

    for max_pq in pq_sums:
        R = results[max_pq]['R']
        R_max = np.nanmax(R)
        tau_max = tau_fine[np.nanargmax(R)]
        print(f"\nmax_pq_sum = {max_pq}:")
        print(f"  R_max = {R_max:.2f} at tau = {tau_max:.2f}")
        if R_max > 32.6:
            print(f"  --> PASS: R_max > 32.6")
        elif R_max >= 30:
            print(f"  --> SOFT MISS: R_max in [30, 32.6]")
        else:
            print(f"  --> HARD CLOSED: R_max < 30")

    # Convergence check
    print("\nConvergence analysis:")
    R6 = results[6]['R']
    if 7 in results:
        R7 = results[7]['R']
        print(f"  max_pq 6->7: max |dR| = {np.nanmax(np.abs(R7 - R6)):.2f}")
    if 8 in results:
        R8 = results[8]['R']
        print(f"  max_pq 7->8: max |dR| = {np.nanmax(np.abs(R8 - results[7]['R'])):.2f}")
        print(f"  max_pq 6->8: max |dR| = {np.nanmax(np.abs(R8 - R6)):.2f}")

    # Final verdict
    converged_R = results[pq_sums[-1]]['R']
    R_final = np.nanmax(converged_R)
    tau_final = tau_fine[np.nanargmax(converged_R)]
    print(f"\nFINAL VERDICT (max_pq={pq_sums[-1]}):")
    print(f"  R_max = {R_final:.4f} at tau = {tau_final:.2f}")
    if R_final > 32.6:
        verdict = "PASS"
    elif R_final >= 30:
        verdict = "SOFT MISS"
    else:
        verdict = "HARD CLOSED"
    print(f"  --> {verdict}")
    print("="*60)

    # ============================================================
    # SAVE DATA
    # ============================================================
    save_dict = {
        'tau_fine': tau_fine,
        'pq_sums': np.array(pq_sums),
        'verdict': verdict,
        'R_final': R_final,
        'tau_R_max': tau_final,
    }
    for max_pq in pq_sums:
        for key, val in results[max_pq].items():
            save_dict[f'pq{max_pq}_{key}'] = val

    np.savez(os.path.join(SCRIPT_DIR, 's21c_neutrino_fine_grid.npz'), **save_dict)
    print(f"\nData saved to s21c_neutrino_fine_grid.npz")

    # ============================================================
    # PLOT
    # ============================================================
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Session 21c P0-4: Neutrino Fine-Grid R(tau)', fontsize=14, fontweight='bold')

    # Panel 1: R(tau) for different max_pq_sum
    ax = axes[0]
    for max_pq in pq_sums:
        ax.plot(tau_fine, results[max_pq]['R'], 'o-', label=f'max_pq={max_pq}', markersize=5)
    ax.axhline(y=32.6, color='r', linestyle='--', linewidth=2, label='Target R=32.6')
    ax.axhline(y=30, color='orange', linestyle=':', label='Hard Closure R=30')
    ax.set_xlabel('tau')
    ax.set_ylabel('R = (l3^2-l2^2)/(l2^2-l1^2)')
    ax.set_title('Neutrino Mass-Squared Ratio R(tau)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Three lightest eigenvalues
    ax = axes[1]
    max_pq = pq_sums[-1]  # Use highest convergence
    ax.plot(tau_fine, results[max_pq]['lambda1'], 'bo-', label='lambda_1', markersize=5)
    ax.plot(tau_fine, results[max_pq]['lambda2'], 'rs-', label='lambda_2', markersize=5)
    ax.plot(tau_fine, results[max_pq]['lambda3'], 'g^-', label='lambda_3', markersize=5)
    ax.set_xlabel('tau')
    ax.set_ylabel('|eigenvalue|')
    ax.set_title(f'Three Lightest Dirac Eigenvalues (max_pq={max_pq})')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: Convergence
    ax = axes[2]
    if len(pq_sums) >= 2:
        for i, max_pq in enumerate(pq_sums):
            ax.plot(tau_fine, results[max_pq]['R'], 'o-', label=f'max_pq={max_pq}', markersize=5)
    ax.axhline(y=32.6, color='r', linestyle='--', linewidth=2, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('R(tau)')
    ax.set_title('Convergence in max_pq_sum')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, 's21c_neutrino_R.png'), dpi=150, bbox_inches='tight')
    print(f"Plot saved to s21c_neutrino_R.png")
    plt.close()

    print("\n=== NEUTRINO FINE-GRID COMPUTATION COMPLETE ===")
