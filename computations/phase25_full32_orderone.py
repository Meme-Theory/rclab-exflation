"""
PHASE 2.5 FULL 32-DIM ORDER-ONE TEST
=====================================

CRITICAL REALIZATION: The order-one test on Psi_+ alone is INSUFFICIENT.
In Connes' NCG, order-one is [[D_F, pi(a)], J pi(b*) J^{-1}] = 0
on the FULL H_F = Psi_+ + Psi_-, with D_F being the FULL 32x32 operator
that COUPLES Psi_+ and Psi_- (off-diagonal in chirality).

The Psi_+ block test was wrong because:
- D_F anticommutes with gamma_F -> D_F is OFF-DIAGONAL in chirality
- D_F maps Psi_+ -> Psi_- and vice versa
- We tested with D_F block-diagonal (WRONG anticommutation with gamma_F!)

This script:
1. Constructs the CORRECT D_F (off-diagonal in chirality)
2. Builds full 32x32 pi(a) and o(b)
3. Tests order-one on full H_F

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

np.set_printoptions(precision=6, linewidth=140, suppress=True)


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


gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
def get_column_index(flat_idx_val):
    if flat_idx_val == 0: return 0
    elif 1 <= flat_idx_val <= 3: return flat_idx_val
    elif 4 <= flat_idx_val <= 6: return 0
    else: return (flat_idx_val - 7) % 3 + 1

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


# =============================================================================
# PART 1: The CORRECT D_F structure (off-diagonal in chirality)
# =============================================================================
print("=" * 76)
print("PART 1: D_F MUST BE OFF-DIAGONAL IN CHIRALITY")
print("=" * 76)

# In Connes' spectral triple, D_F ANTICOMMUTES with gamma_F:
# {D_F, gamma_F} = 0
# Since gamma_F = [[I, 0], [0, -I]], D_F must be:
# D_F = [[0, M^dag], [M, 0]]
# where M is a 16x16 matrix mapping Psi_+ -> Psi_-

# The Yukawa mass matrix M encodes the coupling between particles and antiparticles.
# In our conventions:
# Psi_+ = particles (with rho_plus representation)
# Psi_- = antiparticles (with rho_minus = G5 conj(rho_plus) G5)

# For the c<->b coupling (Baptista eq 2.65):
# M maps Psi_+(0,j) <-> Psi_+(j,0), but on the 32-dim space it should map
# Psi_+ -> Psi_-.

# The simplest off-diagonal D_F:
# M_{16x16} encodes the Yukawa coupling.
# In Connes, M typically couples different generations or isospin components.

# For the c<->b coupling interpreted as M:
M_cb = np.zeros((16, 16), dtype=complex)
for j in range(3):
    M_cb[j+1, j+4] = 1.0  # c_j -> b_j in Psi_- coordinates
    M_cb[j+4, j+1] = 1.0  # b_j -> c_j

# But wait -- M maps Psi_+ to Psi_-, and the representations are DIFFERENT.
# M should satisfy: rho_minus(M) = M (compatibility)
# or more precisely, M should intertwine between rho_plus and rho_minus.

# In Connes, the STANDARD D_F for the SM is:
# D_F = [[0, M^*], [M, 0]] where M is the mass matrix
# with M_jk = Y_jk (Yukawa coupling between generations j and k)

# For now, let's construct D_F as off-diagonal:
D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, 16:] = M_cb.conj().T  # M^dag block (upper-right)
D_F_32[16:, :16] = M_cb            # M block (lower-left)

print(f"\nD_F_32 structure:")
print(f"  D_F_32 = [[0, M^dag], [M, 0]]")
print(f"  M (c<->b coupling):")
for r in range(16):
    for c in range(16):
        if abs(M_cb[r, c]) > 1e-10:
            print(f"    M[{r},{c}] = {M_cb[r,c]:.1f}")

# Check anticommutation with gamma_F
anticomm = D_F_32 @ gamma_F + gamma_F @ D_F_32
print(f"\n  {{D_F, gamma_F}} max = {np.max(np.abs(anticomm)):.2e}")
if np.max(np.abs(anticomm)) < 1e-10:
    print("  CORRECT: D_F anticommutes with gamma_F!")
else:
    print("  ERROR: D_F does NOT anticommute with gamma_F!")

# Check hermiticity
print(f"  D_F hermitian: max |D_F - D_F^dag| = {np.max(np.abs(D_F_32 - D_F_32.conj().T)):.2e}")

# Check J-compatibility: J D_F = D_F J (for KO-dim 6, epsilon' = 1)
# Actually, for KO-dim 6: J D = epsilon' D J with epsilon' = 1
# So J D = D J
J = lambda v: Xi @ v.conj()  # J as operator
# For matrices: J M J^{-1} = Xi @ M^* @ Xi (since J^2 = I)
JDJ = Xi @ D_F_32.conj() @ Xi
print(f"  J-compatibility: max |J D_F J^{-1} - D_F| = {np.max(np.abs(JDJ - D_F_32)):.2e}")


# =============================================================================
# PART 2: Build full 32-dim generators
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 2: FULL 32-DIM A_F GENERATORS")
print(f"{'=' * 76}")

# pi(a) on 32-dim: [[rho_plus(a), 0], [0, rho_minus(a)]]
# where rho_minus(a) = G5 conj(rho_plus(a)) G5

def full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32


# o(b) = J pi(b*) J^{-1} = Xi @ pi(b*)^* @ Xi = Xi @ pi(b)^T @ Xi
# For the full formula: b* means complex conjugate of b,
# pi(b*) = rho_plus(b*) on Psi_+ = conj(rho_plus(b))
# J pi(b*) J^{-1} on 32-dim: Xi @ conj([[conj(b_16), 0], [0, rho_minus(conj(b_16))]]) @ Xi
#                             = Xi @ [[b_16, 0], [0, conj(rho_minus(conj(b_16)))]] @ Xi
# rho_minus(conj(b_16)) = G5 conj(conj(b_16)) G5 = G5 b_16 G5
# conj of that = G5 conj(b_16) G5 = rho_minus(b_16)
# So: Xi @ [[b_16, 0], [0, rho_minus(b_16)]] @ Xi
# = Xi @ pi(b) @ Xi  ... but Xi is not the same as identity...

# Let me just compute directly:
def o_map(gen_32):
    """o(b) = Xi @ gen_32^T @ Xi (from J pi(b*) J^{-1} = Xi @ pi(b)^T @ Xi)"""
    return Xi @ gen_32.T @ Xi


# Build all A_F generators on 16-dim first, then lift
AF_16 = []
AF_names = []
AF_factors = []

# C factor
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_16.append(build_bimodule_16(L_CIm, np.eye(4))); AF_names.append('C_Im'); AF_factors.append('C')
L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
AF_16.append(build_bimodule_16(L_CRe, np.eye(4))); AF_names.append('C_proj'); AF_factors.append('C')

# H factor
L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_16.append(build_bimodule_16(L_Hi, np.eye(4))); AF_names.append('H_i'); AF_factors.append('H')
L_Hj = np.zeros((4, 4), dtype=complex); L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_16.append(build_bimodule_16(L_Hj, np.eye(4))); AF_names.append('H_j'); AF_factors.append('H')
L_Hk = np.zeros((4, 4), dtype=complex); L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_16.append(build_bimodule_16(L_Hk, np.eye(4))); AF_names.append('H_k'); AF_factors.append('H')
AF_16.append(build_bimodule_16(np.eye(4), np.eye(4))); AF_names.append('H_1'); AF_factors.append('H')

# M_3(C) factor
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_elem.conj().T
            AF_16.append(build_bimodule_16(np.eye(4), R_m))
            AF_names.append(f'M3_E{a}{b}_{part}'); AF_factors.append('M3')

# Lift to 32-dim
AF_32 = [full_32(g) for g in AF_16]


# =============================================================================
# PART 3: Order-one on full 32-dim with OFF-DIAGONAL D_F
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 3: ORDER-ONE ON FULL 32-DIM (OFF-DIAGONAL D_F)")
print(f"{'=' * 76}")

max_o1 = 0
o1_by_factor = {}
worst_pair = None

for i in range(len(AF_32)):
    Da = D_F_32 @ AF_32[i] - AF_32[i] @ D_F_32
    for j in range(len(AF_32)):
        ob = o_map(AF_32[j])
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        if err > max_o1:
            max_o1 = err
            worst_pair = (AF_names[i], AF_names[j])
        pk = f'[{AF_factors[i]}, o({AF_factors[j]})]'
        if pk not in o1_by_factor:
            o1_by_factor[pk] = 0.0
        o1_by_factor[pk] = max(o1_by_factor[pk], err)

print(f"\nMax |[[D_F, pi(a)], o(b)]|: {max_o1:.2e}")
if worst_pair:
    print(f"Worst pair: {worst_pair}")
print(f"\nBy factor:")
for pk in sorted(o1_by_factor.keys()):
    v = o1_by_factor[pk]
    s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
    print(f"  {pk}: {s}")


# =============================================================================
# PART 4: Try with LEFT D_F (off-diagonal in chirality but LEFT within each block)
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 4: LEFT D_F (off-diagonal chirality + row coupling)")
print(f"{'=' * 76}")

# D_F that couples row 0 to rows 1-3 but is off-diagonal in chirality:
D_L = np.zeros((4, 4), dtype=complex)
for j in range(1, 4):
    D_L[0, j] = 1.0
    D_L[j, 0] = 1.0

M_left = build_bimodule_16(D_L, np.eye(4, dtype=complex))

D_F_left_32 = np.zeros((32, 32), dtype=complex)
D_F_left_32[:16, 16:] = M_left.conj().T
D_F_left_32[16:, :16] = M_left

anticomm2 = D_F_left_32 @ gamma_F + gamma_F @ D_F_left_32
print(f"  {{D_F_left, gamma_F}} max = {np.max(np.abs(anticomm2)):.2e}")
JDJ2 = Xi @ D_F_left_32.conj() @ Xi
print(f"  J-compatibility: max |JDJ - D| = {np.max(np.abs(JDJ2 - D_F_left_32)):.2e}")

max_o1_left = 0
o1_by_factor_left = {}
for i in range(len(AF_32)):
    Da = D_F_left_32 @ AF_32[i] - AF_32[i] @ D_F_left_32
    for j in range(len(AF_32)):
        ob = o_map(AF_32[j])
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        max_o1_left = max(max_o1_left, err)
        pk = f'[{AF_factors[i]}, o({AF_factors[j]})]'
        if pk not in o1_by_factor_left:
            o1_by_factor_left[pk] = 0.0
        o1_by_factor_left[pk] = max(o1_by_factor_left[pk], err)

print(f"\nMax |[[D_F_left, pi(a)], o(b)]|: {max_o1_left:.2e}")
print(f"\nBy factor:")
for pk in sorted(o1_by_factor_left.keys()):
    v = o1_by_factor_left[pk]
    s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
    print(f"  {pk}: {s}")


# =============================================================================
# PART 5: Scan over D_F forms to find ANY compatible one
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 5: FINDING D_F COMPATIBLE WITH A_F ON FULL 32-DIM")
print(f"{'=' * 76}")

# D_F must satisfy:
# 1. Hermitian: D_F = D_F^dag
# 2. Anti-commutes with gamma: {D_F, gamma_F} = 0 -> off-diagonal
# 3. J-compatible: J D_F J^{-1} = D_F (epsilon' = 1 for KO-dim 6)
# 4. Order-one: [[D_F, pi(a)], o(b)] = 0 for all a, b in A_F

# From (1) and (2): D_F = [[0, M^dag], [M, 0]] where M is 16x16
# From (1): M^dag M = hermitian, etc. -> M can be arbitrary 16x16 complex matrix
# and D_F is automatically hermitian.

# From (3): Xi @ D_F^* @ Xi = D_F
# D_F^* = [[0, M^T], [conj(M), 0]]
# Xi @ D_F^* @ Xi:
# Upper-left: Xi[:16,:16] 0 + Xi[:16,16:] conj(M) = -G5 conj(M)
# Xi^2 computation...
# Actually let me just use the matrix:
# Xi D_F^* Xi where Xi^2 = I (32x32)
# D_F^* has [[0, M^T], [M_bar, 0]]
# Xi @ [[0, M^T], [M_bar, 0]] @ Xi
# = [[-G5, 0], [0, -G5]] ... no, Xi = [[0,-G5],[-G5,0]]
# Xi @ A = [[-G5 * A_lower], [-G5 * A_upper]]
# (Xi A)[:16,:] = -G5 A[16:,:]
# So (Xi A Xi):
# Row 0-15, Col 0-15: (-G5)(A[16:,:16]) ... then x Xi...
# Let me just compute numerically.

# First: characterize M that satisfies J-compatibility
# M is a 16x16 complex matrix -> 512 real parameters
# J-compatibility + hermiticity reduce this
# Order-one adds more constraints

# Since the full space is large (512 real params for M), let's parametrize
# D_F as off-diagonal with M, and check order-one as linear constraint on M.

# Vectorize: M -> R^512 (real and imaginary parts of each entry)
def mat_to_vec_16(M):
    v = np.zeros(512)
    for r in range(16):
        for c in range(16):
            v[32*r + 2*c] = M[r, c].real
            v[32*r + 2*c + 1] = M[r, c].imag
    return v

def vec_to_mat_16(v):
    M = np.zeros((16, 16), dtype=complex)
    for r in range(16):
        for c in range(16):
            M[r, c] = v[32*r + 2*c] + 1j * v[32*r + 2*c + 1]
    return M

# Build J-compatibility constraint
# Xi @ D_F^* @ Xi = D_F means Xi @ conj(D_F) @ Xi = D_F
# For D_F = [[0, M^dag], [M, 0]]:
# conj(D_F) = [[0, M^T], [conj(M), 0]]
# Xi conj(D_F) Xi: let's compute the (lower-left) block:
# (Xi conj(D_F))_{16:,:16} = -G5 @ (conj(D_F))_{:16,:16} = -G5 @ 0 = 0
# Hmm, that's not right. Let me be careful:
# (Xi conj(D_F))_{16:, :} = [-G5 @ conj(D_F)[:16, :] + 0 @ conj(D_F)[16:, :]]
#                           = -G5 @ [[0, M^T]] = [[0, -G5 M^T]]
# Then (Xi conj(D_F) Xi)_{16:, :16} = [[0, -G5 M^T]] @ Xi[:,:16]
#                                    = 0 @ 0 + (-G5 M^T)@(-G5) = G5 M^T G5
# And D_F_{16:,:16} = M
# So J-compat requires: G5 M^T G5 = M, i.e., M = G5 M^T G5

# This is a SYMMETRIC-TYPE condition. Let's find how many real parameters survive.
M_basis = []
for r in range(16):
    for c in range(16):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            E = np.zeros((16, 16), dtype=complex)
            E[r, c] = val
            # J-compat projects: M -> (M + G5 M^T G5) / 2
            E_proj = (E + G5 @ E.T @ G5) / 2
            if np.max(np.abs(E_proj)) > 1e-14:
                M_basis.append(E_proj)

# Orthogonalize
from numpy.linalg import qr
vecs = np.array([mat_to_vec_16(M) for M in M_basis]).T
Q, R_qr = qr(vecs, mode='reduced')
keep = np.abs(np.diag(R_qr)) > 1e-10
Q_J = Q[:, keep]
n_J = Q_J.shape[1]
print(f"  J-compatible M space: {n_J} real dimensions (from 512)")

# Now impose order-one as constraint on M:
# D_F(M) = [[0, M^dag], [M, 0]]
# [[D_F(M), pi(a)], o(b)] = 0 for all a, b in A_F

# This is LINEAR in M (since pi(a) and o(b) are fixed).
# Build the constraint matrix in the J-compatible M coordinates.

print(f"  Building order-one constraint matrix...")

# Use a subset of generators (not all 24) to keep computation manageable
# Use one per factor type: C_Im, H_i, H_j, M3_E00_Re, M3_E01_Re
key_indices = [0, 2, 3, 6, 8]  # C_Im, H_i, H_j, M3_E00_Re, M3_E01_Re
# Actually use ALL generators for completeness
constraints_M = []
for ia in range(len(AF_32)):
    pi_a = AF_32[ia]
    for ib in range(len(AF_32)):
        o_b = o_map(AF_32[ib])
        # For each M (parametrized by Q_J coordinates), compute:
        # [[D_F(M), pi_a], o_b] at each (r,c) entry
        # This is linear in M. We need the 32x32 entries.
        # For efficiency, only check a subset of entries.
        for r in range(32):
            for c in range(32):
                row = np.zeros(n_J)
                for k in range(n_J):
                    M_k = vec_to_mat_16(Q_J[:, k])
                    D_k = np.zeros((32, 32), dtype=complex)
                    D_k[:16, 16:] = M_k.conj().T
                    D_k[16:, :16] = M_k
                    Da = D_k @ pi_a - pi_a @ D_k
                    dc = Da @ o_b - o_b @ Da
                    row[k] = dc[r, c].real
                if np.max(np.abs(row)) > 1e-14:
                    constraints_M.append(row)

                row_im = np.zeros(n_J)
                for k in range(n_J):
                    M_k = vec_to_mat_16(Q_J[:, k])
                    D_k = np.zeros((32, 32), dtype=complex)
                    D_k[:16, 16:] = M_k.conj().T
                    D_k[16:, :16] = M_k
                    Da = D_k @ pi_a - pi_a @ D_k
                    dc = Da @ o_b - o_b @ Da
                    row_im[k] = dc[r, c].imag
                if np.max(np.abs(row_im)) > 1e-14:
                    constraints_M.append(row_im)

        # Print progress every 100 pairs
        total_pairs = len(AF_32) ** 2
        current = ia * len(AF_32) + ib + 1
        if current % 100 == 0 or current == total_pairs:
            print(f"    Processed {current}/{total_pairs} pairs, {len(constraints_M)} constraints so far")

if len(constraints_M) > 0:
    A_M = np.array(constraints_M)
    print(f"\n  Full constraint matrix: {A_M.shape[0]} x {A_M.shape[1]}")

    # SVD to find null space
    ATA_M = A_M.T @ A_M
    evals_M, evecs_M = np.linalg.eigh(ATA_M)
    tol_M = 1e-6 * max(np.max(np.abs(evals_M)), 1e-10)
    null_M = evecs_M[:, evals_M < tol_M]

    print(f"  Null space dimension: {null_M.shape[1]}")
    print(f"  Smallest eigenvalues: {sorted(evals_M)[:10]}")

    if null_M.shape[1] > 0:
        print(f"\n  ORDER-ONE COMPATIBLE D_F EXISTS!")
        for k in range(min(null_M.shape[1], 3)):
            v = null_M[:, k]
            M_sol = vec_to_mat_16(Q_J @ v)
            D_sol = np.zeros((32, 32), dtype=complex)
            D_sol[:16, 16:] = M_sol.conj().T
            D_sol[16:, :16] = M_sol

            # Verify
            max_err = 0
            for ia in range(len(AF_32)):
                Da = D_sol @ AF_32[ia] - AF_32[ia] @ D_sol
                for ib in range(len(AF_32)):
                    ob = o_map(AF_32[ib])
                    dc = Da @ ob - ob @ Da
                    max_err = max(max_err, np.max(np.abs(dc)))

            print(f"\n  Solution {k+1}: max order-one error = {max_err:.2e}")
            print(f"  M nonzero entries:")
            for r in range(16):
                for c in range(16):
                    if abs(M_sol[r, c]) > 0.01 * np.max(np.abs(M_sol)):
                        print(f"    M[{r},{c}] = {M_sol[r,c]:.4f}")
    else:
        print(f"\n  NO ORDER-ONE COMPATIBLE D_F EXISTS for this A_F!")
        print(f"  (within J-compatible hermitian off-diagonal operators)")

        # Check if the constraint matrix has approximate null space
        print(f"\n  Near-null eigenvalues (10 smallest):")
        for ev in sorted(evals_M)[:10]:
            print(f"    {ev:.6e}")
else:
    print("  No constraints generated (empty algebra?)")
