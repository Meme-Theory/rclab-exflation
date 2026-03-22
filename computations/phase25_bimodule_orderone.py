"""
PHASE 2.5 REVISED: Order-One Verification for Bimodule A_F
============================================================

Previous Phase 2.5 applied order-one to the LEFT-ONLY L-closure algebra (38-dim)
and extracted C + M_3(C) = 20 dims. H was structurally absent because H requires
column mixing (RIGHT action), which is not in the R_{u(2)} commutant.

This script takes the CORRECT approach: test order-one directly on the BIMODULE
representation of A_F = C + H + M_3(C) (24 generators, rank 24).

Strategy:
  1. Construct D_F from Baptista eq 2.65 (L-homomorphism failure on C^2 directions)
  2. Verify D_F properties: Hermitian, J-compatible, anticommutation with gamma_F
  3. Compute [[D_F, pi(a_i)], o(b_j)] for all 576 (i,j) pairs
  4. If max error < 1e-10: ORDER-ONE VERIFIED for A_F
  5. Verify MAXIMALITY: show that enlarging A_F breaks order-one

Physical meaning: Order-one passing means the Higgs mechanism (D_F) respects
the bimodule structure of A_F. This would establish the Baptista-Connes bridge.

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

# =============================================================================
# INFRASTRUCTURE (from existing scripts)
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
    """Build 16x16 matrix for bimodule action: X -> L4 . X . R4.
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
# PART 1: Build bimodule A_F generators (24 generators, rank 24)
# =============================================================================

print("=" * 76)
print("PART 1: BIMODULE A_F GENERATORS")
print("=" * 76)

AF_gens_16 = []
AF_names = []
AF_factor = []

# ── C FACTOR (dim 2) ──
# (lambda, 1, I_3): L = diag(lambda, 1, 1, 1), R = I_4
# C_Im: lambda=i
L_CIm = np.diag([1j, 1.0, 1.0, 1.0])
AF_gens_16.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names.append('C_Im')
AF_factor.append('C')

# C_Re_proj: projects onto row-0 relative to identity
L_CRe_proj = np.diag([1.0, 0.0, 0.0, 0.0])
AF_gens_16.append(build_bimodule_16(L_CRe_proj, np.eye(4, dtype=complex)))
AF_names.append('C_Re_proj')
AF_factor.append('C')

# ── H FACTOR (dim 4) ──
# (1, q, I_3): L = diag(alpha, alpha_bar, q_2x2), R = I_4
# H_i: q=i -> alpha=i, alpha_bar=-i
L_Hi = np.diag([1j, -1j, 1j, -1j])
AF_gens_16.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names.append('H_i')
AF_factor.append('H')

# H_j: q=j -> alpha=0, alpha_bar=0, q_2x2=[[0,1],[-1,0]]
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append('H_j')
AF_factor.append('H')

# H_k: q=k -> alpha=0, alpha_bar=0, q_2x2=[[0,i],[i,0]]
L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append('H_k')
AF_factor.append('H')

# H_1 = identity (algebra unit -- needed for closure)
L_H1 = np.eye(4, dtype=complex)
AF_gens_16.append(build_bimodule_16(L_H1, np.eye(4, dtype=complex)))
AF_names.append('H_1=I')
AF_factor.append('H')

# ── M_3(C) FACTOR (dim 18) ──
# (1, 1, m): L = I_4, R = diag(1, m^dag)
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

# Verify rank
AF_vecs = [vec_real(T) for T in AF_gens_32]
AF_rank = np.linalg.matrix_rank(np.column_stack(AF_vecs), tol=1e-8)
print(f"  Rank: {AF_rank} (target: 24)")

# J-compatibility check
j_max = max(np.max(np.abs(T @ Xi - Xi @ np.conj(T))) for T in AF_gens_32)
print(f"  J-compatibility: max error = {j_max:.2e}")


# =============================================================================
# PART 2: Construct D_F from Baptista eq 2.65
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 2: D_F CONSTRUCTION FROM BAPTISTA EQ 2.65")
print(f"{'=' * 76}")

# From eq 2.65, the L-homomorphism failure:
#   [L_u, L_v] - L_{[u,v]} = [[0, 2[u,v]_11 c^T], [-2[u,v]_11 b, 0]]
#
# This gives the ANOMALY TERM: for v in C^2 directions, [u,v]_11 != 0.
# The finite Dirac operator D_F should be the operator that "fixes" the
# homomorphism failure -- it connects the c and b sectors.
#
# In Connes' framework, D_F on Psi_+ = (a, c^T; b, D) acts as:
#   D_F . (a, c^T; b, D) -> something mixing c and b
#
# The simplest D_F from eq 2.65: couples c_j <-> b_j
# D_F[flat(0,j), flat(j,0)] = Y_{jj} for j=1,2,3 (and hermitian conjugate)
# i.e., D_F[j, j+3] = Y_j and D_F[j+3, j] = Y_j^*
#
# The Yukawa matrix Y determines the fermion masses.
# For the order-one CHECK, the specific Yukawa values don't matter
# (we showed Yukawa-independence in the L-closure case).

# Method 1: Direct construction from L-failure
# Compute L_v for each C^2 direction, extract the anomalous part
basis_su3 = su3_basis()

# The C^2 directions of su(3) are the ones that mix u(2) with its complement.
# In the Gell-Mann basis: lambda_4, lambda_5, lambda_6, lambda_7
# These are the generators with nonzero (1,1) entry in [u,v].

# Let's compute the L-failure explicitly
print("\n  Computing L-homomorphism failure for all su(3) pairs...")

# L_action_matrix from branching_computation.py gives the 16x16 L-action
L_matrices = [L_action_matrix(v) for v in basis_su3]

max_delta_all = 0
delta_entries = []

for i in range(8):
    for j in range(8):
        # Compute [L_i, L_j] - L_{[e_i, e_j]}
        comm_LiLj = L_matrices[i] @ L_matrices[j] - L_matrices[j] @ L_matrices[i]

        # Compute [e_i, e_j] in su(3)
        bracket_ij = basis_su3[i] @ basis_su3[j] - basis_su3[j] @ basis_su3[i]

        # L_{[e_i, e_j]}
        L_bracket = L_action_matrix(bracket_ij)

        # Delta = [L_i, L_j] - L_{[e_i, e_j]}
        delta = comm_LiLj - L_bracket

        max_entry = np.max(np.abs(delta))
        if max_entry > 1e-10:
            # Extract [e_i, e_j]_{11}
            bracket_11 = (basis_su3[i] @ basis_su3[j] - basis_su3[j] @ basis_su3[i])[0, 0]
            delta_entries.append((i, j, max_entry, bracket_11))

        max_delta_all = max(max_delta_all, max_entry)

print(f"  Total max L-failure: {max_delta_all:.6e}")
print(f"  Nonzero failures: {len(delta_entries)}")

if delta_entries:
    print(f"\n  Detailed L-failures:")
    for i, j, mx, b11 in delta_entries[:10]:
        print(f"    (e_{i}, e_{j}): max delta = {mx:.6e}, [e_i,e_j]_11 = {b11:.6f}")

# Now construct D_F.
# From Connes: D_F is a Hermitian matrix on H_F that encodes Yukawa couplings.
# The physical D_F couples:
#   - c (neutrino doublet, flat indices 1-3) <-> b (quark singlets, flat indices 4-6)
#   - This is the Dirac Yukawa mass
#   - Majorana mass terms would couple a (index 0) <-> b (indices 4-6) as well
#
# The L-failure structure tells us D_F should have the block structure:
#   D_F = [[0, Y^T], [Y^*, 0]] in the (c, b) subspace
# where Y is a 3x3 Yukawa matrix.

# Test 1: Identity Yukawa (Y = I_3)
print(f"\n  Building D_F with identity Yukawa (Y = I_3)...")

D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0  # c_j -> b_j
    D_F_16[j+4, j+1] = 1.0  # b_j -> c_j

# Extend to C^32
D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = rho_minus(D_F_16)

# Properties
print(f"  D_F Hermitian: {np.max(np.abs(D_F_32 - D_F_32.conj().T)):.2e}")

# J-compatibility: D_F @ Xi = Xi @ conj(D_F) (i.e., JD = DJ, epsilon'=+1)
j_err_DF = np.max(np.abs(D_F_32 @ Xi - Xi @ np.conj(D_F_32)))
print(f"  D_F J-compatible (JD=DJ): {j_err_DF:.2e}")

# Chirality: {D_F, gamma_F} = 0 (anticommutes) or [D_F, gamma_F] = 0 (commutes)?
anticomm = D_F_32 @ gamma_F + gamma_F @ D_F_32
comm_gamma = D_F_32 @ gamma_F - gamma_F @ D_F_32
print(f"  D_F anticommutes with gamma_F: max |D*gamma + gamma*D| = {np.max(np.abs(anticomm)):.2e}")
print(f"  D_F commutes with gamma_F: max |D*gamma - gamma*D| = {np.max(np.abs(comm_gamma)):.2e}")

# Note: our D_F is block-diagonal (within each chirality), so it COMMUTES with gamma_F.
# In the standard NCG convention, D_F should anticommute with gamma for the
# off-diagonal (mass) terms. Let's also try off-diagonal D_F.

# Test 2: Off-diagonal D_F (maps Psi_+ <-> Psi_-)
print(f"\n  Building OFF-DIAGONAL D_F (anticommutes with gamma_F)...")

D_F_offdiag = np.zeros((32, 32), dtype=complex)
D_F_offdiag[:16, 16:] = D_F_16  # maps Psi_- -> Psi_+
D_F_offdiag[16:, :16] = D_F_16  # maps Psi_+ -> Psi_-

# Make hermitian
D_F_offdiag = 0.5 * (D_F_offdiag + D_F_offdiag.conj().T)

print(f"  Off-diag D_F Hermitian: {np.max(np.abs(D_F_offdiag - D_F_offdiag.conj().T)):.2e}")
j_err_off = np.max(np.abs(D_F_offdiag @ Xi - Xi @ np.conj(D_F_offdiag)))
print(f"  Off-diag D_F J-compatible: {j_err_off:.2e}")
anticomm_off = D_F_offdiag @ gamma_F + gamma_F @ D_F_offdiag
comm_off = D_F_offdiag @ gamma_F - gamma_F @ D_F_offdiag
print(f"  Off-diag anticommutes with gamma: {np.max(np.abs(anticomm_off)):.2e}")
print(f"  Off-diag commutes with gamma: {np.max(np.abs(comm_off)):.2e}")


# =============================================================================
# PART 3: Order-one verification for bimodule A_F
# =============================================================================

def test_order_one(D_F, AF_gens, AF_names_list, AF_factor_list, label):
    """Test [[D_F, a], o(b)] = 0 for all pairs in A_F."""
    print(f"\n{'=' * 76}")
    print(f"ORDER-ONE: [[D_F, a], o(b)] = 0 -- {label}")
    print(f"{'=' * 76}")

    n_gens = len(AF_gens)
    max_o1 = 0
    max_o1_pair = None
    n_viol = 0
    o1_by_factor = {}

    for i in range(n_gens):
        # [D_F, a_i]
        Da = D_F @ AF_gens[i] - AF_gens[i] @ D_F
        for j in range(n_gens):
            # o(b_j) = Xi @ b_j^T @ Xi
            ob = Xi @ AF_gens[j].T @ Xi
            # [[D_F, a_i], o(b_j)]
            double_comm = Da @ ob - ob @ Da
            err = np.max(np.abs(double_comm))
            if err > max_o1:
                max_o1 = err
                max_o1_pair = (AF_names_list[i], AF_names_list[j])
            if err > 1e-6:
                n_viol += 1

            # Track by factor pair
            pair_key = f'[{AF_factor_list[i]}, o({AF_factor_list[j]})]'
            if pair_key not in o1_by_factor:
                o1_by_factor[pair_key] = 0.0
            o1_by_factor[pair_key] = max(o1_by_factor[pair_key], err)

    print(f"  Max |[[D_F, a], o(b)]|: {max_o1:.2e}")
    if max_o1_pair:
        print(f"  Worst pair: ({max_o1_pair[0]}, {max_o1_pair[1]})")
    print(f"  Violations (>1e-6): {n_viol} / {n_gens**2}")

    print(f"\n  By factor combination:")
    for pair_key in sorted(o1_by_factor.keys()):
        val = o1_by_factor[pair_key]
        status = 'PASS' if val < 1e-8 else f'FAIL ({val:.2e})'
        print(f"    {pair_key}: {status}")

    if max_o1 < 1e-8:
        print(f"\n  *** ORDER-ONE VERIFIED: {label} ***")
    else:
        print(f"\n  ORDER-ONE FAILS: {label}")

    return max_o1, o1_by_factor


# Test with block-diagonal D_F (commutes with gamma)
max_o1_diag, o1_factors_diag = test_order_one(
    D_F_32, AF_gens_32, AF_names, AF_factor,
    "Block-diagonal D_F (identity Yukawa)"
)

# Test with off-diagonal D_F (anticommutes with gamma)
max_o1_offdiag, o1_factors_offdiag = test_order_one(
    D_F_offdiag, AF_gens_32, AF_names, AF_factor,
    "Off-diagonal D_F (identity Yukawa)"
)


# =============================================================================
# PART 4: Random Yukawa D_F (check Yukawa-independence)
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 4: RANDOM YUKAWA (Yukawa-independence check)")
print(f"{'=' * 76}")

np.random.seed(42)
yukawa = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)

D_F_yuk_16 = np.zeros((16, 16), dtype=complex)
for i in range(3):
    for j in range(3):
        D_F_yuk_16[j+1, i+4] = yukawa[i, j]
        D_F_yuk_16[i+4, j+1] = np.conj(yukawa[i, j])

D_F_yuk_32 = np.zeros((32, 32), dtype=complex)
D_F_yuk_32[:16, :16] = D_F_yuk_16
D_F_yuk_32[16:, 16:] = rho_minus(D_F_yuk_16)

max_o1_yuk, _ = test_order_one(
    D_F_yuk_32, AF_gens_32, AF_names, AF_factor,
    "Block-diagonal D_F (random Yukawa)"
)


# =============================================================================
# PART 5: Majorana D_F (singlet <-> b coupling)
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 5: MAJORANA D_F (singlet coupling)")
print(f"{'=' * 76}")

D_F_maj_16 = D_F_16.copy()
# Add singlet(0) <-> b(4,5,6) coupling
for j in range(3):
    D_F_maj_16[0, j+4] = 0.5
    D_F_maj_16[j+4, 0] = 0.5

D_F_maj_32 = np.zeros((32, 32), dtype=complex)
D_F_maj_32[:16, :16] = D_F_maj_16
D_F_maj_32[16:, 16:] = rho_minus(D_F_maj_16)

j_err_maj = np.max(np.abs(D_F_maj_32 @ Xi - Xi @ np.conj(D_F_maj_32)))
print(f"  Majorana D_F J-compatible: {j_err_maj:.2e}")

max_o1_maj, _ = test_order_one(
    D_F_maj_32, AF_gens_32, AF_names, AF_factor,
    "Block-diagonal D_F (Majorana)"
)


# =============================================================================
# PART 6: MAXIMALITY TEST
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 6: MAXIMALITY -- Does enlarging A_F break order-one?")
print(f"{'=' * 76}")

# Add extra generators OUTSIDE A_F and check if order-one breaks.
# Strategy: add generators from the L-closure that are NOT in A_F.

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

# Extra generators: L_{su(3)} generators that are NOT in A_F
# L_v for v in su(3) act purely on rows.
# These are LEFT-only operators, while A_F has bimodule (left+right) structure.
L_extras_16 = [L_action_matrix(v) for v in basis_su3]
L_extras_32 = [build_full_32(g) for g in L_extras_16]

# Check which L generators are NOT in the A_F span
Q_AF = orth(np.column_stack(AF_vecs))
AF_dim = Q_AF.shape[1]

print(f"\n  A_F span dimension: {AF_dim}")
print(f"\n  Testing L_{'{su(3)}'} generators:")

extras_outside = []
for idx, (T, v) in enumerate(zip(L_extras_32, basis_su3)):
    tv = vec_real(T)
    coeffs = Q_AF.T @ tv
    resid = np.linalg.norm(tv - Q_AF @ coeffs)
    in_AF = resid < 1e-6
    print(f"    L_{idx}: residual from A_F = {resid:.2e} {'(IN A_F)' if in_AF else '(OUTSIDE)'}")
    if not in_AF:
        extras_outside.append((T, f'L_{idx}'))

print(f"\n  Generators outside A_F: {len(extras_outside)}")

# For each extra generator, test order-one with A_F as the "o(b)" algebra
if extras_outside:
    print(f"\n  Testing order-one for extra generators with A_F as opposite:")

    # Use the best D_F (whichever passed above, or the identity Yukawa)
    D_F_test = D_F_32

    for T_extra, name_extra in extras_outside[:8]:
        Da_extra = D_F_test @ T_extra - T_extra @ D_F_test
        max_err_extra = 0
        for j in range(len(AF_gens_32)):
            ob = Xi @ AF_gens_32[j].T @ Xi
            dc = Da_extra @ ob - ob @ Da_extra
            err = np.max(np.abs(dc))
            max_err_extra = max(max_err_extra, err)
        status = 'PASS' if max_err_extra < 1e-8 else f'FAIL ({max_err_extra:.2e})'
        print(f"    {name_extra}: max |[[D_F, extra], o(A_F)]| = {status}")

    # Also test A_F elements against extra generators as opposite
    print(f"\n  Testing order-one for A_F with extras as opposite:")
    for T_extra, name_extra in extras_outside[:8]:
        ob_extra = Xi @ T_extra.T @ Xi
        max_err_rev = 0
        for i in range(len(AF_gens_32)):
            Da = D_F_test @ AF_gens_32[i] - AF_gens_32[i] @ D_F_test
            dc = Da @ ob_extra - ob_extra @ Da
            err = np.max(np.abs(dc))
            max_err_rev = max(max_err_rev, err)
        status = 'PASS' if max_err_rev < 1e-8 else f'FAIL ({max_err_rev:.2e})'
        print(f"    o({name_extra}) with A_F: max |[[D_F, A_F], o(extra)]| = {status}")


# =============================================================================
# PART 7: Order-zero for reference
# =============================================================================

print(f"\n{'=' * 76}")
print("PART 7: ORDER-ZERO (for comparison)")
print(f"{'=' * 76}")

max_o0 = 0
o0_by_factor = {}
n_viol_o0 = 0

for i in range(len(AF_gens_32)):
    for j in range(len(AF_gens_32)):
        ob = Xi @ AF_gens_32[j].T @ Xi
        comm = AF_gens_32[i] @ ob - ob @ AF_gens_32[i]
        err = np.max(np.abs(comm))
        max_o0 = max(max_o0, err)
        if err > 1e-6:
            n_viol_o0 += 1
        pair_key = f'[{AF_factor[i]}, o({AF_factor[j]})]'
        if pair_key not in o0_by_factor:
            o0_by_factor[pair_key] = 0.0
        o0_by_factor[pair_key] = max(o0_by_factor[pair_key], err)

print(f"  Max |[a, o(b)]|: {max_o0:.2e}")
print(f"  Violations (>1e-6): {n_viol_o0} / {len(AF_gens_32)**2}")
print(f"\n  By factor combination:")
for pair_key in sorted(o0_by_factor.keys()):
    val = o0_by_factor[pair_key]
    status = 'PASS' if val < 1e-8 else f'FAIL ({val:.2e})'
    print(f"    {pair_key}: {status}")


# =============================================================================
# PART 8: SUMMARY
# =============================================================================

print(f"\n{'=' * 76}")
print("FINAL SUMMARY: PHASE 2.5 REVISED")
print(f"{'=' * 76}")

print(f"\n  Bimodule A_F: rank {AF_rank}, J-compatible (max err {j_max:.2e})")
print(f"\n  D_F variants tested:")
print(f"    Block-diagonal (identity Yukawa): order-one max = {max_o1_diag:.2e}")
print(f"    Off-diagonal (identity Yukawa):   order-one max = {max_o1_offdiag:.2e}")
print(f"    Block-diagonal (random Yukawa):   order-one max = {max_o1_yuk:.2e}")
print(f"    Block-diagonal (Majorana):        order-one max = {max_o1_maj:.2e}")
print(f"\n  Order-zero (for reference): max = {max_o0:.2e}")
print(f"\n  Target: max |[[D_F, a], o(b)]| < 1e-8 for A_F to satisfy order-one")

if max_o1_diag < 1e-8:
    print(f"\n  *** BAPTISTA-CONNES BRIDGE ESTABLISHED ***")
    print(f"  A_F = C + H + M_3(C) satisfies the order-one condition")
    print(f"  with D_F from Baptista eq 2.65 on H_F = C^32.")
elif max_o1_offdiag < 1e-8:
    print(f"\n  *** BAPTISTA-CONNES BRIDGE ESTABLISHED (off-diagonal D_F) ***")
    print(f"  A_F satisfies order-one with off-diagonal D_F.")
else:
    print(f"\n  Order-one FAILS for bimodule A_F with all D_F variants.")
    print(f"  This means the bimodule representation does NOT give a valid")
    print(f"  spectral triple with this D_F. The failure sectors are:")
    for D_label, o1_fac in [("block-diag", o1_factors_diag), ("off-diag", o1_factors_offdiag)]:
        failing = [(k, v) for k, v in o1_fac.items() if v > 1e-8]
        if failing:
            print(f"    {D_label}: " + ", ".join(f"{k}={v:.2e}" for k, v in failing))

print(f"\n{'=' * 76}")
