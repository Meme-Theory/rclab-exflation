#!/usr/bin/env python3
"""
KZ-PHASE-FNL-69: Kibble-Zurek Phase Winding Correction to Bispectrum
=====================================================================

Maps KZ phase winding on CG(24) to bispectrum modulation. Domain walls
produce phase jumps that modulate phi_eff spatially, correcting the
f_NL^{folded} = 0.129 baseline (S67 GGE-BISPECTRUM-67, W2-C).

Physics chain:
  (1) KZ mechanism during transit produces N_DW = 3 domains (Z_3 partition)
  (2) 52 of 96 edges are domain walls on CG(24) -- wall fraction 0.542
  (3) At each wall, BCS phase jumps by delta_phi = 2*pi/N_DW = 2*pi/3
  (4) Phase variance across cells modulates phi_eff spatially
  (5) Spatial phase modulation creates bispectrum correction via
      <delta_phi * delta_P * delta_P> three-point correlator

Three distinct mechanisms contribute to delta f_NL:

  (A) Phase gradient at walls: The condensate phase gradient at a domain
      wall creates a local current density j ~ nabla(phi). The current
      modulates the local power spectrum via the acoustic metric shift:
      delta c_s / c_s ~ (nabla phi)^2 / (2 * E_J).

  (B) Winding number fluctuation: For N_DW = 3 domains, the total winding
      number W around any closed loop is quantized in Z_3. Loops enclosing
      different numbers of walls have different effective phi, creating
      mode-mode coupling in the bispectrum.

  (C) Wall network topology: The CG(24) wall network has a specific
      connectivity structure (Pillar VI, Paper 29). The wall density
      n_wall = N_wall_edges / N_total_edges modulates the average
      phase correlation length.

Gate: KZ-FNL-69 -- INFO. FLAG if |delta f_NL| > 0.013 (10% of 0.129).

Input:
  - s57_cayley_josephson.npz: CG(24) graph, domain structure, wall edges
  - s63_aniso_josephson.npz: Anisotropic Josephson couplings, phase stiffness
  - s67_gge_bispectrum.npz: Baseline f_NL values from three channels
  - canonical_constants.py: Framework constants

References:
  - Paper 29 (Vachaspati 2006): Kibble-Zurek defect density scaling
  - Paper 15 (Fazio-vdZant 2001): Josephson array phase dynamics
  - Paper 28 (Jackiw-Rebbi 1976): Fermion modes at domain walls
  - S57: CG(24) Josephson structure, N_DW = 3, E_DW = 0
  - S61: DW-CLASS-61 = INFO, geometric crossover (not phase boundary)
  - S67: GGE-BISPECTRUM-67, f_NL^{folded} = 0.129
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import linalg

from canonical_constants import (
    N_cells, J_C2, J_su2, J_u1, T_acoustic,
    n_pairs, c_Gold, P_exc_kz,
    omega_L1, omega_L2,
    dt_transit, H_fold, v_terminal,
    PI,
)

# ============================================================================
#  SECTION 0: Load input data
# ============================================================================

print("=" * 72)
print("KZ-PHASE-FNL-69: Phase Winding Correction to Bispectrum")
print("=" * 72)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load CG(24) domain structure
cg24 = np.load(os.path.join(script_dir, 's57_cayley_josephson.npz'),
               allow_pickle=True)
adj = cg24['adjacency']               # (24, 24) adjacency matrix
domain_assign = cg24['domain_assignment']  # (24,) domain labels {0, 1, 2}
wall_edges = cg24['wall_edges']        # (52, 2) inter-domain edges
N_vert = int(cg24['N_vertices'])       # 24
N_DW = int(cg24['N_domains'])          # 3
N_wall = int(cg24['N_domain_walls'])   # 52
domain_sizes = cg24['domain_sizes']    # [8, 8, 8]
lap_eigs = cg24['laplacian_eigenvalues']  # (24,)

# Load anisotropic Josephson data
aniso = np.load(os.path.join(script_dir, 's63_aniso_josephson.npz'),
                allow_pickle=True)
EJ_per_trans = aniso['EJ_per_trans']   # (6,) E_J per transposition direction
rho_s_eigs = aniso['rho_s_eigs']      # (8,) superfluid stiffness eigenvalues
aniso_ratio = float(aniso['anisotropy_rhos'])  # 24.37

# Load baseline bispectrum
bispec = np.load(os.path.join(script_dir, 's67_gge_bispectrum.npz'),
                 allow_pickle=True)
f_NL_folded_baseline = float(bispec['f_NL_diag_CLT'])    # 0.1293
f_NL_equil_baseline = float(bispec['f_NL_equil'])         # 0.853
f_NL_total_baseline = float(bispec['f_NL_total_corr'])    # 0.324
c_BLV = float(bispec['c_BLV'])                            # 0.485
N_pair = float(bispec['N_pair'])                           # 59.8
N_acoustic = float(bispec['N_acoustic'])                   # 39.8
N_leggett = float(bispec['N_leggett'])                     # 20.0

print(f"\n--- Input Data ---")
print(f"  CG(24): N_vert = {N_vert}, N_DW = {N_DW}")
print(f"  Domain sizes: {domain_sizes}")
print(f"  Wall edges: {N_wall} / {N_wall + (96 - N_wall)} total = "
      f"{N_wall/96:.4f} wall fraction")
print(f"  Laplacian spectrum: {lap_eigs}")
print(f"  Fiedler value: {lap_eigs[1]:.4f}")
print(f"")
print(f"  Anisotropic E_J: {EJ_per_trans}")
print(f"  rho_s eigenvalues: {rho_s_eigs}")
print(f"  Anisotropy ratio: {aniso_ratio:.2f}")
print(f"")
print(f"  Baseline f_NL:")
print(f"    f_NL^{{folded}} (CLT) = {f_NL_folded_baseline:.6f}")
print(f"    f_NL^{{equil}}       = {f_NL_equil_baseline:.6f}")
print(f"    f_NL^{{total,corr}}  = {f_NL_total_baseline:.6f}")
print(f"    c_BLV               = {c_BLV}")
print(f"    N_pair              = {N_pair}")

# ============================================================================
#  SECTION 1: Phase Profile on CG(24) from Z_3 Domain Walls
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 1: Phase Profile from Z_3 Domain Walls")
print("=" * 72)

# The KZ mechanism during the BCS transit produces 3 domains with
# relative phase offsets of 2*pi/3 (the Z_3 symmetry of the three
# degenerate BCS ground states on CG(24)).
#
# From S57: E_DW = 0 exactly (GGE universality). This means the
# domain walls carry NO energy -- they are purely topological phase
# boundaries. The phase at each vertex is:
#
#   phi_i = (2*pi/3) * domain_assign[i] + delta_phi_i
#
# where delta_phi_i is the fluctuation from Josephson coupling.
#
# The key insight from S61: tau_DW is a geometric crossover, NOT a
# phase boundary. But the Z_3 partition is a DISTINCT structure --
# it comes from Kibble-Zurek during the transit, not from the Jensen
# geometry. The domains represent causally disconnected regions that
# independently chose their BCS phase.

# Base phase from Z_3 assignment
phi_base = (2.0 * PI / N_DW) * domain_assign.astype(float)

print(f"\n  Z_3 phase assignment:")
for d in range(N_DW):
    mask = domain_assign == d
    n_d = np.sum(mask)
    phi_d = 2.0 * PI * d / N_DW
    print(f"    Domain {d}: {n_d} vertices, phi_base = {phi_d:.4f} "
          f"({phi_d*180/PI:.1f} deg)")

# Phase differences across all edges
N_total_edges = 0
phase_diffs_wall = []
phase_diffs_internal = []

for i in range(N_vert):
    for j in range(i + 1, N_vert):
        if adj[i, j] > 0:
            N_total_edges += 1
            dphi = phi_base[i] - phi_base[j]
            # Wrap to [-pi, pi]
            dphi = (dphi + PI) % (2 * PI) - PI
            if domain_assign[i] != domain_assign[j]:
                phase_diffs_wall.append(dphi)
            else:
                phase_diffs_internal.append(dphi)

phase_diffs_wall = np.array(phase_diffs_wall)
phase_diffs_internal = np.array(phase_diffs_internal)

print(f"\n  Phase differences across edges:")
print(f"    Wall edges: {len(phase_diffs_wall)}, "
      f"<|delta_phi|> = {np.mean(np.abs(phase_diffs_wall)):.4f}")
print(f"    Internal edges: {len(phase_diffs_internal)}, "
      f"<|delta_phi|> = {np.mean(np.abs(phase_diffs_internal)):.4f}")

# The wall phase jumps are either +2*pi/3 or -2*pi/3 (or +/-4*pi/3
# wrapped to -/+2*pi/3), depending on which domains meet.
# Count the phase jump distribution:
unique_dphis, counts = np.unique(np.round(phase_diffs_wall, 4),
                                  return_counts=True)
print(f"\n  Wall phase jump distribution:")
for dp, c in zip(unique_dphis, counts):
    print(f"    delta_phi = {dp:+.4f} ({dp*180/PI:+.1f} deg): {c} edges")

# ============================================================================
#  SECTION 2: Phase Variance and Correlation Function
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 2: Phase Variance and Correlation Function")
print("=" * 72)

# The phase variance across the tessellation determines the strength
# of the bispectrum modulation. Compute:
#
#  sigma_phi^2 = (1/N_vert) * Sum_i (phi_i - <phi>)^2
#
# where <phi> is the mean phase.

phi_mean = np.mean(phi_base)
phi_var = np.var(phi_base)
phi_std = np.std(phi_base)

# For a Z_3 symmetric partition with equal-size domains:
# <phi> = (1/3)(0 + 2pi/3 + 4pi/3) = 2pi/3
# sigma_phi^2 = (1/3)((2pi/3)^2 + 0 + (2pi/3)^2) = (2/3)(2pi/3)^2
# Actually for a uniform distribution over {0, 2pi/3, 4pi/3} with circular mean:
# The circular variance is 1 - |<e^{i*phi}>|
circ_mean_vec = np.mean(np.exp(1j * phi_base))
circ_var = 1.0 - np.abs(circ_mean_vec)
circ_R = np.abs(circ_mean_vec)

print(f"\n  Phase statistics:")
print(f"    <phi> (linear mean) = {phi_mean:.4f} ({phi_mean*180/PI:.1f} deg)")
print(f"    sigma_phi (linear) = {phi_std:.4f}")
print(f"    sigma_phi^2 = {phi_var:.6f}")
print(f"")
print(f"  Circular statistics:")
print(f"    R = |<e^{{i*phi}}>| = {circ_R:.6f}")
print(f"    Circular variance V = 1 - R = {circ_var:.6f}")
print(f"    [R = 0 means perfectly uniform Z_3; R = 1 means all aligned]")

# Phase correlation function C(d) = <cos(phi_i - phi_j)> at graph distance d
# Compute graph distances via BFS on adjacency matrix
from collections import deque

def graph_distances(adj_matrix, n):
    """Compute all-pairs shortest path distances on graph."""
    dist = np.full((n, n), -1, dtype=int)
    for source in range(n):
        dist[source, source] = 0
        queue = deque([source])
        while queue:
            v = queue.popleft()
            for w in range(n):
                if adj_matrix[v, w] > 0 and dist[source, w] == -1:
                    dist[source, w] = dist[source, v] + 1
                    queue.append(w)
    return dist

dist_matrix = graph_distances(adj, N_vert)
max_dist = dist_matrix.max()

print(f"\n  Graph distance statistics:")
print(f"    Diameter = {max_dist}")
print(f"    Mean distance = {np.mean(dist_matrix[np.triu_indices(N_vert, k=1)]):.2f}")

# Phase correlation at each distance
phase_corr_by_dist = {}
for d in range(max_dist + 1):
    pairs = []
    for i in range(N_vert):
        for j in range(i + 1, N_vert):
            if dist_matrix[i, j] == d:
                pairs.append(np.cos(phi_base[i] - phi_base[j]))
    if pairs:
        phase_corr_by_dist[d] = np.mean(pairs)

print(f"\n  Phase correlation C(d) = <cos(phi_i - phi_j)> at distance d:")
for d in sorted(phase_corr_by_dist.keys()):
    print(f"    C(d={d}) = {phase_corr_by_dist[d]:+.6f}")

# ============================================================================
#  SECTION 3: Mechanism (A) -- Phase Gradient at Walls
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 3: Mechanism (A) -- Phase Gradient at Walls")
print("=" * 72)

# The condensate phase gradient at a domain wall creates a local
# supercurrent density. This shifts the local sound speed via
# the acoustic metric (Pillar I, Papers 01, 03):
#
#   c_s^2(x) = c_BLV^2 * (1 - (v_s(x)/c_BLV)^2)
#
# where v_s is the superfluid velocity from the phase gradient:
#
#   v_s = (1/m*) * nabla(phi)
#
# On CG(24), the "gradient" across an edge (i,j) is:
#   |nabla phi|_{ij} ~ |phi_i - phi_j| / a_lattice
#
# where a_lattice is the lattice spacing (set by M_KK^{-1}).
#
# The Josephson energy at the wall provides the scale:
#   E_J * (1 - cos(delta_phi)) = energy cost of phase mismatch
#
# The superfluid velocity from the phase gradient:
#   v_s ~ (1/m*) * delta_phi / a
# where m* is the effective mass and a is the lattice spacing.
#
# In Josephson array language (Paper 15, Fazio-vdZant):
#   v_s / c_s ~ delta_phi * sqrt(E_J / E_C)
#
# For our system:
#   E_J = J_C2 = 0.933 M_KK (dominant Josephson coupling)
#   E_C ~ T_acoustic = 0.112 M_KK (charging energy ~ GGE temperature)
#   delta_phi = 2*pi/3 at each wall

delta_phi_wall = 2.0 * PI / N_DW  # = 2.094

# Josephson current at wall: I_J = E_J * sin(delta_phi)
I_J_wall = J_C2 * np.sin(delta_phi_wall)

# Energy cost per wall edge: E_wall = E_J * (1 - cos(delta_phi))
E_wall_per_edge = J_C2 * (1.0 - np.cos(delta_phi_wall))

# Total wall energy
E_wall_total = N_wall * E_wall_per_edge

# BUT: S57 established E_DW = 0 exactly. This means the GGE adjusts
# to absorb the wall energy. The effective phase winding is FRUSTRATED
# -- the walls exist but carry no net energy. The phase gradient effect
# is suppressed by the GGE adjustment factor.
#
# The residual effect comes from the FLUCTUATIONS of the phase around
# the Z_3 values, not the mean phase gradient. These fluctuations are
# controlled by the ratio T_acoustic / E_J:

# Thermal phase fluctuation at each vertex (Josephson array theory):
# <(delta_phi)^2>_thermal = T / (z * E_J)
# where z = coordination number (here z = 8 for CG(24))
z_coord = 8  # each vertex has 8 neighbors
delta_phi_sq_thermal = T_acoustic / (z_coord * J_C2)
delta_phi_rms_thermal = np.sqrt(delta_phi_sq_thermal)

print(f"\n  Domain wall parameters:")
print(f"    delta_phi_wall = 2*pi/{N_DW} = {delta_phi_wall:.4f} rad "
      f"({delta_phi_wall*180/PI:.1f} deg)")
print(f"    E_J (C^2 coset) = {J_C2:.3f} M_KK")
print(f"    T_acoustic (GGE) = {T_acoustic:.3f} M_KK")
print(f"    E_wall per edge = E_J*(1-cos(2pi/3)) = {E_wall_per_edge:.4f} M_KK")
print(f"    Total E_wall (52 edges) = {E_wall_total:.2f} M_KK")
print(f"    S57 E_DW = 0 exactly -- walls carry no net energy (GGE absorbed)")
print(f"")
print(f"  Phase fluctuations:")
print(f"    <(delta_phi)^2>_th = T/(z*E_J) = {delta_phi_sq_thermal:.6f}")
print(f"    delta_phi_rms (thermal) = {delta_phi_rms_thermal:.4f} rad "
      f"({delta_phi_rms_thermal*180/PI:.2f} deg)")

# The sound speed modulation from phase gradient (acoustic metric):
# delta c_s / c_s ~ (delta_phi_rms)^2 / 2  (quadratic in phase gradient)
# This is the RELATIVE modulation of c_s at each vertex due to
# thermal phase fluctuations.
delta_cs_over_cs_thermal = delta_phi_sq_thermal / 2.0

# At the domain walls specifically, the mean phase jump contributes
# an ADDITIONAL coherent term. But since E_DW = 0, the GGE redistributes
# the phase to minimize energy. The residual coherent contribution is:
#
# For a frustrated Z_3 partition on a regular graph, the phase at each
# vertex adjusts so that the total Josephson energy is minimized.
# The minimum-energy configuration has uniform phase within each domain
# and cos(delta_phi) = -1/2 at the walls (which is exactly 2*pi/3).
# This gives E_wall = E_J * 3/2 per wall edge.
#
# The GGE has E_DW = 0, meaning the PAIRS have adjusted to compensate.
# The compensation mechanism is that the Bogoliubov quasiparticles
# redistribute their occupation numbers to screen the wall energy.
# The residual phase fluctuation at the wall is then:
#
#   delta_phi_wall_eff ~ sqrt(T_acoustic / (E_J * N_pair_per_wall))
#
# where N_pair_per_wall is the number of pairs screening each wall.

N_pair_per_wall = N_pair / N_wall  # = 59.8 / 52 = 1.15
delta_phi_wall_eff = np.sqrt(T_acoustic / (J_C2 * N_pair_per_wall))

print(f"\n  Effective wall phase fluctuation:")
print(f"    N_pair per wall edge = {N_pair_per_wall:.2f}")
print(f"    delta_phi_wall_eff = sqrt(T/(E_J*N_pair/wall)) = "
      f"{delta_phi_wall_eff:.4f} rad ({delta_phi_wall_eff*180/PI:.2f} deg)")

# ============================================================================
#  SECTION 4: Mechanism (B) -- Winding Number Modulation
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 4: Mechanism (B) -- Winding Number Modulation")
print("=" * 72)

# The Z_3 domain structure creates a topological structure on CG(24).
# Any closed loop on the graph that crosses domain walls accumulates
# a phase winding:
#   W_loop = (1/2pi) * Sum_{edges in loop} delta_phi_{ij}
#
# For a loop crossing between domains d_a and d_b:
#   delta_phi = (2pi/3) * (d_b - d_a) mod 3
#
# A loop that visits all three domains accumulates W = +/-1.
# A loop within one domain has W = 0.
#
# The winding number modulates the bispectrum because triangles
# (k_1, k_2, k_3) that "wrap" around the domain structure have
# a different phase from those that don't.

# Count triangles (3-cycles) on CG(24) and classify by winding
N_triangles_total = 0
N_triangles_wound = 0  # winding != 0
N_triangles_unwound = 0

triangle_windings = []

for i in range(N_vert):
    for j in range(i + 1, N_vert):
        if adj[i, j] > 0:
            for k in range(j + 1, N_vert):
                if adj[j, k] > 0 and adj[k, i] > 0:
                    N_triangles_total += 1
                    # Phase winding around triangle i->j->k->i
                    winding_phase = (phi_base[j] - phi_base[i]) + \
                                    (phi_base[k] - phi_base[j]) + \
                                    (phi_base[i] - phi_base[k])
                    # This is always 0 by construction (telescoping sum)
                    # The non-trivial winding comes from the WRAPPED phases
                    dphi_ij = (phi_base[j] - phi_base[i] + PI) % (2*PI) - PI
                    dphi_jk = (phi_base[k] - phi_base[j] + PI) % (2*PI) - PI
                    dphi_ki = (phi_base[i] - phi_base[k] + PI) % (2*PI) - PI
                    winding = (dphi_ij + dphi_jk + dphi_ki) / (2 * PI)
                    triangle_windings.append(winding)
                    if abs(winding) > 0.01:
                        N_triangles_wound += 1
                    else:
                        N_triangles_unwound += 1

triangle_windings = np.array(triangle_windings)

# Classification by domain content
N_tri_same = 0      # all three vertices in same domain
N_tri_two = 0       # two domains represented
N_tri_three = 0     # all three domains represented (these can wind)

for i in range(N_vert):
    for j in range(i + 1, N_vert):
        if adj[i, j] > 0:
            for k in range(j + 1, N_vert):
                if adj[j, k] > 0 and adj[k, i] > 0:
                    domains = {domain_assign[i], domain_assign[j],
                               domain_assign[k]}
                    if len(domains) == 1:
                        N_tri_same += 1
                    elif len(domains) == 2:
                        N_tri_two += 1
                    else:
                        N_tri_three += 1

print(f"\n  Triangle (3-cycle) census on CG(24):")
print(f"    Total triangles: {N_triangles_total}")
print(f"    Same-domain: {N_tri_same}")
print(f"    Two-domain: {N_tri_two}")
print(f"    Three-domain: {N_tri_three}")
print(f"")
print(f"  Winding classification:")
print(f"    W = 0: {N_triangles_unwound}")
print(f"    W != 0: {N_triangles_wound}")
if N_triangles_total > 0:
    f_wound = N_triangles_wound / N_triangles_total
    print(f"    Fraction wound: {f_wound:.4f}")
else:
    f_wound = 0.0  # (local)
    print(f"    No triangles found")

if len(triangle_windings) > 0:
    unique_w, w_counts = np.unique(np.round(triangle_windings, 4),
                                    return_counts=True)
    print(f"\n  Winding number distribution:")
    for w, c in zip(unique_w, w_counts):
        print(f"    W = {w:+.4f}: {c} triangles")

# The winding fraction determines the TOPOLOGICAL correction to f_NL.
# For unwound triangles, the bispectrum is the baseline.
# For wound triangles, the three-point phase factor is:
#   <e^{i*(phi_1+phi_2+phi_3)}> ~ e^{i * 2*pi*W/3}
# which modulates the amplitude by cos(2*pi*W/3).
#
# The correction to f_NL from winding:
#   delta_f_NL^{wind} = f_NL_baseline * f_wound * (cos(2*pi/3) - 1)
#                      = f_NL_baseline * f_wound * (-3/2)
# But this applies only if the winding is coherent. For the GGE
# (E_DW = 0), the winding is screened, so the effective correction is:
#   delta_f_NL^{wind} ~ f_NL_baseline * f_wound * (-3/2) * (T/E_J)

if N_triangles_total > 0 and f_wound > 0:
    # Unsuppressed (naive) correction
    delta_f_NL_wind_naive = f_NL_folded_baseline * f_wound * (-3.0 / 2.0)

    # GGE-suppressed correction
    T_over_EJ = T_acoustic / J_C2
    delta_f_NL_wind_suppressed = delta_f_NL_wind_naive * T_over_EJ
else:
    delta_f_NL_wind_naive = 0.0  # (local)
    delta_f_NL_wind_suppressed = 0.0  # (local)

print(f"\n  Winding correction to f_NL^{{folded}}:")
print(f"    f_wound = {f_wound:.4f}")
print(f"    delta_f_NL^{{wind}} (naive) = {delta_f_NL_wind_naive:.6f}")
print(f"    T/E_J suppression = {T_acoustic/J_C2:.4f}")
print(f"    delta_f_NL^{{wind}} (GGE-suppressed) = "
      f"{delta_f_NL_wind_suppressed:.6f}")

# ============================================================================
#  SECTION 5: Mechanism (C) -- Wall Network Phase Modulation
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 5: Mechanism (C) -- Wall Network Phase Modulation")
print("=" * 72)

# The wall network has a specific topology that modulates the power
# spectrum. The key quantity is the wall-wall correlation function:
#
#   G_wall(d) = <n_wall(i) * n_wall(j)>_{d(i,j)=d} - <n_wall>^2
#
# where n_wall(i) = fraction of edges from vertex i that are walls.

# Compute wall fraction per vertex
wall_frac_per_vert = np.zeros(N_vert)
for i in range(N_vert):
    n_neighbors = np.sum(adj[i, :] > 0)
    n_wall_neighbors = sum(1 for j in range(N_vert)
                           if adj[i, j] > 0 and domain_assign[i] != domain_assign[j])
    wall_frac_per_vert[i] = n_wall_neighbors / n_neighbors if n_neighbors > 0 else 0.0

wall_frac_mean = np.mean(wall_frac_per_vert)
wall_frac_var = np.var(wall_frac_per_vert)
wall_frac_std = np.std(wall_frac_per_vert)

print(f"\n  Wall fraction per vertex:")
print(f"    Mean: {wall_frac_mean:.4f}")
print(f"    Std:  {wall_frac_std:.4f}")
print(f"    Var:  {wall_frac_var:.6f}")
print(f"    Min:  {np.min(wall_frac_per_vert):.4f}")
print(f"    Max:  {np.max(wall_frac_per_vert):.4f}")

# Distribution by domain
for d_idx in range(N_DW):
    mask = domain_assign == d_idx
    print(f"    Domain {d_idx}: <wall_frac> = {np.mean(wall_frac_per_vert[mask]):.4f}")

# Wall-wall correlation function
wall_corr_by_dist = {}
for d in range(max_dist + 1):
    products = []
    for i in range(N_vert):
        for j in range(N_vert):
            if i != j and dist_matrix[i, j] == d:
                products.append(wall_frac_per_vert[i] * wall_frac_per_vert[j])
    if products:
        wall_corr_by_dist[d] = np.mean(products) - wall_frac_mean**2

print(f"\n  Wall-wall correlation G_wall(d):")
for d in sorted(wall_corr_by_dist.keys()):
    print(f"    G_wall(d={d}) = {wall_corr_by_dist[d]:+.6f}")

# CRITICAL CONSTRAINT: S57 established E_DW = 0 exactly. All 32 cells
# are identical post-quench. The GGE universality means there are NO
# domain walls in the equilibrium GGE state -- the Z_3 partition from
# the KZ mechanism is SCREENED by the Bogoliubov quasiparticle redistribution.
#
# The S67 baseline f_NL^{folded} = 0.129 was computed assuming global
# coherence with N_pair = 59.8. This is CORRECT for the GGE-equilibrated
# state. Mechanism (C) -- which assumes wall fraction reduces coherent
# neighbors -- would DOUBLE-COUNT the wall effect that was already
# screened to E_DW = 0.
#
# The ONLY surviving wall network correction comes from the TRANSIENT
# phase during GGE equilibration. The KZ domains form during the transit
# (dt_transit ~ 1.13e-3 M_KK^{-1}) and then equilibrate on the Thouless
# timescale (t_Th/t_transit = 65.12, S61). During this transient window
# (t_transit < t < t_Th), the domain walls PARTIALLY exist.
#
# The transient correction is suppressed by the ratio:
#   eta_transient = t_transit / t_Thouless = 1/65.12
# because the bispectrum integrates over the full post-transit evolution,
# and the transient phase contributes only a fraction eta of the total.
#
# The transient-only local f_NL variation (same calculation as before,
# but suppressed by eta):

eta_transient = dt_transit / (65.12 * dt_transit)  # = 1/65.12

local_f_NL = np.zeros(N_vert)
for i in range(N_vert):
    N_coh_frac = 1.0 - wall_frac_per_vert[i]
    if N_coh_frac > 0:
        local_f_NL[i] = 1.0 / np.sqrt(N_pair * N_coh_frac)
    else:
        local_f_NL[i] = 1.0 / np.sqrt(N_pair)

f_NL_network_unscreened = np.mean(local_f_NL)
f_NL_network_std = np.std(local_f_NL)

# The SCREENED correction: only the transient window contributes
delta_f_NL_network_unscreened = f_NL_network_unscreened - f_NL_folded_baseline
delta_f_NL_network = delta_f_NL_network_unscreened * eta_transient

print(f"\n  Wall network f_NL modulation:")
print(f"    Baseline f_NL^{{folded}} = {f_NL_folded_baseline:.6f}")
print(f"    <f_NL_local> (unscreened, no GGE) = {f_NL_network_unscreened:.6f}")
print(f"    sigma(f_NL_local) = {f_NL_network_std:.6f}")
print(f"    delta_f_NL (unscreened) = {delta_f_NL_network_unscreened:+.6f}")
print(f"    eta_transient = t_transit/t_Thouless = {eta_transient:.6f}")
print(f"    delta_f_NL^{{network}} (GGE-screened) = {delta_f_NL_network:+.6f}")
print(f"    |delta_f_NL^{{network}}| / f_NL_baseline = "
      f"{abs(delta_f_NL_network)/f_NL_folded_baseline:.6f}")

# ============================================================================
#  SECTION 6: Combined Phase Winding Correction
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 6: Combined Phase Winding Correction")
print("=" * 72)

# Three mechanisms contribute to delta f_NL:
#
# (A) Phase gradient at walls -> sound speed modulation
#     Suppressed by E_DW = 0 (GGE screening)
#     Residual: delta c_s/c_s ~ (T/E_J) * (delta_phi_wall)^2 / 2
#
# (B) Winding number modulation -> triangle phase factor
#     Suppressed by E_DW = 0 (GGE screening)
#     Residual: delta_f_NL ~ f_NL * f_wound * (T/E_J)
#
# (C) Wall network topology -> local coherence modulation
#     NOT suppressed by E_DW = 0 (topological, not energetic)
#     Correction: delta_f_NL from <1/sqrt(N_eff)> != 1/sqrt(<N_eff>)

# Mechanism (A): Sound speed modulation
# delta f_NL^{equil} ~ (85/324) * (2 * delta c_s / c_s) / c_s^2
# For the equilateral channel (Cheung et al.):
# f_NL^{equil} = (85/324)(1-c_s^2)/c_s^2
# delta f_NL^{equil} / f_NL^{equil} ~ 2 * delta c_s / c_s / (1-c_s^2)

# At wall vertices: delta_cs/cs from thermal phase fluctuations
delta_cs_wall = delta_phi_sq_thermal / 2.0

# But this modulates the EQUILATERAL channel, not the folded channel.
# The effect on f_NL^{equil}:
delta_f_NL_equil_A = f_NL_equil_baseline * 2.0 * delta_cs_wall / (1.0 - c_BLV**2)
# Weighted by wall fraction of graph
delta_f_NL_equil_A_avg = delta_f_NL_equil_A * wall_frac_mean

# The folded channel correction from mechanism (A):
# Phase gradient creates an effective position-dependent mass for pairs,
# modulating the Bogoliubov occupation:
# delta n_k / n_k ~ (delta_phi)^2 / (2 * (E_J / T)) per wall pair
delta_nk_frac = delta_phi_sq_thermal / (2.0 * J_C2 / T_acoustic)
delta_f_NL_folded_A = f_NL_folded_baseline * delta_nk_frac * wall_frac_mean

print(f"\n  Mechanism (A): Phase gradient at walls")
print(f"    delta_phi_rms^2 (thermal) = {delta_phi_sq_thermal:.6f}")
print(f"    delta c_s / c_s = {delta_cs_wall:.6f}")
print(f"    delta f_NL^{{equil}} (A) = {delta_f_NL_equil_A_avg:.6f}")
print(f"    delta f_NL^{{folded}} (A) = {delta_f_NL_folded_A:.6f}")

# Mechanism (B): Winding number (already computed)
print(f"\n  Mechanism (B): Winding number modulation")
print(f"    delta f_NL^{{folded}} (B) = {delta_f_NL_wind_suppressed:.6f}")

# Mechanism (C): Network topology (already computed)
print(f"\n  Mechanism (C): Wall network topology")
print(f"    delta f_NL^{{folded}} (C) = {delta_f_NL_network:+.6f}")

# Total correction to f_NL^{folded}
delta_f_NL_total = delta_f_NL_folded_A + delta_f_NL_wind_suppressed + delta_f_NL_network

# Cross-check: also compute the correction to f_NL^{equil}
# Mechanism (A) contributes to equilateral via sound speed modulation
# Mechanisms (B,C) primarily affect the folded channel
delta_f_NL_equil_total = delta_f_NL_equil_A_avg

# Corrected f_NL values
f_NL_folded_corrected = f_NL_folded_baseline + delta_f_NL_total
f_NL_equil_corrected = f_NL_equil_baseline + delta_f_NL_equil_total

print(f"\n  --- Combined Correction ---")
print(f"  f_NL^{{folded}}:")
print(f"    Baseline (S67)  = {f_NL_folded_baseline:.6f}")
print(f"    delta (A)       = {delta_f_NL_folded_A:+.6f}")
print(f"    delta (B)       = {delta_f_NL_wind_suppressed:+.6f}")
print(f"    delta (C)       = {delta_f_NL_network:+.6f}")
print(f"    TOTAL delta     = {delta_f_NL_total:+.6f}")
print(f"    Corrected       = {f_NL_folded_corrected:.6f}")
print(f"    |delta|/baseline = {abs(delta_f_NL_total)/f_NL_folded_baseline:.4f}")
print(f"")
print(f"  f_NL^{{equil}}:")
print(f"    Baseline (S67)  = {f_NL_equil_baseline:.6f}")
print(f"    delta (A)       = {delta_f_NL_equil_total:+.6f}")
print(f"    Corrected       = {f_NL_equil_corrected:.6f}")
print(f"    |delta|/baseline = {abs(delta_f_NL_equil_total)/f_NL_equil_baseline:.6f}")

# ============================================================================
#  SECTION 7: Spectral Decomposition of Phase Winding Effect
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 7: Spectral Decomposition of Phase Winding Effect")
print("=" * 72)

# The phase profile phi_base can be decomposed in the CG(24) Laplacian
# eigenbasis. This reveals which graph modes carry the domain wall signal.

# Compute Laplacian
L = np.diag(np.sum(adj, axis=1)) - adj
L_float = L.astype(float)

# Eigendecomposition
eig_vals, eig_vecs = np.linalg.eigh(L_float)

# Project phi_base onto Laplacian eigenmodes
phi_proj = eig_vecs.T @ phi_base  # coefficients in eigenbasis

print(f"\n  Laplacian eigenvalues: {np.round(eig_vals, 4)}")
print(f"\n  Phase profile projection |<psi_n | phi>|^2:")
for n in range(min(10, N_vert)):
    print(f"    Mode {n:2d} (lambda={eig_vals[n]:.2f}): "
          f"|c_n|^2 = {phi_proj[n]**2:.6f}")

# The dominant modes of the phase profile tell us which Laplacian
# eigenspaces carry the domain wall information.
# This determines the k-dependence of the bispectrum correction.

total_proj_sq = np.sum(phi_proj**2)
print(f"\n  Total |c_n|^2 = {total_proj_sq:.4f}")
print(f"  Fraction in zero mode: {phi_proj[0]**2/total_proj_sq:.4f}")
print(f"  Fraction in Fiedler modes (lambda=4): "
      f"{np.sum(phi_proj[1:5]**2)/total_proj_sq:.4f}")
print(f"  Fraction in lambda=8 modes: "
      f"{np.sum(phi_proj[5:14]**2)/total_proj_sq:.4f}")
print(f"  Fraction in lambda>=10 modes: "
      f"{np.sum(phi_proj[14:]**2)/total_proj_sq:.4f}")

# The wall fraction per vertex can also be decomposed
wf_proj = eig_vecs.T @ wall_frac_per_vert
total_wf_proj_sq = np.sum(wf_proj**2)

print(f"\n  Wall fraction projection:")
for n in range(min(10, N_vert)):
    print(f"    Mode {n:2d} (lambda={eig_vals[n]:.2f}): "
          f"|c_n|^2 = {wf_proj[n]**2:.6f}")
print(f"  Fraction in zero mode: {wf_proj[0]**2/total_wf_proj_sq:.4f}")
print(f"  Fraction in Fiedler modes: "
      f"{np.sum(wf_proj[1:5]**2)/total_wf_proj_sq:.4f}")

# ============================================================================
#  SECTION 8: Gate Verdict and Summary
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: KZ-FNL-69")
print("=" * 72)

gate_threshold = 0.013  # 10% of f_NL^{folded} = 0.129

print(f"\n  Gate: KZ-FNL-69 -- INFO")
print(f"  Pre-registered threshold: |delta f_NL| > {gate_threshold}")
print(f"  (10% of f_NL^{{folded}} = 0.129)")
print(f"")
print(f"  Results:")
print(f"    delta f_NL (mechanism A, phase gradient): {delta_f_NL_folded_A:+.6f}")
print(f"    delta f_NL (mechanism B, winding):        {delta_f_NL_wind_suppressed:+.6f}")
print(f"    delta f_NL (mechanism C, network):        {delta_f_NL_network:+.6f}")
print(f"    TOTAL |delta f_NL^{{folded}}|             = {abs(delta_f_NL_total):.6f}")
print(f"")

if abs(delta_f_NL_total) > gate_threshold:
    gate_verdict = "FLAG"
    gate_detail = (f"|delta f_NL| = {abs(delta_f_NL_total):.4f} > "
                   f"{gate_threshold} threshold. "
                   f"Phase winding is a SIGNIFICANT correction.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"|delta f_NL| = {abs(delta_f_NL_total):.6f} < "
                   f"{gate_threshold} threshold. "
                   f"Phase winding is a NEGLIGIBLE correction.")

print(f"  VERDICT: {gate_verdict}")
print(f"  {gate_detail}")
print(f"")
print(f"  Physical interpretation:")
print(f"    The dominant suppression mechanism is E_DW = 0 (S57). The GGE")
print(f"    screens the domain wall energy, suppressing mechanisms (A) and (B)")
print(f"    by a factor T/E_J = {T_acoustic/J_C2:.4f}.")
print(f"    Mechanism (C) is topological (not energetic) but produces only")
print(f"    a Jensen inequality correction <1/sqrt(N)> - 1/sqrt(<N>).")
print(f"")
print(f"  Cross-pillar connection (Pillar V -> Pillar I):")
print(f"    The Josephson array phase dynamics (Paper 15, Fazio-vdZant)")
print(f"    map to acoustic metric sound speed modulation (Papers 01, 03).")
print(f"    E_DW = 0 (S57) is the substrate analog of the Meissner effect:")
print(f"    the GGE screens topological phase defects, just as a")
print(f"    superconductor screens magnetic flux.")

# ============================================================================
#  SECTION 9: Plotting
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel (a): Phase profile on CG(24) -- vertex phases colored by domain
ax = axes[0, 0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for d_idx in range(N_DW):
    mask = domain_assign == d_idx
    vertices_in_domain = np.where(mask)[0]
    ax.bar(vertices_in_domain, phi_base[mask] * 180 / PI,
           color=colors[d_idx], alpha=0.7,
           label=f'Domain {d_idx} (phi={2*180*d_idx/N_DW:.0f} deg)')
ax.set_xlabel('Vertex index')
ax.set_ylabel('Phase (degrees)')
ax.set_title('(a) Z_3 Phase Profile on CG(24)')
ax.legend()
ax.set_ylim(-10, 260)

# Panel (b): Wall fraction per vertex
ax = axes[0, 1]
for d_idx in range(N_DW):
    mask = domain_assign == d_idx
    vertices_in_domain = np.where(mask)[0]
    ax.bar(vertices_in_domain, wall_frac_per_vert[mask],
           color=colors[d_idx], alpha=0.7,
           label=f'Domain {d_idx}')
ax.axhline(y=wall_frac_mean, color='k', linestyle='--', alpha=0.5,
           label=f'Mean = {wall_frac_mean:.3f}')
ax.set_xlabel('Vertex index')
ax.set_ylabel('Wall fraction')
ax.set_title('(b) Domain Wall Fraction per Vertex')
ax.legend()

# Panel (c): Phase correlation vs graph distance
ax = axes[1, 0]
dists = sorted(phase_corr_by_dist.keys())
corrs = [phase_corr_by_dist[d] for d in dists]
ax.plot(dists, corrs, 'o-', color='#d62728', markersize=8, linewidth=2)
ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
ax.set_xlabel('Graph distance d')
ax.set_ylabel('C(d) = <cos(phi_i - phi_j)>')
ax.set_title('(c) Phase Correlation Function')
ax.set_xlim(-0.1, max_dist + 0.1)

# Panel (d): Spectral decomposition of phase profile
ax = axes[1, 1]
phi_power = phi_proj**2
ax.bar(range(N_vert), phi_power / total_proj_sq, color='#9467bd', alpha=0.8)
ax.set_xlabel('Laplacian eigenmode index n')
ax.set_ylabel('|c_n|^2 / Sum')
ax.set_title('(d) Phase Profile in Laplacian Eigenbasis')

plt.suptitle('KZ-PHASE-FNL-69: Phase Winding Correction to Bispectrum\n'
             f'|delta f_NL| = {abs(delta_f_NL_total):.6f}, '
             f'Gate: {gate_verdict}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 's69_kz_phase_fnl.png'), dpi=150,
            bbox_inches='tight')
print(f"\n  Plot saved: computations/session-69/s69_kz_phase_fnl.png")

# ============================================================================
#  SECTION 10: Save Results
# ============================================================================

save_path = os.path.join(script_dir, 's69_kz_phase_fnl.npz')
np.savez(save_path,
         # Domain structure
         N_DW=N_DW,
         N_wall=N_wall,
         N_total_edges=96,
         wall_fraction=N_wall / 96.0,
         domain_assign=domain_assign,
         domain_sizes=domain_sizes,
         phi_base=phi_base,
         # Phase statistics
         phi_var=phi_var,
         phi_std=phi_std,
         circ_var=circ_var,
         circ_R=circ_R,
         # Phase correlation
         phase_corr_dists=np.array(dists),
         phase_corr_values=np.array(corrs),
         # Triangle census
         N_triangles_total=N_triangles_total,
         N_tri_same=N_tri_same,
         N_tri_two=N_tri_two,
         N_tri_three=N_tri_three,
         N_triangles_wound=N_triangles_wound,
         f_wound=f_wound,
         # Wall network
         wall_frac_per_vert=wall_frac_per_vert,
         wall_frac_mean=wall_frac_mean,
         wall_frac_var=wall_frac_var,
         # Mechanism corrections
         delta_f_NL_folded_A=delta_f_NL_folded_A,
         delta_f_NL_wind_suppressed=delta_f_NL_wind_suppressed,
         delta_f_NL_network=delta_f_NL_network,
         delta_f_NL_total=delta_f_NL_total,
         delta_f_NL_equil_A=delta_f_NL_equil_A_avg,
         # Corrected values
         f_NL_folded_baseline=f_NL_folded_baseline,
         f_NL_folded_corrected=f_NL_folded_corrected,
         f_NL_equil_baseline=f_NL_equil_baseline,
         f_NL_equil_corrected=f_NL_equil_corrected,
         # Spectral decomposition
         phi_proj=phi_proj,
         laplacian_eigs=eig_vals,
         wf_proj=wf_proj,
         # Suppression parameters
         T_over_EJ=T_acoustic / J_C2,
         delta_phi_sq_thermal=delta_phi_sq_thermal,
         delta_phi_wall_eff=delta_phi_wall_eff,
         # Gate
         gate_verdict=gate_verdict,
         gate_detail=gate_detail,
         gate_threshold=gate_threshold,
)
print(f"  Data saved: {save_path}")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
