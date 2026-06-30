#!/usr/bin/env python3
"""
_plan_line_anchor_validator.py — plan-freeze registry-line-anchor drift validator (S93+)

Gate: S93-W9-1-PLAN-LINE-ANCHOR-VALIDATOR ([AUDIT])

Purpose
-------
Detect registry-line-anchor drift in wave plans BEFORE dispatch. A plan-block
that cites a `permanent-results-registry.md` entry by LINE NUMBER (via a
`section_anchor_lines: "L1-L2"` field, or a bare `lines NNNN-MMMM` / `line ~NNNN`
citation adjacent to a registry mention) is pinning a number that DRIFTS every
time the registry grows (a §VII landing above the cited entry pushes it down).
The S92 W4/W5 waves hit this live: three citations had drifted +106 / +229 /
+56 lines between plan-freeze and dispatch, and a fourth (~150 lines) surfaced
in S92 W5. Agents rescued each at runtime via heading-anchor grep per
`substrate-first-canonical-sourcing.md §(ii.B)`, but prevention at plan-freeze
is cheaper than rescue at dispatch.

This validator does NOT trust the cited line number. Instead it extracts the
registry HEADING ANCHOR the citation claims to point at (the `### §VII.X ...` /
`## §VII.X ...` slot named in the surrounding plan text / gate_id / hypothesis),
greps the CURRENT `sessions/permanent-results-registry.md` for that heading,
finds its ACTUAL line number L_actual, and computes:

    drift = |L_plan_anchor - L_actual|

where L_plan_anchor is the start anchor of the cited `section_anchor_lines`
range (or the bare cited line). It then emits severity per the pre-registered
band:

    drift <= 50            -> NO-ACTION
    50  < drift <= 200     -> S2 ADVISORY
    drift  > 200           -> S1 MANDATORY  (halts plan-freeze; recommends
                              runtime-rescue per substrate-first-canonical-
                              sourcing.md §(ii.B))

Layer-Functor F framing (epistemic-discipline.md §"Layer-Decomposition")
------------------------------------------------------------------------
NON-PHONONIC. This validator is the audit-floor F-image of the substrate
PRU-drift problem. Under F: substrate -> methodology -> audit, a plan-pinned
registry line number is the methodology-floor image of a substrate machinery-
pin (the upstream gate's output the plan-block consumes); the line-anchor
validator is the audit-line image of the substrate's numerical PASS-predicate.
No D_K eigenvalue is computed; the validator enforces that methodology-floor
citations stay coherent with the registry's actual structure.

Relationship to _plan_upstream_pin_validator.py
------------------------------------------------
Sibling / extension. `_plan_upstream_pin_validator.py` cross-checks plan-pinned
machinery pins (L_max, n_tau, scheme, convention) against the actual `.npz`
payload an upstream gate emitted. THIS validator cross-checks plan-pinned
registry LINE NUMBERS against the actual registry HEADING-line index. The two
are orthogonal axes of the same plan-freeze coherence discipline:

  - _plan_upstream_pin_validator.py : upstream npz-payload pin consistency
  - _plan_line_anchor_validator.py  : registry line-anchor consistency

This module reuses `_plan_upstream_pin_validator`'s gate-block splitter
(`_extract_gate_blocks`) and table parser (`_parse_table_rows`) when available
(integration hook), falling back to local copies if the import fails.

Usage
-----
    python _plan_line_anchor_validator.py <plan_file.md> [<plan_file.md> ...]
    python _plan_line_anchor_validator.py --json <plan_file.md>
    python _plan_line_anchor_validator.py --strict <plan_file.md>  # exit 1 on any S2+
    python _plan_line_anchor_validator.py --self-test              # run calibration-corpus self-test

Exit codes
----------
    0 — no drift > drift_S1_floor (no S1 MANDATORY); plan-freeze may proceed.
        (S2 ADVISORY does not halt unless --strict.)
    1 — at least one S1 MANDATORY drift (halts plan-freeze), OR (with --strict)
        at least one S2 ADVISORY, OR a self-test failure.
    2 — plan file parse error.

No framework constants imported (NON-PHONONIC methodology tool).
Local intermediates tagged `# (local)` per .claude/rules/math-scripts.md.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU cap (text grep only; no linalg)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local) CPU cap

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

# ------------------------------------------------------------------
# Integration hook — reuse _plan_upstream_pin_validator gate-splitter
# ------------------------------------------------------------------
# This validator EXTENDS _plan_upstream_pin_validator.py: it borrows that
# module's gate-block splitter and table-row parser so the two validators
# parse plan files identically. If the import fails (e.g., the sibling module
# is renamed), fall back to the local copies defined below.
try:
    from _plan_upstream_pin_validator import (  # type: ignore
        _extract_gate_blocks as _upstream_extract_gate_blocks,
        _parse_table_rows as _upstream_parse_table_rows,
    )
    _HAVE_UPSTREAM = True  # (local)
except Exception:
    _upstream_extract_gate_blocks = None  # type: ignore
    _upstream_parse_table_rows = None  # type: ignore
    _HAVE_UPSTREAM = False  # (local)


# ------------------------------------------------------------------
# Self-PRDR pin block (CF-S93-PLAN-LINE-ANCHOR-VALIDATOR origin)
# ------------------------------------------------------------------
DRIFT_S2_FLOOR: int = 50    # S2 ADVISORY threshold (lines); pre-registered
DRIFT_S1_FLOOR: int = 200   # S1 MANDATORY threshold (lines); pre-registered
REGISTRY_PATH_DEFAULT: str = "sessions/permanent-results-registry.md"

# Calibration corpus: the 4 known S92 W4/W5 drift instances (verbatim from
# session-92-w4-workingpaper.md:762 + the S92 W5 ~150-line drift).
# Each tuple: (slot, drift_lines, expected_severity)
CALIBRATION_CORPUS: tuple[tuple[str, int, str], ...] = (
    ("VII.AR",           106, "S2"),  # plan-pinned 17170-17208 -> runtime 17276-17326 (17276-17170=106)
    ("VII.AW.OP-PROJ",   229, "S1"),  # plan-pinned 18020/18054 -> runtime 18249 (18249-18020=229)
    ("VII.U.2",           56, "S2"),  # Corner II row +56-equivalent (grep-anchor-validated drift class)
    ("S92-W5",           150, "S2"),  # S92 W5 ~150-line drift the W5 planner hit
)

# ------------------------------------------------------------------
# Regex patterns
# ------------------------------------------------------------------
# `section_anchor_lines: "L1-L2"` (or 'L1-L2', or unquoted L1-L2) field
RE_SECTION_ANCHOR_LINES = re.compile(
    r"section_anchor_lines\s*[:=]\s*['\"]?(\d+)\s*[-–]\s*(\d+)['\"]?",
    re.I,
)  # (local)
# Bare registry-line citations adjacent to a permanent-results-registry mention:
#   "registry lines 17170-17208" / "lines 17170-17208" / "line ~17276" / "at line 13017"
RE_BARE_LINE_RANGE = re.compile(
    r"\b(?:registry\s+)?lines?\s*~?\s*(\d+)(?:\s*[-–]\s*(\d+))?",
    re.I,
)  # (local)
# §VII slot anchor mention (the heading the citation claims to point at).
# Captures the slot id after a § marker, e.g. "§VII.AW.OP-PROJ", "§VII.AR",
# "§VII.U.2". Stops at whitespace / closing punctuation.
RE_SLOT_ANCHOR = re.compile(
    r"§(VII\.[A-Z0-9]+(?:\.[A-Z0-9-]+)*)",
)  # (local)
# Registry HEADING line: `## §VII.X ...` or `### §VII.X ...` (any H2-H4).
# The slot id is captured for exact-match comparison.
RE_REGISTRY_HEADING = re.compile(
    r"^#{2,4}\s+§(VII\.[A-Z0-9]+(?:\.[A-Z0-9-]+)*)\b",
)  # (local)


# ------------------------------------------------------------------
# Local fallbacks (used only if the _plan_upstream_pin_validator import fails)
# ------------------------------------------------------------------
_RE_GATE_HEADER = re.compile(r"^##\s+§(W[\w-]+-\d+)\.\s+([A-Z][\w-]+)", re.M)  # (local)
_RE_ANY_H2 = re.compile(r"^##\s+", re.M)  # (local)
_RE_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$", re.M)  # (local)


def _local_extract_gate_blocks(plan_text: str) -> list[dict[str, Any]]:
    """Fallback gate-block splitter (mirrors _plan_upstream_pin_validator)."""
    headers = list(_RE_GATE_HEADER.finditer(plan_text))  # (local)
    all_h2 = list(_RE_ANY_H2.finditer(plan_text))  # (local)
    blocks = []  # (local)
    for h in headers:
        start = h.end()  # (local)
        next_h2 = [m.start() for m in all_h2 if m.start() > h.start()]  # (local)
        end = next_h2[0] if next_h2 else len(plan_text)  # (local)
        blocks.append({
            "gate_anchor": h.group(1),
            "gate_id_candidate": h.group(2),
            "header_line": h.group(0),
            "body": plan_text[start:end],
        })
    return blocks


def extract_gate_blocks(plan_text: str) -> list[dict[str, Any]]:
    """Split plan file into per-gate blocks (uses the upstream splitter if available)."""
    if _HAVE_UPSTREAM and _upstream_extract_gate_blocks is not None:
        return _upstream_extract_gate_blocks(plan_text)
    return _local_extract_gate_blocks(plan_text)


# ------------------------------------------------------------------
# Severity band map (pre-registered; monotone non-decreasing in drift)
# ------------------------------------------------------------------
def severity(drift: int) -> str:
    """Map a drift line-count to its pre-registered severity band.

    drift <= DRIFT_S2_FLOOR (50)            -> NO-ACTION
    DRIFT_S2_FLOOR < drift <= DRIFT_S1_FLOOR (200) -> S2 (ADVISORY)
    drift > DRIFT_S1_FLOOR (200)            -> S1 (MANDATORY)

    Monotone non-decreasing in drift by construction (larger drift => at-least-
    as-severe). See the §W9-1 substitution chain.
    """
    if drift <= DRIFT_S2_FLOOR:
        return "NO-ACTION"
    if drift <= DRIFT_S1_FLOOR:
        return "S2"
    return "S1"


def severity_label(sev: str) -> str:
    """Human-readable severity label."""
    return {
        "NO-ACTION": "NO-ACTION",
        "S2": "S2 ADVISORY",
        "S1": "S1 MANDATORY",
    }.get(sev, sev)


# ------------------------------------------------------------------
# Registry heading-line index
# ------------------------------------------------------------------
def build_registry_heading_index(registry_text: str) -> dict[str, int]:
    """Parse the registry into a {slot_id: line_number} map (1-based lines).

    Scans every H2-H4 `## §VII.X ...` heading. The slot id is the full dotted
    suffix after `§` (e.g. `VII.AW.OP-PROJ`). When a slot appears more than once
    (top-table row + body block), the FIRST occurrence wins (top-table rows are
    one-liners; the body block is the substantive anchor — but for drift
    detection the earliest heading-line is the conservative anchor). Callers
    that need the body block specifically should grep for the H2/H3 form.
    """
    index: dict[str, int] = {}  # (local)
    for lineno, line in enumerate(registry_text.splitlines(), start=1):
        m = RE_REGISTRY_HEADING.match(line)  # (local)
        if m:
            slot = m.group(1)  # (local) e.g. "VII.AW.OP-PROJ"
            if slot not in index:
                index[slot] = lineno
    return index


def grep_registry_heading_line(slot: str, heading_index: dict[str, int]) -> Optional[int]:
    """Return the actual line number of a §VII slot heading, or None if absent.

    Exact match first; then a prefix-aware fallback (a citation to `VII.AW` when
    the registry has `VII.AW.OP-PROJ` resolves to the OP-PROJ child only if it
    is the unique extension — otherwise the bare slot is treated as absent so
    the ambiguity surfaces rather than silently mis-resolving).
    """
    if slot in heading_index:
        return heading_index[slot]
    # Prefix-aware fallback: `VII.AW` -> `VII.AW.OP-PROJ` if unique extension.
    candidates = [
        (s, ln) for s, ln in heading_index.items()
        if s == slot or s.startswith(slot + ".")
    ]  # (local)
    if len(candidates) == 1:
        return candidates[0][1]
    return None


# ------------------------------------------------------------------
# Citation extraction from a plan-block
# ------------------------------------------------------------------
def extract_line_citations(body: str) -> list[dict[str, Any]]:
    """Extract every registry-line citation from a plan-block body.

    Returns a list of {kind, l_start, l_end, l_anchor, slot} dicts.
      - kind: "section_anchor_lines" or "bare_line_range"
      - l_start, l_end: the cited line range (l_end == l_start for a point)
      - l_anchor: the START anchor used for drift (matches the W4 WP convention,
        where +106 = 17276 - 17170 is start-to-start)
      - slot: the §VII slot id the citation is associated with (nearest § marker
        in the same body), or None if no slot anchor is found.

    Only citations whose surrounding text mentions `permanent-results-registry`
    (or a §VII slot) are treated as registry-line citations; bare line numbers
    inside unrelated prose are skipped via the slot-association requirement.
    """
    citations: list[dict[str, Any]] = []  # (local)

    # Pre-compute slot-anchor positions in the body for nearest-slot association.
    slot_positions = [
        (m.start(), m.group(1)) for m in RE_SLOT_ANCHOR.finditer(body)
    ]  # (local)

    def nearest_slot(pos: int) -> Optional[str]:
        """Find the §VII slot whose marker is nearest to character `pos`."""
        if not slot_positions:
            return None
        best = min(slot_positions, key=lambda sp: abs(sp[0] - pos))  # (local)
        # Require the slot to be within a reasonable window (same gate-block).
        if abs(best[0] - pos) > 4000:
            return None
        return best[1]

    # (1) section_anchor_lines fields
    for m in RE_SECTION_ANCHOR_LINES.finditer(body):
        l1 = int(m.group(1))  # (local)
        l2 = int(m.group(2))  # (local)
        slot = nearest_slot(m.start())  # (local)
        citations.append({
            "kind": "section_anchor_lines",
            "l_start": l1,
            "l_end": l2,
            "l_anchor": l1,
            "slot": slot,
            "raw": m.group(0),
        })

    # (2) bare registry-line citations — only when a registry mention is in the
    #     same body (the plan-block is talking about the registry).
    body_mentions_registry = "permanent-results-registry" in body  # (local)
    if body_mentions_registry:
        for m in RE_BARE_LINE_RANGE.finditer(body):
            l1 = int(m.group(1))  # (local)
            l2 = int(m.group(2)) if m.group(2) else l1  # (local)
            # Skip tiny line numbers that are almost certainly NOT registry
            # citations (e.g. "lines 1-5" in unrelated prose); registry is
            # > 10k lines, slots of interest are 4-5 digit.
            if l1 < 1000:
                continue
            slot = nearest_slot(m.start())  # (local)
            citations.append({
                "kind": "bare_line_range",
                "l_start": l1,
                "l_end": l2,
                "l_anchor": l1,
                "slot": slot,
                "raw": m.group(0),
            })

    return citations


# ------------------------------------------------------------------
# Validation core
# ------------------------------------------------------------------
def validate_plan_file(
    plan_path: Path,
    registry_path: Path,
) -> dict[str, Any]:
    """Validate one wave plan file against the current registry heading index.

    Returns a report dict with overall verdict and per-citation drift findings.
    """
    if not plan_path.exists():
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": f"Plan file not found: {plan_path}",
        }
    if not registry_path.exists():
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": f"Registry file not found: {registry_path}",
        }
    try:
        plan_text = plan_path.read_text(encoding="utf-8")
        registry_text = registry_path.read_text(encoding="utf-8")
    except OSError as e:
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": f"Read failure: {e!r}",
        }

    heading_index = build_registry_heading_index(registry_text)  # (local)
    blocks = extract_gate_blocks(plan_text)  # (local)
    if not blocks:
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": "No gate blocks (## §W{i}-{n}) found in plan file.",
        }

    findings: list[dict[str, Any]] = []  # (local)
    n_s1 = 0  # (local) S1 MANDATORY count
    n_s2 = 0  # (local) S2 ADVISORY count
    n_noaction = 0  # (local)
    n_unresolved = 0  # (local) citations whose slot heading is absent

    for blk in blocks:
        gate_anchor = blk["gate_anchor"]  # (local)
        body = blk["body"]  # (local)
        citations = extract_line_citations(body)  # (local)
        for cit in citations:
            slot = cit["slot"]  # (local)
            if slot is None:
                # No slot anchor to validate against; record as unresolved.
                n_unresolved += 1
                findings.append({
                    "gate_anchor": gate_anchor,
                    "slot": None,
                    "kind": cit["kind"],
                    "l_anchor": cit["l_anchor"],
                    "l_actual": None,
                    "drift": None,
                    "severity": "UNRESOLVED-NO-SLOT",
                    "raw": cit["raw"],
                })
                continue
            l_actual = grep_registry_heading_line(slot, heading_index)  # (local)
            if l_actual is None:
                n_unresolved += 1
                findings.append({
                    "gate_anchor": gate_anchor,
                    "slot": slot,
                    "kind": cit["kind"],
                    "l_anchor": cit["l_anchor"],
                    "l_actual": None,
                    "drift": None,
                    "severity": "UNRESOLVED-HEADING-ABSENT",
                    "raw": cit["raw"],
                })
                continue
            drift = abs(cit["l_anchor"] - l_actual)  # (local)
            sev = severity(drift)  # (local)
            if sev == "S1":
                n_s1 += 1
            elif sev == "S2":
                n_s2 += 1
            else:
                n_noaction += 1
            findings.append({
                "gate_anchor": gate_anchor,
                "slot": slot,
                "kind": cit["kind"],
                "l_anchor": cit["l_anchor"],
                "l_actual": l_actual,
                "drift": drift,
                "severity": sev,
                "raw": cit["raw"],
            })

    verdict = "FAIL" if n_s1 > 0 else "PASS"  # S1 MANDATORY halts plan-freeze
    return {
        "plan_file": str(plan_path),
        "registry_file": str(registry_path),
        "verdict": verdict,
        "n_citations": len(findings),
        "n_s1_mandatory": n_s1,
        "n_s2_advisory": n_s2,
        "n_no_action": n_noaction,
        "n_unresolved": n_unresolved,
        "drift_S2_floor": DRIFT_S2_FLOOR,
        "drift_S1_floor": DRIFT_S1_FLOOR,
        "findings": findings,
    }


# ------------------------------------------------------------------
# Calibration-corpus self-test
# ------------------------------------------------------------------
def _build_fixture_registry() -> str:
    """Build an in-memory POST-DRIFT fixture registry (the S92-era line layout).

    The fixture places the four calibration slots at the POST-DRIFT line numbers
    documented in session-92-w4-workingpaper.md:762, so that a fixture plan
    citing the PRE-DRIFT anchors produces exactly the corpus drift integers
    (106 / 229 / 56 / 150). Padding lines fill the gaps so heading line numbers
    land where intended.
    """
    # Target heading line numbers (post-drift), chosen so that
    #   drift = L_actual - L_plan_anchor  matches the corpus integers.
    # Plan anchors (pre-drift) used in the fixture plan below:
    #   VII.AR         plan_anchor = 17170 ; L_actual = 17276 ; drift = 106
    #   VII.U.2        plan_anchor = 12961 ; L_actual = 13017 ; drift =  56
    #   VII.AW.OP-PROJ plan_anchor = 18020 ; L_actual = 18249 ; drift = 229
    #   S92-W5 (use VII.BA) plan_anchor = 19000 ; L_actual = 19150 ; drift = 150
    heading_lines = {
        13017: "### §VII.U.2 — Four-corner classification fixture row",
        17276: "## §VII.AR — Rank-ordering at s=4 fixture row",
        18249: "### §VII.AW.OP-PROJ — Substrate-clock-uniqueness fixture row",
        19150: "## §VII.BA — Composite bridge-map fixture row (S92-W5 calibration)",
    }  # (local)
    max_line = max(heading_lines) + 5  # (local)
    lines = []  # (local)
    for ln in range(1, max_line + 1):
        if ln in heading_lines:
            lines.append(heading_lines[ln])
        else:
            lines.append(f"(registry filler line {ln})")
    return "\n".join(lines)


def _build_fixture_plan_with_drift() -> str:
    """Build an in-memory fixture plan citing the PRE-DRIFT anchors.

    Each gate-block cites one calibration slot by its PRE-DRIFT
    `section_anchor_lines` start anchor, so the validator computes the corpus
    drift integer against the POST-DRIFT fixture registry.
    """
    return (
        "# Fixture plan — calibration corpus (pre-drift anchors)\n\n"
        "## §W9-CAL-1. S93-FIXTURE-VII-AR\n"
        "Cites permanent-results-registry §VII.AR.\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"17170-17208\"\n"
        "```\n\n"
        "## §W9-CAL-2. S93-FIXTURE-VII-U2\n"
        "Cites permanent-results-registry §VII.U.2 Corner II row.\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"12961-13005\"\n"
        "```\n\n"
        "## §W9-CAL-3. S93-FIXTURE-VII-AW-OP-PROJ\n"
        "Cites permanent-results-registry §VII.AW.OP-PROJ Element 2.\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"18020-18054\"\n"
        "```\n\n"
        "## §W9-CAL-4. S93-FIXTURE-S92-W5\n"
        "Cites permanent-results-registry §VII.BA (S92 W5 ~150-line drift).\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"19000-19040\"\n"
        "```\n"
    )


def _build_fixture_plan_zero_drift() -> str:
    """Build an in-memory fixture plan whose anchors MATCH the registry headings.

    This is the true-negative: every cited anchor equals the fixture registry's
    actual heading line, so drift = 0 and the validator returns NO-ACTION (no
    false-positive).
    """
    # Gate-header anchors MUST end in `-<digit>` to satisfy the upstream
    # _extract_gate_blocks splitter regex (^##\s+§(W[\w-]+-\d+)\.\s+...).
    return (
        "# Fixture plan — zero-drift true-negative\n\n"
        "## §W9-CAL-90. S93-FIXTURE-ZERO-VII-AR\n"
        "Cites permanent-results-registry §VII.AR.\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"17276-17326\"\n"
        "```\n\n"
        "## §W9-CAL-91. S93-FIXTURE-ZERO-VII-U2\n"
        "Cites permanent-results-registry §VII.U.2.\n"
        "```yaml\n"
        "input_files:\n"
        "  permanent_results_registry:\n"
        "    path: \"sessions/permanent-results-registry.md\"\n"
        "    section_anchor_lines: \"13017-13060\"\n"
        "```\n"
    )


def run_self_test() -> dict[str, Any]:
    """Run the 5-test calibration-corpus self-test.

    4 true-positive tests (each corpus instance detected at correct severity) +
    1 true-negative test (zero-drift fixture returns NO-ACTION). Returns a dict
    with per-test results and an overall PASS/FAIL.
    """
    fixture_registry = _build_fixture_registry()  # (local)
    heading_index = build_registry_heading_index(fixture_registry)  # (local)

    # ---- True-positive tests: validate the drift-fixture plan ----
    plan_text = _build_fixture_plan_with_drift()  # (local)
    blocks = extract_gate_blocks(plan_text)  # (local)

    # Map each gate-block's cited slot -> computed (drift, severity).
    computed: dict[str, dict[str, Any]] = {}  # (local)
    for blk in blocks:
        for cit in extract_line_citations(blk["body"]):
            slot = cit["slot"]  # (local)
            if slot is None:
                continue
            l_actual = grep_registry_heading_line(slot, heading_index)  # (local)
            if l_actual is None:
                computed[slot] = {"drift": None, "severity": "UNRESOLVED"}
                continue
            drift = abs(cit["l_anchor"] - l_actual)  # (local)
            computed[slot] = {"drift": drift, "severity": severity(drift)}

    # The S92-W5 corpus row is realized via the §VII.BA fixture slot.
    slot_for_corpus = {
        "VII.AR": "VII.AR",
        "VII.AW.OP-PROJ": "VII.AW.OP-PROJ",
        "VII.U.2": "VII.U.2",
        "S92-W5": "VII.BA",
    }  # (local)

    tp_results: list[dict[str, Any]] = []  # (local)
    n_tp_pass = 0  # (local)
    for slot_label, expected_drift, expected_sev in CALIBRATION_CORPUS:
        fixture_slot = slot_for_corpus[slot_label]  # (local)
        got = computed.get(fixture_slot, {"drift": None, "severity": "MISSING"})  # (local)
        drift_ok = (got["drift"] == expected_drift)  # (local)
        sev_ok = (got["severity"] == expected_sev)  # (local)
        passed = bool(drift_ok and sev_ok)  # (local)
        if passed:
            n_tp_pass += 1
        tp_results.append({
            "instance": slot_label,
            "fixture_slot": fixture_slot,
            "expected_drift": expected_drift,
            "computed_drift": got["drift"],
            "expected_severity": expected_sev,
            "computed_severity": got["severity"],
            "drift_match": drift_ok,
            "severity_match": sev_ok,
            "pass": passed,
        })

    # ---- True-negative test: zero-drift fixture returns NO-ACTION ----
    zero_plan = _build_fixture_plan_zero_drift()  # (local)
    zero_blocks = extract_gate_blocks(zero_plan)  # (local)
    zero_severities: list[str] = []  # (local)
    zero_details: list[dict[str, Any]] = []  # (local)
    for blk in zero_blocks:
        for cit in extract_line_citations(blk["body"]):
            slot = cit["slot"]  # (local)
            if slot is None:
                continue
            l_actual = grep_registry_heading_line(slot, heading_index)  # (local)
            if l_actual is None:
                zero_severities.append("UNRESOLVED")
                zero_details.append({"slot": slot, "drift": None, "severity": "UNRESOLVED"})
                continue
            drift = abs(cit["l_anchor"] - l_actual)  # (local)
            sev = severity(drift)  # (local)
            zero_severities.append(sev)
            zero_details.append({"slot": slot, "drift": drift, "severity": sev})
    tn_pass = bool(zero_severities and all(s == "NO-ACTION" for s in zero_severities))  # (local)

    overall_pass = bool(n_tp_pass == len(CALIBRATION_CORPUS) and tn_pass)  # (local)

    return {
        "self_test": "S93-W9-1-PLAN-LINE-ANCHOR-VALIDATOR calibration corpus",
        "drift_S2_floor": DRIFT_S2_FLOOR,
        "drift_S1_floor": DRIFT_S1_FLOOR,
        "n_true_positive": len(CALIBRATION_CORPUS),
        "n_true_positive_pass": n_tp_pass,
        "true_positive_results": tp_results,
        "true_negative_pass": tn_pass,
        "true_negative_details": zero_details,
        "n_tests": len(CALIBRATION_CORPUS) + 1,
        "n_tests_pass": n_tp_pass + (1 if tn_pass else 0),
        "integration_hook_upstream_validator": _HAVE_UPSTREAM,
        "overall_pass": overall_pass,
    }


# ------------------------------------------------------------------
# Reporting
# ------------------------------------------------------------------
def _report_human(report: dict[str, Any]) -> None:
    print(f"=== {report['plan_file']} ===")
    if report["verdict"] == "PARSE-ERROR":
        print(f"  PARSE-ERROR: {report.get('error', 'unknown')}")
        return
    print(f"  verdict           : {report['verdict']}")
    print(f"  registry          : {report.get('registry_file', '?')}")
    print(f"  line citations    : {report['n_citations']}")
    print(f"  S1 MANDATORY      : {report['n_s1_mandatory']}")
    print(f"  S2 ADVISORY       : {report['n_s2_advisory']}")
    print(f"  NO-ACTION         : {report['n_no_action']}")
    print(f"  unresolved        : {report['n_unresolved']}")
    print(f"  drift bands       : S2>{report['drift_S2_floor']}  S1>{report['drift_S1_floor']}")
    flagged = [f for f in report["findings"] if f["severity"] in ("S1", "S2")]  # (local)
    if flagged:
        print("\n  DRIFT FINDINGS:")
        for f in flagged:
            print(f"  [{severity_label(f['severity'])}] {f['gate_anchor']} §{f['slot']}: "
                  f"plan_anchor={f['l_anchor']} actual={f['l_actual']} drift={f['drift']}")
    unresolved = [f for f in report["findings"]
                  if str(f["severity"]).startswith("UNRESOLVED")]  # (local)
    if unresolved:
        print("\n  UNRESOLVED (slot heading not found — surface, do not silently pass):")
        for f in unresolved:
            print(f"  [{f['severity']}] {f['gate_anchor']} "
                  f"§{f['slot']}: {f['raw']}")
    print()


def _report_self_test(st: dict[str, Any]) -> None:
    print("=== SELF-TEST: calibration corpus (S92 W4/W5 drift instances) ===")
    print(f"  drift bands: S2>{st['drift_S2_floor']}  S1>{st['drift_S1_floor']}")
    print(f"  integration hook (_plan_upstream_pin_validator import): "
          f"{'OK' if st['integration_hook_upstream_validator'] else 'FALLBACK'}")
    print("\n  TRUE-POSITIVE TESTS:")
    for r in st["true_positive_results"]:
        flag = "PASS" if r["pass"] else "FAIL"  # (local)
        print(f"  [{flag}] §{r['instance']}: drift {r['computed_drift']} "
              f"(expect {r['expected_drift']}) -> {r['computed_severity']} "
              f"(expect {r['expected_severity']})")
    tn = "PASS" if st["true_negative_pass"] else "FAIL"  # (local)
    print(f"\n  TRUE-NEGATIVE TEST (zero-drift fixture): [{tn}] "
          f"all-NO-ACTION={st['true_negative_pass']}")
    print(f"\n  {st['n_tests_pass']}/{st['n_tests']} tests pass; "
          f"overall={'PASS' if st['overall_pass'] else 'FAIL'}")
    print()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Plan-freeze registry-line-anchor drift validator (S93+)."
    )
    parser.add_argument("plan_files", nargs="*", help="Wave plan markdown file(s).")
    parser.add_argument("--registry", default=None,
                        help=f"Registry file (default: {REGISTRY_PATH_DEFAULT}).")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON reports instead of human-readable text.")
    parser.add_argument("--strict", action="store_true",
                        help="Exit non-zero even on S2 ADVISORY (not just S1).")
    parser.add_argument("--self-test", action="store_true",
                        help="Run the calibration-corpus self-test and exit.")
    args = parser.parse_args(argv)

    # Project root: computations/_shared/<file> -> three levels up.
    project_root = Path(__file__).resolve().parent.parent.parent  # (local)

    if args.self_test:
        st = run_self_test()  # (local)
        if args.json:
            print(json.dumps(st, indent=2, default=str))
        else:
            _report_self_test(st)
        return 0 if st["overall_pass"] else 1

    if not args.plan_files:
        parser.error("no plan files given (and --self-test not set)")

    registry_path = Path(args.registry) if args.registry else (
        project_root / REGISTRY_PATH_DEFAULT
    )  # (local)
    if not registry_path.is_absolute():
        registry_path = project_root / registry_path

    reports: list[dict[str, Any]] = []  # (local)
    for pf in args.plan_files:
        pf_path = Path(pf)
        if not pf_path.is_absolute():
            pf_path = project_root / pf
        reports.append(validate_plan_file(pf_path, registry_path))

    if args.json:
        print(json.dumps(reports, indent=2, default=str))
    else:
        for r in reports:
            _report_human(r)

    # Exit code: S1 MANDATORY (FAIL) -> 1; PARSE-ERROR -> 2; S2 under --strict -> 1.
    if any(r["verdict"] == "PARSE-ERROR" for r in reports):
        return 2
    if any(r.get("n_s1_mandatory", 0) > 0 for r in reports):
        return 1
    if args.strict and any(r.get("n_s2_advisory", 0) > 0 for r in reports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
