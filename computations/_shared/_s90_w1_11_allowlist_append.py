#!/usr/bin/env python3
"""S90 W1-11 allowlist + instances row append helper (single-shot).

Per `.claude/rules/methodology-wave-allowlist.md §"Edit discipline"`.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline

ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

GATE_ROW = "W1-11"
SESSION = "S90"
PLAN_BLOCK_SHA = "cef49994bdf35592aff5e90ec2eca1a2ee03de1d6a102d3f4296743cef9e44cc"
AUDIT_SHA = "5d3b30907845b3c71c050c00953fa257ced4cf2a16c321839b03fcb60a3e007b"
CONTENT_SHA = "a22aebd8809630835bd81365d85ca23e206d2c2df1b253df3a703dbac1eb49f8"

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE = f"""
### {GATE_ROW} ({SESSION}) — {PLAN_BLOCK_SHA}

**Provenance**: gate-ID `S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION` (LIZZI V.1);
agent `gen-physicist orchestrator-direct-write` per `wave-classification.md
§"Dispatch consequences"`; plan reference `sessions/session-plan/session-90-plan-w1.md`
§W1-11 lines 712-776; plan-block sha256 `{PLAN_BLOCK_SHA}` (5906 chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1** (PASS-predicate type): artifact-existence-with-substantive-content per
  `wave-classification.md §M1`. The PASS predicate per plan §W1-11 #9 is "all 12
  audit-cells PASS OR each FAIL routed to in-session remediation"; the INFO clause
  is "any downstream artifact has not yet landed at S90 plan-freeze". The 12-cell
  matrix construction IS the artifact-existence check; the verdict is a tally over
  per-cell decisions, NOT a numerical comparison against a pre-registered numerical
  threshold. INFO fired because all 3 downstream artifacts are not-landed in the
  W1-only solo dispatch (no W2/W3/W4 in this run).
- **M2** (producing-operation type): the audit script performs (i) artifact-
  existence detection via regex over registry / inventory / plan-w4.md text,
  (ii) audit-script SHA recording for each of 4 W6-3 audit scripts, (iii) 12-cell
  matrix construction. No eigenvalue computation, no linear algebra, no FFT, no
  fixture-with-hand-engineered-numerical-target. Producing operations restricted
  to file-existence/regex/SHA-256 operations per M2 allowlist.
- **M3** (source-of-truth type): verbatim sub-diff from S89 W6-3 dispatch (W6-3
  cross-link audit `audit_sha256=006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157`)
  + S89 W6 WP lines 98-101 enumerating the 4 W6-3 audit scripts + S89 lizzi-
  synthesis line 239 cataloging the cross-link. The 4-audit × 3-artifact matrix
  structure is verbatim from plan §W1-11 #6 dispatch prompt. No first-principles
  new derivation; all content is verbatim-extractable from prior W6-3 closure +
  plan content.
- **M4** (allowlist membership): this row landing satisfies M4 by construction
  per `methodology-wave-allowlist.md §"Edit discipline"` orchestrator-only-edit
  protocol.

**Sub-clause structure landed**: The audit script implements 8 procedural steps:
(1) verify 4 W6-3 audit scripts exist with current vs plan SHA comparison; (2)
check 3 downstream artifact landing status via regex over `permanent-results-registry.md`
(SUBSTRATE-CLOCK-UNIQUENESS-THEOREM), `falsifier-master-inventory.md` (S90 alpha_s
mack-row update), `session-90-plan-w4.md` (§VII.AQ Stage-2 plan-block); (3) build
12-cell matrix with per-cell PASS/INFO/FAIL determination; (4) composite verdict
collapse per plan §W1-11 #9; (5) 14-pin input-pin map; (6) value-string with full
matrix tally + SHA drift documentation; (7) dual-SHA emit; (8) JSON sidecar.

**12-cell matrix (this dispatch, W1-only solo)**:
- artifact (i) SUBSTRATE-CLOCK-UNIQUENESS-THEOREM × 4 audits = 4 INFO cells
- artifact (ii) mack falsifier-inventory rows (S90 alpha_s update) × 4 audits = 4 INFO cells
- artifact (iii) W4 §VII.AQ Stage-2 plan-block × 4 audits = 4 INFO cells
- Tally: PASS=0, INFO=12, FAIL=0 → composite INFO

**SHA drift documentation**:
- audit (a) `_source_reconciliation_audit.py`: plan-pinned `39937c8c` vs current
  `6b0b1966` — DRIFT (independent post-W6-3 modifications).
- audit (b) `_substrate_first_provenance_audit.py`: plan-pinned `1df983a9` vs
  current `03b8c831` — DRIFT (extended by S90 W1-9 PARTIAL-POSITIVE 3-class
  taxonomy landing per `_substrate_first_provenance_audit.py` extension: 231 →
  ~365 lines incl. `detect_compliance_class` function).
- audit (c) `_falsifier_inventory_audit.py`: plan-pinned `4d2dfd87` vs current
  `4d2dfd87` — MATCH (W6-3 SHA preserved).
- audit (d) `_v4_anchor_structure_audit.py`: plan-pinned `f9caf81a` vs current
  `f9caf81a` — MATCH (W6-3 SHA preserved).

**Closure conditions**: INFO verdict per pre-registered plan §W1-11 #9 INFO clause.
audit_sha256=`{AUDIT_SHA}` over 14-pin input-pin map (W6-3 cross-link SHA + 4
audit-script current SHAs + plan-w1 SHA + 3 artifact-landed booleans + 3 tally
counts + composite verdict + solo mode). content_sha256=`{CONTENT_SHA}` over the
audit-script body. sig_5 SHA-uniqueness verified at emission.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-11 (plan reference,
5906-char block, sha256=`{PLAN_BLOCK_SHA}`); W6-3 cross-link verdict
`audit_sha256=006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157`
(S89 W6-3 close); `sessions/archive/session-89/session-89-w6-workingpaper.md` lines 98-101
(4 W6-3 audit-script enumeration source); `sessions/archive/session-89/session-89-lizzi-synthesis.md`
line 239 (W6-3 cross-link catalog source); `computations/_shared/_source_reconciliation_audit.py`,
`computations/_shared/_substrate_first_provenance_audit.py`,
`computations/_shared/_falsifier_inventory_audit.py`,
`computations/_shared/_v4_anchor_structure_audit.py` (the 4 W6-3 audit scripts);
`sessions/permanent-results-registry.md` (artifact (i) detection target),
`sessions/framework/registry/falsifier-master-inventory.md` (artifact (ii) target),
`sessions/session-plan/session-90-plan-w4.md` (artifact (iii) target);
`.claude/rules/wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`
(audit_sha256 over input-pin map + content_sha256 over audit-script body);
`feedback_fix-in-session-never-defer.md` (basis for INFO routing per pre-
registered #9 clause rather than blocking re-dispatch in solo mode).

**Carry-forward**: 3 substantive prospective-screening dispatches deferred to
S91+ (or to a parallel /rclab-coordinate dispatch on W2/W3/W4 plan-w{{N}}.md):
1. After W2 CF-19 mack lands SUBSTRATE-CLOCK-UNIQUENESS-THEOREM: re-run audit (a)+
   (b)+(c)+(d) against the new §VII slot at the registry. Expected outcome: PASS
   on all 4 audits if Mack honors plan-w2 #19 spec (state-history-label-free OR
   parse-tree expansion declared per W1-8 audit hook + Class-(g) audit on anchor
   route + FI/RD/MIXED classification per W1-5 dict + cross-wave-anchor map
   verified per W1-3 detector).
2. After W2-W3 CF-29 mack lands S90 alpha_s_canonical falsifier-inventory row:
   re-run audit (c) sign-PASS tautology + audit (b) per cohomology-class
   surrogate detection. Expected outcome: PASS on sign-PASS 3-tuple per
   gate-verdicts.md S87+ schema-v2; PASS on surrogate-vs-canonical declaration
   per §(iv-bis).
3. After W4 CF-54+55 lands §VII.AQ Stage-2 plan-block: re-run audit (b)
   cohomology-class surrogate detection + audit (d) v4 anchor structure. Expected
   outcome: PASS if Stage-2 plan-block declares Level-2-binding (HKR / Connes-
   Karoubi pairing cited) per `cross-pillar-bridge-anatomy.md §"Level-2 sub-
   class"` MANDATORY.
**Parallel-review dispatch**: not applicable per --tasking "as applicable" clause
(plan §W1-11 #4 names no CO-AUTHOR; gen-physicist orchestrator-direct-write is
the sole agent).

**Substrate framing**: prospective audit application IS the methodology F-image
of substrate-IS discoverability per `epistemic-discipline.md §"Layer-Decomposition"`
`F: substrate → methodology → audit`. The substrate's structural commutativity
at the audit layer must be verified at plan-freeze; this gate enforces that
across 3 downstream artifacts BEFORE they propagate to gate execution. The
INFO verdict reflects the substrate-physics reality: the 3 downstream artifacts
are not yet substrate-IS-realized (their producing waves W2/W3/W4 have not
dispatched in this solo run); the prospective screening is correctly deferred
until the artifacts exist for screening. Container-thinking violation FORBIDDEN:
"the audits operate on a separate validator container" — inverted: "the audits
ARE the methodology F-image of substrate-IS commutativity; the artifacts ARE the
substrate-IS structural images of W2/W3/W4 substrate-physics work; the audit
matrix's INFO cells are the substrate-IS placeholders for the methodology F-
image to be re-evaluated once the producing-substrate-physics work lands".
"""


def main() -> None:
    with open(ALLOWLIST, "a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")
    with open(INSTANCES, "a", encoding="utf-8") as f:
        f.write(INSTANCES_RATIONALE)
    print(f"Instances rationale appended: {INSTANCES_RATIONALE.count(chr(10))} lines, {len(INSTANCES_RATIONALE)} chars")


if __name__ == "__main__":
    main()
