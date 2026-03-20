"""
Phase 2B.6: Measurement parameter sensitivity (d_pair_factor scan).

Scan d_pair_factor in [1.0, 1.25, 1.5, 1.75, 2.0, 2.5] with all
physics at breakthrough values.

D/H should change smoothly (not discontinuously) as d_pair_factor varies.
This establishes that the result is not an artifact of the pairing definition.
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


# d_pair_factor values to scan
DPAIR_VALUES = [1.0, 1.25, 1.5, 1.75, 2.0, 2.5]

# Breakthrough physics
PHYSICS = {
    'N': 1024,
    'dt': 0.005,
    'g0': 1.0,
    'n0': 1.0,
    'tau_exp': 2.0,
    'alpha': 0.667,
    'gamma0': 0.1,
    'R_freeze': 3.0,
    'freeze_mode': 'boltzmann',
    'tau_Q': 50.0,
    'n_quench': 1000,
    'n_heal': 150,
    'n_expand': 20000,
    'soft_pairing': True,
    'seed': 42,
}


def run_dpair_sensitivity():
    """Run a SINGLE simulation, then re-analyze with different d_pair_factor values.

    The wavefunction evolution is independent of d_pair_factor (it only affects
    post-hoc analysis), so we only need to evolve once and then re-run the
    census at different pairing distances.
    """
    print("=" * 70)
    print("PHASE 2B.6: MEASUREMENT PARAMETER SENSITIVITY (d_pair_factor)")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    N = PHYSICS['N']
    L = 64.0 * (N / 256)
    dt = PHYSICS['dt']
    g0, n0 = PHYSICS['g0'], PHYSICS['n0']

    print(f"\n  Grid: {N}x{N}, L={L:.1f}")
    print(f"  d_pair_factor values: {DPAIR_VALUES}")
    print(f"  Strategy: evolve once, re-analyze with different d_pair_factor")

    # Evolve simulation once
    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=PHYSICS['tau_exp'], alpha=PHYSICS['alpha'],
        g0=g0, n0=n0, gamma0=PHYSICS['gamma0'],
        R_freeze=PHYSICS['R_freeze'], freeze_mode=PHYSICS['freeze_mode'],
    )
    dx = L / N
    xi0 = 1.0 / np.sqrt(g0 * n0)

    print(f"\n  Evolving wavefunction...")
    kibble_zurek_quench(solver, tau_Q=PHYSICS['tau_Q'],
                        n_quench_steps=PHYSICS['n_quench'], seed=PHYSICS['seed'])
    if PHYSICS['n_heal'] > 0:
        heal_wavefunction(solver, n_steps=PHYSICS['n_heal'])

    v0, _ = detect_vortices(solver.psi)
    n_vortex_init = len(v0)
    print(f"  Post-IC vortices: {n_vortex_init}")

    solver.time = 0.0
    n_expand = PHYSICS['n_expand']
    synchronize()
    t0 = time.time()

    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

    synchronize()
    elapsed_evolve = time.time() - t0
    R_final = expansion.scale_factor(solver.time)
    xi_t = expansion.healing_length(solver.time)
    H_t = expansion.hubble_rate(solver.time)

    print(f"  Evolution complete: R={R_final:.2f}, {elapsed_evolve:.1f}s")

    # Re-analyze with different d_pair_factor values
    print(f"\n  Re-analyzing with different d_pair_factor values:")
    results = []

    for dpf in DPAIR_VALUES:
        d_pair_grid = dpf * xi0 / dx

        census = run_census(solver.psi, d_pair_grid, L=N,
                            soft_pairing=PHYSICS['soft_pairing'], n0=n0,
                            xi=xi_t/dx, H=H_t*dx)

        dh = float(census['d_over_h']) if census['d_over_h'] != float('inf') else -1
        wp = float(census.get('weighted_pairs', 0))
        is_bt = (dpf == 1.5)
        marker = " <-- breakthrough" if is_bt else ""

        result = {
            'd_pair_factor': dpf,
            'd_pair_grid': float(d_pair_grid),
            'n_pair': census['n_pair'],
            'n_free': census['n_free'],
            'n_total': census['n_total'],
            'd_over_h': dh,
            'weighted_pairs': wp,
        }
        results.append(result)

        dh_str = f"{dh:.4e}" if dh >= 0 else "inf"
        print(f"    d_pair_factor={dpf:5.2f}  d_pair={d_pair_grid:6.2f}  "
              f"pairs={census['n_pair']:3d}  free={census['n_free']:4d}  "
              f"D/H={dh_str}  wp={wp:.3f}{marker}")

    # Smoothness analysis
    print(f"\n{'=' * 70}")
    print(f"SMOOTHNESS ANALYSIS")
    print(f"{'=' * 70}")

    dh_values = [r['d_over_h'] for r in results if r['d_over_h'] > 0]
    dpf_values = [r['d_pair_factor'] for r in results if r['d_over_h'] > 0]

    if len(dh_values) >= 2:
        log_dh = np.log10(dh_values)

        # Check for discontinuous jumps (> 0.5 OOM between adjacent scan points)
        jumps = np.abs(np.diff(log_dh))
        max_jump = float(np.max(jumps))
        smooth = max_jump < 0.5  # less than 0.5 OOM per step

        print(f"  D/H values: {[f'{d:.4e}' for d in dh_values]}")
        print(f"  log10(D/H) steps: {[f'{j:.3f}' for j in jumps]}")
        print(f"  Max step: {max_jump:.3f} OOM")
        print(f"  Smooth (max step < 0.5 OOM): {'YES' if smooth else 'NO'}")

        # Monotonicity: D/H should generally increase with d_pair_factor
        # (more pairs found at larger pairing distance)
        n_increasing = int(np.sum(np.diff(dh_values) > 0))
        n_decreasing = int(np.sum(np.diff(dh_values) < 0))
        print(f"  Monotonicity: {n_increasing} increasing, {n_decreasing} decreasing steps")
    else:
        smooth = False
        print(f"  Insufficient valid D/H values for smoothness analysis")

    overall = smooth
    print(f"\n{'=' * 70}")
    print(f"PHASE 2B.6 OVERALL: {'PASS' if overall else 'FAIL'}")
    print(f"{'=' * 70}")

    # Save
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'phase2b_dpair_sensitivity.json')

    output = {
        'config': {
            'dpair_values': DPAIR_VALUES,
            'physics': PHYSICS,
            'backend': BACKEND_NAME,
        },
        'evolution': {
            'n_vortex_init': n_vortex_init,
            'R_final': float(R_final),
            'elapsed_s': elapsed_evolve,
        },
        'results': results,
        'smooth': smooth,
        'phase2b6_pass': overall,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return results, overall


if __name__ == '__main__':
    results, passed = run_dpair_sensitivity()
