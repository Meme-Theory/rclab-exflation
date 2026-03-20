"""
DEBUG v7: REVERSE APPROACH.

Instead of computing the commutant and hoping it gives A_F,
construct the KNOWN Connes embedding of A_F into M_{32}(C)
using the particle identification from Baptista eq 2.66,
and then check if it's compatible with Baptista's J = hat{Xi} o conj.

The standard Connes embedding for one generation (arXiv:0706.3688):

A_F = C + H + M_3(C)
H_F = C^{32} = particles (C^16) + antiparticles (C^16)

For (lambda, q, m) in A_F:

On PARTICLES (Psi_+, indices 0-15):
  nu_R (idx 0):     lambda
  u_R^r (idx 1):    lambda
  u_R^g (idx 2):    lambda
  u_R^b (idx 3):    lambda
  e_R (idx 4):      conj(lambda)  -- WAIT, this is wrong for the LEFT action
  Actually, for the LEFT action of A_F on H_F (one generation):

  pi(lambda, q, m) on Psi_+ acts as:

  Leptons (color singlets):
    nu_R:     lambda * nu_R
    e_R:      conj(lambda) * e_R
    (nu_L, e_L) = q * (nu_L, e_L)  (q acts as 2x2 quaternion on the doublet)

  Quarks (color triplets):
    u_R^a:    sum_b m_{ab} * u_R^b
    d_R^a:    sum_b m_{ab} * d_R^b
    (u_L^a, d_L^a): sum_b m_{ab} * q * (u_L^b, d_L^b)

  Wait, this is not right either. The standard action is:

  In the PARTICLE sector:
  pi(lambda, q, m) = diag(lambda, q, ...) acting block-diagonally

  Let me look at the standard reference more carefully.

  From Connes-Chamseddine-Marcolli (0706.3688, eq 2.3):
  For a = (lambda, q, m) in C + H + M_3(C):

  The representation on H_F = (C^2 tensor C^N_c tensor C) + ... is:

  Actually, the key point is the MATRIX form in the particle basis.
  For one generation with N_c = 3 colors:

  H_F = H_R + H_L (right-handed + left-handed particles + antiparticles)

  The representation is:
  On right-handed particles:
    On leptons: lambda (for nu_R), conj(lambda) (for e_R)
    On quarks: lambda * I_3 (trivial on color for u_R), conj(lambda)*I_3 (for d_R)
  On left-handed particles:
    On leptons: q (2x2 quaternion on (nu_L, e_L))
    On quarks: q tensor I_3 (quaternion on isospin, trivial on color)

  Wait, the M_3(C) factor acts on the RIGHT (opposite algebra via J):
  J * m * J^{-1} acts on color from the RIGHT.

  Actually, this is confusing. Let me use a cleaner reference.

  From Suijlekom's textbook "Noncommutative Geometry and Particle Physics" (2015):

  For one generation, the finite Hilbert space is H_F with basis:
  { nu_R, e_R, u_R^1, u_R^2, u_R^3, d_R^1, d_R^2, d_R^3,
    nu_L, e_L, u_L^1, u_L^2, u_L^3, d_L^1, d_L^2, d_L^3 }
  for particles, and similarly for antiparticles.

  The LEFT action pi(lambda, q, m):
    nu_R -> lambda * nu_R
    e_R -> conj(lambda) * e_R
    u_R^a -> sum_b m_{ba} * u_R^b  [NOTE: m acts on color from the left, transposed]

  Wait no. Let me be very precise. The standard is:

  pi(a) for a = (lambda, q, m):

  On H_R (right-handed):
    lepton sector: diag(lambda, conj(lambda)) on (nu_R, e_R)
    quark sector: diag(lambda*I_3, conj(lambda)*I_3) on (u_R^{1,2,3}, d_R^{1,2,3})

  On H_L (left-handed):
    lepton sector: q acting on (nu_L, e_L) via quaternion action
    quark sector: q tensor I_3 acting on ((u_L, d_L)^{1,2,3})

  The M_3(C) factor does NOT appear in the LEFT action at all!
  It appears only via the opposite algebra: J m J^{-1}.

  So: pi_L(lambda, q, m) = pi_L(lambda, q) -- only depends on C and H parts.
  The M_3(C) acts from the RIGHT via J.

  This means: the algebra A_F restricted to its LEFT action on H_F
  is just C + H (real dim 2 + 4 = 6).
  The full A_F = C + H + M_3(C) appears because M_3(C) acts via J.

  For the LEFT action to give C + H:
  Complex dim of pi_L(A_F) in End(H_F) is:
    On right-handed sector (8 particles): lambda acts as 2x2 diagonal, giving 2 params
    On left-handed sector (8 particles): q acts as 2x2 quaternion tensor I_3, giving 4 params
    Total: not simply additive because of the block structure.

  Actually, the dimension of pi_L(C+H) in End(C^16) is:
    pi_L(lambda, q): lambda appears in multiple places, q in others.
    The image is a subalgebra of End(C^16) of real dimension <=6.

  The COMMUTANT of pi_L(C+H) in End(C^16) is what the gauge group comes from.
  And on the full C^32, the commutant of pi(A_F) (with J included) gives
  the full SM gauge group.

  OK let me just construct this explicitly.
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

# ===================================================================
# Particle identification from Baptista eq 2.66
# ===================================================================

# From eq 2.66, Psi_+ (the 4x4 internal matrix) has:
# Position (i,j) -> flattened index
#
# Row 0: a=nu_R     c_1=u_R^r    c_2=u_R^g    c_3=u_R^b
# Row 1: b_1=e_R^-  D_11=d_R^r   D_12=d_R^g   D_13=d_R^b
# Row 2: b_2=nu_L   D_21=u_L^r   D_22=u_L^g   D_23=u_L^b
# Row 3: b_3=e_L^-  D_31=d_L^r   D_32=d_L^g   D_33=d_L^b
#
# Flattened indices:
# 0: a = nu_R           (singlet, right-handed, Y=0)
# 1: c_1 = u_R^r        (singlet, right-handed, Y=2/3)
# 2: c_2 = u_R^g
# 3: c_3 = u_R^b
# 4: b_1 = e_R^-        (singlet, right-handed, Y=-1)
# 5: b_2 = nu_L         (doublet upper, left-handed, Y=-1/2)
# 6: b_3 = e_L^-        (doublet lower, left-handed, Y=-1/2)
# 7: D_11 = d_R^r       (singlet, right-handed, Y=-1/3)
# 8: D_12 = d_R^g
# 9: D_13 = d_R^b
# 10: D_21 = u_L^r      (doublet upper, left-handed, Y=1/6)
# 11: D_22 = u_L^g
# 12: D_23 = u_L^b
# 13: D_31 = d_L^r      (doublet lower, left-handed, Y=1/6)
# 14: D_32 = d_L^g
# 15: D_33 = d_L^b

particle_names = [
    'nu_R', 'u_R^r', 'u_R^g', 'u_R^b',
    'e_R^-', 'nu_L', 'e_L^-',
    'd_R^r', 'd_R^g', 'd_R^b',
    'u_L^r', 'u_L^g', 'u_L^b',
    'd_L^r', 'd_L^g', 'd_L^b',
]

# Grouping by SM multiplet:
idx_nu_R = [0]          # nu_R: (1, 1, 0)
idx_e_R = [4]           # e_R: (1, 1, -1)
idx_u_R = [1, 2, 3]    # u_R: (1, 1, 2/3) x color
idx_d_R = [7, 8, 9]    # d_R: (1, 1, -1/3) x color
idx_lep_L = [5, 6]     # (nu_L, e_L): (1, 2, -1/2)
idx_u_L = [10, 11, 12] # u_L: (1, 2, 1/6) x color (upper component of quark doublet)
idx_d_L = [13, 14, 15] # d_L: (1, 2, 1/6) x color (lower component of quark doublet)

# ===================================================================
# Construct pi(A_F) on Psi_+ (C^16)
# ===================================================================

print("=" * 70)
print("CONSTRUCTING pi(A_F) ON Psi_+ (C^16)")
print("=" * 70)

# The LEFT action of (lambda, q, m) in C + H + M_3(C) on Psi_+:
#
# Standard Connes embedding:
#   nu_R -> lambda * nu_R
#   e_R -> conj(lambda) * e_R
#   u_R^a -> lambda * u_R^a  (trivial on color)
#   d_R^a -> conj(lambda) * d_R^a  (trivial on color)
#   nu_L -> q_11 * nu_L + q_12 * e_L
#   e_L -> q_21 * nu_L + q_22 * e_L
#   u_L^a -> q_11 * u_L^a + q_12 * d_L^a  (quaternion on isospin, trivial on color)
#   d_L^a -> q_21 * u_L^a + q_22 * d_L^a
#
# Where q = (q_11, q_12; q_21, q_22) is a quaternion matrix:
# q in H iff q = alpha*I + beta_1*i*sigma_1 + beta_2*i*sigma_2 + beta_3*i*sigma_3
# This means q = (alpha + i*beta_3, beta_2 + i*beta_1;
#                 -beta_2 + i*beta_1, alpha - i*beta_3)
# with alpha, beta_1, beta_2, beta_3 real.

# Construct basis for pi(A_F):

# pi(lambda=1, q=0, m=0): lambda acts on right-handed particles
pi_lambda_re = np.zeros((16, 16), dtype=complex)
pi_lambda_re[0, 0] = 1      # nu_R -> lambda * nu_R
pi_lambda_re[1, 1] = 1      # u_R^r -> lambda * u_R^r
pi_lambda_re[2, 2] = 1      # u_R^g
pi_lambda_re[3, 3] = 1      # u_R^b
# conj(lambda) on e_R and d_R -- for lambda = 1 (real), conj(1) = 1
pi_lambda_re[4, 4] = 1      # e_R
pi_lambda_re[7, 7] = 1      # d_R^r
pi_lambda_re[8, 8] = 1      # d_R^g
pi_lambda_re[9, 9] = 1      # d_R^b

# pi(lambda=i, q=0, m=0): imaginary lambda
pi_lambda_im = np.zeros((16, 16), dtype=complex)
pi_lambda_im[0, 0] = 1j     # nu_R -> i*lambda = i
pi_lambda_im[1, 1] = 1j     # u_R^r
pi_lambda_im[2, 2] = 1j     # u_R^g
pi_lambda_im[3, 3] = 1j     # u_R^b
# conj(i*lambda) = -i on e_R and d_R
pi_lambda_im[4, 4] = -1j    # e_R
pi_lambda_im[7, 7] = -1j    # d_R^r
pi_lambda_im[8, 8] = -1j    # d_R^g
pi_lambda_im[9, 9] = -1j    # d_R^b

# pi(0, q=I, 0): identity quaternion on left-handed
pi_q_I = np.zeros((16, 16), dtype=complex)
pi_q_I[5, 5] = 1     # nu_L
pi_q_I[6, 6] = 1     # e_L
pi_q_I[10, 10] = 1   # u_L^r
pi_q_I[11, 11] = 1   # u_L^g
pi_q_I[12, 12] = 1   # u_L^b
pi_q_I[13, 13] = 1   # d_L^r
pi_q_I[14, 14] = 1   # d_L^g
pi_q_I[15, 15] = 1   # d_L^b

# pi(0, q=i*sigma_1, 0): quaternion basis element
# i*sigma_1 = (0, i; i, 0)
# Acts on (nu_L, e_L) as: nu_L -> i*e_L, e_L -> i*nu_L
pi_q_is1 = np.zeros((16, 16), dtype=complex)
# Leptons
pi_q_is1[5, 6] = 1j    # nu_L -> i*e_L
pi_q_is1[6, 5] = 1j    # e_L -> i*nu_L
# Quarks (each color independently)
for c in range(3):
    pi_q_is1[10+c, 13+c] = 1j  # u_L^c -> i*d_L^c
    pi_q_is1[13+c, 10+c] = 1j  # d_L^c -> i*u_L^c

# pi(0, q=i*sigma_2, 0):
# i*sigma_2 = (0, 1; -1, 0)
pi_q_is2 = np.zeros((16, 16), dtype=complex)
pi_q_is2[5, 6] = 1     # nu_L -> e_L
pi_q_is2[6, 5] = -1    # e_L -> -nu_L
for c in range(3):
    pi_q_is2[10+c, 13+c] = 1   # u_L^c -> d_L^c
    pi_q_is2[13+c, 10+c] = -1  # d_L^c -> -u_L^c

# pi(0, q=i*sigma_3, 0):
# i*sigma_3 = (i, 0; 0, -i)
pi_q_is3 = np.zeros((16, 16), dtype=complex)
pi_q_is3[5, 5] = 1j    # nu_L -> i*nu_L
pi_q_is3[6, 6] = -1j   # e_L -> -i*e_L
for c in range(3):
    pi_q_is3[10+c, 10+c] = 1j   # u_L^c -> i*u_L^c
    pi_q_is3[13+c, 13+c] = -1j  # d_L^c -> -i*d_L^c

# A_F = C + H + M_3(C)
# The C part: pi(lambda) = pi_lambda_re + i*pi_lambda_im (2 real params)
# The H part: pi(q) = alpha*pi_q_I + beta_1*pi_q_is1 + beta_2*pi_q_is2 + beta_3*pi_q_is3 (4 real params)
# The M_3(C) part: acts via J (opposite algebra) -- NOT in the left action!

# So the LEFT action is 6-dimensional (real):
pi_AF_basis = [pi_lambda_re, pi_lambda_im, pi_q_I, pi_q_is1, pi_q_is2, pi_q_is3]

print(f"\npi(A_F) on Psi_+: {len(pi_AF_basis)} real basis elements")
print("  lambda_re, lambda_im, q_I, q_is1, q_is2, q_is3")

# Check: these should form a real subalgebra
# C part: {lambda_re, lambda_im} generates C (commutative)
# H part: {q_I, q_is1, q_is2, q_is3} generates H (noncommutative)
# C and H commute (they act on different indices)

# Verify the algebra
print("\nVerifying algebra structure:")
for i, name_i in enumerate(['lam_re', 'lam_im', 'q_I', 'q_is1', 'q_is2', 'q_is3']):
    for j, name_j in enumerate(['lam_re', 'lam_im', 'q_I', 'q_is1', 'q_is2', 'q_is3']):
        prod = pi_AF_basis[i] @ pi_AF_basis[j]
        # Check if product is in the span
        V = np.column_stack([b.flatten() for b in pi_AF_basis])
        coeffs = np.linalg.lstsq(V, prod.flatten(), rcond=None)[0]
        resid = np.linalg.norm(prod.flatten() - V @ coeffs)
        if resid > 1e-10:
            print(f"  {name_i} * {name_j}: OUTSIDE span (resid={resid:.2e})")

# ===================================================================
# Extend to H_F = C^32 using J
# ===================================================================

print("\n" + "=" * 70)
print("EXTENDING pi(A_F) TO H_F = C^32")
print("=" * 70)

# The action on Psi_- comes from the OPPOSITE algebra via J:
# pi^o(a)(psi_-) = J pi(a*) J^{-1} psi_-
#
# But also, the LEFT action of A_F on Psi_- is determined by
# the particle content of Psi_-.
#
# From Baptista: Psi_- contains the ANTIPARTICLES:
# anti-nu_L, anti-e_L, anti-u_L, anti-d_L, anti-nu_R, anti-e_R, anti-u_R, anti-d_R
#
# The standard Connes LEFT action on antiparticles:
# pi(lambda, q, m) on Psi_- acts trivially (all as identity):
# Actually NO. The LEFT action on Psi_- is:
#   pi(a) on Psi_- = a acts via the STANDARD representation on antiparticles
#
# Hmm, this is where conventions matter. Let me be precise.
#
# In Connes' framework:
# pi(a) acts on ALL of H_F = Psi_+ + Psi_-.
# On Psi_+: as described above (particles).
# On Psi_-: the antiparticle action.
#
# For antiparticles, the action is:
#   anti-nu_R -> conj(lambda) * anti-nu_R  (conjugate of particle action)
#   anti-e_R -> lambda * anti-e_R
#   etc.
#
# Actually, this is determined by J. If J maps Psi_+ to Psi_-,
# then the action on Psi_- is:
#   pi(a)|_{Psi_-} = J pi(a*) J^{-1}|_{Psi_-}
#
# Wait, no. The LEFT action pi(a) acts on ALL of H_F.
# The specific form on Psi_- depends on the particle assignments.
#
# In Connes' SM, the Hilbert space for one generation is:
# H_F = H_R^+ + H_L^+ + H_R^- + H_L^-
# where + = particles, - = antiparticles, R/L = chirality.
#
# The LEFT action of a = (lambda, q, m) is:
# On H_R^+ (right particles): lambda on leptons
# On H_L^+ (left particles): q on doublets
# On H_R^- (right antiparticles): lambda on (anti-leptons with conjugation)
# On H_L^- (left antiparticles): q on (anti-doublets with conjugation)
#
# The M_3(C) factor acts via the OPPOSITE algebra (right action through J).
#
# To avoid getting confused, let me just directly compute what
# J does to pi(A_F):
#
# J pi(a) J^{-1} should be the OPPOSITE algebra action.
# For Connes' axioms: [pi(a), J pi(b) J^{-1}] = 0 (order-zero condition).

# Let me construct pi(A_F) on all of C^32.
# I'll just extend the Psi_+ action to Psi_- using the standard rule:
# On Psi_-: the SAME algebra acts, but with conjugated representation.

# For simplicity, let me directly check: is the image of pi(A_F) on Psi_+
# compatible with the Baptista gauge action?

# Compute: does pi(A_F) commute with Baptista's u(2)_{L+R} action?
print("\nDoes pi(A_F) commute with u(2)_{L+R} gauge?")
basis_u2 = u2_basis_in_su3()
for b_idx, b_name in enumerate(['lam_re', 'lam_im', 'q_I', 'q_is1', 'q_is2', 'q_is3']):
    pi_b = pi_AF_basis[b_idx]
    max_err = 0
    for v in basis_u2:
        rho_v = LR_action_matrix(v)
        comm = pi_b @ rho_v - rho_v @ pi_b
        max_err = max(max_err, np.max(np.abs(comm)))
    print(f"  [{b_name}, rho(v)] max: {max_err:.2e}")

# If pi(A_F) does NOT commute with the Baptista gauge, then either:
# (a) The particle identification is wrong
# (b) The Baptista gauge is not the commutant of pi(A_F)
# (c) Some convention mismatch

# Also check: does Baptista's gauge action commute with pi(A_F)?
# If the Baptista gauge IS the commutant of pi(A_F), then
# [gauge, pi(A_F)] should be 0.

# But actually, the gauge action in Baptista is L+R on u(2),
# which is the GAUGE SYMMETRY of the SM. The algebra A_F
# is NOT the gauge symmetry -- it's the "internal" coordinate algebra.
# In NCG: gauge symmetry = Inn(A_F) = inner automorphisms of A_F.
# The GAUGE group acts on H_F by U = u J u J^{-1} for u in U(A_F).
# This is DIFFERENT from pi(A_F).

# So the Baptista gauge action (u(2)_{L+R}) should be an inner automorphism
# of pi(A_F), not commuting with it. The COMMUTANT of the Baptista gauge
# gives us pi(A_F) (or something related).

# Actually, I think the correct relationship is:
# The gauge group = U(A_F) = unitaries of A_F
# The gauge action on H_F = pi(u) for u in U(A_F)
# So the gauge generators ARE in pi(A_F).
# The commutant of the gauge group = commutant of pi(A_F) = End_{A_F}(H_F)
# which is the gauge ALGEBRA (the endomorphisms commuting with A_F).

# So Phase 1's computation of End_{U(2)_{L+R}}(Psi_+) should give
# something RELATED TO (but not necessarily equal to) A_F.

# The question is: is the Baptista u(2)_{L+R} action = pi(U(2)) for some
# U(2) subset of A_F?

# In Connes' SM: A_F = C + H + M_3(C)
# U(A_F) = U(1) x SU(2) x U(3) = the unitary elements
# The gauge group (modulo center) = U(1) x SU(2) x SU(3) = SM gauge group
# The gauge generators (in the Lie algebra) = i*C + i*su(2) + i*u(3)

# Baptista's u(2)_{L+R}: the L+R representation of u(2)
# This u(2) embeds as the SU(2)_L x U(1)_Y part of the SM gauge group.
# So pi(u(2)) should map INTO pi(A_F).

# Let me check: are the Baptista gauge generators in the span of pi(A_F)?
print("\n\nAre Baptista gauge generators in span of pi(A_F)?")
V_AF = np.column_stack([b.flatten() for b in pi_AF_basis])

for v_idx, v in enumerate(basis_u2):
    rho_v = LR_action_matrix(v)
    coeffs, resid_arr, _, _ = np.linalg.lstsq(V_AF, rho_v.flatten(), rcond=None)
    resid = np.linalg.norm(rho_v.flatten() - V_AF @ coeffs)
    print(f"  Gauge gen {v_idx}: residual = {resid:.2e}")
    if resid < 1e-6:
        print(f"    Coefficients: {np.round(coeffs, 4)}")
    else:
        print(f"    NOT in span of pi(A_F)!")
        # Check which component is outside
        proj = V_AF @ coeffs
        diff = rho_v.flatten() - proj
        T_diff = diff.reshape(16, 16)
        print(f"    Orthogonal component norm: {np.linalg.norm(diff):.4f}")
        # Where does the orthogonal component act?
        for idx_name, idx_set in [('nu_R', [0]), ('u_R', [1,2,3]), ('e_R', [4]),
                                   ('lep_L', [5,6]), ('d_R', [7,8,9]),
                                   ('u_L', [10,11,12]), ('d_L', [13,14,15])]:
            block = T_diff[np.ix_(idx_set, range(16))]
            block2 = T_diff[np.ix_(range(16), idx_set)]
            norm = np.max(np.abs(block)) + np.max(np.abs(block2))
            if norm > 1e-8:
                print(f"      Acts on {idx_name}: norm={norm:.4f}")

print("\n\nDone.")
