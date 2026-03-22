"""
Defect classification and census.

Classifies detected vortices into:
  - N_free: unpaired vortices (hydrogen/single baryons)
  - N_pair: bound vortex-antivortex pairs (deuterium)
  - N_triple: three-vortex bound states (He-3)
  - N_quad: four-vortex clusters (He-4)
  - N_complex: 7+ vortex clusters (Li-7)

The key ratio: D/H_sim = N_pair / N_free
Target: 2.527 x 10^-5

Phase 2: KD-tree clustering for O(n log n) scaling + soft pairing D/H.
"""

import numpy as np
from scipy.spatial import cKDTree
import scipy.sparse
import scipy.sparse.csgraph
from .vortex_detection import detect_vortices, identify_pairs


def cluster_vortices(vortex_positions, d_cluster, L=None):
    """Cluster nearby vortices using single-linkage clustering.

    Uses KD-tree + sparse distance matrix + connected components
    for O(n log n) scaling.

    Args:
        vortex_positions: list of (y, x, charge)
        d_cluster: clustering distance threshold
        L: box size for periodic BC

    Returns:
        clusters: list of lists, each containing (y, x, charge) tuples
    """
    if len(vortex_positions) == 0:
        return []

    positions = np.array([(y, x) for y, x, c in vortex_positions], dtype=float)
    n = len(positions)

    if n == 1:
        return [list(vortex_positions)]

    # Build KD-tree with periodic BC
    boxsize = [float(L), float(L)] if L is not None else None
    tree = cKDTree(positions, boxsize=boxsize)

    # Sparse distance matrix: only entries within d_cluster
    sparse_dist = tree.sparse_distance_matrix(tree, d_cluster, output_type='coo_matrix')

    # Connected components give cluster labels
    n_components, labels = scipy.sparse.csgraph.connected_components(
        sparse_dist, directed=False
    )

    # Group vortices by cluster label
    clusters = [[] for _ in range(n_components)]
    for idx, label in enumerate(labels):
        clusters[label].append(vortex_positions[idx])

    return clusters


def run_census(psi, d_pair, d_cluster=None, L=None,
               soft_pairing=False, n0=1.0, xi=1.0, H=0.0):
    """Run full defect census on a wavefunction snapshot.

    Args:
        psi: complex 2D wavefunction array
        d_pair: maximum pairing distance for vortex-antivortex pairs
        d_cluster: clustering distance for multi-vortex states (default: 2*d_pair)
        L: box size in grid units for periodic BC
        soft_pairing: if True, use continuous pair weights for D/H
        n0: background density (for soft pairing)
        xi: healing length in grid units (for soft pairing)
        H: Hubble rate (for soft pairing)

    Returns:
        dict with census results
    """
    if d_cluster is None:
        d_cluster = 2.0 * d_pair

    # Detect all vortices
    vortex_positions, winding_field = detect_vortices(psi)

    n_positive = sum(1 for _, _, c in vortex_positions if c > 0)
    n_negative = sum(1 for _, _, c in vortex_positions if c < 0)
    n_total = len(vortex_positions)

    # Pair identification
    if soft_pairing:
        pairs, free_pos, free_neg, pair_weights = identify_pairs(
            vortex_positions, d_pair, L=L,
            soft_pairing=True, n0=n0, xi=xi, H=H
        )
    else:
        pairs, free_pos, free_neg = identify_pairs(vortex_positions, d_pair, L=L)
        pair_weights = []

    n_pair = len(pairs)
    n_free = len(free_pos) + len(free_neg)

    # Cluster analysis for higher-order bound states
    clusters = cluster_vortices(vortex_positions, d_cluster, L=L)

    n_single = 0  # isolated vortices (cluster of 1)
    n_triple = 0  # 3-vortex clusters
    n_quad = 0    # 4-vortex clusters
    n_complex = 0 # 7+ vortex clusters (Li-7 analog)
    cluster_sizes = []

    for cl in clusters:
        size = len(cl)
        cluster_sizes.append(size)
        if size == 1:
            n_single += 1
        elif size == 3:
            n_triple += 1
        elif size == 4:
            n_quad += 1
        elif size >= 7:
            n_complex += 1

    # The key ratio
    if soft_pairing and pair_weights:
        # Continuous D/H: weighted pair count / (free + unweighted fraction)
        weighted_pairs = sum(pair_weights)
        unweighted_free = sum(1.0 - w for w in pair_weights)
        d_over_h = weighted_pairs / (n_free + unweighted_free) if (n_free + unweighted_free) > 0 else float('inf')
    else:
        d_over_h = n_pair / n_free if n_free > 0 else float('inf')

    result = {
        'n_total': n_total,
        'n_positive': n_positive,
        'n_negative': n_negative,
        'n_pair': n_pair,
        'n_free': n_free,
        'n_free_positive': len(free_pos),
        'n_free_negative': len(free_neg),
        'n_triple': n_triple,
        'n_quad': n_quad,
        'n_complex': n_complex,
        'd_over_h': d_over_h,
        'd_over_h_target': 2.527e-5,
        'vortex_positions': vortex_positions,
        'pairs': pairs,
        'clusters': clusters,
        'cluster_sizes': cluster_sizes,
    }

    if soft_pairing:
        result['pair_weights'] = pair_weights
        result['weighted_pairs'] = sum(pair_weights) if pair_weights else 0.0

    return result


def print_census(census):
    """Print a formatted census report."""
    print("=" * 60)
    print("DEFECT CENSUS")
    print("=" * 60)
    print(f"  Total vortices:     {census['n_total']}")
    print(f"    Positive (+1):    {census['n_positive']}")
    print(f"    Negative (-1):    {census['n_negative']}")
    print(f"  Bound pairs:        {census['n_pair']}  (deuterium analog)")
    print(f"  Free vortices:      {census['n_free']}  (hydrogen analog)")
    print(f"  3-vortex clusters:  {census['n_triple']}  (He-3 analog)")
    print(f"  4-vortex clusters:  {census['n_quad']}  (He-4 analog)")
    print(f"  7+ vortex clusters: {census['n_complex']}  (Li-7 analog)")
    if 'weighted_pairs' in census:
        print(f"  Weighted pairs:     {census['weighted_pairs']:.3f}  (soft pairing)")
    print("-" * 60)
    print(f"  D/H ratio:          {census['d_over_h']:.6e}")
    print(f"  D/H target:         {census['d_over_h_target']:.6e}")
    if census['d_over_h'] > 0 and census['d_over_h'] != float('inf'):
        ratio = census['d_over_h'] / census['d_over_h_target']
        print(f"  Ratio sim/target:   {ratio:.4f}")
    print("=" * 60)
