"""
Session 19a — S-3: Spectral Entropy + Heat Capacity
====================================================

Thermodynamic spectral diagnostics:
    Z(tau, beta) = Sum_n mult_n * exp(-beta * lambda_n(tau)^2)
    p_n(tau, beta) = mult_n * exp(-beta * lambda_n^2) / Z
    S(tau, beta) = -Sum_n p_n * log(p_n)              [Shannon entropy]
    C(tau, beta) = beta^2 * (<lambda^4> - <lambda^2>^2)  [heat capacity]

dS/dtau = rate of spectral complexification. Maximum identifies MEPP selected state.
Peak in C(tau) at fixed beta = lambda-point analog (second-order phase transition).

Closure: dS/dtau monotonically increasing/decreasing with no extremum.
Confirm: Peak in C(tau) at tau_c corroborating other diagnostics.

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
# SPECTRAL THERMODYNAMICS
# =============================================================================

def compute_partition_function(eigenvalues, multiplicities, beta):
    """
    Compute spectral partition function Z = Sum mult_n * exp(-beta * lambda_n^2).

    Args:
        eigenvalues: array of |lambda_n|
        multiplicities: array of multiplicities
        beta: inverse temperature

    Returns:
        Z: partition function value
    """
    lam2 = eigenvalues ** 2
    return np.sum(multiplicities * np.exp(-beta * lam2))


def compute_spectral_thermodynamics(eigenvalues, multiplicities, beta):
    """
    Compute spectral thermodynamic quantities at a single (tau, beta).

    Returns:
        Z: partition function
        S: Shannon entropy
        C: heat capacity
        lam2_mean: <lambda^2>
        lam4_mean: <lambda^4>
    """
    lam2 = eigenvalues ** 2
    lam4 = eigenvalues ** 4

    # Boltzmann weights
    boltz = multiplicities * np.exp(-beta * lam2)
    Z = np.sum(boltz)

    if Z <= 0 or not np.isfinite(Z):
        return Z, np.nan, np.nan, np.nan, np.nan

    # Probabilities
    p = boltz / Z

    # Shannon entropy: S = -Sum p_n log(p_n)
    # Avoid log(0) by filtering
    mask = p > 1e-300
    S = -np.sum(p[mask] * np.log(p[mask]))

    # Expectation values
    lam2_mean = np.sum(p * lam2)
    lam4_mean = np.sum(p * lam4)

    # Heat capacity: C = beta^2 * (<lambda^4> - <lambda^2>^2)
    C = beta ** 2 * (lam4_mean - lam2_mean ** 2)

    return Z, S, C, lam2_mean, lam4_mean


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_entropy_capacity(data):
    """
    Full entropy + heat capacity analysis over (tau, beta) grid.
    """
    tau_values = data['tau_values']
    n_tau = len(tau_values)

    # Beta range
    beta_values = np.logspace(-2, 2, 50)
    n_beta = len(beta_values)

    # Storage
    Z_grid = np.zeros((n_tau, n_beta))
    S_grid = np.zeros((n_tau, n_beta))
    C_grid = np.zeros((n_tau, n_beta))
    lam2_grid = np.zeros((n_tau, n_beta))

    print(f"  Computing thermodynamics at {n_tau} x {n_beta} = {n_tau * n_beta} points...")

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]

        for j, beta in enumerate(beta_values):
            Z, S, C, lam2_m, lam4_m = compute_spectral_thermodynamics(evals, mults, beta)
            Z_grid[i, j] = Z
            S_grid[i, j] = S
            C_grid[i, j] = C
            lam2_grid[i, j] = lam2_m

        if i % 5 == 0 or i == n_tau - 1:
            idx_b1 = np.argmin(np.abs(beta_values - 1.0))
            print(f"    tau={tau:.2f}: S(beta=1)={S_grid[i, idx_b1]:.4f}, "
                  f"C(beta=1)={C_grid[i, idx_b1]:.4f}")

    # --- dS/dtau ---
    dtau = tau_values[1] - tau_values[0]
    dS_dtau = np.zeros((n_tau, n_beta))
    for j in range(n_beta):
        dS_dtau[:, j] = np.gradient(S_grid[:, j], dtau)

    # --- Find extrema in dS/dtau and C at each beta ---
    tau_peak_dS = np.zeros(n_beta)
    tau_peak_C = np.zeros(n_beta)
    dS_max_val = np.zeros(n_beta)
    C_max_val = np.zeros(n_beta)

    for j in range(n_beta):
        # dS/dtau peak
        idx_max_dS = np.argmax(dS_dtau[:, j])
        tau_peak_dS[j] = tau_values[idx_max_dS]
        dS_max_val[j] = dS_dtau[idx_max_dS, j]

        # C peak
        idx_max_C = np.argmax(C_grid[:, j])
        tau_peak_C[j] = tau_values[idx_max_C]
        C_max_val[j] = C_grid[idx_max_C, j]

    # --- Representative beta slices ---
    beta_repr = [0.1, 1.0, 10.0]
    beta_repr_idx = [np.argmin(np.abs(beta_values - b)) for b in beta_repr]

    return {
        'tau_values': tau_values,
        'beta_values': beta_values,
        'Z_grid': Z_grid,
        'S_grid': S_grid,
        'C_grid': C_grid,
        'lam2_grid': lam2_grid,
        'dS_dtau': dS_dtau,
        'tau_peak_dS': tau_peak_dS,
        'tau_peak_C': tau_peak_C,
        'dS_max_val': dS_max_val,
        'C_max_val': C_max_val,
        'beta_repr': beta_repr,
        'beta_repr_idx': beta_repr_idx,
    }


def plot_results(results, output_dir):
    """Generate S-3 diagnostic plots."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    tau = results['tau_values']
    beta = results['beta_values']

    # ====== PLOT 1: Main diagnostics (2x2) ======
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel (a): S(tau) at representative beta values
    ax = axes[0, 0]
    for bidx, bval in zip(results['beta_repr_idx'], results['beta_repr']):
        ax.plot(tau, results['S_grid'][:, bidx], 'o-', markersize=4, lw=1.5,
                label=f'beta={bval}')
    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('Shannon entropy S')
    ax.set_title('S-3a: Spectral Entropy S(tau)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (b): dS/dtau at representative beta values
    ax = axes[0, 1]
    for bidx, bval in zip(results['beta_repr_idx'], results['beta_repr']):
        ds = results['dS_dtau'][:, bidx]
        ax.plot(tau, ds, 'o-', markersize=4, lw=1.5, label=f'beta={bval}')
        # Mark peak
        ipeak = np.argmax(ds)
        ax.plot(tau[ipeak], ds[ipeak], '*', markersize=12, color='red')

    ax.axhline(y=0, color='gray', ls=':', lw=0.8)
    ax.axvspan(0.15, 0.30, alpha=0.1, color='green', label='Target zone')
    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('dS/dtau')
    ax.set_title('S-3b: Entropy Production Rate')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (c): C(tau) at representative beta values
    ax = axes[1, 0]
    for bidx, bval in zip(results['beta_repr_idx'], results['beta_repr']):
        C = results['C_grid'][:, bidx]
        ax.plot(tau, C, 'o-', markersize=4, lw=1.5, label=f'beta={bval}')
        # Mark peak
        ipeak = np.argmax(C)
        ax.plot(tau[ipeak], C[ipeak], '*', markersize=12, color='red')

    ax.axvspan(0.15, 0.30, alpha=0.1, color='green', label='Target zone')
    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('Heat capacity C')
    ax.set_title('S-3c: Spectral Heat Capacity C(tau)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (d): Beta-independence check — tau_peak vs beta
    ax = axes[1, 1]
    ax.semilogx(beta, results['tau_peak_dS'], 'b-', lw=1.5, label='tau at max dS/dtau')
    ax.semilogx(beta, results['tau_peak_C'], 'r-', lw=1.5, label='tau at max C')
    ax.axhspan(0.15, 0.30, alpha=0.1, color='green', label='Target zone')
    ax.set_xlabel('Inverse temperature beta')
    ax.set_ylabel('tau at peak')
    ax.set_title('S-3d: Beta-Independence Check')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.1)

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_entropy_capacity.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")

    # ====== PLOT 2: 2D heat maps of S and C ======
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    TAU, LOG_BETA = np.meshgrid(tau, np.log10(beta), indexing='ij')

    # S(tau, beta)
    ax = axes[0]
    cf = ax.contourf(TAU, LOG_BETA, results['S_grid'], levels=20, cmap='viridis')
    plt.colorbar(cf, ax=ax, label='S')
    ax.set_xlabel('tau')
    ax.set_ylabel('log10(beta)')
    ax.set_title('Shannon Entropy S(tau, beta)')

    # C(tau, beta)
    ax = axes[1]
    # Clip C for visualization (can be very large at small beta)
    C_clip = np.clip(results['C_grid'], 0, np.percentile(results['C_grid'], 99))
    cf = ax.contourf(TAU, LOG_BETA, C_clip, levels=20, cmap='hot')
    plt.colorbar(cf, ax=ax, label='C')
    ax.set_xlabel('tau')
    ax.set_ylabel('log10(beta)')
    ax.set_title('Heat Capacity C(tau, beta)')

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_entropy_capacity_2d.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    DATA_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')

    print("S-3: Spectral Entropy + Heat Capacity")
    print(f"  Loading: {DATA_PATH}")

    data = load_sweep_data(DATA_PATH)

    print("\n--- Computing entropy and heat capacity ---")
    results = analyze_entropy_capacity(data)

    print(f"\n{'='*70}")
    print("RESULTS SUMMARY")
    print(f"{'='*70}")

    print(f"\n  Entropy S(tau) at representative beta:")
    for bidx, bval in zip(results['beta_repr_idx'], results['beta_repr']):
        S_vals = results['S_grid'][:, bidx]
        print(f"    beta={bval}: S range [{np.min(S_vals):.4f}, {np.max(S_vals):.4f}], "
              f"tau at max dS/dtau = {results['tau_peak_dS'][bidx]:.2f}")

    print(f"\n  Heat capacity C(tau) peaks:")
    for bidx, bval in zip(results['beta_repr_idx'], results['beta_repr']):
        C_vals = results['C_grid'][:, bidx]
        ipeak = np.argmax(C_vals)
        print(f"    beta={bval}: C_max={C_vals[ipeak]:.4f} at tau={results['tau_values'][ipeak]:.2f}")

    print(f"\n  Beta-independence of tau_peak:")
    # Check if peak tau is stable across beta
    tau_peaks_dS = results['tau_peak_dS']
    tau_peaks_C = results['tau_peak_C']
    dS_std = np.std(tau_peaks_dS)
    C_std = np.std(tau_peaks_C)
    print(f"    dS/dtau peak: mean tau = {np.mean(tau_peaks_dS):.3f}, std = {dS_std:.3f}")
    print(f"    C peak:       mean tau = {np.mean(tau_peaks_C):.3f}, std = {C_std:.3f}")

    # CLOSURE/CONFIRM
    print(f"\n{'='*70}")
    print("CLOSURE / CONFIRM ASSESSMENT")
    print(f"{'='*70}")

    # Check if dS/dtau has a genuine maximum (not at boundary)
    idx_b1 = results['beta_repr_idx'][1]  # beta=1.0
    dS = results['dS_dtau'][:, idx_b1]
    ipeak = np.argmax(dS)
    at_boundary = (ipeak == 0 or ipeak == len(dS) - 1)

    if at_boundary:
        print("  >> CLOSED: dS/dtau peak is at boundary (tau=0 or tau=2.0).")
        print("  >> No interior extremum. Entropy picture adds nothing beyond V_eff.")
    else:
        tau_peak = results['tau_values'][ipeak]
        print(f"  >> Peak in dS/dtau at tau = {tau_peak:.2f} (interior point)")
        if 0.15 <= tau_peak <= 0.30:
            print(f"  >> CONFIRM: dS/dtau peak at tau = {tau_peak:.2f} in target zone!")
        else:
            print(f"  >> INTERMEDIATE: Peak exists but outside target zone [0.15, 0.30].")

    # Check C(tau) peak
    C_b1 = results['C_grid'][:, idx_b1]
    ipeak_C = np.argmax(C_b1)
    at_boundary_C = (ipeak_C == 0 or ipeak_C == len(C_b1) - 1)

    if not at_boundary_C:
        tau_peak_C = results['tau_values'][ipeak_C]
        print(f"  >> C(tau) peak at tau = {tau_peak_C:.2f}")
        if dS_std < 0.3:
            print(f"  >> Beta-independent: dS peak std = {dS_std:.3f}")
        else:
            print(f"  >> Beta-DEPENDENT: dS peak std = {dS_std:.3f} (reduces predictive power)")

    print("\n--- Generating plots ---")
    plot_results(results, SCRIPT_DIR)

    print("\nS-3 complete.")
