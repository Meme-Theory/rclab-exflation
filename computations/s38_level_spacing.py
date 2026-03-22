#!/usr/bin/env python3
"""
s38_level_spacing.py -- CHAOS-1 Gate: D_K Level Spacing Statistics

Compute the level spacing ratio statistic <r> for the Dirac operator D_K
on Jensen-deformed SU(3), within individual Peter-Weyl sectors.

Physics:
  - D_K is block-diagonal by Peter-Weyl decomposition (proven Session 22b)
  - At tau=0 (bi-invariant SU(3)), maximal symmetry => integrable (Poisson)
  - Jensen deformation breaks SU(3) -> U(1)_7, should push toward chaos
  - AZ class BDI, T^2=+1 => if chaotic, expect GOE statistics

Gate CHAOS-1:
  <r> > 0.50 at fold (tau~0.190) => PASS (GOE chaos)
  <r> < 0.42 at fold => FAIL (Poisson integrable)
  0.42 < <r> < 0.50 => INCONCLUSIVE

References:
  - BGS conjecture (Bohigas, Giannoni, Schmit 1984): chaos <-> RMT statistics
  - Berry-Tabor (1977): integrability <-> Poisson statistics
  - Haake (2010): quantum signatures of chaos, practical diagnostics

Author: Kitaev-Quantum-Chaos-Theorist agent, Session 38
"""

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys

# ============================================================
# CONSTANTS
# ============================================================
R_POISSON = 2 * np.log(2) - 1  # ~ 0.38629
R_GOE = 0.5307                   # Atas et al. 2013
R_GUE = 0.5996                   # Atas et al. 2013
DEGENERACY_TOL = 1e-10           # tolerance for identifying degenerate eigenvalues

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def remove_degeneracies(evals, tol=DEGENERACY_TOL):
    """Remove exact degeneracies, returning unique sorted eigenvalues."""
    evals_sorted = np.sort(evals)
    unique = [evals_sorted[0]]
    for e in evals_sorted[1:]:
        if abs(e - unique[-1]) > tol:
            unique.append(e)
    return np.array(unique)


def unfold_polynomial(evals, degree=5):
    """
    Unfold spectrum using polynomial fit to the staircase function.

    Maps eigenvalues E_n -> x_n = N_smooth(E_n) so that unfolded spacings
    have mean 1.
    """
    evals = np.sort(evals)
    N = len(evals)
    staircase = np.arange(1, N + 1)

    # Fit smooth N(E) with polynomial
    coeffs = np.polyfit(evals, staircase, degree)
    N_smooth = np.polyval(coeffs, evals)

    # Unfolded spacings
    spacings = np.diff(N_smooth)

    # Remove any negative spacings from poor fit at edges
    spacings = spacings[spacings > 0]

    return spacings


def unfold_local_average(evals, window=None):
    """
    Unfold spectrum using local average spacing.

    Divide each spacing by the local mean spacing computed over a window.
    """
    evals = np.sort(evals)
    N = len(evals)
    if window is None:
        window = max(5, N // 5)

    raw_spacings = np.diff(evals)
    unfolded = np.zeros(len(raw_spacings))

    for i in range(len(raw_spacings)):
        lo = max(0, i - window // 2)
        hi = min(len(raw_spacings), i + window // 2 + 1)
        local_mean = np.mean(raw_spacings[lo:hi])
        if local_mean > 0:
            unfolded[i] = raw_spacings[i] / local_mean
        else:
            unfolded[i] = 0

    return unfolded[unfolded > 0]


def ratio_statistic(spacings):
    """
    Compute the ratio statistic r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}).
    Returns array of ratios and mean <r>.

    This diagnostic does NOT require unfolding -- it is ratio of consecutive
    spacings, hence scale-free. This is a major advantage over P(s).
    (Oganesyan & Huse 2007, Atas et al. 2013)
    """
    if len(spacings) < 2:
        return np.array([]), np.nan, np.nan

    ratios = []
    for i in range(len(spacings) - 1):
        s1 = spacings[i]
        s2 = spacings[i + 1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))

    ratios = np.array(ratios)
    if len(ratios) == 0:
        return np.array([]), np.nan, np.nan

    r_mean = np.mean(ratios)
    r_std = np.std(ratios) / np.sqrt(len(ratios))
    return ratios, r_mean, r_std


def ratio_from_raw_evals(evals):
    """
    Compute ratio statistic directly from eigenvalues (no unfolding needed).
    The ratio statistic is already scale-free.
    """
    evals = np.sort(evals)
    spacings = np.diff(evals)
    # Remove zero spacings (exact degeneracies)
    spacings = spacings[spacings > DEGENERACY_TOL]
    return ratio_statistic(spacings)


def wigner_surmise_goe(s):
    """P(s) for GOE (Wigner surmise)."""
    return (np.pi / 2) * s * np.exp(-np.pi * s**2 / 4)


def wigner_surmise_gue(s):
    """P(s) for GUE (Wigner surmise)."""
    return (32 / np.pi**2) * s**2 * np.exp(-4 * s**2 / np.pi)


def poisson_distribution(s):
    """P(s) for Poisson (integrable)."""
    return np.exp(-s)


def ratio_distribution_poisson(r):
    """P(r) for Poisson: P(r) = 2/(1+r)^2."""
    return 2.0 / (1 + r)**2


def ratio_distribution_goe(r):
    """
    P(r) for GOE (Atas et al. 2013):
    P(r) = (27/4) * (r + r^2) / (1 + r + r^2)^(5/2)
    """
    return (27.0 / 4.0) * (r + r**2) / (1 + r + r**2)**2.5


# ============================================================
# MAIN COMPUTATION
# ============================================================

def main():
    print("=" * 70)
    print("CHAOS-1 Gate: D_K Level Spacing Statistics")
    print("=" * 70)

    # Load eigenvalue data
    data_path = os.path.join(os.path.dirname(__file__), 's27_multisector_bcs.npz')
    data = np.load(data_path, allow_pickle=True)
    tau_values = data['tau_values']

    # Sector definitions: (p, q, dim_rep, total_evals)
    sector_info = [
        (0, 0, 1, 16),
        (1, 0, 3, 48),
        (0, 1, 3, 48),
        (1, 1, 8, 128),
        (2, 0, 6, 96),
        (0, 2, 6, 96),
        (3, 0, 10, 160),
        (0, 3, 10, 160),
        (2, 1, 15, 240),
    ]

    # ============================================================
    # STEP 1: Compute <r> for ALL sectors at ALL tau values
    # ============================================================
    print("\n--- Step 1: Ratio statistic <r> across all sectors and tau ---\n")

    # Storage
    results = {}

    for si, (p, q, dim_rep, n_evals) in enumerate(sector_info):
        sector_label = f"({p},{q})"
        results[sector_label] = {
            'tau': [], 'r_mean': [], 'r_std': [],
            'r_mean_poly': [], 'r_std_poly': [],
            'r_mean_local': [], 'r_std_local': [],
            'n_unique': [], 'n_spacings': [],
            'spacings_poly': {}, 'spacings_local': {},
            'ratios_raw': {},
        }

        for ti, tau in enumerate(tau_values):
            key = f"evals_{p}_{q}_{ti}"
            if key not in data:
                continue

            evals = data[key]

            # Remove degeneracies
            unique_evals = remove_degeneracies(evals)
            n_unique = len(unique_evals)

            # Method 0: Raw ratio statistic (no unfolding -- the gold standard)
            ratios_raw, r_raw, r_raw_err = ratio_from_raw_evals(unique_evals)

            # Method 1: Polynomial unfolding
            if n_unique >= 8:
                deg = min(5, n_unique // 3)
                sp_poly = unfold_polynomial(unique_evals, degree=deg)
                _, r_poly, r_poly_err = ratio_statistic(sp_poly)
            else:
                sp_poly = np.array([])
                r_poly, r_poly_err = np.nan, np.nan

            # Method 2: Local average unfolding
            if n_unique >= 8:
                sp_local = unfold_local_average(unique_evals)
                _, r_local, r_local_err = ratio_statistic(sp_local)
            else:
                sp_local = np.array([])
                r_local, r_local_err = np.nan, np.nan

            results[sector_label]['tau'].append(tau)
            results[sector_label]['r_mean'].append(r_raw)
            results[sector_label]['r_std'].append(r_raw_err)
            results[sector_label]['r_mean_poly'].append(r_poly)
            results[sector_label]['r_std_poly'].append(r_poly_err)
            results[sector_label]['r_mean_local'].append(r_local)
            results[sector_label]['r_std_local'].append(r_local_err)
            results[sector_label]['n_unique'].append(n_unique)
            results[sector_label]['n_spacings'].append(len(ratios_raw))
            results[sector_label]['spacings_poly'][tau] = sp_poly
            results[sector_label]['spacings_local'][tau] = sp_local
            results[sector_label]['ratios_raw'][tau] = ratios_raw

    # ============================================================
    # STEP 2: Print results table
    # ============================================================
    print(f"{'Sector':>8s} {'tau':>5s} {'N_uniq':>7s} {'<r>_raw':>8s} {'err':>7s} "
          f"{'<r>_poly':>9s} {'err':>7s} {'<r>_local':>10s} {'err':>7s} {'Class':>10s}")
    print("-" * 95)

    for sector_label in results:
        R = results[sector_label]
        for i in range(len(R['tau'])):
            tau = R['tau'][i]
            n = R['n_unique'][i]
            r = R['r_mean'][i]
            re = R['r_std'][i]
            rp = R['r_mean_poly'][i]
            rpe = R['r_std_poly'][i]
            rl = R['r_mean_local'][i]
            rle = R['r_std_local'][i]

            # Classification
            if np.isnan(r):
                cls = "N/A"
            elif r > 0.50:
                cls = "GOE+"
            elif r > 0.42:
                cls = "INTERM"
            elif r > 0.35:
                cls = "POISSON"
            else:
                cls = "SUB-P"

            print(f"{sector_label:>8s} {tau:5.2f} {n:7d} {r:8.4f} {re:7.4f} "
                  f"{rp:9.4f} {rpe:7.4f} {rl:10.4f} {rle:7.4f} {cls:>10s}")
        print()

    # ============================================================
    # STEP 3: Focus on key sectors near fold (tau=0.2 closest to 0.190)
    # ============================================================
    print("\n--- Step 3: Key results at fold (tau=0.20, closest to 0.190) ---\n")

    fold_idx = 3  # tau=0.2
    fold_tau = tau_values[fold_idx]

    key_sectors = ['(2,1)', '(3,0)', '(0,3)', '(1,1)', '(2,0)', '(0,2)']

    for sl in key_sectors:
        R = results[sl]
        if fold_idx < len(R['tau']):
            i = fold_idx
            print(f"  {sl}: N_unique={R['n_unique'][i]}, "
                  f"<r>_raw={R['r_mean'][i]:.4f} +/- {R['r_std'][i]:.4f}, "
                  f"<r>_poly={R['r_mean_poly'][i]:.4f}, "
                  f"<r>_local={R['r_mean_local'][i]:.4f}")

    # ============================================================
    # STEP 4: Pool sectors by conjugate pairs for better statistics
    # ============================================================
    print("\n--- Step 4: Pooled conjugate sectors at fold ---\n")

    # (p,q) and (q,p) are conjugate -- their unique eigenvalues should be
    # the same up to sign convention. But we can also pool SPACINGS from
    # multiple sectors of similar structure for better statistics.

    # Pool all large sectors at fold for overall assessment
    all_ratios_fold = []
    for sl in key_sectors:
        R = results[sl]
        if fold_tau in R['ratios_raw']:
            all_ratios_fold.extend(R['ratios_raw'][fold_tau])

    all_ratios_fold = np.array(all_ratios_fold)
    if len(all_ratios_fold) > 0:
        r_pooled = np.mean(all_ratios_fold)
        r_pooled_err = np.std(all_ratios_fold) / np.sqrt(len(all_ratios_fold))
        print(f"  Pooled (all large sectors): <r> = {r_pooled:.4f} +/- {r_pooled_err:.4f}, "
              f"N_ratios = {len(all_ratios_fold)}")
        print(f"  Poisson benchmark: <r> = {R_POISSON:.4f}")
        print(f"  GOE benchmark:     <r> = {R_GOE:.4f}")
        print(f"  GUE benchmark:     <r> = {R_GUE:.4f}")

    # Also pool at tau=0
    all_ratios_0 = []
    for sl in key_sectors:
        R = results[sl]
        if 0.0 in R['ratios_raw']:
            all_ratios_0.extend(R['ratios_raw'][0.0])

    all_ratios_0 = np.array(all_ratios_0)
    if len(all_ratios_0) > 0:
        r0_pooled = np.mean(all_ratios_0)
        r0_pooled_err = np.std(all_ratios_0) / np.sqrt(len(all_ratios_0))
        print(f"\n  Pooled at tau=0:   <r> = {r0_pooled:.4f} +/- {r0_pooled_err:.4f}, "
              f"N_ratios = {len(all_ratios_0)}")

    # ============================================================
    # STEP 5: <r> vs tau curves for key sectors
    # ============================================================
    print("\n--- Step 5: <r> vs tau evolution ---\n")

    for sl in ['(2,1)', '(1,1)', '(3,0)']:
        R = results[sl]
        print(f"  {sl}:")
        for i in range(len(R['tau'])):
            print(f"    tau={R['tau'][i]:.2f}: <r>={R['r_mean'][i]:.4f} +/- {R['r_std'][i]:.4f} "
                  f"(N={R['n_unique'][i]})")

    # ============================================================
    # STEP 6: D_K has +-E symmetry. Analyze positive eigenvalues only
    # as additional cross-check (positive half-spectrum)
    # ============================================================
    print("\n--- Step 6: Positive half-spectrum cross-check ---\n")

    half_results = {}
    for si, (p, q, dim_rep, n_evals) in enumerate(sector_info):
        sector_label = f"({p},{q})"
        half_results[sector_label] = {}

        for ti, tau in enumerate(tau_values):
            key = f"evals_{p}_{q}_{ti}"
            if key not in data:
                continue

            evals = data[key]
            # Take positive eigenvalues only
            pos_evals = evals[evals > DEGENERACY_TOL]
            if len(pos_evals) < 4:
                continue
            unique_pos = remove_degeneracies(pos_evals)
            if len(unique_pos) < 4:
                continue

            ratios_pos, r_pos, r_pos_err = ratio_from_raw_evals(unique_pos)
            half_results[sector_label][tau] = {
                'r_mean': r_pos, 'r_std': r_pos_err,
                'n_unique': len(unique_pos), 'ratios': ratios_pos
            }

    print(f"{'Sector':>8s} {'tau':>5s} {'N_pos':>6s} {'<r>_pos':>8s} {'err':>7s} "
          f"{'N_full':>7s} {'<r>_full':>9s}")
    print("-" * 60)
    for sl in key_sectors:
        for i, tau in enumerate(results[sl]['tau']):
            if tau in half_results[sl]:
                hr = half_results[sl][tau]
                print(f"{sl:>8s} {tau:5.2f} {hr['n_unique']:6d} {hr['r_mean']:8.4f} {hr['r_std']:7.4f} "
                      f"{results[sl]['n_unique'][i]:7d} {results[sl]['r_mean'][i]:9.4f}")
        print()

    # ============================================================
    # STEP 7: KS test against Poisson and GOE ratio distributions
    # ============================================================
    print("\n--- Step 7: KS tests at fold (tau=0.20) ---\n")

    for sl in ['(2,1)', '(3,0)', '(1,1)']:
        R = results[sl]
        if fold_tau not in R['ratios_raw']:
            continue
        ratios = R['ratios_raw'][fold_tau]
        if len(ratios) < 5:
            continue

        # Generate CDF samples for comparison
        # Poisson ratio CDF: integral of 2/(1+r)^2 from 0 to r = 2r/(1+r)
        def poisson_cdf(r_val):
            return 2 * r_val / (1 + r_val)

        # GOE ratio CDF (numerical integration)
        r_grid = np.linspace(0, 1, 10000)
        goe_pdf = ratio_distribution_goe(r_grid)
        goe_cdf_vals = np.cumsum(goe_pdf) * (r_grid[1] - r_grid[0])
        goe_cdf_vals /= goe_cdf_vals[-1]

        from scipy.interpolate import interp1d
        goe_cdf = interp1d(r_grid, goe_cdf_vals, bounds_error=False, fill_value=(0, 1))

        # KS test against Poisson
        ks_poisson, p_poisson = stats.kstest(ratios, poisson_cdf)

        # KS test against GOE
        ks_goe, p_goe = stats.kstest(ratios, goe_cdf)

        print(f"  {sl} (N={len(ratios)} ratios):")
        print(f"    vs Poisson: KS={ks_poisson:.4f}, p={p_poisson:.4f}")
        print(f"    vs GOE:     KS={ks_goe:.4f}, p={p_goe:.4f}")

        if p_poisson > p_goe:
            print(f"    -> Poisson preferred (p_Poisson/p_GOE = {p_poisson/max(p_goe,1e-15):.2f})")
        else:
            print(f"    -> GOE preferred (p_GOE/p_Poisson = {p_goe/max(p_poisson,1e-15):.2f})")

    # ============================================================
    # STEP 8: GATE VERDICT
    # ============================================================
    print("\n" + "=" * 70)
    print("GATE VERDICT: CHAOS-1")
    print("=" * 70)

    # Use the (2,1) sector at tau=0.2 as primary diagnostic (most eigenvalues)
    R21 = results['(2,1)']
    fold_i = 3  # tau=0.2
    r_primary = R21['r_mean'][fold_i]
    r_primary_err = R21['r_std'][fold_i]
    n_primary = R21['n_unique'][fold_i]

    print(f"\n  Primary diagnostic: (2,1) sector at tau=0.20 (nearest to fold at 0.190)")
    print(f"  <r> = {r_primary:.4f} +/- {r_primary_err:.4f}")
    print(f"  N_unique = {n_primary}, N_ratios = {R21['n_spacings'][fold_i]}")
    print(f"  Cross-check (poly unfold): <r> = {R21['r_mean_poly'][fold_i]:.4f}")
    print(f"  Cross-check (local unfold): <r> = {R21['r_mean_local'][fold_i]:.4f}")
    print()
    print(f"  Benchmarks:")
    print(f"    Poisson (integrable): <r> = {R_POISSON:.4f}")
    print(f"    GOE (TRS chaos):      <r> = {R_GOE:.4f}")
    print(f"    GUE (broken TRS):     <r> = {R_GUE:.4f}")
    print()

    if r_primary > 0.50:
        verdict = "PASS"
        explanation = "GOE statistics detected. Genuine quantum chaos."
    elif r_primary < 0.42:
        verdict = "FAIL"
        explanation = "Poisson statistics. Spectrum is integrable at the fold."
    else:
        verdict = "INCONCLUSIVE"
        explanation = "Intermediate statistics. Edge-of-chaos regime."

    print(f"  VERDICT: {verdict}")
    print(f"  Criterion: <r> > 0.50 => PASS, <r> < 0.42 => FAIL")
    print(f"  Assessment: {explanation}")

    # Also report tau=0 as sanity check
    r_0 = R21['r_mean'][0]
    r_0_err = R21['r_std'][0]
    print(f"\n  Sanity check at tau=0: <r> = {r_0:.4f} +/- {r_0_err:.4f} (expect ~{R_POISSON:.4f} Poisson)")

    # ============================================================
    # STEP 9: Save results
    # ============================================================
    save_dict = {
        'tau_values': tau_values,
        'verdict': np.array([verdict]),
        'r_primary': np.array([r_primary]),
        'r_primary_err': np.array([r_primary_err]),
        'r_poisson': np.array([R_POISSON]),
        'r_goe': np.array([R_GOE]),
        'r_gue': np.array([R_GUE]),
    }

    # Save per-sector results
    for sl in results:
        R = results[sl]
        tag = sl.replace('(', '').replace(')', '').replace(',', '_')
        save_dict[f'r_raw_{tag}'] = np.array(R['r_mean'])
        save_dict[f'r_err_{tag}'] = np.array(R['r_std'])
        save_dict[f'r_poly_{tag}'] = np.array(R['r_mean_poly'])
        save_dict[f'r_local_{tag}'] = np.array(R['r_mean_local'])
        save_dict[f'n_unique_{tag}'] = np.array(R['n_unique'])

    # Save pooled results
    if len(all_ratios_fold) > 0:
        save_dict['r_pooled_fold'] = np.array([r_pooled])
        save_dict['r_pooled_fold_err'] = np.array([r_pooled_err])
    if len(all_ratios_0) > 0:
        save_dict['r_pooled_0'] = np.array([r0_pooled])
        save_dict['r_pooled_0_err'] = np.array([r0_pooled_err])

    out_path = os.path.join(os.path.dirname(__file__), 's38_level_spacing.npz')
    np.savez(out_path, **save_dict)
    print(f"\n  Data saved: {out_path}")

    # ============================================================
    # STEP 10: Generate plots
    # ============================================================
    plot_path = os.path.join(os.path.dirname(__file__), 's38_level_spacing.png')

    fig = plt.figure(figsize=(18, 14))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

    # --- Panel (a): <r> vs tau for key sectors ---
    ax1 = fig.add_subplot(gs[0, :2])
    for sl, color, marker in [('(2,1)', 'C0', 'o'), ('(3,0)', 'C1', 's'),
                               ('(0,3)', 'C2', '^'), ('(1,1)', 'C3', 'D'),
                               ('(2,0)', 'C4', 'v'), ('(0,2)', 'C5', '<')]:
        R = results[sl]
        taus = np.array(R['tau'])
        rs = np.array(R['r_mean'])
        errs = np.array(R['r_std'])
        ax1.errorbar(taus, rs, yerr=errs, marker=marker, color=color,
                     label=sl, capsize=3, markersize=5, linewidth=1)

    ax1.axhline(R_POISSON, color='gray', ls='--', alpha=0.7, label=f'Poisson ({R_POISSON:.3f})')
    ax1.axhline(R_GOE, color='red', ls='--', alpha=0.7, label=f'GOE ({R_GOE:.3f})')
    ax1.axhline(R_GUE, color='blue', ls='--', alpha=0.7, label=f'GUE ({R_GUE:.3f})')
    ax1.axvline(0.190, color='green', ls=':', alpha=0.5, label='Fold (0.190)')
    ax1.axhspan(0.42, 0.50, alpha=0.08, color='orange')
    ax1.set_xlabel(r'$\tau$ (Jensen parameter)')
    ax1.set_ylabel(r'$\langle r \rangle$')
    ax1.set_title(r'(a) Level spacing ratio $\langle r \rangle$ vs $\tau$')
    ax1.legend(fontsize=7, ncol=2, loc='upper right')
    ax1.set_xlim(-0.02, 0.52)
    ax1.set_ylim(0.2, 0.7)
    ax1.grid(True, alpha=0.3)

    # --- Panel (b): Number of unique eigenvalues vs tau ---
    ax2 = fig.add_subplot(gs[0, 2])
    for sl, color in [('(2,1)', 'C0'), ('(3,0)', 'C1'), ('(1,1)', 'C3')]:
        R = results[sl]
        ax2.plot(R['tau'], R['n_unique'], 'o-', color=color, label=sl, markersize=4)
    ax2.set_xlabel(r'$\tau$')
    ax2.set_ylabel('N unique eigenvalues')
    ax2.set_title('(b) Unique levels per sector')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # --- Panel (c): P(s) histogram at tau=0 for (2,1) ---
    ax3 = fig.add_subplot(gs[1, 0])
    R21 = results['(2,1)']
    sp0 = R21['spacings_poly'].get(0.0, np.array([]))
    if len(sp0) > 3:
        ax3.hist(sp0, bins=min(15, len(sp0)//2), density=True, alpha=0.6,
                 color='C0', edgecolor='black', label='Data')
        s_range = np.linspace(0, max(sp0) * 1.1, 200)
        ax3.plot(s_range, poisson_distribution(s_range), 'k-', lw=2, label='Poisson')
        ax3.plot(s_range, wigner_surmise_goe(s_range), 'r--', lw=2, label='GOE')
    ax3.set_xlabel('s (unfolded spacing)')
    ax3.set_ylabel('P(s)')
    ax3.set_title(r'(c) P(s) at $\tau=0$ — sector (2,1)')
    ax3.legend(fontsize=8)
    ax3.set_xlim(0, 4)
    ax3.grid(True, alpha=0.3)

    # --- Panel (d): P(s) histogram at tau=0.2 for (2,1) ---
    ax4 = fig.add_subplot(gs[1, 1])
    sp_fold = R21['spacings_poly'].get(0.2, np.array([]))
    if len(sp_fold) > 3:
        ax4.hist(sp_fold, bins=min(15, len(sp_fold)//2), density=True, alpha=0.6,
                 color='C0', edgecolor='black', label='Data')
        s_range = np.linspace(0, max(sp_fold) * 1.1, 200)
        ax4.plot(s_range, poisson_distribution(s_range), 'k-', lw=2, label='Poisson')
        ax4.plot(s_range, wigner_surmise_goe(s_range), 'r--', lw=2, label='GOE')
    ax4.set_xlabel('s (unfolded spacing)')
    ax4.set_ylabel('P(s)')
    ax4.set_title(r'(d) P(s) at $\tau=0.20$ — sector (2,1)')
    ax4.legend(fontsize=8)
    ax4.set_xlim(0, 4)
    ax4.grid(True, alpha=0.3)

    # --- Panel (e): Ratio distribution at fold for (2,1) ---
    ax5 = fig.add_subplot(gs[1, 2])
    ratios_fold_21 = R21['ratios_raw'].get(0.2, np.array([]))
    if len(ratios_fold_21) > 3:
        ax5.hist(ratios_fold_21, bins=min(12, len(ratios_fold_21)//3), density=True,
                 alpha=0.6, color='C0', edgecolor='black', label='Data')
        r_range = np.linspace(0.001, 0.999, 200)
        ax5.plot(r_range, ratio_distribution_poisson(r_range), 'k-', lw=2, label='Poisson')
        ax5.plot(r_range, ratio_distribution_goe(r_range), 'r--', lw=2, label='GOE')
    ax5.set_xlabel('r')
    ax5.set_ylabel('P(r)')
    ax5.set_title(r'(e) P(r) at $\tau=0.20$ — sector (2,1)')
    ax5.legend(fontsize=8)
    ax5.set_xlim(0, 1)
    ax5.grid(True, alpha=0.3)

    # --- Panel (f): Cross-check: 3 unfolding methods for (2,1) ---
    ax6 = fig.add_subplot(gs[2, 0])
    taus_21 = np.array(R21['tau'])
    ax6.errorbar(taus_21, R21['r_mean'], yerr=R21['r_std'], marker='o',
                 color='C0', label='Raw (no unfold)', capsize=3)
    ax6.plot(taus_21, R21['r_mean_poly'], 's--', color='C1', label='Poly unfold', markersize=4)
    ax6.plot(taus_21, R21['r_mean_local'], '^:', color='C2', label='Local unfold', markersize=4)
    ax6.axhline(R_POISSON, color='gray', ls='--', alpha=0.5)
    ax6.axhline(R_GOE, color='red', ls='--', alpha=0.5)
    ax6.set_xlabel(r'$\tau$')
    ax6.set_ylabel(r'$\langle r \rangle$')
    ax6.set_title(r'(f) Cross-check: unfolding methods — (2,1)')
    ax6.legend(fontsize=8)
    ax6.set_ylim(0.2, 0.7)
    ax6.grid(True, alpha=0.3)

    # --- Panel (g): Pooled ratio distribution at fold ---
    ax7 = fig.add_subplot(gs[2, 1])
    if len(all_ratios_fold) > 3:
        ax7.hist(all_ratios_fold, bins=min(20, len(all_ratios_fold)//3), density=True,
                 alpha=0.6, color='C0', edgecolor='black', label=f'Pooled (N={len(all_ratios_fold)})')
        r_range = np.linspace(0.001, 0.999, 200)
        ax7.plot(r_range, ratio_distribution_poisson(r_range), 'k-', lw=2, label='Poisson')
        ax7.plot(r_range, ratio_distribution_goe(r_range), 'r--', lw=2, label='GOE')
    ax7.set_xlabel('r')
    ax7.set_ylabel('P(r)')
    ax7.set_title(r'(g) Pooled P(r) at fold ($\tau=0.20$)')
    ax7.legend(fontsize=8)
    ax7.set_xlim(0, 1)
    ax7.grid(True, alpha=0.3)

    # --- Panel (h): Summary table ---
    ax8 = fig.add_subplot(gs[2, 2])
    ax8.axis('off')

    table_data = [
        ['Diagnostic', 'Value'],
        [r'$\langle r \rangle$ (2,1) fold', f'{r_primary:.4f} +/- {r_primary_err:.4f}'],
        [r'$\langle r \rangle$ pooled fold', f'{r_pooled:.4f} +/- {r_pooled_err:.4f}' if len(all_ratios_fold) > 0 else 'N/A'],
        [r'$\langle r \rangle$ (2,1) $\tau=0$', f'{R21["r_mean"][0]:.4f} +/- {R21["r_std"][0]:.4f}'],
        ['Poisson', f'{R_POISSON:.4f}'],
        ['GOE', f'{R_GOE:.4f}'],
        ['GUE', f'{R_GUE:.4f}'],
        ['Verdict', verdict],
    ]

    table = ax8.table(cellText=table_data, cellLoc='center', loc='center',
                      colWidths=[0.5, 0.5])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.5)

    # Color verdict cell
    verdict_cell = table[7, 1]
    if verdict == 'PASS':
        verdict_cell.set_facecolor('#90EE90')
    elif verdict == 'FAIL':
        verdict_cell.set_facecolor('#FFB6C1')
    else:
        verdict_cell.set_facecolor('#FFFACD')

    ax8.set_title('(h) Summary', fontweight='bold')

    fig.suptitle(r'CHAOS-1: $D_K$ Level Spacing Statistics on Jensen-deformed SU(3)',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {plot_path}")
    plt.close()

    # ============================================================
    # STEP 11: Additional analysis -- symmetry subspace decomposition
    # ============================================================
    print("\n--- Step 11: Symmetry analysis ---\n")

    # The D_K spectrum has particle-hole symmetry (+-E pairs).
    # The residual U(1)_7 symmetry means each unique eigenvalue has a
    # multiplicity given by the number of K_7 quantum numbers sharing that energy.
    # The PROPER level spacing analysis requires decomposition by K_7 eigenvalue.
    # Without that data, we work with unique eigenvalues, which is conservative:
    # if levels from different K_7 sectors accidentally cross, they appear as
    # near-degeneracies that would be removed, potentially INFLATING <r>
    # toward Poisson. So our <r> is a LOWER BOUND on the true (per-K7) value
    # if the spectrum is chaotic, or ACCURATE if it is integrable.

    # Count degeneracy multiplicities at fold
    for si, (p, q, _, _) in enumerate(sector_info):
        sl = f"({p},{q})"
        key = f"evals_{p}_{q}_{fold_idx}"
        if key not in data:
            continue
        evals = data[key]
        _, counts = np.unique(np.round(evals, 10), return_counts=True)
        deg_dist = {}
        for c in counts:
            deg_dist[c] = deg_dist.get(c, 0) + 1
        print(f"  {sl}: degeneracy distribution: {dict(sorted(deg_dist.items()))}")

    print("\n  NOTE: Remaining degeneracies come from U(1)_7 conserved charge.")
    print("  True level spacing statistics require decomposition by K_7 eigenvalue.")
    print("  Without K_7 labels, we analyze unique eigenvalues -- this is conservative.")
    print("  If the spectrum is truly integrable, our <r> is accurate.")
    print("  If chaotic, our <r> may be slightly biased by unresolved near-crossings.")

    print("\n" + "=" * 70)
    print("COMPUTATION COMPLETE")
    print("=" * 70)

    return verdict, r_primary, r_primary_err, results


if __name__ == '__main__':
    verdict, r_primary, r_primary_err, results = main()
