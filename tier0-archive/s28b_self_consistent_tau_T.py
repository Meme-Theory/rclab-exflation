"""
Session 28b Computation 6: L-7 Self-Consistent (tau, T) -- REDUCED FORM
========================================================================

Since L-1 CLOSED (thermal spectral action F(tau;T) is monotonically
increasing at ALL temperatures), the thermal channel is closed.
L-7 runs in REDUCED FORM: BCS-only at T=0, no thermal free energy.

PHYSICS (REDUCED):
    F_total(tau, mu) = sum_{(p,q)} mult(p,q) * F_cond^{(p,q)}(tau, mu)

    This is identical to the S27 multi-sector BCS total, re-analyzed here
    with focus on the phase diagram structure:

    1. Map the full (tau, mu) phase diagram from S27 data
    2. Identify all local/global minima and their character (interior vs boundary)
    3. Mark BCS condensation regions (Delta > 0 in any sector)
    4. Confirm/deny the interior minimum at tau~0.35, mu/lambda_min~1.20
    5. Report whether thermal channel closure changes the verdict

DATA SOURCES:
    - s27_multisector_bcs.npz: F_cond, F_total, M_max, Delta_max per sector
    - s28a_thermal_spectral_action.npz: F(tau;T) thermal data (for cross-reference)

GATE L-7 (reduced):
    PASS (reduced): Interior minimum in (tau, mu) with tau > 0
    CLOSED: Minimum at tau=0 for all mu, or no condensation

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28b, Computation 6
"""

import os
import sys
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# LOAD DATA
# ===========================================================================

def load_s27_data():
    """Load Session 27 multi-sector BCS data.

    Returns:
        dict with tau_values, mu_ratios, sectors, F_total, F_cond,
        M_max, Delta_max, lambda_min
    """
    path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    if not os.path.exists(path):
        raise FileNotFoundError(f"S27 data not found: {path}")
    d = np.load(path, allow_pickle=True)
    return {
        'tau_values': d['tau_values'],        # (9,)
        'mu_ratios': d['mu_ratios'],          # (12,)
        'sectors': d['sectors'],              # (9, 4) = (p, q, dim, mult)
        'F_total': d['F_total'],              # (9, 12) = (tau, mu)
        'F_cond': d['F_cond'],                # (9, 9, 12) = (sector, tau, mu)
        'M_max': d['M_max'],                  # (9, 9, 12) = (sector, tau, mu)
        'Delta_max': d['Delta_max'],          # (9, 9, 12) = (sector, tau, mu)
        'lambda_min': d['lambda_min'],        # (9, 9) = (sector, tau)
    }


def load_s28a_thermal():
    """Load Session 28a thermal spectral action for cross-reference.

    Returns:
        dict with tau_values, T_values, F_total, verdict
    """
    path = os.path.join(SCRIPT_DIR, "s28a_thermal_spectral_action.npz")
    if not os.path.exists(path):
        print("WARNING: S28a thermal data not found, skipping cross-reference")
        return None
    d = np.load(path, allow_pickle=True)
    return {
        'tau_values': d['tau_values'],   # (21,)
        'T_values': d['T_values'],       # (10,)
        'F_total': d['F_total'],         # (21, 10)
        'verdict': str(d['verdict'][0]),
    }


# ===========================================================================
# PHASE DIAGRAM ANALYSIS
# ===========================================================================

def analyze_phase_diagram(s27):
    """Full analysis of the (tau, mu) phase diagram from S27 BCS data.

    Returns:
        dict with all analysis results
    """
    tau = s27['tau_values']
    mu = s27['mu_ratios']
    F = s27['F_total']          # (n_tau, n_mu)
    Fc = s27['F_cond']          # (n_sector, n_tau, n_mu)
    M = s27['M_max']            # (n_sector, n_tau, n_mu)
    D = s27['Delta_max']        # (n_sector, n_tau, n_mu)
    lmin = s27['lambda_min']    # (n_sector, n_tau)
    sectors = s27['sectors']

    n_tau = len(tau)
    n_mu = len(mu)
    n_sec = len(sectors)

    results = {}

    # -----------------------------------------------------------------------
    # 1. Map condensation regions: any sector with Delta > 0
    # -----------------------------------------------------------------------
    any_condensate = np.zeros((n_tau, n_mu), dtype=bool)
    n_condensed_sectors = np.zeros((n_tau, n_mu), dtype=int)

    for ti in range(n_tau):
        for mi in range(n_mu):
            for si in range(n_sec):
                if D[si, ti, mi] > 1e-20:
                    any_condensate[ti, mi] = True
                    n_condensed_sectors[ti, mi] += 1

    results['any_condensate'] = any_condensate
    results['n_condensed_sectors'] = n_condensed_sectors

    # -----------------------------------------------------------------------
    # 2. Find ALL local minima in the interior (exclude tau=0 and tau=max)
    # -----------------------------------------------------------------------
    interior_minima = []
    boundary_minima = []

    for mi in range(n_mu):
        F_tau = F[:, mi]
        if not np.all(np.isfinite(F_tau)):
            continue
        if np.all(F_tau == 0.0):
            continue

        # Global minimum along tau for this mu
        glob_idx = np.argmin(F_tau)
        glob_F = F_tau[glob_idx]

        if glob_F >= 0.0:
            continue  # No condensation at this mu

        # Is global minimum at boundary or interior?
        if glob_idx == 0 or glob_idx == n_tau - 1:
            boundary_minima.append({
                'tau_idx': glob_idx, 'mu_idx': mi,
                'tau': tau[glob_idx], 'mu_ratio': mu[mi],
                'F_total': glob_F, 'type': 'boundary_global',
            })
        else:
            interior_minima.append({
                'tau_idx': glob_idx, 'mu_idx': mi,
                'tau': tau[glob_idx], 'mu_ratio': mu[mi],
                'F_total': glob_F, 'type': 'interior_global',
            })

        # Also check for local interior minima (not necessarily global)
        for ti in range(1, n_tau - 1):
            if (F_tau[ti] < F_tau[ti - 1] and F_tau[ti] < F_tau[ti + 1]
                    and F_tau[ti] < 0.0 and ti != glob_idx):
                interior_minima.append({
                    'tau_idx': ti, 'mu_idx': mi,
                    'tau': tau[ti], 'mu_ratio': mu[mi],
                    'F_total': F_tau[ti], 'type': 'interior_local',
                })

    results['interior_minima'] = interior_minima
    results['boundary_minima'] = boundary_minima

    # -----------------------------------------------------------------------
    # 3. Classify F_total(tau) profile at each mu
    # -----------------------------------------------------------------------
    profiles = []
    for mi in range(n_mu):
        F_tau = F[:, mi]
        valid = np.all(np.isfinite(F_tau))
        if not valid:
            profiles.append(f"mu/lmin={mu[mi]:.2f}: NaN present")
            continue
        if np.all(F_tau == 0.0):
            profiles.append(f"mu/lmin={mu[mi]:.2f}: zero (no condensate)")
            continue

        diffs = np.diff(F_tau)
        n_sign_changes = np.sum(np.diff(np.sign(diffs + 1e-30)) != 0)
        min_idx = np.argmin(F_tau)
        min_val = F_tau[min_idx]

        if n_sign_changes == 0:
            mono = "decreasing" if diffs[0] < 0 else "increasing"
            profiles.append(
                f"mu/lmin={mu[mi]:.2f}: monotonically {mono}, "
                f"min at tau={tau[min_idx]:.2f} (F={min_val:.4f})"
            )
        else:
            profiles.append(
                f"mu/lmin={mu[mi]:.2f}: non-monotonic ({n_sign_changes} inflections), "
                f"min at tau={tau[min_idx]:.2f} (F={min_val:.4f})"
            )

    results['profiles'] = profiles

    # -----------------------------------------------------------------------
    # 4. Per-sector contribution breakdown at interior minimum tau=0.35
    # -----------------------------------------------------------------------
    ti_035 = np.argmin(np.abs(tau - 0.35))
    sector_breakdown = {}

    for mi in range(n_mu):
        contribs = []
        for si in range(n_sec):
            p, q, dim_rho, mult = sectors[si]
            # (2,1) effective multiplicity includes CPT-conjugate (1,2)
            eff_mult = 450 if (p == 2 and q == 1) else mult
            f_val = Fc[si, ti_035, mi]
            if np.isfinite(f_val) and f_val != 0.0:
                contribs.append({
                    'sector': f"({p},{q})",
                    'mult': eff_mult,
                    'F_cond': f_val,
                    'contrib': eff_mult * f_val,
                    'M_max': M[si, ti_035, mi],
                    'Delta_max': D[si, ti_035, mi],
                })
        sector_breakdown[mu[mi]] = contribs

    results['sector_breakdown_tau035'] = sector_breakdown

    # -----------------------------------------------------------------------
    # 5. Global minimum across entire (tau, mu) plane
    # -----------------------------------------------------------------------
    # Replace NaN with 0 for argmin
    F_safe = np.where(np.isfinite(F), F, 0.0)
    glob_flat_idx = np.argmin(F_safe)
    glob_ti, glob_mi = np.unravel_index(glob_flat_idx, F.shape)
    results['global_min'] = {
        'tau_idx': int(glob_ti), 'mu_idx': int(glob_mi),
        'tau': float(tau[glob_ti]), 'mu_ratio': float(mu[glob_mi]),
        'F_total': float(F[glob_ti, glob_mi]),
        'is_boundary': glob_ti == 0 or glob_ti == n_tau - 1,
    }

    return results


# ===========================================================================
# GATE VERDICT
# ===========================================================================

def compute_verdict(analysis, s28a_thermal):
    """Determine L-7 (reduced) gate verdict.

    PASS (reduced): Interior minimum in (tau, mu) with tau > 0, BCS-only
    CLOSED: Minimum at tau=0 for all mu, or no condensation at all

    Parameters:
        analysis: dict from analyze_phase_diagram
        s28a_thermal: dict from load_s28a_thermal (or None)

    Returns:
        verdict: str
        detail: list of str
    """
    interior = analysis['interior_minima']
    boundary = analysis['boundary_minima']
    gmin = analysis['global_min']

    lines = []

    # Thermal channel status
    if s28a_thermal is not None:
        lines.append(f"L-1 verdict: {s28a_thermal['verdict']} (thermal channel CLOSED)")
    else:
        lines.append("L-1 verdict: CLOSED assumed (thermal channel CLOSED)")

    lines.append("")
    lines.append("BCS-ONLY ANALYSIS (reduced L-7):")

    # Count interior minima with F < 0
    interior_negative = [m for m in interior if m['F_total'] < 0]
    n_interior = len(interior_negative)

    lines.append(f"  Interior (tau>0, tau<tau_max) minima with F<0: {n_interior}")
    for m in interior_negative:
        lines.append(
            f"    tau={m['tau']:.2f}, mu/lmin={m['mu_ratio']:.2f}: "
            f"F={m['F_total']:.4f} [{m['type']}]"
        )

    lines.append(f"  Boundary minima with F<0: {len(boundary)}")
    for m in boundary[:5]:  # Show up to 5
        lines.append(
            f"    tau={m['tau']:.2f}, mu/lmin={m['mu_ratio']:.2f}: "
            f"F={m['F_total']:.4f} [{m['type']}]"
        )

    lines.append(f"\n  Global minimum: tau={gmin['tau']:.2f}, mu/lmin={gmin['mu_ratio']:.2f}, "
                  f"F={gmin['F_total']:.4f} "
                  f"({'BOUNDARY' if gmin['is_boundary'] else 'INTERIOR'})")

    # Verdict logic
    if n_interior > 0:
        # Check if any interior minimum is the global minimum
        best_interior = min(interior_negative, key=lambda m: m['F_total'])
        if gmin['is_boundary'] and gmin['F_total'] < best_interior['F_total']:
            verdict = "PASS_REDUCED_WEAK"
            lines.append(
                f"\n  VERDICT: L-7 PASS (reduced, WEAK)"
            )
            lines.append(
                f"  Interior minimum exists at tau={best_interior['tau']:.2f} "
                f"(F={best_interior['F_total']:.4f})"
            )
            lines.append(
                f"  BUT boundary tau={gmin['tau']:.2f} is deeper "
                f"(F={gmin['F_total']:.4f})"
            )
            lines.append(
                "  BCS free energy has local interior stabilization, not global."
            )
        else:
            verdict = "PASS_REDUCED"
            lines.append(f"\n  VERDICT: L-7 PASS (reduced)")
            lines.append(
                f"  Interior global minimum at tau={best_interior['tau']:.2f}, "
                f"mu/lmin={best_interior['mu_ratio']:.2f}, F={best_interior['F_total']:.4f}"
            )
    else:
        verdict = "CLOSED"
        lines.append(f"\n  VERDICT: L-7 CLOSED")
        lines.append("  No interior minimum in (tau, mu) space with F < 0.")
        if gmin['F_total'] < 0:
            lines.append(
                f"  Global minimum at boundary tau={gmin['tau']:.2f} "
                f"(F={gmin['F_total']:.4f}): BCS does not stabilize tau."
            )
        else:
            lines.append("  No condensation energy found anywhere.")

    # Thermal closure note
    lines.append("")
    lines.append("NOTE: Full L-7 (thermal + BCS) is CLOSED per L-1 CLOSED.")
    lines.append("  Thermal spectral action is monotonically increasing at ALL T.")
    lines.append("  Adding F_thermal would push minimum toward tau=0 (wrong direction).")
    lines.append("  This reduced analysis tests BCS-ONLY stabilization.")

    return verdict, lines


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(s27, analysis, verdict, verdict_lines, save_path):
    """Generate 6-panel phase diagram plot.

    Panels:
        1. F_total(tau) at selected mu values -- the key diagnostic
        2. Phase diagram: condensation regions in (tau, mu) space
        3. Number of condensed sectors in (tau, mu)
        4. Sector contribution breakdown at tau=0.35
        5. M_max(tau) at mu=lambda_min for all sectors
        6. Gate verdict text

    Parameters:
        s27: dict from load_s27_data
        analysis: dict from analyze_phase_diagram
        verdict: str
        verdict_lines: list of str
        save_path: output PNG path
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    tau = s27['tau_values']
    mu = s27['mu_ratios']
    F = s27['F_total']
    sectors = s27['sectors']

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("28b-6 L-7 Self-Consistent (tau, T) -- REDUCED FORM (BCS Only)",
                 fontsize=13, fontweight='bold')

    # ------------------------------------------------------------------
    # Panel 1: F_total(tau) at selected mu values
    # ------------------------------------------------------------------
    ax = axes[0, 0]
    mu_show = [5, 6, 7, 8, 9, 10]  # mu/lmin = 1.0, 1.05, 1.1, 1.2, 1.5, 2.0
    colors_mu = plt.cm.plasma(np.linspace(0.1, 0.9, len(mu_show)))
    for i, mi in enumerate(mu_show):
        if mi < len(mu):
            F_tau = F[:, mi]
            mask = np.isfinite(F_tau) & (F_tau != 0.0)
            if np.any(mask):
                ax.plot(tau[mask], F_tau[mask], 'o-', color=colors_mu[i],
                        label=f'mu/lmin={mu[mi]:.2f}', markersize=5, linewidth=1.5)
                # Mark minimum
                min_idx = np.argmin(F_tau)
                ax.plot(tau[min_idx], F_tau[min_idx], '*', color=colors_mu[i],
                        markersize=12, zorder=5)
    ax.axhline(0, color='k', linestyle='-', alpha=0.3)
    ax.set_xlabel('tau')
    ax.set_ylabel('F_total (BCS only)')
    ax.set_title('F_total(tau) at selected mu')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 2: Phase diagram heatmap -- F_total in (tau, mu)
    # ------------------------------------------------------------------
    ax = axes[0, 1]
    # Only show mu >= 0.8 where condensation happens
    mu_mask = mu >= 0.8
    F_sub = F[:, mu_mask]
    mu_sub = mu[mu_mask]

    # Replace 0 with NaN for better visualization
    F_plot = np.where(F_sub == 0.0, np.nan, F_sub)

    # Custom colormap: white for zero, blue for negative
    im = ax.imshow(F_plot.T, aspect='auto', origin='lower',
                   extent=[tau[0], tau[-1], mu_sub[0], mu_sub[-1]],
                   cmap='RdBu_r', vmin=-50, vmax=5,
                   interpolation='nearest')
    fig.colorbar(im, ax=ax, label='F_total')

    # Mark interior minima
    for m in analysis['interior_minima']:
        if m['F_total'] < 0:
            ax.plot(m['tau'], m['mu_ratio'], 'k*', markersize=15, zorder=5)

    # Mark global minimum
    gm = analysis['global_min']
    ax.plot(gm['tau'], gm['mu_ratio'], 'rv', markersize=12, zorder=5,
            label=f"Global min: F={gm['F_total']:.1f}")

    ax.set_xlabel('tau')
    ax.set_ylabel('mu / lambda_min')
    ax.set_title('F_total(tau, mu) phase diagram')
    ax.legend(fontsize=8, loc='upper right')

    # ------------------------------------------------------------------
    # Panel 3: Number of condensed sectors
    # ------------------------------------------------------------------
    ax = axes[0, 2]
    n_cond = analysis['n_condensed_sectors']
    n_cond_sub = n_cond[:, mu_mask]
    im3 = ax.imshow(n_cond_sub.T, aspect='auto', origin='lower',
                    extent=[tau[0], tau[-1], mu_sub[0], mu_sub[-1]],
                    cmap='YlOrRd', vmin=0, vmax=9,
                    interpolation='nearest')
    fig.colorbar(im3, ax=ax, label='# condensed sectors')
    ax.set_xlabel('tau')
    ax.set_ylabel('mu / lambda_min')
    ax.set_title('Condensed sector count')

    # ------------------------------------------------------------------
    # Panel 4: Sector contributions at tau=0.35, mu/lmin=1.20
    # ------------------------------------------------------------------
    ax = axes[1, 0]
    breakdown = analysis['sector_breakdown_tau035']
    target_mu = 1.2
    # Find closest mu key
    closest_mu = min(breakdown.keys(), key=lambda x: abs(x - target_mu))
    contribs = breakdown[closest_mu]
    if contribs:
        labels_b = [c['sector'] for c in contribs]
        values_b = [abs(c['contrib']) for c in contribs]
        signs_b = ['blue' if c['contrib'] < 0 else 'red' for c in contribs]
        bars = ax.barh(range(len(labels_b)), values_b, color=signs_b)
        ax.set_yticks(range(len(labels_b)))
        ax.set_yticklabels(labels_b)
        ax.set_xlabel('|mult * F_cond|')
        ax.set_title(f'Sector contributions (tau=0.35, mu/lmin={closest_mu:.2f})')
        ax.set_xscale('log')
        # Annotate bars
        for i, c in enumerate(contribs):
            ax.text(abs(c['contrib']) * 1.1, i,
                    f"m={c['mult']}, F={c['F_cond']:.4f}",
                    va='center', fontsize=7)
    else:
        ax.text(0.5, 0.5, 'No condensate', ha='center', va='center',
                transform=ax.transAxes)
        ax.set_title('Sector contributions (no data)')

    # ------------------------------------------------------------------
    # Panel 5: M_max(tau) at mu=lambda_min for all sectors
    # ------------------------------------------------------------------
    ax = axes[1, 1]
    M = s27['M_max']
    mu_idx_lmin = np.argmin(np.abs(mu - 1.0))
    sector_colors = plt.cm.tab10(np.linspace(0, 1, len(sectors)))
    for si, (p, q, dim_rho, mult) in enumerate(sectors):
        M_tau = M[si, :, mu_idx_lmin]
        ax.semilogy(tau, M_tau, 'o-', color=sector_colors[si],
                    label=f'({p},{q})', markersize=4, linewidth=1.2)
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, label='M=1')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max (linearized)')
    ax.set_title('BCS kernel strength at mu=lambda_min')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 6: Gate verdict
    # ------------------------------------------------------------------
    ax = axes[1, 2]
    ax.axis('off')

    v_color = 'green' if 'PASS' in verdict else 'red'
    ax.text(0.5, 0.95, 'GATE L-7 (REDUCED)', fontsize=14, fontweight='bold',
            ha='center', va='top', transform=ax.transAxes)
    ax.text(0.5, 0.85, verdict, fontsize=12, fontweight='bold',
            ha='center', va='top', transform=ax.transAxes, color=v_color)

    # Compact version of verdict lines
    compact = [l for l in verdict_lines if l.strip() and not l.startswith('NOTE')]
    text = '\n'.join(compact[:15])
    ax.text(0.05, 0.75, text, fontsize=7, fontfamily='monospace',
            ha='left', va='top', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved: {save_path}")


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=" * 78)
    print("28b-6 L-7 Self-Consistent (tau, T) -- REDUCED FORM")
    print("=" * 78)
    print()

    # 1. Load data
    print("Loading S27 multi-sector BCS data...")
    s27 = load_s27_data()
    print(f"  tau: {s27['tau_values']}")
    print(f"  mu/lmin: {s27['mu_ratios']}")
    print(f"  sectors: {s27['sectors'].shape[0]}")
    print(f"  F_total shape: {s27['F_total'].shape}")

    print("\nLoading S28a thermal spectral action...")
    s28a = load_s28a_thermal()
    if s28a is not None:
        print(f"  L-1 verdict: {s28a['verdict']}")
    print()

    # 2. Phase diagram analysis
    print("Analyzing (tau, mu) phase diagram...")
    analysis = analyze_phase_diagram(s27)

    # Print profiles
    print("\nF_total(tau) profile at each mu:")
    for line in analysis['profiles']:
        print(f"  {line}")

    # Print interior minima
    print(f"\nInterior minima (F < 0):")
    interior_neg = [m for m in analysis['interior_minima'] if m['F_total'] < 0]
    if interior_neg:
        for m in sorted(interior_neg, key=lambda x: x['F_total']):
            print(f"  tau={m['tau']:.2f}, mu/lmin={m['mu_ratio']:.2f}: "
                  f"F={m['F_total']:.4f} [{m['type']}]")
    else:
        print("  NONE")

    print(f"\nBoundary minima (F < 0):")
    boundary_neg = [m for m in analysis['boundary_minima'] if m['F_total'] < 0]
    if boundary_neg:
        for m in sorted(boundary_neg, key=lambda x: x['F_total']):
            print(f"  tau={m['tau']:.2f}, mu/lmin={m['mu_ratio']:.2f}: "
                  f"F={m['F_total']:.4f} [{m['type']}]")
    else:
        print("  NONE")

    gm = analysis['global_min']
    print(f"\nGlobal minimum: tau={gm['tau']:.2f}, mu/lmin={gm['mu_ratio']:.2f}, "
          f"F={gm['F_total']:.4f} ({'BOUNDARY' if gm['is_boundary'] else 'INTERIOR'})")

    # Print sector breakdown at claimed interior minimum
    print(f"\nSector breakdown at tau=0.35, mu/lmin=1.20:")
    bd = analysis['sector_breakdown_tau035']
    target_mu = 1.2
    closest_mu = min(bd.keys(), key=lambda x: abs(x - target_mu))
    for c in bd[closest_mu]:
        print(f"  {c['sector']} mult={c['mult']:>3d}: F_cond={c['F_cond']:.6f}, "
              f"contrib={c['contrib']:.4f}, M_max={c['M_max']:.3f}, "
              f"Delta_max={c['Delta_max']:.6f}")

    # 3. Condensation coverage
    cond = analysis['any_condensate']
    n_cond_points = np.sum(cond)
    total_points = cond.size
    print(f"\nCondensation coverage: {n_cond_points}/{total_points} grid points "
          f"({100*n_cond_points/total_points:.1f}%)")

    # 4. Gate verdict
    print("\n" + "=" * 78)
    verdict, verdict_lines = compute_verdict(analysis, s28a)
    for line in verdict_lines:
        print(f"  {line}")
    print("=" * 78)

    # 5. Save data
    npz_path = os.path.join(SCRIPT_DIR, "s28b_self_consistent_tau_T.npz")
    np.savez_compressed(
        npz_path,
        tau_values=s27['tau_values'],
        mu_ratios=s27['mu_ratios'],
        F_total=s27['F_total'],
        any_condensate=analysis['any_condensate'],
        n_condensed_sectors=analysis['n_condensed_sectors'],
        n_interior_minima=len(interior_neg),
        global_min_tau=gm['tau'],
        global_min_mu=gm['mu_ratio'],
        global_min_F=gm['F_total'],
        global_min_is_boundary=gm['is_boundary'],
        thermal_verdict='CLOSED',
        verdict=np.array([verdict]),
    )
    print(f"\nData saved: {npz_path}")

    # 6. Plot
    png_path = os.path.join(SCRIPT_DIR, "s28b_self_consistent_tau_T.png")
    make_plots(s27, analysis, verdict, verdict_lines, png_path)

    print(f"\n{'='*78}")
    print(f"FINAL VERDICT: {verdict}")
    print(f"{'='*78}")


if __name__ == "__main__":
    main()
