"""
PHASE 2.5b: Order-One on the 40-dim L-closure algebra
======================================================

The 40-dim algebra (from L_{su(3)} + H closure) IS in the R_{u(2)} commutant
and IS J-compatible. It has 4 Wedderburn factors: C(2)+C(2)+M_3(C)(18)+M_3(C)(18).

The target is to reduce 40 -> 24 using the order-one condition with D_F.
D_F should closure the "lepton pseudo-color" M_3(C) factor, leaving C+H+M_3(C)_quarks.

This approach uses the LEFT algebra (which lives in the commutant) rather than
the bimodule A_F (which has M_3(C) columns outside the commutant).

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
from scipy.linalg import orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

# ── Infrastructure (same as other scripts) ──

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
gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)

def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5

def build_full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32

def flat_idx(row, col):
    if row == 0 and col == 0: return 0
    if row == 0: return col
    if col == 0: return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


# =============================================================================
# PART 1: Build the 40-dim L-closure algebra
# =============================================================================

print("=" * 76)
print("BUILDING 40-DIM L-CLOSURE ALGEBRA (L_{su(3)} + H)")
print("=" * 76)

basis_su3 = su3_basis()

# L_{su(3)} generators (8 generators)
L_gens_16 = [L_action_matrix(v) for v in basis_su3]
L_gens_32 = [build_full_32(g) for g in L_gens_16]

# H generators (j and k only -- i is already in L_{su(3)} span)
# H_j: rows 2-3 mixing (left action)
def build_left_action_16(L4):
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for k in range(4):
            if abs(L4[i, k]) < 1e-15:
                continue
            for j in range(4):
                fi = flat_idx(i, j)
                fk = flat_idx(k, j)
                gen[fi, fk] += L4[i, k]
    return gen

L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
Hj_16 = build_left_action_16(L_Hj)
Hj_32 = build_full_32(Hj_16)

L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
Hk_16 = build_left_action_16(L_Hk)
Hk_32 = build_full_32(Hk_16)

# Combine all generators
all_gens_32 = L_gens_32 + [Hj_32, Hk_32]
all_names = [f'L_{i}' for i in range(8)] + ['H_j', 'H_k']

# Compute algebraic closure
print("\n  Computing algebraic closure of L_{su(3)} + {H_j, H_k}...")

n_flat = 32 * 32
gen_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in all_gens_32]
Q_cur = orth(np.column_stack(gen_vecs))
d_cur = Q_cur.shape[1]
print(f"  Initial span: {d_cur}")

for iteration in range(15):
    cur_basis = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                 for k in range(d_cur)]
    new_vecs = []
    for T1 in cur_basis:
        for T2 in all_gens_32:
            prod = T1 @ T2
            pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
            coeffs = Q_cur.T @ pv
            resid = np.linalg.norm(pv - Q_cur @ coeffs)
            if resid > 1e-8:
                new_vecs.append(pv)
    if not new_vecs:
        break
    all_v = np.column_stack([Q_cur] + [np.column_stack(new_vecs)])
    Q_new = orth(all_v)
    d_new = Q_new.shape[1]
    if d_new == d_cur:
        break
    print(f"    Iteration {iteration+1}: dim {d_cur} -> {d_new}")
    Q_cur = Q_new
    d_cur = d_new

print(f"  Final closure dimension: {d_cur}")

# Extract basis matrices
closure_basis_32 = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                    for k in range(d_cur)]


# =============================================================================
# PART 2: Construct D_F from Baptista non-homomorphism
# =============================================================================

print(f"\n{'=' * 76}")
print("D_F CONSTRUCTION FROM BAPTISTA EQ 2.65")
print(f"{'=' * 76}")

# D_F couples c (flat 1-3) <-> b (flat 4-6)
# Use identity Yukawa first, then generic

# Identity Yukawa D_F on Psi_+ (16x16)
D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0  # c_j -> b_j
    D_F_16[j+4, j+1] = 1.0  # b_j -> c_j

# Extend to C^32 (block diagonal, J-compatible)
D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = G5 @ np.conj(D_F_16) @ G5

print(f"  D_F hermitian: {np.max(np.abs(D_F_32 - D_F_32.conj().T)):.2e}")
print(f"  D_F J-compatible: {np.max(np.abs(D_F_32 @ Xi - Xi @ np.conj(D_F_32))):.2e}")


# =============================================================================
# PART 3: Order-one on the 40-dim closure
# =============================================================================

print(f"\n{'=' * 76}")
print("ORDER-ONE ON 40-DIM CLOSURE: [[D_F, a], Xi b^T Xi] = 0")
print(f"{'=' * 76}")

# For each pair (a, b) from the closure basis, compute [[D_F, a], Xi b^T Xi]
# and build the constraint matrix.

# The order-one condition [[D_F, a], o(b)] = 0 for all b in the algebra
# is LINEAR in a (for fixed D_F and b). So we can find the subspace of a's
# that satisfy order-one.

# For each basis element a_i of the closure, and each basis element b_j,
# compute C_{ij} = [[D_F, a_i], o(b_j)].
# We want to find the subspace of coefficients x_i such that
# sum_i x_i C_{ij} = 0 for all j.

# Vectorize: flatten C_{ij} into a constraint row.
# For each j, the constraint is: sum_i x_i * vec(C_{ij}) = 0.
# This gives a large linear system in the x_i.

print(f"\n  Building order-one constraint matrix...")
print(f"  Closure dim: {d_cur}")
print(f"  Each constraint: vectorized [[D_F, a_i], o(b_j)] for each b_j")

# Build constraint matrix
n_constraints_per_b = 2 * 32 * 32  # real + imag parts of 32x32 matrix
total_constraints = d_cur * n_constraints_per_b  # for all b_j

# This is huge: 40 * 2048 = 81920 constraints on 40 variables.
# But many are redundant. Let's build and rank-check.

# More efficient: for each b_j, build the 40-dim constraint vector
# (entries = max-abs of [[D_F, a_i], o(b_j)], but we need EXACT zeros)

# Actually, let me vectorize differently.
# For the subspace of a satisfying [[D_F, a], o(b)] = 0 for ALL b,
# we need: for each b in the closure basis, [D_F, a] commutes with o(b).
# This means [D_F, a] is in the COMMUTANT of {o(b) : b in closure}.
#
# The o-map: o(b) = Xi @ b.T @ Xi
# The set {o(b) : b in closure} is a 40-dim algebra (o is an anti-automorphism).
# The commutant of this 40-dim algebra in End(C^32) has some dimension d_c.
# Then [D_F, a] must lie in this commutant.
#
# But this is complicated. Let me just build the constraint directly.

# For each b_j: compute the 40x(2*1024) constraint
# constraint_row = vec([[D_F, a_i], o(b_j)]) for each a_i

# Stack all constraints and find the null space.

# Flatten into real representation: vec(T) = [Re(T.flatten()); Im(T.flatten())]
def vec_real(T):
    return np.concatenate([T.flatten().real, T.flatten().imag])

# Precompute o(b_j) for each basis element
o_basis = [Xi @ T.T @ Xi for T in closure_basis_32]

# Precompute [D_F, a_i] for each basis element
D_comm = [D_F_32 @ T - T @ D_F_32 for T in closure_basis_32]

# For each b_j, the order-one constraint on coefficients x = (x_1, ..., x_d):
# sum_i x_i * [[D_F, a_i], o(b_j)] = 0
# i.e., sum_i x_i * (D_comm_i @ o_j - o_j @ D_comm_i) = 0

# Build the full constraint matrix: each row is vec(D_comm_i @ o_j - o_j @ D_comm_i)
# for a specific (i,j) pair. We want null space in x.

# But this grows large. Let's be smarter: for each j, compute the d_cur x d_real matrix
# where d_real = 2*32*32 = 2048.

# Actually, the most efficient approach: compute the d_cur x d_cur matrix
# of "violation magnitudes" and check which a's give zero violations.

# Even simpler: for each a_i, compute max_j |[[D_F, a_i], o(b_j)]|.
# If this is < eps, a_i satisfies order-one.

print(f"\n  Testing each closure basis element for order-one compliance:")

o1_per_basis = np.zeros(d_cur)
for i in range(d_cur):
    max_err = 0
    for j in range(d_cur):
        double_comm = D_comm[i] @ o_basis[j] - o_basis[j] @ D_comm[i]
        err = np.max(np.abs(double_comm))
        max_err = max(max_err, err)
    o1_per_basis[i] = max_err

n_pass = np.sum(o1_per_basis < 1e-8)
n_near = np.sum(o1_per_basis < 1e-4)
print(f"  Basis elements passing order-one (<1e-8): {n_pass} / {d_cur}")
print(f"  Basis elements near-passing (<1e-4): {n_near} / {d_cur}")
print(f"  Max: {np.max(o1_per_basis):.6e}, Min: {np.min(o1_per_basis):.6e}")
print(f"  Distribution: {np.sort(o1_per_basis)[:10]}")

# Now find the LINEAR subspace satisfying order-one
# For each (j): sum_i x_i * vec(D_comm_i @ o_j - o_j @ D_comm_i) = 0

print(f"\n  Building full order-one constraint system...")

# Build constraint matrix: columns = basis elements, rows = constraints from (j, vec_component)
# We use a sampled approach: for each j, add the vectorized constraint
constraint_rows = []
for j in range(d_cur):
    for i in range(d_cur):
        double_comm = D_comm[i] @ o_basis[j] - o_basis[j] @ D_comm[i]
        constraint_rows.append(vec_real(double_comm))

# Stack: shape = (d_cur * d_cur, 2*1024)
C_stacked = np.array(constraint_rows)  # (d^2, 2048)

# Reshape to get constraint on x:
# For fixed j, the d_cur constraints are:
# row_i = vec(D_comm_i @ o_j - o_j @ D_comm_i)  for i = 0..d-1
# We need: sum_i x_i * row_i = 0  -> this is  C_j @ x = 0 where C_j is (2048, d)

# Build the constraint on x directly:
# For each j and each component k of the vectorized double commutator:
# sum_i x_i * C_stacked[j*d + i, k] = 0
# Rearrange: for each (j, k), constraint = C_stacked[j*d + :, k] (d-dim vector dotted with x)

# Actually, the constraint matrix A such that A @ x = 0:
# A has rows indexed by (j, k), columns by i
# A[(j,k), i] = C_stacked[j*d + i, k]

print(f"  Constraint matrix shape: {C_stacked.shape}")

# Rearrange to get A(row=(j,k), col=i)
n_j = d_cur
n_k = C_stacked.shape[1]
A_constraint = np.zeros((n_j * n_k, d_cur))
for j in range(n_j):
    for i in range(d_cur):
        A_constraint[j * n_k : (j+1) * n_k, i] = C_stacked[j * d_cur + i, :]

print(f"  A_constraint shape: {A_constraint.shape}")
print(f"  A_constraint rank: {np.linalg.matrix_rank(A_constraint, tol=1e-8)}")

# Find null space using thin SVD (avoids scipy overflow on tall-skinny matrices)
# A_constraint is (n_j*n_k, d_cur) -- very tall, very skinny
# null(A) = null(A^T A) for full column rank analysis
ATA = A_constraint.T @ A_constraint  # (d_cur, d_cur)
eigvals, eigvecs = np.linalg.eigh(ATA)
tol = 1e-8 * np.max(np.abs(eigvals))
null_mask = eigvals < tol
o1_null = eigvecs[:, null_mask]
o1_dim = o1_null.shape[1] if o1_null.size > 0 else 0
print(f"  Order-one subalgebra dimension: {o1_dim}")
print(f"  Eigenvalue spectrum of A^T A (smallest 10): {np.sort(eigvals)[:10]}")
print(f"  Tolerance used: {tol:.2e}")

if o1_dim > 0:
    # Extract the order-one subalgebra basis
    o1_basis_32 = []
    for k in range(o1_dim):
        coeffs = o1_null[:, k]
        T = sum(c * B for c, B in zip(coeffs, closure_basis_32))
        o1_basis_32.append(T)

    # Verify order-one for extracted basis
    print(f"\n  Verifying order-one on extracted {o1_dim}-dim subalgebra...")
    max_o1_verify = 0
    for i in range(o1_dim):
        Da = D_F_32 @ o1_basis_32[i] - o1_basis_32[i] @ D_F_32
        for j in range(o1_dim):
            ob = Xi @ o1_basis_32[j].T @ Xi
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            max_o1_verify = max(max_o1_verify, err)
    print(f"  Max |[[D_F, a], o(b)]|: {max_o1_verify:.2e}")

    # Check if it's a subalgebra (closed under multiplication)
    o1_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in o1_basis_32]
    Q_o1 = orth(np.column_stack(o1_vecs))
    max_prod_resid = 0
    for T1 in o1_basis_32:
        for T2 in o1_basis_32:
            prod = T1 @ T2
            pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
            coeffs_p = Q_o1.T @ pv
            resid = np.linalg.norm(pv - Q_o1 @ coeffs_p)
            max_prod_resid = max(max_prod_resid, resid)
    print(f"  Algebra closure residual: {max_prod_resid:.2e}")

    # Check order-zero on this subalgebra
    max_o0 = 0
    for i in range(o1_dim):
        for j in range(o1_dim):
            ob = Xi @ o1_basis_32[j].T @ Xi
            comm = o1_basis_32[i] @ ob - ob @ o1_basis_32[i]
            err = np.max(np.abs(comm))
            max_o0 = max(max_o0, err)
    print(f"  Order-zero on subalgebra: max = {max_o0:.2e}")


# =============================================================================
# PART 4: Try with generic Yukawa D_F
# =============================================================================

print(f"\n{'=' * 76}")
print("GENERIC YUKAWA D_F")
print(f"{'=' * 76}")

np.random.seed(42)
yukawa = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)

D_F_yuk_16 = np.zeros((16, 16), dtype=complex)
for i in range(3):
    for j in range(3):
        D_F_yuk_16[j+1, i+4] = yukawa[i, j]
        D_F_yuk_16[i+4, j+1] = np.conj(yukawa[i, j])

D_F_yuk_32 = np.zeros((32, 32), dtype=complex)
D_F_yuk_32[:16, :16] = D_F_yuk_16
D_F_yuk_32[16:, 16:] = G5 @ np.conj(D_F_yuk_16) @ G5

# Precompute
D_comm_yuk = [D_F_yuk_32 @ T - T @ D_F_yuk_32 for T in closure_basis_32]

# Build constraint
C_yuk = []
for j in range(d_cur):
    for i in range(d_cur):
        dc = D_comm_yuk[i] @ o_basis[j] - o_basis[j] @ D_comm_yuk[i]
        C_yuk.append(vec_real(dc))

C_yuk = np.array(C_yuk)
A_yuk = np.zeros((n_j * n_k, d_cur))
for j in range(n_j):
    for i in range(d_cur):
        A_yuk[j * n_k : (j+1) * n_k, i] = C_yuk[j * d_cur + i, :]

rank_yuk = np.linalg.matrix_rank(A_yuk, tol=1e-8)
ATA_yuk = A_yuk.T @ A_yuk
eigvals_yuk, eigvecs_yuk = np.linalg.eigh(ATA_yuk)
tol_yuk = 1e-8 * np.max(np.abs(eigvals_yuk))
null_mask_yuk = eigvals_yuk < tol_yuk
o1_null_yuk = eigvecs_yuk[:, null_mask_yuk]
o1_dim_yuk = o1_null_yuk.shape[1] if o1_null_yuk.size > 0 else 0

print(f"  Constraint rank: {rank_yuk}")
print(f"  Order-one subalgebra dim (Yukawa): {o1_dim_yuk}")
print(f"  Eigenvalue spectrum (smallest 10): {np.sort(eigvals_yuk)[:10]}")

if o1_dim_yuk > 0:
    o1_basis_yuk = []
    for k in range(o1_dim_yuk):
        coeffs = o1_null_yuk[:, k]
        T = sum(c * B for c, B in zip(coeffs, closure_basis_32))
        o1_basis_yuk.append(T)

    # Verify order-one
    max_o1_yuk = 0
    for i in range(o1_dim_yuk):
        Da = D_F_yuk_32 @ o1_basis_yuk[i] - o1_basis_yuk[i] @ D_F_yuk_32
        for j in range(o1_dim_yuk):
            ob = Xi @ o1_basis_yuk[j].T @ Xi
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            max_o1_yuk = max(max_o1_yuk, err)
    print(f"  Max |[[D_yuk, a], o(b)]|: {max_o1_yuk:.2e}")

    # Check algebra closure
    o1_vecs_yuk = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in o1_basis_yuk]
    Q_o1_yuk = orth(np.column_stack(o1_vecs_yuk))
    max_prod_yuk = 0
    for T1 in o1_basis_yuk:
        for T2 in o1_basis_yuk:
            prod = T1 @ T2
            pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
            coeffs_p = Q_o1_yuk.T @ pv
            resid = np.linalg.norm(pv - Q_o1_yuk @ coeffs_p)
            max_prod_yuk = max(max_prod_yuk, resid)
    print(f"  Algebra closure residual (Yukawa): {max_prod_yuk:.2e}")

    # Check order-zero
    max_o0_yuk = 0
    for i in range(o1_dim_yuk):
        for j in range(o1_dim_yuk):
            ob = Xi @ o1_basis_yuk[j].T @ Xi
            comm = o1_basis_yuk[i] @ ob - ob @ o1_basis_yuk[i]
            err = np.max(np.abs(comm))
            max_o0_yuk = max(max_o0_yuk, err)
    print(f"  Order-zero on Yukawa subalgebra: max = {max_o0_yuk:.2e}")


# =============================================================================
# PART 5: Wedderburn analysis of order-one subalgebra(s)
# =============================================================================

def analyze_wedderburn(basis_list, label):
    """Analyze the Wedderburn structure of an algebra given by basis matrices."""
    print(f"\n  === Wedderburn analysis: {label} (dim {len(basis_list)}) ===")
    d = len(basis_list)
    if d == 0:
        print(f"    Empty algebra, nothing to analyze.")
        return

    # Compute structure constants
    vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in basis_list]
    Q = orth(np.column_stack(vecs))
    actual_dim = Q.shape[1]
    print(f"    Independent dims: {actual_dim}")

    # Reconstruct orthonormal basis
    onb = [(Q[:, k][:32*32] + 1j * Q[:, k][32*32:]).reshape(32, 32) for k in range(actual_dim)]

    # Center: elements that commute with all others
    comm_mat = np.zeros((actual_dim * 2 * 32 * 32, actual_dim))
    for j in range(actual_dim):
        for i in range(actual_dim):
            c = onb[i] @ onb[j] - onb[j] @ onb[i]
            cv = np.concatenate([c.flatten().real, c.flatten().imag])
            comm_mat[j * 2 * 32 * 32 : (j+1) * 2 * 32 * 32, i] = cv

    # Center = null space of comm_mat
    CTC = comm_mat.T @ comm_mat
    evals, evecs = np.linalg.eigh(CTC)
    tol_c = 1e-8 * np.max(np.abs(evals)) if np.max(np.abs(evals)) > 0 else 1e-12
    center_mask = evals < tol_c
    center_dim = np.sum(center_mask)
    print(f"    Center dimension: {center_dim}")

    if center_dim > 0:
        center_coeffs = evecs[:, center_mask]
        center_mats = [sum(c * B for c, B in zip(center_coeffs[:, k], onb)) for k in range(center_dim)]

        # Find minimal central idempotents
        # First check if center elements are simultaneously diagonalizable
        print(f"    Center element norms: {[np.linalg.norm(T) for T in center_mats]}")

        # Check if identity is in the algebra
        I32 = np.eye(32, dtype=complex)
        Iv = np.concatenate([I32.flatten().real, I32.flatten().imag])
        coeffs_I = Q.T @ Iv
        resid_I = np.linalg.norm(Iv - Q @ coeffs_I)
        print(f"    Identity residual: {resid_I:.2e}")

    # Compute the radical: elements x such that Tr(xy) = 0 for all y
    # (Killing form of associative algebra = trace form)
    trace_form = np.zeros((actual_dim, actual_dim))
    for i in range(actual_dim):
        for j in range(actual_dim):
            trace_form[i, j] = np.real(np.trace(onb[i] @ onb[j]))

    tf_rank = np.linalg.matrix_rank(trace_form, tol=1e-8)
    radical_dim = actual_dim - tf_rank
    print(f"    Trace form rank: {tf_rank}, Radical dim: {radical_dim}")
    if radical_dim == 0:
        print(f"    -> Semisimple algebra (no radical)")
    else:
        print(f"    -> Has {radical_dim}-dim radical (NOT semisimple)")

    return actual_dim, center_dim, radical_dim

if o1_dim > 0:
    analyze_wedderburn(o1_basis_32, f"Order-one subalgebra (identity D_F)")

if o1_dim_yuk > 0:
    analyze_wedderburn(o1_basis_yuk, f"Order-one subalgebra (Yukawa D_F)")


# =============================================================================
# PART 6: Summary
# =============================================================================

print(f"\n{'=' * 76}")
print("SUMMARY: ORDER-ONE ON L-CLOSURE")
print(f"{'=' * 76}")
print(f"  Closure algebra dim: {d_cur}")
print(f"  D_F (identity Yukawa):")
print(f"    Constraint rank: {np.linalg.matrix_rank(A_constraint, tol=1e-8)}")
print(f"    Order-one subspace dim: {o1_dim}")
if o1_dim > 0:
    print(f"    Algebra closure: {'PASS' if max_prod_resid < 1e-8 else 'FAIL (residual ' + f'{max_prod_resid:.2e})'}")
    print(f"    Order-zero: {'PASS' if max_o0 < 1e-8 else 'FAIL (max ' + f'{max_o0:.2e})'}")
print(f"  D_F (random Yukawa):")
print(f"    Constraint rank: {rank_yuk}")
print(f"    Order-one subspace dim: {o1_dim_yuk}")
print(f"  Target: 24 (= C + H + M_3(C))")
print(f"  Key question: does order-one extract 24-dim semisimple with 3 factors?")
print(f"{'=' * 76}")
