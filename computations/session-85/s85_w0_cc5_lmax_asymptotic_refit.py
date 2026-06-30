#!/usr/bin/env python3
"""
S85 W0-3 — CC-5-LMAX-ASYMPTOTIC-REFIT  [VERIFY-THEOREM]
=======================================================

Gate: S85-CC-5-LMAX-ASYMPTOTIC-REFIT
Classification: GEOMETRIC (triality-orbit-weighted moments of D_K)
Owner: connes-ncg-theorist

Pre-registration (session-85-plan-w0.md §W0-3, patched 2026-04-23):
  HYPOTHESIS: Extending the W3-31 span series from L in {3,5,7,9} to
  L in {8,9,10,11,12} preserves the structural identity
        b_pow(span_2) / b_pow(span_3) = 2.000
  to within 1e-3, with R^2 >= 0.99 per series and monotonic
  convergence of individual b_pow across L in {8..12}.

  PASS: |ratio - 2.000| <= 1e-3 AND R^2 >= 0.99 (all 3 series) AND
        b_pow monotone convergent on L in {8..12} (drift < 5% from
        L=10 to L=12).
  INFO: 1e-3 < |ratio - 2.000| <= 1e-2.
  FAIL: |ratio - 2.000| > 1e-2 OR R^2 < 0.99 on any series OR
        non-monotone.

4-tuple slot: (value=|b_pow(span_2)/b_pow(span_3) - 2.000|,
               scheme=triality-orbit-cluster,
               convention=multiplicative, L_max=12)

SUBSTITUTION CHAIN [VERIFY-THEOREM] (see WP sec VI):

  Step 1. Definitions.
     (i)   span_k(L) is the cluster-span of the kth CC-5 ratio observable
           evaluated across the 5-regulator set {zeta, Zubarev, SDW,
           dim-reg, lattice-BR} at Jensen parameter tau_fold and
           cutoff L_max = L:
              span_k(L) := max_R R_k^R(L) / min_R R_k^R(L)
           where R_1 = n_s/alpha_s, R_2 = A_s/mu, R_3 = f_NL/r.
     (ii)  b_pow_k is the log-log regression slope of span_k(L) on L:
              ln span_k(L) = a_k + b_pow_k * ln L + eps.
     (iii) The structural identity to verify:
              b_pow(span_2) / b_pow(span_3) = 2.000
           (W3-31 machine-precision finding at L in {3,5,7,9};
           extended here to L in {8..12}).

  Step 2. Mechanism for the 2:1 ratio.
     From the CC-RATIOS-ONLY theorem (S80 W1-4):
         A_s^R ~ f_conv^R  (linear in f_conv = pi^4/(9216 M_0^2))
         mu^R  ~ 1/M_0^R   (linear in 1/M_0)
         f_NL^R ~ 1/sqrt(2 M_0^R)  (sqrt in 1/M_0)
         r^R   = r_FW  (transit-invariant, R-independent)
     Therefore:
         R_2 = A_s/mu    = K_2 * f_conv * M_0 = K_2 * pi^4/(9216 M_0)
         R_3 = f_NL/r    = K_3 / sqrt(2 M_0)
     Cluster spans:
         span_2(L) = span_R(1/M_0^R)                    (linear in 1/M_0)
         span_3(L) = span_R(1/sqrt(M_0^R)) = sqrt(span_R(1/M_0))
                   = sqrt(span_2)
     Taking logs:
         ln span_2 = 2 * ln span_3
     Taking d/d ln L (regression slope in log-L):
         d ln span_2 / d ln L = 2 * (d ln span_3 / d ln L)
         b_pow(span_2) = 2 * b_pow(span_3)
     So the 2:1 ratio is the spectral-triple signature of the
     power-counting difference (linear vs sqrt) in the A_s/mu
     and f_NL/r observables under M_0^R cluster variation.

  Step 3. Simplification.
     The structural ratio b_pow(span_2)/b_pow(span_3) = 2.000 is
     an IDENTITY (not a fit value): it holds for ANY data obeying
     ln(span_2) = 2*ln(span_3) + const, regardless of the
     individual b_pow values or the M_0^R dependence on L.
     The identity is a direct corollary of the framework
     observable definitions plus the S80 CC-RATIOS-ONLY theorem.

  Step 4. Direction.
     PASS at 1e-3 tolerance means: the extension to L in {8..12}
     preserves the W3-31 identity to full machine precision, up
     to floating-point arithmetic in the least-squares regression.
     Non-trivial content: the identity must hold across the
     extended L range even as individual b_pow values drift
     (they do: b_pow(span_2) at L in {3..9} = 3.826 vs b_pow at
     L in {8..12} = 6.564). The RATIO is invariant; the
     individual powers are not.

L_max scan: {8, 9, 10, 11, 12} per plan PRDR pin.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s84_spectrum_cache_L12_tau019.npz   (D_K spectrum at tau_fold, L<=12)
  - this script
  - s84_w3_cc5_l_max_asymptotic.py      (W3-31 producing script, ref sha
                                         06ffd14b...178d30 per plan)

Output 4-tuple:
  (value=|b_pow(span_2)/b_pow(span_3) - 2.000|,
   scheme=triality-orbit-cluster, convention=multiplicative, L_max=12)
"""
from __future__ import annotations

# -----------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import PI, M_KK, tau_fold, ns_framework

# -----------------------------------------------------------------
# Section 2 - Standard imports
# CPU path for the regulator weight integrals (scalar scipy.quad);
# M_0 evaluation is a vector dot product over the spectrum cache
# (16k-167k modes at L in {8..12}) and is already CPU-cheap.
# -----------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -----------------------------------------------------------------
# Section 3 - Paths + pre-registration constants
# -----------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S85"                                                    # (local)
GATE_ID = "S85-CC-5-LMAX-ASYMPTOTIC-REFIT"                         # (local)
SCHEME = "triality-orbit-cluster"                                  # (local)
CONVENTION = "multiplicative"                                      # (local)
L_MAX_PRIMARY = 12                                                 # (local) L_max slot in 4-tuple
L_MAX_SCAN = [8, 9, 10, 11, 12]                                    # (local) per PRDR pin
L_MAX_BASELINE = [3, 5, 7, 9]                                      # (local) for W3-31 reproduction sanity

OUT_NPZ = SCRIPT_DIR / "s85_w0_cc5_lmax_asymptotic_refit.npz"
OUT_PNG = SCRIPT_DIR / "s85_w0_cc5_lmax_asymptotic_refit.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"

SPECTRUM_CACHE = SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)
W3_31_SCRIPT = SCRIPT_DIR / "s84_w3_cc5_l_max_asymptotic.py"       # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s85_w0_cc5_lmax_asymptotic_refit.py",
    W3_31_SCRIPT,
]

# Pre-registered gate thresholds (plan §W0-3)
IDENTITY_TARGET = 2.000                                            # (local)
PASS_TOL = 1e-3                                                    # (local) RATIO tol
FAIL_TOL = 1e-2                                                    # (local) RATIO tol
R2_MIN = 0.99                                                      # (local)
MONOTONE_DRIFT_MAX = 0.05                                          # (local) 5% drift L=10->L=12

# Regulator convention pins (Convention A, matching S83 G34 / S84 W3-31)
LAMBDA_Z_A = 1.0                                                   # (local) M_KK units
ALPHA_STAR = 0.912                                                 # (local) SDW f_star sqrt weight
BETA_STAR = 0.088                                                  # (local) SDW f_star exp weight
EVAL_CUTOFF = 0.01                                                 # (local) IR cutoff, inherited G34
R_FW = 0.0242                                                      # (local) r_FW, transit-invariant
N_S_FOLD = ns_framework                                            # (local alias) = 0.9595
ALPHA_S_FOLD = -1.0e-3                                             # (local) framework alpha_s zero-loop central


# -----------------------------------------------------------------
# Section 4 - SHA-256 input pins + closure hash
# -----------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}               # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha}")
        pins[rel] = sha
    return pins


def closure_hash(pins_dict):
    items = sorted(pins_dict.items())   # (local)
    h = hashlib.sha256()                # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------
# Section 5 - Spectrum loader (triality-orbit-cluster filter)
#  Modes are kept if level <= L_max_cut AND |lam| > cutoff.
#  Multiplicity is the SU(3) irrep dim (triality-orbit-weighted).
# -----------------------------------------------------------------
def collect_spectrum(sector_dict, L_max_cut, cutoff):
    abs_list = []   # (local)
    mult_list = []  # (local)
    for _k, data in sorted(sector_dict.items()):
        if data['level'] <= L_max_cut:
            dim = int(data['dim'])  # (local) SU(3) irrep dimension
            for ev in data['abs_evals']:
                a = float(ev)       # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# -----------------------------------------------------------------
# Section 6 - Regulator weights (Convention A, matching G34 / W3-31)
#  Lam-level (for M_0 assembly) and Mellin-variable (for f_k moments).
# -----------------------------------------------------------------
def w_zeta_lam(lam):
    return np.ones_like(lam, dtype=np.float64)

def w_Zubarev_lam(lam, Lambda_Z=LAMBDA_Z_A):
    return np.exp(-(lam / Lambda_Z) ** 2)

def w_SDW_lam(lam, lam_max=None, alpha=ALPHA_STAR, beta=BETA_STAR):
    if lam_max is None:
        lam_max = float(np.max(lam))
    x = (lam / lam_max) ** 2     # (local)
    return alpha * np.sqrt(x) + beta * np.exp(-x)

def w_dimreg_lam(lam):
    return np.ones_like(lam, dtype=np.float64)

def w_latticeBR_lam(lam):
    return np.ones_like(lam, dtype=np.float64)


def M0_of(lam, mult, weight_fn, **kw):
    """M_0^R = 0.5 * sum_j d_j * w_R(lam_j)  (triality-orbit-weighted)."""
    w = weight_fn(lam, **kw) if kw else weight_fn(lam)   # (local)
    return float(0.5 * np.sum(mult * w))


def f_conv_of(M0):
    """f_conv^R = pi^4 / (9216 * (M_0^R)^2)  (framework canonical)."""
    if M0 <= 0.0 or not np.isfinite(M0):
        return float('nan')
    return float(PI ** 4 / (9216.0 * M0 ** 2))


def f_k_moment(regulator, k, L2, lam_max_local=None):
    """f_k^R(L2) = int_0^L2 w_R^moment(u) * u^(k/2 - 1) du."""
    if regulator == 'zeta':
        wfunc = lambda u: 1.0
    elif regulator == 'Zubarev':
        wfunc = lambda u: np.exp(-u)
    elif regulator == 'SDW':
        L2_ref = L2 if lam_max_local is None else lam_max_local ** 2   # (local)
        wfunc = lambda u: ALPHA_STAR * np.sqrt(u / L2_ref) + BETA_STAR * np.exp(-u / L2_ref)
    elif regulator == 'dim-reg':
        wfunc = lambda u: 1.0
    elif regulator == 'lattice-BR':
        wfunc = lambda u: 1.0
    else:
        raise ValueError(f"Unknown regulator: {regulator}")
    integrand = lambda u: wfunc(u) * u ** (k / 2.0 - 1.0)            # (local)
    val, _ = integrate.quad(integrand, 0.0, L2, limit=500,
                            epsabs=1e-14, epsrel=1e-12)
    return float(val)


# -----------------------------------------------------------------
# Section 7 - Per-L span computation (three CC-5 ratios)
# -----------------------------------------------------------------
def compute_spans_at_L(lam, mult):
    """
    Given (|lam|, mult) arrays at fixed L_max, return the three CC-5
    cluster spans and the per-regulator intermediate quantities.
    """
    lam_max = float(lam.max())      # (local)
    L2_primary = lam_max ** 2       # (local)
    regs = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']

    # M_0^R per regulator
    M0 = {
        'zeta':       M0_of(lam, mult, w_zeta_lam),
        'Zubarev':    M0_of(lam, mult, w_Zubarev_lam, Lambda_Z=LAMBDA_Z_A),
        'SDW':        M0_of(lam, mult, w_SDW_lam, lam_max=lam_max),
        'dim-reg':    M0_of(lam, mult, w_dimreg_lam),
        'lattice-BR': M0_of(lam, mult, w_latticeBR_lam),
    }
    f_conv = {R: f_conv_of(v) for R, v in M0.items()}

    # Mellin moments
    f_2 = {R: f_k_moment(R, 2, L2_primary, lam_max_local=lam_max)
           for R in regs}
    f_4 = {R: f_k_moment(R, 4, L2_primary, lam_max_local=lam_max)
           for R in regs}

    # g^R multiplier for alpha_s (normalized g^zeta = 1)
    ratio_24_zeta = f_2['zeta'] / f_4['zeta']           # (local)
    g = {R: (f_2[R] / f_4[R]) / ratio_24_zeta for R in regs}
    alpha_s = {R: ALPHA_S_FOLD * g[R] for R in regs}

    # The three CC-5 observable ratios
    # Ratio 1: n_s / alpha_s (UNBALANCED Mellin)
    ratio_ns_alphas = {R: N_S_FOLD / alpha_s[R] for R in regs}
    # Ratio 2: A_s / mu    (A_s linear in f_conv, mu ~ 1/M_0)
    #   -> ratio ~ f_conv * M_0 = (pi^4/9216) * (1/M_0)
    ratio_As_mu = {R: f_conv[R] / (1.0 / M0[R]) for R in regs}
    # Ratio 3: f_NL / r    (f_NL ~ 1/sqrt(2 M_0), r R-invariant)
    ratio_fNL_r = {R: (1.0 / np.sqrt(2.0 * M0[R])) / R_FW for R in regs}

    def span_of(d):
        vals = np.array([abs(v) for v in d.values()])   # (local)
        if vals.min() <= 0:
            return float('inf')
        return float(vals.max() / vals.min())

    span_1 = span_of(ratio_ns_alphas)
    span_2 = span_of(ratio_As_mu)
    span_3 = span_of(ratio_fNL_r)
    return dict(
        lam_max=lam_max,
        n_modes=len(lam),
        M0=M0, f_conv=f_conv, f_2=f_2, f_4=f_4, g=g,
        ratio_ns_alphas=ratio_ns_alphas,
        ratio_As_mu=ratio_As_mu,
        ratio_fNL_r=ratio_fNL_r,
        span_1=span_1, span_2=span_2, span_3=span_3,
    )


# -----------------------------------------------------------------
# Section 8 - Power-law fitting with R^2 reporting
# -----------------------------------------------------------------
def fit_power_law(L_arr, y_arr):
    """Fit y = A * L^b_pow on log-log scale via OLS; return fit dict."""
    ly = np.log(y_arr)                  # (local)
    xp = np.log(L_arr)                  # (local)
    b_pow, a_pow = np.polyfit(xp, ly, 1)
    ly_hat = a_pow + b_pow * xp         # (local)
    ss_res = np.sum((ly - ly_hat) ** 2) # (local)
    ss_tot = np.sum((ly - np.mean(ly)) ** 2)  # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float('nan')  # (local)
    return dict(b_pow=float(b_pow), a_pow=float(a_pow),
                R2=float(R2))


def windowed_bpow(L_arr, y_arr, window=3):
    """Rolling 3-point b_pow windows across L_arr for convergence trace."""
    L_arr = np.asarray(L_arr, dtype=float)
    y_arr = np.asarray(y_arr, dtype=float)
    out = []   # (local)
    for i in range(len(L_arr) - window + 1):
        fit = fit_power_law(L_arr[i:i+window], y_arr[i:i+window])
        out.append((float(L_arr[i]), float(L_arr[i+window-1]),
                    fit['b_pow']))
    return out


# -----------------------------------------------------------------
# Section 9 - Main
# -----------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # Step 1: input pins + closure
    pins = log_input_pins(INPUT_FILES)
    closure_content_precompute = closure_hash(pins)
    print(f"  content-precompute closure: {closure_content_precompute}")
    print()

    # Step 2: Load D_K spectrum at L<=12
    if not SPECTRUM_CACHE.exists():
        print(f"SPECTRUM CACHE MISSING: {SPECTRUM_CACHE}")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()
    print(f"Loaded spectrum cache L<=12, n_sectors = {len(sector_evals)}")
    print()

    # Step 3: Compute spans at L in {3,5,7,9} (baseline sanity) and
    # L in {8,9,10,11,12} (production scan). Produces the asymptotic
    # series for the power-law regression.
    print("=" * 72)
    print("PER-L CC-5 CLUSTER SPANS")
    print("=" * 72)
    scan_results = {}   # (local)
    all_L = sorted(set(L_MAX_BASELINE + L_MAX_SCAN))
    print(f"{'L':>3s}  {'n_modes':>8s}  {'lam_max':>8s}  "
          f"{'span_1':>10s}  {'span_2':>12s}  {'span_3':>10s}")
    for L in all_L:
        lam, mult = collect_spectrum(sector_evals, L, EVAL_CUTOFF)
        res = compute_spans_at_L(lam, mult)
        scan_results[L] = res
        print(f"{L:>3d}  {res['n_modes']:>8d}  {res['lam_max']:>8.4f}  "
              f"{res['span_1']:>10.4f}  {res['span_2']:>12.4f}  "
              f"{res['span_3']:>10.4f}")
    print()

    # Step 4: Sanity check - reproduce W3-31 fit at L in {3,5,7,9}.
    # S84 W3-31 reported b_pow(span_2)=3.8262, b_pow(span_3)=1.9131,
    # ratio 2.0001 to 0.1%. We should reproduce that to 4 sig figs.
    L_bl = np.array(L_MAX_BASELINE, dtype=float)
    s1_bl = np.array([scan_results[L]['span_1'] for L in L_MAX_BASELINE])
    s2_bl = np.array([scan_results[L]['span_2'] for L in L_MAX_BASELINE])
    s3_bl = np.array([scan_results[L]['span_3'] for L in L_MAX_BASELINE])
    f1_bl = fit_power_law(L_bl, s1_bl)
    f2_bl = fit_power_law(L_bl, s2_bl)
    f3_bl = fit_power_law(L_bl, s3_bl)
    print("BASELINE SANITY (L in {3,5,7,9}, reproducing W3-31):")
    print(f"  b_pow(span_1)={f1_bl['b_pow']:.4f}  R2={f1_bl['R2']:.6f}  "
          f"[W3-31: 1.2738]")
    print(f"  b_pow(span_2)={f2_bl['b_pow']:.4f}  R2={f2_bl['R2']:.6f}  "
          f"[W3-31: 3.8262]")
    print(f"  b_pow(span_3)={f3_bl['b_pow']:.4f}  R2={f3_bl['R2']:.6f}  "
          f"[W3-31: 1.9131]")
    bl_ratio = f2_bl['b_pow'] / f3_bl['b_pow']
    bl_ratio_dev = abs(bl_ratio - IDENTITY_TARGET)
    print(f"  baseline identity ratio = {bl_ratio:.6f}  "
          f"|ratio - 2.000| = {bl_ratio_dev:.2e}")
    print()

    # Step 5: Primary fit - power-law on L in {8,9,10,11,12}.
    L_prod = np.array(L_MAX_SCAN, dtype=float)
    s1_prod = np.array([scan_results[L]['span_1'] for L in L_MAX_SCAN])
    s2_prod = np.array([scan_results[L]['span_2'] for L in L_MAX_SCAN])
    s3_prod = np.array([scan_results[L]['span_3'] for L in L_MAX_SCAN])

    f1 = fit_power_law(L_prod, s1_prod)
    f2 = fit_power_law(L_prod, s2_prod)
    f3 = fit_power_law(L_prod, s3_prod)

    print("=" * 72)
    print("PRIMARY FIT (L in {8,9,10,11,12}):")
    print("=" * 72)
    print(f"  span_1: b_pow = {f1['b_pow']:.6f}  a_pow = {f1['a_pow']:.6f}  "
          f"R2 = {f1['R2']:.6f}")
    print(f"  span_2: b_pow = {f2['b_pow']:.6f}  a_pow = {f2['a_pow']:.6f}  "
          f"R2 = {f2['R2']:.6f}")
    print(f"  span_3: b_pow = {f3['b_pow']:.6f}  a_pow = {f3['a_pow']:.6f}  "
          f"R2 = {f3['R2']:.6f}")
    print()

    # Structural identity value + tolerance
    ratio_2_3 = f2['b_pow'] / f3['b_pow']
    ratio_deviation = abs(ratio_2_3 - IDENTITY_TARGET)
    print(f"STRUCTURAL IDENTITY:")
    print(f"  b_pow(span_2) / b_pow(span_3) = {ratio_2_3:.10f}")
    print(f"  target                        = {IDENTITY_TARGET:.10f}")
    print(f"  |ratio - 2.000|               = {ratio_deviation:.3e}")
    print()

    # Cross-check: second identity b_pow(span_3)/b_pow(span_1) =? 3/2
    ratio_3_1 = f3['b_pow'] / f1['b_pow']
    target_3_2 = 1.5                         # (local) cross-check anchor (S83 G4 Mellin-linear)
    ratio_3_1_dev = abs(ratio_3_1 - target_3_2)
    print(f"SECOND IDENTITY (cross-check only, not gate-binding):")
    print(f"  b_pow(span_3) / b_pow(span_1) = {ratio_3_1:.6f}  "
          f"target = {target_3_2:.4f}")
    print(f"  |ratio - 1.500|               = {ratio_3_1_dev:.3e}")
    print()

    # Step 6: Monotone-convergence check across rolling 3-pt windows
    #   s_k: windows (8..10), (9..11), (10..12)
    print("MONOTONE-CONVERGENCE TRACE (rolling 3-pt b_pow windows):")
    win1 = windowed_bpow(L_prod, s1_prod, window=3)
    win2 = windowed_bpow(L_prod, s2_prod, window=3)
    win3 = windowed_bpow(L_prod, s3_prod, window=3)

    def check_monotone_convergent(windows):
        """Returns (monotone: bool, drift_frac: float)."""
        b_vals = [b for (_, _, b) in windows]
        dirs = [np.sign(b_vals[i+1] - b_vals[i]) for i in range(len(b_vals)-1)]
        monotone = all(d == dirs[0] and d != 0 for d in dirs)
        drift = abs(b_vals[-1] - b_vals[0]) / abs(b_vals[0])
        return monotone, float(drift)

    m1, drift_1 = check_monotone_convergent(win1)
    m2, drift_2 = check_monotone_convergent(win2)
    m3, drift_3 = check_monotone_convergent(win3)
    for name, wins, mono, drift in [('s1', win1, m1, drift_1),
                                    ('s2', win2, m2, drift_2),
                                    ('s3', win3, m3, drift_3)]:
        print(f"  {name}: ", end="")
        for lo, hi, b in wins:
            print(f"window({int(lo)}..{int(hi)})={b:.4f}  ", end="")
        print(f"monotone={mono}  drift={drift:.4f}")
    print()

    # Step 7: Pre-registered gate evaluation
    R2_all_ok = (f1['R2'] >= R2_MIN and f2['R2'] >= R2_MIN
                 and f3['R2'] >= R2_MIN)
    mono_all_ok = m1 and m2 and m3
    drift_all_ok = (drift_1 < MONOTONE_DRIFT_MAX
                    and drift_2 < MONOTONE_DRIFT_MAX
                    and drift_3 < MONOTONE_DRIFT_MAX)

    print("=" * 72)
    print("GATE EVALUATION")
    print("=" * 72)
    print(f"  |ratio - 2.000|      = {ratio_deviation:.3e}  "
          f"(PASS <= {PASS_TOL:.0e}, FAIL > {FAIL_TOL:.0e})")
    print(f"  R2 >= {R2_MIN:.2f} all series  = {R2_all_ok} "
          f"(s1={f1['R2']:.4f}, s2={f2['R2']:.4f}, s3={f3['R2']:.4f})")
    print(f"  monotone convergent  = {mono_all_ok}  "
          f"(s1={m1}, s2={m2}, s3={m3})")
    print(f"  drift < 5% all series= {drift_all_ok}  "
          f"(s1={drift_1:.2%}, s2={drift_2:.2%}, s3={drift_3:.2%})")

    if (ratio_deviation <= PASS_TOL and R2_all_ok
            and mono_all_ok and drift_all_ok):
        verdict = "PASS"
    elif ratio_deviation > FAIL_TOL or not R2_all_ok or not mono_all_ok:
        verdict = "FAIL"
    else:
        verdict = "INFO"
    print(f"  VERDICT: {verdict}")
    print()

    # Step 8: Save artifacts
    np.savez(
        OUT_NPZ,
        # L grids
        L_max_baseline=np.array(L_MAX_BASELINE),
        L_max_scan=np.array(L_MAX_SCAN),
        all_L=np.array(all_L),
        # Spans per L
        spans_L_all=np.array([[L,
                               scan_results[L]['span_1'],
                               scan_results[L]['span_2'],
                               scan_results[L]['span_3']]
                              for L in all_L]),
        # Per-L intermediates for reproducibility
        n_modes_all=np.array([scan_results[L]['n_modes'] for L in all_L]),
        lam_max_all=np.array([scan_results[L]['lam_max'] for L in all_L]),
        # Primary fit L in {8..12}
        span_1_prod=s1_prod, span_2_prod=s2_prod, span_3_prod=s3_prod,
        fit_span_1=np.array(json.dumps(f1)),
        fit_span_2=np.array(json.dumps(f2)),
        fit_span_3=np.array(json.dumps(f3)),
        # Baseline sanity fit L in {3,5,7,9}
        span_1_baseline=s1_bl, span_2_baseline=s2_bl, span_3_baseline=s3_bl,
        fit_span_1_baseline=np.array(json.dumps(f1_bl)),
        fit_span_2_baseline=np.array(json.dumps(f2_bl)),
        fit_span_3_baseline=np.array(json.dumps(f3_bl)),
        baseline_identity_ratio=bl_ratio,
        baseline_identity_deviation=bl_ratio_dev,
        # Primary identity result
        ratio_2_3=ratio_2_3,
        ratio_deviation=ratio_deviation,
        ratio_3_1_crosscheck=ratio_3_1,
        ratio_3_1_deviation=ratio_3_1_dev,
        # Windowed convergence
        windows_s1=np.array(win1),
        windows_s2=np.array(win2),
        windows_s3=np.array(win3),
        monotone_s1=m1, monotone_s2=m2, monotone_s3=m3,
        drift_s1=drift_1, drift_s2=drift_2, drift_s3=drift_3,
        # Gate
        verdict=verdict,
        # Thresholds
        PASS_TOL=PASS_TOL, FAIL_TOL=FAIL_TOL,
        R2_MIN=R2_MIN, MONOTONE_DRIFT_MAX=MONOTONE_DRIFT_MAX,
        IDENTITY_TARGET=IDENTITY_TARGET,
        # Pins
        pins=np.array(json.dumps(pins)),
    )
    print(f"wrote {OUT_NPZ}")

    # Step 9: Plot log-log scan per series
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    all_L_arr = np.array(all_L, dtype=float)
    for ax, key, title in [
        (axes[0, 0], 'span_1', 'span_1: n_s/alpha_s  (UNBALANCED)'),
        (axes[0, 1], 'span_2', 'span_2: A_s/mu       (linear in 1/M_0)'),
        (axes[1, 0], 'span_3', 'span_3: f_NL/r       (sqrt in 1/M_0)'),
    ]:
        y_all = np.array([scan_results[L][key] for L in all_L])
        ax.loglog(all_L_arr, y_all, 'o', ms=7, color='grey',
                  label='all L {3,5,7,9,8,..,12}', mfc='none')
        y_prod = np.array([scan_results[L][key] for L in L_MAX_SCAN])
        L_prod_arr = np.array(L_MAX_SCAN, dtype=float)
        ax.loglog(L_prod_arr, y_prod, 's', ms=10, color='C0',
                  label='production L {8..12}')
        if key == 'span_1':
            f = f1
        elif key == 'span_2':
            f = f2
        else:
            f = f3
        Lfine = np.linspace(L_prod_arr.min(), L_prod_arr.max(), 100)
        yfit = np.exp(f['a_pow'] + f['b_pow'] * np.log(Lfine))
        ax.loglog(Lfine, yfit, '--', color='C1',
                  label=f"fit: b={f['b_pow']:.4f}, R2={f['R2']:.4f}")
        ax.set_xlabel('L_max')
        ax.set_ylabel(key)
        ax.set_title(title)
        ax.grid(True, which='both', alpha=0.3)
        ax.legend(loc='best', fontsize=8)
    # 4th panel: summary text
    ax4 = axes[1, 1]
    ax4.axis('off')
    summary = [
        f"Gate: {GATE_ID}",
        f"Verdict: {verdict}",
        "",
        f"Primary fit L in {{8..12}}:",
        f"  b_pow(span_1) = {f1['b_pow']:.4f}  R2={f1['R2']:.4f}",
        f"  b_pow(span_2) = {f2['b_pow']:.4f}  R2={f2['R2']:.4f}",
        f"  b_pow(span_3) = {f3['b_pow']:.4f}  R2={f3['R2']:.4f}",
        "",
        f"Structural identity:",
        f"  b_pow(span_2)/b_pow(span_3) = {ratio_2_3:.8f}",
        f"  target                      = {IDENTITY_TARGET:.4f}",
        f"  |ratio - 2.000|             = {ratio_deviation:.2e}",
        f"  PASS tol                    = {PASS_TOL:.0e}",
        "",
        f"Second identity (cross-check):",
        f"  b_pow(span_3)/b_pow(span_1) = {ratio_3_1:.4f}",
        f"  target                      = 1.500",
        "",
        f"Monotone-convergent trace:",
        f"  s1: drift = {drift_1:.2%}, monotone = {m1}",
        f"  s2: drift = {drift_2:.2%}, monotone = {m2}",
        f"  s3: drift = {drift_3:.2%}, monotone = {m3}",
    ]
    ax4.text(0.02, 0.98, "\n".join(summary), va='top', ha='left',
             family='monospace', fontsize=9)
    fig.suptitle("S85 W0-3: CC-5 L_max asymptotic refit (L in {8..12})")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    print(f"wrote {OUT_PNG}")

    # Step 10: Compute the two SHAs
    # content_sha256: SHA-256 of the NPZ file (reproducibility pin)
    content_sha = sha256_of(OUT_NPZ)
    # audit_sha256: SHA-256 of the ordered input-pin map (audit pin)
    audit_sha = closure_hash(pins)
    print(f"\ncontent_sha256 = {content_sha}")
    print(f"audit_sha256   = {audit_sha}")

    # Step 11: Append verdict line
    verdict_line = (f"{GATE_ID}: {verdict} -- "
                    f"value={ratio_deviation:.3e} "
                    f"scheme={SCHEME} "
                    f"convention={CONVENTION} "
                    f"L_max={L_MAX_PRIMARY} "
                    f"sha256={content_sha}")
    comment_line = f"# audit_sha256={audit_sha}"
    print()
    print(f"4-tuple: (value={ratio_deviation:.3e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_PRIMARY})")
    print(verdict_line)
    print(comment_line)

    # Write to canonical computations/_shared/s{N}_gate_verdicts.txt
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(verdict_line + "\n")
        f.write(comment_line + "\n")
    print(f"\nAppended to {VERDICT_TXT}")

    elapsed = time.time() - t0
    print(f"\nelapsed: {elapsed:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
