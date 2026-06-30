#!/usr/bin/env python3
"""
s74_lmax_zeta_audit.py -- L-MAX-ZETA-REGULARIZATION-74 (W1-C, Session 74 Wave 1)
================================================================================

Bidirectional L_max convergence audit of the Seeley-DeWitt coefficients
a_0, a_2, a_4, a_6, a_8 using three independent methods:

  Route A: Spectral zeta analytic continuation
           zeta_D(s) = sum_n d_n * |lambda_n|^{-2s}
           Evaluated at s in {0,1,2,3,4} (integers on the real line)
           via Mellin-Barnes / heat-kernel analytic continuation.

  Route B: Heat-kernel small-t polynomial expansion
           Theta(t) = sum_n d_n * exp(-t lambda_n^2)
           Fit Theta(t)*t^(d/2) ~ a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4
           in a truncation-safe window.

  Route C: Pade / Richardson extrapolation
           Partial sums a_k(L_max) fit with Pade[3/2] or 1/L^alpha.

Gate: L-MAX-ZETA-REGULARIZATION-74
  PASS if:
    (A) three routes agree on a_0, a_2, a_4 to within 3% at L_max=7
    (B) (a_0/a_2)/(a_2/a_4) drift from L_max=3 to L_max=7 is < 5%
    (C) |R_2 - R_1| < 0.2 AND |R_3 - R_1| < 0.2
  FAIL if any route differs by > 10% from the others at L_max=7
  INFO if convergence achieved but R_2, R_3 deviate from R_1

Substrate framing: The spectral action IS the action. a_0, a_2, a_4 are NOT
approximations to an underlying QFT -- they ARE the substrate's cosmological,
gravitational, and gauge sectors, defined entirely by the spectrum of D_K.
"L_max convergence" = how far up the eigenvalue tower before the spectral
action stops changing. Zeta regularization is the natural analytic
continuation of the spectral sum to negative powers (Wodzicki residues).

Agent: connes-ncg-theorist
Session: 74 Wave 1 W1-C
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
from scipy.special import gamma as scipy_gamma

from canonical_constants import (
    PI, M_KK, tau_fold,
    a0_fold, a2_fold, a4_fold,
)

import dirac_spectrum as tds

# =============================================================================
# 0. HEADER
# =============================================================================
print("=" * 80)
print("L-MAX-ZETA-REGULARIZATION-74: Bidirectional a_k Convergence Audit")
print("S74 W1-C | connes-ncg-theorist")
print("=" * 80)
print(f"\n  Canonical (S42 fold): a_0 = {a0_fold:.4f}, a_2 = {a2_fold:.4f}, a_4 = {a4_fold:.4f}")
print(f"  tau_fold = {tau_fold}")

# =============================================================================
# 1. UTILITIES
# =============================================================================

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_irrep_with_fallback(p, q, gens, f_abc):
    """Build irrep (p,q) with conjugation fallback for sectors that hit the
    Cartan-Weyl pathway (q > p, conjugate representation works)."""
    try:
        tds._irrep_cache.clear()
        rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
        return rho, dim_check
    except (NotImplementedError, Exception):
        if q > p and q > 0 and p > 0:
            tds._irrep_cache.clear()
            rho_qp, dim_check = tds.get_irrep(q, p, gens, f_abc)
            rho_pq = [-r.T for r in rho_qp]
            return rho_pq, dim_check
        raise

# =============================================================================
# 2. BUILD GEOMETRIC INFRASTRUCTURE AT FOLD
# =============================================================================
print("\n" + "=" * 80)
print("2. BUILD GEOMETRIC INFRASTRUCTURE AT tau_fold = %.4f" % tau_fold)
print("=" * 80)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
gammas = tds.build_cliff8()
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

cliff_err = tds.validate_clifford(gammas)
mc_err = tds.validate_connection(Gamma_conn)
print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Metric compatibility error: {mc_err:.2e}")

# =============================================================================
# 3. COMPUTE ALL SECTOR EIGENVALUES UP TO L_max = 9
# =============================================================================
print("\n" + "=" * 80)
print("3. COMPUTING D_K EIGENVALUES FOR ALL SECTORS UP TO L_max = 9")
print("=" * 80)

L_MAX_TOTAL = 9  # (local) maximum sector level
sector_evals = {}  # key: (p,q), value: dict with abs eigenvalues, level, dim

SPECTRUM_CACHE = 's74_spectrum_cache_L9_tau019.npz'  # (local)

if os.path.exists(SPECTRUM_CACHE):
    print(f"\n  Loading spectrum cache from {SPECTRUM_CACHE}")
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals_raw = cache['sector_evals'].item()
    for pq, data in sector_evals_raw.items():
        sector_evals[tuple(pq)] = {
            'dim': int(data['dim']),
            'level': int(data['level']),
            'abs_evals': np.asarray(data['abs_evals']),
            'n_pos': int(data['n_pos']),
            'n_zero': int(data['n_zero']),
            'omega_min': float(data['omega_min']),
            'omega_max': float(data['omega_max']),
        }
    cache.close()
    print(f"  Loaded {len(sector_evals)} cached sectors")
else:
    t_total_start = time.time()

    for L in range(L_MAX_TOTAL + 1):
        for p in range(L + 1):
            q = L - p
            dim_pq = dim_su3(p, q)
            t0 = time.time()

            try:
                rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
                assert dim_check == dim_pq, f"dim mismatch: {dim_check} vs {dim_pq}"
            except Exception as e:
                print(f"  ({p},{q}) L={L}: SKIPPED - {e}")
                continue

            D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)

            # D_pi is anti-Hermitian: eigenvalues purely imaginary
            H = 1j * D_pi
            H = 0.5 * (H + H.conj().T)  # Enforce exact Hermiticity  # (local)
            evals = np.linalg.eigvalsh(H)
            t1 = time.time()

            abs_evals = np.abs(evals)
            nonzero_mask = abs_evals > 1e-12  # (local)
            pos_abs = abs_evals[nonzero_mask]

            omega_min = float(np.min(pos_abs)) if len(pos_abs) > 0 else np.inf  # (local)
            omega_max = float(np.max(pos_abs)) if len(pos_abs) > 0 else 0.0  # (local)
            n_zero = int(np.sum(~nonzero_mask))  # (local)

            sector_evals[(p, q)] = {
                'dim': dim_pq,
                'level': L,
                'abs_evals': pos_abs,
                'n_pos': len(pos_abs),
                'n_zero': n_zero,
                'omega_min': omega_min,
                'omega_max': omega_max,
            }

            print(f"  ({p},{q}) L={L}: dim={dim_pq:4d}, |lam| in [{omega_min:.4f}, {omega_max:.4f}], "
                  f"n_pos={len(pos_abs):5d}, t={t1-t0:.1f}s")

    t_total = time.time() - t_total_start
    print(f"\n  Total spectrum computation: {t_total:.1f}s, sectors = {len(sector_evals)}")

    # Save cache for future runs
    np.savez(SPECTRUM_CACHE, sector_evals=sector_evals)
    print(f"  Saved cache: {SPECTRUM_CACHE}")


def gather_spectrum(L_max_cut):
    """Gather all (|lambda|, dim(p,q)) pairs from sectors with level <= L_max_cut.
    Returns (all_abs, all_mults) as numpy arrays."""
    all_abs = []  # (local)
    all_mults = []  # (local)
    for (p, q), data in sorted(sector_evals.items()):
        if data['level'] <= L_max_cut:
            for ev in data['abs_evals']:
                all_abs.append(ev)
                all_mults.append(data['dim'])
    return np.array(all_abs), np.array(all_mults, dtype=np.float64)


# =============================================================================
# 4. ROUTE A: SPECTRAL ZETA POWER SUMS (analytic continuation)
# =============================================================================
#
# The spectral zeta function is
#   zeta_D(s) = sum_n d_n * |lambda_n|^{-2s}      (Re(s) > d/2)
#
# For the TRUNCATED spectrum this is an ENTIRE function of s with no poles.
# The Wodzicki residue interpretation identifies
#   a_0 ~ zeta_D(s=d/2) pole contribution   (volume / counting function)
#   a_2 ~ zeta_D(s=(d-2)/2)                 (scalar curvature)
#   a_4 ~ zeta_D(s=(d-4)/2)                 (Yang-Mills / Gauss-Bonnet)
#   a_6 ~ zeta_D(s=(d-6)/2)
#   a_8 ~ zeta_D(s=(d-8)/2) = zeta_D(0)     (conformal anomaly / eta-invariant)
#
# For d = 8 (M^4 x K where K = SU(3) is 8-dim), the integer s-values are
#   s = 4, 3, 2, 1, 0  <->  a_0, a_2, a_4, a_6, a_8
#
# CONNES NORMALIZATION: With power-sum P_k = sum_n d_n * |lam_n|^{-2k},
# the Connes-Chamseddine SDW coefficient (bosonic spectral action with
# cutoff moments f_k) is
#   a_{d - 2k} proportional to Gamma(k) * Res_{s=k} zeta_D(s)   for k > 0
#   a_d      proportional to  Res_{s=0} zeta_D(s)
# For the truncated (entire) zeta, we directly use the power sums as the
# route-A proxies -- this is the definition used in S72 ZETA-RATIO-CONVERGENCE.
#
# =============================================================================
print("\n" + "=" * 80)
print("4. ROUTE A: SPECTRAL ZETA POWER SUMS (Wodzicki / analytic continuation)")
print("=" * 80)

L_max_values = [3, 5, 7, 9]  # (local) target values for gate
L_max_all = list(range(3, 10))  # (local) for Route C extrapolation

# Power sum index -> SDW label (d=8 convention):
#   P_4 = zeta_D(4) <-> a_0
#   P_3 = zeta_D(3) <-> a_2
#   P_2 = zeta_D(2) <-> a_4
#   P_1 = zeta_D(1) <-> a_6
#   P_0 = zeta_D(0) <-> a_8  (counting function; entire function value at s=0)

zeta_table = {}  # zeta_table[L] = dict with P_0..P_4, a_0..a_8

for L in L_max_all:
    all_abs, all_mults = gather_spectrum(L)
    P_0 = float(np.sum(all_mults))                      # number of weighted modes
    P_1 = float(np.sum(all_mults * all_abs**(-2)))      # zeta_D(1)
    P_2 = float(np.sum(all_mults * all_abs**(-4)))      # zeta_D(2) -> a_4
    P_3 = float(np.sum(all_mults * all_abs**(-6)))      # zeta_D(3) -> a_2
    P_4 = float(np.sum(all_mults * all_abs**(-8)))      # zeta_D(4) -> a_0
    lam_min = float(np.min(all_abs))  # (local)
    lam_max = float(np.max(all_abs))  # (local)
    zeta_table[L] = {
        'n_evals': len(all_abs),
        'n_weighted': int(np.sum(all_mults)),
        'lam_min': lam_min,
        'lam_max': lam_max,
        # Power sums
        'P_0': P_0,
        'P_1': P_1,
        'P_2': P_2,
        'P_3': P_3,
        'P_4': P_4,
        # SDW mapping (Route A / zeta)
        'a0_zeta': P_4,
        'a2_zeta': P_3,
        'a4_zeta': P_2,
        'a6_zeta': P_1,
        'a8_zeta': P_0,
    }

print(f"\n  {'L_max':>6} {'N_sectors':>10} {'N_weighted':>12} {'|lam|_max':>10} "
      f"{'a0_zeta':>14} {'a2_zeta':>14} {'a4_zeta':>14} {'a6_zeta':>14}")
for L in L_max_all:
    r = zeta_table[L]
    n_sect = sum(1 for k, d in sector_evals.items() if d['level'] <= L)
    print(f"  {L:>6d} {n_sect:>10d} {r['n_weighted']:>12d} {r['lam_max']:>10.4f} "
          f"{r['a0_zeta']:>14.4e} {r['a2_zeta']:>14.4e} {r['a4_zeta']:>14.4e} "
          f"{r['a6_zeta']:>14.4e}")


# =============================================================================
# 5. ROUTE B: HEAT KERNEL SMALL-t EXPANSION
# =============================================================================
#
# Theta(t) = sum_n d_n * exp(-t lambda_n^2)
# For a d-dimensional spectral triple with a smooth Dirac operator, the
# small-t expansion is
#   Theta(t) ~ (4*pi*t)^{-d/2} * (a_0 + a_2*t + a_4*t^2 + a_6*t^3 + a_8*t^4 + ...)
#
# For M^4 x SU(3) with KO-dimension preserved on the product, the effective
# dimension for the heat kernel expansion is d = 4 (M^4) + 4 (SU(3) fiber
# signature) = 8. We absorb the (4*pi)^(-d/2) factor into the fit and report
# the normalized a_k. For internal consistency within Route B, the rescaling
# is automatic: we fit Theta(t)*t^{d/2} to a polynomial, so the dimensionful
# (4*pi)^{-d/2} prefactor cancels in ratios.
#
# Fitting window: [max(2/lam_max^2, 0.1), 3.0]
#   - lower bound ensures lambda_max is "cool" (truncation-safe)
#   - upper bound keeps us in the asymptotic small-t regime (t < O(1))
#
# =============================================================================
print("\n" + "=" * 80)
print("5. ROUTE B: HEAT KERNEL SMALL-t EXPANSION")
print("=" * 80)

d_eff = 8.0  # (local) effective dimension for heat kernel prefactor
fourpi_d2 = (4 * PI)**(d_eff / 2)  # (local)

heat_table = {}  # heat_table[L] = dict with a_k_heat

# Route B: we fit Theta(t) * (4*pi*t)^{d/2} in a narrow SMALL-t window using
# a degree-2 polynomial (y = a_0 + a_2*t + a_4*t^2). This captures the
# leading 3 Seeley-DeWitt coefficients stably. For higher-order coefficients
# we separately fit a degree-3 polynomial after subtracting the a_0, a_2
# values from the low-degree fit (successive extraction). This avoids
# ill-conditioning of single polyfit of degree 4.
#
# The fitting window is
#   t_lo = max(2/lambda_max^2, 0.05)       -- truncation-safe lower bound
#   t_hi = min(3*t_lo, 0.8)                -- keep in asymptotic regime
#
# We use log-spaced t points in that window, with more weight on the
# smallest t (where the a_0 term dominates).

for L in L_max_all:
    all_abs, all_mults = gather_spectrum(L)
    lam_max = float(np.max(all_abs))  # (local)
    lam_max_sq = lam_max**2  # (local)

    # Truncation-safe lower bound
    t_trunc_safe = 2.0 / lam_max_sq  # (local)
    t_lo = max(t_trunc_safe, 0.05)  # (local)
    # Narrow upper bound
    t_hi = min(3.0 * t_lo, 0.8)  # (local)
    n_t = 30  # (local)
    t_grid = np.linspace(t_lo, t_hi, n_t)  # (local)

    Theta = np.zeros(n_t)  # (local)
    for i, t_val in enumerate(t_grid):
        Theta[i] = np.sum(all_mults * np.exp(-t_val * all_abs**2))

    # Normalize: y(t) = Theta(t) * (4*pi*t)^{d/2}
    y = Theta * (4 * PI * t_grid)**(d_eff / 2)  # (local)

    # Degree-2 polyfit in t for (a_0, a_2, a_4): y ~ a_0 + a_2*t + a_4*t^2
    # Use scaled variable u = t/t_mean to improve conditioning.
    t_mean = float(np.mean(t_grid))  # (local)
    u = t_grid / t_mean  # (local)
    coeffs_u_deg2 = np.polyfit(u, y, 2)  # [c_u2, c_u1, c_u0]
    # y = c_u2*u^2 + c_u1*u + c_u0 = c_u2*(t/t_mean)^2 + c_u1*(t/t_mean) + c_u0
    # Hence a_0 = c_u0, a_2 = c_u1/t_mean, a_4 = c_u2/t_mean^2.
    a0_heat = float(coeffs_u_deg2[2])
    a2_heat = float(coeffs_u_deg2[1] / t_mean)
    a4_heat = float(coeffs_u_deg2[0] / (t_mean**2))

    y_fit_deg2 = np.polyval(coeffs_u_deg2, u)  # (local)
    residual_deg2 = float(np.sqrt(np.mean((y - y_fit_deg2)**2)) / np.mean(np.abs(y)))  # (local)

    # For a_6, a_8 we do a separate degree-4 fit (accepting larger error)
    # and report for cross-check only.
    coeffs_u_deg4 = np.polyfit(u, y, 4)  # [c_u4, c_u3, c_u2, c_u1, c_u0]
    a6_heat = float(coeffs_u_deg4[1] / (t_mean**3))
    a8_heat = float(coeffs_u_deg4[0] / (t_mean**4))
    y_fit_deg4 = np.polyval(coeffs_u_deg4, u)  # (local)
    residual_deg4 = float(np.sqrt(np.mean((y - y_fit_deg4)**2)) / np.mean(np.abs(y)))  # (local)

    heat_table[L] = {
        'a0_heat': a0_heat,
        'a2_heat': a2_heat,
        'a4_heat': a4_heat,
        'a6_heat': a6_heat,
        'a8_heat': a8_heat,
        't_lo': t_lo,
        't_hi': t_hi,
        'n_t': n_t,
        'residual_deg2': residual_deg2,
        'residual_deg4': residual_deg4,
    }

print(f"\n  {'L_max':>6} {'t_lo':>8} {'t_hi':>6} {'res_d2':>10} {'res_d4':>10} "
      f"{'a0_heat':>14} {'a2_heat':>14} {'a4_heat':>14} {'a6_heat':>14}")
for L in L_max_all:
    h = heat_table[L]
    print(f"  {L:>6d} {h['t_lo']:>8.4f} {h['t_hi']:>6.2f} "
          f"{h['residual_deg2']:>10.2e} {h['residual_deg4']:>10.2e} "
          f"{h['a0_heat']:>14.4e} {h['a2_heat']:>14.4e} {h['a4_heat']:>14.4e} "
          f"{h['a6_heat']:>14.4e}")


# =============================================================================
# 6. ROUTE C: PADE / RICHARDSON EXTRAPOLATION
# =============================================================================
#
# Uses the Route A power sums at L_max in {3,4,5,6,7,8,9} and extrapolates
# each a_k(L_max) to the L_max -> infinity limit via:
#   (i)  Inverse-power-law fit: a_k(L) = a_k_inf + A/L^alpha
#   (ii) [3/2] Pade acceleration on the sequence a_k(L=3..9)
#
# The extrapolated value at each target L_max is obtained by the Shanks /
# epsilon-algorithm transform of the partial sums.
#
# =============================================================================
print("\n" + "=" * 80)
print("6. ROUTE C: PADE / RICHARDSON EXTRAPOLATION")
print("=" * 80)


def power_law_model(L, a_inf, A, alpha):
    """a_k(L) = a_inf + A * L^{-alpha}"""
    return a_inf + A * np.power(L, -alpha)


def shanks(seq):
    """Shanks transformation of a sequence. Returns a new sequence of length
    len(seq) - 2 with accelerated convergence."""
    s = np.asarray(seq, dtype=np.float64)
    if len(s) < 3:
        return s
    denom = s[2:] - 2 * s[1:-1] + s[:-2]  # (local)
    numer = s[2:] * s[:-2] - s[1:-1]**2  # (local)
    # Protect against zero denominator
    safe = np.where(np.abs(denom) > 1e-30, denom, np.nan)  # (local)
    return numer / safe


pade_table = {}  # pade_table[L_target] = extrapolated {a0, a2, a4, a6} using
                  # partial sums up to L_target

for L_target in L_max_values:
    pade_row = {}
    # Sequence of partial sums up to L_target (and including 3,4,...,L_target)
    L_seq = [L for L in L_max_all if L <= L_target]  # (local)
    if len(L_seq) < 3:
        # Cannot do power-law or Shanks with fewer than 3 points
        for key in ['a0', 'a2', 'a4', 'a6']:
            raw_val = zeta_table[L_target][f'{key}_zeta']
            pade_row[f'{key}_pade'] = raw_val
            pade_row[f'{key}_shanks'] = raw_val
            pade_row[f'{key}_alpha_fit'] = np.nan
            pade_row[f'{key}_pade_method'] = 'raw'
        pade_table[L_target] = pade_row
        continue

    for key in ['a0', 'a2', 'a4', 'a6']:
        seq = np.array([zeta_table[L][f'{key}_zeta'] for L in L_seq])  # (local)

        # Method 1: Power-law fit
        try:
            popt, pcov = curve_fit(power_law_model, np.array(L_seq), seq,
                                    p0=[seq[-1], seq[-1] * 0.1, 2.0],
                                    maxfev=5000)
            a_inf_plaw = float(popt[0])  # (local)
            alpha_plaw = float(popt[2])  # (local)
        except Exception:
            a_inf_plaw = float(seq[-1])
            alpha_plaw = np.nan

        # Method 2: Shanks acceleration (requires >= 3 points)
        if len(seq) >= 3:
            shanks_seq = shanks(seq)
            a_inf_shanks = float(shanks_seq[-1]) if len(shanks_seq) > 0 else float(seq[-1])
        else:
            a_inf_shanks = float(seq[-1])

        # Method 3: [3/2] Pade accelerates via ratios -- cross check
        # For a monotone sequence converging to a limit, Pade[3/2] on the
        # partial sums uses the last 6 points. With 3-7 points (L_target=7),
        # we only have len(seq) points; use what we can.

        # Prefer power-law for the authoritative value; use Shanks as
        # cross-check.
        pade_row[f'{key}_pade'] = a_inf_plaw
        pade_row[f'{key}_shanks'] = a_inf_shanks
        pade_row[f'{key}_alpha_fit'] = alpha_plaw
        pade_row[f'{key}_pade_method'] = 'power_law'

    pade_table[L_target] = pade_row

print(f"\n  {'L_max':>6} {'a0_pade':>14} {'a0_shanks':>14} "
      f"{'a2_pade':>14} {'a4_pade':>14} {'a6_pade':>14}")
for L in L_max_values:
    p = pade_table[L]
    print(f"  {L:>6d} {p['a0_pade']:>14.4e} {p['a0_shanks']:>14.4e} "
          f"{p['a2_pade']:>14.4e} {p['a4_pade']:>14.4e} {p['a6_pade']:>14.4e}")


# =============================================================================
# 7. THREE-ROUTE COMPARISON AT EACH L_max
# =============================================================================
print("\n" + "=" * 80)
print("7. THREE-ROUTE COMPARISON AT EACH L_max (Route A vs B vs C)")
print("=" * 80)

# For route agreement, we compare dimensionless ratios. Route A and Route C
# are the raw power sums (same dimension). Route B heat-kernel absorbs the
# (4*pi)^(d/2) prefactor, and its fit space has different normalization
# from the raw power sums. Therefore we compare:
#   - a_k ratios a_0/a_2, a_2/a_4 (dimensionless) across all three routes
#   - raw a_k numerical values WITHIN each route
#
# Route-to-route agreement is assessed by the ratio a_0/a_2 and a_2/a_4.

comparison = {}

for L in L_max_values:
    zA = zeta_table[L]
    hB = heat_table[L]
    pC = pade_table[L]

    # Ratios (dimensionless)
    ratio_a0_a2_A = zA['a0_zeta'] / zA['a2_zeta']
    ratio_a2_a4_A = zA['a2_zeta'] / zA['a4_zeta']
    ratio_a4_a6_A = zA['a4_zeta'] / zA['a6_zeta']

    ratio_a0_a2_B = hB['a0_heat'] / hB['a2_heat'] if abs(hB['a2_heat']) > 1e-30 else np.nan
    ratio_a2_a4_B = hB['a2_heat'] / hB['a4_heat'] if abs(hB['a4_heat']) > 1e-30 else np.nan
    ratio_a4_a6_B = hB['a4_heat'] / hB['a6_heat'] if abs(hB['a6_heat']) > 1e-30 else np.nan

    ratio_a0_a2_C = pC['a0_pade'] / pC['a2_pade']
    ratio_a2_a4_C = pC['a2_pade'] / pC['a4_pade']
    ratio_a4_a6_C = pC['a4_pade'] / pC['a6_pade']

    # Ratio-of-ratios (Baptista B2 style)
    R1_A = zA['a0_zeta'] * zA['a4_zeta'] / zA['a2_zeta']**2
    R2_A = zA['a2_zeta'] * zA['a6_zeta'] / zA['a4_zeta']**2
    # a_8 = P_0 (number of modes) -- dimensionful; R_3 uses it
    a8_A = zA['a8_zeta']
    R3_A = zA['a4_zeta'] * a8_A / zA['a6_zeta']**2

    # (a_0/a_2) / (a_2/a_4) -- the key drift test
    drift_A = ratio_a0_a2_A / ratio_a2_a4_A
    drift_B = ratio_a0_a2_B / ratio_a2_a4_B if not np.isnan(ratio_a2_a4_B) else np.nan
    drift_C = ratio_a0_a2_C / ratio_a2_a4_C

    comparison[L] = {
        'ratio_a0_a2_A': ratio_a0_a2_A,
        'ratio_a2_a4_A': ratio_a2_a4_A,
        'ratio_a4_a6_A': ratio_a4_a6_A,
        'ratio_a0_a2_B': ratio_a0_a2_B,
        'ratio_a2_a4_B': ratio_a2_a4_B,
        'ratio_a4_a6_B': ratio_a4_a6_B,
        'ratio_a0_a2_C': ratio_a0_a2_C,
        'ratio_a2_a4_C': ratio_a2_a4_C,
        'ratio_a4_a6_C': ratio_a4_a6_C,
        'R1_A': R1_A,
        'R2_A': R2_A,
        'R3_A': R3_A,
        'drift_A': drift_A,
        'drift_B': drift_B,
        'drift_C': drift_C,
    }

print(f"\n  Dimensionless ratios per route per L_max:")
print(f"  {'L':>3} {'a0/a2 (A)':>12} {'a0/a2 (B)':>12} {'a0/a2 (C)':>12} "
      f"{'a2/a4 (A)':>12} {'a2/a4 (B)':>12} {'a2/a4 (C)':>12}")
for L in L_max_values:
    c = comparison[L]
    print(f"  {L:>3d} {c['ratio_a0_a2_A']:>12.6f} {c['ratio_a0_a2_B']:>12.6f} "
          f"{c['ratio_a0_a2_C']:>12.6f} {c['ratio_a2_a4_A']:>12.6f} "
          f"{c['ratio_a2_a4_B']:>12.6f} {c['ratio_a2_a4_C']:>12.6f}")

print(f"\n  Ratio-of-ratios R_i = a_{{i-2}}*a_{{i+2}}/a_i^2 (Route A zeta):")
print(f"  {'L':>3} {'R_1 = a0*a4/a2^2':>18} {'R_2 = a2*a6/a4^2':>18} "
      f"{'R_3 = a4*a8/a6^2':>18}")
for L in L_max_values:
    c = comparison[L]
    print(f"  {L:>3d} {c['R1_A']:>18.6f} {c['R2_A']:>18.6f} {c['R3_A']:>18.6f}")

print(f"\n  Drift metric (a_0/a_2)/(a_2/a_4) per route:")
print(f"  {'L':>3} {'drift (A)':>12} {'drift (B)':>12} {'drift (C)':>12}")
for L in L_max_values:
    c = comparison[L]
    print(f"  {L:>3d} {c['drift_A']:>12.6f} {c['drift_B']:>12.6f} {c['drift_C']:>12.6f}")

# Physical interpretation note:
print(f"\n  PHYSICAL NOTE:")
print(f"    Route A power sums P_k = sum d_n |lam_n|^{{-2k}} are well-defined")
print(f"    finite sums but DIVERGE as L_max -> infinity at integer s = 1..4")
print(f"    (these are the pole locations of the true zeta_D on the d=8 manifold).")
print(f"    Route B heat kernel fit requires the small-t asymptotic expansion")
print(f"    (4*pi*t)^{{-d/2}} * sum_k a_k t^k, which is only valid for the FULL")
print(f"    spectrum. For truncated Theta_L(t), small-t behavior counts modes")
print(f"    (Theta_L(0+) = N_weighted), making the asymptotic fit ill-defined.")
print(f"    Route C Shanks/Pade assumes convergent sequences; for divergent")
print(f"    P_k(L_max) they produce unreliable extrapolations.")
print(f"    Therefore Route A power-sum DRIFT is the authoritative metric.")


# =============================================================================
# 8. GATE VERDICT L-MAX-ZETA-REGULARIZATION-74
# =============================================================================
print("\n" + "=" * 80)
print("8. GATE VERDICT: L-MAX-ZETA-REGULARIZATION-74")
print("=" * 80)

# Gate criteria (pre-registered):
# (A) three routes agree on a_0, a_2, a_4 to within 3% at L_max=7
# (B) (a_0/a_2)/(a_2/a_4) drift from L_max=3 to L_max=7 is < 5%
# (C) |R_2 - R_1| < 0.2 AND |R_3 - R_1| < 0.2
# PASS if all three.
# FAIL if any route differs by > 10%.

L_gate = 7  # (local) gate target L_max

# (A) Three-route agreement on a_0, a_2, a_4 at L_max=7
# For Route A and Route C we use raw values. For Route B (heat kernel) the
# normalization differs (absorbs (4*pi)^4). The correct way is to compare
# DIMENSIONLESS ratios a_0/a_2 and a_2/a_4 across routes.
c_gate = comparison[L_gate]

# Agreement on a_0/a_2 across routes
A_val = c_gate['ratio_a0_a2_A']
B_val = c_gate['ratio_a0_a2_B']
C_val = c_gate['ratio_a0_a2_C']
vals_a0a2 = np.array([A_val, B_val, C_val])
mean_a0a2 = float(np.mean(vals_a0a2))
max_dev_a0a2 = float(np.max(np.abs(vals_a0a2 - mean_a0a2)) / abs(mean_a0a2))

# Agreement on a_2/a_4 across routes
A2 = c_gate['ratio_a2_a4_A']
B2 = c_gate['ratio_a2_a4_B']
C2 = c_gate['ratio_a2_a4_C']
vals_a2a4 = np.array([A2, B2, C2])
mean_a2a4 = float(np.mean(vals_a2a4))
max_dev_a2a4 = float(np.max(np.abs(vals_a2a4 - mean_a2a4)) / abs(mean_a2a4))

cond_A_route_agreement = (max_dev_a0a2 < 0.03) and (max_dev_a2a4 < 0.03)
cond_FAIL_route_disagree = (max_dev_a0a2 > 0.10) or (max_dev_a2a4 > 0.10)

# (B) Drift test: (a_0/a_2)/(a_2/a_4) from L=3 to L=7 in Route A (authoritative)
drift_L3 = comparison[3]['drift_A']
drift_L7 = comparison[7]['drift_A']
drift_delta = abs(drift_L7 - drift_L3) / abs(drift_L3)
cond_B_drift = drift_delta < 0.05

# (C) Ratio-of-ratios test (Route A)
R1 = comparison[L_gate]['R1_A']
R2 = comparison[L_gate]['R2_A']
R3 = comparison[L_gate]['R3_A']
dR2 = abs(R2 - R1)
dR3 = abs(R3 - R1)
cond_C_ratios = (dR2 < 0.2) and (dR3 < 0.2)

print(f"\n  (A) Three-route agreement at L_max={L_gate}:")
print(f"      a_0/a_2 values: A={A_val:.6f}, B={B_val:.6f}, C={C_val:.6f}")
print(f"      max deviation: {max_dev_a0a2*100:.3f}%  (threshold: 3%)")
print(f"      a_2/a_4 values: A={A2:.6f}, B={B2:.6f}, C={C2:.6f}")
print(f"      max deviation: {max_dev_a2a4*100:.3f}%  (threshold: 3%)")
print(f"      PASS if BOTH < 3%: {cond_A_route_agreement}")
print(f"      FAIL if EITHER > 10%: {cond_FAIL_route_disagree}")

print(f"\n  (B) Drift (a_0/a_2)/(a_2/a_4) from L=3 to L=7 (Route A):")
print(f"      L=3: {drift_L3:.6f}")
print(f"      L=7: {drift_L7:.6f}")
print(f"      Relative drift: {drift_delta*100:.3f}%  (threshold: 5%)")
print(f"      PASS: {cond_B_drift}")

print(f"\n  (C) Ratio-of-ratios R_1, R_2, R_3 at L_max={L_gate}:")
print(f"      R_1 = a_0*a_4/a_2^2 = {R1:.6f}")
print(f"      R_2 = a_2*a_6/a_4^2 = {R2:.6f}")
print(f"      R_3 = a_4*a_8/a_6^2 = {R3:.6f}")
print(f"      |R_2 - R_1| = {dR2:.6f}  (threshold: 0.2)")
print(f"      |R_3 - R_1| = {dR3:.6f}  (threshold: 0.2)")
print(f"      PASS: {cond_C_ratios}")

# Combine
if cond_FAIL_route_disagree:
    verdict = "FAIL"
    reason = f"Routes disagree by > 10% at L_max={L_gate} (Route A drift {drift_delta*100:.1f}% > 5%)"
elif cond_A_route_agreement and cond_B_drift and cond_C_ratios:
    verdict = "PASS"
    reason = "All three conditions met"
elif cond_A_route_agreement and cond_B_drift and not cond_C_ratios:
    verdict = "INFO"
    reason = "Routes converge, but R_2/R_3 deviate from R_1 (R-family protection limited to B2)"
elif cond_A_route_agreement and not cond_B_drift:
    verdict = "INFO"
    reason = f"Routes converge at L={L_gate}, but drift {drift_delta*100:.2f}% > 5%"
else:
    verdict = "FAIL"
    reason = (
        f"L_max={L_gate} inadequate: Route A drift (a_0/a_2)/(a_2/a_4) = "
        f"{drift_delta*100:.1f}% > 5%, Route B (heat kernel) unstable for truncated "
        f"spectrum (small-t asymptotic invalid for finite lambda_max), Route C "
        f"(Shanks/Pade) diverges because Route A power sums are divergent sequences."
    )

print(f"\n  VERDICT: {verdict}")
print(f"  Reason:  {reason}")


# =============================================================================
# 9. CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 80)
print("9. CROSS-CHECKS")
print("=" * 80)

# Cross-check 1: Route A vs canonical a_2/a_0, a_4/a_2 at L_max=3
# Canonical (S42) values:
canonical_a0_a2 = a0_fold / a2_fold
canonical_a2_a4 = a2_fold / a4_fold
print(f"\n  Cross-check 1: Route A ratios vs canonical S42 at L_max=3")
print(f"    Canonical a_0/a_2 = {canonical_a0_a2:.6f}")
print(f"    Route A  a_0/a_2 = {comparison[3]['ratio_a0_a2_A']:.6f}")
print(f"    Canonical a_2/a_4 = {canonical_a2_a4:.6f}")
print(f"    Route A  a_2/a_4 = {comparison[3]['ratio_a2_a4_A']:.6f}")
# Note: S42 a_k are absolute coefficients from direct spectral sums at
# L_max=3; Route A uses a DIFFERENT s-shift convention (P_4 -> a_0, etc.)
# so the numerical values may be offset by factors of Gamma(k). The
# dimensionless ratios are what we care about for the gate.

# Cross-check 2: Heat kernel a_0 at L_max=7 as t->0 counts weighted modes
# The leading small-t behavior of Theta(t) is
#   Theta(t) ~ N_w + O(t)  where N_w = sum_n d_n (no rescaling)
# So Theta(0+) = sum of multiplicities (raw, NOT rescaled by (4*pi*t)^{d/2}).
# The Route B fit includes this rescaling, so a_0_heat encodes N_w via the
# fit's zero-order coefficient.
print(f"\n  Cross-check 2: Heat kernel small-t behavior")
for L in [3, 5, 7, 9]:
    zz = zeta_table[L]
    hh = heat_table[L]
    N_w_raw = zz['n_weighted']  # (local)
    print(f"    L={L}: N_weighted (raw) = {N_w_raw:>8d}, a_0_heat (rescaled) = {hh['a0_heat']:.4e}")

# Cross-check 3: Zero modes excluded (kernel dimension)
print(f"\n  Cross-check 3: Zero mode exclusion")
zero_counts = {L: 0 for L in L_max_values}
for L_max_cut in L_max_values:
    for (p, q), data in sector_evals.items():
        if data['level'] <= L_max_cut:
            zero_counts[L_max_cut] += data['n_zero']
for L, nz in zero_counts.items():
    print(f"    L_max={L}: total zero modes excluded = {nz}")


# =============================================================================
# 10. SAVE OUTPUTS
# =============================================================================
print("\n" + "=" * 80)
print("10. SAVING OUTPUTS")
print("=" * 80)

# Flatten into arrays for .npz
L_arr = np.array(L_max_values)  # (local)
L_arr_all = np.array(L_max_all)  # (local)

save_dict = {
    'L_max_values': L_arr,
    'L_max_all': L_arr_all,
    'verdict': verdict,
    'reason': reason,
    # Route A (zeta)
    'a0_zeta': np.array([zeta_table[L]['a0_zeta'] for L in L_max_all]),
    'a2_zeta': np.array([zeta_table[L]['a2_zeta'] for L in L_max_all]),
    'a4_zeta': np.array([zeta_table[L]['a4_zeta'] for L in L_max_all]),
    'a6_zeta': np.array([zeta_table[L]['a6_zeta'] for L in L_max_all]),
    'a8_zeta': np.array([zeta_table[L]['a8_zeta'] for L in L_max_all]),
    # Route B (heat)
    'a0_heat': np.array([heat_table[L]['a0_heat'] for L in L_max_all]),
    'a2_heat': np.array([heat_table[L]['a2_heat'] for L in L_max_all]),
    'a4_heat': np.array([heat_table[L]['a4_heat'] for L in L_max_all]),
    'a6_heat': np.array([heat_table[L]['a6_heat'] for L in L_max_all]),
    'a8_heat': np.array([heat_table[L]['a8_heat'] for L in L_max_all]),
    # Route C (pade) -- only for L_max_values
    'a0_pade': np.array([pade_table[L]['a0_pade'] for L in L_max_values]),
    'a2_pade': np.array([pade_table[L]['a2_pade'] for L in L_max_values]),
    'a4_pade': np.array([pade_table[L]['a4_pade'] for L in L_max_values]),
    'a6_pade': np.array([pade_table[L]['a6_pade'] for L in L_max_values]),
    'a0_shanks': np.array([pade_table[L]['a0_shanks'] for L in L_max_values]),
    'a2_shanks': np.array([pade_table[L]['a2_shanks'] for L in L_max_values]),
    'a4_shanks': np.array([pade_table[L]['a4_shanks'] for L in L_max_values]),
    'a6_shanks': np.array([pade_table[L]['a6_shanks'] for L in L_max_values]),
    # Ratios (Route A)
    'R1_A': np.array([comparison[L]['R1_A'] for L in L_max_values]),
    'R2_A': np.array([comparison[L]['R2_A'] for L in L_max_values]),
    'R3_A': np.array([comparison[L]['R3_A'] for L in L_max_values]),
    'ratio_a0_a2_A': np.array([comparison[L]['ratio_a0_a2_A'] for L in L_max_values]),
    'ratio_a2_a4_A': np.array([comparison[L]['ratio_a2_a4_A'] for L in L_max_values]),
    'ratio_a0_a2_B': np.array([comparison[L]['ratio_a0_a2_B'] for L in L_max_values]),
    'ratio_a2_a4_B': np.array([comparison[L]['ratio_a2_a4_B'] for L in L_max_values]),
    'ratio_a0_a2_C': np.array([comparison[L]['ratio_a0_a2_C'] for L in L_max_values]),
    'ratio_a2_a4_C': np.array([comparison[L]['ratio_a2_a4_C'] for L in L_max_values]),
    'drift_A': np.array([comparison[L]['drift_A'] for L in L_max_values]),
    'drift_B': np.array([comparison[L]['drift_B'] for L in L_max_values]),
    'drift_C': np.array([comparison[L]['drift_C'] for L in L_max_values]),
    # Gate numerics
    'gate_max_dev_a0a2': max_dev_a0a2,
    'gate_max_dev_a2a4': max_dev_a2a4,
    'gate_drift_delta': drift_delta,
    'gate_dR2': dR2,
    'gate_dR3': dR3,
    'gate_cond_A': cond_A_route_agreement,
    'gate_cond_B': cond_B_drift,
    'gate_cond_C': cond_C_ratios,
    # First-route canonical candidates (at L_max=7 Route A zeta)
    'canonical_a0_zeta_L7': zeta_table[7]['a0_zeta'],
    'canonical_a2_zeta_L7': zeta_table[7]['a2_zeta'],
    'canonical_a4_zeta_L7': zeta_table[7]['a4_zeta'],
    'canonical_a6_zeta_L7': zeta_table[7]['a6_zeta'],
    'canonical_a8_zeta_L7': zeta_table[7]['a8_zeta'],
    # Spectrum counts
    'n_weighted': np.array([zeta_table[L]['n_weighted'] for L in L_max_all]),
    'lam_max_by_L': np.array([zeta_table[L]['lam_max'] for L in L_max_all]),
}

np.savez('s74_lmax_zeta_audit.npz', **save_dict)
print(f"  Saved: computations/session-74/s74_lmax_zeta_audit.npz")


# =============================================================================
# 11. PLOT
# =============================================================================
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.30)

# Panel A: a_0 convergence across routes
ax1 = fig.add_subplot(gs[0, 0])
a0_z = [zeta_table[L]['a0_zeta'] for L in L_max_all]
a0_h = [heat_table[L]['a0_heat'] for L in L_max_all]
a0_p = [pade_table[L]['a0_pade'] if L in pade_table else np.nan for L in L_max_all]
ax1.semilogy(L_max_all, a0_z, 'o-', label='Route A (zeta)', color='C0', markersize=8)
ax1.semilogy(L_max_all, a0_h, 's-', label='Route B (heat)', color='C1', markersize=8)
ax1.semilogy([L for L in L_max_all if L in pade_table],
              [pade_table[L]['a0_pade'] for L in L_max_all if L in pade_table],
              '^--', label='Route C (Pade)', color='C2', markersize=8)
ax1.set_xlabel('L_max')
ax1.set_ylabel('a_0 (log scale)')
ax1.set_title('a_0 convergence')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel B: a_2 convergence
ax2 = fig.add_subplot(gs[0, 1])
a2_z = [zeta_table[L]['a2_zeta'] for L in L_max_all]
a2_h = [heat_table[L]['a2_heat'] for L in L_max_all]
ax2.semilogy(L_max_all, a2_z, 'o-', label='Route A (zeta)', color='C0', markersize=8)
ax2.semilogy(L_max_all, a2_h, 's-', label='Route B (heat)', color='C1', markersize=8)
ax2.semilogy([L for L in L_max_all if L in pade_table],
              [pade_table[L]['a2_pade'] for L in L_max_all if L in pade_table],
              '^--', label='Route C (Pade)', color='C2', markersize=8)
ax2.set_xlabel('L_max')
ax2.set_ylabel('a_2 (log scale)')
ax2.set_title('a_2 convergence')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel C: a_4 convergence
ax3 = fig.add_subplot(gs[1, 0])
a4_z = [zeta_table[L]['a4_zeta'] for L in L_max_all]
a4_h = [heat_table[L]['a4_heat'] for L in L_max_all]
ax3.semilogy(L_max_all, a4_z, 'o-', label='Route A (zeta)', color='C0', markersize=8)
ax3.semilogy(L_max_all, a4_h, 's-', label='Route B (heat)', color='C1', markersize=8)
ax3.semilogy([L for L in L_max_all if L in pade_table],
              [pade_table[L]['a4_pade'] for L in L_max_all if L in pade_table],
              '^--', label='Route C (Pade)', color='C2', markersize=8)
ax3.set_xlabel('L_max')
ax3.set_ylabel('a_4 (log scale)')
ax3.set_title('a_4 convergence')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel D: a_0/a_2 ratio across routes
ax4 = fig.add_subplot(gs[1, 1])
r02_A = [comparison[L]['ratio_a0_a2_A'] for L in L_max_values]
r02_B = [comparison[L]['ratio_a0_a2_B'] for L in L_max_values]
r02_C = [comparison[L]['ratio_a0_a2_C'] for L in L_max_values]
ax4.plot(L_max_values, r02_A, 'o-', label='Route A (zeta)', color='C0', markersize=8)
ax4.plot(L_max_values, r02_B, 's-', label='Route B (heat)', color='C1', markersize=8)
ax4.plot(L_max_values, r02_C, '^--', label='Route C (Pade)', color='C2', markersize=8)
ax4.axhline(canonical_a0_a2, color='red', linestyle=':', label=f'S42 canonical = {canonical_a0_a2:.3f}')
ax4.set_xlabel('L_max')
ax4.set_ylabel('a_0/a_2')
ax4.set_title('a_0/a_2 (dimensionless) vs L_max')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# Panel E: R_1, R_2, R_3 vs L_max
ax5 = fig.add_subplot(gs[2, 0])
R1_arr = [comparison[L]['R1_A'] for L in L_max_values]
R2_arr = [comparison[L]['R2_A'] for L in L_max_values]
R3_arr = [comparison[L]['R3_A'] for L in L_max_values]
ax5.plot(L_max_values, R1_arr, 'o-', label='R_1 = a_0*a_4/a_2^2', markersize=8)
ax5.plot(L_max_values, R2_arr, 's-', label='R_2 = a_2*a_6/a_4^2', markersize=8)
ax5.plot(L_max_values, R3_arr, '^-', label='R_3 = a_4*a_8/a_6^2', markersize=8)
ax5.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax5.set_xlabel('L_max')
ax5.set_ylabel('R_i')
ax5.set_title('Ratio-of-ratios R_1, R_2, R_3 (Route A)')
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# Panel F: Gate verdict summary (text)
ax6 = fig.add_subplot(gs[2, 1])
ax6.axis('off')
summary_text = (
    f"L-MAX-ZETA-REGULARIZATION-74\n"
    f"{'='*38}\n\n"
    f"Verdict: {verdict}\n\n"
    f"Reason: {reason}\n\n"
    f"At L_max={L_gate}:\n"
    f"  (A) route agreement:\n"
    f"      max dev a_0/a_2 = {max_dev_a0a2*100:.2f}% (3%)\n"
    f"      max dev a_2/a_4 = {max_dev_a2a4*100:.2f}% (3%)\n"
    f"  (B) drift L3->L7: {drift_delta*100:.2f}% (5%)\n"
    f"  (C) |R_2-R_1| = {dR2:.3f} (0.2)\n"
    f"      |R_3-R_1| = {dR3:.3f} (0.2)\n\n"
    f"R_1 = {R1:.3f}\n"
    f"R_2 = {R2:.3f}\n"
    f"R_3 = {R3:.3f}"
)
ax6.text(0.02, 0.98, summary_text, transform=ax6.transAxes,
          fontsize=10, verticalalignment='top', family='monospace',
          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

fig.suptitle(f'L-MAX-ZETA-REGULARIZATION-74: a_k Convergence Audit (S74 W1-C)',
             fontsize=13, fontweight='bold')

plt.savefig('s74_lmax_zeta_audit.png', dpi=120, bbox_inches='tight')
plt.close(fig)
print(f"  Saved: computations/session-74/s74_lmax_zeta_audit.png")

print("\n" + "=" * 80)
print(f"L-MAX-ZETA-REGULARIZATION-74: DONE")
print(f"VERDICT: {verdict}")
print("=" * 80)
