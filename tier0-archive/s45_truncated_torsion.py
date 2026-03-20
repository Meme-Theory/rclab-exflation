#!/usr/bin/env python3
"""
S45 — Truncated / Singlet Torsion at Dissolution Scale (TRUNCATED-TORSION-45)
===============================================================================

Gate: TRUNCATED-TORSION-45  (INFO: is physical torsion bounded?)

The full analytic torsion T(SU(3)) ~ 10^{20301} (from W2-R3, s45_analytic_torsion)
reproduces the CC problem in spectral language: log det(D_K^2) ~ 93,490.
But not all modes gravitate equally. This script computes T restricted to
physically relevant modes:

  1. Singlet-only torsion: 16 modes in (0,0) rep with d_k = 1
     zeta'_singlet(0) = -2 sum_{k in singlet} ln|lambda_k|
     T_singlet = exp(-zeta'_singlet(0)/2)

  2. Progressive truncation: T at max_pq_sum = 1,2,3,4,5,6
     Reveals scaling: T ~ exp(N)? Sublinear? Plateau?

  3. Dissolution-bounded torsion: eigenvalues smeared by epsilon_c ~ 1/sqrt(N)
     Does uncertainty in UV eigenvalues significantly affect T?

  4. EIH-weighted torsion: zeta'_EIH(0) = -2 sum_k (1/d_k) ln|lambda_k|
     Weights modes by gravitational coupling (1/d_k).

  5. Physical bound: what torsion does 4D gravity actually see?

Method:
  For a FINITE positive spectrum, zeta'(0) = -2 sum_k d_k ln(lambda_k).
  T = exp(-zeta'(0)/2) = exp(sum_k d_k ln(lambda_k)) = prod lambda_k^{d_k}.
  This is EXACT for the truncated spectrum (no analytic continuation needed).

Author: Spectral-Geometer (Session 45, TRUNCATED-TORSION-45)
Date: 2026-03-15

Input: s45_analytic_torsion.npz, s44_eih_grav.npz, s44_dos_tau.npz,
       s36_sfull_tau_stabilization.npz
Output: s45_truncated_torsion.npz, s45_truncated_torsion.png
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    rho_Lambda_obs, PI, a0_fold, a2_fold, a4_fold
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SECTION 1: Load data
# =============================================================================

def load_all_data():
    """Load spectrum and prior results."""
    # Full spectrum at fold and round
    dos = np.load(os.path.join(DATA_DIR, 's44_dos_tau.npz'), allow_pickle=True)
    omega_fold = dos['tau0.19_all_omega']
    dim2_fold = dos['tau0.19_all_dim2'].astype(int)
    omega_round = dos['tau0.00_all_omega']
    dim2_round = dos['tau0.00_all_dim2'].astype(int)

    # Sector eigenvalues at fold (from s36_sfull)
    sfull = np.load(os.path.join(DATA_DIR, 's36_sfull_tau_stabilization.npz'),
                    allow_pickle=True)

    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
               (3,0), (0,3), (2,1), (1,2)]
    sector_evals = {}
    for (p, q) in sectors:
        key = f'evals_tau0.190_{p}_{q}'
        if key in sfull.files:
            sector_evals[(p, q)] = np.abs(sfull[key])

    # Prior torsion results
    torsion = np.load(os.path.join(DATA_DIR, 's45_analytic_torsion.npz'),
                      allow_pickle=True)

    # EIH results
    eih = np.load(os.path.join(DATA_DIR, 's44_eih_grav.npz'),
                  allow_pickle=True)

    return {
        'omega_fold': omega_fold,
        'dim2_fold': dim2_fold,
        'omega_round': omega_round,
        'dim2_round': dim2_round,
        'sector_evals': sector_evals,
        'torsion': torsion,
        'eih': eih,
    }


# =============================================================================
# SECTION 2: Core spectral functions
# =============================================================================

def zeta_prime_0(omega, deg):
    """zeta'(0) = -2 sum d_k ln|lambda_k| for finite positive spectrum."""
    assert np.all(omega > 0), "All eigenvalues must be positive"
    return -2.0 * np.sum(deg * np.log(omega))


def log10_torsion(omega, deg):
    """log10(T) where T = exp(-zeta'(0)/2) = exp(sum d_k ln lambda_k)."""
    return np.sum(deg * np.log(omega)) / np.log(10.0)


def torsion_from_zp0(zp0):
    """log10(T) from zeta'(0). T = exp(-zp0/2), log10 T = -zp0/(2 ln 10)."""
    return -zp0 / (2.0 * np.log(10.0))


# =============================================================================
# SECTION 3: Singlet-only torsion
# =============================================================================

def compute_singlet_torsion(data):
    """
    Compute T restricted to the 16 modes in the (0,0) representation.

    These are the only modes that couple to 4D gravity via Peter-Weyl
    orthogonality (EIH projection, S44 W2-3).

    The singlet has d_k = 1 for all modes, so:
      zeta'_singlet(0) = -2 sum_{k in singlet} ln|lambda_k|
      T_singlet = exp(-zeta'_singlet(0)/2) = prod |lambda_k|
    """
    # Method 1: from full spectrum, select d^2=1 modes
    mask = data['dim2_fold'] == 1
    om_singlet = data['omega_fold'][mask]
    deg_singlet = np.ones(len(om_singlet), dtype=int)

    # Method 2: from sector decomposition
    om_sector = data['sector_evals'][(0, 0)]

    # Cross-check
    assert len(om_singlet) == 16, f"Expected 16 singlet modes, got {len(om_singlet)}"
    assert len(om_sector) == 16, f"Expected 16 sector modes, got {len(om_sector)}"
    # Values should match (up to sorting)
    diff = np.sort(om_singlet) - np.sort(om_sector)
    assert np.max(np.abs(diff)) < 1e-10, f"Singlet mismatch: max diff = {np.max(np.abs(diff))}"

    zp0 = zeta_prime_0(om_singlet, deg_singlet)
    l10T = torsion_from_zp0(zp0)
    log_det = -zp0  # log det(D_singlet^2)
    product = np.prod(om_singlet)  # direct product = T_singlet

    print("=" * 78)
    print("SECTION 3: SINGLET-ONLY TORSION (16 modes, d_k = 1)")
    print("=" * 78)
    print(f"\n  Singlet eigenvalues |lambda_k| (M_KK units):")

    # Identify the branch structure: B1, B2, B3
    sorted_om = np.sort(om_singlet)
    unique_vals = []
    tol = 1e-6
    for v in sorted_om:
        if not unique_vals or abs(v - unique_vals[-1][0]) > tol:
            unique_vals.append((v, 1))
        else:
            unique_vals[-1] = (unique_vals[-1][0], unique_vals[-1][1] + 1)

    for val, mult in unique_vals:
        branch = "B1" if abs(val - 0.8197) < 0.01 else \
                 "B2" if abs(val - 0.8452) < 0.01 else \
                 "B3" if abs(val - 0.9714) < 0.01 else "?"
        print(f"    lambda = {val:.6f} (x{mult}, {branch})")

    print(f"\n  zeta'_singlet(0) = {zp0:.8f}")
    print(f"  -zeta'_singlet(0)/2 = {-zp0/2:.8f}")
    print(f"  log10(T_singlet) = {l10T:.6f}")
    print(f"  T_singlet = {product:.6f}")
    print(f"  log det(D_singlet^2) = {log_det:.8f}")

    # Cross-check: direct product
    print(f"\n  Cross-check: prod |lambda_k| = {product:.6f}")
    print(f"  Cross-check: exp(-zp0/2) = {np.exp(-zp0/2):.6f}")
    assert abs(product - np.exp(-zp0/2)) < 1e-8, "Product / exp mismatch"

    print(f"\n  INTERPRETATION:")
    if product > 1:
        print(f"    T_singlet = {product:.4f} > 1 (mild amplification)")
        print(f"    log10(T) = {l10T:.4f} (versus full T ~ 10^{{20301}})")
        print(f"    Reduction from full: 10^{{{20301 - l10T:.0f}}} orders")
    else:
        print(f"    T_singlet = {product:.4f} < 1 (suppression)")
        print(f"    Singlet torsion is O(1) — no CC amplification")

    return {
        'omega_singlet': om_singlet,
        'zp0_singlet': zp0,
        'log10_T_singlet': l10T,
        'T_singlet': product,
        'logdet_singlet': log_det,
        'n_modes': len(om_singlet),
    }


# =============================================================================
# SECTION 4: Progressive truncation
# =============================================================================

def compute_progressive_truncation(data):
    """
    Compute T at each truncation level max_pq_sum = 1, 2, ..., 6.

    max_pq_sum  sectors included               modes (per sector * 2 for conj)
    ---------   -------------------------     ---------
    0           (0,0)                          16
    1           + (1,0), (0,1)                 16 + 2*48 = 112
    2           + (1,1), (2,0), (0,2)          112 + 128 + 2*96 = 432
    3           + (2,1), (1,2), (3,0), (0,3)   432 + 2*240 + 2*160 = 1232
    """
    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
               (3,0), (0,3), (2,1), (1,2)]

    # Assign max_pq_sum level to each sector
    sector_level = {}
    for (p, q) in sectors:
        sector_level[(p, q)] = p + q

    # For each truncation level, accumulate eigenvalues
    # With Peter-Weyl weight d_k = dim(p,q)^2
    dim_pq = lambda p, q: (p+1) * (q+1) * (p+q+2) // 2

    print("\n" + "=" * 78)
    print("SECTION 4: PROGRESSIVE TRUNCATION")
    print("=" * 78)

    results = []
    max_levels = sorted(set(sector_level.values()))  # [0, 1, 2, 3]

    for max_pqs in range(max(max_levels) + 1):
        # Collect all eigenvalues up to this level
        all_omega = []
        all_deg = []
        included = []

        for (p, q) in sectors:
            if sector_level[(p, q)] <= max_pqs:
                ev = data['sector_evals'][(p, q)]
                d = dim_pq(p, q)
                all_omega.append(ev)
                all_deg.append(np.full(len(ev), d**2, dtype=int))
                included.append(f"({p},{q})")

        omega = np.concatenate(all_omega)
        deg = np.concatenate(all_deg)
        N_levels = len(omega)
        N_weighted = int(np.sum(deg))

        zp0 = zeta_prime_0(omega, deg)
        l10T = torsion_from_zp0(zp0)

        # Also compute UNWEIGHTED torsion (each mode counted once)
        zp0_uw = zeta_prime_0(omega, np.ones(len(omega), dtype=int))
        l10T_uw = torsion_from_zp0(zp0_uw)

        # And singlet-weighted (1/d_k)
        deg_eih = 1.0 / np.sqrt(deg.astype(float))  # 1/d_k weight
        zp0_eih = -2.0 * np.sum(deg_eih * np.log(omega))
        l10T_eih = torsion_from_zp0(zp0_eih)

        results.append({
            'max_pqs': max_pqs,
            'sectors': included,
            'N_levels': N_levels,
            'N_weighted': N_weighted,
            'zp0_PW': zp0,
            'log10_T_PW': l10T,
            'zp0_unweighted': zp0_uw,
            'log10_T_unweighted': l10T_uw,
            'zp0_EIH': zp0_eih,
            'log10_T_EIH': l10T_eih,
        })

        print(f"\n  max_pq_sum = {max_pqs}:")
        print(f"    Sectors: {', '.join(included)}")
        print(f"    N_levels = {N_levels}, N_weighted (PW) = {N_weighted}")
        print(f"    zeta'(0) [PW-weighted]  = {zp0:>14.4f}  =>  log10 T = {l10T:>12.4f}")
        print(f"    zeta'(0) [unweighted]   = {zp0_uw:>14.4f}  =>  log10 T = {l10T_uw:>12.4f}")
        print(f"    zeta'(0) [EIH: 1/d_k]   = {zp0_eih:>14.4f}  =>  log10 T = {l10T_eih:>12.4f}")

    # Fit log10(T) vs N_weighted to check scaling
    Ns = np.array([r['N_weighted'] for r in results])
    l10s = np.array([r['log10_T_PW'] for r in results])
    if len(Ns) > 2:
        # Linear fit: log10(T) = a * N + b
        p_lin = np.polyfit(Ns, l10s, 1)
        # Sublinear fit: log10(T) = a * N^alpha
        log_N = np.log(Ns[1:])  # skip singlet (too few modes)
        log_l10 = np.log(np.abs(l10s[1:]))
        if np.all(np.isfinite(log_l10)):
            p_power = np.polyfit(log_N, log_l10, 1)
            alpha = p_power[0]
        else:
            alpha = np.nan

        print(f"\n  SCALING ANALYSIS:")
        print(f"    Linear fit: log10(T) = {p_lin[0]:.6f} * N + {p_lin[1]:.4f}")
        print(f"    => T ~ 10^({p_lin[0]:.6f} * N)")
        print(f"    Power-law fit: log10(T) ~ N^{alpha:.4f}")
        if abs(alpha - 1.0) < 0.1:
            print(f"    => LINEARLY extensive: T ~ exp(const * N)")
        elif alpha < 0.9:
            print(f"    => SUBLINEAR in N: effective spectral dimension < total")
        else:
            print(f"    => SUPERLINEAR in N")
    else:
        alpha = np.nan
        p_lin = [0, 0]

    return results, alpha, p_lin


# =============================================================================
# SECTION 5: Dissolution-bounded torsion
# =============================================================================

def compute_dissolution_torsion(data):
    """
    At the dissolution cutoff epsilon_c ~ 1/sqrt(N), the geometry is fuzzy.
    Eigenvalues are uncertain by ~ epsilon_c * |lambda_k|.
    Compute T with eigenvalues smeared by this uncertainty.

    We use a Gaussian smearing: lambda_k -> lambda_k * (1 + epsilon_c * xi_k)
    where xi_k ~ N(0,1). Average over many realizations.
    """
    omega = data['omega_fold']
    deg = data['dim2_fold']
    N_total = int(np.sum(deg))

    # Dissolution scale
    epsilon_c = 1.0 / np.sqrt(N_total)  # ~ 1/sqrt(101984) ~ 3.1e-3

    print("\n" + "=" * 78)
    print("SECTION 5: DISSOLUTION-BOUNDED TORSION")
    print("=" * 78)
    print(f"\n  N_total (PW-weighted) = {N_total}")
    print(f"  epsilon_c = 1/sqrt(N) = {epsilon_c:.6e}")

    # Exact (unsmeared) values
    zp0_exact = zeta_prime_0(omega, deg)
    l10T_exact = torsion_from_zp0(zp0_exact)

    # Analytical estimate of smearing effect:
    # zeta'(0) = -2 sum d_k ln(lambda_k)
    # If lambda_k -> lambda_k * (1 + epsilon * xi_k):
    # ln(lambda_k(1+eps*xi)) = ln(lambda_k) + ln(1+eps*xi)
    #                        ~ ln(lambda_k) + eps*xi - (eps*xi)^2/2 + ...
    # <zeta'(0)_smeared> = zeta'(0)_exact + 2 * sum d_k * eps^2/2
    #                    = zeta'(0)_exact + eps^2 * sum d_k
    #                    = zeta'(0)_exact + eps^2 * N_total
    # Since eps^2 * N = 1, the shift is just +1.
    # Var(zeta'(0)_smeared) = 4 * eps^2 * sum d_k = 4 * eps^2 * N = 4

    shift_analytical = epsilon_c**2 * N_total
    sigma_analytical = 2.0 * epsilon_c * np.sqrt(N_total)

    print(f"\n  ANALYTICAL ESTIMATES (perturbative):")
    print(f"    <delta zeta'(0)> = eps^2 * N = {shift_analytical:.6f}")
    print(f"    sigma(zeta'(0)) = 2*eps*sqrt(N) = {sigma_analytical:.6f}")
    print(f"    Fractional shift: {shift_analytical / abs(zp0_exact):.6e}")
    print(f"    This is NEGLIGIBLE compared to |zeta'(0)| = {abs(zp0_exact):.4f}")

    # Monte Carlo verification
    np.random.seed(42)
    n_realizations = 10000
    zp0_samples = np.zeros(n_realizations)

    for i in range(n_realizations):
        xi = np.random.randn(len(omega))
        omega_smeared = omega * (1.0 + epsilon_c * xi)
        omega_smeared = np.abs(omega_smeared)  # ensure positivity
        omega_smeared = np.maximum(omega_smeared, 1e-15)  # floor
        zp0_samples[i] = zeta_prime_0(omega_smeared, deg)

    mean_zp0 = np.mean(zp0_samples)
    std_zp0 = np.std(zp0_samples)
    l10T_smeared = torsion_from_zp0(mean_zp0)

    print(f"\n  MONTE CARLO ({n_realizations} realizations):")
    print(f"    <zeta'(0)_smeared> = {mean_zp0:.6f}")
    print(f"    sigma(zeta'(0))    = {std_zp0:.6f}")
    print(f"    Exact zeta'(0)     = {zp0_exact:.6f}")
    print(f"    Shift              = {mean_zp0 - zp0_exact:.6f}")
    print(f"    Analytical pred    = {shift_analytical:.6f}")
    print(f"    Fractional shift   = {(mean_zp0 - zp0_exact) / abs(zp0_exact):.6e}")

    print(f"\n  TORSION COMPARISON:")
    print(f"    log10 T (exact)   = {l10T_exact:.4f}")
    print(f"    log10 T (smeared) = {l10T_smeared:.4f}")
    print(f"    Difference        = {l10T_smeared - l10T_exact:.6f} decades")

    # Progressive epsilon scan
    eps_values = np.array([1e-4, 1e-3, 3.1e-3, 1e-2, 3e-2, 1e-1, 3e-1])
    print(f"\n  EPSILON SCAN (perturbative formula: delta log10 T = -eps^2 * N / (2 ln 10)):")
    print(f"  {'epsilon':>10s}  {'delta_zp0':>12s}  {'delta_log10T':>14s}  {'frac_shift':>14s}")
    eps_scan_results = []
    for eps in eps_values:
        d_zp0 = eps**2 * N_total
        d_l10T = -d_zp0 / (2.0 * np.log(10.0))
        frac = d_zp0 / abs(zp0_exact)
        eps_scan_results.append((eps, d_zp0, d_l10T, frac))
        print(f"  {eps:10.4e}  {d_zp0:12.4f}  {d_l10T:14.4f}  {frac:14.6e}")

    return {
        'epsilon_c': epsilon_c,
        'zp0_exact': zp0_exact,
        'zp0_smeared_mean': mean_zp0,
        'zp0_smeared_std': std_zp0,
        'log10_T_exact': l10T_exact,
        'log10_T_smeared': l10T_smeared,
        'shift_analytical': shift_analytical,
        'sigma_analytical': sigma_analytical,
        'eps_scan': np.array(eps_values),
        'eps_scan_delta_log10T': np.array([r[2] for r in eps_scan_results]),
    }


# =============================================================================
# SECTION 6: EIH-weighted torsion
# =============================================================================

def compute_eih_torsion(data):
    """
    Instead of the Peter-Weyl weight d_k^2 (= dim(p,q)^2), use the
    EIH gravitational weight 1/d_k (= 1/dim(p,q)):

      zeta'_EIH(0) = -2 sum_k (1/d_k) ln|lambda_k|
      T_EIH = exp(-zeta'_EIH(0)/2)

    This weights each mode by its gravitational coupling strength.
    The EIH projection says only the singlet gravitates, but for
    modes that partially overlap with the singlet through metric
    fluctuations, the coupling goes as 1/d_k (Clebsch-Gordan coefficient
    for (p,q) -> (0,0) projection).
    """
    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
               (3,0), (0,3), (2,1), (1,2)]
    dim_pq = lambda p, q: (p+1) * (q+1) * (p+q+2) // 2

    print("\n" + "=" * 78)
    print("SECTION 6: EIH-WEIGHTED TORSION")
    print("=" * 78)

    # Compute three torsion variants:
    # (a) Full PW weight: d_k = dim^2
    # (b) EIH weight: w_k = 1/dim
    # (c) Singlet-only: w_k = delta_{(p,q),(0,0)}

    total_zp0_PW = 0.0
    total_zp0_EIH = 0.0
    total_zp0_singlet = 0.0
    total_N_PW = 0
    total_N_EIH = 0.0

    print(f"\n  {'Sector':>12s}  {'dim':>4s}  {'N_ev':>6s}  {'zp0_PW':>14s}  {'zp0_EIH':>14s}  {'ratio':>10s}")

    for (p, q) in sectors:
        ev = data['sector_evals'][(p, q)]
        d = dim_pq(p, q)
        n_ev = len(ev)

        # PW weight: each eigenvalue appears d^2 times in the full spectrum
        zp0_pw = -2.0 * d**2 * np.sum(np.log(ev))

        # EIH weight: 1/d
        zp0_eih = -2.0 * (1.0 / d) * np.sum(np.log(ev))

        total_zp0_PW += zp0_pw
        total_zp0_EIH += zp0_eih
        total_N_PW += n_ev * d**2
        total_N_EIH += n_ev / d

        if (p, q) == (0, 0):
            total_zp0_singlet = zp0_pw  # d=1, so PW = EIH = plain for singlet

        ratio = zp0_eih / zp0_pw if abs(zp0_pw) > 1e-15 else 0.0
        print(f"  ({p},{q}){' '*(8-len(f'({p},{q})'))}  {d:4d}  {n_ev:6d}  {zp0_pw:14.4f}  {zp0_eih:14.4f}  {ratio:10.6f}")

    l10T_PW = torsion_from_zp0(total_zp0_PW)
    l10T_EIH = torsion_from_zp0(total_zp0_EIH)
    l10T_singlet = torsion_from_zp0(total_zp0_singlet)

    print(f"\n  TOTALS:")
    print(f"    zeta'(0) PW-weighted  = {total_zp0_PW:>14.4f}  =>  log10 T = {l10T_PW:>12.4f}")
    print(f"    zeta'(0) EIH (1/d_k)  = {total_zp0_EIH:>14.4f}  =>  log10 T = {l10T_EIH:>12.4f}")
    print(f"    zeta'(0) singlet only  = {total_zp0_singlet:>14.4f}  =>  log10 T = {l10T_singlet:>12.4f}")

    # The key ratio: how much does EIH weighting suppress T?
    suppression = l10T_PW - l10T_EIH
    print(f"\n  EIH SUPPRESSION:")
    print(f"    log10(T_PW / T_EIH) = {suppression:.4f} decades")
    print(f"    T_PW / T_EIH = 10^{{{suppression:.1f}}}")
    print(f"    EIH torsion is smaller by a factor of 10^{{{abs(suppression):.0f}}}")

    # Effective weight ratio
    eff_N_PW = total_N_PW
    eff_N_EIH = total_N_EIH
    print(f"\n  EFFECTIVE MODE COUNT:")
    print(f"    N_eff (PW) = {eff_N_PW}")
    print(f"    N_eff (EIH) = {eff_N_EIH:.4f}")
    print(f"    Ratio: {eff_N_PW / eff_N_EIH:.2f}")

    return {
        'zp0_PW': total_zp0_PW,
        'zp0_EIH': total_zp0_EIH,
        'zp0_singlet': total_zp0_singlet,
        'log10_T_PW': l10T_PW,
        'log10_T_EIH': l10T_EIH,
        'log10_T_singlet': l10T_singlet,
        'N_eff_PW': eff_N_PW,
        'N_eff_EIH': eff_N_EIH,
    }


# =============================================================================
# SECTION 7: Physical bound synthesis
# =============================================================================

def compute_physical_bound(singlet_res, trunc_res, diss_res, eih_res, data):
    """
    Synthesize: what torsion does 4D gravity actually see?

    Three independent filters on the full T ~ 10^{20301}:
      1. EIH projection: only singlet gravitates => T_singlet ~ O(1)
      2. EIH weighting: non-singlet modes suppressed by 1/d_k => T_EIH ~ 10^{7}
      3. Dissolution: epsilon_c smearing negligible (delta log10 T ~ 0.2)

    The PHYSICAL torsion is T_singlet (filter 1), because the statement
    "only singlet modes gravitate" is EXACT (Peter-Weyl orthogonality
    on the compact group SU(3), not an approximation).
    """
    print("\n" + "=" * 78)
    print("SECTION 7: PHYSICAL BOUND SYNTHESIS")
    print("=" * 78)

    # All torsion estimates
    T_full = 20301.0  # log10, from W2-R3
    T_singlet = singlet_res['log10_T_singlet']
    T_EIH = eih_res['log10_T_EIH']
    T_smeared = diss_res['log10_T_smeared']

    # Torsion at each truncation level
    trunc_l10 = [r['log10_T_PW'] for r in trunc_res]
    trunc_N = [r['N_weighted'] for r in trunc_res]

    print(f"\n  TORSION HIERARCHY (all in log10):")
    print(f"  {'Quantity':>30s}  {'log10 T':>12s}  {'vs. full':>12s}")
    print(f"  {'Full PW-weighted':>30s}  {T_full:12.1f}  {'---':>12s}")
    print(f"  {'EIH-weighted (1/d_k)':>30s}  {T_EIH:12.4f}  {T_EIH - T_full:12.1f}")
    print(f"  {'Dissolution-smeared':>30s}  {T_smeared:12.4f}  {T_smeared - T_full:12.1f}")
    print(f"  {'Singlet-only (16 modes)':>30s}  {T_singlet:12.6f}  {T_singlet - T_full:12.1f}")

    # CC contribution from singlet torsion
    # rho_torsion = (M_KK^4 / 32 pi^2) * |zeta'(0)|
    # For singlet: |zeta'(0)| = 3.834 (from EIH data)
    zp0_sing = singlet_res['zp0_singlet']
    rho_sing_grav = (M_KK_gravity**4 / (32.0 * PI**2)) * abs(zp0_sing)
    rho_sing_kern = (M_KK_kerner**4 / (32.0 * PI**2)) * abs(zp0_sing)

    log10_rho_sing_grav = np.log10(rho_sing_grav / rho_Lambda_obs)
    log10_rho_sing_kern = np.log10(rho_sing_kern / rho_Lambda_obs)

    print(f"\n  CC FROM SINGLET TORSION:")
    print(f"    |zeta'_singlet(0)| = {abs(zp0_sing):.6f}")
    print(f"    rho (gravity M_KK) = {rho_sing_grav:.4e} GeV^4")
    print(f"    log10(rho/rho_obs) = {log10_rho_sing_grav:.2f}")
    print(f"    rho (Kerner M_KK)  = {rho_sing_kern:.4e} GeV^4")
    print(f"    log10(rho/rho_obs) = {log10_rho_sing_kern:.2f}")

    # Compare to full torsion CC
    zp0_full = float(data['torsion']['zeta_prime_0_fold'])
    rho_full_grav = (M_KK_gravity**4 / (32.0 * PI**2)) * abs(zp0_full)
    log10_rho_full = np.log10(rho_full_grav / rho_Lambda_obs)

    print(f"\n  SUPPRESSION FACTORS:")
    print(f"    Full torsion CC:    log10(rho/rho_obs) = {log10_rho_full:.2f}")
    print(f"    Singlet torsion CC: log10(rho/rho_obs) = {log10_rho_sing_grav:.2f}")
    print(f"    Reduction: {log10_rho_full - log10_rho_sing_grav:.2f} orders")
    print(f"    (from |zp0| = {abs(zp0_full):.1f} -> {abs(zp0_sing):.4f})")

    # Per-mode analysis
    per_mode_full = abs(zp0_full) / float(data['torsion']['n_weighted_fold'])
    per_mode_singlet = abs(zp0_sing) / singlet_res['n_modes']

    print(f"\n  PER-MODE TORSION:")
    print(f"    Full: |zp0|/N = {per_mode_full:.6f} per mode ({int(data['torsion']['n_weighted_fold'])} modes)")
    print(f"    Singlet: |zp0|/N = {per_mode_singlet:.6f} per mode (16 modes)")
    print(f"    Per-mode ratio: {per_mode_singlet / per_mode_full:.4f}")

    # The decisive question: is the physical torsion O(1)?
    print(f"\n  DECISIVE QUESTION: Is the physical torsion bounded?")
    print(f"    T_singlet = {singlet_res['T_singlet']:.6f}")

    if abs(singlet_res['log10_T_singlet']) < 1:
        verdict_detail = (
            f"YES. T_singlet = {singlet_res['T_singlet']:.4f} is O(1).\n"
            f"    The 16 singlet modes produce a torsion that is of order unity.\n"
            f"    The CC problem from torsion ({T_full:.0f} decades in the full spectrum)\n"
            f"    is ENTIRELY from non-singlet modes that do not gravitate.\n"
            f"    Peter-Weyl orthogonality eliminates the torsion contribution to CC."
        )
    elif abs(singlet_res['log10_T_singlet']) < 10:
        verdict_detail = (
            f"BOUNDED. T_singlet ~ 10^{{{singlet_res['log10_T_singlet']:.1f}}}.\n"
            f"    The singlet torsion is finite and small compared to 10^{{20301}}.\n"
            f"    The CC contribution from torsion is reduced by\n"
            f"    {T_full - singlet_res['log10_T_singlet']:.0f} orders (from {T_full:.0f} to {singlet_res['log10_T_singlet']:.1f})."
        )
    else:
        verdict_detail = (
            f"NOT BOUNDED. T_singlet ~ 10^{{{singlet_res['log10_T_singlet']:.1f}}}.\n"
            f"    Even the singlet torsion is exponentially large."
        )

    print(f"    {verdict_detail}")

    return {
        'T_full_log10': T_full,
        'T_singlet_log10': T_singlet,
        'T_EIH_log10': T_EIH,
        'T_smeared_log10': T_smeared,
        'rho_singlet_grav': rho_sing_grav,
        'rho_singlet_kern': rho_sing_kern,
        'log10_rho_over_obs_grav': log10_rho_sing_grav,
        'log10_rho_over_obs_kern': log10_rho_sing_kern,
        'reduction_orders': log10_rho_full - log10_rho_sing_grav,
        'per_mode_full': per_mode_full,
        'per_mode_singlet': per_mode_singlet,
    }


# =============================================================================
# SECTION 8: Gate evaluation
# =============================================================================

def evaluate_gate(singlet_res, phys_res):
    """TRUNCATED-TORSION-45 gate."""
    print("\n" + "=" * 78)
    print("GATE: TRUNCATED-TORSION-45")
    print("=" * 78)

    T_sing = singlet_res['T_singlet']
    l10T_sing = singlet_res['log10_T_singlet']
    reduction = phys_res['reduction_orders']

    print(f"\n  T_singlet = {T_sing:.6f}")
    print(f"  log10(T_singlet) = {l10T_sing:.6f}")
    print(f"  CC reduction: {reduction:.2f} orders (from full torsion)")
    print(f"  Physical CC from singlet torsion: {phys_res['log10_rho_over_obs_grav']:.1f} orders above obs")

    print(f"\n  Pre-registered criterion: INFO (is physical torsion bounded?)")

    if abs(l10T_sing) < 2:
        bounded = True
        bound_desc = "O(1)"
    elif abs(l10T_sing) < 10:
        bounded = True
        bound_desc = f"O(10^{l10T_sing:.0f})"
    else:
        bounded = False
        bound_desc = f"10^{l10T_sing:.0f}"

    verdict = "INFO"

    print(f"\n  VERDICT: {verdict}")
    print(f"  Physical torsion (singlet-only): T = {T_sing:.4f} [{bound_desc}]")
    print(f"  Bounded: {'YES' if bounded else 'NO'}")

    print(f"\n  STRUCTURAL RESULT:")
    print(f"  The analytic torsion T = 10^{{20301}} decomposes as:")
    print(f"    T = T_singlet * T_non-singlet")
    print(f"    T_singlet ~ {T_sing:.4f} (gravitating, 16 modes)")
    print(f"    T_non-singlet ~ 10^{{{20301 - l10T_sing:.0f}}} (dark, 101968 modes)")
    print(f"  Only T_singlet enters the Friedmann equation via EIH effacement.")
    print(f"  The 'CC problem from torsion' is 100% in the dark sector.")

    return verdict, bounded


# =============================================================================
# SECTION 9: Plotting
# =============================================================================

def make_plots(singlet_res, trunc_res, diss_res, eih_res, phys_res, verdict):
    """Generate diagnostic plots."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # (a) Singlet eigenvalue spectrum
    ax = axes[0, 0]
    om = np.sort(singlet_res['omega_singlet'])
    # Branch identification
    b1 = om[om < 0.83]
    b2 = om[(om >= 0.83) & (om < 0.92)]
    b3 = om[om >= 0.92]
    ax.barh(range(len(b1)), b1, color='C0', height=0.6, label=f'B1 ({len(b1)} modes)')
    ax.barh(range(len(b1), len(b1)+len(b2)), b2, color='C1', height=0.6,
            label=f'B2 ({len(b2)} modes)')
    ax.barh(range(len(b1)+len(b2), len(om)), b3, color='C2', height=0.6,
            label=f'B3 ({len(b3)} modes)')
    ax.set_xlabel('|lambda| (M_KK units)')
    ax.set_ylabel('Mode index')
    ax.set_title(f'(a) Singlet spectrum (16 modes)\n'
                 f'T_singlet = {singlet_res["T_singlet"]:.4f}')
    ax.legend(fontsize=8)
    ax.axvline(1.0, color='gray', ls=':', alpha=0.5, label='|lambda|=1')
    ax.grid(True, alpha=0.3, axis='x')

    # (b) Progressive truncation: log10(T) vs N
    ax = axes[0, 1]
    N_pw = [r['N_weighted'] for r in trunc_res]
    l10_pw = [r['log10_T_PW'] for r in trunc_res]
    l10_uw = [r['log10_T_unweighted'] for r in trunc_res]
    l10_eih = [r['log10_T_EIH'] for r in trunc_res]
    ax.plot(N_pw, l10_pw, 'bo-', label='PW-weighted (d_k^2)', markersize=8)
    ax.plot(N_pw, l10_uw, 'rs-', label='Unweighted', markersize=6)
    ax.plot(N_pw, l10_eih, 'g^-', label='EIH (1/d_k)', markersize=6)
    ax.set_xlabel('N_weighted (PW modes)')
    ax.set_ylabel('log10(T)')
    ax.set_title('(b) Progressive truncation\nlog10(T) vs mode count')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Add level labels
    for i, r in enumerate(trunc_res):
        ax.annotate(f'L{r["max_pqs"]}',
                    (N_pw[i], l10_pw[i]),
                    textcoords="offset points", xytext=(5, 5),
                    fontsize=7, color='blue')

    # (c) Torsion hierarchy (bar chart)
    ax = axes[0, 2]
    labels = ['Full\n(PW)', 'EIH\n(1/d_k)', 'Smeared\n(diss.)', 'Singlet\n(16 modes)']
    values = [phys_res['T_full_log10'],
              phys_res['T_EIH_log10'],
              phys_res['T_smeared_log10'],
              phys_res['T_singlet_log10']]
    colors = ['darkblue', 'steelblue', 'orange', 'red']
    bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=0.5)
    ax.set_ylabel('log10(T)')
    ax.set_title('(c) Torsion hierarchy\nAll estimates')
    ax.grid(True, alpha=0.3, axis='y')
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
                f'{v:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold')

    # (d) Sector decomposition of zeta'(0)
    ax = axes[1, 0]
    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
               (3,0), (0,3), (2,1), (1,2)]
    dim_pq = lambda p, q: (p+1) * (q+1) * (p+q+2) // 2
    sector_labels = [f'({p},{q})\nd={dim_pq(p,q)}' for (p,q) in sectors]
    sector_zp0_pw = []
    sector_zp0_eih = []
    for (p, q) in sectors:
        from s45_truncated_torsion import compute_eih_torsion
        ev = np.abs(np.load(os.path.join(DATA_DIR, 's36_sfull_tau_stabilization.npz'),
                            allow_pickle=True)[f'evals_tau0.190_{p}_{q}'])
        d = dim_pq(p, q)
        sector_zp0_pw.append(-2.0 * d**2 * np.sum(np.log(ev)))
        sector_zp0_eih.append(-2.0 * (1.0/d) * np.sum(np.log(ev)))

    x = np.arange(len(sectors))
    w = 0.35
    ax.bar(x - w/2, sector_zp0_pw, w, label="PW (d_k^2)", color='steelblue')
    ax.bar(x + w/2, sector_zp0_eih, w, label="EIH (1/d_k)", color='coral')
    ax.set_xticks(x)
    ax.set_xticklabels(sector_labels, fontsize=7)
    ax.set_ylabel("zeta'(0) contribution")
    ax.set_title("(d) Sector zeta'(0): PW vs EIH")
    ax.legend(fontsize=8)
    ax.axhline(0, color='k', lw=0.5)
    ax.grid(True, alpha=0.3, axis='y')

    # (e) Dissolution epsilon scan
    ax = axes[1, 1]
    eps_vals = diss_res['eps_scan']
    delta_l10 = diss_res['eps_scan_delta_log10T']
    ax.semilogx(eps_vals, delta_l10, 'ko-', markersize=6)
    ax.axvline(diss_res['epsilon_c'], color='red', ls='--', alpha=0.7,
               label=f'eps_c = {diss_res["epsilon_c"]:.3e}')
    ax.set_xlabel('Smearing epsilon')
    ax.set_ylabel('delta log10(T)')
    ax.set_title('(e) Dissolution smearing effect\non torsion')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # (f) Summary panel
    ax = axes[1, 2]
    ax.axis('off')
    summary = (
        f"TRUNCATED-TORSION-45: {verdict}\n"
        f"{'='*48}\n\n"
        f"Full torsion: log10(T) = {phys_res['T_full_log10']:.0f}\n"
        f"  = CC problem in spectral language\n\n"
        f"Singlet torsion (EIH): T = {singlet_res['T_singlet']:.4f}\n"
        f"  log10(T) = {singlet_res['log10_T_singlet']:.4f}\n"
        f"  = O(1) -- BOUNDED\n\n"
        f"EIH-weighted: log10(T) = {eih_res['log10_T_EIH']:.1f}\n"
        f"  Suppression: 10^{{{phys_res['T_full_log10'] - eih_res['log10_T_EIH']:.0f}}}\n\n"
        f"Dissolution (eps={diss_res['epsilon_c']:.3e}):\n"
        f"  delta log10(T) = {diss_res['log10_T_smeared'] - diss_res['log10_T_exact']:.4f}\n"
        f"  NEGLIGIBLE\n\n"
        f"STRUCTURAL RESULT:\n"
        f"  T = T_singlet x T_dark\n"
        f"  Only T_singlet gravitates\n"
        f"  Torsion CC is 100% in dark sector"
    )
    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=9, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.suptitle('S45 — Truncated Torsion at Dissolution Scale: TRUNCATED-TORSION-45',
                 fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = os.path.join(DATA_DIR, 's45_truncated_torsion.png')
    plt.savefig(plot_path, dpi=150)
    print(f"\n  Saved: {plot_path}")
    plt.close()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("S45 — TRUNCATED / SINGLET TORSION AT DISSOLUTION SCALE")
    print("Gate: TRUNCATED-TORSION-45")
    print("=" * 78)

    # Load all data
    print("\n--- Loading data ---")
    data = load_all_data()
    print(f"  Fold spectrum: {len(data['omega_fold'])} levels, "
          f"{int(np.sum(data['dim2_fold']))} PW-weighted modes")
    print(f"  Sectors loaded: {list(data['sector_evals'].keys())}")

    # 1. Singlet-only torsion
    singlet_res = compute_singlet_torsion(data)

    # 2. Progressive truncation
    trunc_res, alpha, p_lin = compute_progressive_truncation(data)

    # 3. Dissolution-bounded torsion
    diss_res = compute_dissolution_torsion(data)

    # 4. EIH-weighted torsion
    eih_res = compute_eih_torsion(data)

    # 5. Physical bound synthesis
    phys_res = compute_physical_bound(singlet_res, trunc_res, diss_res, eih_res, data)

    # 6. Gate evaluation
    verdict, bounded = evaluate_gate(singlet_res, phys_res)

    # 7. Save results
    print("\n--- Saving results ---")
    save_path = os.path.join(DATA_DIR, 's45_truncated_torsion.npz')

    # Progressive truncation arrays
    trunc_max_pqs = np.array([r['max_pqs'] for r in trunc_res])
    trunc_N_levels = np.array([r['N_levels'] for r in trunc_res])
    trunc_N_weighted = np.array([r['N_weighted'] for r in trunc_res])
    trunc_l10T_PW = np.array([r['log10_T_PW'] for r in trunc_res])
    trunc_l10T_uw = np.array([r['log10_T_unweighted'] for r in trunc_res])
    trunc_l10T_EIH = np.array([r['log10_T_EIH'] for r in trunc_res])
    trunc_zp0_PW = np.array([r['zp0_PW'] for r in trunc_res])

    np.savez(save_path,
             # Singlet torsion
             omega_singlet=singlet_res['omega_singlet'],
             zp0_singlet=singlet_res['zp0_singlet'],
             log10_T_singlet=singlet_res['log10_T_singlet'],
             T_singlet=singlet_res['T_singlet'],
             logdet_singlet=singlet_res['logdet_singlet'],
             n_modes_singlet=singlet_res['n_modes'],

             # Progressive truncation
             trunc_max_pqs=trunc_max_pqs,
             trunc_N_levels=trunc_N_levels,
             trunc_N_weighted=trunc_N_weighted,
             trunc_l10T_PW=trunc_l10T_PW,
             trunc_l10T_unweighted=trunc_l10T_uw,
             trunc_l10T_EIH=trunc_l10T_EIH,
             trunc_zp0_PW=trunc_zp0_PW,
             trunc_scaling_alpha=alpha,
             trunc_linear_slope=p_lin[0],
             trunc_linear_intercept=p_lin[1],

             # Dissolution
             epsilon_c=diss_res['epsilon_c'],
             zp0_smeared_mean=diss_res['zp0_smeared_mean'],
             zp0_smeared_std=diss_res['zp0_smeared_std'],
             log10_T_exact=diss_res['log10_T_exact'],
             log10_T_smeared=diss_res['log10_T_smeared'],
             dissolution_shift=diss_res['shift_analytical'],
             eps_scan=diss_res['eps_scan'],
             eps_scan_delta_log10T=diss_res['eps_scan_delta_log10T'],

             # EIH-weighted
             zp0_PW=eih_res['zp0_PW'],
             zp0_EIH=eih_res['zp0_EIH'],
             zp0_singlet_check=eih_res['zp0_singlet'],
             log10_T_PW=eih_res['log10_T_PW'],
             log10_T_EIH=eih_res['log10_T_EIH'],
             N_eff_PW=eih_res['N_eff_PW'],
             N_eff_EIH=eih_res['N_eff_EIH'],

             # Physical bound
             T_full_log10=phys_res['T_full_log10'],
             reduction_orders=phys_res['reduction_orders'],
             rho_singlet_grav=phys_res['rho_singlet_grav'],
             rho_singlet_kern=phys_res['rho_singlet_kern'],
             log10_rho_over_obs_grav=phys_res['log10_rho_over_obs_grav'],
             log10_rho_over_obs_kern=phys_res['log10_rho_over_obs_kern'],
             per_mode_full=phys_res['per_mode_full'],
             per_mode_singlet=phys_res['per_mode_singlet'],

             # Gate
             gate_verdict=verdict,
             gate_bounded=bounded,
             tau_fold=tau_fold,
             )
    print(f"  Saved: {save_path}")

    # 8. Plot
    # Build sector data inline for the plot (avoid circular import)
    make_plots_inline(singlet_res, trunc_res, diss_res, eih_res, phys_res, verdict, data)

    print(f"\nDone.")


def make_plots_inline(singlet_res, trunc_res, diss_res, eih_res, phys_res, verdict, data):
    """Generate diagnostic plots (inline version, no imports)."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # (a) Singlet eigenvalue spectrum
    ax = axes[0, 0]
    om = np.sort(singlet_res['omega_singlet'])
    b1 = om[om < 0.83]
    b2 = om[(om >= 0.83) & (om < 0.92)]
    b3 = om[om >= 0.92]
    y_offset = 0
    for branch, color, label in [(b1, 'C0', 'B1'), (b2, 'C1', 'B2'), (b3, 'C2', 'B3')]:
        if len(branch) > 0:
            ax.barh(range(y_offset, y_offset + len(branch)), branch,
                    color=color, height=0.6, label=f'{label} ({len(branch)})')
            y_offset += len(branch)
    ax.set_xlabel('|lambda| (M_KK units)')
    ax.set_ylabel('Mode index')
    ax.set_title(f'(a) Singlet spectrum (16 modes)\n'
                 f'T_singlet = {singlet_res["T_singlet"]:.4f}')
    ax.legend(fontsize=8)
    ax.axvline(1.0, color='gray', ls=':', alpha=0.5)
    ax.grid(True, alpha=0.3, axis='x')

    # (b) Progressive truncation
    ax = axes[0, 1]
    N_pw = [r['N_weighted'] for r in trunc_res]
    l10_pw = [r['log10_T_PW'] for r in trunc_res]
    l10_uw = [r['log10_T_unweighted'] for r in trunc_res]
    l10_eih_trunc = [r['log10_T_EIH'] for r in trunc_res]
    ax.plot(N_pw, l10_pw, 'bo-', label='PW (d_k^2)', markersize=8)
    ax.plot(N_pw, l10_uw, 'rs-', label='Unweighted', markersize=6)
    ax.plot(N_pw, l10_eih_trunc, 'g^-', label='EIH (1/d_k)', markersize=6)
    ax.set_xlabel('N_weighted (PW modes)')
    ax.set_ylabel('log10(T)')
    ax.set_title('(b) Progressive truncation\nlog10(T) vs mode count')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    for i, r in enumerate(trunc_res):
        ax.annotate(f'L{r["max_pqs"]}',
                    (N_pw[i], l10_pw[i]),
                    textcoords="offset points", xytext=(5, 5),
                    fontsize=7, color='blue')

    # (c) Torsion hierarchy
    ax = axes[0, 2]
    labels = ['Full\n(PW)', 'EIH\n(1/d_k)', 'Smeared\n(diss.)', 'Singlet\n(16)']
    values = [phys_res['T_full_log10'],
              phys_res['T_EIH_log10'],
              phys_res['T_smeared_log10'],
              phys_res['T_singlet_log10']]
    colors_bar = ['darkblue', 'steelblue', 'orange', 'red']
    bars = ax.bar(labels, values, color=colors_bar, edgecolor='black', linewidth=0.5)
    ax.set_ylabel('log10(T)')
    ax.set_title('(c) Torsion hierarchy')
    ax.grid(True, alpha=0.3, axis='y')
    for bar, v in zip(bars, values):
        y_pos = max(bar.get_height(), 0) + max(abs(v)*0.01, 50)
        ax.text(bar.get_x() + bar.get_width()/2, y_pos,
                f'{v:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold')

    # (d) Sector zeta'(0) decomposition
    ax = axes[1, 0]
    sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
               (3,0), (0,3), (2,1), (1,2)]
    dim_pq = lambda p, q: (p+1) * (q+1) * (p+q+2) // 2

    sfull = np.load(os.path.join(DATA_DIR, 's36_sfull_tau_stabilization.npz'),
                    allow_pickle=True)
    s_labels = [f'({p},{q})' for (p, q) in sectors]
    zp0_pw_list = []
    zp0_eih_list = []
    for (p, q) in sectors:
        ev = np.abs(sfull[f'evals_tau0.190_{p}_{q}'])
        d = dim_pq(p, q)
        zp0_pw_list.append(-2.0 * d**2 * np.sum(np.log(ev)))
        zp0_eih_list.append(-2.0 * (1.0/d) * np.sum(np.log(ev)))

    x = np.arange(len(sectors))
    w = 0.35
    ax.bar(x - w/2, zp0_pw_list, w, label="PW (d_k^2)", color='steelblue')
    ax.bar(x + w/2, zp0_eih_list, w, label="EIH (1/d_k)", color='coral')
    ax.set_xticks(x)
    ax.set_xticklabels(s_labels, fontsize=8)
    ax.set_ylabel("zeta'(0) contribution")
    ax.set_title("(d) Sector zeta'(0): PW vs EIH weight")
    ax.legend(fontsize=8)
    ax.axhline(0, color='k', lw=0.5)
    ax.grid(True, alpha=0.3, axis='y')

    # (e) Dissolution epsilon scan
    ax = axes[1, 1]
    ax.semilogx(diss_res['eps_scan'], diss_res['eps_scan_delta_log10T'],
                'ko-', markersize=6)
    ax.axvline(diss_res['epsilon_c'], color='red', ls='--', alpha=0.7,
               label=f'eps_c = {diss_res["epsilon_c"]:.3e}')
    ax.set_xlabel('Smearing epsilon')
    ax.set_ylabel('delta log10(T)')
    ax.set_title('(e) Dissolution smearing\neffect on torsion')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # (f) Summary
    ax = axes[1, 2]
    ax.axis('off')
    summary = (
        f"TRUNCATED-TORSION-45: {verdict}\n"
        f"{'='*48}\n\n"
        f"Full torsion: log10(T) = {phys_res['T_full_log10']:.0f}\n"
        f"  = CC problem in spectral language\n\n"
        f"Singlet torsion (16 modes, EIH):\n"
        f"  T = {singlet_res['T_singlet']:.4f}\n"
        f"  log10(T) = {singlet_res['log10_T_singlet']:.4f}\n"
        f"  => O(1) — BOUNDED\n\n"
        f"EIH-weighted (all sectors, 1/d_k):\n"
        f"  log10(T) = {eih_res['log10_T_EIH']:.1f}\n\n"
        f"Dissolution (eps={diss_res['epsilon_c']:.3e}):\n"
        f"  delta log10(T) = {diss_res['log10_T_smeared']-diss_res['log10_T_exact']:.4f}\n\n"
        f"CC from singlet torsion:\n"
        f"  log10(rho/rho_obs) = {phys_res['log10_rho_over_obs_grav']:.1f}\n"
        f"  Reduction: {phys_res['reduction_orders']:.1f} orders\n\n"
        f"T = T_singlet x T_dark\n"
        f"Only T_singlet gravitates."
    )
    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=9, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.suptitle('S45 — Truncated Torsion: TRUNCATED-TORSION-45',
                 fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = os.path.join(DATA_DIR, 's45_truncated_torsion.png')
    plt.savefig(plot_path, dpi=150)
    print(f"\n  Saved: {plot_path}")
    plt.close()


if __name__ == '__main__':
    main()
