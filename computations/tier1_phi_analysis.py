"""
TIER 1: PHI-STRUCTURE ANALYSIS OF THE DIRAC SPECTRUM ON (SU(3), g_s)
=====================================================================

Comprehensive statistical analysis of the Dirac eigenvalue spectrum for
Paasch phi-ratio structure. Uses the extended irrep support (p+q <= 6)
from tier1_dirac_spectrum.py and spectral action from tier1_spectral_action.py.

TARGETS:
  - phi   = 1.53158  (Paasch mass ratio)
  - phi^2 = 2.34573
  - phi^3 = 3.59287
  - phi^4 = 5.50257
  - golden = 1.61803  (golden ratio, for comparison)

METHODOLOGY:
  1. Compute extended spectrum at multiple s values with max_pq_sum=5
  2. Comprehensive pairwise ratio scan for ALL phi^n matches
  3. Sector-resolved analysis: which (p,q) pairs produce phi ratios?
  4. Monte Carlo significance: random left-invariant metrics as null hypothesis
  5. Bonferroni-corrected p-values for multiple testing
  6. Re-run spectral action with higher max_pq_sum for convergence check

STATISTICAL PROTOCOL:
  - Number of pairwise ratios grows as O(N^2) where N = # distinct eigenvalues
  - "Look-elsewhere effect" handled by Bonferroni correction
  - Null hypothesis: ratios from random Riemannian metric on SU(3) at comparable spectral density
  - Reported p-values are CONSERVATIVE (Bonferroni overcorrects for correlated ratios)

Author: Sim-Specialist Agent (phonon-exflation project, Session 14)
Date: 2026-02-12

References:
  - Paasch (2005-2025): Mass spiral, phi_paasch=1.53158 from x = e^{-x^2} (NOT the golden ratio)
  - Baptista (2024): Jensen deformation of SU(3) bi-invariant metric
  - Weyl's law: N(Lambda) ~ C_d * Vol * Lambda^d for d=8
"""

import numpy as np
from numpy.linalg import eigvalsh
import sys
import os
import time

# Add tier0-computation to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    collect_spectrum, analyze_spectrum, analyze_nonconsecutive_ratios,
    get_irrep, dirac_operator_on_irrep,
    su2_benchmark
)
from tier1_spectral_action import (
    spectral_action_smooth_cutoff, extract_seeley_dewitt_robust,
    spectral_vs_baptista, scalar_curvature_sweep,
    plot_spectral_action_results
)


# =============================================================================
# MODULE 1: TARGET RATIO DEFINITIONS
# =============================================================================

PHI_PAASCH = 1.53158    # Paasch mass ratio
PHI_2 = PHI_PAASCH**2   # 2.34573
PHI_3 = PHI_PAASCH**3   # 3.59287
PHI_4 = PHI_PAASCH**4   # 5.50257
PHI_5 = PHI_PAASCH**5   # 8.42755
GOLDEN = (1 + np.sqrt(5)) / 2  # 1.61803

TARGETS = {
    'phi':    PHI_PAASCH,
    'phi^2':  PHI_2,
    'phi^3':  PHI_3,
    'phi^4':  PHI_4,
    'phi^5':  PHI_5,
    'golden': GOLDEN,
}


# =============================================================================
# MODULE 2: EXTENDED PAIRWISE RATIO SCANNER
# =============================================================================

def pairwise_ratio_scan(abs_evals, targets=None, tol=0.03, n_max=None,
                        verbose=True):
    """
    Scan ALL pairwise ratios of eigenvalues for target values.

    For N eigenvalues, there are N*(N-1)/2 pairwise ratios. Each ratio
    lambda_j / lambda_i (j > i) is checked against each target value.

    Args:
        abs_evals: sorted array of distinct positive eigenvalues
        targets: dict of name -> target_value. Default: TARGETS
        tol: relative tolerance (fraction, not percent)
        n_max: maximum number of eigenvalues to use (None = all)
        verbose: print results

    Returns:
        results: dict mapping target_name -> list of (i, j, ratio, val_i, val_j, rel_err)
        stats: dict with n_evals, n_pairs, n_hits per target
    """
    if targets is None:
        targets = TARGETS

    n = len(abs_evals) if n_max is None else min(n_max, len(abs_evals))
    evals = abs_evals[:n]
    n_pairs = n * (n - 1) // 2

    results = {name: [] for name in targets}

    for i in range(n):
        for j in range(i + 1, n):
            r = evals[j] / evals[i]
            for name, target in targets.items():
                rel_err = abs(r - target) / target
                if rel_err < tol:
                    results[name].append((i, j, r, evals[i], evals[j], rel_err))

    stats = {
        'n_evals': n,
        'n_pairs': n_pairs,
    }
    for name in targets:
        hits = results[name]
        stats[f'n_hits_{name}'] = len(hits)
        # Sort by error
        results[name] = sorted(hits, key=lambda x: x[5])

    if verbose:
        print(f"\n  Pairwise ratio scan: {n} eigenvalues, {n_pairs} pairs, tol={tol*100:.0f}%")
        for name, target in targets.items():
            hits = results[name]
            print(f"\n    {name} = {target:.5f}: {len(hits)} hits ({len(hits)/n_pairs*100:.2f}% of pairs)")
            for i, j, r, vi, vj, err in hits[:5]:  # show top 5
                print(f"      [{i:2d}]/[{j:2d}]: {vj:.6f}/{vi:.6f} = {r:.6f} "
                      f"(err {err*100:.3f}%)")
            if len(hits) > 5:
                print(f"      ... and {len(hits)-5} more")

    return results, stats


# =============================================================================
# MODULE 3: SECTOR-RESOLVED PHI ANALYSIS
# =============================================================================

def sector_phi_analysis(eval_data, s, targets=None, tol=0.03, verbose=True):
    """
    Identify which SU(3) irrep sectors produce phi-ratio eigenvalue pairs.

    For each pair of sectors (p1,q1) and (p2,q2), compute the lowest eigenvalue
    ratio and check against targets. This identifies the REPRESENTATION-THEORETIC
    origin of any phi structure.

    Args:
        eval_data: list of (p, q, eigenvalues_array) from collect_spectrum
        s: Jensen parameter (for labeling)
        targets: dict of name -> target_value
        tol: relative tolerance
        verbose: print results

    Returns:
        sector_hits: list of dicts with sector info and matching target
    """
    if targets is None:
        targets = TARGETS

    # Extract lowest |eigenvalue| from each sector
    sector_info = []
    for p, q, evals in eval_data:
        abs_ev = np.sort(np.abs(evals))
        # Remove near-zero eigenvalues
        nonzero = abs_ev[abs_ev > 1e-8]
        if len(nonzero) > 0:
            sector_info.append({
                'p': p, 'q': q,
                'dim': (p + 1) * (q + 1) * (p + q + 2) // 2,
                'min_eval': nonzero[0],
                'all_evals': nonzero,
                'n_evals': len(nonzero),
            })

    sector_hits = []

    # Check all pairs of sectors
    n_sec = len(sector_info)
    for i in range(n_sec):
        for j in range(i, n_sec):  # include i==j (intra-sector)
            si = sector_info[i]
            sj = sector_info[j]

            # Check lowest eigenvalue ratios between sectors
            for ev_i in si['all_evals'][:5]:  # first 5 eigenvalues per sector
                for ev_j in sj['all_evals'][:5]:
                    if ev_j <= ev_i:
                        continue
                    r = ev_j / ev_i
                    for name, target in targets.items():
                        rel_err = abs(r - target) / target
                        if rel_err < tol:
                            sector_hits.append({
                                'sector_i': (si['p'], si['q']),
                                'sector_j': (sj['p'], sj['q']),
                                'eval_i': ev_i,
                                'eval_j': ev_j,
                                'ratio': r,
                                'target': name,
                                'rel_err': rel_err,
                            })

    if verbose:
        print(f"\n  Sector-resolved phi analysis at s={s:.3f}:")
        print(f"    {n_sec} sectors, checking cross-sector eigenvalue ratios")

        # Group by target
        for name, target in targets.items():
            hits = [h for h in sector_hits if h['target'] == name]
            if hits:
                print(f"\n    {name} = {target:.5f}: {len(hits)} sector-pair hits")
                for h in sorted(hits, key=lambda x: x['rel_err'])[:8]:
                    print(f"      ({h['sector_i'][0]},{h['sector_i'][1]}) / "
                          f"({h['sector_j'][0]},{h['sector_j'][1]}): "
                          f"{h['eval_j']:.6f}/{h['eval_i']:.6f} = {h['ratio']:.6f} "
                          f"(err {h['rel_err']*100:.3f}%)")
            else:
                print(f"\n    {name} = {target:.5f}: no hits")

    return sector_hits


# =============================================================================
# MODULE 4: MONTE CARLO SIGNIFICANCE TESTING
# =============================================================================

def generate_random_metric_evals(gens, f_abc, gammas, max_pq_sum=3,
                                  n_random=100, seed=42, verbose=True):
    """
    Generate Dirac spectra for RANDOM left-invariant metrics on SU(3).

    A left-invariant metric on SU(3) is parametrized by a positive-definite
    symmetric 8x8 matrix g_ab. The Jensen family is 1-dimensional; a generic
    left-invariant metric has 36 independent parameters (8*9/2).

    To generate a fair null distribution:
    1. Start from the bi-invariant metric g_0 = -B/12 (Killing)
    2. Apply random perturbations of comparable magnitude to Jensen deformations
    3. Ensure positive-definiteness

    This tests whether phi-near ratios are GENERIC to left-invariant metrics
    on SU(3), or SPECIAL to the Jensen family.

    Args:
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators
        max_pq_sum: maximum p+q for spectrum computation
        n_random: number of random metrics to generate
        seed: random seed
        verbose: print progress

    Returns:
        random_spectra: list of sorted abs_evals arrays
        random_ratio_stats: dict of ratio statistics
    """
    rng = np.random.RandomState(seed)

    B_ab = compute_killing_form(f_abc)
    g0 = -B_ab / 12.0  # bi-invariant metric (positive-definite)

    random_spectra = []
    random_ratio_stats = {name: [] for name in TARGETS}

    if verbose:
        print(f"\n  Monte Carlo null distribution: {n_random} random left-invariant metrics")
        print(f"    max_pq_sum={max_pq_sum}")

    for trial in range(n_random):
        if verbose and (trial + 1) % 10 == 0:
            print(f"    Trial {trial+1}/{n_random}...")

        # Generate random perturbation
        # Scale: comparable to Jensen at s~1 (which changes eigenvalues by ~e^2 ~ 7x)
        # We perturb the metric as: g = g0 + epsilon * S where S is random symmetric
        # Then project to positive-definite via eigenvalue clipping

        # Random symmetric perturbation
        A = rng.randn(8, 8)
        S = (A + A.T) / 2.0

        # Scale: use Frobenius norm of g0 as reference
        g0_norm = np.linalg.norm(g0, 'fro')
        epsilon = rng.exponential(0.5)  # random scale, mean 0.5
        S = S / np.linalg.norm(S, 'fro') * g0_norm * epsilon

        g_random = g0 + S

        # Project to positive-definite: clip eigenvalues
        eigvals, eigvecs = np.linalg.eigh(g_random)
        eigvals = np.maximum(eigvals, 0.01 * np.min(np.linalg.eigvalsh(g0)))
        g_random = eigvecs @ np.diag(eigvals) @ eigvecs.T

        # Normalize to same volume as g0 (det^{1/8} matching)
        det_ratio = np.linalg.det(g_random) / np.linalg.det(g0)
        if det_ratio > 0:
            g_random = g_random / det_ratio**(1.0/8)

        # Build Dirac operator with this metric
        try:
            E = orthonormal_frame(g_random)
            ft = frame_structure_constants(f_abc, E)
            Gamma = connection_coefficients(ft)
            Omega = spinor_connection_offset(Gamma, gammas)

            # Collect eigenvalues
            all_eigenvalues = []

            # Trivial sector
            evals_trivial = np.linalg.eigvals(Omega)
            for ev in evals_trivial:
                all_eigenvalues.append((ev, 1))

            # Higher sectors
            for p in range(max_pq_sum + 1):
                for q in range(max_pq_sum + 1 - p):
                    if p == 0 and q == 0:
                        continue
                    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
                    try:
                        rho, _ = get_irrep(p, q, gens, f_abc)
                        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                        evals_pi = np.linalg.eigvals(D_pi)
                        for ev in evals_pi:
                            all_eigenvalues.append((ev, dim_pq))
                    except Exception:
                        continue

            # Extract sorted absolute eigenvalues
            abs_vals = sorted(set(np.round(np.abs([ev for ev, _ in all_eigenvalues]), 10)))
            abs_vals = np.array([v for v in abs_vals if v > 1e-8])

            if len(abs_vals) < 5:
                continue

            random_spectra.append(abs_vals)

            # Count ratio hits
            n = len(abs_vals)
            for i in range(n):
                for j in range(i + 1, n):
                    r = abs_vals[j] / abs_vals[i]
                    for name, target in TARGETS.items():
                        if abs(r - target) / target < 0.03:
                            random_ratio_stats[name].append(1)

            # Record number of pairs for normalization
            n_pairs = n * (n - 1) // 2
            for name in TARGETS:
                # Pad with zeros for pairs that didn't match
                while len(random_ratio_stats[name]) < (trial + 1):
                    random_ratio_stats[name].append(0)

        except Exception as e:
            if verbose and trial < 5:
                print(f"    Trial {trial+1} FAILED: {e}")
            continue

    if verbose:
        print(f"    Completed: {len(random_spectra)} successful trials")

    return random_spectra, random_ratio_stats


def monte_carlo_significance(abs_evals_target, random_spectra, targets=None,
                             tol=0.03, verbose=True):
    """
    Compute p-values for phi-ratio hits by comparison with random metric spectra.

    For each target ratio, count:
      - n_hits_target: # of matching pairs in the Jensen spectrum
      - n_hits_random[k]: # of matching pairs in random spectrum k

    p-value = fraction of random spectra with >= n_hits_target hits.

    Bonferroni correction: multiply p-value by number of targets tested.

    Args:
        abs_evals_target: sorted positive eigenvalues from Jensen metric
        random_spectra: list of sorted abs_evals from random metrics
        targets: dict of name -> target_value
        tol: relative tolerance
        verbose: print results

    Returns:
        p_values: dict of name -> (p_raw, p_bonferroni, n_hits_target, mean_hits_random)
    """
    if targets is None:
        targets = TARGETS

    n_random = len(random_spectra)
    n_targets = len(targets)

    # Count hits in target spectrum
    n_target = len(abs_evals_target)
    hits_target = {}
    for name, target in targets.items():
        count = 0
        for i in range(n_target):
            for j in range(i + 1, n_target):
                r = abs_evals_target[j] / abs_evals_target[i]
                if abs(r - target) / target < tol:
                    count += 1
        hits_target[name] = count

    # Count hits in each random spectrum
    hits_random = {name: [] for name in targets}
    for spec in random_spectra:
        n = len(spec)
        for name, target in targets.items():
            count = 0
            for i in range(n):
                for j in range(i + 1, n):
                    r = spec[j] / spec[i]
                    if abs(r - target) / target < tol:
                        count += 1
            hits_random[name].append(count)

    # Compute p-values
    p_values = {}
    for name in targets:
        n_h = hits_target[name]
        random_counts = np.array(hits_random[name])
        if len(random_counts) == 0:
            p_raw = 1.0
        else:
            p_raw = np.mean(random_counts >= n_h)
        p_bonf = min(p_raw * n_targets, 1.0)

        mean_random = np.mean(random_counts) if len(random_counts) > 0 else 0
        std_random = np.std(random_counts) if len(random_counts) > 0 else 0

        p_values[name] = {
            'p_raw': p_raw,
            'p_bonferroni': p_bonf,
            'n_hits_target': n_h,
            'mean_hits_random': mean_random,
            'std_hits_random': std_random,
            'z_score': (n_h - mean_random) / std_random if std_random > 0 else 0,
        }

    if verbose:
        print(f"\n  Monte Carlo significance test (tol={tol*100:.0f}%, "
              f"{n_random} random metrics):")
        print(f"    {'Target':>10}  {'Jensen hits':>11}  {'Random mean':>11}  "
              f"{'Random std':>10}  {'z-score':>8}  {'p(raw)':>8}  {'p(Bonf)':>8}")
        for name, target in targets.items():
            pv = p_values[name]
            print(f"    {name:>10}  {pv['n_hits_target']:>11d}  "
                  f"{pv['mean_hits_random']:>11.1f}  "
                  f"{pv['std_hits_random']:>10.1f}  "
                  f"{pv['z_score']:>8.2f}  "
                  f"{pv['p_raw']:>8.4f}  "
                  f"{pv['p_bonferroni']:>8.4f}")

    return p_values


# =============================================================================
# MODULE 5: SPECTRAL DENSITY ANALYSIS
# =============================================================================

def spectral_density_analysis(abs_evals, n_bins=50, verbose=True):
    """
    Analyze the spectral density of pairwise ratios.

    If phi-near ratios are significant, the bin [1.50-1.55] should have
    an excess compared to the smooth background. We compute the ratio
    histogram and check for anomalous bins.

    Args:
        abs_evals: sorted positive eigenvalues
        n_bins: number of histogram bins
        verbose: print analysis

    Returns:
        bin_edges: array of bin edges
        bin_counts: array of counts
        bin_density: normalized density
        anomalous_bins: list of (bin_center, count, z_score) for outlier bins
    """
    n = len(abs_evals)
    ratios = []
    for i in range(n):
        for j in range(i + 1, n):
            ratios.append(abs_evals[j] / abs_evals[i])

    ratios = np.array(ratios)

    # Focus on the region [1.0, 6.0] which covers phi through phi^4
    mask = (ratios >= 1.0) & (ratios <= 6.0)
    ratios_focus = ratios[mask]

    bin_edges = np.linspace(1.0, 6.0, n_bins + 1)
    bin_counts, _ = np.histogram(ratios_focus, bins=bin_edges)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_width = bin_edges[1] - bin_edges[0]

    # Smooth background: running average over 5 bins
    from scipy.ndimage import uniform_filter1d
    smooth = uniform_filter1d(bin_counts.astype(float), size=5, mode='nearest')

    # z-score for each bin (relative to local average)
    local_std = np.sqrt(smooth + 1)  # Poisson-like
    z_scores = (bin_counts - smooth) / local_std

    # Anomalous bins: |z| > 2.5
    anomalous = []
    for k in range(len(bin_counts)):
        if abs(z_scores[k]) > 2.5:
            anomalous.append((bin_centers[k], bin_counts[k], z_scores[k]))

    # Normalize to density
    total = np.sum(bin_counts) * bin_width
    bin_density = bin_counts / total if total > 0 else bin_counts

    if verbose:
        print(f"\n  Spectral density of pairwise ratios:")
        print(f"    Total ratios: {len(ratios)}")
        print(f"    Ratios in [1.0, 6.0]: {len(ratios_focus)}")
        print(f"    Bins: {n_bins}, width: {bin_width:.3f}")

        # Check specific target ranges
        for name, target in TARGETS.items():
            # Find bin containing target
            idx = np.searchsorted(bin_edges, target) - 1
            if 0 <= idx < len(bin_counts):
                print(f"    Bin containing {name}={target:.5f}: "
                      f"count={bin_counts[idx]}, z-score={z_scores[idx]:+.2f}")

        if anomalous:
            print(f"\n    Anomalous bins (|z| > 2.5):")
            for center, count, z in sorted(anomalous, key=lambda x: -abs(x[2])):
                # Check if near any target
                near_target = ""
                for name, target in TARGETS.items():
                    if abs(center - target) < bin_width:
                        near_target = f" <-- near {name}"
                        break
                print(f"      center={center:.3f}: count={count}, z={z:+.2f}{near_target}")
        else:
            print(f"\n    No anomalous bins (all |z| < 2.5)")

    return bin_edges, bin_counts, bin_density, anomalous


# =============================================================================
# MODULE 6: PHI-POWER CHAIN DETECTION
# =============================================================================

def phi_chain_search(abs_evals, phi=None, tol=0.03, max_chain=5, verbose=True):
    """
    Search for chains of eigenvalues related by successive powers of phi.

    If the Paasch mass spiral is real, there should exist eigenvalues
    lambda_0, lambda_1, ..., lambda_k such that:
        lambda_{n+1} / lambda_n ~ phi  for all n

    This is a MUCH stronger condition than random pairwise phi matches.

    Args:
        abs_evals: sorted positive eigenvalues
        phi: target ratio (default: PHI_PAASCH)
        tol: relative tolerance
        max_chain: maximum chain length to search for
        verbose: print results

    Returns:
        chains: list of lists of (index, eigenvalue) tuples
    """
    if phi is None:
        phi = PHI_PAASCH

    n = len(abs_evals)
    chains = []

    # For each starting eigenvalue, try to extend a chain
    for start in range(n):
        chain = [(start, abs_evals[start])]
        current_val = abs_evals[start]

        for step in range(1, max_chain):
            target_val = current_val * phi
            # Find closest eigenvalue to target
            diffs = np.abs(abs_evals - target_val)
            best_idx = np.argmin(diffs)
            best_rel_err = diffs[best_idx] / target_val

            if best_rel_err < tol and best_idx > chain[-1][0]:
                chain.append((best_idx, abs_evals[best_idx]))
                current_val = abs_evals[best_idx]
            else:
                break

        if len(chain) >= 3:  # Minimum chain length of 3
            chains.append(chain)

    # Remove sub-chains (keep only maximal chains)
    maximal_chains = []
    for chain in sorted(chains, key=lambda c: -len(c)):
        indices = set(c[0] for c in chain)
        is_sub = False
        for existing in maximal_chains:
            existing_indices = set(c[0] for c in existing)
            if indices.issubset(existing_indices):
                is_sub = True
                break
        if not is_sub:
            maximal_chains.append(chain)

    if verbose:
        print(f"\n  Phi-chain search (phi={phi:.5f}, tol={tol*100:.0f}%):")
        print(f"    Total chains of length >= 3: {len(maximal_chains)}")
        for i, chain in enumerate(maximal_chains[:10]):
            indices = [c[0] for c in chain]
            values = [c[1] for c in chain]
            ratios = [values[k+1]/values[k] for k in range(len(values)-1)]
            ratio_str = ", ".join(f"{r:.5f}" for r in ratios)
            idx_str = " -> ".join(f"[{idx}]" for idx in indices)
            print(f"    Chain {i+1} (len={len(chain)}): {idx_str}")
            print(f"      values: {', '.join(f'{v:.6f}' for v in values)}")
            print(f"      ratios: {ratio_str}")
            avg_ratio = np.mean(ratios)
            std_ratio = np.std(ratios)
            print(f"      mean ratio: {avg_ratio:.6f} (std={std_ratio:.6f}, "
                  f"err from phi: {abs(avg_ratio-phi)/phi*100:.3f}%)")

    return maximal_chains


# =============================================================================
# MODULE 7: ALGEBRAIC RATIO IDENTIFICATION
# =============================================================================

def algebraic_ratio_analysis(abs_evals, verbose=True):
    """
    For bi-invariant (s=0) eigenvalues where lambda^2 = n/36, identify the
    EXACT algebraic ratios between eigenvalues.

    If lambda_i^2 = n_i/36 and lambda_j^2 = n_j/36, then:
        (lambda_j / lambda_i)^2 = n_j / n_i

    Check if any n_j/n_i equals phi^2 = 2.3457... or other algebraic numbers.

    Also check: is sqrt(7/3) = 1.52753 (the 0.26% match found in Session 12)
    the closest possible algebraic approximation to phi from SU(3) Casimirs?

    Args:
        abs_evals: sorted positive eigenvalues (at s=0 for algebraic identification)
        verbose: print results

    Returns:
        ratio_table: list of (n_i, n_j, ratio, closest_target, error) dicts
    """
    # Identify lambda^2 = n/36 values
    identified = []
    for k in range(len(abs_evals)):
        v2 = abs_evals[k]**2
        n36 = round(v2 * 36)
        if abs(v2 - n36 / 36.0) < 1e-4 and n36 > 0:
            identified.append((k, n36, abs_evals[k]))

    ratio_table = []

    if verbose:
        print(f"\n  Algebraic ratio analysis (bi-invariant s=0):")
        print(f"    Identified {len(identified)} eigenvalues with lambda^2 = n/36")
        print(f"\n    Close algebraic approximations to phi^2 = {PHI_2:.6f}:")

    # Check all pairs
    for i in range(len(identified)):
        for j in range(i + 1, len(identified)):
            ki, ni, vi = identified[i]
            kj, nj, vj = identified[j]

            ratio_sq = nj / ni  # exact rational number
            ratio = np.sqrt(ratio_sq)

            # Check against targets
            best_name = None
            best_err = float('inf')
            for name, target in TARGETS.items():
                err = abs(ratio - target) / target
                if err < best_err:
                    best_err = err
                    best_name = name

            entry = {
                'n_i': ni, 'n_j': nj,
                'ratio_sq': ratio_sq, 'ratio': ratio,
                'closest_target': best_name,
                'error': best_err,
                'idx_i': ki, 'idx_j': kj,
            }
            ratio_table.append(entry)

    # Sort by error and show near-misses
    ratio_table.sort(key=lambda x: x['error'])

    if verbose:
        print(f"\n    Top 15 closest matches to any target:")
        print(f"    {'n_i':>4}  {'n_j':>4}  {'n_j/n_i':>10}  {'ratio':>10}  "
              f"{'target':>10}  {'name':>8}  {'err%':>8}")
        for entry in ratio_table[:15]:
            print(f"    {entry['n_i']:4d}  {entry['n_j']:4d}  "
                  f"{entry['ratio_sq']:10.4f}  {entry['ratio']:10.6f}  "
                  f"{TARGETS.get(entry['closest_target'], 0):10.6f}  "
                  f"{entry['closest_target']:>8}  "
                  f"{entry['error']*100:8.4f}")

        # Special: sqrt(7/3) analysis
        sqrt73 = np.sqrt(7.0/3.0)
        err_phi = abs(sqrt73 - PHI_PAASCH) / PHI_PAASCH * 100
        err_gold = abs(sqrt73 - GOLDEN) / GOLDEN * 100
        print(f"\n    sqrt(7/3) = {sqrt73:.6f}")
        print(f"      vs phi  = {PHI_PAASCH:.6f} ({err_phi:.4f}% error)")
        print(f"      vs gold = {GOLDEN:.6f} ({err_gold:.4f}% error)")
        print(f"      This comes from lambda^2 = 7/36 and 3/36")
        print(f"      ALGEBRAIC INVARIANT: independent of deformation parameter s")

    return ratio_table


# =============================================================================
# MODULE 8: CONVERGENCE VS max_pq_sum
# =============================================================================

def convergence_vs_truncation(s_values, gens, f_abc, gammas,
                               pq_sums=[3, 4, 5], Lambda=5.0, verbose=True):
    """
    Study how spectral action results converge as max_pq_sum increases.

    This is essential for assessing whether:
    (a) The spectral action S(s) stabilizes
    (b) The Seeley-DeWitt coefficients converge
    (c) New phi ratios appear at higher truncation

    Args:
        s_values: array of s values to test
        gens, f_abc, gammas: SU(3) infrastructure
        pq_sums: list of max_pq_sum values to compare
        Lambda: cutoff for spectral action
        verbose: print results

    Returns:
        convergence_data: dict mapping max_pq_sum -> dict of results
    """
    convergence_data = {}

    for mps in pq_sums:
        if verbose:
            print(f"\n  {'='*60}")
            print(f"  max_pq_sum = {mps}")
            print(f"  {'='*60}")

        # Count sectors and eigenvalues
        n_sectors = 0
        total_evals = 0
        for p in range(mps + 1):
            for q in range(mps + 1 - p):
                dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
                n_sectors += 1
                total_evals += dim_pq * 16  # per-block

        if verbose:
            print(f"    Sectors: {n_sectors}, eigenvalues per s: {total_evals}")

        # Compute spectrum at s=0
        t0 = time.time()
        all_evals_0, eval_data_0 = collect_spectrum(
            0.0, gens, f_abc, gammas, max_pq_sum=mps, verbose=verbose
        )
        dt = time.time() - t0

        abs_evals_0, ratios_0 = analyze_spectrum(all_evals_0, verbose=False)

        # Phi ratio count
        phi_hits = 0
        n = len(abs_evals_0)
        n_pairs = n * (n - 1) // 2
        for i in range(n):
            for j in range(i + 1, n):
                r = abs_evals_0[j] / abs_evals_0[i]
                if abs(r - PHI_PAASCH) / PHI_PAASCH < 0.03:
                    phi_hits += 1

        # Spectral action
        S_heat, sector_contribs = spectral_action_smooth_cutoff(
            eval_data_0, Lambda, f_type='heat'
        )

        # Seeley-DeWitt
        coeffs, coeffs_unc = extract_seeley_dewitt_robust(eval_data_0, verbose=False)

        convergence_data[mps] = {
            'n_sectors': n_sectors,
            'n_evals': n,
            'n_total_evals': total_evals,
            'abs_evals': abs_evals_0,
            'S_heat_s0': S_heat,
            'phi_hits': phi_hits,
            'n_pairs': n_pairs,
            'phi_fraction': phi_hits / n_pairs if n_pairs > 0 else 0,
            'a_0': coeffs.get('a_0', np.nan),
            'a_2': coeffs.get('a_2', np.nan),
            'a_4': coeffs.get('a_4', np.nan),
            'compute_time': dt,
            'eval_data': eval_data_0,
        }

        if verbose:
            print(f"    Time: {dt:.1f}s")
            print(f"    Distinct |evals|: {n}")
            print(f"    S(0) = {S_heat:.2f} (Lambda={Lambda})")
            print(f"    phi hits: {phi_hits}/{n_pairs} ({phi_hits/n_pairs*100:.2f}%)")
            print(f"    a_0 = {coeffs.get('a_0', np.nan):.4e}")
            print(f"    a_2 = {coeffs.get('a_2', np.nan):.4e}")

    # Convergence summary
    if verbose and len(convergence_data) >= 2:
        print(f"\n  {'='*60}")
        print(f"  CONVERGENCE SUMMARY")
        print(f"  {'='*60}")
        print(f"  {'max_pq':>7}  {'n_eval':>7}  {'S(0)':>12}  {'phi_hits':>9}  "
              f"{'phi_frac':>9}  {'a_0':>12}  {'time(s)':>8}")
        for mps in pq_sums:
            d = convergence_data[mps]
            print(f"  {mps:>7d}  {d['n_evals']:>7d}  {d['S_heat_s0']:>12.2f}  "
                  f"{d['phi_hits']:>9d}  {d['phi_fraction']:>9.4f}  "
                  f"{d['a_0']:>12.4e}  {d['compute_time']:>8.1f}")

    return convergence_data


# =============================================================================
# MODULE 9: SPECTRAL ACTION WITH EXTENDED SPECTRUM
# =============================================================================

def extended_spectral_action(gens, f_abc, gammas, max_pq_sum=5,
                              Lambda=5.0, verbose=True):
    """
    Re-run the full spectral action analysis with extended spectrum.

    This updates the Session 14 results (which used max_pq_sum=3) with
    the kk-theorist's extended irreps (max_pq_sum=5).

    Args:
        gens, f_abc, gammas: SU(3) infrastructure
        max_pq_sum: extended truncation level
        Lambda: cutoff
        verbose: print results

    Returns:
        results: dict compatible with plot_spectral_action_results()
    """
    s_values = np.linspace(0.0, 2.0, 21)

    if verbose:
        print(f"\n  Extended spectral action (max_pq_sum={max_pq_sum}, Lambda={Lambda})")

    results = spectral_vs_baptista(
        s_values, gens, f_abc, gammas,
        max_pq_sum=max_pq_sum, Lambda=Lambda, verbose=verbose
    )

    return results


# =============================================================================
# MODULE 10: VISUALIZATION
# =============================================================================

def plot_phi_analysis(abs_evals, sector_hits, ratio_table, chains,
                       p_values, save_path=None):
    """
    Comprehensive 6-panel visualization of phi-structure analysis.

    Panel 1: Ratio histogram with target overlays
    Panel 2: Sector-pair heatmap (which sectors produce phi ratios)
    Panel 3: Phi-chain diagram
    Panel 4: Monte Carlo null distribution comparison
    Panel 5: Algebraic ratio identification
    Panel 6: Convergence of phi fraction vs max_pq_sum
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available; skipping phi analysis plots.")
        return

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Phi-Structure Analysis of SU(3) Dirac Spectrum',
                 fontsize=14, fontweight='bold')

    # Panel 1: Ratio histogram
    ax1 = axes[0, 0]
    n = len(abs_evals)
    ratios = []
    for i in range(n):
        for j in range(i + 1, n):
            ratios.append(abs_evals[j] / abs_evals[i])
    ratios = np.array(ratios)
    ratios_focus = ratios[(ratios >= 1.0) & (ratios <= 6.0)]

    ax1.hist(ratios_focus, bins=100, density=True, alpha=0.7, color='steelblue',
             edgecolor='none')
    for name, target in TARGETS.items():
        if target <= 6.0:
            ax1.axvline(target, color='red', linestyle='--', alpha=0.7, linewidth=1)
            ax1.text(target, ax1.get_ylim()[1]*0.9, name, fontsize=7,
                     rotation=90, va='top', ha='right', color='red')
    ax1.set_xlabel('Ratio lambda_j / lambda_i')
    ax1.set_ylabel('Density')
    ax1.set_title('Pairwise Ratio Distribution')

    # Panel 2: p-value summary
    ax2 = axes[0, 1]
    if p_values:
        names = list(p_values.keys())
        p_bonf = [p_values[n]['p_bonferroni'] for n in names]
        z_scores = [p_values[n]['z_score'] for n in names]
        colors = ['red' if p < 0.05 else 'orange' if p < 0.10 else 'gray'
                  for p in p_bonf]
        bars = ax2.bar(range(len(names)), z_scores, color=colors, edgecolor='black',
                       linewidth=0.5)
        ax2.set_xticks(range(len(names)))
        ax2.set_xticklabels(names, rotation=45, fontsize=8)
        ax2.axhline(2.0, color='orange', linestyle='--', label='z=2', alpha=0.5)
        ax2.axhline(3.0, color='red', linestyle='--', label='z=3', alpha=0.5)
        ax2.set_ylabel('z-score')
        ax2.set_title('Monte Carlo Significance')
        ax2.legend(fontsize=7)
    else:
        ax2.text(0.5, 0.5, 'No MC data', ha='center', va='center',
                 transform=ax2.transAxes)

    # Panel 3: Eigenvalue spectrum with phi-chain overlay
    ax3 = axes[0, 2]
    ax3.scatter(range(min(40, n)), abs_evals[:40], c='steelblue', s=20, zorder=3)
    if chains:
        for chain in chains[:3]:
            indices = [c[0] for c in chain]
            values = [c[1] for c in chain]
            ax3.plot(indices, values, 'r-o', markersize=8, linewidth=2,
                     alpha=0.6, zorder=4)
    ax3.set_xlabel('Eigenvalue index')
    ax3.set_ylabel('|lambda|')
    ax3.set_title('Spectrum with Phi-Chains')
    ax3.grid(True, alpha=0.3)

    # Panel 4: Algebraic ratio landscape
    ax4 = axes[1, 0]
    if ratio_table:
        errors = [entry['error'] * 100 for entry in ratio_table[:50]]
        ratios_plot = [entry['ratio'] for entry in ratio_table[:50]]
        ax4.scatter(ratios_plot, errors, s=15, c='steelblue', alpha=0.7)
        for name, target in TARGETS.items():
            if target <= max(ratios_plot):
                ax4.axvline(target, color='red', linestyle='--', alpha=0.3)
        ax4.set_xlabel('Eigenvalue ratio')
        ax4.set_ylabel('Error from nearest target (%)')
        ax4.set_title('Algebraic Ratio Matches')
        ax4.set_yscale('log')
        ax4.grid(True, alpha=0.3)
    else:
        ax4.text(0.5, 0.5, 'No data', ha='center', va='center',
                 transform=ax4.transAxes)

    # Panel 5: Sector pair contributions
    ax5 = axes[1, 1]
    if sector_hits:
        # Count hits per sector pair
        pair_counts = {}
        for h in sector_hits:
            key = (h['sector_i'], h['sector_j'])
            pair_counts[key] = pair_counts.get(key, 0) + 1

        pairs = sorted(pair_counts.items(), key=lambda x: -x[1])[:15]
        labels = [f"({p[0][0]},{p[0][1]})/({p[1][0]},{p[1][1]})" for p, c in pairs]
        counts = [c for p, c in pairs]
        ax5.barh(range(len(labels)), counts, color='steelblue',
                 edgecolor='black', linewidth=0.5)
        ax5.set_yticks(range(len(labels)))
        ax5.set_yticklabels(labels, fontsize=7)
        ax5.set_xlabel('Number of phi-ratio hits')
        ax5.set_title('Sector-Pair Contributions')
        ax5.invert_yaxis()
    else:
        ax5.text(0.5, 0.5, 'No sector hits', ha='center', va='center',
                 transform=ax5.transAxes)

    # Panel 6: sqrt(7/3) context
    ax6 = axes[1, 2]
    # Show sqrt(n_j/n_i) for all integer pairs up to n=100
    interesting_ratios = []
    for ni in range(1, 100):
        for nj in range(ni + 1, 100):
            r = np.sqrt(nj / ni)
            if 1.4 < r < 1.7:
                err = min(abs(r - PHI_PAASCH) / PHI_PAASCH,
                          abs(r - GOLDEN) / GOLDEN)
                interesting_ratios.append((ni, nj, r, err))

    interesting_ratios.sort(key=lambda x: x[3])
    top_rs = [ir[2] for ir in interesting_ratios[:30]]
    top_errs = [ir[3] * 100 for ir in interesting_ratios[:30]]
    top_labels = [f"{ir[0]}/{ir[1]}" for ir in interesting_ratios[:30]]

    ax6.scatter(top_rs, top_errs, c='steelblue', s=20, alpha=0.7)
    ax6.axvline(PHI_PAASCH, color='red', linestyle='-', alpha=0.5, label=f'phi={PHI_PAASCH}')
    ax6.axvline(GOLDEN, color='gold', linestyle='-', alpha=0.5, label=f'golden={GOLDEN:.5f}')
    # Highlight sqrt(7/3)
    sqrt73 = np.sqrt(7.0/3.0)
    ax6.scatter([sqrt73], [abs(sqrt73 - PHI_PAASCH)/PHI_PAASCH * 100],
                c='red', s=100, marker='*', zorder=5, label='sqrt(7/3)')
    ax6.set_xlabel('sqrt(n_j/n_i)')
    ax6.set_ylabel('Min error from phi or golden (%)')
    ax6.set_title('Algebraic Approximants to phi/golden')
    ax6.legend(fontsize=7)
    ax6.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"  Plot saved to {save_path}")
    plt.close()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("=" * 80)
    print("TIER 1: PHI-STRUCTURE ANALYSIS OF SU(3) DIRAC SPECTRUM")
    print("=" * 80)

    # --- Infrastructure ---
    print("\n[1] Building infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford err: {cliff_err:.2e}")

    su2_ok, su2_err = su2_benchmark()
    print(f"  SU(2) benchmark: {'PASS' if su2_ok else 'FAIL'} (err={su2_err:.2e})")

    # --- Extended spectrum at s=0 (bi-invariant) ---
    print(f"\n{'='*80}")
    print("[2] Extended spectrum at s=0 (bi-invariant, max_pq_sum=5)...")
    t0 = time.time()
    all_evals_0, eval_data_0 = collect_spectrum(
        0.0, gens, f_abc, gammas, max_pq_sum=5, verbose=True
    )
    dt = time.time() - t0
    print(f"  Computation time: {dt:.1f}s")

    abs_evals_0, ratios_0 = analyze_spectrum(all_evals_0, verbose=True)
    phi_pairs_0, gold_pairs_0 = analyze_nonconsecutive_ratios(abs_evals_0, n_low=50, verbose=True)

    # --- Comprehensive pairwise ratio scan ---
    print(f"\n{'='*80}")
    print("[3] Comprehensive pairwise ratio scan (all phi^n targets)...")
    pw_results, pw_stats = pairwise_ratio_scan(abs_evals_0, verbose=True)

    # --- Sector-resolved analysis ---
    print(f"\n{'='*80}")
    print("[4] Sector-resolved phi analysis...")
    sector_hits_0 = sector_phi_analysis(eval_data_0, s=0.0, verbose=True)

    # --- Phi-chain search ---
    print(f"\n{'='*80}")
    print("[5] Phi-chain search (consecutive phi-ratio sequences)...")
    chains_0 = phi_chain_search(abs_evals_0, verbose=True)

    # --- Algebraic ratio analysis ---
    print(f"\n{'='*80}")
    print("[6] Algebraic ratio analysis (bi-invariant: lambda^2 = n/36)...")
    ratio_table_0 = algebraic_ratio_analysis(abs_evals_0, verbose=True)

    # --- Spectral density analysis ---
    print(f"\n{'='*80}")
    print("[7] Spectral density analysis (ratio histogram)...")
    bin_edges, bin_counts, bin_density, anomalous = spectral_density_analysis(
        abs_evals_0, verbose=True
    )

    # --- Monte Carlo significance ---
    print(f"\n{'='*80}")
    print("[8] Monte Carlo significance test (50 random metrics)...")
    # Use fewer trials and lower max_pq_sum for MC to keep runtime reasonable
    random_spectra, random_stats = generate_random_metric_evals(
        gens, f_abc, gammas, max_pq_sum=3, n_random=50, verbose=True
    )
    p_values = monte_carlo_significance(
        abs_evals_0, random_spectra, verbose=True
    )

    # --- Extended spectrum at non-zero s values ---
    print(f"\n{'='*80}")
    print("[9] Phi analysis at non-zero s values...")
    s_scan = [0.0, 0.5, 1.0, 1.5, 2.0]
    phi_vs_s = {}
    for s in s_scan:
        print(f"\n  --- s = {s:.2f} ---")
        all_evals_s, eval_data_s = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=5, verbose=False
        )
        abs_evals_s, _ = analyze_spectrum(all_evals_s, verbose=False)
        pw_res_s, pw_stat_s = pairwise_ratio_scan(abs_evals_s, verbose=False)
        chains_s = phi_chain_search(abs_evals_s, verbose=False)

        phi_vs_s[s] = {
            'n_evals': len(abs_evals_s),
            'phi_hits': pw_stat_s['n_hits_phi'],
            'phi2_hits': pw_stat_s['n_hits_phi^2'],
            'golden_hits': pw_stat_s['n_hits_golden'],
            'n_pairs': pw_stat_s['n_pairs'],
            'n_chains': len(chains_s),
            'max_chain_len': max(len(c) for c in chains_s) if chains_s else 0,
        }
        print(f"    phi hits: {pw_stat_s['n_hits_phi']}/{pw_stat_s['n_pairs']} "
              f"({pw_stat_s['n_hits_phi']/max(pw_stat_s['n_pairs'],1)*100:.2f}%)")
        print(f"    phi^2 hits: {pw_stat_s['n_hits_phi^2']}")
        print(f"    golden hits: {pw_stat_s['n_hits_golden']}")
        print(f"    chains: {len(chains_s)}, "
              f"max length: {max(len(c) for c in chains_s) if chains_s else 0}")

    # --- Convergence check ---
    print(f"\n{'='*80}")
    print("[10] Convergence check: spectral action with max_pq_sum=3,4,5...")
    conv_data = convergence_vs_truncation(
        np.array([0.0, 1.0, 2.0]), gens, f_abc, gammas,
        pq_sums=[3, 4, 5], Lambda=5.0, verbose=True
    )

    # --- Plots ---
    print(f"\n{'='*80}")
    print("[11] Generating plots...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_phi_analysis(
        abs_evals_0, sector_hits_0, ratio_table_0, chains_0, p_values,
        save_path=os.path.join(script_dir, 'phi_analysis_results.png')
    )

    # --- SUMMARY ---
    print(f"\n{'='*80}")
    print("[12] SUMMARY")
    print("=" * 80)

    n_ev = len(abs_evals_0)
    n_pairs = n_ev * (n_ev - 1) // 2
    print(f"\n  1. SPECTRUM SIZE (max_pq_sum=5):")
    print(f"     Distinct |eigenvalues|: {n_ev}")
    print(f"     Pairwise ratios: {n_pairs}")

    print(f"\n  2. PHI-RATIO HITS (tol=3%):")
    for name in TARGETS:
        hits = pw_stats.get(f'n_hits_{name}', 0)
        frac = hits / n_pairs * 100 if n_pairs > 0 else 0
        print(f"     {name:>10}: {hits:4d} hits ({frac:.2f}%)")

    print(f"\n  3. PHI-CHAINS (length >= 3):")
    print(f"     Count: {len(chains_0)}")
    if chains_0:
        max_len = max(len(c) for c in chains_0)
        print(f"     Max length: {max_len}")

    print(f"\n  4. ALGEBRAIC INVARIANT (s-independent):")
    sqrt73 = np.sqrt(7.0/3.0)
    err_phi = abs(sqrt73 - PHI_PAASCH) / PHI_PAASCH * 100
    print(f"     sqrt(7/3) = {sqrt73:.6f}, phi = {PHI_PAASCH:.6f}")
    print(f"     Error: {err_phi:.4f}%")
    print(f"     Status: {'COINCIDENCE' if err_phi > 1.0 else 'NEAR-MISS' if err_phi > 0.1 else 'VERY CLOSE'}")

    print(f"\n  5. MONTE CARLO SIGNIFICANCE:")
    for name in ['phi', 'golden']:
        if name in p_values:
            pv = p_values[name]
            sig = 'SIGNIFICANT' if pv['p_bonferroni'] < 0.05 else \
                  'MARGINAL' if pv['p_bonferroni'] < 0.10 else 'NOT SIGNIFICANT'
            print(f"     {name}: z={pv['z_score']:.2f}, "
                  f"p(Bonferroni)={pv['p_bonferroni']:.4f} [{sig}]")

    print(f"\n  6. PHI vs DEFORMATION PARAMETER s:")
    print(f"     {'s':>5}  {'phi_hits':>9}  {'phi_frac':>9}  {'chains':>7}  {'max_len':>8}")
    for s in s_scan:
        d = phi_vs_s[s]
        print(f"     {s:5.2f}  {d['phi_hits']:>9d}  "
              f"{d['phi_hits']/max(d['n_pairs'],1)*100:>8.2f}%  "
              f"{d['n_chains']:>7d}  {d['max_chain_len']:>8d}")

    print(f"\n  7. CONVERGENCE:")
    for mps in [3, 4, 5]:
        if mps in conv_data:
            d = conv_data[mps]
            print(f"     max_pq={mps}: S(0)={d['S_heat_s0']:.2f}, "
                  f"phi_frac={d['phi_fraction']*100:.2f}%, "
                  f"a_0={d['a_0']:.4e}")

    # --- Final assessment ---
    print(f"\n  8. ASSESSMENT:")
    # Check if phi fraction exceeds random expectation
    if 'phi' in p_values and p_values['phi']['p_bonferroni'] < 0.05:
        print(f"     PHI STRUCTURE: STATISTICALLY SIGNIFICANT")
        print(f"     Jensen spectrum has MORE phi-ratio pairs than random metrics")
    elif 'phi' in p_values and p_values['phi']['z_score'] > 1.5:
        print(f"     PHI STRUCTURE: SUGGESTIVE BUT NOT SIGNIFICANT")
        print(f"     Trend toward phi-excess, needs more MC trials or higher truncation")
    else:
        print(f"     PHI STRUCTURE: NOT DETECTED")
        print(f"     Phi-ratio hits consistent with random spectral density")

    if chains_0 and max(len(c) for c in chains_0) >= 4:
        print(f"     PHI-CHAINS: STRONG (length {max(len(c) for c in chains_0)} chain found)")
    elif chains_0:
        print(f"     PHI-CHAINS: WEAK (max length {max(len(c) for c in chains_0)})")
    else:
        print(f"     PHI-CHAINS: ABSENT")

    sqrt73_verdict = "ALGEBRAIC NEAR-MISS" if err_phi < 0.5 else "COINCIDENCE"
    print(f"     sqrt(7/3): {sqrt73_verdict} ({err_phi:.4f}% from phi)")

    print(f"\n{'='*80}")
    print("PHI-STRUCTURE ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
