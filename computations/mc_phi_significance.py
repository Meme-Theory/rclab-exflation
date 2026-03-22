"""
Monte Carlo Significance Test: Phi in SU(3) Dirac Spectrum
==========================================================
Author: Gen-Physicist Agent, Session 14
Date: 2026-02-12

Rigorous null-model test for phi = 1.53158 appearance in the Dirac spectrum
on (SU(3), g) with left-invariant metrics.

Null models tested:
  1. DIAGONAL METRICS: su(3) = u(1) + su(2) + C^2 with independent scale factors
     (alpha, beta, gamma). Jensen is the 1-parameter subfamily
     alpha = e^{2s}, beta = e^{-2s}, gamma = e^{s}.

  2. VOLUME-PRESERVING DIAGONAL: alpha * beta^3 * gamma^4 = 1 constraint
     (Jensen is a 1-dim curve in this 2-dim surface).

  3. GENERAL RANDOM METRICS (perturbative): g_0 + epsilon * h where h is random
     symmetric positive perturbation. Tests whether phi survives off the
     su(3) block-diagonal structure.

For each null sample: compute Dirac spectrum, count pairwise phi-hits,
build null distribution, compare to Jensen data.

Key statistics:
  - N_phi(s): number of pairwise ratios within 3% of phi among first N eigenvalues
  - N_phi^best: max over all s of N_phi(s) (for Jensen)
  - N_phi_consecutive: number of consecutive ratios near phi

The test determines: is N_phi = 184/1225 at Jensen s=1.14 anomalous compared
to a generic left-invariant metric on SU(3)?
"""

import numpy as np
from numpy.linalg import eigh, cholesky, inv, eigvalsh
import sys
import os
import time

# Add tier0-computation to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford, build_chirality,
    orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    dirac_operator_on_irrep, get_irrep, validate_irrep,
    analyze_spectrum, analyze_nonconsecutive_ratios
)


# =============================================================================
# MODULE 1: GENERALIZED LEFT-INVARIANT METRICS ON SU(3)
# =============================================================================

# Subspace indices (same as tier1_dirac_spectrum.py)
U1_IDX = [7]
SU2_IDX = [0, 1, 2]
C2_IDX = [3, 4, 5, 6]

def diagonal_metric(B_ab, alpha, beta, gamma):
    """
    Construct a diagonal left-invariant metric on su(3) with three
    independent scale factors on the three summands:

      g = alpha * g_0|_{u(1)} + beta * g_0|_{su(2)} + gamma * g_0|_{C^2}

    Jensen metric: alpha = e^{2s}, beta = e^{-2s}, gamma = e^{s}.

    Args:
        B_ab: (8,8) Killing form
        alpha: scale on u(1) (1 direction)
        beta: scale on su(2) (3 directions)
        gamma: scale on C^2 (4 directions)

    Returns:
        g: (8,8) positive definite metric
    """
    g0 = np.abs(B_ab)
    g = np.zeros((8, 8), dtype=np.float64)

    for a in U1_IDX:
        for b in U1_IDX:
            g[a, b] = g0[a, b] * alpha

    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a, b] = g0[a, b] * beta

    for a in C2_IDX:
        for b in C2_IDX:
            g[a, b] = g0[a, b] * gamma

    return g


def random_diagonal_metric_unconstrained(B_ab, rng, scale_range=(0.1, 10.0)):
    """
    Generate random diagonal metric with independent scale factors
    sampled log-uniformly from scale_range.

    Args:
        B_ab: Killing form
        rng: numpy random generator
        scale_range: (min, max) for each scale factor

    Returns:
        g: (8,8) metric
        params: (alpha, beta, gamma)
    """
    log_min, log_max = np.log(scale_range[0]), np.log(scale_range[1])
    alpha = np.exp(rng.uniform(log_min, log_max))
    beta = np.exp(rng.uniform(log_min, log_max))
    gamma = np.exp(rng.uniform(log_min, log_max))

    g = diagonal_metric(B_ab, alpha, beta, gamma)
    return g, (alpha, beta, gamma)


def random_diagonal_metric_volume_preserving(B_ab, rng, scale_range=(0.1, 10.0)):
    """
    Generate random diagonal metric with volume-preserving constraint:
      alpha * beta^3 * gamma^4 = 1

    Sample alpha and beta freely, solve for gamma.

    Args:
        B_ab: Killing form
        rng: numpy random generator
        scale_range: (min, max) for free parameters

    Returns:
        g: (8,8) metric, or None if gamma out of range
        params: (alpha, beta, gamma)
    """
    log_min, log_max = np.log(scale_range[0]), np.log(scale_range[1])
    alpha = np.exp(rng.uniform(log_min, log_max))
    beta = np.exp(rng.uniform(log_min, log_max))

    # Volume constraint: alpha * beta^3 * gamma^4 = 1
    # => gamma = (1 / (alpha * beta^3))^{1/4}
    gamma = (1.0 / (alpha * beta**3))**(1.0 / 4.0)

    if gamma < scale_range[0] or gamma > scale_range[1]:
        return None, None

    g = diagonal_metric(B_ab, alpha, beta, gamma)
    return g, (alpha, beta, gamma)


def random_general_metric(B_ab, rng, epsilon=0.3):
    """
    Generate random general left-invariant metric by perturbing the
    bi-invariant metric: g = g_0 + epsilon * h, where h is random
    symmetric positive semi-definite.

    This breaks the u(1)+su(2)+C^2 block diagonal structure and
    tests whether phi survives off the diagonal family.

    Args:
        B_ab: Killing form
        epsilon: perturbation scale relative to g_0 norm
        rng: numpy random generator

    Returns:
        g: (8,8) positive definite metric
    """
    g0 = np.abs(B_ab)
    g0_norm = np.max(np.abs(g0))

    # Random symmetric matrix
    A = rng.standard_normal((8, 8))
    h = (A + A.T) / 2.0

    # Scale so perturbation is epsilon * g0_norm
    h = h / np.max(np.abs(h)) * epsilon * g0_norm

    g = g0 + h

    # Ensure positive definiteness
    evals = eigvalsh(g)
    if np.min(evals) <= 0:
        # Shift to make positive definite
        g += (abs(np.min(evals)) + 0.01 * g0_norm) * np.eye(8)

    return g


# =============================================================================
# MODULE 2: SPECTRUM COMPUTATION FOR ARBITRARY METRIC
# =============================================================================

def compute_spectrum_for_metric(g, f_abc, gens, gammas, max_pq_sum=3):
    """
    Compute Dirac spectrum for an arbitrary left-invariant metric g on SU(3).

    Args:
        g: (8,8) positive definite metric
        f_abc: structure constants
        gens: su(3) generators
        gammas: Clifford generators
        max_pq_sum: maximum p+q for irreps

    Returns:
        abs_evals: sorted positive eigenvalue magnitudes (deduplicated)
        n_evals: number of distinct eigenvalues
    """
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    all_eigenvalues = []

    # Trivial irrep
    evals_trivial = np.linalg.eigvals(Omega)
    for ev in evals_trivial:
        all_eigenvalues.append(abs(ev))

    # Non-trivial irreps
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue
            try:
                rho, dim_rho = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_pi = np.linalg.eigvals(D_pi)
                for ev in evals_pi:
                    all_eigenvalues.append(abs(ev))
            except NotImplementedError:
                continue

    # Deduplicate and sort
    all_abs = np.array(all_eigenvalues)
    all_abs = all_abs[all_abs > 1e-10]
    abs_evals = np.sort(np.unique(np.round(all_abs, 10)))

    return abs_evals


def count_phi_pairs(abs_evals, n_low=20, phi=1.53158, tol=0.03):
    """
    Count pairwise ratios within tol of phi among first n_low eigenvalues.

    Args:
        abs_evals: sorted positive eigenvalues
        n_low: how many low-lying eigenvalues to use
        phi: target ratio
        tol: fractional tolerance

    Returns:
        n_phi: number of pairs within tol of phi
        n_total: total number of pairs checked
        best_err: closest approach to phi (fractional)
    """
    n = len(abs_evals) if n_low is None else min(n_low, len(abs_evals))
    n_phi = 0
    n_total = 0
    best_err = 999.0

    for i in range(n):
        for j in range(i + 1, n):
            r = abs_evals[j] / abs_evals[i]
            err = abs(r - phi) / phi
            if err < tol:
                n_phi += 1
            if err < best_err:
                best_err = err
            n_total += 1

    return n_phi, n_total, best_err


def count_phi_powers(abs_evals, n_low=30, phi=1.53158, tol=0.03, max_power=5):
    """
    Count pairwise ratios near phi^n for n = 1, 2, 3, ..., max_power.

    Args:
        abs_evals: sorted positive eigenvalues
        n_low: how many eigenvalues to use
        phi: base ratio
        tol: fractional tolerance
        max_power: highest power to check

    Returns:
        counts: dict mapping power n -> number of pairs near phi^n
        best_errs: dict mapping power n -> closest fractional error
    """
    n = len(abs_evals) if n_low is None else min(n_low, len(abs_evals))
    targets = {k: phi**k for k in range(1, max_power + 1)}
    counts = {k: 0 for k in range(1, max_power + 1)}
    best_errs = {k: 999.0 for k in range(1, max_power + 1)}

    for i in range(n):
        for j in range(i + 1, n):
            r = abs_evals[j] / abs_evals[i]
            for k, target in targets.items():
                err = abs(r - target) / target
                if err < tol:
                    counts[k] += 1
                if err < best_errs[k]:
                    best_errs[k] = err

    return counts, best_errs


def spectral_density_test(abs_evals, n_low=50, bin_width=0.05):
    """
    Compute the spectral density of pairwise ratios and test whether
    the phi-bin [1.505, 1.555] is anomalously populated.

    Returns:
        bin_centers: array of ratio bin centers
        bin_counts: array of counts in each bin
        phi_bin_idx: index of the bin containing phi
        phi_z_score: z-score of phi bin relative to neighbors
    """
    n = len(abs_evals) if n_low is None else min(n_low, len(abs_evals))
    all_ratios = []
    for i in range(n):
        for j in range(i + 1, n):
            r = abs_evals[j] / abs_evals[i]
            if 1.0 < r < 3.0:
                all_ratios.append(r)

    if len(all_ratios) < 10:
        return None, None, None, None

    all_ratios = np.array(all_ratios)
    bins = np.arange(1.0, 3.0 + bin_width, bin_width)
    counts, edges = np.histogram(all_ratios, bins=bins)
    centers = 0.5 * (edges[:-1] + edges[1:])

    # Find phi bin
    phi = 1.53158
    phi_bin_idx = np.searchsorted(edges, phi) - 1
    if phi_bin_idx < 0 or phi_bin_idx >= len(counts):
        return centers, counts, None, None

    # z-score: compare phi bin to local mean (excluding phi bin itself)
    # Use bins within +/- 5 bins but not the phi bin
    local_range = 5
    lo = max(0, phi_bin_idx - local_range)
    hi = min(len(counts), phi_bin_idx + local_range + 1)
    local_counts = np.concatenate([counts[lo:phi_bin_idx], counts[phi_bin_idx+1:hi]])

    if len(local_counts) < 3:
        return centers, counts, phi_bin_idx, None

    mu = np.mean(local_counts)
    sigma = np.std(local_counts)
    if sigma < 1e-10:
        z = 0.0
    else:
        z = (counts[phi_bin_idx] - mu) / sigma

    return centers, counts, phi_bin_idx, z


# =============================================================================
# MODULE 3: MONTE CARLO ENGINE
# =============================================================================

def run_mc_diagonal_unconstrained(n_samples, f_abc, gens, gammas, B_ab,
                                   max_pq_sum=3, n_low=20, seed=42):
    """
    Monte Carlo: random unconstrained diagonal metrics.

    Returns:
        phi_counts: array of phi-pair counts per sample
        total_pairs: total pairs per sample
        params_list: list of (alpha, beta, gamma)
    """
    rng = np.random.default_rng(seed)
    phi_counts = []
    total_pairs_list = []
    best_errs = []
    params_list = []

    for trial in range(n_samples):
        g, params = random_diagonal_metric_unconstrained(B_ab, rng)
        try:
            abs_evals = compute_spectrum_for_metric(g, f_abc, gens, gammas, max_pq_sum)
            n_phi, n_total, best_err = count_phi_pairs(abs_evals, n_low=n_low)
            phi_counts.append(n_phi)
            total_pairs_list.append(n_total)
            best_errs.append(best_err)
            params_list.append(params)
        except Exception as e:
            # Skip degenerate metrics
            continue

    return np.array(phi_counts), np.array(total_pairs_list), np.array(best_errs), params_list


def run_mc_volume_preserving(n_samples, f_abc, gens, gammas, B_ab,
                              max_pq_sum=3, n_low=20, seed=42):
    """
    Monte Carlo: random volume-preserving diagonal metrics.
    """
    rng = np.random.default_rng(seed)
    phi_counts = []
    total_pairs_list = []
    best_errs = []
    params_list = []

    attempts = 0
    while len(phi_counts) < n_samples and attempts < n_samples * 5:
        attempts += 1
        g, params = random_diagonal_metric_volume_preserving(B_ab, rng)
        if g is None:
            continue
        try:
            abs_evals = compute_spectrum_for_metric(g, f_abc, gens, gammas, max_pq_sum)
            n_phi, n_total, best_err = count_phi_pairs(abs_evals, n_low=n_low)
            phi_counts.append(n_phi)
            total_pairs_list.append(n_total)
            best_errs.append(best_err)
            params_list.append(params)
        except Exception:
            continue

    return np.array(phi_counts), np.array(total_pairs_list), np.array(best_errs), params_list


def run_mc_general(n_samples, f_abc, gens, gammas, B_ab,
                    max_pq_sum=3, n_low=20, seed=42, epsilon=0.3):
    """
    Monte Carlo: random general left-invariant metrics (perturbative).
    """
    rng = np.random.default_rng(seed)
    phi_counts = []
    total_pairs_list = []
    best_errs = []

    for trial in range(n_samples):
        g = random_general_metric(B_ab, rng, epsilon=epsilon)
        try:
            abs_evals = compute_spectrum_for_metric(g, f_abc, gens, gammas, max_pq_sum)
            n_phi, n_total, best_err = count_phi_pairs(abs_evals, n_low=n_low)
            phi_counts.append(n_phi)
            total_pairs_list.append(n_total)
            best_errs.append(best_err)
        except Exception:
            continue

    return np.array(phi_counts), np.array(total_pairs_list), np.array(best_errs)


def run_mc_phi_powers(n_samples, f_abc, gens, gammas, B_ab,
                       metric_type='volume_preserving',
                       max_pq_sum=3, n_low=30, seed=42, max_power=5):
    """
    Monte Carlo for phi^n powers: for each random metric, count pairs
    near phi^1, phi^2, ..., phi^max_power.

    Args:
        metric_type: 'diagonal', 'volume_preserving', or 'general'

    Returns:
        power_counts: dict mapping power n -> array of counts per sample
        power_best_errs: dict mapping power n -> array of best errors per sample
    """
    rng = np.random.default_rng(seed)
    power_counts = {k: [] for k in range(1, max_power + 1)}
    power_best_errs = {k: [] for k in range(1, max_power + 1)}

    attempts = 0
    collected = 0
    while collected < n_samples and attempts < n_samples * 5:
        attempts += 1

        if metric_type == 'diagonal':
            g, _ = random_diagonal_metric_unconstrained(B_ab, rng)
        elif metric_type == 'volume_preserving':
            g, params = random_diagonal_metric_volume_preserving(B_ab, rng)
            if g is None:
                continue
        elif metric_type == 'general':
            g = random_general_metric(B_ab, rng, epsilon=0.3)
        else:
            raise ValueError(f"Unknown metric type: {metric_type}")

        try:
            abs_evals = compute_spectrum_for_metric(g, f_abc, gens, gammas, max_pq_sum)
            counts, errs = count_phi_powers(abs_evals, n_low=n_low, max_power=max_power)
            for k in range(1, max_power + 1):
                power_counts[k].append(counts[k])
                power_best_errs[k].append(errs[k])
            collected += 1
        except Exception:
            continue

    for k in range(1, max_power + 1):
        power_counts[k] = np.array(power_counts[k])
        power_best_errs[k] = np.array(power_best_errs[k])

    return power_counts, power_best_errs


# =============================================================================
# MODULE 4: ANALYSIS AND REPORTING
# =============================================================================

def compute_statistics(observed, null_distribution, label=""):
    """
    Compute z-score and p-value for observed count vs null distribution.

    Args:
        observed: observed value
        null_distribution: array of null samples
        label: string label for printing

    Returns:
        z: z-score
        p: p-value (fraction of null >= observed)
    """
    mu = np.mean(null_distribution)
    sigma = np.std(null_distribution)
    if sigma < 1e-10:
        z = 0.0 if abs(observed - mu) < 1e-10 else np.inf
    else:
        z = (observed - mu) / sigma

    p = np.mean(null_distribution >= observed)

    if label:
        print(f"  {label}:")
        print(f"    Observed: {observed}")
        print(f"    Null: {mu:.1f} +/- {sigma:.1f}")
        print(f"    z-score: {z:.2f}")
        print(f"    p-value: {p:.4f} ({p*100:.2f}%)")
        if p > 0:
            print(f"    sigma equivalent: {-np.log10(p)/np.log10(0.5):.1f} half-lives "
                  f"({abs(z):.1f} sigma)")
        else:
            print(f"    sigma equivalent: > {len(null_distribution)} samples needed")

    return z, p


# =============================================================================
# MODULE 5: MAIN EXECUTION
# =============================================================================

def main():
    print("=" * 80)
    print("MONTE CARLO SIGNIFICANCE TEST: PHI IN SU(3) DIRAC SPECTRUM")
    print("Author: Gen-Physicist, Session 14")
    print("=" * 80)

    # --- Setup ---
    print("\n[1] Setting up su(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # CRITICAL: Use ALL eigenvalues (n_low=None -> all 120 distinct eigenvalues)
    # Session 14 correction: n_low=20 or 50 misses phi^2 and phi^3 pairs
    # because the truncated spectrum doesn't span enough dynamic range.
    N_LOW = None  # Use all distinct eigenvalues

    # --- Jensen baseline across s values ---
    print(f"\n[2] Computing Jensen baseline (n_low={N_LOW})...")
    from tier1_dirac_spectrum import jensen_metric

    jensen_results = {}
    for s_val in [0.0, 0.15, 0.43, 0.5, 1.0, 1.14, 1.5, 2.0]:
        g_s = jensen_metric(B_ab, s_val)
        ev_s = compute_spectrum_for_metric(g_s, f_abc, gens, gammas, max_pq_sum=3)
        n_phi_s, n_tot_s, best_s = count_phi_pairs(ev_s, n_low=N_LOW)
        jensen_results[s_val] = (n_phi_s, n_tot_s, best_s, ev_s)
        print(f"  Jensen s={s_val:.2f}: {n_phi_s}/{n_tot_s} pairs near phi, "
              f"best err = {best_s*100:.4f}%, n_evals={len(ev_s)}")

    # Find the best s
    best_s_val = max(jensen_results, key=lambda s: jensen_results[s][0])
    n_phi_best = jensen_results[best_s_val][0]
    evals_best = jensen_results[best_s_val][3]
    print(f"\n  Best Jensen s: {best_s_val:.2f} with {n_phi_best} phi-pairs")

    # Also get s=0 baseline
    n_phi_s0 = jensen_results[0.0][0]
    evals_s0 = jensen_results[0.0][3]
    print(f"  Bi-invariant (s=0): {n_phi_s0} phi-pairs")

    # --- Monte Carlo: Unconstrained diagonal ---
    N_MC = 100  # Keep moderate: ~0.4 sec/sample * 100 = 40 sec
    print(f"\n[3] Monte Carlo: UNCONSTRAINED diagonal metrics ({N_MC} samples, n_low={N_LOW})...")
    t0 = time.time()
    phi_counts_unc, totals_unc, best_errs_unc, params_unc = run_mc_diagonal_unconstrained(
        N_MC, f_abc, gens, gammas, B_ab, max_pq_sum=3, n_low=N_LOW, seed=42
    )
    t1 = time.time()
    print(f"  Completed in {t1-t0:.1f} seconds ({len(phi_counts_unc)/(t1-t0):.1f} samples/sec)")

    z_unc_best, p_unc_best = compute_statistics(
        n_phi_best, phi_counts_unc,
        label=f"Jensen s={best_s_val} vs unconstrained diagonal null"
    )

    z_unc_s0, p_unc_s0 = compute_statistics(
        n_phi_s0, phi_counts_unc,
        label=f"Jensen s=0 (bi-invariant) vs unconstrained diagonal null"
    )

    print(f"  Null distribution: min={np.min(phi_counts_unc)}, "
          f"max={np.max(phi_counts_unc)}, "
          f"median={np.median(phi_counts_unc):.0f}, "
          f"mean={np.mean(phi_counts_unc):.1f}")
    print(f"  Best-error distribution: mean={np.mean(best_errs_unc)*100:.3f}%, "
          f"min={np.min(best_errs_unc)*100:.4f}%")

    # --- Monte Carlo: Volume-preserving ---
    print(f"\n[4] Monte Carlo: VOLUME-PRESERVING diagonal metrics ({N_MC} samples)...")
    t0 = time.time()
    phi_counts_vp, totals_vp, best_errs_vp, params_vp = run_mc_volume_preserving(
        N_MC, f_abc, gens, gammas, B_ab, max_pq_sum=3, n_low=N_LOW, seed=123
    )
    t1 = time.time()
    print(f"  Completed in {t1-t0:.1f} seconds "
          f"({len(phi_counts_vp)}/{N_MC} accepted)")

    z_vp, p_vp = compute_statistics(
        n_phi_best, phi_counts_vp,
        label=f"Jensen s={best_s_val} vs volume-preserving diagonal null"
    )

    print(f"  Null distribution: min={np.min(phi_counts_vp)}, "
          f"max={np.max(phi_counts_vp)}, "
          f"median={np.median(phi_counts_vp):.0f}")

    # --- Monte Carlo: General perturbative ---
    print(f"\n[5] Monte Carlo: GENERAL metrics (epsilon=0.3, {N_MC} samples)...")
    t0 = time.time()
    phi_counts_gen, totals_gen, best_errs_gen = run_mc_general(
        N_MC, f_abc, gens, gammas, B_ab, max_pq_sum=3, n_low=N_LOW, seed=456, epsilon=0.3
    )
    t1 = time.time()
    print(f"  Completed in {t1-t0:.1f} seconds")

    z_gen, p_gen = compute_statistics(
        n_phi_best, phi_counts_gen,
        label=f"Jensen s={best_s_val} vs general perturbative null"
    )

    # --- Phi Powers (on unconstrained diagonal) ---
    N_MC_POWERS = 50  # Reduced since this is slower (n_low=30, max_power=5)
    print(f"\n[6] Phi-powers analysis (phi^1 through phi^5, {N_MC_POWERS} samples)...")
    phi = 1.53158
    print(f"  Targets: phi={phi:.5f}, phi^2={phi**2:.5f}, phi^3={phi**3:.5f}, "
          f"phi^4={phi**4:.5f}, phi^5={phi**5:.5f}")

    # Compute phi powers for Jensen baseline at best s and s=0
    for s_label, ev_set in [("s=0", evals_s0), (f"s={best_s_val}", evals_best)]:
        powers, power_errs = count_phi_powers(ev_set, n_low=N_LOW, max_power=5)
        print(f"\n  Jensen {s_label} phi-power counts:")
        for k in range(1, 6):
            print(f"    phi^{k} = {phi**k:.4f}: {powers[k]} pairs, "
                  f"best err = {power_errs[k]*100:.3f}%")

    # MC null for phi powers
    t0 = time.time()
    mc_power_counts, mc_power_errs = run_mc_phi_powers(
        N_MC_POWERS, f_abc, gens, gammas, B_ab,
        metric_type='diagonal', max_pq_sum=3, n_low=N_LOW, seed=789, max_power=5
    )
    t1 = time.time()
    print(f"\n  MC phi-powers completed in {t1-t0:.1f} seconds")

    # Compare Jensen s=0 against null for each power
    powers_s0, _ = count_phi_powers(evals_s0, n_low=N_LOW, max_power=5)
    powers_best, _ = count_phi_powers(evals_best, n_low=N_LOW, max_power=5)

    print(f"\n  Jensen s=0 vs null:")
    for k in range(1, 6):
        if len(mc_power_counts[k]) > 0:
            z_k, p_k = compute_statistics(
                powers_s0[k], mc_power_counts[k],
                label=f"  phi^{k} = {phi**k:.4f} (s=0)"
            )

    print(f"\n  Jensen s={best_s_val} vs null:")
    for k in range(1, 6):
        if len(mc_power_counts[k]) > 0:
            z_k, p_k = compute_statistics(
                powers_best[k], mc_power_counts[k],
                label=f"  phi^{k} = {phi**k:.4f} (s={best_s_val})"
            )

    # --- Spectral density test ---
    print(f"\n[7] Spectral density test...")
    for s_label, ev_set in [("s=0", evals_s0), (f"s={best_s_val}", evals_best)]:
        centers, counts, phi_idx, phi_z = spectral_density_test(ev_set, n_low=N_LOW)
        if phi_z is not None:
            print(f"  Jensen {s_label}:")
            print(f"    Phi bin (centered at {centers[phi_idx]:.3f}): count = {counts[phi_idx]}")
            lo = max(0, phi_idx - 5)
            hi = min(len(counts), phi_idx + 6)
            print(f"    Local bins: {counts[lo:hi].tolist()}")
            print(f"    Phi bin z-score (local): {phi_z:.2f}")

    # --- Summary ---
    print(f"\n{'='*80}")
    print("SUMMARY: MONTE CARLO SIGNIFICANCE")
    print("=" * 80)
    print()
    print(f"  Observed: Jensen s={best_s_val}: {n_phi_best}/{jensen_results[best_s_val][1]} "
          f"phi-pairs ({n_phi_best/jensen_results[best_s_val][1]*100:.1f}%)")
    print(f"  Observed: Jensen s=0:    {n_phi_s0}/{jensen_results[0.0][1]} "
          f"phi-pairs ({n_phi_s0/jensen_results[0.0][1]*100:.1f}%)")
    print()
    print(f"  Null Model (n_low={N_LOW})                | z-score | p-value | Verdict")
    print("  " + "-" * 72)
    print(f"  Unconstrained diagonal (best s)          | {z_unc_best:7.2f} | {p_unc_best:7.4f} | "
          f"{'SIGNIFICANT' if p_unc_best < 0.003 else 'NOT significant' if p_unc_best > 0.05 else 'Suggestive'}")
    print(f"  Unconstrained diagonal (s=0)             | {z_unc_s0:7.2f} | {p_unc_s0:7.4f} | "
          f"{'SIGNIFICANT' if p_unc_s0 < 0.003 else 'NOT significant' if p_unc_s0 > 0.05 else 'Suggestive'}")
    print(f"  Volume-preserving diagonal (best s)      | {z_vp:7.2f} | {p_vp:7.4f} | "
          f"{'SIGNIFICANT' if p_vp < 0.003 else 'NOT significant' if p_vp > 0.05 else 'Suggestive'}")
    print(f"  General perturbative (best s)            | {z_gen:7.2f} | {p_gen:7.4f} | "
          f"{'SIGNIFICANT' if p_gen < 0.003 else 'NOT significant' if p_gen > 0.05 else 'Suggestive'}")
    print()

    print("  Phi Powers (Jensen s=0 vs diagonal null):")
    print("  " + "-" * 60)
    for k in range(1, 6):
        n_obs = powers_s0[k]
        if len(mc_power_counts[k]) > 0:
            mu_null = np.mean(mc_power_counts[k])
            sig_null = np.std(mc_power_counts[k])
        else:
            mu_null = 0
            sig_null = 0
        print(f"  phi^{k} = {phi**k:.4f}: observed {n_obs} pairs "
              f"(null: {mu_null:.1f}+/-{sig_null:.1f})")

    print()
    print("  INTERPRETATION:")
    print("  The key question is NOT whether Jensen s=1.14 is special")
    print("  (it's parameter-tuned), but whether the ALGEBRAIC phi near-miss")
    print("  at s=0 (sqrt(7/3) ~ phi, representation-theoretic) is anomalous")
    print("  compared to random left-invariant metrics on SU(3).")
    print()
    print("  KEY QUESTION FOR TASK #4:")
    print("  Does the extended spectrum (p+q <= 5) change these statistics?")
    print("  Specifically: does phi^2 = 2.346 appear in ANY pairwise ratios?")
    print("  The Paasch geometric series REQUIRES phi^n for n >= 2.")
    print()
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
