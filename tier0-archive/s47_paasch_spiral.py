#!/usr/bin/env python3
"""
s47_paasch_spiral.py — Paasch Spiral Analysis of Full Dirac Spectrum
=====================================================================

Session 47, Wave 3-1 (PAASCH-SPIRAL-47)

Tests whether the full Dirac eigenvalue spectrum on Jensen-deformed SU(3)
exhibits the discrete sequence structure predicted by Paasch's logarithmic
mass quantization framework.

Paasch's quantization factor phi = 1.53158 was found in the Dirac spectrum
at S12: m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15. This script tests
whether the FULL spectrum organizes into discrete angular sequences when
mapped onto the logarithmic spiral m(angle) = m_0 * exp(k * angle),
where k = ln(1.53158) / (2*pi).

Gate PAASCH-SPIRAL-47:
  PASS: Rayleigh test rejects uniformity at p < 0.01 AND >= 3 distinct clusters
  INFO: Weak clustering (p < 0.05) or fewer than 3 clusters
  FAIL: Phases consistent with uniform distribution (p > 0.05)

Author: paasch-mass-quantization-analyst
"""

import sys
import numpy as np
from scipy import stats
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────────
#  Constants
# ──────────────────────────────────────────────────────────────────────
PHI_PAASCH = 1.53158       # Quantization factor from x = e^{-x^2}
K_SPIRAL = np.log(PHI_PAASCH) / (2 * np.pi)  # Spiral constant
TAU_VALUES = [0.00, 0.05, 0.10, 0.15, 0.19]  # Available tau values

DATA_DIR = Path(__file__).parent
OUTPUT_NPZ = DATA_DIR / 's47_paasch_spiral.npz'
OUTPUT_PNG = DATA_DIR / 's47_paasch_spiral.png'

# Tolerance for grouping eigenvalues as "unique"
EIGENVALUE_TOL = 1e-8

# ──────────────────────────────────────────────────────────────────────
#  Helper: Extract unique eigenvalue magnitudes with tolerance grouping
# ──────────────────────────────────────────────────────────────────────
def get_unique_eigenvalues(omega, dim2):
    """
    Group eigenvalues within tolerance, return (unique_vals, total_deg, counts).
    """
    abs_omega = np.abs(omega)
    # Sort indices
    sort_idx = np.argsort(abs_omega)
    sorted_omega = abs_omega[sort_idx]
    sorted_dim2 = dim2[sort_idx]

    unique_vals = []
    total_degs = []
    counts = []

    i = 0
    while i < len(sorted_omega):
        j = i
        while j < len(sorted_omega) and abs(sorted_omega[j] - sorted_omega[i]) < EIGENVALUE_TOL:
            j += 1
        group_omega = sorted_omega[i:j]
        group_deg = sorted_dim2[i:j]
        mean_val = np.mean(group_omega)
        unique_vals.append(mean_val)
        total_degs.append(np.sum(group_deg))
        counts.append(j - i)
        i = j

    return np.array(unique_vals), np.array(total_degs), np.array(counts)


# ──────────────────────────────────────────────────────────────────────
#  Helper: Map eigenvalues onto Paasch spiral
# ──────────────────────────────────────────────────────────────────────
def spiral_mapping(eigenvalues):
    """
    Map eigenvalues onto the Paasch spiral.

    Returns:
        angles: absolute spiral angle for each eigenvalue
        phases: angle mod 2*pi (position within one turn)
        turns: fractional turn number
    """
    lam_min = eigenvalues.min()
    # Spiral angle: phi_i = (1/k) * ln(lambda_i / lambda_min)
    angles = (1.0 / K_SPIRAL) * np.log(eigenvalues / lam_min)
    phases = angles % (2 * np.pi)
    turns = angles / (2 * np.pi)
    return angles, phases, turns


# ──────────────────────────────────────────────────────────────────────
#  Rayleigh test for circular uniformity
# ──────────────────────────────────────────────────────────────────────
def rayleigh_test(phases, weights=None):
    """
    Rayleigh test for non-uniformity of circular data.

    H0: phases are uniformly distributed on [0, 2*pi)
    H1: phases are clustered (unimodal alternative)

    Returns (R_bar, Z, p_value).

    For unweighted: R_bar = |sum(e^{i*theta})| / n
    Z = n * R_bar^2  (Rayleigh statistic)
    p ~ exp(-Z) for large n.
    """
    n = len(phases)
    if weights is not None:
        # Weighted Rayleigh test
        w = weights / weights.sum()
        C = np.sum(w * np.cos(phases))
        S = np.sum(w * np.sin(phases))
        R_bar = np.sqrt(C**2 + S**2)
        # Effective n for weighted case
        n_eff = 1.0 / np.sum(w**2)
        Z = n_eff * R_bar**2
    else:
        C = np.mean(np.cos(phases))
        S = np.mean(np.sin(phases))
        R_bar = np.sqrt(C**2 + S**2)
        Z = n * R_bar**2
        n_eff = n

    # p-value: exact for small Z, asymptotic otherwise
    p_value = np.exp(-Z) * (1 + (2*Z - Z**2) / (4*n_eff)
              - (24*Z - 132*Z**2 + 76*Z**3 - 9*Z**4) / (288*n_eff**2))
    p_value = max(0, min(1, p_value))

    return R_bar, Z, p_value


# ──────────────────────────────────────────────────────────────────────
#  Cluster detection via circular histogram
# ──────────────────────────────────────────────────────────────────────
def find_clusters(phases, n_bins=36, threshold_sigma=2.0):
    """
    Find angular clusters by identifying bins significantly above
    uniform expectation.

    Returns list of (center_angle, count, eigenvalue_indices).
    """
    bin_edges = np.linspace(0, 2*np.pi, n_bins + 1)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    hist, _ = np.histogram(phases, bins=bin_edges)

    expected = len(phases) / n_bins
    sigma = np.sqrt(expected)  # Poisson

    threshold = expected + threshold_sigma * sigma

    # Find bins above threshold
    hot_bins = np.where(hist > threshold)[0]

    # Merge adjacent hot bins into clusters
    clusters = []
    if len(hot_bins) > 0:
        current_start = hot_bins[0]
        current_end = hot_bins[0]
        for b in hot_bins[1:]:
            if b == current_end + 1 or (current_end == n_bins - 1 and b == 0):
                current_end = b
            else:
                # Finalize cluster
                cluster_bins = list(range(current_start, current_end + 1))
                cluster_center = np.mean([bin_centers[bb] for bb in cluster_bins])
                cluster_count = sum(hist[bb] for bb in cluster_bins)
                # Find which eigenvalues are in this cluster
                cluster_mask = np.zeros(len(phases), dtype=bool)
                for bb in cluster_bins:
                    in_bin = (phases >= bin_edges[bb]) & (phases < bin_edges[bb+1])
                    cluster_mask |= in_bin
                clusters.append({
                    'center': cluster_center,
                    'center_deg': np.degrees(cluster_center),
                    'count': cluster_count,
                    'indices': np.where(cluster_mask)[0],
                    'bins': cluster_bins,
                })
                current_start = b
                current_end = b
        # Finalize last cluster
        cluster_bins = list(range(current_start, current_end + 1))
        cluster_center = np.mean([bin_centers[bb] for bb in cluster_bins])
        cluster_count = sum(hist[bb] for bb in cluster_bins)
        cluster_mask = np.zeros(len(phases), dtype=bool)
        for bb in cluster_bins:
            in_bin = (phases >= bin_edges[bb]) & (phases < bin_edges[bb+1])
            cluster_mask |= in_bin
        clusters.append({
            'center': cluster_center,
            'center_deg': np.degrees(cluster_center),
            'count': cluster_count,
            'indices': np.where(cluster_mask)[0],
            'bins': cluster_bins,
        })

    return clusters, hist, bin_centers, expected, threshold


# ──────────────────────────────────────────────────────────────────────
#  Phi ratio pair counting
# ──────────────────────────────────────────────────────────────────────
def count_phi_ratio_pairs(eigenvalues, phi=PHI_PAASCH, tol_frac=0.01):
    """
    Count pairs where lambda_j/lambda_i is within tol_frac of phi.
    Compare to expected count from random uniform spectrum.
    """
    n = len(eigenvalues)
    sorted_ev = np.sort(eigenvalues)

    observed_pairs = 0
    pair_list = []
    for i in range(n):
        for j in range(i+1, n):
            ratio = sorted_ev[j] / sorted_ev[i]
            if abs(ratio - phi) / phi < tol_frac:
                observed_pairs += 1
                pair_list.append((i, j, sorted_ev[i], sorted_ev[j], ratio))

    # Expected count for random spectrum with same range
    # A uniform distribution on [lam_min, lam_max] has PDF f(x) = 1/(lam_max - lam_min)
    # P(|lambda_j/lambda_i - phi| < tol_frac * phi) for uniform
    lam_min, lam_max = sorted_ev[0], sorted_ev[-1]
    # Monte Carlo estimate
    rng = np.random.default_rng(42)
    n_mc = 100000
    mc_counts = []
    for _ in range(50):
        mc_sample = rng.uniform(lam_min, lam_max, n)
        mc_sample.sort()
        mc_count = 0
        for i in range(n):
            for j in range(i+1, n):
                ratio = mc_sample[j] / mc_sample[i]
                if abs(ratio - phi) / phi < tol_frac:
                    mc_count += 1
        mc_counts.append(mc_count)

    expected_random = np.mean(mc_counts)
    std_random = np.std(mc_counts)

    return observed_pairs, expected_random, std_random, pair_list


# ──────────────────────────────────────────────────────────────────────
#  Sector assignment (rank-based, from W1-1)
# ──────────────────────────────────────────────────────────────────────
def assign_sectors_rank(eigenvalues_per_rep):
    """
    Given eigenvalues grouped by (p,q) rep, assign B1/B2/B3 by rank.
    B1: lowest 2*dim eigenvalues
    B2: next 8*dim eigenvalues
    B3: top 6*dim eigenvalues
    """
    sectors = {}
    for (p, q), evals in eigenvalues_per_rep.items():
        dim_pq = (p+1) * (q+1) * (p+q+2) // 2
        abs_ev = np.sort(np.abs(evals))
        # Each eigenvalue appears as +/- pair, so n_evals = 16*dim
        n_total = len(abs_ev)
        n_per_16 = n_total // 16 if n_total >= 16 else 1

        # Get unique absolute values
        unique_abs = np.unique(np.round(abs_ev, 10))

        # Rank: lowest 2*dim -> B1, next 8*dim -> B2, top 6*dim -> B3
        # Since evals come as +/- pairs and we're looking at |lambda|,
        # we have n_total/2 unique magnitudes (approximately)
        # Actually, unique_abs already computed above
        # Map each unique value to sector by its rank among unique values
        n_unique = len(unique_abs)
        sector_map = {}
        for idx, uv in enumerate(unique_abs):
            # Count how many evals with this |value|
            count_at_val = np.sum(np.abs(abs_ev - uv) < 1e-10)
            # Rank-based assignment per unique value
            # B1: ranks 0 to 2*dim-1 out of 16*dim total (or proportionally)
            frac = idx / n_unique
            if frac < 2/16:
                sector_map[uv] = 'B1'
            elif frac < 10/16:
                sector_map[uv] = 'B2'
            else:
                sector_map[uv] = 'B3'

        sectors[(p,q)] = sector_map

    return sectors


# ──────────────────────────────────────────────────────────────────────
#  MAIN ANALYSIS
# ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 78)
    print("PAASCH SPIRAL ANALYSIS OF FULL DIRAC SPECTRUM (S47 W3-1)")
    print("=" * 78)
    print(f"\nPaasch quantization factor phi = {PHI_PAASCH}")
    print(f"Spiral constant k = ln(phi)/(2*pi) = {K_SPIRAL:.8f}")
    print(f"One full turn = multiplication by phi = {PHI_PAASCH}")

    # Load data
    d44 = np.load(DATA_DIR / 's44_dos_tau.npz', allow_pickle=True)

    # Also load s46 for max_pq_sum=4 spectrum
    try:
        d46 = np.load(DATA_DIR / 's46_max_pq_sum_4.npz', allow_pickle=True)
        has_s46 = True
    except FileNotFoundError:
        has_s46 = False

    # Load sector assignments from W1-1
    try:
        d_sector = np.load(DATA_DIR / 's47_pi_sector.npz', allow_pickle=True)
        has_sectors = True
    except FileNotFoundError:
        has_sectors = False

    # ──────────────────────────────────────────────────────────
    #  Step 1: Extract spectra at all tau values
    # ──────────────────────────────────────────────────────────
    results = {}

    for tau in TAU_VALUES:
        tau_key = f'tau{tau:.2f}'
        omega = d44[f'{tau_key}_all_omega']
        dim2 = d44[f'{tau_key}_all_dim2']

        unique_vals, total_degs, counts = get_unique_eigenvalues(omega, dim2)

        print(f"\n{'─'*60}")
        print(f"tau = {tau:.2f}: {len(unique_vals)} unique eigenvalues from {len(omega)} total")
        print(f"  Range: [{unique_vals[0]:.6f}, {unique_vals[-1]:.6f}]")
        print(f"  Ratio max/min: {unique_vals[-1]/unique_vals[0]:.6f}")
        n_turns = np.log(unique_vals[-1] / unique_vals[0]) / np.log(PHI_PAASCH)
        print(f"  Spiral coverage: {n_turns:.3f} turns ({n_turns*360:.1f} degrees)")

        # ──────────────────────────────────────────────────────
        #  Step 2: Map onto spiral
        # ──────────────────────────────────────────────────────
        angles, phases, turns = spiral_mapping(unique_vals)

        # ──────────────────────────────────────────────────────
        #  Step 3: Statistical tests for sequence structure
        # ──────────────────────────────────────────────────────

        # Rayleigh test (unweighted)
        R_bar, Z, p_ray = rayleigh_test(phases)
        print(f"\n  Rayleigh test (unweighted):")
        print(f"    R_bar = {R_bar:.6f}, Z = {Z:.4f}, p = {p_ray:.6e}")

        # Rayleigh test (PW-weighted)
        R_bar_w, Z_w, p_ray_w = rayleigh_test(phases, weights=total_degs.astype(float))
        print(f"  Rayleigh test (PW-weighted):")
        print(f"    R_bar = {R_bar_w:.6f}, Z = {Z_w:.4f}, p = {p_ray_w:.6e}")

        # Cluster detection
        clusters, hist, bin_centers, expected, threshold = find_clusters(phases, n_bins=36)
        print(f"\n  Angular clustering (36 bins, 2-sigma threshold):")
        print(f"    Expected per bin: {expected:.1f}, threshold: {threshold:.1f}")
        print(f"    Number of clusters: {len(clusters)}")
        for cl in clusters:
            print(f"      Cluster at {cl['center_deg']:.1f} deg: {cl['count']} eigenvalues")

        # Also try higher-order Rayleigh (for multi-modal clustering)
        # Test at harmonics: 2, 3, 4, 6, 8 (corresponding to 2, 3, 4, 6, 8 clusters)
        print(f"\n  Higher-harmonic Rayleigh tests:")
        harmonic_results = {}
        for h in [2, 3, 4, 6, 8]:
            phases_h = (h * phases) % (2 * np.pi)
            R_h, Z_h, p_h = rayleigh_test(phases_h)
            harmonic_results[h] = (R_h, Z_h, p_h)
            sig_str = "***" if p_h < 0.001 else "**" if p_h < 0.01 else "*" if p_h < 0.05 else ""
            print(f"    h={h}: R={R_h:.4f}, Z={Z_h:.3f}, p={p_h:.4e} {sig_str}")

        # Kuiper's test against uniform (more powerful than Rayleigh for multi-modal)
        # Use KS test against uniform as proxy
        ks_stat, ks_p = stats.kstest(phases / (2*np.pi), 'uniform')
        print(f"\n  KS test against uniform: D={ks_stat:.6f}, p={ks_p:.6e}")

        # Watson U^2 test (angular goodness of fit)
        # Compute manually: U^2 = sum((F_i - i/n)^2) + ... correction
        sorted_phases = np.sort(phases / (2 * np.pi))  # Map to [0,1)
        n = len(sorted_phases)
        u_i = sorted_phases
        U2 = np.sum((u_i - (2*np.arange(1, n+1) - 1) / (2*n))**2) + 1/(12*n)
        print(f"  Watson U^2 = {U2:.6f}")

        results[tau] = {
            'unique_vals': unique_vals,
            'total_degs': total_degs,
            'counts': counts,
            'angles': angles,
            'phases': phases,
            'turns': turns,
            'R_bar': R_bar,
            'Z': Z,
            'p_rayleigh': p_ray,
            'R_bar_weighted': R_bar_w,
            'Z_weighted': Z_w,
            'p_rayleigh_weighted': p_ray_w,
            'n_clusters': len(clusters),
            'clusters': clusters,
            'hist': hist,
            'bin_centers': bin_centers,
            'ks_stat': ks_stat,
            'ks_p': ks_p,
            'U2': U2,
            'harmonic_results': harmonic_results,
        }

    # ──────────────────────────────────────────────────────────
    #  Step 4: Phi ratio pair counting (at fold)
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("PHI RATIO PAIR COUNTING (tau=0.19)")
    print(f"{'='*60}")

    fold_vals = results[0.19]['unique_vals']
    n_pairs_obs, n_pairs_exp, n_pairs_std, pair_list = count_phi_ratio_pairs(fold_vals)

    print(f"\nPairs with lambda_j/lambda_i within 1% of phi={PHI_PAASCH}:")
    print(f"  Observed: {n_pairs_obs}")
    print(f"  Expected (random uniform): {n_pairs_exp:.1f} +/- {n_pairs_std:.1f}")
    if n_pairs_std > 0:
        z_score = (n_pairs_obs - n_pairs_exp) / n_pairs_std
        print(f"  Z-score: {z_score:.2f}")
    else:
        z_score = 0

    if len(pair_list) > 0:
        print(f"\n  Phi-ratio pairs (first 20):")
        for i, (idx_i, idx_j, lam_i, lam_j, ratio) in enumerate(pair_list[:20]):
            dev = (ratio - PHI_PAASCH) / PHI_PAASCH * 100
            print(f"    [{idx_i:3d},{idx_j:3d}] {lam_i:.6f} / {lam_j:.6f} = {ratio:.6f} (dev={dev:+.3f}%)")

    # ──────────────────────────────────────────────────────────
    #  Step 5: Nearest-neighbor ratio distribution
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("NEAREST-NEIGHBOR RATIO DISTRIBUTION (tau=0.19)")
    print(f"{'='*60}")

    nn_ratios = fold_vals[1:] / fold_vals[:-1]
    print(f"\nTotal nearest-neighbor ratios: {len(nn_ratios)}")
    print(f"  Range: [{nn_ratios.min():.6f}, {nn_ratios.max():.6f}]")
    print(f"  Mean: {np.mean(nn_ratios):.6f}")
    print(f"  Median: {np.median(nn_ratios):.6f}")

    # How many NN ratios close to phi?
    nn_near_phi = np.sum(np.abs(nn_ratios - PHI_PAASCH) / PHI_PAASCH < 0.01)
    print(f"  NN ratios within 1% of phi: {nn_near_phi}")
    nn_near_phi_5 = np.sum(np.abs(nn_ratios - PHI_PAASCH) / PHI_PAASCH < 0.05)
    print(f"  NN ratios within 5% of phi: {nn_near_phi_5}")

    # ──────────────────────────────────────────────────────────
    #  Step 6: Cross-reference with sectors (if available)
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("SECTOR CROSS-REFERENCE")
    print(f"{'='*60}")

    if has_sectors:
        pi_evals = d_sector['pi_phase_eigenvalues']
        pi_sectors = d_sector['pi_phase_sectors']
        pi_reps = d_sector['pi_phase_reps']

        # Map pi-phase eigenvalues onto spiral
        fold_min = fold_vals.min()
        pi_angles = (1.0 / K_SPIRAL) * np.log(pi_evals / fold_min)
        pi_phases = pi_angles % (2 * np.pi)

        print(f"\nPi-phase states on spiral:")
        for i in range(len(pi_evals)):
            print(f"  {str(pi_reps[i]):>5s} {str(pi_sectors[i]):>2s}  "
                  f"|lam|={pi_evals[i]:.6f}  angle={np.degrees(pi_phases[i]):.1f} deg  "
                  f"turn={pi_angles[i]/(2*np.pi):.3f}")

    # ──────────────────────────────────────────────────────────
    #  Step 7: max_pq_sum=4 analysis
    # ──────────────────────────────────────────────────────────
    if has_s46:
        print(f"\n{'='*60}")
        print("MAX_PQ_SUM=4 EXTENDED SPECTRUM (tau=0.19)")
        print(f"{'='*60}")

        wl = d46['weyl_lambdas']
        # Get unique values
        wl_unique = np.unique(np.round(wl, 10))

        print(f"Total eigenvalues: {len(wl)}")
        print(f"Unique eigenvalues: {len(wl_unique)}")
        print(f"Range: [{wl_unique[0]:.6f}, {wl_unique[-1]:.6f}]")
        n_turns_4 = np.log(wl_unique[-1] / wl_unique[0]) / np.log(PHI_PAASCH)
        print(f"Spiral coverage: {n_turns_4:.3f} turns ({n_turns_4*360:.1f} degrees)")

        angles_4, phases_4, turns_4 = spiral_mapping(wl_unique)

        # Rayleigh test
        R4, Z4, p4 = rayleigh_test(phases_4)
        print(f"\nRayleigh test (unweighted):")
        print(f"  R_bar = {R4:.6f}, Z = {Z4:.4f}, p = {p4:.6e}")

        # Clusters
        clusters_4, hist_4, bc_4, exp_4, thr_4 = find_clusters(phases_4, n_bins=36)
        print(f"Number of clusters: {len(clusters_4)}")
        for cl in clusters_4:
            print(f"  Cluster at {cl['center_deg']:.1f} deg: {cl['count']} eigenvalues")

        # KS test
        ks4, ksp4 = stats.kstest(phases_4 / (2*np.pi), 'uniform')
        print(f"KS test: D={ks4:.6f}, p={ksp4:.6e}")

    # ──────────────────────────────────────────────────────────
    #  Step 8: Paasch sequence assignment
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("PAASCH SEQUENCE ASSIGNMENT (6 sequences at 45-degree separation)")
    print(f"{'='*60}")

    # Paasch's original sequences are at 0, 45, 132, 150, 245, 260, 278, 317 degrees
    # His principal 6 are S1-S6 at roughly 45-degree steps
    # We map our eigenvalues to angles and check if they cluster near these

    fold_phases_deg = np.degrees(results[0.19]['phases'])
    print(f"\nPhase distribution at fold (degrees):")
    print(f"  Min: {fold_phases_deg.min():.1f}")
    print(f"  Max: {fold_phases_deg.max():.1f}")
    print(f"  Mean: {fold_phases_deg.mean():.1f}")
    print(f"  Std: {fold_phases_deg.std():.1f}")

    # Check each 45-degree bin
    print(f"\n  Counts in 45-degree bins:")
    for start in range(0, 360, 45):
        end = start + 45
        count = np.sum((fold_phases_deg >= start) & (fold_phases_deg < end))
        expected_uniform = len(fold_phases_deg) / 8
        ratio = count / expected_uniform if expected_uniform > 0 else 0
        print(f"    [{start:3d}-{end:3d}) deg: {count:3d} eigenvalues (ratio to uniform: {ratio:.2f})")

    # ──────────────────────────────────────────────────────────
    #  GATE VERDICT
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*78}")
    print("GATE VERDICT: PAASCH-SPIRAL-47")
    print(f"{'='*78}")

    fold_result = results[0.19]
    p_ray_fold = fold_result['p_rayleigh']
    n_clusters_fold = fold_result['n_clusters']

    print(f"\n  Rayleigh p-value (unweighted, tau=0.19): {p_ray_fold:.6e}")
    print(f"  Number of clusters (2-sigma): {n_clusters_fold}")
    print(f"  KS p-value: {fold_result['ks_p']:.6e}")

    # Also check the most significant harmonic
    best_harmonic_p = 1.0
    best_harmonic_h = 0
    for h, (R_h, Z_h, p_h) in fold_result['harmonic_results'].items():
        if p_h < best_harmonic_p:
            best_harmonic_p = p_h
            best_harmonic_h = h
    print(f"  Best harmonic: h={best_harmonic_h}, p={best_harmonic_p:.6e}")

    # Gate criteria:
    # PASS: p < 0.01 AND >= 3 clusters
    # INFO: p < 0.05 OR fewer than 3 clusters
    # FAIL: p > 0.05

    if p_ray_fold < 0.01 and n_clusters_fold >= 3:
        verdict = "PASS"
    elif p_ray_fold < 0.05 or n_clusters_fold >= 3:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # But we should also check: does ANY test reject uniformity?
    any_test_rejects = (p_ray_fold < 0.01 or fold_result['ks_p'] < 0.01 or
                        best_harmonic_p < 0.01)

    print(f"\n  ANY test rejects uniformity at p<0.01: {any_test_rejects}")
    print(f"\n  >>> GATE VERDICT: {verdict} <<<")

    if verdict == "FAIL":
        print(f"\n  The phase distribution on the Paasch spiral is consistent with")
        print(f"  uniform for the 120 unique eigenvalues at max_pq_sum=3.")
        print(f"  The Dirac spectrum does NOT exhibit discrete sequence structure")
        print(f"  in the Paasch logarithmic spiral at this truncation.")
    elif verdict == "INFO":
        print(f"\n  Weak or partial clustering detected. May become significant")
        print(f"  at higher truncation.")
    else:
        print(f"\n  Significant clustering detected. {n_clusters_fold} angular sequences found.")

    # Context note
    print(f"\n  IMPORTANT CONTEXT:")
    print(f"  The spectrum spans only {np.log(fold_vals[-1]/fold_vals[0])/np.log(PHI_PAASCH):.2f} turns")
    print(f"  ({fold_vals[-1]/fold_vals[0]:.3f} octaves) of the spiral.")
    print(f"  Paasch's particle mass spectrum spans ~50+ turns (electron to top quark).")
    print(f"  The Dirac spectrum at max_pq_sum=3 probes a very small angular window.")

    # ──────────────────────────────────────────────────────────
    #  Save results
    # ──────────────────────────────────────────────────────────
    save_dict = {
        'phi_paasch': PHI_PAASCH,
        'k_spiral': K_SPIRAL,
        'gate_verdict': verdict,
        'p_rayleigh_fold': p_ray_fold,
        'p_rayleigh_weighted_fold': fold_result['p_rayleigh_weighted'],
        'n_clusters_fold': n_clusters_fold,
        'ks_p_fold': fold_result['ks_p'],
        'best_harmonic_h': best_harmonic_h,
        'best_harmonic_p': best_harmonic_p,
        'n_phi_pairs_observed': n_pairs_obs,
        'n_phi_pairs_expected': n_pairs_exp,
        'n_phi_pairs_std': n_pairs_std,
        'phi_pair_zscore': z_score,
        'nn_ratios': nn_ratios,
    }

    for tau in TAU_VALUES:
        key = f'tau{tau:.2f}'
        r = results[tau]
        save_dict[f'{key}_unique_vals'] = r['unique_vals']
        save_dict[f'{key}_phases'] = r['phases']
        save_dict[f'{key}_turns'] = r['turns']
        save_dict[f'{key}_p_rayleigh'] = r['p_rayleigh']
        save_dict[f'{key}_R_bar'] = r['R_bar']
        save_dict[f'{key}_n_clusters'] = r['n_clusters']
        save_dict[f'{key}_hist'] = r['hist']
        save_dict[f'{key}_bin_centers'] = r['bin_centers']

    if has_s46:
        save_dict['pq4_unique_vals'] = wl_unique
        save_dict['pq4_phases'] = phases_4
        save_dict['pq4_p_rayleigh'] = p4
        save_dict['pq4_n_clusters'] = len(clusters_4)

    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"\nData saved to {OUTPUT_NPZ}")

    # ──────────────────────────────────────────────────────────
    #  VISUALIZATION
    # ──────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(20, 16))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.35)

    # ── Plot A: Polar plot at fold (tau=0.19) ──
    ax_polar = fig.add_subplot(gs[0, 0], projection='polar')
    r = results[0.19]

    # Color by rough sector: use log(eigenvalue) position
    colors = plt.cm.viridis((r['unique_vals'] - r['unique_vals'].min()) /
                             (r['unique_vals'].max() - r['unique_vals'].min()))
    sizes = 5 + 30 * np.log1p(r['total_degs']) / np.log1p(r['total_degs'].max())

    ax_polar.scatter(r['phases'], r['unique_vals'], c=r['unique_vals'],
                     cmap='viridis', s=sizes, alpha=0.7, edgecolors='k', linewidths=0.3)

    # Mark pi-phase states
    if has_sectors:
        pi_phases_fold = (1.0 / K_SPIRAL) * np.log(pi_evals / fold_vals.min()) % (2*np.pi)
        ax_polar.scatter(pi_phases_fold, pi_evals, marker='*', s=100,
                        c='red', edgecolors='darkred', linewidths=0.5, zorder=5,
                        label='pi-phase states')

    # Mark Paasch 45-degree lines
    for angle_deg in range(0, 360, 45):
        ax_polar.plot([np.radians(angle_deg)] * 2, [0.8, 2.1],
                     'k--', alpha=0.15, linewidth=0.5)

    ax_polar.set_title(f'A: Paasch Spiral (tau=0.19)\n'
                       f'k={K_SPIRAL:.5f}, phi={PHI_PAASCH}',
                       fontsize=10, pad=15)
    ax_polar.set_rlabel_position(135)
    ax_polar.set_rlim(0.75, 2.15)

    # ── Plot B: Angular histograms at each tau ──
    ax_hist = fig.add_subplot(gs[0, 1])
    colors_tau = plt.cm.plasma(np.linspace(0.1, 0.9, len(TAU_VALUES)))

    for idx, tau in enumerate(TAU_VALUES):
        r_tau = results[tau]
        phases_deg = np.degrees(r_tau['phases'])
        ax_hist.hist(phases_deg, bins=36, alpha=0.3, color=colors_tau[idx],
                    density=True, label=f'tau={tau:.2f}')

    ax_hist.axhline(1/360, color='gray', linestyle='--', alpha=0.5, label='uniform')
    ax_hist.set_xlabel('Phase (degrees)', fontsize=10)
    ax_hist.set_ylabel('Density', fontsize=10)
    ax_hist.set_title('B: Angular Histogram by tau', fontsize=10)
    ax_hist.legend(fontsize=7)
    ax_hist.set_xlim(0, 360)

    # ── Plot C: NN ratio histogram ──
    ax_nn = fig.add_subplot(gs[0, 2])
    ax_nn.hist(nn_ratios, bins=50, color='steelblue', alpha=0.7, edgecolor='navy',
               density=True)
    ax_nn.axvline(PHI_PAASCH, color='red', linewidth=2, linestyle='--',
                  label=f'phi = {PHI_PAASCH}')
    ax_nn.axvline(np.sqrt(PHI_PAASCH), color='orange', linewidth=1, linestyle=':',
                  label=f'sqrt(phi) = {np.sqrt(PHI_PAASCH):.4f}')
    ax_nn.axvline(PHI_PAASCH**(1/3), color='green', linewidth=1, linestyle=':',
                  label=f'phi^(1/3) = {PHI_PAASCH**(1/3):.4f}')
    ax_nn.set_xlabel(r'$\lambda_{i+1}/\lambda_i$', fontsize=10)
    ax_nn.set_ylabel('Density', fontsize=10)
    ax_nn.set_title('C: Nearest-Neighbor Ratios (tau=0.19)', fontsize=10)
    ax_nn.legend(fontsize=7)

    # ── Plot D: Rayleigh p-values vs tau ──
    ax_ray = fig.add_subplot(gs[1, 0])
    p_vals = [results[tau]['p_rayleigh'] for tau in TAU_VALUES]
    p_vals_w = [results[tau]['p_rayleigh_weighted'] for tau in TAU_VALUES]

    ax_ray.semilogy(TAU_VALUES, p_vals, 'bo-', label='Unweighted', markersize=8)
    ax_ray.semilogy(TAU_VALUES, p_vals_w, 'rs-', label='PW-weighted', markersize=8)
    ax_ray.axhline(0.05, color='orange', linestyle='--', alpha=0.7, label='p=0.05')
    ax_ray.axhline(0.01, color='red', linestyle='--', alpha=0.7, label='p=0.01')
    ax_ray.set_xlabel('tau', fontsize=10)
    ax_ray.set_ylabel('Rayleigh p-value', fontsize=10)
    ax_ray.set_title('D: Rayleigh p-value vs tau', fontsize=10)
    ax_ray.legend(fontsize=8)
    ax_ray.set_xlim(-0.01, 0.20)

    # ── Plot E: All-pairs ratio histogram ──
    ax_allpairs = fig.add_subplot(gs[1, 1])

    # Compute all pairwise ratios (only unique, j > i)
    all_ratios = []
    for i in range(len(fold_vals)):
        for j in range(i+1, min(i+20, len(fold_vals))):  # limit to nearby neighbors
            all_ratios.append(fold_vals[j] / fold_vals[i])
    all_ratios = np.array(all_ratios)

    ax_allpairs.hist(all_ratios, bins=100, color='steelblue', alpha=0.7,
                     density=True, range=(1.0, 2.0))
    ax_allpairs.axvline(PHI_PAASCH, color='red', linewidth=2, linestyle='--',
                        label=f'phi = {PHI_PAASCH}')
    # Mark also the golden ratio and sqrt(2)
    ax_allpairs.axvline(1.61803, color='gold', linewidth=1, linestyle=':',
                        label=f'golden = 1.618')
    ax_allpairs.axvline(np.sqrt(2), color='purple', linewidth=1, linestyle=':',
                        label=f'sqrt(2) = {np.sqrt(2):.4f}')
    ax_allpairs.set_xlabel(r'$\lambda_j / \lambda_i$', fontsize=10)
    ax_allpairs.set_ylabel('Density', fontsize=10)
    ax_allpairs.set_title('E: Pairwise Ratios (nearby pairs, tau=0.19)', fontsize=10)
    ax_allpairs.legend(fontsize=7)

    # ── Plot F: Phase positions colored by (p,q) rep ──
    ax_rep = fig.add_subplot(gs[1, 2])

    # For each eigenvalue, we need to identify its (p,q) rep
    # We can reconstruct this from the s46 data
    if has_s46:
        rep_colors = {
            (0,0): 'red', (0,1): 'blue', (1,0): 'cyan',
            (0,2): 'green', (1,1): 'purple', (2,0): 'lime',
            (0,3): 'orange', (2,1): 'brown', (3,0): 'pink',
        }

        for (p, q) in sorted(rep_colors.keys()):
            key = f'evals_{p}_{q}'
            if key in d46:
                evals_pq = np.abs(d46[key])
                evals_pq_unique = np.unique(np.round(evals_pq, 10))
                if len(evals_pq_unique) > 0 and evals_pq_unique.min() > 0:
                    _, phases_pq, _ = spiral_mapping(evals_pq_unique)
                    # Use fold_vals.min() as reference
                    angles_pq = (1.0 / K_SPIRAL) * np.log(evals_pq_unique / fold_vals.min())
                    phases_pq = angles_pq % (2 * np.pi)
                    ax_rep.scatter(np.degrees(phases_pq), evals_pq_unique,
                                 c=rep_colors[(p,q)], s=15, alpha=0.6,
                                 label=f'({p},{q})')

        ax_rep.axhline(fold_vals.min(), color='gray', linestyle=':', alpha=0.3)
        ax_rep.set_xlabel('Phase (degrees)', fontsize=10)
        ax_rep.set_ylabel(r'$|\lambda|$', fontsize=10)
        ax_rep.set_title('F: Phase vs |lambda| by (p,q) rep', fontsize=10)
        ax_rep.legend(fontsize=6, ncol=3)
        ax_rep.set_xlim(0, 360)

    # ── Plot G: Harmonic Rayleigh significance across tau ──
    ax_harm = fig.add_subplot(gs[2, 0])
    harmonics = [1, 2, 3, 4, 6, 8]

    for h in harmonics:
        if h == 1:
            p_h_vals = [results[tau]['p_rayleigh'] for tau in TAU_VALUES]
        else:
            p_h_vals = [results[tau]['harmonic_results'][h][2] for tau in TAU_VALUES]
        ax_harm.semilogy(TAU_VALUES, p_h_vals, 'o-', markersize=6, label=f'h={h}')

    ax_harm.axhline(0.05, color='orange', linestyle='--', alpha=0.7)
    ax_harm.axhline(0.01, color='red', linestyle='--', alpha=0.7)
    ax_harm.set_xlabel('tau', fontsize=10)
    ax_harm.set_ylabel('p-value', fontsize=10)
    ax_harm.set_title('G: Harmonic Rayleigh p-values', fontsize=10)
    ax_harm.legend(fontsize=7, ncol=3)

    # ── Plot H: Eigenvalue strip with spiral annotation ──
    ax_strip = fig.add_subplot(gs[2, 1:])

    fold_vals_plot = results[0.19]['unique_vals']
    fold_degs_plot = results[0.19]['total_degs']
    fold_phases_plot = np.degrees(results[0.19]['phases'])

    sizes_strip = 3 + 20 * np.log1p(fold_degs_plot) / np.log1p(fold_degs_plot.max())
    scatter = ax_strip.scatter(fold_vals_plot, fold_phases_plot,
                               c=fold_phases_plot, cmap='hsv',
                               s=sizes_strip, alpha=0.7, edgecolors='k', linewidths=0.3)

    # Mark eigenvalues at integer turn multiples (phi^n of minimum)
    lam_min = fold_vals_plot.min()
    for n_turn in range(1, 3):
        lam_turn = lam_min * PHI_PAASCH**n_turn
        if lam_turn <= fold_vals_plot.max() * 1.1:
            ax_strip.axvline(lam_turn, color='red', linestyle='--', alpha=0.4,
                            label=f'phi^{n_turn}*lam_min = {lam_turn:.4f}' if n_turn <= 2 else '')

    ax_strip.axvline(lam_min, color='black', linestyle='-', alpha=0.3, label=f'lam_min = {lam_min:.4f}')

    # Mark phi=1.53158 ratio lines
    for base_idx in [0]:
        base = fold_vals_plot[base_idx]
        for power in range(1, 4):
            target = base * PHI_PAASCH**power
            if target <= fold_vals_plot.max():
                ax_strip.axvline(target, color='red', linestyle=':', alpha=0.2)

    ax_strip.set_xlabel(r'$|\lambda|$', fontsize=10)
    ax_strip.set_ylabel('Phase (degrees)', fontsize=10)
    ax_strip.set_title('H: Eigenvalue vs Spiral Phase (tau=0.19)', fontsize=10)
    ax_strip.legend(fontsize=7)
    plt.colorbar(scatter, ax=ax_strip, label='Phase (deg)')

    # ── Main title ──
    fig.suptitle(f'Paasch Spiral Analysis of Dirac Spectrum\n'
                 f'phi={PHI_PAASCH}, Gate: {verdict}, '
                 f'Rayleigh p={p_ray_fold:.3e}, '
                 f'{n_clusters_fold} clusters',
                 fontsize=13, fontweight='bold', y=0.98)

    plt.savefig(OUTPUT_PNG, dpi=200, bbox_inches='tight')
    print(f"Plot saved to {OUTPUT_PNG}")
    plt.close()

    # ──────────────────────────────────────────────────────────
    #  Summary
    # ──────────────────────────────────────────────────────────
    print(f"\n{'='*78}")
    print("SUMMARY")
    print(f"{'='*78}")
    print(f"\n  Gate: PAASCH-SPIRAL-47 = {verdict}")
    print(f"  Rayleigh (unweighted, fold): R_bar={fold_result['R_bar']:.6f}, p={p_ray_fold:.6e}")
    print(f"  Rayleigh (PW-weighted, fold): R_bar={fold_result['R_bar_weighted']:.6f}, p={fold_result['p_rayleigh_weighted']:.6e}")
    print(f"  KS test (fold): D={fold_result['ks_stat']:.6f}, p={fold_result['ks_p']:.6e}")
    print(f"  Clusters (2-sigma): {n_clusters_fold}")
    print(f"  Best harmonic: h={best_harmonic_h}, p={best_harmonic_p:.6e}")
    print(f"  Phi-ratio pairs: {n_pairs_obs} observed vs {n_pairs_exp:.1f}+/-{n_pairs_std:.1f} expected")
    print(f"  Spiral coverage: {np.log(fold_vals[-1]/fold_vals[0])/np.log(PHI_PAASCH):.2f} turns")
    print(f"  NN ratios near phi (1%): {nn_near_phi}/{len(nn_ratios)}")


if __name__ == '__main__':
    main()
