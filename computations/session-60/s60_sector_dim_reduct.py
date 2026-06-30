#!/usr/bin/env python3
"""
SECTOR-DIM-REDUCT-60: Sector-Resolved Dimensional Reduction for Screening
=========================================================================
Session 60, Wave 4, Task W4-1
Agent: baptista-spacetime-analyst

Physics
-------
The S59 timescape calculation found delta_G/G = -0.526, delta_alpha/alpha = 0.033,
giving a naive screening ratio of |delta_N/N| / |delta_alpha/alpha| ~ 8.0.
The observational constraint requires screening ratio > 10^4:
  - Lapse can vary (drives w_a), but alpha must NOT vary (ALPHA-ENV-43: < 10^{-6}).

The question: does the Riemannian submersion structure from Paper 13 (Baptista 2021,
eq 3.4) provide additional screening? Specifically:

  1. G_eff comes from fiber-integrating the Einstein-Hilbert term over SU(3).
     In spectral action language: 1/(16*pi*G_eff) = a_2 * M_KK^2 / (4*pi).
     The a_2 coefficient is a SUM over all Peter-Weyl sectors weighted by d^2.

  2. alpha comes from the gauge coupling: g'^2 = 12/lambda_1 (Paper 13 eq 5.21).
     This is a POINT EVALUATION on the metric lambda_1 along the u(1) direction.
     It does NOT involve a fiber integral.

  3. The screening ratio = (delta_G_eff/G_eff) / (delta_alpha/alpha).
     If G_eff and alpha have different tau-dependence, screening may occur.

  4. The (M_KK/M_Pl)^2 suppression: determines whether this enters the G channel
     (through the fiber volume in the spectral action) or the alpha channel (it does not).

Gate: SECTOR-DIM-REDUCT-60
  PASS: screening ratio > 10^4
  FAIL: screening ratio < 100
  INFO: screening ratio in [100, 10^4]
"""

import sys
import os
import numpy as np

BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASEDIR)

LOGPATH = os.path.join(BASEDIR, "s60_sector_dim_reduct_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    log.write(str(msg) + "\n")
    log.flush()

try:
    from canonical_constants import (
        tau_fold, a2_fold, a0_fold, a4_fold,
        M_KK_gravity, M_KK_kerner, M_KK,
        M_Pl_reduced, M_Pl_unreduced,
        clock_coeff,
        Vol_SU3_Haar,
        PI,
        alpha_em_MZ_inv,
        sin2_thetaW_MSbar,
        g_SU2_fold, g_U1_fold,
        dS_fold, d2S_fold, S_fold,
    )
    pr("Canonical constants loaded.")

    # Load S59 data
    s59_ts = np.load(os.path.join(BASEDIR, "s59_timescape_wa.npz"), allow_pickle=True)
    s59_sn = np.load(os.path.join(BASEDIR, "s59_spinor_norm.npz"), allow_pickle=True)
    pr("Input data loaded.\n")

    out = {}

    # ================================================================
    #  Step 1: Riemannian Submersion Structure (Paper 13, eq 3.4)
    # ================================================================
    pr("=" * 70)
    pr("Step 1: O'Neill Decomposition of the Scalar Curvature")
    pr("=" * 70)
    pr()
    pr("Paper 13 eq 3.4: R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 delta N")
    pr("After fiber-integration (eq 3.41):")
    pr("  L_M = (1/2k_P)[R_M * f_phi - (1/4)*B_phi*|F|^2 - C_phi*|d_A phi|^2")
    pr("         - D_phi*|d|phi|^2|^2 - V(|phi|^2) - 2*Lambda_M*f_phi] * Vol(K,beta_0)")
    pr()
    pr("Key structure:")
    pr("  * G_eff^{-1} ~ f_phi * Vol(K, beta_0)  (fiber-integrated coefficient of R_M)")
    pr("  * alpha ~ 1/lambda_1  (point evaluation on fiber metric, no integral)")
    pr()

    # The volume form and its tau-dependence
    # Paper 13 eq 2.37: f_phi = lambda^4 * (1 - |phi|^2) * sqrt(1 - 4|phi|^2)
    # In the project's parametrization, tau = |phi|^2, so:
    #   f(tau) = lambda^4 * (1 - tau) * sqrt(1 - 4*tau)
    # This is valid for tau < 1/4 = 0.25.

    tau = tau_fold  # 0.19

    def f_phi(t):
        """Volume form ratio (Paper 13 eq 2.37), normalized by lambda^4."""
        return (1.0 - t) * np.sqrt(1.0 - 4.0 * t)

    def df_phi(t):
        """d(f_phi)/d(tau)."""
        # f = (1-t)*sqrt(1-4t)
        # f' = -sqrt(1-4t) + (1-t)*(-4)/(2*sqrt(1-4t))
        #    = -sqrt(1-4t) - 2*(1-t)/sqrt(1-4t)
        #    = [-( 1-4t) - 2*(1-t)] / sqrt(1-4t)
        #    = [-1+4t - 2+2t] / sqrt(1-4t)
        #    = [6t - 3] / sqrt(1-4t)
        #    = 3*(2t - 1) / sqrt(1-4t)
        return 3.0 * (2.0 * t - 1.0) / np.sqrt(1.0 - 4.0 * t)

    f_val = f_phi(tau)
    df_val = df_phi(tau)
    frac_df = df_val / f_val  # (1/f)(df/dtau)

    pr(f"  tau_fold = {tau}")
    pr(f"  f_phi(tau) = {f_val:.6f}")
    pr(f"  df_phi/dtau = {df_val:.6f}")
    pr(f"  (1/f)(df/dtau) = {frac_df:.6f}")
    pr()

    out["tau_fold"] = np.array(tau)
    out["f_phi"] = np.array(f_val)
    out["df_phi_dtau"] = np.array(df_val)
    out["frac_df_phi"] = np.array(frac_df)

    # ================================================================
    #  Step 2: How delta_tau enters G_eff
    # ================================================================
    pr("=" * 70)
    pr("Step 2: G_eff from the Spectral Action")
    pr("=" * 70)
    pr()
    pr("In the spectral action framework, the 4D Einstein-Hilbert term arises as:")
    pr("  S_EH = (1/16*pi*G_eff) * integral R_M sqrt{g_M} d^4x")
    pr()
    pr("where 1/(16*pi*G_eff) = a_2(tau) * M_KK^2 / (4*pi)")
    pr("and a_2(tau) is the second Seeley-DeWitt coefficient of the full Dirac spectrum.")
    pr()
    pr("The S59 spinor norm computation found the SECTOR-RESOLVED a_2:")

    sector_a2 = s59_sn["sector_a2"]
    sector_a0 = s59_sn["sector_a0"]
    sector_a4 = s59_sn["sector_a4"]
    sector_d2 = s59_sn["sector_d2"]
    sector_count = s59_sn["sector_count"]
    a2_total = float(s59_sn["a2_total"])
    N_factor = float(s59_sn["N_factor_a2"])

    pr(f"  Sector d^2 values: {sector_d2}")
    pr(f"  Sector a_2 values: {sector_a2}")
    pr(f"  Sector mode counts: {sector_count}")
    pr(f"  Total a_2 = {a2_total:.4f}")
    pr(f"  N_factor (a_2 ratio) = {N_factor:.6f}")
    pr()

    # The CRITICAL calculation: how does delta_tau affect a_2?
    # From S59: frac_da2 = (1/a_2)(da_2/dtau) = 99.13 at the fold.
    # This is the fractional sensitivity of a_2 to tau.
    frac_da2 = float(s59_ts["delta_G_over_G"]) / (-float(s59_ts["delta_tau_eff"]))
    # Verify: delta_G/G = -frac_da2 * delta_tau_eff
    delta_tau_eff = float(s59_ts["delta_tau_eff"])
    delta_G_over_G = float(s59_ts["delta_G_over_G"])

    pr(f"  From S59: frac_da2 = (1/a_2)(da_2/dtau) = {frac_da2:.4f}")
    pr(f"  delta_tau_eff = {delta_tau_eff:.6f}")
    pr(f"  delta_G/G = {delta_G_over_G:.6e}")
    pr()

    # G_eff responds to delta_tau through:
    #   delta_G_eff / G_eff = -delta_a2 / a2 = -frac_da2 * delta_tau
    # and delta_N/N = (1/2) * delta_G_eff/G_eff = -(1/2) * frac_da2 * delta_tau
    delta_N_over_N = float(s59_ts["delta_N_over_N"])
    pr(f"  delta_N/N = {delta_N_over_N:.6e}")

    out["frac_da2"] = np.array(frac_da2)
    out["delta_G_over_G"] = np.array(delta_G_over_G)
    out["delta_N_over_N"] = np.array(delta_N_over_N)

    # ================================================================
    #  Step 3: How delta_tau enters alpha (fine structure constant)
    # ================================================================
    pr()
    pr("=" * 70)
    pr("Step 3: alpha from the Fiber Metric (Paper 13 eq 5.21)")
    pr("=" * 70)
    pr()
    pr("The gauge coupling constants come from the fiber metric:")
    pr("  g'^2/4 = 3/lambda_1    (hypercharge)")
    pr("  g^2/4  = 1/lambda_2    (weak isospin)")
    pr("  alpha_EM = e^2/(4*pi)")
    pr("  e = 2*sqrt(3) / sqrt(lambda_1 + 3*lambda_2)  (Paper 13 eq 5.21)")
    pr()
    pr("In the Jensen deformation parametrization (project convention):")
    pr("  g_1/g_2 = e^{-2*tau}   (Session 17a B-1)")
    pr("  => log(g_1^2/g_2^2) = -4*tau")
    pr("  => delta(g_1^2)/g_1^2 - delta(g_2^2)/g_2^2 = -4 * delta_tau")
    pr()
    pr("From the clock constraint (S22d E-3):")
    pr("  delta_alpha/alpha = clock_coeff * delta_tau")
    pr(f"  clock_coeff = {clock_coeff}")
    pr()

    # TWO independent routes to delta_alpha/alpha:
    #
    # Route A: Clock constraint (S22d): delta_alpha/alpha = -3.08 * delta_tau
    # This is a DERIVED result from the Dirac spectrum.
    #
    # Route B: Direct from Paper 13 eq 5.21:
    #   alpha_EM = e^2/(4*pi) = 12 / [pi*(lambda_1 + 3*lambda_2)]
    #   The tau-dependence enters through the metric parameters lambda_i.
    #   In the single-parameter model: lambda_1 = lambda_2 = lambda_3 = lambda(tau)
    #   In the 3-parameter model: each lambda_i has its own tau-dependence.
    #
    # For the SCREENING question, the key structural distinction is:
    #   G_eff involves a_2 = SUM over ALL sectors (integral over K)
    #   alpha involves ONLY the metric in the u(1) direction (point evaluation)
    #
    # But in the project's framework, both ultimately depend on the SAME tau
    # through the left-invariant metric g_phi. There is no independent
    # parameter to tune.

    # Compute delta_alpha/alpha two ways:
    # Method 1: Clock constraint
    delta_alpha_clock = abs(clock_coeff) * delta_tau_eff
    pr(f"  Method 1 (clock constraint): |delta_alpha/alpha| = {delta_alpha_clock:.6e}")

    # Method 2: Direct from g1/g2 = e^{-2tau}
    # The Weinberg angle is sin^2(theta_W) = g'^2/(g'^2 + g^2) = 3*lambda_2/(lambda_1 + 3*lambda_2)
    # In the single-parameter model with the Jensen deformation:
    #   g_1^2 = g'^2 cos^2(theta_W) ... but the project uses g_1/g_2 = e^{-2tau} directly
    # For the EM coupling: alpha_EM = g^2 sin^2(theta_W) / (4*pi)
    #   where g^2 = 4/lambda_2.
    # delta(alpha)/alpha = delta(g^2)/g^2 + delta(sin^2 theta_W)/sin^2(theta_W)
    #
    # In the Jensen parametrization at small delta_tau:
    #   g'/g = sqrt(3*lambda_2/lambda_1) = sqrt(3) * e^{-2*tau}
    #   So lambda_1/lambda_2 = 3 * e^{4*tau}
    #   => d(lambda_1/lambda_2)/dtau = 12 * e^{4*tau}
    #
    # For the single-parameter deformation tau, both g' and g depend on tau.
    # The electromagnetic coupling is:
    #   1/alpha_EM = (lambda_1 + 3*lambda_2)*pi/12 = lambda_2*pi/12 * (3*e^{4tau} + 3)
    #             = lambda_2*pi/4 * (e^{4tau} + 1)
    #
    # If lambda_2 is tau-independent (as in Paper 13 eq 5.21 where it's a free parameter):
    #   d(1/alpha)/dtau = lambda_2 * pi * e^{4tau}
    #   delta_alpha/alpha = -4*delta_tau * e^{4tau}/(1 + e^{4tau})
    #
    # But in the project's actual framework, the Dirac spectrum computation gives
    # the clock constraint directly. The clock constraint is MORE reliable since
    # it comes from the FULL spectral computation, not the classical limit.

    # Method 2: Using exponential parametrization
    e4tau = np.exp(4.0 * tau)
    alpha_sensitivity_direct = 4.0 * e4tau / (1.0 + e4tau)
    delta_alpha_direct = alpha_sensitivity_direct * delta_tau_eff
    pr(f"  Method 2 (Paper 13 direct): |delta_alpha/alpha| = {delta_alpha_direct:.6e}")
    pr(f"    alpha sensitivity = {alpha_sensitivity_direct:.4f} (vs clock = {abs(clock_coeff):.4f})")
    pr()
    pr("  NOTE: Both methods give comparable sensitivities (~3-4 per unit tau).")
    pr("  Using clock constraint (canonical, from full Dirac spectrum).")
    pr()

    delta_alpha_over_alpha = delta_alpha_clock
    out["delta_alpha_over_alpha"] = np.array(delta_alpha_over_alpha)
    out["alpha_sensitivity_clock"] = np.array(abs(clock_coeff))
    out["alpha_sensitivity_direct"] = np.array(alpha_sensitivity_direct)

    # ================================================================
    #  Step 4: The Naive Screening Ratio
    # ================================================================
    pr("=" * 70)
    pr("Step 4: Naive Screening Ratio (no fiber integration correction)")
    pr("=" * 70)
    pr()

    # Screening ratio = |delta_N/N| / |delta_alpha/alpha|
    # = |(1/2)(delta_G/G)| / |delta_alpha/alpha|
    # = (1/2)|frac_da2 * delta_tau| / |clock_coeff * delta_tau|
    # = (1/2)|frac_da2| / |clock_coeff|
    # NOTE: delta_tau CANCELS. The ratio is a structural property of the fold.

    screening_naive = (0.5 * abs(frac_da2)) / abs(clock_coeff)
    pr(f"  |delta_N/N| = (1/2) * |frac_da2| * delta_tau = (1/2) * {abs(frac_da2):.4f} * delta_tau")
    pr(f"  |delta_alpha/alpha| = |clock_coeff| * delta_tau = {abs(clock_coeff):.4f} * delta_tau")
    pr(f"  => delta_tau CANCELS in the ratio")
    pr()
    pr(f"  Screening ratio (naive) = (1/2) * |frac_da2| / |clock_coeff|")
    pr(f"                          = (1/2) * {abs(frac_da2):.4f} / {abs(clock_coeff):.4f}")
    pr(f"                          = {screening_naive:.4f}")
    pr()
    pr(f"  This is {screening_naive:.1f}x.  Gate threshold: 10^4 = 10000.")
    pr(f"  Shortfall: {1e4 / screening_naive:.0f}x below threshold.")
    pr()

    out["screening_naive"] = np.array(screening_naive)

    # ================================================================
    #  Step 5: Fiber Integration Measure and Sector Structure
    # ================================================================
    pr("=" * 70)
    pr("Step 5: Fiber Integration Measure Correction")
    pr("=" * 70)
    pr()
    pr("The key structural question: does the fiber integration measure DIFFERENTIATE")
    pr("the tau-sensitivity of G_eff from that of alpha?")
    pr()
    pr("G_eff pathway:")
    pr("  a_2 = SUM_{(p,q)} d_{(p,q)}^2 * a_2^{(p,q)}(tau)")
    pr("  where d^2 is the Peter-Weyl multiplicity and a_2^{(p,q)} is the sector")
    pr("  Seeley-DeWitt coefficient. The TOTAL a_2 is a weighted sum.")
    pr()
    pr("alpha pathway:")
    pr("  alpha = e^2/(4*pi), with e determined by the fiber metric along the u(1)")
    pr("  generator gamma_phi. This is a POINT evaluation on the Lie algebra metric.")
    pr("  Specifically: e^2 = 6*kappa_M / beta(gamma_phi, gamma_phi) (Paper 13 eq 4.13).")
    pr()
    pr("STRUCTURAL ANALYSIS:")
    pr("  Both G_eff and alpha depend on the SAME left-invariant metric g_phi(tau).")
    pr("  There is exactly ONE deformation parameter: tau = |phi|^2.")
    pr("  a_2(tau) is a function of tau. alpha(tau) is a function of tau.")
    pr("  Both have O(1) sensitivities to tau (da_2/a_2/dtau ~ 99, dalpha/alpha/dtau ~ 3).")
    pr("  The fiber integration sums AMPLIFY the sensitivity of a_2 (frac_da2 = 99)")
    pr("  relative to alpha (sensitivity = 3.08).")
    pr("  This goes in the WRONG direction for screening: G varies MORE than alpha.")
    pr()

    # Sector-resolved analysis: does any sector dominate a_2 sensitivity differently?
    # From S59 spinor norm: sector_a2 and sector_d2
    pr("  Sector-resolved a_2 (from S59 SPINOR-NORM-59):")
    sector_labels = ["(0,0)", "(1,0)", "(2,0)+(0,2)", "(1,1)", "(3,0)+(0,3)", "(2,1)+(1,2)"]
    total_weighted_a2 = 0.0  # (local)
    for i in range(len(sector_d2)):
        weighted = sector_d2[i] * sector_a2[i]
        total_weighted_a2 += weighted
        pr(f"    Sector {sector_labels[i]}: d^2={sector_d2[i]:>4}, a_2={sector_a2[i]:>12.4f}, "
           f"d^2*a_2={weighted:>12.4f} ({100*weighted/a2_total:>5.1f}%)")
    pr(f"    Total: {total_weighted_a2:.4f} (check vs a2_total = {a2_total:.4f})")
    pr()

    # The fiber volume factor enters G_eff but NOT alpha:
    #   G_eff^{-1} ~ a_2 * M_KK^2 / (4*pi)
    #   alpha ~ point evaluation on fiber metric (no Vol(K) factor)
    #
    # But BOTH still depend on tau through the same metric g_phi.
    # The volume factor Vol(K, g_phi) = Vol_Haar * f_phi(tau) does enter G_eff
    # through the fiber integration. However, a_2 ALREADY includes this.
    # The spectral action a_2 is computed FROM the fiber-integrated Dirac spectrum.
    # So the fiber volume is already incorporated in frac_da2 = 99.

    out["sector_a2"] = sector_a2
    out["sector_d2"] = sector_d2
    out["a2_total"] = np.array(a2_total)

    # ================================================================
    #  Step 6: (M_KK / M_Pl)^2 Suppression Factor
    # ================================================================
    pr("=" * 70)
    pr("Step 6: (M_KK / M_Pl)^2 Suppression Factor")
    pr("=" * 70)
    pr()

    MKK_over_MPl_sq = (M_KK / M_Pl_reduced)**2
    pr(f"  M_KK = {M_KK:.4e} GeV (gravity route)")
    pr(f"  M_Pl_reduced = {M_Pl_reduced:.4e} GeV")
    pr(f"  (M_KK / M_Pl)^2 = {MKK_over_MPl_sq:.4e}")
    pr()

    # Where does this factor enter?
    # The relation between the 12D and 4D Newton's constants is:
    #   1/G_4 = Vol(K) / G_12
    # So:
    #   G_4 = G_12 / Vol(K)
    #   M_Pl^2 = M_{12}^{12-2} * Vol(K) = M_KK^{10} * Vol(K)  [in natural units]
    #   Actually: M_Pl^2 = M_KK^2 * (M_KK * R_K)^8 / (something)
    #   In the spectral action: M_Pl^2 = 4*pi*a_2*M_KK^2
    #
    # The key: (M_KK/M_Pl)^2 = 1/(4*pi*a_2)
    # This is just the INVERSE of the spectral action coefficient.
    # It does NOT provide independent suppression --- it IS the a_2 factor.

    check_MKK_MPl = 1.0 / (4.0 * PI * a2_fold)
    pr(f"  Cross-check: 1/(4*pi*a_2_fold) = {check_MKK_MPl:.4e}")
    pr(f"  (M_KK/M_Pl)^2 directly      = {MKK_over_MPl_sq:.4e}")
    pr()

    # Using S59 corrected values:
    a2_corrected = float(s59_sn["a2_corrected"])
    MPl_corrected = float(s59_sn["M_Pl_reduced_corrected"])
    check_corrected = 1.0 / (4.0 * PI * a2_corrected)
    MKK_over_MPl_corrected_sq = (M_KK / MPl_corrected)**2

    pr(f"  With S59 spinor-norm correction (N_factor = {float(s59_sn['N_factor_a2']):.4f}):")
    pr(f"  a_2_corrected = {a2_corrected:.4f}")
    pr(f"  M_Pl_corrected = {MPl_corrected:.4e}")
    pr(f"  1/(4*pi*a_2_corrected) = {check_corrected:.4e}")
    pr(f"  (M_KK/M_Pl_corr)^2 = {MKK_over_MPl_corrected_sq:.4e}")
    pr()

    pr("  STRUCTURAL CONCLUSION:")
    pr("  (M_KK/M_Pl)^2 = 1/(4*pi*a_2). It is NOT an independent suppression factor.")
    pr("  It is algebraically identical to the inverse of the a_2 coefficient that")
    pr("  already determines G_eff. Inserting it would be DOUBLE-COUNTING.")
    pr()
    pr("  The screening ratio formula is:")
    pr("    R_screen = |delta_N/N| / |delta_alpha/alpha|")
    pr("    = (1/2)|delta_G/G| / |delta_alpha/alpha|")
    pr("    = (1/2)|(da_2/dtau)/a_2| / |(dalpha/dtau)/alpha|")
    pr("    = (1/2)|frac_da_2| / |clock_coeff|")
    pr("  The (M_KK/M_Pl)^2 factor cancels: it is in BOTH numerator and denominator")
    pr("  when you trace through the spectral action derivation.")
    pr()

    out["MKK_over_MPl_sq"] = np.array(MKK_over_MPl_sq)
    out["MKK_over_MPl_corrected_sq"] = np.array(MKK_over_MPl_corrected_sq)

    # ================================================================
    #  Step 7: Can Sector Separation Save Screening?
    # ================================================================
    pr("=" * 70)
    pr("Step 7: Sector Separation Analysis")
    pr("=" * 70)
    pr()
    pr("The only escape route: if different PW sectors have DIFFERENT")
    pr("tau-sensitivities, and if alpha depends on a different combination")
    pr("of sectors than G_eff.")
    pr()
    pr("From the D_K block-diagonality theorem (S22b):")
    pr("  D_K is block-diagonal in Peter-Weyl sectors to machine epsilon (8.4e-15).")
    pr("  Each sector evolves independently under the Jensen deformation.")
    pr()
    pr("G_eff: proportional to a_2 = SUM d^2 * a_2^{(p,q)}(tau)")
    pr("alpha: determined by the metric on su(3), specifically the u(1) direction.")
    pr("  In the (p,q) language, the (0,0) singlet sector gives the IDENTITY rep,")
    pr("  which sees only the global metric scale. Higher sectors see curvature.")
    pr()

    # Check: is alpha determined by any specific sector?
    # From Paper 13 eq 4.13: e^2 = 6*kappa_M / beta(gamma_phi, gamma_phi)
    # where gamma_phi is the left-invariant Killing field of g_phi.
    # beta(gamma_phi, gamma_phi) = lambda * |gamma_phi|^2 depends on
    # the normalization of gamma_phi in the metric g_phi.
    # This is determined by the METRIC ON SU(3) at one point (e.g., the identity),
    # not by an integral over SU(3). It is determined entirely by the
    # (0,0) sector properties (the metric itself).
    #
    # Actually: the metric g_phi is a single object on su(3). It determines
    # ALL physical quantities. The Peter-Weyl decomposition resolves the
    # SPECTRAL content of the Dirac operator, but the gauge couplings
    # are classical (zeroth-order in hbar) quantities determined by g_phi directly.
    #
    # So alpha sees the metric g_phi at zeroth order, while G_eff sees the
    # ENTIRE spectrum through a_2. But both ultimately trace back to
    # the SAME one-parameter family g_phi(tau).

    # The (0,0) singlet contributes only 14.23 / 162984 = 0.0087% of a_2
    singlet_a2 = float(s59_sn["a2_singlet"])
    singlet_frac = singlet_a2 / a2_total
    pr(f"  (0,0) singlet a_2 = {singlet_a2:.4f}")
    pr(f"  Fraction of total a_2: {singlet_frac:.6e} = {100*singlet_frac:.4f}%")
    pr()
    pr("  If alpha depended ONLY on the singlet sector and G depended on ALL sectors,")
    pr("  the screening ratio could differ. But this is NOT the case:")
    pr("  alpha depends on the METRIC g_phi, which determines everything.")
    pr()

    # What IS the actual structural ratio?
    # frac_da2 / frac_dalpha = 99.13 / 3.08 = 32.2
    # The 1/2 factor from delta_N/N = (1/2)*delta_G/G gives:
    # screening = 32.2 / 2 = 16.1
    # This is structural: the spectral action has a LARGER tau-sensitivity
    # than the gauge coupling because a_2 sums d^2-weighted eigenvalues
    # that amplify the geometric curvature change.

    structural_ratio = abs(frac_da2) / abs(clock_coeff)
    pr(f"  Structural sensitivity ratio: frac_da2 / |clock_coeff|")
    pr(f"    = {abs(frac_da2):.4f} / {abs(clock_coeff):.4f} = {structural_ratio:.4f}")
    pr(f"  Screening ratio (= structural/2): {screening_naive:.4f}")
    pr()

    # Can the generalized 3-parameter metric help?
    # In Paper 13 Section 5, lambda_1, lambda_2, lambda_3 are INDEPENDENT.
    # If the Jensen deformation primarily changes lambda_3 (the C^2 direction)
    # while leaving lambda_1 (the u(1) direction) fixed, then alpha would
    # be screened while G still varies.
    #
    # But in the project's framework, the Jensen deformation is a ONE-PARAMETER
    # family g_phi(tau) where all lambda_i depend on the SAME tau.
    # The constraint tau = |phi|^2 fixes the relationship between the lambdas.
    #
    # Let me compute the actual lambda ratios:

    pr("  Three-parameter analysis (Paper 13 Section 5):")
    pr("  If lambda_1, lambda_2, lambda_3 could vary INDEPENDENTLY,")
    pr("  we could decouple alpha (which depends on lambda_1, lambda_2)")
    pr("  from G (which depends on the total spectral action).")
    pr("  But in the Jensen deformation: all lambda_i track the same tau.")
    pr()

    # From Paper 13 eq 5.21:
    # g'^2 = 12/lambda_1
    # g^2 = 4/lambda_2
    # alpha_EM = (g')^2 * (g)^2 / [4*pi*((g')^2 + (g)^2)]
    #          = (12/lambda_1)*(4/lambda_2) / [4*pi*(12/lambda_1 + 4/lambda_2)]
    #          = 48/(lambda_1*lambda_2) / [4*pi*(12*lambda_2 + 4*lambda_1)/(lambda_1*lambda_2)]
    #          = 48 / [4*pi*(12*lambda_2 + 4*lambda_1)]
    #          = 12 / [pi*(3*lambda_2 + lambda_1)]
    #
    # So alpha = 12 / [pi*(lambda_1 + 3*lambda_2)]
    # d(alpha)/alpha = -d(lambda_1 + 3*lambda_2)/(lambda_1 + 3*lambda_2)
    #
    # Under Jensen deformation with g'/g = sqrt(3)*e^{-2tau}:
    #   lambda_1/lambda_2 = 3*e^{4*tau}
    # Setting lambda_2 = lambda_0 (constant) => lambda_1 = 3*lambda_0*e^{4*tau}
    #   lambda_1 + 3*lambda_2 = lambda_0*(3*e^{4*tau} + 3) = 3*lambda_0*(e^{4*tau} + 1)
    #   d/dtau = 3*lambda_0 * 4*e^{4*tau} = 12*lambda_0*e^{4*tau}
    #   Fractional: 12*e^{4*tau} / [3*(e^{4*tau}+1)] = 4*e^{4*tau}/(e^{4*tau}+1)
    # At tau=0.19: e^{4*0.19} = e^{0.76} = 2.138
    # Fractional = 4*2.138/(2.138+1) = 8.554/3.138 = 2.726

    e4t = np.exp(4.0 * tau)
    alpha_frac_sensitivity_3param = 4.0 * e4t / (e4t + 1.0)
    pr(f"  e^{{4*tau}} = {e4t:.4f}")
    pr(f"  3-param alpha sensitivity: {alpha_frac_sensitivity_3param:.4f}")
    pr(f"  Clock constraint gives: {abs(clock_coeff):.4f}")
    pr(f"  Ratio: {abs(clock_coeff) / alpha_frac_sensitivity_3param:.4f}")
    pr()

    # ================================================================
    #  Step 8: Alternative Route — Volume Form Screening
    # ================================================================
    pr("=" * 70)
    pr("Step 8: Volume Form Screening (the f_phi factor)")
    pr("=" * 70)
    pr()
    pr("One possible loophole: the fiber volume form f_phi(tau) enters G_eff")
    pr("through the Einstein-Hilbert fiber integration, but alpha is determined")
    pr("by the point metric. If G_eff ~ a_2 * f_phi and alpha ~ 1/lambda_1,")
    pr("then delta_G/G would have an ADDITIONAL contribution from delta_f/f.")
    pr()
    pr("However, a_2 is computed from the FULL Dirac operator on P = M^4 x K,")
    pr("which already includes the fiber volume through the spectral measure.")
    pr("The frac_da2 = 99.13 ALREADY incorporates any volume form effects.")
    pr()
    pr("Verification: the volume form sensitivity:")
    pr(f"  (1/f)(df/dtau) at tau = {tau}: {frac_df:.4f}")
    pr(f"  This is {frac_df:.4f}/{abs(frac_da2):.4f} = {abs(frac_df/frac_da2):.4f}")
    pr(f"  of the spectral a_2 sensitivity.")
    pr()
    pr("  The volume form diverges at tau -> 1/4, contributing to the steep slope.")
    pr("  But this is already captured in a_2(tau).")
    pr()

    out["frac_df_phi"] = np.array(frac_df)

    # ================================================================
    #  Step 9: Final Screening Ratio with All Corrections
    # ================================================================
    pr("=" * 70)
    pr("Step 9: Final Screening Ratio")
    pr("=" * 70)
    pr()

    # The ONLY screening ratio is the structural one.
    # No additional suppression factors exist.
    screening_with_fiber = screening_naive  # Fiber integration is ALREADY in a_2
    screening_with_MKK = screening_naive    # (M_KK/M_Pl)^2 = 1/(4*pi*a_2), already counted

    pr(f"  Screening ratio (naive)              = {screening_naive:.4f}")
    pr(f"  Screening ratio (with fiber vol)     = {screening_with_fiber:.4f} (same: already in a_2)")
    pr(f"  Screening ratio (with (M_KK/M_Pl)^2) = {screening_with_MKK:.4f} (same: algebraic identity)")
    pr()

    # The ONLY way to get a different ratio is if the framework has
    # multiple independent deformation parameters. In the current
    # one-parameter Jensen deformation, the screening ratio is fixed:
    max_possible_screening = screening_naive
    pr(f"  MAXIMUM POSSIBLE screening ratio = {max_possible_screening:.4f}")
    pr(f"  Required for PASS: 10^4 = 10000")
    pr(f"  Shortfall: {1e4 / max_possible_screening:.0f}x")
    pr()

    out["screening_with_fiber"] = np.array(screening_with_fiber)
    out["screening_with_MKK"] = np.array(screening_with_MKK)
    out["screening_ratio_final"] = np.array(max_possible_screening)

    # Supplementary: what delta_tau gives the ALPHA-ENV-43 target?
    alpha_target = 1.0e-6  # (local)
    delta_tau_for_alpha = alpha_target / abs(clock_coeff)
    delta_G_at_alpha_target = abs(frac_da2) * delta_tau_for_alpha
    delta_N_at_alpha_target = 0.5 * delta_G_at_alpha_target

    pr(f"  Supplementary: if delta_alpha/alpha = 10^-6 (ALPHA-ENV-43 target):")
    pr(f"    delta_tau = {delta_tau_for_alpha:.4e}")
    pr(f"    delta_G/G = {delta_G_at_alpha_target:.4e}")
    pr(f"    delta_N/N = {delta_N_at_alpha_target:.4e}")
    pr(f"    This is FAR too small for w_a != 0 (need delta_N/N ~ 0.08)")
    pr()

    out["delta_tau_for_alpha_target"] = np.array(delta_tau_for_alpha)
    out["delta_G_at_alpha_target"] = np.array(delta_G_at_alpha_target)
    out["delta_N_at_alpha_target"] = np.array(delta_N_at_alpha_target)

    # ================================================================
    #  Step 10: Gate Verdict
    # ================================================================
    pr("=" * 70)
    pr("GATE: SECTOR-DIM-REDUCT-60")
    pr("=" * 70)
    pr()

    if max_possible_screening > 1e4:
        verdict = "PASS"
        detail = f"Screening ratio = {max_possible_screening:.1f} > 10^4"
    elif max_possible_screening < 100:
        verdict = "FAIL"
        detail = f"Screening ratio = {max_possible_screening:.1f} < 100"
    else:
        verdict = "INFO"
        detail = f"Screening ratio = {max_possible_screening:.1f} in [100, 10^4]"

    pr(f"  Screening ratio = {max_possible_screening:.4f}")
    pr(f"  Verdict: {verdict}")
    pr(f"  Detail: {detail}")
    pr()
    pr(f"  The Riemannian submersion structure of Paper 13 provides NO additional")
    pr(f"  screening. Both G_eff and alpha depend on the SAME one-parameter Jensen")
    pr(f"  deformation tau. The (M_KK/M_Pl)^2 factor is algebraically 1/(4*pi*a_2),")
    pr(f"  which is already the coefficient determining G_eff. No double-counting.")
    pr()
    pr(f"  The screening ratio is a STRUCTURAL constant at the fold:")
    pr(f"    R_screen = (1/2)|frac_da_2| / |clock_coeff|")
    pr(f"    = (1/2) * {abs(frac_da2):.2f} / {abs(clock_coeff):.2f}")
    pr(f"    = {max_possible_screening:.1f}")
    pr()
    pr(f"  To achieve R_screen > 10^4, the framework would need frac_da2/clock_coeff > 2*10^4,")
    pr(f"  i.e., the spectral action sensitivity would need to exceed the gauge coupling")
    pr(f"  sensitivity by a factor of 20,000. At the fold, the ratio is only {structural_ratio:.1f}.")
    pr()
    pr(f"  PHYSICAL IMPLICATION:")
    pr(f"  Timescape w_a requires delta_N/N ~ 0.08, which implies delta_tau ~ 0.0016.")
    pr(f"  At this delta_tau, delta_alpha/alpha = {abs(clock_coeff) * 0.0016:.4f},")
    pr(f"  which exceeds ALPHA-ENV-43 (10^-6) by {abs(clock_coeff) * 0.0016 / 1e-6:.0f}x.")
    pr(f"  The timescape mechanism is INCOMPATIBLE with constant fine structure constant.")
    pr()

    out["gate_name"] = np.array(["SECTOR-DIM-REDUCT-60"])
    out["gate_verdict"] = np.array([verdict])
    out["gate_detail"] = np.array([detail])

    # Save output
    outpath = os.path.join(BASEDIR, "s60_sector_dim_reduct.npz")
    np.savez(outpath, **out)
    pr(f"Data saved: {outpath}")

    # Also save a results text file
    respath = os.path.join(BASEDIR, "s60_sector_dim_reduct_results.txt")
    with open(respath, "w") as rf:
        rf.write("SECTOR-DIM-REDUCT-60: Sector-Resolved Dimensional Reduction for Screening\n")
        rf.write("=" * 74 + "\n\n")
        rf.write(f"Screening ratio (naive)    = {screening_naive:.4f}\n")
        rf.write(f"Screening ratio (final)    = {max_possible_screening:.4f}\n")
        rf.write(f"frac_da2                   = {abs(frac_da2):.4f}\n")
        rf.write(f"clock_coeff                = {clock_coeff}\n")
        rf.write(f"(M_KK/M_Pl)^2             = {MKK_over_MPl_sq:.4e}\n")
        rf.write(f"1/(4*pi*a_2)               = {check_MKK_MPl:.4e}\n")
        rf.write(f"  => Same quantity (no additional suppression)\n\n")
        rf.write(f"delta_tau_eff              = {delta_tau_eff:.6f}\n")
        rf.write(f"delta_G/G                  = {delta_G_over_G:.6e}\n")
        rf.write(f"delta_N/N                  = {delta_N_over_N:.6e}\n")
        rf.write(f"delta_alpha/alpha           = {delta_alpha_clock:.6e}\n\n")
        rf.write(f"GATE: SECTOR-DIM-REDUCT-60\n")
        rf.write(f"VERDICT: {verdict}\n")
        rf.write(f"DETAIL: {detail}\n")
    pr(f"Results saved: {respath}")
    pr()
    pr("=== SECTOR-DIM-REDUCT-60 COMPLETE ===")

except Exception as e:
    import traceback
    pr(f"\nERROR: {e}")
    pr(traceback.format_exc())

finally:
    log.close()
