"""
SP-2 Debug: Fix Weyl tensor decomposition and derive TRUE analytic forms.
"""

import numpy as np
from numpy.linalg import inv, eigvalsh
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


def full_curvature_at_s(s, f_abc, B_ab):
    """Compute full Riemann tensor + all contractions with careful index conventions."""
    n = 8
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Riemann tensor R^d_{abc}
    # Convention: R(e_a, e_b)e_c = R^d_{abc} e_d
    # In ON frame: R_{dabc} = R^d_{abc} (trivial lowering)
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

    # Verify Riemann symmetries
    # R_{dabc} should satisfy:
    # 1) R_{dabc} = -R_{dbac} (antisymmetry in (a,b))
    # 2) R_{dabc} = -R_{adbc} (antisymmetry in (d,c)??) -- NO, this is wrong for R^d_{abc}

    # Actually for R_{dabc} (all indices down, ON frame):
    # We need R_{dabc} = R^d_{abc} -- but this is the Riemann tensor with
    # first index up. Let me compute the fully lowered version:
    # R_{dabf} = delta_{de} R^e_{abf} = R^d_{abf} (trivial in ON frame)
    #
    # Standard Riemann symmetries for R_{dabc}:
    # (i)   R_{dabc} = -R_{adbc}  (antisymmetry in first pair)  -- WAIT, this is R_{dcba}
    #
    # Let me be very careful. The Riemann tensor convention I'm using:
    # R^d_{abc}: indices are (upper, lower, lower, lower)
    # The standard Riemann tensor R^d_{cab} in most GR texts is:
    #   R^d_{cab} = partial_c Gamma^d_{ab} - partial_a Gamma^d_{cb} + ...
    # But for left-invariant fields, partial = 0, and we have:
    #   R^d_{abc} = Gamma^d_{ae} Gamma^e_{bc} - Gamma^d_{be} Gamma^e_{ac} - ft^e_{ab} Gamma^d_{ec}
    # This matches R(e_a, e_b)e_c = R^d_{abc} e_d.
    #
    # The fully lowered tensor: R_{fdbc} = delta_{fd} R^d_{abc} = R^f_{abc} (in ON frame)
    # Wait, NO. R_{fabc} = g_{fd} R^d_{abc} = delta_{fd} R^d_{abc} = R^f_{abc}.
    # So R_{fabc} = Riem[f, a, b, c].
    #
    # Standard symmetries of Riemann (MTW convention):
    # R_{abcd} = -R_{abdc} = -R_{bacd} = R_{cdab}
    # where (a,b) are the first pair and (c,d) are the second pair.
    #
    # In our notation R_{fabc}, the pairs are (f,a) and (b,c)?
    # NO -- our R_{dabc} = R(e_a, e_b)e_c projected onto e_d.
    # So the pairs are (a,b) as the "curvature" indices and (d,c) as "vector" indices.
    #
    # Standard: R_{μνρσ} with (μ,ν) antisymmetric and (ρ,σ) antisymmetric.
    # Our: R_{dabc} with a,b the curvature indices: R_{d,a,b,c} = <e_d, R(e_a, e_b) e_c>
    # So antisymmetry in (a,b): R_{dabc} = -R_{dbac} -- YES
    # And antisymmetry in (d,c): R_{dabc} = -R_{cabd} -- PAIR SYMMETRY
    # Actually: R_{dabc} = R_{bcda} (pair symmetry)

    # Let me just check:
    err_ab = 0.0  # R_{dabc} + R_{dbac} should be 0
    err_dc = 0.0  # R_{dabc} + R_{cabd} should be 0 (pair antisymmetry)
    err_pair = 0.0 # R_{dabc} - R_{bcda} should be 0 (pair symmetry)

    for d in range(n):
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    err_ab = max(err_ab, abs(Riem[d,a,b,c] + Riem[d,b,a,c]))
                    err_dc = max(err_dc, abs(Riem[d,a,b,c] + Riem[c,a,b,d]))
                    err_pair = max(err_pair, abs(Riem[d,a,b,c] - Riem[b,c,d,a]))

    print(f"  Riemann symmetry checks:")
    print(f"    R_{{dabc}} + R_{{dbac}} = 0 (antisym in a,b): max err = {err_ab:.2e}")
    print(f"    R_{{dabc}} + R_{{cabd}} = 0 (antisym in d,c): max err = {err_dc:.2e}")
    print(f"    R_{{dabc}} - R_{{bcda}} = 0 (pair symmetry):  max err = {err_pair:.2e}")

    # OK so Riem[d,a,b,c] is ANTISYMMETRIC in (a,b) but what about (d,c)?
    # R(X,Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_{[X,Y]} Z
    # <W, R(X,Y)Z> is antisymmetric in (X,Y) and also satisfies:
    # <W, R(X,Y)Z> = -<Z, R(X,Y)W>  (metric compatibility)
    # i.e., R_{dabc} = -R_{cabd}
    # Wait: <e_d, R(e_a, e_b) e_c> = -<e_c, R(e_a, e_b) e_d>
    # So R_{d,a,b,c} = -R_{c,a,b,d}
    # i.e., Riem[d,a,b,c] = -Riem[c,a,b,d]

    err_dc2 = 0.0
    for d in range(n):
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    err_dc2 = max(err_dc2, abs(Riem[d,a,b,c] + Riem[c,a,b,d]))
    print(f"    R_{{d,a,b,c}} + R_{{c,a,b,d}} = 0 (antisym in d,c): max err = {err_dc2:.2e}")

    # Ricci tensor: Ric(X,Z) = sum_b <e_b, R(e_b, X)Z> = sum_b R_{b,b,X,Z}
    # Ric_{ac} = sum_b Riem[b, b, a, c]
    Ric = np.zeros((n, n))
    for a in range(n):
        for c in range(n):
            for b in range(n):
                Ric[a, c] += Riem[b, b, a, c]

    R = np.trace(Ric)

    # Now the Kretschner scalar:
    # K = R_{abcd} R^{abcd} where we need all-lowered Riemann.
    # In our notation: Riem[d,a,b,c] = R_{d,a,b,c} = <e_d, R(e_a, e_b) e_c>
    # But the standard "all lowered" Riemann is R_{μνρσ} where the first pair
    # (μ,ν) and second pair (ρ,σ) are both antisymmetric.
    #
    # In our case: Riem[d,a,b,c] is antisymmetric in (a,b) [curvature indices]
    # and antisymmetric in (d,c) [metric compatibility].
    # So Riem IS the fully-lowered Riemann tensor with indices arranged as
    # R_{d,a,b,c} with (a,b) and (d,c) as the two antisymmetric pairs.
    #
    # Kretschner: K = sum_{d,a,b,c} Riem[d,a,b,c]^2
    K = np.sum(Riem**2)

    # Ricci squared
    Ric2 = np.sum(Ric**2)

    # WEYL TENSOR: In n dimensions, the decomposition of the Riemann tensor is:
    #
    # R_{abcd} = C_{abcd}
    #   + (2/(n-2)) (g_{a[c} S_{d]b} - g_{b[c} S_{d]a})
    #   + (2R/((n-1)(n-2))) g_{a[c} g_{d]b}
    #
    # where S_{ab} = Ric_{ab} - (R/n) g_{ab} is the traceless Ricci tensor.
    # WAIT, this is a different decomposition. Let me use the standard one.
    #
    # The standard decomposition of the Riemann tensor R_{abcd} (all down, with
    # (a,b) and (c,d) antisymmetric pairs) is:
    #
    # R_{abcd} = C_{abcd} + E_{abcd} + G_{abcd}
    #
    # where:
    # G_{abcd} = (R/(n(n-1))) * (g_{ac} g_{bd} - g_{ad} g_{bc})      [scalar part]
    # E_{abcd} = (1/(n-2)) * (g_{ac} S_{bd} + g_{bd} S_{ac} - g_{ad} S_{bc} - g_{bc} S_{ad})  [semi-traceless]
    # S_{ab} = Ric_{ab} - (R/n) g_{ab}  [traceless Ricci]
    # C_{abcd} = R_{abcd} - E_{abcd} - G_{abcd}  [Weyl, totally traceless]
    #
    # But our Riem[d,a,b,c] has different index order!
    # Our R_{d,a,b,c} with antisymmetric pairs (a,b) and (d,c).
    # Standard R_{a,b,c,d} with antisymmetric pairs (a,b) and (c,d).
    #
    # Mapping: our Riem[d,a,b,c] = R_{d,a,b,c}
    # Standard: R_{a,b,c,d} = our Riem[a,?,?,?]
    #
    # Actually, the pair structure of our tensor:
    # Riem[d,a,b,c] is antisym in (a,b) [positions 1,2] and in (d,c) [positions 0,3]
    #
    # To convert to standard form R_{μνρσ} with antisym in (μ,ν) and (ρ,σ):
    # R_{μνρσ} = Riem[ρ, μ, ν, σ]
    # Check: Riem[ρ,μ,ν,σ] is antisym in μ,ν (positions 1,2) ✓
    # Riem[ρ,μ,ν,σ] is antisym in ρ,σ (positions 0,3) ✓
    # So R_standard[μ,ν,ρ,σ] = Riem[ρ, μ, ν, σ]

    # Convert to standard index order
    R_std = np.zeros((n, n, n, n))
    for mu in range(n):
        for nu in range(n):
            for rho in range(n):
                for sigma in range(n):
                    R_std[mu, nu, rho, sigma] = Riem[rho, mu, nu, sigma]

    # Verify standard symmetries
    err1 = 0.0  # antisym in (μ,ν)
    err2 = 0.0  # antisym in (ρ,σ)
    err3 = 0.0  # pair symmetry R_{μνρσ} = R_{ρσμν}
    for mu in range(n):
        for nu in range(n):
            for rho in range(n):
                for sigma in range(n):
                    err1 = max(err1, abs(R_std[mu,nu,rho,sigma] + R_std[nu,mu,rho,sigma]))
                    err2 = max(err2, abs(R_std[mu,nu,rho,sigma] + R_std[mu,nu,sigma,rho]))
                    err3 = max(err3, abs(R_std[mu,nu,rho,sigma] - R_std[rho,sigma,mu,nu]))
    print(f"\n  Standard Riemann symmetries (reindexed):")
    print(f"    antisym (mu,nu): {err1:.2e}")
    print(f"    antisym (rho,sigma): {err2:.2e}")
    print(f"    pair symmetry: {err3:.2e}")

    # Kretschner check (should be same)
    K_std = np.sum(R_std**2)
    print(f"\n  K from original: {K:.10f}")
    print(f"  K from reindexed: {K_std:.10f}")
    print(f"  Difference: {abs(K - K_std):.2e}")

    # Now compute Weyl tensor in standard notation
    Weyl = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    W = R_std[a, b, c, d]

                    # g_{ac}, g_{bd} etc are all delta in ON frame
                    gac = 1.0 if a == c else 0.0
                    gad = 1.0 if a == d else 0.0
                    gbc = 1.0 if b == c else 0.0
                    gbd = 1.0 if b == d else 0.0

                    # Scalar part G_{abcd}
                    W -= R / (n * (n-1)) * (gac * gbd - gad * gbc)

                    # Semi-traceless part E_{abcd}
                    # S_{ab} = Ric_{ab} - R/n * g_{ab}
                    S_ac = Ric[a, c] - R / n * gac
                    S_ad = Ric[a, d] - R / n * gad
                    S_bc = Ric[b, c] - R / n * gbc
                    S_bd = Ric[b, d] - R / n * gbd

                    W -= (1.0 / (n - 2)) * (gac * S_bd + gbd * S_ac - gad * S_bc - gbc * S_ad)

                    Weyl[a, b, c, d] = W

    Weyl2 = np.sum(Weyl**2)

    # The decomposition identity should now hold:
    # |R|^2 = |C|^2 + |E|^2 + |G|^2
    # where these are orthogonal under the inner product sum R_{abcd}^2.
    #
    # |G|^2 = R^2 * sum (gac gbd - gad gbc)^2 / (n(n-1))^2
    # = R^2 * 2*n*(n-1) / (n(n-1))^2 = 2 R^2 / (n(n-1))
    #
    # |E|^2 is more complex. But the IDENTITY is:
    # K = |C|^2 + (4/(n-2)) |S|^2 + 2R^2/(n(n-1))
    # where |S|^2 = sum S_{ab}^2 = |Ric|^2 - R^2/n

    S_tensor = Ric - (R/n) * np.eye(n)
    S2 = np.sum(S_tensor**2)

    K_check = Weyl2 + 4.0/(n-2) * S2 + 2.0 * R**2 / (n * (n-1))

    print(f"\n  CORRECTED Weyl decomposition check at s={s:.2f}:")
    print(f"    K = {K:.10f}")
    print(f"    |C|^2 = {Weyl2:.10f}")
    print(f"    |S|^2 = {S2:.10f}")
    print(f"    K_check = |C|^2 + 4/(n-2)|S|^2 + 2R^2/(n(n-1)) = {K_check:.10f}")
    print(f"    Error: {abs(K - K_check):.2e}")

    # Also check the alternative form:
    # K = |C|^2 + 2/(n-2) * |Ric|^2 - R^2/((n-1)(n-2))
    # This follows from |S|^2 = |Ric|^2 - R^2/n and substituting.
    K_alt = Weyl2 + 2.0/(n-2) * Ric2 - R**2 / ((n-1) * (n-2))
    print(f"    K_alt = |C|^2 + 2/(n-2)|Ric|^2 - R^2/((n-1)(n-2)) = {K_alt:.10f}")
    print(f"    Error_alt: {abs(K - K_alt):.2e}")

    return {
        's': s, 'R': R, 'Ric2': Ric2, 'K': K, 'Weyl2': Weyl2,
        'Ric_eigenvalues': sorted(eigvalsh(Ric)),
        'tidal_fraction': Weyl2 / K if abs(K) > 1e-15 else float('nan')
    }


if __name__ == "__main__":
    f_abc, B_ab = build_infrastructure()

    print("=" * 70)
    print("  SP-2 DEBUG: Weyl tensor decomposition check")
    print("=" * 70)

    for s in [0.0, 0.5, 1.0, 2.0]:
        print(f"\n{'='*60}")
        print(f"  s = {s:.2f}")
        print(f"{'='*60}")
        result = full_curvature_at_s(s, f_abc, B_ab)
        print(f"\n  Summary: R={result['R']:.8f}, K={result['K']:.8f}, "
              f"|Ric|^2={result['Ric2']:.8f}, |Weyl|^2={result['Weyl2']:.8f}")
        print(f"  tidal = {result['tidal_fraction']:.8f}")
