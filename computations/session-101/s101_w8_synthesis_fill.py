#!/usr/bin/env python
"""
s101_w8_synthesis_fill.py — orchestrator-direct filler for (1) the §W8a-3 dropped-optional
record and (2) the Wave 8 team-lead synthesis in session-101-w8-workingpaper.md.

Section-anchored replacement on ASCII headers (`### §W8a-3.` and
`## Wave 8 Synthesis (team-lead)`), avoiding unicode-fragile line matching. Idempotent.

Content provenance: the verified on-disk W8 landings (5 PASS verdict lines at
s101_gate_verdicts.txt:197/201/205/207/209 + W8a-3 dropped) + the session-close
capstone-hygiene gate outcome (housekeeping A13 + corpus K=3) + the plan's run-order /
drop-first disposition (session-101-plan-w8.md §Run-Order item 3).
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403 -- import-only compliance (no constant consumed; WP filler)

WP = "sessions/session-101/session-101-w8-workingpaper.md"

W8A3 = """### §W8a-3. S101-ANALYTIC-HM-CERTIFICATION (connes-ncg-theorist) — *OPTIONAL SLOT, dropped under capacity pressure*

**Status**: DROPPED-OPTIONAL-PER-CAPACITY
**Gate ID**: `S101-ANALYTIC-HM-CERTIFICATION`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: COMPUTE — GEOMETRIC. **OPTIONAL EVOI Tier-3 #11d slot — LAST in run-order, drop-first under capacity pressure.**
**Agent**: `connes-ncg-theorist` (not dispatched)
**Plan reference**: `sessions/session-plan/session-101-plan-w8.md` §W8a-3

**Verdict**: **DROPPED-OPTIONAL-PER-CAPACITY** — NO verdict line emitted (pre-registered optional status per the plan run-order item 3: "If dropped: NO verdict line is emitted — not a mechanical closure, not a FAIL"). The W8a-3 analytic HM vacuum-uniqueness certification was the EVOI Tier-3 drop-first slot; given this session's depth (W1-W7 + the W8a/W8b methodology landings + the session-close capstone-hygiene gate), it is truncated cleanly. **EVOI row 11d (`sessions/evoi-framework.md:69`) remains LIVE for S102 re-admission** — the fresh EVOI case the W4 decision table required is preserved, not consumed. No artifacts, no verdict line, no registry change.

**Substrate framing**: GEOMETRIC (the vacuum-state structure of the C*-dynamical system on the UNTRUNCATED Jensen-SU(3) spectral triple — the fabric itself). The dropped gate would have certified the HM (arXiv 2412.00628) vacuum-non-uniqueness via an analytic d=8 Weyl + Noether-non-ergodicity argument; it carries forward intact as an optional analytic gate, not a closed corridor.

---

"""

SYNTH = """## Wave 8 Synthesis (team-lead)

**Outcome.** Wave 8 (the session's terminal wave) lands the four methodology/audit extensions consolidated from both S100 housekeeping ledgers, sub-decomposed at plan-freeze into W8a (COMPUTE) + W8b (METHODOLOGY) per `wave-classification.md §NROY`. **5 PASS + 1 DROPPED-OPTIONAL:**

| Gate | Class | Verdict | Landing |
|:-----|:------|:--------|:--------|
| W8a-1 `S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT` | COMPUTE | **PASS** | created `_machinery_feasibility_audit.py` (the "queued" entity, PRU Class-8 fix-now) + `detect_selection_rule_preflight` + `--self-test` |
| W8a-2 `S101-MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS` | COMPUTE | **PASS** | extended the module with `detect_multiplicative_cancellation` (3 signature classes) + corpus §21 (2 lab-IN-axis rows, NON-K-ADVANCING) |
| W8b-1 `S101-HK-SELECTION-RULE-PREFLIGHT-RULE` | METHODOLOGY | **PASS** | `math-scripts.md` §Double-Check sub-clause + corpus §22 (K=1 W2-2 calibration) |
| W8b-2 `S101-HK-SUFFIX-DISCIPLINE` | METHODOLOGY | **PASS** | `regulator-pin-discipline.md` Channel-Scope Suffix Extension (verbatim) + corpus §23 (K=1 W-4 census) |
| W8b-3 `S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION` | METHODOLOGY | **PASS** | `gate-verdicts.md` §Composite-collapse companion (collapse block byte-frozen) + corpus §24 (K=1 W4-1) |
| W8a-3 `S101-ANALYTIC-HM-CERTIFICATION` | COMPUTE (optional) | **DROPPED-OPTIONAL-PER-CAPACITY** | no verdict line; EVOI row 11d stays live for S102 |

**Run-order honored**: W8a-1 -> W8a-2 (single-writer on the new module) -> W8b-1 -> W8b-2 -> W8b-3 (corpus single-writer §21->§22->§23->§24, REROUTE=NONE) -> W8a-3 (dropped). The 3 W8b allowlist rows were landed at plan-freeze (M4 satisfied; SHAs `79d4c73c`/`e7bef692`/`8a58c9ea`); the 3 rule-file pre-edit base SHAs matched their plan pins exactly (zero drift); the W8b-3 firewall (composite-collapse pseudo-code BYTE-UNCHANGED) re-verified True. Global sig_5 clean across the full session verdict file (no duplicate `audit_sha256`). No session-aggregate PASS/FAIL ratio is reported (per `feedback_reporting-framing`).

### Carry-Forward Computations (MATH ONLY -> S102)

**No carry-forwards: all W8 wave outcomes closed in-session.** Every W8 item is methodology/audit work effected this session — the two audit detectors created + extended, the three rule directives landed, the four corpus calibration sections appended. The one droppable item (W8a-3) is an EVOI Tier-3 OPTIONAL slot, NOT a 4-field math carry-forward: it emits no verdict line and re-admits via the EVOI table (row 11d LIVE), not via the S102 plan CF stream. No W8a-1/W8a-2 detector FAIL fired (both PASS) -> no detector-remediation CF; no W8a-3 INFO sub-path fired (it was dropped, not run) -> no ergodicity-leg / extraction CF.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)

- [x] W8b-1/2/3 rule-file directives — three orchestrator-direct diffs, each verbatim from its plan binding-text block — `.claude/rules/math-scripts.md` + `regulator-pin-discipline.md` + `gate-verdicts.md` — verified 12/12 must_contain
- [x] Corpus calibration sections §21-§24 — single-shot append-helper, REROUTE=NONE — `sessions/framework/registry/pru-class-corpus.md`
- [x] Three W8b verdict lines emitted (METHODOLOGY dual-SHA, sig_5-unique) via `emit_verdict` — `computations/session-101/s101_gate_verdicts.txt:205/207/209`
- [x] W8b-1/2/3 WP sections filled (Status COMPLETED / Verdict PASS / Output Artifacts / MCP) — this WP §W8b-1/2/3
- [x] §W8a-3 marked DROPPED-OPTIONAL-PER-CAPACITY (no verdict line) — this WP §W8a-3
- [x] Session-close capstone-hygiene 5-question gate RUN (S101 terminal wave): Q1 a(t)-gap no-change; Q2/Q4/Q5 + Q3-status reconciliations all effected in-session (mack A8 / W4-4 / W6-9) or no-op-consistent; zero residual prose drift — `session-101-housekeeping.md §"Capstone-hygiene 5-question gate"` + A13
- [x] Capstone-hygiene gate K=2 -> K=3 promotion (SUGGESTION -> MANDATORY; 3rd distinct catching-session) — `capstone-hygiene-corpus.md` K=3 row + `.claude/rules/capstone-hygiene-gate.md §Status`
- [x] Housekeeping ledger W8 close — A13 + wave-log W8 + §F W1-W8 totals (13) + consumption pointers — `session-101-housekeeping.md`

(Self-audit: `grep -c '^- \\[ \\]'` on this sub-section returns 0.)

### Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-08 | `_machinery_feasibility_audit.py` | "queued" (refs `math-scripts.md:154/:255/:305`) | EXISTS (2 detectors, 4 signature classes; S102 plan-freeze invokes it) | W8a-1 create + W8a-2 extend, both PASS |
| 2026-06-08 | Selection-rule pre-flight directive | absent | SUGGESTION K=1 (`math-scripts.md` §Double-Check) | W8b-1 PASS |
| 2026-06-08 | Channel-scope suffix discipline | absent | SUGGESTION K=1 (`regulator-pin-discipline.md` Extension) | W8b-2 PASS |
| 2026-06-08 | Plan-frozen-operator precedence | absent | SUGGESTION K=1 (`gate-verdicts.md` §Composite-collapse companion) | W8b-3 PASS |
| 2026-06-08 | Capstone-hygiene gate | SUGGESTION K=2 | **MANDATORY K=3** (audit hook S2 -> S1 HARD-HALT) | S101 = 3rd distinct catching-session (D5 + H0 reconciliations) |
| 2026-06-08 | `S101-ANALYTIC-HM-CERTIFICATION` (EVOI 11d) | Tier-3 optional, admitted | DROPPED-OPTIONAL (row 11d live for S102) | drop-first under capacity; no framework state change |

### Files Produced

| Gate | Script / artifact | Edit |
|:-----|:------------------|:-----|
| W8a-1 | `_machinery_feasibility_audit.py` (created), `s101_w8a1_selection_rule_preflight_test.py` (+.npz) | — |
| W8a-2 | `s101_w8a2_mult_cancellation_lab_in_axis_test.py` (+.npz), `s101_w8a2_corpus_append_helper.py` | `_machinery_feasibility_audit.py` extension; `pru-class-corpus.md` §21 |
| W8b-1/2/3 | `s101_w8b_methodology_verify.py`, `s101_w8b_corpus_append_helper.py`, `s101_w8b_wp_fill.py` | `math-scripts.md`, `regulator-pin-discipline.md`, `gate-verdicts.md`; `pru-class-corpus.md` §22-§24 |
| session-close | `s101_w8_synthesis_fill.py` | `capstone-hygiene-corpus.md` (K=3), `capstone-hygiene-gate.md` (MANDATORY), `session-101-housekeeping.md` (A13 + gate block) |
| W8a-3 | (dropped — no artifacts) | EVOI row 11d unchanged |
"""


def main():
    with io.open(WP, "r", encoding="utf-8") as fh:
        text = fh.read()
    # 1. Replace §W8a-3 (header -> just before the synthesis header).
    pat_a3 = re.compile(r"(?s)### §W8a-3\. S101-ANALYTIC-HM-CERTIFICATION.*?(?=## Wave 8 Synthesis \(team-lead\))")
    if not pat_a3.search(text):
        raise SystemExit("FAIL: §W8a-3 span not found")
    text = pat_a3.sub(lambda m: W8A3, text, count=1)
    # 2. Replace the synthesis section (header -> EOF).
    pat_s = re.compile(r"(?s)## Wave 8 Synthesis \(team-lead\).*\Z")
    if not pat_s.search(text):
        raise SystemExit("FAIL: synthesis span not found")
    text = pat_s.sub(lambda m: SYNTH, text)
    with io.open(WP, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("WP §W8a-3 dropped-record + Wave 8 Synthesis filled; new len %d" % len(text))


if __name__ == "__main__":
    main()
