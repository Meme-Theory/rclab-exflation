"""
Phase 2B.5: Energy conservation validation.

Run with gamma0=0 (no dissipation) and track E_kin + E_int over
the full evolution to verify the symplectic integrator preserves energy.

The split-operator pseudo-spectral method should conserve total energy
to near machine precision for unitary evolution (gamma=0). With time-
dependent g(t) from expansion, energy is NOT conserved because the
Hamiltonian is time-dependent, but the Hamiltonian at each step should
be faithfully tracked. For a FIXED g (no expansion, no dissipation),
energy should be exactly conserved.

We test two cases:
  A) gamma0=0, WITH expansion (g changes) -> energy is NOT conserved
     but we can verify it changes smoothly without numerical drift
  B) gamma0=0, NO expansion (g fixed) -> energy IS conserved
     Report max relative drift: target < 1% over 20000 steps
"""

import sys
import os
import time
import json
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.backend import BACKEND_NAME, synchronize, to_numpy
from src.gpe_solver import GPESolver2D
from src.expansion import ExpansionLaw
from src.initial_conditions import kibble_zurek_quench, heal_wavefunction


def compute_energy(solver, g, mu):
    """Compute E_kin + E_int for the current wavefunction state."""
    return solver.get_energy(g=g, mu=mu)


def run_energy_conservation_test():
    """Test energy conservation with gamma0=0."""
    print("=" * 70)
    print("PHASE 2B.5: ENERGY CONSERVATION VALIDATION")
    print(f"Backend: {BACKEND_NAME}")
    print("=" * 70)

    # Use breakthrough grid but smaller for speed; energy conservation
    # is a per-step property, not sensitive to system size
    N = 512
    L = 64.0 * (N / 256)
    dt = 0.005
    g0 = 1.0
    n0 = 1.0
    tau_Q = 50.0
    n_heal = 150
    n_steps = 20000
    measure_interval = 100
    seed = 42

    print(f"\n  Grid: {N}x{N}, L={L:.1f}, dt={dt}")
    print(f"  Steps: {n_steps}, measure every {measure_interval}")

    # ══════════════════════════════════════════════════════════════════
    # Case B: Fixed g, no expansion, no dissipation -> exact conservation
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'=' * 60}")
    print("  Case B: Fixed g (no expansion, gamma=0) -> exact conservation")
    print(f"{'=' * 60}")

    solver = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    kibble_zurek_quench(solver, tau_Q=tau_Q, n_quench_steps=1000, seed=seed)
    heal_wavefunction(solver, n_steps=n_heal)

    solver.time = 0.0
    mu = g0 * n0
    E0 = compute_energy(solver, g=g0, mu=mu)
    print(f"  Initial energy: E0 = {E0:.8e}")

    energy_b = [E0]
    times_b = [0.0]

    synchronize()
    t0 = time.time()

    for step in range(1, n_steps + 1):
        solver.step_real_time(g=g0, mu=mu, gamma=0.0)

        if step % measure_interval == 0:
            E = compute_energy(solver, g=g0, mu=mu)
            energy_b.append(E)
            times_b.append(solver.time)

    synchronize()
    elapsed_b = time.time() - t0

    energy_b = np.array(energy_b)
    rel_drift_b = np.abs(energy_b - E0) / abs(E0)
    max_rel_drift_b = float(np.max(rel_drift_b))

    print(f"  Final energy: E_final = {energy_b[-1]:.8e}")
    print(f"  Max relative drift: {max_rel_drift_b:.2e}")
    print(f"  Time: {elapsed_b:.1f}s")

    pass_b = max_rel_drift_b < 0.01
    print(f"  Pass (< 1%): {'PASS' if pass_b else 'FAIL'}")

    # ══════════════════════════════════════════════════════════════════
    # Case A: With expansion (g changes), no dissipation
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'=' * 60}")
    print("  Case A: With expansion (time-dependent g), gamma=0")
    print(f"{'=' * 60}")

    solver2 = GPESolver2D(N=N, L=L, dt=dt, g0=g0, n0=n0)
    kibble_zurek_quench(solver2, tau_Q=tau_Q, n_quench_steps=1000, seed=seed)
    heal_wavefunction(solver2, n_steps=n_heal)

    expansion = ExpansionLaw(
        tau_exp=2.0, alpha=0.667, g0=g0, n0=n0, gamma0=0.0,
        R_freeze=None,
    )

    solver2.time = 0.0
    g_init = expansion.g_eff(0.0)
    mu_init = expansion.mu_eff(0.0)
    E0_a = compute_energy(solver2, g=g_init, mu=mu_init)
    print(f"  Initial energy: E0 = {E0_a:.8e}")

    energy_a = [E0_a]
    times_a = [0.0]
    g_history = [g_init]

    synchronize()
    t0 = time.time()

    for step in range(1, n_steps + 1):
        g = expansion.g_eff(solver2.time)
        mu = expansion.mu_eff(solver2.time)
        solver2.step_real_time(g=g, mu=mu, gamma=0.0)

        if step % measure_interval == 0:
            g = expansion.g_eff(solver2.time)
            mu = expansion.mu_eff(solver2.time)
            E = compute_energy(solver2, g=g, mu=mu)
            energy_a.append(E)
            times_a.append(solver2.time)
            g_history.append(g)

    synchronize()
    elapsed_a = time.time() - t0

    energy_a = np.array(energy_a)
    print(f"  Final energy: E_final = {energy_a[-1]:.8e}")
    print(f"  Energy ratio final/initial: {energy_a[-1]/E0_a:.4f}")
    print(f"  Time: {elapsed_a:.1f}s")

    # Check smoothness: energy changes should be monotonic (no numerical jumps)
    dE = np.diff(energy_a)
    # With expansion and decreasing g, energy should generally decrease
    n_sign_changes = int(np.sum(np.diff(np.sign(dE)) != 0))
    print(f"  Energy derivative sign changes: {n_sign_changes} "
          f"(out of {len(dE)-1} intervals)")

    # Overall
    print(f"\n{'=' * 70}")
    print(f"PHASE 2B.5 RESULTS")
    print(f"{'=' * 70}")
    print(f"  Case B (fixed g, exact conservation):")
    print(f"    Max relative drift: {max_rel_drift_b:.2e}")
    print(f"    Pass (< 1%): {'PASS' if pass_b else 'FAIL'}")
    print(f"  Case A (expanding g, energy not conserved):")
    print(f"    Energy ratio final/initial: {energy_a[-1]/E0_a:.4f}")
    print(f"    Monotonicity sign changes: {n_sign_changes}")
    overall = pass_b
    print(f"\n  Phase 2B.5 Overall: {'PASS' if overall else 'FAIL'}")

    # Save
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'phase2b_energy_conservation.json')

    output = {
        'config': {
            'N': N, 'L': L, 'dt': dt, 'g0': g0, 'n0': n0,
            'n_steps': n_steps, 'measure_interval': measure_interval,
            'backend': BACKEND_NAME,
        },
        'case_b_fixed_g': {
            'E0': float(E0),
            'E_final': float(energy_b[-1]),
            'max_relative_drift': max_rel_drift_b,
            'pass': pass_b,
            'energy_history': energy_b.tolist(),
            'times': times_b,
        },
        'case_a_expanding_g': {
            'E0': float(E0_a),
            'E_final': float(energy_a[-1]),
            'energy_ratio': float(energy_a[-1] / E0_a),
            'sign_changes': n_sign_changes,
            'energy_history': energy_a.tolist(),
            'times': times_a,
        },
        'phase2b5_pass': overall,
    }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {os.path.abspath(outfile)}")

    return output


if __name__ == '__main__':
    output = run_energy_conservation_test()
