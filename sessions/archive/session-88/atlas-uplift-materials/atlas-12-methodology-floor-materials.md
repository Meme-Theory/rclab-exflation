# Atlas-12 Methodology-Floor — Materials Packet

**Date drafted**: 2026-05-09
**Session**: S88 atlas-uplift campaign
**Target file** (orchestrator will Write): `sessions/framework/Atlas/atlas-12-methodology-floor.md`
**Companion atlas (substrate-side)**: `atlas-11-cross-pillar-bridge-corpus.md` (substrate-IS bridges)
**This atlas (methodology-side)**: process / discipline / audit-trail infrastructure that emerged S82-S88

**Substrate-framing discipline**: this atlas describes HOW the substrate is investigated, NOT WHAT the substrate IS. Atlas-12 is the audit-trail-layer atlas of the layer-functor F. Cross-link to atlas-11 (substrate-IS bridges) makes the substrate-vs-methodology orthogonality explicit. Methodology rules are NOT physics — they govern process.

---

## Section 1 — Atlas-12 structure design (15 sections, refined)

The recommended structure aligns with the methodology-floor's natural decomposition: layer-functor F is the structural backbone (II), Phi correspondence is its weight-pin (III), the four taxonomies (IV–VI) are the rule-engine, the cleanup history (VIII) and audit-trail (IX–X) are the closure machinery, and (XV) is the forward queue.

| § | Title | Role (1 paragraph) |
|:--|:------|:-------------------|
| I | Introduction — what is the methodology floor? | Frames the methodology floor as the substrate ↔ methodology ↔ audit infrastructure that emerged S82-S88. Establishes the substrate-framing discipline (rules govern process, not physics). Cross-links to atlas-11 (substrate-IS bridges) and atlas-04 (assumed-and-proven items). Sets the section-flow expectation: structural backbone (II–III), rule taxonomies (IV–VII), cleanup + workshop discipline (VIII–IX), specific disciplines (X–XIV), forward debts (XV). |
| II | Layer-functor F: substrate ↔ methodology ↔ audit | Specifies F as the formal map from substrate-physics quantities (eigenvalue, numerical PASS predicate, machinery pin, verdict-line value, fixture-by-construction) to their methodology images (rule-file content, artifact-existence predicate, input-pin map, verdict-line artifact-SHA, orchestrator-direct-without-cross-actor) to their audit images (audit-line content, SHA-uniqueness predicate, `closure_hash(input_pin_map) = audit_sha256`, audit_sha256, SHA-hardcoding bug). Frames F as Morita-equivalence-preserving for PRU-class invariants. Anchored at `epistemic-discipline.md §"Layer-Decomposition"` (line 321). |
| III | Phi correspondence: weight(a_n^SD) = weight(Σ_n) | The graded-ring-isomorphism Phi maps `weight(a_n^SD) = n` substrate-side to `weight(Σ_d) = enforcement-strength` methodology-side: `Phi(a_0) = Σ_1` (perimeter / cosmological term, weight-0; user-adjudication-only deliverable); `Phi(a_2) = Σ_2` (Einstein-Hilbert kinematic skeleton, weight-2; wave-classification); `Phi(a_4) = Σ_3` (Yang-Mills + Higgs quartic load-bearing, weight-4; mcp-pre-check hook). Anchored at `epistemic-discipline.md §"Phi correspondence"` (line 349). |
| IV | PRU Class 8.0–8.6 sub-class taxonomy | Enumerates the 7 sub-classes: 8.0/8.1 machinery-pin cardinality (S78 origin, MANDATORY); 8.2 verifier-rubric pre-registration (W-12 origin, MANDATORY at K=5); 8.3 output-precision pre-registration (W1c-8 origin, MANDATORY at K=4); 8.4 representation-convention-pin (W5b-50, K=1 advisory); 8.5 joint-hypersurface-pre-registration-form (W4c-36, K=1 advisory); 8.6 layered-substitution-chain-audit (W5b-47, K=1 advisory). Each entry cites parent rule + corpus location + status. |
| V | Joint-theorem 4-stage promotion pathway | Specifies the 4-stage upgrade pathway (Stage 0 workshop-internal candidate → Stage 1 next-session registry as STAGE-1-CANDIDATE → Stage 2 two-agent parallel cross-check on different axes WITHOUT prior workshop context → Stage 3 STAGE-3-PERMANENT). Frames it as the constructive complement to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 (the "agreement among agents" exclusion). Includes Axis-B Selection Protocol (axis-distinctness + downstream-inheritance reach test + audit-coverage adequacy) and substrate-input-orthogonality clause. |
| VI | Methodology-wave classification (M1–M4 strict conjunction) | Defines the 4-test conjunction for METHODOLOGY-class waves: M1 (PASS predicate is artifact-existence-with-substantive-content, NOT numerical comparison) AND M2 (producing operations restricted to Edit/Write/MultiEdit on `.claude/{rules,templates,skills}/**`) AND M3 (source-of-truth is verbatim sub-diff from prior closed workshop / verbatim 5-class taxonomy / anchor-citation-only landing) AND M4 (gate-ID appears in `methodology-wave-allowlist.md`). NROY clause: a wave cannot be both COMPUTE-class and METHODOLOGY-class. MIXED-class waves MUST be sub-decomposed. |
| VII | Methodology-wave allowlist (append-only, orchestrator-only) | Specifies the allowlist as M4 substrate: append-only, orchestrator-only edit by harness convention (closes the recursion attack where a subagent could append its own gate-ID for self-promotion). 3-column schema (gate_id | session | sha256_of_plan_block). Per-instance rationale prose lifted to `sessions/framework/registry/methodology-wave-instances.md` at S88 W9-RULE-CLEANUP. Currently ~62 rows across S86–S88. |
| VIII | AMRI cleanup history | Documents the Agent-Memory Registry Inversion discipline: agent memory stores AGENT-PRIVATE context only; project-level registries live under `sessions/framework/<registry>.md` + `tools/knowledge.db`. AMRI tests (input-pin / output-target / cross-agent overlap) detect inversions; calibration corpus enumerates the S87 W0 + earlier promotions. Detection tool: `_agent_memory_inversion_audit.py`; migration tool: `/shortterm <agent>`. |
| IX | Workshop methodology (Investigating-Workshops 4-condition definition + 3-question discriminator) | Specifies the 4-condition definition (TWO+ agents with COMPETING perspectives + genuine ledger-dissonance + multi-round structure + STRUCTURAL VERDICT output). Specifies the 3-question discriminator (Q1 math/physics adjudication → workshop; Q2 hygiene/framework-issue → WP CF; Q3 parallel-compute-wave → WP CF wave-together). Workshop-schedule format separates workshop OUTCOMES from carry-forward COMPUTATIONS. **Recommend split**: see Section 3 flag #5 — single section is acceptable because the 3-question discriminator is structurally coupled to the 4-condition definition (the discriminator EXPLAINS the definition's boundary); splitting would over-fragment. |
| X | Mechanical-closure discipline + Layer-separability carve-out | Specifies orchestrator-authored verdict-line emission for upstream-blocked gates (5-clause acceptability: upstream-block topology + verdict honesty + per-gate-distinct audit_sha256 + audit-trail signature + working-paper update in-script). Layer-separability carve-out (S88 W8-89; SUGGESTION at K=1) admits closed-form mechanical evaluation on Type-F (single-summand-projection-trace) sub-observables WITH conditions L1–L4 + Stage-2 PASS-AND. PLANNING DEFECT trigger fires at covered_count ≥ 4. |
| XI | Substrate-first canonical-sourcing | External-paper provenance is METHODOLOGICAL (cross-check) not CANONICAL (replacement). 4-step audit pattern: external-paper heading glob → placeholder pattern detection → schematic library helper detection → substrate-first computation citation. SCHEMATIC vs full physical level pin (MANDATORY at K=4 promotion, S88 W7b-83). Class-(f) PIN-PLACEHOLDER taxonomy. |
| XII | Registry-landing conventions (SOURCE-DOUBLE-CITE-CO-PRIMARY, OP-PROJ vs STATE-PROJ naming) | SOURCE-DOUBLE-CITE-CO-PRIMARY for sequential V_input + C_output chains (NOT PRIMARY+CONFIRMATION which assumes parallel independence). 4-condition detection (sequential, non-fungible, both-anchors-accessible, same-algebra-axis-cell). Bridge-Landing Script Architecture (single-shot pattern: write → fsync → re-read → verify → emit). Operator-Projection Reading-A naming hygiene (MANDATORY at K=3): suffix tag `§VII.X.OP-PROJ` (algebra-side) vs `§VII.X.STATE-PROJ` (state-side). |
| XIII | Verifier-rubric pre-registration (Class 8.2) | When a gate's PASS criterion involves rubric-grading of qualitative content, the gate MUST pre-register the verifier rubric (pattern set + disjunction-vs-conjunction declaration + negative-marker set + pre-registered calibration corpus pinned by SHA). MANDATORY at K=5 (post-S88 W-7/W-21/W-22 simultaneous advancement). |
| XIV | Publication-precision pre-registration (Class 8.3) | When a gate's output VALUE will be cited downstream, pre-register publication precision (sig-fig pin + verifier tolerance match + round-trip cross-check + canonical-metric pin + algebraic-equivalence audit at plan-authorship). MANDATORY at K=4. |
| XV | Forward methodology debts | Open process work: K-counter advancements pending (8.4/8.5/8.6 advisory at K=1; Hybrid Independence Test K=1; substrate-input-orthogonality clause K=1; closing-paragraph-coherence audit pattern K=1); audit-script extension queue (`_substrate_first_provenance_audit.py`, `_joint_theorem_independent_verify_audit.py` extensions, `_registry_landing_audit.py` Class-(g) flags, `_machinery_feasibility_audit.py` boundary-direction sub-check); functional-selection methodology open question. |

---

## Section 2 — Per-section content

### Section I — Introduction

**Frame**: The methodology floor is the substrate ↔ methodology ↔ audit infrastructure that emerged S82-S88. It includes 24 framework rule files at `.claude/rules/`, 9 templates at `.claude/templates/` (+1 frozen example at `.claude/templates/examples/`), the layer-functor F (substrate → methodology → audit triplet), PRU Class 8.0–8.6 sub-class taxonomy, the joint-theorem 4-stage promotion pathway, AMRI (Agent-Memory Registry Inversion) cleanup history, methodology-wave classification, and the workshop methodology.

**Pin to atlas-11**: atlas-11 is the substrate-side new atlas (cross-pillar-bridge-corpus, ~24 entries with 5-anatomy + 3-level ladder); atlas-12 is the methodology-side new atlas (the discipline that ENFORCES atlas-11's anatomy). The two atlases are STRUCTURALLY ORTHOGONAL: atlas-11 captures substrate-IS observables; atlas-12 captures methodology rules that govern HOW the substrate is investigated. Cross-corner co-primary between atlas-11 and atlas-12 is FORBIDDEN per the algebra-axis orthogonality K-counter MANDATORY clause.

**Pin to atlas-04** (assumptions): the methodology floor includes assumed-and-proven items (process axioms): (a) plan-freeze-time pre-registration is binding; (b) verdict permanence (Option A protocol); (c) PROHIBITED_ACTIONS Class 1–4 (convention-shopping, iterate-until-PASS, post-hoc pre-registration editing, ansatz-forced PASS); (d) orchestrator-only edit on rule files (closes recursion attack).

**Pin to atlas-09** (retractions): AMRI cleanups are SUPERSESSIONS — agent memory entries that were promoted to project-level registries and SUPERSEDED at the original location. See cross-link in Section VIII.

---

### Section II — Layer-functor F: substrate ↔ methodology ↔ audit

**Source**: `epistemic-discipline.md §"Layer-Decomposition"` (line 321).

**Substrate ↔ methodology pair**:

| Substrate-physics quantity | Methodology image under F |
|:---------------------------|:--------------------------|
| eigenvalue                 | rule-file content          |
| numerical PASS predicate   | artifact-existence predicate |
| machinery pin              | input-pin map              |
| verdict-line numerical value | verdict-line artifact-SHA |
| fixture-by-construction    | orchestrator-direct-without-cross-actor |

**Methodology ↔ audit pair**:

| Methodology quantity | Audit-leg image under F |
|:---------------------|:------------------------|
| rule-file content    | audit-line content      |
| artifact-existence predicate | SHA-uniqueness predicate |
| input-pin map        | `closure_hash(input_pin_map) = audit_sha256` (S82 W1 helper) |
| verdict-line artifact-SHA | `audit_sha256` (self-referential at audit layer) |
| orchestrator-direct-without-cross-actor | SHA-hardcoding bug (v3-closure-recovery sig_5) |

**Morita-equivalence framing**: F preserves PRU-class invariants analogous to how Mor_NCG preserves K-theoretic invariants. A PRU Class-8.2 violation at the substrate layer (verifier-rubric pre-registration failure) maps under F to an analogous failure at the methodology layer (rule-file pre-registration failure) and at the audit layer (audit-line pre-registration failure). The Class-8 sub-taxonomy (8.0/8.1/8.2/8.3) is preserved by F.

**Status**: pair-verified at S86 R3 (substrate ↔ methodology pair); audit-leg verification pending S87 (per `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` carry-forward). Triplet structurally extended at R3-connes via the 5-mapping reproduction; empirical audit-leg corroboration required to upgrade from pair-verified to triplet-verified.

**Definitional-datum-vs-derived-theorem K-counter**: K=2 at 2026-05-08; advisory until K=3. Distinguishes definitional-datum (true by construction at one layer of F) from derived-theorem (true by structural derivation at a different layer). Future plan-blocks claiming substrate-IS evidence MUST declare which layer of F the evidence sits at.

**F(observable) vs F(trigger predicate) split**: K=1; F applies DIFFERENTLY to observables vs trigger predicates. F(observable) preserves multi-axis structural content; F(trigger) is rule-text-evidence-governed and MAY be single-axis.

---

### Section III — Phi correspondence: weight(a_n^SD) = weight(Σ_n)

**Source**: `epistemic-discipline.md §"Phi correspondence"` (line 349).

**Substitution chain — Phi correspondence is a graded-ring isomorphism**:

```
Step 1 (Definition):  weight(a_n^SD) = n  (Seeley-DeWitt grading on substrate side)
Step 2 (Definition):  weight(Σ_d) = enforcement-strength (rule weight on methodology side)
Step 3 (Map):         Phi : weight(a_n^SD) → weight(Σ_d)
Step 4 (Pin n=0):     Phi(a_0) = Σ_1   (perimeter / cosmological term, weight-0
                                         maps to user-adjudication-only deliverable)
Step 5 (Pin n=2):     Phi(a_2) = Σ_2   (Einstein-Hilbert kinematic skeleton,
                                         weight-2 maps to wave-classification)
Step 6 (Pin n=4):     Phi(a_4) = Σ_3   (Yang-Mills + Higgs quartic load-bearing,
                                         weight-4 maps to mcp-pre-check hook)
Step 7 (Extension):   weight-n substrate observable → enforcement-strength-n
                       methodology rule for all n
```

**Direction**: the higher the Seeley-DeWitt weight on the substrate side, the more load-bearing the methodology rule on the discipline side. The substrate's gravity (a_2) matches the methodology's wave-classification kinematic skeleton; the substrate's Yang-Mills + Higgs quartic (a_4) matches the methodology's load-bearing pre-tool-call hook.

---

### Section IV — PRU Class 8.0–8.6 sub-class taxonomy

**Source**: `epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`.

| Sub-class | Name | Origin | Status | Corpus location |
|:----------|:-----|:-------|:-------|:----------------|
| 8.0 / 8.1 | machinery-pin cardinality failure | S78 (original Class 8) | MANDATORY | parent rule + Source-Reconciliation 6-class taxonomy |
| 8.2 | verifier-rubric pre-registration failure | S86 W-12 ("Z_4 or similar" admitted V_4) | MANDATORY at K=5 (post-S88 W-7 + W-22 + W-21 simultaneous K=2→K=5 advancement, 2026-05-08) | `pru-class-corpus.md §1` |
| 8.3 | output-precision pre-registration failure | S86 W1c-8 (10 vs 15 sig figs) | MANDATORY at K=4 (post-S87 W8) | `pru-class-corpus.md §2` |
| 8.4 | representation-convention-pin failure | S88 W-16 W5b-50 V.5 (operator-domain dim > natural rep dim of substrate algebra; Pad-block convention dependence) | K=1 advisory until K=3 | `pru-class-corpus.md §5` |
| 8.5 | joint-hypersurface-pre-registration-form failure | S88 W-15 W4c-36 V.9 (gates consuming substrate-IS through CHILD pin must emit 2D hypersurface verdict-line value field) | K=1 advisory until K=3 | `pru-class-corpus.md §6` |
| 8.6 | layered-substitution-chain-audit failure | S88 W-17 W5b-47 V.5 (3-layer substitution chain crossing §VII.U.2 corner cells; arithmetic / parse-tree / operationalization layers must be pre-registered) | K=1 advisory until K=3 | `pru-class-corpus.md §7` |

**Source-Reconciliation Class-(a)–(f) taxonomy** (companion to Class 8.0/8.1): (a) PIN-TIGHT-SOURCE-LOOSE; (b) PIN-LOOSE-SOURCE-TIGHT (highest-leverage; FALSE-PASS direction); (c) PIN-DRIFT-FROM-STALE-SOURCE (with c.OOM-misread sub-class); (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY; (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS; (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL (MANDATORY at K=4, S88 W7b-83 close).

**Pre-Registration Completeness — Closing-Paragraph-Coherence Audit Pattern (EG1)** — S88 W-25 W7c-167 §V CF #8 (sagan + gen-physicist closing-paragraph-coherence workshop). K=1 SUGGESTION pending K=3 MANDATORY. For any rule-file section composed of (i) enumerated antecedent list + (ii) closing paragraph that disambiguates rule behavior, plan-freeze auditors MUST apply the closing-paragraph-coherence test: (1) identify two competing structural readings (literal-independent vs strict-conjunctive), (2) test each reading against the closing paragraph's qualifying language, (3) reject the reading that produces self-contradiction.

---

### Section V — Joint-theorem 4-stage promotion pathway

**Source**: `joint-theorem-promotion.md` (S86 W-9).

**Stage 0** — Workshop-Internal Candidate. Joint theorem candidate text drafted by 2 workshop authoring agents on different axes; clauses stated with explicit author-side attribution. Workshop-internal artifact only.

**Stage 1** — S87 (next-session) Registration as Candidate. Full theorem text + 4-stage tag `STAGE-1-CANDIDATE` + identification of joint clauses. Downstream gates may CITE the candidate but must include the qualifier.

**Stage 2** — Two-Agent Parallel Cross-Check (mandatory upgrade gate). TWO independent cross-reviewers, ONE per axis, dispatched in parallel, BOTH operating WITHOUT prior workshop context. JOINT clauses PASS-AND'd across the two verdicts.

**Stage 3** — Permanent Registration. Replace `STAGE-1-CANDIDATE` with `STAGE-3-PERMANENT`. Theorem joins permanent-results table.

**Axis-B Selection Protocol** (S88 W-14 W4a-17 V.2; B.15): MUST satisfy (1) axis-distinctness; (2) original-authoring-agent exclusion with downstream-inheritance reach test; (3) audit-coverage adequacy. K=1 calibration: lizzi's project memory inherited from S87 W-9 R3-B Path-(c) lock-in via direct re-citation — the downstream-inheritance reach test fires, requiring re-dispatch with non-lizzi spectral-side reviewer (re-routed to connes-ncg-theorist).

**Substrate-input-orthogonality clause** (S88 W-23 W7c-167 V.1; B.56): for any Stage-2 verification with N ≥ 2 observables, ∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer. K=1 SUGGESTION pending K=3 MANDATORY. Stage-2 PASS-AND verdicts emitted under SUGGESTION status carry an explicit substrate-input-overlap caveat when the predicate fails.

**Cross-link to "What Does NOT Count as Evidence" item 2**: the 4-stage pathway is the constructive complement to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2. "Agreement among agents" with shared workshop context → still NOT evidence. "Agreement among agents" with NO shared context (Stage 2 cross-reviewers reading only the registered Stage-1 entry) → IS evidence.

**Calibration corpus**: S86 W-9 Joint F_2-Class Path-(c) Theorem (lizzi+transit), 6-clause statement (a)–(f) with 4 corrigenda. Joint clauses (c) and (d). Stage 1 queued as `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` (CF-1); Stage 2 queued as `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (CF-6); Stage 3 blocked on Stage 2 PASS.

---

### Section VI — Methodology-wave classification (M1–M4 strict conjunction)

**Source**: `wave-classification.md` (S86 W-13 RULE-1 / Sigma_2).

A wave is METHODOLOGY-class iff ALL FOUR tests hold (strict logical conjunction):

- **M1 — PASS predicate type**: artifact-existence-with-substantive-content, NOT numerical comparison. PASS iff (file F exists at P) AND (F contains §S) AND (substantive_line_count(§S) ≥ 15) AND (content_sha256(§S) matches input-pin-map-derived hash).
- **M2 — Producing-operation type**: restricted to Edit/Write/MultiEdit on `.claude/{rules,templates,skills}/**`, grep/wc/SHA-256 cross-checks, integer counts. FORBIDDEN: any `.py` script whose output is a numerical comparison.
- **M3 — Source-of-truth type**: verbatim sub-diff from prior closed workshop / verbatim 5-class taxonomy / anchor-citation-only landings. FORBIDDEN: first-principles new derivation.
- **M4 — Allowlist membership**: gate-ID appears in `methodology-wave-allowlist.md`.

**Strict-conjunction**: ALL FOUR must hold. Any one failure routes to COMPUTE-class fallthrough OR MIXED-class triage.

**NROY clause**: a wave CANNOT be both COMPUTE-class and METHODOLOGY-class. MIXED-class waves MUST be sub-decomposed before plan-freeze.

**Forward-pinned-follow-up wave class** (S88 W-25 W7c-167 §V.2; SUGGESTION at K=1): orthogonal axis to the count-keyed PLANNING DEFECT trigger; structural-class-keyed via M1'-M4' analog.

**Calibration corpus**: 4 W0a rows landed at S86 R3 per no-technical-debt rule (W0a-1, W0a-3, W0a-5 pure METHODOLOGY; W0a-2 MIXED → W0a-2a + W0a-2b sub-decomposed).

---

### Section VII — Methodology-wave allowlist (append-only orchestrator-only)

**Source**: `methodology-wave-allowlist.md` (S86 W-13 / Sigma_5; per-instance provenance at `methodology-wave-instances.md`).

**Schema** (3-column, post-S88 W9-RULE-CLEANUP lift-out):
```
gate_id | session | sha256_of_plan_block
```

**Edit discipline** (4 rules):
1. Append-only (rows MAY be added; rows MAY NOT be removed/reordered/modified post-landing)
2. Orchestrator-only edit (subagents denied Edit/Write/MultiEdit by harness convention) — closes the recursion attack
3. Per-row dual-SHA (computed via `closure_hash(plan_block_text)`)
4. Append-helper writes 3-column rows only + parallel registry entry per `### {gate_id} ({session}) — {sha}`

**Recursion-attack closure**: WITHOUT orchestrator-only edit, a subagent dispatched on a non-allowlisted gate-ID could append its own gate-ID to the allowlist mid-execution, satisfying M4 by self-promotion. WITH orchestrator-only edit, allowlist additions can only originate from the orchestrator at plan-freeze time (or from explicit user instruction).

**Cardinality** (post-S88 close): ~62 rows across S86–S88. S88 contributes the bulk (~50 rows) covering registry landings, rule-file extensions, K-counter advancements, and AMRI promotions.

**S88 W9-RULE-CLEANUP lift-out**: schema column count 4→3 (rationale column lifted to `methodology-wave-instances.md`). Allowlist size 42928→10872 chars (74.7% reduction; well under 40K harness threshold). The 40 per-row rationale prose entries lifted verbatim to NEW registry file (39089 chars).

---

### Section VIII — AMRI cleanup history

**Source**: `agent-standards.md §"Agent-Memory Registry Inversion (AMRI)"` (3-test protocol).

**AMRI tests** (any one fires AMRI):
1. **Input-pin test** — another gate lists the memory file as Input-SHA pin in its PRDR machinery block.
2. **Output-target test** — a gate's method section writes to `.claude/agent-memory/*/MEMORY.md` or `project_*.md` as primary registry-maintenance output.
3. **Cross-agent overlap test** — two or more agents' memories contain overlapping entries for the same observable, mechanism, or detector.

**Scope of "memory files"**: BOTH per-agent `.claude/agent-memory/<agent-type>/*.md` AND orchestrator project memory `~/.claude/projects/<project-slug>/memory/*.md`. The user's clarification (2026-04-28): "you HAVE to follow AMRI [for orchestrator memory]; not [following] fully breaks the traceability."

**Calibration corpus** (≥3 AMRI promotions documented):

| # | Source | Target | Session | Notes |
|:-:|:-------|:-------|:--------|:------|
| 1 | `sessions/session-plan/session-87-plan-w13.md` lines 664-668 (5 agent-memory pin rows: connes-ncg, spectral-geometer, transit-dynamics, volovik, gen-physicist) | removed from INPUT-PIN MAP table; project-level RQ ownership at §W13-1.5 retained | S87 W0 (2026-04-28) | Test 1 fired on each of 5 rows; per-agent role assignment was redundant bookkeeping. |
| 2 | mack-cosmic-bridge `reference_key-constraints.md` (Planck/DESI/BICEP-Keck observational anchors + framework prediction snapshots S58–S66) | `sessions/framework/registry/mack-observational-constraints.md` | S87 W0 (2026-04-28) | Test 1 fired multiple times (`session-85-plan-w4.md:357`, `session-86-plan-w15.md:240`, `session-87-plan-w9a.md:848`, `archive/session-68-context.md:158`); cross-agent overlap test ALSO fired with `falsifier-master-inventory.md`, `branch-iv-canonical.md`, `pre-registered-observations.md`. AMRI-promoted with provenance header + cross-link table. |
| 3 | rule-file bloat (cross-pillar-bridge-anatomy.md + epistemic-discipline.md crossed 40K harness perf threshold via per-wave instance landings) | `sessions/framework/registry/cross-pillar-bridge-corpus.md` (6-section corpus) + `sessions/framework/registry/pru-class-corpus.md` (4-section + extensions corpus) | S88 W9-RULE-CLEANUP (2026-05-06) | Cross-pillar 49672→29241 chars (41% reduction); epistemic 43709→31153 chars (29% reduction). Rule statements + base calibration retained in parents; per-instance corpora + K-counter logs + axiomatic skeletons lifted with bidirectional cross-link. |
| 4 | `methodology-wave-allowlist.md` 40 rows of multi-paragraph rationale prose (structurally identical to a session log) | `sessions/framework/registry/methodology-wave-instances.md` | S88 W9-ALLOWLIST-LIFT-OUT (2026-05-06) | Allowlist size 42928→10872 chars (74.7% reduction). Schema column count 4→3. Companion to W9-RULE-CLEANUP precedent. |

**Detection tool**: `computations/_shared/_agent_memory_inversion_audit.py`. **Migration tool**: `/shortterm <agent>` with AMRI-PROMOTE classification.

**What must NOT live in agent memory**: watchlists / detector rosters / observational-prediction tables; cross-session machinery-parameter registries; canonical constant values (those live in `canonical_constants.py`); gate-verdict tables / session-wide tallies; anything referenced by another agent's spawn prompt as authoritative data.

---

### Section IX — Workshop methodology (Investigating-Workshops 4-condition definition + 3-question discriminator)

**Source**: `Investigating-Workshops.md` (S82+; user correction 2026-05-02).

**4-condition workshop definition** (ALL FOUR must hold):
1. TWO+ agents with COMPETING perspectives on a SPECIFIC TENSION (not parallel-agreement)
2. Genuine LEDGER-DISSONANCE (competing-claim adjudication on a number, sign, structural reading, methodology choice, or convention pin)
3. Multi-round structure (R1 steelman / R2 respond to opponent's best case / R3 converge on verdict)
4. Output: STRUCTURAL VERDICT (NEW pinned position — verdict, registry entry, rule diff, pre-registered gate — NOT a queued computation)

**What is NOT a workshop**: solo compute follow-ups; verification gates (Stage-2 cross-check, plan-freeze audit); re-listings of WP-enumerated carry-forwards; single-agent "synthesis"; methodology-rule extension proposals where both agents would agree; registry-state classification choices / hygiene-promotion items / framework-housekeeping; parallel-compute-wave structures dressed as N-agent panels.

**3-question discriminator** (apply BEFORE adding any candidate to workshop schedule; first YES wins):
- **Q1 — Math/physics adjudication?** Does the candidate's resolution require deciding between TWO+ competing readings of a substrate-physics observable / structural identity / convention with first-principles arguments on both sides? If YES → workshop.
- **Q2 — Registry-state classification, hygiene, gate finalization, or framework-issue?** If YES → compute carry-forward to the WP (route to `/rclab-plan` via WP CF blocks, NOT workshop schedule).
- **Q3 — Parallel-compute-wave structure?** N prerequisite conditions, each on a different axis, each with own pre-registered PASS criterion AND verdicts combine via logical AND? If YES → compute carry-forward to the WP, marked "wave-together".

**Calibration corpus (failures)**:
- **S87 batch-1 dispatch (2026-05-02)** — 8 investigators each produced 5-7 "candidates" mostly labeled as "workshops"; on user audit, all 8 seeds contained solo compute follow-ups dressed as 2-agent workshops, verification gates as "workshops", re-listings of wave-synthesis carry-forward queues, narrative inflation around already-WP-known content. User correction: "And these agents are NOT identifying 'workshops', they're just listing carry-forward equations and bloviating."
- **S88 W13 (2026-05-07)** — initial workshop schedule had 4 workshops; user audit removed 2: W-2 §VII.K-META (registry-hygiene, not math; routed as compute carry-forward CF-W13-5) and W-4 PATH-B STEP-0 (parallel-compute-wave dressed as 4-agent workshop; routed as compute carry-forward CF-W13-6 with 4 parallel pre-registered S89 axis-gates + 1 wave-AND closeout). After removals, schedule retained 2 genuine workshops.

**"No workshops" is a valid output**: a session with clean PASSes, unambiguous verdicts, no cross-wave conflicts, settled methodology produces ZERO workshops. Honest count: typical session produces 0–4 genuine workshops.

---

### Section X — Mechanical-closure discipline + Layer-separability carve-out

**Source**: `mechanical-closure-discipline.md` (S86 W3 origin; S88 W8-89 carve-out).

**5-clause acceptability for mechanical closure** (orchestrator-authored verdict-line emission for upstream-blocked gates):
1. Upstream-block topology is the cause (every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, AND plan's downstream decision-point table specifies the documented outcome)
2. Verdict honesty (emitted verdicts are FAIL or PRE-REG-INC, NEVER PASS)
3. Per-gate-distinct audit_sha256 (pinmap embeds per-gate identity keys so SHAs are pairwise distinct)
4. Audit-trail signature (descriptive `value` string names blocking prereq + status; future audit can grep + verify)
5. Working-paper update is in-script (the closure script MUST update WP §Status/Verdict/Results/Substrate-framing IN THE SAME RUN as the verdict-line append)

**Layer-separability carve-out** (S88 W8-89; SUGGESTION at K=1 → MANDATORY at K=3):
- **L1 — Layer-functor cleanness**: substrate-physics observable admits F decomposition; Type-F vs Type-S partition aligns with substrate ↔ methodology layer pair under F.
- **L2 — Type-F closed-form**: Type-F sub-observable admits closed-form algebraic identity (canonical: single-summand-projection trace `Tr_{M_n(C)}(P · A)` with P minimal central projection on `A_K = C ⊕ H ⊕ M_3(C)`); evaluable bit-precision in single-pass pure function.
- **L3 — Type-S separation**: Type-S structurally separated per algebra-axis orthogonality 4-corner classification; mechanical closure on Type-F does NOT pre-determine Type-S verdict.
- **L4 — Honesty disclosure**: verdict-line `convention=` field MUST encode the carve-out tag `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F`; WP section MUST include explicit Type-F / Type-S separation paragraph.

**Stage-2 cross-reviewer PASS-AND requirement**: Axis A (spectral / NCG-axiomatic) connes-ncg-theorist + Axis B (substrate / superfluid-universe) volovik-superfluid-universe-theorist; both operate WITHOUT prior workshop context.

**PLANNING DEFECT trigger**: covered_count ≥ 4. Wave plan was OVER-OPTIMISTIC about prerequisite landings. Class-8 PRU vulnerability at plan-authorship time.

---

### Section XI — Substrate-first canonical-sourcing

**Source**: `substrate-first-canonical-sourcing.md` (S86 W1a-S3).

**Operates at canonical-sourcing axis** (complementary to `phononic-framing.md`'s explanation-direction axis): pins must source from substrate's first-principles computation, not external-paper provenance treated as authoritative.

**External-paper provenance is METHODOLOGICAL** (correct usage) when conceptual framing references / cross-check anchors / heritage citations / notational source for definitions. **External-paper provenance is CANONICAL** (FORBIDDEN — must reroute) when providing the NUMERICAL VALUE of a pin without substrate-first computation having been performed.

**4-step audit pattern** (`_substrate_first_provenance_audit.py` proposed at S87 carry-forward V.1):
1. External-paper heading glob (if absent: `ABSENT-EXTERNAL-HEADING` AUDIT-FAIL; recommend rerouting to substrate source)
2. Placeholder pattern detection (`O(10^?-?\d+)`, `≈ ...`, `~ 10^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`)
3. Schematic library helper detection (verify CLASS pin field FULL vs SCHEMATIC; verdict-line `convention=` carries `-SCHEMATIC` suffix)
4. Substrate-first computation citation → AUDIT-PASS

**SCHEMATIC vs full physical level pin rule** (MANDATORY at K=4 promotion, S88 W7b-83 close, 2026-05-05):
- CLASS pin field with FULL or SCHEMATIC
- Verdict line encodes class in `convention=` field (e.g., `convention=substrate-distance-1-SCHEMATIC`)
- Synthesis section MUST include explicit cross-class disclosure paragraph

**Class-(f) PIN-PLACEHOLDER calibration corpus** (K=4 MANDATORY): W4-2 (S86; NEGATIVE-CALIBRATION baseline; reclassified Class-(d)) + W9b-2 (S87; NEGATIVE-CALIBRATION; reclassified Class-(d)) + W9c-1 (S87; POSITIVE-CALIBRATION canonical model with `convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC` + `tier_pin=TIER-2` companion row) + W5b-2 sub-test (c) (S86 substrate; CALIBRATION-LOCUS-EXEMPT inheritance locus).

**Audit pipeline composition order** (S87+):
```
PRU (cardinality pre-flight) → SOURCE-RECON (value pre-flight) →
SUBSTRATE-FIRST-PROVENANCE (source-existence) → PRDR (machinery enumeration) →
gate execution → v3-recovery audit
```

**Calibration corpus precedents (3 witnesses)**:
- W0c-3 §(b) (vdd §VI absent in 14 papers; rerouted to S83 W2-G24 Cartan-flat R|_{Cartan⁴} = 0)
- W4-2 line 503 (SCHEMATIC `_spectral_action_regulators.py` helpers vs full Connes-Chamseddine 1996 §2.2-2.3 physical multipliers)
- W5a-2 §10 (placeholder `xi_E_GGE_inv ≈ O(10⁻²)` vs canonical `xi_E_GGE_inv = 13.642473425595973` from W4 P4 commit; D_max = 3.13 OOM hits HARD-HALT band)

---

### Section XII — Registry-landing conventions

**Source**: `registry-landing.md` (S86 W-3 RULE-1 + S88 W3c-30 + S88 W8-92).

**SOURCE-DOUBLE-CITE-CO-PRIMARY** (sequential V_input + C_output chains; NOT PRIMARY+CONFIRMATION which assumes parallel independence).

**Schema**:
```
§VII.{slot} {THEOREM-NAME}
  ANCHOR-1 (input layer, V): {citation}
  ANCHOR-2 (output layer, C): {citation}
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V → A_F → C → conclusion
  Closure SHA pin: {64-char workshop verdict SHA}
```

**4-condition detection**:
1. Sequential — Anchor-2 cannot be invoked WITHOUT first invoking Anchor-1
2. Non-fungible — anchors cannot be swapped or reordered
3. Both anchors must remain accessible (neither can be deprecated)
4. Both anchors must be on the same algebra-axis cell (S88 W-15 V.6) per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. Cross-corner co-primary FORBIDDEN.

**Bridge-Landing Script Architecture (single-shot pattern)** (S88 W3c-30): write_promotion → fsync → re-read → verify → emit (exactly one verdict line). FORBIDDEN: BEFORE pattern (write → re-read → verify → conditionally re-write/append (FAIL/INFO emit) → re-read → re-verify → emit corrective PASS) — produces dual-trio verdict-line groups (calibration: S87 W5 4-of-5 dual-trio FAIL/INFO → PASS).

**Operator-Projection Reading-A Naming Hygiene** (MANDATORY at K=3, S88 W8-92 close, 2026-05-05):
- Suffix tag `§VII.X.OP-PROJ` (algebra-side: central-projection traces, quotient-functor cyclic-fold V_4 modulo, bridge-anatomy K-count discipline) vs `§VII.X.STATE-PROJ` (state-side: state-pair functionals, Connes distances, occupation distributions)
- Bare `§VII.X` FORBIDDEN when both readings admissible
- Audit detection regex (positive): `^### §VII\.[A-Z]+(\.[A-Z0-9-]+)*\.(OP-PROJ|STATE-PROJ)\b`
- K=3 corpus: S87 W4-2 §VII.AJ.W4-1 + S87 W6-1 §VII.AG.1 + S87 W11-meta-2

**Calibration corpus (origin)**: S86 W-3 R3 Convergence #2 (Path-H/Path-C multi-valued classification (a)). V1 (3He-B BDI 0D inheritance arrow) + C1 (Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality of A_F = C ⊕ H ⊕ M_3(C)). Volovik's R2-A V1-PRIMARY framing was REVOKED at R3-A; SOURCE-DOUBLE-CITE-CO-PRIMARY adopted.

---

### Section XIII — Verifier-rubric pre-registration (Class 8.2)

**Source**: `epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"`. K=5 MANDATORY at S88 W-7/W-21/W-22 simultaneous advancement (2026-05-08).

**4 required elements when a gate's PASS criterion involves rubric-grading of qualitative content**:
1. **Pattern set**: enumerate specific lexical / structural patterns the verifier accepts (e.g., for substrate-first: `D_K`, `spectral moment`, `Mellin-cone`, `spectral residue`, `Seeley-DeWitt`, `Heitsch cocycle`)
2. **Disjunction-vs-conjunction declaration**: ALL patterns required (conjunction) or ANY (disjunction) per content unit
3. **Negative-marker set** (optional): patterns that auto-fail (e.g., `"in curved spacetime"` without explicit substrate-correction marker)
4. **Pre-registered calibration corpus**: 1+ exemplar passing-content snippet pinned by SHA so rubric can be re-validated

Without (1)–(4), execution-time iteration to calibrate the rubric is structurally indistinguishable from iterate-until-PASS (Class 6 PROHIBITED_ACTIONS) — even when underlying content is unchanged across runs.

**Cross-Proxy Adjudication extension** (T1-19, S86 W-9): when a cross-review gate is dispatched to challenge a prior INFO/FAIL via alternative proxy, additionally pre-register proxy operationalization with rubric pinning + open-verdict framing (NO Class-6-adjacent "iterate-until-PASS" framing in spawn prompt) + document proxy's algebraic relationship to prior (ALGEBRAICALLY DISTINCT or ALGEBRAICALLY EQUIVALENT but semantically distinct).

**K=5 calibration corpus**: Instance #1 W-12 "Z_4 or similar" admitted V_4; Instance #2 W-8 R3 / W2-11 stratum-vs-Cartan-toral V_4; Instance #3 S88 W-7 W2-2 V.5 D-W8-1 underdetermination; Instance #4 S88 W-22 W7a-74 V.3 numerical-metric-class (`spread ≤ 0.06` admitted both `full_atlas` and `f2_only_class` definitions); Instance #5 S88 W-21 W6b-56 V.6 boundary-direction sub-check (asymptotic-limit phrasing admitted FALSE claim).

---

### Section XIV — Publication-precision pre-registration (Class 8.3)

**Source**: `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"`. K=4 MANDATORY at S87 W8 close (2026-04-30).

**5 required elements when a gate's output VALUE will be cited downstream**:
1. **Publication precision pin**: state number of significant figures (e.g., `n_s_published_sig_figs = 15` for full float64)
2. **Verifier tolerance match**: downstream verifier MUST set rel_tol ≥ 10^(−publication_sig_figs); tighter rel_tol structurally guarantees FAIL on precision-floor mismatch
3. **Round-trip cross-check**: producing gate emits full float64 to .npz AND rounded to WP; downstream verifier loads from .npz (full precision), not WP
4. **Canonical-metric pin** (cluster-span family): refactor's threshold formula MUST express the same metric the canonical reports (e.g., cluster-span gates use `|ratio − 2|` canonical, NOT `|b2 − 2·b3|/|b2|` factor-2-different)
5. **Algebraic-equivalence audit at plan-authorship**: when spawn prompt cites a canonical-anchor value, plan-authoring orchestrator MUST verify the spawn-prompt's threshold formula is the same function of underlying quantities

**K=4 calibration corpus**: W1c-8 `n_s` (S86; 10-sig-fig vs 15-sig-fig); W2-4 cluster-span (S86; `|ratio − 2|` vs normalized factor-2 mismatch); W8-2 `max_pair_ratio_A_5` (S87; 6-sig-fig vs 14-sig-fig; FAIL composite); W8-8 `gv_canonical_difference` (S87; 14-sig-fig plan-pinned vs full float64; INFO composite); W13-3 R_842 stale-rectangle relabel (S86 Class-(c) PIN-DRIFT-FROM-STALE-SOURCE).

---

### Section XV — Forward methodology debts

**K-counter advancements pending (advisory until K=3)**:
- PRU Class 8.4 (representation-convention-pin): K=1, advisory
- PRU Class 8.5 (joint-hypersurface-pre-registration-form): K=1, advisory
- PRU Class 8.6 (layered-substitution-chain-audit): K=1, advisory
- Hybrid Independence Test (cross-pillar bridge K-counter): K=1, SUGGESTION
- Substrate-input-orthogonality clause (Stage-2 PASS-AND): K=1, SUGGESTION
- Closing-Paragraph-Coherence Audit Pattern (EG1): K=1, SUGGESTION
- F(observable) vs F(trigger predicate) split: K=1, advisory
- Forward-pinned-follow-up wave class (Corpus B): K=1, SUGGESTION
- Layer-separability carve-out (mechanical-closure): K=1, SUGGESTION
- Definitional-datum-vs-derived-theorem K-counter: K=2, advisory
- Single-τ-slice vs moduli-deformation substrate-IS levels: K=2, advisory
- Element 1 fiducial-anchor binding discipline: K=1, advisory
- Per-Bulletin-per-pole Level-1 wall classification: K=2-3 mixed, partial MANDATORY

**Audit-script extension queue**:
- `_substrate_first_provenance_audit.py` (S87 carry-forward V.1; not yet implemented)
- `_joint_theorem_independent_verify_audit.py` extensions (S89-STAGE-2-AXIS-B-DOWNSTREAM-INHERITANCE-AUDIT; substrate-input-orthogonality predicate; cross-reviewer-machinery-self-authorship audit)
- `_registry_landing_audit.py` Class-(g) flags: `OP-VS-STATE-PROJECTION-NAMING-DRIFT`; `S89-CROSS-CORNER-CO-PRIMARY-AUDIT`
- `_machinery_feasibility_audit.py` boundary-direction substitution-chain sub-check
- `_source_reconciliation_audit.py` Class-(g) flags: `JOINT-HYPERSURFACE-1D-SCALAR-DEGENERATE`; `SPEARMAN-SPREAD-METRIC-UNDECLARED`
- `_cross_pillar_bridge_audit.py` extension for Hybrid Independence Test PER-CLAUSE verdict tagging
- `S89-CROSS-PILLAR-BRIDGE-AUDIT-LEVEL2-SUB-CLASS-CHECK`

**Open methodology questions**:
- Functional-selection methodology (which spectral functional uniquely determines the framework's predictions?) — atlas-08 cross-link
- Layer-functor F audit-leg verification (`S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`)
- M_meta promotion criterion (track future multi-deliverable workshops for adoption of (Scope, Layer) projection; promote at K=3)
- Prompt-encoded-vs-memorized validation (`S87-MCP-DISCIPLINE-INVERSION-VALIDATION` PASS at orchestrator MCP fabrication rate < 5%)

---

## Section 2-NEW-RULES — 24 framework rule files enumerated (target ≥14 EXCEEDED)

| # | Rule file path | Origin session | Role |
|:-:|:---------------|:--------------|:-----|
| 1 | `.claude/rules/joint-theorem-promotion.md` | S86 W-9 | 4-stage candidate→registered→cross-axis-verified→permanent pathway; constructive complement to "agreement among agents" exclusion. Includes Axis-B Selection Protocol + substrate-input-orthogonality clause + cross-reviewer-machinery-self-authorship requirement. |
| 2 | `.claude/rules/cross-pillar-bridge-anatomy.md` | S86 W-5 | MANDATORY 5-anatomy + 3-level ladder for cross-pillar registry entries; Level-2 layer distinction (binding vs non-binding); Element 1 fiducial-anchor binding; Element 2 OE-form discipline; Hybrid Independence Test K-counter; Algebra-axis orthogonality K-counter (MANDATORY at K=3); Per-Bulletin-per-pole Level-1 wall classification. |
| 3 | `.claude/rules/mechanical-closure-discipline.md` | S86 W3 | Orchestrator-authored verdict-line emission discipline for upstream-blocked gates (5-clause acceptability); Layer-separability carve-out (S88 W8-89; SUGGESTION at K=1); PLANNING DEFECT trigger at covered_count ≥ 4. |
| 4 | `.claude/rules/regulator-pin-discipline.md` | S86 W0c-7 | a_n^{regulator} tagging mandatory for NEW citations of Seeley-DeWitt coefficients; Sage-Exact Rationals for Ω_GW Regulator-Class Values extension; Class-(c) PIN-DRIFT-FROM-STALE-SOURCE W-11 calibration corpus extension. |
| 5 | `.claude/rules/regulator-convention-lockdown.md` | S86 W12-4 | Mellin-Barnes / Schur-Zubarev convention freeze (CAC) for DR3-class L_max-stability gates; demarcation theorem (admissibility class via effacement-preservation criterion at L=10). |
| 6 | `.claude/rules/substrate-first-canonical-sourcing.md` | S86 W1a-S3 | Substrate-IS canonical > external-paper provenance; 4-step audit pattern; SCHEMATIC vs full physical level pin (MANDATORY at K=4); Surrogate-vs-Canonical at Cohomology-Class Layer (K=1 advisory); Class-(f) PIN-PLACEHOLDER taxonomy. |
| 7 | `.claude/rules/methodology-wave-allowlist.md` | S86 W-13 | Append-only allowlist of METHODOLOGY-class gate-IDs; orchestrator-only edit by harness convention (closes recursion attack); 3-column schema (post-S88 W9-RULE-CLEANUP lift-out); ~62 rows S86–S88. |
| 8 | `.claude/rules/wave-classification.md` | S86 W-13 | M1–M4 strict-conjunction test for METHODOLOGY-class; NROY clause (cannot be both COMPUTE and METHODOLOGY); MIXED-class sub-decomposition; Forward-pinned-follow-up wave class (K=1 SUGGESTION). |
| 9 | `.claude/rules/Investigating-Workshops.md` | S82+ (user correction 2026-05-02) | 4-condition workshop definition + 3-question discriminator (Q1 math/physics adjudication → workshop; Q2 hygiene → WP CF; Q3 parallel-compute-wave → WP CF wave-together); calibration corpus (S87 batch-1 8-investigator failure; S88 W13 2-removal). |
| 10 | `.claude/rules/inheritance-falsifier-protocol.md` | S86 W-5 RULE-3 | Rank-2 ker(ι_*) protocol with 4 gates (kernel-signature decisive + cohomology-asymmetry ratio + kernel-signature supporting + slope-discrimination); (Δ_B/Δ_A)^p cancellation theorem. |
| 11 | `.claude/rules/registry-landing.md` | S86 W-3 RULE-1 | SOURCE-DOUBLE-CITE-CO-PRIMARY (sequential V+C chains); Bridge-Landing Script Architecture (single-shot pattern, S88 W3c-30); Operator-Projection Reading-A Naming Hygiene (OP-PROJ vs STATE-PROJ; MANDATORY at K=3, S88 W8-92). |
| 12 | `.claude/rules/phononic-framing.md` | S86 W-5 RULE-2 | IS-not-IN convention (substrate IS observable, not IN container); LCDM-vs-substrate vocabulary table; Single-τ-slice vs moduli-deformation substrate-IS levels (S88 W-2 W2-10; K=2 advisory). |
| 13 | `.claude/rules/epistemic-discipline.md` | S82+ (extended; v3 union landing S86 W0a-1) | Layer-Decomposition (F functor); Phi correspondence; PRU Class 8.0–8.6 sub-class taxonomy; Source Reconciliation Class-(a)–(f) taxonomy; Verifier-rubric pre-registration (Class 8.2); Publication-precision pre-registration (Class 8.3); Pole-Scope sub-clause (MANDATORY at K=4, S88 W7a-72); Resolution-Specificity Scoping sub-clause; Closing-Paragraph-Coherence Audit Pattern (EG1). |
| 14 | `.claude/rules/evoi-prioritization.md` | S82+ | Framework probability methodology; EVOI = P(pass)·\|delta_P(pass)\| + P(fail)·\|delta_P(fail)\|; effort-based probability tracking. |
| 15 | `.claude/rules/agent-standards.md` | S82+ (HIGH-DENSITY WORKSHOP TEMPLATE T2-5 from S86 W-12) | Universal agent standards (formal rigor, persistent memory); AMRI 3-test detection; HIGH-DENSITY WORKSHOP TEMPLATE (multi-layer output-slot decomposition). |
| 16 | `.claude/rules/output-standards.md` | S82+ (T1-13/T1-14 from S86 W-3) | 7-component action items format; 7-section handoff document; Workshop Wrap-Up "What Changed" numerical-vs-structural distinction; Carry-Forward Dependency Enumeration. |
| 17 | `.claude/rules/teammate-behavior.md` | S82+ | Inbox-first; 3-files-before-inbox-recheck cap; one-writer-per-output; deduplicate-notifications-against-completed-work; shutdown protocol (only user can initiate). |
| 18 | `.claude/rules/session-handoffs.md` | S82+ | Session naming (`session-NN/`); mandatory handoff per Output Standards 7-section format; chronological integrity (never renumber); recommendation carry-forward (next session's plan is ONLY carry-forward mechanism). |
| 19 | `.claude/rules/computation-environment.md` | S82+ | Hardware + Python specs (`phonon-exflation-sim/.venv312/Scripts/python.exe`; AMD RX 9070 XT; CPU thread-cap pattern); referenced by `math-scripts.md`. |
| 20 | `.claude/rules/knowledge-index-usage.md` | S82+ | MCP knowledge query discipline; canonical pattern (search_knowledge before computing; get_constant for value+provenance; trace_entity for evidence chain). |
| 21 | `.claude/rules/math-scripts.md` | S82+ (extended S87 W11) | Canonical constants discipline (every S34+ script imports from canonical_constants.py); local variable tagging `# (local)`; double-check logic before compute (substitution chain mandatory for sign/direction/threshold claims); D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check (S87 W11 calibration); machinery-feasibility audit (root-count heuristic severity-1 flag); canonical write-order for new framework predictions; mnemonic-vs-exact ratio discipline. |
| 22 | `.claude/rules/mcp-servers.md` | S82+ | MCP server inventory (knowledge, sage, paper-search, mathscinet, oeis, zbmath, astro, madrigal); query patterns + reinforcement guidance. |
| 23 | `.claude/rules/gate-verdicts.md` | S82+ (Option A landed S88 W8-100) | Verdict-line schema (canonical line + dual-SHA companion comment row); Option A `supersedes=<old_audit_sha>` tag protocol under absolute verdict permanence; canonical `append_verdict()` helper. |
| 24 | `.claude/rules/v3-closure-recovery.md` | S82+ (S78 origin) | Stage 1 automatic re-dispatch (max 2 iterations per signal); Stage 2 V3-NON-COMPLIANT fallback; Stage 3 user-intervention trigger; PROHIBITED_ACTIONS Class 1–4 (convention-shopping, iterate-until-PASS, post-hoc pre-registration editing, ansatz-forced PASS); bounded-iteration termination proof. |

**Total: 24 rule files** (target ≥14 — SUBSTANTIALLY EXCEEDED).

---

## Section 2-TEMPLATES — 9 framework templates enumerated (target ≥6 EXCEEDED)

| # | Template path | Role |
|:-:|:--------------|:-----|
| 1 | `.claude/templates/pru-pre-registration-template.md` | Canonical PRDR scaffold + 8-item R3 YAML gate-block + cutoff_axis YAML pin + PRDR keyword 8-K-atom enumeration + 5-class file-pin (SHA) taxonomy. Cited by `epistemic-discipline.md §"Pre-Registration Completeness"`. |
| 2 | `.claude/templates/iteration-audit.md` | Standardized decision rule + tag vocabulary (8 tags: integrator-config / convention-pin-fix / convention-pin-ADDITION / regime-diagnostic-addition / quantity-definition-drift / unclear / iterate-until-PASS / verdict-class-transition) + severity grading (HIGH / MEDIUM / LOW) + WARRANT classes + remediation format. Eliminates PRU at audit-workshop level by construction. |
| 3 | `.claude/templates/synthesis.md` | Synthesis report template (I. Session Outcome / II. Key Results / III. Gate Verdicts / IV. Structural Implications / V. Carry-Forward Computations [MANDATORY 4-field specs]). Per `feedback_fix-in-session-never-defer.md`. |
| 4 | `.claude/templates/workshop.md` | Workshop document template (build FULL skeleton before launching agents; *[NOT STARTED]* placeholders filled by agents during execution). Multi-round structure (R1 / R2 / R3) per `Investigating-Workshops.md`. |
| 5 | `.claude/templates/workshop-schedule.md` | Workshop / Synthesis Schedule template (campaign of slash-command invocations across `/rclab-review` solos + `/rclab-workshop` workshops). Skill-slot mapping load-bearing invariant. Produced by `/rclab-investigate`. |
| 6 | `.claude/templates/workingpaper.md` | Working paper template (the answer log; runtime agent writes its gate's completed entry). Canonical shell shape at `examples/workingpaper-shell-example.md` (frozen). |
| 7 | `.claude/templates/agent-roster.md` | Canonical name-to-type mapping (Name Prefix → subagent_type → Short Name); resolves SendMessage routing. |
| 8 | `.claude/templates/plan-compute.md` | Compute plan template (Session Objective with pre-registered master gate; Wave Structure with dependency graph; per-wave gate blocks). |
| 9 | `.claude/templates/mellin-balance-pre-declaration.md` | Mellin-Balance Pre-Declaration template (S84 W6-71 origin); MANDATORY for all S84+ cluster-test gates; prevents recurrence of S83 G15/G28/G34 ad-hoc cluster-membership failures by forcing pre-registration of Mellin-moment balance BEFORE any scan is run. |

**Plus**: `.claude/templates/examples/workingpaper-shell-example.md` (frozen 10-gate dispatch shell, does not get filled in by runtime).

**Total: 9 templates + 1 frozen example** (target ≥6 — EXCEEDED).

---

## Section 2-AMRI — AMRI cleanup instances enumerated (target ≥3 EXCEEDED)

See Section VIII for the full table. Summary: ≥4 AMRI promotions documented:

1. **S87 W0 plan-w13.md AMRI fix** (2026-04-28): 5 agent-memory pin rows removed from INPUT-PIN MAP table; project-level RQ ownership at §W13-1.5 retained as canonical project-level discharge.
2. **S87 W0 mack-observational-constraints AMRI promotion** (2026-04-28): mack-cosmic-bridge `reference_key-constraints.md` → `sessions/framework/registry/mack-observational-constraints.md`; cross-link table to canonical sister registries (`falsifier-master-inventory.md`, `branch-iv-canonical.md`, `pre-registered-observations.md`); pointer line installed in `reference_key-constraints.md`.
3. **S88 W9-RULE-CLEANUP** (2026-05-06): rule-file bloat in `cross-pillar-bridge-anatomy.md` + `epistemic-discipline.md` lifted to `cross-pillar-bridge-corpus.md` (6-section corpus) + `pru-class-corpus.md` (4-section + extensions corpus); rule-file size reduction 41% + 29%.
4. **S88 W9-ALLOWLIST-LIFT-OUT** (2026-05-06): `methodology-wave-allowlist.md` 40 rationale-prose rows lifted to `methodology-wave-instances.md`; schema column count 4→3; allowlist size reduction 74.7%.

---

## Section 3 — Cross-atlas dependencies

### Atlas-09 (retractions)

AMRI cleanups documented in Section VIII are SUPERSESSIONS — agent memory entries that were promoted to project-level registry/correspondence files and SUPERSEDED at the original location. Cross-link: each AMRI instance's source path appears in atlas-09 as "supersession" entry with target = atlas-12 §VIII row.

**Recommended atlas-09 cross-link entries**:
- mack-cosmic-bridge `reference_key-constraints.md` SUPERSEDED → atlas-12 §VIII row 2
- session-87-plan-w13.md INPUT-PIN MAP rows 664-668 SUPERSEDED → atlas-12 §VIII row 1
- cross-pillar-bridge-anatomy.md per-instance corpora SUPERSEDED → atlas-12 §VIII row 3
- methodology-wave-allowlist.md rationale-prose column SUPERSEDED → atlas-12 §VIII row 4

### Atlas-11 (cross-pillar-bridge-corpus)

**Division of labor** (atlas-11 vs atlas-12):
- **Atlas-11** (substrate-side): cross-pillar bridge ENTRIES — substrate-IS observables with their 5-anatomy + 3-level ladder content. ~24 entries (W-5, W4a-17, W11-5, FWD-C1/C2/C3 candidates, etc.). The CONTENT.
- **Atlas-12** (methodology-side): the RULES that govern atlas-11's anatomy. The DISCIPLINE that produces atlas-11. Specifically: `cross-pillar-bridge-anatomy.md` (rule); `joint-theorem-promotion.md` (4-stage pathway for STAGE-1-CANDIDATE → STAGE-3-PERMANENT); `inheritance-falsifier-protocol.md` (rank-2 ker(ι_*) discipline); `registry-landing.md` (SOURCE-DOUBLE-CITE-CO-PRIMARY, OP-PROJ vs STATE-PROJ).

**Overlap point**: cross-pillar-bridge-anatomy.md rule itself appears in BOTH atlases (as content in atlas-11, as discipline in atlas-12). **Recommended division**: atlas-11 quotes the 5-anatomy + 3-level ladder as the schema atlas-11 entries follow; atlas-12 owns the full rule-file content and audit pipeline (Hybrid Independence Test K-counter; Element 2 OE-form discipline; Per-Bulletin-per-pole Level-1 wall classification; algebra-axis orthogonality K-counter MANDATORY at K=3). Atlas-11 cites atlas-12 §II for the rule's structural backbone.

### Atlas-04 (assumptions)

The methodology floor includes assumed-and-proven items (process axioms): (a) plan-freeze-time pre-registration is binding; (b) verdict permanence (Option A protocol); (c) PROHIBITED_ACTIONS Class 1–4; (d) orchestrator-only edit on rule files (closes recursion attack); (e) AMRI 3-test detection (per-agent + orchestrator memory same path-shape); (f) M1–M4 strict conjunction for METHODOLOGY-class waves; (g) MAX_ITERATIONS_PER_SIGNAL = 2 for v3-closure-recovery Stage 1.

**Recommended atlas-04 cross-link**: atlas-04 includes a "Process Axioms" sub-section that cites atlas-12 §IV (PRU taxonomy) + §V (joint-theorem 4-stage) + §VI (M1–M4) + §VII (orchestrator-only edit).

### Atlas-08 (open questions)

Methodology open questions belong in atlas-08:
- Functional-selection methodology (which spectral functional uniquely determines framework predictions?)
- Layer-functor F audit-leg verification (`S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`)
- M_meta promotion criterion (track future multi-deliverable workshops; promote at K=3)
- Prompt-encoded-vs-memorized validation (`S87-MCP-DISCIPLINE-INVERSION-VALIDATION` PASS at fabrication rate < 5%)
- All K=1 SUGGESTION items pending K=3 MANDATORY (8.4/8.5/8.6/Hybrid Independence/substrate-input-orthogonality/closing-paragraph-coherence/F-trigger-split/Forward-pinned-follow-up/Layer-separability)

**Recommended atlas-08 cross-link**: atlas-08 §"Methodology open questions" cites atlas-12 §XV.

### `.claude/rules/*` and `.claude/templates/*`

Atlas-12 is the curated index OF the rule-file corpus; the rule files themselves are the canonical source. Every atlas-12 reference cites `.claude/rules/<name>.md:line_number` or `.claude/templates/<name>.md`.

**Recommended cross-link**: atlas-00 (index) gains a `### Methodology Floor Atlas Series` row pointing to atlas-12 with the discipline cluster `{rules, templates, registries-side AMRI, audit-pipeline}`.

---

## Citation Discipline (verification)

**Every rule file cited above is verified to exist** (24/24 confirmed via `Glob ".claude/rules/*.md"`):
session-handoffs / evoi-prioritization / teammate-behavior / inheritance-falsifier-protocol / agent-standards / computation-environment / output-standards / knowledge-index-usage / math-scripts / regulator-convention-lockdown / mcp-servers / gate-verdicts / v3-closure-recovery / Investigating-Workshops / phononic-framing / regulator-pin-discipline / cross-pillar-bridge-anatomy / registry-landing / wave-classification / mechanical-closure-discipline / joint-theorem-promotion / methodology-wave-allowlist / epistemic-discipline / substrate-first-canonical-sourcing.

**Every template cited above is verified to exist** (9/9 confirmed via `Glob ".claude/templates/*.md"`):
iteration-audit / synthesis / workshop / mellin-balance-pre-declaration / plan-compute / workingpaper / pru-pre-registration-template / workshop-schedule / agent-roster.

**Anchor-line citations verified**:
- `epistemic-discipline.md §"Layer-Decomposition"`: line 321
- `epistemic-discipline.md §"Phi correspondence"`: line 349
- `agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE"`: line 84

---

## Substrate-Framing Discipline Compliance

This packet treats methodology rules as PROCESS, not physics:
- Section II frames F as a Morita-equivalence-preserving FUNCTOR between layers (categorical, not physical)
- Section III frames Phi as a graded-ring isomorphism between weight axes (algebraic, not physical)
- Section IV–XIV frames each rule as a discipline that GOVERNS HOW the substrate is investigated, never as substrate physics itself
- Section XII (registry landing) explicitly cross-links to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause to enforce that atlas-11 (substrate) and atlas-12 (methodology) are STRUCTURALLY ORTHOGONAL — cross-corner co-primary FORBIDDEN
- No emojis, no filler

---

## REPORT FORMAT BACK

### (1) Packet path

`C:\sandbox\Ainulindale Exflation\sessions\archive\session-88\atlas-uplift-materials\atlas-12-methodology-floor-materials.md`

### (2) Counts

- **Rule files enumerated**: 24 (target ≥14 — SUBSTANTIALLY EXCEEDED)
- **Templates enumerated**: 9 + 1 frozen example (target ≥6 — EXCEEDED)
- **AMRI cleanup instances**: 4 documented (target ≥3 — EXCEEDED)

### (3) Rules whose role overlapped multiple atlas-12 sections

Three rules span multiple atlas-12 sections and are cited from each section that consumes them:

- **`cross-pillar-bridge-anatomy.md`**: appears in §IV (PRU sub-class taxonomy via Class-(c) PIN-DRIFT-FROM-STALE-SOURCE W-11 corpus extension cross-link), §V (joint-theorem 4-stage pathway via STAGE-1-CANDIDATE → STAGE-3-PERMANENT for cross-pillar entries), §XII (registry-landing OP-PROJ vs STATE-PROJ cross-link to algebra-axis orthogonality MANDATORY clause), and is the central cross-link between atlas-11 (substrate) and atlas-12 (methodology). This is an EXPECTED overlap because cross-pillar bridge content sits at the substrate-methodology interface.

- **`epistemic-discipline.md`**: appears in §II (Layer-Decomposition F functor), §III (Phi correspondence), §IV (PRU Class 8.0–8.6 taxonomy), §XI (Source Reconciliation Class-(a)–(f) taxonomy), §XIII (Verifier-rubric pre-registration Class 8.2), §XIV (Publication-precision Class 8.3). This is the central rule-file backbone of atlas-12; cross-section overlap is structural, not redundant.

- **`registry-landing.md`**: appears in §XII (SOURCE-DOUBLE-CITE-CO-PRIMARY + OP-PROJ vs STATE-PROJ + Bridge-Landing Script Architecture). Single section, but the rule itself touches three structurally distinct disciplines (anchor citation, registry-naming hygiene, script architecture). Cited as one section but reader should know it spans three sub-disciplines.

### (4) Atlas-11 vs atlas-12 overlap on bridge-anatomy discipline

**FLAG**: `cross-pillar-bridge-anatomy.md` overlaps both atlases. **RECOMMENDED DIVISION**:

- **Atlas-11** (substrate-side; ~24 entries): owns the bridge ENTRIES (substrate-IS observables with their 5-anatomy + 3-level ladder content per entry). Atlas-11 quotes the 5-anatomy + 3-level ladder as the SCHEMA each entry follows. References atlas-12 §II for the rule's structural backbone.
- **Atlas-12** (methodology-side): owns the full rule-file content and audit pipeline (Hybrid Independence Test K-counter; Element 2 OE-form discipline; Per-Bulletin-per-pole Level-1 wall classification; algebra-axis orthogonality K-counter MANDATORY at K=3; Level-2 layer distinction binding vs non-binding; Element 1 fiducial-anchor binding clause). Atlas-12 owns the rule itself; atlas-11 owns its instances.

This division mirrors atlas-07 (permanent-results) vs atlas-04 (assumptions): atlas-07 enumerates instances, atlas-04 enumerates the underlying axioms.

### (5) Section IX split flag

**FLAG**: Section IX (workshop methodology) covers (a) 4-condition definition, (b) 3-question discriminator, (c) workshop-schedule format. **RECOMMENDED**: KEEP AS SINGLE SECTION IX. Rationale:

- The 3-question discriminator EXPLAINS the boundary of the 4-condition definition (it operationalizes "is this a workshop?" via Q1 → workshop, Q2 → WP CF, Q3 → wave-together). Splitting them would over-fragment the definition's structural argument.
- The workshop-schedule format (campaign of `/rclab-review` + `/rclab-workshop` slots) is operationally distinct but tightly coupled to the 4-condition definition — the schedule format ENFORCES the definition by construction (Slot 2 is `/rclab-workshop` with EXACTLY 2 agents per entry).
- Atlas-12 readers benefit from seeing all three (definition + discriminator + schedule format) together as one workshop discipline cluster.

If split is preferred for length reasons, the natural split is IX-a (4-condition definition + 3-question discriminator combined; the discriminator EXPLAINS the definition) + IX-b (workshop-schedule format; operationally distinct). Three-way split (IX-a + IX-b + IX-c) is over-fragmented and not recommended.
