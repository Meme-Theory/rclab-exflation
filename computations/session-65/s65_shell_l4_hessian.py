#!/usr/bin/env python3
"""
s65_shell_l4_hessian.py — SHELL-L4-65: L_max=4 Shell Hessian UV Convergence Test
==================================================================================
Gate: SHELL-L4-65
  PASS: ||H^{(4)}||_F / ||H^{(3)}||_F < 1.0  (convergent)
  FAIL: ratio > 2.0  (divergent)
  INFO: 1.0 < ratio < 2.0  (marginal)

Motivation:
  S64 SHELL-HESSIAN-64 found L=3 contributes 79.9% of the total one-loop Hessian.
  The per-shell Frobenius norm scales approximately as L^{2.5}:
    L=0: 2.42,  L=1: 36.58,  L=2: 252.91,  L=3: 1160.39
  If this growth continues, L=4 would add ~2.6x the L=3 contribution, implying
  the one-loop Hessian sum diverges in the UV. This would invalidate the
  fold stability result and all downstream predictions (n_s, Sakharov coupling).

Method:
  1. Load L<=3 data from S64 (tree-level Hessian, per-irrep one-loop Hessians).
  2. Construct L=4 SU(3) irreps: (4,0), (3,1), (2,2), (1,3), (0,4).
     - (4,0): Sym^4(fund), dim=15
     - (0,4): Sym^4(anti-fund), dim=15
     - (3,1): from (3,0)x(0,1) Casimir projection, dim=24
     - (1,3): from (0,3)x(1,0) Casimir projection, dim=24
     - (2,2): from (2,0)x(0,2) Casimir projection, dim=27
  3. For each new irrep, compute D_K eigenvalues on the fold metric.
  4. Build per-irrep one-loop Hessian via finite differences (same method as S64).
  5. Compute ||H^{(4)}||_F and compare to ||H^{(3)}||_F from S64.
  6. If convergent, compute corrected total Hessian eigenvalues with L=4 included.

Key physics:
  The one-loop effective potential is V_eff = V_tree + (1/64pi^2) Tr[M^4(ln M^2/mu^2 - 3/2)].
  For the spectral action, the one-loop correction decomposes shell-by-shell in the
  Peter-Weyl expansion. UV convergence requires the per-shell contribution to DECREASE
  for large L, which is guaranteed if the spectral zeta function zeta_D(s) converges
  for Re(s) > dim(K)/2 = 4 (since K = SU(3) has dimension 8). The Hessian is the
  second derivative of the spectral action, so it inherits this convergence if
  the spectral action itself converges — but the RATE of convergence determines
  whether L_max=3 truncation is adequate.

Author: Landau-Condensed-Matter-Theorist (Session 65, Wave 3)
"""

import sys
import os
import time
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from numpy import exp, sqrt, log, pi
from numpy.linalg import eigh, cholesky, inv, norm, eigvalsh
from itertools import permutations, combinations_with_replacement
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI, E_B1, E_B2_mean, E_B3_mean,
    S_fold, d2S_fold, a0_fold, a2_fold, a4_fold
)

print("=" * 78)
print("  SHELL-L4-65: L_max=4 Shell Hessian — UV Convergence Test")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

t_global_start = time.time()

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (same as S64)
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
# 2. Frame, Connection, Dirac Operator (same as S64)
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
# 3. Irrep Construction — Extended to L=4
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

def irrep_symmetric_n(base_gens, n):
    """Build the (n,0) [or (0,n) if base_gens are conjugate] irrep via Sym^n."""
    dim_V = base_gens[0].shape[0]
    dim_total = dim_V ** n
    I_V = np.eye(dim_V, dtype=complex)

    # Action on tensor product
    rho_tensor = []
    for X in base_gens:
        M = np.zeros((dim_total, dim_total), dtype=complex)
        for k in range(n):
            factors = [I_V] * n
            factors[k] = X
            term = factors[0]
            for f in factors[1:]:
                term = np.kron(term, f)
            M += term
        rho_tensor.append(M)

    # Symmetric subspace projector
    sorted_indices = list(combinations_with_replacement(range(dim_V), n))
    dim_sym = len(sorted_indices)

    sym_vecs = []
    for idx in sorted_indices:
        v = np.zeros(dim_total, dtype=complex)
        perms = set(permutations(idx))
        norm_val = np.sqrt(len(perms))
        for p in perms:
            flat_idx = 0
            for k, i in enumerate(p):
                flat_idx += i * (dim_V ** (n - 1 - k))
            v[flat_idx] = 1.0 / norm_val
        sym_vecs.append(v)

    P = np.column_stack(sym_vecs)
    rho = [P.conj().T @ M @ P for M in rho_tensor]
    return rho, dim_sym

def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    """Extract irrep of given dimension from tensor product via Casimir eigenvalue."""
    dim_A = rho_A[0].shape[0]
    dim_B = rho_B[0].shape[0]
    dim_prod = dim_A * dim_B

    rho_prod = []
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    for a in range(8):
        rho_a = (np.kron(rho_A[a], np.eye(dim_B, dtype=complex)) +
                 np.kron(np.eye(dim_A, dtype=complex), rho_B[a]))
        rho_prod.append(rho_a)
        C2 += rho_a @ rho_a

    evals, evecs = np.linalg.eigh(C2)
    tol = 1e-6  # (local)

    # Group eigenvalues
    groups = []
    sorted_pairs = sorted(zip(evals, range(dim_prod)))
    for val, idx in sorted_pairs:
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

def build_l4_irreps(gens, f_abc):
    """Build all 5 L=4 irreps of SU(3).

    Returns list of (p, q, dim_pq, rho_matrices) sorted by (p,q).
    Tensor product decompositions used:
      (4,0): Sym^4(fund),           dim=15
      (3,1): (3,0) x (0,1),         dim=24  [(3,1)+(2,0)=24+6]
      (2,2): (2,0) x (0,2),         dim=27  [(2,2)+(1,1)+(0,0)=27+8+1]
      (1,3): (0,3) x (1,0),         dim=24  [(1,3)+(0,2)=24+6]
      (0,4): Sym^4(anti-fund),      dim=15
    """
    conj_gens = [-g.T for g in gens]
    irreps = []

    # (4,0): Sym^4(fund)
    rho_40, dim_40 = irrep_symmetric_n(gens, 4)
    assert dim_40 == 15
    irreps.append((4, 0, 15, rho_40))

    # (0,4): Sym^4(anti-fund)
    rho_04, dim_04 = irrep_symmetric_n(conj_gens, 4)
    assert dim_04 == 15
    irreps.append((0, 4, 15, rho_04))

    # (3,1) from (3,0) x (0,1)
    rho_30, _ = irrep_symmetric_n(gens, 3)
    rho_01 = [g.copy() for g in conj_gens]
    rho_31 = irrep_via_casimir_projection(rho_30, rho_01, 24, (3, 1))
    irreps.append((3, 1, 24, rho_31))

    # (1,3) from (0,3) x (1,0)
    rho_03, _ = irrep_symmetric_n(conj_gens, 3)
    rho_10 = [g.copy() for g in gens]
    rho_13 = irrep_via_casimir_projection(rho_03, rho_10, 24, (1, 3))
    irreps.append((1, 3, 24, rho_13))

    # (2,2) from (2,0) x (0,2)
    rho_20, _ = irrep_symmetric_n(gens, 2)
    rho_02, _ = irrep_symmetric_n(conj_gens, 2)
    rho_22 = irrep_via_casimir_projection(rho_20, rho_02, 27, (2, 2))
    irreps.append((2, 2, 27, rho_22))

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

# Build L=4 irreps
print("  Building L=4 irreps...")
l4_irreps = build_l4_irreps(gens, f_abc)

# Validate Casimir eigenvalues
def c2_expected(p, q):
    """Expected C2 = -(p^2+q^2+pq+3p+3q)/3 for anti-Hermitian generators."""
    return -(p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

print("\n  L=4 irrep validation:")
for (p, q, dim_rho, rho) in l4_irreps:
    C2 = sum(r @ r for r in rho)
    evals_C2 = np.linalg.eigvalsh(C2)
    c2_exp = c2_expected(p, q)
    c2_err = max(abs(evals_C2.min() - c2_exp), abs(evals_C2.max() - c2_exp))
    n_evals = dim_rho * dim_rho * 16
    print(f"    ({p},{q}): dim={dim_rho:>2}, C2={evals_C2[0]:.6f} (exp={c2_exp:.6f}), "
          f"err={c2_err:.2e}, Dirac dim={dim_rho*16}")

# =============================================================================
# 6. Load S64 Data
# =============================================================================
print("\n--- 3. Loading S64 shell Hessian data ---")

s64_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's64_shell_hessian.npz')
s64_data = np.load(s64_path, allow_pickle=True)

H_1loop_total_L3 = s64_data['H_1loop_total']
H_tree_eigenbasis = s64_data['H_tree_eigenbasis']
evals_tree = s64_data['evals_tree']
evecs_tree = s64_data['evecs_tree']
g_fold = s64_data['g_fold']
Lambda_sq = float(s64_data['Lambda_sq'])
eps_s64 = float(s64_data['epsilon'])

# S64 per-shell Frobenius norms for comparison
irrep_L_s64 = s64_data['irrep_L']
H_1loop_irreps_s64 = s64_data['H_1loop_irreps']
shell_frob_s64 = {}
for L_val in range(4):
    mask = irrep_L_s64 == L_val
    if np.any(mask):
        H_shell = np.sum(H_1loop_irreps_s64[mask], axis=0)
        shell_frob_s64[L_val] = np.sqrt(np.sum(H_shell**2))
    else:
        shell_frob_s64[L_val] = 0.0

total_frob_L3 = np.sqrt(np.sum(H_1loop_total_L3**2))

print(f"  H_tree (eigenbasis) shape: {H_tree_eigenbasis.shape}")
print(f"  Tree eigenvalues: min={evals_tree[0]:.4f}, max={evals_tree[-1]:.4f}")
print(f"  S64 total ||H_1loop||_F = {total_frob_L3:.4f}")
print(f"  S64 per-shell Frobenius norms:")
for L_val in range(4):
    frac = shell_frob_s64[L_val] / total_frob_L3 * 100
    print(f"    L={L_val}: {shell_frob_s64[L_val]:>12.4f} ({frac:>5.1f}%)")

# Load tree-level data (need perturbation matrices)
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

eps = eps_s64  # Same epsilon as S64 for consistency
print(f"  Perturbation epsilon = {eps} (same as S64)")
print(f"  36 directions in Sym(8) tree-eigenbasis")

# =============================================================================
# 8. Compute L=4 Per-Irrep One-Loop Hessian
# =============================================================================
print("\n--- 5. Computing L=4 per-irrep one-loop Hessian ---")

n_l4 = len(l4_irreps)
total_dirac_evals = n_l4 * (36 * 2 + 630 * 2 + 1)
print(f"  {n_l4} irreps, total Dirac diagonalizations: ~{total_dirac_evals}")
print(f"  Irrep dimensions: {[(p,q,d) for (p,q,d,_) in l4_irreps]}")
print(f"  Largest Dirac matrix: {max(d for (_,_,d,_) in l4_irreps)*16}x{max(d for (_,_,d,_) in l4_irreps)*16}")

# Step 1: Per-irrep eigenvalues at the fold
print("\n  Computing eigenvalues at fold metric...")
irrep_evals_center = compute_dirac_evals_per_irrep(g_fold, gens, f_abc, gammas, l4_irreps)

# Per-irrep one-loop action at center
S1_irrep_center = {}
for (p, q, dim_rho, rho) in l4_irreps:
    key = (p, q)
    S1_irrep_center[key] = oneloop_action_from_evals(irrep_evals_center[key])

print("\n  Per-irrep one-loop action at fold:")
for (p, q, dim_rho, _) in l4_irreps:
    n_modes = dim_rho * dim_rho * 16
    print(f"    ({p},{q}): S_1loop = {S1_irrep_center[(p,q)]:>12.4f}  ({n_modes} modes)")

# Step 2: Storage for per-irrep Hessian
H_1loop_l4 = {}
for (p, q, _, _) in l4_irreps:
    H_1loop_l4[(p,q)] = np.zeros((36, 36))

# Pre-compute perturbed actions
S1_irrep_plus = {}
S1_irrep_minus = {}
for (p, q, _, _) in l4_irreps:
    S1_irrep_plus[(p,q)] = np.zeros(36)
    S1_irrep_minus[(p,q)] = np.zeros(36)

# Step 3: Diagonal Hessian elements
print("\n  Phase 1: Diagonal (36 perturbations)...")
t_phase1_start = time.time()

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    evals_plus = compute_dirac_evals_per_irrep(g_plus, gens, f_abc, gammas, l4_irreps)
    evals_minus = compute_dirac_evals_per_irrep(g_minus, gens, f_abc, gammas, l4_irreps)

    for (p, q, _, _) in l4_irreps:
        key = (p, q)
        S1_irrep_plus[key][a] = oneloop_action_from_evals(evals_plus[key])
        S1_irrep_minus[key][a] = oneloop_action_from_evals(evals_minus[key])

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_phase1_start
        rate = (a+1) / elapsed if elapsed > 0 else 1
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"    Direction {a+1}/36 ({elapsed:.1f}s, ~{remaining:.0f}s left)")

# Compute diagonal elements
d2S1_irrep = {}
for (p, q, _, _) in l4_irreps:
    key = (p, q)
    d2S1_irrep[key] = (S1_irrep_plus[key] - 2.0 * S1_irrep_center[key] + S1_irrep_minus[key]) / eps**2
    H_1loop_l4[key][np.diag_indices(36)] = d2S1_irrep[key]

t_phase1_end = time.time()
print(f"  Phase 1 complete: {t_phase1_end - t_phase1_start:.1f}s")

# Diagonal summary
print("\n  Per-irrep diagonal (mean, min, max):")
for (p, q, _, _) in l4_irreps:
    d = d2S1_irrep[(p,q)]
    print(f"    ({p},{q}): mean={np.mean(d):>12.2f}, min={np.min(d):>12.2f}, max={np.max(d):>12.2f}")

# Step 4: Off-diagonal via polarization identity
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
            for (p, q, _, _) in l4_irreps:
                H_1loop_l4[(p,q)][a, b] = 0.0
                H_1loop_l4[(p,q)][b, a] = 0.0
            n_done += 1
            n_skipped += 1
            continue

        evals_plus = compute_dirac_evals_per_irrep(g_plus, gens, f_abc, gammas, l4_irreps)
        evals_minus = compute_dirac_evals_per_irrep(g_minus, gens, f_abc, gammas, l4_irreps)

        for (p, q, _, _) in l4_irreps:
            key = (p, q)
            S1_sum_plus = oneloop_action_from_evals(evals_plus[key])
            S1_sum_minus = oneloop_action_from_evals(evals_minus[key])
            d2S1_sum = (S1_sum_plus - 2.0 * S1_irrep_center[key] + S1_sum_minus) / eps**2
            H_1loop_l4[key][a, b] = 0.5 * (d2S1_sum - d2S1_irrep[key][a] - d2S1_irrep[key][b])
            H_1loop_l4[key][b, a] = H_1loop_l4[key][a, b]

        n_done += 1
        if n_done % 50 == 0:
            elapsed = time.time() - t_phase2_start
            rate = n_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs - n_done) / rate if rate > 0 else 0
            print(f"    Pairs: {n_done}/{n_pairs} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase2_end = time.time()
print(f"  Phase 2 complete: {t_phase2_end - t_phase2_start:.1f}s ({n_skipped} pairs skipped)")

# Symmetry check
print("\n  Per-irrep Hessian symmetry errors:")
for (p, q, _, _) in l4_irreps:
    key = (p, q)
    sym_err = np.max(np.abs(H_1loop_l4[key] - H_1loop_l4[key].T))
    frob = np.sqrt(np.sum(H_1loop_l4[key]**2))
    print(f"    ({p},{q}): sym_err = {sym_err:.2e}, ||H||_F = {frob:.4f}")

# =============================================================================
# 9. Shell Analysis: L=4 vs L=3
# =============================================================================
print("\n--- 6. Shell analysis ---")

# L=4 shell Hessian (sum of all L=4 irreps)
H_1loop_L4_shell = np.zeros((36, 36))
for (p, q, _, _) in l4_irreps:
    H_1loop_L4_shell += H_1loop_l4[(p,q)]

frob_L4 = np.sqrt(np.sum(H_1loop_L4_shell**2))
frob_L3 = shell_frob_s64[3]

ratio_L4_L3 = frob_L4 / frob_L3

print(f"\n  Per-irrep Frobenius norms (L=4):")
for (p, q, _, _) in l4_irreps:
    frob = np.sqrt(np.sum(H_1loop_l4[(p,q)]**2))
    print(f"    ({p},{q}): ||H||_F = {frob:>12.4f}")

print(f"\n  L=4 shell: ||H^(4)||_F = {frob_L4:.4f}")
print(f"  L=3 shell: ||H^(3)||_F = {frob_L3:.4f}")
print(f"  Ratio ||H^(4)||_F / ||H^(3)||_F = {ratio_L4_L3:.6f}")

# Full per-shell scaling table
print(f"\n  Per-shell Frobenius norm scaling:")
print(f"  {'L':>3} {'||H^(L)||_F':>14} {'ratio to L-1':>14} {'L^2.5':>10}")
prev_frob = None
for L_val in range(5):
    if L_val < 4:
        frob = shell_frob_s64[L_val]
    else:
        frob = frob_L4
    ratio_str = f"{frob/prev_frob:.4f}" if prev_frob is not None and prev_frob > 0 else "---"
    l_power = L_val**2.5 if L_val > 0 else 0
    print(f"  {L_val:>3} {frob:>14.4f} {ratio_str:>14} {l_power:>10.2f}")
    prev_frob = frob

# =============================================================================
# 10. Corrected Hessian with L=4 Included
# =============================================================================
print("\n--- 7. Corrected Hessian eigenvalues ---")

# Total one-loop with L=4
H_1loop_total_L4 = H_1loop_total_L3 + H_1loop_L4_shell

# Full effective Hessian at L_max=4
H_eff_L3 = H_tree_eigenbasis + H_1loop_total_L3
H_eff_L4 = H_tree_eigenbasis + H_1loop_total_L4

evals_L3 = np.sort(eigvalsh(H_eff_L3))
evals_L4 = np.sort(eigvalsh(H_eff_L4))

n_pos_L3 = np.sum(evals_L3 > 0)
n_neg_L3 = 36 - n_pos_L3
n_pos_L4 = np.sum(evals_L4 > 0)
n_neg_L4 = 36 - n_pos_L4

print(f"\n  H_eff(L_max=3): {n_pos_L3} positive, {n_neg_L3} negative")
print(f"    min = {evals_L3[0]:.4f}, max = {evals_L3[-1]:.4f}")
print(f"  H_eff(L_max=4): {n_pos_L4} positive, {n_neg_L4} negative")
print(f"    min = {evals_L4[0]:.4f}, max = {evals_L4[-1]:.4f}")

# Signature comparison
sig_L3 = f"({n_pos_L3}+, {n_neg_L3}-)"
sig_L4 = f"({n_pos_L4}+, {n_neg_L4}-)"
signature_changed = (n_pos_L3 != n_pos_L4)

print(f"\n  Signature L_max=3: {sig_L3}")
print(f"  Signature L_max=4: {sig_L4}")
print(f"  Signature changed: {signature_changed}")

# Eigenvalue-by-eigenvalue comparison
print(f"\n  Eigenvalue comparison (L3 vs L4):")
print(f"  {'idx':>4} {'eval_L3':>14} {'eval_L4':>14} {'delta':>14} {'delta/|L3|':>12}")
for k in range(36):
    delta = evals_L4[k] - evals_L3[k]
    rel = abs(delta / evals_L3[k]) if abs(evals_L3[k]) > 1e-10 else float('inf')
    sign_L3 = "+" if evals_L3[k] > 0 else "-"
    sign_L4 = "+" if evals_L4[k] > 0 else "-"
    print(f"  {k:>4} {evals_L3[k]:>13.4f}{sign_L3} {evals_L4[k]:>13.4f}{sign_L4} "
          f"{delta:>14.4f} {rel:>12.4f}")

# =============================================================================
# 11. Convergence Analysis
# =============================================================================
print("\n--- 8. UV convergence analysis ---")

# Frobenius norms as function of L
frobs = [shell_frob_s64.get(L, 0.0) for L in range(4)] + [frob_L4]
Ls = [0, 1, 2, 3, 4]

# Fit power law: ||H^(L)||_F ~ A * L^alpha for L >= 1
from numpy.polynomial import polynomial as P_fit
# log-log fit
Ls_fit = np.array([1, 2, 3, 4], dtype=float)
frobs_fit = np.array([frobs[1], frobs[2], frobs[3], frobs[4]])
log_L = np.log(Ls_fit)
log_F = np.log(frobs_fit)
coeffs = np.polyfit(log_L, log_F, 1)
alpha_fit = coeffs[0]
A_fit = np.exp(coeffs[1])

print(f"  Power-law fit: ||H^(L)||_F ~ {A_fit:.2f} * L^{alpha_fit:.3f}")
print(f"  Fitted values:")
for i, L in enumerate(Ls_fit):
    predicted = A_fit * L**alpha_fit
    actual = frobs_fit[i]
    print(f"    L={int(L)}: actual={actual:.4f}, fit={predicted:.4f}, ratio={actual/predicted:.4f}")

# Theoretical expectation: for dim(K)=8, the spectral zeta function converges
# for Re(s) > 4. The one-loop correction involves zeta_D(2), which converges.
# Per-shell contribution scales as:
#   sum_{(p,q): p+q=L} dim(p,q)^2 * (L*(L+3)/[eigenvalue scale])
# The number of modes per shell grows polynomially, but eigenvalues grow linearly
# in L, so the net contribution should scale as L^{dim-1} / L^{2s} ~ L^{7-2s}.
# For s=2: L^3. For s=4: L^{-1}. The Hessian involves second derivatives of
# zeta_D(s) at s where it converges.

# Check if the series is consistent with an exponential cutoff
# Try fit: ||H^(L)||_F ~ B * L^beta * exp(-gamma * L)
# log(F/L^beta) = log(B) - gamma*L
# Try beta = 3 (polynomial from density of states)
for beta in [2, 2.5, 3, 3.5, 4]:
    y = np.log(frobs_fit / Ls_fit**beta)
    coeffs_exp = np.polyfit(Ls_fit, y, 1)
    gamma = -coeffs_exp[0]
    B = np.exp(coeffs_exp[1])
    residual = np.std(y - np.polyval(coeffs_exp, Ls_fit))
    print(f"  Exponential fit (beta={beta:.1f}): B={B:.2f}, gamma={gamma:.4f}, "
          f"residual={residual:.4f}")

# Ratio test
print(f"\n  Ratio test (consecutive shells):")
for i in range(1, len(frobs)):
    if frobs[i-1] > 0:
        r = frobs[i] / frobs[i-1]
        print(f"    ||H^({i})||_F / ||H^({i-1})||_F = {r:.4f}")

# Cumulative sum
print(f"\n  Cumulative Frobenius norm:")
cumulative = 0
for L_val in range(5):
    cumulative += frobs[L_val]
    frac_of_total = cumulative / sum(frobs) * 100
    print(f"    L=0..{L_val}: {cumulative:.4f} ({frac_of_total:.1f}%)")

# =============================================================================
# 12. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: SHELL-L4-65")
print("=" * 78)

print(f"\n  ||H^(4)||_F / ||H^(3)||_F = {ratio_L4_L3:.6f}")
print(f"  Gate criterion: PASS < 1.0, INFO in [1.0, 2.0], FAIL > 2.0")

if ratio_L4_L3 < 1.0:
    gate_verdict = "PASS"
    print(f"\n  VERDICT: PASS")
    print(f"  L=4 shell contribution DECREASES relative to L=3.")
    print(f"  One-loop Hessian is UV-convergent. L_max=3 truncation is adequate.")
    print(f"  The (8+, 27-) signature is robust against UV completion.")
elif ratio_L4_L3 <= 2.0:
    gate_verdict = "INFO"
    print(f"\n  VERDICT: INFO")
    print(f"  L=4 shell contribution is comparable to L=3 (marginal convergence).")
    print(f"  One-loop Hessian may require L_max >= 5 for quantitative accuracy.")
    print(f"  Signature stability requires further investigation.")
else:
    gate_verdict = "FAIL"
    print(f"\n  VERDICT: FAIL")
    print(f"  L=4 shell contribution EXCEEDS L=3 by more than 2x.")
    print(f"  One-loop Hessian diverges in the UV. L_max=3 truncation is INADEQUATE.")
    print(f"  Fold stability and all downstream predictions are UV-sensitive.")

print(f"\n  Signature at L_max=3: {sig_L3}")
print(f"  Signature at L_max=4: {sig_L4}")
print(f"  Signature change: {signature_changed}")
print(f"  Power-law exponent: alpha = {alpha_fit:.3f}")

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 13. Save Data
# =============================================================================
print("\n--- 9. Saving results ---")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's65_shell_l4_hessian.npz')

l4_keys_ordered = [(p, q) for (p, q, _, _) in l4_irreps]
H_1loop_l4_arr = np.stack([H_1loop_l4[key] for key in l4_keys_ordered], axis=0)

np.savez(out_path,
    # Gate
    gate_name='SHELL-L4-65',
    gate_verdict=gate_verdict,
    # L=4 irrep structure
    l4_irrep_pq=np.array(l4_keys_ordered),
    l4_irrep_dims=np.array([d for (_, _, d, _) in l4_irreps]),
    # Per-irrep L=4 Hessians
    H_1loop_l4_irreps=H_1loop_l4_arr,
    H_1loop_L4_shell=H_1loop_L4_shell,
    # Full effective Hessians
    H_eff_L3=H_eff_L3,
    H_eff_L4=H_eff_L4,
    evals_L3=evals_L3,
    evals_L4=evals_L4,
    # Norms
    frob_L4_shell=frob_L4,
    frob_L3_shell=frob_L3,
    ratio_L4_L3=ratio_L4_L3,
    # Shell scaling
    shell_frobs=np.array(frobs),
    alpha_fit=alpha_fit,
    # Signature
    n_pos_L3=n_pos_L3,
    n_neg_L3=n_neg_L3,
    n_pos_L4=n_pos_L4,
    n_neg_L4=n_neg_L4,
    signature_changed=signature_changed,
    # Parameters
    epsilon=eps,
    tau_fold=tau_fold,
    g_fold=g_fold,
    total_time=t_total,
)
print(f"  Saved: {out_path}")

# =============================================================================
# 14. Visualization
# =============================================================================
print("\n--- 10. Generating visualization ---")

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle(r'SHELL-L4-65: $L_{\max}=4$ Shell Hessian — UV Convergence Test'
             f'\nGate: {gate_verdict} | '
             r'$\|H^{(4)}\|_F / \|H^{(3)}\|_F$'
             f' = {ratio_L4_L3:.4f}',
             fontsize=13, fontweight='bold')

# --- Panel 1: Per-shell Frobenius norm ---
ax1 = axes[0, 0]
L_vals = np.arange(5)
frob_vals = np.array(frobs)
colors_bar = ['C0', 'C1', 'C2', 'C3', 'C4']
bars = ax1.bar(L_vals, frob_vals, color=colors_bar, alpha=0.8, edgecolor='black', linewidth=0.5)

# Overlay power-law fit
L_fine = np.linspace(0.5, 4.5, 100)
fit_line = A_fit * L_fine**alpha_fit
ax1.plot(L_fine, fit_line, 'k--', linewidth=1.5,
         label=rf'Fit: ${A_fit:.1f} \cdot L^{{{alpha_fit:.2f}}}$')

for i, (lv, fv) in enumerate(zip(L_vals, frob_vals)):
    ax1.text(lv, fv * 1.02, f'{fv:.1f}', ha='center', va='bottom', fontsize=9)

ax1.set_xlabel('PW shell $L = p+q$', fontsize=11)
ax1.set_ylabel(r'$\|H_{1\mathrm{loop}}^{(L)}\|_F$', fontsize=11)
ax1.set_title('Per-Shell One-Loop Hessian Norm', fontsize=11)
ax1.set_xticks(L_vals)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')

# --- Panel 2: Ratio test ---
ax2 = axes[0, 1]
ratios = [frobs[i]/frobs[i-1] for i in range(1, 5) if frobs[i-1] > 0]
ratio_labels = [f'L={i}/L={i-1}' for i in range(1, 5)]
ax2.bar(range(len(ratios)), ratios, color=['C1', 'C2', 'C3', 'C4'], alpha=0.8,
        edgecolor='black', linewidth=0.5)
ax2.axhline(y=1.0, color='green', linewidth=2, linestyle='--', label='Convergent threshold')
ax2.axhline(y=2.0, color='red', linewidth=2, linestyle='--', label='Divergent threshold')
for i, r in enumerate(ratios):
    ax2.text(i, r * 1.02, f'{r:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.set_xticks(range(len(ratios)))
ax2.set_xticklabels(ratio_labels, fontsize=10)
ax2.set_ylabel(r'$\|H^{(L)}\|_F / \|H^{(L-1)}\|_F$', fontsize=11)
ax2.set_title('Consecutive Shell Ratio (Convergence Test)', fontsize=11)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Eigenvalue spectrum comparison ---
ax3 = axes[1, 0]
idx = np.arange(36)
width = 0.35  # (local)
ax3.barh(idx - width/2, evals_L3, height=width, color='C0', alpha=0.7, label=r'$L_{\max}=3$')
ax3.barh(idx + width/2, evals_L4, height=width, color='C3', alpha=0.7, label=r'$L_{\max}=4$')
ax3.axvline(x=0, color='k', linewidth=1.0, linestyle='--')
ax3.set_xlabel('Eigenvalue of $H_{eff}$', fontsize=11)
ax3.set_ylabel('Eigenvalue index', fontsize=11)
ax3.set_title(r'Hessian Eigenvalue Spectrum: $L_{\max}=3$ vs $L_{\max}=4$', fontsize=11)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

# --- Panel 4: Per-irrep L=4 contributions ---
ax4 = axes[1, 1]
l4_labels = [f'({p},{q})' for (p, q, _, _) in l4_irreps]
l4_frobs = [np.sqrt(np.sum(H_1loop_l4[(p,q)]**2)) for (p, q, _, _) in l4_irreps]
ax4.bar(range(len(l4_labels)), l4_frobs, color='C4', alpha=0.8,
        edgecolor='black', linewidth=0.5)
for i, (lab, fv) in enumerate(zip(l4_labels, l4_frobs)):
    dim = l4_irreps[i][2]
    ax4.text(i, fv * 1.02, f'd={dim}\n{fv:.1f}', ha='center', va='bottom', fontsize=8)
ax4.set_xticks(range(len(l4_labels)))
ax4.set_xticklabels(l4_labels, fontsize=10)
ax4.set_xlabel('L=4 Irrep $(p,q)$', fontsize=11)
ax4.set_ylabel(r'$\|H_{1\mathrm{loop}}^{(p,q)}\|_F$', fontsize=11)
ax4.set_title('Per-Irrep Contributions at $L=4$', fontsize=11)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's65_shell_l4_hessian.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {png_path}")

# =============================================================================
# 15. Final Summary
# =============================================================================
print("\n" + "=" * 78)
print("  SHELL-L4-65: FINAL SUMMARY")
print("=" * 78)
print(f"  Gate: SHELL-L4-65 = {gate_verdict}")
print(f"  ||H^(4)||_F = {frob_L4:.4f}")
print(f"  ||H^(3)||_F = {frob_L3:.4f}")
print(f"  Ratio = {ratio_L4_L3:.6f}")
print(f"  Power-law fit: alpha = {alpha_fit:.3f}")
print(f"  Signature L3: {sig_L3}, L4: {sig_L4}")
print(f"  Signature changed: {signature_changed}")
print(f"  Total time: {t_total:.1f}s")

# Print per-shell table for easy copy-paste
print(f"\n  Shell scaling table:")
print(f"  {'L':>3} {'||H^(L)||_F':>14} {'cumulative':>14} {'%total':>8}")
cum = 0
total = sum(frobs)
for L_val in range(5):
    cum += frobs[L_val]
    pct = cum / total * 100
    print(f"  {L_val:>3} {frobs[L_val]:>14.4f} {cum:>14.4f} {pct:>7.1f}%")

print("\n" + "=" * 78)
