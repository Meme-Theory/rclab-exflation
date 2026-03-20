"""
SP-2 Refinement: Determine EXACT rational coefficients for curvature invariants.

Strategy: Use the known significant exponents from the initial fit, restrict
the basis to only those terms, and solve with high-precision s-values.
Then test all candidate fractions with denominator <= 144.
"""

import numpy as np
from numpy.linalg import lstsq, eigvalsh
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
    """Compute curvature invariants with correct Weyl tensor."""
    n = 8
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

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

    Ric = np.zeros((n, n))
    for a in range(n):
        for c in range(n):
            for b in range(n):
                Ric[a, c] += Riem[b, b, a, c]

    R = np.trace(Ric)
    K = np.sum(Riem**2)
    Ric2 = np.sum(Ric**2)

    # Reindex + Weyl
    R_std = np.zeros((n, n, n, n))
    for mu in range(n):
        for nu in range(n):
            for rho in range(n):
                for sigma in range(n):
                    R_std[mu, nu, rho, sigma] = Riem[rho, mu, nu, sigma]

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
                    W -= R / (n * (n-1)) * (gac * gbd - gad * gbc)
                    S_ac = Ric[a, c] - R / n * gac
                    S_ad = Ric[a, d] - R / n * gad
                    S_bc = Ric[b, c] - R / n * gbc
                    S_bd = Ric[b, d] - R / n * gbd
                    W -= (1.0 / (n - 2)) * (
                        gac * S_bd + gbd * S_ac - gad * S_bc - gbc * S_ad)
                    Weyl[a, b, c, d] = W

    Weyl2 = np.sum(Weyl**2)
    return R, Ric2, K, Weyl2


def identify_fraction(x, max_denom=504):
    """Try to identify x as a simple fraction p/q with q <= max_denom."""
    if abs(x) < 1e-12:
        return 0, 1, 0.0

    best_err = 1.0
    best_p, best_q = 0, 1

    for q in range(1, max_denom + 1):
        p = round(x * q)
        err = abs(x - p / q)
        if err < best_err:
            best_err = err
            best_p, best_q = p, q

    return best_p, best_q, best_err


def main():
    print("=" * 76)
    print("  SP-2 REFINEMENT: EXACT RATIONAL COEFFICIENTS")
    print("=" * 76)

    f_abc, B_ab = build_infrastructure()

    # Compute at many s-values for a well-conditioned system
    # Use rational s-values to maximize numerical conditioning
    s_vals = np.array([
        0.01, 0.02, 0.03, 0.05, 0.07,
        0.10, 0.13, 0.17, 0.21, 0.25,
        0.30, 0.37, 0.45, 0.55, 0.67,
        0.80, 0.95, 1.10, 1.30, 1.50,
        1.75, 2.00, 2.30, 2.60, 3.00
    ])

    n_pts = len(s_vals)
    R_vals = np.zeros(n_pts)
    Ric2_vals = np.zeros(n_pts)
    K_vals = np.zeros(n_pts)
    Weyl2_vals = np.zeros(n_pts)

    print(f"\n  Computing at {n_pts} s-values...")
    for i, s in enumerate(s_vals):
        R_vals[i], Ric2_vals[i], K_vals[i], Weyl2_vals[i] = curvature_at_s(s, f_abc, B_ab)

    # === |Ric|^2: Significant exponents = {-8, -5, -4, -2, -1, 0, 4} ===
    k_Ric2 = [-8, -5, -4, -2, -1, 0, 4]
    A_Ric2 = np.zeros((n_pts, len(k_Ric2)))
    for i, s in enumerate(s_vals):
        for j, k in enumerate(k_Ric2):
            A_Ric2[i, j] = np.exp(k * s)

    c_Ric2, _, _, _ = lstsq(A_Ric2, Ric2_vals, rcond=None)

    print("\n  |Ric|^2(s) coefficients:")
    for j, k in enumerate(k_Ric2):
        p, q, err = identify_fraction(c_Ric2[j])
        print(f"    e^{{{k:+d}s}}: {c_Ric2[j]:+22.16f}  = {p}/{q} (err={err:.2e})")

    # Verify
    Ric2_fit = A_Ric2 @ c_Ric2
    max_err_Ric2 = np.max(np.abs(Ric2_vals - Ric2_fit) / np.maximum(np.abs(Ric2_vals), 1e-15))
    print(f"    Max rel err: {max_err_Ric2:.2e}")

    # === K: Significant exponents = {-8, -5, -4, -2, -1, 0, 4} ===
    k_K = [-8, -5, -4, -2, -1, 0, 4]
    A_K = np.zeros((n_pts, len(k_K)))
    for i, s in enumerate(s_vals):
        for j, k in enumerate(k_K):
            A_K[i, j] = np.exp(k * s)

    c_K, _, _, _ = lstsq(A_K, K_vals, rcond=None)

    print("\n  K(s) coefficients:")
    for j, k in enumerate(k_K):
        p, q, err = identify_fraction(c_K[j])
        print(f"    e^{{{k:+d}s}}: {c_K[j]:+22.16f}  = {p}/{q} (err={err:.2e})")

    K_fit = A_K @ c_K
    max_err_K = np.max(np.abs(K_vals - K_fit) / np.maximum(np.abs(K_vals), 1e-15))
    print(f"    Max rel err: {max_err_K:.2e}")

    # === |Weyl|^2: Significant exponents = {-8, -5, -4, -2, -1, 0, 1, 2, 4} ===
    k_W2 = [-8, -5, -4, -2, -1, 0, 1, 2, 4]
    A_W2 = np.zeros((n_pts, len(k_W2)))
    for i, s in enumerate(s_vals):
        for j, k in enumerate(k_W2):
            A_W2[i, j] = np.exp(k * s)

    c_W2, _, _, _ = lstsq(A_W2, Weyl2_vals, rcond=None)

    print("\n  |Weyl|^2(s) coefficients:")
    for j, k in enumerate(k_W2):
        p, q, err = identify_fraction(c_W2[j])
        print(f"    e^{{{k:+d}s}}: {c_W2[j]:+22.16f}  = {p}/{q} (err={err:.2e})")

    W2_fit = A_W2 @ c_W2
    max_err_W2 = np.max(np.abs(Weyl2_vals - W2_fit) / np.maximum(np.abs(Weyl2_vals), 1e-15))
    print(f"    Max rel err: {max_err_W2:.2e}")

    # === CROSS-CHECK: Does |Ric|^2 - K give |Weyl|^2? ===
    # K = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1))
    # |S|^2 = |Ric|^2 - R^2/n
    # So |C|^2 = K - 4/(n-2)(|Ric|^2 - R^2/n) - 2R^2/(n(n-1))
    n = 8
    print("\n  CROSS-CHECK: |Weyl|^2 from decomposition")
    for i, s in enumerate(s_vals[:5]):
        R = R_vals[i]
        S2 = Ric2_vals[i] - R**2 / n
        W2_check = K_vals[i] - 4.0/(n-2) * S2 - 2.0 * R**2 / (n * (n-1))
        err = abs(W2_check - Weyl2_vals[i])
        print(f"    s={s:.2f}: |Weyl|^2_direct={Weyl2_vals[i]:.12f} "
              f"|Weyl|^2_decomp={W2_check:.12f} err={err:.2e}")

    # === INDEPENDENT VERIFICATION AT 51 POINTS ===
    print("\n" + "=" * 76)
    print("  INDEPENDENT VERIFICATION AT 51 POINTS")
    print("=" * 76)

    s_verify = np.linspace(0, 2.5, 51)

    def eval_Ric2(s):
        return sum(c_Ric2[j] * np.exp(k_Ric2[j] * s) for j in range(len(k_Ric2)))

    def eval_K(s):
        return sum(c_K[j] * np.exp(k_K[j] * s) for j in range(len(k_K)))

    def eval_W2(s):
        return sum(c_W2[j] * np.exp(k_W2[j] * s) for j in range(len(k_W2)))

    max_errs = {'Ric2': 0, 'K': 0, 'Weyl2': 0}

    for s in s_verify:
        R, Ric2, K, Weyl2 = curvature_at_s(s, f_abc, B_ab)

        e_Ric2 = abs(Ric2 - eval_Ric2(s)) / max(abs(Ric2), 1e-15)
        e_K = abs(K - eval_K(s)) / max(abs(K), 1e-15)
        e_W2 = abs(Weyl2 - eval_W2(s)) / max(abs(Weyl2), 1e-15)

        max_errs['Ric2'] = max(max_errs['Ric2'], e_Ric2)
        max_errs['K'] = max(max_errs['K'], e_K)
        max_errs['Weyl2'] = max(max_errs['Weyl2'], e_W2)

    print(f"\n  Max relative errors (fit vs direct computation):")
    for name, err in max_errs.items():
        status = "MACHINE EPSILON" if err < 1e-12 else ("GOOD" if err < 1e-8 else "WARN")
        print(f"    {name:>8}: {err:.2e}  {status}")

    # === TRY SMALLER DENOMINATOR SEARCH WITH CLEANED COEFFICIENTS ===
    print("\n" + "=" * 76)
    print("  FRACTION IDENTIFICATION (max denominator 504)")
    print("=" * 76)

    for name, k_set, coeffs in [
        ("|Ric|^2", k_Ric2, c_Ric2),
        ("K", k_K, c_K),
        ("|Weyl|^2", k_W2, c_W2)
    ]:
        print(f"\n  {name}(s) = ")
        total_at_0 = 0.0
        for j, k in enumerate(k_set):
            p, q, err = identify_fraction(coeffs[j])
            total_at_0 += p / q
            if err < 1e-8:
                print(f"    + ({p}/{q}) * e^{{{k}s}}", end="")
                if q == 1:
                    print(f"     [{coeffs[j]:+.16f}]")
                else:
                    print(f"     [{coeffs[j]:+.16f}, exact={p/q:+.16f}]")
            else:
                print(f"    + ({coeffs[j]:+.16f}) * e^{{{k}s}}  [NO FRACTION FOUND, err={err:.2e}]")
        p0, q0, e0 = identify_fraction(total_at_0)
        print(f"    Value at s=0: {total_at_0:.16f} = {p0}/{q0} (err={e0:.2e})")


if __name__ == "__main__":
    main()
