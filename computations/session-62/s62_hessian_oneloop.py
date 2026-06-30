#!/usr/bin/env python3
"""
s62_hessian_oneloop.py — HESSIAN-ONELOOP-62: One-Loop Corrected Hessian
=========================================================================
Gate: HESSIAN-ONELOOP-62
  PASS if >= 4 eigenvalues flip positive AND those 4 correspond to U(2) gauge directions.
  FAIL if 0 flip positive.
  INFO if 1-3 flip positive or the flipped directions do not match gauge.

Background:
  S61 MODULI-HESS-61 found ALL 36 eigenvalues of the tree-level Hessian negative.
  The spectral action at tree level is S_b[g] = Tr f(D_K^2 / Lambda^2).

  The one-loop effective action adds quantum corrections:
    S_eff = S_b + (1/2) Tr ln(D_K^2)
          = S_b + (1/2) sum_n ln(lambda_n^2)

  The one-loop Hessian correction in the moduli space eigenbasis {e_a}:
    H_1loop[a,b] = (1/2) sum_n [
        (1/lambda_n^2) * (d^2 lambda_n^2 / d e_a d e_b)
        - (1/lambda_n^4) * (d lambda_n^2 / d e_a) * (d lambda_n^2 / d e_b)
    ]

  This is computed via finite differences of the D_K eigenvalues at perturbed metrics.

Method:
  1. Load tree-level Hessian H_tree, eigenvalues, eigenvectors from S61.
  2. For each of the 36 moduli eigenvectors e_a, perturb:
       g -> g + eps * sum_k (e_a)_k * basis_k
     and recompute D_K eigenvalues.
  3. Compute d(lambda_n^2)/d(e_a) and d^2(lambda_n^2)/d(e_a)d(e_b) by finite differences.
  4. Assemble H_1loop and form H_eff = H_tree + H_1loop.
  5. Diagonalize H_eff and identify sign flips.
  6. Identify U(2) gauge directions and check overlap.

Key physical expectation:
  Gauge directions (U(2) right-translations acting by conjugation on the metric)
  should be FLAT at tree level (spectral action is gauge-invariant) but may acquire
  curvature at one-loop from the functional determinant. If the gauge-fixing ghost
  contributions are included, these directions should become positive (the Faddeev-Popov
  mechanism lifts flat gauge directions into positive modes).

Author: quantum-acoustics-theorist (Session 62, Wave 1)
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
print("  HESSIAN-ONELOOP-62: One-Loop Corrected Hessian of Spectral Action")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (reused from S61)
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
    """Anti-Hermitian generators e_a = -i/2 * lambda_a."""
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
U2_IDX = [0, 1, 2, 7]  # U(2) = SU(2) x U(1) gauge directions

# =============================================================================
# 2. Frame, Connection, Dirac Operator (from S61)
# =============================================================================

def orthonormal_frame(g_s):
    """E such that E g_s E^T = I."""
    L = cholesky(g_s)
    return inv(L)

def frame_structure_constants(f_abc, E):
    """Structure constants in ON frame."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)

def connection_coefficients(ft):
    """Levi-Civita connection in ON frame."""
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
# 3. Irrep Construction (from S61)
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
# 4. Spectral Action and Eigenvalue Computation
# =============================================================================

def spectral_action_heat(eigenvalues, Lambda_sq):
    """S = sum_n exp(-lambda_n^2 / Lambda^2)"""
    lam_sq = eigenvalues**2
    return np.sum(np.exp(-lam_sq / Lambda_sq))

def compute_dirac_eigenvalues(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute all D_K eigenvalues for a given 8x8 metric.
    Returns eigenvalues of -i*D_K (real, from Hermitian iD)."""
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

def compute_dirac_eigenvalues_sorted_sq(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute D_K eigenvalues and return lambda_n^2, sorted by |lambda|.
    Also returns the raw eigenvalues for cross-checking."""
    evals = compute_dirac_eigenvalues(g_metric, gens, f_abc, gammas, irreps_data)
    return evals, evals**2

# =============================================================================
# 5. Build Infrastructure
# =============================================================================
print("\n--- 2. Setting up infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
gammas = build_cliff8()

# Validate
cliff_err = 0.0  # (local)
for a in range(8):
    for b in range(8):
        ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(16)
        cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
print(f"  Clifford algebra error: {cliff_err:.2e}")

# Build irreps (same as S61: max_pq_sum=3)
print("  Building irreps (max p+q = 3)...")
irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3)
total_evals = sum(d*16*d for _,_,d,_ in irreps_data)
for p, q, dim, _ in irreps_data:
    print(f"    ({p},{q}): dim = {dim}, block = {dim*16}")
print(f"  Total eigenvalues per metric point: {total_evals}")

# =============================================================================
# 6. Load Tree-Level Hessian Data from S61
# =============================================================================
print("\n--- 3. Loading S61 tree-level Hessian data ---")

s61_data = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                's61_moduli_hessian.npz'), allow_pickle=True)

H_tree = s61_data['H_36']
evals_tree = s61_data['evals_36']
evecs_tree = s61_data['evecs_36']
g_fold = s61_data['g_fold']
evals_fold_stored = s61_data['evals_fold']
Lambda_sq = s61_data['Lambda_sq']
SA_fold_stored = s61_data['SA_fold']
basis_labels = list(s61_data['basis_labels'])
epsilon_s61 = float(s61_data['epsilon'])

print(f"  H_tree shape: {H_tree.shape}")
print(f"  Tree-level eigenvalues: min={evals_tree[0]:.4f}, max={evals_tree[-1]:.4f}")
print(f"  All negative: {np.all(evals_tree < 0)}")
print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  D_K eigenvalues at fold: {len(evals_fold_stored)} total")
print(f"  Lambda^2: {Lambda_sq:.6f}")
print(f"  SA at fold: {SA_fold_stored:.6f}")

# =============================================================================
# 7. Reconstruct Basis for Sym(8)
# =============================================================================
print("\n--- 4. Reconstructing Sym(8) basis ---")

basis_sym8 = []
# Diagonal
for i in range(8):
    M = np.zeros((8,8))
    M[i,i] = 1.0
    basis_sym8.append(M)
# Off-diagonal
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8,8))
        M[i,j] = 1.0 / sqrt(2.0)
        M[j,i] = 1.0 / sqrt(2.0)
        basis_sym8.append(M)

assert len(basis_sym8) == 36

# Verify fold eigenvalues match
evals_fold_verify = compute_dirac_eigenvalues(g_fold, gens, f_abc, gammas, irreps_data)
max_diff = np.max(np.abs(np.sort(evals_fold_verify) - np.sort(evals_fold_stored)))
print(f"  Eigenvalue reproduction check: max|diff| = {max_diff:.2e}")

# =============================================================================
# 8. Construct U(2) Gauge Directions in the Moduli Space
# =============================================================================
print("\n--- 5. Identifying U(2) gauge directions ---")

# On the space of left-invariant metrics Met(SU(3)), the diffeomorphism group acts.
# For LEFT-invariant metrics, the relevant gauge equivalences come from
# INNER automorphisms: g_ab -> (Ad_h)_a^c (Ad_h)_b^d g_cd for h in SU(3).
#
# The infinitesimal version: for X in su(3),
#   delta_X g_ab = f_{ac}^d X_c g_db + f_{bc}^d X_c g_ad
#   (this is the Lie derivative of g along the right-invariant vector field
#    generated by X, acting on the left-invariant metric)
#
# The U(2) subgroup preserves the block structure: Ad(U(2)) maps the Jensen
# curve to itself. So U(2) gauge directions are TANGENT to the orbits of
# the Ad(U(2)) action on Met(SU(3)).
#
# At the fold metric g_fold (which is Ad(U(2))-invariant), the U(2) gauge
# directions are:
#   delta_X g = [ad_X, g]  (in matrix form)
# where ad_X is the adjoint representation matrix.
#
# For X = e_alpha (alpha in U2_IDX = {0,1,2,7}):
#   (delta_{e_alpha} g)_{ab} = sum_c f_{alpha,a,c} g_{cb} + sum_c f_{alpha,b,c} g_{ac}
#
# These generate tangent vectors to the gauge orbit. At a U(2)-invariant point,
# these tangent vectors live in the off-block directions (mixing different blocks).

def gauge_tangent_vector(alpha, g_metric, f_abc):
    """Compute the tangent vector delta g from the infinitesimal Ad action of e_alpha.
    (delta g)_{ab} = f_{alpha,a,c} g_{cb} + f_{alpha,b,c} g_{ac}"""
    n = g_metric.shape[0]
    delta_g = np.zeros((n, n), dtype=np.float64)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                delta_g[a,b] += f_abc[alpha, a, c] * g_metric[c, b]
                delta_g[a,b] += f_abc[alpha, b, c] * g_metric[a, c]
    # Symmetrize (should already be symmetric, but enforce)
    delta_g = 0.5 * (delta_g + delta_g.T)
    return delta_g

# Compute gauge tangent vectors for all 4 U(2) generators
gauge_directions_8x8 = []
gauge_labels = []
for alpha in U2_IDX:
    dg = gauge_tangent_vector(alpha, g_fold, f_abc)
    gauge_directions_8x8.append(dg)
    gauge_labels.append(f"Ad(e_{alpha})")
    norm_dg = np.sqrt(np.sum(dg**2))
    print(f"  Gauge direction Ad(e_{alpha}): ||delta_g|| = {norm_dg:.6f}")

# Express gauge directions in the Sym(8) basis
def express_in_basis(M, basis):
    """Express an 8x8 symmetric matrix in the basis {basis_k}."""
    coeffs = np.zeros(len(basis))
    for k, B in enumerate(basis):
        coeffs[k] = np.sum(M * B)  # Frobenius inner product
    return coeffs

gauge_directions_36 = []
for k, dg in enumerate(gauge_directions_8x8):
    c = express_in_basis(dg, basis_sym8)  # (local)
    norm_c = np.sqrt(np.sum(c**2))
    if norm_c > 1e-10:
        c_normalized = c / norm_c
    else:
        c_normalized = c
        print(f"  WARNING: Gauge direction {gauge_labels[k]} has zero norm in basis!")
    gauge_directions_36.append(c_normalized)
    # Verify reconstruction
    M_reconstructed = sum(c[j] * basis_sym8[j] for j in range(36))
    recon_err = np.max(np.abs(M_reconstructed - dg))
    print(f"    -> 36D coefficients norm = {norm_c:.6f}, reconstruction error = {recon_err:.2e}")

# Compute overlap of gauge directions with tree-level Hessian eigenvectors
print("\n  Gauge direction overlap with tree-level Hessian eigenvectors:")
gauge_overlaps_tree = np.zeros((4, 36))
for g_idx in range(4):
    for e_idx in range(36):
        gauge_overlaps_tree[g_idx, e_idx] = abs(np.dot(gauge_directions_36[g_idx], evecs_tree[:, e_idx]))

for g_idx in range(4):
    top3 = np.argsort(gauge_overlaps_tree[g_idx])[-3:][::-1]
    print(f"  {gauge_labels[g_idx]}: top overlaps with eigvec "
          f"#{top3[0]}({gauge_overlaps_tree[g_idx,top3[0]]:.4f}), "
          f"#{top3[1]}({gauge_overlaps_tree[g_idx,top3[1]]:.4f}), "
          f"#{top3[2]}({gauge_overlaps_tree[g_idx,top3[2]]:.4f})")

# =============================================================================
# 9. Compute One-Loop Hessian via Eigenvalue Finite Differences
# =============================================================================
print("\n--- 6. Computing one-loop Hessian correction ---")

# Strategy: Work in the tree-level Hessian eigenbasis {v_a = evecs_tree[:, a]}.
# For each direction v_a, perturb the metric:
#   g(eps) = g_fold + eps * Delta_a
# where Delta_a = sum_k (v_a)_k * basis_sym8[k] is the 8x8 perturbation.
#
# Then compute eigenvalues lambda_n(+eps), lambda_n(-eps), lambda_n(0).
# The one-loop effective action is S_1loop = (1/2) sum_n ln(lambda_n^2).
# Its Hessian in direction a is:
#   d^2 S_1loop / d eps_a^2 = (1/2) sum_n d^2/deps^2 [ln(lambda_n^2)]
#     = (1/2) sum_n [ (1/lambda_n^2)(d^2 lambda_n^2/deps^2) - (1/lambda_n^4)(d lambda_n^2/deps)^2 ]
#
# For the off-diagonal:
#   d^2 S_1loop / d eps_a d eps_b = (1/2) sum_n [
#     (1/lambda_n^2)(d^2 lambda_n^2 / d eps_a d eps_b)
#     - (1/lambda_n^4)(d lambda_n^2 / d eps_a)(d lambda_n^2 / d eps_b)
#   ]
#
# The finite difference approach:
# 1. Eigenvalues at g_fold (center): lambda_n(0)
# 2. Eigenvalues at g_fold + eps * Delta_a: lambda_n(+eps_a)
# 3. Eigenvalues at g_fold - eps * Delta_a: lambda_n(-eps_a)
# 4. First derivative: d(lambda_n^2)/d(eps_a) = [lambda_n^2(+eps) - lambda_n^2(-eps)] / (2*eps)
# 5. Second derivative: d^2(lambda_n^2)/d(eps_a)^2 = [lambda_n^2(+) - 2*lambda_n^2(0) + lambda_n^2(-)] / eps^2
# 6. Cross-derivative: d^2/d(eps_a)d(eps_b) via:
#    [lambda_n^2(+a,+b) - lambda_n^2(+a,-b) - lambda_n^2(-a,+b) + lambda_n^2(-a,-b)] / (4 eps^2)
#
# For off-diagonal, I'll use the polarization identity to save evaluations:
#   d^2 S / deps_a deps_b = (1/2) [d^2 S/d(eps_a+eps_b)^2 - d^2 S/deps_a^2 - d^2 S/deps_b^2]

eps = 0.001  # Perturbation size (smaller than S61's 0.005 for higher accuracy)
print(f"  Perturbation epsilon = {eps}")

# First: compute eigenvalues at center point
evals_center = compute_dirac_eigenvalues(g_fold, gens, f_abc, gammas, irreps_data)
lam_sq_center = evals_center**2
N_evals = len(evals_center)
print(f"  Number of D_K eigenvalues: {N_evals}")

# Remove zero eigenvalues from the one-loop sum (they diverge in ln)
# Zero eigenvalues of D_K correspond to zero modes (kernel of D_K)
zero_mask = np.abs(evals_center) < 1e-12
n_zero_modes = np.sum(zero_mask)
nonzero_mask = ~zero_mask
n_nonzero = np.sum(nonzero_mask)
print(f"  Zero modes: {n_zero_modes}")
print(f"  Non-zero modes (used in one-loop): {n_nonzero}")

# Construct the 36 perturbation directions in 8x8 matrix form
# Working in the tree-level eigenbasis
perturbation_matrices = []
for a in range(36):
    Delta_a = np.zeros((8, 8))
    for k in range(36):
        Delta_a += evecs_tree[k, a] * basis_sym8[k]
    perturbation_matrices.append(Delta_a)

# Verify perturbation matrices preserve symmetry and maintain positive definiteness
print("  Checking perturbation matrices...")
for a in range(36):
    sym_err = np.max(np.abs(perturbation_matrices[a] - perturbation_matrices[a].T))
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]
    evals_gp = eigvalsh(g_plus)
    evals_gm = eigvalsh(g_minus)
    if evals_gp[0] < 0 or evals_gm[0] < 0:
        print(f"  WARNING: Direction {a} breaks positive definiteness!")
        print(f"    g_plus min eval: {evals_gp[0]:.6f}")
        print(f"    g_minus min eval: {evals_gm[0]:.6f}")
print("  All perturbation matrices checked.")

# =============================================================================
# 10. Eigenvalue Tracking: Handle Level Crossings
# =============================================================================
# CRITICAL: Eigenvalues can cross as the metric is perturbed. Simple sorting
# will mislabel eigenvalues after crossings. For the one-loop sum, however,
# we only need sum_n terms, so the TOTAL sum is invariant under relabeling.
# We do NOT need to track individual eigenvalues -- the sum is over ALL n.
#
# This is because:
#   sum_n (1/lambda_n^2) * d^2(lambda_n^2)/deps^2 = d^2/deps^2 [sum_n ln(lambda_n^2)]
# and the sum sum_n ln(lambda_n^2) = ln det(D_K^2), which is smooth in the metric
# and does NOT require tracking individual eigenvalues.
#
# Strategy: compute the one-loop action S_1loop(eps) = (1/2) sum_n ln(lambda_n^2(eps))
# directly, then take numerical second derivatives of the TOTAL.
# This avoids eigenvalue tracking entirely.

print("\n--- 7. Computing one-loop effective action along all 36 directions ---")

def oneloop_action(evals):
    """S_1loop = (1/2) sum_{n: lambda_n != 0} ln(lambda_n^2)"""
    lam_sq = evals**2
    mask = lam_sq > 1e-24  # Skip exact zeros
    return 0.5 * np.sum(np.log(lam_sq[mask]))

S1_center = oneloop_action(evals_center)
print(f"  S_1loop at center: {S1_center:.6f}")

# Compute S_1loop at +/- epsilon for all 36 eigendirections
t_evals_start = time.time()
S1_plus = np.zeros(36)
S1_minus = np.zeros(36)

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    ev_plus = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
    ev_minus = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)

    S1_plus[a] = oneloop_action(ev_plus)
    S1_minus[a] = oneloop_action(ev_minus)

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_evals_start
        rate = (a+1) / elapsed if elapsed > 0 else 0
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"  Direction {a+1}/36 done ({elapsed:.1f}s, ~{remaining:.0f}s left)")

# Diagonal of one-loop Hessian (second derivatives along eigendirections)
d2S1_diag = (S1_plus - 2.0 * S1_center + S1_minus) / eps**2

# First derivatives (needed for cross-terms via sum of squares formula)
dS1 = (S1_plus - S1_minus) / (2.0 * eps)

print(f"\n  One-loop diagonal second derivatives:")
for a in range(36):
    print(f"    Direction {a:>2}: d2S1 = {d2S1_diag[a]:>14.4f}, "
          f"dS1 = {dS1[a]:>14.6f}")

t_diag_end = time.time()
print(f"\n  Diagonal computation: {t_diag_end - t_evals_start:.1f}s")

# =============================================================================
# 11. Off-Diagonal One-Loop Hessian via Polarization Identity
# =============================================================================
print("\n--- 8. Computing off-diagonal one-loop Hessian ---")

# For the off-diagonal H_1loop[a,b], we use polarization:
#   d^2 S1 / deps_a deps_b = (1/2) [d^2 S1(v_a + v_b) - d^2 S1(v_a) - d^2 S1(v_b)]
# where d^2 S1(v) means the second derivative of S1 along direction v.
#
# S1(g + h*V) = S_1loop(evals(g + h*V))
# d^2 S1(V)/dh^2 = [S1(g+h*V) - 2*S1(g) + S1(g-h*V)] / h^2
#
# For direction v_a + v_b: Delta = perturbation_matrices[a] + perturbation_matrices[b]
# Need S1 at g +/- eps * (Delta_a + Delta_b)

H_1loop = np.zeros((36, 36))
for a in range(36):
    H_1loop[a, a] = d2S1_diag[a]

n_pairs_total = 36 * 35 // 2
n_pairs_done = 0
t_offdiag_start = time.time()

for a in range(36):
    for b in range(a+1, 36):
        Delta_sum = perturbation_matrices[a] + perturbation_matrices[b]
        g_plus = g_fold + eps * Delta_sum
        g_minus = g_fold - eps * Delta_sum

        # Check PD
        if eigvalsh(g_plus)[0] < 0 or eigvalsh(g_minus)[0] < 0:
            # Skip: direction too large
            H_1loop[a, b] = 0.0
            H_1loop[b, a] = 0.0
            n_pairs_done += 1
            continue

        ev_plus = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
        ev_minus = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)

        S1_sum_plus = oneloop_action(ev_plus)
        S1_sum_minus = oneloop_action(ev_minus)

        d2S1_sum = (S1_sum_plus - 2.0 * S1_center + S1_sum_minus) / eps**2
        H_1loop[a, b] = 0.5 * (d2S1_sum - d2S1_diag[a] - d2S1_diag[b])
        H_1loop[b, a] = H_1loop[a, b]

        n_pairs_done += 1
        if n_pairs_done % 50 == 0:
            elapsed = time.time() - t_offdiag_start
            rate = n_pairs_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs_total - n_pairs_done) / rate if rate > 0 else 0
            print(f"  Pairs: {n_pairs_done}/{n_pairs_total} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_offdiag_end = time.time()
print(f"  Off-diagonal computation: {t_offdiag_end - t_offdiag_start:.1f}s")

# Symmetry check
sym_err_1loop = np.max(np.abs(H_1loop - H_1loop.T))
print(f"  H_1loop symmetry error: {sym_err_1loop:.2e}")

# =============================================================================
# 12. Assemble Effective Hessian
# =============================================================================
print("\n--- 9. Assembling effective Hessian H_eff = H_tree + H_1loop ---")

# H_tree is in its OWN eigenbasis (diagonal). To add H_1loop (computed in the same
# eigenbasis), we just add directly.
# BUT: H_tree in the original script was stored in the Sym(8) basis {basis_sym8[k]},
# not in the eigenbasis. The evecs_tree transform between them.
#
# H_tree_eigenbasis = diag(evals_tree)   [36x36 diagonal]
# H_1loop is already in the eigenbasis of H_tree (we perturbed along eigenvectors)
#
# H_eff_eigenbasis = diag(evals_tree) + H_1loop

H_tree_eigenbasis = np.diag(evals_tree)
H_eff = H_tree_eigenbasis + H_1loop

print(f"  H_tree (eigenbasis) diagonal range: [{evals_tree[0]:.4f}, {evals_tree[-1]:.4f}]")
print(f"  H_1loop diagonal range: [{np.min(np.diag(H_1loop)):.4f}, {np.max(np.diag(H_1loop)):.4f}]")
print(f"  H_1loop off-diagonal max: {np.max(np.abs(H_1loop - np.diag(np.diag(H_1loop)))):.4f}")
print(f"  H_1loop / H_tree ratio (diagonal): {np.mean(np.abs(np.diag(H_1loop) / evals_tree)):.6f}")

# Diagonalize effective Hessian
evals_eff, evecs_eff = eigh(H_eff)

print(f"\n  Effective Hessian eigenvalues:")
for k in range(36):
    sign = "+" if evals_eff[k] > 0 else ("-" if evals_eff[k] < 0 else "~0")
    ratio = evals_eff[k] / evals_tree[k] if abs(evals_tree[k]) > 1e-10 else float('inf')
    print(f"    lambda_eff_{k:>2} = {evals_eff[k]:>14.4f}  (tree: {evals_tree[k]:>14.4f})  "
          f"ratio: {ratio:.6f}  {sign}")

n_pos_eff = np.sum(evals_eff > 0)
n_neg_eff = np.sum(evals_eff < 0)
n_zero_eff = np.sum(np.abs(evals_eff) < 1.0)  # Same threshold as S61

print(f"\n  Effective Hessian signature: ({n_pos_eff}+, {n_neg_eff}-, {n_zero_eff} ~0)")

# =============================================================================
# 13. Identify Sign Flips
# =============================================================================
print("\n--- 10. Identifying sign flips ---")

sign_flips = []
for k in range(36):
    if evals_tree[k] < 0 and evals_eff[k] > 0:
        sign_flips.append(k)
        print(f"  SIGN FLIP at eigendirection {k}: "
              f"tree={evals_tree[k]:.4f} -> eff={evals_eff[k]:.4f}")

n_flips = len(sign_flips)
print(f"\n  Total sign flips: {n_flips}")

# =============================================================================
# 14. Check Gauge Direction Overlap
# =============================================================================
print("\n--- 11. Gauge direction overlap analysis ---")

# The effective Hessian eigenvectors are in the tree-level eigenbasis.
# To check overlap with gauge directions (which are in the Sym(8) basis),
# we need to transform: the effective eigenvector v_eff (in tree eigenbasis)
# maps to the Sym(8) basis via evecs_tree @ v_eff.

# Compute gauge direction overlap with effective Hessian eigenvectors
gauge_overlaps_eff = np.zeros((4, 36))
for g_idx in range(4):
    # Gauge direction in tree eigenbasis:
    gauge_in_tree_basis = evecs_tree.T @ gauge_directions_36[g_idx]  # 36D vector
    for e_idx in range(36):
        gauge_overlaps_eff[g_idx, e_idx] = abs(np.dot(gauge_in_tree_basis, evecs_eff[:, e_idx]))

print("  Gauge direction overlap with effective Hessian eigenvectors:")
for g_idx in range(4):
    top3 = np.argsort(gauge_overlaps_eff[g_idx])[-3:][::-1]
    print(f"  {gauge_labels[g_idx]}: top overlaps with eff-eigvec "
          f"#{top3[0]}(|o|={gauge_overlaps_eff[g_idx,top3[0]]:.4f}), "
          f"#{top3[1]}(|o|={gauge_overlaps_eff[g_idx,top3[1]]:.4f}), "
          f"#{top3[2]}(|o|={gauge_overlaps_eff[g_idx,top3[2]]:.4f})")

# Total gauge content of positive eigendirections
if n_flips > 0:
    print("\n  Gauge content of sign-flipped directions:")
    for k in sign_flips:
        total_gauge_overlap = sum(gauge_overlaps_eff[g, k]**2 for g in range(4))
        print(f"    Eff-eigvec {k}: total gauge overlap^2 = {total_gauge_overlap:.4f}")
        for g_idx in range(4):
            print(f"      {gauge_labels[g_idx]}: |overlap| = {gauge_overlaps_eff[g_idx,k]:.4f}")

# =============================================================================
# 15. Cross-Checks
# =============================================================================
print("\n--- 12. Cross-checks ---")

# 15a. Richardson extrapolation on 5 diagonal elements
print("  15a. Richardson extrapolation (5 directions)...")
eps_half = eps / 2.0
S1_plus_half = np.zeros(5)
S1_minus_half = np.zeros(5)

for a in range(5):
    g_plus = g_fold + eps_half * perturbation_matrices[a]
    g_minus = g_fold - eps_half * perturbation_matrices[a]
    ev_plus = compute_dirac_eigenvalues(g_plus, gens, f_abc, gammas, irreps_data)
    ev_minus = compute_dirac_eigenvalues(g_minus, gens, f_abc, gammas, irreps_data)
    S1_plus_half[a] = oneloop_action(ev_plus)
    S1_minus_half[a] = oneloop_action(ev_minus)

d2S1_half = (S1_plus_half - 2.0 * S1_center + S1_minus_half) / eps_half**2
d2S1_rich = (4.0 * d2S1_half - d2S1_diag[:5]) / 3.0

print(f"  {'Dir':>4} {'d2S1(eps)':>14} {'d2S1(eps/2)':>14} {'Richardson':>14} {'rel_diff':>10}")
for a in range(5):
    if abs(d2S1_diag[a]) > 1e-10:
        rel = abs(d2S1_rich[a] - d2S1_diag[a]) / abs(d2S1_diag[a])
    else:
        rel = float('nan')
    print(f"  {a:>4} {d2S1_diag[a]:>14.4f} {d2S1_half[a]:>14.4f} {d2S1_rich[a]:>14.4f} {rel:>10.6f}")

# 15b. One-loop action is trace of ln: verify sum_n ln(lambda_n^2) = ln(prod_n lambda_n^2)
mask_nz = np.abs(evals_center) > 1e-12
log_det_direct = 2.0 * np.sum(np.log(np.abs(evals_center[mask_nz])))
log_det_from_S1 = 2.0 * S1_center
print(f"\n  15b. ln(det D_K^2) consistency:")
print(f"    Direct: {log_det_direct:.6f}")
print(f"    From S_1loop: {log_det_from_S1:.6f}")
print(f"    Difference: {abs(log_det_direct - log_det_from_S1):.2e}")

# 15c. One-loop correction scale relative to tree-level
print(f"\n  15c. One-loop vs tree-level scale:")
print(f"    |H_tree| range: [{abs(evals_tree[0]):.2f}, {abs(evals_tree[-1]):.2f}]")
print(f"    |H_1loop| diag range: [{np.min(np.abs(np.diag(H_1loop))):.4f}, {np.max(np.abs(np.diag(H_1loop))):.4f}]")
print(f"    Mean ratio |H_1loop|/|H_tree| (diag): "
      f"{np.mean(np.abs(np.diag(H_1loop)) / np.abs(evals_tree)):.6f}")

# =============================================================================
# 16. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: HESSIAN-ONELOOP-62")
print("=" * 78)

print(f"\n  Tree-level: signature (0+, 36-, 0~0)")
print(f"  Effective:  signature ({n_pos_eff}+, {n_neg_eff}-, {n_zero_eff} ~0)")
print(f"  Sign flips: {n_flips}")

if n_flips >= 4:
    # Check if the 4+ flipped directions correspond to U(2) gauge directions
    gauge_content_total = 0.0  # (local)
    for k in sign_flips:
        gauge_content_total += sum(gauge_overlaps_eff[g, k]**2 for g in range(4))
    gauge_content_avg = gauge_content_total / len(sign_flips)

    if gauge_content_avg > 0.5:  # More than 50% gauge content
        gate_verdict = "PASS"
        print(f"\n  VERDICT: **PASS**")
        print(f"  {n_flips} eigenvalues flipped positive.")
        print(f"  Average gauge content of flipped directions: {gauge_content_avg:.4f}")
        print(f"  The one-loop correction lifts U(2) gauge directions as expected.")
    else:
        gate_verdict = "INFO"
        print(f"\n  VERDICT: **INFO**")
        print(f"  {n_flips} eigenvalues flipped positive, but gauge content = {gauge_content_avg:.4f}")
        print(f"  Flipped directions do NOT predominantly correspond to U(2) gauge.")
elif 1 <= n_flips < 4:
    gate_verdict = "INFO"
    print(f"\n  VERDICT: **INFO**")
    print(f"  Only {n_flips} eigenvalue(s) flipped positive (need >= 4 for PASS).")
else:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: **FAIL**")
    print(f"  Zero eigenvalues flipped positive.")
    print(f"  One-loop corrections do not alter the Hessian signature.")
    print(f"  The fold remains a strict maximum at one-loop.")

# =============================================================================
# 17. Key Numbers Summary
# =============================================================================
print("\n" + "=" * 78)
print("  KEY NUMBERS SUMMARY")
print("=" * 78)

print(f"\n  1. Tree-level signature: (0+, 36-, 0~0)")
print(f"  2. Effective signature: ({n_pos_eff}+, {n_neg_eff}-, {n_zero_eff} ~0)")
print(f"  3. Sign flips: {n_flips}")
print(f"  4. |H_1loop/H_tree| mean ratio: {np.mean(np.abs(np.diag(H_1loop)) / np.abs(evals_tree)):.6f}")
print(f"  5. One-loop correction range: [{np.min(np.diag(H_1loop)):.4f}, {np.max(np.diag(H_1loop)):.4f}]")
print(f"  6. Gate verdict: {gate_verdict}")
if n_flips > 0:
    for k in sign_flips:
        gc = sum(gauge_overlaps_eff[g, k]**2 for g in range(4))
        print(f"  7. Flipped direction {k}: tree={evals_tree[k]:.4f}, eff={evals_eff[k]:.4f}, "
              f"gauge_content={gc:.4f}")

# =============================================================================
# 18. Plots
# =============================================================================
print("\n--- 13. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'HESSIAN-ONELOOP-62: One-Loop Corrected Hessian\n'
             f'Gate: {gate_verdict} | Tree: (0+,36-) | Eff: ({n_pos_eff}+,{n_neg_eff}-) | '
             f'Flips: {n_flips}',
             fontsize=13, fontweight='bold')

# Plot 1: Tree-level vs one-loop eigenvalue spectrum
ax = axes[0, 0]
idx = np.arange(36)
ax.bar(idx - 0.2, evals_tree, 0.35, label='Tree-level', color='blue', alpha=0.7)
ax.bar(idx + 0.2, evals_eff, 0.35, label='One-loop eff.', color='red', alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
for k in sign_flips:
    ax.axvline(k, color='green', ls='--', alpha=0.5, lw=1.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue')
ax.set_title('Tree vs Effective Eigenvalues')
ax.legend(fontsize=8)

# Plot 2: One-loop correction (diagonal)
ax = axes[0, 1]
colors_1loop = ['green' if d > 0 else 'orange' for d in d2S1_diag]
ax.bar(range(36), d2S1_diag, color=colors_1loop, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Tree eigendirection index')
ax.set_ylabel('d^2 S_1loop / d eps^2')
ax.set_title('One-loop Hessian diagonal')

# Plot 3: H_1loop matrix heatmap
ax = axes[0, 2]
vmax = np.max(np.abs(H_1loop))
if vmax < 1e-10:
    vmax = 1.0
im = ax.imshow(H_1loop, cmap='RdBu_r', vmin=-vmax, vmax=vmax, aspect='equal')
ax.set_xlabel('Eigendirection')
ax.set_ylabel('Eigendirection')
ax.set_title('H_1loop matrix')
fig.colorbar(im, ax=ax, shrink=0.8)

# Plot 4: Eigenvalue shift = eff - tree
ax = axes[1, 0]
shift = evals_eff - evals_tree
colors_shift = ['red' if s > 0 else 'blue' for s in shift]
ax.bar(range(36), shift, color=colors_shift, alpha=0.7)
ax.axhline(0, color='black', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('lambda_eff - lambda_tree')
ax.set_title('Eigenvalue shift (one-loop correction)')

# Plot 5: Gauge direction overlap with effective eigenvectors
ax = axes[1, 1]
for g_idx in range(4):
    ax.plot(range(36), gauge_overlaps_eff[g_idx], 'o-', markersize=3,
            label=gauge_labels[g_idx], alpha=0.7)
for k in sign_flips:
    ax.axvline(k, color='green', ls='--', alpha=0.3)
ax.set_xlabel('Effective eigenvalue index')
ax.set_ylabel('|Overlap with gauge direction|')
ax.set_title('Gauge direction overlaps')
ax.legend(fontsize=7)

# Plot 6: One-loop/tree ratio
ax = axes[1, 2]
ratio_diag = np.abs(np.diag(H_1loop)) / np.abs(evals_tree)
ax.semilogy(range(36), ratio_diag, 'ko-', markersize=4)
ax.set_xlabel('Eigendirection index')
ax.set_ylabel('|H_1loop| / |H_tree| (diagonal)')
ax.set_title('One-loop / tree-level ratio')

plt.tight_layout()
outpath_plot = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's62_hessian_oneloop.png')
plt.savefig(outpath_plot, dpi=150, bbox_inches='tight')
print(f"  Saved: {outpath_plot}")

# =============================================================================
# 19. Save Data
# =============================================================================
print("\n--- 14. Saving data ---")

outpath_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's62_hessian_oneloop.npz')
np.savez(outpath_data,
    # Effective Hessian
    H_eff=H_eff,
    evals_eff=evals_eff,
    evecs_eff=evecs_eff,

    # One-loop Hessian
    H_1loop=H_1loop,
    d2S1_diag=d2S1_diag,
    dS1=dS1,

    # Tree-level (reproduced for reference)
    H_tree_eigenbasis=H_tree_eigenbasis,
    evals_tree=evals_tree,
    evecs_tree=evecs_tree,

    # Sign flip analysis
    n_positive=n_pos_eff,
    n_flips=n_flips,
    sign_flips=np.array(sign_flips) if sign_flips else np.array([], dtype=int),

    # Gauge direction analysis
    gauge_direction_overlaps=gauge_overlaps_eff,
    gauge_directions_36=np.array(gauge_directions_36),
    gauge_labels=np.array(gauge_labels),

    # Richardson cross-check
    d2S1_half=d2S1_half,
    d2S1_rich=d2S1_rich,

    # Parameters
    epsilon=eps,
    Lambda_sq=Lambda_sq,
    S1_center=S1_center,
    tau_fold=tau_fold,
    g_fold=g_fold,

    # Gate verdict
    gate_verdict=gate_verdict,
)

print(f"  Saved: {outpath_data}")

t_total = time.time() - t_global_start
print(f"\n  Total wall time: {t_total:.1f}s")
print(f"  Total SA evaluations: ~{2*36 + 2*n_pairs_total + 2*5}")
print("\n" + "=" * 78)
print("  HESSIAN-ONELOOP-62 COMPLETE")
print("=" * 78)
