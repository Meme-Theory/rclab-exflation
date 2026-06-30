#!/usr/bin/env python
"""
_plan_staleness_audit.py — S89 W6-1 (S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR)
==============================================================================

A plan-freeze pre-flight validator that scans a session plan file for
staleness signals introduced after a supersession event, plus a Stage-2
Axis-B Selection Protocol downstream-inheritance reach test extended from
runtime to plan-freeze.

Three staleness signal classes
-------------------------------
(a) **pre_supersession_pin** — input-pin SHAs referencing a literal
    threshold against a hypothesis a Bulletin already disproved
    (e.g., literal `eta_threshold_literal` per
    `regulator-pin-discipline.md` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE
    post-supersession-event extension).

(b) **downstream_inheritance_reviewer** — cross-reviewer assignments
    tainted by downstream-inheritance reach (an axis-A or axis-B
    reviewer whose project memory cites the workshop's R1/R2/R3
    transcripts as canonical reference, per
    `joint-theorem-promotion.md` §"Stage-2 Axis-B Selection Protocol"
    K=1 calibration corpus).

(c) **pre_W8_100_corrective_no_supersedes** — pre-W8-100 corrective
    verdict-line emissions that lack a `supersedes=<old_audit_sha>` tag
    (per `gate-verdicts.md` §"Option A — sig_5 remediation pathway
    under absolute verdict permanence"; S88 W8-100 forward-from-emission
    discipline).

Cross-reviewer-eligibility-audit extension
------------------------------------------
For each cross-reviewer assignment in the plan-block §VII.X gates,
verify whether the named reviewer's `.claude/agent-memory/<reviewer>/`
files cite a workshop transcript (R1/R2/R3 markers) — i.e., the
downstream-inheritance reach test extended to plan-freeze. PASS if all
reviewers are CLEAN; FAIL if any reviewer is TAINTED.

Substrate framing
-----------------
The validator IS the methodology-floor F-image of the substrate-physics
plan-staleness predicate at the layer-functor F: substrate → methodology
→ audit. The audit-leg image (this script + verdict line) verifies
F-image consistency between the plan-text content and its declared
input-pin canonicality.

CLI
---
    python _plan_staleness_audit.py --plan PLAN_FILE [--json]
    python _plan_staleness_audit.py --self-test   # invokes 3 synthetic fixtures

Verdict
-------
- PASS  iff no staleness signal fires AND no reviewer tainted.
- FAIL  iff any staleness signal fires OR any reviewer tainted.
- Severity HARD-HALT on FAIL; NO-ACTION on PASS.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

# Canonical-constants import is mandatory per math-scripts.md (S34+ scripts).
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    print("ERROR: canonical_constants.py import failed; computation compliance broken",
          file=sys.stderr)
    raise


# ---------------------------------------------------------------------------
# Staleness signal regex set (4 classes — axis 1 tightened + axis 2 added at S90 W1-3)
# ---------------------------------------------------------------------------
# S90 W1-3 axis-1 tightening: the pre_supersession_pin regex now requires
# YAML pin-map CONTEXT (line begins with optional whitespace + identifier
# + colon). Two admissible forms:
#   (a) KEY-side staleness:  `eta_threshold_literal: 0.5`
#                            `pre_supersession_pin: True`
#                            `stale_eta: ...`
#   (b) VALUE-side staleness: `some_key: pre-supersession-pinned-value`
#                             `some_key: stale_marker`
# Eliminates the W6-plan:226 prose-table false-positive
# `| 1 | pre_supersession_pin_detect | synthetic plan-block citing
#  eta_threshold_literal = 0.5 ... |` (line begins with `|`, not an
# identifier; both branches fail to anchor).
#
# S90 W1-3 axis-2 addition: the cross_wave_anchor_drift regex pre-filters
# plan-block citations of the form `A.N → §VII.X`; the substantive drift
# verification (comparing claimed vs canonical section) happens in
# cross_wave_anchor_drift_audit() below.
STALENESS_PATTERNS: dict[str, str] = {  # (local) regex pinned in script body
    "pre_supersession_pin":
        # KEY-side: staleness keyword as the WHOLE word OR keyword+separator+ext;
        # excludes letter-direct extensions like `staleness_pattern_set` (which
        # is a methodological audit-self-reference, not a stale pin).
        # VALUE-side: arbitrary KEY: + staleness keyword (with `\b` word boundary).
        r"(?im)^\s*"
        r"(?:"
        r"(?:eta_threshold_(?:literal|legacy)|pre[_-]supersession|stale)"
        r"(?:[-_]\w*)?\s*:"
        r"|"
        r"[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*[\"']?"
        r"(?:eta_threshold_(?:literal|legacy)|pre[_-]supersession|stale)\b"
        r")",
    # Either ordering is matched: "(lizzi|connes) ... Axis-X" OR "Axis-X ... (lizzi|connes)".
    # Both forms must co-occur with a workshop-transcript marker "W-N" on the same line.
    "downstream_inheritance_reviewer":
        r"(?:(?:lizzi|connes)[\w\- ]*?(?:Axis-A|Axis-B)|"
        r"(?:Axis-A|Axis-B)[\w\-: ]*?(?:lizzi|connes))"
        r"[\w\-:.,()/ ]*?\bW-\d+\b",
    "pre_W8_100_corrective_no_supersedes":
        r"^# corrective.*audit_sha256(?!.*supersedes=)",
    # NOTE: S90 W1-3 axis-2 cross_wave_anchor_drift is NOT in this dict —
    # its detection requires comparison against the canonical anchor map,
    # not pattern-match alone. The substantive check lives in
    # cross_wave_anchor_drift_audit() and emits S2 advisory (NOT HARD-HALT),
    # so it must not contribute to has_staleness above. The plan-side
    # claim regex `ANCHOR_DRIFT_PATTERN` is defined alongside that
    # function below.
}


def closure_hash(input_pin_map: dict[str, str]) -> str:
    """Closure SHA-256 over an ordered input-pin map (canonical key-sort)."""
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def sha256_of_file(path: Path) -> str:
    """SHA-256 hexdigest of a file. Returns 'MISSING' if path absent."""
    if not path.exists():
        return "MISSING"
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 hexdigest of a text string (utf-8)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Signal (a) — pre-supersession pin scan
# ---------------------------------------------------------------------------
def scan_plan_staleness(plan_text: str) -> dict[str, list]:
    """Return {pattern_name: [(line_number, line_text), ...]} per signal."""
    matches: dict[str, list] = {key: [] for key in STALENESS_PATTERNS}
    for i, line in enumerate(plan_text.splitlines(), start=1):
        for key, pat in STALENESS_PATTERNS.items():
            if re.search(pat, line):
                matches[key].append((i, line))
    return matches


# ---------------------------------------------------------------------------
# Signal (d) — Cross-wave anchor drift (S90 W1-3 axis 2)
# ---------------------------------------------------------------------------
# The pre_supersession_pin tightening (axis 1) eliminates the W6-plan:226
# prose-table false-positive. Axis 2 adds a NEW structural class:
# CROSS_WAVE_ANCHOR_DRIFT detects plan-block citations of the form
# `A.N → §VII.X` whose claimed §VII section conflicts with the canonical
# anchor map built from `sessions/permanent-results-registry.md`.
#
# Severity S2 (advisory; not HARD-HALT) per `epistemic-discipline.md
# §"Source Reconciliation"` 4-band calibration — the drift is a
# methodology-layer F-image divergence between substrate-stable
# A-number-to-§VII-slot correspondence and the plan-author's claim.
ANCHOR_DRIFT_PATTERN = (  # (local) plan-side claim regex (matches the same
                          # pre-filter pattern as STALENESS_PATTERNS["cross_wave_anchor_drift"])
    r"\b(A\.\d+)\s*→\s*(§VII\.\w+)"
)
SECTION_HEADING_PATTERN = (  # (local) registry §VII heading detector
    # Matches BOTH ## (level-2; top-level §VII.X slots like `## §VII.AR`)
    # AND ### (level-3; sub-slot rows like `### §VII.AJ.partition-stability`).
    # The slot-name capture admits letters/digits/dots/hyphens so sub-slot
    # names like `VII.AJ.partition-stability` and `VII.K-PROP` are captured
    # in full.
    r"^#{2,3}\s+§(VII\.[A-Z][A-Za-z0-9.\-]*)"
)
ANCHOR_PARENTHETICAL_PATTERN = (  # (local) S90 W1-3 corrected — A.N WITH parenthetical
    # containing "this entry/gate/row". The parenthetical bounds (`(...)`)
    # are required so cross-link lines like "A.28 (...); A.30 (... this entry); A.31"
    # do NOT incorrectly anchor A.28 to the section the line is in.
    r"\bA\.(\d+)\s*\(([^)]*(?:this entry|this gate|this row)[^)]*)\)"
)
SECTION_REF_PATTERN = (  # (local) §VII.X reference inside text or parenthetical
    r"§(VII\.[A-Za-z0-9.-]+)"
)
FORWARD_DISPATCH_ANCHOR_PATTERN = (  # (local) registry "Forward dispatch
                                      # routing: A.N (S89) ..." sub-bullet
    r"Forward dispatch routing[^\n]*?\bA\.(\d+)\b"
)


def build_canonical_anchor_to_section_map(registry_text: str) -> dict[str, str]:
    """Parse `permanent-results-registry.md` text; return {A.N: §VII.X}.

    Heuristic — an A-number is canonical for §VII.X if either:

      (i)  An "A.N (… this entry|this gate|this row …)" parenthetical
           exists somewhere in the registry text. The canonical §VII.X is:
              - the §VII.X mentioned INSIDE the parenthetical, if any
                (e.g., "A.30 (S89 Stage-2 cross-axis verify of §VII.AS
                — this entry)" → A.30 → §VII.AS regardless of which
                section the line appears in);
              - else the current section the parenthetical occurs in.
      (ii) The body of §VII.X contains "Forward dispatch routing: A.N
           (...)" — explicit downstream-dispatch anchor. Pass-2 fires
           only if pass-1 did not produce a mapping for this A.N.

    Heuristic ambiguity handling: if two parentheticals claim the same
    A.N to different §VII.X targets, the FIRST claim wins.
    """
    section_re = re.compile(SECTION_HEADING_PATTERN, re.MULTILINE)
    paren_re = re.compile(ANCHOR_PARENTHETICAL_PATTERN, re.IGNORECASE)
    section_ref_re = re.compile(SECTION_REF_PATTERN)
    forward_re = re.compile(FORWARD_DISPATCH_ANCHOR_PATTERN, re.IGNORECASE)
    matches = list(section_re.finditer(registry_text))
    sections: dict[str, str] = {}  # (local) section_name → body text
    for i, m in enumerate(matches):
        section_name = m.group(1)  # (local) e.g., "VII.AS"
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(registry_text)
        sections[section_name] = registry_text[start:end]

    canonical_map: dict[str, str] = {}  # (local) A.N → §VII.X
    # Pass 1: explicit parenthetical self-anchor ("this entry"/"this gate"/"this row")
    # Inside-parenthetical §VII.X reference takes precedence over current section.
    for section_name, body in sections.items():
        for sm in paren_re.finditer(body):
            a_num = f"A.{sm.group(1)}"  # (local)
            paren_content = sm.group(2)  # (local) text between ()
            section_refs = section_ref_re.findall(paren_content)  # (local)
            if section_refs:
                # Inside-parenthetical §VII.X = canonical anchor (description's subject)
                canonical_section = f"§{section_refs[-1]}"  # (local)
            else:
                # No §VII.X inside — "this entry" refers to current section
                canonical_section = f"§{section_name}"  # (local)
            if a_num not in canonical_map:
                canonical_map[a_num] = canonical_section
    # Pass 2: forward dispatch routing references (lower precedence)
    for section_name, body in sections.items():
        for fm in forward_re.finditer(body):
            a_num = f"A.{fm.group(1)}"  # (local)
            if a_num not in canonical_map:
                canonical_map[a_num] = f"§{section_name}"
    return canonical_map


def cross_wave_anchor_drift_audit(
    plan_text: str,
    canonical_map: dict[str, str],
) -> list[dict[str, str]]:
    """Detect plan-side `A.N → §VII.X` claims that conflict with the registry's
    canonical anchor map.

    Returns a list of drift findings; each finding is a dict with
    keys: `a_number`, `claimed_section`, `canonical_section`, `severity`,
    `line`. PASS = empty list; one or more findings → S2 advisory.

    A-numbers absent from the canonical map are NOT drift (the registry
    has no canonical claim to compare against — could be a forward A-number
    pre-allocated by the plan author).
    """
    drift_re = re.compile(ANCHOR_DRIFT_PATTERN)
    drifts: list[dict[str, str]] = []  # (local)
    for i, line in enumerate(plan_text.splitlines(), start=1):
        for dm in drift_re.finditer(line):
            a_num = dm.group(1)  # (local)
            claimed = dm.group(2)  # (local)
            canonical = canonical_map.get(a_num)
            if canonical is not None and canonical != claimed:
                drifts.append({
                    "a_number": a_num,
                    "claimed_section": claimed,
                    "canonical_section": canonical,
                    "severity": "S2",
                    "line": str(i),
                })
    return drifts


# ---------------------------------------------------------------------------
# Signal (b) — Stage-2 Axis-B downstream-inheritance reach test
# ---------------------------------------------------------------------------
REVIEWER_ASSIGNMENT_PATTERN = (  # (local) extracts reviewer-axis pairs
    # Greedy match on reviewer name so the suffix-ending agent identifier
    # captures the FULL hyphenated name (e.g., 'lizzi-spectral-functional-theorist')
    # not just its tail. Suffix list mirrors `.claude/templates/agent-roster.md`
    # subagent_type identifiers.
    r"\b(Axis-A|Axis-B)\s*[:\-]?\s*"
    r"([a-z][a-z0-9\-]*"
    r"(?:-theorist|-empiricist|-bridge|-mechanic|-physicist|-cosmologist|-geometer))"
)
TRANSCRIPT_REF_PATTERN = (  # (local) workshop R1/R2/R3 transcript citation
    r"workshop.*\b(?:R1|R2|R3)\b"
)


def cross_reviewer_eligibility_audit(
    plan_text: str,
    memory_root: Path,
) -> dict[str, str]:
    """
    Stage-2 Axis-B Selection Protocol downstream-inheritance reach test
    extended to plan-freeze.

    Returns {reviewer_name: status_string} where status_string is one of:
        - 'CLEAN'                    (no transcript citation in any memory file)
        - 'DOWNSTREAM-INHERITANCE-TAINTED: <list of memory-file paths>'
        - 'MEMORY-DIR-ABSENT'        (the agent-memory dir does not exist)
    """
    findings: dict[str, str] = {}
    pairs = re.findall(REVIEWER_ASSIGNMENT_PATTERN, plan_text)
    reviewers = sorted({reviewer for _axis, reviewer in pairs})
    for reviewer in reviewers:
        memory_dir = memory_root / reviewer
        if not memory_dir.exists():
            findings[reviewer] = "MEMORY-DIR-ABSENT"
            continue
        transcript_refs = []  # local
        for memfile in memory_dir.glob("*.md"):
            try:
                content = memfile.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if re.search(TRANSCRIPT_REF_PATTERN, content):
                transcript_refs.append(str(memfile))
        if transcript_refs:
            findings[reviewer] = (
                f"DOWNSTREAM-INHERITANCE-TAINTED: {transcript_refs}"
            )
        else:
            findings[reviewer] = "CLEAN"
    return findings


# ---------------------------------------------------------------------------
# Composite verdict
# ---------------------------------------------------------------------------
def audit_plan(
    plan_path: Path,
    memory_root: Path | None = None,
    registry_path: Path | None = None,
) -> dict[str, Any]:
    """Run the 4-signal staleness scan + cross-reviewer eligibility audit.

    S90 W1-3 extensions:
      - axis 1: pre_supersession_pin regex tightened to YAML pin-map context
        (eliminates W6-plan:226 false-positive).
      - axis 2: cross_wave_anchor_drift detector added; compares
        plan-block `A.N → §VII.X` claims against canonical anchor map
        built at audit-time from `permanent-results-registry.md`.
        Severity S2 (advisory; not HARD-HALT) — drift findings ARE NOT
        gate-blocking but ARE reported in the audit JSON.
    """
    if memory_root is None:
        memory_root = Path(".claude/agent-memory")
    if registry_path is None:
        registry_path = Path("sessions/permanent-results-registry.md")
    if not plan_path.exists():
        return {
            "gate": "S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR",
            "plan": str(plan_path),
            "verdict": "FAIL",
            "severity": "HARD-HALT",
            "reason": "plan-file-not-found",
        }
    plan_text = plan_path.read_text(encoding="utf-8")

    staleness = scan_plan_staleness(plan_text)
    eligibility = cross_reviewer_eligibility_audit(plan_text, memory_root)

    # Axis 2 (S90 W1-3): cross-wave anchor drift via canonical anchor map.
    drift_findings: list[dict[str, str]] = []  # (local)
    canonical_map: dict[str, str] = {}  # (local)
    if registry_path.exists():
        registry_text = registry_path.read_text(encoding="utf-8")  # (local)
        canonical_map = build_canonical_anchor_to_section_map(registry_text)
        drift_findings = cross_wave_anchor_drift_audit(plan_text, canonical_map)

    has_staleness = any(matches for matches in staleness.values())
    has_taint = any("TAINTED" in v for v in eligibility.values())
    has_drift = bool(drift_findings)

    # HARD-HALT signals: staleness signals (a/b/d as KEY-side) + reviewer taint.
    # S2 advisory only: cross-wave anchor drift (does NOT gate-block).
    verdict = "FAIL" if (has_staleness or has_taint) else "PASS"
    severity = "HARD-HALT" if verdict == "FAIL" else "NO-ACTION"

    return {
        "gate": "S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR",
        "plan": str(plan_path),
        "verdict": verdict,
        "severity": severity,
        "staleness_signals_count": sum(1 for m in staleness.values() if m),
        "staleness_signals": {
            k: [{"line": ln, "text": txt[:200]} for ln, txt in v]
            for k, v in staleness.items()
        },
        "cross_reviewer_eligibility": eligibility,
        # S90 W1-3 axis 2 sub-report
        "cross_wave_anchor_drift_findings": drift_findings,
        "cross_wave_anchor_drift_severity": "S2" if has_drift else "NONE",
        "canonical_anchor_to_section_map_size": len(canonical_map),
    }


# ---------------------------------------------------------------------------
# Synthetic fixtures (in-script self-test mode)
# ---------------------------------------------------------------------------
SYNTH_FIXTURE_1_PLAN = (  # (local) pre-supersession pin
    "## §G1 plan-block\n"
    "machinery_pin_map:\n"
    "  eta_threshold_literal: 0.5  # post-W2-7 superseded canonical\n"
)
SYNTH_FIXTURE_2_PLAN = (  # (local) downstream-inheritance reviewer
    "## §VII.W-3.LAB Stage-2\n"
    "Axis-A: lizzi-spectral-functional-theorist cross-review of W-9 R3 closure\n"
    "Axis-B: transit-dynamics-aether-mechanic\n"
)
SYNTH_FIXTURE_3_PLAN = (  # (local) corrective-without-supersedes
    "# corrective audit_sha256=abcd1234 # PASS after FAIL retry (no supersedes)\n"
)
SYNTH_FIXTURE_4_PLAN = (  # (local) cross-wave anchor drift (S90 W1-3 axis 2)
    "## §W4 plan-block\n"
    "Forward dispatch routing: A.30 → §VII.AR (drift — registry anchors A.30 at §VII.AS)\n"
    "Forward dispatch routing: A.36 → §VII.AR (correct — registry anchors A.36 at §VII.AR)\n"
)
SYNTH_FIXTURE_4_REGISTRY = (  # (local) minimal canonical anchor map source
    "### §VII.AS\n"
    "**Forward dispatch routing**: A.30 (S89 Stage-2 cross-axis verify of §VII.AS — this entry)\n"
    "\n"
    "### §VII.AR\n"
    "**Forward dispatch routing**: A.36 (S89) `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP` — this entry\n"
)


def synthetic_fixture_1() -> dict[str, Any]:
    """Pre-supersession pin detection."""
    matches = scan_plan_staleness(SYNTH_FIXTURE_1_PLAN)
    fired = bool(matches["pre_supersession_pin"])
    return {
        "fixture": 1,
        "name": "pre_supersession_pin_detect",
        "expected_signal": "pre_supersession_pin",
        "signal_fired": fired,
        "fixture_passes": fired,
    }


def synthetic_fixture_2() -> dict[str, Any]:
    """Downstream-inheritance reviewer detection (regex match only;
    eligibility-audit stub uses the transcript-ref pattern via
    in-text simulation).
    """
    matches = scan_plan_staleness(SYNTH_FIXTURE_2_PLAN)
    fired = bool(matches["downstream_inheritance_reviewer"])
    return {
        "fixture": 2,
        "name": "downstream_inheritance_reviewer_detect",
        "expected_signal": "downstream_inheritance_reviewer",
        "signal_fired": fired,
        "fixture_passes": fired,
    }


def synthetic_fixture_3() -> dict[str, Any]:
    """Pre-W8-100 corrective verdict line without supersedes tag."""
    matches = scan_plan_staleness(SYNTH_FIXTURE_3_PLAN)
    fired = bool(matches["pre_W8_100_corrective_no_supersedes"])
    return {
        "fixture": 3,
        "name": "pre_W8_100_no_supersedes_detect",
        "expected_signal": "pre_W8_100_corrective_no_supersedes",
        "signal_fired": fired,
        "fixture_passes": fired,
    }


def synthetic_fixture_4() -> dict[str, Any]:
    """Cross-wave anchor drift detection (S90 W1-3 axis 2).

    Builds canonical map from the synthetic minimal registry text:
      - A.30 → §VII.AS (anchored via "this entry")
      - A.36 → §VII.AR (anchored via "this entry")
    Then runs cross_wave_anchor_drift_audit on synthetic plan with:
      - "A.30 → §VII.AR" — DRIFT (claimed §VII.AR ≠ canonical §VII.AS)
      - "A.36 → §VII.AR" — CORRECT (claimed §VII.AR = canonical §VII.AR)
    Fixture passes iff exactly 1 drift is detected with the expected
    a_number/claimed/canonical fields.
    """
    canonical_map = build_canonical_anchor_to_section_map(SYNTH_FIXTURE_4_REGISTRY)
    drifts = cross_wave_anchor_drift_audit(SYNTH_FIXTURE_4_PLAN, canonical_map)
    expected_drift_count = 1  # (local) only A.30 → §VII.AR drifts
    n_drifts = len(drifts)  # (local)
    a30_correct = (
        n_drifts == 1
        and drifts[0]["a_number"] == "A.30"
        and drifts[0]["claimed_section"] == "§VII.AR"
        and drifts[0]["canonical_section"] == "§VII.AS"
        and drifts[0]["severity"] == "S2"
    )  # (local)
    canonical_map_correct = (
        canonical_map.get("A.30") == "§VII.AS"
        and canonical_map.get("A.36") == "§VII.AR"
    )  # (local)
    return {
        "fixture": 4,
        "name": "cross_wave_anchor_drift_detect",
        "expected_signal": "cross_wave_anchor_drift",
        "n_drifts_detected": n_drifts,
        "n_drifts_expected": expected_drift_count,
        "drifts": drifts,
        "canonical_map_built": canonical_map,
        "canonical_map_correct": canonical_map_correct,
        "fixture_passes": a30_correct and canonical_map_correct,
    }


def synthetic_fixture_5() -> dict[str, Any]:
    """Axis-1 tightening regression check (S90 W1-3).

    Verifies the tightened pre_supersession_pin regex eliminates
    the W6-plan:226-shaped prose-table false-positive while
    preserving fixture 1 (YAML pin-map context detection).

    Two checks:
      (a) Synthetic prose-table line `| 1 | pre_supersession_pin_detect |
          synthetic plan-block citing eta_threshold_literal = 0.5 ... |`
          MUST NOT match pre_supersession_pin (false-positive eliminated).
      (b) SYNTH_FIXTURE_1 YAML pin form MUST still match (regression check).
    """
    prose_table_line = (  # (local)
        "| 1 | `pre_supersession_pin_detect` | synthetic plan-block citing "
        "`eta_threshold_literal = 0.5` (post-W2-7 superseded canonical) | "
        "FAIL with `pre_supersession_pin` match |\n"
    )
    matches_prose = scan_plan_staleness(prose_table_line)
    matches_yaml = scan_plan_staleness(SYNTH_FIXTURE_1_PLAN)
    prose_false_positive_eliminated = (
        not matches_prose["pre_supersession_pin"]
    )  # (local)
    yaml_still_detected = bool(matches_yaml["pre_supersession_pin"])  # (local)
    return {
        "fixture": 5,
        "name": "axis1_tightening_regression_check",
        "prose_false_positive_eliminated": prose_false_positive_eliminated,
        "yaml_still_detected": yaml_still_detected,
        "prose_match_count": len(matches_prose["pre_supersession_pin"]),
        "yaml_match_count": len(matches_yaml["pre_supersession_pin"]),
        "fixture_passes": (prose_false_positive_eliminated
                           and yaml_still_detected),
    }


def cross_reviewer_eligibility_self_test() -> dict[str, Any]:
    """Self-test: a synthetic CLEAN reviewer + a synthetic TAINTED reviewer."""
    # The eligibility audit reads from the real .claude/agent-memory dir.
    # For self-test we run against a non-existent reviewer (CLEAN-by-absence
    # via MEMORY-DIR-ABSENT) and a real reviewer ('lizzi-spectral-functional-theorist'
    # known to have memory files). The self-test passes if the function
    # returns at least one finding (proves it executes); the absolute
    # CLEAN/TAINTED outcome is data-dependent on actual memory contents.
    plan_synth = (
        "Axis-A: lizzi-spectral-functional-theorist cross-review at S88 W-9\n"
        "Axis-B: nonexistent-fictional-theorist cross-review at S88 W-14\n"
    )
    findings = cross_reviewer_eligibility_audit(
        plan_synth, Path(".claude/agent-memory"))
    has_findings = bool(findings)
    has_memory_absent_path = any("ABSENT" in v for v in findings.values())
    return {
        "self_test": "cross_reviewer_eligibility",
        "findings": findings,
        "n_findings": len(findings),
        "self_test_passes": has_findings and has_memory_absent_path,
    }


def run_self_test() -> dict[str, Any]:
    """Run all 5 synthetic fixtures + cross-reviewer eligibility self-test.

    Fixtures 1-3 are the original S89 W6-1 set; fixtures 4-5 are added
    at S90 W1-3 (axis-2 cross-wave-anchor-drift detection + axis-1
    tightening regression check).
    """
    f1 = synthetic_fixture_1()
    f2 = synthetic_fixture_2()
    f3 = synthetic_fixture_3()
    f4 = synthetic_fixture_4()  # S90 W1-3 axis 2
    f5 = synthetic_fixture_5()  # S90 W1-3 axis 1 regression check
    rv = cross_reviewer_eligibility_self_test()
    all_pass = (
        f1["fixture_passes"] and f2["fixture_passes"]
        and f3["fixture_passes"] and f4["fixture_passes"]
        and f5["fixture_passes"] and rv["self_test_passes"]
    )
    return {
        "self_test_overall": "PASS" if all_pass else "FAIL",
        "fixture_1": f1,
        "fixture_2": f2,
        "fixture_3": f3,
        "fixture_4": f4,
        "fixture_5": f5,
        "cross_reviewer_eligibility_self_test": rv,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def run_v2_extension_subset() -> dict[str, Any]:
    """V2 extension subset (S91 W0 R9 explicit CLI exposure of S90 W1-3 v2 work).

    Per `feedback_no-asking-just-execute.md` housekeeping discipline +
    S91 context file §"REMAINING substantive items" R9 spec (T2.19): explicitly
    surface the v2-tightening fixtures (fixture 4 cross-wave-anchor-drift +
    fixture 5 axis-1 regression check) under a dedicated `--extension-v2`
    flag so downstream plan-freeze auditors can request the v2 subset
    specifically without running the full self-test corpus.

    The underlying axis-1 (pre_supersession_pin YAML pin-map context regex)
    and axis-2 (cross-wave-anchor-drift detector) tightenings landed at
    S90 W1-3; this function is the explicit CLI surface for them.

    Returns dict with:
      - v2_overall: PASS|FAIL
      - axis_1_regression_check (fixture 5): axis-1 YAML-context regex
        eliminates the prose-table false-positive
      - axis_2_cross_wave_anchor_drift (fixture 4): cross-wave-anchor
        mis-citation detector fires on the synthetic drift instance
    """
    f4 = synthetic_fixture_4()  # axis-2 cross-wave-anchor-drift detection
    f5 = synthetic_fixture_5()  # axis-1 regression check
    v2_pass = (
        f4.get("fixture_passes", False)
        and f5.get("fixture_passes", False)
    )
    return {
        "v2_overall": "PASS" if v2_pass else "FAIL",
        "axis_2_cross_wave_anchor_drift": f4,
        "axis_1_regression_check": f5,
        "provenance": (
            "S91 W0 R9 explicit CLI exposure of S90 W1-3 v2 work "
            "(pre_supersession_pin YAML pin-map context regex + "
            "cross-wave-anchor mis-citation detector); "
            "per feedback_no-asking-just-execute.md."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", help="Plan-file path to audit")
    parser.add_argument("--memory-root",
                        default=".claude/agent-memory",
                        help="Agent-memory root for cross-reviewer audit")
    parser.add_argument("--self-test", action="store_true",
                        help="Run 5 synthetic fixtures + reviewer self-test")
    parser.add_argument("--extension-v2", action="store_true",
                        help="Run S90 W1-3 v2 subset (axis-1 + axis-2 tightening fixtures only)")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON report to stdout (default: human-readable)")
    args = parser.parse_args()

    if args.extension_v2:
        report = run_v2_extension_subset()
        print(json.dumps(report, indent=2))
        return 0 if report["v2_overall"] == "PASS" else 1

    if args.self_test:
        report = run_self_test()
        print(json.dumps(report, indent=2))
        return 0 if report["self_test_overall"] == "PASS" else 1

    if not args.plan:
        parser.error("--plan PLAN_FILE required when --self-test or --extension-v2 not given")
    plan_path = Path(args.plan)
    memory_root = Path(args.memory_root)
    report = audit_plan(plan_path, memory_root)
    print(json.dumps(report, indent=2))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
