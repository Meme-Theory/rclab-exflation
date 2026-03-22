"""
H-5: FULL COLEMAN-WEINBERG V_eff WITH COMPLETE BOSONIC TOWER
==============================================================

Session 18 — The Decisive Computation.

Previous result (H-1, Session 17a): 0/40 minima with only 4 C^2 bosonic DOF.
This script extends to the FULL bosonic KK tower from B-6 and KK-1.

V_eff(s) = V_tree(s) + V_CW_boson(s) + V_CW_fermion(s)

where:
    V_tree(s) = -R(s)*Vol = 1 - (1/10)[2e^{2s} - 1 + 8e^{-s} - e^{-4s}]
                (monotonically decreasing, no minimum)

    V_CW_boson(s) = +(1/64pi^2) SUM_{bosonic modes} d_n m_n^4(s) [ln(m_n^2/mu^2) - c_b]
                    (POSITIVE, stabilizing)

    V_CW_fermion(s) = -(1/64pi^2) SUM_{(p,q)} dim(p,q) SUM_j |lam_j|^4 [ln(|lam|^2/mu^2) - c_f]
                      (NEGATIVE, destabilizing)

Thermodynamic interpretation (Hawking):
    V_CW = Helmholtz free energy F(s, mu)
    s = order parameter (internal geometry shape)
    mu = temperature analogue
    Minimum dF/ds = 0 = entropy maximization = spontaneous symmetry breaking

Constraint Conditions (pre-registered, Feynman predictions session):
    F1: s_0 must be in [0.24, 0.37] (Weinberg window for 20% sin^2(theta_W) match)
    F2: u(2) gauge bosons exactly massless (structural, already proven)
    F3: Z_3=1 and Z_3=2 degenerate at D_K level (theorem, already proven)
    F4: SM sectors (0,0),(1,0),(0,1) are lightest (already checked)
    F5: Spectral gap never closes (min gap 0.819 at s=0.26, already checked)
    FATAL: No minimum at any s > 0
    FATAL: s_0 > 2
    VERY DAMAGING: V_eff shifts > 50% between truncation orders

Author: Hawking-Theorist Agent (Session 18)
Date: 2026-02-15
"""

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.signal import argrelmin
import sys
import os
import time

# Add tier0-computation to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    collect_spectrum, get_irrep, dirac_operator_on_irrep,
)
from tier1_spectral_action import (
    dim_su3_irrep, baptista_V_potential,
    gauge_boson_masses_baptista, scalar_curvature_analytical,
)


# =============================================================================
# MODULE 1: V_TREE (EXACT, from tier1_coleman_weinberg.py)
# =============================================================================

def V_tree(s, normalize=True):
    """
    Tree-level effective potential from dimensionally reduced EH action.
    V_tree(s) = 1 - (1/10)[2e^{2s} - 1 + 8e^{-s} - e^{-4s}]
    Monotonically decreasing for s > 0 (runaway instability).
    Baptista Paper 15 eq (3.80) at sigma=0.
    """
    s = np.asarray(s, dtype=np.float64)
    R_bracket = 2 * np.exp(2*s) - 1 + 8 * np.exp(-s) - np.exp(-4*s)
    V = 1.0 - R_bracket / 10.0
    if normalize:
        V0 = 1.0 - 8.0/10.0  # = 0.2
        V = V / V0  # V_tree(0) = 1.0
    return V


# =============================================================================
# MODULE 2: BOSONIC CW — FULL TOWER INTERFACE
# =============================================================================

def V_CW_boson_C2_only(s, mu_sq=1.0, c_b=3.0/2.0, n_b=4):
    """
    Original 4 C^2 gauge boson CW (Session 17a baseline).
    m^2(s) = (e^s - e^{-2s})^2 + (1 - e^{-s})^2
    """
    s = np.asarray(s, dtype=np.float64)
    m2 = (np.exp(s) - np.exp(-2*s))**2 + (1 - np.exp(-s))**2
    result = np.zeros_like(s, dtype=np.float64)
    mask = m2 > 1e-30
    if np.any(mask):
        m4 = m2[mask]**2
        log_term = np.log(m2[mask] / mu_sq) - c_b
        result[mask] = (n_b / (64 * np.pi**2)) * m4 * log_term
    return result


def V_CW_boson_full(s, bosonic_eigenvalues_func, mu_sq=1.0, c_b=3.0/2.0):
    """
    Full bosonic CW contribution using eigenvalues from B-6/KK-1.

    bosonic_eigenvalues_func(s) should return:
        list of (mode_type, multiplicity, eigenvalue_squared)
        where:
            mode_type: str ('scalar', 'vector_C2', 'vector_u2', etc.)
            multiplicity: int (number of real DOF for this mode)
            eigenvalue_squared: float (mass-squared at this s)

    V_CW = +(1/64pi^2) SUM_n d_n * m_n^4 * [ln(m_n^2/mu^2) - c_b]
    """
    s_val = float(s)
    bosonic_modes = bosonic_eigenvalues_func(s_val)

    V_b = 0.0
    dof_count = 0

    for mode_type, mult, m2 in bosonic_modes:
        if m2 < 1e-30:
            # Massless modes contribute nothing to CW
            dof_count += mult
            continue
        m4 = m2**2
        log_term = np.log(m2 / mu_sq) - c_b
        V_b += (mult / (64 * np.pi**2)) * m4 * log_term
        dof_count += mult

    return V_b, dof_count


def V_CW_boson_from_eigenvalue_array(s, scalar_evals, scalar_mults,
                                      vector_evals=None, vector_mults=None,
                                      mu_sq=1.0, c_b=3.0/2.0):
    """
    Compute bosonic CW from raw eigenvalue arrays.

    Args:
        s: Jensen parameter (for logging only)
        scalar_evals: array of scalar Laplacian eigenvalues (mass-squared)
        scalar_mults: array of multiplicities for each eigenvalue
        vector_evals: optional array of vector Laplacian eigenvalues
        vector_mults: optional array of vector multiplicities
        mu_sq: renormalization scale
        c_b: subtraction constant

    Returns:
        V_b: total bosonic CW contribution
        n_dof_scalar: scalar DOF count
        n_dof_vector: vector DOF count
    """
    V_b = 0.0
    n_dof_scalar = 0
    n_dof_vector = 0

    # Scalar contribution
    for m2, mult in zip(scalar_evals, scalar_mults):
        n_dof_scalar += mult
        if m2 > 1e-30:
            m4 = m2**2
            log_term = np.log(m2 / mu_sq) - c_b
            V_b += (mult / (64 * np.pi**2)) * m4 * log_term

    # Vector contribution (if available)
    if vector_evals is not None and vector_mults is not None:
        for m2, mult in zip(vector_evals, vector_mults):
            n_dof_vector += mult
            if m2 > 1e-30:
                m4 = m2**2
                log_term = np.log(m2 / mu_sq) - c_b
                V_b += (mult / (64 * np.pi**2)) * m4 * log_term

    return V_b, n_dof_scalar, n_dof_vector


# =============================================================================
# MODULE 3: FERMIONIC CW (from tier1_coleman_weinberg.py)
# =============================================================================

def compute_fermionic_CW(eval_data, mu_sq=1.0, c_f=3.0/2.0, n_f=1):
    """
    Fermionic CW from Dirac eigenvalue data.
    V_CW^fermion = -(n_f/64pi^2) SUM_{(p,q)} dim(p,q) * SUM_j |lam_j|^4 [ln(|lam|^2/mu^2) - c_f]
    """
    V_f = 0.0
    n_dof = 0

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)
        nonzero = abs_evals[abs_evals > 1e-12]
        n_dof += d_pq * len(evals)

        if len(nonzero) == 0:
            continue

        lam4 = nonzero**4
        log_term = np.log(nonzero**2 / mu_sq) - c_f
        V_f += d_pq * np.sum(lam4 * log_term)

    V_f *= -n_f / (64 * np.pi**2)
    return V_f, n_dof


# =============================================================================
# MODULE 4: FULL V_eff COMPUTATION
# =============================================================================

def compute_full_Veff(s, gens, f_abc, gammas,
                      get_bosonic_eigenvalues,
                      max_pq_sum=6, mu_sq=1.0, c_b=3.0/2.0, c_f=3.0/2.0,
                      n_f=1, normalize_tree=True):
    """
    Compute V_eff(s) = V_tree + V_CW_boson(full tower) + V_CW_fermion.

    Args:
        s: Jensen deformation parameter
        gens, f_abc, gammas: SU(3) infrastructure
        get_bosonic_eigenvalues: function(s, max_pq_sum) -> (evals, mults, dof_info)
        max_pq_sum: truncation level for Peter-Weyl
        mu_sq: renormalization scale squared
        c_b, c_f: subtraction constants
        n_f: fermionic DOF multiplier

    Returns:
        dict with all V_eff components and diagnostics
    """
    s_val = float(np.squeeze(s))

    # Tree level
    Vt = float(np.squeeze(V_tree(s_val, normalize=normalize_tree)))

    # Bosonic CW — full tower
    # NOTE: bos_evals already contains ALL bosonic modes (scalar + vector).
    # Do NOT pass separate vector_evals — that would double-count vector modes.
    bos_evals, bos_mults, bos_info = get_bosonic_eigenvalues(s_val, max_pq_sum)
    Vb, n_dof_scalar, n_dof_vector = V_CW_boson_from_eigenvalue_array(
        s_val, bos_evals, bos_mults,
        vector_evals=None, vector_mults=None,
        mu_sq=mu_sq, c_b=c_b
    )

    # Also compute the C^2-only baseline for comparison
    Vb_C2 = float(np.squeeze(V_CW_boson_C2_only(
        np.atleast_1d(s_val), mu_sq, c_b, n_b=4
    )))

    # Fermionic CW — full Dirac tower
    _, eval_data = collect_spectrum(
        s_val, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )
    Vf, n_dof_ferm = compute_fermionic_CW(eval_data, mu_sq, c_f, n_f)

    V_total = Vt + Vb + Vf
    V_total_C2only = Vt + Vb_C2 + Vf

    # Use info dict for scalar/vector DOF breakdown (since combined array
    # is passed as "scalar" to the CW function, n_dof_vector will be 0)
    actual_scalar_dof = bos_info.get('scalar_dof', n_dof_scalar)
    actual_vector_dof = bos_info.get('vector_dof', n_dof_vector)

    return {
        'V_tree': Vt,
        'V_boson_full': Vb,
        'V_boson_C2only': Vb_C2,
        'V_fermion': Vf,
        'V_total': V_total,
        'V_total_C2only': V_total_C2only,
        'n_dof_boson_scalar': actual_scalar_dof,
        'n_dof_boson_vector': actual_vector_dof,
        'n_dof_boson_total': actual_scalar_dof + actual_vector_dof,
        'n_dof_fermion': n_dof_ferm,
        'eval_data': eval_data,
        'bos_info': bos_info,
    }


def sweep_full_Veff(s_values, gens, f_abc, gammas,
                    get_bosonic_eigenvalues,
                    max_pq_sum=6, mu_sq=1.0, c_b=3.0/2.0, c_f=3.0/2.0,
                    n_f=1, verbose=True):
    """
    Sweep V_eff over s values with full bosonic tower.
    Pre-computes Dirac eigenvalues and bosonic eigenvalues.
    """
    n_s = len(s_values)
    V_tree_arr = np.zeros(n_s)
    V_boson_full_arr = np.zeros(n_s)
    V_boson_C2_arr = np.zeros(n_s)
    V_fermion_arr = np.zeros(n_s)
    V_total_arr = np.zeros(n_s)
    V_total_C2_arr = np.zeros(n_s)
    n_dof_boson_arr = np.zeros(n_s, dtype=int)
    n_dof_ferm_arr = np.zeros(n_s, dtype=int)

    eval_data_cache = {}

    t0 = time.time()
    for i, s in enumerate(s_values):
        if verbose and (i % 10 == 0 or i == n_s - 1):
            elapsed = time.time() - t0
            rate = (i + 1) / max(elapsed, 0.01)
            eta = (n_s - i - 1) / max(rate, 0.001)
            print(f"    s={s:.3f} ({i+1}/{n_s}), "
                  f"elapsed={elapsed:.0f}s, ETA={eta:.0f}s", flush=True)

        result = compute_full_Veff(
            s, gens, f_abc, gammas, get_bosonic_eigenvalues,
            max_pq_sum=max_pq_sum, mu_sq=mu_sq, c_b=c_b, c_f=c_f, n_f=n_f
        )

        V_tree_arr[i] = result['V_tree']
        V_boson_full_arr[i] = result['V_boson_full']
        V_boson_C2_arr[i] = result['V_boson_C2only']
        V_fermion_arr[i] = result['V_fermion']
        V_total_arr[i] = result['V_total']
        V_total_C2_arr[i] = result['V_total_C2only']
        n_dof_boson_arr[i] = result['n_dof_boson_total']
        n_dof_ferm_arr[i] = result['n_dof_fermion']
        eval_data_cache[i] = result['eval_data']

    elapsed = time.time() - t0
    if verbose:
        print(f"    Sweep complete: {elapsed:.1f}s ({elapsed/n_s:.2f}s per s-value)")

    return {
        's_values': np.array(s_values),
        'V_tree': V_tree_arr,
        'V_boson_full': V_boson_full_arr,
        'V_boson_C2only': V_boson_C2_arr,
        'V_fermion': V_fermion_arr,
        'V_total': V_total_arr,
        'V_total_C2only': V_total_C2_arr,
        'n_dof_boson': n_dof_boson_arr,
        'n_dof_fermion': n_dof_ferm_arr,
        'eval_data_cache': eval_data_cache,
    }


# =============================================================================
# MODULE 5: MINIMUM FINDER (enhanced from tier1_coleman_weinberg.py)
# =============================================================================

def find_minima(s_values, V_values, verbose=True):
    """
    Find local minima of V_eff(s) from discrete data.
    Uses argrelmin then refines with parabolic fit.
    """
    indices = argrelmin(V_values, order=2)[0]
    minima = []

    for idx in indices:
        if idx < 2 or idx > len(s_values) - 3:
            continue

        # Parabolic fit around minimum
        s_local = s_values[max(0,idx-2):min(len(s_values),idx+3)]
        V_local = V_values[max(0,idx-2):min(len(V_values),idx+3)]

        if len(s_local) < 3:
            continue

        coeffs = np.polyfit(s_local, V_local, 2)
        a, b, c = coeffs

        if a > 0:  # genuine minimum
            s_min = -b / (2*a)
            V_min = a * s_min**2 + b * s_min + c
            V_second = 2 * a

            minima.append({
                's_min': s_min,
                'V_min': V_min,
                'V_second_deriv': V_second,
                'm_s_sq': V_second,
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


# =============================================================================
# MODULE 6: PREDICTION EVALUATION
# =============================================================================

def evaluate_predictions_at_s0(s0, eval_data, max_pq_sum=6):
    """
    Evaluate the Feynman prediction table at a given s_0.

    Returns dict with all predictions and pass/fail assessment.
    """
    predictions = {}

    # F1: Weinberg angle
    sin2_tW = np.exp(-4*s0) / (1 + np.exp(-4*s0))
    sin2_tW_exp = 0.23121
    delta_tW = (sin2_tW - sin2_tW_exp) / sin2_tW_exp
    in_20pct = abs(delta_tW) < 0.20
    in_10pct = abs(delta_tW) < 0.10
    in_5pct = abs(delta_tW) < 0.05

    predictions['F1_weinberg'] = {
        'sin2_tW': sin2_tW,
        'sin2_tW_exp': sin2_tW_exp,
        'delta_pct': delta_tW * 100,
        'in_20pct': in_20pct,
        'in_10pct': in_10pct,
        'in_5pct': in_5pct,
        'pass': in_20pct,
        'closure': not in_20pct and s0 < 0.24 or s0 > 0.37,
    }

    # Gauge coupling ratio
    g1_g2 = np.exp(-2*s0)
    g1_g2_exp = 0.5496  # sqrt(3/5) * tan(theta_W) at M_Z
    predictions['gauge_ratio'] = {
        'e_minus_2s': g1_g2,
        'experimental': g1_g2_exp,
        'delta_pct': (g1_g2 - g1_g2_exp) / g1_g2_exp * 100,
    }

    # B2: Sector mass ratio m(3,0)/m(0,0)
    m_30 = None
    m_00 = None
    for p, q, evals in eval_data:
        if p == 3 and q == 0:
            m_30 = np.min(np.abs(evals[np.abs(evals) > 1e-12]))
        if p == 0 and q == 0:
            m_00 = np.min(np.abs(evals[np.abs(evals) > 1e-12]))

    phi_P = 1.53158  # Paasch transcendental: ln(phi_P) = 1/phi_P^2
    if m_30 is not None and m_00 is not None:
        ratio = m_30 / m_00
        delta_phi = abs(ratio - phi_P) / phi_P
        predictions['B2_phi_ratio'] = {
            'm_30_m_00': ratio,
            'phi_P': phi_P,
            'delta_pct': delta_phi * 100,
            'within_1pct': delta_phi < 0.01,
        }

    # C2 gauge boson mass
    m2_C2 = (np.exp(s0) - np.exp(-2*s0))**2 + (1 - np.exp(-s0))**2
    predictions['C2_mass'] = {
        'm2_C2': m2_C2,
        'm_C2': np.sqrt(m2_C2),
    }

    # N_species at Lambda=1.0
    N_species = 0
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        n_below = np.sum(np.abs(evals) < 1.0)
        N_species += d_pq * n_below

    predictions['N_species'] = {
        'N_at_Lambda_1': N_species,
        'SM_fermionic': 90,
        'ratio': N_species / 90 if N_species > 0 else 0,
    }

    # F4: SM sectors lightest
    sector_mins = {}
    for p, q, evals in eval_data:
        nonzero = np.abs(evals[np.abs(evals) > 1e-12])
        if len(nonzero) > 0:
            sector_mins[(p,q)] = np.min(nonzero)

    sorted_sectors = sorted(sector_mins.items(), key=lambda x: x[1])
    lightest_3 = [s[0] for s in sorted_sectors[:3]]
    sm_sectors = {(0,0), (1,0), (0,1)}
    f4_pass = set(lightest_3) == sm_sectors

    predictions['F4_sm_lightest'] = {
        'lightest_3': lightest_3,
        'sm_sectors': list(sm_sectors),
        'pass': f4_pass,
    }

    return predictions


def format_kill_conditions(predictions, s0):
    """
    Format the pre-registered Constraint Condition results.
    """
    lines = []
    lines.append("=" * 60)
    lines.append("Constraint Condition ASSESSMENT")
    lines.append("=" * 60)

    # F1: Weinberg window
    f1 = predictions.get('F1_weinberg', {})
    f1_status = "PASS" if f1.get('pass') else "FAIL (FATAL)"
    lines.append(f"  F1 (Weinberg angle): {f1_status}")
    lines.append(f"      sin^2(theta_W) = {f1.get('sin2_tW', 'N/A'):.6f} "
                 f"(exp: {f1.get('sin2_tW_exp', 'N/A'):.5f})")
    lines.append(f"      Delta = {f1.get('delta_pct', 'N/A'):.2f}%")
    if f1.get('in_5pct'):
        lines.append(f"      Precision: within 5% -- EXCELLENT")
    elif f1.get('in_10pct'):
        lines.append(f"      Precision: within 10% -- GOOD")
    elif f1.get('in_20pct'):
        lines.append(f"      Precision: within 20% -- MARGINAL")
    else:
        lines.append(f"      Precision: OUTSIDE 20% -- FATAL")

    # s_0 range check
    if s0 is not None:
        if 0.24 <= s0 <= 0.37:
            lines.append(f"  s_0 = {s0:.6f}: IN Weinberg window [0.24, 0.37] -- PASS")
        elif s0 > 2.0:
            lines.append(f"  s_0 = {s0:.6f}: > 2.0 -- FATAL")
        else:
            lines.append(f"  s_0 = {s0:.6f}: OUTSIDE Weinberg window -- FATAL")
    else:
        lines.append(f"  s_0 = None: NO MINIMUM FOUND -- FATAL")

    # F4
    f4 = predictions.get('F4_sm_lightest', {})
    f4_status = "PASS" if f4.get('pass') else "FAIL"
    lines.append(f"  F4 (SM lightest): {f4_status}")
    lines.append(f"      Lightest 3: {f4.get('lightest_3', 'N/A')}")

    return "\n".join(lines)


# =============================================================================
# MODULE 7: CONVERGENCE ANALYSIS
# =============================================================================

def truncation_convergence(s_test, gens, f_abc, gammas,
                           get_bosonic_eigenvalues,
                           mu_sq=1.0, c_b=3.0/2.0, c_f=3.0/2.0,
                           n_f=1, pq_levels=None, verbose=True):
    """
    Test V_eff convergence with increasing max_pq_sum.
    """
    if pq_levels is None:
        pq_levels = [3, 4, 5, 6]

    results = {}
    if verbose:
        print(f"\n  Truncation convergence at s = {s_test:.3f}:")

    for pq_max in pq_levels:
        t0 = time.time()
        r = compute_full_Veff(
            s_test, gens, f_abc, gammas, get_bosonic_eigenvalues,
            max_pq_sum=pq_max, mu_sq=mu_sq, c_b=c_b, c_f=c_f, n_f=n_f
        )
        dt = time.time() - t0

        results[pq_max] = {
            'V_total': r['V_total'],
            'V_boson': r['V_boson_full'],
            'V_fermion': r['V_fermion'],
            'n_dof_boson': r['n_dof_boson_total'],
            'n_dof_fermion': r['n_dof_fermion'],
            'time': dt,
        }

        if verbose:
            print(f"    pq_max={pq_max}: V_total={r['V_total']:.6e}, "
                  f"V_b={r['V_boson_full']:.6e}, V_f={r['V_fermion']:.6e}, "
                  f"DOF_b={r['n_dof_boson_total']}, DOF_f={r['n_dof_fermion']}, "
                  f"time={dt:.1f}s")

    # Convergence metric between successive levels
    metrics = {}
    sorted_pq = sorted(results.keys())
    for i in range(1, len(sorted_pq)):
        pq_lo = sorted_pq[i-1]
        pq_hi = sorted_pq[i]
        V_lo = results[pq_lo]['V_total']
        V_hi = results[pq_hi]['V_total']
        if abs(V_hi) > 1e-30:
            rel = abs(V_hi - V_lo) / abs(V_hi)
        else:
            rel = float('inf')
        metrics[(pq_lo, pq_hi)] = rel
        if verbose:
            pct = rel * 100
            status = "CONVERGED" if rel < 0.1 else ("MARGINAL" if rel < 0.3 else "NOT CONVERGED")
            print(f"    |V({pq_hi})-V({pq_lo})|/|V({pq_hi})| = {pct:.1f}% -- {status}")

    results['metrics'] = metrics
    return results


# =============================================================================
# MODULE 8: DOF BUDGET REPORT
# =============================================================================

def dof_budget_report(s_values, n_dof_boson, n_dof_fermion, bos_info=None):
    """
    Report the DOF budget at several s-values.
    """
    lines = []
    lines.append("=" * 60)
    lines.append("DOF BUDGET (Bosonic vs Fermionic)")
    lines.append("=" * 60)
    lines.append(f"  {'s':>6}  {'N_boson':>8}  {'N_fermion':>10}  {'Ratio B/F':>10}  {'Net sign':>10}")
    lines.append(f"  {'-'*6}  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}")

    for i in range(len(s_values)):
        nb = n_dof_boson[i] if i < len(n_dof_boson) else 0
        nf = n_dof_fermion[i] if i < len(n_dof_fermion) else 0
        ratio = nb / nf if nf > 0 else float('inf')
        net = "BOSON-dom" if nb > nf else "FERMI-dom"
        lines.append(f"  {s_values[i]:6.3f}  {nb:8d}  {nf:10d}  {ratio:10.2f}  {net:>10}")

    if bos_info is not None:
        lines.append("")
        lines.append("  Bosonic mode breakdown:")
        for key, val in bos_info.items():
            if key not in ('vector_evals', 'vector_mults'):
                lines.append(f"    {key}: {val}")

    return "\n".join(lines)


# =============================================================================
# MODULE 9: PLOT GENERATION
# =============================================================================

def generate_plots(sweep_data, minima, save_prefix=None):
    """
    Generate comprehensive V_eff plots.
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available; skipping plots.")
        return

    s = sweep_data['s_values']

    if save_prefix is None:
        save_prefix = os.path.join(SCRIPT_DIR, 'h5_veff')

    # Figure 1: Components + total (4 panels)
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('H-5: Full Coleman-Weinberg V_eff(s) — Complete Bosonic Tower\n'
                 'Session 18: The Decisive Computation',
                 fontsize=14, fontweight='bold')

    # Panel 1: All components
    ax = axes[0, 0]
    ax.plot(s, sweep_data['V_tree'], 'b-', lw=2, label='V_tree')
    ax.plot(s, sweep_data['V_boson_full'], 'r-', lw=2, label='V_boson (FULL tower)')
    ax.plot(s, sweep_data['V_boson_C2only'], 'r--', lw=1, alpha=0.5, label='V_boson (4 C^2 only)')
    ax.plot(s, sweep_data['V_fermion'], 'g-', lw=2, label='V_fermion (Dirac)')
    ax.plot(s, sweep_data['V_total'], 'k-', lw=3, label='V_total (FULL)')
    ax.plot(s, sweep_data['V_total_C2only'], 'k--', lw=1.5, alpha=0.5, label='V_total (C^2 only)')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('V_eff')
    ax.set_title('V_eff Components')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', ls=':', lw=0.5)

    # Mark minima
    for m in minima:
        ax.axvline(x=m['s_min'], color='magenta', ls='--', lw=1, alpha=0.7)
        ax.plot(m['s_min'], m['V_min'], 'mo', markersize=10)

    # Panel 2: V_total zoomed near minimum
    ax = axes[0, 1]
    ax.plot(s, sweep_data['V_total'], 'k-', lw=2, label='V_total (FULL)')
    ax.plot(s, sweep_data['V_total_C2only'], 'gray', ls='--', lw=1.5, label='V_total (C^2 only)')
    # Weinberg window
    ax.axvspan(0.24, 0.37, alpha=0.1, color='green', label='Weinberg window')
    for m in minima:
        ax.axvline(x=m['s_min'], color='magenta', ls='--', lw=1)
        ax.plot(m['s_min'], m['V_min'], 'mo', markersize=10)
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('V_total')
    ax.set_title('V_total with Weinberg Window')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    if minima:
        s_center = minima[0]['s_min']
        ax.set_xlim(max(0, s_center - 0.5), min(2.5, s_center + 0.5))

    # Panel 3: DOF budget
    ax = axes[1, 0]
    ax.plot(s, sweep_data['n_dof_boson'], 'r-', lw=2, label='Bosonic DOF')
    ax.plot(s, sweep_data['n_dof_fermion'], 'g-', lw=2, label='Fermionic DOF')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('Number of DOF')
    ax.set_title('DOF Budget')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 4: Summary text
    ax = axes[1, 1]
    ax.axis('off')
    if minima:
        m = minima[0]
        sin2 = np.exp(-4*m['s_min']) / (1 + np.exp(-4*m['s_min']))
        summary = (
            f"RESULT SUMMARY\n"
            f"{'='*40}\n\n"
            f"Minimum found: YES\n"
            f"s_0 = {m['s_min']:.6f}\n"
            f"V_eff(s_0) = {m['V_min']:.6e}\n"
            f"V''(s_0) = {m['V_second_deriv']:.6e}\n\n"
            f"sin^2(theta_W) = {sin2:.6f}\n"
            f"(experimental: 0.23121)\n"
            f"Delta = {(sin2-0.23121)/0.23121*100:.2f}%\n\n"
            f"e^(-2s_0) = {np.exp(-2*m['s_min']):.6f}\n"
            f"(gauge coupling ratio)\n\n"
        )
        if 0.24 <= m['s_min'] <= 0.37:
            summary += "Weinberg window: IN WINDOW\n"
        else:
            summary += "Weinberg window: OUTSIDE\n"
    else:
        summary = (
            f"RESULT SUMMARY\n"
            f"{'='*40}\n\n"
            f"Minimum found: NO\n"
            f"V_eff is monotonically decreasing\n"
            f"(runaway to large s)\n\n"
            f"Constraint Condition: DECISIVE CLOSURE\n"
            f"No minimum at any s > 0\n"
        )

    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=10, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    save_path = f"{save_prefix}_components.png"
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {save_path}")
    plt.close()

    return save_path


# =============================================================================
# MODULE 10: PARAMETER SWEEP (mu dependence)
# =============================================================================

def mu_sweep(s_values, gens, f_abc, gammas, get_bosonic_eigenvalues,
             mu_values=None, max_pq_sum=6, c_b=3.0/2.0, c_f=3.0/2.0,
             n_f=1, verbose=True):
    """
    Sweep over mu values to assess scheme dependence.
    """
    if mu_values is None:
        mu_values = [0.5, 1.0, 1.5, 2.0, 3.0]

    results = {}
    for mu in mu_values:
        if verbose:
            print(f"\n  mu = {mu:.2f}:")
        sweep = sweep_full_Veff(
            s_values, gens, f_abc, gammas, get_bosonic_eigenvalues,
            max_pq_sum=max_pq_sum, mu_sq=mu**2, c_b=c_b, c_f=c_f,
            n_f=n_f, verbose=verbose
        )
        minima = find_minima(s_values, sweep['V_total'], verbose=verbose)

        results[mu] = {
            'sweep': sweep,
            'minima': minima,
        }

    return results


# =============================================================================
# MODULE 11: MEETING MINUTES GENERATOR
# =============================================================================

def generate_minutes(sweep_data, minima, predictions, conv_results,
                     dof_report, mu_results=None, c1_diagnostic=None):
    """
    Generate Session 18 meeting minutes.
    """
    lines = []
    lines.append("# Session 18: V_eff Convergence — The Eclipse Expedition")
    lines.append("")
    lines.append("## Date: 2026-02-15")
    lines.append("## Session: 18")
    lines.append("## Agents: Hawking-Theorist (computation + writer), "
                 "KK-Theorist (bosonic tower), Baptista-Spacetime-Analyst "
                 "(scalar/vector Laplacian), Connes-NCG-Theorist (convergence)")
    lines.append("## Branch: Valar-1")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Executive Summary
    lines.append("## I. Executive Summary")
    lines.append("")
    if minima:
        m = minima[0]
        sin2 = np.exp(-4*m['s_min']) / (1 + np.exp(-4*m['s_min']))
        in_window = 0.24 <= m['s_min'] <= 0.37
        lines.append(f"The full Coleman-Weinberg V_eff with complete bosonic KK tower "
                     f"{'produces' if minima else 'does NOT produce'} a minimum at "
                     f"s_0 = {m['s_min']:.6f}. "
                     f"{'This IS' if in_window else 'This is NOT'} within the Weinberg "
                     f"window [0.24, 0.37]. The predicted Weinberg angle is "
                     f"sin^2(theta_W) = {sin2:.6f} "
                     f"(experimental: 0.23121, delta = {(sin2-0.23121)/0.23121*100:.1f}%).")
    else:
        lines.append("The full Coleman-Weinberg V_eff with complete bosonic KK tower "
                     "produces NO minimum at any s > 0. The potential remains "
                     "monotonically decreasing (runaway instability). This is a "
                     "FATAL Constraint Condition.")
    lines.append("")

    # DOF Budget
    lines.append("---")
    lines.append("")
    lines.append("## II. DOF Budget")
    lines.append("")
    lines.append("```")
    lines.append(dof_report)
    lines.append("```")
    lines.append("")

    # V_eff Results
    lines.append("---")
    lines.append("")
    lines.append("## III. V_eff Results")
    lines.append("")

    if minima:
        lines.append("### Minima Found")
        lines.append("")
        lines.append("| # | s_min | V_eff(s_min) | V''(s_min) | In Weinberg? |")
        lines.append("|:--|:------|:-------------|:-----------|:-------------|")
        for i, m in enumerate(minima):
            in_w = "YES" if 0.24 <= m['s_min'] <= 0.37 else "NO"
            lines.append(f"| {i+1} | {m['s_min']:.6f} | {m['V_min']:.6e} | "
                        f"{m['V_second_deriv']:.6e} | {in_w} |")
        lines.append("")
    else:
        lines.append("### NO MINIMA FOUND")
        lines.append("")
        lines.append("V_eff is monotonically decreasing for all s > 0.")
        lines.append("")

    # Predictions
    lines.append("---")
    lines.append("")
    lines.append("## IV. Prediction Table at s_0")
    lines.append("")
    if predictions:
        f1 = predictions.get('F1_weinberg', {})
        gr = predictions.get('gauge_ratio', {})
        b2 = predictions.get('B2_phi_ratio', {})
        c2 = predictions.get('C2_mass', {})
        ns = predictions.get('N_species', {})

        lines.append("| Prediction | Value | Experimental | Delta |")
        lines.append("|:-----------|:------|:-------------|:------|")
        lines.append(f"| sin^2(theta_W) | {f1.get('sin2_tW', 'N/A'):.6f} | "
                    f"0.23121 | {f1.get('delta_pct', 'N/A'):.2f}% |")
        lines.append(f"| g_1/g_2 = e^(-2s) | {gr.get('e_minus_2s', 'N/A'):.6f} | "
                    f"0.5496 | {gr.get('delta_pct', 'N/A'):.2f}% |")
        if b2:
            lines.append(f"| m(3,0)/m(0,0) | {b2.get('m_30_m_00', 'N/A'):.6f} | "
                        f"phi_P = 1.53158 | {b2.get('delta_pct', 'N/A'):.4f}% |")
        lines.append(f"| m(C^2) | {c2.get('m_C2', 'N/A'):.6f} | - | - |")
        lines.append(f"| N_species(Lambda=1) | {ns.get('N_at_Lambda_1', 'N/A')} | "
                    f"SM=90 | ratio={ns.get('ratio', 'N/A'):.2f} |")
    lines.append("")

    # Constraint Conditions
    lines.append("---")
    lines.append("")
    lines.append("## V. Constraint Condition Assessment")
    lines.append("")
    if predictions and minima:
        lines.append(format_kill_conditions(predictions, minima[0]['s_min']))
    elif not minima:
        lines.append("FATAL: No minimum at any s > 0.")
    lines.append("")

    # Convergence
    lines.append("---")
    lines.append("")
    lines.append("## VI. Convergence Diagnostic")
    lines.append("")
    if conv_results:
        lines.append("### Truncation convergence")
        lines.append("")
        lines.append("| max_pq_sum | V_total | V_boson | V_fermion | DOF_b | DOF_f | time |")
        lines.append("|:-----------|:--------|:--------|:----------|:------|:------|:-----|")
        for pq in sorted(k for k in conv_results.keys() if isinstance(k, int)):
            r = conv_results[pq]
            lines.append(f"| {pq} | {r['V_total']:.6e} | {r['V_boson']:.6e} | "
                        f"{r['V_fermion']:.6e} | {r['n_dof_boson']} | {r['n_dof_fermion']} | "
                        f"{r['time']:.1f}s |")
        lines.append("")

        metrics = conv_results.get('metrics', {})
        for (lo, hi), rel in metrics.items():
            status = "CONVERGED" if rel < 0.1 else ("MARGINAL" if rel < 0.3 else "NOT CONVERGED")
            lines.append(f"  |V({hi})-V({lo})|/|V({hi})| = {rel*100:.1f}% -- {status}")
    lines.append("")

    # C-1 diagnostic
    if c1_diagnostic:
        lines.append("### Seeley-DeWitt Assessment (C-1)")
        lines.append("")
        lines.append(c1_diagnostic)
        lines.append("")

    # mu dependence
    if mu_results:
        lines.append("---")
        lines.append("")
        lines.append("## VII. mu Dependence")
        lines.append("")
        lines.append("| mu | # minima | s_min (deepest) | V_min | in Weinberg? |")
        lines.append("|:---|:---------|:----------------|:------|:-------------|")
        for mu in sorted(mu_results.keys()):
            r = mu_results[mu]
            n_min = len(r['minima'])
            if n_min > 0:
                best = min(r['minima'], key=lambda m: m['V_min'])
                in_w = "YES" if 0.24 <= best['s_min'] <= 0.37 else "NO"
                lines.append(f"| {mu:.2f} | {n_min} | {best['s_min']:.6f} | "
                            f"{best['V_min']:.6e} | {in_w} |")
            else:
                lines.append(f"| {mu:.2f} | 0 | - | - | - |")
        lines.append("")

    # Framework probability placeholder
    lines.append("---")
    lines.append("")
    lines.append("## VIII. Framework Probability Assessment")
    lines.append("")
    lines.append("*[To be filled after full analysis]*")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("End of Session 18 minutes.")

    return "\n".join(lines)


# =============================================================================
# MODULE 12: BOSONIC EIGENVALUE INTERFACE (placeholder until B-6/KK-1 deliver)
# =============================================================================

def get_bosonic_eigenvalues_C2_only(s, max_pq_sum=6):
    """
    BASELINE (Session 17a): Only 4 C^2 gauge boson masses.
    This will be replaced by the full tower from B-6/KK-1.
    """
    m2_C2 = (np.exp(s) - np.exp(-2*s))**2 + (1 - np.exp(-s))**2
    # 4 C^2 gauge bosons (massive), 4 u(2) gauge bosons (massless)
    evals = np.array([m2_C2, m2_C2, m2_C2, m2_C2, 0.0, 0.0, 0.0, 0.0])
    mults = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    info = {
        'mode_types': ['C2']*4 + ['u2']*4,
        'total_dof': 8,
        'n_massive': 4,
        'n_massless': 4,
        'source': 'C2_only_baseline',
    }
    return evals, mults, info


def get_bosonic_eigenvalues_full(s, max_pq_sum=6):
    """
    FULL TOWER from KK-1 (kk1_bosonic_tower.py).

    Uses bosonic_spectrum_at_s() which computes:
    - Scalar Laplacian eigenvalues (p+q <= max_pq_sum)
    - Vector (Hodge) Laplacian eigenvalues (p+q <= min(max_pq_sum, 4))
    - Baptista gauge boson masses (4 C^2 modes, eq 3.84)

    Returns:
        evals: array of bosonic eigenvalues (mass-squared)
        mults: array of multiplicities (PW weight included)
        info: dict with breakdown
    """
    try:
        from kk1_bosonic_tower import bosonic_spectrum_at_s
    except ImportError:
        print("  WARNING: kk1_bosonic_tower not available. Using C^2-only baseline.")
        return get_bosonic_eigenvalues_C2_only(s, max_pq_sum)

    vec_max_pq = min(max_pq_sum, 4)
    result = bosonic_spectrum_at_s(s, max_pq_scalar=max_pq_sum, max_pq_vector=vec_max_pq)

    all_evals = []
    all_mults = []
    scalar_dof = 0
    vector_dof = 0

    for ev, mult in result['scalar_eigs']:
        all_evals.append(ev)
        all_mults.append(mult)
        scalar_dof += mult

    vec_evals_arr = []
    vec_mults_arr = []
    for ev, mult in result['vector_eigs']:
        all_evals.append(ev)
        all_mults.append(mult)
        vec_evals_arr.append(ev)
        vec_mults_arr.append(mult)
        vector_dof += mult

    info = {
        'n_scalar_entries': result['n_scalar'],
        'n_vector_entries': result['n_vector'],
        'scalar_dof': scalar_dof,
        'vector_dof': vector_dof,
        'total_dof': scalar_dof + vector_dof,
        'source': 'kk1_full_tower',
        'scalar_max_pq': max_pq_sum,
        'vector_max_pq': vec_max_pq,
        'gauge_boson_m2': result['gauge_boson_m2'],
        'vector_evals': np.array(vec_evals_arr) if vec_evals_arr else None,
        'vector_mults': np.array(vec_mults_arr) if vec_mults_arr else None,
    }

    return np.array(all_evals), np.array(all_mults), info


# Cache for SU(3) infrastructure (avoid recomputing for every s-value)
_CACHED_GENS = None
_CACHED_FABC = None

def _get_cached_gens():
    global _CACHED_GENS
    if _CACHED_GENS is None:
        _CACHED_GENS = su3_generators()
    return _CACHED_GENS

def _get_cached_fabc():
    global _CACHED_FABC, _CACHED_GENS
    if _CACHED_FABC is None:
        if _CACHED_GENS is None:
            _CACHED_GENS = su3_generators()
        _CACHED_FABC = compute_structure_constants(_CACHED_GENS)
    return _CACHED_FABC


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("=" * 80)
    print("H-5: FULL COLEMAN-WEINBERG V_eff WITH COMPLETE BOSONIC TOWER")
    print("Session 18 — The Eclipse Expedition")
    print("=" * 80)

    t_start = time.time()

    # --- Infrastructure ---
    print("\n[1] Building SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford algebra error: {cliff_err:.2e}")

    # --- Select bosonic eigenvalue source ---
    print(f"\n[2] Selecting bosonic eigenvalue source...")

    # Try to import the full tower
    try:
        from b6_scalar_vector_laplacian import compute_scalar_laplacian_eigenvalues
        print(f"  FULL TOWER available from B-6.")
        get_bos_evals = get_bosonic_eigenvalues_full
        bosonic_source = "FULL (B-6/KK-1)"
    except ImportError:
        print(f"  B-6 not available. Using C^2-only baseline.")
        get_bos_evals = get_bosonic_eigenvalues_C2_only
        bosonic_source = "C^2-only (4 DOF)"

    # --- Test at s=0 and s=1 ---
    print(f"\n[3] Testing bosonic eigenvalues...")
    for s_test in [0.0, 0.5, 1.0]:
        evals, mults, info = get_bos_evals(s_test, max_pq_sum=6)
        n_nonzero = np.sum(evals > 1e-30)
        total_dof = np.sum(mults)
        print(f"  s={s_test:.1f}: {len(evals)} eigenvalues, "
              f"{n_nonzero} massive, total DOF={total_dof}, source={info.get('source','?')}")

    # --- Reference V_eff at s=1.0 ---
    print(f"\n[4] Reference V_eff decomposition at s=1.0...")
    ref = compute_full_Veff(
        1.0, gens, f_abc, gammas, get_bos_evals,
        max_pq_sum=6, mu_sq=1.0
    )
    print(f"  V_tree(1.0)        = {ref['V_tree']:.6e}")
    print(f"  V_boson_full(1.0)  = {ref['V_boson_full']:.6e}")
    print(f"  V_boson_C2(1.0)    = {ref['V_boson_C2only']:.6e}")
    print(f"  V_fermion(1.0)     = {ref['V_fermion']:.6e}")
    print(f"  V_total(1.0)       = {ref['V_total']:.6e}")
    print(f"  V_total_C2(1.0)    = {ref['V_total_C2only']:.6e}")
    print(f"  DOF: boson={ref['n_dof_boson_total']}, fermion={ref['n_dof_fermion']}")
    if abs(ref['V_boson_full']) > 1e-30:
        ratio = abs(ref['V_fermion'] / ref['V_boson_full'])
        print(f"  |V_ferm/V_boson_full| = {ratio:.2f}")
    if abs(ref['V_boson_C2only']) > 1e-30:
        ratio_C2 = abs(ref['V_fermion'] / ref['V_boson_C2only'])
        print(f"  |V_ferm/V_boson_C2|   = {ratio_C2:.2f} (Session 17a comparison)")

    # --- Truncation convergence ---
    print(f"\n{'='*80}")
    print("[5] Truncation convergence test at s=1.0...")
    conv = truncation_convergence(
        1.0, gens, f_abc, gammas, get_bos_evals,
        mu_sq=1.0, pq_levels=[3, 4, 5, 6], verbose=True
    )

    # --- FULL SWEEP ---
    print(f"\n{'='*80}")
    print(f"[6] FULL V_eff SWEEP (mu=1.0)")
    print(f"  Bosonic source: {bosonic_source}")

    s_values = np.linspace(0.0, 2.5, 101)
    sweep = sweep_full_Veff(
        s_values, gens, f_abc, gammas, get_bos_evals,
        max_pq_sum=6, mu_sq=1.0, verbose=True
    )

    # --- Find minima ---
    print(f"\n{'='*80}")
    print("[7] Finding minima...")
    minima = find_minima(s_values, sweep['V_total'], verbose=True)

    # --- DOF budget ---
    dof_report = dof_budget_report(
        s_values[::10], sweep['n_dof_boson'][::10], sweep['n_dof_fermion'][::10]
    )
    print(f"\n{dof_report}")

    # --- Evaluate predictions ---
    predictions = None
    if minima:
        best = min(minima, key=lambda m: m['V_min'])
        s0 = best['s_min']
        print(f"\n{'='*80}")
        print(f"[8] Evaluating predictions at s_0 = {s0:.6f}...")

        # Get eval_data at closest s
        idx_s0 = np.argmin(np.abs(s_values - s0))
        eval_data_s0 = sweep['eval_data_cache'].get(idx_s0)
        if eval_data_s0 is None:
            _, eval_data_s0 = collect_spectrum(
                s0, gens, f_abc, gammas, max_pq_sum=6, verbose=False
            )

        predictions = evaluate_predictions_at_s0(s0, eval_data_s0)

        # Print prediction table
        print(f"\n  Prediction table at s_0 = {s0:.6f}:")
        f1 = predictions.get('F1_weinberg', {})
        print(f"    sin^2(theta_W) = {f1.get('sin2_tW', 'N/A'):.6f} "
              f"(exp: 0.23121, delta={f1.get('delta_pct', 'N/A'):.2f}%)")
        gr = predictions.get('gauge_ratio', {})
        print(f"    g_1/g_2 = e^(-2s_0) = {gr.get('e_minus_2s', 'N/A'):.6f} "
              f"(exp: 0.5496, delta={gr.get('delta_pct', 'N/A'):.2f}%)")
        b2 = predictions.get('B2_phi_ratio', {})
        if b2:
            print(f"    m(3,0)/m(0,0) = {b2.get('m_30_m_00', 'N/A'):.6f} "
                  f"(phi_P=1.53158, delta={b2.get('delta_pct', 'N/A'):.4f}%)")
        c2 = predictions.get('C2_mass', {})
        print(f"    m(C^2) = {c2.get('m_C2', 'N/A'):.6f}")
        ns = predictions.get('N_species', {})
        print(f"    N_species(Lambda=1) = {ns.get('N_at_Lambda_1', 'N/A')} "
              f"(SM=90, ratio={ns.get('ratio', 'N/A'):.2f})")

        # Constraint Conditions
        print(f"\n{format_kill_conditions(predictions, s0)}")
    else:
        print(f"\n{'='*80}")
        print("[8] NO MINIMUM FOUND — DECISIVE CLOSURE Constraint Condition")
        print("    V_eff remains monotonically decreasing.")
        print("    The full bosonic tower does NOT stabilize the Jensen modulus.")

    # --- mu sweep ---
    print(f"\n{'='*80}")
    print("[9] mu dependence sweep...")
    mu_results = mu_sweep(
        s_values, gens, f_abc, gammas, get_bos_evals,
        mu_values=[0.5, 1.0, 2.0, 3.0],
        max_pq_sum=6, verbose=True
    )

    # Print mu summary
    print(f"\n  mu sweep summary:")
    for mu in sorted(mu_results.keys()):
        r = mu_results[mu]
        n_min = len(r['minima'])
        if n_min > 0:
            best = min(r['minima'], key=lambda m: m['V_min'])
            print(f"    mu={mu:.2f}: {n_min} minimum/minima, "
                  f"deepest s_0={best['s_min']:.6f}")
        else:
            print(f"    mu={mu:.2f}: no minimum (monotonic)")

    # --- Generate plots ---
    print(f"\n{'='*80}")
    print("[10] Generating plots...")
    plot_path = generate_plots(sweep, minima)

    # --- Generate minutes ---
    print(f"\n{'='*80}")
    print("[11] Generating meeting minutes...")
    minutes = generate_minutes(
        sweep, minima, predictions, conv,
        dof_report, mu_results=mu_results,
        c1_diagnostic=None  # Will be filled when C-1 delivers
    )

    minutes_path = os.path.join(
        os.path.dirname(SCRIPT_DIR),
        'meeting-minutes',
        'session-18-veff-convergence.md'
    )
    with open(minutes_path, 'w', encoding='utf-8') as f:
        f.write(minutes)
    print(f"  Minutes written to: {minutes_path}")

    # --- FINAL SUMMARY ---
    t_total = time.time() - t_start
    print(f"\n{'='*80}")
    print("FINAL SUMMARY")
    print("=" * 80)

    print(f"\n  Bosonic source: {bosonic_source}")
    print(f"  DOF at s=1: boson={ref['n_dof_boson_total']}, "
          f"fermion={ref['n_dof_fermion']}")

    if minima:
        best = min(minima, key=lambda m: m['V_min'])
        sin2 = np.exp(-4*best['s_min']) / (1 + np.exp(-4*best['s_min']))
        print(f"\n  MINIMUM FOUND: s_0 = {best['s_min']:.6f}")
        print(f"  sin^2(theta_W) = {sin2:.6f}")
        print(f"  e^(-2s_0) = {np.exp(-2*best['s_min']):.6f}")

        if 0.24 <= best['s_min'] <= 0.37:
            print(f"\n  WEINBERG WINDOW: PASS")
            print(f"  THIS IS A LEVEL 3 PREDICTION.")
        else:
            print(f"\n  WEINBERG WINDOW: FAIL")
            print(f"  Constraint Condition F1 triggered.")
    else:
        print(f"\n  NO MINIMUM: DECISIVE CLOSURE Constraint Condition")

    print(f"\n  Total time: {t_total:.1f}s ({t_total/60:.1f}min)")
    print(f"\n{'='*80}")
    print("H-5 COMPUTATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
