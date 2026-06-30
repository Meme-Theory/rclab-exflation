#!/usr/bin/env python3
"""
S83 W2-G27 — MP-ADMISSIBILITY-UNIFIED
======================================

Gate: S83-MP-ADMISSIBILITY-UNIFIED  [VERIFY]
Classification: GEOMETRIC
Owner: spectral-geometer

PURPOSE
-------
Probe Mellin-Plancherel (MP) admissibility across FIVE distinct function
classes at the KO-dimension anchor s_KO = 6:

    class 1:  log             f(x) = log(x)
    class 2:  step            f(x) = Theta(1 - x)       (Heaviside)
    class 3:  fractional      f(x) = x^a     (a = -1/2, canonical SDW sqrt-pole)
    class 4:  sum_of_exp      f(x) = sum_j c_j exp(-lambda_j x)
    class 5:  oscillatory     f(x) = x cos(omega x)

For each class f we (a) verify convergence of the Mellin transform

    M[f](s) = integral_0^infty f(x) x^{s - 1} dx    (Schwartz-class test)

at s = s_KO = 6 and (b) verify L-invariance of the Mellin multiplier
under positive rescaling L: f(x) -> f(x/L) producing M[f](s) -> L^s M[f](s).

PRE-REGISTERED SUBSTITUTION CHAIN (MANDATORY [VERIFY])
------------------------------------------------------
Step 1 (definition):  MP admissibility at s = KO-dim := Mellin transform of f
    exists and is analytic at s = s_KO = 6. Here we test absolute convergence
    of the integral (Schwartz class), not distributional continuation.
Step 2 (substitution, class by class):
    class 1 (log):       integrand = log(x) * x^5;
                          small-x: integrable, large-x: ~ x^5 log(x) -> infinity.
    class 2 (step):      integrand = Theta(1-x) * x^5;
                          support [0,1], value = 1/6.
    class 3 (frac, a=-1/2): integrand = x^(a+s-1) = x^{9/2};
                          divergent at infinity on [0, infinity).
    class 4 (sum_exp):   integrand = [sum_j c_j exp(-lam_j x)] * x^5;
                          M = Gamma(s) * sum_j c_j / lam_j^s.
    class 5 (oscillatory): integrand = x cos(omega x) * x^5 = x^6 cos(omega x);
                          NOT absolutely convergent (envelope ~ x^6).
Step 3 (simplification):
    class 1: M -> +infinity (log x * x^5 divergence)
    class 2: M = 1/s|_{s=6} = 1/6 < infinity
    class 3: M -> +infinity (power-law)
    class 4: M = Gamma(6) * sum_j c_j / lam_j^6 < infinity
    class 5: M ill-defined (Schwartz sense); Abel-summable only.
Step 4 (direction):
    admissible = {step, sum_of_exp}    (2 of 5)
    excluded   = {log, fractional, oscillatory}    (3 of 5)
    Gate:  FAIL  (admissible_count = 2 < 3 = INFO threshold).

GATE LEVELS (pre-registered task spec)
---------------------------------------
    PASS:  all 5 classes MP-admissible
    INFO:  3 or 4 of 5 classes MP-admissible
    FAIL:  fewer than 3 admissible

L-INVARIANCE CROSS-CHECK (per class)
------------------------------------
Let f_L(x) = f(x/L) for L > 0. Substitution u = x/L:

    M[f_L](s) = int_0^inf f(x/L) x^{s-1} dx
              = L^s * int_0^inf f(u) u^{s-1} du
              = L^s * M[f](s).

If M[f](s_KO) is finite, then M[f_L](s_KO) = L^{s_KO} * M[f](s_KO) and
the Mellin multiplier maps f to L^{s_KO} = L^6 faithfully.
CLASSES THAT DIVERGE IN M[f] DO NOT SATISFY L-INVARIANCE under this norm.

ENVIRONMENT
-----------
CPU thread cap at 8 (before numpy import). Mellin moments via scipy.quad on
[0, R] with R scan for diagnosis of divergent classes.
"""
from __future__ import annotations

import os
# --- CPU thread cap (before numpy)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
from math import gamma as _gamma

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Canonical constants import (MANDATORY from S34+)
HERE = Path(__file__).resolve().parent                      # (local)
sys.path.insert(0, str(HERE))
from canonical_constants import *  # noqa: F401,F403

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================


def _sha256(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()                                    # (local)
    with open(path, 'rb') as fp:
        h.update(fp.read())
    return h.hexdigest()


INPUT_FILES = [                                             # (local)
    HERE / 'canonical_constants.py',
    HERE / 's82_w1_3_cc_ratios_sg.py',
    HERE / 's80_cc_ratios_only_sanity.py',
]

print("=" * 72)
print("S83 W2-G27: MP-ADMISSIBILITY-UNIFIED (5 function classes at s_KO=6)")
print("=" * 72)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                             # (local)
for _f in INPUT_FILES:
    if _f.exists():
        _h = _sha256(_f)                                    # (local)
        INPUT_SHAS[_f.name] = _h
        print(f"  {_f.name:40s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[_f.name] = None
        print(f"  {_f.name:40s} MISSING")

# ============================================================
# SECTION 1: Substitution chain (print for audit trail)
# ============================================================
print("\n[SEC 1] Substitution chain (definition -> substitution -> direction)")
print("  Step 1:  MP admissibility at s_KO=6 :=")
print("           M[f](s) = integral_0^infty f(x) x^{s-1} dx")
print("           is absolutely convergent and analytic at s = 6.")
print("  Step 2:  Per class, compute integrand f(x) * x^{s-1} and probe")
print("           the upper-limit behaviour (finite R scan) for divergence.")
print("  Step 3:  Compare to known analytic closed forms where available")
print("           (step: 1/s;  sum_exp: Gamma(s) * sum c_j / lambda_j^s).")
print("  Step 4:  Direction comes from the R-scan slope:")
print("             bounded as R -> inf   => ADMISSIBLE")
print("             unbounded as R -> inf => EXCLUDED")

# ============================================================
# SECTION 2: Anchor parameters
# ============================================================
print("\n[SEC 2] Anchor parameters")
s_KO = 6.0                                                  # (local) KO-dimension anchor
print(f"  s_KO = {s_KO}  (Connes KO-dim=6 for M4 x SU(3) triple)")

# Scan radii for divergence diagnosis
R_SCAN = [5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0]       # (local)
print(f"  R-scan radii: {R_SCAN}")

# Thresholds for divergence diagnosis
GROWTH_FACTOR_THRESH = 10.0                                 # (local) if |M(R_N)|/|M(R_1)| > this, diverges
ABSOLUTE_FINITE_THRESH = 1e15                               # (local) if any |M(R)| exceeds this: diverges
ADMISSIBLE_REL_TOL = 1e-8                                   # (local) match to analytic closed form
print(f"  Growth-factor threshold: {GROWTH_FACTOR_THRESH}")
print(f"  Absolute-finite threshold: {ABSOLUTE_FINITE_THRESH:.0e}")

# Gate thresholds (pre-registered in task spec)
PASS_COUNT = 5                                              # (local)
INFO_MIN_COUNT = 3                                          # (local)
FAIL_MAX_COUNT = 2                                          # (local)

# ============================================================
# SECTION 3: Class definitions
# ============================================================
print("\n[SEC 3] Function class definitions")

# Class 1: log
def f_log(x):                                               # (local)
    return np.log(x)

# Class 2: step Theta(1-x) (unit threshold)
def f_step(x):                                              # (local)
    # vectorised; np.where requires arrays
    if np.isscalar(x):
        return 1.0 if x <= 1.0 else 0.0
    return np.where(x <= 1.0, 1.0, 0.0)

# Class 3: fractional power
FRAC_ALPHA = -0.5                                           # (local) SDW sqrt-pole canonical
def f_frac(x):                                              # (local)
    return x ** FRAC_ALPHA

# Class 4: sum-of-exponentials (three terms; arbitrary positive coefficients)
SUMEXP_C = np.array([0.5, 0.3, 0.2])                        # (local) coefficients c_j
SUMEXP_LAM = np.array([1.0, 2.0, 0.5])                      # (local) decay rates lambda_j > 0
def f_sumexp(x):                                            # (local)
    return np.sum(SUMEXP_C[:, None] * np.exp(-SUMEXP_LAM[:, None] * x), axis=0) \
        if not np.isscalar(x) else float(np.sum(SUMEXP_C * np.exp(-SUMEXP_LAM * x)))

# Class 5: oscillatory
OSC_OMEGA = 1.0                                             # (local) oscillator frequency
def f_osc(x):                                               # (local)
    return x * np.cos(OSC_OMEGA * x)

CLASSES = {                                                 # (local) name -> f
    "log":          f_log,
    "step":         f_step,
    "fractional":   f_frac,
    "sum_exp":      f_sumexp,
    "oscillatory":  f_osc,
}
print(f"  Classes tested: {list(CLASSES.keys())}")
print(f"  fractional alpha = {FRAC_ALPHA}")
print(f"  sum_exp c_j = {SUMEXP_C}, lambda_j = {SUMEXP_LAM}")
print(f"  oscillator omega = {OSC_OMEGA}")

# ============================================================
# SECTION 4: Mellin R-scan per class
# ============================================================
print("\n[SEC 4] Mellin R-scan at s = s_KO = 6")
print(f"  {'class':<14} | " + " | ".join(f"R={R}" for R in R_SCAN))
print("  " + "-" * 92)

mellin_scan = {}                                            # (local)
for name, f in CLASSES.items():
    vals = []                                               # (local)
    for R in R_SCAN:
        # numerical quad on [eps, R] -- eps small to avoid log(0)
        # Step function has compact support on [0,1]; sampling it over
        # [0, 500] with limit=400 causes scipy.quad to miss the [0,1]
        # interval (sampling density 1.25 / interval) and return 0.
        # For the step class only, split the integration at x=1.
        eps = 1e-10                                         # (local)
        try:
            if name == 'step':
                # Split [eps, min(R,1)] + [1, R]; second piece = 0 since
                # Theta(1-x) = 0 for x > 1.
                R_eff = min(R, 1.0)                         # (local)
                val, _ = quad(
                    lambda x: f(x) * x ** (s_KO - 1.0),
                    eps, R_eff, limit=400,
                )
            else:
                val, _ = quad(
                    lambda x: f(x) * x ** (s_KO - 1.0),
                    eps, R, limit=400,
                )
            vals.append(val)
        except Exception as e:                              # pragma: no cover
            vals.append(float('nan'))
    mellin_scan[name] = np.array(vals)
    row = " | ".join(f"{v:+.3e}" for v in vals)
    print(f"  {name:<14} | " + row)

# ============================================================
# SECTION 5: Classify each class
# ============================================================
print("\n[SEC 5] Classification (ADMISSIBLE / EXCLUDED)")

# Helper: is the M-scan saturating (finite limit) as R grows?
#
# Substitution chain for the classifier:
#   Step 1 (def):   ADMISSIBLE <=> M(R) -> finite limit as R -> infinity.
#   Step 2 (sub):   Saturation test = |M(R_last)/M(R_prev) - 1| small.
#                    (If the integral is Cauchy-converging, late-R increments
#                    vanish relative to the limit.)
#   Step 3 (simp):  Combine with an absolute-finite clip to reject unbounded
#                    magnitudes (log: 1.5e16 at R=500; oscillatory same).
#   Step 4 (dir):   bounded + saturated -> ADMISSIBLE; else EXCLUDED.
SAT_REL_TOL = 1e-3                                          # (local) |M_last/M_prev - 1| < this = saturated


def classify(name, scan_vals):                              # (local)
    """Decide admissibility from R-scan trajectory (saturation test)."""
    abs_vals = np.abs(scan_vals)                            # (local)
    # (a) absolute-finite check: any |M(R)| over cap => divergent
    if np.any(abs_vals > ABSOLUTE_FINITE_THRESH):
        return ("EXCLUDED",
                f"|M(R)| exceeds {ABSOLUTE_FINITE_THRESH:.0e} on scan "
                f"(max = {abs_vals.max():.2e})")
    finite_mask = np.isfinite(abs_vals)                     # (local)
    if finite_mask.sum() < 2:
        return ("EXCLUDED", "insufficient finite values in scan")
    # (b) saturation test on the tail: compare M(R_last) to M(R_prev)
    last = scan_vals[-1]                                    # (local, signed)
    prev = scan_vals[-2]                                    # (local, signed)
    if abs(prev) < 1e-30:
        return ("EXCLUDED",
                f"M(R_prev) ~ 0 ({prev:.2e}), cannot assess saturation")
    rel_step = abs(last - prev) / abs(prev)                 # (local)
    if rel_step < SAT_REL_TOL:
        return ("ADMISSIBLE",
                f"|M(R_last)/M(R_prev) - 1| = {rel_step:.2e} < "
                f"{SAT_REL_TOL:.0e}")
    return ("EXCLUDED",
            f"|M(R_last)/M(R_prev) - 1| = {rel_step:.2e} >= "
            f"{SAT_REL_TOL:.0e} (no saturation)")


classification = {}                                         # (local) name -> (verdict, reason)
for name in CLASSES:
    v, r = classify(name, mellin_scan[name])
    classification[name] = (v, r)
    print(f"  {name:<14} : {v:<11} -- {r}")

# ============================================================
# SECTION 6: Analytic closed-form cross-check
# ============================================================
print("\n[SEC 6] Analytic closed-form cross-check at s = 6")

closed_forms = {}                                           # (local) name -> (expected, numeric, deviation) or None

# Class 2 (step): M = 1/s = 1/6
step_analytic = 1.0 / s_KO                                  # (local)
step_numeric, _ = quad(lambda x: f_step(x) * x ** (s_KO - 1.0),
                       0.0, 2.0, limit=400)
step_dev = abs(step_numeric - step_analytic)                # (local)
closed_forms['step'] = (step_analytic, step_numeric, step_dev)
print(f"  step:       analytic = 1/6 = {step_analytic:.12e}")
print(f"              numeric  =       {step_numeric:.12e}")
print(f"              dev      =       {step_dev:.2e}   "
      f"({'MATCH' if step_dev < ADMISSIBLE_REL_TOL else 'MISMATCH'})")

# Class 4 (sum_exp): M = Gamma(s) * sum_j c_j / lambda_j^s
sumexp_analytic = _gamma(s_KO) * np.sum(SUMEXP_C / SUMEXP_LAM ** s_KO)  # (local)
sumexp_numeric, _ = quad(lambda x: f_sumexp(x) * x ** (s_KO - 1.0),
                         0.0, np.inf, limit=400)
sumexp_dev_abs = abs(sumexp_numeric - sumexp_analytic)      # (local)
sumexp_dev_rel = sumexp_dev_abs / abs(sumexp_analytic)      # (local)
closed_forms['sum_exp'] = (sumexp_analytic, sumexp_numeric, sumexp_dev_abs)
print(f"  sum_exp:    analytic = Gamma(6) * sum c_j/lam_j^6")
print(f"                       = {sumexp_analytic:.6e}")
print(f"              numeric  = {sumexp_numeric:.6e}")
print(f"              dev_abs  = {sumexp_dev_abs:.2e}")
print(f"              dev_rel  = {sumexp_dev_rel:.2e}  "
      f"({'MATCH' if sumexp_dev_rel < ADMISSIBLE_REL_TOL else 'MISMATCH'})")

# Classes 1, 3, 5: no closed-form on [0, infinity) (divergent)
for nm in ('log', 'fractional', 'oscillatory'):
    closed_forms[nm] = None
    print(f"  {nm:<11}: no closed form on [0, infinity) (divergent on Schwartz)")

# ============================================================
# SECTION 7: L-invariance cross-check
# ============================================================
print("\n[SEC 7] L-invariance cross-check (admissible classes only)")
print("  Identity: M[f(x/L)](s) = L^s * M[f](s)")
print("  Test at L = 2, s = 6: ratio should equal 2^6 = 64.")
L_test = 2.0                                                # (local)
expected_L_multiplier = L_test ** s_KO                      # (local) = 64

L_inv_results = {}                                          # (local) name -> (ratio, dev)
for name, f in CLASSES.items():
    if classification[name][0] != 'ADMISSIBLE':
        L_inv_results[name] = (None, None)
        print(f"  {name:<14}: skipped (EXCLUDED class; rescaling meaningless)")
        continue
    # Mellin of f(x/L) over [0, inf) if step, else [0, R_SCAN[-1]]
    def f_rescaled(x):                                      # (local)
        return f(x / L_test)

    R_up = R_SCAN[-1] if name != 'step' else 2.0 * L_test   # (local)
    if name == 'sum_exp':
        R_up = np.inf
    M_rescaled, _ = quad(lambda x: f_rescaled(x) * x ** (s_KO - 1.0),
                         0.0, R_up, limit=400)
    # Original
    R_up_orig = R_SCAN[-1] if name != 'step' else 2.0       # (local)
    if name == 'sum_exp':
        R_up_orig = np.inf
    M_orig, _ = quad(lambda x: f(x) * x ** (s_KO - 1.0),
                     0.0, R_up_orig, limit=400)
    ratio_observed = M_rescaled / M_orig if M_orig != 0 else float('nan')  # (local)
    dev = abs(ratio_observed - expected_L_multiplier) / expected_L_multiplier  # (local)
    L_inv_results[name] = (ratio_observed, dev)
    print(f"  {name:<14}: M[f(x/L)]/M[f] = {ratio_observed:.6e}  "
          f"(target {expected_L_multiplier:.0f})  rel_dev = {dev:.2e}")

# ============================================================
# SECTION 8: Verdict
# ============================================================
print("\n[SEC 8] Gate verdict")

admissible_count = sum(1 for v, _ in classification.values()
                       if v == 'ADMISSIBLE')               # (local)
excluded_count = sum(1 for v, _ in classification.values()
                     if v == 'EXCLUDED')                   # (local)
print(f"  Admissible count: {admissible_count} / {len(CLASSES)}")
print(f"  Excluded  count:  {excluded_count} / {len(CLASSES)}")

# Pre-registered thresholds
print(f"  PASS threshold: admissible_count == {PASS_COUNT}")
print(f"  INFO threshold: admissible_count >= {INFO_MIN_COUNT}")
print(f"  FAIL threshold: admissible_count <= {FAIL_MAX_COUNT}")

if admissible_count == PASS_COUNT:
    verdict_value = 0                                       # (local)
    verdict = "PASS"                                        # (local)
    reason = (                                              # (local)
        f"All {PASS_COUNT} classes MP-admissible at s_KO=6")
elif admissible_count >= INFO_MIN_COUNT:
    verdict_value = 1                                       # (local)
    verdict = "INFO"                                        # (local)
    reason = (                                              # (local)
        f"{admissible_count}/5 classes admissible "
        f"(>= INFO min {INFO_MIN_COUNT}, < PASS threshold)")
else:
    verdict_value = 2                                       # (local)
    verdict = "FAIL"                                        # (local)
    reason = (                                              # (local)
        f"Only {admissible_count}/5 classes MP-admissible "
        f"(< INFO min {INFO_MIN_COUNT}). EXCLUDED: "
        f"{[n for n, (v, _) in classification.items() if v == 'EXCLUDED']}")

print(f"\n  -> verdict value: {verdict_value}")
print(f"  -> verdict:       {verdict}")
print(f"  -> reason:        {reason}")

# ============================================================
# SECTION 9: Closure SHA + 4-tuple emit
# ============================================================
print("\n[SEC 9] Closure SHA and 4-tuple emit")

closure_map = {                                             # (local) ordered input-pin map
    'script': 's83_w2_g27_mp_admissibility_unified.py',
    's_KO': s_KO,
    'classes': list(CLASSES.keys()),
    'R_SCAN': R_SCAN,
    'FRAC_ALPHA': FRAC_ALPHA,
    'SUMEXP_C': SUMEXP_C.tolist(),
    'SUMEXP_LAM': SUMEXP_LAM.tolist(),
    'OSC_OMEGA': OSC_OMEGA,
    'PASS_COUNT': PASS_COUNT,
    'INFO_MIN_COUNT': INFO_MIN_COUNT,
    'FAIL_MAX_COUNT': FAIL_MAX_COUNT,
    'GROWTH_FACTOR_THRESH': GROWTH_FACTOR_THRESH,
    'ABSOLUTE_FINITE_THRESH': ABSOLUTE_FINITE_THRESH,
    'ADMISSIBLE_REL_TOL': ADMISSIBLE_REL_TOL,
    'classification': {n: v for n, (v, _) in classification.items()},
    'admissible_count': admissible_count,
    'excluded_count': excluded_count,
    'verdict_value': verdict_value,
    'verdict': verdict,
    'scheme': 'Mellin-Plancherel',
    'convention': 's_KO=6',
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}

closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

four_tuple = (                                              # (local)
    f"(admissible_count={admissible_count}/5, "
    f"scheme=Mellin-Plancherel, convention=s_KO=6, L_max=N/A)"
)
print(f"  Closure SHA-256 (64 char): {closure_sha}")
print(f"  4-TUPLE: {four_tuple}")
assert len(closure_sha) == 64, "closure SHA must be full 64-char hexdigest"

# ============================================================
# SECTION 10: Save .npz
# ============================================================
print("\n[SEC 10] Saving data")
out_npz = HERE / 's83_w2_g27_mp_admissibility_unified.npz'  # (local)

np.savez(
    out_npz,
    s_KO=s_KO,
    R_SCAN=np.array(R_SCAN),
    classes=np.array(list(CLASSES.keys())),
    mellin_scan=np.array([mellin_scan[n] for n in CLASSES.keys()]),
    classification=np.array([classification[n][0] for n in CLASSES.keys()]),
    classification_reason=np.array(
        [classification[n][1] for n in CLASSES.keys()]),
    step_analytic=step_analytic,
    step_numeric=step_numeric,
    step_dev=step_dev,
    sumexp_analytic=sumexp_analytic,
    sumexp_numeric=sumexp_numeric,
    sumexp_dev_abs=sumexp_dev_abs,
    sumexp_dev_rel=sumexp_dev_rel,
    L_test=L_test,
    expected_L_multiplier=expected_L_multiplier,
    L_inv_admissible=np.array(
        [L_inv_results[n][0] if L_inv_results[n][0] is not None else np.nan
         for n in CLASSES.keys()]),
    L_inv_dev=np.array(
        [L_inv_results[n][1] if L_inv_results[n][1] is not None else np.nan
         for n in CLASSES.keys()]),
    admissible_count=admissible_count,
    excluded_count=excluded_count,
    verdict_value=verdict_value,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    input_shas=np.array(
        [f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 11: PNG diagnostic
# ============================================================
print("\n[SEC 11] Saving PNG diagnostic")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Left: R-scan |M(R)| (log-log)
colors = {'log': 'C0', 'step': 'C1', 'fractional': 'C2',
          'sum_exp': 'C3', 'oscillatory': 'C4'}              # (local)
for name in CLASSES:
    vals = np.abs(mellin_scan[name])                        # (local)
    ax1.semilogy(R_SCAN, np.maximum(vals, 1e-20), 'o-',
                 color=colors[name], label=f"{name} [{classification[name][0]}]")
ax1.set_xlabel("R (upper integration limit)")
ax1.set_ylabel("|M[f](s=6)| truncated to [eps, R]")
ax1.set_title("R-scan: bounded -> admissible; unbounded -> excluded")
ax1.legend(loc='best', fontsize=9)
ax1.grid(True, alpha=0.3)

# Right: classification bar chart
names = list(CLASSES.keys())                                # (local)
admit_bool = np.array([classification[n][0] == 'ADMISSIBLE'
                       for n in names]).astype(float)       # (local)
bar_colors = ['#2ca02c' if a else '#d62728' for a in admit_bool]  # (local)
ax2.bar(names, admit_bool, color=bar_colors)
ax2.set_ylim(0, 1.2)
ax2.set_ylabel("MP-admissible (1 = yes)")
ax2.set_title(f"Admissible count: {admissible_count}/5  (verdict: {verdict})")
ax2.axhline(0.5, color='gray', linestyle='--', alpha=0.5)
for i, n in enumerate(names):
    label = classification[n][0]                            # (local)
    ax2.text(i, admit_bool[i] + 0.05, label, ha='center',
             fontsize=9, color=bar_colors[i])

fig.suptitle("S83 W2-G27: MP-Admissibility at s_KO = 6 (5 function classes)")
fig.tight_layout()
out_png = HERE / 's83_w2_g27_mp_admissibility_unified.png'  # (local)
fig.savefig(out_png, dpi=120)
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 12: Append verdict to s83_gate_verdicts.txt
# ============================================================
print("\n[SEC 12] Append verdict to s83_gate_verdicts.txt")
verdicts_path = HERE / 's83_gate_verdicts.txt'              # (local)
verdict_line = (                                            # (local)
    f"S83-MP-ADMISSIBILITY-UNIFIED: {verdict} -- "
    f"value={verdict_value} "
    f"admissible_count={admissible_count}/5 "
    f"scheme=Mellin-Plancherel "
    f"convention=s_KO=6 "
    f"L_max=N/A "
    f"sha256={closure_sha}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _fh:
    _fh.write(verdict_line)
print(f"  Appended: {verdict_line.strip()}")

# ============================================================
# SECTION 13: Summary
# ============================================================
print("\n" + "=" * 72)
print(f"Summary  |  S83-MP-ADMISSIBILITY-UNIFIED  |  {verdict} "
      f"(value={verdict_value})")
print("=" * 72)
print(f"  Admissible classes : "
      f"{[n for n, (v, _) in classification.items() if v == 'ADMISSIBLE']}")
print(f"  Excluded classes   : "
      f"{[n for n, (v, _) in classification.items() if v == 'EXCLUDED']}")
print(f"  Closed-form match  : step dev {step_dev:.2e}, "
      f"sum_exp rel {sumexp_dev_rel:.2e}")
print(f"  L-invariance tests : {L_inv_results}")
print(f"  Closure SHA-256    : {closure_sha}")
print(f"  4-tuple            : {four_tuple}")
print("=" * 72)
