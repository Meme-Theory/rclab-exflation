#!/usr/bin/env python3
"""
s57_percolation_cc.py — Percolation Threshold on the 32-Cell Tessellation Graph
================================================================================
Gate: PERCOLATION-CC-57 (INFO)

Computes the bond percolation structure of the 32-cell CG graph as a function
of modulus tau. At each tau, bonds with E_J(tau)/H(tau) > 1 are "coherent"
(connected); the rest are "broken". We track:
  1. Connected component structure vs tau
  2. Largest connected component size
  3. Number of domains
  4. Percolation threshold p_c for the specific graph topology
  5. Physical fragmentation tau

Three bond types with distinct Josephson couplings:
  - C2 bonds (50): E_J = J_C2(tau)^2 * F_anom(tau)
  - su2 bonds (24): E_J = J_su2(tau)^2 * F_anom(tau)
  - u1 bonds (19): E_J = J_u1(tau)^2 * F_anom(tau)

Session 57, Wave 3-2. Primary: SP. Co-assigned: Einstein.
"""

import numpy as np
from scipy.interpolate import interp1d
from collections import deque
import sys
sys.path.insert(0, '.')
from canonical_constants import J_C2, J_su2, J_u1, tau_fold

# ============================================================================
#  SECTION 1: Load data
# ============================================================================

d54 = np.load('s54_tb_hamiltonian.npz', allow_pickle=True)
d56 = np.load('s56_post_transit_coh.npz', allow_pickle=True)
dsf = np.load('s54_scale_factor.npz', allow_pickle=True)

tau_values = d54['tau_values']  # 50 points in [0, 0.5]
N_cells = int(d54['N_cells'])  # 32

# Adjacency matrices (32x32, int8, symmetric, disjoint bond types)
adj_C2 = d54['adj_C2'].astype(int)
adj_su2 = d54['adj_su2'].astype(int)
adj_u1 = d54['adj_u1'].astype(int)
adj_total = d54['adjacency'].astype(int)

n_bonds_C2 = int(d54['n_bonds_C2'])    # 50
n_bonds_su2 = int(d54['n_bonds_su2'])  # 24
n_bonds_u1 = int(d54['n_bonds_u1'])    # 19
n_bonds_total = int(d54['n_bonds_total'])  # 93

# Josephson couplings vs tau (from TB Hamiltonian)
J_C2_tau = d54['J_C2_tau']    # shape (50,)
J_su2_tau = d54['J_su2_tau']  # shape (50,)
J_u1_tau = d54['J_u1_tau']    # shape (50,)

# Anomalous fraction from equilibrium BCS
F_anom_eq = d56['F_anom_eq']  # shape (50,)

# Hubble parameter — interpolate from 10-point grid to 50 tau values
tau_sf = dsf['tau']
H_sf = dsf['H']
H_interp = interp1d(tau_sf, H_sf, kind='cubic', fill_value='extrapolate')
H_all = H_interp(tau_values)

print(f"Graph: {N_cells} cells, {n_bonds_total} bonds "
      f"({n_bonds_C2} C2 + {n_bonds_su2} su2 + {n_bonds_u1} u1)")
print(f"Diameter: {int(d54['diameter'])}")

# ============================================================================
#  SECTION 2: E_J / H ratios for each bond type
# ============================================================================

# E_J(type, tau) = J_type(tau)^2 * F_anom(tau)
E_J_C2 = J_C2_tau**2 * F_anom_eq
E_J_su2 = J_su2_tau**2 * F_anom_eq
E_J_u1 = J_u1_tau**2 * F_anom_eq

ratio_C2 = E_J_C2 / H_all
ratio_su2 = E_J_su2 / H_all
ratio_u1 = E_J_u1 / H_all

print(f"\nE_J/H ranges:")
print(f"  C2:  [{ratio_C2.min():.4f}, {ratio_C2.max():.4f}]")
print(f"  su2: [{ratio_su2.min():.6f}, {ratio_su2.max():.6f}]")
print(f"  u1:  [{ratio_u1.min():.6f}, {ratio_u1.max():.6f}]")

# ============================================================================
#  SECTION 3: BFS connected component finder
# ============================================================================

def find_connected_components(adj_matrix):
    """Find all connected components via BFS on a symmetric adjacency matrix.
    Returns: list of sets, each set containing node indices of one component."""
    n = adj_matrix.shape[0]
    visited = set()
    components = []
    for start in range(n):
        if start in visited:
            continue
        # BFS from start
        component = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            for neighbor in range(n):
                if adj_matrix[node, neighbor] > 0 and neighbor not in visited:
                    queue.append(neighbor)
        components.append(component)
    return components

# ============================================================================
#  SECTION 4: Percolation structure vs tau
# ============================================================================

N_tau = len(tau_values)

# Arrays to store results
n_domains = np.zeros(N_tau, dtype=int)
largest_component = np.zeros(N_tau, dtype=int)
n_active_bonds = np.zeros(N_tau, dtype=int)
n_active_C2 = np.zeros(N_tau, dtype=int)
n_active_su2 = np.zeros(N_tau, dtype=int)
n_active_u1 = np.zeros(N_tau, dtype=int)
bond_fraction = np.zeros(N_tau)
component_sizes = []  # list of lists

# Also track C2-only percolation (since su2/u1 never activate)
n_domains_C2only = np.zeros(N_tau, dtype=int)
largest_C2only = np.zeros(N_tau, dtype=int)

print(f"\n{'tau':>6} {'r_C2':>7} {'r_su2':>8} {'r_u1':>8} "
      f"{'#C2':>4} {'#su2':>5} {'#u1':>4} {'#tot':>5} "
      f"{'#dom':>5} {'max':>4} {'#dom_C2':>7} {'max_C2':>6}")

for i in range(N_tau):
    tau = tau_values[i]

    # Build active adjacency: bond is active if E_J/H > 1
    active_adj = np.zeros((N_cells, N_cells), dtype=int)

    # C2 bonds
    if ratio_C2[i] > 1.0:
        active_adj += adj_C2
        n_active_C2[i] = n_bonds_C2
    # su2 bonds
    if ratio_su2[i] > 1.0:
        active_adj += adj_su2
        n_active_su2[i] = n_bonds_su2
    # u1 bonds
    if ratio_u1[i] > 1.0:
        active_adj += adj_u1
        n_active_u1[i] = n_bonds_u1

    n_active_bonds[i] = n_active_C2[i] + n_active_su2[i] + n_active_u1[i]
    bond_fraction[i] = n_active_bonds[i] / n_bonds_total

    # Find connected components on the active graph
    comps = find_connected_components(active_adj)
    n_domains[i] = len(comps)
    sizes = sorted([len(c) for c in comps], reverse=True)
    largest_component[i] = sizes[0]
    component_sizes.append(sizes)

    # C2-only percolation
    active_C2 = adj_C2.copy() if ratio_C2[i] > 1.0 else np.zeros_like(adj_C2)
    comps_C2 = find_connected_components(active_C2)
    n_domains_C2only[i] = len(comps_C2)
    sizes_C2 = sorted([len(c) for c in comps_C2], reverse=True)
    largest_C2only[i] = sizes_C2[0]

    if i % 5 == 0 or i == N_tau - 1:
        print(f"{tau:6.3f} {ratio_C2[i]:7.4f} {ratio_su2[i]:8.6f} {ratio_u1[i]:8.6f} "
              f"{n_active_C2[i]:4d} {n_active_su2[i]:5d} {n_active_u1[i]:4d} {n_active_bonds[i]:5d} "
              f"{n_domains[i]:5d} {largest_component[i]:4d} {n_domains_C2only[i]:7d} {largest_C2only[i]:6d}")

# ============================================================================
#  SECTION 5: Find exact fragmentation tau (C2 crossing)
# ============================================================================

# C2 ratio is the only one that crosses 1. Find exact crossing.
ratio_C2_fine = interp1d(tau_values, ratio_C2, kind='cubic')
# Binary search for tau where ratio_C2 = 1
tau_lo, tau_hi = 0.0, 0.5
# First check that it crosses
if ratio_C2[0] > 1.0 and ratio_C2[-1] < 1.0:
    # It crosses from above to below
    for _ in range(100):
        tau_mid = (tau_lo + tau_hi) / 2
        if ratio_C2_fine(tau_mid) > 1.0:
            tau_lo = tau_mid
        else:
            tau_hi = tau_mid
    tau_frag = (tau_lo + tau_hi) / 2
    print(f"\n=== FRAGMENTATION ===")
    print(f"C2 bonds cross E_J/H = 1 at tau_frag = {tau_frag:.6f}")
    print(f"tau_fold = {tau_fold:.3f}")
    print(f"tau_frag / tau_fold = {tau_frag / tau_fold:.3f}")
    print(f"tau_frag {'<' if tau_frag < tau_fold else '>'} tau_fold: "
          f"{'fragmentation BEFORE fold' if tau_frag < tau_fold else 'fragmentation AFTER fold'}")
else:
    tau_frag = np.nan
    print(f"\nNo C2 crossing detected. C2 ratio at tau=0: {ratio_C2[0]:.4f}, at tau=0.5: {ratio_C2[-1]:.4f}")

# ============================================================================
#  SECTION 6: Graph-theoretic percolation threshold
# ============================================================================
# For the specific 32-cell graph with its 93 bonds, compute p_c by Monte Carlo
# bond percolation. At bond occupation probability p, each bond is independently
# present with probability p. We find p_c where percolating cluster first spans
# the graph (largest component = 32).

print(f"\n=== MONTE CARLO BOND PERCOLATION ===")

rng = np.random.default_rng(42)
N_MC = 10000  # MC samples per p value
p_values = np.linspace(0.0, 1.0, 201)

# Extract bond list from adjacency
bonds_all = []
for i in range(N_cells):
    for j in range(i+1, N_cells):
        if adj_total[i, j] > 0:
            bonds_all.append((i, j))
assert len(bonds_all) == n_bonds_total, f"Bond count mismatch: {len(bonds_all)} vs {n_bonds_total}"

# Also separate by type for type-specific percolation
bonds_C2 = []
bonds_su2 = []
bonds_u1 = []
for i in range(N_cells):
    for j in range(i+1, N_cells):
        if adj_C2[i, j] > 0:
            bonds_C2.append((i, j))
        if adj_su2[i, j] > 0:
            bonds_su2.append((i, j))
        if adj_u1[i, j] > 0:
            bonds_u1.append((i, j))

def mc_percolation(bond_list, n_nodes, p_values, n_samples, rng):
    """Monte Carlo bond percolation on a graph defined by bond_list.
    Returns: mean_largest[p], mean_ndomains[p], P_spanning[p]"""
    n_bonds = len(bond_list)
    n_p = len(p_values)
    mean_largest = np.zeros(n_p)
    mean_ndomains = np.zeros(n_p)
    P_spanning = np.zeros(n_p)  # fraction of samples where largest = n_nodes

    for ip, p in enumerate(p_values):
        largest_acc = 0.0  # (local)
        ndom_acc = 0.0  # (local)
        span_acc = 0.0  # (local)
        for _ in range(n_samples):
            # Each bond present with probability p
            present = rng.random(n_bonds) < p
            # Build adjacency
            adj = np.zeros((n_nodes, n_nodes), dtype=int)
            for ib, (bi, bj) in enumerate(bond_list):
                if present[ib]:
                    adj[bi, bj] = 1
                    adj[bj, bi] = 1
            # Find components
            comps = find_connected_components(adj)
            sizes = [len(c) for c in comps]
            max_s = max(sizes)
            largest_acc += max_s
            ndom_acc += len(comps)
            if max_s == n_nodes:
                span_acc += 1
        mean_largest[ip] = largest_acc / n_samples
        mean_ndomains[ip] = ndom_acc / n_samples
        P_spanning[ip] = span_acc / n_samples
    return mean_largest, mean_ndomains, P_spanning

# Full graph percolation
print(f"Running MC percolation on full graph ({n_bonds_total} bonds, {N_MC} samples/p)...")
ml_full, md_full, ps_full = mc_percolation(bonds_all, N_cells, p_values, N_MC, rng)

# C2-only subgraph percolation
print(f"Running MC percolation on C2 subgraph ({n_bonds_C2} bonds, {N_MC} samples/p)...")
ml_C2, md_C2, ps_C2 = mc_percolation(bonds_C2, N_cells, p_values, N_MC, rng)

# Find p_c (where mean_largest / N jumps above 0.5)
def find_pc(p_values, mean_largest, N, threshold=0.5):
    """Find p_c where <L>/N crosses threshold."""
    frac = mean_largest / N
    for i in range(len(p_values) - 1):
        if frac[i] < threshold and frac[i+1] >= threshold:
            # Linear interpolation
            dp = p_values[i+1] - p_values[i]
            df = frac[i+1] - frac[i]
            return p_values[i] + dp * (threshold - frac[i]) / df
    return np.nan

pc_full = find_pc(p_values, ml_full, N_cells)
pc_C2 = find_pc(p_values, ml_C2, N_cells)

print(f"\nPercolation thresholds (<L>/N = 0.5):")
print(f"  Full graph (93 bonds): p_c = {pc_full:.4f}")
print(f"  C2 subgraph (50 bonds): p_c = {pc_C2:.4f}")

# Also find where P(spanning) = 0.5
def find_pc_spanning(p_values, P_spanning, threshold=0.5):
    for i in range(len(p_values) - 1):
        if P_spanning[i] < threshold and P_spanning[i+1] >= threshold:
            dp = p_values[i+1] - p_values[i]
            df = P_spanning[i+1] - P_spanning[i]
            return p_values[i] + dp * (threshold - P_spanning[i]) / df
    return np.nan

pc_span_full = find_pc_spanning(p_values, ps_full)
pc_span_C2 = find_pc_spanning(p_values, ps_C2)
print(f"\nSpanning thresholds (P(L=N) = 0.5):")
print(f"  Full graph: p_c(span) = {pc_span_full:.4f}")
print(f"  C2 subgraph: p_c(span) = {pc_span_C2:.4f}")

# ============================================================================
#  SECTION 7: Graph-specific analysis
# ============================================================================

# C2-only graph properties
print(f"\n=== C2 SUBGRAPH PROPERTIES ===")
deg_C2 = adj_C2.sum(axis=1)
print(f"Degree distribution: min={deg_C2.min()}, max={deg_C2.max()}, "
      f"mean={deg_C2.mean():.2f}")
# Is C2 subgraph connected?
comps_C2_full = find_connected_components(adj_C2)
print(f"C2 subgraph connected components: {len(comps_C2_full)}")
for ic, comp in enumerate(comps_C2_full):
    print(f"  Component {ic}: {len(comp)} nodes")

# ============================================================================
#  SECTION 8: Physical domain structure at key tau values
# ============================================================================

print(f"\n=== DOMAIN STRUCTURE AT KEY TAU VALUES ===")
key_taus = [0.0, 0.05, 0.08, 0.10, 0.15, 0.19, 0.22, 0.30, 0.40, 0.50]

for t_key in key_taus:
    # Find nearest tau index
    idx = np.argmin(np.abs(tau_values - t_key))
    tau = tau_values[idx]

    # Which bond types active?
    c2_on = ratio_C2[idx] > 1.0
    su2_on = ratio_su2[idx] > 1.0
    u1_on = ratio_u1[idx] > 1.0

    active = np.zeros((N_cells, N_cells), dtype=int)
    if c2_on:
        active += adj_C2
    if su2_on:
        active += adj_su2
    if u1_on:
        active += adj_u1

    n_active = int(active.sum()) // 2
    comps = find_connected_components(active)
    sizes = sorted([len(c) for c in comps], reverse=True)

    status = []
    if c2_on: status.append(f"C2({n_bonds_C2})")
    if su2_on: status.append(f"su2({n_bonds_su2})")
    if u1_on: status.append(f"u1({n_bonds_u1})")
    if not status: status.append("NONE")

    print(f"  tau={tau:.3f}: bonds={'+'.join(status)} ({n_active} active), "
          f"domains={len(comps)}, sizes={sizes}")

# ============================================================================
#  SECTION 9: Desert analysis [0.08, 0.49]
# ============================================================================

# The desert is tau in [0.08, 0.49] per S56 coherence data
# Check if ALL bonds are broken throughout the desert
desert_mask = (tau_values >= 0.08) & (tau_values <= 0.49)
desert_taus = tau_values[desert_mask]
max_ratio_in_desert = np.max(np.column_stack([
    ratio_C2[desert_mask], ratio_su2[desert_mask], ratio_u1[desert_mask]
]), axis=1)

print(f"\n=== DESERT ANALYSIS [0.08, 0.49] ===")
print(f"Number of tau points in desert: {desert_mask.sum()}")
print(f"Max E_J/H across all bond types in desert: {max_ratio_in_desert.max():.4f}")

# Check entry/exit
desert_entry_idx = np.where(desert_mask)[0][0]
desert_exit_idx = np.where(desert_mask)[0][-1]
print(f"Desert entry tau={tau_values[desert_entry_idx]:.3f}: "
      f"C2 ratio={ratio_C2[desert_entry_idx]:.4f}")
print(f"Desert exit tau={tau_values[desert_exit_idx]:.3f}: "
      f"C2 ratio={ratio_C2[desert_exit_idx]:.4f}")

# Is there a narrow window where C2 bonds are active at desert entry?
# tau_frag ~ 0.102 and desert starts at 0.08. C2 bonds are STILL ACTIVE at desert entry.
if not np.isnan(tau_frag):
    print(f"\nC2 bonds active in [0, {tau_frag:.3f}]")
    print(f"Desert starts at 0.08 => C2 bonds active for tau in [0.08, {tau_frag:.3f}] inside desert")
    print(f"Width of active desert window: {tau_frag - 0.08:.4f}")

# ============================================================================
#  SECTION 10: Effective bond fraction mapping to tau
# ============================================================================

# At each tau, what fraction of bonds are active?
# This is a step function: either ALL C2 bonds or NONE, etc.
# But we can define a "soft" bond fraction using E_J/H as a continuous variable
# This gives the effective p(tau) for percolation

# Hard threshold: p = n_active / n_total
p_hard = bond_fraction.copy()

# For the C2 subgraph: p = 1 if C2 active, 0 otherwise
p_C2_hard = np.where(ratio_C2 > 1.0, 1.0, 0.0)

print(f"\n=== BOND FRACTION vs TAU ===")
print(f"{'tau':>6} {'p_hard':>7} {'p_C2':>6}")
for i in range(0, N_tau, 5):
    print(f"{tau_values[i]:6.3f} {p_hard[i]:7.3f} {p_C2_hard[i]:6.1f}")

# ============================================================================
#  SECTION 11: Summary statistics
# ============================================================================

# When does the graph first fragment from 1 domain?
first_frag_idx = None
for i in range(N_tau):
    if n_domains[i] > 1:
        first_frag_idx = i
        break

# When does it reach 32 isolated domains?
full_frag_idx = None
for i in range(N_tau):
    if n_domains[i] == N_cells:
        full_frag_idx = i
        break

print(f"\n=== SUMMARY ===")
if first_frag_idx is not None:
    print(f"First fragmentation: tau = {tau_values[first_frag_idx]:.4f} "
          f"({n_domains[first_frag_idx]} domains)")
else:
    print(f"Graph never fully connected (max component = {largest_component.max()})")

if full_frag_idx is not None:
    print(f"Complete fragmentation (32 isolated): tau = {tau_values[full_frag_idx]:.4f}")
else:
    print(f"Never fully fragmented (min component at tau=0.5: {largest_component[-1]})")

print(f"tau_frag (C2 crossing): {tau_frag:.6f}")
print(f"tau_fold: {tau_fold:.3f}")
print(f"BCS freeze: ~0.22")

# Domain size at fold and BCS
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
bcs_idx = np.argmin(np.abs(tau_values - 0.22))

print(f"\nAt fold (tau={tau_values[fold_idx]:.3f}):")
print(f"  Domains: {n_domains[fold_idx]}, largest: {largest_component[fold_idx]}")
print(f"  Active bonds: {n_active_bonds[fold_idx]}")

print(f"\nAt BCS freeze (tau={tau_values[bcs_idx]:.3f}):")
print(f"  Domains: {n_domains[bcs_idx]}, largest: {largest_component[bcs_idx]}")
print(f"  Active bonds: {n_active_bonds[bcs_idx]}")

# Physical interpretation
print(f"\n=== PHYSICAL INTERPRETATION ===")
if n_domains[fold_idx] == N_cells:
    print("At the fold: ALL cells isolated. Single-cell physics applies.")
elif n_domains[fold_idx] == 1:
    print("At the fold: ALL cells connected. Full fabric coherence.")
else:
    print(f"At the fold: {n_domains[fold_idx]} domains, partial coherence.")

if not np.isnan(tau_frag) and tau_frag < tau_fold:
    print(f"Fragmentation at tau={tau_frag:.4f} PRECEDES fold at tau={tau_fold:.3f}")
    print(f"=> Fabric fragments BEFORE reaching the fold.")
    print(f"=> But W2-2 showed desert transit at Mach 2700 => dynamically frozen.")
    print(f"=> Equilibrium fragmentation is PHYSICAL but DYNAMICALLY IRRELEVANT.")

# ============================================================================
#  SECTION 12: C2 subgraph connectivity analysis
# ============================================================================

# Since only C2 bonds ever activate, analyze the C2 subgraph in detail
print(f"\n=== C2 SUBGRAPH DETAILED ANALYSIS ===")
cell_labels = d54['cell_labels']
cell_dims = d54['cell_dims']

# Which cells have C2 bonds?
has_C2 = deg_C2 > 0
print(f"Cells with C2 bonds: {has_C2.sum()} / {N_cells}")
print(f"Cells without C2 bonds (isolated even when C2 active):")
for i in range(N_cells):
    if not has_C2[i]:
        print(f"  Cell {i}: ({cell_labels[i,0]},{cell_labels[i,1]}), "
              f"dim={cell_dims[i]}")

# For cells with C2 bonds: what's the component structure?
print(f"\nC2 subgraph components:")
for ic, comp in enumerate(comps_C2_full):
    labels_in_comp = [f"({cell_labels[c,0]},{cell_labels[c,1]})" for c in sorted(comp)]
    print(f"  Component {ic} ({len(comp)} cells): {', '.join(labels_in_comp)}")

# ============================================================================
#  SECTION 13: Save results
# ============================================================================

# Pad component_sizes to rectangular array
max_n_comp = max(len(s) for s in component_sizes)
comp_sizes_arr = np.zeros((N_tau, max_n_comp), dtype=int)
for i, sizes in enumerate(component_sizes):
    comp_sizes_arr[i, :len(sizes)] = sizes

np.savez('s57_percolation_cc.npz',
    # Tau grid
    tau_values=tau_values,
    N_cells=N_cells,
    n_bonds_total=n_bonds_total,
    n_bonds_C2=n_bonds_C2,
    n_bonds_su2=n_bonds_su2,
    n_bonds_u1=n_bonds_u1,
    # E_J / H ratios
    ratio_C2=ratio_C2,
    ratio_su2=ratio_su2,
    ratio_u1=ratio_u1,
    E_J_C2=E_J_C2,
    E_J_su2=E_J_su2,
    E_J_u1=E_J_u1,
    H_all=H_all,
    # Percolation structure vs tau
    n_domains=n_domains,
    largest_component=largest_component,
    n_active_bonds=n_active_bonds,
    n_active_C2=n_active_C2,
    n_active_su2=n_active_su2,
    n_active_u1=n_active_u1,
    bond_fraction=bond_fraction,
    component_sizes=comp_sizes_arr,
    # C2-only percolation
    n_domains_C2only=n_domains_C2only,
    largest_C2only=largest_C2only,
    # Fragmentation tau
    tau_frag=tau_frag,
    # MC percolation thresholds
    p_values=p_values,
    ml_full=ml_full,
    md_full=md_full,
    ps_full=ps_full,
    ml_C2=ml_C2,
    md_C2=md_C2,
    ps_C2=ps_C2,
    pc_full=pc_full,
    pc_C2=pc_C2,
    pc_span_full=pc_span_full,
    pc_span_C2=pc_span_C2,
    # Gate
    gate_name='PERCOLATION-CC-57',
    gate_verdict='INFO',
    gate_detail=(
        f"32-cell graph: 93 bonds (50 C2 + 24 su2 + 19 u1). "
        f"Only C2 bonds coherent (E_J/H>1) for tau<{tau_frag:.3f}. "
        f"su2/u1 never coherent. Fragmentation at tau={tau_frag:.4f} < fold={tau_fold:.3f}. "
        f"p_c(full)={pc_full:.3f}, p_c(C2)={pc_C2:.3f}. "
        f"All cells isolated at fold/BCS. Desert dynamically inert (W2-2)."
    )
)

print(f"\nSaved: s57_percolation_cc.npz")
print("DONE")
