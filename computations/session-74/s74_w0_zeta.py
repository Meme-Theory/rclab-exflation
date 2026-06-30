#!/usr/bin/env python3
"""
S74 W1-J: W0-ZETA-74 -- w_0 from Zeta Regularization of Modular Trace
======================================================================

DR3 timeline driver for DESI w_0 prediction (Mack-VdD workshop priority #1).

Computes w_0 from zeta-regularized modular trace Tr_zeta(D^{-s}) at s=4 on the
KMS state of the spectral triple, using the van den Dungen submersion formalism
for the Kasparov product of the fiber Dirac operator D_K on Jensen-deformed
SU(3).

Substrate framing
-----------------
w_0 is NOT a thermodynamic fluid ratio in a cosmological spacetime. It is the
zeta-regularized finite part of the modular trace at s=4, evaluated on the KMS
state defined by the spectral triple's modular automorphism (Tomita-Takesaki
applied to the commutative C*-algebra C(SU(3)) through the spinor
representation). Direction of explanation:

    D_K spectrum  ->  modular automorphism sigma_t
                  ->  KMS state psi_beta
                  ->  Tr_zeta(D^{-s})  ->  w_0 via first-law log-derivative

Method
------
1. Load L_max = 7 D_K spectrum from cache (`s74_spectrum_cache_L9_tau019.npz`).
2. Compute truncated modular trace zeta_L(s) for L in {3,...,9} at a grid of s.
3. Extrapolate L_max -> infinity using power-law fit at each s in the
   convergent region (s > d/2 + 2 = 6 for d_n weighting, s > 10 for d_n^2).
4. Analytically continue from the convergent region to s = 4 via Pade
   approximants in s (with pole at s = 4 subtracted explicitly), yielding
   the finite part FP[zeta_D](4).
5. Compute w_0 = -d log Tr_zeta(D^{-4}) / d log Vol(SU(3)) via two independent
   routes:
   (a) Dimensional scaling: if D ~ Vol^{-1/d}, then lambda^{-s} ~ Vol^{s/d}
       and w_0 = -s/d (at s=4, d=8: w_0 = -1/2, the "pure geometric" limit).
   (b) KMS first-law with beta_GGE: the KMS state weights each eigenvalue by
       its Boltzmann factor, giving a physical dependence on Vol through the
       thermal trace. See Section 4.

6. Uncertainty propagation:
   - beta_GGE: +/-10% (Leggett scale uncertainty)
   - Vol(SU(3)): +/-5% (Weyl volume convention)
   - L_max truncation: L_max = 5, 7, 9 (bracketing)

7. Gate verdict: W0-ZETA-74.
   PASS:  w_0^zeta in [-0.925, -0.910]  with uncertainty < 0.015
   INFO:  w_0^zeta in [-0.935, -0.900]  (1.4 sigma from DESI DR2)
   FAIL:  w_0^zeta outside [-0.94, -0.88]  (DR3 falsifier)
"""

from __future__ import annotations

import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical constants
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from canonical_constants import (           # noqa: E402
    tau_fold,
    Vol_SU3_Haar,
    Vol_SU3_WRONG,
    M_KK,
    omega_L1,
    Delta_BCS,
    T_GGE_B2,
    T_acoustic,
)

# ----------------------------------------------------------------------------
#  Section 1: Load spectrum
# ----------------------------------------------------------------------------

SPEC_CACHE = os.path.join(HERE, "s74_spectrum_cache_L9_tau019.npz")
GGE_CACHE = os.path.join(HERE, "s56_gge_fabric.npz")
OUT_NPZ = os.path.join(HERE, "s74_w0_zeta.npz")
OUT_PNG = os.path.join(HERE, "s74_w0_zeta.png")


def load_spectrum(Lmax_cut: int):
    """Load D_K eigenvalues up to given L_max level."""
    data = np.load(SPEC_CACHE, allow_pickle=True)
    sector_evals = data["sector_evals"].item()
    evals = []
    dims = []
    for key, info in sector_evals.items():
        if info["level"] > Lmax_cut:
            continue
        dim = info["dim"]
        for ev in info["abs_evals"]:
            if ev > 1e-12:
                evals.append(float(ev))
                dims.append(int(dim))
    return np.asarray(evals), np.asarray(dims, dtype=float)


def partial_sum(evals: np.ndarray, dims: np.ndarray, s: float, weight_pow: int) -> float:
    """Compute sum_n d_n^weight_pow * lambda_n^{-s}."""
    w = dims**weight_pow
    return float(np.sum(w * evals**(-s)))


# ----------------------------------------------------------------------------
#  Section 2: L_max extrapolation in the convergent region
# ----------------------------------------------------------------------------

def lmax_extrapolate(s: float, Lmax_values, weight_pow: int = 1) -> dict:
    """
    Fit zeta_L(s) ~ A + B / L^alpha + C / L^(2 alpha) at each s value.
    Returns the extrapolated A (L_max -> infinity limit).
    """
    L_arr = np.array(Lmax_values, dtype=float)
    vals = []
    for Lc in Lmax_values:
        evs, ds = load_spectrum(int(Lc))
        vals.append(partial_sum(evs, ds, s, weight_pow))
    vals = np.array(vals)

    # For convergent sequences, fit A + B*L^{-alpha} using alpha = 1, 2, 3
    # and take the best-converged extrapolation.
    # Use log-linear fit of (vals - A_guess) vs log(L) to determine alpha.
    if len(L_arr) < 3:
        return {"A": vals[-1], "alpha": np.nan, "B": np.nan, "fit_err": np.inf, "vals": vals}

    # Try a Richardson-type 3-point extrapolation:
    # Assume A_L = A + c1*L^{-1} + c2*L^{-2} + ...
    # With 3 L values solve A + c1/L + c2/L^2 = vals[k] for each k.
    # For robustness use the last 4 L values.
    L_fit = L_arr[-4:] if len(L_arr) >= 4 else L_arr
    V_fit = vals[-len(L_fit):]

    # Fit y = A + B/L + C/L^2
    X = np.column_stack([np.ones_like(L_fit), 1.0/L_fit, 1.0/L_fit**2])
    try:
        coef, resid, rank, sv = np.linalg.lstsq(X, V_fit, rcond=None)
        A = coef[0]
        B = coef[1]
        C = coef[2]
        # residual magnitude
        pred = X @ coef
        err = np.linalg.norm(pred - V_fit) / max(1.0, np.linalg.norm(V_fit))
    except np.linalg.LinAlgError:
        A = vals[-1]
        B = np.nan
        C = np.nan
        err = np.inf

    return {
        "A": float(A), "B": float(B), "C": float(C),
        "fit_err": float(err),
        "vals": vals,
        "L_vals": L_arr,
    }


# ----------------------------------------------------------------------------
#  Section 3: Zeta grid and Pade continuation
# ----------------------------------------------------------------------------

def compute_zeta_grid(s_values, Lmax_values, weight_pow: int = 1):
    """
    Compute the truncated modular trace at a grid of s values.
    Returns dict with raw sums and extrapolated limits.
    """
    results = {}
    for s in s_values:
        results[float(s)] = lmax_extrapolate(float(s), Lmax_values, weight_pow=weight_pow)
    return results


def pade_fit_s(s_grid, zeta_vals, s_eval, n_num=2, n_den=2):
    """
    Fit a Pade [n_num/n_den] approximant in s to (s_grid, zeta_vals) and
    evaluate at s_eval.
    Pade form: zeta(s) ~ P(s) / Q(s) with Q(s_pole) = 0 for s_pole in
    {8, 6, 4, 2, 0} (heat kernel poles for d=8).
    """
    # Use log of zeta to stabilize fit in the convergent region,
    # then linearize via log(zeta) ~ linear in s.
    s_arr = np.asarray(s_grid, dtype=float)
    z_arr = np.asarray(zeta_vals, dtype=float)

    # Sort by s
    order = np.argsort(s_arr)
    s_arr = s_arr[order]
    z_arr = z_arr[order]

    # Strip any NaN/Inf
    mask = np.isfinite(z_arr) & (z_arr > 0)
    s_arr = s_arr[mask]
    z_arr = z_arr[mask]

    # Fit log(zeta) vs s with polynomial of degree n_num + n_den
    # then exponentiate and evaluate at s_eval.
    if len(s_arr) < n_num + n_den + 1:
        # Insufficient data, fallback to linear extrapolation
        if len(s_arr) >= 2:
            logz = np.log(z_arr)
            coef = np.polyfit(s_arr, logz, 1)
            return float(np.exp(np.polyval(coef, s_eval)))
        else:
            return float(z_arr[-1])

    logz = np.log(z_arr)
    deg = min(len(s_arr) - 1, 4)
    coef = np.polyfit(s_arr, logz, deg)
    return float(np.exp(np.polyval(coef, s_eval)))


def pade_rational_fit(s_grid, zeta_vals, s_eval, poles=(8, 6, 4, 2, 0)):
    """
    Alternative Pade using explicit pole structure:
    zeta(s) = sum_k R_k / (s - p_k) + P_reg(s)
    where P_reg is a low-order polynomial (the regular part).
    Fit R_k and polynomial coefficients by least-squares.
    Evaluate the FINITE PART at s_eval (skipping the k for which p_k = s_eval).
    """
    s_arr = np.asarray(s_grid, dtype=float)
    z_arr = np.asarray(zeta_vals, dtype=float)
    mask = np.isfinite(z_arr)
    s_arr = s_arr[mask]
    z_arr = z_arr[mask]

    # Only include poles NOT equal to s_eval (else we blow up at the pole)
    active_poles = [p for p in poles if abs(p - s_eval) > 1e-9]

    # Design matrix: one column per pole + polynomial columns
    n_poly = 2  # linear polynomial regular part: a + b*(s - s_eval)
    X = np.zeros((len(s_arr), len(active_poles) + n_poly))
    for k, p in enumerate(active_poles):
        X[:, k] = 1.0 / (s_arr - p)
    for j in range(n_poly):
        X[:, len(active_poles) + j] = (s_arr - s_eval)**j

    try:
        coef, resid, rank, sv = np.linalg.lstsq(X, z_arr, rcond=None)
    except np.linalg.LinAlgError:
        coef = np.zeros(X.shape[1])

    # Evaluate FINITE PART at s_eval: residues at active poles + polynomial at s=s_eval
    # At s = s_eval, 1/(s - p) = 1/(s_eval - p), and polynomial term = coef[pole_idx_0 + 0].
    val = 0.0  # (local)
    for k, p in enumerate(active_poles):
        val += coef[k] / (s_eval - p)
    val += coef[len(active_poles)]  # constant polynomial term
    return float(val), coef, active_poles


# ----------------------------------------------------------------------------
#  Section 4: w_0 from KMS-modular first law
# ----------------------------------------------------------------------------

def compute_modular_trace_kms(evals, dims, beta, s, weight_pow: int = 1):
    """
    Modular trace on the KMS state at inverse temperature beta:
    Tr_{KMS}(D^{-s}) = sum_n d_n^weight_pow * exp(-beta * lambda_n) * lambda_n^{-s}
    The Boltzmann factor tames the UV divergence exactly as beta > 0.
    At s in the pole region, this gives a finite physical trace for any beta > 0.
    """
    w = dims**weight_pow
    return float(np.sum(w * np.exp(-beta * evals) * evals**(-s)))


def compute_w0_from_kms(evals, dims, beta, s=4.0, weight_pow: int = 1):
    """
    Compute w_0 = -d log Tr_{KMS}(D^{-s}) / d log Vol
    under the assumption that Vol scales the eigenvalues as
    lambda -> (Vol_0 / Vol)^{1/d} * lambda    (Weyl scaling, d = 8)

    Chain rule:
        Tr_{KMS}(s; Vol) = sum d_n^weight exp(-beta * lambda * (V0/V)^{1/d}) * (lambda * (V0/V)^{1/d})^{-s}

    Take log and differentiate w.r.t. log(V/V0) at V = V0:
        d/d logV [-s * (1/d) * logV  -  beta * lambda * (V0/V)^{1/d}]
      = -s/d  +  (beta * lambda / d) * (V0/V)^{1/d}

    So the log-derivative of Tr_{KMS} is a weighted average of the per-mode
    contribution against the KMS weights. This gives w_0 naturally from the
    SPECTRAL side, using the KMS state as the weight.
    """
    # Weights: w_n = d_n^weight * exp(-beta * lambda_n) * lambda_n^{-s}
    w_n = dims**weight_pow * np.exp(-beta * evals) * evals**(-s)
    total = np.sum(w_n)

    # Per-mode log-derivative factor (for eigenvalue scaling lambda -> lambda * (V0/V)^{1/d}):
    # d log(Tr) / d logV = - sum_n w_n * [s/d + (beta * lambda_n / d) * (1 - 1)] / total
    # Actually the KMS exponential gives a more subtle result — expand carefully below.

    # Parameterize eps = log(V/V0), so lambda(eps) = lambda_0 * exp(-eps/d).
    # Tr(eps) = sum w_n(eps) * lambda_n(eps)^{-s}
    #         = sum d_n^weight * exp(-beta * lambda_0 * exp(-eps/d)) * (lambda_0 * exp(-eps/d))^{-s}
    #         = e^(s eps/d) * sum d_n^weight * exp(-beta * lambda_0 * e^{-eps/d}) * lambda_0^{-s}
    # d log(Tr)/d eps |_{eps=0}
    #   = s/d  +  [d/d eps of log(sum d_n^weight * exp(-beta * lambda_0 * e^{-eps/d}) * lambda_0^{-s})]|_{0}
    #   = s/d  +  (1/Tr) * sum d_n^weight * lambda_0^{-s} * exp(-beta * lambda_0) * (+beta * lambda_0 / d)
    #
    # Note: d/d eps [exp(-beta * lambda_0 * e^{-eps/d})] = exp(-beta*lambda_0*e^{-eps/d}) * (+beta*lambda_0/d*e^{-eps/d})
    # At eps = 0: = exp(-beta*lambda_0) * (beta*lambda_0/d)
    #
    # So d log(Tr) / d logV = s/d + <beta * lambda / d>_{KMS}
    # where <.>_{KMS} is the KMS-weighted expectation.
    #
    # Therefore:
    #   w_0 = -d log(rho_vac)/d logV  where rho_vac = Tr/V
    # rho = Tr / V, so d log rho / d logV = d log Tr / d logV - 1
    # w_0 = -(d log Tr / d logV - 1) = 1 - d log Tr / d logV
    # w_0 = 1 - s/d - <beta * lambda / d>_{KMS}
    #
    # This is the operational formula we evaluate.
    d_dim = 8  # SU(3) real dimension
    mean_beta_lambda = float(np.sum(w_n * beta * evals) / total)
    d_logTr_d_logV = s / d_dim + mean_beta_lambda / d_dim
    w_0 = 1.0 - d_logTr_d_logV
    return {
        "w_0": float(w_0),
        "d_logTr_d_logV": float(d_logTr_d_logV),
        "mean_beta_lambda": float(mean_beta_lambda),
        "total": float(total),
    }


def compute_w0_pure_geometric(s=4.0, d_dim=8):
    """
    Pure geometric limit: no KMS weighting, just dimensional (Weyl) scaling.

    Under Weyl rescaling lambda -> lambda * (V_0/V)^{1/d}, we have
        Tr_zeta(D^{-s}) = sum d_n lambda^{-s} ~ V^{s/d}
    (proportional, since d_n is V-independent).
    Therefore
        rho_vac = Tr_zeta / V ~ V^{s/d - 1}
        d log rho / d log V = s/d - 1
        w_0 = -d log rho / d log V = 1 - s/d

    For s=4, d=8: w_0 = +0.5 (POSITIVE).
    For s=8, d=8: w_0 =  0.0 (vacuum trace).
    For s=12, d=8: w_0 = -0.5.

    The pure-geometric result is +0.5, not -0.918. The KMS weighting
    provides the negative-pressure correction.
    """
    return 1.0 - s/d_dim


def scan_beta(evals, dims, beta_range, s=4.0, weight_pow=1):
    """Scan beta for w_0 from KMS, useful for sensitivity analysis."""
    results = []
    for b in beta_range:
        r = compute_w0_from_kms(evals, dims, b, s=s, weight_pow=weight_pow)
        results.append({"beta": b, "w_0": r["w_0"], "T": 1.0/b})
    return results


def solve_beta_for_target_w0(evals, dims, target_w0, s=4.0, weight_pow=1,
                              bracket=(0.1, 50.0)):
    """Find beta such that w_0(beta) = target_w0 via bisection."""
    from scipy.optimize import brentq
    def f(b):
        return compute_w0_from_kms(evals, dims, b, s=s, weight_pow=weight_pow)["w_0"] - target_w0
    try:
        return float(brentq(f, bracket[0], bracket[1]))
    except Exception:
        return None


# ----------------------------------------------------------------------------
#  Section 5: Main routine
# ----------------------------------------------------------------------------

def main():
    t0 = time.time()
    print("="*70)
    print("S74 W1-J: W0-ZETA-74 -- w_0 from zeta regularization of modular trace")
    print("="*70)
    print(f"tau_fold = {tau_fold}")
    print(f"Vol_SU3_Haar (canonical) = {Vol_SU3_Haar:.4f}")
    print(f"Vol_SU3_WRONG (task's 8880.9) = {Vol_SU3_WRONG:.4f}")
    print(f"omega_L1 = {omega_L1} (canonical S52)  [task brief cited 0.0492 -- mismatch]")
    print(f"Delta_BCS = {Delta_BCS}")
    print()

    # ------------------------------------------------------------------
    # Step 1: beta_GGE from Leggett scale
    # Task says beta_GGE = 1/omega_L1. With canonical omega_L1 = 0.138,
    # beta_GGE_canonical = 1/0.138 = 7.246 M_KK^-1.
    # Task brief cites omega_L1 = 0.0492, beta_GGE = 20.3 (STALE VALUE).
    # We compute both for robustness.
    # ------------------------------------------------------------------
    beta_canonical = 1.0 / omega_L1        # = 7.246 M_KK^-1
    beta_task = 1.0 / 0.0492               # = 20.3  (as cited in task brief)
    # Alternative: use T_GGE_B2 = 0.668 (B2 sector GGE)
    beta_T_GGE_B2 = 1.0 / T_GGE_B2         # = 1.497
    beta_T_acoustic = 1.0 / T_acoustic     # = 8.929
    print(f"beta_GGE (canonical, 1/omega_L1): {beta_canonical:.4f}")
    print(f"beta_GGE (task brief, 1/0.0492): {beta_task:.4f}")
    print(f"beta (1/T_GGE_B2): {beta_T_GGE_B2:.4f}")
    print(f"beta (1/T_acoustic): {beta_T_acoustic:.4f}")

    # ------------------------------------------------------------------
    # Step 2: Load L_max = 7 spectrum
    # ------------------------------------------------------------------
    L_MAX = 7  # (local)
    Lmax_grid = [3, 4, 5, 6, 7, 8, 9]
    evals_L7, dims_L7 = load_spectrum(L_MAX)
    print(f"\nL_max = {L_MAX}: {len(evals_L7)} bare eigenvalues, "
          f"sum d_n = {int(dims_L7.sum())}, sum d_n^2 = {int((dims_L7**2).sum())}")
    print(f"  lambda_max = {evals_L7.max():.4f}, lambda_min = {evals_L7.min():.4f}")

    # ------------------------------------------------------------------
    # Step 3: Compute Tr_zeta(D^-s) at s in {1, 2, 3, 4} with d_n and d_n^2
    # ------------------------------------------------------------------
    print("\n--- Raw modular trace at L_max = 7 ---")
    print(f"{'s':>4s}  {'d_n weight':>14s}  {'d_n^2 weight':>14s}")
    raw_trace = {}
    for s in [1, 2, 3, 4]:
        p_dn = partial_sum(evals_L7, dims_L7, s, 1)
        p_dn2 = partial_sum(evals_L7, dims_L7, s, 2)
        raw_trace[s] = {"dn": p_dn, "dn2": p_dn2}
        print(f"{s:>4d}  {p_dn:>14.4e}  {p_dn2:>14.4e}")

    # Compare with W1-C canonical values
    print("\nCross-check vs W1-C canonical a_k^zeta (d=8):")
    print(f"  a_0^zeta = sum d_n lambda^{{-8}} = 2185.46  [W1-C L_max=7]")
    print(f"  a_2^zeta = sum d_n lambda^{{-6}} = 6831.81  [W1-C L_max=7]")
    print(f"  a_4^zeta = sum d_n lambda^{{-4}} = 30633.88 [W1-C L_max=7] <- same as Tr_zeta(D^{{-4}}) with d_n weight")
    p_a0 = partial_sum(evals_L7, dims_L7, 8, 1)
    p_a2 = partial_sum(evals_L7, dims_L7, 6, 1)
    p_a4 = partial_sum(evals_L7, dims_L7, 4, 1)
    print(f"Re-computed:    a_0 = {p_a0:.4f}, a_2 = {p_a2:.4f}, a_4 = {p_a4:.4f}")
    assert abs(p_a4 - 30633.878) < 0.1, "a_4 mismatch!"

    # ------------------------------------------------------------------
    # Step 4: L_max scaling — compute zeta_L(s) at wide grid for extrapolation
    # ------------------------------------------------------------------
    print("\n--- L_max scaling (d_n weighting) ---")
    s_grid_wide = np.linspace(4.0, 16.0, 49)  # step 0.25
    zeta_grid_dn = {}
    for s in s_grid_wide:
        zeta_grid_dn[float(s)] = lmax_extrapolate(float(s), Lmax_grid, weight_pow=1)

    # Print at key s values
    print(f"\n{'s':>6s}  " + "  ".join(f"L={L:<2d}" for L in Lmax_grid) + "  |  L->inf")
    for s in [4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
        r = zeta_grid_dn[s]
        row = f"{s:>6.2f}  " + "  ".join(f"{v:>10.3e}" for v in r["vals"]) + f"  |  {r['A']:.3e}  (err={r['fit_err']:.1e})"
        print(row)

    # d_n^2 variant (task-specified weighting)
    print("\n--- L_max scaling (d_n^2 weighting) ---")
    zeta_grid_dn2 = {}
    for s in s_grid_wide:
        zeta_grid_dn2[float(s)] = lmax_extrapolate(float(s), Lmax_grid, weight_pow=2)

    print(f"\n{'s':>6s}  " + "  ".join(f"L={L:<2d}" for L in Lmax_grid) + "  |  L->inf")
    for s in [4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
        r = zeta_grid_dn2[s]
        row = f"{s:>6.2f}  " + "  ".join(f"{v:>10.3e}" for v in r["vals"]) + f"  |  {r['A']:.3e}  (err={r['fit_err']:.1e})"
        print(row)

    # ------------------------------------------------------------------
    # Step 5: Analytic continuation from convergent region to s=4
    # ------------------------------------------------------------------
    # For d_n weighting, the spectral dimension is ~8, so the power sum
    # converges for s > 8. Use s-grid in the convergent region [10, 16]
    # and fit a Pade/polynomial in s, then evaluate at s=4.
    print("\n--- Pade continuation to s = 4 (d_n weighting) ---")
    s_conv = np.array([s for s in s_grid_wide if s >= 10.0])
    z_conv = np.array([zeta_grid_dn[float(s)]["A"] for s in s_conv])

    # Log-fit approach
    val_log = pade_fit_s(s_conv, z_conv, s_eval=4.0)
    print(f"  Log-poly fit value at s=4: {val_log:.4e}")

    # Rational fit with explicit pole structure
    val_rat, coef_rat, poles_rat = pade_rational_fit(s_conv, z_conv, s_eval=4.0)
    print(f"  Rational (pole-structure) fit at s=4: {val_rat:.4e}")
    print(f"  Active poles: {poles_rat}")

    # Reference: direct L->infinity extrapolation at s=4 (divergent, so this
    # is just a "raw truncated" estimate)
    val_direct = zeta_grid_dn[4.0]["A"]
    print(f"  L_max->inf direct extrapolation at s=4: {val_direct:.4e}")
    print(f"  L_max=7 raw value at s=4: {raw_trace[4]['dn']:.4e}")

    # Repeat for d_n^2 weighting
    print("\n--- Pade continuation to s = 4 (d_n^2 weighting) ---")
    s_conv2 = np.array([s for s in s_grid_wide if s >= 12.0])
    z_conv2 = np.array([zeta_grid_dn2[float(s)]["A"] for s in s_conv2])
    val_log2 = pade_fit_s(s_conv2, z_conv2, s_eval=4.0)
    val_rat2, coef_rat2, poles_rat2 = pade_rational_fit(s_conv2, z_conv2, s_eval=4.0)
    val_direct2 = zeta_grid_dn2[4.0]["A"]
    print(f"  Log-poly fit value at s=4: {val_log2:.4e}")
    print(f"  Rational (pole-structure) fit at s=4: {val_rat2:.4e}")
    print(f"  L_max->inf direct extrapolation at s=4: {val_direct2:.4e}")
    print(f"  L_max=7 raw value at s=4: {raw_trace[4]['dn2']:.4e}")

    # ------------------------------------------------------------------
    # Step 6: KMS-modular w_0 via first law
    # ------------------------------------------------------------------
    # w_0 = 1 - s/d - <beta * lambda / d>_{KMS}
    # where the KMS weights are w_n = d_n^weight * exp(-beta*lambda) * lambda^{-s}.
    print("\n--- w_0 from KMS-modular first law ---")
    S_EVAL = 4.0  # (local)
    D_DIM = 8

    w0_results = {}
    for (beta, label) in [
        (beta_canonical, "beta=1/omega_L1 (canonical 7.246)"),
        (beta_task,      "beta=1/0.0492 (task brief 20.3)"),
        (beta_T_GGE_B2,  "beta=1/T_GGE_B2 (1.497)"),
        (beta_T_acoustic,"beta=1/T_acoustic (8.929)"),
    ]:
        res_dn = compute_w0_from_kms(evals_L7, dims_L7, beta, s=S_EVAL, weight_pow=1)
        res_dn2 = compute_w0_from_kms(evals_L7, dims_L7, beta, s=S_EVAL, weight_pow=2)
        w0_results[label] = {
            "beta": beta,
            "dn": res_dn,
            "dn2": res_dn2,
        }
        print(f"\n  {label}: beta = {beta:.4f}")
        print(f"    d_n   weighting: w_0 = {res_dn['w_0']:+.5f}  (d logTr/d logV = {res_dn['d_logTr_d_logV']:.5f})")
        print(f"    d_n^2 weighting: w_0 = {res_dn2['w_0']:+.5f}  (d logTr/d logV = {res_dn2['d_logTr_d_logV']:.5f})")

    # ------------------------------------------------------------------
    # Step 7: Pure geometric comparison (no KMS)
    # ------------------------------------------------------------------
    w0_pure_geom = compute_w0_pure_geometric(s=S_EVAL, d_dim=D_DIM)
    print(f"\n  Pure geometric (no KMS, Weyl scaling only): w_0 = {w0_pure_geom:+.5f}")
    print("  This is the 'dimensional analysis' limit: w_0 = 1 - s/d = +0.5.")
    print("  The KMS weighting is what drives w_0 below 0.")

    # Sign convention check: if we compute w_0 = -d log Tr_zeta / d log V
    # (not from rho_vac = Tr/V), we get a different sign.
    # Geometric: Tr_zeta ~ V^{s/d}, so d log Tr/d log V = s/d = 0.5.
    # w_0^alt = -d log Tr / d log V = -0.5.
    w0_geom_alt = -S_EVAL/D_DIM
    print(f"  Alternative convention w_0 = -d log Tr / d log V: {w0_geom_alt:+.5f}")
    print("  (matches the 'raw task formula' without rho_vac = Tr/V normalization)")

    # Spectral-action-weighted w_0: using ALL a_k terms weighted by f_k * Lambda^{d-2k}
    print("\n  Spectral action-weighted w_0 (all a_k terms, Lambda fixed):")
    # SDW scaling: a_{2k} ~ V^{(d-2k)/d} = V^{1 - k/(d/2)} = V^{1 - k/4} (d=8)
    Lambda_sa = 12.908  # S73A optimal cutoff
    a_coeffs = {
        0: partial_sum(evals_L7, dims_L7, 8, 1),  # a_0 = sum d_n lambda^{-8}
        1: partial_sum(evals_L7, dims_L7, 6, 1),  # a_2
        2: partial_sum(evals_L7, dims_L7, 4, 1),  # a_4
        3: partial_sum(evals_L7, dims_L7, 2, 1),  # a_6
        4: partial_sum(evals_L7, dims_L7, 0, 1),  # a_8 = N_modes (total state count)
    }
    alpha_k = [1 - k/(D_DIM/2) for k in range(5)]  # = [1, 0.75, 0.5, 0.25, 0]
    f_weights_unit = [1.0, 1.0, 1.0, 1.0, 1.0]
    # Gaussian cutoff moments: f_0 = 1, f_2 = 1/2, f_4 = 1/6, f_6 = 1/24, f_8 = 1/120
    f_weights_gauss = [1.0, 1.0, 1.0/2, 1.0/6, 1.0/24]
    for weights, label in [(f_weights_unit, "unit f_k"),
                            (f_weights_gauss, "Gaussian f_k")]:
        terms = [weights[k] * a_coeffs[k] * Lambda_sa**(D_DIM - 2*k) for k in range(5)]
        S_sa = sum(terms)
        weighted_alpha = sum(alpha_k[k]*terms[k] for k in range(5)) / S_sa
        w_sa = -weighted_alpha
        print(f"    {label}: w_0 = {w_sa:+.5f}  (a_0 fraction = {terms[0]/S_sa:.4f})")

    # Solve for the beta that reproduces the Volovik-partition target -0.918
    target_w0 = -0.918  # (local)
    beta_target_dn = solve_beta_for_target_w0(
        evals_L7, dims_L7, target_w0, s=S_EVAL, weight_pow=1
    )
    beta_target_dn2 = solve_beta_for_target_w0(
        evals_L7, dims_L7, target_w0, s=S_EVAL, weight_pow=2
    )
    print(f"\n  Inverse solve: what beta gives w_0 = {target_w0}?")
    if beta_target_dn is not None:
        T_target = 1.0/beta_target_dn
        print(f"    d_n   weighting: beta = {beta_target_dn:.4f}  <=>  T = {T_target:.4f} M_KK")
        scales = {
            "omega_L1": omega_L1,
            "omega_L2": 0.192,
            "omega_H1": 0.380,
            "Delta_BCS": Delta_BCS,
            "E_B1": 0.8191,
            "T_acoustic": T_acoustic,
            "T_GGE_B2": T_GGE_B2,
        }
        ratios = {k: T_target/v for k, v in scales.items()}
        print(f"    Ratios T_target/scale: {ratios}")
    if beta_target_dn2 is not None:
        T_target2 = 1.0/beta_target_dn2
        print(f"    d_n^2 weighting: beta = {beta_target_dn2:.4f}  <=>  T = {T_target2:.4f} M_KK")

    # ------------------------------------------------------------------
    # Step 8: Identify the "canonical" w_0 and uncertainty
    # ------------------------------------------------------------------
    # Canonical choice: d_n weighting (matches framework S41/S42/S73B convention)
    # and beta = 1/omega_L1_canonical (S52 Leggett-1 frequency).
    beta_central = beta_canonical
    res_central = compute_w0_from_kms(evals_L7, dims_L7, beta_central, s=S_EVAL, weight_pow=1)
    w0_central = res_central["w_0"]
    print(f"\n=== CANONICAL w_0 (d_n weighting, beta = 1/omega_L1_S52) ===")
    print(f"w_0 = {w0_central:+.5f}")

    # Uncertainty propagation: vary beta by +/-10%, Vol implicitly through L_max +/-
    print("\n--- Uncertainty propagation ---")

    # (a) beta +/- 10%
    beta_hi = beta_central * 1.10
    beta_lo = beta_central * 0.90
    w0_hi_beta = compute_w0_from_kms(evals_L7, dims_L7, beta_hi, s=S_EVAL, weight_pow=1)["w_0"]
    w0_lo_beta = compute_w0_from_kms(evals_L7, dims_L7, beta_lo, s=S_EVAL, weight_pow=1)["w_0"]
    delta_w0_beta = 0.5 * abs(w0_hi_beta - w0_lo_beta)
    print(f"  beta +/-10%: w_0 range = [{min(w0_hi_beta, w0_lo_beta):+.5f}, {max(w0_hi_beta, w0_lo_beta):+.5f}], delta = +/-{delta_w0_beta:.5f}")

    # (b) Vol +/- 5% — under Weyl scaling, lambda -> lambda * (V0/V)^{1/d}
    # A 5% change in V corresponds to lambda scaling by (1.05)^{-1/8} or (0.95)^{-1/8}.
    V_scale_hi = 1.05**(-1.0/D_DIM)  # lambda multiplied by this for V=V0*1.05
    V_scale_lo = 0.95**(-1.0/D_DIM)
    evals_V_hi = evals_L7 * V_scale_hi
    evals_V_lo = evals_L7 * V_scale_lo
    w0_hi_V = compute_w0_from_kms(evals_V_hi, dims_L7, beta_central, s=S_EVAL, weight_pow=1)["w_0"]
    w0_lo_V = compute_w0_from_kms(evals_V_lo, dims_L7, beta_central, s=S_EVAL, weight_pow=1)["w_0"]
    delta_w0_V = 0.5 * abs(w0_hi_V - w0_lo_V)
    print(f"  Vol +/-5%: w_0 range = [{min(w0_hi_V, w0_lo_V):+.5f}, {max(w0_hi_V, w0_lo_V):+.5f}], delta = +/-{delta_w0_V:.5f}")

    # (c) L_max = 5, 7, 9 bracketing
    w0_L = {}
    for L in [5, 7, 9]:
        evs_L, ds_L = load_spectrum(L)
        w0_L[L] = compute_w0_from_kms(evs_L, ds_L, beta_central, s=S_EVAL, weight_pow=1)["w_0"]
    print(f"  L_max scan:")
    for L in [5, 7, 9]:
        print(f"    L_max = {L}: w_0 = {w0_L[L]:+.5f}")
    delta_w0_Lmax = 0.5 * (w0_L[9] - w0_L[5])  # approx linear extrapolation error

    # Total uncertainty: RSS
    delta_w0_total = float(np.sqrt(delta_w0_beta**2 + delta_w0_V**2 + delta_w0_Lmax**2))
    print(f"\n  Total uncertainty (RSS): +/-{delta_w0_total:.5f}")

    # ------------------------------------------------------------------
    # Step 9: Gate verdict
    # ------------------------------------------------------------------
    print("\n" + "="*70)
    print("Gate W0-ZETA-74 verdict")
    print("="*70)
    print(f"Central value: w_0 = {w0_central:+.5f} +/- {delta_w0_total:.5f}")
    w0_low = w0_central - delta_w0_total
    w0_high = w0_central + delta_w0_total
    print(f"1-sigma range: [{w0_low:+.5f}, {w0_high:+.5f}]")

    pass_range = (-0.925, -0.910)
    info_range = (-0.935, -0.900)
    fail_range = (-0.94, -0.88)

    if pass_range[0] <= w0_central <= pass_range[1] and delta_w0_total < 0.015:
        verdict = "PASS"
        explanation = f"w_0 = {w0_central:+.5f} in PASS range {pass_range} with sigma = {delta_w0_total:.5f} < 0.015"
    elif info_range[0] <= w0_central <= info_range[1]:
        verdict = "INFO"
        explanation = f"w_0 = {w0_central:+.5f} in INFO range {info_range} (broader 1.4 sigma from DESI DR2)"
    elif fail_range[0] <= w0_central <= fail_range[1]:
        verdict = "INFO"
        explanation = f"w_0 = {w0_central:+.5f} in extended tolerance range {fail_range}"
    else:
        verdict = "FAIL"
        explanation = f"w_0 = {w0_central:+.5f} OUTSIDE DR3 falsifier band {fail_range}"

    print(f"\nGate verdict: {verdict}")
    print(f"  {explanation}")

    # Compare to S66 Volovik w_0 = -0.918
    print(f"\nComparison to S66 Volovik q-theory: w_0 = -0.918")
    diff_S66 = w0_central - (-0.918)
    print(f"  Framework minus S66: {diff_S66:+.5f}")
    print(f"  |Difference|/sigma: {abs(diff_S66)/max(delta_w0_total, 1e-9):.2f}")

    # Compare to DESI DR2 w_0 = -0.752 +/- 0.057
    print(f"\nComparison to DESI DR2: w_0 = -0.752 +/- 0.057")
    diff_DR2 = w0_central - (-0.752)
    sigma_DR2 = float(np.sqrt(delta_w0_total**2 + 0.057**2))
    print(f"  Framework minus DR2: {diff_DR2:+.5f}")
    print(f"  Tension (n-sigma): {abs(diff_DR2)/sigma_DR2:.2f}")

    # ------------------------------------------------------------------
    # Step 10: Cross-check — s = 0 limiting case
    # ------------------------------------------------------------------
    print("\n--- Cross-check: s = 0 limit (total state count) ---")
    # Tr(D^0) = sum d_n^weight (finite eigenvalue count)
    n_dn = float(np.sum(dims_L7))
    n_dn2 = float(np.sum(dims_L7**2))
    print(f"  sum d_n (Peter-Weyl dim) = {int(n_dn)} (framework L_max=7 canonical 1,077,120)")
    print(f"  sum d_n^2 = {int(n_dn2)}")
    print(f"  Check: 1,077,120 matches? {int(n_dn) == 1077120}")

    # Dimensional consistency: w_0 dimensionless
    print("\n--- Cross-check: dimensional consistency ---")
    print("  w_0 = 1 - s/d - <beta*lambda/d>_KMS")
    print("  Each term is dimensionless:")
    print(f"    s/d = {S_EVAL}/{D_DIM} = {S_EVAL/D_DIM:.4f}  (dimensionless)")
    print(f"    beta*lambda: beta in M_KK^-1, lambda in M_KK, product dimensionless  [OK]")

    # ------------------------------------------------------------------
    # Step 11: Save data
    # ------------------------------------------------------------------
    # Collect alternative w_0 computations for archival
    # Spectral action weighted
    a_coeffs_final = {
        0: partial_sum(evals_L7, dims_L7, 8, 1),
        1: partial_sum(evals_L7, dims_L7, 6, 1),
        2: partial_sum(evals_L7, dims_L7, 4, 1),
        3: partial_sum(evals_L7, dims_L7, 2, 1),
        4: partial_sum(evals_L7, dims_L7, 0, 1),
    }
    alpha_k_final = [1 - k/4.0 for k in range(5)]
    Lambda_sa_final = 12.908  # (local)
    terms_unit = [a_coeffs_final[k] * Lambda_sa_final**(8 - 2*k) for k in range(5)]
    S_sa_unit = sum(terms_unit)
    w0_sa_unit = -sum(alpha_k_final[k]*terms_unit[k] for k in range(5)) / S_sa_unit

    # Inverse solve
    beta_target_final = solve_beta_for_target_w0(
        evals_L7, dims_L7, -0.918, s=S_EVAL, weight_pow=1
    )
    T_target_final = 1.0/beta_target_final if beta_target_final is not None else np.nan

    np.savez(
        OUT_NPZ,
        w_0_central=w0_central,
        delta_w0_total=delta_w0_total,
        delta_w0_beta=delta_w0_beta,
        delta_w0_V=delta_w0_V,
        delta_w0_Lmax=delta_w0_Lmax,
        Tr_zeta_s1_dn=raw_trace[1]["dn"],
        Tr_zeta_s2_dn=raw_trace[2]["dn"],
        Tr_zeta_s3_dn=raw_trace[3]["dn"],
        Tr_zeta_s4_dn=raw_trace[4]["dn"],
        Tr_zeta_s1_dn2=raw_trace[1]["dn2"],
        Tr_zeta_s2_dn2=raw_trace[2]["dn2"],
        Tr_zeta_s3_dn2=raw_trace[3]["dn2"],
        Tr_zeta_s4_dn2=raw_trace[4]["dn2"],
        a_4_zeta_L7=p_a4,
        beta_central=beta_central,
        beta_task=beta_task,
        beta_T_GGE_B2=beta_T_GGE_B2,
        beta_T_acoustic=beta_T_acoustic,
        w0_hi_beta=w0_hi_beta,
        w0_lo_beta=w0_lo_beta,
        w0_hi_V=w0_hi_V,
        w0_lo_V=w0_lo_V,
        w0_L5=w0_L[5],
        w0_L7=w0_L[7],
        w0_L9=w0_L[9],
        val_log_dn=val_log,
        val_rat_dn=val_rat,
        val_direct_dn=val_direct,
        val_log_dn2=val_log2,
        val_rat_dn2=val_rat2,
        val_direct_dn2=val_direct2,
        verdict=verdict,
        n_dn=n_dn,
        n_dn2=n_dn2,
        tau_fold=tau_fold,
        Vol_SU3=Vol_SU3_Haar,
        s_grid_wide=s_grid_wide,
        Lmax_grid=np.array(Lmax_grid),
        # Alternative w_0 routes
        w0_pure_geom=w0_pure_geom,           # +0.5 (1 - s/d)
        w0_alt_minus_s_over_d=w0_geom_alt,   # -0.5 (-d log Tr / d log V)
        w0_sa_unit=w0_sa_unit,               # ~-0.995 (spectral action weighted)
        # Inverse solve: beta that gives exactly -0.918
        beta_target_w0_minus_918=beta_target_final,
        T_target_w0_minus_918=T_target_final,
        # Alternative betas with their w_0 results (d_n weighting)
        w0_beta_task=w0_results["beta=1/0.0492 (task brief 20.3)"]["dn"]["w_0"],
        w0_beta_T_GGE_B2=w0_results["beta=1/T_GGE_B2 (1.497)"]["dn"]["w_0"],
        w0_beta_T_acoustic=w0_results["beta=1/T_acoustic (8.929)"]["dn"]["w_0"],
    )
    print(f"\nData saved to: {OUT_NPZ}")

    # ------------------------------------------------------------------
    # Step 12: Plot
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Panel A: L_max scaling for key s values
    ax = axes[0, 0]
    for s_key, c in zip([4.0, 6.0, 8.0, 10.0, 12.0, 14.0], ['C0','C1','C2','C3','C4','C5']):
        vals = zeta_grid_dn[s_key]["vals"]
        L_arr = zeta_grid_dn[s_key]["L_vals"]
        ax.semilogy(L_arr, vals, 'o-', color=c, label=f's={s_key}')
    ax.set_xlabel('L_max')
    ax.set_ylabel('zeta_L(s) (d_n weight)')
    ax.set_title('L_max convergence (d_n weighting)')
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: log(zeta_L) vs s at L_max=7
    ax = axes[0, 1]
    s_arr = np.sort([float(k) for k in zeta_grid_dn.keys()])
    z_arr = np.array([zeta_grid_dn[float(s)]["vals"][Lmax_grid.index(L_MAX)] for s in s_arr])
    ax.semilogy(s_arr, z_arr, 'b-', label='L_max=7')
    # Overlay extrapolated L->inf
    z_inf = np.array([zeta_grid_dn[float(s)]["A"] for s in s_arr])
    ax.semilogy(s_arr, z_inf, 'r--', label='L_max->inf extrap')
    ax.axvline(4, color='k', linestyle=':', label='s=4 (target)')
    ax.axvspan(10, 16, color='green', alpha=0.15, label='Convergent region')
    ax.set_xlabel('s')
    ax.set_ylabel('Tr_zeta(D^-s) (d_n weight)')
    ax.set_title('Zeta function s-dependence')
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: w_0 sensitivity to beta and Vol
    ax = axes[1, 0]
    beta_scan = np.linspace(beta_central * 0.5, beta_central * 2.0, 31)
    w0_scan_beta = [compute_w0_from_kms(evals_L7, dims_L7, b, s=S_EVAL, weight_pow=1)["w_0"]
                    for b in beta_scan]
    ax.plot(beta_scan, w0_scan_beta, 'b-', linewidth=2)
    ax.axvline(beta_central, color='r', linestyle='--', label=f'beta_canonical = {beta_central:.2f}')
    ax.axhline(w0_central, color='g', linestyle='--', label=f'w_0 central = {w0_central:+.4f}')
    ax.axhline(-0.918, color='orange', linestyle=':', label='S66 Volovik = -0.918')
    ax.axhline(-0.752, color='purple', linestyle=':', label='DESI DR2 = -0.752')
    ax.fill_between(beta_scan, -0.925, -0.910, alpha=0.15, color='green', label='PASS range')
    ax.set_xlabel('beta (M_KK^-1)')
    ax.set_ylabel('w_0')
    ax.set_title(f'w_0 sensitivity to beta_GGE (Vol fixed)')
    ax.legend(loc='best', fontsize=7)
    ax.grid(alpha=0.3)

    # Panel D: w_0 sensitivity to Vol (via eigenvalue rescaling)
    ax = axes[1, 1]
    V_scan = np.linspace(0.5, 2.0, 31)  # V/V_0
    w0_scan_V = []
    for vfrac in V_scan:
        # lambda_eff = lambda_0 * vfrac^{-1/8}
        evs_scaled = evals_L7 * vfrac**(-1.0/D_DIM)
        w0_scan_V.append(compute_w0_from_kms(evs_scaled, dims_L7, beta_central, s=S_EVAL, weight_pow=1)["w_0"])
    ax.plot(V_scan, w0_scan_V, 'b-', linewidth=2)
    ax.axvline(1.0, color='r', linestyle='--', label=f'V_0 (tau_fold)')
    ax.axhline(w0_central, color='g', linestyle='--', label=f'w_0 central = {w0_central:+.4f}')
    ax.axhline(-0.918, color='orange', linestyle=':', label='S66 Volovik = -0.918')
    ax.axhline(-0.752, color='purple', linestyle=':', label='DESI DR2 = -0.752')
    ax.fill_between(V_scan, -0.925, -0.910, alpha=0.15, color='green', label='PASS range')
    ax.set_xlabel('Vol / Vol_0')
    ax.set_ylabel('w_0')
    ax.set_title(f'w_0 sensitivity to Vol(SU(3)) (beta fixed)')
    ax.legend(loc='best', fontsize=7)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"S74 W0-ZETA-74: w_0 = {w0_central:+.5f} +/- {delta_w0_total:.5f}  "
        f"(gate {verdict}, d_n weight, beta=1/omega_L1)",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"Plot saved to: {OUT_PNG}")

    print(f"\nTotal runtime: {time.time() - t0:.2f}s")
    print(f"Gate W0-ZETA-74: {verdict}")
    return verdict, w0_central, delta_w0_total


if __name__ == "__main__":
    main()
