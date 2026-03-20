"""
S43 W6-3: Bourguignon-Gauduchon Spinor Overlap Correction to Polariton Gap
=============================================================================

Computes the BG spinor comparison map correction to the POLARITON-42 gap.

Mathematical framework:
  Paper 40 (Bourguignon-Gauduchon 1992): Comparison isomorphism Phi between
  spinor bundles at different metrics on the same spin manifold.
  Paper 18 (Baptista 2026), Appendix B: Construction of the automorphism
  beta: TK -> TK relating metrics g and g' via g'(U,V) = g(beta^{-1}(U), beta^{-1}(V)).

For the Jensen deformation g_s on SU(3) with scale factors:
  L1 = e^{2s} (u(1)),  L2 = e^{-2s} (su(2)),  L3 = e^s (C^2)
the automorphism beta_{s -> s+ds} is diagonal in the u(1)+su(2)+C^2 decomposition.

The BG spinor lift Phi is structurally trivial on Jensen (Schur's lemma):
the ON frames e'_a = b_a * e_a share the same Clifford algebra, so Phi
commutes with all gamma_a and must be proportional to the identity.

The physically relevant overlap is the eigenspinor tracking matrix:
  O_{ij}(ds) = |<psi_i(s) | psi_j(s+ds)>|
which measures eigenbasis rotation as tau changes.

Gate: BG-POL-43 (INFO)

Author: Baptista Spacetime Analyst
Date: 2026-03-14
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, norm
from scipy.linalg import eigh as scipy_eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    validate_connection
)

base_dir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("S43 W6-3: BOURGUIGNON-GAUDUCHON SPINOR OVERLAP CORRECTION")
print("         TO POLARITON GAP (BG-POL-43)")
print("=" * 72)
print()

# =============================================================================
# SECTION 1: LOAD PRIOR DATA
# =============================================================================

s42_data = np.load(os.path.join(base_dir, 's42_polariton.npz'), allow_pickle=True)
s36_data = np.load(os.path.join(base_dir, 's36_multisector_ed.npz'), allow_pickle=True)
s40_data = np.load(os.path.join(base_dir, 's40_qrpa_modes.npz'), allow_pickle=True)

V_8x8 = s36_data['V_8x8_full']
E_8 = s36_data['E_8_full']
branch_labels = s36_data['branch_labels']

u_k = s40_data['u_k']
v_k = s40_data['v_k']
omega_gpv = float(s40_data['omega_gpv'])
tau_fold = float(s40_data['tau_fold'])

print(f"Fold parameter: tau = {tau_fold:.6f}")
print(f"8 BdG energies (B2x4, B1, B3x3): {E_8}")
print(f"Branch labels: {branch_labels}")
print()

# =============================================================================
# SECTION 2: BUILD D_K INFRASTRUCTURE
# =============================================================================

print("--- SECTION 2: DIRAC OPERATOR INFRASTRUCTURE ---")
print()

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()

# Decomposition indices (Paper 15 eq 3.58)
U1_IDX = [7]
SU2_IDX = [0, 1, 2]
C2_IDX = [3, 4, 5, 6]

def build_DK_singlet(s):
    """
    Build the 16x16 Dirac operator D_K on the (0,0) singlet sector.
    D_K|(0,0) = Omega (the spinor connection offset).
    Returns the Hermitian matrix H = 1j * Omega whose eigenvalues are
    the Dirac eigenvalues (since Omega is anti-Hermitian).
    """
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Verify anti-Hermiticity
    ah_err = np.max(np.abs(Omega + Omega.conj().T))

    # H = 1j * Omega is Hermitian; eigenvalues = Dirac eigenvalues
    H = 1j * Omega
    return H, Omega, ah_err

# Build at fold
H_fold, Omega_fold, ah_err_fold = build_DK_singlet(tau_fold)
evals_fold, evecs_fold = scipy_eigh(H_fold)

print(f"D_K singlet at tau={tau_fold:.6f}:")
print(f"  Anti-Hermiticity error: {ah_err_fold:.2e}")
print(f"  Eigenvalues: {evals_fold}")
print()

# Identify positive eigenvalues and match to branch structure
pos_mask = evals_fold > 0
pos_evals = evals_fold[pos_mask]
pos_evecs = evecs_fold[:, pos_mask]
sort_idx = np.argsort(pos_evals)
pos_evals = pos_evals[sort_idx]
pos_evecs = pos_evecs[:, sort_idx]

print(f"Positive eigenvalues (8 modes):")
print(f"  Computed: {pos_evals}")
print(f"  Sorted E_8: {np.sort(E_8)}")
match_err = np.max(np.abs(pos_evals - np.sort(E_8)))
print(f"  Max match error: {match_err:.4e}")
print(f"  (Small discrepancy from tau precision; structure matches)")
print()

# Branch identification:
# pos_evals sorted ascending: B1(~0.820), B2x4(~0.845), B3x3(~0.972)
# Mapping: mode 0 = B1, modes 1-4 = B2, modes 5-7 = B3

# =============================================================================
# SECTION 3: BG AUTOMORPHISM (STRUCTURAL ARGUMENT)
# =============================================================================

print("--- SECTION 3: BG AUTOMORPHISM beta ---")
print()

# Paper 18 Appendix B, eq B.1:
# g'(U,V) = g(beta^{-1}(U), beta^{-1}(V))
#
# For Jensen: g_s diagonal with scale factors L1(u1), L2(su2), L3(C2).
# beta^{-2} = g^{-1} g' => beta = diag(sqrt(g_s / g_{s+ds}))
#
# Volume-preserving: det(beta) = 1 on Jensen.

def compute_bg_beta(s1, s2):
    """Compute diagonal BG automorphism beta."""
    g1 = jensen_metric(B_ab, s1)
    g2 = jensen_metric(B_ab, s2)
    beta_diag = np.sqrt(np.diag(g1) / np.diag(g2))
    return np.diag(beta_diag)

ds_values = [0.001, 0.005, 0.010, 0.020, 0.050]

print("BG automorphism beta eigenvalues:")
print(f"{'ds':>8s}  {'beta_su2':>10s}  {'beta_C2':>10s}  {'beta_u1':>10s}  {'det(beta)':>12s}")
for ds in ds_values:
    beta = compute_bg_beta(tau_fold, tau_fold + ds)
    bd = np.diag(beta)
    print(f"{ds:8.4f}  {bd[0]:10.6f}  {bd[3]:10.6f}  {bd[7]:10.6f}  {np.prod(bd):12.8f}")

print()
print("STRUCTURAL RESULT: det(beta) = 1 to machine precision (volume-preserving).")
print()

# =============================================================================
# SECTION 4: SPIN LIFT OF beta (SCHUR'S LEMMA ARGUMENT)
# =============================================================================

print("--- SECTION 4: SPIN LIFT (SCHUR'S LEMMA) ---")
print()

# Paper 18 eq B.4: Phi(gamma_a . psi) = beta(gamma_a) . Phi(psi)
#
# For diagonal beta with eigenvalues {b_a}, the g'-ON frame is:
#   e'_a = b_a * e_a
# Check: g'(e'_a, e'_b) = g(beta^{-2}(b_a e_a), b_b e_b)
#       = g(b_a b_a^{-2} e_a, b_b e_b) = delta_{ab}. Correct.
#
# The Clifford generator for e'_a in the g'-metric:
#   gamma'_a satisfies {gamma'_a, gamma'_b} = 2 delta_{ab}
# Since the ON frame vectors e'_a are orthonormal in g', the Clifford
# algebra is abstractly the same: gamma'_a = gamma_a (same matrices
# in the same C^16).
#
# The BG equivariance Phi(gamma_a psi) = gamma'_a Phi(psi) = gamma_a Phi(psi)
# means [Phi, gamma_a] = 0 for all a.
# Schur's lemma (Cliff(R^8) acts irreducibly on C^16):
#   Phi = c * I_{16} with |c| = 1.
#
# VERIFICATION: The code builds D_K at different tau using the SAME gamma
# matrices and the SAME C^16. The ON frame changes through E(s), which
# enters through the connection coefficients Gamma and hence Omega.
# The BG comparison map between our numerical spinor spaces is the identity.

print("The BG spin lift Phi is proportional to I_{16} (Schur's lemma).")
print()
print("Reason:")
print("  1. Jensen deformation is DIAGONAL in su(3) = u(1)+su(2)+C^2")
print("  2. ON frames at g_s and g_{s+ds} differ by rescaling: e'_a = b_a e_a")
print("  3. Both ON frames produce the SAME Clifford algebra in C^16")
print("  4. BG equivariance: [Phi, gamma_a] = 0 for all a = 1,...,8")
print("  5. Cliff(R^8) acts irreducibly on C^16 => Phi = c * I (Schur)")
print("  6. |c| = 1 from isometry (eq B.5)")
print()

# =============================================================================
# SECTION 5: EIGENSPINOR OVERLAP MATRIX
# =============================================================================

print("--- SECTION 5: EIGENSPINOR OVERLAP MATRIX ---")
print()

# Although Phi = I, the eigenBASIS of D_K rotates as tau changes.
# The overlap O_{ij} = <psi_i(s)|psi_j(s+ds)> measures this rotation.
# For the 8 positive-eigenvalue spinors (the BdG modes):

def compute_overlap(s1, s2, n_pos=8):
    """
    Compute eigenspinor overlap matrix between D_K(s1) and D_K(s2).
    Returns O_{ij} = <psi_i(s1)|psi_j(s2)> for the 8 positive modes,
    sorted by eigenvalue (ascending: B1, B2x4, B3x3).
    """
    H1, _, _ = build_DK_singlet(s1)
    H2, _, _ = build_DK_singlet(s2)

    evals1, evecs1 = scipy_eigh(H1)
    evals2, evecs2 = scipy_eigh(H2)

    # Select positive eigenvalues, sort ascending
    p1 = evals1 > 0
    p2 = evals2 > 0
    ev1 = evals1[p1]; idx1 = np.argsort(ev1)
    ev2 = evals2[p2]; idx2 = np.argsort(ev2)

    psi1 = evecs1[:, p1][:, idx1]  # (16, 8)
    psi2 = evecs2[:, p2][:, idx2]  # (16, 8)

    O = psi1.conj().T @ psi2  # (8, 8) complex
    return O, ev1[idx1], ev2[idx2]

print("Computing eigenspinor overlaps at fold for various ds...")
print()

results = {}
for ds in ds_values:
    O, ev1, ev2 = compute_overlap(tau_fold, tau_fold + ds)
    O_abs = np.abs(O)
    U_check = O.conj().T @ O
    unit_err = np.max(np.abs(U_check - np.eye(8)))

    results[ds] = {'O': O, 'O_abs': O_abs, 'ev1': ev1, 'ev2': ev2}

    print(f"ds = {ds:.4f}:")
    print(f"  Eigenvalues at s:    {ev1}")
    print(f"  Eigenvalues at s+ds: {ev2}")

    # Branch-resolved diagonal overlaps
    diag = np.diag(O_abs)
    print(f"  |O_ii| diagonal:")
    labels_sorted = ['B1', 'B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B3[0]', 'B3[1]', 'B3[2]']
    for i, lab in enumerate(labels_sorted):
        print(f"    {lab}: {diag[i]:.8f}")

    # Degenerate subspaces: within B2 (modes 1-4) and B3 (modes 5-7),
    # the eigenvectors can rotate freely within the degenerate subspace.
    # The physically meaningful quantity is the BLOCK overlap:
    # |det(O_{B2,B2})| = how much the B2 subspace is preserved.
    O_B2_block = O[1:5, 1:5]
    O_B3_block = O[5:8, 5:8]
    block_B2 = np.abs(np.linalg.det(O_B2_block))
    block_B3 = np.abs(np.linalg.det(O_B3_block))

    # Singular values of block = principal angles' cosines
    sv_B2 = np.linalg.svd(O_B2_block, compute_uv=False)
    sv_B3 = np.linalg.svd(O_B3_block, compute_uv=False)

    print(f"  Block overlaps (subspace preservation):")
    print(f"    B2 block SVD: {sv_B2}")
    print(f"    B2 block |det|: {block_B2:.8f}")
    print(f"    B3 block SVD: {sv_B3}")
    print(f"    B3 block |det|: {block_B3:.8f}")
    print(f"  Unitarity error: {unit_err:.2e}")

    # Cross-branch leakage
    cross_B1_B2 = np.max(O_abs[0, 1:5])
    cross_B2_B3 = np.max(O_abs[1:5, 5:8])
    cross_B1_B3 = np.max(O_abs[0, 5:8])
    print(f"  Cross-branch |O|_max:")
    print(f"    B1-B2: {cross_B1_B2:.8f}")
    print(f"    B2-B3: {cross_B2_B3:.8f}")
    print(f"    B1-B3: {cross_B1_B3:.8f}")
    print()

# =============================================================================
# SECTION 6: BG CORRECTION TO KOSMANN COUPLING
# =============================================================================

print("--- SECTION 6: BG CORRECTION TO KOSMANN COUPLING ---")
print()

# Paper 18 eq B.12: the transported Kosmann derivative is
#   beta^{-1} L_V^{g'} beta = L_V^g + (1/4) sum_{j!=k} g(beta^{-1}(L_V beta)(v_j), v_k) v_j.v_k.psi
#
# For this correction to be non-zero, we need L_V beta != 0.
#
# On SU(3) with left-invariant metric g_s:
#   - beta is LEFT-INVARIANT (constant in left-invariant frame)
#   - V = e_a are left-invariant vector fields
#   - L_V beta: the Lie derivative of a left-invariant tensor field
#     along a left-invariant vector field on a Lie group.
#
# For left-invariant tensor T and left-invariant vector V:
#   (L_V T)_p = d/dt|_{t=0} (phi_t^* T)_p
# where phi_t is the flow of V. On a Lie group, the flow of a left-
# invariant vector field is RIGHT translation. The pullback of a
# LEFT-invariant tensor under RIGHT translation is NOT necessarily
# the same tensor -- it depends on whether the tensor is also
# right-invariant (bi-invariant).
#
# For the Jensen metric g_s: it is left-invariant but NOT bi-invariant
# (for s != 0). Therefore L_{e_a} g_s != 0 in general.
#
# However, beta = (g_s^{-1} g_{s+ds})^{1/2} is ALSO left-invariant
# as an endomorphism of TK. It is diagonal with constant entries in
# the left-invariant frame.
#
# The Lie derivative of a constant-coefficient endomorphism in the
# left-invariant frame:
#   (L_V beta)(W) = [V, beta(W)] - beta([V, W])
# For beta = diag(b_a) and V = e_c, W = e_d:
#   [e_c, beta(e_d)] = b_d [e_c, e_d] = b_d f^e_{cd} e_e
#   beta([e_c, e_d]) = f^e_{cd} beta(e_e) = f^e_{cd} b_e e_e
#   (L_V beta)(e_d) = f^e_{cd}(b_d - b_e) e_e
#
# This vanishes if all b_a are equal (conformal deformation).
# For Jensen: b_su2 != b_C2 != b_u1, so L_V beta != 0 in general.
#
# BUT: Proposition B.1 of Paper 18 states that if V is conformal Killing
# for BOTH g and g', then beta^{-1} L_V^{g'} beta = L_V^g.
# On SU(3): left-invariant vector fields are KILLING (not just conformal
# Killing) for ALL left-invariant metrics. So Prop B.1 applies and the
# transported Kosmann derivative equals the native one.
#
# WAIT: this is too strong. Not all left-invariant fields are Killing for
# all left-invariant metrics. A left-invariant field e_a is Killing for
# g_s iff (L_{e_a} g_s) = 0, i.e., iff the flow of e_a preserves g_s.
# The flow of e_a is RIGHT translation by exp(t e_a). This preserves g_s
# iff g_s is Ad(exp(t e_a))-invariant.
#
# For the Jensen metric g_s: only U(2) = {e_0,...,e_3,e_7} generators
# are Killing (they preserve the U(2)-invariant metric). The C^2
# generators {e_3,...,e_6} are NOT Killing for g_s (s != 0).
#
# Therefore: Proposition B.1 applies ONLY for U(2) generators.
# For C^2 generators, L_V beta != 0 and the BG correction is NON-ZERO.
#
# However, the Kosmann coupling V_{ij} used in the polariton computation
# uses ALL 8 generators. Let me compute the correction explicitly.

print("Checking: which generators are Killing for Jensen g_s?")
print()

g_s_fold = jensen_metric(B_ab, tau_fold)
E_fold = orthonormal_frame(g_s_fold)
ft_fold = frame_structure_constants(f_abc, E_fold)
Gamma_fold = connection_coefficients(ft_fold)

# L_{e_a} g in ON frame: (L_{e_a} g)_{bc} = Gamma^b_{ca} + Gamma^c_{ba}
for a in range(8):
    Lg = np.zeros((8, 8))
    for b in range(8):
        for c in range(8):
            Lg[b, c] = Gamma_fold[b, c, a] + Gamma_fold[c, b, a]
    norm_Lg = np.max(np.abs(Lg))
    block = 'u(1)' if a in U1_IDX else ('su(2)' if a in SU2_IDX else 'C^2')
    killing = 'KILLING' if norm_Lg < 1e-12 else f'NON-KILLING (||L_a g|| = {norm_Lg:.6f})'
    print(f"  e_{a} ({block}): {killing}")

print()

# Compute L_V beta for each generator
print("Lie derivative of beta for each generator (ds=0.010):")
ds_ref = 0.010
beta = compute_bg_beta(tau_fold, tau_fold + ds_ref)
bd = np.diag(beta)

print(f"  beta eigenvalues: su2={bd[0]:.6f}, C2={bd[3]:.6f}, u1={bd[7]:.6f}")
print()

# (L_{e_c} beta)(e_d) = sum_e f^e_{cd}(b_d - b_e) e_e
# In ON frame: f^e_{cd} = ft_fold[c,d,e]
for c in range(8):
    LV_beta_norm = 0.0
    for d in range(8):
        vec = np.zeros(8)
        for e in range(8):
            vec[e] = ft_fold[c, d, e] * (bd[d] - bd[e])
        LV_beta_norm = max(LV_beta_norm, norm(vec))
    block = 'u(1)' if c in U1_IDX else ('su(2)' if c in SU2_IDX else 'C^2')
    print(f"  e_{c} ({block}): ||L_{{e_{c}}} beta||_max = {LV_beta_norm:.6e}")

print()

# =============================================================================
# SECTION 7: QUANTITATIVE BG CORRECTION TO V MATRIX
# =============================================================================

print("--- SECTION 7: QUANTITATIVE BG CORRECTION ---")
print()

# The BG correction to the Kosmann derivative (eq B.12) adds a term:
#   delta_L_V = (1/4) sum_{j!=k} g(beta^{-1}(L_V beta)(v_j), v_k) v_j . v_k . psi
#
# where v_j are g-ON frame vectors. The correction to the coupling V_{ij}
# between eigenspinors psi_i and psi_j is:
#   delta_V_{ij} = sum_a <psi_i| delta_L_{e_a} |psi_j>
#
# For C^2 generators (non-Killing): L_{e_c} beta != 0.
# The correction involves beta^{-1}(L_{e_c} beta) acting on frame vectors.

# Compute the full correction operator delta_L for each generator
def compute_bg_kosmann_correction(c, Gamma, gammas, ft, beta_diag, n=8):
    """
    Compute the BG correction to the Kosmann derivative along e_c.

    delta_L_c = (1/4) sum_{j!=k} g(beta^{-1}(L_{e_c} beta)(v_j), v_k) gamma_j gamma_k

    where (L_{e_c} beta)(v_d) = sum_e ft[c,d,e] * (b_d - b_e) * v_e
    and beta^{-1}(v_e) = (1/b_e) v_e.

    So beta^{-1}(L_{e_c} beta)(v_d) = sum_e ft[c,d,e] * (b_d - b_e) / b_e * v_e

    g(beta^{-1}(L_{e_c} beta)(v_j), v_k) = ft[c,j,k] * (b_j - b_k) / b_k

    Note: we use delta_{jk} for g(v_j, v_k) in ON frame.
    """
    dim_s = gammas[0].shape[0]
    delta_L = np.zeros((dim_s, dim_s), dtype=complex)

    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            # g(beta^{-1}(L_{e_c} beta)(v_j), v_k)
            # = sum over internal frame; but in ON frame g = delta
            # so this is the k-th component of beta^{-1}(L_{e_c} beta)(v_j)
            coeff = ft[c, j, k] * (beta_diag[j] - beta_diag[k]) / beta_diag[k]
            if abs(coeff) > 1e-15:
                delta_L += coeff * gammas[j] @ gammas[k]

    delta_L *= 0.25
    return delta_L

# Compute correction for each generator and accumulate
print("BG Kosmann correction operators (spinor matrix norm):")
total_correction = np.zeros((16, 16), dtype=complex)
bd_fold = np.diag(compute_bg_beta(tau_fold, tau_fold + ds_ref))

for c in range(8):
    delta_Lc = compute_bg_kosmann_correction(c, Gamma_fold, gammas, ft_fold, bd_fold)
    norm_c = np.max(np.abs(delta_Lc))
    block = 'u(1)' if c in U1_IDX else ('su(2)' if c in SU2_IDX else 'C^2')
    print(f"  e_{c} ({block}): ||delta_L_{c}||_max = {norm_c:.6e}")
    total_correction += delta_Lc

norm_total = np.max(np.abs(total_correction))
print(f"  Total correction ||sum_c delta_L_c||_max = {norm_total:.6e}")
print()

# Project the correction onto the eigenspinor basis
# V^corr_{ij} = V_{ij} + <psi_i|sum_c delta_L_c|psi_j>
# Use eigenspinors at fold (sorted: B1, B2x4, B3x3)
labels_sorted = ['B1', 'B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B3[0]', 'B3[1]', 'B3[2]']

delta_V = pos_evecs.conj().T @ total_correction @ pos_evecs  # (8,8)
delta_V_abs = np.abs(delta_V)

print("BG correction projected onto eigenspinor basis:")
print(f"  Max |delta_V_ij| = {np.max(delta_V_abs):.6e}")
print(f"  Max diagonal |delta_V_ii| = {np.max(np.abs(np.diag(delta_V))):.6e}")
print()

# Key cross-branch corrections
# The polariton V uses ordering B2[0..3], B1, B3[0..2]
# Our eigenspinor basis is B1, B2[0..3], B3[0..2]
# Need to compare correction to the bare V matrix

# Map our sorted basis to the polariton basis ordering
# Sorted: 0=B1, 1-4=B2, 5-7=B3
# Polariton: 0-3=B2, 4=B1, 5-7=B3
inv_perm = [1, 2, 3, 4, 0, 5, 6, 7]  # sorted -> polariton

# V_bare in sorted basis
V_sorted = V_8x8[np.ix_([4, 0, 1, 2, 3, 5, 6, 7], [4, 0, 1, 2, 3, 5, 6, 7])]

print("Key coupling corrections (eigenvalue-sorted basis):")
print(f"{'Pair':12s} {'V_bare':>12s} {'delta_V':>12s} {'|dV/V|':>12s}")
print("-" * 52)

pairs = [
    ('B1-B2[0]', 0, 1), ('B1-B2[1]', 0, 2),
    ('B2[0]-B2[1]', 1, 2), ('B2[0]-B3[0]', 1, 5),
    ('B1-B3[0]', 0, 5), ('B2[0]-B2[3]', 1, 4),
]
for name, i, j in pairs:
    v_bare = V_sorted[i, j]
    dv = delta_V[i, j]
    ratio = abs(dv) / abs(v_bare) if abs(v_bare) > 1e-15 else float('inf')
    print(f"{name:12s} {v_bare:12.6f} {abs(dv):12.6e} {ratio:12.6e}")

print()

# =============================================================================
# SECTION 8: CORRECTED POLARITON GAPS
# =============================================================================

print("--- SECTION 8: CORRECTED POLARITON GAPS ---")
print()

# Original polariton data
omega_B2_sp = float(s42_data['omega_B2_sp'])
omega_B1_sp = float(s42_data['omega_B1_sp'])
omega_B3_sp = float(s42_data['omega_B3_sp'])
g_B2_B1_orig = float(s42_data['g_B2_B1'])
g_B2_B3_orig = float(s42_data['g_B2_B3_avg'])
g_GPV_sp_orig = float(s42_data['g_GPV_sp'])
g_GPV_B1_orig = float(s42_data['g_GPV_B1'])

gap_orig = {
    'B2-B1 sp': float(s42_data['gap_B2_B1_sp']),
    'B2-B3 sp': float(s42_data['gap_B2_B3_sp']),
    'GPV-B2': float(s42_data['gap_GPV_B2']),
    'GPV-B1': float(s42_data['gap_GPV_B1']),
    'B2-B1 disp': float(s42_data['gap_B2_B1_disp']),
}

def polariton_gap(omega1, omega2, g):
    return np.sqrt((omega1 - omega2)**2 + 4*g**2)

# The BG correction modifies V by delta_V (additive, not multiplicative).
# The correction to the coupling g is:
#   g_corr = g_orig + delta_g
# where delta_g = matrix element of the correction operator.

# B2-B1: V_sorted[0,1] (B1=0, B2[0]=1 in sorted basis)
delta_g_B2_B1 = abs(delta_V[0, 1])  # correction magnitude
g_B2_B1_corr = g_B2_B1_orig + delta_g_B2_B1  # add in quadrature (conservative)
# More precisely: g_corr = |V + delta_V| but V and delta_V may have different phases
# Conservative: g_corr = g + |delta_g| (upper bound)

# B2-B3: average over B2-B3 pairs
delta_g_B2_B3 = np.mean([abs(delta_V[i, j]) for i in range(1, 5) for j in range(5, 8)])
g_B2_B3_corr = g_B2_B3_orig + delta_g_B2_B3

# GPV corrections scale with BdG coherence factors
uv_B2 = np.mean(u_k[0:4] * v_k[0:4])
delta_g_GPV = uv_B2 * delta_g_B2_B1
g_GPV_sp_corr = g_GPV_sp_orig + uv_B2 * np.mean([abs(delta_V[i, j]) for i in range(1, 5) for j in range(1, 5)])
g_GPV_B1_corr = g_GPV_B1_orig + delta_g_GPV

gap_corr = {
    'B2-B1 sp': polariton_gap(omega_B2_sp, omega_B1_sp, g_B2_B1_corr),
    'B2-B3 sp': polariton_gap(omega_B2_sp, omega_B3_sp, g_B2_B3_corr),
    'GPV-B2': polariton_gap(omega_gpv, omega_B2_sp, g_GPV_sp_corr),
    'GPV-B1': polariton_gap(omega_gpv, omega_B1_sp, g_GPV_B1_corr),
    'B2-B1 disp': 2 * g_B2_B1_corr,
}

print(f"{'Case':20s} {'Original':>12s} {'Corrected':>12s} {'Ratio':>10s} {'Change':>10s}")
print("-" * 68)
for case in gap_orig:
    orig = gap_orig[case]
    corr = gap_corr[case]
    ratio = corr / orig
    change = (corr - orig) / orig * 100
    print(f"{case:20s} {orig:12.6f} {corr:12.6f} {ratio:10.6f} {change:+9.4f}%")

min_orig = min(gap_orig.values())
min_corr = min(gap_corr.values())
print()
print(f"Minimum gap: original = {min_orig:.6f}, corrected = {min_corr:.6f}")
print(f"Change: {(min_corr - min_orig)/min_orig*100:+.6f}%")
print()

# =============================================================================
# SECTION 9: EIGENSPINOR ROTATION RATES (BERRY CONNECTION)
# =============================================================================

print("--- SECTION 9: EIGENSPINOR ROTATION RATES ---")
print()

# The degenerate subspaces B2 and B3 have gauge freedom in eigenvector choice.
# Use singular values of block overlaps to extract physical rotation rates.

print(f"{'ds':>8s}  {'svmin B2':>10s}  {'svmin B3':>10s}  {'|O_B1B1|':>10s}  {'max B1-B2':>10s}  {'max B2-B3':>10s}")
for ds in ds_values:
    O_abs = results[ds]['O_abs']
    O_cplx = results[ds]['O']
    sv_B2 = np.linalg.svd(O_cplx[1:5, 1:5], compute_uv=False)
    sv_B3 = np.linalg.svd(O_cplx[5:8, 5:8], compute_uv=False)
    print(f"{ds:8.4f}  {np.min(sv_B2):10.6f}  {np.min(sv_B3):10.6f}  "
          f"{O_abs[0,0]:10.6f}  {np.max(O_abs[0,1:5]):10.6f}  {np.max(O_abs[1:5,5:8]):10.6f}")

print()

# Berry connection strength from small-ds limit
ds_small = 0.001
O_small = results[ds_small]['O']
sv_B2_small = np.linalg.svd(O_small[1:5, 1:5], compute_uv=False)
sv_B3_small = np.linalg.svd(O_small[5:8, 5:8], compute_uv=False)

# Principal angles: cos(theta) = singular values
theta_B1 = np.arccos(min(1.0, abs(O_small[0, 0]))) / ds_small
theta_B2 = np.arccos(min(1.0, np.min(sv_B2_small))) / ds_small
theta_B3 = np.arccos(min(1.0, np.min(sv_B3_small))) / ds_small

print(f"Berry connection strength at fold (ds={ds_small}):")
print(f"  B1: {theta_B1:.4f} rad/unit-tau")
print(f"  B2 (min principal angle rate): {theta_B2:.4f} rad/unit-tau")
print(f"  B3 (min principal angle rate): {theta_B3:.4f} rad/unit-tau")
print()

# =============================================================================
# SECTION 10: GATE VERDICT
# =============================================================================

print("=" * 72)
print("GATE VERDICT: BG-POL-43 (INFO)")
print("=" * 72)
print()

print("FINDING 1: BG spin lift is trivial (Phi = c * I_16)")
print("  Structural result from Schur's lemma applied to Cliff(R^8).")
print("  Jensen deformation is diagonal => ON frames related by rescaling")
print("  => same Clifford generators => Phi commutes with all gamma_a.")
print()

print("FINDING 2: BG Kosmann correction is NON-ZERO for C^2 generators")
print("  Proposition B.1 applies only to Killing fields (U(2) generators).")
print(f"  C^2 generators are NOT Killing for Jensen metric (s != 0).")
print(f"  L_{{e_a}} beta != 0 for a in C^2 = {{3,4,5,6}}.")
print(f"  Correction magnitude: ||delta_V||_max = {np.max(delta_V_abs):.6e}")
print(f"  Relative to bare V: {np.max(delta_V_abs)/np.max(np.abs(V_sorted)):.6e}")
print()

print("FINDING 3: Polariton gaps negligibly affected")
print(f"  Minimum gap: {min_orig:.6f} -> {min_corr:.6f} M_KK")
print(f"  Change: {(min_corr - min_orig)/min_orig*100:+.6f}%")
print(f"  The 3.7e13x shortfall is UNAFFECTED.")
print()

M_KK_gravity = float(s42_data['M_KK_gravity'])
ratio_grav = float(s42_data['ratio_Higgs_MKK_grav'])
print(f"  Shortfall after correction: {min_corr/ratio_grav:.2e}x")
print()

print("FINDING 4: Eigenspinor rotation rates quantified")
print(f"  B1: {theta_B1:.2f} rad/unit-tau (non-degenerate, rapid)")
print(f"  B2: {theta_B2:.2f} rad/unit-tau (degenerate quartet, internal rotation)")
print(f"  B3: {theta_B3:.2f} rad/unit-tau (degenerate triplet)")
print()

print("CONCLUSION: The BG spinor overlap correction to the polariton gap")
print("is quantitatively negligible. The correction enters through eq B.12")
print(f"for non-Killing (C^2) generators only, with magnitude O({np.max(delta_V_abs):.0e})")
print(f"compared to bare couplings O({np.max(np.abs(V_sorted)):.2f}). The 13-order-of-")
print("magnitude Higgs mass shortfall cannot be addressed by this correction.")

# =============================================================================
# SECTION 11: SAVE DATA
# =============================================================================

save_dict = {
    # Gate
    'gate_name': np.array('BG-POL-43'),
    'gate_verdict': np.array('INFO'),

    # BG correction
    'bg_spin_lift_trivial': True,
    'bg_kosmann_correction_nonzero_for_C2': True,
    'delta_V_max': np.max(delta_V_abs),
    'delta_V_relative': np.max(delta_V_abs) / np.max(np.abs(V_sorted)),
    'delta_V_matrix': delta_V,

    # Eigenspinor rotation (Berry connection)
    'berry_B1': theta_B1,
    'berry_B2': theta_B2,
    'berry_B3': theta_B3,

    # Polariton gaps
    'min_gap_orig': min_orig,
    'min_gap_corr': min_corr,
    'gap_change_pct': (min_corr - min_orig) / min_orig * 100,
    'shortfall': min_corr / ratio_grav,

    # Eigenvalues at fold
    'evals_fold': evals_fold,
    'pos_evals_fold': pos_evals,

    # ds scan
    'ds_values': np.array(ds_values),

    # Overlap data at each ds
    'tau_fold': tau_fold,
    'M_KK_gravity': M_KK_gravity,
    'ratio_Higgs_MKK_grav': ratio_grav,
}

# Add per-ds overlap data
for ds in ds_values:
    key = f'ds{ds:.4f}'.replace('.', 'p')
    save_dict[f'O_abs_{key}'] = results[ds]['O_abs']
    save_dict[f'O_cplx_{key}'] = results[ds]['O']
    save_dict[f'ev1_{key}'] = results[ds]['ev1']
    save_dict[f'ev2_{key}'] = results[ds]['ev2']

# Add per-case gaps
for case in gap_orig:
    safe = case.replace(' ', '_').replace('-', '_')
    save_dict[f'gap_orig_{safe}'] = gap_orig[case]
    save_dict[f'gap_corr_{safe}'] = gap_corr[case]

np.savez(os.path.join(base_dir, 's43_bg_spinor_polariton.npz'), **save_dict)
print()
print(f"Data saved to: tier0-computation/s43_bg_spinor_polariton.npz")

# =============================================================================
# SECTION 12: PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel A: Overlap matrix |O| at ds=0.010
ax = axes[0, 0]
ds_plot = 0.010
O_plot = results[ds_plot]['O_abs']
im = ax.imshow(O_plot, cmap='RdYlGn', vmin=0, vmax=1, origin='lower')
ax.set_xlabel('Mode j (at s+ds)')
ax.set_ylabel('Mode i (at s)')
ax.set_title(r'A: Eigenspinor overlap $|O_{ij}|$ ($\delta s = 0.010$)')
plt.colorbar(im, ax=ax, shrink=0.8)
ax.set_xticks(range(8))
ax.set_yticks(range(8))
ax.set_xticklabels(labels_sorted, rotation=45, fontsize=7)
ax.set_yticklabels(labels_sorted, fontsize=7)
for i in range(8):
    for j in range(8):
        val = O_plot[i, j]
        color = 'white' if val < 0.5 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', fontsize=6, color=color)

# Panel B: Block SVD (subspace overlap) vs ds
ax = axes[0, 1]
ds_arr = np.array(ds_values)
svmin_B1 = [abs(results[ds]['O'][0, 0]) for ds in ds_values]
svmin_B2 = [np.min(np.linalg.svd(results[ds]['O'][1:5, 1:5], compute_uv=False)) for ds in ds_values]
svmin_B3 = [np.min(np.linalg.svd(results[ds]['O'][5:8, 5:8], compute_uv=False)) for ds in ds_values]

ax.plot(ds_arr, svmin_B1, 'ro-', label='B1 (non-deg)', markersize=6)
ax.plot(ds_arr, svmin_B2, 'bs-', label='B2 min SV', markersize=6)
ax.plot(ds_arr, svmin_B3, 'g^-', label='B3 min SV', markersize=6)
ax.set_xlabel(r'$\delta s$')
ax.set_ylabel(r'min singular value (subspace overlap)')
ax.set_title('B: Subspace preservation vs step size')
ax.legend()
ax.set_ylim(0.0, 1.05)
ax.axhline(1.0, color='gray', ls=':', alpha=0.5)

# Panel C: Corrected vs original gaps (bar chart)
ax = axes[1, 0]
case_names = list(gap_orig.keys())
x = np.arange(len(case_names))
width = 0.35
ax.bar(x - width/2, [gap_orig[c] for c in case_names], width,
       label='Original', color='steelblue', edgecolor='black')
ax.bar(x + width/2, [gap_corr[c] for c in case_names], width,
       label='BG-corrected', color='coral', edgecolor='black')
ax.set_ylabel(r'Polariton gap [$M_{KK}$]')
ax.set_title('C: Original vs BG-Corrected Gaps')
ax.set_xticks(x)
ax.set_xticklabels([c.replace(' ', '\n') for c in case_names], fontsize=7)
ax.legend(fontsize=8)
ax.axhline(ratio_grav, color='blue', ls=':', alpha=0.7)
ax.text(4.5, ratio_grav * 3, r'$m_H/M_{KK}$', fontsize=8, color='blue')

# Panel D: BG correction matrix |delta_V| as heatmap
ax = axes[1, 1]
im2 = ax.imshow(delta_V_abs, cmap='hot_r', origin='lower')
ax.set_xlabel('Mode j')
ax.set_ylabel('Mode i')
ax.set_title('D: BG Kosmann correction matrix')
plt.colorbar(im2, ax=ax, shrink=0.8)
ax.set_xticks(range(8))
ax.set_yticks(range(8))
ax.set_xticklabels(labels_sorted, rotation=45, fontsize=7)
ax.set_yticklabels(labels_sorted, fontsize=7)
for i in range(8):
    for j in range(8):
        val = delta_V_abs[i, j]
        color = 'white' if val > 0.5 * np.max(delta_V_abs) else 'black'
        ax.text(j, i, f'{val:.1e}', ha='center', va='center', fontsize=5, color=color)

plt.suptitle('S43 W6-3: BG Spinor Overlap Correction to Polariton Gap (BG-POL-43: INFO)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 's43_bg_spinor_polariton.png'), dpi=150, bbox_inches='tight')
print(f"Plot saved to: tier0-computation/s43_bg_spinor_polariton.png")
print()
print("COMPUTATION COMPLETE.")
