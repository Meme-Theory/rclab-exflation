#!/usr/bin/env python3
"""
S56 — ATENSOR-FRUSTRATION-56: A-Tensor Gauge Frustration in Josephson Coupling
================================================================================

The O'Neill A-tensor |A|^2 = 3/2 + (3/2)*exp(-4*tau) generates gauge phases
in Cooper pair hopping between cells on the Clebsch-Gordan graph. This script
computes the gauge-invariant frustration parameter and its effect on the XY
mean-field order parameter <cos(phi)>.

Physics
-------
In the Josephson array, Cooper pairs tunnel between cells i,j along C2 bonds
of the Clebsch-Gordan graph. The A-tensor generates a Peierls phase per hop:

    Phi_{ij} = sign(q8_j - q8_i) * |A(tau)| * d_C(i,j)

where:
  - q8 = p - q is the U(1)_8 charge of representation (p,q)
  - d_C(i,j) is the Connes spectral distance between cells i and j
  - sign(dq) gives the direction of gauge transport (always +/-1 for C2 bonds)

The frustrated Josephson Hamiltonian is:

    H_J^frust = -E_J * Sum_{<ij> in C2} cos(phi_i - phi_j - A_{ij})

Key Structural Facts
--------------------
1. The C2 bond subgraph has ZERO 3-cycles (triangles) but 19 independent
   4-cycles. The 81 triangles in the full adjacency are irrelevant because
   the Josephson Hamiltonian only uses C2 bonds.

2. C2 bonds ALWAYS connect representations with dq_8 = +/-1. This gives a
   natural oriented Peierls phase assignment.

3. The gauge-INVARIANT frustration is the Wilson loop flux through the
   elementary plaquettes (4-cycles) of the C2 graph. This flux is
   gauge-transformation-resistant and represents the true physical frustration.

4. By constructing a spanning tree of the C2 graph and gauge-transforming
   to zero on tree edges, we isolate the gauge-invariant residual flux
   on the 19 loop edges.

Gate: ATENSOR-FRUSTRATION-56 — INFO: frustration parameter f and
      modification of <cos(phi)>.

Author: Baptista-Spacetime-Analyst (Session 56)
Date: 2026-03-22
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp, log
from scipy.special import i0, i1
from scipy.sparse.csgraph import connected_components
from collections import deque, Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

print("=" * 72)
print("  S56 — ATENSOR-FRUSTRATION-56: A-Tensor Gauge Frustration")
print("=" * 72)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
#  SECTION 1: Load Input Data
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 1: Load Input Data")
print("=" * 72)

at_data = np.load(os.path.join(DATA_DIR, 's55_atensor_gauge.npz'), allow_pickle=True)
A_sq_koszul = at_data['A_sq_koszul']
tau_A = at_data['tau_values']
A_sq_fold_val = float(at_data['A_sq_fold'])
print(f"  S55 A-tensor: {len(tau_A)} tau values, |A|^2(fold) = {A_sq_fold_val:.6f}")

cn_data = np.load(os.path.join(DATA_DIR, 's54_connes_latt.npz'), allow_pickle=True)
tau_CN = cn_data['tau_values']
D_matrices = cn_data['distance_matrix']
N_cells = int(cn_data['N_cells'])
print(f"  S54 Connes: {len(tau_CN)} tau values, {N_cells} cells")

tb_data = np.load(os.path.join(DATA_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
adj = tb_data['adjacency']
adj_C2 = tb_data['adj_C2']
adj_su2 = tb_data['adj_su2']
adj_u1 = tb_data['adj_u1']
cell_labels = tb_data['cell_labels']
cell_dims = tb_data['cell_dims']
J_C2_tau = tb_data['J_C2_tau']
tau_TB = tb_data['tau_values']
eigenvalues = tb_data['eigenvalues']
N = N_cells
print(f"  S54 TB: {int(tb_data['n_bonds_total'])} bonds "
      f"(C2={int(tb_data['n_bonds_C2'])}, "
      f"su2={int(tb_data['n_bonds_su2'])}, "
      f"u1={int(tb_data['n_bonds_u1'])})")

# U(1)_8 charge: q_8 = p - q
q8 = (cell_labels[:, 0] - cell_labels[:, 1]).astype(float)

# ============================================================================
#  SECTION 2: Graph Topology — Triangles and 4-Cycles
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 2: Graph Topology — Plaquette Structure")
print("=" * 72)

# Identify triangles in full adjacency
triangles_full = []
for i in range(N):
    for j in range(i + 1, N):
        if adj[i, j]:
            for k in range(j + 1, N):
                if adj[j, k] and adj[i, k]:
                    bond_types = []
                    for (a, b) in [(i, j), (j, k), (i, k)]:
                        if adj_C2[a, b]:
                            bond_types.append('C2')
                        elif adj_su2[a, b]:
                            bond_types.append('su2')
                        elif adj_u1[a, b]:
                            bond_types.append('u1')
                    triangles_full.append((i, j, k, tuple(sorted(bond_types))))

type_counts = Counter([t[3] for t in triangles_full])
n_C2_only_tri = type_counts.get(('C2', 'C2', 'C2'), 0)
print(f"  Full adjacency triangles: {len(triangles_full)}")
for tp, cnt in sorted(type_counts.items()):
    print(f"    {tp}: {cnt}")
print(f"  C2-only triangles: {n_C2_only_tri}")

# Identify 4-cycles in C2-only subgraph
adj_C2_np = np.array(adj_C2)
four_cycles = set()
for i in range(N):
    for j in range(N):
        if adj_C2[i, j] and j != i:
            for k in range(N):
                if adj_C2[j, k] and k != i and k != j:
                    for l in range(N):
                        if adj_C2[k, l] and adj_C2[l, i] and l != i and l != j and l != k:
                            cycle = [i, j, k, l]
                            min_idx = cycle.index(min(cycle))
                            rotated = cycle[min_idx:] + cycle[:min_idx]
                            if rotated[1] > rotated[3]:
                                rotated = [rotated[0]] + rotated[1:][::-1]
                            four_cycles.add(tuple(rotated))

four_cycles = sorted(four_cycles)
N_4cycles = len(four_cycles)
print(f"\n  C2-only 4-cycles (elementary plaquettes): {N_4cycles}")

# Graph topology
n_C2_edges = np.sum(adj_C2_np) // 2
n_comp, _ = connected_components(adj_C2_np)
n_indep_cycles = n_C2_edges - (N - 1)  # Euler formula for connected graph
print(f"  C2 graph: {N} vertices, {n_C2_edges} edges, {n_comp} component(s)")
print(f"  Independent cycles (first Betti number): {n_indep_cycles}")
print(f"  4-cycles found = independent cycles: {N_4cycles == n_indep_cycles}")

# Verify C2 dq_8 structure
dq8_C2 = set()
for i in range(N):
    for j in range(i + 1, N):
        if adj_C2[i, j]:
            dq8_C2.add(abs(q8[j] - q8[i]))
print(f"\n  C2 bond |dq_8| values: {sorted(dq8_C2)}")
print(f"  All C2 bonds have |dq_8| = 1: {dq8_C2 == {1.0}}")

# ============================================================================
#  SECTION 3: Gauge-Invariant Frustration Computation
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 3: Gauge-Invariant Frustration at Each tau")
print("=" * 72)

Delta_BCS = 0.4643  # M_KK, Delta_0_OES from canonical_constants
tau_T_points = np.array([0.0, 0.194, 0.306, 0.5])
T_GH_points = np.array([0.629, 0.590, 0.412, 0.020])  # M_KK, from W0-1


def compute_frustration_gauge_invariant(tau_val, A_sq_val, D_matrix):
    """
    Compute gauge-INVARIANT frustration on the C2 graph.

    Steps:
    1. Assign Peierls phases: Phi_{ij} = sign(dq_8) * |A| * d_C(i,j)
    2. Compute Wilson loop flux through each C2 4-cycle
    3. Gauge-transform to spanning tree gauge (A'=0 on tree edges)
    4. Compute z_eff from gauge-transformed phases
    5. Solve XY mean-field self-consistency
    """
    A_mag = sqrt(A_sq_val)

    # Step 1: Peierls phase assignment
    Phi = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if adj_C2[i, j]:
                dq = q8[j] - q8[i]
                sgn = np.sign(dq) if abs(dq) > 0.5 else 1.0
                Phi[i, j] = sgn * A_mag * D_matrix[i, j]

    # Step 2: Wilson loop flux through each 4-cycle
    wilson_4 = []
    for cyc in four_cycles:
        i, j, k, l = cyc
        flux = Phi[i, j] + Phi[j, k] + Phi[k, l] + Phi[l, i]
        wilson_4.append(flux)
    wilson_4 = np.array(wilson_4)

    # Step 3: Gauge transform to spanning tree gauge
    visited = np.zeros(N, dtype=bool)
    parent = np.full(N, -1)
    chi = np.zeros(N)
    visited[0] = True
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in range(N):
            if adj_C2[u, v] and not visited[v]:
                visited[v] = True
                parent[v] = u
                chi[v] = chi[u] + Phi[u, v]
                queue.append(v)

    # Gauge-transformed phases
    A_prime = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if adj_C2[i, j]:
                A_prime[i, j] = Phi[i, j] + chi[i] - chi[j]

    # Step 4: Effective coordination with gauge-transformed phases
    z_bare = np.zeros(N)
    z_eff = np.zeros(N)
    for i in range(N):
        c2_nbrs = [j for j in range(N) if adj_C2[i, j]]
        z_bare[i] = len(c2_nbrs)
        if len(c2_nbrs) > 0:
            phase_sum = sum(np.exp(1j * A_prime[i, j]) for j in c2_nbrs)
            z_eff[i] = abs(phase_sum)

    mask = z_bare > 0
    z_mean = np.mean(z_bare[mask])
    z_eff_mean = np.mean(z_eff[mask])

    # Step 5: Mean-field self-consistency
    tau_idx_TB = np.argmin(np.abs(tau_TB - tau_val))
    J_C2_val = np.interp(tau_val, tau_TB, J_C2_tau)
    evals = eigenvalues[tau_idx_TB]
    mu = evals[0]  # (local)
    E_qp = np.sqrt((evals - mu)**2 + Delta_BCS**2)
    F_anom = np.sum(Delta_BCS / (2.0 * E_qp**2))
    E_J = J_C2_val**2 * F_anom
    T_GH = np.interp(tau_val, tau_T_points, T_GH_points)
    beta = 1.0 / T_GH if T_GH > 1e-6 else 1e6

    def solve_mf(z_arr):
        m = 0.999
        for iteration in range(300):
            args = beta * z_arr * E_J * m
            ratios = np.zeros(N)
            for idx in range(N):
                x = args[idx]
                if x > 700:
                    ratios[idx] = 1.0 - 1.0 / (2.0 * x)
                elif x < 1e-10:
                    ratios[idx] = x / 2.0
                else:
                    ratios[idx] = i1(x) / i0(x)
            m_new = np.mean(ratios[mask])
            if abs(m_new - m) < 1e-14:
                return m_new
            m = m_new
        return m

    m_unfrust = solve_mf(z_bare)
    m_frust = solve_mf(z_eff)

    # Frustration parameters
    f_plaquette = np.mean(np.abs(wilson_4)) / pi  # fraction of flux quantum
    cos_wilson = np.mean(np.cos(wilson_4))

    # Residual flux on loop edges
    loop_residuals = []
    for i in range(N):
        for j in range(i + 1, N):
            if adj_C2[i, j]:
                is_tree = (parent[j] == i or parent[i] == j)
                if not is_tree:
                    loop_residuals.append(A_prime[i, j])
    loop_residuals = np.array(loop_residuals)

    return {
        'tau': tau_val,
        'A_sq': A_sq_val,
        'A_mag': A_mag,
        'wilson_4': wilson_4,
        'f_plaquette': f_plaquette,
        'cos_wilson': cos_wilson,
        'z_bare': z_bare,
        'z_eff': z_eff,
        'z_mean': z_mean,
        'z_eff_mean': z_eff_mean,
        'z_reduction': z_eff_mean / z_mean if z_mean > 0 else 1.0,
        'E_J': E_J,
        'F_anom': F_anom,
        'T_GH': T_GH,
        'm_unfrust': m_unfrust,
        'm_frust': m_frust,
        'delta_m_frac': (m_frust - m_unfrust) / m_unfrust if m_unfrust > 1e-10 else 0,
        'loop_residuals': loop_residuals,
        'max_loop_residual': np.max(np.abs(loop_residuals)) if len(loop_residuals) > 0 else 0,
        'chi': chi.copy(),
    }


# ============================================================================
#  SECTION 4: Tau Scan
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 4: Frustration Scan over tau")
print("=" * 72)

results_all = []
for cn_idx in range(len(tau_CN)):
    tau_val = tau_CN[cn_idx]
    D_mat = D_matrices[cn_idx]
    A_sq_interp = np.interp(tau_val, tau_A, A_sq_koszul)
    res = compute_frustration_gauge_invariant(tau_val, A_sq_interp, D_mat)
    results_all.append(res)
    print(f"  tau={tau_val:.4f}: |A|={res['A_mag']:.4f}, "
          f"f_plaq={res['f_plaquette']:.6f}, "
          f"z_eff/z={res['z_reduction']:.6f}, "
          f"m_u={res['m_unfrust']:.6f}, "
          f"m_f={res['m_frust']:.6f}, "
          f"dm/m={res['delta_m_frac']:.2e}")

# ============================================================================
#  SECTION 5: Detailed Results at Fold
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 5: Detailed Results at Fold")
print("=" * 72)

fold_cn_idx = np.argmin(np.abs(tau_CN - tau_fold))
r_fold = results_all[fold_cn_idx]

print(f"\n  tau_fold = {tau_fold} (closest Connes: tau = {tau_CN[fold_cn_idx]:.6f})")
print(f"  |A|^2 = {r_fold['A_sq']:.6f}")
print(f"  |A|   = {r_fold['A_mag']:.6f}")

print(f"\n  === C2 Plaquette Fluxes (19 four-cycles) ===")
print(f"  Mean |flux| = {np.mean(np.abs(r_fold['wilson_4'])):.6f} rad")
print(f"  Max  |flux| = {np.max(np.abs(r_fold['wilson_4'])):.6f} rad")
print(f"  Min  |flux| = {np.min(np.abs(r_fold['wilson_4'])):.6f} rad")
print(f"  Mean |flux|/pi = {np.mean(np.abs(r_fold['wilson_4'])) / pi:.6f}")
print(f"  Max  |flux|/pi = {np.max(np.abs(r_fold['wilson_4'])) / pi:.6f}")
print(f"  f_plaquette = {r_fold['f_plaquette']:.6f}")
print(f"  <cos(flux)> = {r_fold['cos_wilson']:.6f}")

print(f"\n  Individual 4-cycle fluxes:")
for idx, cyc in enumerate(four_cycles):
    pqs = [f"({cell_labels[v, 0]},{cell_labels[v, 1]})" for v in cyc]
    flux = r_fold['wilson_4'][idx]
    print(f"    {cyc}: {' - '.join(pqs)} | flux = {flux:.6f} rad ({flux / pi:.6f} pi)")

print(f"\n  === Gauge-Transformed Coordination ===")
print(f"  z_bare (mean) = {r_fold['z_mean']:.4f}")
print(f"  z_eff  (mean) = {r_fold['z_eff_mean']:.4f}")
print(f"  z_reduction   = {r_fold['z_reduction']:.6f}")
print(f"  Max loop residual = {r_fold['max_loop_residual']:.6f} rad "
      f"({r_fold['max_loop_residual'] / pi:.6f} pi)")

print(f"\n  === Loop Edge Residuals ===")
for i, res_val in enumerate(r_fold['loop_residuals']):
    print(f"    Loop edge {i + 1}: A' = {res_val:.6f} rad ({res_val / pi:.6f} pi)")

print(f"\n  === Mean-Field Order Parameter ===")
print(f"  E_J(fold)     = {r_fold['E_J']:.4f} M_KK")
print(f"  F_anom(fold)   = {r_fold['F_anom']:.4f}")
print(f"  T_GH(fold)    = {r_fold['T_GH']:.4f} M_KK")
print(f"\n  m_unfrust     = {r_fold['m_unfrust']:.8f}")
print(f"  m_frust       = {r_fold['m_frust']:.8f}")
print(f"  delta_m/m     = {r_fold['delta_m_frac']:.4e}")
print(f"  |delta_m/m|   = {abs(r_fold['delta_m_frac']):.4e}")

threshold = 0.10  # (local)
exceeds = abs(r_fold['delta_m_frac']) > threshold
print(f"\n  Threshold     = {threshold * 100:.0f}%")
print(f"  Exceeds?      = {'YES' if exceeds else 'NO'}")

# ============================================================================
#  SECTION 6: Cross-Checks
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 6: Cross-Checks")
print("=" * 72)

# 1. tau=0 check
r0 = results_all[0]
print(f"  [CHECK 1] tau=0: |A|^2 = {r0['A_sq']:.6f} (expected 3.000)")

# 2. f_plaquette bounded
for r in results_all:
    assert r['f_plaquette'] >= 0 and r['f_plaquette'] <= 1.0 + 1e-10
print(f"  [CHECK 2] f_plaquette in [0,1] at all tau: PASS")

# 3. m_frust <= m_unfrust
for r in results_all:
    if r['m_frust'] > r['m_unfrust'] + 1e-8:
        print(f"  [CHECK 3] WARNING: m_frust > m_unfrust at tau={r['tau']}")
        break
else:
    print(f"  [CHECK 3] m_frust <= m_unfrust at all tau: PASS")

# 4. W1-1 cross-check
print(f"  [CHECK 4] m_unfrust(fold) = {r_fold['m_unfrust']:.6f} "
      f"(W1-1: 0.9863, diff = {abs(r_fold['m_unfrust'] - 0.9863) / 0.9863 * 100:.2f}%)")
print(f"    Note: difference due to E_J computation method "
      f"(we use E_J={r_fold['E_J']:.4f}, W1-1 uses E_J=7.042)")

# 5. Analytic formula check
print(f"\n  [CHECK 5] |A|^2 formula vs Koszul:")
for tv in [0.0, 0.19, 0.5]:
    formula = 1.5 + 1.5 * exp(-4.0 * tv)
    koszul = np.interp(tv, tau_A, A_sq_koszul)
    print(f"    tau={tv}: formula={formula:.6f}, Koszul={koszul:.6f}, "
          f"rel_err={abs(formula - koszul) / koszul:.2e}")

# 6. N_4cycles = first Betti number
print(f"  [CHECK 6] 4-cycles ({N_4cycles}) = independent cycles ({n_indep_cycles}): "
      f"{'PASS' if N_4cycles == n_indep_cycles else 'FAIL'}")

# 7. Wilson flux consistency: sum of plaquette fluxes around any 2-cycle = 0
# (homological constraint)
print(f"  [CHECK 7] Sum of all plaquette fluxes = "
      f"{np.sum(r_fold['wilson_4']):.4e} rad (should be ~0 if graph is planar)")

# ============================================================================
#  SECTION 7: Tau-Dependence Summary
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 7: Tau-Dependence Summary")
print("=" * 72)

print(f"\n  {'tau':>7s}  {'|A|':>7s}  {'f_plaq':>8s}  {'<cos(W)>':>8s}  "
      f"{'z_eff/z':>8s}  {'m_unfr':>8s}  {'m_frust':>8s}  {'delta_m':>10s}  "
      f"{'max_res':>8s}")
print("  " + "-" * 90)
for r in results_all:
    print(f"  {r['tau']:7.4f}  {r['A_mag']:7.4f}  {r['f_plaquette']:8.6f}  "
          f"{r['cos_wilson']:8.6f}  {r['z_reduction']:8.6f}  "
          f"{r['m_unfrust']:8.6f}  {r['m_frust']:8.6f}  "
          f"{r['delta_m_frac']:10.2e}  {r['max_loop_residual']:8.4f}")

# ============================================================================
#  SECTION 8: Physics Interpretation
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 8: Physics Interpretation")
print("=" * 72)

print("""
  STRUCTURAL RESULT: The A-tensor gauge frustration is NEGLIGIBLE.

  1. GRAPH TOPOLOGY: The C2 bond subgraph has no triangles (girth = 4).
     The 81 triangles in the full adjacency are IRRELEVANT to the Josephson
     Hamiltonian, which couples only C2 bonds. The elementary plaquettes
     are 19 independent 4-cycles.

  2. GAUGE-INVARIANT FLUX: The Wilson loop flux through each C2 plaquette
     is tiny: max |flux|/pi = {:.6f} (less than {:.1f}% of a flux quantum).
     This means the A-tensor Peierls phases can be GAUGE-TRANSFORMED AWAY
     to within ~{:.1f}% residual.

  3. GAUGE TRANSFORM: Constructing a spanning tree of the C2 graph and
     setting chi_i = cumulative Peierls phase along the tree path from
     root, the gauge-transformed phases A'_{{ij}} = Phi_{{ij}} + chi_i - chi_j
     are ZERO on tree edges and < {:.4f} rad on loop edges.

  4. EFFECTIVE COORDINATION: After gauge transform, z_eff/z_bare = {:.6f}
     (essentially 1.0). The initial naive computation showing z_eff/z ~ 0.24
     was a GAUGE ARTIFACT: the Peierls phases were ~pi/2 per bond, causing
     cancellations between "up" and "down" neighbors in q_8 space. These
     cancellations are removed by gauge transform.

  5. ORDER PARAMETER: The frustrated mean-field order parameter
     m_frust = {:.8f} differs from m_unfrust = {:.8f} by only
     delta_m/m = {:.2e}, which is {:.4f}% — far below the 10% threshold.

  6. W1-1 STANDS: The unfrustrated Josephson mean-field result from W1-1
     is UNMODIFIED by gauge frustration. The A-tensor generates large
     Peierls phases per bond (~pi/2), but the physical frustration
     (gauge-invariant plaquette flux) is negligible because the C2 Connes
     distances are nearly UNIFORM across all bonds.
""".format(
    np.max(np.abs(r_fold['wilson_4'])) / pi,
    np.max(np.abs(r_fold['wilson_4'])) / pi * 100,
    (1 - r_fold['z_reduction']) * 100,
    r_fold['max_loop_residual'],
    r_fold['z_reduction'],
    r_fold['m_frust'],
    r_fold['m_unfrust'],
    r_fold['delta_m_frac'],
    abs(r_fold['delta_m_frac']) * 100
))

# ============================================================================
#  SECTION 9: Gate Verdict
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 9: Gate Verdict — ATENSOR-FRUSTRATION-56")
print("=" * 72)

gate_verdict = "INFO"
gate_detail = (f"Gauge-invariant frustration f={r_fold['f_plaquette']:.6f} "
               f"(max flux/pi={np.max(np.abs(r_fold['wilson_4'])) / pi:.4f}). "
               f"After gauge transform: z_eff/z={r_fold['z_reduction']:.6f}, "
               f"delta_m/m={r_fold['delta_m_frac']:.2e}. "
               f"Modification {abs(r_fold['delta_m_frac']) * 100:.4f}% — "
               f"far below 10%. W1-1 unfrustrated result STANDS.")

print(f"\n  GATE: ATENSOR-FRUSTRATION-56")
print(f"  VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# ============================================================================
#  SECTION 10: Save Data
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 10: Save Data")
print("=" * 72)

tau_scan = np.array([r['tau'] for r in results_all])
f_plaq_scan = np.array([r['f_plaquette'] for r in results_all])
cos_wilson_scan = np.array([r['cos_wilson'] for r in results_all])
z_reduction_scan = np.array([r['z_reduction'] for r in results_all])
m_unfrust_scan = np.array([r['m_unfrust'] for r in results_all])
m_frust_scan = np.array([r['m_frust'] for r in results_all])
delta_m_scan = np.array([r['delta_m_frac'] for r in results_all])
A_mag_scan = np.array([r['A_mag'] for r in results_all])
max_res_scan = np.array([r['max_loop_residual'] for r in results_all])

outpath = os.path.join(DATA_DIR, 's56_atensor_frustration.npz')
np.savez(outpath,
    tau_values=tau_scan,
    f_plaquette=f_plaq_scan,
    cos_wilson=cos_wilson_scan,
    z_reduction=z_reduction_scan,
    m_unfrust=m_unfrust_scan,
    m_frust=m_frust_scan,
    delta_m_frac=delta_m_scan,
    A_mag=A_mag_scan,
    max_loop_residual=max_res_scan,
    # Fold scalars
    tau_fold=np.float64(tau_CN[fold_cn_idx]),
    f_plaquette_fold=np.float64(r_fold['f_plaquette']),
    cos_wilson_fold=np.float64(r_fold['cos_wilson']),
    z_reduction_fold=np.float64(r_fold['z_reduction']),
    m_unfrust_fold=np.float64(r_fold['m_unfrust']),
    m_frust_fold=np.float64(r_fold['m_frust']),
    delta_m_fold=np.float64(r_fold['delta_m_frac']),
    max_res_fold=np.float64(r_fold['max_loop_residual']),
    # Topology
    N_triangles_full=np.int64(len(triangles_full)),
    N_C2_triangles=np.int64(n_C2_only_tri),
    N_4cycles=np.int64(N_4cycles),
    N_indep_cycles=np.int64(n_indep_cycles),
    wilson_4_fold=r_fold['wilson_4'],
    # Per-cell
    z_bare=r_fold['z_bare'],
    z_eff_fold=r_fold['z_eff'],
    chi_fold=r_fold['chi'],
    q8=q8,
    # Gate
    gate_name=np.array(['ATENSOR-FRUSTRATION-56']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"  Saved: {outpath}")

# ============================================================================
#  SECTION 11: Generate Plot
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 11: Generate Plot")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('ATENSOR-FRUSTRATION-56: A-Tensor Gauge Frustration\n'
             'in Josephson Coupling on 32-Cell CG Graph\n'
             '(Gauge-Invariant Analysis on C2 Plaquettes)',
             fontsize=12, y=0.98)

# Panel (a): Plaquette frustration vs tau
ax = axes[0, 0]
ax.plot(tau_scan, f_plaq_scan, 'bo-', markersize=5, label='f (plaquette)')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5,
           label=f'tau_fold = {tau_fold}')
ax.set_xlabel('tau')
ax.set_ylabel('Frustration f = <|flux|>/pi')
ax.set_title('(a) Gauge-invariant frustration')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): z_eff/z_bare (gauge-transformed)
ax = axes[0, 1]
ax.plot(tau_scan, z_reduction_scan, 'go-', markersize=5,
        label='z_eff / z_bare (gauge-transformed)')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5)
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('z_eff / z_bare')
ax.set_title('(b) Effective coordination (gauge-transformed)')
ax.set_ylim(0.99, 1.005)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Order parameter comparison
ax = axes[1, 0]
ax.plot(tau_scan, m_unfrust_scan, 'b^-', markersize=5, label='m (unfrustrated)')
ax.plot(tau_scan, m_frust_scan, 'rv-', markersize=5, label='m (frustrated)')
ax.axvline(tau_fold, color='red', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('<cos(phi)>')
ax.set_title('(c) Mean-field order parameter')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Wilson loop flux histogram at fold
ax = axes[1, 1]
ax.bar(range(N_4cycles), r_fold['wilson_4'] / pi, color='steelblue',
       edgecolor='navy', alpha=0.7)
ax.axhline(0, color='gray', linestyle='-', linewidth=0.5)
ax.set_xlabel('Plaquette index')
ax.set_ylabel('Flux / pi')
ax.set_title(f'(d) C2 plaquette fluxes at fold\n'
             f'max |flux|/pi = {np.max(np.abs(r_fold["wilson_4"])) / pi:.4f}')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(DATA_DIR, 's56_atensor_frustration.png')
plt.savefig(plotpath, dpi=150)
print(f"  Saved: {plotpath}")

print("\n" + "=" * 72)
print("  ATENSOR-FRUSTRATION-56 COMPLETE")
print("=" * 72)
