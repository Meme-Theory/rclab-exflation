"""
PHASE 2.5 FULL 32-DIM ORDER-ONE (OPTIMIZED)
=============================================

Optimized version: instead of scanning over all D_F, test specific D_F candidates
with the off-diagonal chirality structure.

Tests:
1. D_F with M = c<->b coupling (our original) -- but off-diagonal in chirality
2. D_F with M = left Yukawa (row coupling) -- off-diagonal in chirality
3. Verify J-compatibility and chirality anticommutation

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
def get_column_index(f):
    if f == 0: return 0
    elif 1 <= f <= 3: return f
    elif 4 <= f <= 6: return 0
    else: return (f - 7) % 3 + 1

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

def full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32

def o_map(gen_32):
    return Xi @ gen_32.T @ Xi


# Build A_F generators
AF_16 = []; AF_names = []; AF_factors = []

L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_16.append(build_bimodule_16(L_CIm, np.eye(4))); AF_names.append('C_Im'); AF_factors.append('C')
L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
AF_16.append(build_bimodule_16(L_CRe, np.eye(4))); AF_names.append('C_proj'); AF_factors.append('C')

L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_16.append(build_bimodule_16(L_Hi, np.eye(4))); AF_names.append('H_i'); AF_factors.append('H')
L_Hj = np.zeros((4, 4), dtype=complex); L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_16.append(build_bimodule_16(L_Hj, np.eye(4))); AF_names.append('H_j'); AF_factors.append('H')
L_Hk = np.zeros((4, 4), dtype=complex); L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_16.append(build_bimodule_16(L_Hk, np.eye(4))); AF_names.append('H_k'); AF_factors.append('H')
AF_16.append(build_bimodule_16(np.eye(4), np.eye(4))); AF_names.append('I'); AF_factors.append('H')

for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_elem.conj().T
            AF_16.append(build_bimodule_16(np.eye(4), R_m))
            AF_names.append(f'M3_E{a}{b}_{part}'); AF_factors.append('M3')

AF_32 = [full_32(g) for g in AF_16]
n_gen = len(AF_32)
print(f"Number of A_F generators: {n_gen}")


def test_order_one(D_F, label):
    """Test [[D_F, pi(a)], o(b)] = 0 for all pairs."""
    max_err = 0
    o1_fac = {}
    worst = None

    for i in range(n_gen):
        Da = D_F @ AF_32[i] - AF_32[i] @ D_F
        for j in range(n_gen):
            ob = o_map(AF_32[j])
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            if err > max_err:
                max_err = err
                worst = (AF_names[i], AF_names[j])
            pk = f'[{AF_factors[i]}, o({AF_factors[j]})]'
            if pk not in o1_fac:
                o1_fac[pk] = 0.0
            o1_fac[pk] = max(o1_fac[pk], err)

    print(f"\n{label}:")
    print(f"  Max error: {max_err:.2e}", end="")
    if worst and max_err > 1e-8:
        print(f"  (worst: {worst})")
    else:
        print()
    for pk in sorted(o1_fac.keys()):
        v = o1_fac[pk]
        s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"  {pk}: {s}")
    return max_err


def check_DF_properties(D_F, label):
    """Check hermiticity, chirality anticommutation, J-compatibility."""
    herm_err = np.max(np.abs(D_F - D_F.conj().T))
    anti_err = np.max(np.abs(D_F @ gamma_F + gamma_F @ D_F))
    j_err = np.max(np.abs(Xi @ D_F.conj() @ Xi - D_F))
    print(f"\n{label} properties:")
    print(f"  Hermitian:     {herm_err:.2e} {'PASS' if herm_err < 1e-10 else 'FAIL'}")
    print(f"  Anti-gamma_F:  {anti_err:.2e} {'PASS' if anti_err < 1e-10 else 'FAIL'}")
    print(f"  J-compatible:  {j_err:.2e} {'PASS' if j_err < 1e-10 else 'FAIL'}")
    return herm_err < 1e-10 and anti_err < 1e-10 and j_err < 1e-10


# =============================================================================
# TEST 1: c<->b coupling, OFF-DIAGONAL chirality
# =============================================================================
print("=" * 76)
print("TEST 1: c<->b M, off-diagonal chirality")
print("=" * 76)

M1 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    M1[j+1, j+4] = 1.0
    M1[j+4, j+1] = 1.0

D1 = np.zeros((32, 32), dtype=complex)
D1[:16, 16:] = M1.conj().T
D1[16:, :16] = M1
check_DF_properties(D1, "D1 (c<->b off-diag)")

# Check J-compatibility: need G5 M^T G5 = M
jc = G5 @ M1.T @ G5
print(f"  G5 M^T G5 = M check: {np.max(np.abs(jc - M1)):.2e}")

# If J-compatibility fails, project onto J-compatible part:
M1_proj = (M1 + G5 @ M1.T @ G5) / 2
D1_proj = np.zeros((32, 32), dtype=complex)
D1_proj[:16, 16:] = M1_proj.conj().T
D1_proj[16:, :16] = M1_proj
check_DF_properties(D1_proj, "D1_proj (J-compatible projection)")
test_order_one(D1_proj, "ORDER-ONE: D1_proj")


# =============================================================================
# TEST 2: Left Yukawa M, OFF-DIAGONAL chirality
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 2: Left Yukawa M, off-diagonal chirality")
print("=" * 76)

D_L = np.zeros((4, 4), dtype=complex)
for j in range(1, 4):
    D_L[0, j] = 1.0; D_L[j, 0] = 1.0

M2 = build_bimodule_16(D_L, np.eye(4, dtype=complex))
D2 = np.zeros((32, 32), dtype=complex)
D2[:16, 16:] = M2.conj().T
D2[16:, :16] = M2
check_DF_properties(D2, "D2 (left Yukawa off-diag)")

M2_proj = (M2 + G5 @ M2.T @ G5) / 2
D2_proj = np.zeros((32, 32), dtype=complex)
D2_proj[:16, 16:] = M2_proj.conj().T
D2_proj[16:, :16] = M2_proj

props_ok = check_DF_properties(D2_proj, "D2_proj (J-compatible projection)")
if props_ok:
    test_order_one(D2_proj, "ORDER-ONE: D2_proj (left Yukawa, J-compatible)")


# =============================================================================
# TEST 3: Block-diagonal D_F (WRONG chirality -- as comparison)
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 3: Block-diagonal D_F (WRONG: doesn't anti-commute with gamma)")
print("=" * 76)

D3 = np.zeros((32, 32), dtype=complex)
D3[:16, :16] = M1  # Same as previous sessions
D3[16:, 16:] = rho_minus(M1)
check_DF_properties(D3, "D3 (block-diagonal, WRONG)")
test_order_one(D3, "ORDER-ONE: D3 (block-diagonal)")


# =============================================================================
# TEST 4: Try M = identity (couples Psi_+ to Psi_- trivially)
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 4: M = identity")
print("=" * 76)

M4 = np.eye(16, dtype=complex)
M4_proj = (M4 + G5 @ M4.T @ G5) / 2
D4 = np.zeros((32, 32), dtype=complex)
D4[:16, 16:] = M4_proj.conj().T
D4[16:, :16] = M4_proj
check_DF_properties(D4, "D4 (M=I projected)")
test_order_one(D4, "ORDER-ONE: D4 (M=I)")


# =============================================================================
# TEST 5: M = diagonal on specific sectors
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 5: M = diagonal projections")
print("=" * 76)

# M that only acts on the c and b sectors
M5 = np.zeros((16, 16), dtype=complex)
for j in range(1, 7):  # indices 1-6 (c and b sectors)
    M5[j, j] = 1.0
M5_proj = (M5 + G5 @ M5.T @ G5) / 2
D5 = np.zeros((32, 32), dtype=complex)
D5[:16, 16:] = M5_proj.conj().T
D5[16:, :16] = M5_proj
props5 = check_DF_properties(D5, "D5 (diagonal on c,b)")
if props5:
    test_order_one(D5, "ORDER-ONE: D5 (diagonal c,b)")


# =============================================================================
# TEST 6: The key insight -- what does G5 M^T G5 = M mean?
# =============================================================================
print(f"\n{'=' * 76}")
print("ANALYSIS: J-COMPATIBILITY CONSTRAINT G5 M^T G5 = M")
print("=" * 76)

print(f"\nG5 diagonal: {np.diag(G5)}")
print(f"\nColumn index map:")
for k in range(16):
    ci = get_column_index(k)
    gs = G5_signs[k]
    print(f"  flat {k:2d} -> col {ci}, G5 sign = {gs:+.0f}")

# G5 M^T G5 = M means M_{ab} = G5_a G5_b M_{ba}
# If G5_a = G5_b (same sign): M_{ab} = M_{ba} (symmetric part)
# If G5_a = -G5_b (different sign): M_{ab} = -M_{ba} (antisymmetric part)
print(f"\nJ-compatibility: M_{{ab}} = G5_a * G5_b * M_{{ba}}")
print(f"  Same G5 sign -> symmetric: M_{{ab}} = M_{{ba}}")
print(f"  Different G5 sign -> antisymmetric: M_{{ab}} = -M_{{ba}}")

# Count dimensions
n_same = 0
n_diff = 0
for a in range(16):
    for b in range(a, 16):
        if G5_signs[a] * G5_signs[b] > 0:
            n_same += 1
        else:
            n_diff += 1
# Symmetric part: n_same entries (including diagonal), antisymmetric: n_diff off-diagonal pairs
# Symmetric: diagonal (where G5_a = G5_a, always same sign) + 2 x off-diagonal same-sign pairs
# But for complex M: each entry has Re and Im
# Total real params = 2 * (n_same_diag + n_same_offdiag + n_diff_offdiag)
# where n_same_diag = 16, n_same_offdiag = count of a<b with same sign, n_diff = a<b with different sign

n_plus = np.sum(G5_signs > 0)
n_minus = np.sum(G5_signs < 0)
print(f"\n  #(G5=+1): {n_plus}, #(G5=-1): {n_minus}")
print(f"  Symmetric sector: {n_plus}x{n_plus} + {n_minus}x{n_minus} = {n_plus*n_plus + n_minus*n_minus} complex entries")
print(f"  Antisymmetric sector: 2 * {n_plus}*{n_minus} = {2*n_plus*n_minus} complex entries")
# Symmetric M: M_{ab} = M_{ba} for same-sign pairs
# Complex symmetric = (n*(n+1)/2) complex params per block
n_sym_plus = n_plus * (n_plus + 1) // 2
n_sym_minus = n_minus * (n_minus + 1) // 2
n_antisym = n_plus * n_minus  # off-diagonal, antisymmetric: n_plus * n_minus independent complex entries
total_complex_params = n_sym_plus + n_sym_minus + n_antisym
print(f"  J-compatible M: {total_complex_params} complex params = {2*total_complex_params} real params")


# =============================================================================
# TEST 7: Random J-compatible M
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 7: RANDOM J-COMPATIBLE M (20 trials)")
print("=" * 76)

np.random.seed(123)
best_err = float('inf')
best_M = None
for trial in range(20):
    M_rand = np.random.randn(16, 16) + 1j * np.random.randn(16, 16)
    M_rand = (M_rand + G5 @ M_rand.T @ G5) / 2  # J-compatible projection
    M_rand = (M_rand + M_rand.conj().T) / 2  # Hermitian M -> hermitian D_F

    D_rand = np.zeros((32, 32), dtype=complex)
    D_rand[:16, 16:] = M_rand.conj().T
    D_rand[16:, :16] = M_rand

    max_err = 0
    for i in range(n_gen):
        Da = D_rand @ AF_32[i] - AF_32[i] @ D_rand
        for j in range(n_gen):
            ob = o_map(AF_32[j])
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            max_err = max(max_err, err)
            if max_err > 100:  # Early exit if clearly fails
                break
        if max_err > 100:
            break

    if max_err < best_err:
        best_err = max_err
        best_M = M_rand.copy()

    if trial < 5 or max_err < 1:
        print(f"  Trial {trial+1}: max error = {max_err:.4f}")

print(f"\n  Best of 20: max error = {best_err:.4f}")

# Now try an ANALYTIC construction: D_F = 0 (trivial) always satisfies order-one
print(f"\n  D_F = 0: trivially satisfies order-one (error = 0)")
print(f"  The question is whether ANY nontrivial D_F works.")

# Check if the answer is fundamentally NO for this bimodule
# by computing the constraint rank
print(f"\n{'=' * 76}")
print("CONSTRAINT RANK ANALYSIS (REDUCED)")
print("=" * 76)

# Use only key generators (1 from each factor) to estimate constraint rank
key_gen = [0, 2, 3, 6]  # C_Im, H_i, H_j, M3_E00_Re

# J-compatible M basis
M_basis_list = []
for a in range(16):
    for b in range(a, 16):
        if G5_signs[a] * G5_signs[b] > 0:
            # Symmetric: E_{ab} + E_{ba}
            E = np.zeros((16, 16), dtype=complex)
            if a == b:
                E[a, a] = 1.0
            else:
                E[a, b] = 1.0; E[b, a] = 1.0
            M_basis_list.append(E)
            E2 = np.zeros((16, 16), dtype=complex)
            if a == b:
                E2[a, a] = 1j
            else:
                E2[a, b] = 1j; E2[b, a] = 1j
            M_basis_list.append(E2)
        else:
            # Antisymmetric: E_{ab} - E_{ba}
            E = np.zeros((16, 16), dtype=complex)
            E[a, b] = 1.0; E[b, a] = -1.0
            M_basis_list.append(E)
            E2 = np.zeros((16, 16), dtype=complex)
            E2[a, b] = 1j; E2[b, a] = -1j
            M_basis_list.append(E2)

n_M = len(M_basis_list)
print(f"J-compatible M basis: {n_M} elements")

# Build constraint matrix for key generators
constraints = []
for ia in key_gen:
    pi_a = AF_32[ia]
    for ib in key_gen:
        o_b = o_map(AF_32[ib])
        for r in range(32):
            for c in range(32):
                row = np.zeros(n_M)
                for h in range(n_M):
                    Mh = M_basis_list[h]
                    Dh = np.zeros((32, 32), dtype=complex)
                    Dh[:16, 16:] = Mh.conj().T
                    Dh[16:, :16] = Mh
                    Da = Dh @ pi_a - pi_a @ Dh
                    dc = Da @ o_b - o_b @ Da
                    row[h] = dc[r, c].real
                if np.max(np.abs(row)) > 1e-14:
                    constraints.append(row)
                row_im = np.zeros(n_M)
                for h in range(n_M):
                    Mh = M_basis_list[h]
                    Dh = np.zeros((32, 32), dtype=complex)
                    Dh[:16, 16:] = Mh.conj().T
                    Dh[16:, :16] = Mh
                    Da = Dh @ pi_a - pi_a @ Dh
                    dc = Da @ o_b - o_b @ Da
                    row_im[h] = dc[r, c].imag
                if np.max(np.abs(row_im)) > 1e-14:
                    constraints.append(row_im)
    print(f"  After generator {AF_names[ia]}: {len(constraints)} constraints")

A_con = np.array(constraints)
print(f"\nConstraint matrix: {A_con.shape}")

ATA = A_con.T @ A_con
evals, evecs = np.linalg.eigh(ATA)
tol = 1e-8 * max(np.max(np.abs(evals)), 1e-10)
null_dim = np.sum(evals < tol)

print(f"Constraint rank: {n_M - null_dim}")
print(f"Null space (compatible D_F) dimension: {null_dim}")
print(f"Smallest eigenvalues: {sorted(evals)[:5]}")

if null_dim > 0:
    null_vecs = evecs[:, evals < tol]
    for k in range(min(null_dim, 3)):
        v = null_vecs[:, k]
        M_sol = sum(v[h] * M_basis_list[h] for h in range(n_M))
        D_sol = np.zeros((32, 32), dtype=complex)
        D_sol[:16, 16:] = M_sol.conj().T
        D_sol[16:, :16] = M_sol

        # Quick check against ALL generators
        max_err_full = 0
        for ia in range(n_gen):
            Da = D_sol @ AF_32[ia] - AF_32[ia] @ D_sol
            for ib in range(n_gen):
                ob = o_map(AF_32[ib])
                dc = Da @ ob - ob @ Da
                max_err_full = max(max_err_full, np.max(np.abs(dc)))

        # Check if M is nonzero
        M_norm = np.max(np.abs(M_sol))
        print(f"\n  Solution {k+1}: |M| = {M_norm:.4f}, full order-one error = {max_err_full:.2e}")
        if M_norm > 1e-8:
            # Show structure
            for r in range(16):
                for c in range(16):
                    if abs(M_sol[r, c]) > 0.05 * M_norm:
                        print(f"    M[{r},{c}] = {M_sol[r,c]:.4f}")
else:
    print(f"\nNO compatible D_F exists (with {len(key_gen)} key generators)!")
    print(f"Checking with just [M3, o(M3)] removed...")

    # Try: only left-factor generators (C, H) for the 'a' side
    constraints2 = []
    left_gen = [0, 1, 2, 3, 4]  # C_Im, C_proj, H_i, H_j, H_k
    right_gen = list(range(6, n_gen))  # M3 generators

    for ia in left_gen:
        pi_a = AF_32[ia]
        for ib in left_gen:
            o_b = o_map(AF_32[ib])
            for r in range(32):
                for c in range(32):
                    row = np.zeros(n_M)
                    for h in range(n_M):
                        Mh = M_basis_list[h]
                        Dh = np.zeros((32, 32), dtype=complex)
                        Dh[:16, 16:] = Mh.conj().T
                        Dh[16:, :16] = Mh
                        Da = Dh @ pi_a - pi_a @ Dh
                        dc = Da @ o_b - o_b @ Da
                        row[h] = dc[r, c].real
                    if np.max(np.abs(row)) > 1e-14:
                        constraints2.append(row)
                    row_im = np.zeros(n_M)
                    for h in range(n_M):
                        Mh = M_basis_list[h]
                        Dh = np.zeros((32, 32), dtype=complex)
                        Dh[:16, 16:] = Mh.conj().T
                        Dh[16:, :16] = Mh
                        Da = Dh @ pi_a - pi_a @ Dh
                        dc = Da @ o_b - o_b @ Da
                        row_im[h] = dc[r, c].imag
                    if np.max(np.abs(row_im)) > 1e-14:
                        constraints2.append(row_im)

    A2 = np.array(constraints2) if constraints2 else np.zeros((1, n_M))
    ATA2 = A2.T @ A2
    ev2, evec2 = np.linalg.eigh(ATA2)
    tol2 = 1e-8 * max(np.max(np.abs(ev2)), 1e-10)
    null2 = np.sum(ev2 < tol2)
    print(f"  LEFT-only constraints: rank={n_M - null2}, null={null2}")
