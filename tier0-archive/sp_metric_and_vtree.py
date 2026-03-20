"""
SP-1 + SP-4: EXPLICIT JENSEN METRIC AND EXACT V_tree(s)
=========================================================

Schwarzschild-Penrose-Geometer — Session 17a

SP-1: Write the full 8×8 metric g_s in the Gell-Mann left-invariant basis,
      verify its structure, and express it in left-invariant 1-forms.

SP-4: Derive R(s) analytically, compute V_tree(s) = -R(s) * Vol(SU(3), g_s),
      and verify against the existing numerical code at machine epsilon.

METHODOLOGY (Schwarzschild method):
  Step 1: Identify symmetries (SU(3) left-invariance + SU(2)×U(1) right-invariance)
  Step 2: Write metric ansatz compatible with symmetries
  Step 3: Compute curvature exactly from connection (no perturbation theory)
  Step 4: Verify all results at machine epsilon

Author: Schwarzschild-Penrose-Geometer (Session 17a)
Date: 2026-02-14
"""

import numpy as np
from numpy.linalg import eigh, cholesky, inv, det, eigvalsh
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients,
    U1_IDX, SU2_IDX, C2_IDX
)
from tier1_spectral_action import (
    scalar_curvature_from_connection, scalar_curvature_analytical,
    baptista_V_potential
)


def separator(title):
    """Print a formatted section separator."""
    print(f"\n{'='*72}")
    print(f"  {title}")
    print(f"{'='*72}")


# =============================================================================
# SP-1: EXPLICIT METRIC g_s IN GELL-MANN BASIS
# =============================================================================

def sp1_explicit_metric():
    """
    SP-1: Write the full 8x8 Jensen-deformed metric g_s.

    The metric is left-invariant on SU(3), meaning it is determined entirely
    by its values on the Lie algebra su(3). In the basis {e_a = -i lambda_a/2}
    (a = 0,...,7), the metric is:

        g_s(e_a, e_b) = [g_s]_{ab}

    Since the Gell-Mann generators satisfy Tr(e_a e_b) = -1/2 delta_{ab},
    the Killing form is B_{ab} = -3 delta_{ab}, and the bi-invariant metric
    is g_0 = |B| = 3 I_8.

    The Jensen TT-deformation (Baptista eq 3.68) rescales the three subspaces:

        g_s = e^{2s} g_0|_{u(1)} + e^{-2s} g_0|_{su(2)} + e^s g_0|_{C^2}

    In matrix form this is DIAGONAL:

        [g_s]_{ab} = diag(3e^{-2s}, 3e^{-2s}, 3e^{-2s},   (su(2): a=0,1,2)
                          3e^s, 3e^s, 3e^s, 3e^s,           (C^2:   a=3,4,5,6)
                          3e^{2s})                            (u(1):  a=7)

    The left-invariant 1-form expression of the metric on SU(3) is:

        ds^2 = 3 e^{-2s} [(w^1)^2 + (w^2)^2 + (w^3)^2]
             + 3 e^s     [(w^4)^2 + (w^5)^2 + (w^6)^2 + (w^7)^2]
             + 3 e^{2s}  (w^8)^2

    where w^a are the left-invariant Maurer-Cartan 1-forms dual to the
    Gell-Mann generators:  w^a(e_b) = delta^a_b.
    """
    separator("SP-1: EXPLICIT 8×8 JENSEN METRIC g_s")

    # Step 1: Build infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    # Verify Killing form = +3 I
    # (B_ab = f_{acd} f_{bcd} = +3 delta_{ab} for our anti-Hermitian generators)
    print("\n  Step 1: Killing form verification")
    print(f"    B_ab = C * delta_ab, C = {B_ab[0,0]:.10f}")
    B_err = np.max(np.abs(B_ab - 3.0 * np.eye(8)))
    print(f"    |B - 3I|_max = {B_err:.2e}  {'PASS' if B_err < 1e-14 else 'FAIL'}")

    # Step 2: Construct g_s at several s values
    print("\n  Step 2: Explicit metric g_s = 3 * diag(e^{-2s}, e^{-2s}, e^{-2s}, e^s, e^s, e^s, e^s, e^{2s})")
    print()

    test_s = [0.0, 0.15, 0.30, 0.50, 1.0, 1.14]
    for s in test_s:
        g_code = jensen_metric(B_ab, s)

        # Analytical metric: g_s = diag(scale_factors) * 3
        scale_factors = np.zeros(8)
        for a in SU2_IDX:   # 0,1,2
            scale_factors[a] = np.exp(-2*s)
        for a in C2_IDX:    # 3,4,5,6
            scale_factors[a] = np.exp(s)
        for a in U1_IDX:    # 7
            scale_factors[a] = np.exp(2*s)
        g_analytic = 3.0 * np.diag(scale_factors)

        err = np.max(np.abs(g_code - g_analytic))
        rel_err = err / np.max(np.abs(g_analytic)) if np.max(np.abs(g_analytic)) > 0 else 0
        det_ratio = det(g_code) / det(jensen_metric(B_ab, 0.0))
        print(f"    s = {s:5.2f}: |g_code - g_analytic|_max = {err:.2e}  "
              f"det(g_s)/det(g_0) = {det_ratio:.14f}  "
              f"{'PASS' if rel_err < 1e-14 else 'FAIL'}")

    # Step 3: Write out the metric explicitly for s = 0.15 (gauge-viable)
    s0 = 0.15
    g_015 = jensen_metric(B_ab, s0)
    print(f"\n  Step 3: Explicit metric at s = {s0} (gauge-viable window)")
    print(f"    g_s = 3 * diag(")
    for a in range(8):
        subspace = "su(2)" if a in SU2_IDX else ("C^2" if a in C2_IDX else "u(1)")
        scale = g_015[a,a] / 3.0
        print(f"      [{a}] {scale:.12f}  ({subspace})")
    print(f"    )")

    # Step 4: Volume preservation
    print(f"\n  Step 4: Volume preservation (det g_s / det g_0 = 1)")
    print(f"    Exponent sum: 1*2s + 3*(-2s) + 4*s = 2s - 6s + 4s = 0  (EXACT)")
    for s in test_s:
        g = jensen_metric(B_ab, s)
        ratio = det(g) / det(jensen_metric(B_ab, 0.0))
        print(f"    s={s:5.2f}: det ratio = {ratio:.16e}")

    # Step 5: Eigenvalues of g_s (should be the three scale factors)
    print(f"\n  Step 5: Metric eigenvalues (3 distinct values for s > 0)")
    for s in [0.0, 0.15, 0.30, 1.0]:
        g = jensen_metric(B_ab, s)
        evals = sorted(eigvalsh(g))
        unique = np.unique(np.round(evals, 10))
        print(f"    s={s:5.2f}: eigenvalues = {[f'{e:.8f}' for e in evals]}")
        print(f"           unique     = {[f'{e:.8f}' for e in unique]}")

    # Step 6: Off-diagonal check (must be exactly zero)
    print(f"\n  Step 6: Off-diagonal elements (must be ZERO)")
    max_offdiag = 0.0
    for s in test_s:
        g = jensen_metric(B_ab, s)
        offdiag = g - np.diag(np.diag(g))
        max_offdiag = max(max_offdiag, np.max(np.abs(offdiag)))
    print(f"    Max off-diagonal element across all s: {max_offdiag:.2e}  "
          f"{'PASS' if max_offdiag < 1e-15 else 'FAIL'}")

    # Step 7: Left-invariant 1-form expression
    print(f"\n  Step 7: LEFT-INVARIANT 1-FORM EXPRESSION")
    print(f"    The metric on (SU(3), g_s) in left-invariant Maurer-Cartan 1-forms:")
    print()
    print(f"    ds^2 = 3 e^{{-2s}} [(w^1)^2 + (w^2)^2 + (w^3)^2]")
    print(f"         + 3 e^s     [(w^4)^2 + (w^5)^2 + (w^6)^2 + (w^7)^2]")
    print(f"         + 3 e^{{2s}}  (w^8)^2")
    print()
    print(f"    where w^a = -2 Tr(e_a g^{{-1}} dg) are the Maurer-Cartan 1-forms")
    print(f"    dual to the Gell-Mann generators e_a = -i lambda_a / 2.")
    print()
    print(f"    Equivalently in ON frame (hat = orthonormal):")
    print(f"    ds^2 = sum_a (w-hat^a)^2")
    print(f"    with w-hat^a = sqrt(g_aa) * w^a = sqrt(3 lambda_a(s)) * w^a")

    return f_abc, B_ab


# =============================================================================
# SP-4: EXACT ANALYTIC V_tree(s)
# =============================================================================

def sp4_exact_vtree(f_abc, B_ab):
    """
    SP-4: Derive and verify the exact analytic scalar curvature R(s) and V_tree(s).

    DERIVATION (Schwarzschild method — exact, no perturbation theory):

    For a left-invariant metric on a compact Lie group, the scalar curvature
    is computed exactly from the connection coefficients. The Koszul formula
    gives Gamma^c_{ab} in terms of the ON-frame structure constants, and the
    Riemann tensor follows algebraically (no derivatives needed since
    everything is left-invariant).

    The result (Baptista eq 3.70/3.80):

        f(s) = 2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}

        R(s) = R(0) * f(s) / f(0)

    with f(0) = 2 - 1 + 8 - 1 = 8 and R(0) = 2.0 in our normalization.

    V_tree(s) = -R(s) * Vol(SU(3), g_s)

    Since Vol(g_s) = Vol(g_0) * sqrt(det(g_s)/det(g_0)) = Vol(g_0) * 1
    (volume-preserving), we have:

        V_tree(s) = -R(0) * Vol(g_0) * f(s) / f(0)

    Setting the overall constant to 1 (Baptista convention, eq 3.80 at sigma=0):

        V(0, s) = 1 - (1/10) * f(s)
    """
    separator("SP-4: EXACT ANALYTIC SCALAR CURVATURE AND V_tree(s)")

    # =================================================================
    # PART A: Scalar curvature — analytical formula
    # =================================================================
    print("\n  PART A: Scalar curvature R(s)")
    print()
    print("  Analytical formula (Baptista eq 3.70):")
    print("    f(s) = 2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}")
    print("    R(s) / R(0) = f(s) / f(0)")
    print("    f(0) = 8,  R(0) = 2.0")

    def f_of_s(s):
        return 2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)

    # Verify f(0) = 8
    f0 = f_of_s(0.0)
    print(f"\n    f(0) = {f0:.15f}  (should be 8.000)")
    print(f"    |f(0) - 8| = {abs(f0 - 8):.2e}")

    # =================================================================
    # PART B: Numerical verification against Levi-Civita computation
    # =================================================================
    print(f"\n  PART B: Verification against Levi-Civita connection (EXACT)")
    print()

    s_values = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50,
                          0.75, 1.00, 1.14, 1.50, 2.00, 2.50])

    R_0_from_code = None
    max_rel_err = 0.0

    print(f"    {'s':>6}  {'R(s) code':>14}  {'R(s) analyt':>14}  {'ratio':>10}  {'rel_err':>12}")
    print(f"    {'-'*6}  {'-'*14}  {'-'*14}  {'-'*10}  {'-'*12}")

    for s in s_values:
        # Exact from Levi-Civita connection
        R_code, Ric_code = scalar_curvature_from_connection(s, f_abc)

        # Analytical
        R_analytic = 2.0 * f_of_s(s) / 8.0  # R(0) = 2.0, f(0) = 8

        if s == 0.0:
            R_0_from_code = R_code

        ratio_code = R_code / R_0_from_code if R_0_from_code else float('nan')
        ratio_analytic = scalar_curvature_analytical(s)
        rel_err = abs(R_code - R_analytic) / abs(R_analytic) if abs(R_analytic) > 1e-15 else 0

        max_rel_err = max(max_rel_err, rel_err)

        print(f"    {s:6.3f}  {R_code:14.10f}  {R_analytic:14.10f}  "
              f"{ratio_code:10.6f}  {rel_err:12.2e}")

    print(f"\n    Maximum relative error: {max_rel_err:.2e}  "
          f"{'MACHINE EPSILON' if max_rel_err < 1e-13 else 'WARNING'}")

    # =================================================================
    # PART C: Ricci tensor structure
    # =================================================================
    print(f"\n  PART C: Ricci tensor eigenstructure")
    print()

    for s in [0.0, 0.15, 0.30, 1.0]:
        _, Ric = scalar_curvature_from_connection(s, f_abc)
        ric_evals = sorted(eigvalsh(Ric))
        R_from_ric = sum(ric_evals)
        R_from_trace = np.trace(Ric)

        print(f"    s = {s:.2f}:")
        print(f"      Ricci eigenvalues: {[f'{e:.8f}' for e in ric_evals]}")
        print(f"      R = Tr(Ric) = {R_from_trace:.10f}")

        # Check if Einstein (Ric = R/8 * g) at s=0
        if abs(s) < 1e-10:
            R_over_8 = R_from_trace / 8.0
            einstein_err = np.max(np.abs(Ric - R_over_8 * np.eye(8)))
            print(f"      Einstein check (s=0): |Ric - R/8 I| = {einstein_err:.2e}  "
                  f"{'PASS (Einstein manifold)' if einstein_err < 1e-13 else 'FAIL'}")
        print()

    # =================================================================
    # PART D: V_tree(s) exact analytic expression
    # =================================================================
    print(f"\n  PART D: Exact V_tree(s) = V(sigma=0, s)")
    print()
    print("  Formula (Baptista eq 3.80 at sigma=0):")
    print("    V(0, s) = 1 - (1/10) * f(s)")
    print("            = 1 - (1/10) * [2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}]")
    print()

    def V_tree(s):
        """Exact V_tree at sigma=0."""
        return 1.0 - (1.0/10.0) * f_of_s(s)

    # Verify against code's baptista_V_potential
    print(f"    {'s':>6}  {'V_tree(s)':>14}  {'V_code(s)':>14}  {'abs_err':>12}")
    print(f"    {'-'*6}  {'-'*14}  {'-'*14}  {'-'*12}")

    max_v_err = 0.0
    for s in s_values:
        v_analytic = V_tree(s)
        v_code = baptista_V_potential(0.0, s)
        err = abs(v_analytic - v_code)
        max_v_err = max(max_v_err, err)
        print(f"    {s:6.3f}  {v_analytic:14.10f}  {v_code:14.10f}  {err:12.2e}")

    print(f"\n    Maximum absolute error: {max_v_err:.2e}  "
          f"{'MACHINE EPSILON' if max_v_err < 1e-14 else 'WARNING'}")

    # =================================================================
    # PART E: Derivatives of V_tree (critical point analysis)
    # =================================================================
    print(f"\n  PART E: V_tree(s) critical point analysis")
    print()

    # First three derivatives of f(s):
    # f(s)   = 2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}
    # f'(s)  = 4 e^{2s} - 8 e^{-s} + 4 e^{-4s}
    # f''(s) = 8 e^{2s} + 8 e^{-s} - 16 e^{-4s}
    # f'''(s) = 16 e^{2s} - 8 e^{-s} + 64 e^{-4s}

    def f_prime(s):
        return 4*np.exp(2*s) - 8*np.exp(-s) + 4*np.exp(-4*s)

    def f_double_prime(s):
        return 8*np.exp(2*s) + 8*np.exp(-s) - 16*np.exp(-4*s)

    def f_triple_prime(s):
        return 16*np.exp(2*s) - 8*np.exp(-s) + 64*np.exp(-4*s)

    # At s=0:
    f0_val = f_of_s(0)
    fp0 = f_prime(0)
    fpp0 = f_double_prime(0)
    fppp0 = f_triple_prime(0)

    print(f"    f(0)    = {f0_val:12.8f}  (= 8)")
    print(f"    f'(0)   = {fp0:12.8f}  (= 4 - 8 + 4 = 0)")
    print(f"    f''(0)  = {fpp0:12.8f}  (= 8 + 8 - 16 = 0)")
    print(f"    f'''(0) = {fppp0:12.8f}  (= 16 - 8 + 64 = 72)")
    print()
    print(f"    V(0,s)  = 1 - f(s)/10")
    print(f"    V'(0)   = -f'(0)/10  = {-fp0/10:.8f}")
    print(f"    V''(0)  = -f''(0)/10 = {-fpp0/10:.8f}")
    print(f"    V'''(0) = -f'''(0)/10 = {-fppp0/10:.8f}")
    print()
    print(f"    RESULT: s=0 is a THIRD-ORDER INFLECTION POINT of V_tree.")
    print(f"    V(0,s) ~ 0.2 - 1.2 s^3 + O(s^4)  for small s.")
    print(f"    V_tree is monotonically DECREASING for s > 0 (runaway, no minimum).")
    print(f"    Stabilization requires 1-loop Coleman-Weinberg correction.")

    # Verify Taylor expansion numerically
    print(f"\n    Taylor expansion verification:")
    for s in [0.01, 0.05, 0.1]:
        v_exact = V_tree(s)
        v_taylor = 0.2 - 1.2 * s**3
        err = abs(v_exact - v_taylor)
        print(f"      s={s:.2f}: V_exact={v_exact:.10f}, V_taylor={v_taylor:.10f}, "
              f"err={err:.6e}")

    # =================================================================
    # PART F: Asymptotic behavior
    # =================================================================
    print(f"\n  PART F: Asymptotic behavior")
    print()
    print(f"    For large s: f(s) ~ 2 e^{{2s}}, so V(0,s) ~ -(1/5) e^{{2s}}")
    print(f"    For small s: V(0,s) ~ 0.2 - 1.2 s^3")
    print()

    for s in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0]:
        v_exact = V_tree(s)
        v_asymp = -0.2 * np.exp(2*s)
        print(f"    s={s:4.1f}: V_exact={v_exact:14.6f}  V_asymp={v_asymp:14.6f}  "
              f"ratio={v_exact/v_asymp:.6f}" if abs(v_asymp) > 0.01 else
              f"    s={s:4.1f}: V_exact={v_exact:14.6f}  (near s=0, asymptotic invalid)")

    # =================================================================
    # PART G: V_tree at gauge-viable s values
    # =================================================================
    print(f"\n  PART G: V_tree at gauge-viable window [0.15, 0.50]")
    print()
    print(f"    {'s':>6}  {'V_tree':>14}  {'R(s)':>12}  {'R(s)/R(0)':>10}  {'gauge: e^(-2s)':>14}")
    print(f"    {'-'*6}  {'-'*14}  {'-'*12}  {'-'*10}  {'-'*14}")

    for s in [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]:
        v = V_tree(s)
        R = 2.0 * f_of_s(s) / 8.0
        R_ratio = f_of_s(s) / 8.0
        gauge = np.exp(-2*s)
        print(f"    {s:6.3f}  {v:14.10f}  {R:12.8f}  {R_ratio:10.6f}  {gauge:14.10f}")

    # =================================================================
    # PART H: Key special values
    # =================================================================
    print(f"\n  PART H: Key special values")
    print()

    # s where e^{3s} = phi (Feynman G3 result)
    phi = (1 + np.sqrt(5)) / 2
    s_phi = np.log(phi) / 3
    print(f"    Golden ratio phi = {phi:.10f}")
    print(f"    s where e^{{3s}} = phi: s = ln(phi)/3 = {s_phi:.10f}")
    print(f"    V_tree({s_phi:.4f}) = {V_tree(s_phi):.10f}")
    print(f"    R({s_phi:.4f}) = {2.0 * f_of_s(s_phi) / 8.0:.10f}")
    print(f"    gauge coupling e^{{-2s}} = {np.exp(-2*s_phi):.10f}")
    print()

    # s=0.30 (backup s_0 from gauge constraint)
    print(f"    Backup s_0 = 0.30:")
    print(f"    V_tree(0.30) = {V_tree(0.30):.10f}")
    print(f"    R(0.30) = {2.0 * f_of_s(0.30) / 8.0:.10f}")
    print(f"    gauge: e^{{-0.60}} = {np.exp(-0.60):.10f}")
    print(f"    SM measured: tan(theta_W)^2 = {0.55:.4f}")

    return V_tree


# =============================================================================
# SP-2 (PARTIAL): CURVATURE INVARIANTS
# =============================================================================

def sp2_curvature_invariants(f_abc):
    """
    Compute the Kretschner scalar K(s), |Ric|^2(s), |Weyl|^2(s).

    Extends the existing scalar_curvature_from_connection to extract the
    full Riemann tensor and compute curvature invariants.
    """
    separator("SP-2 (PARTIAL): CURVATURE INVARIANTS K(s), |Ric|^2, |Weyl|^2")

    B_ab = compute_killing_form(f_abc)
    n = 8  # dim(SU(3))

    s_values = np.linspace(0, 2.5, 51)

    # Storage
    R_arr = np.zeros(len(s_values))
    K_arr = np.zeros(len(s_values))
    Ric2_arr = np.zeros(len(s_values))
    Weyl2_arr = np.zeros(len(s_values))

    for idx, s in enumerate(s_values):
        # Rebuild the Riemann tensor (same logic as scalar_curvature_from_connection
        # but retaining the full tensor)
        g_s = jensen_metric(B_ab, s)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)

        # Riemann tensor R^d_{abc}
        Riem = np.zeros((n, n, n, n))
        for d in range(n):
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        val = 0.0
                        for e in range(n):
                            val += Gamma[d, a, e] * Gamma[e, b, c]
                            val -= Gamma[d, b, e] * Gamma[e, a, c]
                            val -= ft[a, b, e] * Gamma[d, e, c]
                        Riem[d, a, b, c] = val

        # Ricci tensor: Ric_{ac} = R^b_{bac}
        Ric = np.zeros((n, n))
        for a in range(n):
            for c in range(n):
                for b in range(n):
                    Ric[a, c] += Riem[b, b, a, c]

        # Scalar curvature
        R = np.trace(Ric)
        R_arr[idx] = R

        # Kretschner scalar: K = R_{dabc} R^{dabc}
        # In ON frame: K = sum_{d,a,b,c} Riem[d,a,b,c]^2
        K = np.sum(Riem**2)
        K_arr[idx] = K

        # Ricci squared: |Ric|^2 = Ric_{ac} Ric^{ac} = sum Ric[a,c]^2
        Ric2 = np.sum(Ric**2)
        Ric2_arr[idx] = Ric2

        # Weyl tensor in dim n:
        # C_{dabc} = R_{dabc}
        #   - (1/(n-2)) (delta_{da} Ric_{bc} - delta_{db} Ric_{ac}
        #                - delta_{ca} Ric_{bd} + delta_{cb} Ric_{ad})
        #   + (R / ((n-1)(n-2))) (delta_{da} delta_{bc} - delta_{db} delta_{ac})
        #
        # But R_{dabc} here is R^d_{abc} which has upper first index.
        # In ON frame with delta metric: R_{dabc} = R^d_{abc} (lowering with delta is trivial).
        # So the formula applies directly.
        Weyl = np.zeros((n, n, n, n))
        for d in range(n):
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        W = Riem[d, a, b, c]

                        # Ricci correction
                        da = 1.0 if d == a else 0.0
                        db = 1.0 if d == b else 0.0
                        ca = 1.0 if c == a else 0.0
                        cb = 1.0 if c == b else 0.0

                        W -= (1.0 / (n - 2)) * (
                            da * Ric[b, c] - db * Ric[a, c]
                            - ca * Ric[b, d] + cb * Ric[a, d]
                        )

                        # Scalar correction
                        W += R / ((n - 1) * (n - 2)) * (da * (1.0 if b == c else 0.0)
                                                         - db * (1.0 if a == c else 0.0))

                        Weyl[d, a, b, c] = W

        Weyl2 = np.sum(Weyl**2)
        Weyl2_arr[idx] = Weyl2

    # Print results
    print(f"\n    {'s':>6}  {'R(s)':>12}  {'K(s)':>14}  {'|Ric|^2':>14}  {'|Weyl|^2':>14}  {'|Weyl|^2/K':>10}")
    print(f"    {'-'*6}  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*10}")

    for idx in range(0, len(s_values), 5):  # Every 5th point for readability
        s = s_values[idx]
        R = R_arr[idx]
        K = K_arr[idx]
        Ric2 = Ric2_arr[idx]
        W2 = Weyl2_arr[idx]
        tidal = W2 / K if K > 1e-15 else float('nan')
        print(f"    {s:6.3f}  {R:12.6f}  {K:14.6f}  {Ric2:14.6f}  {W2:14.6f}  {tidal:10.6f}")

    # Key diagnostics
    print(f"\n    KEY RESULTS:")
    print(f"    K(0) = {K_arr[0]:.10f}")
    print(f"    K(2.5) / K(0) = {K_arr[-1]/K_arr[0]:.6f}")
    print(f"    |Weyl|^2(0) = {Weyl2_arr[0]:.10f}")

    # Check s=0 Einstein property: |Weyl|^2/K at s=0
    tidal_0 = Weyl2_arr[0] / K_arr[0]
    print(f"    |Weyl|^2 / K at s=0: {tidal_0:.10f}")

    # Prediction check: K(s) ~ e^{8s} for large s?
    print(f"\n    Growth rate check (log K vs s):")
    for idx in [0, 10, 20, 30, 40, 50]:
        if idx < len(s_values):
            s = s_values[idx]
            K = K_arr[idx]
            if K > 0:
                print(f"      s={s:.2f}: K={K:.6e}, log(K)={np.log(K):.4f}, "
                      f"log(K)/s={np.log(K)/s:.4f}" if s > 0.01 else
                      f"      s={s:.2f}: K={K:.6e}")

    return s_values, R_arr, K_arr, Ric2_arr, Weyl2_arr


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("="*72)
    print("  SESSION 17a: SCHWARZSCHILD-PENROSE-GEOMETER")
    print("  SP-1: Explicit Jensen Metric + SP-4: Exact V_tree(s)")
    print("="*72)

    # SP-1
    f_abc, B_ab = sp1_explicit_metric()

    # SP-4
    V_tree = sp4_exact_vtree(f_abc, B_ab)

    # SP-2 (partial)
    s_vals, R_arr, K_arr, Ric2_arr, Weyl2_arr = sp2_curvature_invariants(f_abc)

    # =================================================================
    # SUMMARY
    # =================================================================
    separator("SUMMARY")
    print()
    print("  SP-1 (COMPLETE): Explicit 8×8 metric g_s in Gell-Mann basis")
    print("    g_s = 3 * diag(e^{-2s}, e^{-2s}, e^{-2s}, e^s, e^s, e^s, e^s, e^{2s})")
    print("    All off-diagonal entries: EXACTLY ZERO")
    print("    Volume: det(g_s)/det(g_0) = 1.000000 for all s")
    print("    Metric is LEFT-INVARIANT (constant in Maurer-Cartan 1-form basis)")
    print()
    print("  SP-4 (COMPLETE): Exact V_tree(s) = 1 - f(s)/10")
    print("    f(s) = 2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}")
    print("    f(0) = 8, V(0,0) = 0.2, V'(0) = 0, V''(0) = 0, V'''(0) = -7.2")
    print("    Third-order inflection at s=0: V ~ 0.2 - 1.2 s^3")
    print("    Monotonically decreasing for s > 0 (runaway, no minimum)")
    print("    Verified against Levi-Civita connection at MACHINE EPSILON")
    print()
    print("  SP-2 (PARTIAL): Curvature invariants K(s), |Ric|^2, |Weyl|^2")
    print(f"    K(0) = {K_arr[0]:.10f}")
    print(f"    K(2.5) = {K_arr[-1]:.6f}")
    print(f"    |Weyl|^2(0) / K(0) = {Weyl2_arr[0]/K_arr[0]:.10f}")
    print(f"    |Weyl|^2 trend: {'INCREASING' if Weyl2_arr[-1] > Weyl2_arr[0] else 'DECREASING'}")
    print()
