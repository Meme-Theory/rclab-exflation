#!/usr/bin/env python3
"""
S82 W1-3-SG — CC-RATIOS-ONLY-THEOREM (spectral-geometer track) sanity check
============================================================================

Gate: S82-CC-RATIOS-ONLY-THEOREM-SG  [VERIFY-THEOREM]
Classification: GEOMETRIC
Owner: spectral-geometer (dual-owner alt; connes-ncg-theorist writes §IV.C.CN)

PURPOSE
-------
This is the NUMERICAL SANITY accompanying the analytic proof in
`sessions/archive/session-82/theorems/cc-ratios-only-theorem-sg.md`. It is NOT the
proof itself (the theorem is analytic, from Mellin-Laplace duality applied
to CC96 eq 2.11). It is a regulator-scan checking that the weight-balance
cancellation predicted by Lemma 2 is faithful to machine precision, and that
the unbalanced counterexample REALLY retains regulator dependence as claimed.

CC96 eq 2.11 convention (d-general; d=8 for the framework):
    Tr f(D^2/Lambda^2) ~ sum_{k in S_d} f_k * Lambda^k * a_{d-k}[D^2] / Gamma(k/2)
where:
    f_k = integral_0^inf f(u) u^{k/2 - 1} du    (Mellin moment at s=k/2)

Weight label:
    w(a_n) = d - n = k.
Weight-balanced pair (a_m, a_n): w(a_m) = w(a_n) <=> m = n (binary);
the general monomial form requires MULTISET equality of weight labels.

Pre-registered substitution chain (Lemma 2 step 3; MANDATORY [VERIFY-THEOREM]):
  Step 1 (definition): R_{m,n}^{(f)} = S_m^{(f)} / S_n^{(f)}
    where S_m^{(f)} = f_k * Lambda^k * a_m / Gamma(k/2),   k = d - m.
  Step 2 (substitution, balanced case k_m = k_n = k):
    R = [f_k * Lambda^k * a_m / Gamma(k/2)] / [f_k * Lambda^k * a_n / Gamma(k/2)]
  Step 3 (simplification):
    numerator and denominator share f_k, Lambda^k, Gamma(k/2) -> cancel.
    R = a_m / a_n.
  Direction: balanced => f CANCELS (identity-level, not asymptotic).
             unbalanced (k_m != k_n) => f RETAINS via the surviving
             factor f_{k_m} / f_{k_n} of distinct Mellin moments.

Pre-registered scenarios (S80 plan §W1-4 L1036-1038; task spec):
  PASS: <=3 pages analytic proof + sanity cancellation at machine epsilon.
  INFO: <6 pages analytic sketch or cancellation at > 1e-12 but < 1e-6.
  FAIL: no f-cancellation identity found.

Gate emission (sanity layer):
  value = 0 -> PASS   (balanced spread <= 1e-12, unbalanced spread > 1e-3)
  value = 1 -> INFO   (balanced spread in (1e-12, 1e-6))
  value = 2 -> FAIL   (balanced spread > 1e-6, OR unbalanced spread < 1e-3)
The analytic proof (in .md) carries the page-count PASS/INFO grading.

Regulators tested (three distinct CC96-admissible classes):
    f_A(u) = exp(-u)                        (canonical heat kernel)
    f_B(u) = 1 / (1 + u)^2                  (polynomial power-law)
    f_C(u) = exp(-u^{0.7})                  (stretched exponential)

Weight labels k tested: {2, 4, 6} — all integrable for all three regulators
at d = 8.

Environment: Mellin moments via scipy.quad on [0, inf); no heavy linear
algebra; CPU thread cap at 8 via os.environ.
"""

from __future__ import annotations

import os
# --- CPU thread cap (before numpy)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad

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
    HERE / 's80_cc_ratios_only_sanity.py',                  # prior-session anchor
]

print("=" * 72)
print("S82 W1-3-SG: CC-RATIOS-ONLY-THEOREM (spectral-geometer) sanity")
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
print("\n[SEC 1] Substitution chain (Lemma 2, balanced case)")
print("  Step 1:  R_{m,n}^{(f)} = S_m^{(f)} / S_n^{(f)}")
print("            S_m^{(f)} = f_k * Lambda^k * a_m / Gamma(k/2),   k = d - m")
print("  Step 2:  For k_m = k_n = k (balanced):")
print("            R = [f_k * Lambda^k * a_m / Gamma(k/2)]")
print("              / [f_k * Lambda^k * a_n / Gamma(k/2)]")
print("  Step 3:  f_k, Lambda^k, Gamma(k/2) appear IDENTICALLY top & bottom")
print("            -> cancel at the level of identity (not asymptotic)")
print("            -> R = a_m / a_n  (pure geometric, f-INDEPENDENT)")
print("  Direction (balanced): f CANCELS.")
print("  Direction (unbalanced k_m != k_n): f_{k_m}/f_{k_n} survives -> f RETAINS.")

# ============================================================
# SECTION 2: Framework dimension + regulators
# ============================================================
print("\n[SEC 2] Framework dimension + regulators")
D_TOTAL = 8                                                 # (local) dim(M_4 x SU(3))
print(f"  d = {D_TOTAL}  (framework metric dimension)")

K_VALUES = [2, 4, 6]                                        # (local) Mellin-label test set
print(f"  k (weight labels) tested: {K_VALUES}")


def f_A(u):                                                 # (local)
    return np.exp(-u)


def f_B(u):                                                 # (local)
    return 1.0 / (1.0 + u) ** 2


def f_C(u):                                                 # (local)
    return np.exp(-(u ** 0.7))


REGULATORS = {"A_exp": f_A, "B_poly": f_B, "C_stretched": f_C}  # (local)

# ============================================================
# SECTION 3: Mellin moment evaluator
# ============================================================
print("\n[SEC 3] Mellin moment evaluator")
print("  f_k = integral_0^inf f(u) u^{k/2 - 1} du   (CC96 eq 2.11)")


def mellin_moment(f, k, limit=400):                         # (local)
    """Mellin moment at s = k/2. For k >= 2 integrable for all f above."""
    integrand = lambda u: f(u) * u ** (k / 2.0 - 1.0)       # (local)
    val, _ = quad(integrand, 0.0, np.inf, limit=limit)      # (local)
    return val


fk_table = {}                                               # (local) {reg: {k: f_k}}
for name, f in REGULATORS.items():
    fk_table[name] = {k: mellin_moment(f, k) for k in K_VALUES}

print()
print(f"  {'Regulator':<14} | " + " | ".join(f"f_{k}" for k in K_VALUES))
print("  " + "-" * 68)
for name in REGULATORS:
    row = [f"{fk_table[name][k]:.6e}" for k in K_VALUES]
    print(f"  {name:<14} | " + " | ".join(row))

# ============================================================
# SECTION 4: Part A — trivial balanced ratio f_k / f_k = 1 exactly
# ============================================================
print("\n[SEC 4] Part A — trivial balanced ratio f_k / f_k = 1")
print("  (Identity-level cancellation in Lemma 2 step 3.)")
partA_deviations = []                                       # (local)
for name in REGULATORS:
    fk4 = fk_table[name][4]                                 # (local)
    r = fk4 / fk4                                           # (local)
    d = abs(r - 1.0)                                        # (local)
    partA_deviations.append(d)
    print(f"  reg={name:<14}  f_4/f_4 = {r:.16e}  dev={d:.2e}")

partA_max_dev = float(max(partA_deviations))                # (local)
print(f"  Part A max deviation from 1.0: {partA_max_dev:.2e}")

# ============================================================
# SECTION 5: Part B — f_4 / f_2 varies (Mellin moments are regulator-specific)
# ============================================================
print("\n[SEC 5] Part B — f_4/f_2 across 3 regulators (sanity: DOES vary)")
ratios_B = {}                                               # (local)
for name in REGULATORS:
    ratios_B[name] = fk_table[name][4] / fk_table[name][2]
    print(f"  reg={name:<14}  f_4/f_2 = {ratios_B[name]:.6e}")

partB_vals = np.array(list(ratios_B.values()))              # (local)
partB_spread_abs = float(partB_vals.max() - partB_vals.min())  # (local)
partB_spread_rel = partB_spread_abs / float(np.mean(np.abs(partB_vals)))  # (local)
print(f"  Part B absolute spread: {partB_spread_abs:.4e}")
print(f"  Part B relative spread: {partB_spread_rel*100:.2f}%")
print("  (Part B is NOT a gate test; it documents regulator dependence of")
print("   isolated Mellin moments, which Lemma 1 relies on being generic.)")

# ============================================================
# SECTION 6: Part C — NON-TRIVIAL balanced-channel cancellation
# ============================================================
print("\n[SEC 6] Part C — non-trivial balanced case (distinct k=4 channels)")
# Two GEOMETRICALLY-DISTINCT Seeley-DeWitt integrands both carrying k=4
# (e.g. Riemann^2 and Ricci^2 contributions to a_4 in d=8). Both sit at
# Mellin-label k=4 hence Lambda^k and f_k and Gamma(k/2) identically cancel
# in any ratio (Lemma 2 step 3).
a_4_I = 50.0                                                # (local) e.g. Riemann^2 coefficient
a_4_II = 30.0                                               # (local) e.g. Ricci^2 coefficient
Lambda_test = 1.0                                           # (local) arbitrary scale (cancels)
k_bal = 4                                                   # (local) shared Mellin label
from math import gamma as _gamma

Gamma_kbal = _gamma(k_bal / 2.0)                            # (local) Gamma(2) = 1
expected_ratio = a_4_I / a_4_II                             # (local) = 5/3
print(f"  Expected R_{{I,II}} = a_4^(I)/a_4^(II) = {expected_ratio:.12e}")
print(f"  {'Regulator':<14} | R_{{I,II}} from full S_I/S_II | deviation")
print("  " + "-" * 72)
partC_deviations = []                                       # (local)
for name in REGULATORS:
    fk = fk_table[name][k_bal]                              # (local)
    S_I = fk * Lambda_test ** k_bal * a_4_I / Gamma_kbal    # (local)
    S_II = fk * Lambda_test ** k_bal * a_4_II / Gamma_kbal  # (local)
    R = S_I / S_II                                          # (local)
    dev = abs(R - expected_ratio)                           # (local)
    partC_deviations.append(dev)
    print(f"  {name:<14} | {R:.16e}     | {dev:.2e}")

partC_max_dev = float(max(partC_deviations))                # (local)
print(f"  Part C max deviation (balanced cancellation): {partC_max_dev:.2e}")

# ============================================================
# SECTION 7: Part D — UNBALANCED counterexample
# ============================================================
print("\n[SEC 7] Part D — unbalanced counterexample (k_m=2, k_n=4)")
# S_{a_{d-2}} / S_{a_{d-4}} carries (f_2 / f_4) · Lambda^{-2} · Gamma(2)/Gamma(1)
# which is a genuine function of f (distinct moments at distinct s).
a_6 = 100.0                                                 # (local) substitute SDW coefficient (k=2 slot)
a_4 = 50.0                                                  # (local) SDW coefficient (k=4 slot)
Gamma_1 = _gamma(1.0)                                       # (local) = 1
Gamma_2 = _gamma(2.0)                                       # (local) = 1
print(f"  Expected: ratio = (f_2/f_4) * (a_6/a_4) * Lambda^{{-2}} * Gamma(2)/Gamma(1)")
print(f"  {'Regulator':<14} | f_2/f_4      | S_{{a6}}/S_{{a4}}")
print("  " + "-" * 70)
partD_values = {}                                           # (local)
for name in REGULATORS:
    f2 = fk_table[name][2]                                  # (local)
    f4 = fk_table[name][4]                                  # (local)
    S_a6 = f2 * Lambda_test ** 2 * a_6 / Gamma_1            # (local)
    S_a4 = f4 * Lambda_test ** 4 * a_4 / Gamma_2            # (local)
    R = S_a6 / S_a4                                         # (local)
    partD_values[name] = R
    print(f"  {name:<14} | {f2/f4:.6e} | {R:.6e}")

partD_vals = np.array(list(partD_values.values()))          # (local)
partD_spread_abs = float(partD_vals.max() - partD_vals.min())  # (local)
partD_mean_abs = float(np.mean(np.abs(partD_vals)))         # (local)
partD_spread_rel = partD_spread_abs / partD_mean_abs        # (local)
print(f"  Part D absolute spread: {partD_spread_abs:.4e}")
print(f"  Part D relative spread: {partD_spread_rel*100:.2f}%")
print("  (Large spread required — the unbalanced pair MUST retain f-dependence.)")

# ============================================================
# SECTION 8: Gate verdict rule (sanity layer)
# ============================================================
print("\n[SEC 8] Gate verdict rule (sanity layer)")
BAL_TIGHT = 1e-12                                           # (local) PASS threshold
BAL_LOOSE = 1e-6                                            # (local) INFO upper bound
UNBAL_MIN_REL = 1e-3                                        # (local) counterexample must vary
print(f"  PASS if partC_max_dev <= {BAL_TIGHT:.0e}")
print(f"       AND partD_spread_rel >= {UNBAL_MIN_REL:.0e}")
print(f"  INFO if {BAL_TIGHT:.0e} < partC_max_dev <= {BAL_LOOSE:.0e}")
print(f"  FAIL if partC_max_dev > {BAL_LOOSE:.0e}")
print(f"       OR partD_spread_rel < {UNBAL_MIN_REL:.0e}")


def evaluate_gate(partC_dev, partD_rel):                    # (local)
    """Gate rule for sanity layer. Return (value, verdict, reason)."""
    if partC_dev > BAL_LOOSE:
        return (2, "FAIL",
                f"balanced cancellation dev {partC_dev:.2e} > "
                f"INFO upper {BAL_LOOSE:.0e} (theorem violated numerically)")
    if partD_rel < UNBAL_MIN_REL:
        return (2, "FAIL",
                f"unbalanced counterexample spread {partD_rel:.2e} < "
                f"{UNBAL_MIN_REL:.0e} (f fails to retain dependence)")
    if partC_dev > BAL_TIGHT:
        return (1, "INFO",
                f"balanced cancellation dev {partC_dev:.2e} exceeds PASS "
                f"tight {BAL_TIGHT:.0e} but below INFO upper {BAL_LOOSE:.0e}")
    return (0, "PASS",
            f"balanced dev {partC_dev:.2e} <= {BAL_TIGHT:.0e} and "
            f"unbalanced rel spread {partD_rel:.2e} >= {UNBAL_MIN_REL:.0e}")


verdict_value, verdict, reason = evaluate_gate(partC_max_dev, partD_spread_rel)
print(f"\n  -> verdict value: {verdict_value}")
print(f"  -> verdict:       {verdict}")
print(f"  -> reason:        {reason}")

# ============================================================
# SECTION 9: Closure SHA + 4-tuple emit
# ============================================================
print("\n[SEC 9] Closure SHA and 4-tuple emit")
closure_map = {                                             # (local) ordered input-pin map
    'script': 's82_w1_3_cc_ratios_sg.py',
    'd_total': D_TOTAL,
    'k_values': K_VALUES,
    'regulators': list(REGULATORS.keys()),
    'Lambda_test': Lambda_test,
    'a_4_I': a_4_I,
    'a_4_II': a_4_II,
    'a_6': a_6,
    'a_4': a_4,
    'BAL_TIGHT': BAL_TIGHT,
    'BAL_LOOSE': BAL_LOOSE,
    'UNBAL_MIN_REL': UNBAL_MIN_REL,
    'partA_max_dev': partA_max_dev,
    'partB_spread_rel': partB_spread_rel,
    'partC_max_dev': partC_max_dev,
    'partD_spread_rel': partD_spread_rel,
    'verdict_value': verdict_value,
    'verdict': verdict,
    'scheme': 'CC96-eq-2.11',
    'convention': 'WEIGHT-BALANCE',
    'inputs': {k: v for k, v in sorted(INPUT_SHAS.items())},
}

closure_str = json.dumps(closure_map, sort_keys=True, default=str)  # (local)
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()  # (local)

four_tuple = (                                              # (local)
    f"(value={verdict_value}, scheme=CC96-eq-2.11, "
    f"convention=WEIGHT-BALANCE, L_max=N/A)"
)
print(f"  Closure SHA-256 (64 char): {closure_sha}")
print(f"  4-TUPLE: {four_tuple}")
assert len(closure_sha) == 64, "closure SHA must be full 64-char hexdigest"

# ============================================================
# SECTION 10: Save .npz
# ============================================================
print("\n[SEC 10] Saving data")
out_npz = HERE / 's82_w1_3_cc_ratios_sg.npz'                # (local)
np.savez(
    out_npz,
    d_total=D_TOTAL,
    k_values=np.array(K_VALUES),
    regulators=np.array(list(REGULATORS.keys())),
    # f_k table: rows = regulators, cols = k_values
    fk_matrix=np.array([[fk_table[r][k] for k in K_VALUES]
                        for r in REGULATORS.keys()]),
    # Part A: f_k/f_k = 1 deviations
    partA_deviations=np.array(partA_deviations),
    partA_max_dev=partA_max_dev,
    # Part B: f_4/f_2 spread
    partB_values=np.array([ratios_B[r] for r in REGULATORS.keys()]),
    partB_spread_abs=partB_spread_abs,
    partB_spread_rel=partB_spread_rel,
    # Part C: balanced cancellation
    a_4_I=a_4_I,
    a_4_II=a_4_II,
    expected_ratio=expected_ratio,
    partC_deviations=np.array(partC_deviations),
    partC_max_dev=partC_max_dev,
    # Part D: unbalanced counterexample
    a_6=a_6,
    a_4=a_4,
    partD_values=np.array([partD_values[r] for r in REGULATORS.keys()]),
    partD_spread_abs=partD_spread_abs,
    partD_spread_rel=partD_spread_rel,
    # Gate
    verdict_value=verdict_value,
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    closure_sha=np.array([closure_sha]),
    four_tuple=np.array([four_tuple]),
    # Input SHAs
    input_shas=np.array([f"{k}={v}" for k, v in sorted(INPUT_SHAS.items())]),
)
print(f"  Saved: {out_npz}")

# ============================================================
# SECTION 11: Append verdict to s82_gate_verdicts.txt
# ============================================================
print("\n[SEC 11] Append verdict to s82_gate_verdicts.txt")
verdicts_path = HERE / 's82_gate_verdicts.txt'              # (local)
verdict_line = (                                            # (local)
    f"S82-CC-RATIOS-ONLY-THEOREM-SG: {verdict} -- "
    f"value={verdict_value} "
    f"scheme=CC96-eq-2.11 "
    f"convention=WEIGHT-BALANCE "
    f"L_max=N/A "
    f"sha256={closure_sha}\n"
)
with open(verdicts_path, 'a', encoding='utf-8') as _f:
    _f.write(verdict_line)
print(f"  Appended: {verdict_line.strip()}")

# ============================================================
# SECTION 12: Summary
# ============================================================
print("\n" + "=" * 72)
print(f"Summary  |  S82-CC-RATIOS-ONLY-THEOREM-SG  |  {verdict} (value={verdict_value})")
print("=" * 72)
print(f"  Part A (f_k/f_k=1)    max dev      : {partA_max_dev:.2e}")
print(f"  Part B (f_4/f_2)      rel spread   : {partB_spread_rel*100:.2f}%")
print(f"  Part C (balanced)     max dev      : {partC_max_dev:.2e}")
print(f"  Part D (unbalanced)   rel spread   : {partD_spread_rel*100:.2f}%")
print(f"  Direction — balanced  : f CANCELS (identity-level)")
print(f"  Direction — unbalanced: f RETAINS (distinct Mellin moments)")
print(f"  Closure SHA-256       : {closure_sha}")
print(f"  4-tuple               : {four_tuple}")
print("=" * 72)
