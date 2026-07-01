---
name: methodology-rule-authoring-write-denial
description: How to author a standing methodology rule + audit hook as a subagent when .claude/rules/ writes are harness-denied; verdict semantics for METHODOLOGY-class gates with a write-denied leg
metadata:
  type: feedback
---

When a METHODOLOGY-class gate's deliverable set includes a NEW `.claude/rules/*.md` rule file, the subagent harness DENIES the Write/Edit (a hook fires: "Subagents do not write to `.claude/rules/`. Route the edit to the matched corpus file ... `sessions/framework/registry/<topic>-corpus.md`").

**Why:** rule files are orchestrator-only-edit (recursion-attack closure in `methodology-wave-allowlist.md` edit discipline). The hook's stated remedy (route to a corpus file) is for CALIBRATION-CORPUS material, NOT for a rule file that IS a named gate deliverable. Do not silently obey the hook's "route to corpus" when an orchestrator override explicitly directs a RULE-FILE WRITE FALLBACK.

**How to apply:**
- If the spawn prompt carries a RULE-FILE WRITE FALLBACK instruction (it should, for any gate authoring a rule file), write the COMPLETE intended rule-file content VERBATIM into a fenced ```markdown block in your WP section under a heading "RULE-FILE STAGING — for orchestrator application", and FLAG it in your final message for orchestrator application. Never skip the deliverable.
- `.claude/templates/**` and `sessions/framework/*.md` (curated capstone) writes ARE permitted to subagents — only `.claude/rules/**` is denied. So cross-links INTO the rule (from session-housekeeping.md template + capstone §0) land fine; only the rule body itself stages.
- Author the companion audit hook in `computations/_shared/` (allowed) — match the `_pru_cardinality_audit.py` shape: `re.compile` detectors, a `detect_*()` returning a structured dict (has_flag/severity/diagnostic/block_label), `run_*_self_test()` functions for synthetic POSITIVE + NEGATIVE (+ a no-touch/disambiguator case), a `__main__` `--self-test` block printing each + an overall PASS/FAIL, `sys.exit(0 if PASS)`.
- Two-step detector for "session touched X without running the gate": step-1 a TOUCH regex (does the WP reference the governed object?), step-2 the checklist-block regex. Flag iff touch ∧ ¬block. Bound each per-marker DOTALL reach with a max-gap check so one marker's `.*?` doesn't swallow a later unrelated keyword.

**Verdict semantics (METHODOLOGY-class artifact-existence gate with a write-denied leg):**
- Make the producing script's `compute()` check artifact-existence-with-content for EACH deliverable, then branch: if the on-disk-complete legs (hook + self-test + cross-links + JSON) PASS but the rule file is absent ONLY because of the write-denial (staged in WP) → emit **INFO** ("staged for orchestrator application"), NOT PASS and NOT FAIL. A literal PASS is unreachable as a subagent; an optimistic PASS would be the task-complete-lie (`agent-standards.md` Completion Verification). Genuine FAIL is reserved for: rule body PRESENT-but-DIRTY (session IDs in body) OR hook self-test FAILS.
- The verdict `value=` string must report `rule_present=False;...;hook_selftest=PASS;crosslinks_both=True` so the audit trail shows WHY it's INFO (on-disk truth, not a claim).
- This dovetails with the plan's own INFO_meaning for a new rule entering at K=1 (SUGGESTION) — both readings are honest INFO; state both in the WP.

Concurrency note (confirmed S96 W8-3): the template's atomic `with VERDICT_TXT.open("a") as f: f.write(line+companion)` is safe under concurrent same-wave writers — W8-1 and W8-3 both appended to `computations/session-96/s96_gate_verdicts.txt` with zero clobbering. Never read-modify-write the verdict file.
