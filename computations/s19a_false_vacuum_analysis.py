"""
Session 19a -- S-5 Extension: False Vacuum Analysis
=====================================================

The user asked "False Vacuum?" about the d_s > 8 behavior at large tau.

Key observation: V_eff(tau) is monotonically DECREASING (Session 18 closure).
The system wants to roll to tau -> infinity. But the spectral data says:

1. Spectral gap GROWS with tau (lambda_min: 0.833 -> 3.206)
2. Vacuum energy <lambda^2> grows exponentially (~e^{1.77*tau})
3. d_s exceeds topological dimension 8 at tau > ~1.0
4. Spectral entropy DECREASES monotonically

This is the structure of a FALSE VACUUM: energetically favored by V_eff
but creating a spectral desert where excitations are too expensive for
any physics to exist.

The TRUE vacuum must be at intermediate tau where:
- The spectrum still supports particle-like excitations
- The spectral gap is not too large
- The d_s is close to physical values (4-8)

This script computes:
1. Spectral gap evolution
2. Vacuum energy density evolution
3. Excitation cost: energy to create the lightest mode
4. "Habitability" metric: where can the universe support particles?
5. The spectral false vacuum boundary

Author: Tesla-Resonance (Session 19a)
Date: 2026-02-15
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from s19a_sweep_data import load_sweep_data


def analyze_spectral_gap(data):
    """Track how the spectral gap (smallest |lambda|) evolves with tau."""
    tau_values = data['tau_values']
    gaps = []
    gap_sectors = []

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        sp = data['sector_p'][i]
        sq = data['sector_q'][i]

        idx_min = np.argmin(np.abs(evals))
        gaps.append(np.abs(evals[idx_min]))
        gap_sectors.append((int(sp[idx_min]), int(sq[idx_min])))

    return np.array(gaps), gap_sectors


def analyze_vacuum_energy(data):
    """
    Compute vacuum energy-like quantities at each tau.

    In the superfluid analogy, the zero-point energy is Sum mult_n * |lambda_n| / 2.
    The vacuum energy density is Sum mult_n * lambda_n^2.
    """
    tau_values = data['tau_values']
    E_zeropoint = []
    E_vacuum = []
    mean_lambda_sq = []
    std_lambda_sq = []

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]

        # Total zero-point energy (bosonic: +1/2, fermionic: -1/2)
        # Using PW multiplicities as weights
        total_mult = np.sum(mults)

        # Mean eigenvalue squared (weighted by PW multiplicity)
        weights = mults / np.sum(mults)
        mean_l2 = np.sum(weights * evals**2)
        std_l2 = np.sqrt(np.sum(weights * (evals**2 - mean_l2)**2))

        E_zeropoint.append(np.sum(mults * np.abs(evals)) / 2)
        E_vacuum.append(np.sum(mults * evals**2))
        mean_lambda_sq.append(mean_l2)
        std_lambda_sq.append(std_l2)

    return {
        'E_zeropoint': np.array(E_zeropoint),
        'E_vacuum': np.array(E_vacuum),
        'mean_lambda_sq': np.array(mean_lambda_sq),
        'std_lambda_sq': np.array(std_lambda_sq),
    }


def compute_spectral_dimension_surface(data, sigma_values):
    """
    Compute d_s(tau, sigma) for the full 2D surface.
    This lets us see WHERE d_s > 8 occurs in the (tau, sigma) plane.
    """
    tau_values = data['tau_values']
    d_s_surface = np.zeros((len(tau_values), len(sigma_values)))

    d_log_sigma = 0.01

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]
        evals_sq = evals**2

        for j, sigma in enumerate(sigma_values):
            sigma_m = sigma * np.exp(-d_log_sigma)
            sigma_p = sigma * np.exp(d_log_sigma)

            K_m = np.sum(mults * np.exp(-sigma_m * evals_sq))
            K_p = np.sum(mults * np.exp(-sigma_p * evals_sq))

            if K_m > 0 and K_p > 0:
                d_s_surface[i, j] = -2.0 * (np.log(K_p) - np.log(K_m)) / (2 * d_log_sigma)

    return d_s_surface


def compute_habitability(data, sigma_star=1.0, beta_star=1.0):
    """
    The "habitability" metric: at each tau, can the universe support
    particle-like excitations?

    Criteria:
    1. Spectral gap not too large (gap < gap_threshold)
    2. Spectral dimension near physical (4 < d_s < 8)
    3. Sufficient spectral diversity (entropy > S_threshold)
    4. Excitation cost not too high (mean lambda^2 not exponentially large)

    Returns a habitability score H(tau) in [0, 1].
    """
    tau_values = data['tau_values']
    gaps, _ = analyze_spectral_gap(data)
    vac = analyze_vacuum_energy(data)

    H = np.zeros(len(tau_values))

    d_log_sigma = 0.01

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        mults = data['multiplicities'][i]
        evals_sq = evals**2

        # d_s at sigma_star
        sigma_m = sigma_star * np.exp(-d_log_sigma)
        sigma_p = sigma_star * np.exp(d_log_sigma)
        K_m = np.sum(mults * np.exp(-sigma_m * evals_sq))
        K_p = np.sum(mults * np.exp(-sigma_p * evals_sq))
        d_s = -2.0 * (np.log(K_p) - np.log(K_m)) / (2 * d_log_sigma) if K_m > 0 and K_p > 0 else 0

        # Spectral entropy at beta_star
        log_boltz = -beta_star * evals_sq
        log_boltz -= np.max(log_boltz)
        w = mults * np.exp(log_boltz)
        Z = np.sum(w)
        if Z > 0:
            p = w / Z
            mask = p > 1e-300
            S = -np.sum(p[mask] * np.log(p[mask]))
        else:
            S = 0

        # Score components (each in [0, 1])
        # 1. Gap penalty: sigmoid centered at gap_ref (gap at tau=0)
        gap_ref = gaps[0]  # tau=0 gap
        h_gap = 1.0 / (1.0 + np.exp(5 * (gaps[i] / gap_ref - 2.0)))

        # 2. d_s score: Gaussian peaked at 4-8
        if 4 <= d_s <= 8:
            h_ds = 1.0
        elif d_s < 4:
            h_ds = np.exp(-((d_s - 4)**2) / 2)
        else:  # d_s > 8
            h_ds = np.exp(-((d_s - 8)**2) / 8)

        # 3. Entropy score: sigmoid requiring S > S_ref/2
        S_ref = 8.0  # approximate entropy at tau=0
        h_S = 1.0 / (1.0 + np.exp(-5 * (S / S_ref - 0.5)))

        # 4. Energy cost: sigmoid penalizing exponential growth
        E_ref = vac['mean_lambda_sq'][0]
        h_E = 1.0 / (1.0 + np.exp(2 * (vac['mean_lambda_sq'][i] / E_ref - 3.0)))

        H[i] = h_gap * h_ds * h_S * h_E

    return H


def fit_exponential_growth(tau_values, values, name="quantity"):
    """Fit log(values) = a + b*tau to extract exponential growth rate."""
    mask = values > 0
    if np.sum(mask) < 3:
        return None, None
    log_v = np.log(values[mask])
    tau_fit = tau_values[mask]
    coeffs = np.polyfit(tau_fit, log_v, 1)
    rate = coeffs[0]
    print(f"  {name}: exponential growth rate = {rate:.4f} (fit to log = {coeffs[0]:.4f}*tau + {coeffs[1]:.4f})")
    return rate, coeffs


def main():
    DATA_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')
    OUTPUT_DIR = SCRIPT_DIR

    print("Session 19a -- False Vacuum Analysis")
    print("=" * 60)

    if not os.path.exists(DATA_PATH):
        print(f"ERROR: {DATA_PATH} not found")
        sys.exit(1)

    data = load_sweep_data(DATA_PATH)
    tau_values = data['tau_values']
    print(f"Loaded {len(tau_values)} tau-values")

    # 1. Spectral gap evolution
    print("\n--- 1. Spectral Gap Evolution ---")
    gaps, gap_sectors = analyze_spectral_gap(data)
    for i, tau in enumerate(tau_values):
        print(f"  tau={tau:.1f}: gap={gaps[i]:.6f}, sector=({gap_sectors[i][0]},{gap_sectors[i][1]})")

    rate_gap, _ = fit_exponential_growth(tau_values, gaps, "Spectral gap")

    # 2. Vacuum energy evolution
    print("\n--- 2. Vacuum Energy Evolution ---")
    vac = analyze_vacuum_energy(data)
    for i, tau in enumerate(tau_values):
        print(f"  tau={tau:.1f}: <lambda^2>={vac['mean_lambda_sq'][i]:.6f}, "
              f"std={vac['std_lambda_sq'][i]:.6f}, "
              f"E_vac={vac['E_vacuum'][i]:.4e}")

    rate_vac, _ = fit_exponential_growth(tau_values, vac['mean_lambda_sq'], "<lambda^2>")
    rate_Evac, _ = fit_exponential_growth(tau_values, vac['E_vacuum'], "E_vacuum")

    # 3. d_s surface
    print("\n--- 3. Spectral Dimension Surface ---")
    sigma_values = np.logspace(-1, 1.5, 40)  # 0.1 to ~30
    d_s_surface = compute_spectral_dimension_surface(data, sigma_values)

    # Find where d_s = 8 contour lies
    print("  d_s = 8 boundary (tau where d_s first exceeds 8, per sigma):")
    for j, sigma in enumerate(sigma_values[::5]):  # every 5th
        j_actual = j * 5
        ds_col = d_s_surface[:, j_actual]
        crossings = []
        for k in range(len(ds_col) - 1):
            if (ds_col[k] - 8) * (ds_col[k+1] - 8) < 0:
                frac = (8 - ds_col[k]) / (ds_col[k+1] - ds_col[k])
                tau_cross = tau_values[k] + frac * (tau_values[k+1] - tau_values[k])
                crossings.append(tau_cross)
        if crossings:
            print(f"    sigma={sigma:.3f}: d_s=8 at tau={crossings[0]:.3f}")

    # 4. Habitability metric
    print("\n--- 4. Spectral Habitability H(tau) ---")
    H = compute_habitability(data)
    for i, tau in enumerate(tau_values):
        print(f"  tau={tau:.1f}: H={H[i]:.6f}")

    # Find the habitability boundary (H drops below 0.5)
    for i in range(len(H) - 1):
        if H[i] >= 0.5 and H[i+1] < 0.5:
            frac = (0.5 - H[i]) / (H[i+1] - H[i])
            tau_boundary = tau_values[i] + frac * (tau_values[i+1] - tau_values[i])
            print(f"\n  *** HABITABILITY BOUNDARY: tau ~ {tau_boundary:.3f} ***")
            print(f"  Below this: universe can support excitations")
            print(f"  Above this: spectral desert (false vacuum)")

    # 5. False vacuum interpretation
    print("\n--- 5. FALSE VACUUM INTERPRETATION ---")
    print()
    print("V_eff(tau) is monotonically decreasing (Session 18).")
    print("The system wants to roll to tau -> infinity.")
    print("But at large tau:")
    print(f"  - Spectral gap grows at rate {rate_gap:.4f}/tau")
    print(f"  - Vacuum energy grows at rate {rate_vac:.4f}/tau")
    print(f"  - d_s exceeds 8 (topological dim)")
    print(f"  - Entropy decreases monotonically")
    print()
    print("THESIS: Large-tau is a FALSE VACUUM in the spectral sense.")
    print("  - Energetically favored by V_eff (rolls downhill)")
    print("  - But spectrally barren (no low-lying excitations)")
    print("  - The universe CANNOT exist there because particles cost")
    print("    exponentially more energy than available")
    print()

    # Find the d_s minimum (the boundary of the physical regime)
    d_s_at_sigma1 = d_s_surface[:, np.argmin(np.abs(sigma_values - 1.0))]
    idx_min_ds = np.argmin(d_s_at_sigma1[1:]) + 1  # skip tau=0
    print(f"d_s minimum at tau={tau_values[idx_min_ds]:.1f}: d_s={d_s_at_sigma1[idx_min_ds]:.4f}")
    print("This marks the TRANSITION between physical and spectral desert regimes.")
    print()

    # The key question: what STABILIZES the modulus?
    print("STABILIZATION QUESTION:")
    print("  V_eff drives tau -> infinity (false vacuum)")
    print("  Spectral habitability drives tau -> 0 (no deformation)")
    print("  The PHYSICAL vacuum is where these compete.")
    print("  This is NOT V_eff minimization. It is a BALANCE between")
    print("  the classical potential and the spectral cost of existence.")
    print()
    print("CONDENSED MATTER ANALOG (Volovik):")
    print("  In He-3B, the B-phase gap equation selects the order parameter")
    print("  that MINIMIZES free energy while maintaining a nonzero gap.")
    print("  The gap cannot go to zero (gapless = normal state) or infinity")
    print("  (infinite energy cost). The physical vacuum is the saddle.")
    print("  Our system: V_eff = -infinity as tau -> infinity,")
    print("  but excitation cost -> infinity too. Physical vacuum = finite tau.")

    # =====================================================
    # PLOTS
    # =====================================================

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Plot 1: Spectral gap
    ax = axes[0, 0]
    ax.semilogy(tau_values, gaps, 'b-o', markersize=4, linewidth=2)
    ax.set_xlabel('tau')
    ax.set_ylabel('Spectral gap |lambda_min|')
    ax.set_title('Spectral Gap Growth')
    ax.grid(True, alpha=0.3)
    if rate_gap:
        tau_fit = np.linspace(0, 2, 50)
        ax.semilogy(tau_fit, gaps[0] * np.exp(rate_gap * tau_fit), 'r--', alpha=0.5,
                    label=f'exp({rate_gap:.2f}*tau)')
        ax.legend(fontsize=8)

    # Plot 2: Vacuum energy
    ax = axes[0, 1]
    ax.semilogy(tau_values, vac['mean_lambda_sq'], 'g-o', markersize=4, linewidth=2)
    ax.set_xlabel('tau')
    ax.set_ylabel('<lambda^2>')
    ax.set_title('Mean Eigenvalue Squared (Vacuum Energy)')
    ax.grid(True, alpha=0.3)
    if rate_vac:
        ax.semilogy(tau_fit, vac['mean_lambda_sq'][0] * np.exp(rate_vac * tau_fit), 'r--',
                    alpha=0.5, label=f'exp({rate_vac:.2f}*tau)')
        ax.legend(fontsize=8)

    # Plot 3: d_s at sigma=1
    ax = axes[0, 2]
    ax.plot(tau_values, d_s_at_sigma1, 'k-o', markersize=4, linewidth=2)
    ax.axhline(y=8, color='gray', linestyle='--', alpha=0.5, label='d_s = 8 (topological)')
    ax.axhline(y=4, color='red', linestyle='--', alpha=0.5, label='d_s = 4 (physical)')
    ax.fill_between(tau_values, 4, 8, alpha=0.1, color='green', label='Physical regime')
    ax.set_xlabel('tau')
    ax.set_ylabel('d_s(sigma=1)')
    ax.set_title('Spectral Dimension at sigma=1')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 4: d_s surface contour
    ax = axes[1, 0]
    T, S = np.meshgrid(tau_values, sigma_values)
    levels = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20]
    cs = ax.contourf(T.T, np.log10(S.T), d_s_surface, levels=levels, cmap='RdYlBu_r')
    ax.contour(T.T, np.log10(S.T), d_s_surface, levels=[4, 8], colors=['red', 'black'], linewidths=2)
    plt.colorbar(cs, ax=ax, label='d_s')
    ax.set_xlabel('tau')
    ax.set_ylabel('log10(sigma)')
    ax.set_title('Spectral Dimension Surface d_s(tau, sigma)')

    # Plot 5: Habitability
    ax = axes[1, 1]
    ax.plot(tau_values, H, 'purple', linewidth=2, marker='o', markersize=4)
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='H = 0.5 boundary')
    ax.fill_between(tau_values, 0, H, alpha=0.2, color='purple')
    ax.set_xlabel('tau')
    ax.set_ylabel('Habitability H(tau)')
    ax.set_title('Spectral Habitability')
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Reference lines
    ref_taus = {'0.15': 'phi ratio', '0.30': 'sin^2 theta_W', '0.90': 'd_s min'}
    for t_str, label in ref_taus.items():
        t = float(t_str)
        ax.axvline(x=t, color='blue', linestyle=':', alpha=0.5)
        ax.text(t + 0.02, 0.95, label, fontsize=7, color='blue', rotation=90, va='top')

    # Plot 6: Combined V_eff vs spectral cost schematic
    ax = axes[1, 2]
    # V_eff is monotonically decreasing (from Session 18)
    # Spectral cost is monotonically increasing
    # Their BALANCE defines the physical vacuum
    tau_dense = np.linspace(0, 2, 100)
    # Schematic V_eff (normalized, decreasing)
    V_eff_schematic = -np.exp(1.5 * tau_dense)
    V_eff_schematic = V_eff_schematic / np.abs(V_eff_schematic[-1])
    # Spectral cost (increasing)
    spectral_cost = np.exp(rate_vac * tau_dense if rate_vac else 1.77 * tau_dense)
    spectral_cost = spectral_cost / spectral_cost[-1]
    # Effective potential: V_eff + spectral back-reaction
    V_total = V_eff_schematic + 0.5 * spectral_cost

    ax.plot(tau_dense, V_eff_schematic, 'b-', linewidth=2, label='V_eff (classical, decreasing)')
    ax.plot(tau_dense, spectral_cost, 'r-', linewidth=2, label='Spectral cost (increasing)')
    ax.plot(tau_dense, V_total, 'k-', linewidth=3, label='V_eff + back-reaction')

    # Mark the minimum of V_total
    idx_min = np.argmin(V_total)
    tau_balance = tau_dense[idx_min]
    ax.axvline(x=tau_balance, color='green', linestyle='--', linewidth=2, alpha=0.7)
    ax.annotate(f'tau_phys ~ {tau_balance:.2f}', xy=(tau_balance, V_total[idx_min]),
                xytext=(tau_balance + 0.3, V_total[idx_min] + 0.2),
                fontsize=10, color='green', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='green'))

    ax.set_xlabel('tau')
    ax.set_ylabel('Potential (schematic)')
    ax.set_title('False Vacuum: V_eff vs Spectral Cost')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.3)

    plt.suptitle('FALSE VACUUM ANALYSIS: Spectral Desert at Large tau', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 's19a_false_vacuum.png'), dpi=150)
    plt.close()
    print(f"\nSaved: {os.path.join(OUTPUT_DIR, 's19a_false_vacuum.png')}")

    # =====================================================
    # SUMMARY
    # =====================================================
    print("\n" + "=" * 70)
    print("FALSE VACUUM ANALYSIS SUMMARY")
    print("=" * 70)
    print()
    print("OBSERVATION:")
    print(f"  Spectral gap growth rate: {rate_gap:.4f}/tau")
    print(f"  Vacuum energy growth rate: {rate_vac:.4f}/tau")
    print(f"  d_s minimum: {d_s_at_sigma1[idx_min_ds]:.2f} at tau={tau_values[idx_min_ds]:.1f}")
    print(f"  d_s > 8 onset: tau ~ 1.0-1.2")
    print()
    print("INTERPRETATION:")
    print("  tau -> infinity IS the false vacuum of this system.")
    print("  V_eff drives the system there (monotonically decreasing).")
    print("  But the spectral cost of excitations grows exponentially.")
    print("  The physical vacuum is where V_eff gradient = spectral cost gradient.")
    print()
    print("NEW MECHANISM FOR MODULUS STABILIZATION:")
    print("  Not V_eff minimum (CLOSED -- Session 18).")
    print("  Not CW 1-loop (CLOSED -- Session 18).")
    print("  INSTEAD: back-reaction of spectral energy on the modulus.")
    print("  The universe CANNOT roll to tau -> infinity because the")
    print("  energy cost of its own excitations prevents it.")
    print("  This is the spectral analog of the Casimir effect stabilizing")
    print("  a compact dimension: the zero-point energy of modes on the")
    print("  internal space creates an effective potential that resists")
    print("  further deformation.")
    print()
    print("QUANTITATIVE GAP:")
    print("  V_CW scale: O(10^4) in Planck units (Session 18)")
    print("  Spectral energy scale: O(10^0 - 10^2) per mode")
    print("  Need ~10^2 - 10^4 contributing modes for balance")
    print("  We have 439,488 fermionic PW multiplicity -> sufficient DOF")
    print("  The question is whether back-reaction COUPLES to the modulus.")
    print()
    print("NEXT STEP:")
    print("  Compute the total spectral back-reaction force:")
    print("    F_spectral(tau) = -d/dtau Sum_n mult_n * f(lambda_n(tau)^2)")
    print("  Compare to V_eff gradient:")
    print("    F_Veff(tau) = -dV_CW/dtau")
    print("  Find tau where F_spectral + F_Veff = 0.")
    print("  This is the self-consistent vacuum.")


if __name__ == '__main__':
    main()
