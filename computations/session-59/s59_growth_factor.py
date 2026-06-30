#!/usr/bin/env python3
"""
s59_growth_factor.py — GROWTH-FACTOR-59
=========================================

Compute the linear growth factor D(a) and f*sigma_8(z) for:
  (1) LCDM: w = -1 (constant)
  (2) Framework: w_0 = -0.918, w_a = 0 (constant w != -1)

Compare at DESI redshift bins and assess detectability.

Growth equation (scale-factor form):
  D''(a) + [3/a + (1/2)(dE^2/da)/E^2] D'(a) - (3/2) Omega_m / (a^5 E^2) D(a) = 0

Gate: GROWTH-FACTOR-59
  PASS: max |Delta(f*sigma8)/(f*sigma8)_LCDM| < 1%
  INFO: 1-5%
  FAIL: > 5%

Session 59 — Mack (Cosmic Bridge)
"""

import os
import sys
import traceback

# Wrap everything in try/except to catch errors
try:
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.interpolate import interp1d
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    sys.path.insert(0, script_dir)

    # Import canonical constants
    from canonical_constants import (
        Omega_m, Omega_Lambda, sigma_8, H_0_km_s_Mpc
    )

    # ========================================================================
    # Step 0: Load framework w_0 from S58 data
    # ========================================================================
    s58_data = np.load('s58_w_desi.npz', allow_pickle=True)
    w0 = float(s58_data['w_0_A'])   # = -0.9181
    wa = float(s58_data['w_a_A'])   # = -0.000575 (essentially zero)

    # For this computation we treat w as constant at w_0 (w_a ~ 0)
    Omega_DE = 1.0 - Omega_m  # flat universe

    # ========================================================================
    # Step 1: Hubble functions
    # ========================================================================
    def E2_LCDM(a):
        return Omega_m * a**(-3) + Omega_Lambda

    def E2_wCDM(a, w0_val):
        return Omega_m * a**(-3) + Omega_DE * a**(-3.0*(1.0 + w0_val))

    def dE2_da_LCDM(a):
        return -3.0 * Omega_m * a**(-4)

    def dE2_da_wCDM(a, w0_val):
        exp_w = -3.0*(1.0 + w0_val)
        return -3.0 * Omega_m * a**(-4) + exp_w * Omega_DE * a**(exp_w - 1.0)

    # ========================================================================
    # Step 2: Growth ODE
    # ========================================================================
    # D'' + [3/a + (1/2)(dE2/da)/E2] D' - (3/2) Omega_m / (a^5 * E2) D = 0
    # y = [D, dD/da]

    def growth_rhs_LCDM(a, y):
        D, Dp = y
        e2 = E2_LCDM(a)
        de2 = dE2_da_LCDM(a)
        Dpp = -(3.0/a + 0.5*de2/e2)*Dp + 1.5*Omega_m/(a**5 * e2)*D
        return [Dp, Dpp]

    def growth_rhs_wCDM(a, y):
        D, Dp = y
        e2 = E2_wCDM(a, w0)
        de2 = dE2_da_wCDM(a, w0)
        Dpp = -(3.0/a + 0.5*de2/e2)*Dp + 1.5*Omega_m/(a**5 * e2)*D
        return [Dp, Dpp]

    # ========================================================================
    # Step 3: Initial conditions (matter domination: D=a, dD/da=1)
    # ========================================================================
    a_init = 0.001  # z = 999 (local)
    a_final = 1.0  # (local)
    y0 = [a_init, 1.0]

    a_eval = np.linspace(a_init, a_final, 10000)

    # ========================================================================
    # Step 4: Solve LCDM
    # ========================================================================
    sol_L = solve_ivp(growth_rhs_LCDM, [a_init, a_final], y0,
                      t_eval=a_eval, method='RK45', rtol=1e-10, atol=1e-12)
    assert sol_L.success, f"LCDM integration failed: {sol_L.message}"

    D_L = sol_L.y[0]
    Dp_L = sol_L.y[1]
    a_arr = sol_L.t

    # Normalize D(a=1) = 1
    D_L_norm = D_L / D_L[-1]
    Dp_L_norm = Dp_L / D_L[-1]

    # f = d(ln D)/d(ln a) = a * D'/D
    f_L = a_arr * Dp_L_norm / D_L_norm

    # f*sigma_8(a) with correct normalization for LCDM
    fsig8_L = f_L * sigma_8 * D_L_norm

    # ========================================================================
    # Step 5: Solve wCDM (framework)
    # ========================================================================
    sol_W = solve_ivp(growth_rhs_wCDM, [a_init, a_final], y0,
                      t_eval=a_eval, method='RK45', rtol=1e-10, atol=1e-12)
    assert sol_W.success, f"wCDM integration failed: {sol_W.message}"

    D_W = sol_W.y[0]
    Dp_W = sol_W.y[1]
    a_W = sol_W.t

    # Growth ratio: same A_s => sigma_8 scales by D(1) ratio
    growth_ratio = D_W[-1] / D_L[-1]
    sigma8_W = sigma_8 * growth_ratio

    D_W_norm = D_W / D_W[-1]
    Dp_W_norm = Dp_W / D_W[-1]
    f_W = a_W * Dp_W_norm / D_W_norm
    fsig8_W = f_W * sigma8_W * D_W_norm

    # ========================================================================
    # Step 6: Evaluate at DESI redshift bins
    # ========================================================================
    z_DESI = np.array([0.3, 0.5, 0.7, 1.0, 1.5])
    a_DESI = 1.0 / (1.0 + z_DESI)

    # DESI DR1/DR2 approximate f*sigma_8 uncertainties
    # Based on DESI 2024 KP-VII (BAO+RSD), representative per-bin 1-sigma
    desi_err = np.array([0.025, 0.020, 0.018, 0.022, 0.035])

    iL = interp1d(a_arr, fsig8_L, kind='cubic')
    iW = interp1d(a_W, fsig8_W, kind='cubic')

    fsig8_L_DESI = iL(a_DESI)
    fsig8_W_DESI = iW(a_DESI)

    frac_diff = (fsig8_W_DESI - fsig8_L_DESI) / fsig8_L_DESI
    abs_diff = fsig8_W_DESI - fsig8_L_DESI
    n_sigma = np.abs(abs_diff) / desi_err

    # Also compute f alone at DESI points
    iL_f = interp1d(a_arr, f_L, kind='cubic')
    iW_f = interp1d(a_W, f_W, kind='cubic')
    f_L_DESI = iL_f(a_DESI)
    f_W_DESI = iW_f(a_DESI)

    # Linder gamma: f ~ Omega_m(a)^gamma
    gamma_LCDM = 0.55  # (local)
    gamma_wCDM = 0.55 + 0.05*(1.0 + w0)  # Linder 2005

    max_frac = np.max(np.abs(frac_diff)) * 100.0
    max_nsig = np.max(n_sigma)

    # Gate verdict
    if max_frac < 1.0:
        verdict = "PASS"
        verdict_msg = f"< 1% ({max_frac:.3f}%) -- degenerate with LCDM in growth"
    elif max_frac < 5.0:
        verdict = "INFO"
        verdict_msg = f"1-5% ({max_frac:.3f}%) -- marginally detectable"
    else:
        verdict = "FAIL"
        verdict_msg = f"> 5% ({max_frac:.3f}%) -- testable by DESI f*sigma_8"

    # ========================================================================
    # Step 7: Save results
    # ========================================================================
    np.savez('s59_growth_factor.npz',
        a_arr=a_arr,
        z_DESI=z_DESI, a_DESI=a_DESI,
        D_LCDM_norm=D_L_norm, f_LCDM=f_L, fsig8_LCDM=fsig8_L,
        D_wCDM_norm=D_W_norm, f_wCDM=f_W, fsig8_wCDM=fsig8_W,
        fsig8_LCDM_at_DESI=fsig8_L_DESI,
        fsig8_wCDM_at_DESI=fsig8_W_DESI,
        f_LCDM_at_DESI=f_L_DESI, f_wCDM_at_DESI=f_W_DESI,
        frac_diff=frac_diff, abs_diff=abs_diff,
        n_sigma=n_sigma, desi_err=desi_err,
        w0=np.float64(w0), wa=np.float64(wa),
        sigma8_LCDM=np.float64(sigma_8),
        sigma8_wCDM=np.float64(sigma8_W),
        growth_ratio=np.float64(growth_ratio),
        max_frac_diff_pct=np.float64(max_frac),
        max_nsigma=np.float64(max_nsig),
        gamma_LCDM=np.float64(gamma_LCDM),
        gamma_wCDM=np.float64(gamma_wCDM),
        verdict=np.array(verdict),
    )

    # ========================================================================
    # Step 8: Write text results
    # ========================================================================
    lines = []
    lines.append("GROWTH-FACTOR-59 Results")
    lines.append("=" * 70)
    lines.append(f"Framework: w_0 = {w0:.6f}, w_a = {wa:.6f} (constant w)")
    lines.append(f"LCDM: w = -1")
    lines.append(f"Omega_m = {Omega_m}, Omega_DE = {Omega_DE}")
    lines.append(f"sigma_8(LCDM) = {sigma_8:.4f}")
    lines.append(f"sigma_8(framework) = {sigma8_W:.4f}")
    lines.append(f"Growth ratio D_fw/D_LCDM(z=0) = {growth_ratio:.6f}")
    lines.append(f"Linder gamma: LCDM = {gamma_LCDM:.3f}, wCDM = {gamma_wCDM:.4f}")
    lines.append("")
    lines.append(f"{'z':>5s} {'a':>7s} {'fsig8_L':>10s} {'fsig8_fw':>10s} {'frac%':>8s} {'abs_diff':>10s} {'err':>8s} {'Nsig':>7s}")
    lines.append("-" * 70)
    for i, z in enumerate(z_DESI):
        lines.append(f"{z:5.1f} {a_DESI[i]:7.4f} {fsig8_L_DESI[i]:10.5f} {fsig8_W_DESI[i]:10.5f} "
                     f"{frac_diff[i]*100:7.3f}% {abs_diff[i]:10.5f} {desi_err[i]:8.4f} {n_sigma[i]:7.2f}")
    lines.append("-" * 70)
    lines.append(f"Max fractional difference: {max_frac:.3f}%")
    lines.append(f"Max N-sigma: {max_nsig:.2f}")
    lines.append("")
    lines.append(f"GATE: GROWTH-FACTOR-59 = {verdict}")
    lines.append(f"  {verdict_msg}")
    lines.append("")
    lines.append(f"f(z) at DESI bins:")
    for i, z in enumerate(z_DESI):
        lines.append(f"  z={z:.1f}: f_L={f_L_DESI[i]:.5f}, f_fw={f_W_DESI[i]:.5f}, "
                     f"diff={(f_W_DESI[i]-f_L_DESI[i])/f_L_DESI[i]*100:.3f}%")

    with open('s59_growth_factor_results.txt', 'w') as f:
        f.write('\n'.join(lines))

    # ========================================================================
    # Step 9: Plot
    # ========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(r'GROWTH-FACTOR-59: $f\cdot\sigma_8$ comparison ($w_0 = %.3f$ vs $\Lambda$CDM)' % w0,
                 fontsize=14, fontweight='bold')

    # Panel 1: f*sigma_8(z)
    ax = axes[0, 0]
    z_plot = 1.0/a_arr - 1.0
    mask = z_plot < 3.0
    ax.plot(z_plot[mask], fsig8_L[mask], 'b-', lw=2, label=r'$\Lambda$CDM ($w = -1$)')
    ax.plot(z_plot[mask], fsig8_W[mask], 'r--', lw=2, label=r'Framework ($w_0 = %.3f$)' % w0)
    ax.errorbar(z_DESI, fsig8_L_DESI, yerr=desi_err, fmt='bs', ms=8,
                capsize=4, label=r'DESI 1$\sigma$ ($\Lambda$CDM pred.)')
    ax.set_xlabel('Redshift z')
    ax.set_ylabel(r'$f \cdot \sigma_8(z)$')
    ax.set_xlim(0, 2.5)
    ax.legend(fontsize=9)
    ax.set_title(r'Growth rate $f \cdot \sigma_8$')
    ax.grid(True, alpha=0.3)

    # Panel 2: Fractional difference
    ax = axes[0, 1]
    frac_curve = (fsig8_W - fsig8_L) / fsig8_L * 100
    ax.plot(z_plot[mask], frac_curve[mask], 'k-', lw=2)
    ax.scatter(z_DESI, frac_diff*100, c='red', s=80, zorder=5, label='DESI z-bins')
    for i, z in enumerate(z_DESI):
        err_pct = desi_err[i] / fsig8_L_DESI[i] * 100
        ax.fill_between([z-0.05, z+0.05], [-err_pct]*2, [err_pct]*2,
                        alpha=0.2, color='blue')  # (local)
    ax.axhline(0, color='gray', ls=':', lw=0.5)
    ax.axhline(1, color='orange', ls='--', lw=0.8, alpha=0.7, label='1% threshold')
    ax.axhline(-1, color='orange', ls='--', lw=0.8, alpha=0.7)
    ax.axhline(5, color='red', ls='-.', lw=0.8, alpha=0.7, label='5% threshold')
    ax.axhline(-5, color='red', ls='-.', lw=0.8, alpha=0.7)
    ax.set_xlabel('Redshift z')
    ax.set_ylabel(r'$\Delta(f\sigma_8) / (f\sigma_8)_{\Lambda CDM}$ [%]')
    ax.set_xlim(0, 2.5)
    ax.legend(fontsize=8)
    ax.set_title('Fractional difference (max = %.2f%%)' % max_frac)
    ax.grid(True, alpha=0.3)

    # Panel 3: Growth factor D(a)
    ax = axes[1, 0]
    ax.plot(a_arr, D_L_norm, 'b-', lw=2, label=r'$D(a)$ $\Lambda$CDM')
    ax.plot(a_W, D_W_norm * growth_ratio, 'r--', lw=2,
            label=r'$D(a)$ framework ($\times %.4f$)' % growth_ratio)
    ax.plot(a_arr, a_arr/a_arr[-1], 'g:', lw=1, alpha=0.5, label=r'$D = a$ (matter dom.)')
    ax.set_xlabel('Scale factor a')
    ax.set_ylabel(r'$D(a) / D_{\Lambda CDM}(1)$')
    ax.legend(fontsize=9)
    ax.set_title('Linear growth factor')
    ax.grid(True, alpha=0.3)

    # Panel 4: N-sigma detectability
    ax = axes[1, 1]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars = ax.bar(range(len(z_DESI)), n_sigma, color=colors, edgecolor='black', lw=0.8)
    ax.set_xticks(range(len(z_DESI)))
    ax.set_xticklabels(['z=%.1f' % z for z in z_DESI])
    ax.set_ylabel(r'$N_\sigma$ detectability')
    ax.axhline(1, color='orange', ls='--', lw=1.5, label=r'1$\sigma$')
    ax.axhline(2, color='red', ls='--', lw=1.5, label=r'2$\sigma$')
    ax.set_title('DESI detectability (max = %.2f)' % max_nsig)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, axis='y')
    for bar, val in zip(bars, n_sigma):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                '%.2f' % val, ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig('s59_growth_factor.png', dpi=150, bbox_inches='tight')

    # ========================================================================
    # Step 10: Write completion marker
    # ========================================================================
    with open('_s59_done.txt', 'w') as f:
        f.write(f"DONE\nverdict={verdict}\nmax_frac={max_frac:.3f}\nmax_nsig={max_nsig:.2f}\n")
        f.write(f"growth_ratio={growth_ratio:.6f}\nsigma8_W={sigma8_W:.4f}\n")
        f.write(f"w0={w0:.6f}\n")

except Exception as e:
    with open('_s59_error.txt', 'w') as f:
        f.write(f"ERROR: {e}\n")
        f.write(traceback.format_exc())
