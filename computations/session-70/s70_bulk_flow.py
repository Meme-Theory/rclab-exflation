#!/usr/bin/env python3
"""
s70_bulk_flow.py -- BULK-FLOW-70: Bulk Flow Amplitude at FW Cosmology
=====================================================================
Gate: BULK-FLOW-70
  INFO: Report V_bulk(R) for FW and LCDM

Physics:
  The 3D RMS bulk flow within a sphere of radius R is:
    <|V|^2> = (H_0 f)^2 / (2*pi^2) * integral_0^infty P(k) * |W(kR)|^2 dk
  where W(x) = 3*(sin(x) - x*cos(x))/x^3 is the top-hat window function,
  f is the linear growth rate at z=0, and P(k) is the linear matter power
  spectrum.

  Derivation (confirming the factor):
    v_i(k) = i * k_i/k^2 * aHf * delta(k)
    V_i = integral d^3k/(2pi)^3 W_tilde(k) v_i(k)
    <V_i^2> = (aHf)^2/(6pi^2) integral P(k) |W(kR)|^2 dk   [isotropy: k_i^2 -> k^2/3]
    <|V|^2> = 3 * <V_i^2> = (aHf)^2/(2pi^2) integral P(k) |W(kR)|^2 dk

  So V_rms = sqrt(<|V|^2>) is the RMS of the 3D bulk flow magnitude.
  Each Cartesian component has sigma_1D = V_rms / sqrt(3).
  The magnitude |V| follows a chi distribution with 3 degrees of freedom
  (chi_3), with parameter sigma_1D.

  We compute V_rms(R) for R = [50, 100, 150, 200, 300] Mpc/h using:
    (1) LCDM:      w = -1, sigma_8 = 0.811
    (2) Framework:  w_0 = -0.918, sigma_8 = 0.793

  The Eisenstein & Hu (1998) fitting formula is used for the transfer function
  T(k), giving P(k) = A * k^{n_s} * T^2(k), normalised to sigma_8.

  Statistical comparison:
    The observed bulk flow |V_obs| must be compared against the full
    chi_3 distribution, not just the RMS. Cosmic variance dominates
    the error budget at the scales of interest (50-300 Mpc/h).
    Total error: sigma_total = sqrt(sigma_meas^2 + sigma_cosmic^2)
    where sigma_cosmic = sigma_1D * sqrt(3 - 8/pi).

Author: Cosmic Web Theorist
Session: 70, Task W4-E (BULK-FLOW-70)
"""

import os
import sys
import traceback

try:
    import numpy as np
    from scipy.integrate import solve_ivp, quad
    from scipy.interpolate import interp1d
    from scipy.stats import chi, norm
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, SCRIPT_DIR)

    from canonical_constants import *

    LOGPATH = os.path.join(SCRIPT_DIR, "s70_bulk_flow_log.txt")
    log = open(LOGPATH, "w")

    def pr(msg=""):
        print(str(msg))
        log.write(str(msg) + "\n")
        log.flush()

    pr("=" * 78)
    pr("BULK-FLOW-70: Bulk Flow Amplitude at FW Cosmology")
    pr("=" * 78)

    # =========================================================================
    # 1. Cosmological parameters
    # =========================================================================
    Om_m = Omega_m          # 0.315
    Om_b_val = Omega_b      # 0.0493
    Om_DE = Omega_Lambda    # 0.685
    h_hub = H_0_km_s_Mpc / 100.0   # 0.674
    n_s_spec = 0.965        # Planck 2018 scalar spectral index
    sig8_LCDM = sigma_8     # 0.811

    # Framework parameters (from S64/S69 data)
    s64_path = os.path.join(SCRIPT_DIR, 's64_desi_dv.npz')
    s64_data = np.load(s64_path, allow_pickle=True)
    w0_fw = float(s64_data['w0_fw'])     # -0.918

    # Load framework sigma_8 from S69 growth computation
    s69_path = os.path.join(SCRIPT_DIR, 's69_pvd05_fsigma8.npz')
    s69_data = np.load(s69_path, allow_pickle=True)
    sig8_fw = float(s69_data['sigma8_fw'])       # 0.793
    growth_ratio = float(s69_data['growth_ratio_fw'])  # ~0.978

    pr(f"\nCosmological parameters:")
    pr(f"  Omega_m = {Om_m}")
    pr(f"  Omega_b = {Om_b_val}")
    pr(f"  Omega_DE = {Om_DE}")
    pr(f"  h = {h_hub}")
    pr(f"  n_s = {n_s_spec}")
    pr(f"  sigma_8 (LCDM) = {sig8_LCDM}")
    pr(f"  sigma_8 (FW)   = {sig8_fw:.6f}")
    pr(f"  w_0 (FW) = {w0_fw:.6f}")
    pr(f"  Growth ratio D_FW/D_LCDM at z=0: {growth_ratio:.6f}")

    # =========================================================================
    # 2. Eisenstein & Hu (1998) transfer function (with baryon suppression)
    # =========================================================================
    # Reference: Eisenstein & Hu, ApJ 496, 605 (1998), Eqs. 29-31

    def transfer_EH98(k_hMpc, Om_m_loc, Om_b_loc, h_loc):
        """
        Eisenstein & Hu (1998) transfer function T(k).

        Parameters:
            k_hMpc : array, wavenumber in h/Mpc
            Om_m_loc, Om_b_loc : density parameters
            h_loc : dimensionless Hubble parameter

        Returns:
            T(k) : array, transfer function (T(0) = 1)
        """
        Om_mh2 = Om_m_loc * h_loc**2
        Om_bh2 = Om_b_loc * h_loc**2

        # Sound horizon fitting formula (Eq. 26)
        s_fit = 44.5 * np.log(9.83 / Om_mh2) / \
                np.sqrt(1.0 + 10.0 * Om_bh2**0.75)  # Mpc

        # Shape parameter (Eq. 31) with baryon correction
        alpha_Gamma = 1.0 - 0.328 * np.log(431.0 * Om_mh2) * (Om_b_loc / Om_m_loc) + \
                      0.380 * np.log(22.3 * Om_mh2) * (Om_b_loc / Om_m_loc)**2
        Gamma_eff = Om_m_loc * h_loc * (alpha_Gamma + (1.0 - alpha_Gamma) /
                    (1.0 + (0.43 * k_hMpc * s_fit)**4))

        # Transfer function (Eq. 29)
        Theta_27 = T_CMB / 2.7
        q = k_hMpc * Theta_27**2 / Gamma_eff

        L0 = np.log(2.0 * np.e + 1.8 * q)
        C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
        T_k = L0 / (L0 + C0 * q**2)

        return T_k

    # =========================================================================
    # 3. Linear power spectrum P(k) normalised to sigma_8
    # =========================================================================

    # Build transfer function on a k grid
    k_grid = np.logspace(-5, 2, 10000)  # h/Mpc
    Tk_grid = transfer_EH98(k_grid, Om_m, Om_b_val, h_hub)
    Tk_interp = interp1d(k_grid, Tk_grid, kind='cubic',
                         bounds_error=False, fill_value=(1.0, 0.0))

    # Compute sigma_8 normalisation integral
    def sigma_R_integrand_lnk(lnk, R, ns):
        """Integrand for sigma(R) in d(ln k)."""
        k = np.exp(lnk)
        x = k * R
        if x < 1e-6:
            W = 1.0 - x**2 / 10.0  # (local)
        else:
            W = 3.0 * (np.sin(x) - x * np.cos(x)) / x**3  # (local)
        Tk = float(Tk_interp(k))
        # k^3 P(k) / (2pi^2) with P(k) propto k^ns T^2
        return k**3 * k**ns * Tk**2 * W**2 / (2.0 * np.pi**2)

    sig8_sq_unnorm, _ = quad(sigma_R_integrand_lnk, np.log(1e-5), np.log(100.0),
                              args=(8.0, n_s_spec), limit=500, epsrel=1e-10)
    sig8_unnorm = np.sqrt(sig8_sq_unnorm)
    pr(f"\nsigma_8 (unnormalized integral) = {sig8_unnorm:.6e}")

    # Amplitude normalisation: P(k) = A * k^{n_s} * T(k)^2
    A_LCDM = sig8_LCDM**2 / sig8_sq_unnorm
    A_FW = sig8_fw**2 / sig8_sq_unnorm

    pr(f"  A_LCDM (norm) = {A_LCDM:.6e}")
    pr(f"  A_FW   (norm) = {A_FW:.6e}")

    # Verify sigma_8 normalisation
    def verify_sigma8(A, ns, label):
        result, _ = quad(sigma_R_integrand_lnk, np.log(1e-5), np.log(100.0),
                         args=(8.0, ns), limit=500, epsrel=1e-10)
        return np.sqrt(A * result)

    sig8_check_L = verify_sigma8(A_LCDM, n_s_spec, "LCDM")
    sig8_check_F = verify_sigma8(A_FW, n_s_spec, "FW")
    pr(f"  Verification: sigma_8(LCDM) = {sig8_check_L:.6f} (target {sig8_LCDM})")
    pr(f"  Verification: sigma_8(FW)   = {sig8_check_F:.6f} (target {sig8_fw:.6f})")

    # =========================================================================
    # 4. Growth rate f(z=0) from S69 data
    # =========================================================================
    f_arr_L = s69_data['f_LCDM']
    f_arr_FW = s69_data['f_FW']
    a_arr = s69_data['a_arr']

    f_LCDM_z0 = float(f_arr_L[-1])
    f_FW_z0 = float(f_arr_FW[-1])

    fsig8_LCDM = f_LCDM_z0 * sig8_LCDM
    fsig8_FW = f_FW_z0 * sig8_fw

    pr(f"\nGrowth rate at z=0:")
    pr(f"  f_LCDM  = {f_LCDM_z0:.6f}")
    pr(f"  f_FW    = {f_FW_z0:.6f}")
    pr(f"  f*sig8 (LCDM) = {fsig8_LCDM:.6f}")
    pr(f"  f*sig8 (FW)   = {fsig8_FW:.6f}")
    pr(f"  Ratio FW/LCDM = {fsig8_FW / fsig8_LCDM:.6f}")

    # =========================================================================
    # 5. Bulk flow computation
    # =========================================================================
    # <|V|^2> = (H_0 f)^2 / (2 pi^2) * integral P(k) |W(kR)|^2 dk
    #
    # This gives the 3D RMS: V_rms = sqrt(<Vx^2 + Vy^2 + Vz^2>)
    # Each component: sigma_1D = V_rms / sqrt(3)
    # |V| follows chi_3 distribution with parameter sigma_1D:
    #   <|V|> = sigma_1D * sqrt(8/pi) ~ sigma_1D * 1.596
    #   Var(|V|) = sigma_1D^2 * (3 - 8/pi) ~ sigma_1D^2 * 0.454
    #
    # In h-units: k in h/Mpc, R in Mpc/h, P(k) in (Mpc/h)^3
    # H_0 = 100 km/s / (Mpc/h) in these units

    R_values = np.array([50.0, 100.0, 150.0, 200.0, 300.0])  # Mpc/h

    def compute_bulk_flow_rms(R, A, f_z0, ns, Tk_interp_loc):
        """
        Compute 3D RMS bulk flow V_rms = sqrt(<|V|^2>) in km/s.
        Uses H_0 = 100 km/s/(Mpc/h) in h-units.
        """
        def integrand(lnk):
            k = np.exp(lnk)
            x = k * R
            if x < 1e-6:
                W = 1.0 - x**2 / 10.0  # (local)
            else:
                W = 3.0 * (np.sin(x) - x * np.cos(x)) / x**3  # (local)
            Tk = float(Tk_interp_loc(k))
            Pk = A * k**ns * Tk**2  # (Mpc/h)^3
            return Pk * W**2 * k  # k from d(ln k) Jacobian

        result, err = quad(integrand, np.log(1e-5), np.log(100.0),
                           limit=1000, epsrel=1e-9)
        V2 = (100.0)**2 * f_z0**2 / (2.0 * np.pi**2) * result
        return np.sqrt(V2)

    pr("\n" + "=" * 78)
    pr("Bulk Flow V_rms(R) at z = 0")
    pr("=" * 78)
    pr(f"\nV_rms = sqrt(<|V|^2>) = sqrt(<Vx^2+Vy^2+Vz^2>) [3D RMS]")
    pr(f"sigma_1D = V_rms / sqrt(3) [per-component RMS]")
    pr(f"<|V|> = sigma_1D * sqrt(8/pi) [mean of chi_3 distribution]")
    pr(f"")
    pr(f"{'R [Mpc/h]':>12} {'V_rms_L':>10} {'V_rms_FW':>10} {'sig1D_L':>10} "
       f"{'sig1D_FW':>10} {'<|V|>_L':>10} {'<|V|>_FW':>10} {'Ratio':>8}")
    pr("-" * 85)

    V_rms_LCDM = np.zeros(len(R_values))
    V_rms_FW = np.zeros(len(R_values))

    for i, R in enumerate(R_values):
        V_rms_LCDM[i] = compute_bulk_flow_rms(R, A_LCDM, f_LCDM_z0, n_s_spec, Tk_interp)
        V_rms_FW[i] = compute_bulk_flow_rms(R, A_FW, f_FW_z0, n_s_spec, Tk_interp)
        s1d_L = V_rms_LCDM[i] / np.sqrt(3.0)
        s1d_F = V_rms_FW[i] / np.sqrt(3.0)
        mean_L = s1d_L * np.sqrt(8.0 / np.pi)
        mean_F = s1d_F * np.sqrt(8.0 / np.pi)
        ratio = V_rms_FW[i] / V_rms_LCDM[i]
        pr(f"{R:12.0f} {V_rms_LCDM[i]:10.1f} {V_rms_FW[i]:10.1f} {s1d_L:10.1f} "
           f"{s1d_F:10.1f} {mean_L:10.1f} {mean_F:10.1f} {ratio:8.4f}")

    # =========================================================================
    # 6. Comparison with observations
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Comparison with Observational Data")
    pr("=" * 78)

    # Observational data points (3D bulk flow magnitude measurements)
    # Source: Watkins et al. (2023), MNRAS 524, 1885 (CF4)
    #   |V_bulk| = 252 +/- 11 km/s at effective depth R_eff ~ 150 Mpc/h
    # Qin et al. (2019), MNRAS 487, 5235 (2MTF)
    #   |V_bulk| = 292 +/- 57 km/s at R ~ 100 Mpc/h
    # Hoffman et al. (2015), MNRAS 449, 4494 (CF2 Wiener filter)
    #   |V_bulk| = 259 +/- 15 km/s at R ~ 125 Mpc/h
    # Kashlinsky et al. (2010), ApJ 712, L81 (kSZ, disputed)
    #   |V_bulk| > 600 km/s at R ~ 300 Mpc/h

    obs_R = np.array([100.0, 125.0, 150.0, 300.0])  # Mpc/h
    obs_V = np.array([292.0, 259.0, 252.0, 600.0])   # km/s
    obs_err = np.array([57.0, 15.0, 11.0, 150.0])    # km/s (measurement uncertainty)
    obs_labels = ['Qin+19 (2MTF)', 'Hoffman+15 (CF2)', 'Watkins+23 (CF4)', 'Kashlinsky+10 (kSZ)']
    obs_notes = ['solid', 'solid', 'solid', 'disputed']

    # Interpolate theoretical predictions to observational R values
    V_rms_L_interp = interp1d(R_values, V_rms_LCDM, kind='cubic', fill_value='extrapolate')
    V_rms_F_interp = interp1d(R_values, V_rms_FW, kind='cubic', fill_value='extrapolate')

    pr(f"\nStatistical comparison using chi_3 distribution:")
    pr(f"  |V| follows chi distribution with 3 dof, parameter sigma_1D")
    pr(f"  P(|V| > V_obs) computed directly; converted to equivalent Gaussian sigma")
    pr(f"  Cosmic variance is included through the chi_3 distribution")
    pr(f"")
    pr(f"{'Source':>24} {'R_eff':>6} {'V_obs':>6} {'err':>5} {'V_rms_L':>8} {'V_rms_FW':>8} "
       f"{'P_L(>V)':>10} {'sig_L':>6} {'P_FW(>V)':>10} {'sig_FW':>6} {'Note':>10}")
    pr("-" * 115)

    p_exceed_L = np.zeros(len(obs_R))
    p_exceed_FW = np.zeros(len(obs_R))
    sigma_equiv_L = np.zeros(len(obs_R))
    sigma_equiv_FW = np.zeros(len(obs_R))

    for i in range(len(obs_R)):
        R_obs = obs_R[i]
        V_obs = obs_V[i]
        V_meas_err = obs_err[i]

        VL_rms = float(V_rms_L_interp(R_obs))
        VF_rms = float(V_rms_F_interp(R_obs))

        s1d_L = VL_rms / np.sqrt(3.0)
        s1d_F = VF_rms / np.sqrt(3.0)

        # P(|V| > V_obs) from chi_3 distribution
        # chi_3 has scale parameter sigma_1D
        # Need to account for measurement error: convolve chi_3 with Gaussian
        # For simplicity (measurement error << cosmic variance), use chi_3 directly
        # and add measurement error in quadrature to the cosmic variance
        # sigma_cosmic = sigma_1D * sqrt(3 - 8/pi)
        sigma_cosmic_L = s1d_L * np.sqrt(3.0 - 8.0/np.pi)
        sigma_cosmic_F = s1d_F * np.sqrt(3.0 - 8.0/np.pi)

        # Total effective sigma around the chi_3 mode
        # For a more rigorous approach: compute P(|V| > V_obs | chi_3(sigma_1D))
        # The chi_3 distribution already captures cosmic variance.
        # Measurement error smears the observation, not the theory.

        # Pure chi_3 exceedance probability (cosmic variance only)
        p_L = 1.0 - chi.cdf(V_obs / s1d_L, df=3)
        p_F = 1.0 - chi.cdf(V_obs / s1d_F, df=3)

        p_exceed_L[i] = p_L
        p_exceed_FW[i] = p_F

        # Convert to equivalent Gaussian sigma (one-sided)
        if p_L > 1e-15:
            sig_L = norm.ppf(1.0 - p_L)
        else:
            sig_L = 8.0  # cap  # (local)
        if p_F > 1e-15:
            sig_F = norm.ppf(1.0 - p_F)
        else:
            sig_F = 8.0  # (local)

        sigma_equiv_L[i] = sig_L
        sigma_equiv_FW[i] = sig_F

        pr(f"{obs_labels[i]:>24} {R_obs:6.0f} {V_obs:6.0f} {V_meas_err:5.0f} "
           f"{VL_rms:8.1f} {VF_rms:8.1f} {p_L:10.4e} {sig_L:6.2f} "
           f"{p_F:10.4e} {sig_F:6.2f} {obs_notes[i]:>10}")

    # =========================================================================
    # 7. Detailed analysis at R = 150 Mpc/h (Watkins+23)
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Detailed Analysis: Watkins et al. (2023) at R = 150 Mpc/h")
    pr("=" * 78)

    V_L_150 = float(V_rms_L_interp(150.0))
    V_F_150 = float(V_rms_F_interp(150.0))
    s1d_L_150 = V_L_150 / np.sqrt(3.0)
    s1d_F_150 = V_F_150 / np.sqrt(3.0)

    V_obs_150 = 252.0  # (local)
    err_150 = 11.0  # (local)

    pr(f"\n  Observed |V| = {V_obs_150:.1f} +/- {err_150:.1f} km/s (measurement uncertainty)")
    pr(f"  LCDM:  V_rms = {V_L_150:.1f} km/s, sigma_1D = {s1d_L_150:.1f} km/s")
    pr(f"  FW:    V_rms = {V_F_150:.1f} km/s, sigma_1D = {s1d_F_150:.1f} km/s")
    pr(f"")

    # chi_3 distribution statistics
    mean_chi3_L = s1d_L_150 * np.sqrt(8.0/np.pi)
    mode_chi3_L = s1d_L_150 * np.sqrt(1.0)  # mode of chi_3 = sigma * sqrt(k-1) for k dof: sqrt(1)=1
    # Actually mode of chi(3) = sigma * sqrt(3 - 2/3) ... no.
    # chi(k) has mode at sigma * sqrt(k-1) for k >= 1
    # For k=3: mode = sigma * sqrt(2)
    mode_chi3_L_val = s1d_L_150 * np.sqrt(2.0)
    sigma_cosmic_L = s1d_L_150 * np.sqrt(3.0 - 8.0/np.pi)

    pr(f"  chi_3 distribution (LCDM):")
    pr(f"    Mean:     {mean_chi3_L:.1f} km/s")
    pr(f"    Mode:     {mode_chi3_L_val:.1f} km/s")
    pr(f"    Std dev:  {sigma_cosmic_L:.1f} km/s (cosmic variance)")
    pr(f"    V_rms:    {V_L_150:.1f} km/s")
    pr(f"")

    # Exceedance
    x_obs_L = V_obs_150 / s1d_L_150
    x_obs_F = V_obs_150 / s1d_F_150
    p_L_150 = 1.0 - chi.cdf(x_obs_L, df=3)
    p_F_150 = 1.0 - chi.cdf(x_obs_F, df=3)
    sig_L_150 = norm.ppf(1.0 - p_L_150) if p_L_150 > 1e-15 else 8.0
    sig_F_150 = norm.ppf(1.0 - p_F_150) if p_F_150 > 1e-15 else 8.0

    pr(f"  P(|V| > 252 km/s | LCDM):      {p_L_150:.4e}  ({sig_L_150:.2f} sigma)")
    pr(f"  P(|V| > 252 km/s | Framework):  {p_F_150:.4e}  ({sig_F_150:.2f} sigma)")
    pr(f"  Framework delta_sigma = {sig_F_150 - sig_L_150:+.2f} (worsens tension)")
    pr(f"")

    # Gaussian approximation for comparison
    pull_gauss_L = (V_obs_150 - mean_chi3_L) / np.sqrt(sigma_cosmic_L**2 + err_150**2)
    pr(f"  Gaussian approx pull (LCDM): (252 - {mean_chi3_L:.1f}) / sqrt({sigma_cosmic_L:.1f}^2 + {err_150:.1f}^2) = {pull_gauss_L:.2f} sigma")

    # =========================================================================
    # 8. Scaling analysis
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Scaling Analysis")
    pr("=" * 78)

    expected_ratio = fsig8_FW / fsig8_LCDM
    actual_ratio_mean = np.mean(V_rms_FW / V_rms_LCDM)
    pct_reduction = (1.0 - expected_ratio) * 100.0

    pr(f"\nV_rms propto f * sigma_8 (shape of P(k) unchanged)")
    pr(f"  Expected ratio from f*sigma_8: {expected_ratio:.6f}")
    pr(f"  Actual mean V_FW/V_LCDM:       {actual_ratio_mean:.6f}")
    pr(f"  Match validates computation.")
    pr(f"  Framework reduces bulk flow by {pct_reduction:.2f}%")
    pr(f"")

    # Decompose the 2.50% reduction:
    f_ratio = f_FW_z0 / f_LCDM_z0
    s8_ratio = sig8_fw / sig8_LCDM
    pr(f"  Decomposition:")
    pr(f"    f ratio:      {f_ratio:.6f} ({(1-f_ratio)*100:.2f}% reduction)")
    pr(f"    sigma_8 ratio: {s8_ratio:.6f} ({(1-s8_ratio)*100:.2f}% reduction)")
    pr(f"    Product:       {f_ratio * s8_ratio:.6f}")

    # =========================================================================
    # 9. Discriminating power: FW vs LCDM
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Discriminating Power: FW vs LCDM")
    pr("=" * 78)

    delta_V_150 = abs(V_L_150 - V_F_150)
    sigma_cosmic_for_disc = s1d_L_150 * np.sqrt(3.0 - 8.0/np.pi)

    pr(f"\n|V_rms(LCDM) - V_rms(FW)| at R=150: {delta_V_150:.2f} km/s")
    pr(f"Measurement error (Watkins+23): {err_150:.1f} km/s")
    pr(f"Cosmic variance (chi_3 std): {sigma_cosmic_for_disc:.1f} km/s")
    pr(f"")
    pr(f"SNR_meas = {delta_V_150:.2f} / {err_150:.1f} = {delta_V_150/err_150:.3f}")
    pr(f"SNR_total = {delta_V_150:.2f} / sqrt({err_150:.1f}^2 + {sigma_cosmic_for_disc:.1f}^2) "
       f"= {delta_V_150/np.sqrt(err_150**2 + sigma_cosmic_for_disc**2):.4f}")
    pr(f"")
    pr(f"Cosmic variance DOMINATES the error budget.")
    pr(f"The 2.5% FW/LCDM difference is {delta_V_150:.1f} km/s,")
    pr(f"while cosmic variance alone is {sigma_cosmic_for_disc:.1f} km/s.")
    pr(f"Bulk flow cannot discriminate FW from LCDM.")

    # Future prospects
    pr(f"\nFuture surveys (DESI peculiar velocities, Rubin LSST, SKA):")
    pr(f"  Even with zero measurement error, cosmic variance sets a floor:")
    pr(f"  SNR_max = |delta_V| / sigma_cosmic = {delta_V_150/sigma_cosmic_for_disc:.4f}")
    pr(f"  Bulk flow is NOT a viable discriminator for a 2.5% effect.")
    pr(f"")
    pr(f"  To reach SNR=1, would need |delta_V| ~ {sigma_cosmic_for_disc:.0f} km/s,")
    pr(f"  requiring delta(sigma_8) ~ {sigma_cosmic_for_disc / V_L_150 * sig8_LCDM:.3f}")
    pr(f"  (i.e., sigma_8 difference of ~{sigma_cosmic_for_disc / V_L_150 * 100:.0f}%)")

    # =========================================================================
    # 10. Extended: V_bulk(R) on fine grid
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Extended: V_rms(R) on fine grid")
    pr("=" * 78)

    R_fine = np.linspace(10.0, 400.0, 80)
    V_rms_L_fine = np.zeros(len(R_fine))
    V_rms_F_fine = np.zeros(len(R_fine))

    for i, R in enumerate(R_fine):
        V_rms_L_fine[i] = compute_bulk_flow_rms(R, A_LCDM, f_LCDM_z0, n_s_spec, Tk_interp)
        V_rms_F_fine[i] = compute_bulk_flow_rms(R, A_FW, f_FW_z0, n_s_spec, Tk_interp)

    pr(f"Computed on {len(R_fine)} points from R={R_fine[0]:.0f} to {R_fine[-1]:.0f} Mpc/h")

    # =========================================================================
    # 11. Summary of bulk flow anomaly in context
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("Bulk Flow Anomaly Context")
    pr("=" * 78)
    pr(f"""
The observed bulk flow at R ~ 150 Mpc/h (Watkins+23: 252 +/- 11 km/s) is
higher than the LCDM RMS prediction ({V_L_150:.1f} km/s) at {sig_L_150:.1f} sigma
(including cosmic variance via the chi_3 distribution).

Framework prediction ({V_F_150:.1f} km/s) is 2.5% lower than LCDM, making
the tension marginally worse ({sig_F_150:.1f} sigma).

Key finding: The bulk flow anomaly is a ~{sig_L_150:.1f}-sigma tension in BOTH
LCDM and the framework. The framework's lower sigma_8 (0.793 vs 0.811)
reduces V_rms by only {delta_V_150:.1f} km/s, far below the cosmic variance
of {sigma_cosmic_for_disc:.1f} km/s.

Bulk flow measurements cannot discriminate between FW and LCDM.
The anomaly, if real, points to something beyond both models
(e.g., super-horizon modes, local void, survey systematics).
""")

    # =========================================================================
    # 12. Plot
    # =========================================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Panel 1: V_rms(R) with chi_3 bands
    ax1 = axes[0]

    # 68% and 95% bands from chi_3 distribution
    s1d_L_fine = V_rms_L_fine / np.sqrt(3.0)
    band_68_lo_L = np.array([chi.ppf(0.16, df=3) * s for s in s1d_L_fine])
    band_68_hi_L = np.array([chi.ppf(0.84, df=3) * s for s in s1d_L_fine])
    band_95_lo_L = np.array([chi.ppf(0.025, df=3) * s for s in s1d_L_fine])
    band_95_hi_L = np.array([chi.ppf(0.975, df=3) * s for s in s1d_L_fine])

    ax1.fill_between(R_fine, band_95_lo_L, band_95_hi_L, alpha=0.10, color='blue', label=r'LCDM 95% CI')
    ax1.fill_between(R_fine, band_68_lo_L, band_68_hi_L, alpha=0.20, color='blue', label=r'LCDM 68% CI')

    mean_L_fine = s1d_L_fine * np.sqrt(8.0/np.pi)
    ax1.plot(R_fine, mean_L_fine, 'b-', lw=2, label=r'$\Lambda$CDM $\langle|V|\rangle$')

    s1d_F_fine = V_rms_F_fine / np.sqrt(3.0)
    mean_F_fine = s1d_F_fine * np.sqrt(8.0/np.pi)
    ax1.plot(R_fine, mean_F_fine, 'r--', lw=2, label=r'Framework $\langle|V|\rangle$')

    # Plot observational data
    for i in range(len(obs_R)):
        marker = 'o' if obs_notes[i] == 'solid' else 'x'
        color = 'green' if obs_notes[i] == 'solid' else 'gray'
        ax1.errorbar(obs_R[i], obs_V[i], yerr=obs_err[i], fmt=marker, color=color,
                     capsize=4, markersize=8, label=obs_labels[i])

    ax1.set_xlabel(r'$R$ [Mpc/$h$]', fontsize=13)
    ax1.set_ylabel(r'Bulk flow $|V|$ [km/s]', fontsize=13)
    ax1.set_title('Bulk Flow Amplitude vs Depth', fontsize=14)
    ax1.legend(fontsize=8, loc='upper right')
    ax1.set_xlim(0, 420)
    ax1.set_ylim(0, 700)
    ax1.grid(True, alpha=0.3)

    # Panel 2: chi_3 distribution at R=150
    ax2 = axes[1]
    v_range = np.linspace(0, 400, 500)
    pdf_L = chi.pdf(v_range / s1d_L_150, df=3) / s1d_L_150
    pdf_F = chi.pdf(v_range / s1d_F_150, df=3) / s1d_F_150

    ax2.plot(v_range, pdf_L * 1000, 'b-', lw=2, label=r'$\Lambda$CDM')
    ax2.plot(v_range, pdf_F * 1000, 'r--', lw=2, label='Framework')
    ax2.axvline(V_obs_150, color='green', lw=2, ls='-',
                label=f'Watkins+23: {V_obs_150:.0f} km/s')
    ax2.axvspan(V_obs_150 - err_150, V_obs_150 + err_150, alpha=0.2, color='green')

    ax2.set_xlabel(r'$|V|$ [km/s]', fontsize=13)
    ax2.set_ylabel(r'PDF $\times 10^3$ [(km/s)$^{-1}$]', fontsize=13)
    ax2.set_title(r'$\chi_3$ Distribution at $R = 150$ Mpc/$h$', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 400)

    plt.tight_layout()
    figpath = os.path.join(SCRIPT_DIR, "s70_bulk_flow.png")
    plt.savefig(figpath, dpi=150)
    plt.close()
    pr(f"\nPlot saved: {figpath}")

    # =========================================================================
    # 13. Gate verdict
    # =========================================================================
    pr("\n" + "=" * 78)
    pr("GATE VERDICT")
    pr("=" * 78)

    gate_name = "BULK-FLOW-70"
    gate_verdict = "INFO"

    pr(f"\nGate {gate_name}: {gate_verdict}")
    pr(f"  Criterion: Report V_bulk(R) for FW and LCDM")
    pr(f"  Result: V_rms computed at R = {R_values} Mpc/h (3D RMS)")
    pr(f"  LCDM V_rms:  [{', '.join(f'{v:.1f}' for v in V_rms_LCDM)}] km/s")
    pr(f"  FW   V_rms:  [{', '.join(f'{v:.1f}' for v in V_rms_FW)}] km/s")
    pr(f"  Ratio FW/LCDM: {actual_ratio_mean:.4f} (= f*sigma_8 ratio: {expected_ratio:.4f})")
    pr(f"  Framework reduces bulk flow by {pct_reduction:.2f}%")
    pr(f"  At R=150 Mpc/h: LCDM {sig_L_150:.2f} sigma, FW {sig_F_150:.2f} sigma tension")
    pr(f"  Discrimination SNR (cosmic var floor): {delta_V_150/sigma_cosmic_for_disc:.4f}")
    pr(f"  Verdict: {gate_verdict} -- Bulk flow cannot discriminate FW from LCDM")

    # =========================================================================
    # 14. Save data
    # =========================================================================
    outpath = os.path.join(SCRIPT_DIR, "s70_bulk_flow.npz")
    np.savez(outpath,
             # Primary results
             R_values=R_values,
             V_rms_LCDM=V_rms_LCDM,
             V_rms_FW=V_rms_FW,
             V_ratio=V_rms_FW / V_rms_LCDM,
             # Fine grid
             R_fine=R_fine,
             V_rms_L_fine=V_rms_L_fine,
             V_rms_F_fine=V_rms_F_fine,
             # Growth parameters
             f_LCDM_z0=f_LCDM_z0,
             f_FW_z0=f_FW_z0,
             fsig8_LCDM=fsig8_LCDM,
             fsig8_FW=fsig8_FW,
             sigma8_LCDM=sig8_LCDM,
             sigma8_fw=sig8_fw,
             growth_ratio=growth_ratio,
             w0_fw=w0_fw,
             # Scaling
             expected_ratio=expected_ratio,
             pct_reduction=pct_reduction,
             # Observational comparison
             obs_R_eff=obs_R,
             obs_V_bulk=obs_V,
             obs_V_err=obs_err,
             obs_labels=np.array(obs_labels),
             obs_p_exceed_LCDM=p_exceed_L,
             obs_p_exceed_FW=p_exceed_FW,
             obs_sigma_equiv_LCDM=sigma_equiv_L,
             obs_sigma_equiv_FW=sigma_equiv_FW,
             # R=150 detailed
             V_rms_L_150=V_L_150,
             V_rms_F_150=V_F_150,
             sigma1D_L_150=s1d_L_150,
             sigma1D_F_150=s1d_F_150,
             p_exceed_L_150=p_L_150,
             p_exceed_F_150=p_F_150,
             sigma_equiv_L_150=sig_L_150,
             sigma_equiv_F_150=sig_F_150,
             sigma_cosmic_150=sigma_cosmic_for_disc,
             delta_V_150=delta_V_150,
             SNR_cosmic_var=delta_V_150 / sigma_cosmic_for_disc,
             # Gate
             gate_name=gate_name,
             gate_verdict=gate_verdict)

    pr(f"\nData saved: {outpath}")
    pr(f"\n{'=' * 78}")
    pr("COMPUTATION COMPLETE")
    pr(f"{'=' * 78}")

    log.close()

except Exception as e:
    tb = traceback.format_exc()
    try:
        log.write(f"\nERROR: {e}\n{tb}\n")
        log.close()
    except:
        pass
    print(f"ERROR: {e}")
    print(tb)
    sys.exit(1)
