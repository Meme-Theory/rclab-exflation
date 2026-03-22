"""
N-31Cc: BCS-Kapitza Interference Diagnostic.

Compute instantaneous BCS gap along Kapitza orbits:
    tau(t) = tau_0 + A * sin(omega * t)

For each (tau_0, A, omega), evaluate M_max(tau(t)) at 20 phase points
per cycle using cubic spline interpolation over the 9-point tau grid
from s23a_gap_equation.npz. Then compute time-averaged <M_max> and
max(M_max) over the orbit.

Parameters:
    tau_0 in {0.15, 0.18, 0.21}
    A in {0.02, 0.05, 0.08}
    omega: (1) T3 frequency (omega^2 = 8.326) and
           (2) instanton-driven effective frequency from I-1

Coupling: CONSTANT (N-31Ca-G = FAIL; density-dependent envelopes give
M_max <= 0.275, 3.6x below threshold).

The BCS gap equation at each tau gives M_max = max|eig(V_matrix)| where
V_matrix is the 16x16 Kosmann pairing matrix in the (0,0) singlet sector.
At mu=0, M_max ranges 0.077-0.154 over tau in [0, 0.5] (all far below
the BCS threshold of 1.0). At mu=+lambda_min, M_max ranges 7.7-15.0.

Gate N-31Cc-G (DECISIVE):
    PASS if time-avg <M_max> > 1.2 * M_max_static(tau_0)
    OR if max(M_max) > 1.0

Mathematical background:
    The Kapitza orbit samples the tau direction periodically. If M_max(tau)
    has a maximum near tau ~ 0.25, an orbit centered at tau_0 = 0.18 with
    A = 0.08 would reach tau = 0.26, potentially accessing higher M_max
    values. The time average includes contributions from all phases, so
    <M_max> >= M_max(tau_0) if M_max is convex (Jensen's inequality).

    For BCS: the gap equation Delta = V * Delta / (2*E) where E = sqrt(
    (epsilon-mu)^2 + |Delta|^2). The BCS instability occurs when the
    largest eigenvalue of V exceeds 1 (in units where the DOS factor
    is absorbed). M_max < 1 at all tau means no BCS instability.

    The question is whether the Kapitza oscillation can push M_max
    above the threshold dynamically, even though it is below threshold
    at every static tau value.

Input:
    tier0-computation/s23a_gap_equation.npz (V_matrix, eigenvalues, M_max at 9 tau)
    tier0-computation/s31Ba_kapitza_gate.npz (Kapitza orbit parameters)
    tier0-computation/s31Ba_instanton_kapitza.npz (instanton frequencies)

Output:
    tier0-computation/s31Cc_bcs_kapitza.{py,npz,png}

Session 31Ca -- Nazarewicz Nuclear Structure Computations
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def load_bcs_data(npz_path):
    """
    Load BCS gap equation data from s23a_gap_equation.npz.

    Returns:
        tau_values: array of 9 tau values
        M_max_mu0: M_max at mu=0 for each tau
        M_max_mup: M_max at mu=+lambda_min for each tau
        V_matrices: list of 16x16 V_matrix at each tau
        eigenvalues: list of 16-element eigenvalue arrays at each tau
        lambda_min: array of lambda_min at each tau
    """
    d = np.load(npz_path, allow_pickle=True)
    tau_values = d['tau_values']
    n_tau = len(tau_values)

    M_max_mu0 = np.array([float(d[f'M_max_full16_mu=0_{i}']) for i in range(n_tau)])
    M_max_mup = np.array([float(d[f'M_max_full16_mu=+lmin_{i}']) for i in range(n_tau)])
    M_max_mum = np.array([float(d[f'M_max_full16_mu=-lmin_{i}']) for i in range(n_tau)])
    V_matrices = [d[f'V_matrix_{i}'] for i in range(n_tau)]
    eigenvalues = [d[f'eigenvalues_{i}'] for i in range(n_tau)]
    lambda_min = np.array([float(d[f'lambda_min_{i}']) for i in range(n_tau)])

    return tau_values, M_max_mu0, M_max_mup, M_max_mum, V_matrices, eigenvalues, lambda_min


def build_M_max_splines(tau_values, M_max_mu0, M_max_mup, M_max_mum):
    """
    Build cubic spline interpolators for M_max as function of tau.

    Returns:
        spline_mu0: CubicSpline for M_max at mu=0
        spline_mup: CubicSpline for M_max at mu=+lambda_min
        spline_mum: CubicSpline for M_max at mu=-lambda_min
    """
    spline_mu0 = CubicSpline(tau_values, M_max_mu0, bc_type='natural')
    spline_mup = CubicSpline(tau_values, M_max_mup, bc_type='natural')
    spline_mum = CubicSpline(tau_values, M_max_mum, bc_type='natural')
    return spline_mu0, spline_mup, spline_mum


def kapitza_orbit(tau_0, A, omega, n_phase=20):
    """
    Generate tau values along a Kapitza orbit.

    tau(t) = tau_0 + A * sin(omega * t)
    for t in [0, 2*pi/omega) sampled at n_phase points.

    Returns:
        phases: array of phase angles [0, 2*pi)
        tau_orbit: array of tau values along orbit
    """
    phases = np.linspace(0, 2 * np.pi, n_phase, endpoint=False)
    tau_orbit = tau_0 + A * np.sin(phases)
    return phases, tau_orbit


def evaluate_orbit_M_max(spline, tau_orbit, tau_min=0.0, tau_max=0.5):
    """
    Evaluate M_max along a Kapitza orbit using cubic spline.

    Clamps tau to valid range [tau_min, tau_max].

    Returns:
        M_max_orbit: array of M_max values at each orbit point
        out_of_range: number of orbit points clamped
    """
    tau_clamped = np.clip(tau_orbit, tau_min, tau_max)
    out_of_range = np.sum(tau_orbit != tau_clamped)
    M_max_orbit = spline(tau_clamped)
    return M_max_orbit, int(out_of_range)


def main():
    print("=" * 70)
    print("N-31Cc: BCS-Kapitza Interference Diagnostic")
    print("  Coupling: CONSTANT (N-31Ca-G = FAIL)")
    print("=" * 70)

    # Load data
    bcs_path = os.path.join(os.path.dirname(__file__), "s23a_gap_equation.npz")
    kap_path = os.path.join(os.path.dirname(__file__), "s31Ba_kapitza_gate.npz")
    inst_path = os.path.join(os.path.dirname(__file__), "s31Ba_instanton_kapitza.npz")

    tau_values, M_max_mu0, M_max_mup, M_max_mum, V_matrices, eigenvalues, lambda_min = \
        load_bcs_data(bcs_path)

    dk = np.load(kap_path, allow_pickle=True)
    omega_sq_T3 = float(dk['omega_sq_T3'])
    omega_T3 = np.sqrt(omega_sq_T3)

    di = np.load(inst_path, allow_pickle=True)
    tau_inst = di['tau']
    # Use instanton-driven frequency at r=1.0 (moderate coupling)
    Gamma_inst_r1 = di['Gamma_inst_r1p0']

    print(f"\nBCS data: {len(tau_values)} tau values: {tau_values}")
    print(f"  M_max(mu=0):    [{M_max_mu0.min():.4f}, {M_max_mu0.max():.4f}]")
    print(f"  M_max(mu=+lmin):[{M_max_mup.min():.4f}, {M_max_mup.max():.4f}]")
    print(f"  M_max(mu=-lmin):[{M_max_mum.min():.4f}, {M_max_mum.max():.4f}]")
    print(f"  lambda_min:     [{lambda_min.min():.6f}, {lambda_min.max():.6f}]")
    print(f"\nT3 frequency: omega = {omega_T3:.4f} (omega^2 = {omega_sq_T3:.4f})")

    # Get instanton-driven frequency at tau_0 values
    tau_0_values = [0.15, 0.18, 0.21]
    A_values = [0.02, 0.05, 0.08]
    n_phase = 20

    # Instanton frequency at each tau_0
    inst_freq = {}
    for tau_0 in tau_0_values:
        idx = np.argmin(np.abs(tau_inst - tau_0))
        gamma_inst = Gamma_inst_r1[idx]
        inst_freq[tau_0] = gamma_inst
        print(f"  Instanton frequency at tau_0={tau_0}: Gamma_inst(r=1) = {gamma_inst:.4f}")

    # Build splines
    spline_mu0, spline_mup, spline_mum = build_M_max_splines(
        tau_values, M_max_mu0, M_max_mup, M_max_mum)

    # Also build lambda_min spline for mu tracking
    spline_lmin = CubicSpline(tau_values, lambda_min, bc_type='natural')

    # =====================================================================
    # Main computation: evaluate M_max along Kapitza orbits
    # =====================================================================
    print("\n" + "=" * 70)
    print("KAPITZA ORBIT SCAN")
    print("=" * 70)

    results = []  # list of dicts

    for tau_0 in tau_0_values:
        # Static reference
        M_static_mu0 = float(spline_mu0(tau_0))
        M_static_mup = float(spline_mup(tau_0))

        for A in A_values:
            for freq_type, omega_val in [("T3", omega_T3),
                                          ("instanton", inst_freq[tau_0])]:
                phases, tau_orbit = kapitza_orbit(tau_0, A, omega_val, n_phase)

                # Check orbit range
                tau_min_orbit = tau_orbit.min()
                tau_max_orbit = tau_orbit.max()
                in_range = (tau_min_orbit >= tau_values[0]) and (tau_max_orbit <= tau_values[-1])

                # Evaluate M_max along orbit -- mu=0 case
                M_orbit_mu0, n_clamp_0 = evaluate_orbit_M_max(
                    spline_mu0, tau_orbit, tau_values[0], tau_values[-1])
                M_avg_mu0 = np.mean(M_orbit_mu0)
                M_max_orbit_mu0 = np.max(M_orbit_mu0)
                M_min_orbit_mu0 = np.min(M_orbit_mu0)

                # mu=+lambda_min case (track lambda_min along orbit)
                M_orbit_mup, n_clamp_p = evaluate_orbit_M_max(
                    spline_mup, tau_orbit, tau_values[0], tau_values[-1])
                M_avg_mup = np.mean(M_orbit_mup)
                M_max_orbit_mup = np.max(M_orbit_mup)

                # mu=-lambda_min case
                M_orbit_mum, n_clamp_m = evaluate_orbit_M_max(
                    spline_mum, tau_orbit, tau_values[0], tau_values[-1])
                M_avg_mum = np.mean(M_orbit_mum)
                M_max_orbit_mum = np.max(M_orbit_mum)

                # Enhancement ratios
                ratio_avg_mu0 = M_avg_mu0 / M_static_mu0 if M_static_mu0 > 0 else np.inf
                ratio_max_mu0 = M_max_orbit_mu0 / M_static_mu0 if M_static_mu0 > 0 else np.inf

                result = {
                    'tau_0': tau_0,
                    'A': A,
                    'freq_type': freq_type,
                    'omega': omega_val,
                    'M_static_mu0': M_static_mu0,
                    'M_avg_mu0': M_avg_mu0,
                    'M_max_mu0': M_max_orbit_mu0,
                    'M_min_mu0': M_min_orbit_mu0,
                    'ratio_avg_mu0': ratio_avg_mu0,
                    'ratio_max_mu0': ratio_max_mu0,
                    'M_static_mup': M_static_mup,
                    'M_avg_mup': M_avg_mup,
                    'M_max_mup': M_max_orbit_mup,
                    'M_avg_mum': M_avg_mum,
                    'M_max_mum': M_max_orbit_mum,
                    'tau_range': (tau_min_orbit, tau_max_orbit),
                    'n_clamped': n_clamp_0,
                    'phases': phases,
                    'tau_orbit': tau_orbit,
                    'M_orbit_mu0': M_orbit_mu0,
                    'M_orbit_mup': M_orbit_mup,
                }
                results.append(result)

    # =====================================================================
    # Print results table
    # =====================================================================
    print("\n--- mu=0 (physically self-consistent) ---")
    print(f"{'tau_0':>5} {'A':>5} {'freq':>10} {'omega':>7} "
          f"{'M_static':>8} {'<M>':>8} {'max(M)':>8} "
          f"{'<M>/static':>10} {'max/static':>10} {'tau_range':>16}")

    for r in results:
        print(f"{r['tau_0']:5.2f} {r['A']:5.2f} {r['freq_type']:>10} {r['omega']:7.3f} "
              f"{r['M_static_mu0']:8.5f} {r['M_avg_mu0']:8.5f} {r['M_max_mu0']:8.5f} "
              f"{r['ratio_avg_mu0']:10.4f} {r['ratio_max_mu0']:10.4f} "
              f"[{r['tau_range'][0]:.3f},{r['tau_range'][1]:.3f}]")

    print("\n--- mu=+lambda_min (requires substrate) ---")
    print(f"{'tau_0':>5} {'A':>5} {'freq':>10} {'omega':>7} "
          f"{'M_static':>8} {'<M>':>8} {'max(M)':>8}")

    for r in results:
        print(f"{r['tau_0']:5.2f} {r['A']:5.2f} {r['freq_type']:>10} {r['omega']:7.3f} "
              f"{r['M_static_mup']:8.3f} {r['M_avg_mup']:8.3f} {r['M_max_mup']:8.3f}")

    # =====================================================================
    # Gate N-31Cc-G Assessment
    # =====================================================================
    print("\n" + "=" * 70)
    print("GATE N-31Cc-G ASSESSMENT (DECISIVE)")
    print("=" * 70)

    # Criteria: PASS if:
    #   (a) time-avg <M_max> > 1.2 * M_max_static for ANY (tau_0, A, omega), OR
    #   (b) max(M_max) > 1.0 for ANY (tau_0, A, omega)
    # Both evaluated at mu=0 (the physically self-consistent case).

    best_ratio_avg = max(r['ratio_avg_mu0'] for r in results)
    best_ratio_max = max(r['ratio_max_mu0'] for r in results)
    best_M_max = max(r['M_max_mu0'] for r in results)
    best_M_avg = max(r['M_avg_mu0'] for r in results)

    # Find best configurations
    best_avg_r = max(results, key=lambda r: r['ratio_avg_mu0'])
    best_max_r = max(results, key=lambda r: r['M_max_mu0'])

    print(f"\n  Criterion (a): <M_max>/M_static > 1.2")
    print(f"    Best ratio: {best_ratio_avg:.4f} at tau_0={best_avg_r['tau_0']}, "
          f"A={best_avg_r['A']}, freq={best_avg_r['freq_type']}")
    print(f"    <M_max> = {best_avg_r['M_avg_mu0']:.6f}, M_static = {best_avg_r['M_static_mu0']:.6f}")
    criterion_a = best_ratio_avg > 1.2

    print(f"\n  Criterion (b): max(M_max) > 1.0")
    print(f"    Best max(M_max): {best_M_max:.6f} at tau_0={best_max_r['tau_0']}, "
          f"A={best_max_r['A']}, freq={best_max_r['freq_type']}")
    criterion_b = best_M_max > 1.0

    if criterion_a or criterion_b:
        verdict = "PASS"
        if criterion_a and criterion_b:
            verdict_detail = (f"Both criteria met. <M>/static = {best_ratio_avg:.3f} > 1.2 "
                               f"AND max(M) = {best_M_max:.4f} > 1.0")
        elif criterion_a:
            verdict_detail = (f"Criterion (a) met: <M>/static = {best_ratio_avg:.3f} > 1.2. "
                               f"max(M) = {best_M_max:.4f} < 1.0 (criterion b fails)")
        else:
            verdict_detail = (f"Criterion (b) met: max(M) = {best_M_max:.4f} > 1.0. "
                               f"<M>/static = {best_ratio_avg:.3f} < 1.2 (criterion a fails)")
    else:
        verdict = "DOES NOT FIRE"
        verdict_detail = (f"Neither criterion met. <M>/static = {best_ratio_avg:.4f} (need >1.2), "
                           f"max(M) = {best_M_max:.6f} (need >1.0). "
                           f"BCS gap at mu=0 remains 7-13x below threshold along ALL Kapitza orbits.")

    print(f"\n  Gate N-31Cc-G verdict: {verdict}")
    print(f"  Detail: {verdict_detail}")

    # Diagnostic: how far from threshold?
    factor_below = 1.0 / best_M_max if best_M_max > 0 else np.inf
    print(f"\n  Distance to threshold: max(M_max) is {factor_below:.1f}x below 1.0")
    print(f"  Enhancement from oscillation: {(best_ratio_avg - 1)*100:.2f}% average, "
          f"{(best_ratio_max - 1)*100:.2f}% peak")

    # Also report mu=+lmin case for completeness
    best_mup_max = max(r['M_max_mup'] for r in results)
    print(f"\n  [Diagnostic] mu=+lambda_min case: max(M_max) = {best_mup_max:.3f} "
          f"(always above threshold, but requires substrate-provided mu)")

    # =====================================================================
    # Save
    # =====================================================================
    outfile = os.path.join(os.path.dirname(__file__), "s31Cc_bcs_kapitza.npz")
    save_dict = {
        'tau_0_values': np.array(tau_0_values),
        'A_values': np.array(A_values),
        'omega_T3': np.array(omega_T3),
        'omega_sq_T3': np.array(omega_sq_T3),
        'n_phase': np.array(n_phase),
        'tau_bcs': tau_values,
        'M_max_mu0_bcs': M_max_mu0,
        'M_max_mup_bcs': M_max_mup,
        'M_max_mum_bcs': M_max_mum,
        'lambda_min_bcs': lambda_min,
        'best_ratio_avg': np.array(best_ratio_avg),
        'best_ratio_max': np.array(best_ratio_max),
        'best_M_max_mu0': np.array(best_M_max),
        'best_M_avg_mu0': np.array(best_M_avg),
        'best_mup_max': np.array(best_mup_max),
        'verdict': np.array(verdict),
        'coupling_type': np.array('constant'),
    }

    # Save per-configuration results
    for i, r in enumerate(results):
        prefix = f"cfg{i}_"
        save_dict[prefix + "tau_0"] = np.array(r['tau_0'])
        save_dict[prefix + "A"] = np.array(r['A'])
        save_dict[prefix + "freq_type"] = np.array(r['freq_type'])
        save_dict[prefix + "omega"] = np.array(r['omega'])
        save_dict[prefix + "M_avg_mu0"] = np.array(r['M_avg_mu0'])
        save_dict[prefix + "M_max_mu0"] = np.array(r['M_max_mu0'])
        save_dict[prefix + "ratio_avg"] = np.array(r['ratio_avg_mu0'])
        save_dict[prefix + "M_orbit_mu0"] = r['M_orbit_mu0']
        save_dict[prefix + "tau_orbit"] = r['tau_orbit']

    # Save instanton frequencies used
    for tau_0 in tau_0_values:
        save_dict[f'inst_freq_tau{tau_0:.2f}'] = np.array(inst_freq[tau_0])

    np.savez_compressed(outfile, **save_dict)
    print(f"\n  Saved: {outfile}")

    # =====================================================================
    # Plot
    # =====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: M_max(tau) spline with BCS data points (mu=0)
    ax = axes[0, 0]
    tau_fine = np.linspace(tau_values[0], tau_values[-1], 200)
    ax.plot(tau_fine, spline_mu0(tau_fine), 'b-', lw=2, label=r'$M_{max}(\mu=0)$ spline')
    ax.plot(tau_values, M_max_mu0, 'bo', ms=8, zorder=5)
    ax.axhline(1.0, color='r', ls='--', lw=1.5, label='BCS threshold')
    # Mark orbit ranges
    colors_tau = {0.15: 'green', 0.18: 'red', 0.21: 'orange'}
    for tau_0 in tau_0_values:
        for A in A_values:
            ax.axvspan(tau_0 - A, tau_0 + A, alpha=0.05, color=colors_tau[tau_0])
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$M_{max}$')
    ax.set_title(r'BCS Pairing Strength ($\mu=0$, constant coupling)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 0.2)

    # Panel 2: M_max along representative orbits (tau_0=0.18, all A, both freqs)
    ax = axes[0, 1]
    for r in results:
        if r['tau_0'] == 0.18:
            ls = '-' if r['freq_type'] == 'T3' else '--'
            label = f"A={r['A']}, {r['freq_type']}"
            ax.plot(r['phases'] / np.pi, r['M_orbit_mu0'], ls, lw=1.5, label=label)
    ax.axhline(float(spline_mu0(0.18)), color='gray', ls=':', lw=1, label='static')
    ax.axhline(1.0, color='r', ls='--', lw=1, alpha=0.5)
    ax.set_xlabel(r'Phase / $\pi$')
    ax.set_ylabel(r'$M_{max}$')
    ax.set_title(r'$M_{max}$ Along Kapitza Orbit ($\tau_0=0.18$, $\mu=0$)')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 3: Enhancement ratio <M_max>/M_static for all configurations
    ax = axes[1, 0]
    # Group by frequency type
    for freq_type, marker, color in [('T3', 'o', 'blue'), ('instanton', 's', 'red')]:
        xs = []
        ys = []
        labels = []
        for r in results:
            if r['freq_type'] == freq_type:
                xs.append(r['A'])
                ys.append(r['ratio_avg_mu0'])
                labels.append(f"$\\tau_0={r['tau_0']}$")
        # Color by tau_0
        for tau_0, c in colors_tau.items():
            x_t = [xs[i] for i, r in enumerate([r for r in results if r['freq_type'] == freq_type])
                   if r['tau_0'] == tau_0]
            y_t = [ys[i] for i, r in enumerate([r for r in results if r['freq_type'] == freq_type])
                   if r['tau_0'] == tau_0]
            if x_t:
                lbl = f"{freq_type}, $\\tau_0={tau_0}$"
                ax.plot(x_t, y_t, marker=marker, color=c, ls='-', lw=1.5,
                         label=lbl, ms=6)
    ax.axhline(1.2, color='r', ls='--', lw=1.5, label='Gate threshold (1.2x)')
    ax.axhline(1.0, color='gray', ls=':', lw=1)
    ax.set_xlabel('Amplitude A')
    ax.set_ylabel(r'$\langle M_{max} \rangle / M_{static}$')
    ax.set_title('Enhancement Ratio vs Amplitude')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 4: mu=+lmin case for comparison (diagnostic)
    ax = axes[1, 1]
    ax.plot(tau_fine, spline_mup(tau_fine), 'r-', lw=2, label=r'$M_{max}(\mu=+\lambda_{min})$')
    ax.plot(tau_fine, spline_mum(tau_fine), 'b-', lw=2, label=r'$M_{max}(\mu=-\lambda_{min})$')
    ax.plot(tau_fine, spline_mu0(tau_fine) * 10, 'k--', lw=1,
             label=r'$M_{max}(\mu=0) \times 10$')
    ax.plot(tau_values, M_max_mup, 'ro', ms=6)
    ax.plot(tau_values, M_max_mum, 'bo', ms=6)
    ax.axhline(1.0, color='gray', ls='--', lw=1, label='BCS threshold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$M_{max}$')
    ax.set_title(r'$M_{max}$ at Different $\mu$ (diagnostic)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'N-31Cc: BCS-Kapitza Interference | Gate: {verdict}',
                  fontsize=14, fontweight='bold')
    plt.tight_layout()

    plotfile = os.path.join(os.path.dirname(__file__), "s31Cc_bcs_kapitza.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {plotfile}")

    print("\n" + "=" * 70)
    print(f"N-31Cc COMPLETE. Gate N-31Cc-G: {verdict}")
    print(f"  {verdict_detail}")
    print("=" * 70)


if __name__ == "__main__":
    main()
