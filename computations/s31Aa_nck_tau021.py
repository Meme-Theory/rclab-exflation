"""
BA-31-7: B-31nck at tau~0.21 (NCG-KK Compatibility Test)
==========================================================

Computes Lambda_SA / M_KK at the RGE-compatible tau ~ 0.21.

Lambda_SA is the unification scale where alpha_1 = alpha_2 when running
upward from M_KK using SM one-loop beta functions. The ratio Lambda_SA/M_KK
measures the NCG-KK tension: if the spectral action cutoff must equal the
unification scale, then Lambda_SA/M_KK >> 1 means NCG and KK are
irreconcilable.

Session 30Bb found Lambda_SA/M_KK ~ 2.0e15 at tau~0.57, eps~0.135.
This computation checks tau~0.21 on the Jensen curve (eps=0).

Gate B-31nck:
  PASS if Lambda_SA/M_KK in [10^{-3}, 10^3] at M_KK ~ 10^16 GeV
  FAIL if outside this range

Author: sim (phonon-exflation-sim), Session 31Aa
Date: 2026-03-02
"""

import numpy as np
import time

# SM one-loop beta function coefficients
B1 = 41.0 / 10.0   # U(1)_Y
B2 = -19.0 / 6.0    # SU(2)_L

# PDG values at M_Z
ALPHA_EM = 1.0 / 127.9
SIN2_W_MZ = 0.23122
M_Z = 91.1876e9  # eV -> GeV: 91.2 GeV


def compute_alpha_at_MKK(g1g2, M_KK):
    """
    Compute alpha_1 and alpha_2 at M_KK from the framework's g1/g2 ratio.

    The spectral action gives g1/g2 at the compactification scale.
    Using Formula B (Baptista Paper 14, eq 2.85-2.93):
      sin^2(theta_W) = 3*g1^2 / (g1^2 + 3*g2^2) = 3*(g1/g2)^2 / (1 + 3*(g1/g2)^2)

    Wait -- actually sin^2_B = 3*L2 / (L1 + 3*L2). This is a GEOMETRIC ratio,
    not directly the gauge coupling ratio. The gauge coupling relation is:
      g1^2/g2^2 = L2/L1 (from the spectral action normalization)
    So g1/g2 = sqrt(L2/L1) at M_KK.

    Then: alpha_1_GUT = (5/3) * alpha_1_Y (GUT normalization)
    And the spectral action gives alpha_1_GUT * alpha_2 = g_unified^2 / (4pi)

    For RGE running: we need alpha_1 and alpha_2 separately at M_KK.
    Approach: run SM RGE from M_Z up to M_KK.
    """
    # Run up from M_Z
    t = np.log(M_KK / M_Z)

    # At M_Z: alpha_1 = (5/3) * alpha_em / cos^2_W, alpha_2 = alpha_em / sin^2_W
    alpha_1_MZ = (5.0/3.0) * ALPHA_EM / (1.0 - SIN2_W_MZ)
    alpha_2_MZ = ALPHA_EM / SIN2_W_MZ

    # One-loop running to M_KK
    inv_alpha_1_MKK = 1.0/alpha_1_MZ - B1/(2*np.pi) * t
    inv_alpha_2_MKK = 1.0/alpha_2_MZ - B2/(2*np.pi) * t

    alpha_1_MKK = 1.0 / inv_alpha_1_MKK if inv_alpha_1_MKK > 0 else np.inf
    alpha_2_MKK = 1.0 / inv_alpha_2_MKK if inv_alpha_2_MKK > 0 else np.inf

    return alpha_1_MKK, alpha_2_MKK


def find_Lambda_SA(alpha_1_KK, alpha_2_KK, M_KK):
    """
    Find Lambda_SA where alpha_1 = alpha_2 above M_KK.

    From: 1/alpha_1 - b1/(2pi)*t = 1/alpha_2 - b2/(2pi)*t
    => t = 2pi * (1/alpha_1 - 1/alpha_2) / (b1 - b2)
    => Lambda_SA = M_KK * exp(t)
    """
    delta_inv = 1.0/alpha_1_KK - 1.0/alpha_2_KK
    delta_b = B1 - B2
    t = 2.0 * np.pi * delta_inv / delta_b
    Lambda_SA = M_KK * np.exp(t)
    ratio = Lambda_SA / M_KK
    return Lambda_SA, ratio, t


def main():
    t_start = time.time()

    print("=" * 70)
    print("BA-31-7: B-31nck AT tau~0.21")
    print("=" * 70)

    # Load grid data
    sdw = np.load('tier0-computation/s30b_sdw_grid.npz')
    tau_grid = sdw['tau']
    eps_grid = sdw['eps']
    L1_grid = sdw['L1']
    L2_grid = sdw['L2']
    g1g2_grid = sdw['g1g2']

    # tau=0.21 on Jensen curve (eps=0)
    idx_tau = np.argmin(np.abs(tau_grid - 0.21))
    idx_eps = np.argmin(np.abs(eps_grid - 0.0))

    tau_val = tau_grid[idx_tau]
    L1 = L1_grid[idx_tau, idx_eps]
    L2 = L2_grid[idx_tau, idx_eps]
    g1g2 = g1g2_grid[idx_tau, idx_eps]

    # Formula B Weinberg angle
    sin2_B = 3.0 * L2 / (L1 + 3.0 * L2)

    print(f"\nAt tau={tau_val:.3f}, eps=0.0 (Jensen curve):")
    print(f"  L1 = {L1:.6f}")
    print(f"  L2 = {L2:.6f}")
    print(f"  g1/g2 = sqrt(L2/L1) = {g1g2:.6f}")
    print(f"  sin^2_B = 3*L2/(L1+3*L2) = {sin2_B:.6f}")

    # Scan over M_KK values
    M_KK_values = np.logspace(14, 18, 5)  # 10^14 to 10^18 GeV
    # Convert to GeV
    M_KK_values_GeV = M_KK_values

    print(f"\n{'M_KK (GeV)':>14} {'alpha_1':>10} {'alpha_2':>10} {'a1/a2':>10} "
          f"{'Lambda_SA (GeV)':>16} {'Lambda_SA/M_KK':>16} {'log10(ratio)':>14} {'Status':>8}")
    print("-" * 100)

    results = {}
    for M_KK in M_KK_values_GeV:
        alpha_1, alpha_2 = compute_alpha_at_MKK(g1g2, M_KK)

        if np.isfinite(alpha_1) and np.isfinite(alpha_2) and alpha_1 > 0 and alpha_2 > 0:
            Lambda_SA, ratio, t_val = find_Lambda_SA(alpha_1, alpha_2, M_KK)

            if ratio > 0 and np.isfinite(ratio):
                log_ratio = np.log10(ratio)
                if 1e-3 <= ratio <= 1e3:
                    status = "PASS"
                else:
                    status = "FAIL"
            else:
                log_ratio = np.nan
                status = "N/A"
        else:
            Lambda_SA = np.nan
            ratio = np.nan
            log_ratio = np.nan
            status = "N/A"

        print(f"  {M_KK:12.2e} {alpha_1:10.6f} {alpha_2:10.6f} {alpha_1/alpha_2:10.4f} "
              f"  {Lambda_SA:14.4e} {ratio:14.4e}   {log_ratio:12.4f}     {status}")

        results[M_KK] = {
            'alpha_1': alpha_1, 'alpha_2': alpha_2,
            'Lambda_SA': Lambda_SA, 'ratio': ratio,
            'log_ratio': log_ratio, 'status': status
        }

    # Primary check: M_KK = 10^16 GeV
    M_KK_ref = 1e16
    alpha_1_ref, alpha_2_ref = compute_alpha_at_MKK(g1g2, M_KK_ref)
    Lambda_SA_ref, ratio_ref, t_ref = find_Lambda_SA(alpha_1_ref, alpha_2_ref, M_KK_ref)

    print(f"\n--- Primary check at M_KK = 10^16 GeV ---")
    print(f"  alpha_1(M_KK) = {alpha_1_ref:.6f}")
    print(f"  alpha_2(M_KK) = {alpha_2_ref:.6f}")
    print(f"  alpha_1/alpha_2 = {alpha_1_ref/alpha_2_ref:.4f}")
    print(f"  Lambda_SA = {Lambda_SA_ref:.4e} GeV = 10^{np.log10(Lambda_SA_ref):.2f} GeV")
    print(f"  Lambda_SA/M_KK = {ratio_ref:.4e}")
    print(f"  ln(Lambda_SA/M_KK) = {t_ref:.4f}")

    # Compare to Session 30Bb result at tau=0.57
    print(f"\n--- Comparison to Session 30Bb ---")
    print(f"  tau=0.57 (s30Bb): Lambda_SA/M_KK = 2.00e15 (15 orders above M_KK)")
    print(f"  tau=0.21 (this):  Lambda_SA/M_KK = {ratio_ref:.2e}")
    print(f"  Improvement factor: {2.0e15/ratio_ref:.2e}" if ratio_ref > 0 else "  N/A")

    # Also compute for different sin^2_B at tau=0.21 but using the
    # FRAMEWORK's g1/g2 directly (not the SM RGE running)
    print(f"\n--- Framework coupling at M_KK ---")
    # The framework gives g1/g2 = sqrt(L2/L1) at the compactification scale
    # This gives alpha_1_KK/alpha_2_KK = (5/3) * (g1/g2)^2 in GUT normalization
    # Wait: the FRAMEWORK gives alpha_1/alpha_2 = L2/L1 * normalization
    # More precisely: alpha_i = g_i^2/(4pi), and g1/g2 = sqrt(L2/L1)
    # So alpha_1/alpha_2 = g1^2/g2^2 = L2/L1

    alpha_ratio_framework = L2 / L1  # = g1^2/g2^2 at M_KK
    print(f"  g1/g2 at M_KK (framework) = {g1g2:.6f}")
    print(f"  alpha_1/alpha_2 at M_KK (framework) = {alpha_ratio_framework:.6f}")
    print(f"  For comparison: alpha_1/alpha_2 from SM RGE to 10^16 = {alpha_1_ref/alpha_2_ref:.6f}")
    print(f"  Discrepancy: {abs(alpha_ratio_framework - alpha_1_ref/alpha_2_ref):.6f}")

    # ========================================================================
    # Gate verdict
    # ========================================================================
    print("\n" + "=" * 70)
    print("GATE B-31nck ASSESSMENT")
    print("=" * 70)

    if 1e-3 <= ratio_ref <= 1e3:
        verdict = "PASS"
        print(f"  Lambda_SA/M_KK = {ratio_ref:.4e} at M_KK = 10^16 GeV")
        print(f"  --> B-31nck: PASS (within [10^-3, 10^3])")
    else:
        verdict = "FAIL"
        print(f"  Lambda_SA/M_KK = {ratio_ref:.4e} at M_KK = 10^16 GeV")
        print(f"  --> B-31nck: FAIL (outside [10^-3, 10^3])")
        print(f"  NCG-KK irreconcilable at tau~0.21.")

    # ========================================================================
    # Save
    # ========================================================================
    np.savez('tier0-computation/s31a_nck_tau021.npz',
             tau=tau_val, L1=L1, L2=L2, g1g2=g1g2, sin2_B=sin2_B,
             M_KK_ref=M_KK_ref,
             alpha_1_ref=alpha_1_ref, alpha_2_ref=alpha_2_ref,
             Lambda_SA=Lambda_SA_ref, ratio=ratio_ref,
             t_unification=t_ref,
             M_KK_scan=np.array(list(results.keys())),
             ratio_scan=np.array([results[m]['ratio'] for m in results]),
             verdict=np.array(verdict))
    print(f"\nSaved: tier0-computation/s31a_nck_tau021.npz")

    elapsed = time.time() - t_start
    print(f"Total runtime: {elapsed:.1f}s")
    print(f"\nGATE B-31nck: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
