#!/usr/bin/env python3
"""
CRYSTAL-SPEC-42: Dirac Spectrum at Low Tau — Gatekeeper Computation
====================================================================

Computes the D_K eigenvalues on Jensen-deformed SU(3) at fine tau resolution
in the low-tau regime [0.01, 0.15], where the existing data gap lies.

Hypothesis: If tau overshoots past the BCS fold (tau ~ 0.19) toward tau ~ 0,
it could hit a SECOND spectral threshold — a second Van Hove singularity,
gap closure, or inter-sector eigenvalue crossing — that breaks the GGE's
integrability protection and "crystallizes" matter.

Evidence motivating this computation:
    Berry curvature B = 982.5 at tau = 0.10 (1000x above baseline, from S24).

Mathematical setup:
    D_pi = sum_{a,b} E_{ab} (rho_pi(X_b) tensor gamma_a) + I_{dim_pi} tensor Omega
    where E is the orthonormal frame for the Jensen metric g_s with parameter s=tau.

    We use max_pq_sum = 3, giving 10 Peter-Weyl sectors:
    (0,0), (1,0), (0,1), (2,0), (0,2), (1,1), (3,0), (0,3), (2,1), (1,2)
    Total eigenvalues per tau: 1232

Pre-registered gate criteria:
    1. Van Hove singularity: eigenvalue spacing < 0.005 for 3+ levels at any tau in [0.01, 0.10]
    2. Gap closure: min |lambda| < 0.1 in any sector
    3. Inter-sector crossing: sign change in (lambda_i^A - lambda_j^B) between sectors
    4. Berry curvature: B(tau) peak > 500 in the full multi-sector spectrum

Output: tier0-computation/s42_crystal_spec.npz, s42_crystal_spec.png

Author: Gen-Physicist (Session 42)
Date: 2026-03-13
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    validate_connection,
    dirac_operator_on_irrep,
    get_irrep,
)

# ─────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────

# Fine sampling in the low-tau regime + reference points at higher tau
TAU_VALUES = np.array([
    0.01, 0.02, 0.03, 0.04, 0.05,
    0.06, 0.07, 0.08, 0.09, 0.10,
    0.12, 0.15
])

MAX_PQ_SUM = 3  # 10 sectors

# Gate thresholds
VH_SPACING_THRESHOLD = 0.005   # Van Hove: spacing below this
VH_MIN_LEVELS = 3              # Van Hove: at least this many near-crossings
GAP_CLOSURE_THRESHOLD = 0.1    # Gap closure: min |lambda| below this
BERRY_PEAK_THRESHOLD = 500.0   # Berry curvature peak above this

# Near-crossing definition for counting
NEAR_CROSSING_THRESHOLD = 0.01


def enumerate_sectors(max_pq_sum):
    """Return list of (p, q, dim_pq) for all sectors up to max_pq_sum."""
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            sectors.append((p, q, dim_pq))
    return sectors


def compute_all_sectors(tau, gens, f_abc, gammas, sectors):
    """
    Compute D_K eigenvalues and eigenvectors for all sectors at given tau.

    Returns:
        sector_results: list of dicts with 'p', 'q', 'dim_rho', 'evals', 'evecs', 'ah_err'
        infra: dict with 'E', 'Gamma', 'Omega', 'g_s'
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    infra = {'E': E, 'Gamma': Gamma, 'Omega': Omega, 'g_s': g_s}
    sector_results = []

    for p, q, dim_pq in sectors:
        if (p, q) == (0, 0):
            D_pi = Omega.copy()
        else:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq, f"Dimension mismatch for ({p},{q})"
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        H = 1j * D_pi
        evals, evecs = eigh(H)

        sector_results.append({
            'p': p, 'q': q, 'dim_rho': dim_pq,
            'evals': evals,
            'evecs': evecs,
            'ah_err': ah_err,
        })

    return sector_results, infra


def collect_all_eigenvalues(sector_results):
    """Concatenate all eigenvalues from all sectors, with sector labels."""
    all_evals = []
    all_labels = []
    for sr in sector_results:
        all_evals.extend(sr['evals'])
        all_labels.extend([(sr['p'], sr['q'])] * len(sr['evals']))
    return np.array(all_evals), all_labels


def compute_spacing_stats(evals_sorted):
    """
    Compute eigenvalue spacing statistics.

    Returns:
        min_spacing: minimum spacing between distinct eigenvalues
        spacings: all spacings (sorted)
        n_near: number of spacings below NEAR_CROSSING_THRESHOLD
    """
    if len(evals_sorted) < 2:
        return np.inf, np.array([]), 0
    spacings = np.diff(evals_sorted)
    # Filter out exact degeneracies (spacing < 1e-12)
    nonzero = spacings[spacings > 1e-12]
    if len(nonzero) == 0:
        return 0.0, spacings, len(spacings)
    min_spacing = np.min(nonzero)
    n_near = np.sum(nonzero < NEAR_CROSSING_THRESHOLD)
    return min_spacing, spacings, int(n_near)


def compute_berry_curvature_numerical(evals_at_taus, tau_values):
    """
    Compute Berry curvature B(tau) = sum_n |d E_n / d tau|^2
    using finite differences on the eigenvalue trajectories.

    This is the adiabatic metric (quantum metric tensor component g_{tau,tau})
    summed over all levels. It diverges near avoided crossings.

    For eigenvalue-only Berry curvature (no eigenvector phases needed):
        B(tau) = sum_n (dE_n/dtau)^2

    This is a lower bound on the full quantum geometric tensor but captures
    the essential Van Hove singularity signal.

    Args:
        evals_at_taus: (n_tau, n_evals) array of sorted eigenvalues at each tau
        tau_values: (n_tau,) array of tau values

    Returns:
        B: (n_tau,) Berry curvature at each tau
    """
    n_tau, n_evals = evals_at_taus.shape
    B = np.zeros(n_tau)

    for i in range(n_tau):
        if i == 0:
            # Forward difference
            dtau = tau_values[1] - tau_values[0]
            dE = evals_at_taus[1, :] - evals_at_taus[0, :]
        elif i == n_tau - 1:
            # Backward difference
            dtau = tau_values[-1] - tau_values[-2]
            dE = evals_at_taus[-1, :] - evals_at_taus[-2, :]
        else:
            # Central difference
            dtau = tau_values[i + 1] - tau_values[i - 1]
            dE = evals_at_taus[i + 1, :] - evals_at_taus[i - 1, :]

        B[i] = np.sum((dE / dtau) ** 2)

    return B


def find_intersector_crossings(sector_results_list, tau_values):
    """
    Check for eigenvalue crossings BETWEEN different sectors.

    For each pair of sectors (A, B) with A != B, track the difference
    lambda_i^A(tau) - lambda_j^B(tau) and look for sign changes.

    Returns:
        crossings: list of dicts describing each crossing found
    """
    n_tau = len(tau_values)
    n_sectors = len(sector_results_list[0])
    crossings = []

    # For each tau, collect sorted eigenvalues per sector
    for si in range(n_sectors):
        for sj in range(si + 1, n_sectors):
            p_i, q_i = sector_results_list[0][si]['p'], sector_results_list[0][si]['q']
            p_j, q_j = sector_results_list[0][sj]['p'], sector_results_list[0][sj]['q']

            # Get eigenvalue arrays for both sectors at all tau
            evals_i = np.array([sector_results_list[t][si]['evals'] for t in range(n_tau)])
            evals_j = np.array([sector_results_list[t][sj]['evals'] for t in range(n_tau)])

            # Check all pairs of eigenvalue indices
            n_i = evals_i.shape[1]
            n_j = evals_j.shape[1]

            # For efficiency, only check eigenvalues that are close at ANY tau
            for ki in range(n_i):
                for kj in range(n_j):
                    diff = evals_i[:, ki] - evals_j[:, kj]
                    # Look for sign changes
                    sign_changes = np.where(np.diff(np.sign(diff)))[0]
                    for sc_idx in sign_changes:
                        crossings.append({
                            'sector_A': (p_i, q_i),
                            'sector_B': (p_j, q_j),
                            'idx_A': ki,
                            'idx_B': kj,
                            'tau_range': (tau_values[sc_idx], tau_values[sc_idx + 1]),
                            'diff_before': diff[sc_idx],
                            'diff_after': diff[sc_idx + 1],
                        })

    return crossings


def main():
    print("=" * 70)
    print("CRYSTAL-SPEC-42: Dirac Spectrum at Low Tau")
    print("Gatekeeper Computation for Supersaturation-Crystallization Hypothesis")
    print("=" * 70)
    print(f"Tau values: {TAU_VALUES}")
    print(f"Max p+q: {MAX_PQ_SUM} (10 sectors)")
    print()

    # ─────────────────────────────────────────────────────────────
    # Initialize infrastructure
    # ─────────────────────────────────────────────────────────────
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    sectors = enumerate_sectors(MAX_PQ_SUM)
    print(f"Sectors: {[(p,q) for p,q,d in sectors]}")
    print(f"Total eigenvalues per tau: {sum(d*16 for p,q,d in sectors)}")
    print()

    # ─────────────────────────────────────────────────────────────
    # STEP 1: Compute spectra at all tau values
    # ─────────────────────────────────────────────────────────────
    print("=" * 70)
    print("STEP 1: COMPUTE SPECTRA AT ALL TAU VALUES")
    print("=" * 70)

    all_sector_results = []  # [tau_idx][sector_idx] = sector dict
    all_infras = []
    all_evals_sorted = []    # sorted concatenated eigenvalues at each tau
    all_evals_labels = []    # sector labels for each eigenvalue
    per_sector_evals = {}    # per_sector_evals[(p,q)] = list of evals arrays over tau

    for p, q, d in sectors:
        per_sector_evals[(p, q)] = []

    t_total = time.time()

    for tau_idx, tau in enumerate(TAU_VALUES):
        t0 = time.time()
        sector_results, infra = compute_all_sectors(tau, gens, f_abc, gammas, sectors)
        all_sector_results.append(sector_results)
        all_infras.append(infra)

        evals_concat, labels = collect_all_eigenvalues(sector_results)
        sorted_idx = np.argsort(evals_concat)
        evals_sorted = evals_concat[sorted_idx]
        all_evals_sorted.append(evals_sorted)
        all_evals_labels.append([labels[i] for i in sorted_idx])

        for sr in sector_results:
            per_sector_evals[(sr['p'], sr['q'])].append(sr['evals'])

        # Quick stats
        min_abs = np.min(np.abs(evals_sorted))
        max_abs = np.max(np.abs(evals_sorted))
        min_spacing, spacings, n_near = compute_spacing_stats(evals_sorted)
        max_ah = max(sr['ah_err'] for sr in sector_results)

        dt = time.time() - t0
        print(f"  tau={tau:.3f}: {len(evals_sorted)} evals, "
              f"|lambda| in [{min_abs:.6f}, {max_abs:.4f}], "
              f"min_spacing={min_spacing:.6f}, n_near(<{NEAR_CROSSING_THRESHOLD})={n_near}, "
              f"max_ah_err={max_ah:.2e}, time={dt:.2f}s")

    total_time = time.time() - t_total
    print(f"\nTotal computation time: {total_time:.1f}s")

    # Convert to array for Berry curvature
    n_evals = len(all_evals_sorted[0])
    evals_matrix = np.array(all_evals_sorted)  # (n_tau, n_evals)
    assert evals_matrix.shape == (len(TAU_VALUES), n_evals)

    # ─────────────────────────────────────────────────────────────
    # STEP 2: SPACING ANALYSIS (Van Hove test)
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 2: EIGENVALUE SPACING ANALYSIS")
    print("=" * 70)

    vh_pass = False
    spacing_data = []

    for tau_idx, tau in enumerate(TAU_VALUES):
        evals = all_evals_sorted[tau_idx]
        min_sp, spacings, n_near = compute_spacing_stats(evals)
        n_very_close = int(np.sum(spacings[(spacings > 1e-12)] < VH_SPACING_THRESHOLD)) if len(spacings) > 0 else 0
        spacing_data.append({
            'tau': tau,
            'min_spacing': min_sp,
            'n_near': n_near,
            'n_very_close': n_very_close,
        })
        print(f"  tau={tau:.3f}: min_spacing={min_sp:.6f}, "
              f"n(spacing<{NEAR_CROSSING_THRESHOLD})={n_near}, "
              f"n(spacing<{VH_SPACING_THRESHOLD})={n_very_close}")

        if tau <= 0.10 and n_very_close >= VH_MIN_LEVELS:
            vh_pass = True

    print(f"\n  Van Hove gate (spacing < {VH_SPACING_THRESHOLD} for {VH_MIN_LEVELS}+ levels "
          f"at tau <= 0.10): {'PASS' if vh_pass else 'FAIL'}")

    # ─────────────────────────────────────────────────────────────
    # STEP 3: GAP CLOSURE TEST
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 3: GAP CLOSURE TEST")
    print("=" * 70)

    gap_closure = False
    min_gap_data = []

    for tau_idx, tau in enumerate(TAU_VALUES):
        for sr in all_sector_results[tau_idx]:
            min_abs = np.min(np.abs(sr['evals']))
            if min_abs < GAP_CLOSURE_THRESHOLD:
                gap_closure = True
                print(f"  *** GAP CLOSURE at tau={tau:.3f} in sector ({sr['p']},{sr['q']}): "
                      f"min|lambda| = {min_abs:.8f}")
        # Overall minimum
        evals = all_evals_sorted[tau_idx]
        overall_min = np.min(np.abs(evals))
        min_gap_data.append(overall_min)
        print(f"  tau={tau:.3f}: overall min|lambda| = {overall_min:.8f}")

    min_gap_array = np.array(min_gap_data)
    print(f"\n  Gap closure gate (min|lambda| < {GAP_CLOSURE_THRESHOLD} in any sector): "
          f"{'PASS' if gap_closure else 'FAIL'}")
    print(f"  Global minimum |lambda|: {np.min(min_gap_array):.8f} at tau={TAU_VALUES[np.argmin(min_gap_array)]:.3f}")

    # ─────────────────────────────────────────────────────────────
    # STEP 4: INTER-SECTOR CROSSING TEST
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 4: INTER-SECTOR EIGENVALUE CROSSING TEST")
    print("=" * 70)

    crossings = find_intersector_crossings(all_sector_results, TAU_VALUES)

    if crossings:
        print(f"  Found {len(crossings)} inter-sector crossings:")
        # Group by sector pair
        crossing_pairs = {}
        for c in crossings:
            key = (c['sector_A'], c['sector_B'])
            if key not in crossing_pairs:
                crossing_pairs[key] = []
            crossing_pairs[key].append(c)

        for key, clist in sorted(crossing_pairs.items()):
            print(f"    {key[0]} x {key[1]}: {len(clist)} crossings")
            # Show a few examples
            for c in clist[:3]:
                print(f"      tau in [{c['tau_range'][0]:.3f}, {c['tau_range'][1]:.3f}], "
                      f"diff: {c['diff_before']:+.6f} -> {c['diff_after']:+.6f}")
    else:
        print("  NO inter-sector crossings found.")

    crossing_pass = len(crossings) > 0
    print(f"\n  Inter-sector crossing gate: {'PASS' if crossing_pass else 'FAIL'}")

    # ─────────────────────────────────────────────────────────────
    # STEP 5: BERRY CURVATURE
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 5: BERRY CURVATURE (ADIABATIC METRIC)")
    print("=" * 70)

    B_tau = compute_berry_curvature_numerical(evals_matrix, TAU_VALUES)

    berry_pass = False
    for tau_idx, tau in enumerate(TAU_VALUES):
        print(f"  tau={tau:.3f}: B = {B_tau[tau_idx]:.2f}")
        if B_tau[tau_idx] > BERRY_PEAK_THRESHOLD:
            berry_pass = True

    B_max = np.max(B_tau)
    B_max_tau = TAU_VALUES[np.argmax(B_tau)]
    print(f"\n  Berry curvature peak: B = {B_max:.2f} at tau = {B_max_tau:.3f}")
    print(f"  Berry curvature gate (peak > {BERRY_PEAK_THRESHOLD}): "
          f"{'PASS' if berry_pass else 'FAIL'}")

    # Also compute per-sector Berry curvature for diagnostics
    print("\n  Per-sector Berry curvature peaks:")
    sector_berry = {}
    for p, q, d in sectors:
        ev_arr = np.array(per_sector_evals[(p, q)])  # (n_tau, n_evals_in_sector)
        B_s = compute_berry_curvature_numerical(ev_arr, TAU_VALUES)
        sector_berry[(p, q)] = B_s
        peak = np.max(B_s)
        peak_tau = TAU_VALUES[np.argmax(B_s)]
        print(f"    ({p},{q}): B_max = {peak:.2f} at tau = {peak_tau:.3f}")

    # ─────────────────────────────────────────────────────────────
    # STEP 6: DENSITY OF STATES COMPARISON
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 6: DENSITY OF STATES: tau=0.05 vs tau=0.15")
    print("=" * 70)

    idx_005 = np.argmin(np.abs(TAU_VALUES - 0.05))
    idx_015 = np.argmin(np.abs(TAU_VALUES - 0.15))

    evals_005 = all_evals_sorted[idx_005]
    evals_015 = all_evals_sorted[idx_015]

    # Use positive eigenvalues only (spectrum is +/- symmetric)
    pos_005 = evals_005[evals_005 > 1e-10]
    pos_015 = evals_015[evals_015 > 1e-10]

    print(f"  tau={TAU_VALUES[idx_005]:.3f}: {len(pos_005)} positive eigenvalues, "
          f"range [{pos_005[0]:.4f}, {pos_005[-1]:.4f}]")
    print(f"  tau={TAU_VALUES[idx_015]:.3f}: {len(pos_015)} positive eigenvalues, "
          f"range [{pos_015[0]:.4f}, {pos_015[-1]:.4f}]")

    # ─────────────────────────────────────────────────────────────
    # STEP 7: DETAILED SECTOR-BY-SECTOR MINIMUM EIGENVALUE
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("STEP 7: SECTOR-BY-SECTOR MINIMUM |EIGENVALUE| vs TAU")
    print("=" * 70)

    header = f"{'tau':>6s}"
    for p, q, d in sectors:
        header += f"  ({p},{q}){' '*(6-len(f'({p},{q})'))}"
    print(header)

    for tau_idx, tau in enumerate(TAU_VALUES):
        row = f"{tau:6.3f}"
        for sr in all_sector_results[tau_idx]:
            min_abs = np.min(np.abs(sr['evals']))
            row += f"  {min_abs:8.5f}"
        print(row)

    # ─────────────────────────────────────────────────────────────
    # SAVE DATA
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("SAVING DATA")
    print("=" * 70)

    save_data = {
        'tau_values': TAU_VALUES,
        'evals_matrix': evals_matrix,
        'min_gap_array': min_gap_array,
        'berry_curvature': B_tau,
    }

    # Save per-sector eigenvalues at each tau
    for p, q, d in sectors:
        key = f'evals_{p}_{q}'
        save_data[key] = np.array(per_sector_evals[(p, q)])

    # Save per-sector Berry curvature
    for p, q, d in sectors:
        key = f'berry_{p}_{q}'
        save_data[key] = sector_berry[(p, q)]

    # Save spacing data
    save_data['min_spacings'] = np.array([sd['min_spacing'] for sd in spacing_data])
    save_data['n_near_crossings'] = np.array([sd['n_near'] for sd in spacing_data])
    save_data['n_very_close'] = np.array([sd['n_very_close'] for sd in spacing_data])

    # Save gate verdicts
    save_data['vh_pass'] = np.array([vh_pass])
    save_data['gap_closure_pass'] = np.array([gap_closure])
    save_data['crossing_pass'] = np.array([crossing_pass])
    save_data['berry_pass'] = np.array([berry_pass])
    save_data['n_crossings'] = np.array([len(crossings)])

    output_path = os.path.join(SCRIPT_DIR, "s42_crystal_spec.npz")
    np.savez_compressed(output_path, **save_data)
    print(f"Data saved: {output_path}")

    # ─────────────────────────────────────────────────────────────
    # PLOT
    # ─────────────────────────────────────────────────────────────
    print("\nGenerating diagnostic plot...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # ── Panel 1: Eigenvalue trajectories (spaghetti plot) ──
    ax = axes[0, 0]
    cmap = plt.cm.tab10
    sector_list = [(p, q) for p, q, d in sectors]
    for si, (p, q, d) in enumerate(sectors):
        ev_arr = np.array(per_sector_evals[(p, q)])  # (n_tau, n_evals)
        color = cmap(si / len(sectors))
        for k in range(ev_arr.shape[1]):
            lbl = f'({p},{q})' if k == 0 else None
            ax.plot(TAU_VALUES, ev_arr[:, k], '-', color=color, lw=0.5,
                    alpha=0.6, label=lbl)
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda (eigenvalues of iD_K)')
    ax.set_title('Panel 1: All Eigenvalue Trajectories lambda_k(tau)')
    ax.legend(fontsize=6, ncol=2, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5)

    # ── Panel 2: Minimum eigenvalue spacing vs tau ──
    ax = axes[0, 1]
    min_sps = np.array([sd['min_spacing'] for sd in spacing_data])
    n_nears = np.array([sd['n_near'] for sd in spacing_data])
    n_vclose = np.array([sd['n_very_close'] for sd in spacing_data])

    ax.semilogy(TAU_VALUES, min_sps, 'o-', color='C0', lw=2, label='min spacing')
    ax.axhline(VH_SPACING_THRESHOLD, color='red', ls='--', alpha=0.7,
               label=f'VH threshold = {VH_SPACING_THRESHOLD}')
    ax.axhline(NEAR_CROSSING_THRESHOLD, color='orange', ls=':', alpha=0.7,
               label=f'near-crossing = {NEAR_CROSSING_THRESHOLD}')
    ax.set_xlabel('tau')
    ax.set_ylabel('minimum eigenvalue spacing')
    ax.set_title('Panel 2: Min Eigenvalue Spacing vs tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Add secondary axis for near-crossing count
    ax2 = ax.twinx()
    ax2.bar(TAU_VALUES, n_nears, width=0.006, alpha=0.3, color='C1',
            label=f'n(spacing < {NEAR_CROSSING_THRESHOLD})')
    ax2.set_ylabel('near-crossing count', color='C1')
    ax2.tick_params(axis='y', labelcolor='C1')

    # ── Panel 3: Berry curvature vs tau ──
    ax = axes[1, 0]
    ax.plot(TAU_VALUES, B_tau, 'o-', color='C0', lw=2, ms=6, label='Total B(tau)')
    ax.axhline(BERRY_PEAK_THRESHOLD, color='red', ls='--', alpha=0.7,
               label=f'threshold = {BERRY_PEAK_THRESHOLD}')

    # Show top contributing sectors
    top_sectors = sorted(sector_berry.keys(),
                         key=lambda k: np.max(sector_berry[k]), reverse=True)[:4]
    for si, key in enumerate(top_sectors):
        ax.plot(TAU_VALUES, sector_berry[key], '--', color=cmap(si + 1),
                lw=1, alpha=0.7, label=f'({key[0]},{key[1]})')

    ax.set_xlabel('tau')
    ax.set_ylabel('Berry curvature B(tau)')
    ax.set_title('Panel 3: Berry Curvature (Adiabatic Metric) vs tau')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # ── Panel 4: DOS histogram comparison ──
    ax = axes[1, 1]
    # Use absolute values of eigenvalues
    abs_005 = np.abs(evals_005)
    abs_015 = np.abs(evals_015)

    bins = np.linspace(0, max(np.max(abs_005), np.max(abs_015)) * 1.05, 50)
    ax.hist(abs_005, bins=bins, alpha=0.5, color='C0', density=True,
            label=f'tau={TAU_VALUES[idx_005]:.2f}')
    ax.hist(abs_015, bins=bins, alpha=0.5, color='C1', density=True,
            label=f'tau={TAU_VALUES[idx_015]:.2f}')
    ax.set_xlabel('|lambda|')
    ax.set_ylabel('density')
    ax.set_title('Panel 4: DOS Comparison tau=0.05 vs tau=0.15')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Overall title with gate verdicts
    verdict_str = (f"VH: {'PASS' if vh_pass else 'FAIL'} | "
                   f"Gap: {'PASS' if gap_closure else 'FAIL'} | "
                   f"Crossing: {'PASS' if crossing_pass else 'FAIL'} | "
                   f"Berry: {'PASS' if berry_pass else 'FAIL'}")
    fig.suptitle(f'CRYSTAL-SPEC-42: Low-Tau Dirac Spectrum\n{verdict_str}',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()

    plot_path = os.path.join(SCRIPT_DIR, "s42_crystal_spec.png")
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"Plot saved: {plot_path}")

    # ─────────────────────────────────────────────────────────────
    # FINAL GATE EVALUATION
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("FINAL GATE EVALUATION: CRYSTAL-SPEC-42")
    print("=" * 70)

    gates = [
        ("Van Hove singularity", vh_pass,
         f"spacing < {VH_SPACING_THRESHOLD} for {VH_MIN_LEVELS}+ levels at tau <= 0.10"),
        ("Gap closure", gap_closure,
         f"min|lambda| < {GAP_CLOSURE_THRESHOLD} in any sector"),
        ("Inter-sector crossing", crossing_pass,
         f"sign change in lambda_i^A - lambda_j^B between sectors"),
        ("Berry curvature peak", berry_pass,
         f"B(tau) > {BERRY_PEAK_THRESHOLD} in multi-sector spectrum"),
    ]

    any_pass = False
    for name, passed, criterion in gates:
        status = "PASS" if passed else "FAIL"
        any_pass = any_pass or passed
        print(f"  [{status}] {name}: {criterion}")

    print(f"\n  Overall: {'At least one gate PASSED' if any_pass else 'ALL GATES FAILED'}")

    if any_pass:
        print(f"\n  INTERPRETATION: Spectral fine structure EXISTS in the overshoot regime.")
        print(f"  The supersaturation-crystallization hypothesis has spectral support.")
        print(f"  Further investigation warranted: BdG analysis at the crossing/singularity points.")
    else:
        print(f"\n  INTERPRETATION: The low-tau spectrum is spectrally smooth.")
        print(f"  No Van Hove singularity, gap closure, or crossing detected.")
        print(f"  The GGE's integrability protection appears robust in this regime.")
        print(f"  The crystallization hypothesis lacks spectral support.")

    print(f"\n  Key numbers:")
    print(f"    Global min spacing: {np.min(min_sps):.8f} at tau={TAU_VALUES[np.argmin(min_sps)]:.3f}")
    print(f"    Global min |lambda|: {np.min(min_gap_array):.8f} at tau={TAU_VALUES[np.argmin(min_gap_array)]:.3f}")
    print(f"    Berry curvature peak: {B_max:.2f} at tau={B_max_tau:.3f}")
    print(f"    Inter-sector crossings: {len(crossings)}")

    return {
        'vh_pass': vh_pass,
        'gap_closure': gap_closure,
        'crossing_pass': crossing_pass,
        'berry_pass': berry_pass,
        'any_pass': any_pass,
    }


if __name__ == "__main__":
    results = main()
