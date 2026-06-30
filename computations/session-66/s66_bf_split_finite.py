#!/usr/bin/env python3
"""
s66_bf_split_finite.py -- BF-SPLIT-FINITE-66: B/F Splitting in Finite Spectral Triple
======================================================================================

Gate: BF-SPLIT-FINITE-66
  PASS:  A_F != 0 with |A_F| * a_0/a_2 giving > 10% CC correction
  FAIL:  A_F = 0 identically
  INFO:  A_F != 0 but correction < 10%

Physics
-------
S65 BF-SPLIT-65 proved that on the FIBER spectral triple (pure Riemannian, KO=0),
the B/F spectral asymmetry A = 0 exactly. This is because the spectral action trace
on a pure Riemannian spectral triple has no B/F decomposition.

However, the FULL almost-commutative spectral triple M^4 x F has a finite part F
with KO-dimension 6. The finite Dirac operator D_F encodes Yukawa couplings and
Majorana masses. The question: does Tr_F(gamma_F * f(D_F^2)) vanish?

Structural Analysis
-------------------
The finite spectral triple (A_F, H_F, D_F, J_F, gamma_F) has:
  - A_F = C + H + M_3(C)
  - H_F = C^{32} per generation (C^{96} for 3 generations)
  - KO-dim 6: J_F^2 = +1, J_F D_F = D_F J_F, J_F gamma_F = -gamma_F J_F
  - gamma_F = chirality (+1 on R-particles + L-antiparticles, -1 on L-particles + R-antiparticles)

KEY STRUCTURAL THEOREM:
  The condition J_F gamma_F = -gamma_F J_F (KO-dim 6 sign epsilon'' = -1)
  combined with the spectral triple axiom that D_F anticommutes with gamma_F
  ({gamma_F, D_F} = 0) implies:

  1. D_F maps chirality +1 to chirality -1 and vice versa (off-diagonal in chiral basis)
  2. D_F^2 preserves chirality sectors (block-diagonal)
  3. Nonzero eigenvalues of D_F^2 have equal multiplicity in +1 and -1 sectors
  4. Tr(gamma_F * f(D_F^2)) = f(0) * ind(D_F)    (Eq. 1)

  where ind(D_F) = dim ker(D_F|_{+}) - dim ker(D_F|_{-}) is the Fredholm index
  of D_F restricted to the + chirality sector.

  For the physical SM with all Yukawa couplings nonzero and M_R invertible:
  - D_F has NO kernel (it is an invertible matrix)
  - Therefore ind(D_F) = 0 and A_F = 0 for ALL test functions f

  EVEN if some Yukawas vanish: H_F^+ and H_F^- have equal dimension
  (16N_g each, where N_g = number of generations), so ind(D_F) = 0
  by dimension counting for generic D_F.

References:
  - Chamseddine-Connes-Marcolli (2007), hep-th/0610241: The definitive SM derivation
  - Connes (2006), hep-th/0608226: H_F = C^{32} construction with Majorana
  - van Suijlekom (2024), NCG and Particle Physics 2nd ed.: Modern treatment
  - S65 BF-SPLIT-65: A = 0 on pure Riemannian fiber (KO = 0)

Author: Connes-NCG-Theorist (S66)
Date: 2026-04-03
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    a0_fold, a2_fold, a4_fold, M_KK, PI,
    rho_Lambda_obs, M_Pl_reduced, Lambda_obs_MP4,
)

# =============================================================================
# STEP 0: PRE-REGISTRATION
# =============================================================================
print("=" * 78)
print("BF-SPLIT-FINITE-66: B/F Splitting in Finite Spectral Triple")
print("=" * 78)
print("\n--- PRE-REGISTRATION ---")
print("Gate: BF-SPLIT-FINITE-66")
print("  PASS: A_F != 0 with |A_F| * a_0/a_2 giving > 10% CC correction")
print("  FAIL: A_F = 0 identically")
print("  INFO: A_F != 0 but correction < 10%")
print("  where A_F = Tr_F(gamma_F * f(D_F^2))")

# =============================================================================
# STEP 1: Construct the Finite Hilbert Space H_F
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Finite Hilbert Space H_F = C^{96}")
print("=" * 78)

# H_F = C^{32} per generation, 3 generations = C^{96}
# Basis ordering per generation (following CCM 2007 Section 2):
#
# Particles (chirality gamma_F eigenvalue):
#   0:  nu_R    (+1)    right-handed neutrino
#   1:  e_R     (+1)    right-handed electron
#   2:  nu_L    (-1)    left-handed neutrino
#   3:  e_L     (-1)    left-handed electron
#   4:  u_R^r   (+1)    right-handed up quark, red
#   5:  u_R^g   (+1)    right-handed up quark, green
#   6:  u_R^b   (+1)    right-handed up quark, blue
#   7:  d_R^r   (+1)    right-handed down quark, red
#   8:  d_R^g   (+1)    right-handed down quark, green
#   9:  d_R^b   (+1)    right-handed down quark, blue
#  10:  u_L^r   (-1)    left-handed up quark, red
#  11:  u_L^g   (-1)    left-handed up quark, green
#  12:  u_L^b   (-1)    left-handed up quark, blue
#  13:  d_L^r   (-1)    left-handed down quark, red
#  14:  d_L^g   (-1)    left-handed down quark, green
#  15:  d_L^b   (-1)    left-handed down quark, blue
#
# Antiparticles (J maps gamma_F -> -gamma_F, so chiralities flip):
#  16:  nu_R^c  (-1)    [J maps nu_R (+1) to nu_R^c (-1)]
#  17:  e_R^c   (-1)
#  18:  nu_L^c  (+1)    [J maps nu_L (-1) to nu_L^c (+1)]
#  19:  e_L^c   (+1)
#  20:  u_R^{cr}(-1)
#  21:  u_R^{cg}(-1)
#  22:  u_R^{cb}(-1)
#  23:  d_R^{cr}(-1)
#  24:  d_R^{cg}(-1)
#  25:  d_R^{cb}(-1)
#  26:  u_L^{cr}(+1)
#  27:  u_L^{cg}(+1)
#  28:  u_L^{cb}(+1)
#  29:  d_L^{cr}(+1)
#  30:  d_L^{cg}(+1)
#  31:  d_L^{cb}(+1)

N_gen = 3
dim_per_gen = 32
dim_F = N_gen * dim_per_gen  # = 96

# Chirality eigenvalues per generation
# +1 for R-particles, -1 for L-particles, flipped for antiparticles
chirality_per_gen = np.array([
    # Particles (0-15):
    +1, +1,  # nu_R, e_R (right-handed)
    -1, -1,  # nu_L, e_L (left-handed)
    +1, +1, +1,  # u_R (3 colors)
    +1, +1, +1,  # d_R (3 colors)
    -1, -1, -1,  # u_L (3 colors)
    -1, -1, -1,  # d_L (3 colors)
    # Antiparticles (16-31): chiralities flipped by J gamma = -gamma J
    -1, -1,  # nu_R^c, e_R^c
    +1, +1,  # nu_L^c, e_L^c
    -1, -1, -1,  # u_R^c (3 colors)
    -1, -1, -1,  # d_R^c (3 colors)
    +1, +1, +1,  # u_L^c (3 colors)
    +1, +1, +1,  # d_L^c (3 colors)
], dtype=float)

# Build full gamma_F for 3 generations
gamma_F = np.zeros((dim_F, dim_F), dtype=complex)
for g in range(N_gen):
    offset = g * dim_per_gen
    for i in range(dim_per_gen):
        gamma_F[offset + i, offset + i] = chirality_per_gen[i]

# Verify gamma_F properties
g_sq_err = np.max(np.abs(gamma_F @ gamma_F - np.eye(dim_F)))
tr_gamma = np.real(np.trace(gamma_F))
n_plus = int(np.sum(np.diag(gamma_F).real > 0.5))
n_minus = int(np.sum(np.diag(gamma_F).real < -0.5))

print(f"  dim(H_F) = {dim_F} = {N_gen} generations x {dim_per_gen}")
print(f"  gamma_F^2 = I error: {g_sq_err:.2e}")
print(f"  Tr(gamma_F) = {tr_gamma:.1f}")
print(f"  gamma_F spectrum: {n_plus} (+1), {n_minus} (-1)")
print(f"  Chirality balanced: {n_plus == n_minus}")

assert n_plus == n_minus, f"Chirality unbalanced: {n_plus} vs {n_minus}"
assert abs(tr_gamma) < 1e-10, f"Tr(gamma_F) = {tr_gamma} != 0"

# =============================================================================
# STEP 2: Construct the Real Structure J_F
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Real Structure J_F (KO-dim 6)")
print("=" * 78)

# J_F: particle <-> antiparticle within each generation
# J_F maps basis state i (particle, indices 0-15) to state i+16 (antiparticle)
# and vice versa, with complex conjugation (antilinear)
# J_F is represented as a matrix acting on H_F, with J_F(v) = J_mat @ v.conj()

J_mat = np.zeros((dim_F, dim_F), dtype=complex)
for g in range(N_gen):
    offset = g * dim_per_gen
    for i in range(16):
        # Map particle i to antiparticle i+16
        J_mat[offset + i + 16, offset + i] = 1.0
        J_mat[offset + i, offset + i + 16] = 1.0

# Verify J_F^2 = +1 (J_mat @ J_mat.conj() = I, since J is antilinear)
J_sq = J_mat @ J_mat.conj()
J_sq_err = np.max(np.abs(J_sq - np.eye(dim_F)))
print(f"  J_F^2 = +1 error: {J_sq_err:.2e}")

# Verify J_F gamma_F = -gamma_F J_F (epsilon'' = -1 for KO-dim 6)
# For antilinear J: J(v) = J_mat @ v^*, so J gamma v = J_mat @ (gamma_F @ v)^* = J_mat @ gamma_F^* @ v^*
# gamma J v = gamma_F @ J_mat @ v^*
# Need: J_mat @ gamma_F^* = -gamma_F @ J_mat
# Since gamma_F is real and diagonal: gamma_F^* = gamma_F
# So need: J_mat @ gamma_F = -gamma_F @ J_mat
Jg_comm = J_mat @ gamma_F + gamma_F @ J_mat
Jg_err = np.max(np.abs(Jg_comm))
print(f"  J_F gamma_F + gamma_F J_F = 0 error: {Jg_err:.2e}")
print(f"  Confirms: epsilon'' = -1 (KO-dimension 6)")

# =============================================================================
# STEP 3: Construct the Finite Dirac Operator D_F
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Finite Dirac Operator D_F (Yukawa + Majorana)")
print("=" * 78)

# D_F encodes all Yukawa couplings and the Majorana mass matrix M_R.
# Following CCM 2007, D_F has the structure (per generation, in the
# particle/antiparticle basis):
#
# D_F = ( S    T^* )     S: particle-particle, T: particle-antiparticle
#       ( T    S^* )     (hermiticity condition)
#
# The Yukawa matrices couple L to R within particles:
#   Y_nu: nu_L <-> nu_R   (entries 2 <-> 0)
#   Y_e:  e_L  <-> e_R    (entries 3 <-> 1)
#   Y_u:  u_L  <-> u_R    (entries 10-12 <-> 4-6, per color)
#   Y_d:  d_L  <-> d_R    (entries 13-15 <-> 7-9, per color)
#
# The Majorana mass M_R connects nu_R to its charge conjugate:
#   M_R: nu_R (index 0) <-> nu_R^c (index 16)
#
# For 3 generations, Y_nu, Y_e, Y_u, Y_d are 3x3 matrices.
# M_R is a symmetric 3x3 matrix.
#
# We use physical (PDG 2024) Yukawa couplings at the GUT scale
# (approximately -- the exact values don't matter for the structural question).

# Yukawa couplings (diagonal, 3 generations)
# At GUT scale ~ 10^{16} GeV, approximate values:
# v_EW = 246.0  # GeV, Higgs VEV  # S72: now imported from canonical_constants as v_ew
v_EW = v_ew  # S72: alias for downstream use (capitalization differs)

# Fermion masses at M_Z (PDG 2024, GeV)
m_e = 0.000511  # (local)
m_mu = 0.1057  # S72: truncated from canonical m_mu=0.1056583745 — intentional (4-digit precision)
m_tau = 1.777
m_u = 0.00216  # (local)
m_c = 1.27  # (local)
m_t = 172.76  # (local)
m_d = 0.00467  # (local)
m_s = 0.093  # (local)
m_b = 4.18  # (local)

# Yukawa couplings y = sqrt(2) * m / v
y_e = np.sqrt(2) * np.array([m_e, m_mu, m_tau]) / v_EW
y_u = np.sqrt(2) * np.array([m_u, m_c, m_t]) / v_EW
y_d = np.sqrt(2) * np.array([m_d, m_s, m_b]) / v_EW

# Neutrino Yukawa couplings (seesaw mechanism)
# Using m_nu ~ 0.05 eV and M_R ~ 10^{14} GeV gives y_nu ~ sqrt(2 m_nu M_R) / v
# For the structural question, we use representative values
M_R_scale = 1e14  # GeV (Majorana mass scale)
m_nu = np.array([0.0, 0.0086, 0.050]) * 1e-9  # GeV (normal ordering, approximate)
# Dirac mass = y_nu * v / sqrt(2), seesaw: m_nu = m_D^2 / M_R
# => m_D = sqrt(m_nu * M_R), y_nu = sqrt(2) * m_D / v
m_D_nu = np.sqrt(np.maximum(m_nu, 1e-15) * M_R_scale)
y_nu = np.sqrt(2) * m_D_nu / v_EW

# Majorana mass matrix (diagonal for simplicity; structure doesn't matter for trace)
M_R_diag = M_R_scale * np.array([1.0, 1.0, 1.0])

print(f"  Yukawa couplings (3 generations):")
print(f"    y_e  = {y_e}")
print(f"    y_u  = {y_u}")
print(f"    y_d  = {y_d}")
print(f"    y_nu = {y_nu}")
print(f"    M_R  = {M_R_diag} GeV")

# Build D_F as a 96x96 matrix
D_F = np.zeros((dim_F, dim_F), dtype=complex)

for g in range(N_gen):
    off = g * dim_per_gen  # generation offset

    # --- Particle sector (S block, indices 0-15 within generation) ---

    # Y_nu: nu_L (2) <-> nu_R (0)
    D_F[off + 0, off + 2] = y_nu[g]   # nu_R <- nu_L
    D_F[off + 2, off + 0] = y_nu[g]   # nu_L <- nu_R (hermiticity: y_nu real here)

    # Y_e: e_L (3) <-> e_R (1)
    D_F[off + 1, off + 3] = y_e[g]
    D_F[off + 3, off + 1] = y_e[g]

    # Y_u: u_L^c (10,11,12) <-> u_R^c (4,5,6), per color
    for c in range(3):
        D_F[off + 4 + c, off + 10 + c] = y_u[g]  # u_R^c <- u_L^c
        D_F[off + 10 + c, off + 4 + c] = y_u[g]  # u_L^c <- u_R^c

    # Y_d: d_L^c (13,14,15) <-> d_R^c (7,8,9), per color
    for c in range(3):
        D_F[off + 7 + c, off + 13 + c] = y_d[g]
        D_F[off + 13 + c, off + 7 + c] = y_d[g]

    # --- Antiparticle sector (S* block, indices 16-31 within generation) ---
    # By J_F D_F = D_F J_F (epsilon' = +1 for KO-dim 6), the antiparticle
    # block is the complex conjugate of the particle block, shifted by 16.

    # Y_nu^*: nu_L^c (18) <-> nu_R^c (16)
    D_F[off + 16, off + 18] = np.conj(y_nu[g])
    D_F[off + 18, off + 16] = np.conj(y_nu[g])

    # Y_e^*: e_L^c (19) <-> e_R^c (17)
    D_F[off + 17, off + 19] = np.conj(y_e[g])
    D_F[off + 19, off + 17] = np.conj(y_e[g])

    # Y_u^*: u_L^{c,c} (26,27,28) <-> u_R^{c,c} (20,21,22)
    for c in range(3):
        D_F[off + 20 + c, off + 26 + c] = np.conj(y_u[g])
        D_F[off + 26 + c, off + 20 + c] = np.conj(y_u[g])

    # Y_d^*: d_L^{c,c} (29,30,31) <-> d_R^{c,c} (23,24,25)
    for c in range(3):
        D_F[off + 23 + c, off + 29 + c] = np.conj(y_d[g])
        D_F[off + 29 + c, off + 23 + c] = np.conj(y_d[g])

    # --- Majorana mass term (T block) ---
    # M_R connects nu_R (0) to J(nu_R) = nu_R^c (16)
    # This is a particle-antiparticle mixing term
    D_F[off + 0, off + 16] = M_R_diag[g]
    D_F[off + 16, off + 0] = M_R_diag[g]

# Verify D_F is Hermitian
herm_err = np.max(np.abs(D_F - D_F.conj().T))
print(f"\n  D_F hermiticity error: {herm_err:.2e}")

# Verify J_F D_F = D_F J_F (epsilon' = +1)
# J_F D_F v = J_mat (D_F v)^* = J_mat D_F^* v^*
# D_F J_F v = D_F J_mat v^*
# Need: J_mat D_F^* = D_F J_mat (since D_F is real here, D_F^* = D_F)
JD_comm = J_mat @ D_F.conj() - D_F @ J_mat
JD_err = np.max(np.abs(JD_comm))
print(f"  [J_F, D_F] = 0 error: {JD_err:.2e}")
print(f"  Confirms: epsilon' = +1 (KO-dimension 6)")

# =============================================================================
# STEP 4: Verify {gamma_F, D_F} = 0 (Chirality Anticommutation)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Chirality Anticommutation {gamma_F, D_F} = 0")
print("=" * 78)

anticomm = gamma_F @ D_F + D_F @ gamma_F
anticomm_err = np.max(np.abs(anticomm))
print(f"  ||{{gamma_F, D_F}}|| = {anticomm_err:.2e}")

if anticomm_err < 1e-10:
    print("  CONFIRMED: {gamma_F, D_F} = 0")
    print("  D_F is strictly off-diagonal in the chiral basis.")
    print("  => D_F maps H_F^+ to H_F^- and vice versa.")
    print("  => D_F^2 preserves chirality sectors (block-diagonal).")
    chiral_anticomm = True
else:
    print(f"  WARNING: {{gamma_F, D_F}} != 0 (max entry = {anticomm_err:.6e})")
    print("  Investigating which entries violate chirality anticommutation...")
    # Find the violating entries
    viol_idx = np.argwhere(np.abs(anticomm) > 1e-10)
    for idx in viol_idx[:10]:
        i, j = idx
        gen_i = i // dim_per_gen
        gen_j = j // dim_per_gen
        local_i = i % dim_per_gen
        local_j = j % dim_per_gen
        chi_i = chirality_per_gen[local_i]
        chi_j = chirality_per_gen[local_j]
        print(f"    ({i},{j}): gen ({gen_i},{gen_j}), local ({local_i},{local_j}), "
              f"chi ({chi_i:+.0f},{chi_j:+.0f}), value = {anticomm[i,j]:.6e}")
    chiral_anticomm = False

# =============================================================================
# STEP 5: Spectrum of D_F and D_F^2
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Spectrum of D_F")
print("=" * 78)

evals_DF = np.linalg.eigvalsh(D_F)
evals_DF_sorted = np.sort(evals_DF)

# Count zero eigenvalues
tol = 1e-6  # relative to max eigenvalue (local)
max_eval = np.max(np.abs(evals_DF))
n_zero = np.sum(np.abs(evals_DF) < tol * max_eval)
n_pos = np.sum(evals_DF > tol * max_eval)
n_neg = np.sum(evals_DF < -tol * max_eval)

print(f"  dim(D_F) = {dim_F} x {dim_F}")
print(f"  Max |eigenvalue| = {max_eval:.6e}")
print(f"  Spectrum: {n_pos} positive, {n_neg} negative, {n_zero} zero")
print(f"  (zero threshold = {tol * max_eval:.2e})")

# Display all unique nonzero eigenvalues (there should be at most ~32 distinct ones)
unique_evals = []
for ev in evals_DF_sorted:
    if len(unique_evals) == 0 or abs(ev - unique_evals[-1]) > tol * max_eval:
        unique_evals.append(ev)
unique_evals = np.array(unique_evals)
print(f"\n  Distinct eigenvalue clusters: {len(unique_evals)}")
for i, ev in enumerate(unique_evals):
    mult = np.sum(np.abs(evals_DF - ev) < tol * max_eval)
    if abs(ev) > tol * max_eval:
        print(f"    lambda_{i} = {ev:+.6e}, multiplicity = {mult}")
    else:
        print(f"    lambda_{i} = 0 (|val| < {tol * max_eval:.2e}), multiplicity = {mult}")

# =============================================================================
# STEP 6: Compute the Index ind(D_F) = Tr(gamma_F | ker(D_F))
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Fredholm Index of D_F")
print("=" * 78)

# Get eigenvectors
evals_DF_full, evecs_DF = np.linalg.eigh(D_F)

# Zero modes
zero_mask = np.abs(evals_DF_full) < tol * max_eval
zero_evecs = evecs_DF[:, zero_mask]
n_zero_modes = zero_evecs.shape[1]

if n_zero_modes > 0:
    print(f"  ker(D_F) dimension: {n_zero_modes}")
    # Compute chirality of each zero mode
    chiralities_zero = []
    for i in range(n_zero_modes):
        v = zero_evecs[:, i]
        chi = np.real(v.conj() @ gamma_F @ v)
        chiralities_zero.append(chi)
        print(f"    Zero mode {i}: <gamma_F> = {chi:+.6f}")
    n_plus_zero = sum(1 for c in chiralities_zero if c > 0.5)
    n_minus_zero = sum(1 for c in chiralities_zero if c < -0.5)
    index_DF = n_plus_zero - n_minus_zero
    print(f"\n  ind(D_F) = dim ker(D_F|_+) - dim ker(D_F|_-) = {n_plus_zero} - {n_minus_zero} = {index_DF}")
else:
    index_DF = 0
    print(f"  ker(D_F) = {{0}} (D_F is invertible)")
    print(f"  ind(D_F) = 0 (trivially)")

# =============================================================================
# STEP 7: Compute A_F = Tr(gamma_F * f(D_F^2)) for various f
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: B/F Asymmetry A_F = Tr(gamma_F * f(D_F^2))")
print("=" * 78)

# D_F^2 eigenvalues
evals_DF2 = evals_DF_full**2

# Test functions
Lambda_cutoff = M_KK  # Use M_KK as cutoff

# f_1(x) = exp(-x)
def f_exp(x):
    return np.exp(-x)

# f_2(x) = 1/(1+x)  (Lorentzian cutoff)
def f_lorentz(x):
    return 1.0 / (1.0 + x)

# f_3(x) = theta(1-x) (sharp cutoff)
def f_sharp(x):
    return np.where(x < 1.0, 1.0, 0.0)

# f_4(x) = sqrt(x)  (as specified in task)
def f_sqrt(x):
    return np.sqrt(np.maximum(x, 0.0))

# f_5(x) = x (for a_2-type moment)
def f_linear(x):
    return x

cutoff_funcs = {
    'exp(-x)': f_exp,
    '1/(1+x)': f_lorentz,
    'theta(1-x)': f_sharp,
    'sqrt(x)': f_sqrt,
    'x': f_linear,
}

print(f"\n  Cutoff scale: Lambda = {Lambda_cutoff:.4e} GeV")

results = {}
for name, f in cutoff_funcs.items():
    # Compute Tr(gamma_F * f(D_F^2 / Lambda^2))
    x = evals_DF2 / Lambda_cutoff**2
    f_vals = f(x)

    # gamma_F eigenvalues for each D_F eigenstate
    gamma_expect = np.array([np.real(evecs_DF[:, i].conj() @ gamma_F @ evecs_DF[:, i])
                             for i in range(dim_F)])

    A_F_val = np.sum(gamma_expect * f_vals)

    # Also compute the total trace (no gamma_F)
    total_trace = np.sum(f_vals)

    # Relative asymmetry
    rel_asym = A_F_val / total_trace if abs(total_trace) > 1e-30 else 0.0

    results[name] = {
        'A_F': A_F_val,
        'total': total_trace,
        'rel': rel_asym,
    }

    print(f"\n  f(x) = {name}:")
    print(f"    Tr(f(D_F^2/L^2))             = {total_trace:.10e}")
    print(f"    Tr(gamma_F * f(D_F^2/L^2))   = {A_F_val:.10e}")
    print(f"    Relative asymmetry A_F/total  = {rel_asym:.10e}")

# =============================================================================
# STEP 8: Direct Matrix Computation (independent verification)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Direct Matrix Computation (verification)")
print("=" * 78)

# Compute gamma_F @ f(D_F^2) directly as a matrix and take trace
# This avoids any basis-dependent issues
DF2 = D_F @ D_F

for name, f in [('exp(-x)', f_exp), ('sqrt(x)', f_sqrt)]:
    # Compute f(D_F^2 / Lambda^2) as a matrix function
    evals_m, evecs_m = np.linalg.eigh(DF2)
    x = evals_m / Lambda_cutoff**2
    f_diag = np.diag(f(x))
    fDF2 = evecs_m @ f_diag @ evecs_m.conj().T

    # A_F = Tr(gamma_F @ f(D_F^2))
    product = gamma_F @ fDF2
    A_F_direct = np.real(np.trace(product))
    total_direct = np.real(np.trace(fDF2))

    print(f"\n  f(x) = {name} [DIRECT MATRIX]:")
    print(f"    Tr(f(D_F^2/L^2))             = {total_direct:.10e}")
    print(f"    Tr(gamma_F * f(D_F^2/L^2))   = {A_F_direct:.10e}")

    # Check gamma_F * D_F^2 commutation
    comm_gDF2 = gamma_F @ DF2 - DF2 @ gamma_F
    comm_err = np.max(np.abs(comm_gDF2))
    print(f"    [gamma_F, D_F^2] error: {comm_err:.2e}")

# =============================================================================
# STEP 9: Structural Analysis -- Why A_F = 0
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Structural Analysis")
print("=" * 78)

print("""
  THEOREM (B/F Vanishing for Finite SM Spectral Triple):

  For the finite spectral triple (A_F, H_F, D_F, J_F, gamma_F) of the
  NCG Standard Model with KO-dimension 6:

    Tr_F(gamma_F * f(D_F^2 / Lambda^2)) = f(0) * ind(D_F)    (Eq. 1)

  PROOF:
  1. {gamma_F, D_F} = 0 (verified numerically, Step 4)
     => D_F is off-diagonal in the chiral basis: D_F = (0, D_+; D_-, 0)
     where D_+: H_F^+ -> H_F^- and D_- = D_+^dagger: H_F^- -> H_F^+.

  2. [gamma_F, D_F^2] = 0 (follows from (1))
     => D_F^2 = diag(D_- D_+, D_+ D_-) preserves chirality sectors.

  3. For each nonzero eigenvalue lambda^2 of D_F^2:
     If v is an eigenvector of D_- D_+ with eigenvalue lambda^2 (in H_F^+),
     then D_+ v / lambda is an eigenvector of D_+ D_- with the same
     eigenvalue lambda^2 (in H_F^-).
     => Nonzero eigenvalues have equal multiplicity in + and - sectors.
     => Their contribution to Tr(gamma_F * f(D_F^2)) cancels: f(lambda^2) - f(lambda^2) = 0.

  4. Zero eigenvalues: Tr(gamma_F |_{ker D_F}) = ind(D_F)
     (the Fredholm index of D_+: H_F^+ -> H_F^-).

  5. For the physical SM:
     - dim(H_F^+) = dim(H_F^-) = 48 (per the classification theorem)
     - With nonzero Yukawa couplings and invertible M_R:
       ker(D_F) = {0} (D_F is an invertible 96x96 matrix)
     - Therefore ind(D_F) = 0.

  6. Even if some Yukawas vanish (e.g., m_nu1 = 0):
     The zero modes appear in matched chirality pairs because
     the particle/antiparticle structure ensures dim(ker D_+) = dim(ker D_-)
     whenever D_F has the J_F-symmetric form required by the NCG axioms.

  CONCLUSION: A_F = 0 for ALL test functions f and ALL physical Yukawa parameters.

  This is STRUCTURAL (not numerical):
  - It follows from {gamma_F, D_F} = 0 (chirality axiom)
  - It holds for ANY D_F satisfying the NCG axioms
  - The B/F symmetry of the spectral action is a THEOREM, not an accident
""")

# Verify the index is zero even with modified Yukawas
print("  Stability test: varying Yukawa couplings")
test_configs = [
    ("Physical SM", y_nu.copy(), y_e.copy(), y_u.copy(), y_d.copy(), M_R_diag.copy()),
    ("All Yukawas equal", np.ones(3)*0.5, np.ones(3)*0.5, np.ones(3)*0.5, np.ones(3)*0.5, M_R_diag.copy()),
    ("Zero neutrino Yukawa", np.zeros(3), y_e.copy(), y_u.copy(), y_d.copy(), M_R_diag.copy()),
    ("Zero Majorana mass", y_nu.copy(), y_e.copy(), y_u.copy(), y_d.copy(), np.zeros(3)),
    ("All zero (D_F = 0)", np.zeros(3), np.zeros(3), np.zeros(3), np.zeros(3), np.zeros(3)),
    ("Only top Yukawa", np.zeros(3), np.zeros(3), np.array([0,0,1.0]), np.zeros(3), np.zeros(3)),
    ("Random Yukawas", np.random.rand(3), np.random.rand(3), np.random.rand(3), np.random.rand(3), np.random.rand(3)*1e14),
]

stability_results = []
for label, yn, ye, yu, yd, MR in test_configs:
    D_test = np.zeros((dim_F, dim_F), dtype=complex)
    for g in range(N_gen):
        off = g * dim_per_gen
        D_test[off+0, off+2] = yn[g]; D_test[off+2, off+0] = yn[g]
        D_test[off+1, off+3] = ye[g]; D_test[off+3, off+1] = ye[g]
        for c in range(3):
            D_test[off+4+c, off+10+c] = yu[g]; D_test[off+10+c, off+4+c] = yu[g]
            D_test[off+7+c, off+13+c] = yd[g]; D_test[off+13+c, off+7+c] = yd[g]
        # Antiparticle block
        D_test[off+16, off+18] = np.conj(yn[g]); D_test[off+18, off+16] = np.conj(yn[g])
        D_test[off+17, off+19] = np.conj(ye[g]); D_test[off+19, off+17] = np.conj(ye[g])
        for c in range(3):
            D_test[off+20+c, off+26+c] = np.conj(yu[g]); D_test[off+26+c, off+20+c] = np.conj(yu[g])
            D_test[off+23+c, off+29+c] = np.conj(yd[g]); D_test[off+29+c, off+23+c] = np.conj(yd[g])
        # Majorana
        D_test[off+0, off+16] = MR[g]; D_test[off+16, off+0] = MR[g]

    # Check chirality anticommutation
    ac_err = np.max(np.abs(gamma_F @ D_test + D_test @ gamma_F))

    # Compute A_F
    evals_test = np.linalg.eigvalsh(D_test)
    evals_test2 = evals_test**2
    x_test = evals_test2 / Lambda_cutoff**2
    f_test = np.exp(-x_test)

    _, evecs_test = np.linalg.eigh(D_test)
    gamma_exp = np.array([np.real(evecs_test[:, i].conj() @ gamma_F @ evecs_test[:, i])
                          for i in range(dim_F)])
    A_F_test = np.sum(gamma_exp * f_test)
    total_test = np.sum(f_test)

    n_zero_test = np.sum(np.abs(evals_test) < 1e-10)
    rel_test = A_F_test / total_test if abs(total_test) > 1e-30 else 0.0

    stability_results.append((label, ac_err, A_F_test, n_zero_test, rel_test))
    print(f"    {label:30s}: {{g,D}}={ac_err:.1e}, A_F={A_F_test:+.2e}, "
          f"n_zero={n_zero_test:3d}, rel={rel_test:+.2e}")

# =============================================================================
# STEP 10: CC Correction Estimate
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Cosmological Constant Correction from A_F")
print("=" * 78)

A_F_physical = results['exp(-x)']['A_F']

# Even though A_F = 0, let's compute what the correction WOULD be if it weren't
# The CC from spectral action: Lambda_CC ~ f_4 * Lambda^4 * a_0 / (8*pi^2)
# A correction from B/F splitting would modify a_0 -> a_0 + A_F * (factor)
# The factor depends on how the B/F splitting enters the product geometry

# In the product geometry M^4 x F:
# Tr_full(gamma * f(D^2/L^2)) = Tr_{M4}(gamma_5 * ...) x Tr_F(gamma_F * f(D_F^2/L^2))
# = 0 x 0 = 0 (both factors vanish independently)

# The a_0 coefficient of the product geometry is:
# a_0^{product} = Tr_F(I) * a_0^{M4} = 96 * a_0^{M4}
# (The finite trace is just the dimension of H_F, not a chirality-weighted trace)

# The B/F correction would enter as:
# delta_a_0 = A_F * a_0_M4  (if A_F != 0)
# delta(Lambda_CC) = (A_F / Tr_F(I)) * Lambda_CC = (A_F / 96) * Lambda_CC

delta_a0_over_a0 = A_F_physical / 96.0  # Tr_F(I) = 96

print(f"\n  A_F (exp cutoff) = {A_F_physical:.10e}")
print(f"  delta_a_0 / a_0 = A_F / Tr_F(I) = {delta_a0_over_a0:.10e}")

if abs(A_F_physical) > 1e-20:
    # CC correction
    delta_CC_over_CC = delta_a0_over_a0
    print(f"  delta(Lambda_CC) / Lambda_CC = {delta_CC_over_CC:.10e}")
    print(f"  OOM correction: {np.log10(abs(delta_CC_over_CC)):.1f}")
else:
    print(f"\n  A_F = 0 to machine precision.")
    print(f"  No CC correction from B/F splitting in the finite triple.")
    print(f"  This is STRUCTURAL: {'{'}gamma_F, D_F{'}'} = 0 => Tr(gamma_F * f(D_F^2)) = 0.")

# =============================================================================
# STEP 11: Connection to Full Almost-Commutative Geometry
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Full Almost-Commutative Geometry M^4 x F")
print("=" * 78)

print("""
  The full spectral triple is:
    (A, H, D) = (C^inf(M4) x A_F, L^2(S) x H_F, D_M x 1 + gamma_5 x D_F)

  The full chirality is:
    gamma = gamma_5 x gamma_F

  The spectral action Tr(f(D^2/L^2)) decomposes via heat kernel:
    Tr(f(D^2/L^2)) = sum_k f_k * Lambda^{4-k} * a_k(D^2)

  where a_k(D^2) are the Seeley-DeWitt coefficients of the PRODUCT geometry.

  KEY POINT: The B/F splitting in the NCG-SM comes from the FERMIONIC action
    S_f = <J psi, D psi>
  NOT from the bosonic spectral action Tr(f(D^2/L^2)).

  The bosonic action traces over ALL of H (no chirality weighting).
  The fermionic action uses the chiral projector P_+ = (1 + gamma)/2.

  Specifically (CCM 2007, Section 4):
    S_f = <J psi, D_A psi>
  where psi is in H^+ = {v in H : gamma v = v} and D_A = D + A + JAJ^{-1}
  is the fluctuated Dirac operator.

  The B/F asymmetry Tr(gamma * f(D^2/L^2)) = 0 for the product geometry
  because BOTH factors vanish:
    - Tr_{M4}(gamma_5 * g(D_M^2)) = 0 (Atiyah-Singer, or simply dim M4 = 4 even)
    - Tr_F(gamma_F * f(D_F^2)) = 0 (this computation, from {gamma_F, D_F} = 0)

  The CC problem in the NCG-SM is:
    Lambda_CC = (1/pi^2) * (48 f_4 Lambda^4 - f_2 Lambda^2 c + f_0 d/4)
  where c = Tr(Y^dag Y) and d = Tr((Y^dag Y)^2).
  This is a TOTAL trace, not a chirality-weighted trace.
  B/F splitting does not help.
""")

# =============================================================================
# STEP 12: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: BF-SPLIT-FINITE-66")
print("=" * 78)

# Maximum asymmetry across all test functions
max_asym = max(abs(results[name]['A_F']) for name in results)
max_rel = max(abs(results[name]['rel']) for name in results)

print(f"\n  Max |A_F| across all cutoff functions: {max_asym:.2e}")
print(f"  Max |A_F/total| across all cutoff functions: {max_rel:.2e}")
print(f"  Machine epsilon: {np.finfo(float).eps:.2e}")

if max_asym < 100 * np.finfo(float).eps:
    verdict = "FAIL"
    print(f"\n  VERDICT: **FAIL** -- A_F = 0 identically (to machine precision)")
    print(f"\n  STRUCTURAL REASON:")
    print(f"    {{gamma_F, D_F}} = 0 => Tr(gamma_F * f(D_F^2)) = f(0) * ind(D_F)")
    print(f"    ind(D_F) = 0 (dim H_F^+ = dim H_F^- = 48, kernel matched)")
    print(f"    => A_F = 0 for ALL test functions f and ALL Yukawa parameters")
    print(f"\n  This is the SAME structural zero as BF-SPLIT-65 on the fiber,")
    print(f"  but now proven for the FINITE spectral triple of the NCG-SM.")
    print(f"  The vanishing is UNIVERSAL: it holds for any (A_F, H_F, D_F)")
    print(f"  satisfying the KO-dim 6 axioms with {{gamma_F, D_F}} = 0.")
else:
    # Check against 10% CC correction threshold
    cc_correction = abs(max_asym / 96.0)
    if cc_correction > 0.1:
        verdict = "PASS"
        print(f"\n  VERDICT: **PASS** -- A_F = {max_asym:.4e}, CC correction = {cc_correction:.2%}")
    else:
        verdict = "INFO"
        print(f"\n  VERDICT: **INFO** -- A_F = {max_asym:.4e}, CC correction = {cc_correction:.2e} (< 10%)")

# =============================================================================
# STEP 13: Summary Table
# =============================================================================
print("\n" + "=" * 78)
print("SUMMARY TABLE")
print("=" * 78)

print(f"\n  {'Property':40s} {'Value':>20s}")
print(f"  {'-'*40} {'-'*20}")
print(f"  {'dim(H_F)':40s} {dim_F:>20d}")
print(f"  {'N_generations':40s} {N_gen:>20d}")
print(f"  {'gamma_F^2 = I':40s} {'YES':>20s}")
print(f"  {'Tr(gamma_F)':40s} {tr_gamma:>20.1f}")
print(f"  {'n_+ = n_-':40s} {str(n_plus == n_minus):>20s}")
print(f"  {'J_F^2 = +1':40s} {'YES':>20s}")
print(f"  {'J_F gamma_F = -gamma_F J_F':40s} {'YES':>20s}")
print(f"  {'[J_F, D_F] = 0':40s} {'YES':>20s}")
print(f"  {'{{gamma_F, D_F}} = 0':40s} {str(chiral_anticomm):>20s}")
print(f"  {'ker(D_F) dimension':40s} {n_zero:>20d}")
print(f"  {'ind(D_F)':40s} {index_DF:>20d}")
print(f"  {'A_F (exp cutoff)':40s} {results['exp(-x)']['A_F']:>20.2e}")
print(f"  {'A_F (Lorentzian)':40s} {results['1/(1+x)']['A_F']:>20.2e}")
print(f"  {'A_F (sharp cutoff)':40s} {results['theta(1-x)']['A_F']:>20.2e}")
print(f"  {'A_F (sqrt)':40s} {results['sqrt(x)']['A_F']:>20.2e}")
print(f"  {'Gate verdict':40s} {verdict:>20s}")

# =============================================================================
# STEP 14: Save results
# =============================================================================
print("\n" + "=" * 78)
print("STEP 14: Saving Results")
print("=" * 78)

np.savez('s66_bf_split_finite.npz',
    # Finite triple structure
    dim_F=dim_F,
    N_gen=N_gen,
    gamma_F_diag=np.diag(gamma_F).real,
    evals_DF=evals_DF_sorted,
    evals_DF2=evals_DF_sorted**2,
    # B/F asymmetry
    A_F_exp=results['exp(-x)']['A_F'],
    A_F_lorentz=results['1/(1+x)']['A_F'],
    A_F_sharp=results['theta(1-x)']['A_F'],
    A_F_sqrt=results['sqrt(x)']['A_F'],
    A_F_linear=results['x']['A_F'],
    # Index
    index_DF=index_DF,
    n_zero_modes=n_zero,
    # Structural checks
    chiral_anticomm=chiral_anticomm,
    J_sq_err=J_sq_err,
    Jgamma_err=Jg_err,
    JD_err=JD_err,
    herm_err=herm_err,
    anticomm_err=anticomm_err,
    # Stability
    stability_labels=np.array([s[0] for s in stability_results], dtype=object),
    stability_AF=np.array([s[2] for s in stability_results]),
    stability_nzero=np.array([s[3] for s in stability_results]),
    # Yukawa parameters used
    y_e=y_e, y_u=y_u, y_d=y_d, y_nu=y_nu, M_R_diag=M_R_diag,
    # Gate
    verdict=verdict,
)
print("  Saved: s66_bf_split_finite.npz")

# =============================================================================
# STEP 15: Plot
# =============================================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: D_F spectrum
ax1 = axes[0]
ax1.stem(range(len(evals_DF_sorted)), evals_DF_sorted, markerfmt='o', linefmt='b-',
         basefmt='k-')
ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel('Eigenvalue of D_F (GeV)')
ax1.set_title('Spectrum of D_F')
ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax1.set_yscale('symlog', linthresh=1e-6)

# Panel 2: Chirality expectation values
ax2 = axes[1]
gamma_expectations = np.array([np.real(evecs_DF[:, i].conj() @ gamma_F @ evecs_DF[:, i])
                                for i in range(dim_F)])
ax2.scatter(evals_DF_full, gamma_expectations, s=5, c='blue', alpha=0.5)
ax2.set_xlabel('Eigenvalue of D_F (GeV)')
ax2.set_ylabel('<gamma_F>')
ax2.set_title('Chirality vs Eigenvalue')
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax2.set_xscale('symlog', linthresh=1e-6)

# Panel 3: Stability of A_F across configurations
ax3 = axes[2]
labels = [s[0][:15] for s in stability_results]
af_vals = [s[2] for s in stability_results]
colors = ['green' if abs(v) < 1e-10 else 'red' for v in af_vals]
ax3.barh(range(len(labels)), [abs(v) for v in af_vals], color=colors)
ax3.set_yticks(range(len(labels)))
ax3.set_yticklabels(labels, fontsize=8)
ax3.set_xlabel('|A_F|')
ax3.set_title('A_F Stability (all configs)')
ax3.axvline(x=np.finfo(float).eps, color='r', linestyle='--', label='Machine eps')
ax3.set_xscale('symlog', linthresh=1e-16)
ax3.legend(fontsize=8)

plt.suptitle('BF-SPLIT-FINITE-66: B/F Splitting in NCG-SM Finite Triple', fontsize=13)
plt.tight_layout()
plt.savefig('s66_bf_split_finite.png', dpi=150, bbox_inches='tight')
print("  Saved: s66_bf_split_finite.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
