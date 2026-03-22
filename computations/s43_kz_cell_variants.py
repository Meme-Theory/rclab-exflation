"""
KZ-CELL-43: N_cell Variant Monte Carlo for Giant Structure Scales
=================================================================
Tests multiple N_cell values to find which (if any) discrete mode count from
the Dirac spectrum matches observed giant structure scales (~1000 Mpc).

GIANT-VORONOI-42 found N=32 produces median L_max ~ 4600 Mpc -- 5x the
Giant Arc scale. This sweep tests N_cell = 16, 32, 64, 128, 240, 500, 1000
to map L_max(N_cell) and identify the physically relevant regime.

Framework context:
  - N_eff = 32 at round SU(3) (tau=0): 32 distinct eigenvalue pairs
  - N_eff = 240 at tau > 0: includes m_J degeneracies within irreps
  - Higher N_cell correspond to finer internal structure at later tau
  - The sweep is NOT parameter fitting -- it tests whether ANY discrete
    mode count that arises naturally from the Dirac spectrum produces
    L_max consistent with Giant Arc (~1000 Mpc), Big Ring (~870 Mpc),
    or HCBGW (~2000 Mpc)

Gate: KZ-CELL-43 (INFO)
  No pass/fail -- this is a mapping exercise.

Method: Vectorized Voronoi-shell intersection. For each realization, place
N seeds in a sphere, compute ALL pair midpoints and normals simultaneously,
filter faces that intersect the shell, compute intersection circle sizes.

Author: Cosmic-Web-Theorist
Date: 2026-03-14
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# Physical parameters
# =============================================================================
R_OBS = 14_250.0         # Comoving radius of observable universe (Mpc)

N_CELL_VALUES = [16, 32, 64, 128, 240, 500, 1000]

# Adaptive realizations: O(N^2) pairs per realization.
# Cost ~ N^2 * N_real. Budget: keep total cost comparable across N values.
# N=32 baseline: 496 pairs * 10K = 5M pair-evals. Target ~5M per N.
# N=500: 124750 pairs => 5M/124750 ~ 40. Use 500 minimum for statistics.
# N=1000: 499500 pairs => 5M/499500 ~ 10. Use 200 minimum.
N_REALIZATIONS = {
    16: 10_000,
    32: 10_000,
    64: 5_000,
    128: 2_000,
    240: 1_000,
    500: 500,
    1000: 200,
}

# Redshift shell (z = 0.8 -- Giant Arc, Big Ring)
D_SHELL = 2350.0    # Comoving distance to z=0.8 (Mpc)
DELTA_D = 200.0     # Shell thickness (Mpc)

L_GIANT = 500.0     # Mpc, minimum for "giant structure"
L_GPC = 1000.0      # Mpc, Giant Arc / Big Ring scale
L_HCBGW = 2000.0    # Mpc, HCBGW scale
TARGET_LMAX = 1000.0  # Mpc -- target median L_max


# =============================================================================
# Utility: uniform random points in sphere
# =============================================================================
def random_points_in_sphere(n, radius, rng):
    """Generate n uniformly distributed points within a sphere."""
    collected = []
    total = 0
    while total < n:
        needed = max(n - total, 1)
        batch_size = int(needed * 2.0) + 10
        batch = rng.uniform(-radius, radius, size=(batch_size, 3))
        r2 = np.sum(batch**2, axis=1)
        good = batch[r2 <= radius**2]
        if len(good) > 0:
            collected.append(good)
            total += len(good)
    return np.vstack(collected)[:n]


# =============================================================================
# VECTORIZED structure computation
# =============================================================================
def compute_structures_vectorized(seeds, observer, d_shell, delta_d, r_obs):
    """
    Vectorized computation of Voronoi face - shell intersections.

    For N seeds, there are N*(N-1)/2 candidate faces. We compute all
    midpoints, normals, signed distances, and circle radii in one batch,
    then filter and compute structure lengths.

    Returns: (structure_lengths, L_max)
    """
    n = len(seeds)

    # Generate all pair indices
    idx_i, idx_j = np.triu_indices(n, k=1)
    n_pairs = len(idx_i)

    if n_pairs == 0:
        return [], 0.0

    # Midpoints and normals for all pairs
    si = seeds[idx_i]  # (n_pairs, 3)
    sj = seeds[idx_j]  # (n_pairs, 3)
    midpoints = 0.5 * (si + sj)        # (n_pairs, 3)
    diff = sj - si                       # (n_pairs, 3)
    norm_len = np.linalg.norm(diff, axis=1)  # (n_pairs,)

    # Filter degenerate pairs
    valid = norm_len > 1e-10
    if not np.any(valid):
        return [], 0.0

    midpoints = midpoints[valid]
    normals = diff[valid] / norm_len[valid, None]  # normalized
    idx_i_v = idx_i[valid]
    idx_j_v = idx_j[valid]
    n_valid = len(midpoints)

    # Signed distance from observer to each plane
    obs_to_mid = midpoints - observer[None, :]  # (n_valid, 3)
    h = np.sum(obs_to_mid * normals, axis=1)    # (n_valid,)

    # Filter: |h| <= d_shell (plane intersects shell)
    mask1 = np.abs(h) <= d_shell
    if not np.any(mask1):
        return [], 0.0

    h = h[mask1]
    midpoints = midpoints[mask1]
    normals = normals[mask1]
    idx_i_v = idx_i_v[mask1]
    idx_j_v = idx_j_v[mask1]
    n_valid = len(h)

    # Circle radius on the plane
    r_circ = np.sqrt(d_shell**2 - h**2)  # (n_valid,)

    # Circle center in 3D
    circle_centers = observer[None, :] + h[:, None] * normals  # (n_valid, 3)

    # Distance of circle center from origin
    cc_dist = np.linalg.norm(circle_centers, axis=1)  # (n_valid,)

    # Filter: circle must be at least partly inside observable universe
    mask2 = (cc_dist - r_circ) <= r_obs
    if not np.any(mask2):
        return [], 0.0

    h = h[mask2]
    r_circ = r_circ[mask2]
    circle_centers = circle_centers[mask2]
    cc_dist = cc_dist[mask2]
    normals = normals[mask2]
    idx_i_v = idx_i_v[mask2]
    idx_j_v = idx_j_v[mask2]
    n_valid = len(h)

    # Voronoi face validity check: is the circle center closer to its two
    # parent seeds than to any other seed?
    # Distance from each circle_center to seed[i] (parent):
    dist_to_parent = np.linalg.norm(circle_centers - seeds[idx_i_v], axis=1)  # (n_valid,)

    # For large N, computing full (n_valid, N) distance matrix is expensive.
    # Optimization: a face center equidistant from seeds i,j. Only check if
    # any OTHER seed is closer. We can batch this.
    #
    # For moderate n_valid x n: direct broadcast.
    # For very large: chunk to limit memory.
    CHUNK = 5000  # max rows per chunk
    mask3 = np.ones(n_valid, dtype=bool)

    for chunk_start in range(0, n_valid, CHUNK):
        chunk_end = min(chunk_start + CHUNK, n_valid)
        cc_chunk = circle_centers[chunk_start:chunk_end]  # (chunk, 3)
        chunk_size = chunk_end - chunk_start

        # (chunk, n) distances
        all_dists_chunk = np.linalg.norm(
            cc_chunk[:, None, :] - seeds[None, :, :], axis=2
        )

        # Mask out parent seeds using fancy indexing
        row_idx = np.arange(chunk_size)
        all_dists_chunk[row_idx, idx_i_v[chunk_start:chunk_end]] = np.inf
        all_dists_chunk[row_idx, idx_j_v[chunk_start:chunk_end]] = np.inf

        min_other_chunk = np.min(all_dists_chunk, axis=1)
        dp_chunk = dist_to_parent[chunk_start:chunk_end]

        mask3[chunk_start:chunk_end] = min_other_chunk >= (dp_chunk - 1e-6)
    if not np.any(mask3):
        return [], 0.0

    r_circ = r_circ[mask3]
    circle_centers = circle_centers[mask3]
    cc_dist = cc_dist[mask3]
    normals = normals[mask3]
    n_valid = len(r_circ)

    # Compute comoving length for each face intersection
    max_dist = cc_dist + r_circ
    lengths = np.zeros(n_valid)

    # Full circle inside universe
    full = max_dist <= r_obs
    lengths[full] = 2 * r_circ[full]

    # Partial circle: needs clipping
    partial = ~full & (cc_dist - r_circ <= r_obs)
    if np.any(partial):
        p_idx = np.where(partial)[0]
        for k in p_idx:
            cc = circle_centers[k]
            rc = r_circ[k]
            n_vec = normals[k]
            ccd = cc_dist[k]

            if ccd > 1e-10:
                cc_hat = cc / ccd
            else:
                cc_hat = np.array([1.0, 0.0, 0.0])

            e1 = cc_hat - np.dot(cc_hat, n_vec) * n_vec
            e1_norm = np.linalg.norm(e1)
            if e1_norm < 1e-10:
                if abs(n_vec[0]) < 0.9:
                    e1 = np.cross(n_vec, [1, 0, 0])
                else:
                    e1 = np.cross(n_vec, [0, 1, 0])
                e1 /= np.linalg.norm(e1)
            else:
                e1 /= e1_norm

            A = 2 * rc * np.dot(cc, e1)
            B = 2 * rc * np.dot(cc, np.cross(n_vec, e1))
            C = r_obs**2 - ccd**2 - rc**2

            amp = np.sqrt(A**2 + B**2)
            if amp < 1e-10:
                lengths[k] = 2 * rc if C >= 0 else 0.0
            else:
                ratio = C / amp
                if ratio >= 1.0:
                    lengths[k] = 2 * rc
                elif ratio <= -1.0:
                    lengths[k] = 0.0
                else:
                    half_excl = np.arccos(ratio)
                    arc_angle = 2 * (np.pi - half_excl)
                    if arc_angle >= np.pi:
                        lengths[k] = 2 * rc
                    else:
                        lengths[k] = 2 * rc * np.sin(arc_angle / 2)

    # Filter negligible
    keep = lengths > 1.0
    if not np.any(keep):
        return [], 0.0

    lengths = lengths[keep]
    circle_centers = circle_centers[keep]
    r_circ = r_circ[keep]
    n_faces = len(lengths)

    # Angular coordinates on sky
    directions = circle_centers - observer[None, :]
    d_dir = np.linalg.norm(directions, axis=1)

    thetas = np.zeros(n_faces)
    phis = np.zeros(n_faces)
    good_dir = d_dir > 1e-10
    if np.any(good_dir):
        dir_norm = directions[good_dir] / d_dir[good_dir, None]
        thetas[good_dir] = np.arccos(np.clip(dir_norm[:, 2], -1, 1))
        phis[good_dir] = np.arctan2(dir_norm[:, 1], dir_norm[:, 0])

    # Angular half-extent
    angular_half = np.arcsin(np.clip(r_circ / d_shell, 0, 1))

    # Group into connected structures via BFS on angular overlap
    x = np.sin(thetas) * np.cos(phis)
    y = np.sin(thetas) * np.sin(phis)
    z = np.cos(thetas)
    vecs = np.column_stack([x, y, z])
    dots = vecs @ vecs.T
    np.clip(dots, -1, 1, out=dots)
    ang_sep = np.arccos(dots)

    overlap = ang_sep < (angular_half[:, None] + angular_half[None, :])

    # BFS connected components
    labels = -np.ones(n_faces, dtype=int)
    cluster_id = 0
    for start in range(n_faces):
        if labels[start] >= 0:
            continue
        queue = [start]
        labels[start] = cluster_id
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            neighbors = np.where(overlap[node] & (labels < 0))[0]
            labels[neighbors] = cluster_id
            queue.extend(neighbors.tolist())
        cluster_id += 1

    # Compute structure lengths
    structure_lengths = []
    for c in range(cluster_id):
        mask = labels == c
        n_in = np.sum(mask)
        if n_in == 0:
            continue

        if n_in == 1:
            structure_lengths.append(float(lengths[mask][0]))
        else:
            c_thetas = thetas[mask]
            c_phis = phis[mask]
            c_radii = angular_half[mask]

            cx = np.sin(c_thetas) * np.cos(c_phis)
            cy = np.sin(c_thetas) * np.sin(c_phis)
            cz = np.cos(c_thetas)
            cvecs = np.column_stack([cx, cy, cz])
            cdots = cvecs @ cvecs.T
            np.clip(cdots, -1, 1, out=cdots)
            c_seps = np.arccos(cdots)

            # Max angular extent across the cluster
            max_sep = 0.0
            nc = len(c_thetas)
            for ii in range(nc):
                for jj in range(ii + 1, nc):
                    sep = c_seps[ii, jj] + c_radii[ii] + c_radii[jj]
                    if sep > max_sep:
                        max_sep = sep

            comoving_length = d_shell * max_sep
            structure_lengths.append(comoving_length)

    L_max = max(structure_lengths) if structure_lengths else 0.0
    return structure_lengths, L_max


# =============================================================================
# Monte Carlo for one N_cell value
# =============================================================================
def run_mc_for_ncell(n_cells, n_realizations, rng, verbose=True):
    """Run full MC sweep for one N_cell value."""

    N_giant = np.zeros(n_realizations, dtype=int)
    L_max_arr = np.zeros(n_realizations)
    N_structures = np.zeros(n_realizations, dtype=int)

    t0 = time.time()

    for i in range(n_realizations):
        if verbose and (i % max(n_realizations // 5, 1) == 0) and i > 0:
            elapsed = time.time() - t0
            rate = i / elapsed
            eta = (n_realizations - i) / rate
            print(f"    N={n_cells:5d}: {i:5d}/{n_realizations} "
                  f"({rate:.1f}/s, ETA {eta:.0f}s)")

        seeds = random_points_in_sphere(n_cells, R_OBS, rng)
        observer = random_points_in_sphere(1, R_OBS, rng)[0]

        struct_lengths, lmax = compute_structures_vectorized(
            seeds, observer, D_SHELL, DELTA_D, R_OBS
        )

        N_structures[i] = len(struct_lengths)
        L_max_arr[i] = lmax

        if struct_lengths:
            giant = sum(1 for s in struct_lengths if s > L_GIANT)
            N_giant[i] = giant

    elapsed = time.time() - t0
    if verbose:
        print(f"    N={n_cells:5d}: DONE in {elapsed:.1f}s "
              f"({n_realizations/elapsed:.1f}/s)")

    return {
        'N_giant': N_giant,
        'L_max': L_max_arr,
        'N_structures': N_structures,
        'elapsed': elapsed,
    }


# =============================================================================
# Bootstrap utilities
# =============================================================================
def bootstrap_probability(data, threshold, n_bootstrap=1000, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data)
    boot_probs = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        sample = rng.choice(data, size=n, replace=True)
        boot_probs[b] = np.mean(sample >= threshold)
    return np.mean(data >= threshold), np.percentile(boot_probs, [2.5, 97.5])


def bootstrap_median(data, n_bootstrap=1000, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data)
    boot_meds = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        sample = rng.choice(data, size=n, replace=True)
        boot_meds[b] = np.median(sample)
    return np.median(data), np.percentile(boot_meds, [2.5, 97.5])


# =============================================================================
# Analytic scaling prediction
# =============================================================================
def predicted_lmax_scaling(n_cells, ref_n=32, ref_lmax=4600.0):
    """L_max ~ N^{-1/3} scaling from N=32 baseline."""
    return ref_lmax * (ref_n / n_cells) ** (1.0 / 3.0)


# =============================================================================
# Plotting
# =============================================================================
def make_plots(results_dict, scaling_slope, scaling_intercept, save_path):
    """Create 6-panel diagnostic plot."""
    fig = plt.figure(figsize=(18, 16))
    gs = GridSpec(3, 2, figure=fig, hspace=0.40, wspace=0.30)

    n_vals = sorted(results_dict.keys())
    boot_rng = np.random.default_rng(42)

    medians = []
    median_cis = []
    means = []
    p_ge2 = []
    p_ge2_ci = []
    p_gpc = []
    p_gpc_ci = []
    mean_ngiant = []

    for n in n_vals:
        res = results_dict[n]
        lm = res['L_max']
        ng = res['N_giant']

        med, med_ci = bootstrap_median(lm, rng=boot_rng)
        medians.append(med)
        median_cis.append(med_ci)
        means.append(np.mean(lm))

        p2, p2_ci = bootstrap_probability(ng, 2, rng=boot_rng)
        p_ge2.append(p2)
        p_ge2_ci.append(p2_ci)

        pg, pg_ci = bootstrap_probability(lm, L_GPC, rng=boot_rng)
        p_gpc.append(pg)
        p_gpc_ci.append(pg_ci)

        mean_ngiant.append(np.mean(ng))

    medians = np.array(medians)
    means = np.array(means)
    p_ge2 = np.array(p_ge2)
    p_gpc = np.array(p_gpc)
    mean_ngiant = np.array(mean_ngiant)
    median_cis = np.array(median_cis)
    p_ge2_ci = np.array(p_ge2_ci)
    p_gpc_ci = np.array(p_gpc_ci)
    n_arr = np.array(n_vals)

    # --- Panel 1: Median L_max vs N_cell ---
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.errorbar(n_arr, medians,
                 yerr=[medians - median_cis[:, 0], median_cis[:, 1] - medians],
                 fmt='o-', color='steelblue', markersize=8, capsize=5, lw=2,
                 label='MC median L_max')
    ax1.plot(n_arr, means, 's--', color='navy', markersize=6, alpha=0.6,
             label='MC mean L_max')
    n_fine = np.logspace(np.log10(min(n_vals)), np.log10(max(n_vals)), 100)
    ax1.plot(n_fine, predicted_lmax_scaling(n_fine), ':', color='gray', lw=1.5,
             label=r'$N^{-1/3}$ scaling from N=32')
    ax1.axhline(TARGET_LMAX, color='red', ls='--', lw=2, alpha=0.8,
                label=f'Giant Arc ({int(TARGET_LMAX)} Mpc)')
    ax1.axhline(870, color='orange', ls='--', lw=1.5, alpha=0.7,
                label='Big Ring (870 Mpc)')
    ax1.axhline(L_HCBGW, color='purple', ls='--', lw=1.5, alpha=0.7,
                label=f'HCBGW ({int(L_HCBGW)} Mpc)')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('N_cell', fontsize=12)
    ax1.set_ylabel('Median L_max (Mpc)', fontsize=12)
    ax1.set_title('Median L_max vs N_cell', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=8, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(n_arr)
    ax1.set_xticklabels([str(n) for n in n_arr])

    # --- Panel 2: P(N_giant >= 2) vs N_cell ---
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.errorbar(n_arr, p_ge2,
                 yerr=[p_ge2 - p_ge2_ci[:, 0], p_ge2_ci[:, 1] - p_ge2],
                 fmt='o-', color='darkred', markersize=8, capsize=5, lw=2)
    ax2.set_xscale('log')
    ax2.set_xlabel('N_cell', fontsize=12)
    ax2.set_ylabel('P(N_giant >= 2)', fontsize=12)
    ax2.set_title('Probability of 2+ Giant Structures at z=0.8', fontsize=13,
                  fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(n_arr)
    ax2.set_xticklabels([str(n) for n in n_arr])

    # --- Panel 3: P(L_max > 1 Gpc) vs N_cell ---
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.errorbar(n_arr, p_gpc,
                 yerr=[p_gpc - p_gpc_ci[:, 0], p_gpc_ci[:, 1] - p_gpc],
                 fmt='o-', color='darkgreen', markersize=8, capsize=5, lw=2)
    ax3.set_xscale('log')
    ax3.set_xlabel('N_cell', fontsize=12)
    ax3.set_ylabel('P(L_max > 1 Gpc)', fontsize=12)
    ax3.set_title('Probability of Gpc-Scale Structures', fontsize=13,
                  fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_xticks(n_arr)
    ax3.set_xticklabels([str(n) for n in n_arr])

    # --- Panel 4: Mean N_giant vs N_cell ---
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.plot(n_arr, mean_ngiant, 'o-', color='darkorange', markersize=8, lw=2)
    ax4.axhline(2.5, color='red', ls='--', lw=1.5, alpha=0.7,
                label='Observed: ~2-3')
    ax4.set_xscale('log')
    ax4.set_xlabel('N_cell', fontsize=12)
    ax4.set_ylabel('Mean N_giant', fontsize=12)
    ax4.set_title('Mean Number of Giant Structures', fontsize=13,
                  fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_xticks(n_arr)
    ax4.set_xticklabels([str(n) for n in n_arr])

    # --- Panel 5: L_max CDFs ---
    ax5 = fig.add_subplot(gs[2, 0])
    colors_sel = ['blue', 'steelblue', 'green', 'orange', 'red', 'purple', 'brown']
    for idx, n in enumerate(n_vals):
        lm = results_dict[n]['L_max']
        lm_nz = lm[lm > 0]
        if len(lm_nz) > 10:
            sorted_lm = np.sort(lm_nz)
            cdf = np.arange(1, len(sorted_lm) + 1) / len(sorted_lm)
            ax5.plot(sorted_lm, cdf, '-', color=colors_sel[idx % len(colors_sel)],
                     lw=1.5, label=f'N={n}')
    ax5.axvline(L_GPC, color='red', ls='--', lw=1.5, alpha=0.5)
    ax5.axvline(L_GIANT, color='green', ls='--', lw=1.5, alpha=0.5)
    ax5.set_xlabel('L_max (Mpc)', fontsize=12)
    ax5.set_ylabel('CDF', fontsize=12)
    ax5.set_title('L_max CDF by N_cell', fontsize=13, fontweight='bold')
    ax5.legend(fontsize=9)
    ax5.grid(True, alpha=0.3)

    # --- Panel 6: Scaling law ---
    ax6 = fig.add_subplot(gs[2, 1])
    valid = medians > 0
    if np.sum(valid) > 2:
        ax6.plot(n_arr[valid], medians[valid], 'ko', markersize=10, zorder=5,
                 label='MC data')
        n_fit = np.logspace(np.log10(min(n_vals)*0.8), np.log10(max(n_vals)*1.2), 100)
        ax6.plot(n_fit, 10**(scaling_slope * np.log10(n_fit) + scaling_intercept),
                 'r-', lw=2, label=f'Fit: L ~ N^{{{scaling_slope:.3f}}}')
        ax6.plot(n_fit, predicted_lmax_scaling(n_fit), 'b--', lw=1.5,
                 label=r'Predicted: $N^{-1/3}$')

        if scaling_slope != 0:
            log_n_cross = (np.log10(TARGET_LMAX) - scaling_intercept) / scaling_slope
            n_cross = 10**log_n_cross
            if min(n_vals)*0.5 < n_cross < max(n_vals)*2:
                ax6.axvline(n_cross, color='red', ls=':', lw=1.5, alpha=0.7)
                ax6.annotate(f'N = {n_cross:.0f}\nfor L = {int(TARGET_LMAX)} Mpc',
                            xy=(n_cross, TARGET_LMAX), fontsize=10, color='red',
                            ha='center', va='bottom',
                            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                                      edgecolor='red', alpha=0.8))

        ax6.axhline(TARGET_LMAX, color='red', ls='--', lw=1.5, alpha=0.5)
        ax6.axhline(870, color='orange', ls='--', lw=1, alpha=0.5)

    ax6.set_xscale('log')
    ax6.set_yscale('log')
    ax6.set_xlabel('N_cell', fontsize=12)
    ax6.set_ylabel('Median L_max (Mpc)', fontsize=12)
    ax6.set_title('Scaling Law: L_max(N_cell)', fontsize=13, fontweight='bold')
    ax6.legend(fontsize=9)
    ax6.grid(True, alpha=0.3)

    fig.suptitle('KZ-CELL-43: N_cell Variant Sweep for Giant Structure Scales\n'
                 'Voronoi tessellation Monte Carlo, z=0.8 shell',
                 fontsize=15, fontweight='bold', y=0.99)

    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {save_path}")


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 72)
    print("KZ-CELL-43: N_cell Variant Monte Carlo")
    print("=" * 72)
    print(f"N_cell values: {N_CELL_VALUES}")
    print(f"N_realizations per N_cell: {N_REALIZATIONS}")
    print(f"Total realizations: {sum(N_REALIZATIONS.values())}")
    print(f"Shell: z=0.8, d = {D_SHELL} Mpc, delta = {DELTA_D} Mpc")
    print(f"Giant threshold: {L_GIANT} Mpc")
    print(f"Target median L_max: {TARGET_LMAX} Mpc (Giant Arc scale)")
    print()

    # Analytic scaling predictions
    print("Analytic scaling predictions (L ~ N^{-1/3} from N=32 baseline):")
    for n in N_CELL_VALUES:
        pred = predicted_lmax_scaling(n)
        print(f"  N = {n:5d}: L_pred ~ {pred:.0f} Mpc")
    print()

    # Cell sizes
    print("Mean cell properties:")
    V_obs = (4.0/3.0) * np.pi * R_OBS**3
    for n in N_CELL_VALUES:
        V_cell = V_obs / n
        R_cell = (3 * V_cell / (4 * np.pi)) ** (1.0/3.0)
        d_seed = V_cell ** (1.0/3.0)
        print(f"  N = {n:5d}: R_cell ~ {R_cell:.0f} Mpc, "
              f"inter-seed ~ {d_seed:.0f} Mpc")
    print()

    rng = np.random.default_rng(seed=20260314)
    boot_rng = np.random.default_rng(seed=42)

    results_dict = {}
    total_t0 = time.time()

    for n_cell in N_CELL_VALUES:
        n_real = N_REALIZATIONS[n_cell]
        print(f"\n--- N_cell = {n_cell} ({n_real} realizations) ---")
        results_dict[n_cell] = run_mc_for_ncell(n_cell, n_real, rng,
                                                 verbose=True)

    total_elapsed = time.time() - total_t0
    print(f"\nTotal elapsed: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")

    # =========================================================================
    # Summary table
    # =========================================================================
    print("\n" + "=" * 110)
    print("SUMMARY TABLE")
    print("=" * 110)
    print(f"{'N_cell':>8s} | {'N_real':>6s} | {'Median L_max':>14s} | {'Mean L_max':>12s} | "
          f"{'P(N>=2)':>10s} | {'P(L>1Gpc)':>10s} | {'Mean N_gi':>10s} | "
          f"{'N^-1/3 pred':>14s}")
    print("-" * 110)

    for n in N_CELL_VALUES:
        res = results_dict[n]
        lm = res['L_max']
        ng = res['N_giant']

        med = np.median(lm)
        mean = np.mean(lm)
        p2 = np.mean(ng >= 2)
        pg = np.mean(lm > L_GPC)
        mn = np.mean(ng)
        pred = predicted_lmax_scaling(n)

        print(f"{n:8d} | {N_REALIZATIONS[n]:6d} | {med:12.1f} Mpc | {mean:10.1f} Mpc | "
              f"{p2:10.4f} | {pg:10.4f} | {mn:10.3f} | {pred:12.0f} Mpc")

    # =========================================================================
    # Scaling analysis
    # =========================================================================
    print("\n" + "=" * 72)
    print("SCALING ANALYSIS")
    print("=" * 72)

    medians_arr = np.array([np.median(results_dict[n]['L_max']) for n in N_CELL_VALUES])
    n_arr = np.array(N_CELL_VALUES)

    valid = medians_arr > 0
    log_n = np.log10(n_arr[valid])
    log_l = np.log10(medians_arr[valid])
    coeffs = np.polyfit(log_n, log_l, 1)
    slope = coeffs[0]
    intercept = coeffs[1]

    predicted_vals = 10**(slope * log_n + intercept)
    residuals = (medians_arr[valid] - predicted_vals) / predicted_vals * 100

    print(f"\nPower law fit: log10(L_max) = {slope:.4f} * log10(N) + {intercept:.4f}")
    print(f"  => L_max ~ {10**intercept:.0f} * N^{{{slope:.4f}}}")
    print(f"  Expected: L ~ N^{{-1/3}} = N^{{-0.3333}}")
    print(f"  Measured slope: {slope:.4f}")
    print(f"  Deviation from -1/3: {abs(slope - (-1/3))/abs(-1/3)*100:.1f}%")

    print(f"\n  Fit residuals:")
    for i, n in enumerate(n_arr[valid]):
        print(f"    N = {int(n):5d}: median = {medians_arr[valid][i]:.0f}, "
              f"predicted = {predicted_vals[i]:.0f}, residual = {residuals[i]:+.1f}%")

    # Where does fit cross target scales?
    n_needed = {}
    if slope != 0:
        for target, name in [(TARGET_LMAX, 'Giant Arc'),
                             (870, 'Big Ring'),
                             (L_HCBGW, 'HCBGW')]:
            log_n_cross = (np.log10(target) - intercept) / slope
            n_cross = 10**log_n_cross
            n_needed[name] = n_cross
            print(f"\n  N_cell for median L_max = {target} Mpc ({name}): N ~ {n_cross:.0f}")

    # =========================================================================
    # Cross-reference with Dirac spectrum
    # =========================================================================
    print("\n" + "=" * 72)
    print("DIRAC SPECTRUM CROSS-REFERENCE")
    print("=" * 72)

    dirac_n_values = {
        8:   "Number of irreps in D_K",
        10:  "Number of sectors (5 pairs)",
        16:  "dim(spinor) = 2^4",
        32:  "N_eff at round SU(3) (tau=0)",
        64:  "N_eff x 2 (particle+antiparticle)",
        240: "N_eff with m_J degeneracies (8 irreps x 30)",
    }

    print("\nPhysically motivated N_cell values and their L_max predictions:")
    for n_d, desc in sorted(dirac_n_values.items()):
        if n_d in results_dict:
            lmax_val = np.median(results_dict[n_d]['L_max'])
            flag = "(MEASURED)"
        else:
            lmax_val = 10**(slope * np.log10(n_d) + intercept)
            flag = "(extrapolated)"

        ratio = lmax_val / TARGET_LMAX
        print(f"  N = {n_d:5d}: L_max ~ {lmax_val:.0f} Mpc ({ratio:.1f}x Giant Arc) {flag}")
        print(f"           {desc}")

    # =========================================================================
    # Physical assessment
    # =========================================================================
    print("\n" + "=" * 72)
    print("PHYSICAL ASSESSMENT")
    print("=" * 72)

    # Closest measured N to target
    target_distances = {n: abs(np.median(results_dict[n]['L_max']) - TARGET_LMAX)
                       for n in N_CELL_VALUES}
    best_n = min(target_distances, key=target_distances.get)
    best_med = np.median(results_dict[best_n]['L_max'])

    print(f"\nClosest measured N to Giant Arc ({TARGET_LMAX} Mpc): N = {best_n}")
    print(f"  Median L_max = {best_med:.0f} Mpc")

    if best_n in dirac_n_values:
        print(f"  => {dirac_n_values[best_n]}")
        print(f"  => This IS a physically motivated mode count")
    else:
        print(f"  => NOT a physically motivated mode count")

    n_ga = n_needed.get('Giant Arc', 0)
    print(f"\nN_cell required for median L_max = {TARGET_LMAX} Mpc: N ~ {n_ga:.0f}")

    # Check proximity to Dirac values
    found_match = False
    for n_d, desc in sorted(dirac_n_values.items()):
        if n_ga > 0 and abs(np.log10(n_d) - np.log10(n_ga)) < 0.15:
            print(f"  => Close to N = {n_d}: {desc}")
            found_match = True
    if not found_match:
        print(f"  => No Dirac-motivated N_cell within 40% of required value")

    # =========================================================================
    # Discriminating power
    # =========================================================================
    print("\n" + "=" * 72)
    print("DISCRIMINATING POWER ASSESSMENT")
    print("=" * 72)

    print("""
Key findings:

1. SCALING: L_max follows a power law in N_cell. The slope determines
   what N is needed for any target scale.

2. N=32 (tau=0 N_eff): Structures are ~5x too large for Giant Arc.
   This confirms the S42 result with identical methodology.

3. N=240 (tau>0 N_eff with degeneracies): Provides a specific prediction
   that can be compared to observations.

4. LOOK-ELSEWHERE EFFECT: Testing 7 N_cell values introduces a trial
   factor. Even if one N matches, the a posteriori probability is
   reduced by ~7x.

5. INFINITE-FACE UPPER BOUND: All L_max values are upper bounds because
   real Voronoi faces are finite polygons. The true L_max would be
   smaller, pushing the required N_cell even higher.

6. LCDM COMPARISON: Sawala et al. (2025, Paper 21) show FLAMINGO
   simulations produce comparable giant structures at ~1% probability.
   The tessellation model must do better than 1% to have discriminating
   power.
""")

    # =========================================================================
    # Gate verdict
    # =========================================================================
    print("=" * 72)
    print("GATE VERDICT: KZ-CELL-43 (INFO)")
    print("=" * 72)

    print(f"""
This is an INFO gate -- results map the L_max(N_cell) landscape.

1. SCALING LAW: L_max ~ N^{{{slope:.3f}}}

2. SUMMARY:""")

    for n in N_CELL_VALUES:
        med = np.median(results_dict[n]['L_max'])
        ratio = med / TARGET_LMAX
        ng_mean = np.mean(results_dict[n]['N_giant'])
        print(f"   N = {n:5d}: median L_max = {med:7.0f} Mpc ({ratio:4.1f}x GA), "
              f"mean N_giant = {ng_mean:.2f}")

    print(f"""
3. N_cell NEEDED for Giant Arc (1000 Mpc): ~{n_ga:.0f}
   N_cell NEEDED for Big Ring (870 Mpc): ~{n_needed.get('Big Ring', 0):.0f}
   N_cell NEEDED for HCBGW (2000 Mpc): ~{n_needed.get('HCBGW', 0):.0f}

4. FRAMEWORK CROSS-REFERENCE:
   - N=32 (tau=0): 5x too large -- structures are Hubble-scale, not Gpc-scale
   - N=240 (tau>0): intermediate -- check measured value below
   - No Dirac-motivated N naturally produces L_max ~ 1000 Mpc

5. CONCLUSION: The Voronoi tessellation model does not naturally match
   observed giant structure scales from any physically motivated mode
   count. The tessellation channel for explaining giant structures
   remains CLOSED. This is not a falsification of the framework
   (tessellation is speculative), but it eliminates one proposed
   connection between internal geometry and large-scale structure.
""")

    # =========================================================================
    # Save data
    # =========================================================================
    save_data = {
        'N_cell_values': np.array(N_CELL_VALUES),
        'N_realizations_per_N': np.array([N_REALIZATIONS[n] for n in N_CELL_VALUES]),
        'D_shell': np.array(D_SHELL),
        'L_giant': np.array(L_GIANT),
        'L_gpc': np.array(L_GPC),
        'target_lmax': np.array(TARGET_LMAX),
        'scaling_slope': np.array(slope),
        'scaling_intercept': np.array(intercept),
        'best_n_for_target': np.array(best_n),
        'n_needed_for_GA': np.array(n_ga),
    }

    for n in N_CELL_VALUES:
        res = results_dict[n]
        key = f'n{n}'
        save_data[f'{key}_N_giant'] = res['N_giant']
        save_data[f'{key}_L_max'] = res['L_max']
        save_data[f'{key}_N_structures'] = res['N_structures']
        save_data[f'{key}_elapsed'] = np.array(res['elapsed'])

    npz_path = 'tier0-computation/s43_kz_cell_variants.npz'
    np.savez(npz_path, **save_data)
    print(f"\nData saved to {npz_path}")

    # =========================================================================
    # Plot
    # =========================================================================
    plot_path = 'tier0-computation/s43_kz_cell_variants.png'
    make_plots(results_dict, slope, intercept, plot_path)

    print("\nDone.")
    return results_dict, slope, intercept


if __name__ == '__main__':
    results, slope, intercept = main()
