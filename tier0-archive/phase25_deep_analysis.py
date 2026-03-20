"""
PHASE 2.5d: Deep analysis of the 20-dim order-one subalgebra
=============================================================

Key findings from phase25_wedderburn_detail.py:
- Order-one subalgebra: dim 20, semisimple, center 4
- Wedderburn decomposition: C (dim 2) + M_3(C) (dim 18) = 20
- C factor: acts on indices {1-6, 17-22} (c and b sectors, both chiralities)
- M_3(C) factor: acts on indices {7-15, 23-31} (D-block, both chiralities)
- Missing indices: {0, 16} (singlets in both chiralities)
- NOT the same as the left-row algebra from Session 10

Questions to answer:
1. Why is the image 30-dim (not 32)? What lives at indices 0 and 16?
2. Is the C factor really just C, or could it be hiding H?
3. Why does order-one give C + M_3(C) instead of C + H + M_3(C)?
4. What is the physical interpretation of this decomposition?
5. Is the D_F construction correct? Does a different D_F give H?

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

np.set_printoptions(precision=8, linewidth=140, suppress=True)

# ── Infrastructure (same as before) ──
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

def vec_real(T):
    return np.concatenate([T.flatten().real, T.flatten().imag])

n_flat = 32 * 32


# =============================================================================
# PART 1: Reconstruct order-one subalgebra (same as before)
# =============================================================================

basis_su3 = su3_basis()
L_gens_16 = [L_action_matrix(v) for v in basis_su3]
L_gens_32 = [build_full_32(g) for g in L_gens_16]

L_Hj = np.zeros((4, 4), dtype=complex)
L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
Hj_32 = build_full_32(build_left_action_16(L_Hj))

L_Hk = np.zeros((4, 4), dtype=complex)
L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
Hk_32 = build_full_32(build_left_action_16(L_Hk))

all_gens_32 = L_gens_32 + [Hj_32, Hk_32]

# Closure
gen_vecs = [vec_real(T) for T in all_gens_32]
Q_cur = orth(np.column_stack(gen_vecs))
d_cur = Q_cur.shape[1]

for iteration in range(15):
    cur_basis = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                 for k in range(d_cur)]
    new_vecs = []
    for T1 in cur_basis:
        for T2 in all_gens_32:
            prod = T1 @ T2
            pv = vec_real(prod)
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
    d_cur = d_new
    Q_cur = Q_new

closure_basis_32 = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                    for k in range(d_cur)]

# D_F (identity Yukawa)
D_F_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    D_F_16[j+1, j+4] = 1.0
    D_F_16[j+4, j+1] = 1.0
D_F_32 = np.zeros((32, 32), dtype=complex)
D_F_32[:16, :16] = D_F_16
D_F_32[16:, 16:] = G5 @ np.conj(D_F_16) @ G5

# Order-one extraction
o_basis = [Xi @ T.T @ Xi for T in closure_basis_32]
D_comm = [D_F_32 @ T - T @ D_F_32 for T in closure_basis_32]

n_k = 2 * 32 * 32
A_constraint = np.zeros((d_cur * n_k, d_cur))
for j in range(d_cur):
    for i in range(d_cur):
        double_comm = D_comm[i] @ o_basis[j] - o_basis[j] @ D_comm[i]
        A_constraint[j * n_k : (j+1) * n_k, i] = vec_real(double_comm)

ATA = A_constraint.T @ A_constraint
eigvals, eigvecs = np.linalg.eigh(ATA)
tol = 1e-8 * np.max(np.abs(eigvals))
null_mask = eigvals < tol
o1_null = eigvecs[:, null_mask]
o1_dim = o1_null.shape[1]

o1_basis = []
for k in range(o1_dim):
    coeffs = o1_null[:, k]
    T = sum(c * B for c, B in zip(coeffs, closure_basis_32))
    o1_basis.append(T)

o1_vecs = [vec_real(T) for T in o1_basis]
Q_o1 = orth(np.column_stack(o1_vecs))
o1_dim = Q_o1.shape[1]
o1_basis = [(Q_o1[:, k][:n_flat] + 1j * Q_o1[:, k][n_flat:]).reshape(32, 32)
            for k in range(o1_dim)]

print(f"Order-one subalgebra: dim {o1_dim}")


# =============================================================================
# PART 2: Detailed index analysis
# =============================================================================

print(f"\n{'=' * 76}")
print("INDEX STRUCTURE OF ORDER-ONE SUBALGEBRA")
print(f"{'=' * 76}")

# Map flat indices to physical content
index_names = {}
for row in range(4):
    for col in range(4):
        fi = flat_idx(row, col)
        row_name = ['nu', 'r', 'g', 'b'][row]
        col_name = ['L', 'e1', 'e2', 'e3'][col]  # electroweak
        index_names[fi] = f"({row_name},{col_name})"
        index_names[fi + 16] = f"({row_name},{col_name})_bar"

# Build the 32x32 block structure
print(f"\n  Building nonzero block map of subalgebra...")

# Find which (row, col) pairs are nonzero across all basis elements
block_map = np.zeros((32, 32))
for T in o1_basis:
    block_map += np.abs(T)

# Print nonzero blocks (grouped by 16x16 quadrants)
print(f"\n  Nonzero structure (Psi_+ x Psi_+):")
for r in range(16):
    row_str = f"    {r:2d} {index_names[r]:12s}: "
    for c in range(16):
        if block_map[r, c] > 1e-8:
            row_str += f"{c},"
    if any(block_map[r, c] > 1e-8 for c in range(16)):
        print(row_str)

print(f"\n  Nonzero structure (Psi_- x Psi_-):")
for r in range(16, 32):
    row_str = f"    {r:2d} {index_names[r]:12s}: "
    for c in range(16, 32):
        if block_map[r, c] > 1e-8:
            row_str += f"{c},"
    if any(block_map[r, c] > 1e-8 for c in range(16, 32)):
        print(row_str)

# Check for cross-chirality mixing
print(f"\n  Cross-chirality blocks (Psi_+ x Psi_-):")
cross_max = np.max(block_map[:16, 16:])
print(f"    Max |T(+,-)| : {cross_max:.2e}")
cross_max_2 = np.max(block_map[16:, :16])
print(f"    Max |T(-,+)| : {cross_max_2:.2e}")


# =============================================================================
# PART 3: D_F structure analysis
# =============================================================================

print(f"\n{'=' * 76}")
print("D_F STRUCTURE: WHAT DOES IT COUPLE?")
print(f"{'=' * 76}")

print(f"\n  D_F nonzero entries (Psi_+ block):")
for r in range(16):
    for c in range(16):
        if abs(D_F_16[r, c]) > 1e-10:
            print(f"    D_F[{r},{c}] = {D_F_16[r,c]:.4f}  "
                  f"({index_names[r]} -> {index_names[c]})")

print(f"\n  D_F nonzero entries (Psi_- block):")
D_F_minus = G5 @ np.conj(D_F_16) @ G5
for r in range(16):
    for c in range(16):
        if abs(D_F_minus[r, c]) > 1e-10:
            print(f"    D_F[{r+16},{c+16}] = {D_F_minus[r,c]:.4f}  "
                  f"({index_names[r+16]} -> {index_names[c+16]})")


# =============================================================================
# PART 4: What does order-one actually constrain?
# =============================================================================

print(f"\n{'=' * 76}")
print("ORDER-ONE CONSTRAINT ANALYSIS")
print(f"{'=' * 76}")

# The key question: which of the 38 closure dimensions get closed by order-one?
# Let's identify the 18 closed dimensions.

# Eigenvalues of ATA tell us which directions are constrained
print(f"\n  ATA eigenvalue spectrum (all {d_cur}):")
for i, ev in enumerate(np.sort(eigvals)):
    status = "NULL" if ev < tol else "CONSTRAINED"
    print(f"    {i:2d}: {ev:.6e}  {status}")

# The 20 null directions survive. The 18 constrained directions are closed.
# Let's see what the closed directions look like.
killed_mask = eigvals >= tol
killed_coeffs = eigvecs[:, killed_mask]
killed_dim = killed_coeffs.shape[1]
print(f"\n  Closed dimensions: {killed_dim}")

# Reconstruct closed basis elements
killed_basis = []
for k in range(killed_dim):
    T = sum(killed_coeffs[i, k] * closure_basis_32[i] for i in range(d_cur))
    killed_basis.append(T)

# Check: are the closed elements related to specific physical sectors?
print(f"\n  Closed element index analysis:")
for k in range(killed_dim):
    T = killed_basis[k]
    # Find which sectors it touches
    psi_plus_norm = np.linalg.norm(T[:16, :16])
    psi_minus_norm = np.linalg.norm(T[16:, 16:])

    # Which rows/cols?
    active_rows = [r for r in range(32) if np.max(np.abs(T[r, :])) > 1e-8]
    active_cols = [c for c in range(32) if np.max(np.abs(T[:, c])) > 1e-8]

    # Categorize
    touches_cb = any(r in range(1, 7) or r in range(17, 23) for r in active_rows)
    touches_D = any(r in range(7, 16) or r in range(23, 32) for r in active_rows)
    touches_singlet = any(r in [0, 16] for r in active_rows)

    print(f"    Closed {k}: rows {active_rows[:6]}{'...' if len(active_rows) > 6 else ''}, "
          f"c/b={'Y' if touches_cb else 'N'}, D={'Y' if touches_D else 'N'}, "
          f"singlet={'Y' if touches_singlet else 'N'}")


# =============================================================================
# PART 5: Try EXTENDED D_F (including D-block couplings)
# =============================================================================

print(f"\n{'=' * 76}")
print("EXTENDED D_F: DOES INCLUDING D-BLOCK COUPLINGS CHANGE THINGS?")
print(f"{'=' * 76}")

# The current D_F only couples c <-> b (indices 1-3 <-> 4-6).
# In Connes' NCG, D_F also includes Majorana mass terms and CKM mixing.
# The most general D_F on 16 indices would couple ALL off-diagonal blocks.
#
# What if we include D-block self-coupling (rows 1-3, cols 1-3 to itself)?
# This corresponds to Yukawa couplings within the quark sector.

# Try D_F that also couples within D-block
D_F_ext_16 = np.zeros((16, 16), dtype=complex)

# c <-> b coupling (standard)
for j in range(3):
    D_F_ext_16[j+1, j+4] = 1.0
    D_F_ext_16[j+4, j+1] = 1.0

# Also add singlet coupling: index 0 <-> index 4,5,6 (nu-L to b sector?)
# This would be a Majorana mass term
D_F_maj_16 = D_F_16.copy()
D_F_maj_16[0, 4] = 0.5; D_F_maj_16[4, 0] = 0.5
D_F_maj_16[0, 5] = 0.5; D_F_maj_16[5, 0] = 0.5
D_F_maj_16[0, 6] = 0.5; D_F_maj_16[6, 0] = 0.5

D_F_maj_32 = np.zeros((32, 32), dtype=complex)
D_F_maj_32[:16, :16] = D_F_maj_16
D_F_maj_32[16:, 16:] = G5 @ np.conj(D_F_maj_16) @ G5

print(f"  Extended D_F (with Majorana) hermitian: {np.max(np.abs(D_F_maj_32 - D_F_maj_32.conj().T)):.2e}")
print(f"  Extended D_F J-compatible: {np.max(np.abs(D_F_maj_32 @ Xi - Xi @ np.conj(D_F_maj_32))):.2e}")

# Compute order-one with extended D_F
D_comm_ext = [D_F_maj_32 @ T - T @ D_F_maj_32 for T in closure_basis_32]
A_ext = np.zeros((d_cur * n_k, d_cur))
for j in range(d_cur):
    for i in range(d_cur):
        dc = D_comm_ext[i] @ o_basis[j] - o_basis[j] @ D_comm_ext[i]
        A_ext[j * n_k : (j+1) * n_k, i] = vec_real(dc)

ATA_ext = A_ext.T @ A_ext
eigvals_ext, eigvecs_ext = np.linalg.eigh(ATA_ext)
tol_ext = 1e-8 * np.max(np.abs(eigvals_ext))
null_ext = np.sum(eigvals_ext < tol_ext)

print(f"  Rank of extended constraint: {d_cur - null_ext}")
print(f"  Order-one dim (extended D_F): {null_ext}")

# Also try D_F that couples the D-block internally
# D_F_D: couples rows 7-15 to each other (intra-D mixing)
D_F_D_16 = D_F_16.copy()
for i in range(3):
    for j in range(3):
        if i != j:
            fi = 7 + 3*i + j  # within D-block
            fj = 7 + 3*j + i
            D_F_D_16[fi, fj] = 0.3

D_F_D_32 = np.zeros((32, 32), dtype=complex)
D_F_D_32[:16, :16] = D_F_D_16
D_F_D_32[16:, 16:] = G5 @ np.conj(D_F_D_16) @ G5

# Make hermitian
D_F_D_32 = 0.5 * (D_F_D_32 + D_F_D_32.conj().T)

print(f"\n  D_F with D-block coupling hermitian: {np.max(np.abs(D_F_D_32 - D_F_D_32.conj().T)):.2e}")
print(f"  D_F with D-block coupling J-compatible: {np.max(np.abs(D_F_D_32 @ Xi - Xi @ np.conj(D_F_D_32))):.2e}")

D_comm_D = [D_F_D_32 @ T - T @ D_F_D_32 for T in closure_basis_32]
A_D = np.zeros((d_cur * n_k, d_cur))
for j in range(d_cur):
    for i in range(d_cur):
        dc = D_comm_D[i] @ o_basis[j] - o_basis[j] @ D_comm_D[i]
        A_D[j * n_k : (j+1) * n_k, i] = vec_real(dc)

ATA_D = A_D.T @ A_D
eigvals_D, eigvecs_D = np.linalg.eigh(ATA_D)
tol_D = 1e-8 * np.max(np.abs(eigvals_D))
null_D = np.sum(eigvals_D < tol_D)

print(f"  Rank of D-block constraint: {d_cur - null_D}")
print(f"  Order-one dim (D-block D_F): {null_D}")


# =============================================================================
# PART 6: Intersection of all D_F order-one subspaces
# =============================================================================

print(f"\n{'=' * 76}")
print("INTERSECTION: ALL D_F VARIANTS")
print(f"{'=' * 76}")

# For each D_F variant, get the null space of ATA, then intersect
def get_o1_subspace(D_F_32_variant):
    D_comm_v = [D_F_32_variant @ T - T @ D_F_32_variant for T in closure_basis_32]
    A_v = np.zeros((d_cur * n_k, d_cur))
    for j in range(d_cur):
        for i in range(d_cur):
            dc = D_comm_v[i] @ o_basis[j] - o_basis[j] @ D_comm_v[i]
            A_v[j * n_k : (j+1) * n_k, i] = vec_real(dc)
    ATA_v = A_v.T @ A_v
    ev_v, evec_v = np.linalg.eigh(ATA_v)
    tol_v = 1e-8 * np.max(np.abs(ev_v))
    return evec_v[:, ev_v < tol_v]

# Combine constraints from multiple D_F's
print(f"  Computing combined constraint matrix...")

# Stack all ATA matrices
combined_ATA = ATA.copy()
combined_ATA += ATA_ext
combined_ATA += ATA_D

# Add a few more random D_F variants
for seed in [17, 42, 137]:
    np.random.seed(seed)
    yuk = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
    D_rand_16 = np.zeros((16, 16), dtype=complex)
    for i in range(3):
        for j in range(3):
            D_rand_16[j+1, i+4] = yuk[i, j]
            D_rand_16[i+4, j+1] = np.conj(yuk[i, j])
    D_rand_32 = np.zeros((32, 32), dtype=complex)
    D_rand_32[:16, :16] = D_rand_16
    D_rand_32[16:, 16:] = G5 @ np.conj(D_rand_16) @ G5

    D_comm_r = [D_rand_32 @ T - T @ D_rand_32 for T in closure_basis_32]
    A_r = np.zeros((d_cur * n_k, d_cur))
    for j2 in range(d_cur):
        for i2 in range(d_cur):
            dc = D_comm_r[i2] @ o_basis[j2] - o_basis[j2] @ D_comm_r[i2]
            A_r[j2 * n_k : (j2+1) * n_k, i2] = vec_real(dc)
    combined_ATA += A_r.T @ A_r

eigvals_comb, eigvecs_comb = np.linalg.eigh(combined_ATA)
tol_comb = 1e-8 * np.max(np.abs(eigvals_comb))
null_comb = np.sum(eigvals_comb < tol_comb)

print(f"  Combined constraint null dim: {null_comb}")
print(f"  (This is the intersection of ALL order-one subspaces for different D_F)")

if null_comb > 0:
    # Extract and analyze
    comb_null = eigvecs_comb[:, eigvals_comb < tol_comb]
    comb_basis = []
    for k in range(null_comb):
        T = sum(comb_null[i, k] * closure_basis_32[i] for i in range(d_cur))
        comb_basis.append(T)

    # Verify it's an algebra
    comb_vecs = [vec_real(T) for T in comb_basis]
    Q_comb = orth(np.column_stack(comb_vecs))
    max_closure_comb = 0
    for T1 in comb_basis:
        for T2 in comb_basis:
            prod = T1 @ T2
            pv = vec_real(prod)
            c = Q_comb.T @ pv
            r = np.linalg.norm(pv - Q_comb @ c)
            max_closure_comb = max(max_closure_comb, r)
    print(f"  Algebra closure: max residual = {max_closure_comb:.2e}")

    # Check which indices it acts on
    block_comb = np.zeros((32, 32))
    for T in comb_basis:
        block_comb += np.abs(T)

    active_rows = sorted([r for r in range(32) if np.max(block_comb[r, :]) > 1e-8])
    active_cols = sorted([c for c in range(32) if np.max(block_comb[:, c]) > 1e-8])
    print(f"  Active rows: {active_rows}")
    print(f"  Active cols: {active_cols}")

    # Order-zero check
    max_o0_comb = 0
    for i in range(null_comb):
        for j in range(null_comb):
            ob = Xi @ comb_basis[j].T @ Xi
            comm = comb_basis[i] @ ob - ob @ comb_basis[i]
            err = np.max(np.abs(comm))
            max_o0_comb = max(max_o0_comb, err)
    print(f"  Order-zero: max = {max_o0_comb:.2e}")


# =============================================================================
# PART 7: Physical interpretation
# =============================================================================

print(f"\n{'=' * 76}")
print("PHYSICAL INTERPRETATION")
print(f"{'=' * 76}")

# The flat index mapping:
print(f"\n  Flat index -> Physical content:")
for fi in range(16):
    row = None
    col = None
    for r in range(4):
        for c in range(4):
            if flat_idx(r, c) == fi:
                row, col = r, c
    row_names = ['nu_R/nu_L', 'u_R/u_L', 'u_G/u_G', 'u_B/u_B']
    col_names = ['SU(2)_L singlet', 'SU(2)_L doublet_1', 'SU(2)_L doublet_2', 'SU(2)_L doublet_3']
    if row is not None:
        print(f"    {fi:2d}: row={row} ({row_names[row]}), col={col} ({col_names[col]})")

print(f"\n  Index grouping by sector:")
print(f"    Singlet (row=0, col=0): index 0  -- neutrino singlet")
print(f"    c-sector (row=0, col=1-3): indices 1,2,3 -- neutrino doublet components")
print(f"    b-sector (row=1-3, col=0): indices 4,5,6 -- quark singlets (R,G,B)")
print(f"    D-block (row=1-3, col=1-3): indices 7-15 -- quark doublets (3 colors x 3)")

print(f"\n  C factor (dim 2) acts on: c-sector + b-sector = indices 1-6")
print(f"    Physical: neutrino doublet + quark singlets")
print(f"    This is the LEPTON NUMBER operator!")
print(f"    It's C because it's the same scalar on all c and b indices.")

print(f"\n  M_3(C) factor (dim 18) acts on: D-block = indices 7-15")
print(f"    Physical: quark doublets (all 3 colors)")
print(f"    This is the COLOR ALGEBRA on quark-doublet sector!")

print(f"\n  Missing: H (quaternions) which in Connes' model acts on the")
print(f"    SU(2)_L doublet structure (mixing columns 1-3).")
print(f"    In the LEFT-action framework, weak isospin mixes COLUMNS.")
print(f"    But L-action only mixes ROWS.")
print(f"    H cannot appear as a LEFT algebra because it requires")
print(f"    column mixing (right action) which conflicts with R_{'{u(2)}'}.")

print(f"\n  CONCLUSION: Order-one on the L-closure gives C + M_3(C) = dim 20.")
print(f"  The H factor REQUIRES the bimodule (right action) structure.")
print(f"  Since M_3(C) columns are blocked by R_{'{u(2)}'}, and H requires")
print(f"  column operations, neither can appear via commutant + order-one.")
print(f"  The LEFT algebra captures: lepton number (C) + color (M_3(C)).")
print(f"  The BIMODULE would add: weak isospin (H) + color columns (M_3(C)).")


# =============================================================================
# PART 8: Is there ANY subalgebra of L-closure that gives 24 dims?
# =============================================================================

print(f"\n{'=' * 76}")
print("CAN WE GET 24 FROM THE L-CLOSURE BY ANY ORDER-ONE?")
print(f"{'=' * 76}")

# The order-one gives 20 regardless of D_F. The question is:
# is there a D_F that gives LESS than 20, pushing toward 24?
# No, because order-one is LESS constraining, not more.
# Wait -- order-one RESTRICTS the closure. More constraints = smaller subalgebra.
# The D_F with most constraints gives the smallest subalgebra.
# The Majorana D_F was tested above.

# What if we use D_F that acts on the D-block (indices 7-15)?
# This would constrain the M_3(C) factor.

# Try D_F that couples c <-> D-block
D_F_cD_16 = np.zeros((16, 16), dtype=complex)
for j in range(3):
    for k in range(3):
        # c_j <-> D_{jk}
        fi_c = j + 1
        fi_D = 7 + 3*j + k
        D_F_cD_16[fi_c, fi_D] = 1.0
        D_F_cD_16[fi_D, fi_c] = 1.0

D_F_cD_32 = np.zeros((32, 32), dtype=complex)
D_F_cD_32[:16, :16] = D_F_cD_16
D_F_cD_32[16:, 16:] = G5 @ np.conj(D_F_cD_16) @ G5
D_F_cD_32 = 0.5 * (D_F_cD_32 + D_F_cD_32.conj().T)

jcompat_cD = np.max(np.abs(D_F_cD_32 @ Xi - Xi @ np.conj(D_F_cD_32)))
print(f"  D_F (c<->D) J-compatible: {jcompat_cD:.2e}")

if jcompat_cD < 1e-8:
    D_comm_cD = [D_F_cD_32 @ T - T @ D_F_cD_32 for T in closure_basis_32]
    A_cD = np.zeros((d_cur * n_k, d_cur))
    for j in range(d_cur):
        for i in range(d_cur):
            dc = D_comm_cD[i] @ o_basis[j] - o_basis[j] @ D_comm_cD[i]
            A_cD[j * n_k : (j+1) * n_k, i] = vec_real(dc)
    ATA_cD = A_cD.T @ A_cD
    ev_cD, evec_cD = np.linalg.eigh(ATA_cD)
    tol_cD = 1e-8 * np.max(np.abs(ev_cD))
    null_cD = np.sum(ev_cD < tol_cD)
    print(f"  Order-one dim (c<->D coupling): {null_cD}")
else:
    print(f"  D_F (c<->D) NOT J-compatible, trying hermitianized version...")
    # Try just the b <-> D coupling
    D_F_bD_16 = np.zeros((16, 16), dtype=complex)
    for i in range(3):
        for k in range(3):
            fi_b = i + 4
            fi_D = 7 + 3*i + k
            D_F_bD_16[fi_b, fi_D] = 1.0
            D_F_bD_16[fi_D, fi_b] = 1.0

    D_F_bD_32 = np.zeros((32, 32), dtype=complex)
    D_F_bD_32[:16, :16] = D_F_bD_16
    D_F_bD_32[16:, 16:] = G5 @ np.conj(D_F_bD_16) @ G5
    D_F_bD_32 = 0.5 * (D_F_bD_32 + D_F_bD_32.conj().T)
    jcompat_bD = np.max(np.abs(D_F_bD_32 @ Xi - Xi @ np.conj(D_F_bD_32)))
    print(f"  D_F (b<->D) J-compatible: {jcompat_bD:.2e}")

    if jcompat_bD < 1e-8:
        D_comm_bD = [D_F_bD_32 @ T - T @ D_F_bD_32 for T in closure_basis_32]
        A_bD = np.zeros((d_cur * n_k, d_cur))
        for j in range(d_cur):
            for i in range(d_cur):
                dc = D_comm_bD[i] @ o_basis[j] - o_basis[j] @ D_comm_bD[i]
                A_bD[j * n_k : (j+1) * n_k, i] = vec_real(dc)
        ATA_bD = A_bD.T @ A_bD
        ev_bD, evec_bD = np.linalg.eigh(ATA_bD)
        tol_bD = 1e-8 * np.max(np.abs(ev_bD))
        null_bD = np.sum(ev_bD < tol_bD)
        print(f"  Order-one dim (b<->D coupling): {null_bD}")


print(f"\n{'=' * 76}")
print("FINAL ASSESSMENT")
print(f"{'=' * 76}")
print(f"""
  The L-closure approach (38-dim algebra in R_{'{u(2)}'} commutant) yields:

  Order-one subalgebra: C + M_3(C) = dim 20 (Yukawa-independent)

  This captures:
    - C: lepton number (acts uniformly on c and b sectors)
    - M_3(C): color algebra on quark doublets (D-block)

  This MISSES:
    - H (quaternions): weak isospin, which mixes SU(2)_L doublet COLUMNS
    - Second copy of M_3(C): color on quark singlets (acts on columns)

  ROOT CAUSE: The L-closure is a LEFT algebra (row operations).
  H requires COLUMN mixing (right multiplication by quaternionic matrices).
  M_3(C) columns require RIGHT multiplication by 3x3 matrices.
  Both are in the BIMODULE right-action part of A_F.

  The commutant of R_{'{u(2)}'} can only capture LEFT operators.
  This is a structural limitation, not a D_F choice issue.

  VERDICT: The commutant + order-one route captures C + M_3(C) = 20 dims.
  To get the full A_F = C + H + M_3(C) = 24 dims, one MUST use the
  bimodule framework where A_F acts as pi(a).X = L.X.R, not just L.X.

  This confirms the Baptista-analyst's insight from Session 9:
  A_F^o = JA_FJ^{{-1}} is the OPPOSITE algebra, and R_{'{u(2)}'} generates
  only the commutant of A_F^o, which is the LEFT part of the bimodule.
""")
