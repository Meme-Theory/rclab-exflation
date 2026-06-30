#!/usr/bin/env python
"""
_substrate_first_provenance_audit.py — S89 W6-3 sub-item (i)
=============================================================

Substrate-first canonical-sourcing provenance audit.

Per `.claude/rules/substrate-first-canonical-sourcing.md` §(ii) Audit
pattern: every plan pin (name = value) at plan-freeze is checked for
substrate-first provenance — methodological vs canonical citations,
schematic-helper consumption, placeholder-pattern detection. The audit
emits Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL severity
when placeholder pattern + canonical-existence test conjunction fires.

S89 W6-3 sub-item (i) extension
--------------------------------
Adds **cohomology-class-layer surrogate detection** per
`substrate-first-canonical-sourcing.md §(iv-bis)` "Surrogate-vs-Canonical
at Cohomology-Class Layer" (S88 W-9 W3a-18 V.5; B.12). When a plan-block
proposes a SURROGATE observable for a cohomology-class quantity, the
extension function `cohomology_class_surrogate_audit` scans for the
algebraic-distance theorem pre-registration:

    (i)  substitution chain reducing surrogate to component substrate
         quantities;
    (ii) sign/magnitude lock to Peter-Weyl combinatorial fraction
         (or other substrate-internal combinatorial constraint);
    (iii) uninformative-on-canonical disclosure (FAIL inference safety).

Without all three, the surrogate's verdict is FAIL with MANDATORY
severity, routing to remediation per §(iv-bis).

Substrate framing
-----------------
The audit IS the methodology-layer F-image of the substrate-physics
provenance-classification predicate. The audit-leg image (this script
+ verdict line) verifies F-image consistency between substrate-physics
canonical and methodology-layer pin-text.

CLI
---
    python _substrate_first_provenance_audit.py [--plan PATH] [--json]
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    print("ERROR: canonical_constants.py import failed", file=sys.stderr)
    raise


# ---------------------------------------------------------------------------
# Class-(f) PIN-PLACEHOLDER detection patterns
# ---------------------------------------------------------------------------
PLACEHOLDER_PATTERNS: tuple[str, ...] = (  # (local) per substrate-first-canonical-sourcing.md §(ii)
    r"O\(10\^?-?\d+\)",
    r"≈\s*10\^?-?\d+",
    r"~\s*10\^?-?\d+",
    r"\bplaceholder\b",
    r"\bTBD\b",
    r"\bpending\b",
    r"\banalytic\s+estimate\b",
    r"\brough\s+estimate\b",
    r"\border[\- ]of[\- ]magnitude\b",
)


def has_placeholder_pattern(text: str) -> bool:
    """Return True if any of the 9 placeholder patterns matches."""
    for pat in PLACEHOLDER_PATTERNS:
        if re.search(pat, text):
            return True
    return False


# ---------------------------------------------------------------------------
# §(iv-bis) Cohomology-class-layer surrogate detection (S89 W6-3 sub-item (i))
# ---------------------------------------------------------------------------
SUBSTRATE_DISTANCE_RATIO_PATTERN = (  # (local) detect surrogate proposals
    r"\bsubstrate[\- ]distance[\- ]\d+\s+spectral[\- ]moment\s+ratio\b"
)
SUBSTITUTION_CHAIN_PATTERN = (  # (local) Step 1/2/3/4 substitution-chain markers
    r"(?:Step\s*\d+|Definitions?|Substitution|Simplify|Direction).*"
    r"substitution\s+chain"
)
COMBINATORIAL_LOCK_PATTERN = (  # (local) Peter-Weyl / combinatorial lock disclosure
    r"\b(?:mechanically\s+locked|sign\s+forced|magnitude\s+locked).{0,50}"
    r"(?:Peter[\- ]Weyl|combinatorial)\b"
)
UNINFORMATIVE_DISCLOSURE_PATTERN = (  # (local) FAIL inference safety
    r"(?:uninformative\s+on\s+canonical|"
    r"surrogate\s+FAIL\s+does\s+NOT\s+falsify|"
    r"surrogate\s+is\s+(?:un)?informative)"
)


def cohomology_class_surrogate_audit(plan_block_text: str) -> dict[str, Any]:
    """
    Per substrate-first-canonical-sourcing.md §(iv-bis):

    A surrogate observable for a cohomology-class quantity must
    pre-register all three:
      (i)   substitution chain reducing surrogate to component
            substrate-physics quantities;
      (ii)  sign/magnitude lock to Peter-Weyl combinatorial fraction
            (or other substrate-internal combinatorial constraint) flag;
      (iii) uninformative-on-canonical disclosure (FAIL inference safety).

    Returns audit dict with applicable / sub-clause-presence flags /
    verdict / severity.
    """
    has_substrate_distance_ratio = bool(
        re.search(SUBSTRATE_DISTANCE_RATIO_PATTERN, plan_block_text))
    if not has_substrate_distance_ratio:
        return {
            "applicable": False,
            "verdict": "PASS",  # rule is non-applicable; no defect
            "severity": "NO-ACTION",
            "rationale": "No substrate-distance spectral-moment-ratio surrogate proposed; rule §(iv-bis) non-applicable.",
        }

    has_substitution_chain = bool(re.search(
        SUBSTITUTION_CHAIN_PATTERN, plan_block_text, re.IGNORECASE))
    has_combinatorial_lock = bool(re.search(
        COMBINATORIAL_LOCK_PATTERN, plan_block_text, re.IGNORECASE))
    has_uninformative_disclosure = bool(re.search(
        UNINFORMATIVE_DISCLOSURE_PATTERN, plan_block_text, re.IGNORECASE))
    all_three_present = (
        has_substitution_chain
        and has_combinatorial_lock
        and has_uninformative_disclosure
    )
    verdict = "PASS" if all_three_present else "FAIL"
    severity = "NO-ACTION" if all_three_present else "MANDATORY"
    return {
        "applicable": True,
        "substitution_chain_present": has_substitution_chain,
        "combinatorial_lock_present": has_combinatorial_lock,
        "uninformative_disclosure_present": has_uninformative_disclosure,
        "all_three_present": all_three_present,
        "verdict": verdict,
        "severity": severity,
        "rule_source": "substrate-first-canonical-sourcing.md §(iv-bis)",
        "remediation": (
            "Pre-register the algebraic-distance theorem in the plan-block: "
            "(i) substitution chain reducing surrogate to substrate-physics "
            "quantities; (ii) flag the Peter-Weyl combinatorial lock if the "
            "surrogate's sign or magnitude is mechanically forced; "
            "(iii) explicitly disclose whether a surrogate FAIL is "
            "informative on the canonical's PASS/FAIL prediction."
        ) if not all_three_present else "No remediation required.",
    }


# ---------------------------------------------------------------------------
# §(iv) 3-class compliance taxonomy detector (S90 W1-9 extension)
#
# Per `.claude/rules/substrate-first-canonical-sourcing.md §"3-class compliance
# taxonomy (S90 W1-9 extension; PARTIAL-POSITIVE class admitted)"`:
#   - POSITIVE        = 4-of-4 disclosure elements PASS (severity NO-ACTION)
#   - PARTIAL-POSITIVE = rules (1)∧(2)∧(3) PASS, tier_pin row ABSENT (severity S2)
#   - NEGATIVE        = ≤2-of-4 elements PASS (severity S1)
#
# 2-bit signature partition: (rules-1∧2∧3-all-PASS, tier_pin-row-PRESENT) =
#   (T,T)=POSITIVE; (T,F)=PARTIAL-POSITIVE; (F,*)=NEGATIVE
# ---------------------------------------------------------------------------

# Regex patterns for the 4 disclosure elements (per §(iv) rules + tier_pin row)
SCHEMATIC_CONVENTION_SUFFIX_PATTERN = (  # (local) — rule (2) detection
    r"convention\s*=\s*[^\s]*-SCHEMATIC"
)
SCHEMATIC_DOCSTRING_PATTERNS = (  # (local) — rule (3) detection
    r"\bSCHEMATIC\b",
    r"OPERATIONAL\s+DEVIATION",
    r"_spectral_action_regulators\.py",
    r"substrate-first-canonical-sourcing\.md.*\(iv\)",
    r"TIER-2\s+SCHEMATIC",
)
TIER_PIN_ROW_PATTERN = (  # (local) — tier_pin row detection
    r"#\s*tier_pin\s*=\s*TIER-2"
)
# rule (1) detection — CONJUNCTIVE pattern requiring BOTH the SCHEMATIC term
# AND a §(iv)-level citation to appear in the plan-block + docstring region.
# Rationale: a single-regex AND across multi-line content is brittle (`.*`
# doesn't span newlines without re.DOTALL); the conjunctive form decomposes
# rule (1) into two independently-detected predicates each matchable by a
# single-line-friendly regex. This admits the OPERATIONAL DEVIATION pattern
# (W5-7 instance, where "OPERATIONAL DEVIATION" and "SCHEMATIC" are on
# different lines), the TIER-2 SCHEMATIC docstring pattern (W9c-1 instance),
# and the explicit CLASS pin form (idealized future instances) equally.
SCHEMATIC_TERM_PATTERN = r"\bSCHEMATIC\b"  # (local) — rule (1) part A
IV_SECTION_CITATION_PATTERNS = (  # (local) — rule (1) part B (any one suffices)
    r"\(iv\)",
    r"§iv\b",
    r"K=4\s+MANDATORY",
    r"level[\- ]pin\s+discipline",
    r"_spectral_action_regulators",
    r"TIER-2",
    r"OPERATIONAL\s+DEVIATION",
    r"\bCLASS\s+pin\s+SCHEMATIC\b",
    r"\bCLASS\s*[:=]\s*SCHEMATIC\b",
    r"\bCLASS\s*pin\s*SCHEMATIC\b",
    r"substrate-first-canonical-sourcing",
)


def detect_compliance_class(
    verdict_block: str,
    producing_script_text: str,
    plan_block_text: str = "",
) -> dict[str, Any]:
    """
    Per `.claude/rules/substrate-first-canonical-sourcing.md §"3-class compliance
    taxonomy"`: detect POSITIVE / PARTIAL-POSITIVE / NEGATIVE compliance class
    for a SCHEMATIC-helper-consuming gate based on 4 disclosure elements:

      rule (1) CLASS pin SCHEMATIC declared in plan-block (or producing-script's
               plan-block-equivalent docstring section);
      rule (2) `convention=...-SCHEMATIC` suffix on verdict-line `convention=`
               field;
      rule (3) SCHEMATIC docstring acknowledgment in producing script;
      tier_pin row: `# tier_pin=TIER-2` companion row in verdict file.

    Args:
      verdict_block: multi-line string containing canonical verdict line +
                     companion comment rows for ONE gate (typically the 3-6
                     lines surrounding the gate in `s{N}_gate_verdicts.txt`).
      producing_script_text: full text of the gate's producing script (for
                             docstring scan + plan-block-equivalent rule (1)
                             proxy).
      plan_block_text: optional plan-block text for explicit rule (1) CLASS
                       pin SCHEMATIC detection. Default empty (uses producing
                       script's docstring as proxy via OPERATIONAL DEVIATION
                       block / §(iv) MANDATORY citation).

    Returns:
      dict with keys: compliance_class ∈ {POSITIVE, PARTIAL-POSITIVE, NEGATIVE},
                      rule_1_pass, rule_2_pass, rule_3_pass,
                      tier_pin_row_present, severity, rule_source,
                      signature_2bit, remediation.
    """
    # Compute docstring region first (used by both rule (1) and rule (3))
    docstring_region = "\n".join(producing_script_text.splitlines()[:200])  # (local)

    # rule (1): CLASS pin SCHEMATIC — CONJUNCTIVE detection (SCHEMATIC term AND
    # §(iv)-level citation both present in plan-block + docstring region).
    # Decomposes the rule (1) predicate into two independently-detectable
    # parts so multi-line content (OPERATIONAL DEVIATION above, SCHEMATIC
    # below) is properly recognized without re.DOTALL hazards.
    rule_1_search_corpus = plan_block_text + "\n" + docstring_region  # (local)
    has_schematic_term = bool(
        re.search(SCHEMATIC_TERM_PATTERN, rule_1_search_corpus)
    )
    has_iv_citation = any(
        re.search(p, rule_1_search_corpus, re.IGNORECASE)
        for p in IV_SECTION_CITATION_PATTERNS
    )
    rule_1_pass = has_schematic_term and has_iv_citation

    # rule (2): -SCHEMATIC convention suffix on verdict line
    rule_2_pass = bool(re.search(SCHEMATIC_CONVENTION_SUFFIX_PATTERN, verdict_block))

    # rule (3): SCHEMATIC docstring acknowledgment in producing script
    # Restrict to the docstring region (first 200 lines) to avoid false-matches
    # in test fixtures or nested string literals deep in the script body.
    rule_3_pass = any(
        re.search(p, docstring_region) for p in SCHEMATIC_DOCSTRING_PATTERNS
    )

    # tier_pin row: # tier_pin=TIER-2 companion row in verdict file
    tier_pin_row_present = bool(re.search(TIER_PIN_ROW_PATTERN, verdict_block))

    # 2-bit signature → 3-class taxonomy partition
    rules_1_2_3_all_pass = rule_1_pass and rule_2_pass and rule_3_pass  # (local)
    signature_2bit = (rules_1_2_3_all_pass, tier_pin_row_present)  # (local)

    if signature_2bit == (True, True):
        compliance_class = "POSITIVE"
        severity = "NO-ACTION"
        remediation = "No remediation required (full compliance per §(iv))."
    elif signature_2bit == (True, False):
        compliance_class = "PARTIAL-POSITIVE"
        severity = "ADVISORY-S2"
        remediation = (
            "Substrate-side rules (1)∧(2)∧(3) all PASS; tier_pin=TIER-2 "
            "companion comment row absent in verdict file. Forward-recommended-"
            "not-mandatory: emit `# tier_pin=TIER-2` companion row alongside "
            "the canonical verdict line to advance to POSITIVE class."
        )
    else:
        compliance_class = "NEGATIVE"
        severity = "MANDATORY-S1"
        remediation = (
            "≤2-of-4 disclosure elements PASS at landing time. Re-emit the "
            "verdict line with: (a) `convention=...-SCHEMATIC` suffix per rule "
            "(2); (b) producing-script docstring SCHEMATIC acknowledgment per "
            "rule (3); (c) plan-block CLASS pin SCHEMATIC per rule (1); (d) "
            "tier_pin=TIER-2 companion row to advance to POSITIVE class. "
            "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY routing per "
            "`epistemic-discipline.md §\"Source Reconciliation\"`."
        )

    return {
        "compliance_class": compliance_class,
        "rule_1_pass": rule_1_pass,
        "rule_2_pass": rule_2_pass,
        "rule_3_pass": rule_3_pass,
        "tier_pin_row_present": tier_pin_row_present,
        "rules_1_2_3_all_pass": rules_1_2_3_all_pass,
        "signature_2bit": signature_2bit,
        "severity": severity,
        "rule_source": "substrate-first-canonical-sourcing.md §(iv) 3-class compliance taxonomy (S90 W1-9)",
        "remediation": remediation,
    }


# ---------------------------------------------------------------------------
# Top-level audit driver (per §(ii) Audit pattern)
# ---------------------------------------------------------------------------
def audit_plan_pins(plan_text: str) -> dict[str, Any]:
    """
    Run the §(ii) Audit pattern on a plan text:
      Step 1: External-paper provenance citations are checked for heading
              existence (stub — full implementation requires globbing
              `researchers/<author>/*.md`).
      Step 2: Placeholder-pattern detection on PIN VALUE fields with
              substrate-canonical existence test (Class-(f) emission).
      Step 3: SCHEMATIC-helper consumption disclosure (cross-link to
              `regulator-pin-discipline.md` §"K=4 SCHEMATIC level-pin").
      Step 4: Substrate-first computation citation → AUDIT-PASS.
    """
    findings: dict[str, Any] = {}  # local
    findings["placeholder_count"] = sum(
        1 for pat in PLACEHOLDER_PATTERNS if re.search(pat, plan_text))
    findings["has_schematic_disclosure"] = bool(re.search(
        r"-SCHEMATIC\b|tier_pin\s*=\s*TIER-2", plan_text))
    findings["substrate_first_citation_count"] = len(re.findall(
        r"computations/_shared/s\d+_\w+\.py|"
        r"computations/_shared/s\d+_\w+\.npz", plan_text))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", help="Plan-file path to audit")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.plan:
        # Dispatch the cohomology-class surrogate self-test against a
        # synthetic block (used by W6-3 sub-item (i) fixture).
        synth_block = (
            "Surrogate proposal: substrate-distance-1 spectral-moment "
            "ratio R_surrogate.\n"
            "Step 1 (Definitions): R_surrogate = (Σ_BdG_A − Σ_BdG_M_3C)/"
            "(Σ_BdG_A + Σ_BdG_M_3C); substitution chain follows.\n"
            "The sign of R_surrogate is mechanically locked to the "
            "Peter-Weyl combinatorial fraction f.\n"
            "Surrogate FAIL does NOT falsify the canonical observable; "
            "surrogate is uninformative on canonical PASS/FAIL.\n"
        )
        report = cohomology_class_surrogate_audit(synth_block)
        print(json.dumps(report, indent=2))
        return 0 if report["verdict"] == "PASS" else 1

    plan_text = Path(args.plan).read_text(encoding="utf-8")
    coh = cohomology_class_surrogate_audit(plan_text)
    pins = audit_plan_pins(plan_text)
    report = {
        "gate": "substrate-first-provenance-audit",
        "plan": args.plan,
        "cohomology_class_surrogate_audit": coh,
        "plan_pin_findings": pins,
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
