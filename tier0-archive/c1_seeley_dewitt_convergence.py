"""
C-1: SEELEY-DEWITT CONVERGENCE ASSESSMENT
==========================================

Connes NCG Theorist — Session 18
Date: 2026-02-14

PURPOSE: Determine whether the perturbative (heat kernel / Coleman-Weinberg)
expansion is reliable at the current truncation level max_pq_sum = 6, and
whether pushing to 8 or 10 would change the physics.

THREE DIAGNOSTICS:

1. HEAT KERNEL COEFFICIENTS vs TRUNCATION ORDER
   Compute a_0, a_2, a_4 at max_pq_sum = 3, 4, 5, 6
   by fitting t^4 * K(t) to polynomial in t.
   Convergence = coefficients stabilize.

2. SPECTRAL ZETA FUNCTION CONVERGENCE
   Compute zeta_D(z) = sum dim(p,q) * sum_j |lambda_j|^{-2z}
   at several s values. Determine effective abscissa of convergence
   for the truncated spectrum and compare to d/2 = 4 (the exact value).

3. CW TRUNCATION CONVERGENCE
   Run the Coleman-Weinberg potential at max_pq_sum = 3, 4, 5, 6.
   Track minimum location, depth, and curvature.
   Does the minimum shift stabilize?

MATHEMATICAL BACKGROUND (Connes):
The spectral action S = Tr f(D^2/Lambda^2) has the asymptotic expansion
    S ~ sum_{n >= 0} f_{4-n} a_{2n}(D^2)
where f_k = integral_0^infty f(v) v^{k-1} dv are the momenta of the test function
and a_{2n} are the Seeley-DeWitt coefficients. For a COMPACT manifold of dim d=8:
    K(t) = Tr(e^{-tD^2}) ~ sum_{n>=0} a_{2n} t^{(2n-d)/2}
         = a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + a_6 t^{-1} + a_8 + O(t)

The a_{2n} are LOCAL geometric invariants:
    a_0 = (4pi)^{-d/2} * rank(S) * Vol(M, g)
    a_2 = (4pi)^{-d/2} * (R/6) * rank(S) * Vol(M, g)
    a_4 involves R^2, Ric^2, Riem^2, and gauge field strengths

For a TRUNCATED spectrum (finite max_pq_sum), the heat kernel is an entire
function of t (no singularities at t=0). The polynomial fit extracts
APPROXIMATE a_{2n} that converge to the true values as max_pq_sum -> infinity.

The rate of convergence depends on the TAIL of the spectrum: how much spectral
weight lies beyond our cutoff. Weyl's law for dim=8 gives
    N(Lambda) ~ C * Lambda^8
so the eigenvalue density grows as Lambda^7. This means each additional
irrep shell adds O((max_pq_sum)^7) eigenvalues -- convergence should be
polynomial, not exponential.

Author: Connes NCG Theorist Agent
References:
  - Chamseddine, Connes (1997): The Spectral Action Principle [Paper 07]
  - Chamseddine, Connes, Marcolli (2007): Gravity and the SM [Paper 10]
  - Gilkey (1995): Invariance Theory
"""

import numpy as np
import sys
import os
import time

# Add tier0-computation to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    collect_spectrum, get_irrep, dirac_operator_on_irrep,
)
from tier1_spectral_action import (
    dim_su3_irrep, peter_weyl_degeneracy,
    compute_heat_kernel, extract_seeley_dewitt,
    spectral_zeta, spectral_action_smooth_cutoff,
)
from tier1_coleman_weinberg import (
    V_tree, V_CW_boson, compute_fermionic_CW_nf,
    find_minima,
)


# =============================================================================
# INFRASTRUCTURE: Build SU(3) algebra once
# =============================================================================

def build_infrastructure():
    """Build all reusable SU(3) infrastructure."""
    print("Building SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()
    validate_clifford(gammas)
    print("  Infrastructure ready: 8 generators, Cliff(8) validated.")
    return gens, f_abc, B_ab, gammas


# =============================================================================
# DIAGNOSTIC 1: HEAT KERNEL COEFFICIENTS vs TRUNCATION ORDER
# =============================================================================

def diagnostic_1_heat_kernel_convergence(gens, f_abc, gammas,
                                          s_values=[0.0, 0.15, 0.30, 0.50, 1.0],
                                          max_pq_sums=[3, 4, 5, 6]):
    """
    Compute Seeley-DeWitt coefficients at successive truncation orders.

    For each s and each max_pq_sum, compute the Dirac spectrum and extract
    a_0, a_2, a_4 via polynomial fit of t^4 * K(t).

    Returns:
        results: dict[s][max_pq_sum] -> {a_0, a_2, a_4, n_eigenvalues, spectrum_data}
    """
    print("\n" + "="*72)
    print("DIAGNOSTIC 1: HEAT KERNEL COEFFICIENTS vs TRUNCATION ORDER")
    print("="*72)

    results = {}
    t0_total = time.time()

    for s in s_values:
        results[s] = {}
        print(f"\n  s = {s:.2f}:")

        for mps in max_pq_sums:
            t0 = time.time()
            _, eval_data = collect_spectrum(
                s, gens, f_abc, gammas, max_pq_sum=mps, verbose=False
            )
            t_spec = time.time() - t0

            # Count total eigenvalues (with PW weight)
            n_evals_raw = sum(len(evals) for _, _, evals in eval_data)
            n_evals_weighted = sum(dim_su3_irrep(p, q) * len(evals)
                                   for p, q, evals in eval_data)
            n_sectors = len(eval_data)

            # Extract Seeley-DeWitt coefficients
            # Use a robust t-range: small enough for asymptotic regime,
            # large enough that truncation doesn't cause oscillations
            coeffs, fit_quality = extract_seeley_dewitt(
                eval_data, t_range=(0.005, 0.3), n_points=200,
                n_coeffs=4, verbose=False
            )

            # Also extract with a second t-range for consistency check
            coeffs2, fit2 = extract_seeley_dewitt(
                eval_data, t_range=(0.01, 0.5), n_points=200,
                n_coeffs=4, verbose=False
            )

            # Compute spectral action at Lambda = 1.0 for cross-check
            S_heat, _ = spectral_action_smooth_cutoff(eval_data, Lambda=1.0, f_type='heat')
            S_sharp, _ = spectral_action_smooth_cutoff(eval_data, Lambda=1.0, f_type='sharp')

            results[s][mps] = {
                'a_0': coeffs.get('a_0', 0),
                'a_2': coeffs.get('a_2', 0),
                'a_4': coeffs.get('a_4', 0),
                'a_6': coeffs.get('a_6', 0),
                'a_0_alt': coeffs2.get('a_0', 0),
                'a_2_alt': coeffs2.get('a_2', 0),
                'a_4_alt': coeffs2.get('a_4', 0),
                'fit_residual': fit_quality['residual'],
                'fit_residual_alt': fit2['residual'],
                'n_evals_raw': n_evals_raw,
                'n_evals_weighted': n_evals_weighted,
                'n_sectors': n_sectors,
                'S_heat': S_heat,
                'S_sharp': S_sharp,
                'eval_data': eval_data,
                'compute_time': t_spec,
            }

            print(f"    max_pq_sum={mps}: {n_sectors} sectors, "
                  f"{n_evals_raw} raw/{n_evals_weighted} weighted evals, "
                  f"a_0={coeffs['a_0']:.4e}, a_2={coeffs['a_2']:.4e}, "
                  f"a_4={coeffs['a_4']:.4e}, "
                  f"fit_res={fit_quality['residual']:.2e}, "
                  f"time={t_spec:.1f}s")

    t_total = time.time() - t0_total
    print(f"\n  Total time for Diagnostic 1: {t_total:.1f}s")

    # Convergence analysis
    print("\n  CONVERGENCE TABLE:")
    print(f"  {'s':>5} {'coeff':>5} ", end="")
    for mps in max_pq_sums:
        print(f" {'mps='+str(mps):>12}", end="")
    print(f"  {'delta_56':>10} {'delta_45':>10} {'ratio':>8}")

    for s in s_values:
        for cname in ['a_0', 'a_2', 'a_4']:
            vals = [results[s][mps][cname] for mps in max_pq_sums]
            print(f"  {s:5.2f} {cname:>5} ", end="")
            for v in vals:
                print(f" {v:12.4e}", end="")

            # Compute successive differences
            if len(vals) >= 3:
                d56 = vals[-1] - vals[-2]  # 5->6
                d45 = vals[-2] - vals[-3]  # 4->5
                if abs(d45) > 1e-20:
                    ratio = d56 / d45
                else:
                    ratio = float('nan')
                print(f"  {d56:10.2e} {d45:10.2e} {ratio:8.3f}")
            else:
                print()

    return results


# =============================================================================
# DIAGNOSTIC 2: SPECTRAL ZETA FUNCTION CONVERGENCE
# =============================================================================

def diagnostic_2_spectral_zeta(diag1_results,
                                s_values=[0.0, 0.15, 0.30, 0.50, 1.0],
                                max_pq_sums=[3, 4, 5, 6]):
    """
    Compute the spectral zeta function and assess convergence.

    For dim=8 compact manifold, the abscissa of convergence is d/2 = 4.
    With a truncated spectrum, the sum is finite and converges everywhere,
    but we can measure how rapidly zeta_D(z) grows as z -> 4 from above.

    Key quantity: the Weyl exponent alpha from
        zeta_D(z) ~ C / (z - alpha)  as z -> alpha^+

    For the FULL spectrum, alpha = 4. For truncated spectrum, alpha < 4
    (no true pole). The difference 4 - alpha_eff measures how much spectrum
    is missing.

    Returns:
        zeta_results: dict[s][max_pq_sum] -> {z_values, zeta_values, alpha_eff}
    """
    print("\n" + "="*72)
    print("DIAGNOSTIC 2: SPECTRAL ZETA FUNCTION CONVERGENCE")
    print("="*72)

    z_values = np.linspace(1.0, 8.0, 141)  # include below d/2=4 for truncated
    zeta_results = {}

    for s in s_values:
        zeta_results[s] = {}
        print(f"\n  s = {s:.2f}:")

        for mps in max_pq_sums:
            eval_data = diag1_results[s][mps]['eval_data']

            # Compute zeta function
            zeta_vals = spectral_zeta(eval_data, z_values)

            # Find effective abscissa: where does zeta start to diverge?
            # For truncated spectrum, zeta is finite everywhere, but it
            # grows rapidly as z -> alpha_eff. Measure alpha_eff by finding
            # where d(log zeta)/dz is maximally negative.
            log_zeta = np.log(np.maximum(zeta_vals, 1e-300))
            dlog = np.gradient(log_zeta, z_values[1] - z_values[0])

            # The most negative slope gives the "would-be pole"
            idx_min_slope = np.argmin(dlog)
            alpha_eff = z_values[idx_min_slope]

            # Weyl law check: zeta_D(z) ~ C * Lambda_max^{d-2z} / (d - 2z)
            # for truncated spectrum with max eigenvalue Lambda_max.
            # Find Lambda_max
            all_abs = []
            for p, q, evals in eval_data:
                all_abs.extend(np.abs(evals))
            lambda_max = max(all_abs) if all_abs else 1.0

            # At z=4 (d/2), the true zeta has a pole. Truncated value is:
            zeta_at_4 = spectral_zeta(eval_data, [4.0])[0]

            # Eigenvalue count for Weyl check
            n_evals = diag1_results[s][mps]['n_evals_weighted']

            zeta_results[s][mps] = {
                'z_values': z_values,
                'zeta_values': zeta_vals,
                'alpha_eff': alpha_eff,
                'lambda_max': lambda_max,
                'zeta_at_4': zeta_at_4,
                'dlog_dz': dlog,
            }

            print(f"    max_pq_sum={mps}: lambda_max={lambda_max:.3f}, "
                  f"alpha_eff={alpha_eff:.2f}, "
                  f"zeta(4)={zeta_at_4:.4e}, "
                  f"zeta(5)={spectral_zeta(eval_data, [5.0])[0]:.4e}")

    # Summary table
    print("\n  ZETA CONVERGENCE TABLE:")
    print(f"  {'s':>5}", end="")
    for mps in max_pq_sums:
        print(f"  alpha_eff({mps})", end="")
    for mps in max_pq_sums:
        print(f"  zeta(4,{mps})", end="")
    print()

    for s in s_values:
        print(f"  {s:5.2f}", end="")
        for mps in max_pq_sums:
            print(f"  {zeta_results[s][mps]['alpha_eff']:13.2f}", end="")
        for mps in max_pq_sums:
            print(f"  {zeta_results[s][mps]['zeta_at_4']:11.2e}", end="")
        print()

    # Weyl law verification
    print("\n  WEYL LAW CHECK:")
    print(f"  For dim=8: N(Lambda) ~ C * Lambda^8")
    print("  Effective: zeta(z) = sum |lambda|^{-2z} ~ integral_0^{Lambda_max} "
          "rho(lambda) lambda^{-2z} dlambda")
    print("  With rho ~ lambda^7 (Weyl), integral ~ Lambda_max^{8-2z}/(8-2z)")
    print("  So zeta(z) ~ Lambda_max^{8-2z} -- finite for all z with truncation.")

    for s in s_values:
        print(f"\n  s={s:.2f}:")
        for mps in max_pq_sums:
            r = zeta_results[s][mps]
            lm = r['lambda_max']
            # Predicted: zeta(5) / zeta(6) ~ lm^{-2} (if Weyl holds)
            z5 = spectral_zeta(diag1_results[s][mps]['eval_data'], [5.0])[0]
            z6 = spectral_zeta(diag1_results[s][mps]['eval_data'], [6.0])[0]
            if z6 > 1e-30:
                ratio_predicted = lm**(-2)
                ratio_actual = z6 / z5
                # Actually: zeta(z) ~ lm^{8-2z}, so zeta(6)/zeta(5) ~ lm^{-2}
                print(f"    mps={mps}: lm={lm:.2f}, "
                      f"zeta(6)/zeta(5) = {ratio_actual:.4f} "
                      f"vs Weyl pred lm^{{-2}} = {ratio_predicted:.4f} "
                      f"(ratio = {ratio_actual/ratio_predicted:.3f})")

    return zeta_results


# =============================================================================
# DIAGNOSTIC 3: CW TRUNCATION CONVERGENCE
# =============================================================================

def diagnostic_3_cw_convergence(gens, f_abc, gammas,
                                 max_pq_sums=[3, 4, 5, 6],
                                 mu_sq_values=[0.1, 1.0, 10.0],
                                 n_f_values=[1, 4],
                                 n_s=81, s_range=(0.0, 2.0)):
    """
    Run Coleman-Weinberg V_eff at each truncation order and track the minimum.

    For each (mu_sq, n_f, max_pq_sum), compute V_eff(s) and find minima.
    The key question: does s_min and V''(s_min) stabilize?

    Returns:
        cw_results: dict[(mu_sq, n_f)][max_pq_sum] -> {s_values, V_total, minima, ...}
    """
    print("\n" + "="*72)
    print("DIAGNOSTIC 3: COLEMAN-WEINBERG TRUNCATION CONVERGENCE")
    print("="*72)

    s_values = np.linspace(s_range[0], s_range[1], n_s)
    cw_results = {}
    t0_total = time.time()

    # Pre-compute all eigenvalue data at all s and all truncations
    # This is the expensive part
    print(f"\n  Pre-computing Dirac spectra at {n_s} s-values x {len(max_pq_sums)} truncations...")
    eval_cache = {}  # (s_idx, mps) -> eval_data

    for mps in max_pq_sums:
        t0 = time.time()
        for i, s in enumerate(s_values):
            _, eval_data = collect_spectrum(
                s, gens, f_abc, gammas, max_pq_sum=mps, verbose=False
            )
            eval_cache[(i, mps)] = eval_data
        t_mps = time.time() - t0
        print(f"    max_pq_sum={mps}: {t_mps:.1f}s ({t_mps/n_s:.2f}s/point)")

    t_precompute = time.time() - t0_total
    print(f"  Total pre-computation: {t_precompute:.1f}s")

    # Now sweep parameters
    print(f"\n  Sweeping {len(mu_sq_values)} mu^2 x {len(n_f_values)} n_f "
          f"x {len(max_pq_sums)} truncations...")

    for mu_sq in mu_sq_values:
        for n_f in n_f_values:
            key = (mu_sq, n_f)
            cw_results[key] = {}

            for mps in max_pq_sums:
                # Compute V_eff at all s values
                V_tree_arr = np.array([float(np.squeeze(V_tree(s))) for s in s_values])

                V_boson_arr = np.array([float(np.squeeze(
                    V_CW_boson(np.atleast_1d(s), mu_sq, c_b=5.0/6.0, n_b=4)
                )) for s in s_values])

                V_fermion_arr = np.zeros(n_s)
                for i in range(n_s):
                    Vf, _ = compute_fermionic_CW_nf(
                        eval_cache[(i, mps)], n_f, mu_sq, c_f=3.0/2.0
                    )
                    V_fermion_arr[i] = Vf

                V_total = V_tree_arr + V_boson_arr + V_fermion_arr

                # Find minima
                minima = find_minima(s_values, V_total, verbose=False)

                # Store
                cw_results[key][mps] = {
                    's_values': s_values,
                    'V_tree': V_tree_arr,
                    'V_boson': V_boson_arr,
                    'V_fermion': V_fermion_arr,
                    'V_total': V_total,
                    'minima': minima,
                    'has_minimum': len(minima) > 0,
                }

    # Print convergence table
    print("\n  CW MINIMUM CONVERGENCE TABLE:")
    print(f"  {'mu^2':>6} {'n_f':>3} ", end="")
    for mps in max_pq_sums:
        print(f" {'s_min('+str(mps)+')':>12}", end="")
    print(f"  {'delta s':>10} {'converged':>10}")

    for mu_sq in mu_sq_values:
        for n_f in n_f_values:
            key = (mu_sq, n_f)
            print(f"  {mu_sq:6.1f} {n_f:3d} ", end="")

            s_mins = []
            for mps in max_pq_sums:
                minima = cw_results[key][mps]['minima']
                if minima:
                    best = min(minima, key=lambda m: m['V_min'])
                    s_min = best['s_min']
                    s_mins.append(s_min)
                    print(f" {s_min:12.6f}", end="")
                else:
                    s_mins.append(None)
                    print(f" {'monotonic':>12}", end="")

            # Convergence: delta between last two truncations
            if s_mins[-1] is not None and s_mins[-2] is not None:
                delta = abs(s_mins[-1] - s_mins[-2])
                converged = "YES" if delta < 0.01 else ("MARGINAL" if delta < 0.05 else "NO")
                print(f"  {delta:10.4f} {converged:>10}")
            else:
                print(f"  {'---':>10} {'---':>10}")

    # V_fermion magnitude comparison across truncations
    print("\n  V_FERMION MAGNITUDE AT s=1.0 vs TRUNCATION:")
    s1_idx = np.argmin(np.abs(s_values - 1.0))
    for mu_sq in mu_sq_values:
        for n_f in n_f_values:
            key = (mu_sq, n_f)
            print(f"    mu^2={mu_sq:.1f}, n_f={n_f}: ", end="")
            vals = []
            for mps in max_pq_sums:
                vf = cw_results[key][mps]['V_fermion'][s1_idx]
                vals.append(vf)
                print(f"  mps={mps}: {vf:.4e}", end="")
            if len(vals) >= 2 and abs(vals[-2]) > 1e-30:
                rel_change = abs(vals[-1] - vals[-2]) / abs(vals[-2])
                print(f"  rel_change(5->6)={rel_change:.4f}")
            else:
                print()

    return cw_results


# =============================================================================
# DIAGNOSTIC 4: EIGENVALUE COUNT AND WEYL LAW
# =============================================================================

def diagnostic_4_weyl_law(diag1_results,
                           s_values=[0.0, 0.15, 0.30, 0.50, 1.0],
                           max_pq_sums=[3, 4, 5, 6]):
    """
    Check Weyl's law: N(Lambda) ~ C * Lambda^d for d=8.

    For each truncation, compute the effective Weyl exponent from the
    eigenvalue counting function. If the truncated spectrum already
    has Weyl-law growth, the heat kernel expansion is well-conditioned.

    Returns:
        weyl_results: dict
    """
    print("\n" + "="*72)
    print("DIAGNOSTIC 4: WEYL LAW AND SPECTRAL GROWTH")
    print("="*72)

    weyl_results = {}

    for s in s_values:
        weyl_results[s] = {}
        print(f"\n  s = {s:.2f}:")

        for mps in max_pq_sums:
            eval_data = diag1_results[s][mps]['eval_data']

            # Collect all eigenvalue magnitudes with PW weight
            all_abs_weighted = []
            for p, q, evals in eval_data:
                d_pq = dim_su3_irrep(p, q)
                for ev in evals:
                    all_abs_weighted.extend([abs(ev)] * d_pq)

            all_abs_weighted = np.sort(all_abs_weighted)
            N_total = len(all_abs_weighted)

            # Remove zeros
            nonzero = all_abs_weighted[all_abs_weighted > 1e-12]
            N_nonzero = len(nonzero)

            # Eigenvalue counting function N(Lambda)
            if N_nonzero > 10:
                lambda_max = nonzero[-1]
                lambda_min = nonzero[0]

                # Fit log N vs log Lambda for Weyl exponent
                # Use the upper half of the spectrum for better fit
                mid = N_nonzero // 2
                lambdas_upper = nonzero[mid:]
                N_upper = np.arange(mid + 1, N_nonzero + 1)

                if len(lambdas_upper) > 2:
                    log_lam = np.log(lambdas_upper)
                    log_N = np.log(N_upper)
                    # Linear fit: log N = alpha * log Lambda + beta
                    coeffs = np.polyfit(log_lam, log_N, 1)
                    alpha_weyl = coeffs[0]
                else:
                    alpha_weyl = float('nan')

                # Spectral dimension from return probability
                # P(t) = Tr(e^{-tD^2}) ~ t^{-d_s/2}
                # d_s = -2 d(log P)/d(log t)
                t_test = np.array([0.01, 0.02, 0.05, 0.1])
                K_test, _ = compute_heat_kernel(eval_data, t_test)
                if np.all(K_test > 0):
                    log_K = np.log(K_test)
                    log_t = np.log(t_test)
                    d_s_coeffs = np.polyfit(log_t, log_K, 1)
                    d_spectral = -2 * d_s_coeffs[0]
                else:
                    d_spectral = float('nan')
            else:
                lambda_max = 0
                lambda_min = 0
                alpha_weyl = float('nan')
                d_spectral = float('nan')

            weyl_results[s][mps] = {
                'N_total': N_total,
                'N_nonzero': N_nonzero,
                'lambda_max': lambda_max,
                'lambda_min': lambda_min if N_nonzero > 0 else 0,
                'alpha_weyl': alpha_weyl,
                'd_spectral': d_spectral,
            }

            print(f"    mps={mps}: N={N_total} (nonzero={N_nonzero}), "
                  f"lambda in [{lambda_min:.3f}, {lambda_max:.3f}], "
                  f"Weyl alpha={alpha_weyl:.2f} (expected 8), "
                  f"d_spectral={d_spectral:.2f} (expected 8)")

    return weyl_results


# =============================================================================
# DIAGNOSTIC 5: RATIO STABILITY (PHYSICS-RELEVANT)
# =============================================================================

def diagnostic_5_ratio_stability(diag1_results,
                                  s_values=[0.0, 0.15, 0.30, 0.50, 1.0],
                                  max_pq_sums=[3, 4, 5, 6]):
    """
    Check stability of RATIOS of Seeley-DeWitt coefficients.

    Ratios like a_2/a_0 and a_4/a_0 have physical meaning:
      a_2/a_0 ~ R * Vol / Vol = R  (scalar curvature, up to constants)
      a_4/a_0 ~ gauge coupling strength

    Even if individual coefficients haven't converged, ratios may have.
    This is the most physics-relevant diagnostic.

    Returns:
        ratio_results: dict
    """
    print("\n" + "="*72)
    print("DIAGNOSTIC 5: COEFFICIENT RATIO STABILITY")
    print("="*72)

    print(f"\n  Physics: a_2/a_0 encodes R (scalar curvature relative to volume)")
    print(f"           a_4/a_0 encodes gauge couplings")
    print(f"           a_4/a_2 encodes gauge/gravity ratio")
    print(f"  Ratios should converge FASTER than individual coefficients.")

    ratio_results = {}

    print(f"\n  {'s':>5} {'ratio':>10}", end="")
    for mps in max_pq_sums:
        print(f" {'mps='+str(mps):>12}", end="")
    print(f"  {'rel_chg(5->6)':>14}")

    for s in s_values:
        ratio_results[s] = {}

        for rname, num_key, den_key in [('a_2/a_0', 'a_2', 'a_0'),
                                          ('a_4/a_0', 'a_4', 'a_0'),
                                          ('a_4/a_2', 'a_4', 'a_2')]:
            vals = []
            for mps in max_pq_sums:
                r = diag1_results[s][mps]
                den = r[den_key]
                if abs(den) > 1e-30:
                    ratio_val = r[num_key] / den
                else:
                    ratio_val = float('nan')
                vals.append(ratio_val)

            ratio_results[s][rname] = vals

            print(f"  {s:5.2f} {rname:>10}", end="")
            for v in vals:
                if np.isfinite(v):
                    print(f" {v:12.4e}", end="")
                else:
                    print(f" {'nan':>12}", end="")

            if len(vals) >= 2 and np.isfinite(vals[-1]) and np.isfinite(vals[-2]):
                if abs(vals[-2]) > 1e-30:
                    rel_chg = abs(vals[-1] - vals[-2]) / abs(vals[-2])
                    print(f"  {rel_chg:14.6f}")
                else:
                    print(f"  {'---':>14}")
            else:
                print()

    return ratio_results


# =============================================================================
# FINAL VERDICT
# =============================================================================

def convergence_verdict(diag1, diag2, diag3, diag4, diag5,
                        s_values, max_pq_sums):
    """
    Synthesize all diagnostics into a final convergence verdict.
    """
    print("\n" + "="*72)
    print("FINAL CONVERGENCE VERDICT")
    print("="*72)

    # 1. Heat kernel coefficient stability
    print("\n  1. HEAT KERNEL COEFFICIENTS:")
    max_rel_change_a0 = 0
    max_rel_change_a2 = 0
    max_rel_change_a4 = 0
    for s in s_values:
        for cname, tracker in [('a_0', 'max_rel_change_a0'),
                                 ('a_2', 'max_rel_change_a2'),
                                 ('a_4', 'max_rel_change_a4')]:
            v5 = diag1[s][max_pq_sums[-2]][cname]
            v6 = diag1[s][max_pq_sums[-1]][cname]
            if abs(v5) > 1e-30:
                rc = abs(v6 - v5) / abs(v5)
                if cname == 'a_0':
                    max_rel_change_a0 = max(max_rel_change_a0, rc)
                elif cname == 'a_2':
                    max_rel_change_a2 = max(max_rel_change_a2, rc)
                elif cname == 'a_4':
                    max_rel_change_a4 = max(max_rel_change_a4, rc)

    print(f"     Max relative change (mps 5->6):")
    print(f"       a_0: {max_rel_change_a0:.4f}")
    print(f"       a_2: {max_rel_change_a2:.4f}")
    print(f"       a_4: {max_rel_change_a4:.4f}")
    hk_converged = max_rel_change_a0 < 0.1 and max_rel_change_a2 < 0.2
    print(f"     Verdict: {'CONVERGED' if hk_converged else 'NOT CONVERGED'} "
          f"(threshold: <10% for a_0, <20% for a_2)")

    # 2. Spectral dimension
    print("\n  2. SPECTRAL DIMENSION:")
    d_spec_vals = [diag4[s][max_pq_sums[-1]]['d_spectral'] for s in s_values]
    mean_d_spec = np.nanmean(d_spec_vals)
    print(f"     Spectral dimension at mps=6: {mean_d_spec:.2f} (expected: 8)")
    print(f"     Individual: {', '.join(f'{d:.2f}' for d in d_spec_vals)}")
    d_ok = abs(mean_d_spec - 8) < 2
    print(f"     Verdict: {'OK' if d_ok else 'POOR'}")

    # 3. CW minimum stability
    print("\n  3. CW MINIMUM STABILITY:")
    n_stable = 0
    n_total = 0
    for key in diag3:
        minima_5 = diag3[key].get(max_pq_sums[-2], {}).get('minima', [])
        minima_6 = diag3[key].get(max_pq_sums[-1], {}).get('minima', [])
        n_total += 1

        if minima_5 and minima_6:
            s5 = min(minima_5, key=lambda m: m['V_min'])['s_min']
            s6 = min(minima_6, key=lambda m: m['V_min'])['s_min']
            delta = abs(s6 - s5)
            if delta < 0.05:
                n_stable += 1
        elif not minima_5 and not minima_6:
            n_stable += 1  # both monotonic = stable

    print(f"     Stable minima (|delta s| < 0.05): {n_stable}/{n_total}")
    cw_stable = n_stable > n_total * 0.5
    print(f"     Verdict: {'STABLE' if cw_stable else 'UNSTABLE'}")

    # 4. Ratio convergence
    print("\n  4. RATIO CONVERGENCE (physics-relevant):")
    max_ratio_change = 0
    for s in s_values:
        for rname in ['a_2/a_0', 'a_4/a_0']:
            vals = diag5[s][rname]
            if len(vals) >= 2 and np.isfinite(vals[-1]) and np.isfinite(vals[-2]):
                if abs(vals[-2]) > 1e-30:
                    rc = abs(vals[-1] - vals[-2]) / abs(vals[-2])
                    max_ratio_change = max(max_ratio_change, rc)
    print(f"     Max ratio relative change (5->6): {max_ratio_change:.4f}")
    ratio_ok = max_ratio_change < 0.15
    print(f"     Verdict: {'CONVERGED' if ratio_ok else 'NOT CONVERGED'} (threshold: <15%)")

    # 5. Weyl exponent
    print("\n  5. WEYL LAW:")
    alpha_vals = [diag4[s][max_pq_sums[-1]]['alpha_weyl'] for s in s_values]
    mean_alpha = np.nanmean(alpha_vals)
    print(f"     Mean Weyl exponent at mps=6: {mean_alpha:.2f} (expected: 8)")
    weyl_ok = abs(mean_alpha - 8) < 3

    # OVERALL
    print("\n  " + "-"*60)
    scores = [hk_converged, d_ok, cw_stable, ratio_ok]
    n_pass = sum(scores)
    print(f"  OVERALL: {n_pass}/4 diagnostics pass")

    if n_pass >= 3:
        print(f"  RECOMMENDATION: max_pq_sum=6 is ADEQUATE for qualitative V_eff.")
        print(f"  Pushing to 8 would refine coefficients by ~{max_rel_change_a0*100:.0f}%.")
        print(f"  Cost: ~4x more compute per s-point (from irrep count growth).")
        recommend_push = False
    elif n_pass >= 2:
        print(f"  RECOMMENDATION: max_pq_sum=6 gives INDICATIVE results.")
        print(f"  Pushing to 8 is RECOMMENDED for quantitative conclusions.")
        recommend_push = True
    else:
        print(f"  RECOMMENDATION: Expansion NOT CONVERGED at max_pq_sum=6.")
        print(f"  Pushing to 8+ is ESSENTIAL. Results at 6 are unreliable.")
        recommend_push = True

    # Estimate cost of pushing to 8
    # Number of irreps: sum_{p+q <= N} 1 = N(N+1)/2 + N + 1
    n_irreps_6 = sum(1 for p in range(7) for q in range(7-p))
    n_irreps_8 = sum(1 for p in range(9) for q in range(9-p))
    n_irreps_10 = sum(1 for p in range(11) for q in range(11-p))

    # Compute time scales with n_irreps * (dim_irrep * 16)^2
    # Rough: proportional to sum of dim(p,q)^2
    total_dim2_6 = sum(dim_su3_irrep(p, q)**2 for p in range(7) for q in range(7-p))
    total_dim2_8 = sum(dim_su3_irrep(p, q)**2 for p in range(9) for q in range(9-p))
    total_dim2_10 = sum(dim_su3_irrep(p, q)**2 for p in range(11) for q in range(11-p))

    print(f"\n  COST ESTIMATE:")
    print(f"    max_pq_sum=6: {n_irreps_6} irreps, total dim^2 = {total_dim2_6}")
    print(f"    max_pq_sum=8: {n_irreps_8} irreps, total dim^2 = {total_dim2_8}, "
          f"ratio = {total_dim2_8/total_dim2_6:.1f}x")
    print(f"    max_pq_sum=10: {n_irreps_10} irreps, total dim^2 = {total_dim2_10}, "
          f"ratio = {total_dim2_10/total_dim2_6:.1f}x")

    return {
        'hk_converged': hk_converged,
        'd_ok': d_ok,
        'cw_stable': cw_stable,
        'ratio_ok': ratio_ok,
        'n_pass': n_pass,
        'recommend_push': recommend_push,
        'max_rel_change_a0': max_rel_change_a0,
        'max_rel_change_a2': max_rel_change_a2,
        'max_rel_change_a4': max_rel_change_a4,
        'max_ratio_change': max_ratio_change,
        'mean_d_spectral': mean_d_spec,
    }


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("="*72)
    print("C-1: SEELEY-DEWITT CONVERGENCE ASSESSMENT")
    print("Connes NCG Theorist — Session 18")
    print("="*72)

    t0_global = time.time()

    # Build infrastructure
    gens, f_abc, B_ab, gammas = build_infrastructure()

    s_values = [0.0, 0.15, 0.30, 0.50, 1.0]
    max_pq_sums = [3, 4, 5, 6]

    # Diagnostic 1: Heat kernel coefficients
    diag1 = diagnostic_1_heat_kernel_convergence(
        gens, f_abc, gammas,
        s_values=s_values,
        max_pq_sums=max_pq_sums
    )

    # Diagnostic 2: Spectral zeta
    diag2 = diagnostic_2_spectral_zeta(
        diag1, s_values=s_values, max_pq_sums=max_pq_sums
    )

    # Diagnostic 3: CW convergence (fewer s-points for speed)
    diag3 = diagnostic_3_cw_convergence(
        gens, f_abc, gammas,
        max_pq_sums=max_pq_sums,
        mu_sq_values=[0.1, 1.0, 10.0],
        n_f_values=[1, 4],
        n_s=61,
        s_range=(0.0, 2.0)
    )

    # Diagnostic 4: Weyl law
    diag4 = diagnostic_4_weyl_law(
        diag1, s_values=s_values, max_pq_sums=max_pq_sums
    )

    # Diagnostic 5: Ratio stability
    diag5 = diagnostic_5_ratio_stability(
        diag1, s_values=s_values, max_pq_sums=max_pq_sums
    )

    # Final verdict
    verdict = convergence_verdict(diag1, diag2, diag3, diag4, diag5,
                                  s_values, max_pq_sums)

    t_total = time.time() - t0_global
    print(f"\n  Total runtime: {t_total:.1f}s")
    print("\n" + "="*72)
    print("C-1 COMPLETE")
    print("="*72)
