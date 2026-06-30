#!/usr/bin/env python3
"""
S55 PL-DUAL-CONNES-55: Connes Distance on AN Dual Graph (T-Duality Test)
=========================================================================

Gate: PL-DUAL-CONNES-55
Agent: string-theory-theorist
Session: 55

Physics:
  The CG graph (Clebsch-Gordan graph on SU(3) irreps) is a simplicial complex
  with vertices = irreps, edges = CG-allowed transitions. Its Poincare-Lefschetz
  (PL) dual has:
    - Vertices = edges of CG graph (93 vertices)
    - Edges = pairs of CG edges sharing a triangular face (81 triangles -> 243 dual edges)

  In string theory, T-duality on a torus of radius R maps to a dual torus of
  radius alpha'/R, so d * d_dual = alpha' = const. The question is whether
  the CG/AN pair of dual graphs exhibits a T-duality-like relation:

    d_Connes(CG, tau) * d_Connes(AN, tau) = const(tau)?

  If yes: the CG graph has a T-duality structure at the combinatorial level.
  If no: the product's tau-dependence encodes information about the duality.

Method:
  1. Load CG graph from s54_connes_latt.npz (32 vertices, 93 edges)
  2. Enumerate all triangular faces (3-cliques) in the CG graph
  3. Build AN dual graph: 93 vertices, 243 edges
  4. Build tight-binding Dirac operator on AN graph with sector-dependent
     hopping from s54_tb_hamiltonian.npz
  5. Compute Connes distances:
     a) Graph-distance (resistance metric = lower bound) for all 4278 pairs
     b) Full SDP for 50 representative pairs (verification)
  6. Test constancy of d(CG) * d(AN)

Author: String-Theory-Theorist (Session 55)
"""

import numpy as np
import sys
import os
import time
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold

# ── Paths ──────────────────────────────────────────────────────────────
PROJ = os.path.dirname(os.path.abspath(__file__))
CG_FILE = os.path.join(PROJ, "s54_connes_latt.npz")
TB_FILE = os.path.join(PROJ, "s54_tb_hamiltonian.npz")
OUTPUT_NPZ = os.path.join(PROJ, "s55_pl_dual_connes.npz")
OUTPUT_PNG = os.path.join(PROJ, "s55_pl_dual_connes.png")


# ======================================================================
# SECTION 1: BUILD THE PL DUAL GRAPH
# ======================================================================

def build_pl_dual(adj):
    """
    Build the PL dual graph from the CG adjacency matrix.

    Dual vertices = edges of the CG graph.
    Dual edges = pairs of CG edges that co-bound a triangular face.

    Returns:
      edges_list, edge_to_idx, dual_adj, triangles
    """
    N = adj.shape[0]

    # Enumerate edges
    edges_list = []
    for i in range(N):
        for j in range(i+1, N):
            if adj[i, j] > 0:
                edges_list.append((i, j))
    edge_to_idx = {e: idx for idx, e in enumerate(edges_list)}
    n_edges = len(edges_list)

    # Enumerate triangles (3-cliques)
    triangles = []
    for i in range(N):
        for j in range(i+1, N):
            if adj[i, j] == 0:
                continue
            for k in range(j+1, N):
                if adj[i, k] > 0 and adj[j, k] > 0:
                    triangles.append((i, j, k))

    # Build dual adjacency
    dual_adj = np.zeros((n_edges, n_edges), dtype=np.int8)
    for tri in triangles:
        i, j, k = tri
        tri_edges = [tuple(sorted([i, j])), tuple(sorted([i, k])), tuple(sorted([j, k]))]
        tri_indices = [edge_to_idx[e] for e in tri_edges]
        for a in range(3):
            for b in range(a+1, 3):
                dual_adj[tri_indices[a], tri_indices[b]] = 1
                dual_adj[tri_indices[b], tri_indices[a]] = 1

    return edges_list, edge_to_idx, dual_adj, triangles


# ======================================================================
# SECTION 2: DUAL HAMILTONIAN
# ======================================================================

def build_dual_hamiltonian(dual_adj, edges_list, casimirs, J_C2, J_su2, J_u1,
                            adj_C2, adj_su2, adj_u1):
    """
    Build tight-binding Hamiltonian on the PL dual graph.

    On-site: epsilon_alpha = (C2(i) + C2(j)) / 2  (CG edge endpoints)
    Hopping: t_{alpha,beta} = -sqrt(|J(e_a) * J(e_b)|)  (geometric mean of CG sector hoppings)
    """
    N_dual = dual_adj.shape[0]
    H = np.zeros((N_dual, N_dual))

    # On-site energies
    for alpha, (i, j) in enumerate(edges_list):
        H[alpha, alpha] = (casimirs[i] + casimirs[j]) / 2.0

    # CG edge -> hopping amplitude
    def edge_hopping(i, j):
        ii, jj = min(i, j), max(i, j)
        if adj_C2[ii, jj] > 0:
            return J_C2
        elif adj_su2[ii, jj] > 0:
            return J_su2
        elif adj_u1[ii, jj] > 0:
            return J_u1
        return 0.0

    # Dual hopping
    for alpha in range(N_dual):
        for beta in range(alpha+1, N_dual):
            if dual_adj[alpha, beta] == 0:
                continue
            e_a = edges_list[alpha]
            e_b = edges_list[beta]
            J_a = edge_hopping(e_a[0], e_a[1])
            J_b = edge_hopping(e_b[0], e_b[1])
            t_ab = np.sqrt(np.abs(J_a * J_b))
            H[alpha, beta] = -t_ab
            H[beta, alpha] = -t_ab

    return H


# ======================================================================
# SECTION 3: CONNES DISTANCES
# ======================================================================

def connes_graph_distance(D_off):
    """
    Compute graph-distance (resistance metric) as a lower bound on Connes distance.

    For adjacent vertices: d(i,j) >= 1/|D_{ij}|
    For non-adjacent: d(i,j) >= shortest weighted path in resistance metric.

    This is the EXACT Connes distance for tree graphs, and a lower bound
    for graphs with cycles.
    """
    from scipy.sparse.csgraph import shortest_path

    connected = np.abs(D_off) > 1e-15
    weights = np.full_like(D_off, np.inf)
    weights[connected] = 1.0 / np.abs(D_off[connected])
    return shortest_path(weights, directed=False)


def connes_sdp_distances(D_off, pairs, label=""):
    """
    Compute exact Connes distances via SDP for specified pairs.

    d(i,j) = sup{|f_i - f_j| : ||[D, diag(f)]||_op <= 1}
    Formulated as SDP with Schur complement.
    """
    import cvxpy as cp

    N = D_off.shape[0]

    # Build basis matrices
    E_list = []
    for k in range(N):
        ek = np.zeros(N)
        ek[k] = 1.0
        Ek = np.outer(ek, ek) @ D_off - D_off @ np.outer(ek, ek)
        E_list.append(Ek)

    # Parametric SDP
    f_var = cp.Variable(N)
    c_param = cp.Parameter(N)
    M_mat = sum(f_var[k] * E_list[k] for k in range(N))
    I_n = np.eye(N)
    top = cp.hstack([I_n, M_mat])
    bot = cp.hstack([-M_mat, I_n])
    big = cp.vstack([top, bot])
    prob = cp.Problem(cp.Maximize(c_param @ f_var), [big >> 0])

    # Warm compile
    c_val = np.zeros(N)
    c_val[pairs[0][0]] = 1.0
    c_val[pairs[0][1]] = -1.0
    c_param.value = c_val
    prob.solve(solver=cp.SCS, verbose=False, max_iters=10000)

    distances = np.zeros(len(pairs))
    for pidx, (i, j) in enumerate(pairs):
        c_val = np.zeros(N)
        c_val[i] = 1.0
        c_val[j] = -1.0
        c_param.value = c_val
        try:
            prob.solve(solver=cp.SCS, verbose=False, warm_start=True, max_iters=10000)
            if prob.status not in ['infeasible', 'unbounded', None] and prob.value is not None:
                distances[pidx] = max(prob.value, 0.0)
            else:
                distances[pidx] = np.nan
        except Exception:
            distances[pidx] = np.nan

        if (pidx + 1) % 25 == 0:
            print(f"    {label} SDP pair {pidx+1}/{len(pairs)}")

    return distances


# ======================================================================
# SECTION 4: MAIN COMPUTATION
# ======================================================================

def main():
    print("=" * 72)
    print("S55 PL-DUAL-CONNES-55: Connes Distance on AN Dual Graph")
    print("T-Duality Test: d(CG) * d(AN) =? const")
    print("=" * 72)

    # ── Load ──────────────────────────────────────────────────────────
    cg = np.load(CG_FILE, allow_pickle=True)
    tb = np.load(TB_FILE, allow_pickle=True)

    adj_cg = cg['adjacency']
    cell_labels = cg['cell_labels']
    cell_dims = cg['cell_dims']
    cg_tau = cg['tau_values']
    cg_mean_d = cg['mean_distance']
    cg_max_d = cg['max_distance']
    cg_min_d = cg['min_distance']
    cg_dist_matrices = cg['distance_matrix']

    casimirs = tb['cell_casimirs']
    all_tau_tb = tb['tau_values']
    adj_C2 = tb['adj_C2']
    adj_su2 = tb['adj_su2']
    adj_u1 = tb['adj_u1']

    N_cg = adj_cg.shape[0]
    print(f"\nCG graph: {N_cg} vertices, {adj_cg.sum()//2} edges")
    print(f"CG mean d: {cg_mean_d}")

    # ── Build PL dual ─────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("STEP 1: Build PL Dual Graph")
    print(f"{'='*72}")

    edges_list, edge_to_idx, dual_adj, triangles = build_pl_dual(adj_cg)
    N_dual = len(edges_list)
    N_dual_edges = dual_adj.sum() // 2
    N_triangles = len(triangles)
    dual_degrees = dual_adj.sum(axis=1)

    print(f"  CG edges (= AN dual vertices):   {N_dual}")
    print(f"  CG triangles:                     {N_triangles}")
    print(f"  AN dual edges:                    {N_dual_edges}")
    print(f"  Dual degree: min={dual_degrees.min()}, max={dual_degrees.max()}, "
          f"mean={dual_degrees.mean():.2f}")

    # Connectivity
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse import csr_matrix
    n_comp, comp_labels = connected_components(csr_matrix(dual_adj), directed=False)
    comp_sizes = sorted([np.sum(comp_labels == c) for c in range(n_comp)], reverse=True)
    print(f"  Connected components: {n_comp}")
    print(f"  Component sizes: {comp_sizes}")

    # Edge-type statistics in the dual
    edge_types = {'C2': 0, 'su2': 0, 'u1': 0}
    for (i, j) in edges_list:
        if adj_C2[i, j] > 0: edge_types['C2'] += 1
        elif adj_su2[i, j] > 0: edge_types['su2'] += 1
        elif adj_u1[i, j] > 0: edge_types['u1'] += 1
    print(f"  CG edge types -> dual vertices: C2={edge_types['C2']}, "
          f"su2={edge_types['su2']}, u1={edge_types['u1']}")

    # ── Select SDP pairs ──────────────────────────────────────────────
    # For SDP verification: 50 pairs sampled uniformly, including
    # nearest neighbors and some long-range pairs
    N_SDP = 50
    rng = np.random.RandomState(42)
    all_dual_pairs = [(a, b) for a in range(N_dual) for b in range(a+1, N_dual)]
    sdp_sample_idx = rng.choice(len(all_dual_pairs), min(N_SDP, len(all_dual_pairs)), replace=False)
    sdp_pairs = [all_dual_pairs[k] for k in sorted(sdp_sample_idx)]
    print(f"\n  SDP verification pairs: {len(sdp_pairs)}")

    # ── Compute at all tau ────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("STEP 2: Compute AN Dual Connes Distances")
    print(f"{'='*72}")

    tau_values = cg_tau.copy()
    tau_indices_tb = [int(np.argmin(np.abs(all_tau_tb - t))) for t in tau_values]
    n_tau = len(tau_values)
    print(f"  Tau values: {[f'{t:.4f}' for t in tau_values]}")

    # Storage
    graph_mean_d = np.zeros(n_tau)
    graph_max_d = np.zeros(n_tau)
    graph_min_d = np.zeros(n_tau)
    graph_median_d = np.zeros(n_tau)
    sdp_mean_d = np.zeros(n_tau)
    sdp_all = np.zeros((n_tau, len(sdp_pairs)))
    graph_all_dists = []  # flat arrays for each tau

    t_total = time.time()

    for t_idx in range(n_tau):
        tau = tau_values[t_idx]
        tb_idx = tau_indices_tb[t_idx]
        print(f"\n--- tau = {tau:.4f} ({t_idx+1}/{n_tau}) ---")

        J_C2 = tb['J_C2_tau'][tb_idx]
        J_su2 = tb['J_su2_tau'][tb_idx]
        J_u1 = tb['J_u1_tau'][tb_idx]
        print(f"  J_C2={J_C2:.6f}, J_su2={J_su2:.6f}, J_u1={J_u1:.6f}")

        H_dual = build_dual_hamiltonian(
            dual_adj, edges_list, casimirs, J_C2, J_su2, J_u1,
            adj_C2, adj_su2, adj_u1
        )
        D_off = H_dual - np.diag(np.diag(H_dual))

        # a) Graph-distance for all pairs
        t0 = time.time()
        d_graph = connes_graph_distance(D_off)
        t_g = time.time() - t0

        upper = np.triu(np.ones(N_dual, dtype=bool)[:, None] & np.ones(N_dual, dtype=bool)[None, :], k=1)
        finite = np.isfinite(d_graph) & (d_graph > 0) & upper
        d_vals = d_graph[finite]

        if len(d_vals) > 0:
            graph_mean_d[t_idx] = np.mean(d_vals)
            graph_max_d[t_idx] = np.max(d_vals)
            graph_min_d[t_idx] = np.min(d_vals)
            graph_median_d[t_idx] = np.median(d_vals)
        else:
            graph_mean_d[t_idx] = np.nan
            graph_max_d[t_idx] = np.nan
            graph_min_d[t_idx] = np.nan
            graph_median_d[t_idx] = np.nan

        graph_all_dists.append(d_vals.copy())
        n_inf = np.sum(~np.isfinite(d_graph[upper]))
        print(f"  Graph: mean={graph_mean_d[t_idx]:.6f}, median={graph_median_d[t_idx]:.6f}, "
              f"min={graph_min_d[t_idx]:.6f}, max={graph_max_d[t_idx]:.6f} "
              f"[{t_g:.3f}s, {n_inf} inf]")

        # b) SDP for verification subset
        t0 = time.time()
        sdp_d = connes_sdp_distances(D_off, sdp_pairs, label=f"tau={tau:.3f}")
        t_s = time.time() - t0
        sdp_all[t_idx] = sdp_d

        valid_sdp = sdp_d[~np.isnan(sdp_d)]
        if len(valid_sdp) > 0:
            sdp_mean_d[t_idx] = np.mean(valid_sdp)
        else:
            sdp_mean_d[t_idx] = np.nan

        # Compare SDP vs graph for same pairs
        graph_for_sdp = np.array([d_graph[i, j] for i, j in sdp_pairs])
        both_valid = ~np.isnan(sdp_d) & np.isfinite(graph_for_sdp) & (graph_for_sdp > 0)
        if np.sum(both_valid) > 0:
            ratios = sdp_d[both_valid] / graph_for_sdp[both_valid]
            print(f"  SDP: mean={sdp_mean_d[t_idx]:.6f} [{t_s:.1f}s]. "
                  f"SDP/graph ratio: mean={np.mean(ratios):.4f}, "
                  f"range=[{np.min(ratios):.4f}, {np.max(ratios):.4f}]")
        else:
            print(f"  SDP: mean={sdp_mean_d[t_idx]:.6f} [{t_s:.1f}s]")

    t_total = time.time() - t_total
    print(f"\nTotal: {t_total:.1f}s ({t_total/60:.1f} min)")

    # ── T-Duality Product ─────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("STEP 3: T-Duality Product Test")
    print(f"{'='*72}")

    product_graph = cg_mean_d * graph_mean_d
    product_sdp = cg_mean_d * sdp_mean_d

    # Also test with max distances and min distances
    product_max = cg_max_d * graph_max_d
    product_min = cg_min_d * graph_min_d

    print(f"\n{'tau':>8s} | {'<d_CG>':>10s} | {'<d_AN>_gr':>10s} | {'<d_AN>_sdp':>10s} | "
          f"{'prod_gr':>10s} | {'prod_sdp':>10s}")
    print("-" * 75)

    for t_idx in range(n_tau):
        print(f"{tau_values[t_idx]:8.4f} | {cg_mean_d[t_idx]:10.6f} | "
              f"{graph_mean_d[t_idx]:10.6f} | {sdp_mean_d[t_idx]:10.6f} | "
              f"{product_graph[t_idx]:10.6f} | {product_sdp[t_idx]:10.6f}")

    # Product statistics
    for name, prod in [("Graph product", product_graph), ("SDP product", product_sdp),
                       ("Max product", product_max), ("Min product", product_min)]:
        v = prod[~np.isnan(prod)]
        if len(v) < 2:
            print(f"\n{name}: INSUFFICIENT DATA")
            continue
        m = np.mean(v)
        s = np.std(v)
        rv = s / m if m > 0 else 0
        print(f"\n{name}:")
        print(f"  Mean: {m:.6f}, Std: {s:.6f}, Rel std: {rv*100:.2f}%")
        print(f"  Range: [{v.min():.6f}, {v.max():.6f}]")

    pg_valid = product_graph[~np.isnan(product_graph)]
    pg_mean = np.mean(pg_valid) if len(pg_valid) > 0 else np.nan
    pg_std = np.std(pg_valid) if len(pg_valid) > 0 else np.nan
    pg_rel_var = pg_std / pg_mean if pg_mean > 0 else np.nan

    # ── Scaling Analysis ──────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("STEP 4: Scaling Analysis")
    print(f"{'='*72}")

    # Log-log fit: d_AN = A * d_CG^beta
    valid = (~np.isnan(graph_mean_d) & ~np.isnan(cg_mean_d) &
             (cg_mean_d > 0) & (graph_mean_d > 0))
    if np.sum(valid) >= 3:
        log_cg = np.log(cg_mean_d[valid])
        log_an = np.log(graph_mean_d[valid])
        slope, intercept = np.polyfit(log_cg, log_an, 1)
        print(f"  Log-log fit: log(d_AN) = {slope:.6f} * log(d_CG) + {intercept:.6f}")
        print(f"  Power law: d_AN ~ d_CG^{slope:.4f}")
        print(f"  T-duality slope: -1.0, actual: {slope:.4f}, deviation: {abs(slope+1):.4f}")
        if slope < 0:
            alpha_prime_eff = np.exp(intercept / (1 - slope))  # from d_AN * d_CG^{-slope} = const
            print(f"  If T-duality: effective alpha' = exp(intercept) = {np.exp(intercept):.6f}")
    else:
        slope = np.nan
        print(f"  Insufficient data for scaling fit")

    # Product vs tau: linear fit
    if len(pg_valid) >= 3:
        tau_v = tau_values[~np.isnan(product_graph)]
        lfit = np.polyfit(tau_v, pg_valid, 1)
        print(f"\n  Product linear: P(tau) = {lfit[0]:.6f}*tau + {lfit[1]:.6f}")
        print(f"  Slope/mean product: {abs(lfit[0])/pg_mean:.4f} ({abs(lfit[0])/pg_mean*100:.2f}% per unit tau)")

    # ── Monotonicity ──────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("STEP 5: Monotonicity")
    print(f"{'='*72}")

    for name, arr in [('CG <d>', cg_mean_d), ('AN <d> graph', graph_mean_d),
                       ('AN <d> SDP', sdp_mean_d), ('Product graph', product_graph)]:
        v = arr[~np.isnan(arr)]
        if len(v) < 3:
            print(f"  {name:20s}: INSUFFICIENT DATA")
            continue
        diffs = np.diff(v)
        tol = 1e-10 * np.max(np.abs(v))  # (local)
        if np.all(diffs > -tol):
            mono = "INCREASING"
        elif np.all(diffs < tol):
            mono = "DECREASING"
        else:
            sc = np.where(np.diff(np.sign(diffs)))[0]
            mono = f"NON-MONOTONE (turns at indices {sc})"
        rv = np.std(v) / np.mean(v) * 100
        print(f"  {name:20s}: {mono}, rel_var={rv:.2f}%")

    # ── Per-pair T-duality check ──────────────────────────────────────
    # For the SDP pairs, compute d_CG(i',j') * d_AN(alpha,beta) at each tau
    # where (i',j') are the CG vertices closest to the dual pair
    # This is more nuanced: d_CG and d_AN live on different graphs.
    # The global mean product is the meaningful comparison.

    # ── Gate verdict ──────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("GATE VERDICT: PL-DUAL-CONNES-55")
    print(f"{'='*72}")

    T_STRICT = 0.01  # (local)
    T_APPROX = 0.05  # (local)
    T_LOOSE = 0.15  # (local)

    if np.isfinite(pg_rel_var):
        if pg_rel_var < T_STRICT:
            constancy = "CONSTANT (<1% var) -- T-DUALITY-LIKE"
        elif pg_rel_var < T_APPROX:
            constancy = f"APPROXIMATELY CONSTANT ({pg_rel_var*100:.1f}% var)"
        elif pg_rel_var < T_LOOSE:
            constancy = f"WEAKLY TAU-DEPENDENT ({pg_rel_var*100:.1f}% var)"
        else:
            constancy = f"STRONGLY TAU-DEPENDENT ({pg_rel_var*100:.1f}% var)"
    else:
        constancy = "INSUFFICIENT DATA"

    slope_s = f"{slope:.3f}" if np.isfinite(slope) else "N/A"
    gmin = graph_mean_d[~np.isnan(graph_mean_d)]

    detail = (f"AN dual: {N_dual}v/{N_dual_edges}e from {N_triangles} triangles, "
              f"{n_comp} component(s). "
              f"Product: {constancy}. "
              f"Log-log slope: {slope_s} (T-duality=-1). "
              f"<d_CG>=[{cg_mean_d.min():.3f},{cg_mean_d.max():.3f}], "
              f"<d_AN>=[{gmin.min():.3f},{gmin.max():.3f}].")

    print(f"Verdict: INFO")
    print(f"Detail:  {detail}")

    # ── Save ──────────────────────────────────────────────────────────
    print(f"\n--- Saving ---")
    np.savez(OUTPUT_NPZ,
        tau_values=tau_values,
        cg_mean_distance=cg_mean_d,
        cg_max_distance=cg_max_d,
        cg_min_distance=cg_min_d,
        an_graph_mean_distance=graph_mean_d,
        an_graph_max_distance=graph_max_d,
        an_graph_min_distance=graph_min_d,
        an_graph_median_distance=graph_median_d,
        an_sdp_mean_distance=sdp_mean_d,
        an_sdp_distances=sdp_all,
        product_graph=product_graph,
        product_sdp=product_sdp,
        product_max=product_max,
        product_min=product_min,
        dual_adjacency=dual_adj,
        n_dual_vertices=np.array(N_dual),
        n_dual_edges=np.array(N_dual_edges),
        n_triangles=np.array(N_triangles),
        n_components=np.array(n_comp),
        edges_list=np.array(edges_list),
        log_log_slope=np.array(slope if np.isfinite(slope) else np.nan),
        product_rel_var=np.array(pg_rel_var if np.isfinite(pg_rel_var) else np.nan),
        gate_name=np.array(['PL-DUAL-CONNES-55']),
        gate_verdict=np.array(['INFO']),
        gate_detail=np.array([detail]),
    )
    print(f"Saved: {OUTPUT_NPZ}")

    # ── Plot ──────────────────────────────────────────────────────────
    print(f"\n--- Plotting ---")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('PL-DUAL-CONNES-55: T-Duality Test on CG/AN Dual Graphs  [INFO]',
                 fontsize=14, fontweight='bold')

    # P1: Distances vs tau
    ax = axes[0, 0]
    ax.plot(tau_values, cg_mean_d, 'b-o', lw=2, ms=5, label=r'$\langle d_{CG}\rangle$ (SDP)')
    ax.plot(tau_values, graph_mean_d, 'r-s', lw=2, ms=5, label=r'$\langle d_{AN}\rangle$ (graph)')
    ax.plot(tau_values, sdp_mean_d, 'r--^', lw=1.5, ms=4, alpha=0.7, label=r'$\langle d_{AN}\rangle$ (SDP)')
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7, label='fold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Mean Connes distance')
    ax.set_title('CG and AN Distances')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # P2: Product
    ax = axes[0, 1]
    ax.plot(tau_values, product_graph, 'g-o', lw=2, ms=6, label='graph product')
    ax.plot(tau_values, product_sdp, 'g--^', lw=1.5, ms=4, alpha=0.7, label='SDP product')
    if np.isfinite(pg_mean):
        ax.axhline(pg_mean, color='k', ls='--', alpha=0.5, label=f'mean={pg_mean:.2f}')
        ax.fill_between(tau_values, pg_mean*0.95, pg_mean*1.05,
                         alpha=0.1, color='green', label='5% band')  # (local)
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r"$d_{CG} \cdot d_{AN}$")
    ax.set_title("T-Duality Product")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # P3: Log-log
    ax = axes[0, 2]
    if np.sum(valid) >= 3:
        ax.plot(np.log(cg_mean_d[valid]), np.log(graph_mean_d[valid]), 'ko', ms=6)
        xf = np.linspace(np.log(cg_mean_d[valid].min()), np.log(cg_mean_d[valid].max()), 50)
        ax.plot(xf, slope*xf + intercept, 'r-', lw=1.5, label=f'slope={slope:.3f}')
        # T-duality reference line (slope=-1)
        y0 = np.log(graph_mean_d[valid])[0]
        x0 = np.log(cg_mean_d[valid])[0]
        ax.plot(xf, -xf + (y0 + x0), 'b--', lw=1, alpha=0.5, label='slope=-1 (T-dual)')
    ax.set_xlabel(r'$\ln\langle d_{CG}\rangle$')
    ax.set_ylabel(r'$\ln\langle d_{AN}\rangle$')
    ax.set_title('Log-Log Scaling')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # P4: Dual adjacency
    ax = axes[1, 0]
    im = ax.imshow(dual_adj, cmap='binary', aspect='equal', interpolation='nearest')
    plt.colorbar(im, ax=ax, label='Connected')
    ax.set_title(f'AN Dual Adjacency ({N_dual}x{N_dual})')

    # P5: Ratio
    ax = axes[1, 1]
    ratio = graph_mean_d / cg_mean_d
    ax.plot(tau_values, ratio, 'k-o', lw=2, ms=5)
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\langle d_{AN}\rangle / \langle d_{CG}\rangle$')
    ax.set_title('Distance Ratio')
    ax.grid(True, alpha=0.3)

    # P6: Normalized product
    ax = axes[1, 2]
    if np.isfinite(pg_mean) and pg_mean > 0:
        ax.plot(tau_values, product_graph / pg_mean, 'g-o', lw=2, ms=5)
        ax.axhline(1.0, color='k', ls='--', alpha=0.5)
        ax.fill_between(tau_values, 0.95, 1.05, alpha=0.1, color='green', label='5%')
        ax.fill_between(tau_values, 0.99, 1.01, alpha=0.1, color='blue', label='1%')
    ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r"Product / mean")
    ax.set_title('Normalized Product')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Saved: {OUTPUT_PNG}")

    # ── Summary ───────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("SUMMARY")
    print(f"{'='*72}")
    print(f"AN dual graph: {N_dual} vertices, {N_dual_edges} edges, {N_triangles} triangles")
    print(f"CG <d>: [{cg_mean_d.min():.4f}, {cg_mean_d.max():.4f}]")
    print(f"AN <d>: [{gmin.min():.4f}, {gmin.max():.4f}]")
    if np.isfinite(pg_mean):
        print(f"Product: mean={pg_mean:.6f}, rel_std={pg_rel_var*100:.2f}%")
    if np.isfinite(slope):
        print(f"Log-log slope: {slope:.4f}")
    print(f"Constancy: {constancy}")
    print(f"Gate: PL-DUAL-CONNES-55 -> INFO")
    print(f"Time: {t_total:.1f}s")


if __name__ == '__main__':
    main()
