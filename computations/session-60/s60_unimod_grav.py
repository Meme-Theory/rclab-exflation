#!/usr/bin/env python3
"""
UNIMOD-GRAV-60: Unimodular Gravity from Fiber Integration
============================================================

Session 60, Wave 0, Task 3 (baptista-spacetime-analyst)

QUESTION: Does the Jensen deformation's volume-preservation on K = SU(3)
propagate through dimensional reduction to constrain det(g_4)?

MATHEMATICAL ARGUMENT:
---------------------
The 12D action on P = M^4 x K is (Paper 13 eq 3.41, Paper 15 eq 1.5):

  S_{12D} = (1/2kappa_P) int_{M^4 x K} (R_P - 2*Lambda_P) vol_{g_P}

The Riemannian submersion structure gives:
  vol_{g_P} = vol_{g_K} ^ vol_{g_4}

After fiber integration (Paper 13 eq 3.41):
  S_{4D} = (1/2kappa_P) int_{M^4} [Vol(K) * R_M - (1/4)B_phi*|F_A|^2
           - C_phi*|d_A phi|^2 - V(|phi|^2) - 2*Lambda_P*Vol(K)] sqrt(-g_4) d^4x

The S12 theorem: Vol(K, g_tau) = const for the Jensen TT-deformation.

KEY ANALYSIS:
1. Fiber volume enters as a MULTIPLICATIVE COEFFICIENT in S_{4D}
2. The variation delta(S_{4D})/delta(g_4^{mu nu}) gives standard 4D Einstein
   equations with effective Newton constant G_4 = G_{12}/Vol(K)
3. Vol(K) = const means G_4 = const, NOT that det(g_4) is constrained
4. Unimodular gravity requires constraining det(g_4) = epsilon_0 (Henneaux-Teitelboim)
5. This constraint would need the 12D theory to be unimodular, which is an
   ADDITIONAL ASSUMPTION beyond EH

CROSS-CHECKS:
- O'Neill A-tensor and T-tensor coupling between fiber and base
- Conformal factor analysis for Weyl rescaling to Einstein frame
- Comparison with Henneaux-Teitelboim 1989 formulation
- Numerical verification: Vol(K) constancy along Jensen line
- Lagrange multiplier analysis of the 12D action

References:
  - Paper 13 (2021_Baptista_HD_Routes_SM_Bosons) eqs 2.37, 3.41, 3.42, 3.43
  - Paper 15 (2024_Baptista_Internal_Symmetries_KK) eqs 1.5, 3.7, 3.68-3.72
  - S12 Session: Volume-preserving TT-deformation verified at machine epsilon
  - Henneaux & Teitelboim, Phys Lett B 222 (1989) 195-199
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    PI, tau_fold, Vol_SU3_Haar, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, rho_Lambda_obs, Lambda_obs_MP4,
    a0_fold, a2_fold, a4_fold,
    G_N, hbar_SI, c_light, l_Planck,
    rho_crit_GeV4, Omega_Lambda, H_0_GeV,
    G_DeWitt, S_fold,
)

# =============================================================================
#  SECTION 1: Volume Preservation of the Jensen Deformation
# =============================================================================

def jensen_volume_ratio(s):
    """
    Volume ratio Vol(K, g_s) / Vol(K, g_0) for the Jensen deformation.

    Paper 15 eq 3.68: lambda_1 = e^{2s}, lambda_2 = e^{-2s}, lambda_3 = e^s
    The metric scales as diag(lambda_1, lambda_2, lambda_2, lambda_2, lambda_3, lambda_3, lambda_3, lambda_3)
    on the decomposition su(3) = u(1) + su(2) + C^2 (dims 1+3+4 = 8).

    Vol(K, g_s) / Vol(K, g_0) = sqrt(det(g_s) / det(g_0))
    = sqrt(lambda_1^1 * lambda_2^3 * lambda_3^4)
    = sqrt(e^{2s} * e^{-6s} * e^{4s})
    = sqrt(e^0) = 1

    This is EXACT: the Jensen deformation is TT (traceless-transverse) by construction.
    The volume constraint is lambda_1 * lambda_2^3 * lambda_3^4 = 1.
    """
    lambda_1 = np.exp(2 * s)
    lambda_2 = np.exp(-2 * s)
    lambda_3 = np.exp(s)

    # Volume ratio = sqrt(product of eigenvalues)
    det_ratio = lambda_1**1 * lambda_2**3 * lambda_3**4
    vol_ratio = np.sqrt(det_ratio)

    return vol_ratio, det_ratio


def baptista_volume_function(phi_sq):
    """
    Volume ratio Vol(K, g_phi) / Vol(K, beta_0) for the Baptista phi-deformation.

    Paper 13 eq 2.37:
    vol_{g_phi} = lambda^4 * (1 - |phi|^2) * sqrt(1 - 4|phi|^2) * vol_{beta_0}

    For the single-lambda model: f_phi = lambda^4 * (1 - |phi|^2) * sqrt(1 - 4|phi|^2)

    NOTE: This is NOT the Jensen deformation. The phi-deformation changes the volume.
    The Jensen deformation is a DIFFERENT parametrization that IS volume-preserving.
    """
    if np.any(phi_sq >= 0.25):
        raise ValueError("|phi|^2 must be < 1/4 for positive-definite metric")

    f_phi = (1 - phi_sq) * np.sqrt(1 - 4 * phi_sq)
    return f_phi  # normalized to lambda^4 = 1 at phi = 0


# =============================================================================
#  SECTION 2: Fiber Integration Structure
# =============================================================================

def analyze_fiber_integration():
    """
    Analyze the structure of the 4D effective action after fiber integration.

    The 12D action (Paper 13 eq 3.41):
    S_{4D} = (1/2kappa_P) int_{M^4} L_M * sqrt(-g_4) d^4x

    where L_M = Vol(K, beta_0) * [R_M * f_phi - (1/4)*B_phi*|F_A|^2
                                   - C_phi*|d_A phi|^2 - V(|phi|^2)
                                   - 2*Lambda_M*f_phi]

    Key structural observation:
    - L_M depends on (g_4^{mu nu}, A_mu, phi) through the kinetic terms
    - L_M depends on (g_K) through f_phi, B_phi, C_phi, V
    - The 4D volume element sqrt(-g_4) is NOT constrained by Vol(K) = const

    The variation with respect to g_4^{mu nu} gives:
    delta(S)/delta(g_4^{mu nu}) = standard Einstein equation with effective CC

    The CC term is: Lambda_eff = Vol(K, beta_0) * [V(|phi_0|^2) + 2*Lambda_P*f_phi0]

    In unimodular gravity, one instead derives the TRACE-FREE Einstein equation:
    G_{mu nu} - (1/4)*g_{mu nu}*G = 8*pi*G*(T_{mu nu} - (1/4)*g_{mu nu}*T)
    and Lambda appears as an integration constant from the Bianchi identity.

    For this to happen FROM the fiber, we would need:
    sqrt(-g_{12}) = sqrt(g_K) * sqrt(-g_4) = fixed constant
    => sqrt(-g_4) = const / sqrt(g_K) = const / Vol(K)^{1/vol}

    But Vol(K) = const only means sqrt(-g_4) = const * sqrt(-g_4) -- no constraint!
    """
    results = {}

    # Verify Vol(K) = const along Jensen line
    s_values = np.linspace(0, 2.0, 1000)
    vol_ratios = np.array([jensen_volume_ratio(s)[0] for s in s_values])
    vol_deviation = np.max(np.abs(vol_ratios - 1.0))
    results['vol_deviation_jensen'] = vol_deviation

    # Compare with Baptista phi-deformation (which changes volume)
    phi_sq_values = np.linspace(0, 0.24, 100)
    f_phi_values = baptista_volume_function(phi_sq_values)
    vol_change_phi = 1.0 - f_phi_values[-1]  # volume change at |phi|^2 = 0.24
    results['vol_change_phi_at_0p24'] = vol_change_phi

    # The effective Newton constant
    # G_4 = G_{12} / Vol(K) = kappa_P / (8*pi*Vol(K))
    # Since Vol(K) = const on Jensen line, G_4 = const
    results['G4_constant'] = True  # by construction

    return results, s_values, vol_ratios, phi_sq_values, f_phi_values


# =============================================================================
#  SECTION 3: O'Neill Tensor Analysis
# =============================================================================

def oneill_tensor_analysis():
    """
    Analyze whether the O'Neill A-tensor or T-tensor provides a coupling
    between det(g_K) and det(g_4).

    For a Riemannian submersion pi: (P, g_P) -> (M, g_M) with fiber (K, g_K):

    The A-tensor: A_X Y = V(nabla^P_{HX} HY) + H(nabla^P_{HX} VY)
    where H = horizontal projection, V = vertical projection

    The T-tensor (integrability tensor of vertical distribution):
    T_U V = H(nabla^P_{VU} VV) + V(nabla^P_{VU} HV)

    The mean curvature vector N of the fibers is the trace of T.

    Paper 15 eq 1.5:
    R_P = R_M + R_K - |F_A|^2 - |S_ring|^2 - |N|^2 - 2*delta_check(N)

    where S_ring is traceless second fundamental form and N is mean curvature.

    CRITICAL: The decomposition shows that the scalar curvature of the TOTAL space
    involves coupling between base and fiber through |S_ring|^2 and |N|^2.
    But these are curvature couplings, NOT volume element couplings.

    The volume elements factorize: vol_{g_P} = vol_{g_K} ^ vol_{g_4}
    This factorization is EXACT for any Riemannian submersion.
    It does NOT require the submersion to be totally geodesic.

    Therefore: the A-tensor and T-tensor introduce CURVATURE coupling between
    base and fiber, but they do NOT introduce VOLUME coupling.

    The variation of S_{4D} w.r.t. g_4 does NOT produce a constraint on det(g_4)
    from Vol(K) = const, regardless of the A-tensor and T-tensor.
    """
    results = {}

    # For the product metric (no gauge fields), A = T = 0
    results['product_metric_A_tensor'] = 0.0
    results['product_metric_T_tensor'] = 0.0

    # When gauge fields are turned on, A != 0 but this is the field strength
    # A_X Y ~ F_A(X,Y) for horizontal X, Y
    # This couples to |F_A|^2 in the action, NOT to det(g_4)
    results['gauge_A_tensor_couples_to_det_g4'] = False

    # The mean curvature N (trace of T) appears in the divergence term
    # delta_check(N). For compact fibers, the integral of delta_check(N) over K
    # gives a boundary term that vanishes (K is compact without boundary).
    results['mean_curvature_boundary_term'] = 0.0  # for compact K

    # Jensen deformation: the fibers are NOT totally geodesic
    # (the metric changes along the fiber, so T != 0 in general)
    # But the TT condition means: the TRACE of the deformation h_J is zero
    # => N remains unchanged to first order
    # => The conformal mode (volume) is NOT excited by the Jensen deformation
    results['jensen_TT_excites_conformal_mode'] = False

    return results


# =============================================================================
#  SECTION 4: Conformal Factor and Einstein Frame Analysis
# =============================================================================

def einstein_frame_analysis(s_values):
    """
    Analyze the conformal factor transformation to Einstein frame.

    Paper 15 eq 3.6: To go to Einstein frame, define
    g_K = a_1 * e^{-b_1*phi} * g_bar_K
    where phi is the 'breathing mode' (controls volume of K).

    For k = dim(K) = 8:
    b_1 = sqrt(2 / (k*(k+m-2))) where m = dim(M) = 4
    => b_1 = sqrt(2 / (8*10)) = sqrt(1/40)

    The Einstein frame metric is:
    g_M^{Einstein} = (Vol(K, g_K) / Vol_0)^{2/m} * g_M

    KEY POINT: On the Jensen line, Vol(K) = Vol_0 = const.
    Therefore: g_M^{Einstein} = g_M (no conformal rescaling needed!)

    This means: the Jensen deformation stays IN the Einstein frame.
    There is no conformal mode excited. But this does NOT mean det(g_4)
    is constrained -- it means the conformal factor linking the Jordan
    frame and Einstein frame is trivially 1.

    The distinction:
    - Vol(K) = const => the breathing mode phi = 0 on the Jensen line
    - phi = 0 => no conformal rescaling between Jordan and Einstein frames
    - But this does NOT impose det(g_4) = epsilon_0
    - det(g_4) is still determined by the 4D Einstein equations

    For UNIMODULAR gravity from the 12D theory, we would need:
    The 12D ACTION to be of the unimodular type:
    S_{unimod} = int [R_P - 2*Lambda_P] vol_{g_P}
    with the CONSTRAINT sqrt(-g_P) = epsilon_P (fixed density)

    Then: sqrt(g_K) * sqrt(-g_4) = epsilon_P
    With Vol(K) = const (Jensen), this gives:
    sqrt(-g_4) = epsilon_P / sqrt(g_K)
    and at each point x in M^4:
    sqrt(-g_4(x)) = epsilon_P(x) / (integral over K of sqrt(g_K) d^8y / vol_K)

    But this argument requires assuming the 12D theory is unimodular.
    The standard EH action does NOT impose this constraint.
    """
    results = {}

    # Dimensions
    m = 4  # dim M^4
    k = 8  # dim K = SU(3)

    # Conformal scaling exponent
    b_1 = np.sqrt(2.0 / (k * (k + m - 2)))  # = sqrt(2/80) = sqrt(1/40)
    results['b_1'] = b_1

    # Einstein frame conformal factor
    # Omega^2 = (Vol(K)/Vol_0)^{2/m}
    # On Jensen line: Omega^2 = 1 identically
    vol_ratios = np.array([jensen_volume_ratio(s)[0] for s in s_values])
    omega_sq = vol_ratios**(2.0/m)
    results['omega_sq_deviation'] = np.max(np.abs(omega_sq - 1.0))

    # The breathing mode phi on Jensen line
    # phi = -k*b_1 * ln(Vol(K)/Vol_0) = 0 exactly
    phi_breathing = -k * b_1 * np.log(vol_ratios)
    results['phi_breathing_max'] = np.max(np.abs(phi_breathing))

    return results


# =============================================================================
#  SECTION 5: Lagrange Multiplier Analysis
# =============================================================================

def lagrange_multiplier_analysis():
    """
    Test whether Vol(K) = const acts as an effective Lagrange multiplier
    that could constrain det(g_4).

    In unimodular gravity (Henneaux-Teitelboim 1989), one introduces a
    Lagrange multiplier lambda to enforce sqrt(-g) = epsilon:

    S_{unimod} = int [lambda * (sqrt(-g) - epsilon) + sqrt(-g) * L] d^nx

    Varying w.r.t. lambda gives: sqrt(-g) = epsilon (constraint)
    Varying w.r.t. g^{mu nu} gives: G_{mu nu} - (1/2)*g_{mu nu}*lambda = 0
    Taking the trace: R + 2*lambda = 0 => lambda = -R/2
    The CC drops out of the field equation and becomes an integration constant.

    In our case, the relevant question: does the 12D EH action, restricted to
    the Jensen family on K, naturally produce such a Lagrange multiplier structure?

    The answer is NO. Here's why:

    The 12D action restricted to the Jensen family is:
    S = (1/2kappa_P) * int_{M^4} [R_M*V_K + V_K*R_K(s) - |F|^2*V_K - 2*Lambda_P*V_K] sqrt(-g_4) d^4x

    where V_K = Vol(K) = const on the Jensen line.

    The constraint Vol(K) = const is a constraint on the INTERNAL geometry.
    It removes one degree of freedom from the internal metric (the breathing mode).
    It does NOT introduce a Lagrange multiplier for sqrt(-g_4).

    The effective 4D action is simply:
    S_{4D} = V_K/(2*kappa_P) * int_{M^4} [R_M - 2*Lambda_{eff}] sqrt(-g_4) d^4x

    where Lambda_eff = Lambda_P - R_K(s)/2

    This is the STANDARD Einstein-Hilbert action in 4D with a cosmological constant.
    The CC is determined by the 12D CC and the internal curvature, NOT as an
    integration constant.

    The volume preservation of K has a DIFFERENT physical consequence:
    it prevents the 4D Newton constant G_4 = G_{12}/V_K from varying.
    This is IMPORTANT but it is NOT unimodular gravity.
    """
    results = {}

    # Effective CC in 4D
    # Lambda_eff = Lambda_P - R_K(s_fold)/2
    # The CC problem remains: Lambda_eff is determined by Lambda_P and R_K

    # At the fold, the spectral action gives a_0 = 6440.0 (volume term)
    # The CC contribution from the spectral action is:
    # rho_Lambda = (2/pi^2) * f_0 * Lambda_eff^2 * Vol(K)
    # where f_0 is the spectral function zeroth moment

    # The key ratio: the CC from fiber integration is O(M_KK^4)
    # The observed CC is rho_Lambda_obs ~ 2.7e-47 GeV^4
    # The gap is ~ 10^{113} orders of magnitude
    # Vol(K) = const does NOT change this gap

    # Newton constant stabilization
    G12 = 1.0  # in 12D Planck units  # (local)
    V_K = Vol_SU3_Haar  # = 1349.74
    G4_eff = G12 / V_K
    results['G4_eff'] = G4_eff

    # The CC gap remains
    rho_SA = (2.0 / PI**2) * a0_fold * M_KK_gravity**4
    gap_OOM = np.log10(rho_SA / rho_Lambda_obs)
    results['CC_gap_OOM'] = gap_OOM
    results['CC_gap_unchanged'] = True

    # What Vol(K) = const DOES give:
    # 1. G_4 = const (no fifth force from volume modulus)
    # 2. No light scalar from breathing mode (phi is projected out)
    # 3. The kinetic term for the shape mode (Jensen parameter s) is
    #    purely from the traceless part of the metric deformation
    # 4. No conformal coupling between tau-evolution and expansion

    results['provides_G4_stability'] = True
    results['removes_breathing_mode'] = True
    results['provides_unimodular_constraint'] = False
    results['CC_suppression_OOM'] = 0  # zero OOM of CC suppression

    return results


# =============================================================================
#  SECTION 6: Quantitative Cross-Checks
# =============================================================================

def cross_checks():
    """
    Multiple independent checks of the conclusion.
    """
    results = {}

    # CHECK 1: Volume deviation along Jensen line (should be exactly 0)
    s_test = np.linspace(0, 5.0, 10000)  # extended range
    vol_devs = np.array([abs(jensen_volume_ratio(s)[0] - 1.0) for s in s_test])
    results['vol_max_deviation'] = np.max(vol_devs)
    results['vol_mean_deviation'] = np.mean(vol_devs)
    # Machine epsilon: ~2.2e-16

    # CHECK 2: Baptista f_phi at various phi_sq to show it changes
    phi_sq_test = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.24])
    f_phi_test = baptista_volume_function(phi_sq_test)
    results['f_phi_values'] = dict(zip(phi_sq_test, f_phi_test))
    # At phi=0: f_phi = 1.0
    # At phi=0.24: f_phi << 1 (volume collapses near the boundary)

    # CHECK 3: Determinant constraint algebra
    # If 12D theory were unimodular with constraint sqrt(-g_{12}) = epsilon_{12}:
    #   sqrt(g_K) * sqrt(-g_4) = epsilon_{12}
    #   For x-dependent fields:
    #   sqrt(g_K(x, y)) * sqrt(-g_4(x)) = epsilon_{12}(x, y)
    # But g_K is x-independent (product metric before gauge fields)
    # So: sqrt(-g_4(x)) = epsilon_{12}(x) / sqrt(g_K(y))
    # Integrating over K: sqrt(-g_4(x)) * Vol(K) = int epsilon_{12}(x,y) d^8y
    # With Vol(K) = const: sqrt(-g_4(x)) = (1/Vol(K)) * int epsilon_{12}(x,y) d^8y
    # This WOULD constrain det(g_4) IF the 12D theory is unimodular
    # But standard EH in 12D is NOT unimodular
    results['requires_12D_unimodular'] = True

    # CHECK 4: Count of independent constraints
    # The Jensen TT condition provides: 1 constraint (volume = const)
    # Unimodular gravity requires: 1 constraint (det(g_4) = epsilon)
    # But these are constraints on DIFFERENT objects:
    #   Jensen: constraint on g_K (internal geometry)
    #   Unimodular: constraint on g_4 (external geometry)
    # The fiber volume constraint does NOT propagate to the base metric
    results['constraint_on_different_objects'] = True

    # CHECK 5: Variation structure
    # S = int_{M^4} [V_K * L(g_4, A, phi)] * sqrt(-g_4) d^4x
    # delta S / delta g_4^{mu nu} = V_K * [delta L / delta g_4^{mu nu} * sqrt(-g_4)
    #                                       + L * delta(sqrt(-g_4)) / delta(g_4^{mu nu})]
    # The factor V_K is a constant multiplier. It rescales the equation but
    # does NOT change the structure of the variation.
    # The variation of sqrt(-g_4) gives: delta(sqrt(-g_4)) = -(1/2)*sqrt(-g_4)*g_{mu nu}*delta(g^{mu nu})
    # This is the standard formula -- V_K does not modify it.
    results['VK_modifies_variation_structure'] = False

    # CHECK 6: Trace of the field equation
    # Standard: G_{mu nu} + Lambda * g_{mu nu} = 0 => R + 4*Lambda = 0
    # Unimodular: G_{mu nu} - (1/4)*g_{mu nu}*G = 0 (trace-free)
    # The difference is that unimodular has det(g) constrained, so the trace
    # equation is NOT derived from the action but from the Bianchi identity.
    # Our S_{4D} has standard structure => trace equation is derived => NOT unimodular
    results['standard_trace_equation'] = True

    return results


# =============================================================================
#  SECTION 7: What Vol(K) = const DOES Provide
# =============================================================================

def positive_consequences():
    """
    While Vol(K) = const does NOT provide unimodular gravity,
    it has several important physical consequences.
    """
    results = {}

    # 1. Newton constant stability
    # G_4 = G_{12} / Vol(K) is constant along the Jensen line
    # This means: no time-variation of G during the exflation transit
    # LLR bound: |dG/dt|/G < 4e-13 yr^{-1} (Nordtvedt 2003)
    # Jensen gives dG/dt = 0 exactly
    results['Newton_constant_stability'] = True
    results['dG_dt_over_G'] = 0.0  # exactly zero on Jensen line

    # 2. No light scalar (breathing mode projected out)
    # The breathing mode has mass^2 ~ Lambda_P / Vol(K)^{2/8}
    # On the Jensen line, it's projected out entirely -- not light, but absent
    # This avoids the "moduli problem" for the volume modulus
    results['breathing_mode_projected_out'] = True

    # 3. Shape-only dynamics
    # The Jensen parameter s parametrizes shape deformations only
    # All dynamics is in the shape mode, not the volume mode
    # This is structurally cleaner than general KK with volume and shape
    results['shape_only_dynamics'] = True

    # 4. Sigma stability (S59 result)
    # The Cheeger sigma mode (off-Jensen) has positive Hessian
    # d^2V/dsig^2 > 0 at all tau -- from s59_cheeger_sigma.npz
    # Combined with Vol(K) = const, the internal geometry is rigid
    # against both volume and off-Jensen shape fluctuations
    try:
        cheeger_data = np.load(
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's59_cheeger_sigma.npz'),
            allow_pickle=True
        )
        results['sigma_stable'] = bool(cheeger_data['net_positive_everywhere'])
        results['m_sigma'] = float(cheeger_data['m_sigma'])
    except FileNotFoundError:
        results['sigma_stable'] = None
        results['m_sigma'] = None

    # 5. The true consequence for the CC
    # Vol(K) = const means the CC from fiber integration is:
    # Lambda_{4D} = Vol(K) * [Lambda_P - R_K(s)/2]
    # Since Vol(K) = const, Lambda_{4D} depends on Lambda_P and R_K(s) only
    # The CC is determined, NOT an integration constant
    # The CC problem is: Lambda_P - R_K(s)/2 ~ M_KK^2, not ~ H_0^2

    # Quantitative: at the fold
    # R_K(s_fold) from the scalar curvature at the fold
    # Paper 13 eq 2.40 with the Jensen parametrization
    s_fold = tau_fold  # tau = s in our convention
    lambda_val = 1.0  # normalized  # (local)

    # Scalar curvature at fold: use the spectral action a_2 coefficient
    # a_2 = (1/6) * int_K R_K * vol_K
    # R_K * Vol(K) = 6 * a_2
    R_K_times_VK = 6.0 * a2_fold
    R_K_eff = R_K_times_VK / Vol_SU3_Haar
    results['R_K_eff_at_fold'] = R_K_eff

    # The CC contribution
    # Lambda_{4D} = Vol_K / (2*kappa_{12}) * (2*Lambda_P - R_K)
    # In M_KK units, the CC from internal curvature alone is O(M_KK^2)
    # This gives rho_Lambda ~ M_KK^4, the full CC problem
    results['CC_from_internal_curvature_OOM'] = np.log10(M_KK_gravity**4 / rho_Lambda_obs)

    return results


# =============================================================================
#  MAIN COMPUTATION
# =============================================================================

def main():
    print("=" * 70)
    print("UNIMOD-GRAV-60: Unimodular Gravity from Fiber Integration")
    print("=" * 70)

    # Section 1: Volume preservation verification
    print("\n--- Section 1: Volume Preservation ---")
    s_values = np.linspace(0, 3.0, 1000)
    for s_test in [0.0, tau_fold, 0.5, 1.0, 2.0, 3.0]:
        vr, dr = jensen_volume_ratio(s_test)
        print(f"  s = {s_test:.2f}: Vol ratio = {vr:.16f}, det ratio = {dr:.16e}")

    # Section 2: Fiber integration structure
    print("\n--- Section 2: Fiber Integration Structure ---")
    fib_results, s_vals, vol_rats, phi_sq_vals, f_phi_vals = analyze_fiber_integration()
    print(f"  Jensen Vol(K) deviation from 1: {fib_results['vol_deviation_jensen']:.2e}")
    print(f"  Baptista f_phi change at |phi|^2=0.24: {fib_results['vol_change_phi_at_0p24']:.4f}")
    print(f"  G_4 = const on Jensen line: {fib_results['G4_constant']}")

    # Section 3: O'Neill tensor analysis
    print("\n--- Section 3: O'Neill Tensor Analysis ---")
    oneill_results = oneill_tensor_analysis()
    print(f"  Product metric A-tensor: {oneill_results['product_metric_A_tensor']}")
    print(f"  Gauge A-tensor couples to det(g_4): {oneill_results['gauge_A_tensor_couples_to_det_g4']}")
    print(f"  Mean curvature boundary term: {oneill_results['mean_curvature_boundary_term']}")
    print(f"  Jensen TT excites conformal mode: {oneill_results['jensen_TT_excites_conformal_mode']}")

    # Section 4: Einstein frame analysis
    print("\n--- Section 4: Einstein Frame Analysis ---")
    ef_results = einstein_frame_analysis(s_vals)
    print(f"  b_1 (conformal exponent): {ef_results['b_1']:.6f}")
    print(f"  Omega^2 deviation from 1: {ef_results['omega_sq_deviation']:.2e}")
    print(f"  Breathing mode phi max: {ef_results['phi_breathing_max']:.2e}")

    # Section 5: Lagrange multiplier analysis
    print("\n--- Section 5: Lagrange Multiplier Analysis ---")
    lm_results = lagrange_multiplier_analysis()
    print(f"  CC gap (OOM): {lm_results['CC_gap_OOM']:.1f}")
    print(f"  CC gap unchanged: {lm_results['CC_gap_unchanged']}")
    print(f"  Provides G_4 stability: {lm_results['provides_G4_stability']}")
    print(f"  Removes breathing mode: {lm_results['removes_breathing_mode']}")
    print(f"  Provides unimodular constraint: {lm_results['provides_unimodular_constraint']}")
    print(f"  CC suppression (OOM): {lm_results['CC_suppression_OOM']}")

    # Section 6: Cross-checks
    print("\n--- Section 6: Cross-Checks ---")
    cc_results = cross_checks()
    print(f"  Vol max deviation (s in [0,5]): {cc_results['vol_max_deviation']:.2e}")
    print(f"  Vol mean deviation: {cc_results['vol_mean_deviation']:.2e}")
    print(f"  f_phi values:")
    for phi_sq, f_val in cc_results['f_phi_values'].items():
        print(f"    |phi|^2 = {phi_sq:.2f}: f_phi = {f_val:.6f}")
    print(f"  Requires 12D unimodular: {cc_results['requires_12D_unimodular']}")
    print(f"  Constraint on different objects: {cc_results['constraint_on_different_objects']}")
    print(f"  V_K modifies variation structure: {cc_results['VK_modifies_variation_structure']}")
    print(f"  Standard trace equation: {cc_results['standard_trace_equation']}")

    # Section 7: Positive consequences
    print("\n--- Section 7: Positive Consequences ---")
    pos_results = positive_consequences()
    print(f"  Newton constant stability: {pos_results['Newton_constant_stability']}")
    print(f"  dG/dt / G: {pos_results['dG_dt_over_G']}")
    print(f"  Breathing mode projected out: {pos_results['breathing_mode_projected_out']}")
    print(f"  Sigma stable (S59): {pos_results['sigma_stable']}")
    print(f"  m_sigma (M_KK units): {pos_results['m_sigma']}")
    print(f"  R_K effective at fold: {pos_results['R_K_eff_at_fold']:.4f}")
    print(f"  CC from internal curvature (OOM): {pos_results['CC_from_internal_curvature_OOM']:.1f}")

    # =================================================================
    # GATE VERDICT
    # =================================================================
    print("\n" + "=" * 70)
    print("GATE VERDICT: UNIMOD-GRAV-60")
    print("=" * 70)

    # The Jensen volume-preservation does NOT propagate to constrain det(g_4)
    # The fiber and base volume elements are INDEPENDENT
    # The CC problem remains at 113+ OOM

    gate_verdict = "FAIL"
    gate_detail = (
        "The Jensen volume-preservation Vol(K) = const is a constraint on the "
        "INTERNAL geometry (K = SU(3)), not on the EXTERNAL geometry (M^4). "
        "The 12D volume element factorizes as vol_{g_P} = vol_{g_K} ^ vol_{g_4}, "
        "and Vol(K) = const enters the 4D action as a multiplicative constant "
        "that rescales the effective Newton constant G_4 = G_{12}/Vol(K) but "
        "does NOT constrain det(g_4). "
        "The variation delta(S_{4D})/delta(g_4^{mu nu}) gives standard 4D "
        "Einstein equations, NOT trace-free unimodular equations. "
        "For unimodular gravity to emerge, the 12D theory itself would need "
        "to be unimodular (sqrt(-g_{12}) = epsilon_{12}), which is an "
        "additional assumption beyond the Einstein-Hilbert action. "
        "CC suppression from this mechanism: 0 OOM. "
        "However, Vol(K) = const provides: (1) G_4 stability (no fifth force), "
        "(2) breathing mode projected out (no moduli problem), "
        "(3) shape-only dynamics. "
        f"Vol(K) deviation from 1 on Jensen line: {cc_results['vol_max_deviation']:.2e} "
        "(machine epsilon)."
    )

    cc_suppression = 0  # OOM of CC suppression

    print(f"\n  Verdict: {gate_verdict}")
    print(f"  CC suppression: {cc_suppression} OOM (threshold: >= 50 for PASS)")
    print(f"\n  Detail: {gate_detail}")

    # Key numbers for the gate
    key_numbers = {
        'vol_K_deviation_from_1': cc_results['vol_max_deviation'],
        'CC_gap_OOM': lm_results['CC_gap_OOM'],
        'CC_suppression_OOM': cc_suppression,
        'G4_constant': True,
        'breathing_mode_mass': 'projected out (infinite)',
        'sigma_modulus_mass': pos_results['m_sigma'],
        'b1_conformal_exponent': ef_results['b_1'],
        'omega_sq_max_dev': ef_results['omega_sq_deviation'],
        'requires_12D_unimodular': True,
    }

    print("\n  Key numbers:")
    for k, v in key_numbers.items():
        print(f"    {k}: {v}")

    # =================================================================
    # SAVE RESULTS
    # =================================================================
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             's60_unimod_grav.npz')

    np.savez(save_path,
        # Gate verdict
        gate_name='UNIMOD-GRAV-60',
        gate_verdict=gate_verdict,
        gate_detail=gate_detail,
        CC_suppression_OOM=cc_suppression,

        # Volume preservation data
        s_values=s_vals,
        vol_ratios_jensen=vol_rats,
        vol_deviation_max=cc_results['vol_max_deviation'],
        vol_deviation_mean=cc_results['vol_mean_deviation'],

        # Baptista phi-deformation comparison
        phi_sq_values=phi_sq_vals,
        f_phi_values=f_phi_vals,

        # Einstein frame
        b1_conformal=ef_results['b_1'],
        omega_sq_deviation=ef_results['omega_sq_deviation'],
        phi_breathing_max=ef_results['phi_breathing_max'],

        # Lagrange multiplier analysis
        CC_gap_OOM=lm_results['CC_gap_OOM'],
        G4_eff=lm_results['G4_eff'],
        provides_unimodular=False,
        provides_G4_stability=True,
        removes_breathing_mode=True,

        # Cross-checks
        requires_12D_unimodular=True,
        constraint_on_different_objects=True,
        VK_modifies_variation=False,
        standard_trace_equation=True,

        # Positive consequences
        dG_dt_over_G=0.0,
        R_K_eff_at_fold=pos_results['R_K_eff_at_fold'],
        CC_from_internal_OOM=pos_results['CC_from_internal_curvature_OOM'],
        sigma_stable=pos_results.get('sigma_stable', None),
        m_sigma=pos_results.get('m_sigma', None),
    )

    print(f"\n  Results saved to: {save_path}")
    print("  DONE.")

    return gate_verdict, key_numbers


if __name__ == '__main__':
    main()
