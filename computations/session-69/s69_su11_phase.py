#!/usr/bin/env python3
"""
s69_su11_phase.py — SU(1,1)-PHASE-CG24-69: KZ Phase Topology on CG(24)

Gate: SU11-PHASE-69
  PASS: <cos(phi_eff)> > 0  (net constructive interference)
  INFO: <cos(phi_eff)> < 0  (net destructive) or large variance

Computes spatially averaged cos(phi_eff) on CG(24) Josephson array from
Kibble-Zurek defect topology.  Three phase configurations tested:
  (a) Z_3 winding (maximally frustrated): phi_a in {0, 2pi/3, 4pi/3}
  (b) Uniform random phases: phi_a ~ U(0, 2pi)
  (c) Thermal distribution: P(phi) ~ exp(E_J cos(phi) / T)

Uses anisotropic per-edge E_J from s63 and domain assignment from s57.
Also tests random balanced partitions for robustness.

Session 69, Wave 2-B.
"""

import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Import canonical constants ──────────────────────────────────────────────
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import T_acoustic

# ── Load data ───────────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).resolve().parent

s57 = np.load(DATA_DIR / 's57_cayley_josephson.npz', allow_pickle=True)
s63 = np.load(DATA_DIR / 's63_aniso_josephson.npz', allow_pickle=True)

N_vertices = int(s57['N_vertices'])  # 24
adj63 = s63['adj'].astype(int)       # (24,24) anisotropic adjacency
EJ_unoriented = s63['EJ_unoriented'] # 72 edge weights

# Domain assignment from s57 KZ partitioning
domain_s57 = s57['domain_assignment']  # shape (24,), values in {0,1,2}
N_domains = int(s57['N_domains'])      # 3

# ── Build weighted edge list from s63 adjacency ────────────────────────────
# Upper-triangle ordering matches EJ_unoriented indexing
edges = []
for i in range(N_vertices):
    for j in range(i + 1, N_vertices):
        if adj63[i, j]:
            edges.append((i, j))
edges = np.array(edges)
N_edges = len(edges)
assert N_edges == int(s63['N_unoriented_edges']), \
    f"Edge count mismatch: {N_edges} vs {int(s63['N_unoriented_edges'])}"

# Build weight matrix W[i,j] = E_J for connected pairs, 0 otherwise
W = np.zeros((N_vertices, N_vertices))
for idx, (i, j) in enumerate(edges):
    W[i, j] = EJ_unoriented[idx]
    W[j, i] = EJ_unoriented[idx]


# ── Core computation function ───────────────────────────────────────────────
def compute_phase_average(phases_per_vertex, weight_matrix, edge_list, ej_weights):
    """
    Compute <cos(phi_eff)> = (1/N_edges) * sum_{<ij>} J_ij * cos(phi_i - phi_j)

    Also compute the weighted version normalized by total coupling:
      <cos(phi_eff)>_weighted = sum J_ij cos(dphi) / sum J_ij

    Parameters
    ----------
    phases_per_vertex : array (N_vertices,)
    weight_matrix : array (N_vertices, N_vertices)  [unused, kept for API]
    edge_list : array (N_edges, 2)
    ej_weights : array (N_edges,)

    Returns
    -------
    cos_avg_uniform : float
        (1/N_edges) * sum J_ij cos(dphi_ij)
    cos_avg_weighted : float
        sum J_ij cos(dphi_ij) / sum J_ij
    cos_values : array (N_edges,)
        Per-edge J_ij * cos(dphi_ij)
    """
    dphi = phases_per_vertex[edge_list[:, 0]] - phases_per_vertex[edge_list[:, 1]]
    cos_dphi = np.cos(dphi)
    weighted_cos = ej_weights * cos_dphi

    cos_avg_uniform = weighted_cos.sum() / len(edge_list)
    cos_avg_weighted = weighted_cos.sum() / ej_weights.sum()

    return cos_avg_uniform, cos_avg_weighted, weighted_cos


def assign_domain_phases(domain_assignment, domain_phases):
    """Map domain-level phases to vertex-level phases."""
    return domain_phases[domain_assignment]


# ── (a) Z_3 winding: maximally frustrated ──────────────────────────────────
print("=" * 70)
print("(a) Z_3 winding on s57 domain partition")
print("=" * 70)

# All 6 permutations of Z_3 phases assigned to 3 domains
z3_phases = np.array([0, 2 * np.pi / 3, 4 * np.pi / 3])
from itertools import permutations

z3_results = []
for perm in permutations([0, 1, 2]):
    domain_phi = z3_phases[list(perm)]
    vertex_phi = assign_domain_phases(domain_s57, domain_phi)
    avg_u, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
    z3_results.append((perm, avg_u, avg_w))
    print(f"  Perm {perm}: <cos>_uniform = {avg_u:+.6f}, <cos>_weighted = {avg_w:+.6f}")

# Z_3 exact: all inter-domain pairs have dphi = +/- 2pi/3, cos = -1/2
# Intra-domain pairs have dphi = 0, cos = 1
# So result depends on fraction of intra vs inter edges (weighted)
z3_uniform = np.mean([r[1] for r in z3_results])
z3_weighted = np.mean([r[2] for r in z3_results])
print(f"\n  Z_3 average across permutations:")
print(f"    <cos>_uniform  = {z3_uniform:+.6f}")
print(f"    <cos>_weighted = {z3_weighted:+.6f}")

# Analytical check: separate intra and inter contributions
intra_ej_sum = 0.0  # (local)
inter_ej_sum = 0.0  # (local)
for idx, (i, j) in enumerate(edges):
    if domain_s57[i] == domain_s57[j]:
        intra_ej_sum += EJ_unoriented[idx]
    else:
        inter_ej_sum += EJ_unoriented[idx]

total_ej = EJ_unoriented.sum()
n_intra = sum(1 for idx, (i, j) in enumerate(edges) if domain_s57[i] == domain_s57[j])
n_inter = N_edges - n_intra

print(f"\n  Partition structure (s57 domains on s63 graph):")
print(f"    Intra-domain edges: {n_intra}  (EJ sum = {intra_ej_sum:.6f})")
print(f"    Inter-domain edges: {n_inter}  (EJ sum = {inter_ej_sum:.6f})")
print(f"    Total edges: {N_edges}  (EJ sum = {total_ej:.6f})")
print(f"    Inter-domain fraction (by count): {n_inter / N_edges:.4f}")
print(f"    Inter-domain fraction (by EJ): {inter_ej_sum / total_ej:.4f}")

# For Z_3: cos(0) = 1 for intra, cos(2pi/3) = -1/2 for inter
z3_analytical_weighted = (intra_ej_sum * 1.0 + inter_ej_sum * (-0.5)) / total_ej
z3_analytical_uniform = (intra_ej_sum * 1.0 + inter_ej_sum * (-0.5)) / N_edges
print(f"\n  Analytical Z_3 check:")
print(f"    <cos>_weighted (analytical) = {z3_analytical_weighted:+.6f}")
print(f"    <cos>_uniform  (analytical) = {z3_analytical_uniform:+.6f}")


# ── (b) Uniform random phases ──────────────────────────────────────────────
print("\n" + "=" * 70)
print("(b) Uniform random domain phases: phi_a ~ U(0, 2pi)")
print("=" * 70)

rng = np.random.default_rng(seed=42)
N_random_trials = 100_000

uniform_results_u = np.zeros(N_random_trials)
uniform_results_w = np.zeros(N_random_trials)

for trial in range(N_random_trials):
    domain_phi = rng.uniform(0, 2 * np.pi, size=N_domains)
    vertex_phi = assign_domain_phases(domain_s57, domain_phi)
    avg_u, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
    uniform_results_u[trial] = avg_u
    uniform_results_w[trial] = avg_w

print(f"  {N_random_trials} trials with s57 partition:")
print(f"    <cos>_uniform:  mean = {uniform_results_u.mean():+.6f}, "
      f"std = {uniform_results_u.std():.6f}")
print(f"    <cos>_weighted: mean = {uniform_results_w.mean():+.6f}, "
      f"std = {uniform_results_w.std():.6f}")
print(f"    Fraction with <cos>_weighted > 0: "
      f"{(uniform_results_w > 0).mean():.4f}")


# ── (c) Thermal distribution ───────────────────────────────────────────────
print("\n" + "=" * 70)
print("(c) Thermal phase distribution: P(phi) ~ exp(E_J cos(phi) / T)")
print("=" * 70)

T_GGE = T_acoustic  # 0.112 M_KK from canonical constants
# Mean E_J per edge for thermal scale
EJ_mean = float(s63['EJ_mean'])
beta_eff = EJ_mean / T_GGE

print(f"  T_GGE = {T_GGE:.4f} M_KK")
print(f"  <E_J> = {EJ_mean:.6f} M_KK")
print(f"  beta_eff = E_J/T = {beta_eff:.4f}")

# For thermal: each domain gets a phase drawn from von Mises distribution
# P(phi) ~ exp(kappa * cos(phi)) where kappa = E_J / T
# <cos(phi)> = I_1(kappa) / I_0(kappa) for von Mises
from scipy.special import i0, i1

kappa = beta_eff
von_mises_mean_cos = i1(kappa) / i0(kappa)
print(f"  von Mises <cos(phi)> = I_1/I_0 = {von_mises_mean_cos:.6f}")
print(f"  (This is the single-bond thermal expectation)")

# Monte Carlo with thermal phases
N_thermal_trials = 100_000
thermal_results_u = np.zeros(N_thermal_trials)
thermal_results_w = np.zeros(N_thermal_trials)

for trial in range(N_thermal_trials):
    # Each domain gets a phase from von Mises centered at 0
    domain_phi = rng.vonmises(0, kappa, size=N_domains)
    vertex_phi = assign_domain_phases(domain_s57, domain_phi)
    avg_u, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
    thermal_results_u[trial] = avg_u
    thermal_results_w[trial] = avg_w

print(f"\n  {N_thermal_trials} thermal trials (s57 partition, von Mises kappa={kappa:.4f}):")
print(f"    <cos>_uniform:  mean = {thermal_results_u.mean():+.6f}, "
      f"std = {thermal_results_u.std():.6f}")
print(f"    <cos>_weighted: mean = {thermal_results_w.mean():+.6f}, "
      f"std = {thermal_results_w.std():.6f}")
print(f"    Fraction with <cos>_weighted > 0: "
      f"{(thermal_results_w > 0).mean():.4f}")


# ── Robustness: random balanced partitions ──────────────────────────────────
print("\n" + "=" * 70)
print("Robustness: random balanced partitions (8+8+8)")
print("=" * 70)

N_partition_trials = 1000
N_phase_per_partition = 100

# For each partition, test Z_3 and uniform random phases
z3_partition_results = np.zeros(N_partition_trials)
uniform_partition_results = np.zeros(N_partition_trials)
thermal_partition_results = np.zeros(N_partition_trials)

for pt in range(N_partition_trials):
    # Random balanced partition: shuffle vertices, assign first 8 to domain 0, etc.
    perm = rng.permutation(N_vertices)
    rand_domain = np.zeros(N_vertices, dtype=int)
    rand_domain[perm[:8]] = 0
    rand_domain[perm[8:16]] = 1
    rand_domain[perm[16:]] = 2

    # Z_3 on this partition (average over all 6 Z_3 assignments)
    z3_vals = []
    for z3perm in permutations([0, 1, 2]):
        domain_phi = z3_phases[list(z3perm)]
        vertex_phi = assign_domain_phases(rand_domain, domain_phi)
        _, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
        z3_vals.append(avg_w)
    z3_partition_results[pt] = np.mean(z3_vals)

    # Uniform random on this partition (average over N_phase_per_partition)
    u_vals = []
    t_vals = []
    for _ in range(N_phase_per_partition):
        # Uniform
        domain_phi = rng.uniform(0, 2 * np.pi, size=N_domains)
        vertex_phi = assign_domain_phases(rand_domain, domain_phi)
        _, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
        u_vals.append(avg_w)

        # Thermal
        domain_phi = rng.vonmises(0, kappa, size=N_domains)
        vertex_phi = assign_domain_phases(rand_domain, domain_phi)
        _, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
        t_vals.append(avg_w)

    uniform_partition_results[pt] = np.mean(u_vals)
    thermal_partition_results[pt] = np.mean(t_vals)

print(f"  {N_partition_trials} random balanced partitions, each with {N_phase_per_partition} "
      f"phase trials:")
print(f"\n  Z_3 winding across partitions:")
print(f"    mean = {z3_partition_results.mean():+.6f}, "
      f"std = {z3_partition_results.std():.6f}")
print(f"    min = {z3_partition_results.min():+.6f}, "
      f"max = {z3_partition_results.max():+.6f}")
print(f"    Fraction > 0: {(z3_partition_results > 0).mean():.4f}")

print(f"\n  Uniform random across partitions:")
print(f"    mean = {uniform_partition_results.mean():+.6f}, "
      f"std = {uniform_partition_results.std():.6f}")
print(f"    Fraction > 0: {(uniform_partition_results > 0).mean():.4f}")

print(f"\n  Thermal across partitions:")
print(f"    mean = {thermal_partition_results.mean():+.6f}, "
      f"std = {thermal_partition_results.std():.6f}")
print(f"    Fraction > 0: {(thermal_partition_results > 0).mean():.4f}")


# ── Full vertex-level phase disorder (no domain structure) ──────────────────
print("\n" + "=" * 70)
print("Control: full vertex-level random phases (no domain structure)")
print("=" * 70)

N_vertex_trials = 100_000
vertex_uniform_u = np.zeros(N_vertex_trials)
vertex_uniform_w = np.zeros(N_vertex_trials)
vertex_thermal_u = np.zeros(N_vertex_trials)
vertex_thermal_w = np.zeros(N_vertex_trials)

for trial in range(N_vertex_trials):
    # Uniform
    vertex_phi = rng.uniform(0, 2 * np.pi, size=N_vertices)
    avg_u, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
    vertex_uniform_u[trial] = avg_u
    vertex_uniform_w[trial] = avg_w

    # Thermal (each vertex independently)
    vertex_phi = rng.vonmises(0, kappa, size=N_vertices)
    avg_u, avg_w, _ = compute_phase_average(vertex_phi, W, edges, EJ_unoriented)
    vertex_thermal_u[trial] = avg_u
    vertex_thermal_w[trial] = avg_w

print(f"  {N_vertex_trials} trials, fully random per-vertex phases:")
print(f"\n  Uniform per-vertex:")
print(f"    <cos>_weighted: mean = {vertex_uniform_w.mean():+.6f}, "
      f"std = {vertex_uniform_w.std():.6f}")
print(f"    Fraction > 0: {(vertex_uniform_w > 0).mean():.4f}")

print(f"\n  Thermal per-vertex (von Mises kappa={kappa:.4f}):")
print(f"    <cos>_weighted: mean = {vertex_thermal_w.mean():+.6f}, "
      f"std = {vertex_thermal_w.std():.6f}")
print(f"    Fraction > 0: {(vertex_thermal_w > 0).mean():.4f}")


# ── Cross-check: W1-A found phi_eff = 1.753 rad ────────────────────────────
print("\n" + "=" * 70)
print("Cross-check against W1-A: phi_eff = 1.753 rad")
print("=" * 70)

phi_w1a = 1.753  # (local)
cos_w1a = np.cos(phi_w1a)
print(f"  W1-A phi_eff = {phi_w1a:.3f} rad")
print(f"  W1-A cos(phi_eff) = {cos_w1a:.6f}")

# What fraction of Z_3 domain trials produce cos ~ cos_w1a?
z3_cos_values = [r[2] for r in z3_results]  # All 6 Z_3 permutations
print(f"  Z_3 cos values (all perms): {[f'{v:+.6f}' for v in z3_cos_values]}")
print(f"  Z_3 are all identical: {np.allclose(z3_cos_values, z3_cos_values[0])}")


# ── Summary and gate verdict ───────────────────────────────────────────────
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

# Primary result: Z_3 winding on s57 partition
print(f"\n  (a) Z_3 winding (s57 partition): <cos>_weighted = {z3_weighted:+.6f}")
print(f"  (b) Uniform random (s57 partition): <cos>_weighted = {uniform_results_w.mean():+.6f} "
      f"+/- {uniform_results_w.std():.6f}")
print(f"  (c) Thermal (s57 partition): <cos>_weighted = {thermal_results_w.mean():+.6f} "
      f"+/- {thermal_results_w.std():.6f}")

print(f"\n  Robustness (1000 random partitions):")
print(f"    Z_3: {z3_partition_results.mean():+.6f} +/- {z3_partition_results.std():.6f}")
print(f"    Uniform: {uniform_partition_results.mean():+.6f} +/- "
      f"{uniform_partition_results.std():.6f}")
print(f"    Thermal: {thermal_partition_results.mean():+.6f} +/- "
      f"{thermal_partition_results.std():.6f}")

# Gate verdict
# The primary question: is <cos(phi_eff)> > 0?
# Z_3 winding is the maximally frustrated case. If THAT is > 0, everything else will be.
# If Z_3 is < 0, check thermal and uniform.
primary_cos = z3_weighted
thermal_cos = thermal_results_w.mean()
uniform_cos = uniform_results_w.mean()

print(f"\n  {'=' * 50}")
if thermal_cos > 0:
    verdict = "PASS"
    detail = (f"Thermal <cos>_weighted = {thermal_cos:+.6f} > 0. "
              f"Z_3 frustrated ({z3_weighted:+.6f}), but thermal restores constructive.")
elif uniform_cos > 0:
    verdict = "PASS"
    detail = (f"Uniform <cos>_weighted = {uniform_cos:+.6f} > 0. "
              f"Random phases give net constructive interference.")
elif z3_weighted > 0:
    verdict = "PASS"
    detail = f"Z_3 <cos>_weighted = {z3_weighted:+.6f} > 0."
else:
    # All negative or indeterminate
    if thermal_results_w.std() > abs(thermal_cos):
        verdict = "INFO"
        detail = (f"Thermal <cos>_weighted = {thermal_cos:+.6f} with "
                  f"std = {thermal_results_w.std():.6f}. Large variance, indeterminate.")
    else:
        verdict = "INFO"
        detail = (f"All configurations give <cos>_weighted < 0. "
                  f"Z_3: {z3_weighted:+.6f}, Thermal: {thermal_cos:+.6f}, "
                  f"Uniform: {uniform_cos:+.6f}.")

print(f"  Gate SU11-PHASE-69: {verdict}")
print(f"  {detail}")
print(f"  {'=' * 50}")


# ── Save data ───────────────────────────────────────────────────────────────
np.savez(
    DATA_DIR / 's69_su11_phase.npz',
    # Graph data used
    N_vertices=N_vertices,
    N_edges_s63=N_edges,
    edges_s63=edges,
    EJ_unoriented=EJ_unoriented,
    # Domain partition
    domain_s57=domain_s57,
    N_domains=N_domains,
    n_intra_edges=n_intra,
    n_inter_edges=n_inter,
    intra_ej_sum=intra_ej_sum,
    inter_ej_sum=inter_ej_sum,
    # (a) Z_3 results
    z3_cos_weighted=z3_weighted,
    z3_cos_uniform=z3_uniform,
    z3_analytical_weighted=z3_analytical_weighted,
    # (b) Uniform random results
    uniform_cos_weighted_mean=uniform_results_w.mean(),
    uniform_cos_weighted_std=uniform_results_w.std(),
    uniform_cos_uniform_mean=uniform_results_u.mean(),
    uniform_cos_uniform_std=uniform_results_u.std(),
    uniform_frac_positive=float((uniform_results_w > 0).mean()),
    # (c) Thermal results
    thermal_cos_weighted_mean=thermal_results_w.mean(),
    thermal_cos_weighted_std=thermal_results_w.std(),
    thermal_kappa=kappa,
    T_GGE=T_GGE,
    thermal_frac_positive=float((thermal_results_w > 0).mean()),
    # Robustness across partitions
    z3_partition_mean=z3_partition_results.mean(),
    z3_partition_std=z3_partition_results.std(),
    uniform_partition_mean=uniform_partition_results.mean(),
    uniform_partition_std=uniform_partition_results.std(),
    thermal_partition_mean=thermal_partition_results.mean(),
    thermal_partition_std=thermal_partition_results.std(),
    # Control: per-vertex phases
    vertex_uniform_mean=vertex_uniform_w.mean(),
    vertex_uniform_std=vertex_uniform_w.std(),
    vertex_thermal_mean=vertex_thermal_w.mean(),
    vertex_thermal_std=vertex_thermal_w.std(),
    # W1-A cross-check
    phi_w1a=phi_w1a,
    cos_w1a=cos_w1a,
    # Gate
    gate_name='SU11-PHASE-69',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"\nData saved to {DATA_DIR / 's69_su11_phase.npz'}")


# ── Plot ────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('SU(1,1)-PHASE-CG24-69: KZ Phase Topology on CG(24)',
             fontsize=14, fontweight='bold')

# Panel 1: Histogram of uniform random domain-phase results
ax = axes[0, 0]
ax.hist(uniform_results_w, bins=80, density=True, alpha=0.7, color='steelblue',
        label=f's57 partition\nmean={uniform_results_w.mean():+.4f}')
ax.axvline(0, color='black', linestyle='--', linewidth=1.0, label='cos=0')
ax.axvline(z3_weighted, color='red', linestyle='-', linewidth=2.0,
           label=f'Z_3 = {z3_weighted:+.4f}')
ax.axvline(cos_w1a, color='green', linestyle=':', linewidth=2.0,
           label=f'W1-A = {cos_w1a:+.4f}')
ax.set_xlabel(r'$\langle \cos\phi_{\rm eff}\rangle_{\rm weighted}$')
ax.set_ylabel('Density')
ax.set_title('(b) Uniform Random Domain Phases')
ax.legend(fontsize=8)

# Panel 2: Histogram of thermal domain-phase results
ax = axes[0, 1]
ax.hist(thermal_results_w, bins=80, density=True, alpha=0.7, color='darkorange',
        label=f's57 partition\nmean={thermal_results_w.mean():+.4f}')
ax.axvline(0, color='black', linestyle='--', linewidth=1.0, label='cos=0')
ax.axvline(z3_weighted, color='red', linestyle='-', linewidth=2.0,
           label=f'Z_3 = {z3_weighted:+.4f}')
ax.set_xlabel(r'$\langle \cos\phi_{\rm eff}\rangle_{\rm weighted}$')
ax.set_ylabel('Density')
ax.set_title(f'(c) Thermal Phases ($\\kappa$ = {kappa:.2f})')
ax.legend(fontsize=8)

# Panel 3: Robustness across random partitions
ax = axes[1, 0]
ax.hist(z3_partition_results, bins=50, density=True, alpha=0.6, color='red',
        label=f'Z_3: {z3_partition_results.mean():+.4f}')
ax.hist(uniform_partition_results, bins=50, density=True, alpha=0.6, color='steelblue',
        label=f'Uniform: {uniform_partition_results.mean():+.4f}')
ax.hist(thermal_partition_results, bins=50, density=True, alpha=0.6, color='darkorange',
        label=f'Thermal: {thermal_partition_results.mean():+.4f}')
ax.axvline(0, color='black', linestyle='--', linewidth=1.0)
ax.set_xlabel(r'$\langle \cos\phi_{\rm eff}\rangle_{\rm weighted}$')
ax.set_ylabel('Density')
ax.set_title('Robustness: 1000 Random Balanced Partitions')
ax.legend(fontsize=8)

# Panel 4: Control — per-vertex phases vs domain phases
ax = axes[1, 1]
ax.hist(vertex_uniform_w, bins=80, density=True, alpha=0.5, color='gray',
        label=f'Vertex uniform: {vertex_uniform_w.mean():+.4f}')
ax.hist(vertex_thermal_w, bins=80, density=True, alpha=0.5, color='purple',
        label=f'Vertex thermal: {vertex_thermal_w.mean():+.4f}')
ax.hist(uniform_results_w, bins=80, density=True, alpha=0.3, color='steelblue',
        label=f'Domain uniform: {uniform_results_w.mean():+.4f}')
ax.axvline(0, color='black', linestyle='--', linewidth=1.0)
ax.set_xlabel(r'$\langle \cos\phi_{\rm eff}\rangle_{\rm weighted}$')
ax.set_ylabel('Density')
ax.set_title('Control: Vertex vs Domain Phase Disorder')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(DATA_DIR / 's69_su11_phase.png', dpi=150)
print(f"Plot saved to {DATA_DIR / 's69_su11_phase.png'}")


# ── Final printout ──────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("GATE VERDICT")
print("=" * 70)
print(f"  Gate: SU11-PHASE-69")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print("=" * 70)
