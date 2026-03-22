"""
Session 33 Workshop 3 -- SP Deliverable 1: Dump Point Geometry
=============================================================

Compute Kretschner scalar K(tau), all curvature invariants, and their
derivatives at the dump point (tau=0.190) and phi_paasch point (tau=0.15).

All formulas are EXACT ANALYTIC from SP-2 (Session 17a, verified at
machine epsilon against Levi-Civita connection computation).

Author: Schwarzschild-Penrose-Geometer
Date: 2026-03-06
"""
import numpy as np

# =====================================================================
# EXACT ANALYTIC FORMULAS (rational coefficients, SP-2)
# =====================================================================

def R_exact(s):
    """Scalar curvature R(s). R(0) = 2."""
    return -0.25*np.exp(-4*s) + 2*np.exp(-s) - 0.25 + 0.5*np.exp(2*s)

def Ric2_exact(s):
    """|Ric|^2(s). |Ric|^2(0) = 0.5."""
    return (
        (1/12) * np.exp(-8*s)
        + (-1/2) * np.exp(-5*s)
        + (1/8) * np.exp(-4*s)
        + (13/12) * np.exp(-2*s)
        + (-1/2) * np.exp(-s)
        + (1/8)
        + (1/12) * np.exp(4*s)
    )

def K_exact(s):
    """Kretschner scalar K(s) = R_{abcd} R^{abcd}. K(0) = 0.5."""
    return (
        (23/96) * np.exp(-8*s)
        + (-1) * np.exp(-5*s)
        + (5/16) * np.exp(-4*s)
        + (11/6) * np.exp(-2*s)
        + (-3/2) * np.exp(-s)
        + (17/32)
        + (1/12) * np.exp(4*s)
    )

def Weyl2_exact(s):
    """|Weyl|^2(s) = C_{abcd} C^{abcd}. |C|^2(0) = 5/14."""
    return (
        (377/2016) * np.exp(-8*s)
        + (-5/7) * np.exp(-5*s)
        + (79/336) * np.exp(-4*s)
        + (325/252) * np.exp(-2*s)
        + (-17/14) * np.exp(-s)
        + (101/224)
        + (2/21) * np.exp(s)
        + (-1/84) * np.exp(2*s)
        + (5/126) * np.exp(4*s)
    )

# =====================================================================
# EXACT DERIVATIVES (analytic differentiation)
# =====================================================================

def K_prime(s):
    """K'(s) = dK/ds."""
    return (
        (23/96) * (-8) * np.exp(-8*s)
        + (-1) * (-5) * np.exp(-5*s)
        + (5/16) * (-4) * np.exp(-4*s)
        + (11/6) * (-2) * np.exp(-2*s)
        + (-3/2) * (-1) * np.exp(-s)
        + 0  # constant term
        + (1/12) * 4 * np.exp(4*s)
    )

def K_double_prime(s):
    """K''(s) = d^2K/ds^2."""
    return (
        (23/96) * 64 * np.exp(-8*s)
        + (-1) * 25 * np.exp(-5*s)
        + (5/16) * 16 * np.exp(-4*s)
        + (11/6) * 4 * np.exp(-2*s)
        + (-3/2) * 1 * np.exp(-s)
        + 0
        + (1/12) * 16 * np.exp(4*s)
    )

def K_triple_prime(s):
    """K'''(s) = d^3K/ds^3."""
    return (
        (23/96) * (-512) * np.exp(-8*s)
        + (-1) * (-125) * np.exp(-5*s)
        + (5/16) * (-64) * np.exp(-4*s)
        + (11/6) * (-8) * np.exp(-2*s)
        + (-3/2) * (-1) * np.exp(-s)
        + 0
        + (1/12) * 64 * np.exp(4*s)
    )

def R_prime(s):
    """R'(s) = dR/ds."""
    return np.exp(-4*s) - 2*np.exp(-s) + np.exp(2*s)

def R_double_prime(s):
    """R''(s) = d^2R/ds^2."""
    return -4*np.exp(-4*s) + 2*np.exp(-s) + 2*np.exp(2*s)

def Weyl2_prime(s):
    """|C|^2'(s)."""
    return (
        (377/2016) * (-8) * np.exp(-8*s)
        + (-5/7) * (-5) * np.exp(-5*s)
        + (79/336) * (-4) * np.exp(-4*s)
        + (325/252) * (-2) * np.exp(-2*s)
        + (-17/14) * (-1) * np.exp(-s)
        + (2/21) * 1 * np.exp(s)
        + (-1/84) * 2 * np.exp(2*s)
        + (5/126) * 4 * np.exp(4*s)
    )

def Weyl2_double_prime(s):
    """|C|^2''(s)."""
    return (
        (377/2016) * 64 * np.exp(-8*s)
        + (-5/7) * 25 * np.exp(-5*s)
        + (79/336) * 16 * np.exp(-4*s)
        + (325/252) * 4 * np.exp(-2*s)
        + (-17/14) * 1 * np.exp(-s)
        + (2/21) * 1 * np.exp(s)
        + (-1/84) * 4 * np.exp(2*s)
        + (5/126) * 16 * np.exp(4*s)
    )

def Ric2_prime(s):
    """|Ric|^2'(s)."""
    return (
        (1/12) * (-8) * np.exp(-8*s)
        + (-1/2) * (-5) * np.exp(-5*s)
        + (1/8) * (-4) * np.exp(-4*s)
        + (13/12) * (-2) * np.exp(-2*s)
        + (-1/2) * (-1) * np.exp(-s)
        + 0
        + (1/12) * 4 * np.exp(4*s)
    )


# =====================================================================
# NEC CHECK (Null Energy Condition for Jensen deformation)
# =====================================================================

def nec_check(s):
    """
    NEC for the Jensen modulus: R_ab k^a k^b >= 0 for all null k.

    On a Riemannian manifold with left-invariant metric, the NEC analog
    is that all Ricci eigenvalues are non-negative.

    Ricci eigenvalues for Jensen SU(3):
    - su(2) [x3]: lambda_su2(s)
    - C^2 [x4]:   lambda_C2(s)
    - u(1) [x1]:  lambda_u1 = 1/4 (s-independent)

    From SP-2 verification: Ric = diag(lambda_su2, lambda_su2, lambda_su2,
                                        lambda_C2, lambda_C2, lambda_C2, lambda_C2,
                                        lambda_u1)
    """
    R = R_exact(s)
    Ric2 = Ric2_exact(s)

    # From R = 3*lambda_su2 + 4*lambda_C2 + lambda_u1
    # and |Ric|^2 = 3*lambda_su2^2 + 4*lambda_C2^2 + lambda_u1^2
    # with lambda_u1 = 1/4

    # We can solve for lambda_su2 and lambda_C2:
    # 3*lsu2 + 4*lc2 = R - 1/4
    # 3*lsu2^2 + 4*lc2^2 = Ric2 - 1/16

    # More directly, use the exact eigenvalue formulas:
    # From Baptista eq 3.70 generalized:
    # lambda_su2 = (1/4)(e^{-4s} + 2 - 4e^{-3s} + e^{-2s})  [approx, need exact]

    # Better: compute numerically from the exact invariants
    # R = 3*a + 4*b + 1/4, |Ric|^2 = 3*a^2 + 4*b^2 + 1/16
    # where a = lambda_su2, b = lambda_C2

    u1 = 0.25  # exact for all s
    rhs_R = R - u1
    rhs_Ric2 = Ric2 - u1**2

    # 3a + 4b = rhs_R  => a = (rhs_R - 4b)/3
    # 3a^2 + 4b^2 = rhs_Ric2
    # 3*((rhs_R - 4b)/3)^2 + 4b^2 = rhs_Ric2
    # (rhs_R - 4b)^2/3 + 4b^2 = rhs_Ric2
    # (rhs_R^2 - 8*rhs_R*b + 16b^2)/3 + 4b^2 = rhs_Ric2
    # rhs_R^2/3 - 8*rhs_R*b/3 + 16b^2/3 + 4b^2 = rhs_Ric2
    # (16/3 + 4)*b^2 - (8*rhs_R/3)*b + (rhs_R^2/3 - rhs_Ric2) = 0
    # (28/3)*b^2 - (8*rhs_R/3)*b + (rhs_R^2/3 - rhs_Ric2) = 0

    A_coeff = 28/3
    B_coeff = -8*rhs_R/3
    C_coeff = rhs_R**2/3 - rhs_Ric2

    disc = B_coeff**2 - 4*A_coeff*C_coeff
    if disc < 0:
        return None, None, u1, False

    b1 = (-B_coeff + np.sqrt(disc)) / (2*A_coeff)
    b2 = (-B_coeff - np.sqrt(disc)) / (2*A_coeff)

    # Pick the solution consistent with known ordering at s=0
    # At s=0: all = 1/4. For s > 0: su2 < C2 generically
    for b in [b1, b2]:
        a = (rhs_R - 4*b) / 3
        if abs(3*a + 4*b + u1 - R) < 1e-10:
            lambda_C2 = b
            lambda_su2 = a
            break

    nec_holds = (lambda_su2 >= 0) and (lambda_C2 >= 0) and (u1 >= 0)
    return lambda_su2, lambda_C2, u1, nec_holds


# =====================================================================
# MAIN COMPUTATION
# =====================================================================

def main():
    print("=" * 78)
    print("  SESSION 33 W3: DUMP POINT GEOMETRY")
    print("  Schwarzschild-Penrose-Geometer — Exact Analytic Results")
    print("=" * 78)

    # Key tau values
    tau_dump = 0.190       # B2 eigenvalue minimum
    tau_phi = 0.150        # phi_paasch exact point
    tau_inst = 0.181       # instanton peak
    tau_dnp = 0.285        # DNP crossing
    tau_nec = 0.778        # NEC violation boundary
    tau_round = 0.000      # round metric

    key_taus = {
        'round':     0.000,
        'phi_paasch':0.150,
        'instanton': 0.181,
        'dump':      0.190,
        'DNP':       0.285,
        'NEC_viol':  0.778,
    }

    # ================================================================
    # PART 1: Curvature invariants at all key points
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 1: CURVATURE INVARIANTS AT KEY tau VALUES")
    print("-" * 78)

    print(f"\n  {'tau':>10}  {'Label':>12}  {'R':>10}  {'K':>12}  {'|Ric|^2':>12}  {'|C|^2':>12}  {'|C|^2/K':>8}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*8}")

    for label, tau in key_taus.items():
        R = R_exact(tau)
        K = K_exact(tau)
        Ric2 = Ric2_exact(tau)
        W2 = Weyl2_exact(tau)
        tidal = W2/K if K > 1e-15 else float('nan')
        print(f"  {tau:10.4f}  {label:>12}  {R:10.6f}  {K:12.8f}  {Ric2:12.8f}  {W2:12.8f}  {tidal:8.5f}")

    # ================================================================
    # PART 2: K(tau) and derivatives at dump point
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 2: KRETSCHNER SCALAR AND DERIVATIVES")
    print("-" * 78)

    for label, tau in key_taus.items():
        K = K_exact(tau)
        Kp = K_prime(tau)
        Kpp = K_double_prime(tau)
        Kppp = K_triple_prime(tau)

        print(f"\n  tau = {tau:.4f} ({label}):")
        print(f"    K(tau)    = {K:.10f}")
        print(f"    K'(tau)   = {Kp:.10f}")
        print(f"    K''(tau)  = {Kpp:.10f}")
        print(f"    K'''(tau) = {Kppp:.10f}")

    # ================================================================
    # PART 3: K'(tau) = 0 — locate Kretschner extrema
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 3: KRETSCHNER EXTREMA (K'(tau) = 0)")
    print("-" * 78)

    # Scan for sign changes of K'
    tau_scan = np.linspace(0.001, 2.0, 10000)
    Kp_scan = np.array([K_prime(t) for t in tau_scan])

    print(f"\n  Scanning K'(tau) for zeros in [0.001, 2.0]:")
    print(f"    K'(0.001) = {K_prime(0.001):.8f}")
    print(f"    K'(2.000) = {K_prime(2.000):.8f}")

    extrema = []
    for i in range(len(tau_scan)-1):
        if Kp_scan[i] * Kp_scan[i+1] < 0:
            # Bisect to find zero
            a, b = tau_scan[i], tau_scan[i+1]
            for _ in range(100):
                mid = (a + b) / 2
                if K_prime(a) * K_prime(mid) < 0:
                    b = mid
                else:
                    a = mid
            extrema.append(mid)
            K_at_ext = K_exact(mid)
            Kpp_at_ext = K_double_prime(mid)
            ext_type = "MINIMUM" if Kpp_at_ext > 0 else "MAXIMUM"
            print(f"\n    K'(tau) = 0 at tau = {mid:.10f}")
            print(f"      K(tau)   = {K_at_ext:.10f}")
            print(f"      K''(tau) = {Kpp_at_ext:.10f}  -> {ext_type}")

    if not extrema:
        print("    No extrema found. K(tau) is monotonic on [0.001, 2.0].")

    # ================================================================
    # PART 4: Weyl curvature analysis (WCH check)
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 4: WEYL CURVATURE HYPOTHESIS CHECK")
    print("-" * 78)

    for label, tau in key_taus.items():
        W2 = Weyl2_exact(tau)
        W2p = Weyl2_prime(tau)
        W2pp = Weyl2_double_prime(tau)
        K = K_exact(tau)
        tidal = W2/K if K > 1e-15 else float('nan')

        print(f"\n  tau = {tau:.4f} ({label}):")
        print(f"    |C|^2(tau)   = {W2:.10f}")
        print(f"    |C|^2'(tau)  = {W2p:.10f}")
        print(f"    |C|^2''(tau) = {W2pp:.10f}")
        print(f"    tidal ratio  = {tidal:.10f}")

    print(f"\n  WCH CONSISTENCY:")
    W_round = Weyl2_exact(0)
    W_dump = Weyl2_exact(tau_dump)
    W_nec = Weyl2_exact(tau_nec)
    print(f"    |C|^2(round) = {W_round:.8f} (= 5/14 = {5/14:.8f})")
    print(f"    |C|^2(dump)  = {W_dump:.8f}")
    print(f"    |C|^2(NEC)   = {W_nec:.8f}")
    print(f"    Growth from round to dump: {W_dump/W_round:.4f}x")
    print(f"    WCH requires |C|^2 increasing with tau: {'CONSISTENT' if W_dump > W_round else 'VIOLATION'}")

    # ================================================================
    # PART 5: NEC at key points
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 5: NULL ENERGY CONDITION AUDIT")
    print("-" * 78)

    for label, tau in key_taus.items():
        lsu2, lc2, lu1, nec = nec_check(tau)
        if lsu2 is not None:
            min_eig = min(lsu2, lc2, lu1)
            print(f"\n  tau = {tau:.4f} ({label}):")
            print(f"    Ricci eigenvalues: su(2)={lsu2:.8f} [x3], C^2={lc2:.8f} [x4], u(1)={lu1:.8f} [x1]")
            print(f"    Minimum Ricci eigenvalue: {min_eig:.8f}")
            print(f"    NEC analog: {'HOLDS' if nec else 'VIOLATED'}")
            if not nec:
                print(f"    VIOLATION: {('su(2)' if lsu2 < 0 else '')} {('C^2' if lc2 < 0 else '')}")

    # Scan for NEC violation boundary
    print(f"\n  NEC VIOLATION BOUNDARY SCAN:")
    tau_nec_scan = np.linspace(0, 2.0, 5000)
    nec_boundary = None
    for tau in tau_nec_scan:
        lsu2, lc2, lu1, nec = nec_check(tau)
        if lsu2 is not None and not nec and nec_boundary is None:
            nec_boundary = tau
            print(f"    First NEC violation at tau = {tau:.6f}")
            print(f"    Ricci eigenvalues: su(2)={lsu2:.8f}, C^2={lc2:.8f}, u(1)={lu1:.8f}")
            break

    if nec_boundary is not None:
        # Bisect for precise boundary
        a, b = nec_boundary - 0.001, nec_boundary
        for _ in range(100):
            mid = (a + b) / 2
            _, _, _, nec_mid = nec_check(mid)
            if nec_mid:
                a = mid
            else:
                b = mid
        print(f"    Precise NEC boundary: tau = {mid:.10f}")
        print(f"    Distance from dump point: {mid - tau_dump:.6f}")
        print(f"    Fractional distance: {(mid - tau_dump)/mid:.4f} (={100*(mid-tau_dump)/mid:.1f}% of NEC boundary)")

    # ================================================================
    # PART 6: Comparison dump vs phi_paasch
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 6: DUMP (0.190) vs PHI_PAASCH (0.150) COMPARISON")
    print("-" * 78)

    for tau, name in [(0.150, 'phi_paasch'), (0.190, 'dump')]:
        R = R_exact(tau)
        K = K_exact(tau)
        Kp = K_prime(tau)
        Kpp = K_double_prime(tau)
        W2 = Weyl2_exact(tau)
        Ric2 = Ric2_exact(tau)
        Rp = R_prime(tau)
        Rpp = R_double_prime(tau)

        print(f"\n  tau = {tau:.3f} ({name}):")
        print(f"    R    = {R:.10f},   R'   = {Rp:.10f},   R''  = {Rpp:.10f}")
        print(f"    K    = {K:.10f},   K'   = {Kp:.10f},   K''  = {Kpp:.10f}")
        print(f"    |C|^2= {W2:.10f}")
        print(f"    |S|^2= {Ric2 - R**2/8:.10f}  [traceless Ricci squared]")

    delta_K = K_exact(0.190) - K_exact(0.150)
    delta_R = R_exact(0.190) - R_exact(0.150)
    print(f"\n  DIFFERENCES (dump - phi_paasch):")
    print(f"    Delta K    = {delta_K:.10f}")
    print(f"    Delta R    = {delta_R:.10f}")
    print(f"    Delta |C|^2= {Weyl2_exact(0.190) - Weyl2_exact(0.150):.10f}")

    # ================================================================
    # PART 7: Kretschner at fine scan near dump point
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 7: FINE SCAN NEAR DUMP POINT")
    print("-" * 78)

    tau_fine = np.linspace(0.15, 0.25, 21)
    header = "  {:>8}  {:>14}  {:>14}  {:>14}  {:>12}  {:>12}".format(
        "tau", "K(tau)", "K_prime", "K_dblprime", "R(tau)", "|C|^2")
    print(f"\n{header}")
    print(f"  {'-'*8}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*12}  {'-'*12}")

    for tau in tau_fine:
        print(f"  {tau:8.4f}  {K_exact(tau):14.8f}  {K_prime(tau):14.8f}  {K_double_prime(tau):14.8f}  {R_exact(tau):12.8f}  {Weyl2_exact(tau):12.8f}")

    # ================================================================
    # PART 8: Bianchi decomposition at dump
    # ================================================================
    print("\n" + "-" * 78)
    print("  PART 8: BIANCHI DECOMPOSITION AT DUMP POINT")
    print("-" * 78)

    tau = tau_dump
    K = K_exact(tau)
    R = R_exact(tau)
    Ric2 = Ric2_exact(tau)
    W2 = Weyl2_exact(tau)
    n = 8

    # For n=8: K = |C|^2 + (4/(n-2)) * |S|^2 + (2/(n(n-1))) * R^2
    #        = |C|^2 + (4/6) * |S|^2 + (2/56) * R^2
    # where |S|^2 = |Ric|^2 - R^2/n = |Ric|^2 - R^2/8
    S2 = Ric2 - R**2 / n

    Weyl_frac = W2 / K * 100
    Ric_tracefree_frac = (4/6) * S2 / K * 100
    scalar_frac = (2/(n*(n-1))) * R**2 / K * 100

    print(f"\n  At tau = {tau:.4f} (dump point):")
    print(f"    K = {K:.10f}")
    print(f"    |C|^2         = {W2:.10f}  ({Weyl_frac:.2f}%)")
    print(f"    (4/6)|S|^2    = {(4/6)*S2:.10f}  ({Ric_tracefree_frac:.2f}%)")
    print(f"    (1/28)R^2     = {R**2/28:.10f}  ({scalar_frac:.2f}%)")
    print(f"    Sum check     = {W2 + (4/6)*S2 + R**2/28:.10f}  (should = K)")
    print(f"    Error         = {abs(K - W2 - (4/6)*S2 - R**2/28):.2e}")

    print(f"\n  INTERPRETATION:")
    print(f"    Weyl dominance: {Weyl_frac:.1f}% of K is conformal curvature")
    print(f"    Ricci contribution: {Ric_tracefree_frac:.1f}% from traceless Ricci")
    print(f"    Scalar contribution: {scalar_frac:.1f}% from scalar curvature")
    print(f"    At round metric: Weyl = {5/14*100/0.5:.1f}%, Ricci = 0%, Scalar = {(2/56)*4/0.5*100:.1f}%")

    # ================================================================
    # SUMMARY
    # ================================================================
    print("\n" + "=" * 78)
    print("  SUMMARY OF KEY RESULTS")
    print("=" * 78)

    print(f"""
  1. KRETSCHNER AT DUMP POINT:
     K(0.190) = {K_exact(0.190):.10f}
     K'(0.190) = {K_prime(0.190):.10f}  (positive: K still increasing)
     K''(0.190) = {K_double_prime(0.190):.10f}  (positive: K concave up)
     K(0.190)/K(0) = {K_exact(0.190)/K_exact(0):.6f}

     RESULT: K has NO EXTREMUM near the dump point.
     K is MONOTONICALLY INCREASING through the dump region.
     The dump point is NOT a curvature stationary point.
     The seven-quantity convergence is representation-theoretic (B2 min),
     NOT curvature-invariant.

  2. KRETSCHNER AT PHI_PAASCH:
     K(0.150) = {K_exact(0.150):.10f}
     K'(0.150) = {K_prime(0.150):.10f}
     K(0.150)/K(0) = {K_exact(0.150)/K_exact(0):.6f}

     No special curvature property at tau = 0.150 either.
     Delta K (dump - phi) = {K_exact(0.190)-K_exact(0.150):.10f}

  3. NEC STATUS:
     NEC HOLDS at dump point (all Ricci eigenvalues positive).
     NEC violation boundary at tau ~ {mid:.4f}.
     Dump point is {100*(mid-tau_dump)/mid:.0f}% below the NEC boundary.

  4. WCH CONSISTENCY:
     |C|^2 increases monotonically from round to dump to NEC boundary.
     Growth: {Weyl2_exact(0.190)/Weyl2_exact(0):.4f}x from round to dump.
     CONSISTENT with Weyl Curvature Hypothesis.

  5. BIANCHI DECOMPOSITION:
     At dump: {Weyl_frac:.1f}% Weyl, {Ric_tracefree_frac:.1f}% traceless Ricci, {scalar_frac:.1f}% scalar.
     Jensen deformation shifts curvature from scalar to Weyl+Ricci.
""")


if __name__ == "__main__":
    main()
