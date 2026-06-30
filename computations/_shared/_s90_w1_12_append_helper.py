#!/usr/bin/env python3
"""S90 W1-12 — append helpers for §18 corpus + allowlist + instances rows.

Three atomic open("a") appends:
  1. §18 "Class 8.7 Calibration Corpus" to pru-class-corpus.md
  2. W1-12 row to methodology-wave-allowlist.md
  3. W1-12 rationale to methodology-wave-instances.md
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline

PRU_CORPUS = ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

GATE_ROW = "W1-12"
SESSION = "S90"
PLAN_BLOCK_SHA = "25f08c2be513b86c9082c4a8efbec9e97f3cfc4174c8b440d0e5842af6690f1b"
AUDIT_SHA = "6369a880e2f49b7ec2660e553f0ca91d29f599148b2524b5ba221c20c552e38f"
CONTENT_SHA = "fa9522767eca204fb91833ada976294a84a07941c900c84d36f8c4c2c43988f6"
S89_W1_1_VERDICT_SHA = (
    "6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe"
)

CORPUS_SECTION_18 = f"""
## §18. PRU Class 8.7 Degenerate-Observable Pre-Flight Check (S90 W1-12 landing; epistemic-discipline.md §"Pre-Registration Completeness") — calibration corpus

### Status: SUGGESTION at K=1 (promotes to MANDATORY at K=3)

The Degenerate-Observable Pre-Flight Check (Class 8.7) directs that when a gate's
producing script computes `Tr(P · A) − R_CM` or `ζ_D(0)` on a finite spectral
triple with degenerate dimension-spectrum, the plan-block MUST pre-register a
degeneracy-witness (coincident-root declaration + per-pole multiplicity +
compositional-corridor pin). The class lands SUGGESTION-K=1 per
`feedback_rules-compensate-missing-structure.md` K-counter promotion threshold;
promotes to MANDATORY at K=3 distinct calibration-corpus instances.

### K=1 corpus (S90 W1-12 close, 2026-05-13)

| # | Instance | Substrate-physics pattern | Detection | Pre-registration status |
|:-:|:---------|:--------------------------|:----------|:------------------------|
| 1 | S89 §W1-1 `S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION` FAIL (audit_sha256=`{S89_W1_1_VERDICT_SHA}`) | `S_BH^substrate(M=1e7, L_max=10) = Tr_HSS(P_HSS) − R_CM` at substrate-distance-1 pole s=3 of finite spectral triple `(A_K^≤10, H_K^≤10, D_K^≤10)`; CM-1995 §III.4 residue formula on horizon-spanning sub-triple via P_HSS projector | P1 `r'Tr.*\\bP_HSS\\b.*[−-].*R_CM'` fires (3 matches on plan-w1.md §W1-1) | **NO degeneracy-witness declared in S89 §W1-1 plan-block** — would have flagged Class 8.7 at S2 advisory at S89 plan-freeze had this class been pre-existing |

The S89 §W1-1 FAIL with `value='alpha=-1.590633e-116;...;Tr_HSS=38;R_CM=3.800000e+01;...;monotone=False;K_advance=1to2_BY_CONSTRUCTION'` exhibited the substrate-IS structural pathology this class detects by construction: a naive single-pole CM-1995 §III.4 corridor that discards the multiplicity structure at the LRD-horizon scale (where the dimension-spectrum is degenerate per CM-1995 regular-spectral-triple theorem applicability). The (d)∘(b) compositional corridor per S89 W-1 R3 closure is the substrate-natural disambiguator; pre-registering it as the corridor pin (clause 3 of Class 8.7) at plan-block layer prevents the naive evaluation that produced the FAIL.

### Reserved rows

| # | Reserved-for | Pattern axis |
|:-:|:-------------|:-------------|
| 2 | future instance | Tr(P · A) − R_CM at distinct substrate-distance pole (e.g., s=4 substrate-distance-2) |
| 3 | future instance | `value = ζ_D(0)` direct evaluation OR HKR-image residue trace |

### K-counter advancement

`K_substantive = 1` at S90 W1-12 close (1 distinct calibration-corpus instance: S89 §W1-1). `K_promotion = 3` per `feedback_rules-compensate-missing-structure.md`. `K_substantive < K_promotion` → status remains SUGGESTION-K=1 (advisory until K=3); audit-script emits S2 advisory severity on detected violations until K=3 promotion.

### Forward enforcement (audit-script hook)

`computations/_shared/_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable(plan_block_text, block_label)` returns structured diagnostic dict with `has_class_8_7_flag`, `severity` (S2 or NONE), `p1_matches`, `p2_matches`, `degeneracy_witness_present`, `degeneracy_witness_markers_found`, `diagnostic`. Plan-freeze auditors invoke the detector on each new gate's plan-block; flag at S2 advisory (HARD-HALT after K=3 promotion).

The detector's positive self-test (S89 §W1-1) and negative self-test (synthetic-with-witness) both PASS at S90 W1-12 close, audit_sha256=`{AUDIT_SHA}`.

### Cross-link

- Parent rule: `.claude/rules/epistemic-discipline.md §"Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until K=3)"`.
- Sub-class taxonomy row: `.claude/rules/epistemic-discipline.md §"PRU Class 8 sub-class taxonomy"` row 8.7.
- Audit script: `computations/_shared/_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable()`.
- Self-test driver: `computations/_shared/s90_w1_pru_class_8_7_test.py`.
- K=1 calibration instance source: S89 §W1-1 FAIL at `computations/session-89/s89_gate_verdicts.txt:1`; plan-block at `sessions/session-plan/session-89-plan-w1.md` lines 50-150 (HSS-projector trace minus CM regularized mean substrate-physics pattern).
- W6-3 hygiene-gap discharge context: `sessions/archive/session-89/session-89-w6-workingpaper.md` line 363 ("Plan §1.2 listed `_pru_cardinality_audit.py` as 'hard prerequisite'. None of the three existed on disk. W6-1 was built without using `_pru_cardinality_audit.py` as template.") — `_pru_cardinality_audit.py` was created in-session at S90 W1-12 with Class 8.7 as inaugural content per `feedback_fix-in-session-never-defer.md`.
"""

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE = f"""
### {GATE_ROW} ({SESSION}) — {PLAN_BLOCK_SHA}

**Provenance**: gate-ID `S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE`
(PHONON-FIRST V.4); agent `gen-physicist orchestrator-direct-write` per
`wave-classification.md §"Dispatch consequences"`; plan reference
`sessions/session-plan/session-90-plan-w1.md` §W1-12 lines 780-857; plan-block
sha256 `{PLAN_BLOCK_SHA}` (7631 chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1**: artifact-existence-with-substantive-content per `wave-classification.md §M1`.
  PASS predicate = (i) Class 8.7 row added to PRU sub-class taxonomy + (ii) sub-
  section appended in directive shape + (iii) audit-script extension lands with
  P1+P2 patterns + degeneracy-witness check + (iv) positive self-test fires on
  S89 §W1-1 + (v) K=1 corpus row appended at pru-class-corpus.md §18 + (vi)
  allowlist/instances rows. No numerical comparison; all conditions are
  artifact-existence + content-substance.
- **M2**: producing operations restricted to Edit/Write/MultiEdit on rule-files
  + audit-script extension (`_pru_cardinality_audit.py` created from scratch in-
  session per `feedback_fix-in-session-never-defer.md` discharge of W6-3
  hygiene-gap documented at S89 W6 WP line 363) + Python self-test driver. No
  numerical comparisons against pre-registered thresholds; the test driver's
  PASS predicate is artifact-existence + content-substance (8 binary conditions).
- **M3**: verbatim sub-diff from S89 PHONON-FIRST synthesis §V.4 (which
  proposed Class 8.7 promotion) + S89 §W1-1 FAIL substrate-physics pattern
  (verbatim source of the K=1 calibration instance). No first-principles new
  derivation; the Class 8.7 detection patterns P1+P2 + degeneracy-witness
  markers are verbatim from plan §W1-12 #6 dispatch prompt.
- **M4**: row landing per `methodology-wave-allowlist.md §"Edit discipline"`
  orchestrator-only-edit protocol.

**Sub-clause structure landed**:
1. PRU sub-class taxonomy row 8.7 in `.claude/rules/epistemic-discipline.md`
   (single row addition; directive-shape "advisory until K=3" per hook constraint).
2. New sub-section "Degenerate-Observable Pre-Flight Check (Class 8.7; advisory
   until K=3)" appended in `.claude/rules/epistemic-discipline.md` in directive
   shape: When-X/MUST-Y rule + 3 enumerated structurally-required elements
   (coincident-root declaration / per-pole multiplicity / compositional-corridor
   pin) + audit-script cross-reference + corpus cross-reference.
3. `computations/_shared/_pru_cardinality_audit.py` created from scratch with
   P1 + P2 detector regexes + DEGENERACY_WITNESS_MARKERS regex +
   `detect_class_8_7_degenerate_observable(plan_block_text, block_label)`
   function returning structured diagnostic dict + built-in `run_self_test()`
   on S89 §W1-1 and `run_negative_self_test()` on synthetic-with-witness.
4. §18 "Class 8.7 Calibration Corpus" appended to `pru-class-corpus.md`
   carrying K=1 corpus + reserved rows + K-counter advancement + audit-script
   pin + cross-links (per hook directive that K-counter narrative + audit-SHAs
   + dated content belong in corpus file, not rule file).

**Closure conditions**: PASS verdict per pre-registered #9 (i)-(vi) — 8/8
operational conditions satisfied (taxonomy row, sub-section, P1, P2, witness,
detector function, positive self-test, negative self-test). audit_sha256=
`{AUDIT_SHA}` over 15-pin input-pin map (5 file SHAs + S89 §W1-1 verdict SHA +
3 regex patterns + K-counter status + K-promotion threshold + positive/negative
test result counts + composite verdict). content_sha256=`{CONTENT_SHA}` over
the test-driver body. sig_5 SHA-uniqueness verified at emission.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-12 (plan
reference, 7631-char block, sha256=`{PLAN_BLOCK_SHA}`); `.claude/rules/epistemic-discipline.md §"PRU Class 8 sub-class taxonomy"` row 8.7 + `§"Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until K=3)"`;
`computations/_shared/_pru_cardinality_audit.py` (file created in-session;
Class 8.7 inaugural content); `computations/_shared/s90_w1_pru_class_8_7_test.py`
(self-test driver, T1 positive on S89 §W1-1 + T2 negative on synthetic);
`sessions/framework/registry/pru-class-corpus.md §18` (K=1 corpus + reserved
rows + K-counter advancement); S89 §W1-1 FAIL verdict at audit_sha256=
`{S89_W1_1_VERDICT_SHA}` (K=1 calibration instance source);
`sessions/archive/session-89/session-89-w6-workingpaper.md` line 363 (W6-3 hygiene-gap
context for in-session creation of `_pru_cardinality_audit.py`);
`feedback_fix-in-session-never-defer.md` (basis for in-session file creation
rather than deferring to a separate prerequisite gate);
`feedback_rules-compensate-missing-structure.md` (K-counter promotion threshold
SUGGESTION → MANDATORY at K=3).

**Carry-forward (3 substantive items)**:
1. K=3 promotion: when 2 additional calibration instances land for Class 8.7,
   the audit-script extension `MISSING-DEGENERACY-WITNESS` severity escalates
   from S2 advisory to S1 HARD-HALT at plan-freeze; the rule's status tag in
   epistemic-discipline.md taxonomy row 8.7 migrates from "advisory until K=3"
   to "MANDATORY". Reserved rows 2 + 3 in pru-class-corpus.md §18 await this
   advancement.
2. Broader D_PRU_raw cardinality audit (the OTHER half of `_pru_cardinality_audit.py`
   per `computations/tests/test_pru_cardinality_audit.py` expectations: self-
   audit D_PRU_raw=0, coupling-rank, plan-parser, script-parser, substitution-
   chain arithmetic) is a separate carry-forward NOT discharged by §W1-12. The
   broader audit's test file has been on disk since S84 W9A-97 without the
   implementation; building it out is a future-session work item.
3. S89 §W1-1 substantive remediation: re-dispatch with degeneracy-witness pre-
   registered at plan-block layer (the (d)∘(b) compositional corridor per S89
   W-1 R3 closure recovers the multiplicity structure the naive single-pole
   CM-1995 §III.4 corridor discards). The S89 §W1-1 FAIL is not invalidated by
   the §W1-12 audit landing; rather, §W1-12 provides the structural pre-flight
   that would have caught the naive-corridor evaluation at S89 plan-freeze had
   the class been pre-existing.

**Parallel-review dispatch**: not applicable per --tasking "as applicable"
clause (plan §W1-12 #4 names no CO-AUTHOR; gen-physicist orchestrator-direct-
write is the sole agent).

**Substrate framing**: Dimension-spectrum degeneracy at the LRD-horizon IS a
substrate-IS structural property of the finite spectral triple at the
substrate-distance-1 pole s=3; the multiplicity is the substrate's own
combinatorial fingerprint of the horizon-spanning Peter-Weyl sector
decomposition. Class 8.7 captures the methodology F-image of substrate-IS
degeneracy at the plan-block layer per `epistemic-discipline.md §"Layer-Decomposition"`
`F: substrate → methodology → audit`. The rule prevents silent naive-corridor
evaluation that discards substrate-IS multiplicity; the audit script makes the
substrate's own degeneracy structure visible at the plan-freeze layer.
Container-thinking violation FORBIDDEN: "the degeneracy is a numerical artifact
of L_max truncation" — inverted: "the multiplicity IS substrate-IS, intrinsic
to the spectral triple's Peter-Weyl block decomposition; the audit makes the
substrate's own structure visible at the methodology floor; the (d)∘(b)
compositional corridor IS the substrate-natural disambiguator that recovers the
substrate-IS multiplicity from the residue evaluation".
"""


def main() -> None:
    with open(PRU_CORPUS, "a", encoding="utf-8") as f:
        f.write(CORPUS_SECTION_18)
    print(f"Corpus §18 appended: {CORPUS_SECTION_18.count(chr(10))} lines, {len(CORPUS_SECTION_18)} chars")

    with open(ALLOWLIST, "a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    with open(INSTANCES, "a", encoding="utf-8") as f:
        f.write(INSTANCES_RATIONALE)
    print(f"Instances rationale appended: {INSTANCES_RATIONALE.count(chr(10))} lines, {len(INSTANCES_RATIONALE)} chars")


if __name__ == "__main__":
    main()
