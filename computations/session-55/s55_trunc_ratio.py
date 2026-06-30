#!/usr/bin/env python3
"""
S55 TRUNC-RATIO-55 — Fermionic/Bosonic Spectral Action Ratio at Higher Truncation
==================================================================================

Computes S_f, S_b, and S_f/S_b at three truncation levels: p+q<=3, p+q<=4, p+q<=5.
Tests whether fermionic non-monotonicity (dS_f/dtau > 0) strengthens relative to S_b
at higher truncation, or whether bosonic dominance is structural.

Method:
  1. Use dirac_spectrum.py to compute Dirac eigenvalues for ALL sectors up to p+q=5
  2. S_b(tau) = sum_k dim(p_k,q_k)^2 * |lambda_k(tau)|^2  (bosonic = quadratic)
  3. S_f(tau) = sum_k n_k(tau) * |lambda_k(tau)|  (fermionic = BCS occupation x linear)
  4. n_k = v_k^2 = (1/2)(1 - xi_k/E_k) with xi_k = |lambda_k| - mu, E_k = sqrt(xi_k^2 + Delta^2)
  5. Track ratio S_f/S_b and sign of d(S_b+S_f)/dtau at each level

Author: Spectral-Geometer (S55)
Date: 2026-03-22
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from time import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# Add paths
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, str(_x2_shared_dir()))
from canonical_constants import tau_fold, Delta_0_OES

# Import Dirac spectrum machinery from computations/_shared
sys.path.insert(0, str(_x2_shared_dir()))
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep,
    _irrep_cache
)

# Constants
Delta = Delta_0_OES  # 0.4643 M_KK (BCS gap from S54)
mu = 0.0  # mu=0 forced (PERMANENT, S34) (local)

# Tau values for sweep — fine grid around fold
tau_values = np.array([0.00, 0.05, 0.10, 0.125, 0.15, 0.175, 0.19, 0.20, 0.22, 0.25, 0.30])

# Truncation levels
trunc_levels = [3, 4, 5]

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)"""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def casimir_pq(p, q):
    """Quadratic Casimir C_2(p,q) for SU(3)"""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def sectors_up_to(max_sum):
    """All (p,q) sectors with p+q <= max_sum, ordered by Casimir"""
    secs = []
    for p in range(max_sum + 1):
        for q in range(max_sum + 1 - p):
            secs.append((p, q, dim_pq(p, q), casimir_pq(p, q)))
    secs.sort(key=lambda x: x[3])  # sort by Casimir
    return secs

def bcs_occupation(omega, delta, mu=0.0):
    """
    BCS occupation number v_k^2 = (1/2)(1 - xi_k / E_k)
    where xi_k = |omega_k| - mu, E_k = sqrt(xi_k^2 + delta^2)
    """
    xi = np.abs(omega) - mu
    E = np.sqrt(xi**2 + delta**2)
    return 0.5 * (1.0 - xi / E)

def compute_spectrum_at_tau(tau, gens, f_abc, gammas, max_pq_sum):
    """
    Compute full Dirac spectrum at given tau for sectors up to p+q <= max_pq_sum.

    Returns:
        sector_data: list of (p, q, dim_pq, eigenvalues) for each sector
    """
    global _irrep_cache
    _irrep_cache.clear()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    sector_data = []

    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            d = dim_pq(p, q)

            if (p, q) == (0, 0):
                # Trivial irrep: D = Omega on 16-dim space
                D_trivial = Omega.copy()
                evals_raw = np.linalg.eigvals(D_trivial)
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_raw = np.linalg.eigvals(D_pi)

            # Eigenvalues should be purely imaginary (anti-Hermitian D).
            # Extract imaginary parts as the physical eigenvalues.
            imag_parts = evals_raw.imag

            # Sanity: real parts should be ~0
            max_real = np.max(np.abs(evals_raw.real))
            if max_real > 1e-8:
                print(f"  WARNING: ({p},{q}) has max real part {max_real:.2e}")

            # Use absolute values of imaginary parts (spectrum is symmetric)
            abs_omega = np.abs(imag_parts)

            sector_data.append((p, q, d, abs_omega))

    return sector_data

def spectral_actions_from_sectors(sector_data, delta, max_pq_sum_cutoff):
    """
    Compute S_b and S_f from sector data, using only sectors with p+q <= cutoff.

    S_b = sum_k dim(p,q)^2 * |lambda_k|^2  (bosonic spectral action)
    S_f = sum_k dim(p,q)^2 * n_k * |lambda_k|  (fermionic spectral action)

    Note: Each eigenvalue in sector (p,q) has Peter-Weyl multiplicity dim(p,q).
    The dim(p,q)^2 comes from: dim(p,q) copies of the sector, each with dim(p,q)*16
    eigenvalues. But in the per-sector diagonalization, we get dim(p,q)*16 eigenvalues
    per sector, each with PW multiplicity dim(p,q). So the total contribution is
    dim(p,q) * (value per eigenvalue).

    Returns:
        S_b: bosonic spectral action
        S_f: fermionic spectral action
        N_modes: total number of physical modes (counting PW multiplicity)
    """
    S_b = 0.0  # (local)
    S_f = 0.0  # (local)
    N_modes = 0  # (local)

    for (p, q, d, abs_omega) in sector_data:
        if p + q > max_pq_sum_cutoff:
            continue

        pw_mult = d  # Peter-Weyl multiplicity

        # Bosonic: sum dim^2 * |lambda|^2 (each eigenvalue counted pw_mult times)
        S_b += pw_mult * np.sum(abs_omega**2)

        # Fermionic: sum dim * n_k * |lambda| (BCS occupation)
        n_k = bcs_occupation(abs_omega, delta, mu)
        S_f += pw_mult * np.sum(n_k * abs_omega)

        N_modes += pw_mult * len(abs_omega)

    return S_b, S_f, N_modes


def main():
    t0 = time()
    print("=" * 70)
    print("S55 TRUNC-RATIO-55: Fermionic/Bosonic Spectral Action Ratio")
    print("           at Higher Truncation (p+q <= 3, 4, 5)")
    print("=" * 70)

    # Setup algebra infrastructure (done once)
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Print sector counts
    print("\nSector structure:")
    for L in trunc_levels:
        secs = sectors_up_to(L)
        total_modes = sum(d * d * 16 for (p, q, d, c2) in secs)  # wrong: d * 16 per sector, PW mult d
        total_modes_correct = sum(d * 16 for (p, q, d, c2) in secs)  # eigenvalues per sector * PW
        # Actually: each sector has d*16 eigenvalues (from D_pi matrix), PW multiplicity is d
        # So total modes = sum_sectors d * (d * 16)  ... no.
        # D_pi is (d*16) x (d*16), so d*16 eigenvalues per sector.
        # Each eigenvalue has PW mult = d.
        # Total modes counting PW: sum d * (d * 16) = sum 16 * d^2
        N = sum(16 * d**2 for (p, q, d, c2) in secs)
        n_secs = len(secs)
        print(f"  p+q <= {L}: {n_secs} sectors, {N} modes (with PW multiplicity)")
        if L == 3:
            print(f"    Sectors: {[(p,q,d) for (p,q,d,c2) in secs]}")

    # New sectors at each level
    print("\nNew sectors at p+q=4:")
    for (p, q, d, c2) in sectors_up_to(4):
        if p + q == 4:
            print(f"  ({p},{q}): dim={d}, dim^2={d**2}, C_2={c2:.3f}")

    print("\nNew sectors at p+q=5:")
    for (p, q, d, c2) in sectors_up_to(5):
        if p + q == 5:
            print(f"  ({p},{q}): dim={d}, dim^2={d**2}, C_2={c2:.3f}")

    # Main computation: spectrum at each tau, for max truncation
    max_trunc = max(trunc_levels)

    # Storage
    results = {}  # results[L] = {'S_b': array, 'S_f': array, 'N': array}
    for L in trunc_levels:
        results[L] = {'S_b': np.zeros(len(tau_values)),
                       'S_f': np.zeros(len(tau_values)),
                       'N': np.zeros(len(tau_values), dtype=int)}

    all_sector_data = {}  # all_sector_data[tau_idx] = sector_data

    for i, tau in enumerate(tau_values):
        t1 = time()
        print(f"\n--- tau = {tau:.3f} ({i+1}/{len(tau_values)}) ---")

        # Compute spectrum for all sectors up to max truncation
        sector_data = compute_spectrum_at_tau(tau, gens, f_abc, gammas, max_trunc)
        all_sector_data[i] = sector_data

        # Extract spectral actions at each truncation level
        for L in trunc_levels:
            S_b, S_f, N = spectral_actions_from_sectors(sector_data, Delta, L)
            results[L]['S_b'][i] = S_b
            results[L]['S_f'][i] = S_f
            results[L]['N'][i] = N

        dt = time() - t1
        print(f"  Time: {dt:.1f}s")
        for L in trunc_levels:
            print(f"  p+q<={L}: S_b={results[L]['S_b'][i]:.4f}, "
                  f"S_f={results[L]['S_f'][i]:.4f}, "
                  f"ratio={results[L]['S_f'][i]/results[L]['S_b'][i]:.6f}")

    # Analysis
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    # Compute derivatives (finite differences)
    for L in trunc_levels:
        S_b = results[L]['S_b']
        S_f = results[L]['S_f']
        S_tot = S_b + S_f
        ratio = S_f / S_b

        print(f"\n--- Truncation p+q <= {L} ---")
        print(f"  N_modes: {results[L]['N'][0]}")
        print(f"  tau:    {tau_values}")
        print(f"  S_b:    {S_b}")
        print(f"  S_f:    {S_f}")
        print(f"  S_tot:  {S_tot}")
        print(f"  ratio:  {ratio}")

        # Check monotonicity of S_b
        dS_b = np.diff(S_b)
        print(f"  dS_b signs: {np.sign(dS_b)}")
        S_b_monotone = np.all(dS_b >= 0) or np.all(dS_b <= 0)
        print(f"  S_b monotone: {S_b_monotone}")

        # Check sign of dS_f
        dS_f = np.diff(S_f)
        print(f"  dS_f signs: {np.sign(dS_f)}")
        S_f_has_positive = np.any(dS_f > 0)
        S_f_has_negative = np.any(dS_f < 0)
        S_f_nonmonotone = S_f_has_positive and S_f_has_negative
        print(f"  S_f non-monotone: {S_f_nonmonotone} (has positive dS_f: {S_f_has_positive})")

        # Check if total changes sign
        dS_tot = np.diff(S_tot)
        print(f"  dS_tot signs: {np.sign(dS_tot)}")
        S_tot_nonmonotone = np.any(dS_tot > 0) and np.any(dS_tot < 0)
        print(f"  S_tot non-monotone: {S_tot_nonmonotone}")

        # Find tau of S_f maximum (if non-monotone)
        if S_f_nonmonotone:
            idx_max = np.argmax(S_f)
            print(f"  S_f maximum at tau={tau_values[idx_max]:.3f}, S_f_max={S_f[idx_max]:.6f}")
            idx_min = np.argmin(S_f)
            print(f"  S_f minimum at tau={tau_values[idx_min]:.3f}, S_f_min={S_f[idx_min]:.6f}")

    # Key diagnostic: ratio S_f/S_b trend with truncation
    print("\n--- Ratio S_f/S_b vs Truncation (at fold tau=0.19) ---")
    idx_fold = np.argmin(np.abs(tau_values - tau_fold))
    for L in trunc_levels:
        r = results[L]['S_f'][idx_fold] / results[L]['S_b'][idx_fold]
        print(f"  p+q<={L}: S_f/S_b = {r:.6f}")

    # Ratio at multiple tau values
    print("\n--- Ratio S_f/S_b table ---")
    print(f"  {'tau':>6s}", end="")
    for L in trunc_levels:
        print(f"  {'pq<=' + str(L):>10s}", end="")
    print()
    for i, tau in enumerate(tau_values):
        print(f"  {tau:6.3f}", end="")
        for L in trunc_levels:
            r = results[L]['S_f'][i] / results[L]['S_b'][i]
            print(f"  {r:10.6f}", end="")
        print()

    # Compute the derivative dS_f/dtau at the fold region for each truncation
    print("\n--- dS_f/dtau at fold region ---")
    # Use centered differences where possible
    for L in trunc_levels:
        S_f = results[L]['S_f']
        # Near fold: tau=0.15 to tau=0.19
        idx_pre = np.argmin(np.abs(tau_values - 0.10))
        idx_mid = np.argmin(np.abs(tau_values - 0.15))
        idx_post = np.argmin(np.abs(tau_values - 0.19))

        # Forward difference at mid
        if idx_mid + 1 < len(tau_values):
            dSf_dtau = (S_f[idx_mid + 1] - S_f[idx_mid]) / (tau_values[idx_mid + 1] - tau_values[idx_mid])
            print(f"  p+q<={L}: dS_f/dtau at tau~{tau_values[idx_mid]:.2f} = {dSf_dtau:.4f}")

    # Key question: does dS_f/dtau > 0 strengthen relative to S_b at higher truncation?
    # Compute |dS_f/dtau| / |dS_b/dtau| at the fold region
    print("\n--- |dS_f/dtau| / |dS_b/dtau| at fold ---")
    for L in trunc_levels:
        S_f = results[L]['S_f']
        S_b = results[L]['S_b']
        idx = np.argmin(np.abs(tau_values - 0.125))
        if idx + 1 < len(tau_values):
            dSf = (S_f[idx + 1] - S_f[idx]) / (tau_values[idx + 1] - tau_values[idx])
            dSb = (S_b[idx + 1] - S_b[idx]) / (tau_values[idx + 1] - tau_values[idx])
            if abs(dSb) > 0:
                ratio_deriv = abs(dSf) / abs(dSb)
                print(f"  p+q<={L}: |dS_f/dtau|/|dS_b/dtau| = {ratio_deriv:.6f}")
                print(f"    dS_f/dtau = {dSf:.4f}, dS_b/dtau = {dSb:.4f}")

    # Weyl law check: S_b ~ N^{1+2/d} for d=8
    print("\n--- Weyl scaling check ---")
    for i in range(len(trunc_levels) - 1):
        L1, L2 = trunc_levels[i], trunc_levels[i+1]
        N1 = results[L1]['N'][0]
        N2 = results[L2]['N'][0]
        Sb1 = results[L1]['S_b'][0]
        Sb2 = results[L2]['S_b'][0]
        Sf1 = results[L1]['S_f'][0]
        Sf2 = results[L2]['S_f'][0]

        # log ratio
        if N1 > 0 and N2 > 0 and Sb1 > 0 and Sb2 > 0:
            alpha_b = np.log(Sb2 / Sb1) / np.log(N2 / N1)
            alpha_f = np.log(Sf2 / Sf1) / np.log(N2 / N1)
            print(f"  L={L1}->{L2}: N ratio={N2/N1:.2f}, "
                  f"S_b scaling exponent={alpha_b:.3f}, S_f scaling exponent={alpha_f:.3f}")

    # =========================================================================
    # Save results
    # =========================================================================
    save_dict = {
        'tau_values': tau_values,
        'trunc_levels': np.array(trunc_levels),
        'Delta': Delta,
        'mu': mu,
        'tau_fold': tau_fold,
    }

    for L in trunc_levels:
        save_dict[f'S_b_L{L}'] = results[L]['S_b']
        save_dict[f'S_f_L{L}'] = results[L]['S_f']
        save_dict[f'N_L{L}'] = results[L]['N']

    # Save per-sector breakdown at fold for detailed analysis
    idx_fold_data = np.argmin(np.abs(tau_values - tau_fold))
    fold_sector_data = all_sector_data[idx_fold_data]
    sector_S_b_at_fold = []
    sector_S_f_at_fold = []
    sector_labels = []
    for (p, q, d, abs_omega) in fold_sector_data:
        pw = d
        sb_sector = pw * np.sum(abs_omega**2)
        nk = bcs_occupation(abs_omega, Delta, mu)
        sf_sector = pw * np.sum(nk * abs_omega)
        sector_S_b_at_fold.append(sb_sector)
        sector_S_f_at_fold.append(sf_sector)
        sector_labels.append(f"({p},{q})")

    save_dict['fold_sector_S_b'] = np.array(sector_S_b_at_fold)
    save_dict['fold_sector_S_f'] = np.array(sector_S_f_at_fold)
    save_dict['fold_sector_labels'] = np.array(sector_labels)

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's55_trunc_ratio.npz')
    np.savez(outpath, **save_dict)
    print(f"\nSaved: {outpath}")

    # =========================================================================
    # Plot
    # =========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('TRUNC-RATIO-55: Fermionic/Bosonic Spectral Action at Higher Truncation',
                 fontsize=14, fontweight='bold')

    colors = {3: 'C0', 4: 'C1', 5: 'C2'}

    # Row 1: S_b, S_f, S_tot vs tau at each truncation
    ax = axes[0, 0]
    for L in trunc_levels:
        ax.plot(tau_values, results[L]['S_b'], 'o-', color=colors[L], label=f'p+q<={L}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_b(\tau)$')
    ax.set_title(r'Bosonic $S_b$ vs $\tau$')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    for L in trunc_levels:
        ax.plot(tau_values, results[L]['S_f'], 's-', color=colors[L], label=f'p+q<={L}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_f(\tau)$')
    ax.set_title(r'Fermionic $S_f$ vs $\tau$')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[0, 2]
    for L in trunc_levels:
        S_tot = results[L]['S_b'] + results[L]['S_f']
        ax.plot(tau_values, S_tot, 'd-', color=colors[L], label=f'p+q<={L}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_b + S_f$')
    ax.set_title(r'Total $S_b + S_f$ vs $\tau$')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Row 2: ratio, derivative comparison, sector breakdown
    ax = axes[1, 0]
    for L in trunc_levels:
        ratio = results[L]['S_f'] / results[L]['S_b']
        ax.plot(tau_values, ratio, 'o-', color=colors[L], label=f'p+q<={L}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_f / S_b$')
    ax.set_title(r'Ratio $S_f / S_b$ vs $\tau$')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # dS_f/dtau normalized by S_b for each truncation
    ax = axes[1, 1]
    for L in trunc_levels:
        S_f = results[L]['S_f']
        S_b = results[L]['S_b']
        dtau = np.diff(tau_values)
        dSf = np.diff(S_f) / dtau
        dSb = np.diff(S_b) / dtau
        tau_mid = 0.5 * (tau_values[:-1] + tau_values[1:])
        # Ratio of derivatives
        ax.plot(tau_mid, dSf / np.abs(dSb), 'o-', color=colors[L], label=f'p+q<={L}')
    ax.axhline(0, color='k', ls='-', alpha=0.3)
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$(dS_f/d\tau) / |dS_b/d\tau|$')
    ax.set_title(r'Derivative ratio: $dS_f$ vs $|dS_b|$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Sector breakdown at fold
    ax = axes[1, 2]
    x_pos = np.arange(len(sector_labels))
    bar_width = 0.35  # (local)
    ax.bar(x_pos - bar_width/2, sector_S_b_at_fold, bar_width,
           label=r'$S_b$ (sector)', color='steelblue', alpha=0.7)
    ax.bar(x_pos + bar_width/2, sector_S_f_at_fold, bar_width,
           label=r'$S_f$ (sector)', color='coral', alpha=0.7)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(sector_labels, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel('Spectral action contribution')
    ax.set_title(rf'Per-sector breakdown at $\tau={tau_fold}$')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plotpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's55_trunc_ratio.png')
    plt.savefig(plotpath, dpi=150, bbox_inches='tight')
    print(f"Saved: {plotpath}")
    plt.close()

    # =========================================================================
    # Gate verdict
    # =========================================================================
    print("\n" + "=" * 70)
    print("GATE: TRUNC-RATIO-55")
    print("=" * 70)

    # Key question: does d(S_b + S_f)/dtau change sign at higher truncation?
    total_nonmonotone = {}
    for L in trunc_levels:
        dS = np.diff(results[L]['S_b'] + results[L]['S_f'])
        total_nonmonotone[L] = np.any(dS > 0) and np.any(dS < 0)

    # Does S_f/S_b grow with truncation?
    ratio_at_fold = {L: results[L]['S_f'][idx_fold] / results[L]['S_b'][idx_fold]
                     for L in trunc_levels}
    ratio_growing = ratio_at_fold[5] > ratio_at_fold[3]

    print(f"  S_f/S_b at fold: {ratio_at_fold}")
    print(f"  Ratio growing with truncation: {ratio_growing}")
    print(f"  Total non-monotone: {total_nonmonotone}")

    if any(total_nonmonotone.values()):
        print(f"  VERDICT: INFO — d(S_b+S_f)/dtau changes sign at truncation level(s): "
              f"{[L for L, v in total_nonmonotone.items() if v]}")
    else:
        if ratio_growing:
            print(f"  VERDICT: INFO — S_f/S_b GROWS with truncation ({ratio_at_fold[3]:.6f} -> {ratio_at_fold[5]:.6f}), "
                  f"but total remains monotone. Bosonic dominance weakening.")
        else:
            print(f"  VERDICT: INFO — S_f/S_b SHRINKS with truncation ({ratio_at_fold[3]:.6f} -> {ratio_at_fold[5]:.6f}). "
                  f"Bosonic dominance structural (Weyl).")

    total_time = time() - t0
    print(f"\nTotal runtime: {total_time:.1f}s")
    print("DONE.")

if __name__ == '__main__':
    main()
