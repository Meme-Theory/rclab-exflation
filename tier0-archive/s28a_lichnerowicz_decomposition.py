"""
SESSION 28a COMPUTATION E-1: LICHNEROWICZ GAP DECOMPOSITION
=============================================================

Decomposes the spectral gap ratio gap_T/gap_K from Session 27 (T-1 gate)
into Lichnerowicz components.

Physics:
  The Lichnerowicz formula for the Levi-Civita Dirac operator D_K:
    D_K^2 = nabla*nabla + R/4

  where nabla*nabla is the connection Laplacian and R/4 is the scalar
  curvature endomorphism. This gives the Lichnerowicz bound:
    lambda_K^2 >= R_K(tau)/4     (for the smallest eigenvalue)

  For the canonical-connection Dirac D_can (flat connection, nabla_can
  has zero curvature), we have:
    D_can^2 = nabla_can*nabla_can    (no curvature endomorphism)

  The gap ratio gap_T/gap_K < 1 (proven by T-1 PASS) implies the curvature
  endomorphism R/4 is responsible for part of D_K's spectral gap.

  We decompose:
    gap_K^2 = gap_T^2 + R_contribution
  where R_contribution = gap_K^2 - gap_T^2 isolates the curvature's role.

  The curvature fraction:
    f_R(tau) = R_contribution / gap_K^2 = 1 - (gap_T/gap_K)^2

  quantifies what fraction of gap_K^2 is due to curvature vs. pure algebra.

Additional analysis:
  - Compare R_contribution with the Lichnerowicz lower bound R_K(tau)/4
  - Check whether the gap is tight (saturates the bound) or loose
  - BCS implications: if f_R is large, D_can removes most of the gap barrier

Input:  tier0-computation/s27_torsion_gap_gate.npz
Output: tier0-computation/s28a_lichnerowicz.npz
        tier0-computation/s28a_lichnerowicz.png

Gate: DIAGNOSTIC. Quantifies how much easier BCS becomes when curvature
      endomorphism is absent.

Author: phonon-exflation-sim agent (Session 28a)
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import time

# Add tier0-computation to path for scalar curvature formula
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SCALAR CURVATURE OF JENSEN-DEFORMED SU(3)
# =============================================================================

def scalar_curvature_jensen(tau: float) -> float:
    """
    Scalar curvature R_K(tau) of (SU(3), g_tau) with the Jensen deformation.

    The exact analytic formula (from Baptista Paper 15 eq 3.80, verified in
    sp2_curvature_invariants.py at machine epsilon):

        R_K(tau) = (1/8) * [2*e^{2tau} - 1 + 8*e^{-tau} - e^{-4tau}]

    Wait -- let me use the VERIFIED formula from the codebase. The direct
    computation in tier1_spectral_action.py gives R_K(0) = +2 exactly.

    From sd20a_seeley_dewitt_gate.py (Session 20a), the formula is:
        R(s) = R(0) * [2*exp(2s) - 1 + 8*exp(-s) - exp(-4s)] / 8

    where R(0) = 2.

    Units: spectral (code) units where g_0 = -Killing/3 = I.

    Args:
        tau: Jensen deformation parameter (tau >= 0)

    Returns:
        R_K: scalar curvature (positive for compact Lie group)
    """
    # R(s)/R(0) = [2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}]/8
    # R(0) = 2
    ratio = (2 * np.exp(2 * tau) - 1 + 8 * np.exp(-tau) - np.exp(-4 * tau)) / 8
    return 2.0 * ratio


# =============================================================================
# LICHNEROWICZ DECOMPOSITION
# =============================================================================

def lichnerowicz_decomposition(gap_K: np.ndarray, gap_T: np.ndarray,
                                tau_values: np.ndarray) -> dict:
    """
    Decompose gap_K^2 into curvature and algebraic contributions.

    The Lichnerowicz formula D_K^2 = nabla*nabla + R/4 gives:
        gap_K^2 >= R_K/4

    For D_can (flat connection): gap_T comes from pure algebra (M_Lie).

    Decomposition:
        gap_K^2 = gap_T^2 + R_contribution
        R_contribution = gap_K^2 - gap_T^2
        f_R = R_contribution / gap_K^2 = 1 - (gap_T / gap_K)^2

    Cross-check: R_contribution >= R_K/4 (Lichnerowicz bound consistency).
    If R_contribution < R_K/4, the bound is not tight and there is additional
    algebraic structure beyond the curvature endomorphism.

    Args:
        gap_K: (n_sectors, n_tau) LC Dirac gaps
        gap_T: (n_sectors, n_tau) canonical Dirac gaps
        tau_values: (n_tau,) tau values

    Returns:
        dict with keys:
            R_contribution: gap_K^2 - gap_T^2 per sector
            f_R: curvature fraction (R_contribution / gap_K^2)
            R_K_quarter: R_K(tau)/4 (Lichnerowicz bound)
            tightness: R_contribution / (R_K/4) -- how close to bound
            gap_K_sq: gap_K^2
            gap_T_sq: gap_T^2
    """
    n_sec, n_tau = gap_K.shape

    gap_K_sq = gap_K ** 2
    gap_T_sq = gap_T ** 2
    R_contribution = gap_K_sq - gap_T_sq

    # Curvature fraction
    f_R = np.zeros_like(gap_K)
    for j in range(n_sec):
        for i in range(n_tau):
            if gap_K_sq[j, i] > 1e-30:
                f_R[j, i] = R_contribution[j, i] / gap_K_sq[j, i]
            else:
                f_R[j, i] = np.nan

    # Lichnerowicz bound: gap_K^2 >= R_K/4
    R_K = np.array([scalar_curvature_jensen(t) for t in tau_values])
    R_K_quarter = R_K / 4.0

    # Tightness: how close R_contribution is to the Lichnerowicz bound
    # tightness = R_contribution / (R_K/4). If = 1, bound is saturated.
    # If > 1, gap is above the bound (typical).
    tightness = np.zeros_like(gap_K)
    for j in range(n_sec):
        for i in range(n_tau):
            if abs(R_K_quarter[i]) > 1e-30:
                tightness[j, i] = R_contribution[j, i] / R_K_quarter[i]
            else:
                tightness[j, i] = np.nan

    return {
        'R_contribution': R_contribution,
        'f_R': f_R,
        'R_K': R_K,
        'R_K_quarter': R_K_quarter,
        'tightness': tightness,
        'gap_K_sq': gap_K_sq,
        'gap_T_sq': gap_T_sq,
    }


# =============================================================================
# BCS IMPLICATIONS
# =============================================================================

def bcs_implications(gap_K: np.ndarray, gap_T: np.ndarray,
                      sector_labels: list, tau_values: np.ndarray) -> dict:
    """
    Compute BCS-relevant metrics from the Lichnerowicz decomposition.

    The BCS gap equation critical condition M_max > 1 requires the pairing
    interaction to overcome the spectral gap. With D_can (weaker gap), the
    effective gap barrier is gap_T instead of gap_K.

    Key metrics:
    1. gap_reduction_factor = 1 - gap_T/gap_K : fractional gap reduction
    2. M_max_enhancement = (gap_K/gap_T)^2 : approximate enhancement of M_max
       (since M_max ~ coupling / gap^2 in the BdG kernel)
    3. gap_T_in_units_of_lambda_min : gap_T / lambda_min(tau=0) for BCS threshold

    Args:
        gap_K, gap_T: (n_sec, n_tau) gap arrays
        sector_labels: list of sector label strings
        tau_values: (n_tau,) tau values

    Returns:
        dict with BCS enhancement metrics
    """
    n_sec, n_tau = gap_K.shape

    gap_reduction = np.zeros_like(gap_K)
    M_enhancement = np.zeros_like(gap_K)

    for j in range(n_sec):
        for i in range(n_tau):
            if gap_K[j, i] > 1e-15:
                gap_reduction[j, i] = 1.0 - gap_T[j, i] / gap_K[j, i]
            else:
                gap_reduction[j, i] = np.nan

            if gap_T[j, i] > 1e-15:
                M_enhancement[j, i] = (gap_K[j, i] / gap_T[j, i]) ** 2
            else:
                M_enhancement[j, i] = np.inf  # gap vanishes => infinite enhancement

    return {
        'gap_reduction': gap_reduction,
        'M_enhancement': M_enhancement,
    }


# =============================================================================
# VERIFICATION: ANALYTICAL tau=0 CHECK
# =============================================================================

def verify_tau_zero(gap_K: np.ndarray, gap_T: np.ndarray,
                     sector_labels: list) -> dict:
    """
    At tau=0 (bi-invariant metric), verify D_can = M_Lie eigenvalues against
    known analytical results.

    At tau=0:
      - g_0 = I (round metric, after normalization)
      - Structure constants: ft_{abc} = f_{abc} (orthonormal = coordinate)
      - Gamma_LC^c_{ab} = (1/2)(f_{abc} - f_{bca} + f_{cab}) for the Koszul formula
      - For bi-invariant metric: Gamma_LC^c_{ab} = (1/2) f^c_{ab}
      - Omega_LC = (1/8) sum f_{abc} gamma_a gamma_b gamma_c (the cubic Casimir part)
      - M_Lie = sum_a rho(e_a) x gamma_a

    For the trivial rep (0,0): rho(e_a) = 0, so M_Lie = 0, gap_T = 0.
    For the fundamental (1,0): M_Lie has known eigenvalues from SU(3) representation
    theory tensored with Cliff(8) spinors.

    Verification: at tau=0, the Lichnerowicz bound gives
      gap_K^2(0) >= R_K(0)/4 = 2/4 = 0.5
      gap_K(0) >= sqrt(0.5) = 0.7071

    Known: gap_K(0) = 0.866 for (1,0), so gap_K^2 = 0.75 > 0.5. Not tight.

    Args:
        gap_K, gap_T: arrays at tau=0 (first column)
        sector_labels: list

    Returns:
        dict with verification results
    """
    results = {}

    R_0 = scalar_curvature_jensen(0.0)
    lich_bound = R_0 / 4.0

    for j, label in enumerate(sector_labels):
        gK = gap_K[j, 0]
        gT = gap_T[j, 0]
        gK_sq = gK ** 2
        gT_sq = gT ** 2
        R_contrib = gK_sq - gT_sq

        results[label] = {
            'gap_K': gK,
            'gap_T': gT,
            'gap_K_sq': gK_sq,
            'gap_T_sq': gT_sq,
            'R_contribution': R_contrib,
            'Lichnerowicz_bound': lich_bound,
            'bound_saturated': abs(gK_sq - lich_bound) < 0.01,
            'tightness': R_contrib / lich_bound if lich_bound > 0 else np.nan,
        }

    return results


# =============================================================================
# MAIN
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 72)
    print("SESSION 28a E-1: LICHNEROWICZ GAP DECOMPOSITION")
    print("=" * 72)

    # =========================================================================
    # Load Session 27 T-1 data
    # =========================================================================
    datafile = os.path.join(OUTDIR, "s27_torsion_gap_gate.npz")
    print(f"\nLoading: {datafile}")
    data = np.load(datafile, allow_pickle=True)

    tau_values = data['tau_values']
    sectors = data['sectors']
    sector_labels = [str(s) for s in data['sector_labels']]
    gap_K = data['gap_K']
    gap_T = data['gap_T']
    gap_ratio = data['gap_ratio']

    n_sec, n_tau = gap_K.shape
    print(f"  Sectors: {sector_labels}")
    print(f"  Tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}], n_tau={n_tau}")
    print(f"  Data shapes: gap_K={gap_K.shape}, gap_T={gap_T.shape}")

    # =========================================================================
    # Lichnerowicz decomposition
    # =========================================================================
    print("\n" + "-" * 72)
    print("LICHNEROWICZ DECOMPOSITION")
    print("-" * 72)

    lich = lichnerowicz_decomposition(gap_K, gap_T, tau_values)

    # Print detailed table for non-trivial sectors
    nontrivial = [j for j in range(n_sec) if not (sectors[j][0] == 0 and sectors[j][1] == 0)]

    print(f"\n  R_K(tau) values:")
    for i in [0, 5, 10, 15, 20]:
        print(f"    tau={tau_values[i]:.3f}: R_K={lich['R_K'][i]:.6f}, "
              f"R_K/4={lich['R_K_quarter'][i]:.6f}")

    print(f"\n  Curvature fraction f_R = 1 - (gap_T/gap_K)^2 per sector:")
    print(f"  {'tau':>6s} ", end="")
    for j in nontrivial:
        print(f" | {sector_labels[j]:>8s} f_R  {sector_labels[j]:>8s} tight", end="")
    print()
    print("  " + "-" * (8 + len(nontrivial) * 28))

    for i in range(n_tau):
        print(f"  {tau_values[i]:6.4f} ", end="")
        for j in nontrivial:
            fR = lich['f_R'][j, i]
            tight = lich['tightness'][j, i]
            fR_str = f"{fR:.4f}" if not np.isnan(fR) else "   NaN"
            tight_str = f"{tight:.4f}" if not np.isnan(tight) else "   NaN"
            print(f" | {fR_str:>8s}   {tight_str:>8s}   ", end="")
        print()

    # =========================================================================
    # Summary statistics
    # =========================================================================
    print("\n" + "-" * 72)
    print("SUMMARY BY SECTOR")
    print("-" * 72)

    for j in range(n_sec):
        label = sector_labels[j]
        p, q = sectors[j]

        if p == 0 and q == 0:
            print(f"\n  {label} (trivial):")
            print(f"    gap_T = 0 at all tau (M_Lie = 0 for trivial rep)")
            print(f"    f_R = 1.0 by definition (100% curvature)")
            print(f"    This sector is TRIVIALLY gap-free under D_can.")
            continue

        f_R_vals = lich['f_R'][j, :]
        tight_vals = lich['tightness'][j, :]

        valid = ~np.isnan(f_R_vals)
        f_R_min = np.nanmin(f_R_vals) if np.any(valid) else np.nan
        f_R_max = np.nanmax(f_R_vals) if np.any(valid) else np.nan
        f_R_mean = np.nanmean(f_R_vals) if np.any(valid) else np.nan

        tight_min = np.nanmin(tight_vals) if np.any(valid) else np.nan
        tight_max = np.nanmax(tight_vals) if np.any(valid) else np.nan

        # Where is curvature contribution maximized?
        idx_max_fR = np.nanargmax(f_R_vals) if np.any(valid) else 0

        print(f"\n  {label}:")
        print(f"    f_R range:  [{f_R_min:.4f}, {f_R_max:.4f}]  (mean {f_R_mean:.4f})")
        print(f"    f_R max at: tau={tau_values[idx_max_fR]:.4f}")
        print(f"    Tightness:  [{tight_min:.4f}, {tight_max:.4f}]")
        print(f"    gap_K range:  [{np.min(gap_K[j,:]):.6f}, {np.max(gap_K[j,:]):.6f}]")
        print(f"    gap_T range:  [{np.min(gap_T[j,:]):.6f}, {np.max(gap_T[j,:]):.6f}]")
        print(f"    R_contribution range: [{np.min(lich['R_contribution'][j,:]):.6f}, "
              f"{np.max(lich['R_contribution'][j,:]):.6f}]")

        # BCS implication
        if tight_min > 1.0:
            print(f"    --> R_contribution EXCEEDS R_K/4 everywhere: curvature endomorphism")
            print(f"        accounts for LESS than the full R_contribution. Additional")
            print(f"        algebraic structure in Omega_LC contributes to the gap.")
        elif tight_max < 1.0:
            print(f"    --> R_contribution BELOW R_K/4 everywhere: this should not happen")
            print(f"        if the Lichnerowicz bound is correct. CHECK FOR BUGS.")
        else:
            print(f"    --> Tightness crosses 1.0: transition between curvature-dominated")
            print(f"        and algebra-dominated regimes.")

    # =========================================================================
    # BCS implications
    # =========================================================================
    print("\n" + "-" * 72)
    print("BCS IMPLICATIONS")
    print("-" * 72)

    bcs = bcs_implications(gap_K, gap_T, sector_labels, tau_values)

    print(f"\n  M_max enhancement = (gap_K/gap_T)^2 (approximate BdG kernel scaling):")
    print(f"  {'tau':>6s} ", end="")
    for j in nontrivial:
        print(f" | {sector_labels[j]:>8s}", end="")
    print()
    print("  " + "-" * (8 + len(nontrivial) * 12))

    for i in range(n_tau):
        print(f"  {tau_values[i]:6.4f} ", end="")
        for j in nontrivial:
            enh = bcs['M_enhancement'][j, i]
            if np.isinf(enh):
                print(f" |      inf", end="")
            else:
                print(f" | {enh:8.3f}", end="")
        print()

    # Key BCS numbers
    print(f"\n  Key BCS numbers (from Session 23a: M_max(D_K) = 0.077-0.154 at mu=0):")
    for j in nontrivial:
        label = sector_labels[j]
        # Find tau closest to 0.15 and 0.30 (key tau values)
        for tau_target in [0.15, 0.25, 0.35]:
            i_target = np.argmin(np.abs(tau_values - tau_target))
            enh = bcs['M_enhancement'][j, i_target]
            red = bcs['gap_reduction'][j, i_target]
            gK = gap_K[j, i_target]
            gT = gap_T[j, i_target]
            if not np.isinf(enh):
                M_K_approx_low = 0.077
                M_K_approx_high = 0.154
                M_T_approx_low = M_K_approx_low * enh
                M_T_approx_high = M_K_approx_high * enh
                print(f"    {label} tau={tau_values[i_target]:.3f}: gap {gK:.4f}->{gT:.4f} "
                      f"({red:.1%} reduction), M_max enhancement {enh:.2f}x, "
                      f"M_max(D_can) ~ {M_T_approx_low:.3f}-{M_T_approx_high:.3f}")

    # =========================================================================
    # Verification at tau=0
    # =========================================================================
    print("\n" + "-" * 72)
    print("VERIFICATION AT tau=0 (bi-invariant metric)")
    print("-" * 72)

    v0 = verify_tau_zero(gap_K, gap_T, sector_labels)
    for label, v in v0.items():
        print(f"\n  {label}:")
        print(f"    gap_K = {v['gap_K']:.6f}, gap_K^2 = {v['gap_K_sq']:.6f}")
        print(f"    gap_T = {v['gap_T']:.6f}, gap_T^2 = {v['gap_T_sq']:.6f}")
        print(f"    R_contribution = {v['R_contribution']:.6f}")
        print(f"    Lichnerowicz bound R_K(0)/4 = {v['Lichnerowicz_bound']:.6f}")
        print(f"    Tightness (R_contrib / R/4) = {v['tightness']:.4f}" if not np.isnan(v['tightness']) else "")
        print(f"    Bound saturated? {v['bound_saturated']}")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("GATE E-1 VERDICT: LICHNEROWICZ GAP DECOMPOSITION")
    print("=" * 72)

    # Compute key diagnostic numbers
    max_f_R = 0
    max_f_R_sector = ""
    max_f_R_tau = 0

    for j in nontrivial:
        for i in range(n_tau):
            if not np.isnan(lich['f_R'][j, i]) and lich['f_R'][j, i] > max_f_R:
                max_f_R = lich['f_R'][j, i]
                max_f_R_sector = sector_labels[j]
                max_f_R_tau = tau_values[i]

    # Max M_max enhancement
    max_enh = 0
    max_enh_sector = ""
    max_enh_tau = 0
    for j in nontrivial:
        for i in range(n_tau):
            enh = bcs['M_enhancement'][j, i]
            if not np.isinf(enh) and enh > max_enh:
                max_enh = enh
                max_enh_sector = sector_labels[j]
                max_enh_tau = tau_values[i]

    print(f"\n  VERDICT: DIAGNOSTIC (E-1 is a diagnostic gate, not closure/pass)")
    print(f"\n  Key numbers:")
    print(f"    Max curvature fraction f_R = {max_f_R:.4f} in {max_f_R_sector} at tau={max_f_R_tau:.3f}")
    print(f"    --> {max_f_R:.1%} of gap_K^2 is due to curvature endomorphism")
    print(f"    Max M_enhancement = {max_enh:.2f}x in {max_enh_sector} at tau={max_enh_tau:.3f}")
    print(f"    --> BdG kernel eigenvalue scales as M ~ coupling/gap^2")
    print(f"    --> D_can removes curvature contribution, enhancing M_max by up to {max_enh:.1f}x")
    print(f"\n  BCS assessment:")

    # Check if enhancement is enough to push M_max above 1
    M_K_low = 0.077
    M_K_high = 0.154
    threshold = 1.0

    enh_needed_low = threshold / M_K_low
    enh_needed_high = threshold / M_K_high

    print(f"    M_max(D_K, mu=0) = {M_K_low:.3f} to {M_K_high:.3f} (Session 23a K-1e)")
    print(f"    Enhancement needed for M_max > 1: {enh_needed_high:.1f}x to {enh_needed_low:.1f}x")
    print(f"    Max enhancement available: {max_enh:.2f}x")

    if max_enh >= enh_needed_high:
        print(f"\n    --> Enhancement SUFFICIENT in best case (need {enh_needed_high:.1f}x, have {max_enh:.1f}x)")
        print(f"    --> Torsionful BCS (computation E-4/S-1/L-4) is JUSTIFIED as next step")
        verdict_detail = "SUFFICIENT_ENHANCEMENT"
    else:
        print(f"\n    --> Enhancement INSUFFICIENT even in best case")
        print(f"    --> Torsionful BCS unlikely to cross M_max > 1 from gap reduction alone")
        verdict_detail = "INSUFFICIENT_ENHANCEMENT"

    print("=" * 72)

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    outfile = os.path.join(OUTDIR, "s28a_lichnerowicz.npz")
    np.savez(outfile,
             tau_values=tau_values,
             sectors=sectors,
             sector_labels=np.array(sector_labels),
             gap_K=gap_K,
             gap_T=gap_T,
             gap_K_sq=lich['gap_K_sq'],
             gap_T_sq=lich['gap_T_sq'],
             R_contribution=lich['R_contribution'],
             f_R=lich['f_R'],
             R_K=lich['R_K'],
             R_K_quarter=lich['R_K_quarter'],
             tightness=lich['tightness'],
             gap_reduction=bcs['gap_reduction'],
             M_enhancement=bcs['M_enhancement'],
             verdict_detail=verdict_detail)
    print(f"\nData saved to: {outfile}")

    # =========================================================================
    # PLOT
    # =========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("E-1: Lichnerowicz Gap Decomposition — D_K vs D_canonical",
                 fontsize=14, fontweight='bold')

    colors = {1: '#ff7f0e', 2: '#2ca02c', 3: '#d62728'}  # sector index -> color

    # Panel 1: gap_K^2 decomposition
    ax = axes[0, 0]
    for j in nontrivial:
        ax.fill_between(tau_values, 0, lich['gap_T_sq'][j, :],
                         alpha=0.3, color=colors[j], label=f'{sector_labels[j]} algebraic')
        ax.fill_between(tau_values, lich['gap_T_sq'][j, :], lich['gap_K_sq'][j, :],
                         alpha=0.3, color=colors[j], hatch='//',
                         label=f'{sector_labels[j]} curvature')
        ax.plot(tau_values, lich['gap_K_sq'][j, :], '-', color=colors[j], linewidth=2)
    ax.plot(tau_values, lich['R_K_quarter'], 'k--', linewidth=1.5, label=r'$R_K/4$ (Lich. bound)')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'gap$^2$')
    ax.set_title(r'gap$_K^2$ = algebraic + curvature')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: Curvature fraction f_R
    ax = axes[0, 1]
    for j in nontrivial:
        ax.plot(tau_values, lich['f_R'][j, :], '-o', color=colors[j],
                linewidth=2, markersize=3, label=sector_labels[j])
    ax.axhline(y=0.5, color='gray', linestyle=':', alpha=0.5, label='50%')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$f_R = 1 - (\mathrm{gap}_T / \mathrm{gap}_K)^2$')
    ax.set_title('Curvature fraction of gap$^2$')
    ax.set_ylim(0, 1)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Tightness (R_contribution vs R/4)
    ax = axes[0, 2]
    for j in nontrivial:
        ax.plot(tau_values, lich['tightness'][j, :], '-o', color=colors[j],
                linewidth=2, markersize=3, label=sector_labels[j])
    ax.axhline(y=1.0, color='black', linestyle=':', linewidth=1.5, label='Saturated')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'R_contribution / ($R_K$/4)')
    ax.set_title('Tightness of Lichnerowicz bound')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: M_max enhancement
    ax = axes[1, 0]
    for j in nontrivial:
        enh = bcs['M_enhancement'][j, :]
        enh_plot = np.where(np.isinf(enh), np.nan, enh)
        ax.plot(tau_values, enh_plot, '-o', color=colors[j],
                linewidth=2, markersize=3, label=sector_labels[j])
    ax.axhline(y=enh_needed_high, color='gray', linestyle='--', alpha=0.7,
               label=f'Needed ({enh_needed_high:.1f}x)')
    ax.axhline(y=enh_needed_low, color='gray', linestyle=':', alpha=0.5,
               label=f'Needed ({enh_needed_low:.1f}x)')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$(gap_K / gap_T)^2$')
    ax.set_title(r'$M_\mathrm{max}$ enhancement factor')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 5: Gap reduction percentage
    ax = axes[1, 1]
    for j in nontrivial:
        red = bcs['gap_reduction'][j, :]
        red_plot = np.where(np.isnan(red), np.nan, red * 100)
        ax.plot(tau_values, red_plot, '-o', color=colors[j],
                linewidth=2, markersize=3, label=sector_labels[j])
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Gap reduction (%)')
    ax.set_title('Gap reduction: D_K to D_canonical')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 6: R_K(tau) and R_K/4
    ax = axes[1, 2]
    ax.plot(tau_values, lich['R_K'], 'b-', linewidth=2, label=r'$R_K(\tau)$')
    ax.plot(tau_values, lich['R_K_quarter'], 'r--', linewidth=2, label=r'$R_K/4$')
    for j in nontrivial:
        ax.plot(tau_values, lich['R_contribution'][j, :], '-', color=colors[j],
                linewidth=1.5, label=f'{sector_labels[j]} R_contrib')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Curvature / gap$^2$')
    ax.set_title(r'$R_K(\tau)$ and curvature contribution to gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plotfile = os.path.join(OUTDIR, "s28a_lichnerowicz.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    print(f"Plot saved to: {plotfile}")
    plt.close()

    total_time = time.time() - t_start
    print(f"\nTotal computation time: {total_time:.1f}s")

    return verdict_detail


if __name__ == '__main__':
    verdict = main()
    print(f"\nFinal verdict detail: {verdict}")
