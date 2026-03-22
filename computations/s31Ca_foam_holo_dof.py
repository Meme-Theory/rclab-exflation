"""
F-3: Holographic DOF count on Jensen-deformed SU(3).

Sort eigenvalues |lambda_k| of D_K, compute cumulative mode count N(Lambda)
(number of eigenvalues with |lambda| <= Lambda), and fit N = A * Lambda^alpha.

Compare alpha to:
  - Volume law: alpha = d/2 = 3 (for d=6, Weyl's law on Riemannian manifold)
  - Area law: alpha = (d-1)/2 = 5/2 (if holographic)
  - Holographic foam: alpha = 2/3 (Ng's holographic foam DOF scaling)
  - CDT: alpha = 1 (d_s=2 spectral dimension)

Cross-reference with F-1 spectral dimension: if d_s is the UV spectral
dimension, the eigenvalue counting should scale as N ~ Lambda^{d_s/2}.

Mathematical background:
  Weyl's law on a d-dimensional compact Riemannian manifold (M, g):
    N(Lambda) ~ Vol(M) * omega_d / (2*pi)^d * Lambda^d
  where omega_d is the volume of the unit d-ball and Lambda is the
  eigenvalue cutoff of the Laplacian Delta = D^2.

  For the Dirac operator, eigenvalues come in +/- pairs, and the Weyl
  asymptotic formula gives:
    N_Dirac(Lambda) ~ 2^{[d/2]} * Vol(M) * omega_d / (2*pi)^d * Lambda^d
  where d is the manifold dimension and [d/2] counts the spinor rank.

  On SU(3) (d=6), with spinor dimension 2^3 = 8 (from Cliff(6)) but
  using Cliff(8) (KO-dim 8 spinors, dim=16), the expected scaling is:
    N(Lambda) ~ C * Lambda^6  (for the Laplacian: Weyl)
  or equivalently
    N(|lambda_D|) ~ C * |lambda_D|^6  (for the Dirac eigenvalues)

  But the SPECTRAL dimension d_s is defined from the heat kernel, and
  the relationship is N ~ Lambda^{d_s} for the Dirac eigenvalue |lambda|.

  Wait -- careful. The heat kernel K(t) = sum exp(-t*lambda^2). For large
  Lambda cutoff, K(t) ~ integral_0^Lambda dN(lambda') * exp(-t*lambda'^2).
  If N ~ Lambda^alpha, then K(t) ~ t^{-alpha/2} for small t, giving
  d_s = alpha. So the spectral dimension EQUALS the growth exponent
  of the cumulative mode count.

Gate F-3-G: INFORMATIVE (characterizes the DOF scaling, no pass/fail threshold).

Input: tier0-computation/tier1_dirac_spectrum.py (spectrum computation)
Output: s31Ca_foam_holo_dof.{npz,png}

Session 31Ca -- Quantum Foam Diagnostics
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, collect_spectrum
)


def power_law(x, A, alpha):
    """N = A * Lambda^alpha"""
    return A * x**alpha


def get_spectrum_with_mults(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Get sorted |eigenvalues| with Peter-Weyl multiplicities.

    Returns:
        abs_evals: sorted array of |eigenvalue| (distinct)
        mults: corresponding Peter-Weyl multiplicities
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
    mults = np.array(mults, dtype=float)
    order = np.argsort(abs_evals)
    return abs_evals[order], mults[order]


def compute_cumulative_N(abs_evals, mults):
    """
    Compute cumulative mode count N(Lambda) = number of |eigenvalues| <= Lambda,
    including Peter-Weyl multiplicities.

    Returns:
        Lambda_vals: the sorted |eigenvalue| thresholds
        N_vals: cumulative count at each threshold
    """
    cum_mults = np.cumsum(mults)
    return abs_evals, cum_mults


def main():
    print("=" * 70)
    print("F-3: Holographic DOF Count on Jensen-Deformed SU(3)")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Test at multiple tau values
    tau_test = [0.0, 0.18, 0.35, 0.50]
    max_pq = 6

    results = {}

    for tau in tau_test:
        print(f"\n--- tau = {tau:.2f} ---")
        abs_evals, mults = get_spectrum_with_mults(tau, gens, f_abc, gammas, max_pq)

        # Remove zero eigenvalues for fitting (log-log fails at zero)
        nonzero = abs_evals > 1e-10
        evals_nz = abs_evals[nonzero]
        mults_nz = mults[nonzero]

        Lambda_vals, N_vals = compute_cumulative_N(evals_nz, mults_nz)

        n_distinct = len(evals_nz)
        n_total = int(np.sum(mults_nz))
        lambda_max = evals_nz[-1] if len(evals_nz) > 0 else 0
        lambda_min = evals_nz[0] if len(evals_nz) > 0 else 0

        print(f"  {n_distinct} distinct nonzero eigenvalues, {n_total} total modes")
        print(f"  |lambda| range: [{lambda_min:.4f}, {lambda_max:.4f}]")

        # Fit power law N = A * Lambda^alpha
        # Use the upper 80% of the eigenvalue range for Weyl-regime fit
        fit_mask = Lambda_vals > 0.2 * lambda_max  # upper regime
        if np.sum(fit_mask) > 5:
            try:
                popt, pcov = curve_fit(power_law, Lambda_vals[fit_mask],
                                        N_vals[fit_mask],
                                        p0=[1.0, 6.0], maxfev=10000)
                A_fit, alpha_fit = popt
                alpha_err = np.sqrt(pcov[1, 1]) if pcov[1, 1] > 0 else 0
            except RuntimeError:
                alpha_fit = np.nan
                A_fit = np.nan
                alpha_err = np.nan
        else:
            alpha_fit = np.nan
            A_fit = np.nan
            alpha_err = np.nan

        # Also fit on full range
        if len(Lambda_vals) > 5:
            try:
                popt_full, pcov_full = curve_fit(power_law, Lambda_vals,
                                                  N_vals,
                                                  p0=[1.0, 6.0], maxfev=10000)
                A_full, alpha_full = popt_full
                alpha_full_err = np.sqrt(pcov_full[1, 1]) if pcov_full[1, 1] > 0 else 0
            except RuntimeError:
                alpha_full = np.nan
                A_full = np.nan
                alpha_full_err = np.nan
        else:
            alpha_full = np.nan
            A_full = np.nan
            alpha_full_err = np.nan

        # Log-log slope (local) via finite differences
        if len(Lambda_vals) > 2:
            log_L = np.log(Lambda_vals)
            log_N = np.log(N_vals)
            local_alpha = np.diff(log_N) / np.diff(log_L)
            L_mid = np.exp(0.5 * (log_L[:-1] + log_L[1:]))
        else:
            local_alpha = np.array([])
            L_mid = np.array([])

        print(f"  Power-law fit (upper 80%): N = {A_fit:.2f} * Lambda^{alpha_fit:.3f} +/- {alpha_err:.3f}")
        print(f"  Power-law fit (full range): N = {A_full:.2f} * Lambda^{alpha_full:.3f} +/- {alpha_full_err:.3f}")

        # Comparison to theoretical predictions
        print(f"  Weyl (d=6):     alpha = 6.0")
        print(f"  d_s Weyl (d=6): alpha = 3.0 (for heat kernel d_s = 2*alpha)")
        print(f"  Area law (d=5): alpha = 5.0")
        print(f"  Holo foam:      alpha = 2/3 = 0.667")
        print(f"  CDT (d_s=2):    alpha = 2.0")

        # The spectral dimension relation: d_s = 2 * (effective alpha in N ~ Lambda^alpha for Dirac)
        # Wait -- N ~ Lambda^alpha for Dirac eigenvalues means
        # K(t) ~ integral Lambda^{alpha-1} exp(-t*Lambda^2) dLambda ~ t^{-alpha/2}
        # so d_s = alpha.
        # For Weyl's law on 6D: N_Dirac ~ Lambda^6, so d_s -> 6 at UV.
        # The d_s(t) from F-1 should approach alpha from this fit.
        d_s_from_alpha = alpha_fit
        print(f"  Implied d_s from alpha: {d_s_from_alpha:.3f}")

        results[tau] = {
            'Lambda_vals': Lambda_vals,
            'N_vals': N_vals,
            'alpha_fit': alpha_fit,
            'alpha_err': alpha_err,
            'A_fit': A_fit,
            'alpha_full': alpha_full,
            'alpha_full_err': alpha_full_err,
            'A_full': A_full,
            'local_alpha': local_alpha,
            'L_mid': L_mid,
            'n_distinct': n_distinct,
            'n_total': n_total,
            'lambda_min': lambda_min,
            'lambda_max': lambda_max,
        }

    # =====================================================================
    # Gate F-3-G Assessment
    # =====================================================================
    print("\n" + "=" * 70)
    print("GATE F-3-G ASSESSMENT (INFORMATIVE)")
    print("=" * 70)

    alpha_0_18 = results[0.18]['alpha_fit']
    alpha_0_00 = results[0.0]['alpha_fit']
    alpha_0_50 = results[0.50]['alpha_fit']

    print(f"\n  Growth exponent alpha at key tau values:")
    for tau in tau_test:
        r = results[tau]
        print(f"    tau={tau:.2f}: alpha = {r['alpha_fit']:.3f} +/- {r['alpha_err']:.3f} "
              f"(full-range: {r['alpha_full']:.3f} +/- {r['alpha_full_err']:.3f})")

    print(f"\n  Interpretation:")
    if alpha_0_18 > 5.0:
        print(f"    alpha ~ {alpha_0_18:.1f} >> 2: VOLUME LAW scaling (Weyl). "
              f"No holographic reduction.")
        print(f"    DOF counting is standard Riemannian, not holographic.")
        scaling_type = "VOLUME"
    elif alpha_0_18 > 2.5:
        print(f"    alpha ~ {alpha_0_18:.1f}: between area and volume law. "
              f"Intermediate scaling.")
        scaling_type = "INTERMEDIATE"
    elif alpha_0_18 > 1.5:
        print(f"    alpha ~ {alpha_0_18:.1f}: CDT-like scaling. "
              f"Possible holographic reduction.")
        scaling_type = "CDT-LIKE"
    else:
        print(f"    alpha ~ {alpha_0_18:.1f}: sub-CDT scaling. "
              f"Anomalous spectral behavior.")
        scaling_type = "ANOMALOUS"

    verdict = "INFORMATIVE"
    verdict_detail = (f"N(Lambda) ~ Lambda^{alpha_0_18:.2f} at tau=0.18. "
                       f"Scaling type: {scaling_type}. "
                       f"Cross-ref F-1: d_s(UV) should equal alpha.")

    print(f"\n  Gate F-3-G verdict: {verdict}")
    print(f"  Detail: {verdict_detail}")

    # =====================================================================
    # Save
    # =====================================================================
    outfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_holo_dof.npz")
    save_dict = {
        'tau_test': np.array(tau_test),
        'verdict': np.array(verdict),
        'scaling_type': np.array(scaling_type),
    }
    for tau in tau_test:
        r = results[tau]
        prefix = f"tau{tau:.2f}_"
        save_dict[prefix + "Lambda_vals"] = r['Lambda_vals']
        save_dict[prefix + "N_vals"] = r['N_vals']
        save_dict[prefix + "alpha_fit"] = np.array(r['alpha_fit'])
        save_dict[prefix + "alpha_err"] = np.array(r['alpha_err'])
        save_dict[prefix + "A_fit"] = np.array(r['A_fit'])
        save_dict[prefix + "alpha_full"] = np.array(r['alpha_full'])
        save_dict[prefix + "n_total"] = np.array(r['n_total'])
        if len(r['local_alpha']) > 0:
            save_dict[prefix + "local_alpha"] = r['local_alpha']
            save_dict[prefix + "L_mid"] = r['L_mid']

    np.savez_compressed(outfile, **save_dict)
    print(f"\n  Saved: {outfile}")

    # =====================================================================
    # Plot
    # =====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    colors = {'0.00': 'blue', '0.18': 'red', '0.35': 'green', '0.50': 'purple'}

    # Panel 1: N(Lambda) vs Lambda (log-log) with fits
    ax = axes[0, 0]
    for tau in tau_test:
        r = results[tau]
        c = colors[f'{tau:.2f}']
        ax.loglog(r['Lambda_vals'], r['N_vals'], 'o-', color=c, ms=3, lw=1.5,
                   label=f'$\\tau={tau:.2f}$, $\\alpha={r["alpha_fit"]:.2f}$')
        if not np.isnan(r['alpha_fit']):
            L_fit = np.linspace(r['Lambda_vals'].min(), r['Lambda_vals'].max(), 100)
            ax.loglog(L_fit, power_law(L_fit, r['A_fit'], r['alpha_fit']),
                       '--', color=c, lw=1, alpha=0.6)
    ax.set_xlabel(r'$|\lambda|$ (Dirac eigenvalue)')
    ax.set_ylabel(r'$N(|\lambda|)$ (cumulative count)')
    ax.set_title(r'Cumulative Mode Count $N(\Lambda)$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Local slope alpha(Lambda)
    ax = axes[0, 1]
    for tau in tau_test:
        r = results[tau]
        if len(r['local_alpha']) > 0:
            c = colors[f'{tau:.2f}']
            ax.semilogx(r['L_mid'], r['local_alpha'], '-', color=c, lw=1.5,
                         label=f'$\\tau={tau:.2f}$')
    ax.axhline(6.0, color='orange', ls='--', lw=1, alpha=0.7, label='Weyl (d=6)')
    ax.axhline(3.0, color='brown', ls='--', lw=1, alpha=0.7, label=r'$d_s=6$ heat kernel')
    ax.axhline(2.0, color='green', ls='--', lw=1, alpha=0.7, label='CDT (d_s=2)')
    ax.axhline(0.667, color='purple', ls='--', lw=1, alpha=0.5, label='Holographic foam')
    ax.set_xlabel(r'$|\lambda|$')
    ax.set_ylabel(r'Local slope $\alpha(\Lambda)$')
    ax.set_title('Local Growth Exponent')
    ax.legend(fontsize=7, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-1, 15)

    # Panel 3: alpha_fit vs tau
    ax = axes[1, 0]
    alphas = [results[tau]['alpha_fit'] for tau in tau_test]
    alpha_errs = [results[tau]['alpha_err'] for tau in tau_test]
    ax.errorbar(tau_test, alphas, yerr=alpha_errs, fmt='ko-', lw=2, capsize=5)
    ax.axhline(6.0, color='orange', ls='--', lw=1, label='Weyl (d=6)')
    ax.axhline(2.0, color='green', ls='--', lw=1, label='CDT')
    ax.axhline(0.667, color='purple', ls='--', lw=1, alpha=0.5, label='Holographic')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\alpha$ (growth exponent)')
    ax.set_title(r'Growth Exponent vs $\tau$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: N(Lambda) at tau=0.18 with reference scalings
    ax = axes[1, 1]
    r18 = results[0.18]
    L = r18['Lambda_vals']
    ax.loglog(L, r18['N_vals'], 'ro-', ms=3, lw=2, label=f'Data ($\\tau=0.18$)')
    # Reference lines
    L_ref = np.linspace(L.min(), L.max(), 100)
    N_max = r18['N_vals'][-1]
    L_max = L[-1]
    for alpha_ref, name, color in [(6.0, 'Weyl (d=6)', 'orange'),
                                    (3.0, 'd_s=6 heat', 'brown'),
                                    (2.0, 'CDT', 'green'),
                                    (0.667, 'Holographic', 'purple')]:
        # Normalize to match at L_max
        A_ref = N_max / L_max**alpha_ref
        ax.loglog(L_ref, A_ref * L_ref**alpha_ref, '--', color=color, lw=1,
                   alpha=0.7, label=f'{name} ($\\alpha={alpha_ref}$)')
    ax.set_xlabel(r'$|\lambda|$')
    ax.set_ylabel(r'$N(|\lambda|)$')
    ax.set_title(r'Mode Count at $\tau=0.18$ vs Theory')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'F-3: Holographic DOF Count | {scaling_type} scaling', fontsize=14, fontweight='bold')
    plt.tight_layout()

    plotfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_holo_dof.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {plotfile}")

    print("\n" + "=" * 70)
    print(f"F-3 COMPLETE. Gate F-3-G: {verdict}")
    print(f"  {verdict_detail}")
    print("=" * 70)


if __name__ == "__main__":
    main()
