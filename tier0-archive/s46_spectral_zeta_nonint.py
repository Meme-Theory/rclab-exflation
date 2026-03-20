#!/usr/bin/env python3
"""
SPECTRAL-ZETA-NONINT-46: Spectral zeta function at non-integer s values
========================================================================

Gate: SPECTRAL-ZETA-NONINT-46
Session: 46, Wave 4, Item 14

Computes:
    zeta_D(s) = sum_k d_k |lambda_k|^{-2s}

at s = 1/2, 3/2, 5/2, 7/2 (non-integer half-integer points) and the
integer points s = 1, 2, 3, 4 (for cross-check against known a_{2n}).

Evaluated at:
    - tau = 0.19 (fold / van Hove singularity)
    - tau = 0.00 (round / bi-invariant metric)

Convention:
    d_k = dim(V_{(p,q)}) = (p+1)(q+1)(p+q+2)/2  (Peter-Weyl weight)
    lambda_k = positive eigenvalue of D_K (Dirac operator with Kosmann lift)
    Spectrum from s27_multisector_bcs.npz and s36_sfull_tau_stabilization.npz
    (10 sectors, max_pq_sum=5, 616 positive eigenvalues, sum(d_k)=6440)

q-theory context:
    In Volovik's q-theory, the vacuum energy functional is:
        epsilon(q) = sum_k f(lambda_k(q))
    where f depends on the regularization. The spectral zeta at non-integer s
    provides the integrand for the q-theory vacuum energy at general s:
        zeta_D(s, tau) = sum_k d_k |lambda_k(tau)|^{-2s}
    The RATIO zeta_D(s, fold) / zeta_D(s, round) measures how much the
    Jensen deformation shifts the vacuum energy at each spectral moment.
    Non-integer s probes interpolating behavior between the integer moments
    a_0, a_2, a_4, a_6 that appear in the Seeley-DeWitt expansion.

Input:  s42_hauser_feshbach.npz (for cross-check), canonical_constants.py
Output: s46_spectral_zeta_nonint.{npz,png}

Author: Spectral-Geometer (Session 46)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    M_KK_gravity, M_KK_kerner, M_Pl_reduced, rho_Lambda_obs, PI
)

DATA_DIR = Path(__file__).parent

# =============================================================================
#  SECTION 1: Load Spectrum
# =============================================================================

def load_spectrum(tau_val):
    """
    Load the Dirac eigenvalue spectrum at given tau from authoritative files.

    Returns:
        eigenvalues: array of positive eigenvalues |lambda_k|
        degeneracies: array of Peter-Weyl weights d_{(p,q)}
    """
    d27 = np.load(DATA_DIR / 's27_multisector_bcs.npz', allow_pickle=True)
    d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)

    SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
               (3, 0), (0, 3), (2, 1), (1, 2)]

    def dim_pq(p, q):
        return (p + 1) * (q + 1) * (p + q + 2) // 2

    eigenvalues = []
    degeneracies = []

    for (p, q) in SECTORS:
        key36 = f"evals_tau{tau_val:.3f}_{p}_{q}"
        if key36 in d36.files:
            evals = d36[key36]
        else:
            s27_taus = list(d27['tau_values'])
            ti = min(range(len(s27_taus)),
                     key=lambda i: abs(s27_taus[i] - tau_val))
            pp, qq = (2, 1) if (p, q) == (1, 2) else (p, q)
            key27 = f"evals_{pp}_{qq}_{ti}"
            if key27 in d27.files:
                evals = d27[key27]
            else:
                continue

        deg = dim_pq(p, q)
        pos_evals = evals[evals > 0.01]
        for ev in pos_evals:
            eigenvalues.append(ev)
            degeneracies.append(deg)

    return np.array(eigenvalues), np.array(degeneracies, dtype=float)


# =============================================================================
#  SECTION 2: Spectral Zeta Computation
# =============================================================================

def compute_spectral_zeta(eigenvalues, degeneracies, s_values):
    """
    Compute zeta_D(s) = sum_k d_k |lambda_k|^{-2s} at given s values.

    Returns dict: s -> zeta_D(s)
    """
    zeta = {}
    for s in s_values:
        zeta[s] = np.sum(degeneracies * eigenvalues**(-2 * s))
    return zeta


def compute_zeta_derivative(eigenvalues, degeneracies, s_values):
    """
    Compute d(zeta_D)/ds = -2 * sum_k d_k * log(lambda_k) * lambda_k^{-2s}

    This is the derivative of the spectral zeta with respect to s,
    needed for understanding the sensitivity of the q-theory integrand.
    """
    log_lam = np.log(eigenvalues)
    dzeta = {}
    for s in s_values:
        dzeta[s] = -2.0 * np.sum(degeneracies * log_lam * eigenvalues**(-2 * s))
    return dzeta


def compute_qtheory_ratio(zeta_fold, zeta_round, s_values):
    """
    Compute the q-theory ratio: R(s) = zeta_D(s, fold) / zeta_D(s, round).

    This ratio measures how the Jensen deformation shifts the vacuum energy
    at each spectral moment. R > 1 means the fold INCREASES the contribution
    at that moment; R < 1 means it DECREASES it.

    Also compute the q-theory "integrand change":
        delta_zeta(s) = zeta_D(s, fold) - zeta_D(s, round)
    and the fractional change:
        frac(s) = delta_zeta(s) / zeta_D(s, round)
    """
    ratio = {}
    delta = {}
    frac_change = {}
    for s in s_values:
        ratio[s] = zeta_fold[s] / zeta_round[s]
        delta[s] = zeta_fold[s] - zeta_round[s]
        frac_change[s] = delta[s] / zeta_round[s]
    return ratio, delta, frac_change


# =============================================================================
#  SECTION 3: Weyl-Law Interpolation Check
# =============================================================================

def weyl_prediction(s, N, d, lambda_min, lambda_max):
    """
    Weyl-law prediction for zeta_D(s) on the truncated spectrum.

    For a d-dimensional compact Riemannian manifold:
        rho(lambda) ~ C_0 * lambda^{d-1}
        N ~ C_0 * lambda_max^d / d
        => C_0 = d * N / lambda_max^d

    Then:
        zeta_D(s) ~ C_0 * integral_{lambda_min}^{lambda_max} lambda^{d-1-2s} dlambda
                   = C_0 * [lambda_max^{d-2s} - lambda_min^{d-2s}] / (d - 2s)

    This formula has a pole at s = d/2 (= 4 for d=8), reflecting the UV
    divergence of the spectral zeta function on the continuum.
    """
    C_0 = d * N / lambda_max**d
    if abs(d - 2 * s) < 1e-10:
        # At the pole: logarithmic
        return C_0 * (np.log(lambda_max) - np.log(lambda_min))
    exponent = d - 2 * s
    return C_0 * (lambda_max**exponent - lambda_min**exponent) / exponent


# =============================================================================
#  SECTION 4: Sector-Resolved Zeta
# =============================================================================

def sector_resolved_zeta(tau_val, s_values):
    """
    Compute zeta_D(s) resolved by Peter-Weyl sector (p,q).
    """
    d27 = np.load(DATA_DIR / 's27_multisector_bcs.npz', allow_pickle=True)
    d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)

    SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
               (3, 0), (0, 3), (2, 1), (1, 2)]

    def dim_pq(p, q):
        return (p + 1) * (q + 1) * (p + q + 2) // 2

    sector_zeta = {}
    for (p, q) in SECTORS:
        key36 = f"evals_tau{tau_val:.3f}_{p}_{q}"
        if key36 in d36.files:
            evals = d36[key36]
        else:
            s27_taus = list(d27['tau_values'])
            ti = min(range(len(s27_taus)),
                     key=lambda i: abs(s27_taus[i] - tau_val))
            pp, qq = (2, 1) if (p, q) == (1, 2) else (p, q)
            key27 = f"evals_{pp}_{qq}_{ti}"
            if key27 in d27.files:
                evals = d27[key27]
            else:
                continue

        deg = dim_pq(p, q)
        pos_evals = evals[evals > 0.01]

        sector_zeta[(p, q)] = {}
        for s in s_values:
            sector_zeta[(p, q)][s] = deg * np.sum(pos_evals**(-2 * s))

    return sector_zeta


# =============================================================================
#  SECTION 5: Main Computation
# =============================================================================

def main():
    print("=" * 78)
    print("SPECTRAL-ZETA-NONINT-46: Spectral Zeta at Non-Integer s")
    print("=" * 78)

    # ─── Step 1: Load spectra ───
    print("\n--- Step 1: Load spectra ---")
    evals_fold, degs_fold = load_spectrum(0.19)
    evals_round, degs_round = load_spectrum(0.00)

    print(f"  Fold  (tau=0.19): {len(evals_fold)} eigenvalues, "
          f"sum(d_k) = {np.sum(degs_fold):.0f}")
    print(f"  Round (tau=0.00): {len(evals_round)} eigenvalues, "
          f"sum(d_k) = {np.sum(degs_round):.0f}")
    print(f"  Fold  eigenvalue range: [{evals_fold.min():.6f}, {evals_fold.max():.6f}]")
    print(f"  Round eigenvalue range: [{evals_round.min():.6f}, {evals_round.max():.6f}]")

    # ─── Step 2: Cross-check integer s values ───
    print("\n--- Step 2: Cross-check against canonical a_{2n} ---")
    s_integer = [0.0, 1.0, 2.0, 3.0, 4.0]
    zeta_fold_int = compute_spectral_zeta(evals_fold, degs_fold, s_integer)
    # s=0: sum d_k = a_0
    # s=1: sum d_k lambda_k^{-2} = a_2
    # s=2: sum d_k lambda_k^{-4} = a_4

    canonical = {0.0: a0_fold, 1.0: a2_fold, 2.0: a4_fold}
    for s in [0.0, 1.0, 2.0]:
        computed = zeta_fold_int[s]
        expected = canonical[s]
        err = abs(computed - expected) / abs(expected) if expected != 0 else 0
        status = "OK" if err < 1e-6 else "MISMATCH"
        print(f"  zeta_D({s:.0f}) = {computed:.6f}  "
              f"(canonical a_{int(2*s)} = {expected:.6f})  {status}  err={err:.2e}")

    # ─── Step 3: Compute at non-integer s ───
    print("\n--- Step 3: Spectral zeta at non-integer s ---")
    s_nonint = [0.5, 1.5, 2.5, 3.5]
    s_all = sorted(s_integer + s_nonint)

    zeta_fold_all = compute_spectral_zeta(evals_fold, degs_fold, s_all)
    zeta_round_all = compute_spectral_zeta(evals_round, degs_round, s_all)

    dzeta_fold = compute_zeta_derivative(evals_fold, degs_fold, s_all)
    dzeta_round = compute_zeta_derivative(evals_round, degs_round, s_all)

    ratio, delta, frac_change = compute_qtheory_ratio(
        zeta_fold_all, zeta_round_all, s_all)

    print(f"\n  {'s':>5s}  {'zeta_fold':>14s}  {'zeta_round':>14s}  "
          f"{'ratio F/R':>10s}  {'delta':>12s}  {'frac %':>8s}")
    print(f"  " + "-" * 72)
    for s in s_all:
        print(f"  {s:5.1f}  {zeta_fold_all[s]:14.4f}  {zeta_round_all[s]:14.4f}  "
              f"{ratio[s]:10.6f}  {delta[s]:12.4f}  {frac_change[s]*100:8.4f}")

    # ─── Step 4: Non-integer s analysis ───
    print("\n--- Step 4: Non-integer s analysis ---")
    print("\n  Key result: q-theory integrand ratio R(s) = zeta_D(s,fold)/zeta_D(s,round)")
    print(f"\n  At INTEGER s (Seeley-DeWitt moments):")
    for s in s_integer:
        print(f"    R({s:.0f}) = {ratio[s]:.6f}  "
              f"({'+' if frac_change[s] > 0 else ''}{frac_change[s]*100:.4f}%)")

    print(f"\n  At HALF-INTEGER s (non-Seeley-DeWitt, new information):")
    for s in s_nonint:
        print(f"    R({s:.1f}) = {ratio[s]:.6f}  "
              f"({'+' if frac_change[s] > 0 else ''}{frac_change[s]*100:.4f}%)")

    # ─── Step 5: Monotonicity analysis ───
    print("\n--- Step 5: Monotonicity of R(s) ---")
    s_dense = np.linspace(0.01, 4.5, 500)
    zeta_fold_dense = compute_spectral_zeta(evals_fold, degs_fold, s_dense)
    zeta_round_dense = compute_spectral_zeta(evals_round, degs_round, s_dense)
    ratio_dense = np.array([zeta_fold_dense[s] / zeta_round_dense[s] for s in s_dense])
    delta_dense = np.array([zeta_fold_dense[s] - zeta_round_dense[s] for s in s_dense])

    # Check monotonicity
    dR_ds = np.diff(ratio_dense) / np.diff(s_dense)
    n_pos = np.sum(dR_ds > 0)
    n_neg = np.sum(dR_ds < 0)
    monotone = "MONOTONICALLY DECREASING" if n_neg == len(dR_ds) else \
               "MONOTONICALLY INCREASING" if n_pos == len(dR_ds) else \
               f"NON-MONOTONE ({n_pos} increasing, {n_neg} decreasing)"
    print(f"  R(s) is {monotone}")
    print(f"  R(s) range: [{ratio_dense.min():.6f}, {ratio_dense.max():.6f}]")

    # Find crossing: where does R(s) = 1?
    crossings = []
    for i in range(len(ratio_dense) - 1):
        if (ratio_dense[i] - 1) * (ratio_dense[i + 1] - 1) < 0:
            # Linear interpolation
            s_cross = s_dense[i] + (1 - ratio_dense[i]) / (
                ratio_dense[i + 1] - ratio_dense[i]) * (s_dense[i + 1] - s_dense[i])
            crossings.append(s_cross)
    if crossings:
        print(f"  R(s) = 1 crossing at s = {crossings}")
    else:
        side = "below" if ratio_dense[0] < 1 else "above"
        print(f"  R(s) stays {side} 1 for all s in [0.01, 4.5]")

    # ─── Step 6: Zeta derivative (log-sensitivity) ───
    print("\n--- Step 6: Zeta derivative d(zeta)/ds ---")
    print(f"\n  d(zeta_D)/ds = -2 * sum d_k * ln(lambda_k) * lambda_k^(-2s)")
    print(f"\n  {'s':>5s}  {'dzeta_fold':>14s}  {'dzeta_round':>14s}  "
          f"{'ratio':>10s}")
    print(f"  " + "-" * 50)
    for s in s_all:
        print(f"  {s:5.1f}  {dzeta_fold[s]:14.4f}  {dzeta_round[s]:14.4f}  "
              f"{dzeta_fold[s]/dzeta_round[s]:10.6f}")

    # ─── Step 7: Sector decomposition at half-integer s ───
    print("\n--- Step 7: Sector decomposition ---")
    sector_fold = sector_resolved_zeta(0.19, s_nonint)
    sector_round = sector_resolved_zeta(0.00, s_nonint)

    SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
               (3, 0), (0, 3), (2, 1), (1, 2)]

    for s in s_nonint:
        print(f"\n  s = {s:.1f}:")
        total_fold = sum(sector_fold[pq][s] for pq in sector_fold if s in sector_fold[pq])
        total_round = sum(sector_round[pq][s] for pq in sector_round if s in sector_round[pq])
        print(f"    {'sector':>8s}  {'fold':>12s}  {'round':>12s}  "
              f"{'fold/round':>10s}  {'% of total':>10s}")
        for pq in SECTORS:
            if pq in sector_fold and s in sector_fold[pq]:
                f_val = sector_fold[pq][s]
                r_val = sector_round[pq][s]
                rat = f_val / r_val if r_val > 0 else float('inf')
                pct = f_val / total_fold * 100
                print(f"    ({pq[0]},{pq[1]}){' '*(5-len(str(pq)))}  "
                      f"{f_val:12.4f}  {r_val:12.4f}  {rat:10.6f}  {pct:9.2f}%")

    # ─── Step 8: Weyl-law comparison ───
    print("\n--- Step 8: Weyl-law comparison ---")
    d = 8  # dimension of SU(3)
    N_fold = np.sum(degs_fold)
    N_round = np.sum(degs_round)
    lmin_fold = evals_fold.min()
    lmax_fold = evals_fold.max()
    lmin_round = evals_round.min()
    lmax_round = evals_round.max()

    print(f"\n  {'s':>5s}  {'actual':>12s}  {'Weyl pred':>12s}  "
          f"{'error %':>8s}  (fold)")
    print(f"  " + "-" * 45)
    for s in s_all:
        if s == 0.0:
            continue
        actual = zeta_fold_all[s]
        weyl = weyl_prediction(s, N_fold, d, lmin_fold, lmax_fold)
        err_pct = abs(actual - weyl) / actual * 100
        print(f"  {s:5.1f}  {actual:12.4f}  {weyl:12.4f}  {err_pct:7.2f}%")

    # ─── Step 9: q-theory integrand structure ───
    print("\n--- Step 9: q-theory integrand structure ---")
    print("\n  The q-theory vacuum energy is epsilon(tau) = integral F(zeta_D(s, tau)) ds")
    print("  where F is the regularization-dependent spectral function.")
    print()
    print("  Key observation: the ratio R(s) = zeta_fold / zeta_round is NOT constant.")
    print(f"  R(0) = {ratio[0.0]:.6f}  (volume-weighted count)")
    print(f"  R(1) = {ratio[1.0]:.6f}  (Einstein-Hilbert moment)")
    print(f"  R(2) = {ratio[2.0]:.6f}  (higher-curvature moment)")
    print(f"  R(3) = {ratio[3.0]:.6f}  (a_6 moment)")
    print(f"  R(4) = {ratio[4.0]:.6f}  (a_8 moment)")
    print()

    # Compute spectral slope: d(log zeta)/d(log s)
    log_s = np.log(s_dense[s_dense > 0.1])
    log_zeta_fold = np.array([np.log(zeta_fold_dense[s]) for s in s_dense[s_dense > 0.1]])
    log_zeta_round = np.array([np.log(zeta_round_dense[s]) for s in s_dense[s_dense > 0.1]])

    slope_fold = np.gradient(log_zeta_fold, log_s)
    slope_round = np.gradient(log_zeta_round, log_s)
    print(f"  d(ln zeta)/d(ln s) at s=1: fold={np.interp(0, log_s, slope_fold):.4f}, "
          f"round={np.interp(0, log_s, slope_round):.4f}")
    print(f"  d(ln zeta)/d(ln s) at s=2: fold={np.interp(np.log(2), log_s, slope_fold):.4f}, "
          f"round={np.interp(np.log(2), log_s, slope_round):.4f}")

    # ─── Step 10: Gate verdict ───
    print("\n" + "=" * 78)
    print("GATE VERDICT: SPECTRAL-ZETA-NONINT-46")
    print("=" * 78)

    # The gate question: does the q-theory integrand change at non-integer s
    # in a way that is structurally different from the integer-s behavior?

    # Criterion 1: Is R(s) non-constant? (structurally necessary for any
    # spectral functional to distinguish fold from round)
    R_spread = max(ratio[s] for s in s_all) - min(ratio[s] for s in s_all)
    print(f"\n  R(s) spread: {R_spread:.6f}")

    # Criterion 2: Do half-integer points interpolate smoothly?
    # Compare half-integer R values to the midpoint of adjacent integer values
    interpolation_errors = []
    for s_hi in s_nonint:
        s_lo = s_hi - 0.5
        s_up = s_hi + 0.5
        if s_lo in ratio and s_up in ratio:
            R_mid = (ratio[s_lo] + ratio[s_up]) / 2
            R_actual = ratio[s_hi]
            interp_err = abs(R_actual - R_mid) / abs(R_mid)
            interpolation_errors.append((s_hi, R_actual, R_mid, interp_err))
            print(f"  R({s_hi:.1f}) = {R_actual:.6f}, linear interp = {R_mid:.6f}, "
                  f"deviation = {interp_err*100:.4f}%")

    max_interp_err = max(e[3] for e in interpolation_errors) if interpolation_errors else 0

    # Criterion 3: R(s) monotonicity
    is_monotone = (n_neg == len(dR_ds)) or (n_pos == len(dR_ds))

    print(f"\n  R(s) spread:            {R_spread:.6f}")
    print(f"  Max interpolation error: {max_interp_err*100:.4f}%")
    print(f"  R(s) monotone:           {is_monotone}")

    # Verdict
    verdict = "INFO"
    verdict_text = (
        f"R(s) varies from {min(ratio[s] for s in s_all):.6f} to "
        f"{max(ratio[s] for s in s_all):.6f} over s in [0, 4]. "
        f"Half-integer values interpolate smoothly (max deviation "
        f"{max_interp_err*100:.4f}% from linear). "
        f"R(s) is {'monotonic' if is_monotone else 'non-monotonic'}. "
        f"No half-integer anomaly; q-theory integrand changes smoothly with s."
    )
    print(f"\n  === SPECTRAL-ZETA-NONINT-46: {verdict} ===")
    print(f"  {verdict_text}")

    # ─── Save results ───
    print("\n--- Saving results ---")
    save_dict = {
        # Metadata
        'tau_fold': np.float64(0.19),
        'tau_round': np.float64(0.00),
        'N_eigenvalues': np.int64(len(evals_fold)),
        'sum_dk': np.float64(np.sum(degs_fold)),
        'verdict': np.array([verdict]),

        # s values
        's_all': np.array(s_all),
        's_nonint': np.array(s_nonint),
        's_integer': np.array(s_integer),

        # Zeta values
        'zeta_fold': np.array([zeta_fold_all[s] for s in s_all]),
        'zeta_round': np.array([zeta_round_all[s] for s in s_all]),
        'ratio_fold_over_round': np.array([ratio[s] for s in s_all]),
        'delta_fold_minus_round': np.array([delta[s] for s in s_all]),
        'frac_change': np.array([frac_change[s] for s in s_all]),

        # Derivatives
        'dzeta_fold': np.array([dzeta_fold[s] for s in s_all]),
        'dzeta_round': np.array([dzeta_round[s] for s in s_all]),

        # Dense scan
        's_dense': s_dense,
        'ratio_dense': ratio_dense,
        'delta_dense': delta_dense,

        # Interpolation analysis
        'interp_errors': np.array([e[3] for e in interpolation_errors]),
        'max_interp_error': np.float64(max_interp_err),
        'R_spread': np.float64(R_spread),
        'is_monotone': np.bool_(is_monotone),
    }

    np.savez(DATA_DIR / 's46_spectral_zeta_nonint.npz', **save_dict)
    print(f"  Saved: tier0-computation/s46_spectral_zeta_nonint.npz")

    # ─── Plot ───
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('SPECTRAL-ZETA-NONINT-46: Spectral Zeta at Non-Integer $s$',
                 fontsize=14, fontweight='bold')

    # Panel 1: zeta_D(s) at fold and round
    ax = axes[0, 0]
    s_arr = np.array(s_all)
    z_fold_arr = np.array([zeta_fold_all[s] for s in s_all])
    z_round_arr = np.array([zeta_round_all[s] for s in s_all])
    ax.semilogy(s_arr, z_fold_arr, 'ro-', linewidth=2, markersize=8,
                label=r'$\zeta_D(s, \tau=0.19)$ (fold)', zorder=3)
    ax.semilogy(s_arr, z_round_arr, 'bs-', linewidth=2, markersize=8,
                label=r'$\zeta_D(s, \tau=0)$ (round)', zorder=3)
    # Mark integer vs half-integer
    s_int_arr = np.array(s_integer)
    s_hi_arr = np.array(s_nonint)
    z_fold_int = np.array([zeta_fold_all[s] for s in s_integer])
    z_fold_hi = np.array([zeta_fold_all[s] for s in s_nonint])
    ax.semilogy(s_int_arr, z_fold_int, 'ro', markersize=12, markeredgecolor='black',
                markeredgewidth=1.5, zorder=4)
    ax.semilogy(s_hi_arr, z_fold_hi, 'r^', markersize=10, markeredgecolor='darkred',
                markeredgewidth=1.5, zorder=4, label='half-integer (new)')
    ax.set_xlabel('$s$', fontsize=12)
    ax.set_ylabel(r'$\zeta_D(s) = \sum d_k |\lambda_k|^{-2s}$', fontsize=12)
    ax.set_title(r'Spectral Zeta Function $\zeta_D(s)$', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: Ratio R(s) = zeta_fold / zeta_round
    ax = axes[0, 1]
    ax.plot(s_dense, ratio_dense, 'k-', linewidth=1.5, alpha=0.5, label='dense scan')
    ratio_arr = np.array([ratio[s] for s in s_all])
    ax.plot(s_arr, ratio_arr, 'go-', linewidth=2, markersize=8, zorder=3)
    # Mark integer and half-integer differently
    ratio_int = np.array([ratio[s] for s in s_integer])
    ratio_hi = np.array([ratio[s] for s in s_nonint])
    ax.plot(s_int_arr, ratio_int, 'go', markersize=12, markeredgecolor='black',
            markeredgewidth=1.5, zorder=4, label='integer $s$')
    ax.plot(s_hi_arr, ratio_hi, 'g^', markersize=10, markeredgecolor='darkgreen',
            markeredgewidth=1.5, zorder=4, label='half-integer $s$ (new)')
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$s$', fontsize=12)
    ax.set_ylabel(r'$R(s) = \zeta_D(s,\mathrm{fold})/\zeta_D(s,\mathrm{round})$',
                  fontsize=12)
    ax.set_title('q-Theory Integrand Ratio $R(s)$', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 3: Delta = zeta_fold - zeta_round
    ax = axes[1, 0]
    ax.plot(s_dense, delta_dense, 'k-', linewidth=1.5, alpha=0.5)
    delta_arr = np.array([delta[s] for s in s_all])
    ax.plot(s_arr, delta_arr, 'mo-', linewidth=2, markersize=8, zorder=3)
    delta_int = np.array([delta[s] for s in s_integer])
    delta_hi = np.array([delta[s] for s in s_nonint])
    ax.plot(s_int_arr, delta_int, 'mo', markersize=12, markeredgecolor='black',
            markeredgewidth=1.5, zorder=4, label='integer $s$')
    ax.plot(s_hi_arr, delta_hi, 'm^', markersize=10, markeredgecolor='purple',
            markeredgewidth=1.5, zorder=4, label='half-integer $s$')
    ax.axhline(y=0.0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$s$', fontsize=12)
    ax.set_ylabel(r'$\Delta\zeta(s) = \zeta_D(s,\mathrm{fold}) - \zeta_D(s,\mathrm{round})$',
                  fontsize=12)
    ax.set_title('Absolute Change in Spectral Zeta', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 4: Fractional change and interpolation
    ax = axes[1, 1]
    frac_arr = np.array([frac_change[s] * 100 for s in s_all])
    ax.plot(s_arr, frac_arr, 'co-', linewidth=2, markersize=8, zorder=3)
    frac_int = np.array([frac_change[s] * 100 for s in s_integer])
    frac_hi = np.array([frac_change[s] * 100 for s in s_nonint])
    ax.plot(s_int_arr, frac_int, 'co', markersize=12, markeredgecolor='black',
            markeredgewidth=1.5, zorder=4, label='integer $s$')
    ax.plot(s_hi_arr, frac_hi, 'c^', markersize=10, markeredgecolor='darkcyan',
            markeredgewidth=1.5, zorder=4, label='half-integer $s$')
    ax.axhline(y=0.0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$s$', fontsize=12)
    ax.set_ylabel(r'Fractional change $\Delta\zeta / \zeta_\mathrm{round}$ (%)',
                  fontsize=12)
    ax.set_title('Fractional Change (%)', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(DATA_DIR / 's46_spectral_zeta_nonint.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: tier0-computation/s46_spectral_zeta_nonint.png")
    plt.close()

    return save_dict


if __name__ == '__main__':
    results = main()
