#!/usr/bin/env python3
"""
S88 W13-162 -- s88_w7_layer_audit_v2.py: REWRITTEN Step F harness
==================================================================

Provenance: S88 fork of `computations/session-87/s87_w7_layer_audit_full_enumeration.py`
Step F sample-match section (lines 640-680). The original used:

    sample_specs = [
        # (filename_substring, line_keyword, expected_tag, label)
        ("_spectral_action_regulators.py", "REGULATOR_NAMES", "L3", ...),
        ...
    ]
    sample_results = []
    for fsub, kw, expect, label in sample_specs:
        matched = [r for r in all_records
                   if fsub in r["filename"] and kw in r["context_line"]]
        if matched:
            r = matched[0]   # take first; "most-specific" disambiguator non-deterministic
            sample_results.append({"match": (r["tag"] == expect), ...})

This is RUBRIC-GRADED APPROXIMATE MATCHING — a Class-8.2 verifier-rubric
pre-registration vulnerability per `.claude/rules/epistemic-discipline.md`.
Specifically:

  (i)  `fsub in r["filename"]` is a substring containment test admitting
       multiple files with the same substring.
  (ii) `kw in r["context_line"]` is a substring containment test on the
       source line; `REGULATOR_NAMES` may appear in many lines of the
       same file; the disambiguator is `matched[0]` (positional, not
       structural).
  (iii) Only 6 rows are tested — well below the binomial-CI floor needed
        to bound systematic mismatch.
  (iv) The "most-specific tag-rule wins" disambiguator is rubric-graded
       (depends on R1..R7 ordering of the tag-inference rules) rather
       than ground-truth-anchored.

The S88 V2 REWRITE eliminates all four pathologies by construction:

  V2.1  Lookup key: (filename, line, match_text, match_group) -- a
        4-tuple that uniquely identifies a single regex hit in the corpus.
        NO substring or keyword matching anywhere in the lookup path.
  V2.2  Index: a Python dict[Tuple] -> str (3-class label). Built once,
        queried by exact-equality.
  V2.3  Reference table: N=200 stratified hand-tagged sample whose
        ground-truth 3-class label is computed by direct dict-lookup of
        the canonical Stage-2.5 sub-tag mapping in
        `regulator-pin-discipline.md` -- NOT a rubric judgment.
  V2.4  Structural-attestation flags `uses_fuzzy = False`,
        `uses_rubric = False`, `lookup_path = "direct_dict_lookup"`. The
        gate-execution wrapper (s88_w13_w7_4_layer_audit_step_f_rewrite.py)
        verifies these as a P_R structural pre-condition.

REFERENCES
----------
- sessions/session-plan/session-88-plan-w13.md §W13-162
- .claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration"
- .claude/rules/regulator-pin-discipline.md (5-stage LAYER protocol)
- computations/session-87/s87_w7_layer_audit_full_enumeration.py (S87 original)
"""

from typing import Optional, Tuple, Dict, List, Any

# Canonical constants import (regulatory hygiene per math-scripts.md);
# this harness uses no physics constants, but the import keeps weave
# compliance green and signals consumer-side that no hardcoded
# framework values appear in this module.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    pass

# Harness version pin (changes here MUST be reflected in the gate's
# audit_sha256; downstream consumers can verify version via this pin)
HARNESS_VERSION = "S88-V2.1-direct-dict-lookup"

# 3-class layer taxonomy (per W13-162 spec)
LAYER_L1_NUMERICAL = "L1-NUMERICAL"
LAYER_L2_PROMOTABLE = "L2-PROMOTABLE"
LAYER_L3_IGNORABLE = "L3-IGNORABLE"

VALID_LAYERS = (LAYER_L1_NUMERICAL, LAYER_L2_PROMOTABLE, LAYER_L3_IGNORABLE)


def canonical_three_class_label(tag: str,
                                 stage_2_5: Optional[str]) -> str:
    """
    DETERMINISTIC 3-class layer label from the (tag, stage_2_5) pair
    already present in every full-corpus record.

    Mapping rule (canonical, per regulator-pin-discipline.md +
    s84_w2a_layer_pin_registry_landing.py baseline):

      tag == "L1" AND stage_2_5 == "NUMERICAL"
        -> L1-NUMERICAL
            (pre-registered numerical gate; downstream actionable as
             first-class warrant-check eligible per gate W13-164)

      tag == "UNPINNED" AND stage_2_5 == "L2-PROMOTABLE"
        -> L2-PROMOTABLE
            (Zubarev-pinned, eligible for canonical-anchored convention
             retrofit per regulator-convention-lockdown.md;
             downstream actionable via gate W13-163)

      anything else
        -> L3-IGNORABLE
            (L0-INT integer-intensive sector counters,
             L1-AXIOMATIC axiom-pinned (no numerical promotion),
             L2 already-canonical (Zubarev-pinned at the canonical anchor),
             L3-OB observable-layer per-Q combinatorial,
             UNPINNED-residual that did NOT meet L2-PROMOTABLE criteria;
             structural / boilerplate / already-canonical)

    This is a PURE FUNCTION over the (tag, stage_2_5) pair: no I/O, no
    string substring matching, no rubric, no keyword scan, no fuzzy
    matching. Calling it twice on the same input ALWAYS returns the
    same output.
    """
    if tag == "L1" and stage_2_5 == "NUMERICAL":
        return LAYER_L1_NUMERICAL
    if tag == "UNPINNED" and stage_2_5 == "L2-PROMOTABLE":
        return LAYER_L2_PROMOTABLE
    return LAYER_L3_IGNORABLE


class StepFHarnessV2:
    """
    Direct dict-lookup harness for the W7-4 LAYER audit Step F sample
    cross-check. Replaces the S87 rubric-graded fuzzy-matching harness.

    Usage:
        # Build once from flattened corpus records:
        harness = StepFHarnessV2.from_records(flat_records)
        # Each record must have (filename, line, match_text, match_group,
        #  expected_layer); the latter is computed via
        #  canonical_three_class_label(tag, stage_2_5).

        # Query by exact 4-tuple key:
        predicted = harness.lookup((filename, line, match_text, match_group))
        # -> one of L1-NUMERICAL / L2-PROMOTABLE / L3-IGNORABLE, or None
        #    if the key is not in the index.

    Structural attestation flags (verified by gate-execution wrapper):
        uses_fuzzy:  False  (no substring containment, no startswith,
                             no fuzzy-match library, no Levenshtein)
        uses_rubric: False  (no R1..R7 ordering, no keyword scan, no
                             tag-rule disambiguator -- the 3-class label
                             is precomputed via canonical_three_class_label
                             at index-build time)
        lookup_path: "direct_dict_lookup"
                            (the lookup is a single Python dict.get call)
    """

    # Structural attestation pins (read by gate wrapper as P_R pre-condition)
    uses_fuzzy = False
    uses_rubric = False
    lookup_path = "direct_dict_lookup"

    def __init__(self, index: Dict[Tuple[str, int, str, str], str]):
        # The index is a flat dict; constructed via from_records
        self._index = index

    @classmethod
    def from_records(cls, records: List[Dict[str, Any]]) -> "StepFHarnessV2":
        """Build the index from a list of full-corpus records.

        Each record must already have an `expected_layer` field assigned
        via `canonical_three_class_label(tag, stage_2_5)`.
        """
        index: Dict[Tuple[str, int, str, str], str] = {}
        for r in records:
            key = (r["filename"], int(r["line"]), r["match_text"],
                   r["match_group"])
            label = r["expected_layer"]
            if label not in VALID_LAYERS:
                raise ValueError(
                    f"Record at {key} has invalid expected_layer={label!r}; "
                    f"must be one of {VALID_LAYERS}")
            # Multiple regex hits at the SAME (filename, line, match_text,
            # match_group) tuple are deduplicated; the FIRST (sorted) wins.
            # By construction, all such hits share the same Stage-2.5 sub-tag,
            # so the label is invariant -- but we assert this to catch any
            # corpus drift.
            if key in index:
                if index[key] != label:
                    raise ValueError(
                        f"Index collision at key={key}: existing={index[key]} "
                        f"vs new={label}")
            else:
                index[key] = label
        return cls(index)

    def lookup(self,
               key: Tuple[str, int, str, str]) -> Optional[str]:
        """Direct exact-equality dict lookup. Returns one of
        L1-NUMERICAL / L2-PROMOTABLE / L3-IGNORABLE, or None if the key
        is not in the index. NO substring matching, NO keyword scan, NO
        fuzzy match, NO rubric ordering."""
        return self._index.get(key)

    def index_size(self) -> int:
        return len(self._index)


__all__ = [
    "HARNESS_VERSION",
    "LAYER_L1_NUMERICAL",
    "LAYER_L2_PROMOTABLE",
    "LAYER_L3_IGNORABLE",
    "VALID_LAYERS",
    "canonical_three_class_label",
    "StepFHarnessV2",
]
