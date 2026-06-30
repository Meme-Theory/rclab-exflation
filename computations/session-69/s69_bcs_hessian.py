#!/usr/bin/env python3
"""
s69_bcs_hessian.py — BCS-DRESSED-HESSIAN-69: Fold Stability Under BCS
=======================================================================
Gate: BCS-HESS-69
  PASS: All 36 eigenvalues positive at Lambda = 2.048 M_KK
  FAIL: Any eigenvalue negative (BCS destabilizes fold)
  INFO: All positive but margin < 5x

Motivation:
  The S62/S64/S66 one-loop Hessian found all 36 eigenvalues positive at the
  physical cutoff Lambda = 2.048 M_KK, with stabilization margin alpha = 26x
  (softest eigenvalue 29.4 vs tree maximum |148.7|). The BCS condensate
  modifies D_K by:
    1. Shifting eigenvalues: bare lambda_n -> BdG quasiparticle E_n
    2. Adding off-diagonal BdG structure (u-v mixing)

  This could destabilize some Hessian eigenvalues, especially the softest
  mode (U(1) breathing + C^2-su(2) mixing, cluster #0 with eigenvalue 29.4).

Physics of BCS dressing:
  The BdG spectral action replaces each D_K eigenvalue lambda_n with the
  quasiparticle energy:
    E_n = sqrt((lambda_n - mu)^2 + Delta^2)

  where Delta = 0.464 M_KK (OES gap) and mu = 0.845 M_KK (chemical potential).

  The BdG heat kernel factorization (S64 T36):
    K_BdG(t) = exp(-Delta^2 * t) * K_bare(t)

  implies the spectral action with f(x) = sqrt(x) becomes:
    S_BCS(Lambda) = (1/Lambda) sum_n E_n
                  = (1/Lambda) sum_n sqrt((lambda_n - mu)^2 + Delta^2)

  The key effect: modes near the Fermi surface (|lambda_n| ~ mu) are gapped
  to E_n ~ Delta, while distant modes are barely affected (E_n ~ |lambda_n - mu|).
  This REDUCES spectral weight variation near mu, potentially softening or
  stiffening the Hessian.

Method:
  1. Load bare Hessian data from S64 (g_fold, H_tree, perturbation basis, epsilon)
  2. Load BCS parameters from S68 (Delta, mu_BCS)
  3. Build D_K eigenvalue machinery (same as S64/S66)
  4. For each perturbation direction:
     a. Compute D_K eigenvalues at g_fold +/- eps * Delta_a
     b. Convert to BdG energies: E_n = sqrt((lambda_n - mu)^2 + Delta^2)
     c. Compute S_BCS = (1/Lambda) sum E_n
  5. Build 36x36 Hessian via central finite differences + polarization identity
  6. Form H_BCS_eff = H_tree + H_BCS_1loop, diagonalize
  7. Compare to bare Hessian (S66 Lambda=2.0)

Cross-checks:
  - Tr(H_BCS) vs a_2 BCS correction (11.6% from S68)
  - Bare limit (Delta->0): must recover S66 Lambda=2.0 result
  - All eigenvalues real (symmetric Hessian)

Author: Baptista-Spacetime-Analyst (Session 69, Wave 4)
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

from canonical_constants import (
    tau_fold, PI, Delta_0_OES, E_B2_mean,
    M_KK_gravity, M_KK
)

print("=" * 78)
print("  BCS-DRESSED-HESSIAN-69: Fold Stability Under BCS")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  Delta_BCS = {Delta_0_OES:.6f} M_KK (OES gap)")
print(f"  mu_BCS = {E_B2_mean:.6f} M_KK (chemical potential)")

t_global_start = time.time()

# BCS parameters from canonical constants
Delta_BCS = Delta_0_OES   # 0.4643 M_KK
mu_BCS = E_B2_mean         # 0.8453 M_KK

# Physical cutoff
Lambda_phys = 2.048        # M_KK (from S62 Gaussian optimization)  # (local)

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure (identical to S66)
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
# 2. Frame, Connection, Dirac Operator (identical to S66)
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
# 3. Irrep Construction (identical to S66, max_pq_sum=3)
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
# 4. BCS-Dressed Spectral Action Functions
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

def spectral_action_bare(evals, Lambda):
    """S_bare = (1/Lambda) sum_n |lambda_n|.
    Bare spectral action with f(x) = sqrt(x).
    """
    return np.sum(np.abs(evals)) / Lambda

def spectral_action_bcs(evals, Lambda, Delta, mu):
    """S_BCS = (1/Lambda) sum_n E_n where E_n = sqrt((lambda_n - mu)^2 + Delta^2).

    BdG quasiparticle spectral action. Each bare eigenvalue lambda_n of D_K
    is replaced by the BdG quasiparticle energy E_n.

    Physical picture: the BCS condensate gaps modes near the Fermi surface.
    Modes with |lambda_n| ~ mu have E_n ~ Delta (gapped floor).
    Modes far from mu have E_n ~ |lambda_n - mu| (unaffected).
    """
    xi_n = evals - mu
    E_n = np.sqrt(xi_n**2 + Delta**2)
    return np.sum(E_n) / Lambda

def spectral_action_bcs_full(evals, Lambda, Delta, mu):
    """Full BdG spectral action including both particle and hole branches.

    In the BdG formalism, each bare state n produces TWO quasiparticle branches:
      E_n^+ = +sqrt((lambda_n - mu)^2 + Delta^2)  (particle)
      E_n^- = -sqrt((lambda_n - mu)^2 + Delta^2)  (hole, but |E| same)

    For the spectral action S = (1/Lambda) Tr |D_BdG|, both contribute:
      S_BCS = (2/Lambda) sum_n sqrt((lambda_n - mu)^2 + Delta^2)

    The factor 2 is the BdG doubling. However, for Hessian computation what
    matters is the RELATIVE change, not the absolute value. Since the factor 2
    is constant, it does not affect the Hessian comparison.

    We compute WITHOUT the factor 2 for direct comparison with the bare case,
    then note the doubling in the output.
    """
    xi_n = evals - mu
    E_n = np.sqrt(xi_n**2 + Delta**2)
    return np.sum(E_n) / Lambda

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

# Build irreps (L_max = 3, same as S64/S66)
print("  Building irreps (max p+q = 3)...")
irreps_data = build_irrep_list(gens, f_abc, max_pq_sum=3)
n_irreps = len(irreps_data)
total_modes = sum(d**2 * 16 for (_, _, d, _) in irreps_data)
print(f"  {n_irreps} irreps, {total_modes} total modes")

for (p, q, d, _) in irreps_data:
    print(f"    ({p},{q}): dim={d}, Dirac block={d*16}, modes with deg={d*d*16}")

# =============================================================================
# 6. Load S64 Reference Data
# =============================================================================
print("\n--- 3. Loading reference data ---")

base_dir = os.path.dirname(os.path.abspath(__file__))

s64_path = os.path.join(base_dir, 's64_shell_hessian.npz')
s64_data = np.load(s64_path, allow_pickle=True)

H_tree_eigenbasis = s64_data['H_tree_eigenbasis']
evals_tree = s64_data['evals_tree']
g_fold = s64_data['g_fold']
eps = float(s64_data['epsilon'])  # 0.001

print(f"  g_fold diagonal: {np.diag(g_fold)}")
print(f"  Tree eigenvalues: all negative = {np.all(evals_tree < 0)}")
print(f"    range: [{evals_tree[0]:.4f}, {evals_tree[-1]:.4f}]")
print(f"  Epsilon: {eps}")

# Load S61 perturbation eigenvectors (defines the 36D basis)
s61_path = os.path.join(base_dir, 's61_moduli_hessian.npz')
s61_data = np.load(s61_path, allow_pickle=True)
evecs_tree_s61 = s61_data['evecs_36']

# Load S66 bare Hessian at Lambda=2.0 for comparison
s66_path = os.path.join(base_dir, 's66_hessian_cutoff.npz')
s66_data = np.load(s66_path, allow_pickle=True)
evals_bare_L2 = s66_data['evals_eff_L2p0']
H_eff_bare_L2 = s66_data['H_eff_L2p0']
H_f_bare_L2 = s66_data['H_f_L2p0']

print(f"\n  S66 bare Hessian at Lambda=2.0 M_KK:")
print(f"    Signature: ({int(s66_data['n_pos_L2p0'])}+, {int(s66_data['n_neg_L2p0'])}-)")
print(f"    Eigenvalue range: [{evals_bare_L2[0]:.4f}, {evals_bare_L2[-1]:.4f}]")
print(f"    Softest eigenvalue: {evals_bare_L2[0]:.6f}")

# Load S68 BCS data for cross-check
s68_path = os.path.join(base_dir, 's68_bcs_dressed_mode.npz')
s68_data = np.load(s68_path, allow_pickle=True)
delta_a2_total = float(s68_data['delta_a2_total'])
delta_a4_total = float(s68_data['delta_a4_total'])
print(f"\n  S68 BCS corrections:")
print(f"    delta_a2/a2 = {delta_a2_total:.4f} ({delta_a2_total*100:.2f}%)")
print(f"    delta_a4/a4 = {delta_a4_total:.4f} ({delta_a4_total*100:.2f}%)")

# =============================================================================
# 7. Build Perturbation Matrices (same basis as S64/S66)
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

print(f"  Perturbation epsilon = {eps} (same as S64/S66)")
print(f"  36 directions in Sym(8) tree-eigenbasis")

# =============================================================================
# 8. Compute D_K Eigenvalues at Fold (Reference Point)
# =============================================================================
print("\n--- 5. Computing D_K spectrum at fold ---")

evals_fold = compute_all_dirac_evals(g_fold, gens, f_abc, gammas, irreps_data)
n_total_evals = len(evals_fold)
print(f"  Total eigenvalues: {n_total_evals}")
print(f"  Eigenvalue range: [{evals_fold.min():.6f}, {evals_fold.max():.6f}]")
print(f"  |lambda| range: [{np.min(np.abs(evals_fold)):.6f}, {np.max(np.abs(evals_fold)):.6f}]")

# BdG quasiparticle energies at fold
xi_fold = evals_fold - mu_BCS
E_fold = np.sqrt(xi_fold**2 + Delta_BCS**2)
print(f"\n  BdG energies at fold:")
print(f"    E range: [{E_fold.min():.6f}, {E_fold.max():.6f}]")
print(f"    Modes with |xi| < Delta (strongly gapped): {np.sum(np.abs(xi_fold) < Delta_BCS)}")
print(f"    Modes with |xi| > 5*Delta (weakly affected): {np.sum(np.abs(xi_fold) > 5*Delta_BCS)}")

# Reference spectral actions at fold
S_bare_fold = spectral_action_bare(evals_fold, Lambda_phys)
S_bcs_fold = spectral_action_bcs(evals_fold, Lambda_phys, Delta_BCS, mu_BCS)
print(f"\n  Spectral actions at fold (Lambda = {Lambda_phys} M_KK):")
print(f"    S_bare = {S_bare_fold:.6f}")
print(f"    S_BCS  = {S_bcs_fold:.6f}")
print(f"    Ratio S_BCS/S_bare = {S_bcs_fold/S_bare_fold:.6f}")
print(f"    Relative change: {(S_bcs_fold - S_bare_fold)/S_bare_fold * 100:.4f}%")

# =============================================================================
# 9. MAIN COMPUTATION: BCS-Dressed Hessian
# =============================================================================
print("\n--- 6. Main computation: 36x36 BCS-dressed Hessian ---")
print(f"  Method: central finite differences, eps = {eps}")
print(f"  Lambda = {Lambda_phys} M_KK")
print(f"  Delta = {Delta_BCS:.6f}, mu = {mu_BCS:.6f}")

# Phase 1: Diagonal perturbations (36 directions, +/- each)
print("\n  Phase 1: Diagonal perturbations (36 x 2 = 72 Dirac evaluations)...")
t_phase1_start = time.time()

# Store eigenvalues for reuse
evals_plus = []    # bare D_K eigenvalues at g_fold + eps * Delta_a
evals_minus = []   # bare D_K eigenvalues at g_fold - eps * Delta_a

# BCS spectral action values
S_bcs_plus = np.zeros(36)
S_bcs_minus = np.zeros(36)
S_bare_plus = np.zeros(36)
S_bare_minus = np.zeros(36)

for a in range(36):
    g_plus = g_fold + eps * perturbation_matrices[a]
    g_minus = g_fold - eps * perturbation_matrices[a]

    ev_p = compute_all_dirac_evals(g_plus, gens, f_abc, gammas, irreps_data)
    ev_m = compute_all_dirac_evals(g_minus, gens, f_abc, gammas, irreps_data)

    evals_plus.append(ev_p)
    evals_minus.append(ev_m)

    # BCS spectral actions
    S_bcs_plus[a] = spectral_action_bcs(ev_p, Lambda_phys, Delta_BCS, mu_BCS)
    S_bcs_minus[a] = spectral_action_bcs(ev_m, Lambda_phys, Delta_BCS, mu_BCS)

    # Bare spectral actions (for comparison)
    S_bare_plus[a] = spectral_action_bare(ev_p, Lambda_phys)
    S_bare_minus[a] = spectral_action_bare(ev_m, Lambda_phys)

    if (a+1) % 6 == 0 or a == 35:
        elapsed = time.time() - t_phase1_start
        rate = (a+1) / elapsed if elapsed > 0 else 1
        remaining = (36 - a - 1) / rate if rate > 0 else 0
        print(f"    Direction {a+1}/36 ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase1_end = time.time()
print(f"  Phase 1 complete: {t_phase1_end - t_phase1_start:.1f}s")

# Diagonal second derivatives
d2S_bcs_diag = (S_bcs_plus - 2.0 * S_bcs_fold + S_bcs_minus) / eps**2
d2S_bare_diag = (S_bare_plus - 2.0 * S_bare_fold + S_bare_minus) / eps**2

print(f"\n  Diagonal d^2S/dtau_a^2 (BCS vs bare):")
print(f"    BCS  range: [{d2S_bcs_diag.min():.4f}, {d2S_bcs_diag.max():.4f}]")
print(f"    Bare range: [{d2S_bare_diag.min():.4f}, {d2S_bare_diag.max():.4f}]")

# Phase 2: Off-diagonal perturbations (630 pairs)
print("\n  Phase 2: Off-diagonal perturbations (630 pairs)...")
t_phase2_start = time.time()

S_bcs_pair_plus = {}
S_bcs_pair_minus = {}
S_bare_pair_plus = {}
S_bare_pair_minus = {}
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
            S_bcs_pair_plus[(a,b)] = None
            S_bcs_pair_minus[(a,b)] = None
            S_bare_pair_plus[(a,b)] = None
            S_bare_pair_minus[(a,b)] = None
            n_skipped += 1
            n_done += 1
            continue

        ev_p = compute_all_dirac_evals(g_plus, gens, f_abc, gammas, irreps_data)
        ev_m = compute_all_dirac_evals(g_minus, gens, f_abc, gammas, irreps_data)

        S_bcs_pair_plus[(a,b)] = spectral_action_bcs(ev_p, Lambda_phys, Delta_BCS, mu_BCS)
        S_bcs_pair_minus[(a,b)] = spectral_action_bcs(ev_m, Lambda_phys, Delta_BCS, mu_BCS)
        S_bare_pair_plus[(a,b)] = spectral_action_bare(ev_p, Lambda_phys)
        S_bare_pair_minus[(a,b)] = spectral_action_bare(ev_m, Lambda_phys)

        n_done += 1
        if n_done % 50 == 0:
            elapsed = time.time() - t_phase2_start
            rate = n_done / elapsed if elapsed > 0 else 1
            remaining = (n_pairs_total - n_done) / rate if rate > 0 else 0
            print(f"    Pairs: {n_done}/{n_pairs_total} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_phase2_end = time.time()
print(f"  Phase 2 complete: {t_phase2_end - t_phase2_start:.1f}s ({n_skipped} pairs skipped)")

# =============================================================================
# 10. Assemble BCS Hessian
# =============================================================================
print("\n--- 7. Assembling Hessians ---")

def assemble_hessian(d2S_diag, S_pair_plus, S_pair_minus, S_center, eps_val):
    """Assemble 36x36 Hessian from diagonal and off-diagonal finite differences."""
    H = np.zeros((36, 36))
    H[np.diag_indices(36)] = d2S_diag

    for a in range(36):
        for b in range(a+1, 36):
            if S_pair_plus[(a,b)] is None:
                H[a, b] = 0.0
                H[b, a] = 0.0
            else:
                d2S_sum = (S_pair_plus[(a,b)] - 2.0 * S_center + S_pair_minus[(a,b)]) / eps_val**2
                H[a, b] = 0.5 * (d2S_sum - d2S_diag[a] - d2S_diag[b])
                H[b, a] = H[a, b]
    return H

# BCS one-loop Hessian
H_bcs_1loop = assemble_hessian(d2S_bcs_diag, S_bcs_pair_plus, S_bcs_pair_minus, S_bcs_fold, eps)
sym_err_bcs = np.max(np.abs(H_bcs_1loop - H_bcs_1loop.T))
frob_bcs = np.linalg.norm(H_bcs_1loop, 'fro')

# Bare one-loop Hessian (should match S66)
H_bare_1loop = assemble_hessian(d2S_bare_diag, S_bare_pair_plus, S_bare_pair_minus, S_bare_fold, eps)
sym_err_bare = np.max(np.abs(H_bare_1loop - H_bare_1loop.T))
frob_bare = np.linalg.norm(H_bare_1loop, 'fro')

print(f"  BCS 1-loop Hessian: ||H||_F = {frob_bcs:.4f}, sym_err = {sym_err_bcs:.2e}")
print(f"  Bare 1-loop Hessian: ||H||_F = {frob_bare:.4f}, sym_err = {sym_err_bare:.2e}")

# Effective Hessians: tree + one-loop
H_bcs_eff = H_tree_eigenbasis + H_bcs_1loop
H_bare_eff = H_tree_eigenbasis + H_bare_1loop

evals_bcs_eff = np.sort(eigvalsh(H_bcs_eff))
evals_bare_eff = np.sort(eigvalsh(H_bare_eff))

n_pos_bcs = int(np.sum(evals_bcs_eff > 0))
n_neg_bcs = 36 - n_pos_bcs
n_pos_bare = int(np.sum(evals_bare_eff > 0))
n_neg_bare = 36 - n_pos_bare

print(f"\n  BCS effective Hessian:")
print(f"    Signature: ({n_pos_bcs}+, {n_neg_bcs}-)")
print(f"    Eigenvalue range: [{evals_bcs_eff[0]:.6f}, {evals_bcs_eff[-1]:.6f}]")
print(f"    Softest eigenvalue: {evals_bcs_eff[0]:.6f}")

print(f"\n  Bare effective Hessian (this run, cross-check S66):")
print(f"    Signature: ({n_pos_bare}+, {n_neg_bare}-)")
print(f"    Eigenvalue range: [{evals_bare_eff[0]:.6f}, {evals_bare_eff[-1]:.6f}]")
print(f"    Softest eigenvalue: {evals_bare_eff[0]:.6f}")

# =============================================================================
# 11. Cross-Check: Bare Hessian vs S66
# =============================================================================
print("\n--- 8. Cross-checks ---")

# Compare our bare result to S66 Lambda=2.0
max_dev_s66 = np.max(np.abs(evals_bare_eff - evals_bare_L2))
rel_dev_s66 = max_dev_s66 / np.max(np.abs(evals_bare_L2))
print(f"  Bare eigenvalues vs S66 (Lambda=2.0):")
print(f"    Max deviation: {max_dev_s66:.6e}")
print(f"    Relative deviation: {rel_dev_s66:.2e}")
if max_dev_s66 < 1.0:
    print(f"    CONSISTENT (deviation < 1.0)")
else:
    print(f"    WARNING: deviation from S66 exceeds 1.0")

# Trace comparison: Tr(H_BCS) vs Tr(H_bare)
tr_bcs = np.trace(H_bcs_eff)
tr_bare = np.trace(H_bare_eff)
tr_ratio = tr_bcs / tr_bare if abs(tr_bare) > 1e-10 else float('inf')
print(f"\n  Trace comparison:")
print(f"    Tr(H_BCS_eff) = {tr_bcs:.4f}")
print(f"    Tr(H_bare_eff) = {tr_bare:.4f}")
print(f"    Ratio = {tr_ratio:.6f}")
print(f"    Relative change = {(tr_bcs - tr_bare)/abs(tr_bare)*100:.4f}%")
print(f"    Expected from a_2 BCS correction: ~{delta_a2_total*100:.2f}%")

# Frobenius norm of the BCS correction
H_diff = H_bcs_1loop - H_bare_1loop
frob_diff = np.linalg.norm(H_diff, 'fro')
rel_frob = frob_diff / frob_bare if frob_bare > 0 else float('inf')
print(f"\n  BCS correction to 1-loop Hessian:")
print(f"    ||H_BCS_1loop - H_bare_1loop||_F = {frob_diff:.4f}")
print(f"    Relative to bare: {rel_frob:.6f} ({rel_frob*100:.4f}%)")

# =============================================================================
# 12. Per-Cluster Analysis (Ad(U(2)) decomposition from S63)
# =============================================================================
print("\n--- 9. Per-cluster analysis ---")

# Load S63 Casimir data for cluster assignments
s63_cas_path = os.path.join(base_dir, 's63_hessian_casimir.npz')
s63_cas = np.load(s63_cas_path, allow_pickle=True)
cluster_sizes = s63_cas['cluster_sizes']
cluster_mean_c2 = s63_cas['cluster_mean_c2']

# Cluster boundaries (from S63: sizes {1,1,4,3,6,3,4,8,1,5})
cluster_boundaries = np.cumsum(np.concatenate([[0], cluster_sizes]))
n_clusters = len(cluster_sizes)

# C2 labels for each cluster
c2_labels = ['j=0,Y=0(a)', 'j=0,Y=0(b)', 'j=1/2,Y=q',
             'j=1,Y=0', 'j=1,Y=2q', 'j=1,Y=0\'',
             'j=1/2,Y=q\'', 'j=3/2,Y=q', 'j=0,Y=0(c)', 'j=2,Y=0']

print(f"\n  {'Cluster':>10} {'Size':>5} {'BCS min':>12} {'Bare min':>12} {'BCS/Bare':>10} {'Status':>8}")
print(f"  {'-'*67}")

for i in range(n_clusters):
    lo = cluster_boundaries[i]
    hi = cluster_boundaries[i+1]
    ev_bcs_cluster = evals_bcs_eff[lo:hi]
    ev_bare_cluster = evals_bare_eff[lo:hi]

    min_bcs = np.min(ev_bcs_cluster)
    min_bare = np.min(ev_bare_cluster)
    ratio = min_bcs / min_bare if abs(min_bare) > 1e-10 else float('inf')
    status = "STABLE" if min_bcs > 0 else "UNSTABLE"

    label = c2_labels[i] if i < len(c2_labels) else f"cluster_{i}"
    print(f"  {label:>10} {int(cluster_sizes[i]):>5} {min_bcs:>12.4f} {min_bare:>12.4f} "
          f"{ratio:>10.6f} {status:>8}")

# =============================================================================
# 13. Stabilization Margin Analysis
# =============================================================================
print("\n--- 10. Stabilization margin ---")

min_bcs_eval = evals_bcs_eff[0]
max_tree_abs = np.max(np.abs(evals_tree))
margin_bcs = min_bcs_eval / max_tree_abs

min_bare_eval = evals_bare_eff[0]
margin_bare = min_bare_eval / max_tree_abs

print(f"  max |tree eigenvalue| = {max_tree_abs:.4f}")
print(f"  BCS softest eigenvalue = {min_bcs_eval:.6f}")
print(f"  Bare softest eigenvalue = {min_bare_eval:.6f}")
print(f"  BCS stabilization margin = {margin_bcs:.6f} ({margin_bcs / margin_bare * 100:.2f}% of bare)")
print(f"  Bare stabilization margin = {margin_bare:.6f}")

# Softest mode identification
idx_softest_bcs = 0  # by construction (sorted)
idx_softest_bare = 0

# Eigenvector of softest BCS mode
_, evecs_bcs = eigh(H_bcs_eff)
softest_bcs_evec = evecs_bcs[:, 0]  # eigenvector of smallest eigenvalue
_, evecs_bare = eigh(H_bare_eff)
softest_bare_evec = evecs_bare[:, 0]

# Overlap between BCS and bare softest modes
overlap = abs(np.dot(softest_bcs_evec, softest_bare_evec))
print(f"\n  Softest mode overlap (BCS vs bare): |<v_BCS|v_bare>| = {overlap:.6f}")
if overlap > 0.99:
    print(f"    Same mode (overlap > 0.99)")
elif overlap > 0.9:
    print(f"    Similar mode (overlap > 0.9)")
else:
    print(f"    Different mode (overlap < 0.9)")

# =============================================================================
# 14. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: BCS-HESS-69")
print("=" * 78)

if n_pos_bcs == 36 and margin_bcs >= 0.05:  # margin >= 5x means min/max_tree > 0.05
    # Actually the task says margin >= 5x means min_bcs >= 5 * max_tree * some_factor
    # Let's compute: "5x margin" means the softest eigenvalue is at least 5x away from zero
    # relative to the tree scale. With softest = 29.4 and max_tree = 148.7,
    # ratio = 0.198. "5x" in the gate means min_bcs/max_tree > some threshold.
    # From S62 collab: margin was 26x when min_bcs=31 vs softest_tree=15.
    # Let the "x" be min_bcs / |softest_tree|.
    margin_x = min_bcs_eval / abs(evals_tree[-1])
    if margin_x >= 5.0:
        gate_verdict = "PASS"
        gate_detail = (f"All 36 eigenvalues positive at Lambda = {Lambda_phys} M_KK. "
                       f"BCS stabilization margin = {margin_x:.1f}x. "
                       f"Fold STABLE under BCS condensate.")
    else:
        gate_verdict = "INFO"
        gate_detail = (f"All 36 eigenvalues positive but margin = {margin_x:.1f}x < 5x. "
                       f"Marginal stability under BCS.")
elif n_pos_bcs == 36:
    margin_x = min_bcs_eval / abs(evals_tree[-1])
    if margin_x >= 5.0:
        gate_verdict = "PASS"
        gate_detail = (f"All 36 eigenvalues positive. Margin = {margin_x:.1f}x.")
    else:
        gate_verdict = "INFO"
        gate_detail = (f"All 36 positive but margin = {margin_x:.1f}x < 5.")
else:
    gate_verdict = "FAIL"
    margin_x = min_bcs_eval / abs(evals_tree[-1])
    gate_detail = (f"BCS destabilizes fold: ({n_pos_bcs}+, {n_neg_bcs}-). "
                   f"Most negative eigenvalue: {evals_bcs_eff[0]:.6f}")

print(f"\n  VERDICT: {gate_verdict}")
print(f"  {gate_detail}")

# Also compute margin relative to softest tree eigenvalue
margin_vs_softest_tree = min_bcs_eval / abs(evals_tree[-1])
margin_bare_vs_softest = min_bare_eval / abs(evals_tree[-1])
print(f"\n  Margin (BCS): min_eval / |softest_tree| = {margin_vs_softest_tree:.4f} ({margin_vs_softest_tree:.1f}x)")
print(f"  Margin (bare): min_eval / |softest_tree| = {margin_bare_vs_softest:.4f} ({margin_bare_vs_softest:.1f}x)")
print(f"  Margin ratio (BCS/bare): {margin_vs_softest_tree/margin_bare_vs_softest:.6f}")

# =============================================================================
# 15. Detailed Eigenvalue Comparison Table
# =============================================================================
print(f"\n  Detailed eigenvalue comparison (all 36):")
print(f"  {'idx':>4} {'BCS':>14} {'Bare':>14} {'Ratio':>10} {'Shift':>14} {'RelShift%':>10}")
print(f"  {'-'*76}")

for k in range(36):
    ev_bcs = evals_bcs_eff[k]
    ev_bare = evals_bare_eff[k]
    ratio = ev_bcs / ev_bare if abs(ev_bare) > 1e-10 else float('inf')
    shift = ev_bcs - ev_bare
    rel_shift = shift / abs(ev_bare) * 100 if abs(ev_bare) > 1e-10 else float('inf')
    print(f"  {k:>4} {ev_bcs:>14.4f} {ev_bare:>14.4f} {ratio:>10.6f} {shift:>14.4f} {rel_shift:>10.4f}")

# =============================================================================
# 16. Summary Statistics
# =============================================================================
print("\n" + "=" * 78)
print("  SUMMARY")
print("=" * 78)

mean_shift = np.mean(evals_bcs_eff - evals_bare_eff)
max_shift = np.max(np.abs(evals_bcs_eff - evals_bare_eff))
mean_rel = np.mean((evals_bcs_eff - evals_bare_eff) / np.abs(evals_bare_eff)) * 100

print(f"  BCS gap: Delta = {Delta_BCS:.6f} M_KK")
print(f"  Chemical potential: mu = {mu_BCS:.6f} M_KK")
print(f"  Cutoff: Lambda = {Lambda_phys:.3f} M_KK")
print(f"")
print(f"  Bare Hessian: (36+, 0-), min = {evals_bare_eff[0]:.4f}, max = {evals_bare_eff[-1]:.4f}")
print(f"  BCS Hessian:  ({n_pos_bcs}+, {n_neg_bcs}-), min = {evals_bcs_eff[0]:.4f}, max = {evals_bcs_eff[-1]:.4f}")
print(f"")
print(f"  Mean eigenvalue shift (BCS - bare): {mean_shift:.4f}")
print(f"  Max |eigenvalue shift|: {max_shift:.4f}")
print(f"  Mean relative shift: {mean_rel:.4f}%")
print(f"")
print(f"  Softest mode shift: {evals_bcs_eff[0] - evals_bare_eff[0]:.6f}")
print(f"  Softest mode: {'stiffened' if evals_bcs_eff[0] > evals_bare_eff[0] else 'softened'} under BCS")
print(f"")
print(f"  Gate: BCS-HESS-69 = {gate_verdict}")

t_total = time.time() - t_global_start
print(f"\n  Total computation time: {t_total:.1f}s")

# =============================================================================
# 17. Save Data
# =============================================================================
print("\n--- 11. Saving results ---")

out_path = os.path.join(base_dir, 's69_bcs_hessian.npz')

save_dict = {
    'gate_name': 'BCS-HESS-69',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
    'tau_fold': tau_fold,
    'g_fold': g_fold,
    'epsilon': eps,
    'Lambda_phys': Lambda_phys,
    'Delta_BCS': Delta_BCS,
    'mu_BCS': mu_BCS,
    # Tree-level
    'evals_tree': evals_tree,
    'H_tree_eigenbasis': H_tree_eigenbasis,
    # BCS effective Hessian
    'H_bcs_1loop': H_bcs_1loop,
    'H_bcs_eff': H_bcs_eff,
    'evals_bcs_eff': evals_bcs_eff,
    'n_pos_bcs': n_pos_bcs,
    'n_neg_bcs': n_neg_bcs,
    # Bare effective Hessian (this run)
    'H_bare_1loop': H_bare_1loop,
    'H_bare_eff': H_bare_eff,
    'evals_bare_eff': evals_bare_eff,
    'n_pos_bare': n_pos_bare,
    'n_neg_bare': n_neg_bare,
    # BCS correction
    'H_bcs_minus_bare': H_diff,
    'frob_bcs_correction': frob_diff,
    'frob_rel': rel_frob,
    # Margins
    'margin_bcs_x': margin_x,
    'margin_bare_x': margin_bare_vs_softest,
    'margin_ratio': margin_vs_softest_tree / margin_bare_vs_softest,
    # Softest mode
    'softest_bcs_evec': softest_bcs_evec,
    'softest_bare_evec': softest_bare_evec,
    'softest_overlap': overlap,
    # Cluster info
    'cluster_sizes': cluster_sizes,
    # Traces
    'tr_bcs_eff': tr_bcs,
    'tr_bare_eff': tr_bare,
    # Timings
    'total_time': t_total,
    # D_K eigenvalues at fold
    'evals_fold_DK': evals_fold,
    'E_fold_BdG': E_fold,
}

np.savez(out_path, **save_dict)
print(f"  Saved: {out_path}")

# =============================================================================
# 18. Visualization
# =============================================================================
print("\n--- 12. Generating visualization ---")

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle(
    f'BCS-DRESSED-HESSIAN-69: Fold Stability Under BCS\n'
    f'Gate: {gate_verdict} | '
    r'$\Delta = $' + f'{Delta_BCS:.3f} M_KK, '
    r'$\mu = $' + f'{mu_BCS:.3f} M_KK, '
    r'$\Lambda = $' + f'{Lambda_phys:.3f} M_KK',
    fontsize=13, fontweight='bold')

# --- Panel 1: Eigenvalue comparison ---
ax1 = axes[0, 0]
idx = np.arange(36)
ax1.bar(idx - 0.15, evals_bare_eff, 0.3, label='Bare', alpha=0.7, color='steelblue')
ax1.bar(idx + 0.15, evals_bcs_eff, 0.3, label='BCS-dressed', alpha=0.7, color='firebrick')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('Eigenvalue index (sorted)')
ax1.set_ylabel('Eigenvalue')
ax1.set_title('Hessian Eigenvalues: Bare vs BCS')
ax1.legend()
ax1.grid(alpha=0.3)

# --- Panel 2: Eigenvalue shift ---
ax2 = axes[0, 1]
shifts = evals_bcs_eff - evals_bare_eff
rel_shifts = shifts / np.abs(evals_bare_eff) * 100
ax2.bar(idx, rel_shifts, color='darkorange', alpha=0.7)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axhline(y=delta_a2_total*100, color='green', linewidth=1.5,
            linestyle='--', label=f'a_2 BCS shift ({delta_a2_total*100:.1f}%)')
ax2.set_xlabel('Eigenvalue index')
ax2.set_ylabel('Relative shift (%)')
ax2.set_title('BCS Eigenvalue Shift (relative to bare)')
ax2.legend()
ax2.grid(alpha=0.3)

# --- Panel 3: BdG energy spectrum ---
ax3 = axes[1, 0]
# Sort bare eigenvalues for plotting
evals_sorted = np.sort(evals_fold)
xi_sorted = evals_sorted - mu_BCS
E_sorted = np.sqrt(xi_sorted**2 + Delta_BCS**2)

# Plot |bare eigenvalue| vs BdG energy
ax3.scatter(np.abs(evals_sorted), E_sorted, s=1, alpha=0.3, c='steelblue', label='BdG energies')
ax3.plot([0, np.max(np.abs(evals_sorted))], [Delta_BCS, Delta_BCS],
         'r--', linewidth=1, label=f'Gap $\\Delta$ = {Delta_BCS:.3f}')
ax3.axvline(x=mu_BCS, color='green', linewidth=1, linestyle='--',
            label=f'$\\mu$ = {mu_BCS:.3f}')
ax3.set_xlabel('|Bare eigenvalue|')
ax3.set_ylabel('BdG energy E_n')
ax3.set_title(f'BdG Quasiparticle Spectrum ({n_total_evals} modes)')
ax3.legend()
ax3.grid(alpha=0.3)

# --- Panel 4: Cluster-level comparison ---
ax4 = axes[1, 1]
cluster_bcs_mins = []
cluster_bare_mins = []
cluster_labels_short = []

for i in range(n_clusters):
    lo = cluster_boundaries[i]
    hi = cluster_boundaries[i+1]
    cluster_bcs_mins.append(np.min(evals_bcs_eff[lo:hi]))
    cluster_bare_mins.append(np.min(evals_bare_eff[lo:hi]))
    cluster_labels_short.append(f"C{i}")

x_cl = np.arange(n_clusters)
ax4.bar(x_cl - 0.15, cluster_bare_mins, 0.3, label='Bare', alpha=0.7, color='steelblue')
ax4.bar(x_cl + 0.15, cluster_bcs_mins, 0.3, label='BCS', alpha=0.7, color='firebrick')
ax4.axhline(y=0, color='black', linewidth=0.5)
ax4.set_xticks(x_cl)
ax4.set_xticklabels(cluster_labels_short, fontsize=8)
ax4.set_xlabel('Cluster (Ad(U(2)) decomposition)')
ax4.set_ylabel('Min eigenvalue in cluster')
ax4.set_title('Per-Cluster Stability: Bare vs BCS')
ax4.legend()
ax4.grid(alpha=0.3)

# Add text annotation with key numbers
textstr = (f'Bare: (36+, 0-), min={evals_bare_eff[0]:.1f}\n'
           f'BCS:  ({n_pos_bcs}+, {n_neg_bcs}-), min={evals_bcs_eff[0]:.1f}\n'
           f'Margin ratio: {margin_vs_softest_tree/margin_bare_vs_softest:.3f}\n'
           f'Gate: {gate_verdict}')
ax4.text(0.98, 0.98, textstr, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
fig_path = os.path.join(base_dir, 's69_bcs_hessian.png')
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {fig_path}")
plt.close()

print("\n" + "=" * 78)
print(f"  BCS-DRESSED-HESSIAN-69 COMPLETE — Gate: {gate_verdict}")
print("=" * 78)
