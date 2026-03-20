#!/usr/bin/env python3
"""
Session 28b-7: S-3 Hessian of F_total(tau, mu)
================================================

Gate S-3:
  PASS: Both Hessian eigenvalues positive -- genuine minimum
  FAIL: One or both eigenvalues negative -- saddle or maximum

Method:
-------
1. Extract F_total(tau, mu) from s27 data at mu/lambda_min = 1.20.
2. At candidate minima: compute the 2x2 Hessian:

       H = [[d^2F/dtau^2,   d^2F/dtau dmu],
            [d^2F/dmu dtau, d^2F/dmu^2    ]]

   using finite differences from the s27 grid (9 tau, 12 mu points).
3. Diagonalize H. Report both eigenvalues.
4. Both positive -> true minimum. One negative -> saddle. Both negative -> maximum.

Data:
-----
  s27_multisector_bcs.npz: F_total[tau, mu] shape (9, 12)
  tau grid: 9 points [0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
  mu grid: 12 points [0, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0]
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent
S27_FILE = DATA_DIR / 's27_multisector_bcs.npz'
OUT_NPZ = DATA_DIR / 's28b_hessian.npz'
OUT_TXT = DATA_DIR / 's28b_hessian.txt'
OUT_PNG = DATA_DIR / 's28b_hessian.png'


def compute_hessian_2d(F: np.ndarray, tau_arr: np.ndarray, mu_arr: np.ndarray,
                        ti: int, mi: int) -> np.ndarray:
    """
    Compute the 2x2 Hessian of F(tau, mu) at grid point (ti, mi)
    using central finite differences where possible, forward/backward
    at boundaries.

    Parameters:
        F: shape (n_tau, n_mu)
        tau_arr: shape (n_tau,)
        mu_arr: shape (n_mu,)
        ti: tau index
        mi: mu index

    Returns:
        H: 2x2 Hessian matrix [[d2F/dtau2, d2F/dtau_dmu],
                                [d2F/dmu_dtau, d2F/dmu2]]
    """
    nt, nm = F.shape

    # d2F/dtau2
    if 0 < ti < nt - 1:
        dt_lo = tau_arr[ti] - tau_arr[ti-1]
        dt_hi = tau_arr[ti+1] - tau_arr[ti]
        d2f_dtau2 = 2.0 * (F[ti+1, mi] / (dt_hi * (dt_lo + dt_hi))
                          - F[ti, mi] / (dt_lo * dt_hi)
                          + F[ti-1, mi] / (dt_lo * (dt_lo + dt_hi)))
    elif ti == 0 and nt >= 3:
        dt1 = tau_arr[1] - tau_arr[0]
        dt2 = tau_arr[2] - tau_arr[0]
        d2f_dtau2 = 2.0 * (F[0, mi] / (dt1 * dt2) * dt2
                          - F[1, mi] / (dt1 * (dt2 - dt1)) * dt2
                          + F[2, mi] / (dt2 * (dt2 - dt1)) * dt1) / (dt1)
        # Fallback to forward difference
        d2f_dtau2 = (F[2, mi] - 2*F[1, mi] + F[0, mi]) / ((tau_arr[1] - tau_arr[0])**2)
    elif ti == nt - 1 and nt >= 3:
        d2f_dtau2 = (F[ti, mi] - 2*F[ti-1, mi] + F[ti-2, mi]) / ((tau_arr[ti] - tau_arr[ti-1])**2)
    else:
        d2f_dtau2 = np.nan

    # d2F/dmu2
    if 0 < mi < nm - 1:
        dm_lo = mu_arr[mi] - mu_arr[mi-1]
        dm_hi = mu_arr[mi+1] - mu_arr[mi]
        d2f_dmu2 = 2.0 * (F[ti, mi+1] / (dm_hi * (dm_lo + dm_hi))
                         - F[ti, mi] / (dm_lo * dm_hi)
                         + F[ti, mi-1] / (dm_lo * (dm_lo + dm_hi)))
    elif mi == 0:
        dm = mu_arr[1] - mu_arr[0]
        d2f_dmu2 = (F[ti, 2] - 2*F[ti, 1] + F[ti, 0]) / (dm**2) if nm >= 3 else np.nan
    elif mi == nm - 1:
        dm = mu_arr[mi] - mu_arr[mi-1]
        d2f_dmu2 = (F[ti, mi] - 2*F[ti, mi-1] + F[ti, mi-2]) / (dm**2) if nm >= 3 else np.nan
    else:
        d2f_dmu2 = np.nan

    # d2F/dtau dmu (mixed partial)
    if 0 < ti < nt - 1 and 0 < mi < nm - 1:
        dt = 0.5 * (tau_arr[ti+1] - tau_arr[ti-1])
        dm = 0.5 * (mu_arr[mi+1] - mu_arr[mi-1])
        d2f_dtaudmu = (F[ti+1, mi+1] - F[ti+1, mi-1] - F[ti-1, mi+1] + F[ti-1, mi-1]) / (4 * dt * dm)
    else:
        # Forward/backward where needed
        dti = 1 if ti < nt - 1 else -1
        dmi = 1 if mi < nm - 1 else -1
        ti2 = ti + dti
        mi2 = mi + dmi
        dt = tau_arr[ti2] - tau_arr[ti]
        dm = mu_arr[mi2] - mu_arr[mi]
        if abs(dt) > 1e-15 and abs(dm) > 1e-15:
            d2f_dtaudmu = (F[ti2, mi2] - F[ti2, mi] - F[ti, mi2] + F[ti, mi]) / (dt * dm)
        else:
            d2f_dtaudmu = np.nan

    H = np.array([[d2f_dtau2, d2f_dtaudmu],
                   [d2f_dtaudmu, d2f_dmu2]])
    return H


def find_minima_1d(f_arr, x_arr):
    """
    Find approximate 1D minima locations.

    Returns list of (x_min, f_min, index) where f has a local minimum.
    """
    minima = []
    for i in range(1, len(f_arr) - 1):
        if f_arr[i] < f_arr[i-1] and f_arr[i] < f_arr[i+1]:
            minima.append((x_arr[i], f_arr[i], i))
    return minima


def main():
    # ─── Load data ───────────────────────────────────────────────────────────
    d27 = np.load(S27_FILE, allow_pickle=True)
    tau_values = d27['tau_values']    # (9,)
    mu_ratios = d27['mu_ratios']      # (12,)
    sectors = d27['sectors']          # (9, 4)
    F_total = d27['F_total']          # (9, 12)
    lambda_min_global = d27['lambda_min']  # (9, 9) -- per sector per tau

    # Physical mu = mu_ratio * lambda_min. Since F_total is summed over sectors,
    # and each sector has its own lambda_min, the mu coordinate in F_total is
    # mu_ratio (dimensionless). We work directly in (tau, mu_ratio) space.
    mu_arr = mu_ratios.copy()

    print("=" * 72)
    print("S-3 HESSIAN: Stability Analysis of F_total(tau, mu)")
    print("=" * 72)
    print(f"tau grid ({len(tau_values)}): {tau_values}")
    print(f"mu/lambda_min grid ({len(mu_ratios)}): {mu_ratios}")
    print()

    # ─── Display F_total landscape ───────────────────────────────────────────
    print("─── F_total(tau, mu/lambda_min) ───")
    print(f"{'tau \\ mu':<8}", end="")
    for mi in range(len(mu_ratios)):
        print(f"{mu_ratios[mi]:<8.2f}", end="")
    print()
    for ti in range(len(tau_values)):
        print(f"{tau_values[ti]:<8.2f}", end="")
        for mi in range(len(mu_ratios)):
            print(f"{F_total[ti, mi]:<8.2f}", end="")
        print()

    # ─── Find all candidate minima ───────────────────────────────────────────
    print()
    print("─── Candidate minima search ───")

    # Search: for each mu, find tau-minima; for each tau, find mu-minima
    candidates = []

    # Approach 1: Scan F_total for local minima in the 2D grid
    for ti in range(1, len(tau_values) - 1):
        for mi in range(1, len(mu_ratios) - 1):
            f_c = F_total[ti, mi]
            if f_c == 0.0:
                continue  # Skip zero (no condensation)
            # Check all 4 neighbors
            f_up = F_total[ti-1, mi]
            f_dn = F_total[ti+1, mi]
            f_lt = F_total[ti, mi-1]
            f_rt = F_total[ti, mi+1]
            if f_c < f_up and f_c < f_dn and f_c < f_lt and f_c < f_rt:
                candidates.append((ti, mi, tau_values[ti], mu_ratios[mi], f_c))

    # Approach 2: Check specific mu slices for 1D minima
    for mi in range(len(mu_ratios)):
        f_slice = F_total[:, mi]
        if np.all(f_slice == 0):
            continue
        minima = find_minima_1d(f_slice, tau_values)
        for tau_min, f_min, ti in minima:
            if (ti, mi) not in [(c[0], c[1]) for c in candidates]:
                candidates.append((ti, mi, tau_min, mu_ratios[mi], f_min))

    # Also check boundary: global minimum for key mu slices
    for mi_target in [5, 6, 7, 8, 9]:  # mu = 1.0, 1.05, 1.1, 1.2, 1.5
        f_slice = F_total[:, mi_target]
        nonzero = f_slice != 0.0
        if np.any(nonzero):
            ti_min = np.argmin(f_slice)
            if f_slice[ti_min] < -1e-6:
                already = any(c[0] == ti_min and c[1] == mi_target for c in candidates)
                if not already:
                    candidates.append((ti_min, mi_target, tau_values[ti_min],
                                       mu_ratios[mi_target], f_slice[ti_min]))

    if not candidates:
        print("  No candidate minima found in F_total grid!")
    else:
        print(f"  Found {len(candidates)} candidate point(s)")

    # ─── Compute Hessian at each candidate ───────────────────────────────────
    print()
    print("=" * 72)
    print("HESSIAN ANALYSIS AT CANDIDATE POINTS")
    print("=" * 72)

    txt_lines = []
    txt_lines.append("S-3 Hessian Analysis of F_total(tau, mu)")
    txt_lines.append("=" * 60)

    hessian_results = {}
    any_genuine_minimum = False

    for ci, (ti, mi, tau_c, mu_c, f_c) in enumerate(candidates):
        H = compute_hessian_2d(F_total, tau_values, mu_arr, ti, mi)

        # Eigenvalues
        eigvals = np.linalg.eigvalsh(H)
        det_H = np.linalg.det(H)
        trace_H = np.trace(H)

        # Classification
        if np.all(eigvals > 0):
            classification = "GENUINE MINIMUM"
            any_genuine_minimum = True
        elif np.all(eigvals < 0):
            classification = "MAXIMUM"
        elif eigvals[0] * eigvals[1] < 0:
            classification = "SADDLE POINT"
        else:
            classification = "DEGENERATE"

        label = f"Point {ci+1}: tau={tau_c:.2f}, mu/lmin={mu_c:.2f}"
        print(f"\n  {label}")
        print(f"    F_total = {f_c:.6f}")
        print(f"    H = [[{H[0,0]:+.4f}, {H[0,1]:+.4f}],")
        print(f"         [{H[1,0]:+.4f}, {H[1,1]:+.4f}]]")
        print(f"    Eigenvalues: lambda_1 = {eigvals[0]:.6f}, lambda_2 = {eigvals[1]:.6f}")
        print(f"    det(H) = {det_H:.6f}, tr(H) = {trace_H:.6f}")
        print(f"    Classification: {classification}")

        txt_lines.append(f"\n{label}")
        txt_lines.append(f"  F_total = {f_c:.6f}")
        txt_lines.append(f"  H = [[{H[0,0]:+.6f}, {H[0,1]:+.6f}], [{H[1,0]:+.6f}, {H[1,1]:+.6f}]]")
        txt_lines.append(f"  Eigenvalues: {eigvals[0]:.6f}, {eigvals[1]:.6f}")
        txt_lines.append(f"  Classification: {classification}")

        hessian_results[f'point_{ci}'] = {
            'ti': ti, 'mi': mi, 'tau': tau_c, 'mu': mu_c,
            'F': f_c, 'H': H, 'eigvals': eigvals, 'classification': classification
        }

    # ─── Special analysis: mu/lmin = 1.20 slice ─────────────────────────────
    print()
    print("=" * 72)
    print("DETAILED tau SLICE AT mu/lambda_min = 1.20")
    print("=" * 72)
    mi_12 = int(np.where(mu_ratios == 1.2)[0][0])
    f_slice_12 = F_total[:, mi_12]

    print(f"  {'tau':<8} {'F_total':<14} {'d2F/dtau2':<14} {'Type':<20}")
    print(f"  {'-'*54}")
    for ti in range(len(tau_values)):
        f_val = f_slice_12[ti]
        if 0 < ti < len(tau_values) - 1:
            dt_lo = tau_values[ti] - tau_values[ti-1]
            dt_hi = tau_values[ti+1] - tau_values[ti]
            d2f = 2.0 * (f_slice_12[ti+1] / (dt_hi * (dt_lo + dt_hi))
                        - f_slice_12[ti] / (dt_lo * dt_hi)
                        + f_slice_12[ti-1] / (dt_lo * (dt_lo + dt_hi)))
            if f_val < f_slice_12[ti-1] and f_val < f_slice_12[ti+1]:
                ttype = "LOCAL MINIMUM" if d2f > 0 else "INFLECTION"
            elif f_val > f_slice_12[ti-1] and f_val > f_slice_12[ti+1]:
                ttype = "LOCAL MAXIMUM"
            else:
                ttype = ""
            print(f"  {tau_values[ti]:<8.2f} {f_val:<14.6f} {d2f:<14.4f} {ttype}")
        else:
            print(f"  {tau_values[ti]:<8.2f} {f_val:<14.6f} {'---':<14} {'(boundary)'}")

    # ─── Also check the deepest point across all (tau, mu) ──────────────────
    print()
    print("─── Global minimum of F_total ───")
    min_idx = np.unravel_index(np.argmin(F_total), F_total.shape)
    ti_gmin, mi_gmin = min_idx
    print(f"  Global min: F = {F_total[ti_gmin, mi_gmin]:.4f} at tau = {tau_values[ti_gmin]:.2f}, "
          f"mu/lmin = {mu_ratios[mi_gmin]:.2f}")

    # Hessian at global min
    if 0 < ti_gmin < len(tau_values) - 1 and 0 < mi_gmin < len(mu_ratios) - 1:
        H_gmin = compute_hessian_2d(F_total, tau_values, mu_arr, ti_gmin, mi_gmin)
        eigvals_gmin = np.linalg.eigvalsh(H_gmin)
        print(f"  Hessian eigenvalues: {eigvals_gmin[0]:.4f}, {eigvals_gmin[1]:.4f}")
        if np.all(eigvals_gmin > 0):
            print(f"  Global minimum is a GENUINE MINIMUM")
        else:
            print(f"  Global minimum is NOT a genuine minimum (boundary or saddle)")
    else:
        print(f"  Global minimum is at grid boundary -- Hessian not reliably computable")

    # ─── Gate Verdict ────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("GATE S-3 VERDICT")
    print("=" * 72)

    if any_genuine_minimum:
        print(f"  S-3: PASS")
        print(f"  At least one candidate point has both Hessian eigenvalues positive.")
        verdict = "PASS"
    else:
        # Check if there are ANY negative F_total values (condensation exists)
        has_condensation = np.any(F_total < -1e-6)
        if has_condensation:
            print(f"  S-3: FAIL")
            print(f"  F_total has negative values (condensation exists) but no interior minimum")
            print(f"  with both Hessian eigenvalues positive. All candidate points are saddles or")
            print(f"  boundary points.")
            verdict = "FAIL"
        else:
            print(f"  S-3: FAIL")
            print(f"  No condensation and no minimum in F_total.")
            verdict = "FAIL"

    txt_lines.append(f"\nGATE S-3 VERDICT: {verdict}")

    # ─── Save ────────────────────────────────────────────────────────────────
    save_dict = {
        'tau_values': tau_values,
        'mu_ratios': mu_ratios,
        'F_total': F_total,
        'verdict': verdict,
    }
    for ci, key in enumerate(hessian_results):
        hr = hessian_results[key]
        save_dict[f'H_{ci}'] = hr['H']
        save_dict[f'eigvals_{ci}'] = hr['eigvals']
        save_dict[f'tau_{ci}'] = hr['tau']
        save_dict[f'mu_{ci}'] = hr['mu']
        save_dict[f'F_{ci}'] = hr['F']

    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"\n  Saved: {OUT_NPZ}")

    with open(OUT_TXT, 'w') as f:
        f.write('\n'.join(txt_lines))
    print(f"  Saved: {OUT_TXT}")

    # ─── Plot ────────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('S-3: Hessian Analysis of $F_{\\rm total}(\\tau, \\mu/\\lambda_{\\min})$', fontsize=14)

    # Panel (a): F_total heatmap
    ax = axes[0]
    # Replace zeros with NaN for better visualization
    F_display = F_total.copy()
    F_display[F_display == 0] = np.nan
    im = ax.pcolormesh(mu_ratios, tau_values, F_display, cmap='RdBu_r', shading='nearest')
    fig.colorbar(im, ax=ax, label='$F_{\\rm total}$')
    # Mark candidates
    for ci, (ti, mi, tau_c, mu_c, f_c) in enumerate(candidates):
        hr = hessian_results[f'point_{ci}']
        is_min = hr['classification'] == 'GENUINE MINIMUM'
        marker = 'o' if is_min else 'x'
        color = 'green' if is_min else 'red'
        kwargs = {'marker': marker, 'color': color, 's': 100, 'zorder': 5}
        if is_min:
            kwargs['edgecolors'] = 'k'
            kwargs['linewidths'] = 1.5
        ax.scatter([mu_c], [tau_c], **kwargs)
    ax.set_xlabel('$\\mu/\\lambda_{\\min}$')
    ax.set_ylabel('$\\tau$')
    ax.set_title('(a) $F_{\\rm total}$ landscape')

    # Panel (b): F_total slices at key mu values
    ax = axes[1]
    for mi_target, ls in [(5, '-'), (6, '--'), (7, '-.'), (8, ':'), (9, '-')]:
        label = f'$\\mu/\\lambda_{{\\min}}={mu_ratios[mi_target]:.2f}$'
        ax.plot(tau_values, F_total[:, mi_target], ls, linewidth=2, label=label)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$F_{\\rm total}$')
    ax.set_title('(b) $F_{\\rm total}(\\tau)$ slices')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (c): Hessian eigenvalues at candidates
    ax = axes[2]
    if candidates:
        for ci in range(len(candidates)):
            hr = hessian_results[f'point_{ci}']
            ev = hr['eigvals']
            tau_c = hr['tau']
            mu_c = hr['mu']
            label = f'$\\tau={tau_c:.2f}, \\mu/\\lambda={{\\min}}={mu_c:.2f}$'
            color = 'green' if np.all(ev > 0) else 'red'
            ax.bar([2*ci, 2*ci+1], ev, color=color, alpha=0.7, width=0.8)
            ax.text(2*ci + 0.5, min(ev) - 5, f'({tau_c:.1f},{mu_c:.1f})', ha='center', fontsize=7)
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
        ax.set_ylabel('Hessian eigenvalue')
        ax.set_title('(c) Hessian eigenvalues at candidates')
        ax.set_xticks([2*ci + 0.5 for ci in range(len(candidates))])
        ax.set_xticklabels([f'P{ci+1}' for ci in range(len(candidates))], fontsize=8)
    else:
        ax.text(0.5, 0.5, 'No candidates found', ha='center', va='center', transform=ax.transAxes)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_PNG}")
    plt.close()


if __name__ == '__main__':
    main()
