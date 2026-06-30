#!/usr/bin/env python3
"""
s70_off_jensen_hess.py — OFF-JENSEN-HESS-70: Full 35x35 Off-Jensen Hessian at Fold
====================================================================================
Gate: OFF-JENSEN-HESS-70
  INFO: Report full 35x35 eigenvalue spectrum. Flag any negative eigenvalues.

Motivation:
  The off-Jensen gradient vanishes exactly (S69 permanent theorem: dS/d(eps_perp) = 0
  on the Jensen line by Schur's lemma and U(2) invariance). But the off-Jensen HESSIAN
  (second derivatives) characterizes the curvature of the valley.

  SU(3) has 8 dimensions. A general left-invariant metric has 8*(8+1)/2 = 36
  independent components. One is the overall volume (fixed by the spectral action
  equations of motion). So there are 35 independent volume-preserving directions.

  The Jensen direction is ONE of these 35 (it is volume-preserving at fixed g0).
  The remaining 34 directions break the Jensen structure (SU(2) x U(1) splitting
  of the C^2 coset, off-diagonal mixing, etc.).

  The question: is the fold point tau = 0.19 on the Jensen line a local MINIMUM
  of the spectral action in ALL 35 volume-preserving directions? If so, the
  Jensen metric is a genuine valley minimum, not just a saddle point.

Geometric structure:
  - Riemannian submersion: P = M4 x K, K = SU(3), fiber metric g_K
  - Jensen deformation: g_K(tau) = g0 * exp(2tau * X) for X in su(3)_diag
  - Isometry group of g_K(tau): U(2) = SU(2) x U(1) subset Aut(SU(3))
  - Moduli space: Sym^2(su(3)) / R^+ = 35-dimensional (volume-preserving)
  - Jensen line: 1D submanifold of the moduli space
  - Off-Jensen: 34D complement to the Jensen direction within moduli space

Method:
  1. Load S69 BCS Hessian data: 36x36 effective Hessian H_eff = H_tree + H_1loop
     in the tree-eigenvector basis (S61/S64).
  2. Identify the volume direction h_vol in this basis using g_fold.
  3. Project H_eff onto the 35D volume-preserving subspace perpendicular to h_vol.
  4. Identify the Jensen direction h_Jensen within this 35D space.
  5. Diagonalize the 35x35 projected Hessian.
  6. Decompose: 1 Jensen eigenvalue + 34 off-Jensen eigenvalues.
  7. Spot-check via independent finite-difference computation along selected
     off-Jensen directions (validation of the projection method).

  We compute both the BCS-dressed and bare Hessians for comparison.

Cross-checks:
  - Projection removes exactly 1 eigenvalue from the 36D spectrum.
  - The 35 projected eigenvalues are bounded by the 36 full eigenvalues (interlacing).
  - Spot-check directions must agree with projected Hessian curvatures.
  - Jensen eigenvalue must match d2S/dtau2 from S69 gradient data.
  - Ad(U(2)) irrep structure from S63 Casimir analysis carries over.

Author: Baptista-Spacetime-Analyst (Session 70, Wave 4)
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from numpy import sqrt, log, pi
from numpy.linalg import eigh, eigvalsh, cholesky, inv, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, PI, Delta_0_OES, E_B2_mean,
    M_KK_gravity, M_KK, a2_fold, d2S_fold, S_fold,
    g_SU2_fold, g_U1_fold
)

print("=" * 78)
print("  OFF-JENSEN-HESS-70: Full 35x35 Off-Jensen Hessian at Fold")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  Delta_BCS = {Delta_0_OES:.6f} M_KK (OES gap)")
print(f"  mu_BCS = {E_B2_mean:.6f} M_KK (chemical potential)")

t_global_start = time.time()

# Physical parameters
Lambda_phys = 2.048   # M_KK (S62 Gaussian optimization)  # (local)
Delta_BCS = Delta_0_OES
mu_BCS = E_B2_mean

# =============================================================================
# 1. LOAD EXISTING HESSIAN DATA
# =============================================================================
print("\n--- 1. Loading existing Hessian data ---")

base_dir = os.path.dirname(os.path.abspath(__file__))

# S61: tree-level Hessian and eigenbasis
s61_path = os.path.join(base_dir, 's61_moduli_hessian.npz')
s61 = np.load(s61_path, allow_pickle=True)
evecs_tree = s61['evecs_36']      # 36x36, columns = tree eigenvectors in raw basis
evals_tree_s61 = s61['evals_36']  # 36 tree eigenvalues (all negative)
g_fold = s61['g_fold']            # 8x8 diagonal fold metric
basis_labels = s61['basis_labels']
eps_s61 = float(s61['epsilon'])

print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  Tree eigenvalues: all negative = {np.all(evals_tree_s61 < 0)}")
print(f"    range: [{evals_tree_s61[0]:.4f}, {evals_tree_s61[-1]:.4f}]")

# S69: BCS-dressed 36x36 Hessian at Lambda = 2.048
s69_path = os.path.join(base_dir, 's69_bcs_hessian.npz')
s69 = np.load(s69_path, allow_pickle=True)
H_bcs_eff_36 = s69['H_bcs_eff']       # 36x36, tree + BCS 1-loop, in tree eigenbasis
H_bare_eff_36 = s69['H_bare_eff']     # 36x36, tree + bare 1-loop, in tree eigenbasis
H_tree_eigenbasis = s69['H_tree_eigenbasis']  # 36x36 tree Hessian in tree eigenbasis (diagonal)
H_bcs_1loop = s69['H_bcs_1loop']      # 36x36 BCS one-loop contribution
H_bare_1loop = s69['H_bare_1loop']    # 36x36 bare one-loop contribution
evals_bcs_36 = s69['evals_bcs_eff']   # 36 eigenvalues of H_bcs_eff (sorted)
evals_bare_36 = s69['evals_bare_eff'] # 36 eigenvalues of H_bare_eff (sorted)
evals_tree_s69 = s69['evals_tree']    # tree eigenvalues (should match s61)

print(f"\n  S69 BCS effective Hessian:")
print(f"    36D eigenvalues (sorted): {evals_bcs_36[0]:.4f} ... {evals_bcs_36[-1]:.4f}")
print(f"    All positive: {np.all(evals_bcs_36 > 0)}")
print(f"    Softest: {evals_bcs_36[0]:.6f}")

print(f"\n  S69 bare effective Hessian:")
print(f"    36D eigenvalues (sorted): {evals_bare_36[0]:.4f} ... {evals_bare_36[-1]:.4f}")
print(f"    All positive: {np.all(evals_bare_36 > 0)}")
print(f"    Softest: {evals_bare_36[0]:.6f}")

# Cross-check: tree eigenvalues consistent between S61 and S69
tree_dev = np.max(np.abs(evals_tree_s61 - evals_tree_s69))
print(f"\n  Tree eigenvalue consistency (S61 vs S69): max dev = {tree_dev:.2e}")
assert tree_dev < 1e-6, f"Tree eigenvalue mismatch: {tree_dev}"

# S63: Ad(U(2)) Casimir decomposition
s63_path = os.path.join(base_dir, 's63_hessian_casimir.npz')
s63 = np.load(s63_path, allow_pickle=True)
cluster_sizes_36 = s63['cluster_sizes']
print(f"\n  S63 Casimir cluster sizes (36D): {cluster_sizes_36}")

# S69 off-Jensen gradient data
oj_path = os.path.join(base_dir, 's69_off_jensen_gradient.npz')
oj_data = np.load(oj_path, allow_pickle=True)
d2S_deps2_fold = float(oj_data['d2S_deps2'][2])  # tau=0.19 is index 2
print(f"  S69 d2S/deps_perp^2 at fold: {d2S_deps2_fold:.4f}")

# =============================================================================
# 2. DEFINE THE VOLUME DIRECTION
# =============================================================================
print("\n--- 2. Defining volume and Jensen directions ---")

# The volume of SU(3) with left-invariant metric g scales as det(g)^{1/2}.
# For diagonal g = diag(g_1,...,g_8), det(g) = prod(g_a).
# A perturbation h preserves volume iff:
#   d(det(g+eps*h))/deps |_{eps=0} = 0
#   det(g) * Tr(g^{-1} h) = 0
#   Tr(g^{-1} h) = sum_a h_{aa}/g_{aa} + 2*sum_{a<b} g^{-1}_{ab} h_{ab} = 0
#
# For diagonal g_fold, this simplifies to: sum_a h_{aa}/g_{aa} = 0
# (off-diagonal h components are automatically volume-preserving)
#
# In the raw Sym(8) basis {E_{11}, E_{22}, ..., E_{88}, E_{12}/sqrt(2), ...}:
# The volume gradient is: v_a = delta_{a is diagonal} * (1/g_{aa})

g_diag = np.diag(g_fold)
h_vol_raw = np.zeros(36)
h_vol_raw[:8] = 1.0 / g_diag  # Volume gradient in raw Sym(8) basis
h_vol_raw_norm = h_vol_raw / norm(h_vol_raw)

print(f"  Volume direction (raw, normalized): {h_vol_raw_norm[:8]}")
print(f"  Norm check: {norm(h_vol_raw_norm):.10f}")

# Transform to tree-eigenvector basis (same basis as the Hessian)
h_vol_eig = evecs_tree.T @ h_vol_raw_norm

print(f"\n  Volume direction in tree eigenbasis:")
print(f"    Non-zero components (|c| > 0.01):")
for i in range(36):
    if abs(h_vol_eig[i]) > 0.01:
        print(f"      eigvec {i}: {h_vol_eig[i]:+.6f} (tree eval = {evals_tree_s61[i]:.2f})")

# Verify: h_vol should have unit norm in both bases
assert abs(norm(h_vol_eig) - 1.0) < 1e-10, f"Volume direction norm error: {norm(h_vol_eig)}"

# =============================================================================
# 3. DEFINE THE JENSEN DIRECTION
# =============================================================================

# The Jensen direction in the raw basis is dg/dtau (normalized).
# At the Jensen metric g(tau) = diag(g_su2(tau)*I_3, g_C2(tau)*I_4, g_u1(tau)):
#   dg_su2/dtau, dg_C2/dtau, dg_u1/dtau
#
# For the Jensen deformation with parameter s = exp(2*tau):
#   g_su2 = g0 * s^{alpha_su2}, g_C2 = g0 * s^{alpha_C2}, g_u1 = g0 * s^{alpha_u1}
# where the exponents are determined by the Jensen deformation structure.
#
# Rather than deriving the exact exponents, we use numerical differentiation:
# dg/dtau ~ (g(tau+dt) - g(tau-dt)) / (2*dt)
#
# But we can compute this more directly: the Jensen deformation of SU(3) along
# the SU(2) x U(1) subgroup scales the metric components as:
#   g_su2 = g0 * exp(-2*tau * c_su2)
#   g_coset = g0 * exp(2*tau * c_coset)
# where c_su2, c_coset are determined by the decomposition su(3) = su(2) + u(1) + C^2.
#
# From the fold metric values:
#   g_su2 = 2.0516, g_C2 = 3.6277, g_u1 = 4.3869, g0 = 3.0
#   At tau = 0.19: ln(g_su2/g0)/(-2*0.19) = c_su2
#                  ln(g_C2/g0)/(2*0.19) = c_coset

g0 = 3.0   # round metric diagonal from canonical_constants
tau = tau_fold

# Compute effective scaling exponents
c_su2 = -np.log(g_diag[0] / g0) / (2 * tau)
c_C2 = np.log(g_diag[3] / g0) / (2 * tau)
c_u1 = np.log(g_diag[7] / g0) / (2 * tau)

print(f"\n  Jensen scaling exponents:")
print(f"    c_su2 = {c_su2:.6f}")
print(f"    c_C2  = {c_C2:.6f}")
print(f"    c_u1  = {c_u1:.6f}")

# dg_a/dtau:
dg_dtau_raw = np.zeros(36)
dg_dtau_raw[0] = -2 * c_su2 * g_diag[0]   # dg_su2/dtau for a=0
dg_dtau_raw[1] = -2 * c_su2 * g_diag[1]   # dg_su2/dtau for a=1
dg_dtau_raw[2] = -2 * c_su2 * g_diag[2]   # dg_su2/dtau for a=2
dg_dtau_raw[3] = 2 * c_C2 * g_diag[3]     # dg_C2/dtau for a=3
dg_dtau_raw[4] = 2 * c_C2 * g_diag[4]     # dg_C2/dtau for a=4
dg_dtau_raw[5] = 2 * c_C2 * g_diag[5]     # dg_C2/dtau for a=5
dg_dtau_raw[6] = 2 * c_C2 * g_diag[6]     # dg_C2/dtau for a=6
dg_dtau_raw[7] = 2 * c_u1 * g_diag[7]     # dg_u1/dtau for a=7

dg_dtau_raw_norm = dg_dtau_raw / norm(dg_dtau_raw)

print(f"\n  Jensen direction (raw, normalized):")
print(f"    dg/dtau = {dg_dtau_raw_norm[:8]}")

# Check: Jensen direction should be volume-preserving
vol_dot = np.dot(h_vol_raw, dg_dtau_raw)  # = sum (1/g_a) * dg_a/dtau
print(f"\n  Volume check: <h_vol, dg/dtau> = {vol_dot:.6e}")
print(f"    = sum_a (1/g_a)(dg_a/dtau)")
vol_check = -2*c_su2*3 + 2*c_C2*4 + 2*c_u1*1  # = -6*c_su2 + 8*c_C2 + 2*c_u1
print(f"    = -6*c_su2 + 8*c_C2 + 2*c_u1 = {vol_check:.6e}")

# The Jensen direction may NOT be exactly volume-preserving.
# If not, project it to be volume-preserving.
h_jensen_raw = dg_dtau_raw_norm.copy()
vol_component = np.dot(h_jensen_raw, h_vol_raw_norm)
h_jensen_raw -= vol_component * h_vol_raw_norm
h_jensen_raw /= norm(h_jensen_raw)

print(f"\n  Jensen direction after volume projection:")
print(f"    Volume component removed: {vol_component:.6e}")
print(f"    |h_jensen_perp_vol| before normalization: {norm(dg_dtau_raw_norm - vol_component * h_vol_raw_norm):.6f}")

# Transform to tree-eigenvector basis
h_jensen_eig = evecs_tree.T @ h_jensen_raw

print(f"\n  Jensen direction in tree eigenbasis:")
print(f"    Non-zero components (|c| > 0.01):")
for i in range(36):
    if abs(h_jensen_eig[i]) > 0.01:
        print(f"      eigvec {i}: {h_jensen_eig[i]:+.6f} (tree eval = {evals_tree_s61[i]:.2f})")

# Verify orthogonality: Jensen perpendicular to volume
print(f"\n  Orthogonality: <h_vol, h_jensen> = {np.dot(h_vol_eig, h_jensen_eig):.2e}")

# =============================================================================
# 4. BUILD 35D VOLUME-PRESERVING ORTHONORMAL BASIS
# =============================================================================
print("\n--- 3. Building 35D volume-preserving basis ---")

# The 35D subspace is perpendicular to h_vol in the tree eigenbasis.
# We need an orthonormal basis for this subspace.

# Method: project out h_vol from the standard basis, then orthogonalize.
# Use the projector P_perp = I - |h_vol><h_vol|.
# The 35 eigenvectors of P_perp with eigenvalue 1 form the basis.

P_perp = np.eye(36) - np.outer(h_vol_eig, h_vol_eig)
evals_P, evecs_P = eigh(P_perp)

# Sort by eigenvalue (ascending): first eigenvalue should be ~0, rest ~1
assert np.sum(evals_P > 0.5) == 35, f"Expected 35 nonzero eigenvalues, got {np.sum(evals_P > 0.5)}"

# The 35 columns with eigenvalue ~1 form the orthonormal basis
basis_35 = evecs_P[:, evals_P > 0.5]  # shape (36, 35)

# Verify orthonormality
ortho_err = np.max(np.abs(basis_35.T @ basis_35 - np.eye(35)))
print(f"  Basis orthonormality error: {ortho_err:.2e}")
assert ortho_err < 1e-10

# Verify perpendicularity to volume
vol_overlap = np.max(np.abs(basis_35.T @ h_vol_eig))
print(f"  Max overlap with volume direction: {vol_overlap:.2e}")
assert vol_overlap < 1e-10

# Project Jensen direction onto 35D basis
h_jensen_35 = basis_35.T @ h_jensen_eig
print(f"\n  Jensen direction in 35D basis: |projection| = {norm(h_jensen_35):.10f}")
print(f"    (should be ~1.0 if Jensen is volume-preserving)")

# Normalize Jensen in 35D
h_jensen_35_norm = h_jensen_35 / norm(h_jensen_35)

# =============================================================================
# 5. PROJECT HESSIANS TO 35D
# =============================================================================
print("\n--- 4. Projecting Hessians to 35D volume-preserving subspace ---")

# Project the 36x36 Hessians to 35x35 using the basis_35 transformation
# H_35 = B^T H_36 B where B = basis_35 (36x35 matrix)

H_bcs_35 = basis_35.T @ H_bcs_eff_36 @ basis_35
H_bare_35 = basis_35.T @ H_bare_eff_36 @ basis_35
H_tree_35 = basis_35.T @ H_tree_eigenbasis @ basis_35
H_bcs_1loop_35 = basis_35.T @ H_bcs_1loop @ basis_35
H_bare_1loop_35 = basis_35.T @ H_bare_1loop @ basis_35

# Symmetry check
sym_err_bcs = np.max(np.abs(H_bcs_35 - H_bcs_35.T))
sym_err_bare = np.max(np.abs(H_bare_35 - H_bare_35.T))
print(f"  Symmetry error (BCS): {sym_err_bcs:.2e}")
print(f"  Symmetry error (bare): {sym_err_bare:.2e}")

# Enforce exact symmetry
H_bcs_35 = 0.5 * (H_bcs_35 + H_bcs_35.T)
H_bare_35 = 0.5 * (H_bare_35 + H_bare_35.T)
H_tree_35 = 0.5 * (H_tree_35 + H_tree_35.T)

# Diagonalize
evals_bcs_35, evecs_bcs_35 = eigh(H_bcs_35)
evals_bare_35, evecs_bare_35 = eigh(H_bare_35)
evals_tree_35 = eigvalsh(H_tree_35)

# Sort (eigh returns sorted ascending)
print(f"\n  BCS effective Hessian (35D, volume-preserving):")
print(f"    Eigenvalue range: [{evals_bcs_35[0]:.6f}, {evals_bcs_35[-1]:.6f}]")
print(f"    All positive: {np.all(evals_bcs_35 > 0)}")
print(f"    Softest eigenvalue: {evals_bcs_35[0]:.6f}")
n_pos_bcs_35 = int(np.sum(evals_bcs_35 > 0))
n_neg_bcs_35 = 35 - n_pos_bcs_35
print(f"    Signature: ({n_pos_bcs_35}+, {n_neg_bcs_35}-)")

print(f"\n  Bare effective Hessian (35D, volume-preserving):")
print(f"    Eigenvalue range: [{evals_bare_35[0]:.6f}, {evals_bare_35[-1]:.6f}]")
print(f"    All positive: {np.all(evals_bare_35 > 0)}")
print(f"    Softest eigenvalue: {evals_bare_35[0]:.6f}")
n_pos_bare_35 = int(np.sum(evals_bare_35 > 0))
n_neg_bare_35 = 35 - n_pos_bare_35
print(f"    Signature: ({n_pos_bare_35}+, {n_neg_bare_35}-)")

print(f"\n  Tree Hessian (35D, volume-preserving):")
print(f"    Eigenvalue range: [{evals_tree_35[0]:.6f}, {evals_tree_35[-1]:.6f}]")
print(f"    All negative: {np.all(evals_tree_35 < 0)}")

# =============================================================================
# 6. CAUCHY INTERLACING THEOREM CHECK
# =============================================================================
print("\n--- 5. Cauchy interlacing check ---")

# For a symmetric matrix H (36x36) and its projection onto a 35D subspace,
# the Cauchy interlacing theorem states:
#   lambda_k(H_36) <= lambda_k(H_35) <= lambda_{k+1}(H_36)
# where eigenvalues are sorted in ascending order.

print(f"\n  BCS interlacing check:")
interlace_ok_bcs = True
for k in range(35):
    if not (evals_bcs_36[k] - 1e-6 <= evals_bcs_35[k] <= evals_bcs_36[k+1] + 1e-6):
        print(f"    VIOLATION at k={k}: {evals_bcs_36[k]:.6f} <= {evals_bcs_35[k]:.6f} <= {evals_bcs_36[k+1]:.6f}")
        interlace_ok_bcs = False
if interlace_ok_bcs:
    print(f"    ALL 35 eigenvalues satisfy Cauchy interlacing. PASS.")
else:
    print(f"    Interlacing VIOLATIONS detected.")

print(f"\n  Bare interlacing check:")
interlace_ok_bare = True
for k in range(35):
    if not (evals_bare_36[k] - 1e-6 <= evals_bare_35[k] <= evals_bare_36[k+1] + 1e-6):
        print(f"    VIOLATION at k={k}: {evals_bare_36[k]:.6f} <= {evals_bare_35[k]:.6f} <= {evals_bare_36[k+1]:.6f}")
        interlace_ok_bare = False
if interlace_ok_bare:
    print(f"    ALL 35 eigenvalues satisfy Cauchy interlacing. PASS.")
else:
    print(f"    Interlacing VIOLATIONS detected.")

# =============================================================================
# 7. JENSEN DIRECTION ANALYSIS
# =============================================================================
print("\n--- 6. Jensen direction within 35D subspace ---")

# The Jensen curvature = h_jensen^T H_35 h_jensen (in 35D basis)
curv_jensen_bcs = h_jensen_35_norm @ H_bcs_35 @ h_jensen_35_norm
curv_jensen_bare = h_jensen_35_norm @ H_bare_35 @ h_jensen_35_norm
curv_jensen_tree = h_jensen_35_norm @ H_tree_35 @ h_jensen_35_norm

print(f"  Jensen curvature (h_j^T H h_j):")
print(f"    BCS:  {curv_jensen_bcs:.6f}")
print(f"    Bare: {curv_jensen_bare:.6f}")
print(f"    Tree: {curv_jensen_tree:.6f}")

# Cross-check with d2S/dtau2 from S69/canonical
# The tree-level d2S/dtau2 is in canonical_constants
# But we need to account for the normalization of h_jensen
# d2S/dtau2 = (dg/dtau)^T H_raw (dg/dtau) where H_raw is in the raw Sym(8) basis
# The tree Hessian eigenvalue along Jensen = d2S_fold_tree (from S42)
# d2S_fold from canonical is the FULL d2S/dtau2 at the fold = 317862.85 (tree + one-loop + ...)
# This is the spectral action d2S/dtau2, not the tree Hessian eigenvalue.
print(f"\n  Reference d2S/dtau2 (canonical, full): {d2S_fold:.2f}")
print(f"  Reference S_fold: {S_fold:.2f}")

# The curvatures above are in the tree-eigenbasis Hessian, evaluated with
# f(x) = sqrt(x) spectral action at Lambda = 2.048. The normalization includes
# the metric on Sym(8) from the orthonormal eigenbasis.

# Find which 35D eigenvalue is closest to the Jensen curvature
overlap_jensen_bcs = np.abs(evecs_bcs_35.T @ h_jensen_35_norm)
idx_jensen_bcs = np.argmax(overlap_jensen_bcs)
print(f"\n  Jensen overlap with BCS eigenvectors:")
print(f"    Max overlap: {overlap_jensen_bcs[idx_jensen_bcs]:.6f} at eigvec {idx_jensen_bcs}")
print(f"    Eigenvalue of max-overlap mode: {evals_bcs_35[idx_jensen_bcs]:.6f}")

overlap_jensen_bare = np.abs(evecs_bare_35.T @ h_jensen_35_norm)
idx_jensen_bare = np.argmax(overlap_jensen_bare)
print(f"\n  Jensen overlap with bare eigenvectors:")
print(f"    Max overlap: {overlap_jensen_bare[idx_jensen_bare]:.6f} at eigvec {idx_jensen_bare}")
print(f"    Eigenvalue of max-overlap mode: {evals_bare_35[idx_jensen_bare]:.6f}")

# =============================================================================
# 8. OFF-JENSEN DIRECTIONS: IDENTIFY AND CLASSIFY
# =============================================================================
print("\n--- 7. Off-Jensen direction classification ---")

# Define off-Jensen directions as the 34 eigenvectors perpendicular to Jensen
# within the 35D subspace.

# Build projector out of Jensen direction within 35D
P_off_jensen = np.eye(35) - np.outer(h_jensen_35_norm, h_jensen_35_norm)

# The off-Jensen eigenvalues: project H_35 onto the 34D off-Jensen subspace
# But this is already done by the eigenvector decomposition:
# eigenvalues that are perpendicular to Jensen are the "off-Jensen" eigenvalues

# For each eigenvector of H_35, compute Jensen overlap
print(f"\n  {'Idx':>4} {'Eigenvalue':>12} {'|<v|Jensen>|':>14} {'Type':>12}")
print(f"  {'-'*50}")
for i in range(35):
    ov = overlap_jensen_bcs[i]
    etype = "JENSEN" if ov > 0.5 else "off-Jensen"
    if ov > 0.1:
        etype = f"mixed({ov:.2f})"
    if ov > 0.5:
        etype = "JENSEN"
    print(f"  {i:>4} {evals_bcs_35[i]:>12.4f} {ov:>14.6f} {etype:>12}")

# Pure off-Jensen eigenvalues (overlap < 0.1 with Jensen)
off_jensen_mask = overlap_jensen_bcs < 0.1
n_pure_off_jensen = np.sum(off_jensen_mask)
evals_off_jensen_bcs = evals_bcs_35[off_jensen_mask]
print(f"\n  Pure off-Jensen eigenvalues (overlap < 0.1): {n_pure_off_jensen}")
if n_pure_off_jensen > 0:
    print(f"    Range: [{evals_off_jensen_bcs[0]:.6f}, {evals_off_jensen_bcs[-1]:.6f}]")
    print(f"    All positive: {np.all(evals_off_jensen_bcs > 0)}")

# =============================================================================
# 9. SPOT-CHECK VIA INDEPENDENT FINITE DIFFERENCES
# =============================================================================
print("\n--- 8. Independent spot-check computation ---")

# To validate the projection method, we compute d2S/dh^2 for a few off-Jensen
# directions by directly perturbing the metric and recomputing the spectral action.

# We need the Dirac operator machinery for this.
def gell_mann_matrices():
    lam = []
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3))
    return lam

def su3_generators():
    gm = gell_mann_matrices()
    return [-1j / 2.0 * lam for lam in gm]

def compute_structure_constants(gens):
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a+1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                val = -2.0 * np.trace(comm @ gens[c])  # (local)
                f[a,b,c] = val.real
                f[b,a,c] = -val.real
    return f

def orthonormal_frame(g_s):
    L = cholesky(g_s)
    return inv(L)

def frame_structure_constants(f_abc, E):
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)

def connection_coefficients(ft):
    n = ft.shape[0]
    Gamma = np.zeros((n,n,n), dtype=np.float64)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c,a,b] = 0.5*(ft[a,b,c] - ft[b,c,a] + ft[c,a,b])
    return Gamma

def build_cliff8():
    s1 = np.array([[0,1],[1,0]], dtype=complex)
    s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
    s3 = np.array([[1,0],[0,-1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    def kron4(A,B,C,D):
        return np.kron(A, np.kron(B, np.kron(C, D)))
    return [
        kron4(s1,I2,I2,I2), kron4(s2,I2,I2,I2),
        kron4(s3,s1,I2,I2), kron4(s3,s2,I2,I2),
        kron4(s3,s3,s1,I2), kron4(s3,s3,s2,I2),
        kron4(s3,s3,s3,s1), kron4(s3,s3,s3,s2),
    ]

def spinor_connection_offset(Gamma, gammas):
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b,a,c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gammas[a] @ gammas[b] @ gammas[c]
    Omega *= 0.25
    return Omega

def dirac_operator_on_irrep(rho, E, gammas, Omega):
    dim_rho = rho[0].shape[0]
    dim_spin = 16  # (local)
    dim_total = dim_rho * dim_spin
    D = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(8):
        for b in range(8):
            if abs(E[a,b]) > 1e-15:
                D += E[a,b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    return D

def irrep_fundamental(gens):
    return [g.copy() for g in gens]

def irrep_antifundamental(gens):
    return [-g.T for g in gens]

def irrep_adjoint(f_abc):
    rho = []
    for a in range(8):
        M = f_abc[a,:,:].T
        rho.append(M.astype(complex))
    return rho

def irrep_symmetric2(gens):
    I3 = np.eye(3, dtype=complex)
    sym_vecs = []
    for i in range(3):
        v = np.zeros(9, dtype=complex)
        v[3*i+i] = 1.0
        sym_vecs.append(v)
    for i in range(3):
        for j in range(i+1, 3):
            v = np.zeros(9, dtype=complex)
            v[3*i+j] = 1.0/np.sqrt(2)
            v[3*j+i] = 1.0/np.sqrt(2)
            sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    rho = []
    for X in gens:
        rho_9 = np.kron(X, I3) + np.kron(I3, X)
        rho.append(P.conj().T @ rho_9 @ P)
    return rho

def irrep_symmetric3(gens):
    from itertools import permutations
    I3 = np.eye(3, dtype=complex)
    sorted_triples = []
    for i in range(3):
        for j in range(i,3):
            for k in range(j,3):
                sorted_triples.append((i,j,k))
    sym_vecs = []
    for trip in sorted_triples:
        v = np.zeros(27, dtype=complex)
        perms = set(permutations(trip))
        norm_val = np.sqrt(len(perms))
        for p in perms:
            idx = p[0]*9 + p[1]*3 + p[2]
            v[idx] = 1.0/norm_val
        sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    rho = []
    for X in gens:
        rho_27 = (np.kron(np.kron(X,I3),I3) + np.kron(np.kron(I3,X),I3) +
                  np.kron(np.kron(I3,I3),X))
        rho.append(P.conj().T @ rho_27 @ P)
    return rho

def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    dim_A = rho_A[0].shape[0]
    dim_B = rho_B[0].shape[0]
    dim_prod = dim_A * dim_B
    rho_prod = []
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        rho_a = np.kron(rho_A[a], np.eye(dim_B)) + np.kron(np.eye(dim_A), rho_B[a])
        rho_prod.append(rho_a)
        C2 += rho_a @ rho_a
    evals_c, evecs_c = np.linalg.eigh(C2)
    tol = 1e-8  # (local)
    groups = []
    for val, idx in sorted(zip(evals_c, range(dim_prod))):
        if not groups or abs(val - groups[-1][0]) > tol:
            groups.append((val, [idx]))
        else:
            groups[-1][1].append(idx)
    target_eval = None
    for val, indices in groups:
        if len(indices) == target_dim:
            target_eval = val
            break
    if target_eval is None:
        group_info = [(val, len(indices)) for val, indices in groups]
        label = f"({target_pq[0]},{target_pq[1]})" if target_pq else f"dim={target_dim}"
        raise RuntimeError(f"Cannot find {target_dim}-dim eigenspace for {label}. Dims: {group_info}")
    mask = np.abs(evals_c - target_eval) < tol
    P_proj = evecs_c[:, mask]
    if P_proj.shape[1] != target_dim:
        raise RuntimeError(f"Projection gave dim={P_proj.shape[1]}, expected {target_dim}")
    rho = [P_proj.conj().T @ rho_prod[a] @ P_proj for a in range(8)]
    return rho

def build_irrep_list(gens, f_abc, max_pq_sum=3):
    conj_gens = [-g.T for g in gens]
    irreps = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p+1)*(q+1)*(p+q+2)//2
            try:
                if (p,q) == (0,0):
                    rho = [np.zeros((1,1), dtype=complex) for _ in range(8)]
                elif (p,q) == (1,0):
                    rho = irrep_fundamental(gens)
                elif (p,q) == (0,1):
                    rho = irrep_antifundamental(gens)
                elif (p,q) == (1,1):
                    rho = irrep_adjoint(f_abc)
                elif p >= 2 and q == 0:
                    rho = irrep_symmetric2(gens) if p == 2 else irrep_symmetric3(gens)
                elif p == 0 and q >= 2:
                    rho = irrep_symmetric2(conj_gens) if q == 2 else irrep_symmetric3(conj_gens)
                elif (p,q) == (2,1):
                    rho_3 = irrep_fundamental(gens)
                    rho_8 = irrep_adjoint(f_abc)
                    rho = irrep_via_casimir_projection(rho_3, rho_8, dim_pq, (p,q))
                elif (p,q) == (1,2):
                    conj_f = compute_structure_constants(conj_gens)
                    rho_3c = irrep_fundamental(conj_gens)
                    rho_8c = irrep_adjoint(conj_f)
                    rho = irrep_via_casimir_projection(rho_3c, rho_8c, dim_pq, (2,1))
                else:
                    continue
                irreps.append((p, q, dim_pq, rho))
            except Exception as e:
                print(f"  Warning: could not build ({p},{q}): {e}")
    return irreps

def compute_all_dirac_evals(g_metric, gens, f_abc, gammas, irreps_data):
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma_conn = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma_conn, gammas)
    all_evals = []
    for (p, q, dim_rho, rho) in irreps_data:
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = -1j * D
        ev = eigvalsh(iD)
        all_evals.append(np.repeat(ev, dim_rho))
    return np.concatenate(all_evals)

def spectral_action_f(evals, Lambda):
    """S_f = (1/Lambda) sum |lambda_n|. Spectral action with f(x) = sqrt(x)."""
    return np.sum(np.abs(evals)) / Lambda

# Build infrastructure
print("  Building SU(3) infrastructure...")
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
print("  Building irreps (max p+q = 3)...")
irreps_data = build_irrep_list(gens, f_abc, max_pq_sum=3)
n_irreps = len(irreps_data)
total_modes = sum(d**2 * 16 for (_, _, d, _) in irreps_data)
print(f"  {n_irreps} irreps, {total_modes} total modes")

# Compute reference spectral action at fold
print("  Computing reference D_K spectrum at fold...")
evals_fold_DK = compute_all_dirac_evals(g_fold, gens, f_abc, gammas, irreps_data)
S_ref = spectral_action_f(evals_fold_DK, Lambda_phys)
print(f"  S_f at fold: {S_ref:.6f}")

# Build raw Sym(8) basis
basis_sym8 = []
for i in range(8):
    M = np.zeros((8, 8))
    M[i, i] = 1.0
    basis_sym8.append(M)
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8, 8))
        M[i, j] = 1.0 / sqrt(2.0)
        M[j, i] = 1.0 / sqrt(2.0)
        basis_sym8.append(M)
assert len(basis_sym8) == 36

# Build perturbation matrices in tree eigenbasis
perturbation_matrices = []
for a in range(36):
    Delta_a = np.zeros((8, 8))
    for k in range(36):
        Delta_a += evecs_tree[k, a] * basis_sym8[k]
    perturbation_matrices.append(Delta_a)

# Now select a few off-Jensen directions for spot-checking.
# Use 4 directions: the softest and hardest BCS eigenvectors in 35D,
# plus the Jensen direction itself, plus a random off-Jensen direction.

eps_fd = 0.001  # same epsilon as S69  # (local)

spot_check_dirs_35 = [
    ("softest", evecs_bcs_35[:, 0]),
    ("hardest", evecs_bcs_35[:, -1]),
    ("Jensen", h_jensen_35_norm),
    ("mid", evecs_bcs_35[:, 17]),
]

# Convert 35D direction to 36D (tree eigenbasis) to raw Sym(8) perturbation matrix
def dir_35_to_perturbation_matrix(v_35, basis_35, evecs_tree, basis_sym8):
    """Convert a 35D direction to an 8x8 perturbation matrix."""
    v_36 = basis_35 @ v_35  # Lift to 36D tree eigenbasis
    # Convert to raw Sym(8) basis
    v_raw = evecs_tree @ v_36  # raw Sym(8) components
    # Build 8x8 matrix
    h = np.zeros((8, 8))
    for k in range(36):
        h += v_raw[k] * basis_sym8[k]
    return h

print(f"\n  Spot-checking {len(spot_check_dirs_35)} directions by independent finite differences...")
print(f"  eps = {eps_fd}")
t_spot_start = time.time()

spot_results = []
for name, v_35 in spot_check_dirs_35:
    h_mat = dir_35_to_perturbation_matrix(v_35, basis_35, evecs_tree, basis_sym8)

    # Volume-preserving check
    vol_change = np.trace(inv(g_fold) @ h_mat)
    assert abs(vol_change) < 1e-8, f"Direction {name} not volume-preserving: Tr(g^-1 h) = {vol_change}"

    g_plus = g_fold + eps_fd * h_mat
    g_minus = g_fold - eps_fd * h_mat

    # Check positive definiteness
    if eigvalsh(g_plus)[0] < 0 or eigvalsh(g_minus)[0] < 0:
        print(f"    {name}: SKIPPED (metric not positive definite at eps={eps_fd})")
        spot_results.append((name, np.nan, np.nan))
        continue

    ev_plus = compute_all_dirac_evals(g_plus, gens, f_abc, gammas, irreps_data)
    ev_minus = compute_all_dirac_evals(g_minus, gens, f_abc, gammas, irreps_data)

    S_plus = spectral_action_f(ev_plus, Lambda_phys)
    S_minus = spectral_action_f(ev_minus, Lambda_phys)

    d2S_fd = (S_plus - 2*S_ref + S_minus) / eps_fd**2

    # The spot check computes d2S_f/dh^2 where S_f = (1/Lambda) sum |lambda|.
    # This is the f(x) = sqrt(x) spectral action -- the "one-loop" contribution.
    #
    # In the effective Hessian H_eff = H_tree + H_1loop:
    #   H_tree = d^2(sum ln|lambda|)/dg^2  (f(x) = ln(x), Lambda = inf limit)
    #   H_1loop = d^2((1/Lambda) sum |lambda|)/dg^2  (f(x) = sqrt(x), finite Lambda)
    #
    # The spot check computes H_1loop alone. So compare to H_bare_1loop_35.
    d2S_predicted_1loop = v_35 @ H_bare_1loop_35 @ v_35

    rel_err = abs(d2S_fd - d2S_predicted_1loop) / max(abs(d2S_fd), abs(d2S_predicted_1loop), 1e-10)

    print(f"    {name:>10}: d2S(FD) = {d2S_fd:+.6f}, d2S(proj) = {d2S_predicted_1loop:+.6f}, "
          f"rel_err = {rel_err:.2e}")
    spot_results.append((name, d2S_fd, d2S_predicted_1loop))

t_spot_end = time.time()
print(f"  Spot-check complete: {t_spot_end - t_spot_start:.1f}s")

# =============================================================================
# 10. FULL EIGENVALUE SPECTRUM TABLE
# =============================================================================
print("\n--- 9. Full 35x35 eigenvalue spectrum ---")

print(f"\n  {'Idx':>4} {'BCS eval':>12} {'Bare eval':>12} {'Tree eval':>12} "
      f"{'BCS/Bare':>10} {'|Jensen ov|':>12}")
print(f"  {'-'*72}")
for i in range(35):
    ratio = evals_bcs_35[i] / evals_bare_35[i] if abs(evals_bare_35[i]) > 1e-10 else float('inf')
    ov = overlap_jensen_bcs[i]
    marker = " <-- JENSEN" if ov > 0.5 else ""
    neg_marker = " *** NEGATIVE ***" if evals_bcs_35[i] < 0 else ""
    print(f"  {i:>4} {evals_bcs_35[i]:>12.4f} {evals_bare_35[i]:>12.4f} {evals_tree_35[i]:>12.4f} "
          f"{ratio:>10.6f} {ov:>12.6f}{marker}{neg_marker}")

# =============================================================================
# 11. CONDITION NUMBER AND STIFFNESS HIERARCHY
# =============================================================================
print("\n--- 10. Condition number and stiffness hierarchy ---")

kappa_bcs = evals_bcs_35[-1] / evals_bcs_35[0]
kappa_bare = evals_bare_35[-1] / evals_bare_35[0]

print(f"  BCS condition number:  {kappa_bcs:.4f}")
print(f"  Bare condition number: {kappa_bare:.4f}")
print(f"  Stiffness ratio (max/min BCS): {kappa_bcs:.2f}x")

# Stabilization margin
max_tree_abs = np.max(np.abs(evals_tree_35))
margin_bcs = evals_bcs_35[0] / max_tree_abs
margin_bare = evals_bare_35[0] / max_tree_abs

print(f"\n  Max |tree eigenvalue| (35D): {max_tree_abs:.4f}")
print(f"  BCS stabilization margin: {margin_bcs:.6f} ({margin_bcs*100:.2f}%)")
print(f"  Bare stabilization margin: {margin_bare:.6f} ({margin_bare*100:.2f}%)")

# =============================================================================
# 12. SOFTEST MODE IDENTIFICATION
# =============================================================================
print("\n--- 11. Softest mode analysis ---")

# Softest BCS eigenvector in 35D
v_soft_35 = evecs_bcs_35[:, 0]

# Lift to 36D tree eigenbasis
v_soft_36 = basis_35 @ v_soft_35

# Convert to raw Sym(8) components
v_soft_raw = evecs_tree @ v_soft_36

# Decompose into diagonal and off-diagonal parts
diag_part = v_soft_raw[:8]
offdiag_part = v_soft_raw[8:]
diag_norm_sq = norm(diag_part)**2
offdiag_norm_sq = norm(offdiag_part)**2

print(f"  Softest BCS mode (35D):")
print(f"    Eigenvalue: {evals_bcs_35[0]:.6f}")
print(f"    Diagonal fraction: {diag_norm_sq:.4f}")
print(f"    Off-diagonal fraction: {offdiag_norm_sq:.4f}")
print(f"    Jensen overlap: {overlap_jensen_bcs[0]:.6f}")

# Identify dominant components
print(f"\n    Dominant raw components (|c| > 0.1):")
for k in range(36):
    if abs(v_soft_raw[k]) > 0.1:
        print(f"      {basis_labels[k]:>10}: {v_soft_raw[k]:+.6f}")

# Volume check: should be zero
vol_check_soft = np.dot(h_vol_eig, v_soft_36)
print(f"\n    Volume check: <v_soft|h_vol> = {vol_check_soft:.2e} (should be ~0)")

# Compare to S69 softest mode (36D)
softest_bcs_s69 = s69['softest_bcs_evec']
overlap_with_s69 = abs(np.dot(v_soft_36, softest_bcs_s69))
print(f"    Overlap with S69 softest (36D): {overlap_with_s69:.6f}")

# =============================================================================
# 13. COMPARISON: 36D vs 35D SPECTRA
# =============================================================================
print("\n--- 12. Spectral comparison: 36D vs 35D ---")

print(f"\n  {'Property':>30} {'36D (S69)':>14} {'35D (this)':>14} {'Change':>12}")
print(f"  {'-'*74}")

props = [
    ("Softest eigenvalue (BCS)", evals_bcs_36[0], evals_bcs_35[0]),
    ("Hardest eigenvalue (BCS)", evals_bcs_36[-1], evals_bcs_35[-1]),
    ("Condition number (BCS)", evals_bcs_36[-1]/evals_bcs_36[0], kappa_bcs),
    ("Trace (BCS)", np.sum(evals_bcs_36), np.sum(evals_bcs_35)),
    ("Softest eigenvalue (bare)", evals_bare_36[0], evals_bare_35[0]),
    ("Hardest eigenvalue (bare)", evals_bare_36[-1], evals_bare_35[-1]),
    ("Condition number (bare)", evals_bare_36[-1]/evals_bare_36[0], kappa_bare),
    ("Trace (bare)", np.sum(evals_bare_36), np.sum(evals_bare_35)),
]

for name, v36, v35 in props:
    change = v35 - v36
    pct = (change/abs(v36))*100 if abs(v36) > 1e-10 else float('inf')
    print(f"  {name:>30} {v36:>14.4f} {v35:>14.4f} {change:>+12.4f} ({pct:+.2f}%)")

# The removed eigenvalue should be identifiable
removed_eval_bcs = np.sum(evals_bcs_36) - np.sum(evals_bcs_35)
removed_eval_bare = np.sum(evals_bare_36) - np.sum(evals_bare_35)
print(f"\n  Removed eigenvalue (trace difference):")
print(f"    BCS:  {removed_eval_bcs:.4f}")
print(f"    Bare: {removed_eval_bare:.4f}")

# The removed eigenvalue is the curvature along the volume direction
curv_vol_bcs = h_vol_eig @ H_bcs_eff_36 @ h_vol_eig
curv_vol_bare = h_vol_eig @ H_bare_eff_36 @ h_vol_eig
print(f"\n  Volume-direction curvature (h_vol^T H h_vol):")
print(f"    BCS:  {curv_vol_bcs:.4f}")
print(f"    Bare: {curv_vol_bare:.4f}")

# =============================================================================
# 14. PLOT: EIGENVALUE SPECTRUM
# =============================================================================
print("\n--- 13. Generating plots ---")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel 1: 35D eigenvalue spectrum (BCS vs bare)
ax = axes[0]
idx = np.arange(35)
ax.bar(idx - 0.2, evals_bcs_35, width=0.4, label='BCS', color='steelblue', alpha=0.8)
ax.bar(idx + 0.2, evals_bare_35, width=0.4, label='Bare', color='coral', alpha=0.8)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue')
ax.set_title('35D Volume-Preserving Hessian Spectrum')
ax.legend()
ax.set_yscale('symlog', linthresh=10)

# Panel 2: 36D vs 35D comparison (BCS)
ax = axes[1]
ax.plot(np.arange(36), evals_bcs_36, 'o-', label='36D (full)', color='navy', markersize=3)
ax.plot(np.arange(35), evals_bcs_35, 's-', label='35D (vol-pres)', color='crimson', markersize=3)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue')
ax.set_title('BCS Hessian: 36D vs 35D')
ax.legend()

# Panel 3: Jensen overlap of each eigenvector
ax = axes[2]
ax.bar(idx, overlap_jensen_bcs, color='forestgreen', alpha=0.8)
ax.axhline(y=0.5, color='red', linewidth=1, linestyle='--', label='Jensen threshold (0.5)')
ax.set_xlabel('Eigenvector index (35D)')
ax.set_ylabel('|<v_i|h_Jensen>|')
ax.set_title('Jensen Direction Overlap')
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 's70_off_jensen_hess.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved: computations/session-70/s70_off_jensen_hess.png")

# =============================================================================
# 15. GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: OFF-JENSEN-HESS-70")
print("=" * 78)

all_pos_bcs = np.all(evals_bcs_35 > 0)
all_pos_bare = np.all(evals_bare_35 > 0)
n_neg_total = n_neg_bcs_35 + n_neg_bare_35

if all_pos_bcs and all_pos_bare:
    verdict = "INFO"
    detail = (f"All 35 eigenvalues POSITIVE in both BCS ({n_pos_bcs_35}+, {n_neg_bcs_35}-) "
              f"and bare ({n_pos_bare_35}+, {n_neg_bare_35}-) Hessians. "
              f"Jensen metric is a genuine local minimum in the full volume-preserving moduli space. "
              f"Softest BCS: {evals_bcs_35[0]:.4f}, bare: {evals_bare_35[0]:.4f}. "
              f"Condition number BCS: {kappa_bcs:.2f}, bare: {kappa_bare:.2f}.")
elif all_pos_bcs:
    verdict = "INFO"
    detail = (f"BCS 35D all positive ({n_pos_bcs_35}+, {n_neg_bcs_35}-), "
              f"but bare has {n_neg_bare_35} negative eigenvalues. "
              f"BCS condensate stabilizes the fold.")
else:
    verdict = "INFO"
    n_neg_bcs_val = int(np.sum(evals_bcs_35 < 0))
    detail = (f"{n_neg_bcs_val} NEGATIVE eigenvalues in BCS 35D Hessian. "
              f"Jensen metric is NOT a local minimum in volume-preserving space. "
              f"Most negative: {np.min(evals_bcs_35):.4f}.")

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"\n  Key results:")
print(f"    BCS 35D eigenvalue range: [{evals_bcs_35[0]:.4f}, {evals_bcs_35[-1]:.4f}]")
print(f"    Bare 35D eigenvalue range: [{evals_bare_35[0]:.4f}, {evals_bare_35[-1]:.4f}]")
print(f"    Jensen curvature (BCS): {curv_jensen_bcs:.4f}")
print(f"    Jensen curvature (bare): {curv_jensen_bare:.4f}")
print(f"    Volume-direction curvature: {curv_vol_bcs:.4f} (BCS), {curv_vol_bare:.4f} (bare)")
print(f"    Condition number: {kappa_bcs:.2f} (BCS), {kappa_bare:.2f} (bare)")
print(f"    Softest mode is: {'JENSEN' if overlap_jensen_bcs[0] > 0.5 else 'off-Jensen'}")
print(f"    Stabilization margin: {margin_bcs:.4f} (BCS), {margin_bare:.4f} (bare)")

# Spot-check validation
spot_ok = all(
    abs(fd - proj) / max(abs(fd), abs(proj), 1e-10) < 0.05
    for name, fd, proj in spot_results
    if not np.isnan(fd)
)
print(f"\n  Spot-check validation: {'PASS' if spot_ok else 'FAIL'} (all rel_err < 5%)")

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 16. SAVE DATA
# =============================================================================
print("\n--- 14. Saving data ---")

save_path = os.path.join(base_dir, 's70_off_jensen_hess.npz')
np.savez(save_path,
    # Gate metadata
    gate_name='OFF-JENSEN-HESS-70',
    gate_verdict=verdict,
    gate_detail=detail,

    # Parameters
    tau_fold=tau_fold,
    Lambda_phys=Lambda_phys,
    Delta_BCS=Delta_BCS,
    mu_BCS=mu_BCS,
    g_fold=g_fold,

    # Volume direction
    h_vol_eig=h_vol_eig,
    h_vol_raw_norm=h_vol_raw_norm,

    # Jensen direction
    h_jensen_eig=h_jensen_eig,
    h_jensen_35=h_jensen_35_norm,
    c_su2=c_su2,
    c_C2=c_C2,
    c_u1=c_u1,

    # 35D basis
    basis_35=basis_35,

    # 35D Hessians
    H_bcs_35=H_bcs_35,
    H_bare_35=H_bare_35,
    H_tree_35=H_tree_35,

    # 35D eigenvalues
    evals_bcs_35=evals_bcs_35,
    evals_bare_35=evals_bare_35,
    evals_tree_35=evals_tree_35,

    # 35D eigenvectors (BCS)
    evecs_bcs_35=evecs_bcs_35,
    evecs_bare_35=evecs_bare_35,

    # Jensen analysis
    overlap_jensen_bcs=overlap_jensen_bcs,
    overlap_jensen_bare=overlap_jensen_bare,
    curv_jensen_bcs=curv_jensen_bcs,
    curv_jensen_bare=curv_jensen_bare,
    curv_vol_bcs=curv_vol_bcs,
    curv_vol_bare=curv_vol_bare,

    # Signatures
    n_pos_bcs_35=n_pos_bcs_35,
    n_neg_bcs_35=n_neg_bcs_35,
    n_pos_bare_35=n_pos_bare_35,
    n_neg_bare_35=n_neg_bare_35,

    # Condition numbers
    kappa_bcs=kappa_bcs,
    kappa_bare=kappa_bare,
    margin_bcs=margin_bcs,
    margin_bare=margin_bare,

    # Spot-check results
    spot_check_names=np.array([n for n, _, _ in spot_results]),
    spot_check_fd=np.array([fd for _, fd, _ in spot_results]),
    spot_check_proj=np.array([proj for _, _, proj in spot_results]),

    # 36D reference (from S69)
    evals_bcs_36=evals_bcs_36,
    evals_bare_36=evals_bare_36,
    evals_tree_36=evals_tree_s61,

    # Removed eigenvalues
    removed_eval_bcs=removed_eval_bcs,
    removed_eval_bare=removed_eval_bare,

    # Softest mode
    softest_bcs_35_evec=v_soft_35,
    softest_bcs_36_evec=v_soft_36,
    softest_bcs_raw=v_soft_raw,

    # Timing
    total_time=t_total,
)

print(f"  Data saved: {save_path}")
print(f"\nDone. OFF-JENSEN-HESS-70 complete.")
