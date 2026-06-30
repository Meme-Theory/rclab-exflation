"""
_cross_pillar_bridge_audit.py

Bridge-theorem registry-entry structural-completeness audit
(T4-8, S86 W-5 AUDIT-1).

# NEEDS-ORCHESTRATOR-FOLLOWUP: NEEDS-DECISION readiness — orchestrator
# must decide whether to build in S87 once first bridge-entry lands
# (§VII.W cross-pillar bridge theorem) OR defer until 2nd bridge
# candidate appears. Audit logic is FULL HERE; activation only
# becomes load-bearing once a §VII.W entry is appended to
# `sessions/permanent-results-registry.md`.

Purpose
-------
Scans `sessions/permanent-results-registry.md` for §VII.W (and any
future cross-pillar bridge slots) and verifies that bridge-theorem
entries declare:

  Three-level structural-confidence ladder anatomy (S86 W-5 §EMERGENCE R3-α):
    Level 1: substrate-IS structural identity (cohomology-class level,
             regulator-invariant, L-independent) — STRUCTURAL THEOREM
    Level 2: algebraic convergence envelope (L_max-dependent rate to
             continuum / laboratory image) — STRUCTURAL PREDICTION
    Level 3: empirical anchor (numerical satisfaction at canonical L_max)

  Five IS-not-IN anatomy elements (S86 W-5 §EMERGENCE R3-β):
    1. Substrate-IS observable (finite-L spectral-triple observable)
    2. Laboratory-IN observable (continuum sweep observable)
    3. Bridge map (HKR / K-theory boundary / Connes-Karoubi pairing)
    4. Algebraic envelope (convergence rate L^{-α} bound)
    5. Empirical anchor (numerical satisfaction at canonical L_max)

A bridge-theorem entry PASSes the audit iff all 3 tier markers AND
all 5 anatomy elements appear in the entry text within the
§-anchor block.

Source
------
S86 W-5 §AUDIT-1 (lines 70-74).
S86 W-5 §EMERGENCE R3-α (workshop L2444-2473) — three-level ladder.
S86 W-5 §EMERGENCE R3-β (workshop L2477-2522) — IS-not-IN anatomy.
S86 W-5 RULE-1 + RULE-2 (proposed bridge-anatomy rules).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-8.
Promoted from S86 W-5 AUDIT-1 (volovik + connes, 2026-04-26).

Status
------
SCAFFOLD with ACTIVE LOGIC. The §VII.W slot does not yet exist in
`permanent-results-registry.md`; the audit returns INFO_NO_BRIDGE
until the first bridge entry lands.

Usage
-----
    python _cross_pillar_bridge_audit.py
    python _cross_pillar_bridge_audit.py --json
    python _cross_pillar_bridge_audit.py --strict     # FAIL → nonzero exit
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned audit parameters
# ---------------------------------------------------------------------------

REGISTRY_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "sessions" / "permanent-results-registry.md"
)   # S93 W1-close fix: parent.parent (=computations/) → parent.parent.parent (=project root); the prior path resolved to the nonexistent computations/sessions/... and run_audit() always returned INFO_NO_REGISTRY.

# Bridge-theorem §-anchor pattern (§VII.W, §VII.X, ..., §VII.AA, ..., §VII.AZ,
# §VII.BA, §VII.BB, ..., two-letter codes through §VII.ZZ).
# Slot-allocation note: §VII.W was reserved for Slot 1a-S7 Parity-Grading
# Orthogonality Theorem; W-5 REGISTRY-1 rerouted to §VII.AF (next free letter
# after AE). Next-free-letter rerouting since S91 has populated §VII.BA-§VII.BE
# (Wodzicki-BCS, HH^1-cocycle, Wedderburn-image, Pillar-2-cancellation, FWD-C4
# Pati-Salam); the two-letter range MUST extend past AZ. S93 W1-2 fix: the
# single-letter-second-char form `A[A-Z]` capped at AZ and was BLIND to the
# §VII.B* slots (the §VII.BA Wodzicki-BCS bridge entry, landed S91 W9-9, was
# never audited). Widened to `[A-Z][A-Z]` so all two-letter codes AA-ZZ match.
BRIDGE_SECTION_REGEX = re.compile(
    r"^#+\s*§VII\.([WXYZ]|[A-Z][A-Z])\b.*$", re.IGNORECASE | re.MULTILINE
)

# Three-level ladder markers (case-insensitive substring search).
TIER_MARKERS = {                                          # (local)
    "Level 1": (
        "tier 1",
        "substrate-is structural identity",
        "structural theorem",
    ),
    "Level 2": (
        "tier 2",
        "algebraic convergence envelope",
        "structural prediction",
    ),
    "Level 3": (
        "tier 3",
        "empirical anchor",
    ),
}

# Five IS-not-IN anatomy elements.
ANATOMY_ELEMENTS = {                                       # (local)
    "1_substrate_IS_observable": (
        "substrate-is observable",
        "finite-l spectral-triple observable",
        "(a^{<=l}, h^{<=l}, d^{<=l})",
    ),
    "2_laboratory_IN_observable": (
        "laboratory-in observable",
        "continuum measurement",
        "sweep observable",
    ),
    "3_bridge_map": (
        "bridge map",
        "hkr",
        "k-theory boundary",
        "connes-karoubi pairing",
    ),
    "4_algebraic_envelope": (
        "algebraic envelope",
        "convergence rate l^{-",
        "l^{-3}",
        "l_envelope_d4",
    ),
    "5_empirical_anchor": (
        "empirical anchor",
        "numerical satisfaction",
        "canonical l_max",
        "l_max=10",
    ),
}


# ---------------------------------------------------------------------------
# Element 2 OE-form discipline (S88 W7a-73 hardening)
# ---------------------------------------------------------------------------
#
# Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Element 2 OE-form
# discipline"`, Element 2 (laboratory-IN observable) MUST be specified in
# operator-expression form (integration domain + trace + named projector).
# Prose-only forms admit container-thinking reinterpretation and are
# STRUCTURALLY INSUFFICIENT.

ELEMENT_2_OE_POSITIVE_REGEX = re.compile(                  # (local)
    # Integration domain (\int / ∫ / \sum / ∑) followed by "d" then "Tr"
    # then a named projector "P_<index>" or "Π^<superscript>_<subscript>".
    # The Π is admitted as P-equivalent. DOTALL allows multi-line span.
    r"(?:\\int|∫|\\sum|∑).*?(?:d.*?)?Tr.*?\([ΠP][_^].*?\)",
    re.DOTALL,
)                                                          # (local)

ELEMENT_2_OE_NEGATIVE_REGEX = re.compile(                  # (local)
    # Prose-form Element 2 specifications ending in "measurement" /
    # "spectroscopy" / "test" without an OE-form operator. Matches:
    # "Element 2 (...): <prose> measurement." / "...spectroscopy." /
    # "...test." sentence terminators.
    r"Element\s*2[^:]*:\s*[^.\n]*?(?:measurement|spectroscopy|test)\.",
    re.IGNORECASE,
)                                                          # (local)


def audit_element_2_oe_form(section_text: str) -> dict:
    """Audit Element 2 OE-form discipline on a bridge-theorem section.

    Returns a dict with:
      - oe_positive_match: bool — at least one positive-match present
      - oe_negative_match: bool — any negative-match (forbidden) present
      - oe_form_pass: bool — positive AND not negative
      - matched_positive_snippets: up to 3 example matches
      - matched_negative_snippets: all negative matches (forbidden, must be 0)
    """
    pos_matches = ELEMENT_2_OE_POSITIVE_REGEX.findall(section_text)  # (local)
    neg_matches = ELEMENT_2_OE_NEGATIVE_REGEX.findall(section_text)  # (local)

    oe_positive_match = len(pos_matches) > 0                # (local)
    oe_negative_match = len(neg_matches) > 0                # (local)
    oe_form_pass = oe_positive_match and not oe_negative_match  # (local)

    return {
        "oe_positive_match": oe_positive_match,
        "oe_negative_match": oe_negative_match,
        "oe_form_pass": oe_form_pass,
        "n_positive_matches": len(pos_matches),
        "n_negative_matches": len(neg_matches),
        "matched_positive_snippets": pos_matches[:3],
        "matched_negative_snippets": neg_matches,
    }


# ---------------------------------------------------------------------------
# Deferred-pending intermediate verdict-class detectors (S90 W1-14 landing)
# ---------------------------------------------------------------------------
#
# Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class
# (binding vs non-binding)" §"Deferred-pending intermediate verdict-class
# (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"`.
#
# Between Level-2-binding ELIGIBLE and Level-2-non-binding INELIGIBLE, the
# deferred-pending intermediate verdict-class admits TWO sub-class tags for
# registry entries whose Level-2 envelope structural form is pre-registered
# on the binding axis but whose empirical realization is partial (SCHEMATIC
# proxy / symbolic-only / first-extraction-pending).
#
# Status: SUGGESTION at K=1 (dual calibration instances §VII.AV + §VII.AU
# share the W1-14 landing event); promotes to MANDATORY at K=3 per
# `feedback_rules-compensate-missing-structure.md`. Severity at detection
# is S2 advisory; the detectors do NOT route to plan-freeze HARD-HALT.

PATTERN_PROXY_REFINEMENT = re.compile(                      # (local)
    r"REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT",
)                                                            # (local)

PATTERN_FIRST_EXTRACTION = re.compile(                       # (local)
    r"REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION",
)                                                            # (local)


def detect_deferred_pending_sub_class(
    section_text: str,
    section_anchor: str = "",
) -> dict:
    """Detect deferred-pending sub-class tags in a §VII registry entry.

    Per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs
    non-binding)" §"Deferred-pending intermediate verdict-class"` (S90 W1-14
    landing, advisory until K=3).

    Returns a structured diagnostic dict:
      - deferred_pending: bool — True iff either sub-class tag is present.
      - sub_class: str — "PROXY-REFINEMENT" / "FIRST-EXTRACTION" / "BOTH" / "NONE".
      - severity: str — "S2" advisory if deferred_pending else "NONE".
      - proxy_refinement_matches: int — count of PROXY-REFINEMENT tag matches.
      - first_extraction_matches: int — count of FIRST-EXTRACTION tag matches.
      - section_anchor: str — anchor label (§VII.AV / §VII.AU / ...).
      - diagnostic: str — human-readable diagnostic.

    Does NOT route to plan-freeze HARD-HALT (S1); detection produces S2
    advisory only. The deferred-pending class RESERVES the §VII slot during
    the pending refinement / extraction window without contributing to
    registry-PASS by itself.
    """
    n_proxy = len(PATTERN_PROXY_REFINEMENT.findall(section_text))        # (local)
    n_first = len(PATTERN_FIRST_EXTRACTION.findall(section_text))        # (local)

    if n_proxy and n_first:
        sub_class = "BOTH"                                                # (local)
    elif n_proxy:
        sub_class = "PROXY-REFINEMENT"                                    # (local)
    elif n_first:
        sub_class = "FIRST-EXTRACTION"                                    # (local)
    else:
        sub_class = "NONE"                                                # (local)

    deferred_pending = (n_proxy > 0) or (n_first > 0)                     # (local)
    severity = "S2" if deferred_pending else "NONE"                       # (local)

    if deferred_pending:
        diagnostic = (                                                    # (local)
            f"deferred_pending_sub_class_detected; sub_class={sub_class}; "
            f"severity=S2_advisory_NOT_hard_halt; "
            f"n_proxy_matches={n_proxy}; n_first_extraction_matches={n_first}; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    else:
        diagnostic = (                                                    # (local)
            f"no_deferred_pending_sub_class_tag_detected; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )

    return {
        "deferred_pending": deferred_pending,
        "sub_class": sub_class,
        "severity": severity,
        "proxy_refinement_matches": n_proxy,
        "first_extraction_matches": n_first,
        "section_anchor": section_anchor,
        "diagnostic": diagnostic,
    }


# ---------------------------------------------------------------------------
# Composite Bridge-Map Dimensional-Class Admissibility taxonomy detector
# (S92 §VII.BA connes×mack; cross-pillar-bridge-anatomy.md §"Composite
#  Bridge-Map Dimensional-Class Admissibility"; corpus §18).
#
# Single-function-scope extension (mirrors detect_deferred_pending_sub_class):
# a module-level regex set + one standalone detector branch. Does NOT touch
# find_bridge_sections / audit_section / run_audit / main.
#
# Flags a §VII registry entry that cites a FORBIDDEN-cell composite witness
# (T1 ratio×sum / T2 degree-matched scalar / T4|_{s=s'} equal-pole ratio)
# WITHOUT the corresponding ADMISSIBLE-cell re-route citation (T3 / T4 at
# s≠s' / T5 direct Connes-Karoubi K_0-pairing). The two-axis admissibility
# criterion (deg-match ∧ non-scalar-L_max-dependent) is irreducible; a
# composite entry citing only a forbidden witness is registry-incomplete on
# the re-route axis.
#
# Status: SUGGESTION at K=1 (single §VII.BA instance + S91 W9-8 calibration
# corpus). Severity at detection is S2 advisory; the detector does NOT route
# to plan-freeze HARD-HALT (matches the deferred-pending detector convention
# at K=1 SUGGESTION). Promotes to MANDATORY at K=3 per
# `feedback_rules-compensate-missing-structure.md`.
# ---------------------------------------------------------------------------

# FORBIDDEN-cell witness patterns (T1 / T2 / T4|_{s=s'}).
PATTERN_COMPOSITE_T1_RATIO_TIMES_SUM = re.compile(             # (local)
    r"ratio[×x*\s-]*sum|\(SUM\)\s*[×x*]\s*\(RATIO\)|Res_W\([^)]*\)\s*[·*×]\s*ρ_FULL",
    re.IGNORECASE,
)                                                              # (local)
PATTERN_COMPOSITE_T2_SCALAR_CORRECTOR = re.compile(            # (local)
    r"degree-matched\s+scalar|scalar\s+corrector|N\s*[·*]\s*Res_W|no\s+scalar\s+of\s+any\s+degree",
    re.IGNORECASE,
)                                                              # (local)
PATTERN_COMPOSITE_T4_EQUAL_POLE = re.compile(                  # (local)
    r"T4\s*\|?_?\{?s\s*=\s*s'?\}?|equal-pole\s+(?:ratio|cancellation)|Res_W\(s\)\s*/\s*Res_W\(s\)",
    re.IGNORECASE,
)                                                              # (local)
# ADMISSIBLE-cell re-route citation (T3 / T4|_{s != s'} / T5).
PATTERN_COMPOSITE_ADMISSIBLE_REROUTE = re.compile(             # (local)
    r"ratio-of-ratios|sum-over-sums|T4\s*\|?_?\{?s\s*≠\s*s'?\}?|s\s*!=\s*s'|"
    r"Connes-Karoubi\s+K_?0|K_?0-pairing|degree-matched\s+NON-SCALAR|T[35]\b",
    re.IGNORECASE,
)                                                              # (local)


def detect_composite_bridge_map_taxonomy(
    section_text: str,
    section_anchor: str = "",
) -> dict:
    """Detect composite bridge-map dimensional-class taxonomy compliance.

    Per `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-
    Class Admissibility"` (S92 §VII.BA connes x mack; corpus §18). A composite
    Element-3 bridge map is admissible iff the two-axis conjunction holds:
    deg(B)=d_A (homogeneity) AND B carries non-trivial L_max-dependence
    surviving the dimensionless ratio (substrate-natural-binding). The three
    forbidden-cell witnesses are T1 (ratio x sum, wrong degree), T2 (degree-
    matched scalar corrector), and T4|_{s=s'} (equal-pole ratio == 1).

    Returns a structured diagnostic dict:
      - has_forbidden_witness: bool -- True iff any T1/T2/T4|_{s=s'} tag present.
      - forbidden_witnesses: list[str] -- which witness cells matched.
      - has_admissible_reroute: bool -- True iff a T3/T4|_{s!=s'}/T5 re-route
        citation is present.
      - taxonomy_incomplete: bool -- True iff a forbidden witness is cited
        WITHOUT an admissible re-route (registry-incomplete on the re-route axis).
      - severity: str -- "S2" advisory if taxonomy_incomplete else "NONE".
      - section_anchor: str
      - diagnostic: str

    Does NOT route to plan-freeze HARD-HALT (S1); detection produces S2
    advisory only at K=1 SUGGESTION status.
    """
    witnesses = []                                                       # (local)
    if PATTERN_COMPOSITE_T1_RATIO_TIMES_SUM.search(section_text):
        witnesses.append("T1_RATIO_TIMES_SUM")                           # (local)
    if PATTERN_COMPOSITE_T2_SCALAR_CORRECTOR.search(section_text):
        witnesses.append("T2_DEGREE_MATCHED_SCALAR")                     # (local)
    if PATTERN_COMPOSITE_T4_EQUAL_POLE.search(section_text):
        witnesses.append("T4_EQUAL_POLE")                                # (local)

    has_forbidden = len(witnesses) > 0                                   # (local)
    has_reroute = bool(PATTERN_COMPOSITE_ADMISSIBLE_REROUTE.search(section_text))  # (local)
    taxonomy_incomplete = has_forbidden and not has_reroute              # (local)
    severity = "S2" if taxonomy_incomplete else "NONE"                   # (local)

    if taxonomy_incomplete:
        diagnostic = (                                                   # (local)
            f"composite_forbidden_witness_without_reroute; "
            f"witnesses={witnesses}; "
            f"severity=S2_advisory_NOT_hard_halt; "
            f"missing=ADMISSIBLE_REROUTE_T3_T4_s_neq_s_prime_or_T5; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    elif has_forbidden and has_reroute:
        diagnostic = (                                                   # (local)
            f"composite_forbidden_witness_with_reroute_present; "
            f"witnesses={witnesses}; reroute_cited=True; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    else:
        diagnostic = (                                                   # (local)
            f"no_composite_forbidden_witness_detected; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )

    return {
        "has_forbidden_witness": has_forbidden,
        "forbidden_witnesses": witnesses,
        "has_admissible_reroute": has_reroute,
        "taxonomy_incomplete": taxonomy_incomplete,
        "severity": severity,
        "section_anchor": section_anchor,
        "diagnostic": diagnostic,
    }


# ---------------------------------------------------------------------------
# Class-(g): Weighting-Functional-Family canonical detector (S92 §VII.AU CF-37)
# ---------------------------------------------------------------------------
#
# Per `substrate-first-canonical-sourcing.md §(ii.A)` refinement + corpus §19
# (S92 §VII.AU CF-37 (c)∘(d) volovik x vdd; CONVERGED 2026-05-23). When a
# substrate-distance pole admits >=3 distinct scalar F-images at the SAME
# nominal (algebra, pole, corridor) triple, the §(ii.A) atlas-row/cache-moment
# BINARY is INSUFFICIENT; the correct refinement is a WEIGHTING-FUNCTIONAL
# FAMILY fibered over a finite K_0 class (the topological shadow of the
# canonical Fredholm module). The topological STOPPING rule (every weighting
# factors through the same finite class) makes the K-counter a BASE-count, not
# a fiber-count. A §VII entry that mis-frames the multiple F-images as an
# "N-layer K-counter" (fiber-count) WITHOUT the family-reaxis + stopping-rule
# citation is registry-incomplete on the canonical-identification axis.
#
# Status: SUGGESTION at K=1 (single §VII.AU CF-37 instance; corpus §19).
# Severity at detection is S2 advisory; the detector does NOT route to
# plan-freeze HARD-HALT (matches the composite-bridge / deferred-pending
# detector convention at K=1 SUGGESTION). Promotes to MANDATORY at K=3 per
# `feedback_rules-compensate-missing-structure.md` (advancement requires a
# structurally-distinct triple per the Hybrid Independence Test clause iv).
# ---------------------------------------------------------------------------

# FORBIDDEN mis-framing: "N-layer K-counter" / "N-bin counter" fiber-count
# language applied to multiple F-images at one triple.
PATTERN_WFF_FIBER_COUNT_MISFRAME = re.compile(                 # (local)
    r"\d+\s*-?\s*layer\s+(?:CF-?\d*\s*)?(?:axis\s+)?K-counter|"
    r"\d+\s*-?\s*bin\s+(?:K-?)?counter|"
    r"third\s+(?:discrete\s+)?layer-type|count(?:ing)?\s+weightings\b",
    re.IGNORECASE,
)                                                              # (local)
# ADMISSIBLE re-axis + topological stopping-rule citation.
PATTERN_WFF_FAMILY_REAXIS = re.compile(                        # (local)
    r"weighting-functional\s+family|weighting\s+family|"
    r"re-?axis(?:\s+of)?\s+§?\(?ii\.A\)?|family\s+(?:re-?axis|fibered)|"
    r"Φ_w\b|Phi_w\b",
    re.IGNORECASE,
)                                                              # (local)
PATTERN_WFF_STOPPING_RULE = re.compile(                        # (local)
    r"topological\s+stopping\s+rule|"
    r"factors?\s+through\s+(?:the\s+)?same\s+(?:finite\s+)?(?:K_?0\s+)?class|"
    r"base-?count(?:\s+not\s+a\s+fiber-?count)?|"
    r"nothing\s+new\s+to\s+count\s+until\s+the\s+(?:base\s+)?class\s+changes",
    re.IGNORECASE,
)                                                              # (local)


def detect_weighting_functional_family(
    section_text: str,
    section_anchor: str = "",
) -> dict:
    """Detect weighting-functional-family canonical-identification compliance.

    Per `substrate-first-canonical-sourcing.md §(ii.A)` refinement + corpus
    §19 (S92 §VII.AU CF-37 volovik x vdd). A §VII entry citing >=3 distinct
    scalar F-images at one nominal (algebra, pole, corridor) triple is
    registry-complete on the canonical-identification axis iff it (i) re-axes
    the §(ii.A) atlas-row/cache-moment binary to a WEIGHTING-FUNCTIONAL FAMILY
    AND (ii) cites the topological STOPPING rule (every weighting factors
    through the same finite K_0 class; the K-counter is a base-count, not a
    fiber-count). An entry that mis-frames the multiple F-images as an
    "N-layer K-counter" (fiber-count) WITHOUT the family-reaxis + stopping-rule
    citation is registry-incomplete (the §VII.AU CF-37 WP-draft over-reach the
    workshop retracted).

    Returns a structured diagnostic dict:
      - has_fiber_count_misframe: bool -- True iff "N-layer/N-bin K-counter"
        fiber-count language present.
      - has_family_reaxis: bool -- True iff a weighting-functional-family
        re-axis citation is present.
      - has_stopping_rule: bool -- True iff the topological stopping-rule
        citation is present.
      - canonical_id_incomplete: bool -- True iff a fiber-count misframe is
        present WITHOUT the family-reaxis AND stopping-rule reframe.
      - severity: str -- "S2" advisory if canonical_id_incomplete else "NONE".
      - section_anchor: str
      - diagnostic: str

    Does NOT route to plan-freeze HARD-HALT (S1); detection produces S2
    advisory only at K=1 SUGGESTION status.
    """
    has_misframe = bool(PATTERN_WFF_FIBER_COUNT_MISFRAME.search(section_text))   # (local)
    has_reaxis = bool(PATTERN_WFF_FAMILY_REAXIS.search(section_text))            # (local)
    has_stopping = bool(PATTERN_WFF_STOPPING_RULE.search(section_text))          # (local)

    # The reframe is COMPLETE iff BOTH the family-reaxis AND the stopping rule
    # are cited (the §(ii.A) binary -> family move PLUS its anti-inflation
    # derivation). A misframe is incomplete only if the reframe is absent.
    reframe_complete = has_reaxis and has_stopping                              # (local)
    canonical_id_incomplete = has_misframe and not reframe_complete             # (local)
    severity = "S2" if canonical_id_incomplete else "NONE"                      # (local)

    if canonical_id_incomplete:
        diagnostic = (                                                          # (local)
            f"weighting_functional_family_fiber_count_misframe_without_reframe; "
            f"has_family_reaxis={has_reaxis}; has_stopping_rule={has_stopping}; "
            f"severity=S2_advisory_NOT_hard_halt; "
            f"missing=WEIGHTING_FUNCTIONAL_FAMILY_REAXIS_PLUS_TOPOLOGICAL_STOPPING_RULE; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    elif has_misframe and reframe_complete:
        diagnostic = (                                                          # (local)
            f"fiber_count_language_present_but_reframe_complete "
            f"(family-reaxis + stopping-rule both cited); "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    elif reframe_complete:
        diagnostic = (                                                          # (local)
            f"weighting_functional_family_reframe_complete; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )
    else:
        diagnostic = (                                                          # (local)
            f"no_weighting_functional_family_misframe_detected; "
            f"section_anchor={section_anchor or 'unspecified'}"
        )

    return {
        "has_fiber_count_misframe": has_misframe,
        "has_family_reaxis": has_reaxis,
        "has_stopping_rule": has_stopping,
        "reframe_complete": reframe_complete,
        "canonical_id_incomplete": canonical_id_incomplete,
        "severity": severity,
        "section_anchor": section_anchor,
        "diagnostic": diagnostic,
    }


# ---------------------------------------------------------------------------
# Pending-vs-Defective section-status classifier (S94 W6-17 extension)
# ---------------------------------------------------------------------------
#
# Per `.claude/rules/cross-pillar-bridge-anatomy.md` (Three-Level ladder +
# 5-anatomy IS-not-IN), `joint-theorem-promotion.md` (STAGE-0/1/2/3 pathway),
# and the deferred-pending intermediate verdict-class (above). Substrate
# framing: under `epistemic-discipline.md §"Layer-Decomposition"`, a bridge
# entry whose substrate-IS structural identity (Level-1) holds while its
# empirical realization (Level-2/Level-3) is PENDING is substrate-IS-LEGITIMATE.
# Blanket-FAILing such an entry is the audit-floor F-image of a methodology-floor
# veto over a substrate-IS structural PASS (forbidden per the Level-3 annotation
# discipline). This classifier teaches run_audit() to read a section's OWN
# declared substrate-IS status (STAGE-0/1 candidate, deferred-pending,
# PENDING-VERIFICATION) and to resolve parent/sub-section anatomy inheritance,
# so the verdict flows FROM the substrate's pending-vs-complete distinction
# TOWARD the audit verdict, never inverting.
#
# Status: METHODOLOGY-class audit-script extension. The classifier emits the
# verdict-string PASS-WITH-N-PENDING when every non-PASS section is
# legitimately-pending (genuinely_defective == 0 AND legitimately_pending > 0);
# FAIL (naming the genuinely-defective list) when genuinely_defective > 0;
# PASS when all sections PASS the literal 3-tier/5-anatomy/OE-form audit.
# ---------------------------------------------------------------------------

# A section's OWN declared status. Authoritative source: the section HEADER
# line (the §-anchor) AND the FIRST `**Status**:` body line — NOT a whole-body
# substring scan (cross-reference prose deep in a body routinely mentions
# `STAGE-3-PERMANENT per joint-theorem-promotion.md` etc. about OTHER entries).
# We scope the status read to the header + the leading status declaration.

# Pending-class status markers (legitimately-pending — substrate-IS-LEGITIMATE
# per the deferred-pending intermediate verdict-class + the STAGE-0/1 pathway).
PENDING_STATUS_PATTERNS = [                                    # (local)
    re.compile(r"STAGE-0\b", re.IGNORECASE),
    re.compile(r"STAGE-0-CANDIDATE", re.IGNORECASE),
    re.compile(r"STAGE-1-CANDIDATE", re.IGNORECASE),
    re.compile(r"CANDIDATE-PENDING", re.IGNORECASE),
    re.compile(r"PENDING-VERIFICATION", re.IGNORECASE),
    re.compile(r"PENDING-ANCHOR(?:-SWEEP)?", re.IGNORECASE),
    re.compile(r"PENDING-STAGE-2", re.IGNORECASE),
    re.compile(r"PENDING-S\d+-SUBSTRATE-PHYSICS", re.IGNORECASE),
    re.compile(r"REGISTRY-INCOMPLETE-PENDING-(?:PROXY-REFINEMENT|FIRST-EXTRACTION|OPERATIONAL-ALIGNMENT)", re.IGNORECASE),
]

# Superseded-class status markers (Option-A `supersedes`-tagged successor or an
# explicitly SUPERSEDED/DEPRECATED parent slot). Per `gate-verdicts.md §"Option A
# — sig_5 remediation pathway under absolute verdict permanence"`, the canonical
# reading is the latest NON-superseded line; a superseded slot is EXCLUDED from
# defect-scoring (it is retained on disk for the audit trail, not audited as a
# live bridge).
SUPERSEDED_STATUS_PATTERNS = [                                 # (local)
    re.compile(r"Option-A\s+`?supersedes`?-tagged\s+successor", re.IGNORECASE),
    re.compile(r"\bsupersedes=[a-f0-9]{40,64}\b", re.IGNORECASE),
    re.compile(r"^#+.*\bDEPRECATED\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^#+.*\bSUPERSEDED-BY\b", re.IGNORECASE | re.MULTILINE),
]

# Self-declared-NON-bridge markers (intra-pillar structural identity whose
# Element 2 is explicitly N/A — caught by the `"laboratory-in observable"`
# substring guard in the NEGATING context). Per `cross-pillar-bridge-anatomy.md
# §scope`, a cross-pillar bridge connects a substrate-IS observable to a
# laboratory-IN observable; an entry that self-declares "Element 2: N/A —
# Pillar-N-internal" / "NOT a cross-pillar bridge" / "Laboratory-IN observable:
# N/A" is NOT a cross-pillar bridge and is SKIPPED (not failed), extending the
# S93 W1-close scoping guard to the negating-context false-positives.
SELF_DECLARED_NON_BRIDGE_PATTERNS = [                          # (local)
    re.compile(r"NOT\s+a\s+cross-pillar\s+bridge", re.IGNORECASE),
    re.compile(r"Element\s*2[^:]*:\s*\*{0,2}\s*N/A\s*[—\-]\s*Pillar[- ]?\d", re.IGNORECASE),
    re.compile(r"Laboratory-IN\s+observable\*{0,2}:\s*\*{0,2}\s*N/A\s*[—\-]\s*Pillar", re.IGNORECASE),
    re.compile(r"Pillar[- ]?\d[- ]?internal\s+structural\s+identity\s+carve-out", re.IGNORECASE),
]

# §VII.X.SUFFIX sub-section anchor parser. A sub-section anchor of the form
# `§VII.<LETTERS>.<SUFFIX>` (e.g. §VII.AF.1.STATE-PROJ, §VII.AV.OP-PROJ) inherits
# its 5-anatomy + 3-level block from the parent slot `§VII.<LETTERS>` /
# `§VII.<LETTERS>.<n>` when the parent supplies the missing elements.
SUBSECTION_ANCHOR_REGEX = re.compile(                          # (local)
    r"§VII\.([A-Z0-9\-]+(?:\.[A-Z0-9\-]+)+)", re.IGNORECASE
)
PARENT_ANCHOR_REGEX = re.compile(                              # (local)
    r"§VII\.([A-Z0-9\-]+)", re.IGNORECASE
)


def _status_scope_text(section_text: str) -> str:
    """Return the header line + leading status declaration block of a section.

    The authoritative status of a §VII entry is declared in its HEADER line
    (the §-anchor, which often carries the status tag inline) plus the FIRST
    `**Status**:` body line. Scoping the status read here prevents
    cross-reference prose deep in the body (which routinely names
    STAGE-3-PERMANENT / STAGE-1-CANDIDATE about OTHER slots) from polluting the
    classification. Returns the header line + up to the first 12 body lines OR
    through the first `**Status**:` line (whichever is longer), so a status
    block declared a few lines down (after a provenance blockquote) is still
    captured.
    """
    lines = section_text.split("\n")                           # (local)
    header = lines[0] if lines else ""                         # (local)
    scope_lines = [header]                                     # (local)
    status_idx = None                                          # (local)
    for i, ln in enumerate(lines[1:], start=1):
        if re.search(r"\*\*Status\*\*:", ln):
            status_idx = i
            break
    # Include through the **Status** line if found within the first 30 lines,
    # else the leading 12 body lines (header-tag-only entries).
    if status_idx is not None and status_idx <= 30:
        scope_lines.extend(lines[1:status_idx + 1])            # (local)
    else:
        scope_lines.extend(lines[1:13])                        # (local)
    return "\n".join(scope_lines)


def detect_section_status(section_text: str, section_anchor: str = "") -> dict:
    """Classify a §VII entry's OWN declared status into a status-tier.

    Returns a structured diagnostic dict:
      - status_tier: str — one of {"pending", "superseded", "self-non-bridge",
        "settled"}. "settled" = own status is STAGE-3-PERMANENT / LANDED /
        REFUTED / no-pending-tag (i.e. a closed/permanent result that, if it
        FAILs the literal anatomy/OE-form audit, is a GENUINE defect).
      - is_pending: bool
      - is_superseded: bool
      - is_self_non_bridge: bool
      - matched_pending_markers / matched_superseded_markers /
        matched_non_bridge_markers: list[str]
      - section_anchor: str
      - diagnostic: str

    Status is read from the HEADER line + leading `**Status**:` block ONLY
    (via _status_scope_text), NOT a whole-body substring scan. Self-non-bridge
    is read from the FULL section text (the negating Element-2 declaration can
    sit anywhere in the anatomy block).
    """
    scope = _status_scope_text(section_text)                   # (local)

    matched_pending = [p.pattern for p in PENDING_STATUS_PATTERNS if p.search(scope)]   # (local)
    matched_superseded = [p.pattern for p in SUPERSEDED_STATUS_PATTERNS if p.search(scope)]  # (local)
    # Self-non-bridge: scan the FULL text (negating Element-2 may be in the body).
    matched_non_bridge = [
        p.pattern for p in SELF_DECLARED_NON_BRIDGE_PATTERNS if p.search(section_text)
    ]                                                          # (local)

    is_pending = len(matched_pending) > 0                      # (local)
    is_superseded = len(matched_superseded) > 0                # (local)
    is_self_non_bridge = len(matched_non_bridge) > 0           # (local)

    # Precedence: self-non-bridge (skip) > superseded (exclude) > pending
    # (legitimately-pending) > settled (defect-eligible). A self-declared
    # non-bridge is skipped regardless of pending status (it should never have
    # been scoped as a bridge); a superseded successor is excluded before its
    # pending status is read; a pending status protects from defect-scoring.
    if is_self_non_bridge:
        status_tier = "self-non-bridge"                        # (local)
    elif is_superseded:
        status_tier = "superseded"                             # (local)
    elif is_pending:
        status_tier = "pending"                                # (local)
    else:
        status_tier = "settled"                                # (local)

    diagnostic = (                                             # (local)
        f"status_tier={status_tier}; "
        f"is_pending={is_pending}; is_superseded={is_superseded}; "
        f"is_self_non_bridge={is_self_non_bridge}; "
        f"pending_markers={matched_pending}; "
        f"section_anchor={section_anchor or 'unspecified'}"
    )

    return {
        "status_tier": status_tier,
        "is_pending": is_pending,
        "is_superseded": is_superseded,
        "is_self_non_bridge": is_self_non_bridge,
        "matched_pending_markers": matched_pending,
        "matched_superseded_markers": matched_superseded,
        "matched_non_bridge_markers": matched_non_bridge,
        "section_anchor": section_anchor,
        "diagnostic": diagnostic,
    }


def parse_subsection_parent(anchor: str) -> str | None:
    """Return the parent §VII anchor for a sub-section anchor, else None.

    A sub-section anchor `§VII.<LETTERS>.<SUFFIX>` (e.g. §VII.AF.1.STATE-PROJ)
    has parent `§VII.<LETTERS>.<...>` truncated by ONE trailing dotted segment
    (parent of §VII.AF.1.STATE-PROJ is §VII.AF.1; parent of §VII.AF.1 is
    §VII.AF). Returns the immediate parent slot string `§VII.<...>` or None when
    the anchor has no dotted suffix (top-level slot).
    """
    m = SUBSECTION_ANCHOR_REGEX.search(anchor)                 # (local)
    if not m:
        return None
    dotted = m.group(1)                                        # (local) e.g. "AF.1.STATE-PROJ"
    segments = dotted.split(".")                               # (local)
    if len(segments) < 2:
        return None
    parent_dotted = ".".join(segments[:-1])                    # (local) drop ONE trailing segment
    return f"§VII.{parent_dotted}"


def resolve_anatomy_inheritance(
    sub_audit: dict,
    parent_audit: dict | None,
) -> dict:
    """Merge a parent's PASSing anatomy/tier elements into a sub-section audit.

    A §VII.X.SUFFIX sub-section that inherits its 5-anatomy + 3-level block
    from a parent §VII.X is NOT independently defective IF the parent supplies
    the elements the sub-section is missing. This walks the parent's present
    tier/anatomy/OE-form markers and merges them into the sub-section's missing
    sets, then recomputes a post-inheritance PASS.

    Returns the sub_audit dict augmented with:
      - inherited_from: str | None — parent anchor whose elements were merged.
      - missing_tiers_post_inheritance: list[str]
      - missing_anatomy_post_inheritance: list[str]
      - oe_form_pass_post_inheritance: bool
      - verdict_post_inheritance: "PASS" | "FAIL"

    When parent_audit is None (no parent located OR parent itself is non-PASS),
    no inheritance applies and the post-inheritance fields equal the literal
    fields. Inheritance is only granted from a parent that itself PASSES the
    literal audit (an inheriting sub-section cannot inherit completion from an
    equally-incomplete parent).
    """
    out = dict(sub_audit)                                      # (local)
    literal_missing_tiers = list(sub_audit.get("missing_tiers", []))      # (local)
    literal_missing_anatomy = list(sub_audit.get("missing_anatomy_elements", []))  # (local)
    literal_oe_pass = sub_audit.get("oe_form_check", {}).get("oe_form_pass", False)  # (local)

    if parent_audit is None or parent_audit.get("verdict") != "PASS":
        out["inherited_from"] = None
        out["missing_tiers_post_inheritance"] = literal_missing_tiers
        out["missing_anatomy_post_inheritance"] = literal_missing_anatomy
        out["oe_form_pass_post_inheritance"] = literal_oe_pass
        out["verdict_post_inheritance"] = sub_audit.get("verdict", "FAIL")
        return out

    # Parent PASSES → it supplies ALL 3 tiers + ALL 5 anatomy + OE-form. The
    # inheriting sub-section therefore clears every literal-missing element the
    # parent supplies. (A PASSing parent has 3/3 tiers, 5/5 anatomy, OE-pass by
    # the literal audit's PASS predicate, so inheritance clears all of them.)
    parent_missing_tiers = set(parent_audit.get("missing_tiers", []))     # (local)
    parent_missing_anatomy = set(parent_audit.get("missing_anatomy_elements", []))  # (local)
    parent_oe_pass = parent_audit.get("oe_form_check", {}).get("oe_form_pass", False)  # (local)

    # A tier/anatomy element is STILL missing post-inheritance only if BOTH the
    # sub-section AND the parent lack it (parent cannot supply what it lacks).
    missing_tiers_post = [t for t in literal_missing_tiers if t in parent_missing_tiers]    # (local)
    missing_anatomy_post = [a for a in literal_missing_anatomy if a in parent_missing_anatomy]  # (local)
    oe_pass_post = literal_oe_pass or parent_oe_pass           # (local)

    verdict_post = (                                           # (local)
        "PASS"
        if (not missing_tiers_post and not missing_anatomy_post and oe_pass_post)
        else "FAIL"
    )

    out["inherited_from"] = parent_audit.get("section_anchor")
    out["missing_tiers_post_inheritance"] = missing_tiers_post
    out["missing_anatomy_post_inheritance"] = missing_anatomy_post
    out["oe_form_pass_post_inheritance"] = oe_pass_post
    out["verdict_post_inheritance"] = verdict_post
    return out


def classify_section(
    section_audit: dict,
    status: dict,
    parent_audit: dict | None,
) -> dict:
    """Classify a §VII section into the pending-vs-defective trichotomy.

    Inputs:
      - section_audit: the literal audit_section() result (tier/anatomy/OE-form).
      - status: detect_section_status() result (status_tier).
      - parent_audit: the literal audit of the parent slot (or None).

    Classification (per plan §W6-17 method (a)/(b)/(c) + scoping extensions):
      - "PASS": the section PASSes the literal audit (3/3 tier, 5/5 anatomy,
        OE-form) — no classification needed beyond recording it.
      - "self-non-bridge": self-declared intra-pillar identity (Element 2 N/A)
        — SKIPPED (the S93 W1-close scoping guard extended to negating-context
        false-positives). Does NOT count toward genuinely-defective.
      - "superseded": Option-A successor / DEPRECATED slot — EXCLUDED from
        defect-scoring (canonical reading is the latest non-superseded line).
      - "legitimately-pending": non-PASS AND (status_tier == pending OR the
        sub-section inherits literal-PASS-completion from a PASSing parent).
        Substrate-IS-LEGITIMATE; does NOT count toward genuinely-defective.
      - "genuinely-defective": non-PASS, status_tier == settled, NOT
        self-non-bridge, NOT superseded, and does NOT inherit completion from a
        parent. COUNTS toward genuinely-defective; routed to OE-form/tier
        retrofit (mack-cosmic-bridge sole registry writer).

    Returns the section_audit augmented with: classification, status_tier,
    inherited_from, verdict_post_inheritance, and a per-section diagnostic.
    """
    literal_verdict = section_audit.get("verdict", "FAIL")     # (local)

    # Resolve parent inheritance (no-op when parent is None / non-PASS).
    merged = resolve_anatomy_inheritance(section_audit, parent_audit)  # (local)
    inherits_completion = (                                    # (local)
        merged.get("inherited_from") is not None
        and merged.get("verdict_post_inheritance") == "PASS"
    )

    status_tier = status["status_tier"]                        # (local)

    # PASS is checked FIRST: a section that PASSes the full literal audit
    # (3/3 tier, 5/5 anatomy, OE-form) is unambiguously complete and recorded
    # as PASS, regardless of any self-non-bridge prose it may carry. The
    # self-non-bridge skip is a scoping RESCUE for false-FAILs (entries the
    # `"laboratory-in observable"` substring guard wrongly scoped in via a
    # negating context); it must NOT demote a genuine literal-PASS.
    if literal_verdict == "PASS":
        classification = "PASS"                                # (local)
    elif status_tier == "self-non-bridge":
        classification = "self-non-bridge"                     # (local)
    elif status_tier == "superseded":
        classification = "superseded"                          # (local)
    elif status_tier == "pending":
        classification = "legitimately-pending"                # (local)
    elif inherits_completion:
        # Non-PASS, non-pending, but the sub-section inherits a complete
        # 5-anatomy/3-level block from a PASSing parent → legitimately-pending
        # (the sub-section is a companion slot reusing the parent's anatomy).
        classification = "legitimately-pending"                # (local)
    else:
        classification = "genuinely-defective"                 # (local)

    merged["classification"] = classification
    merged["status_tier"] = status_tier
    merged["status_diagnostic"] = status["diagnostic"]
    return merged


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def find_bridge_sections(registry_text: str) -> list[dict]:
    """Locate all §VII.W / §VII.X / ... bridge-theorem sections."""
    sections = []                                          # (local)
    matches = list(BRIDGE_SECTION_REGEX.finditer(registry_text))
    if not matches:
        return sections
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(registry_text)
        sections.append({
            "anchor": m.group(0).strip(),
            "letter": m.group(1).upper(),
            "start": start,
            "end": end,
            "text": registry_text[start:end],
        })
    return sections


def check_markers(text_lower: str, marker_dict: dict) -> dict:
    """For each marker key, return whether ANY of its substring
    candidates appears in the lowercased section text.
    """
    out = {}                                               # (local)
    for key, candidates in marker_dict.items():
        present = any(c in text_lower for c in candidates)
        out[key] = {
            "present": present,
            "matched_candidates": [c for c in candidates if c in text_lower],
        }
    return out


def audit_section(section: dict) -> dict:
    """Audit a single §VII.X bridge-theorem section.

    S88 W7a-73 EXTENSION: Element 2 OE-form regex pass added as a
    third required condition for PASS, alongside the existing
    tier-marker and anatomy-element checks. Prose-only Element 2
    forms FAIL the audit per `cross-pillar-bridge-anatomy.md
    §"Element 2 OE-form discipline"`.
    """
    text_lower = section["text"].lower()                  # (local)
    tier_check = check_markers(text_lower, TIER_MARKERS)  # (local)
    anatomy_check = check_markers(text_lower, ANATOMY_ELEMENTS)

    tier_count = sum(1 for v in tier_check.values() if v["present"])
    anatomy_count = sum(1 for v in anatomy_check.values() if v["present"])

    # S88 W7a-73: Element 2 OE-form regex pass (case-sensitive over the
    # ORIGINAL section text since the regex contains Unicode and case-
    # sensitive operator symbols Tr / P / Π).
    oe_form_check = audit_element_2_oe_form(section["text"])  # (local)

    verdict = (
        "PASS" if (
            tier_count == 3
            and anatomy_count == 5
            and oe_form_check["oe_form_pass"]
        )
        else "FAIL"
    )

    missing_tiers = [k for k, v in tier_check.items() if not v["present"]]
    missing_anatomy = [k for k, v in anatomy_check.items() if not v["present"]]
    missing_oe_form = []                                  # (local)
    if not oe_form_check["oe_positive_match"]:
        missing_oe_form.append("OE-form positive-match (\\int/∫ + Tr + P_<index>)")
    if oe_form_check["oe_negative_match"]:
        missing_oe_form.append(
            "FORBIDDEN prose-only Element 2 (measurement|spectroscopy|test)"
        )

    return {
        "section_anchor": section["anchor"],
        "verdict": verdict,
        "tier_present_count": tier_count,
        "anatomy_present_count": anatomy_count,
        "tier_check": tier_check,
        "anatomy_check": anatomy_check,
        "oe_form_check": oe_form_check,
        "missing_tiers": missing_tiers,
        "missing_anatomy_elements": missing_anatomy,
        "missing_oe_form": missing_oe_form,
    }


def run_audit() -> dict:
    """Audit all bridge-theorem entries in permanent-results-registry."""
    if not REGISTRY_PATH.exists():
        return {
            "audit_id": "S86-W5-CROSS-PILLAR-BRIDGE-COMPLETENESS",
            "verdict": "INFO_NO_REGISTRY",
            "registry_path": str(REGISTRY_PATH),
            "blocked_by": "permanent-results-registry.md not found",
        }

    text = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)
    all_matched = find_bridge_sections(text)              # (local)

    # S93 W1-close scoping guard: the 5-anatomy audit applies ONLY to
    # cross-pillar BRIDGE entries. Per cross-pillar-bridge-anatomy.md §scope, a
    # cross-pillar bridge connects a substrate-IS observable to a laboratory-IN
    # observable. The widened BRIDGE_SECTION_REGEX (S93 W1-2) also matches
    # OP-PROJ algebra-INVARIANT NON-bridge entries (e.g. §VII.BC.OP-PROJ
    # Wedderburn-image relation: 0 laboratory-IN observable, 0 bridge map);
    # auditing those as bridges is a false FAIL. Restrict to sections that
    # self-declare a laboratory-IN observable (Element 2 — the defining feature
    # of a cross-pillar bridge); non-bridges are skipped, not failed.
    sections = [                                          # (local)
        s for s in all_matched
        if "laboratory-in observable" in s["text"].lower()
    ]
    non_bridge_skipped = [                                # (local)
        s["anchor"] for s in all_matched if s not in sections
    ]

    if not sections:
        return {
            "audit_id": "S86-W5-CROSS-PILLAR-BRIDGE-COMPLETENESS",
            "verdict": "INFO_NO_BRIDGE",
            "registry_path": str(REGISTRY_PATH),
            "note": "No §VII.W / §VII.X / ... bridge-theorem entries found yet. "
                    "Audit becomes load-bearing once first bridge-entry lands "
                    "(S87 CF-1 per W-5 spec).",
        }

    # Literal per-section audit (3-tier / 5-anatomy / OE-form), keyed by anchor
    # so sub-sections can look up their parent's literal audit for inheritance.
    section_audits = [audit_section(s) for s in sections]      # (local)
    audit_by_anchor = {sa["section_anchor"]: sa for sa in section_audits}  # (local)

    # S94 W6-17 status-aware classification. For each section: detect its OWN
    # declared status-tier, resolve parent/sub-section anatomy inheritance, and
    # classify into the pending-vs-defective trichotomy (+ self-non-bridge /
    # superseded scoping extensions). The blanket all_pass FAIL is REPLACED by a
    # status-aware verdict: PASS-WITH-N-PENDING when every non-PASS section is
    # legitimately-pending (genuinely_defective == 0 AND legitimately_pending > 0).
    classified = []                                            # (local)
    for sec, sa in zip(sections, section_audits):
        status = detect_section_status(sec["text"], sa["section_anchor"])  # (local)
        parent_slot = parse_subsection_parent(sa["section_anchor"])        # (local)
        parent_audit = None                                    # (local)
        if parent_slot is not None:
            # Locate the parent audit by prefix-matching the parent slot string
            # against the audited anchors (anchors carry trailing descriptive
            # prose, so match on the leading §VII.<...> token).
            for cand_anchor, cand_audit in audit_by_anchor.items():
                pm = PARENT_ANCHOR_REGEX.search(cand_anchor)   # (local)
                if pm is None:
                    continue
                cand_slot = f"§VII.{pm.group(1)}"              # (local)
                # The parent slot string must match the candidate's leading
                # §VII.<...> token EXACTLY (so §VII.AF.1 parents §VII.AF.1.STATE-PROJ,
                # not §VII.AF.1.OP-PROJ which is itself a sibling sub-section).
                cand_dotted = SUBSECTION_ANCHOR_REGEX.search(cand_anchor)  # (local)
                cand_full = (                                  # (local)
                    f"§VII.{cand_dotted.group(1)}" if cand_dotted else cand_slot
                )
                if cand_full == parent_slot and cand_audit is not sa:
                    parent_audit = cand_audit
                    break
        classified.append(classify_section(sa, status, parent_audit))      # (local)

    n_pass = sum(1 for c in classified if c["classification"] == "PASS")               # (local)
    n_pending = sum(1 for c in classified if c["classification"] == "legitimately-pending")  # (local)
    n_defective = sum(1 for c in classified if c["classification"] == "genuinely-defective")  # (local)
    n_self_non_bridge = sum(1 for c in classified if c["classification"] == "self-non-bridge")  # (local)
    n_superseded = sum(1 for c in classified if c["classification"] == "superseded")   # (local)

    genuinely_defective = [                                     # (local)
        {
            "section_anchor": c["section_anchor"],
            "status_tier": c["status_tier"],
            "missing_tiers": c.get("missing_tiers", []),
            "missing_anatomy_elements": c.get("missing_anatomy_elements", []),
            "missing_oe_form": c.get("missing_oe_form", []),
        }
        for c in classified if c["classification"] == "genuinely-defective"
    ]
    legitimately_pending = [                                    # (local)
        {"section_anchor": c["section_anchor"], "status_tier": c["status_tier"],
         "inherited_from": c.get("inherited_from")}
        for c in classified if c["classification"] == "legitimately-pending"
    ]

    # Status-aware verdict string:
    #   PASS                 — all sections PASS the literal audit (n_pending == 0
    #                          AND n_defective == 0).
    #   PASS-WITH-N-PENDING  — genuinely_defective == 0 AND legitimately_pending > 0
    #                          (every non-PASS is legitimately-pending; the audit
    #                          no longer blanket-FAILs legitimately-pending growth).
    #   FAIL                 — genuinely_defective > 0 (named + routed to mack for
    #                          OE-form/tier retrofit; audit correctly FAILs until
    #                          that lands).
    if n_defective > 0:
        verdict = "FAIL"                                       # (local)
    elif n_pending > 0:
        verdict = f"PASS-WITH-{n_pending}-PENDING"             # (local)
    else:
        verdict = "PASS"                                       # (local)

    return {
        "audit_id": "S86-W5-CROSS-PILLAR-BRIDGE-COMPLETENESS",
        "verdict": verdict,
        "verdict_class": (                                     # (local)
            "PASS-WITH-N-PENDING" if verdict.startswith("PASS-WITH-")
            else verdict
        ),
        "n_bridge_sections": len(sections),
        "n_pass": n_pass,
        "legitimately_pending_count": n_pending,
        "genuinely_defective_count": n_defective,
        "self_non_bridge_count": n_self_non_bridge,
        "superseded_count": n_superseded,
        "genuinely_defective": genuinely_defective,
        "legitimately_pending": legitimately_pending,
        "non_bridge_skipped": non_bridge_skipped,
        "section_audits": classified,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-pillar bridge-theorem completeness audit (T4-8 / S86 W-5)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on FAIL")
    args = parser.parse_args()

    result = run_audit()                                   # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-5 / T4-8 Cross-Pillar Bridge Completeness Audit ===")
        print(f"Verdict: {result['verdict']}")
        for k, v in result.items():
            if k in ("verdict", "audit_id", "section_audits",
                     "genuinely_defective", "legitimately_pending"):
                continue
            print(f"  {k}: {v}")
        # S94 W6-17 status-aware summary of the genuinely-defective set.
        for gd in result.get("genuinely_defective", []):
            print(f"\n  GENUINELY-DEFECTIVE: {gd['section_anchor']}")
            print(f"    status_tier: {gd['status_tier']}")
            if gd["missing_tiers"]:
                print(f"    missing_tiers: {gd['missing_tiers']}")
            if gd["missing_anatomy_elements"]:
                print(f"    missing_anatomy: {gd['missing_anatomy_elements']}")
            if gd["missing_oe_form"]:
                print(f"    missing_oe_form: {gd['missing_oe_form']}")
        for sa in result.get("section_audits", []):
            cls = sa.get("classification", "?")                # (local)
            print(f"\n  Section: {sa['section_anchor']} → "
                  f"{sa['verdict']} [{cls}]")
            print(f"    Tiers present: {sa['tier_present_count']}/3")
            print(f"    Anatomy elements present: {sa['anatomy_present_count']}/5")
            if sa.get("inherited_from"):
                print(f"    inherited_from: {sa['inherited_from']}")
            if sa["missing_tiers"]:
                print(f"    Missing tiers: {sa['missing_tiers']}")
            if sa["missing_anatomy_elements"]:
                print(f"    Missing anatomy: {sa['missing_anatomy_elements']}")

    # --strict exits nonzero on FAIL ONLY. PASS-WITH-N-PENDING is a non-FAIL
    # verdict (genuinely_defective == 0); it does NOT trip the strict exit.
    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
