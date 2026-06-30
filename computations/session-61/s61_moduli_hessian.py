#!/usr/bin/env python3
"""
s61_moduli_hessian.py — MODULI-HESS-61: 36D Moduli Space Hessian of Spectral Action
=====================================================================================
Gate: MODULI-HESS-61
  PASS: All sampled second derivatives d^2 SA/d epsilon^2 <= 0 (fold is maximum in all 36D)
  FAIL: Any direction gives d^2 SA/d epsilon^2 > 0 (fold is saddle, not maximum)
  INFO: Flat directions found (d^2 SA/d epsilon^2 ~ 0 within numerical noise)

Background:
  S60 HESSIAN-3D-60 found the fold is a MAXIMUM in the 3D Ad(U(2))-invariant subspace
  (all three eigenvalues of H_heat negative: -115960, -3006, -19.2).

  The full moduli space of left-invariant metrics on SU(3) is 36-dimensional:
  an 8x8 positive-definite symmetric matrix g_ab has 36 independent entries.

  NCG constraints reduce this:
    - Volume fixing: det(g) = const removes 1D  =>  35D
    - Ad(U(2)) invariance: reduces to 3D (Jensen + sigma + breathing)

  This script probes the remaining 33 directions OUTSIDE the Ad(U(2)) subspace.

Method:
  1. Build the fold metric g_fold from canonical tau_fold in the Ad(U(2))-invariant form.
  2. Construct a basis for the 36D tangent space Sym(8):
     - 3 on-block directions (U(1), SU(2), C^2 scalings) = Ad(U(2))-invariant
     - 3 on-block off-diagonal within SU(2) and C^2 blocks
     - 30 off-block directions mixing generators between different blocks
  3. For each direction delta_g in Sym(8):
     - Compute SA at g_fold + epsilon * delta_g for epsilon = +/- h
     - Central finite difference: d^2 SA/d epsilon^2 = (SA(+h) - 2*SA(0) + SA(-h)) / h^2
  4. Also sample 20 random directions in Sym(8) for robustness.
  5. Assemble the full 36x36 Hessian from a carefully chosen orthonormal basis.

Key insight from van den Dungen (Paper 01, Theorem 3.14):
  The Kasparov product factorization D_total = D_M x_B D_K means the spectral action
  on the total space depends on D_K through its spectrum on each irrep. The spectrum
  of D_K is a smooth function of the metric g_ab, so the spectral action is smooth on
  Sym_+(8). The Hessian is well-defined everywhere in the interior.

  The block-diagonal structure of D_K under Ad(U(2)) (BLOCK-DIAG-GENERAL-61 PASS)
  means the on-block and off-block sectors decouple at linear order. But the Hessian
  CAN have cross-terms between on-block and off-block directions.

Author: van-den-dungen-bridge-theorist (Session 61, Wave 5)
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from numpy import exp, sqrt, log, pi
from numpy.linalg import eigh, cholesky, inv, norm, eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI, E_B1, E_B2_mean, E_B3_mean,
    S_fold, d2S_fold, a0_fold, a2_fold, a4_fold
)

print("=" * 78)
print("  MODULI-HESS-61: 36D Moduli Space Hessian of Spectral Action")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (from s60_hessian_3d.py)
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
    lam.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3))
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

SU2_IDX = [0, 1, 2]
C2_IDX = [3, 4, 5, 6]
U1_IDX = [7]

# =============================================================================
# 2. Frame, Connection, Dirac Operator
# =============================================================================

def orthonormal_frame(g_s):
    """E such that E g_s E^T = I. E = inv(cholesky(g_s))."""
    L = cholesky(g_s)
    return inv(L)

def frame_structure_constants(f_abc, E):
    """Structure constants in ON frame."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)

def connection_coefficients(ft):
    """Levi-Civita connection: 2*Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}"""
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
    """Omega = (1/4) sum Gamma^b_{ac} gamma_a gamma_b gamma_c"""
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
    dim_total = dim_rho * dim_spin
    D = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(8):
        for b in range(8):
            if abs(E[a,b]) > 1e-15:
                D += E[a,b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    return D

# =============================================================================
# 3. Irrep Construction (from s60_hessian_3d.py)
# =============================================================================

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
        rho_27 = (np.kron(np.kron(X,I3),I3) + np.kron(np.kron(I3,X),I3) + np.kron(np.kron(I3,I3),X))
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
    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-8  # (local)
    groups = []
    for i, ev in enumerate(sorted(zip(evals, range(dim_prod)))):
        val, idx = ev
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

# =============================================================================
# 4. Spectral Action
# =============================================================================

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
# 5. Build Infrastructure
# =============================================================================
print("\n--- 2. Setting up infrastructure ---")

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
total_evals = sum(d*16*d for _,_,d,_ in irreps_data)
for p, q, dim, _ in irreps_data:
    print(f"    ({p},{q}): dim = {dim}, block = {dim*16}")
print(f"  Total eigenvalues per metric point: {total_evals}")

# =============================================================================
# 6. Build Fold Metric and Reference SA
# =============================================================================
print("\n--- 3. Building fold metric ---")

# The Ad(U(2))-invariant metric at the fold:
# g = L1 * |B|_{U(1)} + L2 * |B|_{SU(2)} + L3 * |B|_{C^2}
# At fold (tau = tau_fold, sigma=0, delta_1=0):
#   L1 = exp(2*tau_fold), L2 = exp(-2*tau_fold), L3 = exp(tau_fold)

L1_fold = exp(2.0 * tau_fold)
L2_fold = exp(-2.0 * tau_fold)
L3_fold = exp(tau_fold)

print(f"  L1_fold = {L1_fold:.6f} (U(1) direction)")
print(f"  L2_fold = {L2_fold:.6f} (SU(2) directions)")
print(f"  L3_fold = {L3_fold:.6f} (C^2 directions)")

# Build the fold metric
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

print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  g_fold is diagonal: {np.max(np.abs(g_fold - np.diag(np.diag(g_fold)))):.2e}")
print(f"  det(g_fold): {np.linalg.det(g_fold):.6f}")
print(f"  Eigenvalues of g_fold: {eigvalsh(g_fold)}")

# Reference SA at fold
evals_fold = compute_dirac_eigenvalues(g_fold, gens, f_abc, gammas, irreps_data)
Lambda_sq = 4.0 * np.max(evals_fold**2)  # Same convention as S60
SA_fold = spectral_action_heat(evals_fold, Lambda_sq)

print(f"  Lambda^2 = {Lambda_sq:.4f}")
print(f"  SA at fold = {SA_fold:.6f}")

pos_fold = sorted(evals_fold[evals_fold > 1e-6])
print(f"  Positive eigenvalues at fold: {len(pos_fold)}")
if len(pos_fold) >= 8:
    print(f"    B1: {pos_fold[0]:.6f} (canonical: {E_B1:.6f})")
    print(f"    B2: {pos_fold[1]:.6f}-{pos_fold[4]:.6f} (canonical: {E_B2_mean:.6f})")
    print(f"    B3: {pos_fold[5]:.6f}-{pos_fold[7]:.6f} (canonical: {E_B3_mean:.6f})")

# =============================================================================
# 7. Construct Orthonormal Basis for Sym(8)
# =============================================================================
print("\n--- 4. Constructing basis for Sym(8) [36D tangent space] ---")

# A basis for the 36D space of 8x8 symmetric matrices:
# - 8 diagonal matrices E_{ii} (a=i,b=i)
# - 28 off-diagonal matrices (E_{ij} + E_{ji})/sqrt(2) for i < j

basis_sym8 = []
basis_labels = []

# Diagonal basis elements
for i in range(8):
    M = np.zeros((8,8))
    M[i,i] = 1.0
    basis_sym8.append(M)
    basis_labels.append(f"diag({i})")

# Off-diagonal basis elements
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8,8))
        M[i,j] = 1.0 / sqrt(2.0)
        M[j,i] = 1.0 / sqrt(2.0)
        basis_sym8.append(M)
        basis_labels.append(f"off({i},{j})")

assert len(basis_sym8) == 36, f"Expected 36 basis elements, got {len(basis_sym8)}"
print(f"  Basis size: {len(basis_sym8)} symmetric matrices")

# Classify each basis direction
def classify_direction(label):
    """Classify as on-block (Ad(U(2)) invariant subspace) or off-block."""
    if label.startswith("diag"):
        idx = int(label.split("(")[1].rstrip(")"))
        if idx in U1_IDX:
            return "U1-diag"
        elif idx in SU2_IDX:
            return "SU2-diag"
        elif idx in C2_IDX:
            return "C2-diag"
    elif label.startswith("off"):
        parts = label.split("(")[1].rstrip(")").split(",")
        i, j = int(parts[0]), int(parts[1])
        if i in SU2_IDX and j in SU2_IDX:
            return "SU2-off"
        elif i in C2_IDX and j in C2_IDX:
            return "C2-off"
        elif i in U1_IDX and j in U1_IDX:
            return "U1-off"  # Cannot happen (only 1 U1 index)
        # Cross-block directions
        elif (i in SU2_IDX and j in C2_IDX) or (i in C2_IDX and j in SU2_IDX):
            return "SU2-C2-cross"
        elif (i in U1_IDX and j in SU2_IDX) or (i in SU2_IDX and j in U1_IDX):
            return "U1-SU2-cross"
        elif (i in U1_IDX and j in C2_IDX) or (i in C2_IDX and j in U1_IDX):
            return "U1-C2-cross"
    return "unknown"

# Print classification
class_counts = {}
for k, label in enumerate(basis_labels):
    cls = classify_direction(label)
    if cls not in class_counts:
        class_counts[cls] = 0
    class_counts[cls] += 1

print("\n  Basis classification:")
for cls, count in sorted(class_counts.items()):
    print(f"    {cls}: {count} directions")

# Count on-block vs off-block
on_block_classes = {"U1-diag", "SU2-diag", "C2-diag", "SU2-off", "C2-off"}
cross_block_classes = {"SU2-C2-cross", "U1-SU2-cross", "U1-C2-cross"}

n_on_block = sum(class_counts.get(c, 0) for c in on_block_classes)
n_cross_block = sum(class_counts.get(c, 0) for c in cross_block_classes)
print(f"\n  On-block (Ad(U(2)) subspace + internal): {n_on_block}")
print(f"  Cross-block (new directions): {n_cross_block}")
print(f"  Total: {n_on_block + n_cross_block} (should be 36)")

# =============================================================================
# 8. Compute Directional Second Derivatives
# =============================================================================
print("\n--- 5. Computing directional second derivatives (36 basis + 20 random) ---")

epsilon = 0.005  # Perturbation size
# Smaller epsilon for numerical stability, but big enough that SA changes above noise

# Verify epsilon is small enough that g_fold + eps * delta_g stays positive definite
max_delta_norm = max(np.max(np.abs(M)) for M in basis_sym8)
print(f"  epsilon = {epsilon}")
print(f"  max ||delta_g|| = {max_delta_norm:.4f}")
print(f"  min eigenvalue of g_fold = {eigvalsh(g_fold)[0]:.6f}")

def compute_d2SA_direction(g_base, delta_g, eps, gens, f_abc, gammas, irreps_data, Lambda_sq):
    """
    Compute d^2 SA / d epsilon^2 in direction delta_g at g_base.

    Returns (d2SA, SA_plus, SA_center, SA_minus, pd_check).
    pd_check = True if both perturbed metrics are positive-definite.
    """
    g_plus = g_base + eps * delta_g
    g_minus = g_base - eps * delta_g

    # Check positive-definiteness
    evals_p = eigvalsh(g_plus)
    evals_m = eigvalsh(g_minus)
    pd_check = (np.all(evals_p > 0) and np.all(evals_m > 0))

    if not pd_check:
        return np.nan, np.nan, np.nan, np.nan, False

    # Compute SA at three points
    ev_center = compute_dirac_eigenvalues(g_base, gens, f_abc, gammas, irreps_data)
    SA_center = spectral_action_heat(ev_center, Lambda_sq)

    ev_plus = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
    SA_plus = spectral_action_heat(ev_plus, Lambda_sq)

    ev_minus = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)
    SA_minus = spectral_action_heat(ev_minus, Lambda_sq)

    # Central finite difference
    d2SA = (SA_plus - 2.0 * SA_center + SA_minus) / eps**2

    return d2SA, SA_plus, SA_center, SA_minus, True

# Pre-compute SA at fold (avoid redundant computation)
SA_center_cached = SA_fold

def compute_d2SA_direction_cached(g_base, delta_g, eps, SA_center, gens, f_abc, gammas, irreps_data, Lambda_sq):
    """Same but uses pre-computed SA at center."""
    g_plus = g_base + eps * delta_g
    g_minus = g_base - eps * delta_g

    evals_p = eigvalsh(g_plus)
    evals_m = eigvalsh(g_minus)
    if not (np.all(evals_p > 0) and np.all(evals_m > 0)):
        return np.nan, np.nan, np.nan, False

    ev_plus = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
    SA_plus = spectral_action_heat(ev_plus, Lambda_sq)

    ev_minus = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)
    SA_minus = spectral_action_heat(ev_minus, Lambda_sq)

    d2SA = (SA_plus - 2.0 * SA_center + SA_minus) / eps**2

    return d2SA, SA_plus, SA_minus, True

# Compute for all 36 basis directions
t_basis_start = time.time()
d2SA_basis = np.zeros(36)
SA_plus_basis = np.zeros(36)
SA_minus_basis = np.zeros(36)
pd_check_basis = np.zeros(36, dtype=bool)

for k in range(36):
    d2, sp, sm, pd = compute_d2SA_direction_cached(
        g_fold, basis_sym8[k], epsilon, SA_center_cached,
        gens, f_abc, gammas, irreps_data, Lambda_sq
    )
    d2SA_basis[k] = d2
    SA_plus_basis[k] = sp
    SA_minus_basis[k] = sm
    pd_check_basis[k] = pd

    if (k+1) % 6 == 0 or k == 35:
        elapsed = time.time() - t_basis_start
        print(f"  Basis direction {k+1}/36 done ({elapsed:.1f}s)")

print(f"\n  Basis directions: {np.sum(pd_check_basis)}/36 PD-safe")
n_pd_fail = np.sum(~pd_check_basis)
if n_pd_fail > 0:
    print(f"  WARNING: {n_pd_fail} directions had non-PD perturbed metric")

# Print results for all 36 basis directions
print(f"\n  {'Dir':>4} {'Label':>20} {'Class':>18} {'d2SA':>14} {'Sign':>6}")
print(f"  " + "-"*66)

n_negative = 0
n_positive = 0
n_zero = 0  # (local)
n_nan = 0
zero_threshold = 1.0  # Below this absolute value, treat as zero  # (local)

for k in range(36):
    cls = classify_direction(basis_labels[k])
    d2 = d2SA_basis[k]
    if np.isnan(d2):
        sign_str = "NaN"
        n_nan += 1
    elif abs(d2) < zero_threshold:
        sign_str = "~0"
        n_zero += 1
    elif d2 < 0:
        sign_str = "-"
        n_negative += 1
    else:
        sign_str = "+"
        n_positive += 1
    print(f"  {k:>4} {basis_labels[k]:>20} {cls:>18} {d2:>14.4f} {sign_str:>6}")

print(f"\n  Summary: {n_negative} negative, {n_positive} positive, {n_zero} zero, {n_nan} NaN")

# =============================================================================
# 9. Random Direction Sampling
# =============================================================================
print("\n--- 6. Random direction sampling (20 directions) ---")

np.random.seed(42)  # Reproducibility
n_random = 20
d2SA_random = np.zeros(n_random)
random_dirs = []

for k in range(n_random):
    # Generate random symmetric matrix
    A = np.random.randn(8, 8)
    delta_random = (A + A.T) / 2.0
    # Normalize to unit Frobenius norm
    delta_random /= np.sqrt(np.sum(delta_random**2))
    random_dirs.append(delta_random)

    d2, sp, sm, pd = compute_d2SA_direction_cached(
        g_fold, delta_random, epsilon, SA_center_cached,
        gens, f_abc, gammas, irreps_data, Lambda_sq
    )
    d2SA_random[k] = d2

    if (k+1) % 5 == 0:
        elapsed = time.time() - t_basis_start
        print(f"  Random direction {k+1}/{n_random} done ({elapsed:.1f}s)")

print(f"\n  Random directions d2SA: min = {np.nanmin(d2SA_random):.4f}, "
      f"max = {np.nanmax(d2SA_random):.4f}, mean = {np.nanmean(d2SA_random):.4f}")

n_pos_rand = np.sum(d2SA_random > zero_threshold)
n_neg_rand = np.sum(d2SA_random < -zero_threshold)
n_zero_rand = np.sum(np.abs(d2SA_random) <= zero_threshold)
print(f"  Random: {n_neg_rand} negative, {n_pos_rand} positive, {n_zero_rand} zero")

# =============================================================================
# 10. Assemble Full 36x36 Hessian
# =============================================================================
print("\n--- 7. Assembling full 36x36 Hessian ---")

# The diagonal of the Hessian in the basis {E_k} is just d2SA_basis[k].
# For the full Hessian H_{kl} = d^2 SA / d eps_k d eps_l, we need cross-terms.
# Use: H_{kl} = [SA(+h*E_k+h*E_l) - SA(+h*E_k-h*E_l) - SA(-h*E_k+h*E_l) + SA(-h*E_k-h*E_l)] / (4*h^2)
# This requires 4 * C(36,2) = 4 * 630 = 2520 additional SA evaluations.
# TOO EXPENSIVE for full 36x36.
#
# INSTEAD: Use the BLOCK STRUCTURE.
#
# The key insight from BLOCK-DIAG-GENERAL-61:
# D_K on SU(3) with left-invariant metric is block-diagonal under irrep decomposition.
# The Ad(U(2))-invariant metric preserves the U(2) block structure.
#
# For the Hessian, what matters is: does the spectral action have any positive
# curvature direction? The diagonal d2SA_basis already gives the 36 diagonal
# entries. If ALL are negative, the Hessian is diagonally dominant-negative in
# this basis, which constrains but does not prove all eigenvalues are negative.
#
# EFFICIENT APPROACH: Compute the 36x36 Hessian by decomposing into blocks.
# The cross-block entries can be computed more efficiently by noting:
# H_{kl} = d2SA_basis_combined(E_k + E_l) - d2SA_basis[k] - d2SA_basis[l] for k!=l
# where d2SA_basis_combined is the second derivative along E_k + E_l.
#
# But even this requires 630 more evaluations. Given the S60 computation took
# ~6.5s for 125 points, each evaluation takes ~0.05s, so 2*630 = 1260
# evaluations ~ 63s. Feasible.
#
# MORE EFFICIENT: Use the polarization identity:
# H_{kl} = [d2SA(E_k + E_l) - d2SA(E_k) - d2SA(E_l)] / 2
# where d2SA(V) means the second derivative along direction V, evaluated as:
# d2SA(V) = [SA(g + h*V) - 2*SA(g) + SA(g - h*V)] / h^2
# So H_{kl} requires only ONE additional SA evaluation per off-diagonal pair
# (compute d2SA(E_k + E_l), then use already-known d2SA(E_k), d2SA(E_l)).
# Actually that's still C(36,2) = 630 pairs, each needing 2 SA evals = 1260 evals.
#
# PRACTICAL COMPROMISE: Compute full off-diagonal cross-terms. ~1260 SA evaluations.
# At ~0.05s each, this is ~63s. Acceptable.

print("  Computing full 36x36 Hessian via polarization identity...")
print(f"  Need {36*35//2} off-diagonal pairs, each requiring 2 SA evaluations")
print(f"  Estimated time: ~{36*35//2 * 2 * 0.05:.0f}s")

H_36 = np.zeros((36, 36))

# Fill diagonal from already-computed d2SA_basis
for k in range(36):
    H_36[k, k] = d2SA_basis[k]

# Fill off-diagonal using polarization identity
# d2SA(E_k + E_l) = [SA(g + h*(E_k+E_l)) - 2*SA(g) + SA(g - h*(E_k+E_l))] / h^2
# H_{kl} = [d2SA(E_k + E_l) - d2SA(E_k) - d2SA(E_l)] / 2

t_offdiag_start = time.time()
n_pairs_done = 0
n_pairs_total = 36 * 35 // 2
n_pd_fail_offdiag = 0

for k in range(36):
    for l in range(k+1, 36):
        delta_sum = basis_sym8[k] + basis_sym8[l]
        d2_sum, _, _, pd = compute_d2SA_direction_cached(
            g_fold, delta_sum, epsilon, SA_center_cached,
            gens, f_abc, gammas, irreps_data, Lambda_sq
        )
        if pd and not np.isnan(d2_sum):
            H_36[k, l] = 0.5 * (d2_sum - d2SA_basis[k] - d2SA_basis[l])
            H_36[l, k] = H_36[k, l]
        else:
            H_36[k, l] = 0.0
            H_36[l, k] = 0.0
            n_pd_fail_offdiag += 1

        n_pairs_done += 1
        if n_pairs_done % 100 == 0:
            elapsed = time.time() - t_offdiag_start
            rate = n_pairs_done / elapsed
            remaining = (n_pairs_total - n_pairs_done) / rate if rate > 0 else 0
            print(f"  Pairs: {n_pairs_done}/{n_pairs_total} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_offdiag_end = time.time()
print(f"  Off-diagonal computation: {t_offdiag_end - t_offdiag_start:.1f}s")
if n_pd_fail_offdiag > 0:
    print(f"  WARNING: {n_pd_fail_offdiag} pairs had PD failure")

# Symmetry check
sym_err = np.max(np.abs(H_36 - H_36.T))
print(f"  Symmetry error: {sym_err:.2e}")

# =============================================================================
# 11. Eigenvalue Decomposition of Full 36x36 Hessian
# =============================================================================
print("\n--- 8. Eigenvalue decomposition of 36x36 Hessian ---")

evals_36, evecs_36 = eigh(H_36)

print(f"\n  All 36 eigenvalues:")
for k in range(36):
    sign = "+" if evals_36[k] > zero_threshold else ("-" if evals_36[k] < -zero_threshold else "~0")
    print(f"    lambda_{k:>2} = {evals_36[k]:>14.4f}  {sign}")

n_pos_36 = np.sum(evals_36 > zero_threshold)
n_neg_36 = np.sum(evals_36 < -zero_threshold)
n_zero_36 = np.sum(np.abs(evals_36) <= zero_threshold)

print(f"\n  Signature: ({n_pos_36}+, {n_neg_36}-, {n_zero_36} ~0)")
print(f"  Largest eigenvalue: {evals_36[-1]:.4f}")
print(f"  Smallest eigenvalue: {evals_36[0]:.4f}")
print(f"  Condition number: {abs(evals_36[-1]) / (abs(evals_36[0]) + 1e-30):.2f}")

# =============================================================================
# 12. Analyze Eigenvector Structure
# =============================================================================
print("\n--- 9. Eigenvector structure analysis ---")

# For each eigenvalue, show its projection onto on-block vs cross-block
on_block_indices = []
cross_block_indices = []
for k, label in enumerate(basis_labels):
    cls = classify_direction(label)
    if cls in on_block_classes:
        on_block_indices.append(k)
    elif cls in cross_block_classes:
        cross_block_indices.append(k)

on_block_indices = np.array(on_block_indices)
cross_block_indices = np.array(cross_block_indices)

print(f"  On-block indices: {len(on_block_indices)} directions")
print(f"  Cross-block indices: {len(cross_block_indices)} directions")

# Show the 5 most extreme eigenvalues
print(f"\n  5 most negative eigenvalues:")
for k in range(min(5, len(evals_36))):
    v = evecs_36[:, k]
    on_weight = np.sum(v[on_block_indices]**2)
    cross_weight = np.sum(v[cross_block_indices]**2)
    print(f"    lambda_{k} = {evals_36[k]:>14.4f}: "
          f"on-block = {on_weight:.4f}, cross-block = {cross_weight:.4f}")

if n_pos_36 > 0:
    print(f"\n  Positive eigenvalues (SADDLE DIRECTIONS):")
    for k in range(36):
        if evals_36[k] > zero_threshold:
            v = evecs_36[:, k]
            on_weight = np.sum(v[on_block_indices]**2)
            cross_weight = np.sum(v[cross_block_indices]**2)
            # Find top 3 contributing basis elements
            top3 = np.argsort(np.abs(v))[-3:][::-1]
            top3_str = ", ".join(f"{basis_labels[j]}({v[j]:.3f})" for j in top3)
            print(f"    lambda_{k} = {evals_36[k]:>14.4f}: "
                  f"on-block = {on_weight:.4f}, cross-block = {cross_weight:.4f}")
            print(f"      top components: {top3_str}")

# =============================================================================
# 13. Richardson Extrapolation Cross-Check
# =============================================================================
print("\n--- 10. Richardson extrapolation cross-check ---")

# Compute a few diagonal elements at half-step to verify convergence
eps_half = epsilon / 2.0
n_rich_check = min(10, 36)
d2SA_half = np.zeros(n_rich_check)

for k in range(n_rich_check):
    d2h, _, _, pd = compute_d2SA_direction_cached(
        g_fold, basis_sym8[k], eps_half, SA_center_cached,
        gens, f_abc, gammas, irreps_data, Lambda_sq
    )
    d2SA_half[k] = d2h if pd else np.nan

# Richardson extrapolation: H_rich = (4*H_half - H_full) / 3
d2SA_rich = (4.0 * d2SA_half - d2SA_basis[:n_rich_check]) / 3.0

print(f"  {'Dir':>4} {'d2SA(h)':>14} {'d2SA(h/2)':>14} {'Richardson':>14} {'rel_diff':>10}")
for k in range(n_rich_check):
    if not np.isnan(d2SA_half[k]) and abs(d2SA_basis[k]) > 1e-10:
        rel = abs(d2SA_rich[k] - d2SA_basis[k]) / abs(d2SA_basis[k])
    else:
        rel = np.nan
    print(f"  {k:>4} {d2SA_basis[k]:>14.4f} {d2SA_half[k]:>14.4f} {d2SA_rich[k]:>14.4f} {rel:>10.6f}")

# =============================================================================
# 14. Cross-check: 3D subblock vs S60
# =============================================================================
print("\n--- 11. Cross-check: 3D subblock vs S60 ---")

# The Ad(U(2))-invariant directions correspond to specific linear combinations
# of the diagonal basis elements:
# tau direction: d/dtau (L1=e^{2tau}, L2=e^{-2tau}, L3=e^tau)
#   dg/dtau = 2*L1*diag(U1) - 2*L2*diag(SU2) + L3*diag(C2)
# This mixes diagonal(7), diagonal(0,1,2), diagonal(3,4,5,6)

# Load S60 data for comparison
try:
    s60_data = np.load('computations/session-60/s60_hessian_3d.npz', allow_pickle=True)
    print(f"  S60 heat kernel eigenvalues: {s60_data['evals_heat']}")
    print(f"  S60 gate verdict: {s60_data['gate_verdict']}")

    # Extract 3D subblock from our 36x36 Hessian
    # The tau, sigma, delta_1 directions in the 36D basis:
    #
    # tau direction: dg/dtau = 2*L1*g0_{77}*E_77 + (-2)*L2*g0_{ii}*sum(E_ii for i in SU2)
    #                        + L3*g0_{jj}*sum(E_jj for j in C2)
    # In our basis: E_77 is basis element 7 (diag(7)),
    #   E_00,E_11,E_22 are basis 0,1,2, E_33,...,E_66 are basis 3,4,5,6
    #
    # sigma direction: similarly from the sigma parametrization
    # delta_1 direction: breathing mode = sum of all diag * appropriate weights

    # Construct the 3 tangent vectors in 36D basis coordinates
    # dg/dtau at fold: L1' = 2*L1, L2' = -2*L2, L3' = L3
    v_tau = np.zeros(36)
    for a in U1_IDX:
        v_tau[a] = 2.0 * L1_fold * g0[a,a]
    for a in SU2_IDX:
        v_tau[a] = -2.0 * L2_fold * g0[a,a]
    for a in C2_IDX:
        v_tau[a] = L3_fold * g0[a,a]

    # dg/dsigma: L1 -> (-11)*L1, L2 -> (-7)*L2, L3 -> 8*L3
    v_sigma = np.zeros(36)
    for a in U1_IDX:
        v_sigma[a] = -11.0 * L1_fold * g0[a,a]
    for a in SU2_IDX:
        v_sigma[a] = -7.0 * L2_fold * g0[a,a]
    for a in C2_IDX:
        v_sigma[a] = 8.0 * L3_fold * g0[a,a]

    # dg/ddelta_1: L1 -> L1, L2 -> 0, L3 -> 0
    v_d1 = np.zeros(36)
    for a in U1_IDX:
        v_d1[a] = L1_fold * g0[a,a]

    # Project 36x36 Hessian onto the 3D subspace
    V_3d = np.column_stack([v_tau, v_sigma, v_d1])  # 36 x 3
    H_3d_proj = V_3d.T @ H_36 @ V_3d  # 3 x 3

    evals_3d_proj, evecs_3d_proj = eigh(H_3d_proj)

    print(f"\n  3D projected Hessian eigenvalues: {evals_3d_proj}")
    print(f"  S60 Hessian eigenvalues: {s60_data['evals_heat']}")

    # The eigenvalue RATIOS should match (absolute scale depends on parametrization)
    if abs(evals_3d_proj[0]) > 1e-10 and abs(s60_data['evals_heat'][0]) > 1e-10:
        ratio_proj = evals_3d_proj / evals_3d_proj[0]
        ratio_s60 = s60_data['evals_heat'] / s60_data['evals_heat'][0]
        print(f"  Normalized ratios (proj): {ratio_proj}")
        print(f"  Normalized ratios (S60):  {ratio_s60}")

except Exception as e:
    print(f"  Could not cross-check with S60: {e}")

# =============================================================================
# 15. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: MODULI-HESS-61")
print("=" * 78)

all_d2SA = np.concatenate([d2SA_basis[pd_check_basis], d2SA_random])

max_d2SA = np.nanmax(all_d2SA)
min_d2SA = np.nanmin(all_d2SA)

print(f"\n  Full 36x36 Hessian eigenvalues:")
print(f"    Most negative: {evals_36[0]:.4f}")
print(f"    Most positive: {evals_36[-1]:.4f}")
print(f"    Positive eigenvalues: {n_pos_36}")
print(f"    Negative eigenvalues: {n_neg_36}")
print(f"    Near-zero eigenvalues: {n_zero_36}")

print(f"\n  Random direction check:")
print(f"    All {n_random} random d2SA values: min = {np.nanmin(d2SA_random):.4f}, max = {np.nanmax(d2SA_random):.4f}")
print(f"    Random positive: {n_pos_rand}, negative: {n_neg_rand}")

# Gate decision
if n_pos_36 > 0:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: **FAIL**")
    print(f"  {n_pos_36} positive eigenvalue(s) in 36x36 Hessian.")
    print(f"  The fold is a SADDLE POINT in the full 36D moduli space.")
    print(f"  Maximum eigenvalue: {evals_36[-1]:.4f}")

    # Identify the positive-eigenvalue directions
    for k in range(36):
        if evals_36[k] > zero_threshold:
            v = evecs_36[:, k]
            top5 = np.argsort(np.abs(v))[-5:][::-1]
            top5_str = ", ".join(f"{basis_labels[j]}({v[j]:+.3f})" for j in top5)
            print(f"\n  Positive direction lambda_{k} = {evals_36[k]:.4f}:")
            print(f"    top components: {top5_str}")

elif n_zero_36 > 0 and n_neg_36 + n_zero_36 == 36:
    gate_verdict = "INFO"
    print(f"\n  VERDICT: **INFO**")
    print(f"  All eigenvalues non-positive, but {n_zero_36} near-zero.")
    print(f"  Fold is a maximum with {n_zero_36} flat direction(s).")

    # Identify flat directions
    for k in range(36):
        if abs(evals_36[k]) <= zero_threshold:
            v = evecs_36[:, k]
            top3 = np.argsort(np.abs(v))[-3:][::-1]
            top3_str = ", ".join(f"{basis_labels[j]}({v[j]:+.3f})" for j in top3)
            print(f"    Flat direction lambda_{k} = {evals_36[k]:.4f}: {top3_str}")

else:
    gate_verdict = "PASS"
    print(f"\n  VERDICT: **PASS**")
    print(f"  All 36 eigenvalues negative (no flat or positive directions).")
    print(f"  The fold is a strict LOCAL MAXIMUM of SA in the full 36D moduli space.")
    print(f"  Most negative: {evals_36[0]:.4f}")
    print(f"  Least negative: {evals_36[-1]:.4f}")

# =============================================================================
# 16. Key Numbers Summary
# =============================================================================
print("\n" + "=" * 78)
print("  KEY NUMBERS SUMMARY")
print("=" * 78)

print(f"\n  1. 36x36 Hessian eigenvalues (5 most negative):")
for k in range(min(5,36)):
    print(f"       lambda_{k} = {evals_36[k]:.4f}")
print(f"  2. 36x36 Hessian eigenvalues (5 least negative / most positive):")
for k in range(max(0,36-5), 36):
    print(f"       lambda_{k} = {evals_36[k]:.4f}")
print(f"  3. Signature: ({n_pos_36}+, {n_neg_36}-, {n_zero_36} ~0)")
print(f"  4. Gate verdict: {gate_verdict}")
print(f"  5. Basis directions: {n_negative} neg, {n_positive} pos, {n_zero} ~0")
print(f"  6. Random directions (20): {n_neg_rand} neg, {n_pos_rand} pos, {n_zero_rand} ~0")
print(f"  7. S60 consistency: 3D subblock eigenvalue ratios compared above")
print(f"  8. Richardson convergence: checked on {n_rich_check} directions")
print(f"  9. Total SA evaluations: {2*36 + 2*n_random + 2*n_pairs_total + 2*n_rich_check}")
print(f" 10. Total computation time: {time.time() - t_global_start:.1f}s")

# =============================================================================
# 17. Plots
# =============================================================================
print("\n--- 12. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'MODULI-HESS-61: 36D Moduli Space Hessian\n'
             f'Gate: {gate_verdict} | Signature: ({n_pos_36}+, {n_neg_36}-, {n_zero_36} ~0)',
             fontsize=14, fontweight='bold')

# Plot 1: Eigenvalue spectrum of 36x36 Hessian
ax = axes[0, 0]
colors = ['red' if ev > zero_threshold else ('gray' if abs(ev) <= zero_threshold else 'blue')
          for ev in evals_36]
ax.bar(range(36), evals_36, color=colors, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.axhline(zero_threshold, color='orange', ls='--', alpha=0.5, label=f'threshold={zero_threshold}')
ax.axhline(-zero_threshold, color='orange', ls='--', alpha=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue')
ax.set_title('36x36 Hessian eigenvalues')
ax.legend()

# Plot 2: d2SA for all 36 basis directions, colored by type
ax = axes[0, 1]
on_block_mask = np.array([classify_direction(l) in on_block_classes for l in basis_labels])
cross_block_mask = ~on_block_mask
ax.bar(np.where(on_block_mask)[0], d2SA_basis[on_block_mask], color='blue', alpha=0.7, label='on-block')
ax.bar(np.where(cross_block_mask)[0], d2SA_basis[cross_block_mask], color='red', alpha=0.7, label='cross-block')
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Basis direction index')
ax.set_ylabel('d^2 SA / d epsilon^2')
ax.set_title('Directional second derivatives')
ax.legend()

# Plot 3: Hessian matrix heatmap
ax = axes[0, 2]
vmax = np.max(np.abs(H_36))
im = ax.imshow(H_36, cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='equal')
ax.set_xlabel('Basis index')
ax.set_ylabel('Basis index')
ax.set_title('36x36 Hessian matrix')
fig.colorbar(im, ax=ax, shrink=0.8)

# Plot 4: Eigenvector composition (on-block vs cross-block weight)
ax = axes[1, 0]
on_weights = np.array([np.sum(evecs_36[on_block_indices, k]**2) for k in range(36)])
cross_weights = np.array([np.sum(evecs_36[cross_block_indices, k]**2) for k in range(36)])
ax.bar(range(36), on_weights, color='blue', alpha=0.7, label='on-block')
ax.bar(range(36), cross_weights, bottom=on_weights, color='red', alpha=0.7, label='cross-block')
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Weight')
ax.set_title('Eigenvector on-block vs cross-block weight')
ax.legend()

# Plot 5: Random directions histogram
ax = axes[1, 1]
ax.hist(d2SA_random, bins=10, color='green', alpha=0.7, edgecolor='black')
ax.axvline(0, color='red', ls='--')
ax.set_xlabel('d^2 SA / d epsilon^2')
ax.set_ylabel('Count')
ax.set_title(f'Random direction d2SA ({n_random} samples)')

# Plot 6: Eigenvalue distribution (log scale of |eigenvalue|)
ax = axes[1, 2]
abs_evals = np.abs(evals_36)
abs_evals_nonzero = abs_evals[abs_evals > 1e-10]
ax.semilogy(range(len(abs_evals_nonzero)), sorted(abs_evals_nonzero, reverse=True), 'ko-', markersize=4)
ax.set_xlabel('Rank')
ax.set_ylabel('|eigenvalue|')
ax.set_title('Eigenvalue magnitudes (log scale)')

plt.tight_layout()
plt.savefig('computations/session-61/s61_moduli_hessian.png', dpi=150, bbox_inches='tight')
print("  Saved: computations/session-61/s61_moduli_hessian.png")

# =============================================================================
# 18. Save Data
# =============================================================================
print("\n--- 13. Saving data ---")

np.savez('computations/session-61/s61_moduli_hessian.npz',
    # Full 36x36 Hessian
    H_36=H_36,
    evals_36=evals_36,
    evecs_36=evecs_36,

    # Basis direction second derivatives
    d2SA_basis=d2SA_basis,
    SA_plus_basis=SA_plus_basis,
    SA_minus_basis=SA_minus_basis,
    pd_check_basis=pd_check_basis,
    basis_labels=np.array(basis_labels),

    # Random direction results
    d2SA_random=d2SA_random,
    n_random=n_random,

    # Richardson check
    d2SA_half=d2SA_half,
    d2SA_rich=d2SA_rich,

    # Parameters
    epsilon=epsilon,
    Lambda_sq=Lambda_sq,
    SA_fold=SA_fold,
    tau_fold=tau_fold,

    # Fold metric
    g_fold=g_fold,
    evals_fold=evals_fold,

    # Gate verdict
    gate_verdict=gate_verdict,
    n_pos_36=n_pos_36,
    n_neg_36=n_neg_36,
    n_zero_36=n_zero_36,
    signature=np.array([n_pos_36, n_neg_36, n_zero_36]),

    # Metadata
    total_computation_time=time.time() - t_global_start,
    total_SA_evaluations=2*36 + 2*n_random + 2*n_pairs_total + 2*n_rich_check,
)

print("  Saved: computations/session-61/s61_moduli_hessian.npz")

t_total = time.time() - t_global_start
print(f"\n  Total wall time: {t_total:.1f}s")
print("\n" + "=" * 78)
print("  MODULI-HESS-61 COMPLETE")
print("=" * 78)
