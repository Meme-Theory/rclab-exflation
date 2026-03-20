"""
DEBUG SCRIPT v3: Test with FULL gauge group u(2)_L x su(3)_R.

Hypothesis: The J-compatible commutant is too big (80-dim) because we only
use u(2)_{L+R}, not the full gauge algebra. In Baptista's framework:
- L: left su(3) action (but only u(2) part is a homomorphism via L+R)
- R: right su(3) action (full su(3) is a homomorphism)

The correct gauge algebra might be:
  A_L in u(2), A_R in su(3)
  Combined: u(2)_{L+R} for the u(2) part, plus R_{su(3)} for the full right action.

Actually: let's test THREE options:
(a) u(2)_{L+R} only (what Phase 1 used) -- gives 80-dim
(b) u(2)_{L+R} + R_{su(3) complement} -- the R action of the su(3)/u(2) complement
(c) Full u(2)_L + su(3)_R separately
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

# Build G5, Xi
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
basis_su3 = su3_basis()  # full su(3) basis

def rho_plus_LR(v):
    return LR_action_matrix(v)

def rho_plus_L(v):
    return L_action_matrix(v)

def rho_plus_R(v):
    return R_action_matrix(v)

def rho_minus_from_plus(rho_plus_v):
    """Conjugate representation on Psi_-."""
    return G5 @ np.conj(rho_plus_v) @ G5

n = 32

def compute_commutant_and_center(label, gen_list_16):
    """Compute gauge commutant, J-compatible commutant, and center.

    gen_list_16: list of 16x16 matrices (gauge generators on Psi_+).
    """
    print(f"\n{'='*70}")
    print(f"GAUGE: {label}")
    print(f"{'='*70}")

    # Build 32x32 generators
    gens_32 = []
    for g16 in gen_list_16:
        g_minus = G5 @ np.conj(g16) @ G5
        g32 = np.zeros((32, 32), dtype=complex)
        g32[:16, :16] = g16
        g32[16:, 16:] = g_minus
        gens_32.append(g32)

    print(f"  Number of generators: {len(gens_32)}")

    # Build constraint matrix
    constraint_blocks = []
    for rv in gens_32:
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
    print(f"  Gauge commutant complex dim: {d_gauge}")

    if d_gauge == 0:
        print(f"  Commutant is trivial!")
        return

    comm_basis = [ns[:, k].reshape(n, n) for k in range(d_gauge)]

    # J-constraint: T*Xi = Xi*conj(T)
    # Using the correct J-constraint formulation
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

    rank_C = np.linalg.matrix_rank(C_mat, tol=1e-8)
    J_null_dim = 2*d - rank_C
    print(f"  J-constraint rank: {rank_C}, null dim: {J_null_dim}")

    ns_J = null_space(C_mat, rcond=1e-10)
    J_null_dim = ns_J.shape[1]

    Jbasis = []
    for idx in range(J_null_dim):
        coeffs = ns_J[:, idx]
        alphas = coeffs[:d]
        betas = coeffs[d:]
        T = sum((alphas[k] + 1j*betas[k]) * comm_basis[k] for k in range(d))
        Jbasis.append(T)

    # Build real basis
    real_basis_vecs = []
    for T in Jbasis:
        v = np.concatenate([T.flatten().real, T.flatten().imag])
        real_basis_vecs.append(v)

    V = np.column_stack(real_basis_vecs)
    Q = orth(V)
    d_orth = Q.shape[1]
    print(f"  J-compatible commutant real dim: {d_orth}")

    if d_orth == 0:
        print(f"  J-compatible commutant is trivial!")
        return

    n_flat = n * n
    orth_basis = [(Q[:, k][:n_flat] + 1j * Q[:, k][n_flat:]).reshape(n, n) for k in range(d_orth)]

    # Check identity
    id_rv = np.concatenate([np.eye(n).flatten().real, np.eye(n).flatten().imag])
    id_proj = Q @ (Q.T @ id_rv)
    id_resid = np.linalg.norm(id_rv - id_proj)
    print(f"  Identity in algebra? Residual: {id_resid:.2e}")

    # Structure constants (real)
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

    print(f"  Closure: {max_resid:.2e}")

    # Center
    comm_sc = struct_const - struct_const.transpose(1, 0, 2)
    center_rows = []
    for j in range(d_orth):
        for k in range(d_orth):
            center_rows.append(comm_sc[:, j, k])

    center_mat = np.array(center_rows)
    center_ns = null_space(center_mat, rcond=1e-8)
    center_dim = center_ns.shape[1]
    print(f"  Center dim: {center_dim}")

    if center_dim > 0:
        # Wedderburn decomposition
        np.random.seed(42)
        rc = np.random.randn(center_dim)
        gc = sum(c * sum(center_ns[i, idx] * orth_basis[i]
                        for i in range(d_orth))
                for idx, c in enumerate(rc))

        evals, evecs = np.linalg.eig(gc)
        er = np.round(evals, 4)
        ue = np.unique(er)

        print(f"  Wedderburn: {len(ue)} simple factors")
        for ev in ue:
            mask = np.abs(er - ev) < 5e-4
            mult = np.sum(mask)
            V_ev = evecs[:, mask]

            proj_vecs = []
            for T in orth_basis:
                T_p = V_ev.conj().T @ T @ V_ev
                pv = np.concatenate([T_p.flatten().real, T_p.flatten().imag])
                proj_vecs.append(pv)

            P = np.column_stack(proj_vecs)
            fr = np.linalg.matrix_rank(P, tol=1e-6)

            # Identify
            ident = ""
            for nn in range(1, 10):
                if fr == nn**2 and mult == nn: ident += f"M_{nn}(R) "
                if fr == nn**2 and mult == 2*nn: ident += f"M_{nn}(R)_embed "
                if fr == 2*nn**2 and mult == nn: ident += f"M_{nn}(C) "
                if fr == 4*nn**2 and mult == 2*nn: ident += f"M_{nn}(H) "
                if fr == 1 and mult == 1: ident = "R "
                if fr == 2 and mult == 2: ident = "C "
                if fr == 2 and mult == 1: ident = "C_half "  # ??
                if fr == 4 and mult == 2: ident = "H "

            print(f"    ev={ev:.4f}: H_dim={mult}, alg_dim(real)={fr}  {ident}")

        total_H = sum(np.sum(np.abs(er - ev) < 5e-4) for ev in ue)
        total_A = sum(np.linalg.matrix_rank(
            np.column_stack([np.concatenate([(evecs[:, np.abs(er-ev)<5e-4].conj().T @ T @ evecs[:, np.abs(er-ev)<5e-4]).flatten().real,
                                             (evecs[:, np.abs(er-ev)<5e-4].conj().T @ T @ evecs[:, np.abs(er-ev)<5e-4]).flatten().imag])
                             for T in orth_basis]), tol=1e-6)
            for ev in ue)
        print(f"  Total H_dim: {total_H}, Total alg_dim: {total_A}")

    return d_orth, center_dim


# ===================================================================
# TEST (a): u(2)_{L+R} only (Phase 1 gauge group)
# ===================================================================

gens_a = [rho_plus_LR(v) for v in basis_u2]
compute_commutant_and_center("u(2)_{L+R} [Phase 1]", gens_a)

# ===================================================================
# TEST (b): u(2)_{L+R} + R_{su(3)} (add full right su(3) action)
# ===================================================================

# The right action R_v is a homomorphism for ALL v in su(3)
gens_b = list(gens_a)  # start with u(2)_{L+R}
for v in basis_su3:
    gens_b.append(rho_plus_R(v))  # add R_v for each su(3) basis element

compute_commutant_and_center("u(2)_{L+R} + R_{su(3)}", gens_b)

# ===================================================================
# TEST (c): L_{u(2)} + R_{su(3)} separately
# ===================================================================

# L_v for v in u(2) (not combined with R)
gens_c = []
for v in basis_u2:
    gens_c.append(rho_plus_L(v))  # just L
for v in basis_su3:
    gens_c.append(rho_plus_R(v))  # full R

compute_commutant_and_center("L_{u(2)} + R_{su(3)} (separate)", gens_c)

# ===================================================================
# TEST (d): R_{su(3)} ONLY
# ===================================================================

gens_d = [rho_plus_R(v) for v in basis_su3]
compute_commutant_and_center("R_{su(3)} only", gens_d)

# ===================================================================
# TEST (e): L+R for u(2) and R for complement su(3)/u(2)
# ===================================================================

# The complement of u(2) in su(3) consists of the off-diagonal generators
# In the lambda_i basis: u(2) = span(lambda_1, lambda_2, lambda_3, lambda_8)
# Complement = span(lambda_4, lambda_5, lambda_6, lambda_7)
# The su3_basis is e_j = -i*lambda_j/2

gens_e = list(gens_a)  # u(2)_{L+R}
# Add R_v for the complement (lambda_4, lambda_5, lambda_6, lambda_7)
# In su3_basis, these are indices 3,4,5,6 (0-indexed: lambda_{j+1})
# Actually, su3_basis() returns 8 elements corresponding to lambda_1..lambda_8
# The u(2) embedding maps u(2) basis to specific su(3) elements

# Let me just add R_v for ALL su(3) basis elements -- the u(2) part of R is
# already partially captured in L+R, but adding it again doesn't hurt
# (just adds redundant constraints)
for v in basis_su3:
    gens_e.append(rho_plus_R(v))

print("\n(Test (e) is same as test (b))")

print("\nDone.")
