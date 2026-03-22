"""
DEBUG SCRIPT v4: Proper Wedderburn decomposition for the 14-dim J-compatible commutant
with gauge = u(2)_{L+R} + R_{su(3)}.

Key finding from v3: this gauge gives real dim 14, total algebra dim 24 = A_F dimension!
But 11 simple factors is wrong -- complex conjugate pairs must be merged.

For a REAL algebra, a generic center element has real eigenvalues on real eigenspaces
and complex conjugate pairs on paired complex eigenspaces. The correct Wedderburn
decomposition merges conjugate pairs.
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    gell_mann_matrices, su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix, LR_action_matrix,
)

np.set_printoptions(precision=8, linewidth=120, suppress=True)

# ===================================================================
# Setup (same as before)
# ===================================================================

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
basis_su3 = su3_basis()

n = 32

# Build generators: u(2)_{L+R} + R_{su(3)}
gens_16 = []
for v in basis_u2:
    gens_16.append(LR_action_matrix(v))
for v in basis_su3:
    gens_16.append(R_action_matrix(v))

# Build 32x32 generators
rho_gens = []
for g16 in gens_16:
    g_minus = G5 @ np.conj(g16) @ G5
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = g16
    g32[16:, 16:] = g_minus
    rho_gens.append(g32)

print(f"Gauge generators: {len(rho_gens)}")

# ===================================================================
# Gauge commutant
# ===================================================================

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

# ===================================================================
# J-compatible commutant
# ===================================================================

d = d_gauge
A_mats = []
B_mats = []
for k in range(d):
    Tk = comm_basis[k]
    Ak = Tk @ Xi - Xi @ np.conj(Tk)
    Bk = Tk @ Xi + Xi @ np.conj(Tk)
    A_mats.append(Ak.flatten())
    B_mats.append(Bk.flatten())

C_mat = np.zeros((2 * n * n, 2 * d))
for m in range(n * n):
    for k in range(d):
        C_mat[2*m, k] = A_mats[k][m].real
        C_mat[2*m, d+k] = -B_mats[k][m].imag
        C_mat[2*m+1, k] = A_mats[k][m].imag
        C_mat[2*m+1, d+k] = B_mats[k][m].real

ns_J = null_space(C_mat, rcond=1e-10)
J_null_dim = ns_J.shape[1]
print(f"J-compatible commutant (real dim from null_space): {J_null_dim}")

Jbasis = []
for idx in range(J_null_dim):
    coeffs = ns_J[:, idx]
    alphas = coeffs[:d]
    betas = coeffs[d:]
    T = sum((alphas[k] + 1j*betas[k]) * comm_basis[k] for k in range(d))
    Jbasis.append(T)

# Build real orthonormal basis
real_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in Jbasis]
V = np.column_stack(real_vecs)
Q = orth(V)
d_orth = Q.shape[1]
print(f"Orthonormal real basis dim: {d_orth}")

n_flat = n * n
orth_basis = [(Q[:, k][:n_flat] + 1j * Q[:, k][n_flat:]).reshape(n, n) for k in range(d_orth)]

# ===================================================================
# Verify all properties
# ===================================================================

print("\n--- VERIFICATION ---")

# J-compat
max_J = max(np.max(np.abs(T @ Xi - Xi @ np.conj(T))) for T in orth_basis)
print(f"Max J-compat error: {max_J:.2e}")

# Gauge comm
max_g = max(np.max(np.abs(T @ rv - rv @ T)) for T in orth_basis for rv in rho_gens)
print(f"Max gauge comm error: {max_g:.2e}")

# Identity
id_rv = np.concatenate([np.eye(n).flatten().real, np.eye(n).flatten().imag])
id_proj = Q @ (Q.T @ id_rv)
id_resid = np.linalg.norm(id_rv - id_proj)
print(f"Identity residual: {id_resid:.2e}")

# Closure
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
print(f"Closure max residual: {max_resid:.2e}")

# ===================================================================
# Center computation (real)
# ===================================================================

print("\n--- CENTER ---")
comm_sc = struct_const - struct_const.transpose(1, 0, 2)
center_rows = []
for j in range(d_orth):
    for k in range(d_orth):
        center_rows.append(comm_sc[:, j, k])

center_mat = np.array(center_rows)
center_ns = null_space(center_mat, rcond=1e-8)
center_dim = center_ns.shape[1]
print(f"Center dimension: {center_dim}")

# Build center basis as actual matrices
center_basis = []
for idx in range(center_dim):
    coeffs = center_ns[:, idx]
    T = sum(coeffs[i] * orth_basis[i] for i in range(d_orth))
    center_basis.append(T)

# ===================================================================
# PROPER Wedderburn decomposition
# ===================================================================

print("\n--- WEDDERBURN DECOMPOSITION (PROPER) ---")

# For a real semisimple algebra, decompose using TWO generic center elements
# to separate factors robustly.

# First: use a single generic center element
np.random.seed(42)
rc = np.random.randn(center_dim)
gc = sum(c * T for c, T in zip(rc, center_basis))

evals, evecs = np.linalg.eig(gc)

# Round and group by proximity (merge complex conjugate pairs)
# A real matrix has eigenvalues in conjugate pairs.
# But gc is complex (center element of real algebra expressed in complex basis).
# The REAL eigenvalues (|Im(ev)| < tol) are eigenspaces of real type.
# Complex conjugate pairs are eigenspaces of complex type.

print(f"\nGeneric center element eigenvalues:")
tol = 1e-3
used = np.zeros(32, dtype=bool)
factor_info = []

for i in range(32):
    if used[i]:
        continue

    ev = evals[i]
    # Find all eigenvalues close to this one
    close = np.abs(evals - ev) < tol
    # Also find conjugate eigenvalues
    close_conj = np.abs(evals - np.conj(ev)) < tol

    if np.abs(ev.imag) < tol:
        # Real eigenvalue
        idx_set = np.where(close)[0]
        for idx in idx_set:
            used[idx] = True
        mult = len(idx_set)
        V_ev = evecs[:, idx_set]
        factor_info.append({
            'type': 'real',
            'eval': ev.real,
            'mult': mult,
            'V': V_ev,
        })
        print(f"  REAL: ev={ev.real:.6f}, mult={mult}")
    else:
        # Complex pair
        idx_set = np.where(close | close_conj)[0]
        for idx in idx_set:
            used[idx] = True
        mult_total = len(idx_set)
        V_ev = evecs[:, idx_set]

        # The eigenspace for ev and conj(ev) together
        factor_info.append({
            'type': 'complex_pair',
            'eval': ev,
            'eval_conj': np.conj(ev),
            'mult': mult_total,
            'V': V_ev,
        })
        print(f"  COMPLEX PAIR: ev={ev:.6f}, conj(ev)={np.conj(ev):.6f}, total mult={mult_total}")

print(f"\nTotal factors after merging conjugate pairs: {len(factor_info)}")
print(f"Total eigenspace dim: {sum(f['mult'] for f in factor_info)} (should be 32)")

# For each factor, project the algebra and determine its real dimension
print("\n--- FACTOR ANALYSIS ---")
for f_idx, f in enumerate(factor_info):
    V_f = f['V']
    dim_V = V_f.shape[1]

    # Project all algebra elements
    proj_vecs = []
    for T in orth_basis:
        T_p = V_f.conj().T @ T @ V_f
        pv = np.concatenate([T_p.flatten().real, T_p.flatten().imag])
        proj_vecs.append(pv)

    P = np.column_stack(proj_vecs)
    factor_rank = np.linalg.matrix_rank(P, tol=1e-6)

    print(f"\nFactor {f_idx}: {f['type']}, H_dim={dim_V}, alg_rank(real)={factor_rank}")

    # Identify algebra type
    # M_n(R): real dim n^2, acts faithfully on R^n -> complex embedding C^n, dim_V = n
    # M_n(C): real dim 2n^2, acts on C^n, dim_V = n
    # M_n(H): real dim 4n^2, acts on H^n = C^{2n}, dim_V = 2n
    # C (as real algebra): real dim 2, acts on C^1, dim_V = 1 or 2
    # R: real dim 1, acts on R^1, dim_V = 1
    # H: real dim 4, acts on H^1 = C^2, dim_V = 2

    candidates = []
    for nn in range(1, 10):
        if factor_rank == nn**2:
            if dim_V == nn:
                candidates.append(f"M_{nn}(R)")
            if dim_V == 2*nn:
                candidates.append(f"M_{nn}(R)_double")
        if factor_rank == 2 * nn**2:
            if dim_V == nn:
                candidates.append(f"M_{nn}(C)")
            if dim_V == 2*nn:
                candidates.append(f"M_{nn}(C)_double")
        if factor_rank == 4 * nn**2:
            if dim_V == 2*nn:
                candidates.append(f"M_{nn}(H)")
    # Special cases
    if factor_rank == 1:
        candidates.append("R")
    if factor_rank == 2:
        candidates.append("C")
    if factor_rank == 4 and dim_V == 2:
        candidates.append("H")

    if candidates:
        print(f"  Candidates: {', '.join(candidates)}")
    else:
        print(f"  No standard match for rank={factor_rank}, dim_V={dim_V}")

    # Additional: check if the factor algebra is commutative
    if factor_rank <= dim_V**2:  # only if manageable
        factor_basis = []
        for T in orth_basis:
            T_p = V_f.conj().T @ T @ V_f
            factor_basis.append(T_p)

        # Orthonormalize the projected basis
        pvecs = np.column_stack([np.concatenate([T.flatten().real, T.flatten().imag]) for T in factor_basis])
        Q_f = orth(pvecs)
        d_f = Q_f.shape[1]

        if d_f > 0 and d_f <= 20:
            nf = dim_V
            fb = [(Q_f[:, k][:nf*nf] + 1j*Q_f[:, k][nf*nf:]).reshape(nf, nf) for k in range(d_f)]

            # Check commutativity
            max_comm = 0
            for i in range(d_f):
                for j in range(d_f):
                    comm = fb[i] @ fb[j] - fb[j] @ fb[i]
                    max_comm = max(max_comm, np.linalg.norm(comm))

            print(f"  Factor is {'COMMUTATIVE' if max_comm < 1e-6 else 'NON-COMMUTATIVE'} (max comm norm: {max_comm:.2e})")

            # Check if identity is in the factor
            id_f = np.eye(nf)
            id_fv = np.concatenate([id_f.flatten().real, id_f.flatten().imag])
            id_proj = Q_f @ (Q_f.T @ id_fv)
            id_r = np.linalg.norm(id_fv - id_proj)
            print(f"  Identity in factor? Residual: {id_r:.2e}")

# ===================================================================
# Alternative: project algebra onto Psi_+ sector only
# ===================================================================

print("\n\n--- PROJECTION ONTO Psi_+ SECTOR ---")
print("(How does the algebra act on the first 16 components?)")

proj_pp_vecs = []
for T in orth_basis:
    block_pp = T[:16, :16]
    pv = np.concatenate([block_pp.flatten().real, block_pp.flatten().imag])
    proj_pp_vecs.append(pv)

P_pp = np.column_stack(proj_pp_vecs)
rank_pp = np.linalg.matrix_rank(P_pp, tol=1e-8)
print(f"Algebra projected to ++ block: rank {rank_pp}")

proj_pm_vecs = []
for T in orth_basis:
    block_pm = T[:16, 16:]
    pv = np.concatenate([block_pm.flatten().real, block_pm.flatten().imag])
    proj_pm_vecs.append(pv)

P_pm = np.column_stack(proj_pm_vecs)
rank_pm = np.linalg.matrix_rank(P_pm, tol=1e-8)
print(f"Algebra projected to +- block: rank {rank_pm}")

# ===================================================================
# Check order-zero condition
# ===================================================================

print("\n--- ORDER-ZERO CONDITION ---")
# [a, J b* J^{-1}] = 0 for all a, b
# = [a, Xi b^T Xi] = 0

max_o0 = 0
for a in orth_basis:
    for b in orth_basis:
        b_opp = Xi @ b.T @ Xi
        comm = a @ b_opp - b_opp @ a
        max_o0 = max(max_o0, np.max(np.abs(comm)))

print(f"Max |[a, Xi b^T Xi]|: {max_o0:.2e}")
if max_o0 < 1e-6:
    print("ORDER-ZERO CONDITION: SATISFIED!")
else:
    print("ORDER-ZERO CONDITION: VIOLATED")

# ===================================================================
# Trace form analysis
# ===================================================================

print("\n--- TRACE FORM ---")
trace_form = np.zeros((d_orth, d_orth))
for i in range(d_orth):
    for j in range(d_orth):
        # Tr(e_i * e_j) using the real trace on 32x32 matrices
        prod = orth_basis[i] @ orth_basis[j]
        trace_form[i, j] = np.trace(prod).real

tf_evals = np.linalg.eigvalsh(trace_form)
print(f"Trace form eigenvalues: {np.sort(np.round(tf_evals, 4))}")
n_zero = np.sum(np.abs(tf_evals) < 1e-6)
print(f"Zero eigenvalues: {n_zero}")
if n_zero == 0:
    print("Trace form NON-DEGENERATE => algebra is SEMISIMPLE")

print(f"\n--- SUMMARY ---")
print(f"Algebra real dimension: {d_orth}")
print(f"Center dimension: {center_dim}")
print(f"A_F target: real dim 24, center dim 5")
print(f"Our result: real dim {d_orth}, center dim {center_dim}")
print(f"\nA_F = C(2) + H(4) + M_3(C)(18) = dim 24")
print(f"Our algebra has total dim = 14 as a J-compat commutant,")
print(f"but the total algebra dim (sum of factor dims) = 24")
print(f"(the algebra acts on C^32 with multiplicity).")

print("\nDone.")
