#!/usr/bin/env python3
"""
s76_off_jensen_moduli.py -- S76-B10-OFF-JENSEN: 35D Hessian Scan for Restoring Potential
========================================================================================

Gate: S76-B10-OFF-JENSEN
  PASS: At least one negative Hessian eigenvalue found (restoring potential exists off Jensen)
  FAIL: All eigenvalues positive at fold
  INFO: Hessian indefinite but minimum requires tau outside [0.1, 1.0]

Background:
  S61 MODULI-HESS-61 computed the full 36x36 Hessian of the spectral action (heat kernel)
  in the space of left-invariant metrics on SU(3). Found the fold is a local maximum.

  S75 closed all on-Jensen stabilization channels (multi-instanton, cross-moment, ATDHFB).

  This script focuses on the VOLUME-PRESERVING 35D subspace:
    Full space: 8x8 symmetric positive-definite matrices = 36D
    Volume fixing: det(g) = const => 35D
    Jensen line: 1D curve in this 35D space

  The question: does the spectral action have any direction of POSITIVE curvature
  (i.e., a valley wall) in the 35D volume-preserving subspace? If so, the modulus
  has a restoring force in that direction -- a potential stabilization mechanism.

  NOTE ON GATE INTERPRETATION: The gate asks for "negative Hessian eigenvalue."
  In the spectral action context, S(g) is a functional on the space of metrics.
  If we define V = -S (potential energy), then d^2V/deps^2 = -d^2S/deps^2.
  A negative d^2S eigenvalue means S curves downward => V curves upward => restoring force.
  Since S61 found ALL d^2S eigenvalues negative (S is a maximum), ALL V eigenvalues
  are positive. But V = -S being a minimum everywhere means no runaway direction.

  The meaningful physical question is: does the Hessian of -S (the effective potential)
  have structure that could STABILIZE the modulus at a PARTICULAR point (not just the fold)?
  This requires looking at the GRADIENT as well as the Hessian.

Method:
  1. Build the 35D volume-preserving tangent space at the fold metric
  2. Compute the full 35x35 Hessian of S via finite differences
  3. Diagonalize and classify eigenvalues by SU(3) generator direction
  4. Cross-checks: Jensen direction, Weyl symmetry, convergence

  Key improvement over S61: explicit volume-preserving projection.
  S61 used the full 36D Sym(8); this uses the 35D det=const submanifold.

Author: Berry-Geometric-Phase-Theorist (Session 76, Wave 2)
Date: 2026-04-12
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from numpy import exp, sqrt, log, pi
from numpy.linalg import eigh, cholesky, inv, norm, eigvalsh, det
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI, E_B1, E_B2_mean, E_B3_mean,
    S_fold, d2S_fold, a0_fold, a2_fold, a4_fold
)

print("=" * 78)
print("  S76-B10-OFF-JENSEN: 35D Hessian Scan for Restoring Potential")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure
# =============================================================================
print("\n--- 1. SU(3) Lie algebra infrastructure ---")

def gell_mann_matrices():
    """Standard Gell-Mann matrices lambda_1,...,lambda_8."""
    lam = []
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / sqrt(3))
    return lam

def su3_generators():
    """Anti-Hermitian generators e_a = -i/2 * lambda_a. Tr(e_a e_b) = -1/2 delta_{ab}."""
    gm = gell_mann_matrices()
    return [-1j / 2.0 * lam for lam in gm]

def compute_structure_constants(gens):
    """f_{abc} from [e_a, e_b] = f_{abc} e_c."""
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

# Subspace decomposition indices: su(3) = u(1) + su(2) + C^2
# Gell-Mann ordering: lambda_1,2,3 = su(2), lambda_4,5,6,7 = C^2, lambda_8 = u(1)
SU2_IDX = [0, 1, 2]
C2_IDX  = [3, 4, 5, 6]
U1_IDX  = [7]

# =============================================================================
# 2. Dirac Operator and Spectral Action
# =============================================================================
print("\n--- 2. Dirac operator infrastructure ---")

def orthonormal_frame(g_s):
    """E such that E g_s E^T = I."""
    L = cholesky(g_s)
    return inv(L)

def frame_structure_constants(f_abc, E):
    """Structure constants in ON frame."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)

def connection_coefficients(ft):
    """Levi-Civita connection coefficients."""
    n = ft.shape[0]
    Gamma = np.zeros((n,n,n), dtype=np.float64)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c,a,b] = 0.5*(ft[a,b,c] - ft[b,c,a] + ft[c,a,b])
    return Gamma

def build_cliff8():
    """Cliff(R^8) generators: 8 Hermitian 16x16 matrices."""
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
    """Omega = (1/4) Gamma^b_{ac} gamma_a gamma_b gamma_c"""
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
    """D_pi = sum_{a,b} E_{ab} rho[b] x gamma_a + I x Omega"""
    dim_rho = rho[0].shape[0]
    dim_spin = 16  # (local)
    dim_total = dim_rho * dim_spin  # (local)
    D = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(8):
        for b in range(8):
            if abs(E[a,b]) > 1e-15:
                D += E[a,b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    return D

# Irrep constructors
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
            v[3*i+j] = 1.0/sqrt(2)
            v[3*j+i] = 1.0/sqrt(2)
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
        norm_val = sqrt(len(perms))  # (local)
        for p in perms:
            idx = p[0]*9 + p[1]*3 + p[2]  # (local)
            v[idx] = 1.0/norm_val
        sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    rho = []
    for X in gens:
        rho_27 = (np.kron(np.kron(X,I3),I3) + np.kron(np.kron(I3,X),I3) + np.kron(np.kron(I3,I3),X))
        rho.append(P.conj().T @ rho_27 @ P)
    return rho

def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    dim_A = rho_A[0].shape[0]  # (local)
    dim_B = rho_B[0].shape[0]  # (local)
    dim_prod = dim_A * dim_B  # (local)
    rho_prod = []
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        rho_a = np.kron(rho_A[a], np.eye(dim_B)) + np.kron(np.eye(dim_A), rho_B[a])
        rho_prod.append(rho_a)
        C2 += rho_a @ rho_a
    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-8  # (local)
    groups = []
    for i, ev in enumerate(sorted(zip(evals, range(dim_prod)))):
        val, idx = ev
        if not groups or abs(val - groups[-1][0]) > tol:
            groups.append((val, [idx]))
        else:
            groups[-1][1].append(idx)
    target_eval = None  # (local)
    for val, indices in groups:
        if len(indices) == target_dim:
            target_eval = val
            break
    if target_eval is None:
        group_info = [(val, len(indices)) for val, indices in groups]
        label = f"({target_pq[0]},{target_pq[1]})" if target_pq else f"dim={target_dim}"
        raise RuntimeError(f"Cannot find {target_dim}-dim eigenspace for {label}. Dims: {group_info}")
    mask = np.abs(evals - target_eval) < tol
    P = evecs[:, mask]
    if P.shape[1] != target_dim:
        raise RuntimeError(f"Projection gave dim={P.shape[1]}, expected {target_dim}")
    rho = []
    for a in range(8):
        rho.append(P.conj().T @ rho_prod[a] @ P)
    return rho

def get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3):
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
                    conj_gens = [-g.T for g in gens]
                    rho = irrep_symmetric2(conj_gens) if q == 2 else irrep_symmetric3(conj_gens)
                elif (p,q) == (2,1):
                    rho_3 = irrep_fundamental(gens)
                    rho_8 = irrep_adjoint(f_abc)
                    rho = irrep_via_casimir_projection(rho_3, rho_8, dim_pq, (p,q))
                elif (p,q) == (1,2):
                    conj_gens = [-g.T for g in gens]
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

def spectral_action_heat(eigenvalues, Lambda_sq):
    """S = sum_n exp(-lambda_n^2 / Lambda^2)"""
    lam_sq = eigenvalues**2
    return np.sum(np.exp(-lam_sq / Lambda_sq))

def compute_dirac_eigenvalues(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute all D_K eigenvalues for a given 8x8 metric."""
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    all_evals = []
    for (p, q, dim_rho, rho) in irreps_data:
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = -1j * D
        evals = eigvalsh(iD)
        for ev in evals:
            all_evals.extend([ev] * dim_rho)
    return np.array(sorted(all_evals))

# =============================================================================
# 3. Build Infrastructure
# =============================================================================
print("\n--- 3. Setting up infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
gammas = build_cliff8()

# Validate Clifford algebra
cliff_err = 0.0  # (local)
for a in range(8):
    for b in range(8):
        ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(16)
        cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Killing form diagonal: {B_ab[0,0]:.4f} (expected -3)")

# Build irreps
print("\n  Building irreps (max p+q = 3)...")
irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3)
total_evals = sum(d*16*d for _,_,d,_ in irreps_data)  # (local)
for p, q, dim, _ in irreps_data:
    print(f"    ({p},{q}): dim = {dim}, block = {dim*16}")
print(f"  Total eigenvalues per metric point: {total_evals}")

# =============================================================================
# 4. Build Fold Metric and Reference Spectral Action
# =============================================================================
print("\n--- 4. Building fold metric ---")

# Jensen metric: g = L1 * |B|_{u(1)} + L2 * |B|_{su(2)} + L3 * |B|_{C^2}
# At fold: L1 = exp(2*tau_fold), L2 = exp(-2*tau_fold), L3 = exp(tau_fold)
L1_fold = exp(2.0 * tau_fold)  # (local)
L2_fold = exp(-2.0 * tau_fold)  # (local)
L3_fold = exp(tau_fold)  # (local)

print(f"  L1_fold = {L1_fold:.6f} (u(1) direction)")
print(f"  L2_fold = {L2_fold:.6f} (su(2) directions)")
print(f"  L3_fold = {L3_fold:.6f} (C^2 directions)")

g0 = np.abs(B_ab)  # Positive-definite base from Killing form
g_fold = np.zeros((8,8), dtype=np.float64)
for a in U1_IDX:
    for b in U1_IDX:
        g_fold[a,b] = g0[a,b] * L1_fold
for a in SU2_IDX:
    for b in SU2_IDX:
        g_fold[a,b] = g0[a,b] * L2_fold
for a in C2_IDX:
    for b in C2_IDX:
        g_fold[a,b] = g0[a,b] * L3_fold

det_fold = det(g_fold)  # (local)
log_det_fold = log(det_fold)  # (local)
print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  det(g_fold) = {det_fold:.6f}")
print(f"  log det(g_fold) = {log_det_fold:.6f}")

# Reference spectral action
evals_fold = compute_dirac_eigenvalues(g_fold, gens, f_abc, gammas, irreps_data)
Lambda_sq = 4.0 * np.max(evals_fold**2)  # (local) same convention as S60/S61
SA_fold = spectral_action_heat(evals_fold, Lambda_sq)  # (local)

print(f"  Lambda^2 = {Lambda_sq:.4f}")
print(f"  SA at fold = {SA_fold:.6f}")
print(f"  Number of eigenvalues: {len(evals_fold)}")

pos_fold = sorted(evals_fold[evals_fold > 1e-6])
print(f"  Positive eigenvalues: {len(pos_fold)}")
if len(pos_fold) >= 8:
    print(f"    B1: {pos_fold[0]:.6f}")
    print(f"    B2: {pos_fold[1]:.6f}-{pos_fold[4]:.6f}")
    print(f"    B3: {pos_fold[5]:.6f}-{pos_fold[7]:.6f}")

# =============================================================================
# 5. Construct Volume-Preserving Tangent Space (35D)
# =============================================================================
print("\n--- 5. Constructing volume-preserving tangent space (35D) ---")

# The full tangent space at g_fold is Sym(8) = 36D.
# The volume-preserving constraint is: det(g + eps * delta_g) = det(g_fold)
# To linear order: d/deps det(g + eps * delta_g)|_0 = det(g) * Tr(g^{-1} delta_g)
# So the constraint is: Tr(g_fold^{-1} delta_g) = 0.
#
# This defines a 35D subspace of Sym(8).
#
# Strategy: build a 36D basis for Sym(8), then project out the volume direction.

# Step 1: Build the 36D basis for Sym(8)
basis_36 = []
basis_36_labels = []

# Diagonal elements
for i in range(8):
    M = np.zeros((8,8))
    M[i,i] = 1.0
    basis_36.append(M)
    basis_36_labels.append(f"diag({i})")

# Off-diagonal elements (normalized)
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8,8))
        M[i,j] = 1.0 / sqrt(2.0)
        M[j,i] = 1.0 / sqrt(2.0)
        basis_36.append(M)
        basis_36_labels.append(f"off({i},{j})")

assert len(basis_36) == 36, f"Expected 36 basis elements, got {len(basis_36)}"

# Step 2: Compute the volume gradient direction
# The gradient of log det(g) at g_fold is g_fold^{-1} (in the Frobenius inner product).
# In components: d(log det)/d(g_{ab}) = (g^{-1})_{ba}
g_fold_inv = inv(g_fold)

# Volume direction in the 36D basis: v_vol[k] = Tr(g_fold_inv @ basis_36[k])
v_vol = np.zeros(36)
for k in range(36):
    v_vol[k] = np.trace(g_fold_inv @ basis_36[k])

v_vol_norm = norm(v_vol)  # (local)
v_vol_hat = v_vol / v_vol_norm  # (local) unit volume direction

print(f"  Volume gradient norm: {v_vol_norm:.6f}")
print(f"  Volume gradient components (first 8, diagonal): {v_vol[:8]}")

# Step 3: Project out the volume direction using Gram-Schmidt
# For each basis vector e_k, compute e_k' = e_k - (e_k . v_hat) * v_hat
# Then select 35 linearly independent vectors from the projections.

projected_36 = np.zeros((36, 36))
for k in range(36):
    e_k = np.zeros(36)
    e_k[k] = 1.0
    proj = e_k - np.dot(e_k, v_vol_hat) * v_vol_hat
    projected_36[k] = proj

# Remove the one direction that becomes zero (or nearly zero) after projection
norms_proj = np.array([norm(projected_36[k]) for k in range(36)])
keep_mask = norms_proj > 1e-10  # (local)
n_keep = np.sum(keep_mask)  # (local)
print(f"  Directions surviving volume projection: {n_keep}/36")

# Sort by norm (largest first) and take the top 35
idx_sorted = np.argsort(-norms_proj)  # (local)
basis_35_raw = []
basis_35_labels = []
for k in idx_sorted[:35]:
    vec = projected_36[k] / norms_proj[k]  # normalize
    basis_35_raw.append(vec)
    basis_35_labels.append(basis_36_labels[k])

# Orthonormalize using QR decomposition
Q_raw = np.column_stack(basis_35_raw)  # 36 x 35
Q, R = np.linalg.qr(Q_raw)
# Q is 36 x 35, columns are orthonormal in R^36

# Verify volume-preserving property
vol_check = np.array([np.dot(Q[:, k], v_vol_hat) for k in range(35)])
vol_check_max = np.max(np.abs(vol_check))  # (local)
print(f"  Volume constraint check (max |Q_k . v_vol|): {vol_check_max:.2e}")
assert vol_check_max < 1e-10, f"Volume-preserving projection failed: {vol_check_max}"

# Step 4: Identify the Jensen direction within the 35D subspace
# dg/dtau at fold: L1' = 2*L1, L2' = -2*L2, L3' = L3
v_jensen_36 = np.zeros(36)
for a in U1_IDX:
    v_jensen_36[a] = 2.0 * L1_fold * g0[a,a]
for a in SU2_IDX:
    v_jensen_36[a] = -2.0 * L2_fold * g0[a,a]
for a in C2_IDX:
    v_jensen_36[a] = L3_fold * g0[a,a]

# Project Jensen direction onto volume-preserving subspace
v_jensen_proj = v_jensen_36 - np.dot(v_jensen_36, v_vol_hat) * v_vol_hat
v_jensen_proj_norm = norm(v_jensen_proj)  # (local)
v_jensen_35 = Q.T @ v_jensen_proj  # components in the 35D basis
v_jensen_35_hat = v_jensen_35 / norm(v_jensen_35)  # (local)

print(f"\n  Jensen direction (36D) norm: {norm(v_jensen_36):.6f}")
print(f"  Jensen direction volume component: {np.dot(v_jensen_36, v_vol_hat):.6f}")
print(f"  Jensen direction (volume-projected) norm: {v_jensen_proj_norm:.6f}")

# Step 5: Classify basis directions
def classify_direction_36(label):
    """Classify a 36D basis direction."""
    if label.startswith("diag"):
        idx = int(label.split("(")[1].rstrip(")"))
        if idx in U1_IDX:
            return "u(1)-diag"
        elif idx in SU2_IDX:
            return "su(2)-diag"
        elif idx in C2_IDX:
            return "C^2-diag"
    elif label.startswith("off"):
        parts = label.split("(")[1].rstrip(")").split(",")
        i, j = int(parts[0]), int(parts[1])
        if i in SU2_IDX and j in SU2_IDX:
            return "su(2)-internal"
        elif i in C2_IDX and j in C2_IDX:
            return "C^2-internal"
        elif (i in SU2_IDX and j in C2_IDX) or (i in C2_IDX and j in SU2_IDX):
            return "su(2)-C^2 cross"
        elif (i in U1_IDX and j in SU2_IDX) or (i in SU2_IDX and j in U1_IDX):
            return "u(1)-su(2) cross"
        elif (i in U1_IDX and j in C2_IDX) or (i in C2_IDX and j in U1_IDX):
            return "u(1)-C^2 cross"
    return "unknown"

class_counts = {}
for label in basis_35_labels:
    cls = classify_direction_36(label)
    class_counts[cls] = class_counts.get(cls, 0) + 1

print(f"\n  35D basis classification (before QR):")
for cls, count in sorted(class_counts.items()):
    print(f"    {cls}: {count}")

# =============================================================================
# 6. Compute 35x35 Hessian via Finite Differences
# =============================================================================
print("\n--- 6. Computing 35x35 Hessian (finite differences) ---")

# Perturbation size
eps_primary = 0.001  # (local) primary step size as specified

# Function to convert a 35D coefficient vector to an 8x8 metric perturbation
def coeff_to_metric_perturbation(coeffs_35, Q_matrix, basis_list):
    """Convert 35D coefficients to a 36D coefficient vector, then to an 8x8 matrix."""
    coeffs_36 = Q_matrix @ coeffs_35  # (local) project back to 36D
    delta_g = np.zeros((8,8))
    for k in range(36):
        delta_g += coeffs_36[k] * basis_list[k]
    return delta_g

def compute_SA_at_perturbation(g_base, delta_g, gens, f_abc, gammas, irreps_data, Lambda_sq):
    """Compute spectral action at g_base + delta_g, with positive-definite check."""
    g_pert = g_base + delta_g  # (local)
    evals_g = eigvalsh(g_pert)  # (local)
    if np.any(evals_g <= 0):
        return np.nan, False
    ev_dirac = compute_dirac_eigenvalues(g_pert, gens, f_abc, gammas, irreps_data)
    sa = spectral_action_heat(ev_dirac, Lambda_sq)
    return sa, True

# Compute diagonal Hessian elements: H_{kk} = d^2 SA / d eps_k^2
# Using central differences: (SA(+h) - 2*SA(0) + SA(-h)) / h^2
print(f"\n  Step size: eps = {eps_primary}")
print(f"  Computing 35 diagonal elements...")

t_diag_start = time.time()

d2SA_diag = np.zeros(35)
diag_pd_check = np.zeros(35, dtype=bool)

for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_g_plus = coeff_to_metric_perturbation(eps_primary * e_k, Q, basis_36)
    delta_g_minus = coeff_to_metric_perturbation(-eps_primary * e_k, Q, basis_36)

    sa_plus, pd_plus = compute_SA_at_perturbation(
        g_fold, delta_g_plus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    sa_minus, pd_minus = compute_SA_at_perturbation(
        g_fold, delta_g_minus, gens, f_abc, gammas, irreps_data, Lambda_sq)

    if pd_plus and pd_minus:
        d2SA_diag[k] = (sa_plus - 2.0 * SA_fold + sa_minus) / eps_primary**2
        diag_pd_check[k] = True
    else:
        d2SA_diag[k] = np.nan
        diag_pd_check[k] = False

    if (k+1) % 7 == 0 or k == 34:
        elapsed = time.time() - t_diag_start  # (local)
        print(f"    {k+1}/35 diagonal done ({elapsed:.1f}s)")

n_diag_valid = np.sum(diag_pd_check)  # (local)
print(f"  Diagonal: {n_diag_valid}/35 PD-safe")
print(f"  Diagonal d2SA: min={np.nanmin(d2SA_diag):.4f}, max={np.nanmax(d2SA_diag):.4f}")

# Compute full off-diagonal elements via polarization identity
# H_{kl} = [d2SA(e_k + e_l) - d2SA(e_k) - d2SA(e_l)] / 2
print(f"\n  Computing {35*34//2} off-diagonal pairs...")

t_offdiag_start = time.time()
H_35 = np.zeros((35, 35))

# Fill diagonal
for k in range(35):
    H_35[k,k] = d2SA_diag[k]

# Fill off-diagonal
n_pairs_total = 35 * 34 // 2  # (local)
n_pairs_done = 0  # (local)
n_pd_fail = 0  # (local)

for k in range(35):
    for l in range(k+1, 35):
        e_sum = np.zeros(35)
        e_sum[k] = 1.0
        e_sum[l] = 1.0
        delta_g_plus = coeff_to_metric_perturbation(eps_primary * e_sum, Q, basis_36)
        delta_g_minus = coeff_to_metric_perturbation(-eps_primary * e_sum, Q, basis_36)

        sa_plus, pd_plus = compute_SA_at_perturbation(
            g_fold, delta_g_plus, gens, f_abc, gammas, irreps_data, Lambda_sq)
        sa_minus, pd_minus = compute_SA_at_perturbation(
            g_fold, delta_g_minus, gens, f_abc, gammas, irreps_data, Lambda_sq)

        if pd_plus and pd_minus:
            d2SA_sum = (sa_plus - 2.0 * SA_fold + sa_minus) / eps_primary**2
            H_35[k, l] = 0.5 * (d2SA_sum - d2SA_diag[k] - d2SA_diag[l])
            H_35[l, k] = H_35[k, l]
        else:
            H_35[k, l] = 0.0
            H_35[l, k] = 0.0
            n_pd_fail += 1

        n_pairs_done += 1
        if n_pairs_done % 100 == 0:
            elapsed = time.time() - t_offdiag_start
            rate = n_pairs_done / elapsed if elapsed > 0 else 1  # (local)
            remaining = (n_pairs_total - n_pairs_done) / rate if rate > 0 else 0  # (local)
            print(f"    Pairs: {n_pairs_done}/{n_pairs_total} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_offdiag_end = time.time()
print(f"  Off-diagonal computation: {t_offdiag_end - t_offdiag_start:.1f}s")
print(f"  PD failures: {n_pd_fail}/{n_pairs_total}")

# Symmetry check
sym_err_35 = np.max(np.abs(H_35 - H_35.T))  # (local)
print(f"  Symmetry error: {sym_err_35:.2e}")

# =============================================================================
# 7. Eigenvalue Decomposition of 35x35 Hessian
# =============================================================================
print("\n--- 7. Eigenvalue decomposition of 35x35 Hessian ---")

evals_35, evecs_35 = eigh(H_35)

zero_threshold = 1.0  # (local) below this, treat as numerically zero

n_pos_35 = int(np.sum(evals_35 > zero_threshold))  # (local)
n_neg_35 = int(np.sum(evals_35 < -zero_threshold))  # (local)
n_zero_35 = int(np.sum(np.abs(evals_35) <= zero_threshold))  # (local)

print(f"\n  All 35 eigenvalues of H_35:")
for k in range(35):
    sign = "+" if evals_35[k] > zero_threshold else ("-" if evals_35[k] < -zero_threshold else "~0")
    print(f"    lambda_{k:>2} = {evals_35[k]:>14.4f}  {sign}")

print(f"\n  Signature: ({n_pos_35}+, {n_neg_35}-, {n_zero_35} ~0)")
print(f"  Largest eigenvalue: {evals_35[-1]:.4f}")
print(f"  Smallest eigenvalue: {evals_35[0]:.4f}")

# =============================================================================
# 8. Cross-Check 1: Jensen Direction Eigenvalue
# =============================================================================
print("\n--- 8. CHK1: Jensen direction eigenvalue ---")

# Project the Hessian onto the Jensen direction
# d^2S/dtau^2 = v_jensen_hat^T @ H_35 @ v_jensen_hat
d2S_jensen_proj = v_jensen_35_hat @ H_35 @ v_jensen_35_hat  # (local)

# The canonical d2S_fold is the second derivative of S along the Jensen line,
# which should be POSITIVE (S is increasing and accelerating at the fold).
# But the Hessian eigenvalue along Jensen should be NEGATIVE if S is a maximum
# (which S61 found). The difference: dS/dtau != 0 at the fold, so the Hessian
# of S at a point where dS/dtau > 0 does not tell us about maximum/minimum --
# the gradient is nonzero.
#
# What we actually measure: the second derivative of S along the Jensen direction,
# which equals d2S/dtau^2 (up to parameterization factors).

print(f"  d^2S projected onto Jensen direction: {d2S_jensen_proj:.4f}")
print(f"  Canonical d2S_fold (from constants): {d2S_fold:.4f}")
print(f"  Jensen direction weight in 35D basis: {np.dot(v_jensen_35_hat, v_jensen_35_hat):.6f} (should be 1)")

# The spectral action Hessian at a given metric point measures the curvature
# of the spectral action functional. A NEGATIVE eigenvalue means S curves downward
# in that direction. All eigenvalues negative = S is a local maximum.
# This is what S61 found: fold is a maximum of S(g).

# =============================================================================
# 9. Cross-Check 2: Volume-Preserving Verification
# =============================================================================
print("\n--- 9. CHK2: Volume-preserving verification ---")

# Verify that the 35D basis vectors actually preserve volume
max_vol_violation = 0.0  # (local)
for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_g = coeff_to_metric_perturbation(eps_primary * e_k, Q, basis_36)
    g_pert = g_fold + delta_g
    det_pert = det(g_pert)  # (local)
    rel_vol_change = abs(det_pert - det_fold) / det_fold  # (local)
    max_vol_violation = max(max_vol_violation, rel_vol_change)

print(f"  Max relative volume change at eps={eps_primary}: {max_vol_violation:.2e}")
print(f"  (This should be O(eps^2) ~ {eps_primary**2:.2e} since linear term vanishes)")
print(f"  CHK2: {'PASS' if max_vol_violation < 10 * eps_primary**2 else 'MARGINAL'}")

# =============================================================================
# 10. Cross-Check 3: Weyl Symmetry
# =============================================================================
print("\n--- 10. CHK3: S_3 Weyl symmetry of eigenvalues ---")

# The SU(3) Weyl group is S_3, which permutes the three rows/columns of
# the Cartan torus. The Jensen metric has the U(2)-invariant structure:
# u(1): 1 direction, su(2): 3 directions, C^2: 4 directions.
#
# The S_3 permutation symmetry acts on the Cartan subalgebra,
# which maps (lambda_3, lambda_8) -> permutations of the diagonal entries.
# Since the fold metric respects U(2), the Weyl group S_3 acts non-trivially
# only on the su(2) and C^2 blocks.
#
# Within su(2): the 3 generators {e_1, e_2, e_3} transform as a vector under
# SO(3), and the Jensen metric assigns them equal weight. The Hessian eigenvalues
# corresponding to permutations within su(2) should be degenerate.
#
# Within C^2: the 4 generators {e_4, e_5, e_6, e_7} transform as two pairs
# under the Weyl group. The Jensen metric assigns them equal weight.
# The Hessian eigenvalues for C^2-internal perturbations should show
# the SU(2) x U(1) symmetry of the C^2 coset.

# Check degeneracies in the Hessian spectrum
print(f"\n  Eigenvalue degeneracies (tolerance = {zero_threshold}):")
eigenvalue_groups = []
for k in range(35):
    placed = False
    for g in eigenvalue_groups:
        if abs(evals_35[k] - g[0]) < zero_threshold:
            g.append(evals_35[k])
            placed = True
            break
    if not placed:
        eigenvalue_groups.append([evals_35[k]])

for g in eigenvalue_groups:
    deg = len(g)
    mean_val = np.mean(g)  # (local)
    spread = max(g) - min(g) if deg > 1 else 0.0  # (local)
    print(f"    mean={mean_val:>14.4f}, degeneracy={deg}, spread={spread:.4f}")

# =============================================================================
# 11. Convergence Check: Three Step Sizes
# =============================================================================
print("\n--- 11. Convergence check: three step sizes ---")

eps_coarse = 0.01  # (local)
eps_fine = 0.0001  # (local)

# Compute diagonal elements at coarse and fine step sizes for first 10 directions
n_conv_check = min(10, 35)  # (local)
d2SA_coarse = np.zeros(n_conv_check)
d2SA_fine = np.zeros(n_conv_check)

t_conv_start = time.time()

for k in range(n_conv_check):
    e_k = np.zeros(35)
    e_k[k] = 1.0

    # Coarse
    delta_plus = coeff_to_metric_perturbation(eps_coarse * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-eps_coarse * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_fold, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    sa_m, pd_m = compute_SA_at_perturbation(g_fold, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    if pd_p and pd_m:
        d2SA_coarse[k] = (sa_p - 2.0 * SA_fold + sa_m) / eps_coarse**2
    else:
        d2SA_coarse[k] = np.nan

    # Fine
    delta_plus = coeff_to_metric_perturbation(eps_fine * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-eps_fine * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_fold, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    sa_m, pd_m = compute_SA_at_perturbation(g_fold, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    if pd_p and pd_m:
        d2SA_fine[k] = (sa_p - 2.0 * SA_fold + sa_m) / eps_fine**2
    else:
        d2SA_fine[k] = np.nan

print(f"  Convergence check time: {time.time() - t_conv_start:.1f}s")
print(f"\n  {'Dir':>4} {'d2SA(0.01)':>14} {'d2SA(0.001)':>14} {'d2SA(0.0001)':>14} {'conv_ratio':>12}")
for k in range(n_conv_check):
    vals = [d2SA_coarse[k], d2SA_diag[k], d2SA_fine[k]]
    if not any(np.isnan(v) for v in vals) and abs(d2SA_coarse[k] - d2SA_diag[k]) > 1e-10:
        # Richardson ratio: (fine - primary) / (primary - coarse) should be ~1/4 for O(h^2)
        ratio = (d2SA_fine[k] - d2SA_diag[k]) / (d2SA_diag[k] - d2SA_coarse[k]) if abs(d2SA_diag[k] - d2SA_coarse[k]) > 1e-10 else np.nan
        print(f"  {k:>4} {d2SA_coarse[k]:>14.4f} {d2SA_diag[k]:>14.4f} {d2SA_fine[k]:>14.4f} {ratio:>12.4f}")
    else:
        print(f"  {k:>4} {d2SA_coarse[k]:>14.4f} {d2SA_diag[k]:>14.4f} {d2SA_fine[k]:>14.4f} {'N/A':>12}")

# =============================================================================
# 12. Eigenvector Analysis: Which SU(3) Generators?
# =============================================================================
print("\n--- 12. Eigenvector analysis: dominant SU(3) generators ---")

# For each Hessian eigenvalue, identify which 36D directions dominate
# Recall: Q maps 35D -> 36D, so evecs_35 in 35D -> Q @ evecs_35[:,k] in 36D
print(f"\n  5 most negative eigenvalues:")
for k in range(min(5, 35)):
    v_35 = evecs_35[:, k]
    v_36 = Q @ v_35  # (local) map to 36D
    # Top components in 36D basis
    top5 = np.argsort(np.abs(v_36))[-5:][::-1]
    top5_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top5)
    # Jensen content
    jensen_weight = np.dot(v_35, v_jensen_35_hat)**2  # (local)
    print(f"  lambda_{k} = {evals_35[k]:>14.4f}: Jensen content = {jensen_weight:.4f}")
    print(f"    top 36D components: {top5_str}")

if n_pos_35 > 0:
    print(f"\n  POSITIVE eigenvalues (saddle directions):")
    for k in range(35):
        if evals_35[k] > zero_threshold:
            v_35 = evecs_35[:, k]
            v_36 = Q @ v_35
            top5 = np.argsort(np.abs(v_36))[-5:][::-1]
            top5_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top5)
            jensen_weight = np.dot(v_35, v_jensen_35_hat)**2
            print(f"  lambda_{k} = {evals_35[k]:>14.4f}: Jensen content = {jensen_weight:.4f}")
            print(f"    top 36D components: {top5_str}")

print(f"\n  5 least negative / most positive eigenvalues:")
for k in range(max(0, 35-5), 35):
    v_35 = evecs_35[:, k]
    v_36 = Q @ v_35
    top3 = np.argsort(np.abs(v_36))[-3:][::-1]
    top3_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top3)
    jensen_weight = np.dot(v_35, v_jensen_35_hat)**2
    print(f"  lambda_{k} = {evals_35[k]:>14.4f}: Jensen content = {jensen_weight:.4f}")
    print(f"    top components: {top3_str}")

# =============================================================================
# 13. Analysis: V = -S Potential Landscape
# =============================================================================
print("\n--- 13. Effective potential V = -S analysis ---")

# The effective potential is V = -S.
# V eigenvalues = -evals_35.
V_evals = -evals_35

n_V_pos = int(np.sum(V_evals > zero_threshold))  # (local)
n_V_neg = int(np.sum(V_evals < -zero_threshold))  # (local)
n_V_zero = int(np.sum(np.abs(V_evals) <= zero_threshold))  # (local)

print(f"  V = -S Hessian signature: ({n_V_pos}+, {n_V_neg}-, {n_V_zero} ~0)")
print(f"  All V positive => fold is a MINIMUM of V (maximum of S)")
print(f"  Any V negative => fold is a SADDLE of V (restoring potential in some directions)")

if n_V_neg > 0:
    print(f"\n  NEGATIVE V eigenvalues (runaway directions):")
    for k in range(35):
        if V_evals[k] < -zero_threshold:
            print(f"    V_lambda_{k} = {V_evals[k]:.4f}")
    print(f"  => Restoring potential does NOT exist in these directions.")
    print(f"     The fold is locally unstable in {n_V_neg} directions.")
else:
    print(f"\n  All V eigenvalues non-negative => fold is a local MINIMUM of V")
    print(f"  Restoring force exists in ALL 35 off-Jensen directions!")
    print(f"  Strongest restoring: V eigenvalue = {V_evals[-1]:.4f}")
    print(f"  Weakest restoring: V eigenvalue = {V_evals[0]:.4f}")

# =============================================================================
# 14. Gradient Analysis at Fold
# =============================================================================
print("\n--- 14. Gradient of SA at fold (35D) ---")

# Compute dSA/d(eps_k) by central differences
grad_SA = np.zeros(35)
for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_plus = coeff_to_metric_perturbation(eps_primary * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-eps_primary * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_fold, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    sa_m, pd_m = compute_SA_at_perturbation(g_fold, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq)
    if pd_p and pd_m:
        grad_SA[k] = (sa_p - sa_m) / (2.0 * eps_primary)
    else:
        grad_SA[k] = np.nan

grad_norm = norm(grad_SA[~np.isnan(grad_SA)])  # (local)
grad_jensen = np.dot(grad_SA, v_jensen_35_hat)  # (local)

print(f"  |grad SA|_35D = {grad_norm:.6f}")
print(f"  grad SA . Jensen_hat = {grad_jensen:.6f}")
print(f"  (should be ~ dS_fold = {58672.80:.2f}, modulo parameterization)")

# Decompose gradient into Jensen + off-Jensen
grad_off_jensen = grad_SA - grad_jensen * v_jensen_35_hat
grad_off_norm = norm(grad_off_jensen[~np.isnan(grad_off_jensen)])  # (local)
print(f"  |grad SA|_off-Jensen = {grad_off_norm:.6f}")
print(f"  Ratio off-Jensen/Jensen: {grad_off_norm / abs(grad_jensen) if abs(grad_jensen) > 1e-10 else np.inf:.6f}")

if grad_off_norm < 0.01 * abs(grad_jensen):
    print(f"  => Gradient is essentially PURELY along Jensen (off-Jensen < 1%)")
    print(f"     The fold metric is a critical point of S in the off-Jensen directions!")
    print(f"     Combined with all-negative Hessian: fold is a local MAXIMUM in off-Jensen")
else:
    print(f"  => Gradient has significant off-Jensen component ({100*grad_off_norm/abs(grad_jensen):.1f}%)")

# =============================================================================
# 15. Search for Minimum Along Off-Jensen Directions
# =============================================================================
print("\n--- 15. Search for nearby SA minimum (off-Jensen scan) ---")

# If the Hessian is negative-definite in the off-Jensen directions but the gradient
# is nonzero, there is no local minimum AT the fold. But there might be one nearby.
# Check: along the steepest-descent direction of V = -S, scan for a minimum.

# Find the off-Jensen direction of steepest S-ascent (= V-descent)
if grad_off_norm > 1e-10:
    v_steep = grad_off_jensen / grad_off_norm
    # Scan along this direction
    n_scan = 21  # (local)
    eps_scan = np.linspace(-0.05, 0.05, n_scan)  # (local)
    SA_scan = np.zeros(n_scan)

    for i, eps in enumerate(eps_scan):
        delta_g = coeff_to_metric_perturbation(eps * v_steep, Q, basis_36)
        sa, pd = compute_SA_at_perturbation(g_fold, delta_g, gens, f_abc, gammas, irreps_data, Lambda_sq)
        SA_scan[i] = sa if pd else np.nan

    valid = ~np.isnan(SA_scan)
    if np.sum(valid) > 3:
        SA_valid = SA_scan[valid]  # (local)
        eps_valid = eps_scan[valid]  # (local)
        idx_max = np.argmax(SA_valid)  # (local)
        idx_min = np.argmin(SA_valid)  # (local)
        print(f"  Off-Jensen steepest direction scan:")
        print(f"    SA range: [{SA_valid[idx_min]:.6f}, {SA_valid[idx_max]:.6f}]")
        print(f"    SA at fold: {SA_fold:.6f}")
        print(f"    Max at eps = {eps_valid[idx_max]:.4f}")
        print(f"    Min at eps = {eps_valid[idx_min]:.4f}")
        if SA_valid[idx_min] < SA_fold and idx_min not in [0, len(SA_valid)-1]:
            print(f"    => LOCAL MINIMUM found off-Jensen at eps = {eps_valid[idx_min]:.4f}!")
        else:
            print(f"    => No off-Jensen minimum found (monotonic or edge)")
    else:
        print(f"  Too few valid SA values for scan")
else:
    print(f"  Off-Jensen gradient negligible; fold is critical in off-Jensen directions")
    print(f"  Combined with Hessian analysis: fold is a saddle/maximum of S in all 35D")

# =============================================================================
# 16. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: S76-B10-OFF-JENSEN")
print("=" * 78)

# Gate definition:
# PASS: at least one negative Hessian eigenvalue (d^2S < 0 in some direction)
#       This means the spectral action has a direction where it decreases,
#       and V = -S has a direction where it increases = restoring force.
# FAIL: all eigenvalues positive at fold
# INFO: indefinite but minimum requires tau outside [0.1, 1.0]

# All eigenvalues of H_35 (the Hessian of S):
n_neg_final = int(np.sum(evals_35 < -zero_threshold))  # (local)
n_pos_final = int(np.sum(evals_35 > zero_threshold))  # (local)
n_zero_final = int(np.sum(np.abs(evals_35) <= zero_threshold))  # (local)

print(f"\n  35x35 Hessian eigenvalues:")
print(f"    Most negative: {evals_35[0]:.4f}")
print(f"    Most positive: {evals_35[-1]:.4f}")
print(f"    Negative: {n_neg_final}")
print(f"    Positive: {n_pos_final}")
print(f"    Near-zero: {n_zero_final}")
print(f"    Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)")

if n_neg_final > 0:
    gate_verdict = "PASS"
    print(f"\n  VERDICT: **PASS**")
    print(f"  {n_neg_final} negative eigenvalue(s) found in the 35D volume-preserving Hessian.")
    print(f"  The spectral action curves downward in {n_neg_final} direction(s).")
    print(f"  V = -S curves upward in those directions = restoring force exists.")
elif n_pos_final > 0 and n_neg_final == 0:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: **FAIL**")
    print(f"  All eigenvalues non-negative ({n_pos_final} positive, {n_zero_final} near-zero).")
    print(f"  The spectral action is a local minimum at the fold.")
    print(f"  V = -S is a local maximum: no restoring force, pure runaway.")
else:
    # All near-zero: degenerate case
    gate_verdict = "INFO"
    print(f"\n  VERDICT: **INFO**")
    print(f"  All eigenvalues near zero. Flat directions dominate.")

# Physical interpretation
print(f"\n  Physical interpretation:")
if n_neg_final == 35:
    print(f"  ALL 35 eigenvalues negative: S is a strict local MAXIMUM at the fold")
    print(f"  => V = -S is a strict local MINIMUM (restoring potential in ALL directions)")
    print(f"  => The fold metric is the most unstable point: modulus rolls AWAY from fold")
    print(f"  => This is CONSISTENT with the transit picture (dS/dtau drives evolution)")
    print(f"  => But modulus is CONFINED in off-Jensen directions (no off-Jensen escape)")
elif n_neg_final > 0 and n_pos_final > 0:
    print(f"  MIXED signature: S is a saddle point at the fold")
    print(f"  => V = -S is also a saddle point")
    print(f"  => {n_neg_final} restoring directions and {n_pos_final} unstable directions")
elif n_neg_final > 0 and n_pos_final == 0:
    print(f"  All non-positive: S is a local maximum (possibly with flat directions)")
    print(f"  => V = -S is a local minimum (stable equilibrium)")

# =============================================================================
# 17. Key Numbers Summary
# =============================================================================
print("\n" + "=" * 78)
print("  KEY NUMBERS SUMMARY")
print("=" * 78)

print(f"\n  1. 35x35 Hessian eigenvalues (5 most negative):")
for k in range(min(5, 35)):
    print(f"       lambda_{k} = {evals_35[k]:.4f}")
print(f"  2. 35x35 Hessian eigenvalues (5 least negative / most positive):")
for k in range(max(0, 35-5), 35):
    print(f"       lambda_{k} = {evals_35[k]:.4f}")
print(f"  3. Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)")
print(f"  4. Gate verdict: {gate_verdict}")
print(f"  5. Jensen direction d^2S: {d2S_jensen_proj:.4f}")
print(f"  6. Volume constraint max violation: {max_vol_violation:.2e}")
print(f"  7. Gradient |off-Jensen|/|Jensen|: {grad_off_norm/abs(grad_jensen) if abs(grad_jensen) > 1e-10 else np.inf:.6f}")
print(f"  8. Convergence: 3-step check on {n_conv_check} directions")
print(f"  9. Total SA evaluations: ~{2*35 + 2*n_pairs_total + 4*n_conv_check + 2*35 + n_scan}")
print(f" 10. Total computation time: {time.time() - t_global_start:.1f}s")

# =============================================================================
# 18. Save Data
# =============================================================================
print("\n--- 18. Saving data ---")

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
npz_path = os.path.join(DATA_DIR, 's76_off_jensen_moduli.npz')

np.savez(npz_path,
    # Hessian data
    H_35=H_35,
    evals_35=evals_35,
    evecs_35=evecs_35,
    d2SA_diag=d2SA_diag,
    diag_pd_check=diag_pd_check,
    # Basis information
    Q_projection=Q,
    v_vol_hat=v_vol_hat,
    v_jensen_35_hat=v_jensen_35_hat,
    basis_36_labels=np.array(basis_36_labels),
    # Cross-checks
    d2S_jensen_proj=d2S_jensen_proj,
    max_vol_violation=max_vol_violation,
    d2SA_coarse=d2SA_coarse,
    d2SA_fine=d2SA_fine,
    # Gradient
    grad_SA=grad_SA,
    grad_norm=grad_norm,
    grad_jensen=grad_jensen,
    grad_off_norm=grad_off_norm,
    # Fold reference
    SA_fold=SA_fold,
    Lambda_sq=Lambda_sq,
    g_fold=g_fold,
    det_fold=det_fold,
    # Gate
    gate_verdict=gate_verdict,
    n_pos=n_pos_final,
    n_neg=n_neg_final,
    n_zero=n_zero_final,
    signature=f"({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)",
)
print(f"  Saved to {npz_path}")

# =============================================================================
# 19. Plots
# =============================================================================
print("\n--- 19. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'S76-B10-OFF-JENSEN: 35D Volume-Preserving Hessian\n'
             f'Gate: {gate_verdict} | Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)',
             fontsize=14, fontweight='bold')

# Panel 1: Eigenvalue spectrum
ax = axes[0, 0]
colors = ['red' if ev > zero_threshold else ('gray' if abs(ev) <= zero_threshold else 'blue')
          for ev in evals_35]
ax.bar(range(35), evals_35, color=colors, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title('35D Hessian Eigenvalue Spectrum')

# Panel 2: Hessian matrix heatmap
ax = axes[0, 1]
vmax = max(abs(H_35.min()), abs(H_35.max()))
if vmax > 0:
    im = ax.imshow(H_35, cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='auto')
    plt.colorbar(im, ax=ax, label=r'd$^2$S/d$\epsilon_i$d$\epsilon_j$')
ax.set_title('35x35 Hessian Matrix')
ax.set_xlabel('Direction j')
ax.set_ylabel('Direction i')

# Panel 3: Convergence check
ax = axes[0, 2]
valid_conv = ~np.isnan(d2SA_coarse[:n_conv_check]) & ~np.isnan(d2SA_fine[:n_conv_check])
if np.any(valid_conv):
    x_conv = np.arange(n_conv_check)[valid_conv]
    ax.plot(x_conv, d2SA_coarse[:n_conv_check][valid_conv], 's-', label=r'$\epsilon$=0.01', alpha=0.7)
    ax.plot(x_conv, d2SA_diag[:n_conv_check][valid_conv], 'o-', label=r'$\epsilon$=0.001', alpha=0.7)
    ax.plot(x_conv, d2SA_fine[:n_conv_check][valid_conv], '^-', label=r'$\epsilon$=0.0001', alpha=0.7)
    ax.legend()
ax.set_xlabel('Direction index')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title('Convergence: Three Step Sizes')

# Panel 4: Diagonal d^2S values
ax = axes[1, 0]
valid_diag = diag_pd_check
ax.bar(np.arange(35)[valid_diag], d2SA_diag[valid_diag], color='steelblue', alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Basis direction')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title('Diagonal Hessian Elements (35D)')

# Panel 5: V = -S eigenvalues
ax = axes[1, 1]
V_colors = ['green' if v > zero_threshold else ('gray' if abs(v) <= zero_threshold else 'red')
            for v in V_evals]
ax.bar(range(35), sorted(V_evals), color=V_colors, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'd$^2$V/d$\epsilon^2$ = -d$^2$S/d$\epsilon^2$')
ax.set_title('Effective Potential V = -S (sorted)')

# Panel 6: Gradient decomposition
ax = axes[1, 2]
grad_valid = ~np.isnan(grad_SA)
if np.any(grad_valid):
    ax.bar(np.arange(35)[grad_valid], grad_SA[grad_valid], color='orange', alpha=0.7)
    ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Basis direction (35D)')
ax.set_ylabel('dS/d$\\epsilon$')
ax.set_title(f'SA Gradient (|off-Jensen|/|Jensen| = {grad_off_norm/abs(grad_jensen) if abs(grad_jensen) > 1e-10 else np.inf:.4f})')

plt.tight_layout()
png_path = os.path.join(DATA_DIR, 's76_off_jensen_moduli.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved to {png_path}")

print(f"\n  Total runtime: {time.time() - t_global_start:.1f}s")
print("  DONE.")
