#!/usr/bin/env python3
"""
S71 DISCRETE-RW-UNIVERSALITY-71: Exact Velocity Distribution on CG(S_N) Graphs
================================================================================

Constructs Cayley graphs for four groups of increasing order:
  |G| = 24  : S_4
  |G| = 48  : S_4 x Z_2
  |G| = 120 : S_5
  |G| = 240 : S_5 x Z_2

For each:
  1. Build adjacency matrix from standard generating set (adjacent transpositions).
  2. Compute graph Laplacian L = D - A.
  3. Diagonalize L: eigenvalues mu_0=0 < mu_1 <= ... <= mu_{N-1}.
  4. Compute quantum walk propagator U(t) = exp(-i*L*t).
  5. Compute mean-square displacement <r^2(t)>.
  6. Extract velocity distribution P(v) from time derivative of <r^2(t)>.
  7. Extract spectral dimension d_s from log-log slope of <r^2(t)>.

Gate: PASS if D_KL(P_N || P_24) < 0.1 for all N > 24.
      FAIL if D_KL > 1.0 for any N.
      INFO if intermediate.

Session: S71
Author: Kitaev Quantum Chaos Theorist
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy import linalg as la
from itertools import permutations
from collections import deque
import time

from canonical_constants import N_cells, tau_fold, M_KK

# ============================================================================
#  Group construction utilities
# ============================================================================

def permutation_to_tuple(perm):
    """Convert permutation to hashable tuple."""
    return tuple(perm)

def compose_perms(p1, p2):
    """Compose two permutations: (p1 o p2)(i) = p1[p2[i]]."""
    return tuple(p1[p2[i]] for i in range(len(p1)))

def inverse_perm(p):
    """Inverse of a permutation."""
    inv = [0] * len(p)
    for i, pi in enumerate(p):
        inv[pi] = i
    return tuple(inv)

def identity_perm(n):
    """Identity permutation of S_n."""
    return tuple(range(n))

def adjacent_transpositions(n):
    """Standard generating set for S_n: {(i, i+1) for i=0,...,n-2}."""
    gens = []
    for i in range(n - 1):
        p = list(range(n))
        p[i], p[i+1] = p[i+1], p[i]
        gens.append(tuple(p))
    return gens

def build_cayley_graph(elements, generators):
    """
    Build adjacency matrix of Cayley graph.

    Cayley graph CG(G, S): vertices = group elements,
    edge g -- h iff h = g*s for some s in S or s^{-1} in S.

    Parameters
    ----------
    elements : list of tuples
        All group elements as permutation tuples.
    generators : list of tuples
        Generating set (need not include inverses; we symmetrize).

    Returns
    -------
    A : ndarray (N x N)
        Adjacency matrix (symmetric, 0-1).
    elem_to_idx : dict
        Map from element tuple to matrix index.
    """
    N = len(elements)
    elem_to_idx = {e: i for i, e in enumerate(elements)}
    A = np.zeros((N, N), dtype=np.float64)

    # Include generators and their inverses
    gen_set = set()
    for g in generators:
        gen_set.add(g)
        gen_set.add(inverse_perm(g))

    for g in elements:
        ig = elem_to_idx[g]
        for s in gen_set:
            h = compose_perms(g, s)
            ih = elem_to_idx[h]
            A[ig, ih] = 1.0

    return A, elem_to_idx

def graph_distances(A):
    """
    Compute all-pairs shortest path distances via BFS.

    Parameters
    ----------
    A : ndarray (N x N)
        Adjacency matrix.

    Returns
    -------
    dist : ndarray (N x N)
        Shortest path distance matrix.
    """
    N = A.shape[0]
    dist = np.full((N, N), -1, dtype=np.int32)

    for source in range(N):
        dist[source, source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in range(N):
                if A[u, v] > 0 and dist[source, v] == -1:
                    dist[source, v] = dist[source, u] + 1
                    queue.append(v)

    return dist

def build_z2_product(elements, generators):
    """
    Build G x Z_2 from G.

    Elements: (g, 0) and (g, 1) for g in G.
    Generators: original generators (acting on G component) + Z_2 flip.

    Returns elements as permutations on 2n symbols:
      (g, 0) -> g acts on {0,...,n-1}, identity on {n,...,2n-1}
      Z_2 flip: swap positions {0,...,n-1} <-> {n,...,2n-1}

    Actually, represent as tuples (perm, z2_bit) for simplicity.
    """
    n = len(elements[0])  # size of permutation
    new_elements = []
    for g in elements:
        new_elements.append((g, 0))
        new_elements.append((g, 1))

    new_generators = []
    # Lift each generator: (s, 0)
    for s in generators:
        new_generators.append((s, 0))
    # Z_2 flip: (identity, 1)
    new_generators.append((identity_perm(n), 1))

    return new_elements, new_generators

def compose_z2_product(g1, g2):
    """Compose (perm1, z1) * (perm2, z2) = (perm1 o perm2, z1 XOR z2)."""
    return (compose_perms(g1[0], g2[0]), (g1[1] + g2[1]) % 2)

def inverse_z2_product(g):
    """Inverse of (perm, z) = (perm^{-1}, z)."""
    return (inverse_perm(g[0]), g[1])

def build_cayley_graph_z2(elements, generators):
    """Build Cayley graph for G x Z_2 product group."""
    N = len(elements)
    elem_to_idx = {e: i for i, e in enumerate(elements)}
    A = np.zeros((N, N), dtype=np.float64)

    gen_set = set()
    for g in generators:
        gen_set.add(g)
        gen_set.add(inverse_z2_product(g))

    for g in elements:
        ig = elem_to_idx[g]
        for s in gen_set:
            h = compose_z2_product(g, s)
            ih = elem_to_idx[h]
            A[ig, ih] = 1.0

    return A, elem_to_idx

# ============================================================================
#  Quantum walk and velocity distribution
# ============================================================================

def quantum_walk_msd(L_evals, L_evecs, dist_from_origin, t_arr):
    """
    Compute mean-square displacement <r^2(t)> for quantum walk.

    U(t) = exp(-i*L*t) in the eigenbasis.
    P_j(t) = |U(t)_{0,j}|^2 = |<j|exp(-iLt)|0>|^2
    <r^2(t)> = sum_j P_j(t) * d(0,j)^2

    Parameters
    ----------
    L_evals : array (N,)
        Eigenvalues of graph Laplacian.
    L_evecs : array (N, N)
        Eigenvectors (columns).
    dist_from_origin : array (N,)
        Graph distances from vertex 0.
    t_arr : array (n_t,)
        Time points.

    Returns
    -------
    msd : array (n_t,)
        Mean-square displacement at each time.
    return_prob : array (n_t,)
        Return probability P_0(t) = |U(t)_{00}|^2.
    """
    N = len(L_evals)
    n_t = len(t_arr)

    # Precompute: U(t)_{0,j} = sum_k evec_{j,k} * exp(-i*mu_k*t) * evec_{0,k}^*
    # = sum_k V_{j,k} * V_{0,k}^* * exp(-i*mu_k*t)
    # where V = L_evecs (columns are eigenvectors)

    # V_{0,k} = L_evecs[0, k] (row 0 components in eigenbasis)
    v0 = L_evecs[0, :]  # shape (N,)

    d2 = dist_from_origin.astype(np.float64) ** 2

    msd = np.zeros(n_t)
    return_prob = np.zeros(n_t)

    for it, t in enumerate(t_arr):
        # Phase factors
        phases = np.exp(-1j * L_evals * t)  # shape (N,)

        # U(t)_{0,j} = sum_k V_{j,k} * conj(V_{0,k}) * exp(-i*mu_k*t)
        # = sum_k V_{j,k} * (conj(v0_k) * phase_k)
        coeffs = np.conj(v0) * phases  # shape (N,)
        U_0j = L_evecs @ coeffs  # shape (N,)

        P_j = np.abs(U_0j) ** 2
        msd[it] = np.sum(P_j * d2)
        return_prob[it] = P_j[0]

    return msd, return_prob

def extract_velocity_distribution(msd, t_arr, n_bins=50):
    """
    Extract velocity distribution P(v) from <r^2(t)>.

    Instantaneous velocity proxy: v(t) = d(<r^2>)/dt / (2 * sqrt(<r^2>))
    normalized to give a distribution.

    Parameters
    ----------
    msd : array
        Mean-square displacement.
    t_arr : array
        Time points.
    n_bins : int
        Number of histogram bins.

    Returns
    -------
    v_centers : array
        Bin centers of velocity distribution.
    P_v : array
        Normalized velocity distribution.
    v_raw : array
        Raw velocity values at each time point.
    """
    dt = t_arr[1] - t_arr[0]

    # Numerical derivative: d(msd)/dt
    dmsd_dt = np.gradient(msd, dt)

    # Velocity: v = d(msd)/dt / (2 * sqrt(msd + epsilon))
    # This is the spreading velocity
    eps = 1e-12
    v_raw = dmsd_dt / (2 * np.sqrt(msd + eps))

    # Use |v| for the distribution (velocities can be negative due to quantum recurrences)
    v_abs = np.abs(v_raw)

    # Remove NaN/inf
    valid = np.isfinite(v_abs) & (v_abs > 0)
    v_valid = v_abs[valid]

    if len(v_valid) < 10:
        return np.zeros(n_bins), np.zeros(n_bins), v_raw

    # Histogram
    v_max = np.percentile(v_valid, 99)
    bins = np.linspace(0, v_max, n_bins + 1)
    counts, edges = np.histogram(v_valid, bins=bins, density=True)
    v_centers = 0.5 * (edges[:-1] + edges[1:])

    return v_centers, counts, v_raw

def kl_divergence(p, q, eps=1e-12):
    """
    KL divergence D_KL(p || q) with regularization.

    Both p and q must be normalized probability distributions.
    """
    p = np.asarray(p, dtype=np.float64)
    q = np.asarray(q, dtype=np.float64)

    # Normalize
    p_sum = np.sum(p)
    q_sum = np.sum(q)
    if p_sum < eps or q_sum < eps:
        return np.inf
    p = p / p_sum
    q = q / q_sum

    # Regularize: add small epsilon to avoid log(0)
    p = p + eps
    q = q + eps
    p = p / np.sum(p)
    q = q / np.sum(q)

    return np.sum(p * np.log(p / q))

def extract_spectral_dimension(msd, t_arr, fit_range=(0.3, 0.8)):
    """
    Extract spectral dimension d_s from <r^2(t)> ~ t^{2/d_w}.

    d_s = 2 * d(ln <r^2>) / d(ln t)

    Parameters
    ----------
    msd : array
        Mean-square displacement.
    t_arr : array
        Time points.
    fit_range : tuple
        Fractional range of t_arr to use for fit (avoiding early transients
        and late-time finite-size effects).

    Returns
    -------
    d_s : float
        Spectral dimension.
    slope : float
        Log-log slope of <r^2> vs t.
    r_squared : float
        Quality of fit.
    """
    # Select fitting range
    n = len(t_arr)
    i_start = int(fit_range[0] * n)
    i_end = int(fit_range[1] * n)

    # Filter positive values
    mask = (t_arr[i_start:i_end] > 0) & (msd[i_start:i_end] > 0)
    if np.sum(mask) < 5:
        return np.nan, np.nan, 0.0

    ln_t = np.log(t_arr[i_start:i_end][mask])
    ln_msd = np.log(msd[i_start:i_end][mask])

    # Linear fit in log-log space
    coeffs = np.polyfit(ln_t, ln_msd, 1)
    slope = coeffs[0]

    # d_s from walk dimension: <r^2> ~ t^{2/d_w}, d_s = 2*d_H/d_w
    # For spectral dimension from MSD: d_s = 2 * slope (when d_H = slope * d_w / 2)
    # Actually: spectral dimension from return probability P(t) ~ t^{-d_s/2}
    # From MSD: d_w = 2/slope, d_s = 2*d_f/d_w where d_f = fractal dim
    # For regular graphs d_f = topological dim, but on Cayley graphs this is more subtle
    # We report the raw slope and derived d_s = 2 * slope as the anomalous diffusion exponent

    # R^2
    predicted = np.polyval(coeffs, ln_t)
    ss_res = np.sum((ln_msd - predicted) ** 2)
    ss_tot = np.sum((ln_msd - np.mean(ln_msd)) ** 2)
    r_sq = 1.0 - ss_res / max(ss_tot, 1e-30)

    return 2.0 * slope, slope, r_sq

def spectral_dimension_from_return(return_prob, t_arr, fit_range=(0.1, 0.5)):
    """
    Extract spectral dimension from return probability P(t) ~ t^{-d_s/2}.

    This is the standard definition matching S63.
    """
    n = len(t_arr)
    i_start = max(int(fit_range[0] * n), 1)
    i_end = int(fit_range[1] * n)

    mask = (t_arr[i_start:i_end] > 0) & (return_prob[i_start:i_end] > 0)
    if np.sum(mask) < 5:
        return np.nan, np.nan, 0.0

    ln_t = np.log(t_arr[i_start:i_end][mask])
    ln_P = np.log(return_prob[i_start:i_end][mask])

    coeffs = np.polyfit(ln_t, ln_P, 1)
    slope = coeffs[0]  # Should be -d_s/2
    d_s = -2.0 * slope

    predicted = np.polyval(coeffs, ln_t)
    ss_res = np.sum((ln_P - predicted) ** 2)
    ss_tot = np.sum((ln_P - np.mean(ln_P)) ** 2)
    r_sq = 1.0 - ss_res / max(ss_tot, 1e-30)

    return d_s, slope, r_sq

# ============================================================================
#  Main computation
# ============================================================================

def main():
    print("=" * 72)
    print("S71 DISCRETE-RW-UNIVERSALITY-71")
    print("Exact Velocity Distribution on CG(S_N) Graphs")
    print("=" * 72)

    # ----------------------------------------------------------------
    # Build groups
    # ----------------------------------------------------------------
    groups = {}

    # S_4: |S_4| = 24
    print("\n--- Building S_4 (|G|=24) ---")
    t0 = time.time()
    s4_elements = list(permutations(range(4)))
    s4_gens = adjacent_transpositions(4)
    A_24, idx_24 = build_cayley_graph(s4_elements, s4_gens)
    print(f"  CG(24): {A_24.shape[0]} vertices, degree = {int(A_24.sum(axis=1)[0])}")
    print(f"  Generators: {len(s4_gens)} adjacent transpositions")
    print(f"  Build time: {time.time()-t0:.3f}s")
    groups[24] = (A_24, idx_24, s4_elements)

    # S_4 x Z_2: |G| = 48
    print("\n--- Building S_4 x Z_2 (|G|=48) ---")
    t0 = time.time()
    z2_elements, z2_gens = build_z2_product(s4_elements, s4_gens)
    A_48, idx_48 = build_cayley_graph_z2(z2_elements, z2_gens)
    print(f"  CG(48): {A_48.shape[0]} vertices, degree = {int(A_48.sum(axis=1)[0])}")
    print(f"  Generators: {len(z2_gens)} (adj. transpositions + Z_2 flip)")
    print(f"  Build time: {time.time()-t0:.3f}s")
    groups[48] = (A_48, idx_48, z2_elements)

    # S_5: |S_5| = 120
    print("\n--- Building S_5 (|G|=120) ---")
    t0 = time.time()
    s5_elements = list(permutations(range(5)))
    s5_gens = adjacent_transpositions(5)
    A_120, idx_120 = build_cayley_graph(s5_elements, s5_gens)
    print(f"  CG(120): {A_120.shape[0]} vertices, degree = {int(A_120.sum(axis=1)[0])}")
    print(f"  Generators: {len(s5_gens)} adjacent transpositions")
    print(f"  Build time: {time.time()-t0:.3f}s")
    groups[120] = (A_120, idx_120, s5_elements)

    # S_5 x Z_2: |G| = 240
    print("\n--- Building S_5 x Z_2 (|G|=240) ---")
    t0 = time.time()
    z2_5_elements, z2_5_gens = build_z2_product(s5_elements, s5_gens)
    A_240, idx_240 = build_cayley_graph_z2(z2_5_elements, z2_5_gens)
    print(f"  CG(240): {A_240.shape[0]} vertices, degree = {int(A_240.sum(axis=1)[0])}")
    print(f"  Generators: {len(z2_5_gens)} (adj. transpositions + Z_2 flip)")
    print(f"  Build time: {time.time()-t0:.3f}s")
    groups[240] = (A_240, idx_240, z2_5_elements)

    # ----------------------------------------------------------------
    # For each group: Laplacian, spectrum, quantum walk
    # ----------------------------------------------------------------
    results = {}
    N_time = 2000  # time points
    n_v_bins = 60  # velocity histogram bins

    for N_group in [24, 48, 120, 240]:
        print(f"\n{'='*60}")
        print(f"  Processing CG({N_group})")
        print(f"{'='*60}")

        A, idx_map, elements = groups[N_group]
        N = A.shape[0]

        # 1. Graph Laplacian
        D = np.diag(A.sum(axis=1))
        L = D - A

        # Verify symmetry
        assert np.allclose(L, L.T), f"Laplacian not symmetric for N={N_group}"

        # 2. Diagonalize
        t0 = time.time()
        evals, evecs = la.eigh(L)
        print(f"  Diagonalization: {time.time()-t0:.3f}s")

        # Sort
        order = np.argsort(evals)
        evals = evals[order]
        evecs = evecs[:, order]

        print(f"  Eigenvalues: mu_0 = {evals[0]:.6e}, mu_1 = {evals[1]:.6f}, "
              f"mu_max = {evals[-1]:.6f}")
        print(f"  Spectral gap: mu_1 = {evals[1]:.6f}")
        print(f"  Spectral ratio mu_1/mu_max = {evals[1]/evals[-1]:.4f}")

        # Check Ramanujan property: mu_1 >= d - 2*sqrt(d-1) for d-regular graph
        degree = int(A.sum(axis=1)[0])
        ramanujan_bound = degree - 2 * np.sqrt(degree - 1)
        is_ramanujan = evals[1] >= ramanujan_bound - 1e-10
        print(f"  Degree d = {degree}, Ramanujan bound = {ramanujan_bound:.4f}, "
              f"Ramanujan: {is_ramanujan}")

        # 3. Graph distances from vertex 0
        t0 = time.time()
        dist_matrix = graph_distances(A)
        dist_from_0 = dist_matrix[0, :]
        print(f"  BFS distances: {time.time()-t0:.3f}s")
        print(f"  Diameter = {dist_from_0.max()}")
        print(f"  Distance distribution: {np.bincount(dist_from_0)}")

        # 4. Time array: 10 periods of the spectral gap oscillation
        T_gap = 2 * np.pi / evals[1]
        t_max = 10 * T_gap  # (local)
        t_arr = np.linspace(0, t_max, N_time)

        # 5. Quantum walk
        t0 = time.time()
        msd, return_prob = quantum_walk_msd(evals, evecs, dist_from_0, t_arr)
        print(f"  Quantum walk: {time.time()-t0:.3f}s")
        print(f"  <r^2> range: [{msd.min():.4f}, {msd.max():.4f}]")
        print(f"  P_return range: [{return_prob.min():.6f}, {return_prob.max():.6f}]")

        # 6. Velocity distribution
        v_centers, P_v, v_raw = extract_velocity_distribution(msd, t_arr, n_bins=n_v_bins)

        # 7. Spectral dimension from MSD
        d_s_msd, slope_msd, r2_msd = extract_spectral_dimension(msd, t_arr)
        print(f"  d_s (MSD): {d_s_msd:.4f}, slope = {slope_msd:.4f}, R^2 = {r2_msd:.4f}")

        # 8. Spectral dimension from return probability
        d_s_ret, slope_ret, r2_ret = spectral_dimension_from_return(return_prob, t_arr)
        print(f"  d_s (return): {d_s_ret:.4f}, slope = {slope_ret:.4f}, R^2 = {r2_ret:.4f}")

        # 9. Eigenvalue multiplicity structure (representation theory)
        unique_evals, counts = np.unique(np.round(evals, 8), return_counts=True)
        print(f"  Distinct eigenvalues: {len(unique_evals)}")
        print(f"  Eigenvalue multiplicities: {dict(zip(np.round(unique_evals, 4), counts))}")

        results[N_group] = {
            'evals': evals,
            'degree': degree,
            'diameter': int(dist_from_0.max()),
            'dist_distribution': np.bincount(dist_from_0),
            't_arr': t_arr,
            'msd': msd,
            'return_prob': return_prob,
            'v_centers': v_centers,
            'P_v': P_v,
            'v_raw': v_raw,
            'd_s_msd': d_s_msd,
            'd_s_return': d_s_ret,
            'r2_msd': r2_msd,
            'r2_return': r2_ret,
            'spectral_gap': evals[1],
            'is_ramanujan': is_ramanujan,
            'n_distinct_evals': len(unique_evals),
            'ramanujan_bound': ramanujan_bound,
        }

    # ----------------------------------------------------------------
    # KL divergence comparison
    # ----------------------------------------------------------------
    print("\n" + "=" * 72)
    print("  KL DIVERGENCE COMPARISON")
    print("=" * 72)

    # Reference distribution: CG(24)
    ref_v = results[24]['v_centers']
    ref_Pv = results[24]['P_v']

    # For fair comparison, we need to put all distributions on the same
    # velocity grid. Re-extract with a common binning.
    # Use the MSD derivative directly for comparison.

    # Method: compare the SPECTRAL velocity distributions
    # Use power spectral density of <r^2(t)> as the "velocity distribution"
    # This is more robust than the instantaneous velocity histogram.

    # Alternative: compute velocity autocorrelation from the raw v(t) time series
    # and compare its Fourier transform (the velocity spectral density).

    # For the gate, compute KL divergence on the instantaneous velocity histograms
    # after resampling to a common grid.

    # Common velocity grid based on combined range
    v_max_common = 0
    for N_group in [24, 48, 120, 240]:
        v_raw = results[N_group]['v_raw']
        valid = np.isfinite(v_raw)
        if np.any(valid):
            v_max_common = max(v_max_common, np.percentile(np.abs(v_raw[valid]), 99))

    n_common_bins = 60
    common_bins = np.linspace(0, v_max_common, n_common_bins + 1)
    common_centers = 0.5 * (common_bins[:-1] + common_bins[1:])

    common_Pv = {}
    for N_group in [24, 48, 120, 240]:
        v_raw = results[N_group]['v_raw']
        v_abs = np.abs(v_raw)
        valid = np.isfinite(v_abs) & (v_abs > 0)
        counts, _ = np.histogram(v_abs[valid], bins=common_bins, density=True)
        common_Pv[N_group] = counts

    # KL divergences
    D_KL_values = {}
    for N_group in [48, 120, 240]:
        dkl = kl_divergence(common_Pv[N_group], common_Pv[24])
        D_KL_values[N_group] = dkl
        print(f"  D_KL(P_{N_group} || P_24) = {dkl:.6f}")

    # Also compute symmetric KL (Jensen-Shannon)
    D_JS_values = {}
    for N_group in [48, 120, 240]:
        m = 0.5 * (common_Pv[N_group] + common_Pv[24])
        js = 0.5 * kl_divergence(common_Pv[N_group], m) + \
             0.5 * kl_divergence(common_Pv[24], m)
        D_JS_values[N_group] = js
        print(f"  D_JS(P_{N_group}, P_24) = {js:.6f}")

    # ----------------------------------------------------------------
    # Also compare via MSD power spectrum (more robust)
    # ----------------------------------------------------------------
    print("\n--- MSD Power Spectrum Comparison ---")

    msd_spectra = {}
    for N_group in [24, 48, 120, 240]:
        msd_centered = results[N_group]['msd'] - np.mean(results[N_group]['msd'])
        spectrum = np.abs(np.fft.rfft(msd_centered)) ** 2
        # Normalize
        spectrum = spectrum / (np.sum(spectrum) + 1e-30)
        msd_spectra[N_group] = spectrum

    # Truncate to common length
    min_len = min(len(s) for s in msd_spectra.values())
    for N_group in msd_spectra:
        msd_spectra[N_group] = msd_spectra[N_group][:min_len]
        msd_spectra[N_group] = msd_spectra[N_group] / (np.sum(msd_spectra[N_group]) + 1e-30)

    D_KL_spectrum = {}
    for N_group in [48, 120, 240]:
        dkl = kl_divergence(msd_spectra[N_group], msd_spectra[24])
        D_KL_spectrum[N_group] = dkl
        print(f"  D_KL_spectrum(S_{N_group} || S_24) = {dkl:.6f}")

    # ----------------------------------------------------------------
    # Gate verdict
    # ----------------------------------------------------------------
    print("\n" + "=" * 72)
    print("  GATE VERDICT: DISCRETE-RW-UNIVERSALITY-71")
    print("=" * 72)

    max_dkl = max(D_KL_values.values())

    if max_dkl < 0.1:
        verdict = "PASS"
        reason = f"All D_KL < 0.1 (max = {max_dkl:.4f}). Velocity distribution universal."
    elif max_dkl > 1.0:
        verdict = "FAIL"
        reason = f"D_KL > 1.0 for at least one N (max = {max_dkl:.4f}). Graph-dependent."
    else:
        verdict = "INFO"
        reason = f"Intermediate D_KL (max = {max_dkl:.4f}). Partial universality."

    print(f"  Verdict: {verdict}")
    print(f"  Reason: {reason}")
    print(f"  D_KL values: {D_KL_values}")

    # ----------------------------------------------------------------
    # Summary table
    # ----------------------------------------------------------------
    print("\n" + "=" * 72)
    print("  SUMMARY TABLE")
    print("=" * 72)
    print(f"  {'N':>5} {'degree':>6} {'diam':>5} {'mu_1':>8} {'d_s(MSD)':>10} "
          f"{'d_s(ret)':>10} {'D_KL':>8} {'Raman':>6}")
    print(f"  {'-'*5:>5} {'-'*6:>6} {'-'*5:>5} {'-'*8:>8} {'-'*10:>10} "
          f"{'-'*10:>10} {'-'*8:>8} {'-'*6:>6}")

    for N_group in [24, 48, 120, 240]:
        r = results[N_group]
        dkl = D_KL_values.get(N_group, 0.0)
        print(f"  {N_group:5d} {r['degree']:6d} {r['diameter']:5d} "
              f"{r['spectral_gap']:8.4f} {r['d_s_msd']:10.4f} "
              f"{r['d_s_return']:10.4f} {dkl:8.4f} "
              f"{'Y' if r['is_ramanujan'] else 'N':>6}")

    # ----------------------------------------------------------------
    # Comparison to S63
    # ----------------------------------------------------------------
    print("\n--- Comparison to S63 SPECTRAL-DIMENSION-63 ---")
    d_s_S63 = 3.342  # d_s_return from S63 (return probability on SU(3) Peter-Weyl)  # (local)
    d_s_cg24_ret = results[24]['d_s_return']
    print(f"  S63 d_s (return prob, SU(3) PW) = {d_s_S63:.3f}")
    print(f"  CG(24) d_s (return prob)        = {d_s_cg24_ret:.4f}")
    print(f"  Ratio CG(24)/S63 = {d_s_cg24_ret/d_s_S63:.4f}")
    print(f"  NOTE: CG(24) is a 24-vertex discrete graph; S63 uses the full")
    print(f"        SU(3) spectrum (155,984 eigenvalues). Different scales.")

    # ----------------------------------------------------------------
    # Save data
    # ----------------------------------------------------------------
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "s71_discrete_rw_universality.npz")

    save_dict = {
        'gate_name': 'DISCRETE-RW-UNIVERSALITY-71',
        'gate_verdict': verdict,
        'gate_reason': reason,
        'graph_sizes': np.array([24, 48, 120, 240]),
        'D_KL_48': D_KL_values.get(48, np.nan),
        'D_KL_120': D_KL_values.get(120, np.nan),
        'D_KL_240': D_KL_values.get(240, np.nan),
        'D_JS_48': D_JS_values.get(48, np.nan),
        'D_JS_120': D_JS_values.get(120, np.nan),
        'D_JS_240': D_JS_values.get(240, np.nan),
        'D_KL_spectrum_48': D_KL_spectrum.get(48, np.nan),
        'D_KL_spectrum_120': D_KL_spectrum.get(120, np.nan),
        'D_KL_spectrum_240': D_KL_spectrum.get(240, np.nan),
        'max_D_KL': max_dkl,
        'common_v_centers': common_centers,
        'd_s_S63_return': d_s_S63,
    }

    for N_group in [24, 48, 120, 240]:
        r = results[N_group]
        prefix = f'cg{N_group}'
        save_dict[f'{prefix}_evals'] = r['evals']
        save_dict[f'{prefix}_degree'] = r['degree']
        save_dict[f'{prefix}_diameter'] = r['diameter']
        save_dict[f'{prefix}_spectral_gap'] = r['spectral_gap']
        save_dict[f'{prefix}_d_s_msd'] = r['d_s_msd']
        save_dict[f'{prefix}_d_s_return'] = r['d_s_return']
        save_dict[f'{prefix}_r2_msd'] = r['r2_msd']
        save_dict[f'{prefix}_r2_return'] = r['r2_return']
        save_dict[f'{prefix}_is_ramanujan'] = r['is_ramanujan']
        save_dict[f'{prefix}_n_distinct_evals'] = r['n_distinct_evals']
        save_dict[f'{prefix}_ramanujan_bound'] = r['ramanujan_bound']
        save_dict[f'{prefix}_t_arr'] = r['t_arr']
        save_dict[f'{prefix}_msd'] = r['msd']
        save_dict[f'{prefix}_return_prob'] = r['return_prob']
        save_dict[f'{prefix}_Pv'] = common_Pv[N_group]
        save_dict[f'{prefix}_dist_distribution'] = r['dist_distribution']

    np.savez(save_path, **save_dict)
    print(f"\n  Data saved to: {save_path}")

    print("\n  DONE.")

if __name__ == "__main__":
    main()
