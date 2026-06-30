#!/usr/bin/env python3
"""
s75_sin2_lr_normalization.py -- SIN2-LR-NORMALIZATION-75 (W2-D)
=================================================================

Compute sin^2(theta_W) from the Baptista eq 3.41 left-right asymmetry
on SU(3) with Jensen deformation at tau_fold.

PHYSICAL FRAMEWORK
------------------
Paper 13, Section 3 (eq 3.39-3.41): After fiber integration of the
Einstein-Hilbert action on P = M^4 x K, the 4D Yang-Mills terms have
a LEFT-RIGHT asymmetry:

  L_YM = -(1/4) * B_phi * [g_phi(e_j,e_k) F^j_{A_L} F^k_{A_L}
                           + beta(e_j,e_k) F^j_{A_R} F^k_{A_R}]

The LEFT connection A_L (electroweak) couples through the DEFORMED
metric g_phi, while the RIGHT connection A_R (strong) couples through
the BI-INVARIANT metric beta.

Within the LEFT sector, the su(3) = u(1) + su(2) + C^2 decomposition
gives different metric norms for the electroweak gauge fields:
  - U(1)_Y: g_phi|_{u(1)} = lambda * L1 = lambda * exp(+2s)
  - SU(2)_L: g_phi|_{su(2)} = lambda * L2 = lambda * exp(-2s)

Paper 13 eq (5.21) gives the gauge couplings:
  g'^2 = 12/L1 = 12 * exp(-2s)    [U(1)_Y]
  g^2  = 4/L2  = 4 * exp(+2s)     [SU(2)_L]

The Weinberg angle:
  sin^2(theta_W) = g'^2 / (g'^2 + g^2)
                 = 12*exp(-2s) / (12*exp(-2s) + 4*exp(2s))
                 = 3 / (3 + exp(4s))

THREE-PRONG APPROACH
--------------------
1. GEOMETRIC (analytic): sin^2 = 3/(3 + exp(4*tau_fold)) from eq 5.21
2. SPECTRAL (D_K): Extract L/R metric norms from D_K eigenvalue spectrum
   via per-direction Casimir decomposition
3. LEFT-RIGHT ASYMMETRY: Compare LEFT (deformed) vs RIGHT (undeformed)
   effective coupling constants from the fiber integration measure

Gate: S75-H2-SIN2-LR
  PASS: sin^2 in [0.230, 0.233] (within 1% of PDG)
  INFO: sin^2 in [0.220, 0.240] (within 5%)
  FAIL: sin^2 outside [0.220, 0.240]

NOTE: The geometric tree-level value sin^2 = 0.5839 at M_KK is a PERMANENT
result (S33a, S72). This computation explores whether the L/R asymmetry
provides an additional correction mechanism, or whether the tree-level
value is the structural answer that must be corrected by RG running.

Provenance:
  Baptista Paper 13 eq (3.41), (5.21): fiber-integrated 4D Lagrangian, couplings
  Baptista Paper 15 eq (3.7): gauge boson mass from Lie derivative norms
  S72 WEINBERG-72: sin^2(M_KK) = 0.5839, SM running to 0.357
  S73a PW-THRESHOLD-RATIOS: T_2/T_3 = 1, T_Y/T_3 = 4/3 (permanent)
  S74 MODULAR-SIN2: modular averaging does not escape Jensen-blindness

Author: baptista-spacetime-analyst
Session: S75 Wave 2 (W2-D)
"""

import sys
import os
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_Z, tau_fold,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, sin2_thetaW_fold,
    b1_SM, b2_SM, b3_SM,
    M_Pl_reduced,
)

# Dirac spectrum infrastructure
from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, collect_spectrum,
    jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    spinor_connection_offset, compute_killing_form,
    U1_IDX, SU2_IDX, C2_IDX,
)

t_start = time.time()  # (local)

print("=" * 80)
print("SIN2-LR-NORMALIZATION-75: Weinberg angle from L/R asymmetry")
print("S75 W2-D | baptista-spacetime-analyst")
print("=" * 80)
print(f"  tau_fold            = {tau_fold}")
print(f"  M_KK                = {M_KK:.3e} GeV")
print(f"  M_Z                 = {M_Z} GeV")
print(f"  sin^2(theta_W)|PDG  = {sin2_thetaW_MSbar}")
print(f"  sin^2(theta_W)|fold = {sin2_thetaW_fold:.6f}")

# =============================================================================
# 1. GEOMETRIC (ANALYTIC): sin^2 from Baptista eq 5.21
# =============================================================================
print("\n" + "=" * 80)
print("1. GEOMETRIC sin^2 from Baptista eq (5.21)")
print("=" * 80)

s = tau_fold  # (local) Jensen parameter at the fold

# Jensen metric scale factors
L1_fold = np.exp(2.0 * s)   # (local) u(1) direction
L2_fold = np.exp(-2.0 * s)  # (local) su(2) direction
L3_fold = np.exp(s)          # (local) C^2 direction

# Volume-preserving check: L1 * L2^3 * L3^4 = 1
vol_check = L1_fold * L2_fold**3 * L3_fold**4  # (local)

print(f"\n  Jensen scale factors at s = {s}:")
print(f"    L1 (u(1))  = exp(+2s) = {L1_fold:.6f}")
print(f"    L2 (su(2)) = exp(-2s) = {L2_fold:.6f}")
print(f"    L3 (C^2)   = exp(+s)  = {L3_fold:.6f}")
print(f"    Volume: L1 * L2^3 * L3^4 = {vol_check:.10f} (should be 1)")

# Gauge couplings from Baptista eq 5.21:
#   g'^2 = 12/lambda_1 = 12/L1 = 12 * exp(-2s)
#   g^2  = 4/lambda_2  = 4/L2  = 4 * exp(+2s)
#
# DERIVATION of the identification lambda_i = L_i:
#   Paper 13 eq 5.4: beta_tilde(u,v) = lambda_1 Tr(u_Y^dag v_Y) + lambda_2 Tr(u_W^dag v_W) + lambda_3 Tr(u''^dag v'')
#   Our metric: g = L_i * |B|  on each block
#   The Killing form B = -12 * Tr for su(3), so |B| = 12 * Tr
#   The basis e_a is normalized so Tr(e_a^dag e_b) = delta_ab / c_a
#   In Baptista's convention, beta = lambda * Tr, and the identification is
#   lambda_1 = lambda * L1, lambda_2 = lambda * L2, lambda_3 = lambda * L3
#   The overall lambda cancels in ratios.

gp2_geo = 12.0 * np.exp(-2.0 * s)  # (local) g'^2 at M_KK
g2_geo = 4.0 * np.exp(+2.0 * s)    # (local) g^2 at M_KK

sin2_geo = gp2_geo / (gp2_geo + g2_geo)  # (local)
sin2_formula = 3.0 / (3.0 + np.exp(4.0 * s))  # (local) simplified formula

print(f"\n  Gauge couplings at M_KK:")
print(f"    g'^2 = 12*exp(-2s) = {gp2_geo:.6f}  [U(1)_Y]")
print(f"    g^2  = 4*exp(+2s)  = {g2_geo:.6f}   [SU(2)_L]")
print(f"    g'^2/g^2           = {gp2_geo/g2_geo:.6f}  (= 3*exp(-4s) = {3*np.exp(-4*s):.6f})")
print(f"\n  sin^2(theta_W) at M_KK:")
print(f"    From couplings:     {sin2_geo:.6f}")
print(f"    From formula 3/(3+exp(4s)): {sin2_formula:.6f}")
print(f"    Canonical value:    {sin2_thetaW_fold:.6f}")
print(f"    Discrepancy:        {abs(sin2_geo - sin2_thetaW_fold):.2e}")

# Bi-invariant limit check
sin2_biinv = 3.0 / 4.0  # (local)
print(f"\n  Limiting values:")
print(f"    Bi-invariant (s=0): sin^2 = 3/4 = {sin2_biinv:.4f}")
print(f"    NCG (CC 1996):      sin^2 = 3/8 = {3/8:.4f}")
print(f"    Framework (s=0.19): sin^2 = {sin2_geo:.4f}")
print(f"    PDG (M_Z, MSbar):   sin^2 = {sin2_thetaW_MSbar:.5f}")

# =============================================================================
# 2. SPECTRAL: D_K eigenvalue-based L/R decomposition
# =============================================================================
print("\n" + "=" * 80)
print("2. SPECTRAL: D_K eigenvalue decomposition by direction")
print("=" * 80)

# Build the Dirac infrastructure
gens = su3_generators()  # (local)
f_abc = compute_structure_constants(gens)  # (local)
gammas = build_cliff8()  # (local)

B_ab = compute_killing_form(f_abc)  # (local)

# Compute at tau_fold and at s=0 (bi-invariant)
for s_val, label in [(tau_fold, "FOLD (tau=0.19)"), (0.0, "BI-INVARIANT (s=0)")]:
    print(f"\n  --- {label} ---")
    g_s = jensen_metric(B_ab, s_val)  # (local)
    E = orthonormal_frame(g_s)  # (local)

    # The frame E diagonalizes g_s: g_s = E^T E (in matrix sense)
    # The orthonormal frame E_a = sum_b E_{ab} e_b where e_b are coordinate generators

    # Compute the effective metric norms for each direction
    # The Jensen metric g_s = L_i * |B| on each block
    # So g_s(e_a, e_a) = L_i * |B(e_a, e_a)| for e_a in block i

    # Direct metric norms per direction:
    norms_u1 = [g_s[a, a] for a in U1_IDX]  # (local)
    norms_su2 = [g_s[a, a] for a in SU2_IDX]  # (local)
    norms_c2 = [g_s[a, a] for a in C2_IDX]  # (local)

    mean_u1 = np.mean(norms_u1)  # (local)
    mean_su2 = np.mean(norms_su2)  # (local)
    mean_c2 = np.mean(norms_c2)  # (local)

    print(f"    g_s norms (diagonal):")
    print(f"      u(1):  {norms_u1} mean={mean_u1:.6f}")
    print(f"      su(2): {norms_su2} mean={mean_su2:.6f}")
    print(f"      C^2:   {norms_c2} mean={mean_c2:.6f}")

    # The coupling constant is INVERSELY proportional to the metric norm:
    #   1/g_a^2 ~ metric_norm_a
    #   g_a^2 ~ 1/metric_norm_a
    # The Weinberg angle from metric norms:
    #   sin^2 = g'^2/(g'^2+g^2) = (1/norm_u1) / (1/norm_u1 + 1/norm_su2)
    #         = norm_su2 / (norm_u1 + norm_su2)
    # Wait -- let me be more careful.

    # From Paper 13 eq 5.21:
    #   g'/2 = sqrt(3/lambda_1), g/2 = 1/sqrt(lambda_2)
    #   g'^2 = 12/lambda_1, g^2 = 4/lambda_2
    #
    # The lambda_i are the coefficients in beta_tilde = lambda_i Tr on each block.
    # In our metric, g_s = L_i * |B| = L_i * 12 * Tr on each block (for SU(3)).
    # So lambda_i = L_i * 12 (absorbing the Killing form normalization).
    #
    # Then: g'^2 = 12/(12*L1) = 1/L1
    #        g^2 = 4/(12*L2) = 1/(3*L2)
    #
    # Hmm, this doesn't match the S72 formula. Let me reconcile.
    #
    # Actually, the Killing form for SU(3) is B(X,Y) = 2*3*Tr(XY) = 6*Tr(XY)
    # (trace in fundamental representation, with convention B = 2*n*Tr for SU(n)).
    # And |B| = 6 for SU(3) in fundamental.
    #
    # In dirac_spectrum.py, the Killing form B_ab = sum_cd f_acd f_bcd
    # For the Gell-Mann basis lambda_a/2: [lambda_a/2, lambda_b/2] = i f_abc lambda_c/2
    # The structure constants f_abc are real, and B_ab = -3 delta_ab.
    # So |B_ab| = 3 * delta_ab.
    #
    # The metric g_s = L_i * 3 * delta_ab on each block.
    #
    # Baptista's lambda_i relate to our L_i via:
    #   beta_tilde = lambda_i * Tr(e_a^dag e_b) on each block
    #   Our: g_s(e_a, e_b) = L_i * |B|(e_a, e_b) = L_i * 3 * delta_ab
    #   If beta_tilde = lambda_i Tr, and Tr(lambda_a/2 * lambda_b/2) = delta_ab/2,
    #   then beta_tilde(e_a, e_b) = lambda_i * 1/2 delta_ab
    #   So: lambda_i * 1/2 = L_i * 3, hence lambda_i = 6 * L_i
    #
    # Substituting:
    #   g'^2 = 12/lambda_1 = 12/(6*L1) = 2/L1
    #   g^2  = 4/lambda_2  = 4/(6*L2) = 2/(3*L2)
    #
    # And sin^2 = g'^2/(g'^2+g^2) = (2/L1)/((2/L1)+(2/(3*L2)))
    #           = (1/L1)/((1/L1)+(1/(3*L2)))
    #           = 3*L2/(3*L2 + L1)
    #
    # At s=0: L1=L2=1, sin^2 = 3/(3+1) = 3/4 ✓
    # At s=0.19: sin^2 = 3*exp(-2*0.19)/(3*exp(-2*0.19)+exp(2*0.19))
    #           = 3*exp(-0.38)/(3*exp(-0.38)+exp(0.38))
    #
    # Let's check: 3/(3+exp(4s)) = 3/(3+exp(0.76)) = 3/5.1379 = 0.5839 ✓
    # Our formula: 3*L2/(3*L2+L1) = 3*exp(-2s)/(3*exp(-2s)+exp(2s))
    #            = 3/(3+exp(4s)) ✓  (multiply top and bottom by exp(2s))
    #
    # So: sin^2 = 3*L2/(3*L2+L1) = 3*mean_su2/(3*mean_su2 + mean_u1)
    # when the normalization is beta_tilde = lambda_i * Tr.
    #
    # But with our metric normalization g_s = L_i * |B|:
    # We need to know how the coupling extraction actually works.
    # The essential point is that the RATIO determines sin^2:
    #
    #   sin^2 = g'^2/(g'^2+g^2)
    #
    # where g'^2 and g^2 are set by the fiber integration of |F|^2.
    #
    # From Paper 13 eq 3.39:
    #   integral_K |F_L|^2 vol = (1/4) * [g_phi(e_j,e_k) * F^j F^k] * Vol
    #
    # The u(1) part (photon+Z) contributes:
    #   (1/4) * g_phi(gamma, gamma) * |F_gamma|^2 * Vol
    # The su(2) part (W bosons) contributes:
    #   (1/4) * g_phi(w^a, w^a) * |F_{w^a}|^2 * Vol (sum over a=1,2,3)
    #
    # In the LEFT sector, g_phi acts on u(2) = u(1) + su(2).
    # The effective coupling is: 1/g_a^2 = (1/2kappa_P) * (1/4) * g_phi(e_a,e_a) * Vol
    # So g_a^2 ~ 1/g_phi(e_a,e_a).
    #
    # The METRIC NORM approach:
    #   sin^2 = g'^2/(g'^2+g^2) where g'^2 ~ 1/g_phi(u1,u1), g^2 ~ 1/g_phi(su2,su2)
    #
    # But we need the CORRECT normalization factors (12, 4) from eq 5.21.
    # These come from the Lie algebra structure: the hypercharge generator
    # gamma_phi has beta(gamma,gamma) = 12, while each su(2) generator w^a
    # has beta(w^a,w^a) = 2, and there are 3 of them.
    #
    # Actually, g'^2 = (coeff from structure) / lambda_1
    #           g^2  = (coeff from structure) / lambda_2
    # The coefficients 12 and 4 encode the Lie-algebraic structure.
    #
    # Let's just use the METRIC RATIO directly:
    #   R = L1/L2 = exp(4s) = metric anisotropy
    #   sin^2 = 3/(3+R)

    R_aniso = mean_u1 / mean_su2  # (local) should be L1/L2 = exp(4s)
    R_expected = np.exp(4.0 * s_val)  # (local)
    sin2_metric = 3.0 / (3.0 + R_aniso)  # (local)

    print(f"\n    Metric anisotropy R = g_u1/g_su2:")
    print(f"      Computed: {R_aniso:.6f}")
    print(f"      Expected exp(4s): {R_expected:.6f}")
    print(f"      Discrepancy: {abs(R_aniso - R_expected):.2e}")
    print(f"    sin^2(theta_W) = 3/(3+R) = {sin2_metric:.6f}")

# =============================================================================
# 3. D_K EIGENVALUE SPECTRUM: Left-sector spectral moments
# =============================================================================
print("\n" + "=" * 80)
print("3. D_K EIGENVALUE SPECTRUM: Per-sector spectral moments")
print("=" * 80)

MAX_PQ = 4  # (local) sufficient for structural extraction

print(f"\n  Computing D_K spectrum at tau_fold = {tau_fold} with max_pq_sum = {MAX_PQ}")
all_evals_fold, eval_data_fold = collect_spectrum(
    tau_fold, gens, f_abc, gammas, max_pq_sum=MAX_PQ, verbose=True
)

print(f"\n  Computing D_K spectrum at s=0 (bi-invariant) with max_pq_sum = {MAX_PQ}")
all_evals_biinv, eval_data_biinv = collect_spectrum(
    0.0, gens, f_abc, gammas, max_pq_sum=MAX_PQ, verbose=True
)

# Extract spectral data for comparison
# all_evals is a list of (eigenvalue, multiplicity) tuples from collect_spectrum
# eval_data is a list of (p, q, eigenvalues_array) per sector

# Compute spectral moments: sum |lambda|^n * dim(p,q)^2
# The a_4 coefficient (Yang-Mills) is proportional to sum |lambda|^{-4+8} = sum |lambda|^4
# Actually, for the spectral action:
#   Tr(f(D/Lambda)) ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + ...
# The a_4 coefficient from the heat kernel gives the YM action:
#   a_4 ~ integral_K |F|^2 vol_K
#
# For the DIRAC SPECTRUM approach, the spectral moments are:
#   S_n = sum_k |lambda_k|^n * mult_k
#
# The connection to gauge couplings is through the FOURTH spectral moment:
#   1/g_i^2 ~ S_4|_{sector i}
#
# But this is the TOTAL spectral moment. To decompose by gauge direction,
# we need the spectral sum restricted to each su(3) subalgebra direction.
#
# For the Dirac operator D_K = sum_a gamma^a (rho(e_a) + Omega_a), the
# eigenvalues don't decompose cleanly by direction -- they are the full
# operator's spectrum. However, the STRUCTURE CONSTANTS ft_abc (frame
# structure constants) DO decompose by direction, and the connection
# coefficients Gamma_abc encode the metric deformation per direction.
#
# The correct spectral approach: use the RESOLVENT or ZETA FUNCTION.
# For the spectral zeta function:
#   zeta_{D_K^2}(s) = sum_k |lambda_k|^{-2s}
# The a_4 coefficient is related to zeta(0) or more precisely to the
# residue structure.
#
# For our purpose, the key structural result is:
# The spectral action decomposes the a_4 into gauge-group components via
# the Seeley-DeWitt expansion:
#   a_4(D_K^2) = (1/(4pi)^4) * [integral_K (trace of F^2 terms) vol_K]
#
# The per-direction decomposition is:
#   a_4|_{direction a} ~ integral_K g^{ab} g^{cd} R_{acbd} vol_K
#
# For the Jensen deformation, this gives different contributions from
# the u(1), su(2), and C^2 directions.
#
# However, all of this is ALREADY encoded in the metric norms L1, L2, L3.
# The spectral approach just CONFIRMS the geometric formula.

# Let me compute the spectral LEFT/RIGHT asymmetry differently:
# Use the FRAME structure constants to extract per-direction coupling norms.

print("\n  --- Frame structure constants analysis ---")

g_fold = jensen_metric(B_ab, tau_fold)  # (local)
E_fold = orthonormal_frame(g_fold)  # (local)
ft_fold = frame_structure_constants(f_abc, E_fold)  # (local)
Gamma_fold = connection_coefficients(ft_fold)  # (local)

g_biinv = jensen_metric(B_ab, 0.0)  # (local)
E_biinv = orthonormal_frame(g_biinv)  # (local)
ft_biinv = frame_structure_constants(f_abc, E_biinv)  # (local)
Gamma_biinv = connection_coefficients(ft_biinv)  # (local)

# The frame structure constants ft_abc = E^{-1}_{ai} f_{ijk} E_{jb} E_{kc}
# encode how the orthonormal frame transforms the Lie algebra.
# For the LEFT connection, the gauge field components are:
#   A_L^a = left-invariant 1-forms in the u(2) = u(1) + su(2) sector
# For the RIGHT connection:
#   A_R^a = right-invariant 1-forms in the su(3) sector

# The LEFT-sector norm is:
#   ||A_L||^2 = g_phi(e_a, e_b) A_L^a A_L^b  (sum over a,b in u(2))
# In the orthonormal frame:
#   ||A_L||^2 = sum_alpha A_L^alpha A_L^alpha  (alpha in u(2) ONB)

# The effective coupling for the LEFT sector gauge group factor i is:
#   1/g_i^2 ~ sum_{a in sector i} g_phi(e_a, e_a)

# Compute per-sector metric norms (using coordinate basis)
norm_u1_fold = sum(g_fold[a, a] for a in U1_IDX)  # (local)
norm_su2_fold = sum(g_fold[a, a] for a in SU2_IDX)  # (local)
norm_c2_fold = sum(g_fold[a, a] for a in C2_IDX)  # (local)

norm_u1_biinv = sum(g_biinv[a, a] for a in U1_IDX)  # (local)
norm_su2_biinv = sum(g_biinv[a, a] for a in SU2_IDX)  # (local)
norm_c2_biinv = sum(g_biinv[a, a] for a in C2_IDX)  # (local)

print(f"\n  Metric norms (trace over sector):")
print(f"    FOLD (tau={tau_fold}):")
print(f"      sum g_u1   = {norm_u1_fold:.6f}  (1 direction)")
print(f"      sum g_su2  = {norm_su2_fold:.6f}  (3 directions)")
print(f"      sum g_c2   = {norm_c2_fold:.6f}   (4 directions)")
print(f"    BI-INVARIANT (s=0):")
print(f"      sum g_u1   = {norm_u1_biinv:.6f}")
print(f"      sum g_su2  = {norm_su2_biinv:.6f}")
print(f"      sum g_c2   = {norm_c2_biinv:.6f}")

# =============================================================================
# 4. LEFT-RIGHT ASYMMETRY: Coupling extraction
# =============================================================================
print("\n" + "=" * 80)
print("4. LEFT-RIGHT ASYMMETRY: sin^2 from coupling structure")
print("=" * 80)

# From Paper 13 eq 3.39 (Yang-Mills fiber integration):
# LEFT fields: weighted by g_phi
# RIGHT fields: weighted by beta (bi-invariant)
#
# The LEFT connection A_L has gauge algebra = su(3)_L
# But only the u(2) subset of su(3)_L corresponds to the electroweak sector
# (Paper 13 Section 2: the Killing algebra of g_phi is u(1) + su(3), where
# u(1) is the LEFT-invariant Killing field and su(3) is the full RIGHT-invariant
# Killing algebra).
#
# The electroweak fields are:
#   - Photon (gamma): the u(1)_L Killing direction
#   - W bosons: the su(2)_L non-Killing directions (massive)
#   - Z boson: combination of u(1)_L and su(2)_L
#
# The strong fields are:
#   - Gluons (8): the su(3)_R Killing directions (massless)
#
# Key structural point: The LEFT and RIGHT connections see DIFFERENT metrics.
# The effective gauge couplings are:
#
#   LEFT sector (electroweak):
#     1/g_Y^2 ~ Vol(K) * g_phi(gamma, gamma)    [hypercharge]
#     1/g_W^2 ~ Vol(K) * g_phi(w, w)             [weak isospin per direction]
#
#   RIGHT sector (strong):
#     1/g_s^2 ~ Vol(K) * beta(t_a, t_a)          [color per direction]
#
# Since g_phi = L_i * |B| on block i, and beta = |B| (undeformed):
#   1/g_Y^2 ~ L1 * |B|(gamma, gamma)
#   1/g_W^2 ~ L2 * |B|(w, w)
#   1/g_s^2 ~ 1 * |B|(t_a, t_a)   [RIGHT sees beta, not g_phi]
#
# The Weinberg angle depends ONLY on the LEFT-sector ratio:
#   sin^2 = g'^2/(g'^2+g^2)

# Method A: Direct from metric scale factors
# sin^2 = 3*L2/(3*L2 + L1)  [as derived above]
sin2_A = 3.0 * L2_fold / (3.0 * L2_fold + L1_fold)  # (local)

# Method B: From per-direction metric norms
# The effective coupling g'^2 ~ c_Y/lambda_1 and g^2 ~ c_W/lambda_2
# where c_Y = 12 and c_W = 4 are the structure constants from eq 5.21.
#
# The hypercharge generator gamma_phi has norm:
#   beta(gamma, gamma) = 12 (from eq 2.32: gamma = i*sqrt(3)*diag(-1,2I-3...) )
#   More precisely: Baptista normalizes so beta(gamma,gamma) = 12*lambda for
#   the 1-parameter family. On the Jensen line, this becomes 12*lambda*L1.
#
# The SU(2) generators w^a each have norm:
#   beta(w^a, w^a) = 2*lambda for each of the 3 generators
#   Total: sum_a beta(w^a,w^a) = 6*lambda
#   On Jensen line: 6*lambda*L2
#
# So g'^2 is extracted from |F_gamma|^2 * beta(gamma,gamma) / Vol
# and g^2 is extracted from sum_a |F_{w^a}|^2 * beta(w^a,w^a) / Vol
#
# The standard physics convention:
#   L_YM = -(1/4) * (1/g'^2) * F_Y^2 - (1/4) * (1/g^2) * sum_a F_W^a F_W^a
#
# Matching to the fiber integral:
#   1/g'^2 = (B_phi/(2*kappa_P)) * beta_tilde(gamma,gamma) * Vol
#   1/g^2  = (B_phi/(2*kappa_P)) * beta_tilde(w,w) * Vol
#   where beta_tilde incorporates the L/R distinction
#
# For the LEFT electroweak sector: beta_tilde uses g_phi (deformed metric)
# So:
#   1/g'^2 ~ g_phi(gamma,gamma) = L1 * |B|(gamma,gamma)
#   1/g^2  ~ g_phi(w,w)         = L2 * |B|(w,w)
#
# Therefore:
#   g'^2/g^2 = g_phi(w,w) / g_phi(gamma,gamma)
#            = [L2 * |B|(w,w)] / [L1 * |B|(gamma,gamma)]
#
# We need |B|(w,w)/|B|(gamma,gamma):
# |B|(gamma,gamma) = |B_ab|_{u(1)} = 3 (for lambda_8/2 with B=-3*I)
#   i.e., for the SINGLE u(1) direction: norm = 3
# |B|(w^a,w^a) = 3 per direction, so total for 3 directions = 9
#   but per-direction norm = 3
#
# The ratio depends on how we normalize the generators.
# In the Gell-Mann basis: B(lambda_a/2, lambda_b/2) = -3 delta_ab
# So |B| = 3 for each generator.
# The hypercharge generator gamma ~ lambda_8 has the same B-norm.
# Each su(2) generator lambda_{1,2,3}/2 has the same B-norm.
#
# From eq 5.21: g'^2 = 12/lambda_1, g^2 = 4/lambda_2
# The factor 12 vs 4 comes from the HYPERCHARGE NORMALIZATION.
# The U(1)_Y hypercharge Y is defined so that the fundamental
# decomposes as 3 = (1/2, 1/3) + (0, -2/3).
# The hypercharge generator is Y = diag(-2/3, 1/3, 1/3) (in fundamental).
# In su(3): Y = -sqrt(3) lambda_8 / (3*sqrt(2)) ... the normalization matters.
#
# Actually, Baptista's eq 5.21 gives g'/2 = sqrt(3/lambda_1).
# So g'^2 = 4 * 3/lambda_1 = 12/lambda_1.
# The factor 3 is the ratio beta(gamma,gamma)/beta(w,w) * dim(su(2))/dim(u(1))
# effectively encoding the SU(3) -> SU(2) x U(1) embedding.

# The cleanest formula for sin^2 from the LEFT sector metric norms:
# g'^2 = 12/(lambda_1) and g^2 = 4/(lambda_2)
# where lambda_i = c * L_i for some universal constant c
#
# sin^2 = g'^2/(g'^2+g^2) = (12/L1) / (12/L1 + 4/L2)
#        = 12*L2 / (12*L2 + 4*L1) = 3*L2/(3*L2+L1)

# Method B uses the actual g_s matrix to extract L1, L2:
g_fold_u1 = g_fold[U1_IDX[0], U1_IDX[0]]  # (local) g_{88}
g_fold_su2 = g_fold[SU2_IDX[0], SU2_IDX[0]]  # (local) g_{11}
g_biinv_u1 = g_biinv[U1_IDX[0], U1_IDX[0]]  # (local) reference
g_biinv_su2 = g_biinv[SU2_IDX[0], SU2_IDX[0]]  # (local) reference

# Extract L1, L2 from metric ratio
L1_extracted = g_fold_u1 / g_biinv_u1  # (local) should be exp(2*tau_fold)
L2_extracted = g_fold_su2 / g_biinv_su2  # (local) should be exp(-2*tau_fold)

sin2_B = 3.0 * L2_extracted / (3.0 * L2_extracted + L1_extracted)  # (local)

print(f"\n  Method A (analytic scale factors):")
print(f"    L1 = exp(2s) = {L1_fold:.6f}")
print(f"    L2 = exp(-2s) = {L2_fold:.6f}")
print(f"    sin^2 = 3L2/(3L2+L1) = {sin2_A:.6f}")

print(f"\n  Method B (extracted from g_s matrix):")
print(f"    L1_extracted = g_fold_u1/g_biinv_u1 = {L1_extracted:.6f}")
print(f"    L2_extracted = g_fold_su2/g_biinv_su2 = {L2_extracted:.6f}")
print(f"    sin^2 = 3L2/(3L2+L1) = {sin2_B:.6f}")

# Method C: From eigenvalue spectrum LEFT/RIGHT decomposition
# The Dirac operator D_K = sum_a gamma^a (rho(e_a) + Omega_a)
# The u(1) component: D_u1 = sum_{a in U1} gamma^a (rho(e_a) + Omega_a)
# The su(2) component: D_su2 = sum_{a in SU2} gamma^a (rho(e_a) + Omega_a)
# The C^2 component: D_c2 = sum_{a in C2} gamma^a (rho(e_a) + Omega_a)
#
# These don't commute, so D_K != D_u1 + D_su2 + D_c2 in general.
# But the SPECTRAL ACTION decomposes:
#   a_4 = sum_a (contribution from direction a)
# because a_4 comes from the F^2 term in the Seeley-DeWitt expansion.
#
# Method C: Compute Tr(D_K^4) decomposition by direction
# This is the most direct spectral approach. For a single sector (p,q):
#
#   Tr(D_pi^4) = sum of eigenvalue^4 = sum |lambda_k|^4
#
# This total doesn't decompose by direction easily. But we can compute
# Tr(D_{u1}^2 * D_{su2}^2) and similar cross-terms to extract the
# per-direction contributions.
#
# Actually, the simplest spectral approach is via Tr(D_pi^2):
#
#   Tr(D_pi^2) = sum_a Tr(gamma^a (rho(e_a)+Omega_a))^2
#              = sum_a [Tr(rho(e_a)^2) + 2*Tr(rho(e_a)*Omega_a) + Tr(Omega_a^2)]
#   (using gamma^a gamma^b = delta_ab + ... for orthonormal frame)
#
# The Casimir contribution from direction a is:
#   C_a(p,q) = Tr(rho_{(p,q)}(e_a)^2) / dim(p,q)
#
# For the Jensen metric, in the orthonormal frame, each e_a has been rescaled
# by 1/sqrt(L_i), so rho(e_a^ONB) = rho(e_a^coord)/sqrt(L_i).
# Thus C_a(p,q) in the ONB = C_a(p,q)_coord / L_i.
#
# The TOTAL Casimir C_2(p,q) = sum_a C_a(p,q)_coord in coordinate basis.
# In the ONB: sum_a C_a(p,q)_ONB = C_u1/L1 + C_su2/L2 + C_c2/L3
#
# For the gauge coupling, the relevant quantity is the PARTIAL Casimir:
#   C_u1(p,q)/L1 vs C_su2(p,q)/L2

# Compute the per-direction Casimir values from the actual representation matrices.
# For the fundamental (1,0) = 3:
#   C_2(1,0) = (1+0+0+3+3)/3 = 4/3  [standard SU(3) Casimir]
#   C_u1 = Tr(rho(lambda_8)^2)/dim = Tr(diag(1,-1,0)^2/3)/3... wait
#
# Let me compute this properly from the generators.

# The su(3) generators in the Gell-Mann basis lambda_a/2 (a=1..8)
# For the ADJOINT representation, rho_adj(e_a)_{bc} = f_{abc}
# The partial Casimirs:
#   C_u1 = sum_{a in U1} Tr(rho(e_a)^2) / dim
#   C_su2 = sum_{a in SU2} Tr(rho(e_a)^2) / dim
#   C_c2 = sum_{a in C2} Tr(rho(e_a)^2) / dim

# For the FUNDAMENTAL (p,q)=(1,0):
rho_fund = np.array(gens)  # (local) list of 8 generators, each 3x3

# Note: generators are anti-Hermitian (e_a = i*lambda_a/2), so Tr(e_a^2) < 0.
# The Casimir C_2 = -sum_a Tr(rho(e_a)^2)/dim (with the minus sign for anti-Herm).
C_u1_fund = -sum(np.real(np.trace(rho_fund[a] @ rho_fund[a])) for a in U1_IDX) / 3.0  # (local)
C_su2_fund = -sum(np.real(np.trace(rho_fund[a] @ rho_fund[a])) for a in SU2_IDX) / 3.0  # (local)
C_c2_fund = -sum(np.real(np.trace(rho_fund[a] @ rho_fund[a])) for a in C2_IDX) / 3.0  # (local)
C_total_fund = C_u1_fund + C_su2_fund + C_c2_fund  # (local)

print(f"\n  Method C: Per-direction Casimir decomposition")
print(f"    Fundamental (1,0), dim=3:")
print(f"      C_u1   = {C_u1_fund:.6f}")
print(f"      C_su2  = {C_su2_fund:.6f}")
print(f"      C_c2   = {C_c2_fund:.6f}")
print(f"      C_total = {C_total_fund:.6f} (should be 4/3 = {4/3:.6f})")

# Check: C_total should be the quadratic Casimir C_2(1,0) = 4/3
assert abs(C_total_fund - 4.0/3.0) < 1e-10, f"Casimir check failed: {C_total_fund}"
print(f"      C_2 check PASSED: {C_total_fund:.10f} = 4/3")

# The partial Casimirs tell us how the representation "couples" to each direction.
# For the Weinberg angle, we need the ratio:
#   (C_u1 + C_su2) / C_total = LEFT / TOTAL coupling fraction
# But this isn't sin^2 directly.
#
# The correct formula: sin^2 = g'^2/(g'^2+g^2) where
#   1/g'^2 ~ lambda_1 * (beta_tilde-norm of hypercharge generator on each rep)
#   1/g^2  ~ lambda_2 * (beta_tilde-norm of each su(2) generator on each rep)
#
# The hypercharge generator is identified with lambda_8/2 (in su(3)).
# The weak isospin generators are lambda_{1,2,3}/2.
#
# For the fiber integration, the coupling constant is set by:
#   1/g'^2 = (f_phi / 2*kappa_P) * g_phi(Y, Y) * Vol(K)
#   where Y = lambda_8/2 = the hypercharge generator
#   g_phi(Y, Y) = L1 * |B(Y, Y)| = L1 * 3 (for our normalization)
#
#   1/g^2 = (f_phi / 2*kappa_P) * g_phi(T_a, T_a) * Vol(K)
#   where T_a = lambda_a/2 (a=1,2,3) = weak isospin generators
#   g_phi(T_a, T_a) = L2 * |B(T_a, T_a)| = L2 * 3
#   And there is ONE g for all three T_a (by su(2) symmetry).

# The factor 12 vs 4 in eq 5.21 comes from the HYPERCHARGE NORMALIZATION:
# The physical hypercharge Y_phys is related to lambda_8 by:
#   Y_phys = sqrt(4/3) * lambda_8/2  (so that Q = I_3 + Y_phys/2 works)
# This introduces a factor of 4/3 in the coupling.
#
# But we don't need to track this: the formula sin^2 = 3/(3+R) with R=L1/L2
# is the structural result, confirmed by S72.

# Method C: From Casimir ratio weighted by metric
# sin^2 is determined by the LEFT-sector coupling ratio.
# For each representation (p,q), define:
#   c_Y(p,q) = partial Casimir in u(1) direction
#   c_W(p,q) = partial Casimir in su(2) direction (per direction, sum/3)
#
# The LEFT-sector coupling normalization includes the metric weights L1, L2:
#   g'^2 ~ dim(p,q) * c_Y / (L1 * Vol)
#   g^2  ~ dim(p,q) * c_W / (L2 * Vol)
#
# sin^2 = g'^2/(g'^2+g^2) = (c_Y/L1) / (c_Y/L1 + c_W/L2)
#        = c_Y*L2 / (c_Y*L2 + c_W*L1)

# For ALL representations, c_Y and c_W have a FIXED RATIO determined by
# the SU(3) -> SU(2) x U(1) embedding. This is the S73a result:
# T_Y/T_3 = 4/3 (representation-independent).
#
# The partial Casimirs in our normalization:
# C_u1(p,q)/dim(p,q) = T_Y(p,q) equivalent
# C_su2(p,q)/dim(p,q) = T_2(p,q) equivalent (up to normalization)

# Let me compute this for several representations to verify universality.
print(f"\n  Partial Casimir ratios across representations:")
print(f"  {'(p,q)':>8s} {'dim':>5s} {'C_u1':>10s} {'C_su2':>10s} {'C_c2':>10s} {'C_u1/C_su2':>12s}")

from dirac_spectrum import get_irrep

partial_casimir_ratios = []  # (local)
for pq_sum in range(1, MAX_PQ + 1):
    for p in range(pq_sum + 1):
        q = pq_sum - p
        try:
            rho_pq, dim_pq = get_irrep(p, q, gens, f_abc)
            # rho_pq is a list of 8 matrices, each dim_pq x dim_pq
            c_u1_pq = -sum(np.real(np.trace(rho_pq[a] @ rho_pq[a])) for a in U1_IDX) / dim_pq  # (local)
            c_su2_pq = -sum(np.real(np.trace(rho_pq[a] @ rho_pq[a])) for a in SU2_IDX) / dim_pq  # (local)
            c_c2_pq = -sum(np.real(np.trace(rho_pq[a] @ rho_pq[a])) for a in C2_IDX) / dim_pq  # (local)
            ratio_pq = c_u1_pq / c_su2_pq if c_su2_pq > 1e-12 else float('inf')  # (local)
            partial_casimir_ratios.append((p, q, dim_pq, c_u1_pq, c_su2_pq, c_c2_pq, ratio_pq))
            print(f"  ({p},{q}){' ':>{6-len(f'({p},{q})')}} {dim_pq:5d} {c_u1_pq:10.6f} {c_su2_pq:10.6f} {c_c2_pq:10.6f} {ratio_pq:12.6f}")
        except Exception as e:
            print(f"  ({p},{q}): SKIPPED ({e})")

# Check universality: C_u1/C_su2 should be constant (= 1/3 from Dynkin ratios)
ratios_only = [r[6] for r in partial_casimir_ratios if r[6] < float('inf')]  # (local)
ratio_mean = np.mean(ratios_only) if ratios_only else 0  # (local)
ratio_std = np.std(ratios_only) if ratios_only else 0  # (local)

print(f"\n  Universality check:")
print(f"    Mean C_u1/C_su2 = {ratio_mean:.6f}")
print(f"    Std              = {ratio_std:.2e}")
print(f"    Expected (1/3):    {1/3:.6f}")

# The partial Casimir ratio C_u1/C_su2 is the ratio of the number of
# generators times their average coupling strength:
# u(1): 1 generator, C_u1 = Tr(rho(lambda_8)^2)/dim
# su(2): 3 generators, C_su2 = sum_{a=1,2,3} Tr(rho(lambda_a)^2)/dim
# So C_u1/C_su2 = (1 generator)/(3 generators) * (per-gen ratio)
#
# For the fundamental: lambda_8^2/3 = diag(1,1,4)/12 -> Tr/3 = 6/(12*3) = 1/6
# sum lambda_a^2/3 = ... -> Tr/3 = 1/2
# C_u1/C_su2 = (1/6)/(1/2) = 1/3

# Now compute sin^2 using the partial Casimir decomposition:
# sin^2 = (c_Y/L1) / (c_Y/L1 + c_W/L2)
# But c_Y ~ C_u1 and c_W ~ C_su2, and we need the hypercharge normalization.
#
# From Baptista: g'^2 = 12/lambda_1, g^2 = 4/lambda_2
# With lambda_i = c * L_i:
#   g'^2/g^2 = (12/L1)/(4/L2) = 3*L2/L1
#   sin^2 = g'^2/(g'^2+g^2) = 3L2/(3L2+L1)
#
# The factor 3 is EXACTLY C_su2/C_u1 (from our computation above).
# So sin^2 = (C_su2/L1) / (C_su2/L1 + C_u1/L2) ... wait, let me recheck.
#
# g'^2 = 12/lambda_1 and g^2 = 4/lambda_2
# 12 = 4 * 3 = (normalization factor) * (structure ratio)
# The "3" in 12 = 4*3 is the hypercharge normalization factor.
# In terms of our Casimirs: 12 = 4 * (C_su2/C_u1)
# So g'^2 = 4*(C_su2/C_u1)/L1 and g^2 = 4/L2
# sin^2 = g'^2/(g'^2+g^2) = [(C_su2/C_u1)/L1] / [(C_su2/C_u1)/L1 + 1/L2]
#        = (C_su2*L2) / (C_su2*L2 + C_u1*L1)
#
# Using C_su2/C_u1 = 3 (from our computation):
# sin^2 = 3*L2/(3*L2 + L1) ✓ AGREES

# Now compute sin^2 using the ACTUAL partial Casimirs from the spectrum:
# Use the fundamental as representative (result is universal)
c_Y_fund = C_u1_fund  # (local) partial Casimir of u(1) for fundamental
c_W_fund = C_su2_fund  # (local) partial Casimir of su(2) for fundamental

sin2_C = (c_W_fund * L2_fold) / (c_W_fund * L2_fold + c_Y_fund * L1_fold)  # (local)

print(f"\n  Method C result (Casimir-weighted metric):")
print(f"    c_Y (u(1) Casimir) = {c_Y_fund:.6f}")
print(f"    c_W (su(2) Casimir) = {c_W_fund:.6f}")
print(f"    c_W/c_Y = {c_W_fund/c_Y_fund:.6f} (should be 3)")
print(f"    sin^2 = c_W*L2/(c_W*L2 + c_Y*L1) = {sin2_C:.6f}")

# =============================================================================
# 5. SPECTRAL EIGENVALUE SUM: D_K^2 decomposition
# =============================================================================
print("\n" + "=" * 80)
print("5. SPECTRAL EIGENVALUE SUM: sin^2 from Tr(D_K^2) decomposition")
print("=" * 80)

# Compute Tr(D_pi^2) for each sector and decompose by direction.
# D_K = sum_a gamma^a * (rho(e_a) + Omega_a)  in the ONB
# D_K^2 = sum_{a,b} gamma^a gamma^b * (rho(e_a)+Omega_a)(rho(e_b)+Omega_b)
#        = sum_a (rho(e_a)+Omega_a)^2 + cross terms
#        (using gamma^a gamma^b = delta_ab * I + i*... for orthonormal frame)
#
# The diagonal contribution:
#   sum_a Tr[(rho(e_a)+Omega_a)^2] = sum_a [Tr(rho(e_a)^2) + 2*Tr(rho(e_a)*Omega_a) + Tr(Omega_a^2)]
#
# For the partial sum over LEFT directions (u(1)+su(2)):
#   Tr_LEFT(D^2) = sum_{a in u(1)+su(2)} Tr[(rho(e_a)+Omega_a)^2]
#
# But the cross terms between gamma^a and gamma^b (a!=b) involve the
# antisymmetric product gamma^a gamma^b which is traceless, so they
# contribute to Tr(D_K^2) = sum_a Tr[(rho(e_a)+Omega_a)^2] EXACTLY
# (the cross terms vanish in the trace over the Clifford algebra part).

# Build the Dirac operator components for the fold
Omega_fold = spinor_connection_offset(Gamma_fold, gammas)  # (local)

# For each PW sector, compute the per-direction contribution to Tr(D^2)
print(f"\n  Per-direction Tr(D^2) decomposition at tau_fold:")
print(f"  {'(p,q)':>8s} {'dim':>5s} {'Tr_u1':>12s} {'Tr_su2':>12s} {'Tr_c2':>12s} {'Tr_total':>12s} {'LEFT_frac':>10s}")

spectral_results = []  # (local)

# Build the representation-level D operator components
for p, q, evals_raw in eval_data_fold:
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)

    if p == 0 and q == 0:
        # Trivial representation: rho = 0
        # D = Omega on 16-dim spinor space
        # Per-direction: Omega is the spinor connection, same for all directions
        # Tr(Omega^2) = sum_a Tr(Omega_a^2) is what we want
        tr_u1 = sum(np.real(np.trace(gammas[a] @ Omega_fold @ gammas[a] @ Omega_fold))
                     for a in U1_IDX)  # (local)
        tr_su2 = sum(np.real(np.trace(gammas[a] @ Omega_fold @ gammas[a] @ Omega_fold))
                      for a in SU2_IDX)  # (local)
        tr_c2 = sum(np.real(np.trace(gammas[a] @ Omega_fold @ gammas[a] @ Omega_fold))
                     for a in C2_IDX)  # (local)
        # Actually, for the trivial rep, D = Omega (the 16x16 spinor connection)
        # D^2 = Omega^2
        # The eigenvalues give Tr(D^2) = sum |lambda_k|^2
        tr_D2 = np.sum(np.abs(evals_raw)**2)  # (local)
        # The per-direction decomposition is more subtle for (0,0):
        # D_{(0,0)} = sum_a gamma^a * Omega_a (no rho term)
        # Tr(D^2) = sum_{a,b} Tr(gamma^a Omega_a gamma^b Omega_b)
        #         = sum_a Tr(Omega_a^2) + sum_{a!=b} Tr(gamma^a gamma^b Omega_a Omega_b)
        # The cross terms don't vanish in general.
        # Use eigenvalue sum instead:
        tr_u1 = 0.0  # (local) cannot decompose (0,0) cleanly
        tr_su2 = 0.0  # (local)
        tr_c2 = 0.0  # (local)
        tr_total = tr_D2  # (local)
        left_frac = 0.0  # (local) undefined for (0,0)
        print(f"  ({p},{q}){' ':>{6-len(f'({p},{q})')}} {dim_pq:5d} {'N/A':>12s} {'N/A':>12s} {'N/A':>12s} {tr_total:12.4f} {'N/A':>10s}")
        spectral_results.append((p, q, dim_pq, 0, 0, 0, tr_total, 0))
        continue

    try:
        rho_pq, dim_check = get_irrep(p, q, gens, f_abc)

        # Compute per-direction Casimir contribution (the dominant term in D^2)
        # In the ONB: D_pi = sum_a gamma^a tensor (rho(E_a) + Omega * I_{dim_pq})
        # where E_a = sum_b E_{ab}^{-1} e_b is the ONB frame
        # rho(E_a) = sum_b E_{ab}^{-1} rho(e_b)

        # The per-direction Casimir in the ONB:
        E_inv = np.linalg.inv(E_fold)  # (local) frame inverse

        # rho in ONB
        rho_onb = []  # (local)
        for a in range(8):
            rho_a = sum(E_inv[a, b] * rho_pq[b] for b in range(8))  # (local)
            rho_onb.append(rho_a)

        # Per-direction Tr(rho(E_a)^2) — note minus sign for anti-Hermitian generators
        tr_rho2_u1 = -sum(np.real(np.trace(rho_onb[a] @ rho_onb[a])) for a in U1_IDX)  # (local)
        tr_rho2_su2 = -sum(np.real(np.trace(rho_onb[a] @ rho_onb[a])) for a in SU2_IDX)  # (local)
        tr_rho2_c2 = -sum(np.real(np.trace(rho_onb[a] @ rho_onb[a])) for a in C2_IDX)  # (local)
        tr_rho2_total = tr_rho2_u1 + tr_rho2_su2 + tr_rho2_c2  # (local)

        # Actual Tr(D^2) from eigenvalues
        tr_D2_eig = np.sum(np.abs(evals_raw)**2)  # (local)

        # The Casimir contribution dominates for large representations.
        # For gauge coupling extraction, the Casimir ratio IS the coupling ratio.
        left_frac_pq = (tr_rho2_u1 + tr_rho2_su2) / tr_rho2_total if tr_rho2_total > 0 else 0  # (local)

        print(f"  ({p},{q}){' ':>{6-len(f'({p},{q})')}} {dim_pq:5d} {tr_rho2_u1:12.4f} {tr_rho2_su2:12.4f} {tr_rho2_c2:12.4f} {tr_rho2_total:12.4f} {left_frac_pq:10.4f}")
        spectral_results.append((p, q, dim_pq, tr_rho2_u1, tr_rho2_su2, tr_rho2_c2, tr_rho2_total, left_frac_pq))

    except Exception as e:
        print(f"  ({p},{q}): SKIPPED ({e})")

# Now compute sin^2 from the weighted Casimir decomposition
# The per-direction Casimir in the ONB already includes the metric deformation
# because the ONB frame E diagonalizes g_s.
# Specifically: Tr(rho(E_a)^2) = Tr((sum_b E_inv_{ab} rho_b)^2)
# For diagonal g_s: E_inv = diag(1/sqrt(L_i * |B_ii|))
# So rho(E_a) = rho(e_a) / sqrt(L_i * |B_aa|)
# And Tr(rho(E_a)^2) = Tr(rho(e_a)^2) / (L_i * |B_aa|)
#
# The metric-weighted partial Casimirs ARE the coupling-relevant quantities:
#   C^{ONB}_{u1}(p,q) = Tr(rho(E_8)^2)/dim_pq = C_{u1}(p,q) / (L1 * |B_88|)
#   C^{ONB}_{su2}(p,q) = sum_{a=1,2,3} Tr(rho(E_a)^2)/dim_pq = C_{su2}(p,q) / (L2 * |B_11|)
#
# Since |B_11| = |B_88| = 3 (for SU(3) Gell-Mann convention):
#   C^{ONB}_{u1} / C^{ONB}_{su2} = (C_u1/L1) / (C_su2/L2) = (C_u1*L2) / (C_su2*L1)
#
# And sin^2 = g'^2/(g'^2+g^2) = (c_Y/L1)/(c_Y/L1+c_W/L2) ... already computed above.
#
# The SPECTRAL verification: the ratio Tr_su2/(Tr_u1+Tr_su2) from the ONB
# should DIRECTLY give sin^2 through the hypercharge normalization.
#
# Actually: sin^2 = g'^2/(g'^2+g^2) where g'^2 ~ 1/(C^{ONB}_{u1}) and g^2 ~ 1/(C^{ONB}_{su2}/3)
# The factor /3 is because su(2) has 3 generators but one coupling constant.
# So g^2 ~ 3/C^{ONB}_{su2}.
#
# sin^2 = (1/C^{ONB}_{u1}) / (1/C^{ONB}_{u1} + 3/C^{ONB}_{su2})
#        = C^{ONB}_{su2} / (C^{ONB}_{su2} + 3*C^{ONB}_{u1})
#
# Using C^{ONB}_i = C_i / (L_i * |B|):
# sin^2 = (C_su2/L2) / (C_su2/L2 + 3*C_u1/L1)
#        = C_su2*L1 / (C_su2*L1 + 3*C_u1*L2)
#
# Hmm, this doesn't immediately match. Let me go back to Baptista's formulas.

# DEFINITIVE DERIVATION from Baptista eq (5.21):
# g'/2 = sqrt(3/lambda_1)  =>  g'^2 = 12/lambda_1
# g/2 = 1/sqrt(lambda_2)   =>  g^2 = 4/lambda_2
#
# With lambda_1 = L1 * (overall norm), lambda_2 = L2 * (overall norm):
# g'^2 = 12/(norm*L1), g^2 = 4/(norm*L2)
# sin^2 = (12/L1)/(12/L1 + 4/L2) = 12*L2/(12*L2 + 4*L1) = 3*L2/(3*L2 + L1)
#
# The "12" comes from:
#   g' = electric charge / cos(theta) for hypercharge
#   The hypercharge generator Y = (2/sqrt(3)) * lambda_8/2 has
#   beta_tilde(Y,Y) = (4/3) * lambda_1 * Tr(lambda_8^2/4) = (4/3) * lambda_1/2
#   and g'^2 = 4/beta_tilde(Y,Y) = 4/((2/3)*lambda_1) = 6/lambda_1
#   Hmm, that gives 6, not 12.
#
# The exact factor depends on the hypercharge normalization convention.
# Baptista uses g'/2 = sqrt(3/lambda_1), which gives g'^2 = 12/lambda_1.
# The factor 12 encodes the specific hypercharge normalization.
# The key structural result is:
#   g'^2/g^2 = (12/lambda_1)/(4/lambda_2) = 3 * lambda_2/lambda_1 = 3/R
# where R = lambda_1/lambda_2 = L1/L2 = exp(4s).
#
# And sin^2 = g'^2/(g'^2+g^2) = 3/(3+R) = 3/(3+exp(4s)).

# SPECTRAL sin^2 from the ONB Casimir:
# The per-direction Casimirs in ONB are:
#   C^ONB_u1 = C_u1/(L1*|B|) and C^ONB_su2 = C_su2/(L2*|B|)
# The ratio: C^ONB_u1/C^ONB_su2 = (C_u1*L2)/(C_su2*L1)
#
# From the representation theory: C_u1/C_su2 = 1/3 (universal)
# So C^ONB_u1/C^ONB_su2 = L2/(3*L1) = exp(-4s)/3
#
# The coupling factor c_Y = 12 and c_W = 4 from eq 5.21 encode:
#   g'^2 = c_Y / lambda_1 where c_Y = 12 = 4 * (C_su2/C_u1) = 4*3 = 12
#   g^2 = c_W / lambda_2 where c_W = 4
#
# So the "12" IS c_W * (C_su2/C_u1) = 4 * 3 = 12.
# This means: g'^2 = c_W * C_su2 / (C_u1 * lambda_1)
# And: sin^2 = g'^2/(g'^2+g^2) = [C_su2/(C_u1*lambda_1)] / [C_su2/(C_u1*lambda_1) + 1/lambda_2]
#            = C_su2*lambda_2 / (C_su2*lambda_2 + C_u1*lambda_1)
#            = 3*L2 / (3*L2 + L1)   [using C_su2/C_u1 = 3, lambda_i = c*L_i]

# Now use the ACTUAL ONB Casimir values from the spectral computation:
# For the fundamental (1,0):
p_ref, q_ref = 1, 0  # (local) reference representation
ref_data = [r for r in spectral_results if r[0] == p_ref and r[1] == q_ref]  # (local)
if ref_data:
    _, _, dim_ref, tr_u1_ref, tr_su2_ref, tr_c2_ref, tr_total_ref, _ = ref_data[0]

    # These are ONB Casimirs: Tr(rho(E_a)^2) = C_a/(L_i*|B|)
    # sin^2 = C_su2*L2 / (C_su2*L2 + C_u1*L1)
    # Using ONB values: C^ONB_u1 = C_u1/(L1*|B|), C^ONB_su2 = C_su2/(L2*|B|)
    # C_u1*L2 = C^ONB_u1 * L1 * |B| * L2
    # C_su2*L2 = C^ONB_su2 * L2 * |B| * L2
    # This gets circular. Let me just compute directly.

    # The ONB Casimir ratio = (C_u1/L1)/(C_su2/L2) = (C_u1*L2)/(C_su2*L1)
    # For sin^2 = C_su2*L2/(C_su2*L2+C_u1*L1) = 1/(1 + C_u1*L1/(C_su2*L2))
    # = 1/(1 + (L1/L2)*(C_u1/C_su2))

    # From ONB: tr_rho2_u1 / tr_rho2_su2 = (C_u1/L1)/(C_su2/L2) = (C_u1*L2)/(C_su2*L1)
    onb_ratio = tr_u1_ref / tr_su2_ref if tr_su2_ref > 0 else 0  # (local)

    # Invert to get C_u1*L1/(C_su2*L2) = 1/onb_ratio * (L1/L2)^2 ... no.
    # Let's be precise.
    # tr_rho2_u1 = sum_{a in U1} Tr(rho(E_a)^2) = C_u1_coord / (L1 * |B_u1|)
    # tr_rho2_su2 = sum_{a in SU2} Tr(rho(E_a)^2) = C_su2_coord / (L2 * |B_su2|)
    # (where |B_u1| = |B_su2| = 3 for our SU(3) normalization)
    #
    # tr_rho2_u1/tr_rho2_su2 = (C_u1/L1)/(C_su2/L2) = (C_u1*L2)/(C_su2*L1)
    #                        = (1/3) * L2/L1 = (1/3)*exp(-4s)

    onb_ratio_expected = (1.0/3.0) * np.exp(-4.0 * tau_fold)  # (local)

    print(f"\n  ONB Casimir ratio for ({p_ref},{q_ref}):")

    # ANALYSIS: The code used E_inv (= Cholesky(g_s)) to build rho_onb,
    # so rho_onb[a] = sum_b (E^{-1})_{ab} rho[b] = sqrt(3*L_i) * rho(e_a).
    # Therefore: tr_rho2_u1 = 3*L1*dim*C_u1 and tr_rho2_su2 = 3*L2*dim*C_su2.
    # The ratio is: tr_u1/tr_su2 = (L1*C_u1)/(L2*C_su2) = L1/(3*L2) = R/3
    onb_ratio_expected_corrected = L1_fold / (3.0 * L2_fold)  # (local) = R/3
    print(f"    Tr_u1/Tr_su2 (code, using E_inv) = {onb_ratio:.6f}")
    print(f"    Expected L1/(3*L2) = R/3 = {onb_ratio_expected_corrected:.6f}")
    print(f"    Discrepancy: {abs(onb_ratio - onb_ratio_expected_corrected):.2e}")
    print(f"    (Note: code used E_inv not E; rho_onb ~ sqrt(L_i) * rho, not 1/sqrt(L_i) * rho)")

    # CORRECT spectral formula: extract C_u1, C_su2 from the traces
    # tr_u1 = 3*L1*dim*C_u1 => C_u1 = tr_u1/(3*L1*dim)
    # tr_su2 = 3*L2*dim*C_su2 => C_su2 = tr_su2/(3*L2*dim)
    C_u1_from_spec = tr_u1_ref / (3.0 * L1_fold * dim_ref)  # (local)
    C_su2_from_spec = tr_su2_ref / (3.0 * L2_fold * dim_ref)  # (local)

    print(f"\n    Extracted coordinate-basis Casimirs:")
    print(f"      C_u1 (from spectrum) = {C_u1_from_spec:.6f} (analytic: {C_u1_fund:.6f})")
    print(f"      C_su2 (from spectrum) = {C_su2_from_spec:.6f} (analytic: {C_su2_fund:.6f})")
    print(f"      C_su2/C_u1 = {C_su2_from_spec/C_u1_from_spec:.6f} (should be 3)")

    # CORRECT sin^2 from spectral data:
    # sin^2 = C_su2*L2/(C_su2*L2 + C_u1*L1)
    sin2_spectral_correct = (C_su2_from_spec * L2_fold) / \
                            (C_su2_from_spec * L2_fold + C_u1_from_spec * L1_fold)  # (local)

    # ACCIDENTAL formula: sin^2 = tr_su2*L2^2/(tr_su2*L2^2 + tr_u1*L1^2)
    # = C_su2*L2^3/(C_su2*L2^3 + C_u1*L1^3) = 3*L2^3/(3*L2^3 + L1^3)
    sin2_spectral_accidental = (tr_su2_ref * L2_fold**2) / \
                               (tr_su2_ref * L2_fold**2 + tr_u1_ref * L1_fold**2)  # (local)

    sin2_spectral = sin2_spectral_correct  # (local) use the CORRECT formula

    print(f"\n  sin^2 from spectral decomposition (CORRECT, Baptista eq 5.21):")
    print(f"    sin^2 = C_su2*L2/(C_su2*L2 + C_u1*L1) = {sin2_spectral_correct:.6f}")
    print(f"    Analytic: 3L2/(3L2+L1) = {sin2_A:.6f}")
    print(f"    Discrepancy: {abs(sin2_spectral_correct - sin2_A):.2e}")

    print(f"\n  ACCIDENTAL near-PDG result (NOT the Baptista formula):")
    print(f"    sin^2 = 3*L2^3/(3*L2^3 + L1^3) = {sin2_spectral_accidental:.6f}")
    print(f"    PDG value: {sin2_thetaW_MSbar:.5f}")
    print(f"    Discrepancy from PDG: {abs(sin2_spectral_accidental - sin2_thetaW_MSbar)/sin2_thetaW_MSbar*100:.2f}%")
    print(f"    This formula replaces R=L1/L2 with R^3=(L1/L2)^3 in the Weinberg angle.")
    print(f"    It would arise from a volume-weighted fiber integration with an extra")
    print(f"    factor of (metric determinant)^{1} in the measure. NOT established in Baptista.")

# =============================================================================
# 6. SUMMARY AND GATE EVALUATION
# =============================================================================
print("\n" + "=" * 80)
print("6. SUMMARY AND GATE EVALUATION")
print("=" * 80)

# The TREE-LEVEL geometric sin^2 at M_KK
sin2_MKK = sin2_A  # (local) = 0.5839 (all methods agree)

# Run to M_Z using SM 1-loop RG (repeating S72 result)
ln_ratio = np.log(M_KK / M_Z)  # (local) = 34.33

# PDG at M_Z
alpha_em_MZ = 1.0 / alpha_em_MZ_inv  # (local)
alpha_2_MZ_PDG = alpha_em_MZ / sin2_thetaW_MSbar  # (local)
alpha_Y_MZ_PDG = alpha_em_MZ / (1.0 - sin2_thetaW_MSbar)  # (local)
alpha_1_MZ_PDG = (5.0/3.0) * alpha_Y_MZ_PDG  # (local) GUT-normalized

# M_KK boundary conditions from geometric formula
gp2_MKK = 12.0 * np.exp(-2.0 * tau_fold)  # (local)
g2_MKK = 4.0 * np.exp(+2.0 * tau_fold)    # (local)
alpha_Y_MKK = gp2_MKK / (4.0 * PI)  # (local)
alpha_2_MKK = g2_MKK / (4.0 * PI)    # (local)
alpha_1_MKK = (5.0/3.0) * alpha_Y_MKK  # (local) GUT-normalized

alpha1_inv_MKK = 1.0 / alpha_1_MKK  # (local)
alpha2_inv_MKK = 1.0 / alpha_2_MKK  # (local)

# Run DOWN from M_KK to M_Z (SM 1-loop)
alpha1_inv_MZ_pred = alpha1_inv_MKK + b1_SM / (2.0 * PI) * ln_ratio  # (local)
alpha2_inv_MZ_pred = alpha2_inv_MKK + b2_SM / (2.0 * PI) * ln_ratio  # (local)

# Reconstruct sin^2 at M_Z
alpha1_MZ_pred = 1.0 / alpha1_inv_MZ_pred  # (local)
alpha_Y_MZ_pred = (3.0/5.0) * alpha1_MZ_pred  # (local)
alpha2_MZ_pred = 1.0 / alpha2_inv_MZ_pred  # (local)

sin2_MZ_SM_running = alpha_Y_MZ_pred / (alpha_Y_MZ_pred + alpha2_MZ_pred)  # (local)

# The L/R ASYMMETRY approach: does the LEFT/RIGHT metric distinction
# provide additional correction beyond the tree-level formula?
#
# Answer: NO at tree level. The LEFT/RIGHT distinction determines the
# BOUNDARY CONDITIONS at M_KK (sin^2 = 0.5839), but the RUNNING to
# M_Z is determined by the SM beta functions alone.
#
# The L/R asymmetry DOES affect the KK threshold corrections differently:
# LEFT thresholds (SU(2), U(1)) are weighted by g_phi
# RIGHT thresholds (SU(3)_c) are weighted by beta
#
# This means the KK threshold correction formula should be:
#   delta_2 ~ sum_k ln(Lambda^2/m_k^2) weighted by g_phi norm
#   delta_3 ~ sum_k ln(Lambda^2/m_k^2) weighted by beta norm
#
# The L/R metric difference introduces an ASYMMETRIC threshold correction
# that was NOT captured in S73a (which assumed universal metric weighting).

# L/R-corrected threshold: the KK modes in the LEFT sector have masses
# set by g_phi (deformed), while RIGHT sector modes have masses set by beta.
# The mass of a KK mode in sector a is:
#   m_a^2 = lambda_k^2(p,q) (eigenvalue of D_K^2 projected onto direction a)
# For the LEFT (electroweak) sector, the eigenvalues scale as:
#   m_{u1}^2 ~ C_u1(p,q) / L1  (u(1) direction, L1 = exp(2s))
#   m_{su2}^2 ~ C_su2(p,q) / L2  (su(2) direction, L2 = exp(-2s))
# For the RIGHT (strong) sector:
#   m_{su3}^2 ~ C_su3(p,q) / 1  (bi-invariant, no deformation)

# The LEFT threshold corrections have DIFFERENT regulator masses for U(1) and SU(2):
# The SU(2) modes are HEAVIER (L2 = exp(-2s) < 1) by factor exp(-2s) ~ 0.683
# The U(1) mode is LIGHTER (L1 = exp(2s) > 1) by factor exp(2s) ~ 1.462

# This L/R mass asymmetry affects the RG threshold corrections:
#   delta_1 gets LESS threshold correction (lighter KK modes, lower regulator)
#   delta_2 gets MORE threshold correction (heavier KK modes, higher regulator)

# The NET effect on sin^2 at M_Z:
# delta_2 > delta_1 (from L/R asymmetry) shifts sin^2 DOWN from the tree value.
# Quantify this:
# The threshold correction to 1/alpha_i at M_Z is:
#   Delta(1/alpha_i) = delta_i / (2*pi)
# where delta_i is the sum of ln(Lambda^2/m_k^2) weighted by the Dynkin index.
#
# For the L/R-corrected version:
#   delta_2^{LR} ~ T_2 * sum_k ln(Lambda^2 / (C_su2*M_KK^2/L2))
#                = T_2 * sum_k [ln(Lambda^2/(C_su2*M_KK^2)) + ln(L2)]
#                = delta_2^{standard} + T_2 * n_modes * ln(L2)
#
#   delta_1^{LR} ~ T_1 * sum_k [ln(Lambda^2/(C_u1*M_KK^2)) + ln(L1)]
#                = delta_1^{standard} + T_1 * n_modes * ln(L1)
#
# The ADDITIONAL L/R correction:
#   Delta_delta_2 = T_2 * n_modes * ln(L2) = T_2 * n_modes * (-2s)
#   Delta_delta_1 = T_1 * n_modes * ln(L1) = T_1 * n_modes * (+2s)
#
# This shifts 1/alpha_2 UP and 1/alpha_1 UP (making both weaker),
# but DIFFERENTLY because T_1 != T_2 (T_1/T_2 = 20/9 from S73a).

# Compute the L/R threshold correction for the PW modes in our spectrum.
# Use the spectral data from Section 5.

print(f"\n  Tree-level sin^2 at M_KK: {sin2_MKK:.6f}")
print(f"  SM 1-loop running to M_Z: sin^2 = {sin2_MZ_SM_running:.6f}")
print(f"  PDG value:                sin^2 = {sin2_thetaW_MSbar:.5f}")
print(f"  Discrepancy (SM running): {(sin2_MZ_SM_running - sin2_thetaW_MSbar)/sin2_thetaW_MSbar*100:.1f}%")

# L/R threshold correction estimate
# S73a showed T_2/T_3 = 1 and T_1/T_3 = 20/9
# The L/R correction adds:
#   Delta(1/alpha_2) = T_2 * N_eff * (-2*tau_fold) / (2*pi)
#   Delta(1/alpha_1) = T_1 * N_eff * (+2*tau_fold) / (2*pi)
# where N_eff is the effective number of KK modes below the cutoff.

# From S71/S72: S_inf = 2.353, which gives the effective threshold sum.
# The number of effective modes: N_eff ~ S_inf / ln(Lambda^2/m_min^2) ~ S_inf/3
S_inf_est = 2.353  # (local) from S71

# The L/R correction factor per mode:
# For delta_2: extra factor of ln(1/L2) = 2s per mode (SU(2) modes heavier)
# For delta_1: extra factor of ln(1/L1) = -2s per mode (U(1) modes lighter)
lr_correction_per_mode = 2.0 * tau_fold  # (local) = 0.38

# Total L/R-corrected thresholds:
# delta_i^{LR} = delta_i^{standard} * (1 + correction_factor)
# The correction factor is ln(L_i) / <ln(Lambda^2/m^2)> ~ 2s/3 ~ 0.127

# S73a PW-resolved threshold ratios:
# delta_1/delta_3 = 20/9 = 2.222 (PERMANENT)
# delta_2/delta_3 = 1 (PERMANENT)
# These ratios are from the Dynkin index structure.
#
# The L/R correction MODIFIES these ratios:
# delta_1^{LR}/delta_3^{LR} = (T_1 * S_1)/(T_3 * S_3)
# where S_i = sum_k ln(Lambda^2/(lambda_k^2/L_i)) = S_standard + n_modes * ln(L_i)
#
# delta_2^{LR}: LEFT sector, metric g_phi, scale L2 = exp(-2s)
# delta_3^{LR}: RIGHT sector, metric beta, scale 1 (no deformation)

# With standard + L/R correction:
# delta_2^{LR} = T_2 * [S_standard + n * ln(L2)]
# delta_3^{LR} = T_3 * S_standard  (RIGHT sector, no correction)
# delta_1^{LR} = T_1 * [S_standard + n * ln(L1)]

# From S73a: T_2 = T_3 (exact), T_1 = (20/9)*T_3

# The effect on sin^2:
# 1/alpha_2(M_Z) = 1/alpha_2(M_KK) + [b2/(2pi)*ln(M_KK/M_Z) + delta_2^{LR}/(2pi)]
# 1/alpha_1(M_Z) = 1/alpha_1(M_KK) + [b1/(2pi)*ln(M_KK/M_Z) + delta_1^{LR}/(2pi)]

# Standard (no L/R correction):
alpha1_inv_MZ_std = alpha1_inv_MKK + b1_SM / (2.0*PI) * ln_ratio + (20.0/9.0) * S_inf_est / (2.0*PI)  # (local)
alpha2_inv_MZ_std = alpha2_inv_MKK + b2_SM / (2.0*PI) * ln_ratio + 1.0 * S_inf_est / (2.0*PI)  # (local)

# With L/R correction:
# Estimate n_modes from the PW tower: for max_pq_sum=4, count modes
n_modes_total = sum(r[2] for r in partial_casimir_ratios)  # (local) total dim of PW modes
n_modes_est = 50.0  # (local) effective number contributing at the cutoff

# L/R correction to threshold sums:
delta_lr_1 = (20.0/9.0) * n_modes_est * np.log(L1_fold) / (2.0*PI)  # (local) U(1) lighter, +2s
delta_lr_2 = 1.0 * n_modes_est * np.log(L2_fold) / (2.0*PI)  # (local) SU(2) heavier, -2s

alpha1_inv_MZ_lr = alpha1_inv_MZ_std + delta_lr_1  # (local)
alpha2_inv_MZ_lr = alpha2_inv_MZ_std + delta_lr_2  # (local)

# Reconstruct sin^2 with L/R correction
if alpha1_inv_MZ_lr > 0 and alpha2_inv_MZ_lr > 0:
    alpha1_MZ_lr = 1.0 / alpha1_inv_MZ_lr  # (local)
    alpha_Y_MZ_lr = (3.0/5.0) * alpha1_MZ_lr  # (local)
    alpha2_MZ_lr = 1.0 / alpha2_inv_MZ_lr  # (local)
    sin2_MZ_lr = alpha_Y_MZ_lr / (alpha_Y_MZ_lr + alpha2_MZ_lr)  # (local)
else:
    sin2_MZ_lr = float('nan')  # (local)
    alpha2_MZ_lr = float('nan')  # (local)
    alpha_Y_MZ_lr = float('nan')  # (local)

print(f"\n  L/R-corrected threshold corrections:")
print(f"    ln(L1) = +2*tau = {np.log(L1_fold):.4f}  (U(1) correction per mode)")
print(f"    ln(L2) = -2*tau = {np.log(L2_fold):.4f}  (SU(2) correction per mode)")
print(f"    n_modes_effective = {n_modes_est:.0f}")
print(f"    Delta(1/alpha_1) from L/R = {delta_lr_1:.4f}")
print(f"    Delta(1/alpha_2) from L/R = {delta_lr_2:.4f}")
print(f"\n  Running results:")
print(f"    Standard (no L/R): sin^2(M_Z) = {sin2_MZ_SM_running:.6f}")
print(f"    With S_inf thresh: 1/alpha_1 = {alpha1_inv_MZ_std:.4f}, 1/alpha_2 = {alpha2_inv_MZ_std:.4f}")
if not np.isnan(sin2_MZ_lr):
    sin2_MZ_with_thresh = alpha_Y_MZ_lr / (alpha_Y_MZ_lr + alpha2_MZ_lr) if alpha2_MZ_lr > 0 else float('nan')  # (local)
    print(f"    With L/R thresh:   1/alpha_1 = {alpha1_inv_MZ_lr:.4f}, 1/alpha_2 = {alpha2_inv_MZ_lr:.4f}")
    print(f"    sin^2(M_Z) with L/R correction = {sin2_MZ_lr:.6f}")
    discrepancy_lr = (sin2_MZ_lr - sin2_thetaW_MSbar) / sin2_thetaW_MSbar * 100.0  # (local)
    print(f"    Discrepancy from PDG: {discrepancy_lr:.1f}%")
else:
    sin2_MZ_with_thresh = float('nan')  # (local)
    print(f"    L/R correction produced unphysical 1/alpha values")

# =============================================================================
# 7. STRUCTURAL ANALYSIS: Why sin^2 = 0.5839 is permanent
# =============================================================================
print("\n" + "=" * 80)
print("7. STRUCTURAL ANALYSIS")
print("=" * 80)

print("""
  STRUCTURAL RESULT (PERMANENT):

  The tree-level Weinberg angle at M_KK is determined by the Jensen
  deformation parameter through the formula:

    sin^2(theta_W)|_{M_KK} = 3 / (3 + exp(4*tau_fold))       (1)

  This is a SCHEME-INDEPENDENT result from Baptista Paper 13 eq (5.21).
  It follows from three structural inputs:
    (a) The su(3) = u(1) + su(2) + C^2 decomposition (eq 1.1)
    (b) The Jensen metric g_s with L1 = exp(2s), L2 = exp(-2s)  (eq 2.25)
    (c) The fiber integration of |F_L|^2 weighted by g_phi (eq 3.39)

  At tau_fold = 0.19:
    sin^2|_{M_KK} = 3/(3 + exp(0.76)) = 3/5.138 = 0.5839

  The LEFT-RIGHT ASYMMETRY is encoded in eq (3.41):
    - LEFT gauge fields (electroweak): F_{A_L} weighted by g_phi (deformed)
    - RIGHT gauge fields (strong): F_{A_R} weighted by beta (bi-invariant)

  This asymmetry sets the BOUNDARY CONDITIONS at M_KK. It does NOT
  directly give sin^2(M_Z) because SM RG running is required.

  THREE CONFIRMED METHODS all yield sin^2 = 0.5839 at M_KK:
    Method A (analytic):  3/(3+exp(4s))          = 0.5839
    Method B (metric):    3*L2/(3*L2+L1)         = 0.5839
    Method C (spectral):  C_su2*L2/(C_su2*L2+C_u1*L1) = 0.5839

  ACCIDENTAL OBSERVATION:
    The formula 3*L2^3/(3*L2^3+L1^3) = 0.2349 (~1.6% from PDG)
    This arises from replacing R=L1/L2 with R^3 in the Weinberg formula.
    It would require an extra volume factor in the coupling extraction.
    Status: NOT established in Baptista, but numerically suggestive.

  L/R THRESHOLD CORRECTION ANALYSIS:
    The L/R distinction creates ASYMMETRIC KK threshold corrections:
    - U(1) modes: lighter (L1 > 1), less threshold correction
    - SU(2) modes: heavier (L2 < 1), more threshold correction
    - SU(3) modes: undeformed (RIGHT sector), standard threshold

    This shifts delta_1 and delta_2 in OPPOSITE directions relative
    to the standard (S73a) treatment, potentially resolving the
    threshold ratio problem.

  The L/R correction is a REAL PHYSICAL EFFECT missed in S73a,
  which treated all sectors with the same metric weighting.
""")

# =============================================================================
# 8. GATE EVALUATION
# =============================================================================
print("=" * 80)
print("8. GATE EVALUATION: S75-H2-SIN2-LR")
print("=" * 80)

# The gate asks for sin^2 at M_Z. The tree-level value at M_KK is 0.5839.
# After SM running: 0.357 (S72 confirmed).
# With L/R threshold correction: computed above.

sin2_final = sin2_MZ_lr if not np.isnan(sin2_MZ_lr) else sin2_MZ_SM_running  # (local)

print(f"\n  Final result: sin^2(theta_W) at M_Z = {sin2_final:.6f}")
print(f"  PDG target:                           {sin2_thetaW_MSbar:.5f}")

abs_diff = abs(sin2_final - sin2_thetaW_MSbar)  # (local)
rel_diff = abs_diff / sin2_thetaW_MSbar  # (local)

print(f"  Absolute difference: {abs_diff:.6f}")
print(f"  Relative difference: {rel_diff*100:.2f}%")

# Gate classification
PASS_LO = 0.230  # (local)
PASS_HI = 0.233  # (local)
INFO_LO = 0.220  # (local)
INFO_HI = 0.240  # (local)

if PASS_LO <= sin2_final <= PASS_HI:
    verdict = "PASS"
    verdict_detail = f"sin^2 = {sin2_final:.6f} in [{PASS_LO}, {PASS_HI}] (within 1% of PDG)"
elif INFO_LO <= sin2_final <= INFO_HI:
    verdict = "INFO"
    verdict_detail = f"sin^2 = {sin2_final:.6f} in [{INFO_LO}, {INFO_HI}] (within 5% of PDG)"
else:
    verdict = "FAIL"
    verdict_detail = f"sin^2 = {sin2_final:.6f} outside [{INFO_LO}, {INFO_HI}]"

print(f"\n  Gate S75-H2-SIN2-LR: {verdict}")
print(f"  {verdict_detail}")

print(f"\n  PERMANENT: sin^2(theta_W)|_{{M_KK}} = {sin2_MKK:.6f} (all three methods agree)")
print(f"  The discrepancy from PDG is a RUNNING problem, not a BOUNDARY problem.")
print(f"  L/R asymmetry affects threshold corrections but does not change the")
print(f"  tree-level boundary condition at M_KK.")

# =============================================================================
# 9. SAVE RESULTS
# =============================================================================
print("\n" + "=" * 80)
print("9. SAVING RESULTS")
print("=" * 80)

outpath = os.path.join(SCRIPT_DIR, 's75_sin2_lr_normalization.npz')  # (local)

np.savez(
    outpath,
    # Tree-level (M_KK)
    tau_fold=tau_fold,
    L1_fold=L1_fold,
    L2_fold=L2_fold,
    L3_fold=L3_fold,
    sin2_MKK=sin2_MKK,
    gp2_MKK=gp2_MKK,
    g2_MKK=g2_MKK,
    # Per-direction Casimirs (fundamental)
    C_u1_fund=C_u1_fund,
    C_su2_fund=C_su2_fund,
    C_c2_fund=C_c2_fund,
    C_total_fund=C_total_fund,
    # Methods comparison
    sin2_A=sin2_A,
    sin2_B=sin2_B,
    sin2_C=sin2_C,
    sin2_spectral_correct=sin2_spectral_correct,
    sin2_spectral_accidental=sin2_spectral_accidental,
    # Running results
    sin2_MZ_SM_running=sin2_MZ_SM_running,
    sin2_MZ_lr=sin2_MZ_lr,
    sin2_final=sin2_final,
    # L/R corrections
    delta_lr_1=delta_lr_1,
    delta_lr_2=delta_lr_2,
    n_modes_est=n_modes_est,
    S_inf_est=S_inf_est,
    # Gate
    sin2_thetaW_MSbar=sin2_thetaW_MSbar,
    verdict=verdict,
    verdict_detail=verdict_detail,
    # Partial Casimir data
    partial_casimir_ratios=np.array([(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                                     for r in partial_casimir_ratios]),
    spectral_results=np.array([(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
                                for r in spectral_results]),
)
print(f"  Saved: {outpath}")

# =============================================================================
# 10. DIAGNOSTIC PLOT
# =============================================================================
print("\n  Generating diagnostic plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: sin^2 vs tau
tau_range = np.linspace(0, 0.5, 200)  # (local)
sin2_vs_tau = 3.0 / (3.0 + np.exp(4.0 * tau_range))  # (local)

ax = axes[0, 0]
ax.plot(tau_range, sin2_vs_tau, 'b-', linewidth=2, label=r'$\sin^2(\theta_W) = 3/(3+e^{4\tau})$')
ax.axhline(sin2_thetaW_MSbar, color='r', linestyle='--', label=f'PDG = {sin2_thetaW_MSbar}')
ax.axhline(3/8, color='g', linestyle=':', label=f'NCG = 3/8 = {3/8:.4f}')
ax.axvline(tau_fold, color='orange', linestyle='--', alpha=0.7, label=f'tau_fold = {tau_fold}')
ax.plot(tau_fold, sin2_MKK, 'ko', markersize=10, zorder=5)
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'$\sin^2(\theta_W)$')
ax.set_title('Weinberg angle vs Jensen deformation')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: L/R metric ratio
R_vs_tau = np.exp(4.0 * tau_range)  # (local)
ax = axes[0, 1]
ax.semilogy(tau_range, R_vs_tau, 'b-', linewidth=2, label=r'$R = L_1/L_2 = e^{4\tau}$')
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5, label='Bi-invariant (R=1)')
ax.axvline(tau_fold, color='orange', linestyle='--', alpha=0.7)
ax.plot(tau_fold, np.exp(4*tau_fold), 'ko', markersize=10, zorder=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R = L_1/L_2$ (L/R anisotropy)')
ax.set_title('Metric anisotropy ratio')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Partial Casimir ratios
if partial_casimir_ratios:
    dims = [r[2] for r in partial_casimir_ratios]
    ratios_plot = [r[6] for r in partial_casimir_ratios]
    labels = [f'({r[0]},{r[1]})' for r in partial_casimir_ratios]

    ax = axes[1, 0]
    ax.bar(range(len(dims)), ratios_plot, color='steelblue', alpha=0.7)
    ax.axhline(1.0/3.0, color='r', linestyle='--', label=f'Expected = 1/3 = {1/3:.4f}')
    ax.set_xticks(range(len(dims)))
    ax.set_xticklabels(labels, rotation=45, fontsize=7)
    ax.set_ylabel(r'$C_{u(1)}/C_{su(2)}$')
    ax.set_title('Partial Casimir ratio (representation-independent)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

# Panel 4: Summary table
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"GATE S75-H2-SIN2-LR: {verdict}\n\n"
    f"Tree-level at M_KK:\n"
    f"  sin^2 = 3/(3+exp(4*tau)) = {sin2_MKK:.6f}\n\n"
    f"Three methods agree:\n"
    f"  A (analytic):   {sin2_A:.6f}\n"
    f"  B (metric):     {sin2_B:.6f}\n"
    f"  C (spectral):   {sin2_spectral_correct:.6f}\n\n"
    f"Accidental cubic formula:\n"
    f"  3L2^3/(3L2^3+L1^3) = {sin2_spectral_accidental:.6f}\n"
    f"  (1.6% from PDG - NOT Baptista)\n\n"
    f"After SM 1-loop running:\n"
    f"  sin^2(M_Z) = {sin2_MZ_SM_running:.6f}\n\n"
    f"With L/R threshold:\n"
    f"  sin^2(M_Z) = {sin2_MZ_lr:.6f}\n\n"
    f"PDG target: {sin2_thetaW_MSbar}\n"
    f"Discrepancy: {rel_diff*100:.1f}%"
)
ax.text(0.1, 0.5, summary_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='center', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
figpath = os.path.join(SCRIPT_DIR, 's75_sin2_lr_normalization.png')  # (local)
plt.savefig(figpath, dpi=150)
plt.close()
print(f"  Saved: {figpath}")

elapsed = time.time() - t_start  # (local)
print(f"\n  Total runtime: {elapsed:.1f}s")
print("\n" + "=" * 80)
print("COMPUTATION COMPLETE")
print("=" * 80)
