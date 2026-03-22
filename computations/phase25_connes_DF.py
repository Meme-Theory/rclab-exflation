"""
PHASE 2.5 CONNES D_F: Test order-one with Connes-type Dirac operator
=====================================================================

Key finding from phase25_dirac_structure.py:
  Our D_F maps Psi(0,j) <-> Psi(j,0) -- changes BOTH row and column.
  This is a MIXED L*R operator that CANNOT satisfy order-one with bimodule A_F.

Connes' D_F instead couples:
  up-type ROW to down-type ROW (same column) = PURE LEFT operator
  D_F = sum_j Y_j * E_{0,j}^{row} + h.c. (acting on rows only)

This script:
1. Constructs Connes-type D_F (pure left, row mixing)
2. Tests order-one for bimodule A_F
3. If order-one passes, identifies the physical interpretation in Baptista's framework

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

def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5


# =============================================================================
# CONNES-TYPE D_F: Pure LEFT operator coupling row 0 to rows 1,2,3
# =============================================================================
print("=" * 76)
print("CONNES-TYPE D_F: Pure LEFT operator")
print("=" * 76)

# D_F^{Connes} on Psi_+ acts as: Psi -> D_L . Psi where D_L is a 4x4 matrix
# D_L couples row 0 (up-type: nu, u_R) to rows 1-3 (down-type: e, d_R etc.)
# With identity Yukawa: D_L = sum_j (E_{0j} + E_{j0}) for j=1,2,3

D_L = np.zeros((4, 4), dtype=complex)
for j in range(1, 4):
    D_L[0, j] = 1.0  # row 0 -> row j
    D_L[j, 0] = 1.0  # row j -> row 0

print(f"\nD_L (4x4 Yukawa matrix):")
print(D_L.real)

# D_F on Psi_+ as 16x16: this is build_bimodule_16(D_L, I)
D_F_connes_16 = build_bimodule_16(D_L, np.eye(4, dtype=complex))

print(f"\nD_F_connes nonzero entries (16x16):")
count = 0
for r in range(16):
    for c in range(16):
        if abs(D_F_connes_16[r, c]) > 1e-10:
            for i in range(4):
                for j in range(4):
                    if flat_idx(i, j) == r: ri, rj = i, j
                    if flat_idx(i, j) == c: ci, cj = i, j
            print(f"  [{r:2d},{c:2d}] = {D_F_connes_16[r,c]:+.1f}   Psi({ri},{rj}) -> Psi({ci},{cj})")
            count += 1
print(f"  ({count} nonzero entries)")

# Verify: D_F_connes is a pure LEFT operator
is_left = True
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                fi = flat_idx(i, j)
                fk = flat_idx(k, l)
                val = D_F_connes_16[fi, fk]
                if abs(val) > 1e-10 and l != j:
                    is_left = False
print(f"\nD_F_connes is pure LEFT: {is_left}")


# =============================================================================
# Build A_F generators
# =============================================================================
AF_16_list = []
AF_16_names = []
AF_16_factors = []

# C factor: lambda * I on row 0 (lepton number)
L_CIm = np.diag([1j, 0.0, 0.0, 0.0])  # lambda = i, acting on row 0 ONLY
# Wait -- in Connes, C acts as lambda on the ENTIRE doublet space, not just row 0.
# C = lambda * diag(1, 1, 1, 1)? No.
# In Connes' A_F = C + H + M_3(C):
#   C acts as lambda . I_2 on leptons (SU(3) singlet, column 0)
#   H acts as q_{2x2} on doublet rows (row 0/j pairs)
#   M_3(C) acts on color columns (1,2,3)

# Actually, the PRECISE Connes action for one generation on Psi_{4x4} is:
# pi(lambda, q, m) . Psi = [[lambda, 0], [0, q]] . Psi . [[1, 0], [0, m^dag]]
#   where lambda in C, q in H (embedded as 2x2), m in M_3(C)
#   Left matrix: diag(lambda, lambda) for lepton, diag(alpha, alpha_bar) for quark
#   ... Actually the precise conventions matter enormously here.

# From our test_AF_rowaction2.py result, the VERIFIED bimodule generators are:
# C: L = diag(lambda, lambda, lambda, lambda) restricted to column 0
# Wait, let me re-read what worked.

# In the BIMODULE representation from test_AF_rowaction2.py:
# pi(lambda, q, m).X = diag(lambda, alpha_bar, q_{2x2}) . X . diag(1, m^dag)
# where alpha = Re(lambda) and alpha_bar is its conjugate...

# Actually, let me just use the same generators from the previous scripts.
# The issue is clear: with a LEFT-only D_F, the order-one condition is
# AUTOMATICALLY satisfied for any right-acting generators (M_3(C)).
# The question is whether it holds for the LEFT-acting part (C and H).

# Let's just use the generators we had and test directly.

# C factor
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_16_list.append(build_bimodule_16(L_CIm, np.eye(4))); AF_16_names.append('C_Im'); AF_16_factors.append('C')
L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
AF_16_list.append(build_bimodule_16(L_CRe, np.eye(4))); AF_16_names.append('C_Re_proj'); AF_16_factors.append('C')

# H factor
L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_16_list.append(build_bimodule_16(L_Hi, np.eye(4))); AF_16_names.append('H_i'); AF_16_factors.append('H')
L_Hj = np.zeros((4, 4), dtype=complex); L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_16_list.append(build_bimodule_16(L_Hj, np.eye(4))); AF_16_names.append('H_j'); AF_16_factors.append('H')
L_Hk = np.zeros((4, 4), dtype=complex); L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_16_list.append(build_bimodule_16(L_Hk, np.eye(4))); AF_16_names.append('H_k'); AF_16_factors.append('H')
AF_16_list.append(build_bimodule_16(np.eye(4), np.eye(4))); AF_16_names.append('H_1'); AF_16_factors.append('H')

# M_3(C) factor (right action)
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_elem.conj().T
            AF_16_list.append(build_bimodule_16(np.eye(4), R_m))
            AF_16_names.append(f'M3_E{a}{b}_{part}'); AF_16_factors.append('M3')


# =============================================================================
# TEST 1: Order-one with Connes-type D_F (LEFT-only)
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 1: Order-one with Connes-type D_F (pure LEFT)")
print(f"{'=' * 76}")

max_o1 = 0
o1_by_factor = {}
worst_pair = None

for i in range(len(AF_16_list)):
    Da = D_F_connes_16 @ AF_16_list[i] - AF_16_list[i] @ D_F_connes_16
    for j in range(len(AF_16_list)):
        ob = AF_16_list[j].conj().T  # o(b)_++ = b^dag
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        if err > max_o1:
            max_o1 = err
            worst_pair = (AF_16_names[i], AF_16_names[j])
        pk = f'[{AF_16_factors[i]}, o({AF_16_factors[j]})]'
        if pk not in o1_by_factor:
            o1_by_factor[pk] = 0.0
        o1_by_factor[pk] = max(o1_by_factor[pk], err)

print(f"\nMax |[[D_F_connes, a], b^dag]| on Psi_+: {max_o1:.2e}")
if worst_pair:
    print(f"Worst pair: {worst_pair}")
print(f"\nBy factor:")
for pk in sorted(o1_by_factor.keys()):
    v = o1_by_factor[pk]
    s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
    print(f"  {pk}: {s}")


# =============================================================================
# TEST 2: Which generators commute with D_F_connes?
# =============================================================================
print(f"\n{'=' * 76}")
print("GENERATORS COMMUTING WITH D_F_CONNES")
print(f"{'=' * 76}")

for name, gen, fac in zip(AF_16_names, AF_16_list, AF_16_factors):
    Da = D_F_connes_16 @ gen - gen @ D_F_connes_16
    norm = np.max(np.abs(Da))
    if norm > 1e-10:
        # Check if it's a pure left operator
        is_left = True
        for ii in range(4):
            for jj in range(4):
                for kk in range(4):
                    for ll in range(4):
                        fi = flat_idx(ii, jj)
                        fk = flat_idx(kk, ll)
                        val = Da[fi, fk]
                        if abs(val) > 1e-10 and ll != jj:
                            is_left = False
        left_str = "LEFT" if is_left else "MIXED"
        print(f"  {name:15s} ({fac}): |[D_F, a]| = {norm:.4f}, type={left_str}")
    else:
        print(f"  {name:15s} ({fac}): [D_F, a] = 0")


# =============================================================================
# TEST 3: The REAL Connes D_F structure for SM
# =============================================================================
print(f"\n{'=' * 76}")
print("UNDERSTANDING: CONNES D_F FOR THE SM")
print(f"{'=' * 76}")

# In Connes-Chamseddine, the finite Dirac D_F on one generation acts as:
# (For Psi = [nu_R, e_R, nu_L, e_L, u_R, d_R, u_L, d_L] x colors)
#
# D_F = [[0, M^*], [M, 0]] where M encodes Yukawa couplings
# M maps right-handed to left-handed fermions
#
# In the 4x4 matrix representation of Baptista:
# Row 0 = (nu_R-like), Rows 1-3 = (others)
# Column 0 = lepton, Columns 1-3 = quarks
#
# The Connes D_F on Psi_{4x4} acts as:
# (D_F Psi)_{ij} = sum_k Y_{ik} Psi_{kj}
# This is a PURE LEFT multiplication by the Yukawa matrix Y!
# Y_{ij} = Yukawa coupling between row i and row k.

# For the simplest case (one generation, identity Yukawa):
# Y = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# This couples row 0 to rows 1,2,3 symmetrically.

# But this is NOT what the L-homomorphism failure (eq 2.65) gives!
# Eq 2.65 gives c <-> b coupling: position (0,j) <-> (j,0)
# which requires changing BOTH row and column.

# The resolution: eq 2.65 describes the L-HOMOMORPHISM FAILURE,
# not the Dirac operator. The Dirac operator on SU(3) when restricted
# to zero modes gives something different.

# Actually, in Baptista's framework (Paper 16, Section 9):
# ALL particles are null geodesics in 12D.
# The Dirac operator comes from the full 12D geometry.
# Restricted to zero modes on K = SU(3), it gives the MASS MATRIX.
# The mass matrix couples states related by the SAME LEFT generator
# that fails the homomorphism -- but as a ROW operation, not a matrix transposition.

# Let's check: does a LEFT-ONLY D_F coupling row 0 to row j give
# the correct Higgs-like structure?

print("\nConnes D_F = Y otimes I_columns (pure left):")
print(f"  Psi(0,j) -> Psi(k,j) for all j (same column, row mixing)")
print(f"  This preserves color (column) and changes weak isospin (row)")
print(f"  Exactly the Higgs field structure!")

print(f"\nBaptista D_F from eq 2.65 (c<->b = mixed L*R):")
print(f"  Psi(0,j) -> Psi(j,0) (transpose: row and column both change)")
print(f"  This changes BOTH color AND weak isospin")
print(f"  NOT the Higgs field structure!")

print(f"\nConclusion: the L-homomorphism failure (eq 2.65) describes")
print(f"the OBSTRUCTION that generates the Higgs, but is NOT the D_F itself.")
print(f"The actual D_F in Connes' sense would be a LEFT Yukawa matrix")
print(f"that couples rows (up-type to down-type) while preserving columns (color).")


# =============================================================================
# TEST 4: Verify that LEFT D_F + bimodule A_F satisfies order-one ANALYTICALLY
# =============================================================================
print(f"\n{'=' * 76}")
print("ANALYTIC VERIFICATION: LEFT D_F + BIMODULE A_F")
print(f"{'=' * 76}")

# If D_F = D_L otimes I (pure left), then:
# [D_F, pi(a)] where pi(a) = L_a otimes R_a:
# [D_L otimes I, L_a otimes R_a] = [D_L, L_a] otimes R_a   (if D_L and L_a are on same space)
# ... no, that's not quite right because D_L otimes I acts as L_D on rows only,
# while L_a otimes R_a acts on both rows and columns.

# More carefully:
# D_F(X) = D_L . X          (left multiplication by D_L)
# pi(a)(X) = L_a . X . R_a   (bimodule action)
# [D_F, pi(a)](X) = D_L(L_a X R_a) - L_a(D_L X)R_a
#                  = D_L L_a X R_a - L_a D_L X R_a
#                  = [D_L, L_a] X R_a

# Then for o(b)(X) = X . S_b (some right action from the opposite algebra):
# On Psi_+: o(b) = b^dag which can be decomposed as L_b^dag otimes R_b^dag?
# NO! b^dag for a bimodule generator pi(a) with L_a and R_a gives:
# pi(a)^dag(X) = L_a^dag . X . R_a^dag (both parts get daggers)
# So o(b)_++ = b^dag = L_b^dag . (-) . R_b^dag

# Wait, that's the issue. o(b) is the OPPOSITE algebra action.
# For A_F = C + H + M_3(C):
# C and H act LEFT only (R = I), so o(lambda, q, 1) = L_{(lambda,q)}^dag
# M_3(C) acts RIGHT only (L = I), so o(1, 1, m) = R_{m^dag}

# For a LEFT-only generator (C or H): o(b) = L_b^dag
# [D_F, pi(a)] = [D_L, L_a] otimes R_a
# [[D_F, pi(a)], o(b)] = [[D_L, L_a], L_b^dag] otimes R_a
# This is zero iff [[D_L, L_a], L_b^dag] = 0 for all LEFT generators a, b.

# For a RIGHT-only generator (M_3): o(m) = I otimes R_{m^dag}
# [[D_F, pi(a)], o(m)] = [D_L, L_a] otimes [R_a, R_{m^dag}]
# For C and H: R_a = I, so [I, R_{m^dag}] = 0. PASSES AUTOMATICALLY.
# For M_3(C): L_a = I, so [D_L, I] = 0. PASSES TRIVIALLY.

print("\nCase analysis:")
print("  1. [C/H, o(C/H)]: reduces to [[D_L, L_a], L_b^dag] = 0 on 4x4 LEFT space")
print("  2. [C/H, o(M3)]:  = [D_L, L_a] otimes [I, R_m^dag] = 0 (automatic)")
print("  3. [M3, o(C/H)]:  = [D_L, I] otimes [...] = 0 (trivial)")
print("  4. [M3, o(M3)]:   = [D_L, I] otimes [...] = 0 (trivial)")
print("\nSo the ONLY non-trivial condition is:")
print("  [[D_L, L_a], L_b^dag] = 0 for all a, b in C + H (left factors)")

# Test this on the 4x4 LEFT space:
L_gens = [
    (np.diag([1j, 1.0, 1.0, 1.0]), 'C_Im', 'C'),
    (np.diag([1.0, 0.0, 0.0, 0.0]), 'C_Re_proj', 'C'),
    (np.diag([1j, -1j, 1j, -1j]), 'H_i', 'H'),
]
# H_j and H_k
Hj = np.zeros((4, 4), dtype=complex); Hj[2, 3] = 1.0; Hj[3, 2] = -1.0
Hk = np.zeros((4, 4), dtype=complex); Hk[2, 3] = 1j; Hk[3, 2] = 1j
L_gens.append((Hj, 'H_j', 'H'))
L_gens.append((Hk, 'H_k', 'H'))

print(f"\nTesting [[D_L, L_a], L_b^dag] on 4x4 space:")
max_err_4x4 = 0
worst_pair_4x4 = None
for i, (La, na, fa) in enumerate(L_gens):
    Da = D_L @ La - La @ D_L
    for j, (Lb, nb, fb) in enumerate(L_gens):
        Lb_dag = Lb.conj().T
        dc = Da @ Lb_dag - Lb_dag @ Da
        err = np.max(np.abs(dc))
        if err > max_err_4x4:
            max_err_4x4 = err
            worst_pair_4x4 = (na, nb)
        if err > 1e-8:
            print(f"  [[D_L, {na}], {nb}^dag] max = {err:.4f}")

if max_err_4x4 < 1e-8:
    print("  ALL PASS!")
else:
    print(f"\n  Max error: {max_err_4x4:.4f}, worst pair: {worst_pair_4x4}")


# =============================================================================
# TEST 5: What if D_L has generation structure (non-identity Yukawa)?
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST 5: NON-IDENTITY YUKAWA MATRICES")
print(f"{'=' * 76}")

# Physical Yukawa: D_L should have DIFFERENT couplings for each row pair
# D_L = [[0, y_1, y_2, y_3], [y_1*, 0, 0, 0], [y_2*, 0, 0, 0], [y_3*, 0, 0, 0]]
# For SM with 3 colors: y_j are the Yukawa couplings (same for each color)

# Test with random Yukawa:
np.random.seed(42)
y = np.random.randn(3) + 1j * np.random.randn(3)
D_L_yukawa = np.zeros((4, 4), dtype=complex)
for j in range(3):
    D_L_yukawa[0, j+1] = y[j]
    D_L_yukawa[j+1, 0] = y[j].conj()

print(f"Random Yukawa couplings: y = {y}")

max_err_yuk = 0
for i, (La, na, fa) in enumerate(L_gens):
    Da = D_L_yukawa @ La - La @ D_L_yukawa
    for j, (Lb, nb, fb) in enumerate(L_gens):
        Lb_dag = Lb.conj().T
        dc = Da @ Lb_dag - Lb_dag @ Da
        err = np.max(np.abs(dc))
        max_err_yuk = max(max_err_yuk, err)
        if err > 1e-8:
            print(f"  [[D_L, {na}], {nb}^dag] max = {err:.4f}")

if max_err_yuk < 1e-8:
    print("  ALL PASS with random Yukawa!")
else:
    print(f"  Max error with random Yukawa: {max_err_yuk:.4f}")

# Test with arbitrary hermitian D_L (4x4):
D_L_full = np.random.randn(4, 4) + 1j * np.random.randn(4, 4)
D_L_full = D_L_full + D_L_full.conj().T  # hermitian

max_err_full = 0
for i, (La, na, fa) in enumerate(L_gens):
    Da = D_L_full @ La - La @ D_L_full
    for j, (Lb, nb, fb) in enumerate(L_gens):
        Lb_dag = Lb.conj().T
        dc = Da @ Lb_dag - Lb_dag @ Da
        err = np.max(np.abs(dc))
        max_err_full = max(max_err_full, err)

print(f"\nWith arbitrary 4x4 hermitian D_L: max error = {max_err_full:.4f}")

# The question is: for WHICH D_L does [[D_L, L_a], L_b^dag] = 0?
# This is the order-one condition on the LEFT factor algebra C + H.
#
# C + H embeds in M_4(C) as:
#   (lambda, q) -> diag(lambda, ..., q_{2x2 block at rows 2,3})
# Wait, our generators are:
#   C_Im: diag(i, 1, 1, 1) -- NO, this is lambda=i acting as (i, 1, 1, 1)
#   H_i:  diag(i, -i, i, -i)
# These are NOT the standard Connes embedding.

# The standard Connes embedding for one generation:
# A_F = C + H + M_3(C) acts on C^2 (lepton doublet) + C^2 tensor C^3 (quark doublet x color)
# C: lambda -> diag(lambda, lambda_bar) on lepton, diag(lambda, lambda_bar) on quark
# H: q -> q_{2x2} on both leptons and quarks
# M_3(C): m -> I tensor m on quarks, I on leptons

# In the 4x4 MATRIX representation, the embedding is different.
# Let me compute which LEFT algebras L_a satisfy [[D_L, L_a], L_b^dag] = 0
# for D_L = row-coupling Yukawa.

print(f"\n{'=' * 76}")
print("FINDING: ORDER-ONE SUBALGEBRA OF M_4(C) FOR LEFT D_F")
print(f"{'=' * 76}")

# Parametrize D_L as the Yukawa coupling:
# D_L has nonzero entries only in row 0 and column 0 (coupling nu-type to others)
# D_L = [[0, y^T], [y_bar, 0]] where y is a 3-vector

# For any 4x4 matrix A:
# [D_L, A] has entries involving A_{0j} and A_{j0} mixed with y
# [[D_L, A], B^dag] involves second commutator

# The order-one subalgebra consists of all A such that
# [[D_L, A], B^dag] = 0 for all B in the same subalgebra.

# This is exactly the problem Connes solved: the maximal subalgebra of M_4(C)
# satisfying order-one with a rank-3 off-diagonal D_L is C + H (acting on 2+2 block).

# Let me verify: if A = [[a, 0], [0, q_{3x3}]] (block diagonal 1+3):
# [D_L, A] = [[0, y^T], [y_bar, 0]] . [[a, 0], [0, q]] - [[a, 0], [0, q]] . [[0, y^T], [y_bar, 0]]
# = [[0, a*y^T], [q*y_bar, 0]] - [[0, y^T*q], [a*y_bar, 0]]  (where we use y_bar = conj(y))
# Hmm, this requires y^T q vs a y^T... only commutes if a = scalar and q = scalar.
# That gives commutant of D_L within block-diag = C + C. That's dimension 2.

# For order-ONE (not order-zero): [[D_L, A], B^dag] = 0
# This is weaker than [D_L, A] = 0.

# Let me just numerically find the order-one subalgebra for D_L.
# Build constraint matrix: for each pair (i,j) of basis elements e_i, e_j of M_4(C),
# [[D_L, e_i], e_j^dag] should be zero.

print("\nFinding order-one subalgebra of M_4(C) w.r.t. D_L:")

# Basis of M_4(C) as real vector space (32 dimensions):
basis_4x4 = []
basis_names = []
for a in range(4):
    for b in range(4):
        E = np.zeros((4, 4), dtype=complex)
        E[a, b] = 1.0
        basis_4x4.append(E)
        basis_names.append(f'E{a}{b}_Re')
        E2 = np.zeros((4, 4), dtype=complex)
        E2[a, b] = 1j
        basis_4x4.append(E2)
        basis_names.append(f'E{a}{b}_Im')

d = len(basis_4x4)  # 32

# Order-one constraint: for all j, [[D_L, a], e_j^dag] = 0
# This is LINEAR in a. For each j, it gives a set of linear constraints.
# Stack all constraints.

# Use D_L with identity Yukawa for now
constraints = []
for j in range(d):
    ej_dag = basis_4x4[j].conj().T
    # For each basis element e_i as 'a':
    # [[D_L, e_i], e_j^dag] = [D_L e_i - e_i D_L, e_j^dag]
    # = (D_L e_i - e_i D_L) e_j^dag - e_j^dag (D_L e_i - e_i D_L)
    # This is linear in e_i, so we can build the constraint matrix
    for r in range(4):
        for c in range(4):
            # Extract the (r,c) entry of [[D_L, e_i], e_j^dag] as linear function of coefficients
            row = np.zeros(d)
            for i in range(d):
                Di = D_L @ basis_4x4[i] - basis_4x4[i] @ D_L
                dc = Di @ ej_dag - ej_dag @ Di
                row[i] = dc[r, c].real
            if np.max(np.abs(row)) > 1e-14:
                constraints.append(row)

            row_im = np.zeros(d)
            for i in range(d):
                Di = D_L @ basis_4x4[i] - basis_4x4[i] @ D_L
                dc = Di @ ej_dag - ej_dag @ Di
                row_im[i] = dc[r, c].imag
            if np.max(np.abs(row_im)) > 1e-14:
                constraints.append(row_im)

A_cons = np.array(constraints)
print(f"  Constraint matrix: {A_cons.shape[0]} x {A_cons.shape[1]}")

# Find null space
ATA = A_cons.T @ A_cons
eigvals, eigvecs = np.linalg.eigh(ATA)
tol = 1e-8 * np.max(np.abs(eigvals))
null_mask = eigvals < tol
null_space = eigvecs[:, null_mask]

print(f"  Null space dimension: {null_space.shape[1]}")

# Reconstruct the algebra elements
print(f"\n  Order-one subalgebra generators:")
for k in range(null_space.shape[1]):
    v = null_space[:, k]
    A = sum(v[i] * basis_4x4[i] for i in range(d))
    # Clean up
    A[np.abs(A) < 1e-10] = 0
    norm = np.max(np.abs(A))
    if norm > 1e-10:
        A /= norm
        print(f"\n  Generator {k+1}:")
        for r in range(4):
            row_str = "    ["
            for c in range(4):
                if abs(A[r, c].imag) < 1e-10:
                    row_str += f" {A[r,c].real:+.4f}"
                else:
                    row_str += f" {A[r,c]:+.4f}"
            row_str += " ]"
            print(row_str)

# Check if dimension matches C + H = 2 + 4 = 6 (real dimensions)
print(f"\n  Expected for C + H: 2 + 4 = 6 real dimensions")
print(f"  Got: {null_space.shape[1]} real dimensions")
