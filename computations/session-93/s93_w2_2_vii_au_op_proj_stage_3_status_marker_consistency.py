#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W2-2 STAGE-3-PERMANENT status-marker CONSISTENCY completion
===============================================================

CONSISTENCY completion of the S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION
landing (the W2-2 PASS verdict at `s93_gate_verdicts.txt:31`,
audit_sha256=ca2eda5f..., STAYS — this script emits NO new verdict line).

The STAGE-3-PERMANENT promotion BLOCK appended by the W2-2 gate
(`permanent-results-registry.md` line ~19119, before §VII.AX) is correct and
stays. BUT the canonical *current-status* markers that downstream consumers read
still said STAGE-1-CANDIDATE — inconsistent with the block. This script flips
those status markers to LEAD with STAGE-3-PERMANENT (S93 W2-2), matching the
§VII.AH precedent (index row line 104 + `**Status**:` line ~15784 LEAD with
STAGE-3-PERMANENT while PRESERVING the LANDED / Stage-2 / STAGE-3-promotion
history as provenance) and Var_a (§VII.U.2 Corner II).

Flipped markers (all §VII.AU.OP-PROJ; lookalikes §VII.AAU / §VII.AV / §VII.AW
NOT touched):
  1. INDEX ROW (line 144) — current-status leads STAGE-3-PERMANENT; author/date
     columns filled (mack-cosmic-bridge | 2026-05-24), matching §VII.AH.
  2. SECTION HEADER (line ~18061; W7c emission #2 host).
  3. SECTION HEADER (line ~18617; S90 W8-5 landing-confirmation sub-row).
  4. SECTION HEADER (line ~18728; CF-64 RETRY canonical content-host).
  5. **Status**: line ~18621 (the landing-confirmation sub-row).
  6. **Status**: line ~18732 (the CF-64 RETRY canonical content-host).

PRESERVED in every flip:
  - CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class annotation (the asymptotic
    α=-3 deferral to CF-S94-W5-3 is NOT discharged).
  - LANDED-S89-W7c / S90-W1-15 / S91-W5-W6 STAGE-1 / Stage-2 PASS (S92 §W5-4 +
    §W5-5) history as provenance (per §VII.AH "STAGE-1 LANDED ...; Stage-2 PASS
    ...; STAGE-3 promotion ..." pattern).

Single-shot AFTER pattern per `registry-landing.md §"Bridge-Landing Script
Architecture"`: build ALL replacements in memory -> write_atomic_with_fsync ->
re_read + verify (every target reads STAGE-3-PERMANENT; no residual STAGE-1
CURRENT-status marker for §VII.AU.OP-PROJ). NO conditional rewrite. mack sole
registry writer per `feedback_mack-bridge-role.md`. These are registry PROSE
edits (markdown), NOT verdict-file edits; PROHIBITED_ACTIONS Class 3 governs
verdict pass_threshold/pass_band, not registry markdown status prose.

This script is idempotent (each old->new replacement no-ops if the new text is
already present). It emits NO verdict line (the W2-2 verdict stands); it writes a
small JSON sidecar recording the flips + the post-edit consistency booleans.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import json
import re
import sys
from pathlib import Path

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import M_KK, tau_fold  # noqa: F401, E402

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
JSON_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w2_2_vii_au_op_proj_stage_3_status_marker_consistency.json"
)

# Stage-2 chain (full-64-hex; for the index-row + Status provenance text).
W5_4_SHA = "4a95a2769a6ed8f4d439b62c3c80d0f63f43dae2d9a7c8bd2a83994f6939bf64"  # (local)
W5_5_SHA = "64d45d718648f560cb9a209d9d5f91a849d7d5221a7d1ef0c08fe90a68939c4f"  # (local)


# ---------------------------------------------------------------------------
# Step (1) — build the exact old->new replacements (pure; verbatim strings)
# ---------------------------------------------------------------------------
def build_replacements() -> list[tuple[str, str]]:
    """Return (old, new) verbatim string pairs. Each `old` MUST be unique in the
    registry; each `new` LEADS with STAGE-3-PERMANENT (S93 W2-2) while preserving
    the landing/Stage history + CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class,
    per the §VII.AH precedent.
    """
    reps: list[tuple[str, str]] = []  # (local)

    # --- (1) INDEX ROW (line 144) ---
    # Old current-status leads STAGE-1-CANDIDATE; author/date are (unknown)/(undated).
    old_index = (
        "| §VII.AU.OP-PROJ | THM | FWD-C1 Pillar I↔II Bridge Theorem Candidate "
        "(W7c REGISTRY-1; STAGE-1-CANDIDATE per joint-theorem-promotion.md "
        "4-stage pathway; LANDED S89 W7c; S90 W1-15 defe... | (unknown) | (undated) |"
    )
    new_index = (
        "| §VII.AU.OP-PROJ | THM | FWD-C1 Pillar I↔II Bridge Theorem (W7c REGISTRY-1; "
        f"STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway; Stage-2 PASS-AND "
        f"S92 §W5-4 audit_sha256={W5_4_SHA} ∧ §W5-5 audit_sha256={W5_5_SHA}; STAGE-3 promotion "
        "S93 W2-2; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class — asymptotic α=-3 deferred "
        "CF-S94-W5-3; LANDED S89 W7c → STAGE-1 S91 W5/W6) | mack-cosmic-bridge | 2026-05-24 |"
    )
    reps.append((old_index, new_index))

    # --- (2) SECTION HEADER line ~18061 (W7c emission #2 host) ---
    # The header text alone is NOT unique (the SAME string appears at line ~18623
    # as a backtick-wrapped `**Cross-reference to canonical row**` quotation that
    # must NOT be flipped). Disambiguate by anchoring the old-string with the
    # line-18061 trailing context (the blank line + the CF-18 provenance line that
    # follows ONLY the real header, not the mid-sentence quote).
    old_h1 = (
        "### §VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate "
        "(W7c REGISTRY-1; STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage "
        "pathway; LANDED S89 W7c; S90 W1-15 deferred-pending re-tag "
        "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION)\n\n"
        "**Provenance annotation (CF-18)**"
    )
    new_h1 = (
        "### §VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem "
        "(W7c REGISTRY-1; STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage "
        "pathway — STAGE-3 promotion S93 W2-2 on Stage-2 PASS-AND S92 §W5-4 ∧ §W5-5; "
        "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class; "
        "LANDED S89 W7c; S90 W1-15 deferred-pending re-tag "
        "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1 S91 W5/W6 → STAGE-3 S93 W2-2)\n\n"
        "**Provenance annotation (CF-18)**"
    )
    reps.append((old_h1, new_h1))

    # --- (3) SECTION HEADER line ~18617 (S90 W8-5 landing-confirmation sub-row) ---
    old_h2 = (
        "### §VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; "
        "HIT-PASS-CANDIDATE-PENDING-EXTRACTION — S90 W8-5 deferred-pending "
        "landing-confirmation; mack-cosmic-bridge sole-writer per "
        "`feedback_mack-bridge-role.md`, 2026-05-15)"
    )
    new_h2 = (
        "### §VII.AU.OP-PROJ (STAGE-3-PERMANENT per joint-theorem-promotion.md — "
        "STAGE-3 promotion S93 W2-2 on Stage-2 PASS-AND S92 §W5-4 ∧ §W5-5; historical: "
        "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION / HIT-PASS-CANDIDATE-PENDING-EXTRACTION "
        "S90 W8-5 deferred-pending landing-confirmation; mack-cosmic-bridge sole-writer per "
        "`feedback_mack-bridge-role.md`, 2026-05-15)"
    )
    reps.append((old_h2, new_h2))

    # --- (4) SECTION HEADER line ~18728 (CF-64 RETRY canonical content-host) ---
    old_h3 = (
        "### §VII.AU.OP-PROJ (CF-64 RETRY — S90 W8-6 single-shot AFTER-pattern "
        "canonical content-host row; STAGE-1-CANDIDATE per joint-theorem-promotion.md "
        '§"Stage 1"; HIT K-counter calibration corpus instance #4)'
    )
    new_h3 = (
        "### §VII.AU.OP-PROJ (CF-64 RETRY — S90 W8-6 single-shot AFTER-pattern "
        "canonical content-host row; STAGE-3-PERMANENT per joint-theorem-promotion.md "
        '§"Stage 3" — STAGE-3 promotion S93 W2-2 on Stage-2 PASS-AND S92 §W5-4 ∧ §W5-5; '
        "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class; STAGE-1 host S90 W8-6 → STAGE-1 "
        'S91 W5/W6 → STAGE-3 S93 W2-2; HIT K-counter calibration corpus instance #4)'
    )
    reps.append((old_h3, new_h3))

    # --- (5) **Status**: line ~18621 (landing-confirmation sub-row) ---
    # NOTE: the line starts at column 0 with `**Status**:` (NO leading space) —
    # verbatim per the awk byte-dump of line 18621.
    old_s1 = (
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage pathway WITH deferred-pending intermediate verdict-class sub-class tag "
        "`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` AND HIT-PASS-CANDIDATE-PENDING-EXTRACTION "
        "qualifier"
    )
    new_s1 = (
        "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage upgrade pathway — STAGE-1 LANDED S89 W7c (re-tagged S90 W1-15 "
        "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; STAGE-1-CANDIDATE promotion S91 W5/W6); "
        f"Stage-2 PASS-AND S92 §W5-4 (audit_sha256={W5_4_SHA}) ∧ §W5-5 (audit_sha256={W5_5_SHA}); "
        "STAGE-3 promotion S93 W2-2. CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class PRESERVED "
        "(asymptotic α=-3 deferred to CF-S94-W5-3). Historical sub-class tag at this sub-row: "
        "`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` AND HIT-PASS-CANDIDATE-PENDING-EXTRACTION "
        "qualifier"
    )
    reps.append((old_s1, new_s1))

    # --- (6) **Status**: line ~18732 (CF-64 RETRY canonical content-host) ---
    # NOTE: the line starts at column 0 with `**Status**:` (NO leading space) —
    # verbatim per the awk byte-dump of line 18732.
    old_s2 = (
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage pathway. The Level-1 single-τ-slice substrate-IS structural identity "
        "`n_s_FW² − 1 ≡ α_s_canonical` in Q at substrate-distance-1 pole `s=3` is STRUCTURAL "
        "THEOREM (W7a Sage-QQ exact rational; regulator-invariant, L-independent)."
    )
    new_s2 = (
        "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage upgrade pathway — STAGE-1 LANDED S89 W7c (CF-64 RETRY canonical content-host "
        f"S90 W8-6; STAGE-1-CANDIDATE promotion S91 W5/W6); Stage-2 PASS-AND S92 §W5-4 "
        f"(audit_sha256={W5_4_SHA}) ∧ §W5-5 (audit_sha256={W5_5_SHA}); STAGE-3 promotion S93 W2-2 "
        "(THIRD framework cross-axis joint theorem to reach STAGE-3-PERMANENT, after §VII.AH and "
        "§VII.U.2 Corner II Var_a). CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class PRESERVED "
        "(asymptotic α=-3 deferred to CF-S94-W5-3). The Level-1 single-τ-slice substrate-IS "
        "structural identity `n_s_FW² − 1 ≡ α_s_canonical` in Q at substrate-distance-1 pole `s=3` "
        "is STRUCTURAL THEOREM (W7a Sage-QQ exact rational; regulator-invariant, L-independent)."
    )
    reps.append((old_s2, new_s2))

    # --- (7) line ~18623 cross-reference QUOTE annotation ---
    # The S90 W8-5 sub-row body quotes the (then-canonical) §VII.AU.OP-PROJ header
    # verbatim — a HISTORICAL backtick-wrapped quote, NOT a current-status marker.
    # We preserve the quote verbatim and append a clarifying suffix so a naive
    # `§VII.AU.OP-PROJ.*STAGE-1-CANDIDATE` grep cannot mistake it for a current
    # status. (The quote's "registry line 17642" pointer is itself a stale S90
    # internal reference; the live status is the STAGE-3-PERMANENT flip above.)
    old_xref = (
        "for the substantive theorem statement, IS-not-IN anatomy, three-level "
        "ladder, Hybrid Independence Test, and calibration corpus position. This "
        "S90 W8-5 row carries the explicit HIT-PASS-CANDIDATE-PENDING-EXTRACTION "
        "qualifier in the header and the per-plan §W8-5 5-anatomy + 3-level "
        "deferred-pending audit-trail closure."
    )
    new_xref = (
        "for the substantive theorem statement, IS-not-IN anatomy, three-level "
        "ladder, Hybrid Independence Test, and calibration corpus position. This "
        "S90 W8-5 row carries the explicit HIT-PASS-CANDIDATE-PENDING-EXTRACTION "
        "qualifier in the header and the per-plan §W8-5 5-anatomy + 3-level "
        "deferred-pending audit-trail closure. **[HISTORICAL QUOTE — the quoted "
        "STAGE-1-CANDIDATE header text above is the S89/S90 status snapshot; the "
        "CURRENT §VII.AU.OP-PROJ status is STAGE-3-PERMANENT per the S93 W2-2 "
        "STAGE-3 promotion (Stage-2 PASS-AND S92 §W5-4 ∧ §W5-5); the quote is "
        "preserved as provenance, NOT a current-status marker.]**"
    )
    reps.append((old_xref, new_xref))

    return reps


def apply_replacements(text: str, reps: list[tuple[str, str]]) -> tuple[str, list[dict]]:
    """Apply each (old, new) replacement. old MUST be unique (exactly 1 match) OR
    already-resolved (0 old matches AND new present = idempotent no-op). Pure.
    """
    log: list[dict] = []  # (local)
    out = text  # (local)
    for i, (old, new) in enumerate(reps):
        n_old = out.count(old)  # (local)
        n_new_pre = out.count(new)  # (local)
        if n_old == 1:
            out = out.replace(old, new, 1)
            status = "REPLACED"  # (local)
        elif n_old == 0 and n_new_pre >= 1:
            status = "IDEMPOTENT_ALREADY_NEW"  # (local)
        elif n_old == 0 and n_new_pre == 0:
            status = "ERROR_OLD_NOT_FOUND_NEW_ABSENT"  # (local)
        else:
            status = f"ERROR_OLD_NOT_UNIQUE_count={n_old}"  # (local)
        log.append(
            {
                "rep_index": i,
                "status": status,
                "old_count": n_old,
                "new_count_pre": n_new_pre,
                "old_head": old[:70],
                "new_head": new[:70],
            }
        )
    return out, log


def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


def main() -> int:
    print("=== S93-W2-2 STAGE-3-PERMANENT status-marker CONSISTENCY completion ===")
    reps = build_replacements()  # (local) Step (1)
    original = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    new_text, log = apply_replacements(original, reps)  # (local)
    print("Replacement log:")
    errors = []  # (local)
    for entry in log:
        print(
            f"  rep[{entry['rep_index']}] {entry['status']} "
            f"(old_count={entry['old_count']}, new_count_pre={entry['new_count_pre']}) "
            f"old_head={entry['old_head']!r}"
        )
        if entry["status"].startswith("ERROR"):
            errors.append(entry)

    if errors:
        print(f"ABORT: {len(errors)} replacement(s) failed (old not found / not unique).")
        print("No write performed. Inspect the registry; the old strings must match verbatim.")
        _write_json(log=log, wrote=False, consistency={}, errors=errors)
        return 1  # script breakage (verbatim-match failure) — exit != 0 per math-scripts.md

    # Step (2) write atomically (only if something actually changed)
    if new_text != original:
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print("  registry written (atomic + fsync).")
    else:
        print("  no change needed (all replacements idempotent / already-new).")

    # Step (3) re-read + verify: every §VII.AU.OP-PROJ current-status marker reads
    # STAGE-3-PERMANENT; no residual STAGE-1-CANDIDATE *current-status* for the slot.
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    consistency = verify_consistency(actual)  # (local)
    print("Consistency verification:")
    for k, v in consistency.items():
        print(f"  {k} = {v}")

    all_consistent = (  # (local)
        consistency["index_row_stage3"]
        and consistency["header_18061_stage3"]
        and consistency["header_18617_stage3"]
        and consistency["header_18728_stage3"]
        and consistency["status_landing_conf_stage3"]
        and consistency["status_cf64_stage3"]
        and consistency["promo_block_stage3"]
        and consistency["sub_class_preserved"]
        and consistency["no_residual_stage1_current_status"]
    )
    print(f"ALL_CONSISTENT = {all_consistent}")

    _write_json(log=log, wrote=(new_text != original), consistency=consistency, errors=[])
    # NO new verdict line — the W2-2 verdict (s93_gate_verdicts.txt:31 PASS) stands.
    # exit 0 if consistent; 1 if a residual marker remains (script-health signal).
    return 0 if all_consistent else 1


def verify_consistency(text: str) -> dict:
    """Verify every §VII.AU.OP-PROJ current-status marker reads STAGE-3-PERMANENT.

    Index row, the three section headers, the two flipped Status lines, and the
    promotion block all carry STAGE-3-PERMANENT for §VII.AU.OP-PROJ; the
    CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class is preserved; and no residual
    STAGE-1-CANDIDATE *current-status* marker remains for §VII.AU.OP-PROJ (a
    STAGE-1 *LANDED* provenance string is fine).
    """
    # index row (line 144): the §VII.AU.OP-PROJ table row leads STAGE-3-PERMANENT.
    index_row_stage3 = bool(  # (local)
        re.search(
            r"\| §VII\.AU\.OP-PROJ \| THM \| FWD-C1 Pillar I↔II Bridge Theorem "
            r"\(W7c REGISTRY-1; STAGE-3-PERMANENT",
            text,
        )
    )
    header_18061_stage3 = (  # (local)
        "### §VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem "
        "(W7c REGISTRY-1; STAGE-3-PERMANENT" in text
    )
    header_18617_stage3 = (  # (local)
        "### §VII.AU.OP-PROJ (STAGE-3-PERMANENT per joint-theorem-promotion.md — "
        "STAGE-3 promotion S93 W2-2" in text
    )
    header_18728_stage3 = (  # (local)
        "### §VII.AU.OP-PROJ (CF-64 RETRY — S90 W8-6 single-shot AFTER-pattern "
        "canonical content-host row; STAGE-3-PERMANENT" in text
    )
    status_landing_conf_stage3 = (  # (local) column-0 line-start; NO leading space
        "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage upgrade pathway — STAGE-1 LANDED S89 W7c (re-tagged S90 W1-15" in text
    )
    status_cf64_stage3 = (  # (local) column-0 line-start; NO leading space
        "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage upgrade pathway — STAGE-1 LANDED S89 W7c (CF-64 RETRY canonical content-host"
        in text
    )
    promo_block_stage3 = (  # (local) the W2-2-appended promotion block
        "**S93 W2-2 STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion" in text
        and "advances **STAGE-1-CANDIDATE → STAGE-3-PERMANENT**" in text
    )
    sub_class_preserved = "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED" in text  # (local)

    # No residual STAGE-1-CANDIDATE *current-status* marker for §VII.AU.OP-PROJ.
    # A status marker is a header or "**Status**:" line. We scan the three header
    # forms + the two status-line lead-ins; none may still read STAGE-1-CANDIDATE
    # as the CURRENT status. (STAGE-1 LANDED / STAGE-1 S91 W5/W6 provenance is OK.)
    residual_patterns = [  # (local)
        # the OLD index row (STAGE-1 lead) must be gone
        "| §VII.AU.OP-PROJ | THM | FWD-C1 Pillar I↔II Bridge Theorem Candidate "
        "(W7c REGISTRY-1; STAGE-1-CANDIDATE per joint-theorem-promotion.md",
        # the OLD CF-64 RETRY header (STAGE-1 lead) must be gone
        "### §VII.AU.OP-PROJ (CF-64 RETRY — S90 W8-6 single-shot AFTER-pattern "
        "canonical content-host row; STAGE-1-CANDIDATE per joint-theorem-promotion.md",
        # the OLD landing-confirmation header (STAGE-1-bearing form) must be gone
        "### §VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; "
        "HIT-PASS-CANDIDATE-PENDING-EXTRACTION — S90 W8-5",
        # the OLD CF-64 Status lead (STAGE-1-CANDIDATE current) must be gone
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage pathway. The Level-1 single-τ-slice substrate-IS structural identity "
        "`n_s_FW² − 1 ≡ α_s_canonical`",
        # the OLD landing-confirmation Status lead (STAGE-1-CANDIDATE current) must be gone
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` "
        "4-stage pathway WITH deferred-pending intermediate verdict-class sub-class tag "
        "`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` AND HIT-PASS-CANDIDATE-PENDING-EXTRACTION",
    ]
    residuals = [p[:60] for p in residual_patterns if p in text]  # (local)
    # The line-~18623 backtick-wrapped HISTORICAL QUOTE of the (then-canonical)
    # §VII.AU.OP-PROJ header is preserved-as-provenance and explicitly annotated
    # `[HISTORICAL QUOTE — ... CURRENT ... STAGE-3-PERMANENT ...]`; it is NOT a
    # current-status marker. Require that annotation to be present (so a naive
    # grep cannot mistake the quote for a live STAGE-1-CANDIDATE status).
    xref_quote_annotated = (  # (local)
        "[HISTORICAL QUOTE — the quoted STAGE-1-CANDIDATE header text above is the "
        "S89/S90 status snapshot; the CURRENT §VII.AU.OP-PROJ status is "
        "STAGE-3-PERMANENT per the S93 W2-2 STAGE-3 promotion" in text
    )
    no_residual = (len(residuals) == 0) and xref_quote_annotated  # (local)

    return {
        "index_row_stage3": index_row_stage3,
        "header_18061_stage3": header_18061_stage3,
        "header_18617_stage3": header_18617_stage3,
        "header_18728_stage3": header_18728_stage3,
        "status_landing_conf_stage3": status_landing_conf_stage3,
        "status_cf64_stage3": status_cf64_stage3,
        "promo_block_stage3": promo_block_stage3,
        "sub_class_preserved": sub_class_preserved,
        "no_residual_stage1_current_status": no_residual,
        "residual_heads": residuals,
    }


def _write_json(*, log, wrote, consistency, errors) -> None:
    record = {  # (local)
        "gate_id": "S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION",
        "task": "status-marker-consistency-completion",
        "emits_new_verdict_line": False,
        "w2_2_verdict_stands": "s93_gate_verdicts.txt:31 PASS audit_sha256=ca2eda5fcec2d1c7614ec0884e42e4a16b52c1af29911c70db3743f2a6048c3b",
        "registry_written": wrote,
        "replacement_log": log,
        "consistency": consistency,
        "errors": errors,
        "preserved": [
            "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class (asymptotic alpha=-3 deferred CF-S94-W5-3)",
            "LANDED-S89-W7c / S90-W1-15 / S91-W5-W6 STAGE-1 + Stage-2 PASS history as provenance",
        ],
        "precedent": "§VII.AH index row line 104 + Status line ~15784 (lead STAGE-3-PERMANENT, preserve Stage history); Var_a §VII.U.2 Corner II",
    }
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {JSON_PATH}")


if __name__ == "__main__":
    sys.exit(main())
