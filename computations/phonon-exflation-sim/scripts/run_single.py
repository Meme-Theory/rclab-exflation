"""
Phonon-Exflation Substrate Simulation
======================================
Single simulation run with Phase 2 GPU acceleration and freeze-out physics.

Implements the full pipeline:
1. Kibble-Zurek quench through BKT transition -> vortex generation
2. Brief healing to stabilize vortex cores
3. Real-time evolution with cosmological expansion + freeze-out
4. Vortex detection, pair identification, defect census
5. D/H ratio computation and time evolution tracking

Exit criteria: simulation runs to completion, produces D/H ratio.
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.backend import BACKEND_NAME, FFT_BACKEND, synchronize
from src.gpe_solver import GPESolver2D
from src.expansion import ExpansionLaw
from src.initial_conditions import (
    random_phase_ic, heal_wavefunction, kibble_zurek_quench,
    smoothed_random_phase_ic,
)
from src.vortex_detection import detect_vortices
from src.defect_census import run_census, print_census


def run_simulation(
    # Grid
    N=256,
    L=None,  # default: scale with N to keep dx/xi = 0.25
    dt=0.005,
    # Physics
    g0=1.0,
    n0=1.0,
    # Expansion
    tau_exp=2.0,
    alpha=0.667,
    # Dissipation (K-compactification)
    gamma0=0.01,
    # Freeze-out (Phase 2)
    R_freeze=None,
    freeze_mode='boltzmann',
    # Soft pairing (Phase 2)
    soft_pairing=False,
    # Initial conditions
    ic_method='kz_quench',  # 'random_phase', 'smoothed', 'kz_quench'
    n_heal_steps=150,
    tau_Q=50.0,
    n_quench_steps=1000,
    correlation_length=2.0,
    # Evolution
    n_expansion_steps=20000,
    measurement_interval=1000,
    # Analysis
    d_pair_factor=1.5,
    # Reproducibility
    seed=42,
):
    """Run a complete phonon-exflation simulation."""
    # Scale L with N to keep dx/xi constant
    if L is None:
        L = 64.0 * (N / 256)

    print("=" * 70)
    print("PHONON-EXFLATION SUBSTRATE SIMULATION (Phase 2)")
    print(f"Array backend: {BACKEND_NAME}  |  FFT backend: {FFT_BACKEND}")
    print("=" * 70)

    # ── Setup ──
    xi0 = 1.0 / np.sqrt(g0 * n0)
    cs0 = np.sqrt(g0 * n0)
    dx = L / N

    print(f"\n[CONFIG]")
    print(f"  Grid:       {N}x{N}, L={L}, dx={dx:.4f}")
    print(f"  Time step:  {dt}")
    print(f"  Physics:    g0={g0}, n0={n0}, xi0={xi0:.4f}, cs0={cs0:.4f}")
    print(f"  Expansion:  tau_exp={tau_exp}, alpha={alpha}")
    print(f"  Dissipation: gamma0={gamma0} (K-compactification)")
    if R_freeze is not None:
        print(f"  Freeze-out: R_freeze={R_freeze}, mode={freeze_mode}")
    else:
        print(f"  Freeze-out: disabled (legacy mode)")
    if soft_pairing:
        print(f"  Soft pairing: enabled")
    print(f"  IC method:  {ic_method}")
    print(f"  Evolution:  {n_expansion_steps} steps ({n_expansion_steps*dt:.1f} time units)")
    print(f"  dx < xi:    {'OK' if dx < xi0 else 'WARNING: dx > xi!'}")
    print(f"  CFL dt<dx2: {'OK' if dt < dx**2 else 'WARNING: CFL violated!'}")

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(
        tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0,
        R_freeze=R_freeze, freeze_mode=freeze_mode,
    )

    d_pair = d_pair_factor * xi0
    d_pair_grid = d_pair / dx  # FIXED pairing distance in grid units
    L_grid = N

    print(f"  Pairing:    {d_pair:.2f} physical = {d_pair_grid:.2f} grid units (FIXED)")

    if R_freeze is not None:
        t_freeze = expansion.freeze_out_time()
        print(f"  Freeze-out time: t={t_freeze:.2f}")

    # ── Phase 1: Initial conditions ──
    print(f"\n[PHASE 1] Initial conditions: {ic_method}")

    if ic_method == 'kz_quench':
        print(f"  Kibble-Zurek quench: tau_Q={tau_Q}, {n_quench_steps} quench steps")
        synchronize()
        t0 = time.time()
        kibble_zurek_quench(solver, tau_Q=tau_Q, n_quench_steps=n_quench_steps, seed=seed)
        synchronize()
        print(f"  Quench completed in {time.time()-t0:.2f}s")

        # Brief healing to clean up vortex cores
        if n_heal_steps > 0:
            print(f"  Post-quench healing: {n_heal_steps} steps")
            heal_wavefunction(solver, n_steps=n_heal_steps)

    elif ic_method == 'smoothed':
        smoothed_random_phase_ic(solver, correlation_length=correlation_length, seed=seed)
        print(f"  Smoothed random phase (corr_length={correlation_length})")
        if n_heal_steps > 0:
            heal_wavefunction(solver, n_steps=n_heal_steps)

    else:  # random_phase
        random_phase_ic(solver, seed=seed)
        if n_heal_steps > 0:
            heal_wavefunction(solver, n_steps=n_heal_steps)

    # Post-IC census
    vortices_ic, _ = detect_vortices(solver.psi)
    n_ic = len(vortices_ic)
    print(f"  Post-IC vortex count: {n_ic}")

    census0 = run_census(solver.psi, d_pair_grid, L=L_grid,
                         soft_pairing=soft_pairing, n0=n0,
                         xi=xi0/dx, H=0.0)
    print(f"\n[INITIAL CENSUS - Before Expansion]")
    print_census(census0)

    # ── Phase 2: Real-time expansion ──
    print(f"\n[PHASE 2] Real-time evolution with expansion ({n_expansion_steps} steps)")
    t_final = n_expansion_steps * dt
    R_final_expected = expansion.scale_factor(t_final)
    print(f"  Expected final R = {R_final_expected:.2f} ({R_final_expected:.1f}x expansion)")

    solver.time = 0.0
    measurements = []
    synchronize()
    t_start = time.time()

    sc_stopped = False  # self-consistent freeze-out early stop flag

    for step in range(1, n_expansion_steps + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

        if step % measurement_interval == 0 or step == n_expansion_steps:
            synchronize()
            R = expansion.scale_factor(solver.time)
            xi_t = expansion.healing_length(solver.time)
            H_t = expansion.hubble_rate(solver.time)

            census = run_census(solver.psi, d_pair_grid, L=L_grid,
                                soft_pairing=soft_pairing, n0=n0,
                                xi=xi_t/dx, H=H_t*dx)

            # Compute mean inter-vortex spacing for freeze-out check
            n_vortices = census['n_total']
            if n_vortices > 0:
                # d_mean in physical units: sqrt(L^2 / N_vortex)
                d_mean_phys = np.sqrt(L**2 / n_vortices)
            else:
                d_mean_phys = L  # no vortices -> large spacing

            # Self-consistent freeze-out check
            if freeze_mode == 'self_consistent':
                frozen = expansion.check_self_consistent_freeze(solver.time, d_mean_phys)
            elif R_freeze is not None:
                frozen = expansion.is_frozen_out(solver.time, d_mean_phys)
            else:
                frozen = False

            measurements.append({
                'step': step,
                'time': solver.time,
                'R': R,
                'g_eff': g,
                'gamma': gamma,
                'xi': xi_t,
                'd_mean': d_mean_phys,
                'frozen_out': frozen,
                **{k: v for k, v in census.items()
                   if k not in ('vortex_positions', 'pairs', 'clusters',
                                'pair_weights')},
            })

            elapsed = time.time() - t_start
            sps = step / elapsed if elapsed > 0 else 0
            freeze_str = " [FROZEN]" if frozen else ""
            print(f"  Step {step:6d}/{n_expansion_steps} | "
                  f"t={solver.time:8.2f} | R={R:.3f} | g={g:.5f} | "
                  f"gamma={gamma:.5f} | "
                  f"N_v={census['n_total']:4d} | "
                  f"pairs={census['n_pair']:3d} free={census['n_free']:4d} | "
                  f"D/H={census['d_over_h']:.4e} | "
                  f"{sps:.0f} sps{freeze_str}")

            # Self-consistent freeze-out: stop evolution when frozen
            if freeze_mode == 'self_consistent' and frozen and not sc_stopped:
                sc_stopped = True
                print(f"\n  *** SELF-CONSISTENT FREEZE-OUT at t={solver.time:.2f}, "
                      f"R={R:.3f} ***")
                print(f"  *** Stopping evolution (H > c_s/d_mean) ***")
                break

    synchronize()
    t_total = time.time() - t_start

    # ── Final census ──
    final_census = run_census(solver.psi, d_pair_grid, L=L_grid,
                              soft_pairing=soft_pairing, n0=n0,
                              xi=expansion.healing_length(solver.time)/dx,
                              H=expansion.hubble_rate(solver.time)*dx)
    stopped_label = " (self-consistent freeze-out)" if sc_stopped else ""
    print(f"\n[FINAL CENSUS - After Expansion{stopped_label}]")
    print_census(final_census)

    # ── Summary ──
    R_final = expansion.scale_factor(solver.time)
    print(f"\n{'=' * 70}")
    print(f"SIMULATION COMPLETE  ({t_total:.1f}s, {n_expansion_steps/t_total:.0f} steps/s)")
    print(f"{'=' * 70}")
    print(f"  Backend:            {BACKEND_NAME}")
    print(f"  Final D/H ratio:    {final_census['d_over_h']:.6e}")
    print(f"  Target D/H ratio:   2.527000e-05")
    print(f"  Scale factor:       {R_final:.3f} ({R_final:.1f}x expansion)")
    print(f"  Initial vortices:   {n_ic}")
    print(f"  Final vortices:     {final_census['n_total']}")
    print(f"  Vortex annihilation: {n_ic - final_census['n_total']} "
          f"({100*(1 - final_census['n_total']/max(n_ic,1)):.1f}%)")

    if freeze_mode == 'self_consistent':
        if expansion.sc_freeze_time is not None:
            print(f"  Self-consistent freeze-out: t={expansion.sc_freeze_time:.2f}, "
                  f"R={expansion.sc_freeze_R:.3f}")
        else:
            print(f"  Self-consistent freeze-out: NOT TRIGGERED (ran to completion)")

    if final_census['d_over_h'] > 0 and final_census['d_over_h'] != float('inf'):
        log_dh = np.log10(final_census['d_over_h'])
        log_target = np.log10(2.527e-5)
        print(f"  log10(D/H):         {log_dh:.3f}  (target: {log_target:.3f})")
        print(f"  Orders of magnitude off: {log_dh - log_target:.1f}")

    # D/H evolution summary
    print(f"\n  D/H Evolution ({len(measurements)} measurements):")
    print(f"  {'Time':>8s}  {'R':>7s}  {'g_eff':>8s}  {'gamma':>8s}  "
          f"{'N_vort':>6s}  {'N_pair':>6s}  {'N_free':>6s}  {'D/H':>12s}  {'Frozen':>6s}")
    print(f"  {'-'*80}")
    for m in measurements:
        frozen_str = "YES" if m.get('frozen_out', False) else ""
        print(f"  {m['time']:8.2f}  {m['R']:7.3f}  {m['g_eff']:8.5f}  "
              f"{m['gamma']:8.5f}  "
              f"{m['n_total']:6d}  {m['n_pair']:6d}  {m['n_free']:6d}  "
              f"{m['d_over_h']:12.4e}  {frozen_str:>6s}")

    return solver, measurements, final_census


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Single phonon-exflation simulation')
    parser.add_argument('--N', type=int, default=256)
    parser.add_argument('--L', type=float, default=None)
    parser.add_argument('--dt', type=float, default=0.005)
    parser.add_argument('--g0', type=float, default=1.0)
    parser.add_argument('--n0', type=float, default=1.0)
    parser.add_argument('--tau-exp', type=float, default=2.0)
    parser.add_argument('--alpha', type=float, default=0.667)
    parser.add_argument('--gamma0', type=float, default=0.01)
    parser.add_argument('--R-freeze', type=float, default=None)
    parser.add_argument('--freeze-mode', type=str, default='boltzmann',
                        choices=['boltzmann', 'exponential', 'step', 'self_consistent'])
    parser.add_argument('--soft-pairing', action='store_true', default=False)
    parser.add_argument('--ic-method', type=str, default='kz_quench',
                        choices=['random_phase', 'smoothed', 'kz_quench'])
    parser.add_argument('--tau-Q', type=float, default=50.0)
    parser.add_argument('--n-heal-steps', type=int, default=150)
    parser.add_argument('--n-expansion-steps', type=int, default=20000)
    parser.add_argument('--measurement-interval', type=int, default=1000)
    parser.add_argument('--d-pair-factor', type=float, default=1.5)
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()

    solver, measurements, final_census = run_simulation(
        N=args.N, L=args.L, dt=args.dt, g0=args.g0, n0=args.n0,
        tau_exp=args.tau_exp, alpha=args.alpha, gamma0=args.gamma0,
        R_freeze=args.R_freeze, freeze_mode=args.freeze_mode,
        soft_pairing=args.soft_pairing, ic_method=args.ic_method,
        tau_Q=args.tau_Q, n_heal_steps=args.n_heal_steps,
        n_expansion_steps=args.n_expansion_steps,
        measurement_interval=args.measurement_interval,
        d_pair_factor=args.d_pair_factor, seed=args.seed,
    )
