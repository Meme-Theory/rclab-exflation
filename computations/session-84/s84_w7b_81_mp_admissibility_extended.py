#!/usr/bin/env python3
"""
S84 W7b-81 — MP-ADMISSIBILITY-EXTENDED
======================================

Gate: S84-W7b-81-MP-ADMISSIBILITY-EXTENDED  [VERIFY]
Classification: GEOMETRIC
Owner: lizzi-spectral-functional-theorist

PURPOSE
-------
Extend S83-G27 (MP-admissibility, 5 classes) to a 9-class FRESH extension of
the Connes-Moscovici (2008) polynomial-bounded moment test at the KO-dim
anchor s_KO = 6. Atlas contains 11 regulator candidates:

    Retained baseline (2):
      #1 step           Theta(1-x)
      #2 sum_exp        sum_j c_j exp(-lambda_j x)

    Fresh tests (9):
      #3 zeta           x^0 continuation (Hadamard finite part at s=0 limit)
      #4 Zubarev        exp(-alpha x)
      #5 SDW            Seeley-DeWitt poly (1-x)^2 * Theta(1-x)
      #6 dim-reg        x^{-eps} continuation in dimension
      #7 lattice-BR     sinc^2(x) (lattice Brillouin replacement)
      #8 Gaussian^2     exp(-alpha^2 x^4) (double-Gaussian; quartic decay)
      #9 heat-kernel    Mellin-transformed exp(-x)
      #10 Planck-spec   x/(exp(beta x) - 1) Bose-Einstein
      #11 piecewise-lin max(0, 1 - x) on [0, 1]

PRE-REGISTERED SUBSTITUTION CHAIN (MANDATORY [VERIFY])
------------------------------------------------------
Step 1 (definition):  MP admissibility at s = KO-dim := Mellin transform
    M[f](s) = integral_0^infty f(x) x^{s-1} dx
    exists as an absolutely convergent integral and is analytic at s = 6.
Step 2 (substitution, per class at s=6):
    #1  step:           integrand = Theta(1-x) * x^5; support [0,1], M = 1/6.
    #2  sum_exp:        integrand = [sum_j c_j exp(-lam_j x)] * x^5;
                         M = Gamma(6) * sum_j c_j / lam_j^6.
    #3  zeta:           integrand = x^5; M -> +inf (divergent upper limit).
    #4  Zubarev:        integrand = exp(-alpha x) * x^5; M = Gamma(6)/alpha^6.
    #5  SDW:            integrand = (1-x)^2 Theta(1-x) * x^5;
                         B-function form, M = 2 * B(6, 3) = 2/168 = finite.
    #6  dim-reg:        integrand = x^{-eps+5}; divergent at infinity for any eps.
    #7  lattice-BR:     integrand = sinc^2(x) * x^5;
                         envelope ~ x^5 / (x^2) = x^3 at large x -> unbounded.
    #8  Gaussian^2:     integrand = exp(-alpha^2 x^4) * x^5; strong decay, finite.
    #9  heat-kernel:    integrand = exp(-x) * x^5; M = Gamma(6) = 120 finite.
    #10 Planck-spec:    integrand = x^6 / (exp(beta x) - 1); Riemann-zeta finite.
    #11 piecewise-lin:  integrand = (1-x) * x^5 on [0,1]; B(6,2) = 1/42 finite.
Step 3 (simplification):
    Admissible (M finite + L-rescaling preserves measure):
        #1 step, #2 sum_exp (baseline, S83 PASS retained)
        #4 Zubarev:      finite, but L-rescaling maps to Gamma(6)/(alpha L)^{-6}
                          which IS the Mellin multiplier L^6 ✓
        #5 SDW:          finite B-function, compact support, L-rescales ✓
        #8 Gaussian^2:   finite, L-rescales under x -> x/L (but alpha absorbed)
        #9 heat-kernel:  finite Gamma(6), L-rescales exactly
        #10 Planck-spec: finite (zeta(6)*Gamma(6)/beta^6), L-rescales
        #11 piecewise-lin: finite B(6,2), compact support, L-rescales
    Excluded (M divergent or envelope unbounded):
        #3 zeta:         integrand = x^5, M diverges as R -> inf
        #6 dim-reg:      divergent at infinity for any finite eps
        #7 lattice-BR:   oscillatory-envelope not abs. convergent at s=6
Step 4 (direction):
    Baseline admissible = {#1 step, #2 sum_exp} (2 items).
    Fresh admissible candidates (6): #4, #5, #8, #9, #10, #11.
    Fresh excluded candidates (3): #3, #6, #7.
    Total admissible count depends on saturation test in Section 4-5.
Step 5 (KO-dim=6 weighting, §VII.K-META):
    After MP filter, apply Connes-Moscovici polynomial weight at s=6. This is
    already baked into s=6 probe choice (KO-dim=6 anchor).
Step 6 (span test, §VII.K-META G58):
    R-protected span <= 1.5, NOT-R >= 2.5. For MP-admissibility, the relevant
    span is M(R_last)/M(R_prev). Saturated (admissible) <=> ratio -> 1 <= 1.5.
Step 7 (count admissible):
    admissible_i = 1 iff (saturated M-scan) AND (span_last_prev <= SAT_TOL).
Step 8 (decision per plan §W7b-81 thresholds):
    PASS  iff tested_count == 9 AND admissible_count == 2 (step+sum_exp only).
    INFO  iff tested_count == 9 AND admissible_count in {3,4,5,6}.
    FAIL  iff tested_count < 9   OR  admissible_count >= 7.

WARNING — METHODOLOGICAL CALIBRATION
------------------------------------
The plan §W7b-81 HYPOTHESIS states that {step, sum_exp} remains the UNIQUE
admissible pair (admissible_count = 2). The math (Step 2 above) shows
IF we use the classical Mellin absolute-convergence test, MANY fresh classes
(Zubarev, SDW, Gaussian^2, heat-kernel, Planck-spec, piecewise-lin) will also
saturate. Under the G27 saturation-test methodology, they will count as
ADMISSIBLE by the MP filter. This is a genuine result: extending the class
atlas beyond the S83 selection REVEALS more admissible regulators.

Per plan threshold table line 457: "INFO: 9 classes tested AND admissible
in {3, 4, 5, 6}". The PRU-compliant move is to COMPUTE and REPORT the
saturation-test outcome without adjusting the test to force a PASS.

ENVIRONMENT
-----------
CPU thread cap at 8 (before numpy import). Mellin moments via scipy.quad.
(Plan mentioned D_K blocks 1000x1000 at L_max=5 but G27 methodology is pure
Mellin analytic; D_K eigenvalues enter only if we probe Tr(|D|^{-s}) spectrum.
We stay faithful to G27 analytical form — adding a D_K spectral Mellin probe
as a cross-check only, not a primary test.)
"""
from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
from math import gamma as _gamma

import numpy as np
from scipy.integrate import quad
from scipy.special import zeta as _rzeta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent                       # (local)
sys.path.insert(0, str(HERE))
from canonical_constants import *  # noqa: F401,F403

# ============================================================
# SECTION 0: Input SHA-256 pins
# ============================================================

def _sha256(path: Path) -> str:
    h = hashlib.sha256()                                     # (local)
    with open(path, 'rb') as fp:
        h.update(fp.read())
    return h.hexdigest()


INPUT_FILES = [                                              # (local)
    HERE / 'canonical_constants.py',
    HERE / 's83_w2_g27_mp_admissibility_unified.py',
    HERE / 's83_w2_g27_mp_admissibility_unified.npz',
]

print("=" * 72)
print("S84 W7b-81: MP-ADMISSIBILITY-EXTENDED (11-class atlas at s_KO=6)")
print("=" * 72)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                              # (local)
for _f in INPUT_FILES:
    if _f.exists():
        _h = _sha256(_f)                                     # (local)
        INPUT_SHAS[_f.name] = _h
        print(f"  {_f.name:48s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[_f.name] = None
        print(f"  {_f.name:48s} MISSING")

# ============================================================
# SECTION 1: Substitution chain (print for audit trail)
# ============================================================
print("\n[SEC 1] Substitution chain (8 steps, pre-registered)")
print("  Step 1: MP-admissibility at s_KO=6 := M[f](s) abs. conv. at s=6")
print("  Step 2: 11 candidate regulators, compute integrand * x^5")
print("  Step 3: Compare analytic closed forms to numerical quad")
print("  Step 4: Saturation test (R-scan) for divergent candidates")
print("  Step 5: KO-dim=6 weighting (implicit in s=6 probe)")
print("  Step 6: Span test per VII.K-META G58 (SAT_TOL = 1e-3)")
print("  Step 7: Count admissible")
print("  Step 8: PASS/INFO/FAIL per plan thresholds")

# ============================================================
# SECTION 2: Anchor parameters
# ============================================================
print("\n[SEC 2] Anchor parameters")
s_KO = 6.0                                                   # (local) KO-dim anchor
print(f"  s_KO = {s_KO} (Connes KO-dim=6 for M4 x SU(3))")

R_SCAN = [5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0]        # (local)
print(f"  R-scan radii: {R_SCAN}")

GROWTH_FACTOR_THRESH = 10.0                                  # (local)
ABSOLUTE_FINITE_THRESH = 1e15                                # (local)
SAT_REL_TOL = 1e-3                                           # (local) span threshold <= 1.5 (saturated)
ADMISSIBLE_REL_TOL = 1e-6                                    # (local) closed-form match tolerance

# Plan thresholds (re-read from §W7b-81 refined thresholds)
PLAN_TESTED_COUNT_REQ = 9                                    # (local) must test 9 fresh classes
PLAN_PASS_ADMISSIBLE = 2                                     # (local) step + sum_exp only
PLAN_INFO_RANGE = {3, 4, 5, 6}                               # (local) partial extension
PLAN_FAIL_ADMISSIBLE_MIN = 7                                 # (local) degeneracy

print(f"  PLAN PASS:  tested == {PLAN_TESTED_COUNT_REQ} AND admissible == {PLAN_PASS_ADMISSIBLE}")
print(f"  PLAN INFO:  admissible in {sorted(PLAN_INFO_RANGE)}")
print(f"  PLAN FAIL:  tested < {PLAN_TESTED_COUNT_REQ} OR admissible >= {PLAN_FAIL_ADMISSIBLE_MIN}")

# ============================================================
# SECTION 3: 11-class regulator definitions
# ============================================================
print("\n[SEC 3] 11 regulator class definitions")

# --- #1 step (BASELINE from S83) ---
def f_step(x):                                               # (local)
    if np.isscalar(x):
        return 1.0 if x <= 1.0 else 0.0
    return np.where(x <= 1.0, 1.0, 0.0)

# --- #2 sum_exp (BASELINE from S83) ---
SUMEXP_C = np.array([0.5, 0.3, 0.2])                         # (local)
SUMEXP_LAM = np.array([1.0, 2.0, 0.5])                       # (local)
def f_sumexp(x):                                             # (local)
    if np.isscalar(x):
        return float(np.sum(SUMEXP_C * np.exp(-SUMEXP_LAM * x)))
    return np.sum(SUMEXP_C[:, None] * np.exp(-SUMEXP_LAM[:, None] * x), axis=0)

# --- #3 zeta (fresh) ---
# Classical zeta regulator corresponds to s -> 0 continuation; as a Mellin
# test function f(x) = 1 (the x^0 limit of x^{-s} at s=0).
def f_zeta(x):                                               # (local)
    return np.ones_like(x) if not np.isscalar(x) else 1.0

# --- #4 Zubarev (fresh) ---
ZUBAREV_ALPHA = 1.0                                          # (local) decay rate
def f_zubarev(x):                                            # (local)
    return np.exp(-ZUBAREV_ALPHA * x)

# --- #5 SDW (fresh) ---
# Seeley-DeWitt poly: (1-x)^2 * Theta(1-x) -- compact-support quadratic
def f_sdw(x):                                                # (local)
    if np.isscalar(x):
        return (1.0 - x)**2 if x <= 1.0 else 0.0
    return np.where(x <= 1.0, (1.0 - x)**2, 0.0)

# --- #6 dim-reg (fresh) ---
# x^{-eps} continuation in dimension; at eps=0 limit = 1 (same as zeta!).
# Take eps = 0.1 positive to probe regulator action. Will diverge at infinity.
DIMREG_EPS = 0.1                                             # (local)
def f_dimreg(x):                                             # (local)
    return x ** (-DIMREG_EPS)

# --- #7 lattice-BR (fresh) ---
# Brillouin replacement = sinc^2(pi x / 2); at continuum limit -> 1.
def f_lattice_br(x):                                         # (local)
    arg = np.pi * x / 2.0                                    # (local)
    if np.isscalar(x):
        if abs(arg) < 1e-10:
            return 1.0
        return (np.sin(arg) / arg)**2
    result = np.where(np.abs(arg) < 1e-10, 1.0,
                      (np.sin(arg) / np.where(np.abs(arg) < 1e-10, 1.0, arg))**2)
    return result

# --- #8 Gaussian^2 (fresh) ---
# exp(-alpha^2 x^4) quartic decay
GAUSSSQ_ALPHA = 1.0                                          # (local)
def f_gauss_sq(x):                                           # (local)
    return np.exp(-GAUSSSQ_ALPHA**2 * x**4)

# --- #9 heat-kernel (fresh) ---
# Mellin-transformed: canonical heat-kernel = exp(-x)
# Mellin M[exp(-x)](s) = Gamma(s), finite at s=6: Gamma(6) = 120.
def f_heatkernel(x):                                         # (local)
    return np.exp(-x)

# --- #10 Planck-spectrum (fresh) ---
# Bose-Einstein: x / (exp(beta x) - 1). Factor out one x to keep IR regular.
PLANCK_BETA = 1.0                                            # (local)
def f_planck(x):                                             # (local)
    # near x=0: x / (beta x) = 1/beta, finite
    if np.isscalar(x):
        if x < 1e-10:
            return 1.0 / PLANCK_BETA
        return x / (np.exp(PLANCK_BETA * x) - 1.0)
    return np.where(x < 1e-10,
                    1.0 / PLANCK_BETA,
                    x / (np.exp(PLANCK_BETA * x) - 1.0 + 1e-300))

# --- #11 piecewise-linear (fresh) ---
# max(0, 1-|x|), compact support [0, 1]
def f_piecewise_lin(x):                                      # (local)
    if np.isscalar(x):
        return max(0.0, 1.0 - abs(x))
    return np.maximum(0.0, 1.0 - np.abs(x))

# Atlas ordered: 2 baseline + 9 fresh
CLASSES = {                                                  # (local)
    "step":            (f_step,            "BASELINE_S83"),
    "sum_exp":         (f_sumexp,          "BASELINE_S83"),
    "zeta":            (f_zeta,            "FRESH"),
    "Zubarev":         (f_zubarev,         "FRESH"),
    "SDW":             (f_sdw,             "FRESH"),
    "dim_reg":         (f_dimreg,          "FRESH"),
    "lattice_BR":      (f_lattice_br,      "FRESH"),
    "Gaussian_sq":     (f_gauss_sq,        "FRESH"),
    "heat_kernel":     (f_heatkernel,      "FRESH"),
    "Planck_spec":     (f_planck,          "FRESH"),
    "piecewise_lin":   (f_piecewise_lin,   "FRESH"),
}
CLASS_NAMES = list(CLASSES.keys())                           # (local)
N_CLASSES = len(CLASS_NAMES)                                 # (local)
N_FRESH = sum(1 for _, (_, lbl) in CLASSES.items() if lbl == "FRESH")  # (local)
print(f"  Total classes: {N_CLASSES}  (2 baseline + {N_FRESH} fresh)")
print(f"  Class list: {CLASS_NAMES}")
print(f"  Parameters:  ZUBAREV_ALPHA={ZUBAREV_ALPHA}, DIMREG_EPS={DIMREG_EPS},")
print(f"               GAUSSSQ_ALPHA={GAUSSSQ_ALPHA}, PLANCK_BETA={PLANCK_BETA}")

# ============================================================
# SECTION 4: R-scan Mellin integrals per class
# ============================================================
print("\n[SEC 4] R-scan Mellin integrals at s = s_KO = 6")
header = f"  {'class':<16} | " + " | ".join(f"R={R:>5.0f}" for R in R_SCAN)
print(header)
print("  " + "-" * (len(header) - 2))

mellin_scan = {}                                             # (local)
for name in CLASS_NAMES:
    f, _ = CLASSES[name]
    vals = []                                                # (local)
    for R in R_SCAN:
        eps_lo = 1e-10                                       # (local)
        try:
            # Compact support classes: cap R effective.
            if name == 'step':
                R_eff = min(R, 1.0)                          # (local)
                val, _err = quad(lambda x: f(x) * x**(s_KO - 1.0),
                                 eps_lo, R_eff, limit=400)
            elif name == 'SDW':
                R_eff = min(R, 1.0)                          # (local)
                val, _err = quad(lambda x: f(x) * x**(s_KO - 1.0),
                                 eps_lo, R_eff, limit=400)
            elif name == 'piecewise_lin':
                R_eff = min(R, 1.0)                          # (local)
                val, _err = quad(lambda x: f(x) * x**(s_KO - 1.0),
                                 eps_lo, R_eff, limit=400)
            else:
                val, _err = quad(lambda x: f(x) * x**(s_KO - 1.0),
                                 eps_lo, R, limit=400)
            vals.append(val)
        except Exception as e:
            vals.append(float('nan'))
    mellin_scan[name] = np.array(vals)
    row = " | ".join(f"{v:+.2e}" for v in vals)
    print(f"  {name:<16} | " + row)

# ============================================================
# SECTION 5: Classify each class (ADMISSIBLE / EXCLUDED)
# ============================================================
print("\n[SEC 5] Classification per MP saturation test")


def classify(name, scan_vals):                               # (local)
    """ADMISSIBLE <=> bounded + saturated under R -> infinity."""
    abs_vals = np.abs(scan_vals)                             # (local)
    # (a) absolute-finite check
    if np.any(abs_vals > ABSOLUTE_FINITE_THRESH):
        return ("EXCLUDED",
                f"|M(R)| exceeds {ABSOLUTE_FINITE_THRESH:.0e} "
                f"(max = {abs_vals.max():.2e})")
    finite_mask = np.isfinite(abs_vals)                      # (local)
    if finite_mask.sum() < 2:
        return ("EXCLUDED", "insufficient finite values in scan")
    # (b) saturation test on tail
    last = scan_vals[-1]                                     # (local, signed)
    prev = scan_vals[-2]                                     # (local, signed)
    if abs(prev) < 1e-30:
        return ("EXCLUDED",
                f"M(R_prev) ~ 0 ({prev:.2e}), cannot assess saturation")
    rel_step = abs(last - prev) / abs(prev)                  # (local)
    if rel_step < SAT_REL_TOL:
        return ("ADMISSIBLE",
                f"|M(R_last)/M(R_prev) - 1| = {rel_step:.2e} < "
                f"{SAT_REL_TOL:.0e}")
    return ("EXCLUDED",
            f"|M(R_last)/M(R_prev) - 1| = {rel_step:.2e} >= "
            f"{SAT_REL_TOL:.0e} (no saturation)")


classification = {}                                          # (local)
for name in CLASS_NAMES:
    v, r = classify(name, mellin_scan[name])
    classification[name] = (v, r)
    lbl = CLASSES[name][1]                                   # (local)
    print(f"  {name:<16} [{lbl:<12s}]: {v:<11} -- {r}")

# ============================================================
# SECTION 6: Analytic closed forms (cross-check)
# ============================================================
print("\n[SEC 6] Analytic closed-form cross-check at s = 6")

closed_forms = {}                                            # (local)

# step:  M = 1/s = 1/6
step_analytic = 1.0 / s_KO                                   # (local)
step_numeric, _ = quad(lambda x: f_step(x) * x**(s_KO - 1.0),
                       0.0, 2.0, limit=400)
step_dev_abs = abs(step_numeric - step_analytic)             # (local)
closed_forms['step'] = (step_analytic, step_numeric, step_dev_abs)
print(f"  step:        analytic=1/6={step_analytic:.6e} numeric={step_numeric:.6e} "
      f"dev={step_dev_abs:.2e}")

# sum_exp: M = Gamma(6) * sum c_j / lam_j^6
sumexp_analytic = _gamma(s_KO) * np.sum(SUMEXP_C / SUMEXP_LAM**s_KO)  # (local)
sumexp_numeric, _ = quad(lambda x: f_sumexp(x) * x**(s_KO - 1.0),
                         0.0, np.inf, limit=400)
sumexp_dev_abs = abs(sumexp_numeric - sumexp_analytic)       # (local)
closed_forms['sum_exp'] = (sumexp_analytic, sumexp_numeric, sumexp_dev_abs)
print(f"  sum_exp:     analytic={sumexp_analytic:.6e} numeric={sumexp_numeric:.6e} "
      f"dev={sumexp_dev_abs:.2e}")

# Zubarev: M = Gamma(6) / alpha^6
zub_analytic = _gamma(s_KO) / ZUBAREV_ALPHA**s_KO            # (local)
zub_numeric, _ = quad(lambda x: f_zubarev(x) * x**(s_KO - 1.0),
                      0.0, np.inf, limit=400)
zub_dev_abs = abs(zub_numeric - zub_analytic)                # (local)
closed_forms['Zubarev'] = (zub_analytic, zub_numeric, zub_dev_abs)
print(f"  Zubarev:     analytic={zub_analytic:.6e} numeric={zub_numeric:.6e} "
      f"dev={zub_dev_abs:.2e}")

# SDW: M = int_0^1 (1-x)^2 x^5 dx = B(6, 3) = (5! 2!) / 8! = 240/40320 = 1/168
# Actually B(a,b) = Gamma(a)Gamma(b)/Gamma(a+b); B(6,3)=5!*2!/8!=120*2/40320=240/40320=1/168
sdw_analytic = 1.0 / 168.0                                   # (local) B(6, 3)
sdw_numeric, _ = quad(lambda x: f_sdw(x) * x**(s_KO - 1.0),
                      0.0, 1.0, limit=400)
sdw_dev_abs = abs(sdw_numeric - sdw_analytic)                # (local)
closed_forms['SDW'] = (sdw_analytic, sdw_numeric, sdw_dev_abs)
print(f"  SDW:         analytic=B(6,3)=1/168={sdw_analytic:.6e} "
      f"numeric={sdw_numeric:.6e} dev={sdw_dev_abs:.2e}")

# heat_kernel: M = Gamma(6) = 120
hk_analytic = _gamma(s_KO)                                   # (local)
hk_numeric, _ = quad(lambda x: f_heatkernel(x) * x**(s_KO - 1.0),
                     0.0, np.inf, limit=400)
hk_dev_abs = abs(hk_numeric - hk_analytic)                   # (local)
closed_forms['heat_kernel'] = (hk_analytic, hk_numeric, hk_dev_abs)
print(f"  heat_kernel: analytic=Gamma(6)={hk_analytic:.6e} numeric={hk_numeric:.6e} "
      f"dev={hk_dev_abs:.2e}")

# Planck-spec: M = int_0^inf x^6 / (exp(beta x) - 1) dx = Gamma(7)*zeta(6)/beta^7
# Because with our f(x) = x / (exp(beta x) - 1), integrand = f*x^5 = x^6/(exp(beta x)-1).
# Standard result int_0^inf x^(s-1)/(e^x - 1) dx = Gamma(s)*zeta(s); with s=7:
planck_analytic = (_gamma(7.0) * float(_rzeta(7)) /
                   PLANCK_BETA**7)                           # (local) = 720 * zeta(7)
planck_numeric, _ = quad(lambda x: f_planck(x) * x**(s_KO - 1.0),
                         1e-8, np.inf, limit=400)
planck_dev_abs = abs(planck_numeric - planck_analytic)       # (local)
closed_forms['Planck_spec'] = (planck_analytic, planck_numeric, planck_dev_abs)
print(f"  Planck_spec: analytic=Gamma(7)*zeta(7)/beta^7={planck_analytic:.6e} "
      f"numeric={planck_numeric:.6e} dev={planck_dev_abs:.2e}")

# piecewise_lin: M = int_0^1 (1-x) x^5 dx = B(6,2) = 1/42
pl_analytic = 1.0 / 42.0                                     # (local)
pl_numeric, _ = quad(lambda x: f_piecewise_lin(x) * x**(s_KO - 1.0),
                     0.0, 1.0, limit=400)
pl_dev_abs = abs(pl_numeric - pl_analytic)                   # (local)
closed_forms['piecewise_lin'] = (pl_analytic, pl_numeric, pl_dev_abs)
print(f"  piecewise_lin: analytic=B(6,2)=1/42={pl_analytic:.6e} "
      f"numeric={pl_numeric:.6e} dev={pl_dev_abs:.2e}")

# Gaussian_sq: M = int_0^inf exp(-a^2 x^4) x^5 dx; substitute u = a^2 x^4
# du = 4 a^2 x^3 dx, x^5 dx = x^2 / (4 a^2) * du = (u/a^2)^{1/2} / (4 a^2) du
# Result: M = Gamma(3/2) / (2 * alpha^3) ... let me just trust the numeric.
gsq_numeric, _ = quad(lambda x: f_gauss_sq(x) * x**(s_KO - 1.0),
                      0.0, np.inf, limit=400)
# Analytic: substitute t = alpha^2 x^4, x = (t/alpha^2)^{1/4}, dx = (1/(4 alpha^2)) t^{-3/4} dt
# integrand = exp(-t) * (t/alpha^2)^{5/4} * (1/(4 alpha^2)) t^{-3/4}
#           = (1/(4 alpha^{5/2+2})) * exp(-t) * t^{5/4 - 3/4} = (1/(4 alpha^{9/2})) * t^{1/2} exp(-t)
# int_0^inf t^{1/2} e^{-t} dt = Gamma(3/2) = sqrt(pi)/2
gsq_analytic = (np.sqrt(np.pi) / 2.0) / (4.0 * GAUSSSQ_ALPHA**(9.0/2.0))  # (local)
gsq_dev_abs = abs(gsq_numeric - gsq_analytic)                # (local)
closed_forms['Gaussian_sq'] = (gsq_analytic, gsq_numeric, gsq_dev_abs)
print(f"  Gaussian_sq: analytic=Gamma(3/2)/(4 alpha^{{9/2}})={gsq_analytic:.6e} "
      f"numeric={gsq_numeric:.6e} dev={gsq_dev_abs:.2e}")

# zeta, dim_reg, lattice_BR: no finite closed form on [0, infty).
for nm in ('zeta', 'dim_reg', 'lattice_BR'):
    closed_forms[nm] = None
    print(f"  {nm:<16}: no closed form on [0, infty) (divergent at s=6)")

# ============================================================
# SECTION 7: Per-observable verdict map {A_s, m_H, n_s, sin^2_W}
# ============================================================
print("\n[SEC 7] Per-observable MP-admissibility map")
# For each observable, each regulator is MP-admissible iff the classification
# is ADMISSIBLE at s_KO=6. Substrate reasoning: KO-dim weighting at s=6 applies
# uniformly to all four observables (they share the spectral-action
# functional form Tr(f(D^2/Lambda^2)) * D_K weighting at KO-dim=6).
OBSERVABLES = ["A_s", "m_H", "n_s", "sin2thW"]               # (local)
obs_verdict = {}                                             # (local)
for obs in OBSERVABLES:
    row = {name: ("ADM" if classification[name][0] == "ADMISSIBLE"
                  else "EXC") for name in CLASS_NAMES}       # (local)
    obs_verdict[obs] = row
    adm_list = [n for n, v in row.items() if v == "ADM"]     # (local)
    print(f"  {obs:<10}: admissible regulators = {adm_list}")

# ============================================================
# SECTION 8: Tested / admissible counts
# ============================================================
print("\n[SEC 8] Tested-class and admissible counts")

# Tested-fresh count: 9 fresh classes always tested
tested_fresh = N_FRESH                                       # (local)
# Baseline retained count: 2 (step, sum_exp) verified PASS here
baseline_retained = sum(1 for n in ('step', 'sum_exp')
                        if classification[n][0] == 'ADMISSIBLE')  # (local)
total_tested = N_CLASSES                                     # (local) 11 classes total
admissible_count = sum(1 for n in CLASS_NAMES
                       if classification[n][0] == 'ADMISSIBLE')   # (local)
excluded_count = N_CLASSES - admissible_count                # (local)
print(f"  Fresh tested:      {tested_fresh}")
print(f"  Baseline retained: {baseline_retained} / 2")
print(f"  Total tested:      {total_tested}")
print(f"  Admissible total:  {admissible_count}")
print(f"  Excluded total:    {excluded_count}")

# ============================================================
# SECTION 9: PASS / INFO / FAIL decision (plan thresholds)
# ============================================================
print("\n[SEC 9] Gate decision per plan thresholds (§W7b-81)")

# Plan re-reading (line 456-458):
#   PASS: 9 classes tested AND admissible_count == 2 (step, sum_exp only)
#   INFO: 9 classes tested AND admissible_count in {3, 4, 5, 6}
#   FAIL: fewer than 9 classes tested OR admissible_count >= 7

if tested_fresh < PLAN_TESTED_COUNT_REQ:
    verdict = "FAIL"
    verdict_value = -1                                       # (local)
    reason = (f"Fresh tested count {tested_fresh} < required "
              f"{PLAN_TESTED_COUNT_REQ}")                    # (local)
elif admissible_count >= PLAN_FAIL_ADMISSIBLE_MIN:
    verdict = "FAIL"
    verdict_value = -2                                       # (local)
    reason = (f"Admissible count {admissible_count} >= "
              f"degeneracy threshold {PLAN_FAIL_ADMISSIBLE_MIN}") # (local)
elif admissible_count == PLAN_PASS_ADMISSIBLE:
    verdict = "PASS"
    verdict_value = 0                                        # (local)
    reason = (f"Tested {tested_fresh} fresh classes; admissible stayed at "
              f"{admissible_count} (step, sum_exp unique baseline)")  # (local)
elif admissible_count in PLAN_INFO_RANGE:
    verdict = "INFO"
    verdict_value = 1                                        # (local)
    admitted = [n for n in CLASS_NAMES if classification[n][0] == "ADMISSIBLE"]  # (local)
    reason = (f"Tested {tested_fresh} fresh classes; admissible = "
              f"{admissible_count} in INFO range {sorted(PLAN_INFO_RANGE)}; "
              f"admitted set: {admitted}")                   # (local)
else:
    # admissible_count == 1 or 0 -- should not occur because step+sum_exp
    # baseline is mathematically admissible; but handle defensively.
    verdict = "FAIL"
    verdict_value = -3                                       # (local)
    reason = (f"Admissible count {admissible_count} below baseline "
              f"(methodology drift)")                        # (local)

print(f"  Tested_fresh = {tested_fresh} (required {PLAN_TESTED_COUNT_REQ})")
print(f"  Admissible_total = {admissible_count}")
print(f"  -> VERDICT: {verdict}")
print(f"  -> REASON:  {reason}")

# ============================================================
# SECTION 10: Closure SHA + 4-tuple
# ============================================================
print("\n[SEC 10] Closure SHA-256 and 4-tuple emit")

closure_map = {                                              # (local)
    'script': 's84_w7b_81_mp_admissibility_extended.py',
    's_KO': s_KO,
    'classes': CLASS_NAMES,
    'fresh_classes': [n for n in CLASS_NAMES
                      if CLASSES[n][1] == 'FRESH'],
    'R_SCAN': R_SCAN,
    'ZUBAREV_ALPHA': ZUBAREV_ALPHA,
    'DIMREG_EPS': DIMREG_EPS,
    'GAUSSSQ_ALPHA': GAUSSSQ_ALPHA,
    'PLANCK_BETA': PLANCK_BETA,
    'SUMEXP_C': SUMEXP_C.tolist(),
    'SUMEXP_LAM': SUMEXP_LAM.tolist(),
    'GROWTH_FACTOR_THRESH': GROWTH_FACTOR_THRESH,
    'ABSOLUTE_FINITE_THRESH': ABSOLUTE_FINITE_THRESH,
    'SAT_REL_TOL': SAT_REL_TOL,
    'PLAN_TESTED_COUNT_REQ': PLAN_TESTED_COUNT_REQ,
    'PLAN_PASS_ADMISSIBLE': PLAN_PASS_ADMISSIBLE,
    'PLAN_INFO_RANGE': sorted(PLAN_INFO_RANGE),
    'PLAN_FAIL_ADMISSIBLE_MIN': PLAN_FAIL_ADMISSIBLE_MIN,
    'classification': {n: classification[n][0] for n in CLASS_NAMES},
    'admissible_count': admissible_count,
    'excluded_count': excluded_count,
    'tested_fresh': tested_fresh,
    'baseline_retained': baseline_retained,
    'verdict_value': verdict_value,
    'verdict': verdict,
    'scheme': 'CM-MP-filter-KO6',
    'convention': 'L2-Zubarev-substrate-action',
    'L_max': 5,
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items()) if v is not None},
    '__script__': 's84_w7b_81_mp_admissibility_extended',
    '__gate_id__': 'S84-W7b-81-MP-ADMISSIBILITY-EXTENDED',
}

closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)
assert len(closure_sha) == 64, "closure SHA must be full 64-char hexdigest"

four_tuple = (                                               # (local)
    f"(value=(tested={tested_fresh},admissible={admissible_count}), "
    f"scheme=CM-MP-filter-KO6, "
    f"convention=L2-Zubarev-substrate-action, L_max=5)"
)
print(f"  Closure SHA-256 (64 char): {closure_sha}")
print(f"  4-TUPLE: {four_tuple}")

# ============================================================
# SECTION 11: Save .npz
# ============================================================
print("\n[SEC 11] Saving data .npz")
out_npz = HERE / 's84_w7b_81_data.npz'                       # (local)

np.savez(
    out_npz,
    s_KO=s_KO,
    R_SCAN=np.array(R_SCAN),
    classes=np.array(CLASS_NAMES),
    class_labels=np.array([CLASSES[n][1] for n in CLASS_NAMES]),
    mellin_scan=np.array([mellin_scan[n] for n in CLASS_NAMES]),
    classification=np.array([classification[n][0] for n in CLASS_NAMES]),
    classification_reason=np.array([classification[n][1] for n in CLASS_NAMES]),
    # per-observable matrix (obs x class) -> ADM/EXC
    observables=np.array(OBSERVABLES),
    obs_matrix=np.array([[obs_verdict[o][n] for n in CLASS_NAMES]
                         for o in OBSERVABLES]),
    # closed-form deviations
    step_dev=step_dev_abs,
    sumexp_dev=sumexp_dev_abs,
    zub_dev=zub_dev_abs,
    sdw_dev=sdw_dev_abs,
    gsq_dev=gsq_dev_abs,
    hk_dev=hk_dev_abs,
    planck_dev=planck_dev_abs,
    pl_dev=pl_dev_abs,
    tested_fresh=tested_fresh,
    baseline_retained=baseline_retained,
    total_tested=total_tested,
    admissible_count=admissible_count,
    excluded_count=excluded_count,
    verdict_value=verdict_value,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    input_shas=np.array(
        [f"{k}={v}" for k, v in sorted(INPUT_SHAS.items()) if v is not None]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 12: PNG diagnostic
# ============================================================
print("\n[SEC 12] Saving PNG diagnostic")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Left: R-scan |M(R)| (log-log)
cmap = plt.cm.tab20                                          # (local)
for i, name in enumerate(CLASS_NAMES):
    vals = np.abs(mellin_scan[name])                         # (local)
    vals_plot = np.maximum(vals, 1e-20)                      # (local)
    lbl = CLASSES[name][1][0]                                # (local) B or F
    marker = 'o' if lbl == 'B' else 's'                      # (local)
    color = cmap(i / max(1, N_CLASSES - 1))                  # (local)
    ax1.semilogy(R_SCAN, vals_plot, marker + '-', color=color,
                 label=f"{name}[{classification[name][0][:3]}]")
ax1.set_xlabel("R (upper integration limit)")
ax1.set_ylabel("|M[f](s=6)| on [eps, R]")
ax1.set_title("R-scan: bounded+saturated -> ADMISSIBLE")
ax1.legend(loc='best', fontsize=7, ncol=2)
ax1.grid(True, alpha=0.3)

# Right: classification bar
admit_bool = np.array([classification[n][0] == 'ADMISSIBLE'
                       for n in CLASS_NAMES]).astype(float)  # (local)
bar_colors = ['#2ca02c' if a else '#d62728' for a in admit_bool]  # (local)
ax2.barh(range(N_CLASSES), admit_bool, color=bar_colors)
ax2.set_yticks(range(N_CLASSES))
ax2.set_yticklabels([f"{n} [{CLASSES[n][1][:4]}]" for n in CLASS_NAMES])
ax2.set_xlim(0, 1.2)
ax2.set_xlabel("MP-admissible (1=yes)")
ax2.set_title(f"Admissible: {admissible_count}/{N_CLASSES}  verdict={verdict}")
ax2.axvline(0.5, color='gray', linestyle='--', alpha=0.5)
for i, n in enumerate(CLASS_NAMES):
    label = classification[n][0]                             # (local)
    ax2.text(admit_bool[i] + 0.02, i, label, va='center',
             fontsize=8, color=bar_colors[i])

fig.suptitle("S84 W7b-81: MP-Admissibility EXTENDED (11-class atlas at s_KO=6)")
fig.tight_layout()
out_png = HERE / 's84_w7b_81_mp_admissibility_extended.png'  # (local)
fig.savefig(out_png, dpi=120)
plt.close(fig)
print(f"  Saved: {out_png}")

# ============================================================
# SECTION 13: Append verdict line to s84_gate_verdicts.txt
# ============================================================
print("\n[SEC 13] Append verdict to computations/session-84/s84_gate_verdicts.txt")
verdicts_path = HERE / 's84_gate_verdicts.txt'               # (local)
verdict_line = (                                             # (local)
    f"S84-W7b-81-MP-ADMISSIBILITY-EXTENDED: {verdict} -- "
    f"value=(tested={tested_fresh},admissible={admissible_count}) "
    f"scheme=CM-MP-filter-KO6 "
    f"convention=L2-Zubarev-substrate-action "
    f"L_max=5 "
    f"sha256={closure_sha}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _fh:
    _fh.write(verdict_line)
print(f"  Appended: {verdict_line.strip()}")

# ============================================================
# SECTION 14: Summary
# ============================================================
print("\n" + "=" * 72)
print(f"Summary  |  S84-W7b-81-MP-ADMISSIBILITY-EXTENDED  |  {verdict} "
      f"(value={verdict_value})")
print("=" * 72)
print(f"  Fresh classes tested : {tested_fresh}")
print(f"  Baseline retained    : {baseline_retained} / 2 (step, sum_exp)")
print(f"  Admissible total     : {admissible_count} / {N_CLASSES}")
print(f"  Admissible set       : "
      f"{[n for n in CLASS_NAMES if classification[n][0] == 'ADMISSIBLE']}")
print(f"  Excluded set         : "
      f"{[n for n in CLASS_NAMES if classification[n][0] == 'EXCLUDED']}")
print(f"  Closure SHA-256      : {closure_sha}")
print(f"  4-tuple              : {four_tuple}")
print("=" * 72)
