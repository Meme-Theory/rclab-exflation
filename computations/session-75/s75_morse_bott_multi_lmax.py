#!/usr/bin/env python3
"""
s75_morse_bott_multi_lmax.py -- MORSE-BOTT-MULTI-LMAX-75 (GPU-OPTIMIZED)
=========================================================================
Gate: S75-B4-MORSE-MULTI-LMAX
  PASS: Signature (36+, 0-, 0-null) at all three L_max in {3, 5, 7}
  INFO: Signature changes but remains (n+, 0-, 0-null) with different n+
  FAIL: Any negative eigenvalue appears

GPU optimization: Batch all 1333 metric perturbations per L_max and use
torch.linalg.eigvalsh for batched Dirac eigenvalue computation on ROCm.
Original CPU version timed out at ~2h; GPU version targets ~5-10 min.

Author: Team-lead GPU rebuild (Session 75)
"""

import sys, os, time, warnings
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import exp, sqrt, pi
from numpy.linalg import eigh, eigvalsh, inv, norm, cholesky, det
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import torch
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# ROCm fp64 on RDNA4 is 1/32 rate but still faster than serial CPU for batched ops
DTYPE_C = torch.complex128
DTYPE_R = torch.float64
print(f"  Torch device: {DEVICE}, CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  GPU: {torch.cuda.get_device_name(0)}")
    print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

from canonical_constants import (
    tau_fold, PI, S_fold, d2S_fold,
    E_B1, E_B2_mean, E_B3_mean,
)

print("=" * 78)
print("  MORSE-BOTT-MULTI-LMAX-75: 36D Hessian at L_max = {3, 5, 7} [GPU]")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
t_global_start = time.time()
base_dir = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# 1. SU(3) LIE ALGEBRA INFRASTRUCTURE (CPU, one-time)
# =============================================================================
print("\n--- 1. SU(3) Lie algebra infrastructure ---")

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
    return [-1j / 2.0 * lam for lam in gell_mann_matrices()]

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

SU2_IDX = [0, 1, 2]
C2_IDX = [3, 4, 5, 6]
U1_IDX = [7]

# =============================================================================
# 2. FRAME, CONNECTION, DIRAC (CPU helpers for building operators)
# =============================================================================

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

def build_dirac_for_irrep_np(rho, E, gammas, Omega):
    """Build Dirac operator for one irrep on CPU. Returns numpy array."""
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
# 3. IRREP CONSTRUCTION (same as original, CPU one-time)
# =============================================================================

def irrep_fundamental(gens):
    return [g.copy() for g in gens]

def irrep_antifundamental(gens):
    return [-g.T for g in gens]

def irrep_adjoint(f_abc):
    return [f_abc[a,:,:].T.astype(complex) for a in range(8)]

def irrep_symmetric_n(gens, n_sym):
    from itertools import combinations_with_replacement, permutations
    d = 3  # (local)
    basis_indices = list(combinations_with_replacement(range(d), n_sym))
    dim = len(basis_indices)
    d_n = d ** n_sym
    sym_vecs = []
    for idx_tuple in basis_indices:
        v = np.zeros(d_n, dtype=complex)
        perms = set(permutations(idx_tuple))
        norm_val = np.sqrt(len(perms))
        for p in perms:
            flat_idx = sum(pk * (d ** (n_sym - 1 - k)) for k, pk in enumerate(p))
            v[flat_idx] = 1.0 / norm_val
        sym_vecs.append(v)
    P = np.column_stack(sym_vecs)
    I3 = np.eye(d, dtype=complex)
    rho = []
    for X in gens:
        rho_dn = np.zeros((d_n, d_n), dtype=complex)
        for k in range(n_sym):
            factors = [I3] * n_sym
            factors[k] = X
            M = factors[0]
            for fac in factors[1:]:
                M = np.kron(M, fac)
            rho_dn += M
        rho.append(P.conj().T @ rho_dn @ P)
    return rho

def irrep_via_casimir_projection(rho_A, rho_B, target_dim, target_pq=None):
    dim_A, dim_B = rho_A[0].shape[0], rho_B[0].shape[0]
    dim_prod = dim_A * dim_B
    C2 = np.zeros((dim_prod, dim_prod), dtype=complex)
    rho_prod = []
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
        label = f"({target_pq[0]},{target_pq[1]})" if target_pq else f"dim={target_dim}"
        raise RuntimeError(f"Cannot find {target_dim}-dim eigenspace for {label}")
    mask = np.abs(evals - target_eval) < tol
    P = evecs[:, mask]
    return [P.conj().T @ rho_prod[a] @ P for a in range(8)]

def get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3):
    irreps = []
    rho_fund = irrep_fundamental(gens)
    rho_antifund = irrep_antifundamental(gens)
    rho_adj = irrep_adjoint(f_abc)
    built = {}
    built[(0,0)] = [np.zeros((1,1), dtype=complex) for _ in range(8)]
    built[(1,0)] = rho_fund
    built[(0,1)] = rho_antifund
    built[(1,1)] = rho_adj
    conj_gens = [-g.T for g in gens]
    for n in range(2, max_pq_sum + 1):
        dim_n0 = (n+1)*(n+2)//2
        try:
            rho_n0 = irrep_symmetric_n(gens, n)
            if rho_n0[0].shape[0] == dim_n0:
                built[(n,0)] = rho_n0
        except Exception:
            pass
        try:
            rho_0n = irrep_symmetric_n(conj_gens, n)
            if rho_0n[0].shape[0] == dim_n0:
                built[(0,n)] = rho_0n
        except Exception:
            pass
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if (p,q) in built:
                continue
            dim_pq = (p+1)*(q+1)*(p+q+2)//2
            success = False
            if p >= 1 and (p-1,q) in built:
                try:
                    built[(p,q)] = irrep_via_casimir_projection(built[(p-1,q)], rho_fund, dim_pq, (p,q))
                    success = True
                except Exception:
                    pass
            if not success and q >= 1 and (p,q-1) in built:
                try:
                    built[(p,q)] = irrep_via_casimir_projection(built[(p,q-1)], rho_antifund, dim_pq, (p,q))
                    success = True
                except Exception:
                    pass
            if not success and p >= 1 and q >= 1 and (p-1,q-1) in built:
                try:
                    built[(p,q)] = irrep_via_casimir_projection(built[(p-1,q-1)], rho_adj, dim_pq, (p,q))
                    success = True
                except Exception:
                    pass
            if not success:
                print(f"  WARNING: Could not build ({p},{q})")
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if (p,q) in built:
                dim_pq = (p+1)*(q+1)*(p+q+2)//2
                rho = built[(p,q)]
                if rho[0].shape[0] == dim_pq:
                    irreps.append((p, q, dim_pq, rho))
    return irreps

# =============================================================================
# 4. GPU-BATCHED SPECTRAL ACTION
# =============================================================================

def compute_SA_batch_gpu(metrics_batch, gens_np, f_abc_np, gammas_np, irreps_data, Lambda_sq):
    """Compute spectral action for a BATCH of metrics using GPU.

    metrics_batch: list of N 8x8 numpy arrays (perturbed metrics)
    Returns: numpy array of N spectral action values
    """
    N = len(metrics_batch)
    SA_vals = np.zeros(N)  # (local)

    # For each metric, compute frame + connection + spinor connection on CPU
    # (these are cheap 8x8 operations), then batch the Dirac construction on GPU
    frames = []  # (local)
    omegas = []  # (local)
    valid = np.ones(N, dtype=bool)  # (local)

    for i, g_s in enumerate(metrics_batch):
        ev = eigvalsh(g_s)
        if not np.all(ev > 0):
            valid[i] = False
            SA_vals[i] = np.nan
            continue
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc_np, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas_np)
        frames.append(E)
        omegas.append(Omega)

    valid_indices = np.where(valid)[0]  # (local)
    if len(valid_indices) == 0:
        return SA_vals

    # For each irrep, build ALL valid Dirac operators and batch-diagonalize on GPU
    for (p, q, dim_rho, rho) in irreps_data:
        dim_block = dim_rho * 16  # (local)
        n_valid = len(valid_indices)  # (local)

        # Pre-compute kron(rho[b], gamma[a]) once (shared across all metrics)
        rho_gamma_ba = {}  # (local)
        for a in range(8):
            for b in range(8):
                rho_gamma_ba[(b,a)] = np.kron(rho[b], gammas_np[a])

        # Build batch of Dirac operators
        D_batch_np = np.zeros((n_valid, dim_block, dim_block), dtype=complex)  # (local)
        id_rho = np.eye(dim_rho)  # (local)

        for idx, vi in enumerate(valid_indices):
            fi = frames[sum(valid[:vi+1]) - 1]  # map to frames list index
            oi = omegas[sum(valid[:vi+1]) - 1]
            D = np.kron(id_rho, oi).copy()
            for a in range(8):
                for b in range(8):
                    if abs(fi[a,b]) > 1e-15:
                        D += fi[a,b] * rho_gamma_ba[(b,a)]
            D_batch_np[idx] = D

        # Move to GPU and batch diagonalize
        # Use -i*D for Hermitian form
        iD_batch = -1j * torch.tensor(D_batch_np, dtype=DTYPE_C, device=DEVICE)

        try:
            evals_batch = torch.linalg.eigvalsh(iD_batch)  # (n_valid, dim_block) real
            evals_np = evals_batch.cpu().numpy()
        except Exception as e:
            # Fallback to CPU if GPU eigvalsh fails
            print(f"  GPU eigvalsh failed for ({p},{q}), falling back to CPU: {e}")
            evals_np = np.zeros((n_valid, dim_block))
            for idx in range(n_valid):
                evals_np[idx] = eigvalsh((-1j * D_batch_np[idx]).real if np.allclose((-1j * D_batch_np[idx]).imag, 0) else eigvalsh(-1j * D_batch_np[idx]))

        # Accumulate spectral action: SA += dim_rho * sum exp(-evals^2 / Lambda_sq)
        evals_sq = evals_np ** 2  # (local)
        sa_contrib = dim_rho * np.sum(np.exp(-evals_sq / Lambda_sq), axis=1)  # (local)

        for idx, vi in enumerate(valid_indices):
            SA_vals[vi] += sa_contrib[idx]

        # Free GPU memory for this irrep
        del iD_batch, evals_batch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    return SA_vals

def compute_SA_batch_gpu_v2(metrics_batch, gens_np, f_abc_np, gammas_np, irreps_data, Lambda_sq):
    """V2: Pre-compute frames on CPU, build+diag Dirac on GPU per irrep.

    Optimized indexing to avoid the frame mapping bug in v1.
    """
    N = len(metrics_batch)
    SA_vals = np.zeros(N)  # (local)

    # Pre-compute frames and spinor connections for all metrics
    frame_data = [None] * N  # (local) list of (E, Omega) or None if PD fails
    for i, g_s in enumerate(metrics_batch):
        ev = eigvalsh(g_s)
        if not np.all(ev > 0):
            SA_vals[i] = np.nan
            continue
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc_np, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas_np)
        frame_data[i] = (E, Omega)

    valid_indices = [i for i in range(N) if frame_data[i] is not None]  # (local)
    n_valid = len(valid_indices)  # (local)
    if n_valid == 0:
        return SA_vals

    for (p, q, dim_rho, rho) in irreps_data:
        dim_block = dim_rho * 16  # (local)

        # Pre-compute kron(rho[b], gamma[a]) once
        rg = {}  # (local)
        for a in range(8):
            for b in range(8):
                rg[(b,a)] = np.kron(rho[b], gammas_np[a])
        id_omega_base = np.kron(np.eye(dim_rho), np.zeros_like(gammas_np[0]))  # (local)

        # Build batch of Dirac operators on CPU
        D_batch = np.zeros((n_valid, dim_block, dim_block), dtype=complex)  # (local)
        for idx, vi in enumerate(valid_indices):
            E, Omega = frame_data[vi]
            D = np.kron(np.eye(dim_rho), Omega).copy()
            for a in range(8):
                for b in range(8):
                    if abs(E[a,b]) > 1e-15:
                        D += E[a,b] * rg[(b,a)]
            D_batch[idx] = D

        # GPU batch eigvalsh
        iD_batch = -1j * torch.tensor(D_batch, dtype=DTYPE_C, device=DEVICE)

        try:
            evals_batch = torch.linalg.eigvalsh(iD_batch)
            evals_np = evals_batch.cpu().numpy()
        except Exception as e:
            print(f"  GPU failed for ({p},{q}) dim={dim_block}: {e}")
            evals_np = np.zeros((n_valid, dim_block))
            for idx in range(n_valid):
                evals_np[idx] = eigvalsh((-1j * D_batch[idx]))

        evals_sq = evals_np ** 2  # (local)
        sa_contrib = dim_rho * np.sum(np.exp(-evals_sq / Lambda_sq), axis=1)  # (local)

        for idx, vi in enumerate(valid_indices):
            SA_vals[vi] += sa_contrib[idx]

        del iD_batch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    return SA_vals

# =============================================================================
# 5. BUILD ALGEBRAIC INFRASTRUCTURE
# =============================================================================
print("\n--- 2. Building algebraic infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
gammas = build_cliff8()

cliff_err = 0.0  # (local)
for a in range(8):
    for b in range(8):
        ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(16)
        cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
print(f"  Clifford algebra error: {cliff_err:.2e}")

# =============================================================================
# 6. FOLD METRIC
# =============================================================================
print("\n--- 3. Building fold metric ---")

L1_fold = exp(2.0 * tau_fold)  # (local)
L2_fold = exp(-2.0 * tau_fold)  # (local)
L3_fold = exp(tau_fold)  # (local)

g0 = np.abs(B_ab)  # (local)
g_fold = np.zeros((8,8), dtype=np.float64)  # (local)
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
print(f"  det(g_fold): {det(g_fold):.6f}")

# =============================================================================
# 7. SYM(8) BASIS (36D)
# =============================================================================
print("\n--- 4. Constructing Sym(8) basis [36D] ---")

basis_sym8 = []
basis_labels = []
for i in range(8):
    M = np.zeros((8,8))
    M[i,i] = 1.0
    basis_sym8.append(M)
    basis_labels.append(f"diag({i})")
for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8,8))
        M[i,j] = 1.0 / sqrt(2.0)
        M[j,i] = 1.0 / sqrt(2.0)
        basis_sym8.append(M)
        basis_labels.append(f"off({i},{j})")
assert len(basis_sym8) == 36

# =============================================================================
# 8. VOLUME-PRESERVING PROJECTION (35D)
# =============================================================================
print("\n--- 5. Volume-preserving projection ---")

g_fold_inv = inv(g_fold)  # (local)
vol_vec = np.zeros(36)  # (local)
for k in range(36):
    vol_vec[k] = np.sum(g_fold_inv * basis_sym8[k])
vol_vec /= norm(vol_vec)

full_basis = np.eye(36)  # (local)
perp_vecs = []  # (local)
for k in range(36):
    v = full_basis[k] - np.dot(full_basis[k], vol_vec) * vol_vec
    if norm(v) > 1e-10:
        perp_vecs.append(v / norm(v))

basis_35_raw = []  # (local)
for v in perp_vecs:
    for u in basis_35_raw:
        v = v - np.dot(v, u) * u
    if norm(v) > 1e-10:
        basis_35_raw.append(v / norm(v))
    if len(basis_35_raw) == 35:
        break

basis_35 = np.array(basis_35_raw)  # (local)
print(f"  35D basis shape: {basis_35.shape}")
ortho_check = np.max(np.abs(basis_35 @ basis_35.T - np.eye(35)))  # (local)
print(f"  Orthonormality error: {ortho_check:.2e}")

# =============================================================================
# 9. MAIN COMPUTATION: GPU-BATCHED HESSIAN
# =============================================================================
print("\n" + "=" * 78)
print("  MAIN COMPUTATION: GPU-batched Hessian at L_max = {3, 5, 7}")
print("=" * 78)

epsilon = 0.005  # (local)
L_max_values = [3, 5, 7]  # (local)
zero_tol = 1e-6  # (local)
results = {}  # (local)

for L_max in L_max_values:
    print(f"\n{'='*78}")
    print(f"  L_max = {L_max}")
    print(f"{'='*78}")
    t_lmax_start = time.time()

    # Build irreps
    print(f"  Building irreps (p+q <= {L_max})...")
    irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=L_max)
    n_irreps = len(irreps_data)  # (local)
    n_evals = sum(d * 16 * d for _,_,d,_ in irreps_data)  # (local)
    max_block = max(d * 16 for _,_,d,_ in irreps_data)  # (local)
    print(f"  Irreps: {n_irreps}, total evals/metric: {n_evals}, max block: {max_block}")

    # Reference SA at fold
    print(f"  Computing reference SA at fold...")
    SA_ref = compute_SA_batch_gpu_v2([g_fold], gens, f_abc, gammas, irreps_data, 1e30)[0]  # (local)
    # Use proper Lambda from eigenvalue range
    evals_fold_test = []  # (local)
    E_fold = orthonormal_frame(g_fold)
    ft_fold = frame_structure_constants(f_abc, E_fold)
    Gamma_fold = connection_coefficients(ft_fold)
    Omega_fold = spinor_connection_offset(Gamma_fold, gammas)
    for (p, q, dim_rho, rho) in irreps_data:
        D = build_dirac_for_irrep_np(rho, E_fold, gammas, Omega_fold)
        iD = -1j * D
        ev = eigvalsh(iD)
        evals_fold_test.extend([e for e in ev for _ in range(dim_rho)])
    evals_fold_arr = np.array(evals_fold_test)  # (local)
    Lambda_sq = 4.0 * np.max(evals_fold_arr**2)  # (local)

    # Recompute SA with correct Lambda
    SA_fold_val = compute_SA_batch_gpu_v2([g_fold], gens, f_abc, gammas, irreps_data, Lambda_sq)[0]  # (local)
    print(f"  Lambda^2 = {Lambda_sq:.4f}, SA(fold) = {SA_fold_val:.6f}")

    # Pre-build ALL perturbed metrics
    # Diagonal: g +/- eps * B_k  (72 metrics)
    # Off-diagonal: g +/- eps * (B_k + B_l)  (1260 metrics)
    print(f"\n  Pre-building perturbed metrics...")

    diag_metrics_plus = [g_fold + epsilon * basis_sym8[k] for k in range(36)]  # (local)
    diag_metrics_minus = [g_fold - epsilon * basis_sym8[k] for k in range(36)]  # (local)

    offdiag_pairs = [(k, l) for k in range(36) for l in range(k+1, 36)]  # (local)
    offdiag_metrics_plus = [g_fold + epsilon * (basis_sym8[k] + basis_sym8[l]) for k, l in offdiag_pairs]  # (local)
    offdiag_metrics_minus = [g_fold - epsilon * (basis_sym8[k] + basis_sym8[l]) for k, l in offdiag_pairs]  # (local)

    all_metrics = diag_metrics_plus + diag_metrics_minus + offdiag_metrics_plus + offdiag_metrics_minus  # (local)
    n_total = len(all_metrics)  # (local)
    print(f"  Total metrics to evaluate: {n_total}")

    # Batch compute all SA values on GPU
    # Process in chunks to manage VRAM (chunk by number of metrics, not irreps)
    CHUNK_SIZE = 200  # (local) process 200 metrics at a time
    SA_all = np.zeros(n_total)  # (local)

    t_sa_start = time.time()
    for chunk_start in range(0, n_total, CHUNK_SIZE):
        chunk_end = min(chunk_start + CHUNK_SIZE, n_total)
        chunk_metrics = all_metrics[chunk_start:chunk_end]
        SA_chunk = compute_SA_batch_gpu_v2(chunk_metrics, gens, f_abc, gammas, irreps_data, Lambda_sq)
        SA_all[chunk_start:chunk_end] = SA_chunk
        elapsed = time.time() - t_sa_start  # (local)
        pct = chunk_end / n_total * 100  # (local)
        print(f"    {chunk_end}/{n_total} ({pct:.0f}%) in {elapsed:.1f}s")

    t_sa_elapsed = time.time() - t_sa_start  # (local)
    print(f"  All SA evaluations: {t_sa_elapsed:.1f}s ({n_total/t_sa_elapsed:.1f} evals/s)")

    # Unpack SA values
    SA_diag_plus = SA_all[:36]  # (local)
    SA_diag_minus = SA_all[36:72]  # (local)
    SA_offdiag_plus = SA_all[72:72+len(offdiag_pairs)]  # (local)
    SA_offdiag_minus = SA_all[72+len(offdiag_pairs):]  # (local)

    # Assemble 36x36 Hessian
    print(f"\n  Assembling 36x36 Hessian...")
    H_36 = np.zeros((36, 36))  # (local)

    # Diagonal entries
    for k in range(36):
        if np.isnan(SA_diag_plus[k]) or np.isnan(SA_diag_minus[k]):
            H_36[k,k] = 0.0
        else:
            H_36[k,k] = (SA_diag_plus[k] - 2.0 * SA_fold_val + SA_diag_minus[k]) / epsilon**2

    # Off-diagonal via polarization identity
    for idx, (k, l) in enumerate(offdiag_pairs):
        sp = SA_offdiag_plus[idx]  # (local)
        sm = SA_offdiag_minus[idx]  # (local)
        if np.isnan(sp) or np.isnan(sm):
            H_36[k,l] = 0.0
            H_36[l,k] = 0.0
        else:
            d2_sum = (sp - 2.0 * SA_fold_val + sm) / epsilon**2  # (local)
            H_36[k,l] = 0.5 * (d2_sum - H_36[k,k] - H_36[l,l])
            H_36[l,k] = H_36[k,l]

    # Symmetrize
    H_36 = 0.5 * (H_36 + H_36.T)

    # Diagonalize
    evals_36, evecs_36 = eigh(H_36)
    n_pos_36 = np.sum(evals_36 > zero_tol)  # (local)
    n_neg_36 = np.sum(evals_36 < -zero_tol)  # (local)
    n_zero_36 = 36 - n_pos_36 - n_neg_36  # (local)

    print(f"\n  36D Hessian signature: ({n_pos_36}+, {n_neg_36}-, {n_zero_36} null)")
    print(f"  Eigenvalue range: [{evals_36[0]:.4f}, {evals_36[-1]:.4f}]")
    print(f"  Min |eigenvalue|: {np.min(np.abs(evals_36)):.6f}")

    # Project to 35D volume-preserving
    H_35 = basis_35 @ H_36 @ basis_35.T  # (local)
    evals_35 = eigvalsh(H_35)  # (local)
    n_pos_35 = np.sum(evals_35 > zero_tol)  # (local)
    n_neg_35 = np.sum(evals_35 < -zero_tol)  # (local)
    n_zero_35 = 35 - n_pos_35 - n_neg_35  # (local)

    print(f"  35D VP signature: ({n_pos_35}+, {n_neg_35}-, {n_zero_35} null)")
    print(f"  VP eigenvalue range: [{evals_35[0]:.4f}, {evals_35[-1]:.4f}]")

    t_lmax_elapsed = time.time() - t_lmax_start  # (local)
    print(f"\n  L_max = {L_max} total time: {t_lmax_elapsed:.1f}s")

    results[L_max] = {
        'evals_36': evals_36,
        'evals_35': evals_35,
        'sig_36': (n_pos_36, n_neg_36, n_zero_36),
        'sig_35': (n_pos_35, n_neg_35, n_zero_35),
        'SA_fold': SA_fold_val,
        'Lambda_sq': Lambda_sq,
        'n_irreps': n_irreps,
        'n_evals': n_evals,
        'time_s': t_lmax_elapsed,
    }

# =============================================================================
# 10. GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: S75-B4-MORSE-MULTI-LMAX")
print("=" * 78)

all_pass = True  # (local)
any_negative = False  # (local)
for L in L_max_values:
    r = results[L]
    sig36 = r['sig_36']
    sig35 = r['sig_35']
    print(f"\n  L_max = {L}: 36D ({sig36[0]}+, {sig36[1]}-, {sig36[2]}null) | "
          f"35D ({sig35[0]}+, {sig35[1]}-, {sig35[2]}null) | {r['time_s']:.0f}s")
    if sig36 != (36, 0, 0):
        all_pass = False
    if sig36[1] > 0 or sig35[1] > 0:
        any_negative = True

if any_negative:
    verdict = "FAIL"
    verdict_msg = "Negative eigenvalue detected -- moduli instability direction exists"
elif all_pass:
    verdict = "PASS"
    verdict_msg = "Signature (36+, 0-, 0-null) at all three L_max values"
else:
    verdict = "INFO"
    verdict_msg = "Signature stable but not (36+, 0-, 0-null) at all L_max"

print(f"\n  VERDICT: {verdict} -- {verdict_msg}")

# =============================================================================
# 11. SAVE AND PLOT
# =============================================================================
print("\n--- Saving results ---")

npz_path = os.path.join(base_dir, 's75_morse_bott_multi_lmax.npz')
save_dict = {
    'L_max_values': np.array(L_max_values),
    'verdict': verdict,
    'epsilon': epsilon,
    'tau_fold': tau_fold,
}
for L in L_max_values:
    r = results[L]
    save_dict[f'evals_36_L{L}'] = r['evals_36']
    save_dict[f'evals_35_L{L}'] = r['evals_35']
    save_dict[f'sig_36_L{L}'] = np.array(r['sig_36'])
    save_dict[f'sig_35_L{L}'] = np.array(r['sig_35'])
np.savez(npz_path, **save_dict)
print(f"  Saved: {npz_path}")

# Plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, L in enumerate(L_max_values):
    ax = axes[i]
    ev36 = results[L]['evals_36']
    ev35 = results[L]['evals_35']
    ax.bar(range(36), sorted(ev36), alpha=0.6, label='36D full', color='steelblue')
    ax.bar(range(35), sorted(ev35), alpha=0.6, label='35D VP', color='coral')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.set_title(f'L_max = {L}\n36D: {results[L]["sig_36"]}\n35D: {results[L]["sig_35"]}')
    ax.set_xlabel('Eigenvalue index')
    ax.set_ylabel('Hessian eigenvalue')
    ax.legend(fontsize=8)

plt.suptitle(f'S75-B4 Morse-Bott Multi-L_max: {verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
png_path = os.path.join(base_dir, 's75_morse_bott_multi_lmax.png')
plt.savefig(png_path, dpi=150)
print(f"  Saved: {png_path}")

t_total = time.time() - t_global_start
print(f"\n  TOTAL TIME: {t_total:.1f}s ({t_total/60:.1f} min)")
print(f"  Gate: {verdict}")
