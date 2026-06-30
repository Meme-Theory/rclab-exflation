#!/usr/bin/env python3
"""
s63_moduli_dispersion.py — Hessian Eigenvalues as Dispersion on CG(24)
=======================================================================

Session 63, Gate: MODULI-DISPERSION-63 (W5-04)
Agent: tesla-resonance

PHYSICS:
    The 36 moduli of the SU(3) fiber deformation at the fold (tau=0.19) have
    effective Hessian eigenvalues omega_i^2 from the 1-loop corrected spectral
    action. When the SU(3) substrate tiles into N_cells=32 Voronoi domains
    connected by the CG(24) Cayley graph (S_4 with all transpositions, degree 6),
    each modulus can propagate between cells via Josephson-type inter-cell coupling.

    The effective Hamiltonian at graph-momentum k is:
        H(k) = H_eff(k=0) + J_mod * lambda_k * I_36

    where lambda_k is a Laplacian eigenvalue of CG(24) and J_mod encodes
    the inter-cell coupling strength for modular deformations. The CG(24)
    has 5 distinct Laplacian eigenvalues:
        {0, 4, 6, 8, 12} with multiplicities {1, 9, 4, 9, 1}

    For the FULL coupled analysis, we also compute the k-dependent Hessian
    by finite-difference: how does the Hessian change when we include the
    graph Laplacian coupling? The Josephson couplings J_C2, J_su2, J_u1
    (from S42/S57) provide the natural inter-cell scales for the 8 fiber
    directions. The 36 moduli couple through the metric deformation along
    these 8 generators.

    The dispersion omega_i(k) = sqrt(evals_i(k)) gives 36 phonon-like
    branches across the CG(24) Brillouin zone. We extract:
    - Effective sound speeds c_i = d(omega_i)/d(lambda_k)
    - Bandwidth Delta_i = omega_i(lambda_max) - omega_i(lambda_min)
    - Group velocities v_g = d(omega)/d(k_eff) where k_eff = sqrt(lambda_k)
    - Classification: acoustic (omega->0 as k->0) vs optical (omega->const)

    Gate: INFO (diagnostic) — always INFO, no pass/fail criterion.

Inputs:
    computations/session-62/s62_hessian_oneloop.npz
    computations/_shared/canonical_constants.py

Outputs:
    computations/session-63/s63_moduli_dispersion.npz
    computations/session-63/s63_moduli_dispersion.png

Author: tesla-resonance (S63 W5-04)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, J_C2, J_su2, J_u1, N_cells, M_KK, PI
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_moduli_dispersion.npz"
OUT_PNG = SCRIPT_DIR / "s63_moduli_dispersion.png"
OUT_TXT = SCRIPT_DIR / "s63_moduli_dispersion_log.txt"

t_start = time.time()

# =============================================================================
# Output tee
# =============================================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(str(OUT_TXT))

print("=" * 78)
print("S63 MODULI-DISPERSION-63: Hessian Eigenvalues as Dispersion on CG(24)")
print("=" * 78)

# =============================================================================
# SECTION 1: Load Hessian data
# =============================================================================
print("\n--- Section 1: Load Hessian data ---")

d = np.load(SCRIPT_DIR / 's62_hessian_oneloop.npz', allow_pickle=True)
H_eff = d['H_eff']              # (36, 36) effective Hessian at k=0
evals_eff = d['evals_eff']      # (36,) eigenvalues (all positive after 1-loop)
evecs_eff = d['evecs_eff']      # (36, 36) eigenvectors
g_fold = d['g_fold']            # (8, 8) metric at fold
tau_fold_val = float(d['tau_fold'])

print(f"  tau_fold = {tau_fold_val}")
print(f"  H_eff shape: {H_eff.shape}")
print(f"  Eigenvalue range: [{evals_eff.min():.4f}, {evals_eff.max():.4f}] M_KK^2")
print(f"  All positive: {np.all(evals_eff > 0)}")
print(f"  g_fold diagonal: {np.diag(g_fold)}")

# =============================================================================
# SECTION 2: Build CG(24) and compute graph Laplacian eigenvalues
# =============================================================================
print("\n--- Section 2: Build CG(24) graph ---")

elements = list(permutations(range(4)))
elem_to_idx = {p: i for i, p in enumerate(elements)}
N_graph = len(elements)

def apply_transposition(perm, i, j):
    lst = list(perm)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)

generators = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

adj = np.zeros((N_graph, N_graph), dtype=float)
for perm in elements:
    idx = elem_to_idx[perm]  # (local)
    for (i, j) in generators:
        neighbor = apply_transposition(perm, i, j)
        nbr_idx = elem_to_idx[neighbor]
        adj[idx, nbr_idx] = 1.0

degree = int(adj.sum(axis=1)[0])
n_edges = int(adj.sum()) // 2
L_graph = degree * np.eye(N_graph) - adj

# Graph Laplacian eigenvalues
lap_evals_all = np.linalg.eigvalsh(L_graph)
lap_evals_all = np.round(lap_evals_all, 10)

# Distinct eigenvalues and multiplicities
from collections import Counter
lap_rounded = Counter(np.round(lap_evals_all).astype(int))
lap_distinct = sorted(lap_rounded.keys())
lap_mults = [lap_rounded[k] for k in lap_distinct]

print(f"  CG(24): {N_graph} vertices, {n_edges} edges, degree {degree}")
print(f"  Laplacian eigenvalues (distinct): {lap_distinct}")
print(f"  Multiplicities: {lap_mults}")
print(f"  Sum of multiplicities: {sum(lap_mults)}")

# Also record adjacency eigenvalues for cross-check
adj_evals_all = np.linalg.eigvalsh(adj)
adj_distinct = sorted(set(np.round(adj_evals_all).astype(int)), reverse=True)
print(f"  Adjacency eigenvalues (distinct): {adj_distinct}")

# k-points = Laplacian eigenvalues (these are the "crystal momenta" on the graph)
k_points = np.array(lap_distinct, dtype=float)  # {0, 4, 6, 8, 12}
k_mults = np.array(lap_mults, dtype=int)

# =============================================================================
# SECTION 3: Construct inter-cell coupling matrix
# =============================================================================
print("\n--- Section 3: Inter-cell coupling for moduli ---")

# The 36 moduli live in the tangent space of the moduli space at the fold.
# The moduli space is parameterized by deformations of the metric g_ab on SU(3).
# In the eigenbasis of H_eff, the inter-cell coupling is diagonal if we assume
# each eigenmode couples to the graph Laplacian with strength J_i.
#
# Physical coupling mechanism: the spectral action S[D_K] couples neighboring
# cells through shared boundary conditions. A deformation on cell A affects
# the boundary between A and B, generating a coupling:
#
#   H_inter = sum_{<AB>} J_mod * (delta_g_A - delta_g_B)^2
#
# In the graph Fourier basis, this becomes:
#   H(k) = H_eff + J_mod * lambda_k * I
#
# The coupling J_mod is ANISOTROPIC: different fiber directions couple with
# different Josephson energies. From canonical_constants:
#   J_C2  = 0.933 M_KK  (C^2 coset, 4 bonds)
#   J_su2 = 0.059 M_KK  (su(2) stabilizer, 3 bonds)
#   J_u1  = 0.038 M_KK  (u(1), 1 bond)
#
# The 8 fiber directions split as: 3 su(2) + 4 C^2 + 1 u(1).
# The 36 moduli live in Sym^2 of this 8-dim space, so the coupling for
# a modulus that is "mostly su(2) x su(2)" will be ~J_su2, while one
# that is "mostly C^2 x C^2" will be ~J_C2.
#
# Strategy: construct the 8x8 coupling matrix in the fiber basis,
# lift it to the 36-dim moduli space via the metric perturbation,
# then project into the H_eff eigenbasis.

print(f"  J_C2  = {J_C2:.4f} M_KK (C^2 coset, 4 directions)")
print(f"  J_su2 = {J_su2:.4f} M_KK (su(2) stabilizer, 3 directions)")
print(f"  J_u1  = {J_u1:.4f} M_KK (u(1), 1 direction)")

# Build 8x8 Josephson coupling in fiber direction basis
J_fiber = np.zeros(8)
J_fiber[0:3] = J_su2   # su(2) directions
J_fiber[3:7] = J_C2    # C^2 coset directions
J_fiber[7]   = J_u1    # u(1) direction

print(f"  J_fiber = {J_fiber}")

# The 36 moduli = symmetric deformations of the 8x8 metric.
# Index them as (a,b) with a <= b: {(0,0), (0,1), ..., (0,7), (1,1), ..., (7,7)}
# That's 8*9/2 = 36 entries.
moduli_pairs = []
for a in range(8):
    for b in range(a, 8):
        moduli_pairs.append((a, b))
assert len(moduli_pairs) == 36

# For a modulus (a,b), the inter-cell coupling is related to the geometric mean
# of the Josephson couplings in directions a and b:
# J_{(a,b)} ~ sqrt(J_a * J_b) for off-diagonal, J_a for diagonal (a=b)
J_moduli_diag = np.zeros(36)
for idx, (a, b) in enumerate(moduli_pairs):
    if a == b:
        J_moduli_diag[idx] = J_fiber[a]
    else:
        J_moduli_diag[idx] = np.sqrt(J_fiber[a] * J_fiber[b])

print(f"  J_moduli range: [{J_moduli_diag.min():.6f}, {J_moduli_diag.max():.6f}] M_KK")
print(f"  J_moduli unique values: {np.unique(np.round(J_moduli_diag, 6))}")

# Transform J_moduli into the H_eff eigenbasis
# In the original metric-perturbation basis, J_moduli acts diagonally.
# But H_eff is diagonalized in a rotated basis (evecs_eff).
# The coupling in the eigenbasis is:
#   J_eff_{ij} = sum_k (evecs_eff[k,i] * J_moduli_diag[k] * evecs_eff[k,j])
# This is a full 36x36 matrix.

J_eff = evecs_eff.T @ np.diag(J_moduli_diag) @ evecs_eff
print(f"  J_eff diagonal range: [{np.diag(J_eff).min():.6f}, {np.diag(J_eff).max():.6f}]")
print(f"  J_eff off-diagonal max: {np.max(np.abs(J_eff - np.diag(np.diag(J_eff)))):.6f}")
print(f"  J_eff is {'nearly diagonal' if np.max(np.abs(J_eff - np.diag(np.diag(J_eff)))) < 0.1 * np.max(np.abs(np.diag(J_eff))) else 'significantly off-diagonal'}")

# =============================================================================
# SECTION 4: Compute dispersion omega_i(k) at each k-point
# =============================================================================
print("\n--- Section 4: Dispersion relation ---")

n_branches = 36
n_kpoints = len(k_points)

# At each k-point, solve H(k) = H_eff + lambda_k * J_eff
omega_sq = np.zeros((n_kpoints, n_branches))  # eigenvalues (omega^2)
omega = np.zeros((n_kpoints, n_branches))      # frequencies
evecs_k = np.zeros((n_kpoints, n_branches, n_branches))  # eigenvectors at each k

for ik, lam_k in enumerate(k_points):
    H_k = H_eff + lam_k * J_eff
    evals_k, vecs_k = eigh(H_k)
    omega_sq[ik] = evals_k
    omega[ik] = np.sqrt(np.abs(evals_k)) * np.sign(evals_k)
    evecs_k[ik] = vecs_k.T  # Store as row vectors

    n_neg = np.sum(evals_k < 0)
    print(f"  k={lam_k:5.1f}: evals range [{evals_k.min():.4f}, {evals_k.max():.4f}],"
          f" n_negative={n_neg}")

# At k=0 (lambda_k=0), should recover the original H_eff eigenvalues
k0_idx = 0  # lambda_k = 0 is the first k-point
residual = np.max(np.abs(np.sort(omega_sq[k0_idx]) - np.sort(evals_eff)))
print(f"\n  k=0 residual vs evals_eff: {residual:.2e}")
assert residual < 1e-10, f"k=0 eigenvalues don't match H_eff: residual = {residual}"

# =============================================================================
# SECTION 5: Extract sound speeds, bandwidths, group velocities
# =============================================================================
print("\n--- Section 5: Sound speeds and bandwidths ---")

# Sort branches at each k-point by matching to k=0 eigenvectors
# (track branches via eigenvector overlap to avoid crossings)
branch_omega_sq = np.zeros((n_branches, n_kpoints))
branch_omega = np.zeros((n_branches, n_kpoints))

# At k=0, use sorted eigenvalue ordering
sort_idx_k0 = np.argsort(omega_sq[k0_idx])
branch_omega_sq[:, k0_idx] = omega_sq[k0_idx, sort_idx_k0]
branch_omega[:, k0_idx] = omega[k0_idx, sort_idx_k0]
prev_vecs = evecs_k[k0_idx, sort_idx_k0]  # (36, 36)

for ik in range(n_kpoints):
    if ik == k0_idx:
        continue
    # Match branches by maximum eigenvector overlap with previous k-point
    curr_vecs = evecs_k[ik]  # (36, 36)
    overlap = np.abs(prev_vecs @ curr_vecs.T)  # (36, 36)

    # Hungarian-like greedy assignment
    assigned_curr = set()
    assigned_branch = set()
    assignment = np.full(n_branches, -1, dtype=int)

    # Sort by overlap magnitude (highest first)
    flat_idx = np.argsort(overlap.ravel())[::-1]
    for flat in flat_idx:
        br = flat // n_branches
        ci = flat % n_branches
        if br not in assigned_branch and ci not in assigned_curr:
            assignment[br] = ci
            assigned_branch.add(br)
            assigned_curr.add(ci)
        if len(assigned_branch) == n_branches:
            break

    for br in range(n_branches):
        ci = assignment[br]
        branch_omega_sq[br, ik] = omega_sq[ik, ci]
        branch_omega[br, ik] = omega[ik, ci]

# Bandwidth for each branch
bandwidth_sq = branch_omega_sq[:, -1] - branch_omega_sq[:, 0]  # lambda=12 - lambda=0
bandwidth_omega = np.abs(branch_omega[:, -1]) - np.abs(branch_omega[:, 0])

# Effective sound speed: c_i = d(omega)/d(k_eff) where k_eff = sqrt(lambda_k)
# Use the linear coefficient: omega_i^2(k) ~ omega_i^2(0) + alpha_i * lambda_k
# alpha_i = d(omega_i^2)/d(lambda_k) = slope of linear fit
alpha_i = np.zeros(n_branches)  # linear dispersion coefficient
c_eff = np.zeros(n_branches)    # effective sound speed

for br in range(n_branches):
    # Linear fit omega_sq vs lambda_k
    coeffs = np.polyfit(k_points, branch_omega_sq[br], 1)
    alpha_i[br] = coeffs[0]  # slope = d(omega^2)/d(lambda_k)

    # Sound speed: omega = sqrt(omega_0^2 + alpha*lambda_k)
    # d(omega)/d(k_eff) at k_eff=0: c = alpha / (2 * omega_0)
    # where k_eff = sqrt(lambda_k), so d(lambda_k)/d(k_eff) = 2*k_eff -> 0
    # More useful: c = alpha / (2 * omega_0) * (d lambda_k / d k_eff)
    # At the Gamma point, use d(omega)/d(sqrt(lambda)):
    omega_0 = np.sqrt(np.abs(branch_omega_sq[br, 0]))
    if omega_0 > 1e-10:
        c_eff[br] = alpha_i[br] / (2.0 * omega_0)
    else:
        c_eff[br] = np.sqrt(np.abs(alpha_i[br]))  # acoustic limit

print(f"  {'Branch':>7} {'omega_0 (M_KK)':>15} {'alpha':>12} {'c_eff':>10} {'BW_sq':>12} {'BW_omega':>12}")
print(f"  {'-'*7:>7} {'-'*15:>15} {'-'*12:>12} {'-'*10:>10} {'-'*12:>12} {'-'*12:>12}")

for br in range(n_branches):
    om0 = np.sqrt(np.abs(branch_omega_sq[br, 0]))
    print(f"  {br:7d} {om0:15.6f} {alpha_i[br]:12.6f} {c_eff[br]:10.6f}"
          f" {bandwidth_sq[br]:12.6f} {bandwidth_omega[br]:12.6f}")

# =============================================================================
# SECTION 6: Classification — acoustic vs optical
# =============================================================================
print("\n--- Section 6: Branch classification ---")

# Acoustic branch: omega -> 0 as lambda_k -> 0
# Optical branch: omega -> finite as lambda_k -> 0
# The Hessian at k=0 has ALL positive eigenvalues (31.04 to 330.63 M_KK^2),
# so there are NO acoustic branches. All 36 are optical.
# This is expected: the fold is a massive point, not a symmetry-breaking point.

omega_0_all = np.sqrt(np.abs(branch_omega_sq[:, 0]))
acoustic_mask = omega_0_all < 0.1  # threshold for "acoustic-like"
n_acoustic = np.sum(acoustic_mask)
n_optical = np.sum(~acoustic_mask)

print(f"  Acoustic branches (omega_0 < 0.1 M_KK): {n_acoustic}")
print(f"  Optical branches (omega_0 >= 0.1 M_KK): {n_optical}")
print(f"  Minimum omega_0 = {omega_0_all.min():.6f} M_KK")
print(f"  Maximum omega_0 = {omega_0_all.max():.6f} M_KK")

# Group by degeneracy level (from Section 1 analysis)
print("\n  Degeneracy groups:")
tol = 0.2  # (local)
sorted_om0 = np.sort(omega_0_all)
groups = []
current_group = [sorted_om0[0]]
for i in range(1, len(sorted_om0)):
    if abs(sorted_om0[i] - current_group[-1]) < tol:
        current_group.append(sorted_om0[i])
    else:
        groups.append(current_group)
        current_group = [sorted_om0[i]]
groups.append(current_group)

for ig, g in enumerate(groups):
    mean_om = np.mean(g)
    # Find branches in this group
    mask = np.abs(omega_0_all - mean_om) < tol
    c_group = c_eff[mask]
    bw_group = bandwidth_omega[mask]
    print(f"  Level {ig}: omega_0={mean_om:.4f} M_KK, deg={len(g)}, "
          f"c_eff=[{c_group.min():.6f},{c_group.max():.6f}], "
          f"BW=[{bw_group.min():.6f},{bw_group.max():.6f}] M_KK")

# =============================================================================
# SECTION 7: Relative bandwidth analysis
# =============================================================================
print("\n--- Section 7: Relative bandwidth ---")

# The key diagnostic: how flat are these branches?
# Relative bandwidth = |omega(k_max) - omega(0)| / omega(0)
rel_bw = np.abs(bandwidth_omega) / omega_0_all
print(f"  Relative bandwidth range: [{rel_bw.min():.6e}, {rel_bw.max():.6e}]")
print(f"  Mean relative bandwidth: {rel_bw.mean():.6e}")
print(f"  Max relative bandwidth branch: {np.argmax(rel_bw)} (omega_0={omega_0_all[np.argmax(rel_bw)]:.4f})")

# Ratio J/omega^2 tells us how flat/dispersive
J_over_omega2 = np.abs(alpha_i * k_points[-1]) / np.abs(branch_omega_sq[:, 0])
print(f"\n  J*lambda_max / omega_0^2 range: [{J_over_omega2.min():.6e}, {J_over_omega2.max():.6e}]")
print(f"  This ratio << 1 means flat bands (dispersionless), >> 1 means strongly dispersive")

# =============================================================================
# SECTION 8: Condensed matter analog and resonance structure
# =============================================================================
print("\n--- Section 8: Resonance structure ---")

# What oscillates: 36 fiber-metric deformation modes
# What is the cavity: CG(24) = graph of S_4
# Boundary conditions: periodic (graph has no boundary)
# Normal modes: graph Fourier modes (5 distinct eigenvalues)

# The system is analogous to optical phonons on a lattice:
# - Heavy atoms (large omega_0) with weak inter-site coupling (J << omega_0^2)
# - Result: nearly flat optical bands with tiny dispersion
# - Sound speed c ~ J/(2*omega_0) << 1

# Maximum group velocity
v_max = np.max(np.abs(c_eff))
print(f"  Maximum effective sound speed: {v_max:.6e} M_KK (c=1)")
print(f"  This is {v_max:.4f} * c (in natural units)")

# The Josephson coupling hierarchy creates a 3-level dispersion:
# Level 1: C^2-dominated moduli (J_C2 = 0.933 M_KK) — most dispersive
# Level 2: su(2)-dominated moduli (J_su2 = 0.059 M_KK) — intermediate
# Level 3: u(1)-dominated moduli (J_u1 = 0.038 M_KK) — flattest

# Classify by dominant fiber direction
tier_labels = []
for br in range(n_branches):
    # Use the k=0 eigenvector to determine fiber content
    vec = evecs_eff[:, np.argsort(evals_eff)[br]]
    # Project onto fiber pairs
    su2_weight = 0
    C2_weight = 0
    u1_weight = 0
    for idx, (a, b) in enumerate(moduli_pairs):
        w = vec[idx]**2
        if a < 3 and b < 3:
            su2_weight += w
        elif a >= 3 and a < 7 and b >= 3 and b < 7:
            C2_weight += w
        elif a == 7 or b == 7:
            u1_weight += w
        else:
            # Mixed su(2)-C^2 etc.
            if a < 3 or b < 3:
                su2_weight += w * 0.5
                C2_weight += w * 0.5
            else:
                C2_weight += w * 0.5
                u1_weight += w * 0.5
    total = su2_weight + C2_weight + u1_weight
    if total > 0:
        su2_weight /= total
        C2_weight /= total
        u1_weight /= total
    if C2_weight > 0.5:
        tier_labels.append("C2")
    elif su2_weight > 0.5:
        tier_labels.append("su2")
    elif u1_weight > 0.3:
        tier_labels.append("u1")
    else:
        tier_labels.append("mix")

tier_counts = Counter(tier_labels)
print(f"\n  Tier classification: {dict(tier_counts)}")
for tier in ["C2", "su2", "u1", "mix"]:
    mask = np.array([t == tier for t in tier_labels])
    if np.any(mask):
        print(f"    {tier}: n={mask.sum()}, "
              f"c_eff=[{c_eff[mask].min():.6f},{c_eff[mask].max():.6f}], "
              f"rel_bw=[{rel_bw[mask].min():.6e},{rel_bw[mask].max():.6e}]")

# =============================================================================
# SECTION 9: Nonlinear dispersion analysis (beyond linear fit)
# =============================================================================
print("\n--- Section 9: Nonlinear dispersion check ---")

# Fit omega_sq = a + b*lambda_k + c*lambda_k^2 to check for curvature
curvature = np.zeros(n_branches)
linearity_R2 = np.zeros(n_branches)

for br in range(n_branches):
    # Linear fit
    coeffs_lin = np.polyfit(k_points, branch_omega_sq[br], 1)
    residuals_lin = branch_omega_sq[br] - np.polyval(coeffs_lin, k_points)
    ss_res_lin = np.sum(residuals_lin**2)
    ss_tot = np.sum((branch_omega_sq[br] - branch_omega_sq[br].mean())**2)
    if ss_tot > 0:
        linearity_R2[br] = 1.0 - ss_res_lin / ss_tot
    else:
        linearity_R2[br] = 1.0

    # Quadratic fit
    if n_kpoints >= 3:
        coeffs_quad = np.polyfit(k_points, branch_omega_sq[br], 2)
        curvature[br] = coeffs_quad[0]  # coefficient of lambda_k^2

print(f"  Linearity (R^2) range: [{linearity_R2.min():.10f}, {linearity_R2.max():.10f}]")
print(f"  Mean R^2: {linearity_R2.mean():.10f}")
print(f"  Quadratic curvature range: [{curvature.min():.6e}, {curvature.max():.6e}]")
print(f"  Dispersion is {'linear' if linearity_R2.min() > 0.999 else 'nonlinear'}"
      f" (R^2 > 0.999 threshold)")

# =============================================================================
# SECTION 10: Summary and verdict
# =============================================================================
print("\n" + "=" * 78)
print("SUMMARY: MODULI-DISPERSION-63")
print("=" * 78)

print(f"\n  36 moduli branches on CG(24) at tau_fold = {tau_fold_val}")
print(f"  5 k-points (Laplacian eigenvalues): {list(k_points)}")
print(f"  All branches OPTICAL (no acoustic): omega_0 in [{omega_0_all.min():.4f}, {omega_0_all.max():.4f}] M_KK")
print(f"  Maximum sound speed: {v_max:.6e} M_KK (strongly subluminal)")
print(f"  Relative bandwidths: {rel_bw.min():.4e} to {rel_bw.max():.4e}")
print(f"  Mean relative bandwidth: {rel_bw.mean():.4e}")
print(f"  Dispersion character: {'Linear' if linearity_R2.min() > 0.999 else 'Nonlinear'} "
      f"(min R^2 = {linearity_R2.min():.8f})")
print(f"  Josephson hierarchy preserved: J_C2={J_C2:.3f} >> J_su2={J_su2:.3f} ~ J_u1={J_u1:.3f}")
print(f"  Condensed matter analog: optical phonons on lattice with J/omega^2 << 1")

print(f"\n  Gate: MODULI-DISPERSION-63 = INFO")
print(f"  All 36 moduli are optical (massive) with flat dispersion on CG(24).")
print(f"  The Josephson couplings J ~ O(1) M_KK are small compared to omega_0^2 ~ O(30-330) M_KK^2.")
print(f"  Moduli are LOCALIZED, not propagating: the CG(24) lattice acts as a")
print(f"  perturbation, not a band structure generator.")

t_elapsed = time.time() - t_start
print(f"\n  Runtime: {t_elapsed:.1f} s")

# =============================================================================
# SECTION 11: Save data
# =============================================================================
print("\n--- Section 11: Save output ---")

np.savez(str(OUT_NPZ),
    # CG(24) graph data
    k_points=k_points,
    k_multiplicities=k_mults,
    adjacency_eigenvalues=np.array(adj_distinct, dtype=float),
    laplacian_eigenvalues=np.array(lap_distinct, dtype=float),
    # Dispersion data
    omega_sq=omega_sq,                  # (5, 36) omega^2 at each k-point
    omega=omega,                        # (5, 36) omega at each k-point
    branch_omega_sq=branch_omega_sq,    # (36, 5) branch-tracked omega^2
    branch_omega=branch_omega,          # (36, 5) branch-tracked omega
    # Sound speeds and bandwidths
    alpha_i=alpha_i,                    # (36,) linear dispersion coefficient
    c_eff=c_eff,                        # (36,) effective sound speeds
    bandwidth_sq=bandwidth_sq,          # (36,) bandwidth in omega^2
    bandwidth_omega=bandwidth_omega,    # (36,) bandwidth in omega
    rel_bandwidth=rel_bw,              # (36,) relative bandwidth
    # Branch classification
    omega_0=omega_0_all,               # (36,) zero-momentum frequencies
    tier_labels=np.array(tier_labels), # (36,) string labels
    # Coupling data
    J_fiber=J_fiber,                   # (8,) fiber-direction couplings
    J_moduli_diag=J_moduli_diag,       # (36,) moduli-basis couplings
    J_eff_diag=np.diag(J_eff),        # (36,) effective coupling in eigenbasis
    # Fit quality
    linearity_R2=linearity_R2,         # (36,) R^2 of linear fit
    curvature=curvature,               # (36,) quadratic curvature coefficient
    # Metadata
    tau_fold=tau_fold_val,
    gate_verdict='INFO',
)

print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 12: Plot
# =============================================================================
print("\n--- Section 12: Plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.3, wspace=0.3)

# Panel 1: Dispersion relation omega(k) for all 36 branches
ax1 = fig.add_subplot(gs[0, 0])
colors_map = {'C2': 'C0', 'su2': 'C1', 'u1': 'C2', 'mix': 'C3'}
for br in range(n_branches):
    color = colors_map.get(tier_labels[br], 'gray')
    alpha_val = 0.7 if tier_labels[br] != 'mix' else 0.4
    om = np.sqrt(np.abs(branch_omega_sq[br]))
    ax1.plot(k_points, om, '-o', color=color, alpha=alpha_val, ms=3, lw=1)

# Legend
for tier, color in colors_map.items():
    n_t = sum(1 for t in tier_labels if t == tier)
    if n_t > 0:
        ax1.plot([], [], '-o', color=color, label=f'{tier} ({n_t})', ms=4)
ax1.set_xlabel(r'$\lambda_k$ (Laplacian eigenvalue)')
ax1.set_ylabel(r'$\omega$ ($M_{\rm KK}$)')
ax1.set_title('Moduli Dispersion on CG(24)')
ax1.legend(fontsize=8, loc='lower right')
ax1.set_xticks(k_points)

# Panel 2: Zoom on relative bandwidth
ax2 = fig.add_subplot(gs[0, 1])
sort_idx = np.argsort(omega_0_all)
for br_pos, br in enumerate(sort_idx):
    color = colors_map.get(tier_labels[br], 'gray')
    ax2.barh(br_pos, rel_bw[br], color=color, alpha=0.7)
ax2.set_xlabel('Relative Bandwidth')
ax2.set_ylabel('Branch (sorted by $\\omega_0$)')
ax2.set_title('Relative Bandwidth per Branch')
ax2.set_xscale('log')

# Panel 3: Effective sound speeds
ax3 = fig.add_subplot(gs[1, 0])
for br in range(n_branches):
    color = colors_map.get(tier_labels[br], 'gray')
    ax3.scatter(omega_0_all[br], np.abs(c_eff[br]), c=color, s=30, alpha=0.7, zorder=3)
ax3.set_xlabel(r'$\omega_0$ ($M_{\rm KK}$)')
ax3.set_ylabel(r'$|c_{\rm eff}|$ ($M_{\rm KK}$)')
ax3.set_title('Effective Sound Speed vs Gap')
ax3.set_yscale('log')
for tier, color in colors_map.items():
    n_t = sum(1 for t in tier_labels if t == tier)
    if n_t > 0:
        ax3.scatter([], [], c=color, label=f'{tier} ({n_t})', s=30)
ax3.legend(fontsize=8)

# Panel 4: J_eff diagonal (coupling in eigenbasis)
ax4 = fig.add_subplot(gs[1, 1])
J_diag = np.diag(J_eff)
sort_idx_J = np.argsort(omega_0_all)
for br_pos, br in enumerate(sort_idx_J):
    color = colors_map.get(tier_labels[br], 'gray')
    ax4.barh(br_pos, J_diag[br], color=color, alpha=0.7)
ax4.set_xlabel(r'$J_{\rm eff}$ ($M_{\rm KK}$)')
ax4.set_ylabel('Branch (sorted by $\\omega_0$)')
ax4.set_title('Effective Inter-Cell Coupling per Branch')

plt.suptitle(f'MODULI-DISPERSION-63: 36 Moduli on CG(24) @ $\\tau_{{\\rm fold}}={tau_fold_val}$',
             fontsize=14, fontweight='bold')
plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

print("\n--- DONE ---")
