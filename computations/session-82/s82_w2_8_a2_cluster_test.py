#!/usr/bin/env python3
"""
S82 W2-8: A2-CLUSTER-TEST
========================================================================
Gate: S82-A2-CLUSTER-TEST  [VERIFY]
Classification: GEOMETRIC
Owner: lizzi-spectral-functional-theorist
Write-target: sessions/archive/session-82/session-82-results-workingpaper.md §V.H
Related: W2-5 MP-EXCLUSION landed PASS. f* excluded in continuum limit.
Anchor: sessions/session-plan/session-80-plan.md L1447-L1489 (§W2-8)
P4-C reference: sessions/archive/session-79/workshops/p4-c-w2d-fstar-outside-cluster.md

=== PRE-REGISTRATION (S80 plan §W2-8 VERBATIM) ===

GATE: [VERIFY] S82-A2-CLUSTER-TEST
HYPOTHESIS:
  Per P4-C slot-dependent taxonomy: a_0 cluster is tight via CHK3+CHK4;
  a_2 slot is NOT tight (SDW/anomaly = 2/3 exact + f* outlier).
PRE-REGISTERED:
  Compute intra-cluster variance for a_0 (expected small) vs a_2
  (expected large).
PASS:  a_0 variance < 1% AND a_2 variance > 5%.
INFO:  a_2 variance in [1%, 5%].
FAIL:  a_0 variance > 1% OR a_2 variance < 1% (slot-dependent taxonomy fails).

=== OPERATIONAL DEFINITIONS (Chamseddine-Connes convention) ===

For each regulator kernel f(x), the slot weight at Lambda^2 = lam_max^2:
  f_0^{scheme} := f(0)                          (pointwise at x=0)
  f_2^{scheme} := int_0^{Lambda^2} f(u) du      (integral over Lambda^2 band)

These f_n are the Chamseddine-Connes moments weighting a_n in
  S = sum_n Lambda^(4-n) * f_n * a_n

Intra-cluster variance (per S80 template L1472-L1484):
  var_i = sigma^2({a_i under scheme_j}_j) / <a_i>^2  for i in {0, 2}

where the "a_i cluster" ACROSS schemes uses the scheme-specific slot
weights f_n^{scheme} as the effective a_i sibling-class readout. This
matches the P4-C operational definition (L827-L829):
  sibling_class_a0 = {SDW, zeta, anomaly-sharp} via CHK3+CHK4 identities
  sibling_class_a2 = {SDW} anchor + {anomaly-sharp} at 2/3 algebraic ratio

=== SCHEMES (5, S80 plan §W2-8 verbatim) ===

  SDW        : f(x) = sqrt(x)              (Andrianov-Lizzi heat-kernel)
  anomaly    : f(x) = 1 on [0, Lambda^2]   (sharp cutoff, CC/AL forces f_0=1/2)
  f*         : f(x) = 0.912 sqrt(x) + 0.088 exp(-x)   (S72 empirical fit)
  Gaussian   : f(x) = exp(-x^2)            (classical heat-kernel regulator)
  exp-decay  : f(x) = exp(-x)              (exponential decay)

=== SUBSTITUTION CHAIN — a_0 slot (pointwise) ===

  Step 1 (def): f_0^{scheme} = f(0) (CC Mellin weight for a_0).
  Step 2 (substitute):
           f_0^{SDW}      = sqrt(0) = 0 (formal)
           f_0^{anomaly}  = 1/2 (FORCED by Andrianov-Lizzi arXiv:1103.0478)
           f_0^{f*}       = 0.912*0 + 0.088*1 = 0.088
           f_0^{Gaussian} = exp(0) = 1
           f_0^{exp-decay}= exp(0) = 1
  Step 3 (simplify, variance): sigma^2_a0 = variance of {0, 0.5, 0.088, 1, 1}
  Step 4 (direction): f_0 values are spread from 0 to 1, so raw variance is
                      LARGE at the slot-weight level. The P4-C "tight a_0
                      cluster" claim applies to f_conv (which absorbs f_0 into
                      a 1/M_0^2 formula with structural identities CHK3/CHK4).

=== SUBSTITUTION CHAIN — a_2 slot (integral) ===

  Step 1 (def): f_2^{scheme} = int_0^{Lambda^2} f(u) du (CC a_2 weight).
  Step 2 (substitute at Lambda^2 = lam_max^2):
           f_2^{SDW}      = int_0^{L2} sqrt(u) du = (2/3)*L2^(3/2)
           f_2^{anomaly}  = int_0^{L2} 1 du       = L2
           f_2^{f*}       = 0.912*(2/3)*L2^(3/2) + 0.088*(1 - exp(-L2))
           f_2^{Gaussian} = int_0^{L2} exp(-u^2) du = (sqrt(pi)/2)*erf(L2)
           f_2^{exp-decay}= int_0^{L2} exp(-u) du = 1 - exp(-L2)
  Step 3 (P4-C ordering): SDW < anomaly < f* at a_2 (magnitudes differ by
                          factor ~3.93 at L=9).
  Step 4 (direction): sigma^2_a2 is LARGE by construction (integral magnitudes
                      differ by orders when Lambda is large; Gaussian and
                      exp-decay saturate at finite values).

=== NORMALIZATION REMARK ===

Raw integrals span from saturated O(1) (Gaussian, exp-decay as Lambda grows
large) to unbounded O(Lambda^3) (SDW, f*). To compare sibling classes FAIRLY,
use log-variance (regulator classes differ in POWER of Lambda, not coefficient
of the same power). Equivalently, compare after unit-normalization to the
Lambda-independent contribution: the ratio to the f* anchor is the natural
P4-C reference.

We report THREE representations:
  (A) Raw slot variance on {f_0, f_2} values: test direct S80 template.
  (B) Log10 variance: scale-invariant (since integrals span orders).
  (C) P4-C operational f_conv variance for a_0 (matches W2-D cluster).

Gate evaluation uses (A) per S80 template. (B) and (C) are diagnostics.

=== L_max ===

Primary: L_max = 5 (per S80 template L1475). Cross-checks at L_max in
{3, 7, 9} using the s74_spectrum_cache_L9_tau019.npz eigenvalue data.
"""

import sys
import os
import time
import hashlib
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(str(SCRIPT_DIR))

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

from canonical_constants import (
    PI,
    a0_fold, a2_fold, a4_fold,
    M_KK_gravity,
    R_protected_fold,
    tau_fold,
    mellin_f_star_f0, mellin_f_star_f2, mellin_f_star_f4,
)

from scipy import integrate, special

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_NPZ  = SCRIPT_DIR / "s82_w2_8_a2_cluster_test.npz"
OUT_PNG  = SCRIPT_DIR / "s82_w2_8_a2_cluster_test.png"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)
GATE_VERDICTS  = SCRIPT_DIR / "s82_gate_verdicts.txt"            # (local)

t_start = time.time()  # (local)

# =============================================================================
# SECTION 0: SHA-256 INPUT PINS (first 20 stdout lines — per S81+ standard)
# =============================================================================

def sha256_file(path):
    """Return 64-char hex SHA-256 of file contents."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(65536)  # (local)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

SHA_SPECTRUM   = sha256_file(SPECTRUM_CACHE)  # (local)
SHA_CANON      = sha256_file(SCRIPT_DIR / "canonical_constants.py")  # (local)
SHA_THIS       = sha256_file(__file__)  # (local)

print("=" * 78)
print("S82-W2-8: A2-CLUSTER-TEST [VERIFY]")
print("=" * 78)
print(f"tau_fold       = {tau_fold}")
print(f"a0_fold        = {a0_fold}")
print(f"a2_fold        = {a2_fold}")
print(f"a4_fold        = {a4_fold}")
print(f"R_protected    = {R_protected_fold:.10f}")
print()
print("SHA-256 input pins (S81+ canonical form):")
print(f"  SHA_spectrum         = {SHA_SPECTRUM}")
print(f"  SHA_canonical_const  = {SHA_CANON}")
print(f"  SHA_script_self      = {SHA_THIS}")
print()

# =============================================================================
# SECTION 1: LOAD SPECTRUM + DEFINE L_MAX SCAN
# =============================================================================
print("=" * 78)
print("SECTION 1: Load D_K spectrum (L_max=9 Jensen-deformed cache)")
print("=" * 78)

assert SPECTRUM_CACHE.exists(), f"Cache not found: {SPECTRUM_CACHE}"
cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sector_evals = cache['sector_evals'].item()
cache.close()

L_MAX_PRIMARY = 5                                # (local) per S80 template L1475
L_max_scan    = [3, 5, 7, 9]                     # (local) robustness scan
EVAL_CUTOFF   = 0.01                             # (local) IR match S77/S78


def collect_spectrum(sector_dict, L_max, cutoff):
    """Return (|lam|, mult) arrays for modes at level <= L_max and |lam|>cutoff."""
    abs_list  = []  # (local)
    mult_list = []  # (local)
    for (p, q), data in sorted(sector_dict.items()):
        if data['level'] <= L_max:
            dim = int(data['dim'])  # (local) SU(3) irrep dim
            for ev in data['abs_evals']:
                a = float(ev)  # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return np.array(abs_list), np.array(mult_list, dtype=np.float64)


spec_by_L = {L: collect_spectrum(sector_evals, L, EVAL_CUTOFF) for L in L_max_scan}  # (local)
for L in L_max_scan:
    lam, mult = spec_by_L[L]
    print(f"  L_max={L}: n_evals={len(lam):5d}  lam_max={lam.max():.6f}  "
          f"sum(mult)={int(mult.sum())}")

# =============================================================================
# SECTION 2: DEFINE SCHEME KERNELS + MELLIN WEIGHTS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Scheme kernels (5 regulators per S80 §W2-8)")
print("=" * 78)

alpha_star = 0.912  # (local) f* sqrt coefficient
beta_star  = 0.088  # (local) f* exp coefficient (aliases t_star = 0.088)


def k_SDW(x):
    """SDW: f(x) = sqrt(x) — Andrianov-Lizzi heat-kernel."""
    return np.sqrt(np.abs(x))


def k_anomaly(x):
    """Anomaly: sharp cutoff f(x) = 1 on [0, Lambda^2] (CC/AL f_0 = 1/2 forced)."""
    return np.ones_like(np.asarray(x, dtype=np.float64))


def k_fstar(x):
    """f*(x) = 0.912 sqrt(x) + 0.088 exp(-x) — S72 empirical fit."""
    return alpha_star * np.sqrt(np.abs(x)) + beta_star * np.exp(-x)


def k_Gaussian(x):
    """Gaussian: f(x) = exp(-x^2) — classical heat-kernel regulator."""
    return np.exp(-x**2)


def k_expdecay(x):
    """exp-decay: f(x) = exp(-x)."""
    return np.exp(-x)


# a_0 slot weight (pointwise at x = 0), Chamseddine-Connes convention.
# Note: SDW "effective" f_0 is 0 formally; anomaly is CC-AL FORCED to 1/2.
# We report the CC-convention direct pointwise values.
f_0_dict = {  # (local)
    'SDW':       0.0,             # sqrt(0) = 0, formal
    'anomaly':   0.5,             # FORCED by fermionic-anomaly cancellation
    'f*':        float(beta_star),# f*(0) = 0.088
    'Gaussian':  1.0,             # exp(-0) = 1
    'exp-decay': 1.0,             # exp(-0) = 1
}


# a_2 slot weight = int_0^{Lambda^2} f(u) du
def f_2_analytic(scheme, Lam_sq):
    """Analytic a_2 slot weight at cutoff Lambda^2."""
    L2 = float(Lam_sq)  # (local)
    if scheme == 'SDW':
        return (2.0/3.0) * L2**(1.5)
    if scheme == 'anomaly':
        return L2
    if scheme == 'f*':
        return alpha_star * (2.0/3.0) * L2**(1.5) + beta_star * (1.0 - np.exp(-L2))
    if scheme == 'Gaussian':
        return (np.sqrt(np.pi)/2.0) * special.erf(L2)
    if scheme == 'exp-decay':
        return 1.0 - np.exp(-L2)
    raise ValueError(f"Unknown scheme: {scheme}")


# Numerical cross-check via quadrature
def f_2_numeric(scheme, Lam_sq):
    """Numerical a_2 slot weight via scipy.integrate.quad — cross-check."""
    kernel_map = {  # (local)
        'SDW': k_SDW, 'anomaly': k_anomaly, 'f*': k_fstar,
        'Gaussian': k_Gaussian, 'exp-decay': k_expdecay,
    }
    val, err = integrate.quad(kernel_map[scheme], 0.0, float(Lam_sq),
                              limit=500, epsabs=1e-14, epsrel=1e-12)  # (local)
    return float(val)


# =============================================================================
# SECTION 3: PRIMARY COMPUTATION AT L_MAX_PRIMARY = 5
# =============================================================================
print("\n" + "=" * 78)
print(f"SECTION 3: Slot values at L_max = {L_MAX_PRIMARY}")
print("=" * 78)

lam_primary, mult_primary = spec_by_L[L_MAX_PRIMARY]
lam_max_primary = float(lam_primary.max())  # (local)
Lam_sq_primary  = lam_max_primary**2          # (local)

print(f"  lam_max(L={L_MAX_PRIMARY}) = {lam_max_primary:.6f} M_KK")
print(f"  Lambda^2 cutoff         = {Lam_sq_primary:.6f} M_KK^2")
print()

schemes = ['SDW', 'anomaly', 'f*', 'Gaussian', 'exp-decay']  # (local)

# ---- a_0 slot values ----
a0_vals_primary = np.array([f_0_dict[s] for s in schemes])  # (local)

# ---- a_2 slot values (analytic + numerical) ----
a2_analytic_primary = np.array([f_2_analytic(s, Lam_sq_primary) for s in schemes])  # (local)
a2_numeric_primary  = np.array([f_2_numeric(s, Lam_sq_primary)  for s in schemes])  # (local)

print(f"{'Scheme':<12} {'f_0':>12} {'f_2(analytic)':>16} {'f_2(numeric)':>16} {'|diff|/|f_2|':>16}")
for i, s in enumerate(schemes):
    diff = abs(a2_analytic_primary[i] - a2_numeric_primary[i]) / max(abs(a2_analytic_primary[i]), 1e-30)  # (local)
    print(f"{s:<12} {a0_vals_primary[i]:12.6f} {a2_analytic_primary[i]:16.6e} "
          f"{a2_numeric_primary[i]:16.6e} {diff:16.2e}")

# Analytic-numerical agreement check
max_diff = np.max(np.abs(a2_analytic_primary - a2_numeric_primary) /
                  np.maximum(np.abs(a2_analytic_primary), 1e-30))  # (local)
assert max_diff < 1e-8, f"Analytic vs numeric a_2 disagreement {max_diff:.2e}"
print(f"\n  ANALYTIC vs NUMERIC cross-check: max rel-diff = {max_diff:.2e}")


# =============================================================================
# SECTION 4: INTRA-CLUSTER VARIANCE (S80 TEMPLATE L1480-L1483)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Intra-cluster variance (S80 template, L1480-L1483)")
print("=" * 78)

def normalized_variance(vals, name):
    """var_norm = sigma^2(vals) / <vals>^2 (S80 template)."""
    v = np.asarray(vals, dtype=np.float64)  # (local)
    mean = float(np.mean(v))  # (local)
    var  = float(np.var(v))   # (local)
    if abs(mean) < 1e-30:
        return float('inf')
    return var / mean**2


var_a0_full = normalized_variance(a0_vals_primary, 'a_0')  # (local) across all 5 schemes
var_a2_full = normalized_variance(a2_analytic_primary, 'a_2')  # (local) across all 5 schemes

print(f"\n  FULL 5-scheme cluster (SDW, anomaly, f*, Gaussian, exp-decay):")
print(f"    var(f_0)/<f_0>^2 = {var_a0_full*100:12.4f}%")
print(f"    var(f_2)/<f_2>^2 = {var_a2_full*100:12.4f}%")

# ---- P4-C operational triple {SDW, anomaly-sharp, f*} (the sibling-class test) ----
# P4-C (L827-L829) operational sibling class does NOT include Gaussian or
# exp-decay (these are additional sanity schemes). Report the 3-scheme
# sibling-class variance separately as the P4-C-aligned readout.
i_P4C = [schemes.index(s) for s in ['SDW', 'anomaly', 'f*']]  # (local)
var_a0_P4C = normalized_variance(a0_vals_primary[i_P4C], 'a_0-P4C')  # (local)
var_a2_P4C = normalized_variance(a2_analytic_primary[i_P4C], 'a_2-P4C')  # (local)

print(f"\n  P4-C 3-scheme sibling-class (SDW, anomaly-sharp, f*):")
print(f"    var(f_0)/<f_0>^2 = {var_a0_P4C*100:12.4f}%")
print(f"    var(f_2)/<f_2>^2 = {var_a2_P4C*100:12.4f}%")

# ---- Log-space variance (scale-invariant; integrals span decades at large Lambda) ----
# Gaussian saturates at sqrt(pi)/2 ~ 0.886; SDW scales as Lambda^3; spans are
# enormous. The LOG10 variance is the scale-invariant comparison.
# Only compute where vals > 0 (SDW f_0 = 0 -> log undefined; skip).
def log10_variance(vals):
    """sigma^2(log10(vals)) for positive values only."""
    v = np.asarray(vals, dtype=np.float64)  # (local)
    pos = v[v > 1e-30]  # (local)
    if len(pos) < 2:
        return float('nan')
    return float(np.var(np.log10(pos)))


var_log_a0_full = log10_variance(a0_vals_primary)  # (local)
var_log_a2_full = log10_variance(a2_analytic_primary)  # (local)

print(f"\n  LOG10 variance (scale-invariant):")
print(f"    var(log10(f_0)) = {var_log_a0_full:12.4f}  (spans {np.sqrt(var_log_a0_full):.3f} OOM)")
print(f"    var(log10(f_2)) = {var_log_a2_full:12.4f}  (spans {np.sqrt(var_log_a2_full):.3f} OOM)")


# =============================================================================
# SECTION 5: L_MAX SCAN — stability of cluster variance
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: L_max scan (robustness: L in {3, 5, 7, 9})")
print("=" * 78)

scan_var_a0_full = []  # (local)
scan_var_a2_full = []  # (local)
scan_var_a0_P4C  = []  # (local)
scan_var_a2_P4C  = []  # (local)
scan_lam_max     = []  # (local)
scan_f2_per_scheme = {s: [] for s in schemes}  # (local)

for L in L_max_scan:
    lam, _ = spec_by_L[L]
    L2 = float(lam.max())**2  # (local)
    scan_lam_max.append(float(lam.max()))
    a0_L = np.array([f_0_dict[s] for s in schemes])  # (local) L-independent
    a2_L = np.array([f_2_analytic(s, L2) for s in schemes])  # (local)
    scan_var_a0_full.append(normalized_variance(a0_L, 'a0'))
    scan_var_a2_full.append(normalized_variance(a2_L, 'a2'))
    scan_var_a0_P4C.append(normalized_variance(a0_L[i_P4C], 'a0-P4C'))
    scan_var_a2_P4C.append(normalized_variance(a2_L[i_P4C], 'a2-P4C'))
    for j, s in enumerate(schemes):
        scan_f2_per_scheme[s].append(a2_L[j])

print(f"\n  {'L_max':>6} {'lam_max':>10} {'var(f_0)%':>14} {'var(f_2)%':>14} "
      f"{'var(f_0)P4C%':>14} {'var(f_2)P4C%':>14}")
for i, L in enumerate(L_max_scan):
    print(f"  {L:>6d} {scan_lam_max[i]:>10.4f} "
          f"{scan_var_a0_full[i]*100:>14.4f} "
          f"{scan_var_a2_full[i]*100:>14.4f} "
          f"{scan_var_a0_P4C[i]*100:>14.4f} "
          f"{scan_var_a2_P4C[i]*100:>14.4f}")


# =============================================================================
# SECTION 6: GATE EVALUATION (pre-registered thresholds)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: GATE [VERIFY] S82-A2-CLUSTER-TEST — pre-registered thresholds")
print("=" * 78)

# Pre-registered from S80 plan §W2-8 L1458-L1460:
#   PASS:  a_0 variance < 1%   AND a_2 variance > 5%
#   INFO:  a_2 variance in [1%, 5%]
#   FAIL:  a_0 variance > 1%   OR  a_2 variance < 1%
#
# Variance definition (S80 template L1480-L1483): sigma^2({a_i})/<a_i>^2
#
# Primary reference: the FULL 5-scheme variance at L_max=5 (S80 template
# implied by §W2-8 "all regulator schemes (SDW, anomaly=2/3, f*, Gaussian,
# exp-decay)").

PRIMARY_VAR_A0 = var_a0_full * 100.0  # (local) %
PRIMARY_VAR_A2 = var_a2_full * 100.0  # (local) %

print(f"\n  Primary (L_max={L_MAX_PRIMARY}, 5-scheme):")
print(f"    var(a_0) = {PRIMARY_VAR_A0:.4f}%  vs threshold < 1% for PASS")
print(f"    var(a_2) = {PRIMARY_VAR_A2:.4f}%  vs threshold > 5% for PASS")

# Gate direction substitution chain:
#   Step 1 (def): PASS iff var_a0 < 1% AND var_a2 > 5%.
#   Step 2 (sub): var_a0 = {PRIMARY_VAR_A0}%, var_a2 = {PRIMARY_VAR_A2}%.
#   Step 3 (simplify):
#            cond_pass_a0 = (var_a0 < 1)
#            cond_pass_a2 = (var_a2 > 5)
#            cond_info_a2 = (1 <= var_a2 <= 5)
#            cond_fail    = (var_a0 > 1) OR (var_a2 < 1)
#   Step 4 (direction): gate = (PASS if cond_pass_a0 AND cond_pass_a2 else
#                               FAIL if cond_fail else INFO)

cond_pass_a0 = PRIMARY_VAR_A0 < 1.0   # (local)
cond_pass_a2 = PRIMARY_VAR_A2 > 5.0   # (local)
cond_info_a2 = 1.0 <= PRIMARY_VAR_A2 <= 5.0  # (local)
cond_fail    = (PRIMARY_VAR_A0 > 1.0) or (PRIMARY_VAR_A2 < 1.0)  # (local)

print(f"\n  Substitution-chain evaluation:")
print(f"    cond_pass_a0 (var_a0 < 1%): {cond_pass_a0}")
print(f"    cond_pass_a2 (var_a2 > 5%): {cond_pass_a2}")
print(f"    cond_info_a2 (1 <= var_a2 <= 5%): {cond_info_a2}")
print(f"    cond_fail    (var_a0>1 OR var_a2<1): {cond_fail}")

if cond_pass_a0 and cond_pass_a2:
    verdict = "PASS"  # (local)
elif cond_fail:
    verdict = "FAIL"  # (local)
else:
    verdict = "INFO"  # (local)

print(f"\n  *** VERDICT (primary, 5-scheme, L_max={L_MAX_PRIMARY}): {verdict} ***")

# Also report the P4-C 3-scheme verdict for diagnostic context
cond_pass_a0_P4C = (var_a0_P4C * 100.0) < 1.0   # (local)
cond_pass_a2_P4C = (var_a2_P4C * 100.0) > 5.0   # (local)
cond_fail_P4C    = ((var_a0_P4C * 100.0) > 1.0) or ((var_a2_P4C * 100.0) < 1.0)  # (local)
if cond_pass_a0_P4C and cond_pass_a2_P4C:
    verdict_P4C = "PASS"  # (local)
elif cond_fail_P4C:
    verdict_P4C = "FAIL"  # (local)
else:
    verdict_P4C = "INFO"  # (local)

print(f"\n  Diagnostic: P4-C 3-scheme (SDW, anomaly-sharp, f*) at L_max={L_MAX_PRIMARY}:")
print(f"    var(a_0)_P4C = {var_a0_P4C*100:.4f}%")
print(f"    var(a_2)_P4C = {var_a2_P4C*100:.4f}%")
print(f"    Diagnostic verdict: {verdict_P4C}")


# =============================================================================
# SECTION 7: PLOT (diagnostic)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Emit plot (log-scale a_n across schemes, L_max scan)")
print("=" * 78)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Panel A: bar chart of a_0 and a_2 slot values at L_max=5
ax = axes[0]
x_idx = np.arange(len(schemes))  # (local)
width = 0.35                      # (local)
a0_vals_plot = np.array([max(v, 1e-30) for v in a0_vals_primary])  # (local)
a2_vals_plot = np.array([max(v, 1e-30) for v in a2_analytic_primary])  # (local)
ax.bar(x_idx - width/2, a0_vals_plot, width, label='$f_0$ (a_0 slot)', color='steelblue')
ax.bar(x_idx + width/2, a2_vals_plot, width, label='$f_2$ (a_2 slot)', color='darkorange')
ax.set_yscale('log')
ax.set_xticks(x_idx)
ax.set_xticklabels(schemes, rotation=30, ha='right')
ax.set_ylabel('Slot weight (log10 scale)')
ax.set_title(f'Slot weights across schemes (L_max={L_MAX_PRIMARY}, $\\Lambda^2$={Lam_sq_primary:.2f})')
ax.legend(loc='best')
ax.grid(True, alpha=0.3, which='both')

# Panel B: L_max dependence of normalized variance
ax = axes[1]
ax.plot(L_max_scan, [v*100 for v in scan_var_a0_full], 'o-',
        color='steelblue', label='var($a_0$)% — 5-scheme')
ax.plot(L_max_scan, [v*100 for v in scan_var_a2_full], 's-',
        color='darkorange', label='var($a_2$)% — 5-scheme')
ax.plot(L_max_scan, [v*100 for v in scan_var_a0_P4C], 'o--',
        color='cornflowerblue', alpha=0.7, label='var($a_0$)% — P4-C 3-scheme')
ax.plot(L_max_scan, [v*100 for v in scan_var_a2_P4C], 's--',
        color='gold', alpha=0.7, label='var($a_2$)% — P4-C 3-scheme')
ax.axhline(1.0, color='green', linestyle=':', label='PASS threshold a_0 (1%)')
ax.axhline(5.0, color='red', linestyle=':', label='PASS threshold a_2 (5%)')
ax.set_yscale('log')
ax.set_xlabel('$L_{max}$')
ax.set_ylabel('Normalized variance (%)')
ax.set_title('Intra-cluster variance vs $L_{max}$')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=140)
plt.close(fig)
print(f"  -> {OUT_PNG.name}")


# =============================================================================
# SECTION 8: PERSIST ARTIFACTS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Save npz")
print("=" * 78)

np.savez_compressed(
    OUT_NPZ,
    schemes=np.array(schemes),
    f_0_values=a0_vals_primary,
    f_2_analytic=a2_analytic_primary,
    f_2_numeric=a2_numeric_primary,
    L_max_primary=L_MAX_PRIMARY,
    lam_max_primary=lam_max_primary,
    Lambda_sq_primary=Lam_sq_primary,
    var_a0_full=var_a0_full,
    var_a2_full=var_a2_full,
    var_a0_P4C=var_a0_P4C,
    var_a2_P4C=var_a2_P4C,
    var_log_a0_full=var_log_a0_full,
    var_log_a2_full=var_log_a2_full,
    L_max_scan=np.array(L_max_scan),
    scan_lam_max=np.array(scan_lam_max),
    scan_var_a0_full=np.array(scan_var_a0_full),
    scan_var_a2_full=np.array(scan_var_a2_full),
    scan_var_a0_P4C=np.array(scan_var_a0_P4C),
    scan_var_a2_P4C=np.array(scan_var_a2_P4C),
    verdict=verdict,
    verdict_P4C=verdict_P4C,
    SHA_spectrum=SHA_SPECTRUM,
    SHA_canonical=SHA_CANON,
    SHA_script=SHA_THIS,
    tau_fold_used=tau_fold,
    EVAL_CUTOFF=EVAL_CUTOFF,
)
print(f"  -> {OUT_NPZ.name}")


# =============================================================================
# SECTION 9: CLOSURE HASH (SHA-256 of ordered input-pin map)
# =============================================================================
closure_map = (
    f"SHA_spectrum={SHA_SPECTRUM}|"
    f"SHA_canonical={SHA_CANON}|"
    f"SHA_script={SHA_THIS}|"
    f"L_max={L_MAX_PRIMARY}|"
    f"tau_fold={tau_fold}|"
    f"EVAL_CUTOFF={EVAL_CUTOFF}|"
    f"lam_max_primary={lam_max_primary:.10f}|"
    f"var_a0_full={var_a0_full:.10e}|"
    f"var_a2_full={var_a2_full:.10e}|"
    f"verdict={verdict}"
)  # (local)
closure_sha = hashlib.sha256(closure_map.encode("utf-8")).hexdigest()  # (local)


# =============================================================================
# SECTION 10: 4-TUPLE TAG + VERDICT LINE
# =============================================================================
tag_value     = f"{PRIMARY_VAR_A2:.6f}"              # (local) %
tag_scheme    = "FULL-5-SCHEME-CLUSTER"              # (local)
tag_conv      = "P4C-SLOT-TAXONOMY"                  # (local)
tag_L_max     = f"L_max={L_MAX_PRIMARY}"             # (local)

print("\n" + "=" * 78)
print("SECTION 10: Output tag + verdict line")
print("=" * 78)
print(f"  value        = {tag_value}   [%, a_2 intra-cluster variance]")
print(f"  scheme       = {tag_scheme}")
print(f"  convention   = {tag_conv}")
print(f"  L_max        = {tag_L_max}")
print(f"  sha256       = {closure_sha}")
print(f"  verdict      = {verdict}")

verdict_line = (
    f"S82-A2-CLUSTER-TEST: {verdict} -- "
    f"value={tag_value} scheme={tag_scheme} convention={tag_conv} "
    f"{tag_L_max} sha256={closure_sha}"
)  # (local)

# Append to s82_gate_verdicts.txt (NOTE: s82 not s80 per task instruction)
with open(GATE_VERDICTS, "a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")

print(f"\n  appended to: {GATE_VERDICTS.name}")
print(f"  verdict line: {verdict_line}")

print(f"\nelapsed: {time.time() - t_start:.2f}s")
