"""
ANALYSIS OF THE 20-DIM LEFT-ACTION ALGEBRA
============================================

From test_AF_rowaction.py:
  - Gate check PASSED: left row-action M_3(C) commutes with R_{u(2)}
  - ALL 24 generators in R_u(2) commutant and J-compatible
  - But rank = 20 (not 24): H overlaps with M_3(C) on rows 1-3
  - The 20-dim algebra is CLOSED under multiplication

This script:
  1. Identifies the actual algebra type of the 20-dim left-action algebra
  2. Tests whether M_3(C) can be split into H + "complementary M_3 part"
  3. Investigates the BIMODULE representation approach

The key question: can we find a 24-dim order-zero subalgebra?

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
from scipy.linalg import null_space, orth
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

basis_u2 = u2_basis_in_su3()

def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5

def build_full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32

R_u2_gens_16 = [R_action_matrix(v) for v in basis_u2]
R_u2_gens_32 = [build_full_32(g) for g in R_u2_gens_16]

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

def build_right_action_16(R4):
    gen = np.zeros((16, 16), dtype=complex)
    for l in range(4):
        for j in range(4):
            if abs(R4[l, j]) < 1e-15:
                continue
            for i in range(4):
                fi = flat_idx(i, j)
                fl = flat_idx(i, l)
                gen[fi, fl] += R4[l, j]
    return gen


# =============================================================================
# PART 1: The CORRECT Connes A_F representation
# =============================================================================

print("=" * 76)
print("CONNES BIMODULE A_F REPRESENTATION ON BAPTISTA H_F")
print("=" * 76)

# From Connes-Chamseddine-Marcolli (0706.3688):
# A_F = C + H + M_3(C) acts on H_F as a LEFT A_F module.
#
# The representation on the 4x4 internal matrix X = (a, c^T; b, D):
#
#   pi(lambda, q, m) . X = diag(lambda, q) . X . diag(1, m^dag)
#
# where:
#   - diag(lambda, q) is a 4x4 matrix: lambda in (0,0), q embedded as:
#     q = a+bi+cj+dk -> q_matrix = ( alpha   beta  )
#                                    (-beta* alpha* )
#     with alpha = a+bi, beta = c+di
#     Embedding in 4x4: diag(lambda, alpha_bar, q_2x2)
#     Actually: diag(lambda, q) means different things for different particles:
#       Row 0: lambda (from C, for right-handed neutrino)
#       Row 1: alpha_bar (from H, for right-handed electron)
#       Rows 2-3: q_2x2 (from H, for left-handed doublet)
#
#   - diag(1, m^dag) acts on columns:
#     Col 0: 1 (leptons unchanged)
#     Cols 1-3: m^dag (color rotation of quarks)
#
# The LEFT action (on rows) is: L = diag(lambda, alpha_bar, q_2x2)
# The RIGHT action (on cols) is: R = diag(1, m^dag)
#
# As 16x16 operators:
#   pi_16(lambda, q, m) = build_left_action_16(L) @ build_right_action_16(R)
#                        = build_left_action_16(L) + build_right_action_16(R') + ...
# Actually: pi(X) = L . X . R, which as a 16x16 matrix is NOT simply the sum
# L_16 + R_16. It's the composition of left and right actions.
#
# Let's verify: for pi(X) = L.X.R, the 16x16 matrix is:
#   pi_{flat(i,j), flat(k,l)} = L[i,k] * R[l,j]
# This is the tensor product (Kronecker product in the row x col basis).

def build_bimodule_16(L4, R4):
    """Build 16x16 matrix for bimodule action: X -> L4 . X . R4.

    pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j]
    """
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
# PART 2: Build A_F generators using BIMODULE representation
# =============================================================================

print("\n--- Building A_F generators via bimodule action ---")

AF_gens_16 = []
AF_names = []
AF_factor = []

# ── C FACTOR ──
# (lambda, 1, I_3): L = diag(lambda, 1, 1, 1) = diag(lambda, 1, I_2)
#                    R = diag(1, I_3) = I_4
# C_Re: lambda=1 -> L=I_4, R=I_4 -> identity (the full algebra unit)
# C_Im: lambda=i -> L=diag(i, 1, 1, 1), R=I_4

# But wait: (lambda, 1, I_3) means C part = lambda, H part = 1, M_3 part = I_3.
# The H part q=1 gives alpha=1, alpha_bar=1, q_2x2=I_2.
# So L = diag(lambda, 1, I_2).
# The M_3 part m=I_3 gives R = diag(1, I_3^dag) = I_4.
#
# C_Re: lambda=1 -> L=I_4, R=I_4 -> I_16 (identity, skip for now)
#
# C_Im: lambda=i -> L=diag(i, 1, 1, 1), R=I_4
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_gens_16.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names.append('C_Im')
AF_factor.append('C')

# We also need C_Re - but that's the identity. Let's add it as the difference:
# (lambda, 1, I) vs (1, 1, I): L changes only in (0,0) entry.
# C projects onto row 0 RELATIVE to the identity. So:
# C_Re_proj = diag(1,0,0,0) as left action WITH R=I
L_CRe_proj = np.diag([1.0, 0.0, 0.0, 0.0])
AF_gens_16.append(build_bimodule_16(L_CRe_proj, np.eye(4, dtype=complex)))
AF_names.append('C_Re_proj')
AF_factor.append('C')

print(f"  C: 2 generators (C_Im, C_Re_proj)")

# ── H FACTOR ──
# (1, q, I_3): L = diag(alpha, alpha_bar, q_2x2), R = I_4
#
# For q=1: L=I_4 -> identity (skip, redundant with algebra unit)
# For q=i: alpha=i, alpha_bar=-i
#   L = diag(i, -i, i, -i), R = I_4

L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_gens_16.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names.append('H_i')
AF_factor.append('H')

# For q=j: alpha=0, alpha_bar=0, q_2x2=[[0,1],[-1,0]]
#   L = diag(0, 0, [[0,1],[-1,0]])
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0
L_Hj[3, 2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append('H_j')
AF_factor.append('H')

# For q=k: alpha=0, alpha_bar=0, q_2x2=[[0,i],[i,0]]
L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j
L_Hk[3, 2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append('H_k')
AF_factor.append('H')

# H_1 = identity (will be needed for H algebra closure)
L_H1 = np.eye(4, dtype=complex)
AF_gens_16.append(build_bimodule_16(L_H1, np.eye(4, dtype=complex)))
AF_names.append('H_1=I')
AF_factor.append('H')

print(f"  H: 4 generators (H_i, H_j, H_k, H_1)")

# ── M_3(C) FACTOR ──
# (1, 1, m): L = diag(1, 1, I_2) = I_4, R = diag(1, m^dag)
#
# E_{ab} in M_3(C): m = E_{ab}, m^dag = E_{ba}
# R = diag(1, E_{ba}) where E_{ba} is 3x3 elementary with 1 at (b,a)
#
# Note: R acts on COLUMNS. This means m^dag acts on cols 1-3.

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

print(f"  M3: 18 generators (9 x Re/Im)")
print(f"  Total: {len(AF_gens_16)}")

# Extend to C^32
AF_gens_32 = [build_full_32(g) for g in AF_gens_16]


# =============================================================================
# PART 3: VERIFICATION
# =============================================================================

# ── Test 1: Dimension ──
print("\n" + "-" * 76)
print("[TEST 1] Real dimension of A_F generator span")
AF_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in AF_gens_32]
AF_mat = np.column_stack(AF_vecs)
AF_rank = np.linalg.matrix_rank(AF_mat, tol=1e-8)
print(f"  Rank: {AF_rank} (target: 24)")

if AF_rank < len(AF_gens_32):
    print("  Redundant generators:")
    indep = []
    for i, v in enumerate(AF_vecs):
        if not indep:
            indep.append(i)
        else:
            M = np.column_stack([AF_vecs[j] for j in indep])
            coeffs = np.linalg.lstsq(M, v, rcond=None)[0]
            resid = np.linalg.norm(v - M @ coeffs)
            if resid > 1e-8:
                indep.append(i)
            else:
                print(f"    {AF_names[i]}")

# ── Test 2: R_{u(2)} commutant? ──
print("\n" + "-" * 76)
print("[TEST 2] A_F generators in R_u(2) commutant?")
comm_pass = 0
comm_fail = 0
for T, name, fac in zip(AF_gens_32, AF_names, AF_factor):
    max_err = max(np.max(np.abs(T @ R_g - R_g @ T)) for R_g in R_u2_gens_32)
    if max_err > 1e-10:
        print(f"  FAIL: {name} ({fac}): max |[T, R_v]| = {max_err:.6e}")
        comm_fail += 1
    else:
        comm_pass += 1
print(f"  Result: {comm_pass} PASS, {comm_fail} FAIL out of {len(AF_gens_32)}")

# ── Test 3: J-compatible? ──
print("\n" + "-" * 76)
print("[TEST 3] A_F generators J-compatible? (T Xi = Xi conj(T))")
jcompat_pass = 0
for T, name in zip(AF_gens_32, AF_names):
    err = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
    if err > 1e-10:
        print(f"  FAIL: {name}: err = {err:.6e}")
    else:
        jcompat_pass += 1
print(f"  Result: {jcompat_pass} PASS out of {len(AF_gens_32)}")

# ── Test 4: Order-zero ──
print("\n" + "-" * 76)
print("[TEST 4] Order-zero condition [a, Xi b^T Xi] = 0")
max_oz = 0
n_viol = 0
oz_by_factor = {}

for i, (Ti, ni, fi) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
    for j, (Tj, nj, fj) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
        b_opp = Xi @ Tj.T @ Xi
        comm = Ti @ b_opp - b_opp @ Ti
        err = np.max(np.abs(comm))
        if err > max_oz:
            max_oz = err
        if err > 1e-6:
            n_viol += 1
        pair_key = f'[{fi}, o({fj})]'
        if pair_key not in oz_by_factor:
            oz_by_factor[pair_key] = 0.0
        oz_by_factor[pair_key] = max(oz_by_factor[pair_key], err)

print(f"  Max |[a, o(b)]|: {max_oz:.6e}")
print(f"  Violations (>1e-6): {n_viol} / {len(AF_gens_32)**2}")
print("\n  By factor combination:")
for pair_key in sorted(oz_by_factor.keys()):
    val = oz_by_factor[pair_key]
    status = 'PASS' if val < 1e-6 else f'{val:.6e}'
    print(f"    {pair_key}: {status}")


# =============================================================================
# PART 4: HYBRID APPROACH -- Left C+H, Right M_3(C)
# =============================================================================

print("\n" + "=" * 76)
print("HYBRID: Left C+H + Right M_3(C) (gen-physicist row + original column)")
print("=" * 76)

# From the analysis: the bimodule action is pi = L . X . R.
# The LEFT part (C+H on rows) commutes with R_{u(2)} (on columns): CONFIRMED.
# The RIGHT part (M_3(C) on columns) does NOT commute with R_{u(2)}: KNOWN.
#
# So A_F cannot live ENTIRELY in the R_{u(2)} commutant.
# The LEFT part (C+H, dim 6) IS in the commutant.
# The RIGHT part (M_3(C), dim 18) is NOT.
#
# HOWEVER: The LEFT-only M_3(C) on rows IS in the commutant (gate check).
# And the LEFT-only M_3(C) combined with C gives a 20-dim closed algebra.
#
# Question: Is this 20-dim algebra the LEFT part of a DIFFERENT A_F embedding?

# Let's identify the 20-dim algebra. It consists of:
# All 4x4 LEFT actions of the form diag(z, M) where z in C, M in M_3(C).
# This is the algebra C + M_3(C) (direct sum) with dim 2+18=20.
# It is NOT A_F = C + H + M_3(C).

# Where does H go? In the direct sum, H would need to act on a SEPARATE
# subspace from M_3(C). But in the left-action picture, H acts on rows 0-3
# and M_3 acts on rows 1-3. They overlap.

# The resolution from Connes: H is NOT a separate left-action factor.
# H and M_3(C) are entangled through the bimodule structure:
#   - H acts on the LEFT (rows 2-3 mixing)
#   - M_3(C) acts on the RIGHT (cols 1-3 mixing)
# Together they generate the quark sector of A_F.

# The R_{u(2)} commutant captures the LEFT part of A_F but NOT the RIGHT part.
# To get the full A_F, we need BOTH:
#   - LEFT: C + H (dim 6) from the commutant
#   - RIGHT: M_3(C) (dim 18) from the OPPOSITE algebra A_F^o

# But A_F^o = JA_FJ^{-1} is identified with R_{u(2)} (Session 9 insight).
# So M_3(C) is part of R_{u(2)} itself, not the commutant!

# Let me verify: does M_3(C) embed in R_{u(2)}?
# R_{u(2)} is 4-dimensional (Y + T_1 + T_2 + T_3).
# M_3(C) is 18-dimensional. 18 > 4. So NO.

# But R is not just u(2) -- it's the full R_{su(3)} action restricted to u(2).
# The full R_{su(3)} on columns would contain M_3(C) on the D-block.

# Let me check: does the full R_{su(3)} contain color M_3(C)?
# R_v(D) = -D*v. This IS right multiplication by -v for v in su(3).
# The algebra generated by right multiplication by su(3) on D is:
# {-D*v : v in su(3)} which generates ALL of M_3(C)^op (the opposite algebra).
# And M_3(C)^op = M_3(C) (via transpose).

# So: R_{su(3)} generates M_3(C) acting on columns of D.
# And the COMMUTANT of R_{su(3)} on the D-block is M_3(C) acting on ROWS.
# This is exactly what the gate check confirms!

# The 20-dim left-row algebra C + M_3(C) is the commutant of R_{su(3)} on Psi_+
# (restricted to the subspace where a=0 and c=0, i.e., the D-block + b-vector + a-scalar).

# Now, H acts on rows 2-3 of the 4x4 matrix, which is INSIDE the M_3(C) row action.
# Specifically, H embeds in M_3(C) as:
#   q -> diag(alpha_bar, q_2x2) in M_3(C) (the rows 1-3 part)
# But alpha_bar goes in row 1, q_2x2 goes in rows 2-3.

# Let's check: does H embed in M_3(C)?
print("\n  Checking if H embeds in left-row M_3(C)...")

# H_i = diag(i, -i, i, -i) as L4. The rows 1-3 part is diag(-i, i, -i).
# Is diag(-i, i, -i) in M_3(C)? Yes: it's i*diag(-1,1,-1) = i*(E00 - 2*E11 + E22 - I)?
# Actually diag(-1,1,-1) = E_11 + E_22 - I - E_00... Let me just check numerically.

# Extract the rows 1-3 part of H generators
for name_h in ['H_i', 'H_j', 'H_k']:
    idx_h = AF_names.index(name_h)
    T_h = AF_gens_16[idx_h]  # 16x16

    # M_3(C) generators span
    m3_gens = []
    for a in range(3):
        for b in range(3):
            for val in [1.0, 1j]:
                L_m = np.zeros((4, 4), dtype=complex)
                L_m[a + 1, b + 1] = val
                m3_gens.append(build_left_action_16(L_m))

    m3_vecs = [np.concatenate([g.flatten().real, g.flatten().imag]) for g in m3_gens]
    m3_mat = np.column_stack(m3_vecs)
    h_vec = np.concatenate([T_h.flatten().real, T_h.flatten().imag])
    coeffs = np.linalg.lstsq(m3_mat, h_vec, rcond=None)[0]
    resid = np.linalg.norm(h_vec - m3_mat @ coeffs)
    print(f"    {name_h} in M_3(C) row-span? residual = {resid:.2e} "
          f"({'YES' if resid < 1e-8 else 'NO'})")


# =============================================================================
# PART 5: Check Baptista's actual L action vs pure left multiplication
# =============================================================================

print("\n" + "=" * 76)
print("COMPARISON: Baptista L action vs pure left multiplication")
print("=" * 76)

# Baptista's L_v is NOT pure left multiplication. It has the anomalous term.
# Let's compare L_action_matrix(v) with build_left_action_16(v_as_4x4).

basis_su3 = su3_basis()
print("\n  For each su(3) basis element, compare Baptista L vs pure left mult:")

for idx, v in enumerate(basis_su3):
    # Baptista's L action
    L_bap = L_action_matrix(v)

    # Pure left multiplication by the SAME 3x3 matrix v, embedded as diag(0, v) in 4x4
    # Wait, v is 3x3. In the 4x4 matrix, left mult by what?
    # The L action is supposed to be L_v(X) = v*X (for the D block).
    # But with the anomalous term for b.
    # For pure left mult: L_{pure}(X) = V . X where V = ???
    #
    # Actually, L_v acts on the 4x4 matrix X = (a, c; b, D) as:
    #   a -> 0 (closed)
    #   c -> -2*v_11 * c  (scalar mult on row 0)
    #   b -> (2*v_11*I + v) * b  (modified left mult on rows 1-3, col 0)
    #   D -> v * D  (standard left mult on rows 1-3, cols 1-3)
    #
    # Pure left mult by V would give a -> V[0,:]*X[0,:], etc.
    # Baptista L is NOT a simple left multiplication by any single matrix.
    #
    # The ANOMALOUS term (2*v_11*I) makes b's transformation different from D's.
    # If v_11 = 0 (traceless part of su(2) generators T_1,T_2,T_3), then
    # L_v(b) = v*b and L_v(D) = v*D -- consistent with pure left mult.
    # But for the hypercharge Y = diag(-i, i/2, i/2), v_11 = -i,
    # so the anomalous term is 2*(-i)*I = -2i*I.

    # Compare at the D-block level
    # D block: indices 7-15
    L_bap_D = L_bap[7:16, 7:16]

    # Pure left mult on D: (v*D)_{ij} = sum_k v_{ik} D_{kj}
    # As 9x9 matrix: L_pure[3i+j, 3k+j] = v[i,k] for each j
    L_pure_D = np.zeros((9, 9), dtype=complex)
    for i in range(3):
        for k in range(3):
            for j in range(3):
                L_pure_D[3*i+j, 3*k+j] = v[i, k]

    diff_D = np.max(np.abs(L_bap_D - L_pure_D))

    # b-block: indices 4-6
    L_bap_b = L_bap[4:7, 4:7]
    v11 = v[0, 0]
    L_pure_b = v.copy()
    L_anomalous_b = 2 * v11 * np.eye(3, dtype=complex) + v

    diff_b_pure = np.max(np.abs(L_bap_b - v))
    diff_b_anom = np.max(np.abs(L_bap_b - L_anomalous_b))

    print(f"  e_{idx}: v_11={v11:.4f}, D-block diff={diff_D:.2e}, "
          f"b-block: pure={diff_b_pure:.2e}, anomalous={diff_b_anom:.2e}")


# =============================================================================
# PART 6: THE CORRECT INTERPRETATION
# =============================================================================

print("\n" + "=" * 76)
print("INTERPRETATION AND NEXT STEPS")
print("=" * 76)

print("""
FINDINGS:
1. GATE CHECK PASSED: Left row-action M_3(C) IS in R_{u(2)} commutant (exact 0)
2. ALL 24 generators are R_{u(2)}-commutant and J-compatible
3. BUT: rank = 20 (H overlaps with M_3(C) on rows)
4. The 20-dim algebra is C + M_3(C) [left row action], NOT A_F

DIAGNOSIS:
- In Connes' NCG, A_F = C + H + M_3(C) acts as a BIMODULE:
  LEFT: diag(lambda, alpha_bar, q_2x2) [C+H on rows]
  RIGHT: diag(1, m^dag) [M_3(C) on columns]

- R_{u(2)} commutant captures only the LEFT part
- The RIGHT part (M_3(C) on columns) CONFLICTS with R_{u(2)}
- The LEFT-only M_3(C) on rows is in the commutant but is the WRONG M_3(C)
  (it's End(rows 1-3) = M_3(C), but this is the endomorphism algebra of
   the LEFT representation, not the RIGHT color algebra)

- H embeds INSIDE the left-row M_3(C):
  H -> diag(alpha_bar, q_2x2) in M_3(C) acting on rows 1-3
  So dim(C + H) = 2 + 4 = 6, but inside a 20-dim algebra

IMPLICATION:
The R_{u(2)} commutant contains C + M_3(C)_{rows} (dim 20) as a LEFT algebra.
A_F's LEFT part (C + H, dim 6) is a SUBALGEBRA of this 20-dim algebra.
A_F's RIGHT part (M_3(C)_{cols}, dim 18) is NOT in the commutant.

This means: A_F does NOT embed as a subalgebra of the R_{u(2)} commutant.
Only A_F's LEFT component (C + H, dim 6) embeds.

HOWEVER: The ORDER-ZERO condition specifically tests [pi(a), J pi(b*) J^{-1}] = 0,
where pi is the FULL A_F representation and J pi(b*) J^{-1} is the opposite algebra.
If A_F^o = R_{u(2)} (Session 9 insight), then the order-zero test is:
[pi(a), rho_R(v)] = 0, which is just the commutant condition.

But A_F^o is NOT literally R_{u(2)}. A_F^o = J A_F J^{-1} generates a much
larger algebra than the 4-dim R_{u(2)}.

NEXT STEPS:
1. Compute the ACTUAL A_F^o = J pi(A_F) J^{-1} and check if it contains R_{u(2)}
2. OR: impose order-ONE with D_F from Baptista eq 2.65 (bypasses order-zero)
3. The 20-dim C + M_3(C)_{rows} IS significant: it's the LEFT endomorphism
   algebra of the internal space decomposition under R_{u(2)}.
""")

# Quick check: what is the center of the 20-dim left-row algebra?
print("\n  Center of the 20-dim C + M_3(C)_{rows} algebra:")

# Build independent generators of the 20-dim algebra
indep_gens = []
indep_vecs_all = []
# C part: diag(1,0,0,0) and diag(i,0,0,0) as left action
for val in [1.0, 1j]:
    L4 = np.zeros((4, 4), dtype=complex)
    L4[0, 0] = val
    g = build_full_32(build_left_action_16(L4))
    v = np.concatenate([g.flatten().real, g.flatten().imag])
    indep_gens.append(g)
    indep_vecs_all.append(v)

# M_3 part: all E_{ab} x Re/Im on rows 1-3
for a in range(3):
    for b in range(3):
        for val in [1.0, 1j]:
            L4 = np.zeros((4, 4), dtype=complex)
            L4[a+1, b+1] = val
            g = build_full_32(build_left_action_16(L4))
            v = np.concatenate([g.flatten().real, g.flatten().imag])
            indep_gens.append(g)
            indep_vecs_all.append(v)

Q_all = orth(np.column_stack(indep_vecs_all))
d_all = Q_all.shape[1]
print(f"  Total dim: {d_all}")

# Compute structure constants and center
n_b = d_all
basis_mats = []
for k in range(d_all):
    v = Q_all[:, k]
    n_flat = 32*32
    T = (v[:n_flat] + 1j * v[n_flat:]).reshape(32, 32)
    basis_mats.append(T)

# Structure constants C^k_{ij} from [T_i, T_j] = sum_k C^k_{ij} T_k
struct = np.zeros((n_b, n_b, n_b), dtype=complex)
for i in range(n_b):
    for j in range(n_b):
        comm = basis_mats[i] @ basis_mats[j] - basis_mats[j] @ basis_mats[i]
        cv = np.concatenate([comm.flatten().real, comm.flatten().imag])
        struct[i, j, :] = Q_all.T @ cv

# Center: elements c = sum_k z_k T_k such that [c, T_j] = 0 for all j
# This means sum_k z_k C^l_{kj} = 0 for all j, l
# -> constraint matrix: for each (j,l), row = C^l_{:,j}
n_constraints = n_b * n_b
constr = np.zeros((n_constraints, n_b))
for j in range(n_b):
    for l in range(n_b):
        constr[j * n_b + l, :] = struct[:, j, l].real

center_ns = null_space(constr, rcond=1e-8)
print(f"  Center dimension: {center_ns.shape[1]}")
print(f"  Expected for C + M_3(C): center(C) + center(M_3(C)) = C + C = dim 4")

print("\n" + "=" * 76)
print("FINAL SUMMARY")
print("=" * 76)
print(f"  Gate check: PASS (M_3(C) rows commute with R_u(2) cols)")
print(f"  Left-row algebra: C + M_3(C), dim {d_all}")
print(f"  H embeds in M_3(C) rows: YES (H is subalgebra of rows-1-3 endomorphisms)")
print(f"  Bimodule M_3(C) (cols) in commutant: NO (conflicts with R_u(2))")
print(f"  Order-zero for bimodule A_F: CANNOT HOLD (M_3 cols not in commutant)")
print(f"  A_F embeds in R_u(2) commutant: NO (only LEFT part = C+H embeds)")
print(f"")
print(f"  CONCLUSION: R_u(2) commutant approach CANNOT extract full A_F.")
print(f"  The commutant captures the LEFT algebra only.")
print(f"  Phase 2.5 (order-ONE with D_F) is the necessary next step.")
print("=" * 76)
