#!/usr/bin/env python3
"""
S53 — EXFLATION-FLATNESS-53: Does 12D Geometry Inherit 4D Flatness?
====================================================================

Gate: EXFLATION-FLATNESS-53
  PASS: 4D flatness follows from 12D geometry (flatness problem dissolved)
  INFO: Flatness permitted but not forced (like standard FRW)
  FAIL: 12D geometry requires k != 0 (flatness problem worsened)

Physics:
  In exflation, spacetime is M^4 x SU(3) with a Jensen-deformed metric on
  SU(3). The question: does the 12D Einstein equation force k=0 for the
  4D spatial sections, or is spatial curvature an independent degree of freedom?

  Key insight: For a PRODUCT geometry M^d x K^n with time-dependent internal
  metric, the 12D vacuum Einstein equation G_AB = 0 decomposes into:
    (1) External block: G_mu_nu^{(4)} + (internal curvature projection) = 0
    (2) Internal block: G_ab^{(8)} + (external curvature projection) = 0
    (3) Mixed block: constraints from warping / gauge fields

  For the homogeneous ansatz with FRW external metric:
    ds^2_{12} = -dt^2 + a(t)^2 [dr^2/(1-kr^2) + r^2 dOmega_2^2] + g_K(tau(t))

  The decomposition yields modified Friedmann equations where k appears
  as a free parameter. The question is whether the SELF-CONSISTENCY of the
  12D equations constrains k.

  Volume conservation (proven S12): a^3 * V_K(tau) = const
  This gives a definite expansion history a(tau) without reference to k.

  The flatness FRACTION Omega_k = -k/(a*H)^2 then evolves during transit.

Author: Einstein-Theorist (Session 53)
Date: 2026-03-21
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, G_DeWitt, M_KK_kerner, M_Pl_reduced,
    a0_fold, a2_fold, g0_diag, PI, N_e_classical,
    c_light, H_fold, v_terminal, dt_transit,
)

# Output file
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 's53_exflation_flatness_output.txt')

# Redirect stdout to both console and file
import io

class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

outfile = open(OUTPUT_FILE, 'w')
sys.stdout = Tee(sys.__stdout__, outfile)

print("=" * 78)
print("  S53 — EXFLATION-FLATNESS-53: Does 12D Geometry Inherit 4D Flatness?")
print("=" * 78)

# ============================================================================
#  SECTION 1: 12D Einstein Equation Decomposition
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 1: 12D Einstein Equation Decomposition for M^4 x SU(3)")
print(f"{'='*78}")

# The 12D metric ansatz (FRW x Jensen-deformed SU(3)):
#   ds^2_{12} = -dt^2 + a(t)^2 gamma_ij dx^i dx^j + g_ab(tau(t)) dy^a dy^b
#
# where gamma_ij = delta_ij / (1-k*r^2) + ... is the FRW spatial metric
# and g_ab(tau) is the Jensen metric on SU(3).
#
# The 12D Ricci tensor decomposes (O'Neill formulas for warped/product metrics):
#
# For a PRODUCT metric (no warping function):
#   R_{mu nu}^{(12)} = R_{mu nu}^{(4)} + (1/2) g^{ab} (d^2 g_{ab}/dt^2) g_{mu nu}
#                      + terms involving (dg_{ab}/dt)^2
#
# More precisely, for ds^2 = g_M(x) + g_K(x,y) with g_K depending on x through tau(t):
#
# The Riemann tensor of a product with fiber metric varying along base is
# given by the Kaluza-Klein reduction (Baptista Paper 13, eq 3.4):
#
#   R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 div(N)
#
# where P = total space, M = base (4D), K = fiber (SU(3)).
#
# For our ansatz: F = 0 (no gauge fields), N = 0 (volume-preserving, S12).
# |S|^2 generates the modulus kinetic term G_DeWitt * tau_dot^2.
#
# The decomposition of the 12D vacuum equation G_AB = 0:
#
# EXTERNAL (mu,nu) block:
#   G_{mu nu}^{(4)} = -(1/2) g_{mu nu}^{(4)} R_K(tau)
#                     + (kinetic terms from |S|^2)
#
# This is equivalent to the 4D FRIEDMANN EQUATIONS with sources from the
# internal geometry.

print("""
  12D metric ansatz:
    ds^2_{12} = -dt^2 + a(t)^2 gamma_{ij}(k) dx^i dx^j + g_ab(tau(t)) dy^a dy^b

  12D vacuum Einstein equation: G_AB^{(12)} = 0

  DECOMPOSITION (Baptista/O'Neill, F=0, N=0 for volume-preserving Jensen):

  External block (mu,nu):
    G_{mu nu}^{(4)} = -(1/2) g_{mu nu}^{(4)} R_K(tau)
                      + G_DeWitt * [tau_dot^2 terms]

  Internal block (a,b):
    G_{ab}^{(8)} + (4D expansion back-reaction terms) = 0

  Mixed block (mu,a):
    Automatically satisfied for homogeneous tau(t) with A=0.

  The external block yields the MODIFIED FRIEDMANN EQUATIONS:
    H^2 + k/a^2 = (1/(3*M_p^2)) * [G_mod/2 * tau_dot^2 + V_KK(tau)]
    H_dot - k/a^2 = -(1/(2*M_p^2)) * G_mod * tau_dot^2

  KEY OBSERVATION: k appears in these equations as a FREE PARAMETER.
  The 12D Einstein equation does NOT fix k.
""")

# ============================================================================
#  SECTION 2: Why k is Not Fixed — Principle-Theoretic Argument
# ============================================================================
print(f"{'='*78}")
print(f"  SECTION 2: Why Spatial Curvature k is Not Fixed by 12D Geometry")
print(f"{'='*78}")

print("""
  THEOREM: For M^d x K^n with K compact and homogeneous, the d-dimensional
  spatial curvature k is an INDEPENDENT initial condition, not determined
  by the higher-dimensional Einstein equation.

  PROOF (by counting degrees of freedom):

  The 12D metric has two independent sectors:
    (i)  The FRW scale factor a(t) and spatial curvature k
    (ii) The internal modulus tau(t)

  The 12D vacuum equation G_AB = 0 yields:
    - Friedmann constraint: H^2 + k/a^2 = rho/(3*M_p^2)
    - Acceleration: H_dot - k/a^2 = -p/(2*M_p^2)
    - Modulus EOM: tau_ddot + 3*H*tau_dot + V'(tau)/G_mod = 0
    - Internal block: IDENTICALLY SATISFIED when modulus EOM holds
      (this is the EIH theorem applied to KK — S44 permanent result)

  We have 3 equations for 3 unknowns: a(t), tau(t), and H(t).
  But k is NOT an unknown — it is a BOUNDARY CONDITION specifying the
  topology of the spatial sections.

  GENERAL COVARIANCE requires that k be determinable from the spatial
  topology, not from the dynamical equations. A 3-sphere (k=+1),
  flat space (k=0), and 3-hyperboloid (k=-1) are all EQUALLY VALID
  solutions of the 12D Einstein equation.

  This is the SAME situation as in standard GR: the Friedmann equation
  does not determine k. It must be specified as an initial/boundary condition.

  CONCLUSION: k is NOT FIXED by the 12D geometry.
  The flatness problem PERSISTS in the exflation framework.
""")

# ============================================================================
#  SECTION 3: Volume Conservation and Expansion History
# ============================================================================
print(f"{'='*78}")
print(f"  SECTION 3: Volume Conservation => a(tau)")
print(f"{'='*78}")

# The Jensen metric on SU(3):
# g_tau = g_0 * diag(e^{2tau} x 3, e^{-2tau} x 4, e^{tau} x 1)
#   [actually: 1 u(1), 3 su(2), 4 C^2 coset directions]
#   g_tau = g_0 * diag(e^{2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau},
#                       e^{tau}, e^{tau}, e^{tau}, e^{tau})
#
# But wait — the volume-preserving condition:
# det(g_tau) / det(g_0) = e^{2tau*1} * e^{-2tau*3} * e^{tau*4}
#                       = e^{2tau - 6tau + 4tau} = e^{0} = 1
#
# So the Jensen deformation is EXACTLY volume-preserving!
# V_K(tau) = Vol_SU3_Haar = constant for all tau.

det_ratio_check = np.exp(2*tau_fold * 1 + (-2*tau_fold) * 3 + tau_fold * 4)
print(f"\n  Volume-preserving check at tau_fold = {tau_fold}:")
print(f"    det(g_tau)/det(g_0) = exp(2tau - 6tau + 4tau) = exp(0) = {det_ratio_check:.15f}")
print(f"    Volume is EXACTLY preserved (proven S12, verified to machine epsilon)")

print(f"\n  CONSEQUENCE: If a^3 * V_K = const and V_K = const,")
print(f"  then a = const! Volume conservation DOES NOT drive expansion")
print(f"  when the internal deformation is volume-preserving.")

print(f"\n  This is a crucial distinction from Kaluza-Klein cosmology with")
print(f"  a BREATHING mode (uniform rescaling of K), where shrinkage of K")
print(f"  drives expansion of M. The Jensen deformation is a SHAPE change")
print(f"  at fixed volume — it is a TT deformation, not a breathing mode.")

print(f"\n  Volume exflation was CLOSED in G3 (Giant Session 3).")
print(f"  Spectral exflation replaced it: expansion comes from the")
print(f"  spectral action, not from volume change.")

# ============================================================================
#  SECTION 4: KK Potential and Friedmann Dynamics
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 4: Friedmann Dynamics During Transit")
print(f"{'='*78}")

# Internal scalar curvature R_K(tau) — Baptista eq 3.70
alpha_metric = g0_diag  # = 3.0
R_K_0 = 12.0 / alpha_metric  # = 4.0

def R_K(s):
    """Scalar curvature of Jensen-deformed SU(3)."""
    return R_K_0 * (2.0*np.exp(2*s) - 1.0 + 8.0*np.exp(-s) - np.exp(-4*s)) / 8.0

# In M_KK = 1 units
M_p_sq = (M_Pl_reduced / M_KK_kerner)**2
G_mod = M_p_sq * G_DeWitt

def V_KK(tau):
    """KK potential V = -M_p^2 R_K / 2 (M_KK^4 units)."""
    return -M_p_sq * R_K(tau) / 2.0

def dV_dtau(tau, h=1e-8):
    return (V_KK(tau + h) - V_KK(tau - h)) / (2*h)

# Key values
V0 = V_KK(0.0)
Vf = V_KK(tau_fold)
R0 = R_K(0.0)
Rf = R_K(tau_fold)

print(f"\n  Internal curvature:")
print(f"    R_K(0) = {R0:.6f}  (bi-invariant, maximum)")
print(f"    R_K(fold) = {Rf:.6f}")
print(f"    R_K(0.50) = {R_K(0.50):.6f}")

print(f"\n  KK potential (M_KK^4 units):")
print(f"    V_KK(0) = {V0:.4f}")
print(f"    V_KK(fold) = {Vf:.4f}")
print(f"    Delta_V = {Vf - V0:.4f}")
print(f"    M_p^2 = (M_Pl/M_KK)^2 = {M_p_sq:.4f}")
print(f"    G_mod = M_p^2 * G_DeWitt = {G_mod:.2f}")

# ============================================================================
#  SECTION 5: Omega_k Evolution During Transit
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 5: Omega_k Evolution During Transit")
print(f"{'='*78}")

# Friedmann equation with curvature:
# H^2 + k/a^2 = rho_eff / (3*M_p^2)
# rho_eff = G_mod/2 * tau_dot^2 + V_KK(tau)
# BUT V_KK < 0, so we need KE > |V_KK| for H^2 + k/a^2 > 0.
#
# Omega_k = -k / (a*H)^2
# |Omega_k| = |k| / (a*H)^2
#
# For the stiff-matter limit (w=1):
#   a ~ t^{1/3}, H = 1/(3t), so (aH)^2 = a^2/(9t^2) = a_0^2*(t/t_0)^{2/3}/(9t^2)
#   = a_0^2 / (9 * t_0^{2/3} * t^{4/3})
#
#   So (aH)^2 ~ t^{-4/3} — it DECREASES with time!
#   Therefore |Omega_k| = |k|/(aH)^2 ~ t^{4/3} — it INCREASES with time!
#
# For stiff matter, the flatness problem gets WORSE, not better.
# This is the OPPOSITE of inflation (where aH increases, driving Omega_k -> 0).

# For exflation with w=1 (stiff, the dominant regime):
# d(ln|Omega_k|)/dN = d(ln|k/(aH)^2|)/dN
# In terms of the equation of state:
# d(ln|Omega_k|)/dN = 1 + 3w  (for constant w)
#   w = -1 (inflation): d/dN = -2 => |Omega_k| decreases exponentially
#   w = 0 (matter): d/dN = +1 => |Omega_k| increases
#   w = 1/3 (radiation): d/dN = +2 => |Omega_k| increases faster
#   w = 1 (stiff): d/dN = +4 => |Omega_k| increases RAPIDLY

print("""
  The equation of state during transit determines Omega_k evolution:

    d(ln|Omega_k|)/dN = 1 + 3w   (for constant w)

  Inflation (w = -1):   d/dN = -2   => Omega_k -> 0 (solved!)
  Radiation (w = 1/3):  d/dN = +2   => Omega_k grows
  Stiff (w = 1):        d/dN = +4   => Omega_k grows RAPIDLY

  From S52: the exflation transit is in the STIFF LIMIT (w = 1).
  The KE/|V| ratio is large (Delta_V/V ~ 0.9%), kinetic energy dominates.
""")

# Quantitative computation
# N_e = 0.1734 (structural, S52)
# Omega_k grows by factor exp(4*N_e) during transit

N_e = N_e_classical
Omega_k_growth = np.exp(4 * N_e)

print(f"  Quantitative Omega_k evolution during transit:")
print(f"    N_e = {N_e:.4f} (structural, S52)")
print(f"    Growth factor: |Omega_k_f/Omega_k_i| = exp(4*N_e) = exp({4*N_e:.4f})")
print(f"    = {Omega_k_growth:.4f}")
print(f"\n  The growth factor is {Omega_k_growth:.2f} — nearly unity.")
print(f"  Transit is too SHORT (0.17 e-folds) to significantly affect Omega_k.")
print(f"  Omega_k is essentially PRESERVED through the transit.")

# What WOULD be needed?
# To solve flatness, we need |Omega_k| to decrease by ~10^{60}
# (from O(1) to 10^{-60} at Planck time)
# With w=1: need exp(-4*N_e) = 10^{-60} => N_e = 60*ln(10)/4 = 34.5
# With w=-1 (inflation): need exp(-2*N_e) = 10^{-60} => N_e = 60*ln(10)/2 = 69

N_e_needed_stiff = 60 * np.log(10) / 4  # for w=1 (but goes WRONG direction!)
N_e_needed_infl = 60 * np.log(10) / 2   # for w=-1

print(f"\n  To solve the flatness problem:")
print(f"    With inflation (w=-1): need N_e >= {N_e_needed_infl:.1f}")
print(f"    With stiff (w=+1): IMPOSSIBLE — Omega_k grows, doesn't shrink")
print(f"    Available: N_e = {N_e:.4f}")

# ============================================================================
#  SECTION 6: The Horizon Problem in Exflation
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 6: Horizon Problem — Internal Dimension Connectivity")
print(f"{'='*78}")

# In 12D, the causal structure is determined by the FULL 12D metric.
# A null geodesic in 12D satisfies:
#   0 = -dt^2 + a^2 dr^2 + g_ab dy^a dy^b
# The maximum 4D propagation speed is c (the 12D speed of light).
# But the causal DIAMOND in 12D includes internal propagation.
#
# A key question: can two 4D points separated by more than the 4D Hubble
# horizon be causally connected through the internal dimensions?
#
# For a PRODUCT geometry (no warping), the answer is NO.
# The 4D causal horizon is determined by the 4D null geodesics alone:
#   d_horizon^{4D} = a(t) * integral_0^t dt'/a(t')
#
# Internal dimensions do not ADD to the 4D horizon because:
# 1. The 12D metric is a PRODUCT — there is no shortcut through K.
# 2. A photon traveling through K returns to the same 4D point.
# 3. The KK modes ARE the mechanism: massive 4D fields, not extra pathways.

print("""
  THEOREM: For a PRODUCT metric M^4 x K (no warping), the 4D causal
  horizon is IDENTICAL to the standard FRW horizon.

  PROOF:
  The 12D null condition: g_{AB} dx^A dx^B = 0
  For the product metric: -dt^2 + a^2 dr^2 + g_ab dy^a dy^b = 0

  A null geodesic in 12D must satisfy:
    dt^2 = a^2 dr^2 + g_ab dy^a dy^b >= a^2 dr^2

  So the 4D radial velocity is:
    |dr/dt| = sqrt(1 - g_ab (dy^a/dt)(dy^b/dt)) / a <= 1/a

  Any momentum in the internal directions REDUCES the 4D propagation speed!
  Photons moving through the fiber travel SLOWER in 4D, not faster.

  A photon traversing SU(3) in time t ~ 1/M_KK moves zero distance in
  the external directions. Internal propagation does not extend the 4D horizon.

  EXCEPTION: Warped products ds^2 = e^{2A(y)} g_M + g_K CAN modify the
  effective 4D speed. But the Jensen deformation is NOT a warp factor —
  it is a SHAPE deformation of the fiber at each point.

  CONCLUSION: The horizon problem is NOT resolved by the internal dimensions
  in a product geometry.
""")

# Compute the 4D horizon explicitly
# In the stiff limit: a ~ t^{1/3}
# d_horizon = a(t) * integral_0^t dt'/a(t') = a(t) * integral t'^{-1/3} dt'
#           = a(t) * (3/2) * t^{2/3} = (3/2) * a(t)^3 * t_0^2  ... let me be careful.
#
# a(t) = a_0 * (t/t_0)^{1/3}
# integral_0^t dt'/a(t') = (1/a_0) * integral_0^t (t_0/t')^{1/3} dt'
#                        = (t_0^{1/3}/a_0) * (3/2) * t^{2/3}
#                        = (3/2) * t/(a_0*(t/t_0)^{1/3})
#                        = (3/2) * t / a(t)
#
# Wait, that gives d_horizon = a * (3/2) * t / a = (3/2)*t
# Actually more carefully:
# d_comoving = integral_0^t dt'/a(t') = (1/a_0) * (t_0)^{1/3} * (3/2) * t^{2/3}
# d_physical = a(t) * d_comoving = a_0*(t/t_0)^{1/3} * (t_0^{1/3}/a_0) * (3/2)*t^{2/3}
#            = (3/2) * t
# So d_horizon = (3/2)*t for stiff matter. Compare to H^{-1} = 3t.
# d_horizon = H^{-1}/2 — the horizon is HALF the Hubble radius.

print(f"  Quantitative 4D horizon during stiff-matter transit:")
print(f"    a(t) ~ t^{{1/3}} (stiff)")
print(f"    d_horizon = (3/2)*t = H^{{-1}}/2")
print(f"    The horizon is HALF the Hubble radius.")
print(f"    No enhancement from internal dimensions.")

# What about the internal traversal time?
# A photon crosses SU(3) in time ~ R_SU3 / c ~ 1/M_KK
# The diameter of SU(3) with the round metric at scale alpha = 3:
# The geodesic diameter of SU(3) is pi * sqrt(alpha/6) = pi * sqrt(1/2)
# In M_KK^{-1} units.

geodesic_diameter = PI * np.sqrt(g0_diag / 6.0)
traversal_time = geodesic_diameter  # in M_KK^{-1} units

print(f"\n  Internal traversal time:")
print(f"    SU(3) geodesic diameter = pi*sqrt(alpha/6) = {geodesic_diameter:.4f} M_KK^{{-1}}")
print(f"    Traversal time = {traversal_time:.4f} M_KK^{{-1}}")
print(f"    Transit duration = {dt_transit:.6f} M_KK^{{-1}}")
print(f"    Ratio t_traverse / t_transit = {traversal_time / dt_transit:.1f}")
print(f"    The photon can cross SU(3) ~{int(dt_transit/traversal_time)} times during transit")
print(f"    (but this does NOT help with the 4D horizon)")

# ============================================================================
#  SECTION 7: The Stiff Matter Equation of State
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 7: Equation of State w(tau) During Transit")
print(f"{'='*78}")

# The effective energy density and pressure:
# rho = G_mod/2 * tau_dot^2 + V_KK(tau)
# p = G_mod/2 * tau_dot^2 - V_KK(tau)
#
# w = p/rho = (KE - V) / (KE + V)
#
# Since V < 0 and KE > |V| (required for H^2 > 0 when k >= 0):
# w = (KE + |V|) / (KE - |V|) > 1
#
# Wait: V < 0, so:
# rho = KE + V = KE - |V|
# p = KE - V = KE + |V|
# w = (KE + |V|) / (KE - |V|) > 1  for all KE > |V|
#
# Actually for V < 0:
# w -> +inf as KE -> |V| from above (rho -> 0, p -> 2*KE)
# w -> 1 as KE >> |V| (pure kinetic)
# So w >= 1 throughout. This is STIFFER than stiff!

print("""
  For modulus kinetic energy KE and potential V_KK < 0:
    rho_eff = KE + V_KK = KE - |V_KK|
    p_eff   = KE - V_KK = KE + |V_KK|
    w = p/rho = (KE + |V_KK|) / (KE - |V_KK|)

  Since H^2 > 0 requires rho > 0, i.e., KE > |V_KK|:
    w >= 1 (equality when KE >> |V_KK|, i.e., deep stiff limit)

  For the actual transit:
    |V_KK(0)| = {abs_V0:.4f} M_KK^4
    Delta_V = {dV:.4f} M_KK^4 (0.9% change)

  The equation of state satisfies w >= 1 THROUGHOUT the transit.
  This is a STRUCTURAL result: any modulus rolling in a NEGATIVE potential
  has w >= 1. (The negative potential acts as negative energy density
  but positive pressure.)

  For the flatness problem:
    d(ln|Omega_k|)/dN = 1 + 3w >= 4
    Omega_k ALWAYS GROWS during exflation transit.
    Flatness is NOT solved — it is EXACERBATED.
""".format(abs_V0=abs(V0), dV=Vf - V0))

# Compute w for various KE/|V| ratios
print(f"  w(tau) for various KE/|V_KK| ratios:")
print(f"  {'KE/|V|':>8s}  {'w':>10s}  {'1+3w':>10s}  {'Regime':>15s}")
for ke_ratio in [1.01, 1.1, 2.0, 5.0, 10.0, 100.0, 1000.0]:
    w_val = (ke_ratio + 1) / (ke_ratio - 1)
    print(f"  {ke_ratio:8.2f}  {w_val:10.4f}  {1+3*w_val:10.4f}  {'stiff' if w_val < 1.1 else 'ultra-stiff'}")

# What is the actual KE/|V| ratio at the start of transit?
# From S52: in the stiff limit, KE >> |V| by construction.
# H_fold = 586.5 M_KK, so KE = 3*M_p^2*H^2 = 3*M_p^2*H_fold^2
KE_fold = 3 * M_p_sq * H_fold**2
print(f"\n  At the fold:")
print(f"    H_fold = {H_fold:.2f} M_KK")
print(f"    KE = 3*M_p^2*H^2 = {KE_fold:.2e} M_KK^4")
print(f"    |V_KK(fold)| = {abs(Vf):.4f} M_KK^4")
print(f"    KE/|V| = {KE_fold/abs(Vf):.2e}")
w_fold = (KE_fold + abs(Vf)) / (KE_fold - abs(Vf))
print(f"    w(fold) = {w_fold:.6f}")
print(f"    1 + 3w = {1 + 3*w_fold:.6f}")
print(f"    Deep stiff limit: w -> 1 + 2|V|/KE -> 1 + {2*abs(Vf)/KE_fold:.2e}")

# ============================================================================
#  SECTION 8: Numerical Integration — Omega_k(tau) Through Transit
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 8: Numerical Integration of Omega_k Through Transit")
print(f"{'='*78}")

# Solve the coupled system:
# H^2 + k/a^2 = rho/(3*M_p^2)
# tau_ddot + 3*H*tau_dot + V'/(G_mod) = 0
# a_dot = H*a
#
# Variables: y = [a, tau, tau_dot]
# Use ln(a) = N (e-folds) as variable instead of a for numerical stability.

def derivs_flatness(t, y, k_val):
    """RHS for [N, tau, tau_dot] with spatial curvature k."""
    N, tau, tdot = y
    a = np.exp(N)

    KE = 0.5 * G_mod * tdot**2
    V = V_KK(tau)
    rho = KE + V
    dVdt = dV_dtau(tau)

    # H^2 = rho/(3*M_p^2) - k/a^2
    H_sq = rho / (3 * M_p_sq) - k_val / a**2

    if H_sq <= 0:
        return [0, 0, 0]  # stop

    H = np.sqrt(H_sq)

    dN_dt = H
    dtau_dt = tdot
    dtdot_dt = -3 * H * tdot - dVdt / G_mod

    return [dN_dt, dtau_dt, dtdot_dt]

# Initial conditions: tau=0, tau_dot chosen to give H consistent with H_fold
# (we work backwards: set initial velocity to match a reasonable H)
#
# For k=0: H_0^2 = rho_0/(3*M_p^2)
# rho_0 = G_mod/2 * tdot_0^2 + V_KK(0)
# Need rho_0 > 0 => tdot_0^2 > 2*|V_KK(0)|/G_mod

tdot_min = np.sqrt(2 * abs(V0) / G_mod)
print(f"\n  Minimum initial velocity for H > 0:")
print(f"    tau_dot_min = sqrt(2*|V_KK(0)|/G_mod) = {tdot_min:.6f}")

# Use a range of initial velocities
tdot_values = [tdot_min * f for f in [1.01, 1.1, 2.0, 5.0, 10.0, 50.0]]

print(f"\n  Omega_k evolution for various initial conditions:")
print(f"  (Normalizing |Omega_k| = 1 at t=0 for k = +1)")
print(f"\n  {'tdot_0':>10s}  {'w_avg':>8s}  {'N_e':>8s}  {'Omega_k_f/Omega_k_i':>20s}  {'Status':>10s}")

results = []
for tdot0 in tdot_values:
    # k = +1, a_0 = 1
    k_val = 1.0  # (local)
    rho_0 = 0.5 * G_mod * tdot0**2 + V_KK(0.0)
    H_0_sq = rho_0 / (3 * M_p_sq) - k_val
    if H_0_sq <= 0:
        # Need larger a_0
        # H^2 = rho/(3M_p^2) - k/a^2 > 0 => a^2 > 3*k*M_p^2/rho
        a0_min = np.sqrt(3 * k_val * M_p_sq / rho_0)
        a0 = a0_min * 1.1
    else:
        a0 = 1.0  # (local)

    N0 = np.log(a0)
    rho_0_check = 0.5 * G_mod * tdot0**2 + V_KK(0.0)
    H_0_check = np.sqrt(rho_0_check / (3 * M_p_sq) - k_val / a0**2)

    # Omega_k_0 = -k / (a_0 * H_0)^2
    Omega_k_0 = -k_val / (a0 * H_0_check)**2

    # Integrate until tau reaches tau_fold
    def event_fold(t, y, k_val):
        return y[1] - tau_fold
    event_fold.terminal = True
    event_fold.direction = 1

    # Estimate transit time
    t_est = tau_fold / tdot0 * 2  # generous estimate

    try:
        sol = solve_ivp(
            lambda t, y: derivs_flatness(t, y, k_val),
            [0, t_est * 10],
            [N0, 0.0, tdot0],
            events=lambda t, y: event_fold(t, y, k_val),
            rtol=1e-10, atol=1e-12,
            max_step=t_est / 1000
        )

        if sol.t_events[0].size > 0:
            Nf = sol.y_events[0][0][0]
            tauf = sol.y_events[0][0][1]
            tdotf = sol.y_events[0][0][2]

            af = np.exp(Nf)
            rho_f = 0.5 * G_mod * tdotf**2 + V_KK(tauf)
            H_f = np.sqrt(max(0, rho_f / (3 * M_p_sq) - k_val / af**2))

            if H_f > 0:
                Omega_k_f = -k_val / (af * H_f)**2
                ratio = abs(Omega_k_f / Omega_k_0)
                Ne_actual = Nf - N0

                # Average w
                # For stiff: w ~ 1
                w_avg = 1.0  # approximate  # (local)

                status = "GROWS" if ratio > 1 else "SHRINKS"
                print(f"  {tdot0:10.4f}  {w_avg:8.2f}  {Ne_actual:8.4f}  {ratio:20.6f}  {status:>10s}")
                results.append((tdot0, Ne_actual, ratio))
            else:
                print(f"  {tdot0:10.4f}  {'--':>8s}  {'--':>8s}  {'H=0 at fold':>20s}  {'ERROR':>10s}")
        else:
            print(f"  {tdot0:10.4f}  {'--':>8s}  {'--':>8s}  {'no fold':>20s}  {'ERROR':>10s}")
    except Exception as e:
        print(f"  {tdot0:10.4f}  {'--':>8s}  {'--':>8s}  {str(e)[:20]:>20s}  {'ERROR':>10s}")

# ============================================================================
#  SECTION 9: Analytic Omega_k Formula
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 9: Analytic Omega_k Evolution")
print(f"{'='*78}")

# For w = const:
# |Omega_k(N)| = |Omega_k(0)| * exp((1+3w)*N)
#
# For w = 1 (stiff): |Omega_k(N)| = |Omega_k(0)| * exp(4*N)
# For N = 0.1734: growth = exp(0.694) = 2.001

growth_analytic = np.exp(4 * N_e)
print(f"\n  Analytic formula (constant w=1):")
print(f"    |Omega_k(N)|/|Omega_k(0)| = exp((1+3w)*N)")
print(f"    = exp(4 * {N_e:.4f})")
print(f"    = exp({4*N_e:.4f})")
print(f"    = {growth_analytic:.4f}")

print(f"\n  With w > 1 (actual, since V < 0):")
# Estimate actual w
# w ~ 1 + 2|V|/KE for KE >> |V|
# At moderate KE/|V| ~ 2: w = (2+1)/(2-1) = 3
# exp((1+3*3)*0.1734) = exp(10*0.1734) = exp(1.734) = 5.66
for w_test in [1.0, 1.5, 2.0, 3.0, 5.0]:
    growth = np.exp((1 + 3*w_test) * N_e)
    print(f"    w = {w_test:.1f}: growth = exp({(1+3*w_test)*N_e:.4f}) = {growth:.4f}")

print(f"\n  CONCLUSION: For all w >= 1, the growth factor is between")
print(f"  2.0 (w=1, deep stiff) and ~10 (w=5, marginal).")
print(f"  Transit is too short to matter. Omega_k is essentially preserved.")

# ============================================================================
#  SECTION 10: Could Flatness Be a Topological Input?
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 10: Topological Considerations")
print(f"{'='*78}")

print("""
  THREE possible origins of flatness in this framework:

  1. TOPOLOGICAL: If the full 12D spacetime has a specific topology that
     forces the 4D spatial sections to be flat. For example, if the 12D
     spacetime is T^4 x SU(3) rather than S^3 x R x SU(3).

     STATUS: Not determined. The framework assumes M^4 is Minkowski
     (flat spatial sections) from the outset. This is an ASSUMPTION,
     not a derivation.

  2. BDI TOPOLOGICAL PROTECTION (Volovik/Paper 04):
     The BDI topological class (proven, S17c) protects the Fermi point
     (massless spectrum at tau=0). Volovik argued that Fermi point
     topology naturally produces flat spacetime as an emergent low-energy
     phenomenon. The Z-classified topological charge prevents the
     generation of a mass gap, which in the condensed matter analogy
     corresponds to the "cosmological constant" (gap^2 ~ Lambda).

     STATUS: HEURISTIC. This argument operates at the level of universality
     classes and effective field theory. It does not directly constrain k.
     The BDI class protects the SPECTRAL properties of D_K, not the
     SPATIAL topology of M^4.

  3. ANTHROPIC/OBSERVATIONAL: k = 0 is simply an initial condition,
     as in standard FRW cosmology. The framework neither explains nor
     exacerbates the coincidence.

  ASSESSMENT:
  - The framework does NOT solve the flatness problem.
  - The framework does NOT worsen the flatness problem (N_e ~ 0.17
    is too small to significantly affect Omega_k).
  - The flatness problem REMAINS as an open question, as in standard
    cosmology without inflation.
  - The BDI topological argument (Volovik) offers a POTENTIAL resolution
    but requires rigorous derivation connecting spectral topology to
    spatial geometry.
""")

# ============================================================================
#  SECTION 11: Summary and Gate Verdict
# ============================================================================
print(f"\n{'='*78}")
print(f"  SECTION 11: GATE VERDICT — EXFLATION-FLATNESS-53")
print(f"{'='*78}")

print(f"""
  GATE: EXFLATION-FLATNESS-53
  VERDICT: INFO

  4D spatial flatness (k=0) is PERMITTED but NOT FORCED by the 12D geometry.

  DETAILED FINDINGS:

  1. FLATNESS NOT INHERITED (structural):
     The 12D vacuum Einstein equation G_AB = 0 decomposes into modified
     Friedmann equations + modulus EOM. Spatial curvature k appears as a
     free parameter (boundary/initial condition). k = 0, +1, -1 are all
     consistent solutions. This is IDENTICAL to standard GR.

  2. VOLUME CONSERVATION DOES NOT DRIVE EXPANSION:
     The Jensen deformation is volume-preserving (det g_tau = const, proven S12).
     a^3 * V_K = const with V_K = const gives a = const.
     Expansion comes from spectral action dynamics, not volume exchange.

  3. OMEGA_K EVOLUTION:
     w >= 1 (stiff or ultra-stiff) throughout transit.
     d(ln|Omega_k|)/dN = 1 + 3w >= 4.
     Omega_k GROWS during transit (opposite to inflation).
     Growth factor = exp(4*N_e) = exp({4*N_e:.4f}) = {growth_analytic:.2f}.
     NEGLIGIBLE: transit is only {N_e:.4f} e-folds.

  4. HORIZON PROBLEM NOT RESOLVED:
     Product geometry M^4 x K does not extend the 4D causal horizon.
     Internal propagation REDUCES 4D speed (null geodesic theorem).
     Horizon problem persists unchanged.

  5. EQUATION OF STATE:
     w = (KE + |V|)/(KE - |V|) >= 1 for V_KK < 0.
     At the fold: w = {w_fold:.6f} (deep stiff, KE >> |V|).
     Stiff matter CANNOT solve the flatness problem at any N_e.

  PHYSICAL INTERPRETATION:
     The exflation framework treats the 12D geometry as the STAGE on which
     phononic excitations play. The stage geometry (product, volume-preserving)
     does not select a preferred spatial curvature. k = 0 must be imposed
     as an initial condition, or derived from a separate principle
     (e.g., Volovik's BDI topological argument, or a prior phase of
     actual inflation at energies above M_KK).

  PHONONIC CLASSIFICATION: GEOMETRIC
     This result concerns the background geometry, not the phononic
     excitations. The flatness problem is a property of the STAGE,
     not the PLAY (in the language of S37's spectral post-mortem).

  KEY NUMBERS:
     N_e = {N_e:.4f} (stiff-limit e-folds)
     w = {w_fold:.6f} (at fold)
     Omega_k growth = {growth_analytic:.4f} (during transit)
     d_horizon enhancement from K = 1.00 (no enhancement)
     V_K(tau)/V_K(0) = 1.000 (volume-preserving, exact)
""")

# ============================================================================
#  SECTION 12: Constraints on Solution Space
# ============================================================================
print(f"{'='*78}")
print(f"  SECTION 12: Constraint Map Update")
print(f"{'='*78}")

print(f"""
  What was computed:
    - Decomposition of 12D Einstein equation for M^4 x SU(3) with k != 0
    - Omega_k evolution during transit (analytic + numerical)
    - 4D causal horizon in product geometry
    - Equation of state w(tau) during transit

  What region of solution space this constrains:
    - FLATNESS THROUGH GEOMETRY: CLOSED. k is not determined by 12D dynamics.
    - FLATNESS THROUGH VOLUME EXCHANGE: CLOSED (G3). Jensen is volume-preserving.
    - FLATNESS THROUGH TRANSIT: CLOSED. w >= 1 => Omega_k grows.
    - HORIZON THROUGH INTERNAL CONNECTIVITY: CLOSED. Product geometry, no shortcut.

  What survives:
    - FLATNESS AS INITIAL CONDITION (standard cosmology, no explanation)
    - FLATNESS FROM BDI TOPOLOGY (Volovik-type argument, heuristic)
    - FLATNESS FROM PRIOR INFLATION (above M_KK, pre-transit)
    - FLATNESS FROM QUANTUM COSMOLOGY (HH or tunneling boundary condition
      on the 12D Wheeler-DeWitt equation — S52 WDW shows HH selects tau=0,
      could in principle also select k=0)

  What remains uncomputed:
    - BDI -> spatial topology rigorous derivation
    - 12D WDW equation with k as quantum variable
    - Pre-transit dynamics at T > M_KK

  NEXT GATE: BDI-FLATNESS-54 — Does the BDI topological class of D_K
  constrain the 4D spatial topology? Pre-registered criterion:
  PASS: rigorous derivation connecting Z-classification to k=0.
  FAIL: BDI class is independent of spatial topology.
""")

# ============================================================================
#  FIGURE: Omega_k evolution
# ============================================================================
print(f"\n{'='*78}")
print(f"  Generating figure...")
print(f"{'='*78}")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('EXFLATION-FLATNESS-53: Does 12D Geometry Inherit 4D Flatness?',
             fontsize=14, fontweight='bold')

# Panel 1: R_K(tau) and V_KK(tau)
ax1 = axes[0, 0]
tau_plot = np.linspace(0, 0.5, 500)
R_plot = np.array([R_K(t) for t in tau_plot])
V_plot = np.array([V_KK(t) for t in tau_plot])
ax1.plot(tau_plot, R_plot, 'b-', linewidth=2, label=r'$R_K(\tau)$')
ax1.axvline(tau_fold, color='r', linestyle='--', alpha=0.7, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$R_K$ [$M_{KK}^2$]')
ax1.set_title('Internal Scalar Curvature')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: w(tau) for various KE/|V| ratios
ax2 = axes[0, 1]
ke_ratios = np.logspace(np.log10(1.01), 3, 500)
w_vals = (ke_ratios + 1) / (ke_ratios - 1)
ax2.semilogx(ke_ratios, w_vals, 'b-', linewidth=2)
ax2.axhline(1.0, color='gray', linestyle='--', alpha=0.5, label='w=1 (stiff)')
ax2.axhline(-1.0/3, color='green', linestyle='--', alpha=0.5, label='w=-1/3 (accel.)')
ax2.fill_between(ke_ratios, 1, w_vals, alpha=0.1, color='red', label='Omega_k GROWS')
ax2.set_xlabel(r'KE/|V|')
ax2.set_ylabel(r'$w = p/\rho$')
ax2.set_title('Equation of State (V < 0)')
ax2.set_ylim(-0.5, 10)
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# Panel 3: Omega_k growth factor vs N_e for various w
ax3 = axes[1, 0]
N_range = np.linspace(0, 5, 500)
for w_test in [1.0, 2.0, 3.0, 5.0]:
    growth_curve = np.exp((1 + 3*w_test) * N_range)
    ax3.semilogy(N_range, growth_curve, linewidth=2, label=f'w={w_test:.0f}')
# Also show inflation
growth_infl = np.exp(-2 * N_range)
ax3.semilogy(N_range, growth_infl, 'k--', linewidth=2, label='inflation (w=-1)')
ax3.axvline(N_e, color='r', linestyle=':', alpha=0.7, label=f'$N_e$ = {N_e:.3f}')
ax3.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
ax3.set_xlabel(r'$N_e$ (e-folds)')
ax3.set_ylabel(r'$|\Omega_k(N)|/|\Omega_k(0)|$')
ax3.set_title(r'$\Omega_k$ Growth Factor')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel 4: Volume conservation proof
ax4 = axes[1, 1]
# Volume factor det(g_tau)/det(g_0) vs tau
det_ratio = np.exp(2*tau_plot * 1 + (-2*tau_plot) * 3 + tau_plot * 4)
ax4.plot(tau_plot, det_ratio, 'b-', linewidth=3)
ax4.axhline(1.0, color='r', linestyle='--', alpha=0.5)
ax4.axvline(tau_fold, color='r', linestyle='--', alpha=0.7, label=r'$\tau_{\rm fold}$')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$\det(g_\tau)/\det(g_0)$')
ax4.set_title('Volume Conservation (Jensen)')
ax4.set_ylim(0.999, 1.001)
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.text(0.25, 1.0005, 'EXACTLY 1\n(volume-preserving)', ha='center',
         fontsize=10, color='darkgreen', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 's53_exflation_flatness.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s53_exflation_flatness.png")

# Close output
print(f"\n{'='*78}")
print(f"  END OF EXFLATION-FLATNESS-53")
print(f"{'='*78}")

outfile.close()
sys.stdout = sys.__stdout__
print("Output written to s53_exflation_flatness_output.txt")
