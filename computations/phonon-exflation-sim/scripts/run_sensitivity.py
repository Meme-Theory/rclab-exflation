"""
Phase 2B.2: Parameter sensitivity scan.

For each of the 4 free parameters (tau_exp, gamma0, R_freeze, tau_Q),
vary by factors of ~2 while holding the others at breakthrough values.
Each parameter point is averaged over multiple seeds to avoid seed-specific
artifacts.

Pass criterion: D/H varies < 1 OOM for 2x parameter change.
Fail criterion: D/H changes > 2 OOM for 2x parameter change (fine-tuned).

Hidden parameters documented:
  - Sigmoid width in Boltzmann freeze-out: dR = 0.1 * R_freeze (hardcoded in expansion.py)
  - IC healing steps: 150 (post-quench imaginary-time relaxation)
  - Pair regularization: d_min = 0.5 grid units (in vortex_detection.py identify_pairs)
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


# Breakthrough parameter defaults
BREAKTHROUGH = {
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
    'd_pair_factor': 1.5,
    'soft_pairing': True,
}

# Seeds for multi-realization averaging (3 per point for tractability)
SEEDS = [42, 137, 271]

# Parameter scan grids
# R_freeze lower bound extended to 1.5 to capture naive self-consistent estimate (~1.73)
SCAN_PARAMS = {
    'tau_exp': [1.0, 1.5, 2.0, 3.0, 4.0],
    'gamma0': [0.05, 0.075, 0.1, 0.15, 0.2],
    'R_freeze': [1.5, 2.0, 2.5, 3.0, 4.0, 5.0],
    'tau_Q': [25.0, 50.0, 100.0, 200.0],
}


def run_single_point(params, seed):
    """Run a single simulation with given params and seed, return census result."""
    N = params['N']
    L = 64.0 * (N / 256)
    dt = params['dt']
    g0, n0 = params['g0'], params['n0']

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=params['tau_exp'], alpha=params['alpha'],
        g0=g0, n0=n0, gamma0=params['gamma0'],
        R_freeze=params['R_freeze'], freeze_mode=params['freeze_mode'],
    )
    dx = L / N
    xi0 = 1.0 / np.sqrt(g0 * n0)
    d_pair_grid = params['d_pair_factor'] * xi0 / dx

    kibble_zurek_quench(solver, tau_Q=params['tau_Q'],
                        n_quench_steps=params['n_quench'], seed=seed)
    if params['n_heal'] > 0:
        heal_wavefunction(solver, n_steps=params['n_heal'])

    v0, _ = detect_vortices(solver.psi)
    n_vortex_init = len(v0)

    solver.time = 0.0
    n_expand = params['n_expand']
    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

    R_final = expansion.scale_factor(solver.time)
    xi_t = expansion.healing_length(solver.time)
    H_t = expansion.hubble_rate(solver.time)
    census = run_census(solver.psi, d_pair_grid, L=N,
                        soft_pairing=params['soft_pairing'], n0=n0,
                        xi=xi_t/dx, H=H_t*dx)

    dh = float(census['d_over_h']) if census['d_over_h'] != float('inf') else -1.0

    return {
        'seed': seed,
        'n_vortex_init': n_vortex_init,
        'n_total': census['n_total'],
        'n_pair': census['n_pair'],
        'n_free': census['n_free'],
        'd_over_h': dh,
        'R_final': float(R_final),
        'weighted_pairs': float(census.get('weighted_pairs', 0)),
    }


def run_sensitivity_scan(seeds=None):
    """Scan each of 4 free parameters while holding others at breakthrough values.

    Each parameter point is run with multiple seeds and the mean D/H is reported.
    """
    if seeds is None:
        seeds = SEEDS

    n_seeds = len(seeds)

    print("=" * 70)
    print("PHASE 2B.2: PARAMETER SENSITIVITY SCAN")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    print(f"\n  Breakthrough parameters:")
    for k, v in BREAKTHROUGH.items():
        print(f"    {k}: {v}")

    print(f"\n  Seeds per point: {seeds} ({n_seeds} realizations)")

    print(f"\n  Scan grids:")
    for param, values in SCAN_PARAMS.items():
        bt_val = BREAKTHROUGH[param]
        print(f"    {param}: {values}  (breakthrough = {bt_val})")

    total_points = sum(len(v) for v in SCAN_PARAMS.values())
    total_runs = total_points * n_seeds
    print(f"\n  Total parameter points: {total_points}")
    print(f"  Total simulation runs: {total_runs}")

    all_results = {}
    run_idx = 0
    t_total_start = time.time()

    for param_name, scan_values in SCAN_PARAMS.items():
        print(f"\n{'=' * 60}")
        print(f"  Scanning: {param_name}")
        print(f"{'=' * 60}")

        param_results = []
        for val in scan_values:
            params = dict(BREAKTHROUGH)
            params[param_name] = val

            is_breakthrough = (val == BREAKTHROUGH[param_name])
            marker = " <-- breakthrough" if is_breakthrough else ""

            seed_results = []
            synchronize()
            t0 = time.time()
            for seed in seeds:
                run_idx += 1
                result = run_single_point(params, seed)
                seed_results.append(result)
            synchronize()
            elapsed = time.time() - t0

            # Compute mean D/H across seeds
            valid_dh = [r['d_over_h'] for r in seed_results if r['d_over_h'] > 0]
            if valid_dh:
                mean_dh = float(np.mean(valid_dh))
                std_dh = float(np.std(valid_dh, ddof=1)) if len(valid_dh) > 1 else 0.0
            else:
                mean_dh = -1.0
                std_dh = 0.0

            point_result = {
                'param_name': param_name,
                'param_value': val,
                'mean_d_over_h': mean_dh,
                'std_d_over_h': std_dh,
                'n_valid_seeds': len(valid_dh),
                'per_seed': seed_results,
            }
            param_results.append(point_result)

            dh_str = f"{mean_dh:.4e}" if mean_dh > 0 else "inf"
            std_str = f"+/-{std_dh:.4e}" if std_dh > 0 else ""
            print(f"  {param_name}={val:8.3f} | "
                  f"D/H={dh_str} {std_str} "
                  f"({len(valid_dh)}/{n_seeds} valid) | "
                  f"({elapsed:.1f}s){marker}")

        all_results[param_name] = param_results

    t_total = time.time() - t_total_start

    # Sensitivity analysis
    print(f"\n{'=' * 70}")
    print(f"SENSITIVITY ANALYSIS ({total_runs} runs, {t_total:.1f}s)")
    print(f"{'=' * 70}")

    assessments = {}
    for param_name, param_results in all_results.items():
        dh_values = [r['mean_d_over_h'] for r in param_results if r['mean_d_over_h'] > 0]
        param_values = [r['param_value'] for r in param_results if r['mean_d_over_h'] > 0]

        if len(dh_values) < 2:
            print(f"\n  {param_name}: insufficient valid D/H values")
            assessments[param_name] = {'pass': False, 'reason': 'insufficient data'}
            continue

        log_dh = np.log10(dh_values)
        dh_range_oom = float(np.max(log_dh) - np.min(log_dh))

        # Find breakthrough value and compute max change for 2x parameter change
        bt_val = BREAKTHROUGH[param_name]
        bt_idx = None
        for i, r in enumerate(param_results):
            if r['param_value'] == bt_val and r['mean_d_over_h'] > 0:
                bt_idx = i
                break

        max_change_for_2x = 0.0
        if bt_idx is not None:
            bt_dh = param_results[bt_idx]['mean_d_over_h']
            if bt_dh > 0:
                bt_log = np.log10(bt_dh)
                for r in param_results:
                    if r['mean_d_over_h'] > 0 and r['param_value'] != bt_val:
                        ratio = r['param_value'] / bt_val if bt_val != 0 else float('inf')
                        if 0.5 <= ratio <= 2.0:
                            change = abs(np.log10(r['mean_d_over_h']) - bt_log)
                            max_change_for_2x = max(max_change_for_2x, change)

        pass_sensitivity = bool(max_change_for_2x < 1.0)
        fail_sensitivity = bool(max_change_for_2x > 2.0)

        assessments[param_name] = {
            'pass': pass_sensitivity,
            'fail_hard': fail_sensitivity,
            'dh_range_oom': dh_range_oom,
            'max_change_for_2x': float(max_change_for_2x),
        }

        print(f"\n  {param_name}:")
        print(f"    D/H range: {dh_range_oom:.2f} OOM across scan")
        print(f"    Max D/H change for 2x param change: {max_change_for_2x:.2f} OOM")
        print(f"    Assessment: {'PASS' if pass_sensitivity else 'FAIL'}"
              f"{'  (FINE-TUNED)' if fail_sensitivity else ''}")
        for r in param_results:
            marker = " <-- BT" if r['param_value'] == BREAKTHROUGH[param_name] else ""
            dh_str = f"{r['mean_d_over_h']:.4e}" if r['mean_d_over_h'] > 0 else "inf"
            std_str = f"+/-{r['std_d_over_h']:.1e}" if r['std_d_over_h'] > 0 else ""
            print(f"      {param_name}={r['param_value']:8.3f}  "
                  f"D/H={dh_str} {std_str}{marker}")

    # Overall assessment
    all_pass = all(a['pass'] for a in assessments.values())
    any_hard_fail = any(a.get('fail_hard', False) for a in assessments.values())

    print(f"\n{'=' * 70}")
    print(f"PHASE 2B.2 OVERALL: {'PASS' if all_pass else 'FAIL'}")
    if any_hard_fail:
        print(f"  HARD FAIL: At least one parameter is fine-tuned (> 2 OOM / 2x change)")
    print(f"{'=' * 70}")

    # Save
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'phase2b_sensitivity.json')

    # Serialize: strip per_seed detail from JSON (too large), keep summary
    serializable_results = {}
    for param_name, param_results in all_results.items():
        serializable_results[param_name] = [
            {k: v for k, v in r.items() if k != 'per_seed'}
            for r in param_results
        ]

    output = {
        'config': {
            'breakthrough': BREAKTHROUGH,
            'scan_params': {k: v for k, v in SCAN_PARAMS.items()},
            'seeds': seeds,
            'n_seeds_per_point': n_seeds,
            'backend': BACKEND_NAME,
            'hidden_params': {
                'sigmoid_width': '0.1 * R_freeze (hardcoded in expansion.py)',
                'ic_heal_steps': 150,
                'pair_regularization_d_min': '0.5 grid units (vortex_detection.py)',
            },
        },
        'results': serializable_results,
        'assessments': assessments,
        'phase2b2_pass': all_pass,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return all_results, assessments


if __name__ == '__main__':
    all_results, assessments = run_sensitivity_scan()
