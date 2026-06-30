#!/usr/bin/env python3
"""
S58 ANDREEV-PHASE-58: Sub-Gap Andreev Phase Shift and Pi-Junction Search
=========================================================================

Computes Andreev reflection phase shifts for sub-gap Bogoliubov-Anderson modes
on the 32-cell CG(24) fabric, finds a cycle basis for the graph (b_1 = 62),
and checks whether any loop accumulates a total phase within 5% of pi.

Gate: ANDREEV-PHASE-58 (INFO)
Criterion: Any loop phase within 5% of pi?

Input:
  - s56_ba_spectrum.npz: omega_BA(tau, mode), Delta (BCS gap)
  - s54_tb_hamiltonian.npz: adjacency matrix (32x32), bond counts
  - s54_ed_sweep.npz: fold_idx

Output:
  - s58_andreev_phase.npz: all results
  - s58_andreev_phase.png: loop phase distribution + bond phase histogram

Author: Berry Geometric Phase Theorist
Session: 58
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold

# =============================================================================
# 1. LOAD DATA
# =============================================================================

ba_data = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
ed_data = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)
tb_data = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)

# Fold index
fold_idx = int(ed_data['fold_idx'])
tau_fold_val = ed_data['tau_values'][fold_idx]

# BA spectrum at fold
omega_BA_all = ba_data['omega_BA']  # (50, 31)
tau_ba = ba_data['tau_values']
ba_fold_idx = np.argmin(np.abs(tau_ba - tau_fold_val))
omega_BA = omega_BA_all[ba_fold_idx]  # 31 modes

# BCS gap
Delta_GL = float(ba_data['Delta'])

# Adjacency matrix
adjacency = tb_data['adjacency'].astype(int)  # (32, 32)
N_cells = int(tb_data['N_cells'])
n_bonds = int(tb_data['n_bonds_total'])

print(f"tau_fold = {tau_fold_val:.6f}")
print(f"BA fold_idx = {ba_fold_idx}")
print(f"Delta_GL = {Delta_GL:.6f}")
print(f"2*Delta_GL = {2*Delta_GL:.6f}")
print(f"N_cells = {N_cells}, n_bonds = {n_bonds}")
print(f"b_1 = {n_bonds} - {N_cells} + 1 = {n_bonds - N_cells + 1}")

# =============================================================================
# 2. IDENTIFY SUB-GAP MODES AND COMPUTE ANDREEV PHASE SHIFTS
# =============================================================================

# Andreev reflection phase: phi_A(n) = arccos(omega / Delta_gap)
# where Delta_gap = 2*Delta for the full gap (pair-breaking threshold)
# Sub-gap condition: omega < 2*Delta
#
# Physical picture (Berry, Paper 03 -- diabolical points and Andreev reflection):
# At a superconductor-normal interface, an electron with energy E < Delta
# retroreflects as a hole with phase shift phi = arccos(E/Delta).
# Here the BA modes are collective excitations of the BCS condensate on each cell.
# The Andreev phase shift per bond reflects the mismatch between the BA mode
# energy and the local pair-breaking threshold.

two_Delta = 2 * Delta_GL
sub_gap_mask = omega_BA < two_Delta
n_sub_gap = np.sum(sub_gap_mask)
omega_sub_gap = omega_BA[sub_gap_mask]

print(f"\nSub-gap modes: {n_sub_gap}/{len(omega_BA)}")
print(f"Sub-gap omega range: [{omega_sub_gap.min():.4f}, {omega_sub_gap.max():.4f}]")

# Compute Andreev phase for each sub-gap mode
# phi_A = arccos(omega / (2*Delta))
phi_A_sub_gap = np.arccos(omega_sub_gap / two_Delta)
print(f"Andreev phases (rad): [{phi_A_sub_gap.min():.4f}, {phi_A_sub_gap.max():.4f}]")
print(f"Andreev phases (pi):  [{phi_A_sub_gap.min()/np.pi:.4f}, {phi_A_sub_gap.max()/np.pi:.4f}]")

# All modes (sub-gap get Andreev phase, above-gap get 0)
phi_A_all = np.zeros(len(omega_BA))
phi_A_all[sub_gap_mask] = phi_A_sub_gap

print(f"\nAll Andreev phases (rad):")
for i, (omega, phi) in enumerate(zip(omega_BA, phi_A_all)):
    status = "SUB-GAP" if omega < two_Delta else "ABOVE"
    print(f"  mode {i:2d}: omega={omega:.4f}, phi_A={phi:.4f} ({phi/np.pi:.4f}*pi) [{status}]")

# =============================================================================
# 3. EXTRACT BONDS AND BUILD CYCLE BASIS
# =============================================================================

# Extract bond list from adjacency matrix (upper triangle)
bonds = []
for i in range(N_cells):
    for j in range(i+1, N_cells):
        if adjacency[i, j] != 0:
            bonds.append((i, j))

assert len(bonds) == n_bonds, f"Bond count mismatch: {len(bonds)} vs {n_bonds}"
print(f"\nBonds extracted: {len(bonds)}")

# Build spanning tree using BFS from vertex 0
visited = set()
tree_edges = set()
parent = {}
queue = [0]
visited.add(0)

while queue:
    v = queue.pop(0)
    for u in range(N_cells):
        if adjacency[v, u] != 0 and u not in visited:
            visited.add(u)
            parent[u] = v
            tree_edges.add((min(v, u), max(v, u)))
            queue.append(u)

n_tree = len(tree_edges)
print(f"Spanning tree edges: {n_tree} (should be {N_cells - 1})")
assert n_tree == N_cells - 1

# Non-tree edges generate fundamental cycles
non_tree = [b for b in bonds if b not in tree_edges]
b1 = len(non_tree)
print(f"Non-tree edges (b_1): {b1} (should be {n_bonds - N_cells + 1})")
assert b1 == n_bonds - N_cells + 1

# For each non-tree edge (u,v), find the fundamental cycle:
# path from u to v in the spanning tree + the edge (u,v)
def path_to_root(node, parent_dict):
    path = [node]
    while node in parent_dict:
        node = parent_dict[node]
        path.append(node)
    return path

cycles = []
cycle_bonds = []  # list of bond-index sets for each cycle

for edge_idx, (u, v) in enumerate(non_tree):
    # Find paths from u and v to root
    path_u = path_to_root(u, parent)
    path_v = path_to_root(v, parent)

    # Find LCA (lowest common ancestor)
    set_u = set(path_u)
    lca = None
    for node in path_v:
        if node in set_u:
            lca = node
            break

    # Build cycle: u -> lca -> v -> u
    cycle_u = []
    n = u
    while n != lca:
        cycle_u.append(n)
        n = parent[n]
    cycle_u.append(lca)

    cycle_v = []
    n = v
    while n != lca:
        cycle_v.append(n)
        n = parent[n]
    # Don't include lca again

    # Full cycle: u -> ... -> lca -> ... -> v (then edge v->u closes it)
    cycle = cycle_u + list(reversed(cycle_v))
    cycles.append(cycle)

    # Extract bonds in this cycle
    cbonds = []
    for k in range(len(cycle)):
        a = cycle[k]
        b = cycle[(k+1) % len(cycle)]
        bond = (min(a, b), max(a, b))
        # Find bond index
        bond_idx = bonds.index(bond)
        cbonds.append(bond_idx)
    cycle_bonds.append(cbonds)

print(f"\nCycles found: {len(cycles)}")
cycle_lengths = [len(c) for c in cycles]
print(f"Cycle lengths: min={min(cycle_lengths)}, max={max(cycle_lengths)}, "
      f"mean={np.mean(cycle_lengths):.1f}")

# =============================================================================
# 4. ASSIGN ANDREEV PHASES TO BONDS AND COMPUTE LOOP PHASES
# =============================================================================

# Strategy: Each bond carries a phase. The simplest physical assignment is that
# each bond mediates Andreev reflection for all sub-gap modes that propagate
# across it. The total phase per bond is the sum of Andreev phases for all
# sub-gap modes.
#
# However, a more geometric approach recognizes that the BA modes are
# eigenmodes of the Laplacian on CG(24), so each mode has a specific
# spatial profile. The phase accumulated by mode n along bond (i,j) depends
# on the eigenvector amplitude.
#
# We implement BOTH approaches:
# (A) Uniform: each bond carries the MEAN Andreev phase of all sub-gap modes
# (B) Mode-resolved: for each mode n, assign phi_A(n) to each bond weighted
#     by the mode's Laplacian eigenvector overlap, then sum over modes

# --- Approach A: Uniform bond phase ---
mean_phi = np.mean(phi_A_sub_gap)
print(f"\n=== Approach A: Uniform bond phase ===")
print(f"Mean Andreev phase per bond: {mean_phi:.6f} rad ({mean_phi/np.pi:.6f}*pi)")

loop_phases_A = np.zeros(b1)
for c_idx, cbonds in enumerate(cycle_bonds):
    loop_phases_A[c_idx] = len(cbonds) * mean_phi

print(f"Loop phases (uniform): [{loop_phases_A.min():.4f}, {loop_phases_A.max():.4f}] rad")
print(f"Loop phases (pi):      [{loop_phases_A.min()/np.pi:.4f}, {loop_phases_A.max()/np.pi:.4f}]")

# --- Approach B: Mode-resolved with Laplacian eigenvectors ---
# The Laplacian eigenvectors give the spatial profile of each BA mode.
# Load Laplacian eigenvalues (from BA spectrum data)
laplacian_eigs = ba_data['laplacian_eigs']  # (32,) -- includes zero mode
print(f"\n=== Approach B: Mode-resolved (Laplacian eigenvector weighted) ===")

# Compute Laplacian from adjacency
degree = np.sum(adjacency, axis=1)
Laplacian = np.diag(degree) - adjacency
L_evals, L_evecs = np.linalg.eigh(Laplacian.astype(float))
# L_evecs columns are eigenvectors, sorted by eigenvalue

# The 31 non-zero modes correspond to L_evals[1:] (skip zero mode)
# BA mode n corresponds to Laplacian eigenmode n+1

# For each bond (i,j), the contribution of mode n is proportional to
# |psi_n(i) - psi_n(j)|^2, which measures how much mode n oscillates
# across that bond.

# Compute bond weights for each mode
bond_mode_weight = np.zeros((n_bonds, 31))
for b_idx, (i, j) in enumerate(bonds):
    for m in range(31):
        # Mode m corresponds to Laplacian eigenvector m+1
        psi_i = L_evecs[i, m+1]
        psi_j = L_evecs[j, m+1]
        bond_mode_weight[b_idx, m] = (psi_i - psi_j)**2

# Normalize: for each bond, weights sum to 1 (fraction of total mode activity)
bond_weight_sum = np.sum(bond_mode_weight, axis=1)
bond_mode_weight_norm = bond_mode_weight / bond_weight_sum[:, None]

# Phase per bond = sum over sub-gap modes of weight * phi_A
phi_bond_B = np.zeros(n_bonds)
for b_idx in range(n_bonds):
    for m in range(31):
        if sub_gap_mask[m]:
            phi_bond_B[b_idx] += bond_mode_weight_norm[b_idx, m] * phi_A_all[m]

print(f"Bond phases: [{phi_bond_B.min():.6f}, {phi_bond_B.max():.6f}] rad")
print(f"Bond phases (pi): [{phi_bond_B.min()/np.pi:.6f}, {phi_bond_B.max()/np.pi:.6f}]")

# Loop phases for approach B
loop_phases_B = np.zeros(b1)
for c_idx, cbonds in enumerate(cycle_bonds):
    loop_phases_B[c_idx] = np.sum(phi_bond_B[cbonds])

print(f"Loop phases (mode-resolved): [{loop_phases_B.min():.4f}, {loop_phases_B.max():.4f}] rad")
print(f"Loop phases (pi):            [{loop_phases_B.min()/np.pi:.4f}, {loop_phases_B.max()/np.pi:.4f}]")

# --- Approach C: Per-mode loop phases ---
# For each sub-gap mode, compute the loop phase independently
# This is the most physically transparent: does ANY single mode
# produce a pi-junction on ANY loop?
print(f"\n=== Approach C: Per-mode loop phases ===")

n_pi_junctions_C = 0
pi_junction_records = []

for m in range(31):
    if not sub_gap_mask[m]:
        continue
    phi_m = phi_A_all[m]
    for c_idx, cbonds in enumerate(cycle_bonds):
        loop_phase = len(cbonds) * phi_m  # uniform phase per bond for this mode
        # Reduce to [0, 2*pi)
        loop_phase_mod = loop_phase % (2 * np.pi)
        # Check proximity to pi
        dist_to_pi = min(abs(loop_phase_mod - np.pi), abs(loop_phase_mod - np.pi + 2*np.pi), abs(loop_phase_mod - np.pi - 2*np.pi))
        if dist_to_pi < 0.05 * np.pi:
            n_pi_junctions_C += 1
            pi_junction_records.append({
                'mode': m,
                'cycle': c_idx,
                'cycle_len': len(cbonds),
                'phi_A': phi_m,
                'loop_phase': loop_phase,
                'loop_phase_mod': loop_phase_mod,
                'dist_to_pi': dist_to_pi,
                'dist_to_pi_frac': dist_to_pi / np.pi
            })

print(f"Pi-junctions found (per-mode): {n_pi_junctions_C}")
for rec in pi_junction_records[:20]:
    print(f"  mode {rec['mode']}, cycle {rec['cycle']} (len={rec['cycle_len']}): "
          f"phi_A={rec['phi_A']:.4f}, loop_phase_mod={rec['loop_phase_mod']:.4f} "
          f"({rec['loop_phase_mod']/np.pi:.4f}*pi), dist={rec['dist_to_pi_frac']:.4f}*pi")

# =============================================================================
# 5. COMPREHENSIVE PI-JUNCTION CHECK
# =============================================================================

print(f"\n{'='*70}")
print(f"COMPREHENSIVE PI-JUNCTION ANALYSIS")
print(f"{'='*70}")

# Reduce all loop phases mod 2*pi
loop_phases_A_mod = loop_phases_A % (2 * np.pi)
loop_phases_B_mod = loop_phases_B % (2 * np.pi)

# Distance to pi for each loop
dist_A = np.minimum(np.abs(loop_phases_A_mod - np.pi),
                     2*np.pi - np.abs(loop_phases_A_mod - np.pi))
dist_B = np.minimum(np.abs(loop_phases_B_mod - np.pi),
                     2*np.pi - np.abs(loop_phases_B_mod - np.pi))

threshold = 0.05 * np.pi  # (local)

pi_loops_A = np.sum(dist_A < threshold)
pi_loops_B = np.sum(dist_B < threshold)

print(f"\nApproach A (uniform): {pi_loops_A}/{b1} loops within 5% of pi")
print(f"  Closest to pi: loop {np.argmin(dist_A)}, dist={dist_A.min():.6f} rad "
      f"({dist_A.min()/np.pi:.6f}*pi)")

print(f"\nApproach B (mode-resolved): {pi_loops_B}/{b1} loops within 5% of pi")
print(f"  Closest to pi: loop {np.argmin(dist_B)}, dist={dist_B.min():.6f} rad "
      f"({dist_B.min()/np.pi:.6f}*pi)")

print(f"\nApproach C (per-mode): {n_pi_junctions_C} (mode, loop) pairs within 5% of pi")

# Statistics
print(f"\n--- Loop Phase Distribution (Approach A, mod 2*pi) ---")
print(f"  mean = {np.mean(loop_phases_A_mod):.4f} ({np.mean(loop_phases_A_mod)/np.pi:.4f}*pi)")
print(f"  std  = {np.std(loop_phases_A_mod):.4f} ({np.std(loop_phases_A_mod)/np.pi:.4f}*pi)")
print(f"  min  = {np.min(loop_phases_A_mod):.4f} ({np.min(loop_phases_A_mod)/np.pi:.4f}*pi)")
print(f"  max  = {np.max(loop_phases_A_mod):.4f} ({np.max(loop_phases_A_mod)/np.pi:.4f}*pi)")

print(f"\n--- Loop Phase Distribution (Approach B, mod 2*pi) ---")
print(f"  mean = {np.mean(loop_phases_B_mod):.4f} ({np.mean(loop_phases_B_mod)/np.pi:.4f}*pi)")
print(f"  std  = {np.std(loop_phases_B_mod):.4f} ({np.std(loop_phases_B_mod)/np.pi:.4f}*pi)")
print(f"  min  = {np.min(loop_phases_B_mod):.4f} ({np.min(loop_phases_B_mod)/np.pi:.4f}*pi)")
print(f"  max  = {np.max(loop_phases_B_mod):.4f} ({np.max(loop_phases_B_mod)/np.pi:.4f}*pi)")

# =============================================================================
# 6. GATE VERDICT
# =============================================================================

any_pi = (pi_loops_A > 0) or (pi_loops_B > 0) or (n_pi_junctions_C > 0)
gate_verdict = "INFO"
if any_pi:
    gate_detail = (f"PI-JUNCTIONS FOUND: A={pi_loops_A}/{b1}, B={pi_loops_B}/{b1}, "
                   f"C={n_pi_junctions_C} pairs. Frustrated ground states possible.")
else:
    gate_detail = (f"NO PI-JUNCTIONS: A={pi_loops_A}/{b1}, B={pi_loops_B}/{b1}, "
                   f"C={n_pi_junctions_C} pairs. All loop phases far from pi. "
                   f"Closest: {min(dist_A.min(), dist_B.min())/np.pi:.4f}*pi from pi.")

print(f"\n{'='*70}")
print(f"GATE: ANDREEV-PHASE-58 = {gate_verdict}")
print(f"  {gate_detail}")
print(f"{'='*70}")

# =============================================================================
# 7. SAVE DATA
# =============================================================================

np.savez('computations/session-58/s58_andreev_phase.npz',
    # Input parameters
    tau_fold=tau_fold_val,
    ba_fold_idx=ba_fold_idx,
    Delta_GL=Delta_GL,
    two_Delta=two_Delta,
    N_cells=N_cells,
    n_bonds=n_bonds,
    b1=b1,

    # Mode data
    omega_BA=omega_BA,
    sub_gap_mask=sub_gap_mask,
    n_sub_gap=n_sub_gap,
    phi_A_all=phi_A_all,
    phi_A_sub_gap=phi_A_sub_gap,

    # Cycle basis
    cycle_lengths=np.array(cycle_lengths),

    # Approach A
    mean_phi_A=mean_phi,
    loop_phases_A=loop_phases_A,
    loop_phases_A_mod=loop_phases_A_mod,
    dist_to_pi_A=dist_A,
    n_pi_A=pi_loops_A,

    # Approach B
    phi_bond_B=phi_bond_B,
    loop_phases_B=loop_phases_B,
    loop_phases_B_mod=loop_phases_B_mod,
    dist_to_pi_B=dist_B,
    n_pi_B=pi_loops_B,

    # Approach C
    n_pi_C=n_pi_junctions_C,

    # Gate
    gate_name='ANDREEV-PHASE-58',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail
)
print(f"\nData saved: computations/session-58/s58_andreev_phase.npz")

# =============================================================================
# 8. PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'ANDREEV-PHASE-58: Sub-Gap Andreev Phases on CG(24)\n'
             f'tau_fold={tau_fold_val:.4f}, Delta_GL={Delta_GL:.4f}, '
             f'2*Delta={two_Delta:.4f}', fontsize=13)

# Panel 1: BA spectrum with gap
ax = axes[0, 0]
ax.bar(range(31), omega_BA, color=['steelblue' if m else 'gray'
       for m in sub_gap_mask], alpha=0.8)
ax.axhline(two_Delta, color='red', ls='--', lw=2, label=f'2*Delta={two_Delta:.3f}')
ax.set_xlabel('BA mode index')
ax.set_ylabel('omega_BA (M_KK)')
ax.set_title(f'BA Spectrum at Fold ({n_sub_gap}/31 sub-gap)')
ax.legend()

# Panel 2: Andreev phase per mode
ax = axes[0, 1]
sub_idx = np.where(sub_gap_mask)[0]
ax.bar(sub_idx, phi_A_sub_gap / np.pi, color='steelblue', alpha=0.8)
ax.axhline(0.5, color='red', ls='--', lw=1.5, label='pi/2')
ax.axhline(1.0, color='darkred', ls='--', lw=1.5, label='pi')
ax.set_xlabel('BA mode index')
ax.set_ylabel('phi_A / pi')
ax.set_title('Andreev Phase per Sub-Gap Mode')
ax.legend()

# Panel 3: Loop phase distribution (A and B)
ax = axes[1, 0]
bins = np.linspace(0, 2*np.pi, 25)
ax.hist(loop_phases_A_mod, bins=bins, alpha=0.6, label='Uniform (A)', color='steelblue')
ax.hist(loop_phases_B_mod, bins=bins, alpha=0.6, label='Mode-resolved (B)', color='coral')
ax.axvline(np.pi, color='red', ls='--', lw=2, label='pi')
ax.axvspan(np.pi - threshold, np.pi + threshold, alpha=0.15, color='red',
           label='5% window')
ax.set_xlabel('Loop phase mod 2*pi (rad)')
ax.set_ylabel('Count')
ax.set_title(f'Loop Phase Distribution (b_1={b1})')
ax.legend(fontsize=8)

# Panel 4: Distance to pi for all loops
ax = axes[1, 1]
sorted_dist_A = np.sort(dist_A / np.pi)
sorted_dist_B = np.sort(dist_B / np.pi)
ax.plot(range(b1), sorted_dist_A, 'o-', ms=4, label='Uniform (A)', alpha=0.7)
ax.plot(range(b1), sorted_dist_B, 's-', ms=4, label='Mode-resolved (B)', alpha=0.7)
ax.axhline(0.05, color='red', ls='--', lw=1.5, label='5% threshold')
ax.set_xlabel('Loop (sorted by distance to pi)')
ax.set_ylabel('|phase - pi| / pi')
ax.set_title('Distance to Pi-Junction')
ax.legend()
ax.set_ylim(bottom=0)

plt.tight_layout()
plt.savefig('computations/session-58/s58_andreev_phase.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: computations/session-58/s58_andreev_phase.png")
print("\nDone.")
