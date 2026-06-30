"""S92-W5-CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING.

VERIFY-FIRST-RETROFIT of the §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry
landing. Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`
for all §VII registry rows.

Pre-registered per `sessions/session-plan/session-92-plan-w5.md §W5-3`.

Phase A (VERIFY) - read sessions/permanent-results-registry.md and locate
the canonical §VII.AU.OP-PROJ block. Compute its content_sha256 and check
6 predicates (i)..(vi) against `cross-pillar-bridge-anatomy.md §"Audit at
plan-freeze"` items 1-7.

Phase B (DECIDE) - if all 6 predicates PASS, close as VERIFY-ONLY-PASS
(NO Edit).

Phase C (RETROFIT) - if any predicate FAILS, single-shot AFTER-pattern
Edit per `registry-landing.md §"Bridge-Landing Script Architecture"`:
build_promotion_text in memory -> write_atomic_with_fsync -> re_read +
verify_section_matches -> emit ONE verdict line.

Two canonical anchors (SOURCE-DOUBLE-CITE-CO-PRIMARY):
  Anchor_1 W6-1 PASS-A:
    d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d
    (computations/session-91/s91_gate_verdicts.txt:128)
  Anchor_2 S91 W5/W6 in-session promotion:
    54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459
    (computations/session-91/s91_gate_verdicts.txt:270)
"""
from __future__ import annotations

# Section 1 -- Imports
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# Section 2 -- Canonical-constants import (MANDATORY for S34+ per
# computations/_shared/CLAUDE.md). The registry-text VERIFY-FIRST-RETROFIT
# does not consume framework numerics; the import is present to satisfy
# the canonical-import discipline and to ensure the two FWD-C1 two-pin
# canonical anchors exist in canonical_constants.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (  # noqa: F401
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
)

# Section 3 -- Gate-identity constants
GATE_ID = "S92-W5-CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING"
SCHEME = "registry-text-VERIFY-FIRST-RETROFIT-AFTER-pattern"
CONVENTION = (
    "VII-AU-OP-PROJ-STAGE-1-CANDIDATE-landing-VERIFY-FIRST-RETROFIT-"
    "citing-S91-W5-W6-in-session-promotion-and-W6-1-PASS-A-empirical-anchor"
)
L_MAX = "N/A"
SCHEMA_VERSION = "S87+"

PROJECT_ROOT = Path(__file__).resolve().parents[2]                       # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = (
    PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
)
DATA_JSON = (
    PROJECT_ROOT
    / "computations"
    / "session-92"
    / "s92_w5_vii_au_op_proj_stage_1_candidate_landing_verify_first_retrofit.json"
)

# Anchors (full 64-char audit_sha256 values pinned at plan-freeze)
ANCHOR_1_W6_1_PASS_A_FULL = (
    "d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d"
)
ANCHOR_2_S91_W5_W6_PROMOTION_FULL = (
    "54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459"
)
ANCHOR_1_SHORT = ANCHOR_1_W6_1_PASS_A_FULL[:16]                           # (local)
ANCHOR_2_SHORT = ANCHOR_2_S91_W5_W6_PROMOTION_FULL[:16]                   # (local)

# Plan §W5-3 PASS-predicate boundary
MIN_SUBSTANTIVE_LINES = 50                                                # (local)

# Cross-pillar-bridge-anatomy.md verdict tag for SOURCE-DOUBLE-CITE-CO-PRIMARY
DOUBLE_CITE_TAG = "SOURCE-DOUBLE-CITE-CO-PRIMARY"                         # (local)

# Plan-pinned input rule files / verdict files used for audit_sha256 input
# pin map. The SHA digest of each file's content is captured at runtime
# per gate-verdicts.md §"S87+ canonical form" dual-SHA discipline.
RULE_CROSS_PILLAR_BRIDGE_ANATOMY = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
RULE_JOINT_THEOREM_PROMOTION = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
RULE_REGISTRY_LANDING = (
    PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
)
S91_VERDICT_PATH = (
    PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
)
CANONICAL_CONSTANTS_PATH = (
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
)


# Section 4 -- SHA helpers
def sha256_of_text(text: str) -> str:
    """Return the SHA-256 hex digest of ``text`` (utf-8 encoded)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_of_file(path: Path) -> str:
    """Return the SHA-256 hex digest of the file at ``path``."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closure_hash(input_pin_map: dict[str, str]) -> str:
    """Audit-trail SHA over a sorted (key, value) ledger.

    Each key|value pair is appended in canonical order, joined by ``\n``
    delimiters. This matches the canonical pattern used by
    ``_critpath_audit.append_verdict`` and ``_plan_staleness_audit.closure_hash``.
    """
    items = sorted(input_pin_map.items())                                 # (local)
    joined = "\n".join(f"{k}|{v}" for k, v in items)                      # (local)
    return sha256_of_text(joined)


# Section 5 -- Locate the canonical §VII.AU.OP-PROJ block
RE_VII_AU_HEADING = re.compile(
    r"^### §VII\.AU\.OP-PROJ\b", flags=re.MULTILINE
)
RE_NEXT_VII_HEADING = re.compile(
    r"^### §VII\.[A-Z]", flags=re.MULTILINE
)


def locate_canonical_block(registry_text: str) -> tuple[int, int, str]:
    """Locate the canonical §VII.AU.OP-PROJ block in the registry.

    The plan refers to lines 17903-17999 by their pre-S91 position. After
    S91 W5/W6 in-session landings the canonical CF-64 RETRY entry --
    which is the one carrying the S91 W5/W6 STAGE-1-CANDIDATE promotion
    sub-section -- is structurally identified by its heading
    ``### §VII.AU.OP-PROJ (CF-64 RETRY``. We scan all matches and select
    the canonical content-host (the one carrying the S91 W5/W6 promotion
    sub-section text), returning the (start_byte, end_byte, block_text)
    triple.
    """
    headings = list(RE_VII_AU_HEADING.finditer(registry_text))            # (local)
    if not headings:
        raise RuntimeError("§VII.AU.OP-PROJ heading not found in registry")

    next_headings = list(RE_NEXT_VII_HEADING.finditer(registry_text))     # (local)

    canonical_start = None                                                # (local)
    canonical_end = None                                                  # (local)
    canonical_text = None                                                 # (local)

    for h in headings:
        h_start = h.start()                                               # (local)
        # End-of-block = position of the next §VII heading after h_start
        h_end = len(registry_text)                                        # (local)
        for nh in next_headings:
            if nh.start() > h_start:
                h_end = nh.start()
                break
        block_text = registry_text[h_start:h_end]                         # (local)
        # The canonical content-host is the one with the S91 W5/W6
        # promotion sub-section. Heuristic: must contain the sub-section
        # heading "S91 W5/W6 sub-class transition" AND must cite Anchor_1
        # full SHA somewhere in the block. The CF-64 RETRY at line 18634+
        # satisfies both; the §VII.AAU.OP-PROJ WITHDRAWN block does not.
        if (
            "S91 W5/W6 sub-class transition" in block_text
            and ANCHOR_1_W6_1_PASS_A_FULL in block_text
        ):
            canonical_start = h_start
            canonical_end = h_end
            canonical_text = block_text
            break

    if canonical_text is None:
        # Fallback: pick the LAST §VII.AU.OP-PROJ heading (CF-64 RETRY is
        # typically the last canonical content-host emission).
        h = headings[-1]                                                  # (local)
        canonical_start = h.start()
        canonical_end = len(registry_text)
        for nh in next_headings:
            if nh.start() > canonical_start:
                canonical_end = nh.start()
                break
        canonical_text = registry_text[canonical_start:canonical_end]

    return canonical_start, canonical_end, canonical_text


# Section 6 -- VERIFY predicates (i)..(vi)
def verify_predicates(block_text: str) -> dict[str, bool | str | int]:
    """Evaluate the 6 VERIFY predicates per plan §W5-3.

    PASS predicate (per `wave-classification.md §M1`):
      (a) §VII.AU.OP-PROJ block present in registry text
      (b) 5-anatomy Elements 1-5 all present
      (c) 3-level ladder Levels 1-3 all present (Level 2 sub-class
          Level-2-binding)
      (d) S91 W5/W6 promotion citation block present (cites Anchor_1
          AND Anchor_2 audit_sha256 values)
      (e) Hybrid Independence Test K=3 advancement preserved
      (f) substantive_line_count(block) >= 50

    Returns a dictionary with per-predicate booleans, plus the
    content_sha256 of the canonical block (computed inside this
    function for audit-trail completeness).
    """
    # Predicate (a): block presence
    predicate_a = bool(block_text) and "§VII.AU.OP-PROJ" in block_text    # (local)

    # Predicate (b): 5-anatomy Elements 1-5
    # The anatomy is declared with an enumerated "IS-not-IN anatomy"
    # heading and 5 numbered sub-bullets. We require the ENUMERATED list
    # (1./2./3./4./5.) to be present alongside the names of each element.
    has_anatomy_heading = bool(
        re.search(r"\*\*IS-not-IN anatomy\*\*", block_text)
    )                                                                     # (local)
    has_elem_1 = bool(
        re.search(r"\*\*Substrate-IS observable\*\*", block_text)
    )                                                                     # (local)
    has_elem_2 = bool(
        re.search(r"\*\*Laboratory-IN observable\*\*", block_text)
    )                                                                     # (local)
    has_elem_3 = bool(re.search(r"\*\*Bridge map\*\*", block_text))       # (local)
    has_elem_4 = bool(
        re.search(r"\*\*Algebraic envelope\*\*", block_text)
    )                                                                     # (local)
    has_elem_5 = bool(
        re.search(r"\*\*Empirical anchor\*\*", block_text)
    )                                                                     # (local)
    predicate_b = (
        has_anatomy_heading
        and has_elem_1
        and has_elem_2
        and has_elem_3
        and has_elem_4
        and has_elem_5
    )                                                                     # (local)

    # Predicate (c): 3-level ladder Levels 1-3 + Level-2-binding sub-class
    has_ladder_heading = bool(
        re.search(r"\*\*Three-level structural-confidence ladder\*\*",
                  block_text)
    )                                                                     # (local)
    has_level_1 = bool(re.search(r"\bLevel 1\b", block_text))             # (local)
    has_level_2 = bool(re.search(r"\bLevel 2\b", block_text))             # (local)
    has_level_3 = bool(re.search(r"\bLevel 3\b", block_text))             # (local)
    has_level_2_binding = bool(
        re.search(r"Level-2-binding", block_text)
    )                                                                     # (local)
    predicate_c = (
        has_ladder_heading
        and has_level_1
        and has_level_2
        and has_level_3
        and has_level_2_binding
    )                                                                     # (local)

    # Predicate (d): S91 W5/W6 promotion citation block + both anchors
    has_promotion_heading = (
        "S91 W5/W6 sub-class transition" in block_text
        or "S91 W5/W6 STAGE-1-CANDIDATE promotion" in block_text
    )                                                                     # (local)
    has_anchor_1 = ANCHOR_1_W6_1_PASS_A_FULL in block_text                # (local)
    has_anchor_2 = ANCHOR_2_S91_W5_W6_PROMOTION_FULL in block_text        # (local)
    predicate_d = (
        has_promotion_heading and has_anchor_1 and has_anchor_2
    )                                                                     # (local)

    # Predicate (e): Hybrid Independence Test K=3 advancement preserved
    has_hit_heading = bool(
        re.search(r"\*\*Hybrid Independence Test\*\*", block_text)
    )                                                                     # (local)
    has_k_advancement = (
        "K=3 → K=4" in block_text
        or "K=3 -> K=4" in block_text
        or "K=3 → K=4" in block_text
    )                                                                     # (local)
    has_mandatory_at_k3 = (
        "MANDATORY at K=3" in block_text
        or "MANDATORY-K=3" in block_text
        or "MANDATORY since S88 W4a-17" in block_text
    )                                                                     # (local)
    predicate_e = (
        has_hit_heading and has_k_advancement and has_mandatory_at_k3
    )                                                                     # (local)

    # Predicate (f): substantive_line_count >= 50
    # We count NON-EMPTY lines in the block as "substantive" lines.
    lines = block_text.splitlines()                                       # (local)
    substantive_line_count = sum(
        1 for ln in lines if ln.strip() and not ln.strip().startswith("#")
    )                                                                     # (local)
    predicate_f = substantive_line_count >= MIN_SUBSTANTIVE_LINES         # (local)

    content_sha = sha256_of_text(block_text)                              # (local)

    return {
        "predicate_a_block_present": predicate_a,
        "predicate_b_5anatomy_complete": predicate_b,
        "predicate_b_detail": {
            "has_anatomy_heading": has_anatomy_heading,
            "has_elem_1": has_elem_1,
            "has_elem_2": has_elem_2,
            "has_elem_3": has_elem_3,
            "has_elem_4": has_elem_4,
            "has_elem_5": has_elem_5,
        },
        "predicate_c_3level_ladder_complete": predicate_c,
        "predicate_c_detail": {
            "has_ladder_heading": has_ladder_heading,
            "has_level_1": has_level_1,
            "has_level_2": has_level_2,
            "has_level_3": has_level_3,
            "has_level_2_binding": has_level_2_binding,
        },
        "predicate_d_s91_promotion_cite_both_anchors": predicate_d,
        "predicate_d_detail": {
            "has_promotion_heading": has_promotion_heading,
            "has_anchor_1_w6_1_pass_a": has_anchor_1,
            "has_anchor_2_s91_w5_w6_promotion": has_anchor_2,
        },
        "predicate_e_hit_k3_advancement_preserved": predicate_e,
        "predicate_e_detail": {
            "has_hit_heading": has_hit_heading,
            "has_k_advancement_3_to_4": has_k_advancement,
            "has_mandatory_at_k3": has_mandatory_at_k3,
        },
        "predicate_f_substantive_line_count_ge_50": predicate_f,
        "substantive_line_count": substantive_line_count,
        "block_content_sha256": content_sha,
    }


# Section 7 -- DECIDE (verify-only PASS vs RETROFIT path)
def decide_phase(verify_results: dict[str, object]) -> dict[str, object]:
    """Decide between VERIFY-ONLY-PASS and RETROFIT phases.

    Returns the decision payload with the canonical
    ``retrofit_required`` boolean and the failing predicate list.
    """
    predicate_keys = [
        "predicate_a_block_present",
        "predicate_b_5anatomy_complete",
        "predicate_c_3level_ladder_complete",
        "predicate_d_s91_promotion_cite_both_anchors",
        "predicate_e_hit_k3_advancement_preserved",
        "predicate_f_substantive_line_count_ge_50",
    ]                                                                     # (local)
    failing = [k for k in predicate_keys if not verify_results.get(k)]    # (local)
    retrofit_required = bool(failing)                                     # (local)
    return {
        "retrofit_required": retrofit_required,
        "failing_predicates": failing,
        "all_predicates_pass": not retrofit_required,
    }


# Section 8 -- RETROFIT (single-shot AFTER-pattern)
S91_W5_W6_PROMOTION_SUBSECTION_HEADING = (
    "**S91 W5/W6 sub-class transition — REGISTRY-INCOMPLETE-PENDING-"
    "FIRST-EXTRACTION → STAGE-1-CANDIDATE promotion**"
)                                                                         # (local)


def build_anchor_2_citation_block() -> str:
    """Build the inline citation block for Anchor_2 that the registry
    is currently missing.

    This is appended to the existing S91 W5/W6 promotion sub-section in
    the canonical CF-64 RETRY block. The text is verbatim-stable so the
    SHA is reproducible on re-runs.
    """
    lines = [
        "",
        "**S91 W5/W6 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor-pair "
        "(S92 W5-3 VERIFY-FIRST-RETROFIT in-session retrofit, "
        "2026-05-23; mack-cosmic-bridge sole-writer per "
        "`feedback_mack-bridge-role.md`)**:",
        "",
        "Per `registry-landing.md §\"SOURCE-DOUBLE-CITE-CO-PRIMARY\"` "
        "the STAGE-1-CANDIDATE promotion citation MUST cite BOTH "
        "structural anchors at co-primary weight. Neither anchor "
        "alone fixes the STAGE-1-CANDIDATE status (Anchor_1 is the "
        "empirical first-extraction; Anchor_2 is the sub-class "
        "transition); both must be present in the registry citation "
        "block. CF-S91-W2-1 / CF-64 RETRY (the canonical content-host "
        "row above) cites Anchor_1 inline at the W5/W6 sub-class "
        "transition sub-section; the Anchor_2 inline citation is "
        "retrofit-appended here at S92 W5-3 VERIFY-FIRST-RETROFIT:",
        "",
        f"- **Anchor_1 (V_input, W6-1 PASS-A first-extraction)**: "
        f"audit_sha256=`{ANCHOR_1_W6_1_PASS_A_FULL}` "
        "(S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW at "
        "`computations/session-91/s91_gate_verdicts.txt:128`; "
        "tier_pin=TIER-2 POSITIVE-CALIBRATION compliance per "
        "`substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY "
        "level-pin discipline; F_2-axis FI sub-projection consensus "
        "α_b=2.6926 at L_max=22 sub-window). PRESENT inline above.",
        f"- **Anchor_2 (C_output, S91 W5/W6 in-session promotion)**: "
        f"audit_sha256=`{ANCHOR_2_S91_W5_W6_PROMOTION_FULL}` "
        "(CF-S91-W5-W6-IN-SESSION-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-"
        "PROMOTION-LANDING at "
        "`computations/session-91/s91_gate_verdicts.txt:270`; "
        "sub-class transition REGISTRY-INCOMPLETE-PENDING-"
        "FIRST-EXTRACTION → STAGE-1-CANDIDATE; "
        "scheme=in-session-fix-2026-05-22-mack-sole-writer; "
        "all_8_CF_spec_items_PASS). NEWLY CITED here per VERIFY-"
        "predicate (d) SOURCE-DOUBLE-CITE-CO-PRIMARY structure.",
        "",
        f"**STRUCTURE**: `{DOUBLE_CITE_TAG}` per "
        "`registry-landing.md §\"SOURCE-DOUBLE-CITE-CO-PRIMARY\"`. "
        "Sequential V_input → A_F → C_output → bridge-conclusion "
        "derivation chain: Anchor_1 supplies the first-extraction "
        "empirical anchor at L_max=22 sub-window via F_2-axis FI "
        "sub-projection consensus; Anchor_2 supplies the sub-class "
        "transition closing the deferred-pending state. Both anchors "
        "are on the same algebra-axis cell (Cell I; algebra-INVARIANT "
        "spectrum-only-functional × substrate-distance-1 pole `s=3`) "
        "per `registry-landing.md §\"Detection\"` criterion 4 "
        "(S88 W-15 V.6 MANDATORY at K=3). Neither anchor stands "
        "alone — together they fix the §VII.AU.OP-PROJ "
        "STAGE-1-CANDIDATE registry state uniquely.",
        "",
        "**Substrate framing**: the Anchor_2 inline citation IS the "
        "methodology-floor F-image (per `epistemic-discipline.md "
        "§\"Layer-Decomposition\"` Phi correspondence) of the "
        "substrate-IS sub-class transition event at the S91 W5/W6 "
        "close. Container-thinking is FORBIDDEN: the verdict line at "
        "s91_gate_verdicts.txt:270 IS NOT a 'description' of the "
        "substrate-IS sub-class transition; it IS the verdict-line "
        "F-image of that substrate-IS event. The substrate IS the "
        "Pillar I spectral triple at substrate-distance-1 pole `s=3`; "
        "Anchor_2 IS the methodology-floor image of the substrate's "
        "sub-class transition at the registry-text layer.",
        "",
        "**Audit pin**: S92 W5-3 VERIFY-FIRST-RETROFIT gate "
        f"`{GATE_ID}` (`computations/session-92/"
        "s92_w5_vii_au_op_proj_stage_1_candidate_landing_verify_first_"
        "retrofit.py`); Phase C single-shot AFTER-pattern Edit per "
        "`registry-landing.md §\"Bridge-Landing Script Architecture "
        "(single-shot pattern)\"`.",
        "",
    ]                                                                     # (local)
    return "\n".join(lines)


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Atomic file write with fsync (single-shot AFTER-pattern step 2).

    Writes ``text`` to a sibling tempfile then atomically renames over
    the target. The fsync after write guarantees the bytes are on disk
    before re-read.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")                          # (local)
    with tmp.open("w", encoding="utf-8", newline="") as fp:
        fp.write(text)
        fp.flush()
        try:
            import os
            os.fsync(fp.fileno())
        except (AttributeError, OSError):
            # Windows/non-POSIX may not always support fsync on text fp;
            # flush is sufficient since the next step re-reads the file.
            pass
    tmp.replace(path)


def retrofit_phase(
    registry_text: str,
    block_start: int,
    block_end: int,
    block_text: str,
) -> tuple[str, str, str]:
    """Single-shot AFTER-pattern RETROFIT.

    Build the retrofit text in memory; write atomically; re-read; verify
    the new block contains the Anchor_2 citation. Returns the tuple
    (new_block_text, new_block_content_sha, new_registry_content_sha).
    """
    # Build retrofit text (Step 1: build_promotion_text)
    anchor2_block = build_anchor_2_citation_block()                       # (local)

    # Insert the Anchor_2 citation block at the end of the canonical
    # CF-64 block, preserving every byte of pre-existing text.
    new_block_text = block_text.rstrip("\n") + "\n\n" + anchor2_block     # (local)

    # Splice into full registry text (Step 1 cont.)
    new_registry_text = (
        registry_text[:block_start]
        + new_block_text
        + registry_text[block_end:]
    )                                                                     # (local)

    # Step 2: write_atomic_with_fsync
    write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)

    # Step 3: re_read
    verify_registry_text = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)

    # Step 4: verify_section_matches -- locate block again and verify
    _, _, post_edit_block = locate_canonical_block(verify_registry_text)

    new_block_sha = sha256_of_text(post_edit_block)                       # (local)
    new_registry_sha = sha256_of_text(verify_registry_text)               # (local)

    return post_edit_block, new_block_sha, new_registry_sha


# Section 9 -- Main entrypoint
def main() -> int:
    t0 = time.time()                                                     # (local)
    print(f"=== {GATE_ID} ===")
    print(f"  scheme:     {SCHEME}")
    print(f"  convention: {CONVENTION}")
    print(f"  L_max:      {L_MAX}")
    print()

    # ---- Phase A: VERIFY ----
    print("--- Phase A: VERIFY ---")
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")             # (local)
    pre_registry_sha = sha256_of_text(registry_text)                      # (local)
    print(f"  pre-edit registry content_sha256: {pre_registry_sha[:16]}...")

    block_start, block_end, block_text = locate_canonical_block(
        registry_text
    )
    print(
        f"  canonical §VII.AU.OP-PROJ block at "
        f"bytes [{block_start}:{block_end}] "
        f"(len={block_end - block_start})"
    )
    verify_results = verify_predicates(block_text)
    pre_edit_block_sha = verify_results["block_content_sha256"]           # (local)
    print(f"  pre-edit block content_sha256:    {pre_edit_block_sha[:16]}...")
    print()
    for k, v in verify_results.items():
        if k.startswith("predicate_") and not k.endswith("_detail"):
            mark = "PASS" if v else "FAIL"
            print(f"  {k}: {mark}")
    print(f"  substantive_line_count: {verify_results['substantive_line_count']}")
    print()

    # ---- Phase B: DECIDE ----
    print("--- Phase B: DECIDE ---")
    decide = decide_phase(verify_results)
    retrofit_required = decide["retrofit_required"]                       # (local)
    print(f"  all_predicates_pass: {decide['all_predicates_pass']}")
    print(f"  failing_predicates:  {decide['failing_predicates']}")
    print(f"  retrofit_required:   {retrofit_required}")
    print()

    # ---- Phase C: RETROFIT (if needed) ----
    retrofit_payload: dict[str, object] = {}                              # (local)
    if retrofit_required:
        print("--- Phase C: RETROFIT (single-shot AFTER-pattern) ---")
        post_block_text, post_block_sha, post_registry_sha = retrofit_phase(
            registry_text, block_start, block_end, block_text
        )
        # Re-verify against post-edit block
        post_verify = verify_predicates(post_block_text)
        post_decide = decide_phase(post_verify)
        retrofit_payload = {
            "applied": True,
            "pre_edit_block_content_sha256": pre_edit_block_sha,
            "post_edit_block_content_sha256": post_block_sha,
            "pre_edit_registry_content_sha256": pre_registry_sha,
            "post_edit_registry_content_sha256": post_registry_sha,
            "post_edit_verify_results": post_verify,
            "post_edit_all_predicates_pass": post_decide[
                "all_predicates_pass"
            ],
            "post_edit_failing_predicates": post_decide[
                "failing_predicates"
            ],
        }
        print(f"  post-edit block content_sha256:    {post_block_sha[:16]}...")
        print(f"  post-edit registry content_sha256: {post_registry_sha[:16]}...")
        print(f"  post-edit all_predicates_pass:     "
              f"{post_decide['all_predicates_pass']}")
        if not post_decide["all_predicates_pass"]:
            print(
                f"  post-edit failing predicates: "
                f"{post_decide['failing_predicates']}"
            )
        print()
    else:
        retrofit_payload = {
            "applied": False,
            "reason": "VERIFY-ONLY-PASS — all 6 predicates already hold",
        }
        print("--- Phase C: RETROFIT (SKIPPED — VERIFY-ONLY-PASS) ---")
        print()

    # ---- Determine final verdict ----
    if not retrofit_required:
        verdict = "PASS"                                                 # (local)
        value = (
            f"'VERIFY-ONLY-PASS_landing_already_landed_S91_W5_W6_"
            f"audit_sha={ANCHOR_2_SHORT}'"
        )                                                                # (local)
        decide_outcome = "VERIFY-ONLY-PASS"                              # (local)
    else:
        post_decide_pass = bool(retrofit_payload.get(
            "post_edit_all_predicates_pass"
        ))                                                               # (local)
        if post_decide_pass:
            verdict = "PASS"
            value = (
                f"'RETROFIT-PASS_landing_anchor2_citation_appended_"
                f"single_shot_after_pattern_anchor1_short={ANCHOR_1_SHORT}_"
                f"anchor2_short={ANCHOR_2_SHORT}'"
            )                                                            # (local)
            decide_outcome = "RETROFIT-PASS"
        else:
            verdict = "FAIL"
            value = (
                f"'RETROFIT-FAIL_post_edit_predicates_still_fail_"
                f"failing={','.join(retrofit_payload['post_edit_failing_predicates'])}'"
            )                                                            # (local)
            decide_outcome = "RETROFIT-FAIL"

    # ---- Compute dual SHA-256 (audit + content) ----
    script_path = Path(__file__).resolve()                               # (local)
    content_sha = sha256_of_file(script_path)                            # (local)

    input_pin_map = {                                                    # (local)
        "script_content_sha256": content_sha,
        "registry_path": str(
            REGISTRY_PATH.relative_to(PROJECT_ROOT).as_posix()
        ),
        "registry_pre_edit_sha256": pre_registry_sha,
        "registry_post_edit_sha256": (
            retrofit_payload.get("post_edit_registry_content_sha256")
            if retrofit_required
            else pre_registry_sha
        ),
        "block_pre_edit_sha256": pre_edit_block_sha,
        "block_post_edit_sha256": (
            retrofit_payload.get("post_edit_block_content_sha256")
            if retrofit_required
            else pre_edit_block_sha
        ),
        "cross_pillar_bridge_anatomy_rule_sha256": sha256_of_file(
            RULE_CROSS_PILLAR_BRIDGE_ANATOMY
        ),
        "joint_theorem_promotion_rule_sha256": sha256_of_file(
            RULE_JOINT_THEOREM_PROMOTION
        ),
        "registry_landing_rule_sha256": sha256_of_file(
            RULE_REGISTRY_LANDING
        ),
        "s91_verdict_file_sha256": sha256_of_file(S91_VERDICT_PATH),
        "canonical_constants_sha256": sha256_of_file(
            CANONICAL_CONSTANTS_PATH
        ),
        "anchor_1_w6_1_pass_a_full": ANCHOR_1_W6_1_PASS_A_FULL,
        "anchor_2_s91_w5_w6_promotion_full": (
            ANCHOR_2_S91_W5_W6_PROMOTION_FULL
        ),
        "verdict": verdict,
        "decide_outcome": decide_outcome,
        "retrofit_applied": str(retrofit_required),
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
    }
    audit_sha = closure_hash(input_pin_map)                              # (local)

    print(f"--- audit_sha256:   {audit_sha[:16]}... ---")
    print(f"--- content_sha256: {content_sha[:16]}... ---")
    print()

    # ---- Emit ONE canonical verdict line + dual-SHA companion ----
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )                                                                    # (local)
    comment = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )                                                                    # (local)

    # Plan §W5-3 explicitly: `schema_v2_3tuple_required: false` (no
    # SIGN/MAGNITUDE/REGIME companion row required for the [VERIFY]
    # trigger of this gate).

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)

    # ---- Write JSON sidecar ----
    sidecar = {                                                          # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
        "phase_a_verify": verify_results,
        "phase_b_decide": decide,
        "phase_c_retrofit": retrofit_payload,
        "decide_outcome": decide_outcome,
        "input_pin_map": input_pin_map,
        "anchor_1_w6_1_pass_a_full": ANCHOR_1_W6_1_PASS_A_FULL,
        "anchor_2_s91_w5_w6_promotion_full": (
            ANCHOR_2_S91_W5_W6_PROMOTION_FULL
        ),
        "SOURCE_DOUBLE_CITE_CO_PRIMARY": DOUBLE_CITE_TAG,
        "elapsed_seconds": round(time.time() - t0, 3),
    }
    DATA_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  JSON sidecar -> {DATA_JSON.name}")
    print(f"  verdict line -> {VERDICT_TXT.name}")
    print()
    print(f"=== {GATE_ID}: {verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
