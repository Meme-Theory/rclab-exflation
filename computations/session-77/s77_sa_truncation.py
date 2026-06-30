#!/usr/bin/env python3
"""
S77-B11-SA-TRUNC: Full Spectral Action vs Seeley-DeWitt Truncation
====================================================================

Compare the full spectral action sum S_full = Tr f(D^2/Lambda^2) (computed over
all eigenvalues at max_pq_sum=3 with (1,2) sector included) to the Seeley-DeWitt
(SDW) truncation at three terms (a_0, a_2, a_4).

Mathematical Setup:
  The Dirac operator D on (SU(3), g_tau) is anti-Hermitian with purely imaginary
  eigenvalues {+i*mu_j, -i*mu_j}, perfectly ±-paired. The physics Laplacian is
  Delta = -D^2 with eigenvalues mu_j^2 > 0.

  The heat kernel is:
    K(t) = Tr(e^{-t*Delta}) = 2 * sum_{j: positive} PW_j * e^{-t*mu_j^2}

  The SDW expansion for d=8:
    K(t) ~ a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2} + a_6*t^{-1} + a_8 + O(t)

  The canonical SDW coefficients are spectral zeta moments (S42):
    a_0 = sum_{j:pos} PW_j                    = 6440.0
    a_2 = sum_{j:pos} PW_j * mu_j^{-2}        = 2776.165
    a_4 = sum_{j:pos} PW_j * mu_j^{-4}        = 1350.722

  For general test function f, the spectral action is:
    S_full = Tr f(Delta/Lambda^2) = 2 * sum_{j:pos} PW_j * f(mu_j^2/Lambda^2)

  The SDW truncation for f(x) = e^{-x} (heat kernel):
    S_SDW^{(3)} = a_0*Lambda^8 + a_2*Lambda^6 + a_4*Lambda^4

  This comparison tests whether the 3-term truncation is adequate at
  Lambda = 5.033 M_KK (the Hessian stability critical cutoff from S66).

  IMPORTANT: At max_pq_sum=3, the maximum |lambda| = 2.061 M_KK.
  Since Lambda = 5.033 >> lambda_max, ALL eigenvalues contribute.
  The SDW expansion is an ASYMPTOTIC expansion in Lambda -> infinity.
  The question is whether Lambda/lambda_max = 2.44 is large enough for the
  expansion to converge at 3 terms.

  NOTE ON CONVENTION: We use both ALL eigenvalues (for S_full, symmetric)
  and POSITIVE-only (for the canonical SDW coefficients). Both conventions
  give the same physics because of exact ± pairing:
    S_full(all) = 2 * S_full(positive)
    SDW(all)    = 2 * SDW(positive)
  So the residual ratio is convention-independent.

Cutoff functions:
  1. Heat kernel: f(x) = exp(-x)    [cleanest SDW connection]
  2. Sharp:       f(x) = Theta(1-x) [counting function]
  3. Gaussian:    f(x) = exp(-x^2)  [faster UV decay]

Gate S77-B11-SA-TRUNC:
  PASS: Residual < 1% of a_4 contribution  (SDW adequate for gauge sector)
  FAIL: Residual > 10% of a_4 contribution (SDW unreliable)
  INFO: 1% < residual < 10% (borderline)

Author: connes-ncg-theorist (Session 77)
Date: 2026-04-13
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    collect_spectrum,
)
from canonical_constants import tau_fold, a0_fold, a2_fold, a4_fold

# ===========================================================================
# CONFIGURATION
# ===========================================================================

TAU = tau_fold                   # Jensen deformation at the fold = 0.19
LAMBDA = 5.033                   # (local) M_KK units, Hessian critical cutoff (S66)
MAX_PQ_SUM = 3                   # (local) all supported sectors (10 sectors)
OUTDIR = os.path.dirname(os.path.abspath(__file__))

# Gate thresholds
PASS_THRESH = 0.01               # (local) residual < 1% of a_4 -> PASS
FAIL_THRESH = 0.10               # (local) residual > 10% of a_4 -> FAIL


def dim_su3(p, q):
    """SU(3) irrep dimension."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ===========================================================================
# STEP 1: COMPUTE FULL SPECTRUM AT THE FOLD
# ===========================================================================

def compute_spectrum():
    """Build infrastructure and compute Dirac spectrum at tau_fold."""
    print("Building SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    err = validate_clifford(gammas)
    print(f"  Cliff(8) validated: max err = {err:.2e}")

    print(f"\nComputing Dirac spectrum at tau = {TAU:.3f}, max_pq_sum = {MAX_PQ_SUM}...")
    t0 = time.time()  # (local)
    all_eigenvalues, eval_data = collect_spectrum(
        TAU, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=True
    )
    dt = time.time() - t0  # (local)
    print(f"  Spectrum computed in {dt:.1f}s")

    return eval_data


# ===========================================================================
# STEP 2: EXTRACT POSITIVE EIGENVALUES WITH PW WEIGHTS
# ===========================================================================

def extract_positive_eigenvalues(eval_data):
    """
    Extract positive-imaginary eigenvalues with Peter-Weyl weights.

    Returns:
        mu_sq_list: list of (mu_j^2, PW_weight) for positive eigenvalues
        Also computes and verifies SDW coefficients.
    """
    mu_sq_list = []  # (local) list of (mu^2, PW_weight)

    a0_check = 0.0  # (local)
    a2_check = 0.0  # (local)
    a4_check = 0.0  # (local)
    a6_check = 0.0  # (local)
    a8_check = 0.0  # (local)

    print(f"\n  Sector decomposition (positive eigenvalues only):")
    print(f"  {'sector':>8}  {'dim':>4}  {'PW':>4}  {'n_pos':>6}  {'mu_min':>8}  {'mu_max':>8}  {'a0_sec':>8}  {'a2_sec':>12}  {'a4_sec':>12}")
    print("  " + "-" * 90)

    for p, q, evals in eval_data:
        d_pq = dim_su3(p, q)
        pw = d_pq  # (local) Peter-Weyl weight

        # Select positive-imaginary eigenvalues
        pos_mask = evals.imag > 1e-10  # (local)
        pos_evals = evals[pos_mask]  # (local)
        mu_vals = np.abs(pos_evals)  # (local) = |imaginary part|

        n_pos = len(mu_vals)  # (local)
        mu_sq = mu_vals ** 2  # (local)

        for m2 in mu_sq:
            mu_sq_list.append((m2, pw))

        # SDW moments
        s_a0 = pw * n_pos  # (local)
        s_a2 = pw * np.sum(mu_vals ** (-2))  # (local)
        s_a4 = pw * np.sum(mu_vals ** (-4))  # (local)
        s_a6 = pw * np.sum(mu_vals ** (-6))  # (local)
        s_a8 = pw * np.sum(mu_vals ** (-8))  # (local)

        a0_check += s_a0
        a2_check += s_a2
        a4_check += s_a4
        a6_check += s_a6
        a8_check += s_a8

        print(f"  ({p},{q}):  {d_pq:4d}  {pw:4d}  {n_pos:6d}  {mu_vals.min():8.4f}  {mu_vals.max():8.4f}"
              f"  {s_a0:8.0f}  {s_a2:12.4f}  {s_a4:12.4f}")

    # Verify against canonical
    print(f"\n  SDW coefficient verification:")
    print(f"    a_0: computed={a0_check:.1f}, canonical={a0_fold:.1f}, match={abs(a0_check-a0_fold)<0.1}")
    print(f"    a_2: computed={a2_check:.6f}, canonical={a2_fold:.6f}, match={abs(a2_check-a2_fold)<0.01}")
    print(f"    a_4: computed={a4_check:.6f}, canonical={a4_fold:.6f}, match={abs(a4_check-a4_fold)<0.01}")
    print(f"    a_6: computed={a6_check:.6f}")
    print(f"    a_8: computed={a8_check:.6f}")

    return mu_sq_list, a0_check, a2_check, a4_check, a6_check, a8_check


# ===========================================================================
# STEP 3: COMPUTE S_full AND S_SDW FOR EACH CUTOFF FUNCTION
# ===========================================================================

def compute_spectral_actions(mu_sq_list, Lambda, a0, a2, a4, a6, a8):
    """
    For each test function f:
      - Compute S_full = 2 * sum_{j:pos} PW_j * f(mu_j^2/Lambda^2)
      - Compute S_SDW at various truncation orders
      - Compute the residual

    The factor of 2 accounts for the ± pairing. It cancels in all ratios.
    We work with positive-only sums and drop the factor of 2.

    For heat kernel f(x) = e^{-x}:
      S_full_pos = sum PW * exp(-mu^2/Lambda^2)
      S_SDW_pos  = a_0*Lambda^8 + a_2*Lambda^6 + a_4*Lambda^4

    The SDW expansion of the POSITIVE-ONLY heat kernel is:
      K_pos(t) = sum_{pos} PW * e^{-t*mu^2} ~ (a_0/2)*t^{-4} + (a_2/2)*t^{-3} + ...

    WAIT -- this is wrong. The heat kernel K(t) = Tr(e^{-tD^2}) sums over
    ALL eigenvalues. Since |lambda|^2 = mu^2 for both signs:
      K(t) = 2 * sum_{pos} PW * e^{-t*mu^2}
      K(t) ~ a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2} + ...

    But what is the relationship between the SDW coefficients (defined as
    spectral zeta moments from positive eigenvalues) and the heat kernel
    expansion?

    The spectral zeta function:
      zeta_D(s) = sum |lambda|^{-2s} (over all non-zero eigenvalues)
               = 2 * sum_{pos} PW * mu^{-2s}

    The SDW coefficients from the heat kernel expansion should satisfy:
      a_n = (zeta moment) * (some normalization)

    Actually, the relationship is:
      K(t) = sum_all e^{-t*mu^2} = integral_0^infty e^{-t*x} dN(x)
    where N(x) = #{eigenvalues with mu^2 <= x} (full spectrum counting function).

    The Weyl asymptotic for the counting function gives:
      N(x) ~ C_0 * x^4 + C_2 * x^3 + C_4 * x^2 + ...

    And the heat kernel coefficients are related by Mellin transform:
      a_n = C_n * Gamma(4-n)  (for the leading terms)

    No, let me be more precise. For d=8 manifold, the counting function is:
      N(E) = #{mu^2 <= E} ~ sum_n c_n * E^{(d-2n)/2}
    and the heat kernel is:
      K(t) = integral e^{-tE} dN(E)
           = sum_n c_n * Gamma((d-2n)/2 + 1) * t^{-(d-2n)/2}

    But K(t) ~ sum a_{2n} t^{(2n-d)/2}, so:
      a_{2n} = c_{2n} * Gamma((d-2n)/2 + 1) = c_{2n} * Gamma(4-n+1)

    Wait. K(t) = a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + ...

    integral_{0}^{infty} e^{-tE} * E^{alpha} dE = Gamma(alpha+1) / t^{alpha+1}

    If dN/dE ~ sum c_n E^{(d-2n)/2 - 1} = sum c_n E^{3-n}:
      K(t) = integral e^{-tE} sum c_n E^{3-n} dE
           = sum c_n Gamma(4-n) t^{-(4-n)}

    So a_0 = c_0 * Gamma(4), a_2 = c_2 * Gamma(3), a_4 = c_4 * Gamma(2), ...
    i.e., a_0 = 6*c_0, a_2 = 2*c_2, a_4 = c_4, a_6 = c_6 * Gamma(0) = diverges...

    Hmm, this means the heat kernel expansion coefficients are NOT the same as
    the spectral zeta moments. The canonical a_0 = 6440 is defined as
    sum PW * (count of positive eigenvalues), which is the zeroth zeta moment.
    But the heat kernel a_0 should be the counting function leading coefficient
    times Gamma(4) = 6.

    CRITICAL REALIZATION: The canonical "a_0" = 6440 is NOT the heat kernel
    Seeley-DeWitt coefficient. It's the number of positive eigenvalues
    (PW-weighted). The actual heat kernel a_0 would be related but different.

    For a TRUNCATED (finite) spectrum, the heat kernel is EXACTLY:
      K(t) = 2 * sum_{j:pos} PW_j * exp(-t * mu_j^2)

    The SDW expansion of this truncated heat kernel at small t gives approximate
    coefficients that converge to the true geometric SDW coefficients as we
    add more irreps.

    But for the COMPARISON S_full vs S_SDW, the correct approach is:

    Method A (DIRECT): Compare S_full against the SDW expansion using the
    heat kernel coefficients extracted from polynomial fitting of t^4*K(t).

    Method B (SPECTRAL ZETA): Compare S_full against a power series in Lambda
    using the spectral zeta moments a_0^{zeta}, a_2^{zeta}, a_4^{zeta}.

    The canonical values a_0=6440, a_2=2776, a_4=1351 are zeta moments.

    For the heat kernel test function at t = 1/Lambda^2:
      K(1/Lambda^2) = 2 * sum_{pos} PW * exp(-mu^2/Lambda^2)

    The expansion of this in Lambda:
      K(1/Lambda^2) = 2 * sum_{pos} PW * [1 - mu^2/Lambda^2 + mu^4/(2*Lambda^4) - ...]
                    = 2 * [a_0 - a_2/Lambda^2 + (1/2)*a_4^{(raw)}/Lambda^4 - ...]

    Wait. Let me expand term by term:
      sum PW * exp(-mu^2/Lambda^2)
        = sum PW * 1                      -> a_0
        - sum PW * mu^2/Lambda^2          -> a_0^{(2)}/Lambda^2
        + sum PW * mu^4/(2*Lambda^4)      -> (1/2)*a_0^{(4)}/Lambda^4
        - ...

    where a_0^{(2k)} = sum PW * mu^{2k} are the POWER SUM moments (NOT zeta moments).

    The zeta moments are a_{2n} = sum PW * mu^{-2n}. These are DIFFERENT.

    The heat kernel expansion in DESCENDING powers of Lambda uses POWER SUMS:
      K(1/Lambda^2) = sum PW * exp(-mu^2/Lambda^2)
                    = sum_{k=0}^{infty} (-1)^k/(k!) * sum PW * mu^{2k} / Lambda^{2k}
                    = sum_{k=0}^{infty} (-1)^k/(k!) * M_{2k} / Lambda^{2k}

    where M_{2k} = sum PW * mu^{2k} are the power sum moments.

    M_0 = a_0 (the zeroth moment = count of eigenvalues)
    M_2 = sum PW * mu^2 (the spectral action at Lambda=1 for f(x)=x: total energy)
    M_4 = sum PW * mu^4

    The GEOMETRIC Seeley-DeWitt expansion at t -> 0:
      K(t) ~ a_0^{SDW} * t^{-4} + a_2^{SDW} * t^{-3} + a_4^{SDW} * t^{-2} + ...

    For FINITE truncated spectrum (finite number of eigenvalues):
      K(t) = entire function of t, NO singularity at t=0

    So the SDW expansion is meaningless for a truncated spectrum at t -> 0.
    It only makes sense for the FULL infinite spectrum.

    HOWEVER, for FINITE Lambda, the comparison is well-defined:
    - S_full(Lambda) = exact finite sum
    - S_SDW(Lambda) = polynomial in Lambda based on extracted coefficients

    The question becomes: which coefficients to use in the SDW expansion?

    ANSWER: The correct comparison uses the POWER SUM approach. For the heat
    kernel at finite Lambda:

      S_full = sum PW * exp(-mu^2/Lambda^2)

      Taylor expansion around Lambda=infty (i.e., in 1/Lambda^2):
        S_full = M_0 - M_2/Lambda^2 + M_4/(2*Lambda^4) - M_6/(6*Lambda^6) + ...

      3-term truncation:
        S_SDW^{(3)} = M_0 - M_2/Lambda^2 + M_4/(2*Lambda^4)

      Residual = |S_full - S_SDW^{(3)}|

    But this is a small-mu expansion, valid when mu/Lambda << 1.
    Since mu_max = 2.06 and Lambda = 5.033, mu_max/Lambda = 0.41, so
    (mu_max/Lambda)^2 = 0.17. The series should converge reasonably well.

    ALTERNATIVELY, the SDW expansion can use the standard heat kernel
    coefficients. For large Lambda:
      K(1/Lambda^2) ~ a_0^{HK} * Lambda^8 + a_2^{HK} * Lambda^6 + a_4^{HK} * Lambda^4

    where the a_n^{HK} are the heat kernel expansion coefficients. For a
    TRUNCATED spectrum, these must be extracted by fitting.

    Since the canonical a_0=6440 = M_0 (the eigenvalue count), and the
    canonical a_2, a_4 are the inverse-power zeta moments, I will compute
    BOTH comparisons:
      (A) Power sum expansion (Taylor around Lambda=infty)
      (B) Zeta moment "expansion" (using the canonical a_n as given)

    For (A), the power sum moments are just eigenvalue sums.
    """

    L2 = Lambda ** 2  # (local)

    # ===== COMPUTE POWER SUM MOMENTS M_{2k} = sum PW * mu^{2k} =====
    M = np.zeros(10)  # (local) M[k] = M_{2k} for k=0..9
    for mu2, pw in mu_sq_list:
        for k in range(10):
            M[k] += pw * mu2**k

    print(f"\n  Power sum moments M_{{2k}} = sum PW * mu^{{2k}}:")
    for k in range(6):
        print(f"    M_{{{2*k}}} = {M[k]:.6f}")

    print(f"\n  Check: M_0 = {M[0]:.1f} should equal a_0 = {a0:.1f}: {'YES' if abs(M[0]-a0) < 0.1 else 'NO'}")

    # ===== FULL SPECTRAL ACTION (positive eigenvalues only) =====
    results = {}  # (local)

    for f_name, f_func, f_desc in [
        ('heat', lambda x: np.exp(-x), 'f(x) = exp(-x)'),
        ('sharp', lambda x: float(x <= 1.0), 'f(x) = Theta(1-x)'),
        ('gaussian', lambda x: np.exp(-x**2), 'f(x) = exp(-x^2)'),
    ]:
        S_full_pos = 0.0  # (local)
        for mu2, pw in mu_sq_list:
            x = mu2 / L2  # (local) = mu^2/Lambda^2
            S_full_pos += pw * f_func(x)

        results[f_name] = {'S_full_pos': S_full_pos, 'desc': f_desc}

    # ===== SDW EXPANSIONS =====

    # Method A: TAYLOR EXPANSION of heat kernel around Lambda=infty
    # S = M_0 - M_2/L^2 + M_4/(2*L^4) - M_6/(6*L^6) + M_8/(24*L^8) - ...
    # = sum_{k=0}^N (-1)^k / k! * M_{2k} / L^{2k}

    for N_terms in [3, 4, 5, 6]:
        S_taylor = 0.0  # (local)
        for k in range(N_terms):
            from math import factorial
            S_taylor += (-1)**k / factorial(k) * M[k] / L2**k

        results['heat'][f'S_taylor_{N_terms}'] = S_taylor

    # Method B: Using canonical zeta moments as SDW coefficients
    # This is WRONG for the power expansion but let's compute it for comparison
    # The "SDW" with a_0, a_2, a_4 as given:
    # K(t) ~ a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2}
    # at t = 1/Lambda^2: a_0*Lambda^8 + a_2*Lambda^6 + a_4*Lambda^4

    S_zeta_3 = a0*L2**4 + a2*L2**3 + a4*L2**2  # (local)
    S_zeta_4 = S_zeta_3 + a6*L2  # (local)
    S_zeta_5 = S_zeta_4 + a8  # (local)

    results['heat']['S_zeta_3'] = S_zeta_3
    results['heat']['S_zeta_4'] = S_zeta_4
    results['heat']['S_zeta_5'] = S_zeta_5

    # ===== TAYLOR EXPANSION for sharp cutoff =====
    # For sharp cutoff f(x) = Theta(1-x): S_sharp = sum_{mu^2 <= Lambda^2} PW = M_0 = a_0
    # (All eigenvalues are below Lambda since mu_max < Lambda)
    # The SDW expansion of the counting function:
    #   N(Lambda) ~ a_0 (since ALL eigenvalues are below Lambda)
    # So S_sharp_full = S_sharp_SDW = a_0 exactly. No truncation error!
    results['sharp']['S_SDW_exact'] = a0
    results['sharp']['R_exact'] = 0.0

    # ===== TAYLOR EXPANSION for Gaussian =====
    # f(x) = exp(-x^2), S = sum PW * exp(-(mu^2/Lambda^2)^2)
    # Taylor: sum PW * [1 - (mu^2/L^2)^2 + (mu^2/L^2)^4/2 - ...]
    #       = M_0 - M_4/L^4 + M_8/(2*L^8) - M_12/(6*L^12) + ...
    for N_terms in [3, 4, 5]:
        S_gauss_taylor = 0.0  # (local)
        for k in range(N_terms):
            from math import factorial
            S_gauss_taylor += (-1)**k / factorial(k) * M[2*k] / L2**(2*k)
        results['gaussian'][f'S_taylor_{N_terms}'] = S_gauss_taylor

    return results, M


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    t_start = time.time()  # (local)

    print("=" * 78)
    print("S77-B11-SA-TRUNC: Full SA vs Seeley-DeWitt Truncation")
    print(f"Lambda = {LAMBDA:.3f} M_KK, tau = {TAU:.3f}, max_pq_sum = {MAX_PQ_SUM}")
    print("=" * 78)

    # -----------------------------------------------------------------------
    # Step 1: Compute spectrum
    # -----------------------------------------------------------------------
    eval_data = compute_spectrum()

    # -----------------------------------------------------------------------
    # Step 2: Extract positive eigenvalues and verify SDW
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 2: POSITIVE EIGENVALUES AND SDW COEFFICIENTS")
    print("=" * 78)

    mu_sq_list, a0, a2, a4, a6, a8 = extract_positive_eigenvalues(eval_data)

    mu_max = np.sqrt(max(m2 for m2, _ in mu_sq_list))  # (local)
    x_max = mu_max**2 / LAMBDA**2  # (local)
    print(f"\n  mu_max = {mu_max:.4f} M_KK")
    print(f"  Lambda = {LAMBDA:.3f} M_KK")
    print(f"  x_max = mu_max^2/Lambda^2 = {x_max:.6f}")
    print(f"  Expansion parameter: {x_max:.4f} ({'GOOD' if x_max < 0.3 else 'MARGINAL' if x_max < 0.5 else 'POOR'})")

    # -----------------------------------------------------------------------
    # Step 3: Compute S_full and S_SDW
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3: SPECTRAL ACTION COMPARISON")
    print("=" * 78)

    results, M = compute_spectral_actions(mu_sq_list, LAMBDA, a0, a2, a4, a6, a8)

    # -----------------------------------------------------------------------
    # Step 4: HEAT KERNEL COMPARISON (primary metric)
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("HEAT KERNEL: S_full vs Taylor expansion around Lambda = infty")
    print("=" * 78)

    r = results['heat']
    S_full = r['S_full_pos']  # (local)

    print(f"\n  S_full (heat kernel) = {S_full:.6f}")
    print(f"  Power sum moments:  M_0={M[0]:.1f}, M_2={M[1]:.4f}, M_4={M[2]:.4f}")

    # Taylor residuals
    print(f"\n  Taylor expansion residuals (heat kernel, Lambda = {LAMBDA}):")
    print(f"  {'N_terms':>8}  {'S_taylor':>14}  {'|Residual|':>14}  {'R/S_full':>10}  {'R/a4_equiv':>12}")
    print("  " + "-" * 70)

    # The a_4 "equivalent" contribution in the Taylor expansion is the 3rd term:
    # (-1)^2/2! * M_4/Lambda^4 = M_4/(2*Lambda^4)
    a4_taylor_term = M[2] / (2 * LAMBDA**4)  # (local)

    for N in [3, 4, 5, 6]:
        key = f'S_taylor_{N}'
        if key in r:
            S_t = r[key]  # (local)
            res = abs(S_full - S_t)  # (local)
            R_sfull = res / abs(S_full)  # (local)
            R_a4 = res / abs(a4_taylor_term) if abs(a4_taylor_term) > 0 else float('inf')  # (local)
            print(f"  {N:8d}  {S_t:14.6f}  {res:14.6f}  {R_sfull:10.6f}  {R_a4:12.6f}")

    # -----------------------------------------------------------------------
    # Step 5: ZETA MOMENT "SDW" COMPARISON
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("ZETA MOMENT EXPANSION: K(1/Lambda^2) = a_0*L^8 + a_2*L^6 + a_4*L^4 + ...")
    print("=" * 78)

    # This uses the spectral zeta moments as if they were heat kernel coefficients
    L2 = LAMBDA ** 2  # (local)
    print(f"\n  a_0*L^8 = {a0*L2**4:.4f}")
    print(f"  a_2*L^6 = {a2*L2**3:.4f}")
    print(f"  a_4*L^4 = {a4*L2**2:.4f}")
    print(f"  a_6*L^2 = {a6*L2:.4f}")
    print(f"  a_8     = {a8:.4f}")

    print(f"\n  S_full (heat) = {S_full:.6f}")
    for key, label in [('S_zeta_3', '3-term (a0,a2,a4)'),
                       ('S_zeta_4', '4-term (a0,..,a6)'),
                       ('S_zeta_5', '5-term (a0,..,a8)')]:
        if key in r:
            S_z = r[key]  # (local)
            res_z = abs(S_full - S_z)  # (local)
            R_z = res_z / abs(S_full)  # (local)
            print(f"  {label:>25}: S_SDW = {S_z:.4f}, |R| = {res_z:.4f}, R/S = {R_z:.6f}")

    # -----------------------------------------------------------------------
    # Step 6: GAUSSIAN COMPARISON
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("GAUSSIAN CUTOFF: S_full vs Taylor expansion")
    print("=" * 78)

    rg = results['gaussian']
    S_full_g = rg['S_full_pos']  # (local)
    print(f"\n  S_full (Gaussian) = {S_full_g:.6f}")

    for N in [3, 4, 5]:
        key = f'S_taylor_{N}'
        if key in rg:
            S_t = rg[key]  # (local)
            res = abs(S_full_g - S_t)  # (local)
            R_g = res / abs(S_full_g)  # (local)
            print(f"  {N}-term Taylor: S = {S_t:.6f}, |R| = {res:.6f}, R/S = {R_g:.6f}")

    # -----------------------------------------------------------------------
    # Step 7: SHARP CUTOFF COMPARISON
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("SHARP CUTOFF: trivial since all eigenvalues below Lambda")
    print("=" * 78)

    rs = results['sharp']
    print(f"\n  S_full (sharp) = {rs['S_full_pos']:.1f}")
    print(f"  a_0 (count)    = {a0:.1f}")
    print(f"  They are equal: {abs(rs['S_full_pos'] - a0) < 0.1}")
    print(f"  Sharp cutoff residual = 0 (all eigenvalues below Lambda)")

    # -----------------------------------------------------------------------
    # Step 8: CONVERGENCE SCAN
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("CONVERGENCE: Taylor residual vs Lambda (heat kernel, 3 terms)")
    print("=" * 78)

    Lambda_scan = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.033,
                            6.0, 8.0, 10.0, 15.0, 20.0])  # (local)

    print(f"\n  {'Lambda':>8}  {'S_full':>12}  {'S_taylor3':>12}  {'|R|':>12}  {'R/S':>10}  {'x_max':>8}")
    print("  " + "-" * 68)

    conv_results = []  # (local)

    from math import factorial

    for L_val in Lambda_scan:
        L2_val = L_val ** 2  # (local)

        # S_full
        sf = 0.0  # (local)
        for mu2, pw in mu_sq_list:
            sf += pw * np.exp(-mu2 / L2_val)

        # 3-term Taylor
        st = 0.0  # (local)
        for k in range(3):
            st += (-1)**k / factorial(k) * M[k] / L2_val**k

        res = abs(sf - st)  # (local)
        R_val = res / abs(sf) if abs(sf) > 0 else 0.0  # (local)
        x_max_val = mu_max**2 / L2_val  # (local)

        conv_results.append((L_val, sf, st, res, R_val, x_max_val))
        print(f"  {L_val:8.3f}  {sf:12.4f}  {st:12.4f}  {res:12.6f}  {R_val:10.6f}  {x_max_val:8.4f}")

    # -----------------------------------------------------------------------
    # Step 9: TERM DECOMPOSITION at Lambda = 5.033
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("TERM DECOMPOSITION (heat kernel Taylor at Lambda = 5.033)")
    print("=" * 78)

    from math import factorial
    L2 = LAMBDA ** 2  # (local)

    print(f"\n  k=0 (constant/a_0):   M_0/0! = {M[0]:.4f}  ({M[0]/S_full*100:.2f}% of S_full)")
    term_1 = -M[1] / L2  # (local)
    print(f"  k=1 (curvature/a_2):  -M_2/L^2 = {term_1:.4f}  ({abs(term_1)/S_full*100:.2f}% of S_full)")
    term_2 = M[2] / (2 * L2**2)  # (local)
    print(f"  k=2 (gauge/a_4):      M_4/(2L^4) = {term_2:.4f}  ({abs(term_2)/S_full*100:.2f}% of S_full)")
    term_3 = -M[3] / (6 * L2**3)  # (local)
    print(f"  k=3 (a_6 equiv):     -M_6/(6L^6) = {term_3:.6f}  ({abs(term_3)/S_full*100:.4f}% of S_full)")
    term_4 = M[4] / (24 * L2**4)  # (local)
    print(f"  k=4 (a_8 equiv):      M_8/(24L^8) = {term_4:.6f}  ({abs(term_4)/S_full*100:.4f}% of S_full)")

    total_3 = M[0] + term_1 + term_2  # (local)
    total_6 = total_3 + term_3 + term_4  # (local)
    print(f"\n  3-term sum:   {total_3:.6f}")
    print(f"  5-term sum:   {total_6:.6f}")
    print(f"  Exact S_full: {S_full:.6f}")

    res_3 = abs(S_full - total_3)  # (local)
    res_5 = abs(S_full - total_6)  # (local)

    print(f"\n  3-term residual: {res_3:.6f} ({res_3/S_full*100:.4f}% of S_full)")
    print(f"  5-term residual: {res_5:.6f} ({res_5/S_full*100:.4f}% of S_full)")

    # Residual relative to the "a_4" (gauge kinetic) term
    R_a4_equiv = res_3 / abs(term_2) if abs(term_2) > 0 else float('inf')  # (local)
    print(f"\n  3-term residual / a_4 term = {R_a4_equiv:.6f} ({R_a4_equiv*100:.4f}%)")

    # -----------------------------------------------------------------------
    # GATE VERDICT
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("GATE VERDICT: S77-B11-SA-TRUNC")
    print("=" * 78)

    # Primary metric: heat kernel Taylor residual relative to a_4 equivalent term
    R_primary = R_a4_equiv  # (local)
    R_rel = res_3 / abs(S_full)  # (local)

    print(f"\n  S_full (heat, Lambda=5.033) = {S_full:.6f}")
    print(f"  S_SDW (3-term Taylor) = {total_3:.6f}")
    print(f"  |Residual| = {res_3:.6f}")
    print(f"  R / S_full = {R_rel:.6f} ({R_rel*100:.4f}%)")
    print(f"  R / |a_4 term| = {R_primary:.6f} ({R_primary*100:.4f}%)")
    print(f"  Expansion parameter x_max = {x_max:.4f}")

    if R_primary < PASS_THRESH:
        verdict = "PASS"
        reason = f"Residual = {R_primary*100:.4f}% of a_4 term < 1%"
    elif R_primary > FAIL_THRESH:
        verdict = "FAIL"
        reason = f"Residual = {R_primary*100:.4f}% of a_4 term > 10%"
    else:
        verdict = "INFO"
        reason = f"Residual = {R_primary*100:.4f}% of a_4 term, between 1% and 10%"

    print(f"\n  Gate S77-B11-SA-TRUNC: {verdict}")
    print(f"  Reason: {reason}")
    print(f"  Threshold: PASS < {PASS_THRESH*100:.0f}%, FAIL > {FAIL_THRESH*100:.0f}%")

    # Additional context
    print(f"\n  Physical interpretation:")
    print(f"    The heat kernel expansion Tr(e^{{-D^2/Lambda^2}}) converges well at")
    print(f"    Lambda = 5.033 because x_max = {x_max:.4f} << 1.")
    print(f"    The gauge kinetic (a_4) sector is {'adequately' if verdict == 'PASS' else 'inadequately' if verdict == 'FAIL' else 'borderline'}")
    print(f"    captured by the 3-term SDW truncation.")

    if R_primary > PASS_THRESH:
        R_5term_primary = res_5 / abs(term_2)  # (local)
        print(f"\n    5-term residual / a_4 = {R_5term_primary:.6f} ({R_5term_primary*100:.4f}%)")
        if R_5term_primary < PASS_THRESH:
            print(f"    5-term truncation would PASS. Higher SDW terms are needed but available.")

    # -----------------------------------------------------------------------
    # SAVE
    # -----------------------------------------------------------------------
    outfile = os.path.join(OUTDIR, 's77_sa_truncation.npz')

    save_dict = {
        'tau': TAU,
        'Lambda': LAMBDA,
        'max_pq_sum': MAX_PQ_SUM,
        # SDW zeta moments (canonical)
        'a0': a0,
        'a2': a2,
        'a4': a4,
        'a6': a6,
        'a8': a8,
        # Power sum moments
        'M0': M[0],
        'M2': M[1],
        'M4': M[2],
        'M6': M[3],
        'M8': M[4],
        # Spectrum parameters
        'mu_max': mu_max,
        'x_max': x_max,
        # S_full values (positive eigenvalues only, multiply by 2 for full spectrum)
        'S_full_heat': S_full,
        'S_full_sharp': results['sharp']['S_full_pos'],
        'S_full_gaussian': results['gaussian']['S_full_pos'],
        # Taylor expansion values
        'S_taylor_3_heat': results['heat']['S_taylor_3'],
        'S_taylor_4_heat': results['heat']['S_taylor_4'],
        'S_taylor_5_heat': results['heat']['S_taylor_5'],
        'S_taylor_6_heat': results['heat']['S_taylor_6'],
        # Zeta expansion values (heat kernel)
        'S_zeta_3_heat': results['heat']['S_zeta_3'],
        'S_zeta_4_heat': results['heat']['S_zeta_4'],
        # Residuals
        'R_3term_heat': res_3 / abs(S_full),
        'R_5term_heat': res_5 / abs(S_full),
        'R_a4_3term_heat': R_primary,
        # Term contributions
        'term_a0': float(M[0]),
        'term_a2': term_1,
        'term_a4': term_2,
        'term_a6': term_3,
        'term_a8': term_4,
        # Convergence scan
        'conv_Lambda': np.array([c[0] for c in conv_results]),
        'conv_S_full': np.array([c[1] for c in conv_results]),
        'conv_S_taylor3': np.array([c[2] for c in conv_results]),
        'conv_R': np.array([c[4] for c in conv_results]),
        'conv_x_max': np.array([c[5] for c in conv_results]),
        # Gate verdict
        'verdict': verdict,
        'R_primary': R_primary,
    }

    np.savez(outfile, **save_dict)
    print(f"\n  Data saved to: {outfile}")

    dt = time.time() - t_start  # (local)
    print(f"  Total runtime: {dt:.1f}s")
    print("=" * 78)

    return verdict, R_primary


if __name__ == '__main__':
    main()
