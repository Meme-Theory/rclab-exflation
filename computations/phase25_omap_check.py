"""
PHASE 2.5 DEBUG: Verify the o-map (opposite algebra action)
=============================================================

The order-one condition is [[D_F, a], JbJ^{-1}] = 0 where J is the REAL structure.
In our convention: J(v) = Xi @ conj(v) (Xi = real matrix, J = Xi * complex_conj).

So J pi(b) J^{-1}(v) = Xi @ conj(pi(b) @ Xi^{-1} @ conj(v))
                       = Xi @ conj(pi(b)) @ Xi^{-1} @ v   [since Xi is real, Xi^{-1}=Xi]
                       = Xi @ conj(pi(b)) @ Xi @ v

Wait: J(v) = Xi @ v_bar (complex conjugate of v, NOT transpose).
J^{-1}(v) = Xi @ v_bar (since J^2 = +I means Xi @ Xi = I and J^{-1} = J).

So J pi(b) J^{-1}(v) = J( pi(b)( J^{-1}(v) ) )
                       = J( pi(b)( Xi @ v_bar ) )
                       = Xi @ conj( pi(b) @ Xi @ v_bar )
                       = Xi @ conj(pi(b)) @ conj(Xi) @ conj(v_bar)
                       = Xi @ conj(pi(b)) @ Xi @ v   [Xi is real, so conj(Xi)=Xi]

So J pi(b) J^{-1} = Xi @ conj(pi(b)) @ Xi  (as a matrix).

But in our order-zero tests we used: o(b) = Xi @ b^T @ Xi.
These are the SAME only if conj(pi(b)) = pi(b)^T, i.e., pi(b) is a REAL matrix
(which it is NOT for complex generators).

THIS IS THE BUG! Let me check both formulas.

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
from scipy.linalg import orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

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
# PART 1: Verify the o-map
# =============================================================================

print("=" * 76)
print("VERIFYING THE OPPOSITE ALGEBRA MAP")
print("=" * 76)

# In Connes' NCG:
#   J(v) = Xi @ conj(v)  (antilinear: J(alpha*v) = conj(alpha)*J(v))
#   J^2 = +I (epsilon = +1 for KO-dim 6)
#
# The opposite algebra action is:
#   pi^o(b)(v) = J pi(b*) J^{-1}(v)
#
# Since J^{-1} = J (because J^2 = +I):
#   pi^o(b)(v) = J( pi(b*) ( J(v) ) )
#              = J( pi(b*) ( Xi @ conj(v) ) )
#              = Xi @ conj( pi(b*) @ Xi @ conj(v) )
#              = Xi @ conj(pi(b*)) @ conj(Xi) @ v
#              = Xi @ conj(pi(b*)) @ Xi @ v   [Xi is real]
#
# So: pi^o(b) = Xi @ conj(pi(b*)) @ Xi  as a MATRIX.
#
# Now, for Connes' order-zero: [pi(a), pi^o(b)] = 0
#   i.e., [a, Xi @ conj(pi(b*)) @ Xi] = 0
#
# Connes defines b* as the ADJOINT of b in A_F.
# For the *-algebra A_F = C + H + M_3(C):
#   - C: lambda* = conj(lambda)
#   - H: q* = conj(q) (quaternion conjugate)
#   - M_3(C): m* = m^dag (conjugate transpose)
#
# So pi(b*) for each generator:
#   - pi(b*) = pi(conjugate of the algebra element represented by b)
#   - If b is self-adjoint (Hermitian), then pi(b*) = pi(b).
#   - If b is anti-Hermitian, then pi(b*) = -pi(b).
#
# In practice, since our generators are either Hermitian or anti-Hermitian
# as elements of the *-algebra:
#   - Real generators (E_{ii} for M_3, real parts): self-adjoint, pi(b*)=pi(b)
#   - Imaginary generators (iE_{ii}, imaginary parts): anti-Hermitian, pi(b*)=-pi(b)
#
# BUT in the representation, pi(b) is a 32x32 matrix and b* is the
# algebraic adjoint. If we denote the matrix representation of the algebraic
# adjoint as pi(b*), then:
#
# For Hermitian representation (faithful *-representation):
#   pi(b*) = pi(b)^dag
#
# This is the KEY: pi(b*) = pi(b)^dag (the matrix dagger).
# So:
#   pi^o(b) = Xi @ conj(pi(b)^dag) @ Xi = Xi @ pi(b)^T @ Xi
#
# This DOES give o(b) = Xi @ b^T @ Xi, which is what we've been using!
# So the o-map IS correct.

# Let's verify by explicit computation on a test generator.

# Build one A_F generator (H_i)
L_Hi = np.diag([1j, -1j, 1j, -1j])
Hi_16 = build_bimodule_16(L_Hi, np.eye(4, dtype=complex))
Hi_32 = build_full_32(Hi_16)

# Method 1: o(b) = Xi @ b^T @ Xi
o_Hi_method1 = Xi @ Hi_32.T @ Xi

# Method 2: pi^o(b) = Xi @ conj(pi(b)^dag) @ Xi = Xi @ conj(pi(b).conj().T) @ Xi
#          = Xi @ pi(b).T @ Xi  (same thing!)
o_Hi_method2 = Xi @ np.conj(Hi_32.conj().T) @ Xi

print(f"\n  Test on H_i generator:")
print(f"  Method 1 (Xi @ b^T @ Xi) vs Method 2 (Xi @ conj(b^dag) @ Xi):")
print(f"  Max difference: {np.max(np.abs(o_Hi_method1 - o_Hi_method2)):.2e}")

# What about pi(b*) = pi(b)^dag?
# H_i: q=i, q*=conjugate(i)=-i in the quaternion *-algebra.
# pi(-i) should be pi(H_{-i}) = -pi(H_i)
# pi(H_i)^dag = Hi_32^dag
# So pi(b*) = pi(b)^dag means Hi_32^dag = -Hi_32 (anti-Hermitian in matrix sense)
print(f"\n  H_i Hermitian check: max |H_i + H_i^dag| = {np.max(np.abs(Hi_32 + Hi_32.conj().T)):.2e}")
print(f"  (Should be 0 if anti-Hermitian, which means q*=-q for H_i)")

# Let's check: is Hi_32 anti-Hermitian? (i.e., H_i^dag = -H_i)
print(f"  H_i anti-Hermitian: max |H_i^dag + H_i| = {np.max(np.abs(Hi_32.conj().T + Hi_32)):.2e}")
print(f"  H_i is {'ANTI-HERMITIAN' if np.max(np.abs(Hi_32.conj().T + Hi_32)) < 1e-10 else 'NOT anti-Hermitian'}")

# Actually wait. pi is NOT a *-homomorphism because A_F acts via bimodule.
# The LEFT part diag(alpha, alpha_bar, q_2x2) IS a *-homomorphism.
# But the RIGHT part diag(1, m^dag) uses m^dag already, so:
# pi(lambda, q, m) = L(lambda, q) @ X @ R(m)
# pi(lambda*, q*, m*) = L(conj(lambda), q_bar, m^dag) @ X @ R(m^dag)
#                      = L^*(lambda, q) @ X @ R^*(m)
# where L^* and R^* are the representations of the *-algebra.
#
# For L: lambda -> diag(lambda, ...), so L(conj(lambda)) = conj(L(lambda))
#         when lambda is in the (0,0) position.
#   But q -> diag(alpha, alpha_bar, q_2x2), and q* -> diag(conj(alpha), conj(alpha_bar), q_2x2^dag)
#         = diag(alpha_bar, alpha, q_2x2^T.conj())
#         Hmm, this is getting complicated.
#
# Let me just check NUMERICALLY whether pi(b*) = pi(b)^dag.

print(f"\n{'=' * 76}")
print("CHECKING pi(b*) = pi(b)^dag FOR ALL GENERATORS")
print(f"{'=' * 76}")

# For each A_F generator, compute pi(b^*) and compare with pi(b)^dag.
# The *-operation on A_F:
#   C: lambda* = conj(lambda). C_Im: (i)* = -i. C_Re_proj: (projector)* = projector.
#   H: q* = q_bar (quaternion conjugate). H_i: i*=-i, H_j: j*=-j, H_k: k*=-k, H_1: 1*=1.
#   M_3: m* = m^dag. E_{ab}_Re: (E_{ab})* = E_{ba}. E_{ab}_Im: (iE_{ab})* = -iE_{ba}.

# Build the *-conjugate representation for each generator
AF_star_16 = []
AF_star_names = []

# C_Im: lambda=i -> lambda*=-i
L_CIm_star = np.diag([-1j, 1.0, 1.0, 1.0])
AF_star_16.append(build_bimodule_16(L_CIm_star, np.eye(4, dtype=complex)))
AF_star_names.append('C_Im*')

# C_Re_proj: projector is self-adjoint
L_CRe_proj = np.diag([1.0, 0.0, 0.0, 0.0])
AF_star_16.append(build_bimodule_16(L_CRe_proj, np.eye(4, dtype=complex)))
AF_star_names.append('C_Re_proj*')

# H_i*: q=i, q*=-i -> alpha=-i, alpha_bar=i, q_2x2=diag(-i, i)
L_Hi_star = np.diag([-1j, 1j, -1j, 1j])
AF_star_16.append(build_bimodule_16(L_Hi_star, np.eye(4, dtype=complex)))
AF_star_names.append('H_i*')

# H_j*: q=j, q*=-j -> alpha=0, alpha_bar=0, q_2x2=[[0,-1],[1,0]]
L_Hj_star = np.zeros((4, 4), dtype=complex)
L_Hj_star[2, 3] = -1.0; L_Hj_star[3, 2] = 1.0
AF_star_16.append(build_bimodule_16(L_Hj_star, np.eye(4, dtype=complex)))
AF_star_names.append('H_j*')

# H_k*: q=k, q*=-k -> alpha=0, alpha_bar=0, q_2x2=[[0,-i],[-i,0]]
L_Hk_star = np.zeros((4, 4), dtype=complex)
L_Hk_star[2, 3] = -1j; L_Hk_star[3, 2] = -1j
AF_star_16.append(build_bimodule_16(L_Hk_star, np.eye(4, dtype=complex)))
AF_star_names.append('H_k*')

# H_1*: self-adjoint
AF_star_16.append(build_bimodule_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
AF_star_names.append('H_1*')

# M_3 generators: m* = m^dag
# E_{ab}_Re: m=E_{ab} -> m*=E_{ba} -> m^{*dag}=E_{ab} -> R=diag(1, E_{ab})
# Wait: for M_3, pi(m) uses R=diag(1, m^dag). So pi(m*) uses R=diag(1, (m*)^dag)=diag(1, m).
# So pi(m*) = build_bimodule_16(I, diag(1, m)).
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            # m* = m^dag for M_3(C): (val * E_{ab})^dag = conj(val) * E_{ba}
            m_star = m_elem.conj().T
            # pi(m*): R = diag(1, (m*)^dag) = diag(1, m)  [since (m^dag)^dag = m]
            m_star_dag = m_star.conj().T  # = m_elem
            R_mstar = np.eye(4, dtype=complex)
            R_mstar[1:, 1:] = m_star_dag
            AF_star_16.append(build_bimodule_16(np.eye(4, dtype=complex), R_mstar))
            AF_star_names.append(f'M3_E{a}{b}_{part}*')

# Now compare pi(b*)_32 with pi(b)^dag_32
L_CRe_proj = np.diag([1.0, 0.0, 0.0, 0.0])
L_Hi = np.diag([1j, -1j, 1j, -1j])
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j

AF_gens_16_list = []
AF_names_list = []

# Rebuild the same list
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_gens_16_list.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names_list.append('C_Im')
AF_gens_16_list.append(build_bimodule_16(L_CRe_proj, np.eye(4, dtype=complex)))
AF_names_list.append('C_Re_proj')
AF_gens_16_list.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names_list.append('H_i')
AF_gens_16_list.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names_list.append('H_j')
AF_gens_16_list.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names_list.append('H_k')
AF_gens_16_list.append(build_bimodule_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
AF_names_list.append('H_1')
for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            m_dag = m_elem.conj().T
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_dag
            AF_gens_16_list.append(build_bimodule_16(np.eye(4, dtype=complex), R_m))
            AF_names_list.append(f'M3_E{a}{b}_{part}')

print(f"\n  Checking pi(b*) =? pi(b)^dag for each generator:")
max_star_diff = 0
for i in range(len(AF_gens_16_list)):
    pi_b = build_full_32(AF_gens_16_list[i])
    pi_bstar = build_full_32(AF_star_16[i])
    pi_b_dag = pi_b.conj().T

    diff = np.max(np.abs(pi_bstar - pi_b_dag))
    max_star_diff = max(max_star_diff, diff)
    status = 'MATCH' if diff < 1e-10 else f'DIFFER ({diff:.2e})'
    if diff > 1e-10:
        print(f"    {AF_names_list[i]:15s}: pi(b*) vs pi(b)^dag: {status}")

print(f"\n  Max |pi(b*) - pi(b)^dag|: {max_star_diff:.2e}")

if max_star_diff < 1e-10:
    print(f"  CONFIRMED: pi is a *-homomorphism (pi(b*) = pi(b)^dag)")
    print(f"  Therefore o(b) = Xi @ pi(b)^T @ Xi = Xi @ conj(pi(b)^dag) @ Xi")
    print(f"                 = Xi @ conj(pi(b*)) @ Xi = J pi(b*) J^{{-1}}")
    print(f"  The o-map IS CORRECT.")
else:
    print(f"  WARNING: pi is NOT a *-homomorphism!")
    print(f"  The o-map o(b) = Xi @ b^T @ Xi may NOT equal J pi(b*) J^{{-1}}.")
    print(f"  Need to use J pi(b*) J^{{-1}} = Xi @ conj(pi(b*)) @ Xi instead.")

    # Redo order-one with CORRECT o-map: o(b) = Xi @ conj(pi(b*)) @ Xi
    print(f"\n{'=' * 76}")
    print(f"RE-TESTING ORDER-ONE WITH CORRECT o-MAP")
    print(f"{'=' * 76}")

    # D_F (identity Yukawa, block-diagonal)
    D_F_16 = np.zeros((16, 16), dtype=complex)
    for j in range(3):
        D_F_16[j+1, j+4] = 1.0
        D_F_16[j+4, j+1] = 1.0
    D_F_32 = np.zeros((32, 32), dtype=complex)
    D_F_32[:16, :16] = D_F_16
    D_F_32[16:, 16:] = rho_minus(D_F_16)

    AF_gens_32_list = [build_full_32(g) for g in AF_gens_16_list]
    AF_star_32_list = [build_full_32(g) for g in AF_star_16]

    max_o1_correct = 0
    n_viol_correct = 0
    o1_factor_correct = {}

    AF_factors = (['C'] * 2 + ['H'] * 4 +
                  ['M3'] * 18)

    for i in range(len(AF_gens_32_list)):
        Da = D_F_32 @ AF_gens_32_list[i] - AF_gens_32_list[i] @ D_F_32
        for j in range(len(AF_star_32_list)):
            # CORRECT o-map: Xi @ conj(pi(b*)) @ Xi
            ob_correct = Xi @ np.conj(AF_star_32_list[j]) @ Xi
            dc = Da @ ob_correct - ob_correct @ Da
            err = np.max(np.abs(dc))
            max_o1_correct = max(max_o1_correct, err)
            if err > 1e-6:
                n_viol_correct += 1
            pair_key = f'[{AF_factors[i]}, o({AF_factors[j]})]'
            if pair_key not in o1_factor_correct:
                o1_factor_correct[pair_key] = 0.0
            o1_factor_correct[pair_key] = max(o1_factor_correct[pair_key], err)

    print(f"  Max |[[D_F, a], J pi(b*) J^-1]|: {max_o1_correct:.2e}")
    print(f"  Violations: {n_viol_correct} / {len(AF_gens_32_list)**2}")
    print(f"\n  By factor:")
    for pk in sorted(o1_factor_correct.keys()):
        v = o1_factor_correct[pk]
        s = 'PASS' if v < 1e-8 else f'FAIL ({v:.2e})'
        print(f"    {pk}: {s}")

    if max_o1_correct < 1e-8:
        print(f"\n  *** ORDER-ONE PASSES WITH CORRECT o-MAP! ***")
    else:
        print(f"\n  Order-one still fails with correct o-map.")


# =============================================================================
# PART 2: Also test with the SIMPLER o-map variants
# =============================================================================

print(f"\n{'=' * 76}")
print("TESTING ALL o-MAP VARIANTS")
print(f"{'=' * 76}")

AF_gens_32_list = [build_full_32(g) for g in AF_gens_16_list]

D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0
    D_F_16[j+4, j+1] = 1.0
D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = rho_minus(D_F_16)

def test_omap_variant(omap_fn, label):
    """Test order-one with a specific o-map."""
    max_err = 0
    for i in range(len(AF_gens_32_list)):
        Da = D_F_32 @ AF_gens_32_list[i] - AF_gens_32_list[i] @ D_F_32
        for j in range(len(AF_gens_32_list)):
            ob = omap_fn(AF_gens_32_list[j])
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            max_err = max(max_err, err)
    status = 'PASS' if max_err < 1e-8 else f'FAIL ({max_err:.2e})'
    print(f"  {label:50s}: {status}")
    return max_err

# Variant 1: o(b) = Xi @ b^T @ Xi (what we've been using)
test_omap_variant(lambda b: Xi @ b.T @ Xi, "o(b) = Xi @ b^T @ Xi")

# Variant 2: o(b) = Xi @ conj(b) @ Xi
test_omap_variant(lambda b: Xi @ np.conj(b) @ Xi, "o(b) = Xi @ conj(b) @ Xi")

# Variant 3: o(b) = Xi @ b^dag @ Xi
test_omap_variant(lambda b: Xi @ b.conj().T @ Xi, "o(b) = Xi @ b^dag @ Xi")

# Variant 4: o(b) = Xi @ b @ Xi (no conjugation at all)
test_omap_variant(lambda b: Xi @ b @ Xi, "o(b) = Xi @ b @ Xi")

# Variant 5: J pi(b*) J^{-1} with EXPLICIT b* (correct Connes formula)
AF_star_32_list = [build_full_32(g) for g in AF_star_16]

max_err_v5 = 0
for i in range(len(AF_gens_32_list)):
    Da = D_F_32 @ AF_gens_32_list[i] - AF_gens_32_list[i] @ D_F_32
    for j in range(len(AF_star_32_list)):
        ob = Xi @ np.conj(AF_star_32_list[j]) @ Xi
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        max_err_v5 = max(max_err_v5, err)
status = 'PASS' if max_err_v5 < 1e-8 else f'FAIL ({max_err_v5:.2e})'
print(f"  {'o(b) = Xi @ conj(pi(b*)) @ Xi (explicit b*)':50s}: {status}")

# Variant 6: Just b^dag (no Xi)
test_omap_variant(lambda b: b.conj().T, "o(b) = b^dag (no Xi)")

# Variant 7: o(b) = conj(b) (just complex conjugate)
test_omap_variant(lambda b: np.conj(b), "o(b) = conj(b)")

print(f"\n  Note: For a *-homomorphism, Xi @ b^T @ Xi = Xi @ conj(b^dag) @ Xi")
print(f"  So variants 1 and 5 should agree if pi is a *-homomorphism.")
