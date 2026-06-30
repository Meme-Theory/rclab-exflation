# Session 87 Plan — Wave 11 Meta (Methodology-Class Follow-Ups)

**Wave-class**: METHODOLOGY (M1 ∧ M2 ∧ M3 ∧ M4 satisfied per `.claude/rules/wave-classification.md`).

**Wave-owner**: orchestrator (per `.claude/rules/wave-classification.md` §"Dispatch consequences": "METHODOLOGY-class waves SKIP /rclab-coordinate compute-mode. The orchestrator writes the rule-file edits directly, treating each wave-item as analogous to the team-lead synthesis section.")

**Authorization context**: User-authorized mid-session in response to orchestrator's W11 wave-synthesis decision-point #3 surface. Three rule-file updates carry-forwarded from W11 substantive findings:
- METH-1: cross-pillar-bridge-anatomy.md K-counter advancement (W11-5 = FWD-C3 instance #2)
- METH-2: math-scripts.md plan-authorship lesson on D_K block-diagonality (W11-2 + W11-3 dual calibration corpus)
- METH-3: epistemic-discipline.md PRU Class 8.2 corpus closure (W11-1 V_4 supersession event)

**M1-M4 satisfaction (per `.claude/rules/wave-classification.md`)**:
- M1 (PASS predicate type): each gate's PASS predicate is `(rule-file F exists at target path) AND (F contains the appended sub-section §S) AND (substantive_line_count(§S) >= 5) AND (content_sha256(§S diff) matches input-pin-map-derived hash)`. Artifact-existence-with-substantive-content, NOT numerical comparison. ✓
- M2 (Producing-operation type): orchestrator-direct `Edit` operation on `.claude/rules/*.md` files. NO `.py` scripts producing numerical comparisons. ✓
- M3 (Source-of-truth type): all 3 gates derive from verbatim sub-extracts of W11 closed gate-blocks (W11-1, W11-2, W11-3, W11-5 verdict lines + working-paper sections). NO new derivation; the W11 results are the upstream substrate-physics workshop. ✓
- M4 (Allowlist membership): the 3 gate-IDs are appended to `.claude/rules/methodology-wave-allowlist.md` in the same dispatch as the rule-file edits, per orchestrator-only-edit discipline. ✓

---

## §METH-1. S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE

**Source**: S87 W11-5 verdict (FAIL composite, ratio_mismatch=1.029, REGISTRY-FAIL per cross-pillar-bridge-anatomy.md §"Registry-PASS criterion") → calibration corpus K-counter advancement K=1→2 toward MANDATORY at K=3.

**Trigger**: `[VERIFY]` — verify rule-file edit lands the W11-5 instance #2 row at the correct table location with K-counter updates throughout.

**Classification**: METHODOLOGY (per `.claude/rules/wave-classification.md` M1-M4 satisfaction declared above).

**Hypothesis**: cross-pillar-bridge-anatomy.md `Forward template-adoption (calibration-corpus tracking)` sub-section is updated in-place (orchestrator-only edit) to record W11-5 as instance #2 of the calibration corpus (FWD-C3 = Pillar IV ↔ Pillar V; substrate cocycles ↔ 3He-B BdG-undoubled spectral-excess at polycritical pressure; REGISTRY-FAIL Level-3 violates Level-2). K-counter advances from K=1 to K=2 in 3 locations: header line 100, table row 2 line 107, narrative line 110. Calibration-corpus tracking instance #2 line 159 replaces the SUGGESTED placeholder with the actual W11-5 entry.

**Pass/fail/INFO threshold**:
- PASS: rule-file edit on disk AND grep `K=2` returns 3+ hits in §"Forward template-adoption" sub-section AND grep `W11-5` returns 1+ hit in calibration-corpus tracking line 159 AND grep `FWD-C3` returns 1+ hit in instance #2 row.
- FAIL: any of the 3 K-counter locations remains at K=1, OR W11-5 entry absent from line 159, OR FWD-C3 missing from row 2.
- Tolerance rule: THEOREM (artifact-existence + content-grep equality; integer-counted occurrences).

**Machinery pin**:
- Target file: `.claude/rules/cross-pillar-bridge-anatomy.md`
- Edit operation: 4 distinct Edit calls (or 1 MultiEdit) updating: line 100 header K=1→K=2; lines 104-108 table row 2 fill; line 110 narrative K=1→K=2; lines 156-160 calibration-corpus tracking instance #2 fill.
- W-12 / W-5 source preservation: existing instance #1 row (S86 W-5) MUST remain unchanged.
- N_eval: N/A (no compute, artifact-existence test).
- L_max: N/A.
- random_seed: N/A.
- GPU path: N/A.

**Input SHA-256 pins**:
- `.claude/rules/cross-pillar-bridge-anatomy.md` pre-edit content (state at orchestrator-direct-write time).
- `computations/s87_gate_verdicts.txt` line 292 (W11-5 verdict line: `S87-3HEB-EXCESS-INHERITANCE-COMPARISON: FAIL -- value=1.029166e+00 ... audit_sha256=e1aef7ce0deaed2d... content_sha256=9c23976f1a02b3d1...`)
- `sessions/archive/session-87/session-87-results-workingpaper.md` §W11-5 (lines 9090-9275) for the cross-pillar-bridge-anatomy 5-element + 3-level ladder declaration.

**Expected output**:
- Rule-file diff: K-counter advancement at 3 locations + W11-5 instance #2 row + W11-5 calibration-corpus tracking entry.
- Verdict line: `S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE: PASS -- value='K_advanced_1_to_2;instance_2=W11-5_FWD-C3_REGISTRY-FAIL_Tier3_violates_Tier2_by_21x;K_promotion_threshold=3;status_remains_SUGGESTION' scheme=orchestrator-direct-rule-file-edit convention=cross-pillar-bridge-anatomy-K-counter-update L_max=N/A audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`

**Substitution chain (THEOREM artifact-existence)**:
```
Step 1: pre-edit cross-pillar-bridge-anatomy.md state contains K=1 in 3 locations + (—,—,(awaits...)) in row 2 + SUGGESTED placeholder in instance #2.
Step 2: orchestrator Edit operations replace K=1 → K=2 + fill row 2 + replace instance #2 placeholder with actual W11-5 entry.
Step 3: post-edit grep verifies K=2 returns 3+ hits AND W11-5 returns 1+ hit in instance #2 line AND FWD-C3 returns 1+ hit in row 2.
Step 4: PASS direction: all 3 grep checks pass → artifact-existence theorem holds.
        FAIL direction: any check fails → artifact missing or wrong location.
```

No directional inequality; THEOREM artifact-existence test.

**What PASS and FAIL mean**:
- PASS: cross-pillar-bridge-anatomy.md K-counter advanced; W11-5 properly recorded as calibration corpus instance #2; the rule moves from K=1 (1 instance, SUGGESTION) to K=2 (2 instances, still SUGGESTION until K=3 promotion). Future cross-pillar bridge candidates at S88+ continue to land under SUGGESTION discipline.
- FAIL: edit failed to land OR landed at wrong location OR failed to advance K-counter; the rule's calibration-corpus tracking is structurally inconsistent with W11-5's actual landing.

---

## §METH-2. S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON

**Source**: S87 W11-2 (CF-67) + W11-3 (CF-68) joint calibration corpus — both gates surfaced the same upstream plan-authorship gap: plan machinery pin assumed irrep CONSTRUCTION at L_max ≥ 10 is feasible, but recursive Casimir-projection cost is super-polynomial in dim(p,q). Both gates fixed in-session via different structural arguments (W11-2: Casimir-bound + cache cross-check; W11-3: Friedrich-Bär structural-saturation theorem).

**Trigger**: `[VERIFY]` — verify rule-file extension lands the new sub-section "D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check" in math-scripts.md §"Machinery-Feasibility Audit" with both calibration corpus instances cited.

**Classification**: METHODOLOGY.

**Hypothesis**: math-scripts.md §"Machinery-Feasibility Audit" gains a new sub-section that codifies the plan-authorship lesson: D_K is BLOCK-DIAGONAL by Peter-Weyl decomposition (NOT dense at any L_max); the operative computational cost is irrep CONSTRUCTION (recursive Casimir-projection on tensor products with the fundamental); cost is super-polynomial in dim(p,q). Plan authors MUST verify recursive Casimir-projection feasibility BEFORE pinning sparse-Lanczos at high L_max via cache cross-check + Casimir-bound argument (W11-2 precedent) OR Friedrich-Bär structural-saturation theorem (W11-3 precedent).

**Pass/fail/INFO threshold**:
- PASS: rule-file edit on disk AND grep `D_K Block-Diagonality` returns 1+ hit in math-scripts.md §"Machinery-Feasibility Audit" AND both `W11-2` and `W11-3` calibration corpus citations present in the new sub-section.
- FAIL: sub-section absent OR calibration corpus citations missing OR placed in wrong rule-file section.
- Tolerance rule: THEOREM (artifact-existence + content-grep equality).

**Machinery pin**:
- Target file: `.claude/rules/math-scripts.md`
- Edit operation: append new sub-section after §"Root-count heuristic severity-1 flag" within §"Machinery-Feasibility Audit"
- Existing §"Machinery-Feasibility Audit" content MUST remain unchanged.

**Input SHA-256 pins**:
- `.claude/rules/math-scripts.md` pre-edit content.
- `computations/s87_gate_verdicts.txt` lines 296, 298 (W11-3 PASS at value=4 + W11-2 INFO at pass_count=10/11).
- `sessions/archive/session-87/session-87-results-workingpaper.md` §W11-2 (lines 8907-9090) §"Operational L_max truncation (Casimir-bound argument)" subsection + §W11-3 (lines 8928-9093) §"Methodology — Structural-Saturation Theorem (replaces plan's sparse-Lanczos prescription)" subsection.

**Expected output**:
- Rule-file diff: new sub-section "D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check (S87 W11 calibration)" with Provenance / Lesson / Pre-check protocol / Calibration corpus.
- Verdict line: `S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON: PASS -- value='subsection_appended;calibration_corpus=W11-2_Casimir-bound+W11-3_FB-saturation;target=math-scripts.md_Machinery-Feasibility-Audit' scheme=orchestrator-direct-rule-file-edit convention=math-scripts-feasibility-pre-check-extension L_max=N/A audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`

**Substitution chain (THEOREM artifact-existence)**:
```
Step 1: pre-edit math-scripts.md §"Machinery-Feasibility Audit" contains GPU pins / Compute-time pins / Numerical-precision pins + Root-count heuristic severity-1 flag.
Step 2: orchestrator Edit operation appends new sub-section "D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check" after Root-count subsection.
Step 3: post-edit grep verifies new sub-section header + W11-2 + W11-3 citations present.
Step 4: PASS direction: all checks pass; rule-file extension lands.
        FAIL direction: missing or wrong location.
```

**What PASS and FAIL mean**:
- PASS: future plan authors have explicit guidance (with W11-2 + W11-3 calibration corpus) to verify recursive Casimir-projection feasibility BEFORE pinning sparse-Lanczos at high L_max; closes the upstream plan-authorship gap surfaced twice in W11.
- FAIL: rule-file extension not landed; the W11-2 + W11-3 lesson remains undocumented and the gap persists in S88+ plan authorship.

---

## §METH-3. S87-METH-PRU-CLASS-8-2-CORPUS-CLOSURE

**Source**: S87 W11-1 (CF-66) verdict (FAIL composite, max_dev=1.16; supersedes pre-registered S87-MONODROMY-Z4-LANDING per PRU Class 8.2 calibration; CC2 V_4 vs Z_4 element-order mismatch [1,2,2,2] vs [1,2,4,4] confirmed) → closes Class 8.2 calibration corpus instance #1 with empirical confirmation.

**Trigger**: `[VERIFY]` — verify rule-file edit appends W11-1 V_4 supersession-event as Class 8.2 calibration corpus closure entry.

**Classification**: METHODOLOGY.

**Hypothesis**: epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension" Class 8.2 calibration corpus (currently a single S86 W-12 diagnosis entry) gains a closure bullet recording the W11-1 empirical confirmation: V_4 PARALLELOGRAM IDENTITY tested at substrate level (max_dev=1.16 ≫ 1e-9 FAIL ceiling); both V_4 (under natural Cartan-toral character) and Z_4 (independently via element-order mismatch) FAIL. The W-12 candidate finding ("Z_4 or similar" rubric admitted V_4) is now tested-and-confirmed at substrate level — instance #1 closes.

**Pass/fail/INFO threshold**:
- PASS: rule-file edit on disk AND grep `S87 W11-1` and `V_4 supersession` and `element-order` present in §"Pre-Registration Completeness" Class 8.2 calibration corpus subsection.
- FAIL: sub-section not extended OR W11-1 entry missing OR placed in wrong taxonomy class (e.g., Class 8.0 instead of 8.2).
- Tolerance rule: THEOREM (artifact-existence + content-grep equality).

**Machinery pin**:
- Target file: `.claude/rules/epistemic-discipline.md`
- Edit operation: append closure bullet to existing §"S86 Workshop Calibration Corpus + Rule Extensions" §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension" Class 8.2 calibration corpus subsection.
- Existing Class 8.2 calibration corpus entry (S86 W-12 diagnosis) MUST remain unchanged.

**Input SHA-256 pins**:
- `.claude/rules/epistemic-discipline.md` pre-edit content.
- `computations/s87_gate_verdicts.txt` line 294 (W11-1 verdict line: `S87-MONODROMY-V_4-EXPLICIT: FAIL -- value='max_dev=1.163869e+00,supersedes=S87-MONODROMY-Z4-LANDING_per_PRU_Class_8_2' ... audit_sha256=8a4419a830e0e509...`)
- `sessions/archive/session-87/session-87-results-workingpaper.md` §W11-1 §"CC2 (V_4 vs Z_4 structural distinction)" block (line ~8915-8920 within §W11-1 span 8768-8908) for element-order [1,2,2,2] vs [1,2,4,4] citation.

**Expected output**:
- Rule-file diff: closure bullet appended to Class 8.2 calibration corpus entry citing W11-1 V_4 supersession event.
- Verdict line: `S87-METH-PRU-CLASS-8-2-CORPUS-CLOSURE: PASS -- value='class_8_2_corpus_closure_appended;W11-1_V4_supersession_event_FAIL_max_dev=1.16;Z4_alternative_falsified_via_element_order_mismatch' scheme=orchestrator-direct-rule-file-edit convention=epistemic-discipline-PRU-class-8-2-corpus-closure L_max=N/A audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`

**Substitution chain (THEOREM artifact-existence)**:
```
Step 1: pre-edit epistemic-discipline.md Class 8.2 calibration corpus = single S86 W-12 diagnosis bullet.
Step 2: orchestrator Edit operation appends a closure bullet recording W11-1 empirical confirmation (V_4 FAIL + Z_4 falsification via element-order mismatch).
Step 3: post-edit grep verifies W11-1 + V_4 supersession + element-order citations present in Class 8.2 calibration corpus subsection.
Step 4: PASS direction: all checks pass; corpus instance #1 closes empirically.
        FAIL direction: missing or wrong class.
```

**What PASS and FAIL mean**:
- PASS: PRU Class 8.2 calibration corpus instance #1 closes (W-12 diagnosis + W11-1 empirical confirmation jointly establish "Z_4 or similar" rubric is structurally permissive; V_4 admitted via cardinality match despite element-order distinction); both V_4 and Z_4 FAILed at substrate level. Class 8.2 promotion to MANDATORY at K=3 still requires 2 more instances.
- FAIL: rule-file extension not landed; W11-1's empirical confirmation of W-12's diagnosis remains undocumented.

---

## Methodology-class wave dispatch protocol

Per `.claude/rules/wave-classification.md` §"Dispatch consequences": "METHODOLOGY-class waves SKIP /rclab-coordinate compute-mode. The orchestrator writes the rule-file edits directly, treating each wave-item as analogous to the team-lead synthesis section."

Each gate executes via:
1. Orchestrator-direct Edit/MultiEdit on the target rule-file.
2. Append row to `.claude/rules/methodology-wave-allowlist.md` with the gate-ID + computed `sha256_of_plan_block` (over this plan-block file's gate-block).
3. Compute `audit_sha256` (over input-pin map of source documents) + `content_sha256` (over rule-file diff).
4. Append verdict line + dual-SHA companion to `computations/s87_gate_verdicts.txt`.
5. Verify on disk: rule-file diff lands; allowlist row appended; verdict line + companion row present.
6. TaskUpdate to completed.

No subagent dispatch (per M2 producing-operation type); orchestrator is the sole writer.

---

**Plan-block date**: 2026-04-30.
**Plan-block author**: orchestrator (mid-session authorization in response to user decision-point response "3 now").
**Sources**: W11 substantive findings — W11-1 §"CC2" + multi-output decomposition slot 3 (PRU Class 8.2 corpus closure); W11-2 + W11-3 §"Operational L_max truncation (Casimir-bound argument)" + §"Methodology — Structural-Saturation Theorem" (D_K block-diagonality lesson); W11-5 §"Cross-pillar bridge anatomy declaration (calibration corpus instance #2)" (K-counter advancement).
