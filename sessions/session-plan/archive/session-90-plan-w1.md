# Session 90 Plan — Wave 1: Methodology rule-file extensions + audit-script enhancements

**Generated**: 2026-05-12
**Topic label**: S90 W1 carry-forward plan (session-90)
**Skill**: `/rclab-plan session-90`
**Mode**: fanout per-wave plan files
**Wave**: W1 (Cluster A — Methodology rule-file extensions + audit-script enhancements)
**Total items**: 17
**Total effort estimate**: ~4.8 wave-equivalents (gen-physicist orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`)
**Classification**: METHODOLOGY (all 17 items satisfy M1∧M2∧M3∧M4 strict conjunction)

---

## Wave 1 Summary

Wave 1 (Cluster A) consolidates seventeen methodology-class deliverables that emerged from the S89 closeout-solo synthesis (gen-physicist §6) plus three reviewer-private extensions (connes V.3 + V.5, lizzi V.1, phonon-first V.4 + V.7). The unifying signal across all seventeen items: S89 surfaced a layer of audit-script + rule-file gaps that previously admitted silent class-conflations or hygiene drifts (W6-2 §VII.AN ROUTE-A-vs-ROUTE-B; W6-6 §VII.U.2 corner-IV three-axis fields absent; §W5-7 SCHEMATIC partial-positive locus distinct from W9c-1 full POSITIVE; deferred-pending intermediate verdict-class with no rule-file enforcement clause; §VII.AH Stage-3 substrate-input-orthogonality K=1→K=2 advancement; etc.). Each item lands as a rule-file diff (line-anchored) and/or audit-script extension (regex-anchored), plus a single-shot `s90_w1_<gate-slug>.py` self-test script where verifiable output is required, plus a methodology-wave-allowlist append + methodology-wave-instances rationale entry. No `value` field is a numerical scientific-comparison threshold; every gate's PASS predicate is artifact-existence-with-substantive-content per `wave-classification.md §M1`.

Within Cluster A, three intra-wave sequencing constraints are honored: (i) CF-14 PRECEDES CF-15 (deferred-pending rule-file enforcement-clause must land before TEMPLATE-INHERITED convention-tag retrofit cites the routing target); (ii) CF-2 PRECEDES CF-5 + CF-6 (corner audit dict extension must land before FI_RD_MIXED axis field + Parse-tree abbreviation map extensions reference it); (iii) cross-wave W2 CF-25 PRECEDES W1 CF-2 (§VII.U.2 Corner reconciliation Reading B lock-in must complete before audit-script extension reflects corrected Corner-II baseline) — this is a cross-wave handoff documented in the Decision-Point Prerequisites section. All other Cluster A items are dispatch-independent and may execute in parallel under the orchestrator-direct-write protocol.

Substrate-framing reminder. Every dispatch prompt in this wave carries the IS-not-IN direction-of-explanation cross-link per `phononic-framing.md §"IS Space, Not IN Space"`: rule-file diffs and audit-script extensions enforce the structural distinctions that already exist at the substrate layer (substrate-IS observables on `(A_K, H_K, D_K)`; emergent observables on laboratory bridges via HKR / Connes-Karoubi pairings; layer-functor `F : substrate → methodology → audit` preserves PRU class invariants). The methodology floor is the F-image of substrate structure; this wave hardens the F-image at the methodology and audit layers.

---

## Wave 1 Decision Point Prerequisites

### Cross-wave inbound (must clear before W1 dispatches)

- **W2 CF-25 PRECEDES W1 CF-2** (§W1-2 below): §VII.U.2 Corner reconciliation Reading B lock-in (W2's `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN` mack registry-text landing) must complete before W1 CF-2 (`S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION`) reflects the corrected Corner-II baseline. If W2 CF-25 lands FAIL or INFO, W1 CF-2 routes to deferred-pending or extracts the pre-W2-25 baseline as fallback. PASS-thru required.
- **W2 CF-42 PRECEDES W1 CF-12** (§W1-12 below): The §W2-1.A two-gate-split PASS reference is cited as part of the calibration corpus for PRU Class 8.7 Degenerate-Observable Pre-Flight Check (the §W1-1 FAIL would have been flagged at plan-freeze had Class 8.7 been MANDATORY). CF-42 PASS is a hardener but not a strict blocker — CF-12 may land with §W1-1 as the K=1 corpus instance even if §W2-1.A reroutes to a different path.

### Intra-wave constraints

- **CF-14 PRECEDES CF-15** (§W1-14 → §W1-15): deferred-pending rule-file enforcement-clause must define the routing target before the TEMPLATE-INHERITED convention-tag retrofit cites the rule. CF-15 dispatches AFTER CF-14 lands PASS.
- **CF-2 PRECEDES CF-5 + CF-6** (§W1-2 → §W1-5 + §W1-6): corner audit dict extension must land before FI_RD_MIXED axis field + Parse-tree abbreviation map extensions reference the TARGET_SLOTS_S89 dict structure. CF-5 and CF-6 dispatch in parallel AFTER CF-2 PASS.

### Cross-wave outbound (W1 outputs feeding later W-N)

- **CF-12 → W4 §VII.AQ Stage-2 plan-block**: PRU Class 8.7 Degenerate-Observable Pre-Flight Check, once landed in `epistemic-discipline.md §"Pre-Registration Completeness"`, is the audit pattern W4 §VII.AQ Stage-2 plan-block will be screened against at plan-freeze. PASS-thru required for W4 §VII.AQ Stage-2 to inherit Class 8.7 enforcement.
- **CF-14 → W6 CF-63** (deferred-pending mack landing): Deferred-pending state must exist as a valid registry verdict before mack writes §VII.AV + §VII.AU initial deferred-pending registrations in W6 CF-63. PASS-thru required.
- **CF-17 → W6 CF-W4-7-VII-AH-STAGE-3-PROMOTION** (W2 CF-20): K=1→K=2 advancement updates the joint-theorem-promotion.md K-counter so the Stage-3 PERMANENT promotion gate (W2 CF-20) cites K=2 in its provenance.

---

## §W1-1. CF-1 — `S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION`

1. **Gate ID**: `S90-VII-AN-AUDIT-SCRIPT-REGISTRY-ANCHOR-RECONCILIATION-EXTENSION`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write (no CO-AUTHOR; paired with mack registry-text write in W2 CF-23 — this gate is the audit-script side ONLY)
5. **Hypothesis**: Extending `_registry_landing_audit.py` with a new Class-(g) diagnostic `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` detects the W5a-44 NEGATIVE-CALIBRATION pattern (registry anchor cites Route-A while underlying producing-script implements Route-B) by static-string comparison between the §VII slot's "Source" / "Anchor" field and the cited script's docstring header.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Extend `computations/_shared/_registry_landing_audit.py` to add a NEW Class-(g) diagnostic `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION`. Read first:
   > - `computations/_shared/_registry_landing_audit.py` at input-pin SHA `<runtime>` (current head of file)
   > - `sessions/permanent-results-registry.md §VII.AN` block (input-pin SHA `<runtime>`)
   > - `.claude/rules/substrate-first-canonical-sourcing.md §(i)` K=4 NEGATIVE-CALIBRATION corpus
   > - S89 W6-2 audit `9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f`
   >
   > Methodology: the new Class-(g) audit takes a §VII slot's registered "Anchor" / "Source" / "Producing script" field as authoritative; greps the cited producing-script path for its docstring; static-string compares the registry's claimed derivation route (Route-A | Route-B | Route-C label) against the script's docstring header line containing `# Route: <X>` or `# Derivation: <X>`. Mismatch fires Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` at SEVERITY=S2 (advisory) or S1 (MANDATORY) per the SOURCE-RECONCILIATION 4-band calibration in `epistemic-discipline.md §"Source Reconciliation"`. For §VII.AN specifically: registry's V-anchor cite reads "S82 W3-9 single-pole Mellin closure" (Route-A); cited closure script `s82_w3_9_as_adjacent_obs.py` does NOT exist on disk (per W6-2 audit). When script-not-found AND registry claims a specific route, fires Class-(g) with diagnostic substring `script_not_found_AND_route_claimed`.
   >
   > Output files:
   > - `computations/_shared/_registry_landing_audit.py` (extended) — content_sha256 captured at write-time
   > - `computations/_shared/s90_w1_vii_an_audit_script_extension_test.py` (self-test driver; runs the new Class-(g) diagnostic against §VII.AN and emits PASS/INFO)
   > - Verdict line appended to `computations/session-90/s90_gate_verdicts.txt` per `gate-verdicts.md §"Canonical Verdict-File Path"`
   >
   > Substrate framing: Class-(g) audit operates at the F-image methodology layer per `epistemic-discipline.md §"Layer-Decomposition"` F : substrate → methodology → audit. The Route-A-vs-Route-B class-conflation is the methodology-layer image of the substrate-IS Mellin-cone substrate-distance-pole structure; registry-anchor must commute with the substrate's own derivation route. Container thinking ("the registry IS a separate ledger from the substrate-physics computation") is the failure mode; the substrate is logically prior — the registry is the F-image of the substrate's own computation.

7. **Machinery pin (PRDR)**:
   - `_registry_landing_audit.py` head SHA: `<pinned at dispatch>`
   - `permanent-results-registry.md §VII.AN` block SHA: `<pinned at dispatch>`
   - `_substrate_first_provenance_audit.py` (referenced for Class-(g) severity band) SHA: `<pinned at dispatch>`
   - W6-2 audit SHA: `9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f`
   - Audit severity band pin: S2 (advisory) when route_claimed=True AND script_not_found=False; S1 (MANDATORY) when route_claimed=True AND script_not_found=True
   - Detection regex pin: `^#\s*(Route|Derivation):\s*(.+)$` over script docstring
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=audit-script-extension-landed-AND-flags-§VII.AN, scheme=registry-anchor-class-g-extension, convention=route-a-vs-route-b-detection-static-string-compare, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) `_registry_landing_audit.py` patch lands (lines added between existing Class-(f) handler and end-of-class taxonomy block); (ii) self-test script runs and emits Class-(g) diagnostic flag on §VII.AN; (iii) audit-script extension lines ≥ 30 (substantive content per `wave-classification.md §M1`); (iv) `methodology-wave-allowlist.md` row appended with computed `sha256_of_plan_block`; (v) `methodology-wave-instances.md` rationale entry appended.
   - **FAIL** iff any of (i)-(v) absent.
   - **INFO** iff §VII.AN flag fires but reduces to false-positive on inspection (W6-2 audit pin remains canonical reference).

10. **Substitution chain** (for `[AUDIT]` trigger — class-(g) classification routing):

    - Step 1 (Definition): `Route_registry := text in §VII slot Source/Anchor field`; `Route_script := docstring header line matching ^#\s*(Route|Derivation):\s*(.+)$`.
    - Step 2 (Substitution): For §VII.AN, `Route_registry = "S82 W3-9 single-pole Mellin closure" (Route-A claim)`; `Route_script = <undefined>` (script `s82_w3_9_as_adjacent_obs.py` not found on disk per W6-2 audit).
    - Step 3 (Simplify): `script_not_found_AND_route_claimed = True AND True = True` → fires Class-(g) at S1 severity.
    - Step 4 (Direction): Class-(g) S1 routes to MANDATORY remediation; remediation owner = mack registry-text writer per `feedback_mack-bridge-role.md` (handled in W2 CF-23 paired write).
    - Conclusion: §VII.AN flagged Class-(g) ROUTE-A-vs-ROUTE-B-CONFLATION; mack reconciles registry-text in W2 CF-23.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the registry-anchor-route static-string conflation pathway by construction at the audit layer; future §VII landings cannot silently drift between Route-A claim and Route-B implementation without firing Class-(g). Constraint surface gains a wall at the registry-script commutation axis.
    - **FAIL** indicates the audit-script extension is structurally incomplete; W2 CF-23 mack reconciliation still proceeds but without the audit-script enforcement floor.

12. **Effort estimate**: 0.3 we (gen-physicist orchestrator-direct-write).

13. **Substrate-framing reminder**: The new Class-(g) audit is the methodology-layer F-image of substrate-IS commutativity (registry must commute with the producing-script's derivation route). Do NOT frame this as "registry IS a separate container holding script-derived data"; the registry IS the F-image of the substrate's own computation under `F : substrate → methodology → audit`.

---

## §W1-2. CF-2 — `S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION`

1. **Gate ID**: `S90-CORNER-CLASSIFICATION-AUDIT-VII-U-2-EXTENSION` (CF-W6-4 = CF-R1-1)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Extending `_corner_classification_audit.py` TARGET_SLOTS dict to include §VII.U.2 + 4 instance-row sub-targets (Corner I §VII.U.1; Corner II Var_a; Corner III Connes-distance; Corner IV α_s_route_3) populates `per_slot_results['§VII.U.2']` with parse-tree counters = 0 AND a 3-axis classification for Var_a `corner='II'`, `algebra_axis='INVARIANT'`, `mellin_pole='s=4'`.
6. **Method**:

   **PREREQUISITE**: W2 CF-25 `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN` must land PASS before dispatch.

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Extend `computations/_shared/_corner_classification_audit.py` TARGET_SLOTS_S89 dict to include §VII.U.2 + 4 instance-row sub-targets. Read first:
   > - `computations/_shared/_corner_classification_audit.py` head SHA (W6-6 baseline `2b96bf78<full-sha-at-dispatch>`)
   > - `sessions/permanent-results-registry.md §VII.U.2` block lines 12927-13058 (input-pin SHA `<pinned at dispatch>`)
   > - W2 CF-25 verdict line in `computations/session-90/s90_gate_verdicts.txt` for Reading B lock-in PASS confirmation
   > - Parse-tree decision at clause (e) line 12995 of `permanent-results-registry.md`
   >
   > Methodology: extend TARGET_SLOTS_S89 dict so each row carries the structural identification of its instance:
   > ```python
   > TARGET_SLOTS_S89 = {
   >   '§VII.U.2.Corner-I': {'observable': 'α_s_canonical', 'corner': 'I', 'algebra_axis': 'INVARIANT', 'mellin_pole': 's=3'},
   >   '§VII.U.2.Corner-II': {'observable': 'Var_a(n_a^GGE)', 'corner': 'II', 'algebra_axis': 'INVARIANT', 'mellin_pole': 's=4'},
   >   '§VII.U.2.Corner-III': {'observable': 'Connes-distance', 'corner': 'III', 'algebra_axis': 'DEPENDENT', 'mellin_pole': 's=3'},
   >   '§VII.U.2.Corner-IV': {'observable': 'α_s_route_3', 'corner': 'IV', 'algebra_axis': 'DEPENDENT', 'mellin_pole': 's=4'},
   > }
   > ```
   > For each Corner row, audit invokes (a) parse-tree counter check (counters MUST return 0 for properly registered observables); (b) algebra-axis classification check (matches the 4-corner Wedderburn decomposition per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3); (c) Mellin-pole substrate-distance check (Bulletin-class registry per S88 W10-119). Self-test runs the new audit on the post-W2-CF-25 §VII.U.2 block.
   >
   > Output files:
   > - `computations/_shared/_corner_classification_audit.py` (extended)
   > - `computations/_shared/s90_w1_corner_classification_audit_vii_u_2_test.py` (self-test)
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: the 4-corner Wedderburn decomposition IS the substrate's algebra-axis orthogonality structure (algebra-INVARIANT spectrum-only vs algebra-DEPENDENT state-pair functional families); the audit operates at the methodology F-image of this substrate-IS structure. Var_a(n_a^GGE) IS in Cell-II (INVARIANT, s=4) per the substrate's own three-machinery convergence (Wedderburn + clause-(e) parse-tree + F_traj=(k+1)/2); the audit verifies registry-text commutes with this substrate-IS classification.

7. **Machinery pin (PRDR)**:
   - `_corner_classification_audit.py` W6-6 baseline SHA: `2b96bf78<full-at-dispatch>`
   - `permanent-results-registry.md §VII.U.2` post-W2-CF-25 SHA: `<pinned at dispatch>`
   - W2 CF-25 verdict line: must be `PASS` per cross-wave prerequisite check
   - Parse-tree decision substrate at clause (e) line 12995: SHA `<pinned at dispatch>`
   - Expected counter values: `parse_tree_counter_corner_I = 0`, `parse_tree_counter_corner_II = 0`, `parse_tree_counter_corner_III = 0`, `parse_tree_counter_corner_IV = 0`
   - Expected classification dict for Var_a: `{'corner': 'II', 'algebra_axis': 'INVARIANT', 'mellin_pole': 's=4'}`
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=per_slot_results['§VII.U.2']-populated-with-4-corner-rows, scheme=corner-classification-audit-vii-u-2-extension, convention=wedderburn-4-corner-mandatory-k-3, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) TARGET_SLOTS_S89 dict extended with 4 §VII.U.2 sub-targets; (ii) `per_slot_results['§VII.U.2']` populated with all 4 Corner rows; (iii) all parse-tree counters return 0; (iv) Var_a 3-axis classification matches expected `{Corner II, INVARIANT, s=4}`; (v) allowlist + instances rows appended.
   - **FAIL** iff any of (i)-(v) absent OR parse-tree counter ≠ 0 OR Var_a classification mismatch.
   - **INFO** iff W2 CF-25 has not landed PASS at dispatch time (PRE-REG-INC blocked).

10. **Substitution chain** (N/A — `[AUDIT]` trigger; static-string dict extension + classification correctness check).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the §VII.U.2 4-corner registry-audit gap by construction; future Var_a-style observables at any §VII.U-extension slot get the 4-corner classification check at plan-freeze.
    - **FAIL** signals either dict extension incomplete or §VII.U.2 baseline incorrectly reading the three-machinery convergence (would force re-dispatch of W2 CF-25 + W2 CF-71 W-3 composite verify).

12. **Effort estimate**: 0.3 we.

13. **Substrate-framing reminder**: The 4-corner Wedderburn decomposition IS the substrate's algebra-axis orthogonality structure. Do NOT frame this as "Var_a IS in the algebra-INVARIANT cell because we decided to put it there"; the substrate's own Wedderburn block-diagonal structure (algebra-INVARIANT spectrum-only functional family vs algebra-DEPENDENT state-pair functional family) IS the classification — Var_a's structural form (spectrum-only Bogoliubov closed-form) PLACES it in Corner II by construction.

---

## §W1-3. CF-3 — `S90-PLAN-STALENESS-REGEX-TIGHTENING-AND-CROSS-WAVE-ANCHOR-MIS-CITATION-DETECTION`

1. **Gate ID**: `S90-PLAN-STALENESS-REGEX-TIGHTENING-AND-CROSS-WAVE-ANCHOR-MIS-CITATION-DETECTION` (CF-W6-6 + W-3 CF-R1-2)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Tightening `_plan_staleness_audit.py` `pre_supersession_pin` regex to require YAML pin-map context (not arbitrary prose) AND extending it with cross-wave-anchor mis-citation detection (registry says A.30 → §VII.AS but plan cites A.30 → §VII.AR) eliminates the W6-WP:224 false-positive and adds a new structural class.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Extend `computations/_shared/_plan_staleness_audit.py` along two axes. Read first:
   > - `computations/_shared/_plan_staleness_audit.py` head SHA `5f370299<full-at-dispatch>` (W6-6 baseline)
   > - `sessions/archive/session-89/session-89-plan-w6.md:224` (instance of the false-positive)
   > - `sessions/permanent-results-registry.md` line 16971 (§VII.AR with A.36 anchor) AND line 17000 (§VII.AS with A.30 anchor)
   >
   > Axis 1 (regex tightening): replace the existing `pre_supersession_pin` regex `r'(?i)\b(pre[_-]supersession|stale)\b'` with `r'(?im)^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*(?:["\']?)(?:pre[_-]supersession|stale)\b'` to require the pattern to appear in YAML pin-map context (key-value form) rather than prose. Calibration target: re-run on `sessions/archive/session-89/session-89-plan-w6.md:224` returns no hit (false-positive eliminated).
   >
   > Axis 2 (cross-wave-anchor mis-citation extension): add new detector class `CROSS_WAVE_ANCHOR_DRIFT`. Read `sessions/permanent-results-registry.md` for canonical anchor-section mappings (e.g., A.30 → §VII.AS at line 17000; A.36 → §VII.AR at line 16971). Build canonical_anchor_to_section_map dict at audit-time via regex grep on registry text. Then for every plan-block citing the form `A\.\d+\s*→\s*§VII\.\w+`, verify the section in the plan matches the canonical map; mismatch fires `CROSS_WAVE_ANCHOR_DRIFT` at S2 (advisory). Calibration target: W6-WP:224 cross-wave-anchor-drift IS flagged when plan cites A.30 → §VII.AR (which is the false-positive's structural form).
   >
   > Output files:
   > - `computations/_shared/_plan_staleness_audit.py` (extended)
   > - `computations/_shared/s90_w1_plan_staleness_extension_test.py` (self-test against W6-WP:224)
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: the cross-wave-anchor drift detection is the methodology-layer F-image of substrate-IS naming-conventions; the substrate's anchor-section mapping (A-numbers to §VII slot letters) IS a substrate-stable correspondence; plan-block drift from this correspondence violates the F-image commutativity.

7. **Machinery pin (PRDR)**:
   - `_plan_staleness_audit.py` head SHA: `5f370299<full-at-dispatch>`
   - `permanent-results-registry.md` line 16971 (A.36 → §VII.AR) + line 17000 (A.30 → §VII.AS) SHA: `<pinned at dispatch>`
   - `sessions/archive/session-89/session-89-plan-w6.md:224` false-positive instance SHA: `<pinned at dispatch>`
   - Tightened regex pin: `r'(?im)^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*(?:["\']?)(?:pre[_-]supersession|stale)\b'`
   - Cross-wave-anchor-drift regex pin: `r'A\.\d+\s*→\s*§VII\.\w+'`
   - Expected fixtures-still-PASS check: pre-existing audit fixtures continue to PASS at PASS-band rel_dev ≤ 1e-9
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=regex-tightened-AND-cross-wave-anchor-extension-landed, scheme=plan-staleness-extension, convention=yaml-pin-map-context-strict + cross-wave-anchor-section-drift-detection, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) regex tightened to YAML-pin-map-context form; (ii) cross-wave-anchor-drift detector class added; (iii) re-run on W6-WP:224 flags cross-wave-anchor-drift (NOT false-positive); (iv) existing fixtures still PASS; (v) allowlist + instances rows appended.
   - **FAIL** iff regex mistuned (existing fixtures break) OR cross-wave-anchor-drift detector misses W6-WP:224 OR allowlist row missing.

10. **Substitution chain** (N/A — `[AUDIT]` regex-tightening + structural class addition).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the prose-form false-positive class AND adds cross-wave-anchor-drift as a new audit-detected structural class; future plans cannot silently drift across A-number-to-§VII-slot canonical mapping.
    - **FAIL** signals the regex tightening broke pre-existing fixtures (regression) OR the new detector class did not fire on its calibration target.

12. **Effort estimate**: 0.3 we.

13. **Substrate-framing reminder**: The A-number-to-§VII-slot mapping IS a substrate-IS naming-convention defined by the substrate's own canonical-anchor structure; plan-block drift is the methodology-layer F-image of a substrate-stable correspondence violation.

---

## §W1-4. CF-4 — `S90-EG1-K-COUNTER-REGEX-EXTENSION`

1. **Gate ID**: `S90-EG1-K-COUNTER-REGEX-EXTENSION` (CF-W6-7)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Extending `has_count_keyed_trigger` regex in `_w25_closing_paragraph_coherence_sweep_audit.py` to recognize the K-letter K-counter form `K\s*=\s*\d|K-counter|K_promotion` returns ≥1 of 3 rule-files (cross-pillar-bridge-anatomy.md, substrate-first-canonical-sourcing.md, registry-landing.md) with `has_count_keyed_trigger=True`.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Extend `computations/_shared/_w25_closing_paragraph_coherence_sweep_audit.py` regex. Read first:
   > - `computations/_shared/_w25_closing_paragraph_coherence_sweep_audit.py` head SHA `16c2729c<full-at-dispatch>`
   > - `.claude/rules/cross-pillar-bridge-anatomy.md` (K-counter usage instance)
   > - `.claude/rules/substrate-first-canonical-sourcing.md` (K-counter usage instance)
   > - `.claude/rules/registry-landing.md` (K-counter usage instance)
   >
   > Methodology: locate `has_count_keyed_trigger` regex; extend pattern set from existing `r'count[-_]keyed|threshold[-_]count'` to additionally match `r'K\s*=\s*\d|K-counter|K_promotion'` (K-letter K-counter form per `feedback_rules-compensate-missing-structure.md` K-counter convention). Run self-test against the 3 rule-files; expected result: ≥1 returns `has_count_keyed_trigger=True`.
   >
   > Output files:
   > - `computations/_shared/_w25_closing_paragraph_coherence_sweep_audit.py` (extended)
   > - `computations/_shared/s90_w1_eg1_k_counter_regex_test.py` (self-test)
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: K-counter advancement IS a methodology-layer F-image of substrate calibration-corpus accumulation; the regex captures the F-image trigger predicate per `epistemic-discipline.md §"Layer-Decomposition"` F(observable) vs F(trigger predicate) split.

7. **Machinery pin (PRDR)**:
   - `_w25_closing_paragraph_coherence_sweep_audit.py` head SHA: `16c2729c<full-at-dispatch>`
   - 3 rule-file targets SHA: `<pinned at dispatch>` each
   - Regex extension pin: `r'K\s*=\s*\d|K-counter|K_promotion'`
   - Expected output: ≥1 of 3 rule-files with `has_count_keyed_trigger=True`
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=k_counter_regex_extension_landed_AND_geq_1_of_3_rule_files_match, scheme=eg1-regex-extension, convention=k-letter-k-counter-form, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) regex extended; (ii) self-test returns ≥1 of 3 rule-files with `has_count_keyed_trigger=True`; (iii) allowlist + instances rows appended.
   - **FAIL** iff regex extension landed but 0 of 3 rule-files matches (regex still mistuned).

10. **Substitution chain** (N/A — `[AUDIT]` regex extension).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** unifies K-counter trigger detection across rule-files using both old `count-keyed` and new `K=N` forms.
    - **FAIL** indicates the K-letter form still slips past the regex; downstream EG1 closing-paragraph-coherence audit retains its incomplete coverage.

12. **Effort estimate**: 0.1 we.

13. **Substrate-framing reminder**: K-counter advancement IS the methodology-layer F-image of substrate calibration-corpus instance accumulation; the regex captures the trigger predicate per `epistemic-discipline.md §"Layer-Decomposition"` F(trigger predicate) image.

---

## §W1-5. CF-5 — `S90-FI-RD-MIXED-AXIS-FIELD-EXTENSION-CF-W6-4-DICT`

1. **Gate ID**: `S90-FI-RD-MIXED-AXIS-FIELD-EXTENSION-CF-W6-4-DICT` (CF-LZ-2)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write; **CO-AUTHOR**: lizzi-spectral-functional-theorist (trichotomy + F_traj dressing factors co-sign per Cluster A header)
5. **Hypothesis**: Extending TARGET_SLOTS_S89 dict at `_corner_classification_audit.py` with `fi_rd_mixed_axis` field per instance row (5 sub-fields incl. classification, F_traj dressing factors, level_dressed_candidacy) outputs full 5-axis classification + registry annotation amendment.
6. **Method**:

   **PREREQUISITE**: CF-2 (§W1-2 above) must land PASS before dispatch.

   Dispatch prompt (gen-physicist orchestrator-direct-write + lizzi CO-AUTHOR for trichotomy review):

   > Extend `computations/_shared/_corner_classification_audit.py` TARGET_SLOTS_S89 dict with new `fi_rd_mixed_axis` sub-field per instance row. Read first:
   > - `computations/_shared/_corner_classification_audit.py` post-CF-2 SHA `<pinned at dispatch>`
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"`
   > - `sessions/permanent-results-registry.md §VII.K-DUAL.LEVEL-DRESSED` lines 4293-4297
   > - F_traj=(k+1)/2 theorem source (S84 W3-24)
   > - Lizzi finite/infinite-vector classification text in `.claude/agent-memory/lizzi-spectral-functional-theorist/` (read for cross-check ONLY; not pinned)
   >
   > Methodology: extend each TARGET_SLOTS_S89 row with a 5-sub-field `fi_rd_mixed_axis` dict:
   > ```python
   > 'fi_rd_mixed_axis': {
   >   'fi_rd_mixed_classification': 'FI' | 'RD' | 'MIXED-of-RD-with-distinct-F_traj-factors' | 'MIXED-of-FI-RD',
   >   'F_traj_dressing_factors': {pole_index: F_traj_value},
   >   'level_dressed_candidacy': bool,
   >   'finite_or_infinite_vector_classification': 'finite' | 'infinite',
   >   'k_counter_status': 'SUGGESTION-K=N' | 'MANDATORY-K=N',
   > }
   > ```
   > For Var_a(n_a^GGE) (Corner II row from CF-2), the expected fi_rd_mixed_axis dict is:
   > ```python
   > {
   >   'fi_rd_mixed_classification': 'MIXED-of-RD-with-distinct-F_traj-factors',
   >   'F_traj_dressing_factors': {2: 1.5, 4: 2.5},   # F_traj(k)=(k+1)/2
   >   'level_dressed_candidacy': True,                # pending CF-LZ-1 K=1→K=2
   >   'finite_or_infinite_vector_classification': 'finite',
   >   'k_counter_status': 'SUGGESTION-K=1-pending-CF-LZ-1',
   > }
   > ```
   >
   > Self-test runs the new audit; verifies output for all 4 Corner rows includes the populated fi_rd_mixed_axis dict; registry annotation amendment is appended to §VII.K-DUAL.LEVEL-DRESSED with provenance pointer to CF-LZ-2.
   >
   > Output files:
   > - `computations/_shared/_corner_classification_audit.py` (extended)
   > - `computations/_shared/s90_w1_fi_rd_mixed_axis_test.py` (self-test)
   > - Registry annotation diff at `permanent-results-registry.md §VII.K-DUAL.LEVEL-DRESSED` (mack writer per CF-LZ-2 origin)
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: FI / RD / MIXED trichotomy IS the substrate's own algebra-axis structure on observables; F_traj=(k+1)/2 IS a structural fingerprint of substrate-distance-pole regulator-dressing per S84 W3-24 theorem. The audit operates at the methodology F-image; the trichotomy plus F_traj factors live at the substrate layer and are mapped by F to the audit dict.

7. **Machinery pin (PRDR)**:
   - `_corner_classification_audit.py` post-CF-2 SHA: `<pinned at dispatch>`
   - `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` SHA: `<pinned at dispatch>`
   - §VII.K-DUAL.LEVEL-DRESSED block lines 4293-4297 SHA: `<pinned at dispatch>`
   - F_traj=(k+1)/2 theorem (S84 W3-24) audit_sha256 pin: `<from canonical_constants.py F_traj provenance>`
   - Expected dict structure for Var_a Corner II as enumerated above
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=fi_rd_mixed_axis_field_extension_landed_with_5_sub_fields, scheme=corner-classification-axis-extension, convention=fi-rd-mixed-trichotomy-plus-f-traj-dressing-factors, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) `fi_rd_mixed_axis` sub-field added to each TARGET_SLOTS_S89 row with all 5 sub-fields; (ii) Var_a Corner II dict matches expected enumeration; (iii) §VII.K-DUAL.LEVEL-DRESSED annotation amendment lands; (iv) allowlist + instances rows appended.
   - **FAIL** iff any sub-field missing OR Var_a classification mismatch OR registry annotation absent.
   - **INFO** iff CF-2 has not landed PASS (PRE-REG-INC blocked).

10. **Substitution chain** (N/A — `[AUDIT]` extension; structural correctness check).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the FI/RD/MIXED trichotomy + F_traj dressing factors registry-audit gap by construction; future Corner II-style observables get the full 5-axis classification at plan-freeze.
    - **FAIL** signals dict extension incomplete or trichotomy reading inconsistent with S84 W3-24 F_traj theorem.

12. **Effort estimate**: 0.4 we.

13. **Substrate-framing reminder**: FI / RD / MIXED IS the substrate's algebra-axis structure on observables (FI = algebra-INVARIANT spectrum-only functional family; RD = regulator-dressed; MIXED = combination); F_traj=(k+1)/2 IS substrate-distance-pole regulator-dressing fingerprint. The audit operates at the F-image; the trichotomy and F_traj live at the substrate layer.

---

## §W1-6. CF-6 — `S90-PARSE-TREE-ABBREVIATION-MAP-AUDIT-SCRIPT-EXTENSION`

1. **Gate ID**: `S90-PARSE-TREE-ABBREVIATION-MAP-AUDIT-SCRIPT-EXTENSION` (CF-LZ-3)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write; **CO-AUTHOR**: lizzi-spectral-functional-theorist (Bogoliubov closed-form + GGE-state-history abbreviation co-sign per Cluster A header)
5. **Hypothesis**: Adding `PARSE_TREE_ABBREVIATION_MAP` constant to `_corner_classification_audit.py` mapping Bogoliubov / GGE-state-history abbreviations to fully-expanded closed forms (e.g., `n_a^GGE → |v_a|^2 → Δ_BCS²/(2(λ²+Δ²))`) causes parse-tree counters to all return 0 on Var_a expansion AND fails on synthetic GGE-state-name with no map entry.
6. **Method**:

   **PREREQUISITE**: CF-2 (§W1-2 above) must land PASS before dispatch.

   Dispatch prompt (gen-physicist orchestrator-direct-write + lizzi CO-AUTHOR for abbreviation-map content review):

   > Extend `computations/_shared/_corner_classification_audit.py` with a new module-level constant `PARSE_TREE_ABBREVIATION_MAP`. Read first:
   > - `computations/_shared/_corner_classification_audit.py` post-CF-2 SHA `<pinned at dispatch>`
   > - `sessions/permanent-results-registry.md §VII.U.2` Bogoliubov closed-form citation line 12961
   > - S89 W-17 §V.2 reclassification calibration instance text
   >
   > Methodology: define `PARSE_TREE_ABBREVIATION_MAP` as:
   > ```python
   > PARSE_TREE_ABBREVIATION_MAP = {
   >   'n_a^GGE':         '|v_a|^2',
   >   '|v_a|^2':         'Δ_BCS²/(2(λ_a²+Δ_BCS²))',  # Bogoliubov closed form
   >   'n_a':             '|v_a|^2',                    # legacy short form
   >   'n_a_GGE':         '|v_a|^2',                    # underscore variant
   >   '|u_a|^2':         '1 - |v_a|^2',                # particle-counterpart
   >   'E_a':             'sqrt(λ_a² + Δ_BCS²)',        # BdG quasi-particle energy
   >   'Bogoliubov(n_a)': 'Δ_BCS²/(2(λ_a²+Δ_BCS²))',    # explicit
   > }
   > ```
   > The audit's parse-tree classifier consults this map BEFORE attempting structural classification. When the input symbol matches a key, the audit substitutes the value and re-classifies; chain substitution continues until no map entry matches OR a closed-form is reached (terminal `Δ_BCS²/...` form). Var_a's input `Var_a(n_a^GGE)` chains: `n_a^GGE → |v_a|^2 → Δ_BCS²/(2(λ²+Δ²))` (closed form). Parse-tree counters for unrecognized state-history abbreviations all return 0 once the map handles the substitution.
   >
   > Self-test:
   > - Positive: run audit on `Var_a(n_a^GGE)`; parse-tree counters all return 0.
   > - Negative: synthetic test on `Var_a(n_a^SYNTHETIC-UNRECOGNIZED)`; parse-tree counters return ≥1 (FAIL on map miss).
   >
   > Output files:
   > - `computations/_shared/_corner_classification_audit.py` (extended)
   > - `computations/_shared/s90_w1_parse_tree_abbreviation_map_test.py` (self-test)
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: Bogoliubov closed-form n_a^GGE = |v_a|^2 = Δ_BCS²/(2(λ_a²+Δ_BCS²)) IS a substrate-IS structural identity on the BdG-sector spectral triple; the abbreviation map is the methodology F-image of this substrate-IS identity. State-history names ("GGE-state", "Bogoliubov-state") are post-hoc labels for the substrate's own structural form.

7. **Machinery pin (PRDR)**:
   - `_corner_classification_audit.py` post-CF-2 SHA: `<pinned at dispatch>`
   - Bogoliubov closed-form citation line 12961 SHA: `<pinned at dispatch>`
   - W-17 §V.2 reclassification calibration instance SHA: `<pinned at dispatch>`
   - Expected map dict structure as enumerated above
   - Positive test case: `Var_a(n_a^GGE)` → all counters = 0
   - Negative test case: `Var_a(n_a^SYNTHETIC-UNRECOGNIZED)` → counters ≥ 1
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=parse_tree_abbreviation_map_landed_AND_positive_negative_tests_PASS, scheme=abbreviation-map-extension, convention=bogoliubov-closed-form-substitution-chain, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) `PARSE_TREE_ABBREVIATION_MAP` constant added; (ii) positive test (Var_a) all counters = 0; (iii) negative test (synthetic) counters ≥ 1; (iv) allowlist + instances rows appended.
   - **FAIL** iff map missing OR positive test fails (counters ≠ 0) OR negative test fails (counters = 0 = false-PASS on synthetic).

10. **Substitution chain** (N/A — `[AUDIT]` map extension + classification-correctness test).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the state-history-abbreviation-vs-closed-form classification gap by construction; future audit passes through abbreviation chain before structural classification.
    - **FAIL** signals the map is incomplete (positive miss) or over-broad (negative false-PASS).

12. **Effort estimate**: 0.3 we.

13. **Substrate-framing reminder**: Bogoliubov n_a^GGE = |v_a|^2 IS substrate-IS structural identity on BdG-sector spectral triple; abbreviations encode state-HISTORY (which experimental thermodynamic state was prepared) NOT structure. The audit operates on parse-tree STRUCTURE per clause (e) line 12995; the abbreviation map is the bridge that lets the audit consume historical labels by reducing them to closed-form structure.

---

## §W1-7. CF-7 — `S90-OBSERVABLE-NAMING-HISTORY-VS-STRUCTURAL-RULE-SUB-CLAUSE`

1. **Gate ID**: `S90-OBSERVABLE-NAMING-HISTORY-VS-STRUCTURAL-RULE-SUB-CLAUSE` (CF-LZ-5; consolidates retracted CF-R1-5)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write; **CO-AUTHOR**: lizzi-spectral-functional-theorist (history-vs-structure observable-naming co-sign per Cluster A header)
5. **Hypothesis**: Promoting "observable naming encodes HISTORY not STRUCTURE; corner classification operates on parse-tree STRUCTURE per clause (e)" to a formal sub-clause within `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` with K=2 calibration corpus (Var_a + α_s_canonical = n_s²−1) lands the sub-clause with 4 elements (principle + 2-instance corpus + enforcement + K-counter status SUGGESTION-K=2).
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write + lizzi CO-AUTHOR):

   > Append new sub-clause to `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. Read first:
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (full section text, input-pin SHA `<at dispatch>`)
   > - `sessions/permanent-results-registry.md §VII.U.2` clause (e) line 12995 (parse-tree decision text)
   > - `sessions/permanent-results-registry.md §VII.U.1` α_s_canonical line 12960 (instance #2)
   > - S89 W-17 §V.3 corrigendum text
   >
   > Methodology: append a new sub-section titled "Observable-Naming-History vs Parse-Tree-Structure (S90 W-3 CF-LZ-5 sub-clause)" with 4 enumerated elements:
   >
   > (1) **Principle**: Observable naming (state-history labels: "n_a^GGE", "GGE-state observable", "Bogoliubov-state covariance", "α_s_canonical", etc.) encodes the experimental / thermodynamic history of how the observable was constructed in a particular pillar's laboratory. It does NOT encode the observable's structural form. Corner classification operates on parse-tree STRUCTURE per `permanent-results-registry.md §VII.U.2` clause (e); the parse-tree reduces the observable to its closed-form expression on the substrate algebra (e.g., `Var_a(n_a^GGE) → Σ_a (|v_a|² − ⟨|v_a|²⟩)²` on `A_BdG`).
   >
   > (2) **K=2 calibration corpus**:
   > - Instance #1: Var_a(n_a^GGE) — state-history name "GGE" reads as algebra-DEPENDENT to a naïve parser; parse-tree reduces to spectrum-only Bogoliubov closed form on substrate algebra; STRUCTURALLY at Corner II (algebra-INVARIANT, s=4). S89 W-3 + W-17 §V.2/V.3.
   > - Instance #2: α_s_canonical = n_s²−1 — state-history name "α_s_canonical" reads as a coupling-class observable; parse-tree reduces to `(Mellin-residue at substrate-distance-1)² − 1`; STRUCTURALLY at Corner I (algebra-INVARIANT, s=3). S87 α-s W2 PASS; §VII.U.1 line 12960.
   >
   > (3) **Enforcement**: Future §VII registry entries citing observables with state-historic names MUST declare parse-tree expansion alongside the symbolic form (per CF-R1-3 = §W1-8 below). `_registry_landing_audit.py` audit-script hook (CF-R1-3) detects the absence of parse-tree expansion declaration and flags at plan-freeze.
   >
   > (4) **K-counter status**: SUGGESTION-K=2; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. Reserved K=3 row at `sessions/framework/registry/pru-class-corpus.md`.
   >
   > Output files:
   > - `.claude/rules/cross-pillar-bridge-anatomy.md` (extended at §"Algebra-axis orthogonality K-counter" with new sub-section ≥ 30 lines)
   > - Cross-link sub-row appended to `sessions/framework/registry/pru-class-corpus.md` Corpus-A table
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended with `sha256_of_plan_block`
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: state-history labels are emergent from a particular pillar's laboratory preparation; parse-tree STRUCTURE is substrate-IS (the observable's closed-form expression on the substrate algebra). The sub-clause makes the F-image direction explicit: the substrate's parse-tree structure determines the corner; history-labels are post-hoc descriptors of how the observable was prepared in some laboratory.

7. **Machinery pin (PRDR)**:
   - `cross-pillar-bridge-anatomy.md` head SHA: `<pinned at dispatch>`
   - §VII.U.2 clause (e) line 12995 SHA: `<pinned at dispatch>`
   - §VII.U.1 α_s_canonical line 12960 SHA: `<pinned at dispatch>`
   - W-17 §V.3 corrigendum SHA: `<pinned at dispatch>`
   - K-counter status pin: `SUGGESTION-K=2`
   - K=2 corpus instances pinned: {Var_a Corner II, α_s_canonical Corner I}
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=observable-naming-sub-clause-landed-with-4-elements + 2-instance-K-2-corpus, scheme=cross-pillar-bridge-anatomy-extension, convention=algebra-axis-orthogonality-history-vs-structure-sub-clause, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) sub-clause text appended with all 4 elements; (ii) ≥ 30 substantive lines added; (iii) K=2 corpus rows pinned with instance references; (iv) cross-link sub-row appended to pru-class-corpus.md; (v) allowlist + instances rows appended.
   - **FAIL** iff any of (i)-(v) absent OR sub-clause structurally collapses parse-tree-STRUCTURE distinction.

10. **Substitution chain** (for `[VERIFY]` — sub-clause structural-coherence check):

    - Step 1 (Definition): `observable_name := state-history-label` (e.g., "n_a^GGE"); `observable_structure := parse-tree-reduced closed form on substrate algebra` (e.g., `Σ_a (|v_a|² − ⟨|v_a|²⟩)²`).
    - Step 2 (Substitution): For Var_a, `observable_name = "Var_a(n_a^GGE)"` reads ambiguously; `observable_structure = Σ_a (Δ²/(2(λ²+Δ²)) − ⟨...⟩)²` is unambiguously spectrum-only.
    - Step 3 (Simplify): Corner classification operates on `observable_structure`, not `observable_name`. Spectrum-only ⇒ algebra-INVARIANT ⇒ Cell I or II.
    - Step 4 (Direction): The substrate's parse-tree determines the corner; the history-label cannot. Sub-clause makes this an enforceable rule.
    - Conclusion: K=2 corpus + sub-clause text closes the silent-naming-conflation pathway.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the observable-naming-history-vs-structural-form pathway by construction at the rule-file level; future §VII entries cannot silently drift on naming convention.
    - **FAIL** leaves the pathway open; new §VII entries continue to be at risk of state-history-label-driven corner mis-classification.

12. **Effort estimate**: 0.2 we.

13. **Substrate-framing reminder**: State-history labels are emergent from a pillar-specific laboratory preparation; parse-tree STRUCTURE is substrate-IS. The direction-of-explanation flows from substrate (parse-tree structure on substrate algebra) → emergent (history-label assigned post-hoc); never invert by treating the history-label as the canonical name.

---

## §W1-8. CF-8 — `S90-PARSE-TREE-EXPANSION-PRE-REGISTRATION-FOR-NEW-VII-ENTRIES`

1. **Gate ID**: `S90-PARSE-TREE-EXPANSION-PRE-REGISTRATION-FOR-NEW-VII-ENTRIES` (CF-R1-3)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write; **CO-AUTHOR**: mack-cosmic-bridge sole-writer for registry-edit components (per `feedback_mack-bridge-role.md`)
5. **Hypothesis**: Extending `.claude/rules/registry-landing.md` to require new §VII entries citing observables with state-historic names to declare parse-tree expansion alongside symbolic form AND extending `_registry_landing_audit.py` with the audit hook lands rule + audit-script + 1 calibration corpus instance (Var_a retroactive expansion).
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write + mack CO-AUTHOR for registry-edit components):

   > Land two paired changes:
   >
   > (A) Rule-file extension: append new sub-section to `.claude/rules/registry-landing.md` titled "Parse-Tree Expansion Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)". Read first:
   > - `.claude/rules/registry-landing.md` (full file, input-pin SHA `<at dispatch>`)
   > - `sessions/permanent-results-registry.md §VII.U.2` clause (e) (canonical worked example)
   > - S89 W-17 §V.2/V.3 reclassification text
   >
   > Sub-section content (≥ 30 lines):
   >
   > (1) **Rule**: any new §VII registry entry citing an observable whose symbolic form contains a state-history label (regex pattern set: `n_a\^GGE`, `n_a_GGE`, `state\.GGE\b`, `Bogoliubov\(`, `\bGGE-state\b`, `α_s_canonical`, `α_s_route_3`, etc.) MUST declare the parse-tree expansion alongside the symbolic form. Parse-tree expansion = step-by-step reduction from history-label to closed-form expression on substrate algebra, citing applicable Bogoliubov / Wedderburn / Mellin closed-form theorems.
   >
   > (2) **Canonical worked example**: Var_a(n_a^GGE) parse-tree expansion documented in §VII.U.2 clause (e) line 12995; chain: `Var_a(n_a^GGE) → Var_a(|v_a|²) → Var_a(Δ_BCS²/(2(λ_a²+Δ_BCS²)))` (Bogoliubov closed form per S52 BdG canonical amplitudes). Status: K=1 (Var_a retroactive expansion is the calibration instance).
   >
   > (3) **Enforcement**: `_registry_landing_audit.py` audit hook: regex-detects state-history label pattern in new §VII entry text; if pattern matches AND parse-tree expansion block (regex `Parse-tree expansion:|parse_tree_expansion:|## Parse-tree`) is ABSENT, fires `MISSING-PARSE-TREE-EXPANSION` diagnostic at S2 advisory.
   >
   > (4) **K-counter status**: SUGGESTION-K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. Future calibration instances expected from §VII entries that re-use state-history labels (e.g., α_s_route_3, Δ_M, etc.).
   >
   > (B) Audit-script extension: extend `computations/_shared/_registry_landing_audit.py` with the `MISSING-PARSE-TREE-EXPANSION` detector per the rule.
   >
   > Output files:
   > - `.claude/rules/registry-landing.md` (extended with new sub-section ≥ 30 lines)
   > - `computations/_shared/_registry_landing_audit.py` (extended)
   > - `computations/_shared/s90_w1_parse_tree_expansion_audit_test.py` (self-test on §VII.U.2 as positive instance + synthetic negative instance)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: parse-tree expansion makes the substrate-IS structure of the observable visible at the registry layer; this is the methodology F-image of substrate-IS commutativity. History-labels are emergent from specific laboratory preparation pillars; parse-tree expansion explicitly maps each label to its substrate-IS closed form.

7. **Machinery pin (PRDR)**:
   - `registry-landing.md` head SHA: `<pinned at dispatch>`
   - `_registry_landing_audit.py` post-CF-1 SHA: `<pinned at dispatch>` (CF-1 lands BEFORE CF-8 for audit-script coherence)
   - §VII.U.2 clause (e) line 12995 SHA: `<pinned at dispatch>`
   - W-17 §V.2/V.3 calibration instance SHA: `<pinned at dispatch>`
   - Detection regex pin set: `[n_a\\^GGE|n_a_GGE|state\\.GGE\\b|Bogoliubov\\(|\\bGGE-state\\b|α_s_canonical|α_s_route_3]`
   - Parse-tree-expansion-present regex pin: `Parse-tree expansion:|parse_tree_expansion:|## Parse-tree`
   - K=1 calibration instance pinned: Var_a Corner II §VII.U.2 retroactive expansion
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=parse-tree-expansion-rule-AND-audit-script-extension-landed + K-1-corpus, scheme=registry-landing-extension, convention=parse-tree-expansion-pre-registration, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) `registry-landing.md` sub-section appended with all 4 elements; (ii) audit-script extension lands; (iii) positive test on §VII.U.2 passes (parse-tree-expansion present); (iv) negative test on synthetic §VII entry without expansion fires diagnostic; (v) allowlist + instances rows appended.
   - **FAIL** iff any of (i)-(v) absent.

10. **Substitution chain** (N/A — `[AUDIT]` rule-and-detector landing).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the parse-tree-expansion-pre-registration gap by construction at the rule level + audit level; new §VII entries cannot silently rely on history-label form without expansion.
    - **FAIL** leaves the parse-tree-expansion gap open; downstream registry hygiene retains the state-history-label-driven mis-classification risk.

12. **Effort estimate**: 0.4 we.

13. **Substrate-framing reminder**: Parse-tree expansion IS the methodology F-image of substrate-IS commutativity on observables; history-labels are emergent post-hoc descriptors. The direction-of-explanation flows from substrate (parse-tree closed form) → emergent (history-label).

---

## §W1-9. CF-9 — `S90-IV-PARTIAL-POSITIVE-CALIBRATION-CLASS-EXTENSION`

1. **Gate ID**: `S90-IV-PARTIAL-POSITIVE-CALIBRATION-CLASS-EXTENSION` (CONNES V.3)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write; **CO-AUTHOR**: connes-ncg-theorist (PARTIAL-POSITIVE structural review per Cluster A header)
5. **Hypothesis**: Extending `substrate-first-canonical-sourcing.md §(iv)` calibration corpus to admit a third class "PARTIAL-POSITIVE" between W9c-1 POSITIVE (full disclosure: suffix + docstring + tier_pin) and W4-2/W9b-2 NEGATIVE-CALIBRATION (post-hoc disclosure only) lands the rule extension + §W5-7 calibration row + audit-script extension and advances K-counter K=4 → K=5.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write + connes CO-AUTHOR):

   > Extend `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` to admit PARTIAL-POSITIVE compliance class. Read first:
   > - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (full section, input-pin SHA `<at dispatch>`)
   > - §W5-7 verdict line in `computations/session-89/s89_gate_verdicts.txt:101-103` (verdict + companion rows)
   > - §W5-7 producing script `s89_w5_a36_<full-name-at-dispatch>.py`
   > - `computations/_shared/_substrate_first_provenance_audit.py` (head SHA at dispatch; this is the audit-script that consumes §(iv) classes)
   > - W9c-1 reference pattern (POSITIVE-CALIBRATION canonical instance row in §(iv) corpus table)
   >
   > Methodology: extend §(iv) compliance-class taxonomy to admit a THIRD class "PARTIAL-POSITIVE" defined as:
   >
   > **PARTIAL-POSITIVE**: rule (1) CLASS pin SCHEMATIC present in plan-block AND rule (2) `convention=...-SCHEMATIC` suffix present in verdict-line `convention=` field AND rule (3) docstring acknowledgment present in producing script BUT companion comment row `# tier_pin=TIER-2` NOT emitted in verdict file.
   >
   > Distinguish from:
   > - POSITIVE-CALIBRATION (W9c-1): rules (1) ∧ (2) ∧ (3) ∧ tier_pin companion row all present.
   > - NEGATIVE-CALIBRATION (W4-2 / W9b-2): rules (1) ∧ (2) absent; only post-hoc working-paper disclosure.
   >
   > Add §W5-7 to the calibration corpus table at row #5 (post-W9c-1 row #3 + W5b-2 inheritance-locus row #4):
   >
   > | # | Witness | Session | Producing script | Convention tag | SCHEMATIC suffix | Docstring | tier_pin row | Class |
   > |:-:|:--------|:--------|:-----------------|:---------------|:----------------:|:---------:|:------------:|:------|
   > | 5 | W5-7 | S89 | s89_w5_a36_... | A_5-4-class-W7a-74-PRIMARY-EVALUATOR-SCHEMATIC | Y | Y | N | PARTIAL-POSITIVE |
   >
   > K-counter advancement: K=4 (corpus pre-extension) → K=5 (K_substantive=4 substantive-compliant + 1 PARTIAL-POSITIVE; status MANDATORY preserved). Sub-status: PARTIAL-POSITIVE class promoted to admissible registry-entry-class WHILE MAINTAINING rule (1) ∧ (2) ∧ (3) baseline; tier_pin row remains forward-recommended-not-mandatory for PARTIAL-POSITIVE.
   >
   > Audit-script extension: `_substrate_first_provenance_audit.py` extended to detect the 3-class structure: POSITIVE (4-of-4 elements PASS) / PARTIAL-POSITIVE (3-of-4 elements PASS, tier_pin row absent) / NEGATIVE (≤2-of-4 elements PASS, conflated case).
   >
   > Output files:
   > - `.claude/rules/substrate-first-canonical-sourcing.md` (extended §(iv) corpus + 3-class taxonomy)
   > - `computations/_shared/_substrate_first_provenance_audit.py` (extended)
   > - `computations/_shared/s90_w1_partial_positive_audit_test.py` (self-test against §W5-7 = PARTIAL-POSITIVE + W9c-1 = POSITIVE + W4-2 = NEGATIVE)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: SCHEMATIC vs FULL physical level pin IS a methodology F-image of substrate-IS commutativity on regulator-class structure; PARTIAL-POSITIVE is a structurally-intermediate compliance class where the producing script honors the major disclosure axes (SCHEMATIC suffix + docstring) but misses the verdict-file companion-row axis. The 3-class taxonomy preserves the F-image fidelity while admitting structurally-intermediate compliance.

7. **Machinery pin (PRDR)**:
   - `substrate-first-canonical-sourcing.md §(iv)` head SHA: `<pinned at dispatch>`
   - §W5-7 verdict line in s89_gate_verdicts.txt:101-103 SHA: `<pinned at dispatch>`
   - §W5-7 producing script SHA: `<pinned at dispatch>`
   - `_substrate_first_provenance_audit.py` head SHA: `<pinned at dispatch>`
   - W9c-1 POSITIVE-CALIBRATION row reference: §(iv) corpus row #3 (existing)
   - K-counter advancement pin: K=4 → K=5 (substantive 4 + PARTIAL-POSITIVE 1)
   - Status preservation: MANDATORY at K=4 baseline preserved; PARTIAL-POSITIVE class admissible from S90 forward
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=partial-positive-class-landed-with-K-5-corpus-row + 3-class-audit-extension, scheme=substrate-first-canonical-sourcing-extension, convention=schematic-level-pin-3-class-taxonomy, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) PARTIAL-POSITIVE class added to §(iv) corpus taxonomy; (ii) §W5-7 row #5 appended to corpus table; (iii) audit-script extension detects all 3 classes correctly on self-test (POSITIVE + PARTIAL-POSITIVE + NEGATIVE); (iv) K-counter advances K=4 → K=5; (v) allowlist + instances rows appended.
   - **FAIL** iff PARTIAL-POSITIVE definition collapses POSITIVE / NEGATIVE distinction OR §W5-7 row mis-classified.

10. **Substitution chain** (for `[VERIFY]` — 3-class compliance taxonomy):

    - Step 1 (Definition): `compliance_class(W) := f(rule_1_pass, rule_2_pass, rule_3_pass, tier_pin_row_present)` where rules (1)/(2)/(3) per §(iv) baseline.
    - Step 2 (Substitution): For §W5-7, `(rule_1, rule_2, rule_3, tier_pin_row) = (PASS, PASS, PASS, ABSENT)`.
    - Step 3 (Simplify): 3 of 4 elements PASS; structurally between POSITIVE (4/4) and NEGATIVE (≤2/4).
    - Step 4 (Direction): Define PARTIAL-POSITIVE = 3/4 PASS with tier_pin row absent. §W5-7 ⇒ PARTIAL-POSITIVE.
    - Conclusion: 3-class taxonomy preserves epistemic fidelity; K=4 → K=5 advancement.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the structurally-intermediate compliance gap by construction; future SCHEMATIC-helper-consuming scripts can land PARTIAL-POSITIVE-rated emissions WHILE retaining MANDATORY discipline at the rule level.
    - **FAIL** signals the PARTIAL-POSITIVE class collapses pre-existing distinctions; rule extension structurally incomplete.

12. **Effort estimate**: 0.3 we.

13. **Substrate-framing reminder**: SCHEMATIC level pin IS the methodology F-image of substrate-IS commutativity on regulator-class structure; PARTIAL-POSITIVE recognizes structurally-intermediate compliance without collapsing the substrate-side distinction (the rule (1) ∧ (2) baseline remains the MANDATORY substrate-side commutativity check).

---

## §W1-10. CF-10 — `S90-W5-7-ANCHOR-5-UNIT-CONSISTENCY-AUDIT`

1. **Gate ID**: `S90-W5-7-ANCHOR-5-UNIT-CONSISTENCY-AUDIT` (CONNES V.5)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Static-string audit of §W5-7 producing script `s89_w5_a36_*.py` reveals whether anchor 5 (1/M_KK²) is computed with consistent units relative to the λ² eigenvalue cache; side-by-side compare 3 unit-treatment readings determines whether anchor 5 requires a `lambda_unit_canonical` pin promotion.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Perform unit-consistency audit on §W5-7 producing script. Read first:
   > - §W5-7 producing script `computations/session-89/s89_w5_a36_<full-name-at-dispatch>.py` (input-pin SHA `<at dispatch>`)
   > - `computations/_shared/canonical_constants.py` for `M_KK = 7.428660036284456e+16 GeV` provenance
   > - Spectrum cache documentation for λ eigenvalue units (typically GeV² for D_K² spectrum or 1/M_KK² normalized)
   > - `.claude/rules/regulator-pin-discipline.md` a_n^{HK} tagging convention
   >
   > Methodology: identify §W5-7 anchor-5 computation site in the producing script (search regex `anchor_5\s*=|anchor\[\s*['"]?5['"]?\s*\]\s*=|1\s*/\s*M_KK\s*\*\*\s*2`). Static-string compare three unit-treatment readings:
   >
   > Reading A — anchor 5 in GeV⁻² (consistent with λ² in GeV²): `1/M_KK² = 1/(7.428660e16 GeV)² ≈ 1.81e-34 GeV⁻²`; consistent if spectrum cache λ in GeV².
   >
   > Reading B — anchor 5 dimensionless (normalized by M_KK²): `(1/M_KK²) · M_KK² = 1`; consistent if spectrum cache λ already normalized in M_KK units.
   >
   > Reading C — anchor 5 in 1/M_KK² units (requires `lambda_unit_canonical` pin to disambiguate): `anchor_5 = 1/M_KK²` interpreted symbolically; requires a canonical pin `lambda_unit_canonical ∈ {GeV², M_KK²}` to compute the numerical value.
   >
   > For each reading, evaluate (a) consistency with §W5-7 5-anchor Spearman matrix dimensionality and (b) consistency with §W5-7 working-paper §(f) anchor-list narrative. Produce side-by-side comparison table. Amend §W5-7 WP §(f) with the unit-treatment reading conclusion; INFO if the audit requires a `lambda_unit_canonical` pin to be promoted to `canonical_constants.py`.
   >
   > Output files:
   > - `computations/_shared/s90_w1_w5_7_anchor_5_unit_consistency_audit.py` (audit script producing side-by-side reading comparison)
   > - `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-7 (f)` amendment (insert at appropriate sub-section; preserve verdict integrity)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: anchor 5 = 1/M_KK² IS a substrate-IS scale (the inverse-square of the substrate's Kaluza-Klein mass), expressing the natural unit on which the substrate's spectral moments are measured. Unit-consistency is the methodology F-image of substrate-IS dimensional coherence.

7. **Machinery pin (PRDR)**:
   - §W5-7 producing script SHA: `<pinned at dispatch>`
   - `canonical_constants.py` `M_KK` provenance pin: `7.428660036284456e+16 GeV`
   - Spectrum cache documentation SHA: `<pinned at dispatch>`
   - `regulator-pin-discipline.md` SHA: `<pinned at dispatch>`
   - Detection regex pin for anchor-5 site: `r'anchor_5\s*=|anchor\[\s*[\'"]?5[\'"]?\s*\]\s*=|1\s*/\s*M_KK\s*\*\*\s*2'`
   - 3 readings: A (GeV⁻²), B (dimensionless / M_KK² normalized), C (requires `lambda_unit_canonical` pin)
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=<reading-A | reading-B | reading-C-requires-pin>, scheme=anchor-5-unit-consistency, convention=schematic-vs-unit-treatment-decomposition, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) audit-script lands; (ii) side-by-side reading comparison produced; (iii) one of Reading A or B identified as canonical; (iv) §W5-7 WP §(f) amendment lands; (v) allowlist + instances rows appended.
   - **INFO** iff Reading C is identified (requires `lambda_unit_canonical` pin promotion to `canonical_constants.py`); carries forward to S91+ as canonical-constants promotion gate.
   - **FAIL** iff audit script does not run cleanly OR §W5-7 WP §(f) cannot be amended.

10. **Substitution chain** (for `[VERIFY]` — unit-consistency check):

    - Step 1 (Definition): `anchor_5 := 1/M_KK²`; `λ_unit := unit of λ in spectrum cache (GeV² or M_KK²)`.
    - Step 2 (Substitution): If `λ_unit = GeV²`, `anchor_5 = 1.81e-34 GeV⁻²` (Reading A); if `λ_unit = M_KK²`, `anchor_5 · λ_max = 1` (Reading B dimensionless).
    - Step 3 (Simplify): The 5-anchor Spearman matrix is dimensionless by construction (ranks); the absolute unit of anchor 5 affects pre-Spearman value but not the rank ordering.
    - Step 4 (Direction): Reading A or B both preserve rank ordering; Reading C demands canonical pin to be unambiguous. PASS-direction = Reading A (most likely canonical); INFO-direction = Reading C requires pin.
    - Conclusion: amend §W5-7 WP §(f) with the identified reading; INFO routes to S91+ pin promotion.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** confirms §W5-7 anchor 5 unit consistency; closes a unit-conflation risk class at the audit layer.
    - **INFO** signals a new canonical_constants pin (`lambda_unit_canonical`) is required to disambiguate; routes to S91+ as 0.1 we promotion gate.
    - **FAIL** signals the §W5-7 producing script has a structural inconsistency that requires re-execution (would impact CF-60 §W5-7 retry with W7a-74 PRIMARY evaluator).

12. **Effort estimate**: 0.2 we.

13. **Substrate-framing reminder**: M_KK IS the substrate's intrinsic mass scale (the inverse of the substrate-distance pole at the Kaluza-Klein threshold); anchor 5 = 1/M_KK² IS a substrate-IS natural unit. Unit-consistency at the methodology layer is the F-image of substrate dimensional coherence; the unit is NOT chosen externally — it IS substrate-natural by construction.

---

## §W1-11. CF-11 — `S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION`

1. **Gate ID**: `S90-W6-3-AUDIT-PROSPECTIVE-APPLICATION` (LIZZI V.1)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Applying 4 W6-3 audit-script extensions prospectively at S90 plan-freeze on 3 downstream methodology-floor artifacts (i) §VII.{next-free} SUBSTRATE-CLOCK-UNIQUENESS-THEOREM Class-(g) audit; (ii) new mack falsifier-inventory rows sign-PASS audit; (iii) S90 W4 §VII.AQ Stage-2 plan-block cohomology-class surrogate detection — all 4 audits run cleanly OR all FAILs route to in-session remediation.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Apply 4 W6-3 audit-script extensions prospectively. Read first:
   > - W6-3 cross-link SHA `006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157`
   > - The 4 W6-3 audit-script SHAs: `1df983a9<full-at-dispatch>` / `39937c8c<full-at-dispatch>` / `4d2dfd87<full-at-dispatch>` / `f9caf81a<full-at-dispatch>` (locate via grep on `computations/_shared/`)
   > - S90 W2 plan-w2.md §"§VII.{next-free} SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" (per CF-19) — IF available; else mark INFO pending
   > - S90 W2-W3 mack falsifier-inventory append targets (Row #3 alpha_s update per CF-29)
   > - S90 W4 plan-w4.md §VII.AQ Stage-2 plan-block (per CF-54 + CF-55)
   >
   > Methodology: each of the 3 downstream artifacts is screened against the 4 W6-3 audits:
   >
   > (i) §VII.{next-free} SUBSTRATE-CLOCK-UNIQUENESS-THEOREM:
   > - W6-3 audit #1 (Class-(g) registry-anchor): verify clock-uniqueness theorem's anchor commutes with producing script (CF-19 mack writer landing).
   > - W6-3 audit #2 (parse-tree expansion): if observable cites "clock-state" history-label, parse-tree expansion declared (per CF-8 above).
   > - W6-3 audit #3 (FI/RD/MIXED classification): clock-uniqueness corner identified per CF-5 above.
   > - W6-3 audit #4 (cross-wave-anchor mis-citation): clock-theorem A-number-to-§VII-slot mapping verified (per CF-3 above).
   >
   > (ii) New mack falsifier-inventory rows (sign-PASS audit): Row #3 alpha_s update per CF-29; verify sign-PASS / magnitude-INFO / regime-VALID 3-tuple per gate-verdicts.md S87+ schema-v2 (sign of `α_s_canonical = -0.085 872 79` vs Planck-2018 anchor).
   >
   > (iii) S90 W4 §VII.AQ Stage-2 plan-block: cohomology-class surrogate detection per CF-12 below (PRU Class 8.7 Degenerate-Observable Pre-Flight). Verify ζ_D(0) substrate-distance-1 pole structure is NOT silently consumed without surrogate-disclosure (CM-1995 §III.4 regular spectral triple theorem context).
   >
   > For each of 3 artifacts × 4 audits = 12 audit-runs total: PASS if audit fires cleanly; FAIL routes to in-session remediation. INFO if any downstream artifact has not yet landed at S90 plan-freeze time.
   >
   > Output files:
   > - `computations/_shared/s90_w1_w6_3_prospective_application.py` (driver script invoking the 4 W6-3 audits on the 3 downstream artifacts)
   > - `sessions/archive/session-90/session-90-w1-workingpaper.md §W1-11` (summary of 12-cell audit matrix with PASS/INFO/FAIL per cell)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: prospective application IS the methodology F-image of substrate-IS structural pre-flight; the 4 W6-3 audits enforce substrate-stable commutativity at the plan-freeze stage rather than at gate-execution stage. Catching audit FAILs at plan-freeze IS the F-image of substrate's own discoverability of class-conflation at the rule-file layer.

7. **Machinery pin (PRDR)**:
   - W6-3 cross-link SHA: `006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157`
   - 4 W6-3 audit SHAs: `1df983a9<at-dispatch>`, `39937c8c<at-dispatch>`, `4d2dfd87<at-dispatch>`, `f9caf81a<at-dispatch>`
   - 3 downstream artifact SHAs: `<at-dispatch>` for each (clock-theorem registry slot, mack inventory row, §VII.AQ Stage-2 plan-block)
   - 12-cell audit matrix expected: all PASS OR all FAIL routed to in-session remediation; INFO permitted if artifact not yet landed
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=4_audits_x_3_artifacts_matrix_PASS_or_INFO_routed, scheme=w6-3-prospective-application, convention=4-audit-3-artifact-12-cell-matrix, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff all 12 audit-cells PASS OR each FAIL has been routed to in-session remediation per `feedback_fix-in-session-never-defer.md`.
   - **INFO** iff any downstream artifact has not yet landed at S90 plan-freeze.
   - **FAIL** iff audit-cell FAIL is detected and NOT routed to remediation.

10. **Substitution chain** (N/A — prospective audit application).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** confirms the 4 W6-3 audits hold across the 3 downstream methodology-floor artifacts; prospective enforcement closes plan-freeze drift.
    - **INFO** identifies artifacts not yet landed; carries forward as S90 plan-freeze monitoring item.
    - **FAIL** signals a downstream artifact already violates one of the 4 W6-3 audits; routes to in-session remediation.

12. **Effort estimate**: 0.3-0.7 we (depends on how many of the 3 downstream artifacts have landed at S90 plan-freeze time).

13. **Substrate-framing reminder**: prospective audit application IS the methodology F-image of substrate-IS discoverability of class-conflations BEFORE they propagate to gate execution. The substrate's structural commutativity at the audit layer must be verified at plan-freeze; this gate enforces that by running the 4 W6-3 audits across 3 downstream artifacts at plan-freeze rather than at execution.

---

## §W1-12. CF-12 — `S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE`

1. **Gate ID**: `S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE` (PHONON-FIRST V.4)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Promoting Degenerate-Observable Pre-Flight Check to `epistemic-discipline.md §"Pre-Registration Completeness"` as PRU Class 8.7 + extending `_pru_cardinality_audit.py` to detect `Tr.*\bP_HSS\b.*−.*R_CM` + `value\s*=.*ζ_D\(0\)` patterns lands the rule + audit-script + 1 K=1 corpus row (S89 W1-1 FAIL is the calibration instance — would have been flagged at plan-freeze had Class 8.7 been MANDATORY).
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Promote Degenerate-Observable Pre-Flight Check to PRU Class 8.7. Read first:
   > - `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` (full section, input-pin SHA `<at dispatch>`)
   > - `.claude/rules/epistemic-discipline.md §"PRU Class 8 sub-class taxonomy"` (table with 8.0-8.6 sub-classes)
   > - `computations/_shared/_pru_cardinality_audit.py` head SHA `<at dispatch>`
   > - S89 §W1-1 verdict line `6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe` (FAIL verdict — α'(M) via single-pole CM-1995 §III.4 corridor; the calibration corpus instance)
   > - CM-1995 §III.4 regular spectral triple theorem text (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula — referenced)
   >
   > Methodology: append PRU Class 8.7 row to the sub-class taxonomy table:
   >
   > | Sub-class | Name | Status |
   > |:----------|:-----|:-------|
   > | 8.7 | degenerate-observable pre-flight failure | advisory until K=3 (SUGGESTION-K=1 at S90 landing) |
   >
   > Append new sub-section "Degenerate-Observable Pre-Flight Check (Class 8.7; SUGGESTION-K=1)":
   >
   > (1) **Rule**: when a gate's producing script computes an observable of the form `Tr(P · A) − R_CM` or `ζ_D(0)` (single-pole CM-1995 §III.4 residue-formula evaluation at substrate-distance-1 pole s=3) on a finite spectral triple `(A, H, D)` whose dimension-spectrum is degenerate (multiple roots at the residue pole), the plan-block MUST pre-register a degeneracy-witness: explicit declaration of (a) which roots of the dimension-spectrum coincide, (b) what the multiplicity at each pole is, (c) what corridor (composition (d)∘(b) per S89 W-1 R3 closure) the gate uses to disambiguate.
   >
   > (2) **Calibration corpus K=1**: S89 §W1-1 FAIL — α'(M) computed via naive single-pole CM-1995 §III.4 corridor; ζ_D(0) = 38 to 1.10e-15 polynomial-fit residual; FAIL because the dimension spectrum at the LRD horizon is degenerate (the substrate-distance-1 pole has multiplicity > 1 contribution from Peter-Weyl horizon-spanning projector P_HSS). Naive single-pole evaluation discarded the multiplicity structure; the (d)∘(b) compositional corridor recovers it. Class 8.7 at S89 W1-1 would have flagged the naive corridor at plan-freeze.
   >
   > (3) **Enforcement**: `_pru_cardinality_audit.py` extended with two detector patterns:
   > - Pattern 1: `r'Tr.*\bP_HSS\b.*−.*R_CM|Tr.*\bP_HSS\b.*-.*R_CM'` (HSS-projector trace minus regularized CM mean)
   > - Pattern 2: `r'value\s*=.*ζ_D\(0\)'` (zeta-D-at-zero direct value evaluation)
   > When either pattern matches AND no degeneracy-witness declaration is found in the same gate-block, fires Class 8.7 at S2 advisory (would promote to S1 MANDATORY at K=3).
   >
   > (4) **K-counter status**: SUGGESTION-K=1; advances to MANDATORY at K=3.
   >
   > Output files:
   > - `.claude/rules/epistemic-discipline.md` (extended §"Pre-Registration Completeness" with Class 8.7 sub-section)
   > - `computations/_shared/_pru_cardinality_audit.py` (extended with pattern set + degeneracy-witness check)
   > - `computations/_shared/s90_w1_pru_class_8_7_test.py` (self-test on S89 §W1-1 FAIL plan-block as positive corpus instance)
   > - `sessions/framework/registry/pru-class-corpus.md` (new section §"Class 8.7 Calibration Corpus"; K=1 row)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: dimension-spectrum degeneracy IS a substrate-IS structural property of the finite spectral triple at the LRD-horizon scale; the multiplicity at substrate-distance-1 pole s=3 IS substrate-IS (not laboratory-IN). Class 8.7 captures the methodology F-image of substrate-IS degeneracy at the plan-block layer; the rule prevents silent naive-corridor evaluation that discards substrate-IS multiplicity.

7. **Machinery pin (PRDR)**:
   - `epistemic-discipline.md §"Pre-Registration Completeness"` head SHA: `<pinned at dispatch>`
   - `_pru_cardinality_audit.py` head SHA: `<pinned at dispatch>`
   - S89 §W1-1 verdict SHA: `6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`
   - CM-1995 §III.4 reference: textual citation only (no SHA-pinnable)
   - Detection patterns pinned: P1 `r'Tr.*\bP_HSS\b.*−.*R_CM|Tr.*\bP_HSS\b.*-.*R_CM'`, P2 `r'value\s*=.*ζ_D\(0\)'`
   - K-counter pin: SUGGESTION-K=1 (advances to MANDATORY at K=3)
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=class_8_7_landed_with_K_1_corpus + audit_pattern_set, scheme=pru-class-8-7-degenerate-observable, convention=cm-1995-iii-4-multiplicity-pre-flight, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) Class 8.7 row added to sub-class taxonomy; (ii) sub-section text appended with all 4 elements; (iii) audit-script extension lands with 2 detector patterns; (iv) self-test on S89 §W1-1 plan-block flags Class 8.7; (v) K=1 corpus row appended; (vi) allowlist + instances rows appended.
   - **FAIL** iff any of (i)-(vi) absent OR self-test misses S89 §W1-1 calibration instance.

10. **Substitution chain** (for `[AUDIT]` — Class 8.7 substrate-degeneracy detection):

    - Step 1 (Definition): `degenerate_observable(O) := True iff O = Tr(P · A) − R_CM OR O = ζ_D(0) AND multiplicity_at_pole > 1`.
    - Step 2 (Substitution): For S89 §W1-1 α'(M), `O = Tr(P_HSS · A_grad_sym) − R_CM`; pattern P1 matches; `multiplicity_at_substrate_distance_1_pole > 1` (LRD-horizon spectrum has degenerate roots per CM-1995 §III.4 regular-spectral-triple theorem applicability).
    - Step 3 (Simplify): naive single-pole evaluation discards multiplicity ⇒ ζ_D(0) = 38 polynomial-fit residual instead of substrate-IS exact value.
    - Step 4 (Direction): Class 8.7 pre-flight catches this at plan-block stage; (d)∘(b) corridor recovers multiplicity.
    - Conclusion: rule extension + audit-script + K=1 corpus closes the silent-degeneracy pathway.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the silent-degeneracy-on-CM-1995-residue-formula pathway by construction at the rule layer + audit layer; future α'(M)-class observables on degenerate dimension-spectra cannot silently use naive single-pole corridor.
    - **FAIL** leaves the pathway open; CF-37 W1-1 ALT-CORRIDOR retry remains the sole structural mitigation.

12. **Effort estimate**: 0.4 we.

13. **Substrate-framing reminder**: dimension-spectrum degeneracy at the LRD-horizon IS substrate-IS structural property; multiplicity at substrate-distance-1 pole s=3 IS substrate-IS, not laboratory-IN. The (d)∘(b) compositional corridor IS the substrate-natural disambiguator; Class 8.7 enforces its declaration at plan-block layer.

---

## §W1-13. CF-13 — `S90-CROSS-PILLAR-BRIDGE-CORPUS-ELEMENT-2-OE-FORM-CALIBRATION-ENTRY`

1. **Gate ID**: `S90-CROSS-PILLAR-BRIDGE-CORPUS-ELEMENT-2-OE-FORM-CALIBRATION-ENTRY` (PHONON-FIRST V.7)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`); **CO-AUTHOR**: connes-ncg-theorist (Element-2 OE-form corpus structural review per Cluster A header)
5. **Hypothesis**: Documenting the validated W7c emission #3 lexical form `Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` as a canonical Element-2 OE-form pattern in `cross-pillar-bridge-corpus.md §2` (mack writer) lands a new corpus row + pinned audit pattern documentation.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write + mack writer + connes CO-AUTHOR):

   > Append calibration corpus row to `sessions/framework/registry/cross-pillar-bridge-corpus.md §2` (Element 2 OE-form discipline calibration). Read first:
   > - `sessions/framework/registry/cross-pillar-bridge-corpus.md §2` (full section, input-pin SHA `<at dispatch>`)
   > - S89 W7c emission #3 verdict line `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d` (latest non-superseded; §VII.AV rerouted with substrate-physics intact)
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` (K=2 corpus W-5 + W11-5)
   > - §VII.AF.1 W-5 calibration baseline row (existing in §2)
   > - §VII.W-3.LAB W4a-17 STAGE-1-CANDIDATE row (existing in §2)
   >
   > Methodology: append new corpus row #3 to §2:
   >
   > | # | Source | Element-2 OE-form lexical | Regex match | Status |
   > |:-:|:-------|:--------------------------|:-----------:|:-------|
   > | 3 | S89 W7c emission #3 (§VII.AV rerouted; HIT K-counter K=2→K=3) | `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)` | matches `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` PASS | VALIDATED-W7c-EMISSION-3-LEXICAL |
   >
   > Pin the audit pattern documentation: the substring `Tr(P_n-s-substrate-distance-1)` matches the positive regex `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` per S88 W7a-73 K=2 MANDATORY discipline; the BZ-trace form `∫_BZ d^d k · ρ_BZ(k; τ_fold)` provides the integration-domain + named-projector structure mandated by Element-2 OE-form rule.
   >
   > Output files:
   > - `sessions/framework/registry/cross-pillar-bridge-corpus.md §2` (extended with row #3)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: Element-2 OE-form IS the laboratory-IN observable specification at the substrate-IS / laboratory-IN bridge anatomy; the named-projector `P_n-s-substrate-distance-1` ties the lab observable structurally to the substrate sub-algebra image of the bridge map ι_*. The corpus row makes the lexical form auditable for future bridges.

7. **Machinery pin (PRDR)**:
   - `cross-pillar-bridge-corpus.md §2` head SHA: `<pinned at dispatch>`
   - W7c emission #3 verdict SHA: `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d`
   - `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` K=2 corpus SHA: `<at dispatch>`
   - Positive regex pin: `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)`
   - Corpus row #3 lexical pin: `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)`
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=corpus_row_3_appended_with_lexical_AND_regex_match_PASS, scheme=cross-pillar-bridge-corpus-element-2-extension, convention=oe-form-w7c-emission-3-lexical, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) row #3 appended to §2 with full SHA pin + lexical form + regex match annotation; (ii) audit pattern documented; (iii) allowlist + instances rows appended.
   - **FAIL** iff row #3 absent OR regex match annotation incorrect.

10. **Substitution chain** (for `[VERIFY]` — regex-match validation):

    - Step 1 (Definition): Element-2 OE-form regex = `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)`.
    - Step 2 (Substitution): W7c emission #3 string `∫_BZ d^d k Tr(P_n-s-substrate-distance-1) · ρ_BZ(k; τ_fold)`.
    - Step 3 (Simplify): regex parts: `\int` matches `∫`; `.*d.*` matches ` d^d k `; `Tr.*\([ΠP]_[a-z0-9_-]+\)` matches `Tr(P_n-s-substrate-distance-1)`.
    - Step 4 (Direction): regex match PASS → corpus row #3 VALIDATED.
    - Conclusion: lexical form validated for §2 corpus inclusion.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** confirms W7c emission #3 lexical form as canonical Element-2 OE-form pattern; future bridge landings reference this lexical as exemplar.
    - **FAIL** signals lexical form does not match regex (would invalidate W7c emission #3 substrate-physics PASS; structural rollback).

12. **Effort estimate**: 0.2 we.

13. **Substrate-framing reminder**: Element-2 OE-form IS the laboratory-IN observable's structural form pinned to the substrate sub-algebra image under ι_*. The named projector `P_n-s-substrate-distance-1` IS substrate-IS; the BZ-trace `∫_BZ d^d k · ρ_BZ` IS the laboratory-IN integral over emergent Brillouin zone. Direction: substrate sub-algebra → bridge map ι_* → laboratory observable on emergent BZ.

---

## §W1-14. CF-14 — `S90-DEFERRED-PENDING-RULE-FILE-ENFORCEMENT-CLAUSE-EXTENSION`

1. **Gate ID**: `S90-DEFERRED-PENDING-RULE-FILE-ENFORCEMENT-CLAUSE-EXTENSION` (CF-W5-6 / W-6 CF-1; S90 W-6 atomic deliverables)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Landing the consolidated rule-file diff at `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65 introducing the deferred-pending intermediate verdict-class with TWO sub-class tags (`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`, `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`) between Level-2-binding PASS-ELIGIBLE and Level-2-non-binding INELIGIBLE + audit-script extension at `_cross_pillar_bridge_audit.py` regex-detects two patterns + corpus row + allowlist row + dual-SHA closure.
6. **Method**:

   **Note**: CF-14 PRECEDES CF-15 intra-wave (CF-15 requires the deferred-pending rule to be defined before retrofit can cite it).

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Land consolidated rule-file diff at `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65 (current pin head). Read first:
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Enforcement clause"` (lines 57-65; input-pin SHA `<at dispatch>`)
   > - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (cross-link for Level-2 binding axis)
   > - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 layer distinction)
   > - S89 W-6 R2 workshop verdict text (workshop file `s89-w6-level2-binding-inheritance.md §Wrap-Up` per partition manifest)
   > - `computations/_shared/_cross_pillar_bridge_audit.py` head SHA `<at dispatch>`
   >
   > Methodology: extend the Enforcement clause to introduce a deferred-pending intermediate verdict-class with TWO sub-class tags between Level-2-binding (PASS-eligible) and Level-2-non-binding (INELIGIBLE):
   >
   > Append to §"Enforcement clause":
   >
   > #### Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)
   >
   > Between Level-2-binding ELIGIBLE and Level-2-non-binding INELIGIBLE, the deferred-pending intermediate verdict-class admits TWO sub-class tags:
   >
   > - **`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`**: applied to registry entries whose Level-2 envelope is currently realized via a SCHEMATIC proxy or Casimir-bound argument (per the substrate-distance-2 pole), pending refinement by a FULL physical pipeline (e.g., L_max scan + Friedrich-Bär saturation; FULL BdG re-derivation). Calibration corpus instance: §VII.AV (FWD-C2 Pillar III/IV ↔ Pillar V; Casimir-bound proxy pending FULL BdG per CF-W5-3 / W-6 CF-2).
   > - **`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`**: applied to registry entries whose Level-2 envelope is symbolic-only (no numerical anchor yet), pending first extraction via L_max scan or analytic limit derivation. Calibration corpus instance: §VII.AU (FWD-C1 Pillar I-II; parameterized slope_A canonical pending L_max scan per CF-W5-6 / W-6 CF-3).
   >
   > Both sub-classes route to plan-freeze advisory (S2) rather than HARD-HALT (S1); they do NOT contribute to registry-PASS by themselves but reserve the §VII slot during the pending refinement / extraction. Status: SUGGESTION at K=1 (dual instances §VII.AV + §VII.AU); promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.
   >
   > Audit-script extension: extend `_cross_pillar_bridge_audit.py` with regex detectors:
   > - Pattern 1: `r'REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT'` (detects sub-class tag in §VII entry text)
   > - Pattern 2: `r'REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION'` (detects sub-class tag in §VII entry text)
   > When either pattern matches, audit records the entry as `deferred_pending=True` with sub-class assignment; emits S2 advisory; does NOT route to plan-freeze HARD-HALT.
   >
   > Output files:
   > - `.claude/rules/cross-pillar-bridge-anatomy.md` (extended §"Enforcement clause" with deferred-pending sub-section ≥ 30 lines)
   > - `computations/_shared/_cross_pillar_bridge_audit.py` (extended with regex detectors)
   > - `computations/_shared/s90_w1_deferred_pending_audit_test.py` (self-test against §VII.AV + §VII.AU as positive instances after CF-63 W6 lands them)
   > - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (append corpus row #3 = deferred-pending dual instances)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt` with dual-SHA closure (`content_sha256` over rule-file diff + `audit_sha256` over input-pin map)
   >
   > Substrate framing: deferred-pending IS a methodology-layer F-image of substrate-IS partial-information; the substrate's Level-2-binding admissibility predicate IS a structural identity, but its empirical realization can be SCHEMATIC (proxy) or symbolic-only (first-extraction-pending). The two sub-classes preserve the F-image fidelity while admitting structurally-intermediate realization.

7. **Machinery pin (PRDR)**:
   - `cross-pillar-bridge-anatomy.md §"Enforcement clause"` head SHA: `<pinned at dispatch>`
   - `substrate-first-canonical-sourcing.md §(iv)` cross-link SHA: `<at dispatch>`
   - `cross-pillar-bridge-corpus.md §1` head SHA: `<at dispatch>`
   - W-6 R2 workshop verdict text SHA: `<at dispatch>`
   - `_cross_pillar_bridge_audit.py` head SHA: `<at dispatch>`
   - Regex patterns pinned as above
   - K-counter pin: SUGGESTION-K=1 (advances to MANDATORY at K=3)
   - Calibration instances pinned: §VII.AV (PENDING-PROXY-REFINEMENT) + §VII.AU (PENDING-FIRST-EXTRACTION)
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`
   - Dual-SHA closure: `content_sha256` over rule-file diff text + `audit_sha256` over input-pin map per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`

8. **Expected output 4-tuple**: `(value=deferred-pending-sub-class-landed-with-2-sub-classes + audit-extension + K-1-corpus-dual, scheme=cross-pillar-bridge-anatomy-enforcement-clause-extension, convention=deferred-pending-proxy-refinement-first-extraction, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) deferred-pending sub-section appended to Enforcement clause (≥ 30 substantive lines); (ii) 2 sub-class tags defined; (iii) audit-script extension lands with 2 regex detectors; (iv) corpus row #3 appended; (v) allowlist + instances rows appended; (vi) dual-SHA closure emitted.
   - **FAIL** iff any of (i)-(vi) absent.

10. **Substitution chain** (N/A — `[AUDIT]` rule-file diff + detector landing).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** closes the structurally-intermediate Level-2-realization pathway by construction; future §VII entries citing SCHEMATIC proxy or symbolic-only Level-2 envelope can be properly classified at the rule level + audit level.
    - **FAIL** signals the deferred-pending class collapses Level-2-binding distinction; W6 CF-63 (mack writes §VII.AV + §VII.AU) cannot proceed structurally — the rule must exist as routing target.

12. **Effort estimate**: 0.5 we.

13. **Substrate-framing reminder**: deferred-pending IS the methodology F-image of substrate-IS partial information about Level-2 envelope realization; the substrate's binding-axis structural identity is preserved while admitting SCHEMATIC proxy or symbolic-only intermediate realizations. Direction: substrate-IS binding-axis predicate → emergent Level-2 envelope realization (which can be SCHEMATIC or FULL); deferred-pending tags the intermediate state.

---

## §W1-15. CF-15 — `S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED`

1. **Gate ID**: `S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED` (gen §6 W-6 atomic deliverables sub-item; W-6 CF-4)
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Retrofitting §W5-6 convention tag from `lizzi-fwd-c1-retry-parameterized-slope-A-canonical` to `...-TEMPLATE-INHERITED-FROM-W-5` + emitting SUPERSEDES-tagged corrective canonical line per Option A protocol + §(f) disclosure paragraph + §VII.AU sub-class re-tag to PENDING-FIRST-EXTRACTION routes §VII.AU correctly into the deferred-pending taxonomy from CF-14.
6. **Method**:

   **Note**: CF-15 REQUIRES CF-14 PASS (deferred-pending rule-file enforcement-clause must define `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` sub-class tag as routing target before CF-15 retrofits §VII.AU to it).

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Retrofit §W5-6 convention tag with SUPERSEDES-tagged corrective canonical line. Read first:
   > - §W5-6 producing script `computations/session-89/s89_w5_a30_<full-name-at-dispatch>.py` line 1513 (input-pin SHA `<at dispatch>`)
   > - §W5-6 original verdict line in `computations/session-89/s89_gate_verdicts.txt` (locate via grep `S89-W5-6` or `s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical`)
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Enforcement clause"` POST-CF-14 (must include deferred-pending sub-classes)
   > - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (3-class taxonomy POST-CF-9 if landed; else K=4 baseline)
   > - `.claude/rules/v3-closure-recovery.md §"Option A — sig_5 remediation pathway"` (supersedes tag protocol)
   > - `sessions/permanent-results-registry.md §VII.AU` current text (DEFERRED-PENDING REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION per CF-63 W6 landing)
   >
   > Methodology: emit a corrective canonical verdict line at `computations/session-90/s90_gate_verdicts.txt` with:
   > - GATE_ID: `S89-W5-6-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL-RETROFIT` (retrofit-tagged)
   > - composite verdict: same as §W5-6 original (PASS / INFO per §W5-6 outcome — DO NOT alter the scientific verdict)
   > - value: same as original
   > - scheme: same as original
   > - **convention**: `lizzi-fwd-c1-retry-parameterized-slope-A-canonical-TEMPLATE-INHERITED-FROM-W-5` (NEW suffix)
   > - L_max: same as original
   > - audit_sha256: NEW (recomputed under new convention tag)
   > - **supersedes**: `<full-64-char-original-audit_sha256>` per Option A protocol
   >
   > Update §W5-6 working-paper §(f) with disclosure paragraph: "S90 W-6 CF-15 retrofit per `cross-pillar-bridge-anatomy.md §"Enforcement clause"` deferred-pending sub-class taxonomy (S90 landing): convention tag suffix `-TEMPLATE-INHERITED-FROM-W-5` indicates the substrate-IS Element-1 specification template inherits from §VII.AF.1.OP-PROJ W-5 calibration baseline; routes §VII.AU into `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` sub-class. Substrate physics intact; only methodology disclosure tag updated."
   >
   > Update `sessions/permanent-results-registry.md §VII.AU` text: re-tag with sub-class `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (post-CF-14 deferred-pending taxonomy) + cross-link to the CF-15 retrofit + cross-link to CF-65 `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS` (W-6 CF-3) as the FIRST-EXTRACTION gate.
   >
   > Output files:
   > - `computations/session-90/s90_gate_verdicts.txt` (corrective canonical line appended with SUPERSEDES tag)
   > - §W5-6 WP §(f) amendment (preserve verdict integrity; insert disclosure paragraph)
   > - `permanent-results-registry.md §VII.AU` text update with sub-class tag
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   >
   > Substrate framing: TEMPLATE-INHERITED convention tag IS the methodology F-image of substrate-IS Element-1 inheritance from W-5 calibration baseline; the substrate-IS observable's specification template is preserved across FWD-C1 + W-5; the suffix discloses this lineage at the convention-tag layer.

7. **Machinery pin (PRDR)**:
   - §W5-6 producing script line 1513 SHA: `<pinned at dispatch>`
   - §W5-6 original verdict line audit_sha256 (full 64-char): `<grep-extracted at dispatch>`
   - `cross-pillar-bridge-anatomy.md §"Enforcement clause"` POST-CF-14 SHA: `<at dispatch, post-CF-14>`
   - `substrate-first-canonical-sourcing.md §(iv)` POST-CF-9 SHA: `<at dispatch>`
   - `v3-closure-recovery.md §"Option A"` SHA: `<at dispatch>`
   - `permanent-results-registry.md §VII.AU` post-CF-63 SHA: `<at dispatch>`
   - SUPERSEDES tag form pin: full 64-char original audit_sha256
   - Convention-tag suffix pin: `-TEMPLATE-INHERITED-FROM-W-5`
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=corrective-line-with-supersedes-AND-WP-disclosure-AND-vii-au-re-tag-landed, scheme=fwd-c1-template-inherited-retrofit, convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical-TEMPLATE-INHERITED-FROM-W-5, L_max=10)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) corrective canonical line appended with SUPERSEDES tag carrying full-64-char original audit_sha256; (ii) §W5-6 WP §(f) disclosure paragraph appended; (iii) §VII.AU registry text re-tagged with `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` sub-class; (iv) allowlist + instances rows appended.
   - **FAIL** iff SUPERSEDES tag truncated to <64 chars OR WP §(f) disclosure absent OR §VII.AU re-tag absent.
   - **INFO** iff CF-14 has not landed PASS at dispatch (PRE-REG-INC blocked on deferred-pending sub-class definition).

10. **Substitution chain** (N/A — `[AUDIT]` Option A protocol enforcement; convention-tag suffix application).

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** correctly applies Option A SUPERSEDES protocol to the §W5-6 convention-tag retrofit; §VII.AU routed into the deferred-pending taxonomy from CF-14; verdict permanence preserved.
    - **FAIL** signals SUPERSEDES protocol violated (truncated SHA, or missing disclosure); audit trail incomplete.

12. **Effort estimate**: 0.25 we.

13. **Substrate-framing reminder**: TEMPLATE-INHERITED IS substrate-IS Element-1 inheritance from W-5 calibration baseline made visible at the convention-tag layer; the substrate's structural template is preserved across the FWD-C1 candidate. Direction: substrate-IS template (W-5 §VII.AF.1.OP-PROJ baseline) → emergent FWD-C1 §VII.AU candidate inheriting Element-1 specification.

---

## §W1-16. CF-16 — `S90-PROVISIONAL-K3-TAGGING-VII-AR`

1. **Gate ID**: `S90-PROVISIONAL-K3-TAGGING-VII-AR` (CONNES V.4)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write (mack-cosmic-bridge sole-writer for registry-text per `feedback_mack-bridge-role.md`)
5. **Hypothesis**: Editing `permanent-results-registry.md §VII.AR` line 16969 to tag K=3 advancement as "PROVISIONAL pending CF-W5-2" + conditional re-audit text per cross-tier confirmation outcome carries the cross-tier dependency forward in registry text.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write; mack writer for registry-text):

   > Edit `sessions/permanent-results-registry.md §VII.AR` line 16969 to tag K=3 advancement as PROVISIONAL. Read first:
   > - `sessions/permanent-results-registry.md §VII.AR` block (line 16969 plus surrounding context; input-pin SHA `<at dispatch>`)
   > - `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (mixed-status interpretation: MANDATORY-at-cohomology-class-distinct-K=3, pole-distinct K=3 pending)
   > - CF-W5-2 (CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`) plan-block text for cross-tier confirmation predicate
   >
   > Methodology: append PROVISIONAL tag at §VII.AR line 16969 such that the registry text reads:
   >
   > "K-counter status: MANDATORY-at-cohomology-class-distinct-K=3 (S88 W-22 W7a-74 V.5 / B.55 promotion); **PROVISIONAL pending CF-W5-2 cross-tier confirmation outcome** (CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`). Conditional re-audit:
   > - PASS-A (Spearman ≥ 0.9, SCHEMATIC faithful proxy): §VII.AR LEVEL-DRESSED WEAKENED; K=3 advancement RETAINED as MANDATORY.
   > - PASS-B (Spearman < 0.9, rankings DIFFER): §VII.AR LEVEL-DRESSED STRENGTHENED; K=3 advancement RETAINED as MANDATORY-with-strengthened-evidence.
   > - INFO/FAIL on CF-W5-2: K=3 advancement reverts to PROVISIONAL-pending-FULL-tier-N≥4 (advisory until reinforced)."
   >
   > Output files:
   > - `sessions/permanent-results-registry.md §VII.AR` (line 16969 updated)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: PROVISIONAL tagging IS the methodology F-image of substrate-IS conditional cohomology-class advancement; the substrate's K=3 cohomology-class-distinct advancement is structurally established, but its empirical reinforcement under FULL-tier evaluation remains pending (cross-tier confirmation in CF-W5-2). The tag makes this conditional state explicit in registry text.

7. **Machinery pin (PRDR)**:
   - `permanent-results-registry.md §VII.AR` line 16969 SHA: `<pinned at dispatch>`
   - `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` SHA: `<at dispatch>`
   - CF-W5-2 (CF-60) plan-block text SHA: `<at dispatch>`
   - PROVISIONAL tag text pinned as above (3-branch conditional re-audit clause)
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=vii-ar-line-16969-tagged-PROVISIONAL-with-3-branch-conditional-re-audit, scheme=vii-ar-provisional-k3-tag, convention=mixed-status-interpretation-with-cf-w5-2-conditional, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) §VII.AR line 16969 carries PROVISIONAL tag; (ii) 3-branch conditional re-audit clause structurally precise; (iii) cross-link to CF-W5-2 / CF-60 present; (iv) allowlist + instances rows appended.
   - **FAIL** iff any of (i)-(iv) absent OR conditional language structurally imprecise.

10. **Substitution chain** (for `[VERIFY]` — conditional re-audit predicate structural precision):

    - Step 1 (Definition): `K3_status(§VII.AR) := f(cross_tier_confirmation_outcome)` where outcome ∈ {PASS-A, PASS-B, INFO/FAIL}.
    - Step 2 (Substitution): PROVISIONAL-pending-CF-W5-2 := K3_status awaiting CF-60 outcome.
    - Step 3 (Simplify): conditional branches enumerated as above (PASS-A retains K=3 + WEAKENED; PASS-B retains K=3 + STRENGTHENED; INFO/FAIL reverts to PROVISIONAL-pending-FULL-tier-N≥4).
    - Step 4 (Direction): registry text encodes the conditional explicitly; downstream consumers cite K=3 with the PROVISIONAL qualifier until CF-60 dispatches.
    - Conclusion: provisional tag preserves K=3 advancement scope while flagging cross-tier dependency.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** carries the cross-tier confirmation dependency forward in registry text; future readers of §VII.AR cannot cite K=3 as unconditional pending CF-60 outcome.
    - **FAIL** signals the conditional language is structurally imprecise; downstream consumers may cite K=3 unconditionally.

12. **Effort estimate**: 0.2 we.

13. **Substrate-framing reminder**: PROVISIONAL tag IS the methodology F-image of substrate-IS conditional cohomology-class advancement; the substrate's structural K=3 advancement is decided by cross-tier-distinct calibration instances, but the empirical reinforcement at FULL-tier remains conditional on the laboratory-IN evaluator (CF-W5-2 W7a-74 PRIMARY evaluator output). The tag carries this conditionality explicitly.

---

## §W1-17. CF-17 — `S90-VII-AH-STAGE-2-ORTHOGONALITY-K2-RULE-UPDATE`

1. **Gate ID**: `S90-VII-AH-STAGE-2-ORTHOGONALITY-K2-RULE-UPDATE` (CF-W4-7-ORTHOGONALITY-K2)
2. **Trigger**: `[VERIFY]`
3. **Classification**: METHODOLOGY
4. **Agent type**: gen-physicist orchestrator-direct-write
5. **Hypothesis**: Updating `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` K-counter table to reflect K=1 → K=2 advancement via §W4-7 §VII.AH PASS at structural ceiling + reserving K=3 row makes the substrate-input-orthogonality K-counter advance per `pru-class-corpus.md §15-§16` sub-rows.
6. **Method**:

   Dispatch prompt (gen-physicist orchestrator-direct-write):

   > Update K-counter table at `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`. Read first:
   > - `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` (full sub-section, input-pin SHA `<at dispatch>`)
   > - §W4-7 audit `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` (§VII.AH PASS 8/8 + JOINT (c)+(d) + substrate-input-orthogonality at structural ceiling)
   > - `sessions/framework/registry/pru-class-corpus.md §15-§16` (sub-rows for substrate-input-orthogonality calibration corpus)
   > - S88 W-23 V.1 / B.56 source text for original K=1 calibration
   >
   > Methodology: locate K-counter table in `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`. Update from:
   > - Pre-S90: K=1 (W7c-167 obs1 PASS-AND with substrate-input-overlap caveat; shared `s87_w7_ic_per_class_verify.npz` SHA-256 `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f`)
   >
   > Post-S90 (this update):
   > - K=1 (S88 W7c-167; substrate-input-overlap caveat) [retained]
   > - K=2 (S89 W4-7 §VII.AH at structural ceiling; FIRST INSTANCE WITHOUT substrate-input-overlap caveat) — NEW row
   > - K=3 reserved
   >
   > Append K=2 row to the K-counter table with:
   > - Source: S89 W4-7 §VII.AH PASS 8/8
   > - Audit SHA: `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a`
   > - JOINT clauses PASS-AND verified: (c) JOINT + (d) JOINT
   > - Substrate-input-orthogonality status: structural ceiling (no overlap caveat needed at structural layer; first framework cross-axis joint theorem to STAGE-3-PERMANENT eligibility)
   > - K-counter status post-S90: SUGGESTION at K=2 (promotes to MANDATORY at K=3)
   >
   > Cross-link to `sessions/framework/registry/pru-class-corpus.md §15-§16` Corpus row update (mack writer per `feedback_mack-bridge-role.md`).
   >
   > Output files:
   > - `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` (K-counter table updated with K=2 row + K=3 reserved row)
   > - `sessions/framework/registry/pru-class-corpus.md §15-§16` (cross-link sub-row update)
   > - `sessions/framework/registry/methodology-wave-instances.md` rationale entry
   > - `.claude/rules/methodology-wave-allowlist.md` row appended
   > - Verdict line at `computations/session-90/s90_gate_verdicts.txt`
   >
   > Substrate framing: substrate-input-orthogonality K-counter advancement IS the methodology F-image of substrate-IS structural orthogonality at the cross-axis joint-theorem layer; §VII.AH PASS at structural ceiling without overlap caveat IS the substrate's own structural establishment of orthogonality across distinct substrate inputs. K=2 advancement makes this F-image accumulation visible.

7. **Machinery pin (PRDR)**:
   - `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` head SHA: `<pinned at dispatch>`
   - §W4-7 audit SHA: `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a`
   - `pru-class-corpus.md §15-§16` head SHA: `<at dispatch>`
   - S88 W-23 V.1 / B.56 source text SHA: `<at dispatch>`
   - K-counter advancement pin: K=1 → K=2 (reserved K=3)
   - K-counter status pin: SUGGESTION at K=2 (advances to MANDATORY at K=3)
   - `verdict_source`: `computations/session-90/s90_gate_verdicts.txt`

8. **Expected output 4-tuple**: `(value=k-counter-K-1-to-K-2-advancement-AND-K-3-reserved + pru-corpus-cross-link-update, scheme=joint-theorem-promotion-substrate-input-orthogonality-K-counter-update, convention=k-2-structural-ceiling-without-overlap-caveat, L_max=N/A)`

9. **PASS/FAIL/INFO threshold + tolerance**:
   - **PASS** iff (i) K-counter table updated with K=2 row pinned to §W4-7 audit SHA; (ii) K=3 reserved row appended; (iii) pru-class-corpus.md §15-§16 cross-link update lands; (iv) allowlist + instances rows appended.
   - **FAIL** iff K-counter table not updated OR §W4-7 SHA mis-pinned OR K=3 reserved row absent.

10. **Substitution chain** (for `[VERIFY]` — K-counter advancement):

    - Step 1 (Definition): `K_substrate_input_orthogonality := count of distinct calibration-corpus instances satisfying the substrate-input-orthogonality predicate at structural ceiling`.
    - Step 2 (Substitution): Pre-S90 corpus = {W7c-167 obs1 with overlap caveat}; |corpus_pre_S90| = 1. S89 W4-7 §VII.AH PASS 8/8 + JOINT (c)+(d) + structural ceiling (no overlap caveat) ⇒ new instance.
    - Step 3 (Simplify): K_substrate_input_orthogonality = 1 + 1 = 2.
    - Step 4 (Direction): K=2 ≥ K=2 SUGGESTION promotion threshold; status remains SUGGESTION pending K=3.
    - Conclusion: K-counter table reflects K=2 advancement; K=3 row reserved for next-instance landing.

11. **What PASSES/FAILS mean for solution space**:
    - **PASS** advances the substrate-input-orthogonality K-counter to K=2, making it visible across rule + corpus; W2 CF-20 (Stage-3-PERMANENT promotion of §VII.AH) can cite K=2 in its provenance.
    - **FAIL** signals K-counter table not advanced; downstream W2 CF-20 cannot cite K=2.

12. **Effort estimate**: 0.2 we.

13. **Substrate-framing reminder**: substrate-input-orthogonality at structural ceiling IS substrate-IS structural orthogonality at the cross-axis joint-theorem layer; §VII.AH PASS at structural ceiling without overlap caveat IS the substrate's own structural establishment. K=2 K-counter advancement is the methodology F-image accumulation; direction: substrate-IS structural orthogonality → emergent K-counter advancement at the rule-file layer.

---

## Wave 1 → Wave 2 Decision Point

W1 methodology rule-file extensions + audit-script enhancements MUST land PASS before the following W2 dispatches:

- **W1 CF-1 → W2 CF-23**: Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` audit-script extension must exist before mack reconciles §VII.AN registry text (mack reconciliation cites the audit-script's classification).
- **W1 CF-14 → W6 CF-63**: Deferred-pending rule-file enforcement-clause must define sub-class tags before mack writes §VII.AV + §VII.AU initial deferred-pending registrations (mack cites the rule's sub-classes).
- **W1 CF-2 → W3 / W4 corner-classification audits**: Extended `_corner_classification_audit.py` TARGET_SLOTS dict must be in place before W3 CF-49 / CF-51 / CF-53 reference §VII.U.2 4-corner rows.
- **W1 CF-8 → W2 CF-19**: Parse-tree expansion pre-registration rule must exist before mack lands SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (if the theorem cites state-history-label observables, the parse-tree expansion declaration is required at landing).
- **W1 CF-17 → W2 CF-20**: K=1 → K=2 substrate-input-orthogonality advancement must reflect in rule + corpus before W2 CF-20 STAGE-3-PERMANENT promotion gate cites K=2.
- **W1 CF-12 → W4 §VII.AQ Stage-2 plan-block screening**: PRU Class 8.7 Degenerate-Observable Pre-Flight must exist as rule + audit pattern before W4 §VII.AQ Stage-2 plan-block is screened.

W1 outputs are dispatch-independent at intra-wave level except for CF-2 → CF-5 + CF-6, CF-14 → CF-15. Other intra-wave items may execute in parallel under orchestrator-direct-write.

---

## Wave 1 Machinery-Enumeration Pin (§0.11)

Aggregate PRDR machinery pins across all 17 W1 gates:

| Pin axis | Gates | Pin value or `<at dispatch>` |
|:---------|:------|:-----------------------------|
| `_registry_landing_audit.py` head SHA | CF-1, CF-8 | `<at dispatch>` |
| `permanent-results-registry.md §VII.AN` block SHA | CF-1, W2 CF-23 paired | `<at dispatch>` |
| `permanent-results-registry.md §VII.U.2` block SHA | CF-2, CF-5, CF-6, CF-7 | `<at dispatch, post-W2-CF-25>` |
| `_corner_classification_audit.py` head / post-CF-2 SHA | CF-2 (head), CF-5/CF-6 (post-CF-2) | `2b96bf78<at dispatch>` |
| `_plan_staleness_audit.py` head SHA | CF-3 | `5f370299<at dispatch>` |
| `_w25_closing_paragraph_coherence_sweep_audit.py` head SHA | CF-4 | `16c2729c<at dispatch>` |
| `cross-pillar-bridge-anatomy.md` head SHA / per-section | CF-7, CF-13, CF-14 | `<at dispatch>` |
| `substrate-first-canonical-sourcing.md §(iv)` head SHA | CF-9, CF-15 | `<at dispatch>` |
| `_substrate_first_provenance_audit.py` head SHA | CF-9 | `<at dispatch>` |
| `epistemic-discipline.md §"Pre-Registration Completeness"` head SHA | CF-12 | `<at dispatch>` |
| `_pru_cardinality_audit.py` head SHA | CF-12 | `<at dispatch>` |
| `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` head SHA | CF-17 | `<at dispatch>` |
| `_cross_pillar_bridge_audit.py` head SHA | CF-14 | `<at dispatch>` |
| `registry-landing.md` head SHA | CF-8 | `<at dispatch>` |
| §W5-7 producing script SHA | CF-9, CF-10 | `<at dispatch>` (`s89_w5_a36_*.py`) |
| §W5-6 producing script SHA + verdict-line audit_sha256 | CF-15 | `<at dispatch>` (`s89_w5_a30_*.py`) |
| §W5-7 verdict line in s89_gate_verdicts.txt:101-103 SHA | CF-9 | `<at dispatch>` |
| §W4-7 audit SHA | CF-17 | `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` |
| §W1-1 verdict line SHA | CF-12 | `6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe` |
| W6-2 audit SHA | CF-1 | `9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f` |
| W7c emission #3 verdict SHA | CF-13 | `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d` |
| W6-3 cross-link SHA | CF-11 | `006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157` |
| 4 W6-3 audit SHAs | CF-11 | `1df983a9<at dispatch>` + `39937c8c<at dispatch>` + `4d2dfd87<at dispatch>` + `f9caf81a<at dispatch>` |
| W2 CF-25 verdict (cross-wave PASS prerequisite) | CF-2 | `<runtime, from computations/session-90/s90_gate_verdicts.txt>` |
| `cross-pillar-bridge-corpus.md §2` / §1 head SHA | CF-13 / CF-14 | `<at dispatch>` |
| `pru-class-corpus.md §15-§16` head SHA | CF-17 | `<at dispatch>` |
| `verdict_source` (uniform across all 17 gates) | all | `computations/session-90/s90_gate_verdicts.txt` |
| `methodology-wave-allowlist.md` append target | all | `.claude/rules/methodology-wave-allowlist.md` |
| `methodology-wave-instances.md` append target | all | `sessions/framework/registry/methodology-wave-instances.md` |

PRDR completeness check: every audit-script extension pins its head SHA at dispatch; every rule-file diff target pins its section SHA; every verdict-line citation pins its full 64-char audit_sha256; every detector regex pattern is pinned at the gate-block level; expected outputs for all 17 gates are artifact-existence predicates per `wave-classification.md §M1` (NOT numerical comparisons).

No PRU Class 8 free parameters detected. All 17 gates pass PRDR.

---

## Wave 1 Input-SHA Ledger

Catalog of all input files read by W1 gates with SHA pins. Files are sorted by section.

### Rule-file inputs

| File | Pinned at | Consumed by gates |
|:-----|:---------|:------------------|
| `.claude/rules/cross-pillar-bridge-anatomy.md` (full + §"Enforcement clause" + §"Algebra-axis orthogonality K-counter" + §"Per-Bulletin-per-pole" + §"Element 2 OE-form discipline") | `<at dispatch>` | CF-7, CF-13, CF-14, CF-16 |
| `.claude/rules/substrate-first-canonical-sourcing.md §(i)` + §(iv) | `<at dispatch>` | CF-1, CF-9, CF-15 |
| `.claude/rules/registry-landing.md` | `<at dispatch>` | CF-8 |
| `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` + §"Source Reconciliation" + §"Layer-Decomposition" | `<at dispatch>` | CF-12 |
| `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` + §"Stage 2" | `<at dispatch>` | CF-17 |
| `.claude/rules/regulator-pin-discipline.md` | `<at dispatch>` | CF-10 |
| `.claude/rules/v3-closure-recovery.md §"Option A — sig_5 remediation pathway"` | `<at dispatch>` | CF-15 |
| `.claude/rules/wave-classification.md §"Dispatch consequences"` + §"Dual-SHA closure for METHODOLOGY-class" | all 17 | dispatch-protocol input |
| `.claude/rules/methodology-wave-allowlist.md` (append target) | `<at dispatch>` | all 17 |
| `.claude/rules/mechanical-closure-discipline.md` §"Layer-separability carve-out" | `<at dispatch>` | CF-9, CF-12 (cross-link only) |

### Audit-script inputs

| File | Pinned at | Consumed by gates |
|:-----|:---------|:------------------|
| `computations/_shared/_registry_landing_audit.py` | `<at dispatch>` | CF-1, CF-8 |
| `computations/_shared/_corner_classification_audit.py` | `2b96bf78<at dispatch>` (W6-6 baseline; post-CF-2 for CF-5/CF-6) | CF-2, CF-5, CF-6 |
| `computations/_shared/_plan_staleness_audit.py` | `5f370299<at dispatch>` (W6-6 baseline) | CF-3 |
| `computations/_shared/_w25_closing_paragraph_coherence_sweep_audit.py` | `16c2729c<at dispatch>` | CF-4 |
| `computations/_shared/_substrate_first_provenance_audit.py` | `<at dispatch>` | CF-9 |
| `computations/_shared/_pru_cardinality_audit.py` | `<at dispatch>` | CF-12 |
| `computations/_shared/_cross_pillar_bridge_audit.py` | `<at dispatch>` | CF-14 |
| 4 W6-3 audit scripts: `1df983a9*`, `39937c8c*`, `4d2dfd87*`, `f9caf81a*` | `<at dispatch>` each | CF-11 |

### Registry / corpus inputs

| File | Section / Line | Consumed by gates |
|:-----|:--------------|:------------------|
| `sessions/permanent-results-registry.md §VII.AN` block | `<at dispatch>` | CF-1 |
| `sessions/permanent-results-registry.md §VII.U.2` block lines 12927-13058 (clause (e) line 12995) | `<at dispatch, post-W2-CF-25>` | CF-2, CF-5, CF-6, CF-7, CF-8 |
| `sessions/permanent-results-registry.md §VII.U.1` line 12960 (α_s_canonical instance #2) | `<at dispatch>` | CF-7 |
| `sessions/permanent-results-registry.md §VII.AR` line 16969 | `<at dispatch>` | CF-16 |
| `sessions/permanent-results-registry.md §VII.AS` line 17000 (A.30 anchor) | `<at dispatch>` | CF-3 (cross-wave-anchor canonical) |
| `sessions/permanent-results-registry.md §VII.AU` post-CF-63 | `<at dispatch>` | CF-15 |
| `sessions/permanent-results-registry.md §VII.K-DUAL.LEVEL-DRESSED` lines 4293-4297 | `<at dispatch>` | CF-5 |
| `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 layer distinction) | `<at dispatch>` | CF-14 |
| `sessions/framework/registry/cross-pillar-bridge-corpus.md §2` (Element-2 OE-form corpus) | `<at dispatch>` | CF-13 |
| `sessions/framework/registry/pru-class-corpus.md §15-§16` (substrate-input-orthogonality calibration) | `<at dispatch>` | CF-17 |
| `sessions/framework/registry/pru-class-corpus.md` (Class 8.7 new section target) | `<at dispatch>` | CF-12 |
| `sessions/framework/registry/methodology-wave-instances.md` (append target) | `<at dispatch>` | all 17 |
| `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` (line 14690-14722 baseline) | `<at dispatch>` | CF-13 (reference only) |

### Verdict-line inputs

| Verdict source | audit_sha256 (full 64-char) | Consumed by gates |
|:---------------|:----------------------------|:------------------|
| §W4-7 audit | `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` | CF-17 |
| §W1-1 verdict | `6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe` | CF-12 |
| W6-2 audit | `9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f` | CF-1 |
| W7c emission #3 (latest non-superseded) | `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d` | CF-13 |
| W6-3 cross-link | `006f02107827fd71b8ff7d2902d93d30b0c4d25ddc6539b3226fa3936495f157` | CF-11 |
| §W5-7 verdict + companion rows in s89_gate_verdicts.txt:101-103 | `<at dispatch>` | CF-9 |
| §W5-6 verdict audit_sha256 (full 64-char for SUPERSEDES tag) | `<at dispatch via grep>` | CF-15 |
| W2 CF-25 verdict (cross-wave PASS prerequisite for CF-2) | `<runtime from computations/session-90/s90_gate_verdicts.txt>` | CF-2 |
| CF-14 verdict (intra-wave PASS prerequisite for CF-15) | `<runtime>` | CF-15 |
| CF-2 verdict (intra-wave PASS prerequisite for CF-5, CF-6) | `<runtime>` | CF-5, CF-6 |

### Workshop-source inputs

| Workshop / Synthesis source | Consumed by gates |
|:----------------------------|:------------------|
| `sessions/archive/session-89/session-89-gen-physicist-synthesis.md §6` | all 17 (closeout-solo dispatch-dependency-ordered table) |
| `sessions/archive/session-89/session-89-connes-synthesis.md §V.3 + §V.4 + §V.5` | CF-9, CF-10, CF-16 |
| `sessions/archive/session-89/session-89-lizzi-synthesis.md §V.1` | CF-11 |
| `sessions/archive/session-89/session-89-phonon-first-synthesis.md §V.4 + §V.7` | CF-12, CF-13 |
| `sessions/archive/session-89/workshops/s89-w3-vii-u-2-corner-classification.md` (CF-LZ-2/3/5; CF-R1-2/3) | CF-3, CF-5, CF-6, CF-7, CF-8 |
| `sessions/archive/session-89/workshops/s89-w4-vii-aq-mellin-lmax-saturation.md` (CF-W4-7 source) | CF-17 (via §VII.AH §W4-7 PASS provenance) |
| `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md` (W-5 CF-3 / CF-4 source) | CF-15 (via FWD-C1 / §VII.AU substrate-physics intact note) |
| `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (W-6 R2 verdict text) | CF-14 |

---

## End of Session 90 Plan — Wave 1

All 17 gate blocks complete with full 13-field specifications. METHODOLOGY-class strict-conjunction M1∧M2∧M3∧M4 satisfied at plan-freeze. Allowlist + instances row appends pending plan-freeze SHA computation per `methodology-wave-allowlist.md §"Edit discipline"` rules (3-column row in allowlist; rationale prose in instances).

Total wave effort estimate: ~4.8 wave-equivalents (gen-physicist orchestrator-direct-write); see per-gate effort tables in §W1-1 through §W1-17.

Dispatch consequences: per `wave-classification.md §"Dispatch consequences"`, all 17 gates dispatch via orchestrator-direct-write (NOT `/rclab-coordinate` compute-mode). Dual-SHA closure per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`: `content_sha256` over rule-file diff text + `audit_sha256` over input-pin map. Canonical verdict-file path: `computations/session-90/s90_gate_verdicts.txt` (per `gate-verdicts.md §"Canonical Verdict-File Path"`).
