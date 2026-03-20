"""
PHASE 2.5 TRACE: Detailed trace of order-one failure for specific generators
=============================================================================

Trace through the double commutator [[D_F, pi(a)], o(b)] for the worst-case
pair (H_i, H_i) to understand WHERE and WHY order-one fails.

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix,
)

np.set_printoptions(precision=6, linewidth=140, suppress=True)

# Infrastructure
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
# Build specific generators
# =============================================================================

# D_F (identity Yukawa, c<->b coupling)
D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0  # c_j -> b_j
    D_F_16[j+4, j+1] = 1.0  # b_j -> c_j

D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = rho_minus(D_F_16)

# H_i generator (the worst case)
L_Hi = np.diag([1j, -1j, 1j, -1j])
Hi_16 = build_bimodule_16(L_Hi, np.eye(4, dtype=complex))
Hi_32 = build_full_32(Hi_16)

# C_Im generator
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
CIm_16 = build_bimodule_16(L_CIm, np.eye(4, dtype=complex))
CIm_32 = build_full_32(CIm_16)

# M3_E00_Re (simplest M_3 generator: identity in (0,0) position)
m_elem = np.zeros((3, 3), dtype=complex)
m_elem[0, 0] = 1.0
m_dag = m_elem.conj().T
R_m = np.eye(4, dtype=complex)
R_m[1:, 1:] = m_dag
M3_16 = build_bimodule_16(np.eye(4, dtype=complex), R_m)
M3_32 = build_full_32(M3_16)


# =============================================================================
# TRACE: [D_F, H_i] and o(H_i)
# =============================================================================

print("=" * 76)
print("TRACE: [[D_F, H_i], o(H_i)]")
print("=" * 76)

# Step 1: [D_F, H_i]
D_comm_Hi = D_F_32 @ Hi_32 - Hi_32 @ D_F_32

print(f"\n  [D_F, H_i] 32x32 block structure:")
print(f"    Psi_+ block ([:16,:16]): max = {np.max(np.abs(D_comm_Hi[:16, :16])):.4f}")
print(f"    Psi_- block ([16:,16:]): max = {np.max(np.abs(D_comm_Hi[16:, 16:])):.4f}")
print(f"    Cross blocks: max = {max(np.max(np.abs(D_comm_Hi[:16, 16:])), np.max(np.abs(D_comm_Hi[16:, :16]))):.4f}")

print(f"\n  [D_F, H_i] Psi_+ block nonzero entries:")
block_pp = D_comm_Hi[:16, :16]
for r in range(16):
    for c in range(16):
        if abs(block_pp[r, c]) > 1e-10:
            print(f"    [{r},{c}] = {block_pp[r,c]:.4f}")

# Step 2: o(H_i) = Xi @ H_i^T @ Xi
o_Hi = Xi @ Hi_32.T @ Xi

print(f"\n  o(H_i) 32x32 block structure:")
print(f"    Psi_+ block: max = {np.max(np.abs(o_Hi[:16, :16])):.4f}")
print(f"    Psi_- block: max = {np.max(np.abs(o_Hi[16:, 16:])):.4f}")
print(f"    Cross (+,-): max = {np.max(np.abs(o_Hi[:16, 16:])):.4f}")
print(f"    Cross (-,+): max = {np.max(np.abs(o_Hi[16:, :16])):.4f}")

# The cross-chirality structure is key!
# If [D_F, H_i] is block-diagonal but o(H_i) has cross-blocks,
# the double commutator will have cross-blocks.

print(f"\n  o(H_i) cross-block (+,-) nonzero entries:")
cross_pm = o_Hi[:16, 16:]
for r in range(16):
    for c in range(16):
        if abs(cross_pm[r, c]) > 1e-10:
            print(f"    [{r},{c+16}] = {cross_pm[r,c]:.4f}")

# Step 3: [[D_F, H_i], o(H_i)]
double_comm = D_comm_Hi @ o_Hi - o_Hi @ D_comm_Hi

print(f"\n  [[D_F, H_i], o(H_i)]:")
print(f"    Max absolute value: {np.max(np.abs(double_comm)):.4f}")
print(f"    Psi_+ block: max = {np.max(np.abs(double_comm[:16, :16])):.4f}")
print(f"    Psi_- block: max = {np.max(np.abs(double_comm[16:, 16:])):.4f}")
print(f"    Cross blocks: max = {max(np.max(np.abs(double_comm[:16, 16:])), np.max(np.abs(double_comm[16:, :16]))):.4f}")


# =============================================================================
# TRACE: Does o(b) have cross-chirality structure?
# =============================================================================

print(f"\n{'=' * 76}")
print("CROSS-CHIRALITY STRUCTURE OF o-MAP")
print(f"{'=' * 76}")

# For any generator b in A_F, what does o(b) = Xi @ b^T @ Xi look like?
# b_32 is block-diagonal: [[b_16, 0], [0, rho_minus(b_16)]]
# Xi = [[0, -G5], [-G5, 0]]
# Xi^2 = [[G5^2, 0], [0, G5^2]] = I (since G5 is diagonal with +/-1)

# So o(b) = Xi @ b^T @ Xi:
# b^T = [[b_16^T, 0], [0, rho_minus(b_16)^T]]
# Xi @ b^T = [[-G5 @ rho_minus(b_16)^T, -G5 @ b_16^T], [-G5 @ b_16^T, ...]]
# Wait, let me be more careful:

# b_32 = [[A, 0], [0, B]]  where A = b_16, B = rho_minus(b_16) = G5 conj(b_16) G5
# b_32^T = [[A^T, 0], [0, B^T]]
# Xi = [[0, -G5], [-G5, 0]]
#
# Xi @ b_32^T = [[0, -G5], [-G5, 0]] @ [[A^T, 0], [0, B^T]]
#             = [[-G5 @ 0 + ... no wait, standard block multiplication:
#               = [[0*A^T + (-G5)*0, 0*0 + (-G5)*B^T],
#                  [(-G5)*A^T + 0*0, (-G5)*0 + 0*B^T]]
# Hmm, that's not right either. Let me just compute:

# Row 0-15, Col 0-15: Xi[:16,:16] @ b^T[:16,:16] + Xi[:16,16:] @ b^T[16:,:16]
#                    = 0 @ A^T + (-G5) @ 0 = 0
# Row 0-15, Col 16-31: Xi[:16,:16] @ b^T[:16,16:] + Xi[:16,16:] @ b^T[16:,16:]
#                     = 0 @ 0 + (-G5) @ B^T = -G5 B^T
# Row 16-31, Col 0-15: Xi[16:,:16] @ b^T[:16,:16] + Xi[16:,16:] @ b^T[16:,:16]
#                     = (-G5) @ A^T + 0 @ 0 = -G5 A^T
# Row 16-31, Col 16-31: 0

# So Xi @ b^T = [[0, -G5 B^T], [-G5 A^T, 0]]

# Then (Xi @ b^T) @ Xi:
# Row 0-15: [0, -G5 B^T] @ Xi = [(-G5 B^T) @ (-G5), 0 @ (-G5)] = ... wait
# Actually:
# Row 0-15, Col 0-15: 0 @ Xi[:16,:16] + (-G5 B^T) @ Xi[16:,:16]
#                    = 0 + (-G5 B^T)(-G5) = G5 B^T G5
# Row 0-15, Col 16-31: 0 @ Xi[:16,16:] + (-G5 B^T) @ Xi[16:,16:]
#                     = 0 + (-G5 B^T)(0) = 0
# Row 16-31, Col 0-15: (-G5 A^T) @ 0 + 0 @ (-G5) = 0
# Row 16-31, Col 16-31: (-G5 A^T)(-G5) + 0 = G5 A^T G5

# So o(b) = Xi @ b^T @ Xi = [[G5 B^T G5, 0], [0, G5 A^T G5]]
# where A = b_16, B = rho_minus(b_16) = G5 conj(b_16) G5

# G5 B^T G5 = G5 (G5 conj(b_16) G5)^T G5 = G5 G5^T conj(b_16)^T G5^T G5
#           = G5^2 conj(b_16)^T G5^2 = conj(b_16)^T = b_16^dag (the dagger!)
# Since G5 is diagonal and real: G5 = G5^T, G5^2 = I.

# So: o(b) upper-left = b_16^dag = (b_16)^{conjugate transpose}
#     o(b) lower-right = G5 b_16^T G5 = rho_minus_T(b_16)

# THIS MEANS o(b) IS BLOCK-DIAGONAL! No cross-chirality!

print(f"\n  Analytic result: o(b) = Xi @ b^T @ Xi for block-diagonal b:")
print(f"    Upper-left (Psi_+): b_16^dag (conjugate transpose)")
print(f"    Lower-right (Psi_-): G5 @ b_16^T @ G5")
print(f"    Cross-blocks: ZERO")
print(f"\n  This means o(b) is ALSO block-diagonal if b is.")

# Verify numerically
print(f"\n  Numerical verification on H_i:")
print(f"    o(H_i) upper-left = H_i_16^dag?")
Hi_16_dag = Hi_16.conj().T
o_Hi_pp = o_Hi[:16, :16]
print(f"    Max |o(H_i)_++ - H_i_16^dag|: {np.max(np.abs(o_Hi_pp - Hi_16_dag)):.2e}")

print(f"\n    o(H_i) cross (+,-): {np.max(np.abs(o_Hi[:16, 16:])):.2e}")
print(f"    o(H_i) cross (-,+): {np.max(np.abs(o_Hi[16:, :16])):.2e}")

# Good. Both [D_F, a] and o(b) are block-diagonal.
# So the double commutator [[D_F, a], o(b)] is also block-diagonal.
# The order-one condition reduces to TWO conditions:
#   Psi_+: [[D_F_16, a_16], a_16_dag^o] = 0  where a_16_dag^o = b_16^dag
#   Psi_-: similar for the rho_minus block

print(f"\n{'=' * 76}")
print("ORDER-ONE REDUCED TO Psi_+ BLOCK")
print(f"{'=' * 76}")

# For the Psi_+ block:
# [D_F_16, a_16] is a 16x16 matrix
# o(b)_++ = b_16^dag
# [[D_F_16, a_16], b_16^dag] = 0

# Let's test this for all factor pairs on Psi_+ only
print(f"\n  Testing [[D_F_16, a_16], b_16^dag] = 0 on Psi_+ block:")

# Build all generators on Psi_+
AF_16_list = []
AF_16_names = []
AF_16_factors = []

L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_16_list.append(build_bimodule_16(L_CIm, np.eye(4)))
AF_16_names.append('C_Im'); AF_16_factors.append('C')

L_CRe = np.diag([1.0, 0.0, 0.0, 0.0])
AF_16_list.append(build_bimodule_16(L_CRe, np.eye(4)))
AF_16_names.append('C_Re_proj'); AF_16_factors.append('C')

L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_16_list.append(build_bimodule_16(L_Hi, np.eye(4)))
AF_16_names.append('H_i'); AF_16_factors.append('H')

L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_16_list.append(build_bimodule_16(L_Hj, np.eye(4)))
AF_16_names.append('H_j'); AF_16_factors.append('H')

L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_16_list.append(build_bimodule_16(L_Hk, np.eye(4)))
AF_16_names.append('H_k'); AF_16_factors.append('H')

AF_16_list.append(build_bimodule_16(np.eye(4), np.eye(4)))
AF_16_names.append('H_1'); AF_16_factors.append('H')

for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_elem.conj().T
            AF_16_list.append(build_bimodule_16(np.eye(4), R_m))
            AF_16_names.append(f'M3_E{a}{b}_{part}')
            AF_16_factors.append('M3')

# Test on Psi_+ block
max_o1_16 = 0
o1_fac_16 = {}
worst_pair_16 = None

for i in range(len(AF_16_list)):
    Da = D_F_16 @ AF_16_list[i] - AF_16_list[i] @ D_F_16
    for j in range(len(AF_16_list)):
        ob = AF_16_list[j].conj().T  # o(b) on Psi_+ = b^dag
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        if err > max_o1_16:
            max_o1_16 = err
            worst_pair_16 = (AF_16_names[i], AF_16_names[j])
        pk = f'[{AF_16_factors[i]}, o({AF_16_factors[j]})]'
        if pk not in o1_fac_16:
            o1_fac_16[pk] = 0.0
        o1_fac_16[pk] = max(o1_fac_16[pk], err)

print(f"  Max |[[D_F, a], b^dag]| on Psi_+: {max_o1_16:.2e}")
if worst_pair_16:
    print(f"  Worst pair: {worst_pair_16}")
print(f"\n  By factor:")
for pk in sorted(o1_fac_16.keys()):
    v = o1_fac_16[pk]
    s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
    print(f"    {pk}: {s}")


# =============================================================================
# TRACE: What does [D_F, a] look like for different generators?
# =============================================================================

print(f"\n{'=' * 76}")
print("STRUCTURE OF [D_F, a] FOR EACH FACTOR")
print(f"{'=' * 76}")

# D_F couples c<->b: indices 1-3 <-> 4-6
# The other indices (0 and 7-15) are NOT coupled by D_F.
# So [D_F, a] = 0 for any a that acts ONLY on {0, 7-15}.
# [D_F, a] != 0 only for a that acts on {1-6}.

for i, (T, name, fac) in enumerate(zip(AF_16_list, AF_16_names, AF_16_factors)):
    Da = D_F_16 @ T - T @ D_F_16
    norm_Da = np.max(np.abs(Da))
    if norm_Da > 1e-10:
        # Which indices does [D_F, a] act on?
        active = [(r, c) for r in range(16) for c in range(16) if abs(Da[r, c]) > 1e-10]
        active_rows = sorted(set(r for r, c in active))
        active_cols = sorted(set(c for r, c in active))
        print(f"  {name:15s} ({fac}): |[D_F, a]| = {norm_Da:.4f}, rows={active_rows[:8]}, cols={active_cols[:8]}")
    else:
        print(f"  {name:15s} ({fac}): [D_F, a] = 0")

# Key question: which generators commute with D_F?
# If [D_F, a] = 0, then [[D_F, a], o(b)] = 0 trivially.

print(f"\n  Summary: generators commuting with D_F:")
comm_with_DF = []
not_comm = []
for i, (T, name, fac) in enumerate(zip(AF_16_list, AF_16_names, AF_16_factors)):
    Da = D_F_16 @ T - T @ D_F_16
    if np.max(np.abs(Da)) < 1e-10:
        comm_with_DF.append(name)
    else:
        not_comm.append(name)

print(f"    Commute: {comm_with_DF}")
print(f"    Don't commute: {not_comm}")

# For generators that DO NOT commute with D_F, check if b^dag commutes with [D_F, a]
print(f"\n  For non-commuting generators, does b^dag commute with [D_F, a]?")
for name_a in not_comm[:5]:
    idx_a = AF_16_names.index(name_a)
    Da = D_F_16 @ AF_16_list[idx_a] - AF_16_list[idx_a] @ D_F_16
    for name_b in not_comm[:5]:
        idx_b = AF_16_names.index(name_b)
        ob = AF_16_list[idx_b].conj().T
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        if err > 1e-8:
            print(f"    [[D_F, {name_a}], {name_b}^dag]: {err:.4f}")
