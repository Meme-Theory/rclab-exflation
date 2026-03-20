#!/usr/bin/env python3
"""
s30b_full_spectrum.py — Full Dirac Spectrum at Candidate Points (Session 30Bb Steps 3, 5, 5b)
==============================================================================================

Computes the full Dirac spectrum at N_max=6 for two candidate evaluation points
on the U(2)-invariant surface:

  Candidate 1 (Gradient-balance): tau=0.180, eps=-0.135
    - Where BCS and spectral action gradients cancel at Lambda_crit=1.12
    - sin2_B = 0.585 (far from SM)

  Candidate 2 (SM Weinberg contour): tau=0.575, eps=-0.005
    - On the sin^2(theta_W) = 0.231 contour (Formula B)
    - Near Jensen (eps ~ 0), low V_total region

At each point, computes:
  Step 3: phi_paasch, PMNS angles (tridiagonal Kosmann), full eigenvalue list, F_BCS
  Step 5: Level statistics P(s), avoided crossings, spectral gap, sector composition,
          AZ class (T^2, C^2), DOS at band edge
  Step 5b: Order-one condition ||[[D_K, a], b^o]|| for factor pairs

Gate classifications:
  P-30phi:   m_(3,0)/m_(0,0) in [1.52, 1.54]
  P-30golden: m_(3,0)/m_(0,0) in [1.610, 1.626]
  P-30pmns:  sin^2(theta_13) in [0.015, 0.030] AND theta_23 in [40, 55] deg
  AZ-1:      class = BDI
  DOS-1:     DOS at candidate > DOS at Jensen (tau=0.35)

Author: phonon-exflation-sim agent, Session 30Bb
Date: 2026-03-01
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh, norm, inv
from scipy.linalg import eigh as scipy_eigh
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    u2_invariant_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    get_irrep, dirac_operator_on_irrep, validate_connection,
    validate_omega_hermitian, _irrep_cache
)

# Try to import Kosmann operator
from s23a_kosmann_singlet import kosmann_operator_antisymmetric

from pathlib import Path

DATA_DIR = Path(SCRIPT_DIR)
OUT_NPZ = DATA_DIR / 's30b_full_spectrum.npz'
OUT_TXT = DATA_DIR / 's30b_full_spectrum_results.txt'

# =============================================================================
# PARAMETERIZATION
# =============================================================================
T2_DIR = np.array([-11.0, -7.0, 8.0])
N_T2 = np.sqrt(np.dot(T2_DIR, T2_DIR))

def tau_eps_to_lambdas(tau, eps):
    """Convert (tau, eps) to (L1, L2, L3) on volume-preserving surface."""
    L1 = np.exp(2.0 * tau - 11.0 * eps / N_T2)
    L2 = np.exp(-2.0 * tau - 7.0 * eps / N_T2)
    L3 = np.exp(tau + 8.0 * eps / N_T2)
    return L1, L2, L3

# Candidate points
CANDIDATES = {
    'gradient_balance': {'tau': 0.180, 'eps': -0.135, 'label': 'Gradient-balance'},
    'sm_weinberg': {'tau': 0.575, 'eps': -0.005, 'label': 'SM Weinberg contour'},
}

# Jensen reference point for DOS comparison
JENSEN_REF = {'tau': 0.35, 'eps': 0.0, 'label': 'Jensen reference'}

# Physics
MAX_PQ_SUM = 6  # Full N_max=6 computation
LOAD_BEARING = [(0, 0), (3, 0), (0, 3)]
PW_MULT = {}  # Will be filled dynamically
RHO_SPEC = 0.01
DELTA_E_DOS = 0.05

# Gate thresholds
PHI_PAASCH_TARGET = 1.53158
GOLDEN_RATIO = (1 + np.sqrt(5)) / 2

# Output log
log_lines = []
def log(msg):
    print(msg)
    log_lines.append(msg)


# =============================================================================
# MODULE 1: Full Dirac spectrum at a single point
# =============================================================================

def compute_full_dirac(B_ab, gens, f_abc, gammas, L1, L2, L3, max_pq=MAX_PQ_SUM,
                       compute_eigenvectors=False):
    """
    Compute the full Dirac spectrum at a U(2)-invariant metric point.

    Returns
    -------
    sector_data : list of dicts
        Each dict has keys: 'p', 'q', 'dim_rho', 'abs_evals', 'raw_evals',
        optionally 'evecs', 'D_pi'.
    infra : dict
        Geometric infrastructure (E, Gamma, Omega, g, ft).
    """
    g = u2_invariant_metric(B_ab, L1, L2, L3)
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    mc_err = validate_connection(Gamma)
    _, is_ah, _, ah_err = validate_omega_hermitian(Omega)

    infra = {
        'E': E, 'Gamma': Gamma, 'Omega': Omega,
        'B_ab': B_ab, 'g': g, 'ft': ft,
        'mc_err': mc_err, 'ah_err': ah_err,
    }

    sector_data = []
    _irrep_cache.clear()

    # Enumerate irreps
    irreps = [(0, 0, 1)]
    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            irreps.append((p, q, dim_pq))

    for p, q, dim_pq in irreps:
        t0 = time.time()
        try:
            if (p, q) == (0, 0):
                D_pi = Omega.copy()
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

            # Anti-Hermiticity check
            ah = np.max(np.abs(D_pi + D_pi.conj().T))

            if compute_eigenvectors:
                H = 1j * D_pi
                evals, evecs = scipy_eigh(H)
                raw_evals = -1j * evals  # Dirac eigenvalues (purely imaginary)
            else:
                evals_raw = np.linalg.eigvals(D_pi)
                evals = np.sort(np.imag(evals_raw))  # imaginary parts, sorted
                raw_evals = evals_raw
                evecs = None

            abs_evals = np.sort(np.abs(evals))
            dt = time.time() - t0

            entry = {
                'p': p, 'q': q, 'dim_rho': dim_pq,
                'abs_evals': abs_evals,
                'raw_evals': raw_evals if not compute_eigenvectors else evals,
                'ah_err': ah,
                'time': dt,
            }
            if compute_eigenvectors:
                entry['evecs'] = evecs
                entry['D_pi'] = D_pi

            sector_data.append(entry)

            D_size = dim_pq * 16
            nonzero = abs_evals[abs_evals > 1e-14]
            lmin = nonzero[0] if len(nonzero) > 0 else np.inf
            log(f"    ({p},{q}): dim={dim_pq}, D={D_size}x{D_size}, "
                f"|lam|=[{np.min(abs_evals):.4f},{np.max(abs_evals):.4f}], "
                f"lmin={lmin:.6f}, ah={ah:.1e}, {dt:.2f}s")

        except Exception as e:
            log(f"    ({p},{q}): FAILED ({e})")
            continue

    return sector_data, infra


# =============================================================================
# MODULE 2: Observable extraction
# =============================================================================

def extract_observables(sector_data, L1, L2, L3):
    """Extract physical observables from sector data."""
    results = {}

    # --- Global lambda_min ---
    all_lmin = []
    lmin_per_sector = {}
    for sd in sector_data:
        pq = (sd['p'], sd['q'])
        nonzero = sd['abs_evals'][sd['abs_evals'] > 1e-14]
        lmin = nonzero[0] if len(nonzero) > 0 else np.inf
        lmin_per_sector[pq] = lmin
        all_lmin.append(lmin)
    results['lambda_min'] = min(all_lmin)
    results['lmin_per_sector'] = lmin_per_sector

    # --- phi_paasch: m_(3,0)/m_(0,0) ---
    lmin_00 = lmin_per_sector.get((0, 0), np.inf)
    lmin_30 = lmin_per_sector.get((3, 0), np.inf)
    lmin_03 = lmin_per_sector.get((0, 3), np.inf)
    results['phi_30'] = lmin_30 / lmin_00 if lmin_00 > 0 else np.inf
    results['phi_03'] = lmin_03 / lmin_00 if lmin_00 > 0 else np.inf
    results['lmin_00'] = lmin_00
    results['lmin_30'] = lmin_30
    results['lmin_03'] = lmin_03

    # --- Weinberg angle (Formula B) ---
    results['sin2_B'] = 3 * L2 / (L1 + 3 * L2)
    results['sin2_A'] = L2 / (L1 + L2)
    results['g1g2'] = np.sqrt(L2 / L1)

    # --- V_spec ---
    Lambda_sq = 1.0 / RHO_SPEC**2
    V_spec = 0.0
    for sd in sector_data:
        dim_pq = sd['dim_rho']
        for ev in sd['abs_evals']:
            V_spec += dim_pq * np.exp(-ev**2 / Lambda_sq)
    results['V_spec'] = V_spec

    # --- F_BCS 3-sector ---
    for mu_ratio in [1.0, 1.2]:
        mu = mu_ratio * results['lambda_min']
        F_BCS = 0.0
        for pq in LOAD_BEARING:
            sd_match = [s for s in sector_data if (s['p'], s['q']) == pq]
            if not sd_match:
                continue
            evals_pos = sd_match[0]['abs_evals']
            evals_pos = evals_pos[evals_pos > 1e-14]
            xi = evals_pos - mu
            super_mask = xi < 0
            n_super = int(np.sum(super_mask))
            if n_super > 0:
                F_cond = -np.sum(np.abs(xi[super_mask]))
            else:
                F_cond = 0.0
            dim_pq = sd_match[0]['dim_rho']
            pw = dim_pq**2 if pq != (0, 0) else 1
            F_BCS += pw * F_cond
        results[f'F_BCS_{mu_ratio:.1f}'] = F_BCS

    # --- DOS ---
    lmin_g = results['lambda_min']
    dos = 0.0
    for sd in sector_data:
        dim_pq = sd['dim_rho']
        evals_pos = sd['abs_evals'][sd['abs_evals'] > 1e-14]
        in_window = np.sum(np.abs(evals_pos - lmin_g) < DELTA_E_DOS)
        dos += dim_pq * in_window
    results['dos'] = dos

    return results


# =============================================================================
# MODULE 3: Level Statistics (Step 5)
# =============================================================================

def level_statistics(sector_data, label=""):
    """
    Compute nearest-neighbor level spacing distribution P(s).
    Tests for Poisson (integrable) vs GUE/GOE (chaotic) statistics.

    For the FULL spectrum (all sectors combined), computes:
    - Mean level spacing <s>
    - P(s) histogram
    - Brody parameter beta (0 = Poisson, 1 = GOE)
    - Level number variance Sigma^2(L)
    """
    # Collect all eigenvalues with PW multiplicity
    all_evals = []
    for sd in sector_data:
        dim_pq = sd['dim_rho']
        # Use absolute values, positive only
        abs_ev = sd['abs_evals']
        pos = abs_ev[abs_ev > 1e-14]
        for ev in pos:
            all_evals.extend([ev] * dim_pq)  # repeat for PW multiplicity

    all_evals = np.sort(np.array(all_evals))
    n = len(all_evals)
    log(f"\n  Level statistics ({label}):")
    log(f"    Total eigenvalues (with PW mult): {n}")

    if n < 10:
        log(f"    Too few eigenvalues for statistics")
        return {'n_evals': n, 'brody_beta': None}

    # Unfolding: map to uniform density
    # Use local average spacing
    spacings = np.diff(all_evals)
    spacings = spacings[spacings > 1e-14]  # remove exact degeneracies

    if len(spacings) < 5:
        log(f"    Too few distinct spacings")
        return {'n_evals': n, 'brody_beta': None}

    mean_s = np.mean(spacings)
    normalized_s = spacings / mean_s

    # Brody distribution fit: P(s) = (beta+1)*a*s^beta * exp(-a*s^{beta+1})
    # For beta=0: Poisson P(s) = exp(-s)
    # For beta=1: GOE P(s) = (pi/2)*s*exp(-pi*s^2/4)
    from scipy.special import gamma as gamma_fn
    from scipy.optimize import minimize_scalar

    def neg_log_likelihood(beta):
        if beta < -0.5 or beta > 2.0:
            return 1e10
        bp1 = beta + 1
        a = (gamma_fn((beta + 2) / bp1))**bp1 if bp1 > 0 else 1.0
        # log P(s) = log(bp1) + log(a) + beta*log(s) - a*s^bp1
        s = normalized_s
        s = s[s > 1e-14]
        if len(s) == 0:
            return 1e10
        logP = np.log(bp1) + np.log(a) + beta * np.log(s) - a * s**bp1
        return -np.sum(logP)

    res = minimize_scalar(neg_log_likelihood, bounds=(-0.3, 1.5), method='bounded')
    brody_beta = res.x

    # Classify
    if brody_beta < 0.2:
        stat_class = "POISSON (integrable)"
    elif brody_beta > 0.7:
        stat_class = "GOE/GUE (chaotic)"
    else:
        stat_class = "INTERMEDIATE"

    log(f"    Mean spacing: {mean_s:.6f}")
    log(f"    Distinct spacings: {len(spacings)}")
    log(f"    Brody beta: {brody_beta:.4f} ({stat_class})")

    # Also compute within each large sector separately
    for sd in sector_data:
        if sd['dim_rho'] >= 10:
            abs_ev = sd['abs_evals']
            pos = abs_ev[abs_ev > 1e-14]
            if len(pos) > 10:
                sp = np.diff(np.sort(pos))
                sp = sp[sp > 1e-14]
                if len(sp) > 3:
                    ms = np.mean(sp)
                    log(f"    Sector ({sd['p']},{sd['q']}): {len(pos)} levels, "
                        f"mean spacing={ms:.6f}")

    return {
        'n_evals': n,
        'brody_beta': brody_beta,
        'stat_class': stat_class,
        'mean_spacing': mean_s,
        'spacings': normalized_s,
    }


# =============================================================================
# MODULE 4: AZ Symmetry Class (Step 5)
# =============================================================================

def check_az_class(sector_data, infra, gammas):
    """
    Check Altland-Zirnbauer symmetry class at the candidate point.

    For Jensen (eps=0): class BDI with T^2 = +1.
    Off-Jensen (eps != 0): check if T and C symmetries survive.

    Time reversal T: T D T^{-1} = -D (or +D depending on convention)
    Charge conjugation C: C D C^{-1} = -D
    Chiral symmetry: {D, gamma_F} = 0

    We check D in the singlet sector (0,0) where D = Omega.
    """
    log(f"\n  AZ Symmetry Class:")

    # Singlet D = Omega (always available from infra)
    D = infra['Omega']
    dim = D.shape[0]

    # Check anti-Hermiticity
    ah_err = np.max(np.abs(D + D.conj().T))
    log(f"    D anti-Hermitian: {ah_err:.2e}")

    # Build chirality operator gamma_F = prod of all gamma_a
    # For 8D Clifford, gamma_9 = gamma_0 ... gamma_7
    gamma_F = np.eye(16, dtype=complex)
    for g in gammas:
        gamma_F = gamma_F @ g

    # Check chiral grading: {D, gamma_F} = 0
    anticomm = D @ gamma_F + gamma_F @ D
    chiral_err = np.max(np.abs(anticomm))
    log(f"    Chiral grading {{D, gamma_F}}: {chiral_err:.2e}")

    # Time reversal: T = complex conjugation * U_T
    # For real Clifford representation, T = K (complex conjugation)
    # Check if D is real
    real_err = np.max(np.abs(np.imag(D)))
    # D is anti-Hermitian with purely imaginary entries typically
    # Check D^* = D or D^* = -D
    D_conj = D.conj()
    T_plus = np.max(np.abs(D_conj - D))  # D^* = D => T^2 = +1
    T_minus = np.max(np.abs(D_conj + D))  # D^* = -D => T^2 = -1

    if T_minus < 1e-10:
        log(f"    D^* = -D: YES ({T_minus:.2e}) => T^2 = +1 (BDI)")
        t_sq = +1
    elif T_plus < 1e-10:
        log(f"    D^* = +D: YES ({T_plus:.2e}) => T^2 = -1 (CII)")
        t_sq = -1
    else:
        log(f"    D^* != +-D: T_plus={T_plus:.2e}, T_minus={T_minus:.2e}")
        # More general T: need to search for unitary U_T with U_T D^* U_T^dag = -D
        # For now, just report the errors
        t_sq = 0

    # Particle-hole C: check D = -D^T (up to unitary)
    D_T = D.T
    C_plus = np.max(np.abs(D_T + D))
    C_minus = np.max(np.abs(D_T - D))

    if C_plus < 1e-10:
        log(f"    D^T = -D (antisymmetric): YES ({C_plus:.2e}) => C^2 = +1")
        c_sq = +1
    elif C_minus < 1e-10:
        log(f"    D^T = +D (symmetric): YES ({C_minus:.2e}) => C^2 = -1")
        c_sq = -1
    else:
        log(f"    D not (anti)symmetric: C_plus={C_plus:.2e}, C_minus={C_minus:.2e}")
        c_sq = 0

    # Classify
    if t_sq == +1 and c_sq == +1 and chiral_err < 1e-10:
        az_class = "BDI"
    elif t_sq == -1 and c_sq == -1 and chiral_err < 1e-10:
        az_class = "CII"
    elif t_sq == +1 and chiral_err < 1e-10:
        az_class = "BDI (T^2=+1, chiral)"
    elif chiral_err < 1e-10:
        az_class = f"CHIRAL (T^2={t_sq}, C^2={c_sq})"
    else:
        az_class = f"UNKNOWN (T^2={t_sq}, C^2={c_sq}, chiral_err={chiral_err:.2e})"

    log(f"    AZ class: {az_class}")

    return {
        'az_class': az_class,
        't_sq': t_sq, 'c_sq': c_sq,
        'chiral_err': chiral_err,
        'ah_err': ah_err,
    }


# =============================================================================
# MODULE 5: Avoided Crossing Census (Step 5)
# =============================================================================

def avoided_crossing_census(sector_data, label=""):
    """
    Count avoided crossings: pairs of consecutive eigenvalues in the same sector
    with spacing < threshold * mean_spacing.
    """
    log(f"\n  Avoided crossing census ({label}):")

    total_avoided = 0
    total_exact = 0

    for sd in sector_data:
        abs_ev = np.sort(sd['abs_evals'])
        pos = abs_ev[abs_ev > 1e-14]
        if len(pos) < 2:
            continue

        spacings = np.diff(pos)
        mean_s = np.mean(spacings) if len(spacings) > 0 else 1.0

        # Exact degeneracies (spacing < 1e-10)
        exact = np.sum(spacings < 1e-10)
        # Near-degeneracies (spacing < 0.01 * mean)
        near = np.sum((spacings >= 1e-10) & (spacings < 0.01 * mean_s))

        total_exact += exact
        total_avoided += near

        if exact > 0 or near > 0:
            log(f"    ({sd['p']},{sd['q']}): {exact} exact, {near} near-degenerate "
                f"(threshold = {0.01*mean_s:.6f})")

    log(f"    Total: {total_exact} exact degeneracies, {total_avoided} avoided crossings")
    return {'n_exact': total_exact, 'n_avoided': total_avoided}


# =============================================================================
# MODULE 6: Sector Composition Near Gap Edge (Step 5)
# =============================================================================

def gap_edge_composition(sector_data, lambda_min_global, delta=0.05, label=""):
    """
    Which sectors contribute eigenvalues near the spectral gap edge?
    """
    log(f"\n  Sector composition near gap edge ({label}):")
    log(f"    lambda_min = {lambda_min_global:.6f}, window = +/- {delta}")

    compositions = []
    total_near = 0
    for sd in sector_data:
        abs_ev = sd['abs_evals']
        pos = abs_ev[abs_ev > 1e-14]
        in_window = np.sum(np.abs(pos - lambda_min_global) < delta)
        if in_window > 0:
            dim_pq = sd['dim_rho']
            pw_mult = dim_pq**2 if (sd['p'], sd['q']) != (0, 0) else 1
            weighted = pw_mult * in_window
            total_near += weighted
            compositions.append({
                'sector': (sd['p'], sd['q']),
                'n_in_window': int(in_window),
                'pw_mult': pw_mult,
                'weighted': weighted,
            })
            log(f"    ({sd['p']},{sd['q']}): {in_window} levels, "
                f"PW mult={pw_mult}, weighted={weighted}")

    log(f"    Total weighted count near gap: {total_near}")
    return compositions


# =============================================================================
# MODULE 7: Order-One Condition (Step 5b)
# =============================================================================

def order_one_condition(infra, gammas, gens, f_abc, L1, L2, L3, label=""):
    """
    Compute ||[[D_K, a], b^o]|| for factor pairs in the singlet sector.

    The order-one condition requires [[D, a], b^o] = 0 for all a in A_F, b in A_F.
    We test this for the Dirac operator on SU(3) with:
      a, b in {C, H} (complex numbers, quaternions)

    In the singlet sector, D = Omega (16x16).
    We use basis matrices for C (diagonal) and H (Pauli blocks).

    Jensen reference values (from previous sessions):
      (H,H) = 4.000, (C,H) = 2.828, (C,C) = 2.000
    """
    log(f"\n  Order-one condition ({label}):")

    Omega = infra['Omega']

    # Build simple test matrices for a and b^o
    # a acts on the LEFT of the tensor product (algebra side)
    # b^o acts on the RIGHT (opposite algebra)
    # In the singlet (0,0), the space is just C^16 (spinor space)

    # For simplicity, use gamma matrices as proxies for algebra elements
    # This is the standard approach: a = gamma_a, b^o = gamma_b^T (right action)
    dim = 16

    # Compute [[D, gamma_a], gamma_b^T] for a few choices
    results_oo = {}
    test_pairs = [
        ('gamma_0', 'gamma_0', gammas[0], gammas[0].T),
        ('gamma_0', 'gamma_1', gammas[0], gammas[1].T),
        ('gamma_3', 'gamma_3', gammas[3], gammas[3].T),
        ('gamma_3', 'gamma_7', gammas[3], gammas[7].T),
    ]

    for name_a, name_b, a, bo in test_pairs:
        # [[D, a], b^o] = [D, a] b^o - b^o [D, a]
        Da = Omega @ a - a @ Omega  # [D, a]
        result = Da @ bo - bo @ Da  # [[D, a], b^o]
        norm_val = np.max(np.abs(result))
        frob_val = np.sqrt(np.sum(np.abs(result)**2))
        log(f"    [[D, {name_a}], {name_b}^o]: max={norm_val:.6f}, Frobenius={frob_val:.6f}")
        results_oo[(name_a, name_b)] = {'max': norm_val, 'frob': frob_val}

    # Also compute the operator norm of [D, gamma_a] for each a
    log(f"    ||[D, gamma_a]|| (operator norms):")
    for a_idx in range(8):
        Da = Omega @ gammas[a_idx] - gammas[a_idx] @ Omega
        op_norm = np.max(np.abs(np.linalg.eigvals(Da)))
        log(f"      a={a_idx}: {op_norm:.6f}")

    return results_oo


# =============================================================================
# MODULE 8: PMNS Extraction (adapted from s29b_pmns_extraction.py)
# =============================================================================

def extract_pmns_angles(U):
    """Extract PMNS mixing angles from 3x3 unitary matrix."""
    sin2_13 = abs(U[0, 2])**2
    theta_13 = np.degrees(np.arcsin(np.sqrt(sin2_13)))

    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1])**2 / abs(U[0, 0])**2
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))
    else:
        theta_12 = 90.0

    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2])**2 / abs(U[2, 2])**2
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))
    else:
        theta_23 = 90.0

    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))

    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'J': J,
    }


def compute_pmns_at_point(B_ab, gens, f_abc, gammas, L1, L2, L3, label=""):
    """
    Compute PMNS mixing angles via the Kosmann kernel in the singlet sector.

    Builds the 16x16 H_eff = diag(eigenvalues) + V_pairing in the (0,0) sector,
    extracts the 3 lightest positive mass states and their mixing.
    """
    log(f"\n  PMNS extraction ({label}):")

    g = u2_invariant_metric(B_ab, L1, L2, L3)
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Diagonalize singlet D = Omega
    H = 1j * Omega
    evals, evecs = scipy_eigh(H)

    log(f"    Singlet eigenvalues: {evals}")

    # Build Kosmann pairing matrix V in the singlet sector
    # K_a = -(1/8) sum_{r,s} [Gamma[s,r,a] - Gamma[r,s,a]] gamma_r gamma_s
    dim_spin = 16
    V_total = np.zeros((dim_spin, dim_spin), dtype=complex)

    for a in range(8):
        K_a, _ = kosmann_operator_antisymmetric(Gamma, gammas, a)
        # V_pairing from K_a: transform to eigenbasis
        K_in_basis = evecs.conj().T @ K_a @ evecs
        V_total += K_in_basis

    # H_eff = diag(evals) + V_total
    H_eff = np.diag(evals) + V_total

    # Make Hermitian (should be already)
    H_eff = 0.5 * (H_eff + H_eff.conj().T)

    # Diagonalize
    H_evals, H_evecs = scipy_eigh(H_eff)

    # Extract 3 smallest positive eigenvalues
    pos_mask = H_evals > 0
    pos_evals = H_evals[pos_mask]
    pos_evecs = H_evecs[:, pos_mask]

    if len(pos_evals) < 3:
        log(f"    FAIL: only {len(pos_evals)} positive eigenvalues")
        return None

    sort_idx = np.argsort(pos_evals)
    m = pos_evals[sort_idx[:3]]
    U_3 = pos_evecs[:, sort_idx[:3]]

    # Mass ratio R
    denom = m[1]**2 - m[0]**2
    R = (m[2]**2 - m[1]**2) / denom if abs(denom) > 1e-30 else float('inf')

    log(f"    3 lightest masses: {m[0]:.8f}, {m[1]:.8f}, {m[2]:.8f}")
    log(f"    R = dm32^2/dm21^2 = {R:.4f}  (PDG: 32.6)")

    # For PMNS, we need 3x3 overlap with the level subspaces
    # Identify level groupings from original eigenvalues
    # The singlet has 8 positive eigenvalues grouped as:
    #   L1 (singlet), L2 (quadruplet), L3 (triplet) at nonzero tau

    # Group positive eigenvalues
    pos_orig = evals[evals > 0]
    pos_orig_idx = np.where(evals > 0)[0]

    # Cluster by proximity
    sorted_pos = np.sort(pos_orig)
    groups = []
    current_group = [sorted_pos[0]]
    for val in sorted_pos[1:]:
        if abs(val - current_group[-1]) < 0.01 * abs(current_group[-1]):
            current_group.append(val)
        else:
            groups.append(current_group)
            current_group = [val]
    groups.append(current_group)

    log(f"    Level groups: {[len(g) for g in groups]}")
    for i, g in enumerate(groups):
        log(f"      L{i+1}: mult={len(g)}, E={np.mean(g):.6f}")

    if len(groups) >= 3:
        # Build 3x3 from degenerate perturbation theory (Method B from s29b)
        E1 = np.mean(groups[0])
        E2 = np.mean(groups[1])
        E3 = np.mean(groups[2])

        # Get indices for each group
        idx1 = pos_orig_idx[np.argsort(pos_orig)][:len(groups[0])]
        idx2 = pos_orig_idx[np.argsort(pos_orig)][len(groups[0]):len(groups[0])+len(groups[1])]
        idx3 = pos_orig_idx[np.argsort(pos_orig)][len(groups[0])+len(groups[1]):len(groups[0])+len(groups[1])+len(groups[2])]

        # Coupling L1->L2
        v12 = np.array([V_total[idx1[0], j] for j in idx2])
        norm_12 = np.linalg.norm(v12)

        # Effective L2 state
        if norm_12 > 1e-15 and len(idx2) > 0:
            L2_eff = v12 / norm_12
        else:
            L2_eff = np.ones(len(idx2)) / np.sqrt(len(idx2))

        # Coupling L2_eff -> L3
        V_23_block = np.array([[V_total[i, j] for j in idx3] for i in idx2])
        v_eff_23 = L2_eff @ V_23_block
        norm_23 = np.linalg.norm(v_eff_23)

        # 3x3 tridiagonal H
        H_3x3 = np.array([
            [E1,      norm_12, 0.0    ],
            [norm_12, E2,      norm_23],
            [0.0,     norm_23, E3     ]
        ])

        m3_evals, U3 = np.linalg.eigh(H_3x3)
        pmns = extract_pmns_angles(U3)

        log(f"    3x3 H_eff eigenvalues: {m3_evals}")
        log(f"    V_12 = {norm_12:.6f}, V_23 = {norm_23:.6f}")
        log(f"    sin^2(theta_13) = {pmns['sin2_13']:.6f}  (PDG: 0.0220)")
        log(f"    theta_13 = {pmns['theta_13']:.2f} deg  (PDG: 8.54)")
        log(f"    theta_12 = {pmns['theta_12']:.2f} deg  (PDG: 33.4)")
        log(f"    theta_23 = {pmns['theta_23']:.2f} deg  (PDG: 49.1)")

        return {
            'masses': m,
            'R': R,
            'H_3x3': H_3x3,
            'm3_evals': m3_evals,
            'pmns': pmns,
            'V_12': norm_12,
            'V_23': norm_23,
            'H_evals': H_evals,
        }
    else:
        log(f"    Cannot identify 3 distinct level groups")
        return {
            'masses': m,
            'R': R,
            'H_evals': H_evals,
            'n_groups': len(groups),
        }


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()

    log("=" * 78)
    log("SESSION 30Bb: FULL DIRAC SPECTRUM AT CANDIDATE POINTS")
    log("=" * 78)
    log(f"Date: 2026-03-01")
    log(f"N_max (max p+q): {MAX_PQ_SUM}")
    log(f"Spectral cutoff rho: {RHO_SPEC}")

    # Setup algebra
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    log(f"\nKilling form diag: {np.diag(B_ab)}")

    # Storage for all results
    all_results = {}

    # =========================================================================
    # STEP 3 + STEP 5: Full spectrum at each candidate
    # =========================================================================

    for cand_key, cand in CANDIDATES.items():
        tau, eps = cand['tau'], cand['eps']
        L1, L2, L3 = tau_eps_to_lambdas(tau, eps)
        label = cand['label']

        log(f"\n{'=' * 78}")
        log(f"CANDIDATE: {label}")
        log(f"  tau={tau:.3f}, eps={eps:.3f}")
        log(f"  L1={L1:.6f}, L2={L2:.6f}, L3={L3:.6f}")
        log(f"  Volume: {L1 * L2**3 * L3**4:.10f}")
        log(f"  sin2_B = {3*L2/(L1+3*L2):.6f}")
        log(f"{'=' * 78}")

        # --- Full Dirac spectrum (N_max=6) ---
        # Only compute eigenvectors for singlet (AZ check) — full eigvecs too slow at N_max=6
        log(f"\n  Computing Dirac spectrum (N_max={MAX_PQ_SUM})...")
        t0 = time.time()
        sector_data, infra = compute_full_dirac(
            B_ab, gens, f_abc, gammas, L1, L2, L3,
            max_pq=MAX_PQ_SUM, compute_eigenvectors=False
        )
        dt_spec = time.time() - t0
        log(f"  Spectrum computed in {dt_spec:.1f}s ({len(sector_data)} sectors)")

        # --- Observables ---
        obs = extract_observables(sector_data, L1, L2, L3)
        log(f"\n  OBSERVABLES:")
        log(f"    lambda_min = {obs['lambda_min']:.8f}")
        log(f"    phi_30 (m_(3,0)/m_(0,0)) = {obs['phi_30']:.8f}")
        log(f"    phi_03 (m_(0,3)/m_(0,0)) = {obs['phi_03']:.8f}")
        log(f"    sin2_B = {obs['sin2_B']:.6f}")
        log(f"    g1/g2 = {obs['g1g2']:.6f}")
        log(f"    V_spec = {obs['V_spec']:.4f}")
        log(f"    F_BCS (mu=1.0*lmin) = {obs['F_BCS_1.0']:.6f}")
        log(f"    F_BCS (mu=1.2*lmin) = {obs['F_BCS_1.2']:.6f}")
        log(f"    DOS = {obs['dos']:.0f}")

        # --- Gate: P-30phi ---
        phi = obs['phi_30']
        if 1.52 <= phi <= 1.54:
            gate_phi = "P-30phi PASS"
        elif 1.610 <= phi <= 1.626:
            gate_phi = "P-30golden PASS"
        else:
            gate_phi = f"P-30phi FAIL (phi={phi:.6f})"
        log(f"\n  GATE P-30phi: {gate_phi}")

        # --- Step 5: Level statistics ---
        lstats = level_statistics(sector_data, label)

        # --- Step 5: Avoided crossings ---
        acrossings = avoided_crossing_census(sector_data, label)

        # --- Step 5: Gap edge composition ---
        gcomp = gap_edge_composition(sector_data, obs['lambda_min'], label=label)

        # --- Step 5: AZ class ---
        az = check_az_class(sector_data, infra, gammas)
        if az['az_class'] == 'BDI':
            gate_az = "AZ-1 PASS"
        else:
            gate_az = f"AZ-1 FAIL ({az['az_class']})"
        log(f"  GATE AZ-1: {gate_az}")

        # --- Step 5b: Order-one condition ---
        oo = order_one_condition(infra, gammas, gens, f_abc, L1, L2, L3, label)

        # --- Step 3: PMNS ---
        pmns_result = compute_pmns_at_point(B_ab, gens, f_abc, gammas, L1, L2, L3, label)

        # Gate P-30pmns
        if pmns_result and 'pmns' in pmns_result:
            pmns = pmns_result['pmns']
            sin2_13 = pmns['sin2_13']
            theta_23 = pmns['theta_23']
            if 0.015 <= sin2_13 <= 0.030 and 40 <= theta_23 <= 55:
                gate_pmns = "P-30pmns PASS"
            else:
                gate_pmns = f"P-30pmns FAIL (sin2_13={sin2_13:.4f}, theta_23={theta_23:.1f})"
        else:
            gate_pmns = "P-30pmns INCONCLUSIVE (no 3x3 extraction)"
        log(f"  GATE P-30pmns: {gate_pmns}")

        # Store results
        all_results[cand_key] = {
            'tau': tau, 'eps': eps,
            'L1': L1, 'L2': L2, 'L3': L3,
            'observables': obs,
            'level_stats': lstats,
            'avoided_crossings': acrossings,
            'gap_composition': gcomp,
            'az': az,
            'order_one': oo,
            'pmns': pmns_result,
            'gate_phi': gate_phi,
            'gate_az': gate_az,
            'gate_pmns': gate_pmns,
            'sector_count': len(sector_data),
            'compute_time': dt_spec,
        }

    # =========================================================================
    # REFERENCE: Jensen point DOS for DOS-1 gate
    # =========================================================================
    log(f"\n{'=' * 78}")
    log(f"JENSEN REFERENCE POINT (for DOS-1 comparison)")
    log(f"{'=' * 78}")

    tau_j, eps_j = JENSEN_REF['tau'], JENSEN_REF['eps']
    L1_j, L2_j, L3_j = tau_eps_to_lambdas(tau_j, eps_j)
    log(f"  tau={tau_j}, eps={eps_j}")
    log(f"  L1={L1_j:.6f}, L2={L2_j:.6f}, L3={L3_j:.6f}")

    # Compute at N_max=6 for fair comparison
    sector_data_j, infra_j = compute_full_dirac(
        B_ab, gens, f_abc, gammas, L1_j, L2_j, L3_j,
        max_pq=MAX_PQ_SUM, compute_eigenvectors=False
    )
    obs_j = extract_observables(sector_data_j, L1_j, L2_j, L3_j)
    log(f"  Jensen DOS = {obs_j['dos']:.0f}")
    log(f"  Jensen lambda_min = {obs_j['lambda_min']:.8f}")
    log(f"  Jensen phi_30 = {obs_j['phi_30']:.8f}")

    all_results['jensen_ref'] = {
        'tau': tau_j, 'eps': eps_j,
        'observables': obs_j,
    }

    # DOS-1 gate
    for cand_key, cand in CANDIDATES.items():
        cand_dos = all_results[cand_key]['observables']['dos']
        jensen_dos = obs_j['dos']
        if cand_dos > jensen_dos:
            gate_dos = f"DOS-1 PASS ({cand_dos:.0f} > {jensen_dos:.0f})"
        else:
            gate_dos = f"DOS-1 FAIL ({cand_dos:.0f} <= {jensen_dos:.0f})"
        log(f"\n  DOS-1 at {cand['label']}: {gate_dos}")
        all_results[cand_key]['gate_dos'] = gate_dos

    # =========================================================================
    # SUMMARY
    # =========================================================================
    dt_total = time.time() - t_start

    log(f"\n{'=' * 78}")
    log(f"GATE VERDICTS SUMMARY")
    log(f"{'=' * 78}")
    for cand_key in CANDIDATES:
        r = all_results[cand_key]
        log(f"\n  {CANDIDATES[cand_key]['label']}:")
        log(f"    P-30phi:  {r['gate_phi']}")
        log(f"    AZ-1:     {r['gate_az']}")
        log(f"    P-30pmns: {r['gate_pmns']}")
        log(f"    DOS-1:    {r['gate_dos']}")

    log(f"\n  Total computation time: {dt_total:.1f}s")

    # =========================================================================
    # SAVE
    # =========================================================================
    save_dict = {}
    for cand_key in list(CANDIDATES.keys()) + ['jensen_ref']:
        r = all_results[cand_key]
        prefix = cand_key
        save_dict[f'{prefix}_tau'] = r['tau']
        save_dict[f'{prefix}_eps'] = r['eps']
        obs = r['observables']
        for k, v in obs.items():
            if isinstance(v, (int, float, np.floating, np.integer)):
                save_dict[f'{prefix}_{k}'] = v
            elif isinstance(v, dict):
                # Flatten dicts
                for k2, v2 in v.items():
                    save_dict[f'{prefix}_{k}_{k2}'] = v2

    np.savez(OUT_NPZ, **save_dict)
    log(f"\n  Saved to {OUT_NPZ}")

    # Save text log
    with open(OUT_TXT, 'w') as f:
        f.write('\n'.join(log_lines))
    log(f"  Saved text log to {OUT_TXT}")


if __name__ == '__main__':
    main()
