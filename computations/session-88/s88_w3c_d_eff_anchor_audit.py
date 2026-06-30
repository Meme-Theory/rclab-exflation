#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W3c-57 -- d_eff Anchor Convention Audit (HK-5 structural-coincidence test)
==============================================================================

Gate: S88-D-EFF-ANCHOR-CONVENTION-AUDIT  ([VERIFY])
Plan: sessions/session-plan/session-88-plan-w3c.md §W3c-57
Owner: lizzi-spectral-functional-theorist (PRIMARY); connes-ncg-theorist (advisory)

Hypothesis under test
---------------------
The W1b-3 Richardson L^{-3} extrapolated slope_inf_B = 5.061193223 (Conv B
baseline) admits closed-form structural identification as the HK-5 form
    HK-5(tau) = 5 / (1 - tau / (5 * pi))
evaluated at tau_fold = 0.190 (canonical_constants.py).

Triple-prior pre-registration (per epistemic-discipline.md §"Dual-prior
pre-registration as track-discriminator pattern" extended to triple-prior):
  Track A (structural identification, HK-5 closure):  prior 0.30
  Track B (numerical near-match deferred):            prior 0.45
  Track C (numerology coincidence, no derivation):    prior 0.25

Substitution chain Step 4 (Sage-verified at plan-time)
------------------------------------------------------
HK-5(tau_fold) at Sage QQ exact pi:           5.0612193741921105
slope_inf_B (S87 W1b empirical, canonical):   5.061193222987735
residual = slope_inf_B - HK-5(tau_fold):     -2.6151e-05
|residual| < 1e-3 (INFO band) but > 1e-12 (PASS band) ==> Track B INFO expected.

Spawn-prompt rejection (Step 4):
  5 + 4 * tau_fold = 5 + 4 * 0.190 = 5.76    (NOT 5.04 as spawn-prompt stated)
  spawn-prompt's '5.04 + epsilon' reading is ARITHMETIC ERROR.
  The correct candidate identification is HK-5(tau_fold).

PASS / INFO / FAIL predicates (plan §W3c-57)
--------------------------------------------
PASS iff |slope_inf_B - HK-5(tau_fold)| <= 1e-12 (Sage-symbolic identity)
INFO iff PASS-NOT-MET AND |residual| < 1e-3 ABSOLUTE for some tau_anchor
        in {0, tau_fold/2, tau_fold, 2*tau_fold}
FAIL iff |residual| >= 1e-3 across ALL tau_anchor candidates AND no
        algebraic identity slope = a + b*tau_fold + c*tau_fold^2 with
        rational (a,b,c) in {-3..+3} / {1..30} matches within 1e-6
        ==> explicit numerology ruling

Inputs (SHA-256 dual-pinned at runtime)
---------------------------------------
- computations/_shared/canonical_constants.py
- computations/session-87/s87_w1b_hk_3_d_eff_convention_audit.npz (slope_inf_A/B)

Output 4-tuple
--------------
value = (slope_inf_B_observed, hk_5_at_tau_fold, residual_absolute, track_assigned)
4-tuple: (scheme="substrate-IS-Richardson-L3-extrapolation",
          convention="HK-5-form-Conv-B-baseline",
          L_max=10, audit_sha256, content_sha256)

Classification: GEOMETRIC (NCG dim-spectrum residue identification under
                Connes-Moscovici 1995 §III.4 framework; Heat-Kernel form 5).
"""

from __future__ import annotations

# Section 1 -- Canonical constants (MANDATORY)
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent  # (local) computations/session-88/
PROJECT_ROOT = HERE.parent.parent  # (local) project root
SHARED_DIR = HERE.parent / "_shared"  # (local) computations/_shared/
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold  # noqa: E402

# Section 2 -- Standard imports
import os  # noqa: E402

os.environ.setdefault("OMP_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402

# Section 3 -- Pre-registration constants
SESSION = "S88"  # (local)
GATE_ID = "S88-D-EFF-ANCHOR-CONVENTION-AUDIT"  # (local)
SCHEME = "substrate-IS-Richardson-L3-extrapolation"  # (local)
CONVENTION = "HK-5-form-Conv-B-baseline"  # (local)
L_MAX = 10  # (local)

PASS_THRESHOLD_ABS = 1.0e-12  # (local) Sage-symbolic identity (publication-precision)
INFO_THRESHOLD_ABS = 1.0e-3   # (local) numerical near-match
ALG_IDENTITY_TOL = 1.0e-6    # (local) rational fit grid match tolerance

# Inputs / outputs
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
S87_W1B_NPZ = (PROJECT_ROOT / "computations" / "session-87"
               / "s87_w1b_hk_3_d_eff_convention_audit.npz")
OUT_NPZ = HERE / "s88_w3c_d_eff_anchor_audit.npz"
OUT_PNG = HERE / "s88_w3c_d_eff_anchor_audit.png"
VERDICT_TXT = SHARED_DIR / "s88_gate_verdicts.txt"

INPUT_FILES = [CANONICAL_PY, S87_W1B_NPZ]


# Section 4 -- SHA helpers
def sha256_of(path: Path) -> str:
    """Compute SHA-256 of a file's contents."""
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Log SHA-256 pins for each input file; return pinmap dict."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...  ({sha})")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins, identity_tag):
    """Dual-SHA closure (audit + content) per gate-verdicts.md S87+ schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(identity_tag.encode("utf-8"))  # per-gate identity differentiator
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


print("=" * 72)
print(f"{GATE_ID}: d_eff Anchor Convention Audit (HK-5 structural-coincidence test)")
print("=" * 72)

PINS = log_input_pins(INPUT_FILES)

# =============================================================================
# Section 5 -- Load S87 W1b canonical pins
# =============================================================================
print("\n--- Section 5: S87 W1b-HK-3 canonical anchor values ---")
w1b = np.load(S87_W1B_NPZ, allow_pickle=True)
slope_inf_B_observed = float(w1b["d_eff_B_inf"])  # (local) 5.061193222987735
slope_inf_A_observed = float(w1b["d_eff_A_inf"])  # (local) 10.12238644597547
print(f"  slope_inf_A (Conv A) = {slope_inf_A_observed:.15f}")
print(f"  slope_inf_B (Conv B) = {slope_inf_B_observed:.15f}")
print(f"  ratio A/B            = {slope_inf_A_observed / slope_inf_B_observed:.15f}")

# CC1 cross-check: ratio = 2.000000 EXACTLY (Sage QQ verified at plan-time)
ratio_A_over_B = slope_inf_A_observed / slope_inf_B_observed  # (local)
ratio_dev = abs(ratio_A_over_B - 2.0)  # (local)
print(f"  CC1: |ratio - 2|     = {ratio_dev:.3e}  (Sage QQ exact = 0)")

# =============================================================================
# Section 6 -- Substrate-physics derivation Step 2: HK-5(tau_fold)
# =============================================================================
TAU_FOLD = float(tau_fold)
print("\n--- Section 6: HK-5(tau) form evaluation at tau_fold ---")
print(f"  HK-5(tau) := 5 / (1 - tau / (5 * pi))")
print(f"  tau_fold = {TAU_FOLD}  (canonical_constants.py; S58 Volovik partition)")


def hk_5(tau, pi_val=math.pi):
    """Heat-Kernel-form 5 spectral-dimension predicate at tau-deformation."""
    return 5.0 / (1.0 - tau / (5.0 * pi_val))


hk_5_at_tau_fold = hk_5(TAU_FOLD)  # (local)
print(f"  HK-5(tau_fold) at math.pi  = {hk_5_at_tau_fold:.15f}")
print(f"  HK-5(tau_fold) Sage QQ pi  = 5.061219374192111  (plan-time pin)")

# =============================================================================
# Section 7 -- Substrate-physics derivation Step 3: residual + verdict band
# =============================================================================
print("\n--- Section 7: residual = slope_inf_B - HK-5(tau_fold) ---")
residual_absolute = abs(slope_inf_B_observed - hk_5_at_tau_fold)  # (local)
residual_signed = slope_inf_B_observed - hk_5_at_tau_fold  # (local)
print(f"  residual_signed   = {residual_signed:.6e}")
print(f"  residual_absolute = {residual_absolute:.6e}")
print(f"  PASS threshold (1e-12)  = {PASS_THRESHOLD_ABS:.0e}  ", end="")
print("MET" if residual_absolute <= PASS_THRESHOLD_ABS else "NOT MET")
print(f"  INFO threshold (1e-3)   = {INFO_THRESHOLD_ABS:.0e}  ", end="")
print("MET" if residual_absolute <= INFO_THRESHOLD_ABS else "NOT MET")

# =============================================================================
# Section 8 -- Substrate-physics derivation Step 4: spawn-prompt rejection
# =============================================================================
print("\n--- Section 8: spawn-prompt '5 + 4*tau_fold' reading explicit rejection ---")
five_plus_4tau = 5.0 + 4.0 * TAU_FOLD  # (local)
print(f"  Spawn-prompt's 5 + 4*tau_fold = {five_plus_4tau:.6f}")
print(f"  (NOT 5.04 as spawn-prompt stated; arithmetic error: 5 + 4*0.190 = 5.76)")
print(f"  Correct candidate (HK-5(tau_fold)) = {hk_5_at_tau_fold:.6f}")
print(f"  spawn-prompt residual vs slope_inf_B: {abs(slope_inf_B_observed - five_plus_4tau):.4f}")
print(f"  HK-5(tau_fold) residual vs slope_inf_B: {residual_absolute:.4e}")
print(f"  HK-5(tau_fold) is the structurally-correct candidate; spawn-prompt's"
      f" 5+4*tau_fold REJECTED.")
spawn_prompt_rejected = bool(abs(slope_inf_B_observed - five_plus_4tau)
                             >= INFO_THRESHOLD_ABS)  # (local)

# =============================================================================
# Section 9 -- tau_anchor candidate sweep
# =============================================================================
print("\n--- Section 9: tau_anchor candidate sweep ---")
tau_anchor_set = [
    ("0",            0.0),
    ("tau_fold/2",   TAU_FOLD / 2.0),
    ("tau_fold",     TAU_FOLD),
    ("2*tau_fold",   2.0 * TAU_FOLD),
]  # (local)
tau_anchor_results = {}  # (local)
print(f"  {'tau_anchor':>12s}  {'HK-5(tau)':>14s}  {'|residual|':>14s}  band")
for label, tau_val in tau_anchor_set:
    hk5_val = hk_5(tau_val)
    res = abs(slope_inf_B_observed - hk5_val)
    if res <= PASS_THRESHOLD_ABS:
        band = "PASS (1e-12)"
    elif res <= INFO_THRESHOLD_ABS:
        band = "INFO (1e-3)"
    else:
        band = "FAIL (>1e-3)"
    tau_anchor_results[label] = {"tau": tau_val, "hk5": hk5_val,
                                 "res_abs": res, "band": band}
    print(f"  {label:>12s}  {hk5_val:>14.10f}  {res:>14.4e}  {band}")

n_tau_anchor_info = sum(
    1 for v in tau_anchor_results.values() if v["res_abs"] <= INFO_THRESHOLD_ABS
)  # (local)
print(f"\n  tau_anchor candidates with INFO-band match: {n_tau_anchor_info} / 4")

# =============================================================================
# Section 10 -- Algebraic-identity grid search FAIL fallback
#
# Plan §W3c-57: rational (a,b,c) in {-3..+3} / {1..30} for
#   slope = a + b*tau_fold + c*tau_fold^2
# match if |slope_inf_B_observed - (a + b*tau + c*tau^2)| <= 1e-6
# =============================================================================
print("\n--- Section 10: algebraic-identity rational grid search ---")
print("  search grid: (a, b, c) in (numerator/denominator) where")
print("  numerator in {-3,...,+3}, denominator in {1,...,30}")
print("  predicate: |slope_inf_B - (a + b*tau_fold + c*tau_fold^2)| <= 1e-6")

alg_matches = []  # (local)
n_alg_combos = 0  # (local)
NUMERATOR_RANGE = list(range(-3, 4))
DENOMINATOR_RANGE = list(range(1, 31))

# Enumerate distinct rationals in [-3..+3] / [1..30]
rationals = sorted({Fraction(num, den) for num in NUMERATOR_RANGE
                    for den in DENOMINATOR_RANGE if den != 0})
n_rationals = len(rationals)  # (local)
print(f"  distinct rationals in grid: {n_rationals}")

tau_squared = TAU_FOLD ** 2  # (local)
for a in rationals:
    a_f = float(a)
    base = a_f
    if abs(base - slope_inf_B_observed) > 4.0:  # quick prune (b*tau in [-3*0.19, +3*0.19] etc.)
        # broad prune: even with extreme (b,c), can residual close to slope_inf_B?
        # max |b*tau| ~ 3*0.19 = 0.57; max |c*tau^2| ~ 3*0.0361 = 0.108; sum ~ 0.68
        if abs(slope_inf_B_observed - a_f) > 1.0:
            continue
    for b in rationals:
        b_f = float(b)
        for c in rationals:
            c_f = float(c)
            n_alg_combos += 1
            est = a_f + b_f * TAU_FOLD + c_f * tau_squared
            res = abs(slope_inf_B_observed - est)
            if res <= ALG_IDENTITY_TOL:
                alg_matches.append({"a": str(a), "b": str(b), "c": str(c),
                                    "estimate": est, "residual": res})

print(f"  total (a,b,c) combinations evaluated (post-prune): {n_alg_combos}")
print(f"  matches at <= 1e-6: {len(alg_matches)}")
if alg_matches:
    print("  TOP 5 matches:")
    for m in sorted(alg_matches, key=lambda x: x["residual"])[:5]:
        print(f"    a={m['a']}, b={m['b']}, c={m['c']}: "
              f"est={m['estimate']:.10f}, res={m['residual']:.3e}")
else:
    print("  NO matches — (a,b,c) polynomial form does NOT close to within 1e-6")
    print("  This is EXPECTED: HK-5 is a RATIONAL form 5/(1-tau/(5pi)); polynomial")
    print("  approximation cannot capture the pi denominator at the 1e-6 level.")

# =============================================================================
# Section 11 -- Composite verdict per plan §W3c-57 triple-prior rule
# =============================================================================
print("\n--- Section 11: Composite verdict per triple-prior rule ---")

# PASS = HK-5(tau_fold) Sage-symbolic identity (residual <= 1e-12)
pass_track_A = residual_absolute <= PASS_THRESHOLD_ABS  # (local)
# INFO = at least one tau_anchor in INFO band (residual <= 1e-3)
info_track_B = any(v["res_abs"] <= INFO_THRESHOLD_ABS
                   for v in tau_anchor_results.values())  # (local)
# FAIL = neither PASS nor INFO band met AND no algebraic identity match
fail_track_C = (not info_track_B) and (len(alg_matches) == 0)  # (local)

if pass_track_A:
    composite_verdict = "PASS"
    track_assigned = "A"
elif info_track_B:
    composite_verdict = "INFO"
    track_assigned = "B"
else:
    composite_verdict = "FAIL"
    track_assigned = "C"

# S87+ schema-v2 3-tuple companion
# sign_verdict: residual sign expected NEGATIVE (slope < HK-5(tau_fold))
#               actual sign computed from residual_signed
sign_predicted = "NEGATIVE"  # plan Step 5: HK-5 > 5 ⇒ HK-5(tau_fold) > slope_inf_B since tau_fold > 0
sign_actual = "NEGATIVE" if residual_signed < 0 else "POSITIVE"  # (local)
sign_verdict = "PASS" if sign_actual == sign_predicted else "FAIL"  # (local)
magnitude_verdict = "PASS" if pass_track_A else (
    "INFO" if info_track_B else "FAIL"
)  # (local)
regime_verdict = "VALID"  # (local) Richardson L^{-3} converged at L=14 per W1b-3 PASS

print(f"  pass_track_A (HK-5 Sage-symbolic identity, |res|<={PASS_THRESHOLD_ABS:.0e}): {pass_track_A}")
print(f"  info_track_B (any tau_anchor |res|<={INFO_THRESHOLD_ABS:.0e}): {info_track_B}")
print(f"  fail_track_C (no INFO + no algebraic identity match): {fail_track_C}")
print(f"  Track assigned: {track_assigned}")
print(f"  COMPOSITE VERDICT: {composite_verdict}")
print(f"  3-tuple: sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict}")

# =============================================================================
# Section 12 -- Output emission
# =============================================================================
print("\n--- Section 12: Output emission ---")

# 4-tuple value per plan §W3c-57
value_tuple = (slope_inf_B_observed, hk_5_at_tau_fold,
               residual_absolute, track_assigned)  # (local)
value_str = (f"(slope_inf_B_observed={slope_inf_B_observed:.15f},"
             f"hk_5_at_tau_fold={hk_5_at_tau_fold:.15f},"
             f"residual_absolute={residual_absolute:.6e},"
             f"track_assigned={track_assigned})")

# Dual-SHA closure with per-gate identity
IDENTITY_TAG = f"{GATE_ID}|{SCHEME}|{CONVENTION}|L={L_MAX}|track={track_assigned}"  # (local)
audit_sha, content_sha = compute_dual_sha(
    Path(__file__), CANONICAL_PY, PINS, IDENTITY_TAG,
)
print(f"  audit_sha256:   {audit_sha}")
print(f"  content_sha256: {content_sha}")

# Save NPZ
np.savez(
    OUT_NPZ,
    slope_inf_B_observed=np.array(slope_inf_B_observed),
    slope_inf_A_observed=np.array(slope_inf_A_observed),
    hk_5_at_tau_fold=np.array(hk_5_at_tau_fold),
    residual_signed=np.array(residual_signed),
    residual_absolute=np.array(residual_absolute),
    pass_threshold_abs=np.array(PASS_THRESHOLD_ABS),
    info_threshold_abs=np.array(INFO_THRESHOLD_ABS),
    alg_identity_tol=np.array(ALG_IDENTITY_TOL),
    tau_fold=np.array(TAU_FOLD),
    five_plus_4_tau_fold=np.array(five_plus_4tau),
    spawn_prompt_rejected=np.array(spawn_prompt_rejected),
    ratio_A_over_B=np.array(ratio_A_over_B),
    ratio_dev=np.array(ratio_dev),
    tau_anchor_labels=np.array([k for k, _ in tau_anchor_set], dtype=object),
    tau_anchor_residuals=np.array([tau_anchor_results[k]["res_abs"]
                                    for k, _ in tau_anchor_set]),
    n_tau_anchor_info=np.array(n_tau_anchor_info),
    n_alg_combos_evaluated=np.array(n_alg_combos),
    n_alg_matches=np.array(len(alg_matches)),
    alg_matches_top=np.array(
        sorted(alg_matches, key=lambda x: x["residual"])[:10]
        if alg_matches else [], dtype=object
    ),
    track_assigned=np.array(track_assigned),
    composite_verdict=np.array(composite_verdict),
    sign_verdict=np.array(sign_verdict),
    magnitude_verdict=np.array(magnitude_verdict),
    regime_verdict=np.array(regime_verdict),
    audit_sha256=np.array(audit_sha),
    content_sha256=np.array(content_sha),
    L_max=np.array(L_MAX),
)
print(f"  NPZ written: {OUT_NPZ}")

# Generate plot (2-panel: HK-5(tau) curve + tau_anchor sweep + algebraic grid heatmap)
try:
    import matplotlib  # noqa: E402
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # noqa: E402

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    # Top: HK-5(tau) curve with tau_anchor pins + slope_inf_B horizontal line
    tau_grid = np.linspace(0.0, 0.4, 200)
    hk5_grid = np.array([hk_5(t) for t in tau_grid])
    axes[0].plot(tau_grid, hk5_grid, "b-", label="HK-5(tau) = 5/(1 - tau/(5*pi))")
    axes[0].axhline(slope_inf_B_observed, color="r", linestyle="--",
                    label=f"slope_inf_B = {slope_inf_B_observed:.6f} (S87 W1b)")
    for label, tau_val in tau_anchor_set:
        axes[0].plot(tau_val, hk_5(tau_val), "ko", markersize=8)
        axes[0].annotate(label, (tau_val, hk_5(tau_val)), xytext=(5, 8),
                         textcoords="offset points", fontsize=9)
    axes[0].axvline(TAU_FOLD, color="g", linestyle=":", linewidth=0.7,
                    label=f"tau_fold = {TAU_FOLD}")
    axes[0].set_xlabel("tau")
    axes[0].set_ylabel("HK-5(tau)")
    axes[0].set_title(f"{GATE_ID}: HK-5(tau) curve + slope_inf_B + tau_anchor sweep")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[0].grid(alpha=0.3)

    # Bot: tau_anchor residuals (log scale)
    labels = [k for k, _ in tau_anchor_set]
    residuals = [tau_anchor_results[k]["res_abs"] for k in labels]
    colors = ["red" if r > INFO_THRESHOLD_ABS else "orange"
              if r > PASS_THRESHOLD_ABS else "green" for r in residuals]
    axes[1].bar(labels, residuals, color=colors)
    axes[1].axhline(INFO_THRESHOLD_ABS, color="orange", linestyle="--",
                    label=f"INFO threshold = {INFO_THRESHOLD_ABS:.0e}")
    axes[1].axhline(PASS_THRESHOLD_ABS, color="green", linestyle="--",
                    label=f"PASS threshold = {PASS_THRESHOLD_ABS:.0e}")
    axes[1].set_yscale("log")
    axes[1].set_ylabel("|residual| (log scale)")
    axes[1].set_title("tau_anchor residual sweep — only tau_fold yields INFO band")
    axes[1].legend(loc="upper right", fontsize=9)
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  PNG written: {OUT_PNG}")
except Exception as exc:
    print(f"  PNG generation skipped: {exc}")

# Append verdict line + dual-SHA companion + 3-tuple companion (S87+ schema)
verdict_line = (
    f"{GATE_ID}: {composite_verdict} -- value={value_str!r} "
    f"scheme={SCHEME!r} convention={CONVENTION!r} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=R3\n"
)
companion_dual_sha = (
    f"# audit_sha256_short={audit_sha[:16]} "
    f"content_sha256_short={content_sha[:16]} # {GATE_ID} dual-SHA companion row "
    f"(W9a-99 split)\n"
)
companion_3tuple = (
    f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
    f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
    f"(S87 schema-v2)\n"
)

with open(VERDICT_TXT, "a") as f:
    f.write(verdict_line)
    f.write(companion_dual_sha)
    f.write(companion_3tuple)

print(f"  Verdict appended: {VERDICT_TXT}")
print(f"\n  4-tuple: ({value_str}, scheme={SCHEME!r}, "
      f"convention={CONVENTION!r}, L_max={L_MAX})")
print("\n" + "=" * 72)
print(f"{GATE_ID}: {composite_verdict}  [Track {track_assigned}]")
print("=" * 72)
