"""
DEBUG v6: Clean irrep decomposition of Psi_+ and Psi_- under u(2),
then construct A_F embedding and verify J-compatibility.
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    gell_mann_matrices, su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix, LR_action_matrix,
)

np.set_printoptions(precision=6, linewidth=120, suppress=True)

# Setup
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

# ===================================================================
# Irrep decomposition of Psi_+ under u(2)_{L+R}
# ===================================================================

print("=" * 70)
print("IRREP DECOMPOSITION OF Psi_+ UNDER u(2)_{L+R}")
print("=" * 70)

# The u(2) basis in su(3) is: phi_*(a) = diag(-tr(a), a) for a in u(2)
# The su(2) part of u(2): traceless 2x2 anti-Hermitian = -i*sigma_k/2
# The u(1) part: -i*I_2/2 (or similar)

# basis_u2[0..2] = su(2) generators embedded in su(3)
# basis_u2[3] = u(1) generator embedded in su(3)

# Get the L+R matrices
rho = [LR_action_matrix(v) for v in basis_u2]

# SU(2) Casimir: C_2 = -sum(rho_k^2) for k=0,1,2
# (minus because generators are anti-Hermitian: rho_k^dag = -rho_k)
# C_2 eigenvalues = j(j+1) * normalization factor
# The normalization: our generators are rho_k = LR(-i*sigma_k/2 embedded)
# For spin j: C_2 = sum(J_k^2) where J_k = -i*sigma_k/2 for spin 1/2
# J_k are anti-Hermitian, so sum(J_k^2) is negative: = -j(j+1) * something

# Let me just compute: H_k = i * rho_k are Hermitian
H = [1j * r for r in rho[:3]]
C2 = sum(h @ h for h in H)

print("SU(2) Casimir C2 = sum_k (i*rho_k)^2 eigenvalues:")
c2_evals = np.linalg.eigvalsh(C2)
print(f"  {np.sort(np.round(c2_evals, 4))}")

# U(1) charge: Y = i * rho_3 (Hermitian)
Y_op = 1j * rho[3]
print(f"\nU(1) generator Y = i*rho_3 eigenvalues:")
y_evals = np.linalg.eigvalsh(Y_op)
print(f"  {np.sort(np.round(y_evals, 4))}")

# Verify [C2, Y] = 0
print(f"[C2, Y] = {np.max(np.abs(C2 @ Y_op - Y_op @ C2)):.2e}")

# Joint diagonalization
c2_vals, c2_vecs = np.linalg.eigh(C2)
c2_r = np.round(c2_vals, 3)
unique_c2 = np.unique(c2_r)

print("\nJoint (j, Y) decomposition:")
total = 0
for c2v in unique_c2:
    mask = np.abs(c2_r - c2v) < 1e-2
    V = c2_vecs[:, mask]
    dim_c2 = V.shape[1]

    # j from j(j+1) = c2v (with appropriate normalization)
    # Our generators H_k = i * rho_k where rho_k represents -i*sigma_k/2 embedded
    # So H_k represents sigma_k/2 embedded. For spin j, C2 = j(j+1).
    # But the embedding via phi_* may introduce scaling.
    # Let me just compute j from the eigenvalue.
    if c2v >= 0:
        j_val = (-1 + np.sqrt(1 + 4*c2v)) / 2
    else:
        j_val = -1  # flag for negative

    # Y within this C2 eigenspace
    Y_proj = V.conj().T @ Y_op @ V
    y_vals, y_vecs = np.linalg.eigh(Y_proj)
    y_r = np.round(y_vals, 3)
    unique_y = np.unique(y_r)

    for yv in unique_y:
        y_mask = np.abs(y_r - yv) < 1e-2
        dim_jy = np.sum(y_mask)
        total += dim_jy

        if j_val >= 0:
            j_str = f"j={j_val:.2f}"
        else:
            j_str = f"C2={c2v:.3f}"

        # Identify particle
        p = "?"
        # C2 values: j=0 -> 0, j=1/2 -> 0.75, j=1 -> 2
        if abs(c2v) < 0.1:  # j=0
            if abs(yv) < 0.1 and dim_jy == 1: p = "nu_R"
            elif abs(yv + 1) < 0.1 and dim_jy == 1: p = "e_R"
            elif abs(yv - 2/3) < 0.1 and dim_jy == 3: p = "u_R (color)"
            elif abs(yv + 1/3) < 0.1 and dim_jy == 3: p = "d_R (color)"
        elif abs(c2v - 0.75) < 0.1:  # j=1/2
            if abs(yv + 0.5) < 0.1 and dim_jy == 2: p = "(nu_L, e_L)"
            elif abs(yv - 1/6) < 0.1 and dim_jy == 6: p = "(u_L, d_L) x color"

        print(f"  {j_str}, Y={yv:+.3f}, dim={dim_jy}: {p}")

print(f"Total: {total}")

# ===================================================================
# Now: the KEY question. For the 80-dim J-compatible commutant from
# gauge = u(2)_{L+R}, the algebra is too big because of cross-sector
# intertwiners.
#
# The correct approach in NCG is NOT to compute the commutant of the
# gauge group. Instead, we should:
#
# 1. Identify the algebra A_F as a SUBALGEBRA of End(H_F)
# 2. Check that J defines a valid real structure on (A_F, H_F)
#
# The algebra A_F in Connes' SM is determined by the requirement that
# it acts DIFFERENTLY on particles with different quantum numbers.
# Specifically:
#
# For lambda in C: acts as lambda on RIGHT-HANDED LEPTONS, conj(lambda) on
#   LEFT-HANDED LEPTONS (via J)
# For q in H: acts as q on LEFT-HANDED DOUBLETS
# For m in M_3(C): acts as m on QUARKS (color)
#
# The commutant of pi(A_F) in End(H_F) then gives the gauge group.
#
# So the correct computation is:
# 1. Use the irrep decomposition to define pi(A_F)
# 2. Check that J is compatible with this action
# 3. Verify Connes' axioms
#
# Let me construct pi(A_F) explicitly from the irrep decomposition.
# ===================================================================

print("\n" + "=" * 70)
print("CONSTRUCTING pi(A_F) FROM IRREP DECOMPOSITION")
print("=" * 70)

# Step 1: Find the simultaneous eigenspaces on Psi_+ (C^16)
# We need to identify the subspaces corresponding to each SM field.

# Build the projectors onto irrep subspaces
# First, jointly diagonalize C2 and Y on C^16
full_evals_C2, full_evecs = np.linalg.eigh(C2)
Y_in_C2_basis = full_evecs.conj().T @ Y_op @ full_evecs

# This should be block-diagonal in the C2 eigenspaces
# Diagonalize within each C2 block
perm = np.argsort(full_evals_C2)
sorted_evecs = full_evecs[:, perm]
sorted_C2 = full_evals_C2[perm]

# Refine: diagonalize Y within C2 eigenspaces
final_basis = np.zeros((16, 16), dtype=complex)
labels = []

idx = 0
while idx < 16:
    c2v = sorted_C2[idx]
    # Find all indices with same C2 eigenvalue
    end = idx
    while end < 16 and abs(sorted_C2[end] - c2v) < 1e-4:
        end += 1

    V_block = sorted_evecs[:, idx:end]
    Y_block = V_block.conj().T @ Y_op @ V_block
    y_vals, y_vecs = np.linalg.eigh(Y_block)

    for k in range(end - idx):
        final_basis[:, idx + k] = V_block @ y_vecs[:, k]
        j_val = (-1 + np.sqrt(max(0, 1 + 4*c2v))) / 2
        labels.append((round(j_val, 2), round(y_vals[k], 3)))

    idx = end

print(f"Eigenbasis labels (j, Y):")
for k, (j, Y) in enumerate(labels):
    print(f"  k={k}: j={j}, Y={Y:+.3f}")

# Group by (j, Y) to identify SM multiplets
from collections import defaultdict
groups = defaultdict(list)
for k, (j, Y) in enumerate(labels):
    groups[(j, Y)].append(k)

print(f"\nMultiplet structure:")
for (j, Y), indices in sorted(groups.items()):
    print(f"  (j={j}, Y={Y:+.3f}): indices {indices}, mult={len(indices)}")

# ===================================================================
# Now construct the A_F action on Psi_+ in the eigenbasis
# ===================================================================

# In the eigenbasis of (j, Y), A_F = C + H + M_3(C) acts as:
#
# The STANDARD Connes action on particles (Psi_+):
# nu_R (j=0, Y=0): lambda acts as lambda
# e_R (j=0, Y=-1): lambda acts as conj(lambda)
# u_R^r,g,b (j=0, Y=2/3): m_{ij} acts on the color index
# d_R^r,g,b (j=0, Y=-1/3): m_{ij} acts on the color index
# (nu_L, e_L) (j=1/2, Y=-1/2): q acts as quaternion on the doublet
# (u_L, d_L)^r,g,b (j=1/2, Y=1/6): q tensor m acts as quaternion x color

# Wait, this isn't quite right. Let me look up the standard Connes embedding.
# In Connes' SM (e.g., arXiv:0706.3688):
#
# H_F = C^{32} for one generation
# A_F = C + H + M_3(C)
# For (lambda, q, m) in A_F:
#
# On RIGHT-HANDED particles (Psi_+ top block, gamma_F = +1):
#   nu_R: lambda (complex number)
#   e_R: conj(lambda)
#   u_R^a: lambda * delta_{ab} (lambda on each color, trivially)
#   d_R^a: lambda * delta_{ab}
#
# Wait, actually the standard Connes action is:
# pi(lambda, q, m) on the particle Hilbert space H_p = C^{16} is:
#
#   nu_R -> lambda * nu_R
#   e_R -> conj(lambda) * e_R
#   (nu_L, e_L) -> q * (nu_L, e_L)   (quaternion acting on doublet)
#   u_R^a -> (sum_b m_{ab}) * u_R^b = m acting on color
#   d_R^a -> (sum_b m_{ab}) * d_R^b = m acting on color
#   (u_L, d_L)^a -> q tensor delta_{ab} * (u_L, d_L)^b
#
# Hmm, I'm mixing up different conventions. Let me just directly
# construct the action based on what the commutant SHOULD be.

# KEY INSIGHT: Instead of constructing A_F and checking J,
# let me check what happens if I use the BLOCK-DIAGONAL part
# of the 80-dim J-compatible commutant.
#
# The block-diagonal part (A-sector from v2) has dim 2*20 = 40 real.
# Within that, the J-condition pairs A with D = G5*conj(A)*G5.
# So the independent part is A in End_{U(2)}(Psi_+) = Phase 1 commutant (dim 20 complex).
#
# The J condition restricts: for each A in the Phase 1 commutant,
# the corresponding D = G5*conj(A)*G5 is determined.
# The REAL degrees of freedom: A has 20 complex = 40 real DOF,
# but the J condition A = G5*conj(D)*G5 = G5*conj(G5*conj(A)*G5)*G5 = A
# is automatically satisfied (trivial constraint).
# So the block-diagonal part has 40 real DOF.
#
# This is twice the Phase 1 commutant, which was
# End_{U(2)}(Psi_+) = C + M_2(C) + M_3(R) + R = 1 + 4 + 9 + 1 = 15 complex dim
# Wait, Phase 1 found 20 complex dim. Let me recheck.
# C: dim 1, M_2(C): dim 4, M_3(R): dim 9 (but real!), R: dim 1 (real)
# Complex dimensions: C=1, M_2(C)=4, M_3(R)=9 (real basis, complex embedding),
# R=1 (real basis, complex embedding)
# Total COMPLEX dim = 1 + 4 + 9 + 1 = 15? But Phase 1 found 20.
#
# Hmm, the Phase 1 result: End_{U(2)}(Psi_+) has complex dimension 20.
# The Wedderburn decomposition was: C + M_2(C) + M_3(R) + R.
# Real dimensions: C=2, M_2(C)=8, M_3(R)=9, R=1. Total real = 20.
# Complex dimensions as complex algebras: C=1, M_2(C)=4.
# For M_3(R): it's a REAL algebra embedded in complex matrices. Its complex
# span in M_n(C) has complex dimension 9.
# For R: complex dimension 1 (real scalar times identity).
# So total complex dim = 1 + 4 + 9 + 1 = 15? Or 1 + 4 + 9 + 1 = 15?
#
# Actually, Phase 1 found null space dimension 20. The algebra C + M_2(C) + M_3(R) + R:
# Over C: C has complex dim 1, M_2(C) has complex dim 4,
# M_3(R) embedded in M_3(C) has complex dim 9 (a 9-real-dim subspace of a 9-complex-dim space),
# R embedded in C has complex dim 1.
# As a subspace of M_{16}(C): the embedding has complex dimension 1+4+9+1 = 15.
# But if M_3(R) is viewed as spanning ALL of M_3(C) when we allow complex coefficients,
# then the complex span has dim 9. Hmm.
#
# I think the answer is: the Phase 1 null space has complex dim 20, which means
# the commutant algebra, viewed as a complex vector space, has dim 20.
# This is: C(1) + M_2(C)(4) + M_3(C)(9) + C(1) + ???(5)
# Actually 1 + 4 + 9 + 1 = 15, not 20. So where do the extra 5 come from?
#
# Oh! The Phase 1 decomposition found 6 irreps, not 4 factors!
# Let me re-read the Phase 1 result more carefully.

print("\n\n--- PHASE 1 COMMUTANT RECHECK ---")

# Compute the Phase 1 commutant from scratch
rho_gens_16 = [LR_action_matrix(v) for v in basis_u2]

constraint_16 = []
for rv in rho_gens_16:
    block = np.zeros((256, 256), dtype=complex)
    for i in range(16):
        for j in range(16):
            row = i*16 + j
            for k in range(16):
                block[row, i*16+k] += rv[k, j]
                block[row, k*16+j] -= rv[i, k]
    constraint_16.append(block)

A16 = np.vstack(constraint_16)
ns16 = null_space(A16, rcond=1e-10)
d16 = ns16.shape[1]
print(f"Phase 1 commutant complex dim: {d16}")

# Now decompose Psi_+ into irreps and count multiplicities
# From the (j, Y) groups above:
print(f"\nIrrep multiplicities:")
for (j, Y), indices in sorted(groups.items()):
    dim_rep = int(round(2*j + 1)) if j >= 0 else 1
    mult = len(indices) // dim_rep if dim_rep > 0 else len(indices)
    print(f"  (j={j}, Y={Y:+.3f}): dim_rep={dim_rep}, multiplicity={mult}, total={len(indices)}")

# Commutant dim = sum of mult^2 for each irrep (Schur's lemma)
# But for complex vs real vs quaternionic irreps, it's different:
# Complex irrep: M_{mult}(C), contributes mult^2 complex dim
# Real irrep: M_{mult}(R), contributes mult^2 real dim = mult^2/2 complex dim (if we count over R)
# Quaternionic irrep: M_{mult}(H), contributes mult^2 quaternionic dim

# Actually, for the commutant of a group representation on a COMPLEX vector space:
# End_G(V) = bigoplus_i M_{m_i}(C) where V = bigoplus_i m_i * V_i (complex irreps)
# This always gives M_{m_i}(C), regardless of the real/quaternionic type of V_i.
# The real/quaternionic type only matters when we impose a real structure (J).

comm_dim = sum(mult**2 for (j, Y), indices in sorted(groups.items())
               for mult in [len(indices) // max(1, int(round(2*j + 1))) if j >= 0 else len(indices)])

# Wait, that's messy. Let me compute it properly.
comm_dim = 0
for (j, Y), indices in sorted(groups.items()):
    dim_rep = int(round(2*j + 1)) if j >= 0 else 1
    mult = len(indices) // dim_rep if dim_rep > 0 else len(indices)
    contrib = mult**2
    comm_dim += contrib
    print(f"  (j={j}, Y={Y:+.3f}): mult={mult}, contributes M_{mult}(C) = {contrib} complex dim")

print(f"Total commutant complex dim: {comm_dim}")
print(f"Phase 1 found: {d16}")

if comm_dim != d16:
    print(f"MISMATCH: expected {comm_dim}, got {d16}")
    print("This suggests the irrep decomposition grouping is wrong.")
    print("Let me try with finer tolerance...")

    # Try using the actual eigenbasis to decompose more carefully
    # Build the change-of-basis matrix
    P = final_basis  # 16x16 unitary
    print(f"\nChange-of-basis P unitary? {np.allclose(P.conj().T @ P, np.eye(16))}")

    # Transform the generators to the eigenbasis
    rho_transformed = [P.conj().T @ rv @ P for rv in rho_gens_16]

    print(f"\nGenerators in eigenbasis (should be block-diagonal):")
    for g_idx, rt in enumerate(rho_transformed):
        # Check which blocks are nonzero
        print(f"  Generator {g_idx}:")
        for (j1, Y1), idx1 in sorted(groups.items()):
            for (j2, Y2), idx2 in sorted(groups.items()):
                block = rt[np.ix_(idx1, idx2)]
                norm = np.max(np.abs(block))
                if norm > 1e-8:
                    print(f"    ({j1},{Y1:+.3f}) x ({j2},{Y2:+.3f}): max={norm:.4f}")

print("\nDone.")
