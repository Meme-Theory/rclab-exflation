"""
R-1: FULL RIEMANN TENSOR R_{abcd}(tau) ON JENSEN-DEFORMED SU(3)
================================================================

Computes the complete 8x8x8x8 Riemann tensor on (SU(3), g_tau) with the
Jensen TT-deformation, for 21 tau-values in [0, 2.0].

This is the PREREQUISITE for Session 20b's Lichnerowicz computation on TT 2-tensors.
The Lichnerowicz operator Delta_L acts on symmetric 2-tensors h_{ab} as:

    (Delta_L h)_{ab} = (Delta h)_{ab} - 2 R_{acbd} h^{cd}

so we need R_{abcd} explicitly.

Mathematical structure:
    su(3) = u(1) + su(2) + C^2  (Baptista reductive decomposition)
    g_tau = e^{2tau} g_0|_{u(1)} + e^{-2tau} g_0|_{su(2)} + e^{tau} g_0|_{C^2}

On a Lie group with left-invariant metric, all Christoffel symbols are
constants, so the Riemann tensor is purely algebraic:

    R^d_{abc} = sum_e (Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be}
                       - ft^e_{ab} Gamma^d_{ec})

where ft^e_{ab} are the ON-frame structure constants.

Lowering: R_{abcd} = delta_{de} R^e_{abc}  (trivial in ON frame, delta = I).

Validation:
    (1) R_{abcd}|_{tau=0} = -(1/4) f_{abe} f^e_{cd}   (bi-invariant formula)
    (2) R_{ab} = R^c_{acb} must match ricci_tensor_ON()
    (3) g^{ab} R_{ab} must match SP-2 scalar curvature R(tau)
    (4) K(tau) = R_{abcd} R^{abcd} must match K_exact(tau) from SP-2

Author: Sim-Specialist Agent (Session 20a)
Date: 2026-02-19

References:
    - Baptista (2024), arXiv:2306.01049, eqs 3.58, 3.65-3.72
    - SP-2 verification: sp2_final_verification.py (validated at machine epsilon)
    - B-6 infrastructure: b6_scalar_vector_laplacian.py
"""

import numpy as np
from numpy.linalg import inv, cholesky, eigvalsh
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    validate_connection,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)


# =============================================================================
# MODULE 1: RIEMANN TENSOR COMPUTATION
# =============================================================================

def compute_riemann_tensor_ON(s: float) -> np.ndarray:
    """
    Compute the full 8x8x8x8 Riemann tensor R_{abcd}(s) in the ON frame.

    For a left-invariant metric on a Lie group, Christoffel symbols are
    position-independent constants, so the Riemann tensor formula simplifies to:

        R^d_{abc} = sum_e (Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be}
                           - ft^e_{ab} Gamma^d_{ec})

    where:
        Gamma[d,a,b] = Gamma^d_{ab}  (Levi-Civita connection in ON frame)
        ft[a,b,c]    = ft^c_{ab}     (ON-frame structure constants)

    The fully covariant tensor is obtained by lowering with g_{de} = delta_{de}
    in the ON frame (trivial):
        R_{abcd} = R^d_{abc}  (index ordering: R_{abcd} stores the component
                               with all indices down, where the 4th index = d)

    CONVENTION: R[a,b,c,d] = R_{abcd} where
        R_{abcd} = g_{de} R^e_{abc}
        = R evaluated on (e_a, e_b, e_c, e_d)
        with the 2nd pair (c,d) being the "slot" pair.

    Antisymmetry properties of the Riemann tensor:
        R_{abcd} = -R_{bacd}          (antisymmetric in first pair)
        R_{abcd} = -R_{abdc}          (antisymmetric in second pair)
        R_{abcd} = +R_{cdab}          (pair exchange symmetry)
        R_{abcd} + R_{acdb} + R_{adbc} = 0  (first Bianchi)

    Args:
        s: Jensen deformation parameter (s=0 gives bi-invariant SU(3))

    Returns:
        R_abcd: (8,8,8,8) float64 array, R_abcd[a,b,c,d] = R_{abcd}
    """
    n = 8

    # Build geometric infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Compute R^d_{abc} (mixed tensor: d up, a,b,c down)
    # R^d_{abc} = Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be} - ft^e_{ab} Gamma^d_{ec}
    # Using numpy einsum for efficiency:
    #   term1[d,a,b,c] = sum_e Gamma[e,b,c] * Gamma[d,a,e]
    #   term2[d,a,b,c] = sum_e Gamma[e,a,c] * Gamma[d,b,e]
    #   term3[d,a,b,c] = sum_e ft[a,b,e]   * Gamma[d,e,c]

    term1 = np.einsum('ebc,dae->dabc', Gamma, Gamma)
    term2 = np.einsum('eac,dbe->dabc', Gamma, Gamma)
    term3 = np.einsum('abe,dec->dabc', ft, Gamma)

    R_mixed = term1 - term2 - term3  # R_mixed[d,a,b,c] = R^d_{abc}

    # Lower the first (d) index: R_{abcd} = delta_{de} R^e_{abc} = R^d_{abc}
    # In ON frame, g_{de} = delta_{de}, so lowering is trivial.
    # Standard convention: store R_{abcd} with index ordering consistent with
    # Riemann(a,b) applied to pair (c -> slot, d -> result after lowering).
    # We follow sp2_final_verification.py convention:
    #   Riem[d,a,b,c] = R^d_{abc}
    #   R_std[a,b,c,d] = Riem[d(=rho),a(=mu),b(=nu),c(=sigma)]
    #                   = R^{rho}_{mu nu sigma}  -> fully covariant: R_{mu nu sigma rho}
    # For our purposes (Lichnerowicz action), we need R_{acbd} h^{cd}.
    # We store R_abcd[a,b,c,d] = R_{abcd} = R_mixed[d,a,b,c]  (d down = last index).

    R_abcd = np.zeros((n, n, n, n), dtype=np.float64)
    for d in range(n):
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    # R_{abcd} = g_{de} R^e_{abc}; in ON frame g_{de}=delta -> R^d_{abc}
                    R_abcd[a, b, c, d] = R_mixed[d, a, b, c]

    return R_abcd


def compute_riemann_tensor_ON_fast(s: float) -> np.ndarray:
    """
    Vectorized computation of R_{abcd}(s) using einsum throughout.

    This avoids the Python-level quadruple loop in compute_riemann_tensor_ON()
    and is substantially faster for sweep computations.

    Same mathematical content as compute_riemann_tensor_ON() but ~100x faster.

    Returns:
        R_abcd: (8,8,8,8) float64, R_abcd[a,b,c,d] = R_{abcd}
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # R^d_{abc} = Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be} - ft^e_{ab} Gamma^d_{ec}
    # Gamma[c,a,b] = Gamma^c_{ab}
    # term1[d,a,b,c] = sum_e Gamma[e,b,c] * Gamma[d,a,e]
    term1 = np.einsum('ebc,dae->dabc', Gamma, Gamma)
    # term2[d,a,b,c] = sum_e Gamma[e,a,c] * Gamma[d,b,e]
    term2 = np.einsum('eac,dbe->dabc', Gamma, Gamma)
    # term3[d,a,b,c] = sum_e ft[a,b,e] * Gamma[d,e,c]
    term3 = np.einsum('abe,dec->dabc', ft, Gamma)

    R_mixed = term1 - term2 - term3  # R_mixed[d,a,b,c] = R^d_{abc}

    # Lower: R_{abcd} = R^d_{abc} -> R_abcd[a,b,c,d] = R_mixed[d,a,b,c]
    R_abcd = np.einsum('dabc->abcd', R_mixed)

    return R_abcd


# =============================================================================
# MODULE 2: VALIDATION SUITE
# =============================================================================

def scalar_curvature_our_metric(s: float) -> float:
    """
    Exact scalar curvature R(s) for our metric g_s = 3*diag(e^{-2s},...,e^{2s}).

    From SP-2 exact formula (verified at machine epsilon, 51 s-values):
        R(s) = -(1/4) e^{-4s} + 2 e^{-s} - 1/4 + (1/2) e^{2s}

    At s=0: R(0) = 2.0 (Einstein manifold: Ric = (1/4) g)
    """
    return -0.25 * np.exp(-4*s) + 2.0 * np.exp(-s) - 0.25 + 0.5 * np.exp(2*s)


def kretschner_exact(s: float) -> float:
    """
    Exact Kretschner scalar K(s) = R_{abcd} R^{abcd} from SP-2.

    From SP-2 exact formula (verified at machine epsilon):
        K(s) = (23/96) e^{-8s} - e^{-5s} + (5/16) e^{-4s}
              + (11/6) e^{-2s} - (3/2) e^{-s} + 17/32
              + (1/12) e^{4s}
    """
    return (
        (23/96) * np.exp(-8*s)
        - 1.0 * np.exp(-5*s)
        + (5/16) * np.exp(-4*s)
        + (11/6) * np.exp(-2*s)
        - 1.5 * np.exp(-s)
        + (17/32)
        + (1/12) * np.exp(4*s)
    )


def validate_riemann_tensor(R_abcd: np.ndarray, s: float, tol: float = 1e-8) -> dict:
    """
    Comprehensive validation of R_{abcd}(s).

    Tests:
    (V1) Antisymmetry in first pair: R_{abcd} = -R_{bacd}
    (V2) Antisymmetry in second pair: R_{abcd} = -R_{abdc}
    (V3) Pair exchange symmetry: R_{abcd} = R_{cdab}
    (V4) First Bianchi identity: R_{abcd} + R_{acdb} + R_{adbc} = 0
    (V5) Ricci contraction R_{ab} = R^c_{acb} = R[a,c,c,b] matches ricci_tensor_ON()
    (V6) Scalar curvature R = g^{ab} R_{ab} matches SP-2 formula
    (V7) Kretschner K = R_{abcd} R^{abcd} matches SP-2 exact formula
    (V8) At s=0: R_{abcd} = -(1/4) f_{abe} f^e_{cd} (bi-invariant formula)

    Args:
        R_abcd: (8,8,8,8) Riemann tensor from compute_riemann_tensor_ON_fast()
        s: Jensen parameter
        tol: tolerance for all checks

    Returns:
        results: dict with test names as keys and (passed, error, detail) tuples
    """
    n = 8
    results = {}

    # V1: Antisymmetry in (a,b)
    err_V1 = np.max(np.abs(R_abcd + np.einsum('abcd->bacd', R_abcd)))
    results['V1_antisym_ab'] = (err_V1 < tol, err_V1, 'R_{abcd} = -R_{bacd}')

    # V2: Antisymmetry in (c,d)
    err_V2 = np.max(np.abs(R_abcd + np.einsum('abcd->abdc', R_abcd)))
    results['V2_antisym_cd'] = (err_V2 < tol, err_V2, 'R_{abcd} = -R_{abdc}')

    # V3: Pair exchange
    err_V3 = np.max(np.abs(R_abcd - np.einsum('abcd->cdab', R_abcd)))
    results['V3_pair_exchange'] = (err_V3 < tol, err_V3, 'R_{abcd} = R_{cdab}')

    # V4: First Bianchi identity: R_{abcd} + R_{acdb} + R_{adbc} = 0
    bianchi = R_abcd + np.einsum('abcd->acdb', R_abcd) + np.einsum('abcd->adbc', R_abcd)
    err_V4 = np.max(np.abs(bianchi))
    results['V4_first_bianchi'] = (err_V4 < tol, err_V4, 'R_{[abc]d} = 0')

    # V5: Ricci contraction
    # R_{ab} = R^c_{acb} = R_{abcd} contracted appropriately.
    # With our storage R_abcd[a,b,c,d] = R_{abcd}:
    # R^e_{abc} = R_abcd[a,b,c,:] (d index up, but in ON frame d-up = d-down)
    # = R_mixed[d,a,b,c] = R_abcd[a,b,c,d] transposed appropriately.
    # Ricci: Ric[b,c] = sum_a R^a_{abc} = sum_a R_{abca} (using R[a,b,c,d]=R_{abcd})
    # Wait: R^a_{abc} means R with first index up = a, then a,b,c. Let me be careful.
    # R^d_{abc}: mixed, computed as R_mixed[d,a,b,c].
    # R_abcd[a,b,c,d] = R_mixed[d,a,b,c].
    # Ric_{bc} = sum_a R^a_{abc} = sum_a R_mixed[a,a,b,c]
    # R_mixed[a,a,b,c] = R_abcd[a,b,c,a]
    Ric_from_R = np.einsum('abca->bc', R_abcd)  # sum over a: R_{abca} = R^a_{abc}

    # Compare with ricci_tensor_ON from b6_scalar_vector_laplacian.py
    from b6_scalar_vector_laplacian import ricci_tensor_ON
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Ric_ref = ricci_tensor_ON(ft, Gamma)

    err_V5 = np.max(np.abs(Ric_from_R - Ric_ref))
    results['V5_ricci_contraction'] = (err_V5 < tol, err_V5, 'Ric_{bc} = R^a_{abc}')

    # V6: Scalar curvature
    R_scalar = np.trace(Ric_from_R)
    R_expected = scalar_curvature_our_metric(s)
    err_V6 = abs(R_scalar - R_expected)
    results['V6_scalar_curvature'] = (
        err_V6 < tol, err_V6,
        f'R={R_scalar:.8f} vs R_exact={R_expected:.8f}'
    )

    # V7: Kretschner scalar K = R_{abcd} R^{abcd} = sum R_{abcd}^2 (in ON frame)
    K_computed = np.sum(R_abcd ** 2)
    K_exact = kretschner_exact(s)
    err_V7 = abs(K_computed - K_exact) / max(abs(K_exact), 1e-15)
    results['V7_kretschner'] = (
        err_V7 < tol, err_V7,
        f'K={K_computed:.8f} vs K_exact={K_exact:.8f}'
    )

    # V8: Bi-invariant formula at s=0
    # For bi-invariant metric: R_{abcd} = -(1/4) [e_a,e_b] . [e_c,e_d] metric
    # In ON frame: R_{abcd} = -(1/4) sum_e f_{abe} f_{cde}
    # where f_{abe} are ON-frame structure constants at s=0 (= f_abc/sqrt(3) per index)
    # At s=0: ft = E f_abc E^{-1} where E = (1/sqrt(3)) I, so ft[a,b,c] = (1/sqrt(3)) f_abc[a,b,c]
    if abs(s) < 1e-10:
        g0 = jensen_metric(B_ab, 0.0)
        E0 = orthonormal_frame(g0)
        ft0 = frame_structure_constants(f_abc, E0)
        # R_{abcd} = -(1/4) sum_e ft0[a,b,e] * ft0[c,d,e]
        R_biinv = -0.25 * np.einsum('abe,cde->abcd', ft0, ft0)
        err_V8 = np.max(np.abs(R_abcd - R_biinv))
        results['V8_biinv_formula'] = (
            err_V8 < tol, err_V8,
            'R_{abcd}|_{s=0} = -(1/4) f_{abe} f_{cde}'
        )

    return results


# =============================================================================
# MODULE 3: RICCI TENSOR FROM RIEMANN
# =============================================================================

def ricci_from_riemann(R_abcd: np.ndarray) -> np.ndarray:
    """
    Extract Ricci tensor from Riemann tensor.

    Ric_{bc} = R^a_{abc} = R_{abca}  (contraction over a)

    In our storage convention R_abcd[a,b,c,d] = R_{abcd}:
        Ric_{bc} = sum_a R_{abca} = np.einsum('abca->bc', R_abcd)

    Args:
        R_abcd: (8,8,8,8) Riemann tensor

    Returns:
        Ric: (8,8) Ricci tensor in ON frame
    """
    return np.einsum('abca->bc', R_abcd)


# =============================================================================
# MODULE 4: KRETSCHNER AND NORM-SQUARED
# =============================================================================

def riemann_norm_squared(R_abcd: np.ndarray) -> float:
    """
    Compute |Riem|^2 = R_{abcd} R^{abcd}.

    In ON frame (g_{ab} = delta_{ab}), raising indices is trivial:
        R^{abcd} = R_{abcd}

    So: |Riem|^2 = sum_{a,b,c,d} R_{abcd}^2

    This is the Kretschner scalar K needed for the a_4 Seeley-DeWitt coefficient.

    Args:
        R_abcd: (8,8,8,8) Riemann tensor

    Returns:
        K: scalar |Riem|^2
    """
    return float(np.sum(R_abcd ** 2))


# =============================================================================
# MODULE 5: SWEEP OVER TAU VALUES
# =============================================================================

def sweep_riemann_tensor(
    tau_values: np.ndarray,
    verbose: bool = True
) -> dict:
    """
    Compute R_{abcd}(tau) and |Riem|^2(tau) for all tau values.

    Args:
        tau_values: array of Jensen parameter values
        verbose: print progress

    Returns:
        sweep: dict with keys:
            'tau': tau_values array
            'R_abcd': (n_tau, 8, 8, 8, 8) Riemann tensors
            'Ric': (n_tau, 8, 8) Ricci tensors
            'R_scalar': (n_tau,) scalar curvatures
            'K': (n_tau,) Kretschner scalars |Riem|^2
            'val_errors': list of validation error dicts per tau
    """
    n_tau = len(tau_values)
    R_all = np.zeros((n_tau, 8, 8, 8, 8), dtype=np.float64)
    Ric_all = np.zeros((n_tau, 8, 8), dtype=np.float64)
    R_scalar_all = np.zeros(n_tau, dtype=np.float64)
    K_all = np.zeros(n_tau, dtype=np.float64)
    val_errors_all = []

    if verbose:
        print(f"  Computing Riemann tensor at {n_tau} tau-values...")
        print(f"  {'tau':>8}  {'R(tau)':>12}  {'K(tau)':>14}  {'K_err':>10}  {'V1-V7 pass':>12}")
        print(f"  {'-'*70}")

    t0 = time.time()

    for i, tau in enumerate(tau_values):
        R_abcd = compute_riemann_tensor_ON_fast(tau)
        R_all[i] = R_abcd

        Ric = ricci_from_riemann(R_abcd)
        Ric_all[i] = Ric

        R_scalar = float(np.trace(Ric))
        R_scalar_all[i] = R_scalar

        K = riemann_norm_squared(R_abcd)
        K_all[i] = K

        # Validate (skip V8 for non-zero tau to save time, include at tau=0)
        val = validate_riemann_tensor(R_abcd, tau)
        val_errors_all.append(val)

        all_pass = all(v[0] for v in val.values())
        max_err = max(v[1] for v in val.values())

        K_exact = kretschner_exact(tau)
        K_err = abs(K - K_exact) / max(abs(K_exact), 1e-15)

        if verbose:
            status = "ALL PASS" if all_pass else f"FAIL (err={max_err:.2e})"
            print(f"  {tau:8.4f}  {R_scalar:12.6f}  {K:14.8f}  {K_err:10.2e}  {status:>12}")

    dt = time.time() - t0
    if verbose:
        print(f"\n  Sweep complete in {dt:.1f}s ({dt/n_tau:.2f}s per tau)")

    return {
        'tau': tau_values,
        'R_abcd': R_all,
        'Ric': Ric_all,
        'R_scalar': R_scalar_all,
        'K': K_all,
        'val_errors': val_errors_all,
    }


# =============================================================================
# MODULE 6: MAIN
# =============================================================================

def main():
    """
    Main computation: build R_{abcd}(tau) for 21 tau-values, validate, save.
    """
    print("=" * 72)
    print("  R-1: FULL RIEMANN TENSOR ON JENSEN-DEFORMED SU(3)")
    print("  Phonon-Exflation Session 20a")
    print("  Sim-Specialist Agent")
    print("=" * 72)

    tau_values = np.linspace(0.0, 2.0, 21)

    # =========================================================================
    # PHASE 1: VALIDATION AT s=0
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 1: VALIDATION AT s=0 (BI-INVARIANT)")
    print("=" * 72)

    t_start = time.time()
    R0 = compute_riemann_tensor_ON_fast(0.0)
    val0 = validate_riemann_tensor(R0, 0.0, tol=1e-8)

    all_passed = True
    for name, (passed, err, detail) in val0.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {name:30s}: {status}  (err={err:.3e})  {detail}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\n  ALL VALIDATION CHECKS PASS at s=0")
    else:
        print("\n  WARNING: Some validation checks FAILED at s=0")

    # =========================================================================
    # PHASE 2: RIEMANN TENSOR AT SEVERAL KEY s VALUES
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 2: RIEMANN TENSOR PROPERTIES AT KEY s VALUES")
    print("=" * 72)

    key_s_values = [0.0, 0.15, 0.30, 0.50, 1.0, 1.5, 2.0]
    print(f"\n  {'s':>6}  {'R(s)':>12}  {'R_exact':>12}  {'R_err':>10}  "
          f"{'K':>14}  {'K_exact':>14}  {'K_err':>10}")
    print(f"  {'-'*85}")

    for s_val in key_s_values:
        R = compute_riemann_tensor_ON_fast(s_val)
        Ric = ricci_from_riemann(R)
        R_scalar = float(np.trace(Ric))
        K = riemann_norm_squared(R)

        R_ex = scalar_curvature_our_metric(s_val)
        K_ex = kretschner_exact(s_val)
        R_err = abs(R_scalar - R_ex)
        K_err = abs(K - K_ex) / max(abs(K_ex), 1e-15)

        print(f"  {s_val:6.2f}  {R_scalar:12.8f}  {R_ex:12.8f}  {R_err:10.2e}  "
              f"{K:14.8f}  {K_ex:14.8f}  {K_err:10.2e}")

    # =========================================================================
    # PHASE 3: FULL SWEEP — 21 TAU VALUES
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 3: FULL SWEEP — 21 TAU VALUES in [0, 2.0]")
    print("=" * 72)

    sweep = sweep_riemann_tensor(tau_values, verbose=True)

    # =========================================================================
    # PHASE 4: |RIEM|^2 SUMMARY TABLE FOR CONNES (SD-1 a_4 COEFFICIENT)
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 4: |RIEM|^2(tau) — FOR CONNES TEAMMATE (SD-1 a_4)")
    print("=" * 72)

    print(f"\n  K(tau) = R_{{abcd}} R^{{abcd}}  (Kretschner scalar)")
    print(f"  Needed by Connes for Seeley-DeWitt a_4 coefficient.")
    print(f"  Formula: a_4 ~ integral [R^2 + alpha * |Ric|^2 + beta * K + ...]")
    print()
    print(f"  {'tau':>8}  {'K = |Riem|^2':>18}  {'K_exact':>18}  {'rel_err':>10}")
    print(f"  {'-'*65}")

    K_values = sweep['K']
    K_exact_values = np.array([kretschner_exact(tau) for tau in tau_values])
    max_K_rel_err = 0.0

    for i, (tau, K, K_ex) in enumerate(zip(tau_values, K_values, K_exact_values)):
        K_err = abs(K - K_ex) / max(abs(K_ex), 1e-15)
        max_K_rel_err = max(max_K_rel_err, K_err)
        print(f"  {tau:8.4f}  {K:18.10f}  {K_ex:18.10f}  {K_err:10.2e}")

    print(f"\n  Maximum relative error in K(tau): {max_K_rel_err:.3e}")
    status = "PASS" if max_K_rel_err < 1e-8 else "FAIL"
    print(f"  K(tau) validation: {status}")

    # =========================================================================
    # PHASE 5: VALIDATION SUMMARY ACROSS ALL TAU
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 5: FULL VALIDATION SUMMARY ACROSS ALL 21 TAU VALUES")
    print("=" * 72)

    test_names = ['V1_antisym_ab', 'V2_antisym_cd', 'V3_pair_exchange',
                  'V4_first_bianchi', 'V5_ricci_contraction',
                  'V6_scalar_curvature', 'V7_kretschner']

    max_errors_per_test = {t: 0.0 for t in test_names}
    n_failed = {t: 0 for t in test_names}

    for i, (tau, val_dict) in enumerate(zip(tau_values, sweep['val_errors'])):
        for t in test_names:
            if t in val_dict:
                passed, err, _ = val_dict[t]
                max_errors_per_test[t] = max(max_errors_per_test[t], err)
                if not passed:
                    n_failed[t] += 1

    print(f"\n  {'Test':35s}  {'Max Error':>12}  {'Failures':>10}  Status")
    print(f"  {'-'*75}")
    all_global_pass = True
    for t in test_names:
        max_e = max_errors_per_test[t]
        n_f = n_failed[t]
        ok = (n_f == 0)
        if not ok:
            all_global_pass = False
        status = "PASS" if ok else f"FAIL ({n_f} tau)"
        print(f"  {t:35s}  {max_e:12.3e}  {n_f:10d}  {status}")

    if all_global_pass:
        print(f"\n  GLOBAL RESULT: ALL {len(test_names)} TESTS PASS across 21 tau values")
    else:
        print(f"\n  GLOBAL RESULT: FAILURES DETECTED — inspect output above")

    # =========================================================================
    # PHASE 6: SAVE TO NPZ
    # =========================================================================
    print("\n" + "=" * 72)
    print("  PHASE 6: SAVE DATA")
    print("=" * 72)

    outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'r20a_riemann_tensor.npz')

    np.savez_compressed(
        outfile,
        tau=tau_values,
        R_abcd=sweep['R_abcd'],     # (21, 8, 8, 8, 8) full Riemann tensor
        Ric=sweep['Ric'],           # (21, 8, 8) Ricci tensor
        R_scalar=sweep['R_scalar'], # (21,) scalar curvature
        K=sweep['K'],               # (21,) Kretschner = |Riem|^2
        K_exact=K_exact_values,     # (21,) exact analytic values
    )

    print(f"\n  Saved: {outfile}")
    print(f"  Arrays stored:")
    print(f"    tau:     shape {tau_values.shape}")
    print(f"    R_abcd:  shape {sweep['R_abcd'].shape}  (full Riemann tensor)")
    print(f"    Ric:     shape {sweep['Ric'].shape}  (Ricci tensor)")
    print(f"    R_scalar: shape {sweep['R_scalar'].shape}  (scalar curvature)")
    print(f"    K:       shape {sweep['K'].shape}  (Kretschner |Riem|^2)")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)

    t_total = time.time() - t_start
    print(f"""
  R-1 COMPUTATION COMPLETE

  Deliverables:
  1. compute_riemann_tensor_ON(s): function returning 8x8x8x8 R_{{abcd}}
  2. compute_riemann_tensor_ON_fast(s): vectorized version (~100x faster)
  3. Validation suite: 7 tests (antisymmetry x2, pair exchange, Bianchi,
     Ricci contraction, scalar curvature, Kretschner) at all 21 tau values
  4. |Riem|^2(tau) for all 21 tau values (for Connes, SD-1 a_4 coefficient)
  5. Data saved: r20a_riemann_tensor.npz

  Key results:
  - R_{{abcd}} convention: R_abcd[a,b,c,d] = R_{{abcd}} (all indices down, ON frame)
  - R_abcd[a,b,c,d] = R_mixed[d,a,b,c] = R^d_{{abc}} (4th index was upper)
  - |Riem|^2(0) = K(0) = {kretschner_exact(0.0):.8f}
  - |Riem|^2 monotone? From tau=0 to tau=2.0: {K_values[0]:.4f} -> {K_values[-1]:.4f}

  Global validation: {"PASS" if all_global_pass else "FAIL"}
  Total runtime: {t_total:.1f}s
    """)

    # Print K values as a compact array for message to connes
    print("\n  K(tau) = |Riem|^2 VALUES (for Connes teammate):")
    print("  " + ", ".join([f"{K:.8f}" for K in K_values]))

    return sweep


if __name__ == "__main__":
    main()
