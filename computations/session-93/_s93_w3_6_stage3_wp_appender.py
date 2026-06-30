#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the §VII.AV.STATE-PROJ STAGE-3-PERMANENT flip note + ordinal-collision CF
to the §W3-6 aggregation-result subsection. Atomic os.replace; idempotent; keyed on
a unique anchor inserted AFTER the existing 'Verdict-line provenance' line. One-shot
helper for the S93 W3 close Stage-3 promotion."""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
WP = PROJECT_ROOT / "sessions" / "session-93" / "session-93-w3-workingpaper.md"  # (local)
ANCHOR_AFTER = (  # (local) the last line of the existing aggregation subsection
    "convention ends `-FULL`, L_max=12."
)
NEW_ANCHOR = "**§VII.AV.STATE-PROJ STAGE-3-PERMANENT promotion (S93 W3 close)**"  # (local)

NOTE = r"""

**§VII.AV.STATE-PROJ STAGE-3-PERMANENT promotion (S93 W3 close)**: per `joint-theorem-promotion.md §"Stage 3 — Permanent Registration"`, the clean Stage-2 PASS-AND (W3-6, audit_sha256=`610d1ac85b5a2ef0ede76f376c2873992acf1e66b9e49c0f7ee6bc0c8307050b`) triggered the orchestrator session-synthesis tag-flip **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** for §VII.AV.STATE-PROJ ONLY (gate `S93-W3-VII-AV-STATE-PROJ-STAGE-3-PERMANENT-PROMOTION` PASS, `s93_gate_verdicts.txt:62`; single-shot AFTER pattern, `s93_w3_6_vii_av_state_proj_stage_3_promotion.py`). Flipped at all three markers: index-table row (~151), section header (18499), `**Status**:` line (18501) — Stage-1/Stage-2 history preserved as provenance per the §VII.AH / Var_a / §VII.AU.OP-PROJ precedent. `_vii_slot_allocation_audit.py` re-run = **PASS** (F_STALE_STATUS=0; STATE-PROJ STAGE-3-PERMANENT consistent across index + header + Status). The W3-6 verdict line (line 58, INFO) stands UNCHANGED (this is a session-synthesis tag-flip on the already-landed Stage-2 PASS, NOT a new gate; the Stage-3 record line at line 62 is a separate NEW gate-ID, not a W3-6 supersession). **§VII.AV.OP-PROJ STAYS STAGE-1-CANDIDATE** (Cell-II, untouched; pending CF-S94 Axis-A re-verify on the corrected entry).

**Ordinal honesty (NOT asserted)**: the orchestrator adjudication assumed §VII.AV.STATE-PROJ would be the FOURTH cross-axis joint theorem at STAGE-3-PERMANENT (prior three: §VII.AH, §VII.U.2 Var_a, §VII.AU.OP-PROJ). Registry verification BEFORE asserting the ordinal surfaced a **pre-existing bookkeeping collision**: BOTH §VII.AU.OP-PROJ (`permanent-results-registry.md:18908`/`:19297`) AND §VII.AW.OP-PROJ (`:18374`) claim "THIRD framework cross-axis joint theorem to reach STAGE-3-PERMANENT." The fully-promoted (Status == STAGE-3-PERMANENT, not -eligible) set prior to STATE-PROJ is {§VII.AH (FIRST, S90 W2 CF-20), §VII.U.2 Corner-II Var_a (SECOND, S92 W4-7), §VII.AU.OP-PROJ (S93 W2-2), §VII.AW.OP-PROJ} — so STATE-PROJ is at least the FIFTH, but the precise integer is contested by the AU/AW #3 tie. Per `feedback_fix-in-session-never-defer.md` (this is a hygiene observation on OTHER already-landed entries, OUT OF SCOPE for a STATE-PROJ-only flip) the STATE-PROJ promotion records membership in the STAGE-3-PERMANENT set WITHOUT asserting a contested integer, and the AU/AW collision is flagged as a carry-forward rather than silently expanded-scope-fixed.

**Carry-Forward Computations** (additional, from the Stage-3 promotion):

- **CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW**
  1. **What**: resolve the pre-existing STAGE-3-PERMANENT ordinal collision — both §VII.AU.OP-PROJ and §VII.AW.OP-PROJ are tagged "THIRD framework cross-axis joint theorem to reach STAGE-3-PERMANENT." Determine the correct chronological ordering by STAGE-3-promotion date (§VII.AU.OP-PROJ STAGE-3 at S93 W2-2; §VII.AW.OP-PROJ STAGE-3 at 2026-05-24 per its Status line — verify which landed first), re-number the contested "#3" entries, and re-number any downstream ordinal claims (§VII.AZ.OP-PROJ "SECOND-eligible", and STATE-PROJ's own membership note) to a single consistent sequence.
  2. **Inputs**: `permanent-results-registry.md` STAGE-3-PERMANENT entries (§VII.AH, §VII.U.2 Var_a, §VII.AU.OP-PROJ, §VII.AW.OP-PROJ, §VII.AV.STATE-PROJ) + their STAGE-3-promotion dates/verdict SHAs; the S90/S92/S93 verdict files for promotion-event timestamps.
  3. **Gate**: each STAGE-3-PERMANENT cross-axis joint theorem carries a UNIQUE ordinal consistent with promotion chronology; `_vii_slot_allocation_audit.py` PASS; no two entries claim the same integer.
  4. **Effort**: ~0.3 wave-equivalents (registry-text ordinal reconciliation, mack sole-writer; bookkeeping, no new compute).
  Depends on: this S93 W3 STATE-PROJ promotion (LANDED) + the §VII.AU.OP-PROJ / §VII.AW.OP-PROJ STAGE-3 promotions (prior sessions; LANDED).
"""


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    if NEW_ANCHOR in text:
        print("IDEMPOTENT: STAGE-3 flip note already present; no re-insertion.")
        return 0
    if ANCHOR_AFTER not in text:
        raise SystemExit(f"FATAL: anchor not found: {ANCHOR_AFTER!r}")
    if text.count(ANCHOR_AFTER) != 1:
        raise SystemExit(f"FATAL: anchor not unique ({text.count(ANCHOR_AFTER)} sites).")
    insert_at = text.index(ANCHOR_AFTER) + len(ANCHOR_AFTER)  # (local)
    new_text = text[:insert_at] + NOTE + text[insert_at:]  # (local)
    tmp = WP.with_name(WP.name + ".tmp_s3note")  # (local)
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(tmp, WP)
    print("WROTE STAGE-3 flip note + ordinal-collision CF into §W3-6 aggregation subsection.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
