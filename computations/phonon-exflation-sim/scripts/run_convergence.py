"""
Phase 2B.3: Grid convergence and time convergence test.

Grid convergence: Run at N=512, 1024, 2048 with identical physics parameters.
L scales with N: L = 64 * N/256 (keeping dx/xi constant).

Time convergence: D/H is still decreasing at t=100 (20000 steps at dt=0.005).
To assess whether the quantity being compared has stabilized, we measure
D/H at multiple time checkpoints and report the rate of change at the
comparison time.

Pass criterion: D/H change < 30% between N=1024 and N=2048.
Fail criterion: D/H changes > 1 OOM between grid sizes.
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


# Breakthrough physics parameters (grid-independent)
PHYSICS = {
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
    'd_pair_factor': 1.5,
    'soft_pairing': True,
    'seed': 42,
}

# Grid sizes to test
GRID_SIZES = [512, 1024, 2048]


def run_at_grid_size(N):
    """Run simulation at specified grid size with breakthrough physics."""
    L = 64.0 * (N / 256)
    dt = PHYSICS['dt']
    g0, n0 = PHYSICS['g0'], PHYSICS['n0']

    print(f"\n  Running N={N}, L={L:.1f}, dx={L/N:.4f}")

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=PHYSICS['tau_exp'], alpha=PHYSICS['alpha'],
        g0=g0, n0=n0, gamma0=PHYSICS['gamma0'],
        R_freeze=PHYSICS['R_freeze'], freeze_mode=PHYSICS['freeze_mode'],
    )
    dx = L / N
    xi0 = 1.0 / np.sqrt(g0 * n0)
    d_pair_grid = PHYSICS['d_pair_factor'] * xi0 / dx

    print(f"  dx/xi = {dx/xi0:.4f}, d_pair = {d_pair_grid:.2f} grid units")

    kibble_zurek_quench(solver, tau_Q=PHYSICS['tau_Q'],
                        n_quench_steps=PHYSICS['n_quench'], seed=PHYSICS['seed'])
    if PHYSICS['n_heal'] > 0:
        heal_wavefunction(solver, n_steps=PHYSICS['n_heal'])

    v0, _ = detect_vortices(solver.psi)
    n_vortex_init = len(v0)
    print(f"  Post-IC vortices: {n_vortex_init}")

    solver.time = 0.0
    n_expand = PHYSICS['n_expand']
    # Take snapshots every 2000 steps (every dt*2000 = 10 time units)
    # for time-convergence analysis
    measurement_interval = 2000
    snapshots = []

    synchronize()
    t0 = time.time()

    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

        if step % measurement_interval == 0 or step == n_expand:
            R = expansion.scale_factor(solver.time)
            xi_t = expansion.healing_length(solver.time)
            H_t = expansion.hubble_rate(solver.time)
            census = run_census(solver.psi, d_pair_grid, L=N,
                                soft_pairing=PHYSICS['soft_pairing'], n0=n0,
                                xi=xi_t/dx, H=H_t*dx)
            dh = float(census['d_over_h']) if census['d_over_h'] != float('inf') else -1
            snapshots.append({
                'step': step,
                'time': float(solver.time),
                'R': float(R),
                'n_total': census['n_total'],
                'n_pair': census['n_pair'],
                'n_free': census['n_free'],
                'd_over_h': dh,
            })
            dh_str = f"{dh:.4e}" if dh >= 0 else "inf"
            synchronize()
            elapsed_so_far = time.time() - t0
            print(f"    Step {step}/{n_expand}: R={R:.3f}, D/H={dh_str} "
                  f"({elapsed_so_far:.1f}s)")

    synchronize()
    elapsed = time.time() - t0

    final = snapshots[-1]
    return {
        'N': N,
        'L': L,
        'dx': dx,
        'dx_over_xi': dx / xi0,
        'n_vortex_init': n_vortex_init,
        'final_d_over_h': final['d_over_h'],
        'final_n_total': final['n_total'],
        'final_n_pair': final['n_pair'],
        'final_n_free': final['n_free'],
        'final_R': final['R'],
        'elapsed_s': elapsed,
        'snapshots': snapshots,
    }


def run_convergence_test():
    """Run grid convergence study and assess Phase 2B.3 criteria."""
    print("=" * 70)
    print("PHASE 2B.3: GRID CONVERGENCE TEST")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    print(f"\n  Grid sizes: {GRID_SIZES}")
    print(f"  Physics params: breakthrough values")
    for k, v in PHYSICS.items():
        print(f"    {k}: {v}")

    results = []
    for N in GRID_SIZES:
        result = run_at_grid_size(N)
        results.append(result)

    # Convergence analysis
    print(f"\n{'=' * 70}")
    print(f"CONVERGENCE ANALYSIS")
    print(f"{'=' * 70}")

    print(f"\n  {'N':>6s}  {'L':>6s}  {'dx':>8s}  {'dx/xi':>6s}  "
          f"{'D/H':>12s}  {'N_vort':>7s}  {'Time(s)':>8s}")
    print(f"  {'-' * 70}")
    for r in results:
        dh_str = f"{r['final_d_over_h']:.4e}" if r['final_d_over_h'] >= 0 else "inf"
        print(f"  {r['N']:6d}  {r['L']:6.1f}  {r['dx']:8.4f}  {r['dx_over_xi']:6.4f}  "
              f"{dh_str:>12s}  {r['final_n_total']:7d}  {r['elapsed_s']:8.1f}")

    # Relative changes between successive grid sizes
    print(f"\n  Relative D/H changes between grid levels:")
    pass_1024_2048 = True
    fail_1oom = False

    for i in range(1, len(results)):
        r_prev = results[i - 1]
        r_curr = results[i]
        dh_prev = r_prev['final_d_over_h']
        dh_curr = r_curr['final_d_over_h']

        if dh_prev > 0 and dh_curr > 0:
            rel_change = abs(dh_curr - dh_prev) / dh_prev
            oom_change = abs(np.log10(dh_curr) - np.log10(dh_prev))

            print(f"    N={r_prev['N']} -> N={r_curr['N']}: "
                  f"relative change = {rel_change:.2%}, "
                  f"OOM change = {oom_change:.3f}")

            if r_prev['N'] == 1024 and r_curr['N'] == 2048:
                pass_1024_2048 = rel_change < 0.30
                print(f"    Pass criterion (< 30%): {'PASS' if pass_1024_2048 else 'FAIL'}")

            if oom_change > 1.0:
                fail_1oom = True
                print(f"    Fail criterion (> 1 OOM): FAIL")
        else:
            print(f"    N={r_prev['N']} -> N={r_curr['N']}: "
                  f"invalid D/H values, cannot assess")

    # Time-convergence analysis: is D/H still changing rapidly at the comparison time?
    print(f"\n  Time convergence (D/H evolution at each grid size):")
    time_convergence_ok = True
    for r in results:
        snaps = r['snapshots']
        if len(snaps) >= 3:
            # Look at last 3 snapshots
            recent = snaps[-3:]
            times = [s['time'] for s in recent]
            dhs = [s['d_over_h'] for s in recent]
            valid = [d for d in dhs if d > 0]
            if len(valid) >= 2:
                # Relative change over last two intervals
                rel_changes = []
                for i in range(1, len(valid)):
                    rc = abs(valid[i] - valid[i-1]) / valid[i-1]
                    rel_changes.append(rc)
                max_recent_change = max(rel_changes) if rel_changes else 0.0
                print(f"    N={r['N']}: last 3 D/H = "
                      f"{[f'{d:.3e}' for d in dhs[-3:]]}, "
                      f"max recent change = {max_recent_change:.1%}")
                if max_recent_change > 0.50:
                    print(f"    WARNING: D/H still changing > 50% between measurements")
                    time_convergence_ok = False
            else:
                print(f"    N={r['N']}: insufficient valid D/H snapshots")
        else:
            print(f"    N={r['N']}: insufficient snapshots for time convergence")

    if not time_convergence_ok:
        print(f"\n  WARNING: D/H has NOT time-converged at the comparison time.")
        print(f"  Grid convergence comparison is of a still-evolving quantity.")
        print(f"  Consider extending n_expand or comparing at matched R values.")

    overall = pass_1024_2048 and not fail_1oom
    print(f"\n{'=' * 70}")
    print(f"PHASE 2B.3 GRID CONVERGENCE: {'PASS' if overall else 'FAIL'}")
    print(f"PHASE 2B.3 TIME CONVERGENCE: {'OK' if time_convergence_ok else 'WARNING'}")
    print(f"{'=' * 70}")

    # Save
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'phase2b_convergence.json')

    output = {
        'config': {
            'grid_sizes': GRID_SIZES,
            'physics': PHYSICS,
            'backend': BACKEND_NAME,
        },
        'results': results,
        'phase2b3_pass': overall,
        'pass_1024_2048': pass_1024_2048,
        'fail_1oom': fail_1oom,
        'time_convergence_ok': time_convergence_ok,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return results, overall


if __name__ == '__main__':
    results, passed = run_convergence_test()
