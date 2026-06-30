#!/usr/bin/env python
"""
s101_w8b_corpus_append_helper.py — single-shot append-helper for the three W8b
calibration-corpus sections into sessions/framework/registry/pru-class-corpus.md.

  §22 <- W8b-1 S101-HK-SELECTION-RULE-PREFLIGHT-RULE   (selection-rule pre-flight)
  §23 <- W8b-2 S101-HK-SUFFIX-DISCIPLINE               (channel-scope suffix)
  §24 <- W8b-3 S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION (plan-frozen operator precedence)

Registry-write hygiene (epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"): single-shot open("a") O_APPEND writes (NOT Edit round-trip);
scan ALL header levels (## / ### / #### §N) before allocation; runtime-occupancy
reroute to next-free with disclosure. Sole sequential writer under the W8 run-order
(W8a-2 §21 already landed; this helper lands §22 -> §23 -> §24 in order).

Section bodies are transcribed from session-101-plan-w8.md corpus-instruction text:
  §22 <- plan :681-692 ; §23 <- plan :928-937 ; §24 <- plan :1180-1194.
"""
import re
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403 -- import-only compliance (no constant consumed; registry-write helper)

CORPUS = "sessions/framework/registry/pru-class-corpus.md"

BODY_22 = """**Rule home**: `math-scripts.md §"Double-Check Logic Before Compute" -> "Selection-rule pre-flight for pre-registered nonzero matrix elements"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). **Audit hook**: `computations/_shared/_machinery_feasibility_audit.py::detect_selection_rule_preflight` (landed S101 W8a-1; verdict `S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT` PASS).

### K=1 calibration instance -- S100a W2-2 (Yukawa overlap off-diagonal)

The S100a plan-w2 §W2-2 substitution chain asserted `<psi_(1,0)| |s(h)|^2 |psi_(1,1)> != 0` via the rationale "C^2 in su(3) weight connecting triality-adjacent sectors". This is **group-theoretically FALSE**: `|s(h)|^2` is a squared modulus, hence center-character (triality) 0 ALWAYS, so the SU(3) center-Z_3 selection rule annihilates the element to 0 EXACTLY. The cited connecting property belongs to `s(h)` itself (irrep (2,0), triality 2 == -1 mod 3), NOT to `|s(h)|^2`.

Full mod-3 arithmetic table (triality `t(p,q) = (p-q) mod 3`):

| quantity | irrep | triality |
|:---|:---|:---|
| bra psi_(1,0) | (1,0) | t = (1-0) mod 3 = 1 |
| ket psi_(1,1) | (1,1) | t = (1-1) mod 3 = 0 |
| s(h) | (2,0) | t = (2-0) mod 3 = 2 |
| conj(s(h)) | (0,2) | t = (0-2) mod 3 = 1 |
| operator |s(h)|^2 = s*conj(s) | -- | t = (2+1) mod 3 = 0 |

Center-character selection rule: `<a|O|b> != 0` REQUIRES `t(a) == t(b) + t(O) (mod 3)`. Substitute a=(1,0), b=(1,1), O=|s(h)|^2: `1 == 0 + 0 (mod 3)` is **FALSE** => `<(1,0)| |s(h)|^2 |(1,1)> = 0` EXACTLY. Contrast: the bare operator s(h) (t=2) DOES satisfy the necessary check for the (1,0)<->(1,1) pair (`t(1,1) = 0 == t(1,0) + t(s) = 1 + 2 = 3 == 0 mod 3`) -- the connecting property the chain mis-attributed to the squared modulus.

**Disclosure provenance**: caught in-gate and honestly disclosed at plan-freeze -- canonical line `computations/session-100a/s100a_gate_verdicts.txt:36` (gate S100a-YUKAWA-OVERLAP-OFFDIAG, audit `871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925`); selection-rule companion row `:40` ("literal (1,0)<->(1,1) |s|^2 element=0 exact (center-Z3/triality selection)").

**K-counter**: K=1. Advances on DISTINCT inadmissible-claim catches at plan-freeze (a new theorem / sector pair the detector flags), NOT on re-citations of the W2-2 instance."""

BODY_23 = """**Rule home**: `regulator-pin-discipline.md §"Extension: Channel-Scope Suffix Discipline for Register Citations of Channel-/Parity-Scoped PERMANENT Theorems"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`).

### K=1 calibration instance -- S100a W-4 five-surface census

Source: the S100a W-4 D5 seesaw-adjudication workshop `sessions/session-100a/workshops/s100a-w5-d5-seesaw-adjudication-workshop.md` (SHA `d7632f2c6e4e455d02e0640182933fcbac301a8fea2b082218abb2b2d67f0ca5`) -- [AGENDA-6a] FINAL draft + E4 census + V-C6 confirmation + the E-3 2/2-escaped-vs-2/2-caught split. Routing note: housekeeping-100a §D CF-S101-HK-SUFFIX.

The **five-surface census**: five register surfaces were audited for the `S41 W1-2` T-channel `S_F^Connes = 0` citation. Verdict -- the two instances that REACHED registers escaped through consolidation/aggregation steps that dropped the separable scope parenthetical (the over-broad "seesaw = 0" reading regenerated downstream); the two surfaces that carried the scope INSIDE the citation token survived intact (the 2/2-escaped vs 2/2-caught split). Structural mechanism: separable parentheticals do not survive consolidation steps, so scope-inside-the-token makes the wrong reading non-regenerable from the surviving artifact -- the register-side analog of the contrast-inside-the-output pattern.

**K-counter**: K=1. Advances on DISTINCT channel-/parity-scoped PERMANENT theorems (e.g. a new T-/P-channel or gamma9-odd/even theorem receiving the suffix treatment), NOT on repeat citations of S41 W1-2."""

BODY_24 = """**Rule home**: `gate-verdicts.md §"Composite-collapse rule" -> "Plan-frozen gate-block operator precedence (applicability guards)"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). **Adjacent prior**: corpus §19 (Composite-collapse CORE-vs-fringe override-clause) is on a DIFFERENT axis -- §19 overrides a sign=FAIL label via four guards at the gate-semantic layer; THIS clause governs operator-vs-generic-collapse precedence at the plan-freeze layer; both compose with, neither modifies, the collapse rule.

### K=1 calibration instance -- S100b W4-1 (D_K ergodicity, Weyl-applicability guard)

Instance: S100b W4-1 (gate S100b-DK-ERGODICITY, `computations/session-100b/s100b_gate_verdicts.txt:56`, audit `273a0dc45a1e9f2500db5b7548fefed70ab6e7d82c3f4c945dcf9562f945d7ba`). The schema-v2 3-tuple at `:58` is (sign=PASS, magnitude=PASS, regime=MARGINAL); the generic `gate-verdicts.md` composite-collapse reads this via the else-branch as **PASS**. But the plan-frozen W4-1 gate-block operator pre-registered **INFO** on Weyl-applicability failure (the HM Def 2.3 Weyl law on the finite truncation) -- the GUARD, not the hypothesis. The composite-precedence extra-row was pre-declared BEFORE evaluation and is on disk at `:60`: "# composite-precedence: plan SS W4-1 gate-block operator pre-registers INFO on Weyl-applicability failure (guard, not hypothesis); generic gate-verdicts.md collapse of (PASS,PASS,MARGINAL) would read PASS; the plan-specific operator governs the composite".

**Conservative direction**: a hollow PASS was REFUSED in favor of the honest INFO -- the applicability guard failed, so the criterion never tested its hypothesis; awarding PASS would claim more than the truncated spectral functional actually demonstrated.

**K-counter**: K=1. Advances on DISTINCT pre-declared precedence invocations (a new gate whose plan-frozen operator conflicts with the generic collapse and carries the pre-declared extra-row), NOT on re-citations of W4-1."""

SECTIONS = [
    ("S101-HK-SELECTION-RULE-PREFLIGHT-RULE",
     'Selection-rule pre-flight (math-scripts.md §"Double-Check Logic Before Compute" sub-clause) -- calibration corpus',
     BODY_22),
    ("S101-HK-SUFFIX-DISCIPLINE",
     "Channel-scope suffix discipline (regulator-pin-discipline.md Extension) -- calibration corpus",
     BODY_23),
    ("S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION",
     'Plan-frozen gate-block operator precedence (gate-verdicts.md §"Composite-collapse rule" companion) -- calibration corpus',
     BODY_24),
]


def next_free(text):
    nums = [int(m.group(1)) for m in re.finditer(r'(?m)^#{2,4}\s*§(\d+)\b', text)]
    return (max(nums) + 1) if nums else 1


def main():
    with io.open(CORPUS, "r", encoding="utf-8") as fh:
        text = fh.read()
    landed = []
    for gate_id, title, body in SECTIONS:
        n = next_free(text)                                  # (local) all-header-level pre-scan
        section = "\n## §%d. %s\n\n%s\n" % (n, title, body.rstrip())  # (local)
        with io.open(CORPUS, "a", encoding="utf-8") as fh:   # single-shot O_APPEND
            fh.write(section)
        with io.open(CORPUS, "r", encoding="utf-8") as fh:   # re-read for next-free recompute
            text = fh.read()
        landed.append((gate_id, n))
        print("LANDED §%d  <- %s" % (n, gate_id))
    nums = [n for _, n in landed]                            # (local)
    print("REROUTE=NONE" if nums == [22, 23, 24] else "REROUTE landed=%s" % nums)
    return landed


if __name__ == "__main__":
    main()
