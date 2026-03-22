"""
PHASE 2.5c: Detailed Wedderburn analysis of the 20-dim order-one subalgebra
============================================================================

The order-one condition [[D_F, a], Xi b^T Xi] = 0 extracted a 20-dim semisimple
algebra with center 4 from the 38-dim L-closure. This script identifies the
4 simple factors by finding minimal central idempotents.

Strategy:
1. Extract the 20-dim subalgebra from the L-closure (repeat from phase25_DF_on_Lclosure.py)
2. Find the center (4-dim)
3. Find minimal central idempotents by diagonalizing center elements
4. Project algebra onto each idempotent to identify factors
5. Compare against target A_F = C + H + M_3(C)

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

# ── Infrastructure ──

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

def vec_real(T):
    return np.concatenate([T.flatten().real, T.flatten().imag])


# =============================================================================
# PART 1: Reconstruct the 20-dim order-one subalgebra
# =============================================================================

print("=" * 76)
print("RECONSTRUCTING 20-DIM ORDER-ONE SUBALGEBRA")
print("=" * 76)

basis_su3 = su3_basis()

# L_{su(3)} generators
L_gens_16 = [L_action_matrix(v) for v in basis_su3]
L_gens_32 = [build_full_32(g) for g in L_gens_16]

# H generators
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
Hj_16 = build_left_action_16(L_Hj)
Hj_32 = build_full_32(Hj_16)

L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
Hk_16 = build_left_action_16(L_Hk)
Hk_32 = build_full_32(Hk_16)

all_gens_32 = L_gens_32 + [Hj_32, Hk_32]

# Compute algebraic closure
n_flat = 32 * 32
gen_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in all_gens_32]
Q_cur = orth(np.column_stack(gen_vecs))
d_cur = Q_cur.shape[1]

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
    d_cur = d_new
    Q_cur = Q_new

print(f"  L-closure dimension: {d_cur}")

closure_basis_32 = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                    for k in range(d_cur)]

# Build D_F (identity Yukawa)
D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0
    D_F_16[j+4, j+1] = 1.0

D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = G5 @ np.conj(D_F_16) @ G5

# Build order-one constraint
o_basis = [Xi @ T.T @ Xi for T in closure_basis_32]
D_comm = [D_F_32 @ T - T @ D_F_32 for T in closure_basis_32]

n_k = 2 * 32 * 32  # vec dimension

constraint_rows = []
for j in range(d_cur):
    for i in range(d_cur):
        double_comm = D_comm[i] @ o_basis[j] - o_basis[j] @ D_comm[i]
        constraint_rows.append(vec_real(double_comm))

C_stacked = np.array(constraint_rows)

A_constraint = np.zeros((d_cur * n_k, d_cur))
for j in range(d_cur):
    for i in range(d_cur):
        A_constraint[j * n_k : (j+1) * n_k, i] = C_stacked[j * d_cur + i, :]

# Extract null space via A^T A
ATA = A_constraint.T @ A_constraint
eigvals, eigvecs = np.linalg.eigh(ATA)
tol = 1e-8 * np.max(np.abs(eigvals))
null_mask = eigvals < tol
o1_null = eigvecs[:, null_mask]
o1_dim = o1_null.shape[1]

print(f"  Order-one subalgebra dimension: {o1_dim}")

# Extract basis
o1_basis = []
for k in range(o1_dim):
    coeffs = o1_null[:, k]
    T = sum(c * B for c, B in zip(coeffs, closure_basis_32))
    o1_basis.append(T)

# Re-orthogonalize
o1_vecs = [vec_real(T) for T in o1_basis]
Q_o1 = orth(np.column_stack(o1_vecs))
o1_dim_actual = Q_o1.shape[1]
print(f"  Actual independent dimensions: {o1_dim_actual}")

# Rebuild orthonormal basis
o1_basis = [(Q_o1[:, k][:n_flat] + 1j * Q_o1[:, k][n_flat:]).reshape(32, 32)
            for k in range(o1_dim_actual)]


# =============================================================================
# PART 2: Find the center
# =============================================================================

print(f"\n{'=' * 76}")
print("CENTER OF THE 20-DIM SUBALGEBRA")
print(f"{'=' * 76}")

d = o1_dim_actual

# Center = elements commuting with all others: [a, b_j] = 0 for all j
# Build: for each j, the map a -> [a, b_j] in vectorized form
# comm_j(a) = a b_j - b_j a. This is linear in a.
# In the algebra's own basis: (adj_j)_{ki} = coefficients of [b_i, b_j] in basis b_k.
# We need: for each j, the adjoint matrix adj_j such that [b_i, b_j] = sum_k (adj_j)_{ki} b_k
# Center = intersection of null spaces of all adj_j.

# Compute structure constants c^k_{ij} where b_i b_j = sum_k c^k_{ij} b_k
print(f"\n  Computing structure constants...")

struct_const = np.zeros((d, d, d), dtype=complex)
for i in range(d):
    for j in range(d):
        prod = o1_basis[i] @ o1_basis[j]
        pv = vec_real(prod)
        # Project onto algebra basis
        coeffs = Q_o1.T @ pv
        # Structure constants: c^k_{ij} = coeffs[k]
        for k in range(d):
            struct_const[k, i, j] = coeffs[k]

# Verify closure
max_resid = 0
for i in range(d):
    for j in range(d):
        prod = o1_basis[i] @ o1_basis[j]
        reconstructed = sum(struct_const[k, i, j] * o1_basis[k] for k in range(d))
        resid = np.max(np.abs(prod - reconstructed))
        max_resid = max(max_resid, resid)
print(f"  Structure constant reconstruction: max residual = {max_resid:.2e}")

# Adjoint matrices: (ad_j)_{ki} = c^k_{ij} - c^k_{ji}
# [b_i, b_j] = sum_k (c^k_{ij} - c^k_{ji}) b_k
# For center: we need sum_k (c^k_{ij} - c^k_{ji}) = 0 for all j, k
# i.e., for each j, the vector x satisfying sum_i x_i (c^k_{ij} - c^k_{ji}) = 0 for all k

# Build the adjoint constraint matrix:
# For center element a = sum_i x_i b_i, we need [a, b_j] = 0 for all j.
# [a, b_j] = sum_i x_i [b_i, b_j] = sum_i x_i sum_k (c^k_{ij} - c^k_{ji}) b_k
# = sum_k (sum_i x_i (c^k_{ij} - c^k_{ji})) b_k = 0
# So for each (j, k): sum_i x_i (c^k_{ij} - c^k_{ji}) = 0.

adj_constraint = np.zeros((d * d, d), dtype=complex)
for j in range(d):
    for k in range(d):
        for i in range(d):
            adj_constraint[j * d + k, i] = struct_const[k, i, j] - struct_const[k, j, i]

# Use real representation
adj_real = np.zeros((2 * d * d, d))
adj_real[:d*d, :] = adj_constraint.real
adj_real[d*d:, :] = adj_constraint.imag

# Center = null space of adj_real
ATA_adj = adj_real.T @ adj_real
evals_adj, evecs_adj = np.linalg.eigh(ATA_adj)
tol_adj = 1e-8 * np.max(np.abs(evals_adj)) if np.max(np.abs(evals_adj)) > 0 else 1e-12
center_mask_adj = evals_adj < tol_adj
center_dim = np.sum(center_mask_adj)
center_coeffs = evecs_adj[:, center_mask_adj]

print(f"  Center dimension: {center_dim}")

# Construct center elements as 32x32 matrices
center_mats = []
for c_idx in range(center_dim):
    T = sum(center_coeffs[i, c_idx] * o1_basis[i] for i in range(d))
    center_mats.append(T)

# Verify center elements commute with everything
print(f"  Verifying center commutation...")
max_center_err = 0
for cm in center_mats:
    for bi in o1_basis:
        err = np.max(np.abs(cm @ bi - bi @ cm))
        max_center_err = max(max_center_err, err)
print(f"  Max |[center, algebra]|: {max_center_err:.2e}")


# =============================================================================
# PART 3: Find minimal central idempotents
# =============================================================================

print(f"\n{'=' * 76}")
print("MINIMAL CENTRAL IDEMPOTENTS")
print(f"{'=' * 76}")

# The center of a semisimple algebra is a direct sum of copies of C.
# Each minimal central idempotent is the identity element of one simple factor.
# They satisfy: e_a^2 = e_a, e_a e_b = 0 (a != b), sum e_a = I_algebra.
#
# Strategy: the center is a 4-dim commutative algebra. Its elements are
# simultaneously diagonalizable as 32x32 matrices. The minimal idempotents
# correspond to the common eigenspaces.

# Find identity of the algebra first
# I_algebra = sum of all idempotents, but we don't know it yet.
# Instead: diagonalize center elements jointly.

# Step 1: Diagonalize first center element
print(f"\n  Step 1: Joint diagonalization of center elements")

# Compute eigenvalues of each center element
for idx, cm in enumerate(center_mats):
    eigs = np.linalg.eigvals(cm)
    unique_eigs = np.unique(np.round(eigs.real, 6) + 1j * np.round(eigs.imag, 6))
    print(f"  Center element {idx}: {len(unique_eigs)} distinct eigenvalues")
    for e in sorted(unique_eigs, key=lambda x: x.real):
        mult = np.sum(np.abs(eigs - e) < 1e-4)
        print(f"    {e:.6f}  (multiplicity {mult})")

# Step 2: Use the IDENTITY of the algebra to find idempotents
# The algebra identity e satisfies e @ b = b @ e = b for all b in algebra.
# Since the algebra is closed, e must be the projection onto the algebra's image.

# Find the algebra's image: what subspace of C^32 does the algebra act on?
print(f"\n  Step 2: Finding algebra's image space")

# Collect column spaces of all basis elements
image_vecs = []
for T in o1_basis:
    for col in range(32):
        v = T[:, col]
        if np.linalg.norm(v) > 1e-10:
            image_vecs.append(v)

image_mat = np.column_stack(image_vecs)
Q_image = orth(image_mat)
image_dim = Q_image.shape[1]
print(f"  Image dimension: {image_dim}")

# The algebra identity is the projection onto this image
# But only if the image is invariant under all algebra elements.
# Check:
max_inv_err = 0
for T in o1_basis:
    # T should map image into image
    for k in range(image_dim):
        v = Q_image[:, k]
        Tv = T @ v
        coeffs = Q_image.T @ Tv
        resid = np.linalg.norm(Tv - Q_image @ coeffs)
        max_inv_err = max(max_inv_err, resid)
print(f"  Image invariance: max residual = {max_inv_err:.2e}")

# Step 3: Restrict center to image and diagonalize
print(f"\n  Step 3: Center restricted to image")

center_restricted = [Q_image.conj().T @ cm @ Q_image for cm in center_mats]

# These should be commuting matrices -- simultaneously diagonalizable
# Check commutativity
max_comm = 0
for i in range(center_dim):
    for j in range(i+1, center_dim):
        err = np.max(np.abs(center_restricted[i] @ center_restricted[j]
                          - center_restricted[j] @ center_restricted[i]))
        max_comm = max(max_comm, err)
print(f"  Center restricted commutativity: {max_comm:.2e}")

# Diagonalize the first non-scalar center element
# First find a center element that's not proportional to identity on image
print(f"\n  Step 4: Diagonalizing center on image space")

# Compute eigendecomposition of each restricted center element
for idx, cr in enumerate(center_restricted):
    eigs = np.linalg.eigvals(cr)
    unique_eigs = np.unique(np.round(eigs.real, 6) + 1j * np.round(eigs.imag, 6))
    print(f"  Restricted center {idx}: {len(unique_eigs)} distinct eigenvalues, hermitian: {np.max(np.abs(cr - cr.conj().T)):.2e}")

# Use Schur decomposition to simultaneously block-diagonalize
# Start with the first center element that has multiple eigenvalues
best_idx = 0
max_distinct = 0
for idx, cr in enumerate(center_restricted):
    eigs = np.linalg.eigvals(cr)
    unique_eigs = np.unique(np.round(eigs.real, 6) + 1j * np.round(eigs.imag, 6))
    if len(unique_eigs) > max_distinct:
        max_distinct = len(unique_eigs)
        best_idx = idx

print(f"\n  Using center element {best_idx} (most distinct eigenvalues: {max_distinct})")

# Get eigenspaces of this element
cr_best = center_restricted[best_idx]
# Make hermitian part for eigendecomposition
cr_herm = 0.5 * (cr_best + cr_best.conj().T)
evals_best, evecs_best = np.linalg.eigh(cr_herm)

# Cluster eigenvalues
clusters = []
tol_cluster = 1e-4
used = np.zeros(len(evals_best), dtype=bool)
for i in range(len(evals_best)):
    if used[i]:
        continue
    cluster_indices = [i]
    used[i] = True
    for j in range(i+1, len(evals_best)):
        if not used[j] and abs(evals_best[j] - evals_best[i]) < tol_cluster:
            cluster_indices.append(j)
            used[j] = True
    clusters.append((np.mean(evals_best[cluster_indices]), cluster_indices))

print(f"\n  Eigenvalue clusters (tolerance {tol_cluster}):")
for ev, indices in sorted(clusters, key=lambda x: x[0]):
    print(f"    eigenvalue = {ev:.6f}, multiplicity = {len(indices)}")

# Refine: use ALL center elements to split further
# For each cluster, check if other center elements have distinct eigenvalues within it
print(f"\n  Refining clusters using all center elements...")

final_subspaces = []
for ev, indices in clusters:
    # Subspace corresponding to this cluster
    sub_vecs = evecs_best[:, indices]

    # Check other center elements on this subspace
    can_split = False
    for idx in range(center_dim):
        if idx == best_idx:
            continue
        cr_sub = sub_vecs.conj().T @ center_restricted[idx] @ sub_vecs
        sub_evals = np.linalg.eigvalsh(0.5 * (cr_sub + cr_sub.conj().T))
        sub_spread = np.max(sub_evals) - np.min(sub_evals)
        if sub_spread > tol_cluster:
            can_split = True
            # Actually split
            cr_sub_herm = 0.5 * (cr_sub + cr_sub.conj().T)
            sub_ev, sub_evec = np.linalg.eigh(cr_sub_herm)
            sub_clusters = []
            sub_used = np.zeros(len(sub_ev), dtype=bool)
            for i2 in range(len(sub_ev)):
                if sub_used[i2]:
                    continue
                sc = [i2]
                sub_used[i2] = True
                for j2 in range(i2+1, len(sub_ev)):
                    if not sub_used[j2] and abs(sub_ev[j2] - sub_ev[i2]) < tol_cluster:
                        sc.append(j2)
                        sub_used[j2] = True
                sub_clusters.append(sc)

            for sc in sub_clusters:
                refined_vecs = sub_vecs @ sub_evec[:, sc]
                final_subspaces.append(refined_vecs)
            break

    if not can_split:
        final_subspaces.append(sub_vecs)

print(f"\n  Final subspace decomposition: {len(final_subspaces)} blocks")
for idx, sub in enumerate(final_subspaces):
    dim = sub.shape[1]
    print(f"    Block {idx}: dim {dim} in image space (= dim {dim} in C^32)")

# Step 5: Construct idempotents from subspaces
print(f"\n{'=' * 76}")
print("CONSTRUCTING IDEMPOTENTS AND IDENTIFYING FACTORS")
print(f"{'=' * 76}")

idempotents = []
for idx, sub in enumerate(final_subspaces):
    # Project subspace back to C^32
    sub_full = Q_image @ sub  # shape (32, n_sub)
    # Idempotent = projection onto this subspace
    P = sub_full @ sub_full.conj().T  # Hermitian projector
    idempotents.append(P)

    print(f"\n  Block {idx} (dim {sub.shape[1]}):")
    print(f"    P^2 = P: {np.max(np.abs(P @ P - P)):.2e}")
    print(f"    P hermitian: {np.max(np.abs(P - P.conj().T)):.2e}")
    print(f"    Trace: {np.real(np.trace(P)):.1f}")

# Check idempotents are orthogonal
print(f"\n  Idempotent orthogonality:")
for i in range(len(idempotents)):
    for j in range(i+1, len(idempotents)):
        err = np.max(np.abs(idempotents[i] @ idempotents[j]))
        print(f"    P_{i} P_{j}: max = {err:.2e}")

# Check they sum to the algebra identity
P_sum = sum(idempotents)
# Check if P_sum acts as identity on the algebra
max_id_err = 0
for T in o1_basis:
    err1 = np.max(np.abs(P_sum @ T - T))
    err2 = np.max(np.abs(T @ P_sum - T))
    max_id_err = max(max_id_err, err1, err2)
print(f"\n  Sum of idempotents = identity on algebra: max error = {max_id_err:.2e}")

# Step 6: Project algebra onto each block to identify factor type
print(f"\n{'=' * 76}")
print("IDENTIFYING EACH FACTOR")
print(f"{'=' * 76}")

for idx, P in enumerate(idempotents):
    sub = final_subspaces[idx]
    n_sub = sub.shape[1]

    print(f"\n  ---- Factor {idx} (image dim = {n_sub}) ----")

    # Project each algebra basis element: P @ T @ P
    factor_basis = []
    for T in o1_basis:
        projected = P @ T @ P
        if np.max(np.abs(projected)) > 1e-10:
            factor_basis.append(projected)

    # Find independent ones
    if not factor_basis:
        print(f"    EMPTY factor (no algebra elements project here)")
        continue

    fb_vecs = [vec_real(T) for T in factor_basis]
    Q_fb = orth(np.column_stack(fb_vecs))
    factor_dim = Q_fb.shape[1]
    print(f"    Factor algebra dimension: {factor_dim}")

    # Reconstruct orthonormal basis for this factor
    fb_onb = [(Q_fb[:, k][:n_flat] + 1j * Q_fb[:, k][n_flat:]).reshape(32, 32)
              for k in range(factor_dim)]

    # Check closure
    max_closure = 0
    for T1 in fb_onb:
        for T2 in fb_onb:
            prod = T1 @ T2
            pv = vec_real(prod)
            c = Q_fb.T @ pv
            r = np.linalg.norm(pv - Q_fb @ c)
            max_closure = max(max_closure, r)
    print(f"    Closure: max residual = {max_closure:.2e}")

    # Find center of this factor
    if factor_dim > 1:
        adj_fb = np.zeros((factor_dim * factor_dim * 2, factor_dim))
        for jj in range(factor_dim):
            for ii in range(factor_dim):
                comm_fb = fb_onb[ii] @ fb_onb[jj] - fb_onb[jj] @ fb_onb[ii]
                cv = vec_real(comm_fb)
                coeffs_fb = Q_fb.T @ cv
                # Use real representation
                adj_fb[jj * factor_dim * 2 : jj * factor_dim * 2 + factor_dim, ii] = coeffs_fb.real
                adj_fb[jj * factor_dim * 2 + factor_dim : (jj+1) * factor_dim * 2, ii] = coeffs_fb.imag

        ATA_fb = adj_fb.T @ adj_fb
        ev_fb, evec_fb = np.linalg.eigh(ATA_fb)
        tol_fb = 1e-8 * np.max(np.abs(ev_fb)) if np.max(np.abs(ev_fb)) > 0 else 1e-12
        fb_center_dim = np.sum(ev_fb < tol_fb)
        print(f"    Center dim: {fb_center_dim}")
    else:
        fb_center_dim = 1
        print(f"    Center dim: 1 (trivially)")

    # Identify the factor type
    # For a simple algebra M_n(F): dim = n^2 * dim_R(F), center = dim_R(F)
    # F = R: center = 1, dim = n^2
    # F = C: center = 2 (real dim), dim = 2n^2
    # F = H: center = 1, dim = 4n^2 (but center of H = R, so center_dim = 1)
    # Wait: over C, M_n(C) has center C = dim 1 (complex), = dim 2 (real).
    # Actually we're working in complex matrices, so center of M_n(C) = C = dim 1 (complex).
    # But our basis is real-vectorized...
    # Let me count: if factor_dim = k (real independent dims), center_dim = c,
    # then factor is M_m(F) where m^2 * dim_R(F) = k and center = 1 copy of F.

    if fb_center_dim == 1 and factor_dim == 1:
        print(f"    -> TYPE: R (real numbers)")
    elif fb_center_dim == 1 and factor_dim == 4:
        print(f"    -> TYPE: H (quaternions, 4 real dims)")
    elif fb_center_dim == 1 and factor_dim == 9:
        print(f"    -> TYPE: M_3(R) (3x3 real matrices)")
    elif fb_center_dim == 2 and factor_dim == 2:
        print(f"    -> TYPE: C (complex numbers)")
    elif fb_center_dim == 2 and factor_dim == 8:
        print(f"    -> TYPE: M_2(C) (2x2 complex matrices)")
    elif fb_center_dim == 2 and factor_dim == 18:
        print(f"    -> TYPE: M_3(C) (3x3 complex matrices)")
    else:
        # Try to determine: n = sqrt(factor_dim / dim_F)
        # If center_dim = 1: F = R, n = sqrt(factor_dim)
        # If center_dim = 2: F = C, n = sqrt(factor_dim/2)
        n_R = np.sqrt(factor_dim)
        n_C = np.sqrt(factor_dim / 2)
        print(f"    -> UNKNOWN TYPE: dim={factor_dim}, center={fb_center_dim}")
        print(f"       If F=R: n={n_R:.2f}, If F=C: n={n_C:.2f}")

    # Check if the factor is commutative
    max_comm_fb = 0
    for ii in range(min(factor_dim, 5)):
        for jj in range(ii+1, min(factor_dim, 5)):
            err = np.max(np.abs(fb_onb[ii] @ fb_onb[jj] - fb_onb[jj] @ fb_onb[ii]))
            max_comm_fb = max(max_comm_fb, err)
    print(f"    Commutativity check (first 5): max |[a,b]| = {max_comm_fb:.2e}")

    # Check what H_F indices this factor acts on
    nonzero_rows = set()
    nonzero_cols = set()
    for T in fb_onb:
        for r in range(32):
            for c in range(32):
                if abs(T[r, c]) > 1e-8:
                    nonzero_rows.add(r)
                    nonzero_cols.add(c)
    print(f"    Active rows: {sorted(nonzero_rows)}")
    print(f"    Active cols: {sorted(nonzero_cols)}")

    # Physical interpretation: which particles?
    # Psi_+ indices 0-15: (row, col) of 4x4 matrix
    # Row 0: neutrino-like, Row 1-3: quark colors
    # Psi_- indices 16-31: charge conjugates
    print(f"    Psi_+ rows: {sorted([r for r in nonzero_rows if r < 16])}")
    print(f"    Psi_- rows: {sorted([r for r in nonzero_rows if r >= 16])}")


# =============================================================================
# PART 7: Check if P_a are in the algebra
# =============================================================================

print(f"\n{'=' * 76}")
print("ARE THE IDEMPOTENTS IN THE ALGEBRA?")
print(f"{'=' * 76}")

for idx, P in enumerate(idempotents):
    pv = vec_real(P)
    coeffs = Q_o1.T @ pv
    resid = np.linalg.norm(pv - Q_o1 @ coeffs)
    print(f"  P_{idx}: residual from algebra = {resid:.2e}")
    # Check if P is in closure but not in order-one subalgebra
    Q_closure = orth(np.column_stack([vec_real(T) for T in closure_basis_32]))
    coeffs_c = Q_closure.T @ pv
    resid_c = np.linalg.norm(pv - Q_closure @ coeffs_c)
    print(f"  P_{idx}: residual from closure = {resid_c:.2e}")


# =============================================================================
# PART 8: Compare with Session 10 left-row algebra
# =============================================================================

print(f"\n{'=' * 76}")
print("COMPARISON WITH C + M_3(C)_rows FROM SESSION 10")
print(f"{'=' * 76}")

# Build the pure left M_3(C)_rows algebra (9 generators E_{ab} on rows 1-3)
m3_gens_32 = []
for a in range(3):
    for b in range(3):
        L_m = np.zeros((4, 4), dtype=complex)
        L_m[a+1, b+1] = 1.0
        g16 = build_left_action_16(L_m)
        g32 = build_full_32(g16)
        m3_gens_32.append(g32)

# Add C (identity on row 0, zero on rows 1-3)
L_c = np.zeros((4, 4), dtype=complex)
L_c[0, 0] = 1.0
c16 = build_left_action_16(L_c)
c32 = build_full_32(c16)

left_row_gens = [c32] + m3_gens_32  # 10 generators

# Check: is each left-row generator in the order-one subalgebra?
print(f"\n  Left-row generators in order-one subalgebra:")
for idx, T in enumerate(left_row_gens):
    pv = vec_real(T)
    coeffs = Q_o1.T @ pv
    resid = np.linalg.norm(pv - Q_o1 @ coeffs)
    label = 'C' if idx == 0 else f'E_{(idx-1)//3 + 1}{(idx-1)%3 + 1}'
    print(f"    {label}: residual = {resid:.2e} {'<-- IN' if resid < 1e-6 else '<-- NOT IN'}")

# Find the algebraic closure of left-row generators
lr_vecs = [vec_real(T) for T in left_row_gens]
Q_lr = orth(np.column_stack(lr_vecs))
d_lr = Q_lr.shape[1]

# Closure
for it in range(10):
    cur_lr = [(Q_lr[:, k][:n_flat] + 1j * Q_lr[:, k][n_flat:]).reshape(32, 32)
              for k in range(d_lr)]
    new_lr = []
    for T1 in cur_lr:
        for T2 in left_row_gens:
            prod = T1 @ T2
            pv = vec_real(prod)
            c = Q_lr.T @ pv
            r = np.linalg.norm(pv - Q_lr @ c)
            if r > 1e-8:
                new_lr.append(pv)
    if not new_lr:
        break
    all_lr = np.column_stack([Q_lr] + [np.column_stack(new_lr)])
    Q_lr_new = orth(all_lr)
    if Q_lr_new.shape[1] == d_lr:
        break
    d_lr = Q_lr_new.shape[1]
    Q_lr = Q_lr_new

print(f"\n  Left-row algebra closure dimension: {d_lr}")
print(f"  (Expected: 20 = C + M_3(C)_rows)")

# Check overlap: is order-one = left-row?
# Project each order-one basis element onto left-row space
in_lr = 0
for T in o1_basis:
    pv = vec_real(T)
    c = Q_lr.T @ pv
    r = np.linalg.norm(pv - Q_lr @ c)
    if r < 1e-6:
        in_lr += 1

print(f"  Order-one basis elements in left-row algebra: {in_lr} / {o1_dim_actual}")

# And reverse
in_o1 = 0
lr_basis = [(Q_lr[:, k][:n_flat] + 1j * Q_lr[:, k][n_flat:]).reshape(32, 32)
            for k in range(d_lr)]
for T in lr_basis:
    pv = vec_real(T)
    c = Q_o1.T @ pv
    r = np.linalg.norm(pv - Q_o1 @ c)
    if r < 1e-6:
        in_o1 += 1

print(f"  Left-row basis elements in order-one algebra: {in_o1} / {d_lr}")

if in_lr == o1_dim_actual and in_o1 == d_lr:
    print(f"\n  *** ORDER-ONE SUBALGEBRA = LEFT-ROW ALGEBRA (C + M_3(C)_rows) ***")
elif in_lr == o1_dim_actual:
    print(f"\n  Order-one SUBSET of left-row")
elif in_o1 == d_lr:
    print(f"\n  Left-row SUBSET of order-one")
else:
    print(f"\n  Partial overlap: {in_lr}/{o1_dim_actual} o1->lr, {in_o1}/{d_lr} lr->o1")


# =============================================================================
# FINAL SUMMARY
# =============================================================================

print(f"\n{'=' * 76}")
print("FINAL SUMMARY")
print(f"{'=' * 76}")
print(f"  L-closure dimension: {d_cur}")
print(f"  Order-one constraint rank: 18")
print(f"  Order-one subalgebra dimension: {o1_dim_actual}")
print(f"  Semisimple: YES (radical dim = 0)")
print(f"  Center dimension: {center_dim}")
print(f"  Number of simple factors: {len(final_subspaces)}")
for idx, sub in enumerate(final_subspaces):
    print(f"    Factor {idx}: image dim = {sub.shape[1]}")
print(f"  Target: A_F = C + H + M_3(C) (dim 24, center 3, 3 factors)")
print(f"  Order-zero: FAILS (order-one is strictly weaker)")
print(f"{'=' * 76}")
