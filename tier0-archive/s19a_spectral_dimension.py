"""
Session 19a — S-2: Spectral Dimension d_s(tau, sigma)
=====================================================

Computes the spectral dimension from the heat kernel trace:
    K(tau, sigma) = Sum_n mult_n * exp(-sigma * lambda_n(tau)^2)
    d_s(tau, sigma) = -2 * d(log K) / d(log sigma)

For a d-dimensional Riemannian manifold, Weyl's law gives d_s -> d as sigma -> 0.
At tau=0 (homogeneous SU(3)), d_s = 8 at ALL scales (high degeneracies enforce this).
Any departure from d_s = 8 at tau > 0 is a definitive signature of broken homogeneity.

CDT connection: If d_s = 4 crossing exists, direct link to Ambjorn et al. (2005)
spectral dimension flow (d_s flows from ~2 at Planck scales to ~4 at macroscopic scales).

NOTE: This diagnostic uses eigenvalues WITH multiplicities (PW mult = dim(p,q)).
Unlike S-1 (level statistics), S-2 works correctly with block-diagonal data because
the heat kernel trace is a sum over all modes, not a correlation measure.

Constraint Condition: d_s(tau, sigma) = 8 everywhere (no dimensional reduction).
Confirm condition: d_s = 4 crossing exists at some (tau_c, sigma_c).

Environment: Venv Python (numpy + scipy + matplotlib).

Author: phonon-exflation-sim agent (Session 19a)
Date: 2026-02-15
"""

import sys
import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from s19a_sweep_data import load_sweep_data


# =============================================================================
# HEAT KERNEL + SPECTRAL DIMENSION
# =============================================================================

def compute_heat_kernel(eigenvalues, multiplicities, sigma_values):
    """
    Compute heat kernel trace K(sigma) = Sum_n mult_n * exp(-sigma * lambda_n^2).

    Uses eigenvalues with Peter-Weyl multiplicities to get the full trace.

    Args:
        eigenvalues: array of |lambda_n|
        multiplicities: array of PW multiplicities dim(p,q)
        sigma_values: array of diffusion time values

    Returns:
        K: array of heat kernel values K(sigma)
    """
    # lambda_n^2 for each eigenvalue
    lam2 = eigenvalues ** 2

    K = np.zeros(len(sigma_values))
    for i, sigma in enumerate(sigma_values):
        # exp(-sigma * lambda_n^2) with multiplicities
        K[i] = np.sum(multiplicities * np.exp(-sigma * lam2))

    return K


def spectral_dimension(K, sigma_values):
    """
    Extract spectral dimension d_s = -2 * d(log K) / d(log sigma).

    Uses central differences in log-space for numerical differentiation.

    Args:
        K: heat kernel trace values K(sigma)
        sigma_values: corresponding sigma values

    Returns:
        d_s: spectral dimension at each sigma (interior points)
        sigma_mid: sigma values at interior points
    """
    log_K = np.log(K)
    log_sigma = np.log(sigma_values)

    # Central differences for d(log K)/d(log sigma)
    d_log_K = np.gradient(log_K, log_sigma)

    d_s = -2.0 * d_log_K

    return d_s, sigma_values


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_spectral_dimension(data):
    """
    Compute the spectral dimension surface d_s(tau, sigma).
    """
    tau_values = data['tau_values']
    n_tau = len(tau_values)

    # Sigma range: logspace from 0.01 to 100
    sigma_values = np.logspace(-2, 2, 80)
    n_sigma = len(sigma_values)

    # Storage
    K_surface = np.zeros((n_tau, n_sigma))
    d_s_surface = np.zeros((n_tau, n_sigma))

    print(f"  Computing heat kernel at {n_tau} x {n_sigma} = {n_tau * n_sigma} points...")

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]

        # Heat kernel
        K = compute_heat_kernel(evals, mults, sigma_values)
        K_surface[i, :] = K

        # Spectral dimension
        d_s, _ = spectral_dimension(K, sigma_values)
        d_s_surface[i, :] = d_s

        # Check d_s at sigma=1.0 (fiducial)
        idx_sigma1 = np.argmin(np.abs(sigma_values - 1.0))
        d_s_at_1 = d_s[idx_sigma1]

        if i % 5 == 0 or i == n_tau - 1:
            print(f"    tau={tau:.2f}: d_s(sigma=1) = {d_s_at_1:.4f}, "
                  f"K(sigma=0.01) = {K[0]:.2e}, K(sigma=100) = {K[-1]:.2e}")

    # --- VALIDATION: d_s(0, sigma) should be ~8 ---
    d_s_tau0 = d_s_surface[0, :]
    d_s_tau0_mean = np.mean(d_s_tau0[10:-10])  # exclude edges
    print(f"\n  Validation: d_s(tau=0, sigma) mean = {d_s_tau0_mean:.4f} (expected: 8.0)")

    # --- FIND d_s = 4 CROSSING ---
    # For each tau, find sigma where d_s = 4 (if it exists)
    d_s_4_sigma = np.full(n_tau, np.nan)
    for i in range(n_tau):
        for j in range(n_sigma - 1):
            if (d_s_surface[i, j] - 4) * (d_s_surface[i, j + 1] - 4) < 0:
                # Linear interpolation
                frac = (4 - d_s_surface[i, j]) / (d_s_surface[i, j + 1] - d_s_surface[i, j])
                log_sigma_cross = np.log10(sigma_values[j]) + frac * (
                    np.log10(sigma_values[j + 1]) - np.log10(sigma_values[j]))
                d_s_4_sigma[i] = 10 ** log_sigma_cross
                break  # first crossing only

    # --- d_s at sigma=1.0 (1D slice for CDT comparison) ---
    idx_sigma1 = np.argmin(np.abs(sigma_values - 1.0))
    d_s_sigma1 = d_s_surface[:, idx_sigma1]

    # --- d_s range at each tau ---
    d_s_min = np.min(d_s_surface[:, 5:-5], axis=1)  # exclude edge artifacts
    d_s_max = np.max(d_s_surface[:, 5:-5], axis=1)

    return {
        'tau_values': tau_values,
        'sigma_values': sigma_values,
        'K_surface': K_surface,
        'd_s_surface': d_s_surface,
        'd_s_4_sigma': d_s_4_sigma,
        'd_s_sigma1': d_s_sigma1,
        'd_s_tau0': d_s_tau0,
        'd_s_min': d_s_min,
        'd_s_max': d_s_max,
    }


def plot_results(results, output_dir):
    """Generate S-2 diagnostic plots."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize

    tau = results['tau_values']
    sigma = results['sigma_values']
    d_s = results['d_s_surface']

    # ====== PLOT 1: Main diagnostics (4 panels) ======
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel (a): 2D contour of d_s(tau, sigma)
    ax = axes[0, 0]
    TAU, SIGMA = np.meshgrid(tau, np.log10(sigma), indexing='ij')
    levels = np.arange(0, 10, 0.5)
    cf = ax.contourf(TAU, SIGMA, d_s, levels=levels, cmap='viridis', extend='both')
    plt.colorbar(cf, ax=ax, label='d_s')

    # Mark d_s = 4 contour
    ax.contour(TAU, SIGMA, d_s, levels=[4.0], colors='red', linewidths=2, linestyles='--')
    # Mark d_s = 8 contour
    ax.contour(TAU, SIGMA, d_s, levels=[8.0], colors='white', linewidths=1.5, linestyles='-')

    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('log10(sigma)')
    ax.set_title('S-2: Spectral Dimension d_s(tau, sigma)')

    # Panel (b): d_s at sigma=1.0 (1D slice)
    ax = axes[0, 1]
    ax.plot(tau, results['d_s_sigma1'], 'bo-', markersize=5, lw=1.5,
            label='d_s(tau, sigma=1.0)')
    ax.axhline(y=8, color='gray', ls='--', lw=1, label='d_s = 8 (homogeneous)')
    ax.axhline(y=4, color='red', ls='--', lw=1, label='d_s = 4 (CDT target)')
    ax.axvspan(0.15, 0.30, alpha=0.1, color='green', label='Target zone')

    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('Spectral dimension d_s')
    ax.set_title('d_s(tau) at sigma = 1.0')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (c): d_s(tau=0, sigma) validation
    ax = axes[1, 0]
    ax.semilogx(sigma, results['d_s_tau0'], 'b-', lw=2, label='d_s(tau=0, sigma)')
    ax.axhline(y=8, color='red', ls='--', lw=1, label='Expected = 8')

    # Also show d_s at tau=1.0 and tau=2.0
    idx_mid = len(tau) // 2
    ax.semilogx(sigma, d_s[idx_mid, :], 'g-', lw=1.5,
                label=f'd_s(tau={tau[idx_mid]:.1f}, sigma)')
    ax.semilogx(sigma, d_s[-1, :], 'r-', lw=1.5,
                label=f'd_s(tau={tau[-1]:.1f}, sigma)')

    ax.set_xlabel('Diffusion time sigma')
    ax.set_ylabel('Spectral dimension d_s')
    ax.set_title('d_s vs sigma at Fixed tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 12)

    # Panel (d): d_s = 4 crossing location
    ax = axes[1, 1]
    mask = ~np.isnan(results['d_s_4_sigma'])
    if np.any(mask):
        ax.semilogy(tau[mask], results['d_s_4_sigma'][mask], 'ro-', markersize=6, lw=1.5,
                    label='d_s = 4 crossing sigma')
        ax.set_xlabel('Jensen parameter tau')
        ax.set_ylabel('sigma at d_s = 4 crossing')
        ax.set_title('Location of d_s = 4 Crossing')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No d_s = 4 crossing found\nin the (tau, sigma) plane',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
        ax.set_title('d_s = 4 Crossing: NOT FOUND')

    # Also show d_s range
    ax_twin = ax.twinx()
    ax_twin.fill_between(tau, results['d_s_min'], results['d_s_max'],
                         alpha=0.15, color='blue', label='d_s range')
    ax_twin.set_ylabel('d_s range', color='blue')
    ax_twin.tick_params(axis='y', labelcolor='blue')

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_spectral_dimension.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")

    # ====== PLOT 2: d_s flow curves at multiple tau ======
    fig, ax = plt.subplots(figsize=(10, 7))

    cmap = plt.cm.viridis
    for i, t in enumerate(tau):
        color = cmap(i / (len(tau) - 1))
        ax.semilogx(sigma, d_s[i, :], '-', color=color, lw=1,
                    alpha=0.7, label=f'tau={t:.1f}' if i % 4 == 0 else None)

    ax.axhline(y=8, color='black', ls='--', lw=1.5, label='d=8')
    ax.axhline(y=4, color='red', ls='--', lw=1.5, label='d=4')
    ax.axhline(y=2, color='orange', ls='--', lw=1, alpha=0.5, label='d=2')

    ax.set_xlabel('Diffusion time sigma')
    ax.set_ylabel('Spectral dimension d_s')
    ax.set_title('Spectral Dimension Flow d_s(sigma) at Various tau')
    ax.legend(fontsize=7, ncol=2)
    ax.set_ylim(0, 12)
    ax.grid(True, alpha=0.3)

    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=0, vmax=2))
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label='tau')

    path = os.path.join(output_dir, 's19a_spectral_dimension_flow.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    DATA_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')

    print("S-2: Spectral Dimension d_s(tau, sigma)")
    print(f"  Loading: {DATA_PATH}")

    data = load_sweep_data(DATA_PATH)

    print("\n--- Computing spectral dimension surface ---")
    results = analyze_spectral_dimension(data)

    print(f"\n{'='*70}")
    print("RESULTS SUMMARY")
    print(f"{'='*70}")

    print(f"\n  d_s at sigma=1.0:")
    for i, tau in enumerate(results['tau_values']):
        ds1 = results['d_s_sigma1'][i]
        ds4_s = results['d_s_4_sigma'][i]
        ds4_str = f"sigma={ds4_s:.3f}" if not np.isnan(ds4_s) else "NO CROSSING"
        print(f"    tau={tau:.2f}: d_s = {ds1:.4f}, d_s=4 crossing: {ds4_str}")

    # CLOSURE/CONFIRM
    ds_range = results['d_s_sigma1']
    ds_min = np.min(ds_range)
    ds_max = np.max(ds_range)

    print(f"\n  d_s range at sigma=1.0: [{ds_min:.4f}, {ds_max:.4f}]")

    has_ds4_crossing = np.any(~np.isnan(results['d_s_4_sigma']))

    print(f"\n{'='*70}")
    print("CLOSURE / CONFIRM ASSESSMENT")
    print(f"{'='*70}")

    if ds_max - ds_min < 0.5:
        print("  >> CLOSED: d_s(tau, sigma) ~ const. No dimensional reduction.")
        print("  >> CDT connection fails.")
    elif has_ds4_crossing:
        crossing_taus = results['tau_values'][~np.isnan(results['d_s_4_sigma'])]
        print(f"  >> CONFIRM: d_s = 4 crossing found at tau values: {crossing_taus}")
        print("  >> Direct CDT connection!")
    else:
        print(f"  >> INTERMEDIATE: d_s varies from {ds_min:.2f} to {ds_max:.2f}")
        print("  >> Dimensional reduction present but d_s = 4 not reached.")

    print("\n--- Generating plots ---")
    plot_results(results, SCRIPT_DIR)

    print("\nS-2 complete.")
