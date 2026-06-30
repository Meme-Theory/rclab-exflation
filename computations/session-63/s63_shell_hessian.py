#!/usr/bin/env python3
"""
s63_shell_hessian.py — SHELL-HESSIAN-63: Shell-by-Shell FRG Proxy
===================================================================
Gate: SHELL-HESSIAN-63
  PASS if all 36 eigenvalues of H_eff(L) are positive at EVERY PW shell L.
  FAIL if any eigenvalue crosses zero at any shell.

Background:
  S62 HESSIAN-ONELOOP-62 found all 36 eigenvalues positive with ratio 3.47.
  The SP-Phonon workshop proposed removing shells from the UV end to trace
  the FRG flow: does fold stability depend on the UV completion, or is it
  robust at every scale?

  This is the nuclear Strutinsky analog: in nuclear DFT, the self-consistent
  mean field is built from all occupied levels. Shell corrections arise from
  individual j-shells. Removing the highest shell and recomputing tests
  whether the binding energy (here: stability) depends on the specific
  shell structure or is a bulk property.

Method:
  1. Order D_K eigenvalues by PW level L = p+q of the irrep (p,q).
  2. Compute S_1loop(L) = (1/2) sum_{n in shells <= L} ln(lambda_n^2).
     Because ln is additive, S_1loop(L) = sum_{L'=0}^{L} S_1loop^{(L')}.
  3. The one-loop Hessian decomposes: H_1loop(L) = sum_{L'=0}^{L} H_1loop^{(L')}.
  4. For each shell L' we compute H_1loop^{(L')} from finite differences of
     S_1loop^{(L')}, where S_1loop^{(L')} uses ONLY eigenvalues from shell L'.
  5. Cumulate: H_eff(L) = H_tree + sum_{L'=0}^{L} H_1loop^{(L')}.
  6. Diagonalize at each L. Record eigenvalues and zero crossings.
  7. Check 9-multiplet cluster structure from SU(3) rep theory.

Key insight (nuclear analogy):
  In HFB theory, the self-consistent field is built from ALL quasiparticle
  levels within the pairing window. Removing levels tests the stability of
  self-consistency. Here, each PW shell is analogous to a nuclear j-shell:
  the one-loop effective action sums contributions from each shell, and
  we test whether stability requires specific UV shells or is IR-robust.

  The FRG parallel: in the functional renormalization group, one integrates
  out momentum shells from UV to IR, building the effective average action
  Gamma_k. Here, PW level L plays the role of the FRG cutoff k. The flow
  from L=L_max to L=0 maps to the FRG flow from k=Lambda to k=0.

Author: nazarewicz-nuclear-structure-theorist (Session 63, Wave 2)
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
print("  SHELL-HESSIAN-63: Shell-by-Shell FRG Proxy for Fold Stability")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (from S62)
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

# =============================================================================
# 2. Frame, Connection, Dirac Operator (from S62)
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
# 3. Irrep Construction (from S62)
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
    """Returns list of (p, q, dim_pq, rho_matrices)."""
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
# 4. Shell-Resolved Eigenvalue Computation
# =============================================================================

def compute_dirac_evals_by_shell(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute D_K eigenvalues, organized by PW shell L = p+q.

    Returns dict: shell_evals[L] = array of eigenvalues from all irreps with p+q=L.
    Each eigenvalue includes the dim_rho degeneracy factor.
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    shell_evals = {}
    for (p, q, dim_rho, rho) in irreps_data:
        L = p + q
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = -1j * D
        evals = eigvalsh(iD)
        # Each eigenvalue of the block is repeated dim_rho times
        evals_with_deg = np.repeat(evals, dim_rho)
        if L not in shell_evals:
            shell_evals[L] = []
        shell_evals[L].append(evals_with_deg)

    # Concatenate all irreps within each shell
    for L in shell_evals:
        shell_evals[L] = np.concatenate(shell_evals[L])

    return shell_evals

def oneloop_action_from_evals(evals):
    """S_1loop = (1/2) sum_{n: lambda_n != 0} ln(lambda_n^2)"""
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

# Build irreps (max_pq_sum=3, same as S62)
print("  Building irreps (max p+q = 3)...")
irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3)

# Shell structure summary
shell_counts = {}
for p, q, dim, _ in irreps_data:
    L = p + q
    n_evals = dim * dim * 16  # dim_rho^2 * 16
    if L not in shell_counts:
        shell_counts[L] = {'irreps': [], 'n_evals': 0}
    shell_counts[L]['irreps'].append(f"({p},{q}):dim={dim}")
    shell_counts[L]['n_evals'] += n_evals

print("\n  PW Shell Structure:")
L_max = max(shell_counts.keys())
total_evals = 0  # (local)
for L in sorted(shell_counts.keys()):
    info = shell_counts[L]
    total_evals += info['n_evals']
    print(f"    L={L}: {info['n_evals']:>6d} evals, irreps = {', '.join(info['irreps'])}")
print(f"    Total: {total_evals:>6d} evals")

# =============================================================================
# 6. Load Tree-Level Hessian Data from S61
# =============================================================================
print("\n--- 3. Loading S61 tree-level Hessian data ---")

s61_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's61_moduli_hessian.npz')
s61_data = np.load(s61_path, allow_pickle=True)

H_tree = s61_data['H_36']
evals_tree = s61_data['evals_36']
evecs_tree = s61_data['evecs_36']
g_fold = s61_data['g_fold']
Lambda_sq = float(s61_data['Lambda_sq'])
basis_labels = list(s61_data['basis_labels'])
epsilon_s61 = float(s61_data['epsilon'])

print(f"  H_tree shape: {H_tree.shape}")
print(f"  Tree-level eigenvalues: min={evals_tree[0]:.4f}, max={evals_tree[-1]:.4f}")
print(f"  All negative: {np.all(evals_tree < 0)}")
print(f"  Lambda^2: {Lambda_sq:.6f}")

# =============================================================================
# 7. Reconstruct Sym(8) Basis and Perturbation Matrices
# =============================================================================
print("\n--- 4. Reconstructing perturbation infrastructure ---")

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

# Perturbation matrices in the tree-level eigenbasis
perturbation_matrices = []
for a in range(36):
    Delta_a = np.zeros((8, 8))
    for k in range(36):
        Delta_a += evecs_tree[k, a] * basis_sym8[k]
    perturbation_matrices.append(Delta_a)

# Verify fold eigenvalues
evals_fold_verify = compute_dirac_evals_by_shell(g_fold, gens, f_abc, gammas, irreps_data)
total_verify = sum(len(v) for v in evals_fold_verify.values())
print(f"  Shell eigenvalue verification: {total_verify} total eigenvalues")
for L in sorted(evals_fold_verify.keys()):
    evs = evals_fold_verify[L]
    print(f"    L={L}: {len(evs)} evals, |lambda| range: [{np.min(np.abs(evs)):.6f}, {np.max(np.abs(evs)):.6f}]")

# =============================================================================
# 8. Compute Shell-Resolved One-Loop Hessian
# =============================================================================
print("\n--- 5. Computing shell-resolved one-loop Hessian ---")
print(f"  Strategy: Decompose S_1loop = sum_L S_1loop^(L)")
print(f"  Then H_1loop(L_cut) = sum_{{L'=0}}^{{L_cut}} H_1loop^(L')")

eps = 0.001  # Same as S62
print(f"  Perturbation epsilon = {eps}")

# Compute shell-resolved eigenvalues at center
shell_evals_center = compute_dirac_evals_by_shell(g_fold, gens, f_abc, gammas, irreps_data)

# One-loop contribution by shell at center
S1_shell_center = {}
for L in sorted(shell_evals_center.keys()):
    S1_shell_center[L] = oneloop_action_from_evals(shell_evals_center[L])
    print(f"  S_1loop^({L}) at center: {S1_shell_center[L]:.6f}  ({len(shell_evals_center[L])} modes)")

S1_total_center = sum(S1_shell_center.values())
print(f"  S_1loop total at center: {S1_total_center:.6f}")

# =============================================================================
# 9. Diagonal Hessian by Shell
# =============================================================================
print("\n--- 6. Computing diagonal Hessian contributions by shell ---")

# For each direction a (36 total), compute eigenvalues at g +/- eps*Delta_a,
# decompose by shell, and get per-shell second derivatives.

# H_1loop^(L)[a,a] = [S_1loop^(L)(+eps_a) - 2*S_1loop^(L)(0) + S_1loop^(L)(-eps_a)] / eps^2

H_1loop_shell = {}  # H_1loop_shell[L] = 36x36 matrix
for L in sorted(shell_evals_center.keys()):
    H_1loop_shell[L] = np.zeros((36, 36))

d2S1_shell = {}  # d2S1_shell[L][a] = diagonal of shell L
dS1_shell = {}   # first derivatives by shell
for L in sorted(shell_evals_center.keys()):
    d2S1_shell[L] = np.zeros(36)
    dS1_shell[L] = np.zeros(36)

t_start = time.time()

# Pre-compute perturbed eigenvalues by shell for all 36 directions (+/- epsilon)
S1_shell_plus = {}   # S1_shell_plus[L][a]
S1_shell_minus = {}  # S1_shell_minus[L][a]
for L in sorted(shell_evals_center.keys()):
    S1_shell_plus[L] = np.zeros(36)
    S1_shell_minus[L] = np.zeros(36)

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    shell_evals_plus = compute_dirac_evals_by_shell(g_plus, gens, f_abc, gammas, irreps_data)
    shell_evals_minus = compute_dirac_evals_by_shell(g_minus, gens, f_abc, gammas, irreps_data)

    for L in sorted(shell_evals_center.keys()):
        S1_shell_plus[L][a] = oneloop_action_from_evals(shell_evals_plus[L])
        S1_shell_minus[L][a] = oneloop_action_from_evals(shell_evals_minus[L])

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_start
        rate = (a+1) / elapsed if elapsed > 0 else 1
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"  Direction {a+1}/36 done ({elapsed:.1f}s, ~{remaining:.0f}s left)")

# Compute per-shell diagonals
for L in sorted(shell_evals_center.keys()):
    d2S1_shell[L] = (S1_shell_plus[L] - 2.0 * S1_shell_center[L] + S1_shell_minus[L]) / eps**2
    dS1_shell[L] = (S1_shell_plus[L] - S1_shell_minus[L]) / (2.0 * eps)
    H_1loop_shell[L][np.diag_indices(36)] = d2S1_shell[L]

t_diag_end = time.time()
print(f"\n  Diagonal computation: {t_diag_end - t_start:.1f}s")

# Print per-shell diagonal summary
print("\n  Per-shell diagonal Hessian (mean, min, max):")
for L in sorted(shell_evals_center.keys()):
    d = d2S1_shell[L]
    print(f"    L={L}: mean={np.mean(d):>12.4f}, min={np.min(d):>12.4f}, max={np.max(d):>12.4f}")

# Cross-check: sum of shells should match S62 diagonal
d2S1_total = sum(d2S1_shell[L] for L in d2S1_shell)
print(f"\n  Cross-check: shell-summed diagonal vs direct computation:")
print(f"    Shell sum range: [{np.min(d2S1_total):.4f}, {np.max(d2S1_total):.4f}]")

# =============================================================================
# 10. Off-Diagonal Hessian by Shell (Polarization Identity)
# =============================================================================
print("\n--- 7. Computing off-diagonal Hessian by shell ---")

# For a < b:
#   H_1loop^(L)[a,b] = 0.5 * [d2S1^(L)(v_a + v_b) - d2S1^(L)(v_a) - d2S1^(L)(v_b)]
# where d2S1^(L)(V) = [S1^(L)(g+eps*V) - 2*S1^(L)(0) + S1^(L)(g-eps*V)] / eps^2

n_pairs = 36 * 35 // 2
n_done = 0  # (local)
t_offdiag_start = time.time()

for a in range(36):
    for b in range(a+1, 36):
        Delta_sum = perturbation_matrices[a] + perturbation_matrices[b]
        g_plus = g_fold + eps * Delta_sum
        g_minus = g_fold - eps * Delta_sum

        # Check positive definiteness
        if eigvalsh(g_plus)[0] < 0 or eigvalsh(g_minus)[0] < 0:
            for L in shell_evals_center:
                H_1loop_shell[L][a, b] = 0.0
                H_1loop_shell[L][b, a] = 0.0
            n_done += 1
            continue

        shell_evals_plus = compute_dirac_evals_by_shell(g_plus, gens, f_abc, gammas, irreps_data)
        shell_evals_minus = compute_dirac_evals_by_shell(g_minus, gens, f_abc, gammas, irreps_data)

        for L in sorted(shell_evals_center.keys()):
            S1_sum_plus = oneloop_action_from_evals(shell_evals_plus[L])
            S1_sum_minus = oneloop_action_from_evals(shell_evals_minus[L])
            d2S1_sum = (S1_sum_plus - 2.0 * S1_shell_center[L] + S1_sum_minus) / eps**2
            H_1loop_shell[L][a, b] = 0.5 * (d2S1_sum - d2S1_shell[L][a] - d2S1_shell[L][b])
            H_1loop_shell[L][b, a] = H_1loop_shell[L][a, b]

        n_done += 1
        if n_done % 50 == 0:
            elapsed = time.time() - t_offdiag_start
            rate = n_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs - n_done) / rate if rate > 0 else 0
            print(f"  Pairs: {n_done}/{n_pairs} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_offdiag_end = time.time()
print(f"  Off-diagonal computation: {t_offdiag_end - t_offdiag_start:.1f}s")

# Symmetry check per shell
for L in sorted(H_1loop_shell.keys()):
    sym_err = np.max(np.abs(H_1loop_shell[L] - H_1loop_shell[L].T))
    print(f"  H_1loop^({L}) symmetry error: {sym_err:.2e}")

# =============================================================================
# 11. Cumulative Hessian Flow: H_eff(L) = H_tree + sum_{L'<=L} H_1loop^{(L')}
# =============================================================================
print("\n--- 8. Shell-by-shell FRG flow ---")
print("  H_eff(L) = H_tree_eigenbasis + sum_{L'=0}^{L} H_1loop^{(L')}")

H_tree_eigenbasis = np.diag(evals_tree)

L_values = sorted(shell_evals_center.keys())  # [0, 1, 2, 3]
n_shells = len(L_values)

# Storage for the flow
evals_flow = np.zeros((n_shells, 36))  # evals_flow[i, :] = eigenvalues at cutoff L=L_values[i]
n_positive_flow = np.zeros(n_shells, dtype=int)
n_negative_flow = np.zeros(n_shells, dtype=int)
zero_crossings = []  # List of (L, eigenvalue_index, value)

# 9-multiplet cluster analysis
cluster_widths = np.zeros((n_shells, 4))  # For up to 4 clusters at each L

H_1loop_cumulative = np.zeros((36, 36))

print(f"\n  {'L':>3} {'n_pos':>6} {'n_neg':>6} {'min_eval':>14} {'max_eval':>14} "
      f"{'ratio_min':>12} {'Frobenius_1loop':>16}")
print("  " + "-" * 82)

for i, L_cut in enumerate(L_values):
    H_1loop_cumulative += H_1loop_shell[L_cut]
    H_eff = H_tree_eigenbasis + H_1loop_cumulative
    evals_eff, evecs_eff = eigh(H_eff)

    evals_flow[i, :] = evals_eff
    n_pos = np.sum(evals_eff > 0)
    n_neg = np.sum(evals_eff <= 0)
    n_positive_flow[i] = n_pos
    n_negative_flow[i] = n_neg

    # Ratio: one-loop / tree
    ratio_min = np.min(np.abs(evals_eff)) / np.max(np.abs(evals_tree))

    # Frobenius norm of cumulative one-loop
    frob = np.sqrt(np.sum(H_1loop_cumulative**2))

    print(f"  L={L_cut:>2}: {n_pos:>5}+ {n_neg:>5}-  min={evals_eff[0]:>14.4f}  "
          f"max={evals_eff[-1]:>14.4f}  ratio_min={ratio_min:>10.6f}  ||H_1loop||={frob:>12.4f}")

    # Track zero crossings
    if i > 0:
        for k in range(36):
            if evals_flow[i-1, k] * evals_flow[i, k] < 0:
                zero_crossings.append((L_cut, k, evals_flow[i, k]))

    # 9-multiplet cluster analysis
    # In SU(3), the moduli space decomposes into orbits of the adjoint action.
    # The 36D space of symmetric 8x8 matrices splits under SU(3):
    # Sym^2(su(3)) decomposes into irreps. The eigenvalues should cluster
    # by the representation content.
    # With the Jensen metric structure (3+4+1), we expect clusters
    # corresponding to the block structure.

# Detailed eigenvalue printout at each shell
print("\n  Detailed eigenvalue flow:")
header = f"  {'idx':>3}"
for L in L_values:
    header += f"  {'L='+str(L):>14}"
print(header)
print("  " + "-" * (3 + 16 * len(L_values)))
for k in range(36):
    line = f"  {k:>3}"
    for i in range(n_shells):
        sign = "+" if evals_flow[i, k] > 0 else "-"
        line += f"  {evals_flow[i, k]:>13.4f}{sign}"
    print(line)

# =============================================================================
# 12. 9-Multiplet Cluster Analysis
# =============================================================================
print("\n--- 9. Cluster analysis at each shell ---")

# The 36 moduli directions decompose under the Jensen SU(2)xU(1) symmetry.
# The g_fold metric has 3-fold degeneracy in the SU(2) block,
# 4-fold degeneracy in the coset block, and 1 isolated direction (U(1)).
# Expected clusters from the H_tree eigenvalue structure:
#   Group A: ~{-148.69} x 5  (degenerate cluster near most negative)
#   Group B: ~{-131.72} x 1
#   Group C: ~{-67.16} x 8
#   ...and so on

def find_clusters(evals, tol_frac=0.05):
    """Find clusters of eigenvalues within tol_frac relative tolerance."""
    sorted_ev = np.sort(evals)
    clusters = []
    current = [sorted_ev[0]]
    for ev in sorted_ev[1:]:
        ref = np.mean(current) if abs(np.mean(current)) > 1e-10 else 1.0
        if abs(ev - np.mean(current)) / abs(ref) < tol_frac:
            current.append(ev)
        else:
            clusters.append(np.array(current))
            current = [ev]
    clusters.append(np.array(current))
    return clusters

for i, L_cut in enumerate(L_values):
    clusters = find_clusters(evals_flow[i, :], tol_frac=0.10)
    print(f"\n  L={L_cut}: {len(clusters)} clusters")
    for j, cl in enumerate(clusters):
        width = np.max(cl) - np.min(cl) if len(cl) > 1 else 0.0
        print(f"    Cluster {j}: size={len(cl):>2}, "
              f"mean={np.mean(cl):>12.4f}, width={width:>10.6f}")

# =============================================================================
# 13. FRG Flow Ratios
# =============================================================================
print("\n--- 10. FRG flow ratios ---")

# Key diagnostic: how does the minimum eigenvalue scale with the number of
# included modes? In nuclear DFT, the shell correction energy scales as
# N^{-1/3} relative to the bulk. Here, each shell adds ~L^4 modes.

cum_modes = np.zeros(n_shells)
for i, L_cut in enumerate(L_values):
    cum_modes[i] = sum(shell_counts[L]['n_evals'] for L in range(L_cut + 1))

print(f"\n  {'L':>3} {'cum_modes':>10} {'min_eval':>14} {'max_eval':>14} "
      f"{'min/max_ratio':>14} {'one-loop/tree':>14}")
print("  " + "-" * 74)
for i, L_cut in enumerate(L_values):
    min_ev = evals_flow[i, 0]
    max_ev = evals_flow[i, -1]
    ratio = min_ev / max_ev if abs(max_ev) > 1e-10 else float('inf')
    # One-loop dominance ratio
    oneloop_frob = np.sqrt(np.sum(sum(H_1loop_shell[L] for L in range(L_cut+1))**2))
    tree_frob = np.sqrt(np.sum(H_tree_eigenbasis**2))
    ot_ratio = oneloop_frob / tree_frob
    print(f"  L={L_cut:>2}  {cum_modes[i]:>9.0f}  {min_ev:>13.4f}  {max_ev:>13.4f}  "
          f"{ratio:>13.6f}  {ot_ratio:>13.6f}")

# =============================================================================
# 14. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: SHELL-HESSIAN-63")
print("=" * 78)

all_positive = np.all(n_positive_flow == 36)
n_zero_cross = len(zero_crossings)

if all_positive:
    gate_verdict = "PASS"
    print(f"  VERDICT: PASS")
    print(f"  All 36 eigenvalues positive at EVERY PW shell L=0..{L_max}")
    print(f"  Zero crossings: {n_zero_cross}")
    print(f"  Fold stability is UV-robust: does NOT depend on UV completion")
else:
    gate_verdict = "FAIL"
    print(f"  VERDICT: FAIL")
    print(f"  Some eigenvalues cross zero during shell removal")
    print(f"  Zero crossings: {n_zero_cross}")
    for L, k, v in zero_crossings:
        print(f"    At L={L}, eigenvec {k}: value = {v:.6f}")
    print(f"  Fold stability DEPENDS on UV completion")

# Monotonicity check: do eigenvalues grow monotonically with L?
monotone_count = 0  # (local)
for k in range(36):
    if np.all(np.diff(evals_flow[:, k]) >= -1e-10):  # Allow numerical noise
        monotone_count += 1
print(f"\n  Monotonically increasing eigenvalues: {monotone_count}/36")

# Minimum eigenvalue at each L
print(f"\n  Minimum eigenvalue trajectory:")
for i, L_cut in enumerate(L_values):
    print(f"    L={L_cut}: lambda_min = {evals_flow[i, 0]:.6f}")

# Shell contribution fractions
print(f"\n  Per-shell contribution to one-loop Frobenius norm:")
total_frob = np.sqrt(np.sum(sum(H_1loop_shell[L] for L in L_values)**2))
for L in L_values:
    frob_L = np.sqrt(np.sum(H_1loop_shell[L]**2))
    frac = frob_L / total_frob if total_frob > 0 else 0
    print(f"    L={L}: ||H_1loop^({L})||_F = {frob_L:>12.4f} ({frac*100:>6.2f}%)")

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 15. Save Data
# =============================================================================
print("\n--- 11. Saving results ---")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's63_shell_hessian.npz')

# Organize shell Hessian contributions
H_1loop_shells_arr = np.stack([H_1loop_shell[L] for L in L_values], axis=0)  # (n_shells, 36, 36)

np.savez(out_path,
    # Gate info
    gate_name='SHELL-HESSIAN-63',
    gate_verdict=gate_verdict,
    # Shell structure
    L_values=np.array(L_values),
    L_max=L_max,
    shell_mode_counts=np.array([shell_counts[L]['n_evals'] for L in L_values]),
    cum_modes=cum_modes,
    # Eigenvalue flow
    evals_flow=evals_flow,
    n_positive_flow=n_positive_flow,
    n_negative_flow=n_negative_flow,
    # Per-shell Hessians
    H_1loop_shells=H_1loop_shells_arr,
    # Cumulative Hessian at L_max (should match S62)
    H_1loop_total=H_1loop_cumulative,
    H_eff_final=H_tree_eigenbasis + H_1loop_cumulative,
    # Tree level
    H_tree_eigenbasis=H_tree_eigenbasis,
    evals_tree=evals_tree,
    evecs_tree=evecs_tree,
    # Zero crossings
    n_zero_crossings=n_zero_cross,
    # Per-shell diagonal
    d2S1_shell_diag=np.stack([d2S1_shell[L] for L in L_values], axis=0),
    # Parameters
    epsilon=eps,
    Lambda_sq=Lambda_sq,
    tau_fold=tau_fold,
    g_fold=g_fold,
    # Computation metadata
    total_time=t_total,
)
print(f"  Saved: {out_path}")

# =============================================================================
# 16. Visualization
# =============================================================================
print("\n--- 12. Generating visualization ---")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('SHELL-HESSIAN-63: Shell-by-Shell FRG Flow of Fold Stability',
             fontsize=14, fontweight='bold')

# Panel 1: Eigenvalue flow
ax1 = axes[0, 0]
for k in range(36):
    color = 'C0' if evals_flow[-1, k] > 0 else 'C3'
    ax1.plot(L_values, evals_flow[:, k], 'o-', color=color, markersize=3, alpha=0.6)
ax1.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
ax1.set_xlabel('PW Shell Cutoff L')
ax1.set_ylabel('Eigenvalue of H_eff(L)')
ax1.set_title('FRG Flow: All 36 Eigenvalues vs Shell Cutoff')
ax1.set_xticks(L_values)
ax1.grid(True, alpha=0.3)

# Panel 2: Minimum eigenvalue trajectory
ax2 = axes[0, 1]
min_evals = evals_flow[:, 0]
ax2.plot(L_values, min_evals, 'rs-', markersize=8, linewidth=2, label=r'$\lambda_{\min}$')
ax2.plot(L_values, evals_flow[:, -1], 'bs-', markersize=8, linewidth=2, label=r'$\lambda_{\max}$')
ax2.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
ax2.set_xlabel('PW Shell Cutoff L')
ax2.set_ylabel('Eigenvalue')
ax2.set_title('Extremal Eigenvalues vs Shell Cutoff')
ax2.set_xticks(L_values)
ax2.legend()
ax2.grid(True, alpha=0.3)

# Panel 3: Per-shell Frobenius contribution
ax3 = axes[1, 0]
frob_per_shell = [np.sqrt(np.sum(H_1loop_shell[L]**2)) for L in L_values]
modes_per_shell = [shell_counts[L]['n_evals'] for L in L_values]
ax3.bar(L_values, frob_per_shell, color='steelblue', alpha=0.8, label=r'$\|H_{1loop}^{(L)}\|_F$')
ax3.set_xlabel('PW Shell L')
ax3.set_ylabel('Frobenius Norm')
ax3.set_title('Per-Shell One-Loop Hessian Contribution')
ax3.set_xticks(L_values)
# Add mode count on secondary axis
ax3b = ax3.twinx()
ax3b.plot(L_values, modes_per_shell, 'ro-', markersize=6, label='# modes')
ax3b.set_ylabel('Number of Modes', color='red')
ax3b.tick_params(axis='y', labelcolor='red')
ax3.legend(loc='upper left')
ax3b.legend(loc='upper right')
ax3.grid(True, alpha=0.3)

# Panel 4: Cluster structure at L_max
ax4 = axes[1, 1]
for i, L_cut in enumerate(L_values):
    y_pos = L_cut
    for k in range(36):
        color = 'C0' if evals_flow[i, k] > 0 else 'C3'
        ax4.plot(evals_flow[i, k], y_pos, '|', color=color, markersize=15, markeredgewidth=1.5)
ax4.axvline(x=0, color='k', linewidth=0.5, linestyle='--')
ax4.set_xlabel('Eigenvalue')
ax4.set_ylabel('PW Shell Cutoff L')
ax4.set_title('Eigenvalue Spectrum at Each Shell')
ax4.set_yticks(L_values)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's63_shell_hessian.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {png_path}")

# =============================================================================
# 17. Final Summary
# =============================================================================
print("\n" + "=" * 78)
print("  SHELL-HESSIAN-63: FINAL SUMMARY")
print("=" * 78)
print(f"  Gate: SHELL-HESSIAN-63 = {gate_verdict}")
print(f"  PW levels: L = 0, 1, 2, 3  (max_pq_sum = 3)")
print(f"  Total modes: {int(cum_modes[-1])}")
print(f"  Eigenvalue sign at each shell:")
for i, L_cut in enumerate(L_values):
    print(f"    L={L_cut}: {n_positive_flow[i]}+, {n_negative_flow[i]}-")
print(f"  Zero crossings: {n_zero_cross}")
print(f"  Monotone eigenvalues: {monotone_count}/36")
print(f"  Total time: {t_total:.1f}s")
print("=" * 78)
