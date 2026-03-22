"""
Session 28b Computation 8: E-5 Cosmological Constant from Condensation Energy
==============================================================================

Converts the BCS condensation free energy F_total at the interior minimum
from code units (dimensionless, in units of the Dirac operator eigenvalues)
to physical units and compares with the observed cosmological constant.

PHYSICS:
    The BCS condensation energy on the internal manifold M^6 = SU(3)
    contributes to the effective 4D cosmological constant:

        rho_Lambda = F_total * M_KK^4

    where M_KK is the Kaluza-Klein compactification scale, and F_total is
    dimensionless (eigenvalues are measured in units of 1/R where R is the
    SU(3) radius, so M_KK ~ 1/R).

    The observed cosmological constant energy density is:

        rho_Lambda^{obs} = 5.35e-47 GeV^4     (from Planck 2018)

    or equivalently Lambda_obs ~ (2.25 meV)^4.

    The question is: what ratio Sigma = rho_Lambda / rho_Lambda^{obs}?

    If Sigma >> 1 (e.g. 10^{60-120}): standard CC problem inherited.
    If Sigma ~ O(1): partial solution (extremely unlikely, would be major).
    If Sigma << 1: condensation energy negligible compared to CC.

SUBTLETY: DIMENSIONLESS F_total AND UNIT CONVERSION
    The Dirac eigenvalues in our computation are dimensionless numbers
    (they are eigenvalues of D_K / M_KK, where D_K has dimensions of
    inverse length and M_KK = 1/R is the KK mass scale).

    The BCS free energy F_cond has dimensions of [eigenvalue]^1 in our
    formalism (see s27 script: F_kin = -sum(E_paired - E_normal) where
    E = sqrt(xi^2 + Delta^2), xi and Delta in eigenvalue units).

    When we sum F_total = sum mult * F_cond, this is still in eigenvalue units.

    Physical energy density on the internal space:

        rho_6D = F_total * M_KK    (energy per KK volume unit)

    To get 4D energy density, we need:

        rho_4D = rho_6D * Vol(M^6)^{-1} = F_total * M_KK / Vol(M^6)

    But M_KK ~ 1/R and Vol(SU(3)) ~ R^8 (dimension 8), so:

        rho_4D = F_total * M_KK^{dim+1} = F_total * M_KK^9   (WRONG: overcounts)

    Actually the correct dimensional analysis for the spectral action:

        S = Tr f(D/Lambda) ~ sum_n f(lambda_n/Lambda)

    The spectral action gives a dimensionless action. The BCS gap equation
    was solved in the eigenvalue basis, giving F in "eigenvalue units".

    Since eigenvalues have dimension [mass] and F ~ sum(E_n), we get:

        F_physical = F_total * M_KK    (in natural units, GeV)

    But this is the total free energy, not an energy density. To get an
    energy density (for the CC), we divide by the spatial volume V_3:

        rho_Lambda = F_total * M_KK / V_3

    This is frame-dependent and not meaningful as stated. Instead, the
    spectral action formalism gives the action directly:

        S_eff = F_total * (M_KK / Lambda_cutoff)

    For a more robust estimate, we simply note:

        The natural scale of the condensation energy is F_total * M_KK.
        This energy density in the 4D EFT is ~ F_total * M_KK^4 / (something).

    SIMPLEST ESTIMATE (order-of-magnitude):
        rho_Lambda ~ |F_total| * M_KK^4

    This is the standard KK-reduction estimate where each mode contributes
    O(M_KK^4) to the vacuum energy. The factor F_total/N_modes gives the
    BCS suppression.

DATA:
    - S27: F_total(tau=0.35, mu/lmin=1.20) = -18.56 (code units)
    - Interior minimum value from s28b computation 6

OUTPUT:
    s28b_lambda_eff.txt: order-of-magnitude comparison table

GATE E-5: Diagnostic only. Reports the CC problem severity.

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28b, Computation 8
"""

import os
import sys
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ===========================================================================
# PHYSICAL CONSTANTS (natural units, hbar = c = 1)
# ===========================================================================

# Planck mass
M_PL = 1.2209e19       # GeV (reduced Planck mass is M_PL / sqrt(8pi) = 2.435e18)
M_PL_REDUCED = 2.435e18  # GeV

# Newton's constant: G_N = 1 / M_PL^2 (in natural units)
# 8*pi*G_N = 1 / M_PL_REDUCED^2

# Observed cosmological constant energy density
# Lambda_obs = 3 * H_0^2 * Omega_Lambda / (8*pi*G)
# rho_Lambda = Lambda / (8*pi*G) = 5.35e-47 GeV^4 (Planck 2018)
RHO_LAMBDA_OBS = 5.35e-47  # GeV^4

# For reference: (2.25 meV)^4 = (2.25e-3 * 1e-3)^4 = (2.25e-6)^4 GeV^4
# = 2.56e-23 GeV^4 -- this is a different convention (Lambda itself, not rho)
LAMBDA_OBS_SCALE = 2.25e-3  # meV -> (2.25 meV)^4 in GeV^4 = (2.25e-6 GeV)^4

# KK compactification scales to scan
M_KK_VALUES = np.array([1e14, 1e15, 1e16, 1e17, 1e18])  # GeV


# ===========================================================================
# LOAD S27 DATA
# ===========================================================================

def load_data():
    """Load S27 BCS data and extract F_total at interior minimum.

    Returns:
        F_at_min: float, F_total at interior minimum
        tau_min: float, tau at minimum
        mu_min: float, mu/lambda_min at minimum
        F_total_grid: (n_tau, n_mu) full grid
        tau_values: (n_tau,)
        mu_ratios: (n_mu,)
    """
    path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    d = np.load(path, allow_pickle=True)

    tau = d['tau_values']
    mu = d['mu_ratios']
    F = d['F_total']  # (9, 12) = (tau, mu)

    # Find the interior minimum (tau > 0 and tau < tau_max)
    # Scan all interior points
    best_F = 0.0
    best_ti = -1
    best_mi = -1

    for ti in range(1, len(tau) - 1):  # Exclude boundaries
        for mi in range(len(mu)):
            if np.isfinite(F[ti, mi]) and F[ti, mi] < best_F:
                best_F = F[ti, mi]
                best_ti = ti
                best_mi = mi

    if best_ti < 0:
        # No interior minimum with F < 0; use global
        flat_idx = np.argmin(np.where(np.isfinite(F), F, 0.0))
        best_ti, best_mi = np.unravel_index(flat_idx, F.shape)
        best_F = F[best_ti, best_mi]
        print(f"  WARNING: No interior minimum found. Using global min at boundary.")

    return {
        'F_at_min': best_F,
        'tau_min': tau[best_ti],
        'mu_min': mu[best_mi],
        'F_total': F,
        'tau_values': tau,
        'mu_ratios': mu,
        'sectors': d['sectors'],
        'F_cond': d['F_cond'],
        'lambda_min': d['lambda_min'],
    }


# ===========================================================================
# COSMOLOGICAL CONSTANT ESTIMATE
# ===========================================================================

def compute_lambda_eff(F_total_code, M_KK):
    r"""Convert dimensionless BCS condensation energy to 4D energy density.

    The simplest (and most conservative) estimate:

        rho_Lambda^{BCS} = |F_total| * M_KK^4

    This assumes:
    1. F_total is the dimensionless spectral sum (eigenvalue units)
    2. Each eigenvalue lambda_n has physical dimension M_KK (= 1/R)
    3. The BCS energy contributes at 1-loop level to the 4D vacuum energy
    4. KK reduction: rho_4D = integral over M^6 of rho_6D ~ F * M_KK^4
       (the factor M_KK^4 comes from [energy]^4 needed for energy density)

    NOTE: This is an ORDER-OF-MAGNITUDE estimate. The precise coefficient
    depends on the KK reduction, zero-mode wavefunctions, etc.

    Parameters:
        F_total_code: dimensionless BCS condensation energy (< 0 for condensate)
        M_KK: KK mass scale in GeV

    Returns:
        rho_BCS: effective energy density in GeV^4
        ratio: rho_BCS / rho_Lambda_obs
        log_ratio: log10(|ratio|)
    """
    # The BCS free energy is F < 0 (attractive). The vacuum energy contribution
    # is Delta_rho = F_total * M_KK^4 < 0 (lowers vacuum energy).
    rho_BCS = F_total_code * M_KK**4  # GeV^4, negative

    ratio = rho_BCS / RHO_LAMBDA_OBS

    # For the logarithmic comparison, use absolute values
    log_ratio = np.log10(abs(ratio)) if ratio != 0 else float('-inf')

    return rho_BCS, ratio, log_ratio


def compute_sector_contributions(data, M_KK):
    """Compute per-sector vacuum energy contributions at the interior minimum.

    Parameters:
        data: dict from load_data
        M_KK: reference KK scale in GeV

    Returns:
        list of dicts with sector info
    """
    sectors = data['sectors']
    F_cond = data['F_cond']  # (9, 9, 12)
    tau = data['tau_values']
    mu = data['mu_ratios']

    # Find tau and mu indices for interior minimum
    ti = np.argmin(np.abs(tau - data['tau_min']))
    mi = np.argmin(np.abs(mu - data['mu_min']))

    contribs = []
    for si in range(len(sectors)):
        p, q, dim_rho, mult = sectors[si]
        # (2,1) gets doubled for CPT conjugate
        eff_mult = 450 if (p == 2 and q == 1) else mult
        f_cond = F_cond[si, ti, mi]
        f_total_sector = eff_mult * f_cond

        rho_sector = f_total_sector * M_KK**4

        contribs.append({
            'p': p, 'q': q, 'dim': dim_rho, 'mult': eff_mult,
            'F_cond': f_cond,
            'F_sector': f_total_sector,
            'rho_sector': rho_sector,
        })

    return contribs


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=" * 78)
    print("28b-8 E-5 Cosmological Constant from Condensation Energy")
    print("=" * 78)
    print()

    # 1. Load data
    print("Loading S27 BCS data...")
    data = load_data()
    F_min = data['F_at_min']
    tau_min = data['tau_min']
    mu_min = data['mu_min']
    print(f"  Interior minimum: F_total = {F_min:.4f} at tau={tau_min:.2f}, mu/lmin={mu_min:.2f}")

    # Also report global minimum for comparison
    F_all = data['F_total']
    F_safe = np.where(np.isfinite(F_all), F_all, 0.0)
    glob_idx = np.unravel_index(np.argmin(F_safe), F_all.shape)
    F_glob = F_all[glob_idx]
    print(f"  Global minimum:   F_total = {F_glob:.4f} at tau={data['tau_values'][glob_idx[0]]:.2f}, "
          f"mu/lmin={data['mu_ratios'][glob_idx[1]]:.2f}")
    print()

    # 2. Physical constants
    print("Physical constants:")
    print(f"  M_Pl (full)    = {M_PL:.4e} GeV")
    print(f"  M_Pl (reduced) = {M_PL_REDUCED:.4e} GeV")
    print(f"  rho_Lambda_obs = {RHO_LAMBDA_OBS:.3e} GeV^4")
    print(f"  (2.25 meV)^4   = {(2.25e-6)**4:.3e} GeV^4")
    print()

    # 3. Compute Lambda_eff at each M_KK
    print("=" * 78)
    print("COSMOLOGICAL CONSTANT ESTIMATE: rho_BCS = F_total * M_KK^4")
    print("=" * 78)
    print()
    print(f"{'M_KK (GeV)':>14s} {'rho_BCS (GeV^4)':>20s} {'rho/rho_obs':>15s} "
          f"{'log10|ratio|':>14s} {'Orders too large':>18s}")
    print("-" * 85)

    results = []
    for M_KK in M_KK_VALUES:
        rho_BCS, ratio, log_ratio = compute_lambda_eff(F_min, M_KK)
        excess_orders = log_ratio
        results.append({
            'M_KK': M_KK,
            'rho_BCS': rho_BCS,
            'ratio': ratio,
            'log_ratio': log_ratio,
        })
        print(f"  {M_KK:14.0e} {rho_BCS:20.4e} {ratio:15.4e} {log_ratio:14.1f} {excess_orders:18.0f}")

    print()

    # Reference: M_KK = M_GUT ~ 2e16 GeV (typical GUT/compactification scale)
    M_KK_REF = 2e16
    rho_ref, ratio_ref, log_ref = compute_lambda_eff(F_min, M_KK_REF)
    print(f"Reference (M_KK = M_GUT = 2e16 GeV):")
    print(f"  rho_BCS  = {rho_ref:.4e} GeV^4")
    print(f"  ratio    = {ratio_ref:.4e}")
    print(f"  log10    = {log_ref:.1f}")
    print(f"  EXCESS   = {log_ref:.0f} orders of magnitude")
    print()

    # 4. Comparison with standard CC problem
    print("=" * 78)
    print("COMPARISON WITH STANDARD CC PROBLEM")
    print("=" * 78)
    print()
    print("Standard CC problem (zero-point energy):")
    print(f"  rho_ZPE ~ M_Pl^4 = ({M_PL:.2e})^4 = {M_PL**4:.2e} GeV^4")
    print(f"  rho_ZPE / rho_obs = {M_PL**4 / RHO_LAMBDA_OBS:.2e}")
    print(f"  = 10^{np.log10(M_PL**4 / RHO_LAMBDA_OBS):.0f} (the famous 120 orders)")
    print()

    # BCS contribution relative to zero-point
    print(f"BCS condensation contribution (at M_KK = 2e16 GeV):")
    print(f"  rho_BCS / M_Pl^4 = {rho_ref / M_PL**4:.2e}")
    print(f"  = (M_KK/M_Pl)^4 * F_total = ({M_KK_REF/M_PL:.2e})^4 * {F_min:.2f}")
    print(f"  = {(M_KK_REF/M_PL)**4:.2e} * {F_min:.2f}")
    print(f"  = {(M_KK_REF/M_PL)**4 * F_min:.2e}")
    print()
    print(f"The BCS condensation energy is NEGATIVE (F < 0), so it partially")
    print(f"cancels the positive zero-point energy. But the cancellation would")
    print(f"need to be precise to 1 part in 10^{log_ref:.0f} to match rho_obs.")
    print()

    # 5. Suppression factor analysis
    print("=" * 78)
    print("SUPPRESSION FACTOR ANALYSIS")
    print("=" * 78)
    print()
    # Total number of modes contributing
    sectors = data['sectors']
    total_modes = sum(s[2] * 16 for s in sectors)  # dim_rho * 16 (spinor dim)
    total_mult_modes = sum(s[3] * s[2] * 16 for s in sectors)
    print(f"Total spinor modes (per sector): {total_modes}")
    print(f"Total mult-weighted modes: {total_mult_modes}")
    print(f"F_total / total_modes = {F_min / total_modes:.6f}")
    print(f"|F_per_mode| = {abs(F_min / total_modes):.6f} eigenvalue units")
    print()

    # The BCS condensation selects only a few modes near the Fermi surface
    # This gives a suppression relative to the full zero-point energy
    print(f"BCS selects modes near mu ~ lambda_min. Suppression relative to")
    print(f"N_modes * lambda_min: F_total / (N_modes * lambda_min_avg) =")
    lmin_avg = np.mean(data['lambda_min'][:, np.argmin(np.abs(data['tau_values'] - tau_min))])
    print(f"  lambda_min_avg at tau={tau_min:.2f}: {lmin_avg:.4f}")
    print(f"  F_total / (N_mult * lmin) = {F_min / (total_mult_modes * lmin_avg):.6e}")
    print()

    # What M_KK would be needed to match rho_obs?
    # |F_min| * M_KK^4 = rho_obs => M_KK = (rho_obs / |F_min|)^{1/4}
    M_KK_needed = (RHO_LAMBDA_OBS / abs(F_min))**0.25
    print(f"M_KK needed to match rho_Lambda_obs:")
    print(f"  M_KK = (rho_obs / |F_total|)^(1/4) = ({RHO_LAMBDA_OBS:.2e} / {abs(F_min):.2f})^(1/4)")
    print(f"  M_KK = {M_KK_needed:.4e} GeV = {M_KK_needed*1e3:.4e} MeV")
    print(f"  This is ~ {M_KK_needed:.1e} GeV, in the sub-eV range.")
    print(f"  Unphysical for KK compactification (would give sub-mm extra dimensions).")
    print()

    # 6. Per-sector breakdown
    print("=" * 78)
    print("PER-SECTOR BREAKDOWN (M_KK = 2e16 GeV)")
    print("=" * 78)
    contribs = compute_sector_contributions(data, M_KK_REF)
    print(f"{'Sector':>8s} {'dim':>4s} {'mult':>5s} {'F_cond':>12s} "
          f"{'F_sector':>12s} {'rho (GeV^4)':>16s} {'% of total':>10s}")
    print("-" * 75)
    total_F = sum(c['F_sector'] for c in contribs)
    for c in contribs:
        pct = 100 * c['F_sector'] / total_F if total_F != 0 else 0
        print(f"  ({c['p']},{c['q']}) {c['dim']:>4d} {c['mult']:>5d} "
              f"{c['F_cond']:12.6f} {c['F_sector']:12.4f} "
              f"{c['rho_sector']:16.4e} {pct:10.1f}%")
    print("-" * 75)
    print(f"  {'Total':>8s} {'':>4s} {'':>5s} {'':>12s} {total_F:12.4f} "
          f"{total_F * M_KK_REF**4:16.4e} {'100.0':>10s}%")
    print()

    # 7. Gate verdict
    print("=" * 78)
    print("GATE E-5 VERDICT (Diagnostic)")
    print("=" * 78)
    print()
    print(f"  F_total at interior minimum = {F_min:.4f} (code units)")
    print(f"  At M_KK = 2e16 GeV: rho_BCS = {rho_ref:.4e} GeV^4")
    print(f"  Ratio to observed:  {ratio_ref:.4e} ({log_ref:.0f} orders too large)")
    print()

    if log_ref > 50:
        verdict = "STANDARD CC PROBLEM INHERITED"
        print(f"  VERDICT: {verdict}")
        print(f"  The BCS condensation energy inherits the standard cosmological")
        print(f"  constant problem. At GUT-scale compactification, the BCS vacuum")
        print(f"  energy is ~10^{log_ref:.0f} times larger than observed.")
        print(f"  This is comparable to (but smaller than) the Planck-scale CC")
        print(f"  problem (10^120). The deficit is (M_KK/M_Pl)^4 ~ {(M_KK_REF/M_PL)**4:.0e}.")
    elif log_ref > 10:
        verdict = "PARTIAL CC PROBLEM"
        print(f"  VERDICT: {verdict}")
        print(f"  BCS condensation reduces the CC problem from 120 orders to {log_ref:.0f}.")
    elif log_ref < 3:
        verdict = "CC PROBLEM RESOLVED (!!)"
        print(f"  VERDICT: {verdict}")
        print(f"  BCS condensation energy is within 3 orders of rho_obs.")
    else:
        verdict = f"CC MISMATCH: {log_ref:.0f} orders"
        print(f"  VERDICT: {verdict}")

    print()
    print(f"  NOTE: This is DIAGNOSTIC ONLY. The BCS condensation energy does NOT")
    print(f"  solve the CC problem. It contributes one additional term to the")
    print(f"  vacuum energy budget, at the same scale as other KK-mode contributions.")
    print(f"  The CC problem requires a cancellation mechanism (not provided here).")

    # 8. Save text output
    txt_path = os.path.join(SCRIPT_DIR, "s28b_lambda_eff.txt")
    with open(txt_path, 'w') as f:
        f.write("=" * 78 + "\n")
        f.write("28b-8 E-5 Cosmological Constant from Condensation Energy\n")
        f.write("=" * 78 + "\n\n")

        f.write(f"BCS interior minimum: F_total = {F_min:.4f} at tau={tau_min:.2f}, mu/lmin={mu_min:.2f}\n")
        f.write(f"Observed rho_Lambda = {RHO_LAMBDA_OBS:.3e} GeV^4\n\n")

        f.write(f"{'M_KK (GeV)':>14s} {'rho_BCS (GeV^4)':>20s} {'rho/rho_obs':>15s} "
                f"{'log10|ratio|':>14s}\n")
        f.write("-" * 65 + "\n")
        for r in results:
            f.write(f"  {r['M_KK']:14.0e} {r['rho_BCS']:20.4e} {r['ratio']:15.4e} "
                    f"{r['log_ratio']:14.1f}\n")

        f.write(f"\nReference (M_KK = 2e16 GeV):\n")
        f.write(f"  rho_BCS = {rho_ref:.4e} GeV^4\n")
        f.write(f"  ratio   = {ratio_ref:.4e}\n")
        f.write(f"  Excess  = {log_ref:.0f} orders of magnitude\n\n")

        f.write(f"M_KK needed for rho_BCS = rho_obs: {M_KK_needed:.4e} GeV (unphysical)\n\n")

        f.write(f"VERDICT: {verdict}\n")
        f.write(f"  BCS condensation inherits the standard CC problem.\n")
        f.write(f"  At GUT scale: {log_ref:.0f} orders too large.\n")
        f.write(f"  At Planck scale: {np.log10(abs(F_min * M_PL**4 / RHO_LAMBDA_OBS)):.0f} orders too large.\n")

    print(f"\nText output saved: {txt_path}")
    print(f"\n{'='*78}")
    print(f"FINAL VERDICT E-5: {verdict}")
    print(f"{'='*78}")


if __name__ == "__main__":
    main()
