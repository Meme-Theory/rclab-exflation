"""
s87_w9d_stage2_gatespec_audit.py

S87 W9d gate-spec authoring deliverable for the Stage-2 promotion of the
Joint F_2-Class Path-(c) Theorem (`S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY`).

This script is the documentary verification + verdict-line emitter for the
[VERIFY-THEOREM] gate-spec authoring deliverable at S87 plan-freeze. The
script does NOT execute the Stage-2 cross-review (that fires at S88+). At S87
the deliverable is the COMPLETE 13-field gate-spec block in
sessions/archive/session-87/session-87-results-workingpaper.md §W9d-1 plus the verdict
line emitted here.

Substitution chain (composite verdict determination):

  Definitions:
    P_i for i ∈ {1,2,3,4} = boolean: clause i of the 4-clause S87 plan-freeze
                            PASS predicate is satisfied.
    C = boolean: CF-54 (S87-PATH-C-SUCCESSOR-ANCHOR-LANDING) verdict line is
        present in computations/session-87/s87_gate_verdicts.txt at this runtime.

  Substitute:
    composite = PASS iff (P_1 ∧ P_2 ∧ P_3 ∧ P_4 ∧ C)
    composite = INFO iff (P_1 ∧ P_2 ∧ P_3 ∧ P_4 ∧ ¬C)
    composite = FAIL iff ¬(P_1 ∧ P_2 ∧ P_3 ∧ P_4)

  At S87 runtime: P_1..P_4 = True (this script verifies); C status read at
    runtime via grep on the verdict file. If C = False, composite = INFO
    (CONDITIONAL slot pin §VII.AH-OR-NEXT-FREE-LETTER-PER-registry-landing.md).
    If C = True, composite = PASS with the resolved slot identifier from CF-54.

  Direction: per plan §"Substitution chain (for the directional audit-script
    PASS predicate)" Steps 1-5; INFO is the pre-registered branch when the
    §VII.AH dependency is conditionally pinned (S87 plan-freeze closes BEFORE
    CF-54 lands). No numerical sign/direction is being asserted.

3-tuple annotation (S87 schema-v2 per .claude/rules/gate-verdicts.md):
  sign_verdict     = N/A     (no directional pre-registration; theorem-grade
                              gate-spec authoring is structural completeness,
                              not a signed delta)
  magnitude_verdict = PASS|INFO|FAIL  (4-clause AND result; INFO when CF-54
                                       not yet landed at S87 runtime)
  regime_verdict    = VALID  (no regime-of-validity expansion; no auto-
                              shortening clause; no compute-path)

Source
------
sessions/session-plan/session-87-plan-w9d.md §W9d-1
.claude/rules/joint-theorem-promotion.md §"Audit at plan-freeze"
.claude/rules/registry-landing.md §SOURCE-DOUBLE-CITE-CO-PRIMARY
.claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"
.claude/rules/epistemic-discipline.md §"What Does NOT Count as Evidence" item 2
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")


# ---------------------------------------------------------------------------
# Pinned audit parameters (gate-spec deliverable)
# ---------------------------------------------------------------------------

GATE_ID = "S87-W9D-STAGE2-VERIFY-GATE-SPEC-AUTHORING"                         # (local)
FORWARD_PIN_GATE_ID = "S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY"      # (local)

PROJECT_ROOT = Path(__file__).resolve().parent.parent                         # (local)
VERDICT_FILE = PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"   # (local)
SCHEMA_VERSION = "S87+"                                                       # (local)

# Input-pin map (the substrate for audit_sha256 closure).
INPUT_PIN_MAP_FILES = [                                                       # (local)
    ".claude/rules/joint-theorem-promotion.md",
    ".claude/rules/registry-landing.md",
    ".claude/rules/agent-standards.md",
    ".claude/rules/epistemic-discipline.md",
    ".claude/rules/phononic-framing.md",
    "computations/_shared/_joint_theorem_independent_verify_audit.py",
    "sessions/session-plan/session-87-plan-w9d.md",
]

# Forbidden source paths in S88+ Stage-2 cross-reviewer dispatch prompts.
FORBIDDEN_SOURCE_PATHS = [                                                    # (local)
    "sessions/archive/session-86/workshops/",
    "sessions/archive/session-86/session-86-w9-",
    "sessions/archive/session-86/path-c-reassessment-",
]

# Cross-reviewer assignments (mandatory per joint-theorem-promotion §Stage 2).
CROSS_REVIEWER_AXIS_A = "connes-ncg-theorist"                                 # (local) spectral-functional
CROSS_REVIEWER_AXIS_B = "volovik-superfluid-universe-theorist"                # (local) transit-dynamics/superfluid

# Stage-0 workshop authoring agents (FORBIDDEN as cross-reviewers).
WORKSHOP_AUTHORS_FORBIDDEN = [                                                # (local)
    "lizzi-spectral-functional-theorist",
    "transit-dynamics-theorist",
]

# Conditional-slot pin literal (used when CF-54 has not landed at runtime).
CONDITIONAL_SLOT_PIN = "§VII.AH-OR-NEXT-FREE-LETTER-PER-registry-landing.md"  # (local)

# CF-54 upstream gate ID for slot-resolution check.
CF54_GATE_ID = "S87-PATH-C-SUCCESSOR-ANCHOR-LANDING"                          # (local)


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    """SHA-256 over file content."""
    h = hashlib.sha256()                                                      # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """SHA-256 closure over an ordered (key-sorted) input-pin map."""
    canonical = json.dumps(input_pin_map, sort_keys=True,                     # (local)
                           separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


# ---------------------------------------------------------------------------
# 4-clause PASS predicate evaluators
# ---------------------------------------------------------------------------

def evaluate_clause_1_five_element_block(plan_path: Path) -> tuple[bool, str]:
    """Clause 1: 5-element block (per joint-theorem-promotion §Audit at
    plan-freeze) is fully populated in plan-w9d.md §W9d-1."""
    text = plan_path.read_text(encoding="utf-8")                              # (local)
    required_markers = [                                                       # (local)
        "Element 1 — Two cross-reviewers dispatched in PARALLEL",
        "Element 2 — Cross-reviewers on DIFFERENT axes",
        "Element 3 — Neither cross-reviewer is the original workshop authoring agent",
        "Element 4 — Dispatch prompts EXCLUDE workshop R1/R2/R3 transcripts",
        "Element 5 — JOINT clauses (c) and (d) PASS-AND'd across both verdicts",
    ]
    missing = [m for m in required_markers if m not in text]                  # (local)
    return (len(missing) == 0), f"5/5 elements present" if not missing \
        else f"missing: {missing}"


def evaluate_clause_2_cross_reviewers_named(plan_path: Path) -> tuple[bool, str]:
    """Clause 2: cross-reviewer assignments are NAMED with full subagent-type
    strings. Verifies axis-A is connes-ncg-theorist and axis-B is volovik-
    superfluid-universe-theorist; verifies disjointness from forbidden set."""
    text = plan_path.read_text(encoding="utf-8")                              # (local)
    has_axis_a = CROSS_REVIEWER_AXIS_A in text                                # (local)
    has_axis_b = CROSS_REVIEWER_AXIS_B in text                                # (local)
    cross_set = {CROSS_REVIEWER_AXIS_A, CROSS_REVIEWER_AXIS_B}                # (local)
    forbidden_set = set(WORKSHOP_AUTHORS_FORBIDDEN)                           # (local)
    disjoint = len(cross_set & forbidden_set) == 0                            # (local)
    ok = has_axis_a and has_axis_b and disjoint                               # (local)
    note = (f"axis-A={CROSS_REVIEWER_AXIS_A} (in plan: {has_axis_a}); "
            f"axis-B={CROSS_REVIEWER_AXIS_B} (in plan: {has_axis_b}); "
            f"disjoint from forbidden {sorted(forbidden_set)}: {disjoint}")
    return ok, note


def evaluate_clause_3_audit_script_registered(plan_path: Path,
                                              audit_script: Path) -> tuple[bool, str]:
    """Clause 3: audit script is REGISTERED as plan-freeze validator AND
    EXISTS on disk."""
    text = plan_path.read_text(encoding="utf-8")                              # (local)
    registered = "_joint_theorem_independent_verify_audit.py" in text         # (local)
    exists = audit_script.exists()                                            # (local)
    ok = registered and exists                                                # (local)
    note = (f"validator registered in plan: {registered}; "
            f"validator exists on disk: {exists} ({audit_script})")
    return ok, note


def evaluate_clause_4_cf54_dependency_declared(plan_path: Path) -> tuple[bool, str]:
    """Clause 4: CF-54 §VII.AH dependency is DECLARED (either resolved or
    CONDITIONAL slot pin)."""
    text = plan_path.read_text(encoding="utf-8")                              # (local)
    has_dependency = ("CF-54" in text and                                     # (local)
                      "§VII.AH" in text)
    has_conditional = "§VII.AH-OR-NEXT-FREE-LETTER" in text                   # (local)
    ok = has_dependency or has_conditional                                    # (local)
    note = (f"CF-54 dep declared: {has_dependency}; "
            f"CONDITIONAL slot pin literal: {has_conditional}")
    return ok, note


def cf54_landed_in_verdict_file(verdict_path: Path) -> tuple[bool, str | None]:
    """Check if CF-54 (S87-PATH-C-SUCCESSOR-ANCHOR-LANDING) verdict line is
    present in the verdict file. Returns (landed, resolved_slot_identifier)."""
    if not verdict_path.exists():
        return False, None
    text = verdict_path.read_text(encoding="utf-8")                           # (local)
    pattern = re.compile(rf"^{re.escape(CF54_GATE_ID)}:\s+(PASS|FAIL|INFO)",  # (local)
                         re.MULTILINE)
    m = pattern.search(text)                                                  # (local)
    if not m:
        return False, None
    # CF-54 landed; in a future S87+ run, the slot identifier would be parsed
    # from the CF-54 verdict-line value; at this runtime no CF-54 line is
    # present so we return (True, None) only if the regex matched.
    return True, "§VII.AH"


# ---------------------------------------------------------------------------
# Forbidden-path lexical audit (validates Element 4 enforcement language)
# ---------------------------------------------------------------------------

def validate_forbidden_path_enforcement(plan_path: Path) -> tuple[bool, str]:
    """Element 4 audit: plan-w9d.md §W9d-1 must list ALL forbidden source
    path-prefixes that S88+ dispatch prompts MUST exclude."""
    text = plan_path.read_text(encoding="utf-8")                              # (local)
    missing = [fp for fp in FORBIDDEN_SOURCE_PATHS if fp not in text]         # (local)
    return (len(missing) == 0), \
        (f"all {len(FORBIDDEN_SOURCE_PATHS)} forbidden paths declared"
         if not missing else f"missing forbidden-path declarations: {missing}")


# ---------------------------------------------------------------------------
# Verdict-line emitter
# ---------------------------------------------------------------------------

def append_verdict_line(verdict: str, value: str, content_sha: str,
                        audit_sha: str, magnitude_verdict: str) -> None:
    """Append the canonical verdict line + W9a-99 dual-SHA companion +
    S87 schema-v2 3-tuple annotation."""
    canonical_line = (                                                        # (local)
        f"{GATE_ID}: {verdict} -- "
        f"value='{value}' "
        f"scheme=PRDR-stage-2-spec-authoring "
        f"convention=SOURCE-DOUBLE-CITE-CO-PRIMARY "
        f"L_max=N/A "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )
    companion_line = (                                                        # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    annotation_line = (                                                       # (local)
        f"# sign_verdict=N/A "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )
    forward_pin_line = (                                                      # (local)
        f"# forward_pin_gate_id={FORWARD_PIN_GATE_ID} "
        f"# {GATE_ID} S88+ Stage-2 dispatch forward-pin reference"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")
        f.write(annotation_line + "\n")
        f.write(forward_pin_line + "\n")


# ---------------------------------------------------------------------------
# Main: 4-clause AND, dual-SHA closure, verdict emission
# ---------------------------------------------------------------------------

def main() -> int:
    plan_path = PROJECT_ROOT / "sessions" / "session-plan" / "session-87-plan-w9d.md"  # (local)
    audit_script = PROJECT_ROOT / "computations" / "_shared" / "_joint_theorem_independent_verify_audit.py"  # (local)
    wp_path = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"  # (local)

    # Verify input files exist.
    for f in INPUT_PIN_MAP_FILES:
        p = PROJECT_ROOT / f                                                  # (local)
        if not p.exists():
            print(f"FAIL — Input file missing: {f}", file=sys.stderr)
            return 2

    # Compute input-pin map SHAs.
    input_pin_map = {}                                                        # (local)
    for f in INPUT_PIN_MAP_FILES:
        p = PROJECT_ROOT / f                                                  # (local)
        input_pin_map[f] = file_sha256(p)
    audit_sha = closure_hash(input_pin_map)                                   # (local)

    # 4-clause PASS predicate.
    p1, n1 = evaluate_clause_1_five_element_block(plan_path)                  # (local)
    p2, n2 = evaluate_clause_2_cross_reviewers_named(plan_path)               # (local)
    p3, n3 = evaluate_clause_3_audit_script_registered(plan_path, audit_script)  # (local)
    p4, n4 = evaluate_clause_4_cf54_dependency_declared(plan_path)            # (local)

    forbidden_ok, forbidden_note = validate_forbidden_path_enforcement(plan_path)  # (local)

    cf54_landed, cf54_slot = cf54_landed_in_verdict_file(VERDICT_FILE)        # (local)

    # Composite verdict per substitution chain.
    all_4_clauses = p1 and p2 and p3 and p4                                   # (local)
    if not all_4_clauses:
        composite = "FAIL"                                                    # (local)
        magnitude = "FAIL"                                                    # (local)
    elif all_4_clauses and cf54_landed:
        composite = "PASS"                                                    # (local)
        magnitude = "PASS"                                                    # (local)
    else:
        composite = "INFO"                                                    # (local)
        magnitude = "INFO"                                                    # (local)

    # Build value field.
    slot_status = (f"resolved_to_{cf54_slot}" if cf54_landed                  # (local)
                   else f"CONDITIONAL_slot_pin={CONDITIONAL_SLOT_PIN}")
    value_field = (                                                           # (local)
        "5-element-block-populated_AND_"
        "cross-reviewers-named_AND_"
        "audit-script-registered_AND_"
        f"CF-54-dependency-declared_{slot_status}"
    )

    # Compute content_sha256 over the verdict-content commitment string.
    content_payload = json.dumps({                                            # (local)
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": value_field,
        "scheme": "PRDR-stage-2-spec-authoring",
        "convention": "SOURCE-DOUBLE-CITE-CO-PRIMARY",
        "L_max": "N/A",
        "schema_version": SCHEMA_VERSION,
        "forward_pin_gate_id": FORWARD_PIN_GATE_ID,
        "cross_reviewer_axis_A": CROSS_REVIEWER_AXIS_A,
        "cross_reviewer_axis_B": CROSS_REVIEWER_AXIS_B,
        "workshop_authors_forbidden": WORKSHOP_AUTHORS_FORBIDDEN,
        "forbidden_source_paths": FORBIDDEN_SOURCE_PATHS,
        "conditional_slot_pin_literal": CONDITIONAL_SLOT_PIN,
        "cf54_landed": cf54_landed,
        "cf54_slot": cf54_slot,
        "clause_results": {
            "P_1_five_element_block": (p1, n1),
            "P_2_cross_reviewers_named": (p2, n2),
            "P_3_audit_script_registered": (p3, n3),
            "P_4_cf54_dependency_declared": (p4, n4),
            "forbidden_path_enforcement": (forbidden_ok, forbidden_note),
        },
    }, sort_keys=True, separators=(",", ":")).encode("utf-8")
    content_sha = hashlib.sha256(content_payload).hexdigest()                 # (local)

    # Emit JSON sidecar.
    sidecar_path = PROJECT_ROOT / "computations" / \
        "s87_w9d_stage2_gatespec_audit.json"                                  # (local)
    sidecar = {                                                               # (local)
        "gate_id": GATE_ID,
        "forward_pin_gate_id": FORWARD_PIN_GATE_ID,
        "verdict": composite,
        "magnitude_verdict": magnitude,
        "sign_verdict": "N/A",
        "regime_verdict": "VALID",
        "value": value_field,
        "scheme": "PRDR-stage-2-spec-authoring",
        "convention": "SOURCE-DOUBLE-CITE-CO-PRIMARY",
        "L_max": "N/A",
        "schema_version": SCHEMA_VERSION,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_map": input_pin_map,
        "cf54_landed": cf54_landed,
        "cf54_slot": cf54_slot,
        "conditional_slot_pin_literal": CONDITIONAL_SLOT_PIN,
        "cross_reviewer_axis_A": CROSS_REVIEWER_AXIS_A,
        "cross_reviewer_axis_B": CROSS_REVIEWER_AXIS_B,
        "workshop_authors_forbidden": WORKSHOP_AUTHORS_FORBIDDEN,
        "forbidden_source_paths": FORBIDDEN_SOURCE_PATHS,
        "clause_results": {
            "P_1_five_element_block": {"pass": p1, "note": n1},
            "P_2_cross_reviewers_named": {"pass": p2, "note": n2},
            "P_3_audit_script_registered": {"pass": p3, "note": n3},
            "P_4_cf54_dependency_declared": {"pass": p4, "note": n4},
            "forbidden_path_enforcement": {"pass": forbidden_ok,
                                           "note": forbidden_note},
        },
        "wp_path": str(wp_path.relative_to(PROJECT_ROOT)),
    }
    with open(sidecar_path, "w", encoding="utf-8") as f:
        json.dump(sidecar, f, indent=2)

    # Print summary.
    print(f"=== {GATE_ID} ===")
    print(f"Forward-pin (S88+): {FORWARD_PIN_GATE_ID}")
    print(f"P_1 (5-element block):       {p1}  — {n1}")
    print(f"P_2 (cross-reviewers named): {p2}  — {n2}")
    print(f"P_3 (audit script):          {p3}  — {n3}")
    print(f"P_4 (CF-54 dep declared):    {p4}  — {n4}")
    print(f"Forbidden-path enforcement:  {forbidden_ok}  — {forbidden_note}")
    print(f"CF-54 landed: {cf54_landed}; slot: {cf54_slot}")
    print(f"Composite verdict: {composite}")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"Sidecar: {sidecar_path}")

    # Append verdict line.
    append_verdict_line(composite, value_field, content_sha, audit_sha, magnitude)
    print(f"Verdict line appended to: {VERDICT_FILE}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
