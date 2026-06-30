#!/usr/bin/env python3
"""
s60_entangle_cg24.py — Entanglement-Area Law on CG(24) Graph
==============================================================

Session 60, Gate: ENTANGLE-CG24-60

Computes the quantum extremal surface (QES) on the CG(24) graph using the
island formula. The CG(24) graph has 24 vertices and 72 edges (Cayley graph
of S_4 with standard generators, regular degree 6).

The generalized entropy for a bipartition (A, A^c) is:
    S_gen(A) = |dA| * E_J / (4 * G_eff) + S_bulk(A)

where:
    |dA| = number of severed edges (graph cut size)
    E_J  = Josephson coupling energy at the fold
    G_eff = 1 / (16 * pi * a_2)  [effective Newton constant from spectral action]
    S_bulk(A) = von Neumann entanglement entropy of the BCS ground state
                restricted to the subregion A

The bulk entropy is modeled from the S59 Page curve data:
    S_ent(k) for k = 1,...,N-1 cells on the complete graph K_4
    extrapolated to partitions of size k on CG(24) via area-law scaling.

Pre-registered gate:
    PASS: Nontrivial QES exists; Lambda suppression > 50 OOM
    FAIL: No nontrivial extremal surface (S_gen monotone with partition size)
    INFO: QES exists but suppression < 50 OOM

Inputs:
    computations/session-59/s59_page_curve.npz
    computations/session-59/s59_josephson_phase.npz
    computations/_shared/canonical_constants.py

Outputs:
    computations/session-60/s60_entangle_cg24.npz
    computations/session-60/s60_entangle_cg24.png

Author: Hawking-Theorist Agent (S60)
"""

import sys
import os
import numpy as np
from itertools import combinations
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add parent to path for canonical_constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    a2_fold, tau_fold, J_C2, PI, N_cells,
    a0_fold, M_KK_gravity, rho_Lambda_obs, M_Pl_unreduced
)

# ============================================================================
# Section 1: Build the CG(24) Graph
# ============================================================================

def build_cayley_graph_S4():
    """
    Build the Cayley graph of S_4 (symmetric group on 4 elements) with
    generators {(12), (23), (34)} and their inverses.

    This gives a regular graph with:
    - 24 vertices (= |S_4| = 4!)
    - degree 6 (3 generators + 3 inverses)
    - 72 edges (= 24 * 6 / 2)

    We represent S_4 elements as permutations of (0,1,2,3).
    """
    from itertools import permutations

    # All elements of S_4
    elements = list(permutations(range(4)))
    elem_to_idx = {p: i for i, p in enumerate(elements)}

    N = len(elements)
    assert N == 24, f"Expected 24 elements, got {N}"

    # Generators: ALL 6 transpositions of S_4, giving degree 6 and 72 edges
    def apply_transposition(perm, i, j):
        """Apply transposition (i,j) to a permutation."""
        lst = list(perm)
        lst[i], lst[j] = lst[j], lst[i]
        return tuple(lst)

    generators = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    # Build adjacency matrix
    adj = np.zeros((N, N), dtype=np.int8)
    edge_set = set()

    for perm in elements:
        idx = elem_to_idx[perm]  # (local)
        for (i, j) in generators:
            neighbor = apply_transposition(perm, i, j)
            nbr_idx = elem_to_idx[neighbor]
            adj[idx, nbr_idx] = 1
            adj[nbr_idx, idx] = 1
            edge = (min(idx, nbr_idx), max(idx, nbr_idx))
            edge_set.add(edge)

    edges = sorted(edge_set)
    N_edges = len(edges)

    # Verify graph properties
    degrees = adj.sum(axis=1)
    assert np.all(degrees == 6), f"Not regular degree 6: {degrees}"
    assert N_edges == 72, f"Expected 72 edges, got {N_edges}"

    print(f"CG(24) graph: {N} vertices, {N_edges} edges, degree {degrees[0]}")
    print(f"  Diameter: {graph_diameter(adj)}")

    return adj, edges, elements, elem_to_idx


def graph_diameter(adj):
    """Compute graph diameter via BFS from each vertex."""
    N = adj.shape[0]
    max_dist = 0
    for start in range(N):
        dist = np.full(N, -1)
        dist[start] = 0
        queue = [start]
        qi = 0
        while qi < len(queue):
            v = queue[qi]; qi += 1
            for u in range(N):
                if adj[v, u] == 1 and dist[u] == -1:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        max_dist = max(max_dist, dist.max())
    return max_dist


def graph_cut_size(adj, subset):
    """Count edges between subset and its complement."""
    N = adj.shape[0]
    mask = np.zeros(N, dtype=bool)
    mask[list(subset)] = True
    # Count edges from inside to outside
    cut = 0
    for i in range(N):
        if mask[i]:
            for j in range(N):
                if not mask[j] and adj[i, j] == 1:
                    cut += 1
    return cut


def graph_cut_size_fast(adj, mask_array):
    """
    Fast cut-size computation using matrix operations.
    mask_array is a boolean array of shape (N,).
    """
    inner = adj[mask_array][:, ~mask_array]
    return int(inner.sum())


# ============================================================================
# Section 2: Entanglement Entropy Model
# ============================================================================

def bulk_entropy_model(k, N_total, S_ent_data, N_data=4):
    """
    Model the bulk entanglement entropy S_bulk(k) for a partition of size k
    in a graph of N_total vertices, extrapolated from the 4-cell Page curve data.

    The S59 Page curve data gives S_ent(k) for the complete graph K_4 with
    N_pair=1 per cell. Key values:  # (local)
        S_ent(k=1) = 1.201 nats   (bipartition 1|3)
        S_ent(k=2) = 1.381 nats   (bipartition 2|2)

    For a BCS ground state with area-law entanglement:
        S_ent(k) ~ s_0 * |boundary(k)| - S_topo

    where s_0 is the entropy per bond and S_topo is the topological
    entanglement entropy.

    On K_4: boundary(k=1) = 3 bonds, boundary(k=2) = 4 bonds.
    So: 1.201 = 3*s_0 - S_topo, 1.381 = 4*s_0 - S_topo
    => s_0 = 0.180 nats/bond, S_topo = -0.661 nats

    Wait — S_topo should be non-negative for a topological phase.
    The negative S_topo means the entanglement EXCEEDS the naive area law.
    This is consistent with BCS long-range pairing correlations.

    For CG(24), we use: S_bulk(k) = s_0 * |cut_edges(k)| + S_topo_abs
    where S_topo_abs = |S_topo| accounts for the BCS correlation enhancement.

    Actually, let's be more careful. The area-law fit from K_4:
        S(k) = s_0 * n_cut + gamma
    where n_cut is the number of cut edges and gamma is a constant.

    From K_4 data:
        k=1: n_cut = k*(N-k) = 1*3 = 3, S = 1.201
        k=2: n_cut = k*(N-k) = 2*2 = 4, S = 1.381

    Fit: 1.201 = 3*s_0 + gamma, 1.381 = 4*s_0 + gamma
    => s_0 = 0.180 nats/bond
    => gamma = 1.201 - 3*0.180 = 0.661 nats (intercept)

    This gamma > 0 means even zero-cut partition has entropy — which makes
    sense for BCS: the long-range pairing introduces volume-law corrections.
    """
    # Extract from Page curve data
    S_k1 = S_ent_data['S_ent_4cell_k1'][0]  # 1.201 nats
    S_k2 = S_ent_data['S_ent_4cell_k2'][0]  # 1.381 nats

    # Area-law fit on K_4: S = s_0 * n_cut + gamma
    # K_4 cuts: k=1 -> 3 edges, k=2 -> 4 edges
    ncut_k1 = 1 * (4 - 1)  # = 3
    ncut_k2 = 2 * (4 - 2)  # = 4

    s_0 = (S_k2 - S_k1) / (ncut_k2 - ncut_k1)  # nats per bond
    gamma = S_k1 - s_0 * ncut_k1  # intercept

    print(f"\nArea-law fit from 4-cell Page curve:")
    print(f"  S(k=1) = {S_k1:.6f} nats, n_cut = {ncut_k1}")
    print(f"  S(k=2) = {S_k2:.6f} nats, n_cut = {ncut_k2}")
    print(f"  s_0 = {s_0:.6f} nats/bond (entropy per cut bond)")
    print(f"  gamma = {gamma:.6f} nats (intercept / correlation term)")

    return s_0, gamma


# ============================================================================
# Section 3: Generalized Entropy Functional
# ============================================================================

def compute_G_eff():
    """
    Effective Newton constant from spectral action.

    G_eff = 1 / (16 * pi * a_2)

    where a_2 is the Seeley-DeWitt coefficient at the fold.
    This is in M_KK units (G_eff has units of M_KK^{-2}).
    """
    G_eff = 1.0 / (16.0 * PI * a2_fold)
    print(f"\nEffective Newton constant:")
    print(f"  a_2(fold) = {a2_fold:.4f}")
    print(f"  G_eff = 1/(16*pi*a_2) = {G_eff:.6e} M_KK^{{-2}}")
    return G_eff


def generalized_entropy(n_cut, s_0, gamma, E_J, G_eff):
    """
    Compute generalized entropy for a bipartition with n_cut severed edges.

    S_gen = n_cut * E_J / (4 * G_eff)  +  S_bulk(n_cut)

    Area term: Each severed Josephson bond contributes E_J to the
    gravitational area. The analog of A/(4G) is n_cut * E_J / (4 * G_eff).

    Bulk term: S_bulk = s_0 * n_cut + gamma (area-law from Page curve fit).

    Note: The area term DOMINATES when E_J / (4*G_eff) >> s_0, which is the
    semiclassical regime. The bulk term provides the quantum correction.
    """
    area_term = n_cut * E_J / (4.0 * G_eff)
    bulk_term = s_0 * n_cut + gamma
    S_gen = area_term + bulk_term
    return S_gen, area_term, bulk_term


# ============================================================================
# Section 4: Enumerate Bipartitions of CG(24)
# ============================================================================

def min_cut_stoer_wagner(adj):
    """
    Stoer-Wagner algorithm for global minimum cut on an undirected graph.
    Returns (min_cut_value, partition).

    This is O(V^3) and exact for small graphs.
    """
    N = adj.shape[0]
    # Work with a weighted adjacency matrix (initially all 1s for unweighted)
    w = adj.astype(np.float64).copy()

    # Track which original nodes are merged into each supernode
    merged = [[i] for i in range(N)]
    active = list(range(N))

    best_cut = float('inf')
    best_partition = None

    for phase in range(N - 1):
        # Minimum cut phase
        n = len(active)
        if n <= 1:
            break

        # Build weight to "added set" for each node
        in_A = np.zeros(N, dtype=bool)
        key = np.zeros(N, dtype=np.float64)  # weight of edges to A

        last_added = -1
        second_last = -1

        for step in range(n):
            # Find most tightly connected vertex not in A
            best_w = -1
            best_v = -1
            for v in active:
                if not in_A[v]:
                    if key[v] > best_w:
                        best_w = key[v]
                        best_v = v

            if best_v == -1:
                break

            second_last = last_added
            last_added = best_v
            in_A[best_v] = True

            # Update keys
            for u in active:
                if not in_A[u]:
                    key[u] += w[best_v, u]

        # The cut of the phase is key[last_added]
        cut_of_phase = key[last_added]

        if cut_of_phase < best_cut:
            best_cut = cut_of_phase
            best_partition = set()
            for orig in merged[last_added]:
                best_partition.add(orig)

        # Merge last_added into second_last
        if second_last >= 0 and last_added >= 0:
            merged[second_last].extend(merged[last_added])
            for v in active:
                if v != second_last and v != last_added:
                    w[second_last, v] += w[last_added, v]
                    w[v, second_last] += w[v, last_added]
            active.remove(last_added)

    return int(best_cut), best_partition


def enumerate_small_partitions(adj, max_k=6):
    """
    Enumerate all partitions of size k = 1, ..., max_k.
    For k=1: C(24,1)=24 partitions
    For k=2: C(24,2)=276
    For k=3: C(24,3)=2024
    For k=4: C(24,4)=10626
    For k=5: C(24,5)=42504
    For k=6: C(24,6)=134596
    Total for k=1..6: ~190K, manageable.

    Returns dict: k -> (min_cut_size, max_cut_size, mean_cut_size, all_cuts)
    """
    N = adj.shape[0]
    results = {}

    for k in range(1, max_k + 1):
        print(f"  Enumerating k={k}: C({N},{k}) = {len(list(range(1)))}...", end="", flush=True)

        min_cut = float('inf')
        max_cut = 0
        sum_cut = 0
        count = 0  # (local)
        all_cuts = []
        min_cut_partition = None

        for subset in combinations(range(N), k):
            mask = np.zeros(N, dtype=bool)
            mask[list(subset)] = True
            cut = graph_cut_size_fast(adj, mask)

            all_cuts.append(cut)
            sum_cut += cut
            count += 1

            if cut < min_cut:
                min_cut = cut
                min_cut_partition = subset
            if cut > max_cut:
                max_cut = cut

        mean_cut = sum_cut / count
        all_cuts = np.array(all_cuts)

        print(f" done. n={count}, min_cut={min_cut}, mean={mean_cut:.1f}, max={max_cut}")

        results[k] = {
            'min_cut': min_cut,
            'max_cut': max_cut,
            'mean_cut': mean_cut,
            'count': count,
            'min_partition': min_cut_partition,
            'cut_histogram': np.bincount(all_cuts)
        }

    return results


def random_sample_partitions(adj, N_samples=50000, seed=42):
    """
    Random sampling of bipartitions for partition sizes k = 7, ..., 12.
    By symmetry, k and N-k give the same cut size, so we only need k <= N/2 = 12.
    """
    N = adj.shape[0]
    rng = np.random.default_rng(seed)
    results = {}

    for k in range(7, N // 2 + 1):
        min_cut = float('inf')
        max_cut = 0
        sum_cut = 0
        cuts = []
        min_part = None

        n_samp = min(N_samples, 100000)

        for _ in range(n_samp):
            subset = tuple(sorted(rng.choice(N, size=k, replace=False)))
            mask = np.zeros(N, dtype=bool)
            mask[list(subset)] = True
            cut = graph_cut_size_fast(adj, mask)

            cuts.append(cut)
            sum_cut += cut
            if cut < min_cut:
                min_cut = cut
                min_part = subset
            if cut > max_cut:
                max_cut = cut

        mean_cut = sum_cut / n_samp
        cuts = np.array(cuts)

        print(f"  k={k}: {n_samp} samples, min_cut={min_cut}, mean={mean_cut:.1f}, max={max_cut}")

        results[k] = {
            'min_cut': min_cut,
            'max_cut': max_cut,
            'mean_cut': mean_cut,
            'count': n_samp,
            'min_partition': min_part,
            'cut_histogram': np.bincount(cuts)
        }

    return results


# ============================================================================
# Section 5: Quantum Extremal Surface Analysis
# ============================================================================

def find_QES(cut_results, s_0, gamma, E_J, G_eff, N_total=24):
    """
    Find the quantum extremal surface (QES) — the bipartition that minimizes
    the generalized entropy S_gen.

    For each partition size k, we use the minimum-cut partition (which
    minimizes the area term) and compute S_gen.

    The trivial partition (k=0 or k=N) has S_gen = gamma (just the bulk
    constant, no cut edges).

    A non-trivial QES exists if min_k S_gen(k) < S_gen(trivial).
    """
    # Trivial partition: no cut, S_gen = gamma (constant piece only)
    # Actually at k=0: S_bulk = s_0*0 + gamma = gamma. Area = 0. S_gen = gamma
    S_gen_trivial = gamma  # For k=0 (or k=N)

    print(f"\nQuantum Extremal Surface Search:")
    print(f"  E_J = {E_J:.6f} M_KK")
    print(f"  G_eff = {G_eff:.6e} M_KK^{{-2}}")
    print(f"  Area coefficient per bond: E_J/(4*G_eff) = {E_J/(4*G_eff):.4f}")
    print(f"  Bulk coefficient per bond: s_0 = {s_0:.6f}")
    print(f"  S_gen(trivial, k=0) = {S_gen_trivial:.6f}")
    print(f"  {'k':>3s} {'n_cut_min':>10s} {'S_area':>12s} {'S_bulk':>12s} {'S_gen':>12s} {'ratio_to_triv':>14s}")
    print(f"  {'-'*3} {'-'*10} {'-'*12} {'-'*12} {'-'*12} {'-'*14}")

    S_gen_min = S_gen_trivial
    k_min = 0
    ncut_min_at_kmin = 0
    partition_at_min = None

    # Store S_gen vs k for plotting
    k_values = []
    S_gen_values = []
    S_area_values = []
    S_bulk_values = []
    ncut_min_values = []

    for k in sorted(cut_results.keys()):
        n_cut = cut_results[k]['min_cut']
        S_gen, S_area, S_bulk = generalized_entropy(n_cut, s_0, gamma, E_J, G_eff)

        ratio = S_gen / S_gen_trivial if S_gen_trivial > 0 else float('inf')

        print(f"  {k:3d} {n_cut:10d} {S_area:12.4f} {S_bulk:12.4f} {S_gen:12.4f} {ratio:14.4f}")

        k_values.append(k)
        S_gen_values.append(S_gen)
        S_area_values.append(S_area)
        S_bulk_values.append(S_bulk)
        ncut_min_values.append(n_cut)

        if S_gen < S_gen_min:
            S_gen_min = S_gen
            k_min = k
            ncut_min_at_kmin = n_cut
            partition_at_min = cut_results[k].get('min_partition', None)

    # Check the complement: by symmetry, k and N-k have same cut
    # We already get this from k > N/2 if sampled

    print(f"\n  Minimum S_gen = {S_gen_min:.6f} at k = {k_min}")
    if k_min == 0:
        print(f"  TRIVIAL partition wins: no non-trivial QES exists")
        qes_exists = False
    else:
        print(f"  Non-trivial QES at k = {k_min}, n_cut = {ncut_min_at_kmin}")
        print(f"  S_gen(QES) / S_gen(trivial) = {S_gen_min / S_gen_trivial:.6f}")
        qes_exists = True

    return {
        'qes_exists': qes_exists,
        'k_min': k_min,
        'S_gen_min': S_gen_min,
        'S_gen_trivial': S_gen_trivial,
        'ncut_at_min': ncut_min_at_kmin,
        'partition': partition_at_min,
        'k_values': np.array(k_values),
        'S_gen_values': np.array(S_gen_values),
        'S_area_values': np.array(S_area_values),
        'S_bulk_values': np.array(S_bulk_values),
        'ncut_min_values': np.array(ncut_min_values),
    }


# ============================================================================
# Section 6: Lambda Suppression Computation
# ============================================================================

def compute_lambda_suppression(qes_result, s_0, gamma, E_J, G_eff):
    """
    If a non-trivial QES exists, compute the CC suppression.

    The island formula interpretation:
    - The "gravitating" region is inside the QES
    - The "non-gravitating" region (the island) is outside
    - The effective CC is suppressed by exp(-S_boundary)

    For the Josephson fabric:
    Lambda_eff = Lambda_bulk * exp(-S_gen_boundary)

    where S_gen_boundary = S_gen(QES) = the generalized entropy at the
    quantum extremal surface.

    The bare Lambda_bulk ~ M_KK^4 * a_0 / (16*pi^2) ~ 10^{66} GeV^4
    (the spectral action CC).

    The suppression in OOM:
    Delta_OOM = S_gen(QES) / ln(10)

    But this is S_gen per CELL. For the full 24-cell fabric:
    - Each cell contributes independently if they're uncorrelated
    - The total suppression is S_gen_total = N_cells * S_gen(QES) if extensive
    - But entanglement is NOT extensive — it's area-law

    The correct counting:
    - The QES divides the 24 vertices into k_min inside and (24-k_min) outside
    - The boundary has ncut_at_min edges
    - S_gen = ncut * (E_J/4G_eff + s_0) + gamma
    - Lambda_eff / Lambda_bare = exp(-S_gen(QES))

    Also compute: the entanglement entropy contribution alone (without area term):
    S_ent_QES = s_0 * ncut_at_min + gamma
    Lambda suppression from entanglement alone: exp(-S_ent_QES)
    """
    if not qes_result['qes_exists']:
        return {
            'suppression_OOM_total': 0.0,
            'suppression_OOM_ent_only': 0.0,
            'Lambda_ratio': 1.0,
        }

    S_gen = qes_result['S_gen_min']
    ncut = qes_result['ncut_at_min']

    # Full S_gen suppression
    suppression_OOM_total = S_gen / np.log(10)

    # Entanglement-only suppression (bulk term)
    S_ent_only = s_0 * ncut + gamma
    suppression_OOM_ent = S_ent_only / np.log(10)

    # Area-only suppression
    S_area_only = ncut * E_J / (4.0 * G_eff)
    suppression_OOM_area = S_area_only / np.log(10)

    # Lambda ratio
    Lambda_ratio = np.exp(-S_gen) if S_gen < 700 else 0.0  # avoid overflow

    print(f"\nLambda Suppression at QES:")
    print(f"  S_gen(QES) = {S_gen:.4f} nats")
    print(f"  S_area = {S_area_only:.4f} nats ({suppression_OOM_area:.1f} OOM)")
    print(f"  S_bulk = {S_ent_only:.4f} nats ({suppression_OOM_ent:.1f} OOM)")
    print(f"  Total suppression: {suppression_OOM_total:.1f} OOM")
    print(f"  Lambda_eff/Lambda_bare = exp(-{S_gen:.4f}) = {Lambda_ratio:.6e}")

    # Compare to CC gap
    # The CC gap is ~120 OOM (M_Pl^4 / rho_Lambda_obs)
    # The spectral action CC gap is ~113 OOM (from a_0 * M_KK^4)
    CC_gap_OOM = 120.0  # standard CC problem in OOM  # (local)

    print(f"\n  CC gap: {CC_gap_OOM:.0f} OOM")
    print(f"  QES suppression: {suppression_OOM_total:.1f} OOM")
    print(f"  Remaining gap: {CC_gap_OOM - suppression_OOM_total:.1f} OOM")

    return {
        'S_gen_QES': S_gen,
        'S_area_QES': S_area_only,
        'S_bulk_QES': S_ent_only,
        'suppression_OOM_total': suppression_OOM_total,
        'suppression_OOM_area': suppression_OOM_area,
        'suppression_OOM_ent': suppression_OOM_ent,
        'Lambda_ratio': Lambda_ratio,
        'CC_gap_OOM': CC_gap_OOM,
        'remaining_gap_OOM': CC_gap_OOM - suppression_OOM_total,
    }


# ============================================================================
# Section 7: Topological Entanglement Entropy
# ============================================================================

def compute_topological_entropy(s_0, gamma):
    """
    Topological entanglement entropy from the area-law fit.

    In the standard area-law: S(A) = alpha * |dA| - S_topo

    Our fit: S(A) = s_0 * |dA| + gamma

    So S_topo = -gamma (if gamma < 0) or the system has volume-law
    corrections (if gamma > 0).

    For a gapped BCS system with trivial topology (BDI winding = 0, S38):
    S_topo = 0 expected. The positive gamma reflects the BCS pairing
    correlation that extends beyond nearest-neighbor.
    """
    S_topo = -gamma  # Standard convention: S = alpha*L - S_topo

    print(f"\nTopological Entanglement Entropy:")
    print(f"  s_0 (area coefficient) = {s_0:.6f} nats/bond")
    print(f"  gamma (intercept) = {gamma:.6f} nats")
    print(f"  S_topo = -gamma = {S_topo:.6f} nats")

    if S_topo < 0:
        print(f"  NEGATIVE S_topo: system has SUPER-area-law entanglement")
        print(f"  Consistent with BCS pairing correlations (non-local)")
    elif S_topo == 0:
        print(f"  ZERO S_topo: trivial topological order")
    else:
        print(f"  POSITIVE S_topo: nontrivial topological order")
        print(f"  Quantum dimension D = exp(S_topo) = {np.exp(S_topo):.4f}")

    return S_topo


# ============================================================================
# Section 8: Graph Isoperimetric Analysis
# ============================================================================

def isoperimetric_analysis(adj, cut_results):
    """
    Compute the Cheeger constant (isoperimetric number) of CG(24).

    h(G) = min_{|S| <= N/2} |dS| / |S|

    This quantifies how hard it is to "disconnect" the graph, which directly
    relates to the area-law behavior of entanglement.
    """
    N = adj.shape[0]

    h_min = float('inf')
    k_at_min = 0

    print(f"\nIsoperimetric (Cheeger) Analysis:")
    print(f"  {'k':>3s} {'min_cut':>10s} {'|dS|/|S|':>10s} {'|dS|/vol':>10s}")

    for k in sorted(cut_results.keys()):
        if k > N // 2:
            continue
        min_cut = cut_results[k]['min_cut']
        h = min_cut / k
        vol_ratio = min_cut / (k * 6)  # normalize by degree

        print(f"  {k:3d} {min_cut:10d} {h:10.4f} {vol_ratio:10.4f}")

        if h < h_min:
            h_min = h
            k_at_min = k

    print(f"\n  Cheeger constant h(CG(24)) >= {h_min:.4f} (at k={k_at_min})")
    print(f"  For comparison: K_24 has h = 12, hypercube H_5 has h ~ 1")
    print(f"  CG(24) is well-connected (h >> 0)")

    return h_min, k_at_min


# ============================================================================
# Section 9: Plotting
# ============================================================================

def make_plot(qes_result, suppression_result, s_0, gamma, E_J, G_eff,
              cut_results, outpath):
    """
    Create a 2x2 plot:
    (a) S_gen vs partition size k (with area and bulk decomposition)
    (b) Cut-size histogram for representative k values
    (c) Suppression OOM vs partition size
    (d) Isoperimetric profile |dS|/|S| vs k
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Entanglement-Area Law on CG(24): Quantum Extremal Surface',
                 fontsize=14, fontweight='bold')

    # (a) S_gen decomposition
    ax = axes[0, 0]
    k_vals = qes_result['k_values']
    S_gen = qes_result['S_gen_values']
    S_area = qes_result['S_area_values']
    S_bulk = qes_result['S_bulk_values']

    ax.plot(k_vals, S_gen, 'ko-', linewidth=2, markersize=6, label=r'$S_{\rm gen}$')
    ax.plot(k_vals, S_area, 'r^--', linewidth=1.5, markersize=5, label=r'$A/(4G_{\rm eff})$')
    ax.plot(k_vals, S_bulk, 'bs--', linewidth=1.5, markersize=5, label=r'$S_{\rm bulk}$')
    ax.axhline(y=qes_result['S_gen_trivial'], color='gray', linestyle=':',
               label=f'Trivial ($k=0$): {qes_result["S_gen_trivial"]:.3f}')

    ax.set_xlabel('Partition size $k$', fontsize=12)
    ax.set_ylabel('Entropy (nats)', fontsize=12)
    ax.set_title('(a) Generalized entropy decomposition', fontsize=12)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.3)

    # (b) Cut-size distribution for k=1,4,8,12
    ax = axes[0, 1]
    for k_show in [1, 4, 8, 12]:
        if k_show in cut_results:
            hist = cut_results[k_show]['cut_histogram']
            x = np.arange(len(hist))
            if hist.sum() > 0:
                ax.bar(x + 0.15*(k_show//4), hist/hist.sum(), width=0.12,
                       alpha=0.7, label=f'k={k_show}')  # (local)

    ax.set_xlabel('Cut size $|\\partial\\Sigma|$', fontsize=12)
    ax.set_ylabel('Probability', fontsize=12)
    ax.set_title('(b) Cut-size distributions', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # (c) Suppression in OOM vs k
    ax = axes[1, 0]
    # For each k, compute the OOM suppression at minimum cut
    k_all = sorted(cut_results.keys())
    ooms_total = []
    ooms_area = []
    ooms_bulk = []

    for k in k_all:
        ncut = cut_results[k]['min_cut']
        S_g, S_a, S_b = generalized_entropy(ncut, s_0, gamma, E_J, G_eff)
        ooms_total.append(S_g / np.log(10))
        ooms_area.append(S_a / np.log(10))
        ooms_bulk.append(S_b / np.log(10))

    ax.plot(k_all, ooms_total, 'ko-', linewidth=2, markersize=6, label='Total')
    ax.plot(k_all, ooms_area, 'r^--', linewidth=1.5, markersize=5, label='Area')
    ax.plot(k_all, ooms_bulk, 'bs--', linewidth=1.5, markersize=5, label='Bulk')
    ax.axhline(y=120, color='orange', linestyle='-.', linewidth=1.5, label='CC gap (120 OOM)')
    ax.axhline(y=50, color='green', linestyle='-.', linewidth=1.5, label='Target (50 OOM)')

    ax.set_xlabel('Partition size $k$', fontsize=12)
    ax.set_ylabel('Suppression (OOM)', fontsize=12)
    ax.set_title('(c) CC suppression at minimum cut', fontsize=12)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.3)

    # (d) Isoperimetric ratio
    ax = axes[1, 1]
    iso_k = []
    iso_h = []
    iso_mean = []

    for k in sorted(cut_results.keys()):
        if k <= 12:  # Only k <= N/2
            iso_k.append(k)
            iso_h.append(cut_results[k]['min_cut'] / k)
            iso_mean.append(cut_results[k]['mean_cut'] / k)

    ax.plot(iso_k, iso_h, 'ko-', linewidth=2, markersize=6, label='$h(k) = |\\partial S|_{\\min}/k$')
    ax.plot(iso_k, iso_mean, 'gs--', linewidth=1.5, markersize=5, label='$\\langle|\\partial S|\\rangle/k$')

    ax.set_xlabel('Partition size $k$', fontsize=12)
    ax.set_ylabel('Isoperimetric ratio', fontsize=12)
    ax.set_title('(d) Cheeger profile', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved: {outpath}")


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 70)
    print("S60 ENTANGLE-CG24: Quantum Extremal Surface on CG(24)")
    print("=" * 70)

    # --- Load input data ---
    script_dir = os.path.dirname(os.path.abspath(__file__))

    page_data = np.load(os.path.join(script_dir, 's59_page_curve.npz'), allow_pickle=True)
    joseph_data = np.load(os.path.join(script_dir, 's59_josephson_phase.npz'), allow_pickle=True)

    print(f"\nInput data loaded:")
    print(f"  S_ent(k=1) = {page_data['S_ent_4cell_k1'][0]:.6f} nats")
    print(f"  S_ent(k=2) = {page_data['S_ent_4cell_k2'][0]:.6f} nats")
    print(f"  E_J(fold) = {float(joseph_data['E_J_fold']):.6f} M_KK (from Josephson)")
    print(f"  J_C2(fold, canonical) = {J_C2:.6f} M_KK (from canonical)")

    # Use the Josephson-phase E_J (more physically grounded for inter-cell coupling)
    E_J = float(joseph_data['E_J_fold'])

    # --- Step 1: Build CG(24) ---
    print(f"\n{'='*70}")
    print("Step 1: Building Cayley graph of S_4")
    print(f"{'='*70}")
    adj, edges, elements, elem_to_idx = build_cayley_graph_S4()

    # --- Step 2: Area-law fit from Page curve ---
    print(f"\n{'='*70}")
    print("Step 2: Area-law fit from 4-cell Page curve")
    print(f"{'='*70}")
    s_0, gamma = bulk_entropy_model(None, 24, page_data)

    # --- Step 3: Effective Newton constant ---
    print(f"\n{'='*70}")
    print("Step 3: Effective Newton constant")
    print(f"{'='*70}")
    G_eff = compute_G_eff()

    # Area coefficient per bond
    area_coeff = E_J / (4.0 * G_eff)
    print(f"\n  Area coefficient per severed bond: E_J/(4*G_eff) = {area_coeff:.4f}")
    print(f"  Bulk coefficient per bond: s_0 = {s_0:.6f}")
    print(f"  Ratio (area/bulk): {area_coeff / s_0:.2f}")
    print(f"  --> Area term DOMINATES by factor {area_coeff / s_0:.0f}")

    # --- Step 4: Enumerate bipartitions ---
    print(f"\n{'='*70}")
    print("Step 4: Enumerating bipartitions of CG(24)")
    print(f"{'='*70}")

    # Exact enumeration for small k
    print("\n  Exact enumeration (k=1..6):")
    exact_results = enumerate_small_partitions(adj, max_k=6)

    # Random sampling for larger k
    print("\n  Random sampling (k=7..12):")
    random_results = random_sample_partitions(adj, N_samples=50000)

    # Merge results (by symmetry k and 24-k have same minimum cut)
    cut_results = {}
    for k, v in exact_results.items():
        cut_results[k] = v
    for k, v in random_results.items():
        cut_results[k] = v
    # Add symmetric complements
    for k in list(cut_results.keys()):
        comp_k = 24 - k
        if comp_k not in cut_results and comp_k > 0 and comp_k < 24:
            cut_results[comp_k] = cut_results[k].copy()

    # --- Step 4b: Stoer-Wagner exact minimum cut ---
    print("\n  Stoer-Wagner global minimum cut:")
    sw_min_cut, sw_partition = min_cut_stoer_wagner(adj)
    print(f"  Global min cut = {sw_min_cut} edges")
    print(f"  Partition size: {len(sw_partition)} vertices")

    # --- Step 5: Find QES ---
    print(f"\n{'='*70}")
    print("Step 5: Quantum Extremal Surface Search")
    print(f"{'='*70}")
    qes_result = find_QES(cut_results, s_0, gamma, E_J, G_eff)

    # --- Step 6: Lambda suppression ---
    print(f"\n{'='*70}")
    print("Step 6: Lambda Suppression")
    print(f"{'='*70}")
    supp = compute_lambda_suppression(qes_result, s_0, gamma, E_J, G_eff)

    # --- Step 7: Topological entropy ---
    print(f"\n{'='*70}")
    print("Step 7: Topological Entanglement Entropy")
    print(f"{'='*70}")
    S_topo = compute_topological_entropy(s_0, gamma)

    # --- Step 8: Isoperimetric analysis ---
    print(f"\n{'='*70}")
    print("Step 8: Isoperimetric Analysis")
    print(f"{'='*70}")
    h_cheeger, k_cheeger = isoperimetric_analysis(adj, cut_results)

    # --- Gate verdict ---
    print(f"\n{'='*70}")
    print("GATE VERDICT: ENTANGLE-CG24-60")
    print(f"{'='*70}")

    if not qes_result['qes_exists']:
        # S_gen is monotonically increasing with k (since area dominates)
        # Check if S_gen is indeed monotone
        S_gen_increasing = all(
            qes_result['S_gen_values'][i] <= qes_result['S_gen_values'][i+1]
            for i in range(len(qes_result['S_gen_values'])-1)
            if i+1 < len(qes_result['S_gen_values'])
        )

        if S_gen_increasing:
            verdict = "FAIL"
            detail = (f"S_gen monotonically increasing with partition size. "
                     f"Area term ({area_coeff:.1f} per bond) dominates bulk ({s_0:.4f} per bond) "
                     f"by factor {area_coeff/s_0:.0f}x. No nontrivial QES. "
                     f"Trivial partition is global minimum.")
        else:
            verdict = "FAIL"
            detail = (f"No nontrivial QES exists. Trivial partition (k=0) minimizes S_gen. "
                     f"S_gen_min(trivial) = {qes_result['S_gen_trivial']:.4f}. "
                     f"S_gen_min(nontrivial) = {min(qes_result['S_gen_values']):.4f}.")
    elif supp['suppression_OOM_total'] > 50:
        verdict = "PASS"
        detail = (f"Nontrivial QES at k={qes_result['k_min']}, "
                 f"suppression = {supp['suppression_OOM_total']:.1f} OOM > 50 OOM threshold.")
    else:
        verdict = "INFO"
        detail = (f"Nontrivial QES at k={qes_result['k_min']}, "
                 f"but suppression = {supp['suppression_OOM_total']:.1f} OOM < 50 OOM threshold.")

    print(f"\n  Verdict: {verdict}")
    print(f"  Detail: {detail}")

    # --- Summary statistics ---
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"  Graph: CG(24) = Cayley(S_4, {{(12),(23),(34)}})")
    print(f"  Vertices: 24, Edges: 72, Degree: 6")
    print(f"  Diameter: {graph_diameter(adj)}")
    print(f"  Cheeger constant: h >= {h_cheeger:.4f}")
    print(f"  Stoer-Wagner min cut: {sw_min_cut} edges")
    print(f"  Area-law fit: s_0 = {s_0:.6f} nats/bond, gamma = {gamma:.6f} nats")
    print(f"  S_topo = {S_topo:.6f} nats")
    print(f"  G_eff = {G_eff:.6e} M_KK^{{-2}}")
    print(f"  Area coeff per bond: {area_coeff:.4f}")
    print(f"  Area/bulk ratio: {area_coeff/s_0:.0f}x")
    print(f"  QES exists: {qes_result['qes_exists']}")
    if qes_result['qes_exists']:
        print(f"  QES partition size: k = {qes_result['k_min']}")
        print(f"  S_gen(QES) = {qes_result['S_gen_min']:.4f} nats")
        print(f"  Suppression: {supp['suppression_OOM_total']:.1f} OOM")
    else:
        print(f"  S_gen monotone: smallest nontrivial S_gen at k=1: {qes_result['S_gen_values'][0]:.4f}")
        print(f"  S_gen(trivial) = {qes_result['S_gen_trivial']:.4f}")
        print(f"  Dominance ratio: S_gen(k=1)/S_gen(k=0) = {qes_result['S_gen_values'][0]/qes_result['S_gen_trivial']:.2f}x")

    # What the area term ALONE would give if it were the suppression mechanism
    # (hypothetical: if somehow the bulk dominated instead)
    print(f"\n  Hypothetical bulk-only suppression (if area term were absent):")
    for k in [1, 4, 8, 12]:
        if k in cut_results:
            ncut = cut_results[k]['min_cut']
            S_b = s_0 * ncut + gamma
            print(f"    k={k}: n_cut={ncut}, S_bulk={S_b:.4f} nats = {S_b/np.log(10):.2f} OOM")

    # What if we interpret the S59 claim differently — the 62 OOM was from
    # log10(dim(Hilbert)) which for N_cells=32 with 256 states each
    # gives 32 * log10(256) = 32 * 2.408 = 77 OOM (close to 62 if fewer modes)
    N_modes_per_cell = 8  # 4B2 + 1B1 + 3B3
    dim_per_cell = 2**N_modes_per_cell  # = 256
    S_max_per_cell = np.log(dim_per_cell)  # = 5.545 nats
    S_max_total = 24 * S_max_per_cell
    print(f"\n  Maximum entropy (extensive, all cells):")
    print(f"    dim/cell = 2^{N_modes_per_cell} = {dim_per_cell}")
    print(f"    S_max/cell = {S_max_per_cell:.3f} nats")
    print(f"    S_max(24 cells) = {S_max_total:.1f} nats = {S_max_total/np.log(10):.1f} OOM")
    print(f"    If this were suppression: ~{S_max_total/np.log(10):.0f} OOM (volume-law, NOT area-law)")

    # The area-law suppression at the minimum cut
    S_area_at_mincut = s_0 * sw_min_cut + gamma
    print(f"\n  Area-law entropy at global min cut ({sw_min_cut} edges):")
    print(f"    S_ent = {S_area_at_mincut:.4f} nats = {S_area_at_mincut/np.log(10):.2f} OOM")

    # --- Plot ---
    print(f"\n{'='*70}")
    print("Step 9: Generating plot")
    print(f"{'='*70}")
    outpath_png = os.path.join(script_dir, 's60_entangle_cg24.png')
    make_plot(qes_result, supp, s_0, gamma, E_J, G_eff, cut_results, outpath_png)

    # --- Save data ---
    print(f"\n{'='*70}")
    print("Step 10: Saving data")
    print(f"{'='*70}")
    outpath_npz = os.path.join(script_dir, 's60_entangle_cg24.npz')

    np.savez(outpath_npz,
        # Graph properties
        adj=adj,
        N_vertices=24,
        N_edges=72,
        degree=6,
        diameter=graph_diameter(adj),
        cheeger_constant=h_cheeger,
        cheeger_k=k_cheeger,
        sw_min_cut=sw_min_cut,

        # Area-law fit
        s_0=s_0,
        gamma=gamma,
        S_topo=S_topo,

        # Effective Newton constant
        G_eff=G_eff,
        E_J=E_J,
        area_coeff_per_bond=area_coeff,
        area_bulk_ratio=area_coeff / s_0,

        # QES results
        qes_exists=qes_result['qes_exists'],
        k_min=qes_result['k_min'],
        S_gen_min=qes_result['S_gen_min'],
        S_gen_trivial=qes_result['S_gen_trivial'],
        ncut_at_min=qes_result['ncut_at_min'],

        # S_gen vs k arrays
        k_values=qes_result['k_values'],
        S_gen_values=qes_result['S_gen_values'],
        S_area_values=qes_result['S_area_values'],
        S_bulk_values=qes_result['S_bulk_values'],
        ncut_min_values=qes_result['ncut_min_values'],

        # Suppression
        suppression_OOM_total=supp.get('suppression_OOM_total', 0.0),
        suppression_OOM_area=supp.get('suppression_OOM_area', 0.0),
        suppression_OOM_ent=supp.get('suppression_OOM_ent', 0.0),
        Lambda_ratio=supp.get('Lambda_ratio', 1.0),
        CC_gap_OOM=supp.get('CC_gap_OOM', 120.0),
        remaining_gap_OOM=supp.get('remaining_gap_OOM', 120.0),

        # Extensive entropy
        S_max_per_cell=S_max_per_cell,
        S_max_total_24cells=S_max_total,
        S_max_total_OOM=S_max_total / np.log(10),

        # Gate verdict
        gate_name='ENTANGLE-CG24-60',
        gate_verdict=verdict,
        gate_detail=detail,
    )
    print(f"  Data saved: {outpath_npz}")

    # Final gate statement
    print(f"\n{'='*70}")
    print(f"GATE: ENTANGLE-CG24-60 — {verdict}")
    print(f"  {detail}")
    print(f"{'='*70}")

    return verdict, qes_result, supp


if __name__ == '__main__':
    main()
