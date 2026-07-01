# Mechanical-Closure Discipline (Orchestrator-Authored Verdict-Line Emission)

Calibration corpora, K-counter advancement records, dated promotion events, and per-instance narratives live at `sessions/framework/registry/pru-class-corpus.md` (§§13, 14 currently; the §"Layer-separability carve-out" K=1 calibration row is queued as a forward extension). This file carries directives only.

## Scope

Orchestrator-authored mechanical-closure scripts emit verdict lines to `computations/session-{N}/s{N}_gate_verdicts.txt` WITHOUT specialist-agent dispatch and WITHOUT physics computation. The mechanical closure documents that a gate could not be evaluated because at least one upstream prerequisite has verdict ≠ PASS — the gate is structurally untestable at this session.

This rule formalizes the pattern that distinguishes HONEST mechanical closure from the task-complete-lie failure mode (verdict line appended without working-paper section, agent reports completion while final write skipped). Cross-link: `agent-standards.md §"Completion Verification"`.

## When mechanical closure IS acceptable

A mechanical-closure script may be authored ONLY when ALL of the following hold:

1. **Upstream-block topology is the cause**: every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's downstream decision-point table specifies the documented outcome for prereq-block (typically "PRE-REG-INC, deferred to S{N+1}"). The plan author MUST have anticipated the prereq-block scenario; if the plan does not address it, the closure script is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN.

2. **Verdict honesty**: emitted verdicts are FAIL or PRE-REG-INC, NEVER PASS. The descriptive value string MUST follow the `value='PRE-REG-INC_blocked_by_<symbol>_<status>_*'` or `value='upstream_<reason>'` pattern. PASS verdicts from a mechanical closure script are PROHIBITED_ACTIONS Class 4 (ansatz-forced PASS).

3. **Per-gate-distinct audit_sha256**: even when multiple gates share a prerequisite set (e.g., two gates both blocked solely on C10), the pinmap that feeds `audit_sha256` MUST embed per-gate identity keys (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) so the resulting `audit_sha256` values are pairwise distinct across all gates the script closes. Sig_5 ladder uniqueness is preserved by construction.

4. **Audit-trail signature**: the verdict line MUST carry a descriptive `value` string that names the blocking prereq and its status. A future audit script MUST be able to grep the canonical line and verify the named upstream gate exists and has the named status in the same verdict file.

5. **Working-paper update is in-script**: the closure script MUST update the corresponding working-paper section's `**Status**`, `**Verdict**`, `**Results**`, and `**Substrate framing**` blocks IN THE SAME RUN as the verdict-line append. A closure script that emits the verdict line but skips the working-paper update is the task-complete-lie pattern and is FORBIDDEN.

## Layer-separability carve-out (admissible-with-conditions)

Extends mechanical closure admissibility to a STRUCTURALLY DIFFERENT class beyond the upstream-blocked case above: **layer-separable analyses** where the layer-functor `F : substrate → methodology → audit` (per `epistemic-discipline.md §"Layer-Decomposition"`) cleanly separates a substrate-physics observable into a Type-F (single-summand-projection trace) sub-observable that admits closed-form mechanical evaluation, plus a Type-S (state-pair functional) sub-observable that requires numerical evaluation.

Mechanical closure on the Type-F sub-observable IS admissible WITH CONDITIONS L1-L4 below. Mechanical closure on the Type-S sub-observable is NEVER admissible (state-pair functionals are algebra-DEPENDENT per the 4-corner classification of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`).

The carve-out is a STRUCTURAL extension, NOT a per-gate convention swap. The convention-tag honesty discipline L4 is the boundary distinguishing the structural extension from PROHIBITED_ACTIONS Class 1 (convention-shopping).

### Four conditions (L1-L4)

A mechanical-closure script may be authored under this carve-out ONLY when ALL FOUR hold simultaneously:

- **L1 (Layer-functor cleanness)**: the substrate-physics observable admits a layer-functor `F` decomposition `F : substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`, AND the Type-F vs Type-S partition aligns with the substrate ↔ methodology layer pair under `F`. Type-F sub-observable is the substrate-physics image; Type-S is the methodology-floor image; `F` preserves the partition by construction.

- **L2 (Type-F closed-form)**: the Type-F sub-observable admits a closed-form algebraic identity (canonical exemplar: a single-summand-projection trace `Tr_{M_n(ℂ)}(P · A)` with `P` a minimal central projection on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and `A` the observable expression) whose evaluation is **mechanical**: no numerical iteration, no random seed, no scan, no convergence loop. The closed-form must be evaluable bit-precision in a single-pass pure function on the substrate algebra.

- **L3 (Type-S separation)**: the Type-S sub-observable is structurally separated from the Type-F sub-observable per the algebra-axis orthogonality 4-corner classification (Type-F is algebra-INVARIANT spectrum-only functional; Type-S is algebra-DEPENDENT state-pair functional). Mechanical closure on the Type-F sub-observable does NOT pre-determine the Type-S verdict; the Type-S verdict remains a separate numerical evaluation under its own pre-registered threshold.

- **L4 (Honesty disclosure)**: the closure script's verdict-line `convention=` field MUST encode the carve-out tag explicitly, following the canonical pattern `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F`. The corresponding working-paper section MUST include an explicit Type-F / Type-S separation paragraph naming the central projection used for the Type-F evaluation and citing the Type-S sub-observable routing (separate gate or PRE-REG-INC carry-forward). Failure to disclose either the convention tag OR the working-paper paragraph is a PROHIBITED_ACTIONS Class 1 violation (convention-shopping) per `v3-closure-recovery.md §PROHIBITED_ACTIONS` — silent invocation collapses the structural extension and reverts to convention-shopping.

### Stage-2 cross-reviewer PASS-AND requirement

Because the carve-out admits closed-form mechanical evaluation that LOOKS like a substrate-physics PASS gate, a Stage-2 cross-reviewer PASS-AND per `joint-theorem-promotion.md §"Stage 2"` is REQUIRED before any downstream gate may dispatch under this carve-out. Two cross-reviewers operate on opposite axes:

- **Axis A (spectral / NCG-axiomatic)** — `connes-ncg-theorist` audits L1 (layer-functor cleanness) + L2 (closed-form evaluation) from the spectral side. Verifies `F` decomposition is well-defined and closed-form evaluation matches the central-projection trace identity.
- **Axis B (substrate / superfluid-universe)** — `volovik-superfluid-universe-theorist` audits L3 (Type-S separation) + L4 (honesty disclosure) from the substrate side. Verifies Type-F and Type-S are structurally separated under algebra-axis orthogonality and the convention-tag discipline matches the substrate-IS / laboratory-IN distinction.

Both cross-reviewers operate WITHOUT prior workshop context on the carve-out's authoring (read only this clause and cited rule-file references; do NOT receive the authoring plan-block transcript). Stage-2 PASS-AND requires ALL FOUR clauses (L1, L2, L3, L4) to PASS independently in BOTH cross-reviewer verdicts (logical AND, not OR); ANY clause FAIL routes the carve-out back to STAGE-1-CANDIDATE per the joint-theorem-promotion 4-stage pathway.

### Cross-link to PROHIBITED_ACTIONS Class 1 (boundary)

The L4 honesty-disclosure clause is the boundary between the structural extension and Class 1 (convention-shopping):

- Closure script emits `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` AND includes the Type-F / Type-S separation paragraph in its working-paper section → invoking the carve-out structurally; admissible under L1 ∧ L2 ∧ L3 ∧ L4.
- Closure script emits generic `convention=<scheme>` without the `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` suffix while silently performing Type-F partition closure → convention-shopping; PROHIBITED_ACTIONS Class 1 violation; gate FAILs at v3-closure-recovery audit; verdict line rejected at consolidator intake.

The carve-out is admissible-with-conditions: STRUCTURAL (L1-L3) + DISCIPLINARY (L4). Both must hold; either alone is insufficient.

### Audit-trail signature for carve-out invocations

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> \
  scheme=<plan-pinned scheme> \
  convention=<plan-pinned convention>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F \
  L_max=<plan-pinned L_max> \
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=S84+
```

The `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` convention-suffix is the audit-trail marker. `computations/_shared/_mechanical_closure_audit.py` greps for this suffix and verifies L4 compliance (working-paper Type-F / Type-S separation paragraph present + central-projection name cited). Absence of the suffix on a script that performs Type-F partition closure routes to PROHIBITED_ACTIONS Class 1 remediation.

**Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`. K-counter advancement is a structural property (one Type-F partition admissibility per instance), NOT narrative agreement. Calibration corpus pointer: `pru-class-corpus.md` (Layer-separability carve-out row; forward extension).

## When mechanical closure indicates a PLANNING DEFECT

If the closure script's covered-gate count ≥ `N_PLANNING_DEFECT_THRESHOLD = 4` of the wave's total gate count, the wave plan was OVER-OPTIMISTIC about prerequisite landings. This is a Class-8 PRU vulnerability at plan-authorship time: the planner should have routed the gates into a later wave conditional on prereq landing, rather than into the current wave with mechanical-closure deferral.

### Closing-paragraph-coherence disambiguation

The PLANNING DEFECT trigger fires on `covered_count ≥ N_PLANNING_DEFECT_THRESHOLD = 4` **INDEPENDENTLY** of item-1 status (the trigger is count-keyed, not conjunctive with item-1). This rule-section is structurally composed with `§"When mechanical closure IS acceptable"` item 1 — the per-closure admissibility predicate any acceptable closure must satisfy independently of count. The literal-independent reading is canonical; the strict-conjunctive reading admits a self-contradiction between FORBIDDEN-AT-AUTHORING-TIME and acceptable-AT-EXECUTION-TIME.

The closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson and adjust wave-partitioning policy to avoid recurrence.

**Status**: SUGGESTION at K=1. Sociological-metric K-counter framing (K=3 promotion is a signal that the count-keyed pattern recurred across 3 distinct sessions; rule operates as an accumulator). K may stay at 1 indefinitely if the SPLIT_REQUIRED heuristic at `/rclab-plan` operates as designed; the count-keyed audit remains operational regardless of MANDATORY status. Calibration corpus: `pru-class-corpus.md §13` (Corpus A row in the K-counter table) + `pru-class-corpus.md §14` (Closing-Paragraph-Coherence Audit Pattern EG1 — parent rule at `epistemic-discipline.md §"Pre-Registration Completeness"`).

## Audit-trail signature

Canonical verdict-line pattern for a mechanical closure:

```
{GATE_ID}: FAIL -- value='PRE-REG-INC_blocked_by_<sym1>_<status1>[_<sym2>_<status2>...]' \
  scheme=<plan-pinned scheme> convention=<plan-pinned convention> \
  L_max=<plan-pinned L_max> \
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=S84+
```

Companion comment row:

```
# audit_sha256 companion row: {GATE_ID} audit={short16} content={short16} \
# PRE-REG-INC per session-{N}-plan-w{W}.md §X; deferred to S{N+1}; \
# required prereqs: [<sym1>, <sym2>, ...]; \
# closure_script=computations/_shared/s{N}_w{W}_pre_reg_inc_closure.py
```

## Audit script

`computations/_shared/_mechanical_closure_audit.py` enforces this rule. Greps `s{N}_gate_verdicts.txt` canonical lines for the `value='PRE-REG-INC_blocked_by_*'` or `value='upstream_*'` patterns and verifies for each match:

  (i) the named upstream gate exists in the same file
 (ii) the named upstream gate's status matches what the closure value string asserts
(iii) the closure-line `audit_sha256` is unique across all canonical lines in the file
 (iv) the corresponding working-paper section has been updated (status != "NOT STARTED", verdict block populated, substrate framing block present)

Output: JSON report flagging any closure that fails (i)-(iv).

## Carry-forward script-bytes immutability (forward-looking hazard)

A closure script EDITED after emitting verdicts produces a `content_sha256` mismatch between the script-as-emitted and script-at-current-time. This does NOT invalidate the previously-emitted verdicts (the recorded SHAs are commitments to the script-state-at-emission-time), but it does break re-running the closure script as an audit-reproducibility tool.

**Mitigation** (forward-looking): after first execution, mechanical-closure scripts SHOULD be made read-only (`chmod -w` or filesystem-equivalent), OR a tagged immutable snapshot (`{script}.frozen-{audit_sha_short}.py`) should be committed alongside the verdict-file emission. The script's idempotent-recovery branch (parse-and-reuse of existing verdict-line SHAs) handles re-runs from this state.

## Cross-references

- `gate-verdicts.md` — verdict-line schema, dual-SHA pin.
- `v3-closure-recovery.md` — Stage 1/2/3 procedure, PROHIBITED_ACTIONS (Class 1 convention-shopping; Class 3 post-hoc plan editing; Class 4 ansatz-forced PASS).
- `agent-standards.md §"Completion Verification"` — the task-complete-lie failure mode this rule prevents.
- `epistemic-discipline.md §"Pre-Registration Completeness"` — PRU Class 8 framework; mechanical closure is the in-session honest reporting for upstream-blocked PRU-clear gates.
- `epistemic-discipline.md §"Layer-Decomposition"` — layer-functor `F` underpinning the carve-out's L1 condition.
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — Type-F (algebra-INVARIANT) vs Type-S (algebra-DEPENDENT) classification (MANDATORY at K=3).
- `joint-theorem-promotion.md §"Stage 2"` — two-agent cross-axis independent-verify protocol the carve-out's Stage-2 PASS-AND requirement instantiates.
- `phononic-framing.md §"IS Space, Not IN Space"` — substrate framing the carve-out preserves (Type-F observables are intrinsic-to-the-substrate single-summand traces, NOT laboratory-IN measurements).
- `feedback_rules-compensate-missing-structure.md` — K=3 promotion threshold under which the carve-out and Closing-paragraph-coherence sub-clauses harden from SUGGESTION to MANDATORY.
- `computations/_shared/_mechanical_closure_audit.py` — enforces the rule at audit time; greps verdict files for closure patterns + verifies upstream gate existence + working-paper update + SHA uniqueness.
