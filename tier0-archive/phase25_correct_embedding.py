"""
PHASE 2.5 CORRECT EMBEDDING: Find the Connes-compatible C+H embedding
======================================================================

Key finding: The order-one subalgebra of M_4(C) w.r.t. D_L (identity Yukawa)
has dimension 12 (real), which is LARGER than C + H = 6.

This script:
1. Analyzes the 12-dim order-one subalgebra structure
2. Identifies its Wedderburn decomposition
3. Determines how C + H should be embedded
4. Compares to Connes' standard embedding

In Connes' NCG for one generation:
  H_F = M_4(C) for Psi_+
  A_F = C + H + M_3(C)
  C + H acts on the LEFT (rows), M_3(C) on the RIGHT (columns)

  The CORRECT Connes embedding for C + H in M_4(C) is:
  (lambda, q) -> [[lambda, 0, 0, 0],
                   [0, lambda_bar, 0, 0],
                   [0, 0, alpha, beta],
                   [0, 0, -beta_bar, alpha_bar]]
  where q = alpha + beta*j (quaternion components)

  This is DIFFERENT from our Baptista-derived embedding!

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


# =============================================================================
# PART 1: Connes' standard embedding of C + H in M_4(C)
# =============================================================================
print("=" * 76)
print("PART 1: CONNES' STANDARD EMBEDDING")
print("=" * 76)

# In Connes-Chamseddine (see e.g. arXiv:0706.3688, eq. 2.14):
# For ONE generation, the left action of (lambda, q) in C + H on Psi_{4x4} is:
#
# Psi -> [[lambda, 0], [0, q]] . Psi   (block 1+3... no, block 2+2)
#
# Actually, the PRECISE embedding depends on how the 4 rows of Psi are identified.
# In Connes: rows = (nu_R, e_R, nu_L, e_L) for leptons
#            rows = (u_R, d_R, u_L, d_L) for quarks (x 3 colors)
#
# C acts as: lambda on (nu_R, u_R), lambda_bar on (e_R, d_R)
#            lambda on (nu_L, u_L)...
#
# Actually, in the Connes spectral triple for the SM:
# H_F = H_l + H_q where H_l = C^4 (lepton), H_q = C^4 x C^3 (quark x color)
# A_F = C + H + M_3(C) acts as:
#   On H_l: pi_l(lambda, q, m) = diag(lambda, lambda_bar) on (nu_R, e_R)
#           and q acting as 2x2 quaternion on (nu_L, e_L)
#   On H_q: pi_q(lambda, q, m) = diag(lambda, lambda_bar) on (u_R, d_R)
#           and q on (u_L, d_L), all tensored with m^* on color

# In the 4x4 MATRIX representation where Psi_{ij} = particle(row i, color j):
# Row 0 = nu/u (up-type, weak isospin +1/2)
# Row 1-3 = e/d (down-type, or rather rows 1,2,3 carry color for down-type)
#
# BUT this is not exactly the Connes convention. Let me think about what the
# correct LEFT embedding should be for the 4x4 matrix.

# The Baptista 4x4 matrix has:
# Row 0 = "c-type" (same weak isospin component as row 0)
# Rows 1-3 = "b-type" (different weak isospin, carrying color index)
# Column 0 = SU(3) singlet (lepton)
# Columns 1-3 = SU(3) triplet (quarks)

# The key constraint from Connes is:
# (lambda, q) should act on the ISOSPIN doublet as:
# On the up-type component: lambda (scalar multiplication)
# On the down-type components: through the quaternion q

# In our 4x4 matrix:
# Row 0 = up-type -> lambda acts as scalar: L_{00} = lambda
# Rows 1-3 = down-type -> but here we have 3 rows for ONE isospin component
#   In Connes, there's only ONE down-type row per generation.
#   Here, rows 1-3 carry an ADDITIONAL index.

# The resolution: rows 1-3 are NOT separate isospin components.
# They are the SAME isospin-down component, with row index = color index.
# The matrix structure is Psi_{alpha,a} where:
#   alpha = 0 (up-type) or 1,2,3 (down-type, with implicit alpha=1 for all)
#   a = 0 (lepton) or 1,2,3 (quark color)

# So the isospin doublet is (row 0, row j) for each j separately.
# The quaternion should act on (row 0, row j) as a 2x2 matrix:
# q = alpha + beta*j -> [[alpha, beta], [-beta_bar, alpha_bar]] on (row 0, row j)

# BUT this means each pair (row 0, row j) is acted on by the SAME quaternion.
# The 4x4 LEFT matrix should look like:

def connes_embedding_CH(lam, alpha, beta):
    """
    Connes embedding of (lambda, q) in C + H into M_4(C).
    lambda in C, q = alpha + beta*j in H.

    Row 0 = up-type (isospin +1/2)
    Rows 1,2,3 = down-type (isospin -1/2, with color index)

    On lepton column (col 0):
      lambda on row 0, lambda_bar on rows 1-3 (electron-type)
    On quark columns (cols 1-3):
      quaternion q_{2x2} on (row 0, row j) pairs

    BUT the LEFT matrix acts on ALL columns simultaneously.
    So we need a SINGLE 4x4 matrix that acts correctly on both.
    """
    L = np.zeros((4, 4), dtype=complex)

    # In the simplest case (no generation mixing):
    # L = [[alpha, beta, beta, beta],
    #      [-beta_bar, alpha_bar, 0, 0],
    #      [-beta_bar, 0, alpha_bar, 0],
    #      [-beta_bar, 0, 0, alpha_bar]]
    # ... but this mixes the 3 down-type rows, which is wrong.

    # Actually, each down-type row j=1,2,3 pairs with row 0 independently.
    # The quaternion acts as:
    #   Psi(0,a) -> alpha * Psi(0,a) + beta * Psi(j,a)  ... for which j?
    #   Psi(j,a) -> -beta_bar * Psi(0,a) + alpha_bar * Psi(j,a)

    # The problem is that there's no unique "j" to pair with row 0.
    # In the SM, the doublet is (nu, e) or (u, d) -- ONE pair per generation.
    # But here we have ONE up-type row and THREE down-type rows.

    # The resolution in Baptista: the 4x4 matrix IS the generation structure.
    # Row 0 pairs with row j via the j-th C^2 direction of the internal space.
    # The "quaternion" acts as: row 0 -> sum_j q_j * row_j somehow.

    # Let me just use the STANDARD Connes 4x4 embedding.
    # In Connes-Chamseddine-Marcolli (2007), the Dirac operator couples:
    # - Row 0 to rows 1-3 via Yukawa (up-type to down-type mass mixing)
    # - The quaternion acts on each (row 0, row j) pair as 2x2 block

    # For one generation with 3 colors, the correct L is:
    # alpha on row 0, alpha_bar on rows 1-3
    # Off-diagonal: beta * delta_{j,?} -- but WHICH j?

    # In fact, the SU(2)_L doublet structure means:
    # L_q acts on row 0 and rows 1-3 as:
    # Psi(0,:) -> alpha * Psi(0,:)
    # ... with off-diagonal terms coupling to the down-type.

    # I think the issue is that the 4x4 matrix representation conflates
    # the weak doublet structure with the color structure in the row index.

    # Let me just compute: what is the maximal C + H subalgebra of the
    # 12-dim order-one algebra?

    pass
    return L


# =============================================================================
# PART 2: Analyze the 12-dim order-one subalgebra
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 2: STRUCTURE OF 12-DIM ORDER-ONE SUBALGEBRA")
print(f"{'=' * 76}")

# D_L (identity Yukawa coupling row 0 to rows 1,2,3)
D_L = np.zeros((4, 4), dtype=complex)
for j in range(1, 4):
    D_L[0, j] = 1.0
    D_L[j, 0] = 1.0

# Find the 12-dim order-one subalgebra
basis_4x4 = []
for a in range(4):
    for b in range(4):
        E = np.zeros((4, 4), dtype=complex)
        E[a, b] = 1.0
        basis_4x4.append(E)
        E2 = np.zeros((4, 4), dtype=complex)
        E2[a, b] = 1j
        basis_4x4.append(E2)

d = len(basis_4x4)  # 32

# Build constraint matrix: [[D_L, e_i], e_j^dag] = 0 for all j
constraints = []
for j in range(d):
    ej_dag = basis_4x4[j].conj().T
    for r in range(4):
        for c in range(4):
            row_re = np.zeros(d)
            row_im = np.zeros(d)
            for i in range(d):
                Di = D_L @ basis_4x4[i] - basis_4x4[i] @ D_L
                dc = Di @ ej_dag - ej_dag @ Di
                row_re[i] = dc[r, c].real
                row_im[i] = dc[r, c].imag
            if np.max(np.abs(row_re)) > 1e-14:
                constraints.append(row_re)
            if np.max(np.abs(row_im)) > 1e-14:
                constraints.append(row_im)

A_cons = np.array(constraints)
ATA = A_cons.T @ A_cons
eigvals, eigvecs = np.linalg.eigh(ATA)
tol = 1e-8 * np.max(np.abs(eigvals))
null_mask = eigvals < tol
null_vecs = eigvecs[:, null_mask]

print(f"Order-one subalgebra dimension: {null_vecs.shape[1]}")

# Convert to nice basis: reconstruct matrices and orthogonalize
alg_gens = []
for k in range(null_vecs.shape[1]):
    v = null_vecs[:, k]
    A = sum(v[i] * basis_4x4[i] for i in range(d))
    alg_gens.append(A)

# Check if the algebra is closed under multiplication
print("\nChecking closure under multiplication:")
products_outside = 0
for i in range(len(alg_gens)):
    for j in range(len(alg_gens)):
        prod = alg_gens[i] @ alg_gens[j]
        # Project onto the subalgebra
        coeffs = np.zeros(len(alg_gens))
        # Use the null space basis
        v_prod = np.array([np.trace(prod.conj().T @ basis_4x4[k]).real for k in range(d)]
                         + [np.trace(prod.conj().T @ basis_4x4[k]).imag for k in range(d)])
        # Actually, just check if prod is in the null space of A_cons
        v_flat = np.zeros(d)
        for k in range(d):
            # Decompose prod in basis_4x4
            v_flat[k] = np.trace(basis_4x4[k].conj().T @ prod).real / np.trace(basis_4x4[k].conj().T @ basis_4x4[k]).real

        residual = A_cons @ v_flat
        if np.max(np.abs(residual)) > 1e-6:
            products_outside += 1

# Better approach: check closure by Gram-Schmidt in the algebra
# First, get a good basis
from numpy.linalg import qr

# Vectorize the algebra: map each 4x4 complex matrix to R^32
def mat_to_vec(M):
    v = np.zeros(32)
    for a in range(4):
        for b in range(4):
            v[8*a + 2*b] = M[a, b].real
            v[8*a + 2*b + 1] = M[a, b].imag
    return v

def vec_to_mat(v):
    M = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        for b in range(4):
            M[a, b] = v[8*a + 2*b] + 1j * v[8*a + 2*b + 1]
    return M

# Get orthonormal basis of the order-one subalgebra
vecs = np.array([mat_to_vec(A) for A in alg_gens]).T
Q, R_qr = qr(vecs, mode='reduced')
# Keep only columns with non-tiny R diagonal
keep = np.abs(np.diag(R_qr)) > 1e-10
Q = Q[:, keep]
print(f"Orthogonal basis dimension: {Q.shape[1]}")

# Now check closure
basis_mats = [vec_to_mat(Q[:, k]) for k in range(Q.shape[1])]

max_proj_err = 0
for i in range(len(basis_mats)):
    for j in range(len(basis_mats)):
        prod = basis_mats[i] @ basis_mats[j]
        v = mat_to_vec(prod)
        proj = Q @ (Q.T @ v)
        err = np.linalg.norm(v - proj)
        max_proj_err = max(max_proj_err, err)

print(f"Max projection error for products: {max_proj_err:.2e}")
if max_proj_err < 1e-8:
    print("Algebra is CLOSED under multiplication!")
else:
    print(f"Algebra is NOT closed (error {max_proj_err:.2e})")

# Check center
print(f"\nFinding center of the order-one subalgebra:")
n_basis = Q.shape[1]
comm_constraints = []
for i in range(n_basis):
    for j in range(n_basis):
        comm = basis_mats[i] @ basis_mats[j] - basis_mats[j] @ basis_mats[i]
        v = mat_to_vec(comm)
        # Express constraint: [e_k, e_j] = 0 in algebra coordinates
        # We need coefficients of e_k in the algebra
        for r in range(32):
            row = np.zeros(n_basis)
            for k in range(n_basis):
                c_ij = basis_mats[k] @ basis_mats[j] - basis_mats[j] @ basis_mats[k]
                row[k] = mat_to_vec(c_ij)[r]
            if np.max(np.abs(row)) > 1e-14:
                comm_constraints.append(row)

if len(comm_constraints) > 0:
    C_mat = np.array(comm_constraints)
    CTC = C_mat.T @ C_mat
    evals, evecs = np.linalg.eigh(CTC)
    center_mask = evals < 1e-8 * max(np.max(np.abs(evals)), 1e-10)
    center_dim = np.sum(center_mask)
    print(f"  Center dimension: {center_dim}")

    # Get center elements
    center_vecs = evecs[:, center_mask]
    for k in range(center_dim):
        c_elem = sum(center_vecs[i, k] * basis_mats[i] for i in range(n_basis))
        c_elem /= np.max(np.abs(c_elem))
        print(f"\n  Center element {k+1}:")
        for r in range(4):
            row_str = "    ["
            for c in range(4):
                if abs(c_elem[r, c]) < 1e-8:
                    row_str += "   .     "
                elif abs(c_elem[r, c].imag) < 1e-8:
                    row_str += f" {c_elem[r,c].real:+7.4f}"
                else:
                    row_str += f" {c_elem[r,c].real:+.2f}{c_elem[r,c].imag:+.2f}i"
                row_str += " "
            row_str += "]"
            print(row_str)


# =============================================================================
# PART 3: The CORRECT approach -- Connes' embedding
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 3: TESTING CONNES' STANDARD C+H EMBEDDING")
print(f"{'=' * 76}")

# In Connes' NCG for the SM (one generation), the embedding is:
#
# pi(lambda, q) = [[lambda, 0, 0, 0],
#                   [0, lambda_bar, 0, 0],  <-- conjugate for anti-particle
#                   [0, 0, alpha, beta],     <-- quaternion 2x2 block
#                   [0, 0, -beta_bar, alpha_bar]]
#
# where q = alpha + beta*j.
#
# The rows are: 0=nu_R, 1=e_R, 2=nu_L, 3=e_L for leptons
# OR: 0=u_R, 1=d_R, 2=u_L, 3=d_L for quarks (x color)
#
# The D_F couples R to L:
# D_F = [[0, 0, Y_nu, 0],
#         [0, 0, 0, Y_e],
#         [Y_nu^*, 0, 0, 0],
#         [0, Y_e^*, 0, 0]]
# coupling nu_R <-> nu_L and e_R <-> e_L

# THIS is different from our D_L which coupled row 0 to rows 1,2,3!
# Connes' D_F couples (0,2) and (1,3) -- chirality pairs, not isospin pairs!

# Let me test with Connes' D_F:
D_Connes = np.zeros((4, 4), dtype=complex)
Y_nu = 1.0
Y_e = 1.0
D_Connes[0, 2] = Y_nu;  D_Connes[2, 0] = Y_nu  # nu_R <-> nu_L
D_Connes[1, 3] = Y_e;   D_Connes[3, 1] = Y_e    # e_R <-> e_L

print(f"\nConnes D_F (chirality coupling):")
print(f"  D_Connes = ")
for r in range(4):
    print(f"    {D_Connes[r, :].real}")

# Build Connes C+H generators
# C: lambda -> [[lambda, 0], [0, lambda_bar]] on rows 0-1, + identity on rows 2-3...
# Actually, let me be precise:
# pi(lambda, 1_H) = diag(lambda, lambda_bar, lambda, lambda_bar)
# because lambda acts the same on R and L for up-type, lambda_bar for down-type

# Hmm, there are different conventions. Let me just build the generators:

# C: lambda * I_2 on (0,1) block, lambda_bar * I_2 on (2,3) block...
# No. In Connes (0706.3688 eq 2.14):
# pi(lambda, q, m) with q=1, m=1:
# On H_R (rows 0,1): diag(lambda, lambda_bar)
# On H_L (rows 2,3): q(=1) acts as 2x2 identity -> diag(1, 1)...
# Wait, that can't be right.

# Let me use the explicit Connes embedding from the literature.
# From Connes-Marcolli "Noncommutative Geometry, Quantum Fields and Motives" (2008):
#
# The finite algebra A_F = C + H + M_3(C) acts on
# H_F = (C^2 + C^2) + (C^2 + C^2) tensor C^3
# with the representation:
#
# pi(lambda, q, m):
#   On lepton sector C^2_R: (nu_R, e_R) -> (lambda * nu_R, lambda_bar * e_R)
#   On lepton sector C^2_L: (nu_L, e_L) -> q . (nu_L, e_L) [quaternion 2x2]
#   On quark sector C^2_R tensor C^3:
#     (u_R, d_R) -> (lambda * u_R, lambda_bar * d_R), tensored with m^* on color
#   On quark sector C^2_L tensor C^3:
#     (u_L, d_L) -> q . (u_L, d_L), tensored with m^* on color

# So for the 4x4 LEFT matrix (ignoring color which is RIGHT):
# On R-handed (rows 0,1): diag(lambda, lambda_bar)  [from C]
# On L-handed (rows 2,3): q_{2x2}                    [from H]

# Generators of C:
# lambda = 1: diag(1, 1, 1, 1) = identity (trivial)
# lambda = i: diag(i, -i, i, -i)?? No...
# lambda = i acts as: i on rows 0,2 (up-type), -i on rows 1,3 (down-type)
# So: diag(i, -i, i, -i) ... but wait, on L-handed sector q=1_H acts as identity,
# so lambda should NOT affect rows 2,3 at all!

# Let me be very careful:
# pi(lambda, 1_H, 1_M3):
#   row 0 (nu_R): lambda
#   row 1 (e_R): lambda_bar
#   row 2 (nu_L): 1 (from q = 1_H)
#   row 3 (e_L): 1 (from q = 1_H)

# pi(1, q, 1) for q = alpha + beta*j:
#   row 0 (nu_R): 1 (from lambda=1)
#   row 1 (e_R): 1 (from lambda=1, conjugate = 1)
#   row 2 (nu_L): alpha (from q)
#   row 3 (e_L): alpha_bar (from q)
#   Off-diagonal:
#   row 2->3: beta, row 3->2: -beta_bar

# So the full left action matrix is:
# pi(lambda, q, 1) = [[lambda, 0, 0, 0],
#                      [0, lambda_bar, 0, 0],
#                      [0, 0, alpha, beta],
#                      [0, 0, -beta_bar, alpha_bar]]

print(f"\nConnes C+H embedding in M_4(C):")
print(f"  pi(lambda, q) = diag(lambda, lambda_bar, q_{{2x2}})")
print(f"  Rows: 0=nu_R, 1=e_R, 2=nu_L, 3=e_L")

# Build generators:
connes_gens = []
connes_names = []

# C_Re: lambda = 1 -> diag(1, 1, 1, 1) = identity (skip, trivial)
# C_Im: lambda = i -> diag(i, -i, 1, 1) (q stays at identity)
C_Im_connes = np.diag([1j, -1j, 1.0, 1.0])
connes_gens.append(C_Im_connes); connes_names.append('C_Im')

# C_Re_proj: lambda = 1 -> already identity, so use:
# lambda = (1+0i) - identity gives nothing. Use Re part explicitly:
# Re(lambda) shifted: diag(1, 1, 0, 0) - this projects
C_Re_connes = np.diag([1.0, 1.0, 0.0, 0.0])  # projection, not in algebra
# Actually, just use the 2 real generators of C: Re(lambda) and Im(lambda)
# Re(lambda) = s -> diag(s, s, 1, 1)... no, (s, s_bar) = (s, s) for real s
# Hmm, C = C means lambda is complex, so Re and Im are:
# lambda = s + it: diag(s+it, s-it, 1, 1) = s*diag(1,1,1,1) + t*diag(i,-i,0,0)
# The s part is proportional to identity (within C+H), so the non-trivial C generator is:
# C_Im = diag(i, -i, 0, 0) -- but we need it to be diag(i, -i, 1, 1) since q=1_H
# Actually, lambda=i means pi(i, 1_H) = diag(i, -i, 1, 1)
# So C_Im should include the identity part on the H block.
# Let me just use the TRACELESS part: diag(i, -i, 0, 0)
# and have the identity as a separate generator.

# For order-one testing, we need:
# C basis: {I_4, diag(i, -i, 0, 0)}
# H basis: {I_4 already counted, diag(0,0,i,-i), off-diag j, off-diag k}

# H generators:
# H_i: q = i -> alpha=i, beta=0 -> [[i,0],[0,-i]] on rows 2-3
H_i_connes = np.diag([0.0, 0.0, 1j, -1j])
connes_gens.append(H_i_connes); connes_names.append('H_i')

# H_j: q = j -> alpha=0, beta=1 -> [[0,1],[-1,0]] on rows 2-3
H_j_connes = np.zeros((4, 4), dtype=complex)
H_j_connes[2, 3] = 1.0; H_j_connes[3, 2] = -1.0
connes_gens.append(H_j_connes); connes_names.append('H_j')

# H_k: q = k -> alpha=0, beta=i -> [[0,i],[-(-i),0]] = [[0,i],[i,0]] on rows 2-3
H_k_connes = np.zeros((4, 4), dtype=complex)
H_k_connes[2, 3] = 1j; H_k_connes[3, 2] = 1j
connes_gens.append(H_k_connes); connes_names.append('H_k')

# Identity
connes_gens.append(np.eye(4, dtype=complex)); connes_names.append('I')

print(f"\nConnes generators:")
for name, gen in zip(connes_names, connes_gens):
    diag = np.array([gen[i, i] for i in range(4)])
    off_diag = [(i, j, gen[i, j]) for i in range(4) for j in range(4) if i != j and abs(gen[i, j]) > 1e-10]
    print(f"  {name}: diag = {diag}", end="")
    if off_diag:
        print(f", off-diag = {off_diag}")
    else:
        print()


# =============================================================================
# TEST: Order-one with Connes' D_F and Connes' C+H embedding
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST: ORDER-ONE FOR CONNES EMBEDDING + CONNES D_F")
print(f"{'=' * 76}")

# D_Connes couples (0,2) and (1,3):
# D = [[0,0,Y_nu,0],[0,0,0,Y_e],[Y_nu,0,0,0],[0,Y_e,0,0]]

max_err = 0
worst = None
for i, (a, na) in enumerate(zip(connes_gens, connes_names)):
    Da = D_Connes @ a - a @ D_Connes
    for j, (b, nb) in enumerate(zip(connes_gens, connes_names)):
        b_dag = b.conj().T
        dc = Da @ b_dag - b_dag @ Da
        err = np.max(np.abs(dc))
        if err > max_err:
            max_err = err
            worst = (na, nb)
        if err > 1e-8:
            print(f"  [[D, {na}], {nb}^dag]: {err:.4f}")

if max_err < 1e-8:
    print("  ALL PASS! Order-one satisfied for Connes C+H with Connes D_F!")
else:
    print(f"\n  Max error: {max_err:.4f}, worst: {worst}")


# =============================================================================
# TEST: Same Connes C+H with OUR D_L (row 0 <-> rows 1-3)
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST: ORDER-ONE FOR CONNES EMBEDDING + OUR D_L")
print(f"{'=' * 76}")

max_err2 = 0
for i, (a, na) in enumerate(zip(connes_gens, connes_names)):
    Da = D_L @ a - a @ D_L
    for j, (b, nb) in enumerate(zip(connes_gens, connes_names)):
        b_dag = b.conj().T
        dc = Da @ b_dag - b_dag @ Da
        err = np.max(np.abs(dc))
        max_err2 = max(max_err2, err)
        if err > 1e-8:
            print(f"  [[D_L, {na}], {nb}^dag]: {err:.4f}")

if max_err2 < 1e-8:
    print("  ALL PASS!")
else:
    print(f"\n  Max error: {max_err2:.4f}")


# =============================================================================
# TEST: Baptista C+H with Connes D_F (chirality coupling)
# =============================================================================
print(f"\n{'=' * 76}")
print("TEST: ORDER-ONE FOR BAPTISTA EMBEDDING + CONNES D_F")
print(f"{'=' * 76}")

baptista_gens = [
    (np.diag([1j, 1.0, 1.0, 1.0]), 'C_Im_Bapt'),
    (np.diag([1j, -1j, 1j, -1j]), 'H_i_Bapt'),
    (np.zeros((4, 4), dtype=complex), 'H_j_Bapt'),  # placeholder
    (np.zeros((4, 4), dtype=complex), 'H_k_Bapt'),  # placeholder
]
# Fix H_j and H_k for Baptista
baptista_gens[2] = (np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=complex), 'H_j_Bapt')
baptista_gens[3] = (np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1j],[0,0,1j,0]], dtype=complex), 'H_k_Bapt')

max_err3 = 0
for i, (a, na) in enumerate(baptista_gens):
    Da = D_Connes @ a - a @ D_Connes
    for j, (b, nb) in enumerate(baptista_gens):
        b_dag = b.conj().T
        dc = Da @ b_dag - b_dag @ Da
        err = np.max(np.abs(dc))
        max_err3 = max(max_err3, err)
        if err > 1e-8:
            print(f"  [[D_Connes, {na}], {nb}^dag]: {err:.4f}")

if max_err3 < 1e-8:
    print("  ALL PASS!")
else:
    print(f"\n  Max error: {max_err3:.4f}")


# =============================================================================
# COMPARISON: What's different between the two embeddings?
# =============================================================================
print(f"\n{'=' * 76}")
print("COMPARISON: CONNES vs BAPTISTA C+H EMBEDDINGS")
print(f"{'=' * 76}")

print(f"\n  {'Generator':<12} {'Connes':<35} {'Baptista':<35}")
print(f"  {'-'*12} {'-'*35} {'-'*35}")

comparisons = [
    ('C_Im', np.diag([1j, -1j, 1.0, 1.0]), np.diag([1j, 1.0, 1.0, 1.0])),
    ('H_i', np.diag([0, 0, 1j, -1j]), np.diag([1j, -1j, 1j, -1j])),
    ('H_j', np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=complex),
            np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=complex)),
    ('H_k', np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1j],[0,0,1j,0]], dtype=complex),
            np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1j],[0,0,1j,0]], dtype=complex)),
]

for name, connes_gen, bapt_gen in comparisons:
    c_diag = [f"{connes_gen[i,i]:.0f}" if abs(connes_gen[i,i].imag) < 0.01
              else f"{connes_gen[i,i]}" for i in range(4)]
    b_diag = [f"{bapt_gen[i,i]:.0f}" if abs(bapt_gen[i,i].imag) < 0.01
              else f"{bapt_gen[i,i]}" for i in range(4)]
    c_str = f"diag({','.join(c_diag)})"
    b_str = f"diag({','.join(b_diag)})"
    print(f"  {name:<12} {c_str:<35} {b_str:<35}")

print(f"\n  KEY DIFFERENCES:")
print(f"  1. C_Im: Connes has (i, -i, 1, 1) vs Baptista (i, 1, 1, 1)")
print(f"     Connes: lambda acts as lambda on row 0, lambda_bar on row 1")
print(f"     Baptista: lambda acts as lambda on row 0 ONLY")
print(f"  2. H_i: Connes has (0, 0, i, -i) vs Baptista (i, -i, i, -i)")
print(f"     Connes: q only acts on rows 2-3 (left-handed)")
print(f"     Baptista: q acts on ALL rows (mixing R and L components)")
print(f"  3. H_j, H_k: IDENTICAL (both act on rows 2-3 only)")

print(f"\n  DIAGNOSIS:")
print(f"  The Baptista embedding MIXES C and H on rows 0-1.")
print(f"  In Connes, C acts on rows 0-1 (R-handed) and H on rows 2-3 (L-handed).")
print(f"  They are SEPARATED by chirality.")
print(f"  In Baptista, the SU(2) part of U(2) acts on ALL rows, not just L-handed.")
print(f"  This is because Baptista's L-action treats all internal directions equally.")


# =============================================================================
# PART 4: What D_F makes the Baptista embedding satisfy order-one?
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 4: FINDING D_F COMPATIBLE WITH BAPTISTA C+H")
print(f"{'=' * 76}")

# The Baptista C+H generators:
# C_Im = diag(i, 1, 1, 1)
# H_i = diag(i, -i, i, -i)
# H_j = off-diag on rows 2,3
# H_k = off-diag on rows 2,3

# The order-one condition for these generators is:
# [[D, C_Im], C_Im^dag] = 0, [[D, C_Im], H_i^dag] = 0, etc.
# [[D, H_i], C_Im^dag] = 0, [[D, H_i], H_i^dag] = 0, etc.

# Let D be a general hermitian 4x4 matrix (16 real parameters).
# Find all D such that [[D, a], b^dag] = 0 for all a, b in {C_Im, H_i, H_j, H_k}.

# Basis of hermitian 4x4 matrices:
herm_basis = []
herm_names = []
for a in range(4):
    E = np.zeros((4, 4), dtype=complex)
    E[a, a] = 1.0
    herm_basis.append(E)
    herm_names.append(f'E{a}{a}')
    for b in range(a+1, 4):
        E_re = np.zeros((4, 4), dtype=complex)
        E_re[a, b] = 1.0; E_re[b, a] = 1.0
        herm_basis.append(E_re)
        herm_names.append(f'E{a}{b}_Re')
        E_im = np.zeros((4, 4), dtype=complex)
        E_im[a, b] = 1j; E_im[b, a] = -1j
        herm_basis.append(E_im)
        herm_names.append(f'E{a}{b}_Im')

d_herm = len(herm_basis)  # should be 16
print(f"  Hermitian basis dimension: {d_herm}")

# Build constraint: [[D, a_k], a_l^dag] = 0 for all pairs (k,l) of Baptista generators
bapt_left = [
    np.diag([1j, 1.0, 1.0, 1.0]),  # C_Im
    np.diag([1j, -1j, 1j, -1j]),    # H_i
    np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=complex),  # H_j
    np.array([[0,0,0,0],[0,0,0,0],[0,0,0,1j],[0,0,1j,0]], dtype=complex), # H_k
]

constraints_D = []
for ak in bapt_left:
    for al in bapt_left:
        al_dag = al.conj().T
        for r in range(4):
            for c in range(4):
                row = np.zeros(d_herm)
                for h in range(d_herm):
                    D_test = herm_basis[h]
                    Da = D_test @ ak - ak @ D_test
                    dc = Da @ al_dag - al_dag @ Da
                    row[h] = dc[r, c].real
                if np.max(np.abs(row)) > 1e-14:
                    constraints_D.append(row)
                row_im = np.zeros(d_herm)
                for h in range(d_herm):
                    D_test = herm_basis[h]
                    Da = D_test @ ak - ak @ D_test
                    dc = Da @ al_dag - al_dag @ Da
                    row_im[h] = dc[r, c].imag
                if np.max(np.abs(row_im)) > 1e-14:
                    constraints_D.append(row_im)

A_D = np.array(constraints_D)
print(f"  Constraint matrix: {A_D.shape[0]} x {A_D.shape[1]}")

ATA_D = A_D.T @ A_D
evals_D, evecs_D = np.linalg.eigh(ATA_D)
tol_D = 1e-8 * max(np.max(np.abs(evals_D)), 1e-10)
null_D = evecs_D[:, evals_D < tol_D]

print(f"  Compatible D_F space dimension: {null_D.shape[1]}")

if null_D.shape[1] > 0:
    print(f"\n  Compatible D_F generators:")
    for k in range(null_D.shape[1]):
        v = null_D[:, k]
        D_gen = sum(v[h] * herm_basis[h] for h in range(d_herm))
        D_gen /= max(np.max(np.abs(D_gen)), 1e-10)
        print(f"\n  D_F generator {k+1}:")
        for r in range(4):
            row_str = "    ["
            for c in range(4):
                val = D_gen[r, c]
                if abs(val) < 1e-8:
                    row_str += "    .    "
                elif abs(val.imag) < 1e-8:
                    row_str += f" {val.real:+7.4f}"
                else:
                    row_str += f" {val.real:+.3f}{val.imag:+.3f}i"
                row_str += " "
            row_str += "]"
            print(row_str)

    # Check if any of these is the Baptista D_F (c<->b coupling)
    D_bapt = np.zeros((4, 4), dtype=complex)
    for j in range(1, 4):
        D_bapt[0, j] = 1.0; D_bapt[j, 0] = 1.0

    v_bapt = np.array([np.trace(herm_basis[h].conj().T @ D_bapt).real /
                        np.trace(herm_basis[h].conj().T @ herm_basis[h]).real
                        for h in range(d_herm)])

    proj = null_D @ (null_D.T @ v_bapt)
    resid = np.linalg.norm(v_bapt - proj) / np.linalg.norm(v_bapt)
    print(f"\n  Is Baptista D_F (c<->b) in compatible space? Residual: {resid:.4f}")
    if resid < 0.01:
        print("  YES!")
    else:
        print("  NO -- Baptista D_F is NOT compatible with Baptista C+H embedding!")

else:
    print("  Only D_F = 0 is compatible! The Baptista C+H embedding admits NO nontrivial D_F.")
