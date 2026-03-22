"""
SESSION 28a COMPUTATION S-2: M_max vs C_2 DISPERSION RELATION
==============================================================

Plot the BCS maximum kernel eigenvalue M_max as a function of the quadratic
Casimir C_2(p,q) across all 9 Peter-Weyl sectors, at fixed mu/lambda_min
values. This maps the "dispersion relation" of the BCS instability across
representations.

Physics:
  The quadratic Casimir of SU(3) for the (p,q) irrep is:
    C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3

  This is the eigenvalue of the quadratic Casimir operator, analogous to
  k^2 for plane waves. If the BCS instability is phonon-like, we expect:
    M_max ~ f(C_2) for some universal function f

  Specifically:
    - M_max monotonically decreasing with C_2: instability strongest for
      lowest representations, consistent with phonon interpretation
      (long-wavelength modes condense first)
    - M_max ~ sqrt(C_2) for small C_2: acoustic branch (linear dispersion)
    - M_max ~ 1/C_2 for large C_2: gap-edge proximity effect

  The M_max = 1 threshold separates supercritical (condensation) from
  subcritical (no condensation) sectors.

Input:
  tier0-computation/s27_multisector_bcs.npz (M_max, sectors, tau, mu)

Output:
  tier0-computation/s28a_mmax_dispersion.npz
  tier0-computation/s28a_mmax_dispersion.png

Gate S-2: DIAGNOSTIC
  A phonon-like dispersion (M_max decreasing with C_2) is consistent
  with the phonon interpretation. An acoustic branch would be direct
  evidence of phononic structure. Anti-phononic (M_max increasing) or
  flat (no C_2 dependence) would argue against phonon picture.

Author: phonon-exflation-sim agent (Session 28a)
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import time

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# QUADRATIC CASIMIR
# =============================================================================

def casimir_C2(p, q):
    """
    Quadratic Casimir of SU(3) for irrep (p,q).

    C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3

    This is the standard normalization where the fundamental (1,0) has C_2 = 4/3.

    Verification:
      C_2(0,0) = 0          (trivial)
      C_2(1,0) = 4/3        (fundamental)
      C_2(0,1) = 4/3        (antifundamental)
      C_2(1,1) = 3          (adjoint)
      C_2(2,0) = 10/3       (symmetric tensor)
      C_2(3,0) = 6          (decuplet)
      C_2(2,1) = 16/3       (15-dimensional)

    Args:
        p, q: non-negative integers, irrep labels

    Returns:
        C2: float, quadratic Casimir value
    """
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0


# =============================================================================
# FIT FUNCTIONS
# =============================================================================

def power_law(C2, a, b):
    """M_max = a * C2^b"""
    return a * np.power(np.maximum(C2, 1e-10), b)


def acoustic_branch(C2, a, b):
    """M_max = a * sqrt(C2 + b)"""
    return a * np.sqrt(np.maximum(C2 + b, 0))


def exponential_decay(C2, a, b):
    """M_max = a * exp(-b * C2)"""
    return a * np.exp(-b * C2)


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main():
    print("=" * 72)
    print("SESSION 28a COMPUTATION S-2: M_max vs C_2 DISPERSION RELATION")
    print("=" * 72)
    t_start = time.time()

    # -------------------------------------------------------------------------
    # 1. Load data
    # -------------------------------------------------------------------------
    infile = os.path.join(OUTDIR, 's27_multisector_bcs.npz')
    print(f"\nLoading from {infile}")
    data = np.load(infile, allow_pickle=True)

    sectors = data['sectors']        # (9, 4): p, q, dim, mult
    tau_values = data['tau_values']   # (9,)
    mu_ratios = data['mu_ratios']    # (12,)
    M_max = data['M_max']           # (9, 9, 12) = (sector, tau, mu)
    lambda_min = data['lambda_min']  # (9, 9) = (sector, tau)
    F_cond = data['F_cond']         # (9, 9, 12)
    Delta_max = data['Delta_max']   # (9, 9, 12)

    n_sectors = len(sectors)
    n_tau = len(tau_values)
    n_mu = len(mu_ratios)

    print(f"  {n_sectors} sectors, {n_tau} tau values, {n_mu} mu ratios")
    print(f"  mu_ratios: {mu_ratios}")

    # -------------------------------------------------------------------------
    # 2. Compute Casimir C_2 for each sector
    # -------------------------------------------------------------------------
    C2 = np.array([casimir_C2(p, q) for p, q, _, _ in sectors])
    print(f"\nQuadratic Casimir C_2(p,q):")
    for i, (p, q, d, m) in enumerate(sectors):
        print(f"  ({p},{q}): C_2 = {C2[i]:.4f}, dim = {d}, mult = {m}")

    # Sort sectors by C_2
    sort_idx = np.argsort(C2)
    C2_sorted = C2[sort_idx]
    sector_labels = [f"({sectors[i,0]},{sectors[i,1]})" for i in sort_idx]

    # -------------------------------------------------------------------------
    # 3. Extract M_max vs C_2 at fixed (tau, mu/lambda_min)
    # -------------------------------------------------------------------------
    # Target tau values for plotting
    plot_taus = [0.15, 0.30, 0.50]
    tau_indices = []
    for t in plot_taus:
        idx = np.argmin(np.abs(tau_values - t))
        tau_indices.append(idx)
        print(f"  tau = {t:.2f} -> index {idx} (actual tau = {tau_values[idx]:.2f})")

    # Target mu/lambda_min values
    plot_mu_ratios = [0.0, 0.5, 1.0, 1.2]
    mu_indices = []
    for mr in plot_mu_ratios:
        idx = np.argmin(np.abs(mu_ratios - mr))
        mu_indices.append(idx)
        print(f"  mu/lambda_min = {mr:.1f} -> index {idx} "
              f"(actual ratio = {mu_ratios[idx]:.2f})")

    # -------------------------------------------------------------------------
    # 4. Analysis: monotonicity, dispersion type, threshold crossings
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("DISPERSION ANALYSIS")
    print("=" * 72)

    # For each (tau, mu), check if M_max is monotonically decreasing with C_2
    monotonicity = {}
    threshold_sectors = {}  # sectors above M_max=1

    for ti, tau_idx in enumerate(tau_indices):
        for mi, mu_idx in enumerate(mu_indices):
            tau_val = tau_values[tau_idx]
            mu_val = mu_ratios[mu_idx]
            key = (tau_val, mu_val)

            # M_max for each sector at this (tau, mu)
            M_vals = np.array([M_max[s, tau_idx, mu_idx] for s in sort_idx])

            # Check monotonicity with C_2
            diffs = np.diff(M_vals)
            n_inc = np.sum(diffs > 0.001)
            n_dec = np.sum(diffs < -0.001)
            n_flat = np.sum(np.abs(diffs) <= 0.001)

            if n_dec > 0 and n_inc == 0:
                mono = "DECREASING"
            elif n_inc > 0 and n_dec == 0:
                mono = "INCREASING"
            elif n_inc > 0 and n_dec > 0:
                mono = "NON-MONOTONIC"
            else:
                mono = "FLAT"

            monotonicity[key] = mono

            # Sectors above threshold
            above = [sector_labels[j] for j, M in enumerate(M_vals) if M > 1.0]
            threshold_sectors[key] = above

            print(f"\n  tau={tau_val:.2f}, mu/lmin={mu_val:.1f}: "
                  f"monotonicity = {mono}")
            print(f"    M_max values (sorted by C_2):")
            for j, s_idx in enumerate(sort_idx):
                p, q = sectors[s_idx, 0], sectors[s_idx, 1]
                marker = " ***" if M_vals[j] > 1.0 else ""
                print(f"      ({p},{q}) C_2={C2[s_idx]:.3f}: "
                      f"M_max={M_vals[j]:.4f}{marker}")
            if above:
                print(f"    Above M=1 threshold: {above}")
            else:
                print(f"    All sectors BELOW M=1 threshold")

    # -------------------------------------------------------------------------
    # 5. Fit dispersion relations at mu/lambda_min = 1.0 (most interesting)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("DISPERSION FIT at mu/lambda_min = 1.0")
    print("-" * 72)

    mu_1_idx = mu_indices[2]  # mu/lambda_min = 1.0
    fit_results = {}

    for ti, tau_idx in enumerate(tau_indices):
        tau_val = tau_values[tau_idx]
        M_vals = np.array([M_max[s, tau_idx, mu_1_idx] for s in sort_idx])

        # Exclude singlet (C_2 = 0) for power law fits
        mask = C2_sorted > 0
        C2_fit = C2_sorted[mask]
        M_fit = M_vals[mask]

        print(f"\n  tau = {tau_val:.2f}:")

        # Try power law: M ~ a * C2^b
        try:
            popt, pcov = curve_fit(power_law, C2_fit, M_fit,
                                   p0=[5.0, -0.5], maxfev=5000)
            a_pl, b_pl = popt
            residuals = M_fit - power_law(C2_fit, *popt)
            rmse_pl = np.sqrt(np.mean(residuals**2))
            print(f"    Power law: M = {a_pl:.3f} * C2^{b_pl:.3f}, "
                  f"RMSE = {rmse_pl:.4f}")
            fit_results[('power', tau_val)] = (a_pl, b_pl, rmse_pl)
        except (RuntimeError, ValueError) as e:
            print(f"    Power law fit failed: {e}")
            fit_results[('power', tau_val)] = (np.nan, np.nan, np.nan)

        # Try exponential decay: M ~ a * exp(-b * C2)
        try:
            popt, pcov = curve_fit(exponential_decay, C2_fit, M_fit,
                                   p0=[10.0, 0.3], maxfev=5000)
            a_exp, b_exp = popt
            residuals = M_fit - exponential_decay(C2_fit, *popt)
            rmse_exp = np.sqrt(np.mean(residuals**2))
            print(f"    Exponential: M = {a_exp:.3f} * exp(-{b_exp:.3f} * C2), "
                  f"RMSE = {rmse_exp:.4f}")
            fit_results[('exp', tau_val)] = (a_exp, b_exp, rmse_exp)
        except (RuntimeError, ValueError) as e:
            print(f"    Exponential fit failed: {e}")
            fit_results[('exp', tau_val)] = (np.nan, np.nan, np.nan)

        # Correlation coefficient: M_max vs C_2
        if len(C2_fit) >= 3:
            corr = np.corrcoef(C2_fit, M_fit)[0, 1]
            print(f"    Pearson r(C_2, M_max) = {corr:.4f}")

    # -------------------------------------------------------------------------
    # 6. Singlet vs non-singlet analysis
    # -------------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("SINGLET vs NON-SINGLET")
    print("-" * 72)

    singlet_idx = 0  # (0,0) always first
    for ti, tau_idx in enumerate(tau_indices):
        for mi, mu_idx in enumerate(mu_indices):
            tau_val = tau_values[tau_idx]
            mu_val = mu_ratios[mu_idx]
            M_singlet = M_max[singlet_idx, tau_idx, mu_idx]
            M_others = [M_max[s, tau_idx, mu_idx] for s in range(1, n_sectors)]
            M_max_nonsinglet = max(M_others)
            M_min_nonsinglet = min(M_others)
            print(f"  tau={tau_val:.2f}, mu/lmin={mu_val:.1f}: "
                  f"M_singlet={M_singlet:.4f}, "
                  f"M_nonsinglet=[{M_min_nonsinglet:.4f}, {M_max_nonsinglet:.4f}]")

    # -------------------------------------------------------------------------
    # 7. GATE VERDICT
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("GATE S-2 VERDICT: DIAGNOSTIC")
    print("=" * 72)

    # Check if M_max is monotonically decreasing with C_2 at any (tau, mu)
    all_decreasing = all(v == "DECREASING" for v in monotonicity.values())
    any_decreasing = any(v == "DECREASING" for v in monotonicity.values())

    # Count decreasing at mu=0 vs mu>0
    mu0_keys = [(t, 0.0) for t in plot_taus]
    mu0_mono = [monotonicity.get(k, "UNKNOWN") for k in mu0_keys]
    mu1_keys = [(t, 1.0) for t in plot_taus]
    mu1_mono = [monotonicity.get(k, "UNKNOWN") for k in mu1_keys]

    print(f"\n  Monotonicity summary:")
    print(f"    At mu=0:   {mu0_mono}")
    print(f"    At mu=1.0: {mu1_mono}")

    if any_decreasing:
        verdict = "PHONON-LIKE"
        print(f"\n  M_max DECREASES with C_2 in at least some (tau, mu) regimes.")
        print(f"  BCS instability is strongest for lowest representations.")
        print(f"  CONSISTENT with phonon interpretation (long-wavelength condensation).")
    else:
        verdict = "NON-PHONONIC"
        print(f"\n  M_max does NOT decrease monotonically with C_2 in any regime.")
        if all(v == "INCREASING" for v in monotonicity.values()):
            print(f"  M_max INCREASES with C_2: ANTI-PHONONIC dispersion.")
            print(f"  Higher representations have stronger instability.")
        else:
            print(f"  Mixed/non-monotonic dispersion relation.")

    # Check for acoustic branch
    pl_exponents = [fit_results.get(('power', t), (np.nan, np.nan, np.nan))[1]
                    for t in plot_taus]
    valid_exponents = [b for b in pl_exponents if not np.isnan(b)]
    if valid_exponents:
        mean_exp = np.mean(valid_exponents)
        print(f"\n  Power law exponent (M ~ C2^b): b = {mean_exp:.3f}")
        if abs(mean_exp - 0.5) < 0.15:
            print(f"  Near b=0.5: ACOUSTIC BRANCH detected (M ~ sqrt(C2))")
        elif abs(mean_exp + 0.5) < 0.15:
            print(f"  Near b=-0.5: OPTICAL-like decay (M ~ 1/sqrt(C2))")
        elif mean_exp < -0.1:
            print(f"  Negative exponent: M decreases with C2 (phonon-like decay)")
        else:
            print(f"  Positive exponent: M increases with C2 (non-phononic)")

    print(f"\n  VERDICT: S-2 = DIAGNOSTIC ({verdict})")
    print("  This is a diagnostic gate -- no closure/pass implications.")

    # -------------------------------------------------------------------------
    # 8. SAVE DATA
    # -------------------------------------------------------------------------
    outfile = os.path.join(OUTDIR, 's28a_mmax_dispersion.npz')
    np.savez_compressed(outfile,
                        C2=C2,
                        C2_sorted=C2_sorted,
                        sort_idx=sort_idx,
                        sectors=sectors,
                        tau_values=tau_values,
                        mu_ratios=mu_ratios,
                        M_max=M_max,
                        lambda_min=lambda_min,
                        F_cond=F_cond,
                        Delta_max=Delta_max,
                        plot_tau_indices=np.array(tau_indices),
                        plot_mu_indices=np.array(mu_indices),
                        verdict=np.array(verdict))
    print(f"\nData saved to {outfile}")

    # -------------------------------------------------------------------------
    # 9. PLOT
    # -------------------------------------------------------------------------
    print("\nGenerating plots...")
    fig, axes = plt.subplots(3, 4, figsize=(22, 16))

    colors_tau = ['#1f77b4', '#ff7f0e', '#2ca02c']
    markers_mu = ['o', 's', '^', 'D']

    # --- Row 1: M_max vs C_2 at different mu, panels by tau ---
    for ti, tau_idx in enumerate(tau_indices):
        ax = axes[0, ti]
        tau_val = tau_values[tau_idx]

        for mi, mu_idx in enumerate(mu_indices):
            mu_val = mu_ratios[mu_idx]
            M_vals = np.array([M_max[s, tau_idx, mu_idx] for s in sort_idx])

            ax.plot(C2_sorted, M_vals, markers_mu[mi] + '-',
                    label=f'mu/lmin={mu_val:.1f}', markersize=6,
                    linewidth=1.2)

        ax.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7,
                    label='M=1 threshold')
        ax.set_xlabel('C_2(p,q)')
        ax.set_ylabel('M_max')
        ax.set_title(f'tau = {tau_val:.2f}')
        ax.legend(fontsize=7)
        ax.set_yscale('log')
        ax.set_ylim(bottom=0.01)

        # Add sector labels
        for j, s_idx in enumerate(sort_idx):
            p, q = sectors[s_idx, 0], sectors[s_idx, 1]
            ax.annotate(f'({p},{q})', (C2_sorted[j], M_vals[j]),
                        textcoords='offset points', xytext=(0, 8),
                        fontsize=6, ha='center', alpha=0.7)

    # Row 1, col 4: M_max vs C_2 comparison across tau at mu=1.0
    ax = axes[0, 3]
    for ti, tau_idx in enumerate(tau_indices):
        tau_val = tau_values[tau_idx]
        M_vals = np.array([M_max[s, tau_idx, mu_indices[2]] for s in sort_idx])
        ax.plot(C2_sorted, M_vals, 'o-', color=colors_tau[ti],
                label=f'tau={tau_val:.2f}', markersize=6, linewidth=1.5)
    ax.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7)
    ax.set_xlabel('C_2(p,q)')
    ax.set_ylabel('M_max')
    ax.set_title('mu/lmin=1.0: tau comparison')
    ax.legend(fontsize=8)
    ax.set_yscale('log')
    ax.set_ylim(bottom=0.01)

    # --- Row 2: Linear scale, M_max vs C_2 at mu=0, mu=1.0, mu=1.2 ---
    for mi_plot, mu_idx in enumerate([mu_indices[0], mu_indices[2], mu_indices[3]]):
        ax = axes[1, mi_plot]
        mu_val = mu_ratios[mu_idx]

        for ti, tau_idx in enumerate(tau_indices):
            tau_val = tau_values[tau_idx]
            M_vals = np.array([M_max[s, tau_idx, mu_idx] for s in sort_idx])
            ax.plot(C2_sorted, M_vals, 'o-', color=colors_tau[ti],
                    label=f'tau={tau_val:.2f}', markersize=6, linewidth=1.5)

        ax.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7)
        ax.set_xlabel('C_2(p,q)')
        ax.set_ylabel('M_max')
        ax.set_title(f'mu/lmin = {mu_val:.1f} (linear)')
        ax.legend(fontsize=8)

    # Row 2, col 4: Condensation energy F_cond vs C_2
    ax = axes[1, 3]
    for ti, tau_idx in enumerate(tau_indices):
        tau_val = tau_values[tau_idx]
        F_vals = np.array([F_cond[s, tau_idx, mu_indices[2]]
                           for s in sort_idx])
        ax.plot(C2_sorted, F_vals, 'o-', color=colors_tau[ti],
                label=f'tau={tau_val:.2f}', markersize=6, linewidth=1.5)
    ax.axhline(0, color='k', ls=':', lw=0.8)
    ax.set_xlabel('C_2(p,q)')
    ax.set_ylabel('F_cond')
    ax.set_title('Condensation energy at mu/lmin=1.0')
    ax.legend(fontsize=8)

    # --- Row 3: Heatmaps ---
    # M_max heatmap at mu=0
    ax = axes[2, 0]
    M_map_mu0 = np.zeros((n_sectors, n_tau))
    for si in range(n_sectors):
        for ti in range(n_tau):
            M_map_mu0[si, ti] = M_max[sort_idx[si], ti, mu_indices[0]]
    im = ax.imshow(M_map_mu0, aspect='auto', origin='lower',
                    extent=[tau_values[0], tau_values[-1], -0.5, n_sectors - 0.5],
                    cmap='RdYlBu_r', vmin=0, vmax=0.2)
    ax.set_yticks(range(n_sectors))
    ax.set_yticklabels(sector_labels, fontsize=8)
    ax.set_xlabel('tau')
    ax.set_ylabel('Sector (by C_2)')
    ax.set_title('M_max heatmap (mu=0)')
    plt.colorbar(im, ax=ax, label='M_max')

    # M_max heatmap at mu=lambda_min
    ax = axes[2, 1]
    M_map_mu1 = np.zeros((n_sectors, n_tau))
    for si in range(n_sectors):
        for ti in range(n_tau):
            M_map_mu1[si, ti] = M_max[sort_idx[si], ti, mu_indices[2]]
    im = ax.imshow(np.log10(M_map_mu1 + 1e-3), aspect='auto', origin='lower',
                    extent=[tau_values[0], tau_values[-1], -0.5, n_sectors - 0.5],
                    cmap='RdYlBu_r')
    ax.set_yticks(range(n_sectors))
    ax.set_yticklabels(sector_labels, fontsize=8)
    ax.set_xlabel('tau')
    ax.set_ylabel('Sector (by C_2)')
    ax.set_title('log10(M_max) heatmap (mu=lmin)')
    plt.colorbar(im, ax=ax, label='log10(M_max)')

    # M_max heatmap at mu=1.2*lambda_min
    ax = axes[2, 2]
    M_map_mu12 = np.zeros((n_sectors, n_tau))
    for si in range(n_sectors):
        for ti in range(n_tau):
            M_map_mu12[si, ti] = M_max[sort_idx[si], ti, mu_indices[3]]
    im = ax.imshow(np.log10(M_map_mu12 + 1e-3), aspect='auto', origin='lower',
                    extent=[tau_values[0], tau_values[-1], -0.5, n_sectors - 0.5],
                    cmap='RdYlBu_r')
    ax.set_yticks(range(n_sectors))
    ax.set_yticklabels(sector_labels, fontsize=8)
    ax.set_xlabel('tau')
    ax.set_ylabel('Sector (by C_2)')
    ax.set_title('log10(M_max) heatmap (mu=1.2*lmin)')
    plt.colorbar(im, ax=ax, label='log10(M_max)')

    # Threshold crossing: tau where M_max = 1 (by interpolation)
    ax = axes[2, 3]
    # For each sector, plot mu_critical / lambda_min where M_max crosses 1
    for si_plot, s_idx in enumerate(sort_idx):
        p, q = sectors[s_idx, 0], sectors[s_idx, 1]
        for tau_idx in tau_indices:
            tau_val = tau_values[tau_idx]
            M_vs_mu = M_max[s_idx, tau_idx, :]
            # Find mu ratio where M crosses 1
            crossings = np.where(np.diff(np.sign(M_vs_mu - 1.0)))[0]
            if len(crossings) > 0:
                # Linear interpolation
                i_cross = crossings[0]
                mu_low = mu_ratios[i_cross]
                mu_high = mu_ratios[i_cross + 1]
                M_low = M_vs_mu[i_cross]
                M_high = M_vs_mu[i_cross + 1]
                mu_crit = mu_low + (1.0 - M_low) / (M_high - M_low) * (mu_high - mu_low)
                ax.scatter(C2[s_idx], mu_crit,
                           color=colors_tau[tau_indices.index(tau_idx)],
                           s=50, marker='o', zorder=3)

    ax.set_xlabel('C_2(p,q)')
    ax.set_ylabel('mu_crit / lambda_min')
    ax.set_title('Critical mu ratio (M_max=1 crossing)')
    # Add tau legend
    for ti, tau_idx in enumerate(tau_indices):
        ax.scatter([], [], color=colors_tau[ti], s=50,
                   label=f'tau={tau_values[tau_idx]:.2f}')
    ax.legend(fontsize=8)
    ax.axhline(1.0, color='gray', ls=':', lw=0.8)

    plt.suptitle('S-2: BCS M_max vs Quadratic Casimir C_2 Dispersion Relation',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    plotfile = os.path.join(OUTDIR, 's28a_mmax_dispersion.png')
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {plotfile}")

    total_time = time.time() - t_start
    print(f"\nTotal computation time: {total_time:.1f}s")
    print("DONE.")


if __name__ == '__main__':
    main()
