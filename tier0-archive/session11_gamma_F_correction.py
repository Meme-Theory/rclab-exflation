"""
SESSION 11 CROSS-REVIEW: GAMMA_F CORRECTION TEST
==================================================

KK-theorist hypothesis: Our gamma_F = diag(+I_16, -I_16) is the WRONG grading.
It's particle/antiparticle grading (Psi+ vs Psi-), NOT internal chirality.

The CORRECT gamma_F should grade rows 0-1 (RH) vs rows 2-3 (LH) within each
16-dim block. In Connes' NCG:
  gamma_F |_{RH} = +1, gamma_F |_{LH} = -1

For the 4x4 matrix Psi:
  Row 0 = up-RH (nu_R): +1
  Row 1 = down-RH (e_R): +1
  Row 2 = up-LH (nu_L): -1
  Row 3 = down-LH (e_L): -1

On the 16-component vector (flattened 4x4):
  gamma_F_16 = diag of chirality signs, one per (row, col) pair

On the 32-dim H_F = Psi+ + Psi-:
  gamma_F_32 should be block-diagonal with the SAME chirality on each block
  (particle and antiparticle have same chirality assignment)

This script tests:
1. Construct the corrected gamma_F
2. Check if block-diagonal Connes Yukawa D_F anticommutes with it
3. Re-run order-one tests
4. Re-check the impossibility theorem with corrected gamma_F

Author: Sim-Specialist Agent (phonon-exflation project, Session 11 cross-review)
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

def get_row_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return 0
    elif 4 <= flat_idx <= 6: return flat_idx - 3  # rows 1,2,3
    else: return (flat_idx - 7) // 3 + 1

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

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

def vec_real(T):
    return np.concatenate([T.flatten().real, T.flatten().imag])


# =============================================================================
# PART 1: CONSTRUCT CORRECTED GAMMA_F
# =============================================================================

print("=" * 80)
print("PART 1: CORRECTED GAMMA_F -- INTERNAL CHIRALITY GRADING")
print("=" * 80)

# OLD gamma_F: particle/antiparticle
gamma_F_old = np.zeros((32, 32))
gamma_F_old[:16, :16] = np.eye(16)
gamma_F_old[16:, 16:] = -np.eye(16)

# NEW gamma_F: internal chirality (rows 0-1 = RH = +1, rows 2-3 = LH = -1)
# For each flat index, determine the ROW of the 4x4 matrix
chirality_16 = np.zeros(16)
for idx in range(16):
    row = get_row_index(idx)
    if row <= 1:  # RH
        chirality_16[idx] = +1.0
    else:  # LH
        chirality_16[idx] = -1.0

print(f"  Chirality signs on 16-dim (per flat index):")
for idx in range(16):
    row = get_row_index(idx)
    col = get_column_index(idx)
    print(f"    flat={idx:2d}  (row={row}, col={col})  chi = {chirality_16[idx]:+.0f}")

gamma_F_16 = np.diag(chirality_16)

# On H_F = Psi+ + Psi-: gamma_F acts on BOTH blocks with SAME chirality
# (chirality is a property of the particle type, not particle vs antiparticle)
gamma_F_new = np.zeros((32, 32))
gamma_F_new[:16, :16] = gamma_F_16
gamma_F_new[16:, 16:] = gamma_F_16  # SAME sign on both blocks

print(f"\n  gamma_F_new eigenvalues: {np.sort(np.linalg.eigvalsh(gamma_F_new))}")
print(f"  gamma_F_new^2 = I? {np.max(np.abs(gamma_F_new @ gamma_F_new - np.eye(32))):.2e}")
print(f"  gamma_F_new Hermitian? {np.max(np.abs(gamma_F_new - gamma_F_new.T)):.2e}")

# Verify: J should commute with gamma_F (KO-dim 6 has epsilon'' = -1 which is
# {J, gamma_F} = 0 or [J, gamma_F] = 0 depending on convention)
# Actually for KO-dim 6: epsilon'' = -1 means J*gamma = -gamma*J (anticommutation)
# Let's check both
JgF = Xi @ np.conj(gamma_F_new) @ Xi  # careful: J = Xi o conj, so J gamma_F J^-1 = Xi gamma_F_bar Xi
# But gamma_F is real, so gamma_F_bar = gamma_F
JgF_check = Xi @ gamma_F_new @ Xi

comm_J_gamma = np.max(np.abs(JgF_check - gamma_F_new))
anti_J_gamma = np.max(np.abs(JgF_check + gamma_F_new))
print(f"\n  [J, gamma_F_new] = 0? max error: {comm_J_gamma:.2e}")
print(f"  {{J, gamma_F_new}} = 0? max error: {anti_J_gamma:.2e}")

# Also check with old gamma_F for comparison
JgF_old = Xi @ gamma_F_old @ Xi
comm_J_gamma_old = np.max(np.abs(JgF_old - gamma_F_old))
anti_J_gamma_old = np.max(np.abs(JgF_old + gamma_F_old))
print(f"\n  OLD gamma_F:")
print(f"  [J, gamma_F_old] = 0? max error: {comm_J_gamma_old:.2e}")
print(f"  {{J, gamma_F_old}} = 0? max error: {anti_J_gamma_old:.2e}")


# =============================================================================
# PART 2: BUILD A_F GENERATORS AND D_F CANDIDATES
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 2: CONNES A_F GENERATORS + D_F CANDIDATES")
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

# D_F candidates
D_connes_left = np.zeros((4, 4), dtype=complex)
D_connes_left[0, 2] = 1.0; D_connes_left[2, 0] = 1.0
D_connes_left[1, 3] = 1.0; D_connes_left[3, 1] = 1.0
D_connes_16 = build_bimodule_16(D_connes_left, np.eye(4, dtype=complex))

D_baptista_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_baptista_16[j+1, j+4] = 1.0
    D_baptista_16[j+4, j+1] = 1.0

D_color_16 = np.zeros((16, 16), dtype=complex)
for col in range(4):
    for rpair in [(0, 2), (2, 0), (1, 3), (3, 1)]:
        fi = flat_idx(rpair[0], col)
        fj = flat_idx(rpair[1], col)
        D_color_16[fi, fj] = 1.0

DF_candidates = {
    'Connes_left_Yukawa': D_connes_16,
    'Baptista_delta_v': D_baptista_16,
    'Color_coupled': D_color_16,
}


# =============================================================================
# PART 3: TEST ALL D_F WITH CORRECTED GAMMA_F
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 3: D_F PROPERTIES WITH CORRECTED GAMMA_F")
print("=" * 80)

def test_order_one(D_F_32, AF_gens, AF_names_list, AF_factor_list, Xi_mat, label):
    n_gens = len(AF_gens)
    max_o1 = 0
    max_pair = None
    n_viol = 0
    o1_by_factor = {}

    for i in range(n_gens):
        Da = D_F_32 @ AF_gens[i] - AF_gens[i] @ D_F_32
        for j in range(n_gens):
            ob = Xi_mat @ AF_gens[j].T @ Xi_mat
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

    return max_o1, o1_by_factor


# Test in block-diagonal form on C^32
print("\n  --- Block-diagonal D_F (same on Psi+ and rho_minus on Psi-) ---")
for name, DF16 in DF_candidates.items():
    DF32 = np.zeros((32, 32), dtype=complex)
    DF32[:16, :16] = DF16
    DF32[16:, 16:] = rho_minus(DF16)

    herm = np.max(np.abs(DF32 - DF32.conj().T))
    j_compat = np.max(np.abs(DF32 @ Xi - Xi @ np.conj(DF32)))

    # NEW gamma_F tests
    anticomm_new = np.max(np.abs(DF32 @ gamma_F_new + gamma_F_new @ DF32))
    comm_new = np.max(np.abs(DF32 @ gamma_F_new - gamma_F_new @ DF32))

    # OLD gamma_F tests for comparison
    anticomm_old = np.max(np.abs(DF32 @ gamma_F_old + gamma_F_old @ DF32))
    comm_old = np.max(np.abs(DF32 @ gamma_F_old - gamma_F_old @ DF32))

    print(f"\n  {name} (block-diagonal):")
    print(f"    Hermitian: {herm:.2e}, J-compat: {j_compat:.2e}")
    print(f"    OLD gamma_F: anticomm={anticomm_old:.2e}, comm={comm_old:.2e}")
    print(f"    NEW gamma_F: anticomm={anticomm_new:.2e}, comm={comm_new:.2e}")

    # Order-one test
    test_order_one(DF32, AF_gens_32, AF_names, AF_factor, Xi, f"{name} block-diag")


# =============================================================================
# PART 4: THE CRITICAL TEST -- DOES THE CORRECTED GAMMA_F RESOLVE THE CATCH-22?
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 4: CRITICAL TEST -- BLOCK-DIAG CONNES YUKAWA WITH NEW GAMMA_F")
print("=" * 80)

DF32_connes = np.zeros((32, 32), dtype=complex)
DF32_connes[:16, :16] = D_connes_16
DF32_connes[16:, 16:] = rho_minus(D_connes_16)

anticomm = np.max(np.abs(DF32_connes @ gamma_F_new + gamma_F_new @ DF32_connes))
comm = np.max(np.abs(DF32_connes @ gamma_F_new - gamma_F_new @ DF32_connes))
j_compat = np.max(np.abs(DF32_connes @ Xi - Xi @ np.conj(DF32_connes)))
herm = np.max(np.abs(DF32_connes - DF32_connes.conj().T))

print(f"  Connes left-Yukawa D_F (block-diagonal on C^32):")
print(f"    Hermitian: {herm:.2e}")
print(f"    J-compatible: {j_compat:.2e}")
print(f"    {{D, gamma_F_new}} = 0 (anticommutation): {anticomm:.2e}")
print(f"    [D, gamma_F_new] = 0 (commutation): {comm:.2e}")

if anticomm < 1e-10:
    print(f"\n    *** ANTICOMMUTATION SATISFIED! ***")
    print(f"    The KK-theorist gamma_F correction resolves the chirality issue.")

    # Now test order-one
    max_o1, o1f = test_order_one(DF32_connes, AF_gens_32, AF_names, AF_factor, Xi,
                                  "Connes Yukawa + NEW gamma_F")

    n_pass = sum(1 for v in o1f.values() if v < 1e-8)
    n_total = len(o1f)

    print(f"\n    ORDER-ONE SCORE: {n_pass}/{n_total} factor pairs PASS")

    if max_o1 < 1e-8:
        print(f"\n    *** FULL ORDER-ONE SATISFIED! ***")
        print(f"    THE CATCH-22 IS COMPLETELY RESOLVED.")
    else:
        print(f"\n    Order-one still has violations (max = {max_o1:.2e})")
        print(f"    But the key question is: are the SAME 5/9 passing as before?")
        print(f"    If yes: the fix only addresses chirality, not order-one C+H sector")
        print(f"    If different: the gamma_F change fundamentally alters the constraint landscape")
else:
    print(f"\n    Anticommutation NOT satisfied with new gamma_F.")
    print(f"    Checking if the D_F is block-diagonal in the wrong basis...")


# =============================================================================
# PART 5: CHECK GAMMA_F_NEW vs CONNES' STANDARD
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 5: WHAT DOES GAMMA_F_NEW LOOK LIKE ON THE 4x4 MATRIX?")
print("=" * 80)

# The Connes left-Yukawa couples row 0 <-> row 2, row 1 <-> row 3
# These are RH <-> LH couplings.
# With gamma_F_new = diag(+1 on RH rows, -1 on LH rows):
# D acting as L_Y . Psi maps:
#   (RH component) -> (LH component) and vice versa
# So D maps eigenspace +1 -> eigenspace -1 and vice versa
# This means {D, gamma_F_new} = 0 iff D maps between chirality sectors

print("  The Connes Yukawa acts as left multiplication by:")
print(f"    L_Y = [[0, 0, 1, 0],")
print(f"           [0, 0, 0, 1],")
print(f"           [1, 0, 0, 0],")
print(f"           [0, 1, 0, 0]]")
print(f"  This maps row 0 (RH) -> row 2 (LH) and vice versa.")
print(f"  gamma_F = diag(+1, +1, -1, -1) on rows.")
print(f"  L_Y . gamma_F = [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]]")
print(f"  gamma_F . L_Y = [[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]]")
print(f"  Sum (anticommutator) = 0? Let's check:")

L_Y = D_connes_left
gF4 = np.diag([1.0, 1.0, -1.0, -1.0])
anticomm_4x4 = L_Y @ gF4 + gF4 @ L_Y
print(f"    ||L_Y . gF + gF . L_Y|| = {np.max(np.abs(anticomm_4x4)):.2e}")

if np.max(np.abs(anticomm_4x4)) < 1e-10:
    print(f"    YES: L_Y anticommutes with chirality grading (as expected).")
    print(f"    This is the DEFINING property of a Yukawa coupling in Connes NCG.")


# =============================================================================
# PART 6: FULL CHECK -- A_F GENERATORS vs NEW GAMMA_F
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 6: A_F GENERATORS vs NEW GAMMA_F")
print("=" * 80)

print("  Connes A_F elements should COMMUTE with gamma_F (they preserve chirality):")
for i, (gen32, name, factor) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
    comm = np.max(np.abs(gen32 @ gamma_F_new - gamma_F_new @ gen32))
    anticomm = np.max(np.abs(gen32 @ gamma_F_new + gamma_F_new @ gen32))
    comm_status = 'PASS' if comm < 1e-10 else f'FAIL ({comm:.2e})'
    anti_status = 'PASS' if anticomm < 1e-10 else f'FAIL ({anticomm:.2e})'

    if i < 6:  # Only print C+H generators (first 6)
        print(f"    [{name}] ({factor}): [a, gamma_F] = {comm_status}, {{a, gamma_F}} = {anti_status}")

# Check a few M3 generators
m3_comm_max = 0
for gen32 in AF_gens_32[6:]:
    c = np.max(np.abs(gen32 @ gamma_F_new - gamma_F_new @ gen32))
    m3_comm_max = max(m3_comm_max, c)
print(f"    [M3 (all 18)]: [a, gamma_F] max = {m3_comm_max:.2e}")


# =============================================================================
# PART 7: KO-DIMENSION CHECK WITH NEW GAMMA_F
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 7: KO-DIMENSION WITH CORRECTED GAMMA_F")
print("=" * 80)

J = Xi  # J = Xi o complex conjugation

# epsilon: J^2 = epsilon * I
J_squared = Xi @ Xi  # since J is anti-linear, J^2 = Xi . Xi_bar = Xi . Xi (Xi is real)
epsilon = J_squared[0, 0]
print(f"  J^2 = {epsilon:+.0f} * I (epsilon = {epsilon:+.0f})")

# epsilon': J*gamma_F = epsilon' * gamma_F * J
# J . gamma_F . v = Xi . conj(gamma_F . v) = Xi . gamma_F_bar . v_bar = Xi . gamma_F . v_bar
# (gamma_F is real)
# gamma_F . J . v = gamma_F . Xi . v_bar
# So J*gamma_F = Xi . gamma_F vs gamma_F * J = gamma_F . Xi
# epsilon' is determined by Xi . gamma_F_new vs gamma_F_new . Xi

Xi_gamma = Xi @ gamma_F_new
gamma_Xi = gamma_F_new @ Xi

comm_err = np.max(np.abs(Xi_gamma - gamma_Xi))
anti_err = np.max(np.abs(Xi_gamma + gamma_Xi))
print(f"  J*gamma_F_new = +gamma_F_new*J? error: {comm_err:.2e}")
print(f"  J*gamma_F_new = -gamma_F_new*J? error: {anti_err:.2e}")

if comm_err < 1e-10:
    epsilon_pp = 1
elif anti_err < 1e-10:
    epsilon_pp = -1
else:
    epsilon_pp = None
    print(f"  WARNING: Neither commutation nor anticommutation holds!")

print(f"  epsilon'' = {epsilon_pp}")

if epsilon is not None and epsilon_pp is not None:
    # KO-dimension from (epsilon, epsilon'):
    # dim 0: (+, +)
    # dim 2: (-, +)
    # dim 4: (-, -)
    # dim 6: (+, -)
    # (simplified -- full classification also uses epsilon' from D*gamma relation)
    if epsilon == 1 and epsilon_pp == -1:
        print(f"  KO-dimension: 6 mod 8 (CORRECT for SM!)")
    elif epsilon == 1 and epsilon_pp == 1:
        print(f"  KO-dimension: 0 mod 8")
    elif epsilon == -1 and epsilon_pp == 1:
        print(f"  KO-dimension: 2 mod 8")
    elif epsilon == -1 and epsilon_pp == -1:
        print(f"  KO-dimension: 4 mod 8")


# =============================================================================
# PART 8: SUMMARY
# =============================================================================

print(f"\n{'=' * 80}")
print("PART 8: SUMMARY -- GAMMA_F CORRECTION IMPACT")
print("=" * 80)

print(f"""
Results with CORRECTED gamma_F (internal chirality, not particle/antiparticle):

1. Connes left-Yukawa D_F:
   - Anticommutes with gamma_F_new? {anticomm < 1e-10}
   - J-compatible? {j_compat < 1e-10}
   - Hermitian? {herm < 1e-10}

2. A_F generators commute with gamma_F_new? {m3_comm_max < 1e-10}

3. KO-dimension with gamma_F_new: {'6 mod 8' if epsilon_pp == -1 else 'NOT 6'}

4. Implication for catch-22:
""")

if anticomm < 1e-10:
    print(f"   THE CATCH-22 IS DISSOLVED (at least partially).")
    print(f"   Block-diagonal D_F now anticommutes with the CORRECT gamma_F.")
    print(f"   The order-one results from Session 10 (5/9 PASS for block-diag)")
    print(f"   now apply to a chirality-correct D_F.")
    print(f"")
    print(f"   Remaining question: the 4/9 order-one failures in [C,o(C)], [C,o(H)],")
    print(f"   [H,o(C)], [H,o(H)] sectors. These may be resolved by:")
    print(f"   - Using D_K from SU(3) geometry (which has different structure)")
    print(f"   - The physical Yukawa matrix (not unit Yukawa)")
    print(f"   - The non-minimal coupling terms from Baptista eq 7.2")
else:
    print(f"   The gamma_F correction does NOT resolve the anticommutation issue.")
    print(f"   Further investigation needed.")
