"""
H-4: ENTROPY COUNTING AT s_0 — SPECIES vs SM DOF
=================================================

At the V_eff minimum s_0 (from H-1), count the number of light species:
  N_species(s) = number of D_K eigenvalues |lambda_j(s)| below cutoff Lambda

Compare to the Standard Model DOF count:
  ~28 bosonic + ~90 fermionic on-shell DOF = ~118 total

Key question (from Giants G3): Does N_species maximize at or near s_0?
If so, the V_eff minimum maximizes the number of light species —
a thermodynamic selection principle: entropy maximization selects s_0.

The species count is computed WITH Peter-Weyl multiplicities:
  Each eigenvalue in sector (p,q) appears dim(p,q) times in L^2(SU(3),S).
  dim(p,q) = (p+1)(q+1)(p+q+2)/2.

Author: Hawking-Theorist Agent (Session 17d)
Date: 2026-02-14

Reference values:
  s_0 = 0.164 (H-1, Boltzmann-regulated V_eff minimum at Lambda_UV = 1.23)
  s_W = 0.2994 (B-1, from sin^2 theta_W = 0.2312)
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

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
    get_irrep,
    dirac_operator_on_irrep,
    collect_spectrum,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# =============================================================================
# PART 1: SPECIES COUNTING FUNCTION
# =============================================================================

def count_species(all_eigenvalues, cutoff):
    """
    Count the number of species (eigenvalue modes) below a cutoff.

    Each eigenvalue is counted WITH its Peter-Weyl multiplicity.
    Only positive eigenvalues are counted (spectrum is +/- symmetric,
    so total DOF = 2 * N_positive for the Dirac modes).

    Args:
        all_eigenvalues: list of (eigenvalue_complex, pw_multiplicity)
        cutoff: Lambda cutoff value

    Returns:
        n_distinct: number of distinct eigenvalues below cutoff
        n_with_mult: number including Peter-Weyl multiplicities
        n_total_dof: total DOF (counting +/- pairs, so 2 * n_with_mult for positive only)
    """
    n_distinct = 0
    n_with_mult = 0

    for ev, mult in all_eigenvalues:
        val = abs(ev)
        if val < 1e-14:
            continue  # skip zero modes (there are none, but safety)
        if val <= cutoff:
            # Count only positive eigenvalues (each has a -lambda partner)
            if ev.imag > 0 or (abs(ev.imag) < 1e-14 and ev.real > 0):
                n_distinct += 1
                n_with_mult += mult

    # Total DOF: each positive eigenvalue has a negative partner
    # In the Dirac spectrum, +lambda and -lambda are paired by chirality
    # So total = 2 * (positive count with multiplicity)
    n_total_dof = 2 * n_with_mult

    return n_distinct, n_with_mult, n_total_dof


def count_species_all_evals(all_eigenvalues, cutoff):
    """
    Alternative: count ALL eigenvalues below cutoff (not just positive).
    This gives the total number of modes including the +/- pairing.

    Returns:
        n_distinct: distinct eigenvalues with |lambda| <= cutoff
        n_with_mult: including Peter-Weyl multiplicities
    """
    n_distinct = 0
    n_with_mult = 0

    for ev, mult in all_eigenvalues:
        val = abs(ev)
        if val <= cutoff:
            n_distinct += 1
            n_with_mult += mult

    return n_distinct, n_with_mult


# =============================================================================
# PART 2: SPECTRUM AT s_0 WITH CUTOFF SWEEP
# =============================================================================

def spectrum_at_s0(s0, gens, f_abc, gammas, max_pq_sum=6):
    """
    Compute the full spectrum at s_0 and sweep the cutoff Lambda.

    Returns:
        all_evals: raw eigenvalue data
        eval_data: per-sector data
        sweep: list of (Lambda, n_distinct_pos, n_mult_pos, n_total_dof)
    """
    print(f"\n  Computing spectrum at s = {s0:.4f} (max_pq_sum = {max_pq_sum})...")
    t0 = time.time()
    all_evals, eval_data = collect_spectrum(s0, gens, f_abc, gammas,
                                            max_pq_sum=max_pq_sum, verbose=True)
    dt = time.time() - t0
    print(f"  Spectrum computed in {dt:.1f}s")

    # Extract all |lambda| values for reporting
    abs_vals = sorted(set(abs(ev) for ev, _ in all_evals if abs(ev) > 1e-14))
    print(f"\n  Number of distinct |lambda| values: {len(abs_vals)}")
    print(f"  Range: [{abs_vals[0]:.6f}, {abs_vals[-1]:.6f}]")

    # Cutoff sweep
    # Natural cutoff = KK scale = 1/R_SU(3). In our units, R = 1 => Lambda_KK ~ 1.
    # But the eigenvalues are O(1) at s=0 and grow with s.
    # Sweep from 0 to 2*max_eigenvalue.
    max_ev = abs_vals[-1]
    cutoffs = np.concatenate([
        np.arange(0.1, 1.0, 0.1),
        np.arange(1.0, 5.0, 0.25),
        np.arange(5.0, max_ev + 1, 1.0),
    ])

    sweep = []
    print(f"\n  CUTOFF SWEEP:")
    print(f"  {'Lambda':>8s}  {'N_distinct':>10s}  {'N_w/mult':>10s}  {'N_total_DOF':>12s}")
    print(f"  {'':->8s}  {'':->10s}  {'':->10s}  {'':->12s}")
    for lam in cutoffs:
        nd, nm, ntot = count_species(all_evals, lam)
        sweep.append((lam, nd, nm, ntot))
        if lam in [0.5, 1.0, 1.23, 2.0, 3.0, 5.0, 10.0] or lam == cutoffs[-1]:
            print(f"  {lam:8.2f}  {nd:10d}  {nm:10d}  {ntot:12d}")

    return all_evals, eval_data, sweep, abs_vals


# =============================================================================
# PART 3: SM DOF COMPARISON
# =============================================================================

def sm_comparison(n_total_at_kk, eval_data, s0):
    """
    Compare N_species(s_0) to Standard Model DOF count.

    SM on-shell DOF:
      Bosons: photon(2) + W(6) + Z(3) + gluon(16) + Higgs(1) = 28
      Fermions: 3 generations * [u(12)+d(12)+e(4)+nu(2)] = 90
      Total: 118

    Note: The D_K spectrum counts FERMIONIC KK modes only (spinor bundle).
    Bosonic modes (from scalar/vector Laplacians) are NOT included.
    So the comparison should be to fermionic DOF only: 90.
    """
    print(f"\n" + "=" * 70)
    print(f"  SM DOF COMPARISON AT s = {s0:.4f}")
    print(f"=" * 70)

    print(f"""
  Standard Model on-shell DOF:
    Bosons:  photon(2) + W+/-(6) + Z(3) + 8*gluon(16) + Higgs(1) = 28
    Fermions: 3 gen * [u_L,R(12) + d_L,R(12) + e_L,R(4) + nu_L(2)] = 90
    Total: 118

  NOTE: D_K eigenvalues are SPINOR modes (fermionic KK tower).
  Bosonic KK modes require separate Laplacian computation (not available).
  Fair comparison: D_K modes vs fermionic DOF = 90.

  D_K spectrum at s = {s0:.4f}:
    Total modes (all sectors, all eigenvalues): {n_total_at_kk}
    Fermionic SM target: 90
    Ratio: N_species / 90 = {n_total_at_kk / 90.0:.2f}
""")

    # Per-sector breakdown
    print(f"  PER-SECTOR BREAKDOWN:")
    print(f"  {'Sector':>8s}  {'dim(p,q)':>8s}  {'D_size':>6s}  {'N_evals':>8s}  {'N_w/mult':>10s}")
    print(f"  {'':->8s}  {'':->8s}  {'':->6s}  {'':->8s}  {'':->10s}")
    total_evals = 0
    total_mult = 0
    for p, q, evals_pi in eval_data:
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        n_ev = len(evals_pi)
        n_mult = n_ev * dim_pq
        total_evals += n_ev
        total_mult += n_mult
        print(f"  ({p},{q}){' '*(5-len(f'({p},{q})'))}"
              f"  {dim_pq:8d}  {n_ev:6d}  {n_ev:8d}  {n_mult:10d}")

    print(f"  {'TOTAL':>8s}  {'':>8s}  {'':>6s}  {total_evals:8d}  {total_mult:10d}")


# =============================================================================
# PART 4: N_SPECIES(s) AS A FUNCTION OF s
# =============================================================================

def species_vs_s(s_values, cutoff, gens, f_abc, gammas, max_pq_sum=6):
    """
    Compute N_species(s) for a range of s values at fixed cutoff Lambda.

    Returns:
        results: list of (s, n_distinct, n_with_mult, n_total_dof)
    """
    results = []
    for i, s in enumerate(s_values):
        all_evals, _ = collect_spectrum(s, gens, f_abc, gammas,
                                         max_pq_sum=max_pq_sum, verbose=False)
        nd, nm, ntot = count_species(all_evals, cutoff)
        results.append((s, nd, nm, ntot))
        if (i + 1) % 5 == 0:
            print(f"    [{i+1}/{len(s_values)}] s={s:.3f}: "
                  f"N_distinct={nd}, N_mult={nm}, N_total={ntot}")

    return results


# =============================================================================
# PART 5: PLOTTING
# =============================================================================

def make_plots(sweep_data, species_data, s0, cutoff_ref, abs_vals_at_s0):
    """
    Generate the H-4 diagnostic plots.

    Panel 1: N_species vs Lambda (cutoff sweep) at s_0
    Panel 2: N_species vs s at fixed Lambda
    Panel 3: Eigenvalue histogram at s_0
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel 1: Cutoff sweep
    ax1 = axes[0]
    lambdas = [x[0] for x in sweep_data]
    n_tots = [x[3] for x in sweep_data]
    ax1.plot(lambdas, n_tots, 'b-o', markersize=3)
    ax1.axhline(y=90, color='r', linestyle='--', alpha=0.7, label='SM fermion DOF = 90')
    ax1.axhline(y=118, color='g', linestyle='--', alpha=0.7, label='SM total DOF = 118')
    ax1.axvline(x=1.0, color='gray', linestyle=':', alpha=0.5, label='Lambda = 1 (KK scale)')
    ax1.axvline(x=1.23, color='orange', linestyle=':', alpha=0.5, label='Lambda = 1.23 (H-1)')
    ax1.set_xlabel('Cutoff Lambda')
    ax1.set_ylabel('N_total_DOF (with PW multiplicity)')
    ax1.set_title(f'Species Count vs Cutoff at s = {s0:.3f}')
    ax1.legend(fontsize=8)
    ax1.set_xlim(0, 10)
    ax1.grid(True, alpha=0.3)

    # Panel 2: N_species vs s
    ax2 = axes[1]
    s_vals = [x[0] for x in species_data]
    n_tots_s = [x[3] for x in species_data]
    ax2.plot(s_vals, n_tots_s, 'b-o', markersize=3)
    ax2.axvline(x=s0, color='r', linestyle='--', alpha=0.7, label=f's_0 = {s0:.3f} (H-1)')
    ax2.axvline(x=0.2994, color='g', linestyle='--', alpha=0.7, label='s_W = 0.299 (B-1)')
    ax2.set_xlabel('Jensen parameter s')
    ax2.set_ylabel(f'N_total_DOF (Lambda = {cutoff_ref:.1f})')
    ax2.set_title(f'Species Count vs s at Lambda = {cutoff_ref:.1f}')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # Find and mark the maximum
    max_idx = np.argmax(n_tots_s)
    s_max = s_vals[max_idx]
    n_max = n_tots_s[max_idx]
    ax2.plot(s_max, n_max, 'r*', markersize=15, zorder=5)
    ax2.annotate(f's_max = {s_max:.3f}\nN = {n_max}',
                 xy=(s_max, n_max), xytext=(s_max + 0.15, n_max - 20),
                 fontsize=8, arrowprops=dict(arrowstyle='->', color='red'))

    # Panel 3: Eigenvalue histogram at s_0
    ax3 = axes[2]
    ax3.hist(abs_vals_at_s0, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
    ax3.axvline(x=1.0, color='gray', linestyle=':', alpha=0.5, label='Lambda = 1')
    ax3.axvline(x=1.23, color='orange', linestyle=':', alpha=0.5, label='Lambda = 1.23')
    ax3.set_xlabel('|lambda|')
    ax3.set_ylabel('Count (distinct eigenvalues)')
    ax3.set_title(f'Eigenvalue Distribution at s = {s0:.3f}')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'h4_entropy_counting.png')
    plt.savefig(outpath, dpi=150)
    print(f"\n  Plot saved: {outpath}")
    plt.close()
    return outpath


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    t_start = time.time()

    print("=" * 70)
    print("H-4: ENTROPY COUNTING AT s_0 — SPECIES vs SM DOF")
    print("=" * 70)
    sys.stdout.flush()

    # Initialize infrastructure
    print("\n  Initializing SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    assert cliff_err < 1e-14, f"Clifford validation failed: {cliff_err}"
    print(f"  Clifford validated: max error = {cliff_err:.2e}")

    MAX_PQ_SUM = 6  # Same truncation as all Tier 1 computations

    # -------------------------------------------------------------------------
    # PART 1: Spectrum at s_0 = 0.164 (H-1 minimum)
    # -------------------------------------------------------------------------
    s0 = 0.164
    print(f"\n{'='*70}")
    print(f"  PART 1: SPECTRUM AND CUTOFF SWEEP AT s_0 = {s0}")
    print(f"{'='*70}")
    sys.stdout.flush()

    all_evals_s0, eval_data_s0, sweep_s0, abs_vals_s0 = \
        spectrum_at_s0(s0, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM)
    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # Key cutoff values
    # -------------------------------------------------------------------------
    print(f"\n  KEY CUTOFF VALUES:")
    for lam_test in [0.5, 1.0, 1.23, 2.0, 3.0, 5.0]:
        nd, nm, ntot = count_species(all_evals_s0, lam_test)
        nd_all, nm_all = count_species_all_evals(all_evals_s0, lam_test)
        print(f"    Lambda = {lam_test:.2f}: "
              f"N_distinct_pos = {nd}, N_w/mult_pos = {nm}, "
              f"N_total_DOF = {ntot}, "
              f"N_all_distinct = {nd_all}, N_all_w/mult = {nm_all}")
    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # PART 2: SM comparison
    # -------------------------------------------------------------------------
    # Use Lambda = 1.0 (KK scale) as reference cutoff
    _, _, n_total_at_kk = count_species(all_evals_s0, 1.0)
    sm_comparison(n_total_at_kk, eval_data_s0, s0)
    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # PART 3: Also report at Lambda = 1.23 (H-1 cutoff) and s_W = 0.2994
    # -------------------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"  PART 3: SPECTRUM AT s_W = 0.2994 (from sin^2 theta_W)")
    print(f"{'='*70}")
    s_W = 0.2994
    all_evals_sW, eval_data_sW, sweep_sW, abs_vals_sW = \
        spectrum_at_s0(s_W, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM)

    _, _, n_total_sW_kk = count_species(all_evals_sW, 1.0)
    _, _, n_total_sW_123 = count_species(all_evals_sW, 1.23)
    print(f"\n  At s_W = {s_W}:")
    print(f"    N_total_DOF (Lambda=1.0)  = {n_total_sW_kk}")
    print(f"    N_total_DOF (Lambda=1.23) = {n_total_sW_123}")
    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # PART 4: N_species(s) scan
    # -------------------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"  PART 4: N_SPECIES(s) SCAN")
    print(f"{'='*70}")

    # Use Lambda = 1.0 and Lambda = 2.0 as two reference cutoffs
    s_scan = np.linspace(0.0, 2.0, 41)

    print(f"\n  Scanning N_species(s) at Lambda = 1.0:")
    species_data_1 = species_vs_s(s_scan, 1.0, gens, f_abc, gammas,
                                    max_pq_sum=MAX_PQ_SUM)
    sys.stdout.flush()

    print(f"\n  Scanning N_species(s) at Lambda = 2.0:")
    species_data_2 = species_vs_s(s_scan, 2.0, gens, f_abc, gammas,
                                    max_pq_sum=MAX_PQ_SUM)
    sys.stdout.flush()

    # Report maxima
    for label, data in [("Lambda=1.0", species_data_1), ("Lambda=2.0", species_data_2)]:
        n_tots = [x[3] for x in data]
        max_idx = np.argmax(n_tots)
        s_max = data[max_idx][0]
        n_max = n_tots[max_idx]
        print(f"\n  {label}: Maximum N_species = {n_max} at s = {s_max:.3f}")
        # Is it at s=0?
        n_at_0 = data[0][3]
        n_at_s0_val = None
        for s_v, _, _, nt in data:
            if abs(s_v - s0) < 0.03:
                n_at_s0_val = nt
                break
        print(f"    N_species(s=0) = {n_at_0}")
        if n_at_s0_val is not None:
            print(f"    N_species(s={s0}) = {n_at_s0_val}")
        print(f"    Thermodynamic selection? {'YES' if abs(s_max - s0) < 0.1 else 'NO'}"
              f" (s_max = {s_max:.3f}, s_0 = {s0:.3f}, |diff| = {abs(s_max - s0):.3f})")

    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # PART 5: Plots
    # -------------------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"  PART 5: GENERATING PLOTS")
    print(f"{'='*70}")

    plot_path = make_plots(sweep_s0, species_data_1, s0, 1.0, abs_vals_s0)
    sys.stdout.flush()

    # -------------------------------------------------------------------------
    # FINAL SUMMARY
    # -------------------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"  H-4 FINAL SUMMARY")
    print(f"{'='*70}")

    _, _, n_s0_lam1 = count_species(all_evals_s0, 1.0)
    _, _, n_s0_lam123 = count_species(all_evals_s0, 1.23)
    _, _, n_s0_lam2 = count_species(all_evals_s0, 2.0)

    n_tots_1 = [x[3] for x in species_data_1]
    max_idx_1 = np.argmax(n_tots_1)
    s_max_1 = species_data_1[max_idx_1][0]

    n_tots_2 = [x[3] for x in species_data_2]
    max_idx_2 = np.argmax(n_tots_2)
    s_max_2 = species_data_2[max_idx_2][0]

    print(f"""
  AT s_0 = {s0} (H-1 V_eff minimum):
    N_species(Lambda=1.0)  = {n_s0_lam1}   (fermionic DOF, D_K modes only)
    N_species(Lambda=1.23) = {n_s0_lam123}  (H-1 cutoff)
    N_species(Lambda=2.0)  = {n_s0_lam2}

  SM COMPARISON:
    SM fermionic DOF = 90     (3 gen * 30 per gen)
    SM total DOF     = 118    (28 bosonic + 90 fermionic)
    N_species(s_0, Lambda=1.0)  / 90  = {n_s0_lam1/90.0:.2f}
    N_species(s_0, Lambda=1.23) / 90  = {n_s0_lam123/90.0:.2f}

  MAXIMUM SPECIES COUNT:
    At Lambda=1.0: N_max = {n_tots_1[max_idx_1]} at s = {s_max_1:.3f}
    At Lambda=2.0: N_max = {n_tots_2[max_idx_2]} at s = {s_max_2:.3f}
    s_0 = {s0}, s_W = 0.2994

  THERMODYNAMIC SELECTION:
    V_eff min at s_0 {'COINCIDES' if abs(s_max_1 - s0) < 0.1 else 'DOES NOT COINCIDE'}
    with N_species maximum (|s_0 - s_max| = {abs(s_max_1 - s0):.3f} at Lambda=1.0)

  NOTE: D_K counts FERMIONIC KK modes only. Bosonic modes require
  separate scalar/vector Laplacian computation (Tier 2 work).
  The ratio N_species/90 should be ~1 if the truncation at
  max_pq_sum = {MAX_PQ_SUM} captures the right number of light modes.

  PLOT: {plot_path}
""")

    t_total = time.time() - t_start
    print(f"  Total computation time: {t_total:.1f}s")
    print("=" * 70)
    sys.stdout.flush()
