#!/usr/bin/env python3
"""_pru_cardinality_audit.py — PRU Class 8 cardinality + sub-class audit module.

Provenance: file initially created at S90 W1-12 (`S90-RULE-EXTENSION-EPISTEMIC-
PRU-CLASS-8-7-DEGENERATE-OBSERVABLE`) per `feedback_fix-in-session-never-defer.md`
discharge of the W6-3 hygiene gap documented at `sessions/archive/session-89/session-89-w6-workingpaper.md`
line 363 ("Plan §1.2 listed `_pru_cardinality_audit.py` as 'hard prerequisite'.
None of the three existed on disk. W6-1 was built without using
`_pru_cardinality_audit.py` as template (no template needed).").

Initial content (S90 W1-12 — focused scope):
  - Class 8.7 (Degenerate-Observable Pre-Flight Check) detection
  - Detection patterns P1 + P2 + degeneracy-witness check per plan §W1-12 #6
  - Self-test fixture against S89 §W1-1 FAIL plan-block (K=1 calibration corpus
    instance per `epistemic-discipline.md §"Degenerate-Observable Pre-Flight
    Check"` + `pru-class-corpus.md §"Class 8.7 Calibration Corpus"`)

Out of scope (deferred carry-forward — broader D_PRU_raw cardinality audit per
`computations/tests/test_pru_cardinality_audit.py` expectations: self-audit
D_PRU_raw=0, coupling-rank, plan-parser, script-parser, substitution-chain
arithmetic). The test fixture for the broader audit has been on disk since S84
W9A-97 without the implementation; the broader audit is a separate carry-
forward NOT discharged by §W1-12 (plan §W1-12 scope is restricted to Class 8.7).

References:
  - `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` §"PRU
    Class 8 sub-class taxonomy" (row 8.7 + sub-section)
  - `sessions/framework/registry/pru-class-corpus.md §"Class 8.7 Calibration Corpus"`
  - Plan §W1-12 lines 780-857
  - S89 §W1-1 FAIL verdict audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`
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

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline

# ---------------- Class 8.7 Detection Patterns (plan §W1-12 #6) ----------------

# P1: HSS-projector trace minus regularized CM mean — the canonical S89 §W1-1
# substrate-physics pattern (line 150 of session-89-plan-w1.md):
#   S_BH^substrate(M=1e7, L_max=10) = Tr_HSS(P_HSS) − R_CM
# Per plan §W1-12: `r'Tr.*\bP_HSS\b.*−.*R_CM|Tr.*\bP_HSS\b.*-.*R_CM'`
P1_HSS_TRACE_MINUS_RCM = re.compile(
    r"Tr.*\bP_HSS\b.*[−-].*R_CM",
    re.MULTILINE,
)

# P2: zeta-D-at-zero direct value evaluation — the CM-1995 §III.4 residue formula
# entry point on a finite spectral triple. Per plan §W1-12:
#   `r'value\s*=.*ζ_D\(0\)'`
P2_ZETA_D_AT_ZERO = re.compile(
    r"value\s*=.*ζ_D\(0\)|value\s*=.*zeta_D\(0\)",
    re.MULTILINE,
)

# P5: CM-1995 §III.4 trace-residue OP-PROJ form — the §VII.AV.OP-PROJ object (iii)
# `Res_{s=N} Tr(P · D_K^{−2s})` cited as a Level-3 anchor candidate on a finite
# spectral triple. Provenance: S92 §VII.AV anchor-vs-PV reconciliation workshop
# (connes × volovik; CONVERGED 3 rounds, 2026-05-23), final-turn EFFECTED-IN-SESSION
# detector-pattern leg. Full directive + K=1 calibration corpus:
#   sessions/framework/registry/cross-pillar-bridge-corpus.md §22.
# The OP-PROJ trace-residue `Res_{s=4} Tr(P · D_K^{−2s})` on a FINITE spectral
# triple can reduce to a finite-cardinality direct-sum tautology under canonical
# Γ(s) — a Class 8.7 degeneracy. P1 (Tr·P_HSS − R_CM) and P2 (ζ_D(0)) do NOT
# match this trace-residue form; P5 closes that gap.
#
# Tightening: matches `Res_{s=...} Tr(...D_K^{−2s}...)` (ASCII `-` OR Unicode `−`
# minus in the exponent; `D_K` required in the trace). Handles `Res_{s=4}`,
# `Res_{s = 4}`, `Res_s=4`. FALSE-POSITIVE DISAMBIGUATOR (per
# `epistemic-discipline.md §"Class 8.7 pattern extensions P3 + P4"` false-positive
# disambiguator clause): a plan-block must ALSO cite OP-PROJ / Level-3-anchor
# context for P5 to fire as a degenerate-observable witness; the canonical FULL
# physical CM-1995 residue *evaluator* itself (the substrate-natural
# disambiguator) is NOT an instance of the pathology — it demonstrates the
# structural source. The OP-PROJ-context conjunct below enforces this.
P5_OP_PROJ_TRACE_RESIDUE = re.compile(
    r"Res_\{?\s*s\s*=\s*\d+\s*\}?.*Tr.*\bD_K\b.*\^?\{?\s*[−-]\s*2\s*s\s*\}?",
    re.MULTILINE,
)

# P5 context conjunct: the trace-residue must be cited as an OP-PROJ Level-3
# anchor (candidate) for the Class 8.7 witness requirement to apply. Without
# this context the bare `Res Tr(...)` is the canonical evaluator, not a
# degenerate-observable plan-block.
P5_OP_PROJ_CONTEXT = re.compile(
    r"OP-PROJ.*(Level-3|anchor)|(Level-3|anchor).*OP-PROJ",
    re.MULTILINE | re.IGNORECASE,
)

# Degeneracy-witness markers — plan §W1-12 #6 sub-section (1) Rule:
# "the plan-block MUST pre-register a degeneracy-witness: explicit declaration of
#  (a) which roots of the dimension-spectrum coincide, (b) what the multiplicity
#  at each pole is, (c) what corridor (composition (d)∘(b) per S89 W-1 R3
#  closure) the gate uses to disambiguate."
DEGENERACY_WITNESS_MARKERS = re.compile(
    r"degeneracy[-_ ]witness|"
    r"multiplicity[-_ ]at[-_ ]pole|"
    r"compositional[-_ ]corridor|"
    r"\(d\)∘\(b\)|"
    r"\(d\)\s*o\s*\(b\)|"
    r"\(d\)-composed-with-\(b\)|"
    r"dimension[-_ ]spectrum[-_ ]degenerac",
    re.MULTILINE | re.IGNORECASE,
)


def detect_class_8_7_degenerate_observable(plan_block_text: str,
                                            block_label: Optional[str] = None) -> dict:
    """Class 8.7 detector: Degenerate-Observable Pre-Flight Check.

    Detects whether a plan-block computes an observable of the form
    `Tr(P · A) − R_CM` or `ζ_D(0)` on a finite spectral triple AND fails to
    pre-register a degeneracy-witness.

    Returns a structured dict with:
      - has_class_8_7_flag: bool
      - severity: "S2" (advisory until K=3 promotion) or "NONE"
      - p1_matches: list of P1 hits
      - p2_matches: list of P2 hits
      - p5_matches: list of P5 hits (OP-PROJ trace-residue, context-gated)
      - degeneracy_witness_present: bool
      - degeneracy_witness_markers_found: list
      - diagnostic: human-readable reason
      - block_label: cited input label (for audit-trail)
    """
    p1_matches = P1_HSS_TRACE_MINUS_RCM.findall(plan_block_text)  # (local)
    p2_matches = P2_ZETA_D_AT_ZERO.findall(plan_block_text)  # (local)
    # P5 (OP-PROJ trace-residue) fires ONLY when BOTH the trace-residue form
    # AND the OP-PROJ Level-3-anchor context match (false-positive disambiguator
    # per epistemic-discipline.md §"Class 8.7 pattern extensions P3 + P4"): the
    # canonical FULL CM-1995 evaluator alone is NOT an instance of the pathology.
    p5_residue_hits = P5_OP_PROJ_TRACE_RESIDUE.findall(plan_block_text)  # (local)
    p5_context = bool(P5_OP_PROJ_CONTEXT.search(plan_block_text))  # (local)
    p5_matches = p5_residue_hits if (p5_residue_hits and p5_context) else []  # (local)
    has_degenerate_observable = (
        bool(p1_matches) or bool(p2_matches) or bool(p5_matches)
    )  # (local)

    # which pattern fired first (for the diagnostic string)
    fired = "P1" if p1_matches else ("P2" if p2_matches else "P5")  # (local)

    witness_markers_found = DEGENERACY_WITNESS_MARKERS.findall(plan_block_text)  # (local)
    degeneracy_witness_present = bool(witness_markers_found)  # (local)

    if has_degenerate_observable and not degeneracy_witness_present:
        return {
            "has_class_8_7_flag": True,
            "severity": "S2",  # advisory until K=3 promotion
            "p1_matches": p1_matches,
            "p2_matches": p2_matches,
            "p5_matches": p5_matches,
            "degeneracy_witness_present": False,
            "degeneracy_witness_markers_found": [],
            "diagnostic": (
                f"degenerate_observable_detected_via_"
                f"{fired}_AND_no_degeneracy_witness_declared; "
                f"P1_matches={len(p1_matches)};P2_matches={len(p2_matches)};"
                f"P5_matches={len(p5_matches)}; "
                f"plan-block missing the substrate-IS pre-registration of "
                f"(a) dimension-spectrum degenerate roots, "
                f"(b) multiplicity at the residue pole, "
                f"(c) the (d)∘(b) compositional corridor for disambiguation"
            ),
            "block_label": block_label,
        }
    if has_degenerate_observable and degeneracy_witness_present:
        return {
            "has_class_8_7_flag": False,
            "severity": "NONE",
            "p1_matches": p1_matches,
            "p2_matches": p2_matches,
            "p5_matches": p5_matches,
            "degeneracy_witness_present": True,
            "degeneracy_witness_markers_found": list(set(witness_markers_found))[:5],
            "diagnostic": (
                "degenerate_observable_detected_AND_degeneracy_witness_declared_PASS"
            ),
            "block_label": block_label,
        }
    return {
        "has_class_8_7_flag": False,
        "severity": "NONE",
        "p1_matches": [],
        "p2_matches": [],
        "p5_matches": [],
        "degeneracy_witness_present": False,
        "degeneracy_witness_markers_found": [],
        "diagnostic": "no_degenerate_observable_pattern_detected_no_action",
        "block_label": block_label,
    }


def extract_plan_block(plan_path: Path, block_heading: str) -> str:
    """Extract a plan-block from a plan file by its `## §W1-N. ...` heading.

    Returns block text from heading to next `\n---\n\n## ` delimiter.
    """
    text = plan_path.read_text(encoding="utf-8")  # (local)
    # Match the heading line through the next plan-block delimiter
    pattern = re.compile(
        rf"## §{re.escape(block_heading)}\..*?(?=\n---\n\n## §|\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(0) if match else ""


def run_self_test() -> dict:
    """Self-test: run Class 8.7 detector on S89 §W1-1 plan-block.

    Expected: Class 8.7 flag fires (P1 match on `Tr_HSS(P_HSS) − R_CM` at S89
    plan-w1.md line 150; no degeneracy-witness declaration in the plan-block).
    """
    s89_plan_w1 = ROOT / "sessions" / "session-plan" / "session-89-plan-w1.md"
    if not s89_plan_w1.exists():
        # S89 plans archived to session-plan/archive/ per the S52+ archival
        # convention (CLAUDE.md "Active plans (S52+; pre-S52 in
        # session-plan/archive/)"; S89 since archived). Fall back to the
        # archive path before declaring ERROR. (Path-drift fix-in-session per
        # feedback_fix-in-session-never-defer.md; surfaced at S92 §VII.AV
        # workshop final turn when extending the detector with P5.)
        s89_plan_w1 = (
            ROOT / "sessions" / "session-plan" / "archive" / "session-89-plan-w1.md"
        )
    if not s89_plan_w1.exists():
        return {
            "self_test_status": "ERROR",
            "reason": f"S89 plan-w1 not found (active or archive): {s89_plan_w1}",
        }
    block_text = extract_plan_block(s89_plan_w1, "W1-1")
    if not block_text:
        return {
            "self_test_status": "ERROR",
            "reason": "S89 §W1-1 block not extracted",
        }

    result = detect_class_8_7_degenerate_observable(block_text, "S89-§W1-1")

    return {
        "self_test_status": "PASS" if result["has_class_8_7_flag"] else "FAIL",
        "expected_flag": True,
        "actual_flag": result["has_class_8_7_flag"],
        "severity": result["severity"],
        "p1_matches_count": len(result["p1_matches"]),
        "p2_matches_count": len(result["p2_matches"]),
        "degeneracy_witness_present": result["degeneracy_witness_present"],
        "diagnostic": result["diagnostic"],
        "block_label": result["block_label"],
        "block_char_count": len(block_text),
    }


def run_negative_self_test() -> dict:
    """Negative self-test: synthetic plan-block WITH degeneracy-witness declaration.

    Expected: Class 8.7 flag does NOT fire (witness present).
    """
    synthetic_block = """## §SYNTHETIC-POSITIVE. SYNTHETIC-CLASS-8-7-COMPLIANT

Computes S_BH^substrate = Tr_HSS(P_HSS) − R_CM at M=1e7 M_sun, L_max=10.

**Degeneracy-witness**: dimension-spectrum at the substrate-distance-1 pole s=3
has multiplicity m_p=3 from the (1,0) ⊕ (0,1) ⊕ (1,1) Peter-Weyl sectors of
A_K^≤10; the (d)∘(b) compositional corridor per S89 W-1 R3 closure disambiguates
the residue evaluation via the b-channel first, then composes with d.
"""
    result = detect_class_8_7_degenerate_observable(synthetic_block, "SYNTHETIC-POSITIVE")
    return {
        "self_test_status": "PASS" if not result["has_class_8_7_flag"] else "FAIL",
        "expected_flag": False,
        "actual_flag": result["has_class_8_7_flag"],
        "severity": result["severity"],
        "p1_matches_count": len(result["p1_matches"]),
        "p2_matches_count": len(result["p2_matches"]),
        "degeneracy_witness_present": result["degeneracy_witness_present"],
        "degeneracy_witness_markers_count": len(result["degeneracy_witness_markers_found"]),
        "diagnostic": result["diagnostic"],
    }


def run_p5_op_proj_positive_self_test() -> dict:
    """P5 positive self-test: synthetic OP-PROJ trace-residue plan-block WITHOUT
    a degeneracy-witness. Expected: Class 8.7 flag FIRES via P5 (OP-PROJ context
    present, no witness). Provenance: S92 §VII.AV reconciliation workshop final
    turn (corpus §22 §22.1 Class-8.7 detector leg).
    """
    synthetic_op_proj = """## §SYNTHETIC-P5-POSITIVE. SYNTHETIC-OP-PROJ-TRACE-RESIDUE-NO-WITNESS

Pins the §VII.AV.OP-PROJ Level-3 anchor candidate as the CM-1995 §III.4 trace-residue
value = Res_{s=4} Tr(P · D_K^{−2s}) ~ 375 M_KK² on the level-2 Peter-Weyl sectors.
"""
    result = detect_class_8_7_degenerate_observable(synthetic_op_proj, "SYNTHETIC-P5-POSITIVE")
    return {
        "self_test_status": "PASS" if result["has_class_8_7_flag"] else "FAIL",
        "expected_flag": True,
        "actual_flag": result["has_class_8_7_flag"],
        "severity": result["severity"],
        "p5_matches_count": len(result["p5_matches"]),
        "diagnostic": result["diagnostic"],
    }


def run_p5_op_proj_negative_witness_self_test() -> dict:
    """P5 negative self-test A: synthetic OP-PROJ trace-residue plan-block WITH a
    degeneracy-witness. Expected: Class 8.7 flag does NOT fire (witness present).
    """
    synthetic_op_proj_witness = """## §SYNTHETIC-P5-NEGATIVE-WITNESS. OP-PROJ-RESIDUE-WITH-WITNESS

Pins the §VII.AV.OP-PROJ Level-3 anchor candidate as value = Res_{s=4} Tr(P · D_K^{−2s}).

**Degeneracy-witness**: coincident roots at the s=4 pole declared; multiplicity at pole
from the level-2 (0,2) ⊕ (1,1) ⊕ (2,0) Peter-Weyl sectors; the (d)∘(b) compositional
corridor disambiguates the residue evaluation.
"""
    result = detect_class_8_7_degenerate_observable(synthetic_op_proj_witness, "SYNTHETIC-P5-NEGATIVE-WITNESS")
    return {
        "self_test_status": "PASS" if not result["has_class_8_7_flag"] else "FAIL",
        "expected_flag": False,
        "actual_flag": result["has_class_8_7_flag"],
        "p5_matches_count": len(result["p5_matches"]),
        "degeneracy_witness_present": result["degeneracy_witness_present"],
        "diagnostic": result["diagnostic"],
    }


def run_p5_canonical_evaluator_disambiguator_self_test() -> dict:
    """P5 negative self-test B (FALSE-POSITIVE DISAMBIGUATOR): the canonical FULL
    CM-1995 §III.4 residue EVALUATOR cited WITHOUT OP-PROJ Level-3-anchor context.
    Expected: Class 8.7 flag does NOT fire — the canonical evaluator is the
    substrate-natural disambiguator demonstrating the structural source, NOT an
    instance of the pathology (per epistemic-discipline.md §"Class 8.7 pattern
    extensions P3 + P4" false-positive disambiguator clause). P5 requires the
    OP-PROJ-context conjunct, absent here.
    """
    canonical_evaluator = """## §SYNTHETIC-P5-DISAMBIGUATOR. FULL-CM-1995-III-4-RESIDUE-EVALUATOR

The FULL physical CM-1995 §III.4 residue evaluator computes Res_{s=4} Tr(P · D_K^{−2s})
across three regulators (zeta, Pauli-Villars, Mellin) returning R_zeta=141.44, R_PV=114.46,
R_Mellin=141.44 with cross_reg_spread=26.98. This is the substrate-natural disambiguator.
"""
    result = detect_class_8_7_degenerate_observable(canonical_evaluator, "SYNTHETIC-P5-DISAMBIGUATOR")
    return {
        "self_test_status": "PASS" if not result["has_class_8_7_flag"] else "FAIL",
        "expected_flag": False,
        "actual_flag": result["has_class_8_7_flag"],
        "p5_matches_count": len(result["p5_matches"]),
        "diagnostic": result["diagnostic"],
    }


if __name__ == "__main__":
    print("PRU Class 8.7 self-test:")
    pos = run_self_test()
    print(f"  Positive (S89 §W1-1):           {pos}")
    neg = run_negative_self_test()
    print(f"  Negative (synthetic):           {neg}")
    p5_pos = run_p5_op_proj_positive_self_test()
    print(f"  P5 positive (OP-PROJ no-witness): {p5_pos}")
    p5_neg_w = run_p5_op_proj_negative_witness_self_test()
    print(f"  P5 negative (OP-PROJ w/witness):  {p5_neg_w}")
    p5_disambig = run_p5_canonical_evaluator_disambiguator_self_test()
    print(f"  P5 disambiguator (canonical eval): {p5_disambig}")
    overall = (
        "PASS"
        if all(
            t["self_test_status"] == "PASS"
            for t in (pos, neg, p5_pos, p5_neg_w, p5_disambig)
        )
        else "FAIL"
    )
    print(f"  Overall: {overall}")
