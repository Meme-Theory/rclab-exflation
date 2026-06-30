#!/usr/bin/env python3
"""_capstone_hygiene_gate_audit.py — Capstone-Hygiene Gate Q1-Q5 detector.

Enforces the standing capstone-hygiene gate (`.claude/rules/capstone-hygiene-gate.md`):
a session whose wave-synthesis touches the capstone `sessions/framework/phonic-exflation-
equation.md` OR a capstone-governing register (Atlas D04, the retraction log, the
permanent-results registry, the §7 falsifier surface, canonical_constants the capstone
cites) MUST carry the 5-question capstone-hygiene checklist block before the session
closes. When a capstone-touching session WP / housekeeping ledger lacks the Q1-Q5 block,
this detector emits S2 advisory (under SUGGESTION status) / S1 MANDATORY (after K=3
promotion per feedback_rules-compensate-missing-structure.md).

Pattern (per the rule's 5-question checklist):
  Q1 — alters §6.3 a(t) / effective-Friedmann gap status?
  Q2 — alters a §7 falsifier-anchor row (value / σ-distance / detector horizon / status tag)?
  Q3 — changes a PROVEN / CONDITIONAL / BROKEN / INFO status of any capstone claim?
  Q4 — is the change to a PROSE claim, not merely a ledger / registry row?
  Q5 — adds or invalidates a citation in the capstone?
Plus the routing-to-housekeeping marker (§A in-session fix / §B compute carry-forward).

DETECTOR LOGIC (two-step, matching the Class 8.7 detector shape of
`_pru_cardinality_audit.py`):
  1. Is the WP text capstone-touching? (capstone-touch regex)
  2. If yes, does it carry the Q1-Q5 checklist block + the routing marker?
     - present  -> PASS (no flag)
     - absent   -> FLAG at S2 advisory (SUGGESTION) — capstone-touch without the gate
  If NOT capstone-touching -> no_action (the gate does not apply).

--self-test: synthetic POSITIVE (a WP carrying the Q1-Q5 block -> no flag) AND
synthetic NEGATIVE (a capstone-touching WP lacking the block -> flag fires), plus a
no-touch case (a WP that does not touch the capstone -> no_action).

References:
  - `.claude/rules/capstone-hygiene-gate.md` (the standing rule this hook enforces)
  - `.claude/templates/session-housekeeping.md` (§A/§B routing target)
  - `sessions/framework/registry/capstone-hygiene-corpus.md` (calibration corpus + K-counter)
  - detector-shape template: `computations/_shared/_pru_cardinality_audit.py`
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import re
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Canonical-constants discipline (computations/_shared/CLAUDE.md). The detector
# is pure-regex; the import is the mandatory hygiene marker, not load-bearing here.
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Step-1 detectors — is the WP / ledger text CAPSTONE-TOUCHING?
# A session touches the capstone iff it references the living capstone file OR a
# capstone-governing register (Atlas D04, the retraction log, the §7 falsifier
# surface, the permanent-results registry, or a capstone-cited canonical value).
# ---------------------------------------------------------------------------
CAPSTONE_TOUCH = re.compile(
    r"phonic-exflation-equation\.md|"          # the living capstone file
    r"\bcapstone\b|"                            # explicit capstone reference
    r"atlas-04-assumptions|"                    # Atlas D04 governing register
    r"atlas-09-retractions|retraction[-_ ]log|" # the retraction log
    r"§\s*7\.[12]|"                             # the §7 falsifier-anchor surface
    r"falsifier-master-inventory|"              # the §7 falsifier inventory
    r"permanent-results-registry",              # the permanent-results register
    re.MULTILINE | re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Step-2 detectors — the Q1-Q5 capstone-hygiene checklist block.
# Each Qi marker is matched permissively: the question label `Q{n}` followed by
# its topical keyword. The block is PRESENT iff ALL FIVE markers + the routing
# marker are found.
# ---------------------------------------------------------------------------
Q1_MARKER = re.compile(
    r"\bQ1\b.*?(a\(t\)|effective[-_ ]?Friedmann|§\s*6\.3|a-?of-?t-?gap)",
    re.IGNORECASE | re.DOTALL,
)
Q2_MARKER = re.compile(
    r"\bQ2\b.*?(falsifier|§\s*7|σ-?distance|sigma-?distance|detector[-_ ]horizon|observable[-_ ]row)",
    re.IGNORECASE | re.DOTALL,
)
Q3_MARKER = re.compile(
    r"\bQ3\b.*?(PROVEN|CONDITIONAL|BROKEN|INFO|status)",
    re.IGNORECASE | re.DOTALL,
)
Q4_MARKER = re.compile(
    r"\bQ4\b.*?(prose|ledger|registry[-_ ]row|designated[-_ ]writer)",
    re.IGNORECASE | re.DOTALL,
)
Q5_MARKER = re.compile(
    r"\bQ5\b.*?(citation|cite|anchor|primary[-_ ]literature)",
    re.IGNORECASE | re.DOTALL,
)
# The routing-to-housekeeping marker (a YES routes the update to §A / §B).
ROUTING_MARKER = re.compile(
    r"housekeeping.*§\s*[AB]|"
    r"§\s*[AB].*housekeeping|"
    r"in-session.*(?:fix|resolution)|"
    r"compute[-_ ]carry-?forward|"
    r"designated-writer[-_ ]patch",
    re.IGNORECASE | re.DOTALL,
)

# Q-markers are matched per-question to avoid one Qi's DOTALL run swallowing the
# next; we constrain each marker's reach by also requiring a bounded gap.
_Q_MARKERS = {
    "Q1": Q1_MARKER,
    "Q2": Q2_MARKER,
    "Q3": Q3_MARKER,
    "Q4": Q4_MARKER,
    "Q5": Q5_MARKER,
}


def _q_marker_present(pattern: re.Pattern, text: str, max_gap: int = 220) -> bool:
    """A Q-marker is present iff the label-to-keyword gap is bounded (<= max_gap
    chars), so an unrelated later keyword does not spuriously satisfy the marker
    via the DOTALL reach."""
    for m in pattern.finditer(text):
        if (m.end() - m.start()) <= max_gap:
            return True
    return False


def detect_capstone_hygiene_block(wp_text: str,
                                  block_label: Optional[str] = None) -> dict:
    """Capstone-Hygiene Gate detector.

    Step 1: is the WP/ledger text capstone-touching?
    Step 2: if yes, does it carry the Q1-Q5 checklist block + routing marker?

    Returns a structured dict:
      - has_hygiene_flag: bool   (True iff capstone-touching AND block absent)
      - severity: "S2" (advisory until K=3) | "S1" (after K=3 MANDATORY) | "NONE"
      - capstone_touching: bool
      - capstone_touch_markers: list (the matched touch keywords)
      - q_markers_present: dict {Q1..Q5: bool}
      - routing_marker_present: bool
      - block_present: bool
      - diagnostic: human-readable reason
      - block_label: cited input label (for the audit trail)
    """
    touch_hits = CAPSTONE_TOUCH.findall(wp_text)  # (local)
    capstone_touching = bool(touch_hits)  # (local)

    q_present = {
        name: _q_marker_present(pat, wp_text) for name, pat in _Q_MARKERS.items()
    }  # (local)
    routing_present = bool(ROUTING_MARKER.search(wp_text))  # (local)
    block_present = all(q_present.values()) and routing_present  # (local)

    if not capstone_touching:
        return {
            "has_hygiene_flag": False,
            "severity": "NONE",
            "capstone_touching": False,
            "capstone_touch_markers": [],
            "q_markers_present": q_present,
            "routing_marker_present": routing_present,
            "block_present": block_present,
            "diagnostic": "not_capstone_touching_gate_does_not_apply_no_action",
            "block_label": block_label,
        }

    if capstone_touching and block_present:
        return {
            "has_hygiene_flag": False,
            "severity": "NONE",
            "capstone_touching": True,
            "capstone_touch_markers": list(set(touch_hits))[:5],
            "q_markers_present": q_present,
            "routing_marker_present": routing_present,
            "block_present": True,
            "diagnostic": (
                "capstone_touching_AND_Q1-Q5_block_present_AND_routing_marker_present_PASS"
            ),
            "block_label": block_label,
        }

    # capstone-touching but the Q1-Q5 block (or routing marker) is absent -> FLAG
    missing = [name for name, ok in q_present.items() if not ok]  # (local)
    if not routing_present:
        missing.append("ROUTING")
    return {
        "has_hygiene_flag": True,
        "severity": "S2",  # advisory until K=3 promotion (then S1 HARD-HALT)
        "capstone_touching": True,
        "capstone_touch_markers": list(set(touch_hits))[:5],
        "q_markers_present": q_present,
        "routing_marker_present": routing_present,
        "block_present": False,
        "diagnostic": (
            "capstone_touching_session_LACKS_5_question_hygiene_block; "
            f"missing_markers={missing}; "
            "the session touched the capstone or a capstone-governing register "
            "without running the Q1-Q5 capstone-hygiene gate "
            "(.claude/rules/capstone-hygiene-gate.md)"
        ),
        "block_label": block_label,
    }


# ---------------------------------------------------------------------------
# --self-test fixtures (synthetic POSITIVE + synthetic NEGATIVE + no-touch)
# ---------------------------------------------------------------------------

# Synthetic POSITIVE: a capstone-touching WP that DOES carry the Q1-Q5 block.
_SYNTHETIC_POSITIVE = """## §W-N Wave Synthesis — capstone status reconciliation

This wave touched the capstone phonic-exflation-equation.md and atlas-04-assumptions.md.

### Capstone-Hygiene Gate (Q1-Q5)
- Q1. a(t) / effective-Friedmann (§6.3) gap status: unchanged this wave -> no §6.3 edit.
- Q2. §7 falsifier-anchor row (value / σ-distance / detector horizon / status tag): w_a
  σ-distance updated -> routed to mack-cosmic-bridge (§7.2 + falsifier-master-inventory).
- Q3. PROVEN / CONDITIONAL / BROKEN / INFO status of a capstone claim: §5.3 residual
  permanence wording down-tagged to BROKEN per Atlas D04 T3.
- Q4. PROSE claim, not merely a ledger row: yes -> designated-writer reviewed patch.
- Q5. citation add/invalidate: no new citation this wave.

Routing: the §5.3 down-tag was effected in-session -> housekeeping ledger §A; the §7
σ-distance re-pin is a compute carry-forward -> housekeeping §B (mirrored to WP CF).
"""

# Synthetic NEGATIVE: a capstone-touching WP that LACKS the Q1-Q5 block.
_SYNTHETIC_NEGATIVE = """## §W-N Wave Synthesis — GGE relic numerics

This wave recomputed the GGE-relic spectrum and updated the capstone §5.3 narrative in
phonic-exflation-equation.md plus the retraction-log item on thermalization. The R_therm
value and the entanglement-entropy floor were re-derived. No capstone-hygiene checklist
was run; the section was edited directly.
"""

# No-touch: a WP that does NOT reference the capstone or any governing register.
_SYNTHETIC_NO_TOUCH = """## §W-N Wave Synthesis — bottom-K eigenvalue saturation

This wave verified the L_max=10 vs L_max=12 bottom-20 D_K eigenvalue stability on the
Friedrich-Bär saturation argument. Pure spectral computation; no narrative document.
"""


def run_positive_self_test() -> dict:
    """Synthetic POSITIVE: capstone-touching WP WITH the Q1-Q5 block -> NO flag."""
    result = detect_capstone_hygiene_block(_SYNTHETIC_POSITIVE, "SYNTHETIC-POSITIVE")
    return {
        "self_test_status": "PASS" if not result["has_hygiene_flag"] else "FAIL",
        "expected_flag": False,
        "actual_flag": result["has_hygiene_flag"],
        "capstone_touching": result["capstone_touching"],
        "block_present": result["block_present"],
        "q_markers_present": result["q_markers_present"],
        "routing_marker_present": result["routing_marker_present"],
        "diagnostic": result["diagnostic"],
    }


def run_negative_self_test() -> dict:
    """Synthetic NEGATIVE: capstone-touching WP WITHOUT the Q1-Q5 block -> flag FIRES."""
    result = detect_capstone_hygiene_block(_SYNTHETIC_NEGATIVE, "SYNTHETIC-NEGATIVE")
    return {
        "self_test_status": "PASS" if result["has_hygiene_flag"] else "FAIL",
        "expected_flag": True,
        "actual_flag": result["has_hygiene_flag"],
        "severity": result["severity"],
        "capstone_touching": result["capstone_touching"],
        "block_present": result["block_present"],
        "diagnostic": result["diagnostic"],
    }


def run_no_touch_self_test() -> dict:
    """No-touch WP: gate does not apply -> NO flag, no_action."""
    result = detect_capstone_hygiene_block(_SYNTHETIC_NO_TOUCH, "SYNTHETIC-NO-TOUCH")
    return {
        "self_test_status": "PASS" if (not result["has_hygiene_flag"]
                                       and not result["capstone_touching"]) else "FAIL",
        "expected_flag": False,
        "actual_flag": result["has_hygiene_flag"],
        "capstone_touching": result["capstone_touching"],
        "diagnostic": result["diagnostic"],
    }


def run_self_test() -> dict:
    """Aggregate --self-test: POSITIVE + NEGATIVE + no-touch all PASS."""
    pos = run_positive_self_test()
    neg = run_negative_self_test()
    no_touch = run_no_touch_self_test()
    overall = (
        "PASS"
        if all(t["self_test_status"] == "PASS" for t in (pos, neg, no_touch))
        else "FAIL"
    )
    return {
        "overall": overall,
        "positive": pos,
        "negative": neg,
        "no_touch": no_touch,
    }


if __name__ == "__main__":
    if "--self-test" in sys.argv or len(sys.argv) == 1:
        print("Capstone-Hygiene Gate audit — self-test (Q1-Q5 detector):")
        res = run_self_test()
        print(f"  Positive (block present):   {res['positive']}")
        print(f"  Negative (block absent):    {res['negative']}")
        print(f"  No-touch (gate N/A):        {res['no_touch']}")
        print(f"  Overall: {res['overall']}")
        sys.exit(0 if res["overall"] == "PASS" else 1)
    # File-mode: audit a given WP / ledger file path for the hygiene block.
    target = Path(sys.argv[1])
    txt = target.read_text(encoding="utf-8")
    out = detect_capstone_hygiene_block(txt, str(target))
    print(out)
    sys.exit(0)
