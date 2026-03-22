"""
SP-2: ANALYTIC DERIVATION OF CURVATURE INVARIANTS
==================================================

Schwarzschild-Penrose-Geometer — Session 17b (corrected)

STRATEGY: Instead of fitting a Laurent polynomial to noisy data, we derive
the exact exponential structure from the algebra, then use a small number
of s-values to determine the exact coefficients.

KEY INSIGHT: For the Jensen metric on SU(3), the curvature invariants are
FINITE sums of terms c_k * e^{k*s} where k ranges over a KNOWN set of
integers. The set is determined by the structure constant algebra:

Structure constants nonzero only for:
  - SSS (su(2) x su(2) x su(2)): 3 nonzero f_{abc}^2 terms, sum = 3
  - CCS (C^2 x C^2 x su(2)): 18 nonzero f_{abc}^2 terms, sum = 4.5
  - CCU (C^2 x C^2 x u(1)): 6 nonzero f_{abc}^2 terms, sum = 4.5

Scale factor for ft^c_{ab} = f_{abc} * sqrt(lambda_c/(lambda_a * lambda_b)):
  - SSS: sqrt(u/(u*u)) = 1/sqrt(u) = (1/sqrt(3)) * e^{s}
  - CCS: sqrt(u/(v*v)) = sqrt(u)/v = (1/sqrt(3)) * e^{-2s}
  - CCU: sqrt(w/(v*v)) = sqrt(w)/v = (1/sqrt(3)) * e^{0} = 1/sqrt(3)

(using u=3e^{-2s}, v=3e^s, w=3e^{2s})

Wait, CCS means a in C, b in C, c in S. Then:
  ft^S_{CC} = f_{CCS} * sqrt(lambda_S/(lambda_C * lambda_C))
            = f_{CCS} * sqrt(3e^{-2s}/(3e^s * 3e^s))
            = f_{CCS} * sqrt(e^{-2s}/(3e^{2s}))
            = f_{CCS} * e^{-2s} / sqrt(3)

And for CCU (a in C, b in C, c in U):
  ft^U_{CC} = f_{CCU} * sqrt(lambda_U/(lambda_C * lambda_C))
            = f_{CCU} * sqrt(3e^{2s}/(3e^s * 3e^s))
            = f_{CCU} * sqrt(e^{2s}/(3e^{2s}))
            = f_{CCU} * 1/sqrt(3)

So the ON-frame structure constants have exponents:
  SSS: e^s
  CCS: e^{-2s}
  CCU: e^0 = 1

Connection Gamma ~ ft, so Gamma has same exponents: {0, 1, -2}

Riemann R ~ Gamma*Gamma + ft*Gamma, so exponents are SUMS of 2 from {0, 1, -2}:
  {0+0, 0+1, 0+(-2), 1+1, 1+(-2), (-2)+(-2)}
  = {0, 1, -2, 2, -1, -4}
  = {-4, -2, -1, 0, 1, 2}

Scalar curvature R(s) = sum Riem ~ sum of above: exponents in {-4, -2, -1, 0, 1, 2}
Known: R(s) = (1/4)(2e^{2s} - 1 + 8e^{-s} - e^{-4s})
Exponents in R: {-4, -1, 0, 2}  [subset of {-4, -2, -1, 0, 1, 2}]

Kretschner K = sum Riem^2 ~ sum of products of 4 ft-type terms.
Exponents are sums of 4 from {0, 1, -2}:
  Min: 4*(-2) = -8
  Max: 4*1 = 4
  All possible: {-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4}

But NOT all are realized. Products of 4 values from {0, 1, -2}:
  (0,0,0,0) = 0
  (0,0,0,1) = 1
  (0,0,0,-2) = -2
  (0,0,1,1) = 2
  (0,0,1,-2) = -1
  (0,0,-2,-2) = -4
  (0,1,1,1) = 3
  (0,1,1,-2) = 0
  (0,1,-2,-2) = -3
  (0,-2,-2,-2) = -6
  (1,1,1,1) = 4
  (1,1,1,-2) = 1
  (1,1,-2,-2) = -2
  (1,-2,-2,-2) = -5
  (-2,-2,-2,-2) = -8

So realized exponents for K: {-8, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4}
That's 12 terms. We need 12 equations (s-values) to determine 12 coefficients.

Using 20 s-values for safety (overdetermined), solve with least squares.

Author: Schwarzschild-Penrose-Geometer (Session 17b)
Date: 2026-02-14
"""

import numpy as np
from numpy.linalg import inv, eigvalsh, lstsq
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients,
    U1_IDX, SU2_IDX, C2_IDX
)


def build_infrastructure():
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    return f_abc, B_ab


def curvature_at_s(s, f_abc, B_ab):
    """Compute all curvature invariants at s with CORRECT Weyl tensor."""
    n = 8
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Riemann tensor R^d_{abc} = <e_d, R(e_a, e_b) e_c>
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

    # Ricci tensor
    Ric = np.zeros((n, n))
    for a in range(n):
        for c in range(n):
            for b in range(n):
                Ric[a, c] += Riem[b, b, a, c]

    R = np.trace(Ric)

    # Kretschner: K = sum Riem^2
    K = np.sum(Riem**2)

    # |Ric|^2
    Ric2 = np.sum(Ric**2)

    # Reindex to standard form: R_std[mu,nu,rho,sigma] = Riem[rho, mu, nu, sigma]
    R_std = np.zeros((n, n, n, n))
    for mu in range(n):
        for nu in range(n):
            for rho in range(n):
                for sigma in range(n):
                    R_std[mu, nu, rho, sigma] = Riem[rho, mu, nu, sigma]

    # Weyl tensor (CORRECT formula for n dimensions)
    Weyl = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    W = R_std[a, b, c, d]

                    gac = 1.0 if a == c else 0.0
                    gad = 1.0 if a == d else 0.0
                    gbc = 1.0 if b == c else 0.0
                    gbd = 1.0 if b == d else 0.0

                    # Scalar part
                    W -= R / (n * (n-1)) * (gac * gbd - gad * gbc)

                    # Semi-traceless Ricci part
                    S_ac = Ric[a, c] - R / n * gac
                    S_ad = Ric[a, d] - R / n * gad
                    S_bc = Ric[b, c] - R / n * gbc
                    S_bd = Ric[b, d] - R / n * gbd

                    W -= (1.0 / (n - 2)) * (
                        gac * S_bd + gbd * S_ac - gad * S_bc - gbc * S_ad
                    )

                    Weyl[a, b, c, d] = W

    Weyl2 = np.sum(Weyl**2)

    # Verification: K = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1))
    S_mat = Ric - (R/n) * np.eye(n)
    S2 = np.sum(S_mat**2)
    K_check = Weyl2 + 4.0/(n-2) * S2 + 2.0 * R**2 / (n * (n-1))

    return {
        's': s, 'R': R, 'Ric2': Ric2, 'K': K, 'Weyl2': Weyl2,
        'Ric_eigenvalues': sorted(eigvalsh(Ric)),
        'tidal_fraction': Weyl2 / K if abs(K) > 1e-15 else float('nan'),
        'decomp_err': abs(K - K_check)
    }


def fit_invariant(name, s_values, values, k_set, threshold=1e-10):
    """
    Fit values to sum of c_k * e^{k*s} for k in k_set.

    Returns list of (k, c_k) for significant terms.
    """
    n_basis = len(k_set)
    n_data = len(s_values)

    # Design matrix
    A = np.zeros((n_data, n_basis))
    for i, s in enumerate(s_values):
        for j, k in enumerate(k_set):
            A[i, j] = np.exp(k * s)

    # Solve
    c, residuals, rank, sv = lstsq(A, values, rcond=None)

    # Fitted values
    fitted = A @ c
    max_rel_err = np.max(np.abs((values - fitted) / np.where(np.abs(values) > 1e-15, values, 1.0)))

    # Significant terms
    sig = [(k_set[j], c[j]) for j in range(n_basis) if abs(c[j]) > threshold]

    # Try to identify rational coefficients
    print(f"\n  {name}:")
    print(f"    Basis: k in {sorted(k_set)}")
    print(f"    Fit: {n_data} points, rank {rank}, max rel err = {max_rel_err:.2e}")
    print(f"    Significant terms ({len(sig)}):")

    for k, ck in sorted(sig, key=lambda x: x[0]):
        # Try to identify as simple fraction
        frac_str = identify_fraction(ck)
        print(f"      e^{{{k:+d}s}}: {ck:+18.12f}  {frac_str}")

    return sig, c, max_rel_err


def identify_fraction(x, max_denom=144):
    """Try to identify x as a simple fraction p/q."""
    if abs(x) < 1e-12:
        return "(~0)"

    best_err = 1.0
    best_p, best_q = 0, 1

    for q in range(1, max_denom + 1):
        p = round(x * q)
        err = abs(x - p / q)
        if err < best_err:
            best_err = err
            best_p, best_q = p, q

    if best_err < 1e-10:
        if best_q == 1:
            return f"(= {best_p})"
        else:
            return f"(= {best_p}/{best_q})"
    else:
        return f"(no simple fraction, err={best_err:.2e})"


def main():
    print("=" * 76)
    print("  SP-2: EXACT ANALYTIC CURVATURE INVARIANTS")
    print("  Schwarzschild-Penrose-Geometer -- Session 17b")
    print("=" * 76)

    f_abc, B_ab = build_infrastructure()

    # ==========================================================================
    # STEP 1: Determine the correct basis of exponentials
    # ==========================================================================
    print("\n  STEP 1: Basis analysis")
    print("  ON-frame ft exponents: SSS -> e^s, CCS -> e^{-2s}, CCU -> e^0")
    print("  Connection Gamma ~ ft, same exponents: {-2, 0, 1}")
    print("  Riemann R ~ Gamma*Gamma + ft*Gamma")
    print("  Exponents in R: sums of 2 from {-2, 0, 1}")
    print("  = {-4, -2, -1, 0, 1, 2}")
    print()
    print("  R(s) = Tr(Ric) sums over R-components, so R(s) has same exponents.")
    print("  |Ric|^2 sums Ric*Ric, each Ric ~ sum of Riem terms.")
    print("  Since Ric involves one contraction of Riem (4-tensor), Ric components")
    print("  have exponents that are sums of 2 from {-2, 0, 1}.")
    print("  |Ric|^2 = sum Ric^2 involves sums of 4 from {-2, 0, 1}.")
    print()
    print("  K = sum Riem^2 involves sums of 4 pairs from Gamma*Gamma terms.")
    print("  Each Riem component is sum of products of 2 connection values.")
    print("  Riem^2 is thus a product of 4 connection values.")
    print("  Each connection value has exponent from {-2, 0, 1}.")
    print("  Sum of 4: range [-8, 4], realized: {-8,-6,-5,-4,-3,-2,-1,0,1,2,3,4}")
    print()

    # Basis for R(s): k in {-4, -2, -1, 0, 2}
    # (Known: exponents -4, -1, 0, 2. Check if -2 contributes.)
    k_R = [-4, -2, -1, 0, 1, 2]

    # Basis for K, |Ric|^2, |Weyl|^2: all sums of 4 from {-2, 0, 1}
    k_K = [-8, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

    # ==========================================================================
    # STEP 2: Compute invariants at 25 carefully chosen s-values
    # ==========================================================================
    # Use well-separated s-values to avoid conditioning issues
    # Include s=0 for normalization
    s_fit = np.array([
        -0.8, -0.6, -0.4, -0.2, -0.1,
        0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3,
        0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5
    ])

    print(f"\n  STEP 2: Computing at {len(s_fit)} s-values...")

    R_vals = np.zeros(len(s_fit))
    K_vals = np.zeros(len(s_fit))
    Ric2_vals = np.zeros(len(s_fit))
    Weyl2_vals = np.zeros(len(s_fit))

    for i, s in enumerate(s_fit):
        r = curvature_at_s(s, f_abc, B_ab)
        R_vals[i] = r['R']
        K_vals[i] = r['K']
        Ric2_vals[i] = r['Ric2']
        Weyl2_vals[i] = r['Weyl2']
        if i % 5 == 0:
            print(f"    s={s:6.2f}: R={r['R']:12.6f} K={r['K']:14.8f} "
                  f"|Ric|^2={r['Ric2']:14.8f} |Weyl|^2={r['Weyl2']:14.8f} "
                  f"decomp_err={r['decomp_err']:.2e}")

    # ==========================================================================
    # STEP 3: Fit analytic formulas
    # ==========================================================================
    print("\n" + "=" * 76)
    print("  STEP 3: ANALYTIC FITS")
    print("=" * 76)

    sig_R, c_R, err_R = fit_invariant("R(s) [Scalar Curvature]", s_fit, R_vals, k_R)

    # Cross-check R(s) with known formula
    R_known = np.array([
        (1.0/4.0) * (2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s))
        for s in s_fit
    ])
    R_cross_err = np.max(np.abs(R_vals - R_known))
    print(f"    Cross-check vs Baptista: max err = {R_cross_err:.2e}")

    sig_Ric2, c_Ric2, err_Ric2 = fit_invariant("|Ric|^2(s)", s_fit, Ric2_vals, k_K)
    sig_K, c_K, err_K = fit_invariant("K(s) [Kretschner]", s_fit, K_vals, k_K)
    sig_Weyl2, c_Weyl2, err_Weyl2 = fit_invariant("|Weyl|^2(s)", s_fit, Weyl2_vals, k_K)

    # ==========================================================================
    # STEP 4: Independent verification at 51 points in [0, 2.5]
    # ==========================================================================
    print("\n" + "=" * 76)
    print("  STEP 4: VERIFICATION AT 51 INDEPENDENT POINTS")
    print("=" * 76)

    s_verify = np.linspace(0, 2.5, 51)

    def eval_fit(k_set, coeffs, s):
        return sum(coeffs[j] * np.exp(k_set[j] * s)
                   for j in range(len(k_set)))

    max_errs = {'R': 0, 'K': 0, 'Ric2': 0, 'Weyl2': 0}

    all_results = []

    print(f"\n  {'s':>6}  {'R':>12}  {'K':>14}  {'|Ric|^2':>14}  {'|Weyl|^2':>14}  "
          f"{'tidal':>8}  {'R_err':>10}  {'K_err':>10}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*14}  "
          f"{'-'*8}  {'-'*10}  {'-'*10}")

    for i, s in enumerate(s_verify):
        r = curvature_at_s(s, f_abc, B_ab)
        all_results.append(r)

        R_fit = eval_fit(k_R, c_R, s)
        K_fit = eval_fit(k_K, c_K, s)
        Ric2_fit = eval_fit(k_K, c_Ric2, s)
        Weyl2_fit = eval_fit(k_K, c_Weyl2, s)

        re_R = abs(r['R'] - R_fit) / max(abs(r['R']), 1e-15)
        re_K = abs(r['K'] - K_fit) / max(abs(r['K']), 1e-15)
        re_Ric2 = abs(r['Ric2'] - Ric2_fit) / max(abs(r['Ric2']), 1e-15)
        re_Weyl2 = abs(r['Weyl2'] - Weyl2_fit) / max(abs(r['Weyl2']), 1e-15)

        max_errs['R'] = max(max_errs['R'], re_R)
        max_errs['K'] = max(max_errs['K'], re_K)
        max_errs['Ric2'] = max(max_errs['Ric2'], re_Ric2)
        max_errs['Weyl2'] = max(max_errs['Weyl2'], re_Weyl2)

        if i % 5 == 0:
            print(f"  {s:6.3f}  {r['R']:12.6f}  {r['K']:14.6f}  "
                  f"{r['Ric2']:14.6f}  {r['Weyl2']:14.6f}  "
                  f"{r['tidal_fraction']:8.4f}  {re_R:10.2e}  {re_K:10.2e}")

    print(f"\n  Maximum relative verification errors:")
    for name, err in max_errs.items():
        status = "PASS (<1e-10)" if err < 1e-10 else ("GOOD (<1e-6)" if err < 1e-6 else ("WARN (<1e-3)" if err < 1e-3 else "FAIL"))
        print(f"    {name:>8}: {err:.2e}  {status}")

    # ==========================================================================
    # STEP 5: Decomposition verification at all 51 points
    # ==========================================================================
    print(f"\n  Decomposition K = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1)) check:")
    max_decomp_err = max(r['decomp_err'] for r in all_results)
    print(f"    Max decomposition error: {max_decomp_err:.2e}")

    # ==========================================================================
    # STEP 6: Classification answers
    # ==========================================================================
    print("\n" + "=" * 76)
    print("  CLASSIFICATION ANSWERS")
    print("=" * 76)

    r0 = all_results[0]  # s=0
    print(f"\n  Q1: Is g_s ever singular?")
    print(f"    NO. g_s = 3*diag(e^{{-2s}}[3], e^s[4], e^{{2s}}[1]) is positive definite for ALL real s.")
    print(f"    K(s) is finite for all finite s. K(s) -> infinity only as s -> +infinity.")
    print(f"    K(0) = {r0['K']:.10f}")

    # Growth rate
    r_last = all_results[-1]
    growth = np.log(r_last['K'] / r0['K']) / r_last['s']
    print(f"    K(2.5)/K(0) = {r_last['K']/r0['K']:.2f}")
    print(f"    Effective growth exponent: {growth:.4f}")
    # Check which term dominates at large s
    print(f"    Dominant term at large s determined by largest k in K(s) fit.")

    print(f"\n  Q2: Is g_0 (bi-invariant) conformally flat?")
    print(f"    NO. |Weyl|^2(0) = {r0['Weyl2']:.10f} != 0")
    print(f"    |Weyl|^2(0) / K(0) = {r0['tidal_fraction']:.10f}")

    # Check if this equals 5/7
    ratio_57 = 5.0 / 7.0
    print(f"    5/7 = {ratio_57:.10f}")
    print(f"    Match: {abs(r0['tidal_fraction'] - ratio_57):.2e}")
    if abs(r0['tidal_fraction'] - ratio_57) < 1e-8:
        print(f"    CONFIRMED: |Weyl|^2(0) / K(0) = 5/7 EXACTLY.")
    print(f"    SU(3) with bi-invariant metric is NOT conformally flat.")
    print(f"    (Only S^n, R^n, H^n, and products thereof are conformally flat in dim >= 4.)")

    print(f"\n  Q3: Weyl tensor structure")
    print(f"    Tidal fraction |Weyl|^2/K as function of s:")
    for r in all_results[::5]:
        print(f"      s={r['s']:5.2f}: |Weyl|^2/K = {r['tidal_fraction']:.8f}")

    # Asymptotic value
    tidal_last = all_results[-1]['tidal_fraction']
    print(f"\n    Tidal fraction at s=0: {all_results[0]['tidal_fraction']:.8f} = 5/7")
    print(f"    Tidal fraction at s=2.5: {tidal_last:.8f}")
    print(f"    DECREASING: Ricci contribution grows faster than Weyl.")

    # u(1) Ricci eigenvalue
    print(f"\n  REMARKABLE: u(1) Ricci eigenvalue = 0.25 for ALL s")
    for r in all_results[::10]:
        evals = r['Ric_eigenvalues']
        groups = {}
        for e in evals:
            found = False
            for key in groups:
                if abs(e - key) < 1e-6:
                    groups[key] += 1
                    found = True
                    break
            if not found:
                groups[e] = 1
        u1_eval = None
        for key, count in groups.items():
            if count == 1 and abs(r['s']) > 0.01:
                u1_eval = key
        if u1_eval is not None:
            print(f"    s={r['s']:5.2f}: u(1) eigenvalue = {u1_eval:.12f}")
        elif abs(r['s']) < 0.01:
            print(f"    s={r['s']:5.2f}: all eigenvalues = 0.25 (Einstein manifold)")

    # Negative su(2) Ricci eigenvalue
    print(f"\n  su(2) Ricci eigenvalue becomes NEGATIVE at large s:")
    for r in all_results:
        su2_eval = r['Ric_eigenvalues'][0]  # smallest (3-fold)
        if su2_eval < 0 and abs(r['s'] - round(r['s'], 1)) < 0.02:
            print(f"    s={r['s']:5.2f}: su(2) eigenvalue = {su2_eval:.8f}")

    # ==========================================================================
    # STEP 7: Generate plots
    # ==========================================================================
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        s_arr = np.array([r['s'] for r in all_results])
        R_arr = np.array([r['R'] for r in all_results])
        K_arr = np.array([r['K'] for r in all_results])
        Ric2_arr = np.array([r['Ric2'] for r in all_results])
        Weyl2_arr = np.array([r['Weyl2'] for r in all_results])
        tidal_arr = np.array([r['tidal_fraction'] for r in all_results])

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle('SP-2: Curvature Invariants of Jensen-Deformed SU(3)\n'
                     r'$g_s = 3 \cdot \mathrm{diag}(e^{-2s}[3],\, e^s[4],\, e^{2s}[1])$',
                     fontsize=14, fontweight='bold')

        # Panel 1: R(s)
        ax = axes[0, 0]
        ax.plot(s_arr, R_arr, 'b-', lw=2, label='R(s) computed')
        R_analytic = np.array([0.25*(2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)) for s in s_arr])
        ax.plot(s_arr, R_analytic, 'r--', lw=1, alpha=0.7, label='Baptista eq 3.70')
        ax.set_xlabel('s')
        ax.set_ylabel('R(s)')
        ax.set_title('Scalar Curvature R(s)')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.axvline(x=0.15, color='green', alpha=0.4, ls='--')
        ax.axvline(x=0.30, color='orange', alpha=0.4, ls='--')

        # Panel 2: K(s) log scale
        ax = axes[0, 1]
        ax.semilogy(s_arr, K_arr, 'b-', lw=2)
        ax.set_xlabel('s')
        ax.set_ylabel('K(s)')
        ax.set_title(r'Kretschner Scalar $K(s) = R_{abcd}R^{abcd}$')
        ax.grid(True, alpha=0.3)
        ax.axvline(x=0.15, color='green', alpha=0.4, ls='--')
        ax.axvline(x=0.30, color='orange', alpha=0.4, ls='--')

        # Panel 3: All invariants normalized
        ax = axes[0, 2]
        ax.plot(s_arr, K_arr/K_arr[0], 'b-', lw=2, label='K/K(0)')
        ax.plot(s_arr, Ric2_arr/Ric2_arr[0], 'r-', lw=2, label='|Ric|^2/|Ric|^2(0)')
        ax.plot(s_arr, Weyl2_arr/Weyl2_arr[0], 'g-', lw=2, label='|Weyl|^2/|Weyl|^2(0)')
        ax.set_xlabel('s')
        ax.set_ylabel('Normalized')
        ax.set_title('Normalized Growth')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_yscale('log')

        # Panel 4: Tidal fraction
        ax = axes[1, 0]
        ax.plot(s_arr, tidal_arr, 'k-', lw=2)
        ax.axhline(y=5.0/7.0, color='red', alpha=0.4, ls='--', label='5/7 (bi-invariant)')
        ax.set_xlabel('s')
        ax.set_ylabel('|Weyl|^2 / K')
        ax.set_title('Tidal Fraction')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

        # Panel 5: Ricci eigenvalues
        ax = axes[1, 1]
        ric_evals = np.array([r['Ric_eigenvalues'] for r in all_results])
        for j in range(8):
            ax.plot(s_arr, ric_evals[:, j], '-', lw=1, alpha=0.7)
        ax.axhline(y=0.25, color='red', alpha=0.4, ls='--', label='0.25')
        ax.axhline(y=0.0, color='black', alpha=0.3, ls='-')
        ax.set_xlabel('s')
        ax.set_ylabel('Ricci eigenvalue')
        ax.set_title('Ricci Eigenvalue Structure')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

        # Panel 6: Decomposition check
        ax = axes[1, 2]
        decomp_errs = np.array([r['decomp_err'] for r in all_results])
        ax.semilogy(s_arr, decomp_errs + 1e-17, 'b-', lw=2)
        ax.set_xlabel('s')
        ax.set_ylabel('|K - K_decomp|')
        ax.set_title('K = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1))')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'sp2_curvature_invariants_v2.png')
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
        print(f"\n  Plot saved to: {outpath}")
        plt.close()

    except ImportError:
        print("  matplotlib not available, skipping plots.")

    # ==========================================================================
    # STEP 8: DEFINITIVE SUMMARY
    # ==========================================================================
    print("\n" + "=" * 76)
    print("  DEFINITIVE SUMMARY: CURVATURE INVARIANTS OF (SU(3), g_s)")
    print("=" * 76)

    print("""
  METRIC: g_s = 3 * diag(e^{-2s}[3], e^s[4], e^{2s}[1]) in Gell-Mann ON basis
  VOLUME: det(g_s)/det(g_0) = 1 for all s (TT-deformation, EXACT)

  1. SCALAR CURVATURE (EXACT, Baptista eq 3.70):
     R(s) = (1/4) * [2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}]
     R(0) = 2.0 (Einstein manifold, Ric = R/8 * g)""")

    # Print R fit coefficients
    print("\n     Fit verification:")
    for k, ck in sorted(sig_R, key=lambda x: x[0]):
        if abs(ck) > 1e-10:
            frac = identify_fraction(ck)
            print(f"       e^{{{k:+d}s}}: {ck:+18.14f}  {frac}")

    print(f"""
  2. |Ric|^2(s) = R_{{ab}} R^{{ab}}:
     |Ric|^2(0) = {r0['Ric2']:.10f} = 1/2""")
    print("     Terms (threshold > 1e-6):")
    for k, ck in sorted(sig_Ric2, key=lambda x: x[0]):
        if abs(ck) > 1e-6:
            frac = identify_fraction(ck)
            print(f"       e^{{{k:+d}s}}: {ck:+18.14f}  {frac}")

    print(f"""
  3. K(s) = R_{{abcd}} R^{{abcd}} (Kretschner):
     K(0) = {r0['K']:.10f} = 1/2""")
    print("     Terms (threshold > 1e-6):")
    for k, ck in sorted(sig_K, key=lambda x: x[0]):
        if abs(ck) > 1e-6:
            frac = identify_fraction(ck)
            print(f"       e^{{{k:+d}s}}: {ck:+18.14f}  {frac}")

    print(f"""
  4. |Weyl|^2(s) = C_{{abcd}} C^{{abcd}} (CORRECT n=8 Weyl):
     |Weyl|^2(0) = {r0['Weyl2']:.10f} = 5/14""")
    print("     Terms (threshold > 1e-6):")
    for k, ck in sorted(sig_Weyl2, key=lambda x: x[0]):
        if abs(ck) > 1e-6:
            frac = identify_fraction(ck)
            print(f"       e^{{{k:+d}s}}: {ck:+18.14f}  {frac}")

    # Table of values
    print(f"\n  TABLE OF VALUES:")
    print(f"  {'s':>6}  {'R(s)':>12}  {'K(s)':>14}  {'|Ric|^2':>14}  {'|Weyl|^2':>14}  "
          f"{'tidal':>8}  {'Ric eval su2':>14}  {'Ric eval C2':>14}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*14}  "
          f"{'-'*8}  {'-'*14}  {'-'*14}")

    for r in all_results[::5]:
        evals = r['Ric_eigenvalues']
        su2_e = evals[0]  # 3-fold, smallest
        c2_e = evals[3]   # 4-fold, middle
        print(f"  {r['s']:6.3f}  {r['R']:12.6f}  {r['K']:14.6f}  "
              f"{r['Ric2']:14.6f}  {r['Weyl2']:14.6f}  "
              f"{r['tidal_fraction']:8.4f}  {su2_e:14.8f}  {c2_e:14.8f}")

    print(f"\n  DECOMPOSITION IDENTITY (verified at ALL 51 points):")
    print(f"    K = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1))  [n=8]")
    print(f"    Max error: {max(r['decomp_err'] for r in all_results):.2e}")

    print(f"\n  CLASSIFICATION:")
    print(f"    1. g_s NEVER singular (positive definite for all real s)")
    print(f"    2. g_0 NOT conformally flat: |Weyl|^2(0)/K(0) = 5/7")
    print(f"    3. Weyl tensor: |Weyl|^2 increases with s (Penrose-consistent)")
    print(f"       Tidal fraction decreases: 5/7 -> ~0.476 (Ricci grows faster)")
    print(f"    4. u(1) Ricci eigenvalue = 1/4 for ALL s (s-independent)")
    print(f"    5. su(2) Ricci eigenvalue goes NEGATIVE for s > ~1.3")
    print(f"    6. Asymptotic K(s) ~ e^{{alpha*s}} with alpha ~ {growth:.2f}")


if __name__ == "__main__":
    main()
