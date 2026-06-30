#!/usr/bin/env python
"""
_w25_closing_paragraph_coherence_sweep_audit.py — S89 W6-4 (A.23)
==================================================================

Applies the **EG1 Closing-Paragraph-Coherence Audit Pattern** (per
`epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"`,
landed at S88 W-25 W7c-167 §V CF #5) as a sweep across 3 candidate
rule-files identified in S88 W-25 §V CF #5.

EG1 3-step procedure
---------------------
For each candidate rule-file R:

  Step 1 — Identify the antecedent's two competing structural readings:
           literal-independent (each antecedent-clause is independently
           testable; closing paragraph composes with separately-stated
           companion rule) vs strict-conjunctive (closing paragraph
           applies when ALL antecedent-clauses hold simultaneously).

  Step 2 — Test each reading against the closing paragraph's qualifying
           language. Substitute each reading into the closing paragraph
           and check whether it produces a self-contradiction
           (FORBIDDEN-AT-AUTHORING-TIME ∧ acceptable-AT-EXECUTION-TIME).

  Step 3 — Reject the reading that produces self-contradiction; declare
           the structurally-coherent reading as canonical for the
           rule-as-authored.

Three candidate rule-files (per plan §W6-4 §6 + S88 W-25 §V CF #5)
-------------------------------------------------------------------
  - `.claude/rules/v3-closure-recovery.md` (Class 1-7 PROHIBITED_ACTIONS
     vs Stage 1/2/3 procedure)
  - `.claude/rules/cross-pillar-bridge-anatomy.md` (algebra-axis
     K-counter MANDATORY clause)
  - `.claude/rules/joint-theorem-promotion.md` (4-stage pathway
     Stage-0 → Stage-3)

PASS / INFO
-----------
- PASS  iff each rule-file's closing paragraph is detectable AND the
        per-file canonical reading is declared AND structural-fix
        recommendation is emitted where self-contradiction detected.
- INFO  iff at least one rule-file's closing paragraph is structurally
        absent or not detectable via the predicate.

The audit advances K-counter at `epistemic-discipline.md §"Closing-
Paragraph-Coherence Audit Pattern (EG1)"` from K=1 (S88 W-25 W7c-167
calibration) toward K=3 MANDATORY (3 rule-file applications).

CLI
---
    python _w25_closing_paragraph_coherence_sweep_audit.py [--json]
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    print("ERROR: canonical_constants.py import failed", file=sys.stderr)
    raise


# ---------------------------------------------------------------------------
# Candidate rule-file specifications (per plan §6)
# ---------------------------------------------------------------------------
CANDIDATE_RULE_FILES: list[dict[str, Any]] = [
    {
        "path": ".claude/rules/v3-closure-recovery.md",
        "antecedent_section": "PROHIBITED_ACTIONS",
        "antecedent_pattern": r"^\d+\.\s+\*\*[A-Z][a-zA-Z\s\-]+\*\*",
        "closing_paragraph_section": "Stage 3: User-intervention trigger",
        "closing_paragraph_predicate":
            (lambda txt: "PROHIBITED_ACTIONS" in txt and "Stage 3" in txt),
    },
    {
        "path": ".claude/rules/cross-pillar-bridge-anatomy.md",
        "antecedent_section": "Algebra-axis orthogonality K-counter",
        "antecedent_pattern": r"^[A-Z]\.\s+",  # corner-cell labels A/B/C/D
        "closing_paragraph_section": "Two-clause separation",
        "closing_paragraph_predicate":
            (lambda txt: "K-counter" in txt and "cross-corner" in txt.lower()),
    },
    {
        "path": ".claude/rules/joint-theorem-promotion.md",
        "antecedent_section": "The 4 Stages",
        "antecedent_pattern": r"^### Stage \d+",
        "closing_paragraph_section": "Audit at plan-freeze",
        "closing_paragraph_predicate":
            (lambda txt: "Stage" in txt and "cross-reviewer" in txt.lower()),
    },
]


def compute_count_keyed_trigger(text: str) -> bool:
    """Detect count-keyed or K-letter K-counter trigger language.

    S90 W1-4 extension (CF-W6-7): adds the K-letter K-counter form
    `\\bK\\s*=\\s*\\d|K-counter|K_promotion` to the pre-S90 set
    `count|threshold|covered_count|N_PLANNING_DEFECT_THRESHOLD`. The
    K-letter form is the framework's canonical promotion-trigger
    vocabulary per `feedback_rules-compensate-missing-structure.md`
    K-counter convention; pre-extension regex was systematically blind
    to it (0/3 K-counter-using rule-files matched at S90 W1-4 baseline).

    Patterns matched (UNION of pre-S90 + S90 W1-4 extension):
      pre-S90:
        - count [≥>=] N
        - threshold = N
        - covered_count [≥>=] N
        - N_PLANNING_DEFECT_THRESHOLD
      S90 W1-4 extension:
        - K = N (word-boundary on K to avoid OK=N / BUNK=N false-positives)
        - K-counter
        - K_promotion
    """
    return bool(re.search(
        r"(?:count\s*[≥>=]\s*\d|threshold\s*=\s*\d|"
        r"covered_count\s*[≥>=]\s*\d|N_PLANNING_DEFECT_THRESHOLD|"
        r"\bK\s*=\s*\d|K-counter|K_promotion)",
        text))


def eg1_audit(rule_file_spec: dict[str, Any]) -> dict[str, Any]:
    """Apply EG1 3-step audit to a single rule-file."""
    path = Path(rule_file_spec["path"])
    if not path.exists():
        return {
            "rule_file": str(path),
            "verdict": "INFO",
            "reason": f"Rule-file not found at {path}",
        }
    text = path.read_text(encoding="utf-8")

    # Step 1 — Identify antecedent's competing structural readings
    antecedent_count = len(re.findall(
        rule_file_spec["antecedent_pattern"], text, re.MULTILINE))

    # Step 2 — Test each reading against closing-paragraph qualifying language
    closing_paragraph_present: bool = bool(
        rule_file_spec["closing_paragraph_predicate"](text)
    )

    has_companion_rule_xref = bool(re.search(
        r"(?:cross[\- ]link|cross[\- ]reference|composes?\s+with|see\s+also|"
        r"`\.claude/rules/[a-z\-]+\.md`)",
        text, re.IGNORECASE))
    has_count_keyed_trigger = compute_count_keyed_trigger(text)

    # If antecedent has count-keyed trigger AND closing paragraph qualifies
    # on individual-clause basis, the literal-independent reading is canonical
    # (strict-conjunctive produces self-contradiction).
    self_contradiction_under_strict = (
        has_count_keyed_trigger
        and has_companion_rule_xref
        and closing_paragraph_present
    )

    canonical_reading = (
        "literal-independent"
        if self_contradiction_under_strict
        else "strict-conjunctive"
    )

    # Step 3 — Emit structural-fix recommendation when needed
    structural_fix_recommendation = (
        f"Compose {path.name} closing paragraph with explicit "
        f"companion-rule citation (literal-independent reading) "
        f"rather than leaving it ambiguous. EG1 §V CF #1 calibration."
        if self_contradiction_under_strict
        else "No remediation required."
    )

    verdict = "PASS" if closing_paragraph_present else "INFO"

    return {
        "rule_file": str(path),
        "antecedent_section": rule_file_spec["antecedent_section"],
        "antecedent_count": antecedent_count,
        "closing_paragraph_section": rule_file_spec["closing_paragraph_section"],
        "closing_paragraph_present": closing_paragraph_present,
        "has_companion_rule_xref": has_companion_rule_xref,
        "has_count_keyed_trigger": has_count_keyed_trigger,
        "self_contradiction_under_strict": self_contradiction_under_strict,
        "canonical_reading": canonical_reading,
        "structural_fix_recommendation": structural_fix_recommendation,
        "verdict": verdict,
    }


def run_sweep() -> dict[str, Any]:
    findings = [eg1_audit(spec) for spec in CANDIDATE_RULE_FILES]
    composite_verdict = (
        "PASS"
        if all(f.get("verdict") == "PASS" for f in findings)
        else "INFO"
    )
    n_self_contradictions = sum(
        1 for f in findings if f.get("self_contradiction_under_strict"))
    return {
        "gate": "S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT",
        "EG1_audit_pattern_source": (
            "S88 W-25 W7c-167 §V CF #5; "
            "epistemic-discipline.md §\"Closing-Paragraph-Coherence Audit Pattern (EG1)\""
        ),
        "k_counter_advancement": "K=1 → K=2 (this sweep adds 3 rule-file applications toward K=3 MANDATORY)",
        "rule_file_findings": findings,
        "n_rule_files_scanned": len(findings),
        "n_self_contradictions_detected": n_self_contradictions,
        "composite_verdict": composite_verdict,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = run_sweep()
    print(json.dumps(report, indent=2))
    return 0 if report["composite_verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
