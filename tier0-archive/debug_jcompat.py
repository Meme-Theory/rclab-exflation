"""
DEBUG SCRIPT: Investigate center_dim = 0 issue in Phase 2 computation.

Focus: Is the J-constraint correct? Is the center computation correct?
Strategy: Build from scratch with maximum clarity, cross-check every step.
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    gell_mann_matrices, su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix, LR_action_matrix,
    flatten_psi, unflatten_psi,
)

np.set_printoptions(precision=6, linewidth=120, suppress=True)

# ===================================================================
# STEP 1: Build G5 and Xi as in the main script
# ===================================================================

def get_column_index(flat_idx):
    """Column index j of the 4x4 internal matrix for flattened index."""
    if flat_idx == 0:
        return 0
    elif 1 <= flat_idx <= 3:
        return flat_idx
    elif 4 <= flat_idx <= 6:
        return 0
    else:
        d_flat = flat_idx - 7
        d_j = d_flat % 3
        return d_j + 1

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])

# G5[k,k] = -gamma_5[j(k), j(k)]
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

# Xi = (0, -G5; -G5, 0) -- 32x32
Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

print("G5 diagonal:", G5_signs.astype(int))
print("Xi^2 = I?", np.allclose(Xi @ Xi, np.eye(32)))
print("Xi hermitian?", np.allclose(Xi, Xi.T))
print("Xi real?", np.allclose(Xi.imag, 0) if isinstance(Xi[0,0], complex) else "YES (dtype float)")

# ===================================================================
# STEP 2: Build the 32-dim gauge representation
# ===================================================================

basis_u2 = u2_basis_in_su3()

def rho_plus(v):
    return LR_action_matrix(v)

def rho_minus(v):
    rp = rho_plus(v)
    return G5 @ np.conj(rp) @ G5

def rho_full(v):
    R = np.zeros((32, 32), dtype=complex)
    R[:16, :16] = rho_plus(v)
    R[16:, 16:] = rho_minus(v)
    return R

# J-compatibility check
print("\nJ-compatibility: Xi * conj(rho_full(v)) * Xi = rho_full(v)")
for i, v in enumerate(basis_u2):
    rf = rho_full(v)
    check = Xi @ np.conj(rf) @ Xi
    err = np.max(np.abs(check - rf))
    print(f"  basis {i}: err = {err:.2e}")

# ===================================================================
# STEP 3: Compute gauge commutant on C^32
# ===================================================================

print("\n--- GAUGE COMMUTANT ---")
n = 32
rho_gens = [rho_full(v) for v in basis_u2]

# Build constraint: [T, rho_v] = 0 for all v
# T*rho_v - rho_v*T = 0
# Using direct construction (avoid kron)
constraint_blocks = []
for rho_v in rho_gens:
    block = np.zeros((n*n, n*n), dtype=complex)
    for i in range(n):
        for j in range(n):
            row = i * n + j
            for k in range(n):
                block[row, i*n + k] += rho_v[k, j]    # (T*rho_v)_{ij} contribution
                block[row, k*n + j] -= rho_v[i, k]    # (rho_v*T)_{ij} contribution
    constraint_blocks.append(block)

A = np.vstack(constraint_blocks)
print(f"Constraint matrix: {A.shape}")

ns = null_space(A, rcond=1e-10)
d_gauge = ns.shape[1]
print(f"Gauge commutant complex dim: {d_gauge}")

comm_basis = [ns[:, k].reshape(n, n) for k in range(d_gauge)]

# Verify commutation
max_err = max(np.max(np.abs(T @ rv - rv @ T)) for T in comm_basis for rv in rho_gens)
print(f"Max commutation error: {max_err:.2e}")

# ===================================================================
# STEP 4: Check block structure of commutant
# ===================================================================

print("\n--- BLOCK STRUCTURE OF COMMUTANT ---")
# The 32-dim space splits as C^16(+) + C^16(-).
# The gauge commutant should have a block structure:
#   (A, B; C, D) where A: 16->16 on Psi_+, D: 16->16 on Psi_-,
#   B: Psi_- -> Psi_+, C: Psi_+ -> Psi_-

# Check: how many basis elements are purely in the ++ block, --, +-, -+ ?
for T in comm_basis[:5]:  # just first 5
    pp = np.max(np.abs(T[:16, :16]))
    pm = np.max(np.abs(T[:16, 16:]))
    mp = np.max(np.abs(T[16:, :16]))
    mm = np.max(np.abs(T[16:, 16:]))
    print(f"  Block norms: (++) {pp:.3f}  (+-) {pm:.3f}  (-+) {mp:.3f}  (--) {mm:.3f}")

# Count purely diagonal vs off-diagonal
n_diag = 0
n_offdiag = 0
n_mixed = 0
for T in comm_basis:
    pp_mm = np.max(np.abs(T[:16, :16])) + np.max(np.abs(T[16:, 16:]))
    pm_mp = np.max(np.abs(T[:16, 16:])) + np.max(np.abs(T[16:, :16]))
    if pp_mm > 1e-8 and pm_mp < 1e-8:
        n_diag += 1
    elif pm_mp > 1e-8 and pp_mm < 1e-8:
        n_offdiag += 1
    else:
        n_mixed += 1

print(f"\nPurely diagonal (++,--): {n_diag}")
print(f"Purely off-diagonal (+-,-+): {n_offdiag}")
print(f"Mixed: {n_mixed}")

# ===================================================================
# STEP 5: J-compatibility constraint
# ===================================================================

print("\n--- J-COMPATIBILITY ---")
# Condition: T * Xi = Xi * conj(T)
#
# T = sum_k z_k T_k where z_k = alpha_k + i*beta_k
# sum_k z_k (T_k * Xi) = sum_k conj(z_k) * Xi * conj(T_k)
# = sum_k (alpha_k - i*beta_k) * Xi * conj(T_k)
#
# Rearranging:
# sum_k alpha_k * (T_k*Xi - Xi*conj(T_k)) + i * sum_k beta_k * (T_k*Xi + Xi*conj(T_k)) = 0
#
# Let A_k = T_k*Xi - Xi*conj(T_k)  (should be zero if T_k itself is J-compatible)
#     B_k = T_k*Xi + Xi*conj(T_k)
#
# Matrix equation: sum_k alpha_k * A_k + i * sum_k beta_k * B_k = 0
# Vectorizing (1024 complex entries = 2048 real equations):
# For each entry m:
#   sum_k alpha_k * Re(A_k[m]) - sum_k beta_k * Im(B_k[m]) = 0    (real part)
#   sum_k alpha_k * Im(A_k[m]) + sum_k beta_k * Re(B_k[m]) = 0    (imag part)

d = d_gauge
A_mats = []
B_mats = []
for k in range(d):
    Tk = comm_basis[k]
    Ak = Tk @ Xi - Xi @ np.conj(Tk)
    Bk = Tk @ Xi + Xi @ np.conj(Tk)
    A_mats.append(Ak.flatten())
    B_mats.append(Bk.flatten())

# Build the 2*n*n x 2*d constraint matrix
n_entries = n * n  # 1024
C_mat = np.zeros((2 * n_entries, 2 * d))

for m in range(n_entries):
    for k in range(d):
        a_val = A_mats[k][m]
        b_val = B_mats[k][m]

        # Real part equation (row 2*m)
        C_mat[2*m, k] = a_val.real           # alpha_k coeff
        C_mat[2*m, d + k] = -b_val.imag      # beta_k coeff

        # Imag part equation (row 2*m + 1)
        C_mat[2*m + 1, k] = a_val.imag       # alpha_k coeff
        C_mat[2*m + 1, d + k] = b_val.real   # beta_k coeff

print(f"J-constraint matrix: {C_mat.shape}")
rank_C = np.linalg.matrix_rank(C_mat, tol=1e-8)
print(f"J-constraint rank: {rank_C}")
print(f"J-constraint null dim: {2*d - rank_C}")

ns_J = null_space(C_mat, rcond=1e-10)
J_null_dim = ns_J.shape[1]
print(f"J-compatible commutant real dim (from null_space): {J_null_dim}")

# Reconstruct J-compatible basis
Jbasis = []
for idx in range(J_null_dim):
    coeffs = ns_J[:, idx]
    alphas = coeffs[:d]
    betas = coeffs[d:]
    T = sum((alphas[k] + 1j*betas[k]) * comm_basis[k] for k in range(d))
    Jbasis.append(T)

# Verify J-compatibility
max_J_err = 0
for T in Jbasis:
    err = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
    max_J_err = max(max_J_err, err)
print(f"Max J-compat verification error: {max_J_err:.2e}")

# Verify gauge commutation still holds
max_g_err = 0
for T in Jbasis:
    for rv in rho_gens:
        err = np.max(np.abs(T @ rv - rv @ T))
        max_g_err = max(max_g_err, err)
print(f"Max gauge comm verification error: {max_g_err:.2e}")

# ===================================================================
# STEP 6: ALTERNATIVE CENTER COMPUTATION
# ===================================================================

print("\n--- CENTER ANALYSIS ---")

# Orthonormalize
if J_null_dim > 0:
    basis_mat = np.column_stack([T.flatten() for T in Jbasis])
    Q = orth(basis_mat)
    d_orth = Q.shape[1]
    print(f"Orthonormalized basis dim: {d_orth}")

    orth_basis = [Q[:, k].reshape(n, n) for k in range(d_orth)]

    # Check identity
    id_vec = np.eye(n, dtype=complex).flatten()
    id_proj = Q @ (Q.conj().T @ id_vec)
    id_resid = np.linalg.norm(id_vec - id_proj)
    print(f"Identity in algebra? Residual: {id_resid:.2e}")

    # Method 1: Compute center via direct commutator check
    # For each basis element e_i, compute [e_i, e_j] for all j.
    # e_i is central iff all commutators vanish.

    # First, compute products e_i * e_j and project back
    products = np.zeros((d_orth, d_orth, d_orth), dtype=complex)
    max_resid = 0
    for i in range(d_orth):
        for j in range(d_orth):
            prod = orth_basis[i] @ orth_basis[j]
            pv = prod.flatten()
            coeffs = Q.conj().T @ pv
            products[i, j, :] = coeffs
            resid = np.linalg.norm(pv - Q @ coeffs)
            max_resid = max(max_resid, resid)

    print(f"Closure check (max residual): {max_resid:.2e}")

    # Commutator structure constants
    # [e_i, e_j] = sum_k (c^k_{ij} - c^k_{ji}) e_k
    comm_struct = products - products.transpose(1, 0, 2)

    # Method 1a: Center = {x : [x, e_j] = 0 for all j}
    # sum_i x_i [e_i, e_j] = 0 for all j
    # sum_i x_i * (c^k_{ij} - c^k_{ji}) = 0 for all j, k

    # Separate real and imaginary parts for a REAL null space problem
    center_rows = []
    for j in range(d_orth):
        for k in range(d_orth):
            val = comm_struct[:, j, k]  # vector of length d_orth
            center_rows.append(val.real)
            center_rows.append(val.imag)

    center_mat = np.array(center_rows)
    center_rank = np.linalg.matrix_rank(center_mat, tol=1e-8)
    print(f"\nCenter constraint matrix: {center_mat.shape}, rank: {center_rank}")

    center_ns = null_space(center_mat, rcond=1e-8)
    center_dim_method1 = center_ns.shape[1]
    print(f"Center dim (method 1, real null space): {center_dim_method1}")

    # Method 1b: Use complex null space directly
    center_rows_complex = []
    for j in range(d_orth):
        for k in range(d_orth):
            center_rows_complex.append(comm_struct[:, j, k])

    center_mat_c = np.array(center_rows_complex)
    center_rank_c = np.linalg.matrix_rank(center_mat_c, tol=1e-8)
    center_ns_c = null_space(center_mat_c, rcond=1e-8)
    center_dim_complex = center_ns_c.shape[1]
    print(f"Center dim (method 1b, complex null space): {center_dim_complex}")

    # Method 2: Direct commutator test
    # For each basis element, compute its commutator with ALL other basis elements
    # and check if the commutator vanishes
    print("\nMethod 2: Direct commutator norms")
    comm_norms = np.zeros(d_orth)
    for i in range(d_orth):
        total = 0
        for j in range(d_orth):
            comm_ij = orth_basis[i] @ orth_basis[j] - orth_basis[j] @ orth_basis[i]
            total += np.linalg.norm(comm_ij)**2
        comm_norms[i] = np.sqrt(total)

    print(f"Commutator norms (sorted): {np.sort(comm_norms)[:10]}...")
    n_central = np.sum(comm_norms < 1e-6)
    print(f"Number of central basis elements: {n_central}")

    # Method 3: Check if the algebra is COMMUTATIVE
    is_commutative = max_resid < 1e-6 and np.max(np.abs(comm_struct)) < 1e-6
    print(f"\nMax commutator structure constant: {np.max(np.abs(comm_struct)):.2e}")
    print(f"Is the algebra commutative? {is_commutative}")

    if is_commutative:
        print("\n*** ALGEBRA IS COMMUTATIVE ***")
        print(f"This means center = entire algebra, dim = {d_orth}")
        print("A commutative semisimple algebra is a direct sum of copies of C (or R).")
        print("This would give C^k for some k, NOT A_F.")

    # ===================================================================
    # STEP 7: Investigate the REAL structure more carefully
    # ===================================================================

    print("\n--- REAL STRUCTURE ANALYSIS ---")
    # The J-compatible commutant is a real *-algebra.
    # The basis vectors are complex matrices, but the algebra
    # has a reality condition (T*Xi = Xi*conj(T)).
    #
    # Let's check: are the basis elements themselves real (T = conj(T))?
    # Or do they have nontrivial imaginary parts?

    for i in range(min(d_orth, 10)):
        T = orth_basis[i]
        re_norm = np.linalg.norm(T.real)
        im_norm = np.linalg.norm(T.imag)
        print(f"  Basis {i}: ||Re|| = {re_norm:.4f}, ||Im|| = {im_norm:.4f}")

    # Check: does the J-compatible algebra contain the PHASE 1 commutant?
    # Phase 1 had End_{U(2)}(Psi_+) = 20-dim complex.
    # These embed as (T_+, 0; 0, 0) in the 32-dim space.
    # After J-constraint, they should pair with the Psi_- sector.

    print("\n--- EMBEDDING OF PHASE 1 COMMUTANT ---")
    # Build Phase 1 commutant basis on C^16
    rho_plus_gens = [rho_plus(v) for v in basis_u2]
    constraint_16 = []
    for rv in rho_plus_gens:
        block = np.zeros((16*16, 16*16), dtype=complex)
        for i in range(16):
            for j in range(16):
                row = i*16 + j
                for k in range(16):
                    block[row, i*16 + k] += rv[k, j]
                    block[row, k*16 + j] -= rv[i, k]
        constraint_16.append(block)

    A16 = np.vstack(constraint_16)
    ns16 = null_space(A16, rcond=1e-10)
    d16 = ns16.shape[1]
    print(f"Phase 1 commutant dim on C^16: {d16}")

    # For each Phase 1 basis element T_+, embed as diag(T_+, 0) in C^32
    # and project onto the J-compatible commutant
    n_in_Jcompat = 0
    for k in range(d16):
        T16 = ns16[:, k].reshape(16, 16)
        T32 = np.zeros((32, 32), dtype=complex)
        T32[:16, :16] = T16
        # Project onto J-compatible commutant
        t_vec = T32.flatten()
        proj = Q @ (Q.conj().T @ t_vec)
        resid = np.linalg.norm(t_vec - proj)
        if resid < 1e-6:
            n_in_Jcompat += 1

    print(f"Phase 1 elements that survive J-projection: {n_in_Jcompat} / {d16}")

    # Also check: embed as diag(0, T_-) where T_- = G5*conj(T_+)*G5
    n_minus_in = 0
    for k in range(d16):
        T16 = ns16[:, k].reshape(16, 16)
        T16_minus = G5 @ np.conj(T16) @ G5
        T32 = np.zeros((32, 32), dtype=complex)
        T32[16:, 16:] = T16_minus
        t_vec = T32.flatten()
        proj = Q @ (Q.conj().T @ t_vec)
        resid = np.linalg.norm(t_vec - proj)
        if resid < 1e-6:
            n_minus_in += 1

    print(f"Phase 1 Psi_- elements that survive J-projection: {n_minus_in} / {d16}")

    # Check cross-sector elements
    # The J condition T*Xi = Xi*conj(T) for a block matrix (A, B; C, D):
    # (A, B; C, D) * (0, -G5; -G5, 0) = (0, -G5; -G5, 0) * (conj(A), conj(B); conj(C), conj(D))
    #
    # LHS: (-B*G5, -A*G5; -D*G5, -C*G5)
    # RHS: (-G5*conj(C), -G5*conj(D); -G5*conj(A), -G5*conj(B))
    #
    # So:
    # -B*G5 = -G5*conj(C)  =>  B*G5 = G5*conj(C)  =>  B = G5*conj(C)*G5
    # -A*G5 = -G5*conj(D)  =>  A*G5 = G5*conj(D)  =>  A = G5*conj(D)*G5
    # -D*G5 = -G5*conj(A)  =>  D*G5 = G5*conj(A)  =>  D = G5*conj(A)*G5
    # -C*G5 = -G5*conj(B)  =>  C*G5 = G5*conj(B)  =>  C = G5*conj(B)*G5
    #
    # From A = G5*conj(D)*G5 and D = G5*conj(A)*G5:
    # Substituting: A = G5*conj(G5*conj(A)*G5)*G5 = G5*G5*A*G5*G5 = A (consistent, using G5 real, G5^2=I)
    #
    # From B = G5*conj(C)*G5 and C = G5*conj(B)*G5:
    # Same consistency.
    #
    # So the J condition PAIRS:
    # - A with D: D = G5*conj(A)*G5
    # - B with C: C = G5*conj(B)*G5
    #
    # PLUS the gauge commutation condition.

    print("\n--- J CONDITION BLOCK STRUCTURE ---")
    print("J condition pairs: D = G5*conj(A)*G5, C = G5*conj(B)*G5")
    print("So a general J-compatible element is determined by (A, B) alone.")
    print(f"Effective degrees of freedom: dim(A) + dim(B) in the gauge commutant.")

    # Count how many independent A-blocks and B-blocks there are
    # among the J-compatible basis
    A_blocks = []
    B_blocks = []
    for T in Jbasis:
        A_blocks.append(T[:16, :16].flatten())
        B_blocks.append(T[:16, 16:].flatten())

    if len(A_blocks) > 0:
        A_mat = np.column_stack(A_blocks)
        B_mat = np.column_stack(B_blocks)
        A_rank = np.linalg.matrix_rank(A_mat, tol=1e-8)
        B_rank = np.linalg.matrix_rank(B_mat, tol=1e-8)
        print(f"Rank of A-blocks (++ sector): {A_rank}")
        print(f"Rank of B-blocks (+- sector): {B_rank}")
        print(f"Total: {A_rank + B_rank} (should relate to J-compat dim = {J_null_dim})")

    # ===================================================================
    # STEP 8: Check whether algebra is actually C^20 (commutative)
    # ===================================================================

    print("\n--- CHECKING IF ALGEBRA = C^20 ---")
    # If the J-compatible commutant is C^20 (commutative), then:
    # - It has 20 minimal idempotents
    # - Each idempotent projects onto a 1 or 2 dim subspace
    # - The algebra is the direct sum of these

    # A semisimple commutative algebra over C of dim d has exactly d
    # primitive idempotents (by Wedderburn: direct sum of d copies of C).
    # Over R: direct sum of copies of R and C.

    # Let's find the idempotents by diagonalizing a generic element
    if d_orth >= 2:
        np.random.seed(42)
        rand_coeffs = np.random.randn(d_orth)
        generic = sum(c * T for c, T in zip(rand_coeffs, orth_basis))

        # Check if generic is diagonalizable
        evals, evecs = np.linalg.eig(generic)
        print(f"Generic element eigenvalues: {np.sort(np.round(evals.real, 4))}")

        # Count distinct eigenvalues
        evals_rounded = np.round(evals, 4)
        unique_evals = np.unique(evals_rounded)
        print(f"Distinct eigenvalues: {len(unique_evals)}")
        for ev in unique_evals:
            mult = np.sum(np.abs(evals_rounded - ev) < 1e-3)
            print(f"  {ev}: multiplicity {mult}")

print("\nDone.")
