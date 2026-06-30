# Session 87 Plan — Sub-Wave 9d: Stage-2 Verify Gate-Spec (connes+volovik S88+)

**Generated**: 2026-04-27
**Sub-wave owner**: `connes-ncg-theorist` (gate-spec authoring at S87 plan-freeze; CF-59 attribution `connes+volovik` resolves to connes-lead per S86 W-12 attribution convention; the actual S88+ Stage-2 dispatch fires TWO cross-reviewers in parallel — neither of whom is the wave-owner of THIS gate-spec)
**Sub-wave class**: COMPUTE-class gate-spec authoring (per `.claude/rules/wave-classification.md`; the gate-spec itself produces a numerical-or-structural verdict at S88+; at S87 plan-freeze the deliverable is the pre-registered 13-field block — the producing operation at S87 is plan-authoring, NOT execution)
**Source**: `sessions/session-plan/session-87-context.md` §2.1 row CF-59 (sole assigned item)
**Mode**: gate-spec only at S87 (NO S87 dispatch); S88+ orchestrator executes the pre-registered block as-is
**Item count**: 1 (CF-59)

## Sub-Wave 9d Summary

W9d carries a single gate-spec authoring item for CF-59 (W-9 source attribution): the **Stage-2 promotion gate-spec** for the **Joint F_2-Class Path-(c) Theorem**, whose Stage-1 candidate registry entry was authored at S86 W-9 lizzi+transit workshop and whose Stage-1 LANDING gate is CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`, attributed to `mack-cosmic-bridge` in W9-class wave).

Per `.claude/rules/joint-theorem-promotion.md`, joint cross-axis theorems can ONLY enter the permanent-results table via the 4-stage progression Stage-0 (workshop-internal) → Stage-1 (S87 candidate registration) → Stage-2 (two-agent parallel independent verify, S88+) → Stage-3 (permanent registration). W9d pre-registers the Stage-2 gate-spec at S87 plan-freeze so that S88+ orchestrator can dispatch it WITHOUT re-deriving the audit guarantees.

The joint clauses (c) and (d) of the 6-clause statement (a)..(f) require BOTH spectral-functional axis evidence AND transit-dynamics/superfluid axis evidence. The Stage-2 gate-spec dispatches TWO cross-reviewers in PARALLEL on DIFFERENT axes (connes-ncg-theorist on spectral-functional / axis-A; volovik-superfluid-universe-theorist on transit-dynamics / axis-B), with the joint clauses PASS-AND'd across both verdicts. Neither cross-reviewer is the original workshop authoring agent; cross-reviewers operate WITHOUT prior workshop context (R1/R2/R3 transcripts are EXCLUDED from dispatch prompts; cross-reviewers see ONLY the registered Stage-1 entry from §VII.AH plus any ancillary input files explicitly named in the gate-block).

volovik selected per agent-memory feedback "framework's SHARPEST reviewer" (W-9 workshop §T-CR3.2 lines 2138-2139); connes selected as spectral-functional axis cross-reviewer per the joint-theorem-promotion §"Two-Agent Independent-Verify" requirement (cross-reviewers MUST be on DIFFERENT axes from the workshop's authoring agents, AND must NOT be the original authors — lizzi-spectral-functional-theorist and transit-dynamics-theorist authored the Stage-0 workshop, hence connes-ncg-theorist replaces lizzi on the spectral-functional side and volovik-superfluid-universe-theorist replaces transit on the transit/superfluid side).

PASS criterion at S87 plan-freeze: the 5-element block per `joint-theorem-promotion.md` §"Audit at plan-freeze" is fully populated; cross-reviewer assignments are explicitly named; the audit script `computations/_joint_theorem_independent_verify_audit.py` (already inventoried in §0 of session-87-context.md as an EXISTS validator) is registered as the plan-freeze validator that S88+ orchestrator MUST invoke before dispatching the Stage-2 gate.

## Sub-Wave 9d Decision Point Prerequisites

Before W9d gate-spec authoring fires:

1. **CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`)** must have a verdict line emitted in `computations/s87_gate_verdicts.txt` AT-OR-BEFORE the S87 plan-freeze pass at which W9d's gate-spec is finalized — the Stage-2 gate-spec REFERENCES the §VII.AH registry slot (or the plan-author-allocated successor slot) where CF-54 lands the Stage-1 candidate text, and the cross-reviewers MUST consume the §VII.AH entry text as their sole derivational source. If CF-54 has not landed at S87 plan-freeze, W9d's gate-spec authoring proceeds with a CONDITIONAL slot pin (`registry_slot=§VII.AH-OR-NEXT-FREE-LETTER-PER-`registry-landing.md`) and the Stage-2 dispatch at S88+ resolves the slot from the actual CF-54 verdict at that time.

2. **`computations/_joint_theorem_independent_verify_audit.py`** must EXIST on disk at S87 plan-freeze. Per session-87-context.md §0 validation-tool inventory line 49, this validator is INVENTORIED as existing. Verified.

3. **`.claude/rules/joint-theorem-promotion.md`** must EXIST on disk and contain the §Stage 2 + §"Two-Agent Independent-Verify" + §"Audit at plan-freeze" sections referenced by W9d. Verified at S87 plan-freeze (rule-file landed at S86 W-9 promotion).

4. NO compute-execution prerequisite: W9d's deliverable at S87 is a PLAN-ARTIFACT (the gate-spec block in this file). The Stage-2 dispatch is S88+; W9d does NOT consume eigenvalues, NPZ data, or canonical_constants pins at S87 plan-authoring time.

## §W9d-1. S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY (Stage-2 promotion gate-spec)

### Provenance

- **CF source**: CF-59 in session-87-context.md §2.1 row 156 (W-9 CF-6).
- **Recommending agent**: `connes+volovik` (resolved to connes-ncg-theorist as wave-owner per attribution heuristic; ACTUAL S88+ Stage-2 cross-reviewers are connes-ncg-theorist axis-A + volovik-superfluid-universe-theorist axis-B per joint-theorem-promotion §Stage 2 different-axes requirement).
- **Effort estimate** (S88+ dispatch): 1.0 wave-equivalent.
- **Effort estimate** (S87 gate-spec authoring): ~2 hours plan-authoring (this file's §W9d-1 block).
- **Substrate target**: 6-clause Joint F_2-Class Path-(c) Theorem (Stage-0 workshop-internal text frozen at S86 W-9 R3-B closure lines 2203-2209 lock-ins, line 2291 final text). Joint clauses (c) and (d) require BOTH axes; single-axis clauses (a) lizzi-side, (e) lizzi-side; (b) transit-side, (f) transit-side.
- **Stage-1 LANDING reference**: CF-54 `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` lands the §VII.AH Stage-1 candidate registry entry at S87. W9d's gate-spec consumes the §VII.AH entry as its sole derivational source at S88+ dispatch time.

### Gate ID

`S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY`

### Trigger

`[VERIFY-THEOREM]` — Stage-2 cross-reviewer verification of a registered Stage-1 candidate joint cross-axis theorem against its 6-clause statement, NOT a numerical-comparison gate. The Stage-2 verdict is a STRUCTURAL theorem-grade verdict (each clause PASSes or FAILs; joint clauses are PASS-AND'd across the two reviewers).

### Classification

GEOMETRIC × PARTICLE (joint cross-axis theorem mixes spectral-functional axis content — F_2-class regulator behaviour, Path-(c) successor anchor cohomology — with transit-dynamics/superfluid axis content — Path-(c) inheritance arrow, transit-trajectory partition); NON-NUMERICAL at the top level (the verdict is theorem-grade); SUBSTRATE classification is INHERITED from Stage-1 entry §VII.AH.

### Hypothesis

The Stage-1 candidate Joint F_2-Class Path-(c) Theorem (6-clause statement (a)..(f) per S86 W-9 workshop §E-R2.2 lines 1097-1112, §T-CR2.4 lines 1336-1385, §L-CR3.3 amendment to clause (e) lines 1849-1858; final lock-in at lines 2203-2209 with final text at line 2291) holds as a STRUCTURAL THEOREM (Stage-3 promotable to permanent-results-registry §VII.AH-PERMANENT) when verified independently by:

- A spectral-functional cross-reviewer (axis-A) WITHOUT prior workshop context (R1/R2/R3 transcripts EXCLUDED), auditing single-axis clauses (a) + (e) + JOINT clauses (c) + (d).
- A transit-dynamics/superfluid cross-reviewer (axis-B) WITHOUT prior workshop context, auditing single-axis clauses (b) + (f) + JOINT clauses (c) + (d).

Joint clauses (c) and (d) PASS-AND'd across both verdicts (logical AND, not OR; an INFO from either reviewer on a joint clause stalls the joint clause at INFO-deferred; a FAIL from either reviewer on a joint clause routes the theorem to Stage-1 with FAILing-clause remediation queue).

### PASS / FAIL / INFO threshold

**Top-level Stage-2 verdict** (theorem-grade, not numerical):

- **PASS** at S88+ Stage-2 dispatch iff:
  1. BOTH cross-reviewers return PASS on their respective single-axis clauses (clauses (a) + (e) PASS by axis-A reviewer; clauses (b) + (f) PASS by axis-B reviewer); AND
  2. JOINT clauses (c) and (d) PASS independently in BOTH verdicts (logical AND across reviewers); AND
  3. Both cross-reviewers' dispatch-time prompts are AUDITED to confirm they EXCLUDE the workshop's R1/R2/R3 transcripts AND are dispatched in PARALLEL (not sequentially) AND are NOT the original Stage-0 workshop authoring agents (i.e., connes-ncg-theorist for axis-A and volovik-superfluid-universe-theorist for axis-B; NOT lizzi-spectral-functional-theorist or transit-dynamics-theorist).
- **FAIL** at S88+ iff: either cross-reviewer returns FAIL on ANY clause (single-axis or joint). Stage 2 → 3 promotion is BLOCKED; theorem stays at Stage-1; FAILing clauses route to next-session remediation queue with structured 4-field carry-forward specs.
- **INFO** at S88+ iff: either cross-reviewer returns INFO on a clause (no FAIL). Theorem stays at Stage-1; the INFO clause is documented as a Stage-2-INFO-deferred item with carry-forward to a future Stage-2 re-dispatch under modified verifier-rubric.

**S87 plan-freeze PASS criterion** (this gate-spec authoring deliverable, distinct from the S88+ Stage-2 verdict):

- **PASS at S87 plan-freeze** iff:
  1. The 5-element block per `joint-theorem-promotion.md` §"Audit at plan-freeze" is FULLY POPULATED in §W9d-1 below (5/5 elements explicit; see §"5-Element Block" sub-section); AND
  2. Cross-reviewer assignments are NAMED with full subagent-type strings (`connes-ncg-theorist`, `volovik-superfluid-universe-theorist`); AND
  3. Audit script `computations/_joint_theorem_independent_verify_audit.py` is REGISTERED as the plan-freeze validator that S88+ orchestrator MUST invoke before dispatching the Stage-2 gate; AND
  4. CF-54 §VII.AH dependency is declared (CONDITIONAL slot pin per W9d §"Decision Point Prerequisites" item 1 if CF-54 has not landed at the moment of S87 plan-freeze).
- **FAIL at S87 plan-freeze** if any of (1)-(4) is missing.
- **INFO at S87 plan-freeze** if 5-element block is partial AND cross-reviewer assignments are named AND audit-script registered AND §VII.AH dependency declared, but the CONDITIONAL slot pin has NOT been resolved (i.e., CF-54 has not landed). In this case, S87 plan-freeze emits the gate-spec with `registry_slot=§VII.AH-OR-NEXT-FREE-LETTER` and the S88+ orchestrator resolves the slot at dispatch time.

**Tolerance rule**: THEOREM (theorem-grade verdict; no numerical tolerance applies).

### Machinery pin (PRDR — Pre-Registration Dry-Run, fully enumerated)

```yaml
schema_version: R3
gate_id: S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY
verdict_source: computations/s87_gate_verdicts.txt   # for the S87 plan-freeze PASS verdict
verdict_source_s88_plus: computations/s88_gate_verdicts.txt  # for the S88+ Stage-2 dispatch verdict (forward-pin; orchestrator uses the actual session number at dispatch)
trigger: VERIFY-THEOREM
classification: GEOMETRIC × PARTICLE (NON-NUMERICAL theorem-grade)

machinery:
  # Cross-reviewer assignment (mandatory per joint-theorem-promotion §Stage 2)
  cross_reviewer_axis_A: connes-ncg-theorist    # spectral-functional axis
  cross_reviewer_axis_B: volovik-superfluid-universe-theorist  # transit-dynamics/superfluid axis
  cross_reviewer_axis_A_audits_clauses: [a, e, c-JOINT, d-JOINT]
  cross_reviewer_axis_B_audits_clauses: [b, f, c-JOINT, d-JOINT]
  joint_clauses_AND_aggregation: [c-JOINT, d-JOINT]   # logical AND across both reviewers' verdicts
  dispatch_mode: PARALLEL    # NOT sequential per §Stage 2 requirement
  workshop_context_excluded: true   # R1/R2/R3 transcripts EXCLUDED from dispatch prompts
  workshop_authoring_agents_forbidden: [lizzi-spectral-functional-theorist, transit-dynamics-theorist]   # cannot serve as cross-reviewers
  cross_reviewer_input_documents:
    - sessions/permanent-results-registry.md §VII.AH (Stage-1 entry; sole derivational source)
    - canonical_constants.py (read-only, for any framework-shared constants the theorem cites)
    - sessions/framework/registry/falsifier-master-inventory.md rows updated by CF-54 (for falsifier-anchor cross-references)
  cross_reviewer_input_documents_FORBIDDEN:
    - sessions/archive/session-86/workshops/* (workshop transcripts EXCLUDED)
    - sessions/archive/session-86/session-86-w9-* (workshop synthesis EXCLUDED)
    - sessions/archive/session-86/path-c-reassessment-* (workshop closure EXCLUDED)

  # Audit-script registration (mandatory per joint-theorem-promotion §"Audit at plan-freeze")
  plan_freeze_validator: computations/_joint_theorem_independent_verify_audit.py
  validator_invocation: |
    python computations/_joint_theorem_independent_verify_audit.py \
      --gate-id S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY \
      --plan-file sessions/session-plan/session-87-plan-w9d.md \
      --json sessions/session-plan/session-87-plan-w9d-stage2-validation.json
  validator_pass_criteria: |
    PASS iff (1) two cross-reviewers dispatched in parallel (not sequentially);
            (2) cross-reviewers on DIFFERENT axes (spectral-functional + transit-dynamics/superfluid);
            (3) cross-reviewers NOT the original workshop authoring agents
                (i.e., NOT lizzi-spectral-functional-theorist, NOT transit-dynamics-theorist);
            (4) dispatch prompts EXCLUDE workshop R1/R2/R3 transcripts
                (verified by grep on the prompt text for forbidden source paths);
            (5) JOINT clauses (c) and (d) PASS-AND'd across both verdicts in the gate logic.

  # Stage-1 candidate registry slot dependency (CONDITIONAL on CF-54 landing)
  registry_slot_pin: §VII.AH-OR-NEXT-FREE-LETTER-PER-registry-landing.md
  registry_slot_resolution_protocol: |
    At S88+ Stage-2 dispatch time, orchestrator greps computations/s87_gate_verdicts.txt
    for the CF-54 verdict line (gate ID S87-PATH-C-SUCCESSOR-ANCHOR-LANDING); the verdict
    line's STAGE-1-CANDIDATE entry tag carries the actual §VII.{slot} identifier; this
    is substituted into the cross-reviewer dispatch prompts.

  # 6-clause statement source (read-only by cross-reviewers via §VII.AH entry text)
  theorem_clauses:
    a: lizzi-side single-axis (cross-reviewer axis-A audits)
    b: transit-side single-axis (cross-reviewer axis-B audits)
    c: JOINT (BOTH axes; PASS-AND'd across reviewers)
    d: JOINT (BOTH axes; PASS-AND'd across reviewers)
    e: lizzi-side single-axis (cross-reviewer axis-A audits)
    f: transit-side single-axis (cross-reviewer axis-B audits)
  theorem_corrigenda:
    - CR1: per S86 W-9 workshop §L-CR3.3 amendment to clause (e) lines 1849-1858
    - CR2: per S86 W-9 workshop §T-CR2.4 lines 1336-1385 (clause (b) refinement)
    - CR3: per S86 W-9 workshop R3-B closure lines 2203-2209 (final lock-ins)
    - CR4: per S86 W-9 workshop §E-R2.2 lines 1097-1112 (clause (c) joint-anchor pin)

  # Numerical-machinery pins (none at S87 gate-spec authoring; the gate is theorem-grade)
  N_eval: N/A   # theorem-grade verdict; no eigenvalue computation
  L_max: N/A   # theorem-grade verdict; no L-scan
  scan_range: N/A
  step_size: N/A
  tolerance: THEOREM (no numerical tolerance)
  scheme: N/A (not regulator-axis dependent at theorem level)
  convention: SOURCE-DOUBLE-CITE-CO-PRIMARY per registry-landing.md (joint-clause anchors are sequential V_input + C_output chain across spectral-functional + transit-dynamics axes; both anchors at co-primary weight)
  random_seed: N/A
  GPU_path: N/A (no eigenvalue/linear-algebra dispatch)
  domain_used_frac: N/A (no auto-shortening clause; theorem-grade gate)

  # Output 4-tuple (theorem-grade)
  expected_output_4_tuple_S87_planfreeze:
    value: '5-element-block-populated AND cross-reviewers-named AND audit-script-registered AND CF-54-dependency-declared'
    scheme: 'PRDR-stage-2-spec-authoring'
    convention: 'SOURCE-DOUBLE-CITE-CO-PRIMARY'
    L_max: 'N/A'
  expected_output_4_tuple_S88_plus:
    value: 'PASS|FAIL|INFO with per-clause sub-verdicts (a, b, c-JOINT, d-JOINT, e, f)'
    scheme: 'two-agent-parallel-independent-verify'
    convention: 'joint-clause-AND-aggregation'
    L_max: 'N/A'
```

### Input SHA-256 pins

The gate-spec at S87 plan-freeze pins the following input documents by content (the SHA-256 values below are pinned at S87 plan-freeze; the S88+ orchestrator re-computes and verifies they match before dispatching):

```yaml
input_sha_pins:
  # Rule-files (must exist at S88+ dispatch; SHA verified against S87 plan-freeze pin)
  - file: .claude/rules/joint-theorem-promotion.md
    sha256: <computed-at-S87-planfreeze>
    role: stage-2-protocol-source
  - file: .claude/rules/registry-landing.md
    sha256: <computed-at-S87-planfreeze>
    role: SOURCE-DOUBLE-CITE-CO-PRIMARY-convention-source
  - file: .claude/rules/agent-standards.md
    sha256: <computed-at-S87-planfreeze>
    role: cross-reviewer-completion-verification-source
  - file: .claude/rules/epistemic-discipline.md
    sha256: <computed-at-S87-planfreeze>
    role: independent-verification-evidence-source
  - file: .claude/rules/phononic-framing.md
    sha256: <computed-at-S87-planfreeze>
    role: substrate-first-direction-of-explanation-source

  # Stage-1 entry source (CONDITIONAL on CF-54 landing; SHA computed at S88+ dispatch)
  - file: sessions/permanent-results-registry.md
    sha256: <computed-at-S88-plus-dispatch>
    role: stage-1-candidate-entry-source-VII-AH
    note: |
      At S87 plan-freeze, the §VII.AH slot identifier is CONDITIONAL on CF-54 landing;
      at S88+ Stage-2 dispatch, the orchestrator resolves the slot from the CF-54 verdict
      line and re-pins the SHA at dispatch time.

  # Audit-script (must exist at S87 plan-freeze; verified by §0 validation-tool inventory)
  - file: computations/_joint_theorem_independent_verify_audit.py
    sha256: <computed-at-S87-planfreeze>
    role: plan-freeze-validator-source

  # Falsifier-master-inventory (SHA computed at CF-54 landing time; W9d cross-reviewers consume CF-54-updated rows)
  - file: sessions/framework/registry/falsifier-master-inventory.md
    sha256: <computed-at-S88-plus-dispatch>
    role: falsifier-anchor-cross-reference-source

  # Workshop-transcript files (FORBIDDEN — listed here only to enforce exclusion; cross-reviewer prompts MUST NOT cite these)
  - file: sessions/archive/session-86/workshops/* AND sessions/archive/session-86/session-86-w9-* AND sessions/archive/session-86/path-c-reassessment-*
    sha256: N/A
    role: FORBIDDEN-workshop-context-source
    enforcement: |
      Plan-freeze validator _joint_theorem_independent_verify_audit.py greps the dispatch
      prompts for any of these path-prefixes; presence triggers FAIL severity (cross-reviewer
      independence is structurally compromised).
```

### Expected output 4-tuple (S87 plan-freeze and S88+ dispatch)

At **S87 plan-freeze**:

```
(value='5-element-block-populated AND cross-reviewers-named AND audit-script-registered AND CF-54-dependency-declared',
 scheme='PRDR-stage-2-spec-authoring',
 convention='SOURCE-DOUBLE-CITE-CO-PRIMARY',
 L_max='N/A')
```

At **S88+ Stage-2 dispatch** (forward-pin; the actual verdict line will be appended to `computations/s{NN}_gate_verdicts.txt` where NN is the actual S88+ session number):

```
(value='PASS|FAIL|INFO with per-clause sub-verdicts (a-axisA, b-axisB, c-JOINT-AND, d-JOINT-AND, e-axisA, f-axisB)',
 scheme='two-agent-parallel-independent-verify',
 convention='joint-clause-AND-aggregation',
 L_max='N/A')
```

### Substitution chain (for the directional audit-script PASS predicate)

The plan-freeze validator's PASS predicate is a 5-conjunction logical AND. The substitution chain showing the predicate is well-defined and bounded:

**Step 1** — Definitions:
- Let `P_5` = the 5-element block per `joint-theorem-promotion.md` §"Audit at plan-freeze".
- Let `P_5(i)` for `i ∈ {1, 2, 3, 4, 5}` = the i-th element of `P_5` (1: rank declared; 2: 4 gate types pre-registered; 3: ratio prediction with substrate-derived value + tolerance band; 4: cancellation theorem applicability declared; 5: per-row substrate predictions + lab S/N margin).
- Let `present(P_5(i))` = boolean indicating whether element `i` is populated in §W9d-1 above.

**Step 2** — Substitute into PASS predicate:
- PLAN-FREEZE-PASS := `(forall i in {1..5}: present(P_5(i))) AND (cross_reviewer_axis_A and cross_reviewer_axis_B both named) AND (validator_pin = _joint_theorem_independent_verify_audit.py) AND (CF-54 dependency declared)`.

**Step 3** — Simplify to canonical form:
- PLAN-FREEZE-PASS := `(P_5 fully populated) ∧ (cross-reviewers named) ∧ (validator registered) ∧ (CF-54 dep declared)`.

**Step 4** — Read off the direction:
- PLAN-FREEZE-PASS is a 4-clause logical AND. Failure of ANY clause routes the gate to FAIL or INFO per the §"PASS / FAIL / INFO threshold" pre-registration. Specifically:
  - All 4 clauses present → PASS.
  - 3-of-4 with CONDITIONAL slot pin only on the §VII.AH dependency (CF-54 not yet landed at plan-freeze moment) → INFO.
  - Any other partial → FAIL.

**Step 5** — Conclusion:
- The plan-freeze PASS predicate is a deterministic 4-clause AND with a single allowed INFO branch (the §VII.AH CONDITIONAL slot pin); no numerical sign or threshold ambiguity. The direction is monotone: each populated clause moves the verdict from FAIL toward PASS; INFO is reached only when 3-of-4 clauses are populated AND the missing clause is the CONDITIONAL §VII.AH slot pin.

### What PASS, FAIL, INFO mean for the solution space

**At S87 plan-freeze**:

- **PASS** means: the Stage-2 gate-spec is COMPLETE and READY for S88+ orchestrator dispatch as-is, without further plan-authoring work. The S88+ dispatch can fire WITHOUT re-deriving any audit guarantees. The Joint F_2-Class Path-(c) Theorem's promotion pathway is on-rails for Stage-2 → Stage-3 if the cross-reviewers PASS.

- **FAIL** means: the gate-spec is INCOMPLETE; one or more of the 5-element block, cross-reviewer assignments, audit-script registration, or CF-54 dependency declaration is missing. The S88+ dispatch is BLOCKED at the plan-freeze validator step and the gate-spec returns to W9d (or to an S87 W9d-FOLLOWUP gate) for completion.

- **INFO** means: the gate-spec is STRUCTURALLY COMPLETE except for the §VII.AH slot pin which is CONDITIONAL on CF-54 landing. The S88+ orchestrator resolves the slot at dispatch time from the CF-54 verdict line. This is the EXPECTED INFO state if S87 plan-freeze is consolidated BEFORE CF-54 (W9-class wave under mack-cosmic-bridge) lands.

**At S88+ Stage-2 dispatch**:

- **PASS** means: the Joint F_2-Class Path-(c) Theorem 6-clause statement is INDEPENDENTLY verified by both cross-reviewers; joint clauses (c) and (d) PASS-AND'd; the theorem is eligible for Stage-3 PERMANENT registration in `permanent-results-registry.md` §VII.AH-PERMANENT (or the resolved slot identifier). The framework gains a permanent cross-axis joint theorem connecting spectral-functional axis (F_2-class regulator behaviour, Path-(c) successor anchor cohomology) and transit-dynamics/superfluid axis (Path-(c) inheritance arrow, transit-trajectory partition).

- **FAIL** means: at least one cross-reviewer returns FAIL on a clause. Stage 2 → 3 promotion is BLOCKED. The theorem stays at Stage-1 candidate. FAILing clauses route to next-session remediation queue with structured 4-field carry-forward specs identifying the FAIL'd clause and the remediation gate. The framework's joint-theorem registry retains the candidate at STAGE-1-CANDIDATE tag pending remediation.

- **INFO** means: at least one cross-reviewer returns INFO on a clause; no FAIL. Theorem stays at Stage-1. INFO clauses route to a future Stage-2 re-dispatch under modified verifier-rubric or with additional ancillary inputs. The framework's joint-theorem registry retains the candidate at STAGE-1-CANDIDATE tag with INFO-deferred sub-clause notation.

### Substrate framing (per `phononic-framing.md` §"IS Space, Not IN Space")

The Joint F_2-Class Path-(c) Theorem is a SUBSTRATE-FIRST theorem: clauses (a)..(f) name SUBSTRATE-IS observables (F_2-class regulator behaviour at substrate-distance Mellin poles; Path-(c) successor anchor cohomology classes on the substrate's spectral triple `(A_K, H_K, D_K)`; Path-(c) inheritance arrow as substrate-mode-by-substrate-mode transit-trajectory partition); the LABORATORY-IN observables emerging via the substrate-laboratory bridge are the predicted CMB falsifier values (LiteBIRD n_T discrimination band, LISA Ω_GW regulator-class contrast).

Joint clauses (c) and (d) connect the SUBSTRATE-IS spectral-functional content to the SUBSTRATE-IS transit-dynamics content via a regulator-class-preserving morphism (per registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"; the V_input layer is the F_2-class regulator algebra, the C_output layer is the Path-(c) inheritance arrow theorem CONDITIONAL on the F_2-class premise; together they fix the joint conclusion uniquely).

The Stage-2 cross-reviewer dispatch enforces the IS-not-IN convention at the audit level: connes-ncg-theorist (axis-A) audits the substrate-IS spectral-functional clauses (a) + (e) + JOINT (c) + (d) WITHOUT prior workshop context; volovik-superfluid-universe-theorist (axis-B) audits the substrate-IS transit-dynamics/superfluid clauses (b) + (f) + JOINT (c) + (d) WITHOUT prior workshop context. Neither reviewer is permitted to invoke a LABORATORY-IN observable as logically prior to a SUBSTRATE-IS observable; the direction of explanation is FROM substrate TOWARD emergent laboratory predictions.

### 5-Element Block (per `joint-theorem-promotion.md` §"Audit at plan-freeze")

Per the rule-file's §"Audit at plan-freeze" requirements, plan-freeze validators landing a Stage-2 gate-spec MUST verify the 5 elements below. W9d's gate-spec populates each element explicitly:

#### Element 1 — Two cross-reviewers dispatched in PARALLEL (not sequentially)

- `cross_reviewer_axis_A`: `connes-ncg-theorist`
- `cross_reviewer_axis_B`: `volovik-superfluid-universe-theorist`
- `dispatch_mode`: PARALLEL
- Enforcement: the S88+ orchestrator dispatches BOTH cross-reviewers in a SINGLE Agent-tool batch (per the multi-agent parallel-dispatch convention per `feedback_dispatch-discipline.md` and `feedback_dispatch-discipline.md`); the plan-freeze validator `_joint_theorem_independent_verify_audit.py` greps the dispatch log for the parallel-batch signature.

#### Element 2 — Cross-reviewers on DIFFERENT axes

- Axis-A (spectral-functional): connes-ncg-theorist
- Axis-B (transit-dynamics/superfluid): volovik-superfluid-universe-theorist
- Differentness verification: connes-ncg-theorist's spawn-prompt domain is "spectral triple (A, H, D), KO-dimension, Seeley-DeWitt coefficients, NCG axioms" per `connes-ncg-theorist.md` agent definition; volovik-superfluid-universe-theorist's spawn-prompt domain is "superfluid-universe analog, transit-dynamics, GGE relic, BdG spectral triple, 3He-B inheritance" per `volovik-superfluid-universe-theorist.md` agent definition. Domains are SEMANTICALLY DISJOINT at the spectral-functional vs transit-dynamics partition.
- Enforcement: validator greps both agent definitions for the listed domain phrases; verifies disjoint partition.

#### Element 3 — Neither cross-reviewer is the original workshop authoring agent

- Stage-0 workshop authoring agents (per S86 W-9 attribution): `lizzi-spectral-functional-theorist` (lizzi-side; clauses (a) + (e) + JOINT (c) + (d) authoring) + `transit-dynamics-theorist` (transit-side; clauses (b) + (f) + JOINT (c) + (d) authoring).
- Stage-2 cross-reviewers: `connes-ncg-theorist` (axis-A; replaces lizzi as spectral-functional cross-reviewer) + `volovik-superfluid-universe-theorist` (axis-B; replaces transit as transit-dynamics/superfluid cross-reviewer).
- Disjointness verification: `{connes-ncg-theorist, volovik-superfluid-universe-theorist} ∩ {lizzi-spectral-functional-theorist, transit-dynamics-theorist} = ∅`.
- Enforcement: validator compares cross-reviewer subagent_type strings against forbidden-set; presence of any forbidden agent triggers FAIL.

#### Element 4 — Dispatch prompts EXCLUDE workshop R1/R2/R3 transcripts

- Forbidden source paths in dispatch prompts:
  - `sessions/archive/session-86/workshops/*` (any workshop transcript)
  - `sessions/archive/session-86/session-86-w9-*` (W-9 synthesis files)
  - `sessions/archive/session-86/path-c-reassessment-*` (Path-(c) reassessment workshop closure)
- Allowed source paths in dispatch prompts:
  - `sessions/permanent-results-registry.md §VII.AH` (Stage-1 entry; sole derivational source)
  - `computations/canonical_constants.py` (read-only, framework-shared constants)
  - `sessions/framework/registry/falsifier-master-inventory.md` rows updated by CF-54 (falsifier-anchor cross-references)
- Enforcement: `_joint_theorem_independent_verify_audit.py` greps dispatch prompt text for the forbidden-source-paths list; presence of any forbidden path triggers FAIL severity at the plan-freeze validation step.

#### Element 5 — JOINT clauses (c) and (d) PASS-AND'd across both verdicts

- JOINT clauses requiring bilateral PASS: clause (c) and clause (d).
- Aggregation logic at gate execution (S88+):
  - Clause (c) Stage-2 verdict := `(connes-ncg-theorist clause-c verdict == PASS) AND (volovik-superfluid-universe-theorist clause-c verdict == PASS)`.
  - Clause (d) Stage-2 verdict := `(connes-ncg-theorist clause-d verdict == PASS) AND (volovik-superfluid-universe-theorist clause-d verdict == PASS)`.
  - INFO from EITHER reviewer on a JOINT clause stalls the JOINT clause at INFO-deferred (NOT PASS); the joint-AND is monotone INFO-absorbing.
  - FAIL from EITHER reviewer on a JOINT clause routes the JOINT clause to FAIL (NOT INFO); the joint-AND is monotone FAIL-absorbing.
- Single-axis clauses ((a), (e) by axis-A; (b), (f) by axis-B) are evaluated as standalone PASS|FAIL|INFO from the assigned reviewer; no AND-aggregation across reviewers (each reviewer independently audits their assigned clauses).
- Enforcement: the gate execution at S88+ implements the AND-aggregation in the gate's verdict-line emission script; the plan-freeze validator checks the script's logic against the pre-registered aggregation rule.

### Cross-link to `epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2

The 5-element block is the CONSTRUCTIVE PATHWAY for joint cross-axis evidence to enter the permanent-results table WITHOUT falling into the "agreement-among-agents" exclusion. Specifically:

- "Agreement among agents" with shared workshop context (Stage-0 lizzi + transit at R3-B closure) → NOT evidence per item-2.
- "Agreement among agents" with NO shared workshop context (Stage-2 connes + volovik dispatched with R1/R2/R3 EXCLUDED, reading ONLY §VII.AH Stage-1 entry) → IS evidence per the standard "What Counts as a Result" criterion.

The 4-stage progression (Stage-0 workshop → Stage-1 candidate → Stage-2 independent verify → Stage-3 permanent) is the ONLY recognized pathway for joint cross-axis theorems per `joint-theorem-promotion.md`; W9d's gate-spec implements Stage-2 as on-rails for the Joint F_2-Class Path-(c) Theorem.

## Sub-Wave 9d → next-sub-wave Decision Point

W9d is the LAST sub-wave in the W9 partition (W9a/W9b/W9c precede; W9d is the Stage-2-promotion gate-spec for CF-59 specifically). At S87 plan-freeze close:

- **W9d → W10 transition**: independent of W9d outcome; W10 wave consumes its own CF assignments per the partition manifest.
- **W9d S87 verdict-line** lands in `computations/s87_gate_verdicts.txt` per the canonical-form schema-version=R3 dual-SHA template at S87 plan-freeze closure. Verdict format:

```
S87-W9D-STAGE2-VERIFY-GATE-SPEC-AUTHORING: PASS|INFO|FAIL -- value='<5-element-block-status_AND_cross-reviewers-named_AND_audit-script-registered_AND_CF-54-dependency-declared>' scheme=PRDR-stage-2-spec-authoring convention=SOURCE-DOUBLE-CITE-CO-PRIMARY L_max=N/A audit_sha256=<computed> content_sha256=<computed> schema_version=R3
```

(The S87 verdict pinned at plan-freeze-closure documents whether W9d's gate-spec authoring deliverable is COMPLETE; the S88+ Stage-2 dispatch verdict is a SEPARATE verdict-line emitted at S88+ session against the actual two-agent independent-verify outcome.)

- **S88+ pre-dispatch decision point**: at S88+ (or whenever orchestrator schedules the Stage-2 dispatch), the plan-freeze validator `_joint_theorem_independent_verify_audit.py` MUST be invoked AS-A-PRE-DISPATCH-CHECK. Validator PASS → orchestrator fires the parallel two-agent dispatch with the ALLOWED input documents; cross-reviewers operate WITHOUT prior workshop context. Validator FAIL → dispatch is BLOCKED; FAILing element returns to W9d-FOLLOWUP gate-spec amendment.

- **Cross-W9 dependencies**: W9d's gate-spec consumes the §VII.AH registry slot pinned at CF-54 (W9-class wave under mack-cosmic-bridge). At S87 plan-freeze, if CF-54 has landed before W9d closes, W9d pins the resolved slot identifier directly; otherwise W9d pins the CONDITIONAL slot `§VII.AH-OR-NEXT-FREE-LETTER` and the S88+ orchestrator resolves at dispatch time per the §"Decision Point Prerequisites" item-1 protocol.

## Sub-Wave 9d Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"PRDR (Pre-Registration Dry-Run)", every gate-block has its free parameters statically enumerated at plan-write time. W9d's §W9d-1 gate-spec has its full machinery-pin block in §"Machinery pin (PRDR — Pre-Registration Dry-Run, fully enumerated)" above. The §0.11 machinery-enumeration pin for W9d is:

```yaml
machinery_enumeration_pin_W9d:
  total_gates: 1
  gates:
    - gate_id: S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY
      free_parameters_enumerated:
        - cross_reviewer_axis_A
        - cross_reviewer_axis_B
        - cross_reviewer_axis_A_audits_clauses
        - cross_reviewer_axis_B_audits_clauses
        - joint_clauses_AND_aggregation
        - dispatch_mode
        - workshop_context_excluded
        - workshop_authoring_agents_forbidden
        - cross_reviewer_input_documents
        - cross_reviewer_input_documents_FORBIDDEN
        - plan_freeze_validator
        - validator_invocation
        - validator_pass_criteria
        - registry_slot_pin
        - registry_slot_resolution_protocol
        - theorem_clauses
        - theorem_corrigenda
        - N_eval (= N/A)
        - L_max (= N/A)
        - scan_range (= N/A)
        - step_size (= N/A)
        - tolerance (= THEOREM)
        - scheme (= N/A; theorem-grade)
        - convention (= SOURCE-DOUBLE-CITE-CO-PRIMARY)
        - random_seed (= N/A)
        - GPU_path (= N/A)
        - domain_used_frac (= N/A)
      diagnostics_declared:
        - N/A (theorem-grade gate; no numerical diagnostics)
      pin_count: 27
      unpinned_count: 0
      PRU_status: CARDINALITY-CLEAR
  total_pins: 27
  total_unpinned: 0
  PRU_aggregate_status: CARDINALITY-CLEAR (D_PRU_raw = 0)
  source_recon_status: NOT-APPLICABLE (no numerical pins consumed against canonical_constants.py)
  substrate_first_provenance_status: PASS (cross-reviewer input documents are SUBSTRATE-FIRST: §VII.AH Stage-1 entry, canonical_constants.py, falsifier-master-inventory.md; NO external-paper provenance citations)
  feasibility_envelope_status: NOT-APPLICABLE (no compute-time, GPU, or precision pins consumed at S87 plan-freeze; the S88+ Stage-2 dispatch is agent-mediated cross-review, not eigenvalue-class compute)
```

## Sub-Wave 9d Input-SHA Ledger

The complete Input-SHA ledger for W9d is enumerated in §W9d-1 §"Input SHA-256 pins" above. Summary at sub-wave level:

| File | Role | SHA computation moment |
|:-----|:-----|:------------------------|
| `.claude/rules/joint-theorem-promotion.md` | Stage-2 protocol source | S87 plan-freeze |
| `.claude/rules/registry-landing.md` | SOURCE-DOUBLE-CITE-CO-PRIMARY convention source | S87 plan-freeze |
| `.claude/rules/agent-standards.md` | Cross-reviewer completion verification source | S87 plan-freeze |
| `.claude/rules/epistemic-discipline.md` | Independent-verification evidence-source pinning | S87 plan-freeze |
| `.claude/rules/phononic-framing.md` | Substrate-first direction-of-explanation source | S87 plan-freeze |
| `computations/_joint_theorem_independent_verify_audit.py` | Plan-freeze validator source | S87 plan-freeze (verified EXISTS per session-87-context.md §0 line 49) |
| `sessions/permanent-results-registry.md §VII.AH` | Stage-1 candidate entry (CF-54 output) | S88+ Stage-2 dispatch (CONDITIONAL on CF-54 landing) |
| `sessions/framework/registry/falsifier-master-inventory.md` | Falsifier-anchor cross-references (CF-54 row updates) | S88+ Stage-2 dispatch (CONDITIONAL on CF-54 landing) |
| `computations/canonical_constants.py` | Framework-shared constants (read-only) | S88+ Stage-2 dispatch |

**Forbidden inputs** (enforcement at plan-freeze validator):

| Forbidden path-prefix | Reason |
|:----------------------|:-------|
| `sessions/archive/session-86/workshops/*` | Workshop transcripts EXCLUDED per §Stage 2 "without prior workshop context" requirement |
| `sessions/archive/session-86/session-86-w9-*` | W-9 synthesis files EXCLUDED per same requirement |
| `sessions/archive/session-86/path-c-reassessment-*` | Path-(c) reassessment workshop closure EXCLUDED per same requirement |

End of session-87-plan-w9d.md.
