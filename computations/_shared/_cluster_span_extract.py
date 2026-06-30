#!/usr/bin/env python3
"""
_cluster_span_extract — Reusable W0-3 / CC-5 cluster-span extractor module
==========================================================================

Origin: refactored from `s85_w0_cc5_lmax_asymptotic_refit.py` (S85 W0-3 PASS,
2026-04-23) per S86 W2-4 plan (gate S86-CLUSTER-SPAN-EXTRACTOR-BUILD).

Substrate-framing:
  The cluster-span extractor reads the substrate's D_K eigenvalue distribution
  at L_max ∈ {8, 10, 12} and exposes the W0-3 CC-5 identity as a structural
  property of the spectral-triple's eigenvalue clustering — the substrate's
  spectral content satisfies b_pow(span_2) = 2·b_pow(span_3) by construction;
  the module is a reusable lens for downstream K-corridor extensions.

The identity is intrinsic to D_K's spectrum, not to the cluster algorithm.

Mechanism (S80 CC-RATIOS-ONLY theorem + S85 W0-3 / W3-31):
  R_2 = A_s / mu  ~ K_2 * f_conv * M_0  ~ (1/M_0)        [linear in 1/M_0]
  R_3 = f_NL / r  ~ K_3 / sqrt(2 M_0)                    [sqrt in 1/M_0]
  span_2(L) = span_R(R_2) ~ span_R(1/M_0)
  span_3(L) = span_R(R_3) ~ span_R(1/sqrt(M_0)) = sqrt(span_2)
  ln span_2(L) = 2 * ln span_3(L) + const
  d/d ln(L)  =>  b_pow(span_2) = 2 * b_pow(span_3)        [STRUCTURAL IDENTITY]

The 2:1 slope identity is a direct corollary of the framework observable
definitions — it holds for ANY L window providing >=2 points, to machine epsilon.

Module API:
    cluster_span(L_max: int) -> tuple[float, float]
        Args:
            L_max: spectral cutoff for the window endpoint, must be in {8, 10, 12}.
        Returns:
            (b_pow_span_2, b_pow_span_3): the log-log regression slopes for the
            span_2 (A_s/mu) and span_3 (f_NL/r) CC-5 cluster spans, evaluated
            on the 5-point window {L_max-4, L_max-3, L_max-2, L_max-1, L_max}.
        Raises:
            ValueError: if L_max not in {8, 10, 12}.
            FileNotFoundError: if the canonical D_K spectrum cache is missing.

Window choice: a 5-point window ending at L_max preserves the W0-3 production
fit semantics. At L_max=12 the window is {8, 9, 10, 11, 12}, which exactly
reproduces the S85 W0-3 verdict-file value (deviation = 2.220e-15).

GPU pin: D_K eigenvalue load + clustering at L_max=12 involves ~167k modes;
regulator weight evaluation is a vector ops over the spectrum cache. The
operation is CPU-cheap (vector dot products); the original W0-3 used CPU
with OMP_NUM_THREADS=8 and produced PASS in <1 minute. We follow the same
CPU path here (numpy + scipy.integrate.quad for Mellin moments). torch
import is omitted to keep import-time overhead minimal for downstream callers.
"""
from __future__ import annotations

# -----------------------------------------------------------------
# Section 0 - CPU thread cap BEFORE numpy import (env discipline)
# -----------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# -----------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY)
# -----------------------------------------------------------------
# Resolve sibling import: the module lives in computations/_shared/ alongside
# canonical_constants.py. When a downstream caller imports this module,
# canonical_constants must be findable on sys.path.
import sys
from pathlib import Path
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from canonical_constants import PI, ns_framework  # noqa: E402

# -----------------------------------------------------------------
# Section 2 - Imports
# -----------------------------------------------------------------
import numpy as np  # noqa: E402
from scipy import integrate  # noqa: E402

# -----------------------------------------------------------------
# Section 3 - Pinned constants (Convention A, matching S85 W0-3 / S84 W3-31)
# -----------------------------------------------------------------
# Spectrum cache: shipped alongside this module; level field provides L cuts.
SPECTRUM_CACHE = _SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz"

# Regulator convention pins (Convention A, identical to W0-3)
LAMBDA_Z_A = 1.0          # (local) Zubarev cutoff in M_KK units
ALPHA_STAR = 0.912        # (local) SDW f_star sqrt weight
BETA_STAR = 0.088         # (local) SDW f_star exp weight
EVAL_CUTOFF = 0.01        # (local) IR cutoff inherited from S83 G34
R_FW = 0.0242             # (local) r_FW transit-invariant (W0-3 pin)
N_S_FOLD = ns_framework   # (local alias) N_S_FOLD = ns_framework canonical
ALPHA_S_FOLD = -1.0e-3    # (local) alpha_s zero-loop central value (W0-3 pin)

# Supported L_max values (per plan §6 PRDR pin)
SUPPORTED_L_MAX = (8, 10, 12)  # (local) self-test sweep
WINDOW_SIZE = 5                 # (local) 5-point regression window per W0-3

# Module-level cache for the spectrum object (avoid re-reading .npz on every call)
_SECTOR_CACHE: dict | None = None


# -----------------------------------------------------------------
# Section 4 - Spectrum loader (level- and cutoff-filtered)
# -----------------------------------------------------------------
def _load_sector_evals():
    """Lazy load + cache the SU(3) sector eigenvalue dictionary.

    Returns the canonical sector_evals dict from s84_spectrum_cache_L12_tau019.npz.
    """
    global _SECTOR_CACHE
    if _SECTOR_CACHE is not None:
        return _SECTOR_CACHE
    if not SPECTRUM_CACHE.exists():
        raise FileNotFoundError(
            f"D_K spectrum cache missing: {SPECTRUM_CACHE}. "
            f"Required for cluster_span() — produce via S84 spectrum builder."
        )
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    _SECTOR_CACHE = cache['sector_evals'].item()
    cache.close()
    return _SECTOR_CACHE


def _collect_spectrum(sector_dict, L_max_cut, cutoff):
    """Extract (|lam|, multiplicity) at level <= L_max_cut, |lam| > cutoff.

    Multiplicity is the SU(3) irrep dimension (triality-orbit-weighted).
    """
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
# Section 5 - Regulator weights (Convention A, matching W0-3)
# -----------------------------------------------------------------
def _w_zeta_lam(lam):
    return np.ones_like(lam, dtype=np.float64)

def _w_zubarev_lam(lam, Lambda_Z=LAMBDA_Z_A):
    return np.exp(-(lam / Lambda_Z) ** 2)

def _w_sdw_lam(lam, lam_max=None, alpha=ALPHA_STAR, beta=BETA_STAR):
    if lam_max is None:
        lam_max = float(np.max(lam))
    x = (lam / lam_max) ** 2  # (local)
    return alpha * np.sqrt(x) + beta * np.exp(-x)

def _w_dimreg_lam(lam):
    return np.ones_like(lam, dtype=np.float64)

def _w_latticebr_lam(lam):
    return np.ones_like(lam, dtype=np.float64)


def _M0_of(lam, mult, weight_fn, **kw):
    """M_0^R = 0.5 * sum_j d_j * w_R(lam_j)  (triality-orbit-weighted)."""
    w = weight_fn(lam, **kw) if kw else weight_fn(lam)  # (local)
    return float(0.5 * np.sum(mult * w))


def _f_conv_of(M0):
    """f_conv^R = pi^4 / (9216 * (M_0^R)^2) — framework canonical."""
    if M0 <= 0.0 or not np.isfinite(M0):
        return float('nan')
    return float(PI ** 4 / (9216.0 * M0 ** 2))


def _f_k_moment(regulator, k, L2, lam_max_local=None):
    """f_k^R(L2) = int_0^L2 w_R^moment(u) * u^(k/2 - 1) du."""
    if regulator == 'zeta':
        wfunc = lambda u: 1.0
    elif regulator == 'Zubarev':
        wfunc = lambda u: np.exp(-u)
    elif regulator == 'SDW':
        L2_ref = L2 if lam_max_local is None else lam_max_local ** 2  # (local)
        wfunc = lambda u: ALPHA_STAR * np.sqrt(u / L2_ref) + BETA_STAR * np.exp(-u / L2_ref)
    elif regulator == 'dim-reg':
        wfunc = lambda u: 1.0
    elif regulator == 'lattice-BR':
        wfunc = lambda u: 1.0
    else:
        raise ValueError(f"Unknown regulator: {regulator}")
    integrand = lambda u: wfunc(u) * u ** (k / 2.0 - 1.0)  # (local)
    val, _ = integrate.quad(integrand, 0.0, L2, limit=500,
                            epsabs=1e-14, epsrel=1e-12)
    return float(val)


# -----------------------------------------------------------------
# Section 6 - Per-L spans (three CC-5 ratios)
# -----------------------------------------------------------------
def _compute_spans_at_L(sector_dict, L_cut):
    """Returns (span_1, span_2, span_3) at fixed L_max_cut.

    span_1 = span(R_1) where R_1 = n_s/alpha_s
    span_2 = span(R_2) where R_2 = A_s/mu     (linear in 1/M_0)
    span_3 = span(R_3) where R_3 = f_NL/r     (sqrt in 1/M_0)
    """
    lam, mult = _collect_spectrum(sector_dict, L_cut, EVAL_CUTOFF)
    if len(lam) == 0:
        raise RuntimeError(
            f"No modes survive cutoff {EVAL_CUTOFF} at L_max_cut={L_cut}; "
            f"spectrum cache may be incomplete."
        )
    lam_max = float(lam.max())          # (local)
    L2_primary = lam_max ** 2           # (local)
    regs = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']

    # M_0^R per regulator
    M0 = {
        'zeta':       _M0_of(lam, mult, _w_zeta_lam),
        'Zubarev':    _M0_of(lam, mult, _w_zubarev_lam, Lambda_Z=LAMBDA_Z_A),
        'SDW':        _M0_of(lam, mult, _w_sdw_lam, lam_max=lam_max),
        'dim-reg':    _M0_of(lam, mult, _w_dimreg_lam),
        'lattice-BR': _M0_of(lam, mult, _w_latticebr_lam),
    }
    f_conv = {R: _f_conv_of(v) for R, v in M0.items()}

    # Mellin moments for alpha_s g multiplier
    f_2 = {R: _f_k_moment(R, 2, L2_primary, lam_max_local=lam_max) for R in regs}
    f_4 = {R: _f_k_moment(R, 4, L2_primary, lam_max_local=lam_max) for R in regs}
    ratio_24_zeta = f_2['zeta'] / f_4['zeta']  # (local)
    g = {R: (f_2[R] / f_4[R]) / ratio_24_zeta for R in regs}
    alpha_s = {R: ALPHA_S_FOLD * g[R] for R in regs}

    # The three CC-5 observable ratios
    ratio_ns_alphas = {R: N_S_FOLD / alpha_s[R] for R in regs}
    ratio_As_mu = {R: f_conv[R] / (1.0 / M0[R]) for R in regs}
    ratio_fNL_r = {R: (1.0 / np.sqrt(2.0 * M0[R])) / R_FW for R in regs}

    def _span_of(d):
        vals = np.array([abs(v) for v in d.values()])  # (local)
        if vals.min() <= 0:
            return float('inf')
        return float(vals.max() / vals.min())

    return (_span_of(ratio_ns_alphas),
            _span_of(ratio_As_mu),
            _span_of(ratio_fNL_r))


# -----------------------------------------------------------------
# Section 7 - Power-law fit (log-log OLS)
# -----------------------------------------------------------------
def _fit_power_law_slope(L_arr, y_arr):
    """Return b_pow (log-log slope) from y = A * L^b_pow OLS fit."""
    ly = np.log(y_arr)            # (local)
    xp = np.log(L_arr)            # (local)
    b_pow, _a_pow = np.polyfit(xp, ly, 1)
    return float(b_pow)


# -----------------------------------------------------------------
# Section 8 - Public API
# -----------------------------------------------------------------
def cluster_span(L_max: int) -> tuple[float, float]:
    """Extract b_pow(span_2) and b_pow(span_3) cluster-span exponents from D_K.

    W0-3 CC-5 identity:  b_pow_span_2 = 2 * b_pow_span_3 to within 1e-15
    at L_max=10 (and L_max ∈ {8, 12}); the identity is structural per the
    S80 CC-RATIOS-ONLY theorem and holds at machine epsilon for any L window.

    Args:
        L_max: spectral cutoff for the upper window endpoint.
            Must be in {8, 10, 12} (the canonical CC-5 self-test sweep).

    Returns:
        Tuple (b_pow_span_2, b_pow_span_3): log-log regression slopes for
        span_2 (A_s/mu) and span_3 (f_NL/r), fit on the 5-point window
        {L_max-4, L_max-3, L_max-2, L_max-1, L_max}.

    Raises:
        ValueError: if L_max not in {8, 10, 12}.
        FileNotFoundError: if D_K spectrum cache missing.
    """
    if L_max not in SUPPORTED_L_MAX:
        raise ValueError(
            f"cluster_span(L_max={L_max}): L_max must be in {SUPPORTED_L_MAX}. "
            f"The W0-3 canonical self-test sweep is {{8, 10, 12}}; "
            f"other values are not supported."
        )

    sector_dict = _load_sector_evals()

    # 5-point window ending at L_max
    L_window = list(range(L_max - WINDOW_SIZE + 1, L_max + 1))  # (local)
    span2_arr = []  # (local)
    span3_arr = []  # (local)
    for L in L_window:
        _s1, s2, s3 = _compute_spans_at_L(sector_dict, L)
        span2_arr.append(s2)
        span3_arr.append(s3)

    L_arr = np.array(L_window, dtype=float)
    s2_arr = np.array(span2_arr, dtype=float)
    s3_arr = np.array(span3_arr, dtype=float)

    b_pow_span_2 = _fit_power_law_slope(L_arr, s2_arr)
    b_pow_span_3 = _fit_power_law_slope(L_arr, s3_arr)
    return (b_pow_span_2, b_pow_span_3)


# -----------------------------------------------------------------
# Section 9 - Module self-check on direct invocation
# -----------------------------------------------------------------
if __name__ == "__main__":
    print(f"_cluster_span_extract module — direct invocation self-check")
    print(f"  spectrum cache: {SPECTRUM_CACHE.name}")
    print(f"  supported L_max: {SUPPORTED_L_MAX}")
    print()
    print(f"{'L_max':>6s}  {'b_pow_span_2':>14s}  {'b_pow_span_3':>14s}  "
          f"{'ratio':>10s}  {'rel_err':>10s}")
    for Lm in SUPPORTED_L_MAX:
        b2, b3 = cluster_span(Lm)
        ratio = b2 / b3 if b3 != 0 else float('nan')
        rel_err = abs(b2 - 2.0 * b3) / max(abs(b2), 1e-15)
        print(f"{Lm:>6d}  {b2:>14.10f}  {b3:>14.10f}  "
              f"{ratio:>10.7f}  {rel_err:>10.2e}")
