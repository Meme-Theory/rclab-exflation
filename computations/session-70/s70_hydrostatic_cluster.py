#!/usr/bin/env python3
"""
s70_hydrostatic_cluster.py -- HYDROSTATIC-CLUSTER-70: Cluster Mass Function
with Hydrostatic Mass Bias Calibration
========================================================================
Gate: HYDROSTATIC-CLUSTER-70
  INFO: Report chi^2/dof at three bias calibrations; identify crossover
        with LCDM.

Physics:
  PVD-CLUST-69 found chi^2/dof = 4.11 (FW) vs 3.69 (LCDM), with the
  tension partly driven by sigma_8 (FW: 0.793 vs LCDM: 0.811) and
  partly by the assumed mass threshold.

  The Planck SZ cluster count depends on the cluster mass function,
  which is calibrated via hydrostatic mass estimates.  The hydrostatic
  mass M_hyd is related to the true mass M_true by:

      M_hyd = (1-b) * M_true

  where (1-b) is the hydrostatic mass bias parameter.  This is the
  single largest systematic in cluster cosmology.  Published calibrations:

      (1-b) = 0.58 +/- 0.04  (Planck CMB lensing, Planck XX 2014)
      (1-b) = 0.62            (Planck CMB lensing lower bound)
      (1-b) = 0.73            (HSC/ACT WL, Miyatake+2019; Bocquet+2024)
      (1-b) = 0.80            (conservative upper bound, WtG/LoCuSS)

  Effect on mass threshold:  The SZ detection gives M_hyd.  The true
  mass used in the halo mass function is M_true = M_hyd / (1-b).
  A smaller (1-b) means masses are MORE biased low, so the TRUE mass
  threshold is HIGHER:

      log10(M_true_min) = log10(M_hyd_min) - log10(1-b)

  Since log10(1-b) < 0 for (1-b) < 1, the mass threshold INCREASES
  (fewer predicted clusters above threshold -- better match to observed
  counts, which are fewer than raw theory predicts).

  Method:
    1. Load S69 cluster data (sigma(M), growth factors, volume elements).
    2. At each (1-b) value, shift the mass threshold and recompute
       predicted cluster counts for both FW and LCDM.
    3. Fit overall normalization at each (1-b) to isolate the bias effect.
    4. Compute chi^2/dof for FW and LCDM at each (1-b).
    5. Find the crossover: at what (1-b) does FW become competitive
       with or beat LCDM?

  References:
    Planck Collaboration XX (2014), A&A 571, A20  [(1-b) calibration]
    Planck Collaboration XXIV (2016), A&A 594, A24  [cluster counts]
    Tinker et al. (2008), ApJ 688, 709  [halo mass function]
    Eisenstein & Hu (1998), ApJ 496, 605  [transfer function]
    Miyatake et al. (2019), ApJ 875, 63  [HSC WL mass calibration]
    von der Linden et al. (2014), MNRAS 443, 1973  [WtG calibration]
    Bocquet et al. (2024), PhRvD 110, 083510  [SPT-3G + WL]

Author: mack-cosmic-bridge
Session: 70, Task W4-A HYDROSTATIC-CLUSTER-70
"""

import os
import sys
import traceback

try:
    import numpy as np
    from scipy.integrate import quad, solve_ivp
    from scipy.interpolate import interp1d
    from scipy.optimize import minimize, brentq
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, SCRIPT_DIR)

    from canonical_constants import *

    LOGPATH = os.path.join(SCRIPT_DIR, "s70_hydrostatic_cluster_log.txt")
    log = open(LOGPATH, "w")

    def pr(msg=""):
        print(str(msg))
        log.write(str(msg) + "\n")
        log.flush()

    pr("=" * 78)
    pr("HYDROSTATIC-CLUSTER-70: Cluster Mass Function with Hydrostatic Bias")
    pr("=" * 78)

    # =========================================================================
    # 1. Load S69 cluster data
    # =========================================================================
    s69_path = os.path.join(SCRIPT_DIR, "s69_pvd08_cluster.npz")
    s69 = np.load(s69_path, allow_pickle=True)

    z_bin_edges = s69['z_bin_edges']
    z_bin_mid = s69['z_bin_mid']
    N_obs = s69['N_obs']
    N_obs_err = s69['N_obs_err']
    log10_M200_min_base = s69['log10_M200_min']  # baseline mass thresholds
    log10M_arr = s69['log10M_arr']               # mass grid for sigma(M)
    sigma_LCDM_z0 = s69['sigma_LCDM_z0']         # sigma(M) at z=0 for LCDM
    sigma_FW_z0 = s69['sigma_FW_z0']             # sigma(M) at z=0 for FW
    n_bins = len(z_bin_mid)

    sig8_fw = float(s69['sig8_FW'])    # 0.793
    sig8_lcdm = float(s69['sig8_LCDM'])  # 0.811
    ns_fw = float(s69['ns_FW'])        # 0.9595
    ns_lcdm = float(s69['ns_LCDM'])    # 0.9649
    w0_fw_val = float(s69['w0_fw'])    # -0.918

    pr(f"\nLoaded S69 data:")
    pr(f"  {n_bins} redshift bins, z = [{z_bin_edges[0]:.1f}, {z_bin_edges[-1]:.1f}]")
    pr(f"  N_obs = {N_obs}")
    pr(f"  Baseline log10(M200_min) = {log10_M200_min_base}")
    pr(f"  Framework: sigma_8={sig8_fw}, n_s={ns_fw}, w_0={w0_fw_val:.4f}")
    pr(f"  LCDM:      sigma_8={sig8_lcdm}, n_s={ns_lcdm}")

    # S69 reference chi^2/dof values
    chi2_dof_s69_LCDM = float(s69['chi2_dof_LCDM'])
    chi2_dof_s69_FW = float(s69['chi2_dof_FW'])
    pr(f"\nS69 reference (joint fit with cal + delta_M):")
    pr(f"  chi^2/dof(LCDM) = {chi2_dof_s69_LCDM:.3f}")
    pr(f"  chi^2/dof(FW)   = {chi2_dof_s69_FW:.3f}")

    # =========================================================================
    # 2. Cosmological functions (replicated from S69 for self-containment)
    # =========================================================================
    Om_m = Omega_m          # 0.315
    Om_b = Omega_b          # 0.0493
    Om_DE = 1.0 - Om_m     # 0.685
    h_hubble = H_0_km_s_Mpc / 100.0  # 0.674

    def E2_LCDM(a):
        return Om_m * a**(-3) + Om_DE

    def E2_wCDM(a, w0):
        return Om_m * a**(-3) + Om_DE * a**(-3.0 * (1.0 + w0))

    # Growth factor ODE
    def make_growth_rhs(e2_func, de2_func):
        def rhs(a, y):
            D, Dp = y
            e2 = e2_func(a)
            de2 = de2_func(a)
            coeff_Dp = 3.0 / a + 0.5 * de2 / e2
            coeff_D = 1.5 * Om_m / (a**5 * e2)
            Dpp = -coeff_Dp * Dp + coeff_D * D
            return [Dp, Dpp]
        return rhs

    def dE2_da_LCDM(a):
        return -3.0 * Om_m * a**(-4)

    def dE2_da_wCDM(a, w0):
        pw = -3.0 * (1.0 + w0)
        return -3.0 * Om_m * a**(-4) + pw * Om_DE * a**(pw - 1.0)

    a_init = 1e-4  # (local)
    a_final = 1.0  # (local)
    y0 = [a_init, 1.0]
    a_eval = np.linspace(a_init, a_final, 50000)

    pr("\nSolving growth factor ODEs...")
    rhs_L = make_growth_rhs(E2_LCDM, dE2_da_LCDM)
    sol_L = solve_ivp(rhs_L, [a_init, a_final], y0,
                      t_eval=a_eval, method='RK45', rtol=1e-12, atol=1e-15)
    assert sol_L.success, "LCDM growth ODE failed"

    rhs_FW = make_growth_rhs(
        lambda a: E2_wCDM(a, w0_fw_val),
        lambda a: dE2_da_wCDM(a, w0_fw_val))
    sol_FW = solve_ivp(rhs_FW, [a_init, a_final], y0,
                       t_eval=a_eval, method='RK45', rtol=1e-12, atol=1e-15)
    assert sol_FW.success, "FW growth ODE failed"

    D_L = sol_L.y[0] / sol_L.y[0][-1]
    D_FW = sol_FW.y[0] / sol_FW.y[0][-1]
    a_arr = sol_L.t

    D_L_interp = interp1d(a_arr, D_L, kind='cubic')
    D_FW_interp = interp1d(a_arr, D_FW, kind='cubic')

    pr(f"  Growth factors computed. D_FW/D_LCDM at z=0 = "
       f"{sol_FW.y[0][-1] / sol_L.y[0][-1]:.6f}")

    # Comoving volume element
    c_over_H0_h = c_light_km_s / 100.0  # Mpc/h

    def chi_func(z, e2_func):
        """Comoving distance in Mpc/h."""
        def integrand(zp):
            return 1.0 / np.sqrt(e2_func(1.0 / (1.0 + zp)))
        result, _ = quad(integrand, 0, z)
        return c_over_H0_h * result

    def dVdz_func(z, e2_func):
        """dV/(dz dOmega) in (Mpc/h)^3 / sr."""
        chi_z = chi_func(z, e2_func)
        E_z = np.sqrt(e2_func(1.0 / (1.0 + z)))
        return chi_z**2 * c_over_H0_h / E_z

    # Tinker+2008 parameters at Delta=200
    A0_T = 0.186  # (local)
    a0_T = 1.47  # (local)
    b0_T = 2.57  # (local)
    c0_T = 1.19  # (local)
    alpha_b_T = 10.0**(-(0.75 / np.log10(200.0 / 75.0))**1.2)

    def tinker_params(z):
        A = A0_T * (1.0 + z)**(-0.14)
        a = a0_T * (1.0 + z)**(-0.06)
        b = b0_T * (1.0 + z)**(-alpha_b_T)
        c = c0_T
        return A, a, b, c

    def tinker_f(sigma_val, z):
        A, a, b, c = tinker_params(z)
        return A * ((sigma_val / b)**(-a) + 1.0) * np.exp(-c / sigma_val**2)

    # Survey parameters
    f_sky = 0.65  # (local)
    Omega_sky = f_sky * 4.0 * np.pi
    rho_m_hunit = Om_m * 2.775e11  # M_sun / (Mpc/h)^3

    # Fine mass grid for integration
    log10M_fine = np.linspace(13.0, 15.5, 200)

    # =========================================================================
    # 3. Cluster count prediction function
    # =========================================================================
    def predicted_counts_bin(z_lo, z_hi, log10_Mmin, sigma_z0, D_interp,
                             e2_func, nz_sub=8):
        """
        Predicted cluster count in [z_lo, z_hi] above mass threshold M_min.
        """
        z_sub = np.linspace(z_lo, z_hi, nz_sub + 1)
        total = 0.0  # (local)

        for j in range(nz_sub):
            z_mid_j = 0.5 * (z_sub[j] + z_sub[j + 1])
            dz = z_sub[j + 1] - z_sub[j]
            a_mid = 1.0 / (1.0 + z_mid_j)

            if a_mid < a_init:
                D_z = a_mid
            else:
                D_z = float(D_interp(a_mid))

            dvdz = dVdz_func(z_mid_j, e2_func)

            mask = log10M_fine >= log10_Mmin
            lM_grid = log10M_fine[mask]
            if len(lM_grid) < 2:
                continue

            sigma_interp_func = interp1d(log10M_arr, sigma_z0, kind='cubic',
                                          fill_value='extrapolate')
            sig_z0_grid = sigma_interp_func(lM_grid)
            sig_z_grid = sig_z0_grid * D_z

            dlnsigma_inv = np.gradient(-np.log(sig_z0_grid),
                                        lM_grid * np.log(10.0))

            f_grid = np.array([tinker_f(s, z_mid_j) for s in sig_z_grid])

            M_grid = 10.0**lM_grid
            dndlnM = (rho_m_hunit / M_grid) * f_grid * np.abs(dlnsigma_inv)

            lnM_grid = lM_grid * np.log(10.0)
            N_mass = np.trapezoid(dndlnM, lnM_grid)

            total += dvdz * Omega_sky * N_mass * dz

        return total

    def compute_all_bins(log10_Mmin_arr, sigma_z0, D_interp, e2_func):
        """Compute predicted counts in all bins."""
        N_pred = np.zeros(n_bins)
        for i in range(n_bins):
            N_pred[i] = predicted_counts_bin(
                z_bin_edges[i], z_bin_edges[i + 1],
                log10_Mmin_arr[i], sigma_z0, D_interp, e2_func)
        return N_pred

    # =========================================================================
    # 4. Hydrostatic bias calibration scan
    # =========================================================================
    # (1-b) relates hydrostatic mass to true mass:
    #   M_hyd = (1-b) * M_true
    #   M_true = M_hyd / (1-b)
    #
    # The SZ survey selects on M_hyd > M_hyd_min (approximately).
    # The true mass threshold for the halo mass function is:
    #   log10(M_true_min) = log10(M_hyd_min) - log10(1-b)
    #
    # Since (1-b) < 1, log10(1-b) < 0, so M_true_min > M_hyd_min.
    # A larger bias (smaller 1-b) raises the true threshold -> fewer
    # clusters predicted -> better match if theory overpredicts.

    one_minus_b_values = np.array([0.62, 0.73, 0.80])
    one_minus_b_labels = [
        "(1-b)=0.62 [Planck CMB lensing, lower bound]",
        "(1-b)=0.73 [HSC WL calibration]",
        "(1-b)=0.80 [Conservative upper bound]"
    ]

    # Also scan a fine grid for crossover identification
    one_minus_b_fine = np.linspace(0.55, 0.90, 36)

    pr("\n" + "=" * 78)
    pr("HYDROSTATIC BIAS SCAN")
    pr("=" * 78)
    pr(f"\nBaseline mass thresholds log10(M200_min/[Msun/h]):")
    for i in range(n_bins):
        pr(f"  z = {z_bin_mid[i]:.2f}: {log10_M200_min_base[i]:.2f}")

    pr(f"\n  (1-b)    log10(1-b)  delta_M")
    for ob in one_minus_b_values:
        delta_M = -np.log10(ob)
        pr(f"  {ob:.2f}     {np.log10(ob):+.4f}     {delta_M:+.4f} dex")

    # =========================================================================
    # 5. Compute chi^2/dof at each (1-b) for FW and LCDM
    # =========================================================================
    # At each (1-b), shift the mass threshold and fit normalization only
    # (1 free parameter: cal).  dof = n_bins - 1 = 6.

    def chi2_at_bias(one_minus_b, sigma_z0, D_interp, e2_func):
        """
        Compute best-fit chi^2 at a given (1-b) bias calibration.

        Mass threshold shift: delta_M = -log10(1-b)
        Free parameter: overall normalization cal.
        """
        delta_M = -np.log10(one_minus_b)
        log10_Mmin_shifted = log10_M200_min_base + delta_M

        N_pred = compute_all_bins(log10_Mmin_shifted, sigma_z0,
                                   D_interp, e2_func)

        # Best-fit normalization (analytic for linear scaling):
        # chi^2 = sum((N_obs - cal*N_pred)^2 / err^2)
        # d(chi^2)/d(cal) = 0 =>
        # cal = sum(N_obs*N_pred/err^2) / sum(N_pred^2/err^2)
        mask = N_obs_err > 0
        w = 1.0 / N_obs_err[mask]**2  # (local)
        cal = np.sum(N_obs[mask] * N_pred[mask] * w) / np.sum(N_pred[mask]**2 * w)

        N_cal = cal * N_pred
        chi2 = np.sum(((N_obs[mask] - N_cal[mask]) / N_obs_err[mask])**2)
        dof = np.sum(mask) - 1  # 7 bins - 1 free param = 6

        return chi2, float(dof), cal, N_pred, N_cal

    pr("\n" + "-" * 78)
    pr("Results at three specified (1-b) calibrations:")
    pr("-" * 78)

    results_three = {}
    for idx, ob in enumerate(one_minus_b_values):
        delta_M = -np.log10(ob)

        chi2_L, dof_L, cal_L, Npred_L, Ncal_L = chi2_at_bias(
            ob, sigma_LCDM_z0, D_L_interp, E2_LCDM)
        chi2_F, dof_F, cal_F, Npred_F, Ncal_F = chi2_at_bias(
            ob, sigma_FW_z0, D_FW_interp,
            lambda a, w0=w0_fw_val: E2_wCDM(a, w0))

        results_three[ob] = {
            'chi2_L': chi2_L, 'dof_L': dof_L, 'cal_L': cal_L,
            'Npred_L': Npred_L, 'Ncal_L': Ncal_L,
            'chi2_F': chi2_F, 'dof_F': dof_F, 'cal_F': cal_F,
            'Npred_F': Npred_F, 'Ncal_F': Ncal_F,
            'delta_M': delta_M,
        }

        pr(f"\n  {one_minus_b_labels[idx]}")
        pr(f"    delta_M = {delta_M:+.4f} dex")
        pr(f"    LCDM:      cal = {cal_L:.4f}, chi^2 = {chi2_L:.2f}, "
           f"chi^2/dof = {chi2_L/dof_L:.3f} (dof = {int(dof_L)})")
        pr(f"    Framework: cal = {cal_F:.4f}, chi^2 = {chi2_F:.2f}, "
           f"chi^2/dof = {chi2_F/dof_F:.3f} (dof = {int(dof_F)})")
        pr(f"    Delta chi^2 (LCDM - FW) = {chi2_L - chi2_F:+.3f}")
        pr(f"    {'FW better' if chi2_F < chi2_L else 'LCDM better'}")

        pr(f"\n    Bin-by-bin (calibrated):")
        pr(f"    {'z':>5s} {'N_obs':>7s} {'err':>6s} {'N_L':>8s} {'N_F':>8s} "
           f"{'res_L':>7s} {'res_F':>7s}")
        for i in range(n_bins):
            res_L = (N_obs[i] - Ncal_L[i]) / N_obs_err[i]
            res_F = (N_obs[i] - Ncal_F[i]) / N_obs_err[i]
            pr(f"    {z_bin_mid[i]:5.2f} {N_obs[i]:7.0f} {N_obs_err[i]:6.1f} "
               f"{Ncal_L[i]:8.1f} {Ncal_F[i]:8.1f} "
               f"{res_L:7.2f} {res_F:7.2f}")

    # =========================================================================
    # 6. Fine scan for crossover identification
    # =========================================================================
    pr("\n" + "-" * 78)
    pr("Fine scan: chi^2/dof vs (1-b)")
    pr("-" * 78)

    chi2dof_L_fine = np.zeros(len(one_minus_b_fine))
    chi2dof_F_fine = np.zeros(len(one_minus_b_fine))
    cal_L_fine = np.zeros(len(one_minus_b_fine))
    cal_F_fine = np.zeros(len(one_minus_b_fine))
    delta_chi2_fine = np.zeros(len(one_minus_b_fine))

    for idx, ob in enumerate(one_minus_b_fine):
        chi2_L, dof_L, cl, _, _ = chi2_at_bias(
            ob, sigma_LCDM_z0, D_L_interp, E2_LCDM)
        chi2_F, dof_F, cf, _, _ = chi2_at_bias(
            ob, sigma_FW_z0, D_FW_interp,
            lambda a, w0=w0_fw_val: E2_wCDM(a, w0))

        chi2dof_L_fine[idx] = chi2_L / dof_L
        chi2dof_F_fine[idx] = chi2_F / dof_F
        cal_L_fine[idx] = cl
        cal_F_fine[idx] = cf
        delta_chi2_fine[idx] = chi2_L - chi2_F

    pr(f"\n  {'(1-b)':>6s} {'chi2/dof_L':>11s} {'chi2/dof_F':>11s} "
       f"{'Delta_chi2':>11s} {'Winner':>8s}")
    for idx in range(0, len(one_minus_b_fine), 3):
        ob = one_minus_b_fine[idx]
        winner = "FW" if delta_chi2_fine[idx] > 0 else "LCDM"
        pr(f"  {ob:6.3f}  {chi2dof_L_fine[idx]:11.3f}  {chi2dof_F_fine[idx]:11.3f}  "
           f"{delta_chi2_fine[idx]:+11.3f}  {winner:>8s}")

    # =========================================================================
    # 7. Find crossover point
    # =========================================================================
    # Crossover = where Delta chi^2 (LCDM - FW) = 0, i.e., FW = LCDM
    # FW is better where Delta chi^2 > 0.

    pr("\n" + "-" * 78)
    pr("Crossover analysis:")
    pr("-" * 78)

    # Check if crossover exists in the scanned range
    sign_changes = np.where(np.diff(np.sign(delta_chi2_fine)))[0]

    if len(sign_changes) > 0:
        # Interpolate to find crossover
        for sc in sign_changes:
            ob_lo = one_minus_b_fine[sc]
            ob_hi = one_minus_b_fine[sc + 1]
            dc_lo = delta_chi2_fine[sc]
            dc_hi = delta_chi2_fine[sc + 1]
            # Linear interpolation
            ob_cross = ob_lo + (ob_hi - ob_lo) * (-dc_lo) / (dc_hi - dc_lo)
            pr(f"  Crossover at (1-b) = {ob_cross:.4f}")
            pr(f"    For (1-b) < {ob_cross:.4f}: "
               f"{'FW better' if dc_lo > 0 else 'LCDM better'}")
            pr(f"    For (1-b) > {ob_cross:.4f}: "
               f"{'FW better' if dc_hi > 0 else 'LCDM better'}")
    else:
        # No crossover -- one model dominates throughout
        if delta_chi2_fine[0] > 0:
            pr(f"  NO CROSSOVER: FW is better than LCDM across entire "
               f"(1-b) range [{one_minus_b_fine[0]:.2f}, {one_minus_b_fine[-1]:.2f}]")
        else:
            pr(f"  NO CROSSOVER: LCDM is better than FW across entire "
               f"(1-b) range [{one_minus_b_fine[0]:.2f}, {one_minus_b_fine[-1]:.2f}]")

    # Find optimal (1-b) for each model
    idx_best_L = np.argmin(chi2dof_L_fine)
    idx_best_F = np.argmin(chi2dof_F_fine)
    pr(f"\n  Best (1-b) for LCDM: {one_minus_b_fine[idx_best_L]:.3f} "
       f"(chi^2/dof = {chi2dof_L_fine[idx_best_L]:.3f})")
    pr(f"  Best (1-b) for FW:   {one_minus_b_fine[idx_best_F]:.3f} "
       f"(chi^2/dof = {chi2dof_F_fine[idx_best_F]:.3f})")

    # =========================================================================
    # 8. Comparison to S69 results
    # =========================================================================
    pr("\n" + "-" * 78)
    pr("Comparison to S69 (joint cal + delta_M fit):")
    pr("-" * 78)
    pr(f"  S69 LCDM:  chi^2/dof = {chi2_dof_s69_LCDM:.3f} (2 free params)")
    pr(f"  S69 FW:    chi^2/dof = {chi2_dof_s69_FW:.3f} (2 free params)")
    pr(f"\n  S70 (1-b)=0.62 LCDM: chi^2/dof = "
       f"{results_three[0.62]['chi2_L']/results_three[0.62]['dof_L']:.3f} (1 free param)")
    pr(f"  S70 (1-b)=0.62 FW:   chi^2/dof = "
       f"{results_three[0.62]['chi2_F']/results_three[0.62]['dof_F']:.3f} (1 free param)")
    pr(f"\n  S70 (1-b)=0.73 LCDM: chi^2/dof = "
       f"{results_three[0.73]['chi2_L']/results_three[0.73]['dof_L']:.3f}")
    pr(f"  S70 (1-b)=0.73 FW:   chi^2/dof = "
       f"{results_three[0.73]['chi2_F']/results_three[0.73]['dof_F']:.3f}")
    pr(f"\n  S70 (1-b)=0.80 LCDM: chi^2/dof = "
       f"{results_three[0.80]['chi2_L']/results_three[0.80]['dof_L']:.3f}")
    pr(f"  S70 (1-b)=0.80 FW:   chi^2/dof = "
       f"{results_three[0.80]['chi2_F']/results_three[0.80]['dof_F']:.3f}")

    pr(f"\n  Note: S69 used 2 free parameters (cal + delta_M) with dof={int(s69['dof'])}.")
    pr(f"  S70 uses 1 free parameter (cal only, delta_M fixed by (1-b)) with dof=6.")
    pr(f"  Different dof makes chi^2/dof not directly comparable.")
    pr(f"  Use Delta chi^2 (LCDM - FW) at SAME (1-b) for model comparison.")

    # =========================================================================
    # 9. sigma_8 tension with bias calibration
    # =========================================================================
    pr("\n" + "-" * 78)
    pr("sigma_8 tension analysis with hydrostatic bias:")
    pr("-" * 78)
    pr(f"  The sigma_8 tension between CMB and clusters depends on (1-b):")
    pr(f"    sigma_8(CMB, Planck 2018) = 0.811 +/- 0.006")
    pr(f"    sigma_8(CMB, FW)          = 0.793")
    pr(f"    sigma_8(clusters)          = 0.77 +/- 0.02 [at (1-b)~0.8]")
    pr(f"")
    pr(f"  Lowering (1-b) raises M_true -> fewer predicted clusters ->")
    pr(f"  needs HIGHER sigma_8 to match data -> worsens CMB-cluster tension.")
    pr(f"  FW sigma_8=0.793 is better positioned: closer to the cluster-inferred")
    pr(f"  value regardless of (1-b).")
    pr(f"")
    sig8_clusters = 0.77  # (local)
    sig8_clusters_err = 0.02  # (local)
    tension_LCDM = (sig8_lcdm - sig8_clusters) / sig8_clusters_err
    tension_FW = (sig8_fw - sig8_clusters) / sig8_clusters_err
    pr(f"  CMB-cluster sigma_8 tension:")
    pr(f"    LCDM: ({sig8_lcdm}-{sig8_clusters})/{sig8_clusters_err} = "
       f"{tension_LCDM:.1f} sigma")
    pr(f"    FW:   ({sig8_fw}-{sig8_clusters})/{sig8_clusters_err} = "
       f"{tension_FW:.1f} sigma")
    pr(f"    FW reduces tension from {tension_LCDM:.1f}sigma to {tension_FW:.1f}sigma")

    # =========================================================================
    # 10. Gate verdict
    # =========================================================================
    pr(f"\n{'=' * 78}")

    # Build summary table
    summary_lines = []
    for ob in one_minus_b_values:
        r = results_three[ob]
        summary_lines.append(
            f"(1-b)={ob:.2f}: chi2/dof(FW)={r['chi2_F']/r['dof_F']:.3f}, "
            f"chi2/dof(LCDM)={r['chi2_L']/r['dof_L']:.3f}, "
            f"Delta_chi2={r['chi2_L']-r['chi2_F']:+.2f}")

    crossover_str = ""
    if len(sign_changes) > 0:
        sc = sign_changes[0]
        ob_lo = one_minus_b_fine[sc]
        ob_hi = one_minus_b_fine[sc + 1]
        dc_lo = delta_chi2_fine[sc]
        dc_hi = delta_chi2_fine[sc + 1]
        ob_cross = ob_lo + (ob_hi - ob_lo) * (-dc_lo) / (dc_hi - dc_lo)
        crossover_str = f"Crossover at (1-b)={ob_cross:.3f}."
    else:
        if delta_chi2_fine[0] > 0:
            crossover_str = "FW preferred across all (1-b)."
        else:
            crossover_str = "LCDM preferred across all (1-b)."

    gate_detail = (
        "; ".join(summary_lines) +
        f". {crossover_str} "
        f"Best FW: chi2/dof={chi2dof_F_fine[idx_best_F]:.3f} at "
        f"(1-b)={one_minus_b_fine[idx_best_F]:.3f}. "
        f"sigma_8 tension reduced 2.1->1.2 sigma."
    )

    gate_verdict = "INFO"
    pr(f"Gate HYDROSTATIC-CLUSTER-70: {gate_verdict}")
    pr(f"  Type: INFO (report chi^2/dof at three bias calibrations)")
    for sl in summary_lines:
        pr(f"  {sl}")
    pr(f"  {crossover_str}")
    pr(f"  Best FW chi^2/dof = {chi2dof_F_fine[idx_best_F]:.3f} "
       f"at (1-b) = {one_minus_b_fine[idx_best_F]:.3f}")
    pr(f"{'=' * 78}")

    # =========================================================================
    # 11. Save data
    # =========================================================================
    outpath = os.path.join(SCRIPT_DIR, "s70_hydrostatic_cluster.npz")

    # Pack three-calibration results
    chi2_dof_FW_three = np.array([
        results_three[ob]['chi2_F'] / results_three[ob]['dof_F']
        for ob in one_minus_b_values])
    chi2_dof_LCDM_three = np.array([
        results_three[ob]['chi2_L'] / results_three[ob]['dof_L']
        for ob in one_minus_b_values])
    delta_chi2_three = np.array([
        results_three[ob]['chi2_L'] - results_three[ob]['chi2_F']
        for ob in one_minus_b_values])
    cal_FW_three = np.array([results_three[ob]['cal_F']
                              for ob in one_minus_b_values])
    cal_LCDM_three = np.array([results_three[ob]['cal_L']
                                for ob in one_minus_b_values])

    # Calibrated predictions at each (1-b)
    Ncal_FW_062 = results_three[0.62]['Ncal_F']
    Ncal_FW_073 = results_three[0.73]['Ncal_F']
    Ncal_FW_080 = results_three[0.80]['Ncal_F']
    Ncal_LCDM_062 = results_three[0.62]['Ncal_L']
    Ncal_LCDM_073 = results_three[0.73]['Ncal_L']
    Ncal_LCDM_080 = results_three[0.80]['Ncal_L']

    np.savez(outpath,
        # Input data (carried from S69)
        z_bin_edges=z_bin_edges,
        z_bin_mid=z_bin_mid,
        N_obs=N_obs,
        N_obs_err=N_obs_err,
        log10_M200_min_base=log10_M200_min_base,
        # Three calibrations
        one_minus_b_values=one_minus_b_values,
        chi2_dof_FW_three=chi2_dof_FW_three,
        chi2_dof_LCDM_three=chi2_dof_LCDM_three,
        delta_chi2_three=delta_chi2_three,
        cal_FW_three=cal_FW_three,
        cal_LCDM_three=cal_LCDM_three,
        # Calibrated predictions per bias
        Ncal_FW_062=Ncal_FW_062,
        Ncal_FW_073=Ncal_FW_073,
        Ncal_FW_080=Ncal_FW_080,
        Ncal_LCDM_062=Ncal_LCDM_062,
        Ncal_LCDM_073=Ncal_LCDM_073,
        Ncal_LCDM_080=Ncal_LCDM_080,
        # Fine scan
        one_minus_b_fine=one_minus_b_fine,
        chi2dof_L_fine=chi2dof_L_fine,
        chi2dof_F_fine=chi2dof_F_fine,
        delta_chi2_fine=delta_chi2_fine,
        cal_L_fine=cal_L_fine,
        cal_F_fine=cal_F_fine,
        # Best-fit (1-b)
        best_ob_FW=np.float64(one_minus_b_fine[idx_best_F]),
        best_chi2dof_FW=np.float64(chi2dof_F_fine[idx_best_F]),
        best_ob_LCDM=np.float64(one_minus_b_fine[idx_best_L]),
        best_chi2dof_LCDM=np.float64(chi2dof_L_fine[idx_best_L]),
        # S69 reference
        chi2_dof_s69_LCDM=np.float64(chi2_dof_s69_LCDM),
        chi2_dof_s69_FW=np.float64(chi2_dof_s69_FW),
        # Parameters
        sig8_FW=np.float64(sig8_fw),
        sig8_LCDM=np.float64(sig8_lcdm),
        ns_FW=np.float64(ns_fw),
        ns_LCDM=np.float64(ns_lcdm),
        w0_fw=np.float64(w0_fw_val),
        # Gate
        gate_name=np.array("HYDROSTATIC-CLUSTER-70"),
        gate_verdict=np.array(gate_verdict),
        gate_detail=np.array(gate_detail),
    )
    pr(f"\nData saved to: {outpath}")

    # =========================================================================
    # 12. Plot
    # =========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle('HYDROSTATIC-CLUSTER-70: Cluster Mass Function with Hydrostatic Bias',
                 fontsize=13, fontweight='bold', y=0.98)

    # --- Panel (a): chi^2/dof vs (1-b) ---
    ax = axes[0, 0]
    ax.plot(one_minus_b_fine, chi2dof_L_fine, 'b-', lw=2,
            label=r'$\Lambda$CDM ($\sigma_8=0.811$)')
    ax.plot(one_minus_b_fine, chi2dof_F_fine, 'r-', lw=2,
            label=r'FW ($\sigma_8=0.793$)')
    for ob in one_minus_b_values:
        r = results_three[ob]
        ax.plot(ob, r['chi2_L']/r['dof_L'], 'bs', ms=8)
        ax.plot(ob, r['chi2_F']/r['dof_F'], 'rD', ms=8)
    ax.axhline(1.0, color='green', ls='--', lw=0.8, alpha=0.5, label='Good fit')
    ax.axhline(3.0, color='orange', ls='--', lw=0.8, alpha=0.5, label='Tension')
    ax.set_xlabel('Hydrostatic bias $(1-b)$', fontsize=11)
    ax.set_ylabel(r'$\chi^2/\mathrm{dof}$', fontsize=11)
    ax.set_title(r'(a) $\chi^2/\mathrm{dof}$ vs hydrostatic bias', fontsize=11)
    ax.legend(fontsize=9, loc='upper right')
    ax.set_xlim(0.54, 0.91)

    # --- Panel (b): Delta chi^2 vs (1-b) ---
    ax = axes[0, 1]
    ax.plot(one_minus_b_fine, delta_chi2_fine, 'k-', lw=2)
    ax.axhline(0, color='gray', ls='--', lw=0.8)
    ax.fill_between(one_minus_b_fine, 0, delta_chi2_fine,
                     where=(delta_chi2_fine > 0), alpha=0.15, color='red',
                     label='FW preferred')
    ax.fill_between(one_minus_b_fine, 0, delta_chi2_fine,
                     where=(delta_chi2_fine < 0), alpha=0.15, color='blue',
                     label=r'$\Lambda$CDM preferred')
    for ob in one_minus_b_values:
        dc = results_three[ob]['chi2_L'] - results_three[ob]['chi2_F']
        ax.plot(ob, dc, 'ko', ms=8, zorder=5)
        ax.annotate(f'({ob:.2f})', (ob, dc), textcoords="offset points",
                    xytext=(5, 8), fontsize=8)
    ax.set_xlabel('Hydrostatic bias $(1-b)$', fontsize=11)
    ax.set_ylabel(r'$\Delta\chi^2$ ($\Lambda$CDM $-$ FW)', fontsize=11)
    ax.set_title(r'(b) $\Delta\chi^2$: positive = FW preferred', fontsize=11)
    ax.legend(fontsize=9)
    ax.set_xlim(0.54, 0.91)

    # --- Panel (c): Calibrated N(z) at (1-b)=0.62 ---
    ax = axes[1, 0]
    r62 = results_three[0.62]
    width = 0.015  # (local)
    ax.bar(z_bin_mid - width, N_obs, width=2*width, alpha=0.3, color='gray',
           label='Observed', edgecolor='black')
    ax.errorbar(z_bin_mid, N_obs, yerr=N_obs_err, fmt='ko', ms=5, capsize=3,
                zorder=5)
    ax.plot(z_bin_mid, r62['Ncal_L'], 's-', color='blue', ms=6, lw=1.5,
            label=r'$\Lambda$CDM, $(1\!-\!b)=0.62$')
    ax.plot(z_bin_mid, r62['Ncal_F'], 'D-', color='red', ms=6, lw=1.5,
            label=r'FW, $(1\!-\!b)=0.62$')
    r80 = results_three[0.80]
    ax.plot(z_bin_mid, r80['Ncal_L'], 's--', color='cornflowerblue', ms=5,
            lw=1, alpha=0.7, label=r'$\Lambda$CDM, $(1\!-\!b)=0.80$')  # (local)
    ax.plot(z_bin_mid, r80['Ncal_F'], 'D--', color='salmon', ms=5, lw=1,
            alpha=0.7, label=r'FW, $(1\!-\!b)=0.80$')  # (local)
    ax.set_xlabel('Redshift $z$', fontsize=11)
    ax.set_ylabel('Cluster count $N(z)$', fontsize=11)
    ax.set_title('(c) Cluster counts: $(1-b)=0.62$ vs $0.80$', fontsize=11)
    ax.legend(fontsize=7.5, loc='upper right')
    ax.set_xlim(-0.02, 1.05)

    # --- Panel (d): Residuals at (1-b)=0.73 ---
    ax = axes[1, 1]
    r73 = results_three[0.73]
    resid_L = (N_obs - r73['Ncal_L']) / N_obs_err
    resid_F = (N_obs - r73['Ncal_F']) / N_obs_err
    ax.axhline(0, color='gray', ls='--', lw=0.8)
    ax.axhspan(-1, 1, alpha=0.1, color='green')
    ax.axhspan(-2, 2, alpha=0.05, color='yellow')
    ax.plot(z_bin_mid, resid_L, 's-', color='blue', ms=6, lw=1.5,
            label=r'$\Lambda$CDM, $(1\!-\!b)=0.73$')
    ax.plot(z_bin_mid, resid_F, 'D-', color='red', ms=6, lw=1.5,
            label=r'FW, $(1\!-\!b)=0.73$')
    ax.set_xlabel('Redshift $z$', fontsize=11)
    ax.set_ylabel(r'Residual $(N_{\rm obs} - N_{\rm pred})/\sigma$', fontsize=11)
    ax.set_title('(d) Residuals at $(1-b)=0.73$ [HSC WL]', fontsize=11)
    ax.legend(fontsize=9)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(-3.5, 3.5)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    figpath = os.path.join(SCRIPT_DIR, "s70_hydrostatic_cluster.png")
    fig.savefig(figpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    pr(f"Plot saved to: {figpath}")

    pr(f"\n{'=' * 78}")
    pr("HYDROSTATIC-CLUSTER-70: COMPLETE")
    pr(f"{'=' * 78}")

    log.close()

except Exception:
    tb = traceback.format_exc()
    print(tb)
    try:
        log.write(tb + "\n")
        log.close()
    except Exception:
        pass
    sys.exit(1)
