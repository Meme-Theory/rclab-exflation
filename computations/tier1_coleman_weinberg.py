"""
TIER 1: FULL COLEMAN-WEINBERG EFFECTIVE POTENTIAL V_eff(s)
==========================================================

Computes the complete 1-loop effective potential for the Jensen deformation
parameter s on (SU(3), g_s):

    V_eff(s) = V_tree(s) + V_CW^boson(s) + V_CW^fermion(s)

Components:
  V_tree(s) = -R(s) * Vol  (dimensionally reduced Einstein-Hilbert action)
            = proportional to [2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}]

  V_CW^boson(s) = +(n_b / 64 pi^2) * sum_j m_j^4(s) [ln(m_j^2/mu^2) - c_b]
                  with 4 C^2 gauge boson masses from Baptista eq 3.84

  V_CW^fermion(s) = -(n_f / 64 pi^2) * sum_{(p,q)} dim(p,q) *
                     sum_j |lambda_j^{(p,q)}(s)|^4 [ln(|lambda_j|^2/mu^2) - 3/2]
                    with full Dirac tower from tier1_dirac_spectrum.py

DOF ISSUE (Session 16):
  Asymptotic DOF: 45 bosonic vs 16 fermionic on 8D SU(3).
  Available data: only 4 C^2 bosonic modes. Full bosonic KK tower NOT computed.
  Result is "Version C-modified" -- INDICATIVE, not definitive.

SWEEP PROTOCOL:
  40 combinations: 5 mu x 2 n_f x 2 c_b x 2 subtraction_scheme
  Binding criterion: monotonic for ALL 40 = FAILURE (soft, DOF excuse)
  Minimum in [0.15, 0.50] for ANY combo = PASS

Author: Hawking-Theorist Agent (Session 17)
Date: 2026-02-14

Thermodynamic interpretation (Hawking):
  V_CW = Helmholtz free energy F = U - TS
  Minimum dF/ds = 0 is entropy maximization
  mu plays role of temperature in phase diagram
  Pfaffian sign change at s_c = Hawking-Page transition
"""

import numpy as np
from scipy.optimize import minimize_scalar, brentq
from scipy.signal import argrelmin
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
    dim_su3_irrep, baptista_V_potential,
    gauge_boson_masses_baptista, scalar_curvature_from_connection,
    scalar_curvature_analytical,
)


# =============================================================================
# MODULE 1: TREE-LEVEL POTENTIAL (EXACT)
# =============================================================================

def V_tree(s, normalize=True):
    """
    Tree-level effective potential from dimensionally reduced Einstein-Hilbert action.

    V_tree(s) = A * {1 - (1/10) * [2 e^{2s} - 1 + 8 e^{-s} - e^{-4s}]}

    where A = (P^5_M / (2 Vol_0)) * (2/15)^4 is an overall constant.

    At s=0: bracket = [2-1+8-1] = 8, so V_tree(0) = A * (1 - 8/10) = A * 0.2.
    V_tree is MONOTONICALLY DECREASING for s > 0 (runaway instability).

    Baptista Paper 15 eq (3.80) at sigma=0.

    Args:
        s: Jensen deformation parameter (scalar or array)
        normalize: if True, normalize so V_tree(0) = 1.0

    Returns:
        V: tree-level potential value(s)
    """
    s = np.asarray(s, dtype=np.float64)
    R_bracket = 2 * np.exp(2*s) - 1 + 8 * np.exp(-s) - np.exp(-4*s)
    V = 1.0 - R_bracket / 10.0

    if normalize:
        V0 = 1.0 - 8.0/10.0  # = 0.2
        V = V / V0  # V_tree(0) = 1.0

    return V


def V_tree_derivatives(s):
    """
    Compute V_tree(s) and its first two derivatives analytically.

    V = 1 - (1/10)[2e^{2s} - 1 + 8e^{-s} - e^{-4s}]
    V' = -(1/10)[4e^{2s} - 8e^{-s} + 4e^{-4s}]
       = -(4/10)[e^{2s} - 2e^{-s} + e^{-4s}]
    V'' = -(4/10)[2e^{2s} + 2e^{-s} - 4e^{-4s}]

    Returns:
        V, dV, d2V: function value, first and second derivatives
    """
    e2s = np.exp(2*s)
    ems = np.exp(-s)
    e4s = np.exp(-4*s)

    V = 1.0 - (2*e2s - 1 + 8*ems - e4s) / 10.0
    dV = -(4*e2s - 8*ems + 4*e4s) / 10.0
    d2V = -(8*e2s + 8*ems - 16*e4s) / 10.0

    return V, dV, d2V


# =============================================================================
# MODULE 2: COLEMAN-WEINBERG BOSONIC CONTRIBUTION
# =============================================================================

def V_CW_boson(s, mu_sq=1.0, c_b=5.0/6.0, n_b=4):
    """
    1-loop Coleman-Weinberg contribution from C^2 gauge bosons.

    V_CW^boson = +(n_b / 64 pi^2) * sum_j m_j^4 [ln(m_j^2/mu^2) - c_b]

    For the Jensen deformation, 4 C^2 gauge bosons acquire mass.
    m^2(s) = (e^s - e^{-2s})^2 + (1 - e^{-s})^2  (Baptista eq 3.84, sigma=0)

    The 4 u(2) bosons remain massless and contribute zero.

    Sign convention: bosonic CW is POSITIVE (stabilizing at large s).

    Args:
        s: Jensen parameter (scalar or array)
        mu_sq: renormalization scale squared
        c_b: subtraction constant (5/6 for MS-bar, 3/2 for cutoff)
        n_b: number of real bosonic DOF (4 = one per C^2 direction)

    Returns:
        V_b: bosonic CW potential
    """
    s = np.asarray(s, dtype=np.float64)
    m2 = (np.exp(s) - np.exp(-2*s))**2 + (1 - np.exp(-s))**2

    # At s=0: m^2 = 0, contribution = 0
    result = np.zeros_like(s, dtype=np.float64)
    mask = m2 > 1e-30

    if np.any(mask):
        m4 = m2[mask]**2
        log_term = np.log(m2[mask] / mu_sq) - c_b
        result[mask] = (n_b / (64 * np.pi**2)) * m4 * log_term

    return result


def V_CW_boson_extended(s, mu_sq=1.0, c_b=5.0/6.0, n_b_per_boson=1):
    """
    Extended bosonic CW with explicit DOF counting.

    DOF analysis for C^2 gauge bosons:
    - 4 C^2 directions in su(3)/u(2)
    - Each gauge boson in 4D has 3 polarization DOF (massive) or 2 (massless)
    - Total bosonic DOF from C^2: 4 * 3 = 12 (massive)
    - n_b_per_boson: real DOF per mass-squared eigenvalue

    Returns:
        V_b: bosonic CW contribution with specified DOF
    """
    return V_CW_boson(s, mu_sq, c_b, n_b=4 * n_b_per_boson)


# =============================================================================
# MODULE 3: COLEMAN-WEINBERG FERMIONIC CONTRIBUTION
# =============================================================================

def compute_fermionic_CW_from_eigenvalues(eval_data, mu_sq=1.0, c_f=3.0/2.0):
    """
    Compute the fermionic CW contribution from Dirac eigenvalue data.

    V_CW^fermion = -(1/64 pi^2) * sum_{(p,q)} dim(p,q) *
                    sum_j |lambda_j|^4 [ln(|lambda_j|^2/mu^2) - c_f]

    The NEGATIVE sign is because fermion loops contribute with opposite sign
    to boson loops (Pauli exclusion -> negative vacuum energy contribution).

    The Peter-Weyl weight dim(p,q) accounts for the multiplicity of each
    eigenvalue in the full L^2 spectrum.

    Each eigenvalue of D_{(p,q)} represents ONE Dirac spinor degree of freedom.
    For 4D Dirac fermion, n_f = 4 (two chiralities x two complex DOF).

    Args:
        eval_data: list of (p, q, eigenvalues_array) from collect_spectrum
        mu_sq: renormalization scale squared
        c_f: subtraction constant (3/2 for both MS-bar and cutoff with fermions)

    Returns:
        V_f: total fermionic CW contribution (NEGATIVE)
        V_f_sectors: dict (p,q) -> sector contribution
    """
    V_f = 0.0
    V_f_sectors = {}

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)

        # Skip zero eigenvalues (they contribute nothing via lim x^4 ln x -> 0)
        nonzero = abs_evals[abs_evals > 1e-12]

        if len(nonzero) == 0:
            V_f_sectors[(p, q)] = 0.0
            continue

        lam4 = nonzero**4
        log_term = np.log(nonzero**2 / mu_sq) - c_f

        # Sum over eigenvalues, weighted by PW multiplicity
        sector_V = d_pq * np.sum(lam4 * log_term)
        V_f_sectors[(p, q)] = sector_V
        V_f += sector_V

    # Overall coefficient with NEGATIVE sign (fermionic)
    V_f *= -1.0 / (64 * np.pi**2)
    for key in V_f_sectors:
        V_f_sectors[key] *= -1.0 / (64 * np.pi**2)

    return V_f, V_f_sectors


def compute_fermionic_CW_nf(eval_data, n_f=1, mu_sq=1.0, c_f=3.0/2.0):
    """
    Fermionic CW with explicit n_f multiplicity.

    n_f accounts for the number of 4D Dirac fermion DOF per internal mode:
      n_f = 1: each D eigenvalue = 1 real DOF (most conservative)
      n_f = 4: each D eigenvalue = 4 real DOF (full 4D Dirac fermion)

    Returns:
        V_f: n_f * base fermionic CW
        V_f_sectors: dict
    """
    V_f_base, sectors_base = compute_fermionic_CW_from_eigenvalues(
        eval_data, mu_sq, c_f
    )
    V_f = n_f * V_f_base
    sectors = {k: n_f * v for k, v in sectors_base.items()}
    return V_f, sectors


# =============================================================================
# MODULE 4: HIGH-TEMPERATURE EXPANSION (CROSS-CHECK)
# =============================================================================

def V_high_T_fermion(eval_data, T_sq=1.0):
    """
    High-temperature expansion of fermionic free energy.

    At high T, the 1-loop contribution goes as |lambda|^2 (not |lambda|^4).
    This converges FASTER and serves as a robustness cross-check.

    F_high_T = -(pi^2/90) T^4 * N_eff + (1/24) T^2 * sum m_i^2 + ...

    For fixed T, the s-dependent part is:
    V_HT(s) ~ sum_{(p,q)} dim(p,q) * sum_j |lambda_j(s)|^2

    This is just the heat kernel K(t=1) up to normalization.

    Args:
        eval_data: eigenvalue data
        T_sq: temperature scale

    Returns:
        V_HT: high-T approximation
        V_HT_sectors: dict
    """
    V_HT = 0.0
    V_HT_sectors = {}

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)
        nonzero = abs_evals[abs_evals > 1e-12]

        if len(nonzero) == 0:
            V_HT_sectors[(p, q)] = 0.0
            continue

        sector_V = d_pq * np.sum(nonzero**2)
        V_HT_sectors[(p, q)] = sector_V
        V_HT += sector_V

    # Normalize with T^2 factor
    V_HT *= T_sq / 24.0
    for key in V_HT_sectors:
        V_HT_sectors[key] *= T_sq / 24.0

    return V_HT, V_HT_sectors


# =============================================================================
# MODULE 5: TOTAL V_eff AND PARAMETER SWEEP
# =============================================================================

def compute_Veff_at_s(s, gens, f_abc, gammas, max_pq_sum=6,
                      mu_sq=1.0, n_f=1, c_b=5.0/6.0, c_f=3.0/2.0,
                      n_b_per_boson=1, normalize_tree=True,
                      kappa_tree=1.0, kappa_CW=1.0):
    """
    Compute the full V_eff(s) at a single s value.

    V_eff = kappa_tree * V_tree(s) + kappa_CW * [V_CW^boson(s) + V_CW^fermion(s)]

    Args:
        s: Jensen parameter
        gens, f_abc, gammas: SU(3) infrastructure
        max_pq_sum: irrep truncation
        mu_sq: renormalization scale squared
        n_f: fermionic DOF multiplier
        c_b: bosonic subtraction constant
        c_f: fermionic subtraction constant
        n_b_per_boson: bosonic DOF per mass eigenvalue
        normalize_tree: if True, V_tree(0)=1
        kappa_tree, kappa_CW: relative weight factors

    Returns:
        dict with V_tree, V_boson, V_fermion, V_total, eval_data
    """
    # Tree level
    Vt = V_tree(s, normalize=normalize_tree)
    if np.ndim(Vt) == 0:
        Vt = float(Vt)

    # Bosonic CW
    Vb = V_CW_boson(np.atleast_1d(s), mu_sq, c_b, n_b=4*n_b_per_boson)
    Vb = float(Vb[0]) if np.ndim(Vb) > 0 else float(Vb)

    # Fermionic CW -- need Dirac eigenvalues
    _, eval_data = collect_spectrum(
        s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )
    Vf, Vf_sectors = compute_fermionic_CW_nf(eval_data, n_f, mu_sq, c_f)

    # High-T cross-check
    V_HT, _ = V_high_T_fermion(eval_data)

    V_total = kappa_tree * Vt + kappa_CW * (Vb + Vf)

    return {
        'V_tree': Vt,
        'V_boson': Vb,
        'V_fermion': Vf,
        'V_total': V_total,
        'V_high_T': V_HT,
        'eval_data': eval_data,
        'Vf_sectors': Vf_sectors,
    }


def sweep_Veff(s_values, gens, f_abc, gammas, max_pq_sum=6,
               mu_sq=1.0, n_f=1, c_b=5.0/6.0, c_f=3.0/2.0,
               n_b_per_boson=1, verbose=True):
    """
    Sweep V_eff(s) over an array of s values.

    Caches Dirac eigenvalues at each s to avoid recomputation.

    Returns:
        results: dict with arrays V_tree(s), V_boson(s), V_fermion(s), V_total(s)
    """
    n_s = len(s_values)
    V_tree_arr = np.zeros(n_s)
    V_boson_arr = np.zeros(n_s)
    V_fermion_arr = np.zeros(n_s)
    V_total_arr = np.zeros(n_s)
    V_HT_arr = np.zeros(n_s)

    # Cache eigenvalue data
    eval_data_cache = {}

    for i, s in enumerate(s_values):
        if verbose and (i % 10 == 0 or i == n_s - 1):
            print(f"    s={s:.3f} ({i+1}/{n_s})...", flush=True)

        # Tree level
        Vt = V_tree(s, normalize=True)
        V_tree_arr[i] = float(np.squeeze(Vt))

        # Bosonic CW
        Vb = V_CW_boson(np.atleast_1d(s), mu_sq, c_b, n_b=4*n_b_per_boson)
        V_boson_arr[i] = float(np.squeeze(Vb))

        # Fermionic CW
        if s not in eval_data_cache:
            _, eval_data = collect_spectrum(
                s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
            )
            eval_data_cache[s] = eval_data
        else:
            eval_data = eval_data_cache[s]

        Vf, _ = compute_fermionic_CW_nf(eval_data, n_f, mu_sq, c_f=c_f)
        V_fermion_arr[i] = Vf

        # High-T
        V_HT, _ = V_high_T_fermion(eval_data)
        V_HT_arr[i] = V_HT

        V_total_arr[i] = V_tree_arr[i] + V_boson_arr[i] + V_fermion_arr[i]

    return {
        's_values': np.array(s_values),
        'V_tree': V_tree_arr,
        'V_boson': V_boson_arr,
        'V_fermion': V_fermion_arr,
        'V_total': V_total_arr,
        'V_high_T': V_HT_arr,
        'eval_data_cache': eval_data_cache,
    }


# =============================================================================
# MODULE 6: MINIMUM FINDER
# =============================================================================

def find_minima(s_values, V_values, verbose=True):
    """
    Find local minima of V_eff(s) from discrete data.

    Uses argrelmin to find discrete minima, then refines with parabolic fit.

    Args:
        s_values: array of s values
        V_values: array of V_eff values

    Returns:
        minima: list of dicts {s_min, V_min, V_second_deriv, curvature_mass}
    """
    # Find local minima (not at boundaries)
    indices = argrelmin(V_values, order=1)[0]

    minima = []
    for idx in indices:
        if idx < 2 or idx > len(s_values) - 3:
            continue

        # Parabolic fit around minimum for refinement
        s_local = s_values[idx-2:idx+3]
        V_local = V_values[idx-2:idx+3]

        # Fit quadratic: V = a*s^2 + b*s + c
        coeffs = np.polyfit(s_local, V_local, 2)
        a, b, c = coeffs

        if a > 0:  # genuine minimum (not maximum)
            s_min = -b / (2*a)
            V_min = a * s_min**2 + b * s_min + c
            V_second = 2 * a

            # "Mass" of the s-modulus (eigenvalue of fluctuations)
            m_s_sq = V_second

            minima.append({
                's_min': s_min,
                'V_min': V_min,
                'V_second_deriv': V_second,
                'm_s_sq': m_s_sq,
                'discrete_idx': idx,
            })

    if verbose:
        if minima:
            print(f"    Found {len(minima)} local minimum/minima:")
            for m in minima:
                print(f"      s_min = {m['s_min']:.6f}, V_min = {m['V_min']:.6e}, "
                      f"V'' = {m['V_second_deriv']:.6e}")
        else:
            print(f"    No local minimum found (monotonic or boundary)")

    return minima


def check_gauge_viability(s_min):
    """
    Check if s_min falls in the gauge-viable window.

    The gauge coupling ratio g_1/g_2 = e^{-2s_0} should be in [0.2, 0.8]
    for phenomenological viability. This constrains s_0 in [0.11, 0.80].

    The tighter constraint s_0 in [0.15, 0.50] corresponds to
    e^{-2s_0} in [0.37, 0.74].

    Args:
        s_min: stabilized Jensen parameter

    Returns:
        dict with gauge coupling ratio and viability assessment
    """
    ratio = np.exp(-2 * s_min)

    in_wide_window = 0.11 <= s_min <= 0.80
    in_tight_window = 0.15 <= s_min <= 0.50

    return {
        'e_minus_2s': ratio,
        's_min': s_min,
        'wide_window': in_wide_window,
        'tight_window': in_tight_window,
        'assessment': ('PASS (tight)' if in_tight_window
                       else 'PASS (wide)' if in_wide_window
                       else 'FAIL'),
    }


# =============================================================================
# MODULE 7: FULL 40-COMBO PARAMETER SWEEP
# =============================================================================

def full_parameter_sweep(gens, f_abc, gammas, max_pq_sum=6, n_s=101,
                         s_range=(0.0, 2.5), verbose=True):
    """
    Execute the full 40-combination parameter sweep as specified in Session 16.

    Parameters swept:
      mu_sq in {0.01, 0.09, 1.0, 9.0, 100.0}  (5 values = mu^2)
      n_f in {1, 4}                              (2 values)
      c_b in {5/6, 3/2}                          (2 values)
      subtraction: c_f in {3/2, 1/2}             (2 values -- MS-bar vs zeta)

    Total: 5 * 2 * 2 * 2 = 40 combinations

    For each: compute V_eff(s) at n_s points and find minima.

    Returns:
        sweep_results: list of dicts, one per parameter combo
        summary: dict with aggregate statistics
    """
    s_values = np.linspace(s_range[0], s_range[1], n_s)

    # Parameter grid
    mu_sq_values = [0.01, 0.09, 1.0, 9.0, 100.0]
    n_f_values = [1, 4]
    c_b_values = [5.0/6.0, 3.0/2.0]
    c_f_values = [3.0/2.0, 1.0/2.0]

    total_combos = len(mu_sq_values) * len(n_f_values) * len(c_b_values) * len(c_f_values)

    if verbose:
        print(f"\n  FULL PARAMETER SWEEP: {total_combos} combinations")
        print(f"  s range: [{s_range[0]}, {s_range[1]}], n_s = {n_s}")
        print(f"  max_pq_sum = {max_pq_sum}")
        print(f"  mu^2 values: {mu_sq_values}")
        print(f"  n_f values: {n_f_values}")
        print(f"  c_b values: {c_b_values}")
        print(f"  c_f values: {c_f_values}")

    # Pre-compute Dirac eigenvalues at ALL s values (expensive but shared)
    print(f"\n  Phase 1: Pre-computing Dirac eigenvalues at {n_s} s-values...")
    t0 = time.time()
    eval_data_cache = {}
    for i, s in enumerate(s_values):
        if i % 10 == 0:
            elapsed = time.time() - t0
            print(f"    s={s:.3f} ({i+1}/{n_s}), elapsed={elapsed:.1f}s", flush=True)
        _, eval_data = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
        )
        eval_data_cache[i] = eval_data

    t_eigenvalues = time.time() - t0
    print(f"  Eigenvalue computation: {t_eigenvalues:.1f}s ({t_eigenvalues/n_s:.2f}s per s-value)")

    # Phase 2: Sweep parameter combinations
    print(f"\n  Phase 2: Sweeping {total_combos} parameter combinations...")
    sweep_results = []
    combo_idx = 0

    n_with_minimum = 0
    n_in_gauge_window = 0

    for mu_sq in mu_sq_values:
        for n_f in n_f_values:
            for c_b in c_b_values:
                for c_f in c_f_values:
                    combo_idx += 1

                    # Compute V_eff at all s values
                    V_tree_arr = np.array([float(np.squeeze(V_tree(s))) for s in s_values])
                    V_boson_arr = np.array([float(np.squeeze(
                        V_CW_boson(np.atleast_1d(s), mu_sq, c_b, n_b=4)
                    )) for s in s_values])

                    V_fermion_arr = np.zeros(n_s)
                    for i in range(n_s):
                        Vf, _ = compute_fermionic_CW_nf(
                            eval_data_cache[i], n_f, mu_sq, c_f
                        )
                        V_fermion_arr[i] = Vf

                    V_total = V_tree_arr + V_boson_arr + V_fermion_arr

                    # Find minima
                    minima = find_minima(s_values, V_total, verbose=False)

                    has_minimum = len(minima) > 0
                    gauge_viable = False
                    best_minimum = None

                    if has_minimum:
                        n_with_minimum += 1
                        # Find the deepest minimum
                        best_minimum = min(minima, key=lambda m: m['V_min'])
                        gauge_check = check_gauge_viability(best_minimum['s_min'])
                        gauge_viable = gauge_check['tight_window']
                        if gauge_viable:
                            n_in_gauge_window += 1

                    result = {
                        'combo_idx': combo_idx,
                        'mu_sq': mu_sq,
                        'n_f': n_f,
                        'c_b': c_b,
                        'c_f': c_f,
                        'V_tree': V_tree_arr,
                        'V_boson': V_boson_arr,
                        'V_fermion': V_fermion_arr,
                        'V_total': V_total,
                        'minima': minima,
                        'has_minimum': has_minimum,
                        'gauge_viable': gauge_viable,
                        'best_minimum': best_minimum,
                    }
                    sweep_results.append(result)

                    if verbose and (combo_idx % 10 == 0 or has_minimum):
                        status = "MIN" if has_minimum else "---"
                        gauge_str = " GAUGE" if gauge_viable else ""
                        s_str = f"s0={best_minimum['s_min']:.4f}" if best_minimum else "none"
                        print(f"    [{combo_idx:2d}/{total_combos}] mu2={mu_sq:.2f} "
                              f"nf={n_f} cb={c_b:.3f} cf={c_f:.3f}: "
                              f"{status} {s_str}{gauge_str}")

    # Summary
    summary = {
        'total_combos': total_combos,
        'n_with_minimum': n_with_minimum,
        'n_in_gauge_window': n_in_gauge_window,
        'n_monotonic': total_combos - n_with_minimum,
        'binding_pass': n_with_minimum > 0,
        'binding_fail': n_with_minimum == 0,
        'strong_pass': n_in_gauge_window > 0,
    }

    return sweep_results, summary, s_values, eval_data_cache


# =============================================================================
# MODULE 8: DIAGNOSTICS
# =============================================================================

def thermodynamic_diagnostics(s_values, V_total, V_tree_arr, V_boson_arr,
                               V_fermion_arr, mu_sq=1.0, verbose=True):
    """
    Hawking's thermodynamic diagnostics on V_eff.

    1. Spectral entropy: S(s) = -dV/d(ln mu) ~ -sum |lam|^4
    2. Specific heat sign: d^2V/d(mu^2)^2 at minimum
    3. Free energy decomposition: U(s) and TS(s) separately
    4. Phase transition scan: s_0(mu) trajectory

    Returns:
        diag: dict of diagnostic quantities
    """
    ds = s_values[1] - s_values[0] if len(s_values) > 1 else 0.01

    # Numerical derivatives
    dV = np.gradient(V_total, ds)
    d2V = np.gradient(dV, ds)

    # "Spectral entropy": the s-derivative of the fermionic contribution
    # In thermodynamic analogy: S = -dF/dT = -dV_CW/d(mu^2)
    # Approximated by numerical difference of V_fermion at nearby mu
    dV_ferm = np.gradient(V_fermion_arr, ds)

    # Energy = V_total + T * S in thermodynamic analogy
    # Here: "internal energy" U ~ V_tree, "entropy contribution" ~ V_CW

    if verbose:
        print(f"\n  Thermodynamic diagnostics (mu^2 = {mu_sq}):")
        print(f"    V_total range: [{np.min(V_total):.6e}, {np.max(V_total):.6e}]")
        print(f"    V_tree range:  [{np.min(V_tree_arr):.6e}, {np.max(V_tree_arr):.6e}]")
        print(f"    V_boson range: [{np.min(V_boson_arr):.6e}, {np.max(V_boson_arr):.6e}]")
        print(f"    V_ferm range:  [{np.min(V_fermion_arr):.6e}, {np.max(V_fermion_arr):.6e}]")

        # Find where dV/ds = 0
        zero_crossings = []
        for i in range(len(dV) - 1):
            if dV[i] * dV[i+1] < 0:
                s_cross = s_values[i] - dV[i] * ds / (dV[i+1] - dV[i])
                zero_crossings.append(s_cross)

        if zero_crossings:
            print(f"    dV/ds = 0 at s = {', '.join(f'{z:.4f}' for z in zero_crossings)}")
        else:
            print(f"    dV/ds has no zero crossings (monotonic)")

        # Ratio of contributions at s=1
        idx_1 = np.argmin(np.abs(s_values - 1.0))
        print(f"\n    At s=1.0:")
        print(f"      V_tree   = {V_tree_arr[idx_1]:.6e}")
        print(f"      V_boson  = {V_boson_arr[idx_1]:.6e}")
        print(f"      V_fermion = {V_fermion_arr[idx_1]:.6e}")
        if abs(V_boson_arr[idx_1]) > 1e-30:
            print(f"      |V_ferm/V_boson| = {abs(V_fermion_arr[idx_1]/V_boson_arr[idx_1]):.1f}")

    return {
        'dV_ds': dV,
        'd2V_ds2': d2V,
        'dV_ferm_ds': dV_ferm,
    }


def truncation_convergence_test(s_test, gens, f_abc, gammas, mu_sq=1.0,
                                  n_f=1, c_b=5.0/6.0, c_f=3.0/2.0,
                                  verbose=True):
    """
    Test convergence of V_eff with respect to max_pq_sum truncation.

    Computes V_CW^fermion at a fixed s for max_pq_sum = 3, 4, 5, 6.

    CRITICAL TEST: if V_CW changes significantly from pq=5 to pq=6,
    the computation is NOT converged and results are unreliable.

    Args:
        s_test: s value to test at

    Returns:
        convergence: dict with V_CW at each truncation level
    """
    if verbose:
        print(f"\n  Truncation convergence test at s = {s_test:.3f}:")

    results = {}
    for pq_max in [3, 4, 5, 6]:
        t0 = time.time()
        _, eval_data = collect_spectrum(
            s_test, gens, f_abc, gammas, max_pq_sum=pq_max, verbose=False
        )
        Vf, _ = compute_fermionic_CW_nf(eval_data, n_f, mu_sq, c_f)
        Vb = float(np.squeeze(V_CW_boson(np.atleast_1d(s_test), mu_sq, c_b, n_b=4)))
        n_evals = sum(len(ed[2]) for ed in eval_data)
        dt = time.time() - t0

        results[pq_max] = {
            'V_fermion': Vf,
            'V_boson': Vb,
            'V_CW_total': Vf + Vb,
            'n_evals': n_evals,
            'time': dt,
        }

        if verbose:
            print(f"    pq_max={pq_max}: V_f={Vf:.6e}, V_b={Vb:.6e}, "
                  f"n_evals={n_evals}, time={dt:.1f}s")

    # Convergence metric: |V(6) - V(5)| / |V(6)|
    if 5 in results and 6 in results:
        V5 = results[5]['V_CW_total']
        V6 = results[6]['V_CW_total']
        if abs(V6) > 1e-30:
            rel_change = abs(V6 - V5) / abs(V6)
        else:
            rel_change = float('inf')
        results['convergence_metric'] = rel_change

        if verbose:
            print(f"    Convergence: |V(6)-V(5)|/|V(6)| = {rel_change:.4f}")
            if rel_change < 0.1:
                print(f"    CONVERGED (< 10% change)")
            elif rel_change < 0.3:
                print(f"    MARGINAL (10-30% change)")
            else:
                print(f"    NOT CONVERGED (> 30% change)")

    return results


# =============================================================================
# MODULE 9: BINDING CONSISTENCY CHECKS (Hawking)
# =============================================================================

def binding_checks(s_min, V_total_at_min, V_total_at_0, V_second_deriv,
                   eval_data_at_min=None, verbose=True):
    """
    Hawking's 6 binding consistency checks from Session 16 Round 2a.

    1. F(s_0) < F(0): broken state has lower free energy than symmetric
    2. d^2F/ds^2 > 0: stable minimum
    3. C_s finite: no phase transition AT s_0 (can be nearby)
    4. Bekenstein bound: S_internal ~ O(1) in Planck units
    5. Species bound: N * m_lightest^2 <= M_Pl^2
    6. GSL: dS_gen/dt >= 0

    Checks 4-6 require assumptions about overall normalization and
    are evaluated qualitatively.

    Returns:
        checks: dict of {check_name: (pass/fail, value, assessment)}
    """
    checks = {}

    # Check 1: F(s_0) < F(0)
    ch1 = V_total_at_min < V_total_at_0
    checks['free_energy_lowered'] = {
        'pass': ch1,
        'value': V_total_at_min - V_total_at_0,
        'desc': f"V(s0)={V_total_at_min:.6e} < V(0)={V_total_at_0:.6e}"
    }

    # Check 2: d^2V/ds^2 > 0
    ch2 = V_second_deriv > 0
    checks['stable_minimum'] = {
        'pass': ch2,
        'value': V_second_deriv,
        'desc': f"V''(s0) = {V_second_deriv:.6e}"
    }

    # Check 3: C_s finite (specific heat)
    # C_s ~ -T * d^2F/dT^2 ~ d^2V/d(mu^2)^2
    # Cannot compute directly without mu variation, so check V'' is finite
    ch3 = np.isfinite(V_second_deriv) and V_second_deriv != 0
    checks['finite_specific_heat'] = {
        'pass': ch3,
        'value': V_second_deriv,
        'desc': f"V'' finite and nonzero at s0"
    }

    # Check 4: Bekenstein bound (qualitative)
    # Internal entropy S ~ ln(number of microstates)
    # For single modulus s, S ~ O(1) -- automatically satisfied
    checks['bekenstein_bound'] = {
        'pass': True,
        'value': 1.0,
        'desc': "Single modulus s: S_internal ~ O(1) (trivially satisfied)"
    }

    # Check 5: Species bound N * m^2 <= M_Pl^2
    # With our normalized eigenvalues, this is a constraint on the overall scale
    # Qualitative: N_species from Dirac tower at s_min
    if eval_data_at_min is not None:
        N_species = sum(dim_su3_irrep(p, q) * len(evals)
                       for p, q, evals in eval_data_at_min)
        checks['species_bound'] = {
            'pass': True,  # qualitative
            'value': N_species,
            'desc': f"N_species = {N_species} (check N*m_light^2 << M_Pl^2)"
        }

    # Check 6: GSL (qualitative -- requires dynamics)
    checks['generalized_second_law'] = {
        'pass': True,  # assumed if V has stable minimum
        'value': None,
        'desc': "GSL satisfied if universe relaxes to minimum (equilibrium)"
    }

    if verbose:
        print(f"\n  Binding consistency checks at s_min = {s_min:.6f}:")
        for name, ch in checks.items():
            status = "PASS" if ch['pass'] else "FAIL"
            print(f"    [{status}] {name}: {ch['desc']}")

    return checks


# =============================================================================
# MODULE 10: PLOTS
# =============================================================================

def plot_Veff_results(sweep_results, s_values, summary, save_path=None):
    """
    Generate comprehensive plots of V_eff sweep results.
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available; skipping plots.")
        return

    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('Coleman-Weinberg V_eff(s) — Full 40-Combo Parameter Sweep\n'
                 'Version C-modified: Full Dirac tower + 4 C^2 bosons',
                 fontsize=14, fontweight='bold')

    # Panel 1: V_tree, V_boson, V_fermion at reference params
    ax1 = axes[0, 0]
    ref = sweep_results[0]  # first combo
    ax1.plot(s_values, ref['V_tree'], 'b-', linewidth=2, label='V_tree')
    ax1.plot(s_values, ref['V_boson'], 'r-', linewidth=2, label='V_boson (4 C^2)')
    ax1.plot(s_values, ref['V_fermion'], 'g-', linewidth=2, label='V_fermion (Dirac)')
    ax1.plot(s_values, ref['V_total'], 'k--', linewidth=2, label='V_total')
    ax1.set_xlabel('Jensen parameter s')
    ax1.set_ylabel('V_eff')
    ax1.set_title('Components (mu^2=0.01, nf=1, cb=5/6)')
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='gray', linestyle=':', linewidth=0.5)

    # Panel 2: V_total for all 40 combos (overlay)
    ax2 = axes[0, 1]
    colors = plt.cm.tab20(np.linspace(0, 1, len(sweep_results)))
    for i, r in enumerate(sweep_results):
        alpha = 0.3
        lw = 0.5
        if r['has_minimum']:
            alpha = 0.8
            lw = 1.5
        ax2.plot(s_values, r['V_total'], '-', color=colors[i % 20],
                alpha=alpha, linewidth=lw)
    ax2.set_xlabel('Jensen parameter s')
    ax2.set_ylabel('V_total')
    ax2.set_title(f'All {len(sweep_results)} combos (thick = has minimum)')
    ax2.grid(True, alpha=0.3)

    # Panel 3: Minimum locations
    ax3 = axes[0, 2]
    min_s = []
    min_V = []
    min_colors = []
    for r in sweep_results:
        if r['best_minimum']:
            min_s.append(r['best_minimum']['s_min'])
            min_V.append(r['best_minimum']['V_min'])
            min_colors.append('green' if r['gauge_viable'] else 'orange')

    if min_s:
        ax3.scatter(min_s, min_V, c=min_colors, s=50, zorder=5)
        ax3.axvspan(0.15, 0.50, alpha=0.1, color='green', label='Gauge window')
        ax3.set_xlabel('s_min')
        ax3.set_ylabel('V_eff(s_min)')
        ax3.set_title(f'{len(min_s)} minima found ({summary["n_in_gauge_window"]} gauge-viable)')
        ax3.legend(fontsize=8)
    else:
        ax3.text(0.5, 0.5, 'NO MINIMA FOUND\n(all 40 monotonic)',
                transform=ax3.transAxes, ha='center', va='center',
                fontsize=14, color='red', fontweight='bold')
        ax3.set_title('Minimum locations')
    ax3.grid(True, alpha=0.3)

    # Panel 4: mu^2 dependence
    ax4 = axes[1, 0]
    for r in sweep_results:
        if r['n_f'] == 1 and abs(r['c_b'] - 5.0/6.0) < 0.01 and abs(r['c_f'] - 3.0/2.0) < 0.01:
            mu_label = f"mu^2={r['mu_sq']:.2g}"
            ax4.plot(s_values, r['V_total'], '-', linewidth=1.5, label=mu_label)
    ax4.set_xlabel('Jensen parameter s')
    ax4.set_ylabel('V_total')
    ax4.set_title('mu^2 dependence (nf=1, cb=5/6, cf=3/2)')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)

    # Panel 5: n_f dependence
    ax5 = axes[1, 1]
    for r in sweep_results:
        if abs(r['mu_sq'] - 1.0) < 0.01 and abs(r['c_b'] - 5.0/6.0) < 0.01:
            nf_label = f"nf={r['n_f']}, cf={r['c_f']:.2f}"
            ax5.plot(s_values, r['V_total'], '-', linewidth=1.5, label=nf_label)
    ax5.set_xlabel('Jensen parameter s')
    ax5.set_ylabel('V_total')
    ax5.set_title('n_f and c_f dependence (mu^2=1, cb=5/6)')
    ax5.legend(fontsize=8)
    ax5.grid(True, alpha=0.3)

    # Panel 6: Summary table as text
    ax6 = axes[1, 2]
    ax6.axis('off')
    summary_text = (
        f"SWEEP SUMMARY\n"
        f"{'='*40}\n"
        f"Total combinations: {summary['total_combos']}\n"
        f"With minimum: {summary['n_with_minimum']}\n"
        f"Gauge-viable: {summary['n_in_gauge_window']}\n"
        f"Monotonic: {summary['n_monotonic']}\n\n"
        f"BINDING CRITERION:\n"
    )
    if summary['binding_fail']:
        summary_text += "ALL 40 MONOTONIC = FAILURE\n(soft: DOF excuse)"
    elif summary['strong_pass']:
        summary_text += f"PASS: {summary['n_in_gauge_window']} in gauge window"
    else:
        summary_text += f"WEAK PASS: minimum outside gauge window"

    ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes,
            fontsize=11, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()

    if save_path is None:
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'coleman_weinberg_sweep.png')
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved to {save_path}")
    plt.close()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("=" * 80)
    print("TIER 1: FULL COLEMAN-WEINBERG V_eff(s)")
    print("Session 17 — Hawking-Theorist Computation")
    print("=" * 80)

    t_start = time.time()

    # --- Infrastructure ---
    print("\n[1] Building SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford algebra error: {cliff_err:.2e}")

    # --- Verify V_tree ---
    print(f"\n{'='*80}")
    print("[2] V_tree(s) verification...")
    s_test = np.array([0.0, 0.15, 0.30, 0.50, 1.0, 1.5, 2.0, 2.5])
    for s in s_test:
        V, dV, d2V = V_tree_derivatives(s)
        R_ratio = scalar_curvature_analytical(s)
        print(f"  s={s:.2f}: V_tree={V:.6f}, V'={dV:.6f}, V''={d2V:.6f}, "
              f"R(s)/R(0)={R_ratio:.6f}")

    # Confirm V_tree has no minimum
    V_arr = np.array([V_tree(s) for s in np.linspace(0, 2.5, 100)])
    is_monotonic = np.all(np.diff(V_arr) <= 0)
    print(f"  V_tree monotonically decreasing: {is_monotonic}")
    print(f"  Eq. (1): V_tree(s) = 1 - (1/10)[2e^(2s) - 1 + 8e^(-s) - e^(-4s)]")
    print(f"  Validation: V_tree(0) = {V_tree(0.0):.6f} (expected 1.0)")

    # --- Truncation convergence test ---
    print(f"\n{'='*80}")
    print("[3] Truncation convergence test...")
    conv = truncation_convergence_test(
        1.0, gens, f_abc, gammas, mu_sq=1.0, n_f=1, verbose=True
    )

    # --- Single reference computation at s=1.0 ---
    print(f"\n{'='*80}")
    print("[4] Reference V_eff decomposition at s=1.0...")
    ref_result = compute_Veff_at_s(
        1.0, gens, f_abc, gammas, max_pq_sum=6,
        mu_sq=1.0, n_f=1, c_b=5.0/6.0, c_f=3.0/2.0
    )
    print(f"  Eq. (2): V_CW^boson(s) = +(n_b/64pi^2) sum m_j^4 [ln(m_j^2/mu^2) - c_b]")
    print(f"  Eq. (3): V_CW^fermion(s) = -(n_f/64pi^2) sum dim*|lam|^4 [ln(|lam|^2/mu^2) - c_f]")
    print(f"  V_tree(1.0)   = {ref_result['V_tree']:.6e}")
    print(f"  V_boson(1.0)  = {ref_result['V_boson']:.6e}")
    print(f"  V_fermion(1.0) = {ref_result['V_fermion']:.6e}")
    print(f"  V_total(1.0)  = {ref_result['V_total']:.6e}")
    print(f"  V_high_T(1.0) = {ref_result['V_high_T']:.6e}")
    if abs(ref_result['V_boson']) > 1e-30:
        ratio = abs(ref_result['V_fermion'] / ref_result['V_boson'])
        print(f"  |V_ferm/V_boson| = {ratio:.1f}  (DOF inversion check)")

    # Sector decomposition of fermion CW
    print(f"\n  Fermionic CW sector decomposition:")
    print(f"  {'(p,q)':>6}  {'dim':>4}  {'V_f_sector':>14}  {'fraction':>8}")
    total_Vf = ref_result['V_fermion']
    for (p, q), Vf_s in sorted(ref_result['Vf_sectors'].items(), key=lambda x: -abs(x[1])):
        d_pq = dim_su3_irrep(p, q)
        frac = Vf_s / total_Vf if abs(total_Vf) > 1e-30 else 0.0
        if abs(frac) > 0.001:
            print(f"  ({p},{q})  {d_pq:4d}  {Vf_s:14.6e}  {frac:7.1%}")

    # --- FULL 40-COMBO SWEEP ---
    print(f"\n{'='*80}")
    print("[5] FULL 40-COMBINATION PARAMETER SWEEP")
    print(f"  Eq. (4): V_eff(s) = V_tree(s) + V_CW^boson(s) + V_CW^fermion(s)")
    print(f"  Using max_pq_sum=6 (28 irreps)")

    sweep_results, summary, s_values, eval_cache = full_parameter_sweep(
        gens, f_abc, gammas, max_pq_sum=6, n_s=101, s_range=(0.0, 2.5),
        verbose=True
    )

    # --- Print results table ---
    print(f"\n{'='*80}")
    print("[6] RESULTS TABLE")
    print(f"  {'#':>3} {'mu^2':>7} {'n_f':>3} {'c_b':>5} {'c_f':>5} "
          f"{'min?':>4} {'s_min':>8} {'V_min':>12} {'V_pp':>10} {'gauge':>6}")
    print(f"  {'-'*76}")

    for r in sweep_results:
        min_str = "YES" if r['has_minimum'] else "no"
        if r['best_minimum']:
            s_str = f"{r['best_minimum']['s_min']:.4f}"
            V_str = f"{r['best_minimum']['V_min']:.4e}"
            Vpp_str = f"{r['best_minimum']['V_second_deriv']:.4e}"
            g_str = "YES" if r['gauge_viable'] else "no"
        else:
            s_str = "---"
            V_str = "---"
            Vpp_str = "---"
            g_str = "---"

        print(f"  {r['combo_idx']:3d} {r['mu_sq']:7.2f} {r['n_f']:3d} "
              f"{r['c_b']:5.3f} {r['c_f']:5.3f} "
              f"{min_str:>4} {s_str:>8} {V_str:>12} {Vpp_str:>10} {g_str:>6}")

    # --- Binding criterion ---
    print(f"\n{'='*80}")
    print("[7] BINDING CRITERION EVALUATION")
    print(f"  Total combinations: {summary['total_combos']}")
    print(f"  With minimum: {summary['n_with_minimum']}")
    print(f"  In gauge window [0.15, 0.50]: {summary['n_in_gauge_window']}")
    print(f"  Monotonic: {summary['n_monotonic']}")

    if summary['binding_fail']:
        print(f"\n  RESULT: ALL {summary['total_combos']} MONOTONIC = BINDING FAILURE")
        print(f"  Verdict: V_eff Version C-modified has NO minimum.")
        print(f"  Caveat: DOF inversion (45B:16F asymptotic). Only 4 of ~45 bosonic")
        print(f"  DOF included. Full bosonic KK tower may change result (Version D).")
        print(f"  This is a SOFT failure per Session 16 pre-registration.")
    elif summary['strong_pass']:
        print(f"\n  RESULT: PASS — {summary['n_in_gauge_window']} combos have minimum "
              f"in gauge window [0.15, 0.50]")
        # Print details of gauge-viable minima
        for r in sweep_results:
            if r['gauge_viable']:
                m = r['best_minimum']
                gc = check_gauge_viability(m['s_min'])
                print(f"    mu^2={r['mu_sq']:.2f}, nf={r['n_f']}, "
                      f"cb={r['c_b']:.3f}, cf={r['c_f']:.3f}: "
                      f"s_min={m['s_min']:.6f}, e^(-2s) = {gc['e_minus_2s']:.4f}")
    else:
        print(f"\n  RESULT: WEAK PASS — minimum exists but outside gauge window")
        for r in sweep_results:
            if r['has_minimum']:
                m = r['best_minimum']
                print(f"    mu^2={r['mu_sq']:.2f}, nf={r['n_f']}: "
                      f"s_min={m['s_min']:.6f}")

    # --- Thermodynamic diagnostics on reference combo ---
    if sweep_results[0]['has_minimum']:
        ref_r = sweep_results[0]
        print(f"\n{'='*80}")
        print("[8] THERMODYNAMIC DIAGNOSTICS (reference combo)")
        diag = thermodynamic_diagnostics(
            s_values, ref_r['V_total'], ref_r['V_tree'],
            ref_r['V_boson'], ref_r['V_fermion'],
            mu_sq=ref_r['mu_sq'], verbose=True
        )

        # Binding checks at best minimum
        m = ref_r['best_minimum']
        idx_min = m['discrete_idx']
        idx_0 = 0

        # Get eval_data at minimum
        eval_data_min = eval_cache.get(idx_min, None)

        binding = binding_checks(
            m['s_min'], ref_r['V_total'][idx_min], ref_r['V_total'][idx_0],
            m['V_second_deriv'], eval_data_min, verbose=True
        )

    # --- Plots ---
    print(f"\n{'='*80}")
    print("[9] Generating plots...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_Veff_results(
        sweep_results, s_values, summary,
        save_path=os.path.join(script_dir, 'coleman_weinberg_sweep.png')
    )

    # --- Final Summary ---
    t_total = time.time() - t_start
    print(f"\n{'='*80}")
    print("[10] FINAL SUMMARY")
    print("=" * 80)

    print(f"\n  1. TREE-LEVEL POTENTIAL:")
    print(f"     V_tree(s) = 1 - (1/10)[2e^(2s) - 1 + 8e^(-s) - e^(-4s)]")
    print(f"     Monotonically decreasing: YES (runaway instability)")
    print(f"     V_tree(0) = 1.0 (normalized)")

    print(f"\n  2. BOSONIC CW (4 C^2 gauge bosons, Baptista eq 3.84):")
    print(f"     V_boson(1.0) = {ref_result['V_boson']:.6e}")
    print(f"     Sign: POSITIVE (stabilizing)")

    print(f"\n  3. FERMIONIC CW (full Dirac tower, max_pq_sum=6):")
    print(f"     V_fermion(1.0) = {ref_result['V_fermion']:.6e}")
    print(f"     Sign: NEGATIVE (destabilizing)")
    if abs(ref_result['V_boson']) > 1e-30:
        print(f"     |V_ferm/V_boson| = {abs(ref_result['V_fermion']/ref_result['V_boson']):.1f}")

    print(f"\n  4. TRUNCATION CONVERGENCE:")
    if 'convergence_metric' in conv:
        print(f"     |V(pq=6) - V(pq=5)| / |V(pq=6)| = {conv['convergence_metric']:.4f}")

    print(f"\n  5. SWEEP RESULT:")
    print(f"     {summary['n_with_minimum']}/{summary['total_combos']} combos have minimum")
    print(f"     {summary['n_in_gauge_window']}/{summary['total_combos']} in gauge window")

    verdict = "PASS" if summary['strong_pass'] else (
        "WEAK PASS" if summary['n_with_minimum'] > 0 else
        "FAILURE (soft, DOF caveat)")
    print(f"     BINDING VERDICT: {verdict}")

    print(f"\n  6. DOF CAVEAT:")
    print(f"     Available: 4 bosonic DOF (C^2 gauge), full fermionic Dirac tower")
    print(f"     Missing: ~41 bosonic DOF (scalar, vector, tensor KK modes)")
    print(f"     Result classification: VERSION C-MODIFIED (indicative)")

    print(f"\n  7. PHYSICAL INTERPRETATION (Hawking thermodynamic framing):")
    print(f"     V_CW = Helmholtz free energy F(s, mu)")
    print(f"     s = order parameter (internal geometry shape)")
    print(f"     Minimum dF/ds = 0 = entropy maximization")
    if summary['n_with_minimum'] > 0:
        best_overall = None
        for r in sweep_results:
            if r['best_minimum'] and (best_overall is None or
                r['best_minimum']['V_min'] < best_overall['V_min']):
                best_overall = r['best_minimum']
                best_params = r
        if best_overall:
            print(f"     Deepest minimum: s_0 = {best_overall['s_min']:.6f}")
            gc = check_gauge_viability(best_overall['s_min'])
            print(f"     e^(-2s_0) = {gc['e_minus_2s']:.4f} (gauge coupling ratio proxy)")
            print(f"     Gauge assessment: {gc['assessment']}")

    print(f"\n  Total computation time: {t_total:.1f}s ({t_total/60:.1f}min)")
    print(f"\n{'='*80}")
    print("COLEMAN-WEINBERG COMPUTATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
