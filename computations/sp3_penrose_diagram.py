"""
SP-3: HIGHER-DIMENSIONAL PENROSE DIAGRAM FOR (SU(3), g_{s(t)})
================================================================

Schwarzschild-Penrose-Geometer -- Session 17c

THE PROBLEM:
  The full spacetime is M^4 x (SU(3), g_{s(t)}), where s(t) is the
  time-dependent Jensen deformation parameter (spectral exflation).

  We construct the Penrose diagram for the (1+1)-dimensional MODULI SPACE
  reduction: coordinates (t, s), where:
    - t = external cosmological time
    - s = Jensen shape modulus (dynamical)

  The metric on this mini-superspace is derived from the kinetic energy
  of the modulus field s(t) and the tree-level potential V_tree(s).

METHODOLOGY (Schwarzschild + Penrose synthesis):
  1. Write the exact mini-superspace metric from dimensional reduction
  2. Analyze curvature singularities at s -> +/- infinity
  3. Classify geodesic completeness
  4. Construct conformal compactification
  5. Draw the Penrose diagram with all boundaries labeled
  6. Apply Penrose singularity theorem (or explain why it fails)

KEY INPUTS FROM 17a-17b:
  - g_s = 3 * diag(e^{-2s}x3, e^s x4, e^{2s}x1) [SP-1]
  - V_tree(s) = 1 - (1/10)(2e^{2s} - 1 + 8e^{-s} - e^{-4s}) [SP-4]
  - K(s) = (23/96)e^{-8s} - e^{-5s} + (5/16)e^{-4s} + (11/6)e^{-2s}
           - (3/2)e^{-s} + 17/32 + (1/12)e^{4s}  [SP-2]
  - g_s NEVER singular at finite s [SP-2]
  - u(1) Ricci eigenvalue = 1/4 for all s [SP-2]

Author: Schwarzschild-Penrose-Geometer (Session 17c)
Date: 2026-02-14
"""

import numpy as np
from numpy.linalg import det, eigvalsh
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# NOTE: All curvature computations use EXACT ANALYTIC formulas from SP-2.
# No slow numerical Riemann tensor computation needed.
# Imports from tier1_dirac_spectrum / tier1_spectral_action NOT NEEDED.


def separator(title):
    print(f"\n{'='*76}")
    print(f"  {title}")
    print(f"{'='*76}")


# =============================================================================
# PART 0: CURVATURE INVARIANT FORMULAS (exact from SP-2)
# =============================================================================

def R_exact(s):
    """Scalar curvature R(s) -- exact (Baptista eq 3.70)."""
    return -0.25*np.exp(-4*s) + 2*np.exp(-s) - 0.25 + 0.5*np.exp(2*s)

def K_exact(s):
    """Kretschner scalar K(s) -- exact (SP-2)."""
    return (
        (23/96) * np.exp(-8*s)
        - 1.0 * np.exp(-5*s)
        + (5/16) * np.exp(-4*s)
        + (11/6) * np.exp(-2*s)
        - (3/2) * np.exp(-s)
        + 17/32
        + (1/12) * np.exp(4*s)
    )

def Ric2_exact(s):
    """|Ric|^2(s) -- exact (SP-2)."""
    return (
        (1/12) * np.exp(-8*s)
        - 0.5 * np.exp(-5*s)
        + (1/8) * np.exp(-4*s)
        + (13/12) * np.exp(-2*s)
        - 0.5 * np.exp(-s)
        + 1/8
        + (1/12) * np.exp(4*s)
    )

def Weyl2_exact(s):
    """|Weyl|^2(s) -- exact (SP-2)."""
    return (
        (377/2016) * np.exp(-8*s)
        - (5/7) * np.exp(-5*s)
        + (79/336) * np.exp(-4*s)
        + (325/252) * np.exp(-2*s)
        - (17/14) * np.exp(-s)
        + 101/224
        + (2/21) * np.exp(s)
        - (1/84) * np.exp(2*s)
        + (5/126) * np.exp(4*s)
    )

def f_of_s(s):
    """The f(s) function from V_tree."""
    return 2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)

def V_tree(s):
    """Tree-level potential V(sigma=0, s)."""
    return 1.0 - (1.0/10.0) * f_of_s(s)


# =============================================================================
# PART 1: MINI-SUPERSPACE METRIC FROM DIMENSIONAL REDUCTION
# =============================================================================

def part1_minisuperspace():
    """
    Derive the (1+1)D mini-superspace metric for the modulus s(t).

    DERIVATION:
    -----------
    The full (4+8)D spacetime has topology M^4 x SU(3) with metric:

      ds^2_{12D} = g_{mu nu}(x) dx^mu dx^nu + g_{ab}(s(t)) w^a w^b

    where g_{ab}(s) is the 8x8 Jensen metric and w^a are Maurer-Cartan
    1-forms on SU(3).

    Dimensional reduction to 4D gives the effective action:

      S_4D = integral d^4x sqrt(-g_4) Vol(SU(3), g_s) * [R_4 + R_int(s)
             + G_ss (ds/dt)^2 / 2]

    where:
      - Vol(SU(3), g_s) = Vol(SU(3), g_0) * sqrt(det(g_s)/det(g_0))
                        = Vol(SU(3), g_0) * 1   [volume-preserving!]
      - R_int(s) = scalar curvature of (SU(3), g_s) = our R_exact(s)
      - G_ss = moduli space metric on the space of Jensen deformations

    The moduli space metric G_ss is the DeWitt metric on the space of
    metrics on SU(3), restricted to the Jensen 1-parameter family:

      G_ss = (1/2) integral_{SU(3)} g^{ab} g^{cd} (dg_{ac}/ds)(dg_{bd}/ds) dvol

    For the diagonal Jensen metric g_s = 3*diag(lambda_1,...,lambda_8):

      dg_{ab}/ds = 3*diag(d(lambda_a)/ds)

    where:
      lambda_a = e^{-2s} for a in SU2 (indices 0,1,2)
      lambda_a = e^{s}   for a in C2  (indices 3,4,5,6)
      lambda_a = e^{2s}  for a in U1  (index 7)

    So d(lambda_a)/ds = {-2 e^{-2s}, e^{s}, 2 e^{2s}} on {SU2, C2, U1}.

    The DeWitt metric on the space of diagonal metrics:
      G_ss = (1/2) sum_a (d ln lambda_a / ds)^2

    since g^{ab} g^{cd} dg_{ac}/ds dg_{bd}/ds = sum_a (dg_{aa}/ds / g_{aa})^2
    = sum_a (d ln lambda_a / ds)^2.

    d ln(lambda_a)/ds = {-2, 1, 2} on {SU2, C2, U1}.

    G_ss = (1/2) [3*(-2)^2 + 4*(1)^2 + 1*(2)^2]
         = (1/2) [12 + 4 + 4]
         = 10

    NOTE: G_ss = 10 is CONSTANT (independent of s).
    This is because the Jensen deformation is a geodesic in the DeWitt
    supermetric on the space of left-invariant metrics on SU(3).
    """
    separator("PART 1: MINI-SUPERSPACE METRIC")

    print("""
  The mini-superspace for the modulus s(t) is a (1+1)D spacetime with
  coordinates (t, s) and an EFFECTIVE metric derived from dimensional
  reduction of the 12D Einstein-Hilbert action.

  KEY RESULT: The DeWitt metric on the 1D moduli space is:

      G_ss = (1/2) * sum_a (d ln lambda_a / ds)^2
           = (1/2) * [3*(-2)^2 + 4*(1)^2 + 1*(2)^2]
           = (1/2) * [12 + 4 + 4]
           = 10

  This is CONSTANT in s (the Jensen deformation is a DeWitt geodesic).
""")

    # Verify ANALYTICALLY (no numerical differentiation needed)
    # d ln(lambda_a)/ds = {-2, 1, 2} for {SU2, C2, U1}
    # These are CONSTANTS (independent of s), confirming G_ss = const = 10.
    print("  Analytical verification of G_ss:")
    dlog_su2 = -2.0   # d/ds ln(e^{-2s}) = -2
    dlog_c2 = 1.0     # d/ds ln(e^{s}) = 1
    dlog_u1 = 2.0     # d/ds ln(e^{2s}) = 2
    G_ss_analytic = 0.5 * (3 * dlog_su2**2 + 4 * dlog_c2**2 + 1 * dlog_u1**2)
    print(f"    G_ss = (1/2)[3*(-2)^2 + 4*(1)^2 + 1*(2)^2] = {G_ss_analytic:.1f}")
    print(f"    G_ss is s-INDEPENDENT (Jensen deformation = DeWitt geodesic)")

    G_ss = G_ss_analytic  # = 10.0

    print(f"""
  MINI-SUPERSPACE METRIC:
  -----------------------
  The effective (1+1)D dynamics is governed by:

      L = (1/2) G_ss * (ds/dt)^2 - V_tree(s)

  with G_ss = 10 (constant). The equation of motion is:

      G_ss * d^2s/dt^2 = -dV_tree/ds = (1/10) * f'(s)

  or simply:

      d^2s/dt^2 = (1/100) * f'(s)

  where f'(s) = 4 e^{{2s}} - 8 e^{{-s}} + 4 e^{{-4s}}

  The MINI-SUPERSPACE LINE ELEMENT for the (t, s) plane is:

      ds^2_mini = -dt^2 + (1/G_ss) ds^2 = -dt^2 + (1/10) ds^2

  This is FLAT Minkowski space in (1+1)D with a rescaled s-coordinate!
  The s-dynamics is driven by the potential V_tree(s), not by intrinsic
  curvature of the moduli space.

  NOTE: The (t, s) mini-superspace is Lorentzian, with t timelike and
  s spacelike. The potential V_tree(s) acts as an external force, not
  a metric deformation.
""")

    return G_ss


# =============================================================================
# PART 2: CURVATURE SINGULARITY ANALYSIS
# =============================================================================

def part2_singularity_analysis():
    """
    Analyze whether s -> +/- infinity produces curvature singularities
    in the 8D internal space (SU(3), g_s).
    """
    separator("PART 2: CURVATURE SINGULARITY ANALYSIS")

    print("""
  QUESTION: Is the internal space (SU(3), g_s) singular at any s?

  From SP-2 exact formulas:
    K(s) = (23/96) e^{-8s} - e^{-5s} + (5/16) e^{-4s} + (11/6) e^{-2s}
           - (3/2) e^{-s} + 17/32 + (1/12) e^{4s}
""")

    # Asymptotic analysis
    print("  ASYMPTOTIC ANALYSIS:")
    print()

    print("  (a) s -> +infinity:")
    print("      K(s) ~ (1/12) e^{4s} -> +infinity")
    print("      R(s) ~ (1/2) e^{2s} -> +infinity")
    print("      |Ric|^2(s) ~ (1/12) e^{4s} -> +infinity")
    print("      |Weyl|^2(s) ~ (5/126) e^{4s} -> +infinity")
    print()
    print("      ALL curvature invariants DIVERGE as s -> +infinity.")
    print("      s = +infinity is a CURVATURE SINGULARITY of the internal space.")
    print()

    print("  (b) s -> -infinity:")
    print("      K(s) ~ (23/96) e^{-8s} -> +infinity")
    print("      R(s) ~ -(1/4) e^{-4s} -> -infinity")
    print("      |Ric|^2(s) ~ (1/12) e^{-8s} -> +infinity")
    print("      |Weyl|^2(s) ~ (377/2016) e^{-8s} -> +infinity")
    print()
    print("      ALL curvature invariants DIVERGE as s -> -infinity.")
    print("      s = -infinity is ALSO a curvature singularity.")
    print()

    print("  (c) Finite s:")
    print("      K(s) is a smooth function of s for ALL finite s.")
    print("      The metric g_s = 3*diag(e^{-2s}, e^{-2s}, e^{-2s}, e^s, e^s, e^s, e^s, e^{2s})")
    print("      is positive definite for all finite s.")
    print("      NO singularity at finite s.")

    # Compute and display K(s) at key points
    print()
    print(f"  {'s':>8}  {'K(s)':>16}  {'R(s)':>14}  {'|Weyl|^2(s)':>16}  {'Verdict':>20}")
    print(f"  {'-'*8}  {'-'*16}  {'-'*14}  {'-'*16}  {'-'*20}")

    s_test = [-5, -3, -2, -1, 0, 0.15, 0.30, 0.50, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
    for s in s_test:
        K = K_exact(s)
        R = R_exact(s)
        W2 = Weyl2_exact(s)
        if abs(s) > 4:
            verdict = "CURVATURE GROWING"
        elif abs(s) <= 0.5:
            verdict = "FINITE, SMOOTH"
        else:
            verdict = "LARGE BUT FINITE"
        print(f"  {s:8.2f}  {K:16.6e}  {R:14.6e}  {W2:16.6e}  {verdict:>20}")

    print()
    print("  SINGULARITY CLASSIFICATION:")
    print("  ----------------------------")
    print("  s -> +infinity: CURVATURE SINGULARITY (K ~ (1/12) e^{4s})")
    print("    - su(2) directions shrink: e^{-2s} -> 0")
    print("    - C^2 directions grow: e^{s} -> infinity")
    print("    - u(1) direction grows: e^{2s} -> infinity")
    print("    - Geometry: SU(3) degenerates to SU(2)-collapsed fiber over CP^2 x U(1)")
    print("    - PHYSICAL: the su(2) sector is crushed. 3 of 8 dimensions degenerate.")
    print()
    print("  s -> -infinity: CURVATURE SINGULARITY (K ~ (23/96) e^{-8s})")
    print("    - su(2) directions grow: e^{-2s} -> infinity")
    print("    - C^2 directions shrink: e^{s} -> 0")
    print("    - u(1) direction shrinks: e^{2s} -> 0")
    print("    - Geometry: SU(3) degenerates to su(2)-blown-up with collapsed C^2 x U(1)")
    print("    - PHYSICAL: the coset C^2 and u(1) are crushed. 5 of 8 dimensions degenerate.")
    print()
    print("  BOTH singularities are at INFINITE AFFINE PARAMETER (see Part 3).")
    print("  The internal space is geodesically complete for the STATIC metric at")
    print("  any fixed finite s, because SU(3) is compact.")
    print("  The singularities arise only in the MODULI SPACE (t, s) when s -> +/- infinity.")

    return


# =============================================================================
# PART 3: GEODESIC COMPLETENESS IN THE MODULI SPACE
# =============================================================================

def part3_geodesic_completeness():
    """
    Analyze geodesic completeness of the (1+1)D mini-superspace.

    The mini-superspace line element is ds^2 = -dt^2 + (1/10) ds^2
    (flat Minkowski, rescaled), but the physical evolution has
    d^2s/dt^2 = -V'(s) / G_ss.

    A GEODESIC in the potential-free mini-superspace is just a straight
    line (t, s) = (t_0 + tau, s_0 + v*tau) which reaches s = +/- infinity
    in INFINITE proper time tau -> +/- infinity. So the MINI-SUPERSPACE
    is geodesically complete (all geodesics extend to infinite affine
    parameter).

    However, with the POTENTIAL V_tree(s), the dynamics is modified.
    V_tree(s) is monotonically decreasing for s > 0, which means the
    modulus is accelerated toward s -> +infinity (runaway). We need to
    check if the modulus reaches s = infinity in FINITE or INFINITE time.
    """
    separator("PART 3: GEODESIC COMPLETENESS")

    G_ss = 10.0

    # V_tree derivatives
    def V_prime(s):
        """dV_tree/ds = -(1/10) * f'(s)"""
        fp = 4*np.exp(2*s) - 8*np.exp(-s) + 4*np.exp(-4*s)
        return -(1.0/10.0) * fp

    def V_double_prime(s):
        """d^2V_tree/ds^2 = -(1/10) * f''(s)"""
        fpp = 8*np.exp(2*s) + 8*np.exp(-s) - 16*np.exp(-4*s)
        return -(1.0/10.0) * fpp

    print("  The equation of motion for s(t) in the potential V_tree(s) is:")
    print()
    print("      G_ss * s'' = -V'(s)")
    print("      10 * s'' = -V'(s)")
    print()
    print("  where V'(s) = -(1/10) * [4 e^{2s} - 8 e^{-s} + 4 e^{-4s}]")
    print()

    # Check the force direction
    print("  Force analysis: -V'(s) = (1/10) * [4 e^{2s} - 8 e^{-s} + 4 e^{-4s}]")
    print()
    print(f"  {'s':>6}  {'V(s)':>12}  {'-V_prime(s)':>12}  {'Force dir':>12}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}")

    for s in [-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0, 5.0]:
        V = V_tree(s)
        F = -V_prime(s)
        direction = "-> +inf" if F > 0.01 else ("-> -inf" if F < -0.01 else "~ 0")
        print(f"  {s:6.2f}  {V:12.6f}  {F:12.6f}  {direction:>12}")

    # ===================================================================
    # Solve s(t) numerically to check finite-time blow-up
    # ===================================================================
    print("\n  NUMERICAL INTEGRATION: Does s(t) reach infinity in finite time?")
    print()

    # Case A: Start at s=0 with zero velocity (released from rest at inflection)
    def eom(t, y):
        s_val, sdot = y
        sddot = -V_prime(s_val) / G_ss
        return [sdot, sddot]

    def event_s_large(t, y):
        return y[0] - 50.0  # trigger at s=50
    event_s_large.terminal = True

    def event_s_neg_large(t, y):
        return y[0] + 50.0  # trigger at s=-50
    event_s_neg_large.terminal = True

    test_cases = [
        ("A: s(0)=0, s'(0)=0 (rest at inflection)", [0.0, 0.0]),
        ("B: s(0)=0, s'(0)=+1 (outward kick)", [0.0, 1.0]),
        ("C: s(0)=0.15, s'(0)=0 (gauge window)", [0.15, 0.0]),
        ("D: s(0)=0.30, s'(0)=0 (sin^2 theta_W)", [0.30, 0.0]),
        ("E: s(0)=0, s'(0)=-1 (inward kick)", [0.0, -1.0]),
    ]

    for label, y0 in test_cases:
        sol = solve_ivp(eom, [0, 500], y0, events=[event_s_large, event_s_neg_large],
                        max_step=0.5, rtol=1e-10, atol=1e-12,
                        method='RK45')

        final_s = sol.y[0, -1]
        final_t = sol.t[-1]

        # Check for runaway
        if sol.t_events[0].size > 0:
            t_blow = sol.t_events[0][0]
            print(f"    Case {label}")
            print(f"      s reaches +50 at t = {t_blow:.6f}")
            print(f"      (finite time blow-up to +infinity)")
        elif sol.t_events[1].size > 0:
            t_blow = sol.t_events[1][0]
            print(f"    Case {label}")
            print(f"      s reaches -50 at t = {t_blow:.6f}")
            print(f"      (finite time blow-up to -infinity)")
        else:
            print(f"    Case {label}")
            print(f"      Final: s({final_t:.2f}) = {final_s:.6f}  (no blow-up in t < {final_t:.0f})")
        print()

    # ===================================================================
    # Analytic estimate of blow-up time
    # ===================================================================
    print("  ANALYTIC BLOW-UP TIME ESTIMATE:")
    print()
    print("  For s >> 1: V_tree(s) ~ -(1/5) e^{2s}, so V'(s) ~ -(2/5) e^{2s}")
    print("  The EOM becomes: 10 s'' = (2/5) e^{2s}")
    print("  => s'' = (1/25) e^{2s}")
    print()
    print("  This is s'' = A e^{2s} with A = 1/25.")
    print("  Multiplying by s': s' s'' = A e^{2s} s' => (s'^2/2)' = A (e^{2s}/2)'")
    print("  => s'^2 = A e^{2s} + C (energy conservation)")
    print()
    print("  For s -> +inf from rest: s' ~ sqrt(A) e^s = (1/5) e^s")
    print("  => ds/e^s = dt/5 => -e^{-s} = t/5 + const")
    print("  => e^{-s} -> 0 as t -> t_blow (FINITE)")
    print()
    print("  So s -> +infinity in FINITE TIME. The modulus hits the curvature")
    print("  singularity at s=+infinity in finite proper time.")
    print("  This means the mini-superspace is GEODESICALLY INCOMPLETE.")
    print()

    # More precise estimate: integrate ds / sqrt(A * e^{2s})
    # from s_0 to infinity = integral e^{-s} ds from s_0 to inf = e^{-s_0}
    # Time = 5 * e^{-s_0}
    for s0 in [0.0, 0.15, 0.30, 1.0]:
        t_est = 5.0 * np.exp(-s0)
        print(f"    From s_0 = {s0:.2f}: estimated blow-up time t* ~ {t_est:.4f}")

    print()
    print("  For s -> -infinity: V_tree(s) ~ (1/10) e^{-4s}, V'(s) ~ -(4/10) e^{-4s}")
    print("  EOM: 10 s'' = (4/10) e^{-4s} => s'' = (1/25) e^{-4s}")
    print("  For s << -1 starting at rest: s' ~ -(2/5*sqrt(10)) e^{-2s} -> -infinity")
    print("  => ds / e^{-2s} = dt * const => e^{2s}/2 = t*const + C")
    print("  => e^{2s} -> 0 as t -> t_blow (FINITE)")
    print()
    print("  So s -> -infinity ALSO in FINITE TIME.")
    print("  BOTH singularities are reached in finite proper time!")

    # ===================================================================
    # Nature of singularities in the internal space
    # ===================================================================
    print()
    print("  NATURE OF THE SINGULARITIES IN THE FULL 12D SPACETIME:")
    print()
    print("  The 12D metric is:")
    print("    ds^2 = -dt^2 + a(t)^2 dx_3^2 + g_{ab}(s(t)) w^a w^b")
    print()
    print("  When s(t) -> +infinity in finite t:")
    print("    - g_{SU2} = 3 e^{-2s} -> 0 : SU(2) directions COLLAPSE")
    print("    - g_{C2}  = 3 e^{s} -> inf : C^2 directions EXPAND")
    print("    - g_{U1}  = 3 e^{2s} -> inf : U(1) direction EXPANDS")
    print("    - Volume = constant (TT): shape change, not volume change")
    print("    - K(s) -> infinity: GENUINE curvature singularity")
    print("    -> The SU(3) internal space degenerates: SU(2) fiber collapses.")
    print("    -> This is a SPACELIKE singularity in the (t,s) mini-superspace")
    print("       (it occurs at a specific finite time t*, simultaneously everywhere).")
    print()
    print("  When s(t) -> -infinity in finite t:")
    print("    - g_{SU2} = 3 e^{-2s} -> inf : SU(2) directions EXPAND")
    print("    - g_{C2}  = 3 e^{s} -> 0 : C^2 directions COLLAPSE")
    print("    - g_{U1}  = 3 e^{2s} -> 0 : U(1) direction COLLAPSES")
    print("    - K(s) -> infinity: GENUINE curvature singularity")
    print("    -> The coset C^2 and U(1) fiber collapses.")
    print("    -> Also SPACELIKE in the (t,s) mini-superspace.")

    return


# =============================================================================
# PART 4: CONFORMAL COMPACTIFICATION AND PENROSE DIAGRAM
# =============================================================================

def part4_penrose_diagram():
    """
    Construct the Penrose diagram for the (1+1)D moduli space (t, s).

    The mini-superspace metric is:
      ds^2 = -dt^2 + (1/G_ss) ds^2 = -dt^2 + (1/10) ds^2

    This is (1+1)D Minkowski space with speed of propagation c_s = 1/sqrt(10).
    (Or equivalently, rescale sigma = s/sqrt(10) to get ds^2 = -dt^2 + dsigma^2.)

    However, the DYNAMICS in this space is governed by V_tree(s), which drives
    the modulus to the singularities at s = +/- infinity in finite time.

    The Penrose diagram must show:
    1. The TWO curvature singularities (s = +inf and s = -inf)
    2. The bi-invariant point s = 0 (has no special causal status)
    3. The gauge-viable window s in [0.15, 0.50]
    4. The causal structure: light cones in the (t, s) plane
    5. Conformal infinity (t -> +/- inf at finite s)

    CONFORMAL STRUCTURE:
    The (t, sigma) space with sigma = s/sqrt(10) is flat Minkowski (1+1)D.
    Its Penrose diagram is the standard diamond for (1+1)D Minkowski:

        - Null coordinates: u = t - sigma, v = t + sigma
        - Conformal: U = arctan(u), V = arctan(v)
        - Boundaries: U, V in (-pi/2, pi/2)

    BUT: the physical domain has FINITE s-extent because s -> +/- inf
    are singularities reached in finite time. This truncates the diagram.
    The V_tree potential gives a POTENTIAL WALL at large negative s and
    a RUNAWAY at large positive s, but both endpoints are singularities.

    For the KINEMATIC Penrose diagram (ignoring dynamics, just causal
    structure), the (t, s) mini-superspace with s in (-inf, +inf)
    is conformally equivalent to the full (1+1)D Minkowski diamond.

    For the DYNAMICAL Penrose diagram (including V_tree), the evolution
    s(t) generically reaches a singularity in finite time. The actual
    spacetime is a SUBSET of the Minkowski diamond, bounded by the
    singularity surface.
    """
    separator("PART 4: PENROSE DIAGRAM CONSTRUCTION")

    G_ss = 10.0
    c_s = 1.0 / np.sqrt(G_ss)  # "speed of light" in moduli space

    print(f"  Mini-superspace 'speed of light': c_s = 1/sqrt(G_ss) = {c_s:.6f}")
    print()

    # Rescaled coordinate: sigma = s / sqrt(G_ss) = s / sqrt(10)
    # Then ds^2 = -dt^2 + dsigma^2 is standard (1+1)D Minkowski.

    # Null coordinates in (t, sigma):
    # u = t - sigma, v = t + sigma

    # Conformal compactification:
    # U = arctan(u), V = arctan(v)  both in (-pi/2, pi/2)

    # The singularity s = +inf corresponds to sigma = +inf.
    # In null coordinates, the locus sigma = +inf is either u = -inf or v = +inf
    # (depending on t). In compactified coordinates:
    #   sigma -> +inf at fixed t: U -> arctan(-inf) = -pi/2 or V -> arctan(+inf) = pi/2

    # Similarly s = -inf corresponds to sigma = -inf:
    #   sigma -> -inf at fixed t: U -> arctan(+inf) = pi/2 or V -> arctan(-inf) = -pi/2

    print("  KINEMATIC PENROSE DIAGRAM (causal structure only):")
    print("  ==================================================")
    print()
    print("  Coordinates: sigma = s / sqrt(10)")
    print("  Null coords: u = t - sigma, v = t + sigma")
    print("  Compactified: U = arctan(u), V = arctan(v)")
    print("  Diagram coords: T = (V+U)/2, S = (V-U)/2")
    print("  Range: -pi/2 < U < pi/2, -pi/2 < V < pi/2, V >= U")
    print()

    # The kinematic diagram is just the standard (1+1)D Minkowski diamond.
    # But s = +/- inf are NOT at conformal infinity -- they are in the
    # interior of the compactified space (at finite t) because the
    # singularities are reached in finite proper time!

    # Actually wait. Let me reconsider. In the kinematic picture (no potential),
    # a geodesic at constant velocity ds/dt = const reaches s = +/- infinity
    # only as t -> infinity. But WITH the potential, the acceleration drives
    # s to infinity in finite t. The singularity surface s(t_*) = infinity
    # at finite t_* would appear as a SPACELIKE boundary inside the diamond.

    # For the STATIC picture (fixed s, no dynamics), the internal space is
    # compact SU(3) -- there is no horizon, no singularity, no issue.

    # The interesting diagram arises when we consider s as dynamical.

    # Let me compute the singularity surface t_*(s_0) for different initial s_0.
    print("  DYNAMICAL ANALYSIS: Singularity surfaces")
    print()

    def eom(t, y):
        s_val, sdot = y
        fp = 4*np.exp(2*s_val) - 8*np.exp(-s_val) + 4*np.exp(-4*s_val)
        sddot = (1.0/10.0) * (1.0/10.0) * fp  # -V'/G_ss
        return [sdot, sddot]

    # For the Penrose diagram, we need the CAUSAL STRUCTURE.
    # The key insight: the mini-superspace is (1+1)D Minkowski, but the
    # physical spacetime is bounded by curvature singularities at s = +/- inf.

    # Since s ranges over all of R and the metric is flat (constant G_ss),
    # the KINEMATIC causal structure is exactly (1+1)D Minkowski.

    # The singularities at s = +/- infinity are at spacelike infinity i^0
    # in the standard Penrose diagram. They are NOT reachable in finite
    # proper time along a geodesic of the KINEMATIC metric.

    # BUT: with the POTENTIAL, the modulus is accelerated, and reaches
    # s = +/- infinity in finite coordinate time. This is PHYSICAL but
    # does NOT change the CAUSAL structure (which depends only on the
    # light cone, i.e., the conformal class of the metric).

    # RESOLUTION: The Penrose diagram for the causal structure IS the
    # standard (1+1)D Minkowski diamond. The singularities at s = +/- inf
    # are at spatial infinity i^0. The physical evolution creates
    # SPACELIKE singularity surfaces at finite t, but these are
    # dynamical features, not causal boundaries.

    # HOWEVER: from the perspective of the FULL 12D spacetime, the
    # singularity at s = s_c occurs at finite t_*. The 12D curvature
    # invariant K_12D diverges at this t_*. This IS a spacelike
    # singularity in the 12D spacetime.

    # So the PENROSE DIAGRAM FOR THE 12D SPACETIME has a spacelike
    # singularity boundary at t = t_* (like the Big Crunch in FRW).

    print("  The (1+1)D mini-superspace (t, sigma = s/sqrt(10)) has a")
    print("  conformally FLAT metric (it IS Minkowski). The causal structure")
    print("  is therefore the standard (1+1)D Minkowski diamond.")
    print()
    print("  However, the V_tree potential drives s(t) to s = +infinity in")
    print("  FINITE proper time t_*. At this time, the 12D Kretschner scalar")
    print("  K(s) -> infinity. This is a SPACELIKE curvature singularity")
    print("  in the full 12D spacetime, analogous to the Big Crunch in FRW.")
    print()
    print("  The diagram is therefore a TRUNCATED Minkowski diamond, with")
    print("  the future singularity as an upper spacelike boundary.")

    return


# =============================================================================
# PART 5: PENROSE SINGULARITY THEOREM APPLICABILITY
# =============================================================================

def ricci_eigenvalues_analytic(s):
    """
    Compute the 3 distinct Ricci eigenvalues ANALYTICALLY.

    For the Jensen metric g_s = 3*diag(e^{-2s}[3], e^s[4], e^{2s}[1]),
    the Ricci tensor in the ON frame has eigenvalues determined by the
    connection coefficients. From the R(s) formula and the structure of
    the Ricci tensor on a 3-parameter left-invariant metric on SU(3):

    R(s) = 3*ric_su2(s) + 4*ric_c2(s) + 1*ric_u1(s)
    |Ric|^2(s) = 3*ric_su2(s)^2 + 4*ric_c2(s)^2 + 1*ric_u1(s)^2

    We know from SP-2 that ric_u1 = 1/4 for all s.
    With R(s) and |Ric|^2(s) known exactly, we can solve for ric_su2 and ric_c2.
    """
    R = R_exact(s)
    Ric2 = Ric2_exact(s)
    ric_u1 = 0.25  # proven s-independent in SP-2

    # R = 3*a + 4*b + c where a=ric_su2, b=ric_c2, c=1/4
    # => 3*a + 4*b = R - 1/4
    # |Ric|^2 = 3*a^2 + 4*b^2 + 1/16
    # => 3*a^2 + 4*b^2 = Ric2 - 1/16

    # From first: a = (R - 1/4 - 4*b) / 3
    # Substitute: 3*((R - 1/4 - 4*b)/3)^2 + 4*b^2 = Ric2 - 1/16
    # (R - 1/4 - 4*b)^2 / 3 + 4*b^2 = Ric2 - 1/16
    # Let P = R - 1/4, Q = Ric2 - 1/16
    # (P - 4b)^2 / 3 + 4b^2 = Q
    # P^2 - 8Pb + 16b^2 + 12b^2 = 3Q
    # 28b^2 - 8Pb + P^2 - 3Q = 0
    # b = (8P +/- sqrt(64P^2 - 4*28*(P^2 - 3Q))) / (2*28)
    # b = (8P +/- sqrt(64P^2 - 112P^2 + 336Q)) / 56
    # b = (8P +/- sqrt(-48P^2 + 336Q)) / 56
    # b = (8P +/- sqrt(48*(7Q - P^2))) / 56

    P = R - 0.25
    Q = Ric2 - 1.0/16.0

    disc = 48.0 * (7.0 * Q - P * P)
    if disc < 0:
        disc = 0.0  # numerical noise

    sqrt_disc = np.sqrt(disc)
    b1 = (8.0 * P + sqrt_disc) / 56.0
    b2 = (8.0 * P - sqrt_disc) / 56.0

    a1 = (P - 4.0 * b1) / 3.0
    a2 = (P - 4.0 * b2) / 3.0

    # Which root is correct? At s=0, all eigenvalues = 1/4.
    # a1 at s=0 should be 1/4.
    if abs(s) < 1e-10:
        return 0.25, 0.25, 0.25

    # For s > 0, su2 eigenvalue decreases, c2 increases.
    # Pick the root where a < b (su2 < c2 for s > 0).
    if a1 < b1:
        return a1, b1, ric_u1
    else:
        return a2, b2, ric_u1


def part5_singularity_theorem():
    """
    Apply (or explain failure of) the Penrose singularity theorem.
    """
    separator("PART 5: PENROSE SINGULARITY THEOREM")

    print("""
  PENROSE SINGULARITY THEOREM (1965):
  ====================================
  If a spacetime (M, g) satisfies:
    (a) The null energy condition: R_mu_nu k^mu k^nu >= 0 for all null k
    (b) There exists a non-compact Cauchy surface
    (c) There exists a closed trapped surface

  THEN M is null geodesically incomplete (contains a singularity).

  APPLICATION TO THE INTERNAL SPACE (SU(3), g_s):
  ================================================

  CHECK (a) -- NULL ENERGY CONDITION:
    The internal space (SU(3), g_s) satisfies the vacuum Einstein equations
    WITH cosmological constant (the scalar curvature R(s) acts as a
    cosmological constant). For a left-invariant metric on a Lie group:

      Ric_{ab} = eigenvalue * g_{ab}  (at s=0: Einstein manifold, Ric = (1/4) g)
      At s > 0: Ricci has 3 distinct eigenvalues (su2, C2, u1).
""")

    # Compute Ricci eigenvalues ANALYTICALLY (no slow numerical Riemann tensor)
    print("    Ricci eigenvalues at key s values (ANALYTIC):")
    print(f"    {'s':>6}  {'su2 (x3)':>14}  {'C2 (x4)':>14}  {'u1 (x1)':>14}  {'NEC':>8}")
    print(f"    {'-'*6}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*8}")

    nec_violations = []
    for s in [0.0, 0.15, 0.30, 0.50, 1.0, 1.3, 1.5, 2.0, 2.5, 3.0]:
        su2_val, c2_val, u1_val = ricci_eigenvalues_analytic(s)

        # NEC: all Ricci eigenvalues >= 0? (for Riemannian manifold, this is
        # the positive Ricci curvature condition, which is the analog of NEC)
        all_positive = (su2_val >= -1e-10 and c2_val >= -1e-10 and u1_val >= -1e-10)
        nec_status = "PASS" if all_positive else "FAIL"
        if not all_positive:
            nec_violations.append(s)

        print(f"    {s:6.2f}  {su2_val:14.8f}  {c2_val:14.8f}  {u1_val:14.8f}  {nec_status:>8}")

    # Find exact NEC crossover by bisection on su2 Ricci eigenvalue
    def su2_ric(s):
        a, b, c = ricci_eigenvalues_analytic(s)
        return a

    from scipy.optimize import brentq as _brentq
    try:
        s_nec = _brentq(su2_ric, 0.5, 1.5)
    except Exception:
        s_nec = None

    print()
    if nec_violations:
        nec_msg = f"    NEC VIOLATED at s >= {min(nec_violations):.2f}"
        if s_nec is not None:
            nec_msg += f"  (exact crossover: s_NEC = {s_nec:.6f})"
        print(nec_msg)
        print(f"    (su(2) Ricci eigenvalue goes NEGATIVE)")
    else:
        print(f"    NEC satisfied at all tested s values")

    print(f"""
  CHECK (b) -- NON-COMPACT CAUCHY SURFACE:
    The internal space SU(3) is COMPACT. There is no non-compact Cauchy surface
    within the internal space itself.

    For the FULL mini-superspace (t, s): the Cauchy surface is the constant-t
    slice, which is the real line s in (-inf, +inf). This IS non-compact.

    CHECK (b) PASSES for the mini-superspace, FAILS for the internal space.

  CHECK (c) -- TRAPPED SURFACE:
    SU(3) is compact. In a compact Riemannian manifold, EVERY closed surface
    has the property that outgoing normals converge (by compactness).
    However, this is in the Riemannian (spatial) context, not Lorentzian.

    In the (1+1)D Lorentzian mini-superspace: a "trapped surface" is just a
    single point (0-dimensional surface). There is no meaningful trapped
    surface in (1+1)D.

    CHECK (c) FAILS in (1+1)D.
""")

    print("  VERDICT ON PENROSE SINGULARITY THEOREM:")
    print("  ----------------------------------------")
    print("  The Penrose singularity theorem DOES NOT APPLY to this setup because:")
    print()
    print("  1. The internal space SU(3) is COMPACT (violates condition (b)).")
    print("     The Penrose theorem requires a non-compact Cauchy surface.")
    print("     Compact Riemannian manifolds are automatically geodesically")
    print("     complete (by Hopf-Rinow), so the theorem is not needed.")
    print()
    print("  2. The (1+1)D mini-superspace has no trapped surfaces (dim too low).")
    print("     The concept of trapped surface requires codimension-2 submanifolds")
    print("     in a spacetime of dimension >= 3.")
    print()
    print("  3. The NEC is VIOLATED for s > ~0.8 (su(2) Ricci eigenvalue goes negative).")
    print("     Even if conditions (b) and (c) held, the theorem would not apply")
    print("     beyond s ~ 0.78 (exact crossover from bisection).")
    print()
    print("  NEVERTHELESS: The moduli space IS geodesically incomplete.")
    print("  The singularity at s -> +infinity is reached in finite proper time.")
    print("  This is not a consequence of the Penrose theorem, but of the")
    print("  V_tree runaway: the potential has no minimum, so the modulus")
    print("  accelerates unboundedly.")
    print()
    print("  ANALOGY: This is like a particle falling off a cliff in Newtonian")
    print("  mechanics. The singularity is dynamical, not geometric.")
    print("  Stabilization (Coleman-Weinberg corrections) would prevent the")
    print("  singularity by creating a potential minimum at finite s.")

    return nec_violations


# =============================================================================
# PART 6: THE PENROSE DIAGRAM (ASCII)
# =============================================================================

def part6_ascii_penrose():
    """
    Construct and display the Penrose diagram.
    """
    separator("PART 6: THE PENROSE DIAGRAM")

    print("""
  PENROSE DIAGRAM FOR THE (t, s) MODULI SPACE
  ==============================================

  The mini-superspace metric is ds^2 = -dt^2 + (1/10) ds^2.
  This is conformally equivalent to (1+1)D Minkowski space.

  KINEMATIC diagram (without potential, s ranges over all of R):

                      i^+
                       /\\
                      /  \\
                     /    \\
                    /      \\
            I^+_L /        \\ I^+_R
                 /          \\
                /    FUTURE   \\
               /              \\
    i^0_L  --<      (t,s)     >--  i^0_R
    (s=-inf)   \\              /   (s=+inf)
                \\    PAST    /
                 \\          /
            I^-_L \\        / I^-_R
                    \\      /
                     \\    /
                      \\  /
                       \\/
                      i^-

  LABELS:
    i^+         = future timelike infinity (t -> +inf at finite s)
    i^-         = past timelike infinity (t -> -inf at finite s)
    i^0_L       = left spacelike infinity (s -> -inf, K -> inf: SINGULARITY)
    i^0_R       = right spacelike infinity (s -> +inf, K -> inf: SINGULARITY)
    I^+_L, I^+_R = future null infinity (left/right)
    I^-_L, I^-_R = past null infinity (left/right)

  -----------------------------------------------------------------------

  DYNAMICAL diagram (with V_tree potential, runaway to s -> +inf):

  V_tree(s) has NO minimum for s > 0. It drives the modulus toward
  s -> +infinity. Starting from any s_0 >= 0, the modulus reaches
  s = +infinity (curvature singularity) in FINITE time t_*.

  The physical spacetime is therefore TRUNCATED by a future spacelike
  singularity:

                  ~~~~~~~~~~~~~ s = +inf SINGULARITY (K -> inf) ~~~
                 /|             |               |               |\\
                / |             |               |               | \\
               /  |    s=0.30   |     s=1.0     |    s -> inf   |  \\
              /   |  (sin^2 thW)|               |  (singularity)|   \\
             /    |             |               |               |    \\
            /     |             |               |               |     \\
           /      |   GAUGE     |   TRANS-      |   SINGULAR    |      \\
          /       |   WINDOW    |   ITION       |   REGION      |       \\
    s=-inf        | s in        |   ZONE        | K >> 1        |    s=+inf
   (sing.) --<    |[0.15,0.50]  |               |               |    >--(sing.)
          \\       |             |               |               |       /
           \\      |             |               |               |      /
            \\     |             |               |               |     /
             \\    |    s=0      |     s=0.5     |               |    /
              \\   | (bi-inv)    |               |               |   /
               \\  |  K=0.5     |               |               |  /
                \\ |             |               |               | /
                 \\|             |               |               |/
                  ~~~~~~~~~~~~~ s = -inf SINGULARITY (K -> inf) ~~~

  In this DYNAMICAL picture:
  - The upper boundary is a spacelike singularity where s -> +infinity
    (SU(2) collapses, K diverges as (1/12) e^{4s})
  - The lower boundary is a spacelike singularity where s -> -infinity
    (C^2 and U(1) collapse, K diverges as (23/96) e^{-8s})
  - WITHOUT V_eff stabilization, the modulus ALWAYS hits one singularity
  - WITH V_eff stabilization at s_0, the modulus oscillates around s_0
    and NEVER reaches the singularity (the stabilized spacetime is
    geodesically complete)

  -----------------------------------------------------------------------

  PHYSICALLY REALIZED DIAGRAM (with CW stabilization at s_0 ~ 0.3):

               i^+  (t -> +infinity)
                /\\
               /  \\
              /    \\
             /      \\
            / STABLE  \\
           / s ~ s_0   \\
          /  oscillates  \\
         /    around s_0  \\
  i^0_L /                  \\ i^0_R
  (s=-inf)   s = s_0      (s=+inf)
  (V_eff \\  (V_eff min)  / (V_eff
  barrier) \\            /  barrier)
            \\          /
             \\        /
              \\      /
               \\    /
                \\  /
                 \\/
                i^-

  In the STABILIZED case:
  - V_eff(s) has a minimum at s_0 ~ 0.30
  - The modulus oscillates: s(t) = s_0 + delta*cos(omega*t)
  - The effective potential creates barriers at both sides
  - The singularities at s = +/- inf are BEHIND potential barriers
  - The spacetime is geodesically COMPLETE
  - This is analogous to the Reissner-Nordstrom INNER horizon:
    the potential barrier prevents the singularity from being reached

  KEY STRUCTURAL RESULT:
    Tree-level V_tree -> geodesically INCOMPLETE (singularity in finite time)
    Stabilized V_eff  -> geodesically COMPLETE (modulus trapped near s_0)
    The Coleman-Weinberg correction is therefore ESSENTIAL for
    physical consistency. Without it, the framework predicts its own
    destruction (the internal space degenerates).
""")


# =============================================================================
# PART 7: WEYL CURVATURE HYPOTHESIS
# =============================================================================

def part7_weyl_hypothesis():
    """
    Apply Penrose's Weyl curvature hypothesis to the internal space.
    """
    separator("PART 7: PENROSE'S WEYL CURVATURE HYPOTHESIS")

    print("""
  Penrose's Weyl Curvature Hypothesis (WCH):
  ===========================================
  The Weyl tensor was zero (or near-zero) at the Big Bang and grows
  through gravitational clumping, providing the arrow of time.

  For the INTERNAL space (SU(3), g_s):
  ------------------------------------
  The Weyl tensor |C|^2(s) is nonzero for ALL s (including s=0).
  The bi-invariant metric g_0 is NOT conformally flat.

  This means the WCH does NOT apply in its standard form to the
  internal space.

  HOWEVER: Consider the TIDAL FRACTION |C|^2 / K:
""")

    s_array = np.linspace(0, 3, 61)
    print(f"    {'s':>6}  {'|C|^2':>14}  {'K':>14}  {'|C|^2/K':>10}  {'|C|^2/|C|^2(0)':>16}")
    print(f"    {'-'*6}  {'-'*14}  {'-'*14}  {'-'*10}  {'-'*16}")

    W2_0 = Weyl2_exact(0)
    for s in s_array[::6]:
        W2 = Weyl2_exact(s)
        K = K_exact(s)
        tidal = W2 / K if K > 1e-15 else float('nan')
        growth = W2 / W2_0
        print(f"    {s:6.2f}  {W2:14.6e}  {K:14.6e}  {tidal:10.6f}  {growth:16.6f}")

    print("""
  OBSERVATIONS:
  1. |C|^2 grows MONOTONICALLY with s (gravitational tidal effects increase)
  2. |C|^2/K DECREASES with s (Ricci grows FASTER than Weyl)
  3. At s=0 (most symmetric point): |C|^2/K = 5/7 = 0.714

  INTERPRETATION FOR EXFLATION:
  - If exflation starts at s=0 (maximum symmetry, bi-invariant), the
    Weyl tensor is nonzero but at its MINIMUM absolute value.
  - As s increases during exflation, |C|^2 grows -- consistent with
    the Penrose WCH (gravitational clumping increases Weyl).
  - The RATIO |C|^2/K decreases, meaning the Ricci (matter) contribution
    grows faster than the Weyl (tidal) contribution.
  - This is CONSISTENT with exflation being driven by matter (phonon
    condensate) rather than by tidal forces.

  MODIFIED WCH FOR THE INTERNAL SPACE:
  The appropriate statement is: the Jensen deformation parameter s
  increases monotonically from s=0, and the Weyl curvature |C|^2
  increases monotonically with s. The "initial condition" s=0
  corresponds to maximum symmetry (bi-invariant SU(3)), which is the
  analog of "Weyl = 0" for a space that cannot be conformally flat.

  s=0 is the MOST SYMMETRIC point (full SU(3)_L x SU(3)_R isometry).
  For s > 0, symmetry breaks to SU(2) x U(1) (the SM gauge group!).
  Weyl growth accompanies symmetry breaking. This is the geometric
  arrow of time for the internal space.
""")


# =============================================================================
# PART 8: SUMMARY AND DELIVERABLES
# =============================================================================

def part8_summary():
    """Print the complete SP-3 deliverable."""
    separator("SP-3 COMPLETE DELIVERABLE")

    print("""
  =====================================================================
  SP-3: HIGHER-DIMENSIONAL PENROSE DIAGRAM FOR (SU(3), g_{s(t)})
  =====================================================================

  METRIC:
    Full: ds^2 = -dt^2 + a(t)^2 dx_3^2 + g_{ab}(s(t)) w^a w^b
    Mini-superspace: ds^2 = -dt^2 + (1/10) ds^2  [FLAT Minkowski (1+1)D]
    DeWitt metric: G_ss = 10 (CONSTANT, s-independent)

  CURVATURE SINGULARITY STRUCTURE:
    s -> +infinity: K ~ (1/12) e^{4s} -> infinity (SU(2) collapses)
    s -> -infinity: K ~ (23/96) e^{-8s} -> infinity (C^2 + U(1) collapse)
    Finite s: K(s) FINITE, g_s positive definite. NO singularity.

  GEODESIC COMPLETENESS:
    Kinematic (no potential): COMPLETE. The mini-superspace is flat Minkowski.
    Dynamical (with V_tree):  INCOMPLETE. The tree-level potential V_tree(s)
      has no minimum. The modulus s(t) is accelerated toward s = +infinity
      (or -infinity), reaching the curvature singularity in FINITE proper time.
      Estimate: t_* ~ 5 e^{-s_0} (from s_0 to s = +infinity).
    Stabilized (with V_eff): COMPLETE. If the 1-loop CW correction creates
      a potential minimum at s_0, the modulus is trapped and the spacetime
      is geodesically complete.

  PENROSE SINGULARITY THEOREM:
    DOES NOT APPLY. Three independent reasons:
    (1) Internal space SU(3) is COMPACT (no non-compact Cauchy surface)
    (2) (1+1)D mini-superspace has no trapped surfaces (dimension too low)
    (3) Null energy condition VIOLATED for s > 0.778 (su(2) Ricci < 0)

    The geodesic incompleteness is DYNAMICAL (V_tree runaway),
    not GEOMETRIC (no trapped surface focusing).

  PENROSE DIAGRAM (ASCII):

    TREE-LEVEL (UNSTABILIZED):

                    ~~~~~~~~~~~~ SINGULARITY (s->+inf, K->inf) ~~~~~~~~~~~~
                   /             su(2) collapses                          \\
                  /              K ~ (1/12)e^{4s}                          \\
                 /                                                          \\
                /     s=0.15         s=0.30          s=1.0       s>>1        \\
               /     (gauge)      (sin^2 thW)     (trans.)    (singular)     \\
              /                                                               \\
             /              PHYSICAL SPACETIME                                 \\
    i^0_L  <                 (t, s) plane                                      > i^0_R
    (s=-inf) \\          (flat Minkowski 1+1D)                                /  (s=+inf)
    K->inf    \\                                                             /   K->inf
               \\                                                           /
                \\     s=0.15         s=0.30          s=1.0       s>>1      /
                 \\    (gauge)      (sin^2 thW)     (trans.)   (singular) /
                  \\                                                      /
                   \\             C^2 + U(1) collapse                    /
                    ~~~~~~~~~~~~ SINGULARITY (s->-inf, K->inf) ~~~~~~~~~

    45-degree lines are null geodesics (light cones).
    Both top and bottom boundaries are SPACELIKE curvature singularities.
    i^0_L and i^0_R are ALSO singularities (reached in finite t).
    This spacetime has NO regular conformal infinity.

    STABILIZED (V_eff minimum at s_0):

                         i^+  (t -> +infinity)
                          /\\
                         /  \\
                        /    \\
                       /      \\
                      /        \\
                     /  STABLE   \\
                    /   REGION    \\
                   /  s ~ s_0     \\
                  /  (oscillates)  \\
    s -> -inf    /                  \\   s -> +inf
    (behind  ) </   s = s_0 ~0.30   \\> (behind
     V_eff     |   GAUGE COUPLING    |   V_eff
     barrier)  |     MATCH HERE      |  barrier)
                \\                  /
                 \\   STABLE      /
                  \\  REGION    /
                   \\          /
                    \\        /
                     \\      /
                      \\    /
                       \\  /
                        \\/
                        i^-  (t -> -infinity)

    The singularities are BEHIND potential barriers.
    The physical spacetime is geodesically COMPLETE.
    i^+, i^- are regular timelike infinities.
    The modulus oscillates around s_0 forever.

  WEYL CURVATURE HYPOTHESIS:
    |C|^2 grows monotonically with s (Weyl increases during exflation).
    |C|^2/K DECREASES (Ricci grows faster than Weyl).
    s=0 is maximum symmetry (bi-invariant SU(3)): analog of "Weyl = 0".
    Symmetry breaking SU(3)xSU(3) -> SU(2)xU(1) accompanies Weyl growth.
    Consistent with Penrose's geometric arrow of time.

  KEY PHYSICAL CONCLUSION:
    V_eff stabilization is not just a technical detail.
    Without it, the framework PREDICTS ITS OWN DESTRUCTION:
    the internal space degenerates in finite time.
    The Coleman-Weinberg correction is ESSENTIAL for physical consistency.
    This makes the V_eff minimum computation (Tier 1.5) even more decisive.
""")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 76)
    print("  SP-3: HIGHER-DIMENSIONAL PENROSE DIAGRAM")
    print("  Schwarzschild-Penrose-Geometer -- Session 17c")
    print("=" * 76)

    # Part 1: Mini-superspace metric
    G_ss = part1_minisuperspace()

    # Part 2: Singularity analysis
    part2_singularity_analysis()

    # Part 3: Geodesic completeness
    part3_geodesic_completeness()

    # Part 4: Penrose diagram construction
    part4_penrose_diagram()

    # Part 5: Singularity theorem applicability
    nec_violations = part5_singularity_theorem()

    # Part 6: ASCII Penrose diagram
    part6_ascii_penrose()

    # Part 7: Weyl curvature hypothesis
    part7_weyl_hypothesis()

    # Part 8: Summary
    part8_summary()

    print("\n" + "=" * 76)
    print("  SP-3 COMPUTATION COMPLETE.")
    print("  Script: tier0-computation/sp3_penrose_diagram.py")
    print("=" * 76)
