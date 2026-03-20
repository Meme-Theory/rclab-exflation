"""
Initial condition generators for the GPE simulation.

Option B (Random phase seeding): Start with uniform density and random phase,
then evolve with imaginary-time propagation to heal the wavefunction.
This naturally generates a population of vortices from the random phase field.
"""

import numpy as np
from src.backend import xp, fft, ensure_array, BACKEND_NAME

# numexpr for parallel elementwise math in KZ quench hot loop
_use_ne = False
if BACKEND_NAME == "numpy":
    try:
        import numexpr as ne
        _use_ne = True
    except ImportError:
        pass


def random_phase_ic(solver, seed=None):
    """Option B: Random phase seeding.

    Sets psi = sqrt(n0) * exp(i * random_phase).
    Must then be healed with imaginary-time propagation.
    """
    rng = np.random.default_rng(seed)
    phase = rng.uniform(0, 2 * np.pi, size=(solver.N, solver.N))
    solver.psi = ensure_array(np.sqrt(solver.n0) * np.exp(1j * phase))


def smoothed_random_phase_ic(solver, correlation_length=4.0, seed=None):
    """Random phase seeding with spatial correlations.

    Smoothing the phase field controls the initial vortex density:
    larger correlation_length -> fewer initial vortices.
    """
    rng = np.random.default_rng(seed)

    # Generate random phase on CPU for reproducibility
    raw_phase = rng.uniform(0, 2 * np.pi, size=(solver.N, solver.N))

    # Transfer to backend and smooth in Fourier space
    raw_phase_gpu = ensure_array(raw_phase)
    phase_k = fft.fft2(xp.exp(1j * raw_phase_gpu))

    # Gaussian filter in k-space
    sigma_k = 2 * np.pi / correlation_length
    gauss_filter = xp.exp(-(solver.kx**2 + solver.ky**2) / (2 * sigma_k**2))
    phase_k *= gauss_filter

    smoothed = fft.ifft2(phase_k)
    smoothed_phase = xp.angle(smoothed)

    solver.psi = xp.sqrt(solver.n0) * xp.exp(1j * smoothed_phase)


def heal_wavefunction(solver, n_steps=500):
    """Imaginary-time propagation to heal the wavefunction.

    This relaxes the random phase field toward the ground state
    while preserving topological defects (vortices).
    """
    for _ in range(n_steps):
        solver.step_imaginary_time()

    return solver


def kibble_zurek_quench(solver, tau_Q=100.0, n_quench_steps=2000, seed=None):
    """Option A: Kibble-Zurek quench through the BKT transition.

    Uses REAL-TIME evolution with ramping g(t). This is critical:
    the KZM requires that the system cannot fully relax during the
    quench, so defects freeze in. Imaginary-time would always relax
    to ground state, bypassing the KZM entirely.

    Protocol:
    1. Start with random phase (disordered state)
    2. Brief imaginary-time step to establish smooth density (but keep phase disorder)
    3. Ramp g from 0 to g0 using REAL-TIME split-operator steps
    4. Fast ramp -> more defects freeze in (KZM scaling)
    5. Slow ramp -> system relaxes, fewer defects

    Args:
        solver: GPESolver2D instance
        tau_Q: quench timescale (controls ramp speed: dt_quench = tau_Q/n_quench_steps)
        n_quench_steps: number of steps for the g ramp
        seed: random seed
    """
    # Start with random phase (disordered state above T_KT)
    random_phase_ic(solver, seed=seed)

    # Brief imaginary-time to smooth density while keeping phase topology
    for _ in range(20):
        solver.step_imaginary_time(g=0.01 * solver.g0, mu=0.01 * solver.g0 * solver.n0)

    # Use solver dt for stability; compute actual number of steps from tau_Q
    dt_eff = solver.dt
    actual_steps = max(int(tau_Q / dt_eff), 100)

    g_start = 0.01 * solver.g0
    g_final = solver.g0
    n0 = solver.n0
    k2 = solver.k2
    psi = solver.psi

    # Ramp g using REAL-TIME evolution (split-operator)
    for step in range(actual_steps):
        frac = step / max(actual_steps - 1, 1)
        g_t = g_start + (g_final - g_start) * frac
        mu_t = g_t * n0
        dt_half = dt_eff / 2.0

        if _use_ne:
            # 1. Half nonlinear step
            density = ne.evaluate('real(psi * conj(psi))')
            V_nl = ne.evaluate('g_t * density - mu_t')
            psi = ne.evaluate('psi * exp(-1j * V_nl * dt_half)')

            # 2. Kinetic step
            psi_k = fft.fft2(psi)
            psi_k = ne.evaluate('psi_k * exp(-0.5j * k2 * dt_eff)')
            psi = fft.ifft2(psi_k)

            # 3. Half nonlinear step
            density = ne.evaluate('real(psi * conj(psi))')
            V_nl = ne.evaluate('g_t * density - mu_t')
            psi = ne.evaluate('psi * exp(-1j * V_nl * dt_half)')
        else:
            # 1. Half nonlinear step
            density = xp.abs(psi) ** 2
            psi *= xp.exp(-1j * (g_t * density - mu_t) * dt_half)

            # 2. Kinetic step
            psi_k = fft.fft2(psi)
            psi_k *= xp.exp(-0.5j * k2 * dt_eff)
            psi = fft.ifft2(psi_k)

            # 3. Half nonlinear step
            density = xp.abs(psi) ** 2
            psi *= xp.exp(-1j * (g_t * density - mu_t) * dt_half)

    solver.psi = psi
    return solver
