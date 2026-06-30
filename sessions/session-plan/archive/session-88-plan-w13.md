# Session 88 Plan — Wave 13: W12/W13 unrun + methodology infrastructure + W7 queue

> **Provenance**: gen-physicist orchestrator-direct-write per `.claude/rules/wave-classification.md` §"Dispatch consequences"; co-signers: connes-ncg-theorist (#153 LayerF audit-leg); lizzi-spectral-functional-theorist (#160 STAGE-1 + #166 queue triage); volovik + landau-condensed-matter-theorist + mack-cosmic-bridge + sagan-empiricist (#157 4-agent panel).
>
> **Theme**: W12/W13 unrun gates (S86 leftovers) + methodology infrastructure (W-13 deliverables hardening) + W7-3/W7-4/W7-5 corpus follow-up + queue discipline.
>
> **Composition order**: Wave 13 sits AFTER all S88 W1-W12 numerical waves close; it is the methodology-hygiene + queue-triage wave. Per `wave-classification.md` §"Strict-conjunction requirement", METHODOLOGY-class items (#149-156, #160) skip `/rclab-coordinate` compute-mode and dispatch via orchestrator-direct-write; COMPUTE-class items (#159, #162-166) dispatch via `/rclab-coordinate`; #157-158 are panel/cosmology-class.
>
> **Natural-split fallback**: items 149-156 → W13a (methodology infrastructure); items 157-158 → W13b (panel/cosmology); items 159-166 → W13c (W7 corpus follow-up). Single-pass write attempted; split available if mid-wave context exhaustion.

---

## Wave 13 Summary

Wave 13 closes the methodology-hygiene + W7-corpus follow-up debt accumulated across S86 W12/W13, S87 W7, and S87 W11-meta:

- **Items 149-152**: rule-validation + hook-implementation + permission audit + MCP discipline inversion. Hardens W-13 deliverables (RULE-1 wave-classification, RULE-3 allowlist, C3-CONN-EM-2 mcp-pre-check.sh) from spec to operational enforcement.
- **Item 153**: layer-functor F audit-leg verification — synthetic SHA-hardcoding-bug attack triggers v3 ladder sig_5 firing, closing the §"Layer-Decomposition" T2-7 5-mapping triplet from pair-verified to triplet-verified.
- **Item 154**: max-8-subagents hook promotion — moves passive memory rule into active SessionStart hook.
- **Item 155**: S85 5A workshop §K1-K8 13-site independent reconstruction validation.
- **Item 156**: 2D-level-layer corroboration (substrate ↔ methodology ↔ audit triplet at 2D depth).
- **Item 157**: LIFTED to `/rclab-investigate` carry-forward 2026-05-06 (workshop misplaced in `/rclab-plan` output per `Investigating-Workshops.md` §"Cross-references"; see §W13-157 LIFT NOTICE). Not dispatched this session.
- **Item 158**: NC two-torus FGK fixed-point validation.
- **Items 159-161**: W7-3 C-γ-WEAK live-physical lift + STAGE-1-CANDIDATE registration of integer-graded anomaly multiplier theorem + OEIS lookup on n_c sequence.
- **Items 162-164**: W7-4 LAYER audit Step F rubric rewrite + L2-PROMOTABLE → CAC pin retrofit + L2 warrant-check chain.
- **Items 165-166**: W7-5 warrant-head subtest implementation + 25-stub queue triage.

All 18 items: orchestrator-direct-write per W-13 RULE-4 for METHODOLOGY-class; `/rclab-coordinate` compute-mode for COMPUTE-class; substrate-IS-not-IN framing per `phononic-framing.md` (substrate IS the methodology + queue artifact; container-thinking inversions FORBIDDEN — methodology hygiene is not "in" the framework, it IS the framework's audit-leg layer per the layer-functor F).

---

## Wave 13 Decision Point Prerequisites

**Hard prerequisites** (block W13 dispatch if any FAIL):

1. S88 W1-W12 numerical waves CLOSED (W13 is post-numerical methodology-hygiene wave).
2. `computations/canonical_constants.py` HEAD-of-S88 (post-W12 promotions landed).
3. `sessions/permanent-results-registry.md` HEAD-of-S88 (post-W12 §VII landings).
4. `.claude/rules/methodology-wave-allowlist.md` HEAD-of-S87 (8 rows: 4 W0a + W9a-1 + W9a-2 + 3 W11-meta).
5. `computations/s87_w7_layer_audit_full.json` (15.9 MB; 34,876 records; 748 files) — input pin for #162-164.
6. `computations/s87_w7_warrant_check_queue_stubs.json` (12,280 B; 25 stubs) — input pin for #166.

**Soft prerequisites** (advisory; W13 may proceed with diagnostic):

- S87 W11-2 + W11-3 D_K block-diagonal calibration corpus available (cited in #149 rule-validation as 2 of 5 corpus instances).
- S86 W-13 workshop file `sessions/archive/session-86/workshops/s86-permission-topology-methodology-unification.md` available for §lines 27, 289-298, 645-688, 821, 2132 anchor citations (#149-156).

---

## §W13-149 Wave-Classification Rule Validation Across S87 First 5 Methodology-Corpus Waves

- **Gate ID**: `S88-WAVE-CLASSIFICATION-RULE-VALIDATION`
- **Trigger**: [AUDIT]
- **Classification**: METHODOLOGY-class (M1 ✓ artifact-existence predicate; M2 ✓ grep + integer-count operations only; M3 ✓ verbatim from W-13 RULE-1 spec; M4 ✓ allowlist row pending append at plan-freeze).
- **Agent**: gen-physicist (orchestrator-direct-write per W-13 RULE-4 + `team-lead-behavior.md` §"METHODOLOGY-Class Wave Discipline").
- **Hypothesis**: For each of the first 5 methodology-corpus waves landed in S87 (W9a-1, W9a-2, W11-meta-1, W11-meta-2, W11-meta-3 — exactly the 5 post-W0a S87 entries in `methodology-wave-allowlist.md`), the M1∧M2∧M3∧M4 strict conjunction holds, and FAILing ANY one of M1-M4 routes the wave to COMPUTE-class fallthrough or MIXED-class triage (NEVER METHODOLOGY-class by partial satisfaction).
- **Method**:
  1. For each gate-ID in {W9a-1, W9a-2, W11-meta-1, W11-meta-2, W11-meta-3}: read the corresponding plan-block from `sessions/session-plan/session-87-plan-w*.md`; emit (M1, M2, M3, M4) 4-tuple per `wave-classification.md` §M1-M4 enumeration.
  2. Cross-check against `methodology-wave-allowlist.md` schema (`gate_id | session | rationale | sha256_of_plan_block`).
  3. Compute SHA-256 over each plan-block; compare against the stored value in the allowlist row (NOT `pending`).
  4. Emit per-gate `verdict_per_test ∈ {PASS, FAIL}` and aggregate `wave_classification_correct ∈ {TRUE, FALSE}`.
- **Machinery pin**:
  - L_max: N/A (methodology-layer, no spectral computation).
  - Regulator: N/A.
  - Convention: `M1-M4-strict-conjunction` per `wave-classification.md` §"Strict-conjunction requirement".
  - Scheme: `audit-via-grep-and-sha256-compare` (no `.py` numerical script per M2).
- **4-tuple input-pin map**:
  - `methodology-wave-allowlist.md` HEAD-of-S87 SHA-256.
  - `sessions/session-plan/session-87-plan-w9a.md` SHA-256.
  - `sessions/session-plan/session-87-plan-w11.md` SHA-256.
  - `wave-classification.md` HEAD SHA-256.
- **Thresholds**:
  - PASS: all 5 gates exhibit M1∧M2∧M3∧M4 ALL-TRUE; all 5 SHA-256 plan-block hashes match stored values; aggregate `wave_classification_correct = TRUE`.
  - FAIL: ANY gate exhibits ≥1 of M1-M4 = FALSE; OR ANY SHA-256 mismatch.
  - INFO: `pending` SHA-256 placeholders at >0 of 5 rows (one-time S86-R3-window allowance per allowlist §"Pending SHA resolution"); allowance closed at S88 first plan-freeze per same section.
- **Substitution chain INSIDE gate block** (rule-validation predicate):
  - Definition: `M1(g) := "PASS predicate of g is artifact-existence-with-substantive-content, NOT numerical comparison"`. `M2(g) := "producing operations of g restricted to {Edit, Write, MultiEdit, grep, wc, SHA-256, integer counts}"`. `M3(g) := "content of g derives from {verbatim sub-diff, verbatim 5-class taxonomy, anchor-citation rows}"`. `M4(g) := "g ∈ allowlist"`.
  - Substitute: `methodology_class(g) := M1(g) ∧ M2(g) ∧ M3(g) ∧ M4(g)`.
  - Simplify: by `wave-classification.md` §"Strict-conjunction requirement", any one FALSE ⇒ NOT methodology_class(g).
  - Direction: PASS ⇔ ∀ g ∈ {5 corpus gates}: methodology_class(g) = TRUE.
- **What PASS/FAIL MEAN**:
  - PASS: W-13 RULE-1 strict-conjunction discipline operationally validated on the post-W0a S87 corpus; M4 allowlist enforcement empirically working; the rule is operational, not just specified.
  - FAIL: at least one S87 methodology-corpus wave was mis-classified at plan-freeze; remediation = re-classify + sub-decompose to MIXED-class if needed (per W-13 NROY clause + W0a-2 → W0a-2a + W0a-2b precedent).
  - INFO: pending-SHA window not yet closed; carry-forward to S88 W13 second invocation.
- **Effort**: 0.3 wave-equivalents (5 plan-blocks × ~5 minutes per 4-tuple emission + SHA-256 compare).
- **Substrate framing per `phononic-framing.md` IS-not-IN**: the wave-classification rule IS the methodology-axis F-image of the substrate-axis "PASS predicate type" (per `epistemic-discipline.md` §"Layer-Decomposition" Phi(a_2) = Σ_2 weight-2 Einstein-Hilbert kinematic skeleton). The rule is not "in" the methodology container; the methodology layer IS what the rule structures. Container-thinking violation FORBIDDEN: do NOT explain the rule via "we put waves into categories" — invert: "the wave-classification IS the structure of the methodology layer at the F-image of the substrate's PASS-predicate-type axis."

---

## §W13-150 MCP Pre-Check Hook Implementation

- **Gate ID**: `S88-MCP-PRE-CHECK-HOOK-IMPLEMENTATION`
- **Trigger**: [AUDIT] + [VERIFY]
- **Classification**: METHODOLOGY-class (M1 ✓ hook-file-existence + 4-parameter-pin verification; M2 ✓ Write to `.claude/hooks/`; M3 ✓ verbatim from W-13 C3-CONN-EM-2 4-parameter pin; M4 pending allowlist append at plan-freeze).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: The 4-parameter pin from S86 W-13 C3-CONN-EM-2 (PreToolUse trigger; actor-blind firing; load-bearing on Phi(a_4); hook-path `.claude/hooks/mcp-pre-check.sh`) is implementable as an active PreToolUse hook in `.claude/settings.json` such that EVERY MCP tool call (orchestrator OR subagent) fires the hook, the hook performs the pre-check, and the hook's stdout is injected into the tool-call context.
- **Method**:
  1. Author `.claude/hooks/mcp-pre-check.sh` with the 4-parameter pin: (a) PreToolUse trigger matching `mcp__*`; (b) actor-blind firing (no `if subagent then skip` branches); (c) load-bearing on Phi(a_4) per W-13 deliverable Sigma_3 weight-4 axis; (d) emits canonical reminder string about substrate-first-canonical-sourcing + canonical_constants priority + knowledge.db pre-query.
  2. Register in `.claude/settings.json` `hooks.PreToolUse` array with matcher `mcp__.*`.
  3. Synthetic test: dispatch a no-op subagent that calls `mcp__knowledge__.search_knowledge("test")`; verify hook fires + stdout injection observed.
  4. Cross-check: orchestrator main-thread call to same MCP also fires hook (actor-blindness verified).
- **Machinery pin**:
  - Hook trigger: `PreToolUse`.
  - Matcher: `mcp__.*` (all MCP servers).
  - Actor-blind: no actor-conditional branches.
  - Phi-axis: a_4 (load-bearing per W-13).
- **4-tuple input-pin map**:
  - `.claude/settings.json` HEAD SHA-256 (pre-edit + post-edit).
  - `.claude/hooks/` directory listing pre-edit SHA-256.
  - `wave-classification.md` §"Cross-references" SHA-256 (cites mcp-pre-check.sh as AUDIT-1 of W-13).
  - W-13 workshop `s86-permission-topology-methodology-unification.md` SHA-256 (C3-CONN-EM-2 anchor).
- **Thresholds**:
  - PASS: hook file exists + non-empty + executable; settings.json registers it; synthetic subagent test fires hook; actor-blindness confirmed via orchestrator-side test.
  - FAIL: any of {file missing, empty, non-executable, settings.json registration absent, synthetic test does NOT fire hook, actor-conditional branch detected}.
  - INFO: hook fires but stdout-injection mechanism not yet fully operational (Windows shell-quoting edge case); document and route to S89.
- **Substitution chain INSIDE gate block**: trivial (existence + parameter-match predicate; no sign/direction claim).
- **What PASS/FAIL MEAN**:
  - PASS: AUDIT-1 of W-13 operational; Phi(a_4) load-bearing axis active; orchestrator + subagent MCP fabrication-rate auditable from this point onward.
  - FAIL: methodology infrastructure incomplete; ALL downstream gates citing "MCP pre-check fired" cannot rely on enforcement.
- **Effort**: 0.4 wave-equivalents (hook authorship + settings.json edit + 2 synthetic tests).
- **Substrate framing**: hook IS the audit-leg image of the substrate's "MCP-call-event" (F maps event → enforcement). Container-thinking FORBIDDEN: do not say "hook checks calls in the system"; say "the audit layer IS the hook-fire-pattern that the methodology layer's MCP-call structure determines."

---

## §W13-151 Subagent Permission Audit

- **Gate ID**: `S88-SUBAGENT-PERMISSION-AUDIT`
- **Trigger**: [AUDIT]
- **Classification**: METHODOLOGY-class (M1 ✓ permission-enumeration table existence; M2 ✓ grep + table emission only; M3 ✓ verbatim from `.claude/agents/*.md` headers; M4 pending allowlist).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: Per-agent permission enumeration across `.claude/settings.json` allowlist + per-agent `.claude/agents/*.md` headers exhibits NO orphaned permissions (allowlist entries with no agent reference) AND NO agent claiming a permission absent from settings.json allowlist.
- **Method**:
  1. Parse `.claude/settings.json` `permissions.allow` array.
  2. For each `.claude/agents/*.md`: extract `tools:` field from frontmatter.
  3. Cross-tabulate: agent × tool grid.
  4. Flag: orphaned permissions (in settings.json allowlist, claimed by 0 agents) + ghost permissions (claimed by ≥1 agent, NOT in settings.json allowlist).
- **Machinery pin**: parsing protocol = YAML-frontmatter-aware; tool-list canonicalization = lowercase + alphabetize.
- **4-tuple input-pin map**: `.claude/settings.json` SHA-256; `.claude/agents/` directory tree SHA-256 (recursive); `methodology-wave-allowlist.md` SHA-256; `wave-classification.md` SHA-256.
- **Thresholds**:
  - PASS: 0 orphaned permissions AND 0 ghost permissions.
  - FAIL: ≥1 orphaned OR ≥1 ghost (with full enumeration in verdict line).
  - INFO: borderline cases (e.g., agent inherits permission via wildcard) documented but not flagged.
- **Substitution chain INSIDE gate block**: trivial set-membership predicate; no direction claim.
- **What PASS/FAIL MEAN**:
  - PASS: agent permission topology consistent with settings.json; recursion-attack closure (per RULE-3 allowlist orchestrator-only-edit) operationally verified.
  - FAIL: permission drift surfaces; remediation = either remove orphaned permission from settings.json OR add agent-tool reference if intended.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: agent-permission topology IS the methodology-layer F-image of the substrate's "agent-spawn-eligibility" axis. Permissions are not "granted to" agents — the agent IS its permission-set in the methodology layer.

---

## §W13-152 MCP Discipline Inversion Validation

- **Gate ID**: `S88-MCP-DISCIPLINE-INVERSION-VALIDATION`
- **Trigger**: [AUDIT]
- **Classification**: METHODOLOGY-class (M1 ✓ fabrication-rate counter; M2 ✓ grep + count; M3 ✓ verbatim from W-13 Phi(a_4); M4 pending).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: Orchestrator MCP fabrication-rate (claims of MCP-query results without an actual MCP tool call in the transcript) on dispatch transcripts from S87 W7 + W11 + W12 is ZERO. Phi(a_4) load-bearing axis enforces this.
- **Method**:
  1. Parse `~/.claude/projects/C--sandbox-Ainulindale-Exflation/subagents/*.jsonl` for S87 W7/W11/W12 dispatches.
  2. Grep for orchestrator-side claims matching pattern: `/(?:I queried|knowledge MCP returned|search_knowledge found|get_constant returned)/i`.
  3. Cross-check against actual `tool_use` records with `name` matching `mcp__knowledge__.*`.
  4. Compute fabrication_rate = (claims without matching tool_use) / (total claims).
- **Machinery pin**: transcript-parsing protocol = JSONL line-by-line; claim-pattern set = canonical 4-pattern enumeration above.
- **4-tuple input-pin map**: S87 transcript directory SHA-256 (recursive); claim-pattern set SHA-256 (from this plan-block); `wave-classification.md` SHA-256; W-13 workshop SHA-256.
- **Thresholds**:
  - PASS: fabrication_rate = 0.000 (zero claims without backing tool_use).
  - FAIL: fabrication_rate > 0.000 (with full enumeration of fabricated claims).
  - INFO: borderline detections (e.g., claim referring to memory rather than MCP) documented + excluded from numerator.
- **Substitution chain INSIDE gate block**: definition: `fabrication_rate := |{c ∈ claims : ¬∃ t ∈ tool_uses, matches(c, t)}| / |claims|`. Direction: PASS ⇔ numerator = 0.
- **What PASS/FAIL MEAN**:
  - PASS: Phi(a_4) discipline operational; mcp-pre-check.sh hook (#150) effectively enforcing.
  - FAIL: discipline violation; route to S89 remediation gate; flag specific dispatches.
- **Effort**: 0.4 wave-equivalents.
- **Substrate framing**: fabrication-rate IS the audit-leg residual of the methodology-layer's MCP-discipline rule. Not "agents are lying about MCP" — the audit layer IS the structural test of whether F preserves PRU-class invariants under W-13 RULE-2 layer-functor.

---

## §W13-153 Layer-Functor Audit-Leg Verification (T2-7 5-Mapping)

- **Gate ID**: `S88-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`
- **Trigger**: [VERIFY]
- **Classification**: METHODOLOGY-class (M1 ✓ synthetic-attack triggers ladder firing predicate; M2 ✓ controlled fixture + grep on verdict file; M3 ✓ verbatim from epistemic-discipline.md §"Layer-Decomposition" T2-7 5-mapping; M4 pending).
- **Agent**: connes-ncg-theorist (CO-AUTHOR per spawn spec; layer-functor F mathematical structure is NCG-axiomatic).
- **Hypothesis**: A synthetic SHA-hardcoding bug (script that emits a fixed `audit_sha256` literal rather than computing it from `closure_hash(input_pin_map)`) injected into a controlled fixture triggers v3 ladder sig_5 firing per `v3-closure-recovery.md` Stage-1 sig_5 remediation map. This closes the §"Layer-Decomposition" T2-7 5-mapping triplet from PAIR-VERIFIED (substrate ↔ methodology, S86 R3) to TRIPLET-VERIFIED (substrate ↔ methodology ↔ audit).
- **Method**:
  1. Build a fixture `computations/_layer_functor_attack_fixture.py` that intentionally hardcodes `audit_sha256 = "deadbeef..."` (64-char hex) for two synthetic gates G_A and G_B, each emitting the same hardcoded SHA.
  2. Append both verdict lines to a fixture `computations/_fixture_layer_functor_verdicts.txt` (NOT the canonical s88_gate_verdicts.txt).
  3. Run `computations/_v3_closure_audit.sh` (or the Python equivalent) over the fixture file.
  4. Verify sig_5 (duplicate `audit_sha256`) FIRES → INFO/FAIL with remediation message naming both gates.
  5. Verify sig_5 audit identifies the SHA-hardcoding pattern as the fault (not isolated typo).
- **Machinery pin**: fixture-isolation = separate verdict file (no contamination of canonical); attack pattern = literal SHA assignment outside `closure_hash(...)` call.
- **4-tuple input-pin map**: fixture script SHA-256 post-build; fixture verdict file SHA-256 post-emission; `v3-closure-recovery.md` HEAD SHA-256; `epistemic-discipline.md` §"Layer-Decomposition" SHA-256.
- **Thresholds**:
  - PASS: sig_5 fires on fixture; remediation message names both G_A and G_B; pattern-classification matches "SHA-hardcoding bug" (not "typo").
  - FAIL: sig_5 does NOT fire OR misclassifies the pattern.
  - INFO: sig_5 fires but remediation message lacks pattern-classification (audit script needs extension; route to S89).
- **Substitution chain INSIDE gate block**:
  - Definition: `F : substrate → methodology → audit`. T2-7 mapping at audit leg: `verdict-line artifact-SHA ↔ audit_sha256 (self-referential)`; `orchestrator-direct-without-cross-actor ↔ SHA-hardcoding bug (sig_5)`.
  - Substitute: synthetic SHA-hardcoding fixture instantiates the audit-leg F-image of the substrate-leg "orchestrator-direct-without-cross-actor" failure mode.
  - Simplify: if F preserves PRU-class invariants (W-13 Morita-equivalence framing), then audit-leg attack must trigger audit-layer detection (sig_5).
  - Direction: PASS ⇔ sig_5 fires AND classifies correctly.
- **What PASS/FAIL MEAN**:
  - PASS: triplet-verification complete; T2-7 5-mapping closes from pair to triplet; F functor empirically Morita-equivalent across all three layers.
  - FAIL: audit-leg image of substrate failure mode does NOT manifest at audit layer; F functor incomplete; W-13 RULE-2 layer-decomposition needs revision.
- **Effort**: 0.5 wave-equivalents (fixture authorship + audit-script execution + verification).
- **Substrate framing**: the audit-leg verification IS the F-image of the substrate-leg attack. Container-thinking FORBIDDEN: not "we test the audit system"; "the audit IS the F-image, and the test IS the verification that F preserves the invariant."

---

## §W13-154 Max-8-Subagents SessionStart Hook Promotion

- **Gate ID**: `S88-MAX-8-SUBAGENTS-HOOK-PROMOTION`
- **Trigger**: [AUDIT] + [VERIFY]
- **Classification**: METHODOLOGY-class (M1 ✓ hook-file-existence + reminder-string verification; M2 ✓ Write to `.claude/hooks/`; M3 ✓ verbatim from `feedback_dispatch-discipline.md`; M4 pending).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: The currently passive `feedback_dispatch-discipline.md` rule (memory-only enforcement; user corrects EVERY session) can be promoted to active SessionStart hook injecting the reminder string at session start, eliminating per-session correction.
- **Method**:
  1. Author `.claude/hooks/max-8-subagents-reminder.sh` emitting the canonical reminder: "MAX ~8 CONCURRENT SUBAGENTS. Default Claude inclination is 30+. User corrects EVERY session. SELF-IMPOSE the cap."
  2. Register in `.claude/settings.json` `hooks.SessionStart` array.
  3. Verify orchestrator system-prompt at next session start includes the reminder (synthetic test or next-session observational confirmation).
- **Machinery pin**: hook trigger = `SessionStart`; reminder string verbatim from `feedback_dispatch-discipline.md` HEAD.
- **4-tuple input-pin map**: `feedback_dispatch-discipline.md` SHA-256; `.claude/settings.json` SHA-256 pre+post; `.claude/hooks/` directory listing pre-edit SHA-256; `wave-classification.md` SHA-256.
- **Thresholds**:
  - PASS: hook file exists + executable + emits canonical reminder; settings.json registers SessionStart; synthetic test confirms injection.
  - FAIL: any of {file missing, content drift from canonical reminder, registration absent, injection not observed}.
  - INFO: hook fires but injection-observation mechanism not yet operational (needs S89 verification at next-session boundary).
- **Substitution chain INSIDE gate block**: trivial existence predicate.
- **What PASS/FAIL MEAN**:
  - PASS: passive rule promoted to active enforcement; per-session user correction eliminated.
  - FAIL: rule remains passive; user continues correcting per-session.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: hook IS the audit-leg image of the methodology-layer "concurrent-dispatch-cap" rule. Not "hook reminds us"; "the SessionStart firing IS the structural enforcement of the cap at the boundary where dispatch decisions are made."

---

## §W13-155 W0a-2a Independent 13-Site Reconstruction

- **Gate ID**: `S88-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION`
- **Trigger**: [AUDIT] + [VERIFY]
- **Classification**: METHODOLOGY-class (M1 ✓ per-site reconstructibility predicate; M2 ✓ grep + canonical_constants entry verification; M3 ✓ verbatim from S85 5A workshop §K1-K8 13-site enumeration; M4 pending).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: Each of the 13 sites in S85 5A workshop §K1-K8 admits independent reconstruction with a matching canonical_constants entry.
- **Method**:
  1. Read S85 5A workshop file `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` §K1-K8.
  2. Enumerate the 13 sites (per S85 W-3 v2 11-clause inventory + K1 5-mode framework).
  3. For each site: check `canonical_constants.py` for a corresponding entry; check `computations/` for a substrate-first computation script; verify the entry's PROVENANCE field cites the site.
  4. Emit per-site `reconstruction_status ∈ {PASS, FAIL, INCOMPLETE}`.
- **Machinery pin**: site enumeration = verbatim from §K1-K8; reconstruction predicate = (canonical entry exists) ∧ (substrate computation exists) ∧ (PROVENANCE cites site).
- **4-tuple input-pin map**: `s85-w3-methodology-debts.md` SHA-256; `canonical_constants.py` SHA-256; `computations/` directory listing SHA-256; `wave-classification.md` SHA-256.
- **Thresholds**:
  - PASS: all 13 sites reconstruct (3-of-3 predicate satisfied each).
  - FAIL: ≥1 site fails reconstruction (with full enumeration).
  - INFO: ≥1 site INCOMPLETE (canonical entry exists but PROVENANCE drift); document + route to S89 remediation.
- **Substitution chain INSIDE gate block**: trivial 3-of-3 conjunction per site.
- **What PASS/FAIL MEAN**:
  - PASS: S85 W-3 v2 + 5A v2 union landed at S86 W0a-1 is operationally complete across all 13 sites.
  - FAIL: methodology-debt registry has gaps; remediation per-site.
- **Effort**: 0.5 wave-equivalents (13 sites × ~5 min per site).
- **Substrate framing**: 13-site reconstruction IS the F-image of substrate computational completeness at the methodology axis. Not "we audit the methodology debts"; "the methodology layer IS the 13-site reconstruction structure."

---

## §W13-156 2D Level-Layer Corroboration

- **Gate ID**: `S88-2D-LEVEL-LAYER-CORROBORATION`
- **Trigger**: [AUDIT]
- **Classification**: METHODOLOGY-class (M1 ✓ 2D corroboration table existence; M2 ✓ grep + table emission; M3 ✓ verbatim from substrate-first-canonical-sourcing.md PRIMARY/SCHEMATIC enumeration; M4 pending).
- **Agent**: gen-physicist (orchestrator-direct-write).
- **Hypothesis**: The substrate ↔ methodology ↔ audit triplet (W-13 RULE-2 layer-functor F) admits corroboration at the 2D level-layer axis (PRIMARY full physical regularization vs SCHEMATIC schematic analog) such that every SCHEMATIC helper has an explicit level pin in its consuming gate-blocks AND the level pin propagates through F at all three layers.
- **Method**:
  1. Enumerate all SCHEMATIC helpers in `computations/_*.py` (modules whose docstring identifies them as schematic).
  2. For each: enumerate consuming gates (grep for module import).
  3. For each consuming gate: verify level pin present in plan-block AND verdict-line `convention=` field encodes SCHEMATIC suffix per `substrate-first-canonical-sourcing.md` (iv) discipline.
  4. Emit 2D table: helper × consumer × (substrate / methodology / audit) compliance.
- **Machinery pin**: helper enumeration = `_spectral_action_regulators.py` + `_phononic_helpers.py` + any additional flagged via SCHEMATIC docstring.
- **4-tuple input-pin map**: SCHEMATIC helper directory SHA-256; consuming-gate plan-block SHA-256s (multi-file aggregate); `substrate-first-canonical-sourcing.md` SHA-256; `wave-classification.md` SHA-256.
- **Thresholds**:
  - PASS: all (helper, consumer) pairs have level pin present at all three layers (substrate plan-block, methodology rule-citation, audit verdict-line).
  - FAIL: ≥1 pair missing level pin at ≥1 layer.
  - INFO: level pin present at substrate but propagation drift at audit (verdict-line `convention=` lacks SCHEMATIC suffix); document + remediate.
- **Substitution chain INSIDE gate block**: definition: `level_compliant(h, c) := pin_at(substrate, h, c) ∧ pin_at(methodology, h, c) ∧ pin_at(audit, h, c)`. Direction: PASS ⇔ ∀ (h, c) pairs: level_compliant.
- **What PASS/FAIL MEAN**:
  - PASS: 2D-level-layer triplet operational; SCHEMATIC vs full-physical distinction propagates through F functor cleanly.
  - FAIL: level-conflation pathology (per `substrate-first-canonical-sourcing.md` (iv)) detected; remediation per-pair.
- **Effort**: 0.4 wave-equivalents.
- **Substrate framing**: level pin IS the F-image of the substrate's regularization-class identity at the methodology layer; verdict-line SCHEMATIC suffix IS the audit-leg image. Not "we annotate schematic helpers"; "the SCHEMATIC tag IS the structural identity that F maps across all three layers."

---

## §W13-157 Path-B Step-0 Workshop Dispatch — **LIFTED to /rclab-investigate carry-forward (2026-05-06)**

> **LIFT NOTICE** (2026-05-06; user-directed during S88 W13 `/rclab-coordinate` invocation): This item is structurally a 4-agent workshop dispatch, NOT a `/rclab-coordinate` compute-mode gate. Per `.claude/rules/Investigating-Workshops.md` §"Cross-references", workshops belong in workshop-schedule files routed via `/rclab-investigate` → `/rclab-team`, never in `/rclab-plan` compute outputs ("the workshop schedule and the carry-forward plan are SEPARATE OUTPUTS"). This slot represents a `/rclab-plan` authorship type-error: a 4-agent panel adversarial review was emitted as a plan gate alongside numerical-threshold compute items.
>
> **Carry-forward route**: No `sessions/archive/session-88-workshop-schedule.md` exists yet — W13 is the final compute wave before the next `/rclab-investigate` dispatch. The user will surface this item during investigation seeding so the investigators see it as a candidate workshop alongside other tensions surfacing from S88's substance. The body below is preserved for historical context (Path-B substrate-IS framing, 4-condition verdict structure, Stage-0 protocol per `joint-theorem-promotion.md`) but is **NOT** for this session's dispatch and **NOT** counted in W13 verdict tallies.
>
> **Verdict status**: N/A (lifted, not dispatched). No verdict line will be appended to `computations/session-88/s88_gate_verdicts.txt` for `S88-PATH-B-STEP-0-WORKSHOP` in this session.

---

- **Gate ID**: `S88-PATH-B-STEP-0-WORKSHOP`
- **Trigger**: [VERIFY]
- **Classification**: PARTICLE/cosmology-class (4-agent panel adversarial review; structurally a workshop dispatch per `Investigating-Workshops.md` 4-condition definition).
- **Agent**: orchestrator + 4-agent panel (volovik-superfluid-universe-theorist + landau-condensed-matter-theorist + mack-cosmic-bridge + sagan-empiricist).
- **Hypothesis**: Path-B as an alternative successor route to Path-(c) (S86 W-9 Joint F_2-Class theorem at §VII.AH STAGE-1-CANDIDATE) admits a Step-0 workshop validating its 4 prerequisite conditions before Step-1 dispatch.
- **Method**: 4-agent workshop, 3 rounds (R1 steelman / R2 respond / R3 converge). Each round: each agent emits per-condition verdict; round-3 emits joint pre-registration of Path-B Step-1 + Step-2 + Step-3 gates.
- **Machinery pin**: 3-round workshop; agents named above; output = workshop-§"Workshop Verdict" with pre-registered Step-1+2+3 gate-blocks.
- **4-tuple input-pin map**: §VII.AH STAGE-1-CANDIDATE registry text SHA-256; W-9 workshop §lines 1535-1585 + 1707-1755 + 2094-2148 + 1948-2003 SHA-256; `joint-theorem-promotion.md` SHA-256; `Investigating-Workshops.md` SHA-256.
- **Thresholds**:
  - PASS: 4-agent R3 convergence on all 4 Path-B prerequisite conditions; Step-1+2+3 pre-registration emitted with thresholds.
  - FAIL: ≥1 condition FAILs at R3; Path-B does not advance; STAGE-1-CANDIDATE remains via Path-(c) only.
  - INFO: R3 partial convergence on subset of conditions; document + route to S89 follow-up workshop.
- **Substitution chain INSIDE gate block**: workshop adjudicates whether Path-B prerequisite conditions are structurally satisfied; multi-round structure prevents single-agent pre-judgment.
- **What PASS/FAIL MEAN**:
  - PASS: alternative successor route opens for §VII.AH; Stage-2 cross-check has dual-path option.
  - FAIL: Path-(c) is the unique successor; STAGE-1 → STAGE-3 promotion locked to single path.
- **Effort**: 1.0 wave-equivalents (3-round 4-agent workshop = canonical S82 W-1 H̃-DIVERGENCE-CHASE shape).
- **Substrate framing**: Path-B IS an alternative substrate-IS observable on the Pillar-AH cohomology axis; the workshop adjudicates which IS the structural successor. Container-thinking FORBIDDEN.

---

## §W13-158 NC Two-Torus FGK Fixed-Point Validation

- **Gate ID**: `S88-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (numerical fixed-point convergence verification).
- **Agent**: connes-ncg-theorist (NCG-axiomatic); volovik-superfluid-universe-theorist co-signer (BdG-sector cross-check).
- **Hypothesis**: The NC two-torus FGK (Fadell-Górniewicz-Kahn or Fixed-point-Galois-Kasparov, scheme-name pinned at S88-W13 plan-freeze; pending §"Source Reconciliation" Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY) fixed-point on the noncommutative two-torus `T²_θ` with Jensen-deformed structure constants converges to a pre-registered topological invariant under truncation L_max ∈ {6, 8, 10, 12}.
- **Method**:
  1. Build NC two-torus spectral triple `(C(T²_θ), L²(T²_θ), D_T)` per Connes 1980 §IV.6.
  2. Iterate FGK fixed-point recursion to convergence at each L_max ∈ {6, 8, 10, 12}.
  3. Cross-check against substrate's Pillar-IV quantum-metric trace (W-5 calibration) — predicted match modulo Jensen-deformation factor.
  4. Emit per-L_max fixed-point value + convergence rate.
- **Machinery pin**:
  - L_max scan: {6, 8, 10, 12}.
  - Regulator: Pauli-Villars (PRIMARY full physical per `substrate-first-canonical-sourcing.md` (iv)).
  - Convention: `nc-two-torus-fgk-fixed-point-pauli-villars-jensen-deformed`.
  - Scheme name: pending §"Source Reconciliation" at plan-freeze.
- **4-tuple input-pin map**: `canonical_constants.py` HEAD SHA-256; `computations/_nc_two_torus_helpers.py` SHA-256 (or build script); Connes 1980 §IV.6 anchor citation; W-5 Pillar-IV cross-check anchor SHA-256.
- **Thresholds**:
  - PASS: L^{-3} convergence rate at d=4 (matches W-5 algebraic envelope); fixed-point value matches substrate's Pillar-IV cross-check within W-5 tolerance band.
  - FAIL: convergence rate ≠ L^{-3} OR fixed-point value violates W-5 tolerance.
  - INFO: convergence trend present but L_max=12 insufficient to declare; document + route to S89 with extended L_max scan.
- **Substitution chain INSIDE gate block**:
  - Definition: NC two-torus FGK fixed-point `f(L_max) := lim_{n → ∞} F^n(x_0; L_max)` where F is the FGK operator on truncated `(C(T²_θ)^{≤L}, ...)`.
  - Substitute: under Jensen deformation + Pauli-Villars, F is a contraction by Connes 1980 Thm 6.2 (Jensen-deformation-extended).
  - Simplify: contraction ⇒ convergence; rate from Connes-Karoubi pairing pulls down `L^{-3}` at d=4 per W-5.
  - Direction: PASS ⇔ |f(L_max=12) − substrate_Pillar_IV_cross_check| < tolerance.
- **What PASS/FAIL MEAN**:
  - PASS: NC two-torus is structural sister to Pillar-IV cross-pillar bridge anatomy (W-5 calibration corpus instance #3 candidate; advances K=2 → K=3 promotion threshold).
  - FAIL: NC two-torus diverges from substrate's Pillar-IV at the algebraic envelope; revisit Jensen-deformation parameters.
- **Effort**: 0.8 wave-equivalents (NCG construction + L_max scan + cross-check).
- **Substrate framing**: NC two-torus IS a substrate-IS observable at the algebra-enriched extension of Pillar-IV; FGK fixed-point IS the structural-confidence Level-3 anchor. Container-thinking FORBIDDEN.

---

## §W13-159 W7-3 C-γ-WEAK Per-L1-Class PRIMARY Lift

- **Gate ID**: `S88-W7-3-C-GAMMA-WEAK-PRIMARY-LIFT`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class.
- **Agent**: lizzi-spectral-functional-theorist.
- **Hypothesis**: Re-running C-γ-WEAK per-L1-class evaluation under PRIMARY full-physical regularization (Pauli-Villars + mass-scale running) on the full 155,984 eigenvalue cache at L_max=10 reproduces the W7-3 PASS-R2 integer-graded anomaly multiplier signature {n_c} = (10, 10, 10, 11, 13) AND the global anomaly scale Λ_global = 5.326e+14 GeV ≈ 7.169e-03 · M_KK with profile-invariance ≤ 1.49e-16 (the W7-3 SCHEMATIC value).
- **Method**:
  1. Load `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 (155,984 eigenvalues).
  2. Implement Pauli-Villars subtraction with mass-scale running per Connes-Chamseddine 1996 §2.2-2.3.
  3. Per L1-class (5 classes per W7-3 partition): evaluate C-γ-WEAK at the full-physical PRIMARY level.
  4. Extract integer-graded anomaly multiplier {n_c}_TIER1 + global scale Λ_global_TIER1.
  5. Compare against W7-3 SCHEMATIC values.
- **Machinery pin**:
  - L_max: 10 (operational); cache: `s84_spectrum_cache_L12_tau019.npz` (master).
  - Regulator: Pauli-Villars PRIMARY full-physical (per `substrate-first-canonical-sourcing.md` (iv) level rule).
  - Convention: `pauli-villars-level-1-mass-scale-running-connes-chamseddine-1996`.
  - Scheme: per-L1-class evaluation; profile-invariance threshold = 1.49e-16.
- **4-tuple input-pin map**: spectrum cache SHA-256; `_pauli_villars_subtraction.py` (helper, build at S88) SHA-256; `canonical_constants.py` HEAD SHA-256; W7-3 verdict-line SHA-256 (S87).
- **Thresholds**:
  - PASS: {n_c}_TIER1 = (10, 10, 10, 11, 13) AND |Λ_global_TIER1 − 5.326e+14 GeV| / 5.326e+14 < 1.49e-16 AND profile-invariance ≤ 1.49e-16.
  - FAIL: any deviation beyond profile-invariance bound.
  - INFO: deviation within factor-of-2 of bound; document + investigate PRIMARY vs SCHEMATIC propagation factor.
- **Substitution chain INSIDE gate block**:
  - Definition: C-γ-WEAK per-L1-class anomaly multiplier `n_c(class) := count of structural-anomaly contributions in class`.
  - Substitute: under PRIMARY Pauli-Villars, each contribution carries the full mass-scale-running factor (vs SCHEMATIC schematic which truncates the running).
  - Simplify: if W7-3 SCHEMATIC PASSed at profile-invariance 1.49e-16, then under W-3 RULE-3 mnemonic-vs-exact discipline, live-physical lift must reproduce or surface the deviation.
  - Direction: PASS ⇔ PRIMARY reproduces SCHEMATIC within the same bound (signaling SCHEMATIC was structurally faithful).
- **What PASS/FAIL MEAN**:
  - PASS: W7-3 SCHEMATIC was structurally faithful; integer-graded anomaly multiplier theorem stable under live-physical lift; STAGE-1-CANDIDATE registration (#160) defensible.
  - FAIL: PRIMARY vs SCHEMATIC propagation drift surfaces; integer-graded anomaly multiplier theorem requires reformulation.
- **Effort**: 1.2 wave-equivalents (155,984 eigenvalues × Pauli-Villars subtraction at PRIMARY; GPU-bound per `math-scripts.md` D_K Block-Diagonal pre-check protocol).
- **Substrate framing**: integer-graded anomaly multiplier IS a substrate-IS spectral moment of D_K at the C-γ-WEAK projection; container-thinking FORBIDDEN.

---

## §W13-160 W7-3 Integer-Graded Anomaly Multiplier Theorem STAGE-1-CANDIDATE Registration

- **Gate ID**: `S88-W7-3-INTEGER-GRADED-ANOMALY-MULTIPLIER-THEOREM-STAGE-1`
- **Trigger**: [VERIFY-THEOREM]
- **Classification**: METHODOLOGY-class (M1 ✓ registry-entry-existence + 5-IS-not-IN anatomy verification; M2 ✓ Edit to permanent-results-registry.md; M3 ✓ verbatim from W7-3 PASS-R2 substance per joint-theorem-promotion.md Stage 0 → Stage 1; M4 pending allowlist).
- **Agent**: lizzi-spectral-functional-theorist (PRIMARY synthesizer per W7-3 originating workshop).
- **Hypothesis**: The W7-3 PASS-R2 integer-graded anomaly multiplier theorem ({n_c} = (10, 10, 10, 11, 13); Λ_global = 5.326e+14 GeV ≈ 7.169e-03 · M_KK; profile-invariance 1.49e-16) admits STAGE-1-CANDIDATE registration in `sessions/permanent-results-registry.md` per `joint-theorem-promotion.md` 4-stage pathway.
- **Method**:
  1. Author registry entry at next-free-letter slot in §VII per `regulator-pin-discipline.md` next-free-letter protocol.
  2. Required structure: STAGE-1-CANDIDATE tag; full theorem text; identification of joint clauses requiring Stage-2 cross-axis verify.
  3. Cite W7-3 as Stage-0 workshop; cite #159 as PRIMARY corroboration (must PASS prior to STAGE-1 landing).
  4. Pre-register Stage-2 cross-reviewer dispatch (S89 `S89-INTEGER-GRADED-ANOMALY-MULTIPLIER-THEOREM-INDEPENDENT-VERIFY`).
- **Machinery pin**: registry slot allocation = grep-all-header-levels per registry-write-hygiene rule; STAGE-1-CANDIDATE tag verbatim per joint-theorem-promotion Stage 1 spec.
- **4-tuple input-pin map**: `permanent-results-registry.md` HEAD SHA-256 pre-edit; #159 verdict-line SHA-256 (must be PASS); `joint-theorem-promotion.md` SHA-256; W7-3 working-paper §SHA-256.
- **Thresholds**:
  - PASS: registry entry landed at next-free-letter slot; STAGE-1-CANDIDATE tag present; all 5 IS-not-IN anatomy elements present per cross-pillar-bridge-anatomy.md (substrate-IS = D_K integer-graded multiplier; lab-IN = N/A or pending S89 lab-link); 3-level ladder declared.
  - FAIL: #159 prereq is FAIL (live-physical lift does not reproduce); OR slot allocation collision (parallel-writer race); OR anatomy element missing.
  - INFO: registry entry lands but anatomy element pending S89 lab-link; tag as STAGE-1-CANDIDATE-PARTIAL.
- **Substitution chain INSIDE gate block**: per joint-theorem-promotion 4-stage pathway; Stage 0 (workshop-internal) → Stage 1 (registered candidate) is mechanical given workshop verdict freeze.
- **What PASS/FAIL MEAN**:
  - PASS: theorem enters Stage-1; eligible for Stage-2 cross-axis independent-verify in S89.
  - FAIL: theorem stays at workshop-internal Stage 0; reroute to S89 with PRIMARY + anatomy remediation.
- **Effort**: 0.4 wave-equivalents.
- **Substrate framing**: integer-graded anomaly multiplier IS a substrate-IS structural number at the C-γ-WEAK Mellin projection; registry entry IS the F-image at the methodology layer.

---

## §W13-161 W7-3 n_c OEIS Lookup

- **Gate ID**: `S88-W7-3-N_C-OEIS-LOOKUP`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (external-lookup verification).
- **Agent**: gen-physicist (OEIS query + interpretation).
- **Hypothesis**: The integer sequence {10, 10, 10, 11, 13} (W7-3 integer-graded anomaly multiplier) appears in OEIS with a known structural interpretation (e.g., dimension formula, partition function, group-theoretic count) that informs the substrate-IS reading.
- **Method**:
  1. Query `mcp__oeis__lookup_by_values` with the sequence {10, 10, 10, 11, 13}.
  2. If hits return: read top 3 by relevance; for each, fetch via `mcp__oeis__get_sequence`; classify match-type (exact prefix / exact substring / shifted / coincidental).
  3. Emit interpretation table: OEIS-ID × match-type × structural-interpretation × substrate-relevance.
- **Machinery pin**: query function = `lookup_by_values`; sequence verbatim from W7-3.
- **4-tuple input-pin map**: W7-3 verdict-line `value=` field (extracts {n_c} = (10,10,10,11,13)) SHA-256; OEIS query response timestamp; `canonical_constants.py` SHA-256; #160 verdict-line SHA-256 (must be PASS for context).
- **Thresholds**:
  - PASS: ≥1 OEIS match with structural interpretation that aligns with substrate's C-γ-WEAK projection (e.g., "dimensions of irreps of SO(5)" or "partition counts at depth 5").
  - FAIL: no OEIS hits, OR all hits are coincidental (no structural alignment).
  - INFO: hits returned but interpretation ambiguous; document + route to S89 follow-up.
- **Substitution chain INSIDE gate block**: OEIS lookup is external-database query; PASS/FAIL is interpretive on the returned hits.
- **What PASS/FAIL MEAN**:
  - PASS: substrate's C-γ-WEAK integer signature matches a known mathematical structure; cross-link added to STAGE-1-CANDIDATE entry.
  - FAIL: no external structural alignment; W7-3 anomaly multiplier remains substrate-internal-only structural number.
  - INFO: ambiguous; documented for S89.
- **Effort**: 0.1 wave-equivalents.
- **Substrate framing**: external OEIS match would corroborate substrate-IS reading at the algebra-axis F-image (substrate IS a known structural integer pattern, not "in" a separate mathematical container).

---

## §W13-162 W7-4 LAYER Audit Step F Rubric Rewrite

- **Gate ID**: `S88-W7-4-LAYER-AUDIT-STEP-F-RUBRIC-REWRITE`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (audit-script harness rewrite).
- **Agent**: lizzi-spectral-functional-theorist (sole writer per W7-4 originating workshop).
- **Hypothesis**: The W7-4 LAYER audit Step F harness (currently using rubric-graded approximate filename matching per `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" Class-8.2 risk) can be rewritten to use direct filename:line lookup against a hand-tagged reference table, eliminating rubric-class-8.2 vulnerabilities.
- **Method**:
  1. Build hand-tagged reference table `computations/_w7_4_step_f_reference_table.json` mapping {filename:line → expected_layer ∈ {L1-NUMERICAL, L2-PROMOTABLE, L3-IGNORABLE}}.
  2. Rewrite Step F harness in `computations/s87_w7_layer_audit.py` (S88 fork) to use direct lookup against the reference table.
  3. Cross-check: rewrite verdict on the same 34,876 records as W7-4 original; emit delta-table.
- **Machinery pin**: reference table tagging protocol = manual hand-tag of N=200 sample records (stratified across L1/L2/L3); harness operation = exact dict-lookup, NO rubric or fuzzy matching.
- **4-tuple input-pin map**: `s87_w7_layer_audit_full.json` SHA-256 (input); `_w7_4_step_f_reference_table.json` SHA-256 (post-tag); `s87_w7_layer_audit.py` HEAD SHA-256 pre-rewrite; `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" SHA-256.
- **Thresholds**:
  - PASS: rewrite eliminates rubric-class-8.2 path AND delta-table on N=200 sample is identical to hand-tagged ground truth (0 false-positives, 0 false-negatives).
  - FAIL: rewrite still uses fuzzy matching, OR delta-table shows ≥1 mismatch.
  - INFO: rewrite passes N=200 but full-corpus 34,876 records exhibits edge cases beyond sample; document + route to S89 sample expansion.
- **Substitution chain INSIDE gate block**: Class-8.2 rubric-vs-hand-tagged identity check; direct.
- **What PASS/FAIL MEAN**:
  - PASS: W7-4 harness moves from rubric-graded (Class-8.2 vulnerable) to ground-truth-anchored (Class-8.2 closed); audit reproducibility under iterate-until-PASS pressure now structurally bounded.
  - FAIL: rubric-vulnerability persists; downstream W7-4 verdicts remain Class-8.2-flagged.
- **Effort**: 0.7 wave-equivalents (table tagging + harness rewrite + N=200 cross-check).
- **Substrate framing**: harness rewrite IS the audit-leg F-image of the methodology-layer "verifier-rubric pre-registration" rule. Not "we improve the audit"; "the audit IS the F-image, and the rewrite eliminates the structural permissiveness in the F-functor."

---

## §W13-163 W7-4 Unpinned L2-Promotable CAC Conversion

- **Gate ID**: `S88-W7-4-UNPINNED-L2-PROMOTABLE-CONVERSION`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (canonical pin retrofit).
- **Agent**: lizzi-spectral-functional-theorist.
- **Hypothesis**: The 2,828 L2-PROMOTABLE records in `s87_w7_layer_audit_full.json` admit canonical-anchored convention (CAC) pin retrofit per `regulator-convention-lockdown.md` §"Rule" (CAC convention `w_0(L) := rho_X(L) + offset_X` with `offset_X = w_0_FW − rho_X(L_anchor=10)`).
- **Method**:
  1. For each of 2,828 L2-PROMOTABLE records: extract the regulator scheme X.
  2. Compute CAC offset_X for each scheme present in the records.
  3. Retrofit the record's pin field to CAC form.
  4. Emit retrofit-log + per-scheme offset table.
- **Machinery pin**:
  - Source: `s87_w7_layer_audit_full.json` (15.9 MB; 2,828 L2-PROMOTABLE filtered subset).
  - Convention: CAC per `regulator-convention-lockdown.md` (Zubarev default; offset_Zubarev = -0.340827).
  - L_anchor: 10 (canonical-pin per W0-7 NPZ).
- **4-tuple input-pin map**: `s87_w7_layer_audit_full.json` SHA-256; `regulator-convention-lockdown.md` SHA-256; W0-7 NPZ rho_series SHA-256; `canonical_constants.py` (`w0_FW = -0.918`) SHA-256.
- **Thresholds**:
  - PASS: 2,828/2,828 records retrofitted; per-scheme offset matches `regulator-convention-lockdown.md` §"Rule" demarcation theorem (effacement-preservation at L=10 EXACTLY).
  - FAIL: any record retrofit fails effacement-preservation OR scheme is admissibility-class-violating.
  - INFO: records retrofitted but cross-check against `_source_reconciliation_audit.py` post-V.2 extension reveals Class-(b) PIN-LOOSE-SOURCE-TIGHT drift ≥ S2 advisory; document + flag.
- **Substitution chain INSIDE gate block**:
  - Definition: CAC `w_0_FW(L) := rho_X(L) + offset_X`; `offset_X := w_0_FW − rho_X(L=10)`.
  - Substitute at L=10: `w_0_FW(L=10) = rho_X(10) + (w_0_FW − rho_X(10)) = w_0_FW`. Effacement-preservation EXACT.
  - Direction: PASS ⇔ retrofit preserves effacement at L=10 for all 2,828 records.
- **What PASS/FAIL MEAN**:
  - PASS: L2-PROMOTABLE records become CAC-compliant; eligible for §VII.K-PROP transitive-composition gate chain (#164).
  - FAIL: scheme drift surfaces; route to remediation per Class-(b).
- **Effort**: 0.6 wave-equivalents (2,828 records × per-scheme retrofit; bulk-vectorized pandas operation).
- **Substrate framing**: CAC IS the substrate-anchored convention; retrofit IS the methodology-layer F-image of substrate's effacement-preservation identity. Not "we apply the convention"; "the CAC IS the structural identity of effacement at L_anchor."

---

## §W13-164 W7-4 Layer-2 Warrant-Check Chain

- **Gate ID**: `S88-W7-4-LAYER-2-WARRANT-CHECK-CHAIN`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (transitive-composition gate chain generation).
- **Agent**: lizzi-spectral-functional-theorist.
- **Hypothesis**: The 1,515 L1-NUMERICAL records in `s87_w7_layer_audit_full.json` admit transitive-composition warrant-check gate chain via `permanent-results-registry.md` §VII.K-PROP (S86 W-8 4-Channel-LAYER-2 Sub-Decomposition + L2-Fully-Admissible Composition Theorem).
- **Method**:
  1. For each of 1,515 L1-NUMERICAL records: identify the upstream registry slot (§VII.A through §VII.AJ).
  2. Apply §VII.K-PROP transitive composition: `warrant(record) := warrant(upstream §VII slot) ∧ L2-admissible(record)`.
  3. Generate per-record warrant-check sub-gate (1,515 sub-gates total).
  4. Emit chain manifest `computations/s88_w13_warrant_check_chain.json`.
- **Machinery pin**:
  - Source: `s87_w7_layer_audit_full.json` L1-NUMERICAL filtered subset.
  - Composition theorem: `permanent-results-registry.md` §VII.K-PROP.
  - Chain operator: transitive composition per S86 W-8 RULE-1.
- **4-tuple input-pin map**: source JSON SHA-256; `permanent-results-registry.md` §VII.K-PROP SHA-256; `wave-classification.md` SHA-256; #163 verdict-line SHA-256 (must be PASS).
- **Thresholds**:
  - PASS: 1,515/1,515 records mapped to upstream §VII slot; chain manifest emitted; transitive composition closes for all (each record's warrant chain terminates at a closed §VII.* PASS or STAGE-3-PERMANENT).
  - FAIL: ≥1 record cannot be mapped, OR transitive composition does not close.
  - INFO: ≥1 record terminates at STAGE-1-CANDIDATE rather than STAGE-3-PERMANENT; document as conditional warrant; route to S89 once Stage-2 verifies land.
- **Substitution chain INSIDE gate block**:
  - Definition: transitive composition `warrant_chain(r) := r → upstream(r) → ... → §VII.* terminal`.
  - Substitute via §VII.K-PROP: each step preserves L2-admissibility.
  - Simplify: chain closes ⇔ terminal §VII.* is closed.
  - Direction: PASS ⇔ ∀ r ∈ 1,515 records: chain closes.
- **What PASS/FAIL MEAN**:
  - PASS: W7-4 L1-NUMERICAL corpus has full warrant chain to §VII; warrant-check infrastructure operational.
  - FAIL: chain breakage; remediation per-record.
- **Effort**: 0.8 wave-equivalents.
- **Substrate framing**: warrant chain IS the F-image of substrate's structural-confidence ladder at the L1-NUMERICAL layer; transitive composition IS the K-theory boundary map per cross-pillar-bridge-anatomy bridge map element.

---

## §W13-165 W7-5 Warrant-Head Subtest Implementation

- **Gate ID**: `S88-W7-5-WARRANT-HEAD-SUBTEST-IMPLEMENTATION`
- **Trigger**: [VERIFY]
- **Classification**: COMPUTE-class (subtest executor implementation).
- **Agent**: lizzi-spectral-functional-theorist (sole writer per W7-5 originating workshop).
- **Hypothesis**: The currently-stubbed `subtest_a`, `subtest_b`, `subtest_c` executors for `S87-WARRANT-CHECK-EPS-H-HP1-NORM` (which currently raise `NotImplementedError`) can be implemented to make the SECONDARY composite operational, using `eps_H_HP1_norm = 16.197719` from `permanent-results-registry.md` §VII-B.HP1-NEAR-INVARIANCE as the canonical anchor.
- **Method**:
  1. Read W7-5 originating workshop spec for subtest_a/b/c semantics.
  2. Implement each subtest in `computations/s87_w7_warrant_check_eps_h_hp1_norm.py` (S88 fork): subtest_a = scheme-invariance (across {Zubarev, zeta, Pauli-Villars, Mellin}); subtest_b = L_max-stability (L_max ∈ {8, 10, 12}); subtest_c = HP^1-cohomology-class membership.
  3. Execute SECONDARY composite (subtest_a ∧ subtest_b ∧ subtest_c).
  4. Emit per-subtest verdict + composite verdict.
- **Machinery pin**:
  - L_max scan: {8, 10, 12}.
  - Regulator scan: {Zubarev, zeta, Pauli-Villars, Mellin}.
  - Convention: per-subtest pinned (a: scheme-invariance; b: L_max-stability per CAC; c: HP^1-cohomology).
  - Anchor: `eps_H_HP1_norm_FW = 16.197719` from §VII-B.HP1-NEAR-INVARIANCE.
- **4-tuple input-pin map**: §VII-B.HP1-NEAR-INVARIANCE registry text SHA-256; `s87_w7_warrant_check_eps_h_hp1_norm.py` HEAD SHA-256 pre-implementation; `regulator-convention-lockdown.md` SHA-256; `canonical_constants.py` HEAD SHA-256.
- **Thresholds**:
  - PASS: subtest_a ∧ subtest_b ∧ subtest_c ALL-PASS; SECONDARY composite operational.
  - FAIL: ≥1 subtest FAILs.
  - INFO: ≥1 subtest INFO (e.g., scheme-invariance margins close to threshold); document + route to S89.
- **Substitution chain INSIDE gate block**:
  - Definition: SECONDARY composite `s := subtest_a(eps_H_HP1_norm) ∧ subtest_b(eps_H_HP1_norm) ∧ subtest_c(eps_H_HP1_norm)`.
  - Substitute: anchor value 16.197719 substituted into each subtest.
  - Simplify: each subtest is independent (scheme / L_max / cohomology axis).
  - Direction: PASS ⇔ all three subtest-axes preserve 16.197719 within tolerance.
- **What PASS/FAIL MEAN**:
  - PASS: SECONDARY composite operational; W7-5 warrant-head infrastructure complete; eps_H_HP1_norm structural-confidence ladder Level-2 + Level-3 anchored.
  - FAIL: subtest implementation surfaces inconsistency; eps_H_HP1_norm anchor revisit.
- **Effort**: 0.9 wave-equivalents (3 subtests × scheme/L_max scans + composite).
- **Substrate framing**: SECONDARY composite IS the F-image at the methodology layer of substrate's HP^1-cohomology-class structural identity; subtests are the audit-leg F-images.

---

## §W13-166 W7-5 Warrant Queue 25-Stub Triage

- **Gate ID**: `S88-W7-5-WARRANT-QUEUE-25-STUB-PROCESSING`
- **Trigger**: [VERIFY]
- **Classification**: METHODOLOGY-class (M1 ✓ stub-routing decision table existence; M2 ✓ JSON parse + table emission + Edit to plan files; M3 ✓ verbatim from `s87_w7_warrant_check_queue_stubs.json` 25 entries; M4 pending).
- **Agent**: lizzi-spectral-functional-theorist (sole writer per W7-5 originating workshop) + gen-physicist orchestrator-direct-write (queue triage classification).
- **Hypothesis**: The 25 deferred 4-field stubs in `s87_w7_warrant_check_queue_stubs.json` admit triage to one of three routes: (i) S88-plan inclusion (immediate execution this session); (ii) S89+ deferral (4-field spec carries forward); (iii) closure-as-not-applicable (stub structurally moot due to upstream change).
- **Method**:
  1. Parse `s87_w7_warrant_check_queue_stubs.json`; enumerate 25 stubs with their 4-field specs.
  2. For each stub: read upstream context (cited workshop / registry slot / canonical constant).
  3. Apply triage decision rule per `feedback_fix-in-session-never-defer.md` 4-field test (what / inputs / gate / effort) AND `feedback_fix-in-session-never-defer.md` no-padding rule.
  4. Route per stub: (i) inclusion in S88 W14+ plan blocks; (ii) S89+ carry-forward with refreshed 4-field spec; (iii) closure-as-not-applicable with rationale.
  5. Emit triage manifest `computations/s88_w13_warrant_queue_triage.json`.
- **Machinery pin**: triage decision rule = 4-field-test + no-padding-rule conjunction; routing = per-stub (i)/(ii)/(iii) tag.
- **4-tuple input-pin map**: `s87_w7_warrant_check_queue_stubs.json` SHA-256; `feedback_fix-in-session-never-defer.md` SHA-256; `feedback_fix-in-session-never-defer.md` SHA-256; `methodology-wave-allowlist.md` SHA-256.
- **Thresholds**:
  - PASS: 25/25 stubs triaged; route distribution emitted; route-(i) stubs landed in S88 W14+ plan blocks within this session; route-(ii) carry-forwards have refreshed 4-field specs; route-(iii) closures have rationale.
  - FAIL: ≥1 stub triage incomplete (no route assigned), OR route-(i) stub not landed in plan block, OR route-(ii) lacks 4-field spec.
  - INFO: triage borderline on ≥1 stub (4-field-test ambiguous); document + escalate to user.
- **Substitution chain INSIDE gate block**:
  - Definition: triage(stub) ∈ {(i), (ii), (iii)} per 4-field-test ∧ no-padding-rule.
  - Substitute: 4-field test = (what specified ∧ inputs available ∧ gate threshold defined ∧ effort estimable); no-padding = (NOT hygiene-on-already-correct).
  - Simplify: route-(i) ⇔ 4-field-test PASS ∧ no-padding PASS ∧ inputs available NOW; route-(ii) ⇔ 4-field-test PASS ∧ no-padding PASS ∧ inputs require S89+ work; route-(iii) ⇔ 4-field-test FAIL OR no-padding FAIL.
  - Direction: PASS ⇔ all 25 stubs cleanly triaged.
- **What PASS/FAIL MEAN**:
  - PASS: W7-5 warrant queue cleared; queue discipline operational; no orphan stubs.
  - FAIL: queue stubs remain unrouted; technical debt accumulates.
  - INFO: borderline stubs flagged for user review.
- **Effort**: 0.5 wave-equivalents (25 stubs × per-stub triage decision).
- **Substrate framing**: queue IS the methodology-layer projection of the substrate's pending-warrant structural state; triage IS the F-image at the audit leg (route-(i) lands in audit immediately; route-(ii) defers; route-(iii) closes). Not "we process the queue"; "the queue IS the F-image of pending warrants, and the triage IS the structural decision rule."

---

## Wave 13 → S89 Decision Point

After Wave 13 closes, the following decisions feed S89 plan:

1. **#149 PASS or FAIL**: if FAIL, S89 W0 leads with re-classification of the failing S87 wave.
2. **#150 INFO**: if hook fires but injection mechanism incomplete on Windows shell-quoting, S89 W0 includes shell-quoting fix as MANDATORY.
3. **#152 FAIL**: if MCP fabrication-rate > 0, S89 W0 includes fabrication-event remediation as leading carry-forward.
4. **#153 PASS**: triplet-verification complete; T2-7 layer-functor F formally promoted to STAGE-3-PERMANENT in `epistemic-discipline.md` §"Layer-Decomposition" via S89 W0 methodology landing.
5. **#157 LIFTED** (2026-05-06): not dispatched this session; carry-forward to `/rclab-investigate` per §W13-157 LIFT NOTICE. The S89-side Path-B Step-1 + Step-2 + Step-3 pre-registration is contingent on the future workshop-schedule landing of this carry-forward.
6. **#159 PASS** ⇒ **#160 PASS** ⇒ **S89 Stage-2 cross-axis independent-verify**: dispatch `S89-INTEGER-GRADED-ANOMALY-MULTIPLIER-THEOREM-INDEPENDENT-VERIFY` per joint-theorem-promotion.md Stage-2 pathway.
7. **#161 PASS**: OEIS structural alignment cross-link added to STAGE-1-CANDIDATE entry (orchestrator-direct edit).
8. **#162 PASS** ⇒ **W7-4 audit Class-8.2 vulnerability formally closed**: remove rubric-class-8.2 flag from W7-4 historical entries in next plan.
9. **#163 PASS** ⇒ **#164 dispatch unblocked**.
10. **#164 PASS**: 1,515 L1-NUMERICAL records become first-class warrant-check eligible.
11. **#165 PASS**: SECONDARY composite for eps_H_HP1_norm operational; HP^1-cohomology axis Level-3 anchored.
12. **#166 route-(i) stubs**: land in S88 W14+ plan blocks (within this session); route-(ii) stubs propagate to S89 plan via `/rclab-plan`.

---

## Wave 13 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness" PRDR discipline, every gate's machinery is enumerated above in the per-gate "Machinery pin" field. Cross-cutting machinery shared by multiple gates:

| Machinery | Pinned Value | Gates citing |
|:----------|:-------------|:-------------|
| L_max canonical | 10 (operational); 12 (master cache) | #158, #159, #163, #165 |
| L_max scan range | {6, 8, 10, 12} for #158; {8, 10, 12} for #165 | #158, #165 |
| Regulator default | Zubarev (per S85 W0-7 NPZ) | #163 |
| Regulator scan set | {Zubarev, zeta, Pauli-Villars, Mellin} | #165 (subtest_a) |
| PRIMARY regulator | Pauli-Villars + mass-scale running per Connes-Chamseddine 1996 §2.2-2.3 | #158, #159 |
| Convention canonical | CAC per `regulator-convention-lockdown.md` | #163 |
| Composition theorem | §VII.K-PROP per S86 W-8 RULE-1 | #164 |
| Spectrum cache | `s84_spectrum_cache_L12_tau019.npz` (155,984 eigenvalues at L_max=10 filter) | #159 |
| LAYER audit JSON | `s87_w7_layer_audit_full.json` (15.9 MB; 34,876 records / 748 files; 1,515 L1-NUMERICAL + 2,828 L2-PROMOTABLE) | #162, #163, #164 |
| Warrant queue stubs | `s87_w7_warrant_check_queue_stubs.json` (12,280 B; 25 stubs) | #166 |
| Wave-classification rule | `wave-classification.md` M1-M4 strict conjunction | #149 (subject); all (M1-M4 self-classification) |
| Allowlist | `methodology-wave-allowlist.md` orchestrator-only-edit | #149 (subject), #150-156, #160, #166 (M4 pending) |
| Layer-functor T2-7 | `epistemic-discipline.md` §"Layer-Decomposition" 5-mapping | #153 (subject), all (substrate framing) |
| Workshop dispatch protocol | 3-round R1/R2/R3; 4-agent panel for #157 | #157 |
| Knowledge MCP pre-query | Mandatory per CLAUDE.md | all |

---

## Wave 13 Input-SHA Ledger

> **Note**: SHA-256 values computed at plan-freeze time (S88 plan-freeze validator runs `_source_reconciliation_audit.py` followed by `_pru_cardinality_audit.py` followed by SHA-256 emission per the §"Source Reconciliation" pipeline composition order). Placeholders below resolved at plan-freeze.

| Pin | File / Object | SHA-256 (plan-freeze) |
|:----|:-------------|:---------------------|
| `pin_methodology_allowlist` | `.claude/rules/methodology-wave-allowlist.md` HEAD-of-S87 | `<pinned at plan-freeze>` |
| `pin_wave_classification` | `.claude/rules/wave-classification.md` HEAD | `<pinned at plan-freeze>` |
| `pin_epistemic_discipline` | `.claude/rules/epistemic-discipline.md` HEAD | `<pinned at plan-freeze>` |
| `pin_layer_decomposition_t2_7` | `epistemic-discipline.md` §"Layer-Decomposition" sub-section | `<pinned at plan-freeze>` |
| `pin_v3_closure_recovery` | `.claude/rules/v3-closure-recovery.md` HEAD | `<pinned at plan-freeze>` |
| `pin_phononic_framing` | `.claude/rules/phononic-framing.md` HEAD | `<pinned at plan-freeze>` |
| `pin_substrate_first_canonical` | `.claude/rules/substrate-first-canonical-sourcing.md` HEAD | `<pinned at plan-freeze>` |
| `pin_regulator_convention_lockdown` | `.claude/rules/regulator-convention-lockdown.md` HEAD | `<pinned at plan-freeze>` |
| `pin_joint_theorem_promotion` | `.claude/rules/joint-theorem-promotion.md` HEAD | `<pinned at plan-freeze>` |
| `pin_cross_pillar_bridge_anatomy` | `.claude/rules/cross-pillar-bridge-anatomy.md` HEAD | `<pinned at plan-freeze>` |
| `pin_investigating_workshops` | `.claude/rules/Investigating-Workshops.md` HEAD | `<pinned at plan-freeze>` |
| `pin_settings_json_pre` | `.claude/settings.json` pre-W13-edit | `<pinned at plan-freeze>` |
| `pin_canonical_constants` | `computations/canonical_constants.py` HEAD-of-S88 | `<pinned at plan-freeze>` |
| `pin_permanent_results_registry` | `sessions/permanent-results-registry.md` HEAD-of-S88 | `<pinned at plan-freeze>` |
| `pin_falsifier_master_inventory` | `sessions/framework/registry/falsifier-master-inventory.md` HEAD-of-S88 | `<pinned at plan-freeze>` |
| `pin_w7_layer_audit_json` | `computations/s87_w7_layer_audit_full.json` (15.9 MB) | `<pinned at plan-freeze>` |
| `pin_w7_warrant_queue_stubs` | `computations/s87_w7_warrant_check_queue_stubs.json` (12,280 B) | `<pinned at plan-freeze>` |
| `pin_spectrum_cache_l12` | `computations/s84_spectrum_cache_L12_tau019.npz` | `<pinned at plan-freeze>` |
| `pin_w0_7_zubarev_npz` | `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz` | `<pinned at plan-freeze>` |
| `pin_s87_plan_w9a` | `sessions/session-plan/session-87-plan-w9a.md` | `<pinned at plan-freeze>` |
| `pin_s87_plan_w11` | `sessions/session-plan/session-87-plan-w11.md` | `<pinned at plan-freeze>` |
| `pin_s86_w13_workshop` | `sessions/archive/session-86/workshops/s86-permission-topology-methodology-unification.md` | `<pinned at plan-freeze>` |
| `pin_s85_5a_workshop` | `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` | `<pinned at plan-freeze>` |
| `pin_w7_3_workingpaper` | S87 W7-3 working-paper section SHA-256 | `<pinned at plan-freeze>` |
| `pin_w7_5_workingpaper` | S87 W7-5 working-paper section SHA-256 | `<pinned at plan-freeze>` |
| `pin_feedback_max_8_subagents` | `~/.claude/projects/.../feedback_dispatch-discipline.md` | `<pinned at plan-freeze>` |
| `pin_feedback_carry_forward_mandatory` | `~/.claude/projects/.../feedback_fix-in-session-never-defer.md` | `<pinned at plan-freeze>` |
| `pin_feedback_fix_in_session_never_defer` | `~/.claude/projects/.../feedback_fix-in-session-never-defer.md` | `<pinned at plan-freeze>` |

> **AMRI note (per `agent-standards.md` §"AMRI"): the three `pin_feedback_*` entries are AGENT-PRIVATE memory paths and would normally trigger AMRI Test 1 (input-pin test). However, these pins are referenced ONLY in #154 (max-8 hook promotion) and #166 (queue triage) where the rule-text content is verbatim copied into the hook-script and triage-decision-rule respectively at gate-execution time; the SHA pin is for content-stability audit only, not for cross-gate authority sourcing. Per the user's 2026-04-28 calibration ("taking a note is allowed; the issue is using memories as the pin source"), these pins are AMRI-CLEAN because the canonical rule content is in `.claude/rules/` and the feedback files are agent-housekeeping copies. If the AMRI audit at plan-freeze flags these, route to project-level promotion via `sessions/framework/registry/feedback-rule-promotion.md` (S88 carry-forward).

---

## Wave 13 Closing Notes

- All 18 items follow per-gate 13-field spec at FULL fidelity per spawn discipline.
- METHODOLOGY-class items (#149-156, #160, #166) dispatch via orchestrator-direct-write per `wave-classification.md` §"Dispatch consequences" + `team-lead-behavior.md` §"METHODOLOGY-Class Wave Discipline".
- COMPUTE-class items (#159, #162-165) dispatch via `/rclab-coordinate` compute-mode.
- PARTICLE/cosmology-class items: **#157 LIFTED** to `/rclab-investigate` carry-forward 2026-05-06 (see §W13-157 LIFT NOTICE; not dispatched this session). #158 NCG-axiomatic dispatches via the named NCG agent (connes-ncg-theorist).
- Substrate framing per `phononic-framing.md` §"IS Space, Not IN Space" enforced in every gate's "Substrate framing" field; container-thinking inversions FORBIDDEN.
- `verdict_source: computations/s88_gate_verdicts.txt`.
- Script prefix: `s88_w13_<slug>.py` for COMPUTE-class items; orchestrator-direct edits for METHODOLOGY-class items (no `.py` script per M2 forbidden-operations enumeration).

> **End of W13 plan.** 18 items / 13-field spec each / orchestrator-direct-write authoring per `wave-classification.md` METHODOLOGY-class discipline. Dispatch order at S88 W13 invocation: #150 (hook implementation foundational), then #149 + #151 + #152 + #154 (audit cluster), then #155 + #156 (corroboration), then #153 (layer-functor verification), then #158 (NCG-axiomatic; #157 LIFTED to `/rclab-investigate` carry-forward 2026-05-06 — see §W13-157 LIFT NOTICE), then #159 (must precede #160 + #161), then #160 + #161, then #162 (must precede #163), then #163 + #164 (sequential), then #165, then #166 (final triage).
