"""
PHASE 2.5: D_F Construction and Order-One Condition
====================================================

From Baptista eq 2.65, the L-action failure on C^2 directions gives:
  L_{[u,v]} - [L_u, L_v] = ( 0              2[u,v]_11 * c^T )
                             ( -2[u,v]_11 * b    0           )

This is the "Higgs term" -- it couples c (row 0, cols 1-3) with b (rows 1-3, col 0).
The finite Dirac operator D_F encodes this coupling.

In Connes' NCG, D_F is a self-adjoint operator on H_F = C^32 that:
  1. Anticommutes with chirality: {D_F, gamma_F} = 0 (since D_F is off-diagonal in chirality)
  2. Satisfies order-one: [[D_F, a], Jb*J^{-1}] = 0 for all a,b in A_F
  3. Encodes Yukawa couplings (Higgs sector of the SM)

The simplest D_F that captures the Baptista non-homomorphism:

  D_F . Psi_+ = Y . Psi_+ where Y couples c <-> b:
  Y(a, c, b, D) = (0, b^T . y, y^dag . c, 0)  for some 3x3 Yukawa matrix y

On the 4x4 matrix X = (a, c^T; b, D):
  D_F acts as: X -> (0, b^T.y; y^dag.c, 0) = off-diagonal coupling

As a 16x16 matrix, D_F maps:
  c_j (idx 1-3) -> sum_k y^dag_{jk} . b_k (idx 4-6, shifted)
  Wait -- D_F on the 4x4 matrix X = (a,c;b,D) gives:
  (D_F . X)_{0j} = sum_k y_{jk} b_k  [row 0, col j: from b_k]
  (D_F . X)_{i0} = sum_k y^dag_{ik} c_k  [row i, col 0: from c_k]
  All other entries: 0

Actually, for Connes' D_F, we need to be more careful about the precise form.
The Yukawa matrix y is ARBITRARY (it parametrizes the Higgs VEV).

For the ORDER-ONE TEST, the specific value of y doesn't matter -- we need to check
whether [[D_F, a], JbJ^{-1}] = 0 for a GENERIC D_F of the right form.

But first let me construct the SIMPLEST D_F and verify the order-one condition.

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
gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)

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


# =============================================================================
# PART 1: Construct D_F from Baptista eq 2.65
# =============================================================================

print("=" * 76)
print("PHASE 2.5: FINITE DIRAC OPERATOR D_F CONSTRUCTION")
print("=" * 76)

# The non-homomorphism of L on the C^2 directions gives:
#   delta(u,v) = L_{[u,v]} - [L_u, L_v]
#             = ( 0              2[u,v]_11 * c^T )
#               ( -2[u,v]_11 * b    0           )
#
# This couples:
#   c (indices 1-3, row 0 of 4x4) <-> b (indices 4-6, col 0 of 4x4)
#
# The C^2 directions in su(3) are spanned by:
#   e_3 = -i*lambda_4/2, e_4 = -i*lambda_5/2 (connecting row/col 0 and 1 in su(3))
#   e_5 = -i*lambda_6/2, e_6 = -i*lambda_7/2 (connecting row/col 0 and 2 in su(3))
#
# These are the off-diagonal generators connecting the u(2) block {rows 1-2} with
# the "extra" direction {row 0} in su(3).
#
# For Connes' D_F, the Dirac operator on H_F typically has the form:
#   D_F: Psi_+ -> Psi_-  (chirality-changing, maps particles to antiparticles)
#
# But in our setup, D_F acts WITHIN H_F = C^32 as a Hermitian operator that
# anticommutes with gamma_F (chirality).
#
# D_F anticommutes with gamma_F means:
#   D_F is block off-diagonal: D_F = (0, D_+; D_+^dag, 0) in the Psi_+/Psi_- basis
#
# The non-homomorphism delta couples c and b WITHIN Psi_+.
# So the relevant D_F should have components:
#   D_F on Psi_+: off-diagonal coupling c <-> b (within the 16-dim Psi_+ space)
#   D_F on Psi_-: related by J

# Let me construct D_F that captures the Baptista eq 2.65 structure.
# The simplest version: D_F couples c_j <-> b_j (identity Yukawa y = I_3).

print("\n--- Constructing D_F from Baptista non-homomorphism term ---")

# D_F on Psi_+ (16x16): couples c (idx 1-3) <-> b (idx 4-6)
# For Yukawa matrix y = I_3 (identity):
#   D_F . c_j = b_j  (maps c entries to b entries)
#   D_F . b_j = c_j  (maps b entries to c entries)
# Self-adjoint: D_F^dag = D_F

D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    c_idx = j + 1     # c entries are at flat indices 1, 2, 3
    b_idx = j + 4     # b entries are at flat indices 4, 5, 6
    D_F_16[c_idx, b_idx] = 1.0
    D_F_16[b_idx, c_idx] = 1.0

print(f"  D_F_16 shape: {D_F_16.shape}")
print(f"  D_F_16 hermitian: {np.max(np.abs(D_F_16 - D_F_16.conj().T)):.2e}")
print(f"  D_F_16 nonzero entries: {np.count_nonzero(D_F_16)}")

# D_F on C^32:
# Option 1: Block OFF-diagonal (anticommutes with gamma_F):
#   D_F_32 = (0, D_F_16; D_F_16^dag, 0)
# This maps Psi_+ -> Psi_- and Psi_- -> Psi_+.

D_F_32_offdiag = np.zeros((32, 32), dtype=complex)
D_F_32_offdiag[:16, 16:] = D_F_16
D_F_32_offdiag[16:, :16] = D_F_16.conj().T

print(f"\n  D_F_32 (off-diagonal) hermitian: "
      f"{np.max(np.abs(D_F_32_offdiag - D_F_32_offdiag.conj().T)):.2e}")
anticomm = D_F_32_offdiag @ gamma_F + gamma_F @ D_F_32_offdiag
print(f"  {{D_F, gamma_F}} = 0: {np.max(np.abs(anticomm)):.2e}")

# Option 2: Block DIAGONAL (commutes with gamma_F):
#   D_F_32 = diag(D_F_16_plus, D_F_16_minus)
# where D_F_16_minus = G5 conj(D_F_16) G5 (J-compatible extension)

D_F_16_minus = G5 @ np.conj(D_F_16) @ G5
D_F_32_diag = np.zeros((32, 32), dtype=complex)
D_F_32_diag[:16, :16] = D_F_16
D_F_32_diag[16:, 16:] = D_F_16_minus

comm_gamma = D_F_32_diag @ gamma_F - gamma_F @ D_F_32_diag
print(f"\n  D_F_32 (diagonal) commutes with gamma_F: {np.max(np.abs(comm_gamma)):.2e}")

# In standard NCG, D_F anticommutes with gamma (off-diagonal in chirality).
# But D_F can also have a diagonal part if it commutes with gamma.
# The Baptista non-homomorphism acts WITHIN Psi_+, so it should be diagonal.
#
# Let's also check: does D_F constructed this way anticommute with J?
# In NCG: D_F J = epsilon' J D_F. For KO-dim 6: epsilon' = +1, so D_F J = J D_F.

# Check J-compatibility of both options
for label, D_F_32 in [("off-diagonal", D_F_32_offdiag), ("diagonal", D_F_32_diag)]:
    # J D_F = Xi conj(D_F): need D_F Xi = Xi conj(D_F)?
    # Actually J = Xi . conj, so J D_F J^{-1} = Xi conj(D_F . Xi . conj(.)) ...
    # Simpler: [D_F, J] = 0 means D_F (Xi . conj(v)) = Xi . conj(D_F . v)
    # for all v. As matrices: D_F Xi = Xi conj(D_F), i.e. J-compat.
    err_jcompat = np.max(np.abs(D_F_32 @ Xi - Xi @ np.conj(D_F_32)))
    print(f"  D_F_32 ({label}) J-compatible: {err_jcompat:.2e}")


# =============================================================================
# PART 2: Build A_F generators (bimodule representation)
# =============================================================================

print("\n" + "=" * 76)
print("BUILDING A_F GENERATORS (bimodule representation)")
print("=" * 76)

def build_bimodule_16(L4, R4):
    """pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j]"""
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen

AF_gens_16 = []
AF_names = []
AF_factor = []

# C factor
L_C1 = np.diag([1.0, 0, 0, 0]).astype(complex)  # projection on row 0
L_Ci = np.diag([1j, 0, 0, 0]).astype(complex)
AF_gens_16.append(build_bimodule_16(L_C1, np.eye(4, dtype=complex)))
AF_names.append('C_Re'); AF_factor.append('C')
AF_gens_16.append(build_bimodule_16(L_Ci, np.eye(4, dtype=complex)))
AF_names.append('C_Im'); AF_factor.append('C')

# H factor
# H_1 = full identity
AF_gens_16.append(build_bimodule_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
AF_names.append('H_1'); AF_factor.append('H')

# H_i: diag(i, -i, i, -i) on rows
AF_gens_16.append(build_bimodule_16(np.diag([1j, -1j, 1j, -1j]), np.eye(4, dtype=complex)))
AF_names.append('H_i'); AF_factor.append('H')

# H_j: rows 2-3 mixing
L_Hj = np.zeros((4,4), dtype=complex)
L_Hj[2,3] = 1.0; L_Hj[3,2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append('H_j'); AF_factor.append('H')

# H_k: rows 2-3 mixing
L_Hk = np.zeros((4,4), dtype=complex)
L_Hk[2,3] = 1j; L_Hk[3,2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append('H_k'); AF_factor.append('H')

# M_3(C) factor: L=I_4, R=diag(1, m^dag)
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m = np.zeros((3,3), dtype=complex)
            m[a,b] = val
            R_m = np.eye(4, dtype=complex)
            R_m[1:,1:] = m.conj().T  # m^dag
            AF_gens_16.append(build_bimodule_16(np.eye(4, dtype=complex), R_m))
            AF_names.append(f'M3_E{a}{b}_{part}')
            AF_factor.append('M3')

print(f"  Total generators: {len(AF_gens_16)}")

# Extend to C^32
AF_gens_32 = [build_full_32(g) for g in AF_gens_16]


# =============================================================================
# PART 3: ORDER-ONE TEST with both D_F options
# =============================================================================

for label, D_F_32 in [("off-diagonal", D_F_32_offdiag), ("diagonal", D_F_32_diag)]:
    print(f"\n{'=' * 76}")
    print(f"ORDER-ONE TEST: [[D_F, a], Xi b^T Xi] = 0  (D_F = {label})")
    print(f"{'=' * 76}")

    max_o1 = 0
    n_viol = 0
    o1_by_factor = {}

    for i, (Ti, ni, fi) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
        comm_Da = D_F_32 @ Ti - Ti @ D_F_32  # [D_F, a]
        for j, (Tj, nj, fj) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
            b_opp = Xi @ Tj.T @ Xi  # Jb*J^{-1}
            double_comm = comm_Da @ b_opp - b_opp @ comm_Da  # [[D_F, a], Jb*J^{-1}]
            err = np.max(np.abs(double_comm))
            if err > max_o1:
                max_o1 = err
                worst = (ni, nj, err)
            if err > 1e-6:
                n_viol += 1

            pair_key = f'[{fi}, o({fj})]'
            if pair_key not in o1_by_factor:
                o1_by_factor[pair_key] = 0.0
            o1_by_factor[pair_key] = max(o1_by_factor[pair_key], err)

    print(f"\n  Max |[[D_F, a], o(b)]|: {max_o1:.6e}")
    print(f"  Violations (>1e-6): {n_viol} / {len(AF_gens_32)**2}")
    if max_o1 > 1e-6:
        print(f"  Worst pair: [[D_F, {worst[0]}], o({worst[1]})] = {worst[2]:.6e}")

    print(f"\n  By factor combination:")
    for pair_key in sorted(o1_by_factor.keys()):
        val = o1_by_factor[pair_key]
        status = 'PASS' if val < 1e-6 else f'{val:.6e}'
        print(f"    {pair_key}: {status}")


# =============================================================================
# PART 4: Also try D_F from ACTUAL Baptista non-homomorphism
# =============================================================================

print(f"\n{'=' * 76}")
print(f"D_F FROM BAPTISTA NON-HOMOMORPHISM (eq 2.65 directly)")
print(f"{'=' * 76}")

# The C^2 directions in su(3) are:
# e_3 = -i*lambda_4/2 (off-diag 0-1 real part)
# e_4 = -i*lambda_5/2 (off-diag 0-1 imag part)
# e_5 = -i*lambda_6/2 (off-diag 0-2 real part)
# e_6 = -i*lambda_7/2 (off-diag 0-2 imag part)

basis_su3 = su3_basis()
C2_gens = [basis_su3[3], basis_su3[4], basis_su3[5], basis_su3[6]]

print("\n  C^2 generators of su(3):")
for idx, v in enumerate(C2_gens):
    print(f"    e_{idx+3}: v_11 = {v[0,0]:.4f}")

# The non-homomorphism delta(u, v) for u, v in C^2:
# delta(u,v) = L_{[u,v]} - [L_u, L_v]
# On the 4x4 matrix:
#   delta(u,v)_{0,j} = 2*[u,v]_11 * c_j  (j=1,2,3, acting on row 0)
#   delta(u,v)_{i,0} = -2*[u,v]_11 * b_i  (i=1,2,3, acting on col 0)
#   all other entries = 0

# As a 16x16 matrix, delta(u,v) has entries:
#   delta[flat(0,j), flat(i,j')] for coupling c <-> b

# Let me compute delta directly using L_action_matrix
print("\n  Computing L non-homomorphism for C^2 x C^2 pairs:")

deltas_16 = []
for i, u in enumerate(C2_gens):
    for j, v in enumerate(C2_gens):
        uv = u @ v - v @ u  # [u, v] in su(3)
        L_uv = L_action_matrix(uv)
        L_u = L_action_matrix(u)
        L_v = L_action_matrix(v)
        comm_LuLv = L_u @ L_v - L_v @ L_u
        delta = L_uv - comm_LuLv
        err = np.max(np.abs(delta))
        if err > 1e-10:
            uv_11 = uv[0, 0]
            print(f"    delta(e_{i+3}, e_{j+3}): max={err:.4f}, [u,v]_11={uv_11:.4f}")
            deltas_16.append(delta)

print(f"\n  Number of nonzero deltas: {len(deltas_16)}")

# Build D_F from the deltas
# The finite Dirac operator is typically a SUM of these delta terms,
# or more precisely, it's the bilinear form that the deltas represent.
#
# In Connes' framework, D_F is parametrized by Yukawa matrices.
# The STRUCTURE is fixed (it's the c<->b coupling), but the COEFFICIENTS
# (Yukawa couplings) are free parameters.
#
# For order-one checking, the key is: does A_F satisfy order-one for ALL
# D_F of the correct form, or just for specific values?
#
# The order-one condition is: [[D_F, a], Jb*J^{-1}] = 0 for all a, b in A_F.
# This must hold for ALL D_F in the allowed space (since D_F parametrizes
# the Higgs field, and order-one must hold for all Higgs configurations).

# Let's use a GENERIC D_F: sum of random coefficients * deltas
if deltas_16:
    # Use a random Yukawa (complex 3x3)
    np.random.seed(42)
    yukawa = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)

    # D_F from Yukawa: couples c_j <-> b_i with coefficient yukawa[i,j]
    D_F_yukawa_16 = np.zeros((16, 16), dtype=complex)
    for i in range(3):
        for j in range(3):
            c_idx = j + 1  # c entries at flat 1,2,3
            b_idx = i + 4  # b entries at flat 4,5,6
            D_F_yukawa_16[c_idx, b_idx] = yukawa[i, j]  # c -> b coupling
            D_F_yukawa_16[b_idx, c_idx] = np.conj(yukawa[i, j])  # b -> c (hermitian)

    print(f"\n  D_F (random Yukawa) hermitian: "
          f"{np.max(np.abs(D_F_yukawa_16 - D_F_yukawa_16.conj().T)):.2e}")

    # Extend to C^32 (block diagonal for within-chirality coupling)
    D_F_yuk_32 = np.zeros((32, 32), dtype=complex)
    D_F_yuk_32[:16, :16] = D_F_yukawa_16
    D_F_yuk_32[16:, 16:] = G5 @ np.conj(D_F_yukawa_16) @ G5

    print(f"  D_F_32 (Yukawa) hermitian: "
          f"{np.max(np.abs(D_F_yuk_32 - D_F_yuk_32.conj().T)):.2e}")
    err_jcompat = np.max(np.abs(D_F_yuk_32 @ Xi - Xi @ np.conj(D_F_yuk_32)))
    print(f"  D_F_32 (Yukawa) J-compatible: {err_jcompat:.2e}")

    # Test order-one with Yukawa D_F
    print(f"\n  ORDER-ONE with Yukawa D_F (diagonal):")
    max_o1_yuk = 0
    n_viol_yuk = 0
    o1_by_factor_yuk = {}

    for i, (Ti, ni, fi) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
        comm_Da = D_F_yuk_32 @ Ti - Ti @ D_F_yuk_32
        for j, (Tj, nj, fj) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
            b_opp = Xi @ Tj.T @ Xi
            double_comm = comm_Da @ b_opp - b_opp @ comm_Da
            err = np.max(np.abs(double_comm))
            max_o1_yuk = max(max_o1_yuk, err)
            if err > 1e-6:
                n_viol_yuk += 1

            pair_key = f'[{fi}, o({fj})]'
            if pair_key not in o1_by_factor_yuk:
                o1_by_factor_yuk[pair_key] = 0.0
            o1_by_factor_yuk[pair_key] = max(o1_by_factor_yuk[pair_key], err)

    print(f"    Max |[[D_F, a], o(b)]|: {max_o1_yuk:.6e}")
    print(f"    Violations (>1e-6): {n_viol_yuk} / {len(AF_gens_32)**2}")

    print(f"\n    By factor combination:")
    for pair_key in sorted(o1_by_factor_yuk.keys()):
        val = o1_by_factor_yuk[pair_key]
        status = 'PASS' if val < 1e-6 else f'{val:.6e}'
        print(f"      {pair_key}: {status}")


# =============================================================================
# PART 5: Also try D_F as OFF-DIAGONAL (chirality-changing)
# =============================================================================

print(f"\n{'=' * 76}")
print(f"ORDER-ONE with OFF-DIAGONAL Yukawa D_F (chirality-changing)")
print(f"{'=' * 76}")

if deltas_16:
    D_F_offdiag_yuk = np.zeros((32, 32), dtype=complex)
    D_F_offdiag_yuk[:16, 16:] = D_F_yukawa_16
    D_F_offdiag_yuk[16:, :16] = D_F_yukawa_16.conj().T

    print(f"  hermitian: {np.max(np.abs(D_F_offdiag_yuk - D_F_offdiag_yuk.conj().T)):.2e}")
    anticomm = D_F_offdiag_yuk @ gamma_F + gamma_F @ D_F_offdiag_yuk
    print(f"  {{D_F, gamma}} = 0: {np.max(np.abs(anticomm)):.2e}")
    err_jcompat = np.max(np.abs(D_F_offdiag_yuk @ Xi - Xi @ np.conj(D_F_offdiag_yuk)))
    print(f"  J-compatible: {err_jcompat:.2e}")

    max_o1_off = 0
    n_viol_off = 0
    o1_by_factor_off = {}

    for i, (Ti, ni, fi) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
        comm_Da = D_F_offdiag_yuk @ Ti - Ti @ D_F_offdiag_yuk
        for j, (Tj, nj, fj) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
            b_opp = Xi @ Tj.T @ Xi
            double_comm = comm_Da @ b_opp - b_opp @ comm_Da
            err = np.max(np.abs(double_comm))
            max_o1_off = max(max_o1_off, err)
            if err > 1e-6:
                n_viol_off += 1
            pair_key = f'[{fi}, o({fj})]'
            if pair_key not in o1_by_factor_off:
                o1_by_factor_off[pair_key] = 0.0
            o1_by_factor_off[pair_key] = max(o1_by_factor_off[pair_key], err)

    print(f"\n  Max |[[D_F, a], o(b)]|: {max_o1_off:.6e}")
    print(f"  Violations (>1e-6): {n_viol_off} / {len(AF_gens_32)**2}")

    print(f"\n  By factor combination:")
    for pair_key in sorted(o1_by_factor_off.keys()):
        val = o1_by_factor_off[pair_key]
        status = 'PASS' if val < 1e-6 else f'{val:.6e}'
        print(f"    {pair_key}: {status}")


# =============================================================================
# PART 6: SUMMARY
# =============================================================================

print(f"\n{'=' * 76}")
print("SUMMARY")
print(f"{'=' * 76}")
print(f"  D_F from Baptista eq 2.65 non-homomorphism: c <-> b coupling")
print(f"  Nonzero delta pairs: {len(deltas_16)}")
print(f"  D_F forms tested:")
print(f"    1. Identity Yukawa, off-diagonal (chirality-changing)")
print(f"    2. Identity Yukawa, diagonal (within-chirality)")
print(f"    3. Random Yukawa, diagonal")
print(f"    4. Random Yukawa, off-diagonal (chirality-changing)")
