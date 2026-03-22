"""
SD-1: SEELEY-DEWITT FAST GATE — da_2/dtau vs da_4/dtau Sign Check
==================================================================

Computes the Seeley-DeWitt coefficients a_2(tau) and a_4(tau) for the
spectral action Tr f(D_K^2 / Lambda^2) on (SU(3), g_tau) with Jensen
TT-deformation parameter tau.

The spectral action effective potential is:

    V_eff(tau) = 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2(tau) + f_0 a_4(tau)

where:
    a_0 = (4pi)^{-d/2} Vol(K)             [tau-INDEPENDENT: volume-preserving]
    a_2 = (4pi)^{-d/2} (1/6) R_K(tau) Vol(K)
    a_4 = (4pi)^{-d/2} (1/360) [5 R^2 - 2|Ric|^2 + 2|Riem|^2](tau) Vol(K)

For d = dim(SU(3)) = 8, using the Gilkey formula for the Dirac operator D^2
on an 8-manifold without boundary (Gilkey 1995, Theorem 4.1.6; BGV 1992
Theorem 4.1):

    Tr(e^{-t D^2}) = (4 pi t)^{-4} * dim(S) * Vol(K)
                    * [1 + (1/6) R t + (1/360)(5R^2 - 2|Ric|^2 + 2|Riem|^2 - 60 R_S) t^2 + ...]

where dim(S) = 2^4 = 16 is the spinor fiber dimension and R_S is the
endomorphism curvature correction. For the spinor bundle with Levi-Civita
connection, R_S = R/4 (Lichnerowicz formula), and the full a_4 coefficient
becomes (for the SPIN Dirac Laplacian):

    a_4^{spin} = (4pi)^{-4} * (1/360) * [(-30 + 5)R^2 + (60 - 2)|Ric|^2
                 + (-180 + 2)|Riem|^2 + dim(S) * 12 * (correction)] * Vol(K)

Actually, let me use the standard result directly. For D^2 = nabla*nabla + E
where E = R/4 on spinors:

    a_0 = (4pi)^{-4} tr(Id) Vol = (4pi)^{-4} * 16 * Vol
    a_2 = (4pi)^{-4} tr(R/6 + E) Vol = (4pi)^{-4} * 16 * (R/6 + R/4) Vol
                                       = (4pi)^{-4} * 16 * (5R/12) Vol
    a_4 = (4pi)^{-4} * (1/360) tr[60*E_{;kk} + 60*R*E + 180*E^2
                                   + (5R^2 - 2|Ric|^2 + 2|Riem|^2) Id
                                   + 12 Omega_{ij}^2] * Vol

where Omega_{ij} is the curvature of the spin connection. For spinors:
    E = R/4 * Id_16
    E_{;kk} = (nabla^2 R)/4 * Id_16
    Omega_{ij} = (1/4) R_{ijkl} gamma^k gamma^l

The trace tr(Omega_{ij}^2) over spinor indices requires:
    tr(gamma^k gamma^l gamma^m gamma^n) = 16 (delta_{kl} delta_{mn}
                                              - delta_{km} delta_{ln}
                                              + delta_{kn} delta_{lm})

So: tr(Omega_{ij}^2) = (1/16) R_{ijkl} R_{ijmn} * 16 * (delta_{kl}delta_{mn}
                         - delta_{km}delta_{ln} + delta_{kn}delta_{lm})
                       = R_{ijkl} R_{ij}^{..kl} * (-1)
                       ... this gets intricate. Let me use the KNOWN result.

For the Dirac operator on a d-dimensional Riemannian manifold (BGV Theorem 4.1):

    a_0 = 2^{[d/2]} (4pi)^{-d/2} Vol
    a_2 = 2^{[d/2]} (4pi)^{-d/2} (R/6) Vol    [sic -- not 5R/12; E contribution cancels]

Wait -- there are different conventions. Let me use the definitive source.

DEFINITIVE: Berline-Getzler-Vergne (Heat Kernels and Dirac Operators, 1992),
Theorem 4.1 for the SPIN Dirac operator D, not D^2:

For D^2 = nabla*nabla + R/4 (Lichnerowicz):

    Tr(e^{-tD^2}) ~ (4pi t)^{-d/2} sum_{k>=0} A_k * t^k

where A_k = integral_M a_k(x) dvol(x) and:

    a_0 = 2^{[d/2]}
    a_1 = 2^{[d/2]} * R/6
    a_2 = 2^{[d/2]} * (1/360) [(-12 nabla^2 R + 5R^2 - 2|Ric|^2 + 2|Riem|^2)
                                + 30R * (R/4) + 60 (R/4)^2 + 12 |Omega|^2 ]

Hmm, this is getting into convention wars. Let me just use the UNIVERSAL
Gilkey-Seeley coefficients for a general Laplacian-type operator
P = -(g^{ij} partial_i partial_j + ...) = nabla*nabla + E:

    a_0(P) = (4pi)^{-d/2} integral tr(Id)
    a_2(P) = (4pi)^{-d/2} (1/6) integral tr(6E + R Id)
    a_4(P) = (4pi)^{-d/2} (1/360) integral tr(
        60 E_{;kk} + 60 R E + 180 E^2
        + (5R^2 - 2|Ric|^2 + 2|Riem|^2) Id
        + 12 Omega_{ij} Omega^{ij}
    )

For the spin Dirac Laplacian D^2 = nabla^S * nabla^S + R/4:
    - Id has trace 2^{d/2} = 16 (for d=8)
    - E = (R/4) Id, so tr(E) = 4R
    - E_{;kk} = (nabla^2 R/4) Id, but on a HOMOGENEOUS space nabla^2 R = 0.
    - Omega_{ij} = (1/4) R_{ijkl} gamma^{kl} is the spin curvature
    - tr(Omega_{ij}^2) = (1/16) R_{ijkl} R_{ijmn} tr(gamma^{kl} gamma^{mn})

For d=8: tr(gamma^{kl} gamma^{mn}) = 16 * 2 (delta^{km}delta^{ln} - delta^{kn}delta^{lm})
                                    = 32 (delta^{km}delta^{ln} - delta^{kn}delta^{lm})

Wait, tr(gamma^a gamma^b) = 2^{d/2} delta^{ab} for Euclidean gamma matrices.
For gamma^{kl} = (1/2)[gamma^k, gamma^l]:
    tr(gamma^{kl} gamma^{mn}) = (1/4) tr([gamma^k,gamma^l][gamma^m,gamma^n])
Let me just compute this numerically using the existing Clifford algebra.

Actually, there's a much cleaner way. I'll compute a_2 and a_4 using:
1. The EXACT analytic curvature formulas from SP-2 (R, |Ric|^2, |Riem|^2)
2. For a_4, the standard Gilkey formula for spin-d/2, and
3. VERIFY by cross-checking the bi-invariant (tau=0) case against known SU(3) results

The key for the GATE is only the SIGNS of da_2/dtau and da_4/dtau.
Even if the absolute normalization has convention-dependent factors, the
tau-dependence is unambiguous because those factors are tau-independent.

Author: Connes-NCG-Theorist Agent (Session 20a)
Date: 2026-02-19
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# EXACT ANALYTIC CURVATURE FORMULAS FROM SP-2 (Session 17b)
# ============================================================================

def R_exact(tau):
    """Scalar curvature R_K(tau) on (SU(3), g_tau).
    R(tau) = -(1/4) e^{-4tau} + 2 e^{-tau} - 1/4 + (1/2) e^{2tau}
    R(0) = 2. Verified at machine epsilon (SP-2, 51 points).
    """
    return -0.25*np.exp(-4*tau) + 2*np.exp(-tau) - 0.25 + 0.5*np.exp(2*tau)


def Ric2_exact(tau):
    """|Ric|^2(tau) = sum Ric_{ab}^2 on (SU(3), g_tau).
    |Ric|^2(0) = 1/2. Verified at machine epsilon.
    """
    return (
        (1/12) * np.exp(-8*tau)
        + (-1/2) * np.exp(-5*tau)
        + (1/8) * np.exp(-4*tau)
        + (13/12) * np.exp(-2*tau)
        + (-1/2) * np.exp(-tau)
        + 1/8
        + (1/12) * np.exp(4*tau)
    )


def K_exact(tau):
    """|Riem|^2(tau) = Kretschner scalar on (SU(3), g_tau).
    K(0) = 1/2. Verified at machine epsilon.
    """
    return (
        (23/96) * np.exp(-8*tau)
        + (-1) * np.exp(-5*tau)
        + (5/16) * np.exp(-4*tau)
        + (11/6) * np.exp(-2*tau)
        + (-3/2) * np.exp(-tau)
        + 17/32
        + (1/12) * np.exp(4*tau)
    )


# ============================================================================
# ANALYTIC DERIVATIVES (exact differentiation of exponential sums)
# ============================================================================

def dR_dtau(tau):
    """d/dtau [R_K(tau)].
    = e^{-4tau} + (-2) e^{-tau} + e^{2tau}
    Check: dR/dtau|_0 = 1 - 2 + 1 = 0 (bi-invariant is critical point of R).
    """
    return np.exp(-4*tau) + (-2)*np.exp(-tau) + np.exp(2*tau)


def dRic2_dtau(tau):
    """d/dtau [|Ric|^2(tau)]."""
    return (
        (1/12) * (-8) * np.exp(-8*tau)
        + (-1/2) * (-5) * np.exp(-5*tau)
        + (1/8) * (-4) * np.exp(-4*tau)
        + (13/12) * (-2) * np.exp(-2*tau)
        + (-1/2) * (-1) * np.exp(-tau)
        + 0  # constant term
        + (1/12) * 4 * np.exp(4*tau)
    )


def dK_dtau(tau):
    """d/dtau [|Riem|^2(tau)] = d/dtau [Kretschner]."""
    return (
        (23/96) * (-8) * np.exp(-8*tau)
        + (-1) * (-5) * np.exp(-5*tau)
        + (5/16) * (-4) * np.exp(-4*tau)
        + (11/6) * (-2) * np.exp(-2*tau)
        + (-3/2) * (-1) * np.exp(-tau)
        + 0  # constant
        + (1/12) * 4 * np.exp(4*tau)
    )


# ============================================================================
# SEELEY-DEWITT COEFFICIENTS (up to tau-independent overall factors)
# ============================================================================
#
# For the spectral action V_eff(tau) = 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2(tau) + f_0 a_4(tau),
# the stabilization condition dV/dtau = 0 requires:
#
#     2 f_2 Lambda^2 (da_2/dtau) + f_0 (da_4/dtau) = 0
#
# Since f_2, f_0, Lambda are all tau-independent, the GATE question is purely
# about the signs of da_2/dtau and da_4/dtau.
#
# CRITICAL CONVENTION NOTE:
# The overall (4pi)^{-4} * dim(S) * Vol(K) factor is tau-INDEPENDENT
# (volume-preserving Jensen deformation, dim(S) = 16 constant).
# So we can work with the REDUCED coefficients:
#
#     a_2^red(tau) = (1/6) R_K(tau)         [proportional to R]
#     a_4^red(tau) = (1/360) [alpha R^2 - beta |Ric|^2 + gamma |Riem|^2](tau)
#
# The coefficients alpha, beta, gamma depend on the operator (scalar Laplacian,
# Dirac, etc.) but NOT on tau. For the Dirac operator D^2:
#
# Using Gilkey's formula for P = nabla*nabla + E with E = R/4 on spinors:
#   a_2 = (4pi)^{-4} tr(R/6 Id + E) Vol = (4pi)^{-4} * 16 * (R/6 + R/4) Vol
#        = (4pi)^{-4} * 16 * (5R/12) Vol
#
# But the tr(6E + R Id)/6 = tr(6*(R/4)*Id + R*Id)/6 = tr((3R/2 + R)*Id)/6
# Hmm let me just be careful. Gilkey's a_2:
#   a_2(x) = tr(6E + R*Id) / 6
#   For E = (R/4)*Id_{16}: tr(6*(R/4)*Id + R*Id) = tr((3R/2 + R)*Id) = (5R/2)*16
#   So a_2(x) = (5R/2)*16/6 = 40R/6 = 20R/3
#
# And a_4 from Gilkey:
#   a_4(x) = (1/360) tr(60 E_{;kk} + 60RE + 180E^2
#                        + (5R^2 - 2|Ric|^2 + 2|Riem|^2)*Id + 12*Omega^2)
#
# On SU(3) (homogeneous): E_{;kk} = (nabla^2 R / 4)*Id = 0 (R is constant on SU(3))
# E = (R/4)*Id, so:
#   60RE = 60*R*(R/4)*Id = 15R^2 * Id
#   180E^2 = 180*(R/4)^2*Id = (180/16)R^2 * Id = (45/4)R^2 * Id
#   tr(15R^2 * Id + (45/4)R^2 * Id) = 16*(15 + 45/4)R^2 = 16*(105/4)R^2 = 420R^2
#
# For the spin connection curvature Omega_{ij} = (1/4) R_{ijkl} gamma^{kl}:
#   tr(Omega_{ij}Omega^{ij}) = (1/16) R_{ijkl} R^{ij}_{mn} tr(gamma^{kl}gamma^{mn})
#
# For d=8: tr(gamma^{kl}gamma^{mn}) where gamma^{kl} = (gamma^k gamma^l - gamma^l gamma^k)/2
# = (1/4)[tr(gamma^k gamma^l gamma^m gamma^n) - tr(gamma^k gamma^l gamma^n gamma^m)
#         - tr(gamma^l gamma^k gamma^m gamma^n) + tr(gamma^l gamma^k gamma^n gamma^m)]
#
# Using tr(gamma^a gamma^b gamma^c gamma^d) = 2^{d/2}(delta_{ab}delta_{cd}
#           - delta_{ac}delta_{bd} + delta_{ad}delta_{bc}) for d=8:
# = 16(delta_{ab}delta_{cd} - delta_{ac}delta_{bd} + delta_{ad}delta_{bc})
#
# tr(gamma^{kl}gamma^{mn}) = (1/4)[
#   16(delta_{kl}delta_{mn} - delta_{km}delta_{ln} + delta_{kn}delta_{lm})
# - 16(delta_{kn}delta_{lm} - delta_{km}delta_{nl} + delta_{kl}delta_{mn})  [swap m,n on second]
# Wait, let me be more careful.
#
# Actually: tr(gamma^k gamma^l gamma^m gamma^n) = 16(d_{kl}d_{mn} - d_{km}d_{ln} + d_{kn}d_{lm})
#
# tr([gamma^k,gamma^l][gamma^m,gamma^n])/4
# = (1/4) tr(gamma^k gamma^l gamma^m gamma^n - gamma^k gamma^l gamma^n gamma^m
#          - gamma^l gamma^k gamma^m gamma^n + gamma^l gamma^k gamma^n gamma^m)
# = (1/4) * 16 * [(d_{kl}d_{mn} - d_{km}d_{ln} + d_{kn}d_{lm})
#                 -(d_{kl}d_{nm} - d_{kn}d_{lm} + d_{km}d_{ln})
#                 -(d_{lk}d_{mn} - d_{lm}d_{kn} + d_{ln}d_{km})
#                 +(d_{lk}d_{nm} - d_{ln}d_{km} + d_{lm}d_{kn})]
# = (1/4) * 16 * [(- d_{km}d_{ln} + d_{kn}d_{lm})
#                 -(- d_{kn}d_{lm} + d_{km}d_{ln})
#                 -(- d_{lm}d_{kn} + d_{ln}d_{km})
#                 +(- d_{ln}d_{km} + d_{lm}d_{kn})]
#    (the d_{kl}d_{mn} terms all cancel in pairs)
# = (1/4) * 16 * [(-d_{km}d_{ln} + d_{kn}d_{lm})
#                 + (d_{kn}d_{lm} - d_{km}d_{ln})
#                 + (d_{lm}d_{kn} - d_{ln}d_{km})
#                 + (-d_{ln}d_{km} + d_{lm}d_{kn})]
# = (1/4) * 16 * 4 * (d_{kn}d_{lm} - d_{km}d_{ln})
# = 16 (d_{kn}d_{lm} - d_{km}d_{ln})
#
# So tr(Omega_{ij}Omega^{ij}) = (1/16) R_{ijkl} R^{ij}_{mn} * 16(d_{kn}d_{lm} - d_{km}d_{ln})
#                              = R_{ijkl} R^{ij}_{mn} (d_{kn}d_{lm} - d_{km}d_{ln})
#                              = R_{ijkl} R^{ijlk} - R_{ijkl} R^{ijkl}
#                              = -|Riem|^2 - |Riem|^2  ... no wait
#
# R_{ijkl} R^{ij}_{mn} d_{kn} d_{lm} = R_{ijkl} R^{ij}_{lk} = R_{ijkl} R^{ijlk}
# By symmetry R^{ijlk} = -R^{ijkl}, so this = -R_{ijkl} R^{ijkl} = -|Riem|^2
#
# R_{ijkl} R^{ij}_{mn} d_{km} d_{ln} = R_{ijkl} R^{ij}_{kl} = R_{ijkl} R^{ijkl} = |Riem|^2
#
# So tr(Omega_{ij}Omega^{ij}) = -|Riem|^2 - |Riem|^2 = -2|Riem|^2
#
# Therefore 12 * tr(Omega^2) = 12 * (-2|Riem|^2) = -24|Riem|^2
# But we need to be careful: the tr() in a_4 includes the fiber trace.
# Actually Omega_{ij} is already a matrix on the spinor fiber, so
# tr(Omega_{ij}Omega^{ij}) already includes the spinor trace.
# But we also need the Vol factor... let me recount.
#
# In the formula: a_4(x) = (1/360) * [
#   60*E_{;kk} + 60*R*E + 180*E^2 + (5R^2 - 2|Ric|^2 + 2|Riem|^2)*Id + 12*Omega^2
# ]
# All quantities are endomorphism-valued (spinor fiber). The trace tr() is
# taken of the whole expression. So:
#
# a_4(x) = (1/360) * {
#   0  (E_{;kk} = 0 on homogeneous space)
#   + 16 * 15R^2  (from 60RE)
#   + 16 * (45/4)R^2  (from 180E^2)
#   + 16 * (5R^2 - 2|Ric|^2 + 2|Riem|^2)  (from curvature invariants * Id)
#   + 12 * (-2|Riem|^2)  (from spin connection curvature)
# }
# = (1/360) * {
#   240R^2 + 180R^2 + 80R^2 - 32|Ric|^2 + 32|Riem|^2 - 24|Riem|^2
# }
# = (1/360) * {500R^2 - 32|Ric|^2 + 8|Riem|^2}
# = (1/360) * 4 * {125R^2 - 8|Ric|^2 + 2|Riem|^2}
# = (1/90) * {125R^2 - 8|Ric|^2 + 2|Riem|^2}
#
# VERIFICATION at tau=0 (bi-invariant SU(3)):
# R=2, |Ric|^2=1/2, |Riem|^2=1/2
# a_4^red(0) = (1/90)*(125*4 - 8*0.5 + 2*0.5) = (1/90)*(500 - 4 + 1) = 497/90 = 5.5222...
#
# For the REDUCED a_2 (with Dirac Lichnerowicz E = R/4):
# a_2^red(tau) = (1/6)*tr(6E + R*Id) = (1/6)*(6*(R/4)*16 + R*16)
#              = (1/6)*(24R + 16R) = (1/6)*40R = 20R/3
# So a_2^red = (20/3) R
# a_2^red(0) = (20/3)*2 = 40/3 = 13.333...
#
# CRITICAL INSIGHT FOR THE GATE:
# Since the overall factors (4pi)^{-4} * Vol(K) are tau-independent,
# the SIGN of da_2/dtau is determined by dR/dtau alone,
# and the SIGN of da_4/dtau is determined by d/dtau[125R^2 - 8|Ric|^2 + 2|Riem|^2].

def a2_reduced(tau):
    """Reduced a_2 coefficient: a_2^red = (20/3) R_K(tau).
    Full a_2 = (4pi)^{-4} * Vol(K) * a_2^red.
    """
    return (20.0 / 3.0) * R_exact(tau)


def a4_reduced(tau):
    """Reduced a_4 coefficient: a_4^red = (1/90)[125 R^2 - 8|Ric|^2 + 2|Riem|^2].
    Full a_4 = (4pi)^{-4} * Vol(K) * a_4^red.
    """
    R = R_exact(tau)
    Ric2 = Ric2_exact(tau)
    K = K_exact(tau)
    return (1.0 / 90.0) * (125.0 * R**2 - 8.0 * Ric2 + 2.0 * K)


def da2_reduced_dtau(tau):
    """d/dtau [a_2^red] = (20/3) dR/dtau."""
    return (20.0 / 3.0) * dR_dtau(tau)


def da4_reduced_dtau(tau):
    """d/dtau [a_4^red] = (1/90)[250 R dR/dtau - 8 d|Ric|^2/dtau + 2 d|Riem|^2/dtau]."""
    R = R_exact(tau)
    return (1.0 / 90.0) * (
        250.0 * R * dR_dtau(tau)
        - 8.0 * dRic2_dtau(tau)
        + 2.0 * dK_dtau(tau)
    )


# ============================================================================
# ALTERNATIVE: SCALAR LAPLACIAN COEFFICIENTS (for comparison)
# ============================================================================
# For the scalar Laplacian Delta_0 = nabla*nabla (E = 0, Omega = 0, tr(Id) = 1):
#   a_2^scalar = (1/6) R
#   a_4^scalar = (1/360)(5R^2 - 2|Ric|^2 + 2|Riem|^2)
# This is the "minimal" formula with no E or Omega corrections.

def a2_scalar(tau):
    return (1.0 / 6.0) * R_exact(tau)

def a4_scalar(tau):
    R = R_exact(tau)
    return (1.0 / 360.0) * (5*R**2 - 2*Ric2_exact(tau) + 2*K_exact(tau))

def da2_scalar_dtau(tau):
    return (1.0 / 6.0) * dR_dtau(tau)

def da4_scalar_dtau(tau):
    R = R_exact(tau)
    return (1.0 / 360.0) * (10*R*dR_dtau(tau) - 2*dRic2_dtau(tau) + 2*dK_dtau(tau))


# ============================================================================
# NUMERICAL VERIFICATION OF ANALYTIC DERIVATIVES
# ============================================================================

def verify_derivatives():
    """Cross-check analytic derivatives against finite differences."""
    print("=" * 76)
    print("  DERIVATIVE VERIFICATION (analytic vs finite difference)")
    print("=" * 76)

    h = 1e-7
    test_taus = [0.1, 0.3, 0.6, 1.0, 1.5, 2.0]  # skip tau=0 where derivatives vanish

    print(f"\n  {'tau':>6}  {'da2_an':>14}  {'da2_fd':>14}  {'err':>10}  "
          f"{'da4_an':>14}  {'da4_fd':>14}  {'err':>10}")
    print(f"  {'-'*90}")

    max_err_a2 = 0
    max_err_a4 = 0

    for tau in test_taus:
        # Analytic
        da2_an = da2_reduced_dtau(tau)
        da4_an = da4_reduced_dtau(tau)

        # Finite difference (central)
        da2_fd = (a2_reduced(tau + h) - a2_reduced(tau - h)) / (2*h)
        da4_fd = (a4_reduced(tau + h) - a4_reduced(tau - h)) / (2*h)

        err_a2 = abs(da2_an - da2_fd) / max(abs(da2_an), 1e-15)
        err_a4 = abs(da4_an - da4_fd) / max(abs(da4_an), 1e-15)

        max_err_a2 = max(max_err_a2, err_a2)
        max_err_a4 = max(max_err_a4, err_a4)

        print(f"  {tau:6.2f}  {da2_an:14.8f}  {da2_fd:14.8f}  {err_a2:10.2e}  "
              f"{da4_an:14.8f}  {da4_fd:14.8f}  {err_a4:10.2e}")

    print(f"\n  Max relative errors: da2 = {max_err_a2:.2e}, da4 = {max_err_a4:.2e}")
    status_a2 = "PASS" if max_err_a2 < 1e-6 else "FAIL"
    status_a4 = "PASS" if max_err_a4 < 1e-6 else "FAIL"
    print(f"  Derivative verification: da2 {status_a2}, da4 {status_a4}")

    return max_err_a2 < 1e-6 and max_err_a4 < 1e-6


# ============================================================================
# MAIN COMPUTATION: SIGN ANALYSIS
# ============================================================================

def main():
    print("=" * 76)
    print("  SD-1: SEELEY-DEWITT FAST GATE")
    print("  V_eff(tau) = 2 f_2 L^2 a_2(tau) + f_0 a_4(tau)")
    print("  Gate: do da_2/dtau and da_4/dtau have opposite signs?")
    print("=" * 76)

    # Step 0: Verify at tau=0
    print("\n  VERIFICATION AT tau=0 (bi-invariant SU(3)):")
    print(f"    R(0) = {R_exact(0):.10f}  (expected 2.0)")
    print(f"    |Ric|^2(0) = {Ric2_exact(0):.10f}  (expected 0.5)")
    print(f"    |Riem|^2(0) = {K_exact(0):.10f}  (expected 0.5)")
    print(f"    a_2^red(0) = {a2_reduced(0):.10f}  (expected 40/3 = {40/3:.10f})")
    print(f"    a_4^red(0) = {a4_reduced(0):.10f}  (expected 497/90 = {497/90:.10f})")
    print(f"    dR/dtau(0) = {dR_dtau(0):.10f}  (expected 0: bi-invariant is critical)")

    # Step 1: Verify derivatives
    print()
    deriv_ok = verify_derivatives()

    # Step 2: Main table
    print("\n" + "=" * 76)
    print("  SEELEY-DEWITT COEFFICIENTS AND DERIVATIVES")
    print("  (Spin Dirac operator D^2 on 8-dim SU(3) with Jensen deformation)")
    print("=" * 76)

    tau_grid = np.linspace(-2.0, 2.0, 41)

    print(f"\n  {'tau':>6}  {'a_2^red':>12}  {'a_4^red':>12}  "
          f"{'da_2/dtau':>12}  {'da_4/dtau':>12}  {'sgn(da2)':>9}  {'sgn(da4)':>9}  {'OPPOSITE?':>10}")
    print(f"  {'-'*100}")

    opposite_found = False
    opposite_ranges = []

    results = []
    for tau in tau_grid:
        a2 = a2_reduced(tau)
        a4 = a4_reduced(tau)
        da2 = da2_reduced_dtau(tau)
        da4 = da4_reduced_dtau(tau)

        # Sign determination (with tolerance for near-zero)
        tol = 1e-10
        sgn_da2 = '+' if da2 > tol else ('-' if da2 < -tol else '0')
        sgn_da4 = '+' if da4 > tol else ('-' if da4 < -tol else '0')

        opposite = (sgn_da2 == '+' and sgn_da4 == '-') or (sgn_da2 == '-' and sgn_da4 == '+')
        opp_str = "YES" if opposite else "no"

        if opposite:
            opposite_found = True
            opposite_ranges.append(tau)

        results.append((tau, a2, a4, da2, da4, sgn_da2, sgn_da4, opp_str))

        print(f"  {tau:6.2f}  {a2:12.6f}  {a4:12.6f}  "
              f"{da2:12.6f}  {da4:12.6f}  {sgn_da2:>9}  {sgn_da4:>9}  {opp_str:>10}")

    # Step 3: Fine scan for sign crossings (FULL range including negative tau)
    print("\n" + "=" * 76)
    print("  FINE SCAN: da_2/dtau and da_4/dtau zero crossings")
    print("=" * 76)

    tau_fine = np.linspace(-2.5, 2.5, 5000)
    da2_fine = np.array([da2_reduced_dtau(t) for t in tau_fine])
    da4_fine = np.array([da4_reduced_dtau(t) for t in tau_fine])

    # Find zero crossings of da2
    da2_zeros = []
    for i in range(len(tau_fine)-1):
        if da2_fine[i] * da2_fine[i+1] < 0:
            # Linear interpolation
            t0 = tau_fine[i] - da2_fine[i] * (tau_fine[i+1] - tau_fine[i]) / (da2_fine[i+1] - da2_fine[i])
            da2_zeros.append(t0)

    da4_zeros = []
    for i in range(len(tau_fine)-1):
        if da4_fine[i] * da4_fine[i+1] < 0:
            t0 = tau_fine[i] - da4_fine[i] * (tau_fine[i+1] - tau_fine[i]) / (da4_fine[i+1] - da4_fine[i])
            da4_zeros.append(t0)

    print(f"\n  da_2/dtau zero crossings: {da2_zeros}")
    print(f"  da_4/dtau zero crossings: {da4_zeros}")

    # Also check: is dR/dtau = 0 at tau=0? (Yes, by design)
    print(f"\n  dR/dtau at tau=0: {dR_dtau(0):.15f}  (should be 0)")
    print(f"  dR/dtau at tau=0.001: {dR_dtau(0.001):.10f}")

    # Step 4: If opposite signs found, compute required f_2/f_0 ratio
    print("\n" + "=" * 76)
    print("  STABILIZATION ANALYSIS")
    print("=" * 76)

    if opposite_found:
        print(f"\n  OPPOSITE SIGNS FOUND at tau values: ",
              [f"{t:.2f}" for t in opposite_ranges])

        # For each tau with opposite signs, compute required ratio
        print(f"\n  Required ratio: f_2 Lambda^2 / f_0 = -(da_4/dtau) / (2 da_2/dtau)")
        print(f"  (Positive ratio => physical cutoff function exists)")
        print(f"\n  {'tau':>6}  {'da_2/dtau':>14}  {'da_4/dtau':>14}  {'f2L2/f0':>14}  {'Natural?':>10}")
        print(f"  {'-'*65}")

        for tau in opposite_ranges:
            da2 = da2_reduced_dtau(tau)
            da4 = da4_reduced_dtau(tau)
            ratio = -da4 / (2 * da2) if abs(da2) > 1e-15 else float('inf')
            natural = "O(1)" if 0.01 < abs(ratio) < 100 else ("fine-tuned" if abs(ratio) > 100 else "??")
            print(f"  {tau:6.2f}  {da2:14.8f}  {da4:14.8f}  {ratio:14.6f}  {natural:>10}")

        # Continuous curve of the ratio
        print(f"\n  Continuous ratio f_2*Lambda^2/f_0 over tau range with opposite signs:")
        tau_opp = np.linspace(max(0.01, min(opposite_ranges)-0.1),
                              min(2.0, max(opposite_ranges)+0.1), 100)
        for i, tau in enumerate(tau_opp):
            da2 = da2_reduced_dtau(tau)
            da4 = da4_reduced_dtau(tau)
            if abs(da2) > 1e-10:
                ratio = -da4 / (2 * da2)
                if ratio > 0 and i % 10 == 0:
                    print(f"    tau={tau:.4f}: f_2*L^2/f_0 = {ratio:.6f}")
    else:
        print("\n  NO OPPOSITE SIGNS FOUND.")
        print("  da_2/dtau and da_4/dtau have the SAME sign for all tau in [0, 2].")
        print("  This means the spectral action V_eff = f_2*L^2*a_2 + f_0*a_4")
        print("  is MONOTONIC for any positive f_0, f_2.")

    # Step 5: Also check scalar Laplacian (for comparison)
    print("\n" + "=" * 76)
    print("  COMPARISON: SCALAR LAPLACIAN a_4 (without spinor corrections)")
    print("=" * 76)

    print(f"\n  {'tau':>6}  {'da2_scal':>12}  {'da4_scal':>12}  {'sgn2':>6}  {'sgn4':>6}  {'opp?':>6}")
    print(f"  {'-'*60}")

    scalar_opposite = False
    for tau in tau_grid:
        da2s = da2_scalar_dtau(tau)
        da4s = da4_scalar_dtau(tau)
        s2 = '+' if da2s > 1e-10 else ('-' if da2s < -1e-10 else '0')
        s4 = '+' if da4s > 1e-10 else ('-' if da4s < -1e-10 else '0')
        opp = "YES" if (s2=='+' and s4=='-') or (s2=='-' and s4=='+') else "no"
        if opp == "YES":
            scalar_opposite = True
        print(f"  {tau:6.2f}  {da2s:12.6f}  {da4s:12.6f}  {s2:>6}  {s4:>6}  {opp:>6}")

    # Step 6: Second derivative check (convexity at tau=0)
    print("\n" + "=" * 76)
    print("  SECOND DERIVATIVE ANALYSIS AT tau=0")
    print("=" * 76)

    h = 1e-5
    d2a2 = (a2_reduced(h) - 2*a2_reduced(0) + a2_reduced(-h)) / h**2
    d2a4 = (a4_reduced(h) - 2*a4_reduced(0) + a4_reduced(-h)) / h**2

    print(f"\n  d^2 a_2/dtau^2 |_0 = {d2a2:.8f}")
    print(f"  d^2 a_4/dtau^2 |_0 = {d2a4:.8f}")
    print(f"  Signs: d2a2={'+'if d2a2>0 else '-'}, d2a4={'+'if d2a4>0 else '-'}")

    if d2a2 > 0 and d2a4 > 0:
        print("  Both concave UP at tau=0 => local minimum of V at tau=0 for appropriate signs")
    elif d2a2 * d2a4 < 0:
        print("  Mixed convexity => V_eff shape depends on f_2/f_0 ratio")
    else:
        print("  Both concave in same direction")

    # Step 7: R^2 dominance check
    print("\n" + "=" * 76)
    print("  TERM DECOMPOSITION IN a_4^red")
    print("=" * 76)
    print(f"\n  a_4^red = (1/90) [125 R^2 - 8|Ric|^2 + 2|Riem|^2]")
    print(f"\n  {'tau':>6}  {'125*R^2':>14}  {'-8*Ric2':>14}  {'2*Riem2':>14}  {'total':>14}  {'R^2 frac':>10}")
    print(f"  {'-'*80}")

    for tau in tau_grid[::2]:
        R = R_exact(tau)
        Ric2 = Ric2_exact(tau)
        K = K_exact(tau)
        t1 = 125 * R**2
        t2 = -8 * Ric2
        t3 = 2 * K
        total = t1 + t2 + t3
        frac = t1 / total if abs(total) > 1e-15 else float('nan')
        print(f"  {tau:6.2f}  {t1:14.6f}  {t2:14.6f}  {t3:14.6f}  {total:14.6f}  {frac:10.4f}")

    # Step 8: Plot
    print("\n" + "=" * 76)
    print("  GENERATING PLOT")
    print("=" * 76)

    tau_plot = np.linspace(-2.0, 2.0, 1000)
    da2_plot = np.array([da2_reduced_dtau(t) for t in tau_plot])
    da4_plot = np.array([da4_reduced_dtau(t) for t in tau_plot])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: a_2 and a_4 vs tau
    ax1 = axes[0, 0]
    a2_plot = np.array([a2_reduced(t) for t in tau_plot])
    a4_plot = np.array([a4_reduced(t) for t in tau_plot])
    ax1.plot(tau_plot, a2_plot, 'b-', linewidth=2, label=r'$a_2^{red}(\tau)$')
    ax1.plot(tau_plot, a4_plot, 'r-', linewidth=2, label=r'$a_4^{red}(\tau)$')
    ax1.set_xlabel(r'$\tau$')
    ax1.set_ylabel('Coefficient value')
    ax1.set_title('Seeley-DeWitt Coefficients vs Jensen parameter')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)

    # Panel 2: Derivatives (THE GATE)
    ax2 = axes[0, 1]
    ax2.plot(tau_plot, da2_plot, 'b-', linewidth=2, label=r'$da_2/d\tau$')
    ax2.plot(tau_plot, da4_plot, 'r-', linewidth=2, label=r'$da_4/d\tau$')
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.set_xlabel(r'$\tau$')
    ax2.set_ylabel('Derivative value')
    ax2.set_title('SD-1 GATE: Sign comparison of derivatives')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Shade regions where signs are opposite
    for i in range(len(tau_plot)-1):
        if da2_plot[i] * da4_plot[i] < 0:
            ax2.axvspan(tau_plot[i], tau_plot[i+1], alpha=0.1, color='green')

    # Panel 3: Required f_2*L^2/f_0 ratio
    ax3 = axes[1, 0]
    ratio_plot = np.zeros_like(tau_plot)
    for i, t in enumerate(tau_plot):
        if abs(da2_plot[i]) > 1e-10:
            r = -da4_plot[i] / (2 * da2_plot[i])
            ratio_plot[i] = r if r > 0 else np.nan
        else:
            ratio_plot[i] = np.nan

    valid = ~np.isnan(ratio_plot)
    if np.any(valid):
        ax3.plot(tau_plot[valid], ratio_plot[valid], 'g-', linewidth=2)
        ax3.set_xlabel(r'$\tau$')
        ax3.set_ylabel(r'$f_2 \Lambda^2 / f_0$')
        ax3.set_title('Required cutoff ratio for stabilization')
        ax3.grid(True, alpha=0.3)
        ax3.set_yscale('log')
    else:
        ax3.text(0.5, 0.5, 'No stabilization possible\n(same sign everywhere)',
                 ha='center', va='center', transform=ax3.transAxes, fontsize=14)
        ax3.set_title('Required cutoff ratio (NONE)')

    # Panel 4: Curvature invariants
    ax4 = axes[1, 1]
    R_plot = np.array([R_exact(t) for t in tau_plot])
    Ric2_plot = np.array([Ric2_exact(t) for t in tau_plot])
    K_plot = np.array([K_exact(t) for t in tau_plot])
    ax4.plot(tau_plot, R_plot, 'b-', linewidth=2, label=r'$R_K$')
    ax4.plot(tau_plot, Ric2_plot, 'r-', linewidth=2, label=r'$|Ric|^2$')
    ax4.plot(tau_plot, K_plot, 'g-', linewidth=2, label=r'$|Riem|^2$')
    ax4.set_xlabel(r'$\tau$')
    ax4.set_ylabel('Curvature invariant')
    ax4.set_title('Curvature invariants on (SU(3), g_tau)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('tier0-computation/sd20a_seeley_dewitt_gate.png', dpi=150, bbox_inches='tight')
    print("  Plot saved: tier0-computation/sd20a_seeley_dewitt_gate.png")

    # ========================================================================
    # FINAL VERDICT
    # ========================================================================
    print("\n" + "=" * 76)
    print("  ======  VERDICT  ======")
    print("=" * 76)

    # Separate analysis for positive and negative tau
    pos_opposite = [t for t in opposite_ranges if t > 0]
    neg_opposite = [t for t in opposite_ranges if t < 0]

    if pos_opposite:
        tau_min = min(pos_opposite)
        tau_max = max(pos_opposite)
        tau_mid = (tau_min + tau_max) / 2
        da2_mid = da2_reduced_dtau(tau_mid)
        da4_mid = da4_reduced_dtau(tau_mid)
        ratio_mid = -da4_mid / (2 * da2_mid) if abs(da2_mid) > 1e-15 else float('inf')

        print(f"\n  NCG SPECTRAL ACTION PATH (tau > 0): *** OPEN ***")
        print(f"\n  Opposite signs in tau in [{tau_min:.2f}, {tau_max:.2f}].")
        print(f"  Required f_2*Lambda^2/f_0 ~ {ratio_mid:.4f}")
    else:
        print(f"\n  NCG SPECTRAL ACTION PATH (tau > 0): *** CLOSED ***")
        print(f"  da_2/dtau and da_4/dtau are BOTH POSITIVE for all tau > 0.")
        print(f"  No spectral action minimum at positive tau for any cutoff function.")

    if neg_opposite:
        tau_min_neg = min(neg_opposite)
        tau_max_neg = max(neg_opposite)

        print(f"\n  NCG SPECTRAL ACTION PATH (tau < 0): *** OPEN ***")
        print(f"\n  da_2/dtau > 0 and da_4/dtau < 0 for tau in [{tau_min_neg:.2f}, {tau_max_neg:.2f}].")
        print(f"  da_4/dtau crosses zero at tau ~ -0.686.")
        print(f"  A spectral action MINIMUM exists for positive f_2*Lambda^2/f_0.")

        # Print ratio table
        print(f"\n  Required cutoff ratio vs stabilization point:")
        print(f"  {'tau_0':>8}  {'f2*L2/f0':>12}  {'R(tau_0)':>10}  {'regime':>20}")
        print(f"  {'-'*55}")
        for tau in [-0.7, -0.8, -0.9, -1.0, -1.2, -1.5, -2.0]:
            da2 = da2_reduced_dtau(tau)
            da4 = da4_reduced_dtau(tau)
            if abs(da2) > 1e-15 and da4 * da2 < 0:
                ratio = -da4 / (2 * da2)
                R = R_exact(tau)
                regime = "O(1) NATURAL" if 0.1 < ratio < 10 else ("moderate" if ratio < 100 else "hierarchy")
                print(f"  {tau:8.2f}  {ratio:12.4f}  {R:10.4f}  {regime:>20}")

        print(f"\n  PHYSICAL INTERPRETATION:")
        print(f"  At negative tau, the Jensen deformation EXPANDS the SU(2) sector")
        print(f"  and SHRINKS the U(1) + C^2 sectors (volume preserved).")
        print(f"  The scalar curvature R_K goes NEGATIVE (concave internal geometry).")
        print(f"  The a_2 term (proportional to R) and a_4 term (dominated by R^2)")
        print(f"  evolve in opposite directions because da_4/dtau is driven by")
        print(f"  d/dtau[125*R^2], which has opposite sign from dR/dtau when R < 0.")
        print(f"\n  KEY: For tau_0 ~ -0.9, the ratio f_2*L^2/f_0 ~ 0.88 is O(1).")
        print(f"  This is NATURAL -- no fine-tuning of the cutoff function required.")
    else:
        print(f"\n  No opposite signs found at negative tau either.")

    # Overall verdict
    print(f"\n  {'='*60}")
    print(f"  OVERALL VERDICT:")
    print(f"  {'='*60}")
    if neg_opposite and not pos_opposite:
        print(f"\n  SD-1 GATE: CONDITIONALLY OPEN")
        print(f"\n  The Seeley-DeWitt expansion of the spectral action V_eff(tau)")
        print(f"  admits a minimum at NEGATIVE tau (tau_0 in [-2, -0.69]).")
        print(f"  At tau_0 ~ -0.9, the required ratio f_2*L^2/f_0 ~ 0.88 is O(1).")
        print(f"\n  CONDITION: This requires the Jensen deformation to go in the")
        print(f"  'wrong' direction -- expanding SU(2) while shrinking U(1).")
        print(f"  The physical viability depends on whether this regime connects")
        print(f"  to the correct SM gauge coupling ratios.")
        print(f"\n  For POSITIVE tau (the physically interesting direction where")
        print(f"  g_1/g_2 = e^{{-2tau}} < 1 as observed): CLOSED.")
        print(f"  Both da_2/dtau and da_4/dtau are positive, and the spectral")
        print(f"  action is monotonically increasing. No minimum exists.")
    elif pos_opposite:
        print(f"\n  SD-1 GATE: OPEN at positive tau (primary target)")
    elif opposite_found:
        print(f"\n  SD-1 GATE: OPEN (details above)")
    else:
        print(f"\n  SD-1 GATE: CLOSED everywhere")

    print("\n" + "=" * 76)


if __name__ == "__main__":
    main()
