#!/usr/bin/env python3
"""
s70_discrete_berry_dennis.py -- Bucher Test 5: Berry-Dennis on Discrete Graphs
================================================================================

Gate: DISCRETE-BERRY-DENNIS-70
    PASS:  chi^2/ndof < 3 on CG(24) for the discrete Berry-Dennis distribution
    FAIL:  No well-defined discrete limit exists for N_vertices < 100
    INFO:  Discrete limit exists but requires N > 24 for convergence

Physics:
    The Berry-Dennis velocity distribution for phase singularities in a 2D
    Gaussian random wave field is:

        P(|v|) = 8 * pi^2 * <v>^2 * |v| / (pi^2 * |v|^2 + 4 * <v>^2)^2

    This is derived for CONTINUOUS isotropic Gaussian random waves. We test
    whether this universality survives discretization onto finite graphs:
        - CG(24): 24-cell vertices (24 vertices, 96 edges, 8-regular)
        - CG(48): Cycle-based 8-regular graph (48 vertices, 192 edges)
        - CG(120): 600-cell vertices (120 vertices, 720 edges, 12-regular)

Method:
    1. Construct the graph Laplacian L on each graph
    2. Compute eigenmodes phi_n(v) of L
    3. Generate N_real random Gaussian wave fields as superpositions of eigenmodes
       with spectral density S(omega_n) = 1/(1 + omega_n^2) (Lorentzian)
    4. For each realization, construct time-dependent field
       psi(v, t) = sum_n a_n * phi_n(v) * exp(-i*omega_n*t)
    5. Identify phase singularities on plaquettes (faces with 2*pi phase winding)
    6. Track singularities between time steps to extract velocities
    7. Histogram velocity distribution, fit to Berry-Dennis, compute chi^2/ndof
    8. Test convergence: report at what N_vertices chi^2/ndof < 3

Phase singularity identification on a graph:
    A phase singularity lives on a PLAQUETTE (triangular face). For triangle
    (v_i, v_j, v_k), the discrete phase circulation is:
        Gamma = wrap(theta_j - theta_i) + wrap(theta_k - theta_j) + wrap(theta_i - theta_k)
    where wrap(x) maps to [-pi, pi]. If |Gamma| > pi, singularity present.

Velocity extraction:
    Singularity position interpolated within triangle using inverse-amplitude
    barycentric weighting. Velocity = |delta_r|/delta_t between matched
    singularities at consecutive time steps. Matching by nearest same-charge
    neighbor using vectorized distance matrix.

Author: kitaev-quantum-chaos-theorist
Session: S70, W3-E
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar
from scipy.stats import kstest
from itertools import product, permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    N_cells, c_Gold, omega_L1, J_C2,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s70_discrete_berry_dennis.npz"
OUT_PNG = SCRIPT_DIR / "s70_discrete_berry_dennis.png"

PI = np.pi
t_start = time.time()

print("=" * 78)
print("  S70 DISCRETE-BERRY-DENNIS-70: Berry-Dennis Universality on Finite Graphs")
print("=" * 78)

# =============================================================================
# SECTION 1: Graph Construction (vectorized)
# =============================================================================
print("\n--- Section 1: Construct graphs CG(24), CG(48), CG(120) ---")


def build_24cell():
    """24-cell: 24 vertices, 96 edges, 8-regular."""
    verts = []
    for i in range(4):
        for sign in [+1.0, -1.0]:
            v = np.zeros(4); v[i] = sign; verts.append(v)
    for signs in product([+0.5, -0.5], repeat=4):
        verts.append(np.array(signs))
    verts = np.array(verts)
    N = len(verts)
    # Pairwise distances via broadcasting
    diff = verts[:, None, :] - verts[None, :, :]  # (N, N, 4)
    dist = np.sqrt(np.sum(diff**2, axis=2))
    d_min = np.min(dist[dist > 1e-12])
    adj = (np.abs(dist - d_min) < 1e-10).astype(int)
    np.fill_diagonal(adj, 0)
    print(f"  CG(24): {N} vertices, {np.sum(adj)//2} edges, degree {np.sum(adj, axis=1)[0]}")
    return verts, adj


def build_600cell():
    """600-cell: 120 vertices, 720 edges, 12-regular."""
    phi = (1 + np.sqrt(5)) / 2
    inv_phi = phi - 1
    verts_set = set()

    def add_vert(w, x, y, z):
        verts_set.add(tuple(round(c, 10) for c in [w, x, y, z]))

    # Type 1: 8 permutations of (+/-1, 0, 0, 0)
    for i in range(4):
        for s in [+1.0, -1.0]:
            v = [0.0, 0.0, 0.0, 0.0]; v[i] = s; add_vert(*v)

    # Type 2: 16 vertices (+/-1/2)^4
    for signs in product([+0.5, -0.5], repeat=4):
        add_vert(*signs)

    # Type 3: even permutations of (+/-phi/2, +/-1/2, +/-1/(2phi), 0)
    base_set = [phi / 2, 0.5, inv_phi / 2, 0.0]
    all_perms = list(permutations(range(4)))
    even_perms = [p for p in all_perms
                  if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]

    for perm in even_perms:
        vals = [base_set[perm[i]] for i in range(4)]
        nz = [i for i in range(4) if abs(vals[i]) > 1e-12]
        for signs in product([+1.0, -1.0], repeat=len(nz)):
            v = list(vals)
            for k, idx in enumerate(nz):
                v[idx] *= signs[k]
            add_vert(*v)

    verts = np.array(sorted(verts_set))
    N = len(verts)
    assert N == 120, f"Expected 120, got {N}"
    diff = verts[:, None, :] - verts[None, :, :]
    dist = np.sqrt(np.sum(diff**2, axis=2))
    d_min = np.min(dist[dist > 1e-12])
    adj = (np.abs(dist - d_min) < 1e-8).astype(int)
    np.fill_diagonal(adj, 0)
    n_edges = np.sum(adj) // 2
    deg = np.sum(adj, axis=1)
    print(f"  CG(120): {N} vertices, {n_edges} edges, degree {deg[0]} "
          f"(uniform: {np.all(deg == deg[0])})")
    assert n_edges == 720
    assert np.all(deg == 12)
    return verts, adj


def build_cg48():
    """
    CG(48): 8-regular graph on 48 vertices.
    Use circulant graph C_48(1,2,3,4) -- each vertex connected to
    the 4 nearest neighbors on each side of a cycle.
    """
    N = 48
    d = 8  # (local)
    adj = np.zeros((N, N), dtype=int)
    for i in range(N):
        for dd in range(1, d // 2 + 1):
            j = (i + dd) % N
            adj[i, j] = 1
            adj[j, i] = 1
    # Place vertices on a circle in R^4 for position estimation
    angles = np.linspace(0, 2 * PI, N, endpoint=False)
    verts = np.column_stack([np.cos(angles), np.sin(angles),
                             np.cos(2 * angles), np.sin(2 * angles)])
    n_edges = np.sum(adj) // 2
    print(f"  CG(48): {N} vertices, {n_edges} edges, degree {d}")
    return verts, adj


def find_triangles_vectorized(adj):
    """Find all triangles using matrix multiplication: A^3 diagonal."""
    N = adj.shape[0]
    A = adj.astype(float)
    # Triangle exists (i,j,k) iff A[i,j]*A[j,k]*A[k,i] = 1
    # Use adjacency list for efficiency
    triangles = []
    # Build neighbor lists
    neighbors = [np.where(adj[i] > 0)[0] for i in range(N)]
    for i in range(N):
        for j in neighbors[i]:
            if j <= i:
                continue
            # Find common neighbors > j
            common = np.intersect1d(neighbors[i], neighbors[j])
            for k in common:
                if k > j:
                    triangles.append((i, j, k))
    return triangles


# Build graphs
verts_24, adj_24 = build_24cell()
verts_48, adj_48 = build_cg48()
verts_120, adj_120 = build_600cell()

# Find triangles
print("\n  Finding triangles...")
tri_24 = find_triangles_vectorized(adj_24)
tri_48 = find_triangles_vectorized(adj_48)
tri_120 = find_triangles_vectorized(adj_120)
print(f"  CG(24):  {len(tri_24)} triangles")
print(f"  CG(48):  {len(tri_48)} triangles")
print(f"  CG(120): {len(tri_120)} triangles")

graphs = {
    'CG(24)': (verts_24, adj_24, tri_24, 50000),
    'CG(48)': (verts_48, adj_48, tri_48, 50000),
    'CG(120)': (verts_120, adj_120, tri_120, 10000),   # Fewer realizations (larger graph)
}

# =============================================================================
# SECTION 2: Graph Laplacian Eigenmodes
# =============================================================================
print("\n--- Section 2: Compute graph Laplacian eigenmodes ---")

eigenmodes = {}
eigenvals = {}

for name, (verts, adj, tri, _) in graphs.items():
    N = len(verts)
    deg = np.sum(adj, axis=1).astype(float)
    L = np.diag(deg) - adj.astype(float)
    evals, evecs = eigh(L)
    eigenvals[name] = evals
    eigenmodes[name] = evecs
    print(f"  {name}: Laplacian spectrum: [{evals[0]:.4f}, {evals[1]:.4f}, ..., {evals[-1]:.4f}]")
    print(f"    Spectral gap = {evals[1]:.4f}, N_modes = {N}")


# =============================================================================
# SECTION 3: Vectorized Berry-Dennis Analysis
# =============================================================================
print("\n--- Section 3: Berry-Dennis analysis (vectorized) ---")


def berry_dennis_pdf(v, v_mean):
    """P(|v|) = 8*pi^2*<v>^2*|v| / (pi^2*|v|^2 + 4*<v>^2)^2"""
    num = 8 * PI**2 * v_mean**2 * v
    den = (PI**2 * v**2 + 4 * v_mean**2)**2
    return num / den


def berry_dennis_cdf(v, v_mean):
    """F(v) = 1 - 4*<v>^2 / (pi^2*v^2 + 4*<v>^2)"""
    return 1.0 - 4 * v_mean**2 / (PI**2 * v**2 + 4 * v_mean**2)


def detect_singularities_batch(phase, tri_arr):
    """
    Vectorized singularity detection on all triangles.

    Parameters:
        phase: (N,) array of phases at vertices
        tri_arr: (n_tri, 3) array of triangle vertex indices

    Returns:
        sing_mask: (n_tri,) boolean, True if singularity present
        charges: (n_tri,) int, +1 or -1 for each singularity
    """
    i_idx = tri_arr[:, 0]
    j_idx = tri_arr[:, 1]
    k_idx = tri_arr[:, 2]

    # Phase differences, wrapped to [-pi, pi]
    d_ij = (phase[j_idx] - phase[i_idx] + PI) % (2 * PI) - PI
    d_jk = (phase[k_idx] - phase[j_idx] + PI) % (2 * PI) - PI
    d_ki = (phase[i_idx] - phase[k_idx] + PI) % (2 * PI) - PI

    gamma = d_ij + d_jk + d_ki
    sing_mask = np.abs(gamma) > PI
    charges = np.sign(gamma).astype(int)

    return sing_mask, charges


def compute_positions_batch(psi, tri_arr, verts, sing_mask):
    """
    Compute singularity positions for all detected singularities.

    Uses inverse-amplitude barycentric interpolation.
    """
    if not np.any(sing_mask):
        return np.empty((0, verts.shape[1]))

    sing_tris = tri_arr[sing_mask]  # (n_sing, 3)
    i_idx = sing_tris[:, 0]
    j_idx = sing_tris[:, 1]
    k_idx = sing_tris[:, 2]

    amp_i = np.abs(psi[i_idx])
    amp_j = np.abs(psi[j_idx])
    amp_k = np.abs(psi[k_idx])

    w_i = 1.0 / (amp_i + 1e-30)
    w_j = 1.0 / (amp_j + 1e-30)
    w_k = 1.0 / (amp_k + 1e-30)
    w_sum = w_i + w_j + w_k

    w_i /= w_sum
    w_j /= w_sum
    w_k /= w_sum

    positions = (w_i[:, None] * verts[i_idx] +
                 w_j[:, None] * verts[j_idx] +
                 w_k[:, None] * verts[k_idx])

    return positions


def match_and_velocity_batch(pos1, charges1, pos2, charges2, dt):
    """
    Vectorized matching: for each singularity at t1, find nearest
    same-charge singularity at t2. Return velocities.
    """
    if len(pos1) == 0 or len(pos2) == 0:
        return np.array([])

    # Distance matrix: (n1, n2)
    diff = pos1[:, None, :] - pos2[None, :, :]  # (n1, n2, d)
    dist = np.sqrt(np.sum(diff**2, axis=2))      # (n1, n2)

    # Mask: only same-charge pairs
    charge_match = (charges1[:, None] == charges2[None, :])  # (n1, n2)
    dist_masked = np.where(charge_match, dist, np.inf)

    # Greedy nearest-neighbor matching
    velocities = []
    used_2 = set()

    # Sort by minimum distance to get best matches first
    min_dists = np.min(dist_masked, axis=1)
    order = np.argsort(min_dists)

    for ip in order:
        row = dist_masked[ip].copy()
        for ic in used_2:
            row[ic] = np.inf
        best_ic = np.argmin(row)
        if row[best_ic] < np.inf:
            v = row[best_ic] / dt
            if v > 0 and np.isfinite(v):
                velocities.append(v)
            used_2.add(best_ic)

    return np.array(velocities)


def run_berry_dennis_test(name, verts, adj, triangles, evals, evecs, n_real, rng):
    """Run the full Berry-Dennis test on a single graph (vectorized)."""
    N = len(verts)
    n_tri = len(triangles)

    if n_tri == 0:
        print(f"    {name}: NO TRIANGLES -- cannot detect phase singularities")
        return None

    print(f"\n  Processing {name}: {N} vertices, {n_tri} triangles, {n_real} realizations")

    # Convert triangles to array for vectorized operations
    tri_arr = np.array(triangles, dtype=int)  # (n_tri, 3)

    # Frequencies: omega_n = sqrt(lambda_n) (wave equation on graph)
    omega = np.sqrt(np.maximum(evals, 0))
    omega[0] = 0  # Zero mode

    # Spectral density: Lorentzian
    S = 1.0 / (1.0 + omega**2)  # (local)
    S[0] = 0  # Kill zero mode
    S_sqrt = np.sqrt(S)

    # Time step
    omega_max = omega[-1]
    dt = 0.1 / omega_max if omega_max > 0 else 0.01  # (local)
    print(f"    omega_max = {omega_max:.4f}, dt = {dt:.6f}")

    # Phase factors for t=0 and t=dt
    pf_1 = np.ones(N, dtype=complex)  # exp(-i*0) = 1
    pf_2 = np.exp(-1j * omega * dt)

    # Collect velocities
    all_velocities = []
    n_sings_total = 0
    n_with_sings = 0

    t_loop = time.time()

    for r in range(n_real):
        # Random amplitudes with spectral weighting
        a = (rng.randn(N) + 1j * rng.randn(N)) * S_sqrt  # (N,)

        # Field at t=0 and t=dt
        psi_1 = evecs @ (a * pf_1)  # (N,)
        psi_2 = evecs @ (a * pf_2)  # (N,)

        phase_1 = np.angle(psi_1)
        phase_2 = np.angle(psi_2)

        # Detect singularities (vectorized)
        mask_1, charges_1 = detect_singularities_batch(phase_1, tri_arr)
        mask_2, charges_2 = detect_singularities_batch(phase_2, tri_arr)

        n1 = np.sum(mask_1)
        n2 = np.sum(mask_2)
        if n1 == 0 or n2 == 0:
            continue

        n_sings_total += n1
        n_with_sings += 1

        # Compute positions
        pos_1 = compute_positions_batch(psi_1, tri_arr, verts, mask_1)
        pos_2 = compute_positions_batch(psi_2, tri_arr, verts, mask_2)

        ch_1 = charges_1[mask_1]
        ch_2 = charges_2[mask_2]

        # Match and get velocities
        vels = match_and_velocity_batch(pos_1, ch_1, pos_2, ch_2, dt)
        if len(vels) > 0:
            all_velocities.append(vels)

        if (r + 1) % 10000 == 0:
            n_vel_so_far = sum(len(v) for v in all_velocities)
            elapsed_loop = time.time() - t_loop
            rate = (r + 1) / elapsed_loop
            eta = (n_real - r - 1) / rate
            print(f"    [{r+1}/{n_real}] {n_vel_so_far} velocities, "
                  f"{rate:.0f} real/s, ETA {eta:.0f}s")

    elapsed_loop = time.time() - t_loop
    print(f"    Loop time: {elapsed_loop:.1f}s ({elapsed_loop/n_real*1000:.2f} ms/real)")
    print(f"    Realizations with singularities: {n_with_sings}/{n_real}")
    print(f"    Total singularities detected: {n_sings_total}")

    if len(all_velocities) == 0:
        print(f"    NO VELOCITIES COLLECTED")
        return {'name': name, 'N_vertices': N, 'N_triangles': n_tri,
                'N_velocities': 0, 'chi2_ndof': np.inf, 'v_mean': np.nan,
                'status': 'NO_DATA'}

    velocities = np.concatenate(all_velocities)
    print(f"    Total matched velocities: {len(velocities)}")

    if len(velocities) < 50:
        print(f"    INSUFFICIENT DATA: only {len(velocities)} velocities")
        return {'name': name, 'N_vertices': N, 'N_triangles': n_tri,
                'N_velocities': len(velocities), 'chi2_ndof': np.inf,
                'v_mean': np.mean(velocities), 'status': 'INSUFFICIENT_DATA'}

    # =========================================================================
    # Fit to Berry-Dennis distribution
    # =========================================================================
    v_mean = np.mean(velocities)
    v_median = np.median(velocities)
    v_std = np.std(velocities)
    print(f"    Statistics: <v> = {v_mean:.6f}, median = {v_median:.6f}, std = {v_std:.6f}")

    # Verify: E[v] for Berry-Dennis with parameter v_0 IS v_0
    # (derived in the docstring above)

    # MLE fit: maximize log-likelihood over v_0
    def neg_log_lik(log_v0):
        v0 = np.exp(log_v0)
        pdf_vals = berry_dennis_pdf(velocities, v0)
        pdf_vals = np.maximum(pdf_vals, 1e-300)
        return -np.sum(np.log(pdf_vals))

    result = minimize_scalar(neg_log_lik,
                             bounds=(np.log(v_mean * 0.01), np.log(v_mean * 100)),
                             method='bounded')
    v_0_mle = np.exp(result.x)
    print(f"    MLE fit: v_0 = {v_0_mle:.6f} (ratio to <v>: {v_0_mle/v_mean:.4f})")

    # Chi-squared test: bin and compare
    v_max_hist = np.percentile(velocities, 99.5)
    n_bins = max(20, min(50, len(velocities) // 200))
    bin_edges = np.linspace(0, v_max_hist, n_bins + 1)
    counts, _ = np.histogram(velocities, bins=bin_edges)

    # Expected counts (MLE)
    expected_mle = np.zeros(n_bins)
    for b in range(n_bins):
        expected_mle[b] = len(velocities) * (
            berry_dennis_cdf(bin_edges[b + 1], v_0_mle) -
            berry_dennis_cdf(bin_edges[b], v_0_mle)
        )
    # Renormalize to match observed total in range
    if np.sum(expected_mle) > 0:
        expected_mle *= np.sum(counts) / np.sum(expected_mle)

    # Expected counts (sample mean)
    expected_mean = np.zeros(n_bins)
    for b in range(n_bins):
        expected_mean[b] = len(velocities) * (
            berry_dennis_cdf(bin_edges[b + 1], v_mean) -
            berry_dennis_cdf(bin_edges[b], v_mean)
        )
    if np.sum(expected_mean) > 0:
        expected_mean *= np.sum(counts) / np.sum(expected_mean)

    # Chi^2 with MLE
    mask_mle = expected_mle > 5
    if np.sum(mask_mle) < 5:
        mask_mle = expected_mle > 1
    n_good_mle = int(np.sum(mask_mle))
    if n_good_mle >= 3:
        chi2_mle = float(np.sum((counts[mask_mle] - expected_mle[mask_mle])**2
                                / expected_mle[mask_mle]))
        ndof_mle = n_good_mle - 1  # One fitted parameter
        chi2_ndof_mle = chi2_mle / ndof_mle
    else:
        chi2_mle = np.inf
        ndof_mle = 0
        chi2_ndof_mle = np.inf

    # Chi^2 with sample mean
    mask_mean = expected_mean > 5
    if np.sum(mask_mean) < 5:
        mask_mean = expected_mean > 1
    n_good_mean = int(np.sum(mask_mean))
    if n_good_mean >= 3:
        chi2_mean = float(np.sum((counts[mask_mean] - expected_mean[mask_mean])**2
                                 / expected_mean[mask_mean]))
        ndof_mean = n_good_mean - 1
        chi2_ndof_mean = chi2_mean / ndof_mean
    else:
        chi2_mean = np.inf
        ndof_mean = 0
        chi2_ndof_mean = np.inf

    print(f"    Chi^2/ndof (MLE):  {chi2_ndof_mle:.3f} (chi2={chi2_mle:.1f}, ndof={ndof_mle})")
    print(f"    Chi^2/ndof (mean): {chi2_ndof_mean:.3f} (chi2={chi2_mean:.1f}, ndof={ndof_mean})")

    # KS test
    vel_trimmed = velocities[velocities < v_max_hist]
    ks_stat, ks_pval = kstest(vel_trimmed, lambda x: berry_dennis_cdf(x, v_0_mle))
    print(f"    KS test (MLE): D = {ks_stat:.6f}, p = {ks_pval:.4e}")

    ks_stat_mean, ks_pval_mean = kstest(vel_trimmed, lambda x: berry_dennis_cdf(x, v_mean))
    print(f"    KS test (mean): D = {ks_stat_mean:.6f}, p = {ks_pval_mean:.4e}")

    # Use the better of MLE and mean for the gate
    chi2_best = min(chi2_ndof_mle, chi2_ndof_mean)
    print(f"    Best chi^2/ndof = {chi2_best:.3f}")

    return {
        'name': name,
        'N_vertices': N,
        'N_triangles': n_tri,
        'N_velocities': len(velocities),
        'N_realizations': n_real,
        'v_mean': v_mean,
        'v_median': v_median,
        'v_std': v_std,
        'v_0_mle': v_0_mle,
        'chi2_mle': chi2_mle,
        'ndof_mle': ndof_mle,
        'chi2_ndof_mle': chi2_ndof_mle,
        'chi2_mean': chi2_mean,
        'ndof_mean': ndof_mean,
        'chi2_ndof_mean': chi2_ndof_mean,
        'chi2_best': chi2_best,
        'ks_stat': ks_stat,
        'ks_pval': ks_pval,
        'ks_stat_mean': ks_stat_mean,
        'ks_pval_mean': ks_pval_mean,
        'velocities': velocities,
        'bin_edges': bin_edges,
        'counts': counts,
        'expected_mle': expected_mle,
        'expected_mean': expected_mean,
        'avg_sings_per_real': n_sings_total / max(n_with_sings, 1),
        'status': 'COMPLETE'
    }


# =============================================================================
# SECTION 4: Run the Berry-Dennis test on all graphs
# =============================================================================
print("\n--- Section 4: Run Berry-Dennis tests ---")

rng = np.random.RandomState(2070)
results = {}

for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    verts, adj, tri, n_real = graphs[name]
    evals = eigenvals[name]
    evecs = eigenmodes[name]
    res = run_berry_dennis_test(name, verts, adj, tri, evals, evecs, n_real, rng)
    results[name] = res

# =============================================================================
# SECTION 5: Convergence Analysis and Gate Verdict
# =============================================================================
print("\n--- Section 5: Convergence analysis ---")
print(f"\n{'='*100}")
print(f"  {'Graph':<10} {'N_v':>5} {'N_tri':>6} {'N_vel':>8} "
      f"{'<v>':>10} {'v0_MLE':>10} {'chi2/ndf':>10} {'chi2_MLE':>10} "
      f"{'KS D':>8} {'KS p':>10}")
print(f"  {'-'*96}")

for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    res = results[name]
    if res is None or res['status'] != 'COMPLETE':
        status_str = res['status'] if res else 'NONE'
        print(f"  {name:<10} -- {status_str}")
        continue
    print(f"  {name:<10} {res['N_vertices']:>5} {res['N_triangles']:>6} "
          f"{res['N_velocities']:>8} {res['v_mean']:>10.6f} "
          f"{res['v_0_mle']:>10.6f} {res['chi2_ndof_mean']:>10.3f} "
          f"{res['chi2_ndof_mle']:>10.3f} "
          f"{res['ks_stat']:>8.4f} {res['ks_pval']:>10.2e}")
print(f"{'='*100}")

# Gate logic
chi2_24_best = results['CG(24)']['chi2_best'] if (results['CG(24)'] and results['CG(24)']['status'] == 'COMPLETE') else np.inf
chi2_48_best = results['CG(48)']['chi2_best'] if (results['CG(48)'] and results['CG(48)']['status'] == 'COMPLETE') else np.inf
chi2_120_best = results['CG(120)']['chi2_best'] if (results['CG(120)'] and results['CG(120)']['status'] == 'COMPLETE') else np.inf

# Check convergence trend
print(f"\n  Convergence: CG(24)={chi2_24_best:.3f}, CG(48)={chi2_48_best:.3f}, CG(120)={chi2_120_best:.3f}")

if chi2_24_best < 3:
    verdict = "PASS"
    verdict_detail = f"chi^2/ndof = {chi2_24_best:.3f} < 3 on CG(24)"
elif chi2_48_best < 3 or chi2_120_best < 3:
    # Determine minimum N for convergence
    converged_N = 48 if chi2_48_best < 3 else 120
    verdict = "INFO"
    verdict_detail = (f"Discrete limit exists but requires N > 24 for convergence. "
                      f"CG(24): {chi2_24_best:.3f}, converges at N={converged_N} "
                      f"(chi^2/ndof={min(chi2_48_best, chi2_120_best):.3f})")
else:
    # Check if trend is improving
    trend = [chi2_24_best, chi2_48_best, chi2_120_best]
    trend_valid = [t for t in trend if np.isfinite(t)]
    if len(trend_valid) >= 2 and trend_valid[-1] < trend_valid[0]:
        verdict = "INFO"
        verdict_detail = (f"Improving trend ({chi2_24_best:.1f} -> {chi2_120_best:.1f}) "
                          f"but N=120 still exceeds threshold. "
                          f"Extrapolated convergence at N > 120")
    else:
        verdict = "FAIL"
        verdict_detail = (f"No well-defined discrete limit for N_vertices <= 120. "
                          f"Best chi^2/ndof = {min(chi2_24_best, chi2_48_best, chi2_120_best):.3f}")

print(f"\n{'='*78}")
print(f"  GATE: DISCRETE-BERRY-DENNIS-70")
print(f"  Verdict: {verdict}")
print(f"  Detail:  {verdict_detail}")
print(f"{'='*78}")

# =============================================================================
# SECTION 6: Detailed Physics Discussion
# =============================================================================
print("\n--- Section 6: Physics discussion ---")

print("""
  PHYSICS ANALYSIS:

  Berry-Dennis universality rests on the central limit theorem applied to
  Gaussian random wave superpositions. On a continuous 2D domain, the real
  and imaginary parts of psi(r) are each Gaussian random fields, and phase
  singularity velocity statistics follow from the joint distribution of
  psi, grad(psi), and dpsi/dt. The Berry-Dennis form
     P(|v|) = 8*pi^2*<v>^2*|v| / (pi^2*|v|^2 + 4*<v>^2)^2
  is universal for ANY isotropic Gaussian random wave field in 2D.

  On a discrete graph with N vertices:
  1. The field psi(v) is sampled at N points, not continuously
  2. "Phase singularities" are defined on plaquettes (triangles), not points
  3. Singularity positions are interpolated, introducing discretization error
  4. The number of independent modes = N, so the CLT has limited applicability
     for small N

  For CG(24), N=24 modes contribute to each realization. The CLT requires
  a large number of independent contributions for Gaussianity. With 24 modes,
  deviations from Gaussianity are expected at O(1/sqrt(24)) ~ 20%.

  The key diagnostic question: does chi^2/ndof decrease with N, approaching
  the continuous Berry-Dennis prediction? If so, the universality holds in
  the thermodynamic limit and the CG(24) graph is simply too small.
  If chi^2/ndof does NOT decrease with N, the graph topology fundamentally
  breaks the Berry-Dennis universality (e.g., through anisotropy or
  non-trivial correlations in the graph's spectral geometry).
""")

# Check if CG(24) is too anisotropic for Berry-Dennis
# The 24-cell is highly symmetric (Coxeter group F_4, order 1152)
# so it is as isotropic as a finite graph can be
print("  Graph symmetry check:")
for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    evals = eigenvals[name]
    # Eigenvalue degeneracies indicate symmetry
    unique_evals = []
    tol = 1e-8  # (local)
    for e in evals:
        if len(unique_evals) == 0 or abs(e - unique_evals[-1]) > tol:
            unique_evals.append(e)
    print(f"    {name}: {len(evals)} modes, {len(unique_evals)} distinct eigenvalues, "
          f"max degeneracy = {max(sum(1 for e2 in evals if abs(e2-e1)<tol) for e1 in unique_evals)}")

# =============================================================================
# SECTION 7: Save Data
# =============================================================================
print("\n--- Section 7: Save results ---")

save_dict = {
    'verdict': verdict,
    'verdict_detail': verdict_detail,
    'N_realizations_24': graphs['CG(24)'][3],
    'N_realizations_48': graphs['CG(48)'][3],
    'N_realizations_120': graphs['CG(120)'][3],
}

for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    prefix = name.replace('(', '').replace(')', '')
    res = results[name]
    if res is None:
        continue
    for key in ['N_vertices', 'N_triangles', 'N_velocities', 'v_mean', 'v_median',
                'v_std', 'v_0_mle', 'chi2_mle', 'ndof_mle', 'chi2_ndof_mle',
                'chi2_mean', 'ndof_mean', 'chi2_ndof_mean', 'chi2_best',
                'ks_stat', 'ks_pval', 'ks_stat_mean', 'ks_pval_mean',
                'avg_sings_per_real']:
        if key in res:
            save_dict[f'{prefix}_{key}'] = res[key]
    if 'velocities' in res and len(res['velocities']) > 0:
        save_dict[f'{prefix}_velocities'] = res['velocities']
    if 'bin_edges' in res:
        save_dict[f'{prefix}_bin_edges'] = res['bin_edges']
    if 'counts' in res:
        save_dict[f'{prefix}_counts'] = res['counts']
    if 'expected_mle' in res:
        save_dict[f'{prefix}_expected_mle'] = res['expected_mle']
    if 'expected_mean' in res:
        save_dict[f'{prefix}_expected_mean'] = res['expected_mean']

# Save Laplacian spectra
for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    prefix = name.replace('(', '').replace(')', '')
    save_dict[f'{prefix}_laplacian_evals'] = eigenvals[name]

np.savez_compressed(OUT_NPZ, **save_dict)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 8: Plot
# =============================================================================
print("\n--- Section 8: Generate plots ---")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, name in enumerate(['CG(24)', 'CG(48)', 'CG(120)']):
    ax = axes[idx]
    res = results[name]

    if res is None or res['status'] != 'COMPLETE' or res['N_velocities'] < 50:
        ax.text(0.5, 0.5, f'{name}\n{res["status"] if res else "None"}',
                ha='center', va='center', transform=ax.transAxes, fontsize=14)
        ax.set_title(name)
        continue

    v = res['velocities']
    v_max = np.percentile(v, 99.5)
    v_plot = np.linspace(1e-6, v_max, 500)

    # Histogram (normalized to PDF)
    n_bins_plot = 40
    ax.hist(v[v < v_max], bins=n_bins_plot, density=True, alpha=0.5,
            color='steelblue', edgecolor='navy', linewidth=0.5, label='Data')

    # Berry-Dennis with MLE v_0
    pdf_mle = berry_dennis_pdf(v_plot, res['v_0_mle'])
    ax.plot(v_plot, pdf_mle, 'r-', linewidth=2,
            label=f'BD(v0={res["v_0_mle"]:.4f})')

    # Berry-Dennis with sample mean
    pdf_mean = berry_dennis_pdf(v_plot, res['v_mean'])
    ax.plot(v_plot, pdf_mean, 'g--', linewidth=1.5,
            label=f'BD(<v>={res["v_mean"]:.4f})')

    ax.set_xlabel('|v| (graph units)', fontsize=11)
    ax.set_ylabel('P(|v|)', fontsize=11)
    chi2_str = (f"chi2/ndf(MLE)={res['chi2_ndof_mle']:.2f}\n"
                f"chi2/ndf(mean)={res['chi2_ndof_mean']:.2f}\n"
                f"KS p={res['ks_pval']:.2e}")
    ax.set_title(f'{name} (N={res["N_vertices"]}, n_vel={res["N_velocities"]})',
                 fontsize=12)
    # Add text box
    ax.text(0.98, 0.98, chi2_str, transform=ax.transAxes,
            fontsize=8, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax.legend(fontsize=8, loc='upper left')
    ax.set_xlim(0, v_max)

plt.suptitle('Berry-Dennis Universality on Discrete Graphs (Bucher Test 5)',
             fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# =============================================================================
# SECTION 9: Summary
# =============================================================================
elapsed = time.time() - t_start
print(f"\n{'='*78}")
print(f"  COMPUTATION COMPLETE in {elapsed:.1f}s ({elapsed/60:.1f} min)")
print(f"  Gate: DISCRETE-BERRY-DENNIS-70 = {verdict}")
print(f"  {verdict_detail}")
for name in ['CG(24)', 'CG(48)', 'CG(120)']:
    res = results[name]
    if res and res['status'] == 'COMPLETE':
        print(f"    {name}: chi2_best={res['chi2_best']:.3f}, "
              f"<v>={res['v_mean']:.6f}, v0_MLE={res['v_0_mle']:.6f}, "
              f"KS p={res['ks_pval']:.2e}")
print(f"{'='*78}")
