#!/usr/bin/env python3
"""
s69_euclid_joint.py -- EUCLID-ISW-RSD-JOINT-69: Combined Fisher Forecast
==========================================================================
Gate: EUCLID-JOINT-69 (INFO)

Constructs a combined Fisher matrix forecast for Euclid ISW + RSD + CMB-S4
lensing to determine the joint discrimination power between the phonon-exflation
framework (w_0 = -0.918, c_s^2 = 0) and w_0CDM (generic w_0, c_s^2 = 1).

Parameter space: theta = {w_0, c_s^2_DE}
  Framework fiducial: w_0 = -0.918, c_s^2_DE = 0 (tracking vacuum)
  Null hypothesis: w_0CDM with arbitrary w_0 and c_s^2_DE = 1

Three Fisher sub-matrices:
  F_ISW:  ISW-galaxy cross-correlation C_l^{Tg} at l = 2-30
          Uses Euclid photometric survey (n_g ~ 30/arcmin^2, f_sky = 0.364)
  F_RSD:  Redshift-space distortion f*sigma_8 at Euclid spectroscopic bins
          (z = 0.9, 1.1, 1.3, 1.5, 1.8)
  F_lens: CMB lensing power spectrum C_l^{kk} at l = 100-500 with CMB-S4 noise

Combined: F_total = F_ISW + F_RSD + F_lens

Input files:
  - s68_isw_tracking_test.npz (ISW ratios)
  - s69_pvd05_fsigma8.npz (growth rate curves)

Physics:
  The key discriminant is c_s^2_DE. The tracking vacuum (c_s^2 = 0) allows DE to
  cluster with matter, enhancing ISW and modifying growth. Quintessence (c_s^2 = 1)
  has smooth DE. The ISW-galaxy cross-correlation at l < 30 is the cleanest probe
  of c_s^2_DE. RSD constrains w_0 independently. Lensing adds constraining power
  on w_0 through the lensing efficiency kernel.

Observational references:
  Euclid photometric: Euclid Collaboration (2020), A&A 642, A191 (Red Book)
  Euclid spectroscopic: Euclid Collaboration (2020), A&A 642, A191
  CMB-S4: CMB-S4 Collaboration (2016), arXiv:1610.02743
  ISW-galaxy: Planck 2015 results XXI (1502.01595)

Author: Katie Mack (Cosmic Bridge)
Session: 69, Task EUCLID-ISW-RSD-JOINT-69
"""

import os
import sys
import traceback

try:
    import numpy as np
    from scipy.integrate import quad, solve_ivp
    from scipy.interpolate import interp1d
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, SCRIPT_DIR)

    from canonical_constants import (
        H_0_km_s_Mpc, Omega_m, Omega_Lambda, Omega_b, Omega_DM,
        Omega_r, T_CMB, c_light_km_s, sigma_8, A_s_CMB,
        Mpc_to_m, H_0_inv_s, arcsec_to_rad
    )

    LOGPATH = os.path.join(SCRIPT_DIR, "s69_euclid_joint_log.txt")
    log = open(LOGPATH, "w")

    def pr(msg=""):
        print(str(msg))
        log.write(str(msg) + "\n")
        log.flush()

    pr("=" * 78)
    pr("EUCLID-ISW-RSD-JOINT-69: Combined Fisher Forecast")
    pr("Gate: EUCLID-JOINT-69 (INFO)")
    pr("=" * 78)

    # =========================================================================
    # 0. Constants and parameters
    # =========================================================================
    H0 = H_0_km_s_Mpc   # km/s/Mpc
    c = c_light_km_s     # km/s
    Om_m = Omega_m       # 0.315
    Om_r = Omega_r       # 9.15e-5
    Om_DE = Omega_Lambda # 0.685
    sig8 = sigma_8       # 0.811

    # Framework parameters
    # w0_FW = -0.918       # Volovik vacuum + effacement (S68)  # S72: now imported from canonical_constants
    cs2_FW = 0.0         # Tracking vacuum: c_s^2_DE = 0  # (local)
    # wa_FW = 0.0          # w_a locked = 0  # S72: now imported from canonical_constants

    # Alternative models for comparison
    # w0_LCDM = -1.0  # S72: now imported from canonical_constants
    cs2_quint = 1.0      # Quintessence: c_s^2_DE = 1  # (local)

    # Fisher step sizes (numerical derivatives)
    dw0 = 0.01           # Step in w_0
    dcs2 = 0.05          # Step in c_s^2_DE (0 is boundary, use one-sided from 0 to 0.05)

    # Euclid survey parameters (Red Book, Euclid Collaboration 2020)
    f_sky_euclid = 15000.0 / 41253.0  # 15,000 deg^2 = 0.364
    n_g_arcmin2 = 30.0   # galaxy number density (arcmin^{-2})
    n_g_sr = n_g_arcmin2 / arcsec_to_rad**2 * (1.0/3600.0)  # convert to sr^{-1}
    # Actually: n_g in sr^{-1} = n_g(arcmin^{-2}) * (arcmin/rad)^2 = 30 * (60*180/pi)^2
    n_g_sr = n_g_arcmin2 * (60.0 * 180.0 / np.pi)**2  # ~ 3.53e9 sr^{-1}

    # CMB-S4 noise parameters (CMB-S4 Science Book, 1610.02743)
    # Temperature noise: sigma_T = 1 muK-arcmin
    # Beam: theta_FWHM = 1 arcmin
    sigma_T_muK_arcmin = 1.0  # (local)
    theta_beam_arcmin = 1.0  # (local)
    theta_beam_rad = theta_beam_arcmin * np.pi / (180.0 * 60.0)

    pr(f"\nSurvey parameters:")
    pr(f"  Euclid f_sky = {f_sky_euclid:.4f}")
    pr(f"  Euclid n_g = {n_g_arcmin2} arcmin^{{-2}} = {n_g_sr:.3e} sr^{{-1}}")
    pr(f"  CMB-S4 noise = {sigma_T_muK_arcmin} muK-arcmin, beam = {theta_beam_arcmin} arcmin")

    # =========================================================================
    # 1. Cosmological functions
    # =========================================================================
    def E_squared(z, w0=-1.0, wa=0.0):
        """(H/H0)^2 for flat w0waCDM."""
        zp1 = 1.0 + z
        de_factor = zp1**(3*(1 + w0 + wa)) * np.exp(-3 * wa * z / zp1)
        return Om_r * zp1**4 + Om_m * zp1**3 + Om_DE * de_factor

    def H_func(z, w0=-1.0, wa=0.0):
        """Hubble parameter in km/s/Mpc."""
        return H0 * np.sqrt(E_squared(z, w0, wa))

    def chi(z, w0=-1.0, wa=0.0):
        """Comoving distance in Mpc."""
        result, _ = quad(lambda zp: c / H_func(zp, w0, wa), 0, z)
        return result

    def Omega_m_z(z, w0=-1.0, wa=0.0):
        """Matter density parameter at redshift z."""
        return Om_m * (1 + z)**3 / E_squared(z, w0, wa)

    def Omega_DE_z(z, w0=-1.0, wa=0.0):
        """DE density parameter at redshift z."""
        zp1 = 1.0 + z
        de_factor = zp1**(3*(1 + w0 + wa)) * np.exp(-3 * wa * z / zp1)
        return Om_DE * de_factor / E_squared(z, w0, wa)

    # =========================================================================
    # 2. Growth factor via ODE
    # =========================================================================
    def compute_growth(z_out, w0=-1.0, wa=0.0, N_a=10000):
        """Compute D(z), f(z) = dln(D)/dln(a) via ODE integration.

        Growth ODE in scale factor a:
          D'' + [3/a + E'/E] D' - (3/2) Omega_m / (a^3 E^2) D = 0
        where E = H/H0, primes are d/da.
        """
        a_start = 1e-4  # (local)
        a_end = 1.0  # (local)
        a_arr = np.linspace(a_start, a_end, N_a)

        def dE2_da(a):
            z = 1.0/a - 1.0
            zp1 = 1.0/a
            eps = 1e-6
            e2p = E_squared(1.0/(a+eps) - 1.0, w0, wa)
            e2m = E_squared(1.0/(a-eps) - 1.0, w0, wa)
            return (e2p - e2m) / (2*eps)

        def rhs(a, y):
            D, Dp = y
            z = 1.0/a - 1.0
            E2 = E_squared(z, w0, wa)
            dE2 = dE2_da(a)
            coeff1 = 3.0/a + 0.5 * dE2 / E2
            coeff2 = 1.5 * Om_m / (a**3 * E2)
            return [Dp, -coeff1 * Dp + coeff2 * D]

        # Initial conditions in matter domination: D ~ a, D' = 1
        y0 = [a_start, 1.0]
        sol = solve_ivp(rhs, [a_start, a_end], y0, t_eval=a_arr, method='RK45',
                        rtol=1e-10, atol=1e-13)

        D_arr = sol.y[0]
        Dp_arr = sol.y[1]  # dD/da

        # Normalize D(a=1) = 1
        D0 = D_arr[-1]
        D_arr /= D0
        Dp_arr /= D0

        # f = a/D * dD/da = dln(D)/dln(a)
        f_arr = sol.t / D_arr * Dp_arr

        # Interpolate and evaluate at z_out
        z_grid = 1.0/sol.t - 1.0
        D_interp = interp1d(z_grid[::-1], D_arr[::-1], kind='cubic', fill_value='extrapolate')
        f_interp = interp1d(z_grid[::-1], f_arr[::-1], kind='cubic', fill_value='extrapolate')

        return D_interp(z_out), f_interp(z_out)

    # =========================================================================
    # 3. ISW-galaxy cross-correlation
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 1: ISW FISHER MATRIX")
    pr("="*72)

    # Load S68 ISW results
    isw_data = np.load(os.path.join(SCRIPT_DIR, "s68_isw_tracking_test.npz"))
    l_isw = isw_data['l_arr']      # ell values
    Cl_A = isw_data['Cl_A']        # LCDM
    Cl_B = isw_data['Cl_B']        # Framework (w_0=-0.918, c_s^2=0)
    Cl_C = isw_data['Cl_C']        # Quintessence (w_0=-0.918, c_s^2=1)
    ratio_BA = isw_data['ratio_BA']  # FW / LCDM
    ratio_BC = isw_data['ratio_BC']  # FW / Quint

    pr(f"Loaded ISW data: {len(l_isw)} multipoles, l = [{l_isw[0]}, {l_isw[-1]}]")
    pr(f"  Mean C_l^Tg ratios (l < 30):")
    mask_low_l = l_isw <= 30
    pr(f"    FW/LCDM  = {np.mean(ratio_BA[mask_low_l]):.4f}")
    pr(f"    FW/Quint = {np.mean(ratio_BC[mask_low_l]):.4f}")

    # ISW Fisher matrix in {w_0, c_s^2_DE}
    #
    # The ISW power spectrum C_l^{Tg} depends on both w_0 and c_s^2_DE.
    # We have three computed models:
    #   A: (w_0=-1.0, c_s^2=N/A)  -- LCDM
    #   B: (w_0=-0.918, c_s^2=0)  -- Framework (tracking)
    #   C: (w_0=-0.918, c_s^2=1)  -- Quintessence (smooth)
    #
    # Numerical derivatives:
    #   dCl/dw0  at c_s^2=0:  approx from (C_B - C_A_shifted) / dw0
    #     where A_shifted uses LCDM (w=-1, no DE pert) and B uses w=-0.918 with tracking
    #     delta_w0 = -0.918 - (-1.0) = 0.082
    #   dCl/dc_s^2 at w0=-0.918: from (C_C - C_B) / (1 - 0)
    #     delta_c_s^2 = 1.0 - 0.0 = 1.0

    # Derivatives at fiducial (w_0=-0.918, c_s^2=0)
    delta_w0_AB = w0_FW - w0_LCDM   # = 0.082
    delta_cs2_BC = cs2_quint - cs2_FW  # = 1.0

    # dCl/dw0: use (C_B - C_A) / delta_w0
    # This captures both expansion history AND tracking effects together at c_s^2=0
    # For the pure w_0 effect, we should use the quintessence pair (C_C - C_A)
    # which isolates expansion history (both have smooth DE)
    # But since our fiducial is c_s^2=0, the correct derivative is at c_s^2=0
    dCl_dw0 = (Cl_B - Cl_A) / delta_w0_AB

    # dCl/dc_s^2: use (C_C - C_B) / delta_cs2
    # This isolates the tracking effect at fixed w_0
    dCl_dcs2 = (Cl_C - Cl_B) / delta_cs2_BC

    pr(f"\n  ISW derivatives at fiducial (w_0={w0_FW}, c_s^2={cs2_FW}):")
    pr(f"    delta_w0 = {delta_w0_AB:.3f}, delta_c_s^2 = {delta_cs2_BC:.3f}")
    pr(f"    Mean |dCl/dw0| (l<30)  = {np.mean(np.abs(dCl_dw0[mask_low_l])):.4e}")
    pr(f"    Mean |dCl/dcs2| (l<30) = {np.mean(np.abs(dCl_dcs2[mask_low_l])):.4e}")

    # ISW covariance: Cov(l) = [C_l^{TT} + N_l^{TT}] * [C_l^{gg} + 1/n_g] / (f_sky * (2l+1))
    #
    # C_l^{TT}: CMB temperature power spectrum (use analytic approximation)
    # C_l^{gg}: galaxy angular power spectrum
    # N_l^{TT}: CMB noise (negligible for Planck/CMB-S4 at l < 30)
    #
    # For a Fisher forecast at l < 30, cosmic variance dominates. The ISW signal
    # is subdominant to the primordial CMB at these scales, so C_l^{TT} is
    # dominated by the primary CMB.

    # Primary CMB TT power spectrum (approximate Sachs-Wolfe + acoustic)
    # At l < 30, use Sachs-Wolfe: l(l+1) C_l^{TT} / (2*pi) ~ (T_CMB)^2 * A_s / 9
    # C_l^{TT} ~ 2*pi * (T_CMB)^2 * A_s / (9 * l * (l+1))
    # In muK^2: T_CMB_muK = 2.7255e6 muK
    T_CMB_muK = T_CMB * 1e6
    Cl_TT = np.zeros(len(l_isw))
    for i, l in enumerate(l_isw):
        # Sachs-Wolfe plateau: l(l+1) C_l/(2pi) ~ 1090 muK^2
        # => C_l ~ 2*pi * 1090 / (l*(l+1)) muK^2
        Cl_TT[i] = 2 * np.pi * 1090.0 / (l * (l + 1))  # muK^2

    # CMB-S4 noise
    Nl_TT = (sigma_T_muK_arcmin * np.pi / (180 * 60))**2 * \
            np.exp(l_isw * (l_isw + 1) * theta_beam_rad**2 / (8 * np.log(2)))

    # Galaxy angular power spectrum: C_l^{gg} ~ b^2 * P_m(k=l/chi) / chi^2
    # For ISW at l < 30, typical z ~ 0.5-1, chi ~ 1500 Mpc, so k ~ 0.01-0.02 h/Mpc
    # b ~ 1.5 (typical Euclid photometric bias)
    # P_m ~ 10^4 (Mpc/h)^3 at k ~ 0.01 h/Mpc
    # C_l^gg ~ b^2 * integral[dN/dz * D^2 * P(l/chi) / chi^2 / H(z)] dz
    # Approximate with C_l^{gg} ~ 1e-6 for these scales (order of magnitude from Euclid forecasts)
    bias_g = 1.5  # (local)
    # Galaxy noise: N_l^{gg} = 1/n_g (shot noise in sr)
    Nl_gg = 1.0 / n_g_sr

    # Simple galaxy power spectrum model at ISW scales
    # Using Limber: C_l^{gg} = integral dz [dN/dz]^2 * H(z)/c * b^2 * P(l/chi, z) / chi^2
    # For l ~ 2-30, k = l/chi ~ 0.001-0.02 Mpc^{-1} (linear regime)
    # P_lin(k) ~ A_s * (k/k_piv)^{n_s-1} * T^2(k) * D^2(z) * (2*pi^2/k^3) * (c*k/H0)^4
    # Simplified: C_l^{gg} ~ 1e-7 to 1e-5 across l = 2-30
    # For Fisher forecast, we need an estimate. Use the Euclid Red Book Fig 2.3 scaling.
    # At l ~ 10: C_l^{gg} ~ 5e-6
    z_eff_isw = 0.6  # effective redshift for ISW  # (local)
    chi_eff = chi(z_eff_isw, w0_FW)  # Mpc
    D_eff, f_eff = compute_growth(z_eff_isw, w0_FW)
    # Linear P(k) ~ 2*pi^2 * A_s * (k/k_piv)^(n_s-1) / k^3 * T^2 * D^2
    # At k ~ 0.01 Mpc^{-1}: P ~ 10^4 Mpc^3 (from Planck)
    k_piv = 0.05  # Mpc^{-1}  # (local)
    P_lin_ref = 1e4  # Mpc^3, approximate at k ~ 0.01

    # Galaxy redshift distribution: dN/dz ~ z^2 exp(-z/z0) with z0 ~ 0.3 for Euclid photo
    # Integrated (dN/dz)^2 / (chi^2 * H/c) ~ n_g_eff
    # C_l^{gg} ~ b^2 * n_g_eff * P_lin(l/chi_eff)
    # For l ~ 10: k = 10/chi(0.6) ~ 10/1700 ~ 0.006 Mpc^{-1}
    # P_lin(0.006) ~ 2e4 Mpc^3 (slightly larger than at 0.01)
    # Rough integral of window function ~ Delta_z / chi_eff^2 * c/H(z_eff)
    # ~ 1.0 / (1700^2) * 3e5/100 ~ 1e-3

    Cl_gg = np.zeros(len(l_isw))
    for i, l_val in enumerate(l_isw):
        if l_val < 2:
            Cl_gg[i] = 1e-5
        else:
            k_eff = l_val / chi_eff
            # Simple scaling: P(k) ~ P_ref * (k/k_ref)^{n_s-4} for k < k_eq
            # n_s ~ 0.96, so exponent ~ -3.04
            # But transfer function modifies this. Use P(k) ~ 2e4 * (k/0.006)^(-1.5) for k < 0.1
            P_k = P_lin_ref * (k_eff / 0.01)**(-1.5) if k_eff < 0.1 else P_lin_ref * 0.1
            Cl_gg[i] = bias_g**2 * P_k * D_eff**2 * 1e-3 / chi_eff**2
            Cl_gg[i] = max(Cl_gg[i], 1e-8)

    # ISW-galaxy cross-spectrum signal (use C_B as fiducial)
    # The signal is in units consistent with the ISW computation from S68
    # S68 Cl_B are in arbitrary normalization. For Fisher, we need the ratio structure.
    # The ISW SNR per mode is: SNR^2(l) = f_sky * (2l+1) * (C_l^{Tg})^2 / [(C_l^{TT} + N_TT)(C_l^{gg} + N_gg)]
    #
    # For the DERIVATIVE-based Fisher matrix, we work in terms of the ISW amplitude.
    # F_ij = sum_l f_sky * (2l+1)/2 * Tr[C^{-1} dC/dtheta_i C^{-1} dC/dtheta_j]
    # For the Tg cross only:
    # F_ij = sum_l f_sky * (2l+1) * [dC_l^Tg/dtheta_i * dC_l^Tg/dtheta_j] / sigma^2(C_l^Tg)
    # where sigma^2(C_l^Tg) = [(C_l^{TT})(C_l^{gg} + 1/n_g) + (C_l^{Tg})^2] / [f_sky * (2l+1)]

    # The S68 C_l values are normalized as fractional ISW amplitude ratios.
    # We need to convert to a consistent normalization.
    # From S68: the Cl_A, Cl_B, Cl_C represent relative power in arbitrary normalization.
    # The ISW SNR was computed from these ratios: SNR = |A_FW - A_LCDM| / sigma_A
    # where sigma_A = 0.25 for Planck, and sigma_A * sqrt(Planck_modes/Euclid_modes) for Euclid.
    #
    # For the Fisher matrix, we use the AMPLITUDE approach:
    # The ISW amplitude A_ISW is defined relative to LCDM prediction.
    # A_FW = mean(Cl_B/Cl_A) at l < 30 = 1.123
    # A_Quint = mean(Cl_C/Cl_A) at l < 30 = 1.044
    #
    # dA/dw0 at (w_0=-0.918, cs2=0): (A_FW - 1.0) / delta_w0 where 1.0 is LCDM
    # dA/dcs2 at (w0=-0.918, cs2=0): (A_Quint - A_FW) / delta_cs2

    # Work with ISW amplitude approach (consistent with Planck ISW analysis)
    A_FW = float(isw_data['mean_ratio_BA'])      # 1.123
    A_Quint = float(isw_data['mean_ratio_CA'])    # 1.044
    A_LCDM = 1.0  # (local)

    pr(f"\n  ISW amplitudes (relative to LCDM):")
    pr(f"    A_FW   = {A_FW:.4f} (w_0=-0.918, c_s^2=0)")
    pr(f"    A_Quint = {A_Quint:.4f} (w_0=-0.918, c_s^2=1)")
    pr(f"    A_LCDM = {A_LCDM:.4f}")

    # Derivatives of ISW amplitude
    # dA/dw0: Combined effect of expansion + tracking at c_s^2=0
    #   (A_FW - A_LCDM) / (w0_FW - w0_LCDM) = (1.123 - 1.0) / 0.082 = 1.500
    dA_dw0 = (A_FW - A_LCDM) / delta_w0_AB
    # dA/dc_s^2: Tracking effect at fixed w_0=-0.918
    #   (A_Quint - A_FW) / (1.0 - 0.0) = (1.044 - 1.123) / 1.0 = -0.079
    dA_dcs2 = (A_Quint - A_FW) / delta_cs2_BC

    pr(f"\n  ISW amplitude derivatives:")
    pr(f"    dA/dw_0    = {dA_dw0:.4f}")
    pr(f"    dA/dc_s^2  = {dA_dcs2:.4f}")

    # ISW measurement uncertainty
    # Planck: sigma_A = 0.25
    # Euclid photometric: improvement factor ~ sqrt(N_modes_Euclid / N_modes_Planck)
    # Euclid f_sky ~ 0.36 vs Planck f_sky ~ 0.78 (fewer modes), BUT Euclid has
    # ~10x more galaxy density and multiple tomographic bins.
    # The dominant limitation is cosmic variance at l < 30.
    # For l_max = 30: N_modes = sum(2l+1) * f_sky ~ 30^2 * 0.36 ~ 324
    # Planck ISW: sigma ~ 0.25 using ~600 modes (from their pipeline)
    # Euclid improvement is mainly from galaxy density (lower shot noise):
    # sigma_A(Euclid) ~ sigma_A(Planck) * sqrt(C_gg^Planck + N_Planck) / sqrt(C_gg^Euclid + N_Euclid)
    # With ~10x better n_g: improvement factor ~ 2-3x
    # Conservative estimate from literature: sigma_A(Euclid photo) ~ 0.10
    # (Euclid Red Book forecasts for ISW are broadly consistent with this)

    # Compute ISW Fisher using per-multipole approach
    # F_ij^ISW = sum_{l=2}^{30} f_sky * (2l+1) / [sigma_l^{Tg}]^2 * d_i * d_j
    # where d_i = dC_l^{Tg}/dtheta_i / C_l^{Tg} * A_ISW
    # Since we work with amplitude A: F_ij = dA/dtheta_i * dA/dtheta_j / sigma_A^2

    # Per-multipole variance of C_l^{Tg}
    # Var(C_l^{Tg}) = 1/((2l+1)*f_sky) * [(C_l^{TT})(C_l^{gg} + 1/n_g) + (C_l^{Tg})^2]
    # At l < 30, C_l^{TT} >> C_l^{Tg} (ISW is ~5% of primary TT at l=10)
    # So Var ~ C_l^{TT} * (C_l^{gg} + 1/n_g) / ((2l+1)*f_sky)

    # The S68 ISW SNR calculation used:
    # SNR(Euclid) = SNR(Planck) * improvement_factor(5x)
    # This gave SNR(FW vs LCDM) = 2.46 for Euclid
    # Which corresponds to sigma_A(Euclid) = |A_FW - A_LCDM| / SNR = 0.123/2.46 = 0.050
    sigma_A_euclid = (A_FW - A_LCDM) / float(isw_data['SNR_FW_vs_LCDM_euclid'])

    pr(f"    sigma_A(Planck) = {float(isw_data['sigma_A_ISW']):.3f}")
    pr(f"    sigma_A(Euclid) = {sigma_A_euclid:.4f}")

    # ISW Fisher matrix (2x2 in {w_0, c_s^2})
    F_ISW = np.zeros((2, 2))
    deriv_ISW = np.array([dA_dw0, dA_dcs2])
    F_ISW = np.outer(deriv_ISW, deriv_ISW) / sigma_A_euclid**2

    pr(f"\n  ISW Fisher matrix:")
    pr(f"    F_ISW[w0,w0]     = {F_ISW[0,0]:.4f}")
    pr(f"    F_ISW[w0,cs2]    = {F_ISW[0,1]:.4f}")
    pr(f"    F_ISW[cs2,cs2]   = {F_ISW[1,1]:.4f}")

    # =========================================================================
    # 4. RSD Fisher matrix
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 2: RSD FISHER MATRIX")
    pr("="*72)

    # Euclid spectroscopic survey bins (from Euclid Red Book Table 3.1)
    # 5 bins covering z = 0.9-1.8
    z_euclid_spec = np.array([0.9, 1.1, 1.3, 1.5, 1.8])
    # Expected sigma(f*sigma_8) per bin (from Euclid Red Book forecasts)
    # These are approximate from Table 3.1 of Laureijs et al. (2011)
    # and updated Euclid forecasts (Blanchard et al. 2020, A&A 642, A191)
    # Typical: sigma(f*sig8) ~ 0.010-0.020 per bin
    sigma_fsig8_euclid = np.array([0.010, 0.012, 0.014, 0.017, 0.020])

    # Compute f*sigma_8 for fiducial model and shifted models
    pr("\n  Computing growth rates for fiducial and shifted models...")

    # Fiducial (w_0=-0.918, c_s^2=0)
    D_fid, f_fid = compute_growth(z_euclid_spec, w0_FW)
    fsig8_fid = f_fid * sig8 * D_fid  # using Planck sigma_8 as normalization
    # Correction: framework has sigma_8 = 0.793 (from S69)
    sig8_fw = 0.793  # (local)
    fsig8_fid_fw = f_fid * sig8_fw * D_fid

    # Model with w_0 + dw0
    D_wp, f_wp = compute_growth(z_euclid_spec, w0_FW + dw0)
    fsig8_wp = f_wp * sig8 * D_wp

    # Model with w_0 - dw0
    D_wm, f_wm = compute_growth(z_euclid_spec, w0_FW - dw0)
    fsig8_wm = f_wm * sig8 * D_wm

    # Derivative dfsig8/dw0
    dfsig8_dw0 = (fsig8_wp - fsig8_wm) / (2 * dw0)

    # c_s^2 effect on growth: in the tracking vacuum, DE clusters with c_s^2=0.
    # The effective Newton's constant is modified:
    # G_eff = G_N * [1 + (1+w)/(1-3w) * Omega_DE/Omega_m] for c_s^2=0
    # For c_s^2=1: G_eff = G_N (no DE clustering on sub-horizon scales)
    #
    # Growth rate modification from c_s^2:
    # delta(f*sigma_8) / delta(c_s^2) ~ f*sigma_8 * (1+w)/(1-3w) * Omega_DE/Omega_m * correction
    # At z ~ 1: Omega_DE ~ 0.3, Omega_m ~ 0.7
    # (1+w)/(1-3w) = 0.082/3.754 = 0.0218 at w=-0.918
    # Enhancement: ~ 0.0218 * 0.3/0.7 * f*sig8 ~ 0.009 * f*sig8 ~ 0.3% at z~1

    # Compute the c_s^2 effect on f*sigma_8 more carefully.
    # With tracking (c_s^2=0), the growth equation is modified:
    # D'' + [...] D' - 3/2 * Omega_m_eff(a) / (a^3 E^2) * D = 0
    # where Omega_m_eff includes DE clustering: Omega_m_eff = Omega_m + Omega_DE * (1+w)/(1-3w)
    # The correction is: delta(f*sig8)/f*sig8 ~ (1+w)/(2*(1-3w)) * integral of Omega_DE/Omega_m
    # This is a few percent effect at most.

    # For the tracking model, compute growth with enhanced Poisson equation
    def compute_growth_tracking(z_out, w0, cs2_de, N_a=10000):
        """Growth with DE clustering (c_s^2_DE modifies Poisson equation)."""
        a_start = 1e-4  # (local)
        a_end = 1.0  # (local)
        a_arr = np.linspace(a_start, a_end, N_a)

        def rhs(a, y):
            D, Dp = y
            z = 1.0/a - 1.0
            E2 = E_squared(z, w0)
            eps = 1e-6
            e2p = E_squared(1.0/(a+eps) - 1.0, w0)
            e2m = E_squared(1.0/(a-eps) - 1.0, w0)
            dE2 = (e2p - e2m) / (2*eps)

            coeff1 = 3.0/a + 0.5 * dE2 / E2
            # Standard: 3/2 * Omega_m / (a^3 * E^2)
            source = 1.5 * Om_m / (a**3 * E2)

            # Tracking DE enhancement: delta_DE = (1+w)/(1-3w) * delta_m
            # adds (1+w)/(1-3w) * Omega_DE(z) to the effective matter source
            if cs2_de < 0.5:
                zp1 = 1.0/a
                de_factor = zp1**(3*(1 + w0)) * Om_DE / E2
                ratio_de = (1 + w0) / (1 - 3*w0) if abs(1 - 3*w0) > 1e-10 else 0.0
                source += 1.5 * de_factor * ratio_de / (a**3)

            return [Dp, -coeff1 * Dp + source * D]

        y0 = [a_start, 1.0]
        sol = solve_ivp(rhs, [a_start, a_end], y0, t_eval=a_arr, method='RK45',
                        rtol=1e-10, atol=1e-13)

        D_arr = sol.y[0]
        Dp_arr = sol.y[1]
        D0 = D_arr[-1]
        D_arr /= D0
        Dp_arr /= D0
        f_arr = sol.t / D_arr * Dp_arr

        z_grid = 1.0/sol.t - 1.0
        D_interp = interp1d(z_grid[::-1], D_arr[::-1], kind='cubic', fill_value='extrapolate')
        f_interp = interp1d(z_grid[::-1], f_arr[::-1], kind='cubic', fill_value='extrapolate')

        return D_interp(z_out), f_interp(z_out)

    # Fiducial with tracking (c_s^2=0)
    D_cs0, f_cs0 = compute_growth_tracking(z_euclid_spec, w0_FW, cs2_de=0.0)
    fsig8_cs0 = f_cs0 * sig8 * D_cs0

    # Smooth DE (c_s^2=1) -- same as standard growth
    D_cs1, f_cs1 = compute_growth_tracking(z_euclid_spec, w0_FW, cs2_de=1.0)
    fsig8_cs1 = f_cs1 * sig8 * D_cs1

    # Derivative dfsig8/dcs2
    dfsig8_dcs2 = (fsig8_cs1 - fsig8_cs0) / (cs2_quint - cs2_FW)

    pr(f"\n  Euclid spectroscopic bins:")
    pr(f"  {'z':>5s} | {'f*sig8(fid)':>12s} | {'df/dw0':>10s} | {'df/dcs2':>10s} | {'sigma':>8s}")
    pr(f"  {'-'*5}-+-{'-'*12}-+-{'-'*10}-+-{'-'*10}-+-{'-'*8}")
    for i in range(len(z_euclid_spec)):
        pr(f"  {z_euclid_spec[i]:5.2f} | {fsig8_cs0[i]:12.6f} | {dfsig8_dw0[i]:10.6f} | {dfsig8_dcs2[i]:10.6f} | {sigma_fsig8_euclid[i]:8.4f}")

    # RSD Fisher matrix
    F_RSD = np.zeros((2, 2))
    for i in range(len(z_euclid_spec)):
        deriv_rsd = np.array([dfsig8_dw0[i], dfsig8_dcs2[i]])
        F_RSD += np.outer(deriv_rsd, deriv_rsd) / sigma_fsig8_euclid[i]**2

    pr(f"\n  RSD Fisher matrix:")
    pr(f"    F_RSD[w0,w0]     = {F_RSD[0,0]:.4f}")
    pr(f"    F_RSD[w0,cs2]    = {F_RSD[0,1]:.4f}")
    pr(f"    F_RSD[cs2,cs2]   = {F_RSD[1,1]:.4f}")

    # =========================================================================
    # 5. CMB Lensing Fisher matrix
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 3: CMB LENSING FISHER MATRIX")
    pr("="*72)

    # CMB lensing convergence power spectrum C_l^{kk}
    # The lensing kernel is sensitive to the matter distribution at z ~ 0.5-5
    # and thus constrains w_0 through its effect on the distance-growth combination.
    #
    # C_l^{kk} = (9/4) * Omega_m^2 * H_0^4 / c^4 * integral dz * (1+z)^2 * D^2(z) *
    #            [chi(z*) - chi(z)]^2 / [chi(z*)^2 * chi(z)^2 * H(z)]
    # where z* ~ 1100 (CMB last scattering)
    #
    # For Fisher: we compute dCl^{kk}/dw0 and dCl^{kk}/dcs2

    l_lens = np.arange(100, 501)  # l = 100-500
    f_sky_cmbs4 = 0.4             # CMB-S4 sky fraction  # (local)

    # Lensing noise: N_l^{kk} for CMB-S4
    # From CMB-S4 Science Book: sigma(kappa) = 0.45 per arcmin^2 at l ~ 300
    # Approximate: N_l^{kk} ~ l^2 * sigma_N^2 / n_eff for iterative delensing
    # Use the CMB-S4 minimum-variance noise from their Table II (1610.02743):
    # N_l^{kk} ~ 1e-8 * (l/100)^2 for l < 500 (approximate)

    # More careful: The lensing reconstruction noise is
    # N_l^{kk} ~ (l^2 / (2*pi)) * [C_l^{TT} + N_l^{TT}]^2 / integral
    # But for a Fisher forecast, use published noise curves.
    # CMB-S4 achieves sigma(Cl^{kk}) ~ few percent for l in [100,500].
    # The noise per mode is:
    # N_l^{kk} ~ 1/(l^2) * (sigma_T * theta_beam)^2 / T_CMB^2 * exp(l^2 theta^2/(8ln2))
    # But this is the MAP noise, not the reconstruction noise.

    # Use CMB-S4 projected reconstruction noise from Abazajian et al. (2016):
    # For iterative EB delensing: N_l^{kk} ~ 1e-8 at l=200 (Fig 16)
    # Approximate power law: N_l^{kk} ~ 1e-8 * (l/200)^2

    # Signal: CMB lensing convergence power spectrum C_l^{kk}
    # Using Limber approximation:
    # C_l^{kk} = integral_0^{chi_*} dchi [W(chi)]^2 P_delta((l+0.5)/chi, z(chi)) / chi^2
    # W(chi) = (3/2) Omega_m (H_0/c)^2 chi (chi_* - chi)/chi_* (1+z)
    #
    # For P_delta(k, z), use the Eisenstein-Hu (1998) no-wiggle transfer function
    # with proper sigma_8 normalization. This gives P(k=0.1, z=0) ~ 5000 Mpc^3,
    # yielding C_l^{kk} ~ 1e-7 at l ~ 200 (matching Planck observations).

    chi_star = chi(1100.0)
    pr(f"  chi(z*=1100) = {chi_star:.0f} Mpc")

    z_lens_grid = np.linspace(0.01, 5.0, 200)

    # Eisenstein-Hu (1998) no-wiggle transfer function (ApJ 496, 605, Eq. 29-31)
    def transfer_EH(k_Mpc, Om_m_val=Om_m, Om_b_val=Omega_b, h_val=H0/100):
        """Eisenstein-Hu no-wiggle transfer function T(k).
        k in Mpc^{-1}. Returns T(k) normalized to T(0)=1.
        """
        Om_mh2 = Om_m_val * h_val**2
        Om_bh2 = Om_b_val * h_val**2
        f_b = Om_b_val / Om_m_val
        theta_cmb = T_CMB / 2.7  # ~ 1.0

        # Sound horizon
        s = 44.5 * np.log(9.83 / Om_mh2) / np.sqrt(1 + 10 * Om_bh2**0.75)
        # alpha_gamma
        alpha_gamma = 1 - 0.328 * np.log(431 * Om_mh2) * f_b + 0.38 * np.log(22.3 * Om_mh2) * f_b**2
        # Effective shape parameter Gamma_eff
        Gamma_eff = Om_m_val * h_val * (alpha_gamma + (1 - alpha_gamma) / (1 + (0.43 * k_Mpc * s)**4))
        # q
        q = k_Mpc * theta_cmb**2 / Gamma_eff
        # Transfer function (Eq. 29)
        L = np.log(2 * np.e + 1.8 * q)
        C = 14.2 + 731.0 / (1 + 62.5 * q)
        T0 = L / (L + C * q**2)
        return T0

    # Linear matter power spectrum P(k, z) with sigma_8 normalization
    n_s_val = 0.965  # (local)
    k_piv_val = 0.05  # Mpc^{-1} (Planck pivot)  # (local)

    def P_lin(k, z, D_z, w0_val=-1.0):
        """Linear matter power spectrum in Mpc^3.
        P(k,z) = P_0 * (k/k_piv)^{n_s} * T^2(k) * D^2(z)
        where P_0 is determined by sigma_8 normalization.
        """
        Tk = transfer_EH(k)
        # Shape: k^{n_s} * T^2(k) -- the actual P(k) shape
        return (k / k_piv_val)**n_s_val * Tk**2 * D_z**2

    # Normalize to sigma_8 = 0.811
    # sigma_8^2 = (1/(2*pi^2)) * integral dk k^2 P(k) W^2(k*R8)
    # where R8 = 8 Mpc/h = 8/0.674 Mpc
    R8 = 8.0 / (H0/100)  # ~ 11.87 Mpc
    k_norm = np.logspace(-4, 1, 5000)
    W_tophat = lambda kR: 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3

    integrand_sig8 = np.zeros_like(k_norm)
    for j, k in enumerate(k_norm):
        kR = k * R8
        if kR < 1e-6:
            W = 1.0  # (local)
        else:
            W = W_tophat(kR)
        integrand_sig8[j] = k**2 * P_lin(k, 0.0, 1.0) * W**2

    sigma8_unnorm_sq = np.trapezoid(integrand_sig8, k_norm) / (2 * np.pi**2)
    P0_norm = sig8**2 / sigma8_unnorm_sq  # normalization factor
    pr(f"  P(k) normalization: P_0 = {P0_norm:.4e} Mpc^3")

    # Verify: P(k=0.1, z=0) should be ~5000 Mpc^3
    P_check = P0_norm * P_lin(0.1, 0.0, 1.0)
    pr(f"  P(0.1 Mpc^-1, z=0) = {P_check:.0f} Mpc^3 (expect ~5000)")
    P_check2 = P0_norm * P_lin(0.01, 0.0, 1.0)
    pr(f"  P(0.01 Mpc^-1, z=0) = {P_check2:.0f} Mpc^3 (expect ~10000)")

    def compute_Clkk(l_arr, w0_val, cs2_val=0.0, use_tracking=False):
        """Compute CMB lensing convergence power spectrum C_l^{kk}.
        Uses Limber approximation with Eisenstein-Hu P(k) and sigma_8 normalization.
        """
        chi_arr = np.array([chi(z, w0_val) for z in z_lens_grid])
        chi_s = chi(1100.0, w0_val)

        if use_tracking and cs2_val < 0.5:
            D_arr, _ = compute_growth_tracking(z_lens_grid, w0_val, cs2_de=cs2_val)
        else:
            D_arr, _ = compute_growth(z_lens_grid, w0_val)

        H_arr = np.array([H_func(z, w0_val) for z in z_lens_grid])

        # Lensing kernel: W(chi) = (3/2) * Omega_m * (H_0/c)^2 * chi * (chi_s-chi)/chi_s * (1+z)
        W_kappa = 1.5 * Om_m * (H0/c)**2 * chi_arr * (chi_s - chi_arr) / chi_s * (1 + z_lens_grid)

        Cl = np.zeros(len(l_arr))
        for i, l in enumerate(l_arr):
            k_arr = (l + 0.5) / chi_arr
            P_k = np.array([P0_norm * P_lin(k, 0, D_arr[j]) for j, k in enumerate(k_arr)])

            # C_l = integral dz W^2(z) P(l/chi, z) H(z)/(c * chi^2)
            # Note: dchi = c/H(z) dz, so integral over z uses dz directly
            integrand = W_kappa**2 * P_k * H_arr / (c * chi_arr**2)
            Cl[i] = np.trapezoid(integrand, z_lens_grid)

        return Cl

    pr("  Computing lensing power spectra...")

    # Fiducial (w_0=-0.918, c_s^2=0, tracking)
    Clkk_fid = compute_Clkk(l_lens, w0_FW, cs2_val=0.0, use_tracking=True)

    # w_0 shifted
    Clkk_wp = compute_Clkk(l_lens, w0_FW + dw0, cs2_val=0.0, use_tracking=True)
    Clkk_wm = compute_Clkk(l_lens, w0_FW - dw0, cs2_val=0.0, use_tracking=True)

    # c_s^2 shifted (c_s^2 = 1, smooth)
    Clkk_cs1 = compute_Clkk(l_lens, w0_FW, cs2_val=1.0, use_tracking=False)

    # Derivatives
    dClkk_dw0 = (Clkk_wp - Clkk_wm) / (2 * dw0)
    dClkk_dcs2 = (Clkk_cs1 - Clkk_fid) / delta_cs2_BC

    pr(f"  Lensing derivatives computed for l = [{l_lens[0]}, {l_lens[-1]}]")
    pr(f"    Mean C_l^kk(fid) = {np.mean(Clkk_fid):.4e}")
    pr(f"    Mean dCl/dw0     = {np.mean(np.abs(dClkk_dw0)):.4e}")
    pr(f"    Mean dCl/dcs2    = {np.mean(np.abs(dClkk_dcs2)):.4e}")
    pr(f"    Cl^kk(cs2=1)/Cl^kk(cs2=0) - 1 = {np.mean(Clkk_cs1/Clkk_fid) - 1:.4f}")

    # CMB-S4 lensing noise
    Nlkk = 1e-8 * (l_lens / 200.0)**2  # Approximate CMB-S4 reconstruction noise

    # Lensing Fisher matrix
    F_lens = np.zeros((2, 2))
    for i in range(len(l_lens)):
        l = l_lens[i]
        # Total variance: sigma^2(Cl^kk) = 2/(f_sky*(2l+1)) * (Cl^kk + Nl^kk)^2
        sigma_Cl = np.sqrt(2.0 / (f_sky_cmbs4 * (2*l + 1))) * (Clkk_fid[i] + Nlkk[i])
        if sigma_Cl > 0:
            deriv_lens = np.array([dClkk_dw0[i], dClkk_dcs2[i]])
            F_lens += np.outer(deriv_lens, deriv_lens) / sigma_Cl**2

    pr(f"\n  Lensing Fisher matrix:")
    pr(f"    F_lens[w0,w0]     = {F_lens[0,0]:.4e}")
    pr(f"    F_lens[w0,cs2]    = {F_lens[0,1]:.4e}")
    pr(f"    F_lens[cs2,cs2]   = {F_lens[1,1]:.4e}")

    # =========================================================================
    # 6. Combined Fisher matrix
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 4: COMBINED FISHER MATRIX")
    pr("="*72)

    F_total = F_ISW + F_RSD + F_lens

    pr(f"\n  Individual Fisher matrices (diagonal entries: 1/sigma^2):")
    pr(f"  {'Probe':>12s} | {'F[w0,w0]':>12s} | {'F[w0,cs2]':>12s} | {'F[cs2,cs2]':>12s}")
    pr(f"  {'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}")
    pr(f"  {'ISW':>12s} | {F_ISW[0,0]:12.4f} | {F_ISW[0,1]:12.4f} | {F_ISW[1,1]:12.4f}")
    pr(f"  {'RSD':>12s} | {F_RSD[0,0]:12.4f} | {F_RSD[0,1]:12.4f} | {F_RSD[1,1]:12.4f}")
    pr(f"  {'Lensing':>12s} | {F_lens[0,0]:12.4e} | {F_lens[0,1]:12.4e} | {F_lens[1,1]:12.4e}")
    pr(f"  {'COMBINED':>12s} | {F_total[0,0]:12.4f} | {F_total[0,1]:12.4f} | {F_total[1,1]:12.4f}")

    # Invert for parameter covariance
    if np.linalg.det(F_total) > 0:
        Cov_total = np.linalg.inv(F_total)
        sigma_w0 = np.sqrt(Cov_total[0, 0])
        sigma_cs2 = np.sqrt(Cov_total[1, 1])
        rho_corr = Cov_total[0, 1] / (sigma_w0 * sigma_cs2)
    else:
        pr("  WARNING: Fisher matrix is singular, using pseudo-inverse")
        Cov_total = np.linalg.pinv(F_total)
        sigma_w0 = np.sqrt(Cov_total[0, 0])
        sigma_cs2 = np.sqrt(Cov_total[1, 1])
        rho_corr = Cov_total[0, 1] / (sigma_w0 * sigma_cs2) if sigma_w0 * sigma_cs2 > 0 else 0

    pr(f"\n  Marginalized constraints:")
    pr(f"    sigma(w_0)    = {sigma_w0:.4f}")
    pr(f"    sigma(c_s^2)  = {sigma_cs2:.4f}")
    pr(f"    correlation   = {rho_corr:.4f}")

    # Also compute individual probe constraints
    results_by_probe = {}
    for name, F in [("ISW", F_ISW), ("RSD", F_RSD), ("Lensing", F_lens),
                     ("ISW+RSD", F_ISW + F_RSD), ("COMBINED", F_total)]:
        if np.linalg.det(F) > 1e-30:
            C = np.linalg.inv(F)
            sw = np.sqrt(C[0, 0])
            sc = np.sqrt(C[1, 1])
            r = C[0, 1] / (sw * sc) if sw * sc > 0 else 0
        else:
            # Singular -- use diagonal only
            sw = 1.0 / np.sqrt(F[0, 0]) if F[0, 0] > 0 else np.inf
            sc = 1.0 / np.sqrt(F[1, 1]) if F[1, 1] > 0 else np.inf
            r = 0
        results_by_probe[name] = (sw, sc, r)

    pr(f"\n  Probe-by-probe marginalized constraints:")
    pr(f"  {'Probe':>12s} | {'sigma(w_0)':>12s} | {'sigma(c_s^2)':>12s} | {'corr':>8s}")
    pr(f"  {'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*8}")
    for name in ["ISW", "RSD", "Lensing", "ISW+RSD", "COMBINED"]:
        sw, sc, r = results_by_probe[name]
        pr(f"  {name:>12s} | {sw:12.4f} | {sc:12.4f} | {r:8.4f}")

    # =========================================================================
    # 7. Discrimination significance
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 5: DISCRIMINATION SIGNIFICANCE")
    pr("="*72)

    # Distance in parameter space between FW and w0CDM
    # FW: (w_0=-0.918, c_s^2=0)
    # w0CDM null: (w_0 free, c_s^2=1)
    # The key discriminant is c_s^2 = 0 vs c_s^2 = 1
    # At fixed w_0 = -0.918:
    delta_cs2 = 1.0 - 0.0  # = 1.0
    delta_w0_null = 0.0     # same w_0  # (local)

    # Significance of c_s^2 = 0 vs c_s^2 = 1 at fixed w_0:
    sig_cs2_only = delta_cs2 / sigma_cs2

    # Full 2D significance: Delta_theta^T F_total Delta_theta
    # where Delta_theta is the separation vector in parameter space
    # FW vs LCDM: Delta_theta = (0.082, -1.0)
    # FW vs Quintessence: Delta_theta = (0.0, -1.0)
    delta_FW_vs_LCDM = np.array([w0_FW - w0_LCDM, cs2_FW - cs2_quint])  # (0.082, -1.0)
    delta_FW_vs_Quint = np.array([0.0, cs2_FW - cs2_quint])               # (0.0, -1.0)

    chi2_FW_vs_LCDM = delta_FW_vs_LCDM @ F_total @ delta_FW_vs_LCDM
    chi2_FW_vs_Quint = delta_FW_vs_Quint @ F_total @ delta_FW_vs_Quint
    sig_FW_vs_LCDM = np.sqrt(chi2_FW_vs_LCDM)
    sig_FW_vs_Quint = np.sqrt(chi2_FW_vs_Quint)

    pr(f"\n  Discrimination significance (combined Euclid + CMB-S4):")
    pr(f"    FW vs LCDM         : {sig_FW_vs_LCDM:.2f}-sigma  (Delta_theta = [{delta_FW_vs_LCDM[0]:.3f}, {delta_FW_vs_LCDM[1]:.3f}])")
    pr(f"    FW vs Quintessence  : {sig_FW_vs_Quint:.2f}-sigma  (Delta_theta = [{delta_FW_vs_Quint[0]:.3f}, {delta_FW_vs_Quint[1]:.3f}])")
    pr(f"    c_s^2 = 0 vs 1     : {sig_cs2_only:.2f}-sigma  (marginalized 1D)")

    # Breakdown by probe
    pr(f"\n  Probe-by-probe discrimination (FW vs LCDM):")
    for name, F in [("ISW", F_ISW), ("RSD", F_RSD), ("Lensing", F_lens),
                     ("ISW+RSD", F_ISW + F_RSD), ("COMBINED", F_total)]:
        chi2 = delta_FW_vs_LCDM @ F @ delta_FW_vs_LCDM
        sig = np.sqrt(chi2)
        pr(f"    {name:>12s}: {sig:.2f}-sigma")

    pr(f"\n  Probe-by-probe discrimination (FW vs Quintessence):")
    for name, F in [("ISW", F_ISW), ("RSD", F_RSD), ("Lensing", F_lens),
                     ("ISW+RSD", F_ISW + F_RSD), ("COMBINED", F_total)]:
        chi2 = delta_FW_vs_Quint @ F @ delta_FW_vs_Quint
        sig = np.sqrt(chi2)
        pr(f"    {name:>12s}: {sig:.2f}-sigma")

    # Also compute with 21cm (from S68 forecast)
    # S68 gave 21cm SNR: FW vs LCDM = 12.3-sigma, FW vs Quint = 7.9-sigma
    # These were amplitude-only. Scale the ISW Fisher by (12.3/2.46)^2 for 21cm
    SNR_21cm_FW_LCDM = float(isw_data.get('SNR_FW_vs_LCDM_euclid', 2.46)) * 5.0  # S68: 21cm ~ 5x Euclid
    F_21cm = F_ISW * (SNR_21cm_FW_LCDM / float(isw_data['SNR_FW_vs_LCDM_euclid']))**2
    F_total_21cm = F_21cm + F_RSD + F_lens

    chi2_21cm_LCDM = delta_FW_vs_LCDM @ F_total_21cm @ delta_FW_vs_LCDM
    chi2_21cm_Quint = delta_FW_vs_Quint @ F_total_21cm @ delta_FW_vs_Quint

    pr(f"\n  Future with 21cm (replacing Euclid ISW):")
    pr(f"    FW vs LCDM         : {np.sqrt(chi2_21cm_LCDM):.2f}-sigma")
    pr(f"    FW vs Quintessence  : {np.sqrt(chi2_21cm_Quint):.2f}-sigma")

    # =========================================================================
    # 8. Figure of Merit
    # =========================================================================
    pr("\n" + "="*72)
    pr("SECTION 6: FIGURE OF MERIT")
    pr("="*72)

    # DETF Figure of Merit: FoM = 1 / sqrt(det(Cov_2D))
    # This is proportional to the reciprocal of the 2D error ellipse area
    FoM_total = 1.0 / np.sqrt(np.linalg.det(Cov_total)) if np.linalg.det(Cov_total) > 0 else 0
    pr(f"  FoM(w_0, c_s^2) = {FoM_total:.2f}")
    pr(f"  Ellipse area (95%) = {np.pi * 5.991 * np.sqrt(np.linalg.det(Cov_total)):.4f}")

    # =========================================================================
    # 9. Gate verdict
    # =========================================================================
    pr("\n" + "="*72)
    pr("GATE VERDICT: EUCLID-JOINT-69")
    pr("="*72)
    pr(f"\n  Gate type: INFO (report combined discrimination)")
    pr(f"  sigma(w_0) = {sigma_w0:.4f}")
    pr(f"  sigma(c_s^2) = {sigma_cs2:.4f}")
    pr(f"  FW vs LCDM: {sig_FW_vs_LCDM:.2f}-sigma (Euclid + CMB-S4)")
    pr(f"  FW vs Quintessence: {sig_FW_vs_Quint:.2f}-sigma (Euclid + CMB-S4)")
    pr(f"  FW vs LCDM (with 21cm): {np.sqrt(chi2_21cm_LCDM):.2f}-sigma")

    if sig_FW_vs_LCDM >= 5.0:
        verdict_str = "Definitive discrimination achievable"
    elif sig_FW_vs_LCDM >= 3.0:
        verdict_str = "Strong discrimination expected"
    elif sig_FW_vs_LCDM >= 2.0:
        verdict_str = "Marginal discrimination"
    else:
        verdict_str = "Discrimination below detection threshold"
    pr(f"  Assessment: {verdict_str}")

    gate_verdict = "INFO"
    pr(f"\n  Verdict: {gate_verdict}")

    # =========================================================================
    # 10. Save results
    # =========================================================================
    pr("\n" + "="*72)
    pr("SAVING RESULTS")
    pr("="*72)

    outpath = os.path.join(SCRIPT_DIR, "s69_euclid_joint.npz")
    np.savez(outpath,
             # Parameters
             w0_FW=w0_FW, cs2_FW=cs2_FW, wa_FW=wa_FW,
             w0_LCDM=w0_LCDM, cs2_quint=cs2_quint,
             # Fisher matrices
             F_ISW=F_ISW, F_RSD=F_RSD, F_lens=F_lens, F_total=F_total,
             Cov_total=Cov_total,
             # Marginalized errors
             sigma_w0=sigma_w0, sigma_cs2=sigma_cs2, rho_corr=rho_corr,
             # Discrimination
             sig_FW_vs_LCDM=sig_FW_vs_LCDM,
             sig_FW_vs_Quint=sig_FW_vs_Quint,
             sig_cs2_only=sig_cs2_only,
             sig_FW_vs_LCDM_21cm=np.sqrt(chi2_21cm_LCDM),
             sig_FW_vs_Quint_21cm=np.sqrt(chi2_21cm_Quint),
             # ISW inputs
             A_FW=A_FW, A_Quint=A_Quint,
             dA_dw0=dA_dw0, dA_dcs2=dA_dcs2,
             sigma_A_euclid=sigma_A_euclid,
             # RSD inputs
             z_euclid_spec=z_euclid_spec,
             sigma_fsig8_euclid=sigma_fsig8_euclid,
             fsig8_cs0=fsig8_cs0, fsig8_cs1=fsig8_cs1,
             dfsig8_dw0=dfsig8_dw0, dfsig8_dcs2=dfsig8_dcs2,
             # Lensing inputs
             l_lens=l_lens,
             Clkk_fid=Clkk_fid, Clkk_cs1=Clkk_cs1,
             dClkk_dw0=dClkk_dw0, dClkk_dcs2=dClkk_dcs2,
             # Gate
             gate_name=np.array("EUCLID-JOINT-69"),
             gate_verdict=np.array(gate_verdict),
             FoM=FoM_total,
             )

    pr(f"  Saved: {outpath}")

    # =========================================================================
    # 11. Plot
    # =========================================================================
    pr("\n  Generating plot...")

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle("EUCLID-ISW-RSD-JOINT-69: Combined Fisher Forecast\n"
                 f"FW (w$_0$={w0_FW}, c$_s^2$=0) vs w$_0$CDM (c$_s^2$=1)",
                 fontsize=14, fontweight='bold')

    # Panel 1: ISW C_l ratios (from S68)
    ax1 = axes[0, 0]
    ax1.plot(l_isw, ratio_BA, 'b-', lw=2, label='FW / LCDM')
    ax1.plot(l_isw, isw_data['ratio_BC'], 'r-', lw=2, label='FW / Quint')
    ax1.axhline(1.0, color='gray', ls='--', alpha=0.5)
    ax1.axvline(30, color='gray', ls=':', alpha=0.5, label='l=30 cutoff')
    ax1.set_xlabel('Multipole l', fontsize=12)
    ax1.set_ylabel(r'$C_\ell^{Tg}$ ratio', fontsize=12)
    ax1.set_title('ISW-Galaxy Cross-Correlation', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.set_xlim(2, 100)
    ax1.set_ylim(0.95, 1.25)

    # Panel 2: f*sigma_8 at Euclid bins
    ax2 = axes[0, 1]
    z_plot = np.linspace(0.5, 2.0, 200)
    D_plot_cs0, f_plot_cs0 = compute_growth_tracking(z_plot, w0_FW, cs2_de=0.0)
    D_plot_cs1, f_plot_cs1 = compute_growth_tracking(z_plot, w0_FW, cs2_de=1.0)
    D_plot_lcdm, f_plot_lcdm = compute_growth(z_plot, -1.0)

    fsig8_plot_cs0 = f_plot_cs0 * sig8 * D_plot_cs0
    fsig8_plot_cs1 = f_plot_cs1 * sig8 * D_plot_cs1
    fsig8_plot_lcdm = f_plot_lcdm * sig8 * D_plot_lcdm

    ax2.plot(z_plot, fsig8_plot_lcdm, 'k-', lw=2, label=r'$\Lambda$CDM')
    ax2.plot(z_plot, fsig8_plot_cs0, 'b-', lw=2, label=r'FW ($c_s^2$=0)')
    ax2.plot(z_plot, fsig8_plot_cs1, 'r--', lw=2, label=r'Quint ($c_s^2$=1)')
    ax2.errorbar(z_euclid_spec, fsig8_cs0, yerr=sigma_fsig8_euclid,
                 fmt='bs', ms=8, capsize=4, label='Euclid forecast', zorder=5)
    ax2.set_xlabel('Redshift z', fontsize=12)
    ax2.set_ylabel(r'$f\sigma_8(z)$', fontsize=12)
    ax2.set_title('Growth Rate (Euclid Spectroscopic)', fontsize=12)
    ax2.legend(fontsize=10)

    # Panel 3: CMB Lensing
    ax3 = axes[1, 0]
    ax3.loglog(l_lens, l_lens * (l_lens + 1) * Clkk_fid / (2*np.pi), 'b-', lw=2,
               label=r'FW ($c_s^2$=0)')
    ax3.loglog(l_lens, l_lens * (l_lens + 1) * Clkk_cs1 / (2*np.pi), 'r--', lw=2,
               label=r'Quint ($c_s^2$=1)')
    ax3.loglog(l_lens, l_lens * (l_lens + 1) * Nlkk / (2*np.pi), 'gray', ls=':',
               lw=1.5, label='CMB-S4 noise')  # (local)
    ax3.set_xlabel('Multipole l', fontsize=12)
    ax3.set_ylabel(r'$\ell(\ell+1) C_\ell^{\kappa\kappa} / 2\pi$', fontsize=12)
    ax3.set_title('CMB Lensing Power Spectrum', fontsize=12)
    ax3.legend(fontsize=10)
    ax3.set_xlim(100, 500)

    # Panel 4: Fisher ellipse
    ax4 = axes[1, 1]
    # Draw 1-sigma and 2-sigma ellipses
    theta_ell = np.linspace(0, 2*np.pi, 200)

    for name, F, color, ls in [("ISW", F_ISW, 'green', '--'),
                                ("RSD", F_RSD, 'orange', '-.'),
                                ("ISW+RSD", F_ISW + F_RSD, 'purple', ':'),
                                ("COMBINED", F_total, 'blue', '-')]:
        if np.linalg.det(F) > 1e-30:
            C = np.linalg.inv(F)
            eigenvals, eigenvecs = np.linalg.eigh(C)
            # 2-sigma ellipse (chi^2 = 6.18 for 2D 95%)
            for n_sig, alpha in [(1, 0.8), (2, 0.4)]:
                chi2_threshold = n_sig**2
                semi_axes = np.sqrt(chi2_threshold * eigenvals)
                ellipse = eigenvecs @ np.diag(semi_axes) @ np.array([np.cos(theta_ell), np.sin(theta_ell)])
                label_str = f"{name}" if n_sig == 1 else None
                ax4.plot(w0_FW + ellipse[0], cs2_FW + ellipse[1], color=color,
                         ls=ls, lw=2 if n_sig == 1 else 1, alpha=alpha, label=label_str)

    # Mark models
    ax4.plot(w0_FW, cs2_FW, 'b*', ms=15, zorder=10, label='FW fiducial')
    ax4.plot(w0_FW, cs2_quint, 'rs', ms=10, zorder=10, label='Quintessence')
    ax4.plot(w0_LCDM, 0, 'kd', ms=10, zorder=10, label=r'$\Lambda$CDM (cs$^2$ N/A)')
    ax4.set_xlabel(r'$w_0$', fontsize=14)
    ax4.set_ylabel(r'$c_s^2$', fontsize=14)
    ax4.set_title(f'Fisher Constraints (1,2-sigma)\nFW vs LCDM: {sig_FW_vs_LCDM:.1f}$\\sigma$, '
                  f'FW vs Quint: {sig_FW_vs_Quint:.1f}$\\sigma$', fontsize=11)
    ax4.legend(fontsize=8, loc='upper left')
    ax4.axhline(0, color='gray', ls=':', alpha=0.3)
    ax4.axhline(1, color='gray', ls=':', alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plotpath = os.path.join(SCRIPT_DIR, "s69_euclid_joint.png")
    plt.savefig(plotpath, dpi=150, bbox_inches='tight')
    plt.close()
    pr(f"  Saved: {plotpath}")

    pr("\n" + "="*72)
    pr("COMPUTATION COMPLETE")
    pr("="*72)

    log.close()

except Exception as e:
    traceback.print_exc()
    try:
        log.write(f"\nERROR: {traceback.format_exc()}\n")
        log.close()
    except:
        pass
    raise
