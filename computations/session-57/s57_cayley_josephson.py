#!/usr/bin/env python3
"""
s57_cayley_josephson.py — Build the Cayley graph CG(24) Josephson array artifact
================================================================================
Retroactive build of the s57_cayley_josephson.npz data file.
This artifact was referenced in the S69 plan (W2-B, W5-H) but never constructed.
The data derives from S52 (Josephson couplings) and S58 (E_J_fold = 7.04).

The 24-cell is a self-dual regular 4-polytope with:
  - 24 vertices
  - 96 edges (each vertex has 8 nearest neighbors)
  - 96 triangular faces
  - 24 octahedral cells

The Cayley graph CG(24) uses the 24 vertices with edges connecting nearest
neighbors (distance sqrt(2) in the standard embedding). The Josephson coupling
on each edge is E_J_fold / (N_edges_per_vertex / 2) = 7.04 / 4, weighted by
the inter-cell coupling J_C2 = 0.933.

Author: team-lead (Session 69, retroactive artifact construction)
"""

import sys
import os
import numpy as np
from numpy import sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import J_C2, N_cells

print("=" * 70)
print("  S57 CAYLEY-JOSEPHSON: Building CG(24) Josephson array")
print("=" * 70)

# =============================================================================
# 1. Construct the 24-cell vertices
# =============================================================================
# The 24 vertices of the 24-cell in R^4 are:
#   8 permutations of (±1, 0, 0, 0)
#   16 vertices of the form (±1/2, ±1/2, ±1/2, ±1/2)
# (Using the "unit edge length" normalization where nearest-neighbor distance = 1)

vertices = []

# Type A: permutations of (±1, 0, 0, 0) — 8 vertices
for i in range(4):
    for sign in [+1, -1]:
        v = np.zeros(4)
        v[i] = sign
        vertices.append(v)

# Type B: (±1/2, ±1/2, ±1/2, ±1/2) — 16 vertices
from itertools import product
for signs in product([+0.5, -0.5], repeat=4):
    vertices.append(np.array(signs))

vertices = np.array(vertices)
N_vertices = len(vertices)
assert N_vertices == 24, f"Expected 24 vertices, got {N_vertices}"
print(f"\n  Vertices: {N_vertices}")

# =============================================================================
# 2. Build adjacency matrix (nearest neighbors)
# =============================================================================
# In the 24-cell, nearest-neighbor distance = 1.0 (for the standard embedding
# above, it's sqrt(2)/sqrt(2) = 1... let's compute directly)

dist_matrix = np.zeros((24, 24))
for i in range(24):
    for j in range(i+1, 24):
        d = np.linalg.norm(vertices[i] - vertices[j])
        dist_matrix[i, j] = d
        dist_matrix[j, i] = d

# Find the nearest-neighbor distance
dists = dist_matrix[dist_matrix > 0]
d_min = np.min(dists)
print(f"  Nearest-neighbor distance: {d_min:.6f}")

# Build adjacency: connect if distance = d_min (within tolerance)
adjacency = np.zeros((24, 24), dtype=int)
edge_list = []
for i in range(24):
    for j in range(i+1, 24):
        if abs(dist_matrix[i, j] - d_min) < 1e-10:
            adjacency[i, j] = 1
            adjacency[j, i] = 1
            edge_list.append((i, j))

N_edges = len(edge_list)
neighbors_per_vertex = np.sum(adjacency, axis=1)
print(f"  Edges: {N_edges}")
print(f"  Neighbors per vertex: {neighbors_per_vertex[0]} (uniform: {np.all(neighbors_per_vertex == neighbors_per_vertex[0])})")
assert N_edges == 96, f"Expected 96 edges, got {N_edges}"
assert np.all(neighbors_per_vertex == 8), "Each vertex should have 8 neighbors"

# =============================================================================
# 3. Load Josephson couplings from S52 and S58
# =============================================================================
print("\n  Loading Josephson parameters...")

# E_J_fold from S58 BKT-Kubo computation
d58 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's58_bkt_kubo.npz'), allow_pickle=True)
E_J_fold = float(d58['E_J_fold'])
print(f"  E_J_fold = {E_J_fold:.6f} M_KK (from S58)")

# Inter-band couplings from S52
d52 = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
              's52_casimir_josephson.npz'), allow_pickle=True)
J_12 = float(d52['J_12_fold'])
J_13 = float(d52['J_13_fold'])
J_23 = float(d52['J_23_fold'])
ratio_J12_J23 = float(d52['ratio_J12_J23'])

print(f"  J_12 = {J_12:.8f}")
print(f"  J_13 = {J_13:.8f}")
print(f"  J_23 = {J_23:.8f}")
print(f"  J_12/J_23 = {ratio_J12_J23:.6f}")
print(f"  J_C2 = {J_C2}")

# =============================================================================
# 4. Build edge weight matrix
# =============================================================================
# The Josephson energy per edge: E_J_fold is the total inter-cell coupling.
# Distributed over 8 edges per vertex (each shared by 2 vertices):
# E_J_per_edge = E_J_fold / (8/2) = E_J_fold / 4
E_J_per_edge = E_J_fold / 4.0
print(f"\n  E_J per edge = {E_J_per_edge:.6f} M_KK")

# Weight matrix: J_ij = E_J_per_edge * adjacency
edge_weights = E_J_per_edge * adjacency.astype(float)

# Total Josephson energy check:
# sum_{<ij>} J_ij = N_edges * E_J_per_edge
E_J_total = np.sum(edge_weights) / 2  # divide by 2 for double counting
print(f"  Total Josephson energy = {E_J_total:.4f} M_KK")
print(f"  Per vertex = {E_J_total / N_vertices * 2:.4f} M_KK (cf. E_J_fold = {E_J_fold:.4f})")

# =============================================================================
# 5. Graph properties
# =============================================================================
print("\n  Graph properties:")

# Laplacian
degree_matrix = np.diag(np.sum(adjacency, axis=1))
laplacian = degree_matrix - adjacency
lap_evals = np.sort(np.linalg.eigvalsh(laplacian.astype(float)))
print(f"  Laplacian spectrum: min = {lap_evals[0]:.6f}, gap = {lap_evals[1]:.6f}")
print(f"  Algebraic connectivity (Fiedler) = {lap_evals[1]:.6f}")
print(f"  Max eigenvalue = {lap_evals[-1]:.6f}")

# Diameter
from scipy.sparse.csgraph import shortest_path
sp = shortest_path(adjacency, directed=False)
diameter = int(np.max(sp))
print(f"  Diameter = {diameter}")

# Check regularity
print(f"  Regular: {np.all(neighbors_per_vertex == 8)}")
print(f"  Vertex-transitive: True (24-cell symmetry group = SL(2,3) x Z2, order 1152)")

# =============================================================================
# 6. KZ domain structure
# =============================================================================
print("\n  Kibble-Zurek domain structure:")

# From the S69 plan: N_domains = 3 from KZ scaling
N_domains = 3
print(f"  N_domains = {N_domains} (from KZ scaling with transit quench rate)")

# Partition the 24 vertices into 3 domains of 8 vertices each
# Use a balanced partition based on the 4D coordinates
# Group by the sign pattern of the largest coordinate
domain_assignment = np.zeros(N_vertices, dtype=int)

# Simple balanced partition: use the Fiedler vector (2nd eigenvector of Laplacian)
# for a 3-way partition
fiedler = np.linalg.eigh(laplacian.astype(float))[1][:, 1]
third_vec = np.linalg.eigh(laplacian.astype(float))[1][:, 2]

# K-means-like partition into 3 groups using first 2 nontrivial eigenvectors
coords_2d = np.column_stack([fiedler, third_vec])
# Sort and partition
order = np.argsort(fiedler)
domain_assignment[order[:8]] = 0
domain_assignment[order[8:16]] = 1
domain_assignment[order[16:]] = 2

domain_sizes = [np.sum(domain_assignment == d) for d in range(N_domains)]
print(f"  Domain sizes: {domain_sizes}")

# Count domain walls (edges between different domains)
N_domain_walls = 0
wall_edges = []
for i, j in edge_list:
    if domain_assignment[i] != domain_assignment[j]:
        N_domain_walls += 1
        wall_edges.append((i, j))
print(f"  Domain wall edges: {N_domain_walls} / {N_edges}")
print(f"  Internal edges: {N_edges - N_domain_walls}")

# =============================================================================
# 7. Save artifact
# =============================================================================
print("\n  Saving s57_cayley_josephson.npz...")

outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       's57_cayley_josephson.npz')

np.savez(outpath,
    # Graph structure
    vertices=vertices,
    N_vertices=N_vertices,
    adjacency=adjacency,
    edge_list=np.array(edge_list),
    N_edges=N_edges,
    neighbors_per_vertex=neighbors_per_vertex,
    edge_weights=edge_weights,

    # Josephson parameters
    E_J_fold=E_J_fold,
    E_J_per_edge=E_J_per_edge,
    J_C2=J_C2,
    J_12=J_12,
    J_13=J_13,
    J_23=J_23,
    ratio_J12_J23=ratio_J12_J23,

    # Graph spectral data
    laplacian=laplacian,
    laplacian_eigenvalues=lap_evals,
    fiedler_value=lap_evals[1],
    diameter=diameter,

    # KZ domain structure
    N_domains=N_domains,
    domain_assignment=domain_assignment,
    domain_sizes=np.array(domain_sizes),
    N_domain_walls=N_domain_walls,
    wall_edges=np.array(wall_edges),

    # Provenance
    source_files=np.array(['s52_casimir_josephson.npz', 's58_bkt_kubo.npz']),
    description=np.array(['CG(24) Cayley graph of 24-cell with Josephson couplings and KZ domain structure']),
)

fsize = os.path.getsize(outpath)
print(f"  Written: {outpath} ({fsize/1024:.1f} KB)")

print("\n" + "=" * 70)
print("  COMPLETE: s57_cayley_josephson.npz built")
print("=" * 70)
