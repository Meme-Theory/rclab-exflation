"""
PHASE 2.5 DIRAC STRUCTURE: Understanding D_F and the order-one condition
========================================================================

The order-one condition [[D_F, a], o(b)] = 0 FAILS for all factor pairs.
This script investigates WHY by examining:

1. The precise structure of D_F on the 4x4 matrix representation Psi = (nu, c, b, D)^T
2. How LEFT and RIGHT actions interact with D_F
3. Whether the correct D_F (from Baptista eq 2.65) differs from what we constructed
4. Whether Yukawa coupling constants Y_{ij} can rescue order-one

The key insight: in Connes' NCG, D_F is NOT arbitrary. It is constrained to satisfy
order-one BY CONSTRUCTION. Here we check if any D_F coupling c<->b can satisfy it
for the bimodule A_F.

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

np.set_printoptions(precision=6, linewidth=140, suppress=True)


# =============================================================================
# Flat index convention for Psi_+ (16-dim)
# =============================================================================
# Psi_+ is a 4x4 matrix with rows (nu, c1, c2, c3) and columns (0=singlet, 1,2,3=color)
# flat_idx maps (row, col) -> {0,...,15}:
#   (0,0)=0, (0,1)=1, (0,2)=2, (0,3)=3       [nu_R, c^1, c^2, c^3]
#   (1,0)=4, (2,0)=5, (3,0)=6                  [b_1, b_2, b_3]  (singlet column)
#   (1,1)=7, (1,2)=8, (1,3)=9                  [D^1_1, D^1_2, D^1_3]
#   (2,1)=10,(2,2)=11,(2,3)=12                 [D^2_1, D^2_2, D^2_3]
#   (3,1)=13,(3,2)=14,(3,3)=15                 [D^3_1, D^3_2, D^3_3]

def flat_idx(row, col):
    if row == 0 and col == 0: return 0
    if row == 0: return col
    if col == 0: return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4, R4):
    """Build 16x16 matrix for bimodule: X -> L4 . X . R4"""
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
# PART 1: Physical meaning of D_F entries
# =============================================================================
print("=" * 76)
print("PART 1: D_F STRUCTURE IN MATRIX REPRESENTATION")
print("=" * 76)

# Baptista eq 2.65: L_u fails for u in C^2 (indices 5-8 of su(3)):
# [L_u, L_v] - L_{[u,v]} = 2[u,v]_{11} * (something on c and b blocks)
# The c-sector has (0,j) for j=1,2,3 (flat indices 1,2,3)
# The b-sector has (i,0) for i=1,2,3 (flat indices 4,5,6)

# D_F = identity Yukawa coupling c <-> b:
D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0  # c_j -> b_j (row 0, col j+1) <-> (row j+1, col 0)
    D_F_16[j+4, j+1] = 1.0  # b_j -> c_j

print("\nD_F couples: c-sector (indices 1,2,3) <-> b-sector (indices 4,5,6)")
print("In matrix notation: Psi[0,j] <-> Psi[j,0] (transposition within c/b!)")
print("\nD_F_16 nonzero entries:")
for r in range(16):
    for c in range(16):
        if abs(D_F_16[r, c]) > 1e-10:
            # Decode flat indices back to (row, col)
            for i in range(4):
                for j in range(4):
                    if flat_idx(i, j) == r:
                        ri, rj = i, j
                    if flat_idx(i, j) == c:
                        ci, cj = i, j
            print(f"  D_F[{r},{c}] = {D_F_16[r,c]:.1f}   "
                  f"  Psi({ri},{rj}) -> Psi({ci},{cj})")


# =============================================================================
# PART 2: Why LEFT action fails order-one
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 2: STRUCTURE OF LEFT AND RIGHT ACTIONS ON c AND b SECTORS")
print(f"{'=' * 76}")

# LEFT action: X -> L . X (acts on rows)
# On c-sector (row 0): L affects which row contributions mix
# On b-sector (col 0): L acts directly on rows 1,2,3

# RIGHT action: X -> X . R (acts on columns)
# On c-sector (row 0, cols 1,2,3): R acts on columns directly
# On b-sector (col 0): R doesn't touch these (col 0 is singlet)

# H_i = diag(i, -i, i, -i) acts LEFT only
L_Hi = np.diag([1j, -1j, 1j, -1j])
Hi_16 = build_bimodule_16(L_Hi, np.eye(4))

print("\nH_i (left action) on specific indices:")
for idx in [1, 2, 3, 4, 5, 6]:
    diag_val = Hi_16[idx, idx]
    if abs(diag_val) > 1e-10:
        print(f"  H_i[{idx},{idx}] = {diag_val:.4f}")

# The key: D_F swaps c_j <-> b_j, but H_i acts DIFFERENTLY on c and b!
# On c_j (flat index j+1): H_i[j+1,j+1] = eigenvalue from row 0 of L_Hi
# Wait, that's not right. Let me trace through carefully.

print("\nDetailed trace for H_i:")
print("  c-sector (row=0, col=j): L acts on row index only")
print("    H_i on c_1 (flat 1): L_Hi[0,0] * I = i * c_1")
print("    H_i on c_2 (flat 2): L_Hi[0,0] * I = i * c_2")
print("    H_i on c_3 (flat 3): L_Hi[0,0] * I = i * c_3")
print("  b-sector (row=j, col=0): L acts on row index j")
print("    H_i on b_1 (flat 4): L_Hi[1,1] * I = -i * b_1")
print("    H_i on b_2 (flat 5): L_Hi[2,2] * I = i * b_2")
print("    H_i on b_3 (flat 6): L_Hi[3,3] * I = -i * b_3")

# Verify
print("\nNumerical verification:")
for idx, name in [(1,'c_1'), (2,'c_2'), (3,'c_3'), (4,'b_1'), (5,'b_2'), (6,'b_3')]:
    print(f"  {name} (flat {idx}): H_i eigenvalue = {Hi_16[idx,idx]:.4f}")

print("\n*** KEY: D_F maps c_j -> b_j, but H_i has DIFFERENT eigenvalues on them! ***")
print("  c_1: eigenvalue +i     b_1: eigenvalue -i    MISMATCH (diff = 2i)")
print("  c_2: eigenvalue +i     b_2: eigenvalue +i    MATCH")
print("  c_3: eigenvalue +i     b_3: eigenvalue -i    MISMATCH (diff = 2i)")
print("\n  [D_F, H_i] is nonzero precisely because of these mismatches.")
print("  This is not a bug -- it's how the LEFT action (which distinguishes c and b")
print("  via different row indices) interacts with D_F (which swaps them).")


# =============================================================================
# PART 3: What order-one MEANS for the bimodule
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 3: ORDER-ONE IN THE BIMODULE CONTEXT")
print(f"{'=' * 76}")

# In Connes' NCG, the order-one condition [[D, a], JbJ^{-1}] = 0 means:
# "D is a first-order differential operator with respect to the bimodule structure"
#
# For our bimodule Psi -> L.Psi.R:
# pi(a) = L_a . Psi (left multiplication)
# o(b) = Psi . R_b^dag (right multiplication by conjugate transpose)
#
# ORDER-ONE means: the "derivative" [D, a] commutes with right multiplications.
# In differential geometry: d(f.omega) = df . omega + f . d(omega)
# Leibniz rule for the RIGHT module structure.
#
# For a MATRIX Psi acted on by L from left and R from right:
# [D_F, L_a] . R_b^dag = R_b^dag . [D_F, L_a]
# i.e., [D_F, L_a] must commute with ALL right multiplications.

print("\nOrder-one means: [D_F, pi(a)] commutes with ALL o(b).")
print("Equivalently: [D_F, L_a otimes I] commutes with [I otimes R_b^dag]")
print("\nBut [D_F, L_a otimes I] = [D_F, L_a] otimes I only if D_F = D_L otimes I.")
print("Our D_F couples c<->b which mixes ROWS -- it IS a left-type operator.")
print("So [D_F, L_a] is a left-type operator and should commute with right actions...")
print("\nWait -- let me check if [D_F, L_a] is actually a pure left operator.")

# Check: is [D_F, H_i] = L_something otimes I?
# A pure left operator satisfies: gen[flat(i,j), flat(k,l)] = L[i,k] * delta[l,j]
Da = D_F_16 @ Hi_16 - Hi_16 @ D_F_16
print("\n[D_F, H_i] -- check if it's a pure LEFT operator (L otimes I):")
is_left = True
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                fi = flat_idx(i, j)
                fk = flat_idx(k, l)
                val = Da[fi, fk]
                if abs(val) > 1e-10:
                    if l != j:
                        is_left = False
                        print(f"  NOT left: Da[({i},{j}),({k},{l})] = {val:.4f} but l={l} != j={j}")

if is_left:
    # Extract L matrix
    L_extracted = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for k in range(4):
            L_extracted[i, k] = Da[flat_idx(i, 0), flat_idx(k, 0)]
    print("  YES: [D_F, H_i] = L_extracted otimes I")
    print(f"  L_extracted:\n{L_extracted}")

# Similarly check if [D_F, M3_E00_Re] is a pure RIGHT operator
m_elem = np.zeros((3, 3), dtype=complex)
m_elem[0, 0] = 1.0
R_m = np.eye(4, dtype=complex)
R_m[1:, 1:] = m_elem.conj().T
M3_16 = build_bimodule_16(np.eye(4), R_m)
Da_M3 = D_F_16 @ M3_16 - M3_16 @ D_F_16

print(f"\n[D_F, M3_E00_Re] -- check if it's a pure RIGHT operator (I otimes R):")
is_right = True
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                fi = flat_idx(i, j)
                fk = flat_idx(k, l)
                val = Da_M3[fi, fk]
                if abs(val) > 1e-10:
                    if i != k:
                        is_right = False
                        # Only print first few violations
                        if sum(1 for _ in range(1)) <= 5:
                            print(f"  NOT right: Da[({i},{j}),({k},{l})] = {val:.4f} but i={i} != k={k}")

if is_right:
    print("  YES: it's a pure right operator")
else:
    # Check if it's left
    is_left2 = True
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    fi = flat_idx(i, j)
                    fk = flat_idx(k, l)
                    val = Da_M3[fi, fk]
                    if abs(val) > 1e-10 and l != j:
                        is_left2 = False
    if is_left2:
        print("  It IS a left operator!")
    else:
        print("  It's NEITHER purely left NOR purely right -- it's MIXED!")


# =============================================================================
# PART 4: D_F AS LEFT OPERATOR -- THE FUNDAMENTAL ISSUE
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 4: IS D_F ITSELF A LEFT OPERATOR?")
print(f"{'=' * 76}")

# Check: is D_F = L_D otimes I?
print("\nChecking if D_F is a pure left operator:")
is_left_DF = True
violations = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                fi = flat_idx(i, j)
                fk = flat_idx(k, l)
                val = D_F_16[fi, fk]
                if abs(val) > 1e-10:
                    if l != j:
                        is_left_DF = False
                        violations += 1
                        if violations <= 10:
                            print(f"  NOT left: D_F[({i},{j}),({k},{l})] = {val:.4f}, "
                                  f"l={l} != j={j}")

if is_left_DF:
    print("  D_F IS a pure left operator!")
    L_D = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for k in range(4):
            L_D[i, k] = D_F_16[flat_idx(i, 0), flat_idx(k, 0)]
    print(f"  L_D:\n{L_D}")

    # If D_F = L_D otimes I, then [D_F, L_a otimes I] = [L_D, L_a] otimes I
    # which is again a left operator.
    # And o(b) = I otimes R_b^dag is a right operator.
    # Left and right operators COMMUTE on tensor products!
    # So order-one should be AUTOMATICALLY satisfied!

    print("\n  IF D_F = L_D otimes I, order-one is AUTOMATIC!")
    print("  Because [D_F, L_a otimes I] = [L_D, L_a] otimes I")
    print("  and o(b) = I otimes R_b^dag commutes with all left operators.")
    print("\n  But our computation shows FAILURE. This means either:")
    print("  1. D_F is NOT a pure left operator")
    print("  2. The bimodule structure is not a simple tensor product")
    print("  3. The flat indexing mixes left and right")

else:
    print(f"\n  D_F is NOT a pure left operator ({violations} violations)")
    print("  D_F couples c_j (row=0, col=j) to b_j (row=j, col=0)")
    print("  This is a c<->b coupling that acts on the MATRIX structure of Psi")
    print("  It cannot be written as L otimes I or I otimes R")
    print("\n  THIS is why order-one fails: D_F 'transposes' part of the matrix,")
    print("  which is neither a left nor right action.")


# =============================================================================
# PART 5: WHAT KIND OF OPERATOR IS D_F?
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 5: D_F AS A TRANSPOSE/FLIP OPERATOR")
print(f"{'=' * 76}")

# D_F maps Psi[0,j] -> Psi[j,0] and vice versa for j=1,2,3
# This is literally a PARTIAL TRANSPOSE of the matrix!
# In the bimodule M_4(C), the partial transpose T_{13} sends:
# e_{0j} -> e_{j0} (and vice versa, if we restrict to the 3 values j=1,2,3)

# This is known in NCG! The Dirac operator for the finite spectral triple
# IS supposed to be this kind of "off-diagonal" operator that mixes L and R.
# In Connes-Chamseddine, D_F has exactly this structure.

# Let's write D_F in terms of standard matrix units:
print("\nD_F in terms of matrix units E_{ij} of M_4(C):")
print("  D_F = sum_{j=1}^{3} (E_{0j} otimes E_{j0} + E_{j0} otimes E_{0j})")
print("  where the first index is row action, second is column action.")
print("\n  More precisely, D_F[flat(0,j), flat(j,0)] = 1 means")
print("  D_F maps the entry at position (0,j) to position (j,0)")
print("  This is NOT L otimes I or I otimes R!")
print("  It's a MIXED operator: sum_j L_{E_{j0}} * R_{E_{0j}} + h.c.")

# Verify: D_F = sum_j L_{E_{j0}} R_{E_{0j}} + L_{E_{0j}} R_{E_{j0}}
print("\nVerification:")
D_check = np.zeros((16, 16), dtype=complex)
for j in range(1, 4):
    L_ej0 = np.zeros((4, 4), dtype=complex)
    L_ej0[j, 0] = 1.0
    R_e0j = np.zeros((4, 4), dtype=complex)
    R_e0j[j, 0] = 1.0  # R acts as R^dag on Psi, so R_{E_{0j}} means column j -> col 0
    # Actually, the bimodule action is X -> L.X.R where R is the RIGHT multiplier
    # D_F maps Psi[0,j] -> Psi[j,0]: this requires L_{j,0} and R to move column j to column 0

    # Let me think more carefully:
    # flat(0,j) -> flat(j,0) means Psi_{0j} -> Psi_{j0}
    # L . Psi . R maps Psi_{kl} -> sum L_{ik} R_{lj'} Psi_{kl} at position (i,j')
    # We want (i=j, j'=0): L_{jk} R_{l,0} Psi_{kl} picks out k=0, l=j
    # So L[j,0] * R[j,0] = 1 -> gives the entry at (j,0)
    # But R here acts as column multiplier: X -> X . R
    # X.R at position (j, 0) = sum_l Psi_{jl} R_{l0}
    # We want to get contribution from Psi_{0j}:
    # At position (j,0): sum_l Psi_{jl} R_{l0} ... no, this acts on row j, not row 0

    # The tensor product decomposition is:
    # D_F = sum_j |e_j><e_0| otimes |e_0><e_j| + |e_0><e_j| otimes |e_j><e_0|
    # where first factor acts LEFT (on rows) and second acts RIGHT (on columns)

    Lj0 = np.zeros((4, 4), dtype=complex)
    Lj0[j, 0] = 1.0  # |e_j><e_0|
    R0j = np.zeros((4, 4), dtype=complex)
    R0j[0, j] = 1.0  # |e_0><e_j| acting on right: X . |e_0><e_j| keeps col j, puts in col 0
    # Wait. RIGHT action: X -> X . R. Entry (i, j') of X.R = sum_l X_{il} R_{lj'}
    # For R = |e_0><e_j|: R_{lj'} = delta_{l0} delta_{j'j}
    # (X.R)_{ij'} = X_{i0} delta_{j'j}
    # So X.R only has nonzero in column j, equal to column-0 of X.
    # That's not right for our purpose.

    # D_F: Psi_{0j} -> Psi_{j0}.
    # In the bimodule, X -> L.X.R maps X_{kl} -> sum_{k',l'} L_{ik'} X_{k'l'} R_{l'j'}
    #                                            at (i,j')
    # We need: contribution to (j,0) from (0,j) = L_{j,0} * R_{j,0}
    # Contribution to (0,j) from (j,0) = L_{0,j} * R_{0,j}

    pass

# Let me just verify numerically using tensor product construction:
print("\nNumerical construction: D_F as sum of L otimes R terms:")
D_reconstruct = np.zeros((16, 16), dtype=complex)
for j in range(1, 4):
    # Term 1: |j><0| acting left, column-swap acting right
    # Psi_{0,j} -> Psi_{j,0}:
    # At flat(j,0), we need contribution from flat(0,j)
    # Using bimodule: (L.X.R)_{jk'} for k'=0 needs X_{0,l} R_{l,0}
    # With L = E_{j0}: L_{j,0}=1, so picks row 0 of X: X_{0,l}
    # With R = E_{j0}: R_{l,0} = delta_{lj}, so picks X_{0,j}
    # Result: contribution = X_{0,j} at position (j,0). YES!

    L_term = np.zeros((4, 4), dtype=complex)
    L_term[j, 0] = 1.0  # E_{j,0}
    R_term = np.zeros((4, 4), dtype=complex)
    R_term[j, 0] = 1.0  # E_{j,0}
    D_reconstruct += build_bimodule_16(L_term, R_term)

    # Term 2: Psi_{j,0} -> Psi_{0,j}: hermitian conjugate
    L_term2 = np.zeros((4, 4), dtype=complex)
    L_term2[0, j] = 1.0  # E_{0,j}
    R_term2 = np.zeros((4, 4), dtype=complex)
    R_term2[0, j] = 1.0  # E_{0,j}
    D_reconstruct += build_bimodule_16(L_term2, R_term2)

err_recon = np.max(np.abs(D_reconstruct - D_F_16))
print(f"  |D_reconstruct - D_F_16| = {err_recon:.2e}")

if err_recon < 1e-10:
    print("\n  CONFIRMED: D_F = sum_{j=1}^{3} [L_{E_j0} R_{E_j0} + L_{E_0j} R_{E_0j}]")
    print("  D_F is a SUM OF TENSOR PRODUCTS of L and R operators!")
    print("  It is NOT a pure left or pure right operator.")
    print("\n  In NCG language: D_F is a MIXED first-order operator.")
    print("  The order-one condition [[D_F, a], JbJ^{-1}] = 0 constrains which")
    print("  (a, b) pairs are compatible with this particular D_F.")
else:
    print(f"\n  Reconstruction FAILED (error {err_recon:.2e})")
    print("  Need to find the correct tensor decomposition.")


# =============================================================================
# PART 6: When does order-one hold for tensor-decomposed D_F?
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 6: ORDER-ONE CONDITION FOR D_F = SUM L_alpha R_alpha")
print(f"{'=' * 76}")

# D_F = sum_alpha L_alpha otimes R_alpha
# [D_F, a otimes 1] = sum_alpha [L_alpha, a] otimes R_alpha
# [[D_F, a otimes 1], 1 otimes b^dag] = sum_alpha [L_alpha, a] otimes [R_alpha, b^dag]
#
# For this to be ZERO for all a, b, we need:
# sum_alpha [L_alpha, a] otimes [R_alpha, b^dag] = 0 for all a in A_L, b in A_R
#
# This does NOT factor: individual terms [L_alpha, a] otimes [R_alpha, b^dag]
# can be nonzero, but they must CANCEL in the sum.
#
# For our D_F: alpha = j (j=1,2,3)
# L_alpha = E_{j0}, R_alpha = E_{j0} (for the first set of terms)
#
# [E_{j0}, a_L] depends on the LEFT component of a
# [E_{j0}, b_R^dag] depends on the RIGHT component of b

# Let's compute explicitly for a = H_i (left), b = H_i (right should be identity)
# H_i has L_Hi = diag(i, -i, i, -i), R = I

# [E_{j0}, L_Hi] = E_{j0} L_Hi - L_Hi E_{j0}
# E_{j0} L_Hi: (E_{j0})_{ik} (L_Hi)_{kl} = delta_{ij} delta_{k0} (L_Hi)_{kl}
#            = delta_{ij} (L_Hi)_{0l}
# L_Hi E_{j0}: (L_Hi)_{ik} delta_{kj} delta_{l0} = (L_Hi)_{ij} delta_{l0}
# So [E_{j0}, L_Hi]_{il} = delta_{ij} (L_Hi)_{0l} - (L_Hi)_{ij} delta_{l0}

L_Hi = np.diag([1j, -1j, 1j, -1j])
for j in range(1, 4):
    E_j0 = np.zeros((4, 4), dtype=complex)
    E_j0[j, 0] = 1.0
    comm = E_j0 @ L_Hi - L_Hi @ E_j0
    if np.max(np.abs(comm)) > 1e-10:
        print(f"  [E_{j}0, L_Hi] nonzero entries:")
        for r in range(4):
            for c in range(4):
                if abs(comm[r, c]) > 1e-10:
                    print(f"    [{r},{c}] = {comm[r,c]:.4f}")

# For o(b): when b has only RIGHT component (M_3(C)), b^dag = R_b^dag on Psi_+
# When b has only LEFT component (C or H), b^dag still acts LEFT (as dagger)

print("\n  For H_i (left-only action), o(H_i)_++ = H_i_16^dag")
print("  H_i is diagonal with eigenvalues on c/b sectors:")
Hi_16_dag = Hi_16.conj().T
print(f"  H_i^dag diagonal on {[1,2,3,4,5,6]}:")
for idx in [1, 2, 3, 4, 5, 6]:
    print(f"    [{idx}] = {Hi_16_dag[idx,idx]:.4f}")

# The order-one double commutator:
# [[D_F, H_i], H_i^dag] on Psi_+
# = [sum_j [L_{Ej0} R_{Ej0}, H_i] + h.c., H_i^dag]
#
# Since H_i = L_Hi otimes I and R_{Ej0} commutes with I:
# [L_{Ej0} R_{Ej0}, L_Hi otimes I] = [L_{Ej0}, L_Hi] R_{Ej0} otimes I
#                                     + L_{Ej0} [R_{Ej0}, I] ... = 0
# Wait, that's not right for the bimodule. In the bimodule,
# L_{Ej0} R_{Ej0} is NOT the tensor product L otimes R in the usual sense.
# The bimodule action X -> L.X.R has:
# (L_{Ej0} R_{Ej0})(X) = E_{j0} . X . E_{j0}

# And H_i acts as: H_i(X) = L_Hi . X . I = L_Hi . X
# So [D_F, H_i](X) = D_F(L_Hi . X) - L_Hi . D_F(X)
#                   = sum_j E_{j0}(L_Hi X)E_{j0} + E_{0j}(L_Hi X)E_{0j}
#                     - L_Hi [sum_j E_{j0} X E_{j0} + E_{0j} X E_{0j}]
#                   = sum_j [E_{j0} L_Hi - L_Hi E_{j0}] X E_{j0}
#                     + sum_j [E_{0j} L_Hi - L_Hi E_{0j}] X E_{0j}
#                   = sum_j [E_{j0}, L_Hi] . X . E_{j0}
#                     + sum_j [E_{0j}, L_Hi] . X . E_{0j}

# Then for o(H_i) = H_i^dag (which on Psi_+ is L_Hi^dag):
# [[D_F, H_i], o(H_i)](X) = [D_F, H_i](L_Hi^dag X) - L_Hi^dag [D_F, H_i](X)
# = sum_j [E_{j0}, L_Hi](L_Hi^dag X) E_{j0} - L_Hi^dag [E_{j0}, L_Hi] X E_{j0}
#   + similar E_{0j} terms
# = sum_j [[E_{j0}, L_Hi], L_Hi^dag] X E_{j0} + [[E_{0j}, L_Hi], L_Hi^dag] X E_{0j}

# So the double commutator picks up [[E_{j0}, L_Hi], L_Hi^dag] as the LEFT factor
# and E_{j0} or E_{0j} as the RIGHT factor.

print(f"\n{'=' * 76}")
print("PART 7: EXPLICIT DOUBLE COMMUTATOR DECOMPOSITION")
print(f"{'=' * 76}")

# [[E_{j0}, L_Hi], L_Hi^dag] for each j:
L_Hi_dag = L_Hi.conj().T  # = diag(-i, i, -i, i)
print("\nDouble commutators [[E_{j0}, L_Hi], L_Hi^dag]:")
for j in range(1, 4):
    E_j0 = np.zeros((4, 4), dtype=complex)
    E_j0[j, 0] = 1.0
    inner = E_j0 @ L_Hi - L_Hi @ E_j0
    outer = inner @ L_Hi_dag - L_Hi_dag @ inner
    if np.max(np.abs(outer)) > 1e-10:
        print(f"  j={j}: [[E_{j}0, L_Hi], L_Hi^dag] =")
        for r in range(4):
            for c in range(4):
                if abs(outer[r, c]) > 1e-10:
                    print(f"    [{r},{c}] = {outer[r,c]:.4f}")
    else:
        print(f"  j={j}: ZERO")

print("\nDouble commutators [[E_{0j}, L_Hi], L_Hi^dag]:")
for j in range(1, 4):
    E_0j = np.zeros((4, 4), dtype=complex)
    E_0j[0, j] = 1.0
    inner = E_0j @ L_Hi - L_Hi @ E_0j
    outer = inner @ L_Hi_dag - L_Hi_dag @ inner
    if np.max(np.abs(outer)) > 1e-10:
        print(f"  j={j}: [[E_{0j}, L_Hi], L_Hi^dag] =")
        for r in range(4):
            for c in range(4):
                if abs(outer[r, c]) > 1e-10:
                    print(f"    [{r},{c}] = {outer[r,c]:.4f}")
    else:
        print(f"  j={j}: ZERO")

# The KEY question: in Connes' SM, does order-one hold for A_F with his D_F?
# YES -- it does by construction. His D_F has a SPECIFIC structure:
# D_F acts between chiralities (off-diagonal in gamma_5)
# On Psi_+: D_F couples the first row (nu, c) to the first column (nu, b)
# The Yukawa matrices Y_u, Y_d, Y_e enter as COUPLING CONSTANTS.
#
# The difference is: in Connes, pi(a) for a in H acts as:
#   pi(q) = diag(alpha, alpha, beta, beta_bar) on ROWS (for quaternion q = alpha + beta j)
# NOT as diag(i, -i, i, -i) which mixes the SU(2) and U(1) parts!
#
# The quaternionic action is:
#   q = a + bj where a, b in C
#   pi(q)|_{2x2 block} = [[a, b], [-b_bar, a_bar]]

print(f"\n{'=' * 76}")
print("PART 8: THE QUATERNIONIC ACTION -- CONNES VS BAPTISTA")
print(f"{'=' * 76}")

# In Connes' NCG, the quaternion H acts on the 2x2 doublet block as:
# q = alpha + beta*j maps to [[alpha, beta], [-conj(beta), conj(alpha)]]
# This is the STANDARD embedding H -> M_2(C).
#
# In our bimodule from Baptista, H_i = diag(i, -i, i, -i) acts diagonally.
# This is an ABELIANIZED version of H!
#
# The full quaternionic action would have off-diagonal generators H_j and H_k
# that MIX the two doublet components:
#   H_j maps to [[0, 1], [-1, 0]] on the 2x2 block
#   H_k maps to [[0, i], [i, 0]] on the 2x2 block

# In our script, H_j and H_k DO have off-diagonal structure:
L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j

print("\nH generators in 4x4 LEFT representation:")
print(f"  H_i = diag(i, -i, i, -i)  -- acts on doublets (nu/e, u/d)")
print(f"  H_j = [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]] -- mixes 3<->4")
print(f"  H_k = [[0,0,0,0],[0,0,0,0],[0,0,0,i],[0,0,i,0]] -- mixes 3<->4")

# H_j only acts on rows 2,3 (the b-sector in the original indexing)
# It does NOT act on rows 0,1 (the nu/c sector)
# But wait -- in the Connes convention, the quaternion acts on the LEPTON doublet
# and the QUARK doublet. That's rows (0,2) and (1,3) in some conventions.

# In our convention:
# Row 0 = nu (lepton singlet / right-handed neutrino)
# Row 1 = c (first color component -- this is the c-type quarks)
# Row 2 = b (second component -- not the b quark, but the isospin partner)
# Row 3 = D (third color component)

# Actually from Baptista's 4x4 matrix Psi:
# Psi = [[nu, c_red, c_green, c_blue],
#         [e,  d_red,  d_green, d_blue],
#         [reserved...]]
# No, let me recheck the conventions from Baptista eq 2.66

print("\nBaptista 4x4 matrix Psi convention (eq 2.66 in 2024 paper):")
print("  Column 0 = SU(3) singlet = leptons")
print("  Columns 1-3 = SU(3) triplet = quarks")
print("  Row 0 = first component = (nu_R, u_R^1, u_R^2, u_R^3)")
print("  Row 1-3 map to down-type and others via L action")
print("\n  The LEFT SU(2) action mixes (Row 0, Row j) pairs")
print("  That is: H_j mixes rows 2<->3 (which are inside the b/D block)")

# In Connes' A_F = C + H + M_3(C):
# C acts as lambda * I on leptons (column 0)
# H acts as quaternion on the (doublet) rows
# M_3(C) acts on columns 1,2,3
#
# The order-one condition with Connes' D_F works because:
# D_F couples row 0 (up-type) to rows 1-3 (down-type) via Yukawa
# H acts as 2x2 blocks on (row 0, row j) pairs
# M_3(C) acts on columns
# [D_F, pi(q)] for quaternion q gives a LEFT operator
# JqJ^{-1} gives a RIGHT operator
# They commute because left and right commute on the matrix

# BUT in our representation:
# D_F couples c (row 0, col j) to b (row j, col 0)
# This is NOT "row 0 to row j" -- it's "position (0,j) to position (j,0)"
# It mixes BOTH row AND column indices!

print(f"\n*** FUNDAMENTAL ISSUE IDENTIFIED ***")
print("  Connes' D_F couples: up-type ROW to down-type ROW (same column)")
print("  Baptista's D_F couples: position (0,j) to position (j,0)")
print("  The Baptista D_F changes BOTH row and column!")
print("  This makes it impossible to factor as left x right.")
print("\n  In Connes: D_F|_{row} . X . I  (pure left action on rows)")
print("  In Baptista: D_F maps Psi_{0j} <-> Psi_{j0} (mixes L and R)")

# But wait -- is this actually what Baptista means?
# Let me re-read eq 2.65 more carefully...
# The L-homomorphism failure [L_u, L_v] - L_{[u,v]} = 2[u,v]_{11} * ...
# This is about the LEFT action of su(3), not about D_F.
# D_F in the NCG sense comes from the INTERNAL Dirac operator on K = SU(3).

print(f"\n{'=' * 76}")
print("PART 9: THE CORRECT D_F -- INTERNAL DIRAC OPERATOR ON SU(3)")
print(f"{'=' * 76}")

print("\nThe D_F we've been using (c<->b coupling) is INSPIRED by eq 2.65,")
print("but the actual finite Dirac operator in Connes' NCG is different.")
print("\nIn Connes' spectral triple (A_F, H_F, D_F):")
print("  H_F = C^{2N} for N generations (N=3 for SM)")
print("  D_F encodes Yukawa couplings and Majorana masses")
print("  D_F is off-diagonal in chirality: D_F anticommutes with gamma_F")
print("  D_F satisfies order-one BY CONSTRUCTION (it's built to do so)")
print("\nBut in Baptista's KK framework:")
print("  H_F = 4x4 matrices (16-dim for Psi_+)")
print("  D_F comes from the GEOMETRIC Dirac operator restricted to zero modes")
print("  There is NO guarantee that this geometric D_F satisfies Connes' order-one")
print("\nThe order-one condition IS a consistency requirement.")
print("If the geometric D_F from KK doesn't satisfy it, that means:")
print("  1. The Baptista-Connes correspondence works at the ALGEBRA level (A_F)")
print("  2. But the DIRAC OPERATOR may need modification to match Connes' spectral triple")
print("  3. This is actually EXPECTED: the KK Dirac operator includes contributions")
print("     from both the internal geometry AND the gauge connection.")
print("     The 'bare' D_F (without gauge field) = mass matrix = Yukawa terms.")
print("     These are NOT purely geometric -- they involve the specific metric g_s.")
