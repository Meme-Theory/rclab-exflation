#!/usr/bin/env python3
"""
s61_thouless_cayley.py — Thouless Time on CG(24) via Spectral Gap
==================================================================
Gate: GGE-THERM-61
  PASS if t_Th / t_transit > 10
  FAIL if t_Th / t_transit < 0.1
  INFO if in [0.1, 10]

Constructs the Cayley graph of S_4 with generators = all 6 transpositions.
Computes graph Laplacian eigenvalues both:
  (a) Numerically from explicit 24x24 adjacency matrix
  (b) Analytically from character table of S_4
Cross-checks agree.

Then: t_Th = 1 / (E_J * lambda_1), compared to t_transit.
Also: spectral dimension d_s(t) from return probability on CG(24).
"""

import numpy as np
from itertools import permutations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# ── Import framework constants ──────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import omega_tau, dt_transit

# E_J from s60 data (not in canonical_constants)
_s60 = np.load(Path(__file__).resolve().parent / 's60_rg_integrals.npz',
               allow_pickle=True)
E_J = float(_s60['E_J_fold'])  # 3.3969 M_KK

# Transit time
t_transit = dt_transit  # 0.001130 M_KK^{-1}

print("=" * 72)
print("s61_thouless_cayley.py — Thouless Time on CG(24)")
print("=" * 72)
print(f"  E_J       = {E_J:.6f} M_KK")
print(f"  omega_tau = {omega_tau:.4f} M_KK")
print(f"  t_transit = {t_transit:.10e} M_KK^{{-1}}")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 1: Construct CG(24) numerically
# ══════════════════════════════════════════════════════════════════════════════

# Elements of S_4 as tuples (permutations of (0,1,2,3))
elements = list(permutations(range(4)))  # 24 elements
n = len(elements)
assert n == 24, f"Expected 24 elements, got {n}"

# Map each element to an index
elem_to_idx = {p: i for i, p in enumerate(elements)}

# Generators: all 6 transpositions of {0,1,2,3}
# (ij) swaps positions i and j
transpositions = []
for i in range(4):
    for j in range(i+1, 4):
        transpositions.append((i, j))
assert len(transpositions) == 6

def apply_transposition(perm, trans):
    """Apply transposition (i,j) to permutation tuple."""
    i, j = trans
    lst = list(perm)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)

# Build adjacency matrix
A = np.zeros((n, n), dtype=int)
for idx, p in enumerate(elements):
    for t in transpositions:
        q = apply_transposition(p, t)
        jdx = elem_to_idx[q]
        A[idx, jdx] = 1

# Verify: each vertex has degree 6 (transpositions are involutions)
degrees = A.sum(axis=1)
assert np.all(degrees == 6), f"Degree check failed: {degrees}"

# Verify symmetry (Cayley graph of group with symmetric generating set)
assert np.allclose(A, A.T), "Adjacency matrix not symmetric"

# Graph Laplacian L = D - A, where D = diag(degrees) = 6*I
D = np.diag(degrees)
L = D - A

# Numerical eigenvalues
eigvals_num = np.sort(np.linalg.eigvalsh(L.astype(float)))

print("PART 1: Numerical eigenvalues of graph Laplacian")
print(f"  Shape: {L.shape}")
print(f"  Degree: {degrees[0]} (regular graph)")
print(f"  Eigenvalues (sorted):")
# Group by multiplicity
unique_vals = []
tol = 1e-10  # (local)
for v in eigvals_num:
    if len(unique_vals) == 0 or abs(v - unique_vals[-1][0]) > tol:
        unique_vals.append([v, 1])
    else:
        unique_vals[-1][1] += 1
for v, m in unique_vals:
    print(f"    lambda = {v:10.6f}  (multiplicity {m})")
print(f"  Total eigenvalues: {sum(m for _, m in unique_vals)} (should be 24)")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 2: Analytic eigenvalues from character table of S_4
# ══════════════════════════════════════════════════════════════════════════════
#
# S_4 character table:
#   Conjugacy class:  {e}  (12)  (123)  (1234)  (12)(34)
#   Class size:         1    6     8      6        3
#
#   trivial    (d=1):   1    1     1      1        1
#   sign       (d=1):   1   -1     1     -1        1
#   standard   (d=3):   3    1     0     -1       -1
#   sign*std   (d=3):   3   -1     0      1       -1
#   2D         (d=2):   2    0    -1      0        2
#
# For Cayley graph with generating set T = {all 6 transpositions}:
# The eigenvalue of the normalized adjacency operator for irrep rho is:
#   mu_rho = (1/dim(rho)) * sum_{t in T} chi_rho(t)
#
# Since all generators are transpositions (conjugacy class (12), size 6):
#   mu_rho = (6 / dim(rho)) * chi_rho((12))
#           = 6 * chi_rho((12)) / dim(rho)
#
# Laplacian eigenvalue: lambda_rho = |T| - dim(rho) * mu_rho
#                                  = 6 - 6 * chi_rho((12)) ... wait
#
# Actually for the graph Laplacian on a Cayley graph, the eigenvalues
# are lambda_rho = |T| - (sum_{t in T} chi_rho(t)) / dim(rho)
# Each irrep rho of dimension d contributes d^2 eigenvalues, all equal
# to lambda_rho. Total = sum d^2 = 1+1+9+9+4 = 24. Check.
#
# More precisely: the adjacency matrix of a Cayley graph Gamma(G,S) has
# eigenvalues mu_{rho,ij} = (|G|/d_rho) * sum_{s in S} rho(s)_{ij}
# ... but for the purpose of the Laplacian spectrum, each irrep rho
# contributes eigenvalues of L that are:
#   lambda_{rho,k} = |S| - eta_k(rho)
# where eta_k are eigenvalues of the matrix M_rho = sum_{s in S} rho(s)
# (a d_rho x d_rho matrix). For 1D irreps, M_rho is a scalar.
# For higher-dimensional irreps, M_rho may have multiple distinct eigenvalues.

print("PART 2: Analytic eigenvalues from representation theory")
print()

# Character values at transposition (12)
chi_at_trans = {
    'trivial': 1,
    'sign': -1,
    'standard': 1,
    'sign_standard': -1,
    '2D': 0
}
dims = {
    'trivial': 1,
    'sign': 1,
    'standard': 3,
    'sign_standard': 3,
    '2D': 2
}

# For 1D irreps, the Laplacian eigenvalue is exact:
#   lambda = |S| - |S| * chi(trans) = 6(1 - chi(trans))
# For higher-dim irreps, we need M_rho = sum_{s in S} rho(s)

# Let's compute M_rho for each irrep explicitly.

# === Trivial representation (d=1) ===
# rho(s) = 1 for all s
# M = 6 * 1 = 6
# lambda = 6 - 6 = 0  (multiplicity 1)

# === Sign representation (d=1) ===
# rho(trans) = -1
# M = 6 * (-1) = -6
# lambda = 6 - (-6) = 12  (multiplicity 1)

# === Standard representation (d=3) ===
# The standard rep of S_4 acts on V = {(x1,x2,x3,x4) : sum xi = 0}
# For transposition (ij), the matrix permutes coordinates i and j.
# In the basis e1-e4, e2-e4, e3-e4 of V:
# We need M_std = sum of rho_std(t) over all 6 transpositions.
# By Schur's lemma, since the transpositions form a single conjugacy class
# and the standard rep is irreducible:
#   M_std = (|class| * chi_std(class) / dim) * I = (6 * 1 / 3) * I = 2 * I
# So eigenvalue of M_std = 2, with multiplicity 3.
# Laplacian eigenvalue = 6 - 2 = 4, multiplicity 3.
# But wait -- 3^2 = 9 eigenvalues from a d=3 irrep.
# Actually: in the Cayley graph Laplacian, each irrep of dimension d
# contributes d^2 eigenvalues. But by Schur's lemma for the sum over
# a full conjugacy class, M_rho = (c/d) * I where c = |class|*chi(class).
# Then all d eigenvalues of M_rho are the same = c/d.
# The multiplicity in the Laplacian is d^2 (each eigenvalue repeated d times
# for d copies of the irrep in the regular representation, and each copy
# gives d eigenvalues from M_rho).
# Wait -- let me be more careful.
#
# The regular representation decomposes as: R = direct_sum_rho d_rho * rho
# where each irrep rho appears d_rho times. The adjacency matrix block for
# irrep rho is M_rho tensor I_{d_rho}. So the eigenvalues of A restricted
# to the rho-isotypic component are: eigenvalues of M_rho, each with
# multiplicity d_rho.
# M_rho is d_rho x d_rho. By Schur's lemma (since T = full conjugacy class):
#   M_rho = (|T| * chi_rho(T) / d_rho) * I_{d_rho}
# where chi_rho(T) means chi_rho evaluated on any element of T.
# So all eigenvalues of M_rho are (|T| * chi_rho(t) / d_rho) = mu_rho.
# Total multiplicity of mu_rho as eigenvalue of A: d_rho * d_rho = d_rho^2.
# Laplacian eigenvalue: lambda_rho = |T| - mu_rho.

# KEY INSIGHT: Because our generating set T is a SINGLE conjugacy class
# (all 6 transpositions), Schur's lemma guarantees M_rho is proportional
# to identity. So each irrep gives ONE distinct Laplacian eigenvalue
# with multiplicity d_rho^2.

# However, if T were a UNION of conjugacy classes, M_rho could have
# multiple eigenvalues within a single irrep. Here T is a single class. Good.

print("  Generating set T = {all 6 transpositions} = single conjugacy class")
print("  Schur's lemma => M_rho = (|T| * chi_rho(trans) / d_rho) * I")
print()

analytic_eigenvalues = {}
analytic_multiplicities = {}
total_mult = 0

for name in ['trivial', 'sign', 'standard', 'sign_standard', '2D']:
    d = dims[name]
    chi_t = chi_at_trans[name]
    mu = 6 * chi_t / d  # eigenvalue of adjacency matrix for this irrep
    lam = 6 - mu         # Laplacian eigenvalue
    mult = d**2
    analytic_eigenvalues[name] = lam
    analytic_multiplicities[name] = mult
    total_mult += mult
    print(f"  {name:15s} (d={d}): chi(trans)={chi_t:+d}, "
          f"mu={mu:+.4f}, lambda={lam:.4f}, mult={mult}")

print(f"\n  Total multiplicities: {total_mult} (should be 24)")
assert total_mult == 24

# Sort analytic eigenvalues
analytic_sorted = sorted(analytic_eigenvalues.items(), key=lambda x: x[1])
print("\n  Analytic spectrum (sorted):")
for name, lam in analytic_sorted:
    print(f"    lambda = {lam:10.6f}  (mult {analytic_multiplicities[name]:2d}, "
          f"irrep: {name})")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 3: Cross-check analytic vs numerical
# ══════════════════════════════════════════════════════════════════════════════

print("PART 3: Cross-check analytic vs numerical")

# Build full analytic spectrum
analytic_full = []
for name, lam in analytic_eigenvalues.items():
    analytic_full.extend([lam] * analytic_multiplicities[name])
analytic_full = np.sort(analytic_full)

residual = np.max(np.abs(analytic_full - eigvals_num))
print(f"  Max |analytic - numerical| = {residual:.2e}")
assert residual < 1e-10, f"Analytic/numerical mismatch: {residual}"
print("  CROSS-CHECK PASSED: analytic and numerical spectra agree to < 1e-10")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 4: Spectral gap and Thouless time
# ══════════════════════════════════════════════════════════════════════════════

print("PART 4: Thouless time computation")
print()

# Spectral gap = smallest nonzero eigenvalue
lambda_1 = analytic_sorted[1][1]  # second smallest (first is trivial = 0)
lambda_1_name = analytic_sorted[1][0]
print(f"  Spectral gap lambda_1 = {lambda_1:.6f} (from irrep: {lambda_1_name})")
print(f"  Full Laplacian spectrum: {[f'{lam:.4f}(x{analytic_multiplicities[n]})' for n, lam in analytic_sorted]}")
print()

# Thouless time: t_Th = 1 / (E_J * lambda_1)
t_Th = 1.0 / (E_J * lambda_1)
print(f"  t_Th = 1 / (E_J * lambda_1)")
print(f"       = 1 / ({E_J:.6f} * {lambda_1:.6f})")
print(f"       = {t_Th:.10e} M_KK^{{-1}}")
print()

# Ratio
ratio = t_Th / t_transit
print(f"  t_transit = {t_transit:.10e} M_KK^{{-1}}")
print(f"  t_Th / t_transit = {ratio:.6f}")
print()

# Gate verdict
if ratio > 10:
    verdict = "PASS"
    detail = f"t_Th/t_transit = {ratio:.2f} > 10. GGE survives: thermalization too slow."
elif ratio < 0.1:
    verdict = "FAIL"
    detail = f"t_Th/t_transit = {ratio:.2f} < 0.1. GGE thermalizes within transit."
else:
    verdict = "INFO"
    detail = f"t_Th/t_transit = {ratio:.2f} in [0.1, 10]. Marginal regime."

print(f"  ┌─────────────────────────────────────────────────────┐")
print(f"  │  GATE: GGE-THERM-61 = {verdict:4s}                         │")
print(f"  │  {detail}")
print(f"  └─────────────────────────────────────────────────────┘")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 5: Mixing time estimates
# ══════════════════════════════════════════════════════════════════════════════

print("PART 5: Mixing time estimates")
print()

# For a regular graph, the mixing time satisfies:
#   t_mix ~ (1/lambda_1) * ln(n)
# where n = number of vertices
t_mix_graph = (1.0 / lambda_1) * np.log(n)
t_mix_physical = t_mix_graph / E_J

print(f"  Graph mixing time ~ (1/lambda_1) * ln(24) = {t_mix_graph:.6f}")
print(f"  Physical mixing time = t_mix_graph / E_J = {t_mix_physical:.10e} M_KK^{{-1}}")
print(f"  Physical mixing / t_transit = {t_mix_physical / t_transit:.6f}")
print()

# Relaxation time (inverse spectral gap on graph)
t_relax_graph = 1.0 / lambda_1
t_relax_physical = t_relax_graph / E_J
print(f"  Graph relaxation time = 1/lambda_1 = {t_relax_graph:.6f}")
print(f"  Physical relaxation time = {t_relax_physical:.10e} M_KK^{{-1}}")
print()

# Diameter of CG(24)
# The diameter of the Cayley graph of S_4 with all transpositions as generators
# equals the maximum number of transpositions needed to express any permutation.
# This is the maximum of the "reflection length" = n - #cycles(sigma).
# For S_4, max reflection length = 4 - 1 = 3 (for a 4-cycle).
# Actually: any permutation in S_n can be written as at most n-1 transpositions.
# For S_4 with ALL transpositions (not just adjacent), diameter = 3.
# Verify by BFS:
from collections import deque
identity = (0, 1, 2, 3)
dist = {identity: 0}
queue = deque([identity])
while queue:
    p = queue.popleft()
    for t in transpositions:
        q = apply_transposition(p, t)
        if q not in dist:
            dist[q] = dist[p] + 1
            queue.append(q)
diameter = max(dist.values())
print(f"  Graph diameter (BFS verified) = {diameter}")
print(f"  Distance distribution: {dict(sorted([(d, sum(1 for v in dist.values() if v == d)) for d in set(dist.values())]))}")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 6: Spectral dimension d_s(t) from return probability
# ══════════════════════════════════════════════════════════════════════════════

print("PART 6: Spectral dimension d_s(t)")
print()

# Return probability on the Cayley graph:
#   P(t) = (1/|G|) * sum_rho d_rho^2 * exp(-lambda_rho * t)
#
# where the sum runs over all irreps rho of G, lambda_rho is the Laplacian
# eigenvalue, and d_rho is the dimension.
#
# This is the heat kernel trace: P(t) = (1/N) * Tr(e^{-Lt})
#
# Spectral dimension: d_s(t) = -2 * d(log P) / d(log t)

# Eigenvalue data for computation
irrep_data = []
for name, lam in analytic_eigenvalues.items():
    d = dims[name]
    irrep_data.append((name, d, lam))

# Time range (in graph units, i.e., E_J * physical_time)
t_graph = np.logspace(-3, 2, 2000)
t_phys = t_graph / E_J

# Return probability
P_return = np.zeros_like(t_graph)
for name, d, lam in irrep_data:
    P_return += (d**2 / n) * np.exp(-lam * t_graph)

# Spectral dimension via numerical log-derivative
log_t = np.log(t_graph)
log_P = np.log(P_return)
d_s = -2.0 * np.gradient(log_P, log_t)

# Key values
# Early time (t << 1/lambda_max): d_s -> dimension of generating set
# Late time (t >> 1/lambda_1): d_s -> 0 (finite graph, P -> 1/24)
# Intermediate: d_s reflects effective dimensionality

# Find d_s at specific times
t_targets = [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
print(f"  {'t_graph':>10s}  {'t_phys (M_KK^-1)':>20s}  {'P(t)':>12s}  {'d_s(t)':>8s}")
print(f"  {'-'*10}  {'-'*20}  {'-'*12}  {'-'*8}")
for tt in t_targets:
    idx = np.argmin(np.abs(t_graph - tt))
    print(f"  {t_graph[idx]:10.4f}  {t_phys[idx]:20.10e}  {P_return[idx]:12.6f}  {d_s[idx]:8.4f}")

# Spectral dimension at transit time
t_transit_graph = E_J * t_transit
idx_transit = np.argmin(np.abs(t_graph - t_transit_graph))
print(f"\n  At transit time (t_graph = E_J * t_transit = {t_transit_graph:.6f}):")
print(f"    P(t_transit)  = {P_return[idx_transit]:.6f}")
print(f"    d_s(t_transit) = {d_s[idx_transit]:.4f}")
print()

# Peak spectral dimension
idx_peak = np.argmax(d_s[10:]) + 10  # skip edge effects
print(f"  Peak spectral dimension: d_s_max = {d_s[idx_peak]:.4f} at t_graph = {t_graph[idx_peak]:.4f}")
print()

# Long-time asymptote
print(f"  Long-time: P(t->inf) = {1.0/n:.6f} (= 1/24)")
print(f"  d_s(t->inf) = 0 (finite graph)")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 7: Connection to Pillar VII — spectral dimension flow
# ══════════════════════════════════════════════════════════════════════════════

print("PART 7: Cross-pillar connections")
print()

# The spectral dimension of CG(24) flows from ~3 (early time, reflecting
# the local 3D structure since each vertex has 6 neighbors arranged as
# edges of an octahedron in the Cayley graph) down to 0 (finite-size
# cutoff). This mirrors the d_s flow in CDT/LQG (Pillar VII, Papers 26-28)
# from 4 to 2, but on a discrete group manifold.

# The Laplacian spectrum encodes the geometry of the permutation group
# viewed as a discrete metric space. The spectral gap lambda_1 = 4
# is set by the standard representation — the fundamental irrep of S_4.

# For the Josephson fabric, this means the GGE relaxation is controlled
# by the representation theory of the permutation symmetry of the cells.

# Cheeger constant bound
# For a d-regular graph: lambda_1 >= h^2 / (2d) where h is Cheeger constant
# and lambda_1 <= 2h. Since lambda_1 = 4, d = 6:
# h >= sqrt(2 * 6 * 4) = sqrt(48) ≈ 6.93 ... but h <= 6 for a 6-regular graph
# Actually the bound is: h^2/(2d) <= lambda_1 <= 2h
# So: h <= lambda_1/2 ... wait, the discrete Cheeger inequality is:
# lambda_1/2 <= h <= sqrt(2 * d * lambda_1) for unnormalized Laplacian
# Actually: for normalized Laplacian L_norm = D^{-1/2} L D^{-1/2},
# lambda_1^norm / 2 <= h <= sqrt(2 * lambda_1^norm)
# Here lambda_1^norm = lambda_1 / d = 4/6 = 2/3
h_lower = (4.0 / 6.0) / 2.0  # lambda_1_norm / 2
h_upper = np.sqrt(2.0 * 4.0 / 6.0)
print(f"  Cheeger constant bounds: {h_lower:.4f} <= h <= {h_upper:.4f}")
print(f"  (Graph is a good expander: lambda_1/d = {4.0/6.0:.4f})")
print()

# Ramanujan bound check
# A d-regular graph is Ramanujan if all nontrivial eigenvalues of adjacency
# satisfy |mu| <= 2*sqrt(d-1) = 2*sqrt(5) ≈ 4.47
# Adjacency eigenvalues: mu = 6 - lambda
adj_eigenvalues = [6 - lam for _, lam in analytic_sorted]
ramanujan_bound = 2.0 * np.sqrt(5)
print(f"  Adjacency eigenvalues: {[f'{m:.1f}' for m in adj_eigenvalues]}")
print(f"  Ramanujan bound: 2*sqrt(5) = {ramanujan_bound:.4f}")
is_ramanujan = all(abs(m) <= ramanujan_bound for m in adj_eigenvalues[1:-1])
print(f"  Nontrivial |mu| values: {[f'{abs(m):.1f}' for m in adj_eigenvalues[1:-1]]}")
print(f"  Is Ramanujan? {is_ramanujan}")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 8: Normalized Laplacian analysis
# ══════════════════════════════════════════════════════════════════════════════

print("PART 8: Normalized Laplacian")
print()

# For a d-regular graph, L_norm = L/d. Eigenvalues in [0, 2].
print(f"  Normalized spectrum: {[f'{lam/6:.4f}' for _, lam in analytic_sorted]}")
print(f"  Spectral gap (normalized) = {lambda_1/6:.6f}")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 9: Save data
# ══════════════════════════════════════════════════════════════════════════════

outfile = Path(__file__).resolve().parent / 's61_thouless_cayley.npz'
np.savez(outfile,
         # Graph structure
         n_vertices=np.int64(n),
         degree=np.int64(6),
         diameter=np.int64(diameter),
         adjacency_matrix=A,
         laplacian_eigenvalues_num=eigvals_num,
         # Analytic spectrum
         irrep_names=np.array(['trivial', 'sign', 'standard', 'sign_standard', '2D']),
         irrep_dims=np.array([1, 1, 3, 3, 2]),
         irrep_chi_trans=np.array([1, -1, 1, -1, 0]),
         laplacian_eigenvalues_analytic=np.array([analytic_eigenvalues[n] for n in
                                                   ['trivial', 'sign', 'standard', 'sign_standard', '2D']]),
         laplacian_multiplicities=np.array([1, 1, 9, 9, 4]),
         # Key results
         spectral_gap=np.float64(lambda_1),
         E_J=np.float64(E_J),
         t_transit=np.float64(t_transit),
         t_Th=np.float64(t_Th),
         ratio_tTh_ttransit=np.float64(ratio),
         # Spectral dimension
         t_graph=t_graph,
         t_phys=t_phys,
         P_return=P_return,
         d_s=d_s,
         # Gate
         gate_name=np.array(['GGE-THERM-61']),
         gate_verdict=np.array([verdict]),
         gate_detail=np.array([detail]),
         )
print(f"Data saved to {outfile}")
print()

# ══════════════════════════════════════════════════════════════════════════════
# PART 10: Plot
# ══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

# --- Panel 1: Laplacian eigenvalue spectrum ---
ax1 = axes[0]
for name, lam in analytic_sorted:
    d = dims[name]
    m = d**2
    ax1.barh(name, lam, height=0.6, color='steelblue', alpha=0.8)
    ax1.text(lam + 0.15, name, f'{lam:.1f} (x{m})', va='center', fontsize=10)
ax1.set_xlabel('Laplacian eigenvalue', fontsize=11)
ax1.set_title('CG(24) = Cayley(S$_4$, transpositions)\nLaplacian spectrum', fontsize=12)
ax1.axvline(x=lambda_1, color='red', linestyle='--', alpha=0.5, label=f'$\\lambda_1={lambda_1:.0f}$ (gap)')
ax1.legend(fontsize=9)
ax1.set_xlim(-0.5, 14)

# --- Panel 2: Spectral dimension d_s(t) ---
ax2 = axes[1]
ax2.semilogx(t_graph, d_s, 'b-', linewidth=1.5)
ax2.axvline(x=t_transit_graph, color='red', linestyle='--', linewidth=1.5,
            label=f'$t_{{transit}}$ = {t_transit_graph:.4f}')
ax2.axvline(x=1.0/lambda_1, color='orange', linestyle=':', linewidth=1.5,
            label=f'$1/\\lambda_1$ = {1.0/lambda_1:.3f}')
ax2.set_xlabel('$t$ (graph units = $E_J \\cdot t_{phys}$)', fontsize=11)
ax2.set_ylabel('$d_s(t)$', fontsize=11)
ax2.set_title('Spectral dimension flow on CG(24)', fontsize=12)
ax2.set_ylim(-0.5, max(d_s[10:]) * 1.2)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Annotate key features
if idx_transit < len(d_s):
    ax2.annotate(f'$d_s(t_{{tr}})$ = {d_s[idx_transit]:.2f}',
                xy=(t_transit_graph, d_s[idx_transit]),
                xytext=(t_transit_graph * 5, d_s[idx_transit] + 0.5),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=9, color='red')

# --- Panel 3: Return probability P(t) ---
ax3 = axes[2]
ax3.semilogy(t_graph, P_return, 'b-', linewidth=1.5)
ax3.axhline(y=1.0/24, color='gray', linestyle=':', alpha=0.5, label='$1/24$ (uniform)')
ax3.axvline(x=t_transit_graph, color='red', linestyle='--', linewidth=1.5,
            label=f'$t_{{transit}}$')
ax3.axvline(x=t_Th * E_J, color='green', linestyle='-.', linewidth=1.5,
            label=f'$t_{{Th}}$ = {t_Th*E_J:.4f} (graph)')
ax3.set_xlabel('$t$ (graph units)', fontsize=11)
ax3.set_ylabel('$P(t)$', fontsize=11)
ax3.set_title('Return probability (heat kernel trace)', fontsize=12)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Suptitle with gate verdict
fig.suptitle(f'GGE-THERM-61 = {verdict}:  $t_{{Th}}/t_{{transit}}$ = {ratio:.4f}',
             fontsize=14, fontweight='bold',
             color='green' if verdict == 'PASS' else ('red' if verdict == 'FAIL' else 'darkorange'),
             y=1.02)

plt.tight_layout()
plotfile = Path(__file__).resolve().parent / 's61_thouless_cayley.png'
fig.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plotfile}")

# ══════════════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

print()
print("=" * 72)
print("FINAL SUMMARY")
print("=" * 72)
print(f"  CG(24) = Cayley graph of S_4 with 6 transpositions")
print(f"  24 vertices, degree 6, diameter {diameter}")
print(f"")
print(f"  Laplacian spectrum (analytic, cross-checked numerically):")
for name, lam in analytic_sorted:
    print(f"    {name:15s}: lambda = {lam:6.2f}, mult = {analytic_multiplicities[name]:2d}")
print(f"")
print(f"  Spectral gap:  lambda_1 = {lambda_1}")
print(f"  E_J:           {E_J:.6f} M_KK")
print(f"  t_Th:          {t_Th:.10e} M_KK^{{-1}}")
print(f"  t_transit:     {t_transit:.10e} M_KK^{{-1}}")
print(f"  t_Th/t_transit = {ratio:.6f}")
print(f"")
print(f"  GATE: GGE-THERM-61 = {verdict}")
print(f"  {detail}")
print(f"")
print(f"  Spectral dimension at transit: d_s = {d_s[idx_transit]:.4f}")
print(f"  Peak spectral dimension: d_s = {d_s[idx_peak]:.4f}")
print(f"")
print(f"  Cross-check: analytic vs numerical max residual = {residual:.2e}")
print("=" * 72)
