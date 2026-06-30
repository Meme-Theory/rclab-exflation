#!/usr/bin/env python3
"""
s66_hessian_cutoff.py — HESSIAN-CUTOFF-66: One-Loop Hessian at Finite Lambda
==============================================================================
Gate: HESSIAN-CUTOFF-66
  PASS: (36+, 0-) signature preserved at ALL Lambda values
  FAIL: Negative eigenvalues appear at some Lambda
  INFO: Marginal eigenvalues near zero but no sign change

Motivation:
  The one-loop Hessian H_{ij} = d^2 S / dtau_i dtau_j at the fold determines
  Jensen metric stability. At infinite Lambda (S64/S65), all 36 eigenvalues
  are positive. But the spectral action is physically evaluated at a FINITE
  cutoff Lambda. Does the positive-definite signature survive?

  The one-loop effective action changes from:
    S_1loop(inf) = (1/2) sum_n ln(lambda_n^2)    [infinite cutoff]
  to the spectral action with cutoff function f(x) = sqrt(x):
    S_f(Lambda) = sum_n sqrt(lambda_n^2 / Lambda^2) = (1/Lambda) sum_n |lambda_n|

  This is the Chamseddine-Connes bosonic spectral action with f(x)=sqrt(x).
  At each Lambda, we compute the 36x36 Hessian of S_f by numerical second
  derivatives in the 36D symmetric metric space, then diagonalize.

Method:
  1. Load fold metric g_fold and tree-level Hessian from S64/S61.
  2. Build SU(3) Dirac operator infrastructure (same as S64/S65).
  3. For each Lambda in {0.5, 1.0, 2.0, 5.0, 10.0} * M_KK:
     a. Compute S_f at fold and at +/- eps perturbations in each of 36 directions.
     b. Build 36x36 Hessian of S_f via central finite differences.
     c. Combine: H_eff = H_tree + H_f.
     d. Diagonalize: report (n_positive, n_negative) signature.
  4. For comparison, also compute at Lambda = infinity (S64 limit).

Key physics:
  The spectral action S_f = Tr f(D_K^2/Lambda^2) at finite Lambda is the
  physically relevant quantity. Its Hessian controls moduli stability.
  If the signature changes at physical cutoffs, fold stability is UV-sensitive
  and the downstream predictions (n_s, Higgs mass) become cutoff-dependent.

  The tree-level Hessian has signature (0+, 36-) — pure saddle.
  The infinite-Lambda one-loop correction flips this to (36+, 0-).
  The question: does the flip survive at finite Lambda?

Author: Baptista-Spacetime-Analyst (Session 66, Wave 8)
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from numpy import sqrt, log, pi
from numpy.linalg import eigh, cholesky, inv, eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import tau_fold, PI

print("=" * 78)
print("  HESSIAN-CUTOFF-66: One-Loop Hessian at Finite Lambda")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (same as S64/S65)
# =============================================================================
print("\n--- 1. SU(3) infrastructure ---")

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

# =============================================================================
# 2. Frame, Connection, Dirac Operator (same as S64/S65)
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
# 3. Irrep Construction (same as S64, up to L=3)
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
    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-8  # (local)
    groups = []
    for val, idx in sorted(zip(evals, range(dim_prod))):
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
    rho = [P.conj().T @ rho_prod[a] @ P for a in range(8)]
    return rho

def build_irrep_list(gens, f_abc, max_pq_sum=3):
    """Returns list of (p, q, dim_pq, rho_matrices) for ALL irreps up to p+q <= max_pq_sum."""
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

# =============================================================================
# 4. Per-Irrep Eigenvalue and Cutoff Action Computation
# =============================================================================

def compute_geometric_data(g_metric, gens, f_abc, gammas):
    """Compute orthonormal frame, connection, and spinor connection for a metric."""
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return E, Omega

def compute_all_dirac_evals(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute D_K eigenvalues from all irreps combined.

    Returns flat array of ALL eigenvalues (with PW degeneracy).
    """
    E, Omega = compute_geometric_data(g_metric, gens, f_abc, gammas)
    all_evals = []
    for (p, q, dim_rho, rho) in irreps_data:
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = -1j * D
        evals = eigvalsh(iD)
        # Each eigenvalue has dim_rho degeneracy from the PW expansion
        evals_with_deg = np.repeat(evals, dim_rho)
        all_evals.append(evals_with_deg)
    return np.concatenate(all_evals)

def spectral_action_f_sqrt(evals, Lambda):
    """S_f = Tr f(D_K^2 / Lambda^2) with f(x) = sqrt(x).

    S_f = sum_n sqrt(lambda_n^2 / Lambda^2)
        = (1/Lambda) sum_n |lambda_n|

    This counts all eigenvalues equally, weighted by |lambda_n|/Lambda.
    No hard cutoff — all modes contribute, but UV modes are suppressed
    relative to the ln(lambda^2) action which diverges logarithmically.
    """
    return np.sum(np.abs(evals)) / Lambda

def oneloop_action_infinite(evals):
    """S_1loop = (1/2) sum_{n: lambda_n != 0} ln(lambda_n^2)

    This is the infinite-Lambda limit (standard one-loop determinant).
    """
    lam_sq = evals**2
    mask = lam_sq > 1e-24
    return 0.5 * np.sum(np.log(lam_sq[mask]))

# =============================================================================
# 5. Build Infrastructure
# =============================================================================
print("\n--- 2. Setting up infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Validate Clifford algebra
cliff_err = 0.0  # (local)
for a in range(8):
    for b in range(8):
        ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(16)
        cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
print(f"  Clifford algebra error: {cliff_err:.2e}")

# Build irreps (L_max = 3, same as S64)
print("  Building irreps (max p+q = 3)...")
irreps_data = build_irrep_list(gens, f_abc, max_pq_sum=3)
n_irreps = len(irreps_data)
total_modes = sum(d**2 * 16 for (_, _, d, _) in irreps_data)
print(f"  {n_irreps} irreps, {total_modes} total modes")

for (p, q, d, _) in irreps_data:
    print(f"    ({p},{q}): dim={d}, Dirac block={d*16}, modes with deg={d*d*16}")

# =============================================================================
# 6. Load S64/S61 Data
# =============================================================================
print("\n--- 3. Loading reference data ---")

s64_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's64_shell_hessian.npz')
s64_data = np.load(s64_path, allow_pickle=True)

H_tree_eigenbasis = s64_data['H_tree_eigenbasis']
evals_tree = s64_data['evals_tree']
g_fold = s64_data['g_fold']
eps_s64 = float(s64_data['epsilon'])

# S64 full effective Hessian (infinite-Lambda reference)
H_eff_inf = s64_data['H_eff_full']
evals_eff_inf = np.sort(eigvalsh(H_eff_inf))
n_pos_inf = np.sum(evals_eff_inf > 0)

print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  Tree eigenvalues: all negative = {np.all(evals_tree < 0)}")
print(f"    range: [{evals_tree[0]:.4f}, {evals_tree[-1]:.4f}]")
print(f"  S64 H_eff(inf): {n_pos_inf} positive, {36 - n_pos_inf} negative")
print(f"    range: [{evals_eff_inf[0]:.4f}, {evals_eff_inf[-1]:.4f}]")

# Load S61 perturbation eigenvectors
s61_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's61_moduli_hessian.npz')
s61_data = np.load(s61_path, allow_pickle=True)
evecs_tree_s61 = s61_data['evecs_36']

# =============================================================================
# 7. Build Perturbation Matrices (same basis as S64)
# =============================================================================
print("\n--- 4. Perturbation infrastructure ---")

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

perturbation_matrices = []
for a in range(36):
    Delta_a = np.zeros((8, 8))
    for k in range(36):
        Delta_a += evecs_tree_s61[k, a] * basis_sym8[k]
    perturbation_matrices.append(Delta_a)

eps = eps_s64  # Same epsilon as S64 for consistency (0.001)
print(f"  Perturbation epsilon = {eps} (same as S64)")
print(f"  36 directions in Sym(8) tree-eigenbasis")

# =============================================================================
# 8. Compute Eigenvalues at Fold (Reference Point)
# =============================================================================
print("\n--- 5. Computing D_K spectrum at fold ---")

evals_fold = compute_all_dirac_evals(g_fold, gens, f_abc, gammas, irreps_data)
n_total_evals = len(evals_fold)
print(f"  Total eigenvalues: {n_total_evals}")
print(f"  Eigenvalue range: [{evals_fold.min():.6f}, {evals_fold.max():.6f}]")
print(f"  |lambda| range: [{np.min(np.abs(evals_fold)):.6f}, {np.max(np.abs(evals_fold)):.6f}]")

# Lambda values in M_KK units
Lambda_factors = np.array([0.5, 1.0, 2.0, 5.0, 10.0])
# In M_KK units, M_KK = 1 by convention in the eigenvalue computation
# The D_K eigenvalues are in M_KK units (max ~ 2.06)

# Reference actions at fold for each Lambda
print(f"\n  Spectral action S_f(fold) at each Lambda:")
for Lam in Lambda_factors:
    S_f = spectral_action_f_sqrt(evals_fold, Lam)
    S_inf = oneloop_action_infinite(evals_fold)
    print(f"    Lambda = {Lam:.1f} M_KK: S_f = {S_f:.6f}, S_1loop(inf) = {S_inf:.6f}")

# =============================================================================
# 9. MAIN COMPUTATION: Hessian at Each Lambda
# =============================================================================
print("\n--- 6. Main computation: 36x36 Hessian at each Lambda ---")
print(f"  Method: central finite differences, eps = {eps}")
print(f"  Requires: 36 diagonal + 630 off-diagonal = 666 perturbed metrics per Lambda")
print(f"  Total Dirac evaluations: ~{666 * 2 * n_irreps} per Lambda, x {len(Lambda_factors)} Lambda values")
print(f"  PLUS infinite-Lambda reference = {len(Lambda_factors) + 1} total sweeps")

# We compute all perturbed eigenvalue sets ONCE, then evaluate S_f for each Lambda.
# This is the key optimization: eigenvalue computation is expensive, but evaluating
# S_f = (1/Lambda) sum |lambda_n| is cheap once eigenvalues are known.

# Phase 1: Diagonal perturbations (36 directions, +/- each)
print("\n  Phase 1: Diagonal perturbations (36 x 2 = 72 Dirac evaluations)...")
t_phase1_start = time.time()

evals_plus = []   # evals_plus[a] = eigenvalues at g_fold + eps * Delta_a
evals_minus = []  # evals_minus[a] = eigenvalues at g_fold - eps * Delta_a

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    ev_p = compute_all_dirac_evals(g_plus, gens, f_abc, gammas, irreps_data)
    ev_m = compute_all_dirac_evals(g_minus, gens, f_abc, gammas, irreps_data)

    evals_plus.append(ev_p)
    evals_minus.append(ev_m)

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_phase1_start
        rate = (a+1) / elapsed if elapsed > 0 else 1
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"    Direction {a+1}/36 ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase1_end = time.time()
print(f"  Phase 1 complete: {t_phase1_end - t_phase1_start:.1f}s")

# Phase 2: Off-diagonal perturbations (630 pairs)
print("\n  Phase 2: Off-diagonal perturbations (630 x 2 = 1260 Dirac evaluations)...")
t_phase2_start = time.time()

# evals_pair_plus[a,b] and evals_pair_minus[a,b] for a < b
evals_pair_plus = {}
evals_pair_minus = {}
n_pairs_total = 36 * 35 // 2
n_done = 0  # (local)
n_skipped = 0  # (local)

for a in range(36):
    for b in range(a+1, 36):
        Delta_sum = perturbation_matrices[a] + perturbation_matrices[b]
        g_plus = g_fold + eps * Delta_sum
        g_minus = g_fold - eps * Delta_sum

        # Check positive definiteness
        if eigvalsh(g_plus)[0] < 0 or eigvalsh(g_minus)[0] < 0:
            evals_pair_plus[(a,b)] = None
            evals_pair_minus[(a,b)] = None
            n_skipped += 1
            n_done += 1
            continue

        ev_p = compute_all_dirac_evals(g_plus, gens, f_abc, gammas, irreps_data)
        ev_m = compute_all_dirac_evals(g_minus, gens, f_abc, gammas, irreps_data)

        evals_pair_plus[(a,b)] = ev_p
        evals_pair_minus[(a,b)] = ev_m

        n_done += 1
        if n_done % 50 == 0:
            elapsed = time.time() - t_phase2_start
            rate = n_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs_total - n_done) / rate if rate > 0 else 0
            print(f"    Pairs: {n_done}/{n_pairs_total} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase2_end = time.time()
print(f"  Phase 2 complete: {t_phase2_end - t_phase2_start:.1f}s ({n_skipped} pairs skipped)")

# =============================================================================
# 10. Assemble Hessians for Each Lambda
# =============================================================================
print("\n--- 7. Assembling Hessians ---")

# Include infinite Lambda as a comparison point
Lambda_list = list(Lambda_factors) + [np.inf]
Lambda_labels = [f"{L:.1f}" if np.isfinite(L) else "inf" for L in Lambda_list]

results = {}  # Lambda -> {H_f, H_eff, evals_eff, n_pos, n_neg, S_f_center}

for Lam_idx, Lam in enumerate(Lambda_list):
    label = Lambda_labels[Lam_idx]
    print(f"\n  Lambda = {label} M_KK:")

    # Choose action function
    if np.isfinite(Lam):
        action_fn = lambda ev: spectral_action_f_sqrt(ev, Lam)
    else:
        action_fn = oneloop_action_infinite

    # Center value
    S_center = action_fn(evals_fold)

    # Diagonal: d^2S / dtau_a^2
    d2S_diag = np.zeros(36)
    for a in range(36):
        S_p = action_fn(evals_plus[a])
        S_m = action_fn(evals_minus[a])
        d2S_diag[a] = (S_p - 2.0 * S_center + S_m) / eps**2

    # Build full Hessian
    H_f = np.zeros((36, 36))
    H_f[np.diag_indices(36)] = d2S_diag

    # Off-diagonal via polarization identity:
    # d^2S / (dtau_a dtau_b) = (1/2) [d^2S/(d(tau_a+tau_b))^2 - d^2S/dtau_a^2 - d^2S/dtau_b^2]
    for a in range(36):
        for b in range(a+1, 36):
            if evals_pair_plus[(a,b)] is None:
                H_f[a, b] = 0.0
                H_f[b, a] = 0.0
            else:
                S_sum_p = action_fn(evals_pair_plus[(a,b)])
                S_sum_m = action_fn(evals_pair_minus[(a,b)])
                d2S_sum = (S_sum_p - 2.0 * S_center + S_sum_m) / eps**2
                H_f[a, b] = 0.5 * (d2S_sum - d2S_diag[a] - d2S_diag[b])
                H_f[b, a] = H_f[a, b]

    # Symmetry check
    sym_err = np.max(np.abs(H_f - H_f.T))
    frob_f = np.linalg.norm(H_f, 'fro')

    # Full effective Hessian: tree + one-loop(cutoff)
    H_eff = H_tree_eigenbasis + H_f
    evals_eff = np.sort(eigvalsh(H_eff))
    n_pos = int(np.sum(evals_eff > 0))
    n_neg = 36 - n_pos
    n_near_zero = int(np.sum(np.abs(evals_eff) < 0.1 * np.max(np.abs(evals_eff))))

    results[Lam] = {
        'H_f': H_f,
        'H_eff': H_eff,
        'evals_eff': evals_eff,
        'n_pos': n_pos,
        'n_neg': n_neg,
        'n_near_zero': n_near_zero,
        'S_f_center': S_center,
        'frob_f': frob_f,
        'sym_err': sym_err,
    }

    print(f"    S_f(fold) = {S_center:.6f}")
    print(f"    ||H_f||_F = {frob_f:.4f}, sym_err = {sym_err:.2e}")
    print(f"    H_eff signature: ({n_pos}+, {n_neg}-)")
    print(f"    H_eff eigenvalue range: [{evals_eff[0]:.4f}, {evals_eff[-1]:.4f}]")
    print(f"    Smallest |eigenvalue|: {np.min(np.abs(evals_eff)):.6f}")

# =============================================================================
# 11. Summary Table
# =============================================================================
print("\n" + "=" * 78)
print("  SUMMARY: Hessian Signature vs Lambda")
print("=" * 78)

print(f"\n  {'Lambda/M_KK':>12} {'S_f(fold)':>14} {'||H_f||_F':>12} {'n_pos':>6} {'n_neg':>6} "
      f"{'min(eval)':>14} {'max(eval)':>14} {'min|eval|':>12}")
print("  " + "-" * 102)

for Lam in Lambda_list:
    r = results[Lam]
    label = f"{Lam:.1f}" if np.isfinite(Lam) else "inf"
    evals_eff = r['evals_eff']
    print(f"  {label:>12} {r['S_f_center']:>14.4f} {r['frob_f']:>12.4f} "
          f"{r['n_pos']:>6} {r['n_neg']:>6} "
          f"{evals_eff[0]:>14.4f} {evals_eff[-1]:>14.4f} "
          f"{np.min(np.abs(evals_eff)):>12.6f}")

# Tree-level reference
print(f"\n  Tree-level (no one-loop): 0+, 36-")
print(f"    min = {evals_tree[0]:.4f}, max = {evals_tree[-1]:.4f}")

# =============================================================================
# 12. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: HESSIAN-CUTOFF-66")
print("=" * 78)

all_positive = all(results[Lam]['n_neg'] == 0 for Lam in Lambda_factors)
any_negative = any(results[Lam]['n_neg'] > 0 for Lam in Lambda_factors)
min_abs_eval = min(np.min(np.abs(results[Lam]['evals_eff'])) for Lam in Lambda_factors)
max_abs_eval = max(np.max(np.abs(results[Lam]['evals_eff'])) for Lam in Lambda_factors)
marginality_ratio = min_abs_eval / max_abs_eval

if all_positive:
    if marginality_ratio < 0.01:
        gate_verdict = "INFO"
        print(f"\n  VERDICT: INFO")
        print(f"  All eigenvalues positive at every Lambda, but marginality ratio = {marginality_ratio:.6f} < 0.01")
        print(f"  Some eigenvalues are near zero relative to the spectrum scale.")
    else:
        gate_verdict = "PASS"
        print(f"\n  VERDICT: PASS")
        print(f"  All 36 eigenvalues POSITIVE at every tested Lambda = {Lambda_factors} * M_KK")
        print(f"  (36+, 0-) signature preserved. Jensen fold is stable under finite cutoffs.")
elif any_negative:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: FAIL")
    print(f"  Negative eigenvalues appear at some Lambda values:")
    for Lam in Lambda_factors:
        r = results[Lam]
        if r['n_neg'] > 0:
            print(f"    Lambda = {Lam:.1f}: ({r['n_pos']}+, {r['n_neg']}-)")

print(f"\n  Marginality ratio (min|eval|/max|eval|): {marginality_ratio:.6f}")
print(f"  Minimum |eigenvalue| across all Lambda: {min_abs_eval:.6f}")

# Detailed eigenvalue table at each Lambda
print(f"\n  Eigenvalue spectrum at each Lambda (first 10 and last 3 of 36):")
header = f"  {'idx':>3}"
for Lam in Lambda_list:
    label = f"{Lam:.1f}" if np.isfinite(Lam) else "inf"
    header += f"  {label:>12}"
print(header)
print("  " + "-" * (3 + 14 * len(Lambda_list)))

display_indices = list(range(min(10, 36))) + list(range(max(33, 0), 36))
for k in display_indices:
    line = f"  {k:>3}"
    for Lam in Lambda_list:
        ev = results[Lam]['evals_eff'][k]
        sign = "+" if ev > 0 else "-"
        line += f"  {ev:>11.4f}{sign}"
    print(line)

# =============================================================================
# 13. Structural Analysis
# =============================================================================
print("\n--- 8. Structural analysis ---")

# How does ||H_f||_F scale with Lambda?
print(f"\n  One-loop Hessian Frobenius norm vs Lambda:")
for Lam in Lambda_list:
    r = results[Lam]
    label = f"{Lam:.1f}" if np.isfinite(Lam) else "inf"
    ratio_to_tree = r['frob_f'] / np.linalg.norm(H_tree_eigenbasis, 'fro')
    print(f"    Lambda = {label}: ||H_f||_F = {r['frob_f']:.4f}, "
          f"ratio to tree = {ratio_to_tree:.4f}")

# At what Lambda does the one-loop Hessian equal the tree Hessian in norm?
tree_frob = np.linalg.norm(H_tree_eigenbasis, 'fro')
print(f"\n  ||H_tree||_F = {tree_frob:.4f}")
print(f"  For fold stability (all eigenvalues positive), need ||H_f|| > ||H_tree|| in the soft direction.")

# Critical Lambda: smallest Lambda where all eigenvalues remain positive
print(f"\n  Critical Lambda analysis:")
for Lam in Lambda_factors:
    r = results[Lam]
    min_ev = r['evals_eff'][0]
    print(f"    Lambda = {Lam:.1f}: min eigenvalue = {min_ev:.6f} ({'STABLE' if min_ev > 0 else 'UNSTABLE'})")

# =============================================================================
# 14. Consistency Check: Lambda -> inf limit vs S64
# =============================================================================
print("\n--- 9. Consistency check ---")

r_inf = results[np.inf]
evals_this = r_inf['evals_eff']
evals_s64 = evals_eff_inf

max_dev = np.max(np.abs(evals_this - evals_s64))
rel_dev = max_dev / np.max(np.abs(evals_s64))
print(f"  Lambda=inf eigenvalues vs S64: max deviation = {max_dev:.6e} ({rel_dev:.2e} relative)")
if max_dev < 0.1:
    print(f"  CONSISTENT with S64 (deviation < 0.1)")
else:
    print(f"  WARNING: deviation from S64 exceeds 0.1")

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 15. Save Data
# =============================================================================
print("\n--- 10. Saving results ---")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's66_hessian_cutoff.npz')

save_dict = {
    'gate_name': 'HESSIAN-CUTOFF-66',
    'gate_verdict': gate_verdict,
    'Lambda_factors': Lambda_factors,
    'tau_fold': tau_fold,
    'g_fold': g_fold,
    'epsilon': eps,
    'evals_tree': evals_tree,
    'H_tree_eigenbasis': H_tree_eigenbasis,
    'evals_fold_DK': evals_fold,
    'total_time': t_total,
}

for i, Lam in enumerate(Lambda_factors):
    r = results[Lam]
    key = f"L{Lambda_labels[i].replace('.', 'p')}"
    save_dict[f'H_f_{key}'] = r['H_f']
    save_dict[f'H_eff_{key}'] = r['H_eff']
    save_dict[f'evals_eff_{key}'] = r['evals_eff']
    save_dict[f'n_pos_{key}'] = r['n_pos']
    save_dict[f'n_neg_{key}'] = r['n_neg']
    save_dict[f'frob_{key}'] = r['frob_f']

# Infinite Lambda reference
r_inf = results[np.inf]
save_dict['H_f_inf'] = r_inf['H_f']
save_dict['H_eff_inf'] = r_inf['H_eff']
save_dict['evals_eff_inf'] = r_inf['evals_eff']
save_dict['n_pos_inf'] = r_inf['n_pos']
save_dict['n_neg_inf'] = r_inf['n_neg']

np.savez(out_path, **save_dict)
print(f"  Saved: {out_path}")

# =============================================================================
# 16. Visualization
# =============================================================================
print("\n--- 11. Generating visualization ---")

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle(r'HESSIAN-CUTOFF-66: One-Loop Hessian at Finite $\Lambda$'
             f'\nGate: {gate_verdict} | '
             r'$f(x) = \sqrt{x}$, Spectral Action Cutoff',
             fontsize=13, fontweight='bold')

# --- Panel 1: Eigenvalue spectrum at each Lambda ---
ax1 = axes[0, 0]
Lambda_plot = Lambda_factors
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(Lambda_plot)))
for i, Lam in enumerate(Lambda_plot):
    evals_eff = results[Lam]['evals_eff']
    ax1.plot(range(36), evals_eff, 'o-', color=colors[i], markersize=3,
             linewidth=1.0, label=rf'$\Lambda = {Lam:.1f} M_{{KK}}$')

# Add infinite-Lambda reference
evals_inf = results[np.inf]['evals_eff']
ax1.plot(range(36), evals_inf, 's--', color='red', markersize=4,
         linewidth=1.5, alpha=0.7, label=r'$\Lambda = \infty$')

ax1.axhline(y=0, color='k', linewidth=1.0, linestyle='--')
ax1.set_xlabel('Eigenvalue index', fontsize=11)
ax1.set_ylabel(r'$H_{\mathrm{eff}}$ eigenvalue', fontsize=11)
ax1.set_title(r'Hessian Eigenvalue Spectrum vs $\Lambda$', fontsize=11)
ax1.legend(fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)

# --- Panel 2: Signature diagram ---
ax2 = axes[0, 1]
n_pos_vals = [results[L]['n_pos'] for L in Lambda_factors]
n_neg_vals = [results[L]['n_neg'] for L in Lambda_factors]

x_pos = np.arange(len(Lambda_factors))
ax2.bar(x_pos, n_pos_vals, color='green', alpha=0.7, label='Positive')
ax2.bar(x_pos, n_neg_vals, bottom=n_pos_vals, color='red', alpha=0.7, label='Negative')
ax2.axhline(y=36, color='k', linewidth=0.5, linestyle=':')

for i, (np_v, nn_v) in enumerate(zip(n_pos_vals, n_neg_vals)):
    ax2.text(i, 18, f'({np_v}+, {nn_v}-)', ha='center', va='center',
             fontsize=10, fontweight='bold', color='white')

ax2.set_xticks(x_pos)
ax2.set_xticklabels([f'{L:.1f}' for L in Lambda_factors], fontsize=10)
ax2.set_xlabel(r'$\Lambda / M_{KK}$', fontsize=11)
ax2.set_ylabel('Number of eigenvalues', fontsize=11)
ax2.set_title('Hessian Signature vs Cutoff', fontsize=11)
ax2.legend(fontsize=10)
ax2.set_ylim(0, 40)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Minimum eigenvalue vs Lambda ---
ax3 = axes[1, 0]
min_evals = [results[L]['evals_eff'][0] for L in Lambda_factors]
ax3.plot(Lambda_factors, min_evals, 'o-', color='blue', linewidth=2, markersize=8)
ax3.axhline(y=0, color='red', linewidth=2, linestyle='--', label='Stability boundary')

# Add reference line for infinite Lambda
ax3.axhline(y=evals_eff_inf[0], color='gray', linewidth=1, linestyle=':',
            label=rf'$\Lambda = \infty$: {evals_eff_inf[0]:.1f}')

for i, (Lam, me) in enumerate(zip(Lambda_factors, min_evals)):
    ax3.annotate(f'{me:.1f}', (Lam, me), textcoords="offset points",
                 xytext=(10, 5), fontsize=9)

ax3.set_xlabel(r'$\Lambda / M_{KK}$', fontsize=11)
ax3.set_ylabel('Minimum eigenvalue of $H_{eff}$', fontsize=11)
ax3.set_title('Softest Hessian Mode vs Cutoff', fontsize=11)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_xscale('log')

# --- Panel 4: Frobenius norm of one-loop Hessian vs Lambda ---
ax4 = axes[1, 1]
frob_vals = [results[L]['frob_f'] for L in Lambda_factors]
frob_inf = results[np.inf]['frob_f']

ax4.plot(Lambda_factors, frob_vals, 'o-', color='purple', linewidth=2, markersize=8)
ax4.axhline(y=tree_frob, color='red', linewidth=1.5, linestyle='--',
            label=rf'$\|H_{{tree}}\|_F = {tree_frob:.0f}$')
ax4.axhline(y=frob_inf, color='gray', linewidth=1, linestyle=':',
            label=rf'$\Lambda = \infty$: $\|H_f\|_F = {frob_inf:.0f}$')

for i, (Lam, fv) in enumerate(zip(Lambda_factors, frob_vals)):
    ax4.annotate(f'{fv:.0f}', (Lam, fv), textcoords="offset points",
                 xytext=(10, 5), fontsize=9)

ax4.set_xlabel(r'$\Lambda / M_{KK}$', fontsize=11)
ax4.set_ylabel(r'$\|H_{f}\|_F$', fontsize=11)
ax4.set_title(r'One-Loop Hessian Frobenius Norm vs $\Lambda$', fontsize=11)
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3)
ax4.set_xscale('log')
ax4.set_yscale('log')

plt.tight_layout()
fig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's66_hessian_cutoff.png')
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {fig_path}")

print("\n" + "=" * 78)
print(f"  HESSIAN-CUTOFF-66 COMPLETE")
print(f"  Verdict: {gate_verdict}")
print(f"  Time: {t_total:.1f}s")
print("=" * 78)
