"""
Core split-operator pseudo-spectral GPE integrator for 2D superfluid simulation.

Solves the dimensionless 2D Gross-Pitaevskii equation:
    i dpsi/dt = [-1/2 nabla^2 + g(t)|psi|^2 - mu(t)] psi

Using the split-operator method:
    1. Half-step nonlinear (position space)
    2. FFT to momentum space
    3. Full-step kinetic (momentum space)
    4. IFFT back to position space
    5. Half-step nonlinear (position space)

Elementwise operations use numexpr for multithreaded evaluation when available.
"""

import numpy as np
from src.backend import xp, fft, to_numpy, BACKEND_NAME

# numexpr for parallel elementwise math (CPU path only)
_use_ne = False
if BACKEND_NAME == "numpy":
    try:
        import numexpr as ne
        _use_ne = True
    except ImportError:
        pass


def _density(psi):
    """Compute |psi|^2, multithreaded if possible."""
    if _use_ne:
        return ne.evaluate('real(psi * conj(psi))')
    return xp.abs(psi) ** 2


def _nonlinear_prop(psi, V_nl, dt_half):
    """psi * exp(-1j * V_nl * dt_half), multithreaded."""
    if _use_ne:
        return ne.evaluate('psi * exp(-1j * V_nl * dt_half)')
    phase = -1j * V_nl * dt_half
    return psi * xp.exp(phase)


def _nonlinear_prop_imag(psi, V_nl, dt_half):
    """psi * exp(-V_nl * dt_half), imaginary time."""
    if _use_ne:
        return ne.evaluate('psi * exp(-V_nl * dt_half)')
    return psi * xp.exp(-V_nl * dt_half)


def _nonlinear_prop_diss(psi, V_nl, dt_half, damp):
    """psi * exp((-1j - damp) * V_nl * dt_half), dissipative."""
    if _use_ne:
        return ne.evaluate('psi * exp((-1j - damp) * V_nl * dt_half)')
    return psi * xp.exp((-1j - damp) * V_nl * dt_half)


def _kinetic_prop_diss(psi_k, k2, dt, damp):
    """psi_k * exp((-0.5j - 0.5*damp) * k2 * dt), dissipative kinetic."""
    if _use_ne:
        half_damp = 0.5 * damp
        return ne.evaluate('psi_k * exp((-0.5j - half_damp) * k2 * dt)')
    return psi_k * xp.exp((-0.5j - 0.5 * damp) * k2 * dt)


def _renormalize(psi, target_sum):
    """Renormalize psi so sum(|psi|^2) = target_sum."""
    d = _density(psi)
    if _use_ne:
        s = ne.evaluate('sum(d)')
        norm = np.sqrt(target_sum / s)
        return ne.evaluate('psi * norm')
    norm = xp.sqrt(target_sum / xp.sum(d))
    return psi * norm


class GPESolver2D:
    """2D Gross-Pitaevskii equation solver using split-operator pseudo-spectral method."""

    def __init__(self, N=256, L=64.0, dt=0.005, g0=1.0, n0=1.0):
        self.N = N
        self.L = L
        self.dx = L / N
        self.dt = dt
        self.g0 = g0
        self.n0 = n0
        self.xi = 1.0 / np.sqrt(g0 * n0)  # healing length
        self.c_s = np.sqrt(g0 * n0)  # speed of sound
        self.time = 0.0
        self._target_sum = n0 * N**2  # for renormalization

        # Spatial grid
        x = xp.linspace(-L / 2, L / 2, N, endpoint=False)
        self.x, self.y = xp.meshgrid(x, x)

        # Momentum grid
        kx = 2 * np.pi * fft.fftfreq(N, d=self.dx)
        self.kx, self.ky = xp.meshgrid(kx, kx)
        self.k2 = self.kx**2 + self.ky**2

        # Kinetic propagator (full step): exp(-i * k^2/2 * dt)
        self.kinetic_propagator = xp.exp(-0.5j * self.k2 * dt)

        # Kinetic propagator for imaginary time: exp(-k^2/2 * dt)
        self.kinetic_propagator_imag = xp.exp(-0.5 * self.k2 * dt)

        # Wavefunction
        self.psi = xp.sqrt(n0) * xp.ones((N, N), dtype=complex)

    def step_real_time(self, g=None, mu=None, gamma=0.0):
        """Advance one time step using split-operator method.

        When gamma > 0, uses dissipative GPE: i dpsi/dt = (1-i*gamma)[H psi].
        """
        if g is None:
            g = self.g0
        if mu is None:
            mu = g * self.n0

        dt_half = self.dt / 2.0
        psi = self.psi

        if gamma > 0:
            damp = gamma

            # 1. Half nonlinear (dissipative)
            V_nl = g * _density(psi) - mu
            psi = _nonlinear_prop_diss(psi, V_nl, dt_half, damp)

            # 2. Kinetic step (dissipative)
            psi_k = fft.fft2(psi)
            psi_k = _kinetic_prop_diss(psi_k, self.k2, self.dt, damp)
            psi = fft.ifft2(psi_k)

            # 3. Half nonlinear (dissipative)
            V_nl = g * _density(psi) - mu
            psi = _nonlinear_prop_diss(psi, V_nl, dt_half, damp)

            # Renormalize
            self.psi = _renormalize(psi, self._target_sum)
        else:
            # 1. Half-step nonlinear
            V_nl = g * _density(psi) - mu
            psi = _nonlinear_prop(psi, V_nl, dt_half)

            # 2. FFT -> kinetic -> IFFT
            psi_k = fft.fft2(psi)
            if _use_ne:
                kp = self.kinetic_propagator
                psi_k = ne.evaluate('psi_k * kp')
            else:
                psi_k *= self.kinetic_propagator
            psi = fft.ifft2(psi_k)

            # 3. Half-step nonlinear
            V_nl = g * _density(psi) - mu
            self.psi = _nonlinear_prop(psi, V_nl, dt_half)

        self.time += self.dt

    def step_imaginary_time(self, g=None, mu=None):
        """Advance one step in imaginary time (for ground state / healing)."""
        if g is None:
            g = self.g0
        if mu is None:
            mu = g * self.n0

        dt_half = self.dt / 2.0
        psi = self.psi

        # 1. Half-step nonlinear (imaginary time)
        V_nl = g * _density(psi) - mu
        psi = _nonlinear_prop_imag(psi, V_nl, dt_half)

        # 2. FFT -> kinetic -> IFFT
        psi_k = fft.fft2(psi)
        if _use_ne:
            kp = self.kinetic_propagator_imag
            psi_k = ne.evaluate('psi_k * kp')
        else:
            psi_k *= self.kinetic_propagator_imag
        psi = fft.ifft2(psi_k)

        # 3. Half-step nonlinear (imaginary time)
        V_nl = g * _density(psi) - mu
        psi = _nonlinear_prop_imag(psi, V_nl, dt_half)

        # Renormalize
        self.psi = _renormalize(psi, self._target_sum)
        self.time += self.dt

    def get_density(self):
        return _density(self.psi)

    def get_phase(self):
        return xp.angle(self.psi)

    def get_total_particle_number(self):
        return float(xp.sum(_density(self.psi)) * self.dx**2)

    def get_energy(self, g=None, mu=None):
        """Compute total energy: kinetic + interaction."""
        if g is None:
            g = self.g0
        if mu is None:
            mu = g * self.n0

        density = _density(self.psi)

        # Kinetic energy via momentum space
        psi_k = fft.fft2(self.psi)
        E_kin = 0.5 * xp.sum(self.k2 * xp.abs(psi_k) ** 2) * (self.dx / self.N) ** 2

        # Interaction energy
        E_int = 0.5 * g * xp.sum(density**2) * self.dx**2

        return float(to_numpy(xp.real(E_kin + E_int)))
