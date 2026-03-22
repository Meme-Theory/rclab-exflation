"""
F-2: Domain-boundary phase shift estimate.

For two adjacent Planck-popcorn domains at tau_0 = 0.18 and tau_0 + delta_tau,
compute the D_K eigenvalue mismatch and the resulting phase shift per boundary.
Then compute cumulative random-walk Delta_L at d = 1 Gpc as a function of
coherence length l_coh.

Tests whether the Planck popcorn survives Perlman observational bounds.

Mathematical background:
  A photon-like mode propagating through the internal geometry acquires a phase
  phi = k * L where k ~ 1/lambda_min (the spectral gap sets the effective
  wavenumber in internal space). At a domain boundary where tau changes by
  delta_tau, the eigenvalue mismatch is:

    delta_k = |lambda_min(tau_0 + delta_tau) - lambda_min(tau_0)| / lambda_min(tau_0)

  The phase shift per boundary crossing is:

    delta_phi = delta_k * l_coh  (coherence length sets the effective path through each domain)

  For N_domains = d / l_coh domain crossings over propagation distance d,
  the cumulative phase fluctuation (random walk) is:

    Delta_phi = delta_phi * sqrt(N_domains) = delta_k * l_coh * sqrt(d / l_coh)
              = delta_k * sqrt(d * l_coh)

  The corresponding distance fluctuation (in Planck units):

    Delta_L = Delta_phi * l_P / (2*pi)

  Perlman bound: Delta_L < 10^{-15} m for d = 1 Gpc.

  Find minimum l_coh such that Delta_L < Perlman bound.

Gate F-2-G: PASS if l_coh < 10^6 * l_P satisfies Perlman bound.

Input: tier0-computation/tier1_dirac_spectrum.py (spectrum computation)
       OR s31Ca_foam_spectral_dim.npz (if available, for cached spectra)
Output: s31Ca_foam_domain_phase.{npz,png}

Session 31Ca -- Quantum Foam Diagnostics
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, collect_spectrum
)

# Physical constants
l_P = 1.616e-35       # Planck length (m)
Gpc_m = 3.086e25      # 1 Gpc in meters
Perlman_bound = 1e-15  # Delta_L bound (m) for d = 1 Gpc


def get_lambda_min_at_tau(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Compute the spectral gap (smallest |eigenvalue|) of D_K at given tau.

    Returns:
        lambda_min: float, smallest |eigenvalue|
        all_abs_evals: sorted array of all |eigenvalues|
    """
    all_evals, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                            max_pq_sum=max_pq_sum,
                                            verbose=False)
    abs_evals = np.array([np.abs(ev) for (ev, _) in all_evals])
    # Filter out zero modes (|lambda| < 1e-10)
    nonzero = abs_evals[abs_evals > 1e-10]
    if len(nonzero) == 0:
        return 0.0, abs_evals
    return np.min(nonzero), np.sort(abs_evals)


def get_eigenvalue_spectrum_at_tau(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Return full eigenvalue spectrum (absolute values, sorted) with multiplicities.
    """
    all_evals, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                            max_pq_sum=max_pq_sum,
                                            verbose=False)
    abs_evals = []
    mults = []
    for (ev, mult) in all_evals:
        abs_evals.append(np.abs(ev))
        mults.append(mult)
    abs_evals = np.array(abs_evals)
    mults = np.array(mults)
    order = np.argsort(abs_evals)
    return abs_evals[order], mults[order]


def main():
    print("=" * 70)
    print("F-2: Domain-Boundary Phase Shift Estimate")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    tau_0 = 0.18
    delta_tau_values = np.linspace(0.001, 0.05, 20)

    max_pq = 6

    # Compute reference spectrum at tau_0
    print(f"\nReference spectrum at tau_0 = {tau_0}...")
    lmin_0, evals_0 = get_lambda_min_at_tau(tau_0, gens, f_abc, gammas, max_pq)
    print(f"  lambda_min(tau_0) = {lmin_0:.6f}")

    # Full spectrum for phase-shift calculation
    abs_evals_0, mults_0 = get_eigenvalue_spectrum_at_tau(tau_0, gens, f_abc, gammas, max_pq)
    n_modes = len(abs_evals_0)
    n_total = int(np.sum(mults_0))
    print(f"  {n_modes} distinct eigenvalues, {n_total} total modes")

    # Compute eigenvalue mismatch for each delta_tau
    print(f"\nComputing eigenvalue mismatch at {len(delta_tau_values)} delta_tau values...")
    delta_k_values = np.zeros(len(delta_tau_values))
    lmin_shifted = np.zeros(len(delta_tau_values))

    # We also compute the RMS eigenvalue mismatch across the full spectrum
    # weighted by multiplicities (more physically relevant for phase accumulation)
    rms_mismatch = np.zeros(len(delta_tau_values))

    for i, dtau in enumerate(delta_tau_values):
        tau_shifted = tau_0 + dtau
        lmin_s, evals_s = get_lambda_min_at_tau(tau_shifted, gens, f_abc, gammas, max_pq)
        lmin_shifted[i] = lmin_s

        # Fractional spectral gap mismatch
        delta_k_values[i] = abs(lmin_s - lmin_0) / lmin_0

        # RMS mismatch over full spectrum (matching by index after sorting)
        abs_evals_s, mults_s = get_eigenvalue_spectrum_at_tau(tau_shifted, gens, f_abc, gammas, max_pq)
        n_compare = min(len(abs_evals_0), len(abs_evals_s))
        diff_sq = (abs_evals_0[:n_compare] - abs_evals_s[:n_compare])**2
        total_mults = mults_0[:n_compare]
        rms_mismatch[i] = np.sqrt(np.sum(total_mults * diff_sq) / np.sum(total_mults))

        print(f"  delta_tau={dtau:.4f}: lmin={lmin_s:.6f}, "
              f"delta_k/k={delta_k_values[i]:.6f}, rms_mismatch={rms_mismatch[i]:.6f}")

    # =====================================================================
    # Phase shift calculation
    # =====================================================================
    print("\n--- Phase Shift vs Coherence Length ---")

    d_prop = Gpc_m  # propagation distance = 1 Gpc
    l_coh_test = np.array([10, 100, 1000, 1e6]) * l_P  # test coherence lengths

    # Use the median delta_tau case (delta_tau ~ 0.025) as representative
    representative_idx = len(delta_tau_values) // 2
    delta_k_rep = delta_k_values[representative_idx]
    delta_tau_rep = delta_tau_values[representative_idx]
    rms_rep = rms_mismatch[representative_idx]

    print(f"\nRepresentative delta_tau = {delta_tau_rep:.4f}")
    print(f"  delta_k/k = {delta_k_rep:.6f}")
    print(f"  RMS mismatch = {rms_rep:.6f}")

    print(f"\nPerlman bound: Delta_L < {Perlman_bound:.0e} m at d = 1 Gpc")
    print(f"  (1 Gpc = {d_prop:.3e} m)")

    results_table = []
    for l_c in l_coh_test:
        N_domains = d_prop / l_c
        # Phase shift per boundary: delta_phi = delta_k * (l_c / l_P)
        # because the internal wavenumber is in Planck units
        # and the effective path through internal space scales with l_c
        #
        # More precisely: delta_phi_per_boundary = |delta_lambda_min| * l_c / l_P
        # where delta_lambda_min is in KK units (1/R_KK ~ 1/l_P at Planck scale)
        delta_phi_per_boundary = delta_k_rep  # fractional mismatch = dimensionless phase shift

        # Cumulative random walk
        Delta_phi = delta_phi_per_boundary * np.sqrt(N_domains)

        # Convert to distance fluctuation
        # Delta_L = (Delta_phi / (2*pi)) * l_P  (one wavelength = one Planck length)
        Delta_L = (Delta_phi / (2 * np.pi)) * l_P

        passes_perlman = Delta_L < Perlman_bound
        l_c_ratio = l_c / l_P

        results_table.append((l_c_ratio, N_domains, delta_phi_per_boundary,
                               Delta_phi, Delta_L, passes_perlman))

        print(f"  l_coh = {l_c_ratio:.0e} l_P: N_dom = {N_domains:.2e}, "
              f"Delta_phi = {Delta_phi:.2e}, Delta_L = {Delta_L:.2e} m, "
              f"Perlman: {'PASS' if passes_perlman else 'FAIL'}")

    # Find critical l_coh analytically
    # Delta_L = (delta_k / (2*pi)) * l_P * sqrt(d_prop / l_coh)
    # Delta_L < Perlman_bound
    # => l_coh > d_prop * (delta_k * l_P / (2*pi * Perlman_bound))^2
    l_coh_critical = d_prop * (delta_k_rep * l_P / (2 * np.pi * Perlman_bound))**2
    l_coh_critical_lP = l_coh_critical / l_P

    print(f"\n  Critical coherence length: l_coh_crit = {l_coh_critical_lP:.2e} l_P = {l_coh_critical:.2e} m")

    # =====================================================================
    # Also compute with RMS mismatch (more conservative)
    # =====================================================================
    print("\n--- RMS Mismatch Analysis ---")
    # Use rms_rep instead of delta_k_rep
    l_coh_critical_rms = d_prop * (rms_rep * l_P / (2 * np.pi * Perlman_bound))**2
    l_coh_critical_rms_lP = l_coh_critical_rms / l_P
    print(f"  With RMS mismatch ({rms_rep:.6f}):")
    print(f"  Critical coherence length: l_coh_crit = {l_coh_critical_rms_lP:.2e} l_P")

    # =====================================================================
    # Scan over all delta_tau to find max l_coh_crit
    # =====================================================================
    print("\n--- l_coh_crit vs delta_tau ---")
    l_coh_crit_vs_dtau = np.zeros(len(delta_tau_values))
    for i, dtau in enumerate(delta_tau_values):
        dk = delta_k_values[i]
        if dk > 0:
            l_coh_crit_vs_dtau[i] = d_prop * (dk * l_P / (2 * np.pi * Perlman_bound))**2 / l_P
        else:
            l_coh_crit_vs_dtau[i] = 0

    max_lcrit = np.max(l_coh_crit_vs_dtau)
    max_dtau = delta_tau_values[np.argmax(l_coh_crit_vs_dtau)]
    print(f"  Maximum l_coh_crit = {max_lcrit:.2e} l_P at delta_tau = {max_dtau:.4f}")

    # =====================================================================
    # Gate F-2-G Assessment
    # =====================================================================
    print("\n" + "=" * 70)
    print("GATE F-2-G ASSESSMENT")
    print("=" * 70)

    gate_threshold = 1e6 * l_P  # l_coh < 10^6 l_P
    # The gate asks: does l_coh < 10^6 l_P satisfy Perlman?
    # This means: is l_coh_crit < 10^6 l_P?
    # If l_coh_crit < 10^6 l_P, then even small coherence lengths suffice -> PASS
    # If l_coh_crit > 10^6 l_P, then macroscopic coherence is needed -> FAIL (or CONDITIONAL)

    if l_coh_critical_lP < 1e6:
        verdict = "PASS"
        verdict_detail = (f"l_coh_crit = {l_coh_critical_lP:.2e} l_P < 10^6 l_P. "
                          f"Even sub-micron coherence satisfies Perlman.")
    elif l_coh_critical_lP < 1e20:
        verdict = "CONDITIONAL"
        verdict_detail = (f"l_coh_crit = {l_coh_critical_lP:.2e} l_P > 10^6 l_P. "
                          f"Macroscopic coherence required. "
                          f"Popcorn survives IF coherence transition has occurred.")
    else:
        verdict = "FAIL"
        verdict_detail = (f"l_coh_crit = {l_coh_critical_lP:.2e} l_P. "
                          f"Absurdly large coherence required. Popcorn excluded.")

    print(f"\n  Gate F-2-G verdict: {verdict}")
    print(f"  Detail: {verdict_detail}")

    # =====================================================================
    # Save
    # =====================================================================
    outfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_domain_phase.npz")
    np.savez_compressed(outfile,
        tau_0=np.array(tau_0),
        delta_tau_values=delta_tau_values,
        delta_k_values=delta_k_values,
        rms_mismatch=rms_mismatch,
        lmin_0=np.array(lmin_0),
        lmin_shifted=lmin_shifted,
        l_coh_critical_lP=np.array(l_coh_critical_lP),
        l_coh_critical_rms_lP=np.array(l_coh_critical_rms_lP),
        l_coh_crit_vs_dtau=l_coh_crit_vs_dtau,
        max_lcrit_lP=np.array(max_lcrit),
        d_prop_m=np.array(d_prop),
        Perlman_bound_m=np.array(Perlman_bound),
        verdict=np.array(verdict),
    )
    print(f"\n  Saved: {outfile}")

    # =====================================================================
    # Plot
    # =====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: delta_k/k vs delta_tau
    ax = axes[0, 0]
    ax.plot(delta_tau_values, delta_k_values, 'bo-', lw=2, label=r'$\delta k / k$ (gap)')
    ax.plot(delta_tau_values, rms_mismatch, 'rs-', lw=2, label='RMS mismatch')
    ax.set_xlabel(r'$\delta\tau$')
    ax.set_ylabel('Fractional eigenvalue mismatch')
    ax.set_title(r'Eigenvalue Mismatch at $\tau_0=0.18$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: lambda_min vs tau around tau_0
    ax = axes[0, 1]
    tau_plot = tau_0 + delta_tau_values
    ax.plot(tau_plot, lmin_shifted, 'bo-', lw=2)
    ax.axhline(lmin_0, color='r', ls='--', lw=1, label=f'$\\lambda_{{min}}(\\tau_0)={lmin_0:.4f}$')
    ax.axvline(tau_0, color='gray', ls=':', lw=1, label=f'$\\tau_0={tau_0}$')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\lambda_{min}$')
    ax.set_title('Spectral Gap Near Gradient-Balance Point')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: l_coh_crit vs delta_tau
    ax = axes[1, 0]
    ax.semilogy(delta_tau_values, l_coh_crit_vs_dtau, 'ko-', lw=2)
    ax.axhline(1e6, color='r', ls='--', lw=1, label=r'$10^6 \, l_P$')
    ax.axhline(1, color='green', ls='--', lw=1, alpha=0.5, label=r'$l_P$')
    ax.set_xlabel(r'$\delta\tau$')
    ax.set_ylabel(r'$l_{coh,crit}$ [$l_P$]')
    ax.set_title('Critical Coherence Length for Perlman')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 4: Delta_L vs l_coh for representative delta_tau
    ax = axes[1, 1]
    l_coh_range = np.logspace(0, 30, 200) * l_P
    N_dom = d_prop / l_coh_range
    Delta_L_range = (delta_k_rep / (2 * np.pi)) * l_P * np.sqrt(N_dom)
    ax.loglog(l_coh_range / l_P, Delta_L_range, 'b-', lw=2, label=f'$\\delta\\tau={delta_tau_rep:.3f}$')
    ax.axhline(Perlman_bound, color='r', ls='--', lw=2, label=f'Perlman: $\\Delta L < {Perlman_bound:.0e}$ m')
    ax.axvline(1e6, color='orange', ls='--', lw=1, alpha=0.7, label=r'$10^6 \, l_P$')
    ax.axvline(l_coh_critical_lP, color='green', ls=':', lw=2, label=f'$l_{{coh,crit}} = {l_coh_critical_lP:.1e} \\, l_P$')
    ax.set_xlabel(r'Coherence length $l_{coh}$ [$l_P$]')
    ax.set_ylabel(r'$\Delta L$ [m]')
    ax.set_title(f'Distance Fluctuation (d = 1 Gpc)')
    ax.legend(fontsize=7)
    ax.set_xlim(1, 1e35)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'F-2: Domain-Boundary Phase Shift | Gate: {verdict}', fontsize=14, fontweight='bold')
    plt.tight_layout()

    plotfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_domain_phase.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {plotfile}")

    print("\n" + "=" * 70)
    print(f"F-2 COMPLETE. Gate F-2-G: {verdict}")
    print(f"  {verdict_detail}")
    print("=" * 70)


if __name__ == "__main__":
    main()
