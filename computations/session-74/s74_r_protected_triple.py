#!/usr/bin/env python3
"""
s74_r_protected_triple.py -- R-PROTECTED-TRIPLE-74 (W2-O)
==========================================================

Gate: R-PROTECTED-TRIPLE-74
  Task: Compute R_protected_fold = a_0 * a_4 / a_2^2 via three independent
        routes and check whether they agree to within 3%.

    Route A: Spectral partial sum in the S73B project convention at L_max=7.
             a_0^A = 0.5 * P_0     (half the mode count)
             a_2^A = 0.5 * P_1 = 0.5 * sum d_n / lam_n^2
             a_4^A = 0.5 * P_2 = 0.5 * sum d_n / lam_n^4
             R^A   = a_0^A * a_4^A / (a_2^A)^2
             (The 0.5 factors cancel in the ratio; Vol(SU(3)) cancels per
              Baptista B2.)

    Route B: Direct curvature invariant from the Jensen metric (Gilkey
             Seeley-DeWitt formula for the spin-Dirac Laplacian on (SU(3),
             g_Jensen(tau=0.19)).
             a_0^G = (4pi)^{-4} * 16 * Vol
             a_2^G = (4pi)^{-4} * (20R/3) * Vol
             a_4^G = (4pi)^{-4} * (1/360)*(500R^2 - 32|Ric|^2 - 28K) * Vol
             R^B   = a_0^G * a_4^G / (a_2^G)^2
             (All (4pi)^{-4} and Vol factors cancel; only curvature invariants
              remain. Route B is the exact L_max = infinity value of the
              heat-kernel Seeley-DeWitt coefficients.)

    Route C: Zeta-regulated analytic continuation. The spectral partial sums
             a_k^A are the finite-L_max truncation of the (divergent) spectral
             zeta function. The ratio R^A stays finite because the leading
             Weyl divergences cancel, but sub-leading corrections drift with
             L_max. Route C extrapolates R^A(L_max) to L_max -> infinity via
             a three-parameter power-law fit R(L) = R_inf - A * L^(-alpha).
             Route C uses the SAME convention as Route A (S73B project); it
             simply estimates the L_max -> infinity limit of the same ratio.

  PASS if max_ij |R^i - R^j| / |R^i| < 3%
  INFO if max deviation is in [3%, 10%]
  FAIL if max deviation is > 10%

Physics (substrate framing):
----------------------------
R_protected is meant to be a dimensionless invariant of the substrate at
the Jensen fold. Three routes test whether the quantity is actually a
scheme-independent observable:

  Route A uses the project's preferred partial-sum recipe (what entered
  canonical_constants.py via W1-M).

  Route B uses the mathematically rigorous heat-kernel Seeley-DeWitt
  coefficients, which are exact functions of the local curvature
  invariants R, |Ric|^2, K = |Riem|^2 of the Jensen metric. These are the
  L_max = infty values by definition -- the a_k that appear in the
  Chamseddine-Connes spectral action, Tr(f(D/Lambda)) ~ (4pi)^{-4} *
  sum_k f_{d-2k} Lambda^{d-2k} a_k.

  Route C uses the same spectrum as Route A, but extrapolates to
  L_max = infty using a power-law fit on the ratio (not on individual a_k,
  which individually diverge).

If Routes A and B agree numerically, then the partial-sum recipe is a
faithful discretization of the Gilkey heat-kernel invariant. If they do
not, the two quantities measure different things -- the partial-sum
ratio is a *truncated zeta function* quantity, and the Gilkey ratio
is a curvature-invariant polynomial quantity. They would only agree if
the partial-sum divergences in numerator and denominator cancel all the
way through to the finite residue scale.

Both routes are legitimate spectral observables; the gate is whether
they numerically coincide under the L_max=7 convention. The outcome
tells us whether R_protected is protected against convention choice or
only against L_max choice within one convention.

Agent: Spectral-Geometer (Session 74, Wave 2, Batch 3, W2-O)
Parent dependencies:
  - W1-M R-PROTECTED-FOLD-ADDITION-74 (established S73B canonical value 1.128655)
  - W1-C L-MAX-ZETA-REGULARIZATION-74 (provided Wodzicki partial sums + spectrum cache)
  - S73B landau-baptista workshop action #3 (three-route agreement test)
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

from canonical_constants import (
    PI, M_KK, tau_fold, Vol_SU3_Haar,
    a0_fold, a2_fold, a4_fold,
)

# R_protected_fold (from W1-M addition proposal; not yet in canonical_constants.py)
R_PROTECTED_CANONICAL = 1.128655  # (local)

# =============================================================================
# 0. HEADER
# =============================================================================
print("=" * 80)
print("R-PROTECTED-TRIPLE-74: Triple-Route R_protected Computation")
print("S74 W2-O | spectral-geometer")
print("=" * 80)
print()
print(f"  tau_fold = {tau_fold}")
print(f"  Vol_SU3_Haar = {Vol_SU3_Haar}")
print(f"  W1-M canonical R_protected_fold = {R_PROTECTED_CANONICAL}")
print()
print("  Gate: PASS if max deviation < 3%, INFO in [3%, 10%], FAIL > 10%.")
print("  Convention: all three routes reported in S73B project convention.")
print()

t_start = time.time()


# =============================================================================
# 1. LOAD INPUTS: W1-C SPECTRUM CACHE AND ZETA AUDIT
# =============================================================================
print("=" * 80)
print("1. LOAD W1-C INPUTS")
print("=" * 80)

# Full Dirac spectrum at tau=0.19, L_max=9 (missing 3 conjugate sectors at L>=8)
cache_path = "s74_spectrum_cache_L9_tau019.npz"
cache = np.load(cache_path, allow_pickle=True)
sector_evals = cache['sector_evals'].item()

# W1-C zeta audit (Wodzicki partial sums per L_max)
audit_path = "s74_lmax_zeta_audit.npz"
audit = np.load(audit_path, allow_pickle=True)
L_max_all = audit['L_max_all']  # [3,4,5,6,7,8,9]
a0_Wz_L = audit['a0_zeta']      # P_4 per L_max (Wodzicki: a_0 = zeta_D(4))
a2_Wz_L = audit['a2_zeta']      # P_3
a4_Wz_L = audit['a4_zeta']      # P_2
a6_Wz_L = audit['a6_zeta']      # P_1
a8_Wz_L = audit['a8_zeta']      # P_0 (mode count)

print(f"  Cache: {cache_path}")
print(f"    sectors present: {len(sector_evals)}")
print(f"  Audit: {audit_path}")
print(f"    L_max values: {L_max_all}")
print()

# Completeness check: cache is complete for L_max in {3,...,7}; (4,4) missing at L=8,
# and (4,4),(4,5),(5,4) missing at L=9 because the Cartan-Weyl fallback cannot
# build self-conjugate (p=q) sectors above (3,3).
def pq_weight(p, q):
    """SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

complete_L_max = []  # (local) L_max values for which the cache is complete
for L in range(3, 10):
    expected = set((p, q) for p in range(L + 1) for q in range(L + 1) if p + q <= L)
    present = set((p, q) for (p, q) in sector_evals.keys() if p + q <= L)
    missing = expected - present  # (local)
    if not missing:
        complete_L_max.append(L)
    status = "COMPLETE" if not missing else f"MISSING {sorted(missing)}"
    print(f"    L_max={L}: {status}")
print(f"  Complete L_max range: {complete_L_max}")
print()

assert 7 in complete_L_max, "Cache must be complete at L_max=7 for Route A"


# =============================================================================
# 2. ROUTE A: SPECTRAL PARTIAL SUM IN S73B CONVENTION AT L_max=7
# =============================================================================
print("=" * 80)
print("2. ROUTE A: Spectral Partial Sum (S73B Convention)")
print("=" * 80)


def partial_sums_S73B(L_max):
    """
    Compute the S73B-convention partial sums at a given L_max.

    S73B convention (canonical project convention, used by S42/W1-M):
        P_0 = sum_{(p,q) : p+q <= L_max} dim(p,q) * len(abs_evals_{(p,q)})
        P_k = sum_{(p,q) : p+q <= L_max} dim(p,q) * sum_n |lam_n^{(p,q)}|^{-k}

    Seeley-DeWitt mapping (project convention):
        a_0^{S73B} = 0.5 * P_0
        a_2^{S73B} = 0.5 * P_1
        a_4^{S73B} = 0.5 * P_2

    Returns dict with P_0..P_4 and a_0, a_2, a_4 in S73B convention.
    """
    P_0 = 0.0  # (local)
    P_1 = 0.0  # (local)
    P_2 = 0.0  # (local)
    P_3 = 0.0  # (local)
    P_4 = 0.0  # (local)
    for (p, q), v in sector_evals.items():
        if p + q > L_max:
            continue
        d_pq = pq_weight(p, q)
        abs_evals = v['abs_evals']
        w = d_pq  # (local) outer PW multiplier
        P_0 += w * len(abs_evals)
        P_1 += w * float(np.sum(abs_evals ** (-2)))
        P_2 += w * float(np.sum(abs_evals ** (-4)))
        P_3 += w * float(np.sum(abs_evals ** (-6)))
        P_4 += w * float(np.sum(abs_evals ** (-8)))
    return {
        'P_0': P_0, 'P_1': P_1, 'P_2': P_2, 'P_3': P_3, 'P_4': P_4,
        'a0_S73B': 0.5 * P_0,
        'a2_S73B': 0.5 * P_1,
        'a4_S73B': 0.5 * P_2,
    }


# L_max sweep for extrapolation (Route C)
R_A_by_L = {}  # (local) Route A per L_max
for L in complete_L_max:
    ps = partial_sums_S73B(L)
    a0 = ps['a0_S73B']
    a2 = ps['a2_S73B']
    a4 = ps['a4_S73B']
    R_A_by_L[L] = {
        'a0': a0, 'a2': a2, 'a4': a4,
        'R_protected': a0 * a4 / a2 ** 2,
    }

# Canonical Route A value at L_max=7
ps_7 = partial_sums_S73B(7)
a0_A = ps_7['a0_S73B']
a2_A = ps_7['a2_S73B']
a4_A = ps_7['a4_S73B']
R_protected_A = a0_A * a4_A / a2_A ** 2

# Cross-check against W1-C cache at L_max=3 (canonical W1-M value)
ps_3 = partial_sums_S73B(3)
R_protected_A_L3 = ps_3['a0_S73B'] * ps_3['a4_S73B'] / ps_3['a2_S73B'] ** 2

print(f"  L_max sweep (S73B convention, complete cache only):")
print(f"  {'L_max':>6} {'a_0':>14} {'a_2':>14} {'a_4':>14} {'R_protected':>14}")
for L in complete_L_max:
    r = R_A_by_L[L]
    print(f"  {L:>6d} {r['a0']:>14.6e} {r['a2']:>14.6e} {r['a4']:>14.6e} "
          f"{r['R_protected']:>14.6f}")
print()
print(f"  [L_max=3] R_protected^A = {R_protected_A_L3:.6f}  (W1-M canonical: "
      f"{R_PROTECTED_CANONICAL})")
print(f"  [L_max=7] R_protected^A = {R_protected_A:.6f}")
print(f"  L_max drift (L=3 -> L=7) = "
      f"{100 * (R_protected_A - R_protected_A_L3) / R_protected_A_L3:+.4f}%")
print()

# Cross-check of Route A via W1-C audit (Wodzicki labels, relabeled to S73B)
# a_0^{S73B} = 0.5 * P_0 = 0.5 * a8_Wz
# a_2^{S73B} = 0.5 * P_1 = 0.5 * a6_Wz
# a_4^{S73B} = 0.5 * P_2 = 0.5 * a4_Wz
idx_L7 = int(np.where(L_max_all == 7)[0][0])  # (local)
R_A_via_audit_L7 = (0.5 * a8_Wz_L[idx_L7]) * (0.5 * a4_Wz_L[idx_L7]) / (0.5 * a6_Wz_L[idx_L7]) ** 2
print(f"  [W1-C audit cross-check at L=7] R^A = {R_A_via_audit_L7:.6f} "
      f"(should match {R_protected_A:.6f})")
assert abs(R_A_via_audit_L7 - R_protected_A) < 1e-8, \
    "W1-C audit reprocessing of S73B convention must agree with direct partial sum"
print(f"  Cross-check: PASS (|diff| = {abs(R_A_via_audit_L7 - R_protected_A):.2e})")
print()


# =============================================================================
# 3. ROUTE B: DIRECT CURVATURE INVARIANT FROM JENSEN METRIC (GILKEY)
# =============================================================================
print("=" * 80)
print("3. ROUTE B: Gilkey Curvature Invariant at tau_fold")
print("=" * 80)


def R_scalar(tau):
    """
    Exact scalar curvature R(tau) on Jensen-deformed SU(3).
    Provenance: S20a 147/147 Riemann component verification, reused
    across S61, S46, S52. R(0) = 2.0 exactly (bi-invariant metric is
    Einstein: Ric = (R/8) g).
    """
    return -0.25 * np.exp(-4 * tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2 * tau)


def Ric2_exact(tau):
    """
    Exact |Ric|^2(tau) = Ric_{ab} Ric^{ab} on Jensen-deformed SU(3).
    Closed-form polynomial in exp(tau).
    Provenance: s22c_higgs_sigma.py (SP-2 formula, machine epsilon).
    |Ric|^2(0) = 0.5 exactly.
    """
    return (
        (1.0 / 12) * np.exp(-8 * tau)
        + (-1.0 / 2) * np.exp(-5 * tau)
        + (1.0 / 8) * np.exp(-4 * tau)
        + (13.0 / 12) * np.exp(-2 * tau)
        + (-1.0 / 2) * np.exp(-tau)
        + 1.0 / 8
        + (1.0 / 12) * np.exp(4 * tau)
    )


def K_exact(tau):
    """
    Exact Kretschmann scalar K(tau) = R_{abcd} R^{abcd} on Jensen-deformed SU(3).
    Provenance: r20a_riemann_tensor.py.
    K(0) = 0.5 exactly.
    """
    return (
        (23.0 / 96) * np.exp(-8 * tau)
        + (-1.0) * np.exp(-5 * tau)
        + (5.0 / 16) * np.exp(-4 * tau)
        + (11.0 / 6) * np.exp(-2 * tau)
        + (-3.0 / 2) * np.exp(-tau)
        + 17.0 / 32
        + (1.0 / 12) * np.exp(4 * tau)
    )


def gilkey_a0_a2_a4(tau):
    """
    Gilkey Seeley-DeWitt coefficients a_0, a_2, a_4 for the spin-Dirac
    Laplacian D_K^2 on (SU(3), g_Jensen(tau)).

    Conventions:
        E = -R/4 * I_{16}  (Lichnerowicz square)  # (local)
        d = 8  # (local)
        rank(S_8) = 16
        No connection curvature Omega beyond gravitational at a_2.

    Formulas:
        a_0 = (4pi)^{-d/2} * rank(S) * Vol(K)
            = (4pi)^{-4} * 16 * Vol_SU3_Haar

        a_2 = (4pi)^{-d/2} * int_K tr_S(R/6 - E) dvol
            = (4pi)^{-4} * 16 * (5R/12) * Vol
            = (4pi)^{-4} * (20 R / 3) * Vol

        a_4 = (4pi)^{-d/2} * int_K tr_S[5R^2 - 2|Ric|^2 + 2K
                                        + 60 R E + 180 E^2
                                        + 30 Omega^2
                                        + 12 nabla^2 R] / 360 dvol
            = (4pi)^{-4} * (1/360) * (500 R^2 - 32 |Ric|^2 - 28 K) * Vol

    The detailed expansion (verified in S61 HK-RATIO-61 and S46):
        tr_S(60 R E)    = 60 R * tr_S(-R/4) = 60 R * (-4R) = -240 R^2
        tr_S(180 E^2)   = 180 * tr_S(R^2/16) = 180 * R^2 = 180 R^2
        ... (see s61_heat_kernel_a4.py for full derivation)
    Final combination (homogeneous space, constant curvature):
        500 R^2 - 32 |Ric|^2 - 28 K
    """
    R = R_scalar(tau)
    Ric2 = Ric2_exact(tau)
    K = K_exact(tau)
    pref = (4 * PI) ** (-4)
    a0 = pref * 16.0 * Vol_SU3_Haar
    a2 = pref * (20.0 / 3.0) * R * Vol_SU3_Haar
    a4 = pref * (1.0 / 360.0) * (500.0 * R ** 2 - 32.0 * Ric2 - 28.0 * K) * Vol_SU3_Haar
    return a0, a2, a4, R, Ric2, K


a0_B, a2_B, a4_B, R_fold, Ric2_fold, K_fold = gilkey_a0_a2_a4(tau_fold)
R_protected_B = a0_B * a4_B / a2_B ** 2

# Closed-form check: the (4pi)^{-4} and Vol cancel exactly in the ratio.
# R_protected^B = [16 * (500 R^2 - 32|Ric|^2 - 28K) / 360] / [(20 R/3)^2]
#               = (16 * 9 / (360 * 400)) * (500 R^2 - 32|Ric|^2 - 28K) / R^2
#               = (1/1000) * (500 - 32 |Ric|^2/R^2 - 28 K/R^2)
#               = 0.5 - 0.032 * (|Ric|^2/R^2) - 0.028 * (K/R^2)
closed_form = 0.5 - 0.032 * (Ric2_fold / R_fold ** 2) - 0.028 * (K_fold / R_fold ** 2)

print(f"  Jensen metric invariants at tau = {tau_fold}:")
print(f"    R(tau_fold)     = {R_fold:.10f}   [R(0) = 2.0]")
print(f"    |Ric|^2(tau_fold) = {Ric2_fold:.10f}   [|Ric|^2(0) = 0.5]")
print(f"    K(tau_fold)     = {K_fold:.10f}   [K(0) = 0.5]")
print()
print(f"  Gilkey Seeley-DeWitt coefficients (include (4pi)^{{-4}} * Vol factor):")
print(f"    a_0^G = (4pi)^{{-4}} * 16 * Vol       = {a0_B:.10f}")
print(f"    a_2^G = (4pi)^{{-4}} * (20R/3) * Vol  = {a2_B:.10f}")
print(f"    a_4^G = (4pi)^{{-4}} * (1/360) * (500R^2 - 32|Ric|^2 - 28K) * Vol")
print(f"          = {a4_B:.10f}")
print()
print(f"  R_protected^B (Gilkey) = a_0^G * a_4^G / (a_2^G)^2 = {R_protected_B:.6f}")
print(f"  Closed form (no (4pi) or Vol): (1/1000)*(500 - 32|Ric|^2/R^2 - 28 K/R^2)")
print(f"                                = {closed_form:.6f}")
print(f"  Consistency: |R^B - closed_form| = {abs(R_protected_B - closed_form):.2e}")
print()

# Sanity check at tau = 0 (bi-invariant limit)
a0_0, a2_0, a4_0, R_0, Ric2_0, K_0 = gilkey_a0_a2_a4(0.0)
R_B_at_0 = a0_0 * a4_0 / a2_0 ** 2
R_B_closed_0 = (1.0 / 1000.0) * (500.0 - 32.0 * 0.5 / 4.0 - 28.0 * 0.5 / 4.0)
# At tau=0: R=2, |Ric|^2=0.5, K=0.5, R^2=4
# => (1/1000)*(500 - 32*0.5/4 - 28*0.5/4) = (1/1000)*(500 - 4 - 3.5) = 492.5/1000 = 0.4925
print(f"  Bi-invariant sanity check at tau=0:")
print(f"    R(0)={R_0}, |Ric|^2(0)={Ric2_0}, K(0)={K_0}")
print(f"    R_protected^B(0) = {R_B_at_0:.6f}   closed form: {R_B_closed_0}")
print(f"    Exact at tau=0: 492.5/1000 = 0.4925")
print()


# =============================================================================
# 4. ROUTE C: ZETA ANALYTIC CONTINUATION (POWER-LAW EXTRAPOLATION TO L=infty)
# =============================================================================
print("=" * 80)
print("4. ROUTE C: Zeta Analytic Continuation (L_max -> infty Extrapolation)")
print("=" * 80)

# Route C strategy: fit R_protected^A(L) with a power-law model and extract
# the L_max -> infty limit. This is the analytic-continuation proxy -- the
# individual partial sums a_k^A diverge as L^{d-2k} in the Weyl regime, but
# the ratio R^A is finite at each L and has a controlled drift. Power-law
# extrapolation estimates the continuum / analytically-continued value.

L_range_C = np.array([L for L in complete_L_max])  # [3,4,5,6,7]
R_range_C = np.array([R_A_by_L[L]['R_protected'] for L in L_range_C])

print(f"  Route A sequence (input to Route C extrapolation):")
for L, R in zip(L_range_C, R_range_C):
    print(f"    L_max = {L}: R^A = {R:.6f}")
print()


def power_law_model(L, R_inf, A, alpha):
    """R(L) = R_inf - A * L^(-alpha). Finite limit at L=infty."""
    return R_inf - A * L ** (-alpha)


# Three-parameter power-law fit
try:
    popt_pl, pcov_pl = curve_fit(
        power_law_model, L_range_C, R_range_C,
        p0=[1.15, 0.1, 1.0],
        maxfev=20000,
    )
    R_inf_pl = popt_pl[0]
    A_pl = popt_pl[1]
    alpha_pl = popt_pl[2]
    residuals_pl = R_range_C - power_law_model(L_range_C, *popt_pl)
    print(f"  Power-law fit R(L) = R_inf - A*L^(-alpha):")
    print(f"    R_inf = {R_inf_pl:.6f}")
    print(f"    A     = {A_pl:.6f}")
    print(f"    alpha = {alpha_pl:.4f}")
    print(f"    residuals: {residuals_pl}")
    print(f"    max |residual|: {np.max(np.abs(residuals_pl)):.2e}")
except Exception as e:
    print(f"  Power-law fit FAILED: {e}")
    R_inf_pl = float(R_range_C[-1])
    A_pl = np.nan
    alpha_pl = np.nan
print()

# Cross-check: linear 1/L model
def inv_L_model(L, R_inf, B):
    return R_inf - B / L

try:
    popt_inv, _ = curve_fit(inv_L_model, L_range_C, R_range_C, p0=[1.15, 0.1])
    R_inf_inv = popt_inv[0]
    print(f"  Linear 1/L fit cross-check:")
    print(f"    R_inf (1/L) = {R_inf_inv:.6f}")
    print(f"    residuals:  {R_range_C - inv_L_model(L_range_C, *popt_inv)}")
except Exception:
    R_inf_inv = R_inf_pl
print()

# Cross-check: Aitken Delta^2
def aitken(seq):
    n = len(seq)
    if n < 3:
        return np.array([])
    s = np.zeros(n - 2)
    for i in range(n - 2):
        d = seq[i + 2] - 2 * seq[i + 1] + seq[i]
        if abs(d) < 1e-16:
            s[i] = seq[i + 1]
        else:
            s[i] = seq[i] - (seq[i + 1] - seq[i]) ** 2 / d
    return s

aitken_d1 = aitken(R_range_C)
aitken_d2 = aitken(aitken_d1) if len(aitken_d1) >= 3 else np.array([])
print(f"  Aitken Delta^2 cross-check:")
print(f"    Depth 1: {aitken_d1}")
if len(aitken_d2) > 0:
    print(f"    Depth 2: {aitken_d2}")
R_aitken = float(aitken_d1[-1]) if len(aitken_d1) > 0 else R_range_C[-1]
print(f"    Estimate (deepest value): {R_aitken:.6f}")
print()

# Primary Route C value: power-law fit extrapolation
R_protected_C = R_inf_pl
print(f"  Primary Route C value (power-law): R^C = {R_protected_C:.6f}")
print()


# =============================================================================
# 5. ROUTE COMPARISON AND GATE EVALUATION
# =============================================================================
print("=" * 80)
print("5. TRIPLE-ROUTE COMPARISON")
print("=" * 80)

routes = {
    'A': R_protected_A,
    'B': R_protected_B,
    'C': R_protected_C,
}
print(f"  Route A (spectral partial sum, L_max=7, S73B conv):  {routes['A']:.6f}")
print(f"  Route B (Gilkey curvature invariant, tau_fold):      {routes['B']:.6f}")
print(f"  Route C (zeta extrapolation L_max -> infty):         {routes['C']:.6f}")
print()

# Pairwise fractional deviations
pairs = [('A', 'B'), ('A', 'C'), ('B', 'C')]
pair_devs = {}
for (i, j) in pairs:
    diff = routes[i] - routes[j]
    # Fractional relative to the first-route value
    frac = abs(diff) / abs(routes[i])
    pair_devs[(i, j)] = frac
    print(f"  |R^{i} - R^{j}| / |R^{i}| = {frac * 100:.4f}%   "
          f"(R^{i}={routes[i]:.6f}, R^{j}={routes[j]:.6f})")
print()

max_dev = max(pair_devs.values())
print(f"  MAX pairwise deviation: {max_dev * 100:.4f}%")
print()

# Gate verdict
if max_dev < 0.03:
    verdict = "PASS"
    verdict_msg = "All three routes agree within 3% in the S73B convention."
elif max_dev <= 0.10:
    verdict = "INFO"
    verdict_msg = f"Routes agree within 10% but not 3% ({max_dev * 100:.2f}% max dev)."
else:
    verdict = "FAIL"
    verdict_msg = f"Routes disagree by >10% ({max_dev * 100:.2f}% max dev)."

print(f"  GATE VERDICT: {verdict}")
print(f"  {verdict_msg}")
print()


# =============================================================================
# 6. STRUCTURAL ANALYSIS
# =============================================================================
print("=" * 80)
print("6. STRUCTURAL ANALYSIS")
print("=" * 80)

# Check: are Routes A and B fundamentally different quantities, or do they
# differ by a known normalization factor?
ratio_AB = routes['A'] / routes['B']
ratio_AC = routes['A'] / routes['C']
ratio_BC = routes['B'] / routes['C']
print(f"  Route ratios:")
print(f"    R^A / R^B = {ratio_AB:.6f}")
print(f"    R^A / R^C = {ratio_AC:.6f}")
print(f"    R^B / R^C = {ratio_BC:.6f}")
print()

# Route A / Route C: how far is L_max=7 from the extrapolated limit?
A_vs_C_drift = abs(routes['A'] - routes['C']) / routes['C'] * 100
print(f"  Route A (L_max=7) vs Route C (extrapolated): {A_vs_C_drift:.3f}% drift")
print(f"    This is the residual Weyl-divergence drift at L_max=7.")
print()

# Route A vs Route B interpretation:
# The partial sum in S73B convention sums |lam|^{-k} for k = 0, 1, 2.
# The Gilkey Seeley-DeWitt a_k is (4pi)^{-d/2}*(polynomial in curvature)*Vol.
# These are NOT equal in general -- they are related by the Mellin/heat-kernel
# identity only at specific residue points, and the correspondence breaks down
# when the partial sum is truncated at finite L_max.
AB_ratio_exact = 0.5 - 0.032 * (Ric2_fold / R_fold ** 2) - 0.028 * (K_fold / R_fold ** 2)
# Route B exactly = 0.4923 at tau_fold (curvature-invariant polynomial)
# Route A = 1.1407 at L_max=7 (truncated zeta sum)
# Their ratio ~2.32 reflects the fundamentally different normalizations.
print(f"  Route B (Gilkey exact): {R_protected_B:.6f}")
print(f"  Route B (closed form at tau_fold):")
print(f"    (1/1000) * (500 - 32 * |Ric|^2/R^2 - 28 * K/R^2)")
print(f"    = (1/1000) * (500 - 32 * {Ric2_fold/R_fold**2:.6f} - 28 * {K_fold/R_fold**2:.6f})")
print(f"    = {AB_ratio_exact:.6f}")
print()

print("  INTERPRETATION:")
print("    Route A (S73B partial sum): truncated spectral zeta ratio.")
print("      Sums at |lam|^0, |lam|^{-2}, |lam|^{-4}. At L_max=7 the individual")
print("      a_k diverge as L^{d-2k}*Vol (Weyl law); only the ratio is finite")
print("      because leading Weyl divergences cancel. Residual drift ~ 1%/step.")
print()
print("    Route B (Gilkey): exact heat-kernel Seeley-DeWitt coefficients.")
print("      a_k are defined by the small-t expansion of Tr(e^{-tD^2}) and are")
print("      polynomial in the local curvature invariants R, |Ric|^2, K.")
print("      Independent of any L_max; exactly R^B = 0.4923 at tau = 0.19.")
print()
print("    Route C (zeta extrapolation): L_max -> infty of Route A's ratio.")
print("      Power-law fit recovers the L-infinity limit of the partial-sum ratio,")
print("      independent of truncation drift. R^C ~ 1.15 -- a finite limit,")
print("      reflecting that the leading Weyl corrections leave a residual ratio.")
print()
print("    Routes A and C converge to a partial-sum-ratio limit ~1.15, while")
print("    Route B gives the curvature-polynomial limit ~0.49. These differ by")
print("    a factor of ~2.33 because they are DIFFERENT mathematical objects:")
print("    Route A/C compute the truncated-spectrum ratio; Route B computes the")
print("    Gilkey-polynomial ratio. They have the same symbolic label 'R_protected'")
print("    but different definitions. The S73B/canonical convention uses Route A.")
print()


# =============================================================================
# 7. CROSS-CHECKS
# =============================================================================
print("=" * 80)
print("7. CROSS-CHECKS")
print("=" * 80)

# X1: Route A at L_max=7 should match W1-M expected drift from L=3
# W1-M canonical: R(L=3) = 1.128655; drift to L=7 should be 1.067%.
expected_R_A_L7 = R_protected_A_L3 * 1.01067
X1_pass = abs(R_protected_A - expected_R_A_L7) / expected_R_A_L7 < 0.01
print(f"  X1: Route A at L_max=7 consistent with W1-M drift 1.067%?")
print(f"      Expected R^A (L=7) = R(L=3) * 1.01067 = {expected_R_A_L7:.6f}")
print(f"      Computed R^A (L=7) = {R_protected_A:.6f}")
print(f"      Relative diff: {abs(R_protected_A - expected_R_A_L7) / expected_R_A_L7 * 100:.4f}%")
print(f"      X1: {'PASS' if X1_pass else 'FAIL'}")
print()

# X2: Gilkey ratio at tau=0 closed form
R_B_tau0_exact = 0.4925  # (local)
X2_pass = abs(R_B_at_0 - R_B_tau0_exact) < 1e-10
print(f"  X2: Gilkey Route B at tau=0 equals exact closed form 0.4925?")
print(f"      Computed: {R_B_at_0:.10f}")
print(f"      Expected: {R_B_tau0_exact:.10f}")
print(f"      X2: {'PASS' if X2_pass else 'FAIL'}")
print()

# X3: Vol(SU(3)) cancellation in Route B
# Compute Route B with Vol scaled by various factors; ratio must be invariant.
def gilkey_scaled(tau, vol_factor):
    R = R_scalar(tau)
    Ric2 = Ric2_exact(tau)
    K = K_exact(tau)
    vol = Vol_SU3_Haar * vol_factor
    pref = (4 * PI) ** (-4)
    a0 = pref * 16.0 * vol
    a2 = pref * (20.0 / 3.0) * R * vol
    a4 = pref * (1.0 / 360.0) * (500.0 * R ** 2 - 32.0 * Ric2 - 28.0 * K) * vol
    return a0 * a4 / a2 ** 2

vol_test = [0.5, 1.0, 2.0, 5.0, 100.0]
R_B_scaled = [gilkey_scaled(tau_fold, f) for f in vol_test]
X3_max_dev = max(abs(r - R_protected_B) for r in R_B_scaled)
X3_pass = X3_max_dev < 1e-12
print(f"  X3: Vol(SU(3)) cancels exactly in Route B?")
print(f"      Test factors: {vol_test}")
print(f"      R^B scaled: {[f'{r:.12f}' for r in R_B_scaled]}")
print(f"      Max deviation: {X3_max_dev:.2e}")
print(f"      X3: {'PASS' if X3_pass else 'FAIL'}")
print()

# X4: (4pi)^{-4} cancellation in Route B
# Same check with the (4pi)^{-d/2} prefactor multiplied out.
def gilkey_no_prefactor(tau):
    R = R_scalar(tau)
    Ric2 = Ric2_exact(tau)
    K = K_exact(tau)
    a0 = 16.0 * Vol_SU3_Haar  # (local)
    a2 = (20.0 / 3.0) * R * Vol_SU3_Haar
    a4 = (1.0 / 360.0) * (500.0 * R ** 2 - 32.0 * Ric2 - 28.0 * K) * Vol_SU3_Haar
    return a0 * a4 / a2 ** 2

R_B_nop = gilkey_no_prefactor(tau_fold)
X4_pass = abs(R_B_nop - R_protected_B) < 1e-12
print(f"  X4: (4pi)^{{-4}} cancels in Route B?")
print(f"      With prefactor:    {R_protected_B:.12f}")
print(f"      Without prefactor: {R_B_nop:.12f}")
print(f"      X4: {'PASS' if X4_pass else 'FAIL'}")
print()

# X5: Route C power-law fit residual check
residual_ok = np.max(np.abs(residuals_pl)) < 1e-4
print(f"  X5: Route C power-law fit residuals < 1e-4?")
print(f"      Max |residual|: {np.max(np.abs(residuals_pl)):.2e}")
print(f"      X5: {'PASS' if residual_ok else 'FAIL'}")
print()


# =============================================================================
# 8. OUTPUT DATA AND PLOT
# =============================================================================
print("=" * 80)
print("8. OUTPUT: DATA AND PLOT")
print("=" * 80)

output_data = {
    # Route values
    'R_protected_A': R_protected_A,
    'R_protected_B': R_protected_B,
    'R_protected_C': R_protected_C,
    'max_deviation': max_dev,
    'verdict': verdict,
    'reason': verdict_msg,
    # Route A details
    'a0_A': a0_A,
    'a2_A': a2_A,
    'a4_A': a4_A,
    'R_protected_A_L3': R_protected_A_L3,
    'L_max_drift_A_3_to_7': 100 * (R_protected_A - R_protected_A_L3) / R_protected_A_L3,
    # Route B details
    'a0_B': a0_B,
    'a2_B': a2_B,
    'a4_B': a4_B,
    'R_scalar_fold': R_fold,
    'Ric2_fold': Ric2_fold,
    'K_fold': K_fold,
    # Route C details
    'R_inf_pl': R_inf_pl,
    'A_pl': A_pl,
    'alpha_pl': alpha_pl,
    'residuals_pl': residuals_pl,
    'R_inf_inv_L': R_inf_inv,
    'R_aitken': R_aitken,
    # Route A L_max sweep
    'L_max_sweep': L_range_C,
    'R_A_sweep': R_range_C,
    # Pairwise deviations
    'dev_AB': pair_devs[('A', 'B')],
    'dev_AC': pair_devs[('A', 'C')],
    'dev_BC': pair_devs[('B', 'C')],
    # Cross-check verdicts
    'X1_drift_consistent': X1_pass,
    'X2_Gilkey_tau0_exact': X2_pass,
    'X3_Vol_cancels_in_B': X3_pass,
    'X4_prefactor_cancels_in_B': X4_pass,
    'X5_fit_residuals_ok': residual_ok,
    # Convention & provenance
    'convention': 'S73B_canonical',
    'tau_fold': tau_fold,
    'Vol_SU3_Haar': Vol_SU3_Haar,
    'R_protected_canonical_L3': R_PROTECTED_CANONICAL,
}

npz_path = "s74_r_protected_triple.npz"
np.savez(npz_path, **output_data)
print(f"  Data saved: {npz_path}")

# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(14, 9))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.30)

# Panel 1: Route A L_max convergence + Route C extrapolation
ax1 = fig.add_subplot(gs[0, 0])
L_dense = np.linspace(3, 30, 300)
ax1.plot(L_range_C, R_range_C, 'o-', color='tab:blue', markersize=8,
         label='Route A (S73B partial sum)', linewidth=2)
ax1.plot(L_dense, power_law_model(L_dense, *popt_pl), '--', color='tab:orange',
         label=f'Power-law fit (L_inf={R_inf_pl:.4f})', linewidth=1.8)
ax1.axhline(R_inf_pl, color='tab:orange', linestyle=':', linewidth=1.5,
            label=f'Route C = {R_inf_pl:.4f}')
ax1.axhline(R_protected_B, color='tab:red', linestyle='-.', linewidth=1.8,
            label=f'Route B (Gilkey) = {R_protected_B:.4f}')
ax1.axhline(R_PROTECTED_CANONICAL, color='tab:green', linestyle=':', linewidth=1.2,
            label=f'W1-M canonical (L=3) = {R_PROTECTED_CANONICAL:.4f}')
ax1.set_xlabel('L_max')
ax1.set_ylabel('R_protected')
ax1.set_title('Route A Convergence + Route C Extrapolation')
ax1.legend(fontsize=8, loc='upper left')
ax1.grid(alpha=0.3)
ax1.set_xlim(2.5, 30)

# Panel 2: Three-route bar chart with deviations
ax2 = fig.add_subplot(gs[0, 1])
route_names = ['Route A\n(partial sum,\nL=7)',
               'Route B\n(Gilkey,\nexact)',
               'Route C\n(zeta extrap,\nL=inf)']
route_vals = [routes['A'], routes['B'], routes['C']]
colors = ['tab:blue', 'tab:red', 'tab:orange']
bars = ax2.bar(route_names, route_vals, color=colors, edgecolor='black')
for bar, val in zip(bars, route_vals):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
             f'{val:.4f}', ha='center', va='bottom', fontsize=10)
ax2.set_ylabel('R_protected')
ax2.set_title(f'Three-Route Values (max dev = {max_dev*100:.2f}%)')
ax2.axhline(R_PROTECTED_CANONICAL, color='tab:green', linestyle=':', linewidth=1,
            label=f'W1-M canonical {R_PROTECTED_CANONICAL:.4f}')
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3, axis='y')

# Panel 3: Pairwise deviation table
ax3 = fig.add_subplot(gs[1, 0])
ax3.axis('off')
table_data = [
    ['Pair', 'Difference', 'Rel. dev.'],
    ['A - B', f'{routes["A"] - routes["B"]:.4f}', f'{pair_devs[("A","B")]*100:.2f}%'],
    ['A - C', f'{routes["A"] - routes["C"]:.4f}', f'{pair_devs[("A","C")]*100:.2f}%'],
    ['B - C', f'{routes["B"] - routes["C"]:.4f}', f'{pair_devs[("B","C")]*100:.2f}%'],
    ['', '', ''],
    ['MAX', '', f'{max_dev*100:.2f}%'],
    ['GATE', '', verdict],
]
table = ax3.table(cellText=table_data, loc='center', cellLoc='center',
                  colWidths=[0.3, 0.35, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.8)
# Style header and verdict row
for col in range(3):
    table[0, col].set_facecolor('#d0d0d0')
    table[0, col].set_text_props(weight='bold')
verdict_color = {'PASS': '#b3f5b3', 'INFO': '#f5f5b3', 'FAIL': '#f5b3b3'}.get(verdict, '#ffffff')
for col in range(3):
    table[6, col].set_facecolor(verdict_color)
    table[6, col].set_text_props(weight='bold')
ax3.set_title('Pairwise Deviations', pad=10)

# Panel 4: Structural schematic
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
txt = (
    "STRUCTURAL INTERPRETATION\n"
    "=" * 42 + "\n\n"
    f"R^A = {routes['A']:.4f} (S73B partial sum L_max=7)\n"
    f"R^B = {routes['B']:.4f} (Gilkey curvature exact)\n"
    f"R^C = {routes['C']:.4f} (zeta extrap L_max=inf)\n\n"
    "Routes A and C use truncated spectral zeta\n"
    "sums; Route C extrapolates Route A to L=inf.\n"
    "Route B uses exact Gilkey heat-kernel SD\n"
    "coefficients from the local curvature.\n\n"
    f"Ratio R^A / R^B = {routes['A'] / routes['B']:.4f}\n"
    f"Ratio R^C / R^B = {routes['C'] / routes['B']:.4f}\n\n"
    f"Jensen metric at tau = {tau_fold}:\n"
    f"  R = {R_fold:.4f}\n"
    f"  |Ric|^2 = {Ric2_fold:.4f}\n"
    f"  K       = {K_fold:.4f}\n\n"
    f"Route B closed form:\n"
    f"  (1/1000)*(500 - 32|Ric|^2/R^2 - 28 K/R^2)\n"
    f"  = {R_protected_B:.6f}"
)
ax4.text(0.05, 0.95, txt, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='#f7f7f7', edgecolor='black'))

fig.suptitle(f'R-PROTECTED-TRIPLE-74 (W2-O): Triple-Route R_protected Test  |  Gate: {verdict}',
             fontsize=12, fontweight='bold')

plot_path = "s74_r_protected_triple.png"
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"  Plot saved: {plot_path}")
print()


# =============================================================================
# 9. GATE VERDICT SUMMARY
# =============================================================================
print("=" * 80)
print("9. GATE VERDICT SUMMARY")
print("=" * 80)
print()
print(f"  R-PROTECTED-TRIPLE-74: {verdict}")
print(f"    Threshold: PASS < 3%, INFO in [3%, 10%], FAIL > 10%")
print(f"    Computed:  max pairwise deviation = {max_dev*100:.4f}%")
print()
print(f"    Route A (spectral partial sum, S73B, L_max=7): {routes['A']:.6f}")
print(f"    Route B (Gilkey curvature invariant, exact):   {routes['B']:.6f}")
print(f"    Route C (zeta extrapolation L_max -> infty):   {routes['C']:.6f}")
print()
print(f"    Verdict: {verdict_msg}")
print()
print(f"  Runtime: {time.time() - t_start:.2f} s")
print("=" * 80)
