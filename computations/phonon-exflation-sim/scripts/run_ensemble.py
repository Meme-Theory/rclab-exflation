"""
Ensemble simulation: run multiple realizations and compute statistical D/H.

Runs the simulation with different random seeds to build statistical
confidence in the D/H ratio measurement.

Phase 2B.1: Extended to support 50 realizations at breakthrough parameters,
with 95% CI, CV, and per-seed D/H array output.
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


def run_one(seed, N=256, L=None, dt=0.005, g0=1.0, n0=1.0,
            tau_exp=2.0, alpha=0.667, gamma0=0.0, tau_Q=50.0, n_quench=1000,
            n_heal=150, n_expand=15000, d_pair_factor=1.5,
            R_freeze=None, freeze_mode='boltzmann', soft_pairing=False):
    """Run single realization, return census at multiple times."""
    if L is None:
        L = 64.0 * (N / 256)

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0,
        R_freeze=R_freeze, freeze_mode=freeze_mode,
    )
    dx = L / N
    xi0 = 1.0 / np.sqrt(g0 * n0)
    d_pair_grid = d_pair_factor * xi0 / dx

    kibble_zurek_quench(solver, tau_Q=tau_Q, n_quench_steps=n_quench, seed=seed)
    if n_heal > 0:
        heal_wavefunction(solver, n_steps=n_heal)

    v0, _ = detect_vortices(solver.psi)
    n_vortex_init = len(v0)

    solver.time = 0.0
    meas_interval = max(n_expand // 10, 1)
    snapshots = []

    for step in range(1, n_expand + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

        if step % meas_interval == 0 or step == n_expand:
            R = expansion.scale_factor(solver.time)
            xi_t = expansion.healing_length(solver.time)
            H_t = expansion.hubble_rate(solver.time)
            census = run_census(solver.psi, d_pair_grid, L=N,
                                soft_pairing=soft_pairing, n0=n0,
                                xi=xi_t/dx, H=H_t*dx)
            snapshots.append({
                'step': step,
                'time': float(solver.time),
                'R': float(R),
                'g_eff': float(g),
                'gamma': float(gamma),
                'n_total': census['n_total'],
                'n_pair': census['n_pair'],
                'n_free': census['n_free'],
                'n_triple': census['n_triple'],
                'n_quad': census['n_quad'],
                'n_complex': census['n_complex'],
                'd_over_h': float(census['d_over_h']) if census['d_over_h'] != float('inf') else -1,
            })
            if soft_pairing and 'weighted_pairs' in census:
                snapshots[-1]['weighted_pairs'] = float(census['weighted_pairs'])

    return {
        'seed': seed,
        'n_vortex_init': n_vortex_init,
        'snapshots': snapshots,
        'final_d_over_h': snapshots[-1]['d_over_h'],
        'final_n_total': snapshots[-1]['n_total'],
        'final_n_pair': snapshots[-1]['n_pair'],
        'final_n_free': snapshots[-1]['n_free'],
    }


def run_ensemble(n_realizations=10, seed_base=1000, seed_stride=17,
                 output_file=None, **kwargs):
    """Run ensemble and compute statistics.

    Args:
        n_realizations: Number of independent realizations.
        seed_base: Base seed for the sequence. seed_i = seed_base + i * seed_stride.
        seed_stride: Stride between seeds (default: 17, coprime to common periods).
        output_file: Override output filename. Default: data/ensemble_results.json
                     or data/phase2b_ensemble.json for n_realizations >= 50.
        **kwargs: Forwarded to run_one (N, tau_exp, alpha, gamma0, etc.).

    Returns:
        results: list of per-realization dicts.
        output: summary dict with config, statistics, and per-realization data.
    """
    print("=" * 70)
    print("ENSEMBLE SIMULATION: Statistical D/H Measurement")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    N = kwargs.get('N', 256)
    tau_exp = kwargs.get('tau_exp', 2.0)
    alpha = kwargs.get('alpha', 0.667)
    gamma0 = kwargs.get('gamma0', 0.0)
    tau_Q = kwargs.get('tau_Q', 50.0)
    n_expand = kwargs.get('n_expand', 15000)
    d_pair_factor = kwargs.get('d_pair_factor', 1.5)
    R_freeze = kwargs.get('R_freeze', None)
    freeze_mode = kwargs.get('freeze_mode', 'boltzmann')
    soft_pairing = kwargs.get('soft_pairing', False)

    print(f"\n  Grid: {N}x{N}")
    print(f"  Expansion: tau_exp={tau_exp}, alpha={alpha}, gamma0={gamma0}")
    print(f"  Quench: tau_Q={tau_Q}")
    print(f"  Steps: {n_expand}")
    print(f"  d_pair_factor: {d_pair_factor}")
    if R_freeze is not None:
        print(f"  Freeze-out: R_freeze={R_freeze}, mode={freeze_mode}")
    if soft_pairing:
        print(f"  Soft pairing: enabled")
    print(f"  Realizations: {n_realizations}")
    print(f"  Seed sequence: {seed_base} + i*{seed_stride} for i in 0..{n_realizations-1}")

    results = []
    synchronize()
    t_total_start = time.time()

    for i in range(n_realizations):
        seed = seed_base + i * seed_stride
        synchronize()
        t0 = time.time()
        result = run_one(seed=seed, **kwargs)
        synchronize()
        elapsed = time.time() - t0
        results.append(result)

        dh = result['final_d_over_h']
        dh_str = f"{dh:.4e}" if dh >= 0 else "inf"
        print(f"  [{i+1:3d}/{n_realizations}] seed={seed:5d}  "
              f"init_v={result['n_vortex_init']:4d}  "
              f"final_v={result['final_n_total']:4d}  "
              f"pairs={result['final_n_pair']:3d}  "
              f"free={result['final_n_free']:4d}  "
              f"D/H={dh_str}  ({elapsed:.1f}s)")

    synchronize()
    t_total = time.time() - t_total_start

    # Statistics
    # Per-realization D/H values are already soft-weighted from run_census
    dh_values = np.array([r['final_d_over_h'] for r in results if r['final_d_over_h'] >= 0])
    n_pair_values = [r['final_n_pair'] for r in results]
    n_free_values = [r['final_n_free'] for r in results]
    n_total_values = [r['final_n_total'] for r in results]

    # Aggregate D/H: use binary pair count (geometric pairing, not soft-weighted).
    # NOTE: This differs from per-realization D/H which uses soft-weighted pairs.
    # Both are reported; the per-realization soft-weighted mean is the primary metric.
    total_pairs = sum(n_pair_values)
    total_free = sum(n_free_values)
    aggregate_dh_binary = total_pairs / total_free if total_free > 0 else float('inf')

    # Per-realization statistics
    mean_dh = float(np.mean(dh_values)) if len(dh_values) > 0 else float('nan')
    median_dh = float(np.median(dh_values)) if len(dh_values) > 0 else float('nan')
    std_dh = float(np.std(dh_values, ddof=1)) if len(dh_values) > 1 else float('nan')
    min_dh = float(np.min(dh_values)) if len(dh_values) > 0 else float('nan')
    max_dh = float(np.max(dh_values)) if len(dh_values) > 0 else float('nan')

    # Coefficient of variation
    cv = (std_dh / mean_dh * 100.0) if (mean_dh > 0 and not np.isnan(std_dh)) else float('nan')

    # 95% confidence interval (t-distribution for small samples, normal for large)
    n_valid = len(dh_values)
    if n_valid >= 2:
        se = std_dh / np.sqrt(n_valid)
        # Use 1.96 for large samples, scipy.stats.t for small if available
        if n_valid >= 30:
            z = 1.96
        else:
            try:
                from scipy.stats import t as tdist
                z = float(tdist.ppf(0.975, df=n_valid - 1))
            except ImportError:
                z = 2.0  # conservative fallback
        ci_low = mean_dh - z * se
        ci_high = mean_dh + z * se
    else:
        ci_low = float('nan')
        ci_high = float('nan')

    print(f"\n{'=' * 70}")
    print(f"ENSEMBLE RESULTS ({n_realizations} realizations, {t_total:.1f}s)")
    print(f"{'=' * 70}")
    print(f"\n  Per-realization D/H statistics ({n_valid} valid of {n_realizations}):")
    print(f"    Mean D/H:       {mean_dh:.6e}")
    print(f"    Median D/H:     {median_dh:.6e}")
    print(f"    Std D/H:        {std_dh:.6e}")
    print(f"    CV:             {cv:.1f}%")
    print(f"    95% CI:         [{ci_low:.6e}, {ci_high:.6e}]")
    print(f"    Min D/H:        {min_dh:.6e}")
    print(f"    Max D/H:        {max_dh:.6e}")

    print(f"\n  Aggregate statistics (pooled across realizations, BINARY pair count):")
    print(f"    Total binary pairs: {total_pairs}")
    print(f"    Total free:         {total_free}")
    print(f"    Aggregate D/H:      {aggregate_dh_binary:.6e}  (binary, NOT soft-weighted)")
    print(f"    Target D/H:         2.527e-05")
    print(f"    NOTE: Per-realization D/H (above) uses soft-weighted pairs -- that is")
    print(f"          the primary metric. Aggregate binary D/H is for reference only.")

    print(f"\n  Vortex statistics:")
    print(f"    Mean total:     {np.mean(n_total_values):.1f}")
    print(f"    Mean pairs:     {np.mean(n_pair_values):.1f}")
    print(f"    Mean free:      {np.mean(n_free_values):.1f}")

    # Phase 2B.1 pass/fail assessment
    print(f"\n  Phase 2B.1 Assessment:")
    pass_mean = 1e-5 <= mean_dh <= 5e-5
    pass_cv = cv < 50.0
    fail_cv = cv > 100.0
    fail_range = mean_dh < 1e-6 or mean_dh > 1e-4
    print(f"    Mean D/H in [1e-5, 5e-5]:  {'PASS' if pass_mean else 'FAIL'}")
    print(f"    CV < 50%%:                  {'PASS' if pass_cv else 'FAIL'}")
    if fail_cv:
        print(f"    CV > 100%% (noise):         FAIL")
    if fail_range:
        print(f"    Mean outside [1e-6, 1e-4]:  FAIL (noise)")
    overall = pass_mean and pass_cv
    print(f"    Overall 2B.1:               {'PASS' if overall else 'FAIL'}")

    # Per-seed D/H array for downstream analysis
    per_seed_dh = [{'seed': r['seed'], 'd_over_h': r['final_d_over_h']} for r in results]

    # Save results
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)

    if output_file is not None:
        outfile = os.path.join(outdir, output_file)
    elif n_realizations >= 50:
        outfile = os.path.join(outdir, 'phase2b_ensemble.json')
    else:
        outfile = os.path.join(outdir, 'ensemble_results.json')

    output = {
        'config': {
            'N': N, 'tau_exp': tau_exp, 'alpha': alpha,
            'gamma0': gamma0, 'tau_Q': tau_Q,
            'n_expand': n_expand, 'd_pair_factor': d_pair_factor,
            'n_realizations': n_realizations,
            'seed_base': seed_base, 'seed_stride': seed_stride,
            'R_freeze': R_freeze, 'freeze_mode': freeze_mode,
            'soft_pairing': soft_pairing,
            'backend': BACKEND_NAME,
        },
        'statistics': {
            'mean_dh': mean_dh,
            'median_dh': median_dh,
            'std_dh': std_dh,
            'cv_percent': cv,
            'ci_95_low': ci_low,
            'ci_95_high': ci_high,
            'min_dh': min_dh,
            'max_dh': max_dh,
            'aggregate_dh_binary': float(aggregate_dh_binary) if aggregate_dh_binary != float('inf') else -1,
            'total_pairs': total_pairs,
            'total_free': total_free,
            'n_valid': n_valid,
        },
        'phase2b1_pass': overall,
        'per_seed_dh': per_seed_dh,
        'realizations': results,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return results, output


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ensemble D/H measurement')
    parser.add_argument('--n-realizations', type=int, default=50,
                        help='Number of realizations (default: 50 for Phase 2B.1)')
    parser.add_argument('--N', type=int, default=1024, help='Grid size')
    parser.add_argument('--tau-exp', type=float, default=2.0)
    parser.add_argument('--alpha', type=float, default=0.667)
    parser.add_argument('--gamma0', type=float, default=0.1)
    parser.add_argument('--tau-Q', type=float, default=50.0)
    parser.add_argument('--R-freeze', type=float, default=3.0)
    parser.add_argument('--freeze-mode', type=str, default='boltzmann')
    parser.add_argument('--soft-pairing', action='store_true', default=True)
    parser.add_argument('--no-soft-pairing', dest='soft_pairing', action='store_false')
    parser.add_argument('--n-expand', type=int, default=20000)
    parser.add_argument('--d-pair-factor', type=float, default=1.5)
    parser.add_argument('--seed-base', type=int, default=1000)
    parser.add_argument('--seed-stride', type=int, default=17)
    parser.add_argument('--output', type=str, default=None, help='Output filename')
    args = parser.parse_args()

    results, output = run_ensemble(
        n_realizations=args.n_realizations,
        seed_base=args.seed_base,
        seed_stride=args.seed_stride,
        output_file=args.output,
        N=args.N,
        tau_exp=args.tau_exp,
        alpha=args.alpha,
        gamma0=args.gamma0,
        tau_Q=args.tau_Q,
        R_freeze=args.R_freeze,
        freeze_mode=args.freeze_mode,
        soft_pairing=args.soft_pairing,
        n_expand=args.n_expand,
        d_pair_factor=args.d_pair_factor,
    )
