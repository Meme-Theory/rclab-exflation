#!/usr/bin/env python3
"""
Session 29Bb-3: BCS Gap Equation with Bogoliubov Occupation
============================================================

Replace the Fermi-Dirac distribution in the BCS gap equation with the
non-equilibrium Bogoliubov occupation n_k = B_k from KC-1 parametric amplification.

BEC-side gap equation (Landau advisory):
  Delta_n = -sum_m V_{nm} * Delta_m * (1 + 2*B_m) / (2 * E_m)
  where E_m = sqrt((lambda_m - mu)^2 + Delta_m^2)
  and B_m = |beta_m|^2 from s28a_bogoliubov_coefficients.npz

The (1 + 2*B) factor is the STIMULATED EMISSION enhancement -- bosonic
occupation enhances pairing, unlike fermionic Pauli blocking.

Gate P-29c: Delta(B_k)/lambda_min > 0.01 at 3 load-bearing sectors
Gate B-29c: Delta = 0 for all sectors --> non-equilibrium too hot for BCS

Load-bearing sectors: (3,0), (0,3), (0,0)
Chemical potential: mu/lambda_min = 1.20 (confirmed minimum from 29B-1)

Author: phonon-exflation-sim agent, Session 29Bb
Date: 2026-02-28
"""

import numpy as np
from scipy.optimize import curve_fit
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(SCRIPT_DIR)
BOG_FILE = DATA_DIR / 's28a_bogoliubov_coefficients.npz'
S27_FILE = DATA_DIR / 's27_multisector_bcs.npz'
OUT_NPZ = DATA_DIR / 's29b_bogoliubov_bcs.npz'
OUT_PNG = DATA_DIR / 's29b_bogoliubov_bcs.png'
OUT_TXT = DATA_DIR / 's29b_bogoliubov_bcs.txt'

MU_RATIO = 1.20
LOAD_BEARING = [(0, 0), (3, 0), (0, 3)]
GATE_THRESHOLD = 0.01  # Delta/lambda_min > 0.01

# BCS self-consistency parameters
MAX_ITER = 500
CONV_TOL = 1e-10
MIXING_ALPHA = 0.3  # Mixing parameter for stability


# =============================================================================
# MODULE 1: DATA LOADING AND B_k MAPPING
# =============================================================================

def load_data():
    """Load Bogoliubov coefficients and s27 BCS data."""
    bog = np.load(BOG_FILE, allow_pickle=True)
    s27 = np.load(S27_FILE, allow_pickle=True)
    return bog, s27


def map_bk_to_sector(bog, s27, p, q, tau_idx_s27):
    """
    Map Bogoliubov occupation B_k to the eigenvalue grid of sector (p,q)
    at a given s27 tau index.

    The Bogoliubov data has B_k(tau, mode) for 11,424 modes across all sectors,
    indexed by sector_p_ref and sector_q_ref. The s27 data has eigenvalues
    per sector at each tau.

    We match modes by:
    1. Select modes in sector (p,q) from Bogoliubov data
    2. Find the closest Bogoliubov tau to the s27 tau
    3. Sort both Bogoliubov omega and s27 |eigenvalues| within the sector
    4. Map B_k by index (both are sorted by eigenvalue magnitude)

    Parameters
    ----------
    bog : npz archive
        Bogoliubov coefficient data.
    s27 : npz archive
        Multi-sector BCS data.
    p, q : int
        Sector labels.
    tau_idx_s27 : int
        Index into s27 tau_values.

    Returns
    -------
    B_mapped : ndarray
        Bogoliubov occupation for each mode in the sector, same order as s27 eigenvalues.
    omega_bog : ndarray
        Bogoliubov omega values (for diagnostics).
    evals_s27 : ndarray
        s27 eigenvalues in the sector.
    """
    tau_s27 = s27['tau_values'][tau_idx_s27]
    tau_bog = bog['tau_values']

    # Find closest Bogoliubov tau
    bog_tau_idx = np.argmin(np.abs(tau_bog - tau_s27))
    tau_bog_used = tau_bog[bog_tau_idx]

    # Get sector mask in Bogoliubov data
    sector_p = bog['sector_p_ref']
    sector_q = bog['sector_q_ref']
    mask = (sector_p == p) & (sector_q == q)

    B_sector = bog['B_k'][bog_tau_idx, mask]
    omega_sector = bog['omega_tracked'][bog_tau_idx, mask]

    # Get s27 eigenvalues
    evals_key = f'evals_{p}_{q}_{tau_idx_s27}'
    evals_s27 = s27[evals_key]
    abs_evals_s27 = np.abs(evals_s27)

    # Both datasets should have the same number of modes per sector
    n_bog = len(B_sector)
    n_s27 = len(evals_s27)

    if n_bog != n_s27:
        print(f"  WARNING: mode count mismatch ({p},{q}): bog={n_bog}, s27={n_s27}")
        # If mismatch, interpolate B_k from omega to s27 eigenvalues
        sort_bog = np.argsort(omega_sector)
        sort_s27 = np.argsort(abs_evals_s27)
        B_mapped = np.interp(abs_evals_s27[sort_s27], omega_sector[sort_bog], B_sector[sort_bog])
        # Unsort to match s27 eigenvalue order
        B_out = np.zeros(n_s27)
        B_out[sort_s27] = B_mapped
        return B_out, omega_sector, evals_s27

    # Same mode count: sort both by magnitude and match by index
    sort_bog = np.argsort(omega_sector)
    sort_s27 = np.argsort(abs_evals_s27)

    # Map: B_mapped[sort_s27[k]] = B_sector[sort_bog[k]]
    B_mapped = np.zeros(n_s27)
    for k in range(n_s27):
        B_mapped[sort_s27[k]] = B_sector[sort_bog[k]]

    return B_mapped, omega_sector, evals_s27


# =============================================================================
# MODULE 2: BCS GAP EQUATION WITH BOGOLIUBOV OCCUPATION
# =============================================================================

def solve_bcs_gap_bogoliubov(evals, V_nm, B_k, mu, max_iter=MAX_ITER,
                              tol=CONV_TOL, alpha=MIXING_ALPHA):
    """
    Solve the BEC-side BCS gap equation self-consistently with Bogoliubov occupation.

    Delta_n = -sum_m V_{nm} * Delta_m * (1 + 2*B_m) / (2 * E_m)
    E_m = sqrt((lambda_m - mu)^2 + Delta_m^2)

    Uses mixing for stability: Delta_new = alpha * Delta_computed + (1-alpha) * Delta_old

    Parameters
    ----------
    evals : ndarray (N,)
        Dirac eigenvalues (absolute values) in the sector.
    V_nm : ndarray (N, N)
        Kosmann pairing matrix.
    B_k : ndarray (N,)
        Bogoliubov occupation numbers.
    mu : float
        Chemical potential.
    max_iter : int
        Maximum iterations.
    tol : float
        Convergence tolerance on max|Delta_new - Delta_old|.
    alpha : float
        Mixing parameter.

    Returns
    -------
    Delta : ndarray (N,)
        Self-consistent gap values.
    converged : bool
        Whether the iteration converged.
    n_iter : int
        Number of iterations used.
    history : list
        Convergence history (max|Delta_diff| per iteration).
    """
    N = len(evals)
    abs_evals = np.abs(evals)
    xi = abs_evals - mu  # xi_m = |lambda_m| - mu

    # Initial seed: uniform gap proportional to max V matrix element
    V_max = np.max(np.abs(V_nm))
    Delta = np.ones(N) * 0.05 * V_max  # Small initial gap

    history = []
    converged = False
    n_iter = 0

    for iteration in range(max_iter):
        E_m = np.sqrt(xi**2 + Delta**2)

        # BEC enhancement factor
        enhancement = 1.0 + 2.0 * B_k  # (1 + 2*B_m)

        # Gap equation kernel: K_m = Delta_m * (1 + 2*B_m) / (2 * E_m)
        kernel = Delta * enhancement / (2.0 * E_m)

        # New gap: Delta_n = -sum_m V_{nm} * kernel_m
        Delta_new = -V_nm @ kernel

        # Mixing for stability
        Delta_mixed = alpha * Delta_new + (1.0 - alpha) * Delta

        # Convergence check
        diff = np.max(np.abs(Delta_mixed - Delta))
        history.append(diff)

        Delta = Delta_mixed
        n_iter = iteration + 1

        if diff < tol:
            converged = True
            break

    return Delta, converged, n_iter, history


def solve_bcs_gap_vacuum(evals, V_nm, mu, max_iter=MAX_ITER,
                          tol=CONV_TOL, alpha=MIXING_ALPHA):
    """
    Solve the standard BCS gap equation at T=0 (vacuum, B_k=0).

    Delta_n = -sum_m V_{nm} * Delta_m / (2 * E_m)

    This is the reference: what gap would form WITHOUT Bogoliubov injection.
    """
    B_zero = np.zeros(len(evals))
    return solve_bcs_gap_bogoliubov(evals, V_nm, B_zero, mu, max_iter, tol, alpha)


def solve_bcs_gap_thermal(evals, V_nm, mu, T, max_iter=MAX_ITER,
                           tol=CONV_TOL, alpha=MIXING_ALPHA):
    """
    Solve the thermal BCS gap equation at temperature T.

    Delta_n = -sum_m V_{nm} * Delta_m * tanh(E_m/(2T)) / (2 * E_m)

    This uses Fermi-Dirac statistics for comparison.
    """
    N = len(evals)
    abs_evals = np.abs(evals)
    xi = abs_evals - mu

    Delta = np.ones(N) * 0.05 * np.max(np.abs(V_nm))
    history = []
    converged = False
    n_iter = 0

    for iteration in range(max_iter):
        E_m = np.sqrt(xi**2 + Delta**2)

        if T > 1e-15:
            thermal_factor = np.tanh(E_m / (2.0 * T))
        else:
            thermal_factor = np.ones(N)

        kernel = Delta * thermal_factor / (2.0 * E_m)
        Delta_new = -V_nm @ kernel
        Delta_mixed = alpha * Delta_new + (1.0 - alpha) * Delta

        diff = np.max(np.abs(Delta_mixed - Delta))
        history.append(diff)
        Delta = Delta_mixed
        n_iter = iteration + 1

        if diff < tol:
            converged = True
            break

    return Delta, converged, n_iter, history


# =============================================================================
# MODULE 3: EFFECTIVE TEMPERATURE EXTRACTION
# =============================================================================

def fit_bose_einstein(omega, B_k):
    """
    Fit B_k to a Bose-Einstein distribution: n_BE = 1/(exp((omega - mu_BE)/T_eff) - 1)

    Parameters
    ----------
    omega : ndarray
        Frequencies (eigenvalue magnitudes).
    B_k : ndarray
        Bogoliubov occupation.

    Returns
    -------
    T_eff : float
        Effective temperature.
    mu_BE : float
        Effective chemical potential for BE distribution.
    chi2 : float
        Reduced chi-squared goodness of fit.
    """
    # Filter out zero or near-zero B_k values
    mask = B_k > 1e-8
    if np.sum(mask) < 3:
        return np.nan, np.nan, np.inf

    omega_fit = omega[mask]
    B_fit = B_k[mask]

    def bose_einstein(w, T, mu_be):
        arg = (w - mu_be) / T
        # Clip to avoid overflow
        arg = np.clip(arg, -50, 50)
        return 1.0 / (np.exp(arg) - 1.0 + 1e-30)

    try:
        # Initial guess: T ~ spread of omega, mu_BE ~ min(omega)
        T_guess = 0.3 * (np.max(omega_fit) - np.min(omega_fit))
        mu_guess = np.min(omega_fit) - 0.1

        popt, pcov = curve_fit(bose_einstein, omega_fit, B_fit,
                               p0=[T_guess, mu_guess],
                               bounds=([1e-6, -10], [100, np.max(omega_fit)]),
                               maxfev=5000)
        T_eff, mu_BE = popt

        # Reduced chi-squared
        B_pred = bose_einstein(omega_fit, T_eff, mu_BE)
        residuals = B_fit - B_pred
        chi2 = np.sum(residuals**2) / (len(B_fit) - 2)

        return T_eff, mu_BE, chi2
    except (RuntimeError, ValueError):
        return np.nan, np.nan, np.inf


# =============================================================================
# MODULE 4: MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()
    print("Session 29Bb-3: BCS Gap with Bogoliubov Occupation")
    print("=" * 70)

    # Load data
    print("\n[1] Loading data...")
    bog, s27 = load_data()

    tau_values_s27 = s27['tau_values']
    sectors = s27['sectors']
    print(f"  s27 tau grid: {tau_values_s27}")
    print(f"  Bogoliubov tau grid: {bog['tau_values'][:10]}... ({len(bog['tau_values'])} points)")
    print(f"  Load-bearing sectors: {LOAD_BEARING}")
    print(f"  mu/lambda_min = {MU_RATIO}")

    # Results storage
    results = {}
    all_deltas = {}
    all_T_eff = {}
    all_diagnostics = {}

    print(f"\n[2] Computing BCS gap for each sector at each tau...")

    for p, q in LOAD_BEARING:
        print(f"\n  --- Sector ({p},{q}) ---")

        sector_idx = None
        for si in range(len(sectors)):
            if sectors[si, 0] == p and sectors[si, 1] == q:
                sector_idx = si
                break
        if sector_idx is None:
            print(f"    Sector ({p},{q}) not found in s27 data!")
            continue

        pw_mult = sectors[sector_idx, 3]
        print(f"    Peter-Weyl multiplicity: {pw_mult}")

        delta_bog_list = []
        delta_vac_list = []
        delta_thermal_list = []
        T_eff_list = []
        B_mean_list = []
        lmin_list = []

        for tau_idx in range(len(tau_values_s27)):
            tau = tau_values_s27[tau_idx]

            # Load eigenvalues and pairing matrix
            evals = s27[f'evals_{p}_{q}_{tau_idx}']
            V_nm = s27[f'V_{p}_{q}_{tau_idx}']

            # Map Bogoliubov B_k to this sector
            B_mapped, omega_bog, evals_check = map_bk_to_sector(bog, s27, p, q, tau_idx)

            # Chemical potential
            abs_evals = np.abs(evals)
            lmin = np.min(abs_evals[abs_evals > 1e-14])
            mu = MU_RATIO * lmin
            lmin_list.append(lmin)

            # Mean B_k for diagnostics
            B_mean = np.mean(B_mapped)
            B_max = np.max(B_mapped)
            B_mean_list.append(B_mean)

            # Solve with Bogoliubov occupation
            Delta_bog, conv_bog, niter_bog, hist_bog = solve_bcs_gap_bogoliubov(
                evals, V_nm, B_mapped, mu
            )
            Delta_max_bog = np.max(np.abs(Delta_bog))

            # Solve at vacuum (T=0, B=0)
            Delta_vac, conv_vac, niter_vac, hist_vac = solve_bcs_gap_vacuum(
                evals, V_nm, mu
            )
            Delta_max_vac = np.max(np.abs(Delta_vac))

            # Fit T_eff
            omega_sorted = np.sort(np.abs(evals))
            B_sorted_by_eval = B_mapped[np.argsort(np.abs(evals))]
            T_eff, mu_BE, chi2 = fit_bose_einstein(omega_sorted, B_sorted_by_eval)
            T_eff_list.append(T_eff)

            # Solve at thermal T=T_eff (if T_eff is finite)
            if np.isfinite(T_eff) and T_eff > 1e-10:
                Delta_th, conv_th, niter_th, hist_th = solve_bcs_gap_thermal(
                    evals, V_nm, mu, T_eff
                )
                Delta_max_th = np.max(np.abs(Delta_th))
            else:
                Delta_max_th = np.nan
                Delta_th = np.zeros_like(Delta_bog)

            delta_bog_list.append(Delta_max_bog)
            delta_vac_list.append(Delta_max_vac)
            delta_thermal_list.append(Delta_max_th)

            ratio_bog = Delta_max_bog / lmin if lmin > 0 else 0
            ratio_vac = Delta_max_vac / lmin if lmin > 0 else 0

            print(f"    tau={tau:.2f}: Delta_bog/lmin={ratio_bog:.4f}, "
                  f"Delta_vac/lmin={ratio_vac:.4f}, "
                  f"B_mean={B_mean:.4f}, B_max={B_max:.4f}, "
                  f"T_eff={T_eff:.4f}" if np.isfinite(T_eff)
                  else f"    tau={tau:.2f}: Delta_bog/lmin={ratio_bog:.4f}, "
                  f"Delta_vac/lmin={ratio_vac:.4f}, "
                  f"B_mean={B_mean:.4f}, B_max={B_max:.4f}, "
                  f"T_eff=NaN")

        results[(p, q)] = {
            'delta_bog': np.array(delta_bog_list),
            'delta_vac': np.array(delta_vac_list),
            'delta_thermal': np.array(delta_thermal_list),
            'T_eff': np.array(T_eff_list),
            'B_mean': np.array(B_mean_list),
            'lambda_min': np.array(lmin_list),
        }

    # Gate evaluation
    print(f"\n{'=' * 70}")
    print("GATE EVALUATION")
    print(f"{'=' * 70}")

    gate_results = {}
    for p, q in LOAD_BEARING:
        if (p, q) not in results:
            continue
        r = results[(p, q)]
        ratios = r['delta_bog'] / r['lambda_min']
        max_ratio = np.max(ratios)
        best_tau_idx = np.argmax(ratios)
        best_tau = tau_values_s27[best_tau_idx]

        passes = max_ratio > GATE_THRESHOLD
        gate_results[(p, q)] = {
            'max_ratio': max_ratio,
            'best_tau': best_tau,
            'passes': passes,
        }

        print(f"\n  Sector ({p},{q}):")
        print(f"    Max Delta/lambda_min = {max_ratio:.6f} at tau = {best_tau:.2f}")
        print(f"    Gate threshold: {GATE_THRESHOLD}")
        print(f"    PASSES: {passes}")

        # Comparison with vacuum
        vac_ratios = r['delta_vac'] / r['lambda_min']
        max_vac = np.max(vac_ratios)
        enhancement = max_ratio / max(max_vac, 1e-15) if max_vac > 1e-15 else np.inf
        print(f"    Vacuum Delta/lmin = {max_vac:.6f}")
        print(f"    Bogoliubov / Vacuum enhancement: {enhancement:.2f}x")

    # Overall gate verdict
    all_pass = all(g['passes'] for g in gate_results.values())
    any_pass = any(g['passes'] for g in gate_results.values())

    print(f"\n{'=' * 70}")
    if all_pass:
        verdict = 'PASS'
        print(f"  P-29c FIRES: Delta(B_k)/lambda_min > {GATE_THRESHOLD} at ALL 3 load-bearing sectors")
        print(f"  Thermal Goldilocks CONFIRMED: non-equilibrium distribution supports BCS")
    elif any_pass:
        verdict = 'PARTIAL'
        passing = [f"({p},{q})" for (p, q), g in gate_results.items() if g['passes']]
        failing = [f"({p},{q})" for (p, q), g in gate_results.items() if not g['passes']]
        print(f"  PARTIAL: {', '.join(passing)} pass, {', '.join(failing)} fail")
    else:
        verdict = 'FAIL'
        print(f"  B-29c FIRES: Delta = 0 for all sectors")
        print(f"  Non-equilibrium distribution is TOO HOT for BCS condensation")
    print(f"{'=' * 70}")

    t_total = time.time() - t_start
    print(f"\nTotal runtime: {t_total:.1f}s")

    # Save results
    print(f"\n[SAVE] Writing output files...")
    save_dict = {
        'tau_values': tau_values_s27,
        'mu_ratio': MU_RATIO,
        'gate_threshold': GATE_THRESHOLD,
        'verdict': verdict,
    }

    for p, q in LOAD_BEARING:
        if (p, q) not in results:
            continue
        r = results[(p, q)]
        prefix = f's{p}_{q}'
        save_dict[f'{prefix}_delta_bog'] = r['delta_bog']
        save_dict[f'{prefix}_delta_vac'] = r['delta_vac']
        save_dict[f'{prefix}_delta_thermal'] = r['delta_thermal']
        save_dict[f'{prefix}_T_eff'] = r['T_eff']
        save_dict[f'{prefix}_B_mean'] = r['B_mean']
        save_dict[f'{prefix}_lambda_min'] = r['lambda_min']
        if (p, q) in gate_results:
            save_dict[f'{prefix}_max_ratio'] = gate_results[(p, q)]['max_ratio']
            save_dict[f'{prefix}_best_tau'] = gate_results[(p, q)]['best_tau']

    np.savez(OUT_NPZ, **save_dict)

    # Text output
    with open(OUT_TXT, 'w') as f:
        f.write("Session 29Bb-3: BCS Gap with Bogoliubov Occupation\n")
        f.write(f"mu/lambda_min = {MU_RATIO}, gate threshold = {GATE_THRESHOLD}\n")
        f.write(f"Verdict: {verdict}\n\n")
        for p, q in LOAD_BEARING:
            if (p, q) not in results:
                continue
            r = results[(p, q)]
            f.write(f"\nSector ({p},{q}):\n")
            f.write(f"{'tau':>6s}  {'Delta_bog/lmin':>14s}  {'Delta_vac/lmin':>14s}  "
                    f"{'Enhancement':>12s}  {'B_mean':>8s}  {'T_eff':>8s}\n")
            for ti in range(len(tau_values_s27)):
                tau = tau_values_s27[ti]
                db = r['delta_bog'][ti] / r['lambda_min'][ti]
                dv = r['delta_vac'][ti] / r['lambda_min'][ti]
                enh = db / max(dv, 1e-15) if dv > 1e-15 else float('inf')
                bm = r['B_mean'][ti]
                te = r['T_eff'][ti]
                f.write(f"{tau:6.2f}  {db:14.6f}  {dv:14.6f}  {enh:12.2f}  "
                        f"{bm:8.4f}  {te:8.4f}\n" if np.isfinite(te)
                        else f"{tau:6.2f}  {db:14.6f}  {dv:14.6f}  {enh:12.2f}  "
                        f"{bm:8.4f}  {'NaN':>8s}\n")
            if (p, q) in gate_results:
                g = gate_results[(p, q)]
                f.write(f"  Max Delta_bog/lmin = {g['max_ratio']:.6f} at tau = {g['best_tau']:.2f}\n")
                f.write(f"  PASSES gate: {g['passes']}\n")

    # Plot
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    for col, (p, q) in enumerate(LOAD_BEARING):
        if (p, q) not in results:
            continue
        r = results[(p, q)]

        # Top row: Delta/lambda_min vs tau
        ax = axes[0, col]
        ratios_bog = r['delta_bog'] / r['lambda_min']
        ratios_vac = r['delta_vac'] / r['lambda_min']
        ax.plot(tau_values_s27, ratios_bog, 'bo-', label='Bogoliubov', markersize=4)
        ax.plot(tau_values_s27, ratios_vac, 'rs--', label='Vacuum (T=0)', markersize=4)
        ratios_th = r['delta_thermal'] / r['lambda_min']
        valid_th = np.isfinite(ratios_th)
        if np.any(valid_th):
            ax.plot(tau_values_s27[valid_th], ratios_th[valid_th], 'g^:', label='Thermal T_eff',
                    markersize=4)
        ax.axhline(y=GATE_THRESHOLD, color='black', linestyle='--', linewidth=0.5,
                   label=f'Gate: {GATE_THRESHOLD}')
        ax.set_xlabel('tau')
        ax.set_ylabel('Delta / lambda_min')
        ax.set_title(f'Sector ({p},{q})')
        ax.legend(fontsize=7)
        ax.set_ylim(bottom=-0.01)

        # Bottom row: B_k statistics vs tau
        ax = axes[1, col]
        ax.plot(tau_values_s27, r['B_mean'], 'ko-', label='mean(B_k)', markersize=4)
        ax2 = ax.twinx()
        valid_T = np.isfinite(r['T_eff'])
        if np.any(valid_T):
            ax2.plot(tau_values_s27[valid_T], r['T_eff'][valid_T], 'r^-',
                     label='T_eff', markersize=4, alpha=0.7)
            ax2.set_ylabel('T_eff', color='red')
        ax.set_xlabel('tau')
        ax.set_ylabel('mean(B_k)')
        ax.set_title(f'Bogoliubov statistics ({p},{q})')
        ax.legend(loc='upper left', fontsize=7)

    plt.suptitle(f'29B-3: BCS Gap with Bogoliubov Occupation | Verdict: {verdict}',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_NPZ}")
    print(f"  Saved: {OUT_TXT}")
    print(f"  Saved: {OUT_PNG}")

    # Append to gate verdicts
    verdicts_file = DATA_DIR / 's29b_gate_verdicts.txt'
    with open(verdicts_file, 'a') as f:
        f.write(f"\n29B-3 BCS Gap with Bogoliubov Occupation:\n")
        f.write(f"  Verdict: {verdict}\n")
        for (p, q), g in gate_results.items():
            f.write(f"  ({p},{q}): Delta/lmin = {g['max_ratio']:.6f} at tau = {g['best_tau']:.2f} "
                    f"({'PASS' if g['passes'] else 'FAIL'})\n")

    return verdict, results, gate_results


if __name__ == '__main__':
    verdict, results, gate_results = main()
