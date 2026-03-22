#!/usr/bin/env python3
"""
s30b_grid_bcs.py — BCS Free Energy on U(2)-invariant 2D Grid
=============================================================

Session 30Ba Step 2: Compute the full Dirac spectrum at each (tau, eps)
grid point, evaluate V_total = V_spec + F_BCS, locate the minimum,
verify Hessian stability, and extract physical observables.

At each grid point:
  1. Dirac eigenvalues for all 10 sectors (p+q <= 3)
  2. lambda_min (global smallest positive eigenvalue)
  3. V_spec from heat kernel: sum_n mult * exp(-lambda_n^2 / Lambda^2)
  4. F_BCS^{3-sector} at mu = lambda_min and mu = 1.2*lambda_min
  5. BCS gap Delta/lambda_min per load-bearing sector
  6. DOS N(E_F): eigenvalues within delta_E of lambda_min
  7. sin^2(theta_W) and phi_paasch from eigenvalue ratios

After grid computation:
  - Locate minimum of V_total at mu/lambda_min = 1.20
  - 2x2 Hessian at minimum (both eigenvalues must be positive)
  - 5D stability check: perturb in T3, T4 directions at the 2D minimum

Uses the same (tau, eps) parameterization as s30b_sdw_grid.py:
  log L1 = 2*tau - 11*eps/N, log L2 = -2*tau - 7*eps/N, log L3 = tau + 8*eps/N

Author: phonon-exflation-sim agent, Session 30Ba
Date: 2026-02-28
"""

import numpy as np
from numpy.linalg import eigvalsh
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    u2_invariant_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    get_irrep, dirac_operator_on_irrep, _irrep_cache
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(SCRIPT_DIR)
OUT_NPZ = DATA_DIR / 's30b_grid_bcs.npz'
OUT_STAB = DATA_DIR / 's30b_5d_stability.npz'
OUT_LANDSCAPE = DATA_DIR / 's30b_landscape.png'
OUT_WEINBERG = DATA_DIR / 's30b_weinberg_contour.png'
OUT_PHI = DATA_DIR / 's30b_phi_contour.png'
OUT_FBCS = DATA_DIR / 's30b_fbcs_landscape.png'
OUT_DOS = DATA_DIR / 's30b_dos_landscape.png'

# Grid — same as SDW grid
N_TAU = 21
N_EPS = 21
TAU_MIN, TAU_MAX = 0.0, 0.60
EPS_MIN, EPS_MAX = -0.15, 0.15

# T2 normalization
T2_DIR = np.array([-11.0, -7.0, 8.0])
N_T2 = np.sqrt(np.dot(T2_DIR, T2_DIR))  # sqrt(234)

# Physics parameters
MAX_PQ_SUM = 3
RHO_SPEC = 0.01  # spectral cutoff for V_spec
MU_RATIOS = [1.0, 1.20]  # chemical potential ratios to evaluate
DELTA_E_DOS = 0.05  # energy window for DOS computation

# Load-bearing sectors
LOAD_BEARING = [(0, 0), (3, 0), (0, 3)]
PW_MULT = {(0, 0): 1, (3, 0): 100, (0, 3): 100}

# Phi_paasch reference
PHI = (1 + np.sqrt(5)) / 2  # 1.6180339...


# =============================================================================
# MODULE 1: Parameterization (same as SDW grid)
# =============================================================================

def tau_eps_to_lambdas(tau, eps):
    """Convert (tau, eps) to (L1, L2, L3) on volume-preserving surface."""
    L1 = np.exp(2.0 * tau - 11.0 * eps / N_T2)
    L2 = np.exp(-2.0 * tau - 7.0 * eps / N_T2)
    L3 = np.exp(tau + 8.0 * eps / N_T2)
    return L1, L2, L3


# =============================================================================
# MODULE 2: Dirac spectrum computation at a single grid point
# =============================================================================

def compute_dirac_at_point(B_ab, gens, f_abc, gammas, L1, L2, L3):
    """
    Compute full Dirac spectrum for all sectors p+q <= MAX_PQ_SUM
    at a U(2)-invariant metric with scale factors (L1, L2, L3).

    Returns
    -------
    sector_evals : dict
        Maps (p,q) -> sorted array of |eigenvalue| (absolute values).
    all_evals_flat : list of (|eigenvalue|, pw_multiplicity)
    lambda_min_global : float
        Smallest positive eigenvalue across all sectors.
    lambda_min_per_sector : dict
        (p,q) -> min|eigenvalue| for that sector.
    """
    g = u2_invariant_metric(B_ab, L1, L2, L3)
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    sector_evals = {}
    lambda_min_per_sector = {}
    all_evals_flat = []

    # Trivial irrep (0,0)
    evals_00 = np.linalg.eigvals(Omega)
    abs_00 = np.sort(np.abs(evals_00))
    nonzero = abs_00[abs_00 > 1e-14]
    lmin_00 = nonzero[0] if len(nonzero) > 0 else np.inf
    sector_evals[(0, 0)] = abs_00
    lambda_min_per_sector[(0, 0)] = lmin_00
    for ev in abs_00:
        all_evals_flat.append((ev, 1))

    # Non-trivial irreps
    _irrep_cache.clear()
    for p in range(MAX_PQ_SUM + 1):
        for q in range(MAX_PQ_SUM + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            try:
                rho, _ = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_pi = np.linalg.eigvals(D_pi)
                abs_pi = np.sort(np.abs(evals_pi))
                nonzero = abs_pi[abs_pi > 1e-14]
                lmin = nonzero[0] if len(nonzero) > 0 else np.inf
                sector_evals[(p, q)] = abs_pi
                lambda_min_per_sector[(p, q)] = lmin
                for ev in abs_pi:
                    all_evals_flat.append((ev, dim_pq))
            except Exception:
                continue

    # Global lambda_min
    all_lmin = [v for v in lambda_min_per_sector.values() if np.isfinite(v)]
    lambda_min_global = min(all_lmin) if all_lmin else np.inf

    return sector_evals, all_evals_flat, lambda_min_global, lambda_min_per_sector


# =============================================================================
# MODULE 3: V_spec and F_BCS computation
# =============================================================================

def compute_v_spec(all_evals_flat, rho_spec=RHO_SPEC):
    """
    Spectral action from heat kernel: V_spec = sum_n mult * exp(-lambda_n^2/Lambda^2).
    Lambda = 1/rho_spec.
    """
    Lambda_sq = 1.0 / rho_spec**2
    V_spec = 0.0
    for ev, mult in all_evals_flat:
        V_spec += mult * np.exp(-ev**2 / Lambda_sq)
    return V_spec


def compute_fbcs_3sector(sector_evals, lambda_min_global, mu_ratio):
    """
    3-sector BCS free energy: F_BCS = sum_{r in load-bearing} PW_mult(r) * F_cond(r).

    F_cond per sector = -sum_m |xi_m| for modes with xi_m = |lambda_m| - mu < 0
    (strong-coupling BCS condensation energy estimate).

    Parameters
    ----------
    sector_evals : dict
        (p,q) -> sorted |eigenvalues|.
    lambda_min_global : float
        Smallest positive eigenvalue across all sectors.
    mu_ratio : float
        mu = mu_ratio * lambda_min_global.

    Returns
    -------
    F_BCS : float
        Total 3-sector BCS free energy.
    F_per_sector : dict
        (p,q) -> F_cond for each load-bearing sector.
    n_supercrit : dict
        (p,q) -> number of supercritical modes.
    """
    mu = mu_ratio * lambda_min_global
    F_BCS = 0.0
    F_per_sector = {}
    n_supercrit = {}

    for pq in LOAD_BEARING:
        if pq not in sector_evals:
            F_per_sector[pq] = 0.0
            n_supercrit[pq] = 0
            continue

        evals = sector_evals[pq]
        evals_pos = evals[evals > 1e-14]

        xi = evals_pos - mu
        super_mask = xi < 0
        n_super = int(np.sum(super_mask))

        if n_super > 0:
            F_cond = -np.sum(np.abs(xi[super_mask]))
        else:
            F_cond = 0.0

        F_per_sector[pq] = F_cond
        n_supercrit[pq] = n_super
        F_BCS += PW_MULT[pq] * F_cond

    return F_BCS, F_per_sector, n_supercrit


def compute_dos(sector_evals, lambda_min_global, delta_E=DELTA_E_DOS):
    """
    Density of states N(E_F): count eigenvalues within delta_E of lambda_min.
    Weighted by Peter-Weyl multiplicity.
    """
    total_dos = 0.0
    for (p, q), evals in sector_evals.items():
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        evals_pos = evals[evals > 1e-14]
        in_window = np.sum(np.abs(evals_pos - lambda_min_global) < delta_E)
        total_dos += dim_pq * in_window
    return total_dos


def compute_phi_paasch(sector_evals):
    """
    Compute phi_paasch = lambda_min(3,0) / lambda_min(0,0).
    Also compute lambda_min(0,3)/lambda_min(0,0) for comparison.
    """
    lmin_00 = sector_evals.get((0, 0), np.array([np.inf]))
    lmin_00 = lmin_00[lmin_00 > 1e-14]
    lmin_00 = lmin_00[0] if len(lmin_00) > 0 else np.inf

    lmin_30 = sector_evals.get((3, 0), np.array([np.inf]))
    lmin_30 = lmin_30[lmin_30 > 1e-14]
    lmin_30 = lmin_30[0] if len(lmin_30) > 0 else np.inf

    lmin_03 = sector_evals.get((0, 3), np.array([np.inf]))
    lmin_03 = lmin_03[lmin_03 > 1e-14]
    lmin_03 = lmin_03[0] if len(lmin_03) > 0 else np.inf

    ratio_30 = lmin_30 / lmin_00 if lmin_00 > 0 else np.inf
    ratio_03 = lmin_03 / lmin_00 if lmin_00 > 0 else np.inf

    return ratio_30, ratio_03, lmin_00, lmin_30, lmin_03


# =============================================================================
# MODULE 4: Full grid computation
# =============================================================================

def compute_bcs_grid(B_ab, gens, f_abc, gammas):
    """
    Compute V_spec, F_BCS, V_total, and observables on the full 21x21 grid.
    """
    tau_arr = np.linspace(TAU_MIN, TAU_MAX, N_TAU)
    eps_arr = np.linspace(EPS_MIN, EPS_MAX, N_EPS)

    # Output arrays
    V_spec_grid = np.zeros((N_TAU, N_EPS))
    F_BCS_grid = {r: np.zeros((N_TAU, N_EPS)) for r in MU_RATIOS}
    V_total_grid = {r: np.zeros((N_TAU, N_EPS)) for r in MU_RATIOS}
    lambda_min_grid = np.zeros((N_TAU, N_EPS))
    dos_grid = np.zeros((N_TAU, N_EPS))
    sin2_tw_grid = np.zeros((N_TAU, N_EPS))
    g1g2_grid = np.zeros((N_TAU, N_EPS))
    phi_30_grid = np.zeros((N_TAU, N_EPS))
    phi_03_grid = np.zeros((N_TAU, N_EPS))
    lmin_00_grid = np.zeros((N_TAU, N_EPS))
    lmin_30_grid = np.zeros((N_TAU, N_EPS))
    lmin_03_grid = np.zeros((N_TAU, N_EPS))
    n_supercrit_grid = {r: np.zeros((N_TAU, N_EPS)) for r in MU_RATIOS}

    # Per-sector F_cond for diagnostics (at mu_ratio=1.20)
    F_cond_00_grid = np.zeros((N_TAU, N_EPS))
    F_cond_30_grid = np.zeros((N_TAU, N_EPS))
    F_cond_03_grid = np.zeros((N_TAU, N_EPS))

    t_start = time.time()
    n_total = N_TAU * N_EPS
    n_done = 0

    for i, tau in enumerate(tau_arr):
        for j, eps in enumerate(eps_arr):
            L1, L2, L3 = tau_eps_to_lambdas(tau, eps)

            # Algebraic observables
            sin2_tw_grid[i, j] = L2 / (L1 + L2)
            g1g2_grid[i, j] = np.sqrt(L2 / L1)

            # Dirac spectrum
            sector_evals, all_evals_flat, lmin_global, lmin_per_sector = \
                compute_dirac_at_point(B_ab, gens, f_abc, gammas, L1, L2, L3)

            lambda_min_grid[i, j] = lmin_global

            # V_spec
            V_spec = compute_v_spec(all_evals_flat)
            V_spec_grid[i, j] = V_spec

            # F_BCS at each mu_ratio
            for mu_r in MU_RATIOS:
                F_BCS, F_per, n_sup = compute_fbcs_3sector(
                    sector_evals, lmin_global, mu_r)
                F_BCS_grid[mu_r][i, j] = F_BCS
                V_total_grid[mu_r][i, j] = V_spec + F_BCS
                n_supercrit_grid[mu_r][i, j] = sum(n_sup.values())

                if mu_r == 1.20:
                    F_cond_00_grid[i, j] = F_per.get((0, 0), 0.0)
                    F_cond_30_grid[i, j] = F_per.get((3, 0), 0.0)
                    F_cond_03_grid[i, j] = F_per.get((0, 3), 0.0)

            # DOS
            dos_grid[i, j] = compute_dos(sector_evals, lmin_global)

            # Phi_paasch
            r30, r03, l00, l30, l03 = compute_phi_paasch(sector_evals)
            phi_30_grid[i, j] = r30
            phi_03_grid[i, j] = r03
            lmin_00_grid[i, j] = l00
            lmin_30_grid[i, j] = l30
            lmin_03_grid[i, j] = l03

            n_done += 1

        elapsed = time.time() - t_start
        rate = n_done / elapsed if elapsed > 0 else 0
        remaining = (n_total - n_done) / rate if rate > 0 else 0
        print(f"  tau={tau:.2f}: {n_done}/{n_total} pts "
              f"({elapsed:.1f}s elapsed, ~{remaining:.0f}s remaining)")

    return {
        'tau': tau_arr,
        'eps': eps_arr,
        'V_spec': V_spec_grid,
        'F_BCS': F_BCS_grid,
        'V_total': V_total_grid,
        'lambda_min': lambda_min_grid,
        'dos': dos_grid,
        'sin2_tw': sin2_tw_grid,
        'g1g2': g1g2_grid,
        'phi_30': phi_30_grid,
        'phi_03': phi_03_grid,
        'lmin_00': lmin_00_grid,
        'lmin_30': lmin_30_grid,
        'lmin_03': lmin_03_grid,
        'n_supercrit': n_supercrit_grid,
        'F_cond_00': F_cond_00_grid,
        'F_cond_30': F_cond_30_grid,
        'F_cond_03': F_cond_03_grid,
    }


# =============================================================================
# MODULE 5: Minimum location + Hessian
# =============================================================================

def find_minimum_and_hessian(results, mu_ratio=1.20):
    """
    Locate the minimum of V_total on the 2D grid and compute the Hessian.

    Returns min location, Hessian eigenvalues, and physical observables at minimum.
    """
    tau_arr = results['tau']
    eps_arr = results['eps']
    V = results['V_total'][mu_ratio]

    # Find minimum
    min_idx = np.unravel_index(np.argmin(V), V.shape)
    tau_min = tau_arr[min_idx[0]]
    eps_min = eps_arr[min_idx[1]]
    V_min = V[min_idx]

    print(f"\nV_total minimum at mu/lmin = {mu_ratio}:")
    print(f"  (tau, eps) = ({tau_min:.4f}, {eps_min:.4f})")
    print(f"  V_total = {V_min:.6f}")
    print(f"  V_spec = {results['V_spec'][min_idx]:.6f}")
    print(f"  F_BCS = {results['F_BCS'][mu_ratio][min_idx]:.6f}")
    print(f"  lambda_min = {results['lambda_min'][min_idx]:.6f}")
    print(f"  sin^2(theta_W) = {results['sin2_tw'][min_idx]:.6f}")
    print(f"  g1/g2 = {results['g1g2'][min_idx]:.6f}")
    print(f"  phi_30 = {results['phi_30'][min_idx]:.6f}")
    print(f"  phi_03 = {results['phi_03'][min_idx]:.6f}")
    print(f"  DOS = {results['dos'][min_idx]:.1f}")

    # 2x2 Hessian via finite differences
    ti, ej = min_idx
    dtau = tau_arr[1] - tau_arr[0]
    deps = eps_arr[1] - eps_arr[0]

    # d2V/dtau2
    if 0 < ti < len(tau_arr) - 1:
        d2V_dtau2 = (V[ti+1, ej] + V[ti-1, ej] - 2*V[ti, ej]) / dtau**2
    else:
        d2V_dtau2 = np.nan

    # d2V/deps2
    if 0 < ej < len(eps_arr) - 1:
        d2V_deps2 = (V[ti, ej+1] + V[ti, ej-1] - 2*V[ti, ej]) / deps**2
    else:
        d2V_deps2 = np.nan

    # d2V/dtau*deps
    if 0 < ti < len(tau_arr) - 1 and 0 < ej < len(eps_arr) - 1:
        d2V_dtaudeps = (V[ti+1, ej+1] + V[ti-1, ej-1]
                        - V[ti+1, ej-1] - V[ti-1, ej+1]) / (4*dtau*deps)
    else:
        d2V_dtaudeps = np.nan

    H = np.array([[d2V_dtau2, d2V_dtaudeps],
                   [d2V_dtaudeps, d2V_deps2]])

    evals_H = eigvalsh(H)
    both_positive = bool(np.all(evals_H > 0))

    print(f"\n2x2 Hessian:")
    print(f"  H = [[{d2V_dtau2:.4f}, {d2V_dtaudeps:.4f}],")
    print(f"       [{d2V_dtaudeps:.4f}, {d2V_deps2:.4f}]]")
    print(f"  Eigenvalues: [{evals_H[0]:.4f}, {evals_H[1]:.4f}]")
    print(f"  Both positive: {both_positive}")

    return {
        'tau_min': tau_min,
        'eps_min': eps_min,
        'V_min': V_min,
        'V_spec_min': results['V_spec'][min_idx],
        'F_BCS_min': results['F_BCS'][mu_ratio][min_idx],
        'lambda_min_at_min': results['lambda_min'][min_idx],
        'sin2_tw_at_min': results['sin2_tw'][min_idx],
        'g1g2_at_min': results['g1g2'][min_idx],
        'phi_30_at_min': results['phi_30'][min_idx],
        'phi_03_at_min': results['phi_03'][min_idx],
        'dos_at_min': results['dos'][min_idx],
        'H': H,
        'evals_H': evals_H,
        'both_positive': both_positive,
        'grid_idx': min_idx,
    }


# =============================================================================
# MODULE 6: 5D stability at minimum (T3, T4 transverse directions)
# =============================================================================

def check_5d_stability(B_ab, gens, f_abc, gammas, min_info, mu_ratio=1.20):
    """
    Check stability in the T3 (su(2) anisotropy) and T4 (C^2 anisotropy)
    directions at the 2D minimum. These break U(2) symmetry.

    Uses the same approach as s29b_jensen_transverse.py but evaluated at
    the off-Jensen minimum point.
    """
    tau_min = min_info['tau_min']
    eps_min = min_info['eps_min']
    L1, L2, L3 = tau_eps_to_lambdas(tau_min, eps_min)

    print(f"\n{'=' * 70}")
    print(f"5D STABILITY CHECK at (tau={tau_min}, eps={eps_min})")
    print(f"  L1={L1:.6f}, L2={L2:.6f}, L3={L3:.6f}")
    print(f"{'=' * 70}")

    # Perturbation size
    eps_fd = 0.02

    # U(1) indices
    U1_IDX = [7]
    SU2_IDX = [0, 1, 2]
    C2_IDX = [3, 4, 5, 6]

    def build_metric_with_aniso(L1, L2, L3, eps3=0.0, eps4=0.0):
        """Build U(2)-breaking metric with T3/T4 perturbations."""
        g0 = np.abs(compute_killing_form(f_abc))
        g = np.zeros((8, 8), dtype=np.float64)

        for a in U1_IDX:
            for b in U1_IDX:
                g[a, b] = g0[a, b] * L1

        # su(2) with T3 anisotropy: index 0 scaled by e^{2*eps3}, 1,2 by e^{-eps3}
        su2_aniso = [np.exp(2.0 * eps3), np.exp(-eps3), np.exp(-eps3)]
        for i, a in enumerate(SU2_IDX):
            g[a, a] = L2 * su2_aniso[i] * g0[a, a]

        # C^2 with T4 anisotropy: 3,4 by e^{eps4}, 5,6 by e^{-eps4}
        c2_aniso = [np.exp(eps4), np.exp(eps4), np.exp(-eps4), np.exp(-eps4)]
        for i, a in enumerate(C2_IDX):
            g[a, a] = L3 * c2_aniso[i] * g0[a, a]

        return g

    def eval_V_aniso(eps3=0.0, eps4=0.0):
        """Evaluate V_total at anisotropic perturbation."""
        g = build_metric_with_aniso(L1, L2, L3, eps3, eps4)

        # Check positive definiteness
        g_evals = eigvalsh(g)
        if not np.all(g_evals > 0):
            return np.nan

        E = orthonormal_frame(g)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        sector_evals = {}
        all_evals_flat = []

        # (0,0)
        evals_00 = np.linalg.eigvals(Omega)
        abs_00 = np.sort(np.abs(evals_00))
        sector_evals[(0, 0)] = abs_00
        for ev in abs_00:
            all_evals_flat.append((ev, 1))

        # Non-trivial
        _irrep_cache.clear()
        for p in range(MAX_PQ_SUM + 1):
            for q in range(MAX_PQ_SUM + 1 - p):
                if p == 0 and q == 0:
                    continue
                dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
                try:
                    rho, _ = get_irrep(p, q, gens, f_abc)
                    D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                    evals_pi = np.linalg.eigvals(D_pi)
                    abs_pi = np.sort(np.abs(evals_pi))
                    sector_evals[(p, q)] = abs_pi
                    for ev in abs_pi:
                        all_evals_flat.append((ev, dim_pq))
                except Exception:
                    continue

        # Global lambda_min
        all_lmin = []
        for (p, q), ev in sector_evals.items():
            nz = ev[ev > 1e-14]
            if len(nz) > 0:
                all_lmin.append(nz[0])
        lmin_global = min(all_lmin) if all_lmin else np.inf

        V_spec = compute_v_spec(all_evals_flat)
        F_BCS, _, _ = compute_fbcs_3sector(sector_evals, lmin_global, mu_ratio)

        return V_spec + F_BCS

    # Center value
    V_0 = eval_V_aniso(0, 0)
    print(f"  V_total(center) = {V_0:.6f}")

    # T3 direction (su(2) anisotropy)
    V_T3p = eval_V_aniso(eps3=eps_fd, eps4=0)
    V_T3m = eval_V_aniso(eps3=-eps_fd, eps4=0)
    H_T3 = (V_T3p + V_T3m - 2 * V_0) / eps_fd**2

    # T4 direction (C^2 anisotropy)
    V_T4p = eval_V_aniso(eps3=0, eps4=eps_fd)
    V_T4m = eval_V_aniso(eps3=0, eps4=-eps_fd)
    H_T4 = (V_T4p + V_T4m - 2 * V_0) / eps_fd**2

    # T3-T4 cross
    V_pp = eval_V_aniso(eps_fd, eps_fd)
    V_mm = eval_V_aniso(-eps_fd, -eps_fd)
    V_pm = eval_V_aniso(eps_fd, -eps_fd)
    V_mp = eval_V_aniso(-eps_fd, eps_fd)
    H_34 = (V_pp + V_mm - V_pm - V_mp) / (4 * eps_fd**2)

    H_trans = np.array([[H_T3, H_34], [H_34, H_T4]])
    evals_trans = eigvalsh(H_trans)
    trans_stable = bool(np.all(evals_trans > 0))

    print(f"\nT3/T4 transverse Hessian:")
    print(f"  H_T3 = {H_T3:.4f}")
    print(f"  H_T4 = {H_T4:.4f}")
    print(f"  H_34 = {H_34:.4f}")
    print(f"  Eigenvalues: [{evals_trans[0]:.4f}, {evals_trans[1]:.4f}]")
    print(f"  Stable (both positive): {trans_stable}")

    # V along T3, T4 for diagnostics
    print(f"\n  V along T3: {V_T3m:.6f} | {V_0:.6f} | {V_T3p:.6f}")
    print(f"  V along T4: {V_T4m:.6f} | {V_0:.6f} | {V_T4p:.6f}")

    return {
        'H_T3': H_T3,
        'H_T4': H_T4,
        'H_34': H_34,
        'H_trans': H_trans,
        'evals_trans': evals_trans,
        'trans_stable': trans_stable,
        'V_0': V_0,
        'V_T3_plus': V_T3p,
        'V_T3_minus': V_T3m,
        'V_T4_plus': V_T4p,
        'V_T4_minus': V_T4m,
    }


# =============================================================================
# MODULE 7: PLOTTING
# =============================================================================

def plot_landscape(results, min_info, mu_ratio=1.20):
    """V_total landscape with minimum marked."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # Panel 1: V_total contour
    ax = axes[0, 0]
    V = results['V_total'][mu_ratio]
    c = ax.contourf(TAU, EPS, V, levels=40, cmap='viridis')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title(f'V_total (mu/lmin={mu_ratio})')

    # Panel 2: V_spec alone
    ax = axes[0, 1]
    c = ax.contourf(TAU, EPS, results['V_spec'], levels=40, cmap='plasma')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('V_spec (spectral action)')

    # Panel 3: F_BCS alone
    ax = axes[0, 2]
    F = results['F_BCS'][mu_ratio]
    c = ax.contourf(TAU, EPS, F, levels=40, cmap='RdBu_r')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title(f'F_BCS^{{3-sector}} (mu/lmin={mu_ratio})')

    # Panel 4: lambda_min
    ax = axes[1, 0]
    c = ax.contourf(TAU, EPS, results['lambda_min'], levels=40, cmap='YlOrRd')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('lambda_min (global)')

    # Panel 5: V_total along tau at eps=eps_min
    ax = axes[1, 1]
    ej = min_info['grid_idx'][1]
    ax.plot(tau, V[:, ej], 'b-o', markersize=3, label=f'eps={eps[ej]:.3f}')
    # Also plot Jensen (eps=0) for comparison
    j0 = N_EPS // 2
    ax.plot(tau, V[:, j0], 'k--', linewidth=1, alpha=0.7, label='Jensen (eps=0)')
    ax.axvline(min_info['tau_min'], color='red', linestyle=':', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('V_total')
    ax.set_title('V_total slices')
    ax.legend(fontsize=8)

    # Panel 6: V_total along eps at tau=tau_min
    ax = axes[1, 2]
    ti = min_info['grid_idx'][0]
    ax.plot(eps, V[ti, :], 'b-o', markersize=3, label=f'tau={tau[ti]:.3f}')
    ax.axvline(min_info['eps_min'], color='red', linestyle=':', alpha=0.5)
    ax.set_xlabel('epsilon')
    ax.set_ylabel('V_total')
    ax.set_title(f'V_total at tau={tau[ti]:.3f}')
    ax.legend(fontsize=8)

    plt.suptitle(f'Session 30Ba: V_total Landscape | min at tau={min_info["tau_min"]:.3f}, '
                 f'eps={min_info["eps_min"]:.3f}', fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT_LANDSCAPE, dpi=150, bbox_inches='tight')
    print(f"Saved {OUT_LANDSCAPE}")


def plot_weinberg(results, min_info):
    """Weinberg angle contour with minimum and SM target."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    c = ax.contourf(TAU, EPS, results['sin2_tw'], levels=30, cmap='viridis')
    plt.colorbar(c, ax=ax, label='sin^2(theta_W)')

    # SM target contour
    cs = ax.contour(TAU, EPS, results['sin2_tw'], levels=[0.20, 0.231, 0.25],
                    colors=['white', 'red', 'white'], linewidths=[1, 2.5, 1])
    ax.clabel(cs, inline=True, fontsize=9, fmt='%.3f')

    # Mark minimum
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=20,
            markeredgecolor='white', markeredgewidth=1)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5, label='Jensen')

    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('epsilon', fontsize=12)
    ax.set_title(f'sin^2(theta_W) | at min: {min_info["sin2_tw_at_min"]:.4f} '
                 f'(SM: 0.231)', fontsize=12)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(OUT_WEINBERG, dpi=150, bbox_inches='tight')
    print(f"Saved {OUT_WEINBERG}")


def plot_phi(results, min_info):
    """Phi_paasch contour with minimum marked."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for k, (name, grid, ref) in enumerate([
        ('phi_30 = lmin(3,0)/lmin(0,0)', results['phi_30'], PHI),
        ('phi_03 = lmin(0,3)/lmin(0,0)', results['phi_03'], PHI),
    ]):
        ax = axes[k]
        c = ax.contourf(TAU, EPS, grid, levels=30, cmap='plasma')
        plt.colorbar(c, ax=ax)
        # Mark phi contour
        cs = ax.contour(TAU, EPS, grid, levels=[ref],
                        colors=['lime'], linewidths=[2])
        ax.clabel(cs, inline=True, fontsize=9, fmt='%.4f')
        ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
        ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
        ax.set_xlabel('tau')
        ax.set_ylabel('epsilon')
        ax.set_title(name)

    plt.suptitle(f'Phi_paasch | at min: {min_info["phi_30_at_min"]:.4f} '
                 f'(phi={PHI:.4f})', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PHI, dpi=150, bbox_inches='tight')
    print(f"Saved {OUT_PHI}")


def plot_fbcs(results, min_info, mu_ratio=1.20):
    """F_BCS landscape and per-sector breakdown."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: F_BCS total
    ax = axes[0, 0]
    c = ax.contourf(TAU, EPS, results['F_BCS'][mu_ratio], levels=40, cmap='RdBu_r')
    plt.colorbar(c, ax=ax)
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'r*', markersize=15)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title(f'F_BCS total (mu/lmin={mu_ratio})')

    # Panel 2: F_cond (0,0) sector
    ax = axes[0, 1]
    c = ax.contourf(TAU, EPS, results['F_cond_00'], levels=40, cmap='RdBu_r')
    plt.colorbar(c, ax=ax)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('F_cond (0,0) * mult=1')

    # Panel 3: F_cond (3,0) sector
    ax = axes[1, 0]
    c = ax.contourf(TAU, EPS, results['F_cond_30'] * 100, levels=40, cmap='RdBu_r')
    plt.colorbar(c, ax=ax)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('F_cond (3,0) * mult=100')

    # Panel 4: n_supercritical modes
    ax = axes[1, 1]
    c = ax.contourf(TAU, EPS, results['n_supercrit'][mu_ratio], levels=20, cmap='YlOrRd')
    plt.colorbar(c, ax=ax)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title(f'N supercritical modes (mu/lmin={mu_ratio})')

    plt.suptitle(f'F_BCS Landscape (mu/lmin={mu_ratio})', fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT_FBCS, dpi=150, bbox_inches='tight')
    print(f"Saved {OUT_FBCS}")


def plot_dos(results, min_info):
    """DOS landscape."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    c = ax.contourf(TAU, EPS, results['dos'], levels=30, cmap='hot')
    plt.colorbar(c, ax=ax, label='N(E_F)')
    ax.plot(min_info['tau_min'], min_info['eps_min'], 'c*', markersize=15)
    ax.plot(tau, np.zeros_like(tau), 'w--', linewidth=1, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title(f'DOS at lambda_min (delta_E={DELTA_E_DOS})')
    plt.tight_layout()
    plt.savefig(OUT_DOS, dpi=150, bbox_inches='tight')
    print(f"Saved {OUT_DOS}")


# =============================================================================
# MODULE 8: MAIN
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 70)
    print("Session 30Ba Step 2: BCS Grid on U(2)-invariant surface")
    print(f"  Grid: {N_TAU}x{N_EPS} = {N_TAU*N_EPS} points")
    print(f"  max_pq_sum = {MAX_PQ_SUM}, mu_ratios = {MU_RATIOS}")
    print(f"  rho_spec = {RHO_SPEC}")
    print("=" * 70)

    # Infrastructure
    print("\n[SETUP] Building algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # Compute grid
    print(f"\n[COMPUTE] Running BCS grid ({N_TAU*N_EPS} points)...")
    results = compute_bcs_grid(B_ab, gens, f_abc, gammas)
    t_grid = time.time() - t_start
    print(f"\nGrid computation: {t_grid:.1f}s")

    # Find minimum and Hessian for each mu_ratio
    min_info = {}
    for mu_r in MU_RATIOS:
        print(f"\n{'=' * 70}")
        print(f"MINIMUM AT mu/lmin = {mu_r}")
        print(f"{'=' * 70}")
        min_info[mu_r] = find_minimum_and_hessian(results, mu_ratio=mu_r)

    # Primary result at mu/lmin = 1.20
    primary = min_info[1.20]

    # 5D stability check
    stab = check_5d_stability(B_ab, gens, f_abc, gammas, primary, mu_ratio=1.20)

    # Summary
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")

    # Compare Jensen to off-Jensen minimum
    j0 = N_EPS // 2  # eps=0 column
    print(f"\nJensen curve comparison (eps=0 vs minimum):")
    # Find tau at Jensen minimum
    V_jensen = results['V_total'][1.20][:, j0]
    ti_j = np.argmin(V_jensen)
    tau_j = results['tau'][ti_j]
    print(f"  Jensen min: tau={tau_j:.3f}, V={V_jensen[ti_j]:.6f}")
    print(f"  Off-Jensen min: tau={primary['tau_min']:.3f}, eps={primary['eps_min']:.3f}, "
          f"V={primary['V_min']:.6f}")
    print(f"  V improvement: {V_jensen[ti_j] - primary['V_min']:.6f}")

    print(f"\nPhysical observables at off-Jensen minimum:")
    print(f"  sin^2(theta_W) = {primary['sin2_tw_at_min']:.6f} (SM: 0.231)")
    print(f"  g1/g2 = {primary['g1g2_at_min']:.6f}")
    print(f"  phi_30 = {primary['phi_30_at_min']:.6f} (phi: {PHI:.6f})")
    print(f"  phi_03 = {primary['phi_03_at_min']:.6f}")
    print(f"  lambda_min = {primary['lambda_min_at_min']:.6f}")

    print(f"\nStability:")
    print(f"  2D Hessian: eigenvalues [{primary['evals_H'][0]:.4f}, {primary['evals_H'][1]:.4f}]")
    print(f"  2D stable: {primary['both_positive']}")
    print(f"  T3/T4 transverse: [{stab['evals_trans'][0]:.4f}, {stab['evals_trans'][1]:.4f}]")
    print(f"  4D stable: {primary['both_positive'] and stab['trans_stable']}")

    # Gate verdicts
    print(f"\n{'=' * 70}")
    print("GATE VERDICTS")
    print(f"{'=' * 70}")

    # P-30w: sin^2(theta_W) in [0.20, 0.25]
    sin2 = primary['sin2_tw_at_min']
    p30w = 0.20 <= sin2 <= 0.25
    print(f"\nP-30w: sin^2(theta_W) in [0.20, 0.25]?")
    print(f"  Value: {sin2:.6f}")
    print(f"  Verdict: {'FIRES' if p30w else 'DOES NOT FIRE'}")

    # 2D stability
    print(f"\n2D minimum stability:")
    print(f"  Verdict: {'PASS' if primary['both_positive'] else 'FAIL (saddle or boundary)'}")

    # 4D stability (including T3/T4)
    full_4d = primary['both_positive'] and stab['trans_stable']
    print(f"\n4D stability (2D + T3/T4):")
    print(f"  Verdict: {'PASS' if full_4d else 'FAIL'}")

    t_total = time.time() - t_start
    print(f"\nTotal runtime: {t_total:.1f}s")

    # Save results
    print(f"\n[SAVE] Writing outputs...")
    save_dict = {
        'tau': results['tau'],
        'eps': results['eps'],
        'V_spec': results['V_spec'],
        'F_BCS_1p00': results['F_BCS'][1.0],
        'F_BCS_1p20': results['F_BCS'][1.20],
        'V_total_1p00': results['V_total'][1.0],
        'V_total_1p20': results['V_total'][1.20],
        'lambda_min': results['lambda_min'],
        'dos': results['dos'],
        'sin2_tw': results['sin2_tw'],
        'g1g2': results['g1g2'],
        'phi_30': results['phi_30'],
        'phi_03': results['phi_03'],
        'lmin_00': results['lmin_00'],
        'lmin_30': results['lmin_30'],
        'lmin_03': results['lmin_03'],
        'F_cond_00': results['F_cond_00'],
        'F_cond_30': results['F_cond_30'],
        'F_cond_03': results['F_cond_03'],
        'n_supercrit_1p00': results['n_supercrit'][1.0],
        'n_supercrit_1p20': results['n_supercrit'][1.20],
        # Minimum info (mu=1.20)
        'tau_min': primary['tau_min'],
        'eps_min': primary['eps_min'],
        'V_min': primary['V_min'],
        'V_spec_min': primary['V_spec_min'],
        'F_BCS_min': primary['F_BCS_min'],
        'lambda_min_at_min': primary['lambda_min_at_min'],
        'sin2_tw_at_min': primary['sin2_tw_at_min'],
        'g1g2_at_min': primary['g1g2_at_min'],
        'phi_30_at_min': primary['phi_30_at_min'],
        'phi_03_at_min': primary['phi_03_at_min'],
        'dos_at_min': primary['dos_at_min'],
        'H_2d': primary['H'],
        'evals_H_2d': primary['evals_H'],
        'both_positive_2d': primary['both_positive'],
        # Gate verdicts
        'P_30w': p30w,
        'P_30w_value': sin2,
        'stable_4d': full_4d,
    }
    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"  Saved: {OUT_NPZ}")

    # 5D stability
    np.savez_compressed(OUT_STAB,
                        tau_min=primary['tau_min'],
                        eps_min=primary['eps_min'],
                        H_T3=stab['H_T3'],
                        H_T4=stab['H_T4'],
                        H_34=stab['H_34'],
                        H_trans=stab['H_trans'],
                        evals_trans=stab['evals_trans'],
                        trans_stable=stab['trans_stable'],
                        H_2d=primary['H'],
                        evals_H_2d=primary['evals_H'])
    print(f"  Saved: {OUT_STAB}")

    # Plots
    plot_landscape(results, primary, mu_ratio=1.20)
    plot_weinberg(results, primary)
    plot_phi(results, primary)
    plot_fbcs(results, primary, mu_ratio=1.20)
    plot_dos(results, primary)

    print(f"\n{'=' * 70}")
    print(f"Step 2 COMPLETE. {N_TAU*N_EPS} grid points in {t_total:.1f}s.")
    print(f"{'=' * 70}")

    return results, min_info, stab


if __name__ == '__main__':
    results, min_info, stab = main()
