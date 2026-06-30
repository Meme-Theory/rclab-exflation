# Session 87 Plan — Wave 12: Methodology Validation + MCP Hooks + Audit-Leg

**Generated**: 2026-04-27
**Wave-owner**: `connes-ncg-theorist` (W-13 attribution lead per `connes+lizzi` convention; co-signed by `lizzi-spectral-functional-theorist` on all 7 active gates per S86 W-13 joint-authorship pattern)
**Wave class**: MIXED — gates partition into METHODOLOGY-class (CF-72 validation, CF-75 inversion-validation, CF-76 audit-leg verification, CF-78 13-site reconstruction) + COMPUTE/INFRA-class (CF-73 hook implementation, CF-77 hook promotion) + INFRA-AUDIT-class (CF-74 permission audit) + BOOKKEEPING-only (CF-79). Per `.claude/rules/wave-classification.md` §"NROY clause", the MIXED-class wave is sub-decomposed at the gate-item level (each §W12-N gate carries its own M1-M4 4-tuple in its block); plan-freeze halt avoided via per-gate sub-classification.
**Verdict file**: `computations/s87_gate_verdicts.txt`
**Schema version**: R3 (per `.claude/rules/gate-verdicts.md` S87+ schema-v2 + W9a-99 dual-SHA companion row)
**Total gate count**: 8 (7 active + 1 bookkeeping)
**Specialist mapping**:
  - `connes-ncg-theorist` (PRIMARY): CF-72 (§W12-1), CF-75 (§W12-4), CF-76 (§W12-5), CF-78 (§W12-7)
  - `lizzi-spectral-functional-theorist` (CO-SIGNED on all): CF-72/75/76/78 joint W-13 attribution
  - `gen-physicist` (script-author breadth): CF-73 (§W12-2), CF-77 (§W12-6) infrastructure/hooks; CF-74 (§W12-3) permission audit; CF-79 (§W12-8) bookkeeping orchestration

---

## Wave 12 Summary

| §   | Gate ID                                                  | CF source | Owner               | Wave class       | Effort           | Trigger     |
|:----|:---------------------------------------------------------|:----------|:--------------------|:-----------------|:-----------------|:------------|
| W12-1 | `S87-WAVE-CLASSIFICATION-RULE-VALIDATION`               | CF-72     | connes-ncg + lizzi  | METHODOLOGY      | ~1 wave + 1 review | [VERIFY]   |
| W12-2 | `S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION`                 | CF-73     | gen-physicist       | INFRA-COMPUTE    | ~1 wave; 3-5 disp | [VERIFY]   |
| W12-3 | `S87-SUBAGENT-PERMISSION-AUDIT`                         | CF-74     | gen-physicist       | INFRA-AUDIT      | ~0.5 wave; 2 disp | [AUDIT]    |
| W12-4 | `S87-MCP-DISCIPLINE-INVERSION-VALIDATION`               | CF-75     | connes-ncg + lizzi  | METHODOLOGY      | ~1 wave; ~10 disp | [VERIFY]   |
| W12-5 | `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`              | CF-76     | connes-ncg + lizzi  | METHODOLOGY      | ~1 wave; 3-5 disp | [VERIFY]   |
| W12-6 | `S87-MAX-8-SUBAGENTS-HOOK-PROMOTION`                    | CF-77     | gen-physicist       | INFRA-COMPUTE    | ~0.5 wave; 2 disp | [VERIFY]   |
| W12-7 | `S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION`         | CF-78     | connes-ncg + lizzi  | METHODOLOGY      | ~1 wave; 3-5 disp | [AUDIT]    |
| W12-8 | `S87-2D-LEVEL-LAYER-CORROBORATION`                       | CF-79     | gen-physicist       | BOOKKEEPING-only | implicit/observation | [N/A]   |

---

## Wave 12 Decision Point Prerequisites

Wave 12 dispatches IFF the following S86-close artifacts are available on disk (verified at plan-freeze 2026-04-27; per `feedback_dispatch-discipline.md`, plan prereq notes are planner expectations, not halt-commands):

1. **`.claude/rules/wave-classification.md`** — EXISTS (S86 W-13 RULE-1 landing); 4-test M1-M4 conjunction defined; pre-allocated allowlist at `.claude/rules/methodology-wave-allowlist.md` with 4 W0a rows (S86 R3 closure pre-population). REQUIRED for §W12-1 + §W12-4.
2. **`.claude/rules/methodology-wave-allowlist.md`** — EXISTS; append-only, orchestrator-only edit; 4 S86 W0a rows pre-populated. REQUIRED for §W12-1 (M4 substrate test).
3. **`.claude/rules/v3-closure-recovery.md`** — EXISTS; sig_5 SHA-uniqueness-collision detection wired into Stage-1 remediation map. REQUIRED for §W12-5 (synthetic Class-8-at-audit attack target).
4. **`.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7** — EXISTS (S86 W-13 RULE-2 landing); 5-mapping audit-leg image table pinned. REQUIRED for §W12-5.
5. **`.claude/agent-memory/<orchestrator>/feedback_dispatch-discipline.md`** — EXISTS in user MEMORY.md feedback index; SessionStart hook target. REQUIRED for §W12-6.
6. **`sessions/archive/session-85/workshops/s85-w3-methodology-debts.md`** — EXISTS at S85 close; 5A workshop site-by-site enumeration target for §W12-7. Site count expected: 13 (per CF-78 brief).
7. **`computations/s86_gate_verdicts.txt`** — EXISTS at S86 close; input pin for `audit_sha256` collision-uniqueness verification in §W12-5 synthetic attack.
8. **`.claude/hooks/`** — directory EXISTS; target for `mcp-pre-check.sh` (§W12-2) + `max-8-subagents-session-start.sh` (§W12-6) hook script writes.
9. **S87 first 5-wave methodology corpus** — runtime-resolved at S87 dispatch time; pre-registered as the empirical test corpus for §W12-1 + §W12-4 (specifically: W1a, W1b, W1c, W2, W3 — the W-13 RULE-1 calibration target). If the planning chain produces fewer than 5 methodology-class waves at S87 plan-freeze, the corpus shrinks to the actual count and §W12-1's pass band scales by `n_actual / 5`.

---

## §W12-1. S87-WAVE-CLASSIFICATION-RULE-VALIDATION (CF-72)

**Owner**: `connes-ncg-theorist` PRIMARY; `lizzi-spectral-functional-theorist` CO-SIGNED.
**Wave class**: METHODOLOGY (M1: artifact-existence + count predicate; M2: grep + integer counts; M3: verbatim-extract from `.claude/rules/wave-classification.md`; M4: gate-ID `S87-WAVE-CLASSIFICATION-RULE-VALIDATION` to be appended to `.claude/rules/methodology-wave-allowlist.md` at plan-freeze with `pending` SHA → orchestrator-resolved post-freeze)
**Trigger**: `[VERIFY]`
**Classification**: NON-PHONONIC (rule-file methodology validation; no substrate observable)
**Hypothesis**: The 4-test M1-M4 conjunction defined in `.claude/rules/wave-classification.md` correctly classifies each of the S87 first 5 methodology-corpus waves into METHODOLOGY / COMPUTE / MIXED with all 4 sub-tests passing per gate. Empirical validation that the partition-honest classification is operational, not just specified.

**Pre-registered corpus**: S87 first 5 methodology-corpus waves at S87 dispatch time (resolved at runtime per dependency 9 above). Default expectation: `{W1a, W1b, W1c, W2, W3}`.

**Threshold**:
  - **PASS**: ≥ 4 of 5 waves classified with all 4 sub-tests (M1, M2, M3, M4) passing per gate AND classification result agreeing with the planner's pre-freeze label (recorded in each plan-w{i}.md `Wave class:` header). Composite verdict requires `sign_verdict=PASS` (classification direction matches planner intent) + `magnitude_verdict=PASS` (≥80% match rate across the 5-wave corpus = 4 of 5) + `regime_verdict=VALID` (4-test conjunction is well-defined on each wave's plan-block input — no missing fields).
  - **INFO band**: 3 of 5 waves classified with all 4 sub-tests passing AND ≥ 1 wave's classification disagrees with planner intent in a structurally interpretable way (e.g., MIXED vs pure METHODOLOGY due to a single COMPUTE gate-item; rule-file enforcement catches a plan-author oversight). `magnitude_verdict=INFO`.
  - **FAIL**: ≤ 2 of 5 waves pass all 4 sub-tests OR ≥ 2 classification-disagreements indicate the rule's M1-M4 specification is structurally under-determined. `regime_verdict=BREAKDOWN`.

**Tolerance rule**: ABSOLUTE (integer count of waves passing all 4 sub-tests; no float comparison).

**Machinery pin (PRDR)**:
  - `N_eval`: 5 (corpus size)
  - `L_max`: N/A (rule-file validation; no spectral-truncation parameter)
  - `scan_range`: per-wave plan-block paths `sessions/session-plan/session-87-plan-w{1a,1b,1c,2,3}.md`
  - `step_size`: N/A
  - `tolerance`: integer-count ABSOLUTE; no float epsilon
  - `scheme`: 4-test M1-M4 conjunction per `.claude/rules/wave-classification.md` §M1-M4
  - `convention`: per-wave plan-block input → 4-tuple `(M1, M2, M3, M4)` emission per gate within the wave; aggregate per-wave classification = AND of all gate-level 4-tuples
  - `random_seed`: N/A (deterministic rule-file glob + grep)
  - `GPU path`: N/A (CPU-only string operations)
  - `verifier-rubric (per `.claude/rules/epistemic-discipline.md` §Verifier-Rubric Pre-Registration)`:
    - **Pattern set (M1)**: PASS predicate text matching `/exists.*at path.*P/i` OR `/contains section.*§/i` OR `/substantive_line_count\s*\(\s*§S\s*\)\s*>=?\s*15/` OR `/content_sha256.*matches/i` (disjunction)
    - **Pattern set (M2)**: producing operations restricted to Edit|Write|MultiEdit|grep|wc|sha256; ABSENCE of any `\.py` script with numerical comparison (negative-marker conjunction)
    - **Pattern set (M3)**: provenance text matching `/verbatim sub-diff/i` OR `/verbatim.*workshop/i` OR `/anchor[- ]citation[- ]only/i` (disjunction)
    - **Pattern set (M4)**: gate-ID present in `.claude/rules/methodology-wave-allowlist.md` table (literal SHA-aware grep on `gate_id` column)
    - **Disjunction-vs-conjunction**: M1 disjunction within set; M2 conjunction (presence-of-allowed AND absence-of-forbidden); M3 disjunction; M4 literal membership. Final classification = M1 ∧ M2 ∧ M3 ∧ M4.
    - **Calibration corpus**: the 4 W0a rows in `methodology-wave-allowlist.md` (W0a-1, W0a-2b, W0a-3, W0a-5) are pre-registered as PASSING exemplars; the wave's executor verifies these all pass M1-M4 before scoring the S87 corpus (smoke-test).

**Input SHA-256 pins**:
  - `<computed-at-runtime>` for `sessions/session-plan/session-87-plan-w1a.md`
  - `<computed-at-runtime>` for `sessions/session-plan/session-87-plan-w1b.md`
  - `<computed-at-runtime>` for `sessions/session-plan/session-87-plan-w1c.md`
  - `<computed-at-runtime>` for `sessions/session-plan/session-87-plan-w2.md`
  - `<computed-at-runtime>` for `sessions/session-plan/session-87-plan-w3.md`
  - `<static>` for `.claude/rules/wave-classification.md` (pre-frozen at S86 close)
  - `<static>` for `.claude/rules/methodology-wave-allowlist.md` (pre-frozen at S86 close + 4-row population)

**Expected output 4-tuple**: `(value=<n_pass>/5, scheme=M1-M4-conjunction, convention=per-wave-plan-block-input, L_max=N/A)`

**Substitution chain** (verifier scoring direction):
  Step 1: For wave W ∈ corpus, define `match(W) = [planner_label(W) == classified_label(W)] AND [all 4 sub-tests pass per gate]`.
  Step 2: `n_pass = Σ_{W ∈ corpus} match(W)`.
  Step 3: PASS criterion = `n_pass ≥ 4`; INFO band = `n_pass = 3`; FAIL = `n_pass ≤ 2`.
  Step 4: Direction: monotone in `n_pass`; higher = better classification operational.
  Conclusion: PASS reports the rule operates correctly on the empirical S87 corpus; FAIL reports a structural specification gap.

**What PASS means**: The 4-test M1-M4 conjunction is operational on real S87 plan blocks. Plan-freeze validators (per skill §3e) can rely on the rule for partition-honest classification. Carry-forward: rule promoted from S86 W-13 RULE-1 calibration corpus to permanent operational discipline.

**What FAIL means**: The 4-test conjunction has a structural under-determination — at least one M-test admits multiple readings on the empirical corpus. Solution-space update: the rule needs strengthening (additional pattern-set entries OR explicit conjunction-vs-disjunction tightening). Routes to `S88-WAVE-CLASSIFICATION-RULE-V2-LANDING` carry-forward.

**Producing script**: `computations/s87_w12_wave_classification_rule_validation.py`

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-WAVE-CLASSIFICATION-RULE-VALIDATION
trigger: VERIFY
wave_class: METHODOLOGY
m1_pass: pending  # at-runtime
m2_pass: pending
m3_pass: pending
m4_pass: pending  # gate-ID requires append to methodology-wave-allowlist.md at plan-freeze
```

---

## §W12-2. S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION (CF-73)

**Owner**: `gen-physicist` (script-author breadth; hook-shell + Python integration)
**Wave class**: INFRA-COMPUTE (hybrid: shell hook script + Python self-test; failing M2 due to `.py` self-test, but the test is artifact-existence-of-MCP-query-firing, not numerical-comparison-against-threshold)
**Trigger**: `[VERIFY]`
**Classification**: NON-PHONONIC (infrastructure hook implementation)
**Hypothesis**: A production-grade `.claude/hooks/mcp-pre-check.sh` PreToolUse hook can be implemented per the W-13 C3-CONN-EM-2 4-parameter pin. The hook fires actor-blind (orchestrator + subagent identical), enforces MCP query before MCP-bearing tool calls, and is load-bearing on the Phi(a_4) axis of the layer-functor F.

**Threshold**:
  - **PASS**: hook script `.claude/hooks/mcp-pre-check.sh` exists at non-trivial size (≥30 lines, executable bit set OR Windows-equivalent shebang); `.claude/settings.json` (or `.claude/settings.local.json`) has `hooks.PreToolUse` entry registering the hook with matcher pattern covering `mcp__*` tool names; ≥1 self-test demonstrates the hook fires on an `mcp__*` tool call attempt and emits the canonical pre-check reminder. All 4 C3-CONN-EM-2 parameters verified in self-test output:
    - (1) actor-blind firing: hook output present in BOTH orchestrator-direct and subagent-context test runs
    - (2) PreToolUse trigger: hook fires BEFORE the tool call body executes
    - (3) MCP query enforcement: hook output contains `search_knowledge` / `get_constant` / `trace_entity` reminder text
    - (4) load-bearing on Phi(a_4) axis: hook is registered in the canonical Phi correspondence path per `.claude/rules/epistemic-discipline.md` §"Phi correspondence" weight-4 enforcement-strength
  - **INFO band**: hook script + settings.json registration land but ≤1 of the 4 parameters self-test FAILs (e.g., actor-blind test shows asymmetry; load-bearing-axis test ambiguous).
  - **FAIL**: hook script absent OR ≥2 of 4 parameters fail self-test OR settings.json registration absent.

**Tolerance rule**: THEOREM (artifact-existence + 4-parameter conjunction; binary per parameter)

**Machinery pin (PRDR)**:
  - `N_eval`: 4 (parameter count)
  - `L_max`: N/A
  - `scan_range`: 4-parameter test matrix per C3-CONN-EM-2
  - `step_size`: N/A
  - `tolerance`: parameter-binary-AND
  - `scheme`: shell-hook + Python self-test integration
  - `convention`: actor-blind PreToolUse hook per `.claude/hooks/` precedent (e.g., `math-is-hard.sh`)
  - `random_seed`: N/A
  - `GPU path`: N/A

**Input SHA-256 pins**:
  - `<static>` for `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7 (Phi correspondence weight-4 spec)
  - `<static>` for `.claude/hooks/math-is-hard.sh` (existing PreToolUse hook precedent)
  - `<static>` for `.claude/settings.json` baseline schema
  - `<computed-at-runtime>` for `.claude/hooks/mcp-pre-check.sh` post-write
  - `<computed-at-runtime>` for `.claude/settings.json` post-edit OR `.claude/settings.local.json`

**Expected output 4-tuple**: `(value=<n_params_passing>/4, scheme=actor-blind-PreToolUse, convention=mcp-query-enforcement, L_max=N/A)`

**Substitution chain**:
  Step 1: Define `param_pass(i) = [self-test for parameter i emits expected reminder text]` for i ∈ {1,2,3,4}.
  Step 2: `n_params_passing = Σ_i param_pass(i)`.
  Step 3: PASS = `n_params_passing == 4 AND hook_exists AND settings_registered`.
  Step 4: Direction monotone; PASS iff conjunction holds.

**What PASS means**: The MCP pre-check hook is operational. Orchestrator + subagent MCP-fabrication risk reduced (calls to `mcp__knowledge__*` etc. are gated by a reminder to query first). Phi(a_4) load-bearing axis is structurally complete. Carry-forward to §W12-4 CF-75 inversion-validation rerun under hook-injected mandate.

**What FAIL means**: Hook implementation is non-trivial; either the actor-blind firing pattern doesn't carry over from `math-is-hard.sh` precedent, OR the settings.json schema for PreToolUse matchers needs extension. Routes to `S88-MCP-PRE-CHECK-HOOK-V2` with structural redesign.

**Producing script**: `computations/s87_w12_mcp_pre_check_hook_implementation.py` (Python wrapper that writes the shell hook + edits settings + runs self-test; verdict-line append happens post-self-test)

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION
trigger: VERIFY
wave_class: INFRA-COMPUTE
hook_target: .claude/hooks/mcp-pre-check.sh
settings_target: .claude/settings.json or .claude/settings.local.json
parameter_matrix: [actor-blind, PreToolUse, MCP-query-enforcement, Phi-a4-load-bearing]
```

---

## §W12-3. S87-SUBAGENT-PERMISSION-AUDIT (CF-74)

**Owner**: `gen-physicist` (orchestrator with Read access to `.claude/settings.json` + `.claude/agents/*.md`)
**Wave class**: INFRA-AUDIT (artifact-existence + grep-derived count; methodology-adjacent but not in allowlist — classified COMPUTE-fallthrough with M2-shell-only producing operation; M1 PASS as artifact-existence; M3 PASS as Σ_1 user adjudication outcome verbatim source; M4 FAIL on allowlist absence → routes to COMPUTE-class for verdict-line discipline)
**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (permission-topology audit)
**Hypothesis**: Subagent permission topology under the Σ_1 user-adjudication outcome (memorized in `feedback_framework-hygiene.md` + agent-memory inversion rule per `.claude/rules/agent-standards.md` §AMRI) is correctly reflected in the on-disk `.claude/settings.json` + `.claude/agents/*.md` permission grants. Specifically: (i) subagents are denied Edit / Write / MultiEdit on `.claude/rules/methodology-wave-allowlist.md` (recursion-attack closure); (ii) only the orchestrator (or user direct edit) can append to the allowlist.

**Threshold**:
  - **PASS**: permission audit emits a JSON report with: (a) `methodology-wave-allowlist.md` Edit/Write/MultiEdit denials present in subagent permission specs (or absent from allowlist of allowed paths); (b) `permanent-results-registry.md` + `falsifier-master-inventory.md` + `canonical_constants.py` write-protocols match the documented "one writer per file" + AMRI hygiene; (c) at least 2 dispatches' worth of audit coverage with no permission-topology violations detected.
  - **INFO band**: 1 violation detected, with the violation traceable to a known precedent (e.g., a legacy agent definition missing the allowlist denial); structurally fixable by next-session edit.
  - **FAIL**: ≥2 violations OR a structural gap in permission topology (e.g., the recursion-attack closure rule is enforced by convention only, not by harness configuration).

**Tolerance rule**: THEOREM (audit-output JSON satisfies all 3 sub-criteria)

**Machinery pin (PRDR)**:
  - `N_eval`: subagent count (currently ~14 agents in `.claude/agents/*.md`)
  - `L_max`: N/A
  - `scan_range`: `.claude/agents/*.md` + `.claude/settings.json` + `.claude/settings.local.json`
  - `step_size`: N/A
  - `tolerance`: 3-criterion conjunction
  - `scheme`: grep + JSON-extraction; cross-reference with `.claude/rules/methodology-wave-allowlist.md` §"Edit discipline (recursion-attack closure)"
  - `convention`: permission-topology-as-encoded-on-disk
  - `random_seed`: N/A
  - `GPU path`: N/A

**Input SHA-256 pins**:
  - `<static>` for `.claude/rules/methodology-wave-allowlist.md` (recursion-attack closure spec)
  - `<static>` for `.claude/rules/agent-standards.md` §AMRI (Agent-Memory Registry Inversion)
  - `<computed-at-runtime>` for each of `.claude/agents/*.md`
  - `<computed-at-runtime>` for `.claude/settings.json` + `.claude/settings.local.json`

**Expected output 4-tuple**: `(value=<n_violations>, scheme=permission-topology-grep, convention=on-disk-vs-rule-spec, L_max=N/A)`

**Substitution chain**:
  Step 1: For each agent definition file F ∈ `.claude/agents/*.md`, extract permission grants P(F).
  Step 2: For each protected resource R ∈ {methodology-wave-allowlist.md, permanent-results-registry.md, falsifier-master-inventory.md, canonical_constants.py}, define `violation(F, R) = [P(F) grants Edit/Write/MultiEdit on R AND R has documented one-writer-only or recursion-attack-closure rule]`.
  Step 3: `n_violations = Σ_{F, R} violation(F, R)`.
  Step 4: PASS iff `n_violations == 0`.

**What PASS means**: Permission topology operationalizes the recursion-attack closure (subagents cannot self-promote into the allowlist mid-execution). The Σ_1 user-adjudication outcome is encoded in harness configuration, not just memorized norm.

**What FAIL means**: Permission topology has structural gaps — the recursion-attack closure relies on convention-only enforcement. Routes to `S88-PERMISSION-TOPOLOGY-V2-HARDENING` carry-forward (closes via harness-config edits, not rule-file additions).

**Producing script**: `computations/s87_w12_subagent_permission_audit.py` (reads agent defs + settings; emits JSON audit report; appends verdict line)

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-SUBAGENT-PERMISSION-AUDIT
trigger: AUDIT
wave_class: INFRA-AUDIT
protected_resources:
  - .claude/rules/methodology-wave-allowlist.md
  - sessions/permanent-results-registry.md
  - sessions/framework/registry/falsifier-master-inventory.md
  - computations/canonical_constants.py
sigma_1_user_adjudication: feedback_framework-hygiene.md + AMRI
```

---

## §W12-4. S87-MCP-DISCIPLINE-INVERSION-VALIDATION (CF-75)

**Owner**: `connes-ncg-theorist` PRIMARY; `lizzi-spectral-functional-theorist` CO-SIGNED.
**Wave class**: METHODOLOGY (M1: orchestrator MCP fabrication rate as artifact-existence-of-MCP-query-event predicate; M2: grep on dispatch transcripts; M3: verbatim corpus from §W12-1; M4: gate-ID to be appended to methodology-wave-allowlist.md at plan-freeze with `pending` SHA)
**Trigger**: `[VERIFY]`
**Classification**: NON-PHONONIC (methodology discipline-inversion validation; orchestrator-side MCP discipline)
**Hypothesis**: Under the §W12-2 hook-injected orchestrator mandate (mcp-pre-check.sh active in PreToolUse), orchestrator MCP fabrication rate (calls to `mcp__*` tools without a prior MCP query in the same dispatch transcript) drops to ≤ 5%. This is the empirical corroboration that the hook closes the discipline-inversion failure mode (CLAUDE.md §"Knowledge MCP — MANDATORY for Computation Agents" pre-hook precedent: agents repeatedly rediscover settled results despite the rule existing in text).

**Pre-registered corpus**: same §W12-1 first 5-wave methodology corpus, REPLAYED under hook-injected mandate. Per-dispatch logs scanned for `mcp__*` tool calls; for each call, scan upstream transcript for prior `search_knowledge` / `get_constant` / `trace_entity` / `query_entity` / `list_constants` / `usage_stats` invocation in the same dispatch.

**Threshold**:
  - **PASS**: fabrication rate `f_fab = (mcp_calls_without_prior_query) / (total_mcp_calls) ≤ 0.05` across the corpus. Composite: `sign_verdict=PASS` (hook-injected mandate reduces fabrication rate vs S86 baseline ~50% rough estimate from CLAUDE.md framing); `magnitude_verdict=PASS` (`|f_fab − 0| ≤ 0.05`); `regime_verdict=VALID` (corpus size ≥ 5 waves, hook firing observed in ≥ 80% of dispatches).
  - **INFO band**: `0.05 < f_fab ≤ 0.15`. `magnitude_verdict=INFO`. The hook reduces fabrication but not to PASS-tight band; refinement carry-forward.
  - **FAIL**: `f_fab > 0.15` OR hook-firing rate < 80% (`regime_verdict=BREAKDOWN`).

**Tolerance rule**: ABSOLUTE (rate threshold; bands at 0.05 and 0.15)

**Machinery pin (PRDR)**:
  - `N_eval`: per-corpus dispatch count (estimate ~10 dispatches across the 5-wave corpus per spawn-prompt)
  - `L_max`: N/A
  - `scan_range`: dispatch transcripts at agent JSONL paths (per CLAUDE.md §"Agent Output Monitoring")
  - `step_size`: per-dispatch-binary
  - `tolerance`: rate-band ABSOLUTE
  - `scheme`: hook-firing-confirmation + dispatch-transcript-grep for `mcp__*` calls + upstream-query check
  - `convention`: orchestrator MCP fabrication rate; subagent rate tracked separately as diagnostic
  - `random_seed`: N/A (deterministic transcript scan)
  - `GPU path`: N/A
  - `verifier-rubric`:
    - **Pattern set (mcp_call)**: literal grep on `mcp__knowledge__|mcp__sage__|mcp__oeis__|mcp__paper-search__|mcp__mathscinet__|mcp__zbmath__|mcp__astro__|mcp__madrigal__` tool-name strings in transcript JSONL `tool_use` blocks
    - **Pattern set (prior_query)**: same set, but only `mcp__knowledge__search_knowledge|get_constant|trace_entity|query_entity|list_constants|usage_stats` qualifies as a "query" (not a value-fetch or update); upstream of the candidate `mcp_call` in the SAME dispatch transcript JSONL
    - **Disjunction**: any one of the 6 query subnames present upstream → prior_query satisfied
    - **Negative-marker**: `mcp__knowledge__update_constant` does NOT count as a query (it's a write); fabrication if no read-pattern precedes
    - **Calibration corpus**: a known-good dispatch from S86 W12-4 (mack-cosmic-bridge invoked `mcp__sage__sage_eval` after a documented `search_knowledge` query) is pre-pinned as PASS exemplar

**Input SHA-256 pins**:
  - `<computed-at-runtime>` for `.claude/hooks/mcp-pre-check.sh` (post-§W12-2 PASS)
  - `<computed-at-runtime>` for each dispatch-transcript JSONL in the corpus
  - `<static>` for `.claude/rules/agent-standards.md` (HIGH-DENSITY WORKSHOP TEMPLATE T2-5)
  - `<static>` for CLAUDE.md §"Knowledge MCP — MANDATORY for Computation Agents"

**Expected output 4-tuple**: `(value=f_fab, scheme=hook-injected-mandate, convention=orchestrator-MCP-fabrication-rate, L_max=N/A)`

**Substitution chain**:
  Step 1: Define `mcp_call(d)` = set of `mcp__*` tool calls in dispatch transcript d.
  Step 2: For each c ∈ mcp_call(d), define `has_prior_query(c) = [∃ q in transcript d, q precedes c in time, q ∈ {search_knowledge, get_constant, trace_entity, query_entity, list_constants, usage_stats}]`.
  Step 3: `fab_count(d) = |{c ∈ mcp_call(d) : NOT has_prior_query(c)}|`; `total_count(d) = |mcp_call(d)|`.
  Step 4: `f_fab = (Σ_d fab_count(d)) / (Σ_d total_count(d))`.
  Step 5: PASS iff `f_fab ≤ 0.05`; INFO iff `0.05 < f_fab ≤ 0.15`; FAIL iff `f_fab > 0.15`.
  Step 6: Direction: f_fab decreasing under hook-injected mandate is the expected direction; PASS confirms hook closes the discipline-inversion failure mode.

**Cross-check against §W12-2 dependency**: §W12-4 dispatches IFF §W12-2 closes PASS or INFO. If §W12-2 closes FAIL, §W12-4 closes mechanically per `.claude/rules/mechanical-closure-discipline.md` as `value='PRE-REG-INC_blocked_by_S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION_FAIL'`.

**What PASS means**: The hook-injected MCP discipline mandate closes the orchestrator's fabrication failure mode. Carry-forward: hook becomes permanent infrastructure; methodology-class waves get an artifact-existence-grade discipline guarantee. Layer-functor F's Phi(a_4) axis is empirically validated as load-bearing.

**What FAIL means**: Hook reduces fabrication but not to PASS-band — discipline-inversion is partial. Routes to `S88-MCP-PRE-CHECK-HOOK-V2-STRENGTHENING` with structural redesign of the hook trigger pattern (e.g., HARD-HALT instead of soft-reminder).

**Producing script**: `computations/s87_w12_mcp_discipline_inversion_validation.py`

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-MCP-DISCIPLINE-INVERSION-VALIDATION
trigger: VERIFY
wave_class: METHODOLOGY
upstream_dependency: S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION (W12-2)
mechanical_closure_rule: .claude/rules/mechanical-closure-discipline.md
fab_rate_thresholds: {pass: 0.05, info_ceiling: 0.15}
```

---

## §W12-5. S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION (CF-76)

**Owner**: `connes-ncg-theorist` PRIMARY; `lizzi-spectral-functional-theorist` CO-SIGNED.
**Wave class**: METHODOLOGY (M1: synthetic attack artifact-existence + sig_5 firing predicate; M2: Python attack script + grep on v3 ladder JSON; M3: verbatim 5-mapping table from `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7; M4: gate-ID `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` allowlist append at plan-freeze)
**Trigger**: `[VERIFY]`
**Classification**: NON-PHONONIC (audit-layer F-image empirical corroboration)
**Hypothesis**: The audit-leg image of the layer-functor F (per `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7 second table) preserves PRU-class invariants. Specifically: a synthetic Class-8-at-audit attack — an audit script with a hardcoded SHA matching a different canonical audit's SHA — induces v3-closure-recovery sig_5 firing per `.claude/rules/v3-closure-recovery.md` Per-signal remediation map. The triplet F (substrate ↔ methodology ↔ audit) extends from pair-verified to triplet-verified.

**Threshold**:
  - **PASS**: synthetic Class-8-at-audit attack produces a duplicate `audit_sha256` in the test verdict file; v3 ladder audit (`v3-closure-audit.sh` or `_recovery_controller.py --self-test`) detects the duplication; sig_5 fires; Stage-1 remediation per the per-signal map invokes (flag offending gate for SHA-hardcoding-bug review, attempt fix, rerun). PASS = sig_5 firing observed AND duplicate detected with correct gate-ID in the audit log.
  - **INFO band**: sig_5 fires but the Stage-1 remediation map's automatic-fix branch produces an inconsistent SHA on rerun (i.e., the synthetic attack exposes a remediation-side bug that doesn't invalidate sig_5 but flags refinement work).
  - **FAIL**: sig_5 does NOT fire OR the v3 ladder reports CLOSED despite the synthetic duplicate (audit-leg F-image is NOT preserving PRU-class invariants — the layer-functor's triplet-extension claim is structurally broken).

**Tolerance rule**: THEOREM (sig_5 firing is binary; duplicate detection is binary)

**Machinery pin (PRDR)**:
  - `N_eval`: 1 (one synthetic attack scenario)
  - `L_max`: N/A
  - `scan_range`: `computations/s87_gate_verdicts.txt` (synthetic test copy at `computations/_test_layer_functor_audit_leg_verdicts.txt`)
  - `step_size`: N/A
  - `tolerance`: 2-criterion conjunction (sig_5 fires AND duplicate detected)
  - `scheme`: synthetic Class-8-at-audit injection per W-13 RULE-2 audit-layer 5-mapping table
  - `convention`: SHA-hardcoding bug analog at audit layer (per `.claude/rules/v3-closure-recovery.md` sig_5 description)
  - `random_seed`: 42 (for synthetic SHA payload generation; reproducible)
  - `GPU path`: N/A
  - `attack_specification`:
    - Construct test verdict file with 2 canonical lines for distinct gate-IDs sharing identical 64-char `audit_sha256` (force the bug)
    - Invoke `_recovery_controller.py --self-test --target-file <test_file>` OR `v3-closure-audit.sh` on the test file
    - Capture sig_5 firing event from `recovery_iteration_log.json` AND `completion-queue.jsonl` Stage_1 entry
    - Verify the offending gate-IDs are correctly named in the audit output

**Input SHA-256 pins**:
  - `<static>` for `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7
  - `<static>` for `.claude/rules/v3-closure-recovery.md` (sig_5 spec)
  - `<static>` for `computations/_recovery_controller.py`
  - `<static>` for `.claude/hooks/post-session/v3-closure-audit.sh`
  - `<computed-at-runtime>` for synthetic test verdict file

**Expected output 4-tuple**: `(value=<sig_5_fired_AND_duplicate_detected>, scheme=synthetic-Class-8-at-audit, convention=audit-leg-F-image, L_max=N/A)`

**Substitution chain**:
  Step 1: Define synthetic attack payload P = (gate_id_1, gate_id_2, shared_audit_sha256) with gate_id_1 ≠ gate_id_2.
  Step 2: Inject P into test verdict file T.
  Step 3: Run v3 ladder audit on T; capture (sig_5_fired, duplicate_detected) ∈ {0,1}^2.
  Step 4: PASS iff `sig_5_fired AND duplicate_detected`.
  Step 5: Direction: triplet-extension of F preserves PRU-class invariants AT AUDIT LAYER iff synthetic attack induces correct ladder response.

**Cross-link**: per `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" §"Mandatory caveat (C3-CONN-CONV-3)" — this gate is the S87 audit-leg verification step. PASS upgrades F from pair-verified to triplet-verified.

**What PASS means**: The layer-functor F triplet (substrate ↔ methodology ↔ audit) is empirically corroborated. PRU Class-8 sub-taxonomy (8.0/8.1/8.2/8.3) is preserved across all three layers. The Phi correspondence weight-2/4 enforcement-strength image is structurally complete at the audit layer.

**What FAIL means**: Triplet extension is broken — audit-layer F-image does NOT preserve PRU invariants. Possible structural causes: (i) sig_5 spec under-determines what counts as a duplicate (e.g., 16-char vs 64-char prefix); (ii) Stage-1 remediation has a code path that suppresses the sig_5 firing under specific synthetic patterns. Routes to `S88-V3-LADDER-SIG5-SPEC-V2` carry-forward.

**Producing script**: `computations/s87_w12_layer_functor_audit_leg_verification.py`

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION
trigger: VERIFY
wave_class: METHODOLOGY
synthetic_attack_class: Class-8-at-audit (SHA-hardcoding-bug analog)
target_signal: sig_5 (v3-closure-recovery.md)
triplet_status_target: pair-verified -> triplet-verified
```

---

## §W12-6. S87-MAX-8-SUBAGENTS-HOOK-PROMOTION (CF-77)

**Owner**: `gen-physicist` (script-author breadth; SessionStart hook + agent-memory edit)
**Wave class**: INFRA-COMPUTE (hook script + reminder-injection self-test; non-numerical-comparison; classified COMPUTE-fallthrough due to `.py` script presence on the implementation side)
**Trigger**: `[VERIFY]`
**Classification**: NON-PHONONIC (orchestrator dispatch-discipline hook)
**Hypothesis**: The `feedback_dispatch-discipline.md` memorized-norm (per user MEMORY.md: "SELF-IMPOSE ≤~8 concurrent agents every session... User corrects this EVERY session — the rule is self-imposition, not correction-response") can be promoted from a memorized feedback rule into a prompt-encoded ritual via SessionStart hook. The hook fires on session start and injects a "≤8 concurrent agents" reminder into the orchestrator's first-turn context.

**Threshold**:
  - **PASS**: SessionStart hook script exists at `.claude/hooks/max-8-subagents-session-start.sh` (or .bat / .py per harness-conventions); `.claude/settings.json` registers it on the SessionStart event; ≥1 self-test confirms the reminder text appears in the orchestrator's first-turn additionalContext (per the `<system-reminder>` injection pattern observed in this session's spawn). Reminder text MUST contain "≤8 concurrent" or equivalent literal token.
  - **INFO band**: hook fires but reminder text is delivered via a non-canonical path (e.g., as agent-memory pre-load instead of SessionStart system-reminder); structurally functional but bypasses the standard hook channel.
  - **FAIL**: hook absent OR fires but reminder text not present in orchestrator first-turn context.

**Tolerance rule**: THEOREM (artifact-existence + reminder-text-detection conjunction)

**Machinery pin (PRDR)**:
  - `N_eval`: 1 (one self-test per dispatch event)
  - `L_max`: N/A
  - `scan_range`: SessionStart hook output text in orchestrator first-turn context
  - `step_size`: N/A
  - `tolerance`: text-presence-binary
  - `scheme`: SessionStart hook injection per `.claude/hooks/post-session/` precedent (existing hooks: `v3-closure-audit.sh` is PostSession; analog for SessionStart)
  - `convention`: literal token "≤8 concurrent" OR "max 8 subagents" OR "self-impose 8 cap" presence in injected context
  - `random_seed`: N/A
  - `GPU path`: N/A

**Input SHA-256 pins**:
  - `<static>` for user MEMORY.md `feedback_dispatch-discipline.md` content (verifiable via Read tool on `C:\Users\ryan\.claude\projects\C--sandbox-Ainulindale-Exflation\memory\feedback_dispatch-discipline.md`)
  - `<static>` for `.claude/hooks/post-session/v3-closure-audit.sh` (PostSession hook precedent)
  - `<static>` for `.claude/settings.json` baseline schema for `hooks.SessionStart` event registration
  - `<computed-at-runtime>` for `.claude/hooks/max-8-subagents-session-start.sh` post-write
  - `<computed-at-runtime>` for `.claude/settings.json` post-edit

**Expected output 4-tuple**: `(value=<reminder_text_detected>, scheme=SessionStart-hook-injection, convention=literal-token-grep, L_max=N/A)`

**Substitution chain**:
  Step 1: Define `hook_fires(s) = [SessionStart event triggers script execution]` for session-start event s.
  Step 2: Define `reminder_present(s) = [orchestrator first-turn context contains literal token from {"≤8 concurrent", "max 8 subagents", "self-impose 8 cap"}]`.
  Step 3: PASS iff `hook_fires(s) AND reminder_present(s)`.
  Step 4: Direction: hook-fires + reminder-present is the artifact-existence chain; PASS iff conjunction holds.

**What PASS means**: The user-correction-every-session pattern (max-8-subagents) is closed at the harness level. Orchestrator no longer relies on agent-memory recall to self-impose the cap; the rule is structurally encoded in session-start ritual. Carry-forward to `S88-OTHER-FEEDBACK-RULE-HOOK-PROMOTIONS` (e.g., `feedback_fix-in-session-never-defer.md`, `feedback_no-master-gate-tally.md` evaluated for similar promotion).

**What FAIL means**: SessionStart hook channel doesn't deliver injected text into the orchestrator's first-turn `<system-reminder>` block — harness limitation. Routes to `S88-SESSIONSTART-HOOK-PROTOCOL-V2` with alternative injection mechanism (agent-memory pre-load OR settings.json `additionalContext` static text).

**Producing script**: `computations/s87_w12_max_8_subagents_hook_promotion.py`

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-MAX-8-SUBAGENTS-HOOK-PROMOTION
trigger: VERIFY
wave_class: INFRA-COMPUTE
hook_target: .claude/hooks/max-8-subagents-session-start.sh
hook_event: SessionStart
literal_token_set: ["≤8 concurrent", "max 8 subagents", "self-impose 8 cap"]
```

---

## §W12-7. S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION (CF-78)

**Owner**: `connes-ncg-theorist` PRIMARY; `lizzi-spectral-functional-theorist` CO-SIGNED.
**Wave class**: METHODOLOGY (M1: artifact-existence of 13 reconstructed-site entries with matching canonicals predicate; M2: grep + Read-only on S85 5A workshop notes + cross-check on canonical_constants.py; M3: verbatim site-by-site enumeration from S85 5A workshop §K1-K8; M4: gate-ID `S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION` allowlist append at plan-freeze)
**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (audit-output reconstruction; methodology-grade)
**Hypothesis**: The 13 historical sites enumerated in the S85 5A workshop site-by-site corpus (per `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` §K1-K8 + the 5A G3/G4 sub-diff atom enumeration; see `.claude/templates/pru-pre-registration-template.md` §"PRDR keyword window" for the K-family specialization) can be independently reconstructed by a separate read-pass over the S85 5A workshop notes WITHOUT consulting any S86 or S87 derivative documents.

**Threshold**:
  - **PASS**: 13 of 13 sites reproduced with matching canonical corrections AND matching provenance (each site = (S85 5A bare-K window finding + canonical correction + provenance) tuple). Match = literal SHA equality on the canonical_constants.py value at S85-close OR documented-discrepancy with traceable migration-ledger row.
  - **INFO band**: 11-12 of 13 sites reproduced; ≤ 2 sites have provenance drift from S85-close to S87 entry (e.g., a canonical_constants.py value updated in S86; reconstruction reflects S87 value; site-finding remains structurally identical).
  - **FAIL**: ≤ 10 of 13 sites reproduced OR ≥ 3 site-findings differ structurally from S85 5A workshop's enumeration.

**Tolerance rule**: ABSOLUTE (integer count of reconstructed sites + provenance match)

**Machinery pin (PRDR)**:
  - `N_eval`: 13 (site count per CF-78 brief)
  - `L_max`: N/A
  - `scan_range`: `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` §K1-K8 + 5A G3/G4 sub-diff
  - `step_size`: per-site
  - `tolerance`: integer-count + provenance-match conjunction
  - `scheme`: independent-read-and-reconstruct (Stage-2 cross-check protocol per `.claude/rules/joint-theorem-promotion.md` §Stage 2; reconstructor must NOT have read S86 W-13 syntheses prior to dispatch)
  - `convention`: site-tuple = (S85 5A bare-K window finding string, canonical correction value, provenance citation)
  - `random_seed`: N/A (deterministic read-pass)
  - `GPU path`: N/A
  - `independence-protocol`: dispatched agent receives ONLY (i) the S85 5A workshop notes file path, (ii) the empty 13-row reconstruction template, (iii) read access to `computations/canonical_constants.py` for canonical lookups. Agent MUST NOT receive any S86 W-13 synthesis files OR `compute-carryforward.md` site-list.

**Input SHA-256 pins**:
  - `<static>` for `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md`
  - `<static>` for `.claude/templates/pru-pre-registration-template.md` §"PRDR keyword window"
  - `<computed-at-runtime>` for `computations/canonical_constants.py` (per-site canonical lookup)
  - `<static>` for `.claude/rules/joint-theorem-promotion.md` §Stage 2 (independence-protocol substrate)

**Expected output 4-tuple**: `(value=<n_sites_reproduced>/13, scheme=independent-read-reconstruct, convention=site-tuple-canonical-match, L_max=N/A)`

**Substitution chain**:
  Step 1: For each of 13 sites s_i in S85 5A enumeration, the reconstructor produces a tuple T_i = (finding_string, canonical_value, provenance).
  Step 2: Cross-check T_i against S85 5A canonical T_i^ref via literal match on finding_string + SHA equality on canonical_value (with migration-ledger tolerance for S85→S87 value updates) + provenance citation match.
  Step 3: `n_reproduced = Σ_i [match(T_i, T_i^ref)]`.
  Step 4: PASS iff `n_reproduced >= 13`; INFO iff `11 <= n_reproduced <= 12`; FAIL iff `n_reproduced <= 10`.
  Step 5: Direction: monotone in `n_reproduced`; PASS confirms independence-of-reconstruction substrate.

**What PASS means**: The S85 5A workshop's site-by-site enumeration is structurally robust under independent reconstruction — the 13 sites are not workshop-context-dependent. Carry-forward: the 5A G3/G4 sub-diff atom enumeration is registry-grade, not workshop-only. Promotes the 5A enumeration from workshop-internal to session-canonical.

**What FAIL means**: Reconstruction-independence fails — the S85 5A enumeration relies on workshop-context cues that don't survive independent re-reading. Routes to `S88-S85-5A-ENUMERATION-V2-LANDING` carry-forward (re-canonicalize the enumeration with explicit per-site provenance pins).

**Producing script**: `computations/s87_w12_w0a_2a_independent_13_site_reconstruction.py`

**Dispatch protocol**: orchestrator dispatches the reconstructor agent (connes-ncg-theorist or lizzi-spectral-functional-theorist) with the dispatch prompt EXPLICITLY excluding S86 W-13 syntheses and `compute-carryforward.md` site-list per `.claude/rules/joint-theorem-promotion.md` §Stage 2 independence-protocol.

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION
trigger: AUDIT
wave_class: METHODOLOGY
site_count: 13
independence_protocol: joint-theorem-promotion.md Stage 2
forbidden_dispatch_inputs: [session-86/session-86-w13-*, compute-carryforward.md site-list section]
```

---

## §W12-8. S87-2D-LEVEL-LAYER-CORROBORATION (CF-79; bookkeeping only)

**Owner**: `gen-physicist` (orchestrator-side bookkeeping; no specialist dispatch)
**Wave class**: BOOKKEEPING-only (M1: N/A — no PASS predicate beyond existence-of-tracking-artifact; M2: N/A; M3: N/A; M4: NOT in allowlist; classified outside the M1-M4 conjunction per `feedback_fix-in-session-never-defer.md` distinction between hygiene and carry-forward)
**Trigger**: `[N/A]` (no compute slot at S87; observation-only)
**Classification**: NON-PHONONIC (forward-tracking artifact)
**Hypothesis**: 2D Scope × Layer corroboration + CategoricalDual pattern propagation tracking is observation-only at S87. M_meta candidates emerge from §W12-1 + §W12-4 + §W12-5 outputs as side-effects; tracked but not separately computed.

**Threshold**: NONE (no compute slot; artifact-existence-only)
  - **PASS predicate (degenerate)**: a tracking note appears in the W12 working-paper section §W12-8 enumerating any M_meta candidates surfaced by W12-1/4/5 outputs.
  - **INFO/FAIL**: not applicable; pure bookkeeping.

**Tolerance rule**: N/A (no numerical comparison)

**Machinery pin (PRDR)**: N/A — bookkeeping per `.claude/rules/epistemic-discipline.md` §"What Does NOT Count as Evidence" item: this is hygiene, not a result. Per `feedback_fix-in-session-never-defer.md`, this is logged in-session and propagated as a planning input to S88 (not a compute carry-forward).

**Input SHA-256 pins**:
  - `<computed-at-runtime>` for §W12-1, §W12-4, §W12-5 verdict-line outputs (post-PASS/INFO/FAIL of those gates)

**Expected output 4-tuple**: N/A — no verdict line emission required; instead, a working-paper section §W12-8 entry naming any M_meta candidate observed.

**Substitution chain**: N/A (no direction claim)

**What PASS means** (degenerate): the W12 working paper has §W12-8 entry; M_meta candidates carried forward into S88 planning input.

**What FAIL means** (degenerate): §W12-8 entry missing from working paper; carry-forward to S88 W0 hygiene fix.

**Producing script**: NONE — orchestrator writes §W12-8 directly into the W12 working paper at session-end synthesis.

**YAML**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt  # no verdict line emission for §W12-8; per .claude/rules/mechanical-closure-discipline.md, bookkeeping items are NOT mechanically closed (they are not compute gates with upstream-blocked predicates)
gate_id: S87-2D-LEVEL-LAYER-CORROBORATION
trigger: N/A
wave_class: BOOKKEEPING-only
m_meta_candidates_source: [§W12-1 outputs, §W12-4 outputs, §W12-5 outputs]
forward_propagation: S88 planning input (not S87 compute carry-forward)
```

---

## Wave 12 → Wave 13 Decision Point

Wave 12 closes when all 7 active gates (W12-1..W12-7) emit verdict lines (PASS / INFO / FAIL or PRE-REG-INC mechanical closure per `.claude/rules/mechanical-closure-discipline.md`) AND §W12-8 working-paper bookkeeping entry is written. Decision routing for downstream waves:

1. **§W12-1 PASS** → wave-classification rule operational; W13+ planners may rely on M1-M4 conjunction at plan-freeze. **§W12-1 FAIL** → carry-forward `S88-WAVE-CLASSIFICATION-RULE-V2-LANDING`.

2. **§W12-2 PASS** → §W12-4 dispatches under hook-injected mandate (canonical path). **§W12-2 FAIL** → §W12-4 mechanically closes per `.claude/rules/mechanical-closure-discipline.md` with `value='PRE-REG-INC_blocked_by_S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION_FAIL'`; carry-forward `S88-MCP-PRE-CHECK-HOOK-V2`.

3. **§W12-3 PASS** → permission topology audit-validated; recursion-attack closure operational at harness level. **§W12-3 INFO/FAIL** → carry-forward `S88-PERMISSION-TOPOLOGY-V2-HARDENING`.

4. **§W12-4 PASS** → MCP discipline-inversion empirically corroborated; layer-functor F's Phi(a_4) axis load-bearing confirmed at empirical level. **§W12-4 INFO/FAIL** → carry-forward `S88-MCP-PRE-CHECK-HOOK-V2-STRENGTHENING`.

5. **§W12-5 PASS** → layer-functor F upgraded from pair-verified to triplet-verified; PRU Class-8 sub-taxonomy preserved across all three layers. **§W12-5 FAIL** → carry-forward `S88-V3-LADDER-SIG5-SPEC-V2`.

6. **§W12-6 PASS** → max-8-subagents pattern closed at SessionStart hook level; user no longer corrects every session. **§W12-6 INFO/FAIL** → carry-forward `S88-SESSIONSTART-HOOK-PROTOCOL-V2`.

7. **§W12-7 PASS** → S85 5A enumeration registry-grade; reconstruction-independence substrate confirmed. **§W12-7 INFO/FAIL** → carry-forward `S88-S85-5A-ENUMERATION-V2-LANDING`.

8. **§W12-8 entry present** → M_meta candidates tracked into S88 planning input. **§W12-8 entry absent** → carry-forward S88 W0 hygiene fix (NOT a compute carry-forward per `feedback_fix-in-session-never-defer.md`).

---

## Wave 12 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR clause: every gate-relevant machinery parameter is enumerated below at the wave level. Per-gate pins are repeated in each §W12-N block above.

| Parameter | Wave-level value | Per-gate variation |
|:----------|:----------------|:-------------------|
| `N_eval` | varies | W12-1: 5 (corpus size); W12-2: 4 (parameter count); W12-3: ~14 (agent count); W12-4: ~10 (dispatch count); W12-5: 1 (synthetic attack); W12-6: 1 (self-test); W12-7: 13 (site count); W12-8: N/A |
| `L_max` | N/A across all gates | rule-file/methodology validation; no spectral-truncation parameter |
| `scan_range` | per-gate (see blocks above) | path globs / corpus enumerations / synthetic-attack payloads |
| `step_size` | per-gate (see blocks above) | per-wave / per-dispatch / per-site / per-parameter |
| `tolerance` | THEOREM (binary conjunctions) on W12-2/3/5/6; ABSOLUTE (integer count or rate band) on W12-1/4/7 | see per-gate blocks |
| `scheme` | per-gate (see blocks above) | M1-M4 conjunction / actor-blind PreToolUse / permission-topology-grep / hook-injected mandate / synthetic Class-8 / SessionStart hook / independent-read-reconstruct |
| `convention` | per-gate (see blocks above) | per-wave-plan-block / mcp-query-enforcement / on-disk-vs-rule-spec / orchestrator-MCP-fabrication-rate / audit-leg-F-image / literal-token-grep / site-tuple-canonical-match |
| `random_seed` | 42 only on W12-5 (synthetic SHA payload generation); N/A elsewhere | deterministic operations otherwise |
| `GPU path` | N/A across all gates | rule-file methodology + hook implementation; no spectral computation |
| `verifier-rubric` | per-gate (W12-1, W12-4 explicit rubrics; W12-7 independence-protocol; W12-2, W12-5, W12-6 artifact-existence binaries) | calibration corpus per gate where applicable |

**PRU cardinality pre-flight**: all 8 gates have machinery pins enumerated. PRU `D_PRU_raw = 0` expected at plan-freeze validation.

**SOURCE-RECON pre-flight**: no canonical_constants.py pins consumed numerically (rule-file/methodology); SOURCE-RECON 5+1-class taxonomy emits NO-ACTION default. Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL not applicable (no substrate observable).

**SUBSTRATE-FIRST-PROVENANCE pre-flight**: no substrate observables consumed; rule applies vacuously. NO-ACTION.

**Wave-classification 4-test conjunction (M1-M4) at plan-freeze** (self-application of the rule being validated; per `.claude/rules/wave-classification.md` self-classification at plan-freeze):

| Gate | M1 PASS predicate type | M2 producing-op | M3 source-of-truth | M4 allowlist | Resulting class |
|:-----|:------------|:----|:----|:-------|:----|
| W12-1 | artifact-existence + count | shell + grep | verbatim wave-classification.md | append at freeze | METHODOLOGY |
| W12-2 | artifact-existence + 4-param | Python + shell hook | verbatim epistemic-discipline.md §Layer-Decomposition | not in allowlist (script present) | INFRA-COMPUTE |
| W12-3 | artifact-existence + count | grep + JSON | verbatim AMRI rule | not in allowlist | INFRA-AUDIT |
| W12-4 | rate threshold (artifact-existence-of-MCP-query-event) | Python transcript scan | verbatim §W12-1 corpus | append at freeze | METHODOLOGY |
| W12-5 | artifact-existence + sig_5 firing | Python synthetic attack | verbatim v3-closure-recovery.md sig_5 | append at freeze | METHODOLOGY |
| W12-6 | artifact-existence + token grep | Python + shell hook | verbatim feedback_dispatch-discipline.md | not in allowlist (script present) | INFRA-COMPUTE |
| W12-7 | count + provenance match | grep + Read | verbatim S85 5A workshop notes | append at freeze | METHODOLOGY |
| W12-8 | bookkeeping degenerate | none | hygiene-only | not in allowlist | BOOKKEEPING-only |

Allowlist appendage targets at plan-freeze (orchestrator-only edit per `.claude/rules/methodology-wave-allowlist.md` §"Edit discipline"):

| gate_id | session | rationale | sha256_of_plan_block |
|:--------|:--------|:----------|:--------------------|
| W12-1 | S87 | S87-WAVE-CLASSIFICATION-RULE-VALIDATION (M1-M4 4-test empirical validation on first 5 methodology-class waves) | pending |
| W12-4 | S87 | S87-MCP-DISCIPLINE-INVERSION-VALIDATION (orchestrator MCP fabrication rate measurement under hook-injected mandate) | pending |
| W12-5 | S87 | S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION (synthetic Class-8-at-audit attack inducing v3-closure-recovery sig_5 firing) | pending |
| W12-7 | S87 | S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION (independent reconstruction of S85 5A workshop 13-site enumeration under joint-theorem-promotion.md §Stage 2 protocol) | pending |

**PRDR machinery dry-run** (per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR sub-clause): producing scripts for W12-1/2/3/4/5/6/7 each enumerate their free parameters (corpus paths, hook script paths, agent-def paths, transcript paths, synthetic SHA payloads, token sets, site-list paths) per the per-gate Machinery pin (PRDR) blocks above. No mid-execution parameter introduction expected.

---

## Wave 12 Input-SHA Ledger

Static input SHAs (frozen at S86-close; computed at plan-freeze 2026-04-27):

| File | Status | Used by |
|:-----|:------|:--------|
| `.claude/rules/wave-classification.md` | static | W12-1, W12-4 (corpus self-classification) |
| `.claude/rules/methodology-wave-allowlist.md` | static (4 W0a rows pre-populated) | W12-1 (M4 substrate test), W12-4/5/7 (allowlist append targets) |
| `.claude/rules/v3-closure-recovery.md` | static | W12-5 (sig_5 spec) |
| `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7 | static | W12-2 (Phi(a_4) load-bearing axis spec), W12-5 (5-mapping audit-leg image table) |
| `.claude/rules/mechanical-closure-discipline.md` | static | W12-4 (mechanical closure if W12-2 FAILs), W12-8 (NOT applicable per BOOKKEEPING classification) |
| `.claude/rules/joint-theorem-promotion.md` §Stage 2 | static | W12-7 (independence-protocol substrate) |
| `.claude/rules/agent-standards.md` §AMRI | static | W12-3 (permission-topology audit substrate) |
| `.claude/templates/pru-pre-registration-template.md` §"PRDR keyword window" | static | W12-7 (5A G3/G4 sub-diff atom enumeration substrate) |
| `.claude/hooks/math-is-hard.sh` | static | W12-2 (PreToolUse hook precedent) |
| `.claude/hooks/post-session/v3-closure-audit.sh` | static | W12-5 (v3 ladder audit invocation), W12-6 (PostSession hook precedent for SessionStart hook design) |
| `computations/_recovery_controller.py` | static | W12-5 (--self-test invocation target) |
| `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` | static | W12-7 (13-site enumeration source) |
| `computations/canonical_constants.py` | static (S86-close state) | W12-7 (per-site canonical lookup; agent reads at runtime, value at S87-entry pinned) |
| `computations/s86_gate_verdicts.txt` | static (S86-close state) | W12-5 (input pin for synthetic-attack baseline; collision-uniqueness baseline) |
| `CLAUDE.md` §"Knowledge MCP — MANDATORY" | static | W12-4 (rule-text source for the discipline being validated) |

Runtime-computed SHAs:

| File | Computed when |
|:-----|:--------------|
| `sessions/session-plan/session-87-plan-w1a.md` | at W12-1/W12-4 dispatch (corpus member 1) |
| `sessions/session-plan/session-87-plan-w1b.md` | at W12-1/W12-4 dispatch (corpus member 2) |
| `sessions/session-plan/session-87-plan-w1c.md` | at W12-1/W12-4 dispatch (corpus member 3) |
| `sessions/session-plan/session-87-plan-w2.md` | at W12-1/W12-4 dispatch (corpus member 4) |
| `sessions/session-plan/session-87-plan-w3.md` | at W12-1/W12-4 dispatch (corpus member 5) |
| `.claude/hooks/mcp-pre-check.sh` | at W12-2 post-write |
| `.claude/hooks/max-8-subagents-session-start.sh` | at W12-6 post-write |
| `.claude/settings.json` (or `.claude/settings.local.json`) | at W12-2 + W12-6 post-edit |
| `.claude/agents/*.md` (each agent definition) | at W12-3 read pass |
| Synthetic test verdict file `computations/_test_layer_functor_audit_leg_verdicts.txt` | at W12-5 attack injection |
| Per-dispatch transcript JSONLs | at W12-4 corpus replay |
| Per-site reconstruction output | at W12-7 read-pass |

**Cross-wave SHA-uniqueness audit**: each producing script computes its `audit_sha256` from `closure_hash(input_pin_map)` per `computations/script-template.py append_verdict()` template. Cross-gate uniqueness verified post-emission via `computations/_recovery_controller.py` sig_5 check on `s87_gate_verdicts.txt`. W12-5's SYNTHETIC duplication attack uses a SEPARATE test verdict file (`_test_layer_functor_audit_leg_verdicts.txt`); the production `s87_gate_verdicts.txt` retains uniqueness invariant.

---

**End of session-87-plan-w12.md.**
