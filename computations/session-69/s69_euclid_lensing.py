#!/usr/bin/env python3
"""
s69_euclid_lensing.py -- EUCLID-LENSING-TRACKING-69: CMB Lensing from Tracking DE
====================================================================================
Gate: EUCLID-LENS-69

Computes the tracking-induced modification to CMB lensing convergence power spectrum
C_l^{kk} at l = 100-500. The framework's tracking vacuum (c_s^2_DE = 0) means DE
perturbations track matter via delta_DE = [(1+w)/(1-3w)] * delta_m, modifying the
lensing potential growth at z < 2.

Three models:
  A: LCDM  (w = -1, smooth DE, no DE perturbations)
  B: Framework  (w_0 = -0.918, c_s^2 = 0, tracking DE)
  C: Quintessence  (w_0 = -0.918, c_s^2 = 1, smooth DE)

Key observable:
  Delta_kk(l) = [C_l^{FW} - C_l^{Quint}] / C_l^{LCDM}
  This isolates the tracking effect (c_s^2 = 0 vs 1) at fixed expansion history.

Gate pre-registration:
  PASS if Delta_kk > 0.5% at l = 100-500  (CMB-S4 detectable)
  FAIL if Delta_kk < 0.1%  (below all foreseeable detection)
  INFO if Delta_kk 0.1-0.5%  (marginal)

Physics:
  The Poisson equation relates the lensing potential Phi to matter + DE perturbations:
    k^2 Phi = -4*pi*G * a^2 * [rho_m * delta_m + rho_DE * delta_DE]

  For tracking DE (c_s^2 = 0):
    delta_DE = [(1+w)/(1-3w)] * delta_m  (sub-horizon, adiabatic)
  This enhances the lensing source by factor F(z) = 1 + [Omega_DE(z)/Omega_m(z)] * (1+w)/(1-3w).

  For smooth DE (c_s^2 = 1, quintessence):
    delta_DE ~ 0 on sub-horizon scales.

  The growth equation is also modified: DE clustering sources additional growth.

Input:
  - computations/_shared/canonical_constants.py
  - computations/session-68/s68_isw_tracking_test.npz (for F_tracking cross-check)

Output:
  - computations/session-69/s69_euclid_lensing.npz
  - computations/session-69/s69_euclid_lensing.png

Author: Katie Mack (Cosmic Bridge)
Session: 69, Task EUCLID-LENSING-TRACKING-69 (W4-D)
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

    LOGPATH = os.path.join(SCRIPT_DIR, "s69_euclid_lensing_log.txt")
    log = open(LOGPATH, "w")

    def pr(msg=""):
        print(str(msg))
        log.write(str(msg) + "\n")
        log.flush()

    pr("=" * 78)
    pr("EUCLID-LENSING-TRACKING-69: CMB Lensing from Tracking DE")
    pr("Gate: EUCLID-LENS-69")
    pr("=" * 78)

    # =========================================================================
    # 0. Constants and cosmological parameters
    # =========================================================================
    H0 = H_0_km_s_Mpc   # 67.4 km/s/Mpc
    c = c_light_km_s     # km/s
    Om_m = Omega_m       # 0.315
    Om_r = Omega_r       # 9.15e-5
    Om_DE = Omega_Lambda # 0.685
    sig8 = sigma_8       # 0.811

    # Framework parameters (from S68 Volovik-Mack workshop)
    # w0_FW = -0.918       # Volovik vacuum + effacement  # S72: now imported from canonical_constants
    # w0_LCDM = -1.0       # LCDM  # S72: now imported from canonical_constants
    # wa = 0.0             # w_a locked = 0 (four-fold protection, S68)  # S72: now imported as wa_FW from canonical_constants
    wa = wa_FW  # S72: alias for downstream use (both FW and LCDM have wa=0)
    cs2_tracking = 0.0   # Framework: tracking vacuum  # (local)
    cs2_smooth = 1.0     # Quintessence: smooth DE  # (local)

    # Survey parameters
    f_sky_cmbs4 = 0.4    # CMB-S4 sky fraction  # (local)
    sigma_T_muK_arcmin = 1.0   # CMB-S4 temperature noise  # (local)
    theta_beam_arcmin = 1.0    # CMB-S4 beam FWHM  # (local)
    theta_beam_rad = theta_beam_arcmin * np.pi / (180.0 * 60.0)

    # Multipole range for lensing analysis
    l_min, l_max = 100, 500
    l_arr = np.arange(l_min, l_max + 1)
    N_ell = len(l_arr)

    pr(f"\nParameters:")
    pr(f"  H_0 = {H0} km/s/Mpc")
    pr(f"  Omega_m = {Om_m}, Omega_DE = {Om_DE}")
    pr(f"  sigma_8 = {sig8}")
    pr(f"  w_0(FW) = {w0_FW}, w_0(LCDM) = {w0_LCDM}")
    pr(f"  c_s^2(tracking) = {cs2_tracking}, c_s^2(smooth) = {cs2_smooth}")
    pr(f"  CMB-S4: f_sky = {f_sky_cmbs4}, sigma_T = {sigma_T_muK_arcmin} muK-arcmin")
    pr(f"  Multipole range: l = [{l_min}, {l_max}] ({N_ell} modes)")

    # =========================================================================
    # 1. Cosmological background functions
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 1: BACKGROUND COSMOLOGY")
    pr("=" * 72)

    def E_squared(z, w0=-1.0):
        """(H/H0)^2 for flat w0CDM (w_a = 0)."""
        zp1 = 1.0 + z
        de_factor = zp1**(3 * (1 + w0))
        return Om_r * zp1**4 + Om_m * zp1**3 + Om_DE * de_factor

    def H_func(z, w0=-1.0):
        """Hubble parameter in km/s/Mpc."""
        return H0 * np.sqrt(E_squared(z, w0))

    def chi_comoving(z, w0=-1.0):
        """Comoving distance in Mpc."""
        result, _ = quad(lambda zp: c / H_func(zp, w0), 0, z, limit=200)
        return result

    def Omega_m_z(z, w0=-1.0):
        """Matter density parameter at redshift z."""
        return Om_m * (1 + z)**3 / E_squared(z, w0)

    def Omega_DE_z(z, w0=-1.0):
        """DE density parameter at redshift z."""
        zp1 = 1.0 + z
        de_factor = zp1**(3 * (1 + w0))
        return Om_DE * de_factor / E_squared(z, w0)

    # Tracking enhancement factor
    def F_track(z, w0):
        """Tracking enhancement factor for Poisson equation.
        F = 1 + [Omega_DE(z) / Omega_m(z)] * (1+w) / (1-3w)

        This multiplies the matter source in the Poisson equation when DE
        perturbations track matter (c_s^2 = 0).
        """
        if abs(1 - 3*w0) < 1e-10:
            return 1.0
        ratio = (1 + w0) / (1 - 3*w0)
        return 1.0 + (Omega_DE_z(z, w0) / Omega_m_z(z, w0)) * ratio

    # Report tracking factor at key redshifts
    pr("\n  Tracking enhancement factor F(z) [c_s^2 = 0, w_0 = -0.918]:")
    for z_test in [0.0, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0]:
        F_val = F_track(z_test, w0_FW)
        pr(f"    F(z={z_test:.1f}) = {F_val:.6f}")

    # Cross-check against S68 ISW data
    try:
        isw_data = np.load(os.path.join(SCRIPT_DIR, "s68_isw_tracking_test.npz"))
        F_s68 = isw_data['F_tracking']
        z_s68 = isw_data['z_arr']
        # Compare at z=0.5
        idx_05 = np.argmin(np.abs(z_s68 - 0.5))
        pr(f"\n  Cross-check vs S68: F(z=0.5)")
        pr(f"    This script: {F_track(0.5, w0_FW):.6f}")
        pr(f"    S68 ISW:     {F_s68[idx_05]:.6f}")
        pr(f"    Agreement:   {abs(F_track(0.5, w0_FW) - F_s68[idx_05]) / F_s68[idx_05] * 100:.4f}%")
    except Exception as e:
        pr(f"  [Warning: S68 cross-check skipped: {e}]")

    # Comoving distances
    chi_star = chi_comoving(1100.0, w0_LCDM)
    chi_star_FW = chi_comoving(1100.0, w0_FW)
    pr(f"\n  chi(z*=1100, LCDM) = {chi_star:.0f} Mpc")
    pr(f"  chi(z*=1100, FW)   = {chi_star_FW:.0f} Mpc")

    # =========================================================================
    # 2. Growth factor computation
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 2: GROWTH FACTORS")
    pr("=" * 72)

    def compute_growth(z_out, w0=-1.0, tracking=False, N_a=10000):
        """Compute linear growth factor D(z) and growth rate f(z) via ODE.

        Growth ODE in scale factor a:
          D'' + [3/a + E'/E] D' - (3/2) * Q(z) / (a^3 * E^2) * D = 0
        where:
          Q = Omega_m  for LCDM and smooth DE (c_s^2 = 1)
          Q = Omega_m + Omega_DE * (1+w)/(1-3w)  for tracking DE (c_s^2 = 0)

        The tracking term modifies the effective gravitational source.
        """
        a_start = 1e-4  # (local)
        a_end = 1.0  # (local)
        a_arr = np.linspace(a_start, a_end, N_a)

        def rhs(a, y):
            D, Dp = y
            z = 1.0/a - 1.0
            E2 = E_squared(z, w0)

            # dE^2/da via finite difference
            eps = 1e-6
            e2p = E_squared(1.0/(a + eps) - 1.0, w0)
            e2m = E_squared(1.0/(a - eps) - 1.0, w0)
            dE2 = (e2p - e2m) / (2 * eps)

            coeff1 = 3.0/a + 0.5 * dE2 / E2

            # Gravitational source term
            source = 1.5 * Om_m / (a**3 * E2)

            if tracking and abs(1 - 3*w0) > 1e-10:
                # Additional source from DE clustering
                zp1 = 1.0/a
                de_factor = zp1**(3 * (1 + w0))
                Omega_DE_a = Om_DE * de_factor / E2
                ratio_de = (1 + w0) / (1 - 3*w0)
                source += 1.5 * Omega_DE_a * ratio_de / (a**3)

            return [Dp, -coeff1 * Dp + source * D]

        y0 = [a_start, 1.0]  # D ~ a, dD/da = 1 in matter domination
        sol = solve_ivp(rhs, [a_start, a_end], y0, t_eval=a_arr, method='RK45',
                        rtol=1e-10, atol=1e-13)

        D_arr = sol.y[0]
        Dp_arr = sol.y[1]  # dD/da
        D0 = D_arr[-1]
        D_arr /= D0
        Dp_arr /= D0

        # f = a/D * dD/da = dln(D)/dln(a)
        f_arr = sol.t / D_arr * Dp_arr

        z_grid = 1.0/sol.t - 1.0
        D_interp = interp1d(z_grid[::-1], D_arr[::-1], kind='cubic', fill_value='extrapolate')
        f_interp = interp1d(z_grid[::-1], f_arr[::-1], kind='cubic', fill_value='extrapolate')

        return D_interp(z_out), f_interp(z_out)

    # Redshift grid for lensing integration (z=0 to z=5)
    z_lens = np.linspace(0.01, 5.0, 300)

    pr("\n  Computing growth factors for three models...")

    # Model A: LCDM (w=-1, no tracking)
    D_A, f_A = compute_growth(z_lens, w0=w0_LCDM, tracking=False)

    # Model B: Framework (w_0=-0.918, tracking c_s^2=0)
    D_B, f_B = compute_growth(z_lens, w0=w0_FW, tracking=True)

    # Model C: Quintessence (w_0=-0.918, smooth c_s^2=1)
    D_C, f_C = compute_growth(z_lens, w0=w0_FW, tracking=False)

    pr(f"  D(z=0): LCDM={D_A[0]:.6f}, FW={D_B[0]:.6f}, Quint={D_C[0]:.6f}")
    pr(f"  D(z=1): LCDM={D_A[np.argmin(np.abs(z_lens-1))]:.6f}, "
       f"FW={D_B[np.argmin(np.abs(z_lens-1))]:.6f}, "
       f"Quint={D_C[np.argmin(np.abs(z_lens-1))]:.6f}")
    pr(f"  D(z=2): LCDM={D_A[np.argmin(np.abs(z_lens-2))]:.6f}, "
       f"FW={D_B[np.argmin(np.abs(z_lens-2))]:.6f}, "
       f"Quint={D_C[np.argmin(np.abs(z_lens-2))]:.6f}")

    # Key diagnostic: ratio D_B/D_C - 1 = pure effect of tracking on growth
    D_ratio_BC = D_B / D_C - 1
    pr(f"\n  D_FW/D_Quint - 1 at key z:")
    for z_test in [0.0, 0.3, 0.5, 1.0, 2.0, 3.0]:
        idx = np.argmin(np.abs(z_lens - z_test))
        pr(f"    z={z_test:.1f}: {D_ratio_BC[idx]*100:.4f}%")

    # =========================================================================
    # 3. Eisenstein-Hu transfer function and P(k)
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 3: MATTER POWER SPECTRUM")
    pr("=" * 72)

    h_val = H0 / 100.0  # 0.674

    def transfer_EH(k_Mpc):
        """Eisenstein-Hu (1998) no-wiggle transfer function T(k).
        k in Mpc^{-1}. Returns T(k) normalized to T(0)=1.
        ApJ 496, 605, Eq. 29-31.
        """
        Om_mh2 = Om_m * h_val**2
        Om_bh2 = Omega_b * h_val**2
        f_b = Omega_b / Om_m
        theta_cmb = T_CMB / 2.7

        # Sound horizon
        s = 44.5 * np.log(9.83 / Om_mh2) / np.sqrt(1 + 10 * Om_bh2**0.75)
        # alpha_gamma
        alpha_gamma = (1 - 0.328 * np.log(431 * Om_mh2) * f_b
                       + 0.38 * np.log(22.3 * Om_mh2) * f_b**2)
        # Effective shape parameter
        Gamma_eff = Om_m * h_val * (alpha_gamma +
                                     (1 - alpha_gamma) / (1 + (0.43 * k_Mpc * s)**4))
        # q
        q = k_Mpc * theta_cmb**2 / Gamma_eff
        # Transfer function (Eq. 29)
        L = np.log(2 * np.e + 1.8 * q)
        C_val = 14.2 + 731.0 / (1 + 62.5 * q)
        T0 = L / (L + C_val * q**2)
        return T0

    # Primordial spectral index
    n_s_val = 0.965  # (local)
    k_piv = 0.05  # Mpc^{-1} (Planck pivot)  # (local)

    def P_shape(k):
        """Unnormalized linear power spectrum shape: k^{n_s} * T^2(k)."""
        Tk = transfer_EH(k)
        return (k / k_piv)**n_s_val * Tk**2

    # Normalize to sigma_8 = 0.811
    R8 = 8.0 / h_val  # ~ 11.87 Mpc

    def W_tophat(kR):
        """Top-hat window function in Fourier space."""
        if kR < 1e-6:
            return 1.0
        return 3.0 * (np.sin(kR) - kR * np.cos(kR)) / kR**3

    k_norm = np.logspace(-4, 1.5, 10000)
    integrand_sig8 = np.zeros_like(k_norm)
    for j, k in enumerate(k_norm):
        W = W_tophat(k * R8)
        integrand_sig8[j] = k**2 * P_shape(k) * W**2

    sigma8_unnorm_sq = np.trapezoid(integrand_sig8, k_norm) / (2 * np.pi**2)
    P0 = sig8**2 / sigma8_unnorm_sq  # Normalization factor in Mpc^3
    pr(f"\n  P(k) normalization: P_0 = {P0:.4e} Mpc^3")

    # Verification
    P_01 = P0 * P_shape(0.1)
    P_001 = P0 * P_shape(0.01)
    pr(f"  P(k=0.1, z=0) = {P_01:.0f} Mpc^3 (expect ~5000)")
    pr(f"  P(k=0.01, z=0) = {P_001:.0f} Mpc^3 (expect ~10000)")

    def P_lin(k, D_z):
        """Linear matter power spectrum P(k, z) = P_0 * shape(k) * D^2(z) in Mpc^3."""
        return P0 * P_shape(k) * D_z**2

    # =========================================================================
    # 4. CMB lensing convergence power spectrum C_l^{kk}
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 4: CMB LENSING CONVERGENCE C_l^{kk}")
    pr("=" * 72)

    pr("""
  Theory:
  The CMB lensing convergence kappa is an integral of the lensing potential
  along the line of sight:

    kappa(n) = -1/2 * integral_0^{chi_*} dchi * chi(chi_*-chi)/chi_* * nabla^2_perp Phi

  In the Limber approximation, the convergence power spectrum is:

    C_l^{kk} = integral_0^{chi_*} dchi [W_kappa(chi)]^2 / chi^2 * P_Phi(l/chi, z)

  where the lensing kernel is:
    W_kappa(chi) = (3/2) * Omega_m * (H_0/c)^2 * chi * (chi_*-chi)/chi_* * (1+z)

  And P_Phi = [3/2 * Omega_m * H_0^2 / (c^2 * k^2)]^2 * (1+z)^2 * P_delta(k, z)

  Substituting: the C_l^{kk} integral in terms of P_delta becomes:

    C_l^{kk} = integral dz * [W(z)]^2 * P_delta(l/chi, z) * H(z) / (c * chi^2)

  For tracking DE (c_s^2 = 0):
    - D(z) is enhanced by DE clustering in the growth ODE
    - The Poisson equation source is enhanced by F(z)
    - Both effects multiply: Phi_tracking ~ D_B(z) * F(z) / (1+z)
    - The lensing power gets an additional factor F^2(z) beyond growth

  For smooth DE (c_s^2 = 1):
    - Modified expansion history changes D(z) relative to LCDM
    - But no Poisson enhancement: F = 1
""")

    def compute_Clkk(l_arr, w0, tracking=False):
        """Compute C_l^{kk} using Limber approximation.

        For tracking DE:
          1. Growth factor D(z) includes DE clustering source
          2. Lensing kernel picks up additional F(z) factor from Poisson enhancement
        """
        # Comoving distances for this cosmology
        chi_arr = np.array([chi_comoving(z, w0) for z in z_lens])
        chi_s = chi_comoving(1100.0, w0)

        # Growth factors
        D_arr, f_arr_unused = compute_growth(z_lens, w0=w0, tracking=tracking)

        # Hubble parameter
        H_arr = np.array([H_func(z, w0) for z in z_lens])

        # Lensing kernel: W(chi) = (3/2) * Om_m * (H_0/c)^2 * chi * (chi_s-chi)/chi_s * (1+z)
        W_kappa = 1.5 * Om_m * (H0/c)**2 * chi_arr * (chi_s - chi_arr) / chi_s * (1 + z_lens)

        # For tracking DE: the Poisson equation has additional source F(z)
        # This modifies the lensing potential: Phi ~ F(z) * D(z) * delta_m / (1+z)
        # The convergence depends on nabla^2 Phi, so C_l^{kk} scales as F^2
        # But growth already absorbed the tracking source into D, so we apply
        # F(z) to the lensing kernel itself (one power of F, because the growth
        # ODE already includes one power through the modified source term).
        #
        # More precisely:
        #   Standard Poisson: k^2 Phi = -4pi G a^2 rho_m delta_m
        #   Tracking Poisson: k^2 Phi = -4pi G a^2 [rho_m + rho_DE*(1+w)/(1-3w)] delta_m
        #                             = -4pi G a^2 rho_m F(z) delta_m
        #
        # The growth equation in tracking already includes the modified source
        # (1.5 * [Om_m + Om_DE*(1+w)/(1-3w)] / (a^3 E^2)), producing D_track(z).
        #
        # The lensing potential is Phi ~ F(z) * delta_m / k^2 (Poisson).
        # But delta_m ~ D(z), and D_track already grew faster due to F.
        # The explicit F in the Poisson equation is a SEPARATE effect from the
        # growth enhancement.
        #
        # To be precise:
        #   C_l^{kk}(tracking) / C_l^{kk}(smooth) =
        #     [D_track(z) * F(z)]^2 / [D_smooth(z) * 1]^2
        #   where the F comes from the Poisson equation enhancement.
        #
        # In the growth ODE, the tracking source is already included, so:
        #   D_track > D_smooth (growth is enhanced)
        # And additionally, the lensing potential is enhanced by F(z).
        #
        # We must apply F(z) to the lensing kernel to capture the Poisson effect.
        if tracking:
            F_arr = np.array([F_track(z, w0) for z in z_lens])
            W_kappa = W_kappa * F_arr

        Cl = np.zeros(len(l_arr))
        for i, l in enumerate(l_arr):
            k_arr = (l + 0.5) / chi_arr

            # P_delta(k, z) = P_0 * shape(k) * D^2(z)
            P_k = np.array([P_lin(k_arr[j], D_arr[j]) for j in range(len(z_lens))])

            # Limber approximation in comoving distance chi:
            #   C_l = integral_0^{chi_*} dchi W^2(chi) P(l/chi, z) / chi^2
            #
            # Converting to z-integration: dchi = c/H(z) dz
            #   C_l = integral dz * (c/H) * W^2 * P / chi^2
            integrand = W_kappa**2 * P_k * c / (H_arr * chi_arr**2)
            Cl[i] = np.trapezoid(integrand, z_lens)

        return Cl

    pr("  Computing C_l^{kk} for three models...")

    # Model A: LCDM
    pr("    Model A: LCDM (w=-1, smooth)...")
    Clkk_A = compute_Clkk(l_arr, w0=w0_LCDM, tracking=False)

    # Model B: Framework (w_0=-0.918, tracking c_s^2=0)
    pr("    Model B: Framework (w_0=-0.918, c_s^2=0, tracking)...")
    Clkk_B = compute_Clkk(l_arr, w0=w0_FW, tracking=True)

    # Model C: Quintessence (w_0=-0.918, smooth c_s^2=1)
    pr("    Model C: Quintessence (w_0=-0.918, c_s^2=1, smooth)...")
    Clkk_C = compute_Clkk(l_arr, w0=w0_FW, tracking=False)

    pr(f"\n  Power spectrum values at selected multipoles:")
    pr(f"  {'l':>5s} | {'C_l^kk(LCDM)':>14s} | {'C_l^kk(FW)':>14s} | {'C_l^kk(Quint)':>14s}")
    pr(f"  {'-'*5}-+-{'-'*14}-+-{'-'*14}-+-{'-'*14}")
    for l_test in [100, 150, 200, 250, 300, 400, 500]:
        idx = l_test - l_min
        if 0 <= idx < N_ell:
            pr(f"  {l_test:5d} | {Clkk_A[idx]:14.6e} | {Clkk_B[idx]:14.6e} | {Clkk_C[idx]:14.6e}")

    # =========================================================================
    # 5. Key observable: Delta_kk
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 5: TRACKING MODIFICATION Delta_kk")
    pr("=" * 72)

    # Delta_kk = (C_l^FW - C_l^Quint) / C_l^LCDM
    # This isolates the c_s^2 effect at fixed expansion history
    Delta_kk = (Clkk_B - Clkk_C) / Clkk_A

    # Also compute FW vs LCDM ratio
    ratio_BA = Clkk_B / Clkk_A
    ratio_CA = Clkk_C / Clkk_A

    pr(f"\n  Delta_kk = (C_FW - C_Quint) / C_LCDM at selected multipoles:")
    pr(f"  {'l':>5s} | {'Delta_kk':>12s} | {'%':>8s} | {'FW/LCDM':>10s} | {'Quint/LCDM':>10s}")
    pr(f"  {'-'*5}-+-{'-'*12}-+-{'-'*8}-+-{'-'*10}-+-{'-'*10}")
    for l_test in [100, 150, 200, 250, 300, 350, 400, 450, 500]:
        idx = l_test - l_min
        if 0 <= idx < N_ell:
            pr(f"  {l_test:5d} | {Delta_kk[idx]:12.6f} | {Delta_kk[idx]*100:8.4f} | "
               f"{ratio_BA[idx]:10.6f} | {ratio_CA[idx]:10.6f}")

    # Statistics over the full range
    mean_Delta = np.mean(Delta_kk)
    median_Delta = np.median(Delta_kk)
    min_Delta = np.min(Delta_kk)
    max_Delta = np.max(Delta_kk)

    pr(f"\n  Statistics (l = {l_min}-{l_max}):")
    pr(f"    Mean   Delta_kk = {mean_Delta:.6f} = {mean_Delta*100:.4f}%")
    pr(f"    Median Delta_kk = {median_Delta:.6f} = {median_Delta*100:.4f}%")
    pr(f"    Min    Delta_kk = {min_Delta:.6f} = {min_Delta*100:.4f}%")
    pr(f"    Max    Delta_kk = {max_Delta:.6f} = {max_Delta*100:.4f}%")

    mean_ratio_BA = np.mean(ratio_BA)
    mean_ratio_CA = np.mean(ratio_CA)
    pr(f"\n    Mean FW/LCDM     = {mean_ratio_BA:.6f} ({(mean_ratio_BA-1)*100:.4f}%)")
    pr(f"    Mean Quint/LCDM  = {mean_ratio_CA:.6f} ({(mean_ratio_CA-1)*100:.4f}%)")

    # Decomposition: growth effect vs Poisson effect
    # Re-compute FW without Poisson F to isolate growth-only
    pr("\n  Decomposition: growth-only vs growth+Poisson")
    Clkk_B_growth_only = compute_Clkk(l_arr, w0=w0_FW, tracking=False)
    # But with tracking growth (need separate computation)
    # Actually, compute_Clkk with tracking=False uses smooth growth.
    # To isolate: compute with tracking growth but no F in lensing kernel.
    # We'll re-compute inline:

    D_B_track, _ = compute_growth(z_lens, w0=w0_FW, tracking=True)
    D_C_smooth, _ = compute_growth(z_lens, w0=w0_FW, tracking=False)
    growth_enhancement = np.mean(D_B_track / D_C_smooth)
    pr(f"    Mean D_track/D_smooth at z ~ 0.5-2 (lensing kernel peak):")
    for z_test in [0.5, 1.0, 1.5, 2.0]:
        idx = np.argmin(np.abs(z_lens - z_test))
        pr(f"      z={z_test}: D_track/D_smooth = {D_B_track[idx]/D_C_smooth[idx]:.6f} "
           f"({(D_B_track[idx]/D_C_smooth[idx]-1)*100:.4f}%)")

    # =========================================================================
    # 6. CMB-S4 noise and SNR
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 6: CMB-S4 NOISE AND SNR")
    pr("=" * 72)

    # CMB-S4 lensing reconstruction noise N_l^{kk}
    # From CMB-S4 Science Book (1610.02743), iterative EB delensing:
    # N_l^{kk} ~ 1e-8 at l ~ 200, scaling as l^2
    # More precisely, using minimum-variance quadratic estimator:
    #   N_l^{kk} = l^2 * sigma_N^2_kappa / (2*pi)
    # For CMB-S4 with 1 muK-arcmin noise and 1' beam:
    #   - At l ~ 200: N ~ 1e-8 (matching Fig. 16 of 1610.02743)
    #   - Approximate: N_l = 1e-8 * (l/200)^2

    Nlkk = 1e-8 * (l_arr / 200.0)**2

    pr(f"\n  Lensing noise N_l^{{kk}} (CMB-S4 iterative delensing):")
    for l_test in [100, 200, 300, 400, 500]:
        idx = l_test - l_min
        if 0 <= idx < N_ell:
            snr_per_l = Clkk_A[idx] / Nlkk[idx]
            pr(f"    N_{{l={l_test}}} = {Nlkk[idx]:.3e}, "
               f"C_l/N_l = {snr_per_l:.2f}")

    # Per-multipole variance: sigma^2(C_l) = 2/(f_sky*(2l+1)) * (C_l + N_l)^2
    sigma_Clkk = np.sqrt(2.0 / (f_sky_cmbs4 * (2 * l_arr + 1))) * (Clkk_A + Nlkk)

    # Fractional error per multipole
    frac_err = sigma_Clkk / Clkk_A

    pr(f"\n  Per-multipole fractional error sigma(C_l)/C_l:")
    for l_test in [100, 200, 300, 400, 500]:
        idx = l_test - l_min
        if 0 <= idx < N_ell:
            pr(f"    l = {l_test}: {frac_err[idx]*100:.2f}%")

    # Signal-to-noise for detecting Delta_kk
    # The signal at each l is: Delta C_l = Clkk_B - Clkk_C
    # The noise is sigma(C_l) computed from the fiducial (LCDM)
    Delta_Cl = Clkk_B - Clkk_C

    # Per-multipole SNR
    snr_per_l = Delta_Cl / sigma_Clkk

    # Cumulative SNR
    snr_squared_cumul = np.cumsum(snr_per_l**2)
    snr_total = np.sqrt(np.sum(snr_per_l**2))

    pr(f"\n  SNR for detecting tracking signal (FW - Quint):")
    pr(f"    Per-multipole peak SNR: {np.max(np.abs(snr_per_l)):.4f} at l = {l_arr[np.argmax(np.abs(snr_per_l))]}")
    pr(f"    Cumulative SNR(l={l_min}-{l_max}): {snr_total:.4f}")

    # Also compute SNR for FW vs LCDM
    Delta_Cl_BA = Clkk_B - Clkk_A
    snr_per_l_BA = Delta_Cl_BA / sigma_Clkk
    snr_total_BA = np.sqrt(np.sum(snr_per_l_BA**2))
    pr(f"    Cumulative SNR(FW vs LCDM): {snr_total_BA:.4f}")

    # Binned SNR (for more realistic assessment)
    n_bins = 8  # (local)
    l_bin_edges = np.linspace(l_min, l_max, n_bins + 1)
    pr(f"\n  Binned SNR (FW-Quint, {n_bins} bins):")
    pr(f"  {'l_min':>6s}-{'l_max':>5s} | {'Mean Delta_kk':>14s} | {'SNR_bin':>8s}")
    pr(f"  {'-'*6}-{'-'*5}-+-{'-'*14}-+-{'-'*8}")
    snr_binned_sq = 0.0  # (local)
    for b in range(n_bins):
        mask = (l_arr >= l_bin_edges[b]) & (l_arr < l_bin_edges[b+1])
        if np.any(mask):
            bin_snr = np.sqrt(np.sum(snr_per_l[mask]**2))
            bin_delta = np.mean(Delta_kk[mask])
            snr_binned_sq += np.sum(snr_per_l[mask]**2)
            pr(f"  {l_bin_edges[b]:6.0f}-{l_bin_edges[b+1]:5.0f} | {bin_delta:14.6f} | {bin_snr:8.4f}")
    pr(f"  Total binned SNR: {np.sqrt(snr_binned_sq):.4f}")

    # =========================================================================
    # 7. Gate verdict
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 7: GATE VERDICT")
    pr("=" * 72)

    mean_Delta_pct = abs(mean_Delta) * 100
    pr(f"\n  |Mean Delta_kk| = {mean_Delta_pct:.4f}%")
    pr(f"  Gate threshold: PASS > 0.5%, FAIL < 0.1%, INFO 0.1-0.5%")

    if mean_Delta_pct > 0.5:
        verdict = "PASS"
        reason = f"Delta_kk = {mean_Delta_pct:.2f}% > 0.5% (CMB-S4 detectable)"
    elif mean_Delta_pct < 0.1:
        verdict = "FAIL"
        reason = f"Delta_kk = {mean_Delta_pct:.4f}% < 0.1% (below detection)"
    else:
        verdict = "INFO"
        reason = f"Delta_kk = {mean_Delta_pct:.4f}% in [0.1%, 0.5%] (marginal)"

    pr(f"\n  =================================================")
    pr(f"  Gate EUCLID-LENS-69: {verdict}")
    pr(f"  {reason}")
    pr(f"  Cumulative SNR (FW vs Quint, l=100-500): {snr_total:.4f}")
    pr(f"  Cumulative SNR (FW vs LCDM, l=100-500): {snr_total_BA:.4f}")
    pr(f"  =================================================")

    # =========================================================================
    # 8. Save data
    # =========================================================================
    pr("\n" + "=" * 72)
    pr("SECTION 8: OUTPUT")
    pr("=" * 72)

    outpath = os.path.join(SCRIPT_DIR, "s69_euclid_lensing.npz")
    np.savez(outpath,
             # Multipoles
             l_arr=l_arr,
             # Lensing power spectra
             Clkk_LCDM=Clkk_A,
             Clkk_FW=Clkk_B,
             Clkk_Quint=Clkk_C,
             # Key observable
             Delta_kk=Delta_kk,
             ratio_FW_LCDM=ratio_BA,
             ratio_Quint_LCDM=ratio_CA,
             # SNR
             snr_per_l=snr_per_l,
             snr_total=snr_total,
             snr_per_l_BA=snr_per_l_BA,
             snr_total_BA=snr_total_BA,
             # Noise
             Nlkk=Nlkk,
             sigma_Clkk=sigma_Clkk,
             # Statistics
             mean_Delta_kk=mean_Delta,
             median_Delta_kk=median_Delta,
             min_Delta_kk=min_Delta,
             max_Delta_kk=max_Delta,
             # Parameters
             w0_FW=w0_FW,
             w0_LCDM=w0_LCDM,
             sig8=sig8,
             Om_m=Om_m,
             Om_DE=Om_DE,
             f_sky=f_sky_cmbs4,
             # Gate verdict
             verdict=verdict,
             mean_Delta_pct=mean_Delta_pct,
             )
    pr(f"  Data saved: {outpath}")

    # =========================================================================
    # 9. Plot
    # =========================================================================
    pr("\nGenerating plot...")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("EUCLID-LENSING-TRACKING-69: CMB Lensing from Tracking DE\n"
                 f"Gate: EUCLID-LENS-69 — {verdict}", fontsize=14, fontweight='bold')

    # Panel 1: C_l^{kk} for three models
    ax1 = axes[0, 0]
    ax1.semilogy(l_arr, l_arr * (l_arr + 1) * Clkk_A / (2*np.pi), 'k-', lw=2, label=r'$\Lambda$CDM ($w=-1$)')
    ax1.semilogy(l_arr, l_arr * (l_arr + 1) * Clkk_B / (2*np.pi), 'r-', lw=2, label=r'FW ($w_0=-0.918$, $c_s^2=0$)')
    ax1.semilogy(l_arr, l_arr * (l_arr + 1) * Clkk_C / (2*np.pi), 'b--', lw=2, label=r'Quint ($w_0=-0.918$, $c_s^2=1$)')
    ax1.set_xlabel(r'Multipole $\ell$', fontsize=12)
    ax1.set_ylabel(r'$\ell(\ell+1) C_\ell^{\kappa\kappa} / 2\pi$', fontsize=12)
    ax1.set_title('CMB Lensing Convergence Power Spectrum', fontsize=11)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Delta_kk = (FW - Quint) / LCDM
    ax2 = axes[0, 1]
    ax2.plot(l_arr, Delta_kk * 100, 'r-', lw=2, label=r'$\Delta_{\kappa\kappa}$ (FW$-$Quint)/LCDM')
    ax2.axhline(0.5, color='green', ls=':', lw=1, label='PASS threshold (0.5%)')
    ax2.axhline(0.1, color='orange', ls=':', lw=1, label='FAIL threshold (0.1%)')
    ax2.axhline(np.mean(Delta_kk) * 100, color='gray', ls='--', lw=1,
                label=f'Mean = {np.mean(Delta_kk)*100:.3f}%')
    ax2.set_xlabel(r'Multipole $\ell$', fontsize=12)
    ax2.set_ylabel(r'$\Delta_{\kappa\kappa}$ (%)', fontsize=12)
    ax2.set_title('Tracking Modification to CMB Lensing', fontsize=11)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    # Panel 3: Ratios FW/LCDM and Quint/LCDM
    ax3 = axes[1, 0]
    ax3.plot(l_arr, (ratio_BA - 1) * 100, 'r-', lw=2, label='FW/LCDM $-$ 1')
    ax3.plot(l_arr, (ratio_CA - 1) * 100, 'b--', lw=2, label='Quint/LCDM $-$ 1')
    ax3.axhline(0, color='k', ls='-', lw=0.5)
    ax3.set_xlabel(r'Multipole $\ell$', fontsize=12)
    ax3.set_ylabel(r'$C_\ell / C_\ell^{\Lambda\mathrm{CDM}} - 1$ (%)', fontsize=12)
    ax3.set_title('Fractional Deviation from LCDM', fontsize=11)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)

    # Panel 4: Per-multipole SNR and cumulative
    ax4 = axes[1, 1]
    ax4.plot(l_arr, snr_per_l, 'r-', lw=1, alpha=0.5, label=r'Per-$\ell$ SNR (FW$-$Quint)')
    ax4_twin = ax4.twinx()
    ax4_twin.plot(l_arr, np.sqrt(snr_squared_cumul), 'k-', lw=2,
                  label=f'Cumulative SNR = {snr_total:.3f}')
    ax4.set_xlabel(r'Multipole $\ell$', fontsize=12)
    ax4.set_ylabel(r'Per-$\ell$ SNR', fontsize=12, color='r')
    ax4_twin.set_ylabel('Cumulative SNR', fontsize=12)
    ax4.set_title('Signal-to-Noise for CMB-S4', fontsize=11)

    lines1, labels1 = ax4.get_legend_handles_labels()
    lines2, labels2 = ax4_twin.get_legend_handles_labels()
    ax4.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper left')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plotpath = os.path.join(SCRIPT_DIR, "s69_euclid_lensing.png")
    plt.savefig(plotpath, dpi=150, bbox_inches='tight')
    plt.close()
    pr(f"  Plot saved: {plotpath}")

    pr("\n" + "=" * 72)
    pr("COMPUTATION COMPLETE")
    pr("=" * 72)

    log.close()

except Exception as e:
    traceback.print_exc()
    try:
        log.close()
    except:
        pass
    sys.exit(1)
