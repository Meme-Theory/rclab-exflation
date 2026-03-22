"""
DEBUG SCRIPT v2: Fix the center computation.

Core issue: The J-compatible commutant is a REAL algebra (real dim 80).
When we orthonormalize the basis with complex inner product and compute
structure constants, we get complex structure constants for what should
be a real algebra. The center computation then fails because we ask
for real coefficients satisfying complex equations.

Fix: Use a REAL orthonormal basis for the algebra.
The J-compatible basis elements are complex 32x32 matrices T satisfying
T*Xi = Xi*conj(T). We can decompose each T into T_re and T_im parts
that independently satisfy this condition, then orthonormalize in the
REAL vector space R^{2*32*32}.
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

# ===================================================================
# Build G5, Xi, gauge generators (same as before)
# ===================================================================

def get_column_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return flat_idx
    elif 4 <= flat_idx <= 6: return 0
    else:
        d_flat = flat_idx - 7
        return d_flat % 3 + 1

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

basis_u2 = u2_basis_in_su3()

def rho_plus(v):
    return LR_action_matrix(v)

def rho_minus(v):
    return G5 @ np.conj(rho_plus(v)) @ G5

def rho_full(v):
    R = np.zeros((32, 32), dtype=complex)
    R[:16, :16] = rho_plus(v)
    R[16:, 16:] = rho_minus(v)
    return R

# ===================================================================
# Compute gauge commutant
# ===================================================================

n = 32
rho_gens = [rho_full(v) for v in basis_u2]

constraint_blocks = []
for rho_v in rho_gens:
    block = np.zeros((n*n, n*n), dtype=complex)
    for i in range(n):
        for j in range(n):
            row = i * n + j
            for k in range(n):
                block[row, i*n + k] += rho_v[k, j]
                block[row, k*n + j] -= rho_v[i, k]
    constraint_blocks.append(block)

A = np.vstack(constraint_blocks)
ns = null_space(A, rcond=1e-10)
d_gauge = ns.shape[1]
print(f"Gauge commutant complex dim: {d_gauge}")

comm_basis = [ns[:, k].reshape(n, n) for k in range(d_gauge)]

# ===================================================================
# J-compatibility: CORRECT formulation as real linear problem
# ===================================================================

# The J-compatible commutant consists of complex matrices T satisfying:
# 1. [T, rho(v)] = 0 for all v  (gauge commutant)
# 2. T * Xi = Xi * conj(T)       (J-compatibility)
#
# Condition 2 in block form (T = (A,B;C,D), Xi = (0,-G5;-G5,0)):
#   D = G5 * conj(A) * G5
#   C = G5 * conj(B) * G5
#
# So T is determined by its upper-left block A and upper-right block B.
#
# From condition 1: T must commute with rho_full(v) = diag(rho_+, rho_-).
# This means:
#   A * rho_+ = rho_+ * A  (A commutes with Psi_+ gauge action)
#   B * rho_- = rho_+ * B  (B intertwines Psi_- to Psi_+)
#   C * rho_+ = rho_- * C  (C intertwines Psi_+ to Psi_-)
#   D * rho_- = rho_- * D  (D commutes with Psi_- gauge action)
#
# The J condition D = G5*conj(A)*G5 is automatically consistent with
# gauge if A commutes with rho_+ (since rho_- = G5*conj(rho_+)*G5).
#
# So the J-compatible commutant elements are determined by:
#   (A, B) where A in End_{U(2)}(Psi_+), B in Hom_{U(2)}(Psi_-, Psi_+)
#   with D = G5*conj(A)*G5, C = G5*conj(B)*G5
#
# Phase 1 told us dim(End_{U(2)}(Psi_+)) = 20 (complex).
# The intertwiner space Hom_{U(2)}(Psi_-, Psi_+) depends on
# whether Psi_+ and Psi_- share irreducible subrepresentations.
#
# Since rho_- = G5 * conj(rho_+) * G5, it's the conjugate representation.
# An intertwiner B: Psi_- -> Psi_+ satisfies B * rho_- = rho_+ * B,
# i.e., B * G5 * conj(rho_+) * G5 = rho_+ * B.
#
# This is equivalent to (B*G5) * conj(rho_+) = rho_+ * (B*G5) / G5
# Hmm, let's just compute it numerically.

print("\n--- COMPUTING INTERTWINER SPACES SEPARATELY ---")

# A-space: End_{U(2)}(Psi_+) -- the Phase 1 commutant
rho_p_gens = [rho_plus(v) for v in basis_u2]
c16 = []
for rv in rho_p_gens:
    block = np.zeros((256, 256), dtype=complex)
    for i in range(16):
        for j in range(16):
            row = i*16 + j
            for k in range(16):
                block[row, i*16+k] += rv[k, j]
                block[row, k*16+j] -= rv[i, k]
    c16.append(block)

A16 = np.vstack(c16)
ns_A = null_space(A16, rcond=1e-10)
d_A = ns_A.shape[1]
print(f"A-space dim (End_U(2)(Psi_+)): {d_A}")

A_basis = [ns_A[:, k].reshape(16, 16) for k in range(d_A)]

# B-space: Hom_{U(2)}(Psi_-, Psi_+)
# B * rho_-(v) = rho_+(v) * B for all v
# B * G5 * conj(rho_+(v)) * G5 = rho_+(v) * B
rho_m_gens = [rho_minus(v) for v in basis_u2]

c16_B = []
for i_v in range(len(basis_u2)):
    rp = rho_p_gens[i_v]
    rm = rho_m_gens[i_v]
    block = np.zeros((256, 256), dtype=complex)
    for i in range(16):
        for j in range(16):
            row = i*16 + j
            for k in range(16):
                block[row, i*16+k] += rm[k, j]  # B*rho_- part: column action
                block[row, k*16+j] -= rp[i, k]  # rho_+*B part: row action
    c16_B.append(block)

A16_B = np.vstack(c16_B)
ns_B = null_space(A16_B, rcond=1e-10)
d_B = ns_B.shape[1]
print(f"B-space dim (Hom_U(2)(Psi_-, Psi_+)): {d_B}")

B_basis = [ns_B[:, k].reshape(16, 16) for k in range(d_B)]

print(f"\nTotal complex dimension of (A,B): {d_A + d_B}")
print(f"Total real dimension with J constraint: {2*(d_A + d_B)}")
print(f"(Because each complex A determines a real D = G5*conj(A)*G5,")
print(f" the real dimension is 2*(dim_A + dim_B) since A,B are complex.)")
print(f"BUT WAIT: the J condition imposes A = G5*conj(D)*G5 which means")
print(f"A is NOT free -- it determines D. The real degrees of freedom in A")
print(f"are 2*d_A (real + imaginary parts). So total = 2*d_A + 2*d_B = {2*(d_A+d_B)}.")

# ===================================================================
# Build explicit J-compatible basis (REAL basis)
# ===================================================================

print("\n--- BUILDING REAL J-COMPATIBLE BASIS ---")

# For each A-space basis element A_k:
# T_k^{re} = (A_k, 0; 0, G5*conj(A_k)*G5) / sqrt(2) (real coeff = 1)
# T_k^{im} = (i*A_k, 0; 0, G5*conj(i*A_k)*G5) = (i*A_k, 0; 0, -i*G5*conj(A_k)*G5) (imag coeff)
#
# Wait, let me be more careful.
# A general J-compatible element from the A-sector:
#   T = (z*A_k, 0; 0, G5*conj(z*A_k)*G5) = (z*A_k, 0; 0, conj(z)*G5*conj(A_k)*G5)
#   for any complex z = alpha + i*beta.
#
# Real basis: alpha=1, beta=0 gives T^(re) = (A_k, 0; 0, G5*conj(A_k)*G5)
#             alpha=0, beta=1 gives T^(im) = (i*A_k, 0; 0, -i*G5*conj(A_k)*G5)
#
# Similarly for B-sector:
#   T = (0, z*B_k; G5*conj(z*B_k)*G5, 0) = (0, z*B_k; conj(z)*G5*conj(B_k)*G5, 0)
# Real basis:
#   T^(re) = (0, B_k; G5*conj(B_k)*G5, 0)
#   T^(im) = (0, i*B_k; -i*G5*conj(B_k)*G5, 0)

real_basis = []

# A-sector
for k in range(d_A):
    Ak = A_basis[k]
    Dk_conj = G5 @ np.conj(Ak) @ G5

    # Real part
    T_re = np.zeros((32, 32), dtype=complex)
    T_re[:16, :16] = Ak
    T_re[16:, 16:] = Dk_conj
    real_basis.append(T_re)

    # Imaginary part
    T_im = np.zeros((32, 32), dtype=complex)
    T_im[:16, :16] = 1j * Ak
    T_im[16:, 16:] = -1j * Dk_conj
    real_basis.append(T_im)

# B-sector
for k in range(d_B):
    Bk = B_basis[k]
    Ck_conj = G5 @ np.conj(Bk) @ G5

    # Real part
    T_re = np.zeros((32, 32), dtype=complex)
    T_re[:16, 16:] = Bk
    T_re[16:, :16] = Ck_conj
    real_basis.append(T_re)

    # Imaginary part
    T_im = np.zeros((32, 32), dtype=complex)
    T_im[:16, 16:] = 1j * Bk
    T_im[16:, :16] = -1j * Ck_conj
    real_basis.append(T_im)

print(f"Real basis elements: {len(real_basis)}")
print(f"Expected: 2*{d_A} + 2*{d_B} = {2*(d_A+d_B)}")

# Verify J-compatibility and gauge commutation
max_J_err = 0
max_g_err = 0
for T in real_basis:
    err_J = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
    max_J_err = max(max_J_err, err_J)
    for rv in rho_gens:
        err_g = np.max(np.abs(T @ rv - rv @ T))
        max_g_err = max(max_g_err, err_g)

print(f"Max J-compat error: {max_J_err:.2e}")
print(f"Max gauge comm error: {max_g_err:.2e}")

# Orthonormalize using REAL inner product
# The real inner product: <T1, T2> = Re(Tr(T1^dag T2)) = sum of Re(conj(T1_ij)*T2_ij)
# We can vectorize as: [Re(T); Im(T)] and use standard dot product

real_vecs = []
for T in real_basis:
    v = np.concatenate([T.flatten().real, T.flatten().imag])
    real_vecs.append(v)

V = np.column_stack(real_vecs)
Q_real = orth(V)
d_orth = Q_real.shape[1]
print(f"\nReal orthonormal basis dim: {d_orth}")

# Reconstruct orthonormal basis as complex matrices
n_flat = n * n  # 1024
orth_basis = []
for k in range(d_orth):
    v = Q_real[:, k]
    T = (v[:n_flat] + 1j * v[n_flat:]).reshape(n, n)
    orth_basis.append(T)

# Check identity
id_real_vec = np.concatenate([np.eye(n).flatten().real, np.eye(n).flatten().imag])
id_proj = Q_real @ (Q_real.T @ id_real_vec)
id_resid = np.linalg.norm(id_real_vec - id_proj)
print(f"Identity in algebra? Residual: {id_resid:.2e}")

# ===================================================================
# Compute structure constants IN THE REAL BASIS
# ===================================================================

print("\n--- STRUCTURE CONSTANTS (REAL BASIS) ---")

# Product of two basis elements: e_i * e_j
# Project back onto the basis using REAL inner product
struct_const = np.zeros((d_orth, d_orth, d_orth))
max_resid = 0

for i in range(d_orth):
    for j in range(d_orth):
        prod = orth_basis[i] @ orth_basis[j]
        prod_real_vec = np.concatenate([prod.flatten().real, prod.flatten().imag])
        coeffs = Q_real.T @ prod_real_vec
        struct_const[i, j, :] = coeffs
        resid = np.linalg.norm(prod_real_vec - Q_real @ coeffs)
        max_resid = max(max_resid, resid)

print(f"Closure check (max residual): {max_resid:.2e}")
if max_resid > 1e-6:
    print("WARNING: Algebra does NOT close under multiplication!")
    print("This means the J-compatible commutant is NOT a subalgebra.")
    print("Possible cause: the B-sector elements don't form a closed algebra")
    print("with the A-sector elements.")

# Center: find x such that [sum_i x_i e_i, e_j] = 0 for all j
# With REAL structure constants and REAL coefficients x_i
comm_sc = struct_const - struct_const.transpose(1, 0, 2)

center_rows = []
for j in range(d_orth):
    for k in range(d_orth):
        center_rows.append(comm_sc[:, j, k])

center_mat = np.array(center_rows)
center_rank = np.linalg.matrix_rank(center_mat, tol=1e-8)
center_ns = null_space(center_mat, rcond=1e-8)
center_dim = center_ns.shape[1]

print(f"\nCenter constraint: {center_mat.shape}, rank: {center_rank}")
print(f"Center dimension: {center_dim}")
print(f"(For A_F = C + H + M_3(C) over R: center should be dim 5 = 2+1+2)")
print(f"(Wait: center(C)=C(dim 2 real), center(H)=R(dim 1), center(M_3(C))=C(dim 2))")
print(f"(Total center real dim for A_F: 2 + 1 + 2 = 5)")

if center_dim > 0:
    print(f"\n  CENTER ELEMENTS:")
    for idx in range(center_dim):
        coeffs = center_ns[:, idx]
        T_center = sum(coeffs[i] * orth_basis[i] for i in range(d_orth))
        # Verify it commutes with everything
        max_comm = 0
        for T in orth_basis:
            comm = T_center @ T - T @ T_center
            max_comm = max(max_comm, np.linalg.norm(comm))
        print(f"  Center element {idx}: max commutator norm = {max_comm:.2e}")

        # Check if it's proportional to identity
        ratio = T_center / np.eye(32) if np.max(np.abs(np.eye(32))) > 0 else None
        id_test = T_center - T_center[0,0] * np.eye(32)
        print(f"    Proportional to identity? Max deviation: {np.max(np.abs(id_test)):.2e}")

    # ===================================================================
    # Wedderburn decomposition via generic central element
    # ===================================================================

    print("\n--- WEDDERBURN DECOMPOSITION ---")
    np.random.seed(42)
    rand_c = np.random.randn(center_dim)
    generic_center = sum(c * sum(center_ns[i, idx] * orth_basis[i]
                                 for i in range(d_orth))
                        for idx, c in enumerate(rand_c))

    evals, evecs = np.linalg.eig(generic_center)
    evals_r = np.round(evals, 4)
    unique = np.unique(evals_r)

    print(f"Generic center element: {len(unique)} distinct eigenvalues")
    for ev in unique:
        mult = np.sum(np.abs(evals_r - ev) < 5e-4)
        print(f"  {ev}: mult {mult}")

    # For each eigenvalue, project algebra and determine type
    for ev in unique:
        mask = np.abs(evals_r - ev) < 5e-4
        V = evecs[:, mask]
        dim_V = V.shape[1]

        # Project all algebra elements
        proj_vecs = []
        for T in orth_basis:
            T_proj = V.conj().T @ T @ V
            pv = np.concatenate([T_proj.flatten().real, T_proj.flatten().imag])
            proj_vecs.append(pv)

        if len(proj_vecs) > 0:
            P = np.column_stack(proj_vecs)
            factor_rank = np.linalg.matrix_rank(P, tol=1e-6)
        else:
            factor_rank = 0

        print(f"\n  Factor at ev={ev:.4f}:")
        print(f"    Eigenspace dim: {dim_V}")
        print(f"    Algebra rank (real): {factor_rank}")

        # Identify type
        # M_n(R): real dim = n^2, acts on R^n (= C^n via embedding, so dim_V = n or 2n)
        # M_n(C): real dim = 2n^2, acts on C^n, dim_V = n
        # M_n(H): real dim = 4n^2, acts on H^n, dim_V = 2n
        for n_try in range(1, 10):
            if factor_rank == n_try**2:
                print(f"    Candidate: M_{n_try}(R) (real dim {n_try**2}, H_dim should be {n_try} or {2*n_try})")
            if factor_rank == 2 * n_try**2:
                print(f"    Candidate: M_{n_try}(C) (real dim {2*n_try**2}, H_dim should be {n_try})")
            if factor_rank == 4 * n_try**2:
                print(f"    Candidate: M_{n_try}(H) (real dim {4*n_try**2}, H_dim should be {2*n_try})")

    # Total
    print(f"\n  Total eigenspace dim: {sum(np.sum(np.abs(evals_r - ev) < 5e-4) for ev in unique)} (should be 32)")

elif center_dim == 0:
    print(f"\nCenter dim = 0 again!")
    print("Investigating further...")

    # Check if the algebra actually closes
    print(f"\nMax closure residual: {max_resid:.2e}")

    # If it doesn't close, the issue is that the B-sector elements
    # (cross-sector intertwiners) don't form a closed algebra with A-sector.
    # Let's check the A-sector alone.

    print("\n--- A-SECTOR SUBALGEBRA ---")
    # Just the first 2*d_A elements (A-sector real basis)
    A_basis_32 = real_basis[:2*d_A]

    # Check closure of A-sector
    A_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in A_basis_32]
    V_A = np.column_stack(A_vecs)
    Q_A = orth(V_A)
    d_A_orth = Q_A.shape[1]
    print(f"A-sector real dim: {d_A_orth}")

    A_orth = [( Q_A[:, k][:n_flat] + 1j * Q_A[:, k][n_flat:]).reshape(n, n) for k in range(d_A_orth)]

    sc_A = np.zeros((d_A_orth, d_A_orth, d_A_orth))
    max_resid_A = 0
    for i in range(d_A_orth):
        for j in range(d_A_orth):
            prod = A_orth[i] @ A_orth[j]
            pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
            coeffs = Q_A.T @ pv
            sc_A[i, j, :] = coeffs
            resid = np.linalg.norm(pv - Q_A @ coeffs)
            max_resid_A = max(max_resid_A, resid)

    print(f"A-sector closure: {max_resid_A:.2e}")

    if max_resid_A < 1e-6:
        print("A-sector IS a subalgebra!")
        # Compute its center
        comm_A = sc_A - sc_A.transpose(1, 0, 2)
        cr_A = []
        for j in range(d_A_orth):
            for k in range(d_A_orth):
                cr_A.append(comm_A[:, j, k])
        cm_A = np.array(cr_A)
        cns_A = null_space(cm_A, rcond=1e-8)
        print(f"A-sector center dim: {cns_A.shape[1]}")

        # Decompose A-sector
        if cns_A.shape[1] > 0:
            np.random.seed(42)
            rc = np.random.randn(cns_A.shape[1])
            gc_A = sum(c * sum(cns_A[i, idx] * A_orth[i]
                              for i in range(d_A_orth))
                      for idx, c in enumerate(rc))

            evals_A, evecs_A = np.linalg.eig(gc_A)
            er_A = np.round(evals_A, 4)
            ue_A = np.unique(er_A)
            print(f"  Generic center element: {len(ue_A)} distinct eigenvalues on C^32")
            for ev in ue_A:
                mult = np.sum(np.abs(er_A - ev) < 5e-4)
                print(f"    {ev}: mult {mult}")

    # Check B-sector closure
    print("\n--- B-SECTOR PRODUCTS ---")
    # B * B^dag type products? B is Psi_- -> Psi_+, so B1 * B2 doesn't make sense
    # dimensionally (B1: 16x16 from - to +, B2: 16x16 from - to +).
    # But in the 32x32 space:
    # T_B1 = (0, B1; C1, 0), T_B2 = (0, B2; C2, 0)
    # T_B1 * T_B2 = (B1*C2, 0; 0, C1*B2) -- this is in the A-sector!
    # So B*B products MAP INTO the A-sector.

    # This means: the FULL algebra generated by A-sector and B-sector
    # has A-sector as a subalgebra, and B-sector elements generate
    # cross-terms. Let's check if B*C products are in the A-sector.

    if d_B > 0:
        print(f"Checking B*C products (should be in A-sector)...")
        for ib in range(min(d_B, 3)):
            for jb in range(min(d_B, 3)):
                T_B1 = real_basis[2*d_A + 2*ib]  # real part of B_ib
                T_B2 = real_basis[2*d_A + 2*jb]  # real part of B_jb
                prod = T_B1 @ T_B2
                # This should be block-diagonal
                off_diag = np.max(np.abs(prod[:16, 16:])) + np.max(np.abs(prod[16:, :16]))
                on_diag = np.max(np.abs(prod[:16, :16])) + np.max(np.abs(prod[16:, 16:]))
                pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
                proj = Q_A @ (Q_A.T @ pv)
                resid = np.linalg.norm(pv - proj)
                print(f"  B_{ib} * B_{jb}: off-diag={off_diag:.2e}, on-diag={on_diag:.4f}, A-sector resid={resid:.2e}")

    print("\n--- FULL ALGEBRA ANALYSIS ---")
    # Since the full algebra might not close (B*A products might not project back),
    # let's check closure more carefully by generating ALL products and checking
    # if they stay within the span.

    # Actually, the closure residual max_resid was computed above.
    # If it's small, the algebra closes. If not, we need to extend.
    print(f"Full algebra closure residual: {max_resid:.2e}")

    if max_resid > 1e-6:
        # The algebra doesn't close! We need to generate more elements.
        print("Algebra does NOT close. Generating products...")

        # Generate all products and extend the basis
        new_vecs = list(Q_real.T)  # start with existing basis
        for i in range(d_orth):
            for j in range(d_orth):
                prod = orth_basis[i] @ orth_basis[j]
                pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
                new_vecs.append(pv)

        new_V = np.column_stack(new_vecs)
        Q_ext = orth(new_V)
        d_ext = Q_ext.shape[1]
        print(f"Extended basis dim: {d_ext} (was {d_orth})")

        if d_ext > d_orth:
            # There were products not in the original span!
            print(f"Found {d_ext - d_orth} new linearly independent products.")
            # Reconstruct extended basis
            ext_basis = [(Q_ext[:, k][:n_flat] + 1j * Q_ext[:, k][n_flat:]).reshape(n, n) for k in range(d_ext)]

            # Check if THESE elements still satisfy J-compat and gauge comm
            max_J2 = 0
            max_g2 = 0
            for T in ext_basis:
                err_J = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
                max_J2 = max(max_J2, err_J)
                for rv in rho_gens:
                    err_g = np.max(np.abs(T @ rv - rv @ T))
                    max_g2 = max(max_g2, err_g)
            print(f"Extended basis: max J-error = {max_J2:.2e}, max gauge-error = {max_g2:.2e}")

print("\nDone.")
