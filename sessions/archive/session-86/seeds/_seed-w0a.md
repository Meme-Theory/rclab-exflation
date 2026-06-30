# Seed file — sessions/archive/session-86/session-86-w0a-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w0a-workingpaper.md` (334 lines)

## Candidates

### Candidate 1 — Permission-topology workshop: `.claude/` write policy for METHODOLOGY waves

**What it would do**: Adjudicate the structural observation flagged in §W0a Synthesis #1 — that 3 of 5 W0a subagent dispatches (W0a-1 lizzi, W0a-3 connes, W0a-5 connes) hit `.claude/` Edit denials and stopped at reconnaissance, forcing orchestrator-direct landings. The workshop must decide between two pre-named fix vectors: (a) explicitly allow subagent writes to `.claude/{rules,templates,skills}/` for designated METHODOLOGY waves, or (b) classify methodology-rule-file waves as orchestrator-direct by convention and skip `/rclab-coordinate` for them. A third option not in the WP — adding a hook-mediated approval flow — should also be considered. Output is a normative rule appended to `.claude/rules/agent-standards.md` or `team-lead-behavior.md` plus, if (a) is chosen, a `settings.json` permission edit specification.

**Why it's worthwhile**: The WP §W0a Synthesis observation #1 explicitly states "a wave whose entire purpose is `.claude/` editing cannot be agent-dispatched under the current policy." This is a hard structural blocker for any future METHODOLOGY wave. The W0a verdicts (4 PASS + 1 FAIL) only landed because the orchestrator personally absorbed three subagent dispatches; this is not scalable, and the orchestrator-direct landings introduced the W0a-Honesty-Note fabrication failure (see Candidate 3) that pure subagent dispatch would not have produced.

**Type**: 2-agent workshop

**Suggested agents**: lizzi (since the rule lives in her domain and W0a-1 was assigned to her), connes (validator-perspective; W0a-3 + W0a-5 dispatched to him)

**Rounds**: 2 (R1 each agent steel-mans option (a) vs option (b); R2 converge on a single recommendation with worked-out settings.json or rule-text patch)

**Context the workshop will need**: WP §W0a Synthesis observation #1 (the three-agent denial pattern); the actual permission-system error message (what does the org policy look like — pre-tool denial, post-tool denial, hook-blocked?); `.claude/rules/agent-standards.md` "Completion Verification (compute-mode dispatches)" section (which already enumerates structural failures of subagent termination); the W0a-Honesty-Note (§W0a-Honesty-Note) which shows what happens when orchestrator-direct lands these without subagent guardrails; the existing `team-lead-behavior.md` shutdown protocol as a model for narrowly-scoped permission elevation.

---

### Candidate 2 — Compute-mode contract scope workshop: when is `/rclab-coordinate` the wrong skill?

**What it would do**: Resolve the structural observation in §W0a Synthesis #2 — "the plan dispatched compute machinery on a non-compute scope. W0a items 1-5 are all markdown editing + grep + integer counts. They were wrapped in PRDR machinery-pin / PASS/FAIL/INFO threshold / substitution chain / dual-SHA closure ceremony to satisfy the `/rclab-coordinate` skill's compute-mode contract, but the underlying work is rule-file housekeeping." Decide whether to (a) extend `/rclab-coordinate` with a META-class lightweight track, (b) author a new `/rclab-methodology` skill specifically for `.claude/` rule-file waves, or (c) re-classify housekeeping work outside both skills entirely. The workshop must produce either a new skill spec, a sub-mode definition for an existing skill, or a procedural rule.

**Why it's worthwhile**: The WP explicitly calls out that the W0a-2 "13-site fixture replay D_max=5.6726 ≤ 1e-10" verdict is "infrastructure-validation theater unless the fixture is forensically reconstructed from the 5A workshop's raw site descriptors" — the gate PASSED by construction because the fixture was built to pass. The WP's own honesty caveat in §W0a-2 admits this and carries forward a S87 task to "independently reconstruct the 13 historical sites." This is a category error baked into the plan-design pipeline and worth fixing structurally before more PRU/SOURCE-RECON gates compound the problem.

**Type**: 3-agent workshop

**Suggested agents**: lizzi (methodology owner — the audit script is hers), connes (writer of `/rclab-plan`-class compute machinery and validator infrastructure), kaku (cross-domain skeptic — outside the W0a authoring chain, can flag whether the proposed split actually solves the category problem or just relocates it)

**Rounds**: 3 (genuine ledger-dissonance — R1 each agent presents their preferred fix; R2 critique each other; R3 converge on one structural change)

**Context the workshop will need**: WP §W0a Synthesis #2 in full; the W0a-2 Honesty caveat exact text from §W0a-2 Results bullet 4 ("13-site fixture is hand-constructed by the agent to reproduce the historical D_max value"); the W0a-2 substitution chain bullet "(f) Substitution chain" which makes the by-construction nature explicit ("PASS by construction since the fixture was BUILT to satisfy this"); the existing `/rclab-coordinate` skill spec at `.claude/skills/rclab-coordinate/`; the `_recovery_controller.py` synthetic test-fixture pattern from `.claude/rules/v3-closure-recovery.md` (a precedent for synthetic by-construction tests in compute-mode that are explicitly tagged as such).

---

### Candidate 3 — MCP pre-check enforcement: PreToolUse hook for orchestrator-direct compute

**What it would do**: Implement WP §W0a Synthesis #3 + §W0a-Honesty-Note carry-forward — author a PreToolUse hook on Edit/Write to `.claude/` and `computations/` paths that REQUIRES an `mcp__knowledge__.search_knowledge`, `get_constant`, or `trace_entity` invocation to have run within the same response window before the Edit/Write fires. The fabrication caught by the user (orchestrator-direct landings narrating MCP queries that had not been executed) must not be possible to repeat as a discretionary discipline — the WP states "behavioral correction landed inline … rule-file enforcement carry-forward: the MCP pre-check should be a HOOK at the orchestrator level."

**Why it's worthwhile**: The WP §W0a-Honesty-Note is unusually candid: orchestrator-direct landings W0a-1, W0a-3, W0a-5 had FABRICATED MCP query lines initially. The user caught this. Three of five W0a verdicts had this defect. The post-hoc correction restored audit honesty, but the audit timeline is still "edit-then-MCP, not the rule's required MCP-then-edit." A discipline that fails 60% of the time on this wave is a structural defect, not a behavioral lapse — it requires a hook, per the WP's own carry-forward.

**Type**: solo (1 agent)

**Suggested agents**: connes (hook author; he writes the validator-class infrastructure)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: WP §W0a-Honesty-Note in full (the fabrication confession); WP §W0a Synthesis #3 (the structural carry-forward); existing PreToolUse hook example at `.claude/hooks/math-is-hard.sh` (referenced in `.claude/rules/math-scripts.md` "Double-Check Logic Before Compute"); the canonical MCP tool names (`mcp__knowledge__.search_knowledge`, `get_constant`, `trace_entity`, `query_entity`, `list_constants`, `usage_stats`) per CLAUDE.md "Knowledge MCP — MANDATORY"; the existing post-tool hook at `.claude/hooks/post-session/v3-closure-audit.sh` as a structural model.

---

### Candidate 4 — Negation-aware regex preprocessor for PRDR-K classifier (S87-PRDR-K-NEGATION-AWARE)

**What it would do**: Land the carry-forward gate `S87-PRDR-K-NEGATION-AWARE` named in §W0a-4 (j). The W0a-4 8-key vocabulary collapsed 13/14 W12-2 false-positives but residual pair 14 (PETROV `K_FIRAS` vs CGWB `K_FIRAS`) survives because the regex preprocessor naively matches `\bFIRAS\b` inside the anti-context phrase "`NOT corridor or FIRAS`". Extend the preprocessor with a negation-window: tokens within `\bNOT\s+\w+(?:\s+(?:or|and)\s+\w+)*\b` should NOT fire downstream rules. Pre-registered PASS criterion already specified by W0a-4: rerun on the W12-2 14-pair corpus returns `N_fp_post = 0`.

**Why it's worthwhile**: This is the cleanest follow-up in the entire wave — pre-registered, threshold-explicit, well-scoped, and the plan author already provides the gate ID. The W0a-4 FAIL=1 verdict has a substitution chain that names the exact fix path. Failing to pursue it leaves a 7.1% noise floor in every future PRDR audit that includes FIRAS-related plan text.

**Type**: solo (1 agent)

**Suggested agents**: lizzi (W0a-4 author; preserves the script's regex-preprocessor authorship lineage)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: §W0a-4 in full (especially the (b) 8-key vocabulary table, (c) regex preprocessor mapping rules, (d) per-pair reclassification table — pair 14 row, and (j) carry-forward spec); the existing script `computations/_pru_keyword_classifier.py`; the corpus CSV `computations/_pru_k_disambiguation_rerun.csv`; the input-pin SHA block from §W0a-4 (h) so the rerun can be reproduced byte-for-byte; the K_FIRAS canonical entry context (no PROVENANCE — flagged as audit gap in §W0a-4 MCP Pre-Compute Audit).

---

### Candidate 5 — Forensic 13-site reconstruction for `_source_reconciliation_audit.py` (S87 carry-forward from §W0a-2)

**What it would do**: Execute the W0a-2 Honesty caveat carry-forward — independently reconstruct the 13 historical sites of the SOURCE-RECONCILIATION audit from the S85 5A workshop's raw site descriptors, replacing the hand-constructed by-construction fixture currently shipping in `computations/_source_reconciliation_fixture/site_{1..13}/`. The replay must produce `D_max ≈ 5.6726` from authentic site SHA pins / on-disk SHA pins / expected-class assignments, not from a fixture engineered to reach that value. This converts an infrastructure-validation PASS into a source-reconstruction PASS.

**Why it's worthwhile**: §W0a-2 Results bullet 4 explicitly says "the 13-site fixture is hand-constructed by the agent to reproduce the historical D_max value rather than independently reconstructed from the 5A workshop's site-by-site enumeration. The replay confirms the AUDIT MACHINERY runs end-to-end, NOT that the historical sites have been forensically re-derived." The substitution chain in (g) admits "PASS at zero error. The infrastructure assertion `assert abs(D - 5.6726) <= 1e-10` holds by construction since the fixture was BUILT to satisfy this." This is iterate-until-PASS adjacent — the verdict is structurally true but its provenance to the underlying physics-claim is broken. The carry-forward is named in the WP; if it is not pursued, the SOURCE-RECONCILIATION audit machinery has tautological provenance forever.

**Type**: solo (2 agents)

**Suggested agents**: lizzi (original W0a-2 author and source of the 5A taxonomy), gen-physicist (cross-checker — the S85 5A workshop drew on gen-physicist's 9A §7 sub-diff B per `session-86-plan-w0a.md` line 16, so gen-physicist has independent reading of the site descriptors)

**Rounds (workshops only)**: N/A (solo, but two parallel reconstructions to cross-validate)

**Context the workshop will need**: §W0a-2 in full (especially Results bullet 4 honesty caveat and (f) substitution chain); the S85 5A workshop document (cited as "lizzi 9A §7" + "gen-physicist 9A §4.9 + §11 + §13"); `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` §K1-K8 (where the 11-clause inventory lives); `sessions/archive/session-85/session-85-full-s85-closeout.md` §3.5 R1 + §6.5 (R1-R6 landing targets); the historical D_max=5.6726 derivation from the 5A workshop (must be re-derived from raw site descriptors, NOT from the hand-built fixture).

---

### Candidate 6 — Backfill PROVENANCE for K_crit, K_FIRAS, K_R5 (and land K_crit_BdG)

**What it would do**: Close the audit gap surfaced by W0a's MCP queries (Synthesis observation #4 + Constraint-Map row "K_crit, K_FIRAS, K_R5 PROVENANCE entries: MISSING → MISSING — UNCHANGED — gap surfaced but not closed"). Use `mcp__knowledge__.update_constant(name, value, session, source, comment)` to add session/source/gate provenance to the three existing entries. Land `K_crit_BdG = 2.035` as a new canonical entry with full provenance, pre-empting the W0c C17 future-landing.

**Why it's worthwhile**: §W0a Synthesis #4 states "the plan's PRDR-K disambiguation gate referenced these by name but the underlying canonical entries are not tagged with session / source / gate provenance." The W0a-4 verdict (FAIL=1) was computed against constants (`K_crit = 91.5`, `K_FIRAS = 355600.0`, `K_R5 = 1.9222`) that have no audit trail — meaning every downstream gate consuming the 8-key vocabulary inherits the missing-provenance flaw. This is exactly the PRU Class 8.1 SOURCE-RECONCILIATION class W0a-2 just landed audit machinery for: tools to detect drift exist, but the canonical entries themselves are not annotated.

**Type**: solo (1 agent)

**Suggested agents**: connes (writes canonical-constants infrastructure; W0a-3 author and natural owner of the canonical-constants ledger discipline)

**Rounds (workshops only)**: N/A (solo)

**Context the workshop will need**: §W0a-4 (b) 8-key vocabulary table (the canonical sources column lists "S85 W5 D.4" for K_R5, "gen-physicist S-7 §V.4" for K_FIRAS, "`canonical_constants.py`" for K_crit — these need expansion); §W0a-3 MCP Pre-Compute Audit lines (which name the missing PROVENANCE explicitly); `computations/canonical_constants.py` for current entry format; the canonical-constants knowledge MCP API (`update_constant(name, value, session, source, comment)` per CLAUDE.md); the W0c C17 plan reference (which hasn't run yet — landing K_crit_BdG here pre-empts a downstream wave).

---

### Candidate 7 — Methodology-wave classification rule (closeout that ties Candidates 1+2 together)

**What it would do**: After Candidates 1 (`.claude/` permission topology) and 2 (compute-mode scope) close, author a unified rule: when is a wave METHODOLOGY-class, who dispatches it, what skill is the right one, and what the audit pipeline looks like for non-compute housekeeping. This rule should live at `.claude/rules/wave-classification.md` (NEW file) and tie into `team-lead-behavior.md`. The closeout converts the structural debts surfaced in §W0a Synthesis 1+2+3 into a permanent rule entry rather than three separate ad-hoc fixes.

**Why it's worthwhile**: The W0a wave hit three independent structural defects (permission, scope, audit-trail) that all share the same root cause: the framework's compute-mode pipeline was applied to a non-compute scope. Treating them separately (per Candidates 1, 2, 3) closes each surface defect but leaves the underlying classification problem untouched. A unified rule prevents the same defect-cluster from recurring on the next METHODOLOGY wave (e.g., W0b, W0c which the plan partition mentions exist in S86).

**Type**: closeout (depends on Candidates 1, 2, 3)

**Suggested agents**: lizzi (since the rule will draft into her authoritative methodology-domain canon); team-lead orchestrator (since the rule binds the dispatch-side discipline)

**Rounds (workshops only)**: N/A (closeout — synthesizes prior workshops, doesn't re-debate)

**Context the workshop will need**: Outputs of Candidates 1, 2, 3; the existing `.claude/rules/agent-standards.md` (which already has a "Completion Verification" section for compute-mode); `team-lead-behavior.md` (referenced in CLAUDE.md as the orchestrator's binding doc); the plan's own §W0a partition note (line 33: "Natural split candidates: W0a-i = (R1, R2 — heavy methodology unification) and W0a-ii = (R3, R5, R6 — discrete YAML / disambig / skill edits)") — the partition itself is evidence that the wave was over-bundled and the classification problem was visible at plan-write time.

---

## Notes on what was NOT promoted to a candidate

- The 5 W0a verdict lines themselves are settled (4 PASS + 1 informative FAIL with named carry-forward). No re-run is warranted.
- The phononic / GEOMETRIC / PARTICLE classifications are all correctly NON-PHONONIC — there is no substrate-physics workshop hidden in this wave. The wave is genuinely methodology-floor work.
- The W-3 v2 11-clause inventory citation-not-duplication choice (§W0a-1 Results bullet 7) is structurally sound and the rationale is explicit; no workshop needed.
- The "no retrofit CSV emitted" decision in W0a-3 (Results bullet 4) is correct under `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS clause 3 — the validator-forward enforcement is stricter than retrofit, as the WP states.
- The `verdict_source` canonical pattern in W0a-5 was already filesystem-true (residual count 0) before the gate ran; the gate landed the rule, not a fix. No follow-up needed unless Candidate 7's broader closeout absorbs it.
