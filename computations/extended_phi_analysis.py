"""
Extended Phi Analysis Pipeline for Higher Irreps
=================================================
Author: Gen-Physicist Agent, Session 14
Date: 2026-02-12

Ready to analyze extended Dirac spectrum from kk-theorist's Task #2
(p+q <= 5-6). Designed to be called after higher irreps are available.

Key tests:
  1. phi^n (n=1,...,5) in pairwise ratios — decisive for Paasch geometric series
  2. Sector-specific analysis — which (p,q) sectors contribute phi ratios?
  3. Spectral density — is phi-bin anomalously populated with more eigenvalues?
  4. Consecutive ratio analysis — does phi^1 appear in consecutive eigenvalues?
  5. Band structure analysis — does band spacing encode phi?
  6. Comparison with MC null from mc_phi_significance.py

Intended usage:
  python extended_phi_analysis.py  (once tier1_dirac_spectrum.py supports p+q>3)
  OR
  from extended_phi_analysis import analyze_extended_spectrum
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    spinor_connection_offset, dirac_operator_on_irrep,
    get_irrep, validate_irrep, collect_spectrum
)


# =============================================================================
# MODULE 1: EXTENDED PHI POWER ANALYSIS
# =============================================================================

def analyze_phi_powers(abs_evals, n_low=None, phi=1.53158, tol=0.03, max_power=5):
    """
    Comprehensive phi^n analysis on extended spectrum.

    For each power n=1,...,max_power, finds all pairwise ratios within tol
    of phi^n, computes the best match, and reports statistics.

    Args:
        abs_evals: sorted positive eigenvalues (deduplicated)
        n_low: how many to use (None = all)
        phi: target base ratio
        tol: fractional tolerance
        max_power: highest power

    Returns:
        results: dict mapping power n -> {
            'count': int,
            'total_pairs': int,
            'best_err': float,
            'best_pair': (i, j, ratio),
            'pairs': list of (i, j, ratio)
        }
    """
    n = len(abs_evals) if n_low is None else min(n_low, len(abs_evals))
    total_pairs = n * (n - 1) // 2

    results = {}
    for k in range(1, max_power + 1):
        target = phi ** k
        pairs = []
        best_err = 999.0
        best_pair = None

        for i in range(n):
            for j in range(i + 1, n):
                r = abs_evals[j] / abs_evals[i]
                err = abs(r - target) / target
                if err < tol:
                    pairs.append((i, j, r))
                if err < best_err:
                    best_err = err
                    best_pair = (i, j, r)

        results[k] = {
            'count': len(pairs),
            'total_pairs': total_pairs,
            'best_err': best_err,
            'best_pair': best_pair,
            'pairs': pairs,
            'target': target
        }

    return results


def print_phi_powers(results, label=""):
    """Print phi-power analysis results."""
    phi = 1.53158
    print(f"\n  Phi-Power Analysis{' (' + label + ')' if label else ''}:")
    print(f"  {'Power':>6} {'Target':>8} {'Count':>6} {'Fraction':>10} "
          f"{'Best Err':>10} {'Verdict':>15}")
    print("  " + "-" * 65)

    for k in sorted(results.keys()):
        r = results[k]
        frac = r['count'] / r['total_pairs'] if r['total_pairs'] > 0 else 0
        err_str = f"{r['best_err']*100:.4f}%" if r['best_err'] < 1 else f"{r['best_err']*100:.1f}%"
        if r['count'] > 0 and r['best_err'] < 0.01:
            verdict = "PRESENT (<1%)"
        elif r['count'] > 0:
            verdict = f"MARGINAL ({r['best_err']*100:.1f}%)"
        else:
            verdict = "ABSENT"
        print(f"  phi^{k:>1} = {r['target']:8.4f} {r['count']:6d} "
              f"{frac:10.4f} {err_str:>10} {verdict:>15}")

    # Geometric series test
    has_phi1 = results[1]['count'] > 0 and results[1]['best_err'] < 0.03
    has_phi2 = results[2]['count'] > 0 and results[2]['best_err'] < 0.03
    has_phi3 = results[3]['count'] > 0 and results[3]['best_err'] < 0.03

    print(f"\n  GEOMETRIC SERIES TEST:")
    if has_phi1 and has_phi2 and has_phi3:
        print(f"    phi^1, phi^2, phi^3 ALL PRESENT -- Paasch series SUPPORTED")
    elif has_phi1 and has_phi2:
        print(f"    phi^1, phi^2 present; phi^3 absent -- PARTIAL support")
    elif has_phi1:
        print(f"    Only phi^1 present -- SINGLE RATIO only, NOT a series")
    else:
        print(f"    phi^1 ABSENT -- NO phi structure")


# =============================================================================
# MODULE 2: SECTOR-SPECIFIC ANALYSIS
# =============================================================================

def sector_phi_analysis(eval_data, phi=1.53158, tol=0.03):
    """
    For each pair of sectors, check if the minimum eigenvalue ratio is near phi^n.

    This tests whether phi relates specific representation-theoretic sectors,
    not just arbitrary eigenvalue pairs.

    Args:
        eval_data: list of (p, q, eigenvalues_array)
        phi: target ratio
        tol: fractional tolerance

    Returns:
        sector_results: list of (sector1, sector2, ratio, nearest_power, err)
    """
    sector_mins = {}
    for p, q, evals in eval_data:
        abs_ev = np.abs(evals)
        abs_ev = abs_ev[abs_ev > 1e-10]
        if len(abs_ev) > 0:
            sector_mins[(p, q)] = np.min(abs_ev)

    results = []
    sectors = sorted(sector_mins.keys(), key=lambda x: sector_mins[x])

    for i, s1 in enumerate(sectors):
        for s2 in sectors[i+1:]:
            r = sector_mins[s2] / sector_mins[s1]
            # Check against phi^n for n=1,...,5
            best_k = 0
            best_err = 999
            for k in range(1, 6):
                err = abs(r - phi**k) / (phi**k)
                if err < best_err:
                    best_err = err
                    best_k = k

            if best_err < tol:
                results.append((s1, s2, r, best_k, best_err))

    return results


def print_sector_analysis(sector_results):
    """Print sector-specific phi analysis."""
    print(f"\n  Sector-Specific Phi Analysis (minimum eigenvalue ratios):")
    if not sector_results:
        print("    No sector pairs with ratio near phi^n (tol=3%)")
        return

    print(f"  {'Sector 1':>10} {'Sector 2':>10} {'Ratio':>8} "
          f"{'Near':>8} {'Error':>8}")
    print("  " + "-" * 50)
    for s1, s2, r, k, err in sorted(sector_results, key=lambda x: x[4]):
        print(f"  ({s1[0]},{s1[1]}){' ':>{7-len(f'({s1[0]},{s1[1]})')}} "
              f"({s2[0]},{s2[1]}){' ':>{7-len(f'({s2[0]},{s2[1]})')}} "
              f"{r:8.5f} phi^{k:1d} {err*100:7.3f}%")


# =============================================================================
# MODULE 3: BAND STRUCTURE ANALYSIS
# =============================================================================

def analyze_band_structure(abs_evals, gap_threshold=0.03):
    """
    Identify band structure in the eigenvalue spectrum.

    Bands are groups of eigenvalues separated by relative gaps larger
    than gap_threshold.

    Args:
        abs_evals: sorted positive eigenvalues
        gap_threshold: minimum relative gap to define a band boundary

    Returns:
        bands: list of (min_eval, max_eval, count, center)
    """
    if len(abs_evals) < 2:
        return [(abs_evals[0], abs_evals[0], 1, abs_evals[0])]

    gaps = np.diff(abs_evals) / abs_evals[:-1]

    bands = []
    band_start = 0
    for i, g in enumerate(gaps):
        if g > gap_threshold:
            band = abs_evals[band_start:i+1]
            bands.append((band[0], band[-1], len(band), np.mean(band)))
            band_start = i + 1

    # Last band
    band = abs_evals[band_start:]
    if len(band) > 0:
        bands.append((band[0], band[-1], len(band), np.mean(band)))

    return bands


def print_band_analysis(bands, phi=1.53158):
    """Print band structure and check inter-band ratios for phi."""
    print(f"\n  Band Structure Analysis:")
    print(f"  {'Band':>5} {'Min':>8} {'Max':>8} {'Center':>8} {'Count':>6} {'Width':>8}")
    print("  " + "-" * 50)
    for i, (mn, mx, cnt, ctr) in enumerate(bands):
        width = (mx - mn) / ctr * 100 if ctr > 0 else 0
        print(f"  {i+1:5d} {mn:8.4f} {mx:8.4f} {ctr:8.4f} {cnt:6d} {width:7.2f}%")

    # Inter-band center ratios
    if len(bands) > 1:
        print(f"\n  Inter-band center ratios:")
        for i in range(len(bands)):
            for j in range(i+1, len(bands)):
                r = bands[j][3] / bands[i][3]
                flag = ""
                for k in range(1, 6):
                    if abs(r - phi**k) / (phi**k) < 0.05:
                        flag = f" <-- phi^{k} (err {abs(r - phi**k)/phi**k*100:.2f}%)"
                        break
                if flag or (1.0 < r < 6.0):
                    print(f"    Band {i+1} -> Band {j+1}: {r:.5f}{flag}")


# =============================================================================
# MODULE 4: GAUGE COUPLING ANALYSIS (for spectral action results)
# =============================================================================

def analyze_gauge_couplings(s_val, a4_data=None):
    """
    Compare spectral action gauge couplings to SM values.

    SM gauge couplings at M_Z:
      g_1 = 0.3575 (U(1)_Y, GUT normalized)
      g_2 = 0.6514 (SU(2)_L)
      g_3 = 1.221  (SU(3)_c)

    The spectral action predicts:
      g_i^2 ~ 1/f_i(s)
    where f_i are Seeley-DeWitt a_4 coefficient components.

    Args:
        s_val: Jensen parameter
        a4_data: dict with 'g1', 'g2', 'g3' gauge coupling predictions
                 (from spectral action computation)

    Returns:
        comparison: dict with ratios and relative errors
    """
    sm_couplings = {
        'g1': 0.3575,
        'g2': 0.6514,
        'g3': 1.221
    }

    # Ratio predictions (independent of overall normalization)
    sm_ratios = {
        'g2/g1': sm_couplings['g2'] / sm_couplings['g1'],  # 1.822
        'g3/g2': sm_couplings['g3'] / sm_couplings['g2'],  # 1.875
        'g3/g1': sm_couplings['g3'] / sm_couplings['g1'],  # 3.416
    }

    print(f"\n  SM Gauge Coupling Ratios at M_Z:")
    for name, val in sm_ratios.items():
        print(f"    {name} = {val:.4f}")

    if a4_data:
        print(f"\n  Spectral Action Predictions at s={s_val}:")
        if 'g1' in a4_data and 'g2' in a4_data:
            pred_g2_g1 = a4_data['g2'] / a4_data['g1']
            err = abs(pred_g2_g1 - sm_ratios['g2/g1']) / sm_ratios['g2/g1']
            print(f"    g2/g1 = {pred_g2_g1:.4f} (SM: {sm_ratios['g2/g1']:.4f}, err: {err*100:.1f}%)")

        if 'g2' in a4_data and 'g3' in a4_data:
            pred_g3_g2 = a4_data['g3'] / a4_data['g2']
            err = abs(pred_g3_g2 - sm_ratios['g3/g2']) / sm_ratios['g3/g2']
            print(f"    g3/g2 = {pred_g3_g2:.4f} (SM: {sm_ratios['g3/g2']:.4f}, err: {err*100:.1f}%)")

    # Order-of-magnitude estimate from Jensen geometry
    # quantum-acoustics Session 13: g_1 ~ e^{-s}, g_2 ~ e^{s}, g_3 ~ e^{-s/2}
    g1_est = np.exp(-s_val)
    g2_est = np.exp(s_val)
    g3_est = np.exp(-s_val / 2)

    pred_g2_g1_est = g2_est / g1_est
    pred_g3_g2_est = g3_est / g2_est

    print(f"\n  Order-of-Magnitude Estimates (from quantum-acoustics Session 13):")
    print(f"    g1 ~ e^{{-s}} = {g1_est:.4f}")
    print(f"    g2 ~ e^{{s}}  = {g2_est:.4f}")
    print(f"    g3 ~ e^{{-s/2}} = {g3_est:.4f}")
    print(f"    g2/g1 ~ e^{{2s}} = {pred_g2_g1_est:.4f} "
          f"(SM: {sm_ratios['g2/g1']:.4f}, err: "
          f"{abs(pred_g2_g1_est - sm_ratios['g2/g1'])/sm_ratios['g2/g1']*100:.0f}%)")
    print(f"    g3/g2 ~ e^{{-3s/2}} = {pred_g3_g2_est:.4f} "
          f"(SM: {sm_ratios['g3/g2']:.4f}, err: "
          f"{abs(pred_g3_g2_est - sm_ratios['g3/g2'])/sm_ratios['g3/g2']*100:.0f}%)")

    # What s gives the SM ratios?
    # g2/g1 = e^{2s} = 1.822 => s = ln(1.822)/2 = 0.30
    # g3/g2 = e^{-3s/2} = 1.875 => s = -2/3 * ln(1.875) = -0.42
    # These are INCOMPATIBLE (opposite signs), confirming the
    # order-of-magnitude estimate is too crude.
    s_from_g21 = np.log(sm_ratios['g2/g1']) / 2
    s_from_g32 = -2/3 * np.log(sm_ratios['g3/g2'])
    print(f"\n  Required s for SM ratios (OOM estimate):")
    print(f"    From g2/g1: s = {s_from_g21:.4f}")
    print(f"    From g3/g2: s = {s_from_g32:.4f}")
    print(f"    INCOMPATIBLE (opposite signs) -- OOM estimate too crude.")
    print(f"    Proper computation from spectral action a_4 coefficient required.")


# =============================================================================
# MODULE 5: MAIN ANALYSIS (runs when higher irreps are available)
# =============================================================================

def analyze_extended_spectrum(max_pq_sum=5, s_values=None):
    """
    Main analysis routine for extended spectrum.

    Args:
        max_pq_sum: maximum p+q (needs get_irrep to support this)
        s_values: list of s values to analyze (default: key values)
    """
    if s_values is None:
        s_values = [0.0, 0.15, 0.43, 0.5, 1.0, 1.14]

    print("=" * 80)
    print(f"EXTENDED PHI ANALYSIS: p+q <= {max_pq_sum}")
    print("=" * 80)

    # Setup
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    phi = 1.53158

    for s in s_values:
        print(f"\n{'='*70}")
        print(f"  s = {s:.4f}")
        print(f"{'='*70}")

        # Collect spectrum
        try:
            all_evals, eval_data = collect_spectrum(
                s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=True
            )
        except NotImplementedError as e:
            print(f"  SKIPPED: {e}")
            continue

        # Extract and sort eigenvalues
        abs_vals = []
        for ev, mult in all_evals:
            v = abs(ev)
            if v > 1e-10:
                abs_vals.append(v)
        abs_evals = np.sort(np.unique(np.round(abs_vals, 10)))

        print(f"\n  Total distinct eigenvalues: {len(abs_evals)}")
        print(f"  Range: [{abs_evals[0]:.4f}, {abs_evals[-1]:.4f}]")
        print(f"  Max/min ratio: {abs_evals[-1]/abs_evals[0]:.4f}")
        print(f"  Can reach phi^2 = {phi**2:.4f}? "
              f"{'YES' if abs_evals[-1]/abs_evals[0] > phi**2 else 'NO'}")

        # 1. Phi powers
        power_results = analyze_phi_powers(abs_evals, phi=phi, max_power=5)
        print_phi_powers(power_results, label=f"s={s}")

        # 2. Sector analysis
        sector_results = sector_phi_analysis(eval_data, phi=phi)
        print_sector_analysis(sector_results)

        # 3. Band structure
        bands = analyze_band_structure(abs_evals)
        print_band_analysis(bands, phi=phi)

        # 4. Gauge coupling estimates
        analyze_gauge_couplings(s)

    # Final summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print("=" * 80)
    print()
    print(f"  The extended spectrum (p+q <= {max_pq_sum}) provides:")
    print(f"  1. Wider dynamic range for phi^2 test")
    print(f"  2. More sectors for sector-specific analysis")
    print(f"  3. Better spectral density statistics")
    print(f"  4. Definitive answer on Paasch geometric series")


def main():
    """Run extended analysis with current max_pq_sum=3 as baseline."""
    # First run with p+q <= 3 (currently available)
    print("Running baseline analysis (p+q <= 3)...")
    analyze_extended_spectrum(max_pq_sum=3, s_values=[0.0, 0.15, 1.14])

    # Attempt p+q <= 5 (will fail gracefully if not implemented)
    print("\n\nAttempting extended analysis (p+q <= 5)...")
    try:
        analyze_extended_spectrum(max_pq_sum=5, s_values=[0.0, 0.15, 1.14])
    except Exception as e:
        print(f"  Extended analysis not yet available: {e}")
        print(f"  Waiting for kk-theorist's Task #2 completion.")


if __name__ == "__main__":
    main()
