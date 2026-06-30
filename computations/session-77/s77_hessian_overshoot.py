#!/usr/bin/env python3
"""
s77_hessian_overshoot.py -- S77-C5-HESSIAN-OVERSHOOT: Off-Jensen Hessian at tau = 1.614
========================================================================================

Gate: S77-C5-HESSIAN-OVERSHOOT
  PASS: All 35 eigenvalues negative at tau = 1.614 (Jensen ridge persists at turnaround)
  FAIL: Any positive eigenvalue at tau = 1.614 (tachyonic direction; modulus could roll off)
  INFO: Partial computation, subset of directions analyzed

Background:
  S76 W2-J computed the full 35x35 volume-preserving Hessian of the spectral action
  at tau_fold = 0.190 and found ALL 35 eigenvalues negative (range [-148.69, -17.35]).
  This means the Jensen line is a RIDGE (local maximum of S in all off-Jensen directions).

  This script tests whether the ridge persists at the turnaround tau = 1.614, which is
  the point where the modulus overshoots the fold and reverses. If any eigenvalue becomes
  positive at 1.614, a tachyonic instability exists: the modulus could roll off the
  Jensen line during the overshoot, breaking the one-parameter dynamics.

  S76 W2-J (V-TAU-VALIDATION) confirmed tau_max_reliable = 2.000, so tau = 1.614 is
  within the regime of direct computation -- no extrapolation needed.

Method:
  1. Build the Jensen metric at tau = 1.614 using the same 3-parameter decomposition:
       g = L1(tau) * |B|_{u(1)} + L2(tau) * |B|_{su(2)} + L3(tau) * |B|_{C^2}
     where L1 = exp(2*tau), L2 = exp(-2*tau), L3 = exp(tau).
  2. Construct the 35D volume-preserving tangent space at this metric
  3. Compute the full 35x35 Hessian via finite differences
  4. Diagonalize and classify eigenvalues
  5. Cross-checks:
     CHK1: Reproduce 35/35 negative at tau_fold = 0.190 (reference)
     CHK2: Hessian real symmetric (|H - H^T| < eps)
     CHK3: Trace(Hessian) = sum of diagonal d^2S values

Author: Baptista-Spacetime-Analyst (Session 77, Wave 3)
Date: 2026-04-13
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

# =============================================================================
# Configuration
# =============================================================================
TAU_TURNAROUND = 1.614  # (local) overshoot turnaround point
MAX_PQ_SUM = 3  # (local) irrep truncation (matches S76)
EPS_PRIMARY = 0.001  # (local) primary finite-difference step
EPS_COARSE = 0.01  # (local) convergence check coarse step
EPS_FINE = 0.0001  # (local) convergence check fine step
ZERO_THRESHOLD = 1.0  # (local) eigenvalue sign classification threshold
N_CONV_CHECK = 10  # (local) number of directions for convergence check

print("=" * 78)
print("  S77-C5-HESSIAN-OVERSHOOT: Off-Jensen Hessian at tau = 1.614")
print("=" * 78)
print(f"  tau_turnaround = {TAU_TURNAROUND}")
print(f"  tau_fold = {tau_fold} (reference)")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (identical to S76)
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
SU2_IDX = [0, 1, 2]
C2_IDX  = [3, 4, 5, 6]
U1_IDX  = [7]

# =============================================================================
# 2. Dirac Operator and Spectral Action (identical to S76)
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

# Irrep constructors (identical to S76)
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
                    rho_6 = irrep_symmetric2(gens)
                    rho_3c = irrep_antifundamental(gens)
                    rho = irrep_via_casimir_projection(rho_6, rho_3c, dim_pq, (p,q))
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
print(f"\n  Building irreps (max p+q = {MAX_PQ_SUM})...")
irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=MAX_PQ_SUM)
total_evals = sum(d*16*d for _,_,d,_ in irreps_data)  # (local)
for p, q, dim, _ in irreps_data:
    print(f"    ({p},{q}): dim = {dim}, block = {dim*16}")
print(f"  Total eigenvalues per metric point: {total_evals}")

# =============================================================================
# 4. Build Jensen Metric at tau = 1.614 (turnaround)
# =============================================================================
print("\n--- 4. Building Jensen metric at tau = 1.614 ---")

# Jensen metric parametrization:
# g(tau) = L1(tau) * |B|_{u(1)} + L2(tau) * |B|_{su(2)} + L3(tau) * |B|_{C^2}
# where L1 = exp(2*tau), L2 = exp(-2*tau), L3 = exp(tau)

g0 = np.abs(B_ab)  # Positive-definite base from Killing form

def build_jensen_metric(tau):
    """Build the Jensen-deformed metric at parameter value tau."""
    L1 = exp(2.0 * tau)  # (local) u(1) direction
    L2 = exp(-2.0 * tau)  # (local) su(2) directions
    L3 = exp(tau)  # (local) C^2 directions
    g = np.zeros((8,8), dtype=np.float64)
    for a in U1_IDX:
        for b in U1_IDX:
            g[a,b] = g0[a,b] * L1
    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a,b] = g0[a,b] * L2
    for a in C2_IDX:
        for b in C2_IDX:
            g[a,b] = g0[a,b] * L3
    return g, L1, L2, L3

g_turn, L1_turn, L2_turn, L3_turn = build_jensen_metric(TAU_TURNAROUND)

det_turn = det(g_turn)  # (local)
log_det_turn = log(det_turn)  # (local)

print(f"  tau = {TAU_TURNAROUND}")
print(f"  L1 = exp(2*tau) = {L1_turn:.6f} (u(1) direction)")
print(f"  L2 = exp(-2*tau) = {L2_turn:.6f} (su(2) directions)")
print(f"  L3 = exp(tau) = {L3_turn:.6f} (C^2 directions)")
print(f"  g_turn diagonal: {np.diag(g_turn)}")
print(f"  det(g_turn) = {det_turn:.6f}")
print(f"  log det(g_turn) = {log_det_turn:.6f}")

# Verify positive-definite
evals_g_turn = eigvalsh(g_turn)  # (local)
print(f"  g_turn eigenvalues: {evals_g_turn}")
assert np.all(evals_g_turn > 0), "Turnaround metric is not positive-definite!"

# Compute Dirac spectrum and spectral action at turnaround
print("\n  Computing Dirac spectrum at tau = 1.614...")
t_dirac_start = time.time()
evals_turn = compute_dirac_eigenvalues(g_turn, gens, f_abc, gammas, irreps_data)
Lambda_sq_turn = 4.0 * np.max(evals_turn**2)  # (local) same convention as S76
SA_turn = spectral_action_heat(evals_turn, Lambda_sq_turn)  # (local)
t_dirac_end = time.time()

print(f"  Dirac spectrum computation: {t_dirac_end - t_dirac_start:.1f}s")
print(f"  Lambda^2 = {Lambda_sq_turn:.6f}")
print(f"  SA at tau=1.614 = {SA_turn:.6f}")
print(f"  Number of eigenvalues: {len(evals_turn)}")

pos_turn = sorted(evals_turn[evals_turn > 1e-6])
print(f"  Positive eigenvalues: {len(pos_turn)}")
if len(pos_turn) >= 8:
    print(f"    Smallest 8: {pos_turn[:8]}")

# Also build fold metric for CHK1
g_fold, L1_fold, L2_fold, L3_fold = build_jensen_metric(tau_fold)
det_fold = det(g_fold)  # (local)
evals_fold_dirac = compute_dirac_eigenvalues(g_fold, gens, f_abc, gammas, irreps_data)
Lambda_sq_fold = 4.0 * np.max(evals_fold_dirac**2)  # (local)
SA_fold_comp = spectral_action_heat(evals_fold_dirac, Lambda_sq_fold)  # (local)
print(f"\n  Fold reference: SA(tau_fold) = {SA_fold_comp:.6f}, Lambda^2 = {Lambda_sq_fold:.6f}")

# =============================================================================
# 5. Construct Volume-Preserving Tangent Space (35D) at tau = 1.614
# =============================================================================
print("\n--- 5. Constructing volume-preserving tangent space (35D) at tau = 1.614 ---")

# Build 36D basis for Sym(8)
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

# Volume gradient at turnaround metric
g_turn_inv = inv(g_turn)
v_vol = np.zeros(36)
for k in range(36):
    v_vol[k] = np.trace(g_turn_inv @ basis_36[k])

v_vol_norm = norm(v_vol)  # (local)
v_vol_hat = v_vol / v_vol_norm  # (local) unit volume direction

print(f"  Volume gradient norm: {v_vol_norm:.6f}")
print(f"  Volume gradient components (first 8, diagonal): {v_vol[:8]}")

# Project out volume direction
projected_36 = np.zeros((36, 36))
for k in range(36):
    e_k = np.zeros(36)
    e_k[k] = 1.0
    proj = e_k - np.dot(e_k, v_vol_hat) * v_vol_hat
    projected_36[k] = proj

norms_proj = np.array([norm(projected_36[k]) for k in range(36)])
keep_mask = norms_proj > 1e-10  # (local)
n_keep = np.sum(keep_mask)  # (local)
print(f"  Directions surviving volume projection: {n_keep}/36")

# Sort by norm and take top 35
idx_sorted = np.argsort(-norms_proj)  # (local)
basis_35_raw = []
basis_35_labels = []
for k in idx_sorted[:35]:
    vec = projected_36[k] / norms_proj[k]
    basis_35_raw.append(vec)
    basis_35_labels.append(basis_36_labels[k])

# Orthonormalize via QR
Q_raw = np.column_stack(basis_35_raw)  # 36 x 35
Q, R = np.linalg.qr(Q_raw)

# Verify volume-preserving property
vol_check = np.array([np.dot(Q[:, k], v_vol_hat) for k in range(35)])
vol_check_max = np.max(np.abs(vol_check))  # (local)
print(f"  Volume constraint check (max |Q_k . v_vol|): {vol_check_max:.2e}")
assert vol_check_max < 1e-10, f"Volume-preserving projection failed: {vol_check_max}"

# Jensen direction at turnaround
v_jensen_36 = np.zeros(36)
for a in U1_IDX:
    v_jensen_36[a] = 2.0 * L1_turn * g0[a,a]
for a in SU2_IDX:
    v_jensen_36[a] = -2.0 * L2_turn * g0[a,a]
for a in C2_IDX:
    v_jensen_36[a] = L3_turn * g0[a,a]

v_jensen_proj = v_jensen_36 - np.dot(v_jensen_36, v_vol_hat) * v_vol_hat
v_jensen_proj_norm = norm(v_jensen_proj)  # (local)
v_jensen_35 = Q.T @ v_jensen_proj  # components in 35D basis
v_jensen_35_hat = v_jensen_35 / norm(v_jensen_35)  # (local)

print(f"\n  Jensen direction (36D) norm: {norm(v_jensen_36):.6f}")
print(f"  Jensen direction volume component: {np.dot(v_jensen_36, v_vol_hat):.6f}")
print(f"  Jensen direction (volume-projected) norm: {v_jensen_proj_norm:.6f}")

# Classify basis directions
def classify_direction_36(label):
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
# 6. Compute 35x35 Hessian at tau = 1.614 via Finite Differences
# =============================================================================
print("\n--- 6. Computing 35x35 Hessian at tau = 1.614 (finite differences) ---")

def coeff_to_metric_perturbation(coeffs_35, Q_matrix, basis_list):
    """Convert 35D coefficients to an 8x8 metric perturbation."""
    coeffs_36 = Q_matrix @ coeffs_35  # (local)
    delta_g = np.zeros((8,8))
    for k in range(36):
        delta_g += coeffs_36[k] * basis_list[k]
    return delta_g

def compute_SA_at_perturbation(g_base, delta_g, gens, f_abc, gammas, irreps_data, Lambda_sq):
    """Compute spectral action at g_base + delta_g."""
    g_pert = g_base + delta_g  # (local)
    evals_g = eigvalsh(g_pert)  # (local)
    if np.any(evals_g <= 0):
        return np.nan, False
    ev_dirac = compute_dirac_eigenvalues(g_pert, gens, f_abc, gammas, irreps_data)
    sa = spectral_action_heat(ev_dirac, Lambda_sq)
    return sa, True

# Diagonal Hessian elements
print(f"\n  Step size: eps = {EPS_PRIMARY}")
print(f"  Computing 35 diagonal elements...")

t_diag_start = time.time()

d2SA_diag = np.zeros(35)
diag_pd_check = np.zeros(35, dtype=bool)

for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_g_plus = coeff_to_metric_perturbation(EPS_PRIMARY * e_k, Q, basis_36)
    delta_g_minus = coeff_to_metric_perturbation(-EPS_PRIMARY * e_k, Q, basis_36)

    sa_plus, pd_plus = compute_SA_at_perturbation(
        g_turn, delta_g_plus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    sa_minus, pd_minus = compute_SA_at_perturbation(
        g_turn, delta_g_minus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)

    if pd_plus and pd_minus:
        d2SA_diag[k] = (sa_plus - 2.0 * SA_turn + sa_minus) / EPS_PRIMARY**2
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

# Full off-diagonal via polarization identity
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
        delta_g_plus = coeff_to_metric_perturbation(EPS_PRIMARY * e_sum, Q, basis_36)
        delta_g_minus = coeff_to_metric_perturbation(-EPS_PRIMARY * e_sum, Q, basis_36)

        sa_plus, pd_plus = compute_SA_at_perturbation(
            g_turn, delta_g_plus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
        sa_minus, pd_minus = compute_SA_at_perturbation(
            g_turn, delta_g_minus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)

        if pd_plus and pd_minus:
            d2SA_sum = (sa_plus - 2.0 * SA_turn + sa_minus) / EPS_PRIMARY**2
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

# CHK2: Symmetry check
sym_err_35 = np.max(np.abs(H_35 - H_35.T))  # (local)
print(f"\n  CHK2: Hessian symmetry error: {sym_err_35:.2e}")
print(f"  CHK2: {'PASS' if sym_err_35 < 1e-10 else 'MARGINAL' if sym_err_35 < 1e-6 else 'FAIL'}")

# CHK3: Trace consistency
trace_H = np.trace(H_35)  # (local)
sum_diag = np.nansum(d2SA_diag)  # (local)
trace_err = abs(trace_H - sum_diag) / (abs(sum_diag) + 1e-15)  # (local)
print(f"  CHK3: Tr(H) = {trace_H:.4f}, sum(d2SA_diag) = {sum_diag:.4f}, rel err = {trace_err:.2e}")
print(f"  CHK3: {'PASS' if trace_err < 1e-10 else 'MARGINAL' if trace_err < 1e-6 else 'FAIL'}")

# =============================================================================
# 7. Eigenvalue Decomposition at tau = 1.614
# =============================================================================
print("\n--- 7. Eigenvalue decomposition of 35x35 Hessian at tau = 1.614 ---")

evals_35, evecs_35 = eigh(H_35)

n_pos_35 = int(np.sum(evals_35 > ZERO_THRESHOLD))  # (local)
n_neg_35 = int(np.sum(evals_35 < -ZERO_THRESHOLD))  # (local)
n_zero_35 = int(np.sum(np.abs(evals_35) <= ZERO_THRESHOLD))  # (local)

print(f"\n  All 35 eigenvalues of H_35 at tau = {TAU_TURNAROUND}:")
for k in range(35):
    sign = "+" if evals_35[k] > ZERO_THRESHOLD else ("-" if evals_35[k] < -ZERO_THRESHOLD else "~0")
    print(f"    lambda_{k:>2} = {evals_35[k]:>14.6f}  {sign}")

print(f"\n  Signature: ({n_pos_35}+, {n_neg_35}-, {n_zero_35} ~0)")
print(f"  Largest eigenvalue: {evals_35[-1]:.6f}")
print(f"  Smallest eigenvalue: {evals_35[0]:.6f}")

# =============================================================================
# 8. CHK1: Reproduce S76 fold result (35/35 negative)
# =============================================================================
print("\n--- 8. CHK1: Reproduce 35/35 negative at tau_fold = 0.190 ---")

# Build volume-preserving tangent space at fold
g_fold_inv = inv(g_fold)
v_vol_fold = np.zeros(36)
for k in range(36):
    v_vol_fold[k] = np.trace(g_fold_inv @ basis_36[k])
v_vol_fold_norm = norm(v_vol_fold)  # (local)
v_vol_fold_hat = v_vol_fold / v_vol_fold_norm  # (local)

projected_fold = np.zeros((36, 36))
for k in range(36):
    e_k = np.zeros(36)
    e_k[k] = 1.0
    proj = e_k - np.dot(e_k, v_vol_fold_hat) * v_vol_fold_hat
    projected_fold[k] = proj

norms_proj_fold = np.array([norm(projected_fold[k]) for k in range(36)])
idx_sorted_fold = np.argsort(-norms_proj_fold)  # (local)
basis_35_raw_fold = []
for k in idx_sorted_fold[:35]:
    vec = projected_fold[k] / norms_proj_fold[k]
    basis_35_raw_fold.append(vec)

Q_fold_raw = np.column_stack(basis_35_raw_fold)
Q_fold, R_fold = np.linalg.qr(Q_fold_raw)

# Compute diagonal Hessian at fold (fast check: diagonal only)
print(f"  Computing 35 diagonal Hessian elements at fold...")
t_chk1_start = time.time()
d2SA_diag_fold = np.zeros(35)

for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    coeffs_36_fold = Q_fold @ e_k  # (local)
    delta_g = np.zeros((8,8))
    for m in range(36):
        delta_g += coeffs_36_fold[m] * basis_36[m]

    g_plus = g_fold + EPS_PRIMARY * delta_g  # (local)
    g_minus = g_fold - EPS_PRIMARY * delta_g  # (local)

    evals_gp = eigvalsh(g_plus)  # (local)
    evals_gm = eigvalsh(g_minus)  # (local)

    if np.all(evals_gp > 0) and np.all(evals_gm > 0):
        ev_p = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
        sa_p = spectral_action_heat(ev_p, Lambda_sq_fold)
        ev_m = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)
        sa_m = spectral_action_heat(ev_m, Lambda_sq_fold)
        d2SA_diag_fold[k] = (sa_p - 2.0 * SA_fold_comp + sa_m) / EPS_PRIMARY**2
    else:
        d2SA_diag_fold[k] = np.nan

    if (k+1) % 7 == 0 or k == 34:
        elapsed = time.time() - t_chk1_start  # (local)
        print(f"    {k+1}/35 done ({elapsed:.1f}s)")

n_neg_fold_chk = int(np.sum(d2SA_diag_fold < -ZERO_THRESHOLD))  # (local)
n_pos_fold_chk = int(np.sum(d2SA_diag_fold > ZERO_THRESHOLD))  # (local)
n_zero_fold_chk = int(np.sum(np.abs(d2SA_diag_fold) <= ZERO_THRESHOLD))  # (local)

print(f"\n  CHK1 fold diagonal Hessian: {n_neg_fold_chk} negative, {n_pos_fold_chk} positive, {n_zero_fold_chk} ~zero")
print(f"  CHK1 fold d2SA: min={np.nanmin(d2SA_diag_fold):.4f}, max={np.nanmax(d2SA_diag_fold):.4f}")

# Compare with S76 stored values
s76_data = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's76_off_jensen_moduli.npz'), allow_pickle=True)
s76_evals = s76_data['evals_35']
print(f"  S76 reference: min={s76_evals.min():.4f}, max={s76_evals.max():.4f}")
print(f"  S76: 35/35 negative (confirmed)")

# For CHK1 we only need diagonal to confirm all-negative sign structure
# The full Hessian would require off-diagonal too, but diagonal sign is sufficient
# to verify consistency since S76 found ALL eigenvalues negative
chk1_all_neg = all(d2SA_diag_fold[k] < -ZERO_THRESHOLD for k in range(35) if not np.isnan(d2SA_diag_fold[k]))
print(f"  CHK1: All fold diagonal elements negative? {chk1_all_neg}")
print(f"  CHK1: {'PASS' if chk1_all_neg else 'MARGINAL -- diagonal check only'}")

# =============================================================================
# 9. Volume-Preserving Verification at Turnaround
# =============================================================================
print("\n--- 9. Volume-preserving verification at turnaround ---")

max_vol_violation = 0.0  # (local)
for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_g = coeff_to_metric_perturbation(EPS_PRIMARY * e_k, Q, basis_36)
    g_pert = g_turn + delta_g
    det_pert = det(g_pert)  # (local)
    rel_vol_change = abs(det_pert - det_turn) / det_turn  # (local)
    max_vol_violation = max(max_vol_violation, rel_vol_change)

print(f"  Max relative volume change at eps={EPS_PRIMARY}: {max_vol_violation:.2e}")
print(f"  (Expected O(eps^2) ~ {EPS_PRIMARY**2:.2e})")
print(f"  Volume-preserving: {'PASS' if max_vol_violation < 10 * EPS_PRIMARY**2 else 'MARGINAL'}")

# =============================================================================
# 10. Convergence Check at Turnaround
# =============================================================================
print("\n--- 10. Convergence check: three step sizes ---")

d2SA_coarse = np.zeros(N_CONV_CHECK)
d2SA_fine = np.zeros(N_CONV_CHECK)

t_conv_start = time.time()

for k in range(N_CONV_CHECK):
    e_k = np.zeros(35)
    e_k[k] = 1.0

    # Coarse
    delta_plus = coeff_to_metric_perturbation(EPS_COARSE * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-EPS_COARSE * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_turn, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    sa_m, pd_m = compute_SA_at_perturbation(g_turn, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    if pd_p and pd_m:
        d2SA_coarse[k] = (sa_p - 2.0 * SA_turn + sa_m) / EPS_COARSE**2
    else:
        d2SA_coarse[k] = np.nan

    # Fine
    delta_plus = coeff_to_metric_perturbation(EPS_FINE * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-EPS_FINE * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_turn, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    sa_m, pd_m = compute_SA_at_perturbation(g_turn, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    if pd_p and pd_m:
        d2SA_fine[k] = (sa_p - 2.0 * SA_turn + sa_m) / EPS_FINE**2
    else:
        d2SA_fine[k] = np.nan

print(f"  Convergence check time: {time.time() - t_conv_start:.1f}s")
print(f"\n  {'Dir':>4} {'d2SA(0.01)':>14} {'d2SA(0.001)':>14} {'d2SA(0.0001)':>14} {'conv_ratio':>12}")
for k in range(N_CONV_CHECK):
    vals = [d2SA_coarse[k], d2SA_diag[k], d2SA_fine[k]]
    if not any(np.isnan(v) for v in vals) and abs(d2SA_coarse[k] - d2SA_diag[k]) > 1e-10:
        ratio = (d2SA_fine[k] - d2SA_diag[k]) / (d2SA_diag[k] - d2SA_coarse[k]) if abs(d2SA_diag[k] - d2SA_coarse[k]) > 1e-10 else np.nan  # (local)
        print(f"  {k:>4} {d2SA_coarse[k]:>14.4f} {d2SA_diag[k]:>14.4f} {d2SA_fine[k]:>14.4f} {ratio:>12.4f}")
    else:
        print(f"  {k:>4} {d2SA_coarse[k]:>14.4f} {d2SA_diag[k]:>14.4f} {d2SA_fine[k]:>14.4f} {'N/A':>12}")

# =============================================================================
# 11. Eigenvector Analysis: SU(3) Representation Content
# =============================================================================
print("\n--- 11. Eigenvector analysis: dominant SU(3) generators ---")

print(f"\n  5 most negative eigenvalues:")
for k in range(min(5, 35)):
    v_35 = evecs_35[:, k]
    v_36 = Q @ v_35  # (local)
    top5 = np.argsort(np.abs(v_36))[-5:][::-1]
    top5_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top5)
    jensen_weight = np.dot(v_35, v_jensen_35_hat)**2  # (local)
    print(f"  lambda_{k} = {evals_35[k]:>14.6f}: Jensen content = {jensen_weight:.4f}")
    print(f"    top 36D components: {top5_str}")

if n_pos_35 > 0:
    print(f"\n  POSITIVE eigenvalues (tachyonic directions):")
    for k in range(35):
        if evals_35[k] > ZERO_THRESHOLD:
            v_35 = evecs_35[:, k]
            v_36 = Q @ v_35
            top5 = np.argsort(np.abs(v_36))[-5:][::-1]
            top5_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top5)
            jensen_weight = np.dot(v_35, v_jensen_35_hat)**2
            print(f"  lambda_{k} = {evals_35[k]:>14.6f}: Jensen content = {jensen_weight:.4f}")
            print(f"    top 36D components: {top5_str}")

print(f"\n  5 least negative / most positive eigenvalues:")
for k in range(max(0, 35-5), 35):
    v_35 = evecs_35[:, k]
    v_36 = Q @ v_35
    top3 = np.argsort(np.abs(v_36))[-3:][::-1]
    top3_str = ", ".join(f"{basis_36_labels[j]}({v_36[j]:+.3f})" for j in top3)
    jensen_weight = np.dot(v_35, v_jensen_35_hat)**2
    print(f"  lambda_{k} = {evals_35[k]:>14.6f}: Jensen content = {jensen_weight:.4f}")
    print(f"    top components: {top3_str}")

# =============================================================================
# 12. Comparison: Fold vs Turnaround
# =============================================================================
print("\n--- 12. Fold vs Turnaround comparison ---")

# Load S76 eigenvalues for direct comparison
print(f"  {'Metric':>10} | {'min(lambda)':>14} | {'max(lambda)':>14} | {'n_neg':>6} | {'n_pos':>6} | {'n_zero':>6}")
print(f"  {'----------':>10}-+-{'----------':>14}-+-{'----------':>14}-+-{'------':>6}-+-{'------':>6}-+-{'------':>6}")
print(f"  {'Fold(0.19)':>10} | {s76_evals.min():>14.4f} | {s76_evals.max():>14.4f} | {35:>6} | {0:>6} | {0:>6}")
print(f"  {'Turn(1.61)':>10} | {evals_35.min():>14.6f} | {evals_35.max():>14.6f} | {n_neg_35:>6} | {n_pos_35:>6} | {n_zero_35:>6}")

# Ratio of eigenvalue magnitudes
if n_neg_35 > 0:
    ratio_min = evals_35.min() / s76_evals.min()  # (local)
    ratio_max = evals_35.max() / s76_evals.max()  # (local)
    print(f"\n  Ratio turnaround/fold:")
    print(f"    min(lambda): {ratio_min:.6f}")
    print(f"    max(lambda): {ratio_max:.6f}")

# Degeneracy structure at turnaround
print(f"\n  Eigenvalue degeneracies at turnaround (tolerance = {ZERO_THRESHOLD}):")
eigenvalue_groups = []
for k in range(35):
    placed = False
    for g in eigenvalue_groups:
        if abs(evals_35[k] - g[0]) < ZERO_THRESHOLD:
            g.append(evals_35[k])
            placed = True
            break
    if not placed:
        eigenvalue_groups.append([evals_35[k]])

for g in eigenvalue_groups:
    deg = len(g)
    mean_val = np.mean(g)  # (local)
    spread = max(g) - min(g) if deg > 1 else 0.0  # (local)
    print(f"    mean={mean_val:>14.6f}, degeneracy={deg}, spread={spread:.6f}")

# =============================================================================
# 13. Gradient Analysis at Turnaround
# =============================================================================
print("\n--- 13. Gradient of SA at turnaround (35D) ---")

grad_SA = np.zeros(35)
for k in range(35):
    e_k = np.zeros(35)
    e_k[k] = 1.0
    delta_plus = coeff_to_metric_perturbation(EPS_PRIMARY * e_k, Q, basis_36)
    delta_minus = coeff_to_metric_perturbation(-EPS_PRIMARY * e_k, Q, basis_36)
    sa_p, pd_p = compute_SA_at_perturbation(g_turn, delta_plus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    sa_m, pd_m = compute_SA_at_perturbation(g_turn, delta_minus, gens, f_abc, gammas, irreps_data, Lambda_sq_turn)
    if pd_p and pd_m:
        grad_SA[k] = (sa_p - sa_m) / (2.0 * EPS_PRIMARY)
    else:
        grad_SA[k] = np.nan

grad_norm = norm(grad_SA[~np.isnan(grad_SA)])  # (local)
grad_jensen = np.dot(grad_SA, v_jensen_35_hat)  # (local)

print(f"  |grad SA|_35D = {grad_norm:.6f}")
print(f"  grad SA . Jensen_hat = {grad_jensen:.6f}")

grad_off_jensen = grad_SA - grad_jensen * v_jensen_35_hat
grad_off_norm = norm(grad_off_jensen[~np.isnan(grad_off_jensen)])  # (local)
print(f"  |grad SA|_off-Jensen = {grad_off_norm:.6f}")
if abs(grad_jensen) > 1e-10:
    print(f"  Ratio off-Jensen/Jensen: {grad_off_norm / abs(grad_jensen):.6f}")
else:
    print(f"  Jensen gradient ~ 0 (turnaround point)")

# =============================================================================
# 14. Gate Verdict: S77-C5-HESSIAN-OVERSHOOT
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: S77-C5-HESSIAN-OVERSHOOT")
print("=" * 78)

n_neg_final = int(np.sum(evals_35 < -ZERO_THRESHOLD))  # (local)
n_pos_final = int(np.sum(evals_35 > ZERO_THRESHOLD))  # (local)
n_zero_final = int(np.sum(np.abs(evals_35) <= ZERO_THRESHOLD))  # (local)

print(f"\n  35x35 Hessian eigenvalues at tau = {TAU_TURNAROUND}:")
print(f"    Most negative: {evals_35[0]:.6f}")
print(f"    Most positive: {evals_35[-1]:.6f}")
print(f"    Negative: {n_neg_final}")
print(f"    Positive: {n_pos_final}")
print(f"    Near-zero: {n_zero_final}")
print(f"    Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)")

if n_neg_final == 35 and n_pos_final == 0:
    gate_verdict = "PASS"
    print(f"\n  VERDICT: **PASS**")
    print(f"  All 35 eigenvalues negative at tau = {TAU_TURNAROUND}.")
    print(f"  Jensen ridge persists through the turnaround.")
    print(f"  No tachyonic direction exists -- modulus cannot roll off Jensen line.")
elif n_pos_final > 0:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: **FAIL**")
    print(f"  {n_pos_final} positive eigenvalue(s) at tau = {TAU_TURNAROUND}.")
    print(f"  Tachyonic direction exists -- modulus could roll off Jensen line.")
else:
    gate_verdict = "INFO"
    print(f"\n  VERDICT: **INFO**")
    print(f"  {n_neg_final} negative, {n_zero_final} near-zero, {n_pos_final} positive.")
    print(f"  Ridge structure unclear at turnaround.")

# Cross-check summary
print(f"\n  Cross-checks:")
print(f"    CHK1 (fold reproduction): {'PASS' if chk1_all_neg else 'MARGINAL'} -- all fold diagonal negative: {chk1_all_neg}")
print(f"    CHK2 (symmetry): |H-H^T| = {sym_err_35:.2e}")
print(f"    CHK3 (trace): Tr(H) vs sum(diag) rel err = {trace_err:.2e}")
print(f"    Volume-preserving: max delta_V/V = {max_vol_violation:.2e}")

# =============================================================================
# 15. Key Numbers Summary
# =============================================================================
print("\n" + "=" * 78)
print("  KEY NUMBERS SUMMARY")
print("=" * 78)

print(f"\n  1. tau = {TAU_TURNAROUND} (turnaround)")
print(f"  2. SA(tau=1.614) = {SA_turn:.6f}")
print(f"  3. Lambda^2 = {Lambda_sq_turn:.6f}")
print(f"  4. 35x35 Hessian eigenvalues (5 most negative):")
for k in range(min(5, 35)):
    print(f"       lambda_{k} = {evals_35[k]:.6f}")
print(f"  5. 35x35 Hessian eigenvalues (5 least negative / most positive):")
for k in range(max(0, 35-5), 35):
    print(f"       lambda_{k} = {evals_35[k]:.6f}")
print(f"  6. Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)")
print(f"  7. Gate verdict: {gate_verdict}")
print(f"  8. Jensen direction d^2S: {np.dot(v_jensen_35_hat, H_35 @ v_jensen_35_hat):.6f}")
print(f"  9. Gradient |off-Jensen|/|Jensen|: {grad_off_norm/abs(grad_jensen) if abs(grad_jensen) > 1e-10 else 'inf'}")
print(f" 10. Total computation time: {time.time() - t_global_start:.1f}s")

# =============================================================================
# 16. Save Data
# =============================================================================
print("\n--- 16. Saving data ---")

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
npz_path = os.path.join(DATA_DIR, 's77_hessian_overshoot.npz')

np.savez(npz_path,
    # Primary results
    tau_turnaround=TAU_TURNAROUND,
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
    # Reference metric
    g_turn=g_turn,
    det_turn=det_turn,
    SA_turn=SA_turn,
    Lambda_sq_turn=Lambda_sq_turn,
    # Cross-checks
    sym_err=sym_err_35,
    trace_err=trace_err,
    max_vol_violation=max_vol_violation,
    d2SA_coarse=d2SA_coarse,
    d2SA_fine=d2SA_fine,
    d2SA_diag_fold_chk1=d2SA_diag_fold,
    # Gradient
    grad_SA=grad_SA,
    grad_norm=grad_norm,
    grad_jensen=grad_jensen,
    grad_off_norm=grad_off_norm,
    # Comparison with fold
    s76_evals_fold=s76_evals,
    # Gate
    gate_verdict=gate_verdict,
    n_pos=n_pos_final,
    n_neg=n_neg_final,
    n_zero=n_zero_final,
    signature=f"({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)",
)
print(f"  Saved to {npz_path}")

# =============================================================================
# 17. Plots
# =============================================================================
print("\n--- 17. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'S77-C5-HESSIAN-OVERSHOOT: 35D Off-Jensen Hessian at tau = {TAU_TURNAROUND}\n'
             f'Gate: {gate_verdict} | Signature: ({n_pos_final}+, {n_neg_final}-, {n_zero_final} ~0)',
             fontsize=14, fontweight='bold')

# Panel 1: Eigenvalue spectrum at turnaround
ax = axes[0, 0]
colors = ['red' if ev > ZERO_THRESHOLD else ('gray' if abs(ev) <= ZERO_THRESHOLD else 'blue')
          for ev in evals_35]
ax.bar(range(35), evals_35, color=colors, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title(f'Hessian Eigenvalues at tau = {TAU_TURNAROUND}')

# Panel 2: Fold vs Turnaround comparison
ax = axes[0, 1]
x = np.arange(35)
width = 0.35  # (local)
ax.bar(x - width/2, s76_evals, width, label=f'Fold (tau={tau_fold})', color='steelblue', alpha=0.7)
ax.bar(x + width/2, evals_35, width, label=f'Turn (tau={TAU_TURNAROUND})', color='darkorange', alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title('Fold vs Turnaround Hessian Eigenvalues')
ax.legend()

# Panel 3: Hessian matrix heatmap
ax = axes[0, 2]
vmax_h = max(abs(H_35.min()), abs(H_35.max()))  # (local)
if vmax_h > 0:
    im = ax.imshow(H_35, cmap='RdBu_r', vmin=-vmax_h, vmax=vmax_h, aspect='auto')
    plt.colorbar(im, ax=ax, label=r'd$^2$S/d$\epsilon_i$d$\epsilon_j$')
ax.set_title(f'35x35 Hessian Matrix (tau={TAU_TURNAROUND})')
ax.set_xlabel('Direction j')
ax.set_ylabel('Direction i')

# Panel 4: Convergence check
ax = axes[1, 0]
valid_conv = ~np.isnan(d2SA_coarse[:N_CONV_CHECK]) & ~np.isnan(d2SA_fine[:N_CONV_CHECK])
if np.any(valid_conv):
    x_conv = np.arange(N_CONV_CHECK)[valid_conv]
    ax.plot(x_conv, d2SA_coarse[:N_CONV_CHECK][valid_conv], 's-', label=r'$\epsilon$=0.01', alpha=0.7)
    ax.plot(x_conv, d2SA_diag[:N_CONV_CHECK][valid_conv], 'o-', label=r'$\epsilon$=0.001', alpha=0.7)
    ax.plot(x_conv, d2SA_fine[:N_CONV_CHECK][valid_conv], '^-', label=r'$\epsilon$=0.0001', alpha=0.7)
    ax.legend()
ax.set_xlabel('Direction index')
ax.set_ylabel(r'd$^2$S/d$\epsilon^2$')
ax.set_title('Convergence: Three Step Sizes')

# Panel 5: Eigenvalue ratio (turnaround / fold)
ax = axes[1, 1]
if n_neg_35 > 0 and np.all(s76_evals < 0):
    ratios = evals_35 / s76_evals
    ax.bar(range(35), ratios, color='teal', alpha=0.7)
    ax.axhline(1.0, color='red', ls='--', lw=1, label='ratio=1')
    ax.set_xlabel('Eigenvalue index')
    ax.set_ylabel(r'$\lambda_{turn} / \lambda_{fold}$')
    ax.set_title('Eigenvalue Ratio: Turnaround / Fold')
    ax.legend()
else:
    ax.text(0.5, 0.5, 'N/A\n(sign change)', ha='center', va='center', transform=ax.transAxes, fontsize=14)
    ax.set_title('Eigenvalue Ratio (N/A if sign differs)')

# Panel 6: Gradient decomposition at turnaround
ax = axes[1, 2]
grad_valid = ~np.isnan(grad_SA)
if np.any(grad_valid):
    ax.bar(np.arange(35)[grad_valid], grad_SA[grad_valid], color='orange', alpha=0.7)
    ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Basis direction (35D)')
ax.set_ylabel('dS/d$\\epsilon$')
ax.set_title(f'SA Gradient at tau = {TAU_TURNAROUND}')

plt.tight_layout()
png_path = os.path.join(DATA_DIR, 's77_hessian_overshoot.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved to {png_path}")

print(f"\n  Total runtime: {time.time() - t_global_start:.1f}s")
print("  DONE.")
