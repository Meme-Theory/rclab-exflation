"""
Diagnostic tools: energy spectra, correlation functions, conservation checks.
"""

import numpy as np
from src.backend import xp, fft, to_numpy, as_int, clone


def compute_velocity_field(psi, dx):
    """Compute superfluid velocity v = grad(phase) / (avoiding singularities)."""
    phase = xp.angle(psi)

    # Phase gradient using central differences with proper wrapping
    vx = xp.angle(xp.exp(1j * (xp.roll(phase, -1, axis=1) - xp.roll(phase, 1, axis=1)))) / (2 * dx)
    vy = xp.angle(xp.exp(1j * (xp.roll(phase, -1, axis=0) - xp.roll(phase, 1, axis=0)))) / (2 * dx)

    return vx, vy


def incompressible_compressible_decomposition(psi, dx):
    """Decompose kinetic energy into incompressible and compressible parts.

    Following Nore et al. and Reeves et al., we decompose:
    J = sqrt(rho) * v = J_incomp + J_comp
    where div(J_incomp) = 0 and curl(J_comp) = 0.
    """
    density = xp.abs(psi) ** 2
    sqrt_rho = xp.sqrt(density + 1e-30)

    vx, vy = compute_velocity_field(psi, dx)

    # Weighted velocity (momentum density)
    Jx = sqrt_rho * vx
    Jy = sqrt_rho * vy

    N = psi.shape[0]
    kx_arr = 2 * np.pi * fft.fftfreq(N, d=dx)
    kx_grid, ky_grid = xp.meshgrid(kx_arr, kx_arr)
    k2 = kx_grid**2 + ky_grid**2
    k2_safe = clone(k2)
    k2_safe[0, 0] = 1.0  # avoid division by zero

    # Helmholtz decomposition in Fourier space
    Jx_k = fft.fft2(Jx)
    Jy_k = fft.fft2(Jy)

    # Compressible part: J_comp = grad(phi) where phi = div(J) / k^2
    div_J_k = 1j * kx_grid * Jx_k + 1j * ky_grid * Jy_k
    phi_k = div_J_k / k2_safe

    Jx_comp_k = 1j * kx_grid * phi_k
    Jy_comp_k = 1j * ky_grid * phi_k

    # Incompressible part
    Jx_incomp_k = Jx_k - Jx_comp_k
    Jy_incomp_k = Jy_k - Jy_comp_k

    return Jx_incomp_k, Jy_incomp_k, Jx_comp_k, Jy_comp_k


def energy_spectrum(psi, dx):
    """Compute 1D energy spectrum E(k) from radial binning.

    Returns k_bins, E_incomp(k), E_comp(k) as NumPy arrays.
    Uses vectorized bincount instead of Python loop.
    """
    N = psi.shape[0]
    Jx_i_k, Jy_i_k, Jx_c_k, Jy_c_k = incompressible_compressible_decomposition(psi, dx)

    kx_arr = 2 * np.pi * fft.fftfreq(N, d=dx)
    kx_grid, ky_grid = xp.meshgrid(kx_arr, kx_arr)
    k_mag = xp.sqrt(kx_grid**2 + ky_grid**2)

    # Energy densities in k-space
    E_incomp_2d = 0.5 * (xp.abs(Jx_i_k)**2 + xp.abs(Jy_i_k)**2) / N**4
    E_comp_2d = 0.5 * (xp.abs(Jx_c_k)**2 + xp.abs(Jy_c_k)**2) / N**4

    # Vectorized radial binning via bincount
    dk = 2 * np.pi / (N * dx)
    bin_indices = as_int(xp.round(k_mag / dk)).ravel()
    n_bins = int(to_numpy(xp.max(bin_indices))) + 1

    E_incomp_flat = xp.real(E_incomp_2d).ravel()
    E_comp_flat = xp.real(E_comp_2d).ravel()

    E_incomp_binned = xp.bincount(bin_indices, weights=E_incomp_flat, minlength=n_bins)
    E_comp_binned = xp.bincount(bin_indices, weights=E_comp_flat, minlength=n_bins)

    # Convert to numpy for output; skip bin 0 (DC component)
    k_bins = np.arange(1, n_bins) * float(dk)
    E_incomp_1d = to_numpy(E_incomp_binned[1:n_bins])
    E_comp_1d = to_numpy(E_comp_binned[1:n_bins])

    return k_bins, E_incomp_1d, E_comp_1d
