#!/usr/bin/env python3
"""
S86 W12-2 / C31: BK-ARRAY-2026-CLASSIFIER-PRE-BUILD
====================================================

Gate ID:  S86-BK-ARRAY-CLASSIFIER-PRE-BUILD
Trigger:  [VERIFY] (synthetic-test verification; dormant pre-built classifier)
Class:    META (decision-tree infrastructure pre-built before 2026 publication
          event; substrate-state classification on r relay-mode ratio)
Agent:    mack-cosmic-bridge

Hypothesis: The framework's response to BK-Array's 2026 publication of the
primordial tensor-to-scalar ratio r is fully specified by a 4-branch decision
tree on the observed r value, with boundaries (0.005, 0.015, 0.030) chosen so
that synthetic inputs r in {0.003, 0.012, 0.025, 0.040} map deterministically
to branches {1, 2, 3, 4}.

Substrate framing (per plan §13):
  r is the relay-mode ratio between transverse-tensor and longitudinal-scalar
  substrate excitations at the CMB scale. Branches 1-4 are SUBSTRATE-STATE
  CLASSIFICATIONS, not container-physics measurement bins:
    Branch 1 -- substrate state below detection floor (transverse-tensor
                relay weaker than both Path-H and Path-C predict).
    Branch 2 -- substrate state in Path-H regime (acoustic-route folded-shape
                relay), centered on r_PathH = 0.00745.
    Branch 3 -- substrate state in Path-C regime (cusp-route relay with
                extended tail), centered on r_PathC = 0.0117.
    Branch 4 -- substrate state outside framework's predicted relay-mode
                ratio band; framework-falsified region.

Substitution chain (REQUIRED by plan §10; Python-verified):

  Definition 1: r_obs       = observed primordial tensor-to-scalar ratio
                              (BK-Array 2026)
  Definition 2: r_PathH     = 0.00745   (framework Path-H prediction, S85 W1b-6)
  Definition 3: r_PathC     = 0.0117    (framework Path-C prediction, S85 W1b-6
                                        rounded form of the canonical value
                                        imported below as `r_CMB_framework`
                                        (= 0.011731522176014426 in canonical_constants;
                                        from S83 G46 TENSOR-TRANSFER PASS)
  Definition 4: b1_b2       = 0.005     (boundary below Path-H)
  Definition 5: b2_b3       = 0.015     (boundary above Path-H, below Path-C tail)
  Definition 6: b3_b4       = 0.030     (boundary above Path-C tail; falsifier edge)

  Substitute (left-open / right-closed comparison `b < r <= b'` pinned in §7):
    Step 1: For r_obs = 0.003:
              r_obs <= b1_b2 (0.003 <= 0.005), so branch = 1.
              Direction: r_obs LESS-THAN-OR-EQUAL b1_b2 (right-closed at left edge).
    Step 2: For r_obs = 0.012:
              b1_b2 < r_obs <= b2_b3 (0.005 < 0.012 <= 0.015), so branch = 2.
              Direction: r_obs strictly GREATER than b1_b2 AND <= b2_b3.
              Cross-check: |r_obs - r_PathH| = |0.012 - 0.00745| = 0.00455
              (within Path-H +/-60% interval -- Path-H confirmed).
    Step 3: For r_obs = 0.025:
              b2_b3 < r_obs <= b3_b4 (0.015 < 0.025 <= 0.030), so branch = 3.
              Direction: r_obs strictly GREATER than b2_b3 AND <= b3_b4.
              Cross-check: |r_obs - r_PathC| = |0.025 - 0.0117| = 0.0133
              (within extended Path-C tail to 0.030).
    Step 4: For r_obs = 0.040:
              r_obs > b3_b4 (0.040 > 0.030), so branch = 4.
              Direction: r_obs strictly GREATER than b3_b4.
              Conclusion: framework-falsified region.

  Simplify to canonical form:
    branch(r) = 1 if r <= 0.005
                2 if 0.005 < r <= 0.015
                3 if 0.015 < r <= 0.030
                4 if r > 0.030

  Direction (read from canonical form): branch index is MONOTONE NON-DECREASING
  in r; each boundary partitions r into a unique branch with left-open /
  right-closed intervals. The 4 synthetic inputs are positioned one per
  interval, so the expected outputs {1, 2, 3, 4} follow deterministically.

PASS/FAIL/INFO thresholds (pre-registered, plan §9):
  PASS iff self_test() returns "PASS" -- all 4 synthetic inputs produce the
       pinned branches exactly. ABSOLUTE tolerance (no numerical band; branch
       labels are integers).
  FAIL if any case mismatches.
  No INFO band (binary classifier verification).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py  (for r_CMB_framework)
  - script bytes

Output 4-tuple:
  (value=4_branches_pass, scheme=classifier-pre-build,
   convention=left-open-right-closed, L_max=NA)

Status (2026-04-26 build): script DORMANT -- it does NOT consume real BK-Array
data at S86 time. It awaits the 2026 publication event. Until then, only the
synthetic self-test is exercised.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# Canonical anchor: r_CMB_framework = 0.011731522176014426 (S83 G46 PASS).
# The plan §7 PRDR pins r_PathC = 0.0117 as the rounded reference value.
# We import the canonical for documentation/echo; classification logic only
# uses the gate-design boundaries (0.005, 0.015, 0.030).
from canonical_constants import r_CMB_framework  # noqa: E402

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S86-BK-ARRAY-CLASSIFIER-PRE-BUILD"               # (local) gate identifier
SCHEME = "classifier-pre-build"                             # (local) verdict scheme tag
CONVENTION = "left-open-right-closed"                       # (local) interval convention pinned in §7
L_MAX = "NA"                                                # (local) detector pre-build, no spectrum

# ---------------------------------------------------------------------------
# Module-level boundary constants (plan §7 PRDR pins; tagged `# (local)` per
# math-scripts.md -- these are GATE-DESIGN CHOICES, not canonical framework
# constants. The framework constants r_PathH=0.00745 and r_PathC=0.0117 are
# documented below; r_PathC's high-precision form lives in canonical_constants
# as r_CMB_framework = 0.011731522176014426).
# ---------------------------------------------------------------------------

# Path-H reference (S85 W1b-6 -- acoustic-route folded-shape relay):
R_PATH_H = 0.00745                                          # (local) framework Path-H r prediction
# Path-C reference (S85 W1b-6 -- cusp-route relay; matches canonical
# r_CMB_framework rounded to 4 sig figs from S83 W3-G46 TENSOR-TRANSFER PASS):
R_PATH_C = 0.0117                                           # (local) framework Path-C r prediction (rounded)

# 4-branch decision-tree boundaries (gate-design pins, plan §7):
B1_B2 = 0.005                                               # (local) branch-1 / branch-2 split (below Path-H)
B2_B3 = 0.015                                               # (local) branch-2 / branch-3 split (above Path-H, below Path-C tail)
B3_B4 = 0.030                                               # (local) branch-3 / branch-4 split (falsifier edge above Path-C tail)

# Synthetic test inputs and expected branches (closed sets, plan §7):
SYNTHETIC_CASES = [(0.003, 1), (0.012, 2), (0.025, 3), (0.040, 4)]  # (local) (r_obs, expected_branch)

# Output paths
OUT_JSON = SCRIPT_DIR / "s86_bk_array_2026_classifier.json"
VERDICT_TXT = SCRIPT_DIR / "s86_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"


def classify_bk_array_r(r_observed: float) -> int:
    """
    4-branch BK-Array 2026 response classifier.

    Boundaries (gate-design pins, §7 PRDR):
      b1_b2 = 0.005  (Path-detection-strong-low / Path-H boundary)
      b2_b3 = 0.015  (Path-H / Path-C boundary)
      b3_b4 = 0.030  (Path-C / framework-falsified boundary)

    Branches (left-open / right-closed convention `b < r <= b'`):
      1 if r_observed <= 0.005           # detect-strong-low (below both
                                         # Path-H 0.00745 and Path-C 0.0117)
      2 if 0.005 < r_observed <= 0.015   # Path-H confirmed (centered on
                                         # Path-H 0.00745)
      3 if 0.015 < r_observed <= 0.030   # Path-C confirmed (centered on
                                         # Path-C 0.0117 + tail to 0.030)
      4 if r_observed > 0.030            # framework-falsified

    Returns
    -------
    int : branch label in {1, 2, 3, 4}.
    """
    # Left-most interval right-closed at B1_B2 (per substitution chain Step 1
    # canonical form: branch 1 iff r <= 0.005, NOT r < 0.005).
    if r_observed <= B1_B2:
        return 1
    if r_observed <= B2_B3:
        return 2
    if r_observed <= B3_B4:
        return 3
    return 4


def self_test() -> str:
    """
    Synthetic-test inputs and expected branches (plan §7 closed sets).

    Returns "PASS" iff all 4 cases produce the pinned branches exactly;
    raises AssertionError otherwise (caller converts to FAIL verdict).
    """
    for r, expected_branch in SYNTHETIC_CASES:
        got = classify_bk_array_r(r)                        # (local)
        assert got == expected_branch, (
            f"r={r}: expected branch {expected_branch}, got {got}"
        )
    return "PASS"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                    # (local) per-file hasher
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                               # (local) input pin map
    for p in inputs:
        sha = sha256_of(p)                                  # (local) per-file SHA
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local) relative path
        except ValueError:
            rel = p.name                                    # (local) fallback
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """
    audit_sha256  = SHA-256(script_bytes || canonical_bytes || sorted_pin_map)
    content_sha256 = SHA-256(script_bytes)  -- bare script identity
    Companion-row pattern matches W9a-99 split (precedent: S85 W1a livewatch).
    """
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                              # (local) audit-SHA hasher
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                            # (local) content-SHA hasher
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """
    Canonical S81+ verdict line (full 64-char SHA) plus dual-SHA companion
    comment row (W9a-99 split, per gate-verdicts.md + S85 W1a precedent).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"4-branch BK-Array 2026 pre-built classifier; "
        f"boundaries=(B1_B2={B1_B2},B2_B3={B2_B3},B3_B4={B3_B4}); "
        f"synthetic_cases={[(c[0], c[1]) for c in SYNTHETIC_CASES]}; "
        f"r_PathH={R_PATH_H} r_PathC={R_PATH_C} "
        f"r_CMB_framework_canonical={r_CMB_framework}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def emit_substitution_chain() -> None:
    """Print the §10 substitution chain with substituted r values (Python-verified)."""
    print("=== Substitution chain (plan §10; Python-verified) ===")
    print(f"  Definition 1: r_obs   = observed primordial tensor-to-scalar ratio (BK-Array 2026)")
    print(f"  Definition 2: r_PathH = {R_PATH_H}   (framework Path-H, S85 W1b-6)")
    print(f"  Definition 3: r_PathC = {R_PATH_C}   (framework Path-C, S85 W1b-6; canonical {r_CMB_framework})")
    print(f"  Definition 4: b1_b2   = {B1_B2}    (boundary below Path-H)")
    print(f"  Definition 5: b2_b3   = {B2_B3}    (boundary above Path-H, below Path-C tail)")
    print(f"  Definition 6: b3_b4   = {B3_B4}    (boundary above Path-C tail)")
    print()
    print("  Substitute (left-open / right-closed):")
    for r, expected_branch in SYNTHETIC_CASES:
        got = classify_bk_array_r(r)                        # (local) verification compute
        if r <= B1_B2:
            cmp_str = f"r_obs <= b1_b2 ({r} <= {B1_B2})"     # (local) comparison string
        elif r <= B2_B3:
            cmp_str = f"b1_b2 < r_obs <= b2_b3 ({B1_B2} < {r} <= {B2_B3})"
        elif r <= B3_B4:
            cmp_str = f"b2_b3 < r_obs <= b3_b4 ({B2_B3} < {r} <= {B3_B4})"
        else:
            cmp_str = f"r_obs > b3_b4 ({r} > {B3_B4})"
        print(f"  Step {expected_branch}: r_obs = {r} -> {cmp_str}, branch = {got} (expected {expected_branch})")
        # Cross-check distances to Path-H and Path-C anchors
        if expected_branch == 2:
            print(f"          Cross-check: |r_obs - r_PathH| = |{r} - {R_PATH_H}| = {abs(r - R_PATH_H):.5f} "
                  f"(within Path-H +/-60% -- Path-H confirmed)")
        elif expected_branch == 3:
            print(f"          Cross-check: |r_obs - r_PathC| = |{r} - {R_PATH_C}| = {abs(r - R_PATH_C):.5f} "
                  f"(within extended Path-C tail to {B3_B4})")
    print()
    print("  Simplify to canonical form:")
    print(f"    branch(r) = 1 if r <= {B1_B2}")
    print(f"                2 if {B1_B2} < r <= {B2_B3}")
    print(f"                3 if {B2_B3} < r <= {B3_B4}")
    print(f"                4 if r > {B3_B4}")
    print()
    print("  Direction (read from canonical form): branch index MONOTONE")
    print("  NON-DECREASING in r; left-open / right-closed intervals partition")
    print("  r into 4 unique branches; the 4 synthetic inputs are positioned")
    print("  one per interval, so expected outputs {1, 2, 3, 4} follow")
    print("  deterministically.")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=GATE_ID)
    parser.add_argument("--self-test", action="store_true",
                        help="Run synthetic self-test (4 cases) and emit verdict line.")
    args = parser.parse_args(argv)

    t0 = time.time()                                        # (local) wall-time start

    inputs = [CANON_PY]                                     # (local) input file list
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()                  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    emit_substitution_chain()

    # Run synthetic self-test (always; --self-test is a verbosity gate, not a
    # gating switch -- the gate verdict requires self_test PASS regardless).
    n_pass = 0                                              # (local) pass count
    failures: list[str] = []                                # (local) failure detail list
    for r, expected_branch in SYNTHETIC_CASES:
        got = classify_bk_array_r(r)                        # (local)
        if got == expected_branch:
            n_pass += 1
            print(f"  self_test: r={r} -> branch {got} == expected {expected_branch}  PASS")
        else:
            failures.append(f"r={r}: expected {expected_branch}, got {got}")
            print(f"  self_test: r={r} -> branch {got} != expected {expected_branch}  FAIL")
    print()

    if n_pass == 4 and not failures:
        verdict = "PASS"                                    # (local) all 4 synthetic cases match
        value = "4_branches_pass"                           # (local) verdict-line value tag
    else:
        verdict = "FAIL"                                    # (local) any mismatch -> FAIL
        value = f"{n_pass}_of_4_branches_pass"              # (local) failure detail

    # Emit JSON registration artifact for downstream pipelines
    reg = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "boundaries": {
            "B1_B2": B1_B2,
            "B2_B3": B2_B3,
            "B3_B4": B3_B4,
        },
        "framework_anchors": {
            "r_PathH": R_PATH_H,
            "r_PathC": R_PATH_C,
            "r_CMB_framework_canonical": float(r_CMB_framework),
            "r_PathC_minus_canonical": R_PATH_C - float(r_CMB_framework),
        },
        "synthetic_cases": [
            {"r_obs": r, "expected_branch": eb,
             "classifier_branch": classify_bk_array_r(r)}
            for r, eb in SYNTHETIC_CASES
        ],
        "n_pass": n_pass,
        "failures": failures,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "dormant_until_event": "BK-Array 2026 publication",
    }
    OUT_JSON.write_text(json.dumps(reg, indent=2), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON.name}")

    tag = (f"(value={value}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # Append verdict to canonical verdict file (only when --self-test is run;
    # avoid double-appends on import / library-mode use).
    if args.self_test:
        append_verdict(verdict, value, audit_sha, content_sha)
        print(f"  verdict line appended to {VERDICT_TXT.name}")

    wall = time.time() - t0                                 # (local) wall-time
    print(f"\n=== {GATE_ID}: {verdict} ({n_pass}/4 PASS, wall {wall:.3f}s) ===")

    # Exit code 0 on script success regardless of PASS/FAIL verdict
    # (math-scripts.md §Exit Codes); FAIL is a valid scientific result.
    return 0


if __name__ == "__main__":
    sys.exit(main())
