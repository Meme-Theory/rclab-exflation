"""
DEBUG v9: Deep analysis of R_{u(2)} commutant.

This is the ONLY gauge choice giving center dim = 5 (matching A_F).
The J-compatible commutant has real dim 128 (too big for A_F = 24).
But A_F should be a SUBALGEBRA.

The Wedderburn decomposition shows 3 factors with the RIGHT center dim.
Let's see if the factor types match A_F = C + H + M_3(C).
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    gell_mann_matrices, su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix, LR_action_matrix,
)

np.set_printoptions(precision=6, linewidth=120, suppress=True)

# Setup
def get_column_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return flat_idx
    elif 4 <= flat_idx <= 6: return 0
    else: return (flat_idx - 7) % 3 + 1

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

basis_u2 = u2_basis_in_su3()
n = 32

# Build R_{u(2)} gauge generators on C^32
gens_16 = [R_action_matrix(v) for v in basis_u2]

rho_gens = []
for g16 in gens_16:
    g_minus = G5 @ np.conj(g16) @ G5
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = g16
    g32[16:, 16:] = g_minus
    rho_gens.append(g32)

# Gauge commutant
constraint_blocks = []
for rv in rho_gens:
    block = np.zeros((n*n, n*n), dtype=complex)
    for i in range(n):
        for j in range(n):
            row = i*n + j
            for k in range(n):
                block[row, i*n+k] += rv[k, j]
                block[row, k*n+j] -= rv[i, k]
    constraint_blocks.append(block)

A = np.vstack(constraint_blocks)
ns = null_space(A, rcond=1e-10)
d_gauge = ns.shape[1]
print(f"Gauge commutant complex dim: {d_gauge}")

comm_basis = [ns[:, k].reshape(n, n) for k in range(d_gauge)]

# J-constraint
d = d_gauge
A_mats = [(comm_basis[k] @ Xi - Xi @ np.conj(comm_basis[k])).flatten() for k in range(d)]
B_mats = [(comm_basis[k] @ Xi + Xi @ np.conj(comm_basis[k])).flatten() for k in range(d)]

C_mat = np.zeros((2 * n * n, 2 * d))
for m in range(n * n):
    for k in range(d):
        C_mat[2*m, k] = A_mats[k][m].real
        C_mat[2*m, d+k] = -B_mats[k][m].imag
        C_mat[2*m+1, k] = A_mats[k][m].imag
        C_mat[2*m+1, d+k] = B_mats[k][m].real

ns_J = null_space(C_mat, rcond=1e-10)
J_null_dim = ns_J.shape[1]

Jbasis = []
for idx in range(J_null_dim):
    coeffs = ns_J[:, idx]
    T = sum((coeffs[k] + 1j*coeffs[d+k]) * comm_basis[k] for k in range(d))
    Jbasis.append(T)

# Real orthonormal basis
real_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in Jbasis]
V = np.column_stack(real_vecs)
Q = orth(V)
d_orth = Q.shape[1]
print(f"J-compatible commutant real dim: {d_orth}")

n_flat = n * n
orth_basis = [(Q[:, k][:n_flat] + 1j * Q[:, k][n_flat:]).reshape(n, n) for k in range(d_orth)]

# Structure constants
struct_const = np.zeros((d_orth, d_orth, d_orth))
max_resid = 0
for i in range(d_orth):
    for j in range(d_orth):
        prod = orth_basis[i] @ orth_basis[j]
        pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
        coeffs = Q.T @ pv
        struct_const[i, j, :] = coeffs
        resid = np.linalg.norm(pv - Q @ coeffs)
        max_resid = max(max_resid, resid)
print(f"Closure: {max_resid:.2e}")

# Center
comm_sc = struct_const - struct_const.transpose(1, 0, 2)
center_rows = []
for j in range(d_orth):
    for k in range(d_orth):
        center_rows.append(comm_sc[:, j, k])
center_mat = np.array(center_rows)
center_ns = null_space(center_mat, rcond=1e-8)
center_dim = center_ns.shape[1]
print(f"Center dim: {center_dim}")

# ===================================================================
# WEDDERBURN DECOMPOSITION
# ===================================================================

print("\n" + "=" * 70)
print("WEDDERBURN DECOMPOSITION")
print("=" * 70)

center_basis = [sum(center_ns[i, idx] * orth_basis[i] for i in range(d_orth))
               for idx in range(center_dim)]

np.random.seed(42)
rc = np.random.randn(center_dim)
gc = sum(c * T for c, T in zip(rc, center_basis))

evals, evecs = np.linalg.eig(gc)

# Merge conjugate pairs
tol = 1e-3
used = np.zeros(32, dtype=bool)
factors = []
for i in range(32):
    if used[i]: continue
    ev = evals[i]
    close = np.abs(evals - ev) < tol
    close_conj = np.abs(evals - np.conj(ev)) < tol
    idx_set = np.where(close | close_conj)[0]
    for idx in idx_set: used[idx] = True
    V_ev = evecs[:, idx_set]

    # Project algebra onto this eigenspace
    proj_vecs = [np.concatenate([(V_ev.conj().T @ T @ V_ev).flatten().real,
                                 (V_ev.conj().T @ T @ V_ev).flatten().imag])
                for T in orth_basis]
    P = np.column_stack(proj_vecs)
    fr = np.linalg.matrix_rank(P, tol=1e-6)

    is_real = np.abs(ev.imag) < tol
    factors.append({
        'ev': ev, 'is_real': is_real,
        'dim_V': len(idx_set), 'alg_rank': fr,
        'V': V_ev
    })

    # Identify
    ident = ""
    dv = len(idx_set)
    for nn in range(1, 10):
        if fr == nn**2 and dv == nn: ident += f"M_{nn}(R) "
        if fr == nn**2 and dv == 2*nn: ident += f"M_{nn}(R)_embed "
        if fr == 2*nn**2 and dv == nn: ident += f"M_{nn}(C) "
        if fr == 2*nn**2 and dv == 2*nn: ident += f"M_{nn}(C)_embed "
        if fr == 4*nn**2 and dv == 2*nn: ident += f"M_{nn}(H) "
    if fr == 1 and dv == 1: ident = "R "
    if fr == 2 and dv == 2: ident = "C "
    if fr == 2 and dv == 1: ident = "C_half "
    if fr == 4 and dv == 2: ident = "H "

    print(f"  Factor: {'REAL' if is_real else 'CPAIR'} ev={ev:.4f}, dim_V={dv}, alg_rank(real)={fr}  {ident}")

total_V = sum(f['dim_V'] for f in factors)
total_A = sum(f['alg_rank'] for f in factors)
print(f"\nTotal: dim_V={total_V}, alg_rank={total_A}")

# ===================================================================
# Detailed factor analysis
# ===================================================================

print("\n" + "=" * 70)
print("DETAILED FACTOR ANALYSIS")
print("=" * 70)

for f_idx, f in enumerate(factors):
    V_f = f['V']
    dim_V = f['dim_V']
    fr = f['alg_rank']

    print(f"\nFactor {f_idx}: dim_V={dim_V}, alg_rank={fr}, {'REAL' if f['is_real'] else 'CPAIR'}")

    # Project algebra onto eigenspace
    proj_basis_raw = [V_f.conj().T @ T @ V_f for T in orth_basis]

    # Orthonormalize projected basis
    pvecs = np.column_stack([np.concatenate([T.flatten().real, T.flatten().imag])
                            for T in proj_basis_raw])
    Q_f = orth(pvecs)
    d_f = Q_f.shape[1]

    nf = dim_V
    fb = [(Q_f[:, k][:nf*nf] + 1j * Q_f[:, k][nf*nf:]).reshape(nf, nf) for k in range(d_f)]

    print(f"  Projected algebra dim: {d_f}")

    # Check commutativity
    max_comm = 0
    for i in range(min(d_f, 20)):
        for j in range(min(d_f, 20)):
            comm = fb[i] @ fb[j] - fb[j] @ fb[i]
            max_comm = max(max_comm, np.linalg.norm(comm))
    print(f"  Commutativity: {'YES' if max_comm < 1e-6 else f'NO (max={max_comm:.2e})'}")

    # Check if identity is in factor
    id_f = np.eye(nf, dtype=complex)
    id_fv = np.concatenate([id_f.flatten().real, id_f.flatten().imag])
    id_proj = Q_f @ (Q_f.T @ id_fv)
    id_r = np.linalg.norm(id_fv - id_proj)
    print(f"  Identity in factor: {'YES' if id_r < 1e-6 else f'NO (resid={id_r:.2e})'}")

    # Compute factor center
    if d_f > 0 and d_f <= 30:
        fsc = np.zeros((d_f, d_f, d_f))
        max_fr = 0
        for i in range(d_f):
            for j in range(d_f):
                prod = fb[i] @ fb[j]
                pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
                coeffs = Q_f.T @ pv
                fsc[i, j, :] = coeffs
                resid = np.linalg.norm(pv - Q_f @ coeffs)
                max_fr = max(max_fr, resid)

        if max_fr < 1e-6:
            fcomm = fsc - fsc.transpose(1, 0, 2)
            fcr = []
            for j in range(d_f):
                for k in range(d_f):
                    fcr.append(fcomm[:, j, k])
            fcm = np.array(fcr)
            fcns = null_space(fcm, rcond=1e-8)
            print(f"  Factor center dim: {fcns.shape[1]}")
            print(f"  Factor closure: {max_fr:.2e}")

    # Which particles does this factor act on?
    # Check which Psi_+ indices have nonzero projection onto V_f
    print(f"  Particle content (overlap with Psi_+ basis vectors):")
    particle_names = [
        'nu_R', 'u_R^r', 'u_R^g', 'u_R^b',
        'e_R', 'nu_L', 'e_L',
        'd_R^r', 'd_R^g', 'd_R^b',
        'u_L^r', 'u_L^g', 'u_L^b',
        'd_L^r', 'd_L^g', 'd_L^b',
    ]
    anti_names = ['anti_' + p for p in particle_names]

    for k in range(32):
        e_k = np.zeros(32, dtype=complex)
        e_k[k] = 1
        # Project onto V_f
        proj = V_f @ (V_f.conj().T @ e_k)
        overlap = np.linalg.norm(proj)
        if overlap > 0.1:
            name = particle_names[k] if k < 16 else anti_names[k-16]
            print(f"    idx {k:>2}: {name:>15}  overlap={overlap:.4f}")

print("\n\n--- SUMMARY ---")
print(f"R_{{u(2)}} J-compatible commutant: real dim {d_orth}, center dim {center_dim}")
print(f"Factors:")
for f in factors:
    print(f"  dim_V={f['dim_V']}, alg_rank={f['alg_rank']}")
print(f"\nA_F = C + H + M_3(C):")
print(f"  Center dim: 5 (MATCHES: {center_dim})")
print(f"  Real dim: 24 (GOT: {d_orth})")
print(f"  Factors: C(dim_V=2, rank=2), H(dim_V=2, rank=4), M_3(C)(dim_V=6, rank=18)")

print("\nDone.")
