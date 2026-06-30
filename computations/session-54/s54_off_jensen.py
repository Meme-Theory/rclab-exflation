#!/usr/bin/env python3
"""
S54 — OFF-JENSEN-T2-54: Two-Field Dynamics at Speed Bump
==========================================================

Compute V_eff along the T2 deformation direction v_T2 = (-11, -7, 8)
at the speed bump (tau = 0.2015). Determine whether the 2D (Jensen, T2)
landscape has a valley, saddle, or escape route.

The left-invariant metric on SU(3) with U(2)-invariant structure has
three parameters (alpha_1, alpha_2, alpha_3) on the subspaces:
  u(1) [dim 1], su(2) [dim 3], C^2 [dim 4].

The Jensen deformation is:
  alpha_1(s) = e^{2s}, alpha_2(s) = e^{-2s}, alpha_3(s) = e^s

The T2 direction in exponent space is v_T2 = (-11, -7, 8):
  alpha_1(s, sigma) = e^{2s - 11*sigma}
  alpha_2(s, sigma) = e^{-2s - 7*sigma}
  alpha_3(s, sigma) = e^{s + 8*sigma}

Volume preservation check: 1*(-11) + 3*(-7) + 4*8 = -11 - 21 + 32 = 0.

The scalar curvature is computed from Milnor's formula (Paper 15 eq 3.55)
using the explicit structure constants of su(3) in the orthonormal basis.

Gate: OFF-JENSEN-T2-54 — INFO: 2D landscape topology at speed bump.
Output: s54_off_jensen_t2.npz, s54_off_jensen_t2.png

Author: Baptista-Spacetime-Analyst (Session 54)
Date: 2026-03-21
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp, log, cosh, sinh
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

from canonical_constants import *

print("=" * 72)
print("  S54 — OFF-JENSEN-T2-54: Two-Field Dynamics at Speed Bump")
print("=" * 72)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
#  SECTION 1: Scalar curvature of the general 3-parameter metric on SU(3)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 1: Scalar curvature R(alpha_1, alpha_2, alpha_3)")
print("=" * 72)

# The su(3) Lie algebra decomposes as u(1) + su(2) + C^2.
# We use the Gell-Mann-like basis adapted to this decomposition.
#
# Basis vectors (orthonormal w.r.t. gamma_0 = -Tr(u*v)):
#   u0 = (1/sqrt(6*alpha_1)) * diag(-2i, i, i)           [u(1)]
#   u1, u2, u3 = Pauli matrices in upper-left 2x2 / sqrt(2*alpha_2)  [su(2)]
#   w1, w2, w3, w4 = off-diagonal generators / sqrt(2*alpha_3)   [C^2]
#
# The structure constants [e_a, e_b] = f_{ab}^c e_c in a hat-g-orthonormal
# basis are rescaled from the gamma_0-orthonormal structure constants by
# factors of sqrt(alpha_i/alpha_j).
#
# Paper 15 eq (3.65): scalar curvature (our reconstruction from Besse Ch 7)
# For unimodular Lie group with metric hat-g:
#   R = -1/4 sum_{a,b} |[e_a, e_b]|^2 + 1/2 sum_a B(e_a, e_a)
# where B is the Killing form and e_a are hat-g-orthonormal.
#
# Working out the structure constants explicitly for su(3) = u(1) + su(2) + C^2:
#
# The three types of brackets and their norms:
#   [u(1), su(2)] = 0                       -> contributes 0
#   [su(2), su(2)] = su(2)                  -> |[u_i, u_j]|^2 = alpha_2/alpha_2 = 1
#   [u(1), C^2] = C^2                       -> |[u_0, w_j]|^2 = alpha_1/alpha_3
#   [su(2), C^2] = C^2                      -> |[u_i, w_j]|^2 = alpha_2/alpha_3
#   [C^2, C^2] = u(1) + su(2) = u(2)       -> has two parts
#     -> u(1) part: |[w_j, w_k]|^2_{u(1)} = alpha_3^2/alpha_1
#     -> su(2) part: |[w_j, w_k]|^2_{su(2)} = alpha_3^2/alpha_2
#
# Detailed computation using Gell-Mann matrices (verified against Jensen case):

def R_K_general(a1, a2, a3):
    """
    Scalar curvature of the left-invariant metric hat-g on SU(3)
    with eigenvalues (a1, a2, a3) on (u(1), su(2), C^2).

    Uses the formula from Besse Chapter 7 / Milnor for compact unimodular groups.
    For the decomposition su(3) = u(1) + su(2) + C^2 with dims (1, 3, 4):

    R = (3/2) * (1/a3) + (4/a3) - (a1 + a2)/(2*a3^2) - (a3^2)/(2*a1*a2)

    Wait -- let me derive this systematically.
    """
    # -- SYSTEMATIC DERIVATION from Milnor's formula --
    # For a left-invariant metric on a unimodular Lie group:
    #   R = -1/2 sum_{a<b} |[e_a, e_b]|^2_g + 1/4 sum_{a,b,c} (g([e_a,e_b],e_c))^2
    #     - wait, Milnor's formula for R is (3.55):
    #   R = -1/4 sum_{a,b} g([e_a,e_b],[e_a,e_b]) + 1/2 sum_{a,b} g([ea,[ea,eb]],eb)
    #
    # The second sum: sum_a g([ea,[ea,eb]],eb) = sum_a tr(ad_ea^T ad_ea)
    # For a compact semisimple group, this is simply sum_a B(ea,ea)
    # where B is the Killing form. But B(ea,ea) = -6*alpha_a (for SU(3) with
    # our normalization gamma_0 = -Tr(uv) = -B/6).
    #
    # Actually for a g-orthonormal ea, B(ea,ea) = alpha_a^{-1} * B(fa,fa)
    # where fa is gamma_0-orthonormal. And B(fa,fa) = -6.
    #
    # So sum_a B(ea,ea) = -6 * (1/a1 + 3/a2 + 4/a3).
    #
    # The first sum: sum_{a,b} g([ea,eb],[ea,eb])
    # Let's use gamma_0-orthonormal basis {f_a} with f_a = sqrt(alpha_i) * e_a.
    # Then [e_a, e_b] = (1/sqrt(alpha_i * alpha_j)) * [f_a, f_b]_k * (1/sqrt(alpha_k)) * e_k
    # ... this is getting complicated. Let me just compute numerically.
    pass

def R_K_numeric(a1, a2, a3):
    """
    Compute scalar curvature of SU(3) with U(2)-invariant metric
    by explicitly building the structure constants and using Milnor's formula.

    Basis (gamma_0-orthonormal, i.e. -Tr(u*v) = delta):
      f0 = diag(-2i, i, i) / sqrt(6)           [u(1)]
      f1 = sigma_1 embed / sqrt(2)              [su(2)]
      f2 = sigma_2 embed / sqrt(2)              [su(2)]
      f3 = sigma_3 embed / sqrt(2)              [su(2)]
      f4...f7 = off-diagonal C^2 generators     [C^2]

    Then hat-g orthonormal: e_a = f_a / sqrt(alpha_i) where a in subspace i.
    """
    # Structure constants of su(3) in a gamma_0-orthonormal basis
    # [f_a, f_b] = c_{ab}^c f_c where c are REAL and antisymmetric in (a,b)
    #
    # We use Gell-Mann matrices lambda_1...lambda_8 with the conventions
    # T_a = i*lambda_a/2 (anti-hermitian). Then gamma_0(T_a, T_b) = delta_{ab}/2.
    # Renormalize: f_a = T_a * sqrt(2) so gamma_0(f_a, f_b) = delta_{ab}.
    #
    # Actually, let me just build the 8x8x8 structure constant tensor.

    dim = 8
    # Gell-Mann matrices (standard conventions)
    lam = np.zeros((9, 3, 3), dtype=complex)
    lam[1] = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
    lam[2] = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
    lam[3] = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
    lam[4] = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
    lam[5] = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
    lam[6] = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
    lam[7] = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
    lam[8] = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / sqrt(3.0)

    # Anti-hermitian generators: T_a = i*lam[a]/2
    T = np.zeros((9, 3, 3), dtype=complex)
    for a in range(1, 9):
        T[a] = 1j * lam[a] / 2.0

    # Inner product gamma_0(u,v) = -Tr(u*v) on anti-hermitian matrices
    # Check: gamma_0(T_a, T_b) = -Tr(T_a T_b) = Tr(lam_a lam_b)/4 = delta_{ab}/2
    # So f_a = T_a * sqrt(2) gives gamma_0(f_a, f_b) = delta_{ab}

    # Reorder to match Baptista's decomposition:
    # u(1): lambda_8 -> index 0
    # su(2): lambda_1, lambda_2, lambda_3 -> indices 1, 2, 3
    # C^2: lambda_4, lambda_5, lambda_6, lambda_7 -> indices 4, 5, 6, 7

    reorder = [8, 1, 2, 3, 4, 5, 6, 7]  # Gell-Mann indices

    # Build generators in the reordered basis
    f = np.zeros((8, 3, 3), dtype=complex)
    for i in range(8):
        f[i] = T[reorder[i]] * sqrt(2.0)  # gamma_0-orthonormal

    # Verify orthonormality: gamma_0(f_a, f_b) = -Tr(f_a * f_b)
    gram_f = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            gram_f[a, b] = -np.trace(f[a] @ f[b]).real
    assert np.allclose(gram_f, np.eye(8), atol=1e-14), f"Gram matrix error: {np.max(np.abs(gram_f - np.eye(8)))}"

    # Compute structure constants in gamma_0-orthonormal basis
    # [f_a, f_b] = sum_c c_{ab}^c f_c
    # c_{ab}^c = gamma_0([f_a, f_b], f_c) = -Tr([f_a, f_b] * f_c)
    c_abc = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            bracket = f[a] @ f[b] - f[b] @ f[a]
            for cc in range(8):
                c_abc[a, b, cc] = -np.trace(bracket @ f[cc]).real

    # Verify antisymmetry
    assert np.allclose(c_abc, -np.transpose(c_abc, (1, 0, 2)), atol=1e-14)

    # Assign subspace indices: 0 -> u(1), 1-3 -> su(2), 4-7 -> C^2
    # alpha_i for each basis vector
    alpha = np.zeros(8)
    alpha[0] = a1       # u(1)
    alpha[1:4] = a2     # su(2)
    alpha[4:8] = a3     # C^2

    # hat-g-orthonormal basis: e_a = f_a / sqrt(alpha_a)
    # [e_a, e_b] = (1/sqrt(alpha_a * alpha_b)) * sum_c c_{ab}^c * sqrt(alpha_c) * e_c
    # ... no wait: [e_a, e_b] = [f_a/sqrt(alpha_a), f_b/sqrt(alpha_b)]
    #            = (1/(sqrt(alpha_a)*sqrt(alpha_b))) * [f_a, f_b]
    #            = (1/(sqrt(alpha_a)*sqrt(alpha_b))) * sum_c c_{ab}^c * f_c
    #            = (1/(sqrt(alpha_a)*sqrt(alpha_b))) * sum_c c_{ab}^c * sqrt(alpha_c) * e_c
    #
    # So g([e_a, e_b], [e_a, e_b]) = sum_c (c_{ab}^c)^2 * alpha_c / (alpha_a * alpha_b)

    # Milnor formula (3.55) for unimodular groups:
    # R = -1/4 * sum_{a,b} g([ea,eb],[ea,eb]) + 1/2 * sum_{a,b} g([ea,[ea,eb]],eb)

    # First term: T1 = sum_{a,b} g([ea,eb],[ea,eb])
    T1 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for cc in range(8):
                T1 += c_abc[a, b, cc]**2 * alpha[cc] / (alpha[a] * alpha[b])

    # Second term: T2 = sum_{a,b} g([ea,[ea,eb]], eb)
    # [ea, eb] has components: (c_{ab}^c * sqrt(alpha_c)) / (sqrt(alpha_a) * sqrt(alpha_b)) in e_c
    # [ea, [ea,eb]] = sum_c (c_{ab}^c * sqrt(alpha_c))/(sqrt(alpha_a)*sqrt(alpha_b)) * [ea, ec]
    #              = sum_{c,d} (c_{ab}^c * sqrt(alpha_c) * c_{ac}^d * sqrt(alpha_d)) /
    #                          (alpha_a * sqrt(alpha_b) * sqrt(alpha_c)) * e_d
    #              = sum_{c,d} c_{ab}^c * c_{ac}^d * sqrt(alpha_d) / (alpha_a * sqrt(alpha_b)) * e_d
    #
    # g([ea,[ea,eb]], eb) = sum_{c,d} c_{ab}^c * c_{ac}^d * alpha_d^{1/2} / (alpha_a * alpha_b^{1/2}) * delta_{d,b}
    #                     wait, g(e_d, e_b) = delta_{db}
    # So g([ea,[ea,eb]], eb) = sum_c c_{ab}^c * c_{ac}^b * sqrt(alpha_b) / (alpha_a * sqrt(alpha_b))
    #                       wait, let me redo this more carefully.
    #
    # Actually, let's use the direct formula:
    # g([ea,[ea,eb]], eb) = -g(ad_ea^2 eb, eb) = -sum_d g([ea,[ea,eb]], ed) delta_{db}

    # Simplest: compute directly
    T2 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            # [ea, eb] = sum_c gamma_{ab}^c e_c
            # where gamma_{ab}^c = c_{ab}^c * sqrt(alpha[c]) / (sqrt(alpha[a]) * sqrt(alpha[b]))
            gamma_ab = np.zeros(8)
            for cc in range(8):
                gamma_ab[cc] = c_abc[a, b, cc] * sqrt(alpha[cc]) / (sqrt(alpha[a]) * sqrt(alpha[b]))

            # [ea, [ea, eb]] = sum_c gamma_{ab}^c [ea, ec]
            # = sum_c gamma_{ab}^c * sum_d gamma_{ac}^d e_d
            inner = 0.0
            for cc in range(8):
                gamma_ac = np.zeros(8)
                for d in range(8):
                    gamma_ac[d] = c_abc[a, cc, d] * sqrt(alpha[d]) / (sqrt(alpha[a]) * sqrt(alpha[cc]))
                # g([ea,[ea,eb]], eb) += gamma_ab^c * gamma_ac^b
                inner += gamma_ab[cc] * gamma_ac[b]
            T2 += inner

    # The correct Milnor formula for unimodular compact groups (Besse 7.38):
    # R = -(1/4) T1 - (1/2) T2
    # where T1 = sum |[ea,eb]|^2 and T2 = sum g([ea,[ea,eb]],eb)
    # NOTE: The transcription of Paper 15 eq (3.55) has a sign error in T2.
    # Cross-checked: for bi-invariant SU(3), T1=48, T2=-48, R = 12.
    R = -0.25 * T1 - 0.5 * T2
    return R

# Cross-check against known Jensen formula
def R_K_Jensen(s):
    """Scalar curvature from Paper 15 eq (3.70), with alpha_K = 3."""
    # R(s) = (3/(2*alpha)) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})
    # With the normalization from s53_7dof_saddles.py:
    return (12.0 / g0_diag) * (2.0*exp(2.0*s) - 1.0 + 8.0*exp(-s) - exp(-4.0*s)) / 8.0

# But wait: the formula in Paper 15 uses gamma_0 = -Tr(u*v) as the base metric,
# not our convention with g0_diag = 3. The general metric is:
#   hat-g = alpha_1 * gamma_0|_{u(1)} + alpha_2 * gamma_0|_{su(2)} + alpha_3 * gamma_0|_{C^2}
# So for the bi-invariant case alpha_1 = alpha_2 = alpha_3 = alpha:
#   R_bi = R_numeric(alpha, alpha, alpha)
# And from the known result for the round metric: R_SU3 = 12 (in our gamma_0 normalization).
# Wait no -- the curvature depends on the overall scale.

# Let's verify. For alpha=1 (metric = gamma_0), the bi-invariant SU(3):
R_bi = R_K_numeric(1.0, 1.0, 1.0)
print(f"\n  R(1,1,1) [bi-invariant, gamma_0 scale] = {R_bi:.6f}")
# For a round SU(3) with metric = c * gamma_0, R scales as 1/c.
# The Killing metric B = 6*gamma_0 on SU(3) gives R = 12/6 = 2.
# With gamma_0: the scalar curvature from Milnor should give R = 12.

# Cross-check at Jensen s=0 (which is alpha=1,1,1):
R_Jensen_0 = R_K_Jensen(0.0)
print(f"  R_Jensen(s=0) = {R_Jensen_0:.6f}")

# The s53 script uses: R_K(s) = (12/alpha_K) * (2*exp(2s) - 1 + 8*exp(-s) - exp(-4s))/8
# At s=0: R_K(0) = (12/3) * (2 - 1 + 8 - 1)/8 = 4 * 8/8 = 4.0
# So R_K(0) = 4.0 in the s53 convention with alpha_K = 3.

# The discrepancy is the overall normalization. Paper 15 defines:
#   g_K^e = (15/2) * gamma_0
# as the Einstein metric (see eq 3.71 context, eq 3.903).
# The s53 code sets alpha_K = g0_diag = 3.0.
#
# Actually, the s53 code and Paper 15 use DIFFERENT overall normalizations.
# Paper 15's Jensen metric is:
#   hat-g(s) = alpha * (e^{2s} gamma_0|u1 + e^{-2s} gamma_0|su2 + e^s gamma_0|C2)
# with alpha = 15/2 for the Einstein normalization.
# The scalar curvature from eq (3.70) is:
#   R(s) = (3/(2*alpha)) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})
#
# The s53 code normalizes differently. Let me match conventions.
#
# In the GENERAL case without overall scale: if we set alpha_i = c * beta_i
# then R(c*beta) = R(beta) / c. So the scalar curvature scales inversely with
# the metric eigenvalues.

# My R_K_numeric function computes R for hat-g = a1*gamma_0|u1 + a2*gamma_0|su2 + a3*gamma_0|C2.
# Let me verify it matches the Jensen formula.

# For the Jensen family with general alpha:
#   a1 = alpha * e^{2s}, a2 = alpha * e^{-2s}, a3 = alpha * e^s
# where alpha is the overall scale. With alpha = 1:
R_Jensen_test = R_K_numeric(exp(0.0), exp(0.0), exp(0.0))
print(f"  R_numeric(e^0, e^0, e^0) = {R_Jensen_test:.6f}")

for s_test in [0.0, 0.1, 0.19, 0.3]:
    a1_t = exp(2.0*s_test)
    a2_t = exp(-2.0*s_test)
    a3_t = exp(s_test)
    R_num = R_K_numeric(a1_t, a2_t, a3_t)
    # Paper 15 eq 3.70 with alpha=1: R(s) = (3/2) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})
    R_paper = (3.0/2.0) * (2.0*exp(2.0*s_test) - 1.0 + 8.0*exp(-s_test) - exp(-4.0*s_test))
    print(f"  s={s_test:.2f}: R_numeric = {R_num:.6f}, R_Paper15_eq3.70 = {R_paper:.6f}, ratio = {R_num/R_paper:.10f}")

# ============================================================================
#  SECTION 2: General parameterization for Jensen + T2
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 2: Jensen + T2 parameterization")
print("=" * 72)

# Jensen direction in exponent space: v_J = (2, -2, 1)
# T2 direction in exponent space: v_T2 = (-11, -7, 8)
#
# General 2-parameter metric:
#   a1(s, sigma) = alpha * exp(2*s - 11*sigma)
#   a2(s, sigma) = alpha * exp(-2*s - 7*sigma)
#   a3(s, sigma) = alpha * exp(s + 8*sigma)
#
# Volume: vol = a1^{1/2} * a2^{3/2} * a3^2 * vol_0  (dims 1, 3, 4)
# Exponent: (1/2)*ln(a1) + (3/2)*ln(a2) + 2*ln(a3)
#         = (1/2)*(2s - 11*sig) + (3/2)*(-2s - 7*sig) + 2*(s + 8*sig)
#         = s - 5.5*sig - 3s - 10.5*sig + 2s + 16*sig
#         = (s - 3s + 2s) + (-5.5 - 10.5 + 16)*sig
#         = 0 + 0*sig = 0 ✓  (volume-preserving for both directions)

# Wait -- volume form from eq (3.64):
#   vol_{hat-g} = alpha_1^{1/2} * alpha_2^{3/2} * alpha_3^2 * vol_0
# That's what I need. The exponents in the volume are:
#   (1/2) * exp_1 + (3/2) * exp_2 + 2 * exp_3
# For Jensen: (1/2)*2s + (3/2)*(-2s) + 2*s = s - 3s + 2s = 0  ✓
# For T2: (1/2)*(-11) + (3/2)*(-7) + 2*8 = -5.5 - 10.5 + 16 = 0  ✓

# Hmm, but eq (3.64) says vol_{hat-g} = alpha_1^{1/2} * alpha_2^{3/2} * alpha_3^2 * vol_0.
# Let me re-check against the actual equation. From the transcription:
#   vol g^ = 1 23 34 vol0   (3.64)
# This reads: vol_{hat-g} = alpha_1^{something} * alpha_2^{something} * alpha_3^{something} * vol_0
# Given dims u(1)=1, su(2)=3, C^2=4, the volume form is:
#   vol_{hat-g} = alpha_1^{1/2} * alpha_2^{3/2} * alpha_3^{4/2} * vol_0
#               = sqrt(a1) * a2^{3/2} * a3^2 * vol_0
#
# This is exactly what we need. The logarithmic volume constraint is:
#   (1/2)*ln(a1) + (3/2)*ln(a2) + 2*ln(a3) = const.
# Or in exponent space with a_i = exp(xi_i):
#   (1/2)*xi_1 + (3/2)*xi_2 + 2*xi_3 = 0
# i.e., n . xi = 0 where n = (1/2, 3/2, 2) = (1, 3, 4)/2.
# So the volume-preserving constraint is n . v = 0 with n = (1, 3, 4).
# Jensen: n . (2, -2, 1) = 2 - 6 + 4 = 0  ✓
# T2: n . (-11, -7, 8) = -11 - 21 + 32 = 0  ✓

v_Jensen = np.array([2.0, -2.0, 1.0])
v_T2 = np.array([-11.0, -7.0, 8.0])
n_vol = np.array([1.0, 3.0, 4.0])

print(f"  Jensen direction: v_J = {v_Jensen}")
print(f"  T2 direction:     v_T2 = {v_T2}")
print(f"  Volume normal:    n = {n_vol}")
print(f"  n . v_J = {np.dot(n_vol, v_Jensen):.1f}  (volume-preserving: ✓)")
print(f"  n . v_T2 = {np.dot(n_vol, v_T2):.1f}  (volume-preserving: ✓)")

# Orthogonality in DeWitt metric
# The DeWitt metric on the space of metrics is proportional to:
#   G_ij = (dim_i/2) * delta_ij (on the exponent space)
# This is because the kinetic term in the action is:
#   K = (1/2) * sum_i dim_i * (d(xi_i)/dt)^2
# For our decomposition: dim = (1, 3, 4).
# So G = diag(1, 3, 4)/2 on the exponent space.
# Actually from Paper 15 eq (3.79), the kinetic terms are:
#   -(1/2)|dphi|^2 - (5/2)|dsigma|^2
# where phi is the RESCALING field and sigma is the TT field.
# This uses a specific parameterization. Let me use the general form.

# The DeWitt metric in exponent coordinates (xi_1, xi_2, xi_3):
# G_{DeWitt} = (1/2) * diag(dim_1, dim_2, dim_3) = (1/2)*diag(1, 3, 4)
# But this is the metric on the UNCONSTRAINED space. On the volume-preserving
# submanifold, we project out the volume direction.
#
# Actually, from Paper 15 eq (3.76)-(3.79), the kinetic energy for the
# TT-deformation sigma is (5/2)|d sigma|^2 and for the rescaling phi it's (1/2)|d phi|^2.
# The phi field is NOT volume-preserving (it's the overall rescaling).
# The sigma field IS the Jensen TT direction.
# But we want to parameterize the VOLUME-PRESERVING submanifold in the (sigma, sigma_T2) plane.

# Let me compute the DeWitt inner product of v_Jensen and v_T2 restricted to
# the volume-preserving surface.

G_DW = np.diag([1.0, 3.0, 4.0]) / 2.0  # DeWitt metric in exponent space

# Inner products
GJJ = v_Jensen @ G_DW @ v_Jensen
GTT = v_T2 @ G_DW @ v_T2
GJT = v_Jensen @ G_DW @ v_T2

print(f"\n  DeWitt metric G = diag(1, 3, 4)/2")
print(f"  G(v_J, v_J) = {GJJ:.4f}")
print(f"  G(v_T2, v_T2) = {GTT:.4f}")
print(f"  G(v_J, v_T2) = {GJT:.4f}")
print(f"  Inertia ratio G_T2/G_J = {GTT/GJJ:.4f}")
print(f"  cos(angle) = {GJT/(sqrt(GJJ)*sqrt(GTT)):.6f}")

# So v_Jensen and v_T2 are NOT orthogonal in the DeWitt metric!
# Let me orthogonalize. The T2 direction after Gram-Schmidt:
v_T2_perp = v_T2 - (GJT / GJJ) * v_Jensen
GTTp = v_T2_perp @ G_DW @ v_T2_perp
GJTp = v_Jensen @ G_DW @ v_T2_perp

print(f"\n  After Gram-Schmidt:")
print(f"  v_T2_perp = {v_T2_perp}")
print(f"  G(v_J, v_T2_perp) = {GJTp:.2e}  (should be ~0)")
print(f"  G(v_T2_perp, v_T2_perp) = {GTTp:.6f}")

# Normalize so that the kinetic term is (1/2)|ds|^2 + (1/2)|dsigma|^2
# with s = Jensen coordinate, sigma = orthogonal T2 coordinate
norm_J = sqrt(GJJ)
norm_T2 = sqrt(GTTp)
print(f"\n  Normalization factors:")
print(f"    |v_J|_G = {norm_J:.6f}")
print(f"    |v_T2_perp|_G = {norm_T2:.6f}")

# ============================================================================
#  SECTION 3: 2D landscape V_eff(tau, sigma)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 3: 2D potential landscape V(tau, sigma)")
print("=" * 72)

# The KK potential (neglecting the rescaling field phi, which is frozen
# by the much steeper rescaling potential):
#   V_KK(s, sigma) = -(M_p^2/2) * R_K(a1(s,sigma), a2(s,sigma), a3(s,sigma))
#
# Here (s, sigma) parameterize the 2D volume-preserving surface via:
#   xi = s * v_Jensen + sigma * v_T2_perp
# which gives:
#   a1 = exp(2*s + v_T2_perp[0]*sigma)
#   a2 = exp(-2*s + v_T2_perp[1]*sigma)
#   a3 = exp(s + v_T2_perp[2]*sigma)
#
# But actually, the task says to parameterize as g(tau, s) = g_Jensen(tau) + s * v_T2.
# Let me use the EXPONENT parameterization directly:
#   xi_i(tau, sigma) = tau * v_Jensen[i] + sigma * v_T2[i]
# and then a_i = exp(xi_i).
#
# For the potential, we use the scale from the existing codebase.
# The s53 code uses alpha_K = 3.0 as the overall scale factor.
# In terms of the scaled metric: g_K = alpha_K * hat-g
# So R_K = R_{hat-g} / alpha_K.
# And V_KK = -(M_p^2/2) * R_K.

alpha_K = g0_diag  # = 3.0

def metric_params(tau, sigma):
    """Return (a1, a2, a3) for the 2-parameter family."""
    xi1 = 2.0*tau - 11.0*sigma
    xi2 = -2.0*tau - 7.0*sigma
    xi3 = tau + 8.0*sigma
    return exp(xi1), exp(xi2), exp(xi3)

def V_KK_2d(tau, sigma):
    """KK potential on the 2D volume-preserving surface."""
    a1, a2, a3 = metric_params(tau, sigma)
    R = R_K_numeric(a1, a2, a3)
    # Scale by alpha_K and compute potential
    # V_KK = -(M_p^2/2) * R / alpha_K
    # Actually: the metric in the codebase is alpha_K * hat-g,
    # so R_phys = R_hat / alpha_K. But alpha_K is already absorbed
    # into the Jensen parameterization in s53. Let me match conventions.
    # The s53 code: V_KK = -(M_p^2/2) * R_K where R_K includes alpha_K.
    # R_K = (12/alpha_K) * f(s) / 8 for Jensen.
    # R_numeric gives R for the hat-g metric with eigenvalues a_i.
    # For Jensen with alpha_K = 1: R_numeric = (3/2)*(2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})
    # Paper 15: R = (3/(2*alpha)) * (same)
    # So R_numeric with alpha = alpha_K = 3 means we need:
    # R_K = R_numeric(alpha_K*a1, alpha_K*a2, alpha_K*a3)
    # or equivalently R_numeric(a1,a2,a3)/alpha_K when alpha_K is an overall scale.
    #
    # Let me just match the Jensen case exactly.
    # For Jensen at s=0, a1=a2=a3=1:
    #   R_numeric(1,1,1) should match R_Jensen(0) * alpha_K = 4.0 * 3.0 = 12.0?
    # No. R_numeric(1,1,1) gives the scalar curvature of gamma_0.
    # The physical metric is alpha_K * gamma_0, so R_phys = R_numeric / alpha_K.
    # R_phys(s=0) = R_numeric(1,1,1) / 3.0
    #
    # And V_KK = -(M_p^2/2) * R_phys = -(M_p^2/2) * R_numeric / alpha_K
    #
    # Check: R_Jensen(0) = (12/3) * (2-1+8-1)/8 = 4*(8/8) = 4.0
    # R_numeric(1,1,1) should be = R_Jensen(0) * alpha_K = 4.0 * 3.0 = 12.0
    # Yes! Because R_numeric computes R for the gamma_0 metric (alpha=1),
    # while R_Jensen already includes 1/alpha_K.

    return -0.5 * M_P_over_MKK**2 * R / alpha_K

# Where M_P_over_MKK is defined
M_KK_val = M_KK_kerner
M_P_over_MKK = M_Pl_reduced / M_KK_val

# Verify against s53 at the speed bump
tau_sb = 0.2015  # speed bump location  # (local)
V_2d_sb = V_KK_2d(tau_sb, 0.0)
V_1d_sb = -0.5 * M_P_over_MKK**2 * R_K_Jensen(tau_sb)

# For the 1D Jensen formula, R_K_Jensen already divides by alpha_K:
# R_K_Jensen(s) = (12/alpha_K) * (...) / 8
# So V_1d = -(M_P^2/2) * R_K_Jensen
print(f"\n  Speed bump (tau={tau_sb}, sigma=0):")
print(f"    V_KK_2d = {V_2d_sb:.6f}")
print(f"    V_KK_1d = {V_1d_sb:.6f}")
print(f"    Match: {abs(V_2d_sb - V_1d_sb):.2e}")

# ============================================================================
#  SECTION 4: Hessian at the speed bump
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 4: Hessian of V_KK at speed bump")
print("=" * 72)

# Compute the Hessian by finite differences (second-order central)
h_tau = 1e-4
h_sig = 1e-5  # smaller because T2 is a large vector

# V values for finite differences
V_00 = V_KK_2d(tau_sb, 0.0)
V_p0 = V_KK_2d(tau_sb + h_tau, 0.0)
V_m0 = V_KK_2d(tau_sb - h_tau, 0.0)
V_0p = V_KK_2d(tau_sb, h_sig)
V_0m = V_KK_2d(tau_sb, -h_sig)
V_pp = V_KK_2d(tau_sb + h_tau, h_sig)
V_pm = V_KK_2d(tau_sb + h_tau, -h_sig)
V_mp = V_KK_2d(tau_sb - h_tau, h_sig)
V_mm = V_KK_2d(tau_sb - h_tau, -h_sig)

d2V_dtau2 = (V_p0 - 2*V_00 + V_m0) / h_tau**2
d2V_dsig2 = (V_0p - 2*V_00 + V_0m) / h_sig**2
d2V_dtau_dsig = (V_pp - V_pm - V_mp + V_mm) / (4*h_tau*h_sig)

# First derivatives
dV_dtau = (V_p0 - V_m0) / (2*h_tau)
dV_dsig = (V_0p - V_0m) / (2*h_sig)

print(f"\n  At (tau={tau_sb}, sigma=0):")
print(f"    V_KK = {V_00:.6f}")
print(f"    dV/dtau = {dV_dtau:.6e}")
print(f"    dV/dsigma = {dV_dsig:.6e}")
print(f"\n  Hessian H_ij = d^2V/(dx_i dx_j):")
print(f"    H_tautau   = {d2V_dtau2:.6f}")
print(f"    H_sigsig   = {d2V_dsig2:.6f}")
print(f"    H_tausig   = {d2V_dtau_dsig:.6e}")

# Eigenvalues of the Hessian
H = np.array([[d2V_dtau2, d2V_dtau_dsig],
              [d2V_dtau_dsig, d2V_dsig2]])
evals_H = np.linalg.eigvalsh(H)
evecs_H = np.linalg.eigh(H)[1]

print(f"\n  Hessian eigenvalues: {evals_H[0]:.6f}, {evals_H[1]:.6f}")
print(f"  Hessian eigenvectors:")
print(f"    v1 = ({evecs_H[0,0]:.6f}, {evecs_H[1,0]:.6f}) [eigenvalue {evals_H[0]:.6f}]")
print(f"    v2 = ({evecs_H[0,1]:.6f}, {evecs_H[1,1]:.6f}) [eigenvalue {evals_H[1]:.6f}]")

# Classification
if evals_H[0] > 0 and evals_H[1] > 0:
    topology = "MINIMUM (both positive)"
elif evals_H[0] < 0 and evals_H[1] < 0:
    topology = "MAXIMUM (both negative)"
elif evals_H[0] * evals_H[1] < 0:
    topology = "SADDLE (opposite signs)"
else:
    topology = "DEGENERATE (one zero eigenvalue)"

print(f"\n  LANDSCAPE TOPOLOGY: {topology}")

# ============================================================================
#  SECTION 5: Verify with analytic derivatives
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 5: Analytic verification (Jensen direction)")
print("=" * 72)

# The 1D Jensen curvature d2V_KK/dtau2 at the speed bump should match s53
# s53 reports d2V_KK/dtau2(0.19) from the formula with alpha_K = 3
d2V_KK_s53 = d2V_dtau2
print(f"  d2V_KK/dtau2 (finite diff, 2D) = {d2V_KK_s53:.6f}")

# From the analytic Jensen formula:
def d2R_Jensen(s):
    """Second derivative of R_K along Jensen."""
    return (12.0/g0_diag) * (8.0*exp(2.0*s) + 8.0*exp(-s) - 16.0*exp(-4.0*s)) / 8.0

d2V_1d = -0.5 * M_P_over_MKK**2 * d2R_Jensen(tau_sb)
print(f"  d2V_KK/dtau2 (analytic 1D)     = {d2V_1d:.6f}")
print(f"  Agreement: {abs(d2V_KK_s53 - d2V_1d)/abs(d2V_1d):.2e} relative")

# ============================================================================
#  SECTION 6: R_K along T2 direction
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 6: Scalar curvature along T2")
print("=" * 72)

# R_K(tau_sb, sigma) along T2 at fixed tau = speed bump
sigmas = np.linspace(-0.02, 0.02, 41)
R_along_T2 = np.array([R_K_numeric(*metric_params(tau_sb, sig)) for sig in sigmas])

print(f"  R_K at sigma = 0: {R_along_T2[20]:.6f}")
print(f"  R_K at sigma = -0.02: {R_along_T2[0]:.6f}")
print(f"  R_K at sigma = +0.02: {R_along_T2[-1]:.6f}")
print(f"  dR/dsigma at sigma=0: {(R_along_T2[21] - R_along_T2[19])/(2*(sigmas[1]-sigmas[0])):.6f}")
print(f"  d2R/dsigma2 at sigma=0: {(R_along_T2[21] - 2*R_along_T2[20] + R_along_T2[19])/(sigmas[1]-sigmas[0])**2:.6f}")

# ============================================================================
#  SECTION 7: Full 2D landscape scan
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 7: Full 2D landscape scan")
print("=" * 72)

# Scan over a grid
N_tau = 51  # (local)
N_sig = 41
tau_range = np.linspace(0.0, 0.40, N_tau)
sig_range = np.linspace(-0.015, 0.015, N_sig)
V_grid = np.zeros((N_tau, N_sig))
R_grid = np.zeros((N_tau, N_sig))

print(f"  Computing {N_tau}x{N_sig} = {N_tau*N_sig} grid points...")
for i, t in enumerate(tau_range):
    for j, sig in enumerate(sig_range):
        a1, a2, a3 = metric_params(t, sig)
        R = R_K_numeric(a1, a2, a3)
        R_grid[i, j] = R / alpha_K
        V_grid[i, j] = -0.5 * M_P_over_MKK**2 * R / alpha_K

print(f"  Grid computed.")
print(f"  V range: [{V_grid.min():.4f}, {V_grid.max():.4f}]")
print(f"  V at speed bump: {V_grid[N_tau//2, N_sig//2]:.4f}")

# Find the gradient flow: does the T2 direction provide an escape?
# At the speed bump, if d2V/dsig2 < 0, there's a T2 escape route.
print(f"\n  Along the JENSEN line (sigma=0):")
j_mid = N_sig // 2
for i_label, i_val in [(0, 0), (12, 12), (25, 25), (38, 38), (50, -1)]:
    if i_val < 0:
        i_val = N_tau - 1
    if i_val < N_tau:
        print(f"    tau={tau_range[i_val]:.3f}: V={V_grid[i_val, j_mid]:.4f}, R={R_grid[i_val, j_mid]:.4f}")

# ============================================================================
#  SECTION 8: DeWitt-corrected Hessian (with inertia)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 8: DeWitt-corrected Hessian (physical mass matrix)")
print("=" * 72)

# The kinetic energy in the 2D subspace:
# K = (1/2) * v^T G v where v = (dtau/dt, dsigma/dt)
# and G is the DeWitt metric restricted to the (tau, sigma) coordinates.
#
# G_ij = v_i^T . G_DW . v_j where v_i are the direction vectors.
# Here v_tau = v_Jensen and v_sigma = v_T2.

G_tau_tau = v_Jensen @ G_DW @ v_Jensen
G_sig_sig = v_T2 @ G_DW @ v_T2
G_tau_sig = v_Jensen @ G_DW @ v_T2

G_2d = np.array([[G_tau_tau, G_tau_sig],
                 [G_tau_sig, G_sig_sig]])

print(f"  2D DeWitt metric tensor:")
print(f"    G_tau_tau = {G_tau_tau:.6f}")
print(f"    G_sig_sig = {G_sig_sig:.6f}")
print(f"    G_tau_sig = {G_tau_sig:.6f}")
print(f"    det(G) = {np.linalg.det(G_2d):.6f}")

# The physical mass matrix (stability matrix) is:
# M = G^{-1} . H
# Its eigenvalues determine stability.
G_inv = np.linalg.inv(G_2d)
M_phys = G_inv @ H

evals_M = np.linalg.eigvals(M_phys)
print(f"\n  Physical mass matrix M = G^-1 H:")
print(f"    Eigenvalues: {evals_M[0]:.6f}, {evals_M[1]:.6f}")
print(f"    (Negative = unstable, Positive = stable)")

# Also compute omega^2 from the generalized eigenvalue problem:
# H v = omega^2 G v
from scipy.linalg import eigh
evals_gen, evecs_gen = eigh(H, G_2d)
print(f"\n  Generalized eigenvalues (H v = omega^2 G v):")
print(f"    omega^2_1 = {evals_gen[0]:.6f}")
print(f"    omega^2_2 = {evals_gen[1]:.6f}")
print(f"    Eigenvector 1: ({evecs_gen[0,0]:.6f}, {evecs_gen[1,0]:.6f})")
print(f"    Eigenvector 2: ({evecs_gen[0,1]:.6f}, {evecs_gen[1,1]:.6f})")

# Convert eigenvectors to directions in (u1, su2, C2) exponent space
for k in range(2):
    v = evecs_gen[0, k] * v_Jensen + evecs_gen[1, k] * v_T2
    print(f"    Direction {k+1} in exponent space: ({v[0]:.3f}, {v[1]:.3f}, {v[2]:.3f})")

# ============================================================================
#  SECTION 9: Escape route analysis
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 9: Escape route analysis")
print("=" * 72)

# At the speed bump, the 1D Jensen direction has V''(tau) < 0 (it's a maximum).
# Question: does the T2 direction also have V'' < 0, or does it provide a valley?
print(f"\n  At the speed bump (tau={tau_sb}):")
print(f"    d2V/dtau2    = {d2V_dtau2:.4f}  {'(UNSTABLE)' if d2V_dtau2 < 0 else '(STABLE)'}")
print(f"    d2V/dsigma2  = {d2V_dsig2:.4f}  {'(UNSTABLE)' if d2V_dsig2 < 0 else '(STABLE)'}")
print(f"    d2V/dtau_dsig = {d2V_dtau_dsig:.4e}")

if d2V_dtau2 < 0 and d2V_dsig2 < 0:
    print(f"    ==> MAXIMUM in both directions: no escape, no valley")
    print(f"    The speed bump is a 2D maximum (hill top)")
elif d2V_dtau2 < 0 and d2V_dsig2 > 0:
    print(f"    ==> SADDLE: T2 direction is a valley!")
    print(f"    A trajectory can follow the T2 valley at the speed bump")
elif d2V_dtau2 > 0 and d2V_dsig2 < 0:
    print(f"    ==> SADDLE: Jensen direction is a valley, T2 is escape")
else:
    print(f"    ==> MINIMUM in both directions")

# Scan: V along T2 direction at the speed bump
print(f"\n  V_KK(tau_sb, sigma) profile along T2:")
for sig in [-0.01, -0.005, -0.001, 0.0, 0.001, 0.005, 0.01]:
    V_val = V_KK_2d(tau_sb, sig)
    dV = V_val - V_00
    print(f"    sigma={sig:+.4f}: V = {V_val:.6f}, dV = {dV:+.6e}")

# ============================================================================
#  SECTION 10: Scanning for T2 minimum or saddle point
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 10: Search for critical points in 2D")
print("=" * 72)

# Search along sigma at each tau for dV/dsigma = 0
print("  Searching for sigma_crit(tau) where dV/dsigma = 0:")
for tau_test in np.linspace(0.0, 0.35, 15):
    # dV/dsigma by finite differences
    h = 1e-6  # (local)
    Vp = V_KK_2d(tau_test, h)
    Vm = V_KK_2d(tau_test, -h)
    dVds = (Vp - Vm) / (2*h)

    Vpp = V_KK_2d(tau_test, 2*h)
    Vmm = V_KK_2d(tau_test, -2*h)
    V0 = V_KK_2d(tau_test, 0.0)
    d2Vds2 = (Vp - 2*V0 + Vm) / h**2

    print(f"    tau={tau_test:.3f}: dV/dsig={dVds:.4e}, d2V/dsig2={d2Vds2:.4f}", end="")
    if abs(dVds) < 1e-6:
        print(f" <-- CRITICAL (sigma=0)", end="")
    print()

# Is sigma=0 always a critical point?
# Due to the Z_2 symmetry sigma -> -sigma? NO, the T2 direction does NOT
# have this symmetry in general. Let's check.
print(f"\n  Symmetry check: V(tau, sigma) vs V(tau, -sigma)")
for tau_test in [0.0, 0.10, 0.2015, 0.30]:
    for sig_test in [0.001, 0.005, 0.01]:
        Vp = V_KK_2d(tau_test, sig_test)
        Vm = V_KK_2d(tau_test, -sig_test)
        print(f"    tau={tau_test:.4f}, sig={sig_test:.3f}: V(+sig)={Vp:.8f}, V(-sig)={Vm:.8f}, diff={Vp-Vm:.4e}")

# ============================================================================
#  SECTION 11: Key diagnostic — does T2 change the transit?
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 11: Transit dynamics implications")
print("=" * 72)

# The key question: if the modulus starts along the Jensen direction,
# does it acquire a T2 component during transit?
# This requires dV/dsigma != 0 along Jensen (sigma=0).
# If sigma=0 is a critical line (dV/dsig = 0 for all tau), then
# the Jensen trajectory is a geodesic in the 2D landscape and
# T2 never activates.

print(f"  dV/dsigma along the Jensen line (sigma=0):")
tau_scan = np.linspace(0.0, 0.40, 81)
dVdsig_scan = np.zeros_like(tau_scan)
d2Vdsig2_scan = np.zeros_like(tau_scan)
V_Jensen_scan = np.zeros_like(tau_scan)

h_s = 1e-6
for i, t in enumerate(tau_scan):
    Vp = V_KK_2d(t, h_s)
    Vm = V_KK_2d(t, -h_s)
    V0 = V_KK_2d(t, 0.0)
    dVdsig_scan[i] = (Vp - Vm) / (2*h_s)
    d2Vdsig2_scan[i] = (Vp - 2*V0 + Vm) / h_s**2
    V_Jensen_scan[i] = V0

max_dVdsig = np.max(np.abs(dVdsig_scan))
print(f"  max |dV/dsigma| along Jensen: {max_dVdsig:.4e}")

if max_dVdsig < 1e-6:
    print(f"  ==> sigma=0 IS a critical line: the Jensen trajectory is EXACTLY a")
    print(f"      geodesic in the 2D landscape. T2 never activates spontaneously.")
    print(f"  This is expected by symmetry: the T2 direction is the second")
    print(f"  volume-preserving TT mode, and the Jensen line is a 1D fixed-point")
    print(f"  submanifold of the T2 symmetry (sigma -> -sigma symmetry in V).")
else:
    print(f"  ==> sigma=0 is NOT a critical line. The Jensen trajectory is UNSTABLE")
    print(f"      and the modulus acquires a T2 component during transit.")

# The crucial diagnostic: d2V/dsig2 along Jensen determines whether
# the Jensen trajectory is a VALLEY or a RIDGE.
print(f"\n  d2V/dsigma2 along the Jensen line (stability of Jensen path):")
for i in range(0, len(tau_scan), 10):
    stable = "STABLE (valley)" if d2Vdsig2_scan[i] > 0 else "UNSTABLE (ridge)"
    print(f"    tau={tau_scan[i]:.3f}: d2V/dsig2 = {d2Vdsig2_scan[i]:.4f}  [{stable}]")

# ============================================================================
#  SECTION 12: Summary and gate verdict
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 12: Summary")
print("=" * 72)

print(f"\n  V_KK at speed bump: {V_00:.6f}")
print(f"\n  Hessian at (tau={tau_sb}, sigma=0):")
print(f"    H_tautau   = {d2V_dtau2:.4f}")
print(f"    H_sigsig   = {d2V_dsig2:.4f}")
print(f"    H_tausig   = {d2V_dtau_dsig:.4e}")
print(f"    Eigenvalues = ({evals_H[0]:.4f}, {evals_H[1]:.4f})")
print(f"    Topology: {topology}")
print(f"\n  DeWitt-corrected mass matrix eigenvalues: ({evals_gen[0]:.4f}, {evals_gen[1]:.4f})")
print(f"  Inertia ratio G_T2/G_Jensen = {GTT/GJJ:.2f}")
print(f"  Jensen-T2 angle (DeWitt): {np.degrees(np.arccos(abs(GJT)/(sqrt(GJJ)*sqrt(GTT)))):.1f} deg")

# Is the Jensen line an exact critical manifold for sigma?
if max_dVdsig < 1e-6:
    print(f"\n  RESULT: sigma=0 is an EXACT critical line (|dV/dsig| < {max_dVdsig:.1e})")
    print(f"  The Jensen trajectory is a 1D submanifold of the 2D landscape.")
    print(f"  The T2 direction is a TRANSVERSE perturbation.")

    # Sign of d2V/dsig2 determines valley vs ridge
    d2V_at_sb = d2Vdsig2_scan[np.argmin(np.abs(tau_scan - tau_sb))]
    if d2V_at_sb > 0:
        print(f"  At the speed bump: d2V/dsig2 = {d2V_at_sb:.4f} > 0")
        print(f"  ==> Jensen path is a VALLEY along T2: the speed bump is a")
        print(f"      saddle point (maximum along Jensen, minimum along T2)")
        print(f"  ==> No escape route. T2 provides CONFINEMENT to the Jensen line.")
    else:
        print(f"  At the speed bump: d2V/dsig2 = {d2V_at_sb:.4f} < 0")
        print(f"  ==> Jensen path is a RIDGE along T2: the speed bump is a")
        print(f"      local 2D maximum. T2 provides an ESCAPE ROUTE.")
        print(f"  ==> Modulus can deflect off Jensen during transit!")

print(f"\n  GATE: OFF-JENSEN-T2-54 = INFO")

# ============================================================================
#  PLOTTING
# ============================================================================
print("\n" + "=" * 72)
print("  Generating plots...")
print("=" * 72)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('OFF-JENSEN-T2-54: Two-Field Landscape at Speed Bump', fontsize=14)

# Panel 1: 2D contour plot of V_KK
ax = axes[0, 0]
TAU, SIG = np.meshgrid(tau_range, sig_range, indexing='ij')
levels = 30
cp = ax.contourf(TAU, SIG, V_grid, levels=levels, cmap='RdYlBu_r')
ax.contour(TAU, SIG, V_grid, levels=levels, colors='k', linewidths=0.3, alpha=0.5)
ax.plot(tau_sb, 0.0, 'ko', ms=8, label=f'Speed bump')
ax.axhline(0.0, color='white', ls='--', lw=1, alpha=0.7)
ax.set_xlabel(r'$\tau$ (Jensen)')
ax.set_ylabel(r'$\sigma$ (T2)')
ax.set_title(r'$V_{\rm KK}(\tau, \sigma)$')
ax.legend(fontsize=8)
fig.colorbar(cp, ax=ax, label=r'$V_{\rm KK}$ [$M_{\rm KK}^4$]', shrink=0.8)

# Panel 2: V along Jensen (sigma=0)
ax = axes[0, 1]
V_Jensen_line = np.array([V_KK_2d(t, 0.0) for t in tau_range])
ax.plot(tau_range, V_Jensen_line, 'b-', lw=2)
ax.axvline(tau_sb, color='r', ls='--', lw=1, label=f'Speed bump')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{\rm KK}$')
ax.set_title(r'$V_{\rm KK}(\tau, 0)$ along Jensen')
ax.legend()

# Panel 3: V along T2 at the speed bump
ax = axes[0, 2]
sig_fine = np.linspace(-0.015, 0.015, 101)
V_T2_line = np.array([V_KK_2d(tau_sb, s) for s in sig_fine])
ax.plot(sig_fine, V_T2_line, 'r-', lw=2)
ax.axvline(0.0, color='k', ls='--', lw=0.5)
ax.set_xlabel(r'$\sigma$ (T2 amplitude)')
ax.set_ylabel(r'$V_{\rm KK}$')
ax.set_title(rf'$V_{{\rm KK}}({tau_sb}, \sigma)$ along T2')

# Panel 4: d2V/dsig2 along Jensen
ax = axes[1, 0]
ax.plot(tau_scan, d2Vdsig2_scan, 'g-', lw=2)
ax.axhline(0.0, color='k', ls='--', lw=0.5)
ax.axvline(tau_sb, color='r', ls='--', lw=1, label='Speed bump')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\partial^2 V/\partial\sigma^2$')
ax.set_title(r'T2 stability along Jensen')
ax.legend()

# Panel 5: Scalar curvature along T2
ax = axes[1, 1]
ax.plot(sigmas, R_along_T2 / alpha_K, 'purple', lw=2)
ax.axvline(0.0, color='k', ls='--', lw=0.5)
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$R_K / \alpha_K$')
ax.set_title(rf'Scalar curvature along T2 at $\tau={tau_sb}$')

# Panel 6: Hessian eigenvalues along Jensen
ax = axes[1, 2]
# Compute Hessian eigenvalues at each tau
eig1_scan = np.zeros_like(tau_scan)
eig2_scan = np.zeros_like(tau_scan)

for i, t in enumerate(tau_scan):
    h_t = 1e-4
    h_s2 = 1e-5
    V00 = V_KK_2d(t, 0.0)
    Vp0 = V_KK_2d(t + h_t, 0.0)
    Vm0 = V_KK_2d(t - h_t, 0.0)
    V0p = V_KK_2d(t, h_s2)
    V0m = V_KK_2d(t, -h_s2)
    Vpp2 = V_KK_2d(t + h_t, h_s2)
    Vpm2 = V_KK_2d(t + h_t, -h_s2)
    Vmp2 = V_KK_2d(t - h_t, h_s2)
    Vmm2 = V_KK_2d(t - h_t, -h_s2)

    H11 = (Vp0 - 2*V00 + Vm0) / h_t**2
    H22 = (V0p - 2*V00 + V0m) / h_s2**2
    H12 = (Vpp2 - Vpm2 - Vmp2 + Vmm2) / (4*h_t*h_s2)

    H_local = np.array([[H11, H12], [H12, H22]])
    ev = np.linalg.eigvalsh(H_local)
    eig1_scan[i] = ev[0]
    eig2_scan[i] = ev[1]

ax.plot(tau_scan, eig1_scan, 'b-', lw=2, label=r'$\lambda_1$ (smaller)')
ax.plot(tau_scan, eig2_scan, 'r-', lw=2, label=r'$\lambda_2$ (larger)')
ax.axhline(0.0, color='k', ls='--', lw=0.5)
ax.axvline(tau_sb, color='gray', ls='--', lw=1)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Hessian eigenvalue')
ax.set_title('Hessian eigenvalues along Jensen')
ax.legend()

plt.tight_layout()
plot_path = os.path.join(DATA_DIR, 's54_off_jensen_t2.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

# ============================================================================
#  Save data
# ============================================================================
data_path = os.path.join(DATA_DIR, 's54_off_jensen_t2.npz')
np.savez(data_path,
         tau_range=tau_range,
         sig_range=sig_range,
         V_grid=V_grid,
         R_grid=R_grid,
         tau_sb=tau_sb,
         V_sb=V_00,
         Hessian=H,
         Hessian_evals=evals_H,
         Hessian_evecs=evecs_H,
         G_2d=G_2d,
         gen_evals=evals_gen,
         gen_evecs=evecs_gen,
         v_Jensen=v_Jensen,
         v_T2=v_T2,
         v_T2_perp=v_T2_perp,
         d2Vdsig2_scan=d2Vdsig2_scan,
         dVdsig_scan=dVdsig_scan,
         V_Jensen_scan=V_Jensen_scan,
         tau_scan=tau_scan,
         eig1_scan=eig1_scan,
         eig2_scan=eig2_scan)
print(f"  Data saved: {data_path}")

print("\n" + "=" * 72)
print("  OFF-JENSEN-T2-54: COMPLETE")
print("=" * 72)
