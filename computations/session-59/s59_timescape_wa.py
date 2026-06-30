#!/usr/bin/env python3
"""
TIMESCAPE-WA-59: Substrate Compaction Timescape
================================================
Session 59, Wave 4, Hypothesis 1 (W4H-1)
Agent: Katie Mack (Cosmic Bridge)

Physics: The SU(3) fiber's Jensen parameter tau varies spatially with local
matter density (substrate compaction). Voids have less backreaction -> lower
effective tau. Walls/filaments -> higher tau near fold. This creates a
Wiltshire-type clock-rate variance that generates apparent w_a != 0 from
a framework with intrinsic w_a = 0.

Gate: TIMESCAPE-WA-59
  PASS: |w_a_apparent| > 0.3
  FAIL: |w_a_apparent| < 0.01
  INFO: |w_a_apparent| in [0.01, 0.3]
"""

import sys
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASEDIR)

LOGPATH = os.path.join(BASEDIR, "s59_timescape_wa_log.txt")

import numpy as np
from scipy.optimize import curve_fit

# Redirect all output to log
log = open(LOGPATH, "w")

def pr(msg=""):
    log.write(str(msg) + "\n")
    log.flush()

try:
    from canonical_constants import (
        tau_fold, d2S_fold, a2_fold, a0_fold, a4_fold,
        M_KK_gravity, M_KK_kerner, M_KK,
        M_Pl_reduced, M_Pl_unreduced,
        H_0_km_s_Mpc,
        Omega_m, Omega_Lambda,
        rho_crit_GeV4, rho_Lambda_obs, clock_coeff,
        c_light_km_s,
        N_cells, dS_fold, S_fold,
        G_DeWitt, Z_fold,
        dt_transit, v_terminal,
    )
    pr("Canonical constants loaded.")

    # Load input data
    sa_data = np.load(os.path.join(BASEDIR, "s58_sa_saddle.npz"), allow_pickle=True)
    fried_data = np.load(os.path.join(BASEDIR, "s58_friedmann_derivation.npz"), allow_pickle=True)
    w_data = np.load(os.path.join(BASEDIR, "s58_w_desi.npz"), allow_pickle=True)
    pr("Input data loaded.")

    # Extract arrays
    a2_spectrum = sa_data["a2_spectrum"]
    tau_sweep = sa_data["tau_sweep"]
    w_0_A = float(w_data["w_0_A"])
    desi_wa = float(w_data["desi_dr2_wa"])
    desi_wa_e = float(w_data["desi_dr2_wa_e"])
    N_factor = float(fried_data["M_Pl_ratio"])

    out = {}

    # ================================================================
    #  Step 1: delta_tau from two routes
    # ================================================================

    fold_idx = np.argmin(np.abs(tau_sweep - tau_fold))
    dtau = tau_sweep[1] - tau_sweep[0]

    # Numerical da2/dtau at fold
    if fold_idx > 0 and fold_idx < len(tau_sweep) - 1:
        da2 = (a2_spectrum[fold_idx + 1] - a2_spectrum[fold_idx - 1]) / (2 * dtau)
    else:
        da2 = (a2_spectrum[fold_idx] - a2_spectrum[fold_idx - 1]) / dtau

    a2_fold_val = a2_spectrum[fold_idx]
    frac_da2 = da2 / a2_fold_val

    pr(f"\nStep 1: Backreaction")
    pr(f"  tau_fold = {tau_fold}")
    pr(f"  fold_idx = {fold_idx}")
    pr(f"  a2_at_fold = {a2_fold_val:.4f}")
    pr(f"  da2/dtau = {da2:.4f}")
    pr(f"  frac_da2 = {frac_da2:.6f}")

    # Route 1: Matter backreaction on SA
    rho_m_MKK4 = Omega_m * rho_crit_GeV4 / M_KK**4
    delta_tau_per_delta_route1 = rho_m_MKK4 * abs(frac_da2) / d2S_fold
    pr(f"  rho_matter/M_KK^4 = {rho_m_MKK4:.3e}")
    pr(f"  Route 1: delta_tau/delta = {delta_tau_per_delta_route1:.3e}")

    # Route 2: KZ-derived tau variance
    delta_tau_KZ = dt_transit * v_terminal
    sigma_tau = delta_tau_KZ / np.sqrt(N_cells)
    delta_tau_eff = sigma_tau  # conservative 1-sigma void-wall separation

    pr(f"\n  Route 2: KZ variance")
    pr(f"  dt_transit = {dt_transit:.6f}")
    pr(f"  v_terminal = {v_terminal:.3f}")
    pr(f"  delta_tau_KZ = {delta_tau_KZ:.6f}")
    pr(f"  sigma_tau = {sigma_tau:.6f}")
    pr(f"  delta_tau_eff = {delta_tau_eff:.6f}")
    pr(f"  Fractional = {delta_tau_eff/tau_fold:.4f}")

    out["delta_tau_per_delta_route1"] = np.array(delta_tau_per_delta_route1)
    out["delta_tau_KZ"] = np.array(delta_tau_KZ)
    out["sigma_tau"] = np.array(sigma_tau)
    out["delta_tau_eff"] = np.array(delta_tau_eff)

    # ================================================================
    #  Step 2: Lapse variation
    # ================================================================

    delta_G_over_G = -frac_da2 * delta_tau_eff
    delta_N_over_N = 0.5 * delta_G_over_G

    pr(f"\nStep 2: Lapse")
    pr(f"  delta_G/G = {delta_G_over_G:.6e}")
    pr(f"  delta_N/N = {delta_N_over_N:.6e}")

    out["delta_G_over_G"] = np.array(delta_G_over_G)
    out["delta_N_over_N"] = np.array(delta_N_over_N)

    # ================================================================
    #  Step 3: Wiltshire D_H correction
    # ================================================================

    f_void = 0.76  # Wiltshire 2007  # (local)

    z_DESI = np.array([0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 2.0, 2.5])

    def H_LCDM(z):
        return H_0_km_s_Mpc * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)

    def H_CPL(z, w0, wa):
        zf = z / (1.0 + z)
        rDE = (1+z)**(3*(1+w0+wa)) * np.exp(-3*wa*zf)
        return H_0_km_s_Mpc * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda * rDE)

    def DH_CPL(z, w0, wa):
        return c_light_km_s / H_CPL(z, w0, wa)

    DH_fw = c_light_km_s / H_CPL(z_DESI, w_0_A, 0.0)

    corr_factor = f_void * delta_N_over_N

    pr(f"\nStep 3: D_H correction")
    pr(f"  f_void = {f_void}")
    pr(f"  Correction factor = {corr_factor:.6e}")
    pr(f"  As percentage = {abs(corr_factor)*100:.6f}%")

    # Three alpha values
    alphas = [0.0, 0.3, 0.5]
    DH_corr = {}
    for alpha in alphas:
        corr = 1.0 + corr_factor * (1 + z_DESI)**alpha
        DH_corr[alpha] = DH_fw * corr

    out["z_DESI"] = z_DESI
    out["DH_framework"] = DH_fw
    out["corr_factor"] = np.array(corr_factor)

    # ================================================================
    #  Step 4: CPL fit
    # ================================================================

    pr(f"\nStep 4: CPL fits")

    w0_app = {}
    wa_app = {}
    for alpha in alphas:
        target = DH_corr[alpha]
        try:
            popt, pcov = curve_fit(DH_CPL, z_DESI, target, p0=[-0.92, -0.01],
                                   bounds=([-2.0, -3.0], [0.0, 3.0]))
            w0_app[alpha] = popt[0]
            wa_app[alpha] = popt[1]
            rms = np.sqrt(np.mean((DH_CPL(z_DESI, *popt) - target)**2))
            pr(f"  alpha={alpha}: w0={popt[0]:.8f}, wa={popt[1]:.8f}, rms={rms:.3e}")
        except Exception as e:
            pr(f"  alpha={alpha}: FAILED: {e}")
            w0_app[alpha] = w_0_A
            wa_app[alpha] = 0.0

    best_alpha = 0.3  # (local)
    wa_result = wa_app.get(best_alpha, 0.0)
    w0_result = w0_app.get(best_alpha, w_0_A)

    pr(f"\n  BEST (alpha={best_alpha}): w0={w0_result:.8f}, wa={wa_result:.8f}")
    pr(f"  |w_a| = {abs(wa_result):.8f}")

    out["w0_apparent"] = np.array([w0_app.get(a, 0) for a in alphas])
    out["wa_apparent"] = np.array([wa_app.get(a, 0) for a in alphas])
    out["alphas"] = np.array(alphas)
    out["wa_result"] = np.array(wa_result)
    out["w0_result"] = np.array(w0_result)

    # ================================================================
    #  Step 4b: What correction is NEEDED?
    # ================================================================

    def wa_from_corr(c, z_arr, aw=0.3):
        target = DH_fw * (1.0 + c * (1 + z_arr)**aw)
        try:
            popt, _ = curve_fit(DH_CPL, z_arr, target, p0=[-0.92, -0.5],
                                bounds=([-2.0, -5.0], [0.0, 5.0]))
            return popt[1]
        except:
            return 0.0

    corr_scan = np.linspace(-0.15, 0.15, 201)
    wa_scan = np.array([wa_from_corr(c, z_DESI, 0.3) for c in corr_scan])

    idx_target = np.argmin(np.abs(wa_scan - desi_wa))
    corr_needed = corr_scan[idx_target]
    delta_N_needed = corr_needed / f_void

    shortfall = abs(delta_N_needed / delta_N_over_N) if abs(delta_N_over_N) > 1e-30 else np.inf

    pr(f"\nStep 4b: Required correction")
    pr(f"  Correction needed = {corr_needed:.6f}")
    pr(f"  delta_N/N needed = {delta_N_needed:.6f}")
    pr(f"  Framework delta_N/N = {delta_N_over_N:.6e}")
    pr(f"  Shortfall = {shortfall:.1f}x")

    out["corr_scan"] = corr_scan
    out["wa_scan"] = wa_scan
    out["corr_needed"] = np.array(corr_needed)
    out["delta_N_needed"] = np.array(delta_N_needed)
    out["shortfall"] = np.array(shortfall)

    # ================================================================
    #  Step 5: ALPHA-ENV-43 cross-check
    # ================================================================

    delta_alpha_vw = abs(2 * clock_coeff * delta_tau_eff)
    alpha_target = 1e-6

    pr(f"\nStep 5: ALPHA-ENV-43")
    pr(f"  clock_coeff = {clock_coeff}")
    pr(f"  delta_alpha/alpha (void-wall) = {delta_alpha_vw:.3e}")
    pr(f"  Target = {alpha_target:.1e}")

    if delta_tau_eff > 0:
        delta_tau_for_alpha = alpha_target / abs(2 * clock_coeff)
        alpha_shortfall = delta_tau_for_alpha / delta_tau_eff
        pr(f"  delta_tau needed for alpha = {delta_tau_for_alpha:.6f}")
        pr(f"  Alpha shortfall = {alpha_shortfall:.1f}x")
    else:
        alpha_shortfall = np.inf

    out["delta_alpha_vw"] = np.array(delta_alpha_vw)
    out["alpha_shortfall"] = np.array(alpha_shortfall)

    # Also: what delta_tau is needed for DESI w_a?
    if abs(frac_da2) > 0:
        delta_tau_for_wa = 2 * abs(delta_N_needed) / abs(frac_da2)
        pr(f"\n  delta_tau needed for DESI wa = {delta_tau_for_wa:.4f}")
        pr(f"  = {delta_tau_for_wa/tau_fold*100:.1f}% of tau_fold")
        out["delta_tau_for_wa"] = np.array(delta_tau_for_wa)

    # ================================================================
    #  Step 6: Gate
    # ================================================================

    wa_abs = abs(wa_result)
    if wa_abs > 0.3:
        verdict = "PASS"
        detail = f"|w_a_apparent| = {wa_abs:.4f} > 0.3"
    elif wa_abs < 0.01:
        verdict = "FAIL"
        detail = (
            f"|w_a_apparent| = {wa_abs:.2e} < 0.01. "
            f"Root cause: KZ tau variance sigma_tau={sigma_tau:.4f} gives "
            f"delta_N/N={delta_N_over_N:.2e}, need {abs(delta_N_needed):.4f} "
            f"({shortfall:.0f}x shortfall). Backreaction route gives "
            f"delta_tau ~ {delta_tau_per_delta_route1:.2e}/delta (10^120 below stiffness). "
            f"Neither route approaches DESI w_a={desi_wa}."
        )
    else:
        verdict = "INFO"
        detail = f"|w_a_apparent| = {wa_abs:.4f} in [0.01, 0.3]"

    pr(f"\n{'='*70}")
    pr(f"  GATE: TIMESCAPE-WA-59")
    pr(f"  VERDICT: {verdict}")
    pr(f"  {detail}")
    pr(f"{'='*70}")

    out["gate_name"] = np.array(["TIMESCAPE-WA-59"])
    out["gate_verdict"] = np.array([verdict])
    out["gate_detail"] = np.array([detail])

    # ================================================================
    #  Summary
    # ================================================================

    pr(f"\n{'='*70}")
    pr(f"  SUMMARY")
    pr(f"{'='*70}")
    pr(f"  tau_fold                    = {tau_fold}")
    pr(f"  d2S_fold                    = {d2S_fold:.1f}")
    pr(f"  m_tau                       = {np.sqrt(d2S_fold/Z_fold):.3f} M_KK")
    pr(f"  rho_m / M_KK^4             = {rho_m_MKK4:.3e}")
    pr(f"  Route 1 delta_tau/delta     = {delta_tau_per_delta_route1:.3e}")
    pr(f"  Route 2 sigma_tau (KZ)      = {sigma_tau:.6f}")
    pr(f"  Route 2 delta_tau_eff       = {delta_tau_eff:.6f}")
    pr(f"  frac_da2                    = {frac_da2:.6f}")
    pr(f"  delta_G/G                   = {delta_G_over_G:.6e}")
    pr(f"  delta_N/N                   = {delta_N_over_N:.6e}")
    pr(f"  Wiltshire correction        = {abs(corr_factor)*100:.6f}%")
    pr(f"  w_a_apparent                = {wa_result:.8f}")
    pr(f"  |w_a_apparent|              = {abs(wa_result):.8f}")
    pr(f"  Needed delta_N/N            = {abs(delta_N_needed):.6f}")
    pr(f"  Shortfall                   = {shortfall:.0f}x")
    pr(f"  delta_alpha/alpha (void-wall)= {delta_alpha_vw:.3e}")
    pr(f"  ALPHA-ENV-43 target         = {alpha_target:.1e}")

    # ================================================================
    #  Plotting
    # ================================================================

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("TIMESCAPE-WA-59: Substrate Compaction Timescape", fontsize=14, fontweight="bold")

    # Panel 1: a_2(tau) and KZ band
    ax1 = axes[0, 0]
    ax1.plot(tau_sweep, a2_spectrum, "b-", lw=2, label=r"$a_2(\tau)$")
    ax1.axvline(tau_fold, color="r", ls="--", lw=1, label=f"$\\tau_{{fold}}$={tau_fold}")
    tau_t = np.linspace(tau_fold - 0.05, tau_fold + 0.05, 50)
    a2_t = a2_fold_val + da2 * (tau_t - tau_fold)
    ax1.plot(tau_t, a2_t, "r-", lw=1.5, alpha=0.7, label=f"slope={da2:.1f}")
    ax1.axvspan(tau_fold - sigma_tau, tau_fold + sigma_tau, alpha=0.2, color="orange",
                label=f"KZ $\\sigma_\\tau$={sigma_tau:.4f}")
    ax1.set_xlabel(r"$\tau$")
    ax1.set_ylabel(r"$a_2$")
    ax1.set_title(r"$a_2(\tau)$ and KZ tau variance")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: D_H correction vs z
    ax2 = axes[0, 1]
    for alpha in alphas:
        pct = (DH_corr[alpha] / DH_fw - 1) * 100
        ax2.plot(z_DESI, pct, "o-", ms=4, label=f"$\\alpha$={alpha}")
    ax2.set_xlabel("Redshift $z$")
    ax2.set_ylabel(r"$\Delta D_H / D_H$ (%)")
    ax2.set_title("Timescape correction magnitude")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.annotate(f"Peak: {abs(corr_factor)*100:.4f}%",
                 xy=(0.5, 0.9), xycoords="axes fraction", fontsize=9,
                 bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    # Panel 3: w_a scan
    ax3 = axes[1, 0]
    ax3.plot(corr_scan * 100, wa_scan, "b-", lw=2)
    ax3.axhline(desi_wa, color="r", ls="--", lw=1, label=f"DESI: $w_a$={desi_wa}")
    ax3.axhline(0, color="gray", ls=":", lw=0.5)
    ax3.axvline(corr_factor * 100, color="green", ls="-.", lw=1.5,
                label=f"Framework: {corr_factor*100:.4f}%")
    ax3.axvline(corr_needed * 100, color="orange", ls="-.", lw=1.5,
                label=f"Needed: {corr_needed*100:.2f}%")
    ax3.set_xlabel("Correction amplitude (%)")
    ax3.set_ylabel(r"$w_a^{\rm apparent}$")
    ax3.set_title(r"Apparent $w_a$ vs correction")
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    # Panel 4: Summary text
    ax4 = axes[1, 1]
    ax4.axis("off")
    txt = (
        f"GATE: TIMESCAPE-WA-59\n"
        f"VERDICT: {verdict}\n\n"
        f"Route 1 (backreaction):\n"
        f"  delta_tau/delta = {delta_tau_per_delta_route1:.2e}\n"
        f"  (10^120 below SA stiffness)\n\n"
        f"Route 2 (KZ variance):\n"
        f"  sigma_tau = {sigma_tau:.4f}\n"
        f"  delta_N/N = {delta_N_over_N:.2e}\n"
        f"  |w_a| = {abs(wa_result):.2e}\n\n"
        f"DESI requires:\n"
        f"  delta_N/N = {abs(delta_N_needed):.4f}\n"
        f"  Shortfall: {shortfall:.0f}x\n\n"
        f"ALPHA-ENV-43:\n"
        f"  Framework: {delta_alpha_vw:.2e}\n"
        f"  Target: {alpha_target:.1e}\n"
        f"  Shortfall: {alpha_shortfall:.0f}x"
    )
    ax4.text(0.05, 0.95, txt, transform=ax4.transAxes,
             fontsize=9, va="top", fontfamily="monospace",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))

    plt.tight_layout()
    plotpath = os.path.join(BASEDIR, "s59_timescape_wa.png")
    plt.savefig(plotpath, dpi=150, bbox_inches="tight")
    pr(f"\nPlot saved: {plotpath}")

    # Save npz
    npzpath = os.path.join(BASEDIR, "s59_timescape_wa.npz")
    np.savez(npzpath, **out)
    pr(f"Data saved: {npzpath}")

    pr("\n=== TIMESCAPE-WA-59 COMPLETE ===")

except Exception as e:
    import traceback
    pr(f"\n=== ERROR ===\n{traceback.format_exc()}")

finally:
    log.close()
