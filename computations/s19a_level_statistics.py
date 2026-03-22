"""
Session 19a — S-1: Level Statistics q(tau)
==========================================

THE single most decisive computation of Session 19.

Computes the Brody parameter q(tau) that interpolates between:
  - q=0: Poisson statistics (integrable, uncoupled sectors)
  - q=1: GOE statistics (chaotic, fully coupled sectors)

CRITICAL IMPLEMENTATION NOTE:
  The Dirac operator D_K(tau) is block-diagonal in the Peter-Weyl basis at EVERY
  tau (not just tau=0). Each (p,q) sector gives dim(p,q)*16 eigenvalues, but most
  are degenerate (spinor structure). The raw 11,424 eigenvalues contain only ~45
  distinct levels at tau=0 and ~1445 per-sector-distinct levels at tau>0.

  Level statistics must be computed on DISTINCT eigenvalue levels, not raw data.
  We analyze:
    (A) Global distinct: all unique eigenvalues across all sectors, sorted
    (B) Per-sector distinct: unique eigenvalues within each sector
    (C) Pooled intra-sector: spacings from all sectors pooled together
    (D) Inter-sector: consecutive distinct eigenvalues from different sectors

  The physically meaningful test is (A+D): does the GLOBAL DISTINCT spectrum
  transition from Poisson to GOE as tau increases? If sectors remain uncoupled
  (block-diagonal), the superposition of independent spectra gives Poisson.
  If inter-sector coupling breaks block-diagonality, GOE emerges.

Constraint Condition: q(tau) ~ 0 for all tau => spectral complexity CLOSED.
Confirm condition: q(tau) rises with inflection at tau_c in [0.15, 0.30].

Environment: Venv Python (numpy + scipy + matplotlib).

Author: phonon-exflation-sim agent (Session 19a)
Date: 2026-02-15
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gamma as gamma_fn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from s19a_sweep_data import load_sweep_data


# =============================================================================
# EIGENVALUE DEDUPLICATION
# =============================================================================

def extract_distinct_levels(eigenvalues, sector_p, sector_q, tol=1e-8):
    """
    Extract distinct eigenvalue levels from the raw spectrum.

    Within each (p,q) sector, many eigenvalues are degenerate due to spinor
    structure. We deduplicate within each sector (tolerance-based rounding),
    then merge across sectors.

    Returns:
        global_distinct: sorted array of globally distinct |lambda| values
        sector_distinct: dict mapping (p,q) -> sorted array of distinct |lambda|
        global_labels: array of (p,q) labels for each global_distinct entry
                       (sector of origin; for shared eigenvalues, takes first sector)
    """
    sectors = {}
    for e, p, q in zip(eigenvalues, sector_p, sector_q):
        key = (int(p), int(q))
        if key not in sectors:
            sectors[key] = []
        sectors[key].append(float(e))

    sector_distinct = {}
    for key in sorted(sectors.keys()):
        vals = np.array(sectors[key])
        # Round to tolerance and take unique
        rounded = np.round(vals / tol) * tol
        unique_vals = np.unique(rounded)
        sector_distinct[key] = unique_vals

    # Global merge: collect all per-sector distinct values with labels
    all_vals = []
    all_labels = []
    for key in sorted(sector_distinct.keys()):
        for v in sector_distinct[key]:
            all_vals.append(v)
            all_labels.append(key)

    all_vals = np.array(all_vals)
    sort_idx = np.argsort(all_vals)
    all_vals_sorted = all_vals[sort_idx]
    all_labels_sorted = [all_labels[i] for i in sort_idx]

    # Global dedup (eigenvalues shared across sectors)
    global_distinct = []
    global_labels = []
    prev = -np.inf
    for v, lab in zip(all_vals_sorted, all_labels_sorted):
        if v - prev > tol:
            global_distinct.append(v)
            global_labels.append(lab)
            prev = v

    return (np.array(global_distinct),
            sector_distinct,
            global_labels)


# =============================================================================
# SPECTRAL UNFOLDING
# =============================================================================

def unfold_spectrum(eigenvalues, poly_degree=6):
    """
    Unfold a sorted eigenvalue spectrum to normalize mean spacing to 1.

    Uses Chebyshev polynomial fit to the cumulative eigenvalue count N(lambda).
    The unfolded eigenvalues are x_n = N_smooth(lambda_n).

    Args:
        eigenvalues: sorted 1D array of distinct eigenvalues
        poly_degree: degree of polynomial for smoothing

    Returns:
        unfolded: array of unfolded eigenvalues (mean spacing ~ 1)
    """
    n = len(eigenvalues)
    if n < 10:
        return np.arange(n, dtype=np.float64)

    cumulative = np.arange(1, n + 1, dtype=np.float64)

    # Adaptive polynomial degree: don't overfit small datasets
    deg = min(poly_degree, max(2, n // 10))

    coeffs = np.polynomial.chebyshev.chebfit(eigenvalues, cumulative, deg)
    unfolded = np.polynomial.chebyshev.chebval(eigenvalues, coeffs)

    # Ensure strict monotonicity
    for i in range(1, len(unfolded)):
        if unfolded[i] <= unfolded[i - 1]:
            unfolded[i] = unfolded[i - 1] + 1e-10

    return unfolded


def compute_spacings(unfolded):
    """
    Compute normalized nearest-neighbor spacings from unfolded eigenvalues.

    Args:
        unfolded: sorted array of unfolded eigenvalues

    Returns:
        spacings: array of spacings normalized to mean 1
    """
    spacings = np.diff(unfolded)
    mean_s = np.mean(spacings)
    if mean_s > 0:
        spacings = spacings / mean_s
    return spacings


# =============================================================================
# BRODY DISTRIBUTION + FITTING
# =============================================================================

def brody_pdf(s, q):
    """
    Brody distribution P(s, q) = (q+1) * b * s^q * exp(-b * s^{q+1}).
    b = [Gamma((q+2)/(q+1))]^{q+1}
    q=0: Poisson, q=1: GOE-like.
    """
    q = np.clip(q, 0.0, 2.0)
    b = gamma_fn((q + 2) / (q + 1)) ** (q + 1)
    s_safe = np.maximum(s, 0)
    return (q + 1) * b * np.power(s_safe, q) * np.exp(-b * np.power(s_safe, q + 1))


def brody_cdf(s, q):
    """Brody CDF: F(s, q) = 1 - exp(-b * s^{q+1})."""
    q = np.clip(q, 0.0, 2.0)
    b = gamma_fn((q + 2) / (q + 1)) ** (q + 1)
    return 1.0 - np.exp(-b * np.power(np.maximum(s, 0), q + 1))


def fit_brody_mle(spacings):
    """
    Fit Brody parameter q by maximum likelihood estimation.

    Returns:
        q_best: best-fit Brody parameter
        neg_loglik: negative log-likelihood at best fit
    """
    spacings = spacings[spacings > 1e-15]
    N = len(spacings)
    if N < 5:
        return 0.0, np.inf

    log_s = np.log(spacings)

    def neg_loglik(q):
        if q < 0 or q > 2:
            return 1e20
        b = gamma_fn((q + 2) / (q + 1)) ** (q + 1)
        s_qp1 = np.power(spacings, q + 1)
        ll = N * np.log(q + 1) + N * np.log(b) + q * np.sum(log_s) - b * np.sum(s_qp1)
        return -ll

    result = minimize_scalar(neg_loglik, bounds=(0.0, 2.0), method='bounded')
    return result.x, result.fun


def fit_brody_ks(spacings):
    """
    Fit Brody parameter q by minimizing Kolmogorov-Smirnov statistic.

    Returns:
        q_best: best-fit Brody parameter
        ks_stat: KS statistic at best fit
    """
    spacings = np.sort(spacings[spacings > 1e-15])
    N = len(spacings)
    if N < 5:
        return 0.0, 1.0

    empirical_cdf = np.arange(1, N + 1) / N

    def ks_stat(q):
        theoretical_cdf = brody_cdf(spacings, q)
        return np.max(np.abs(empirical_cdf - theoretical_cdf))

    result = minimize_scalar(ks_stat, bounds=(0.0, 2.0), method='bounded')
    return result.x, result.fun


# =============================================================================
# NUMBER VARIANCE
# =============================================================================

def number_variance(unfolded, L_values, n_windows=1000):
    """
    Compute number variance Sigma^2(L).
    Poisson: Sigma^2 = L. GOE: Sigma^2 ~ (2/pi^2)(log(2*pi*L) + gamma + 1 - pi^2/8).
    """
    sigma2 = np.zeros(len(L_values))
    x_min, x_max = unfolded[0], unfolded[-1]
    total_range = x_max - x_min

    rng = np.random.default_rng(42)

    for i, L in enumerate(L_values):
        if L >= total_range * 0.9:
            sigma2[i] = np.nan
            continue

        starts = rng.uniform(x_min, x_max - L, size=n_windows)
        counts = np.zeros(n_windows)
        for j, start in enumerate(starts):
            counts[j] = np.sum((unfolded >= start) & (unfolded < start + L))

        mean_count = np.mean(counts)
        sigma2[i] = np.mean((counts - mean_count) ** 2)

    return sigma2


def sigma2_poisson(L):
    return np.asarray(L, dtype=float)


def sigma2_goe(L):
    L = np.asarray(L, dtype=float)
    gamma_euler = 0.5772156649
    return (2.0 / np.pi**2) * (np.log(2 * np.pi * L) + gamma_euler + 1.0 - np.pi**2 / 8.0)


# =============================================================================
# INTER-SECTOR ANALYSIS ON DISTINCT LEVELS
# =============================================================================

def compute_intersector_spacings_distinct(global_distinct, global_labels):
    """
    Compute spacings between consecutive DISTINCT eigenvalues from DIFFERENT sectors.

    Args:
        global_distinct: sorted array of globally distinct eigenvalues
        global_labels: list of (p,q) tuples for each

    Returns:
        inter_spacings: raw spacings between cross-sector consecutive pairs
        frac_inter: fraction of consecutive pairs that are inter-sector
    """
    inter_spacings = []
    n_total = 0

    for i in range(len(global_distinct) - 1):
        n_total += 1
        if global_labels[i] != global_labels[i + 1]:
            spacing = global_distinct[i + 1] - global_distinct[i]
            inter_spacings.append(spacing)

    frac_inter = len(inter_spacings) / max(n_total, 1)
    return np.array(inter_spacings), frac_inter


# =============================================================================
# POOLED INTRA-SECTOR ANALYSIS
# =============================================================================

def pooled_intrasector_spacings(sector_distinct):
    """
    Pool unfolded spacings from all sectors.

    For each sector with >= 5 distinct eigenvalues, unfold and compute spacings.
    Pool all spacings together. This tests whether individual sectors show GOE
    structure internally (which would happen if D_{(p,q)} is chaotic).

    Returns:
        pooled: array of all pooled spacings (normalized per-sector)
        n_sectors_used: number of sectors with enough data
    """
    pooled = []
    n_used = 0

    for key, evals in sorted(sector_distinct.items()):
        if len(evals) >= 5:
            unfolded = unfold_spectrum(evals, poly_degree=min(4, len(evals) // 3))
            spacings = compute_spacings(unfolded)
            pooled.extend(spacings.tolist())
            n_used += 1

    return np.array(pooled), n_used


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_level_statistics(data):
    """
    Full level statistics analysis at each tau, using distinct eigenvalue levels.
    """
    tau_values = data['tau_values']
    n_tau = len(tau_values)

    # Storage for 4 analysis types
    # (A) Global distinct
    q_global = np.zeros(n_tau)
    q_global_mle = np.zeros(n_tau)
    ks_global = np.zeros(n_tau)
    n_global = np.zeros(n_tau, dtype=int)

    # (B) Pooled intra-sector
    q_intra = np.zeros(n_tau)
    q_intra_mle = np.zeros(n_tau)
    ks_intra = np.zeros(n_tau)
    n_intra = np.zeros(n_tau, dtype=int)
    n_sectors_used = np.zeros(n_tau, dtype=int)

    # (C) Inter-sector distinct
    q_inter = np.zeros(n_tau)
    q_inter_mle = np.zeros(n_tau)
    ks_inter = np.zeros(n_tau)
    n_inter = np.zeros(n_tau, dtype=int)
    frac_inter = np.zeros(n_tau)

    all_spacings_global = []
    all_spacings_intra = []
    all_spacings_inter = []
    all_unfolded_global = []

    for i, tau in enumerate(tau_values):
        evals = data['eigenvalues'][i]
        sp = data['sector_p'][i]
        sq = data['sector_q'][i]

        # Extract distinct levels
        global_dist, sector_dist, global_labels = extract_distinct_levels(evals, sp, sq)
        n_global[i] = len(global_dist)

        # --- (A) GLOBAL DISTINCT ---
        if len(global_dist) >= 10:
            unfolded_g = unfold_spectrum(global_dist, poly_degree=8)
            all_unfolded_global.append(unfolded_g)
            spacings_g = compute_spacings(unfolded_g)
            all_spacings_global.append(spacings_g)

            q_ks, ks = fit_brody_ks(spacings_g)
            q_global[i] = q_ks
            ks_global[i] = ks
            q_ml, _ = fit_brody_mle(spacings_g)
            q_global_mle[i] = q_ml
        else:
            all_unfolded_global.append(np.array([]))
            all_spacings_global.append(np.array([]))

        # --- (B) POOLED INTRA-SECTOR ---
        pooled, n_s = pooled_intrasector_spacings(sector_dist)
        n_intra[i] = len(pooled)
        n_sectors_used[i] = n_s
        all_spacings_intra.append(pooled)

        if len(pooled) >= 10:
            q_ks_i, ks_i = fit_brody_ks(pooled)
            q_intra[i] = q_ks_i
            ks_intra[i] = ks_i
            q_ml_i, _ = fit_brody_mle(pooled)
            q_intra_mle[i] = q_ml_i

        # --- (C) INTER-SECTOR DISTINCT ---
        inter_sp, fr = compute_intersector_spacings_distinct(global_dist, global_labels)
        n_inter[i] = len(inter_sp)
        frac_inter[i] = fr
        all_spacings_inter.append(inter_sp)

        if len(inter_sp) >= 10:
            # Normalize
            mean_is = np.mean(inter_sp)
            if mean_is > 0:
                inter_norm = inter_sp / mean_is
            else:
                inter_norm = inter_sp
            q_ks_inter, ks_inter_val = fit_brody_ks(inter_norm)
            q_inter[i] = q_ks_inter
            ks_inter[i] = ks_inter_val
            q_ml_inter, _ = fit_brody_mle(inter_norm)
            q_inter_mle[i] = q_ml_inter

        print(f"  tau={tau:.2f}: n_distinct={n_global[i]:4d}, "
              f"q_global={q_global[i]:.4f} (KS={ks_global[i]:.3f}), "
              f"q_intra={q_intra[i]:.4f} ({n_s} sectors, {n_intra[i]} spacings), "
              f"q_inter={q_inter[i]:.4f} ({n_inter[i]} pairs, frac={fr:.3f})")

    # --- DERIVATIVES + INFLECTION ---
    dtau = tau_values[1] - tau_values[0]
    dq_global = np.gradient(q_global, dtau)
    d2q_global = np.gradient(dq_global, dtau)
    dq_intra = np.gradient(q_intra, dtau)
    d2q_intra = np.gradient(dq_intra, dtau)
    dq_inter = np.gradient(q_inter, dtau)
    d2q_inter = np.gradient(dq_inter, dtau)

    tau_c_global = find_inflection(tau_values, d2q_global)
    tau_c_intra = find_inflection(tau_values, d2q_intra)
    tau_c_inter = find_inflection(tau_values, d2q_inter)

    # --- NUMBER VARIANCE ---
    L_values = np.linspace(0.5, min(20.0, n_global[0] * 0.3), 40)

    if len(all_unfolded_global[0]) > 10:
        sigma2_tau0 = number_variance(all_unfolded_global[0], L_values)
    else:
        sigma2_tau0 = np.full(len(L_values), np.nan)

    # At midpoint
    mid_idx = len(tau_values) // 2
    if len(all_unfolded_global[mid_idx]) > 10:
        sigma2_mid = number_variance(all_unfolded_global[mid_idx], L_values)
    else:
        sigma2_mid = np.full(len(L_values), np.nan)

    # At tau=2.0
    if len(all_unfolded_global[-1]) > 10:
        sigma2_end = number_variance(all_unfolded_global[-1], L_values)
    else:
        sigma2_end = np.full(len(L_values), np.nan)

    return {
        'tau_values': tau_values,
        # Global
        'q_global': q_global, 'q_global_mle': q_global_mle,
        'ks_global': ks_global, 'n_global': n_global,
        'dq_global': dq_global, 'd2q_global': d2q_global,
        'tau_c_global': tau_c_global,
        # Intra-sector
        'q_intra': q_intra, 'q_intra_mle': q_intra_mle,
        'ks_intra': ks_intra, 'n_intra': n_intra, 'n_sectors_used': n_sectors_used,
        'dq_intra': dq_intra, 'd2q_intra': d2q_intra,
        'tau_c_intra': tau_c_intra,
        # Inter-sector
        'q_inter': q_inter, 'q_inter_mle': q_inter_mle,
        'ks_inter': ks_inter, 'n_inter': n_inter, 'frac_inter': frac_inter,
        'dq_inter': dq_inter, 'd2q_inter': d2q_inter,
        'tau_c_inter': tau_c_inter,
        # Spacings
        'all_spacings_global': all_spacings_global,
        'all_spacings_intra': all_spacings_intra,
        'all_spacings_inter': all_spacings_inter,
        'all_unfolded_global': all_unfolded_global,
        # Number variance
        'L_values': L_values,
        'sigma2_tau0': sigma2_tau0,
        'sigma2_mid': sigma2_mid,
        'sigma2_end': sigma2_end,
        'mid_idx': mid_idx,
    }


def find_inflection(x, d2y):
    """Find x-value where d2y changes sign (inflection point)."""
    for i in range(len(d2y) - 1):
        if np.isnan(d2y[i]) or np.isnan(d2y[i + 1]):
            continue
        if d2y[i] * d2y[i + 1] < 0:
            frac = d2y[i] / (d2y[i] - d2y[i + 1])
            return x[i] + frac * (x[i + 1] - x[i])
    return None


# =============================================================================
# PLOTTING
# =============================================================================

def plot_results(results, output_dir):
    """Generate all S-1 diagnostic plots."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    tau = results['tau_values']

    # ====== PLOT 1: Main diagnostics (4 panels) ======
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel (a): q(tau) — three analysis types
    ax = axes[0, 0]
    ax.plot(tau, results['q_global'], 'bo-', label='Global distinct (KS)', markersize=5, lw=1.5)
    ax.plot(tau, results['q_intra'], 'gs-', label='Pooled intra-sector (KS)', markersize=5, lw=1.5)
    ax.plot(tau, results['q_inter'], 'r^-', label='Inter-sector (KS)', markersize=5, lw=1.5)
    ax.plot(tau, results['q_global_mle'], 'b--', label='Global (MLE)', lw=0.8, alpha=0.6)
    ax.plot(tau, results['q_intra_mle'], 'g--', label='Intra (MLE)', lw=0.8, alpha=0.6)

    ax.axhline(y=0, color='gray', ls=':', lw=0.8, label='Poisson')
    ax.axhline(y=1, color='gray', ls='--', lw=0.8, label='GOE')
    ax.axvspan(0.15, 0.30, alpha=0.1, color='green', label='Target [0.15, 0.30]')

    for name, tc, color in [('global', results['tau_c_global'], 'blue'),
                             ('intra', results['tau_c_intra'], 'green'),
                             ('inter', results['tau_c_inter'], 'red')]:
        if tc is not None:
            ax.axvline(x=tc, color=color, ls=':', alpha=0.5, label=f'tau_c ({name})={tc:.2f}')

    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('Brody parameter q')
    ax.set_title('S-1: Brody Parameter q(tau)')
    ax.legend(fontsize=6, loc='best', ncol=2)
    ax.set_ylim(-0.1, max(np.max(results['q_global']),
                          np.max(results['q_intra']),
                          np.nanmax(results['q_inter']), 1.1) + 0.15)
    ax.grid(True, alpha=0.3)

    # Panel (b): Sample sizes and degeneracy
    ax = axes[0, 1]
    ax.plot(tau, results['n_global'], 'bo-', label='Distinct levels', markersize=5, lw=1.5)
    ax.plot(tau, results['n_intra'], 'gs-', label='Intra-sector spacings', markersize=4, lw=1)
    ax.plot(tau, results['n_inter'], 'r^-', label='Inter-sector pairs', markersize=4, lw=1)

    ax2 = ax.twinx()
    ax2.plot(tau, results['frac_inter'], 'k--', label='Frac inter-sector', lw=1, alpha=0.5)
    ax2.set_ylabel('Fraction inter-sector', color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    ax.set_xlabel('Jensen parameter tau')
    ax.set_ylabel('Count')
    ax.set_title('Distinct Eigenvalue Counts')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel (c): P(s) histograms at tau=0, mid, end — GLOBAL DISTINCT
    ax = axes[1, 0]
    s_grid = np.linspace(0.01, 5, 200)

    for idx, color, lbl in [(0, 'blue', f'tau=0.0'),
                             (results['mid_idx'], 'green', f'tau={tau[results["mid_idx"]]:.1f}'),
                             (-1, 'red', f'tau=2.0')]:
        spacings = results['all_spacings_global'][idx]
        q_val = results['q_global'][idx]
        if len(spacings) > 5:
            ax.hist(spacings, bins=40, density=True, alpha=0.35, color=color,
                    label=f'{lbl} (q={q_val:.3f})', edgecolor='none')

    ax.plot(s_grid, brody_pdf(s_grid, 0), 'k-', lw=1.5, label='Poisson (q=0)')
    ax.plot(s_grid, brody_pdf(s_grid, 1), 'k--', lw=1.5, label='GOE (q=1)')

    ax.set_xlabel('Normalized spacing s')
    ax.set_ylabel('P(s)')
    ax.set_title('P(s) — Global Distinct Spectrum')
    ax.legend(fontsize=7)
    ax.set_xlim(0, 5)
    ax.grid(True, alpha=0.3)

    # Panel (d): Number variance
    ax = axes[1, 1]
    L = results['L_values']
    for sigma2, lbl, color, marker in [
        (results['sigma2_tau0'], 'tau=0.0', 'blue', 'o'),
        (results['sigma2_mid'], f'tau={tau[results["mid_idx"]]:.1f}', 'green', 's'),
        (results['sigma2_end'], 'tau=2.0', 'red', '^'),
    ]:
        mask = ~np.isnan(sigma2)
        if np.any(mask):
            ax.plot(L[mask], sigma2[mask], f'{color[0]}{marker}-', markersize=3,
                    label=lbl, lw=1.5)

    L_th = np.linspace(0.5, float(L[-1]), 100)
    ax.plot(L_th, sigma2_poisson(L_th), 'k-', lw=1.5, label='Poisson')
    L_th_goe = L_th[L_th > 0.2]
    ax.plot(L_th_goe, sigma2_goe(L_th_goe), 'k--', lw=1.5, label='GOE')

    ax.set_xlabel('Interval length L')
    ax.set_ylabel('Number variance Sigma^2(L)')
    ax.set_title('Number Variance')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_level_statistics.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")

    # ====== PLOT 2: Intra-sector P(s) detail ======
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for ax_idx, tau_idx in enumerate([0, results['mid_idx'], len(tau) - 1]):
        ax = axes[ax_idx]
        spacings = results['all_spacings_intra'][tau_idx]
        tau_val = tau[tau_idx]
        q_val = results['q_intra'][tau_idx]

        if len(spacings) > 5:
            ax.hist(spacings, bins=40, density=True, alpha=0.5, color='coral',
                    edgecolor='black', lw=0.5)
            ax.plot(s_grid, brody_pdf(s_grid, 0), 'k-', lw=1.5, label='Poisson')
            ax.plot(s_grid, brody_pdf(s_grid, 1), 'k--', lw=1.5, label='GOE')
            if q_val > 0.01:
                ax.plot(s_grid, brody_pdf(s_grid, q_val), 'r-', lw=2,
                        label=f'Brody q={q_val:.3f}')
        ax.set_xlabel('Normalized spacing s')
        ax.set_ylabel('P(s)')
        ax.set_title(f'Intra-sector P(s) at tau={tau_val:.1f} (q={q_val:.3f})')
        ax.legend(fontsize=8)
        ax.set_xlim(0, 5)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_level_statistics_intrasector.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")

    # ====== PLOT 3: Derivatives ======
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(tau, results['dq_global'], 'b-', label='dq/dtau (global)', lw=1.5)
    ax.plot(tau, results['dq_intra'], 'g-', label='dq/dtau (intra)', lw=1.5)
    ax.plot(tau, results['dq_inter'], 'r-', label='dq/dtau (inter)', lw=1.5)
    ax.axhline(y=0, color='gray', ls=':', lw=0.8)
    ax.set_xlabel('tau')
    ax.set_ylabel('dq/dtau')
    ax.set_title('First Derivative')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(tau, results['d2q_global'], 'b-', label='d2q/dtau2 (global)', lw=1.5)
    ax.plot(tau, results['d2q_intra'], 'g-', label='d2q/dtau2 (intra)', lw=1.5)
    ax.plot(tau, results['d2q_inter'], 'r-', label='d2q/dtau2 (inter)', lw=1.5)
    ax.axhline(y=0, color='gray', ls=':', lw=0.8)
    ax.set_xlabel('tau')
    ax.set_ylabel('d2q/dtau2')
    ax.set_title('Second Derivative (inflection search)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, 's19a_level_statistics_derivatives.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    DATA_PATH = os.path.join(SCRIPT_DIR, 's19a_sweep_data.npz')

    print("S-1: Level Statistics (Corrected — Distinct Levels)")
    print(f"  Loading: {DATA_PATH}")

    data = load_sweep_data(DATA_PATH)
    print(f"  Loaded: {len(data['tau_values'])} tau-values")

    print("\n--- Computing level statistics ---")
    results = analyze_level_statistics(data)

    print(f"\n{'='*70}")
    print("RESULTS SUMMARY")
    print(f"{'='*70}")

    print(f"\n(A) Global distinct q(tau):")
    for i, tau in enumerate(results['tau_values']):
        print(f"    tau={tau:.2f}: q={results['q_global'][i]:.4f}, "
              f"n={results['n_global'][i]}, KS={results['ks_global'][i]:.3f}")
    print(f"    Inflection tau_c = {results['tau_c_global']}")

    print(f"\n(B) Pooled intra-sector q(tau):")
    for i, tau in enumerate(results['tau_values']):
        print(f"    tau={tau:.2f}: q={results['q_intra'][i]:.4f}, "
              f"n_spacings={results['n_intra'][i]}, "
              f"n_sectors={results['n_sectors_used'][i]}")
    print(f"    Inflection tau_c = {results['tau_c_intra']}")

    print(f"\n(C) Inter-sector distinct q(tau):")
    for i, tau in enumerate(results['tau_values']):
        print(f"    tau={tau:.2f}: q={results['q_inter'][i]:.4f}, "
              f"n_pairs={results['n_inter'][i]}, "
              f"frac_inter={results['frac_inter'][i]:.3f}")
    print(f"    Inflection tau_c = {results['tau_c_inter']}")

    # CLOSURE/CONFIRM
    q_max_global = np.max(results['q_global'])
    q_max_intra = np.max(results['q_intra'])
    q_max_inter = np.nanmax(results['q_inter'])

    print(f"\n{'='*70}")
    print("CLOSURE / CONFIRM ASSESSMENT")
    print(f"{'='*70}")
    print(f"  Max q (global):  {q_max_global:.4f}")
    print(f"  Max q (intra):   {q_max_intra:.4f}")
    print(f"  Max q (inter):   {q_max_inter:.4f}")

    if q_max_global < 0.05 and q_max_intra < 0.05:
        print("\n  >> CLOSED: q ~ 0 for all tau across all analysis types.")
        print("  >> No Poisson-to-GOE transition detected.")
        print("  >> NOTE: This is EXPECTED for block-diagonal D_K(tau).")
        print("  >>   The Peter-Weyl decomposition keeps sectors decoupled")
        print("  >>   at the eigenvalue level. The spectral complexity")
        print("  >>   hypothesis requires OFF-DIAGONAL inter-sector coupling")
        print("  >>   (Kosmann-Lichnerowicz), which only appears when")
        print("  >>   the FULL D_K matrix is assembled, NOT in the")
        print("  >>   block-diagonalized form used by collect_spectrum().")
        print("  >> This is NOT a closure of the framework — it's a diagnostic")
        print("  >>   of what information the current eigenvalue data contains.")
    elif q_max_global > 0.2 or q_max_intra > 0.2:
        tc_best = results['tau_c_global'] or results['tau_c_intra']
        if tc_best is not None and 0.15 <= tc_best <= 0.30:
            print(f"\n  >> CONFIRM: tau_c = {tc_best:.3f} in [0.15, 0.30].")
        elif tc_best is not None:
            print(f"\n  >> INTERMEDIATE: Transition at tau_c = {tc_best:.3f}")
        else:
            print(f"\n  >> INTERMEDIATE: q rises but no clear inflection.")
    else:
        print(f"\n  >> WEAK: q_max < 0.2. Marginal evidence for transition.")

    print("\n--- Generating plots ---")
    plot_results(results, SCRIPT_DIR)

    print("\nS-1 complete.")
