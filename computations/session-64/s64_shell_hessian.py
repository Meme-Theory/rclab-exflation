#!/usr/bin/env python3
"""
s64_shell_hessian.py — SHELL-HESSIAN-64: FRG Shell-by-Shell Hessian Decimation
================================================================================
Gate: SHELL-HESSIAN-64
  PASS if all 36 eigenvalues of H_eff remain positive at EVERY decimation step.
  FAIL if any eigenvalue crosses zero during multiplet removal.

Method (FRG decimation, UV -> IR):
  1. Start with the FULL effective Hessian (all PW multiplets included):
       H_eff = H_tree + sum_{(p,q)} H_1loop^{(p,q)}
     where all 36 eigenvalues are POSITIVE (verified S63).

  2. Remove the highest PW multiplets one at a time, ordered by the PW level
     L = p+q (UV to IR). Within the same L, ordered by descending dim(p,q).

  3. At each removal step, recompute the effective Hessian:
       H_eff^{(k)} = H_tree + sum_{remaining irreps} H_1loop^{(p,q)}
     and diagonalize to get all 36 eigenvalues.

  4. Track eigenvalue trajectories and zero crossings through 9 removal steps
     (leaving only the singlet (0,0)).

Physical interpretation:
  This is the FRG flow in the PW cutoff direction. Each removal step corresponds
  to lowering the FRG regulator from L_max to L_max - 1, etc. If eigenvalues
  remain positive throughout, the fold stability is UV-robust: it does not depend
  on the specific UV completion. If eigenvalues cross zero, fold stability requires
  specific UV modes -- the landscape topology changes with the cutoff.

  The nuclear DFT analog (Strutinsky): removing shells from a self-consistent
  mean-field potential tests whether the nuclear binding is a bulk property or
  depends on specific shell structure. Here, each PW irrep is a nuclear j-shell.

Key insight from S63:
  The IR-to-UV direction showed ALL eigenvalues negative until L=3 was included.
  The UV dominance is extreme: L=3 alone provides the positive-definiteness.
  Decimation from the top tests whether removing sub-components of L=3 creates
  instabilities, and whether intermediate stages (L=3 partially included) are stable.

Irrep ordering (UV to IR removal):
  Step 0: Full spectrum (all 10 irreps) -- baseline
  Step 1: Remove (3,0) dim=10
  Step 2: Remove (2,1) dim=15
  Step 3: Remove (1,2) dim=15
  Step 4: Remove (0,3) dim=10  -- L=3 shell fully removed
  Step 5: Remove (2,0) dim=6
  Step 6: Remove (1,1) dim=8
  Step 7: Remove (0,2) dim=6   -- L=2 shell fully removed
  Step 8: Remove (1,0) dim=3
  Step 9: Remove (0,1) dim=3   -- L=1 shell fully removed, only (0,0) remains

Author: gen-physicist (Session 64, Wave 7)
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
print("  SHELL-HESSIAN-64: FRG Shell-by-Shell Hessian Decimation")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure
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
# 2. Frame, Connection, Dirac Operator
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
# 3. Irrep Construction
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

def build_irrep_list(gens, f_abc, max_pq_sum=3):
    """Returns list of (p, q, dim_pq, rho_matrices) for ALL irreps up to p+q <= max_pq_sum."""
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
# 4. Per-Irrep Eigenvalue Computation
# =============================================================================

def compute_geometric_data(g_metric, gens, f_abc, gammas):
    """Compute orthonormal frame, connection, and spinor connection for a metric."""
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return E, Omega

def compute_dirac_evals_per_irrep(g_metric, gens, f_abc, gammas, irreps_data):
    """Compute D_K eigenvalues per individual (p,q) irrep.

    Returns dict: irrep_evals[(p,q)] = array of eigenvalues (with degeneracy).
    """
    E, Omega = compute_geometric_data(g_metric, gens, f_abc, gammas)
    irrep_evals = {}
    for (p, q, dim_rho, rho) in irreps_data:
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = -1j * D
        evals = eigvalsh(iD)
        # Each eigenvalue has dim_rho degeneracy from the PW expansion
        evals_with_deg = np.repeat(evals, dim_rho)
        irrep_evals[(p,q)] = evals_with_deg
    return irrep_evals

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

# Build irreps
print("  Building irreps (max p+q = 3)...")
irreps_data = build_irrep_list(gens, f_abc, max_pq_sum=3)

# Enumerate and order irreps for decimation (UV to IR)
# Order: within same L, descending dim_pq. Between shells, descending L.
irrep_info = []
for (p, q, dim_pq, rho) in irreps_data:
    L = p + q
    n_evals = dim_pq * 16  # Dirac block size (before degeneracy repeat)
    n_evals_with_deg = dim_pq * dim_pq * 16  # After degeneracy repeat
    irrep_info.append({
        'p': p, 'q': q, 'dim': dim_pq, 'L': L,
        'n_evals': n_evals_with_deg, 'label': f'({p},{q})'
    })

# Sort for UV-to-IR removal: highest L first, within same L by descending dim
irrep_info.sort(key=lambda x: (-x['L'], -x['dim']))

print("\n  Irrep decimation order (UV -> IR removal):")
print(f"  {'Step':>4} {'Remove':>8} {'dim':>4} {'L':>3} {'#evals':>8} {'Remaining':>10}")
print("  " + "-" * 45)
remaining_evals = sum(info['n_evals'] for info in irrep_info)
print(f"  {0:>4} {'(none)':>8} {'':>4} {'':>3} {'':>8} {remaining_evals:>10}")
for step, info in enumerate(irrep_info[:-1], 1):  # Don't remove the singlet
    remaining_evals -= info['n_evals']
    print(f"  {step:>4} {info['label']:>8} {info['dim']:>4} {info['L']:>3} "
          f"{info['n_evals']:>8} {remaining_evals:>10}")

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
print(f"  Tree eigenvalues: min={evals_tree[0]:.4f}, max={evals_tree[-1]:.4f}")
print(f"  All negative: {np.all(evals_tree < 0)}")

# =============================================================================
# 7. Build Sym(8) Basis and Perturbation Matrices
# =============================================================================
print("\n--- 4. Perturbation infrastructure ---")

basis_sym8 = []
for i in range(8):
    M = np.zeros((8,8))
    M[i,i] = 1.0
    basis_sym8.append(M)
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8,8))
        M[i,j] = 1.0 / sqrt(2.0)
        M[j,i] = 1.0 / sqrt(2.0)
        basis_sym8.append(M)
assert len(basis_sym8) == 36

perturbation_matrices = []
for a in range(36):
    Delta_a = np.zeros((8, 8))
    for k in range(36):
        Delta_a += evecs_tree[k, a] * basis_sym8[k]
    perturbation_matrices.append(Delta_a)

# =============================================================================
# 8. Compute Per-Irrep One-Loop Hessian
# =============================================================================
print("\n--- 5. Computing per-irrep one-loop Hessian (this is the main computation) ---")
print(f"  10 irreps x (36 diagonal + 630 off-diagonal) = 6,660 Dirac evaluations")

eps = 0.001  # Same as S63
print(f"  Perturbation epsilon = {eps}")

# Step 1: Compute per-irrep eigenvalues at the fold
irrep_evals_center = compute_dirac_evals_per_irrep(g_fold, gens, f_abc, gammas, irreps_data)

# Per-irrep one-loop action at center
S1_irrep_center = {}
for (p, q, dim_rho, rho) in irreps_data:
    key = (p, q)
    S1_irrep_center[key] = oneloop_action_from_evals(irrep_evals_center[key])

print("\n  Per-irrep one-loop action at fold:")
for info in irrep_info:
    key = (info['p'], info['q'])
    print(f"    {info['label']}: S_1loop = {S1_irrep_center[key]:>12.4f}  ({info['n_evals']} modes)")

S1_total = sum(S1_irrep_center.values())
print(f"  Total S_1loop: {S1_total:.4f}")

# Step 2: Per-irrep Hessian via finite differences
# H_1loop^{(p,q)}[a,b] built from per-irrep one-loop actions at perturbed metrics

# Storage: one 36x36 matrix per irrep
H_1loop_irrep = {}
for (p, q, _, _) in irreps_data:
    H_1loop_irrep[(p,q)] = np.zeros((36, 36))

# Pre-compute per-irrep actions at +/- epsilon along each of the 36 directions
S1_irrep_plus = {}   # S1_irrep_plus[(p,q)][a]
S1_irrep_minus = {}
for (p, q, _, _) in irreps_data:
    S1_irrep_plus[(p,q)] = np.zeros(36)
    S1_irrep_minus[(p,q)] = np.zeros(36)

print("\n  Phase 1: Diagonal (36 perturbations)...")
t_phase1_start = time.time()

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    # Compute per-irrep eigenvalues at perturbed metrics
    evals_plus = compute_dirac_evals_per_irrep(g_plus, gens, f_abc, gammas, irreps_data)
    evals_minus = compute_dirac_evals_per_irrep(g_minus, gens, f_abc, gammas, irreps_data)

    for (p, q, _, _) in irreps_data:
        key = (p, q)
        S1_irrep_plus[key][a] = oneloop_action_from_evals(evals_plus[key])
        S1_irrep_minus[key][a] = oneloop_action_from_evals(evals_minus[key])

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_phase1_start
        rate = (a+1) / elapsed if elapsed > 0 else 1
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"    Direction {a+1}/36 ({elapsed:.1f}s, ~{remaining:.0f}s left)")

# Compute per-irrep diagonal Hessian elements
d2S1_irrep = {}
for (p, q, _, _) in irreps_data:
    key = (p, q)
    d2S1_irrep[key] = (S1_irrep_plus[key] - 2.0 * S1_irrep_center[key] + S1_irrep_minus[key]) / eps**2
    H_1loop_irrep[key][np.diag_indices(36)] = d2S1_irrep[key]

t_phase1_end = time.time()
print(f"  Phase 1 complete: {t_phase1_end - t_phase1_start:.1f}s")

# Per-irrep diagonal summary
print("\n  Per-irrep diagonal Hessian (mean, min, max):")
for info in irrep_info:
    key = (info['p'], info['q'])
    d = d2S1_irrep[key]
    print(f"    {info['label']}: mean={np.mean(d):>12.2f}, "
          f"min={np.min(d):>12.2f}, max={np.max(d):>12.2f}")

# Cross-check: sum of per-irrep diagonals should match S63 per-shell diagonals
print("\n  Cross-check: per-irrep sum vs S63 per-shell:")
for L in range(4):
    d_sum = sum(d2S1_irrep[(p,q)] for (p,q,_,_) in irreps_data if p+q == L)
    print(f"    L={L}: irrep-sum mean = {np.mean(d_sum):>12.4f}")

# Step 3: Off-diagonal Hessian via polarization identity
print("\n  Phase 2: Off-diagonal (630 pairs)...")
t_phase2_start = time.time()

n_pairs = 36 * 35 // 2
n_done = 0  # (local)
n_skipped = 0  # (local)

for a in range(36):
    for b in range(a+1, 36):
        Delta_sum = perturbation_matrices[a] + perturbation_matrices[b]
        g_plus = g_fold + eps * Delta_sum
        g_minus = g_fold - eps * Delta_sum

        # Check positive definiteness
        if eigvalsh(g_plus)[0] < 0 or eigvalsh(g_minus)[0] < 0:
            for (p, q, _, _) in irreps_data:
                H_1loop_irrep[(p,q)][a, b] = 0.0
                H_1loop_irrep[(p,q)][b, a] = 0.0
            n_done += 1
            n_skipped += 1
            continue

        evals_plus = compute_dirac_evals_per_irrep(g_plus, gens, f_abc, gammas, irreps_data)
        evals_minus = compute_dirac_evals_per_irrep(g_minus, gens, f_abc, gammas, irreps_data)

        for (p, q, _, _) in irreps_data:
            key = (p, q)
            S1_sum_plus = oneloop_action_from_evals(evals_plus[key])
            S1_sum_minus = oneloop_action_from_evals(evals_minus[key])
            d2S1_sum = (S1_sum_plus - 2.0 * S1_irrep_center[key] + S1_sum_minus) / eps**2
            H_1loop_irrep[key][a, b] = 0.5 * (d2S1_sum - d2S1_irrep[key][a] - d2S1_irrep[key][b])
            H_1loop_irrep[key][b, a] = H_1loop_irrep[key][a, b]

        n_done += 1
        if n_done % 50 == 0:
            elapsed = time.time() - t_phase2_start
            rate = n_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs - n_done) / rate if rate > 0 else 0
            print(f"    Pairs: {n_done}/{n_pairs} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase2_end = time.time()
print(f"  Phase 2 complete: {t_phase2_end - t_phase2_start:.1f}s ({n_skipped} pairs skipped)")

# Symmetry check per irrep
print("\n  Per-irrep Hessian symmetry errors:")
for info in irrep_info:
    key = (info['p'], info['q'])
    sym_err = np.max(np.abs(H_1loop_irrep[key] - H_1loop_irrep[key].T))
    frob = np.sqrt(np.sum(H_1loop_irrep[key]**2))
    print(f"    {info['label']}: sym_err = {sym_err:.2e}, ||H||_F = {frob:.4f}")

# =============================================================================
# 9. FRG Decimation: Remove Multiplets UV -> IR
# =============================================================================
print("\n--- 6. FRG decimation (UV -> IR) ---")
print("  Starting from full H_eff, removing multiplets one at a time")

H_tree_eigenbasis = np.diag(evals_tree)

# Compute the full H_1loop (sum of all irreps)
H_1loop_total = np.zeros((36, 36))
for (p, q, _, _) in irreps_data:
    H_1loop_total += H_1loop_irrep[(p,q)]

# Full effective Hessian (step 0)
H_eff_full = H_tree_eigenbasis + H_1loop_total
evals_full = eigvalsh(H_eff_full)
print(f"\n  Step 0 (full): all eigenvalues positive = {np.all(evals_full > 0)}")
print(f"    min = {evals_full[0]:.4f}, max = {evals_full[-1]:.4f}")

# Verify against S63 final result
s63_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's63_shell_hessian.npz')
if os.path.exists(s63_path):
    s63_data = np.load(s63_path, allow_pickle=True)
    s63_evals_final = s63_data['evals_flow'][-1, :]  # L=3 (full)
    max_deviation = np.max(np.abs(np.sort(evals_full) - np.sort(s63_evals_final)))
    print(f"    Cross-check vs S63 full: max|delta| = {max_deviation:.4f}")

# Decimation loop
n_steps = len(irrep_info)  # 10 irreps, step 0 = all, steps 1..9 = remove one each
evals_flow = np.zeros((n_steps, 36))
evals_flow[0, :] = np.sort(evals_full)

# Track what's removed at each step
removed_at_step = [None]  # Step 0: nothing removed
H_1loop_current = H_1loop_total.copy()

print(f"\n  {'Step':>4} {'Remove':>8} {'L':>3} {'n_pos':>6} {'n_neg':>6} "
      f"{'min_eval':>14} {'max_eval':>14} {'gap_ratio':>12}")
print("  " + "-" * 82)

n_pos = np.sum(evals_full > 0)
n_neg = 36 - n_pos
gap_ratio = evals_full[0] / evals_full[-1] if evals_full[-1] != 0 else 0
print(f"  {0:>4} {'(full)':>8} {'-':>3} {n_pos:>6} {n_neg:>6} "
      f"{evals_full[0]:>14.4f} {evals_full[-1]:>14.4f} {gap_ratio:>12.6f}")

zero_crossings = []  # (step, eigenvalue_index, value)

for step in range(1, n_steps):
    # Remove the (step-1)-th irrep in the UV-to-IR order
    # But skip the last one (singlet) -- we remove 9, leaving 1
    if step > 9:
        break

    info = irrep_info[step - 1]
    key = (info['p'], info['q'])
    removed_at_step.append(info['label'])

    # Subtract this irrep's contribution
    H_1loop_current = H_1loop_current - H_1loop_irrep[key]

    # New effective Hessian
    H_eff = H_tree_eigenbasis + H_1loop_current
    evals_eff = np.sort(eigvalsh(H_eff))
    evals_flow[step, :] = evals_eff

    n_pos = np.sum(evals_eff > 0)
    n_neg = 36 - n_pos
    gap_ratio = evals_eff[0] / evals_eff[-1] if evals_eff[-1] != 0 else 0

    print(f"  {step:>4} {info['label']:>8} {info['L']:>3} {n_pos:>6} {n_neg:>6} "
          f"{evals_eff[0]:>14.4f} {evals_eff[-1]:>14.4f} {gap_ratio:>12.6f}")

    # Track zero crossings
    for k in range(36):
        if evals_flow[step-1, k] * evals_flow[step, k] < 0:
            zero_crossings.append((step, k, evals_flow[step, k]))

# =============================================================================
# 10. Detailed Eigenvalue Flow Table
# =============================================================================
print("\n--- 7. Detailed eigenvalue flow ---")

actual_steps = min(n_steps, 10)
header = f"  {'idx':>3}"
for s in range(actual_steps):
    if s == 0:
        header += f"  {'Full':>14}"
    else:
        header += f"  {removed_at_step[s]:>14}"
print(header)
print("  " + "-" * (3 + 16 * actual_steps))

for k in range(36):
    line = f"  {k:>3}"
    for s in range(actual_steps):
        sign = "+" if evals_flow[s, k] > 0 else "-"
        line += f"  {evals_flow[s, k]:>13.4f}{sign}"
    print(line)

# =============================================================================
# 11. FRG Flow Analysis
# =============================================================================
print("\n--- 8. FRG flow analysis ---")

# Track where eigenvalues first go negative
first_negative_step = {}
for k in range(36):
    for s in range(actual_steps):
        if evals_flow[s, k] <= 0:
            first_negative_step[k] = s
            break

if first_negative_step:
    print(f"\n  Eigenvalues that become negative:")
    for k, s in sorted(first_negative_step.items()):
        if s == 0:
            continue  # Skip if already negative at start
        info = irrep_info[s - 1]
        print(f"    ev[{k}]: first negative at step {s} (after removing {info['label']})")

# Monotonicity check: do eigenvalues decrease monotonically during decimation?
monotone_count = 0  # (local)
for k in range(36):
    if np.all(np.diff(evals_flow[:actual_steps, k]) <= 1e-10):
        monotone_count += 1
print(f"\n  Monotonically DECREASING eigenvalues: {monotone_count}/36")
print(f"  (Expected: all should decrease as positive UV corrections are removed)")

# Per-irrep contribution fractions
print(f"\n  Per-irrep contribution to total one-loop ||H||_F:")
total_frob = np.sqrt(np.sum(H_1loop_total**2))
for info in irrep_info:
    key = (info['p'], info['q'])
    frob = np.sqrt(np.sum(H_1loop_irrep[key]**2))
    frac = frob / total_frob * 100
    print(f"    {info['label']} (L={info['L']}): ||H||_F = {frob:>12.4f} ({frac:>6.2f}%)")

# Cumulative fraction after each removal
print(f"\n  Cumulative remaining ||H_1loop||_F after removal:")
H_rem = H_1loop_total.copy()
for step in range(1, actual_steps):
    info = irrep_info[step - 1]
    key = (info['p'], info['q'])
    H_rem = H_rem - H_1loop_irrep[key]
    frob_rem = np.sqrt(np.sum(H_rem**2))
    frac_rem = frob_rem / total_frob * 100
    print(f"    Step {step} (removed {info['label']}): remaining = {frob_rem:>12.4f} ({frac_rem:>6.2f}%)")

# =============================================================================
# 12. Critical Scale: Where Does Topology Change?
# =============================================================================
print("\n--- 9. Critical scale identification ---")

# Find the step where the minimum eigenvalue crosses zero
critical_step = None
for s in range(1, actual_steps):
    if evals_flow[s, 0] <= 0 and evals_flow[s-1, 0] > 0:
        critical_step = s
        break

if critical_step is not None:
    info_crit = irrep_info[critical_step - 1]
    print(f"  CRITICAL SCALE: Step {critical_step}, removing {info_crit['label']} (L={info_crit['L']})")
    print(f"  Minimum eigenvalue jumps from {evals_flow[critical_step-1, 0]:.4f} "
          f"to {evals_flow[critical_step, 0]:.4f}")
    print(f"  Landscape topology change: fold gains unstable directions")

    # How many eigenvalues flip at this step?
    n_flip = sum(1 for k in range(36)
                 if evals_flow[critical_step-1, k] > 0 and evals_flow[critical_step, k] <= 0)
    print(f"  Number of eigenvalues flipping: {n_flip}/36")
else:
    print(f"  No critical scale found: all eigenvalues remain positive throughout decimation")

# Percentage of L=3 contribution needed for stability
if any(info['L'] == 3 for info in irrep_info):
    L3_irreps = [(info['p'], info['q']) for info in irrep_info if info['L'] == 3]
    L3_total_frob = np.sqrt(np.sum(sum(H_1loop_irrep[key] for key in L3_irreps)**2))
    L3_frac = L3_total_frob / total_frob * 100
    print(f"\n  L=3 shell total: {L3_frac:.1f}% of one-loop Hessian")
    print(f"  L=3 contains: {', '.join(f'({p},{q})' for p,q in L3_irreps)}")

# =============================================================================
# 13. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: SHELL-HESSIAN-64")
print("=" * 78)

all_positive_throughout = True
for s in range(actual_steps):
    if np.any(evals_flow[s, :] <= 0):
        all_positive_throughout = False
        break

if all_positive_throughout:
    gate_verdict = "PASS"
    print(f"  VERDICT: PASS")
    print(f"  All 36 eigenvalues remain positive through ALL 9 multiplet removals")
    print(f"  Fold stability is UV-robust under FRG decimation")
    print(f"  Zero crossings: {len(zero_crossings)}")
else:
    gate_verdict = "FAIL"
    # Find first step with any negative eigenvalue (after step 0)
    fail_step = None
    for s in range(1, actual_steps):
        if np.any(evals_flow[s, :] <= 0):
            fail_step = s
            break

    if fail_step is not None:
        info_fail = irrep_info[fail_step - 1]
        n_neg = np.sum(evals_flow[fail_step, :] <= 0)
        print(f"  VERDICT: FAIL")
        print(f"  First failure at step {fail_step}: after removing {info_fail['label']} (L={info_fail['L']})")
        print(f"  {n_neg}/36 eigenvalues negative at that step")
        print(f"  Fold stability REQUIRES UV modes above L={info_fail['L']}")
        print(f"  Zero crossings: {len(zero_crossings)}")
    else:
        # Already negative at step 0 — would indicate S63 inconsistency
        print(f"  VERDICT: FAIL (eigenvalues already negative at full spectrum)")

# Additional diagnostic: at what step do we lose more than half the eigenvalues?
for s in range(actual_steps):
    n_neg = np.sum(evals_flow[s, :] <= 0)
    if n_neg > 18:
        print(f"\n  Majority negative at step {s}: {n_neg}/36 eigenvalues negative")
        break

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 14. Save Data
# =============================================================================
print("\n--- 10. Saving results ---")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's64_shell_hessian.npz')

# Stack per-irrep Hessians in decimation order
irrep_keys_ordered = [(info['p'], info['q']) for info in irrep_info]
H_1loop_irreps_arr = np.stack([H_1loop_irrep[key] for key in irrep_keys_ordered], axis=0)

np.savez(out_path,
    # Gate info
    gate_name='SHELL-HESSIAN-64',
    gate_verdict=gate_verdict,
    # Irrep structure
    irrep_pq=np.array(irrep_keys_ordered),
    irrep_dims=np.array([info['dim'] for info in irrep_info]),
    irrep_L=np.array([info['L'] for info in irrep_info]),
    irrep_n_evals=np.array([info['n_evals'] for info in irrep_info]),
    # Eigenvalue flow through decimation
    evals_flow=evals_flow[:actual_steps],
    n_steps=actual_steps,
    # Per-irrep Hessians (in decimation order)
    H_1loop_irreps=H_1loop_irreps_arr,
    # Total one-loop and tree
    H_1loop_total=H_1loop_total,
    H_tree_eigenbasis=H_tree_eigenbasis,
    evals_tree=evals_tree,
    evecs_tree=evecs_tree,
    # Full effective Hessian
    H_eff_full=H_eff_full,
    # Zero crossings
    n_zero_crossings=len(zero_crossings),
    zero_crossings=np.array(zero_crossings) if zero_crossings else np.array([]).reshape(0,3),
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
# 15. Visualization
# =============================================================================
print("\n--- 11. Generating visualization ---")

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('SHELL-HESSIAN-64: FRG Decimation of Fold Hessian (UV $\\to$ IR)',
             fontsize=14, fontweight='bold')

# Panel 1: Full eigenvalue flow through decimation
ax1 = axes[0, 0]
steps = np.arange(actual_steps)
for k in range(36):
    color = 'C0' if evals_flow[-1, k] > 0 else 'C3'
    ax1.plot(steps, evals_flow[:actual_steps, k], 'o-', color=color,
             markersize=3, alpha=0.5, linewidth=0.8)
ax1.axhline(y=0, color='k', linewidth=1.0, linestyle='--')
step_labels = ['Full'] + [irrep_info[s]['label'] for s in range(actual_steps - 1)]
ax1.set_xticks(steps)
ax1.set_xticklabels(step_labels, rotation=45, ha='right', fontsize=8)
ax1.set_xlabel('Decimation Step (irrep removed)', fontsize=10)
ax1.set_ylabel('Eigenvalue of $H_{eff}$', fontsize=10)
ax1.set_title('FRG Flow: All 36 Eigenvalues', fontsize=11)
ax1.grid(True, alpha=0.3)

# Panel 2: Minimum eigenvalue trajectory
ax2 = axes[0, 1]
min_evals = evals_flow[:actual_steps, 0]
max_evals = evals_flow[:actual_steps, -1]
ax2.plot(steps, min_evals, 'rs-', markersize=8, linewidth=2, label=r'$\lambda_{\min}$')
ax2.plot(steps, max_evals, 'bs-', markersize=8, linewidth=2, label=r'$\lambda_{\max}$')
ax2.axhline(y=0, color='k', linewidth=1.0, linestyle='--')
ax2.set_xticks(steps)
ax2.set_xticklabels(step_labels, rotation=45, ha='right', fontsize=8)
ax2.set_xlabel('Decimation Step', fontsize=10)
ax2.set_ylabel('Eigenvalue', fontsize=10)
ax2.set_title('Extremal Eigenvalues vs Decimation', fontsize=11)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Panel 3: Per-irrep Frobenius contribution (bar chart)
ax3 = axes[1, 0]
frob_per_irrep = [np.sqrt(np.sum(H_1loop_irrep[(info['p'], info['q'])]**2))
                  for info in irrep_info]
labels_bar = [info['label'] for info in irrep_info]
colors_bar = [f'C{info["L"]}' for info in irrep_info]
ax3.bar(range(len(irrep_info)), frob_per_irrep, color=colors_bar, alpha=0.8)
ax3.set_xticks(range(len(irrep_info)))
ax3.set_xticklabels(labels_bar, rotation=45, ha='right', fontsize=9)
ax3.set_xlabel('Irrep $(p,q)$', fontsize=10)
ax3.set_ylabel(r'$\|H_{1loop}^{(p,q)}\|_F$', fontsize=10)
ax3.set_title('Per-Irrep One-Loop Hessian Strength', fontsize=11)
ax3.grid(True, alpha=0.3)
# Add L labels
for i, info in enumerate(irrep_info):
    ax3.text(i, frob_per_irrep[i] * 1.02, f'L={info["L"]}',
             ha='center', va='bottom', fontsize=7, color=colors_bar[i])

# Panel 4: Eigenvalue spectrum at selected steps (stem plot)
ax4 = axes[1, 1]
show_steps = [0, 4, 7, 9] if actual_steps >= 10 else list(range(actual_steps))
show_steps = [s for s in show_steps if s < actual_steps]
offsets = np.linspace(-0.3, 0.3, len(show_steps))
for i, s in enumerate(show_steps):
    evals_s = evals_flow[s, :]
    pos_mask = evals_s > 0
    neg_mask = ~pos_mask
    if s == 0:
        label = 'Full'
    else:
        label = f'Step {s}'
    ax4.scatter(evals_s[pos_mask], np.ones(np.sum(pos_mask)) * (i + 0.05),
                color='C0', s=20, alpha=0.7, zorder=3)
    ax4.scatter(evals_s[neg_mask], np.ones(np.sum(neg_mask)) * (i + 0.05),
                color='C3', s=20, alpha=0.7, zorder=3, marker='x')
ax4.axvline(x=0, color='k', linewidth=1.0, linestyle='--')
ax4.set_yticks(range(len(show_steps)))
y_labels_4 = []
for s in show_steps:
    if s == 0:
        y_labels_4.append('Full (all)')
    elif s <= 4:
        y_labels_4.append(f'Step {s} ($-$L=3)')
    elif s <= 7:
        y_labels_4.append(f'Step {s} ($-$L$\\leq$2)')
    else:
        y_labels_4.append(f'Step {s} ($-$L$\\leq$1)')
ax4.set_yticklabels(y_labels_4, fontsize=9)
ax4.set_xlabel('Eigenvalue', fontsize=10)
ax4.set_title('Spectrum at Selected Decimation Steps', fontsize=11)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's64_shell_hessian.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {png_path}")

# =============================================================================
# 16. Final Summary
# =============================================================================
print("\n" + "=" * 78)
print("  SHELL-HESSIAN-64: FINAL SUMMARY")
print("=" * 78)
print(f"  Gate: SHELL-HESSIAN-64 = {gate_verdict}")
print(f"  Multiplets: 10 irreps, 9 removed (UV -> IR)")
print(f"  Decimation order: {' -> '.join(info['label'] for info in irrep_info)}")
print(f"  Zero crossings: {len(zero_crossings)}")
print(f"  Total computation time: {t_total:.1f}s")

# Summary table
print(f"\n  Summary Table:")
print(f"  {'Step':>4} {'Irrep':>8} {'L':>3} {'Action':>10} {'n+':>4} {'n-':>4} "
      f"{'lambda_min':>14} {'lambda_max':>14}")
print("  " + "-" * 68)
for s in range(actual_steps):
    if s == 0:
        label = '(full)'
        action = 'baseline'
        L_val = '-'
    else:
        label = removed_at_step[s]
        action = 'removed'
        L_val = str(irrep_info[s-1]['L'])
    n_p = np.sum(evals_flow[s, :] > 0)
    n_n = 36 - n_p
    print(f"  {s:>4} {label:>8} {L_val:>3} {action:>10} {n_p:>4} {n_n:>4} "
          f"{evals_flow[s, 0]:>14.4f} {evals_flow[s, -1]:>14.4f}")

print("\n  [END SHELL-HESSIAN-64]")
