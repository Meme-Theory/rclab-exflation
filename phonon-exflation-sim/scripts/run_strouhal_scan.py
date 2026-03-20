"""
Strouhal Number Scan: Primary production script for Phase 2.

Sweeps St = (c_s/xi) * tau_exp = g0*n0*tau_exp to find the (St, R_freeze)
combination where D/H approaches the BBN target of 2.527e-5.

Primary scan axis: tau_exp (controls St at fixed g0, n0)
Secondary scan axis: R_freeze (controls freeze-out scale factor)

Uses:
  - 1024x1024 grid (~5,000 vortices)
  - Boltzmann freeze-out + soft pairing
  - 10 ensemble realizations per point
"""

import sys
import os
import time
import json
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.backend import BACKEND_NAME, synchronize
from src.gpe_solver import GPESolver2D
from src.expansion import ExpansionLaw
from src.initial_conditions import kibble_zurek_quench, heal_wavefunction
from src.vortex_detection import detect_vortices
from src.defect_census import run_census


def run_one_point(tau_exp, R_freeze, seed,
                  N=1024, g0=1.0, n0=1.0, alpha=0.667,
                  gamma0=0.01, freeze_mode='boltzmann',
                  dt=0.005, tau_Q=50.0, n_heal=150,
                  n_expand=20000, d_pair_factor=1.5,
                  soft_pairing=True):
    """Run a single (tau_exp, R_freeze) point with one seed."""
    L = 64.0 * (N / 256)
    dx = L / N
    xi0 = 1.0 / np.sqrt(g0 * n0)
    d_pair_grid = d_pair_factor * xi0 / dx

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0,
        R_freeze=R_freeze, freeze_mode=freeze_mode,
    )

    # IC: Kibble-Zurek quench
    kibble_zurek_quench(solver, tau_Q=tau_Q, seed=seed)
    if n_heal > 0:
        heal_wavefunction(solver, n_steps=n_heal)

    v0, _ = detect_vortices(solver.psi)
    n_vortex_init = len(v0)

    # Expansion evolution
    solver.time = 0.0
    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

    # Final census
    xi_t = expansion.healing_length(solver.time)
    H_t = expansion.hubble_rate(solver.time)
    census = run_census(solver.psi, d_pair_grid, L=N,
                        soft_pairing=soft_pairing, n0=n0,
                        xi=xi_t/dx, H=H_t*dx)

    R_final = expansion.scale_factor(solver.time)
    St = expansion.strouhal_number(0.0)

    return {
        'seed': seed,
        'tau_exp': tau_exp,
        'R_freeze': R_freeze,
        'St': float(St),
        'R_final': float(R_final),
        'n_vortex_init': n_vortex_init,
        'n_total': census['n_total'],
        'n_pair': census['n_pair'],
        'n_free': census['n_free'],
        'n_triple': census['n_triple'],
        'n_quad': census['n_quad'],
        'n_complex': census['n_complex'],
        'd_over_h': float(census['d_over_h']) if census['d_over_h'] != float('inf') else -1,
        'weighted_pairs': float(census.get('weighted_pairs', census['n_pair'])),
    }


def run_strouhal_scan(
    N=1024,
    n_realizations=10,
    tau_exp_values=None,
    R_freeze_values=None,
    n_expand=20000,
    gamma0=0.01,
    soft_pairing=True,
    freeze_mode='boltzmann',
):
    """Sweep Strouhal number (via tau_exp) and R_freeze."""
    if tau_exp_values is None:
        tau_exp_values = np.logspace(np.log10(0.5), np.log10(500), 20).tolist()
    if R_freeze_values is None:
        R_freeze_values = [2.0, 5.0, 10.0, 20.0, 50.0]

    print("=" * 80)
    print("STROUHAL NUMBER SCAN: D/H vs St (Production)")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 80)
    print(f"\n  Grid: {N}x{N}")
    print(f"  Soft pairing: {soft_pairing}")
    print(f"  Freeze mode: {freeze_mode}")
    print(f"  gamma0: {gamma0}")
    print(f"  n_expand: {n_expand}")
    print(f"  tau_exp values ({len(tau_exp_values)}): {[f'{v:.2f}' for v in tau_exp_values]}")
    print(f"  R_freeze values: {R_freeze_values}")
    print(f"  Realizations per point: {n_realizations}")

    total_points = len(tau_exp_values) * len(R_freeze_values)
    total_runs = total_points * n_realizations
    print(f"  Total grid points: {total_points}")
    print(f"  Total simulation runs: {total_runs}")

    all_results = []
    summary = []
    run_idx = 0

    synchronize()
    t_scan_start = time.time()

    for R_freeze in R_freeze_values:
        print(f"\n{'='*80}")
        print(f"  R_freeze = {R_freeze}")
        print(f"{'='*80}")

        for tau_exp in tau_exp_values:
            point_results = []
            synchronize()
            t_point_start = time.time()

            for r in range(n_realizations):
                seed = 1000 + r * 17
                run_idx += 1

                result = run_one_point(
                    tau_exp=tau_exp, R_freeze=R_freeze, seed=seed,
                    N=N, gamma0=gamma0, freeze_mode=freeze_mode,
                    n_expand=n_expand, soft_pairing=soft_pairing,
                )
                point_results.append(result)
                all_results.append(result)

            synchronize()
            t_point = time.time() - t_point_start

            # Aggregate across realizations
            dh_vals = [r['d_over_h'] for r in point_results if r['d_over_h'] >= 0]
            n_pair_total = sum(r['n_pair'] for r in point_results)
            n_free_total = sum(r['n_free'] for r in point_results)
            agg_dh = n_pair_total / n_free_total if n_free_total > 0 else float('inf')
            St = point_results[0]['St']

            point_summary = {
                'tau_exp': tau_exp,
                'R_freeze': R_freeze,
                'St': St,
                'mean_dh': float(np.mean(dh_vals)) if dh_vals else -1,
                'std_dh': float(np.std(dh_vals)) if dh_vals else -1,
                'aggregate_dh': float(agg_dh) if agg_dh != float('inf') else -1,
                'mean_n_total': float(np.mean([r['n_total'] for r in point_results])),
                'mean_n_pair': float(np.mean([r['n_pair'] for r in point_results])),
                'mean_n_free': float(np.mean([r['n_free'] for r in point_results])),
                'mean_n_complex': float(np.mean([r['n_complex'] for r in point_results])),
            }
            summary.append(point_summary)

            log_dh = np.log10(point_summary['aggregate_dh']) if point_summary['aggregate_dh'] > 0 else float('nan')

            print(f"  [{run_idx:4d}/{total_runs}] tau_exp={tau_exp:8.2f} St={St:8.1f} | "
                  f"D/H={point_summary['aggregate_dh']:.4e} (log={log_dh:+.2f}) | "
                  f"v={point_summary['mean_n_total']:.0f} "
                  f"p={point_summary['mean_n_pair']:.1f} "
                  f"Li7={point_summary['mean_n_complex']:.1f} | "
                  f"{t_point:.1f}s")

    synchronize()
    t_scan_total = time.time() - t_scan_start

    # Summary table
    print(f"\n{'='*80}")
    print(f"STROUHAL SCAN RESULTS ({t_scan_total:.0f}s total)")
    print(f"{'='*80}")
    print(f"\n{'R_freeze':>8s}  {'tau_exp':>8s}  {'St':>10s}  {'D/H_agg':>12s}  "
          f"{'log10(D/H)':>10s}  {'N_vort':>6s}  {'N_pair':>6s}  {'Li7':>4s}")
    print("-" * 85)

    for s in summary:
        log_dh = np.log10(s['aggregate_dh']) if s['aggregate_dh'] > 0 else float('nan')
        print(f"{s['R_freeze']:8.1f}  {s['tau_exp']:8.2f}  {s['St']:10.1f}  "
              f"{s['aggregate_dh']:12.4e}  {log_dh:10.4f}  "
              f"{s['mean_n_total']:6.0f}  {s['mean_n_pair']:6.1f}  "
              f"{s['mean_n_complex']:4.1f}")

    # Find best point
    valid_summary = [s for s in summary if s['aggregate_dh'] > 0]
    if valid_summary:
        target_log = np.log10(2.527e-5)
        best = min(valid_summary, key=lambda s: abs(np.log10(s['aggregate_dh']) - target_log))
        print(f"\n  Closest to target D/H = 2.527e-5:")
        print(f"    tau_exp = {best['tau_exp']:.2f}, R_freeze = {best['R_freeze']:.1f}")
        print(f"    St = {best['St']:.1f}")
        print(f"    D/H = {best['aggregate_dh']:.4e} (target: 2.527e-5)")
        print(f"    log10 gap: {np.log10(best['aggregate_dh']) - target_log:+.3f} decades")

    # Save results
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'strouhal_scan_results.json')

    output = {
        'config': {
            'N': N, 'n_realizations': n_realizations,
            'gamma0': gamma0, 'freeze_mode': freeze_mode,
            'soft_pairing': soft_pairing,
            'n_expand': n_expand,
            'tau_exp_values': tau_exp_values,
            'R_freeze_values': R_freeze_values,
            'backend': BACKEND_NAME,
        },
        'summary': summary,
        'all_results': all_results,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return summary, all_results


if __name__ == '__main__':
    summary, all_results = run_strouhal_scan()
