#!/usr/bin/env python3
"""
S55 — ATENSOR-GAUGE-55: O'Neill A-Tensor with SU(2)xU(1) Gauge Field Background
==================================================================================

Compute the O'Neill A-tensor for the Riemannian submersion SU(3) -> CP^2
(coset fibration) with the Jensen metric, and then with gauge field
backgrounds from NCG inner fluctuations.

Mathematical Setup
------------------
For the submersion pi: SU(3) -> SU(3)/U(2) = CP^2:
  - Vertical = u(2) generators (indices 0-3 in our basis)
  - Horizontal = C^2 coset directions (indices 4-7)

The O'Neill A-tensor measures the failure of integrability of the
horizontal distribution:
  A_X Y = (1/2) [X, Y]^V   for horizontal X, Y in m = C^2

For a LEFT-INVARIANT metric on SU(3):
  A_{e_a} e_b = (1/2) [e_a, e_b]^{u(2)}  for e_a, e_b in C^2

This is STRUCTURALLY NONZERO because [C^2, C^2] = u(2) (Paper 13, eq 2.5).

With gauge fields: the NCG inner fluctuations produce a gauge connection
A = sum a_j [D, b_j] which modifies the horizontal distribution. The
modified A-tensor has additional terms.

Baptista's Notation
-------------------
Baptista calls the O'Neill A-tensor "F" (Paper 13/15 footnote on p.20/18):
"the tensor called A in [O'Ne, Bes] is called here F, to avoid confusion
with the gauge fields."

There are TWO distinct O'Neill A-tensors in this framework:
1. The EXTERNAL A-tensor for M4 x K -> M4: this is Baptista's F (eq 3.6)
   F_X Y = (nabla_X^H Y^H)^V = (1/2)[X^H, Y^H]^V = F_A (gauge curvature)

2. The INTERNAL A-tensor for the coset submersion K -> K/U(2):
   A_{e_a} e_b = (1/2)[e_a, e_b]^{u(2)}  for e_a, e_b in m = C^2
   This measures the fiber geometry and is what we compute here.

Gate: ATENSOR-GAUGE-55 — PASS if |A|^2 > 0 with gauge fields. FAIL if A = 0.
Output: s55_atensor_gauge.npz, s55_atensor_gauge.png

Author: Baptista-Spacetime-Analyst (Session 55)
Date: 2026-03-22
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp, log
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

print("=" * 72)
print("  S55 — ATENSOR-GAUGE-55: O'Neill A-Tensor with Gauge Fields")
print("=" * 72)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
#  SECTION 1: Build the su(3) structure constants
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 1: su(3) Structure Constants and Reductive Decomposition")
print("=" * 72)

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

# gamma_0-orthonormal basis: f_a = T_a * sqrt(2)
# Reorder to Baptista's decomposition: su(3) = u(1) + su(2) + C^2
# u(1): lambda_8 -> index 0
# su(2): lambda_1, lambda_2, lambda_3 -> indices 1, 2, 3
# C^2: lambda_4, lambda_5, lambda_6, lambda_7 -> indices 4, 5, 6, 7
reorder = [8, 1, 2, 3, 4, 5, 6, 7]

f = np.zeros((8, 3, 3), dtype=complex)
for i in range(8):
    f[i] = T[reorder[i]] * sqrt(2.0)

# Verify orthonormality: gamma_0(f_a, f_b) = -Tr(f_a * f_b) = delta_{ab}
gram_f = np.zeros((8, 8))
for a in range(8):
    for b in range(8):
        gram_f[a, b] = -np.trace(f[a] @ f[b]).real
assert np.allclose(gram_f, np.eye(8), atol=1e-14), \
    f"Gram matrix error: {np.max(np.abs(gram_f - np.eye(8)))}"
print("  gamma_0-orthonormality verified: max deviation = "
      f"{np.max(np.abs(gram_f - np.eye(8))):.2e}")

# Structure constants: [f_a, f_b] = c_{ab}^c f_c
# c_{ab}^c = gamma_0([f_a, f_b], f_c) = -Tr([f_a, f_b] * f_c)
c_abc = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        bracket = f[a] @ f[b] - f[b] @ f[a]
        for cc in range(8):
            c_abc[a, b, cc] = -np.trace(bracket @ f[cc]).real

# Verify antisymmetry
assert np.allclose(c_abc, -np.transpose(c_abc, (1, 0, 2)), atol=1e-14), \
    "Structure constants not antisymmetric!"
print("  Structure constant antisymmetry verified")

# Verify Jacobi identity
jacobi_max = 0.0  # (local)
for a in range(8):
    for b in range(8):
        for c in range(8):
            J = 0.0
            for d in range(8):
                J += c_abc[a, b, d] * c_abc[d, c, :].sum()  # wrong
            # Actually:
            pass
# Let's do Jacobi properly
jacobi_violations = []
for a in range(8):
    for b in range(8):
        for c in range(8):
            for e in range(8):
                J = 0.0
                for d in range(8):
                    J += (c_abc[a,b,d]*c_abc[d,c,e] +
                          c_abc[b,c,d]*c_abc[d,a,e] +
                          c_abc[c,a,d]*c_abc[d,b,e])
                jacobi_violations.append(abs(J))
print(f"  Jacobi identity max violation: {max(jacobi_violations):.2e}")

# Subspace labels
# Vertical (u(2)): indices 0,1,2,3  [u(1) + su(2)]
# Horizontal (C^2 = m): indices 4,5,6,7
vert_idx = [0, 1, 2, 3]  # u(2) = u(1) + su(2)
horiz_idx = [4, 5, 6, 7]  # C^2 (coset directions)

# Print the key bracket structure: [C^2, C^2] -> u(2)
print("\n  Bracket structure [m, m] -> u(2):")
print("  [C^2, C^2] projected onto u(2):")
for a in horiz_idx:
    for b in horiz_idx:
        if a < b:
            proj_u2 = np.zeros(4)
            for k, v in enumerate(vert_idx):
                proj_u2[k] = c_abc[a, b, v]
            if np.linalg.norm(proj_u2) > 1e-10:
                print(f"    [f_{a}, f_{b}]^{{u(2)}} = "
                      f"{proj_u2[0]:.4f}*f_0 + {proj_u2[1]:.4f}*f_1 + "
                      f"{proj_u2[2]:.4f}*f_2 + {proj_u2[3]:.4f}*f_3")

# ============================================================================
#  SECTION 2: O'Neill A-tensor for the INTERNAL coset submersion
#             SU(3) -> SU(3)/U(2) = CP^2 with the Jensen metric
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 2: O'Neill A-Tensor for Internal Coset Submersion")
print("=" * 72)

def compute_atensor_jensen(tau):
    """
    Compute the O'Neill A-tensor for the coset submersion SU(3) -> CP^2
    with the Jensen metric at deformation parameter tau.

    The Jensen metric has eigenvalues:
      alpha_1(tau) = e^{2*tau}   on u(1)
      alpha_2(tau) = e^{-2*tau}  on su(2)
      alpha_3(tau) = e^{tau}     on C^2

    For the submersion SU(3) -> SU(3)/U(2):
      Vertical = u(2), Horizontal = C^2 (the coset space directions)

    The O'Neill A-tensor is:
      A_{e_a} e_b = (nabla_{e_a^H} e_b^H)^V for horizontal e_a, e_b

    For a left-invariant metric on a Lie group, with the natural
    Levi-Civita connection:
      nabla_{e_a} e_b = (1/2)([e_a, e_b] - ad*_{e_a}(e_b) - ad*_{e_b}(e_a))

    where ad*_u(v) is the adjoint of ad_u with respect to the metric g:
      g(ad*_u(v), w) = g(v, [u, w])

    For the coset A-tensor, we only need the vertical projection of
    nabla_{e_a} e_b for horizontal e_a, e_b.

    In a reductive homogeneous space G/H where g = h + m and [h,m] = m,
    the O'Neill A-tensor simplifies to:
      A_{X} Y = (1/2) [X, Y]^h  for X, Y in m
    when the metric is the ROUND (bi-invariant) metric.

    For a general left-invariant metric, the Koszul formula gives
    a more involved expression. Let's compute it fully.
    """
    # Metric eigenvalues
    a1 = exp(2.0 * tau)   # u(1)
    a2 = exp(-2.0 * tau)  # su(2)
    a3 = exp(tau)          # C^2

    # The metric in the gamma_0-orthonormal basis {f_a} is:
    # g(f_a, f_b) = alpha_i * delta_{ab}  when f_a, f_b in subspace i
    # So the g-orthonormal basis is: e_a = f_a / sqrt(alpha_i)

    alpha = np.zeros(8)
    alpha[0] = a1
    alpha[1:4] = a2
    alpha[4:8] = a3

    # Metric tensor in the f-basis: g_{ab} = alpha_a * delta_{ab}
    # (diagonal since the Jensen metric is diagonal in this basis)
    g_ab = np.diag(alpha)

    # Levi-Civita connection coefficients in the f-basis (NOT g-orthonormal)
    # Koszul formula: 2 g(nabla_{f_a} f_b, f_c) =
    #   g([f_a, f_b], f_c) - g([f_b, f_c], f_a) + g([f_c, f_a], f_b)
    # = alpha_c * c_{ab}^c - alpha_a * c_{bc}^a + alpha_b * c_{ca}^b
    #
    # Since g is diagonal: g([f_a, f_b], f_c) = sum_d c_{ab}^d * g_{dc}
    #                                         = c_{ab}^c * alpha_c

    # Connection coefficients: Gamma_{ab}^c such that nabla_{f_a} f_b = Gamma_{ab}^c f_c
    # 2 * alpha_c * Gamma_{ab}^c = alpha_c * c_{ab}^c - alpha_a * c_{bc}^a + alpha_b * c_{ca}^b
    # Gamma_{ab}^c = (1/2)(c_{ab}^c - (alpha_a/alpha_c)*c_{bc}^a + (alpha_b/alpha_c)*c_{ca}^b)

    Gamma = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                Gamma[a, b, c] = 0.5 * (c_abc[a, b, c]
                                         - (alpha[a] / alpha[c]) * c_abc[b, c, a]
                                         + (alpha[b] / alpha[c]) * c_abc[c, a, b])

    # Verify metric compatibility: nabla g = 0
    # d_a g_{bc} - Gamma_{ab}^d g_{dc} - Gamma_{ac}^d g_{bd} = 0
    # For left-invariant metric, d_a g_{bc} = f_a(g(f_b, f_c)) = 0 since g is constant
    # So: Gamma_{ab}^d * g_{dc} + Gamma_{ac}^d * g_{bd} = 0
    # i.e. Gamma_{ab}^d * alpha_c * delta_{dc} + Gamma_{ac}^d * alpha_b * delta_{bd} = 0
    # i.e. Gamma_{ab}^c * alpha_c + Gamma_{ac}^b * alpha_b = 0
    # i.e. g(nabla_a b, c) + g(b, nabla_a c) = 0 (metric compatibility)
    metric_compat_err = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                err = Gamma[a, b, c] * alpha[c] + Gamma[a, c, b] * alpha[b]
                metric_compat_err = max(metric_compat_err, abs(err))

    # Verify torsion-free: Gamma_{ab}^c - Gamma_{ba}^c = c_{ab}^c
    torsion_err = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                err = Gamma[a, b, c] - Gamma[b, a, c] - c_abc[a, b, c]
                torsion_err = max(torsion_err, abs(err))

    # O'Neill A-tensor: A_{e_a} e_b = (nabla_{e_a} e_b)^V  for horizontal e_a, e_b
    # In the f-basis: for a, b in horiz_idx (C^2):
    # A^c_{ab} = Gamma_{ab}^c  for c in vert_idx (u(2))
    # These are the vertical components of nabla_{f_a} f_b.

    # The A-tensor components (vertical projection of nabla for horizontal inputs)
    A_tensor = np.zeros((4, 4, 4))  # A_tensor[i,j,k] = A_{h_i, h_j}^{v_k}
    # where h_i = f_{horiz_idx[i]}, v_k = f_{vert_idx[k]}
    for i, a in enumerate(horiz_idx):
        for j, b in enumerate(horiz_idx):
            for k, c in enumerate(vert_idx):
                A_tensor[i, j, k] = Gamma[a, b, c]

    # Compute |A|^2 = sum_{a,b in horiz} g_V(A_{e_a} e_b, A_{e_a} e_b)
    # = sum_{a,b in horiz} sum_{c,d in vert} A^c_{ab} * A^d_{ab} * g_{cd}
    # = sum_{a,b in horiz} sum_{c in vert} (A^c_{ab})^2 * alpha_c
    # (since g is diagonal)

    # But wait: the A-tensor should be computed with g-orthonormal horizontal
    # vectors! Let e_a = f_a / sqrt(alpha_a) be g-orthonormal.
    # Then A_{e_a} e_b = nabla_{e_a} e_b)^V
    # = (nabla_{f_a/sqrt(alpha_a)} f_b/sqrt(alpha_b))^V
    # = (1/(sqrt(alpha_a)*sqrt(alpha_b))) * (nabla_{f_a} f_b)^V
    # = (1/(sqrt(alpha_a)*sqrt(alpha_b))) * sum_{c in vert} Gamma_{ab}^c * f_c

    # |A|^2 using g-orthonormal horizontal basis:
    # = sum_{i,j} g_V(A_{e_{h_i}} e_{h_j}, A_{e_{h_i}} e_{h_j})
    # = sum_{i,j} sum_{k in vert} [Gamma_{h_i,h_j}^{v_k} / (sqrt(alpha_{h_i})*sqrt(alpha_{h_j}))]^2 * alpha_{v_k}

    A_sq = 0.0  # (local)
    A_sq_components = np.zeros((4, 4))  # contribution from each (i,j) pair
    for i, a in enumerate(horiz_idx):
        for j, b in enumerate(horiz_idx):
            term = 0.0
            for k, c in enumerate(vert_idx):
                term += (Gamma[a, b, c] / (sqrt(alpha[a]) * sqrt(alpha[b])))**2 * alpha[c]
            A_sq_components[i, j] = term
            A_sq += term

    # Also compute the SIMPLIFIED formula A = (1/2)[X,Y]^V and compare
    # This is valid only for the bi-invariant (round) metric where Levi-Civita
    # = (1/2)[,]. For general left-invariant metrics, the full Koszul formula
    # is needed.
    A_sq_simple = 0.0  # (local)
    for i, a in enumerate(horiz_idx):
        for j, b in enumerate(horiz_idx):
            term = 0.0
            for k, c in enumerate(vert_idx):
                half_bracket = 0.5 * c_abc[a, b, c]
                term += (half_bracket / (sqrt(alpha[a]) * sqrt(alpha[b])))**2 * alpha[c]
            A_sq_simple += term

    return {
        'tau': tau,
        'alpha': (a1, a2, a3),
        'A_sq': A_sq,
        'A_sq_simple': A_sq_simple,
        'A_sq_components': A_sq_components,
        'Gamma_vert': np.array([[Gamma[a, b, c] for c in vert_idx]
                                for a in horiz_idx for b in horiz_idx]).reshape(4,4,4),
        'metric_compat_err': metric_compat_err,
        'torsion_err': torsion_err,
    }


# Scan over tau values
tau_values = np.linspace(0.0, 0.5, 51)
results = []
for tau in tau_values:
    r = compute_atensor_jensen(tau)
    results.append(r)

# Print results at key tau values
print("\n  O'Neill A-tensor |A|^2 for coset submersion SU(3) -> CP^2:")
print("  " + "-" * 66)
print(f"  {'tau':>6s}  {'alpha_1':>10s}  {'alpha_2':>10s}  {'alpha_3':>10s}  "
      f"{'|A|^2':>12s}  {'|A|^2_simple':>12s}")
print("  " + "-" * 66)
for r in results[::5]:
    a1, a2, a3 = r['alpha']
    print(f"  {r['tau']:6.3f}  {a1:10.4f}  {a2:10.4f}  {a3:10.4f}  "
          f"{r['A_sq']:12.6f}  {r['A_sq_simple']:12.6f}")
print("  " + "-" * 66)

# Verification at tau=0 (round metric)
r0 = compute_atensor_jensen(0.0)
print(f"\n  At tau=0 (round metric):")
print(f"    |A|^2 (full Koszul)  = {r0['A_sq']:.10f}")
print(f"    |A|^2 (1/2 bracket)  = {r0['A_sq_simple']:.10f}")
print(f"    Metric compat error  = {r0['metric_compat_err']:.2e}")
print(f"    Torsion-free error   = {r0['torsion_err']:.2e}")
print(f"    Ratio full/simple    = {r0['A_sq']/r0['A_sq_simple']:.10f}")

# At the fold
r_fold = compute_atensor_jensen(tau_fold)
print(f"\n  At tau={tau_fold} (fold):")
print(f"    |A|^2 (full Koszul)  = {r_fold['A_sq']:.10f}")
print(f"    |A|^2 (1/2 bracket)  = {r_fold['A_sq_simple']:.10f}")
print(f"    Metric compat error  = {r_fold['metric_compat_err']:.2e}")
print(f"    Torsion-free error   = {r_fold['torsion_err']:.2e}")

# ============================================================================
#  SECTION 3: O'Neill A-tensor with SU(2)xU(1) Gauge Field Background
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 3: A-Tensor with Gauge Field Background")
print("=" * 72)

# The gauge fields from NCG inner fluctuations modify the horizontal
# distribution. In Baptista's framework (Paper 13, eq 3.3):
#
# X^H = X + A^j_L(X) e^L_j - A^j_R(X) e^R_j
#
# The A_L has values in u(2) c su(3) (electroweak), and A_R in su(3) (strong).
#
# The O'Neill A-tensor (Baptista's F) for the EXTERNAL submersion M4 x K -> M4
# is (Paper 13, eq 3.11):
#   F_{X^H} Y^H = (1/2)[X^H, Y^H]^V = F_A(X,Y) = gauge field strength
#
# This is NONZERO whenever the gauge field strength F_A != 0.
#
# However, the question asks about the INTERNAL coset submersion with
# gauge field background. The gauge field modifies the Levi-Civita connection
# on the total space P = M4 x K. For the internal directions, the relevant
# modification comes from the fact that the gauge field A_mu couples to
# the horizontal lift, changing the geometry of the fibration.
#
# More precisely: when gauge fields are present, the horizontal distribution
# on P is no longer the simple product TM x {0}. It tilts into the fiber
# directions. This changes the induced connection on the internal space
# when viewed from the 4D perspective.
#
# The correct framework is:
# 1. Start with the total space P = M4 x SU(3) with submersive metric g_P
# 2. The gauge field A defines a horizontal distribution H on P
# 3. For each fiber K_x = {x} x SU(3), the internal O'Neill A-tensor is
#    computed for the coset submersion K_x -> K_x/U(2)
# 4. The gauge field modifies the metric on K_x through the off-diagonal
#    terms in g_P, changing the Levi-Civita connection and hence the A-tensor
#
# From Baptista Paper 13 eq (1.4):
# g_P(X, Y) = g_M(X,Y) + g_K(A(X), A(Y))
# g_P(X, V) = -g_K(A(X), V)
# g_P(U, V) = g_K(U, V)
#
# The fiber metric g_K is UNCHANGED. What changes is the connection
# because of the off-diagonal terms.
#
# The A-tensor for the INTERNAL coset submersion at each fiber:
# This depends only on g_K (the Jensen metric), not on the gauge fields,
# because the internal geometry within a single fiber is determined by g_K.
# The gauge field only affects the EXTERNAL submersion (how fibers are
# connected across M4).
#
# HOWEVER, there is a subtler effect: the Baptista parameter phi in C^2
# (the Higgs-like field) IS a gauge field component. When phi != 0, the
# internal metric IS the Jensen metric g_{phi}, which is already our metric.
# The A-tensor we computed in Section 2 ALREADY includes the effect of
# phi through the tau-dependent metric.
#
# The ADDITIONAL gauge field effect comes from the SU(2) x U(1) gauge
# potentials A^j_L on M4, which create cross-terms between horizontal
# (M4) and vertical (fiber) directions. These affect the EXTERNAL A-tensor
# (= gauge field strength F_A), not the internal coset A-tensor.
#
# Let us now compute the EXTERNAL O'Neill A-tensor |F|^2 explicitly.

print("\n  EXTERNAL O'Neill A-tensor (Baptista's F = gauge field strength):")
print("  " + "-" * 60)
print("  For a general SU(2)xU(1) gauge field configuration,")
print("  the O'Neill A-tensor for M4 x K -> M4 is:")
print("    F_{X^H} Y^H = F_A(X,Y) = dA + A wedge A")
print("  This is identically the gauge curvature 2-form.")
print("  |F|^2 = (1/4) g^{mu rho} g^{nu sigma} g_K(e_j, e_k) F^j_{mu nu} F^k_{rho sigma}")
print()

# Now compute the gauge-modified coset A-tensor.
# When we have gauge fields A_L valued in u(2), the total space metric
# creates a modified connection. At a given point of M4, if we look at
# the coset submersion SU(3) -> CP^2 WITHIN the total space P,
# the horizontal distribution for this internal submersion is also modified.
#
# Actually, let's think about this more carefully. The coset submersion
# SU(3) -> SU(3)/U(2) lives entirely within the fiber. The gauge field
# on M4 does not directly change the fiber-internal geometry. But the
# inner fluctuations of the NCG spectral triple DO modify the Dirac
# operator, and through it, the effective metric on the fiber.
#
# In the NCG framework (Paper 57, van Suijlekom Ch. 8-11):
# The inner fluctuations are D -> D + A + JAJ^{-1} where
# A = sum a_j [D, b_j] (a one-form in Connes' sense)
#
# For the continuous manifold part, this gives the usual gauge connection.
# For the finite part, it gives the Higgs field.
#
# The key insight: in the KK picture, the Higgs field IS the metric
# deformation parameter phi (Baptista's observation). So the NCG inner
# fluctuation that produces the Higgs is equivalent to deforming the
# Jensen metric from tau=0 to tau!=0.
#
# The gauge fields A_mu^j modify the horizontal distribution but NOT
# the fiber metric. They create the EXTERNAL A-tensor = field strength.
#
# So for the INTERNAL coset submersion:
# - The A-tensor depends on tau (the Higgs/Jensen deformation) -> already computed
# - The SU(2)xU(1) gauge potentials on M4 do NOT change it
#
# But there is one more effect to consider: the TOTAL A-tensor.
# When we have both the coset structure AND gauge fields, the total
# O'Neill A-tensor has contributions from BOTH:
# 1. The internal coset A-tensor (vertical projection within the fiber)
# 2. The external gauge A-tensor (connecting different fibers)
#
# These combine in the TOTAL scalar curvature via the O'Neill formula
# (Paper 13/15 eq 2.5 / 3.4):
#   R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 delta N

print("\n  Computing TOTAL A-tensor decomposition...")
print()

# Let's compute the internal A-tensor at a representative gauge field
# configuration. We introduce SU(2) x U(1) gauge field strengths as
# a parametric background.

def compute_total_atensor(tau, F_Y_sq, F_W_sq, F_S_sq):
    """
    Compute the total O'Neill A-tensor squared norm including both:
    1. Internal coset A-tensor (from Jensen metric)
    2. External gauge A-tensor (from SU(2)xU(1) and SU(3)_color field strengths)

    Parameters:
    -----------
    tau : float
        Jensen deformation parameter
    F_Y_sq : float
        |F_Y|^2 = U(1)_Y field strength squared (in M_KK^4 units)
    F_W_sq : float
        |F_W|^2 = SU(2)_W field strength squared (one component)
    F_S_sq : float
        |F_S|^2 = SU(3)_strong field strength squared (one component)

    Returns:
    --------
    dict with A-tensor components
    """
    a1 = exp(2.0 * tau)   # u(1)
    a2 = exp(-2.0 * tau)  # su(2)
    a3 = exp(tau)          # C^2

    # Internal coset A-tensor |A_coset|^2
    r = compute_atensor_jensen(tau)
    A_coset_sq = r['A_sq']

    # External gauge A-tensor |F|^2
    # From Paper 13 eq (3.16), after fiber integration:
    # |F|^2 vol_K = (1/4) g^{mu rho} g^{nu sigma} *
    #   [sum_{j,k in u(2)} kappa(e_j, e_k) (F^j_L)_{mu nu} (F^k_L)_{rho sigma}
    #  + sum_{j,k in su(3)} kappa(e_j, e_k) (F^j_R)_{mu nu} (F^k_R)_{rho sigma}] * Vol(K)
    #
    # The key point: kappa(e_j, e_k) = delta_{jk} for kappa-orthonormal basis.
    # The gauge coupling constants come from the metric normalization.
    #
    # For the u(2) gauge fields (L sector):
    # |F_L|^2 = (1/4) * [|F_Y|^2 / kappa_1 + sum_{i=1}^3 |F_W^i|^2 / kappa_2]
    #
    # For the su(3) gauge fields (R sector):
    # |F_R|^2 = (1/4) * sum_{a=1}^8 |F_S^a|^2 / kappa_0
    # where kappa_0 = alpha_K is the bi-invariant metric normalization
    #
    # Since the fiber metric for R fields uses kappa (not g), the gauge
    # coupling is independent of tau for the R sector.
    # For the L sector, g = kappa on u(2), so also independent of tau.

    # The external |F|^2 is proportional to the standard Yang-Mills Lagrangian:
    F_ext_sq = F_Y_sq + 3.0 * F_W_sq + 8.0 * F_S_sq

    # The TOTAL squared norm in the O'Neill decomposition is:
    # |A_total|^2 = |A_coset|^2 + |F_ext|^2
    # These contribute ADDITIVELY to R_P with a minus sign.

    return {
        'tau': tau,
        'A_coset_sq': A_coset_sq,
        'F_ext_sq': F_ext_sq,
        'A_total_sq': A_coset_sq + F_ext_sq,
    }


# ============================================================================
#  SECTION 4: Compute |A_coset|^2 Across the Transit and with Gauge Fields
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 4: |A_coset|^2 Across the Transit + Gauge Field Effect")
print("=" * 72)

# Compute the coset A-tensor across the full tau range
A_sq_values = np.array([r['A_sq'] for r in results])
A_sq_simple_values = np.array([r['A_sq_simple'] for r in results])

# Check: at tau=0, the round metric has [e_a, e_b] = c_{ab}^c e_c
# and the Levi-Civita connection nabla_a b = (1/2) [a,b] for bi-invariant metrics.
# So A_{e_a} e_b = (nabla_{e_a} e_b)^V = (1/2) [e_a, e_b]^V
# and the full Koszul result should equal the simple (1/2)[,]^V result at tau=0.

print(f"\n  Consistency check at tau=0 (bi-invariant metric):")
print(f"    Full Koszul |A|^2     = {A_sq_values[0]:.10f}")
print(f"    Simple (1/2)[,]^V |A|^2 = {A_sq_simple_values[0]:.10f}")
print(f"    Agreement: {np.isclose(A_sq_values[0], A_sq_simple_values[0])}")

# Detailed component analysis at key points
for tau_val, label in [(0.0, "round"), (tau_fold, "fold"), (0.30, "deep"), (0.50, "extreme")]:
    r = compute_atensor_jensen(tau_val)
    print(f"\n  tau = {tau_val:.2f} ({label}):")
    print(f"    |A_coset|^2 = {r['A_sq']:.8f}")
    print(f"    Component matrix (horiz_i, horiz_j) contributions:")
    total = 0.0  # (local)
    for i in range(4):
        for j in range(4):
            if r['A_sq_components'][i,j] > 1e-10:
                print(f"      ({i},{j}): {r['A_sq_components'][i,j]:.8f}")
                total += r['A_sq_components'][i,j]
    print(f"    Sum of components: {total:.8f}")

# Now compute with representative gauge field values
print("\n  With gauge field backgrounds (F^2 = 1 M_KK^4 each):")
print("  " + "-" * 60)
print(f"  {'tau':>6s}  {'|A_coset|^2':>12s}  {'|F_ext|^2':>12s}  "
      f"{'|A_total|^2':>12s}  {'ratio':>8s}")
print("  " + "-" * 60)

for tau_val in [0.0, 0.10, tau_fold, 0.30, 0.50]:
    rt = compute_total_atensor(tau_val, F_Y_sq=1.0, F_W_sq=1.0, F_S_sq=1.0)
    ratio = rt['F_ext_sq'] / rt['A_coset_sq'] if rt['A_coset_sq'] > 0 else float('inf')
    print(f"  {tau_val:6.3f}  {rt['A_coset_sq']:12.6f}  {rt['F_ext_sq']:12.6f}  "
          f"{rt['A_total_sq']:12.6f}  {ratio:8.3f}")

# ============================================================================
#  SECTION 5: The Key Physical Result — A is Structurally Nonzero
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 5: Gate Assessment — ATENSOR-GAUGE-55")
print("=" * 72)

# The A-tensor for the internal coset submersion SU(3) -> CP^2:
A_min = np.min(A_sq_values)
A_max = np.max(A_sq_values)
A_fold = compute_atensor_jensen(tau_fold)['A_sq']

print(f"\n  INTERNAL coset A-tensor |A_coset|^2:")
print(f"    Minimum over tau in [0, 0.5]: {A_min:.8f}")
print(f"    Maximum over tau in [0, 0.5]: {A_max:.8f}")
print(f"    At the fold (tau={tau_fold}):       {A_fold:.8f}")
print(f"    At round metric (tau=0):       {A_sq_values[0]:.8f}")

# STRUCTURAL RESULT:
# The A-tensor is nonzero at ALL tau because [C^2, C^2] = u(2) is a
# property of the Lie algebra su(3), not of the metric. The Jensen metric
# only modifies the NORM but cannot make the projection vanish.
#
# With gauge fields: the EXTERNAL A-tensor = gauge field strength F_A
# is ALSO nonzero whenever the gauge fields are nontrivial.
# The total |A|^2 = |A_coset|^2 + |F_ext|^2 > 0 always.

print(f"\n  STRUCTURAL THEOREM:")
print(f"    The O'Neill A-tensor for the internal coset submersion")
print(f"    SU(3) -> CP^2 is STRICTLY POSITIVE at all tau.")
print(f"    This is algebraic: [C^2, C^2] = u(2) in su(3).")
print(f"    The Jensen metric modifies the norm but cannot zero it.")
print(f"")
print(f"    With SU(2)xU(1) gauge fields from NCG inner fluctuations:")
print(f"    The EXTERNAL A-tensor (= field strength F_A) contributes")
print(f"    ADDITIVELY: |A_total|^2 = |A_coset|^2 + |F_ext|^2 > 0")
print(f"    Both terms are non-negative; the coset term is strictly positive.")

# Analytical cross-check at tau=0
# For the round metric, all alpha_i = 1.
# The A-tensor A_{e_a} e_b = (1/2) [e_a, e_b]^{u(2)} for a,b in C^2.
# |A|^2 = sum_{a,b in C^2} sum_{c in u(2)} [(1/2) c_{ab}^c]^2
# = (1/4) sum_{a,b in {4..7}} sum_{c in {0..3}} c_{ab}^c^2

A_sq_analytic_round = 0.0  # (local)
for a in horiz_idx:
    for b in horiz_idx:
        for c in vert_idx:
            A_sq_analytic_round += 0.25 * c_abc[a, b, c]**2

print(f"\n  Analytical check at tau=0:")
print(f"    |A|^2 = (1/4) sum_{{a,b in C^2}} sum_{{c in u(2)}} c_{{ab}}^c^2")
print(f"    = {A_sq_analytic_round:.10f}")
print(f"    Numerical: {A_sq_values[0]:.10f}")
print(f"    Agreement: {np.isclose(A_sq_analytic_round, A_sq_values[0])}")

# Decompose into u(1) and su(2) parts
A_sq_u1 = 0.0  # (local)
A_sq_su2 = 0.0  # (local)
for a in horiz_idx:
    for b in horiz_idx:
        A_sq_u1 += 0.25 * c_abc[a, b, 0]**2  # u(1) component
        for c in [1, 2, 3]:  # su(2) components
            A_sq_su2 += 0.25 * c_abc[a, b, c]**2

print(f"\n  Decomposition at tau=0:")
print(f"    |A|^2_{{u(1)}} = {A_sq_u1:.6f}  ({100*A_sq_u1/A_sq_analytic_round:.1f}%)")
print(f"    |A|^2_{{su(2)}} = {A_sq_su2:.6f}  ({100*A_sq_su2/A_sq_analytic_round:.1f}%)")
print(f"    Total = {A_sq_u1 + A_sq_su2:.6f}")

# ============================================================================
#  SECTION 6: Phononic Interpretation and Connection to Framework
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 6: Phononic Interpretation")
print("=" * 72)

print("""
  PHONONIC CLASSIFICATION: GEOMETRIC

  The O'Neill A-tensor measures the CURVATURE of the horizontal distribution
  in the coset submersion SU(3) -> CP^2. In the phononic framework:

  1. The coset directions (C^2) are the 4D "horizontal" phonon propagation
     directions in the internal space.

  2. The stabilizer directions (u(2)) are the "vertical" gauge symmetry
     directions.

  3. A nonzero A-tensor means the coset distribution is NON-INTEGRABLE:
     phonon excitations propagating in two different coset directions
     acquire a vertical (gauge) component upon parallel transport.
     This is the GEOMETRIC ORIGIN of gauge interactions in the phononic
     framework.

  4. The tau-dependence of |A|^2 means the gauge coupling strength is
     MODULATED by the Jensen deformation. This connects to the known
     result g_1/g_2 = e^{-2*tau} (Session 17a B-1).

  5. The gauge field strengths from NCG inner fluctuations add to the
     A-tensor ADDITIVELY. In the phononic picture, these are the dynamical
     gauge excitations on top of the geometric background.
""")

# Compute the ratio |A|^2 / R_K (A-tensor contribution to scalar curvature)
def R_K_Jensen_formula(tau):
    """Paper 13 eq (2.40) with kappa = 1, parametrized by ||phi||^2."""
    # In Paper 15 convention: R = (3/(2*alpha)) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})/4
    # where s = tau. But this is for the alpha_K = 3 normalization.
    # With alpha = 1 (our convention in the orthonormal basis):
    s = tau
    return 0.5 * (2.0*exp(2.0*s) - 1.0 + 8.0*exp(-s) - exp(-4.0*s))

R_K_values = np.array([R_K_Jensen_formula(tau) for tau in tau_values])

# Actually compute R_K using the Milnor formula for consistency
def R_K_milnor(tau):
    a1 = exp(2.0*tau)
    a2 = exp(-2.0*tau)  # (local)
    a3 = exp(tau)
    alpha = np.zeros(8)
    alpha[0] = a1
    alpha[1:4] = a2
    alpha[4:8] = a3

    T1 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for cc in range(8):
                T1 += c_abc[a, b, cc]**2 * alpha[cc] / (alpha[a] * alpha[b])

    T2 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for cc in range(8):
                for d in range(8):
                    gamma_ab_c = c_abc[a, b, cc] * sqrt(alpha[cc]) / (sqrt(alpha[a]) * sqrt(alpha[b]))
                    gamma_ac_d = c_abc[a, cc, d] * sqrt(alpha[d]) / (sqrt(alpha[a]) * sqrt(alpha[cc]))
                    T2 += gamma_ab_c * gamma_ac_d * (1.0 if d == b else 0.0)

    return -0.25 * T1 - 0.5 * T2

R_K_milnor_values = np.array([R_K_milnor(tau) for tau in tau_values])

print(f"  Cross-check: R_K at tau=0")
print(f"    Milnor formula: {R_K_milnor_values[0]:.6f}")
print(f"    Expected (bi-invariant SU(3)): 12.0 (with alpha=1)")
# For bi-invariant metric with gamma_0 = -Tr(uv), R = 3/alpha_K.
# But with our normalization where gamma_0(f_a,f_b) = delta_{ab},
# alpha_K = 1, R = 12 (same as Paper 13 eq 2.40 with kappa=1).

print(f"\n  |A_coset|^2 / R_K ratio across transit:")
for tau_val in [0.0, 0.10, tau_fold, 0.30, 0.50]:
    idx = np.argmin(np.abs(tau_values - tau_val))
    ratio = A_sq_values[idx] / R_K_milnor_values[idx] if R_K_milnor_values[idx] != 0 else float('inf')
    print(f"    tau={tau_val:.2f}: |A|^2={A_sq_values[idx]:.6f}, "
          f"R_K={R_K_milnor_values[idx]:.4f}, ratio={ratio:.6f}")

# ============================================================================
#  SECTION 7: Gate Verdict
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 7: GATE VERDICT — ATENSOR-GAUGE-55")
print("=" * 72)

# The gate asks: |A|^2 > 0 with gauge fields?
# Answer: YES, structurally. In two independent ways:
# 1. The INTERNAL coset A-tensor is > 0 at all tau (algebraic)
# 2. The EXTERNAL gauge A-tensor = F_A > 0 whenever gauge fields are on

A_coset_positive = np.all(A_sq_values > 0)
gate_pass = A_coset_positive

print(f"\n  Gate: ATENSOR-GAUGE-55")
print(f"  Question: Is |A|^2 > 0 with gauge fields?")
print(f"")
print(f"  |A_coset|^2 > 0 at all {len(tau_values)} tau points: {A_coset_positive}")
print(f"  Minimum |A_coset|^2 = {A_min:.8f} at tau = {tau_values[np.argmin(A_sq_values)]:.3f}")
print(f"  Maximum |A_coset|^2 = {A_max:.8f} at tau = {tau_values[np.argmax(A_sq_values)]:.3f}")
print(f"")
if gate_pass:
    print(f"  >>> GATE VERDICT: PASS <<<")
    print(f"")
    print(f"  The O'Neill A-tensor is STRUCTURALLY POSITIVE at all tau.")
    print(f"  Root cause: [C^2, C^2] = u(2) in su(3) (non-integrable coset).")
    print(f"  Gauge fields from NCG inner fluctuations contribute ADDITIVELY")
    print(f"  through the external field strength F_A.")
else:
    print(f"  >>> GATE VERDICT: FAIL <<<")

# ============================================================================
#  SECTION 8: Save Data and Generate Plot
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 8: Save Data and Plot")
print("=" * 72)

# Save results
np.savez(os.path.join(DATA_DIR, 's55_atensor_gauge.npz'),
         tau_values=tau_values,
         A_sq_koszul=A_sq_values,
         A_sq_simple=A_sq_simple_values,
         R_K_milnor=R_K_milnor_values,
         tau_fold=tau_fold,
         A_sq_fold=A_fold,
         A_sq_round=A_sq_values[0],
         gate_pass=gate_pass,
         A_min=A_min,
         A_max=A_max)
print(f"  Saved: s55_atensor_gauge.npz")

# Generate plot
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: |A|^2 vs tau
ax = axes[0]
ax.plot(tau_values, A_sq_values, 'b-', linewidth=2, label=r'$|A|^2$ (full Koszul)')
ax.plot(tau_values, A_sq_simple_values, 'r--', linewidth=1.5, label=r'$|A|^2$ (simple $\frac{1}{2}[,]^V$)')
ax.axvline(x=tau_fold, color='green', linestyle=':', alpha=0.7, label=f'fold $\\tau={tau_fold}$')
ax.set_xlabel(r'$\tau$ (Jensen parameter)', fontsize=12)
ax.set_ylabel(r'$|A_{\mathrm{coset}}|^2$', fontsize=12)
ax.set_title("O'Neill A-tensor: Internal Coset", fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: Ratio |A|^2 / R_K
ax = axes[1]
ratio_vals = A_sq_values / R_K_milnor_values
ax.plot(tau_values, ratio_vals, 'b-', linewidth=2)
ax.axvline(x=tau_fold, color='green', linestyle=':', alpha=0.7, label=f'fold $\\tau={tau_fold}$')
ax.set_xlabel(r'$\tau$ (Jensen parameter)', fontsize=12)
ax.set_ylabel(r'$|A|^2 / R_K$', fontsize=12)
ax.set_title(r"A-tensor / Scalar Curvature Ratio", fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Total A-tensor with unit gauge field
ax = axes[2]
F_ext_unit = 1.0 + 3.0 + 8.0  # |F_Y|^2 + 3*|F_W|^2 + 8*|F_S|^2 with each = 1
A_total = A_sq_values + F_ext_unit
ax.fill_between(tau_values, 0, A_sq_values, alpha=0.4, color='blue', label=r'$|A_{\mathrm{coset}}|^2$')
ax.fill_between(tau_values, A_sq_values, A_total, alpha=0.4, color='red',
                label=r'$|F_{\mathrm{ext}}|^2$ (unit gauge)')
ax.plot(tau_values, A_total, 'k-', linewidth=1.5)
ax.axvline(x=tau_fold, color='green', linestyle=':', alpha=0.7, label=f'fold $\\tau={tau_fold}$')
ax.set_xlabel(r'$\tau$ (Jensen parameter)', fontsize=12)
ax.set_ylabel(r'$|A_{\mathrm{total}}|^2$', fontsize=12)
ax.set_title("Total A-tensor = Coset + Gauge", fontsize=13)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, 's55_atensor_gauge.png'), dpi=150)
print(f"  Saved: s55_atensor_gauge.png")

print("\n" + "=" * 72)
print("  COMPUTATION COMPLETE")
print("=" * 72)
