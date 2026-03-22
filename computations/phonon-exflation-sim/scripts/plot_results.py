"""
Visualization for the phonon-exflation simulation.
Generates density plots, phase plots, vortex maps, and D/H evolution.
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

from src.backend import BACKEND_NAME, to_numpy, synchronize
from src.gpe_solver import GPESolver2D
from src.expansion import ExpansionLaw
from src.initial_conditions import random_phase_ic, kibble_zurek_quench, heal_wavefunction
from src.vortex_detection import detect_vortices
from src.defect_census import run_census


def plot_snapshot(solver, census, title, filename, L):
    """Generate a 2x2 panel showing density, phase, vortex map, and census."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle(title, fontsize=14, fontweight='bold')

    density = to_numpy(solver.get_density())
    phase = to_numpy(solver.get_phase())
    dx = solver.dx

    extent = [-L/2, L/2, -L/2, L/2]

    # Panel 1: Density
    ax = axes[0, 0]
    im = ax.imshow(density, extent=extent, cmap='inferno', origin='lower')
    plt.colorbar(im, ax=ax, label=r'$|\psi|^2$')
    ax.set_title('Condensate Density')
    ax.set_xlabel('x / xi')
    ax.set_ylabel('y / xi')

    # Panel 2: Phase
    ax = axes[0, 1]
    im = ax.imshow(phase, extent=extent, cmap='twilight', origin='lower',
                   vmin=-np.pi, vmax=np.pi)
    plt.colorbar(im, ax=ax, label='Phase (rad)')
    ax.set_title('Phase Field')
    ax.set_xlabel('x / xi')
    ax.set_ylabel('y / xi')

    # Panel 3: Vortex map
    ax = axes[1, 0]
    ax.imshow(density, extent=extent, cmap='gray_r', origin='lower', alpha=0.3)

    vortex_positions = census['vortex_positions']
    pairs = census['pairs']

    # Plot free vortices
    for y, x, c in vortex_positions:
        physical_x = (x / solver.N - 0.5) * L
        physical_y = (y / solver.N - 0.5) * L
        is_paired = False
        for (py1, px1), (py2, px2) in pairs:
            if (y == py1 and x == px1) or (y == py2 and x == px2):
                is_paired = True
                break
        if not is_paired:
            color = 'red' if c > 0 else 'blue'
            marker = '+' if c > 0 else 'x'
            ax.plot(physical_x, physical_y, marker, color=color, markersize=6, alpha=0.7)

    # Plot paired vortices with connecting lines
    for (py1, px1), (py2, px2) in pairs:
        x1 = (px1 / solver.N - 0.5) * L
        y1 = (py1 / solver.N - 0.5) * L
        x2 = (px2 / solver.N - 0.5) * L
        y2 = (py2 / solver.N - 0.5) * L
        ax.plot([x1, x2], [y1, y2], 'g-', linewidth=1, alpha=0.5)
        ax.plot(x1, y1, '+', color='green', markersize=6)
        ax.plot(x2, y2, 'x', color='green', markersize=6)

    ax.set_title(f'Vortex Map (red/blue=free, green=paired)')
    ax.set_xlabel('x / xi')
    ax.set_ylabel('y / xi')
    ax.set_xlim(-L/2, L/2)
    ax.set_ylim(-L/2, L/2)

    # Panel 4: Census text
    ax = axes[1, 1]
    ax.axis('off')
    text = (
        f"DEFECT CENSUS\n"
        f"{'='*40}\n"
        f"Total vortices:     {census['n_total']}\n"
        f"  Positive (+1):    {census['n_positive']}\n"
        f"  Negative (-1):    {census['n_negative']}\n\n"
        f"Bound pairs:        {census['n_pair']}  (D analog)\n"
        f"Free vortices:      {census['n_free']}  (H analog)\n"
        f"3-vortex clusters:  {census['n_triple']}  (He-3)\n"
        f"4-vortex clusters:  {census['n_quad']}  (He-4)\n"
        f"7+ clusters:        {census['n_complex']}  (Li-7)\n\n"
        f"{'='*40}\n"
        f"D/H ratio:          {census['d_over_h']:.6e}\n"
        f"D/H target:         {census['d_over_h_target']:.6e}\n"
    )
    ax.text(0.1, 0.95, text, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")


def plot_evolution(measurements, filename):
    """Plot D/H ratio, vortex counts, and scale factor evolution."""
    fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    fig.suptitle('Phonon-Exflation Simulation: Time Evolution', fontsize=14, fontweight='bold')

    times = [m['time'] for m in measurements]
    d_over_h = [m['d_over_h'] for m in measurements]
    n_total = [m['n_total'] for m in measurements]
    n_pair = [m['n_pair'] for m in measurements]
    n_free = [m['n_free'] for m in measurements]
    R = [m['R'] for m in measurements]

    # Panel 1: D/H ratio
    ax = axes[0]
    ax.semilogy(times, d_over_h, 'ko-', markersize=4, label='D/H (simulation)')
    ax.axhline(y=2.527e-5, color='r', linestyle='--', label=f'D/H target = 2.527e-5')
    ax.set_ylabel('D/H ratio')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title('Deuterium-to-Hydrogen Ratio')

    # Panel 2: Vortex counts
    ax = axes[1]
    ax.plot(times, n_total, 'k-', label='Total', linewidth=2)
    ax.plot(times, n_free, 'r-', label='Free (H analog)')
    ax.plot(times, n_pair, 'g-', label='Paired (D analog)')
    ax.set_ylabel('Count')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title('Vortex Population')

    # Panel 3: Scale factor
    ax = axes[2]
    ax.plot(times, R, 'b-', linewidth=2)
    ax.set_ylabel('Scale Factor R(t)')
    ax.set_xlabel('Time (units of xi/c_s)')
    ax.grid(True, alpha=0.3)
    ax.set_title('Cosmological Expansion')

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")


def generate_all_plots():
    """Run simulation and generate all visualization."""
    print("=" * 70)
    print(f"GENERATING VISUALIZATION (Backend: {BACKEND_NAME})")
    print("=" * 70)

    figdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(figdir, exist_ok=True)

    # Setup - uses KZ quench + dissipative expansion
    N, L, dt = 256, 64.0, 0.005
    g0, n0 = 1.0, 1.0
    tau_exp, alpha = 2.0, 0.667
    gamma0 = 0.01  # K-compactification dissipation
    d_pair_factor = 1.5
    seed = 42

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    expansion = ExpansionLaw(tau_exp=tau_exp, alpha=alpha, g0=g0, n0=n0, gamma0=gamma0)
    xi0 = 1.0 / np.sqrt(g0 * n0)
    d_pair_grid = d_pair_factor * xi0 / solver.dx

    # Initial conditions - KZ quench
    print("\n[1/4] Kibble-Zurek quench IC...")
    kibble_zurek_quench(solver, tau_Q=50.0, seed=seed)
    census = run_census(solver.psi, d_pair_grid, L=N)
    plot_snapshot(solver, census, "Post-Quench: Vortex Population (KZ)",
                  os.path.join(figdir, "01_post_quench.png"), L)

    # After healing
    print("[2/4] Post-quench healing...")
    heal_wavefunction(solver, n_steps=150)
    census = run_census(solver.psi, d_pair_grid, L=N)
    plot_snapshot(solver, census, "After Healing: Stabilized Vortices",
                  os.path.join(figdir, "02_after_healing.png"), L)

    # Dissipative expansion evolution
    print("[3/4] Dissipative expansion evolution...")
    solver.time = 0.0
    n_steps = 15000
    meas_interval = 500
    measurements = []

    snapshot_steps = {500, n_steps // 2, n_steps}

    for step in range(1, n_steps + 1):
        g = expansion.g_eff(solver.time)
        mu = expansion.mu_eff(solver.time)
        gamma = expansion.gamma_eff(solver.time)
        solver.step_real_time(g=g, mu=mu, gamma=gamma)

        if step % meas_interval == 0:
            R = expansion.scale_factor(solver.time)
            census = run_census(solver.psi, d_pair_grid, L=N)
            measurements.append({
                'step': step, 'time': solver.time, 'R': R,
                **{k: v for k, v in census.items()
                   if k not in ('vortex_positions', 'pairs', 'clusters')},
            })

            if step in snapshot_steps:
                plot_snapshot(solver, census,
                              f"Expansion+Dissipation: t={solver.time:.1f}, R={R:.2f}",
                              os.path.join(figdir, f"03_expansion_t{solver.time:.0f}.png"), L)

    # Evolution plot
    print("[4/4] Evolution plots...")
    plot_evolution(measurements,
                   os.path.join(figdir, "04_evolution.png"))

    print(f"\nAll figures saved to {os.path.abspath(figdir)}")


if __name__ == '__main__':
    generate_all_plots()
