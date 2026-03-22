"""
SESSION 11: CHIRALITY CATCH-22 SYSTEMATIC EXPLORATION
=====================================================

The catch-22 from Session 10:
  - Block-diagonal D_F: COMMUTES with gamma_F (wrong), 5/9 order-one PASS
  - Off-diagonal D_F: ANTICOMMUTES with gamma_F (correct), 9/9 order-one FAIL

This script systematically explores whether ANY D_F can satisfy BOTH constraints
simultaneously.

Strategy:
  1. Linear combinations D = alpha * D_block + beta * D_off
  2. Parameterized family search (gradient descent on constraint violation)
  3. Alternative coupling structures beyond row 0<->2, 1<->3
  4. Mathematical analysis of why the constraints may be incompatible

Key identity (mathematical backbone):
  gamma_F = diag(I_16, -I_16)
  Block-diagonal D commutes with gamma_F: [D_block, gamma_F] = 0
  Off-diagonal D anticommutes with gamma_F: {D_off, gamma_F} = 0

  For D = D_block + D_off:
    [D, gamma_F] = [D_block, gamma_F] + [D_off, gamma_F]
                  = 0 + 2 * gamma_F @ D_off
    {D, gamma_F} = {D_block, gamma_F} + {D_off, gamma_F}
                  = 2 * gamma_F @ D_block + 0

  So {D, gamma_F} = 0 iff D_block = 0 (ONLY off-diagonal).
  And [D, gamma_F] = 0 iff D_off = 0 (ONLY block-diagonal).

This means: anticommutation with gamma_F REQUIRES D to be purely off-diagonal.
The question reduces to: can ANY off-diagonal D_F satisfy order-one?

Author: Sim-Specialist Agent (phonon-exflation project, Session 11)
Date: 2026-02-12
"""

import numpy as np
import sys
import os
from itertools import product as iter_product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import su3_basis, u2_basis_in_su3, L_action_matrix, R_action_matrix

np.set_printoptions(precision=8, linewidth=140, suppress=True)


# =============================================================================
# INFRASTRUCTURE (from phase25_connes_embedding_test.py)
# =============================================================================

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

J = Xi  # J = Xi o complex_conjugation (applied separately)

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

def build_bimodule_16(L4, R4):
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


# =============================================================================
# PART 1: BUILD CONNES A_F GENERATORS
# =============================================================================

print("=" * 80)
print("PART 1: CONNES STANDARD A_F GENERATORS")
print("=" * 80)

AF_gens_16 = []
AF_names = []
AF_factor = []

# C factor
L_CIm = np.diag([1j, -1j, 1.0, 1.0])
AF_gens_16.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names.append('C_Im')
AF_factor.append('C')

L_CRe = np.diag([1.0, -1.0, 0.0, 0.0])
AF_gens_16.append(build_bimodule_16(L_CRe, np.eye(4, dtype=complex)))
AF_names.append('C_Re')
AF_factor.append('C')

# H factor
L_Hi = np.diag([0.0, 0.0, 1j, -1j])
AF_gens_16.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names.append('H_i')
AF_factor.append('H')

L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append('H_j')
AF_factor.append('H')

L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append('H_k')
AF_factor.append('H')

L_H1 = np.eye(4, dtype=complex)
AF_gens_16.append(build_bimodule_16(L_H1, np.eye(4, dtype=complex)))
AF_names.append('H_1=I')
AF_factor.append('H')

# M_3(C) factor
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            m_dag = m_elem.conj().T
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_dag
            AF_gens_16.append(build_bimodule_16(np.eye(4, dtype=complex), R_m))
            AF_names.append(f'M3_E{a}{b}_{part}')
            AF_factor.append('M3')

AF_gens_32 = [build_full_32(g) for g in AF_gens_16]

print(f"  Total generators: {len(AF_gens_32)}")
print(f"  Rank: {np.linalg.matrix_rank(np.column_stack([np.concatenate([T.flatten().real, T.flatten().imag]) for T in AF_gens_32]), tol=1e-8)}")


# =============================================================================
# PART 2: MATHEMATICAL PROOF -- ANTICOMMUTATION FORCES PURE OFF-DIAGONAL
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 2: MATHEMATICAL CONSTRAINT ANALYSIS")
print("=" * 80)

print("""
THEOREM: Any D_F on C^32 that anticommutes with gamma_F must be purely off-diagonal.

Proof:
  Write D = [[A, B], [C, D_block]] in the Psi_+ / Psi_- block decomposition.
  gamma_F = [[I, 0], [0, -I]].

  D @ gamma_F = [[A, -B], [C, -D_block]]
  gamma_F @ D = [[A, B], [-C, -D_block]]

  {D, gamma_F} = [[2A, 0], [0, -2*D_block]]

  {D, gamma_F} = 0 iff A = 0 AND D_block = 0.

  So D must have form [[0, B], [C, 0]] -- purely off-diagonal.
  For Hermiticity: C = B^dag.

COROLLARY: The block-diagonal part CANNOT contribute to a valid D_F.
  The linear combination D = alpha * D_block + beta * D_off satisfies
  {D, gamma_F} = 0 iff alpha = 0.

  The catch-22 reduces to: can ANY off-diagonal Hermitian D_F satisfy order-one?
""")


# =============================================================================
# PART 3: SYSTEMATIC OFF-DIAGONAL D_F SEARCH
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 3: SYSTEMATIC OFF-DIAGONAL D_F SEARCH")
print("=" * 80)

def make_off_diagonal_DF(B_16):
    """Build 32x32 off-diagonal D_F from a 16x16 block B.
    D = [[0, B], [B^dag, 0]] ensures Hermiticity.
    """
    D = np.zeros((32, 32), dtype=complex)
    D[:16, 16:] = B_16
    D[16:, :16] = B_16.conj().T
    return D

def check_j_compat(D32):
    """Check D @ J = J @ D_bar (J = Xi o conj)."""
    # JDJ^{-1} = Xi @ D_bar @ Xi  (since J^2 = I, J is own inverse)
    # For D to commute with J: D = Xi @ D_bar @ Xi
    return np.max(np.abs(D32 - Xi @ np.conj(D32) @ Xi))

def check_anticomm_gamma(D32):
    return np.max(np.abs(D32 @ gamma_F + gamma_F @ D32))

def compute_order_one_error(D32, gens_32, Xi_mat):
    """Compute max ||[[D,a], JbJ^{-1}]|| over all generator pairs."""
    max_err = 0.0
    for a in gens_32:
        Da = D32 @ a - a @ D32
        for b in gens_32:
            ob = Xi_mat @ b.T @ Xi_mat  # o(b) = Xi . b^T . Xi
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            if err > max_err:
                max_err = err
    return max_err

def compute_order_one_by_factor(D32, gens_32, names, factors, Xi_mat):
    """Return dict of max order-one error by factor pair."""
    o1_by_factor = {}
    for i, a in enumerate(gens_32):
        Da = D32 @ a - a @ D32
        for j, b in enumerate(gens_32):
            ob = Xi_mat @ b.T @ Xi_mat
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            pk = f'[{factors[i]}, o({factors[j]})]'
            o1_by_factor[pk] = max(o1_by_factor.get(pk, 0), err)
    return o1_by_factor


# --- 3a: Original D_F candidates, off-diagonal form ---

print("\n  --- 3a: Baseline off-diagonal candidates ---")

# Connes Yukawa (row 0<->2, 1<->3)
D_connes_left = np.zeros((4, 4), dtype=complex)
D_connes_left[0, 2] = 1.0; D_connes_left[2, 0] = 1.0
D_connes_left[1, 3] = 1.0; D_connes_left[3, 1] = 1.0
D_connes_16 = build_bimodule_16(D_connes_left, np.eye(4, dtype=complex))

# Baptista delta_v (c<->b)
D_baptista_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_baptista_16[j+1, j+4] = 1.0
    D_baptista_16[j+4, j+1] = 1.0

# Color-coupled
D_color_16 = np.zeros((16, 16), dtype=complex)
for col in range(4):
    for rpair in [(0, 2), (2, 0), (1, 3), (3, 1)]:
        fi = flat_idx(rpair[0], col)
        fj = flat_idx(rpair[1], col)
        D_color_16[fi, fj] = 1.0

baseline_candidates = {
    'Connes_Yukawa': D_connes_16,
    'Baptista_delta_v': D_baptista_16,
    'Color_coupled': D_color_16,
}

for name, B16 in baseline_candidates.items():
    D32 = make_off_diagonal_DF(B16)
    ac = check_anticomm_gamma(D32)
    jc = check_j_compat(D32)
    herm = np.max(np.abs(D32 - D32.conj().T))
    o1 = compute_order_one_error(D32, AF_gens_32, Xi)
    o1f = compute_order_one_by_factor(D32, AF_gens_32, AF_names, AF_factor, Xi)

    print(f"\n  {name}:")
    print(f"    Hermitian: {herm:.2e}")
    print(f"    J-compat:  {jc:.2e}")
    print(f"    {'{'}D,gamma_F{'}'} = 0: {ac:.2e}")
    print(f"    Order-one max: {o1:.2e}")
    for pk in sorted(o1f.keys()):
        v = o1f[pk]
        st = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"      {pk}: {st}")


# --- 3b: J-compatible off-diagonal D_F exploration ---

print(f"\n  --- 3b: J-compatible off-diagonal search ---")
print("  Constraint: D = [[0, B], [B^dag, 0]] with D = Xi @ D_bar @ Xi")
print("  This constrains B: B = -G5 @ B_bar @ (-G5) = G5 @ B_bar @ G5")

# J-compatibility for off-diagonal D:
#   D = [[0, B], [B^dag, 0]]
#   Xi @ D_bar @ Xi = [[0, -G5], [-G5, 0]] @ [[0, B_bar], [(B^dag)_bar, 0]] @ [[0, -G5], [-G5, 0]]
#
#   Xi @ D_bar = [[0, -G5], [-G5, 0]] @ [[0, B_bar], [B^T, 0]]
#              = [[-G5 @ B^T, 0], [0, -G5 @ B_bar]]
#
#   (Xi @ D_bar) @ Xi = [[-G5 @ B^T, 0], [0, -G5 @ B_bar]] @ [[0, -G5], [-G5, 0]]
#                      = [[G5 @ B^T @ G5, 0], [G5 @ B_bar @ G5, 0]]  # Wait, let me redo...
#
# Actually:
#   Xi = [[0, -G5], [-G5, 0]]
#   D_bar = [[0, B_bar], [(B^dag)_bar, 0]] = [[0, B_bar], [B^T, 0]]
#
#   Xi @ D_bar @ Xi = [[0,-G5],[-G5,0]] @ [[0,B_bar],[B^T,0]] @ [[0,-G5],[-G5,0]]
#
#   First: Xi @ D_bar:
#     top: [0*0 + (-G5)*B^T,  0*B_bar + (-G5)*0] = [-G5 @ B^T, 0]
#     bot: [-G5*0 + 0*B^T,    -G5*B_bar + 0*0]    = [0, -G5 @ B_bar]
#
#   Then (Xi @ D_bar) @ Xi:
#     top: [-G5@B^T*0 + 0*(-G5),  -G5@B^T*(-G5) + 0*0] = [0, G5@B^T@G5]
#     bot: [0*0 + (-G5@B_bar)*(-G5),  0*(-G5) + (-G5@B_bar)*0] = [G5@B_bar@G5, 0]
#
# So Xi @ D_bar @ Xi = [[0, G5@B^T@G5], [G5@B_bar@G5, 0]]
#
# For D = Xi@D_bar@Xi:
#   B = G5 @ B^T @ G5  (and B^dag = G5 @ B_bar @ G5)
#
# The B = G5 @ B^T @ G5 constraint is a SYMMETRY condition on B.

# Let's verify numerically
B_test = D_connes_16.copy()
B_transformed = G5 @ B_test.T @ G5
print(f"\n  Verification: B = G5 @ B^T @ G5 for Connes Yukawa:")
print(f"    ||B - G5 @ B^T @ G5|| = {np.max(np.abs(B_test - B_transformed)):.2e}")

B_test2 = D_baptista_16.copy()
B_transformed2 = G5 @ B_test2.T @ G5
print(f"  Verification for Baptista delta_v:")
print(f"    ||B - G5 @ B^T @ G5|| = {np.max(np.abs(B_test2 - B_transformed2)):.2e}")


# --- 3c: FULL parameterized off-diagonal search ---

print(f"\n  --- 3c: Parameterized off-diagonal D_F search ---")
print("  Strategy: parameterize B as 16x16 matrix satisfying:")
print("    (i)  B = G5 @ B^T @ G5  (J-compatibility)")
print("    (ii) D = [[0,B],[B^dag,0]] is Hermitian (automatic)")
print("  Then minimize order-one violation.")

# Build basis of J-compatible off-diagonal matrices
# B = G5 @ B^T @ G5 means: writing B_{ij}, we need B_{ij} = sum_{k,l} G5_{ik} B_{lk} G5_{lj}
# Since G5 is diagonal: B_{ij} = G5_{ii} * B_{ji} * G5_{jj}
# So B_{ij} = g_i * g_j * B_{ji}  where g_k = G5_{kk} = +/- 1.
#
# This means: B_{ij} = g_i * g_j * B_{ji}
# If g_i * g_j = +1: B_{ij} = B_{ji} (symmetric pair)
# If g_i * g_j = -1: B_{ij} = -B_{ji} (antisymmetric pair)
# Diagonal: B_{ii} = g_i^2 * B_{ii} = B_{ii} (always free)

print(f"\n  G5 diagonal signs: {np.diag(G5).real.astype(int)}")

# Count the independent real parameters
n_sym = 0   # symmetric pairs (real + imag each free)
n_anti = 0  # antisymmetric pairs (real + imag each free)
n_diag = 0  # diagonal (purely real or complex depending)

g = np.diag(G5).real
basis_B = []  # list of (name, B_matrix) for basis of J-compatible off-diag D

# Diagonal elements: B_{ii} is free (complex)
for i in range(16):
    # Real part
    B_re = np.zeros((16, 16), dtype=complex)
    B_re[i, i] = 1.0
    basis_B.append((f'diag_{i}_Re', B_re))
    # Imag part
    B_im = np.zeros((16, 16), dtype=complex)
    B_im[i, i] = 1j
    basis_B.append((f'diag_{i}_Im', B_im))
    n_diag += 1

# Off-diagonal pairs (i < j)
for i in range(16):
    for j in range(i+1, 16):
        if g[i] * g[j] > 0:
            # Symmetric: B_{ij} = B_{ji}
            B_re = np.zeros((16, 16), dtype=complex)
            B_re[i, j] = 1.0
            B_re[j, i] = 1.0
            basis_B.append((f'sym_{i}_{j}_Re', B_re))

            B_im = np.zeros((16, 16), dtype=complex)
            B_im[i, j] = 1j
            B_im[j, i] = 1j
            basis_B.append((f'sym_{i}_{j}_Im', B_im))
            n_sym += 1
        else:
            # Antisymmetric: B_{ij} = -B_{ji}
            B_re = np.zeros((16, 16), dtype=complex)
            B_re[i, j] = 1.0
            B_re[j, i] = -1.0
            basis_B.append((f'anti_{i}_{j}_Re', B_re))

            B_im = np.zeros((16, 16), dtype=complex)
            B_im[i, j] = 1j
            B_im[j, i] = -1j
            basis_B.append((f'anti_{i}_{j}_Im', B_im))
            n_anti += 1

print(f"  Diagonal: {n_diag}, Symmetric pairs: {n_sym}, Antisymmetric pairs: {n_anti}")
print(f"  Total real parameters: {len(basis_B)} = {2*n_diag + 2*n_sym + 2*n_anti}")
print(f"  (Expected: 16 diag * 2 + 120 off-diag * 2 = {16*2 + 120*2})")

# Verify basis validity
print(f"\n  Verifying all {len(basis_B)} basis elements satisfy B = G5 @ B^T @ G5...")
n_fail = 0
for name, B in basis_B:
    err = np.max(np.abs(B - G5 @ B.T @ G5))
    if err > 1e-14:
        print(f"    FAIL: {name}, error = {err:.2e}")
        n_fail += 1
print(f"  Result: {len(basis_B) - n_fail}/{len(basis_B)} PASS")


# =============================================================================
# PART 4: ORDER-ONE AS LINEAR SYSTEM
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 4: ORDER-ONE AS LINEAR CONSTRAINT ON D_F PARAMETERS")
print("=" * 80)

print("""
  Key insight: [[D, a], o(b)] is LINEAR in D.
  So for D = sum_k alpha_k * D_k (basis expansion),
    [[D, a], o(b)] = sum_k alpha_k * [[D_k, a], o(b)]

  Order-one is satisfied iff ALL [[D, a_i], o(b_j)] = 0.
  This gives a HOMOGENEOUS LINEAR SYSTEM in the alpha_k.

  We can solve this exactly: construct the constraint matrix M where
  M @ alpha = 0, and find its null space.
""")

# For efficiency, only use the non-identity C+H generators for the failing sector
# The failure is in [C,o(C)], [C,o(H)], [H,o(C)], [H,o(H)]
# Let's use ALL generators but focus on the failure pattern

n_basis = len(basis_B)
n_gens = len(AF_gens_32)

# The constraint is: for all (i,j), [[D, a_i], o(b_j)] = 0
# This is a 32x32 matrix equation for each (i,j) pair.
# Vectorized: for each (i,j), the constraint is a linear map from R^{n_basis} -> R^{32*32*2}
# Total constraints: n_gens^2 * 32^2 * 2 (real DOF of 32x32 complex matrix)

print(f"  Building constraint matrix...")
print(f"  n_basis = {n_basis}, n_gen_pairs = {n_gens**2}")
print(f"  Each constraint: 32x32 complex = 2048 real components")
print(f"  Total constraint rows: {n_gens**2 * 2048}")
print(f"  This is a {n_gens**2 * 2048} x {n_basis} linear system.")

# Build the basis D_F matrices (off-diagonal form on C^32)
D_basis_32 = []
for name, B in basis_B:
    D32 = make_off_diagonal_DF(B)
    D_basis_32.append(D32)

# Compute the order-one tensor: [[D_k, a_i], o(b_j)] for each k, i, j
# and flatten into constraint matrix

# For memory efficiency, we'll build the constraint matrix in batches
# First, precompute o(b_j) = Xi @ b_j^T @ Xi for all j
o_gens = [Xi @ b.T @ Xi for b in AF_gens_32]

# For each basis element k, compute the vectorized constraint
# Constraint matrix: M[row, k] where row indexes (i, j, matrix_element)

# Actually, n_gens^2 * 2048 = 576 * 2048 ~ 1.2M rows. This is large but feasible.
# n_basis = 272 columns. So M is 1.2M x 272. SVD is fine.

# But we can be smarter: we only need the NULL SPACE of M.
# Instead of building full M, use iterative null-space finding.

# Actually, let's just build it -- 1.2M x 272 of float64 ~ 2.5 GB. That's too much.
# Better approach: use the normal equations. M^T @ M is 272 x 272, and
# null(M) = null(M^T @ M). We can compute M^T @ M incrementally.

print(f"\n  Using normal equation approach (M^T @ M is {n_basis}x{n_basis})...")

MTM = np.zeros((n_basis, n_basis), dtype=float)

# For each generator pair (i,j), compute the 272-vector of constraint contributions
# and accumulate M^T @ M
n_pairs_processed = 0
for i in range(n_gens):
    a_i = AF_gens_32[i]
    for j in range(n_gens):
        ob_j = o_gens[j]

        # For each basis D_k: compute [[D_k, a_i], ob_j]
        # = (D_k @ a_i - a_i @ D_k) @ ob_j - ob_j @ (D_k @ a_i - a_i @ D_k)

        # Precompute a_i @ ob_j and ob_j @ a_i for reuse
        # [[D_k, a_i], ob_j] = D_k @ a_i @ ob_j - a_i @ D_k @ ob_j
        #                     - ob_j @ D_k @ a_i + ob_j @ a_i @ D_k

        # This is linear in D_k. For each k:
        # C_k = D_k @ (a_i @ ob_j) - (a_i) @ D_k @ ob_j - ob_j @ D_k @ a_i + (ob_j @ a_i) @ D_k

        aiobj = a_i @ ob_j
        objai = ob_j @ a_i

        # For each k, flatten C_k and compute inner products
        vecs = np.zeros((n_basis, 2048), dtype=float)  # 2048 = 32*32*2 real components
        for k in range(n_basis):
            Dk = D_basis_32[k]
            Ck = Dk @ aiobj - a_i @ Dk @ ob_j - ob_j @ Dk @ a_i + objai @ Dk
            vecs[k, :] = np.concatenate([Ck.flatten().real, Ck.flatten().imag])

        # Accumulate M^T @ M
        MTM += vecs @ vecs.T
        n_pairs_processed += 1

print(f"  Processed {n_pairs_processed} generator pairs.")
print(f"  ||M^T M||_F = {np.linalg.norm(MTM):.6e}")

# Find null space of MTM
eigenvalues, eigenvectors = np.linalg.eigh(MTM)
print(f"\n  Eigenvalue spectrum of M^T M:")
print(f"    Min 10: {eigenvalues[:10]}")
print(f"    Max 10: {eigenvalues[-10:]}")

# Count null eigenvalues (within tolerance)
tol = 1e-8 * eigenvalues[-1]  # relative tolerance
n_null = np.sum(eigenvalues < tol)
print(f"\n  Null space dimension: {n_null} (tolerance: {tol:.2e})")

if n_null > 0:
    print(f"\n  *** NON-TRIVIAL NULL SPACE FOUND! ***")
    null_vecs = eigenvectors[:, :n_null]

    # Reconstruct the D_F solutions
    for sol_idx in range(min(n_null, 5)):
        alpha = null_vecs[:, sol_idx]

        # Build B = sum_k alpha_k * B_k
        B_sol = np.zeros((16, 16), dtype=complex)
        for k in range(n_basis):
            B_sol += alpha[k] * basis_B[k][1]

        D_sol = make_off_diagonal_DF(B_sol)

        herm = np.max(np.abs(D_sol - D_sol.conj().T))
        jc = check_j_compat(D_sol)
        ac = check_anticomm_gamma(D_sol)
        o1 = compute_order_one_error(D_sol, AF_gens_32, Xi)

        print(f"\n  Solution #{sol_idx+1}:")
        print(f"    Hermitian: {herm:.2e}")
        print(f"    J-compat:  {jc:.2e}")
        print(f"    {'{'}D,gamma_F{'}'}: {ac:.2e}")
        print(f"    Order-one: {o1:.2e}")
        print(f"    ||B||_F:   {np.linalg.norm(B_sol):.6f}")
        print(f"    Non-zero elements (|B_{ij}| > 0.01):")
        for ii in range(16):
            for jj in range(16):
                if abs(B_sol[ii, jj]) > 0.01:
                    print(f"      B[{ii},{jj}] = {B_sol[ii,jj]:.6f}")
else:
    print(f"\n  NULL SPACE IS EMPTY.")
    print(f"  No off-diagonal D_F satisfies order-one with the Connes A_F embedding.")
    print(f"  The catch-22 is mathematically IRRECONCILABLE for this H_F.")

    # Find the LEAST violating direction
    print(f"\n  Least-violating D_F (minimum eigenvalue direction):")
    alpha_min = eigenvectors[:, 0]

    B_min = np.zeros((16, 16), dtype=complex)
    for k in range(n_basis):
        B_min += alpha_min[k] * basis_B[k][1]

    D_min = make_off_diagonal_DF(B_min)

    herm = np.max(np.abs(D_min - D_min.conj().T))
    jc = check_j_compat(D_min)
    ac = check_anticomm_gamma(D_min)
    o1 = compute_order_one_error(D_min, AF_gens_32, Xi)
    o1f = compute_order_one_by_factor(D_min, AF_gens_32, AF_names, AF_factor, Xi)

    print(f"    Hermitian: {herm:.2e}")
    print(f"    J-compat:  {jc:.2e}")
    print(f"    {'{'}D,gamma_F{'}'}: {ac:.2e}")
    print(f"    Order-one: {o1:.2e}")
    print(f"    Smallest eigenvalue: {eigenvalues[0]:.6e}")
    for pk in sorted(o1f.keys()):
        v = o1f[pk]
        st = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"      {pk}: {st}")


# =============================================================================
# PART 5: RELAXED SEARCH -- GAMMA_F APPROXIMATE ANTICOMMUTATION
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 5: RELAXED SEARCH -- TRADE OFF ANTICOMMUTATION vs ORDER-ONE")
print("=" * 80)

print("""
  If strict anticommutation forces null order-one solutions, consider:
  D = cos(theta) * D_block + sin(theta) * D_off

  At theta=0: D commutes with gamma_F, 5/9 order-one PASS
  At theta=pi/2: D anticommutes, 0/9 order-one PASS (if null space empty)

  Sweep theta to find the Pareto frontier.
""")

# Use Connes_left_Yukawa as the prototype D_F
D_block_full = np.zeros((32, 32), dtype=complex)
D_block_full[:16, :16] = D_connes_16
D_block_full[16:, 16:] = rho_minus(D_connes_16)

D_off_full = make_off_diagonal_DF(D_connes_16)

thetas = np.linspace(0, np.pi/2, 19)
print(f"\n  theta | anticomm(gamma_F) | commut(gamma_F) | order-one max | C-C    | M3-M3")
print(f"  {'-'*85}")

for theta in thetas:
    D_mix = np.cos(theta) * D_block_full + np.sin(theta) * D_off_full

    ac = np.max(np.abs(D_mix @ gamma_F + gamma_F @ D_mix))
    cm = np.max(np.abs(D_mix @ gamma_F - gamma_F @ D_mix))
    o1f = compute_order_one_by_factor(D_mix, AF_gens_32, AF_names, AF_factor, Xi)
    o1 = max(o1f.values())
    cc = o1f.get('[C, o(C)]', 0)
    mm = o1f.get('[M3, o(M3)]', 0)

    print(f"  {theta:5.3f} | {ac:18.4f} | {cm:16.4f} | {o1:13.4f} | {cc:6.4f} | {mm:6.4f}")


# =============================================================================
# PART 6: ALTERNATIVE COUPLING STRUCTURES
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 6: ALTERNATIVE OFF-DIAGONAL COUPLING STRUCTURES")
print("=" * 80)

print("  Testing D_F with different row-row coupling patterns (off-diagonal on C^32):")

# All 2-element coupling patterns between 4 rows
row_couplings = [
    ("0<->1", [(0,1),(1,0)]),
    ("0<->2", [(0,2),(2,0)]),
    ("0<->3", [(0,3),(3,0)]),
    ("1<->2", [(1,2),(2,1)]),
    ("1<->3", [(1,3),(3,1)]),
    ("2<->3", [(2,3),(3,2)]),
    ("0<->2,1<->3 (Connes)", [(0,2),(2,0),(1,3),(3,1)]),
    ("0<->1,2<->3", [(0,1),(1,0),(2,3),(3,2)]),
    ("0<->3,1<->2", [(0,3),(3,0),(1,2),(2,1)]),
    ("all_pairs", [(i,j) for i in range(4) for j in range(4) if i != j]),
]

for name, pairs in row_couplings:
    # Build a D_F that couples specified row pairs, acting on ALL columns
    B16 = np.zeros((16, 16), dtype=complex)
    for col in range(4):
        for (r1, r2) in pairs:
            fi = flat_idx(r1, col)
            fj = flat_idx(r2, col)
            B16[fi, fj] = 1.0

    D32 = make_off_diagonal_DF(B16)
    jc = check_j_compat(D32)
    ac = check_anticomm_gamma(D32)
    o1 = compute_order_one_error(D32, AF_gens_32, Xi)
    o1f = compute_order_one_by_factor(D32, AF_gens_32, AF_names, AF_factor, Xi)

    n_pass = sum(1 for v in o1f.values() if v < 1e-8)
    n_total = len(o1f)

    print(f"\n  {name}:")
    print(f"    J-compat: {jc:.2e}, anticomm: {ac:.2e}")
    print(f"    Order-one: {o1:.2e} ({n_pass}/{n_total} factor pairs PASS)")
    for pk in sorted(o1f.keys()):
        v = o1f[pk]
        if v > 1e-8:
            print(f"      {pk}: FAIL ({v:.2e})")


# =============================================================================
# PART 7: RIGHT-ACTION D_F (Yukawa as right multiplication)
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 7: RIGHT-ACTION D_F CANDIDATES")
print("=" * 80)

print("  Testing D_F = Psi -> Psi . Y (right multiplication by Yukawa)")

# Right multiplication by column-mixing matrix
right_couplings = {
    "R_01": ([(0,1),(1,0)], "col 0 <-> col 1 (lepton <-> quark)"),
    "R_12": ([(1,2),(2,1)], "col 1 <-> col 2"),
    "R_13": ([(1,3),(3,1)], "col 1 <-> col 3"),
    "R_23": ([(2,3),(3,2)], "col 2 <-> col 3"),
    "R_color_mix": ([(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)], "all color mixing"),
}

for name, (pairs, desc) in right_couplings.items():
    R4 = np.zeros((4, 4), dtype=complex)
    for (a, b) in pairs:
        R4[a, b] = 1.0
    B16 = build_bimodule_16(np.eye(4, dtype=complex), R4)
    D32 = make_off_diagonal_DF(B16)

    jc = check_j_compat(D32)
    ac = check_anticomm_gamma(D32)
    o1 = compute_order_one_error(D32, AF_gens_32, Xi)
    o1f = compute_order_one_by_factor(D32, AF_gens_32, AF_names, AF_factor, Xi)
    n_pass = sum(1 for v in o1f.values() if v < 1e-8)

    print(f"\n  {name} ({desc}):")
    print(f"    J-compat: {jc:.2e}, anticomm: {ac:.2e}")
    print(f"    Order-one: {o1:.2e} ({n_pass}/{len(o1f)} PASS)")


# =============================================================================
# PART 8: MIXED LEFT-RIGHT D_F
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 8: MIXED LEFT-RIGHT D_F (Psi -> L . Psi . R)")
print("=" * 80)

print("  Testing bimodule-type D_F with both row AND column coupling:")

# The SM Yukawa is precisely: D_F . Psi = Y_up . Psi . P_R + Y_down . Psi . P_L
# where P_R, P_L project onto color/lepton sectors.
# Let's try various L-R combinations.

mixed_candidates = {
    "LR_chirality_color": {
        "L4": D_connes_left,  # row 0<->2, 1<->3 (chirality flip)
        "R4": np.diag([0, 1, 1, 1]).astype(complex),  # project onto color
    },
    "LR_chirality_lepton": {
        "L4": D_connes_left,
        "R4": np.diag([1, 0, 0, 0]).astype(complex),  # project onto lepton
    },
    "LR_02_diag_color": {
        "L4": np.array([[0,0,1,0],[0,0,0,0],[1,0,0,0],[0,0,0,0]], dtype=complex),
        "R4": np.diag([1, 1, 1, 1]).astype(complex),
    },
}

for name, d in mixed_candidates.items():
    B16 = build_bimodule_16(d["L4"], d["R4"])
    D32 = make_off_diagonal_DF(B16)

    jc = check_j_compat(D32)
    ac = check_anticomm_gamma(D32)
    o1 = compute_order_one_error(D32, AF_gens_32, Xi)
    o1f = compute_order_one_by_factor(D32, AF_gens_32, AF_names, AF_factor, Xi)
    n_pass = sum(1 for v in o1f.values() if v < 1e-8)

    print(f"\n  {name}:")
    print(f"    J-compat: {jc:.2e}, anticomm: {ac:.2e}")
    print(f"    Order-one: {o1:.2e} ({n_pass}/{len(o1f)} PASS)")
    for pk in sorted(o1f.keys()):
        v = o1f[pk]
        st = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"      {pk}: {st}")


# =============================================================================
# PART 9: SUMMARY AND VERDICT
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 9: SUMMARY")
print("=" * 80)

print(f"""
CHIRALITY CATCH-22 ANALYSIS COMPLETE
=====================================

MATHEMATICAL FACTS:
  1. {'{'}D, gamma_F{'}'} = 0 REQUIRES D to be purely off-diagonal (PROVEN).
  2. The order-one condition [[D,a],o(b)] = 0 is LINEAR in D.
  3. The null space dimension of the off-diagonal order-one system: {n_null}
  4. Smallest eigenvalue of M^T M: {eigenvalues[0]:.6e}

INTERPRETATION:
""")

if n_null == 0:
    print("""  The null space is EMPTY. There is NO off-diagonal D_F on this H_F = C^32
  that simultaneously:
    (a) anticommutes with gamma_F (chirality)
    (b) satisfies order-one [[D,a],o(b)] = 0 for Connes' A_F

  This is a MATHEMATICAL IMPOSSIBILITY, not a failure to search hard enough.
  The constraint system M @ alpha = 0 has no non-trivial solutions.

  IMPLICATIONS:
  - The Baptista H_F (with this specific gamma_F and J) cannot support
    Connes' standard A_F spectral triple with ANY chirality-correct D_F.
  - This is the SAME space where KO-dim=6 was confirmed in Session 8.
  - The KO-dimension and the order-one condition are in TENSION.

  POSSIBLE RESOLUTIONS:
  (a) Different gamma_F (not the standard +/-I block form)
  (b) Different J (not Xi-based)
  (c) The correct D_F comes from D_K on SU(3) and modifies the constraints
  (d) The Baptista framework requires a modified NCG axiom set
  (e) A_F is NOT the correct target -- the actual algebra is different
""")
else:
    print(f"  A {n_null}-dimensional family of valid D_F exists!")
    print(f"  The catch-22 IS resolvable.")

print(f"\nScript complete.")
