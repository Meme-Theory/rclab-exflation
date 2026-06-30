#!/usr/bin/env python3
"""
S52 — RICCI-FLOW-52: Ricci Flow vs Modulus Dynamics on Jensen SU(3)
====================================================================

Gate: INFO (does Ricci flow reproduce the spectral action gradient?)

Physics:
  Compare the Ricci flow direction on the Jensen-deformed SU(3) metric
  with the spectral action gradient and KK potential gradient from W2-A.

  1. Ricci flow: dg/dt = -2 Ric(g). On left-invariant metrics of SU(3),
     this reduces to an ODE for the metric components on three irreducible
     summands of su(3) = u(1) + su(2) + C^2.

  2. Jensen metric: g_s = (x1(s), x2(s), x3(s)) on (u(1), su(2), C^2)
     with volume-preserving constraint x1 * x2^3 * x3^4 = const.

  3. The bi-invariant metric (x1 = x2 = x3 = alpha) is an Einstein fixed
     point of normalized Ricci flow. The Jensen deformation moves away
     from this fixed point.

  4. Ricci flow direction at the fold: does d(tau)/dt_RF point back toward
     tau = 0 (the bi-invariant metric)?

  5. Compare with:
     - dS_SA/dtau = +58672.80 (spectral action gradient at fold)
     - dV_KK/dtau from 12D reduction (KK potential gradient)

Mathematical framework:
  For a compact semisimple Lie group G with left-invariant metric diagonal
  in an orthogonal decomposition g = m_1 + m_2 + m_3, the Ricci tensor
  on each summand m_i (with metric x_i * B|_{m_i}) is given by the
  Milnor-type formula (Besse Ch. 7):

    Ric_i = (1/2) * sum_j (B_i/(2*x_i)) + ...

  For SU(3) with g = u(1) + su(2) + C^2 (dimensions 1, 3, 4):
  The structure constants c_{ijk} control the Ricci components.

  The KEY formula (D'Atri-Ziller, Bohm-Wilking, Park-Sakane):
  For left-invariant metrics on SU(3) parameterized by (x1, x2, x3)
  on (u(1), su(2), C^2), with [ijk] structure constants from the
  Lie algebra decomposition, the Ricci flow is:

    dx_i/dt = -2 * r_i(x1, x2, x3)

  where r_i are the Ricci curvature eigenvalues on each summand.

Inputs:
  - canonical_constants.py: tau_fold, dS_fold, G_DeWitt, g0_diag, etc.
  - s52_12d_reduction.npz: R_K(tau) data

Output:
  - s52_ricci_flow.npz
  - s52_ricci_flow.png (3-panel)

Author: Baptista-Spacetime-Analyst (Session 52)
Date: 2026-03-20
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, g0_diag, dS_fold, d2S_fold, G_DeWitt, Vol_SU3_Haar,
    M_KK_kerner, M_Pl_reduced, PI, S_fold, a2_fold, a4_fold, a0_fold,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("  S52 — RICCI-FLOW-52: Ricci Flow vs Modulus Dynamics on Jensen SU(3)")
print("=" * 72)

# ============================================================================
#  STEP 1: SU(3) Lie algebra structure constants
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 1: SU(3) Lie Algebra Decomposition and Structure Constants")
print(f"{'='*72}")

# su(3) = u(1) + su(2) + C^2
# Dimensions: d1 = 1, d2 = 3, d3 = 4
# Total: 1 + 3 + 4 = 8 = dim(SU(3))
d1, d2, d3 = 1, 3, 4

# The Cartan-Killing form on su(3): B(X,Y) = 6 * Tr(X*Y) (for our normalization)
# The bi-invariant metric: kappa(X,Y) = alpha * (-Tr(X*Y)) where alpha = g0_diag = 3
alpha = g0_diag  # = 3.0

# For the Killing form normalization:
# B(X,Y) = Tr(ad_X ad_Y) = 6 * Tr(X*Y) for SU(3)
# We use kappa = alpha * (-Tr(X*Y)) = -(alpha/6) * B
# So B|_{u(1)} restricted to our normalization:
# The dual Coxeter number of SU(3) is h* = 3
# Killing form: B(H,H) = 2*h* for the longest root

# Structure constants for su(3) = u(1) + su(2) + C^2:
# The key non-vanishing brackets are:
#   [u(1), C^2] -> C^2   (the u(1) charge of the doublet)
#   [su(2), C^2] -> C^2  (the doublet representation)
#   [su(2), su(2)] -> su(2)  (the Lie bracket of su(2))
#   [C^2, C^2] -> u(1) + su(2)  (back-reaction from the doublet)
#
# The structure constants squared, summed over basis elements:
# We need the quantities [ijk] = sum_{a in m_i, b in m_j, c in m_k} c_{abc}^2

# For SU(3) with the decomposition u(1) + su(2) + C^2:
# From Besse Chapter 7, or explicit computation with Gell-Mann matrices:
#
# The SU(3) generators in the standard basis:
# lambda_1,...,lambda_8 (Gell-Mann matrices)
# u(1) = span{lambda_8} (the hypercharge generator)
# su(2) = span{lambda_1, lambda_2, lambda_3} (isospin)
# C^2 = span{lambda_4, lambda_5, lambda_6, lambda_7} (the doublet)
#
# Structure constants f_{abc} from [T_a, T_b] = i f_{abc} T_c
# with T_a = lambda_a / 2.
#
# We need the "triple bracket" sums for the Ricci tensor.
# Define:
#   [ijk] = sum_{a in m_i, b in m_j, c in m_k} (f_{abc})^2
#
# For SU(3) with the basis T_a = lambda_a/2:
# f_{123} = 1
# f_{147} = f_{165} = f_{246} = f_{257} = f_{345} = f_{376} = 1/2
# f_{458} = f_{678} = sqrt(3)/2
#
# Let's compute [ijk] explicitly.

# SU(3) structure constants f_{abc} (totally antisymmetric)
# Non-zero values (and permutations):
f_abc = {}
f_abc[(1,2,3)] = 1.0
f_abc[(1,4,7)] = 0.5
f_abc[(1,6,5)] = 0.5  # f_{165} = -f_{156} = 0.5, so f_{156} = -0.5
f_abc[(2,4,6)] = 0.5
f_abc[(2,5,7)] = 0.5
f_abc[(3,4,5)] = 0.5
f_abc[(3,7,6)] = 0.5  # f_{376} = -f_{367} = 0.5, so f_{367} = -0.5
f_abc[(4,5,8)] = np.sqrt(3)/2
f_abc[(6,7,8)] = np.sqrt(3)/2

# Build full antisymmetric tensor
import itertools
f_full = np.zeros((9, 9, 9))  # 1-indexed via index+1
for (a, b, c), val in f_abc.items():
    for perm in itertools.permutations([a, b, c]):
        sign = 1  # (local)
        # Compute sign of permutation
        inv = 0
        lst = list(perm)
        for ii in range(3):
            for jj in range(ii+1, 3):
                if lst[ii] > lst[jj]:
                    inv += 1
        sign = (-1)**inv
        f_full[perm[0], perm[1], perm[2]] = sign * val

# Group indices by summand:
# u(1): index 8
# su(2): indices 1,2,3
# C^2: indices 4,5,6,7
idx_u1 = [8]
idx_su2 = [1, 2, 3]
idx_C2 = [4, 5, 6, 7]

groups = [idx_u1, idx_su2, idx_C2]
group_names = ['u(1)', 'su(2)', 'C^2']

# Compute [ijk] = sum_{a in m_i, b in m_j, c in m_k} f_{abc}^2
# Note: this counts ORDERED triples. The [ijk] with all three distinct
# has a symmetry factor, but for the Ricci formula we need specific combinations.
bracket_sq = np.zeros((3, 3, 3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            total = 0.0  # (local)
            for a in groups[i]:
                for b in groups[j]:
                    for c in groups[k]:
                        total += f_full[a, b, c]**2
            bracket_sq[i, j, k] = total

print(f"\n  Structure constant sums [ijk] = sum f_abc^2:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if bracket_sq[i, j, k] > 1e-15:
                print(f"    [{group_names[i]},{group_names[j]},{group_names[k]}] = {bracket_sq[i,j,k]:.6f}")

# ============================================================================
#  STEP 2: Ricci curvature of left-invariant metrics on SU(3)
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 2: Ricci Curvature Formula for Left-Invariant Metrics")
print(f"{'='*72}")

# For a left-invariant metric on a compact semisimple Lie group G with
# orthogonal decomposition g = m_1 + m_2 + ... + m_p,
# where the metric has value x_i on m_i (i.e., g|_{m_i} = x_i * B|_{m_i}),
# the Ricci curvature eigenvalue on m_i is (Besse, eq. 7.38):
#
#   r_i = (1/(2*x_i)) * B_i - (1/2) * sum_{j,k} [ijk]^2 / (d_i * x_j * x_k)
#         * (x_k^2 - (x_i - x_j)^2) / (4 * x_i)
#
# Wait, let me be more careful. The standard formula for the Ricci tensor
# on a compact Lie group with left-invariant metric is:
#
# For G compact semisimple, g = m_1 + m_2 + m_3 with metric diag(x_1, x_2, x_3)
# relative to the Killing form B:
#
#   Ric(e_a, e_a) = (1/2) * B(e_a, e_a) / x_a
#     - (1/4) * sum_{b,c} f_{abc}^2 * x_a / (x_b * x_c)
#     + (1/2) * sum_{b,c} f_{abc}^2 * x_c / (x_a * x_b)
#
# But this is for a basis e_a with B(e_a, e_a) = 1.
# Our metric is g(e_a, e_a) = x_i when a in m_i.
# The Ricci tensor as a (0,2) tensor on the orthonormal basis is:
#   r_i = Ric(e_a, e_a) for a in m_i
#
# Actually, for left-invariant metrics on a unimodular Lie group G,
# the Milnor-Besse formula gives (for a g-orthonormal basis {e_a}):
#
#   Ric(e_a, e_a) = -(1/2) sum_b B(e_a, e_b)
#                   - (1/4) sum_{b,c} f_{abc}^2
#                   + (1/2) sum_{b,c} f_{bca}^2  [note index order]
#
# For SU(3), the Killing form B(X,Y) = 6*Tr(X*Y) with normalization
# T_a = lambda_a/2.
#
# Actually, let me use the more standard and explicit formula from
# D'Atri-Ziller (1979) and Park-Sakane (1986) for diagonal metrics
# on three-summand decompositions.
#
# For G compact semisimple with g = m_1 + m_2 + m_3 (d_i = dim m_i),
# metric g_i on m_i (meaning g(X,X) = g_i * kappa(X,X) for X in m_i,
# where kappa = Killing form), the Ricci curvature on m_i is:
#
#   r_i = 1/(2*g_i) + (g_i^2 - (g_j - g_k)^2)/(8*g_j*g_k) * (-[ijk]^2/(d_i*c_B))
#
# where c_B is a Killing form normalization.
#
# This is getting notation-heavy. Let me use the EXPLICIT formula that
# Baptista's eq 2.22 from Paper 13 gives us, adapted to diagonal metrics.

# CLEAN DERIVATION using Besse Chapter 7, Proposition 7.38:
#
# For a compact Lie group G, left-invariant metric <,> on g.
# Choose <,>-orthonormal basis {e_i} of g.
# The scalar curvature is:
#   R = -(1/4) sum_{i,j} |[e_i, e_j]|^2 + (1/2) sum_{i,j} <[e_i,[e_i,e_j]], e_j>
#
# (This is eq 2.22 of Baptista Paper 13, coming from Besse.)
#
# For the RICCI tensor on individual directions, we need:
#   Ric(e_a, e_a) = -(1/2) sum_b <[e_a,[e_a,e_b]], e_b>
#                   - (1/4) sum_{b,c} |<[e_b,e_c], e_a>|^2
#                   + (1/2) sum_{b,c} <[e_c,e_a], e_b>^2
#
# For a DIAGONAL metric in the decomposition g = m_1 + m_2 + m_3
# with g|_{m_i} = x_i * kappa|_{m_i}, a kappa-orthonormal basis
# {u_alpha} of m_i has g-norm sqrt(x_i), so the g-orthonormal
# basis is e_alpha = u_alpha / sqrt(x_i).
#
# The structure constants in the g-orthonormal basis become:
#   f'_{abc} = f_{abc} / sqrt(x_i * x_j * x_k)
# where a in m_i, b in m_j, c in m_k, and f_{abc} are the structure
# constants in the kappa-orthonormal basis.
#
# The Ricci tensor on a g-orthonormal direction e_a in m_i is then:
#   r_i = Ric(e_a, e_a) / x_i   [Ricci as ratio to metric]
#
# Let me just compute it directly from first principles numerically.

# Build the metric on su(3) in the Gell-Mann basis.
# T_a = lambda_a / 2, so Tr(T_a T_b) = delta_{ab}/2
# Killing form: B(T_a, T_b) = Tr(ad(T_a) ad(T_b))
# For su(3): B(T_a, T_b) = 6 * Tr(T_a T_b) = 3 * delta_{ab}
# Our reference metric kappa = alpha * (-Tr(X Y)) with alpha = 3
# So kappa(T_a, T_b) = 3 * Tr(T_a T_b) = 3/2 * delta_{ab}
# (Note: Tr(T_a T_b) = (1/2) delta_{ab} for su(N) with T_a = lambda_a/2)

# With the Killing form normalization B(T_a, T_b) = 3 * delta_{ab},
# a B-orthonormal basis has B-norm = 1, meaning Tr(T_a T_b) = 1/3.
# Our kappa-orthonormal basis has kappa(e_a, e_a) = 1, meaning
# alpha * Tr(e_a e_a) = 1, so Tr(e_a^2) = 1/alpha = 1/3.
# Thus e_a = sqrt(2/3) * lambda_a / sqrt(2) = lambda_a / sqrt(3)...
# Actually let me just work numerically with T_a = lambda_a/2.

# The metric assigns scales (x1, x2, x3) to (u(1), su(2), C^2).
# In the standard basis {T_1,...,T_8}:
# g(T_a, T_b) = x_i * Tr(T_a T_b) for a,b in m_i (both in same summand)
#             = 0 for a in m_i, b in m_j, i != j (orthogonal summands)
#
# Wait, actually the Jensen metric is NOT block-diagonal in this sense.
# Baptista's metric g has off-diagonal terms mixing u(2) and C^2.
# The volume-preserving Jensen parameterization rediagonalizes this.
#
# Let me use the REDIAGONALIZED form. From the 12D reduction script:
# Jensen metric: g_s = e^{2s} * kappa|_{u(1)} + e^{-2s} * kappa|_{su(2)} + e^s * kappa|_{C^2}
# Volume: det(g) ~ (e^{2s})^1 * (e^{-2s})^3 * (e^s)^4 = e^{2s-6s+4s} = e^0 = 1
# Volume-preserving: CHECK.
#
# In terms of scales: x1 = alpha * e^{2s}, x2 = alpha * e^{-2s}, x3 = alpha * e^s
# where alpha = 3.0 is the overall scale.
#
# IMPORTANT: This is the volume-preserving Jensen deformation where
# s = tau is the framework parameter.

print(f"\n  Jensen metric parameterization:")
print(f"  g_s = diag(x1(s), x2(s), x3(s)) on (u(1), su(2), C^2)")
print(f"  x1(s) = alpha * e^{{2s}},  x2(s) = alpha * e^{{-2s}},  x3(s) = alpha * e^s")
print(f"  alpha = {alpha:.1f}")
print(f"  Volume: x1^1 * x2^3 * x3^4 = alpha^8 * e^{{2s - 6s + 4s}} = alpha^8 = const")

def jensen_metric(s):
    """Return (x1, x2, x3) for the volume-preserving Jensen metric at parameter s."""
    return alpha * np.exp(2*s), alpha * np.exp(-2*s), alpha * np.exp(s)

# Verify volume preservation
for s_test in [0.0, 0.1, 0.19, 0.5]:
    x1, x2, x3 = jensen_metric(s_test)
    vol = x1**1 * x2**3 * x3**4
    vol_0 = alpha**8
    print(f"  s={s_test:.2f}: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}, vol/vol_0 = {vol/vol_0:.10f}")

# ============================================================================
#  STEP 3: Ricci tensor computation from structure constants
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 3: Ricci Tensor on SU(3) with Jensen Metric")
print(f"{'='*72}")

# For a compact Lie group G with left-invariant metric, the Ricci tensor
# at the identity (on the Lie algebra g) is given by (Besse 7.38):
#
# For X in g, with {e_i} a g-orthonormal basis:
#   Ric(X,X) = -(1/2) * sum_i g([X,[X,e_i]], e_i)
#              -(1/4) * sum_{i,j} g([e_i,e_j], X)^2
#              +(1/2) * sum_{i,j} g([X,e_i], e_j)^2
#
# With our diagonal metric g(T_a, T_b) = x_{grp(a)} * (Tr(T_a T_b) * 2)
# where Tr(T_a T_b) = delta_{ab}/2 and grp(a) is the summand containing a.
# So g(T_a, T_b) = x_{grp(a)} * delta_{ab} when a,b in same group,
# and 0 when in different groups (block-diagonal assumption).
#
# Wait — I need to be careful. The Jensen metric is NOT block-diagonal
# in the original Gell-Mann basis. It mixes u(2) and C^2.
# But in the REDIAGONALIZED basis (Baptista eq 2.35-2.36), it IS diagonal.
#
# However, the structure constants CHANGE when we change basis.
#
# SIMPLIFICATION: For the VOLUME-PRESERVING Jensen deformation, where
# the metric is diagonal in the (u(1), su(2), C^2) decomposition with
# eigenvalues (x1, x2, x3), we can compute the Ricci tensor directly.
#
# The key formula for the Ricci curvature of a diagonal left-invariant
# metric g_a = x_{grp(a)} on a compact Lie group (Milnor, Besse):
#
# For a g-orthonormal basis e_a = T_a / sqrt(x_{grp(a)}):
#   Ric(e_a, e_a) = (1/2x_i) - (1/4) sum_{b,c} (c^a_{bc})^2
#                   + (1/2) sum_{b,c} (c^b_{ac})^2
#
# where c^a_{bc} = g([e_b, e_c], e_a) = f_{bca} / sqrt(x_i * x_j * x_k)
# with a in m_i, b in m_j, c in m_k.
#
# Actually, for a LEFT-invariant metric on a Lie group, the formula
# involves the Killing form explicitly. Let me use the standard result
# from Milnor (1976) for unimodular Lie groups.
#
# For a unimodular Lie group with left-invariant metric, if {e_i} is an
# orthonormal basis and [e_i, e_j] = sum_k c^k_{ij} e_k, then:
#
#   Ric(e_a, e_a) = -(1/2) sum_i (c^i_{ia})^2
#                   + (1/4) sum_{i,j} [2*(c^a_{ij})^2 - c^i_{ja} * c^j_{ia}]
#
# But for semisimple groups, this simplifies. Let me just compute directly.

def ricci_on_su3(x1, x2, x3):
    """
    Compute the Ricci tensor eigenvalues (r1, r2, r3) on (u(1), su(2), C^2)
    for the left-invariant metric with scales (x1, x2, x3) on SU(3).

    Uses the EXPLICIT formula for the scalar curvature's decomposition
    into summand contributions, derived from the structure constants
    of su(3) = u(1) + su(2) + C^2.

    The approach: compute Ric(e_a, e_a) for a representative e_a in each
    summand, using the formula from Besse Chapter 7.

    For a compact Lie group with left-invariant metric g and
    g-orthonormal basis {e_i}, with structure constants c^k_{ij}:

      Ric(e_a, e_a) = -(1/2) sum_{i,j} c^a_{ij} * c^a_{ji}
                      -(1/4) sum_{i,j} (c^j_{ai})^2
                      +(1/2) sum_{i,j} c^j_{ai} * c^i_{ja}

    Wait, I need to be very precise. Let me use the Besse formula directly.
    """
    # Build the 8x8 metric matrix in the T_a basis
    # g(T_a, T_b) = x_{grp(a)} * Tr(T_a T_b) * 2 = x_{grp(a)} * delta_{ab}
    # (since Tr(T_a T_b) = delta_{ab}/2)
    #
    # IMPORTANT: This assumes the Jensen metric IS diagonal in the Gell-Mann
    # basis. But actually, the Jensen deformation introduces off-diagonal terms.
    # The VOLUME-PRESERVING parameterization g_s is defined as:
    #   g_s|_{u(1)} = alpha * e^{2s} * kappa_0|_{u(1)}
    #   g_s|_{su(2)} = alpha * e^{-2s} * kappa_0|_{su(2)}
    #   g_s|_{C^2} = alpha * e^{s} * kappa_0|_{C^2}
    # where kappa_0 is the Killing metric restricted to each summand.
    #
    # This IS block-diagonal because the three summands are kappa-orthogonal
    # AND g_s just rescales each block independently.
    #
    # Note: Baptista's sigma-parameterized metric g_sigma is NOT block-diagonal
    # (it mixes u(2) and C^2). But the volume-preserving Jensen metric g_s
    # (which is what our framework uses) IS block-diagonal after the basis
    # change of eq 2.35-2.36.

    # Metric matrix: g_{ab} = x_{grp(a)} * delta_{ab} (in Gell-Mann basis)
    # Inverse: g^{ab} = (1/x_{grp(a)}) * delta_{ab}

    # g-orthonormal basis: e_a = T_a / sqrt(x_{grp(a)})
    # Structure constants in g-orthonormal basis:
    # [e_b, e_c] = [T_b, T_c] / sqrt(x_j * x_k) = i * f_{bcd} T_d / sqrt(x_j * x_k)
    # g([e_b, e_c], e_a) = i * f_{bca} * sqrt(x_i) / sqrt(x_j * x_k)
    # ... but structure constants are real, not imaginary!
    #
    # For the Lie bracket: [T_a, T_b] = i * f_{abc} * T_c (physics convention)
    # But Ric uses the REAL Lie bracket, so [T_a, T_b] = f_{abc} T_c in the
    # Besse convention (where f includes the factor of i implicitly).
    #
    # Actually, the Gell-Mann matrices satisfy:
    # [lambda_a/2, lambda_b/2] = i * f_{abc} * lambda_c/2
    # So for the REAL structure constants of the REAL Lie algebra su(3)
    # (viewed as anti-Hermitian matrices), we have:
    # [X_a, X_b] = c_{abc} X_c where X_a = i*lambda_a/2
    # c_{abc} = -f_{abc} (the sign flip from the factor of i)
    # ... no wait. Let me be precise.
    #
    # su(3) consists of traceless anti-Hermitian 3x3 matrices.
    # A basis is X_a = i * lambda_a / 2 (a = 1,...,8).
    # Then [X_a, X_b] = -f_{abc} X_c (where f_{abc} are the standard
    # structure constants of the Gell-Mann basis).
    #
    # No — let me just compute: [X_a, X_b] = [i*lambda_a/2, i*lambda_b/2]
    # = i^2 * [lambda_a/2, lambda_b/2] = -1 * i*f_{abc}*lambda_c/2
    # = -f_{abc} * (i*lambda_c/2) = -f_{abc} * X_c
    #
    # Hmm, that gives a minus sign. But structure constants should be
    # [e_a, e_b] = c_{ab}^c e_c. So c_{ab}^c = -f_{abc} for the anti-Hermitian
    # basis. But actually the sign doesn't matter for the Ricci tensor
    # since everything involves c^2.
    #
    # For the Ricci computation, what matters is the sum:
    # sum_{b,c} c_{abc}^2 = sum_{b,c} f_{abc}^2
    # which is what we already computed in bracket_sq.

    # We use the formula from Besse (7.38) for COMPACT Lie groups:
    #
    # Ric(X, Y) = -(1/2) B(X, Y) + (1/4) sum_{i,j} g([X_i, X_j], X) * g([X_i, X_j], Y)
    #
    # Wait, that's the Ricci tensor where B is the Killing form.
    # For semisimple compact groups: B(X,Y) = Tr(ad_X ad_Y).
    #
    # The correct Milnor-Besse formula for compact semisimple G:
    # Ric(X, X) = (1/4*x_i) * B(X, X) [if X in m_i]
    #   ... no, that's only for the bi-invariant metric.

    # Let me just use the EXPLICIT formula from D'Atri-Ziller (1979).
    # For a compact Lie group G with bi-invariant metric B = Killing form,
    # and a left-invariant metric g that is diagonal in a B-orthogonal
    # decomposition g = m_1 + ... + m_p:
    #   g|_{m_i} = lambda_i * B|_{m_i}
    #
    # The Ricci tensor of g on m_i is:
    #   Ric_i = B_i/(2*lambda_i) - sum_{j,k} [ijk]^2 * lambda_i / (4*d_i*lambda_j*lambda_k)
    #           + sum_{j,k} [jki]^2 / (2*d_i*lambda_j)
    #
    # where B_i = B|_{m_i} eigenvalue, d_i = dim(m_i), and
    # [ijk] = sum_{a in m_i, b in m_j, c in m_k} f_{abc}^2.
    #
    # Hmm, this still isn't quite right. Let me use a cleaner source.
    #
    # Park-Sakane (1986), Prop 3.1, for SU(3) specifically:
    # With the decomposition su(3) = p1 + p2 + p3 where
    # p1 = real span of {iH} (u(1), dim 1)
    # p2 = real span of {E_alpha} for roots in su(2) (dim 3)
    # p3 = real span of {E_beta} for remaining roots (C^2, dim 4)
    #
    # Actually the cleanest approach: compute Ric from the scalar curvature.
    # For a diagonal metric (x1, x2, x3) on (1,3,4)-dim summands:
    #   R = d1*r1/x1 + d2*r2/x2 + d3*r3/x3 (where r_i = Ric eigenvalue on m_i)
    #   R = 1*r1/x1 + 3*r2/x2 + 4*r3/x3
    #
    # We know R from Baptista (eq 2.40). And we need Ric_i.
    #
    # Alternative: compute numerically. Build 8x8 matrices and compute directly.

    # === NUMERICAL COMPUTATION ===
    # Use the Milnor formula (Besse Prop 7.38):
    # For a g-orthonormal basis {e_a} of the Lie algebra, with
    # structure constants gamma^k_{ij} = g([e_i, e_j], e_k):
    #
    #   ric(e_a, e_a) = -(1/2) * sum_i g([e_a,[e_a,e_i]], e_i)
    #                   -(1/4) * sum_{i,j} gamma^a_{ij}^2
    #                   +(1/2) * sum_{i,j} (gamma^j_{ai})^2
    #
    # But this is for a UNIMODULAR Lie group.

    # Build the metric-dependent structure constants.
    # In the original T_a = lambda_a/2 basis, the structure constants are f_{abc}
    # (stored in f_full). The metric assigns:
    #   g(T_a, T_b) = x_{grp(a)} * delta_{ab} / 2  [since Tr(T_a T_b) = delta_{ab}/2]
    #
    # Wait, I need to be more careful about normalization.
    # The Killing metric on su(3): B(X,Y) = Tr(ad_X ad_Y)
    # For T_a = lambda_a/2: B(T_a, T_b) = sum_c f_{acd} f_{bcd} = C_adj * delta_{ab}
    # For su(N): C_adj = N, so B(T_a, T_b) = 3 * delta_{ab} for SU(3).
    #
    # Our reference metric kappa = alpha * (-Tr(X Y)). For X = i*lambda_a/2:
    # -Tr(X^2) = -Tr(-lambda_a^2/4) = Tr(lambda_a^2)/4 = (1/2)/...
    # Actually Tr(lambda_a lambda_b) = 2*delta_{ab} for Gell-Mann matrices.
    # So for X_a = i*lambda_a/2: -Tr(X_a X_b) = -i^2 Tr(lambda_a lambda_b)/4
    # = Tr(lambda_a lambda_b)/4 = 2*delta_{ab}/4 = delta_{ab}/2.
    # So kappa(X_a, X_b) = alpha * delta_{ab}/2 = (3/2) * delta_{ab}.
    #
    # The Jensen metric with scales (x1, x2, x3) means:
    # g(X_a, X_b) = x_{grp(a)} * delta_{ab}/2  [proportional to kappa with scale]
    # Wait, if kappa(X_a, X_b) = (alpha/2)*delta_{ab}, and we want
    # g|_{m_i} = (x_i/alpha) * kappa|_{m_i}, then
    # g(X_a, X_b) = (x_i/alpha) * (alpha/2) * delta_{ab} = (x_i/2) * delta_{ab}
    # for a,b both in m_i.
    #
    # So the metric matrix in the X_a basis is diagonal:
    # G_{ab} = (x_{grp(a)}/2) * delta_{ab}

    # Map index a (1-8) to group
    def grp(a):
        if a == 8: return 0  # u(1)
        elif a in [1,2,3]: return 1  # su(2)
        else: return 2  # C^2 (4,5,6,7)

    x = [x1, x2, x3]

    # g-orthonormal basis: e_a = X_a * sqrt(2/x_{grp(a)})
    # so that g(e_a, e_a) = (x_{grp(a)}/2) * (2/x_{grp(a)}) = 1

    # Structure constants in g-orthonormal basis:
    # [e_b, e_c] = sqrt(2/x_j) * sqrt(2/x_k) * [X_b, X_c]
    #            = (2/sqrt(x_j*x_k)) * (-f_{bcd}) * X_d
    #            = (2/sqrt(x_j*x_k)) * (-f_{bcd}) * (1/sqrt(2/x_i)) * e_d  [if d in m_i]
    #            = (2/sqrt(x_j*x_k)) * (-f_{bcd}) * sqrt(x_i/2) * e_d
    #            = -f_{bcd} * sqrt(2*x_i / (x_j*x_k)) * e_d
    #
    # So: gamma^d_{bc} = g([e_b, e_c], e_d) = -f_{bcd} * sqrt(2*x_{grp(d)} / (x_{grp(b)}*x_{grp(c)}))
    # Wait, that's the structure constant of the ANTI-Hermitian basis,
    # which carries a minus from [X_a, X_b] = -f_{abc} X_c.
    #
    # For the Ricci computation, only gamma^2 matters, so the sign cancels.
    # gamma^d_{bc} = f_{bcd} * sqrt(2*x_{grp(d)} / (x_{grp(b)}*x_{grp(c)}))
    #
    # Wait, I realize I should just be computing this numerically from
    # the explicit 8x8 matrix representation. Let me go that route.

    # The Besse formula for unimodular Lie groups (Prop 7.38):
    # In terms of the g-orthonormal basis {e_i} with
    # [e_i, e_j] = sum_k gamma^k_{ij} e_k:
    #
    # ric(e_a, e_a) = -(1/2) sum_c gamma^c_{ca} * gamma^?_...
    #
    # Actually Besse 7.38 for a LEFT-invariant metric on a Lie group:
    # ric(X, X) = -(1/2) B(X,X) + (1/4) sum_{i,j} <[e_i,e_j],X>^2
    #
    # where B is the Killing form and <,> is the left-invariant metric.
    # This is only valid when X is in the center or for bi-invariant metrics.
    #
    # NO. The correct general formula (Milnor 1976, Besse 7.38):
    #
    # For a left-invariant metric <,> on a Lie group G, with orthonormal basis {e_i}:
    #
    # ric(e_k, e_k) = -(1/2) sum_j |ad_{e_j}(e_k)|^2
    #                 + (1/4) sum_{i,j} <[e_i,e_j], e_k>^2
    #                 + (1/2) sum_j <[e_k, e_j], e_k>  * ???
    #
    # I realize I'm going in circles with the formula. Let me use the
    # most explicit version.
    #
    # From Milnor (Curvatures of left invariant metrics on Lie groups, 1976):
    # For a unimodular Lie group with orthonormal basis {e_i}:
    #
    # ric(e_k, e_k) = -(1/2) sum_j [gamma^j_{jk}]^2  [this is 0 for unimodular!]
    #                 -(1/2) sum_j (gamma^k_{jk})^2      [also 0 for semisimple]
    #                 -(1/4) sum_{i,j} (gamma^k_{ij})^2
    #                 +(1/2) sum_{i,j} (gamma^j_{ik})^2
    #
    # Wait, Milnor's formula for unimodular groups simplifies. Let me
    # just use the heat equation approach or compute from the curvature
    # tensor directly.
    #
    # SIMPLEST CORRECT APPROACH for semisimple compact groups:
    # From the Koszul formula, the Levi-Civita connection is:
    #   nabla_{e_i} e_j = (1/2) [e_i, e_j] + U(e_i, e_j)
    # where U is the symmetric tensor:
    #   <U(X,Y), Z> = (1/2)(<[Z,X],Y> + <[Z,Y],X>)
    #
    # Then R(X,Y)Z = nabla_X nabla_Y Z - nabla_Y nabla_X Z - nabla_{[X,Y]} Z
    # and Ric(X,X) = sum_i <R(e_i, X)X, e_i>

    # Let me compute numerically by building the connection and curvature.
    n = 8  # dimension of su(3)

    # Structure constants gamma^k_{ij} in the g-orthonormal basis
    gamma = np.zeros((n, n, n))  # gamma[k][i][j] = gamma^k_{ij}
    for i_idx in range(n):
        i_lie = i_idx + 1  # Lie algebra index (1-8)
        for j_idx in range(n):
            j_lie = j_idx + 1
            for k_idx in range(n):
                k_lie = k_idx + 1
                # gamma^k_{ij} = f_{ijk_lie} * sqrt(x_{grp(k)} / (x_{grp(i)} * x_{grp(j)}))
                # Factor of sqrt(2) cancels in the ratio
                gi = x[grp(i_lie)]
                gj = x[grp(j_lie)]
                gk = x[grp(k_lie)]
                # Factor of sqrt(2) comes from g(X_a, X_b) = x_i/2 * delta_{ab}
                # The g-orthonormal basis e_a = X_a * sqrt(2/x_i), giving
                # gamma^k_{ij} = f_{ijk} * sqrt(2*x_k / (x_i*x_j))
                gamma[k_idx, i_idx, j_idx] = f_full[i_lie, j_lie, k_lie] * np.sqrt(2.0 * gk / (gi * gj))

    # The Koszul formula for the Levi-Civita connection on a Lie group
    # with left-invariant metric:
    # nabla_{e_i} e_j = (1/2) sum_k (gamma^k_{ij} - gamma^i_{jk} - gamma^j_{ik}) e_k
    #
    # Wait, the standard formula is:
    # 2<nabla_X Y, Z> = <[X,Y],Z> - <[Y,Z],X> + <[Z,X],Y>
    # = gamma^Z_{XY} - gamma^X_{YZ} + gamma^Y_{ZX}  [where gamma^Z_{XY} = <[X,Y],Z>]
    # = gamma[Z,X,Y] - gamma[X,Y,Z] + gamma[Y,Z,X]
    #
    # So nabla_{e_i} e_j = sum_k Gamma^k_{ij} e_k where:
    # 2*Gamma^k_{ij} = gamma[k,i,j] - gamma[i,j,k] + gamma[j,k,i]

    Gamma = np.zeros((n, n, n))  # Gamma[k][i][j] = Gamma^k_{ij}
    for i_idx in range(n):
        for j_idx in range(n):
            for k_idx in range(n):
                Gamma[k_idx, i_idx, j_idx] = 0.5 * (
                    gamma[k_idx, i_idx, j_idx]
                    - gamma[i_idx, j_idx, k_idx]
                    + gamma[j_idx, k_idx, i_idx]
                )

    # Riemann curvature tensor:
    # R^l_{kij} = sum_m (Gamma^l_{im} * Gamma^m_{jk} - Gamma^l_{jm} * Gamma^m_{ik})
    #           + sum_m Gamma^l_{m,k} * gamma^m_{ij}  [from nabla_{[e_i,e_j]} term]
    #
    # Actually: R(e_i, e_j)e_k = nabla_i nabla_j e_k - nabla_j nabla_i e_k - nabla_{[e_i,e_j]} e_k
    #
    # nabla_i nabla_j e_k = nabla_i (sum_l Gamma^l_{jk} e_l)
    #                     = sum_l Gamma^l_{jk} nabla_i e_l
    #                     = sum_l,m Gamma^l_{jk} * Gamma^m_{il} * e_m
    #                     (ignoring the d(Gamma) term since Gamma is constant on a Lie group!)
    #
    # [e_i, e_j] = sum_m gamma^m_{ij} e_m
    # nabla_{[e_i,e_j]} e_k = sum_m gamma^m_{ij} nabla_{e_m} e_k
    #                       = sum_m,l gamma^m_{ij} Gamma^l_{mk} e_l
    #
    # So: R^l_{kij} = sum_m (Gamma^m_{jk} Gamma^l_{im} - Gamma^m_{ik} Gamma^l_{jm})
    #                - sum_m gamma^m_{ij} Gamma^l_{mk}

    # Ricci tensor: Ric_{kj} = sum_i R^i_{kij}
    # = sum_i [ sum_m (Gamma^m_{ik} Gamma^i_{jm} - Gamma^m_{jk} Gamma^i_{im})
    #           + sum_m gamma^m_{ji} Gamma^i_{mk} ]
    # Wait, I have the index order wrong. Let me be more careful.
    #
    # R(e_i, e_j)e_k = sum_l R^l_{kij} e_l
    # Ric(e_a, e_b) = sum_i R^i_{aib} = sum_i <R(e_i, e_a)e_b, e_i> ...
    # No. Ric(X,Y) = Tr(Z -> R(Z,X)Y)
    # So Ric(e_a, e_b) = sum_c <R(e_c, e_a)e_b, e_c> = wait that's wrong too.
    #
    # Ric(e_a, e_b) = sum_c R(e_c, e_a, e_b, e_c) = sum_c <R(e_c, e_a)e_b, e_c>
    # No: R(W,X,Y,Z) = <R(X,Y)Z, W> in the (3,1) convention.
    # Ric(Y,Z) = sum_a R(e_a, Y, Z, e_a) = sum_a <R(Y,Z)e_a, e_a>
    # Wait. Ric(X,Y) = Tr(Z -> R(Z,X)Y) = sum_a <R(e_a, X)Y, e_a>.
    #
    # So Ric(e_k, e_k) = sum_i <R(e_i, e_k)e_k, e_i>

    Ric_diag = np.zeros(n)
    for k in range(n):
        ric_kk = 0.0  # (local)
        for i in range(n):
            # <R(e_i, e_k)e_k, e_i> = R^i_{k,i,k}
            # R(e_i, e_k)e_k = sum_l R^l_{k,i,k} e_l
            # We want the l=i component.
            #
            # R^l_{k,i,k}: this is the curvature in the convention
            # R(e_i, e_k)e_k = nabla_i nabla_k e_k - nabla_k nabla_i e_k - nabla_{[e_i,e_k]} e_k
            #
            # Let me compute R^l_{k,ik} = the l component of R(e_i, e_k)e_k
            # Using the formula I derived:
            # R^l_{k,ij} with j=k:
            # R(e_i, e_k)e_k:
            #   nabla_i nabla_k e_k = sum_m Gamma^m_{kk} * sum_l' Gamma^{l'}_{im} e_{l'}
            #                       = sum_{m,l'} Gamma^m_{kk} Gamma^{l'}_{im} e_{l'}
            #   nabla_k nabla_i e_k = sum_{m,l'} Gamma^m_{ik} Gamma^{l'}_{km} e_{l'}
            #   nabla_{[e_i,e_k]} e_k = sum_m gamma^m_{ik} sum_{l'} Gamma^{l'}_{mk} e_{l'}

            # Component l=i of R(e_i, e_k)e_k:
            R_comp = 0.0  # (local)
            for m in range(n):
                R_comp += Gamma[m, k, k] * Gamma[i, i, m]  # nabla_i nabla_k e_k, component i
                R_comp -= Gamma[m, i, k] * Gamma[i, k, m]  # nabla_k nabla_i e_k, component i
                R_comp -= gamma[m, i, k] * Gamma[i, m, k]  # nabla_{[e_i,e_k]} e_k, component i
            ric_kk += R_comp
        Ric_diag[k] = ric_kk

    # Extract Ricci eigenvalues per summand (should be constant within each summand)
    r1 = Ric_diag[7]  # index 7 = T_8 in u(1)
    r2 = np.mean([Ric_diag[0], Ric_diag[1], Ric_diag[2]])  # su(2)
    r3 = np.mean([Ric_diag[3], Ric_diag[4], Ric_diag[5], Ric_diag[6]])  # C^2

    # Verify uniformity within each summand
    r2_std = np.std([Ric_diag[0], Ric_diag[1], Ric_diag[2]])
    r3_std = np.std([Ric_diag[3], Ric_diag[4], Ric_diag[5], Ric_diag[6]])

    return r1, r2, r3, r2_std, r3_std, Ric_diag

# Test at the bi-invariant point (s=0): Ric = (1/4)*B for bi-invariant metric on compact group
# For SU(3) with our normalization:
# B(T_a, T_b) = 3 * delta_{ab}
# Ric = (1/4) * B = (3/4) * delta_{ab} in the T_a basis
# In the orthonormal basis with g = alpha/2 * I:
# Ric(e_a, e_a) = (3/4) / (alpha/2) = 3/(2*alpha) = 3/6 = 1/2

x1_0, x2_0, x3_0 = jensen_metric(0.0)
r1_0, r2_0, r3_0, std2_0, std3_0, ric_full_0 = ricci_on_su3(x1_0, x2_0, x3_0)

print(f"\n  Ricci at bi-invariant point (s=0):")
print(f"  x1 = x2 = x3 = {x1_0:.4f}")
print(f"  r1 (u(1))  = {r1_0:.8f}")
print(f"  r2 (su(2)) = {r2_0:.8f}  (std = {std2_0:.2e})")
print(f"  r3 (C^2)   = {r3_0:.8f}  (std = {std3_0:.2e})")
print(f"  Expected: Ric = B/(4*g) = 3/(4*(alpha/2)) = {3.0/(4.0*alpha/2.0):.8f}")
print(f"  Full Ric diag: {[f'{r:.6f}' for r in ric_full_0]}")

# Scalar curvature check:
# R = sum_a Ric(e_a, e_a) (in g-orthonormal basis)
R_from_ric_0 = np.sum(ric_full_0)
# From Baptista: R(0) = 12/alpha = 4.0
# But in the g-orthonormal basis: R = sum_a ric(e_a, e_a)
# The scalar curvature in the coordinate basis is:
# R_scalar = sum_a g^{aa} Ric_{aa} = sum_a (1/g_{aa}) * Ric_{aa}
# In the orthonormal basis: R_scalar = sum_a ric(e_a, e_a) directly
print(f"\n  Scalar curvature from Ric: R = {R_from_ric_0:.6f}")
print(f"  Expected (Baptista): R(0) = 12/alpha = {12.0/alpha:.6f}")

# ============================================================================
#  STEP 4: Ricci flow on the Jensen one-parameter family
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 4: Ricci Flow Direction Along Jensen Path")
print(f"{'='*72}")

# The Ricci flow is dg/dt = -2 Ric(g).
# For our diagonal metric (x1, x2, x3) on (u(1), su(2), C^2):
#   dx_i/dt = -2 * r_i * x_i
# (where r_i is the Ricci eigenvalue in the g-orthonormal basis,
# and x_i is the metric component — the factor x_i comes from
# converting back to the coordinate basis.)
#
# Wait: the Ricci flow dg/dt = -2 Ric operates on the metric TENSOR.
# If g|_{m_i} = x_i * kappa_0|_{m_i}, then
#   dg|_{m_i}/dt = (dx_i/dt) * kappa_0|_{m_i}
# and Ric|_{m_i} = r_i * g|_{m_i} = r_i * x_i * kappa_0|_{m_i}
# (where r_i is the ratio Ric/g on m_i, i.e., the Einstein eigenvalue).
#
# Actually, for a diagonal metric in the orthonormal frame, the Ricci
# tensor is also diagonal: Ric(e_a, e_b) = ric_a * delta_{ab}.
# In the coordinate (T_a) basis:
#   Ric(T_a, T_b) = ric_a * g(T_a, T_b) = ric_a * (x_i/2) * delta_{ab}
#   = (ric_a * x_i / 2) * delta_{ab}
#
# The metric in coordinate basis: g(T_a, T_b) = (x_i/2) * delta_{ab}
# So the Ricci flow: d/dt [g(T_a, T_b)] = -2 Ric(T_a, T_b)
# => d(x_i/2)/dt = -2 * (ric_a * x_i / 2)
# => dx_i/dt = -2 * ric_a * x_i
# where ric_a is the eigenvalue Ric(e_a, e_a) in the orthonormal frame.
#
# Hmm, but ric_a should be independent of which basis element within m_i.
# So dx_i/dt = -2 * r_i * x_i where r_i = Ric(e_a, e_a) for any a in m_i.

# Now: for the Jensen family, x_i(s) = alpha * exp(c_i * s) with c_1=2, c_2=-2, c_3=1.
# dx_i/ds = c_i * x_i
# So s flows as: ds/dt = (1/c_i) * (1/x_i) * dx_i/dt = (1/c_i) * (-2 * r_i)
#
# But this gives potentially DIFFERENT ds/dt for each summand i!
# That's because the Ricci flow doesn't stay on the Jensen family in general.
# The Jensen family is a 1D curve in the space of left-invariant metrics,
# but the Ricci flow is a 3D ODE system (or higher).
#
# What we can compute is: the PROJECTION of the Ricci flow vector field
# onto the tangent direction of the Jensen curve.
#
# Jensen tangent vector at s: d(x1,x2,x3)/ds = (2*x1, -2*x2, x3)
# Ricci flow vector: d(x1,x2,x3)/dt_RF = (-2*r1*x1, -2*r2*x2, -2*r3*x3)
#
# The projection (in a natural metric on the space of metrics):
# The DeWitt supermetric is G_{ij} = d_i * delta_{ij} / x_i^2
# (the metric on the space of diagonal left-invariant metrics)
#
# Actually, the natural metric on the cone of positive-definite metrics
# on each summand is the Fisher information metric:
# ds_super^2 = sum_i d_i * (dx_i/x_i)^2
#
# In terms of log(x_i), this is flat: sum_i d_i * (d log x_i)^2
#
# Jensen tangent: d(log x_i)/ds = c_i = (2, -2, 1)
# Ricci flow: d(log x_i)/dt = -2*r_i
#
# The projection of the Ricci flow onto the Jensen direction:
# ds/dt_RF = <Ricci_flow, Jensen_tangent> / |Jensen_tangent|^2
#         = [sum_i d_i * (-2*r_i) * c_i] / [sum_i d_i * c_i^2]
#
# where d_i = dim(m_i) = (1, 3, 4).

# Compute at the fold (s = tau_fold = 0.19):
s_fold = tau_fold
x1_f, x2_f, x3_f = jensen_metric(s_fold)
r1_f, r2_f, r3_f, std2_f, std3_f, ric_full_f = ricci_on_su3(x1_f, x2_f, x3_f)

print(f"\n  Ricci at fold (s = {s_fold}):")
print(f"  x1 = {x1_f:.6f}, x2 = {x2_f:.6f}, x3 = {x3_f:.6f}")
print(f"  r1 (u(1))  = {r1_f:.8f}  (std = n/a)")
print(f"  r2 (su(2)) = {r2_f:.8f}  (std = {std2_f:.2e})")
print(f"  r3 (C^2)   = {r3_f:.8f}  (std = {std3_f:.2e})")
print(f"  Full Ric diag: {[f'{r:.6f}' for r in ric_full_f]}")

# Scalar curvature at fold:
R_from_ric_f = np.sum(ric_full_f)
# Cross-check with Baptista analytic formula:
def R_K_analytic(s):
    """R_K(s)/R_K(0) = [2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}]/8, R_K(0)=12/alpha."""
    R0 = 12.0 / alpha
    return R0 * (2.0*np.exp(2*s) - 1.0 + 8.0*np.exp(-s) - np.exp(-4*s)) / 8.0

print(f"\n  Scalar curvature cross-check:")
print(f"  R from Ric sum = {R_from_ric_f:.8f}")
print(f"  R from Baptista analytic = {R_K_analytic(s_fold):.8f}")
print(f"  Relative error = {abs(R_from_ric_f - R_K_analytic(s_fold))/abs(R_K_analytic(s_fold)):.2e}")

# Jensen coefficients c_i = (2, -2, 1), dimensions d_i = (1, 3, 4)
c_jensen = np.array([2.0, -2.0, 1.0])
d_dims = np.array([d1, d2, d3], dtype=float)
r_fold = np.array([r1_f, r2_f, r3_f])

# Projection of Ricci flow onto Jensen direction:
numerator = np.sum(d_dims * (-2.0 * r_fold) * c_jensen)
denominator = np.sum(d_dims * c_jensen**2)
ds_dt_RF = numerator / denominator

print(f"\n  Ricci flow projection onto Jensen direction at fold:")
print(f"  Jensen tangent c_i = {c_jensen}")
print(f"  Ricci flow d(log x_i)/dt = -2*r_i = {-2.0*r_fold}")
print(f"  d_i * (-2*r_i) * c_i = {d_dims * (-2.0*r_fold) * c_jensen}")
print(f"  Numerator = sum d_i * (-2*r_i) * c_i = {numerator:.8f}")
print(f"  Denominator = sum d_i * c_i^2 = {denominator:.1f}")
print(f"  ds/dt_RF = {ds_dt_RF:.8f}")
print(f"  SIGN: {'TOWARD s=0 (restoring)' if ds_dt_RF < 0 else 'AWAY from s=0 (destabilizing)'}")

# ============================================================================
#  STEP 5: Ricci flow over the full Jensen path
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 5: Ricci Flow Direction Over Full Jensen Path")
print(f"{'='*72}")

s_values = np.linspace(0.01, 0.50, 50)  # Avoid s=0 where all Ric are equal
ds_dt_values = np.zeros_like(s_values)
r1_values = np.zeros_like(s_values)
r2_values = np.zeros_like(s_values)
r3_values = np.zeros_like(s_values)
R_ric_values = np.zeros_like(s_values)
R_analytic_values = np.zeros_like(s_values)

for idx, s in enumerate(s_values):
    x1, x2, x3 = jensen_metric(s)
    r1, r2, r3, _, _, ric_full = ricci_on_su3(x1, x2, x3)
    r_vec = np.array([r1, r2, r3])

    num = np.sum(d_dims * (-2.0 * r_vec) * c_jensen)
    ds_dt_values[idx] = num / denominator
    r1_values[idx] = r1
    r2_values[idx] = r2
    r3_values[idx] = r3
    R_ric_values[idx] = np.sum(ric_full)
    R_analytic_values[idx] = R_K_analytic(s)

print(f"\n  ds/dt_RF along Jensen path:")
print(f"  {'s':>6s}  {'ds/dt_RF':>12s}  {'r1':>10s}  {'r2':>10s}  {'r3':>10s}  {'R_ric':>10s}  {'R_anl':>10s}")
for idx in range(0, len(s_values), 5):
    s = s_values[idx]
    print(f"  {s:6.3f}  {ds_dt_values[idx]:12.8f}  {r1_values[idx]:10.6f}  {r2_values[idx]:10.6f}  {r3_values[idx]:10.6f}  {R_ric_values[idx]:10.6f}  {R_analytic_values[idx]:10.6f}")

# Key question: is ds/dt_RF < 0 for all s > 0?
# If so, Ricci flow drives the Jensen parameter back toward s=0 (bi-invariant).
all_negative = np.all(ds_dt_values < 0)
print(f"\n  ds/dt_RF < 0 for ALL s in (0, 0.5]: {all_negative}")
if not all_negative:
    first_positive = s_values[ds_dt_values >= 0][0] if np.any(ds_dt_values >= 0) else None
    print(f"  First s where ds/dt_RF >= 0: {first_positive}")

# ============================================================================
#  STEP 6: Comparison with spectral action gradient
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 6: Comparison — Ricci Flow vs Spectral Action Gradient")
print(f"{'='*72}")

# The spectral action gradient at the fold:
# dS_SA/dtau = +58672.80 (from canonical constants)
# This means: S_SA INCREASES with tau.
# The "force" from the spectral action: -dS_SA/dtau < 0 pushes toward LOWER tau.
# (Because the equations of motion from the spectral action include -dS/dtau as a force.)

# The KK potential gradient from 12D reduction:
# V_KK(tau) = -M_p^2 * R_K(tau) / 2
# Since R_K increases for small tau (cubic behavior R ~ 4*(1 + 1.5*s^3)),
# V_KK decreases (becomes more negative), so dV/dtau < 0 at the fold.
# The force -dV/dtau > 0 pushes toward HIGHER tau.

# Let's compute dV/dtau at the fold:
M_p_sq_MKK = (M_Pl_reduced / M_KK_kerner)**2
def V_KK(s):
    return -M_p_sq_MKK * R_K_analytic(s) / 2.0
h = 1e-7  # (local)
dV_fold = (V_KK(s_fold + h) - V_KK(s_fold - h)) / (2.0*h)

# Ricci flow force:
# ds/dt_RF at the fold (already computed)
RF_force_fold = ds_dt_RF

# Spectral action force (as acceleration on tau):
# From the EOM: G_mod * tau_ddot + ... = -dS_SA/dtau (schematically)
# The direction is: -dS_SA/dtau pushes tau
SA_force_direction = -dS_fold  # negative of gradient = force direction

# KK potential force:
# -dV/dtau is the force on the modulus
KK_force = -dV_fold

print(f"\n  At the fold (s = tau = {s_fold}):")
print(f"")
print(f"  1. RICCI FLOW projection onto Jensen direction:")
print(f"     ds/dt_RF = {RF_force_fold:.8f}")
print(f"     Direction: {'TOWARD s=0' if RF_force_fold < 0 else 'AWAY from s=0'}")
print(f"")
print(f"  2. SPECTRAL ACTION gradient:")
print(f"     dS_SA/dtau = {dS_fold:.2f}")
print(f"     Force -dS/dtau = {SA_force_direction:.2f}")
print(f"     Direction: {'TOWARD tau=0' if SA_force_direction < 0 else 'AWAY from tau=0'}")
print(f"")
print(f"  3. KK POTENTIAL gradient:")
print(f"     dV_KK/dtau = {dV_fold:.4f}")
print(f"     Force -dV/dtau = {KK_force:.4f}")
print(f"     Direction: {'TOWARD tau=0' if KK_force < 0 else 'AWAY from tau=0'}")

# Are they aligned?
RF_sign = np.sign(RF_force_fold)
SA_sign = np.sign(SA_force_direction)
KK_sign = np.sign(KK_force)

print(f"\n  ALIGNMENT:")
print(f"  Ricci flow sign: {'+' if RF_sign > 0 else '-'}")
print(f"  Spectral action sign: {'+' if SA_sign > 0 else '-'}")
print(f"  KK potential sign: {'+' if KK_sign > 0 else '-'}")
print(f"  RF vs SA: {'ALIGNED' if RF_sign == SA_sign else 'OPPOSED'}")
print(f"  RF vs KK: {'ALIGNED' if RF_sign == KK_sign else 'OPPOSED'}")
print(f"  SA vs KK: {'ALIGNED' if SA_sign == KK_sign else 'OPPOSED'}")

# ============================================================================
#  STEP 7: Normalized Ricci flow (volume-preserving)
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 7: Normalized (Volume-Preserving) Ricci Flow")
print(f"{'='*72}")

# The unnormalized Ricci flow changes the volume.
# The NORMALIZED Ricci flow preserves volume:
#   dg/dt = -2 Ric(g) + (2*R_avg/n) * g
# where R_avg = integral R / Vol and n = dim(G).
#
# For our diagonal metric:
#   d(log x_i)/dt = -2*r_i + (2*R_avg/8)
# where R_avg = (1*r1 + 3*r2 + 4*r3) / (1+3+4) * 8 = R (scalar curvature)
# Actually R_avg = R/8 for homogeneous spaces.
# The normalized flow:
#   d(log x_i)/dt = -2*r_i + R/4

R_scalar_fold = np.sum(ric_full_f)
norm_flow = np.array([-2.0*r_fold[i] + R_scalar_fold/4.0 for i in range(3)])

# Projection onto Jensen direction:
num_norm = np.sum(d_dims * norm_flow * c_jensen)
ds_dt_norm = num_norm / denominator

print(f"  R(fold) = {R_scalar_fold:.8f}")
print(f"  Normalized flow d(log x_i)/dt = -2*r_i + R/4:")
print(f"    u(1):  {norm_flow[0]:.8f}")
print(f"    su(2): {norm_flow[1]:.8f}")
print(f"    C^2:   {norm_flow[2]:.8f}")
print(f"  Normalized ds/dt_RF = {ds_dt_norm:.8f}")
print(f"  Direction: {'TOWARD s=0' if ds_dt_norm < 0 else 'AWAY from s=0'}")

# Compute normalized flow over full path
ds_dt_norm_values = np.zeros_like(s_values)
for idx, s in enumerate(s_values):
    R_s = R_ric_values[idx]
    r_vec = np.array([r1_values[idx], r2_values[idx], r3_values[idx]])
    nf = -2.0*r_vec + R_s/4.0
    ds_dt_norm_values[idx] = np.sum(d_dims * nf * c_jensen) / denominator

print(f"\n  Normalized ds/dt_RF along Jensen path:")
print(f"  {'s':>6s}  {'ds/dt_unorm':>14s}  {'ds/dt_norm':>14s}")
for idx in range(0, len(s_values), 5):
    print(f"  {s_values[idx]:6.3f}  {ds_dt_values[idx]:14.8f}  {ds_dt_norm_values[idx]:14.8f}")

# ============================================================================
#  STEP 8: Full 3D Ricci flow integration (not restricted to Jensen)
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 8: Full 3D Ricci Flow from the Fold")
print(f"{'='*72}")

# Solve the full 3-component ODE system:
# d(log x_i)/dt = -2 * r_i(x1, x2, x3) + R(x1,x2,x3)/4
# (normalized Ricci flow)

def ricci_flow_rhs(t, log_x):
    """RHS of normalized Ricci flow in log coordinates."""
    x1 = np.exp(log_x[0])
    x2 = np.exp(log_x[1])
    x3 = np.exp(log_x[2])

    r1, r2, r3, _, _, ric_full = ricci_on_su3(x1, x2, x3)
    R_scalar = np.sum(ric_full)

    d_log_x1 = -2.0*r1 + R_scalar/4.0
    d_log_x2 = -2.0*r2 + R_scalar/4.0
    d_log_x3 = -2.0*r3 + R_scalar/4.0

    return [d_log_x1, d_log_x2, d_log_x3]

# Initial condition: Jensen metric at the fold
x1_init, x2_init, x3_init = jensen_metric(s_fold)
log_x_init = [np.log(x1_init), np.log(x2_init), np.log(x3_init)]

print(f"  Initial condition (fold): x = ({x1_init:.6f}, {x2_init:.6f}, {x3_init:.6f})")
print(f"  log(x) = ({log_x_init[0]:.6f}, {log_x_init[1]:.6f}, {log_x_init[2]:.6f})")

# Integrate forward
sol_RF = solve_ivp(ricci_flow_rhs, [0, 50.0], log_x_init,
                   max_step=0.1, rtol=1e-10, atol=1e-12, method='RK45',
                   dense_output=True)

t_RF = sol_RF.t
x1_RF = np.exp(sol_RF.y[0])
x2_RF = np.exp(sol_RF.y[1])
x3_RF = np.exp(sol_RF.y[2])

# Extract the Jensen parameter s from the metric
# x1 = alpha * e^{2s}, x2 = alpha * e^{-2s}, x3 = alpha * e^s
# => s from x1: s = log(x1/alpha)/2
# => s from x2: s = -log(x2/alpha)/2
# => s from x3: s = log(x3/alpha)
# If the flow stays on the Jensen family, all three give the same s.
s_from_x1 = np.log(x1_RF / alpha) / 2.0
s_from_x2 = -np.log(x2_RF / alpha) / 2.0
s_from_x3 = np.log(x3_RF / alpha)

# Measure deviation from Jensen family
s_avg = (s_from_x1 + 3*s_from_x2 + 4*s_from_x3) / 8.0  # weighted average
s_spread = np.sqrt(((s_from_x1 - s_avg)**2 + 3*(s_from_x2 - s_avg)**2 + 4*(s_from_x3 - s_avg)**2) / 8.0)

print(f"\n  Ricci flow trajectory (selected points):")
print(f"  {'t_RF':>8s}  {'s_x1':>10s}  {'s_x2':>10s}  {'s_x3':>10s}  {'s_avg':>10s}  {'spread':>10s}")
stride = max(1, len(t_RF) // 15)
for idx in range(0, len(t_RF), stride):
    print(f"  {t_RF[idx]:8.3f}  {s_from_x1[idx]:10.6f}  {s_from_x2[idx]:10.6f}  {s_from_x3[idx]:10.6f}  {s_avg[idx]:10.6f}  {s_spread[idx]:10.6f}")

# Check: does s_avg decrease (flow toward bi-invariant)?
if len(t_RF) > 1:
    s_final = s_avg[-1]
    s_initial = s_avg[0]
    print(f"\n  s(t=0) = {s_initial:.6f}")
    print(f"  s(t_final={t_RF[-1]:.1f}) = {s_final:.6f}")
    print(f"  Delta_s = {s_final - s_initial:.6f}")
    print(f"  Ricci flow drives s {'TOWARD' if s_final < s_initial else 'AWAY FROM'} zero (bi-invariant)")

    # Is the flow approximately on the Jensen family?
    max_spread = np.max(s_spread)
    print(f"  Maximum Jensen deviation (spread) = {max_spread:.6f}")
    print(f"  Flow stays on Jensen: {'YES (spread < 0.01)' if max_spread < 0.01 else 'NO (significant deviation)'}")

# Volume check
vol_RF = x1_RF * x2_RF**3 * x3_RF**4
vol_0 = alpha**8
print(f"\n  Volume preservation check:")
print(f"  Vol(0)/Vol_0 = {vol_RF[0]/vol_0:.10f}")
print(f"  Vol(final)/Vol_0 = {vol_RF[-1]/vol_0:.10f}")

# ============================================================================
#  STEP 9: Ricci flow timescale vs physical timescale
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 9: Timescale Comparison")
print(f"{'='*72}")

# Ricci flow rate at fold: ds/dt_RF (computed above)
# Physical transit rate: tau_dot from the 12D reduction
# From s52_12d_reduction: the N_e = tau_fold * sqrt(G_DeWitt/6) analytic result
# tau_dot is determined by the initial kick, but the GEOMETRIC rate from
# the Ricci flow is ds/dt_RF.

# The Ricci flow timescale for tau to return to 0:
# tau_RF ~ |s_fold / ds_dt_RF| (crude linear estimate)
if abs(ds_dt_norm) > 1e-15:
    t_RF_return = abs(s_fold / ds_dt_norm)
    print(f"  Ricci flow rate at fold: ds/dt = {ds_dt_norm:.8f}")
    print(f"  Linear return time: t_RF ~ s_fold / |ds/dt| = {t_RF_return:.2f} (in curvature time units)")
else:
    t_RF_return = float('inf')
    print(f"  Ricci flow rate at fold: ds/dt = {ds_dt_norm:.8f} (essentially zero)")

# Physical transit timescale from canonical constants
dt_transit_phys = dt_transit   # canonical: 0.001130 M_KK^{-1} (S38)
v_terminal_phys = v_terminal   # canonical: 26.545 (S38)

print(f"\n  Physical transit: dt = {dt_transit_phys:.6f} M_KK^{{-1}}")
print(f"  Physical velocity: v_terminal = {v_terminal_phys:.3f}")
print(f"  Ricci flow velocity at fold: |ds/dt_RF| = {abs(ds_dt_norm):.8f}")
print(f"  Ratio v_physical / v_RF = {v_terminal_phys / abs(ds_dt_norm):.2f}" if abs(ds_dt_norm) > 1e-15 else "  v_RF ~ 0, ratio undefined")

# ============================================================================
#  STEP 10: Summary and Gate Verdict
# ============================================================================

print(f"\n{'='*72}")
print(f"  STEP 10: Summary and Gate Verdict")
print(f"{'='*72}")

# The key questions:
# 1. Does Ricci flow drive tau toward 0 (bi-invariant)?
# 2. Does it agree with the spectral action gradient?
# 3. What's the timescale comparison?

print(f"""
  RICCI-FLOW-52 RESULTS:
  ======================

  1. RICCI FLOW DIRECTION:
     At the fold (tau={s_fold}), the normalized Ricci flow projects onto
     the Jensen direction with ds/dt_RF = {ds_dt_norm:.8f}
     Direction: {'RESTORING (toward bi-invariant s=0)' if ds_dt_norm < 0 else 'DESTABILIZING (away from s=0)'}

  2. FULL 3D FLOW:
     Starting from the fold, the 3D normalized Ricci flow evolves s from
     {s_fold:.4f} to {s_final:.6f} over t_RF = {t_RF[-1]:.1f}
     Maximum Jensen deviation (spread) = {max_spread:.6f}
     {'Flow approximately stays on Jensen family' if max_spread < 0.01 else 'Flow deviates from Jensen family'}

  3. COMPARISON WITH SPECTRAL ACTION:
     Ricci flow force:     ds/dt_RF = {ds_dt_norm:.8f} ({'<0' if ds_dt_norm < 0 else '>0'})
     Spectral action force: -dS/dtau = {SA_force_direction:.2f} ({'<0' if SA_force_direction < 0 else '>0'})
     KK potential force:   -dV/dtau = {KK_force:.4f} ({'<0' if KK_force < 0 else '>0'})
     RF-SA alignment: {'ALIGNED' if RF_sign == SA_sign else 'OPPOSED'}
     RF-KK alignment: {'ALIGNED' if RF_sign == KK_sign else 'OPPOSED'}

  4. SCALAR CURVATURE CROSS-CHECK:
     At fold: R_from_Ric = {R_from_ric_f:.8f}, R_Baptista = {R_K_analytic(s_fold):.8f}
     Relative error: {abs(R_from_ric_f - R_K_analytic(s_fold))/abs(R_K_analytic(s_fold)):.2e}

  5. TIMESCALE:
     Ricci flow: |ds/dt| = {abs(ds_dt_norm):.6f} (curvature time^{{-1}})
     Physical transit: |dtau/dt| = {v_terminal_phys:.3f} M_KK
     Ratio: physical transit is {v_terminal_phys/abs(ds_dt_norm):.0f}x faster than Ricci flow

  GATE: INFO (Ricci flow direction analysis)
  VERDICT: The pure geometry (Ricci flow) {'AGREES' if RF_sign == SA_sign else 'DISAGREES'} with the spectral action gradient.
""")

# ============================================================================
#  SAVE DATA
# ============================================================================

np.savez(os.path.join(DATA_DIR, 's52_ricci_flow.npz'),
    # Jensen path data
    s_values=s_values,
    ds_dt_RF=ds_dt_values,
    ds_dt_RF_norm=ds_dt_norm_values,
    r1_values=r1_values,
    r2_values=r2_values,
    r3_values=r3_values,
    R_ric_values=R_ric_values,
    R_analytic_values=R_analytic_values,
    # At the fold
    s_fold=s_fold,
    ds_dt_RF_fold=RF_force_fold,
    ds_dt_RF_norm_fold=ds_dt_norm,
    r1_fold=r1_f, r2_fold=r2_f, r3_fold=r3_f,
    R_fold_ric=R_from_ric_f,
    R_fold_analytic=R_K_analytic(s_fold),
    # Comparison
    dS_SA_fold=dS_fold,
    dV_KK_fold=dV_fold,
    SA_force=SA_force_direction,
    KK_force=KK_force,
    RF_SA_aligned=(RF_sign == SA_sign),
    RF_KK_aligned=(RF_sign == KK_sign),
    # Full 3D flow
    t_RF=t_RF,
    x1_RF=x1_RF, x2_RF=x2_RF, x3_RF=x3_RF,
    s_from_x1=s_from_x1, s_from_x2=s_from_x2, s_from_x3=s_from_x3,
    s_avg_RF=s_avg, s_spread_RF=s_spread,
    vol_RF=vol_RF,
)
print(f"\n  Data saved to: s52_ricci_flow.npz")

# ============================================================================
#  PLOT
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S52 — RICCI-FLOW-52: Ricci Flow vs Modulus Dynamics on Jensen SU(3)', fontsize=13)

# Panel 1: Ricci eigenvalues along Jensen path
ax = axes[0, 0]
ax.plot(s_values, r1_values, 'b-', linewidth=2, label=r'$r_1$ (u(1))')
ax.plot(s_values, r2_values, 'r-', linewidth=2, label=r'$r_2$ (su(2))')
ax.plot(s_values, r3_values, 'g-', linewidth=2, label=r'$r_3$ ($\mathbb{C}^2$)')
ax.axvline(s_fold, color='gray', linestyle='--', alpha=0.5, label=f's = {s_fold} (fold)')
ax.set_xlabel(r'Jensen parameter $s = \tau$')
ax.set_ylabel('Ricci eigenvalue')
ax.set_title('Ricci Curvature Eigenvalues')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: ds/dt from Ricci flow
ax = axes[0, 1]
ax.plot(s_values, ds_dt_values, 'b-', linewidth=2, label='Unnormalized')
ax.plot(s_values, ds_dt_norm_values, 'r-', linewidth=2, label='Normalized (vol-pres)')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(s_fold, color='gray', linestyle='--', alpha=0.5, label=f's = {s_fold} (fold)')
ax.set_xlabel(r'Jensen parameter $s = \tau$')
ax.set_ylabel(r'$ds/dt_{RF}$')
ax.set_title('Ricci Flow Velocity Along Jensen Path')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Scalar curvature comparison
ax = axes[1, 0]
ax.plot(s_values, R_ric_values, 'b-', linewidth=2, label='R from Ric (numerical)')
ax.plot(s_values, R_analytic_values, 'r--', linewidth=2, label='R from Baptista (analytic)')
ax.axvline(s_fold, color='gray', linestyle='--', alpha=0.5, label=f's = {s_fold} (fold)')
ax.set_xlabel(r'Jensen parameter $s = \tau$')
ax.set_ylabel('Scalar curvature R')
ax.set_title('Scalar Curvature Cross-Check')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: Full 3D Ricci flow trajectory
ax = axes[1, 1]
ax.plot(t_RF, s_from_x1, 'b-', linewidth=1, alpha=0.7, label=r'$s$ from $x_1$ (u(1))')
ax.plot(t_RF, s_from_x2, 'r-', linewidth=1, alpha=0.7, label=r'$s$ from $x_2$ (su(2))')
ax.plot(t_RF, s_from_x3, 'g-', linewidth=1, alpha=0.7, label=r'$s$ from $x_3$ ($\mathbb{C}^2$)')
ax.plot(t_RF, s_avg, 'k-', linewidth=2, label=r'$s_{avg}$ (weighted)')
ax.axhline(0, color='black', linewidth=0.5, linestyle=':')
ax.axhline(s_fold, color='gray', linestyle='--', alpha=0.5, label=f's = {s_fold} (fold)')
ax.set_xlabel(r'Ricci flow time $t_{RF}$')
ax.set_ylabel(r'Jensen parameter $s$')
ax.set_title('Full 3D Normalized Ricci Flow from Fold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, 's52_ricci_flow.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved to: s52_ricci_flow.png")

print(f"\n{'='*72}")
print(f"  RICCI-FLOW-52 COMPLETE")
print(f"{'='*72}")
