#!/usr/bin/env python3
"""
Session 32b Task #3: PARAM-B2 -- Mathieu Stability for B2 Flat-Band Modes

CONDITIONAL on U-32a POSITIVE (confirmed: V_{B3,B2,B1} = +0.049).

Computes the Mathieu stability diagram for B2 flat-band modes under periodic
instanton drive. The Mathieu equation:

    d^2 x / dt^2 + [a - 2q cos(2t)] x = 0

governs parametric resonance. For B2 modes with natural frequency omega_B2 ~ 0.845
and instanton drive, the Mathieu parameters are:

    a = (omega_B2 / omega_drive)^2
    q = A * d^2V/dtau^2|_B2 / (2 * omega_drive^2)

If (a, q) falls in an unstable band: B2 occupation grows exponentially.

Gate PB-32b: PASS if any B2 mode in unstable band, FAIL if all stable.

Author: sim (phonon-exflation-sim)
Date: 2026-03-03
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import mathieu_a, mathieu_b
from pathlib import Path

# ============================================================
# Configuration
# ============================================================
DATA_DIR = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")
INSTANTON_FILE = DATA_DIR / "s31Ba_instanton_kapitza.npz"
UMKLAPP_FILE = DATA_DIR / "s32a_umklapp_vertex.npz"
OUTPUT_NPZ = DATA_DIR / "s32b_param_b2_mathieu.npz"
OUTPUT_PNG = DATA_DIR / "s32b_param_b2_mathieu.png"


# ============================================================
# Module 1: Mathieu Stability Boundaries
# ============================================================
def compute_mathieu_boundaries(q_max=5.0, n_q=500, n_orders=6):
    """Compute the Mathieu stability boundaries a_n(q) and b_n(q).

    The stable regions of the Mathieu equation are bounded by the
    characteristic values a_n(q) and b_n(q). The first unstable tongue
    is between a_0(q) and b_1(q), centered at a=0. The n-th tongue is
    centered at a = n^2.

    Parameters
    ----------
    q_max : float
        Maximum q to compute.
    n_q : int
        Number of q points.
    n_orders : int
        Number of Mathieu orders to compute.

    Returns
    -------
    q_arr : ndarray
        q values.
    a_boundaries : dict
        a_n(q) for n = 0, 1, 2, ...
    b_boundaries : dict
        b_n(q) for n = 1, 2, 3, ...
    """
    q_arr = np.linspace(0, q_max, n_q)
    a_boundaries = {}
    b_boundaries = {}

    for n in range(n_orders):
        a_vals = np.array([mathieu_a(n, q) for q in q_arr])
        a_boundaries[n] = a_vals

    for n in range(1, n_orders):
        b_vals = np.array([mathieu_b(n, q) for q in q_arr])
        b_boundaries[n] = b_vals

    return q_arr, a_boundaries, b_boundaries


def is_in_unstable_band(a, q, a_boundaries, b_boundaries, q_arr):
    """Check if (a, q) falls in an unstable band.

    Unstable bands are the regions between:
    - b_n(q) and a_n(q) for n >= 1 (the nth tongue)
    - Below a_0(q) (always unstable for large enough q)

    Parameters
    ----------
    a, q : float
        Mathieu parameters.

    Returns
    -------
    unstable : bool
    tongue_number : int or None
        Which tongue the point is in (0-based).
    """
    # Interpolate boundaries at this q
    if q > q_arr[-1] or q < q_arr[0]:
        return False, None

    # Find the bands
    for n in range(1, len(a_boundaries)):
        if n not in b_boundaries:
            continue
        a_n = np.interp(q, q_arr, a_boundaries[n])
        b_n = np.interp(q, q_arr, b_boundaries[n])

        # Unstable band: b_n < a < a_n (for the nth tongue)
        # Actually: the instability tongue n is between a_{n-1}(q) and b_n(q) for q>0
        # Standard: tongue n opens at a = n^2 for q=0
        # Between b_n(q) and a_n(q): unstable
        if b_n < a < a_n:
            return True, n

    # Also check the zeroth band: a < a_0(q)
    a_0 = np.interp(q, q_arr, a_boundaries[0])
    if a < a_0:
        return True, 0

    return False, None


# ============================================================
# Module 2: B2 Mode Parameters
# ============================================================
def compute_b2_mathieu_params():
    """Compute Mathieu (a, q) parameters for B2 modes.

    The B2 mode is modeled as an oscillator with natural frequency omega_B2
    driven by periodic instanton tunneling events at rate Gamma_inst.

    The mapping to Mathieu parameters:
        omega_drive = Gamma_inst (instanton rate as the driving frequency)
        a = (omega_B2 / (omega_drive/2))^2   (natural freq / half drive freq)
        q = A_eff / omega_drive^2             (drive amplitude / drive freq^2)

    where A_eff is the effective drive amplitude coupling to B2 modes.
    """
    # Load data
    inst = np.load(INSTANTON_FILE, allow_pickle=True)
    umk = np.load(UMKLAPP_FILE, allow_pickle=True)

    tau_inst = inst['tau']
    B2_mean = umk['B2_mean']  # B2 eigenvalue at each tau
    tau_evals = umk['tau_values']

    # B2 natural frequency at the operating point tau ~ 0.18-0.20
    # omega_B2 = B2 eigenvalue = mass of the mode
    omega_B2 = np.interp(0.19, tau_evals, B2_mean)

    # d^2V/dtau^2 at the operating point (from instanton data)
    d2V = inst['d2V_dtau2']

    # B2 curvature: how much the B2 eigenvalue curves with tau
    # d^2(lambda_B2)/dtau^2 at tau=0.20
    # From B2_mean: central difference
    idx = 3  # tau=0.20
    h1 = tau_evals[idx] - tau_evals[idx-1]
    h2 = tau_evals[idx+1] - tau_evals[idx]
    d2_B2 = 2 * (B2_mean[idx+1]*h1 - B2_mean[idx]*(h1+h2) + B2_mean[idx-1]*h2) / (h1*h2*(h1+h2))
    print(f"  d^2(lambda_B2)/dtau^2 at tau=0.20: {d2_B2:.6f}")

    results = {}
    coupling_ratios = inst['coupling_ratios']

    for r_label, r_val in zip(['0p1', '0p3', '0p5', '1p0', '2p0', '5p0'], coupling_ratios):
        Gamma = inst[f'Gamma_inst_r{r_label}']
        S = inst[f'S_inst_r{r_label}']

        # At the operating point tau ~ 0.18
        idx_018 = np.argmin(np.abs(tau_inst - 0.18))
        Gamma_018 = Gamma[idx_018]
        S_018 = S[idx_018]

        if Gamma_018 <= 0:
            continue

        # Drive frequency = instanton rate
        omega_drive = Gamma_018

        # Mathieu parameter a: natural frequency ratio squared
        # Standard Mathieu: x'' + (a - 2q cos(2t)) x = 0
        # Physical: x'' + omega_B2^2 x = -A cos(omega_d t) * x
        # Rescale t -> omega_d * t / 2:
        # x'' + (2*omega_B2/omega_d)^2 x = -4A/omega_d^2 cos(2t') x
        # => a = (2*omega_B2/omega_d)^2
        # => q = 2*A_eff/omega_d^2

        a_param = (2.0 * omega_B2 / omega_drive)**2

        # Drive amplitude: the instanton tunneling modulates the B2 eigenvalue
        # A_eff ~ |d^2(lambda_B2)/dtau^2| * (instanton amplitude)^2 / 2
        # The instanton amplitude ~ 1/Gamma (characteristic tunneling distance)
        # More precisely: A_eff = d2_B2 * (delta_tau_inst)^2
        # where delta_tau_inst is the instanton displacement in tau-space

        # From the instanton action: the instanton connects tau_min to tau_max
        # The instanton amplitude in tau-space: delta_tau ~ sqrt(2*|S|/d2V)
        d2V_018 = np.interp(0.18, tau_inst, d2V)
        if abs(d2V_018) > 1e-10:
            delta_tau = np.sqrt(2.0 * abs(S_018) / abs(d2V_018))
        else:
            delta_tau = 0.1

        A_eff = abs(d2_B2) * delta_tau**2

        # Mathieu q parameter
        q_param = 2.0 * A_eff / omega_drive**2

        # Also try direct mapping: q = B2_curvature * instanton_amplitude / omega_d^2
        # Alternative: use the Kapitza-style formula
        # q_alt = |d2V/dtau2| * A^2 / (4 * omega_drive^2)
        A_kapitza = delta_tau
        q_kapitza = abs(d2V_018) * A_kapitza**2 / (4 * omega_drive**2)

        results[r_val] = {
            'r_label': r_label,
            'Gamma_018': Gamma_018,
            'S_018': S_018,
            'omega_drive': omega_drive,
            'a': a_param,
            'q': q_param,
            'q_kapitza': q_kapitza,
            'delta_tau': delta_tau,
            'A_eff': A_eff,
        }

    return omega_B2, d2_B2, results


# ============================================================
# Module 3: Main
# ============================================================
def main():
    print("=" * 70)
    print("PARAM-B2: Mathieu Stability for B2 Flat-Band Modes")
    print("CONDITIONAL: U-32a PASS (V_{B3,B2,B1} = +0.049 > 0)")
    print("=" * 70)

    # Compute Mathieu stability boundaries
    print("\nComputing Mathieu stability boundaries...")
    q_arr, a_bounds, b_bounds = compute_mathieu_boundaries(q_max=10.0, n_q=1000, n_orders=8)

    # Compute B2 mode parameters
    print("\nComputing B2 Mathieu parameters...")
    omega_B2, d2_B2, b2_results = compute_b2_mathieu_params()

    print(f"\n  omega_B2 (natural frequency) = {omega_B2:.6f}")
    print(f"  d^2(lambda_B2)/dtau^2 = {d2_B2:.6f}")

    # Check each coupling ratio
    print(f"\n{'='*60}")
    print("Mathieu Parameters and Stability")
    print(f"{'='*60}")

    any_unstable = False
    stability_results = {}

    for r_val in sorted(b2_results.keys()):
        res = b2_results[r_val]
        a = res['a']
        q = res['q']
        q_k = res['q_kapitza']

        # Check stability for both q estimates
        unstable_q, tongue_q = is_in_unstable_band(a, q, a_bounds, b_bounds, q_arr)
        unstable_qk, tongue_qk = is_in_unstable_band(a, q_k, a_bounds, b_bounds, q_arr)

        print(f"\n  r = {r_val}:")
        print(f"    Gamma_inst = {res['Gamma_018']:.4f}")
        print(f"    S_inst = {res['S_018']:.4f}")
        print(f"    omega_drive = {res['omega_drive']:.4f}")
        print(f"    delta_tau = {res['delta_tau']:.4f}")
        print(f"    a = (2*omega_B2/omega_d)^2 = {a:.4f}")
        print(f"    q (from B2 curvature) = {q:.6f}")
        print(f"    q (Kapitza-style)      = {q_k:.6f}")
        print(f"    Unstable (q): {unstable_q} (tongue {tongue_q})")
        print(f"    Unstable (q_kapitza): {unstable_qk} (tongue {tongue_qk})")

        if unstable_q or unstable_qk:
            any_unstable = True

        stability_results[r_val] = {
            'a': a,
            'q': q,
            'q_kapitza': q_k,
            'unstable_q': unstable_q,
            'tongue_q': tongue_q,
            'unstable_qk': unstable_qk,
            'tongue_qk': tongue_qk,
            'Gamma': res['Gamma_018'],
        }

    # ============================================================
    # Check stability at the primary parametric resonance: a ~ 1
    # ============================================================
    print(f"\n{'='*60}")
    print("Primary Parametric Resonance Check (a ~ 1)")
    print(f"{'='*60}")

    # For the first unstable tongue: a ~ 1, centered at omega_drive = 2*omega_B2
    omega_drive_resonant = 2.0 * omega_B2
    print(f"  Resonant drive frequency: 2*omega_B2 = {omega_drive_resonant:.4f}")

    # Which coupling ratios give instanton rates near this?
    inst = np.load(INSTANTON_FILE, allow_pickle=True)
    tau_inst = inst['tau']
    idx_018 = np.argmin(np.abs(tau_inst - 0.18))

    print(f"  Instanton rates at tau=0.18:")
    for r_label in ['0p1', '0p3', '0p5', '1p0', '2p0', '5p0']:
        Gamma = inst[f'Gamma_inst_r{r_label}'][idx_018]
        ratio = Gamma / omega_drive_resonant
        print(f"    r={r_label}: Gamma={Gamma:.4f}, Gamma/(2*omega_B2)={ratio:.4f}")

    # The first tongue requires omega_drive ~ 2*omega_B2 = 1.69
    # At r=0.1: Gamma = 7.12, way above resonance
    # The instanton rate is much higher than 2*omega_B2 for all r < 5
    # This means a = (2*omega_B2/Gamma)^2 << 1 for small r
    # and a >> 1 for large r (where Gamma < 2*omega_B2)

    # Scan over tau to find where Gamma ~ 2*omega_B2
    print(f"\n  Scanning tau for Gamma = 2*omega_B2 = {omega_drive_resonant:.4f}:")
    for r_label in ['0p1', '0p3', '0p5', '1p0', '2p0', '5p0']:
        Gamma = inst[f'Gamma_inst_r{r_label}']
        # Find where Gamma crosses 2*omega_B2
        crossings = []
        for i in range(len(Gamma) - 1):
            if (Gamma[i] - omega_drive_resonant) * (Gamma[i+1] - omega_drive_resonant) < 0:
                tau_cross = tau_inst[i] + (omega_drive_resonant - Gamma[i]) / (Gamma[i+1] - Gamma[i]) * (tau_inst[i+1] - tau_inst[i])
                crossings.append(tau_cross)
        if crossings:
            print(f"    r={r_label}: Gamma = 2*omega_B2 at tau = {crossings}")
        else:
            # Check if always above or below
            if np.all(Gamma > omega_drive_resonant):
                print(f"    r={r_label}: Gamma always > 2*omega_B2 (minimum Gamma = {np.min(Gamma):.4f})")
            elif np.all(Gamma < omega_drive_resonant):
                print(f"    r={r_label}: Gamma always < 2*omega_B2 (maximum Gamma = {np.max(Gamma):.4f})")
            else:
                print(f"    r={r_label}: Gamma range [{np.min(Gamma):.4f}, {np.max(Gamma):.4f}]")

    # ============================================================
    # Higher tongue check: a ~ n^2
    # ============================================================
    print(f"\n{'='*60}")
    print("Higher Tongue Check")
    print(f"{'='*60}")

    for r_val in sorted(b2_results.keys()):
        res = b2_results[r_val]
        a = res['a']
        nearest_n = int(np.round(np.sqrt(a)))
        print(f"  r={r_val}: a={a:.4f}, nearest integer sqrt = {nearest_n}, "
              f"distance to tongue center = {abs(a - nearest_n**2):.4f}")

    # ============================================================
    # Gate Verdict
    # ============================================================
    print(f"\n{'='*70}")
    print("GATE VERDICT: PB-32b")
    print(f"{'='*70}")

    primary_verdict = "PASS" if any_unstable else "FAIL"
    print(f"  Any B2 mode in unstable band: {any_unstable}")
    print(f"  Verdict: {primary_verdict}")

    if not any_unstable:
        print(f"\n  Note: All (a, q) points fall in STABLE regions.")
        print(f"  The q values are very small ({min(r['q'] for r in b2_results.values()):.2e} to "
              f"{max(r['q'] for r in b2_results.values()):.2e})")
        print(f"  because d^2(lambda_B2)/dtau^2 is small (B2 is FLAT).")
        print(f"  Parametric amplification requires q > 0.5 for the first tongue.")
        print(f"  The B2 flatness that makes it good for WALL-1 trapping")
        print(f"  also makes it immune to parametric excitation.")

    # ============================================================
    # Save results
    # ============================================================
    save_dict = {
        'omega_B2': np.array(omega_B2),
        'd2_lambda_B2': np.array(d2_B2),
        'primary_verdict': np.array(primary_verdict),
        'q_arr': q_arr,
    }

    for n in range(min(6, len(a_bounds))):
        save_dict[f'a_bound_{n}'] = a_bounds[n]
    for n in range(1, min(6, len(b_bounds) + 1)):
        if n in b_bounds:
            save_dict[f'b_bound_{n}'] = b_bounds[n]

    r_values = sorted(b2_results.keys())
    save_dict['coupling_ratios'] = np.array(r_values)
    save_dict['a_params'] = np.array([stability_results[r]['a'] for r in r_values])
    save_dict['q_params'] = np.array([stability_results[r]['q'] for r in r_values])
    save_dict['q_kapitza'] = np.array([stability_results[r]['q_kapitza'] for r in r_values])
    save_dict['unstable'] = np.array([stability_results[r]['unstable_q'] for r in r_values])
    save_dict['Gamma_inst'] = np.array([stability_results[r]['Gamma'] for r in r_values])

    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"\nResults saved to {OUTPUT_NPZ}")

    # ============================================================
    # Plotting
    # ============================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('PARAM-B2: Mathieu Stability for B2 Flat-Band Modes', fontsize=14)

    # Panel 1: Mathieu stability diagram with B2 operating points
    ax = axes[0]

    # Draw stability boundaries (shade unstable regions)
    for n in range(1, min(5, len(a_bounds))):
        if n in b_bounds:
            a_n = a_bounds[n]
            b_n = b_bounds[n]
            ax.fill_between(q_arr, b_n, a_n, alpha=0.3, color=f'C{n}',
                            label=f'Tongue {n}')
    # Zeroth tongue
    ax.fill_between(q_arr, -10 * np.ones_like(q_arr), a_bounds[0],
                    alpha=0.2, color='gray', label='Tongue 0')

    # Plot B2 operating points
    for r_val in r_values:
        sr = stability_results[r_val]
        marker = 'x' if sr['unstable_q'] else 'o'
        color = 'red' if sr['unstable_q'] else 'green'
        ax.plot(sr['q'], sr['a'], marker, markersize=10, color=color,
                label=f'r={r_val:.1f}')

    ax.set_xlabel('q (drive amplitude)')
    ax.set_ylabel('a (frequency ratio)')
    ax.set_xlim([-0.1, 2.0])
    ax.set_ylim([-1, 10])
    ax.set_title('Mathieu Stability Diagram')
    ax.legend(fontsize=7, loc='upper right')
    ax.grid(True, alpha=0.3)

    # Panel 2: a parameter vs coupling ratio
    ax = axes[1]
    a_vals = [stability_results[r]['a'] for r in r_values]
    q_vals = [stability_results[r]['q'] for r in r_values]
    ax.semilogy(r_values, a_vals, 'bo-', linewidth=2, markersize=8, label='a')
    ax.semilogy(r_values, [max(q, 1e-10) for q in q_vals], 'r^-', linewidth=2,
                markersize=8, label='q')
    ax.axhline(y=1, color='gray', linestyle=':', label='a=1 (1st tongue center)')
    ax.axhline(y=4, color='gray', linestyle='--', label='a=4 (2nd tongue center)')
    ax.set_xlabel('Coupling ratio r')
    ax.set_ylabel('Mathieu parameter')
    ax.set_title('Parameters vs Coupling Ratio')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Plot saved to {OUTPUT_PNG}")

    return stability_results, primary_verdict


if __name__ == '__main__':
    results, verdict = main()
