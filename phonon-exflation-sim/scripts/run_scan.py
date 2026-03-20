"""
Parameter scan: sweep tau_exp and alpha to characterize D/H dependence.

Systematically vary expansion parameters and measure the bound-pair fraction
to identify scaling laws and the regime approaching D/H ~ 10^-5.
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.backend import BACKEND_NAME, synchronize
from src.gpe_solver import GPESolver2D
from src.expansion import ExpansionLaw
from src.initial_conditions import random_phase_ic, heal_wavefunction
from src.defect_census import run_census


def run_single(tau_exp, alpha, seed=42, N=256, L=None, dt=0.005,
               g0=1.0, n0=1.0, n_heal=500, n_expand=6000, d_pair_factor=2.5,
               gamma0=0.0, R_freeze=None, freeze_mode='boltzmann',
               soft_pairing=False):
    """Run a single simulation and return final census."""
    if L is None:
        L = 64.0 * (N / 256)

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0,
        R_freeze=R_freeze, freeze_mode=freeze_mode,
    )

    xi0 = 1.0 / np.sqrt(g0 * n0)
    dx = L / N
    d_pair_grid = d_pair_factor * xi0 / dx
    L_grid = N

    random_phase_ic(solver, seed=seed)
    heal_wavefunction(solver, n_steps=n_heal)

    solver.time = 0.0

    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

    xi_t = expansion.healing_length(solver.time)
    H_t = expansion.hubble_rate(solver.time)
    census = run_census(solver.psi, d_pair_grid, L=L_grid,
                        soft_pairing=soft_pairing, n0=n0,
                        xi=xi_t/dx, H=H_t*dx)
    R_final = expansion.scale_factor(solver.time)
    St = expansion.strouhal_number(0.0)

    return {
        'tau_exp': tau_exp,
        'alpha': alpha,
        'R_final': R_final,
        'St': St,
        **{k: v for k, v in census.items()
           if k not in ('vortex_positions', 'pairs', 'clusters', 'pair_weights')},
    }


def run_parameter_scan(**kwargs):
    """Scan over tau_exp and alpha to map D/H dependence."""
    print("=" * 70)
    print("PARAMETER SCAN: D/H vs Expansion Parameters")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    # Scan variables
    tau_exp_values = [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]
    alpha_values = [0.3, 0.5, 0.667, 0.8, 1.0]

    results = []
    total_runs = len(tau_exp_values) * len(alpha_values)
    run_idx = 0

    print(f"\nTotal runs: {total_runs}")
    print(f"tau_exp values: {tau_exp_values}")
    print(f"alpha values: {alpha_values}")
    print()

    for alpha in alpha_values:
        for tau_exp in tau_exp_values:
            run_idx += 1
            synchronize()
            t0 = time.time()
            result = run_single(tau_exp=tau_exp, alpha=alpha, **kwargs)
            synchronize()
            elapsed = time.time() - t0

            results.append(result)
            print(f"  [{run_idx:3d}/{total_runs}] tau_exp={tau_exp:6.1f} alpha={alpha:.3f} "
                  f"R={result['R_final']:6.2f} St={result['St']:8.1f} "
                  f"vortices={result['n_total']:4d} pairs={result['n_pair']:3d} "
                  f"free={result['n_free']:4d} D/H={result['d_over_h']:.4e} "
                  f"({elapsed:.1f}s)")

    # Summary table
    print(f"\n{'=' * 70}")
    print("SUMMARY TABLE")
    print(f"{'=' * 70}")
    print(f"{'tau_exp':>8s} {'alpha':>6s} {'R_final':>8s} {'St':>10s} "
          f"{'N_vort':>7s} {'N_pair':>7s} {'N_free':>7s} {'D/H':>12s} {'log10(D/H)':>12s}")
    print("-" * 90)

    for r in results:
        log_dh = np.log10(r['d_over_h']) if r['d_over_h'] > 0 and r['d_over_h'] != float('inf') else float('nan')
        print(f"{r['tau_exp']:8.1f} {r['alpha']:6.3f} {r['R_final']:8.3f} {r['St']:10.1f} "
              f"{r['n_total']:7d} {r['n_pair']:7d} {r['n_free']:7d} "
              f"{r['d_over_h']:12.4e} {log_dh:12.4f}")

    # Analyze scaling
    print(f"\n{'=' * 70}")
    print("SCALING ANALYSIS")
    print(f"{'=' * 70}")

    # Fix alpha=0.667 and fit D/H vs tau_exp
    alpha_ref = 0.667
    ref_results = [r for r in results if abs(r['alpha'] - alpha_ref) < 0.01]

    if len(ref_results) >= 3:
        tau_vals = np.array([r['tau_exp'] for r in ref_results])
        dh_vals = np.array([r['d_over_h'] for r in ref_results])
        valid = (dh_vals > 0) & (dh_vals < float('inf'))

        if np.sum(valid) >= 3:
            log_tau = np.log10(tau_vals[valid])
            log_dh = np.log10(dh_vals[valid])

            coeffs = np.polyfit(log_tau, log_dh, 1)
            print(f"\n  At alpha={alpha_ref}:")
            print(f"  Power law fit: D/H ~ tau_exp^({coeffs[0]:.3f})")
            print(f"  Intercept: {10**coeffs[1]:.4e}")
            print(f"  For D/H = 2.527e-5: tau_exp ~ {10**((-5 - np.log10(2.527) - coeffs[1]) / coeffs[0]):.1f}")

    # Fix tau_exp=5 and fit D/H vs alpha
    tau_ref = 5.0
    ref_results2 = [r for r in results if abs(r['tau_exp'] - tau_ref) < 0.1]
    if len(ref_results2) >= 3:
        alpha_vals = np.array([r['alpha'] for r in ref_results2])
        dh_vals = np.array([r['d_over_h'] for r in ref_results2])
        valid = (dh_vals > 0) & (dh_vals < float('inf'))

        if np.sum(valid) >= 3:
            coeffs2 = np.polyfit(alpha_vals[valid], np.log10(dh_vals[valid]), 1)
            print(f"\n  At tau_exp={tau_ref}:")
            print(f"  Exponential fit: log10(D/H) ~ {coeffs2[0]:.3f} * alpha + {coeffs2[1]:.3f}")

    print(f"\n{'=' * 70}")
    print("SCAN COMPLETE")
    print(f"{'=' * 70}")

    return results


if __name__ == '__main__':
    results = run_parameter_scan()
