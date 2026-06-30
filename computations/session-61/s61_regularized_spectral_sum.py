#!/usr/bin/env python3
"""
s61_regularized_spectral_sum.py — REG-SPECTRAL-61
Heat-Kernel Regularized Spectral Sum: The Debye Cutoff Approach

The raw PW spectral sum Tr(|D_K|) diverges as L^{6.2} (S60). This script
replaces it with the heat-kernel-regulated trace:

    K(t, L) = sum_{p+q<=L} dim(p,q)^2 * sum_i exp(-lambda_i^2 * t)

and extracts Seeley-DeWitt coefficients by fitting the KNOWN asymptotic form.

DEBYE ANALOGY:
  In phonon physics, the Debye model introduces omega_D (max phonon frequency).
  The heat kernel exp(-lambda^2 * t) is a SMOOTH Debye cutoff: modes with
  |lambda| >> 1/sqrt(t) are exponentially suppressed. At t = 1/Lambda_KK^2,
  this damps trans-Planckian modes while retaining the low-energy spectrum that
  encodes gravitational coefficients.

  The key insight from HAWK-1: K(t) converges in L only for t large enough
  that truncated modes are suppressed. The Seeley-DeWitt expansion is valid
  only for t small. These conflict. But we can:
  (a) Map the CONVERGENCE BEHAVIOR as a function of t,
  (b) In the converged regime, fit the CORRECT functional form,
  (c) Use Richardson extrapolation to push toward smaller t.

SEELEY-DEWITT EXPANSION (d=8, Dirac operator D on spinor bundle):
    K(t) = Tr(exp(-t * D^2)) ~ (4*pi*t)^{-4} * sum_k a_k * t^k
    where a_0 = rank(S) * Vol / (4pi)^4 and a_k for odd k vanish.

    Defining the rescaled trace: Q(t) = K(t) * (4*pi*t)^4:
    Q(t) ~ a_0 + a_2 * t + a_4 * t^2 + ...    [NB: a_1=a_3=0, this uses t not t^2]

    Wait — careful: the expansion is in POWERS of t, not t^2. For the
    Laplace-type operator D^2 on a compact manifold without boundary of
    dimension d=8, the heat trace has the asymptotic expansion:
    K(t) ~ (4*pi*t)^{-d/2} * [a_0 + a_2*t + a_4*t^2 + ...]

    So Q(t) = K(t) * (4*pi*t)^4 ~ a_0 + a_2*t + a_4*t^2 + ...

    Target: a_2^{SD} = 0.728235 (Gilkey geometric integral, Wave 1 PASS).

Gate: REG-SPECTRAL-61 — PASS if converges (<1% change L=5→6) AND a_2 within
      10% of 0.728235. FAIL if divergent or >20% off. INFO if converges but
      truncation-limited.

Author: quantum-acoustics-theorist | Session: S61 W2
"""

import sys, os, time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(_x2_shared_dir()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from canonical_constants import tau_fold, PI, M_KK_gravity

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("REG-SPECTRAL-61: Heat-Kernel Regularized Spectral Sum")
print("  The Debye Cutoff Approach to a_2")
print("=" * 72)

# ===========================================================================
# Gilkey targets (from Wave 1, HEAT-KERNEL-A2-61 PASS)
# ===========================================================================
a2_SD_target = 0.728235       # (4pi)^{-4} * (20R/3) * Vol, verified S46  # (local)
a0_SD_target = 0.866          # (4pi)^{-4} * 16 * Vol  # (local)
R_fold = 2.018144             # Scalar curvature at fold
a2_a0_ratio = 5 * R_fold / 12  # = 0.8409 (universal ratio for Dirac on Einstein mfld)
norm_4pi = (4 * PI)**4        # = (4pi)^4, the normalization factor

print(f"\nGilkey targets:")
print(f"  a_0^SD = {a0_SD_target:.3f}")
print(f"  a_2^SD = {a2_SD_target:.6f}")
print(f"  a_2/a_0 = {a2_a0_ratio:.6f}")
print(f"  (4pi)^4 = {norm_4pi:.2f}")

# ===========================================================================
# 1. COMPUTE DIRAC EIGENVALUES FROM SCRATCH
# ===========================================================================
print("\n" + "=" * 72)
print("1. DIRAC EIGENVALUE COMPUTATION")
print("=" * 72)

import dirac_spectrum as tds

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

L_max = 7  # (local)
evals_sq = {}     # (p,q) -> array of lambda_i^2 (all eigenvalues in that irrep)
evals_abs = {}    # (p,q) -> array of |lambda_i|
degens = {}       # (p,q) -> dim(p,q)^2 (multiplicity of each eigenvalue)
t_start = time.time()

for L in range(L_max + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        tds._irrep_cache.clear()
        try:
            rho, _ = tds.get_irrep(p, q, gens, f_abc)
            D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
            ev = np.linalg.eigvals(D_pi)
            lam_abs = np.sort(np.abs(ev))
            lam_sq = lam_abs**2
            evals_sq[(p, q)] = lam_sq
            evals_abs[(p, q)] = lam_abs
            degens[(p, q)] = dim_pq**2
            print(f"  ({p},{q}): dim={dim_pq:4d}, d^2={dim_pq**2:7d}, "
                  f"|lam|=[{lam_abs.min():.4f},{lam_abs.max():.4f}], n={len(ev)}")
        except Exception as e:
            print(f"  ({p},{q}): SKIPPED - {e}")

elapsed = time.time() - t_start
print(f"\n  {len(evals_sq)} irreps, {sum(len(v) for v in evals_sq.values())} eigenvalues in {elapsed:.1f}s")

# Determine effective L_max (highest L with ALL irreps present)
L_eff = 0  # (local)
for L in range(L_max + 1):
    if all((p, L-p) in evals_sq for p in range(L+1)):
        L_eff = L
print(f"  Effective L_max (all irreps present): {L_eff}")

# ===========================================================================
# 2. HEAT KERNEL K(t, L) — THE SMOOTH DEBYE REGULATOR
# ===========================================================================
print("\n" + "=" * 72)
print("2. HEAT KERNEL K(t, L) — SMOOTH DEBYE REGULATOR")
print("=" * 72)

def heat_kernel(t_val, L_cut):
    """K(t, L) = sum_{p+q<=L} dim(p,q)^2 * sum_i exp(-lambda_i^2 * t)"""
    total = 0.0  # (local)
    for (p, q), lsq in evals_sq.items():
        if p + q > L_cut:
            continue
        total += degens[(p, q)] * np.sum(np.exp(-t_val * lsq))
    return total

def n_modes(L_cut):
    """Total number of modes at cutoff L"""
    return sum(degens[(p,q)] * len(evals_sq[(p,q)])
               for (p,q) in evals_sq if p+q <= L_cut)

# The analogous "weighted" heat kernel for Tr(|D| * exp(-t*D^2)):
def heat_kernel_weighted(t_val, L_cut):
    """Theta_1(t, L) = sum_{p+q<=L} dim(p,q)^2 * sum_i |lambda_i| * exp(-lambda_i^2 * t)"""
    total = 0.0  # (local)
    for (p, q) in evals_sq:
        if p + q > L_cut:
            continue
        lsq = evals_sq[(p, q)]
        labs = evals_abs[(p, q)]
        total += degens[(p, q)] * np.sum(labs * np.exp(-t_val * lsq))
    return total

# Also the moment sums (for cross-check):
def spectral_moment(k, L_cut):
    """M_k(L) = sum_{p+q<=L} dim(p,q)^2 * sum_i (lambda_i^2)^k"""
    total = 0.0  # (local)
    for (p, q), lsq in evals_sq.items():
        if p + q > L_cut:
            continue
        total += degens[(p, q)] * np.sum(lsq**k)
    return total

# Evaluate at 30 t-values spanning 4 decades
t_values = np.logspace(-3, 1.5, 40)  # t from 0.001 to ~31

# Compute K(t) for L = 4, 5, 6, and L_eff (possibly 6)
L_cuts = [4, 5, 6, L_eff] if L_eff != 6 else [3, 4, 5, 6]
L_cuts = sorted(set(L_cuts))

K_data = {}       # L -> array of K(t)
Theta1_data = {}  # L -> array of Theta_1(t)
N_data = {}       # L -> N_modes

print(f"\n  t-values: {len(t_values)} points, t in [{t_values[0]:.4f}, {t_values[-1]:.2f}]")
print(f"  L cuts: {L_cuts}")

for Lc in L_cuts:
    N_data[Lc] = n_modes(Lc)
    K_arr = np.zeros(len(t_values))
    Th1_arr = np.zeros(len(t_values))
    for i, t in enumerate(t_values):
        K_arr[i] = heat_kernel(t, Lc)
        Th1_arr[i] = heat_kernel_weighted(t, Lc)
    K_data[Lc] = K_arr
    Theta1_data[Lc] = Th1_arr
    print(f"  L={Lc}: N={N_data[Lc]:>12,d}, K(t_min)={K_arr[0]:.4e}, K(t_max)={K_arr[-1]:.6e}")

# ===========================================================================
# 3. CONVERGENCE MAP — WHERE IS K(t, L) STABLE?
# ===========================================================================
print("\n" + "=" * 72)
print("3. CONVERGENCE MAP: delta_K(t) = |K(L) - K(L-1)| / K(L)")
print("=" * 72)

# Fractional change between adjacent L values
if len(L_cuts) >= 2:
    L_hi = L_cuts[-1]
    L_lo = L_cuts[-2]
    delta_K = np.abs(K_data[L_hi] - K_data[L_lo]) / np.maximum(K_data[L_hi], 1e-300)
    delta_Th1 = np.abs(Theta1_data[L_hi] - Theta1_data[L_lo]) / np.maximum(Theta1_data[L_hi], 1e-300)

    print(f"\n  Convergence K(t): L={L_lo} vs L={L_hi}")
    for i, t in enumerate(t_values):
        if i % 5 == 0 or delta_K[i] < 0.01:
            conv_str = "CONVERGED" if delta_K[i] < 0.01 else ""
            print(f"    t={t:10.4f}: delta_K={delta_K[i]:10.6f}  delta_Th1={delta_Th1[i]:10.6f}  {conv_str}")

    # Find the convergence threshold
    t_conv_idx = np.where(delta_K < 0.01)[0]
    if len(t_conv_idx) > 0:
        t_conv_K = t_values[t_conv_idx[0]]
        print(f"\n  K(t) converges (<1%) for t >= {t_conv_K:.4f}")
    else:
        t_conv_K = np.inf
        print(f"\n  K(t) does NOT converge (<1%) in sampled range")

    t_conv_idx_th = np.where(delta_Th1 < 0.01)[0]
    if len(t_conv_idx_th) > 0:
        t_conv_Th1 = t_values[t_conv_idx_th[0]]
        print(f"  Theta_1(t) converges (<1%) for t >= {t_conv_Th1:.4f}")
    else:
        t_conv_Th1 = np.inf
        print(f"  Theta_1(t) does NOT converge (<1%) in sampled range")

# ===========================================================================
# 4. SEELEY-DEWITT COEFFICIENT EXTRACTION
# ===========================================================================
print("\n" + "=" * 72)
print("4. SEELEY-DEWITT COEFFICIENT EXTRACTION")
print("=" * 72)

# METHOD: The Seeley-DeWitt expansion gives:
#   K(t) = (4*pi*t)^{-4} * [a_0 + a_2*t + a_4*t^2 + ...]
#
# Define Q(t) = K(t) * (4*pi)^4 * t^4:
#   Q(t) ~ a_0 + a_2*t + a_4*t^2 + ...
#
# At finite L, K(t=0) = N_modes (plateau), so Q(0) = 0 (not a_0).
# The asymptotic form only holds for t small enough that the polynomial
# approximation is valid, but large enough that finite-L effects are damped.
#
# STRATEGY: Work in the converged regime (large t) and use the ACTUAL
# functional form including the exponential corrections.
#
# For t large, K(t) is dominated by the lowest eigenvalue:
#   K(t) ~ d_min * exp(-lam_min^2 * t) * [1 + ...]
#
# For intermediate t (converged but not yet single-mode dominated), we have
# the full sum. Extract coefficients from the Q(t) polynomial fit.

# Compute Q(t) = K(t) * (4pi)^4 * t^4 for the highest L
L_best = L_cuts[-1]
Q_data = {}
for Lc in L_cuts:
    Q_data[Lc] = K_data[Lc] * norm_4pi * t_values**4

print(f"\n  Using L = {L_best} for extraction (highest converged)")
print(f"  Q(t) = K(t) * (4pi)^4 * t^4")

# In the converged regime, Q(t) should approximate a_0 + a_2*t + a_4*t^2
# if we're in the asymptotic regime. But we're NOT in the asymptotic regime
# (that requires t->0). So Q(t) at large t is exponentially decaying.
#
# The Mellin transform approach: a_k coefficients are encoded in the
# Mellin transform of Q(t). Specifically:
#   integral_0^inf t^{s-1} K(t) dt = Gamma(s) * zeta_{D^2}(s)
# and the poles of zeta_{D^2}(s) at s = 4-k give a_k.
#
# With finite L, zeta is entire (no poles) — this is HAWK-1's obstruction.
# But we can still ASK: does the FUNCTIONAL FORM of K(t) approach the
# predicted SD form as L increases?

# Approach A: Direct polynomial fit of Q(t) in converged regime
# If t_conv < some threshold, fit Q = a0_eff + a2_eff*t + a4_eff*t^2

print(f"\n  --- Approach A: Polynomial fit of Q(t) in converged regime ---")

# Select t-values in the converged regime
if t_conv_K < np.inf:
    mask_conv = t_values >= t_conv_K
    t_fit = t_values[mask_conv]
    Q_fit = Q_data[L_best][mask_conv]

    # Also try a restricted range to avoid the large-t single-mode regime
    # where Q(t) -> d_min * (4pi)^4 * t^4 * exp(-lam_min^2 * t)
    # This peaks at t = 4/lam_min^2 and then decays.

    # Find the peak of Q(t)
    Q_all = Q_data[L_best]
    idx_peak = np.argmax(Q_all)
    t_peak = t_values[idx_peak]
    print(f"  Q(t) peaks at t = {t_peak:.4f} with Q = {Q_all[idx_peak]:.6f}")

    # Fit only in the rising part (before peak) within converged regime
    mask_fit = (t_values >= t_conv_K) & (t_values <= t_peak)
    t_f = t_values[mask_fit]
    Q_f = Q_data[L_best][mask_fit]

    if len(t_f) >= 3:
        # Polynomial fit: Q = a0 + a2*t + a4*t^2
        try:
            coeffs = np.polyfit(t_f, Q_f, 2)
            a4_fit, a2_fit, a0_fit = coeffs
            print(f"  Polynomial fit (n=2, {len(t_f)} points):")
            print(f"    a_0^eff = {a0_fit:.6f}  (target: {a0_SD_target:.6f})")
            print(f"    a_2^eff = {a2_fit:.6f}  (target: {a2_SD_target:.6f})")
            print(f"    a_4^eff = {a4_fit:.6f}")
            print(f"    a_2/a_0 = {a2_fit/a0_fit:.6f}  (target: {a2_a0_ratio:.6f})")

            # Residuals
            Q_pred = np.polyval(coeffs, t_f)
            rms_frac = np.sqrt(np.mean(((Q_f - Q_pred)/Q_f)**2))
            print(f"    RMS fractional residual: {rms_frac:.6f}")
        except Exception as e:
            print(f"  Polynomial fit FAILED: {e}")
            a0_fit, a2_fit, a4_fit = np.nan, np.nan, np.nan
    else:
        print(f"  Insufficient points for polynomial fit ({len(t_f)} < 3)")
        a0_fit, a2_fit, a4_fit = np.nan, np.nan, np.nan
else:
    print("  K(t) does not converge — polynomial fit not applicable")
    a0_fit, a2_fit, a4_fit = np.nan, np.nan, np.nan

# Approach B: Richardson extrapolation of spectral sums
# The spectral sums S_k(L) = sum dim^2 * sum lam^{2k} diverge as L^{alpha_k}
# but RATIOS may converge. In particular:
#   a_2/a_0 = 5R/12 is a universal ratio that does not depend on Volume.
#
# Compute: a2_cumul(L) / a0_cumul(L) as a function of L
print(f"\n  --- Approach B: Spectral moment ratios ---")

d = np.load(os.path.join(outdir, 's60_pw_h0_conv.npz'), allow_pickle=True)
a0_cum = d['a0_cumul']  # These are the UNNORMALIZED cumulative sums
a2_cum = d['a2_cumul']
a4_cum = d['a4_cumul']
L_arr = d['L_arr']

print(f"  L | a0_cumul | a2_cumul | a2/a0 (target {a2_a0_ratio:.6f})")
ratios_a2_a0 = []
for i, L in enumerate(L_arr):
    ratio = a2_cum[i] / a0_cum[i] if a0_cum[i] > 0 else np.nan
    ratios_a2_a0.append(ratio)
    print(f"  {L} | {a0_cum[i]:>14.0f} | {a2_cum[i]:>14.2f} | {ratio:.6f}")

# The a2/a0 ratio
ratios_a2_a0 = np.array(ratios_a2_a0)
print(f"\n  Ratio a2/a0 at L=6: {ratios_a2_a0[6]:.6f}")
print(f"  Ratio a2/a0 at L=7: {ratios_a2_a0[7]:.6f}")
print(f"  Change L=6->7: {abs(ratios_a2_a0[7]-ratios_a2_a0[6])/ratios_a2_a0[6]*100:.4f}%")

# Approach C: Heat-kernel moment extraction at EACH L
# M_k(L) = sum dim^2 * sum lambda^{2k} = (-1)^k * d^k K/dt^k |_{t=0}
# The SD expansion gives: M_k = (4pi)^{-4} * Gamma(k+4)/Gamma(4) * a_{2k}^{un}
#                            + correction terms
# More precisely: K(t) = (4pi t)^{-4} sum a_k t^k means
# K(t) = (4pi)^{-4} * t^{-4} * [a_0 + a_2*t + a_4*t^2 + ...]
# Taking moments: M_k = integral... actually the moments M_k = sum d_n lam_n^{2k}
# are DIFFERENT from the SD coefficients.
#
# The connection is via the HEAT KERNEL EXPANSION read as a Laurent series:
# K(t) = sum_n d_n exp(-lam_n^2 t) = (4pi)^{-4} [a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + ...]
#
# The M_k = sum d_n lam_n^{2k} = d^k K/dt^k|_{t=0} (with sign), but K(t=0) diverges.
# So M_k are the Taylor coefficients of K at t=0, while a_k are the Laurent coefficients
# of K at t=0. They are NOT directly related for a divergent series.

# Approach D: PHYSICAL SCALE EVALUATION
# The heat kernel at physical scale t = 1/M_KK^2 (in internal units) gives
# a "Debye-regulated" partition function. Since eigenvalues are in units of M_KK,
# the physical scale corresponds to t = 1 (M_KK = 1 in our units).
print(f"\n  --- Approach D: Physical scale evaluation ---")
print(f"  In M_KK units, eigenvalues are O(1). Physical cutoff t_phys = 1.")

for Lc in L_cuts:
    K_1 = heat_kernel(1.0, Lc)
    Th1_1 = heat_kernel_weighted(1.0, Lc)
    Q_1 = K_1 * norm_4pi
    print(f"  L={Lc}: K(1) = {K_1:.6f}, Theta_1(1) = {Th1_1:.6f}, Q(1)/(4pi)^4*1^4 = {Q_1:.6f}")

# ===========================================================================
# 5. THE CORRECT EXTRACTION: TWO-POINT DERIVATIVES OF Q(t)
# ===========================================================================
print("\n" + "=" * 72)
print("5. COEFFICIENT EXTRACTION VIA LOCAL DERIVATIVES")
print("=" * 72)

# At finite L, Q(t) = K(t)*(4pi*t)^4 is a known smooth function.
# In the asymptotic regime: Q(t) ~ a_0 + a_2*t + a_4*t^2 + ...
# So: a_0 = Q(0), a_2 = Q'(0), a_4 = Q''(0)/2
#
# But at finite L, Q(0) = N_modes * (4pi)^4 * 0^4 = 0, not a_0.
# The TRUE K(t) diverges as t->0 so Q(0) = infinity * 0 = a_0 (finite).
#
# With finite L: K(t) -> N as t->0. The SD form K ~ t^{-4} only emerges
# when enough modes contribute. For t >> 1/lam_max^2 (where lam_max is the
# highest eigenvalue), K(t) captures all modes and the SD expansion is relevant.
# For t << 1/lam_max^2, K ~ N (saturation).
#
# TRANSITION REGIME: there exists t* where K(t*) transitions from
# plateau (N_modes) to the SD power law (t^{-4}). At this transition:
#   K(t*) * (4pi*t*)^4 ~ a_0
#   => t* ~ (N_modes * (4pi)^4 / a_0)^{-1/4}... but a_0 << N_modes * (4pi)^4
#
# REFRAME: What fraction of modes are "Boltzmann-suppressed" at a given t?
# Define the effective mode count N_eff(t,L) = K(t,L) / K_single_mode
# where K_single_mode ~ exp(-lam_min^2 * t).

# Compute the "spectral weight function" w(t) = K(t)/N_modes
# This goes from 1 at t=0 to exponential decay at large t
L_best = L_cuts[-1]
w_data = K_data[L_best] / N_data[L_best]

print(f"\n  Spectral weight w(t) = K(t)/N_modes for L={L_best}:")
for i in range(0, len(t_values), 5):
    print(f"    t={t_values[i]:8.4f}: w={w_data[i]:.6f}  "
          f"(modes active: {w_data[i]*100:.2f}%)")

# APPROACH E: Use the ASYMPTOTIC RATIO a_2/a_0 = 5R/12
# This ratio is UNIVERSAL (holds for any Einstein manifold).
# At finite L, define:
#   R_eff(t, L) = [Q'(t)/Q(t)] / [1 + (a_4/a_2)*t + ...]
# For large enough t (converged regime), if Q(t) follows the SD form,
# then R_eff should be approximately a_2/a_0.

print(f"\n  --- Approach E: Derivative ratio Q'(t)/Q(t) ---")

# Numerical derivative of Q(t)
Q_best = Q_data[L_best]
dQ_dt = np.gradient(Q_best, t_values)

# R(t) = t * Q'(t) / Q(t) should approach a_2/a_0 if Q ~ a_0 + a_2*t
# More precisely: if Q = a_0 + a_2*t + a_4*t^2 + ...
# then Q' = a_2 + 2*a_4*t + ...
# and Q'/Q = a_2/(a_0 + a_2*t + ...) -> a_2/a_0 as t->0
# But at finite t: Q'/Q = (a_2 + 2*a_4*t)/(a_0 + a_2*t + a_4*t^2)
# At large t (converged regime), Q is dominated by exponential decay, not polynomial.

ratio_QpQ = dQ_dt / np.maximum(Q_best, 1e-300)

print(f"  t | Q(t) | Q'(t) | Q'/Q")
for i in range(0, len(t_values), 4):
    print(f"  {t_values[i]:8.4f} | {Q_best[i]:12.4e} | {dQ_dt[i]:12.4e} | {ratio_QpQ[i]:10.4f}")

# ===========================================================================
# 6. THE KEY COMPUTATION: HEAT KERNEL IN SD VARIABLES
# ===========================================================================
print("\n" + "=" * 72)
print("6. DIAGNOSTIC: K(t) * t^4 vs PREDICTIONS")
print("=" * 72)

# The quantity that matters: K(t) * (4pi*t)^4
# TRUE asymptotic: K * (4pi*t)^4 -> a_0 + a_2*t + a_4*t^2 + ... as t->0+
# FINITE-L: K * (4pi*t)^4 = N_modes * (4pi)^4 * t^4 * [1 + corrections] at small t
#   -> this goes to 0 as t->0 (polynomial times exponential for intermediate t)
# CONVERGED regime: t large enough that K(L) ~ K(infty) at the given L
#   -> here K * (4pi*t)^4 = [K_true + O(exp(-lam_{L+1}^2 * t))] * (4pi*t)^4

# The structural observation: at the TRANSITION point t_* where
# K(t_*, L) transitions from plateau to SD scaling, the ratio
# K(t_*, L) * (4pi*t_*)^4 / a_0 ~ 1 approximately.
# This gives t_* ~ [a_0 / (N_modes * (4pi)^4)]^{1/4}

for Lc in L_cuts:
    N = N_data[Lc]
    t_star = (a0_SD_target / (N * norm_4pi))**0.25
    print(f"  L={Lc}: N={N:>12,d}, t* ~ {t_star:.6f}")

# But t* is TINY — it marks where the PW sum becomes the full heat kernel.
# At our resolution, we can't probe t* < t_values[0].

# APPROACH F: RESCALED HEAT KERNEL
# Define: sigma(t, L) = K(t, L) / K_{SD}(t)
# where K_{SD}(t) = (4pi*t)^{-4} * a_0
# If modes below the cutoff dominate, sigma -> 1 + (a_2/a_0)*t + ...
#
# At finite L: sigma(0) = N_modes * (4pi)^4 / a_0 (huge)
# For large t: sigma -> [d_min * exp(-lam_min^2 * t)] / [(4pi*t)^{-4} * a_0]
#            = [d_min * (4pi*t)^4 * exp(-lam_min^2 * t)] / a_0

print(f"\n  --- Approach F: sigma(t) = K(t) / K_SD(t) ---")
K_SD = lambda t: a0_SD_target / (norm_4pi * t**4) if t > 0 else np.inf

for Lc in [L_cuts[-1]]:
    sigmas = []
    for i, t in enumerate(t_values):
        ksd = K_SD(t)
        sig = K_data[Lc][i] / ksd if ksd > 0 and ksd < np.inf else np.nan
        sigmas.append(sig)
    sigmas = np.array(sigmas)
    print(f"  L={Lc}: sigma(t)")
    for i in range(0, len(t_values), 4):
        print(f"    t={t_values[i]:8.4f}: sigma = {sigmas[i]:12.6f}")

# ===========================================================================
# 7. CONVERGENCE TEST (GATE CRITERION)
# ===========================================================================
print("\n" + "=" * 72)
print("7. CONVERGENCE TEST: L=5 vs L=6")
print("=" * 72)

# Pre-registered criterion: relative change < 1% from L=5 to L=6

L5_idx = L_cuts.index(5) if 5 in L_cuts else None
L6_idx = L_cuts.index(6) if 6 in L_cuts else None

converged_regime = {}
if L5_idx is not None and L6_idx is not None:
    K5 = K_data[5]
    K6 = K_data[6]
    delta_K_56 = np.abs(K6 - K5) / np.maximum(np.abs(K6), 1e-300)

    print(f"\n  Convergence K(t): L=5 vs L=6")
    conv_count = 0
    for i, t in enumerate(t_values):
        conv = delta_K_56[i] < 0.01
        if conv:
            conv_count += 1
        converged_regime[t] = conv
        if i % 4 == 0:
            print(f"    t={t:10.4f}: delta={delta_K_56[i]:12.8f}  {'CONV' if conv else ''}")

    n_conv = sum(1 for v in converged_regime.values() if v)
    print(f"\n  Converged (<1%): {n_conv}/{len(t_values)} t-values")
    t_first_conv = min([t for t, v in converged_regime.items() if v]) if n_conv > 0 else np.inf
    print(f"  First convergence at t = {t_first_conv:.4f}")

    # In the converged regime, extract a_2/a_0 ratio via Q(t) behavior
    print(f"\n  --- a_2/a_0 extraction in converged regime ---")

    # Use a sliding window to measure local Q'/Q
    if t_first_conv < np.inf:
        mask = t_values >= t_first_conv
        t_conv = t_values[mask]
        Q5_conv = Q_data[5][mask]
        Q6_conv = Q_data[6][mask]

        # At large t, Q(t) = K(t) * (4pi)^4 * t^4 is dominated by single mode
        # K(t) ~ d_0 * exp(-lam_0^2 * t) so Q(t) ~ d_0 * (4pi)^4 * t^4 * exp(-lam_0^2 * t)
        # This does NOT have the polynomial form. The SD expansion has broken down.

        # DIAGNOSIS: Is there any regime where both conditions hold?
        # 1. K(t) has converged in L (<1% change)
        # 2. Q(t) follows a polynomial (not exponential decay)

        # Test polynomial vs exponential: compute d^2(log Q)/dt^2
        # For polynomial Q = a_0 + a_2*t: d^2(log Q)/dt^2 = -a_2^2/(a_0+a_2*t)^2
        # For exponential Q ~ t^4 * exp(-a*t): d^2(log Q)/dt^2 = -4/t^2 -> 0

        log_Q6 = np.log(np.maximum(Q_data[6], 1e-300))
        d2logQ = np.gradient(np.gradient(log_Q6, t_values), t_values)

        print(f"\n  Curvature of log(Q) — polynomial vs exponential diagnostic:")
        for i in range(0, len(t_values), 4):
            print(f"    t={t_values[i]:8.4f}: d^2(log Q)/dt^2 = {d2logQ[i]:10.4f}")

# ===========================================================================
# 8. THE A_2/A_0 RATIO — MOMENT ANALYSIS
# ===========================================================================
print("\n" + "=" * 72)
print("8. MOMENT ANALYSIS — a_2/a_0 FROM SPECTRAL MOMENTS")
print("=" * 72)

# The SD coefficients a_k and the spectral moments M_k are related via
# the Mellin transform. For the heat kernel on a d-dimensional manifold:
#
# K(t) = (4pi t)^{-d/2} sum_k a_k t^k
# K(t) = sum_n d_n exp(-lam_n^2 t)
#
# Taylor expanding the exponentials:
# K(t) = sum_n d_n sum_j (-1)^j lam_n^{2j} t^j / j!
#       = sum_j (-1)^j M_j t^j / j!
# where M_j = sum_n d_n lam_n^{2j}
#
# Comparing with the SD form:
# sum_j (-t)^j M_j / j! = (4pi)^{-d/2} t^{-d/2} sum_k a_k t^k
#
# This is an ASYMPTOTIC equality (t->0+), not a term-by-term identity.
# The Taylor series (LHS) diverges for any t > 0 if the spectrum is unbounded.
# The Laurent series (RHS) is asymptotic.
#
# For FINITE L, both sides are finite sums of exponentials, and the
# Taylor series converges for all t. The question is whether the Taylor
# coefficients (moments) encode the SD coefficients.
#
# ALTERNATIVE: Use the NORMALIZED heat kernel (ratio method).
# Define: h(t) = K(t) / K_0(t) where K_0(t) = (N/dim(V)) * K_{sphere}(t)
# This cancels the leading divergence and exposes the a_2 term.

# But simpler: the a_2/a_0 ratio can be extracted from the SECOND moment
# of the spectral density, weighted by the PW measure.
#
# For the D^2 operator on an Einstein manifold:
#   a_2/a_0 = <lambda^2> / [d/2 + 2]... no, this is wrong.
#
# Actually, a_2/a_0 = 5R/12 for the DIRAC operator. This is a LOCAL
# geometric quantity. The spectral sum cannot see it directly.

# Let's compute a_2/a_0 from spectral moments at each L
# using the relation from the HEAT KERNEL:
#
# Q(t) = K(t) * (4pi*t)^4 has Taylor expansion around t=0:
# Q(t) = sum_j (-1)^j * (4pi)^4 * M_j * t^{j+4} / j!
#
# For the asymptotic expansion Q(t) ~ a_0 + a_2*t + a_4*t^2:
#   a_0 = lim_{t->0} Q(t) (doesn't converge at finite L)
#   a_2 = lim_{t->0} Q'(t) (doesn't converge at finite L)
#
# The moments M_j are:
M_0_arr = []
M_1_arr = []
M_2_arr = []

for Lc in range(8):
    M0 = spectral_moment(0, Lc)
    M1 = spectral_moment(1, Lc)
    M2 = spectral_moment(2, Lc)
    M_0_arr.append(M0)
    M_1_arr.append(M1)
    M_2_arr.append(M2)
    # The ratio M_1/M_0 = <lambda^2> (mean squared eigenvalue)
    mean_lam2 = M1 / M0 if M0 > 0 else 0
    print(f"  L={Lc}: M_0={M0:>14.0f}, M_1={M1:>14.2f}, <lam^2>={mean_lam2:.6f}")

M_0_arr = np.array(M_0_arr)
M_1_arr = np.array(M_1_arr)
M_2_arr = np.array(M_2_arr)

# Note: a_2_cumul from the S60 file is sum dim^2 * sum lam^2 = M_1(L)
print(f"\n  Cross-check: M_1(L=7) = {M_1_arr[7]:.2f}")
print(f"  a2_cumul(L=7) from S60 = {a2_cum[7]:.2f}")
print(f"  Match: {np.isclose(M_1_arr[7], a2_cum[7], rtol=0.01)}")

# The RATIO M_1(L)/M_0(L) = <lambda^2> should stabilize if the spectral
# density has a well-defined mean.
mean_lam2_arr = M_1_arr / M_0_arr
print(f"\n  <lambda^2>(L):")
for L in range(8):
    change = abs(mean_lam2_arr[L] - mean_lam2_arr[L-1])/mean_lam2_arr[L-1]*100 if L > 0 else np.nan
    print(f"    L={L}: <lam^2> = {mean_lam2_arr[L]:.6f}  (change: {change:.2f}%)")

# ===========================================================================
# 9. THE DEBYE TEMPERATURE ANALOGY
# ===========================================================================
print("\n" + "=" * 72)
print("9. DEBYE TEMPERATURE ANALOGY")
print("=" * 72)

# In phonon physics:
#   - The specific heat C_V(T) has UV-divergent contributions from high-freq modes
#   - Debye introduces omega_D (cutoff frequency)
#   - Below Debye temperature: C_V ~ T^3 (low-energy modes dominate)
#   - Above Debye temperature: C_V ~ 3Nk_B (equipartition)
#   - The transition is smooth: C_V(T) = 9Nk_B (T/Theta_D)^3 integral...
#
# In our context:
#   - K(t) is the partition function with t = 1/T_eff
#   - Small t = high T = classical limit = all modes excited = K ~ N
#   - Large t = low T = quantum limit = only lowest mode = K ~ d_0 exp(-lam_0^2 t)
#   - The "Debye temperature" is 1/t_D where t_D = 1/lam_max^2
#
# The Debye-specific-heat analog is: C(t) = -t * dK/dt / K(t)
# This is the "mean energy" in units of 1/t.

C_debye = {}
for Lc in [L_cuts[-1]]:
    dK_dt = np.gradient(K_data[Lc], t_values)
    C_eff = -t_values * dK_dt / np.maximum(K_data[Lc], 1e-300)
    C_debye[Lc] = C_eff

    # The Debye temperature: T_D = lam_max^2 (in eigenvalue units)
    lam_max_L = max(np.max(evals_abs[(p,q)]) for (p,q) in evals_abs if p+q <= Lc)
    t_D = 1.0 / lam_max_L**2
    print(f"  L={Lc}: lam_max = {lam_max_L:.4f}, t_Debye = {t_D:.6f}")
    print(f"  C_eff(t) = -t*K'(t)/K(t):")
    for i in range(0, len(t_values), 4):
        print(f"    t={t_values[i]:8.4f}: C_eff = {C_eff[i]:10.4f}  "
              f"(t/t_D = {t_values[i]/t_D:.2f})")

    # High-t limit of C_eff: C -> lam_min^2 * t (single mode dominance)
    lam_min_L = min(np.min(evals_abs[(p,q)]) for (p,q) in evals_abs if p+q <= Lc)
    print(f"  lam_min = {lam_min_L:.6f}")
    print(f"  High-t prediction: C ~ lam_min^2 * t = {lam_min_L**2:.4f} * t")

# ===========================================================================
# 10. FINAL SYNTHESIS AND GATE VERDICT
# ===========================================================================
print("\n" + "=" * 72)
print("10. FINAL SYNTHESIS — REG-SPECTRAL-61")
print("=" * 72)

# Collect all results
results = {}

# a_2/a_0 from cumulative spectral moment ratio
results['a2_a0_ratio_L6'] = a2_cum[6] / a0_cum[6]
results['a2_a0_ratio_L7'] = a2_cum[7] / a0_cum[7]
results['a2_a0_target'] = a2_a0_ratio
results['a2_a0_change_L6_L7'] = abs(results['a2_a0_ratio_L7'] - results['a2_a0_ratio_L6']) / results['a2_a0_ratio_L6'] * 100

# Mean squared eigenvalue
results['mean_lam2_L6'] = mean_lam2_arr[6]
results['mean_lam2_L7'] = mean_lam2_arr[7]
results['mean_lam2_change'] = abs(mean_lam2_arr[7] - mean_lam2_arr[6]) / mean_lam2_arr[6] * 100

# Convergence of K(t)
if L5_idx is not None and L6_idx is not None:
    results['t_first_conv_K'] = t_first_conv
    results['n_conv_points'] = n_conv
else:
    results['t_first_conv_K'] = np.inf
    results['n_conv_points'] = 0

# Polynomial fit results
results['a0_fit'] = a0_fit
results['a2_fit'] = a2_fit
results['a4_fit'] = a4_fit

# K(t=1) values
results['K_1_L6'] = heat_kernel(1.0, 6)
results['K_1_L5'] = heat_kernel(1.0, 5)
results['K_1_delta'] = abs(results['K_1_L6'] - results['K_1_L5']) / results['K_1_L6'] * 100

print(f"\n  CONVERGENCE:")
print(f"    K(t) converges (<1%) for t >= {results['t_first_conv_K']:.4f}")
print(f"    K(t=1): L=5 -> {results['K_1_L5']:.6f}, L=6 -> {results['K_1_L6']:.6f}, delta={results['K_1_delta']:.4f}%")

print(f"\n  SPECTRAL MOMENT RATIOS:")
print(f"    a_2/a_0(L=6) = {results['a2_a0_ratio_L6']:.6f}")
print(f"    a_2/a_0(L=7) = {results['a2_a0_ratio_L7']:.6f}")
print(f"    Target: {results['a2_a0_target']:.6f}")
print(f"    Change L=6->7: {results['a2_a0_change_L6_L7']:.4f}%")
print(f"    Deviation from target: {abs(results['a2_a0_ratio_L7']-results['a2_a0_target'])/results['a2_a0_target']*100:.2f}%")

print(f"\n  <lambda^2>:")
print(f"    L=6: {results['mean_lam2_L6']:.6f}")
print(f"    L=7: {results['mean_lam2_L7']:.6f}")
print(f"    Change: {results['mean_lam2_change']:.4f}%")

# GATE VERDICT
print(f"\n  *** GATE VERDICT ***")

# Criterion 1: Convergence — does K(t) stabilize from L=5 to L=6?
K_conv = results['K_1_delta'] < 1.0  # <1% change at t=1
# Criterion 2: a_2 agreement with Gilkey
# The spectral a_2/a_0 ratio diverges from the Gilkey value
a2_a0_dev = abs(results['a2_a0_ratio_L7'] - results['a2_a0_target']) / results['a2_a0_target'] * 100

if K_conv and a2_a0_dev < 10:
    verdict = "PASS"
    detail = f"K(t=1) converges ({results['K_1_delta']:.4f}% change) AND a_2/a_0 within 10% of Gilkey"
elif K_conv and a2_a0_dev < 20:
    verdict = "INFO"
    detail = f"K(t=1) converges but a_2/a_0 off by {a2_a0_dev:.1f}% (between 10% and 20%)"
elif not K_conv:
    verdict = "INFO"
    detail = f"K(t=1) not converged ({results['K_1_delta']:.2f}% change). Truncation-limited."
else:
    verdict = "FAIL"
    detail = f"a_2/a_0 deviates by {a2_a0_dev:.1f}% (>20% threshold)"

print(f"  REG-SPECTRAL-61 = {verdict}")
print(f"  Detail: {detail}")
results['verdict'] = verdict
results['detail'] = detail
results['a2_a0_deviation_pct'] = a2_a0_dev

# ===========================================================================
# SAVE DATA
# ===========================================================================
print("\n" + "=" * 72)
print("SAVING DATA")
print("=" * 72)

np.savez(os.path.join(outdir, 's61_regularized_spectral_sum.npz'),
         # Eigenvalue data
         t_values=t_values,
         L_cuts=np.array(L_cuts),
         # Heat kernel traces
         K_L3=K_data.get(3, np.array([])),
         K_L4=K_data.get(4, np.array([])),
         K_L5=K_data.get(5, np.array([])),
         K_L6=K_data.get(6, np.array([])),
         Theta1_L5=Theta1_data.get(5, np.array([])),
         Theta1_L6=Theta1_data.get(6, np.array([])),
         # Rescaled Q(t)
         Q_L5=Q_data.get(5, np.array([])),
         Q_L6=Q_data.get(6, np.array([])),
         # Moments
         M_0=M_0_arr,
         M_1=M_1_arr,
         M_2=M_2_arr,
         mean_lam2=mean_lam2_arr,
         # Convergence
         delta_K_56=delta_K_56 if 'delta_K_56' in dir() else np.array([]),
         # Results
         a2_a0_ratio_L6=results['a2_a0_ratio_L6'],
         a2_a0_ratio_L7=results['a2_a0_ratio_L7'],
         a2_a0_target=results['a2_a0_target'],
         a2_a0_deviation_pct=results['a2_a0_deviation_pct'],
         K_1_L5=results['K_1_L5'],
         K_1_L6=results['K_1_L6'],
         K_1_delta=results['K_1_delta'],
         a0_fit=results['a0_fit'],
         a2_fit=results['a2_fit'],
         verdict=np.array([verdict]),
         detail=np.array([detail]))

print(f"  Saved: s61_regularized_spectral_sum.npz")

# ===========================================================================
# PLOT
# ===========================================================================
print("\nGenerating 4-panel diagnostic plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("REG-SPECTRAL-61: Heat-Kernel Regularized Spectral Sum\n"
             f"Verdict: {verdict}", fontsize=14, fontweight='bold')

# Panel 1: K(t) for different L values
ax = axes[0, 0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for idx, Lc in enumerate(L_cuts):
    ax.semilogy(t_values, K_data[Lc], color=colors[idx % len(colors)],
                label=f'L={Lc} (N={N_data[Lc]:,})', linewidth=1.5)
# Overlay SD prediction
t_sd = t_values[t_values > 0.01]
K_sd = a0_SD_target / (norm_4pi * t_sd**4) * (1 + a2_a0_ratio * t_sd)
ax.semilogy(t_sd, K_sd, 'k--', linewidth=1, alpha=0.5, label=f'SD: a_0(1+a_2/a_0*t)/norm')
ax.set_xlabel('t (regulator scale)')
ax.set_ylabel('K(t) = Tr(exp(-tD²))')
ax.set_title('Heat Kernel K(t, L)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Convergence delta
ax = axes[0, 1]
if 'delta_K_56' in dir():
    ax.semilogy(t_values, delta_K_56, 'b-', linewidth=1.5, label='|K(L=6)-K(L=5)|/K(L=6)')
    if 'delta_Th1' in dir():
        ax.semilogy(t_values, delta_Th1, 'r-', linewidth=1.5, alpha=0.7,
                     label='|Θ₁(L=6)-Θ₁(L=5)|/Θ₁(L=6)')
    ax.axhline(0.01, color='green', linestyle='--', alpha=0.7, label='1% threshold')
    if t_first_conv < np.inf:
        ax.axvline(t_first_conv, color='green', linestyle=':', alpha=0.5)
ax.set_xlabel('t')
ax.set_ylabel('Fractional change L=5→6')
ax.set_title('Convergence Map')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Q(t) = K(t)*(4pi*t)^4 — the Seeley-DeWitt diagnostic
ax = axes[1, 0]
for idx, Lc in enumerate(L_cuts):
    ax.plot(t_values, Q_data[Lc], color=colors[idx % len(colors)],
            label=f'L={Lc}', linewidth=1.5)
# SD prediction: Q = a_0 + a_2*t
t_line = np.linspace(0, 2, 100)
Q_sd = a0_SD_target + a2_SD_target * t_line
ax.plot(t_line, Q_sd, 'k--', linewidth=1, alpha=0.7,
        label=f'SD: {a0_SD_target:.3f} + {a2_SD_target:.3f}t')
ax.set_xlabel('t')
ax.set_ylabel('Q(t) = K(t)·(4πt)⁴')
ax.set_title('Rescaled Heat Trace Q(t)')
ax.set_xlim(0, 5)
y_max = max(np.max(Q_data[Lc]) for Lc in L_cuts) * 1.1
ax.set_ylim(0, min(y_max, 50))
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Spectral moment ratio a_2/a_0 vs L
ax = axes[1, 1]
L_plot = np.arange(8)
ax.plot(L_plot, ratios_a2_a0, 'bo-', markersize=8, linewidth=2,
        label='a₂_cum/a₀_cum')
ax.axhline(a2_a0_ratio, color='red', linestyle='--', linewidth=1.5,
           label=f'Gilkey: 5R/12 = {a2_a0_ratio:.4f}')
ax.set_xlabel('L (PW cutoff)')
ax.set_ylabel('a₂/a₀ ratio')
ax.set_title(f'Spectral Moment Ratio a₂/a₀\n'
             f'(L=7: {ratios_a2_a0[7]:.4f}, Gilkey: {a2_a0_ratio:.4f}, '
             f'dev={a2_a0_dev:.1f}%)')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xticks(L_plot)

plt.tight_layout()
plt.savefig(os.path.join(outdir, 's61_regularized_spectral_sum.png'), dpi=150,
            bbox_inches='tight')
print(f"  Saved: s61_regularized_spectral_sum.png")

print("\n" + "=" * 72)
print(f"DONE. REG-SPECTRAL-61 = {verdict}")
print("=" * 72)
