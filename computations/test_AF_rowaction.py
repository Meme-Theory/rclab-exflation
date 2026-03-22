"""
GATE CHECK + CORRECTED A_F CONSTRUCTION
========================================

Gen-physicist critical insight (Session 10):
  M_3(C) acts on ROWS of the 4x4 matrix (LEFT multiplication: D -> m*D),
  NOT on columns. R_{u(2)} acts on COLUMNS (RIGHT mult: D -> -D*v).
  Left and right commute: (m*D)*v = m*(D*v).

This script:
  1. Constructs 9 color generators E_{ij} acting on ROWS 1-3 of 4x4 matrix
  2. GATE CHECK: verifies [E_{ij}^{32}, rho_R(v)] = 0 for all R_{u(2)} gens
  3. Constructs full A_F = C + H + M_3(C) with corrected row-action M_3(C)
  4. Tests: commutant, J-compat, quaternions, order-zero, closure

Gate check threshold: max |[E_{ij}^{32}, rho_R(v)]| < 1e-10
Order-zero threshold: max |[a, Xi b^T Xi]| < 1e-10

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

# ── Infrastructure from Phase 2a ──

particle_names_plus = [
    'nu_R', 'u_R^r', 'u_R^g', 'u_R^b',
    'e_R^-', 'd_R^r', 'd_R^g', 'd_R^b',  # Note: Baptista ordering
    'nu_L', 'u_L^r', 'u_L^g', 'u_L^b',
    'e_L^-', 'd_L^r', 'd_L^g', 'd_L^b',
]

def get_column_index(flat_idx):
    """Get column index of flat_idx in the 4x4 matrix."""
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return flat_idx
    elif 4 <= flat_idx <= 6: return 0
    else: return (flat_idx - 7) % 3 + 1

def get_row_index(flat_idx):
    """Get row index of flat_idx in the 4x4 matrix."""
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return 0
    elif 4 <= flat_idx <= 6: return flat_idx - 3  # 4->1, 5->2, 6->3
    else: return (flat_idx - 7) // 3 + 1  # 7-9->1, 10-12->2, 13-15->3

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)

n = 32
basis_u2 = u2_basis_in_su3()

def rho_minus(rho_plus_v):
    """Psi_- gauge action: G5 conj(rho_+) G5."""
    return G5 @ np.conj(rho_plus_v) @ G5

def build_full_32(gen_16):
    """Extend a 16x16 Psi_+ operator to 32x32 via J-compatibility."""
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32

# R_{u(2)} generators on C^32
R_u2_gens_16 = [R_action_matrix(v) for v in basis_u2]
R_u2_gens_32 = [build_full_32(g) for g in R_u2_gens_16]

# ── Flat index mapping (Baptista convention) ──
# Psi_+ as 4x4 matrix:
#   (0,0)=0:nu_R   (0,1)=1:u_R^r  (0,2)=2:u_R^g  (0,3)=3:u_R^b     row 0
#   (1,0)=4:e_R    (1,1)=7:d_R^r  (1,2)=8:d_R^g  (1,3)=9:d_R^b     row 1
#   (2,0)=5:nu_L   (2,1)=10:u_L^r (2,2)=11:u_L^g (2,3)=12:u_L^b    row 2
#   (3,0)=6:e_L    (3,1)=13:d_L^r (3,2)=14:d_L^g (3,3)=15:d_L^b    row 3

def flat_idx(row, col):
    """Convert 4x4 matrix index (row, col) to Baptista flat 16-index."""
    if row == 0 and col == 0: return 0
    if row == 0: return col          # (0,1)=1, (0,2)=2, (0,3)=3
    if col == 0: return row + 3      # (1,0)=4, (2,0)=5, (3,0)=6
    return 7 + 3 * (row - 1) + (col - 1)  # D entries


def build_left_action_16(L4):
    """Build 16x16 matrix for LEFT multiplication: Psi -> L4 . Psi.

    For a 4x4 matrix Psi with entries Psi[i,j], left multiplication by L4 gives:
      (L4 . Psi)[i,j] = sum_k L4[i,k] * Psi[k,j]

    In flat indices: gen[flat(i,j), flat(k,j)] += L4[i,k] for each col j.
    """
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for k in range(4):
            if abs(L4[i, k]) < 1e-15:
                continue
            for j in range(4):  # column is spectator
                fi = flat_idx(i, j)
                fk = flat_idx(k, j)
                gen[fi, fk] += L4[i, k]
    return gen


def build_right_action_16(R4):
    """Build 16x16 matrix for RIGHT multiplication: Psi -> Psi . R4.

    For a 4x4 matrix Psi, right multiplication by R4 gives:
      (Psi . R4)[i,j] = sum_l Psi[i,l] * R4[l,j]

    In flat indices: gen[flat(i,j), flat(i,l)] += R4[l,j] for each row i.
    """
    gen = np.zeros((16, 16), dtype=complex)
    for l in range(4):
        for j in range(4):
            if abs(R4[l, j]) < 1e-15:
                continue
            for i in range(4):  # row is spectator
                fi = flat_idx(i, j)
                fl = flat_idx(i, l)
                gen[fi, fl] += R4[l, j]
    return gen


# =============================================================================
# PART 1: GATE CHECK -- M_3(C) row-action commutes with R_{u(2)}
# =============================================================================

print("=" * 76)
print("GATE CHECK: M_3(C) acting on ROWS vs R_{u(2)} acting on COLUMNS")
print("=" * 76)

# M_3(C) generators: E_{ab} for a,b in {0,1,2} acting on ROWS 1-3
# Left multiplication by L_m = diag(1, m) where m is 3x3:
#   - Row 0 of 4x4: unchanged (multiplied by 1)
#   - Rows 1-3 of 4x4: mixed by m (left mult D -> m*D, b -> m*b)
#
# For E_{ab}: m has 1 at position (a,b), zeros elsewhere.
# L_m = diag(1, E_{ab}) is 4x4.

color_gens_16 = []
color_names = []

for a in range(3):
    for b in range(3):
        L_m = np.zeros((4, 4), dtype=complex)
        L_m[0, 0] = 0.0  # NOT identity on row 0; just the E_{ab} piece
        L_m[a + 1, b + 1] = 1.0
        gen_16 = build_left_action_16(L_m)
        color_gens_16.append(gen_16)
        color_names.append(f'E_{a}{b}')

# Extend to C^32
color_gens_32 = [build_full_32(g) for g in color_gens_16]

# Gate check: [E_{ij}^{32}, rho_R(v)] = 0?
print("\n  9 color generators E_{ij} (left row action on rows 1-3)")
print(f"  Testing against {len(R_u2_gens_32)} R_u(2) generators\n")

gate_max = 0
gate_results = []
for ci, (E32, cn) in enumerate(zip(color_gens_32, color_names)):
    for gi, Rv in enumerate(R_u2_gens_32):
        comm = E32 @ Rv - Rv @ E32
        err = np.max(np.abs(comm))
        gate_max = max(gate_max, err)
        if err > 1e-10:
            gate_results.append((cn, gi, err))

if gate_max < 1e-10:
    print(f"  *** GATE CHECK PASSED ***  max |[E_ij, R_v]| = {gate_max:.2e}")
else:
    print(f"  *** GATE CHECK FAILED ***  max |[E_ij, R_v]| = {gate_max:.2e}")
    for cn, gi, err in gate_results[:10]:
        print(f"    {cn} vs R_gen_{gi}: {err:.6e}")


# =============================================================================
# PART 2: FULL A_F CONSTRUCTION with corrected row-action
# =============================================================================

print("\n" + "=" * 76)
print("A_F = C + H + M_3(C) CONSTRUCTION (row-action for all factors)")
print("=" * 76)

AF_gens_16 = []
AF_names = []
AF_factor = []  # Track which factor each generator belongs to

# ── C FACTOR (2 real dims) ──
# C acts as scalar lambda on row 0 of 4x4 matrix:
#   L_lambda = diag(lambda, 0, 0, 0) [only row 0]
# But wait -- in Connes' model, lambda also multiplies the quark entries.
# Actually: the A_F element (lambda, q, m) acts on X as:
#   X[0,:] -> lambda * X[0,:]    (row 0)
#   X[1:,:] -> q * X[1:,:] * ...  (rows 1-3, from H and M_3)
#
# The C factor acts ONLY on the first row. The scalar lambda multiplies
# the entire row 0 (all columns): nu_R, u_R^r, u_R^g, u_R^b.
#
# As left multiplication: L = diag(lambda, 0, 0, 0) on the 4x4 matrix.
# Note: this is a PROJECTION, not identity. C acts as lambda on row 0 only.
# The identity of A_F is (1, 1, I_3) which gives L = diag(1, I_3) = I_4.
# So C_Re = P_row0 (projection onto row 0) and C_Im = i*P_row0.

# C generator 1: Re(lambda) -- projection onto row 0
L_C_Re = np.zeros((4, 4), dtype=complex)
L_C_Re[0, 0] = 1.0
AF_gens_16.append(build_left_action_16(L_C_Re))
AF_names.append('C_Re')
AF_factor.append('C')

# C generator 2: Im(lambda) -- i * projection onto row 0
L_C_Im = np.zeros((4, 4), dtype=complex)
L_C_Im[0, 0] = 1j
AF_gens_16.append(build_left_action_16(L_C_Im))
AF_names.append('C_Im')
AF_factor.append('C')

# ── H FACTOR (4 real dims) ──
# H = quaternions {1, i, j, k} acting on rows 2-3 of the 4x4 matrix
# (the SU(2)_L doublet rows).
#
# From Connes: q in H acts on the 4x4 matrix as left multiplication by:
#   L_q = diag(q_+, q) where q_+ = q_0 + i*q_1 (complex scalar for RH)
#   and q is the 2x2 quaternion matrix acting on rows 2-3.
#
# Wait -- which rows? In Baptista's convention:
#   Row 0: (a, c^T) = RH singlets (nu_R, u_R^{r,g,b})
#   Row 1: (b_0, D_{0,:}) = lepton e_R and d_R quarks
#   Row 2: (b_1, D_{1,:}) = lepton nu_L and u_L quarks
#   Row 3: (b_2, D_{2,:}) = lepton e_L and d_L quarks
#
# The SU(2)_L doublet is (nu_L, e_L) = rows 2-3, col 0 for leptons
# and (u_L, d_L) = rows 2-3, cols 1-3 for quarks.
#
# But the H factor in A_F also acts on the RH sector:
# For (lambda, q, m) in A_F:
#   RH neutrino (row 0, col 0): lambda (from C)
#   RH electron (row 1, col 0): q_- = q_0 - i*q_1 (conjugate scalar)
#   LH doublet (rows 2-3, col 0): q as 2x2 matrix
#
# So the L action is:
#   L_{(lambda,q,m)} = ( lambda    0    0  )
#                       (  0      q_-   0  )   [where q_- = bar{q_+}]
#                       (  0       0    q  )   [q is 2x2 quaternion]
#
# Wait, this is a mixture of C and H. The PURE H generators (with lambda=1, m=I):
#   q=1:  L = diag(1, 1, I_2) = I_4  [identity, same as C_Re]
#   q=i:  L = diag(i, -i, i*sigma_3)?
#
# Let me be more precise. In the standard Connes model, H embeds in M_4(C) as:
#   q = a + bi + cj + dk  ->  L_q = diag(alpha, bar{alpha}, q_2x2)
# where alpha = a + bi and q_2x2 = ((a+bi, c+di), (-c+di, a-bi)).
#
# But which rows of the 4x4 matrix does this act on?
# Row 0: acted on by alpha = a+bi (from C and H_i -- C and H share this action)
# Row 1: acted on by bar{alpha} = a-bi
# Rows 2-3: acted on by q_2x2

# For PURE H (separating from C), we need generators that are linearly
# independent of C. Note C_Re = P_row0 and C_Im = i*P_row0.
#
# H_1: Acts as (1, 1, I_2) on rows = I_4. This is the identity of the FULL algebra.
# H_i: Acts as (i, -i, diag(i,-i)) on rows.
# H_j: Acts as (0, 0, sigma_x type) on rows.  [j mixes rows 2-3]
# H_k: Acts as (0, 0, sigma_y type) on rows.  [k mixes rows 2-3]
#
# The H factor as a subalgebra acts on:
#   row 0: alpha (complex scalar from q)
#   row 1: bar{alpha} (conjugate)
#   rows 2-3: q as 2x2 quaternion matrix

# But rows 0 and 1 get alpha and bar{alpha} from the SAME quaternion q.
# The C factor contributes lambda on row 0 only.
# So the TOTAL action of (lambda, q, m) on row 0 is lambda * alpha.
# And on row 1 it is bar{alpha}.
# And on rows 2-3 it is q_2x2.

# To separate C from H cleanly:
# C = {(lambda, 1, I_3)} -- lambda on row 0, identity everywhere else
# H = {(1, q, I_3)} -- q acts as alpha on row 0, bar{alpha} on row 1, q_2x2 on rows 2-3
#
# But (1, q, I_3) with q=1 gives alpha=1, which acts as identity on row 0 too.
# And C with lambda=1 also gives identity on row 0.
# So C_Re and H_1 are BOTH the identity on row 0. They overlap!
#
# In the DIRECT SUM A_F = C + H + M_3(C), each summand acts on DIFFERENT
# subsets of H_F (or at least their actions don't interfere). Actually no --
# in A_F as a direct sum, an element is (lambda, q, m) and the action is:
#
#   pi(lambda, q, m) . Psi = left_action(lambda, q, m) . Psi . right_action(m^dag)
#
# Hmm, this is getting complex. Let me focus on what we KNOW from the
# existing test_AF_direct.py results and the gen-physicist's analysis.
#
# The gen-physicist says (Section 6, PREDICTION A):
#   C generators on Psi_+: 16x16 with 1's at diagonal positions 0,1,2,3 (row 0)
#   for Re, and i at those positions for Im.
#
# But from Connes' full representation, the A_F action is:
#   pi(lambda, q, m) on the 4x4 matrix X = (a, c; b, D):
#
#     a -> lambda * a                    (scalar on (0,0))
#     c -> lambda * c * m^dag            (row 0, cols 1-3)
#     b -> q_lowertriangle * b           (rows 1-3, col 0)
#     D -> q_lowertriangle * D * m^dag   (rows 1-3, cols 1-3)
#
# Wait, the precise embedding depends on conventions. Let me use the
# SIMPLEST possible construction: pure LEFT action with no m^dag on the right.
# The M_3(C) part acts on the RIGHT. But we said M_3(C) acts on ROWS!
#
# OK I need to be very careful. Let me re-read the gen-physicist Section 5.1-5.2.
#
# Gen-physicist says:
#   "M_3(C) in A_F acts on ROWS of the 4x4 matrix (via left multiplication on
#    the 3x3 D-block)"
#   "D -> m D"  (left multiplication)
#
# This means M_3(C) acts on ROWS 1-3 via left multiplication, affecting
# both b (col 0) and D (cols 1-3).
# Similarly, C and H act on ROWS via left multiplication:
#   C: scalar on row 0
#   H: quaternionic on all rows (alpha on row 0, bar{alpha} on row 1, q on rows 2-3)
#
# And the OPPOSITE algebra A_F^o = R_{u(2)} acts on COLUMNS via right multiplication.
#
# So the ENTIRE A_F is a LEFT-ACTION algebra, and A_F^o is the RIGHT-ACTION.
# This is consistent with Connes' framework: pi(a) on the left, pi^o(b) on the right.
#
# For the A_F left action: pi(lambda, q, m) . X = L . X where
#   L = diag(lambda, m)  [wait, that mixes C and M_3]
#
# Actually, in Connes' model (see Chamseddine-Connes-Marcolli 0706.3688):
#   A_F = C + H + M_3(C) acts on M_4(C) as:
#     (lambda, q, m) . X = diag(lambda, q) . X . diag(1, m)^dag
#
# So the action is BIMODULE: LEFT by diag(lambda, q) and RIGHT by diag(1, m^dag).
# This means M_3(C) acts on the RIGHT after all!
#
# But gen-physicist says M_3(C) acts on the LEFT (rows). This seems contradictory.
#
# RESOLUTION: There is a CHOICE of convention. In one convention (Connes 2006):
#   A_F acts as LEFT x RIGHT bimodule on M_4(C)
# In another convention (equivalent):
#   A_F can be embedded purely as LEFT operators on H_F = C^32
#   by absorbing the right action into the operator via the matrix structure
#
# For our COMPUTATIONAL purpose, what matters is: does the generator commute
# with R_{u(2)}? Let's test BOTH:
# (a) M_3(C) as LEFT row action: build_left_action_16(diag(0, m))
# (b) M_3(C) as RIGHT col action: build_right_action_16(diag(1, m^dag))
#
# We already know (b) FAILS from test_AF_direct.py. Let's test (a).
# The gate check above already tests (a) for the color generators.

# For the full A_F, let me try the PURE LEFT action convention:
# pi(lambda, q, m) = build_left_action_16(diag(lambda * alpha_row0,
#                                                bar_alpha_row1,
#                                                q_2x2_rows23) * ?)
#
# No -- M_3(C) mixes rows 1-3 among themselves. If the full A_F left action is:
#   L = diag(lambda, m_rows1-3)  where m is the M_3(C) element
# then C acts on row 0 and M_3(C) acts on rows 1-3.
#
# And H? H acts on the doublet structure. If rows 2-3 are the SU(2)_L doublet,
# then H acts within rows 2-3, which OVERLAPS with M_3(C) on rows 1-3.
#
# This is the key: in a DIRECT SUM A_F = C + H + M_3(C), each summand acts
# on a SEPARATE part of the representation space. So:
#   C acts on the C-module part of H_F
#   H acts on the H-module part
#   M_3(C) acts on the M_3-module part
#
# These parts are NOT the same as "rows" of the 4x4 matrix.
#
# Let me just COMPUTE and let the numbers speak. I'll build all generators
# as LEFT row operations and check everything numerically.

print("\n--- C factor (2 generators) ---")
print("  C_Re: identity on row 0 (left mult by diag(1,0,0,0))")
print("  C_Im: i*identity on row 0 (left mult by diag(i,0,0,0))")

# Already added C_Re and C_Im above.

# ── H FACTOR ──
# For H, the key is that it acts on the SU(2)_L doublet structure.
# On the 4x4 matrix, the quaternionic structure embeds as:
#   q = a + bi + cj + dk acts on rows via:
#   Row 0: multiplied by (a+bi) = alpha
#   Row 1: multiplied by (a-bi) = bar{alpha}
#   Rows 2-3: acted on by q as 2x2 matrix [[a+bi, c+di],[-c+di, a-bi]]
#
# H_1 = identity (on rows 0-3, acts as 1 everywhere)
#   L = I_4
# But wait -- H_1 = I_4 is the SAME as having C_Re (P_row0) + M3_identity
# (P_rows1-3). So we need to be careful about the direct sum structure.
#
# Actually, in the direct sum C + H + M_3(C), the element (1, 1, I_3) is the
# identity. Each summand contributes to different SLOTS:
#   C slot: lambda in C
#   H slot: q in H
#   M_3 slot: m in M_3(C)
#
# The representation pi: C + H + M_3(C) -> End(C^16) maps:
#   pi(lambda, 0, 0) = action of C component
#   pi(0, q, 0) = action of H component
#   pi(0, 0, m) = action of M_3 component
# and pi(lambda, q, m) = pi(lambda,0,0) + pi(0,q,0) + pi(0,0,m)
# because it's a direct sum representation.
#
# For M_3(C): pi(0, 0, m) acts on some subspace of C^16.
# For C: pi(lambda, 0, 0) acts on a different subspace.
# For H: pi(0, q, 0) acts on yet another subspace.
#
# The THREE subspaces are ORTHOGONAL and span C^16.
#
# From the SM fermion content (one generation):
#   nu_R (idx 0): C-module (lambda acts as lambda)
#   (e_R, nu_L, e_L) (idx 4,5,6): this is where H would act?
#   u_R^{r,g,b} (idx 1,2,3): C tensor M_3(C)-module
#   d quarks + u_L quarks + d_L quarks: H tensor M_3(C)-module
#
# Hmm, actually the representation theory is more subtle.
# Let me just build the generators based on what MUST be true:
#
# The A_F left action on Psi_+ (following Connes-Chamseddine-Marcolli):
#   For (lambda, q, m) in C + H + M_3(C):
#
#   On the 4x4 matrix X = (a, c^T; b, D):
#     a (scalar, idx 0) -> lambda * a
#     c_j (idx 1-3) -> lambda * (m^* . c)_j  [m acts on color]
#     b_i (idx 4-6) -> sum_k (Q)_{ik} * b_k  [q acts on SU(2)]
#     D_{ij} (idx 7-15) -> sum_k (Q)_{ik} * (D . m^dag)_{kj} [both q and m act]
#
# where Q is the 3x3 "left-block" from the quaternion q embedded as:
#   Q = diag(alpha_bar, q_2x2) with alpha_bar = q_0 - i*q_1
#
# This is a BIMODULE action: LEFT by (lambda/Q) and RIGHT by m^dag on D and c.
#
# For R_{u(2)} commutant: the RIGHT action by m^dag does NOT commute with R
# (both act on columns). The LEFT action by Q DOES commute with R (different axes).
#
# So the question becomes: which part of A_F's action is LEFT-only and commutes
# with R_{u(2)}?
#
# The LEFT part: diag(lambda, Q) acting on rows.
# The RIGHT part: diag(1, m^dag) acting on columns.
#
# For the R_{u(2)} COMMUTANT, we need operators that commute with R. Only the
# LEFT part qualifies. The RIGHT part (m^dag) does NOT commute with R.
#
# THIS MEANS: In the R_{u(2)} commutant, A_F embeds with:
#   LEFT component: diag(lambda, Q) -- this is C + H (dim 2+4=6)
#   M_3(C) RIGHT component: DOES NOT EMBED (conflicts with R)
#
# UNLESS... M_3(C) can be re-expressed as a LEFT action.
#
# The gen-physicist says M_3(C) acts on rows. But in the standard Connes model,
# M_3(C) acts on COLUMNS (colors). Colors ARE columns in the 4x4 matrix.
#
# HOWEVER, there's a SECOND M_3(C) action: the OPPOSITE algebra A_F^o = JA_FJ^{-1}.
# In the opposite algebra, M_3(C) acts from the RIGHT on the original, which
# becomes LEFT action on the J-transformed space.
#
# Let me abandon the theoretical analysis and just DO THE GATE CHECK.
# The gate check result will tell us definitively.

# If the gate check passed (tested above), then left-action M_3(C) on rows 1-3
# IS in the commutant, regardless of whether this matches Connes' convention.

if gate_max < 1e-10:
    print("\n  Gate check PASSED -- proceeding with full A_F construction")
else:
    print("\n  Gate check FAILED -- but proceeding with analysis anyway")

# ── H generators (pure left row action) ──

# H_1: q=1 -> alpha=1, bar_alpha=1, q_2x2=I_2
# L = diag(1, 1, 1, 1) = I_4  (identity)
L_H_1 = np.eye(4, dtype=complex)
AF_gens_16.append(build_left_action_16(L_H_1))
AF_names.append('H_1')
AF_factor.append('H')

# H_i: q=i -> alpha=i, bar_alpha=-i, q_2x2=diag(i,-i)
# L = diag(i, -i, i, -i)
L_H_i = np.diag([1j, -1j, 1j, -1j])
AF_gens_16.append(build_left_action_16(L_H_i))
AF_names.append('H_i')
AF_factor.append('H')

# H_j: q=j -> alpha=0, bar_alpha=0, q_2x2=[[0,1],[-1,0]]
# L = diag(0, 0, [[0,1],[-1,0]])
L_H_j = np.zeros((4, 4), dtype=complex)
L_H_j[2, 3] = 1.0
L_H_j[3, 2] = -1.0
AF_gens_16.append(build_left_action_16(L_H_j))
AF_names.append('H_j')
AF_factor.append('H')

# H_k: q=k -> alpha=0, bar_alpha=0, q_2x2=[[0,i],[i,0]]
# L = diag(0, 0, [[0,i],[i,0]])
L_H_k = np.zeros((4, 4), dtype=complex)
L_H_k[2, 3] = 1j
L_H_k[3, 2] = 1j
AF_gens_16.append(build_left_action_16(L_H_k))
AF_names.append('H_k')
AF_factor.append('H')

# ── M_3(C) generators (left row action on rows 1-3) ──

# E_{ab} for a,b in {0,1,2}: L_m = diag(0, E_{ab}) as 4x4
# Re and Im parts: 9 x 2 = 18 generators

for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            L_m = np.zeros((4, 4), dtype=complex)
            L_m[a + 1, b + 1] = val
            AF_gens_16.append(build_left_action_16(L_m))
            AF_names.append(f'M3_E{a}{b}_{part}')
            AF_factor.append('M3')

print(f"\n  Total generators: {len(AF_gens_16)}")
print(f"    C: 2, H: 4, M3: 18, total: 24")

# Extend to C^32
AF_gens_32 = [build_full_32(g) for g in AF_gens_16]


# =============================================================================
# PART 3: VERIFICATION TESTS
# =============================================================================

# ── Test 1: Identity check ──
print("\n" + "-" * 76)
print("[TEST 1] Verify build_left_action_16 gives correct identity")
test_id = build_left_action_16(np.eye(4, dtype=complex))
err_id = np.max(np.abs(test_id - np.eye(16)))
print(f"  left_action(I_4) = I_16: {err_id:.2e} ({'PASS' if err_id < 1e-14 else 'FAIL'})")

# Verify flat_idx mapping
print("\n  Flat index verification:")
for r in range(4):
    row_str = "  row " + str(r) + ": "
    for c in range(4):
        fi = flat_idx(r, c)
        row_str += f"({r},{c})={fi:2d}  "
    print(row_str)

# ── Test 2: Independence and dimension ──
print("\n" + "-" * 76)
print("[TEST 2] Real dimension of A_F generator span")
AF_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in AF_gens_32]
AF_mat = np.column_stack(AF_vecs)
AF_rank = np.linalg.matrix_rank(AF_mat, tol=1e-8)
print(f"  Rank: {AF_rank} (target: 24)")

# Check which generators are redundant
if AF_rank < len(AF_gens_32):
    print("  Checking for redundant generators...")
    unique_idx = []
    for i, v in enumerate(AF_vecs):
        if not unique_idx:
            unique_idx.append(i)
        else:
            M = np.column_stack([AF_vecs[j] for j in unique_idx])
            _, s, _ = np.linalg.svd(np.column_stack([M, v.reshape(-1, 1)]))
            if s[-1] > 1e-8:
                unique_idx.append(i)
            else:
                print(f"    Redundant: {AF_names[i]}")

# ── Test 3: In R_{u(2)} commutant? ──
print("\n" + "-" * 76)
print("[TEST 3] A_F generators in R_u(2) commutant?")
comm_pass = 0
comm_fail = 0
for idx, (T, name, fac) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
    max_err = max(np.max(np.abs(T @ R_g - R_g @ T)) for R_g in R_u2_gens_32)
    if max_err > 1e-10:
        print(f"  FAIL: {name} ({fac}): max |[T, R_v]| = {max_err:.6e}")
        comm_fail += 1
    else:
        comm_pass += 1

print(f"  Result: {comm_pass} PASS, {comm_fail} FAIL out of {len(AF_gens_32)}")

# ── Test 4: J-compatible? ──
print("\n" + "-" * 76)
print("[TEST 4] A_F generators J-compatible? (T Xi = Xi conj(T))")
jcompat_pass = 0
for idx, (T, name) in enumerate(zip(AF_gens_32, AF_names)):
    err = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
    if err > 1e-10:
        print(f"  FAIL: {name}: max error = {err:.6e}")
    else:
        jcompat_pass += 1
print(f"  Result: {jcompat_pass} PASS out of {len(AF_gens_32)}")

# ── Test 5: Quaternion relations ──
print("\n" + "-" * 76)
print("[TEST 5] Quaternion relations in H factor")
Hi = AF_gens_32[AF_names.index('H_i')]
Hj = AF_gens_32[AF_names.index('H_j')]
Hk = AF_gens_32[AF_names.index('H_k')]
H1 = AF_gens_32[AF_names.index('H_1')]

for label, prod, exp in [
    ('i^2=-1', Hi @ Hi, -H1),
    ('j^2=-1', Hj @ Hj, -H1),
    ('k^2=-1', Hk @ Hk, -H1),
    ('ij=k', Hi @ Hj, Hk),
    ('jk=i', Hj @ Hk, Hi),
    ('ki=j', Hk @ Hi, Hj),
]:
    err = np.max(np.abs(prod - exp))
    status = 'PASS' if err < 1e-10 else 'FAIL'
    print(f"  {label}: {status} (err={err:.2e})")

# ── Test 6: Order-zero condition ──
print("\n" + "-" * 76)
print("[TEST 6] Order-zero condition [a, Xi b^T Xi] = 0")
max_oz = 0
n_viol = 0
worst_pair = ('', '', 0)
oz_by_factor = {}

for i, (Ti, ni, fi) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
    for j, (Tj, nj, fj) in enumerate(zip(AF_gens_32, AF_names, AF_factor)):
        b_opp = Xi @ Tj.T @ Xi
        comm = Ti @ b_opp - b_opp @ Ti
        err = np.max(np.abs(comm))
        if err > max_oz:
            max_oz = err
            worst_pair = (ni, nj, err)
        if err > 1e-6:
            n_viol += 1

        pair_key = f'[{fi}, o({fj})]'
        if pair_key not in oz_by_factor:
            oz_by_factor[pair_key] = 0.0
        oz_by_factor[pair_key] = max(oz_by_factor[pair_key], err)

print(f"  Max |[a, o(b)]|: {max_oz:.6e}")
print(f"  Violations (>1e-6): {n_viol} / {len(AF_gens_32)**2}")
if max_oz > 1e-6:
    print(f"  Worst pair: [{worst_pair[0]}, o({worst_pair[1]})] = {worst_pair[2]:.6e}")

print("\n  By factor combination:")
for pair_key in sorted(oz_by_factor.keys()):
    val = oz_by_factor[pair_key]
    status = 'PASS' if val < 1e-6 else f'{val:.6e}'
    print(f"    {pair_key}: {status}")

# ── Test 7: Algebra closure ──
print("\n" + "-" * 76)
print("[TEST 7] Algebraic closure")

# Get independent generators
indep_idx = []
indep_vecs = []
for i, T in enumerate(AF_gens_32):
    v = np.concatenate([T.flatten().real, T.flatten().imag])
    if not indep_vecs:
        indep_idx.append(i)
        indep_vecs.append(v)
    else:
        M = np.column_stack(indep_vecs)
        coeffs = np.linalg.lstsq(M, v, rcond=None)[0]
        resid = np.linalg.norm(v - M @ coeffs)
        if resid > 1e-8:
            indep_idx.append(i)
            indep_vecs.append(v)

print(f"  Independent generators: {len(indep_idx)} / {len(AF_gens_32)}")

# Check closure: all products in the span?
gen_mats = [AF_gens_32[i] for i in indep_idx]
Q_gens = orth(np.column_stack(indep_vecs))
d_gens = Q_gens.shape[1]

max_resid = 0
for T1 in gen_mats:
    for T2 in gen_mats:
        prod = T1 @ T2
        pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
        coeffs = Q_gens.T @ pv
        resid = np.linalg.norm(pv - Q_gens @ coeffs)
        max_resid = max(max_resid, resid)

print(f"  Product closure: max residual = {max_resid:.2e} "
      f"({'CLOSED' if max_resid < 1e-6 else 'OPEN'})")

if max_resid > 1e-6:
    # Compute full algebraic closure iteratively
    print("  Computing algebraic closure...")
    n_flat = 32 * 32
    Q_cur = Q_gens.copy()
    d_cur = d_gens

    for iteration in range(10):
        cur_basis = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                     for k in range(d_cur)]
        new_vecs = []
        for T1 in cur_basis:
            for T2 in gen_mats:
                prod = T1 @ T2
                pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
                coeffs = Q_cur.T @ pv
                resid = np.linalg.norm(pv - Q_cur @ coeffs)
                if resid > 1e-8:
                    new_vecs.append(pv)
        if not new_vecs:
            break
        all_v = np.column_stack([Q_cur] + [np.column_stack(new_vecs)])
        Q_new = orth(all_v)
        d_new = Q_new.shape[1]
        if d_new == d_cur:
            break
        print(f"    Iteration {iteration+1}: dim {d_cur} -> {d_new}")
        Q_cur = Q_new
        d_cur = d_new

    print(f"  Algebraic closure dimension: {d_cur}")


# =============================================================================
# PART 4: SUMMARY
# =============================================================================

print("\n" + "=" * 76)
print("SUMMARY")
print("=" * 76)
print(f"  GATE CHECK (M3 row-action in R_u(2) commutant): "
      f"{'PASS' if gate_max < 1e-10 else 'FAIL'} (max={gate_max:.2e})")
print(f"  Independent dimension: {AF_rank} (target: 24)")
print(f"  In R_u(2) commutant: {comm_pass}/{len(AF_gens_32)} "
      f"({'PASS' if comm_fail == 0 else 'FAIL'})")
print(f"  J-compatible: {jcompat_pass}/{len(AF_gens_32)} "
      f"({'PASS' if jcompat_pass == len(AF_gens_32) else 'FAIL'})")
print(f"  Order-zero max: {max_oz:.6e} "
      f"({'PASS' if max_oz < 1e-10 else 'FAIL'})")
print(f"  Order-zero violations: {n_viol}/{len(AF_gens_32)**2}")
print(f"  Closure max resid: {max_resid:.2e} "
      f"({'CLOSED' if max_resid < 1e-6 else 'OPEN'})")
print("=" * 76)
