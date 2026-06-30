#!/usr/bin/env python
"""
s101_w8b_wp_fill.py — orchestrator-direct WP section filler for the three W8b
METHODOLOGY-class gates (§W8b-1/2/3) in session-101-w8-workingpaper.md.

Replaces the three NOT-STARTED scaffold sections wholesale (matched by their ASCII
`### §W8b-N.` headers, so no unicode-fragile line matching) with COMPLETED sections
carrying the verified outcome + emitted dual-SHA. The §W8a-3 section that follows is
left untouched. Idempotent: re-running rewrites the same three sections.

Content provenance: the scaffold's own pending descriptions (planner-authored expected
outcome) + the verified on-disk landings + the emitted verdict SHAs
(s101_gate_verdicts.txt). Not a compute artifact — orchestrator-direct presentation.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403 -- import-only compliance (no constant consumed; WP presentation filler)

WP = "sessions/session-101/session-101-w8-workingpaper.md"

SEC_W8B1 = """### §W8b-1. S101-HK-SELECTION-RULE-PREFLIGHT-RULE (orchestrator-direct-write)

**Status**: COMPLETED
**Gate ID**: `S101-HK-SELECTION-RULE-PREFLIGHT-RULE`
**Trigger**: `[AUDIT]`
**Classification**: **METHODOLOGY** (wave-class, post-allowlist-append; M1-M3 PASS, M4 satisfied by the plan-freeze ledger row `79d4c73c...`) -- NON-PHONONIC (rule-file directive landing; orchestrator-direct-write per `wave-classification.md §Dispatch consequences`)
**Agent**: orchestrator (direct-write; gen-physicist authored the plan block, the orchestrator effected the edits)
**Hypothesis**: The selection-rule pre-flight directive lands in `math-scripts.md §Double-Check Logic Before Compute` (after §Plan-author discipline) and its W2-2 calibration instance lands as a `pru-class-corpus.md` section -- closing, at the rule layer, the same plan-freeze gap W8a-1's detector closes at the audit layer.
**Plan reference**: `sessions/session-plan/session-101-plan-w8.md` §W8b-1

**Output Artifacts** (closure-verified on disk by content-presence regex):
- `.claude/rules/math-scripts.md` -- new `#### Selection-rule pre-flight for pre-registered nonzero matrix elements` sub-section inserted after §Plan-author discipline at plan-freeze; 4/4 must_contain present (`#### Selection-rule pre-flight for pre-registered nonzero matrix elements`, `center-character / triality CG-admissibility check`, `NECESSARY condition only`, `detect_selection_rule_preflight`). Pre-edit base SHA `ed062fc5...` matched the plan pin.
- `sessions/framework/registry/pru-class-corpus.md` §22 -- 3/3 must_contain present (`Selection-rule pre-flight`, `871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925`, `K=1`). Landed via single-shot append-helper (REROUTE=NONE).
- `computations/session-101/s101_w8b_methodology_verify.py` (shared W8b-1/2/3 driver; created here) -- `from canonical_constants import`, `print_verdict_payload` present.
- `computations/session-101/s101_w8b_corpus_append_helper.py` -- single-shot O_APPEND corpus writer.
- Verdict line `S101-HK-SELECTION-RULE-PREFLIGHT-RULE: PASS` + dual-SHA companion in `computations/session-101/s101_gate_verdicts.txt` (no schema-v2 3-tuple -- [AUDIT] gate).

**MCP Pre-Compute Audit**: METHODOLOGY-class artifact-existence landing -- NO substrate-physics result to pre-close. Query-first discipline (knowledge-MCP) confirms this is a NEW directive sub-section (no prior `selection-rule pre-flight` directive in `math-scripts.md`) and a NEW corpus section -- not a re-derivation of any closed mechanism. PRE-CLOSED check: N/A (the protected substrate fact -- SU(3) center-Z_3 sector selection -- is the SAME grading underlying the already-PROVEN block-diagonal D_K structure; this gate adds the methodology-floor enforcement, not a new physics claim).

**Verdict**: **PASS** -- `audit_sha256=e9e6e46be4ba4560ed6acdd2a71bc025c9341fd8a1282a2146a40d9e2f0f2b5e` `content_sha256=ee62969a347f6c41050987bdf1749645f6086c1d8b6e7b18391a2ba7ff2c8b38` (METHODOLOGY dual-SHA: content over applied rule-section + corpus-section; audit over the source-document input-pin map incl. `_gate_id`; sig_5-unique). scheme=METHODOLOGY-DIRECTIVE-LANDING, convention=DIRECTIVE-ONLY-RULE-PLUS-CORPUS, L_max=N/A.

**Results**: The directive (SUGGESTION K=1 -> MANDATORY at K=3) binds any plan-block substitution chain asserting a "generically nonzero" / `!= 0` matrix element between named irrep sectors to a two-line center-character (triality) CG-admissibility check at plan-freeze: state `t(a)`, `t(b)`, `t(O)` (`t(p,q)=(p-q) mod 3`; `|f|^2` is ALWAYS triality 0); verify `t(a) == t(b)+t(O) (mod 3)` as a NECESSARY condition only (a passed check does NOT certify nonzero; a failed check proves 0 EXACTLY); route a mismatch through the existing OPERATOR-MISMATCH-DETECTED path. The K=1 corpus calibration (§22) is the S100a W2-2 instance: the plan-w2 chain claimed `<(1,0)| |s(h)|^2 |(1,1)> != 0` via "C^2 in su(3) weight connecting triality-adjacent sectors" -- group-theoretically FALSE (`|s(h)|^2` is triality 0; `1 != 0+0 mod 3` => element 0 exact; the connecting property belongs to `s(h)` in (2,0), not `|s(h)|^2`), caught in-gate at `s100a:36` (audit `871573da...`) / companion `:40`. The rule layer (this gate) and the audit layer (W8a-1's `detect_selection_rule_preflight`) now close the same gap from both sides; the directive names the W8a-1 detector as its enforcement hook, and the run-order guaranteed that hook existed on disk before the directive cited it.

**Substrate framing**: NON-PHONONIC (methodology). The middle layer of the layer-functor F-image `substrate -> methodology -> audit` (`epistemic-discipline.md §Layer-Decomposition`): the fabric's Peter-Weyl sectors are Z_3-graded by the SU(3) center, and center-invariant observables cannot connect mismatched gradings -- an identity OF D_K's representation theory. F maps that substrate-IS identity to this rule-file directive (inadmissible claims are revised at plan-freeze) and onward to the audit detector. Direction substrate-first: the rule encodes what D_K's block structure already IS.

---

"""

SEC_W8B2 = """### §W8b-2. S101-HK-SUFFIX-DISCIPLINE (orchestrator-direct-write)

**Status**: COMPLETED
**Gate ID**: `S101-HK-SUFFIX-DISCIPLINE`
**Trigger**: `[AUDIT]`
**Classification**: **METHODOLOGY** (wave-class, post-allowlist-append; M1-M3 PASS -- M3 is VERBATIM transcription, the strongest form -- M4 ledger row `e7bef692...`) -- NON-PHONONIC (register-citation rule landing)
**Agent**: orchestrator (direct-write; gen-physicist authored the plan block)
**Hypothesis**: The channel-scope suffix discipline -- drafted FINAL by the S100a W-4 D5 adjudication workshop -- lands VERBATIM as a register-citation Extension in `regulator-pin-discipline.md` (the genre file for citation-tagging disciplines), with the W-4 five-surface census as the K=1 corpus calibration.
**Plan reference**: `sessions/session-plan/session-101-plan-w8.md` §W8b-2

**Output Artifacts** (closure-verified on disk):
- `.claude/rules/regulator-pin-discipline.md` -- new `## Extension: Channel-Scope Suffix Discipline for Register Citations of Channel-/Parity-Scoped PERMANENT Theorems (SUGGESTION at K=1)` appended after the existing `:110`/`:136` Extension blocks; 4/4 must_contain present, including the three pinned VERBATIM fragments (`scope inside the citation token itself`, `T-channel S_F^Connes = 0; channel-scoped per S56 W4 Correction 1`, `the K-counter advances on distinct theorems, not repeat citations of S41`). Pre-edit base SHA `4eb42d63...` matched the plan pin.
- `sessions/framework/registry/pru-class-corpus.md` §23 -- 4/4 must_contain present (`Channel-scope suffix discipline`, `five-surface census`, `s100a-w5-d5-seesaw-adjudication-workshop`, `K=1`); both rule + corpus cite the workshop as source (binding-CF gate criterion).
- Shared driver `s101_w8b_methodology_verify.py`; verdict line `S101-HK-SUFFIX-DISCIPLINE: PASS` + dual-SHA companion (no 3-tuple).

**MCP Pre-Compute Audit**: METHODOLOGY-class artifact-existence landing -- no substrate result to pre-close. Query-first confirms a NEW Extension section (no prior channel-scope suffix directive in `regulator-pin-discipline.md`); the cited substrate content (S41 W1-2 T-channel `S_F^Connes = 0`, scoped per S56 W4 Correction 1) is an already-registered PERMANENT theorem, NOT re-adjudicated here. PRE-CLOSED: N/A.

**Verdict**: **PASS** -- `audit_sha256=000b4fc01441e51469eec40e679c05ac92d32cfc4d3f7f70c68aa7b192dbb1bd` `content_sha256=38b34be223df034ef1478499779acf6d28be215311a3f8a30cf424304aadb29e` (drift guard: workshop SHA `d7632f2c...` + housekeeping-100a SHA matched plan pins). scheme=METHODOLOGY-DIRECTIVE-LANDING, convention=DIRECTIVE-ONLY-VERBATIM-TRANSCRIPTION, L_max=N/A.

**Results**: The Extension (SUGGESTION K=1 -> MANDATORY at K=3) requires register-surface citations of channel-/parity-scoped PERMANENT theorems to carry the scope INSIDE the citation token (write `S41 W1-2 (T-channel S_F^Connes = 0; channel-scoped per S56 W4 Correction 1)` -- never bare `S41 W1-2, exact`, never `seesaw = 0`). Structural rationale: separable parentheticals do not survive consolidation/aggregation steps, so scope-inside-the-token makes the over-broad reading non-regenerable from the surviving artifact -- the register-side analog of the contrast-inside-the-output pattern. The K=1 corpus calibration (§23) is the S100a W-4 five-surface census (workshop `s100a-w5-d5-seesaw-adjudication-workshop.md`, SHA `d7632f2c...`; E4 census + V-C6 + the E-3 2/2-escaped-vs-2/2-caught split): of five audited register surfaces, the two that REACHED registers escaped through consolidation steps that dropped the scope parenthetical, the two that carried scope inside the token survived. K-counter advances on DISTINCT channel-/parity-scoped theorems, not repeat citations of S41.

**Substrate framing**: NON-PHONONIC (methodology). F-image: the substrate holds channel-scoped structural facts (the T-channel `S_F^Connes = 0` theorem is a statement about ONE channel of the fabric's seesaw structure, not a bare "seesaw = 0"). F maps that scoping to the methodology invariant "the scope travels INSIDE the citation token" so registry consolidation (an audit-floor operation) cannot strip it and regenerate the over-broad reading. The discipline is the register-side conservation law for substrate scoping content -- substrate-first: it protects the fabric's theorem from documentation-pipeline erosion.

---

"""

SEC_W8B3 = """### §W8b-3. S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION (orchestrator-direct-write)

**Status**: COMPLETED
**Gate ID**: `S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION`
**Trigger**: `[AUDIT]`
**Classification**: **METHODOLOGY** (wave-class, post-allowlist-append; M1-M3 PASS, M4 ledger row `8a58c9ea...`) -- NON-PHONONIC (verdict-schema clarification that COMPOSES WITH, never modifies, the collapse rule)
**Agent**: orchestrator (direct-write; gen-physicist authored the plan block)
**Hypothesis**: A one-paragraph `gate-verdicts.md` clarification -- a plan-frozen R3 gate-block operator takes precedence over the generic schema-v2 composite-collapse on conflict, PROVIDED the producing gate emits a mandatory pre-declared disclosure extra-row -- lands as a directive that COMPOSES WITH (never modifies) the byte-frozen collapse rule, closing the applicability-GUARD gap (INFO-on-inapplicability as a first-class outcome), with W4-1 as the K=1 corpus instance.
**Plan reference**: `sessions/session-plan/session-101-plan-w8.md` §W8b-3

**Output Artifacts** (closure-verified on disk):
- `.claude/rules/gate-verdicts.md` -- new `#### Plan-frozen gate-block operator precedence (applicability guards)` inserted AFTER §Composite-collapse rule (after its Class-3 warning paragraph, before §Auto-shortening); 4/4 must_contain present (`#### Plan-frozen gate-block operator precedence (applicability guards)`, `pre-declared disclosure extra-row`, `applicability is a guard, not the hypothesis`, `COMPOSES WITH the collapse rule; it does not modify it`). **FIREWALL re-verified: the pre-existing composite-collapse pseudo-code block is BYTE-UNCHANGED** (additive-only diff; the verify driver asserts the exact 11-line block survives). Pre-edit base SHA `08659d97...` matched the plan pin.
- `sessions/framework/registry/pru-class-corpus.md` §24 -- 4/4 must_contain present (`Plan-frozen gate-block operator precedence`, `273a0dc45a1e9f2500db5b7548fefed70ab6e7d82c3f4c945dcf9562f945d7ba`, `a hollow PASS was REFUSED`, `§19`).
- Shared driver `s101_w8b_methodology_verify.py`; verdict line `S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION: PASS` + dual-SHA companion + firewall extra-row (no 3-tuple).

**MCP Pre-Compute Audit**: METHODOLOGY-class artifact-existence + byte-invariance landing -- no substrate result to pre-close. Query-first confirms a NEW companion sub-section to the (byte-frozen) composite-collapse rule; corpus §19 (CORE-vs-fringe override) is the adjacent prior on a DIFFERENT axis, cross-linked not duplicated. PRE-CLOSED: N/A.

**Verdict**: **PASS** -- `audit_sha256=7f2ddc488ddeb23500ff2193ed7a8446fb517494c4aaabc98673f7740dec54f5` `content_sha256=9f8ff3df7b2f4dbf9ac165e4bdf4cb6f1e022c24a47c0fe5efea298ba1a7850a`. Firewall: composite-collapse pseudo-code block byte-intact = True. scheme=METHODOLOGY-DIRECTIVE-LANDING, convention=DIRECTIVE-ONLY-COMPOSES-WITH-COLLAPSE, L_max=N/A.

**Results**: The directive (SUGGESTION K=1 -> MANDATORY at K=3) clarifies that when a plan-frozen R3 gate-block operator pre-registers a composite semantic conflicting with the generic collapse, the PLAN-FROZEN operator takes precedence -- PROVIDED the gate emits a mandatory pre-declared `# composite-precedence:` extra-row (naming the plan anchor + the overridden generic-collapse reading) DECLARED before evaluation. It COMPOSES WITH the collapse rule, never modifies it (a precedence invocation without the pre-declared extra-row is a Class-3 boundary violation). Structural gap closed: applicability GUARDS (INFO-on-inapplicability) have no 3-tuple axis -- `regime=BREAKDOWN` is the nearest encoding but forces `composite=FAIL`, which is wrong (applicability is a guard, not the hypothesis). The K=1 corpus calibration (§24) is S100b W4-1 (gate S100b-DK-ERGODICITY, `s100b:56` audit `273a0dc4...`): the 3-tuple `(sign=PASS, magnitude=PASS, regime=MARGINAL)` at `:58` collapses generically to PASS, but the plan-frozen operator pre-registered INFO on Weyl-applicability failure (the guard); the pre-declared extra-row at `:60` disclosed the override -- a hollow PASS was REFUSED in favor of the honest INFO. The byte-frozen collapse pseudo-code block is untouched (modifying it would be the Class-3 violation the directive exists to avoid).

**Substrate framing**: NON-PHONONIC (methodology). F-image: at the substrate layer a criterion's regime-of-validity is a statement about WHERE a functional of D_K's spectrum expresses the continuum structure it certifies (W4-1: whether the truncated heat trace can express the Weyl regime at all). F maps that applicability hypothesis to the methodology distinction "guard vs hypothesis" and onward to the audit-floor extra-row marker. Substrate-first: a verdict label never claims more than the truncated spectral functional actually tested.

---

"""


def main():
    with io.open(WP, "r", encoding="utf-8") as fh:
        text = fh.read()
    new_block = SEC_W8B1 + SEC_W8B2 + SEC_W8B3
    pat = re.compile(r"(?s)### §W8b-1\. S101-HK-SELECTION-RULE-PREFLIGHT-RULE.*?(?=### §W8a-3\. )")
    if not pat.search(text):
        raise SystemExit("FAIL: W8b-1..W8b-3 span not found (anchors drifted)")
    text2 = pat.sub(lambda m: new_block, text, count=1)
    with io.open(WP, "w", encoding="utf-8") as fh:
        fh.write(text2)
    print("WP §W8b-1/2/3 filled; len %d -> %d" % (len(text), len(text2)))


if __name__ == "__main__":
    main()
