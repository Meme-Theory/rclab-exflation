"""
DEBUG SCRIPT v5: Test the CORRECT Connes setup.

In Connes' NCG, the algebra A_F acts on H_F from the LEFT.
The opposite algebra A_F^o = J A_F^* J^{-1} acts from the RIGHT.

In Baptista's framework:
- L_v: left su(3) action on Psi
- R_v: right su(3) action on Psi
- L+R: combined action (homomorphism only for u(2))

The correct Connes setup:
- The gauge group for the LEFT action is u(2)_{L+R} (the part that IS a homomorphism)
- The RIGHT action (R_{su(3)}) should NOT be imposed as a constraint
- Instead, it should EMERGE from J * A_F^o * J^{-1}

So we should use:
(1) Gauge = u(2)_{L+R} (4 generators)
(2) J-compatibility: T * Xi = Xi * conj(T)
(3) Then CHECK: does J decompose the resulting algebra?

BUT: the issue from v2 was that this gives 80-dim algebra (too big).

New hypothesis: The problem is that with ONLY u(2)_{L+R}, the commutant
includes the full Hom(Psi_-, Psi_+) because Psi_+ and Psi_- are
isomorphic as u(2) representations. In Connes' framework, the LEFT
gauge group doesn't act on the Psi_- sector via the same representation.

Actually, let me reconsider. In Baptista's framework, the gauge action
on Psi_- is the CONJUGATE of the action on Psi_+:
  rho_-(v) = G5 * conj(rho_+(v)) * G5

This means Psi_- carries the CONJUGATE representation. For the commutant
to give A_F, we need the irreps in Psi_+ and Psi_- to NOT intertwine
(so that the off-diagonal blocks vanish).

But rho_+ and rho_- = conj(rho_+) (after G5 conjugation) DO share
irreps: a complex irrep R in rho_+ appears as conj(R) in rho_-,
and R and conj(R) intertwine via complex conjugation (for self-conjugate reps)
or don't (for truly complex reps).

The key question: which u(2) irreps in the decomposition of Psi_+
are self-conjugate (real or quaternionic) vs truly complex?

For truly complex irreps: Hom(R, conj(R)) = 0, so NO cross-sector intertwiners.
For self-conjugate irreps: Hom(R, conj(R)) = R or H, giving cross-sector intertwiners.

In Phase 1, the u(2) irreps in Psi_+ were identified. Let me check which
are self-conjugate.

Actually, maybe the issue is different. Let me try:
(a) L only on u(2) (4 generators of L restricted to u(2))
(b) L+R on u(2), but WITHOUT cross-sector intertwiners
(c) L+R on u(2), then project to block-diagonal part
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
n = 32

# ===================================================================
# APPROACH: Connes' commutant is NOT End_gauge(H_F),
# it's the ALGEBRA ITSELF.
#
# In NCG, we DON'T compute the commutant of the gauge group.
# Instead, the algebra A_F IS the object we're looking for.
# The gauge group is U(A_F) = the unitary elements of A_F.
#
# The relationship to Baptista is:
# A_F acts on H_F = C^32 via a representation pi: A_F -> End(H_F)
# This representation is determined by the particle content (eq 2.66).
#
# What Phase 1 actually computed was End_{gauge}(Psi_+), which gives
# the space of operators commuting with the gauge action.
# By Schur's lemma, this IS an algebra (the commutant algebra).
#
# For the standard SM spectral triple:
# H_F = C^{32} (one generation)
# A_F = C + H + M_3(C)
# pi: A_F -> End(H_F) embeds A_F into M_{32}(C)
# The image pi(A_F) should be exactly the commutant of the gauge group
# action, intersected with J-compatibility.
#
# But WHICH gauge group? The gauge group of the SM spectral triple is
# U(1) x SU(2) x SU(3). In Baptista's language:
# - SU(2) x U(1) comes from L (left su(3) restricted to u(2))
# - SU(3) comes from R (right su(3))
#
# The algebra A_F commutes with NONE of these -- it IS the gauge symmetry.
# The commutant of A_F in End(H_F) gives the gauge group.
#
# So the correct question is: find an algebra A in End(H_F) such that:
# 1. A is J-compatible: J * A * J^{-1} = A^{opp}
# 2. The gauge group U(A) reproduces SM gauge
# 3. Order-zero: [A, J*A*J^{-1}] = 0
#
# This is the REVERSE of what we've been doing.
# We should find A_F as a SUBALGEBRA of End(H_F), not as a commutant.
#
# HOWEVER, Connes' reconstruction theorem says:
# A_F = End_{U(A_F), J-compat}(H_F) -- but this is circular unless we
# know U(A_F) a priori.
#
# The NON-circular version: A_F is the unique algebra (up to isomorphism)
# satisfying:
# 1. J-compatibility
# 2. Order-zero condition
# 3. KO-dimension 6
# 4. Acts faithfully on C^32
# 5. Yields the correct particle content
#
# Let me instead directly CONSTRUCT the embedding pi: A_F -> M_{32}(C)
# using the particle content from eq 2.66, and then CHECK if this
# embedding is consistent with J = hat{Xi} o conj.
# ===================================================================

print("=" * 70)
print("DIRECT CONSTRUCTION: Embed A_F into End(C^32) via particle content")
print("=" * 70)

# From eq 2.66 and Connes' SM spectral triple, the standard embedding is:
#
# A_F = C + H + M_3(C)
# An element is (lambda, q, m) where:
#   lambda in C, q in H, m in M_3(C)
#
# The representation on H_F is determined by the particle content.
# For ONE generation (32 components = 16 particles + 16 antiparticles):
#
# From Phase 1, the decomposition of Psi_+ under u(2) was:
#   Psi_+(16) = (1,2,1/2) + (1,1,0)_a + (1,1,0)_c + (1,1,0)_D +
#               (3,2,1/6) + (3,1,-1/3) + (3,1,2/3)
#
# Wait, the actual Phase 1 result was:
# End_{U(2)_{L+R}}(Psi_+) = C + M_2(C) + M_3(R) + R
# with multiplicity pattern showing these irreps.
#
# Let me approach this differently: construct the KNOWN A_F embedding
# and then check if it matches the J from Baptista.

# Standard Connes embedding for one generation:
# Particle content of Psi_+ (from Baptista eq 2.66):
#
# Flattened Psi_+ indices:
# idx 0: a = nu_R  (singlet under SU(2), Y=0)
# idx 1: c_1 = u_R^r (singlet, Y=2/3, color r)
# idx 2: c_2 = u_R^g (singlet, Y=2/3, color g)
# idx 3: c_3 = u_R^b (singlet, Y=2/3, color b)
# idx 4: b_1 = e_R^-  (singlet, Y=-1)
# idx 5: b_2 = nu_L   (doublet upper, Y=-1/2)  <-- Wait, this is wrong
# idx 6: b_3 = e_L^-   (doublet lower, Y=-1/2)
# Hmm, I need to check the actual particle identification more carefully.

# Let me re-read the Phase 1 results to get the correct mapping.
# From the Phase 1 script output (branching_computation.py):

# Actually, the key info is in the irrep decomposition.
# Phase 1 found these irreducible subspaces of Psi_+(16) under U(2)_{L+R}:
#
# From the script output:
# The eigenvalues of the Casimir operators on each irreducible component
# identify the representation as (j, Y) = SU(2) spin x U(1) hypercharge.

# Let me just run Phase 1 quickly to get the decomposition.

print("\nRunning Phase 1 decomposition...")

# Build U(2) Casimirs
# The u(2) generators on Psi_+(C^16) are rho_+(v) for v in basis_u2.
# Casimir C_2 of SU(2): sum of (sigma_i/2)^2 = j(j+1)
# U(1) charge: the u(1) generator = i * I_2 / 2 (or similar)

# u(2) = su(2) + u(1)
# basis_u2[0] = i*sigma_1/2 (su(2))  -- actually depends on the convention
# basis_u2[1] = i*sigma_2/2
# basis_u2[2] = i*sigma_3/2
# basis_u2[3] = i*I_2/2 (u(1))
#
# But u2_basis_in_su3() embeds these into su(3) as:
# phi_*(a) = diag(-tr(a), a) for a in u(2)
# So the su(2) part uses sigma_1, sigma_2, sigma_3 in the lower 2x2 block
# and the u(1) part uses I_2 in the lower 2x2 block.

# The SU(2) Casimir on Psi_+:
rho_su2 = [LR_action_matrix(basis_u2[i]) for i in range(3)]  # first 3 = su(2)
rho_u1 = LR_action_matrix(basis_u2[3])  # 4th = u(1)

C2_su2 = sum(r @ r for r in rho_su2)
print(f"\nSU(2) Casimir eigenvalues on Psi_+(C^16):")
c2_evals = np.linalg.eigvalsh(C2_su2)
print(f"  {np.sort(np.round(c2_evals, 4))}")

print(f"\nU(1) generator eigenvalues on Psi_+(C^16):")
u1_evals = np.linalg.eigvalsh(1j * rho_u1)  # multiply by i since rho is anti-Hermitian
print(f"  {np.sort(np.round(u1_evals.real, 4))}")

# The irrep decomposition is determined by the joint eigenvalues of (C2, Y).
# C2 = j(j+1): j=0 -> C2=0, j=1/2 -> C2=3/4
# Y = hypercharge eigenvalue of the u(1) generator

# Diagonalize simultaneously
joint = C2_su2 + 100 * (1j * rho_u1)  # combine with large weight to separate
j_evals, j_evecs = np.linalg.eigh(joint.real)  # Hmm, this isn't right for joint diag

# Better: compute C2 and Y as commuting Hermitian operators, jointly diagonalize
# C2 is Hermitian, i*rho_u1 is Hermitian (since rho_u1 is anti-Hermitian)
Y_op = 1j * rho_u1

# Verify they commute
comm_CY = C2_su2 @ Y_op - Y_op @ C2_su2
print(f"\n[C2, Y] commutator: {np.max(np.abs(comm_CY)):.2e}")

# Joint diagonalization
# Since they commute, find simultaneous eigenbasis
# Method: diagonalize C2, then within each eigenspace diagonalize Y
c2_vals, c2_vecs = np.linalg.eigh(C2_su2)
c2_rounded = np.round(c2_vals, 4)
unique_c2 = np.unique(c2_rounded)

print("\nJoint (j, Y) decomposition of Psi_+(C^16):")
total = 0
irrep_spaces = []
for c2v in unique_c2:
    mask = np.abs(c2_rounded - c2v) < 1e-3
    V_c2 = c2_vecs[:, mask]
    dim_c2 = V_c2.shape[1]

    # Diagonalize Y within this eigenspace
    Y_proj = V_c2.conj().T @ Y_op @ V_c2
    y_vals, y_vecs_local = np.linalg.eigh(Y_proj)
    y_rounded = np.round(y_vals, 4)
    unique_y = np.unique(y_rounded)

    # j from C2 = j(j+1)
    j_val = (-1 + np.sqrt(1 + 4*c2v)) / 2
    j_str = f"{j_val:.1f}"

    for yv in unique_y:
        y_mask = np.abs(y_rounded - yv) < 1e-3
        dim_jy = np.sum(y_mask)
        V_jy = V_c2 @ y_vecs_local[:, y_mask]

        # This is a (j, Y) irrep with dimension dim_jy
        # For SU(2) spin j: dim = 2j+1
        # So the multiplicity = dim_jy / (2j+1)
        dim_rep = int(round(2*j_val + 1))
        if dim_rep > 0:
            mult = dim_jy // dim_rep
        else:
            mult = dim_jy

        total += dim_jy
        print(f"  j={j_str}, Y={yv:.4f}: dim={dim_jy} = {mult} x {dim_rep}")
        irrep_spaces.append({
            'j': j_val, 'Y': yv, 'dim': dim_jy,
            'mult': mult, 'rep_dim': dim_rep,
            'V': V_jy
        })

print(f"Total: {total}")

# ===================================================================
# Now construct the A_F embedding based on the irrep decomposition
# ===================================================================

print("\n\n--- CONSTRUCTING STANDARD A_F EMBEDDING ---")
print("The standard SM spectral triple has A_F = C + H + M_3(C)")
print("acting on one generation of fermions.")
print()
print("Standard action (Connes-Chamseddine):")
print("  lambda in C acts as: lambda on nu_R (j=0, singlet, no color)")
print("  q in H acts as: q on SU(2) doublets")
print("  m in M_3(C) acts as: m on color triplets")
print()
print("The commutant of this action gives the gauge group SU(2)xU(1)xSU(3).")
print()
print("In Baptista's framework, the question is whether the SPECIFIC")
print("particle assignments in eq 2.66 reproduce this standard embedding")
print("when combined with J = hat{Xi} o conj.")

# Let me identify which irreps correspond to which SM particles:
for irr in irrep_spaces:
    j, Y, dim, mult, rdim = irr['j'], irr['Y'], irr['dim'], irr['mult'], irr['rep_dim']
    # Standard SM quantum numbers (one generation, Psi_+):
    # nu_R: j=0, Y=0, color singlet -> dim 1
    # e_R: j=0, Y=-1, color singlet -> dim 1
    # u_R: j=0, Y=2/3, color triplet -> dim 3
    # d_R: j=0, Y=-1/3, color triplet -> dim 3
    # (nu_L, e_L): j=1/2, Y=-1/2, color singlet -> dim 2
    # (u_L, d_L): j=1/2, Y=1/6, color triplet -> dim 6

    particles = "?"
    if abs(j) < 0.1:  # j=0 (singlets)
        if abs(Y) < 0.1 and dim == 1:
            particles = "nu_R"
        elif abs(Y + 1) < 0.1 and dim == 1:
            particles = "e_R"
        elif abs(Y - 2/3) < 0.1 and dim == 3:
            particles = "u_R (color triplet)"
        elif abs(Y + 1/3) < 0.1 and dim == 3:
            particles = "d_R (color triplet)"
        elif dim == 3:
            particles = f"color triplet (Y={Y:.3f})"
        elif dim == 1:
            particles = f"singlet (Y={Y:.3f})"
    elif abs(j - 0.5) < 0.1:  # j=1/2 (doublets)
        if abs(Y + 0.5) < 0.1 and dim == 2:
            particles = "(nu_L, e_L) lepton doublet"
        elif abs(Y - 1/6) < 0.1 and dim == 6:
            particles = "(u_L, d_L) quark doublet (color triplet)"
        elif dim == 2:
            particles = f"doublet (Y={Y:.3f})"
        elif dim == 6:
            particles = f"doublet x triplet (Y={Y:.3f})"

    print(f"  j={j:.1f}, Y={Y:.4f}, dim={dim}: {particles}")

print("\nDone.")
