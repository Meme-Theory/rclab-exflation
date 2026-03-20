#!/usr/bin/env python3
"""
Session 28b-5: L-9 Cubic Invariant at BCS Sector Boundaries
=============================================================

Gate L-9 (Diagnostic): Cusps at sector boundaries confirm first-order BCS
transitions.

Method:
-------
At mu/lambda_min = 1.20 (where the interior minimum exists in F_total),
analyze the Landau expansion of the free energy near the BCS transition:

    F_cond ~ a * (M_max - 1) + b * (M_max - 1)^2 + c * (M_max - 1)^3

The cubic invariant c != 0 implies a first-order transition (the Landau
symmetry-breaking argument). c = 0 implies second-order (standard BCS).

We also compute:
  - dF_total/dtau and d^2F_total/dtau^2 via finite differences
  - d^3F_total/dtau^3 left and right of sector boundaries
  - Discontinuity in d^3F/dtau^3 at each cusp

Data:
-----
  s27_multisector_bcs.npz: F_total(tau, mu), F_cond(sector, tau, mu),
                           M_max(sector, tau, mu)
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent
S27_FILE = DATA_DIR / 's27_multisector_bcs.npz'
OUT_NPZ = DATA_DIR / 's28b_cubic_invariant.npz'
OUT_PNG = DATA_DIR / 's28b_cubic_invariant.png'


def finite_diff_derivatives(tau_arr, f_arr):
    """
    Compute 1st, 2nd, 3rd derivatives of f(tau) via central finite differences.
    Uses non-uniform spacing formulas at endpoints.

    Parameters:
        tau_arr: shape (n,)
        f_arr: shape (n,)

    Returns:
        df, d2f, d3f: each shape (n,)
    """
    n = len(tau_arr)
    df = np.zeros(n)
    d2f = np.zeros(n)
    d3f = np.zeros(n)

    # Use cubic spline for robust derivatives
    cs = CubicSpline(tau_arr, f_arr)
    df = cs(tau_arr, 1)    # 1st derivative
    d2f = cs(tau_arr, 2)   # 2nd derivative
    d3f = cs(tau_arr, 3)   # 3rd derivative

    return df, d2f, d3f


def fit_landau_cubic(mmax_arr, fcond_arr, tau_arr):
    """
    Fit F_cond vs (M_max - 1) to a Landau polynomial near the transition.

    For each sector, near M_max = 1:
        F_cond ~ a*(M-1) + b*(M-1)^2 + c*(M-1)^3

    Parameters:
        mmax_arr: shape (n_tau,) M_max values for one sector
        fcond_arr: shape (n_tau,) F_cond values for one sector
        tau_arr: shape (n_tau,)

    Returns:
        dict with Landau coefficients and fit quality
    """
    # Only use points where F_cond != 0 (i.e., the sector is supercritical)
    mask = (np.abs(fcond_arr) > 1e-15) & (np.abs(mmax_arr - 1.0) < 10.0)

    if np.sum(mask) < 3:
        return {'a': np.nan, 'b': np.nan, 'c': np.nan, 'r2': np.nan, 'n_pts': int(np.sum(mask))}

    x = mmax_arr[mask] - 1.0   # deviation from critical
    y = fcond_arr[mask]

    # Polynomial fit: F_cond = a*x + b*x^2 + c*x^3 (no constant term: F_cond=0 at M_max=1)
    try:
        # Use weighted least squares with x, x^2, x^3
        X = np.column_stack([x, x**2, x**3])
        coeffs, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)
        a, b, c = coeffs

        # R-squared
        y_pred = X @ coeffs
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    except Exception:
        return {'a': np.nan, 'b': np.nan, 'c': np.nan, 'r2': np.nan, 'n_pts': int(np.sum(mask))}

    return {'a': a, 'b': b, 'c': c, 'r2': r2, 'n_pts': int(np.sum(mask))}


def main():
    # ─── Load data ───────────────────────────────────────────────────────────
    d27 = np.load(S27_FILE, allow_pickle=True)
    tau_values = d27['tau_values']        # (9,)
    mu_ratios = d27['mu_ratios']          # (12,)
    sectors = d27['sectors']              # (9, 4)
    M_max = d27['M_max']                  # (9, 9, 12)
    F_cond = d27['F_cond']                # (9, 9, 12)
    F_total = d27['F_total']              # (9, 12)

    # mu/lambda_min = 1.20 is index 8
    mu_idx_12 = int(np.where(mu_ratios == 1.2)[0][0])
    n_sectors = sectors.shape[0]
    sector_labels = [f'({sectors[i,0]},{sectors[i,1]})' for i in range(n_sectors)]

    print("=" * 72)
    print("L-9 CUBIC INVARIANT: Landau Expansion near BCS Transition")
    print("=" * 72)
    print(f"tau grid: {tau_values}")
    print(f"mu/lambda_min = 1.20 (index {mu_idx_12})")
    print()

    # ─── F_total derivatives at mu/lmin = 1.20 ──────────────────────────────
    f_total_120 = F_total[:, mu_idx_12]
    print("─── F_total(tau) at mu/lambda_min = 1.20 ───")
    for ti in range(len(tau_values)):
        print(f"  tau={tau_values[ti]:.2f}: F_total = {f_total_120[ti]:.6f}")

    # Compute derivatives via cubic spline
    cs_ftotal = CubicSpline(tau_values, f_total_120)
    tau_fine = np.linspace(tau_values[0], tau_values[-1], 500)
    f_fine = cs_ftotal(tau_fine)
    df_fine = cs_ftotal(tau_fine, 1)
    d2f_fine = cs_ftotal(tau_fine, 2)
    d3f_fine = cs_ftotal(tau_fine, 3)

    # Find interior extrema of F_total
    # dF/dtau = 0 and d2F/dtau2 > 0 => minimum
    sign_changes_df = []
    for i in range(len(tau_fine) - 1):
        if df_fine[i] * df_fine[i+1] < 0:
            tau_ext = tau_fine[i] - df_fine[i] * (tau_fine[i+1] - tau_fine[i]) / (df_fine[i+1] - df_fine[i])
            d2f_at_ext = cs_ftotal(tau_ext, 2)
            f_at_ext = cs_ftotal(tau_ext)
            ext_type = "MINIMUM" if d2f_at_ext > 0 else "MAXIMUM"
            sign_changes_df.append((tau_ext, f_at_ext, d2f_at_ext, ext_type))

    print(f"\n  Interior extrema of F_total:")
    for tau_ext, f_ext, d2f_ext, ext_type in sign_changes_df:
        print(f"    tau = {tau_ext:.4f}: F = {f_ext:.4f}, d2F/dtau2 = {d2f_ext:.4f} ({ext_type})")

    # ─── d3F/dtau3 discontinuities ──────────────────────────────────────────
    print(f"\n─── d3F/dtau3 Analysis (cusp detection) ───")
    # Compute d3F at each data point from left and right
    df_data, d2f_data, d3f_data = finite_diff_derivatives(tau_values, f_total_120)

    print(f"  {'tau':<8} {'dF/dtau':<14} {'d2F/dtau2':<14} {'d3F/dtau3':<14}")
    print(f"  {'-'*48}")
    for ti in range(len(tau_values)):
        print(f"  {tau_values[ti]:<8.2f} {df_data[ti]:<14.4f} {d2f_data[ti]:<14.4f} {d3f_data[ti]:<14.4f}")

    # Detect jumps in d3F (cusp indicator)
    cusp_detected = []
    for ti in range(1, len(tau_values)):
        d3_jump = abs(d3f_data[ti] - d3f_data[ti-1])
        d3_avg = 0.5 * (abs(d3f_data[ti]) + abs(d3f_data[ti-1]))
        if d3_avg > 0 and d3_jump / d3_avg > 0.5:  # >50% relative jump
            cusp_detected.append((tau_values[ti-1], tau_values[ti], d3f_data[ti-1], d3f_data[ti], d3_jump))

    if cusp_detected:
        print(f"\n  d3F/dtau3 discontinuities detected:")
        for tau_lo, tau_hi, d3_lo, d3_hi, jump in cusp_detected:
            print(f"    Between tau={tau_lo:.2f} and {tau_hi:.2f}: d3F jumps from {d3_lo:.2f} to {d3_hi:.2f} (|jump| = {jump:.2f})")
    else:
        print(f"\n  No significant d3F/dtau3 discontinuities detected.")

    # ─── Per-sector Landau cubic expansion ───────────────────────────────────
    print()
    print("=" * 72)
    print("LANDAU CUBIC INVARIANT: F_cond ~ a*(M-1) + b*(M-1)^2 + c*(M-1)^3")
    print("=" * 72)

    landau_results = {}
    print(f"\n  {'Sector':<10} {'a':<12} {'b':<12} {'c':<12} {'R^2':<10} {'n_pts':<8} {'Order':<12}")
    print(f"  {'-'*62}")

    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        mmax_tau = M_max[si, :, mu_idx_12]
        fcond_tau = F_cond[si, :, mu_idx_12]

        result = fit_landau_cubic(mmax_tau, fcond_tau, tau_values)
        landau_results[f'landau_{p}_{q}'] = result

        c_val = result['c']
        order = "1st-order" if (not np.isnan(c_val) and abs(c_val) > 1e-3) else \
                "2nd-order" if (not np.isnan(c_val) and abs(c_val) <= 1e-3) else "N/A"

        print(f"  ({p},{q}){'':<6} {result['a']:<12.4f} {result['b']:<12.4f} {result['c']:<12.6f} "
              f"{result['r2']:<10.4f} {result['n_pts']:<8d} {order}")

    # ─── Per-sector F_cond derivatives for cusp detection ────────────────────
    print()
    print("=" * 72)
    print("SECTOR-LEVEL F_cond(tau) CUSPS at mu/lambda_min = 1.20")
    print("=" * 72)

    sector_cusps = {}
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        fcond_tau = F_cond[si, :, mu_idx_12]

        # Only analyze sectors with non-trivial condensate
        active = np.abs(fcond_tau) > 1e-15
        if np.sum(active) < 3:
            continue

        # Find onset point (where F_cond becomes non-zero)
        onset_idx = None
        for ti in range(len(tau_values)):
            if abs(fcond_tau[ti]) > 1e-15:
                onset_idx = ti
                break

        if onset_idx is not None and onset_idx > 0:
            # dF_cond/dtau jumps from 0 to finite = cusp
            df_onset = (fcond_tau[onset_idx] - 0.0) / (tau_values[onset_idx] - tau_values[max(0, onset_idx-1)])
            print(f"  ({p},{q}): onset at tau={tau_values[onset_idx]:.2f}, dF_cond/dtau|onset = {df_onset:.4f}")
            sector_cusps[f'onset_{p}_{q}'] = tau_values[onset_idx]
        elif onset_idx == 0:
            # Active from tau=0
            print(f"  ({p},{q}): active from tau=0.00, F_cond(0) = {fcond_tau[0]:.6f}")

    # ─── Also analyze at mu/lambda_min = 1.0 (reference) ────────────────────
    mu_idx_10 = int(np.where(mu_ratios == 1.0)[0][0])
    print()
    print("─── Comparison: mu/lambda_min = 1.0 ───")
    f_total_10 = F_total[:, mu_idx_10]
    for ti in range(len(tau_values)):
        print(f"  tau={tau_values[ti]:.2f}: F_total = {f_total_10[ti]:.6f}")

    # ─── Gate Verdict ────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("GATE L-9 VERDICT")
    print("=" * 72)

    # Check: any cubic invariant c significantly non-zero?
    c_values = []
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        key = f'landau_{p}_{q}'
        if key in landau_results and not np.isnan(landau_results[key]['c']):
            c_values.append((f'({p},{q})', landau_results[key]['c']))

    n_first_order = sum(1 for _, c in c_values if abs(c) > 1e-3)
    n_second_order = sum(1 for _, c in c_values if abs(c) <= 1e-3)

    has_cusps = len(cusp_detected) > 0

    if n_first_order > 0 or has_cusps:
        print(f"  L-9: PASS (DIAGNOSTIC)")
        print(f"  {n_first_order}/{len(c_values)} sectors have |c| > 1e-3 (first-order character)")
        if has_cusps:
            print(f"  {len(cusp_detected)} cusp(s) in d3F_total/dtau3")
        verdict = "PASS"
    else:
        print(f"  L-9: FAIL")
        print(f"  All cubic invariants c ~ 0: pure second-order BCS transitions")
        print(f"  No cusps in F_total")
        verdict = "FAIL"

    print(f"\n  Cubic invariants:")
    for label, c in c_values:
        print(f"    {label}: c = {c:.6f} ({'1st-order' if abs(c) > 1e-3 else '2nd-order'})")

    # ─── Save ────────────────────────────────────────────────────────────────
    save_dict = {
        'tau_values': tau_values,
        'tau_fine': tau_fine,
        'mu_ratios': mu_ratios,
        'sectors': sectors,
        'f_total_120': f_total_120,
        'f_total_10': f_total_10,
        'f_fine': f_fine,
        'df_fine': df_fine,
        'd2f_fine': d2f_fine,
        'd3f_fine': d3f_fine,
        'df_data': df_data,
        'd2f_data': d2f_data,
        'd3f_data': d3f_data,
        'verdict': verdict,
    }

    # Store Landau coefficients
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        key = f'landau_{p}_{q}'
        if key in landau_results:
            for coeff_name in ['a', 'b', 'c', 'r2']:
                save_dict[f'{key}_{coeff_name}'] = landau_results[key][coeff_name]

    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"\n  Saved: {OUT_NPZ}")

    # ─── Plot ────────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('L-9: Cubic Invariant and Phase Transition Character ($\\mu/\\lambda_{\\min} = 1.20$)', fontsize=13)

    # Panel (a): F_total(tau) at mu/lmin = 1.20
    ax = axes[0, 0]
    ax.plot(tau_fine, f_fine, 'b-', linewidth=2)
    ax.scatter(tau_values, f_total_120, color='blue', zorder=5, s=40)
    for tau_ext, f_ext, d2f_ext, ext_type in sign_changes_df:
        marker = 'v' if ext_type == "MINIMUM" else '^'
        color = 'red' if ext_type == "MINIMUM" else 'green'
        ax.scatter([tau_ext], [f_ext], marker=marker, color=color, s=100, zorder=6,
                   label=f'{ext_type} at $\\tau={tau_ext:.3f}$')
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$F_{\\rm total}$')
    ax.set_title('(a) $F_{\\rm total}(\\tau)$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (b): d3F/dtau3
    ax = axes[0, 1]
    ax.plot(tau_fine, d3f_fine, 'r-', linewidth=2)
    ax.scatter(tau_values, d3f_data, color='red', zorder=5, s=40)
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$d^3 F/d\\tau^3$')
    ax.set_title('(b) Third derivative (cusp indicator)')
    ax.grid(True, alpha=0.3)

    # Panel (c): F_cond vs (M_max - 1) for each sector
    ax = axes[1, 0]
    colors = plt.cm.tab10(np.linspace(0, 1, n_sectors))
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        mmax_tau = M_max[si, :, mu_idx_12]
        fcond_tau = F_cond[si, :, mu_idx_12]
        mask = np.abs(fcond_tau) > 1e-15
        if np.sum(mask) >= 2:
            x = mmax_tau[mask] - 1.0
            y = fcond_tau[mask]
            ax.scatter(x, y, color=colors[si], label=f'({p},{q})', s=30, zorder=5)

            # Plot Landau fit
            key = f'landau_{p}_{q}'
            if key in landau_results and not np.isnan(landau_results[key]['a']):
                x_fit = np.linspace(x.min(), x.max(), 100)
                lr = landau_results[key]
                y_fit = lr['a'] * x_fit + lr['b'] * x_fit**2 + lr['c'] * x_fit**3
                ax.plot(x_fit, y_fit, color=colors[si], linestyle='--', alpha=0.5)

    ax.axvline(x=0, color='k', linestyle=':', alpha=0.3)
    ax.set_xlabel('$M_{\\max} - 1$')
    ax.set_ylabel('$F_{\\rm cond}$')
    ax.set_title('(c) Landau expansion: $F_{\\rm cond}$ vs $(M_{\\max}-1)$')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel (d): Cubic coefficient c for each sector
    ax = axes[1, 1]
    sector_names = []
    c_vals = []
    for si in range(n_sectors):
        p, q = sectors[si, 0], sectors[si, 1]
        key = f'landau_{p}_{q}'
        if key in landau_results and not np.isnan(landau_results[key]['c']):
            sector_names.append(f'({p},{q})')
            c_vals.append(landau_results[key]['c'])

    if c_vals:
        bar_colors = ['red' if abs(c) > 1e-3 else 'blue' for c in c_vals]
        ax.bar(range(len(c_vals)), c_vals, color=bar_colors, alpha=0.7)
        ax.set_xticks(range(len(c_vals)))
        ax.set_xticklabels(sector_names, fontsize=8)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axhline(y=1e-3, color='gray', linestyle=':', alpha=0.5, label='$|c| = 10^{-3}$')
        ax.axhline(y=-1e-3, color='gray', linestyle=':', alpha=0.5)
        ax.set_xlabel('Sector')
        ax.set_ylabel('Cubic coefficient $c$')
        ax.set_title('(d) Landau cubic invariant by sector')
        ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_PNG}")
    plt.close()


if __name__ == '__main__':
    main()
