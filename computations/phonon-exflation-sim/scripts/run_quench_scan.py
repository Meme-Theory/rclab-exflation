"""
Quench rate scan: D/H vs Kibble-Zurek quench timescale tau_Q.

In the BKT/KZM picture, the defect density and pair fraction are determined
by the quench dynamics, not the subsequent expansion. This scan identifies
how the quench rate controls D/H and finds the regime approaching 10^-5.

Physics:
- Fast quench (small tau_Q) -> many defects, short correlation -> more close pairs -> higher D/H
- Slow quench (large tau_Q) -> fewer defects, long correlation -> fewer close pairs -> lower D/H
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


def run_quench_scan(gamma0=0.0, R_freeze=None, freeze_mode='boltzmann',
                    soft_pairing=False):
    print("=" * 70)
    print("QUENCH RATE SCAN: D/H vs tau_Q (Kibble-Zurek)")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    N, L, dt = 256, 64.0, 0.005
    g0, n0 = 1.0, 1.0
    tau_exp, alpha = 2.0, 0.667
    n_expand = 6000
    n_heal = 150

    # Scan quench timescale: fast to slow
    tau_Q_values = [5.0, 10.0, 20.0, 50.0, 100.0, 200.0]
    d_pair_factors = [1.0, 1.5, 2.0]

    xi0 = 1.0 / np.sqrt(g0 * n0)
    dx = L / N

    results = []
    total_runs = len(tau_Q_values) * len(d_pair_factors)
    run_idx = 0

    print(f"\n  Grid: {N}x{N}, L={L}")
    print(f"  Expansion: tau_exp={tau_exp}, alpha={alpha}, gamma0={gamma0}, {n_expand} steps")
    if R_freeze is not None:
        print(f"  Freeze-out: R_freeze={R_freeze}, mode={freeze_mode}")
    if soft_pairing:
        print(f"  Soft pairing: enabled")
    print(f"  tau_Q values: {tau_Q_values}")
    print(f"  d_pair_factor values: {d_pair_factors}")
    print(f"  Total runs: {total_runs}\n")

    for d_pair_factor in d_pair_factors:
        d_pair_grid = d_pair_factor * xi0 / dx
        print(f"\n  --- d_pair_factor = {d_pair_factor} ({d_pair_grid:.1f} grid pts) ---")

        for tau_Q in tau_Q_values:
            run_idx += 1
            synchronize()
            t0 = time.time()

            # Scale quench steps with tau_Q, cap at 2000 for tractability
            n_quench = min(max(int(tau_Q / dt), 200), 2000)

            solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
            expansion = ExpansionLaw(
                tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0,
                R_freeze=R_freeze, freeze_mode=freeze_mode,
            )

            kibble_zurek_quench(solver, tau_Q=tau_Q, n_quench_steps=n_quench, seed=42)
            heal_wavefunction(solver, n_steps=n_heal)

            # Pre-expansion census
            census_pre = run_census(solver.psi, d_pair_grid, L=N,
                                    soft_pairing=soft_pairing, n0=n0,
                                    xi=xi0/dx, H=0.0)

            # Expansion
            solver.time = 0.0
            for step in range(1, n_expand + 1):
                g = expansion.g_eff(solver.time)
                mu = expansion.mu_eff(solver.time)
                gamma = expansion.gamma_eff(solver.time)
                solver.step_real_time(g=g, mu=mu, gamma=gamma)

            # Post-expansion census
            R_final = expansion.scale_factor(solver.time)
            xi_t = expansion.healing_length(solver.time)
            H_t = expansion.hubble_rate(solver.time)
            census_post = run_census(solver.psi, d_pair_grid, L=N,
                                     soft_pairing=soft_pairing, n0=n0,
                                     xi=xi_t/dx, H=H_t*dx)
            synchronize()
            elapsed = time.time() - t0

            result = {
                'tau_Q': tau_Q,
                'd_pair_factor': d_pair_factor,
                'n_quench_steps': n_quench,
                'R_final': float(R_final),
                'pre_n_total': census_pre['n_total'],
                'pre_n_pair': census_pre['n_pair'],
                'pre_n_free': census_pre['n_free'],
                'pre_dh': float(census_pre['d_over_h']) if census_pre['d_over_h'] != float('inf') else -1,
                'post_n_total': census_post['n_total'],
                'post_n_pair': census_post['n_pair'],
                'post_n_free': census_post['n_free'],
                'post_dh': float(census_post['d_over_h']) if census_post['d_over_h'] != float('inf') else -1,
            }
            results.append(result)

            pre_dh_str = f"{result['pre_dh']:.4e}" if result['pre_dh'] >= 0 else "inf"
            post_dh_str = f"{result['post_dh']:.4e}" if result['post_dh'] >= 0 else "inf"

            print(f"  [{run_idx:3d}/{total_runs}] tau_Q={tau_Q:7.1f} | "
                  f"pre: v={result['pre_n_total']:3d} p={result['pre_n_pair']:2d} D/H={pre_dh_str} | "
                  f"post: v={result['post_n_total']:3d} p={result['post_n_pair']:2d} D/H={post_dh_str} | "
                  f"R={R_final:.2f} ({elapsed:.1f}s)")

    # Analysis
    print(f"\n{'=' * 70}")
    print("QUENCH RATE SCALING ANALYSIS")
    print(f"{'=' * 70}")

    for dpf in d_pair_factors:
        subset = [r for r in results if r['d_pair_factor'] == dpf]
        taus = np.array([r['tau_Q'] for r in subset])
        pre_dhs = np.array([r['pre_dh'] for r in subset])

        print(f"\n  d_pair_factor = {dpf}:")
        print(f"  {'tau_Q':>8s}  {'pre_D/H':>12s}  {'post_D/H':>12s}  {'N_vort_pre':>10s}  {'N_vort_post':>11s}")
        for r in subset:
            print(f"  {r['tau_Q']:8.1f}  {r['pre_dh']:12.4e}  {r['post_dh']:12.4e}  "
                  f"{r['pre_n_total']:10d}  {r['post_n_total']:11d}")

        # Power law fit for pre-expansion D/H vs tau_Q
        valid = pre_dhs > 0
        if np.sum(valid) >= 3:
            log_tau = np.log10(taus[valid])
            log_dh = np.log10(pre_dhs[valid])
            coeffs = np.polyfit(log_tau, log_dh, 1)
            print(f"  Pre-expansion fit: D/H ~ tau_Q^({coeffs[0]:.3f})")
            tau_target = 10**((-4.597 - coeffs[1]) / coeffs[0])
            print(f"  For D/H = 2.527e-5: tau_Q ~ {tau_target:.1f}")

    # Save
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'quench_scan_results.json')
    with open(outfile, 'w') as f:
        json.dump({'results': results, 'backend': BACKEND_NAME}, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")


if __name__ == '__main__':
    run_quench_scan()
