#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atomic read-modify-write of the §W3-6 WP aggregation-result subsection.

Idempotent; keyed on a unique anchor; inserts AFTER the Axis-B subsection and
BEFORE the §W3-7 section delimiter. Per `epistemic-discipline.md §"Registry-Write
Hygiene"`: atomic os.replace, not Edit-tool round-trip. One-shot helper for the
W3-6 aggregation/emission step.
"""
import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
WP = PROJECT_ROOT / "sessions" / "session-93" / "session-93-w3-workingpaper.md"  # (local)
HEADER = "### §W3-6. S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"  # (local)
AGG_ANCHOR = "#### Aggregation result (composite Stage-2 verdict + corner-cell remediation)"  # (local)

SUBSECTION = r"""
#### Aggregation result (composite Stage-2 verdict + corner-cell remediation)

**Status**: COMPLETED.
**Composite Verdict**: **INFO** (W3-6 = `S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT`; emitted with Option-A `supersedes` + convention ending `-FULL`).
**Output Artifacts**: producing/aggregation script `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py`; aggregation sidecar `s93_w3_6_vii_av_stage_2_cross_axis_verify.json`; corner-cell remediation script `s93_w3_6_vii_av_op_proj_cell_ii_remediation.py`; both axis verdict JSONs (`s93_w3_6_axis_a_vdd_verdicts.json` + `s93_w3_6_axis_b_mack_verdicts.json`).
**MCP Pre-Compute Audit**: see the Axis-B subsection above (search_knowledge / trace_entity / get_constant queries on §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ; NOT PRE-CLOSED — Stage-2 verify of STAGE-1-CANDIDATE sub-slots is a new gate).

**Per-sub-slot Axis-A / Axis-B PASS-AND breakdown** (orchestrator-objective adjudication, S93 W3-6):

| Sub-slot | Corner cell | Axis-A (vdd) | Axis-B (mack) | JOINT PASS-AND | Sub-slot outcome | Stage-3 status |
|:---------|:-----------|:-------------|:--------------|:---------------|:-----------------|:---------------|
| **§VII.AV.STATE-PROJ** | Cell IV (DEPENDENT × s=4) | PASS | PASS | PASS (bridge-map + ortho) | **clean Stage-2 PASS-AND** | **STAGE-3-ELIGIBLE** |
| **§VII.AV.OP-PROJ** | Cell II (INVARIANT × s=4) [CORRECTED] | FAIL (corner-cell only, as-registered Cell I) | PASS | PASS (bridge-map + ortho) | corner-cell-defect caught + remediated | **STAGE-1-CANDIDATE-PENDING-S94-REVERIFY** |

**Corner-cell catch + remediation narrative** (the Stage-2 verify's PURPOSE — it caught a real classification defect): vdd's Axis-A OP-PROJ `corner_cell_classification` clause FAILed on the as-registered entry, which carried **Cell I**. This FAIL is objectively correct: §VII.U.2's 4-corner partition (`permanent-results-registry.md:12998-12999`) defines **Cell I = algebra-INVARIANT × Mellin pole s=3** and **Cell II = algebra-INVARIANT × Mellin pole s=4**. §VII.AV.OP-PROJ is the trace-residue `Tr_{A_K}(P_a·|D_K|^{-2s})` at substrate-distance-2 pole **s=4**, algebra-INVARIANT ⇒ **Cell II**, NOT Cell I. Direct precedent: the Var_a Cell I→Cell II retraction (CF-25 S90 W2, `permanent-results-registry.md:13043`) for exactly this reason (algebra-INVARIANT × s=4 is Cell II). The W3-1/W3-5 landing mislabeled it. **Remediated in-session** (S93 W3-6, mack sole-writer, single-shot AFTER pattern with re-read+verify) via `s93_w3_6_vii_av_op_proj_cell_ii_remediation.py`: all 19 §VII.AV.OP-PROJ `Cell I` markers (index row 143, sub-slot heading + body, three-object map row (iii), STATE-PROJ cross-refs to OP-PROJ's cell, parent host-body sub-slot list + ASCII map) flipped `Cell I → Cell II`; residual Cell-I markers = 0; the GENERIC `Cell I (algebra-INVARIANT × substrate-distance-1)` cross-corner-co-primary-FORBIDDEN boilerplate (registry ~18634/18682) was preserved INTACT (it correctly cites the canonical Cell I = INVARIANT × s=3 definition, NOT §VII.AV.OP-PROJ). This is a confirmed classification-defect fix, NOT convention-shopping — the corner-cell is FORCED by the source-pinned partition definition (algebra-axis × Mellin-pole), not a free choice. `_vii_slot_allocation_audit.py` re-run post-remediation = **PASS** (zero drift: A_REGISTERED_AND_MATCHED=4, all of B/C/D/E/F = 0; slot map preserved — heading text changed, slot identifier `§VII.AV.OP-PROJ` unchanged).

**JOINT-ortho PASS-CONDITIONAL → PASS resolution**: vdd's Axis-A OP-PROJ `JOINT_structural_orthogonal_companion` clause was rendered `PASS-CONDITIONAL`, conditional on the W3-3 Class-8.7 degeneracy-witness confirming the ~375 trace-residue is genuine regulator-sensitive analytic content (NOT a finite-cardinality direct-sum tautology). That condition IS MET: W3-3 (`S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS`, audit_sha256=`f21af912268f548edaf21ccabaf020366b3df670bb9e038095a9c7d26955e91c`) returned PASS (cross_reg_spread_rel=0.190765 ~19%, `NOT_direct_sum_tautology`, n_degenerate_roots=1, max_root_mult=2). The aggregation reads the W3-3 verdict from the verdict file and resolves `PASS-CONDITIONAL → PASS` for this JOINT clause (recorded with `conditional_upgraded=true` in the aggregation JSON). Both JOINT clauses (bridge-map + orthogonal-companion) therefore PASS-AND across both axes on BOTH sub-slots.

**STATE-PROJ STAGE-3-eligibility**: §VII.AV.STATE-PROJ is a clean Stage-2 PASS-AND — Axis-A vdd PASS + Axis-B mack PASS + JOINT (bridge-map Connes-Karoubi Level-2-binding [W3-4 certified] + orthogonal-companion) PASS-AND. Substrate-input orthogonality at the **structural ceiling, NO overlap caveat** (the STATE-PROJ runtime npz `s91_w5_1_full_bdg_pv.npz` loaded ONLY by Axis-A vdd; the OP-PROJ residue cache `s92_w3_9...` loaded ONLY by Axis-B mack — disjoint substrate inputs, the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent). OAA exclusion {connes-ncg, phonon-first, volovik} satisfied (neither reviewer in the set; neither read the W-3 transcript). Convention ends `-FULL`. ⇒ §VII.AV.STATE-PROJ is STAGE-3-PERMANENT-ELIGIBLE per `joint-theorem-promotion.md §"Stage 3"` (the STAGE-3 registry-write flip is a separate registry-write sequenced via the W0-1 slot-pre-allocation lockfile, NOT in this wave).

**OP-PROJ Stage-2 re-verify carry-forward (CF-S94)**: although §VII.AV.OP-PROJ is structurally Stage-2-PASS-eligible on the CORRECTED (Cell II) entry (Axis-B all-PASS + JOINT PASS-AND + corner-cell now correct), the FORMAL Stage-2 verdict was rendered on the as-registered (Cell I) entry, which FAILed Axis-A's corner-cell clause. Per the strict Stage-2 protocol (`joint-theorem-promotion.md §"Stage 2"`: a FAIL on ANY clause blocks Stage-2→3), OP-PROJ Stage-2→3 promotion requires a RE-VERIFY of Axis-A on the Cell-II-corrected entry. This is a near-trivial re-dispatch (vdd already verified all other OP-PROJ clauses PASS; only the corner-cell clause changes on the corrected entry), but formally a re-verify gate. **§VII.AV.OP-PROJ stays STAGE-1-CANDIDATE.**

**Carry-Forward Computations**:

- **CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY-ON-CELL-II-CORRECTED-ENTRY**
  1. **What**: re-dispatch the Stage-2 Axis-A (vdd) cross-review of §VII.AV.OP-PROJ on the Cell-II-corrected registered entry; confirm the `corner_cell_classification` clause now PASSes (Cell II = INVARIANT × s=4), with all other OP-PROJ clauses (substrate-IS identity, parse-tree-INVARIANT classification, Level-1 single-τ-slice tag, JOINT bridge-map + orthogonal-companion) re-confirmed PASS; then aggregate the OP-PROJ sub-slot Stage-2 PASS-AND (Axis-A PASS + Axis-B PASS [already on disk] + JOINT PASS-AND).
  2. **Inputs**: the Cell-II-corrected §VII.AV.OP-PROJ registered entry (`sessions/permanent-results-registry.md`, post-S93-W3-6-remediation); the W3-3 witness verdict (audit_sha256=`f21af912...`, PASS); the existing Axis-B verdict JSON `s93_w3_6_axis_b_mack_verdicts.json` (OP-PROJ all-PASS); the OP-PROJ residue cache `s92_w3_9_...npz` (Axis-B-orthogonal input retained).
  3. **Gate**: OP-PROJ Stage-2 PASS-AND iff Axis-A vdd corner-cell clause == PASS (on Cell-II entry) AND all other OP-PROJ Axis-A clauses == PASS AND Axis-B == PASS AND JOINT PASS-AND. PASS ⇒ §VII.AV.OP-PROJ STAGE-3-PERMANENT-ELIGIBLE. The substrate-input-orthogonality structural ceiling + OAA-exclusion + convention-`-FULL` are inherited from W3-6.
  4. **Effort**: ~0.3 wave-equivalents (single Axis-A re-dispatch on the corrected entry; near-trivial since only the corner-cell clause changes).
  Depends on: S93 W3-6 corner-cell remediation (this wave; LANDED) + W3-3 witness PASS (this wave; LANDED).

**Verdict-line provenance**: W3-6 emitted as composite INFO at `computations/session-93/s93_gate_verdicts.txt` (latest non-superseded line; Option-A `supersedes` chain: original PRE-REG-INC target d6f990a7...4274771c [S91 W8-CF-68] → first INFO emission e79f577d... → enriched-value re-emit 610d1ac8...). scheme=`joint-theorem-promotion-Stage-2-per-sub-slot-parallel-cross-axis-PASS-AND`, convention ends `-FULL`, L_max=12.
"""


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    if AGG_ANCHOR in text:
        print("IDEMPOTENT: aggregation subsection already present; no re-insertion.")
        return 0
    if HEADER not in text:
        raise SystemExit(f"FATAL: §W3-6 header not found: {HEADER!r}")

    hdr_idx = text.index(HEADER)  # (local)
    rest = text[hdr_idx:]  # (local)
    m = re.search(r"\n---\n", rest)  # (local) section-closing delimiter after §W3-6
    if m:
        insert_at = hdr_idx + m.start() + 1  # (local) keep the leading '\n'
        new_text = text[:insert_at] + SUBSECTION + text[insert_at:]  # (local)
    else:
        new_text = text + SUBSECTION  # (local)

    tmp = WP.with_name(WP.name + ".tmp_agg")  # (local)
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(tmp, WP)
    print("WROTE aggregation-result subsection into §W3-6 (atomic os.replace).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
