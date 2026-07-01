# Registry-Landing Conventions

Governs how registry entries in `sessions/permanent-results-registry.md` cite their derivational anchors.

Calibration corpora, K-counter advancement records, dated promotion events, per-instance narratives, and worked-example traces live at `sessions/framework/registry/pru-class-corpus.md` (and the corresponding rule-specific corpus sections; see the pointer table at the end). This file carries directives only.

## SOURCE-DOUBLE-CITE-CO-PRIMARY

When a registry entry's derivation is a **sequential V_input + C_output chain** — the input layer V supplies a premise; the output layer C supplies a structural theorem CONDITIONAL on that input — the registry entry MUST cite both anchors at **co-primary** weight. Neither anchor alone fixes the conclusion; together they fix it uniquely.

### Schema

```
§VII.{slot} {THEOREM-NAME}
  ANCHOR-1 (input layer, V): {citation}
  ANCHOR-2 (output layer, C): {citation}
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V → A_F → C → conclusion
  Closure SHA pin: {64-char workshop verdict SHA}
```

Both anchors are tagged at equal weight; neither is decoration. Removing either layer breaks the derivation.

### When PRIMARY+CONFIRMATION is wrong

PRIMARY+CONFIRMATION implies the two anchors INDEPENDENTLY reproduce the same conclusion via parallel routes. SOURCE-DOUBLE-CITE-CO-PRIMARY implies sequential dependence. For sequential V+C chains, PRIMARY+CONFIRMATION is structurally incorrect.

If two anchors independently reproduce the same conclusion via DIFFERENT routes (parallel, not sequential), use PRIMARY + INDEPENDENT-CROSS-CHECK instead.

### Detection

Apply SOURCE-DOUBLE-CITE-CO-PRIMARY when ALL of the following hold:

1. The derivation is **sequential** — Anchor-2 cannot be invoked without first invoking Anchor-1.
2. The two anchors are **non-fungible** — they cannot be swapped or reordered without breaking the chain.
3. **Both anchors must remain accessible** — neither can be deprecated without invalidating the conclusion.
4. **Both anchors must be on the same algebra-axis cell** per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. Cross-corner co-primary structures (one anchor on the algebra-INVARIANT spectrum-only-functional cell, the other on the algebra-DEPENDENT state-pair-functional cell) are STRUCTURALLY FORBIDDEN — the two cells live on orthogonal algebra-axes and cannot enter a single non-fungible chain. Forward enforcement: `_registry_landing_audit.py` flags cross-corner SOURCE-DOUBLE-CITE-CO-PRIMARY structures at plan-freeze with HARD-HALT remediation.

### Audit at plan-freeze

Plan-freeze validators reading registry entries with two anchors MUST check that the structure tag (CO-PRIMARY vs CONFIRMATION vs INDEPENDENT-CROSS-CHECK) matches the actual derivational dependency. Mis-tagged anchors are a registry-hygiene defect; fix in-session.

Calibration corpus: `pru-class-corpus.md §"Registry-landing SOURCE-DOUBLE-CITE-CO-PRIMARY"` (corpus entry pending).

## Bridge-Landing Script Architecture (single-shot pattern)

Bridge-landing scripts (those that write a registry entry into `sessions/permanent-results-registry.md` AND emit a verdict line in the same run) MUST follow the **single-shot** emission pattern:

```
build_promotion_text → write_atomic_with_fsync → re_read + verify_section_matches → emit (exactly one verdict line)
```

The promotion text is FULLY built in memory before any disk write; the post-fsync re-read is the FINAL verification step; the verify step's outcome determines the verdict; the emission is exactly one canonical line + one dual-SHA companion row + (if `[SIGN]` trigger) one 3-tuple companion row per `gate-verdicts.md` schema-v2. Reusable template: `computations/_bridge_landing_script_template.py`.

### Forbidden BEFORE pattern

```
write → re-read → verify → conditionally re-write/append (FAIL/INFO emit) → re-read → re-verify → emit corrective PASS
```

Pollutes the verdict file with a 2-trio (4-line) verdict-line group per gate. Cross-link to `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6 ("iterate-until-PASS") adjacency: the conditional rewrite is permitted ONLY when the underlying content is unchanged across runs; the AFTER pattern eliminates the adjacency by construction.

### Detection at plan-freeze

A producing script for a registry-landing gate is **BEFORE-pattern** (FORBIDDEN) iff it contains BOTH of:

1. A verdict-line emission call BEFORE a `re_read + verify` pair has determined the canonical PASS/FAIL outcome.
2. A conditional rewrite branch that triggers on a FAIL/INFO outcome of an intermediate verify and emits a SECOND verdict line for the corrective state.

A producing script is **AFTER-pattern** (REQUIRED) iff it contains:

1. A pure-function `build_promotion_text(...)` step producing the FULL text in memory.
2. A `write_atomic_with_fsync(...)` step writing the text to disk.
3. A `re_read + verify_section_matches(actual, expected)` step yielding a single boolean.
4. Exactly ONE `emit_verdict_line(...)` call whose verdict is the boolean from step 3.

If verify FAILs in the AFTER pattern, the script emits FAIL once and the gate honestly closes per `mechanical-closure-discipline.md` (no corrective rewrite permitted in-script; remediation escalates to next-session plan).

### Audit at plan-freeze

Plan-freeze validators dispatching a registry-landing gate MUST verify the producing script has:

1. A pure `build_promotion_text` step (no I/O before write).
2. A single `write_atomic_with_fsync` (no per-attempt rewrites).
3. A single `verify_section_matches` returning a boolean (no nested conditional retries).
4. Exactly one `emit_verdict_line` call whose verdict argument is that boolean.

Script failing any of (1)-(4) is BEFORE-pattern → plan-freeze halt with remediation request (refactor against `computations/_bridge_landing_script_template.py`).

Calibration corpus: `computations/_bridge_landing_audit_trail_observation_S87_W5.md`.

## Operator-Projection Reading-A Naming Hygiene

**Status**: MANDATORY at K=3.

The Reading-A operator-projection vs state-projection distinction is a STRUCTURAL distinction at the algebra-axis orthogonality layer (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3). Operator-projection observables (algebra-side: central-projection traces on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, quotient-functor cyclic-fold V_4 modulo, bridge-anatomy K-count discipline) and state-projection observables (state-side: state-pair functionals on `A`, Connes distances, occupation distributions) are STRUCTURALLY ORTHOGONAL in identity-class membership.

### Naming convention (MANDATORY)

When a §VII.X theorem admits BOTH operator-projection and state-projection readings, the registry slot identifier MUST suffix-tag the projection side:

- Operator-side projection (algebra-INVARIANT family; spectrum-only functionals; algebra-side central-projection traces): `§VII.X.OP-PROJ`
- State-side projection (algebra-DEPENDENT family; state-pair functionals; state-side occupation/coherence observables): `§VII.X.STATE-PROJ`

Bare `§VII.X` (without suffix tag) is FORBIDDEN when both readings are admissible.

### Enforcement

Audit `computations/_shared/_registry_landing_audit.py` Class-(g) `OP-VS-STATE-PROJECTION-NAMING-DRIFT` flag. Detection pattern (regex over `sessions/permanent-results-registry.md`):

```
positive-match (admissible):  ^### §VII\.[A-Z]+(\.[A-Z0-9-]+)*\.(OP-PROJ|STATE-PROJ)\b
negative-match (FORBIDDEN):   ^### §VII\.[A-Z]+\b(?!.*(?:OP-PROJ|STATE-PROJ))   # only when both readings admissible
```

Legacy entries with ambiguous projection-side readings are GRANDFATHERED with mandatory retrofit at next-session plan-freeze (`mack-cosmic-bridge` sole writer per `feedback_mack-bridge-role.md`).

### Cross-link to algebra-axis orthogonality

This rule is the registry-naming-layer specialization of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause. The orthogonality clause prevents conflation in the theorem statement; this rule prevents conflation in the registry-slot identifier.

### Forward-looking enforcement

- **Plan-freeze halt**: any registry-landing gate citing a §VII.X slot WITHOUT projection-side suffix tagging (when both readings are admissible per the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`) triggers plan-halt with MANDATORY remediation per `_source_reconciliation_audit.py` Class-(c) extension.
- **Cross-corner co-primary FORBIDDEN**: per the algebra-axis orthogonality MANDATORY clause, OP-PROJ and STATE-PROJ entries CANNOT be co-primary anchors of the same theorem; structural-orthogonal-companion is the correct anchor structure when both projection-side readings are independently registry-eligible.

Calibration corpus (K=3): `pru-class-corpus.md §"Reading-A naming hygiene"` (corpus entry pending).

## Parse-Tree Expansion Pre-Registration for new §VII entries

**Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. Until promotion, new §VII registry entries SHOULD declare the parse-tree expansion; post-promotion, missing declarations route to plan-freeze HARD-HALT.

Hardens the parse-tree expansion declaration discipline at the registry-landing layer. Pairs with `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` (the bridge-anatomy-layer parent).

### (1) Rule

Any NEW §VII registry entry citing an observable whose symbolic form contains a state-history label MUST declare the parse-tree expansion alongside the symbolic form.

**Parse-tree expansion** = step-by-step reduction from history-label → closed-form expression on the substrate algebra `(A_K, H_K, D_K)`, citing the applicable closed-form theorems (e.g., Bogoliubov closed forms per the BdG canonical amplitudes; Wedderburn decomposition; Mellin-Barnes residue identities per §VII.U.1).

The expansion serves two structural purposes:

1. **Disambiguation** — makes the substrate-IS algebra-axis classification (Corner I/II/III/IV per §VII.U.2 4-corner partition) decidable from the registry text alone, without consulting the producing script or session workshop.
2. **Audit traceability** — pins the state-historic-label-to-substrate-closed-form bridge map in the registry-permanent layer.

### (2) State-history label pattern set

Authoritative downstream-enforcement source: `_registry_landing_audit.py` `STATE_HISTORY_LABEL_PATTERNS` (currently 11 patterns; extend per rule changelog). Pattern set includes: `n_a^GGE`, `n_a_GGE`, `state.GGE`, `Bogoliubov(`, `GGE-state`, `α_s_canonical`, `α_s_route_[0-9]+`, `Bogoliubov-(state|amplitude|coefficient)`, `Δ_M\b`, `\bDelta_M\b`.

### (3) Enforcement (`_registry_landing_audit.py` Class-(h))

Detector: `detect_class_h_missing_parse_tree_expansion`. Logic:

1. Scan §VII entry block for any `STATE_HISTORY_LABEL_PATTERNS` match.
2. No match → diagnostic `no_state_history_label_present` (rule does not apply).
3. Match found → scan for `PARSE_TREE_EXPANSION_MARKERS` (formal block markers `Parse-tree expansion:|parse_tree_expansion:|## Parse-tree|### Parse-tree` OR inline `parse-tree (decision|level|reduction|expansion)` references OR bare `parse-tree` mention).
4. Marker found → diagnostic PASS.
5. No marker → diagnostic `MISSING-PARSE-TREE-EXPANSION` at S2 advisory severity (escalates to S1 HARD-HALT on K=3 MANDATORY promotion); halts plan-freeze.

### Cross-link

Registry-landing-layer enforcement of the `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` sub-clause. Three layers, same structural distinction, non-redundant operational coverage: the algebra-axis orthogonality K=3 MANDATORY clause prevents conflation in the theorem statement; the bridge-anatomy sub-clause prevents conflation in the substrate-IS observable specification; this rule prevents conflation in the registry-text layer.

### Forward-looking enforcement

- **Plan-freeze halt**: a registry-landing gate emitting a §VII entry citing a state-historic label WITHOUT a parse-tree expansion declaration triggers plan-freeze halt at S2 advisory severity (SUGGESTION status); on K=3 MANDATORY promotion, severity escalates to S1 HARD-HALT.
- **Legacy entries grandfathered** with mandatory retrofit at next-session plan-freeze (`mack-cosmic-bridge` sole writer per `feedback_mack-bridge-role.md`).

Calibration corpus + canonical worked example (Var_a Corner II retroactive expansion at `permanent-results-registry.md §VII.U.2` Corner II row): `pru-class-corpus.md §17`.

## Class-(i) INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT

**Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3.

A Level-3 registry row stating band-edge numbers AND a containment claim those same numbers falsify (a "1σ band [L_b, U_b] ... both edges inside ... conjunct [L_c, U_c]" pattern where `L_b < L_c` or `U_b > U_c`) is internally inconsistent and fires `INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT` at S2 advisory (HARD-HALT on K=3 promotion), halting plan-freeze. Detector: `computations/_shared/_registry_landing_audit.py::detect_class_i_internally_inconsistent_level_3_band` (`LEVEL_3_BAND_CONTAINMENT_PATTERNS` + numeric sub-check on the two bracketed float pairs). Catches self-contradictory Level-3 rows at plan-freeze, not only at Stage-2 cross-review; parallels Class-(h) MISSING-PARSE-TREE-EXPANSION. Criterion-side home: `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"` Level-3 annotation discipline. Full directive + K=1 calibration corpus: `sessions/framework/registry/cross-pillar-bridge-corpus.md §20`.

## Calibration corpus + K-counter status (pointers)

| Rule sub-section | Corpus location | Current status |
|:-----------------|:----------------|:---------------|
| SOURCE-DOUBLE-CITE-CO-PRIMARY | `pru-class-corpus.md` (entry pending) | Forward-looking |
| Bridge-Landing single-shot architecture | `computations/_bridge_landing_audit_trail_observation_S87_W5.md` | Forward-looking |
| Operator-Projection Reading-A naming hygiene | `pru-class-corpus.md` (entry pending) | MANDATORY at K=3 |
| Parse-Tree Expansion Pre-Registration | `pru-class-corpus.md §17` (shares corpus with bridge-anatomy parent) | SUGGESTION at K=1 |
| Class-(i) Internally-inconsistent Level-3 band-statement | `cross-pillar-bridge-corpus.md §20` | SUGGESTION at K=1 |
