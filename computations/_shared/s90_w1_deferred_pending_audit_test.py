#!/usr/bin/env python3
"""S90 W1-14 — Self-test driver for `detect_deferred_pending_sub_class()`.

Per `sessions/session-plan/session-90-plan-w1.md` §W1-14 #6 output files:
    `computations/_shared/s90_w1_deferred_pending_audit_test.py`
    (self-test against §VII.AV + §VII.AU as positive instances after CF-63
    W6 lands them).

Since §VII.AV / §VII.AU registry entries are CF-63 W6 carry-forwards (NOT
yet landed at S90 W1-14 close), this self-test uses synthetic-stub
fixtures emulating the post-CF-63 entry-text shape with the sub-class
tags present. T1-T3 are positive tests (one tag / other tag / both);
T4 is negative test (no tag, e.g., the existing W-5 §VII.AF.1 baseline).

All 4 tests MUST pass for W1-14 to land PASS. Each test asserts:
  - deferred_pending boolean
  - sub_class string ("PROXY-REFINEMENT" / "FIRST-EXTRACTION" / "BOTH" / "NONE")
  - severity string ("S2" advisory / "NONE")
  - proxy_refinement_matches + first_extraction_matches integer counts
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline
from _cross_pillar_bridge_audit import detect_deferred_pending_sub_class


# --- Synthetic fixtures (emulate post-CF-63 W6 §VII.AV / §VII.AU entry-text shape) ---

FIXTURE_PROXY_ONLY = """
### §VII.AV.OP-PROJ — FWD-C2 Pillar III/IV ↔ Pillar V cross-pillar bridge candidate

**Substrate-IS observable** (Pillar III BdG / Pillar IV BZ-trace):
`Tr_{M_2(C)}(P_BdG)` on `A_BdG` sub-algebra at substrate-distance-2 pole s=4.

**Laboratory-IN observable**: `∫_BZ d^d k Tr(P_BdG) · ρ_BZ(k; τ_fold)`.

**Bridge map**: HKR-image `L_max → ∞` per `cross-pillar-bridge-corpus.md §1`
Level-2-binding sub-class.

**Algebraic envelope**: `L^{-α}` Casimir-bound proxy at substrate-distance-2 pole.

**Empirical anchor**: pending FULL BdG re-derivation per S61/S78 Pauli-Villars
pipeline.

**Level-2 sub-class tag**: `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`
(deferred-pending PROXY-REFINEMENT per S90 W1-14 landing; awaits FULL BdG
pipeline replacement of Casimir-bound proxy).
"""

FIXTURE_FIRST_EXTRACTION_ONLY = """
### §VII.AU.OP-PROJ — FWD-C1 Pillar I-II cross-pillar bridge candidate

**Substrate-IS observable** (Pillar I spectral-action / Pillar II Mellin):
`Tr(P_n-s-substrate-distance-1)` at substrate-distance-1 pole s=3.

**Laboratory-IN observable**: `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) ·
ρ_BZ(k; τ_fold)` (W7c emission #3 lexical per S90 W1-13 §2 corpus row #3).

**Bridge map**: HKR-image `L_max → ∞` Level-2-binding.

**Algebraic envelope**: `L^{-α}` parameterized slope_A canonical pending
L_max scan.

**Empirical anchor**: pending L_max scan + Friedrich-Bär saturation theorem
per S87 W11-2 + W11-3 precedents.

**Level-2 sub-class tag**: `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`
(deferred-pending FIRST-EXTRACTION per S90 W1-14 landing; awaits L_max
scan + analytic limit derivation).
"""

FIXTURE_BOTH = """
### §VII.XX.OP-PROJ — Hypothetical dual-class bridge (BOTH sub-class tags)

This is a hypothetical fixture testing the BOTH branch of the
`detect_deferred_pending_sub_class()` decision procedure. Real registry
entries would have ONE sub-class; the BOTH case is admitted by the
detector to cover edge-case overlap (e.g., a multi-axis bridge whose
axis-A is PROXY-pending and axis-B is FIRST-EXTRACTION-pending).

**Axis A**: `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`.
**Axis B**: `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`.
"""

FIXTURE_NEGATIVE_BASELINE = """
### §VII.AF.1.OP-PROJ — W-5 calibration baseline (no deferred-pending tags)

**Substrate-IS observable**: finite-L Hochschild pairing
`R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` on `(A_K^≤10, H_K^≤10,
D_K^≤10)`.

**Laboratory-IN observable**: `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k;
τ_fold) d^d k`.

**Bridge map**: `L_max → ∞` HKR image.

**Algebraic envelope**: `L^{-3}` envelope at d=4 (Level-2-binding; HKR-
image bridge).

**Empirical anchor**: 0.0095% F_4 strict at L_max=10.

**Level-2 sub-class declaration**: Level-2-binding (NOT deferred-pending;
this is the calibration baseline for the positive Level-2-binding sub-class).
"""


# --- S91 W0 R11 extensions: T5 false-positive + T6 false-negative fixtures ---
#
# Per S91 context file §"REMAINING substantive items" R11 spec (T2.18 carry-
# forward closure; per `feedback_no-asking-just-execute.md`, 2026-05-16):
# extend the self-test suite with two boundary-case fixtures that probe the
# detector's behavior on edge-case mentions of the sub-class tag.
#
# T5 (FALSE-POSITIVE Cross-references citation): the sub-class tag appears
#     ONLY in a Cross-references block citing OTHER entries' deferred-pending
#     state, NOT as a substantive declaration on THIS entry. The current
#     regex-based detector cannot distinguish substantive declarations from
#     citation mentions and WILL fire; T5 documents this as a known
#     limitation. Future detector iterations may add Cross-references-block
#     context awareness; T5 is the regression-test target for that work.
#
# T6 (FALSE-NEGATIVE historical reference): the sub-class tag appears in a
#     historical reference (e.g., "the §VII.AV PROXY-REFINEMENT instance
#     landed at S90 W1-14...") mentioning a past instance. The current
#     detector cannot distinguish historical mentions from current-entry
#     declarations and WILL fire; T6 documents this similarly.
#
# Both T5 and T6 are SUGGESTION-tagged: their CURRENT verdict under the
# regex-only detector is `deferred_pending=True` (positive). Once the
# detector adds context-awareness (e.g., scope-restricted to Status /
# Anatomy / Sub-class declaration sections, excluding Cross-references
# and historical-reference blocks), these fixtures will return
# `deferred_pending=False` as the EXPECTED behavior. The tests assert the
# CURRENT behavior + flag the limitation as forward-improvement target.

FIXTURE_CROSS_REF_CITATION_ONLY = """
### §VII.YY.OP-PROJ — Hypothetical entry citing OTHER entries' sub-classes

**Substrate-IS observable**: finite-L Hochschild pairing on
`(A_K^≤10, H_K^≤10, D_K^≤10)` — fully landed; NO deferred-pending status
on THIS entry.

**Laboratory-IN observable**: standard BZ-trace.

**Bridge map**: HKR `L_max → ∞`.

**Algebraic envelope**: `L^{-3}` Level-2-binding (fully landed).

**Empirical anchor**: 0.0050% strict at L_max=10 (PASS).

**Level-2 sub-class declaration**: Level-2-binding (FULLY LANDED — NOT
deferred-pending).

**Cross-references**:
- `sessions/permanent-results-registry.md §VII.AV.OP-PROJ` —
  REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT (FWD-C2 instance; this
  CITATION is a CROSS-REFERENCE to a different entry's sub-class state,
  NOT a declaration that THIS §VII.YY entry is deferred-pending).
- `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` —
  REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (FWD-C1 instance; same
  citation-context discipline applies).
"""


FIXTURE_HISTORICAL_REFERENCE_ONLY = """
### §VII.ZZ.OP-PROJ — Entry with HISTORICAL reference to past sub-class instances

**Substrate-IS observable**: NEW substrate observable; no deferred-pending
status at landing.

**Laboratory-IN observable**: standard BZ-trace projection.

**Bridge map**: HKR `L_max → ∞`.

**Algebraic envelope**: `L^{-3}` Level-2-binding (fully landed at S91+).

**Empirical anchor**: 0.0048% strict at L_max=10 (PASS).

**Level-2 sub-class declaration**: Level-2-binding (FULLY LANDED; this
entry is NOT in deferred-pending state).

**Substrate framing**: the prior K=2 calibration corpus instances for
the REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class (§VII.AV at
S90 W1-14 + §VII.AX at S91 W0 R5) demonstrated the structural pattern;
this entry §VII.ZZ does NOT inherit deferred-pending state. The
historical-reference mention of "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION
at §VII.AU.OP-PROJ" earlier in the framework's K-counter calibration
corpus is purely descriptive context; this §VII.ZZ entry is NOT in
that sub-class state.
"""


# --- Test cases ---

def run_T1_proxy_only():
    """T1 positive: PROXY-REFINEMENT tag only → sub_class=PROXY-REFINEMENT."""
    result = detect_deferred_pending_sub_class(
        FIXTURE_PROXY_ONLY,
        section_anchor="§VII.AV.OP-PROJ",
    )
    assert result["deferred_pending"] is True, \
        f"T1 PROXY-ONLY: expected deferred_pending=True, got {result['deferred_pending']}"
    assert result["sub_class"] == "PROXY-REFINEMENT", \
        f"T1 PROXY-ONLY: expected sub_class='PROXY-REFINEMENT', got '{result['sub_class']}'"
    assert result["severity"] == "S2", \
        f"T1 PROXY-ONLY: expected severity='S2', got '{result['severity']}'"
    assert result["proxy_refinement_matches"] == 1, \
        f"T1 PROXY-ONLY: expected proxy_refinement_matches=1, got {result['proxy_refinement_matches']}"
    assert result["first_extraction_matches"] == 0, \
        f"T1 PROXY-ONLY: expected first_extraction_matches=0, got {result['first_extraction_matches']}"
    print(f"T1 PROXY-REFINEMENT only: PASS — {result['diagnostic']}")
    return result


def run_T2_first_extraction_only():
    """T2 positive: FIRST-EXTRACTION tag only → sub_class=FIRST-EXTRACTION."""
    result = detect_deferred_pending_sub_class(
        FIXTURE_FIRST_EXTRACTION_ONLY,
        section_anchor="§VII.AU.OP-PROJ",
    )
    assert result["deferred_pending"] is True
    assert result["sub_class"] == "FIRST-EXTRACTION", \
        f"T2 FIRST-EXTRACTION-ONLY: expected sub_class='FIRST-EXTRACTION', got '{result['sub_class']}'"
    assert result["severity"] == "S2"
    assert result["proxy_refinement_matches"] == 0
    assert result["first_extraction_matches"] == 1
    print(f"T2 FIRST-EXTRACTION only: PASS — {result['diagnostic']}")
    return result


def run_T3_both():
    """T3 positive: BOTH tags → sub_class=BOTH."""
    result = detect_deferred_pending_sub_class(
        FIXTURE_BOTH,
        section_anchor="§VII.XX.OP-PROJ",
    )
    assert result["deferred_pending"] is True
    assert result["sub_class"] == "BOTH", \
        f"T3 BOTH: expected sub_class='BOTH', got '{result['sub_class']}'"
    assert result["severity"] == "S2"
    assert result["proxy_refinement_matches"] == 1
    assert result["first_extraction_matches"] == 1
    print(f"T3 BOTH: PASS — {result['diagnostic']}")
    return result


def run_T4_negative_baseline():
    """T4 negative: W-5 §VII.AF.1 baseline (no deferred-pending tags) → sub_class=NONE."""
    result = detect_deferred_pending_sub_class(
        FIXTURE_NEGATIVE_BASELINE,
        section_anchor="§VII.AF.1.OP-PROJ",
    )
    assert result["deferred_pending"] is False, \
        f"T4 NEGATIVE: expected deferred_pending=False, got {result['deferred_pending']}"
    assert result["sub_class"] == "NONE"
    assert result["severity"] == "NONE"
    assert result["proxy_refinement_matches"] == 0
    assert result["first_extraction_matches"] == 0
    print(f"T4 negative baseline: PASS — {result['diagnostic']}")
    return result


def run_T5_cross_ref_citation_false_positive():
    """T5 boundary: Cross-references citation ONLY (no substantive declaration).

    The §VII.YY fixture's `Level-2 sub-class declaration` is "Level-2-binding
    FULLY LANDED" (NOT deferred-pending). The sub-class tags appear ONLY in
    the **Cross-references** block citing OTHER entries' deferred-pending
    state (§VII.AV + §VII.AU).

    EXPECTED behavior under the current regex-only detector: FIRES (false-
    positive), since the detector cannot distinguish Cross-references
    citations from substantive declarations. T5 documents this as a known
    limitation; future detector iterations should add Cross-references-block
    context awareness so this fixture returns `deferred_pending=False`.

    Current assertion: detector returns `deferred_pending=True` with
    `sub_class='BOTH'` (both PROXY-REFINEMENT and FIRST-EXTRACTION tags
    present in Cross-references block).
    """
    result = detect_deferred_pending_sub_class(
        FIXTURE_CROSS_REF_CITATION_ONLY,
        section_anchor="§VII.YY.OP-PROJ",
    )
    # Current detector behavior: fires on Cross-references citation
    # (regex-only; no context-awareness). Forward improvement: add
    # Cross-references-block exclusion → expected `deferred_pending=False`.
    assert result["deferred_pending"] is True, (
        f"T5 cross-ref citation: current detector EXPECTS deferred_pending=True "
        f"(known false-positive limitation); got {result['deferred_pending']}"
    )
    assert result["sub_class"] == "BOTH", (
        f"T5 cross-ref citation: expected sub_class='BOTH' (both tags in "
        f"Cross-references block), got '{result['sub_class']}'"
    )
    assert result["severity"] == "S2", (
        f"T5 cross-ref citation: expected severity='S2' advisory, got '{result['severity']}'"
    )
    print(f"T5 Cross-references false-positive (boundary case; current regex-only detector): PASS — {result['diagnostic']}")
    print(f"    LIMITATION FLAG: current detector cannot distinguish Cross-references")
    print(f"    citations from substantive declarations. Forward improvement target:")
    print(f"    add Cross-references-block exclusion → expected deferred_pending=False.")
    return result


def run_T6_historical_reference_false_negative():
    """T6 boundary: historical reference to past instances (NOT current state).

    The §VII.ZZ fixture's `Level-2 sub-class declaration` is "Level-2-binding
    FULLY LANDED" (NOT deferred-pending). The sub-class tag appears in the
    **Substrate framing** historical-reference paragraph describing the prior
    K=2 calibration corpus instances.

    EXPECTED behavior under the current regex-only detector: FIRES (false-
    positive on historical reference), since the detector cannot distinguish
    historical mentions from current-entry declarations. T6 documents this
    as a known limitation; future detector iterations should add
    historical-reference exclusion so this fixture returns
    `deferred_pending=False`.

    Current assertion: detector returns `deferred_pending=True` with
    `sub_class='FIRST-EXTRACTION'` (the historical reference cites the
    §VII.AU.OP-PROJ FIRST-EXTRACTION instance).
    """
    result = detect_deferred_pending_sub_class(
        FIXTURE_HISTORICAL_REFERENCE_ONLY,
        section_anchor="§VII.ZZ.OP-PROJ",
    )
    # Current detector behavior: fires on historical-reference mention
    # (regex-only; no context-awareness). Forward improvement: add
    # historical-reference exclusion → expected `deferred_pending=False`.
    assert result["deferred_pending"] is True, (
        f"T6 historical reference: current detector EXPECTS deferred_pending=True "
        f"(known false-positive limitation); got {result['deferred_pending']}"
    )
    # The §VII.ZZ fixture has FIRST-EXTRACTION in the historical-reference
    # paragraph + PROXY-REFINEMENT in the substrate-framing K=2 corpus
    # citation. Both tags fire → sub_class='BOTH'.
    assert result["sub_class"] in ("FIRST-EXTRACTION", "BOTH"), (
        f"T6 historical reference: expected sub_class in {{FIRST-EXTRACTION, BOTH}}, "
        f"got '{result['sub_class']}'"
    )
    assert result["severity"] == "S2"
    print(f"T6 historical reference false-positive (boundary case; current regex-only detector): PASS — {result['diagnostic']}")
    print(f"    LIMITATION FLAG: current detector cannot distinguish historical")
    print(f"    references from current-entry declarations. Forward improvement target:")
    print(f"    add historical-reference exclusion → expected deferred_pending=False.")
    return result


def main() -> int:
    """Run all 6 self-tests (T1-T6) and return exit 0 on success, 1 on assert failure.

    T1-T4: positive + negative baseline tests (original S90 W1-14 set).
    T5-T6: boundary-case fixtures (S91 W0 R11 extension per
           `feedback_no-asking-just-execute.md`):
      - T5: false-positive Cross-references citation (LIMITATION FLAG)
      - T6: false-positive historical reference (LIMITATION FLAG)
    """
    results = {                                                       # (local)
        "T1_proxy_only": run_T1_proxy_only(),
        "T2_first_extraction_only": run_T2_first_extraction_only(),
        "T3_both": run_T3_both(),
        "T4_negative_baseline": run_T4_negative_baseline(),
        "T5_cross_ref_citation": run_T5_cross_ref_citation_false_positive(),
        "T6_historical_reference": run_T6_historical_reference_false_negative(),
    }
    summary = {                                                       # (local)
        "all_tests_pass": True,
        "n_tests": 6,
        "current_detector_limitations": [
            "T5: regex-only detector cannot distinguish Cross-references citations "
            "from substantive declarations (false-positive on cross-citing entries)",
            "T6: regex-only detector cannot distinguish historical references from "
            "current-entry declarations (false-positive on historical mentions)",
        ],
        "forward_improvement_target": (
            "Add context-awareness to detect_deferred_pending_sub_class(): "
            "exclude matches inside **Cross-references** blocks and historical-"
            "reference paragraphs. Re-test T5 + T6 should then return "
            "deferred_pending=False for both fixtures."
        ),
        "results": {k: {
            "deferred_pending": v["deferred_pending"],
            "sub_class": v["sub_class"],
            "severity": v["severity"],
        } for k, v in results.items()},
    }
    print("\n" + json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
