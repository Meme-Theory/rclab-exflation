"""
PHASE 2.5 DECISIVE TEST: Connes Standard A_F Embedding on Baptista's H_F
=========================================================================

The gen-physicist corrected the row identification:
  Row 0 = up-RH (nu_R), Row 1 = down-RH (e_R), Row 2 = up-LH (nu_L), Row 3 = down-LH (e_L)
This MATCHES Connes' convention.

Previous scripts used a "Baptista-inspired" embedding where C_Im = diag(i,1,1,1)
and H_i = diag(i,-i,i,-i). The character theory proof showed these are NOT unitarily
equivalent to the Connes embedding.

THIS SCRIPT tests the CONNES STANDARD embedding:
  C: lambda -> diag(lambda, lambda_bar, 1, 1)    [acts on RH rows 0,1]
  H: q -> diag(1, 1, q_{2x2})                    [acts on LH rows 2,3]
  M_3(C): m -> diag(1, m^dag)                    [acts on color cols 1-3]

Combined with BOTH:
  (a) Baptista D_F from eq 2.65 (delta_v, partial transpose c<->b)
  (b) Various D_F candidates including Connes-type Yukawa

If (a) fails but (b) passes, gen-physicist's insight is confirmed:
  delta_v is NOT the correct D_F; the actual D_F comes from D_K.

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import su3_basis, u2_basis_in_su3, L_action_matrix, R_action_matrix

np.set_printoptions(precision=10, linewidth=140, suppress=True)


# =============================================================================
# INFRASTRUCTURE
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
    """Build 16x16 for bimodule action: Psi -> L4 . Psi . R4
    pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j]"""
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen

def vec_real(T):
    return np.concatenate([T.flatten().real, T.flatten().imag])


# =============================================================================
# PART 1: CONNES STANDARD A_F GENERATORS
# =============================================================================

print("=" * 76)
print("PART 1: CONNES STANDARD A_F EMBEDDING")
print("=" * 76)

AF_gens_16 = []
AF_names = []
AF_factor = []

# -- C FACTOR (dim 2) --
# Connes: (lambda, 1, I_3) -> L = diag(lambda, lambda_bar, 1, 1), R = I_4
# C_Im: lambda = i -> diag(i, -i, 1, 1)
L_CIm = np.diag([1j, -1j, 1.0, 1.0])
AF_gens_16.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names.append('C_Im')
AF_factor.append('C')

# C_Re_proj: lambda-dependent part
L_CRe = np.diag([1.0, -1.0, 0.0, 0.0])  # lambda=1 piece minus identity
AF_gens_16.append(build_bimodule_16(L_CRe, np.eye(4, dtype=complex)))
AF_names.append('C_Re')
AF_factor.append('C')

# -- H FACTOR (dim 4) --
# Connes: (1, q, I_3) -> L = diag(1, 1, q_{2x2}), R = I_4
# H_i: q = i -> diag(1, 1, i, -i) -> subtract identity to get generator
L_Hi = np.diag([0.0, 0.0, 1j, -1j])
AF_gens_16.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names.append('H_i')
AF_factor.append('H')

# H_j: q = j -> diag(1, 1, [[0,1],[-1,0]])
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append('H_j')
AF_factor.append('H')

# H_k: q = k
L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append('H_k')
AF_factor.append('H')

# H_1 = identity on rows 2-3 (included for closure)
L_H1 = np.eye(4, dtype=complex)
AF_gens_16.append(build_bimodule_16(L_H1, np.eye(4, dtype=complex)))
AF_names.append('H_1=I')
AF_factor.append('H')

# -- M_3(C) FACTOR (dim 18) --
# (1, 1, m) -> L = I_4, R = diag(1, m^dag)
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

print(f"  Total generators: {len(AF_gens_16)}")

# Extend to C^32
AF_gens_32 = [build_full_32(g) for g in AF_gens_16]

# Rank
AF_vecs = [vec_real(T) for T in AF_gens_32]
AF_rank = np.linalg.matrix_rank(np.column_stack(AF_vecs), tol=1e-8)
print(f"  Rank: {AF_rank} (target: 24)")

# J-compatibility
j_max = max(np.max(np.abs(T @ Xi - Xi @ np.conj(T))) for T in AF_gens_32)
print(f"  J-compatibility max error: {j_max:.2e}")

# Character check
print(f"\n  Character verification (Connes embedding):")
print(f"    Tr(C_Im)  = {np.trace(L_CIm):.4f} (expect 0 = i + (-i) + 1 + 1 - 2 offset... actual: {np.trace(AF_gens_16[0]):.4f})")
print(f"    Tr(H_i)   = {np.trace(L_Hi):.4f}")


# =============================================================================
# PART 2: CONSTRUCT MULTIPLE D_F CANDIDATES
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 2: D_F CANDIDATES")
print("=" * 76)

# D_F TYPE 1: Baptista delta_v (c<->b coupling, partial transpose)
# From eq 2.65: couples Psi(0,j) <-> Psi(j,0) i.e. c_j <-> b_j
D_baptista_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_baptista_16[j+1, j+4] = 1.0  # c_j -> b_j
    D_baptista_16[j+4, j+1] = 1.0  # b_j -> c_j

# D_F TYPE 2: Connes Yukawa (couples row 0 <-> row 2, row 1 <-> row 3)
# In Connes, D_F couples RH to LH within each column:
#   nu_R <-> nu_L (row 0 <-> row 2), e_R <-> e_L (row 1 <-> row 3)
# On the 4x4 matrix Psi, this is LEFT multiplication by an off-diagonal matrix
# coupling rows (0,2) and (1,3)
D_connes_left = np.zeros((4, 4), dtype=complex)
D_connes_left[0, 2] = 1.0; D_connes_left[2, 0] = 1.0  # nu_R <-> nu_L
D_connes_left[1, 3] = 1.0; D_connes_left[3, 1] = 1.0  # e_R <-> e_L

D_connes_16 = build_bimodule_16(D_connes_left, np.eye(4, dtype=complex))

# D_F TYPE 3: Generalized Yukawa (couples RH to LH with Yukawa matrix Y)
# D_F . Psi = Y . Psi where Y has off-diagonal blocks coupling chiralities
# Y = [[0, Y_u], [Y_d, 0]] in the (RH, LH) block structure
# For simplicity, Y_u = Y_d = I_2 (degenerate Yukawa)
D_yukawa_16 = D_connes_16.copy()

# D_F TYPE 4: Connes + color-dependent Yukawa
# D_F . Psi = Y_col . Psi . Z_col where Y couples chiralities, Z is color-dependent
# This allows different Yukawa couplings for different colors
D_connes_color = np.zeros((16, 16), dtype=complex)
for col in range(4):
    # For each column, couple row 0<->2 and row 1<->3
    for rpair in [(0, 2), (2, 0), (1, 3), (3, 1)]:
        fi = flat_idx(rpair[0], col)
        fj = flat_idx(rpair[1], col)
        D_connes_color[fi, fj] = 1.0

DF_candidates = {
    'Baptista_delta_v': D_baptista_16,
    'Connes_left_Yukawa': D_connes_16,
    'Connes_color_coupled': D_connes_color,
}

# Properties check
for name, DF16 in DF_candidates.items():
    DF32 = np.zeros((32, 32), dtype=complex)
    # Try block-diagonal first
    DF32[:16, :16] = DF16
    DF32[16:, 16:] = rho_minus(DF16)

    herm = np.max(np.abs(DF32 - DF32.conj().T))
    j_compat = np.max(np.abs(DF32 @ Xi - Xi @ np.conj(DF32)))
    anticomm = np.max(np.abs(DF32 @ gamma_F + gamma_F @ DF32))
    comm = np.max(np.abs(DF32 @ gamma_F - gamma_F @ DF32))

    print(f"\n  {name} (block-diagonal on 32):")
    print(f"    Hermitian: {herm:.2e}")
    print(f"    J-compatible: {j_compat:.2e}")
    print(f"    anticommutes(gamma_F): {anticomm:.2e}")
    print(f"    commutes(gamma_F): {comm:.2e}")

# Also try OFF-DIAGONAL chirality placement
print(f"\n  --- Off-diagonal D_F (maps Psi+ <-> Psi-) ---")
for name, DF16 in DF_candidates.items():
    DF32_off = np.zeros((32, 32), dtype=complex)
    DF32_off[:16, 16:] = DF16
    DF32_off[16:, :16] = DF16
    DF32_off = 0.5 * (DF32_off + DF32_off.conj().T)

    herm = np.max(np.abs(DF32_off - DF32_off.conj().T))
    j_compat = np.max(np.abs(DF32_off @ Xi - Xi @ np.conj(DF32_off)))
    anticomm = np.max(np.abs(DF32_off @ gamma_F + gamma_F @ DF32_off))
    comm = np.max(np.abs(DF32_off @ gamma_F - gamma_F @ DF32_off))

    print(f"\n  {name} (off-diagonal):")
    print(f"    Hermitian: {herm:.2e}")
    print(f"    J-compatible: {j_compat:.2e}")
    print(f"    anticommutes(gamma_F): {anticomm:.2e}")
    print(f"    commutes(gamma_F): {comm:.2e}")


# =============================================================================
# PART 3: ORDER-ONE TEST FOR ALL D_F CANDIDATES x CONNES EMBEDDING
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 3: ORDER-ONE TESTS")
print("=" * 76)

def test_order_one(D_F_32, AF_gens, AF_names_list, AF_factor_list, label):
    n_gens = len(AF_gens)
    max_o1 = 0
    max_pair = None
    n_viol = 0
    o1_by_factor = {}

    for i in range(n_gens):
        Da = D_F_32 @ AF_gens[i] - AF_gens[i] @ D_F_32
        for j in range(n_gens):
            ob = Xi @ AF_gens[j].T @ Xi
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            if err > max_o1:
                max_o1 = err
                max_pair = (AF_names_list[i], AF_names_list[j])
            if err > 1e-6:
                n_viol += 1
            pk = f'[{AF_factor_list[i]}, o({AF_factor_list[j]})]'
            o1_by_factor[pk] = max(o1_by_factor.get(pk, 0), err)

    print(f"\n  [{label}]")
    print(f"    Max ||[[D,a],o(b)]||: {max_o1:.2e}")
    if max_pair:
        print(f"    Worst pair: ({max_pair[0]}, {max_pair[1]})")
    print(f"    Violations: {n_viol}/{n_gens**2}")

    for pk in sorted(o1_by_factor.keys()):
        v = o1_by_factor[pk]
        st = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"    {pk}: {st}")

    return max_o1

# Test each D_F candidate in block-diagonal form
for name, DF16 in DF_candidates.items():
    DF32 = np.zeros((32, 32), dtype=complex)
    DF32[:16, :16] = DF16
    DF32[16:, 16:] = rho_minus(DF16)
    test_order_one(DF32, AF_gens_32, AF_names, AF_factor, f"{name} (block-diag)")

# Test each D_F candidate in off-diagonal form
for name, DF16 in DF_candidates.items():
    DF32 = np.zeros((32, 32), dtype=complex)
    DF32[:16, 16:] = DF16
    DF32[16:, :16] = DF16
    DF32 = 0.5 * (DF32 + DF32.conj().T)
    test_order_one(DF32, AF_gens_32, AF_names, AF_factor, f"{name} (off-diag)")


# =============================================================================
# PART 4: GAUGE COMPATIBILITY CHECK
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 4: CONNES A_F vs BAPTISTA GAUGE ACTIONS")
print("=" * 76)

# Key question: does the Connes A_F embedding commute with R_{u(2)}?
# The Baptista gauge is R_{u(2)}: right su(3) restricted to u(2).
# In the previous phases, R_{u(2)} was the gauge that uniquely gave
# center=5, 3 factors.

basis_u2 = u2_basis_in_su3()
R_matrices = [R_action_matrix(v) for v in basis_u2]

print(f"\n  Testing Connes generators against R_{{u(2)}} gauge (4 generators):")
for i, (gen16, name) in enumerate(zip(AF_gens_16[:6], AF_names[:6])):
    max_comm = 0
    for R_v in R_matrices:
        c = gen16 @ R_v - R_v @ gen16
        max_comm = max(max_comm, np.max(np.abs(c)))
    status = 'PASS' if max_comm < 1e-10 else f'FAIL ({max_comm:.2e})'
    print(f"    [{name}] commutes with R_{{u(2)}}? {status}")

# Also check Baptista L_{u(2)} for comparison
L_matrices_u2 = [L_action_matrix(v) for v in basis_u2]

print(f"\n  Testing Connes generators against L_{{u(2)}} gauge:")
for i, (gen16, name) in enumerate(zip(AF_gens_16[:6], AF_names[:6])):
    max_comm = 0
    for L_v in L_matrices_u2:
        c = gen16 @ L_v - L_v @ gen16
        max_comm = max(max_comm, np.max(np.abs(c)))
    status = 'PASS' if max_comm < 1e-10 else f'FAIL ({max_comm:.2e})'
    print(f"    [{name}] commutes with L_{{u(2)}}? {status}")

# M_3(C) check with R_{su(3)}
basis_su3 = su3_basis()
R_matrices_su3 = [R_action_matrix(v) for v in basis_su3]

print(f"\n  Testing M_3(C) generators against R_{{su(3)}} gauge (8 generators):")
max_m3_comm = 0
for gen16, name in zip(AF_gens_16[6:], AF_names[6:]):
    for R_v in R_matrices_su3:
        c = gen16 @ R_v - R_v @ gen16
        err = np.max(np.abs(c))
        max_m3_comm = max(max_m3_comm, err)
status = 'PASS' if max_m3_comm < 1e-10 else f'FAIL ({max_m3_comm:.2e})'
print(f"    M_3(C) commutes with R_{{su(3)}}? {status}")


# =============================================================================
# PART 5: KEY DIAGNOSTIC -- WHAT BAPTISTA L ACTION ACTUALLY DOES TO CONNES GENERATORS
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 5: BAPTISTA L ACTION vs CONNES LEFT MULTIPLICATION")
print("=" * 76)

# For each u(2) generator v, compute:
#   (a) The Baptista L action: L_action_matrix(v) on C^16
#   (b) The simple left-multiplication: build_bimodule_16(v_4x4, I_4) on C^16
# where v_4x4 is v embedded as a 4x4 matrix acting on the rows.

# First, what is the 4x4 LEFT multiplication matrix for each u(2) generator?
# u(2) in su(3): v = diag(-tr(a), a) for a in u(2)
# Row action of v on 4x4 Psi is: v . Psi (simple left mult)
# In 16x16 language this is build_bimodule_16(v_as_4x4, I_4)

# But wait -- the u(2) generators sit in the 3x3 su(3) matrices,
# and we need to understand how they act on the 4x4 Psi rows.
# The row index of Psi is: row 0 = "a" sector, rows 1-3 = "b,c,D" sectors
# Actually: Psi = [[a, c^T], [b, D]] so:
#   row 0 = (a, c_1, c_2, c_3)
#   row 1 = (b_1, D_11, D_12, D_13)
#   row 2 = (b_2, D_21, D_22, D_23)
#   row 3 = (b_3, D_31, D_32, D_33)

# The Baptista L action from eq 2.62 is NOT simple left multiplication.
# L_v acts differently on each block:
#   L_v(a) = 0
#   L_v(c) = -2*v_11*c
#   L_v(b) = (2*v_11*I+v)*b
#   L_v(D) = v*D

# Compare with simple left mult v . Psi:
#   (v.Psi)_{ij} = sum_k v_{ik} Psi_{kj}
# This would give the same action on D (v*D = left mult) but DIFFERENT on a,c,b.

print("\n  Comparing Baptista L_v with simple left-multiplication v.Psi:")
print(f"  (using u(2) generators in su(3))")

for idx, v in enumerate(basis_u2):
    L_bapt = L_action_matrix(v)

    # Build the 4x4 version of v for left multiplication
    # v is 3x3 in su(3). For the 4x4 Psi, v acts on rows as:
    # The 4 rows of Psi correspond to rows of the block structure [[a,c^T],[b,D]]
    # Row 0 of Psi = first row of [[a,c^T]] = (a, c_1, c_2, c_3)
    # Rows 1-3 of Psi = rows of [[b, D]] = (b_i, D_{i1}, D_{i2}, D_{i3})
    # Simple left mult by v (3x3 on rows 1-3, v_11 on row 0):
    # Actually this doesn't make sense directly because v is 3x3 and Psi is 4x4.
    # The 4x4 matrix has a non-standard structure.

    # Build 4x4 left-mult matrix that would give v*D on the D-block:
    # v acts as 3x3 on the row-index of the 4x4 matrix? No.
    # The 4x4 row index is: 0=singlet, 1-3=triplet.
    # v (3x3, traceless anti-Hermitian) naturally acts on the triplet (rows 1-3).
    # Row 0 (singlet) would get v_11 from the full SU(3) action,
    # but v_11 = -tr(v_{u(2)}) in the su(3) embedding.

    # Let's just compare numerically
    L_simple = np.zeros((16, 16), dtype=complex)
    # v . Psi means: rows of (v . Psi)_{alpha, a} = sum_beta v_{alpha,beta} Psi_{beta,a}
    # But v is 3x3 and alpha runs 0-3.
    # In the (a,b,c,D) basis: a is at position (0,0), so it's a scalar not touched by 3x3 v.
    # This IS the issue -- v acts on the 3-dim space (rows 1-3), not on row 0.

    # Actually, for the SU(3) LEFT action:
    # su(3) acts on the spinor through the (infinitesimal) left regular representation
    # which is eq 2.62. There is NO simple "v . Psi" interpretation because
    # the a,c,b,D blocks transform DIFFERENTLY under L.

    # Print the Baptista action
    print(f"\n  u(2) generator #{idx}:")
    print(f"    v_11 = {v[0,0]:.6f}")

    # Action on each block
    # a (index 0): L_v(a) = sum over col 0 row
    a_row = L_bapt[0, :]
    print(f"    L_v on a-sector (row 0): max = {np.max(np.abs(a_row)):.6e} (should be 0)")

    # c (indices 1-3, 1-col): L_v(c) = -2*v_11*c
    c_block = L_bapt[1:4, 1:4]
    expected_c = -2 * v[0,0] * np.eye(3, dtype=complex)
    print(f"    L_v on c-sector: -2*v_11*c error = {np.max(np.abs(c_block - expected_c)):.6e}")

    # b (indices 4-6): L_v(b) = (2*v_11*I+v)*b
    b_block = L_bapt[4:7, 4:7]
    expected_b = 2 * v[0,0] * np.eye(3, dtype=complex) + v
    print(f"    L_v on b-sector: (2v_11*I+v)*b error = {np.max(np.abs(b_block - expected_b)):.6e}")

    # D (indices 7-15): L_v(D) = v*D
    # This IS simple left multiplication by v on the row-index of D
    D_block = L_bapt[7:16, 7:16]  # 9x9 matrix
    # v*D in flattened form: (v*D)_{ij} = sum_k v_{ik}*D_{kj}
    # Flattened index 3*i+j maps to 3*k+j via v[i,k]
    expected_D = np.zeros((9, 9), dtype=complex)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                expected_D[3*i+j, 3*k+j] = v[i, k]
    print(f"    L_v on D-sector: v*D error = {np.max(np.abs(D_block - expected_D)):.6e}")


# =============================================================================
# PART 6: SUMMARY
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 6: SUMMARY")
print("=" * 76)

print("""
KEY FINDINGS:

1. The Connes standard A_F embedding uses:
   C: lambda -> diag(lambda, lambda_bar, 1, 1)
   H: q -> diag(1, 1, q_{2x2})
   M_3(C): m -> R = diag(1, m^dag)

2. This is tested against BOTH Baptista and Connes-type D_F.

3. The Baptista L action from eq 2.62 is NOT simple left-multiplication.
   It has v_11 anomalous terms on the c and b sectors.
   This is the GAUGE action, not the A_F bimodule action.

4. The A_F bimodule action (pi: A_F -> End(H_F)) is:
   pi(lambda, q, m): Psi -> diag(lambda, lambda_bar, q) . Psi . diag(1, m^dag)
   This IS simple left-right multiplication (build_bimodule_16 is correct).

5. The previous Session 11 scripts used BAPTISTA-inspired generators
   (C_Im = diag(i,1,1,1), H_i = diag(i,-i,i,-i)) which are NOT the
   Connes standard embedding. This script uses the CORRECT Connes embedding.
""")
