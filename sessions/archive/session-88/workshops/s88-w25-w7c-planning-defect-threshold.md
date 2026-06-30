# Session 88 Workshop W-25: sagan x gen-physicist

**Date**: 2026-05-08
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: sagan (sagan-empiricist), gen-physicist (gen-physicist)
**Source Documents**:
- `sessions/archive/session-88/session-88-w7c-workingpaper.md`
- `sessions/session-plan/session-88-plan-w7c.md`
- `sessions/archive/session-88/workshops/_seed-w7c.md`
- `.claude/rules/mechanical-closure-discipline.md`

**Focus Topics** (per schedule §W-25 invocation —`session-88-workshop-schedule.md` line 402):

1. **Rule-trigger reading**: Is the `N_PLANNING_DEFECT_THRESHOLD ≥ 4` rule a SUFFICIENT condition for planning-defect (synthesis §2 reading: count alone) or NECESSARY-but-not-sufficient (gen-physicist reading: count AND prereq-blocks were NOT pre-registered)?
2. **Pre-registration anticipation**: Does explicit pre-registration in plan §"Wave 7c Decision Point Prerequisites" lines 23-31 (each prereq listed with blocked-by routing rule) constitute "anticipation" that cancels the planning-defect signal — or is the relevant signal "wave was scheduled before its prereqs were ready" regardless of plan-author awareness?
3. **Rule-file edit required**: If both readings agree the threshold fires, what RULE-FILE EDIT disambiguates trigger-condition for future calibration-corpus instances? Does the rule need a NEW clause "anticipated-and-pre-registered prereq-blocks DO NOT count toward N_PLANNING_DEFECT_THRESHOLD"?
4. **K-counter status of W7c**: Per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, if W7c counts as instance #1 the rule will harden at K=3; if NOT, the K-counter stays at 0 — is that the right outcome given W7c's structural content (forward-pinned follow-ups to SCHEMATIC FAIL whose prereq landings were KNOWN-queued)?
5. **Forward template for plan-authors**: When SHOULD forward-pinned follow-up waves be SPLIT (machinery-landing W6 + cross-review W7) vs when single-wave forward-pinning structurally clean?

**Cross-cutting**: Substrate framing of "planning-defect" — does the metaphor live at the methodology layer (substrate-IS plan structural property) or at the organizational layer (plan-author behavioral property)?

---

## Round 1 — sagan: Opening Analysis

### S1: Rule-trigger reading (sufficient-condition vs necessary-and-anticipation-test)

**Position**: The rule-text of `mechanical-closure-discipline.md §"When mechanical closure indicates a PLANNING DEFECT"` (lines 274-286) states a SUFFICIENT condition. Count alone fires it. The "anticipation cancels" clause that gen-physicist will argue from is not in the text — it would be a NEW rule extension, not a reading of the current rule.

**Substitution chain (rule-text reading, no quantitative claim)**:

```
Step 1 (Definition):
  rule_predicate(W) := closure_script(W).covered_gate_count
                       >= N_PLANNING_DEFECT_THRESHOLD
  N_PLANNING_DEFECT_THRESHOLD := 4 (pinned in rule body line 277)
  rule_consequent(W) := "wave plan W was OVER-OPTIMISTIC about
                         prerequisite landings"
  rule_form := "if rule_predicate(W) then rule_consequent(W)"
               (literal "If ... then" syntax at lines 276-281)

Step 2 (Substitution at W = W7c):
  closure_script(W7c).covered_gate_count = 4
    (verdict file lines 238/241/244/247 + 250/253/256/259/262/265
     for the four gate-IDs #84, #85, #86, #167; WP §1 outcome
     table lines 866-869 confirms 3-of-4 full PRE-REG-INC + 1-of-4
     partial-PRE-REG-INC = 4 covered gates)
  4 >= 4 = True
  rule_predicate(W7c) = True

Step 3 (Simplification):
  rule_consequent(W7c) follows by modus ponens.
  No additional clause in lines 274-286 conditions the consequent
  on plan-author awareness, anticipation status, or whether
  upstream-block topology was pre-registered. The text is a
  bare conditional on the count.

Step 4 (Direction):
  The trigger fires on the structural property
  (count >= threshold), not on the plan-authoring history
  (anticipated vs unanticipated). An "anticipation cancels"
  reading requires INSERTING a missing premise — i.e., reading
  the rule as
     "if rule_predicate(W) AND not anticipated(W) then
      rule_consequent(W)"
  — which is not the form the rule takes.

Conclusion:
  Sufficient-condition reading is the literal reading.
  The W7c synthesis (§2 lines 873-881; §9 line 1006; §"Constraint-Map
  Updates" line 1020) applied this reading correctly. Calibration-
  corpus instance #1 status follows from the rule as written.
```

**Source-doc evidence**:

- `mechanical-closure-discipline.md` lines 276-281: "**If** the closure script's covered-gate count ≥ N_PLANNING_DEFECT_THRESHOLD (pin: 4) of the wave's total gate count, the wave plan was OVER-OPTIMISTIC about prerequisite landings." Bare conditional. No "and was unanticipated" qualifier.
- WP §"1. Wave-level outcome" lines 866-869: 4 gates covered, 3-of-4 full PRE-REG-INC + 1-of-4 partial — count is 4 by direct enumeration of the outcome table.
- WP §"2. Plan-authoring discipline" line 877: "W7c's 4-of-4 prereq-block pattern (3× full PRE-REG-INC + 1× partial) hits the threshold exactly."
- WP §"9. Session classification" line 1006: "DID trigger the planning-defect threshold (4-of-4 prereq blocks) — `mechanical-closure-discipline.md §"When mechanical closure indicates a PLANNING DEFECT"` calibration-corpus instance #1."

**Structural implication**: The SUFFICIENT/NECESSARY distinction is not symmetric in the empiricist's reading. A NECESSARY-and-additional-test reading is a STRENGTHENING of the rule (it admits FEWER triggers), and rule-strengthenings to a published rule require explicit pre-registration. Reading-in an unwritten anticipation-cancels clause AFTER the synthesis already declared instance #1 status is structurally a Class-3 PROHIBITED_ACTIONS analog at the rule-file layer (post-hoc rule editing in response to a verdict already on disk).

**Note on §"When mechanical closure IS acceptable" item 1**: That clause says the producing closure script is CLEAN AT EXECUTION TIME if the plan pre-registered the upstream-block topology. The §"PLANNING DEFECT" clause ALSO says (line 282-286) "the closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson." The two clauses are NOT redundant — one says "the script is acceptable", the other says "the plan was over-optimistic". A plan that pre-registers prereq-block routing for FOUR gates is BOTH (i) executing clean mechanical closure AND (ii) signaling that the wave was scheduled with prereqs unready. Both readings hold simultaneously. Item 1 of §"IS acceptable" is an EXECUTION-LAYER predicate; the §"PLANNING DEFECT" clause is a PLAN-LAYER predicate. They live at different layers of the layer-functor F decomposition.

### S2: Pre-registration anticipation status — methodology-IS observable, not psychology container

**Position**: The relevant signal "the wave was scheduled before its prereqs were ready" is a STRUCTURAL property of the plan-as-artifact-on-disk. Documented anticipation in plan §"Wave 7c Decision Point Prerequisites" lines 23-31 records WHAT the plan author KNEW; it does not change the empirical fact that four gates were scheduled in W7c whose machinery+data prerequisites had not yet landed. Knowledge of the failure mode is not the same as preventing it.

**Substrate-framing analogy (per `phononic-framing.md` §"IS Space, Not IN Space")**: A "planning defect" is a methodology-layer-IS observable on the plan artifact, not a plan-author-psychology container observable. The plan IS the structural artifact; whether the author "anticipated" the prereq-block scenario is an organizational-layer property, not a methodology-layer-IS property. This is the same distinction the framing rule enforces between substrate-IS observables (intrinsic to the spectral triple) and laboratory-IN observables (measured in a continuum container). Plan-author awareness lives in a "container" (the author's mental state); the plan structure lives at the methodology layer (a file on disk with concrete gate-IDs and prereq routings).

**Direct empirical reading**:

- The plan §"Wave 7c Decision Point Prerequisites" line 30: "if absent, route #84 to PRE-REG-INC blocked-by-S88-PV-PIPELINE-LANDING."
- The plan §line 31: "if absent, route #85 to PRE-REG-INC blocked-by-S88-CHEEGER-SIMONS-MACHINERY."
- Plan §line 33: "If any prerequisite fails verification at dispatch time, the producing script emits PRE-REG-INC..."

These three sentences anticipate the VERY FAILURE MODE the rule fires on. The author KNEW the prereqs might be absent. They were absent. The wave was scheduled anyway. That is precisely the structural property "OVER-OPTIMISTIC about prerequisite landings" describes — the plan anticipated the failure path AND scheduled the wave anyway. The anticipation is itself evidence of awareness of the planning defect, not a cancellation of it.

**Cross-reference to §"When mechanical closure IS acceptable" item 1** (rule lines 25-31): The rule explicitly states pre-registration is REQUIRED for mechanical-closure execution to be honest at execution time. It does NOT state that pre-registration EXEMPTS the plan from the planning-defect diagnostic. These are independent predicates:

| Layer | Predicate | W7c status |
|:------|:----------|:-----------|
| EXECUTION layer | "closure script honestly emits PRE-REG-INC iff plan pre-registered prereq-block routing" (item 1) | PASS — all 4 gates emitted PRE-REG-INC honestly per the rule |
| PLAN layer | "wave plan was over-optimistic iff covered_count >= N_PLANNING_DEFECT_THRESHOLD" (§PLANNING DEFECT) | TRIGGERED — count = 4, threshold = 4 |

Both predicates fire simultaneously and consistently. The plan is honest at execution time AND was over-optimistic at scheduling time. Reading the two clauses as mutually-cancelling collapses the layer distinction — it treats item 1's EXECUTION-layer admissibility as if it were also PLAN-layer exoneration.

**Empirical analogue (Sagan voice)**: This is the same epistemic move as a weather forecaster who, knowing the radar shows a storm cell incoming, schedules a parade for an hour later, posts a "if rain occurs, the parade is cancelled" sign, and then claims the parade was not poorly scheduled because the cancellation contingency was pre-registered. The "if it rains" sign documents that the forecaster KNEW. The schedule was made anyway. The structural fact is: a parade was put on the calendar with rain forecast. Whether the forecaster knew in advance changes nothing about whether the scheduling was sound.

**Source-doc evidence — the plan IS the over-optimism**:

- Plan §"Wave 7c Summary" line 18 enumerates 4 gates totaling 3.8 wave-equivalents of effort BUDGET against prereqs that lines 23-31 explicitly mark as potentially absent. The budget itself reflects expectation that the wave would execute substantively.
- WP §"8. Carry-forwards" lines 934-996 enumerates 10 carry-forwards totaling ~5.6 wave-equivalents — 1.5× the W7c budget. The S89 effort-debt this generates is the empirical signature of the over-optimism. If W7c had been correctly partitioned (machinery W6 + cross-review W7), the carry-forward queue would not exist; the work would already be in S88's wave sequence.

**Pose to gen-physicist**: If documented anticipation cancels the planning-defect trigger, what is the operational signature that distinguishes a "well-scheduled forward-pinned wave" from a "wave scheduled before its prereqs were ready"? Both look identical at execution time (both pre-register PRE-REG-INC routing). The only structural difference is the COUNT of covered gates, which is exactly what the rule already pins. Inserting an "anticipation cancels" clause would make the rule unfalsifiable: any plan that hits the threshold can claim anticipation, and the rule has no further structural test to apply.

### S3: Rule-file edit requirement — affirm count-alone, do NOT add anticipation-cancels

**Position**: A rule-file edit IS warranted, but NOT the "anticipation-cancels" clause that the seed Workshop-2 question (c) (`_seed-w7c.md` line 30) raises as a candidate. The correct edit is an AFFIRMING clause that pins the sufficient-condition reading explicitly, plus a CALIBRATION-CORPUS table, plus an explicit cross-link to `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold so future calibration-corpus instances are tracked structurally rather than re-litigated per session.

**Why NOT add an anticipation-cancels clause** (the structural argument):

1. **Falsifiability collapse** (per `epistemic-discipline.md §"Falsifiability"` — every claim must state what would refute it). An anticipation-cancels clause has no falsification criterion. ANY plan that hits the threshold can claim its prereq-blocks were "anticipated" by pointing to a §"Decision Point Prerequisites" subsection. The clause would be vacuous in practice.

2. **Class-3 PROHIBITED_ACTIONS adjacency** (per `v3-closure-recovery.md §PROHIBITED_ACTIONS Class 3` — post-hoc pre-registration editing). The synthesis at WP §"9. Session classification" line 1006 ALREADY declared instance #1 status. Editing the rule's trigger condition AFTER the verdict was emitted to retroactively exempt W7c is the rule-layer F-image of post-hoc threshold editing. The image of Class 3 under the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`) is "post-hoc rule-text editing in response to a session's verdict already on disk."

3. **K-counter-reset hazard**. If anticipation cancels, the K-counter never advances on cleanly-pre-registered forward-pinned waves — but those are exactly the waves that produce calibration-corpus signal. The rule would advance only when planners FAIL to pre-register prereq-block routing (i.e., when they ALSO violate §"IS acceptable" item 1). This makes the §"PLANNING DEFECT" clause structurally redundant with item 1's converse, and the K=3 promotion threshold becomes effectively unreachable.

4. **Structural diagnostic destroyed**. The point of the §"PLANNING DEFECT" clause is to detect when a wave was scheduled with too many unmet prereqs, regardless of whether the planner saw it coming. Knowing the ship is going to hit the iceberg does not make hitting the iceberg good navigation. The rule exists to pin the navigation defect, not to credit anticipatory awareness.

**Proposed edit** (affirming sufficient-condition reading, with calibration-corpus structure):

```
### When mechanical closure indicates a PLANNING DEFECT

If the closure script's covered-gate count >= N_PLANNING_DEFECT_THRESHOLD
(pin: 4) of the wave's total gate count, the wave plan was OVER-OPTIMISTIC
about prerequisite landings.

[NEW] **Trigger condition is a SUFFICIENT condition on the structural
property (count). The trigger fires regardless of whether the
prereq-blocks were anticipated and pre-registered in the plan's
"Decision Point Prerequisites" section. Pre-registration of prereq-block
routing per §"When mechanical closure IS acceptable" item 1 makes the
closure script HONEST AT EXECUTION TIME, but DOES NOT EXEMPT the plan
from the planning-defect diagnostic. The two clauses operate at
different layers of the layer-functor F decomposition (per
`epistemic-discipline.md §"Layer-Decomposition"`): item 1 is the
EXECUTION-layer predicate; this clause is the PLAN-layer predicate.
Both can fire simultaneously and consistently on the same wave.**

The closure script remains acceptable AT EXECUTION TIME (preserving the
audit trail honestly), but the next session's planner MUST log this as
a plan-authorship lesson and adjust wave-partitioning policy to avoid
recurrence.

[NEW] **Calibration corpus** (per `feedback_rules-compensate-missing-structure.md`
K=3 promotion threshold; status: SUGGESTION at K=1, hardens to MANDATORY
at K=3):

| # | Source | covered_gates | total_gates | covered_fraction | Status |
|:-:|:-------|:-------------:|:-----------:|:----------------:|:-------|
| 1 | S88 W7c (4-of-4 prereq cluster) | 4 | 4 | 1.00 | INSTANCE-#1 |
| 2 | reserved for next K-advancing wave | -- | -- | -- | pending |
| 3 | reserved for next K-advancing wave | -- | -- | -- | pending |

K-counter advancement is a structural property (one prereq-cluster
trigger per instance) NOT narrative agreement. K = 3 promotes status
to MANDATORY; until then the clause is SUGGESTION-status with
in-session lesson-logging.
```

**Substitution-chain check on the edit's status pin** (no quantitative claim — purely a counter):

```
Step 1 (Definition):
  K_promotion := 3 (per feedback_rules-compensate-missing-structure.md)
  K_W7c := count of structurally-distinct calibration corpus instances
           of "covered_count >= 4" trigger
Step 2 (Substitution):
  K_W7c = 1 (W7c is the first such instance per WP §9 line 1006)
Step 3 (Simplification):
  K_W7c = 1 < K_promotion = 3
Step 4 (Direction):
  Status := SUGGESTION (NOT MANDATORY)
Conclusion:
  The edit lands the clause at SUGGESTION-status with calibration-corpus
  table pre-registered for instances #2 and #3.
```

**Cross-link to existing rule patterns**: This is structurally identical to the layer-separability carve-out at `mechanical-closure-discipline.md` lines 59-272 (rule lines 177-195) which is itself "SUGGESTION at K=1" with a 3-row corpus table. The §"Layer-separability carve-out" rule is already template for this kind of K=1→K=3 calibration-corpus tracking. The §"PLANNING DEFECT" clause should adopt the same template.

**What the edit does NOT need**:

- It does NOT need to redefine the threshold (the pin "4" stands).
- It does NOT need to add an anticipation-cancels clause.
- It does NOT need to remove the EXECUTION-layer/PLAN-layer distinction (that distinction is what makes the rule consistent with item 1).
- It does NOT change W7c's status as instance #1.

The edit's purpose is preventive: pin the sufficient-condition reading explicitly so future calibration-corpus instances are not re-litigated session by session.

### S4: W7c K-counter status — accept as instance #1

**Position**: W7c IS calibration-corpus instance #1 of the §"PLANNING DEFECT" trigger. This is the right outcome empirically; it is the right outcome rule-textually; and it is the right outcome epistemically. The exempt-by-pre-registration alternative would be a methodology-floor regression.

**Substitution chain (K-counter arithmetic, no quantitative claim beyond integer counting)**:

```
Step 1 (Definition):
  K_promotion := 3
    (per feedback_rules-compensate-missing-structure.md;
     see precedent at mechanical-closure-discipline.md
     §"Layer-separability carve-out" lines 177-195 which uses
     identical K=1→K=3 promotion structure)
  K_planning_defect := count of structurally-distinct
    calibration-corpus instances of (covered_gate_count >=
    N_PLANNING_DEFECT_THRESHOLD) trigger, post-rule-landing

Step 2 (Substitution at session-end S88):
  Pre-W7c instances: 0
    (rule landed at S86 W3 6/6 PRE-REG-INC closure; provenance
     line 3-5 of mechanical-closure-discipline.md; no triggers
     between S86 W3 and S88 W7c)
  W7c instance: 1
    (4-of-4 covered, count = 4 >= threshold = 4; verified S1
     above via direct enumeration; WP §9 line 1006; WP
     §Constraint-Map Updates line 1020)
  K_planning_defect = 0 + 1 = 1

Step 3 (Simplification):
  K_planning_defect = 1 < K_promotion = 3

Step 4 (Direction):
  Status := SUGGESTION (NOT MANDATORY)
  Promotion event: NOT triggered

Conclusion:
  W7c counts as instance #1. Calibration corpus opens with one
  filled row + two reserved rows. K-counter advances from 0 to 1.
  Status remains SUGGESTION. Forward template: instances #2 and
  #3 require the SAME structural trigger (covered_count >= 4)
  on a structurally-distinct wave to advance K. Promotion to
  MANDATORY at K = 3.
```

**Why exempt-by-pre-registration is the WRONG outcome**:

1. **K-counter dies-on-arrival**. If pre-registered prereq-block routing exempts a wave, then by the converse of `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1, ANY wave that fires the §"PLANNING DEFECT" trigger WITHOUT pre-registration is ALREADY violating item 1 (post-hoc plan editing, PROHIBITED_ACTIONS Class 3). The §"PLANNING DEFECT" clause becomes a logical impossibility: it can only fire on plans that are simultaneously violating item 1, and those plans should be rejected at plan-freeze BEFORE the wave executes. The K-counter has no observation window. The rule never advances. K_promotion = 3 is unreachable BY CONSTRUCTION.

2. **The published rule has been on disk since S86 W3 (2026-04-26)** and produced ZERO calibration-corpus instances over S86 + S87 + S88 W1-W6 — until W7c. Refusing instance #1 status sets the K-counter back to zero with no path forward. This is the methodology-floor analog of refusing observational evidence on the grounds that it could in principle be re-classified as something else. Under Sagan-empiricist standards, that is the move that produces unfalsifiable rules. (`epistemic-discipline.md §"Falsifiability"`: "If no observation could falsify the claim, it is not science.")

3. **The synthesis already declared instance #1 status**. WP §"Constraint-Map Updates" line 1020:
   > "2026-05-05 | `mechanical-closure-discipline.md §"When mechanical closure indicates a PLANNING DEFECT"` N_PLANNING_DEFECT_THRESHOLD=4 | RULE EXISTS, 0 calibration corpus instances | RULE WITH calibration corpus instance #1 (W7c 4-of-4 prereq cluster) | First substantive trigger of the planning-defect threshold; lesson documented in §2 above"

   And WP §"9. Session classification" line 1006:
   > "DID trigger the planning-defect threshold (4-of-4 prereq blocks) — `mechanical-closure-discipline.md §"When mechanical closure indicates a PLANNING DEFECT"` calibration-corpus instance #1."

   And WP §"7. Downstream implications" line 930:
   > "Plan-authoring discipline | 4-of-4 prereq blocks at dispatch time → planning-defect threshold trigger | S89 plan-author MUST sequence machinery + data landings BEFORE cross-review verify gates; calibration-corpus instance #1 of `mechanical-closure-discipline.md` N_PLANNING_DEFECT_THRESHOLD"

   Three independent sites in the WP synthesis declare instance #1 status. Demoting that declaration retroactively is the rule-layer F-image of post-hoc threshold editing (Class 3 PROHIBITED_ACTIONS analog at the methodology layer per `epistemic-discipline.md §"Layer-Decomposition"`).

4. **The 10-item carry-forward queue is the empirical signature of the planning defect**. Total carry-forward effort ≈ 5.6 wave-equivalents = 1.5× the W7c wave budget itself (WP §8 line 996). Half of those carry-forwards (CF #1, #3, #5, #7, #8) are W6-equivalent machinery + data landings that should have preceded the W7c gates. The carry-forward queue is the displaced W6 work the plan-author should have scheduled in W6, not in W7c. This is the structural definition of "OVER-OPTIMISTIC about prerequisite landings" — the plan budgeted W7c to execute substantively, the wave instead generated a deferred work queue 1.5× its own size, and that queue IS the lesson the §"PLANNING DEFECT" clause exists to surface.

**Forward implication**: K = 1 is the correct counter state. S89 plan-author has explicit operational guidance per WP §"Next-step routing" line 1042: "sequence machinery + data landings (carry-forwards 1, 3, 5, 7, 8) as W6-equivalent prerequisites BEFORE re-dispatching the cross-review verify gates (carry-forwards 2, 4, 6, 9)." If S89 follows that guidance, no §"PLANNING DEFECT" trigger fires in S89, and the K-counter stays at 1 — which is exactly the correct outcome (the rule has done its job: documented the defect, prevented recurrence, K stays where it should pending another instance).

**Pose to gen-physicist**: If the K-counter does not advance on W7c, what session-specific structural property would advance it? Name a hypothetical W7c-prime that WOULD count as instance #1 under your reading. If your answer requires absent prereq-block routing pre-registration (i.e., the §"IS acceptable" item 1 violation), then your reading collapses §"PLANNING DEFECT" into the converse of item 1 and the K=3 promotion threshold is structurally unreachable.

### S5: Forward template — split when prereq-block routings approach the threshold

**Position**: A forward-pinned follow-up wave SHOULD be split into a machinery-landing W{N} + cross-review W{N+1} pair when the count of pre-registered prereq-block routings (the count of plan §"Decision Point Prerequisites" items that route to PRE-REG-INC if absent) approaches or hits N_PLANNING_DEFECT_THRESHOLD = 4. The empirical signal is structural and observable AT PLAN-FREEZE TIME, before any dispatch fires.

**Discriminator** (operational; pin candidates for plan-freeze auditor):

```
Define at plan-freeze time, on a candidate wave W:
  PB(W) := count of items in W's "Decision Point Prerequisites"
           section that route a wave-W gate to PRE-REG-INC if the
           prereq is absent at dispatch time
  G(W)  := total covered-gate count of W
  PB_frac(W) := PB(W) / G(W)

Decision rule (proposed for plan-author auditor):
  if PB(W) >= N_PLANNING_DEFECT_THRESHOLD = 4:
    SPLIT_REQUIRED (W is at the threshold by construction)
  elif PB(W) >= 0.50 * N_PLANNING_DEFECT_THRESHOLD = 2 and PB_frac(W) >= 0.50:
    SPLIT_RECOMMENDED (the wave's prereq-load is half-or-more of
      the trigger threshold AND half-or-more of the wave's gates
      are prereq-conditional)
  else:
    SINGLE_WAVE_OK (forward-pinning is structurally clean)
```

**Substitution-chain check at W = W7c**:

```
Step 1 (Definition):
  PB(W7c) := count of plan §"Wave 7c Decision Point Prerequisites"
             items routing to PRE-REG-INC
  G(W7c)  := total W7c covered-gate count

Step 2 (Substitution at W7c):
  PB(W7c) = 4
    (plan lines 23-31: PV pipeline #4, Cheeger-Simons #5, GV-Heitsch
     implicit, observable-2/3 data implicit; verified at WP §2
     line 875 "ALL FOUR machinery/data prerequisites were absent")
  G(W7c) = 4
    (plan §summary table lines 13-17 enumerates 4 gates)
  PB_frac(W7c) = 4/4 = 1.00

Step 3 (Simplification):
  PB(W7c) = 4 >= 4 = N_PLANNING_DEFECT_THRESHOLD
  Decision rule branch taken: SPLIT_REQUIRED

Step 4 (Direction):
  W7c was a SPLIT_REQUIRED wave. The plan ran it as single-wave
  forward-pinning instead. Calibration-corpus instance #1 fires.

Conclusion:
  W7c is the prototype case for SPLIT_REQUIRED diagnosis at
  plan-freeze. The forward template is: when PB(W) >= 4, split
  to W{N} (machinery landings) + W{N+1} (cross-review verify).
```

**The empirical signal at plan-freeze**: It is NOT in the plan-author's mental state. It is in the plan document on disk. Specifically:

1. **Count of prereq items in the "Decision Point Prerequisites" section.** This is greppable. Plan authors do not need to introspect; the auditor counts items.
2. **Each prereq item's blocked-by symbol.** Each blocking symbol points to a machinery-or-data landing that does not yet exist. Listing 4 of these is structurally incompatible with single-wave execution.
3. **Wave-effort budget vs carry-forward budget ratio.** When the carry-forward total approaches or exceeds the wave's own effort budget, the wave is structurally a deferred-work-queue generator, not a substantive-execution wave. WP §8 line 996 measures this ratio at 1.5× for W7c (5.6 wave-equiv carry-forward against 3.8 wave-equiv W7c budget). The ratio is observable POST-WAVE; the structural cause (4 absent prereqs) is observable AT PLAN-FREEZE.

**Proposed extension to `mechanical-closure-discipline.md`** (additional clause at end of §"PLANNING DEFECT"):

```
### Forward template — split discriminator at plan-freeze

A forward-pinned follow-up wave W with PB(W) >= 4 (count of
"Decision Point Prerequisites" items routing to PRE-REG-INC)
is at the planning-defect threshold BY CONSTRUCTION at
plan-freeze time. Plan authors MUST split such waves into:

  - W{N}_machinery: the machinery + data landings for ALL
    prereqs in PB(W). Pre-register PASS criteria as
    "module callable" / "data file exists with substrate-IS
    bit-stationarity" / etc. (no cross-review verify gates).
  - W{N+1}_verify: the cross-review verify gates that consumed
    the prereqs. Pre-register PB(W{N+1}) = 0 (no Decision Point
    Prerequisites section is required because all prereqs
    landed in W{N}).

For 2 <= PB(W) < 4 with PB_frac(W) >= 0.50, splitting is
RECOMMENDED but not MANDATORY; plan authors document the
single-wave forward-pinning rationale at plan-freeze
(specifically: which prereq landings are expected to land
in-session, and from which upstream gate).

For PB(W) < 2 OR PB_frac(W) < 0.50, single-wave forward-pinning
is structurally clean.
```

**Why W7c was the wrong shape (concrete diagnosis)**:

- Plan §summary line 18 budgeted W7c at 3.8 wave-equivalents.
- 4 of 4 covered gates had absent prereqs at dispatch time.
- WP §8 lines 936-994 enumerated 10 carry-forwards totaling 5.6 wave-equivalents.
- 5 of those 10 carry-forwards (CF #1, #3, #5, #7, #8) are machinery + data landings that should have preceded the cross-review gates. They total 0.8 + 0.4 + 0.6 + 0.3 + 0.3 = 2.4 wave-equivalents.
- The remaining 5 carry-forwards (CF #2, #4, #6, #9, #10) are the cross-review re-runs after the machinery lands, totaling 0.5 + 0.8 + 0.6 + 1.0 + 0.3 = 3.2 wave-equivalents.
- A correctly-split sequence would have been: W7c-machinery (2.4 wave-equiv) producing the 5 missing modules + data, then W7c-verify (3.2 wave-equiv) producing the 4 substantive cross-review gates. Total 5.6 wave-equiv — the same as the carry-forward queue. The work was not eliminated; it was DEFERRED.

**Pose to gen-physicist**: Under your "anticipated prereq cluster is structurally clean" reading, what is the operational signal that triggers SPLIT_REQUIRED at plan-freeze? If anticipation cancels, plan-authors have no rule to consult. They will keep producing W7c-shaped waves indefinitely. The empirical evidence at plan-freeze (the count of prereq-block routings) is the only observable that fires before the wave executes. Any forward template that does not key on that count cannot prevent recurrence.

### S6: Cross-Cutting Observations — substrate framing of "planning-defect"

**The "planning-defect" is a methodology-layer-IS observable, not an organizational-layer-IN observable.**

This is the same epistemic structure as the substrate-IS / laboratory-IN distinction in `phononic-framing.md §"IS Space, Not IN Space"`, transported under the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`) from the substrate ↔ laboratory pair to the methodology ↔ organization pair. The error pattern that gen-physicist will run on this question is the rule-layer image of container-thinking on the substrate side.

**Layer-functor F image table** (extends `epistemic-discipline.md §"F at substrate ↔ methodology pair"`):

| Substrate-IS (physics layer) | Methodology-IS (rule layer; under F) |
|:----------------------------|:-------------------------------------|
| eigenvalue of D_K | trigger predicate of a rule clause |
| numerical PASS predicate | artifact-existence predicate (covered_count >= threshold) |
| machinery pin | input-pin map of a plan gate-block |
| substrate IS the spectral triple | plan IS the gate enumeration on disk |
| "particles created IN curved spacetime" (WRONG) | "planning defect IN the plan-author's mental state" (WRONG) |
| "fiber spectrum reorganizes at the fold" (RIGHT) | "plan structurally over-schedules prereq-conditional gates" (RIGHT) |

**Direction of explanation** (per `phononic-framing.md` §"IS Space, Not IN Space"):

```
Plan artifact (the .md file on disk; gate-IDs + prereq-routings)
   IS the planning-defect-eligible structure
   →  Methodology-rule trigger predicate
      (count(prereq-block routings) >= threshold)
   →  Plan-authoring discipline lesson
      (next-session planner sequences W6 + W7 split)
```

Inverting this — placing the plan-author's psychology as fundamental and the on-disk plan structure as derived — is a container-thinking violation at the methodology layer. The author's awareness of the prereq-block scenario is downstream of the on-disk enumeration; "anticipation" is the plan-author's PERCEPTION of the structural property, not the structural property itself.

**The §"PLANNING DEFECT" clause is a structural diagnostic over the plan artifact.** Its predicate (count >= 4) reads the plan structure directly. It does not read the plan-author's notes, comments, "Decision Point Prerequisites" anticipation language, or any other layer of plan-author commentary. Those are organizational-layer-IN content. The trigger fires on methodology-IS content (the count of covered gates, which is a function of the plan as enumerated artifact).

**Why this matters for the K-counter**: A K-counter that advances on methodology-IS observations is a structural diagnostic. A K-counter that advances only on organizational-IN failures (plan-authors who fail to pre-register prereq-block routing) tracks plan-author behavior, not plan structure. The framework already has organizational-layer rules that police pre-registration discipline (`epistemic-discipline.md §"Pre-Registration Completeness"`, `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1). The §"PLANNING DEFECT" clause exists precisely to catch the structural failure mode that DOES NOT manifest as a pre-registration violation — it catches the case where pre-registration was scrupulous AND the wave was still over-scheduled. That is W7c.

**Cross-link to PROHIBITED_ACTIONS Class 3 at the methodology layer**: Per `v3-closure-recovery.md §PROHIBITED_ACTIONS Class 3`, post-hoc pre-registration editing is forbidden at the EXECUTION layer. The layer-functor F image of Class 3 is post-hoc rule-text editing in response to an on-disk verdict. The W7c synthesis declared instance #1 status at three sites in the WP (lines 881, 1006, 1020). Reading-in an "anticipation cancels" clause AFTER the verdict was emitted retroactively exempts W7c from the K-counter — that is the rule-layer F-image of Class 3. The substrate-layer prohibition on post-hoc threshold editing transports to the methodology layer as a prohibition on post-hoc rule-text editing in response to a calibration-corpus instance already on disk.

**Substrate framing applied to "anticipation"**: "Did the plan-author anticipate the prereq-block scenario?" is a container question — it presupposes a container (the author's mental state) inside which anticipation occurs. The substrate-IS reframe: "Does the plan artifact ENUMERATE prereq-block routing for >= 4 covered gates?" YES, it does (plan §lines 23-31). That enumeration IS the planning defect made structurally visible. The wave was scheduled with prereq-blocks routed for 4 of 4 gates. The plan IS the over-optimism, made manifest on disk.

**One-line summary for the verdict table**: Planning-defect is a methodology-IS observable on the plan artifact; the trigger fires on the on-disk count of prereq-block routings; plan-author awareness is downstream of the structural property and does not change it.

### S7: Questions for gen-physicist

These questions focus on the four adjudication-clauses (a)/(b)/(c)/(d) of the spawn prompt's Workshop 2 statement.

**Q1 (clause (a) — sufficient vs necessary)**: Read the literal text of `mechanical-closure-discipline.md §"When mechanical closure indicates a PLANNING DEFECT"` lines 276-281. Where in those six lines do you locate the textual basis for an "anticipation cancels" qualifier? The rule-text reads "If the closure script's covered-gate count >= N_PLANNING_DEFECT_THRESHOLD ... the wave plan was OVER-OPTIMISTIC about prerequisite landings." It is a bare "If P then Q" conditional on the count. Cite the specific token or phrase you read as conditioning the consequent on plan-authoring history (not item 1 of §"IS acceptable" — that clause governs EXECUTION-layer admissibility, a different predicate at a different layer per the layer-functor F decomposition). If no token in lines 276-281 carries that conditioning, your reading is a rule extension, not a rule reading.

**Q2 (clause (b) — falsifiability of "anticipation cancels")**: Suppose I grant your reading: count >= 4 AND prereq-blocks were UNANTICIPATED ⇒ planning-defect. State a falsifier. What concrete W7c-prime plan structure would FAIL "anticipation cancels" — i.e., name a hypothetical plan that hits count = 4 AND that you would still classify as planning-defect under your reading. If your falsifier requires the plan-author to have OMITTED a "Decision Point Prerequisites" section (i.e., violating §"IS acceptable" item 1 outright), then your "anticipation cancels" reading collapses §"PLANNING DEFECT" into the converse of item 1. The §"PLANNING DEFECT" clause has no independent observation window, the K-counter is structurally unreachable, and `feedback_rules-compensate-missing-structure.md` K=3 promotion never fires for this rule. Address this collapse directly.

**Q3 (clause (c) — concrete rule-file edit text)**: If you maintain that an "anticipation cancels" clause should be added, write the EXACT text you would insert at line 282 of `mechanical-closure-discipline.md`. Include the falsifier from Q2. Then test your text on TWO hypothetical waves:
- (i) a 4-gate wave with all 4 prereq-blocks pre-registered in §"Decision Point Prerequisites" (W7c shape);
- (ii) a 4-gate wave with NO §"Decision Point Prerequisites" section (which is already a §"IS acceptable" item 1 violation routed to plan-freeze halt per `epistemic-discipline.md` §"Pre-Registration Completeness" Class 8).

If your clause classifies (i) as exempt and (ii) as planning-defect, but (ii) is ALREADY rejected at plan-freeze (so it never produces a closure script and never reaches the §"PLANNING DEFECT" trigger), then your clause selects an empty set. That is the K-counter-death-on-arrival argument from S4.

**Q4 (clause (d) — K-counter consequence)**: Per S4 substitution-chain, K_planning_defect = 1 if W7c counts; K_planning_defect = 0 if W7c is exempted. Per `feedback_rules-compensate-missing-structure.md`, K_promotion = 3. Under your reading, when does the rule promote to MANDATORY status? Name a session-shape that would advance the K-counter without violating §"IS acceptable" item 1. If you cannot name one, your reading effectively retires the rule. Is that the intended outcome? If yes, propose deletion of the §"PLANNING DEFECT" clause outright (cleaner than retaining a clause that can never advance). If no, your reading needs modification to allow a non-empty observation window.

**Q5 (substrate framing — layer-functor F)**: Per S6, "planning defect" is a methodology-IS observable on the plan artifact (count of covered gates with absent prereqs at dispatch time). "Anticipation" is an organizational-IN observable on plan-author behavior (whether they pre-registered prereq-block routing in the plan's §"Decision Point Prerequisites" subsection). These live at different layers of the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`). A K-counter that advances on methodology-IS structural properties is a structural diagnostic; a K-counter that advances only on organizational-IN behavioral failures (i.e., when plan-authors violate item 1) is redundant with item 1 itself. Address: which K-counter is the §"PLANNING DEFECT" clause designed to be — structural (methodology-IS, count-keyed) or behavioral (organizational-IN, item-1-violation-keyed)? If the latter, what does §"PLANNING DEFECT" add beyond the existing item-1 enforcement at plan-freeze?

---

## Round 1 — gen-physicist: Response & Cross-Synthesis

### Part 1: Response to sagan's Sections

#### Re: S1 — Rule-trigger reading

**AGREE** with sagan's S1 framing of the literal text as an `If P then Q` syntactic shape. Sagan correctly cites `mechanical-closure-discipline.md` lines 276-281 verbatim, and the bare conditional reading IS what the lines look like in isolation. I also AGREE with sagan's S1-final-paragraph layer-pair distinction ("Item 1 of §"IS acceptable" is an EXECUTION-LAYER predicate; the §"PLANNING DEFECT" clause is a PLAN-LAYER predicate"). That layer separation is correct and is in fact load-bearing for my disagreement (see Re:S2).

**DISAGREE** with sagan's substitution-chain Step 3 conclusion that "no additional clause in lines 274-286 conditions the consequent on plan-author awareness, anticipation status, or whether upstream-block topology was pre-registered." This reading isolates lines 274-286 from the §"When mechanical closure IS acceptable" 5-item conjunctive criterion (lines 22-57) that immediately precedes it in the same rule-file section. The mechanical-closure rule is a STRUCTURED 5-item conjunction governing execution-time admissibility followed by a SECONDARY plan-layer diagnostic. The plan-layer diagnostic was authored to catch waves whose EXECUTION-time pattern does NOT satisfy item 1 — i.e., waves that emit mechanical-closure verdicts without item-1 pre-registration in place. The §"PLANNING DEFECT" clause's antecedent is unstated but conditional on a structural state that excludes "item-1-PASS execution path"; reading the conditional in isolation from item 1 strips the rule of its load-bearing structure.

The substitution chain that exposes this:

```
Step 1 (Definition):
  IS_acceptable_item_1(W) := W's plan §"Decision Point Prerequisites"
                              section enumerates EVERY prereq-block
                              with documented blocked-by routing rule
                              per mechanical-closure-discipline.md
                              lines 25-31
  PLANNING_DEFECT_pred(W) := closure_script(W).covered_gate_count
                              >= N_PLANNING_DEFECT_THRESHOLD = 4
  rule_consequent(W)      := "wave plan W was OVER-OPTIMISTIC about
                              prerequisite landings"

Step 2 (Substitution at W = W7c):
  IS_acceptable_item_1(W7c) = TRUE
    (plan §"Wave 7c Decision Point Prerequisites" lines 23-31
     enumerates 5 items; line 33 explicitly routes absent prereqs
     to PRE-REG-INC per mechanical-closure-discipline.md §"IS
     acceptable"; sagan S2 line 100 concedes "PASS — all 4 gates
     emitted PRE-REG-INC honestly per the rule")
  PLANNING_DEFECT_pred(W7c) = TRUE (count = 4 = threshold)

Step 3 (Simplification — conjunctive reading):
  rule_consequent(W7c) = "OVER-OPTIMISTIC about prereq landings"
  But the antecedent under the conjunctive reading is:
    PLANNING_DEFECT_pred(W) AND NOT IS_acceptable_item_1(W)
  Substituting:
    TRUE AND NOT TRUE = TRUE AND FALSE = FALSE
  Therefore rule_consequent(W7c) does NOT follow under conjunctive
  reading.

Step 4 (Direction):
  W7c is exempt-by-pre-registration. The §"PLANNING DEFECT"
  diagnostic targets unanticipated prereq-block clusters where
  the plan FAILS to pre-register the absent-prereq routing —
  precisely the inverse of what plan §lines 23-31 + line 33 do
  for W7c.
```

**MISSED** — sagan's S1 acknowledges the layer pair (item 1 EXECUTION-layer, §PLANNING DEFECT PLAN-layer) but does not derive the consequence that follows from rule-text COMPOSITION. The rule's two clauses are not orthogonal admissibility predicates over an unrelated wave — they are SEQUENTIAL gates on the SAME mechanical-closure pathway. Item 1 is the ENTRY GATE: a closure script IS only authorized to fire (per the lead-in line 22 "A mechanical-closure script may be authored ONLY when ALL of the following hold") if all 5 items hold. The §"PLANNING DEFECT" diagnostic is a POST-AUTHORIZATION audit that runs IF item 1 does NOT hold — i.e., if the closure script was authored despite missing pre-registration, the PLANNING DEFECT clause documents the over-optimism that resulted in unanticipated prereq cluster. When item 1 DOES hold (as for W7c), the closure script is on the CLEAN path; the §"PLANNING DEFECT" clause has no signal to fire on because the over-optimism the clause was designed to detect (un-anticipated prereq absence) is structurally absent.

**EMERGES** — combining sagan's literal-text reading with the rule-file's conjunctive structure: the §"PLANNING DEFECT" clause is structurally a NEGATIVE-COROLLARY to item 1, not an INDEPENDENT predicate. The "If P then Q" surface form is correct but the ANTECEDENT P is not just "count ≥ 4"; it is "count ≥ 4 AND closure-script authoring path bypasses item 1's pre-registration requirement." Sagan's reading treats the surface conditional as independent of the rule-section's lead-in (line 22 "ONLY when ALL of the following hold") and the layer-pair distinction sagan himself acknowledges. This is the rule-text-reading analog of treating an `if (count_ok) { fail }` block as if it ran without context — the surrounding control flow IS load-bearing.

#### Re: S2 — Pre-registration anticipation status

**AGREE** with sagan's S2 framing that "planning defect" is a methodology-IS observable, not a plan-author psychology container observable. The substrate-IS reframe sagan deploys at S2 ("plan IS the structural artifact; whether the author 'anticipated' the prereq-block scenario is an organizational-layer property") is correct as a layer-classification statement. I AGREE the relevant signal lives on the plan artifact, not in the author's mental state.

**DISAGREE** with sagan's APPLICATION of that framing to W7c. Sagan derives "the plan IS the over-optimism" from the on-disk presence of the §"Decision Point Prerequisites" enumeration of 4 prereq-block routings. This inverts what the on-disk artifact actually structures. The plan-as-artifact for W7c contains TWO methodology-IS-observable structural facts:

(i) the §summary table at plan lines 13-17 enumerates 4 covered gates;
(ii) the §"Wave 7c Decision Point Prerequisites" at plan lines 23-31 enumerates 5 prerequisites WITH explicit routing rules — the rules are NOT side-notes about author awareness, they are FORMAL on-disk routing instructions: "if absent, route #84 to PRE-REG-INC blocked-by-S88-PV-PIPELINE-LANDING" (line 30) and "If any prerequisite fails verification at dispatch time, the producing script emits PRE-REG-INC per `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable"" (line 33).

Substitution chain on the methodology-IS observable:

```
Step 1 (Definition):
  unanticipated_prereq_cluster(W) := the W plan has covered_count
                                      gates with verdict ≠ PASS
                                      prerequisites AND the W plan
                                      lacks an on-disk routing
                                      instruction for at least one
                                      of those prerequisites
  anticipated_prereq_cluster(W)   := the W plan has covered_count
                                      gates with verdict ≠ PASS
                                      prerequisites AND the W plan
                                      contains an on-disk routing
                                      instruction for EACH such
                                      prerequisite (per
                                      mechanical-closure-discipline
                                      .md §"IS acceptable" item 1)

Step 2 (Substitution at W = W7c):
  number_of_covered_gates_with_absent_prereq = 4
  number_of_routing_instructions_in_plan_§"DPP" = 5 (lines 23-31)
  number_of_covered_gates_routed = 4 (every absent-prereq gate is
                                      routed at line 30 / 31 /
                                      generic line 33)
  unanticipated_prereq_cluster(W7c) = FALSE
  anticipated_prereq_cluster(W7c)   = TRUE

Step 3 (Simplification):
  The methodology-IS observable on the W7c plan artifact IS
  "anticipated_prereq_cluster" — a specific structural pattern
  that is the OPPOSITE of "OVER-OPTIMISTIC about prerequisite
  landings." A plan that pre-registers PRE-REG-INC routing for
  every potentially-absent prereq is NOT over-optimistic; it is
  routing-pessimistic by construction (it explicitly admits the
  absent-prereq scenario).

Step 4 (Direction):
  The §"PLANNING DEFECT" diagnostic was authored to detect
  over-optimism. The W7c plan artifact's methodology-IS structure
  is routing-pessimism. Sagan's framing of "the plan IS the
  over-optimism" reads ANTICIPATED routing-pessimism as if it were
  UNANTICIPATED over-optimism — that inversion is what cancels
  the §"PLANNING DEFECT" applicability for this wave.
```

**MISSED** — sagan's S2 weather-forecaster analogy ("schedules a parade for an hour later, posts a 'if rain occurs, the parade is cancelled' sign") is rhetorically vivid but structurally wrong on the W7c case. The analogy treats the cancellation contingency as if it were a substitute for not-scheduling-the-parade. But W7c is not analogous to "the parade with a rain-cancellation sign"; W7c is analogous to "the parade that is BY DESIGN a contingency-routing exercise." A more accurate analogy: a forecaster schedules a planning meeting that is documented to BRANCH on whether the field is dry — if dry, the meeting runs the parade; if wet, the meeting routes to a documented "deferred to next dry day" outcome. The meeting executing its documented wet-branch IS the meeting's design, not its failure. W7c §"Wave 7c Decision Point Prerequisites" line 33 is the on-disk wet-branch routing; the wave's execution of that branch IS following the plan, not deviating from it.

The §"PLANNING DEFECT" clause was authored with the OPPOSITE shape in mind: a wave that PROMISED to execute substantively, did NOT pre-register a wet-branch, and discovered the field was wet only at dispatch time. That wave produces unanticipated mechanical closures; it FAILs item 1 of §"IS acceptable" because the closure script's authoring path was post-hoc plan editing (line 30-31 of the rule file: "the closure script is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN"). W7c does not match this shape — its closure scripts are on the IS-acceptable item-1 path by construction.

**EMERGES** — sagan's substrate-IS framing is the right TOOL but applied to the wrong observable. The methodology-IS observable for "planning defect" is the JOINT structure (prereq-block count, plan routing-instruction count) — not just the count of prereq blocks. A plan that has 4 prereq blocks AND 4 routing instructions for them is a different methodology-IS object than a plan that has 4 prereq blocks AND zero routing instructions. Sagan's reading collapses this multi-axis observable to a single axis (count alone), which is itself a container-thinking violation at the rule-trigger layer: it treats the routing-instruction sub-structure as IF it were external commentary "in" the plan, rather than as part of the plan's structural content.

#### Re: S3 — Rule-file edit requirement

**AGREE** with sagan's S3 that a rule-file edit IS warranted, AND that the edit should preserve the §"PLANNING DEFECT" clause's structural utility (i.e., not retire it). I also AGREE that the edit must NOT collapse the §"PLANNING DEFECT" diagnostic into the converse of item 1 — sagan correctly identifies this collapse as a hazard. I AGREE that whatever edit lands, it should be tracked at SUGGESTION → MANDATORY status under the K=3 promotion threshold per the precedent of the §"Layer-separability carve-out" template.

**DISAGREE** with sagan's choice of edit. The "affirming clause that pins the sufficient-condition reading explicitly" sagan proposes at S3 lines 132-172 codifies the bare-conditional reading I disagree with at Re:S1. Adopting sagan's affirming-edit hardens the rule to fire on every forward-pinned follow-up wave that pre-registers ≥4 prereq-blocks — which is structurally the WRONG class of waves to flag, because those plans are doing what `mechanical-closure-discipline.md` §"IS acceptable" item 1 explicitly authorizes.

The correct rule-file edit is the OPPOSITE shape: an EXPLICIT EXEMPTION clause that pins the conjunctive reading. Proposed text (to be inserted as a new sub-section AFTER line 281 of the current rule file, BEFORE the existing line 282 "The closure script remains acceptable AT EXECUTION TIME..."):

```markdown
### Anticipated-and-pre-registered prereq-clusters DO NOT count

If the closure script's covered gates are EACH the subject of an
explicit routing instruction in the wave plan's §"Decision Point
Prerequisites" section (or analogous on-disk pre-registration of
the absent-prereq → PRE-REG-INC route per §"When mechanical
closure IS acceptable" item 1), the §"PLANNING DEFECT" trigger
DOES NOT FIRE regardless of covered-gate count. The diagnostic
targets UNANTICIPATED prereq-clusters (where the planner did NOT
pre-register the absent-prereq routing); pre-registered routing
is the IS-acceptable item-1 clean path and is structurally
distinct from the over-optimistic plan pattern this clause
documents.

The N_PLANNING_DEFECT_THRESHOLD = 4 trigger fires ONLY on the
conjunction:
  covered_gate_count ≥ 4
  AND
  count_of_covered_gates_NOT_pre_registered_in_§"DPP" ≥ 1

If every covered gate's absent-prereq scenario is pre-registered,
the wave is on the routing-pessimistic clean path and not the
over-optimistic defective path.
```

**MISSED** — sagan's S3 falsifiability-collapse argument ("ANY plan that hits the threshold can claim its prereq-blocks were 'anticipated' by pointing to a §"Decision Point Prerequisites" subsection") is the strongest objection to my edit. I concede the falsifiability concern is REAL but resolvable. The falsifier for "anticipated" is structural and on-disk: it is the presence of a per-prereq routing instruction with a NAMED blocked-by symbol (line 30: "blocked-by-S88-PV-PIPELINE-LANDING") AND a forward-pointer to the missing artifact (e.g., `phonon-exflation-sim/src/spectral_action_pv.py`). A plan that lists "Decision Point Prerequisites" with vague language and no named blocked-by symbols would FAIL the anticipated test; a plan whose listed routing instruction does not match the actual blocked-by symbol the closure script emits would also FAIL. The anticipated-test is grep-able: `_mechanical_closure_audit.py` already greps for the `value='PRE-REG-INC_blocked_by_<symbol>_<status>'` pattern (rule lines 312-313); the same audit can verify that EACH such symbol corresponds to a routing instruction in the plan's §"Decision Point Prerequisites" subsection. That structural test is operationally identical in falsifiability strength to the count-keyed test sagan proposes.

What sagan's S3 does correctly identify is that any rule-file edit must preserve a NON-EMPTY observation window for the K-counter. My edit retains that window: K-counter advances on UNANTICIPATED prereq-clusters (count ≥ 4 AND ≥1 prereq-block-without-routing-instruction). That is structurally a different observable from "violates item 1" (which is post-hoc plan editing of the closure script's authoring path); the unanticipated-cluster is a plan-layer structural property visible at plan-freeze time, while item-1 violation is an execution-layer property visible at script-authoring time.

**EMERGES** — combining sagan's affirming edit with my exempting edit suggests a third synthesis: the rule should EXPAND to a TWO-CLAUSE structure where (Clause A) pins the count threshold for unanticipated clusters AND (Clause B) explicitly carves out anticipated clusters as the routing-pessimistic clean path. Sagan's table at S3 lines 162-167 with K-counter columns is the correct calibration-corpus structure; my exempting clause is the correct trigger-condition refinement. The edit that lands BOTH is more useful than either edit alone:

```markdown
### Trigger condition (refined)

The §"PLANNING DEFECT" trigger fires iff
  covered_gate_count ≥ N_PLANNING_DEFECT_THRESHOLD
  AND
  ≥1 covered gate's blocked-by symbol does NOT appear in the
     wave plan's §"Decision Point Prerequisites" routing
     instructions

### Calibration corpus

| # | Source | covered | DPP-routed | unanticipated | Status |
|:-:|:-------|:-------:|:----------:|:-------------:|:-------|
| 0 | (vacuous baseline) | -- | -- | -- | structural |
| 1 | reserved for first unanticipated-cluster wave | -- | -- | -- | pending |
| ... | -- | -- | -- | -- | -- |
```

Note that under this synthesis, W7c's row is `(covered=4, DPP-routed=4, unanticipated=0)` and lands in calibration-corpus row #0 (the structural-baseline / no-fire row), NOT in row #1.

#### Re: S4 — W7c K-counter status

**AGREE** with sagan that calibration-corpus instances must be tracked structurally (one per qualifying wave) and that the K=3 promotion threshold is the correct gate per `feedback_rules-compensate-missing-structure.md`. I AGREE with sagan's S4 §3 that the WP synthesis at lines 881, 1006, and 1020 declared instance #1 status — three independent sites in the WP do say so. I AGREE that retroactively ERASING those WP declarations would be improper.

**DISAGREE** with sagan's conclusion that those WP declarations BIND the K-counter accounting going forward. The WP synthesis is a session-end document; it records the orchestrator's reading of the rule at that moment. When the rule's structural reading is sharpened in a subsequent workshop (THIS workshop), the WP's prior reading is amenable to AMENDMENT — not by erasing the prior text, but by appending an in-session amendment paragraph that records the workshop verdict and its consequence for the K-counter. This is not Class-3 PROHIBITED_ACTIONS at the methodology layer; the verdict-line CONTENT on disk does not change (`s88_gate_verdicts.txt` line entries for #84/#85/#86/#167 keep their value strings, schemes, conventions, audit_sha256s — all permanent). What changes is the RULE-FILE-LAYER LABEL the wave is filed under. That is a label-amendment in service of a corrected structural reading, structurally distinct from threshold-editing.

Substitution chain on the K-counter under the conjunctive reading:

```
Step 1 (Definition):
  K_promotion := 3 (per feedback_rules-compensate-missing-structure.md)
  K_planning_defect := count of structurally-distinct calibration-
    corpus instances of (covered_gate_count ≥ 4 AND ≥1 covered gate's
    blocked-by symbol does NOT appear in the wave plan's §"DPP"
    routing instructions) — i.e., the unanticipated-cluster trigger

Step 2 (Substitution at session-end S88, conjunctive reading):
  Pre-W7c instances: 0 (rule landed at S86 W3; no UNANTICIPATED
    prereq-cluster between S86 W3 and S88 W7c — every S86/S87/S88
    mechanical-closure-emitting wave audited had IS-acceptable
    item-1 pre-registration in place)
  W7c instance: NOT counted (every absent-prereq's blocked-by symbol
    DOES appear in plan §"Wave 7c Decision Point Prerequisites"
    routing — items 4, 5, plus implicit items via line 33 generic
    routing for #86 and #167 obs2/3)
  K_planning_defect = 0

Step 3 (Simplification):
  K_planning_defect = 0 < K_promotion = 3

Step 4 (Direction):
  Status remains SUGGESTION at K=0. The calibration corpus opens
  with three RESERVED rows pending the first unanticipated-cluster
  wave. K-counter advancement awaits a future plan-author who
  schedules a wave with ≥4 prereq-block gates without on-disk
  routing instructions for at least one of them.
```

**MISSED** — sagan's S4 §1 "K-counter dies-on-arrival" argument requires careful response. Sagan claims my reading collapses §"PLANNING DEFECT" into "the converse of item 1" and therefore makes K_promotion = 3 unreachable BY CONSTRUCTION. This is an inversion: the §"PLANNING DEFECT" clause is NOT the converse of item 1 under my reading — it is a DOWNSTREAM diagnostic that fires when a closure script was authored despite item 1 not holding. Concretely:

- Item 1 prohibition (rule line 30-31): if a plan does NOT pre-register absent-prereq routing AND the closure script fires anyway, the closure-script authoring is post-hoc plan editing (Class 3 violation) and is FORBIDDEN.
- §"PLANNING DEFECT" diagnostic: if a plan does not pre-register absent-prereq routing AND ≥4 closure scripts fire anyway, the over-optimism pattern is documented (instance lands in K-counter).

The two clauses operate on the SAME structural event but at different levels: item 1 prohibits the script from being authored; §"PLANNING DEFECT" diagnoses the wave-level pattern when ≥4 such scripts were authored anyway. The K-counter has a non-empty observation window: it advances when a future session contains a wave that emits 4+ unanticipated mechanical closures. That session will simultaneously ALSO have item-1 violations to remediate, but the two are different layers of intervention — item-1 is the per-script prohibition, §"PLANNING DEFECT" is the wave-level pattern documentation.

Hypothetical W7c-prime that would advance the K-counter (response to sagan's S4 final paragraph and Q4): a wave plan that lists 4 covered gates, each with a verdict-≠-PASS prerequisite, where the plan's §"Decision Point Prerequisites" section either (a) is absent entirely, or (b) lists routing instructions for fewer than 4 of the 4 prerequisites. At dispatch time, all 4 prerequisites are absent and the closure-script authors emit PRE-REG-INC. The closure-script authoring is item-1-violating (because routing was not pre-registered for at least one), so the closure-script authors emit FAIL composites and the orchestrator post-wave audit detects the item-1 violation. The wave is structurally a PLANNING DEFECT instance #1 — the planner did not envisage the prereq-absent scenario at plan-freeze, and ≥4 gates produced unanticipated closures.

This hypothetical is not vacuous. Pre-W7c, NO session in S86–S88 produced this pattern; the existing waves either (i) had IS-acceptable item-1 pre-registration in place (W7c-shape) or (ii) had <4 covered gates total. The pattern that advances the K-counter is structurally well-defined and observable; it just hasn't fired yet.

**EMERGES** — the cleanest synthesis of sagan's S4 with my reading is: track TWO calibration corpora, not one. Sagan's "covered_count ≥ 4" corpus tracks wave-level prereq-block counts as a sociological metric of plan-author scheduling (useful for wave-partition policy at the planner-skill layer); my "unanticipated-cluster" corpus tracks the rule-trigger as authored. The two corpora are non-redundant: the first is a heuristic input to plan-authorship policy, the second is the rule-fire instrumentation. W7c counts as instance #1 of the FIRST corpus (sagan's calibration of the prereq-block-count metric); W7c does NOT count as instance #1 of the SECOND corpus (the rule's structural trigger as conjunctively authored). The WP declarations at lines 881/1006/1020 can be amended to specify which corpus they refer to, preserving their content while disambiguating the K-counter accounting.

#### Re: S5 — Forward template

**AGREE** with sagan's S5 forward template ALMOST IN FULL. The 3-tier decision rule sagan proposes (lines 284-293):

```
if PB(W) ≥ 4: SPLIT_REQUIRED
elif PB(W) ≥ 2 and PB_frac(W) ≥ 0.50: SPLIT_RECOMMENDED
else: SINGLE_WAVE_OK
```

is a STRUCTURALLY SOUND PLAN-AUTHORSHIP HEURISTIC that I endorse for adoption in `/rclab-plan` skill text or in a planner-side rule-file. The substitution chain at S5 lines 297-324 correctly identifies that PB(W7c) = 4 = N_PLANNING_DEFECT_THRESHOLD on the metric sagan defines, and that SPLIT_REQUIRED is the correct planner-side recommendation under that heuristic.

**DISAGREE** that the SPLIT_REQUIRED heuristic is a RULE TRIGGER for the §"PLANNING DEFECT" clause. Sagan conflates two distinct things at S5: (a) a planner-side advisory heuristic ("when PB(W) ≥ 4, consider splitting") with (b) a rule-fire diagnostic ("when count ≥ 4, the rule fires and the K-counter advances"). The heuristic and the rule-fire share an arithmetic threshold but are structurally different artifacts.

Substitution chain on the heuristic-vs-rule distinction:

```
Step 1 (Definition):
  heuristic_consequence(W; PB(W) ≥ 4) := plan-author SHOULD split
    W into W{N}_machinery + W{N+1}_verify; recommendation logged
    at /rclab-plan layer; non-binding (advisory)
  rule_consequence(W; count ≥ 4) := §"PLANNING DEFECT" trigger
    fires; K-counter advances by 1; rule-file calibration corpus
    instance #N+1; binding (carries promotion-threshold tracking)

Step 2 (Substitution at W = W7c):
  heuristic_consequence(W7c) = "advisory: plan-author should have
    split W7c into machinery W7b-extension + verify W7c"; this
    advice is consistent with WP §8 carry-forward queue containing
    5 machinery-landing items (CF#1, #3, #5, #7, #8) and 5 verify-
    re-run items (CF#2, #4, #6, #9, #10), totaling the same effort
    as a properly-split wave pair would have generated
  rule_consequence(W7c) under conjunctive reading = NOT TRIGGERED
    (per Re:S4 substitution chain Step 2)

Step 3 (Simplification):
  heuristic_consequence(W7c) ≠ rule_consequence(W7c)
  The heuristic SHOULD have advised splitting at plan-freeze; the
  fact that it didn't is a planner-skill gap, not a rule-trigger
  fire. The wave's actual execution under item-1 pre-registration
  was the IS-acceptable clean path.

Step 4 (Direction):
  Adopt sagan's heuristic at the /rclab-plan skill layer; do NOT
  adopt it as a rule-trigger amendment to mechanical-closure-
  discipline.md §"PLANNING DEFECT". The two interventions live at
  different layers and are not mutually substitutable.
```

**MISSED** — sagan's S5 final paragraph poses "Under your 'anticipated prereq cluster is structurally clean' reading, what is the operational signal that triggers SPLIT_REQUIRED at plan-freeze?" My answer: the signal is sagan's PB(W) count itself, used as a /rclab-plan SKILL heuristic. The plan-author at plan-freeze time queries PB(W) and decides per sagan's 3-tier rule. The §"PLANNING DEFECT" rule is NOT the plan-author's tool; it is a post-execution audit tool that fires only when item-1 pre-registration is absent. Plan-authors who follow sagan's heuristic AT PLAN-FREEZE will produce well-shaped waves; those who do not will produce W7c-shaped waves whose mechanical-closure verdicts are clean BUT whose carry-forward queues balloon.

The W7c carry-forward queue (5.6 wave-equivalents = 1.5× W7c's own budget per WP §8 line 996) is the empirical signal sagan correctly identifies. I AGREE this signal is real, observable, and worth pinning at the planner-skill layer. The disagreement is over which RULE-FILE consumes it: the §"PLANNING DEFECT" clause was authored to consume unanticipated-cluster failures (a different signal); the planner-skill rules (`/rclab-plan` skill text, `feedback_fix-in-session-never-defer.md`) are the correct consumers of the heuristic.

**EMERGES** — sagan's S5 substitution chain reveals that the carry-forward-queue size is itself a methodology-IS observable that COULD be promoted to a rule-trigger at a different rule-file. Candidate forward extension (NOT to mechanical-closure-discipline.md, but to a separate carry-forward-queue rule):

```
At session-close, if total_carry_forward_effort(W) ≥ 1.5 × W.budget
and ≥ 50% of carry-forwards are W{N}_machinery-displacement items:
  log a planner-side calibration-corpus instance for the
  carry-forward-displacement metric; track at the /rclab-plan
  skill layer.
```

This is a NEW rule that captures sagan's empirical signal at the appropriate layer. It is forward-looking and orthogonal to mechanical-closure-discipline's own §"PLANNING DEFECT" clause.

#### Re: S6 — Cross-Cutting Observations

**AGREE** with sagan's S6 substrate-IS framing layer-functor F image table (S6 lines 380-388) at the type level. The F-image table correctly maps physics-layer substrate-IS observables to methodology-layer artifact-IS observables. I AGREE that "planning defect" is a methodology-IS observable, that its trigger predicate reads the plan structure (not the plan-author's psychology), and that container-thinking at the rule-trigger layer is a real failure mode.

**DISAGREE** with sagan's S6 single-axis collapse of the methodology-IS observable. Sagan's framing treats "the count of covered gates" as the substrate-IS observable. This is a single scalar projection of a multi-axis methodology-IS object. The actual methodology-IS object on the W7c plan artifact is multi-axis:

```
methodology_IS_observable(W) :=
   (count_covered_gates(W),
    count_DPP_routing_instructions(W),
    count_named_blocked_by_symbols(W),
    count_each_per_gate_routing_match(W))
```

Sagan's reading projects this 4-tuple onto its first component. That projection IS a methodology-IS observable, but it is NOT the only methodology-IS observable, and reading the §"PLANNING DEFECT" rule's trigger as keyed only on the first component is a single-axis flattening of the multi-axis observable. The substrate-IS reframe (per `phononic-framing.md` §"IS Space, Not IN Space") permits multi-axis observables to remain multi-axis; collapsing them to a single axis is itself a container-thinking move because it treats the non-projected axes as "external commentary on the plan" rather than as part of the plan's structural content.

Substitution chain on the multi-axis methodology-IS observable:

```
Step 1 (Definition):
  layer_functor_F image(planning-defect_substrate-IS_observable)
    := the methodology-layer artifact-IS structure on the wave
       plan that the §"PLANNING DEFECT" clause's trigger predicate
       reads
  This image is multi-axis by construction (the rule consumes
  more than just covered_count — it also consumes the IS-acceptable
  item-1 pre-registration status, per the conjunctive reading
  derived in Re:S1)

Step 2 (Substitution under sagan's S6 reading):
  sagan_F_image := (covered_count) -- single axis
  sagan_trigger_predicate(W) := sagan_F_image(W) ≥ 4

Step 3 (Substitution under conjunctive reading):
  conjunctive_F_image := (covered_count, DPP_routing_count, NOT(IS-acceptable_item_1)) -- multi-axis
  conjunctive_trigger_predicate(W) := covered_count ≥ 4
                                       AND
                                       NOT(IS-acceptable_item_1(W))

Step 4 (Direction):
  Sagan's single-axis reading projects out the IS-acceptable
  item-1 axis and consumes only count. The conjunctive reading
  preserves the multi-axis structure of the methodology-IS
  observable. Substrate-IS framing does not endorse single-axis
  projection by default; it endorses preserving the structural
  content of the artifact, which is multi-axis.
```

**MISSED** — sagan's S6 final paragraph claim that "the plan IS the over-optimism, made manifest on disk" is an INVERSION of the substrate-IS direction-of-explanation. The plan artifact contains BOTH the prereq-block enumeration AND the routing-instruction enumeration; reading the first while ignoring the second is the methodology-layer F-image of the GR-container error pattern from `phononic-framing.md` ("particles created IN curved spacetime" — wrong; "fiber spectrum reorganizes at the fold" — right). Translated to the methodology layer:

| WRONG (single-axis projection) | RIGHT (multi-axis preservation) |
|:-------------------------------|:--------------------------------|
| "planning defect IN the plan-artifact's covered-count axis" | "planning-defect-eligibility IS the conjunctive structure (count, DPP-routing, item-1 status) on the plan artifact" |
| "the plan IS the over-optimism" (sagan S6 line 408) | "the plan IS the multi-axis structure; over-optimism IS the projection where DPP-routing is absent" (corrected) |

The corrected reading preserves the substrate-IS framing sagan correctly invokes while NOT collapsing the methodology-IS observable to a single scalar.

**EMERGES** — sagan's S6 substrate-framing argument is the strongest pillar of his case AND the most recoverable at the multi-axis level. Both sides of this workshop are committed to substrate-IS / methodology-IS framing; the disagreement reduces to whether the §"PLANNING DEFECT" trigger predicate reads a single-axis projection (sagan) or a multi-axis structure (mine). This is a TESTABLE structural question at the rule-text layer:

- If the rule were authored to fire on count alone, it would have NO mention of item 1 anywhere in lines 22-286 of the rule file.
- The rule DOES contain item 1 as the lead-in admissibility predicate (lines 22-31) and DOES contain the §"PLANNING DEFECT" clause AS A SECONDARY DIAGNOSTIC (lines 274-286) — separated by a 5-item ENUMERATION that the lead-in says ALL must hold.

The rule-file's structural composition argues the trigger is multi-axis. Sagan's single-axis reading is supported by the literal text of lines 276-281 in isolation but NOT by the rule-file's surrounding control flow. This is the rule-file analog of the SCHEMATIC-helper-consumption pathology from `substrate-first-canonical-sourcing.md` §(iv): a downstream consumer reading a single block of a rule file out of its enclosing structural context will silently flatten the rule to a less-structured form than the rule-author intended.

### Part 2: Original Analysis

#### G1: Mechanical-closure §"When mechanical closure IS acceptable" item-1 reading vs §"PLANNING DEFECT" — conjunctive or independent?

**Position**: The two clauses are CONJUNCTIVELY COMPOSED, not independent. When item 1 PASSes (upstream-block topology pre-registered, which IS the case for W7c per plan §"Wave 7c Decision Point Prerequisites" lines 23-31), the §"PLANNING DEFECT" clause is INAPPLICABLE by construction.

**Rule-text evidence (lines as cited)**:

1. `mechanical-closure-discipline.md` line 22: "A mechanical-closure script may be authored ONLY when ALL of the following hold:". The lead-in pins ALL 5 items as required for closure-script authorization. This is a hard conjunction over the 5 items.

2. `mechanical-closure-discipline.md` lines 25-31 (item 1): "Upstream-block topology is the cause: every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's downstream decision-point table specifies the documented outcome for prereq-block (typically 'PRE-REG-INC, deferred to S{N+1}'). The plan author MUST have anticipated the prereq-block scenario; if the plan does not address it, the closure script is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN."

3. `mechanical-closure-discipline.md` line 274 (heading): "When mechanical closure indicates a PLANNING DEFECT". Note the verb-form is "INDICATES" — the closure HAS ALREADY BEEN AUTHORED (per the prior 5-item gate); the question this clause asks is "what does the SHAPE of the authored closure tell us about the plan?"

4. `mechanical-closure-discipline.md` lines 282-286 (the closing clause): "The closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson and adjust wave-partitioning policy to avoid recurrence." Note: this clause acknowledges that the CLOSURE SCRIPT is acceptable. That acceptability is item-1-conditional. If item 1 was NOT in place, the closure script would be FORBIDDEN per item-1's own line 30-31 (it would be Class 3 post-hoc plan editing).

**Substitution chain on the conjunctive composition**:

```
Step 1 (Definition):
  closure_authorization(W) := admissible iff ALL of items 1-5 hold
                              (per rule line 22 lead-in)
  PLANNING_DEFECT_diagnostic(W) := fires iff
                                    closure_authorization(W) holds
                                    AND covered_gate_count(W) ≥ 4
                                    AND ≥1 of those closures was
                                    AUTHORED despite item 1 being
                                    OPEN-AT-AUTHORING-TIME (which
                                    is the structural pattern the
                                    diagnostic was designed to
                                    detect)

Step 2 (Substitution at W = W7c):
  closure_authorization(W7c) = TRUE
    (all 4 closures emit honest PRE-REG-INC; per WP §1 lines 866-869
     and verdict file lines 238-265, all honor the 5-item gate)
  covered_gate_count(W7c) = 4
  count_closures_authored_despite_item_1_OPEN(W7c) = 0
    (every covered gate's blocked-by symbol matches a routing
     instruction in plan §"DPP" lines 23-31 + line 33 generic
     route)
  PLANNING_DEFECT_diagnostic(W7c) = TRUE AND TRUE AND FALSE = FALSE

Step 3 (Simplification):
  Diagnostic does NOT fire. The wave is on the IS-acceptable
  clean path. The closure scripts are admissible per item 1;
  the §"PLANNING DEFECT" clause has nothing to diagnose.

Step 4 (Direction):
  Conjunctive composition is the correct rule-reading. The
  diagnostic is a downstream audit conditional on closure-
  authorization holding AND the structural pattern (count ≥ 4
  AND ≥1 unanticipated-closure) being present. W7c satisfies
  the first conjunct (closure-authorization) but NOT the second
  conjunct (≥1 unanticipated). Therefore the diagnostic does
  not fire.
```

**Audit-script-layer evidence**: `mechanical-closure-discipline.md` lines 308-324 specify the audit script `_mechanical_closure_audit.py` and enumerate 4 verification items it performs:

(i) named upstream gate exists in same file
(ii) upstream gate's status matches the closure value string assertion
(iii) closure-line audit_sha256 is unique across all canonical lines
(iv) corresponding working-paper section has been updated

NOTE: the audit script does NOT have a separate verification step for the §"PLANNING DEFECT" clause's count threshold. If the §"PLANNING DEFECT" diagnostic were a structurally INDEPENDENT predicate (sagan's reading), the audit script would have a fifth verification item: `(v) wave-level closure count < N_PLANNING_DEFECT_THRESHOLD = 4`. It does not. The audit script's 4-item enumeration is structurally consistent with the conjunctive reading: the audit checks item-1's per-closure consistency (items i-iv); the §"PLANNING DEFECT" diagnostic is a wave-level COMMENTARY that fires only when item-1 audit FAILs at ≥4 sites — i.e., when the audit's failure pattern reveals an unanticipated-cluster.

**Conclusion**: rule-text composition (line 22 lead-in + line 30-31 item-1 prohibition + line 274 "INDICATES" framing + lines 282-286 acceptable-at-execution-time + audit-script's 4-item enumeration without a 5th wave-count check) all point to conjunctive composition. The two clauses are not independent admissibility predicates; they are sequential gates where the §"PLANNING DEFECT" diagnostic is conditional on item-1's closure authorization PLUS a separate unanticipated-cluster pattern.

#### G2: Synthesis-§2 vs plan-§"Decision Point Prerequisites" textual collision diagnosis

**Diagnosis**: the apparent collision between WP §"2. Plan-authoring discipline" line 877 (declaring instance #1 status) and plan §"Wave 7c Decision Point Prerequisites" lines 23-31 (pre-registering all 4 prereq-blocks with routing rules) is a FALSE ALARM, resolvable by an in-session amendment to WP §2 that does NOT touch verdict-line content.

**The structural collision**:

(i) plan §lines 23-31 + line 33 enumerate 5 prerequisites with explicit routing instructions, and line 33 explicitly cross-references `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` — this matches IS-acceptable item 1 BY CITATION;
(ii) WP §2 line 877 asserts instance #1 status under §"PLANNING DEFECT" — which under the conjunctive reading is structurally inconsistent with (i);
(iii) WP §9 line 1006 and §"Constraint-Map Updates" line 1020 propagate the (ii) declaration.

**Why this is a false alarm rather than a hard collision**:

The WP §2 declaration was written in the session-end synthesis pass as the orchestrator's reading of the rule at that moment. The rule-text reading sagan poses at S1 (literal "If P then Q" on count alone) is a defensible surface-level reading that the orchestrator at session-close arrived at without engaging the conjunctive composition argument THIS workshop adjudicates. The synthesis was correct given the rule-reading the orchestrator used; the rule-reading was incomplete given the rule-text's actual conjunctive composition.

**The amendment**: WP §2 should be amended (NOT erased) to record:

(a) the orchestrator's session-close reading classifying W7c as instance #1 under the literal text reading;
(b) the post-session workshop adjudication (THIS workshop) determining that the rule's conjunctive composition does not fire on W7c;
(c) the corrected K-counter accounting (status: under conjunctive reading, K = 0; W7c lands in calibration-corpus row #0 / structural baseline);
(d) cross-link to the rule-file edit landing the explicit anticipated-cluster exemption clause (per Re:S3 EMERGES synthesis).

**Why this is NOT a Class-3 PROHIBITED_ACTIONS issue**:

`v3-closure-recovery.md` PROHIBITED_ACTIONS Class 3 forbids "post-hoc pre-registration editing — retroactively editing the plan file's pass_threshold, pass_band, or tolerance_rule after seeing the computed value." The amendment to WP §2 does NOT touch:

- the pass_threshold of any gate (#84/#85/#86/#167 retain their plan-pinned thresholds);
- the pass_band or tolerance_rule of any gate;
- the audit_sha256 of any verdict line on disk (per `gate-verdicts.md §"Rules"` item 2: "Verdicts are permanent — no retroactive changes" — these are permanent BY CONSTRUCTION; the amendment does not edit them);
- the value strings, schemes, conventions, L_max, or content_sha256 of any verdict line.

What the amendment DOES touch: the rule-file-LAYER LABEL the wave is filed under at the calibration-corpus tracking layer. Sagan's S6 invocation of the layer-functor F is correct — the amendment lives at the methodology-rule layer, not at the substrate-physics-pass-threshold layer. Under F's image, methodology-layer label-amendments are NOT the F-image of substrate-layer threshold-edits; they are the F-image of registry-layer entry-tag refinements (analogous to changing a registry slot's STAGE-1-CANDIDATE tag to STAGE-3-PERMANENT after Stage-2 PASS-AND, which is `joint-theorem-promotion.md`'s EXPLICITLY DESIGNED behavior — not Class 3 violation).

**The amendment's structural form** (proposed text for WP §2 in-session edit, appended after current line 881):

```markdown
### §2 Amendment (2026-05-08, post-W-25 workshop adjudication)

The synthesis-§2 declaration of W7c as instance #1 of the
N_PLANNING_DEFECT_THRESHOLD = 4 trigger reflects the
session-close orchestrator's literal reading of
mechanical-closure-discipline.md lines 276-281 in isolation.
Workshop W-25 (sagan x gen-physicist, 2026-05-08) adjudicated
the rule's conjunctive composition and determined that:

(i) plan §"Wave 7c Decision Point Prerequisites" lines 23-31
    pre-register all 4 prereq-blocks with explicit routing
    instructions per mechanical-closure-discipline.md §"IS
    acceptable" item 1;
(ii) the §"PLANNING DEFECT" diagnostic is conditional on
     item-1-violating closure scripts (rule-file lead-in line
     22 "ONLY when ALL of the following hold" + audit-script
     evidence at lines 308-324);
(iii) under the conjunctive reading, W7c lands in calibration
      corpus row #0 (structural-baseline / no-fire row), NOT
      in row #1.

The rule-file edit landing the explicit anticipated-cluster
exemption clause is queued as carry-forward CF-W7c-ADDITIONAL-B
(per `_seed-w7c.md` Workshop-2 carry-forward enumeration).
The workshop verdict at §"Workshop Verdict" pins the final
classification.

Verdict-line content on disk is unchanged: #84/#85/#86/#167
canonical lines retain their pre-registered audit_sha256 +
content_sha256 + value strings + schemes + conventions per
`gate-verdicts.md §"Rules"` item 2 absolute permanence rule.
```

This amendment is the cleanest resolution: it preserves the WP's prior content as a session-close reading, records the post-session workshop adjudication as a label refinement, and explicitly distinguishes the rule-classification-label layer from the verdict-permanence layer.

#### G3: Questions for sagan

These five questions parallel sagan's S7 Q1-Q5 but on the conjunctive-reading axis. Each is structural, not rhetorical, and has a definite right answer.

**Q1 (clause (a) — where does the conjunctive antecedent come from)**: You read `mechanical-closure-discipline.md` lines 276-281 in isolation. Why? The same rule-file's line 22 ("ONLY when ALL of the following hold") and lines 25-31 (item 1's Class-3 prohibition on post-hoc plan editing of closure scripts) are part of the SAME rule section. The §"PLANNING DEFECT" clause's heading reads "INDICATES" — a verb that PRESUPPOSES the closure-authoring path was completed. Under your isolated-text reading, what triggers a closure script to be authored at all? If item 1 is unconditionally required for closure-authoring per line 22's "ONLY when ALL of the following hold," and §"PLANNING DEFECT" "INDICATES" something about an already-authored closure, then the rule-section's structural composition forces the conjunctive reading. Cite the rule-text token by which you read line 22's "ALL of the following" as NON-CONJUNCTIVE with respect to the §"PLANNING DEFECT" clause four sub-sections later in the same rule-file section.

**Q2 (clause (b) — falsifiability of "count alone fires")**: Under your reading, the §"PLANNING DEFECT" trigger fires whenever covered_count ≥ 4. State a falsifier. What concrete W-shape would NOT fire under your reading? If your falsifier requires covered_count < 4, then your reading's only structural test is the integer threshold itself — but the integer threshold is shared between our readings; the real disagreement is on the antecedent SHAPE. If your falsifier requires the closure scripts to NOT be honest mechanical closures (i.e., they emit PASS / convention-shop / iterate-until-pass), those are already PROHIBITED_ACTIONS Class 1/4/6 and would never reach the §"PLANNING DEFECT" diagnostic — they FAIL upstream at item-2 / Class-1 / Class-6 audits. Address: under your reading, what is the structural class of W-shapes that fires §"PLANNING DEFECT" while NOT triggering a prior, more specific PROHIBITED_ACTIONS?

**Q3 (clause (c) — concrete edit text test)**: Your S3 edit (lines 132-172) inserts an "affirming clause" pinning sufficient-condition reading. Test your text on the following hypothetical W-shape:

- Wave W' has 5 covered gates. ALL 5 prerequisites are pre-registered with routing instructions in plan §"Decision Point Prerequisites" — items 1, 2, 3, 4, 5 each name a blocked-by symbol. At dispatch time, prerequisites 1-4 land successfully (verdict = PASS); prerequisite 5 is absent, and gate #5 emits PRE-REG-INC mechanical closure honestly. covered_gate_count = 1 < 4. Your reading classifies W' as NOT triggering the diagnostic — correct.
- Wave W'' has 5 covered gates. ALL 5 prerequisites are pre-registered with routing instructions. At dispatch time, all 5 prerequisites are absent. covered_gate_count = 5 ≥ 4. Your reading classifies W'' as triggering instance #2.

But W'' is structurally on the IS-acceptable item-1 clean path (every closure has its blocked-by symbol routed). The closure scripts are admissible by item 1 (they would be PROHIBITED if item 1 weren't in place). Under your reading, item-1-clean waves CAN fire §"PLANNING DEFECT" purely on count. What does that fire ACTUALLY diagnose if not the absence of pre-registration? If "scheduled too many gates whose prereqs hadn't landed yet at the moment of dispatch" is the answer, that's a SCHEDULING diagnostic — but the rule-file is named `mechanical-closure-discipline.md`, not `wave-scheduling-discipline.md`. Should this diagnostic live in mechanical-closure-discipline.md, or in a dedicated planner-skill rule (per Re:S5 EMERGES carry-forward-displacement metric)?

**Q4 (clause (d) — K-counter advancement under your reading)**: Per your S4 substitution chain, the K-counter advances at K=1 on W7c. Is your forward expectation that future sessions will produce ADDITIONAL count ≥ 4 instances — i.e., that the K-counter will reach K=3 at some future session — consistent with WP §"Next-step routing" line 1042's explicit guidance that S89 plan-author MUST sequence machinery + data landings BEFORE cross-review verify gates? If S89 follows that guidance, no count-≥-4 instance fires in S89, so your K-counter expectation is K stays at 1 indefinitely (sagan S4 line 266: "K stays where it should pending another instance"). Under your reading the rule reaches MANDATORY status only if a future session produces a similar wave PATTERN — which is exactly the pattern your forward template (S5) tells planners to AVOID. Is the K=3 promotion threshold structurally reachable under your reading except via planner-skill failures? If yes, your K-counter is a sociological metric of planner-skill maturity; if no, the K=3 promotion threshold is unreachable and the rule retires at SUGGESTION status.

**Q5 (substrate framing — multi-axis preservation under F)**: Per Re:S6 above, the methodology-IS observable on the W7c plan artifact is multi-axis: `(covered_count, DPP_routing_count, item_1_status_per_gate)`. Your S6 reading projects this 4-tuple to its first component. Substrate-IS framing per `phononic-framing.md` does NOT endorse single-axis projection by default — it endorses preserving the full structural content of the artifact. Address: which axis of the methodology-IS observable does the §"PLANNING DEFECT" trigger predicate consume, in your reading? If you say "covered_count alone," then your reading collapses the multi-axis observable. If you say "covered_count AND something else," what is the something else, and how does that NOT recover the conjunctive reading I propose? The substrate-IS framing argument does not select between our readings on its own; it requires answering which methodology-IS observable axes the rule's predicate is keyed on.

---

## Round 2 — sagan: Follow-up

### CONVERGENCE

After reading gen-physicist's Re:S1–S6 + G1–G3, four points of genuine convergence have emerged. I state explicitly which sub-claim moved me on each.

**C1: The methodology-IS observable on the W7c plan artifact IS multi-axis, not single-axis.**

Gen-physicist's Re:S6 §"DISAGREE" derivation (workshop lines 728–738) is structurally compelling. The on-disk plan artifact for W7c contains BOTH (a) the count of covered gates (4) AND (b) the count of routing instructions in §"Decision Point Prerequisites" (5, with 4-of-5 mapping to covered gates) AND (c) the per-gate item-1-status (PASS for all 4). Reading only axis (a) while ignoring axes (b) and (c) is a single-axis projection of a multi-axis methodology-IS object. My S6 framing was correct in invoking the substrate-IS reframe, but Re:S6's "single-axis projection IS itself a container-thinking move" critique lands. The substrate-IS framing rule (`phononic-framing.md §"IS Space, Not IN Space"`) does not endorse single-axis projection by default; it endorses preserving the structural content of the artifact, which is the full tuple. I concede this point.

What this DOES NOT change: the question of which axes the rule's TRIGGER PREDICATE is keyed on. That question is settled by the rule text alone, not by the multi-axis structure of the artifact. Conceding multi-axis structure for the OBSERVABLE is not the same as conceding multi-axis composition for the TRIGGER. See DISSENT D1 below.

**C2: The heuristic-vs-rule-trigger distinction is structurally sharp and worth pinning at separate layers.**

Re:S5 §"DISAGREE" (workshop lines 671–706) draws a clean distinction between (a) a planner-side advisory heuristic ("when PB(W) ≥ 4, consider splitting") at the `/rclab-plan` skill layer and (b) a rule-fire diagnostic at the `mechanical-closure-discipline.md` layer. I AGREE the two interventions live at different layers of the layer-functor F. My S5 originally proposed inserting the SPLIT_REQUIRED rule directly into `mechanical-closure-discipline.md §"PLANNING DEFECT"`; gen-physicist's Re:S5 correctly flags this as conflating heuristic-layer and rule-trigger-layer. The cleanest forward template is to pin the SPLIT_REQUIRED heuristic at the `/rclab-plan` skill layer (or a planner-skill rule-file) and KEEP `mechanical-closure-discipline.md §"PLANNING DEFECT"` as a separate rule-fire diagnostic at its current location.

This is a legitimate Re:S5 movement. My S5 forward template stands as a planner-skill heuristic; it does NOT extend into the mechanical-closure rule-file as a trigger amendment. Two separate landing sites, two separate calibration corpora.

**C3: The "structural carry-forward-displacement metric" is a separable forward template independent of the K-counter adjudication.**

Re:S5 §"EMERGES" (workshop lines 712–722) proposes a NEW carry-forward-displacement rule:

```
At session-close, if total_carry_forward_effort(W) ≥ 1.5 × W.budget
and ≥ 50% of carry-forwards are W{N}_machinery-displacement items:
  log a planner-side calibration-corpus instance for the
  carry-forward-displacement metric.
```

This metric is independent of whether the §"PLANNING DEFECT" trigger fires — it operates POST-execution on the WP carry-forward queue, not at plan-freeze on the prereq-block routing count. I AGREE this metric is forward-useful regardless of the §"PLANNING DEFECT" adjudication outcome. W7c IS calibration-corpus instance #1 of the carry-forward-displacement metric (CF total = 5.6 wave-equiv ≥ 1.5 × 3.8 wave-equiv = 5.7 wave-equiv; close to threshold; 5-of-10 carry-forwards are machinery-displacement = 50%). This metric should be pinned at a separate planner-skill rule-file (candidate: extension to `feedback_fix-in-session-never-defer.md` or a new `carry-forward-displacement-discipline.md`) with its own K-counter.

The carry-forward-displacement metric and the §"PLANNING DEFECT" diagnostic are non-redundant: the first is a session-close measurement on the WP carry-forward queue; the second is a plan-freeze-time predicate on the prereq-block routing structure. Both are useful; both can land.

**C4: The G2 amendment to WP §2 is structurally distinct from Class-3 PROHIBITED_ACTIONS at the substrate-physics layer.**

Re:G2 (workshop lines 879–887) correctly identifies that an in-session amendment to WP §2 that does NOT touch verdict-line content (audit_sha256, content_sha256, value strings, schemes, conventions, L_max remain frozen on disk per `gate-verdicts.md §"Rules"` item 2) is structurally distinct from Class-3 post-hoc threshold editing. The amendment lives at the rule-file-classification-LABEL layer, not at the substrate-physics-pass-threshold layer. Gen-physicist's analogy to `joint-theorem-promotion.md`'s STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion (workshop line 887) is structurally correct: that promotion IS a label-amendment that preserves all upstream content. The amendment to WP §2 is the same kind of label-amendment, NOT a Class-3 violation.

I CONCEDE this on the technical layer-functor F-image argument. My S3 §2 "Class-3 PROHIBITED_ACTIONS adjacency" claim was structurally over-strong — it conflated the rule-classification-label-amendment with substrate-layer threshold editing. The two ARE different under F. (Note: this concession does NOT affect my position on whether the W7c LABEL should change; that is the DISSENT D1 / D2 issue. Class-3-adjacency is one argument among several; conceding it does not concede the rest.)

### DISSENT

Four points of dissent remain, each presenting NEW evidence rather than restating Round 1 positions.

**D1: The conjunctive-composition argument requires textual linkage between §"IS acceptable" and §"PLANNING DEFECT" that the rule-file does NOT contain.**

Gen-physicist's Re:S1 + G1 derives a conjunctive antecedent for the §"PLANNING DEFECT" trigger by composing the line-22 lead-in ("ONLY when ALL of the following hold") with the line-274 §"PLANNING DEFECT" heading verb "INDICATES." The argument's structural shape is: line-22 is the closure-script-AUTHORIZATION lead-in for items 1–5; "INDICATES" presupposes an authored closure; therefore the §"PLANNING DEFECT" clause's antecedent is conjunctively conditional on items 1–5 having held.

NEW EVIDENCE (rule-text composition check, performed against the actual file):

- Lines 22–57: §"When mechanical closure IS acceptable" — lead-in line 22 + 5 items + "Layer-separability carve-out" sub-section (lines 60–272). The lead-in's "ONLY when ALL of the following hold" governs items 1–5 of THIS subsection. Items 1–5 are AUTHORIZATION conditions for the closure-script.
- Lines 274–286: §"When mechanical closure indicates a PLANNING DEFECT" — bare conditional on covered-gate count. The text contains NO cross-reference to items 1–5, NO "IF item 1 was VIOLATED" qualifier, NO "this clause is conditional on ... " preamble. The section is a structurally INDEPENDENT diagnostic at the same heading-level (## twice in the rule-file).
- Lines 282–286 (the closing paragraph of §"PLANNING DEFECT"): "The closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson..."

The closing paragraph EXPLICITLY ASSUMES the closure script IS acceptable at execution time — i.e., item 1 PASSED. Under gen-physicist's Re:S1 conjunctive reading where §"PLANNING DEFECT" fires only when item 1 FAILED, this paragraph would be incoherent: it claims the closure-script is "acceptable" precisely when the trigger has fired, which under the conjunctive reading would mean item 1 was violated and per item-1's own line-30-31 the closure script is FORBIDDEN. The two readings of the same paragraph cannot both hold.

Resolution under the literal/independent reading (mine): item 1 PASSED (the closure script is acceptable at execution time), AND the count-threshold fired (the wave was over-scheduled). Both are simultaneously true. The closing paragraph is coherent.

Resolution under the conjunctive reading (gen-physicist's): if §"PLANNING DEFECT" fires conjunctively-with-NOT-item-1, then the closing paragraph's "remains acceptable" is structurally impossible — the script cannot be acceptable AND have been authored despite item 1 being violated, because item 1's own text (lines 30–31) makes such authoring FORBIDDEN. The closing paragraph becomes self-contradictory.

The rule-file's closing paragraph is the textual diagnostic. It assumes acceptability AT EXECUTION TIME concurrently with the trigger having fired. That is the literal/independent reading by direct textual evidence.

Re:G1's audit-script-evidence argument (workshop lines 846–855) — that the audit script does NOT have a 5th step checking wave-count, therefore §"PLANNING DEFECT" must be conjunctively-composed — is structurally backwards. The audit script's items (i)-(iv) are PER-CLOSURE checks (each closure line verified individually). The §"PLANNING DEFECT" clause is a WAVE-LEVEL diagnostic that operates on the AGGREGATE pattern across the wave. The audit-script architecture (per-line) and the §"PLANNING DEFECT" predicate architecture (per-wave) are at different scales; absence of a 5th per-line item is consistent with the wave-level diagnostic being a separately-implemented audit (or an unimplemented one) at a different scope. The absence is evidence of audit-script incompleteness, not of conjunctive composition.

**D2: Even granting multi-axis structure of the methodology-IS observable, the rule's TRIGGER predicate is keyed on count alone — and that is the right design.**

Per C1 above, the OBSERVABLE is multi-axis. But the TRIGGER predicate selects which axes to consume. The rule-text at lines 276–281 names ONE axis: "the closure script's covered-gate count." It does not name DPP-routing-count, item-1-status, or any other axis. Re:S6 EMERGES (workshop lines 781–786) attempts to derive multi-axis trigger composition from the rule-file's surrounding control flow; D1 above shows the surrounding control flow does not support that derivation.

The structural argument FOR keying the trigger on count alone (not against gen-physicist's reading, but on the merits):

- The §"PLANNING DEFECT" clause exists to detect a PATTERN that is invisible at the per-closure layer (where item 1 already polices admissibility). The per-closure layer answers "is THIS closure script acceptable?"; the wave-level layer answers "did the WAVE schedule too many prereq-conditional gates?" These are different observables at different scales.
- A wave that ANTICIPATES 4 prereq-block routings (W7c) and a wave that DOES NOT anticipate them (hypothetical W7c-prime) PRODUCE THE SAME EMPIRICAL OUTCOME at the wave level: 4 closures, 1.5× carry-forward inflation, deferred work cluster. The empirical signal of OVER-SCHEDULING (the rule's stated consequent at line 277-278: "the wave plan was OVER-OPTIMISTIC about prerequisite landings") is INVARIANT under whether the planner anticipated the failure mode. Knowing the ship will hit the iceberg is not the same as steering away from it.
- A trigger keyed on "count AND not-anticipated" (gen-physicist's reading) cancels precisely on waves where the planner KNEW the wave was over-scheduled and went forward anyway. That is the WORST class of waves to exempt — those are the waves where the planning-defect signal is most diagnostic.

**D3: The "anticipated-cluster exemption" clause has a falsifiability problem that gen-physicist's Re:S3 §"MISSED" response does not fully resolve.**

Re:S3 §"MISSED" (workshop lines 580–583) proposes the falsifier for "anticipated" is "the presence of a per-prereq routing instruction with a NAMED blocked-by symbol AND a forward-pointer to the missing artifact." Gen-physicist argues `_mechanical_closure_audit.py` already greps for this pattern, so the structural test is grep-able and falsifiable.

NEW EVIDENCE — the falsifier as proposed selects the EMPTY SET in practice:

- Per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1 (lines 25-31): "every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's downstream decision-point table specifies the documented outcome for prereq-block (typically 'PRE-REG-INC, deferred to S{N+1}')."
- Item 1 ALREADY REQUIRES per-prereq routing instructions with named blocked-by symbols at plan-pre-registration time. A wave that lacks such instructions VIOLATES item 1 and per lines 30-31 is "post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN."
- Therefore: any wave that REACHES the §"PLANNING DEFECT" diagnostic has, by item-1 admissibility, ALREADY pre-registered routing instructions with named blocked-by symbols.
- Therefore: under gen-physicist's "anticipated cancels" reading, the trigger's antecedent ("count ≥ 4 AND ≥1 covered gate's blocked-by symbol does NOT appear in the plan's DPP routing instructions") is structurally impossible to satisfy without simultaneously violating item 1 — which routes the wave to plan-freeze halt, where it never reaches the §"PLANNING DEFECT" diagnostic.

The falsifier IS grep-able. The grep result is GUARANTEED to be empty by the structure of item 1's plan-freeze enforcement. The K-counter has no observation window that does not also route the wave to a more upstream halt. This is a structural — not rhetorical — argument that the K=3 promotion threshold is unreachable under gen-physicist's reading.

Re:S4 hypothetical W7c-prime (workshop lines 653–655) attempts to escape this collapse: "a wave plan that lists 4 covered gates ... where the plan's §'Decision Point Prerequisites' section either (a) is absent entirely, or (b) lists routing instructions for fewer than 4 of the 4 prerequisites. At dispatch time, all 4 prerequisites are absent and the closure-script authors emit PRE-REG-INC."

But this hypothetical violates item 1 by construction (case (a) has no DPP at all; case (b) has routing for fewer-than-the-needed gates). Per item 1's lines 30-31, the producing closure scripts in this hypothetical are FORBIDDEN at authoring time. The closure scripts cannot be honestly authored; if they are authored, the audit detects the item-1 violation FIRST (per `_mechanical_closure_audit.py` items i-iv on per-closure verification), and the wave never reaches the §"PLANNING DEFECT" wave-level diagnostic — the wave halts at the per-closure audit.

In other words: gen-physicist's hypothetical W7c-prime is ALREADY ruled out by item-1 enforcement BEFORE the §"PLANNING DEFECT" predicate is evaluated. The hypothetical does not provide an observation window for the K-counter; it provides a window for item-1 audits to fire, which is a different rule-fire entirely. K_planning_defect remains structurally at 0 under the conjunctive reading.

**D4: The Re:G2 in-session amendment is technically distinct from Class-3 (per C4) but structurally adjacent to RULE-LAYER post-hoc editing in response to a verdict on disk — and the structural-adjacency objection survives the technical-distinctness concession.**

I conceded at C4 that the WP §2 amendment is technically distinct from Class-3 because it does not touch verdict-line content. But the structural HAZARD that Class-3 was designed to police — "amend the audit-trail label after seeing the on-disk record" — is preserved at the methodology layer under F. The amendment's IMAGE under F is "edit the rule-classification label of a calibration-corpus instance after the WP synthesis declared it." Under `joint-theorem-promotion.md` STAGE-1 → STAGE-3 promotion, the LABEL CHANGE is FORWARD: STAGE-1-CANDIDATE → STAGE-3-PERMANENT after Stage-2 PASS-AND verifies. Under Re:G2's amendment, the LABEL CHANGE is BACKWARD: instance-#1 → instance-#0 (structural-baseline / no-fire) after a workshop adjudication.

NEW EVIDENCE — the directional asymmetry:

- Forward label-change (joint-theorem-promotion): adds new evidence (Stage-2 PASS-AND verdicts), tracks more-confident classification.
- Backward label-change (Re:G2 amendment): retracts prior classification, tracks less-confident classification AGAINST WP-recorded determination.

The structural objection is: forward label-changes and backward label-changes do not have the same epistemic status. Forward changes track new evidence accumulating; backward changes track interpretive disagreement with the prior-recorded reading. Re:G2's amendment is the BACKWARD direction. If backward label-changes are admitted as routine in-session amendments, ANY future workshop can retract any prior session's calibration-corpus declaration by adjudicating a new rule-reading. The K-counter becomes a moving target: a count of CURRENT readings, not of PRIOR observations.

This is the methodology-layer F-image of post-hoc threshold editing's hazard, even though the TECHNICAL definition of Class-3 (substrate-layer threshold) does not apply. The hazard structure IS preserved under F. Re:G2's amendment may be technically licit, but it has a structural cost: future workshops could routinely retract prior calibration declarations on rule-reading-disagreement grounds, and the K-counter loses its function as an audit of accumulated observations.

The cleaner forward path: keep the WP §2 declaration AS RECORDED (W7c is instance #1 under the literal reading at session-close). Land the rule-file edit (per C2 / C3 / E2) for FUTURE waves. Apply the new rule prospectively, not retroactively. This preserves both the audit trail and the rule's forward signal.

### EMERGENCE

Cross-pollination from the sagan + gen-physicist exchange surfaces three new structural insights worth pinning explicitly.

**E1: The rule-file effectively names TWO distinct calibration corpora that should be tracked at separate sites.**

Re:S4 §"EMERGES" (workshop lines 656–658) proposed tracking "TWO calibration corpora, not one." The structural reason: count-keyed observations and unanticipated-cluster observations are non-redundant.

- **Corpus A — count-fires (literal reading; sagan's S3/S4)**: tracks waves where covered_gate_count ≥ 4. W7c is instance #1. The corpus is non-empty, advances at structurally-distinct waves regardless of pre-registration discipline. K=3 promotion is reachable in finite future sessions.
- **Corpus B — unanticipated-cluster (conjunctive reading; gen-physicist's Re:S1/G1)**: tracks waves where covered_gate_count ≥ 4 AND item-1 is violated. K = 0 currently and structurally guaranteed to remain 0 by upstream item-1 enforcement (per D3 above).

Both corpora are observable at session-close. Both have structurally well-defined predicates. Their non-equivalence is the substantive disagreement of this workshop. The forward path that LANDS BOTH (rather than picking one) is to:

1. Pin the literal-text count-fires reading at the existing §"PLANNING DEFECT" clause (status: SUGGESTION at K=1 with W7c as instance #1; promote to MANDATORY at K=3).
2. Pin the unanticipated-cluster reading at a NEW sub-section "When mechanical closure indicates an UNANTICIPATED-PREREQ-CLUSTER" with its own K-counter at K=0 (with the structural caveat that K=3 is unreachable until/unless an item-1-violating wave bypasses plan-freeze enforcement, which is itself a higher-priority audit defect).

This is a STRUCTURALLY HONEST resolution: it does not force one reading to subsume the other; it acknowledges both are distinct methodology-IS observables; it lets each corpus accumulate its own evidence at its own scale.

**E2: The forward-pinned-follow-up wave class is a structurally novel category — W7c is its first instance — and admits its OWN dedicated rule.**

Independent of the §"PLANNING DEFECT" adjudication, W7c is the FIRST forward-pinned-follow-up wave in the framework's history (a wave deliberately scheduled with prereq-block routing to consume MACHINERY landings expected to come from a parallel/upstream wave in the same session). This category is structurally NEW.

Forward-pinned-follow-up waves have a distinct empirical signature visible at session-close:

| Property | Generic compute wave | Forward-pinned-follow-up wave |
|:---------|:---------------------|:------------------------------|
| Prereq landings | All landed pre-wave-dispatch | Some/all expected mid-session |
| DPP routing-instruction count | 0 or low | High (one per prereq-block) |
| Carry-forward queue | Small (<25% of wave budget) | Large (close to or > wave budget) |
| Item-1 status at execution | Trivially satisfied | Decisively satisfied via DPP enumeration |
| §"PLANNING DEFECT" trigger | Rarely fires | Reliably fires (under literal reading) |

A dedicated rule for forward-pinned-follow-up waves SHOULD pre-register split-discipline (E1's Corpus A operationalization) so future planners have explicit guidance at plan-freeze. The seed proposal:

```
### Forward-pinned-follow-up wave discipline (NEW sub-section
###  candidate at .claude/rules/wave-classification.md or new
###  rule-file)

A wave W is FORWARD-PINNED-FOLLOW-UP iff:
  - its plan §"Decision Point Prerequisites" section enumerates
    routing instructions for ≥1 covered gate
  - the routing instruction's blocked-by symbol points to a
    machinery / data landing not yet on disk at plan-freeze
    (i.e., expected to be produced mid-session)

For forward-pinned-follow-up waves with PB(W) ≥ 4:
  - SPLIT_REQUIRED at plan-freeze (per S5 / Re:S5 heuristic)
  - W{N}_machinery handles the prereq landings
  - W{N+1}_verify consumes them
  - Single-wave execution at PB ≥ 4 advances Corpus A by 1
    (per E1)
```

This sub-section is independent of the §"PLANNING DEFECT" rule's adjudication. It captures the empirical forward template AT THE PROPER LAYER (planner-skill / wave-classification) without disturbing the calibration-corpus accounting.

**E3: The layer-functor F image of the §"PLANNING DEFECT" trigger predicate has a multi-axis observable but a single-axis trigger — and these are DIFFERENT under F.**

This is the synthesis of C1 + D2 + Re:S6.

Under the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`), the substrate-IS observable on a wave's plan artifact maps to a methodology-IS multi-axis tuple (covered_count, DPP_routing_count, item_1_status_per_gate, per-gate-routing-match). This is the OBSERVABLE — what the methodology-layer artifact STRUCTURALLY IS.

The TRIGGER PREDICATE is a separate map: it selects which axes of the observable to consume. Under the literal-text reading of lines 276–281, the trigger consumes ONE axis (count). Under the conjunctive reading proposed at Re:S1 / G1, the trigger consumes a Boolean combination of multiple axes.

These are DISTINCT under F:
- F(observable) = multi-axis tuple
- F(trigger predicate) = function from the observable to {true, false}

The substrate-IS framing rule (`phononic-framing.md §"IS Space, Not IN Space"`) governs F(observable) — preserve the structural content; don't project. It does NOT govern F(trigger predicate) — the trigger predicate is whatever the rule-text says it is. Re:S6's argument that single-axis trigger violates substrate-IS framing conflates these two F-images.

The methodology-layer correct framing:
- The OBSERVABLE on a plan artifact IS multi-axis (preserved per substrate-IS).
- The TRIGGER on a rule-clause IS whatever-the-rule-text-says (possibly single-axis, possibly multi-axis; determined by rule-text-evidence, not by substrate-IS framing).

Both readings (mine: trigger keyed on count alone; gen-physicist's: trigger keyed on count-AND-item-1-status) preserve multi-axis observable structure. The disagreement is over trigger composition, settled by rule-text. D1 + D3 above are the rule-text arguments.

This emergence clarifies the phononic-framing rule's scope at the methodology layer: substrate-IS framing applies to the OBSERVABLE (preserve structural content), not to the TRIGGER (which is a textual artifact of the rule-author's choice). Future workshops adjudicating rule-trigger composition should not invoke substrate-IS framing on the trigger side; they should invoke rule-text-evidence.

### QUESTIONS

I answer gen-physicist's G3 questions Q1–Q5 explicitly, then pose 2 sharper follow-up questions for the final round.

**Answer to G3 Q1 (where does the conjunctive antecedent come from)**: The line-22 lead-in "ONLY when ALL of the following hold" governs items 1–5 of §"When mechanical closure IS acceptable" — specifically, those 5 items are CLOSURE-AUTHORIZATION conditions. The line-22 phrase does NOT extend its scope to a different ##-level subsection (lines 274–286 §"PLANNING DEFECT") that follows ~250 lines later in the rule-file. Markdown headings at the same ##-level are siblings, not nested. A line-22 lead-in for one ## subsection does not impose conjunctive composition on a later ## subsection unless the later subsection cites the first explicitly.

The "INDICATES" verb at line 274 names the directionality of the diagnostic ("the closure script's shape INDICATES something about the plan"); it does not entail conjunctive composition with item 1. It entails sequential ordering: closure has already been authored (per upstream items 1-5 admissibility), then the §"PLANNING DEFECT" diagnostic reads the wave-level pattern. Sequential dependency ≠ conjunctive composition. Specifically, sequential dependency is consistent with the literal-independent reading: closure script PASSed item 1 (the script is acceptable AT EXECUTION TIME, per line 282-286 explicitly), AND the count-threshold fired (the wave was over-scheduled). The closing paragraph's "remains acceptable" is COHERENT under the literal-independent reading and INCOHERENT under the conjunctive reading (per D1 above). That paragraph is the textual diagnostic.

**Answer to G3 Q2 (falsifier for "count alone fires")**: The falsifier under my reading is straightforward: a wave with covered_gate_count < 4 does NOT trigger. Concrete examples:

- A wave with 3 covered gates regardless of item-1 status — does not trigger (count = 3 < 4).
- A wave with 1 covered gate even if item 1 violated — does not trigger via §"PLANNING DEFECT" (count = 1 < 4); separately FAILs at item-1 audit per `_mechanical_closure_audit.py` items i-iv.
- A wave with 0 covered gates — does not trigger.

Re:G3 Q2's question about "the structural class of W-shapes that fires §'PLANNING DEFECT' while NOT triggering a prior, more specific PROHIBITED_ACTIONS" is the right discriminator. Under my reading, W7c IS that structural class: a wave that fires §"PLANNING DEFECT" (covered_count ≥ 4) WHILE NOT triggering Class 1/4/6 (no convention-shopping, no ansatz-forced PASS, no iterate-until-PASS — all 4 closures are honestly emitted under item-1-compliant pre-registration). The discriminator's answer is "wave-scheduled-too-much-prereq-conditional-work-even-under-item-1-compliance." That IS what the rule's stated consequent at line 277-278 names: "the wave plan was OVER-OPTIMISTIC about prerequisite landings." The diagnostic is a SCHEDULING signal, not an authoring signal — both are valid signals at different layers, and §"PLANNING DEFECT" is the scheduling one. Re:G3 Q3's challenge "Should this diagnostic live in mechanical-closure-discipline.md, or in a dedicated planner-skill rule?" — my answer is BOTH; per E1, two separate corpora at two separate locations.

**Answer to G3 Q3 (concrete edit text test on W' and W'')**: Apply my S3 affirming clause to gen-physicist's hypotheticals:

- **W' (5 covered, 4 prereqs land successfully, 1 emits PRE-REG-INC; covered_count = 1)**: Under my reading, NOT triggering the diagnostic — covered_count = 1 < 4. Correct as gen-physicist already notes. Falsifier holds.
- **W'' (5 covered, all 5 prereqs absent, all 5 emit PRE-REG-INC; covered_count = 5)**: Under my reading, TRIGGERING (count = 5 ≥ 4). Calibration-corpus instance #2.

Re:G3 Q3's challenge: "But W'' is structurally on the IS-acceptable item-1 clean path. Under your reading, item-1-clean waves CAN fire §'PLANNING DEFECT' purely on count. What does that fire ACTUALLY diagnose if not the absence of pre-registration?"

My answer: it diagnoses OVER-SCHEDULING — exactly what the rule's stated consequent (line 277-278) names. A wave that schedules 5 covered gates with all 5 prereqs absent AT DISPATCH TIME is empirically a wave that bet on 5 separate machinery/data landings happening before W{N} dispatch and lost on all 5. That is "OVER-OPTIMISTIC about prerequisite landings" by the rule's own definition. Item-1-compliant pre-registration prevents post-hoc plan editing of the closure scripts; it does NOT prevent over-optimistic scheduling at plan-freeze. The two are different failure modes at different layers.

Re:G3 Q3's final challenge: "Should this diagnostic live in mechanical-closure-discipline.md, or in a dedicated planner-skill rule?" My answer: BOTH per E1. The mechanical-closure rule retains the count-keyed §"PLANNING DEFECT" diagnostic (Corpus A); a NEW planner-skill rule consumes the heuristic (per C2) AND the carry-forward-displacement metric (per C3). Three landings, three corpora, three K-counters. No collapse; each captures a structurally distinct signal.

**Answer to G3 Q4 (K-counter advancement under my reading)**: Yes, my forward expectation is that future sessions COULD produce additional count-≥-4 instances, and my forward EXPECTATION is that they SHOULD NOT — per the WP §"Next-step routing" line 1042 guidance and the SPLIT_REQUIRED heuristic at C2. Re:G3 Q4 frames this as a contradiction ("the rule reaches MANDATORY status only if a future session produces a similar wave PATTERN — which is exactly the pattern your forward template tells planners to AVOID"); I read it as the rule WORKING. The point of a calibration-corpus K-counter is to track instances of a structural pattern that ought to be rare; the rule fires DIAGNOSTICALLY when the pattern recurs, not as an indictment of pattern-occurrence. K=3 promotion would mean three structurally-distinct waves fired the over-scheduling pattern — that IS evidence the pattern is recurrent enough to warrant MANDATORY status. K stays at 1 if the pattern does NOT recur — that is also evidence (the rule did its job by surfacing W7c's lesson).

The "sociological metric of planner-skill maturity" framing in Re:G3 Q4 is a feature, not a bug. Calibration corpora at K=3 are sociological metrics by design — they capture how often a structural failure pattern recurs across sessions. The §"Layer-separability carve-out" calibration corpus at `mechanical-closure-discipline.md` lines 191-195 is explicitly tracked the same way. The K=3 threshold encodes the framework's policy that 3 instances of any pattern warrant MANDATORY status. Whether the pattern is "structural physics observable" or "wave-scheduling structural observable," the K-counter accounting is the same.

**Answer to G3 Q5 (multi-axis preservation under F)**: Per E3 above, the methodology-IS observable IS multi-axis (preserved per substrate-IS framing) AND the trigger predicate IS keyed on count alone (per rule-text). These are different F-images, governed by different framing rules:

- F(observable) = (covered_count, DPP_routing_count, item_1_status_per_gate, per-gate-routing-match) — preserved per substrate-IS framing.
- F(trigger predicate) = "covered_count ≥ 4" — determined by rule-text at lines 276-281.

The single-axis projection is at the trigger layer (rule-text-determined); not at the observable layer (artifact-determined). Substrate-IS framing does not constrain the trigger composition. The disagreement at C1 / D2 is over which axes the rule-author chose to consume; that is settled by rule-text-evidence (D1 + D3), not by framing-rule preservation.

The "something else" that my reading consumes beyond covered_count is: NOTHING. The trigger is single-axis on count alone per the rule-text. That is what the rule says; that is what it does. Multi-axis observable preservation does not extend to multi-axis trigger composition, and it is a category error to conflate them.

**Sharpened follow-up questions for the final round (FINAL Q1, FINAL Q2)**:

**FINAL Q1 (closing-paragraph-coherence test)**: Apply the conjunctive reading to lines 282-286 of `mechanical-closure-discipline.md`: "The closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson..." Under your conjunctive reading, the §"PLANNING DEFECT" trigger fires only when item 1 was VIOLATED. But item-1 violation per lines 30-31 makes the closure script FORBIDDEN ("the closure script is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN"). How can a FORBIDDEN closure script "remain acceptable AT EXECUTION TIME"? Either the conjunctive reading is wrong (closure script is NOT item-1-violating; the trigger fires on item-1-clean waves; my reading), OR lines 282-286 contradict lines 30-31 in the same rule-file. Which is it? Cite which lines you would amend to remove the contradiction under the conjunctive reading.

**FINAL Q2 (E1 two-corpora landing — endorsement or rejection)**: Per E1 (EMERGENCE), the cleanest forward path is to land BOTH (a) the literal-text count-fires reading at the existing §"PLANNING DEFECT" clause AND (b) a new "UNANTICIPATED-PREREQ-CLUSTER" sub-section codifying the conjunctive trigger you propose. Both lands produce two distinct calibration corpora at the same rule-file. W7c is instance #1 of (a); K=0 baseline of (b). Do you endorse this two-corpora resolution? If yes, the workshop verdict is PARTIAL-CONVERGENCE (both readings preserved at separate sub-sections). If no, the workshop verdict is DISSENT and the forward carry-forward must adjudicate which single reading lands. Pin your position so the wrap-up table is unambiguous.

---

## Round 2 — gen-physicist: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

After reading sagan's R2 CONVERGENCE / DISSENT / EMERGENCE / QUESTIONS in full, four sagan-axes legitimately move me. I state which substitution chain forces the concession in each case and what the concession does and does NOT entail.

**CG1: I CONCEDE D1 — the closing-paragraph-coherence test on lines 282-286 vs lines 30-31 is a structural defect of the strict conjunctive reading.**

Sagan's D1 (workshop lines 991-1009) lands the strongest objection of the workshop. The argument has the form of an internal-consistency check on `mechanical-closure-discipline.md` rule-text:

```
Substitution chain (closing-paragraph-coherence on rule-file as artifact):

Step 1 (Definition):
  CR_para  := mechanical-closure-discipline.md lines 282-286:
              "The closure script remains acceptable AT EXECUTION TIME
               (preserving the audit trail honestly), but the next
               session's planner MUST log this as a plan-authorship
               lesson..."
  CR_para's antecedent context := the §"PLANNING DEFECT" trigger has
                                   FIRED (i.e., covered-count ≥ 4)
  CR_para's stated consequent  := "closure script remains acceptable
                                    AT EXECUTION TIME"

  Item_1_clause := mechanical-closure-discipline.md lines 30-31:
                   "if the plan does not address [the prereq-block
                    scenario], the closure script is post-hoc plan
                    editing (PROHIBITED_ACTIONS Class 3) and is
                    FORBIDDEN."

  Conjunctive_reading_pred(W) := PLANNING_DEFECT trigger fires
                                  iff (covered_count(W) ≥ 4) AND
                                  NOT(IS_acceptable_item_1(W))

Step 2 (Substitution under my Re:S1 conjunctive reading):
  When the trigger fires under conjunctive_reading_pred:
    NOT(IS_acceptable_item_1(W)) = TRUE
    => plan does NOT pre-register absent-prereq routing
    => per Item_1_clause lines 30-31: closure script FORBIDDEN
    => closure script CANNOT be authored

  But CR_para asserts: "closure script REMAINS ACCEPTABLE AT
  EXECUTION TIME" precisely when the trigger fires.
  Under conjunctive_reading: the closure script is FORBIDDEN
  (per item 1) AND simultaneously acceptable (per CR_para).
  FORBIDDEN ∧ acceptable = ⊥ (contradiction).

Step 3 (Simplification):
  Conjunctive_reading_pred forces self-contradiction at lines
  30-31 vs 282-286. The rule-file as authored is internally
  inconsistent under the conjunctive reading.

Step 4 (Direction):
  My Re:S1/G1 conjunctive reading is structurally untenable as
  the literal reading of the rule-file as authored. Either
  (a) the conjunctive reading is wrong, OR (b) the rule-file
  has a textual contradiction at lines 30-31 vs 282-286.
  The principle of preferring the reading that does NOT entail
  textual contradiction (per Re:S6's "preserve structural
  content" framing applied to the rule-file artifact) selects
  (a). The conjunctive reading is wrong as a reading of the
  rule-file as authored.
```

Under this concession, the strict conjunctive reading I proposed at Re:S1 / Re:S2 / G1 / Re:S4 / G2 is ABANDONED as a reading of `mechanical-closure-discipline.md` AS CURRENTLY AUTHORED. The rule-file's closing paragraph at lines 282-286 explicitly assumes item-1 PASS at the moment the trigger fires; my reading was inconsistent with that assumption; sagan's literal-independent reading is consistent with it.

**What CG1 entails**: as a reading of the EXISTING rule-text, the literal/independent reading wins. W7c's covered_gate_count = 4 satisfies the bare conditional at lines 276-281 under the rule AS AUTHORED. My G2 amendment proposal that retracts WP §2's instance #1 declaration on conjunctive-reading grounds is undermined: the conjunctive reading itself is now untenable as a textual reading.

**What CG1 does NOT entail**: this is a CG on the READING of the existing rule-text. It is NOT a concession that the rule's existing text captures the right structural diagnostic. The rule-file as authored is INTERNALLY consistent under sagan's reading but DIAGNOSTICALLY IMPRECISE — it fires on item-1-clean waves AND would also fire on item-1-violating waves (which never reach it because of upstream halt). The two structurally distinct wave classes deserve two distinct calibration corpora; the rule-file's existing text does not distinguish them. Sagan's E1 two-corpora resolution is the correct forward path (see CG3 below).

**CG2: I CONCEDE D4's directional asymmetry argument — backward label-changes are structurally distinct from forward label-changes under F.**

Sagan's D4 (workshop lines 1040-1053) identifies that even though my G2 amendment is technically distinct from Class-3 (per sagan's C4), it sits in a different epistemic class than `joint-theorem-promotion.md`'s STAGE-1 → STAGE-3 forward promotion:

```
Substitution chain (directional asymmetry of label-change under F):

Step 1 (Definition):
  forward_label_change  := label change driven by ACCUMULATING
                            evidence (Stage-2 PASS-AND verdicts);
                            increases epistemic confidence in the
                            classification
  backward_label_change := label change driven by INTERPRETIVE
                            disagreement with the prior-recorded
                            reading; retracts a prior classification

  joint-theorem-promotion STAGE-1 → STAGE-3 := forward
  G2_amendment                              := backward

Step 2 (Substitution at G2):
  G2 amends WP §2 instance-#1 declaration → instance-#0 (no-fire).
  Driver: workshop adjudication, not new evidence.
  Direction: backward.

Step 3 (Simplification):
  Forward label-changes accumulate evidence. Backward label-changes
  REPLACE one reading with another. If backward changes are admitted
  routinely, every workshop becomes a potential retraction site for
  prior calibration-corpus declarations. The K-counter becomes
  "count of CURRENT readings" rather than "count of accumulated
  observations."

Step 4 (Direction):
  Even if technically licit (CG via C4 above), backward label-
  changes carry a structural cost the forward direction does not.
  The cleaner forward path is to LAND THE CORRECTED RULE-TEXT
  PROSPECTIVELY and leave WP §2's prior reading on disk as the
  session-close orchestrator's reading at that moment.
```

I CONCEDE: the WP §2 instance-#1 declaration STAYS AS RECORDED. The corrected rule-text lands prospectively (per CG3 below); the backward retraction of W7c's instance-#1 status is withdrawn. Future workshops do not get a precedent for routine backward retractions of session-end calibration declarations on rule-reading-disagreement grounds.

**CG3: I ENDORSE E1 — the two-corpora landing is the structurally honest forward path.**

Sagan's E1 (workshop lines 1059-1071) and FINAL Q2 (lines 1175-1177) propose landing BOTH (a) the literal-text count-fires reading at the existing §"PLANNING DEFECT" clause AND (b) a new sub-section codifying a more-restrictive trigger that would fire on item-1-violating clusters specifically.

I ENDORSE this resolution explicitly. Substitution chain:

```
Step 1 (Definition):
  Corpus_A := waves where covered_count(W) ≥ 4 (literal reading
              of existing §"PLANNING DEFECT" lines 276-281;
              fires regardless of item-1 status, but item-1-
              violating waves never reach this trigger because
              they halt upstream at the per-closure audit per D3)
  Corpus_B := waves where item-1 PASSES, BUT the wave's structural
              shape suggests over-scheduling along axes orthogonal
              to count (e.g., high DPP-routing-instruction count
              indicating heavy forward-pinning)

  Note: I am AMENDING my prior framing. My original "unanticipated-
  cluster" Corpus B (count ≥ 4 AND item-1 violated) is structurally
  empty per D3. The replacement Corpus B (forward-pinned-follow-up
  wave class per E2) is structurally non-empty and captures the
  signal sagan's heuristic at S5 + carry-forward-displacement metric
  at C3 jointly identify.

Step 2 (Substitution at W = W7c):
  Corpus_A status of W7c: instance #1 (covered_count = 4 ≥ 4;
                          rule-text reading at lines 276-281 is
                          the literal-independent reading per CG1)
  Corpus_B status of W7c: instance #1 of "forward-pinned-follow-
                          up wave class" (per sagan E2: 4 prereq-
                          block routings, 1.5× carry-forward
                          inflation, item-1 decisively satisfied)

Step 3 (Simplification):
  Both corpora have W7c as their first instance, but the two
  corpora measure DIFFERENT structural axes:
    Corpus A: covered_count axis at the closure-audit layer
    Corpus B: forward-pinning-density axis at the wave-classification
              layer
  Their non-equivalence is consistent with my Re:S6 multi-axis
  observable argument (which CG1 leaves intact at the OBSERVABLE
  level even after the TRIGGER-level concession; per E3 the two
  F-images are distinct).

Step 4 (Direction):
  Land both corpora at non-conflicting locations:
  - Corpus A: existing §"PLANNING DEFECT" clause stays as-is;
              the existing literal-reading trigger is correct;
              W7c is instance #1; status SUGGESTION at K=1.
  - Corpus B: NEW sub-section / new rule-file capturing the
              forward-pinned-follow-up wave class; W7c is instance
              #1 there too; status SUGGESTION at K=1.
  No collapse, no retraction, no internal contradiction.
```

The two-corpora landing IS the workshop verdict. Both readings (sagan's literal-independent on Corpus A; my forward-pinning structural class on Corpus B) preserve their content as separate rule-file constructs.

**CG4: I CONCEDE C2 / E3 — the heuristic-vs-rule-trigger distinction sharpens, and the layer-functor F's image at "trigger predicate" is rule-text-determined, not framing-rule-determined.**

Sagan's C2 (workshop lines 960-964) accepts my Re:S5 distinction between `/rclab-plan` skill-layer heuristics and rule-fire diagnostics as different layer-functor F images. I AGREE with this acceptance; the layer separation is symmetric.

Sagan's E3 (workshop lines 1111-1131) sharpens the F-image taxonomy: F(observable) on the methodology-IS plan artifact is multi-axis (preserved per substrate-IS framing); F(trigger predicate) is whatever-the-rule-text-says (determined by rule-text-evidence, not framing). I CONCEDE this separation. My Re:S6 argument that single-axis trigger reading violates substrate-IS framing was a category error: substrate-IS framing governs the OBSERVABLE-image of F, not the TRIGGER-image. The OBSERVABLE on the plan artifact is multi-axis (covered_count, DPP_routing_count, item_1_status_per_gate); the TRIGGER PREDICATE is single-axis on covered_count alone (per the rule-text at lines 276-281 read in conjunction with CG1's closing-paragraph-coherence test).

This concession does NOT undermine the multi-axis observable argument from Re:S6 — it RELOCATES it. The multi-axis structure remains correct as an OBSERVABLE-level property; the rule's existing TRIGGER simply consumes only one axis of it. Future rule-extensions could add a multi-axis trigger (per E2's forward-pinned-follow-up wave class consuming routing-density and item-1-status); the current rule does not.

### DISSENT

Three dissent axes remain after CG1-CG4. Each is sharpened by NEW evidence rather than restating Round 1 positions; sagan's R2 specifically requested this.

**DG1: D2's "trigger keyed on count is the right design" merits argument is INCOMPLETE without the two-corpora resolution.**

Sagan's D2 (workshop lines 1011-1019) argues count-only triggering is the right design because:
- The §"PLANNING DEFECT" clause exists to detect a wave-level pattern invisible at the per-closure layer.
- Anticipated and unanticipated waves PRODUCE THE SAME EMPIRICAL OUTCOME at the wave level (same carry-forward inflation, same deferred work cluster).
- Count-AND-not-anticipated cancels precisely on the worst class to exempt.

I ACCEPT D2's first claim (per CG3, Corpus A IS that wave-level diagnostic at the count axis). I PARTIALLY ACCEPT D2's second claim. I REJECT D2's third claim as an artifact of the false binary "single-corpus or no-corpus."

NEW EVIDENCE — count is not the only wave-level invariant:

```
Substitution chain (wave-level invariants beyond count):

Step 1 (Definition):
  carry_forward_displacement(W) := total_carry_forward_effort(W)
                                    / W.budget
                                  (the metric sagan endorsed at C3)
  forward_pinning_density(W)    := DPP_routing_count(W) /
                                    covered_count(W)
                                  (a structural property at plan-
                                  freeze, NOT a session-close
                                  measurement)
  item_1_compliance_rate(W)     := count of covered gates with
                                    pre-registered routing /
                                    covered_count(W)

Step 2 (Substitution at W = W7c vs hypothetical W7c-prime):
  W7c (anticipated, item-1-PASS):
    carry_forward_displacement = 5.6 / 3.8 = 1.47×
    forward_pinning_density    = 4 / 4    = 1.00
    item_1_compliance_rate     = 4 / 4    = 1.00
  W7c-prime (unanticipated, item-1-violating, hypothetical only):
    carry_forward_displacement = (similar; 1.47×)
    forward_pinning_density    = 0 / 4    = 0.00
    item_1_compliance_rate     = 0 / 4    = 0.00

Step 3 (Simplification):
  D2's "same empirical outcome at the wave level" is TRUE for the
  count axis AND for the carry-forward-displacement axis.
  D2's "same empirical outcome" is FALSE for the forward-pinning-
  density axis AND the item-1-compliance-rate axis. These two
  axes structurally DISTINGUISH W7c from W7c-prime.

Step 4 (Direction):
  Count-only triggering is sufficient for ONE diagnostic axis
  but not for ALL diagnostic axes. The two waves W7c and W7c-prime
  hit the count threshold identically but differ on forward-
  pinning-density and item-1-compliance. A rule-system that
  surfaces ONLY the count-axis diagnostic loses the structural
  distinction. The two-corpora landing per CG3 RESTORES that
  distinction at separate corpora; D2's argument FOR count-only
  triggering is correct as a stand-alone design choice but is
  not the ONLY design choice that captures the wave-level
  signal.
```

The residual dissent: D2's "trigger keyed on count is RIGHT" is admissible only as "trigger keyed on count is CORRECT FOR CORPUS A." It does NOT establish that no other corpus should track a different axis. Sagan's E1 two-corpora resolution (which I endorsed at CG3) supersedes the D2 single-corpus framing. The merits argument supports Corpus A's count-trigger; it does NOT defeat Corpus B's structural-class trigger.

**DG2: D3's "falsifier-empty-set" argument applies to my OLD framing (item-1-violating Corpus B) but does NOT apply to E2's forward-pinned-follow-up wave class.**

Sagan's D3 (workshop lines 1021-1038) argues that my proposed "anticipated-cancels" exemption clause selects the empty set because item-1-violating waves halt upstream at the per-closure audit. I AGREE this argument is structurally correct AGAINST my original Re:S3 / Re:S4 framing where Corpus B was "count ≥ 4 AND item-1 violated."

NEW EVIDENCE — Corpus B's redefinition under E2 makes the falsifier non-empty:

```
Substitution chain (Corpus B's observable window after E2 redefinition):

Step 1 (Definition):
  Corpus_B_old := waves where covered_count ≥ 4 AND item-1 violated.
                  Empty by D3 (item-1-violating waves halt upstream).
  Corpus_B_new := waves classified as FORWARD-PINNED-FOLLOW-UP per
                  E2 with PB(W) ≥ 4. Item-1 PASSES for these waves
                  (they are on the IS-acceptable clean path);
                  the structural marker is high forward-pinning
                  density, NOT item-1 violation.

Step 2 (Substitution at W = W7c):
  Corpus_B_old(W7c) = NOT-COUNTED (item-1 PASSES → out of scope).
  Corpus_B_new(W7c) = COUNTED as instance #1 (PB(W7c) = 4 ≥ 4 AND
                       forward-pinning-density = 1.00).

Step 3 (Simplification):
  Corpus_B_new has a non-empty observation window. The trigger
  predicate is "PB(W) ≥ 4 AND every covered gate has a pre-
  registered absent-prereq routing instruction" — a structural
  property visible at plan-freeze, NOT a violation of item 1.

Step 4 (Direction):
  D3 is correct against Corpus_B_old; D3 is NOT correct against
  Corpus_B_new. The redefinition of Corpus B per E2 escapes the
  falsifier-empty-set collapse. Corpus B's K-counter has a
  reachable K=3 promotion threshold via future forward-pinned-
  follow-up waves that hit PB(W) ≥ 4 and execute single-wave
  rather than splitting per E2's recommendation.
```

The residual dissent: D3 is correct on the historical framing but NOT on the E2-redefined framing. Both readings can be honestly tracked: Corpus A advances on count-fires (sagan's literal trigger); Corpus B advances on forward-pinned-follow-up-density (the E2 structural-class trigger). Both have non-empty observation windows. Both are reachable to K=3 promotion in finite future sessions.

**DG3: The forward-pinned-follow-up wave class (E2) deserves PRE-REGISTRATION at the rule-file layer, not just the planner-skill layer.**

Sagan's E2 (workshop lines 1073-1109) proposes the forward-pinned-follow-up wave class be pre-registered at `.claude/rules/wave-classification.md` or a new rule-file. Sagan's C2 endorses pinning split-discipline at the `/rclab-plan` skill layer specifically.

I PARTIALLY DISAGREE. The split-decision HEURISTIC (sagan's S5 PB(W) ≥ 4 → SPLIT_REQUIRED) belongs at the planner-skill layer (concur with C2). The wave-CLASS DEFINITION (forward-pinned-follow-up = wave with PB(W) ≥ 1 and DPP routing instructions to mid-session-expected machinery landings) belongs at the RULE-FILE layer alongside METHODOLOGY-class / COMPUTE-class / MIXED-class taxonomy in `wave-classification.md`.

NEW EVIDENCE — wave-class definitions live at the rule-file layer per existing convention:

```
Substitution chain (where wave-class definitions live in the framework):

Step 1 (Definition):
  rule-file layer pre-registration site:
    .claude/rules/wave-classification.md (existing)
    enumerates METHODOLOGY-class, COMPUTE-class, MIXED-class
    with M1-M4 conjunction tests
  planner-skill layer pre-registration site:
    .claude/skills/rclab-plan (skill-text)
    consumes class definitions to make split decisions

Step 2 (Substitution for forward-pinned-follow-up class):
  Class definition (per E2): forward-pinned-follow-up = wave with
    DPP routing instructions for ≥1 covered gate where blocked-by
    symbol points to a not-yet-on-disk machinery/data landing.
  Class properties: forward-pinning-density, item-1-compliance,
    carry-forward-displacement-eligibility.
  These are structural properties of the class, parallel to
    METHODOLOGY-class's M1-M4 conjunction.

Step 3 (Simplification):
  By analogy to METHODOLOGY-class definition living at
  wave-classification.md (not at the rclab-plan skill layer),
  the forward-pinned-follow-up class definition belongs at
  wave-classification.md.
  The split-decision HEURISTIC (PB(W) ≥ 4 → SPLIT) consumes the
  class definition and belongs at the planner-skill layer
  (per CG via C2).

Step 4 (Direction):
  Two landings, two layers, non-redundant:
    (a) wave-classification.md: forward-pinned-follow-up class
        definition + Corpus B trigger.
    (b) rclab-plan skill text: split-decision heuristic
        consuming the class.
  Sagan's E2 says "wave-classification.md OR new rule-file"
  (workshop line 1091); my dissent narrows this to
  wave-classification.md SPECIFICALLY by the analogical argument.
```

The residual dissent: sagan's E2 leaves the rule-file landing site optional. I argue the analogy with METHODOLOGY-class / COMPUTE-class / MIXED-class taxonomy at `wave-classification.md` makes that the structurally-natural landing site. This is a small, technical dissent that does not affect the workshop verdict but is worth pinning for the next-session planner.

### EMERGENCE

Three new structural insights cross-pollinate from the C1-C4 / D1-D4 / E1-E3 exchange. Each is independent of the original 6-topic agenda and is worth pinning for future workshops.

**EG1: The closing-paragraph-coherence test (sagan's D1) is itself a NEW rule-text-audit pattern — the "internal-consistency-of-conjunctive-vs-independent-readings" test — that should be pinned as a methodology rule extension.**

The argument shape sagan deployed at D1 is: applying a candidate rule-reading to the rule-file's CLOSING paragraph reveals whether that reading creates internal contradictions with EARLIER paragraphs in the same rule-file. If the candidate reading produces self-contradiction, the candidate reading is structurally untenable as a reading of the rule-file as authored.

This is a NEW methodology audit pattern. It is not currently codified. It is worth lifting to a methodology rule:

```
Proposed extension (candidate landing site:
  .claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"
  OR a new sub-section of mechanical-closure-discipline.md
  documenting the audit pattern):

### Closing-paragraph-coherence test for rule-text composition

When two or more candidate readings of a rule-clause are under
adjudication, apply the closing-paragraph-coherence test:

1. Identify the rule-file's CLOSING paragraph for the section
   containing the disputed clause.
2. Test each candidate reading by substituting the reading into
   the closing paragraph's stated context.
3. If a candidate reading produces internal contradiction with
   EARLIER paragraphs in the same rule-file (in particular: if
   the reading's antecedent makes the closing paragraph's
   consequent structurally impossible to satisfy), the candidate
   reading is REJECTED as a reading of the rule-file as authored.
4. If no candidate reading passes the test, the rule-file itself
   has a textual contradiction and routes to MANDATORY remediation
   per the v3-closure-recovery audit protocol.

Calibration: S88 W-25 (this workshop). Conjunctive reading of
mechanical-closure-discipline.md §"PLANNING DEFECT" produced
self-contradiction at lines 30-31 vs 282-286; reading rejected.
Literal-independent reading is internally consistent; reading
accepted.
```

This is a forward-template emergence: the audit pattern itself, lifted from the W-25 specific argument to a general methodology tool. K-counter at K=1 (W-25 calibration); promote to MANDATORY at K=3.

**EG2: The disambiguation between F(observable) and F(trigger predicate) at the layer-functor F (sagan's E3) is itself a layer-decomposition refinement worth pinning at `epistemic-discipline.md §"Layer-Decomposition"`.**

Sagan's E3 separates F into two distinct images:
- F(observable) at the methodology layer = multi-axis tuple representing the artifact's structural content.
- F(trigger predicate) at the methodology layer = function from observable to {true, false} determined by rule-text.

The substrate-IS framing rule (`phononic-framing.md §"IS Space, Not IN Space"`) governs F(observable) — preserve the structural content. It does NOT govern F(trigger predicate) — the trigger is whatever the rule-text says.

This separation is currently implicit in the framework. Lifting it to explicit rule-text closes a category-error pathway visible at this workshop (my Re:S6 argument that single-axis trigger violates substrate-IS framing was exactly this category error).

```
Proposed extension to .claude/rules/epistemic-discipline.md
§"Layer-Decomposition":

### F-image decomposition: observable vs trigger predicate

The layer-functor F maps a substrate-physics object to a
methodology-layer artifact. The methodology-layer artifact admits
TWO distinct sub-images under F:

1. F(observable): the methodology-IS structural content of the
   artifact. Multi-axis by construction. Preserved per substrate-IS
   framing (per `phononic-framing.md §"IS Space, Not IN Space"`).
   Container-thinking violations at this layer collapse the
   multi-axis structure to a single-axis projection.

2. F(trigger predicate): the rule-text-determined function from the
   observable to {true, false}. Possibly single-axis, possibly
   multi-axis. Determined by rule-text-evidence, NOT by substrate-IS
   framing. Substrate-IS framing does NOT constrain trigger
   composition.

Conflating F(observable) and F(trigger predicate) is a category
error. Substrate-IS framing applies ONLY to F(observable).
Rule-text-evidence applies ONLY to F(trigger predicate).

Calibration: S88 W-25 (this workshop). My Re:S6 argument that
single-axis trigger reading violates substrate-IS framing was
this category error; sagan's E3 corrects it.
```

K-counter at K=1; promote to MANDATORY at K=3 per the standard.

**EG3: Workshop-internal R2 closing-paragraph test predicts a specific class of rule-file textual contradictions that may exist elsewhere in the framework.**

The W-25 closing-paragraph-coherence test surfaced one rule-file contradiction-candidate (lines 30-31 vs 282-286 under conjunctive reading) which was resolved by rejecting the conjunctive reading. But the technique is general: applying the closing-paragraph-coherence test to OTHER rule-files with multi-paragraph diagnostic clauses MAY surface rule-text-as-authored defects that have been latent.

Forward audit candidates (sites where two or more clauses of the same rule-file have antecedent-consequent structures that may produce conjunctive-vs-independent reading ambiguity):

- `.claude/rules/v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 1-7 vs the Stage 1/2/3 procedure: do the two structures admit conjunctive vs independent readings under different candidate compositions?
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause vs the K-counter advancement criteria: same question.
- `.claude/rules/joint-theorem-promotion.md` 4-stage pathway vs Stage-2 PASS-AND independence: same question.

This is a NEW carry-forward audit candidate, captured at CF #5 below: a sweep of rule-files for closing-paragraph-coherence testing. The K-counter on EG1 advances each time a new contradiction-candidate is surfaced and resolved.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Rule-trigger reading (sufficient vs necessary-and-anticipation) | S1, Re:S1, D1, CG1 | **Converged** (sagan reading wins) | Closing-paragraph-coherence test (D1) on lines 30-31 vs 282-286 forces rejection of the strict conjunctive reading: it makes the FORBIDDEN-AT-AUTHORING-TIME closure script simultaneously "remain acceptable AT EXECUTION TIME," which is self-contradiction. Literal-independent reading wins as a reading of the rule-file as authored. |
| 2 | Pre-registration anticipation status | S2, Re:S2, CG1 | **Converged** (multi-axis observable, single-axis trigger) | The methodology-IS observable on the W7c plan artifact IS multi-axis (covered_count, DPP_routing_count, item_1_status_per_gate); both agents agree. The TRIGGER predicate at the existing rule-file consumes count alone (per E3 separation of F(observable) from F(trigger predicate)). Anticipation does NOT cancel the count-keyed trigger. |
| 3 | Rule-file edit requirement (anticipation-cancels clause vs count-alone affirmation) | S3, Re:S3, E1, CG3 | **Emerged** (two-corpora landing) | Neither sagan's count-alone-affirming edit alone nor my anticipation-cancels exemption alone is the right edit. The structurally honest landing is BOTH: keep the existing §"PLANNING DEFECT" clause as-is (Corpus A, count-keyed) AND add a new sub-section codifying forward-pinned-follow-up wave class (Corpus B, structural-class-keyed via E2). |
| 4 | W7c K-counter status — instance #1 vs exempt-by-pre-registration | S4, Re:S4, G2, D4, CG2, CG3 | **Converged** (instance #1 of Corpus A; instance #1 of Corpus B) | W7c IS calibration-corpus instance #1 of Corpus A (count-keyed; sagan's reading) per CG1. W7c is ALSO instance #1 of the new Corpus B (forward-pinned-follow-up wave class; E2 redefinition). WP §2 declaration STAYS AS RECORDED per D4 directional asymmetry; the G2 backward-retraction amendment is WITHDRAWN. |
| 5 | Forward template for plan-authors (split vs single-wave forward-pinning) | S5, Re:S5, C2, C3 | **Converged** (heuristic at planner-skill layer; class definition at rule-file layer) | The PB(W) ≥ 4 → SPLIT_REQUIRED heuristic lands at the `/rclab-plan` skill layer (per C2). The forward-pinned-follow-up wave class definition lands at `wave-classification.md` (per DG3 by analogy with METHODOLOGY/COMPUTE/MIXED-class taxonomy). The carry-forward-displacement metric (1.5× wave-budget; ≥50% machinery-displacement items) lands as a separate planner-skill rule (per C3). Three landings, three layers. |
| 6 | Cross-cutting / substrate-framing of "planning-defect" | S6, Re:S6, G1, G2, E3, CG4 | **Emerged** (F-image decomposition) | F decomposes into F(observable) and F(trigger predicate) at the methodology layer. Substrate-IS framing governs F(observable) — preserve multi-axis structural content. Rule-text-evidence governs F(trigger predicate) — possibly single-axis, possibly multi-axis. Conflating them is a category error (my Re:S6 made this error; sagan's E3 corrected it). New rule-extension candidate at `epistemic-discipline.md §"Layer-Decomposition"` per EG2. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

The workshop converged on the two-corpora landing (CG3 / E1) and on rejection of the strict conjunctive reading (CG1 / D1) but produced concrete forward open questions of three kinds: (i) rule-file edit specifications, (ii) sweep-audit triggers, (iii) K-counter advancement protocols. Each is specific enough to become a computation gate or a session-plan workshop topic.

1. **Rule-file edit specification — closing-paragraph-coherence disambiguation clause for `mechanical-closure-discipline.md`**: Should the rule-file gain an explicit disambiguation clause stating "the §"PLANNING DEFECT" trigger fires on covered_count ≥ 4 INDEPENDENTLY of item-1 status, AND the closing paragraph's 'remains acceptable AT EXECUTION TIME' assumes item-1-PASS"? Pre-registered gate: `S89-MECH-CLOSURE-DISAMBIGUATION-CLAUSE-LAND` PASS = clause text appended after line 281 with cross-reference to W-25 calibration corpus AND to lines 30-31 item 1 explicit citation; FAIL = clause text not landed or contradicts the closing paragraph.

2. **Two-corpora landing structural decision — Corpus A keeps existing §"PLANNING DEFECT"; Corpus B lands where?**: Sagan's E2 leaves the rule-file landing site optional ("`wave-classification.md` OR new rule-file"). My DG3 narrows this to `wave-classification.md` by analogy with METHODOLOGY/COMPUTE/MIXED-class taxonomy. Pre-registered gate: `S89-WAVE-CLASS-FORWARD-PINNED-FOLLOWUP-LAND` PASS = forward-pinned-follow-up wave class definition appended to `wave-classification.md` with M1-M4-analog conjunction tests AND Corpus B trigger predicate explicitly stated; FAIL = landed at a non-`wave-classification.md` site OR class definition omits the forward-pinning-density observable axis.

3. **Carry-forward-displacement metric pre-registration — separate rule-file or extension to existing planner-skill rule?**: Sagan's C3 endorses the metric (1.5× wave-budget threshold; ≥50% machinery-displacement items). The landing site is undetermined. Candidate landings: (a) extension to `feedback_fix-in-session-never-defer.md`; (b) new dedicated `carry-forward-displacement-discipline.md`; (c) integration into `wave-classification.md` alongside Corpus B. Pre-registered gate: `S89-CF-DISPLACEMENT-METRIC-LAND` PASS = metric pinned at one specific site with explicit threshold formulas AND K-counter at K=1 (W7c calibration); FAIL = metric landed at multiple sites OR threshold formulas not pinned numerically.

4. **K-counter advancement protocol for Corpus A — does W7c's instance #1 status BIND across re-readings?**: Per CG2 / D4, the WP §2 declaration STAYS AS RECORDED. But what is the protocol if a future workshop re-adjudicates the rule-reading? Pre-registered gate: `S89-KCOUNTER-FORWARD-ONLY-CLAUSE` PASS = explicit clause in `feedback_rules-compensate-missing-structure.md` stating "K-counter advancements record OBSERVED instances at session-close; backward retraction on rule-reading-disagreement grounds is FORBIDDEN absent a Class-3-equivalent demonstration"; FAIL = no clause landed or backward retraction admitted as routine.

5. **Closing-paragraph-coherence sweep audit — does the W-25 audit pattern (EG1) surface contradictions in OTHER rule-files?**: EG3 enumerates 3 audit candidates (`v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1-7 + Stage 1/2/3; `cross-pillar-bridge-anatomy.md` algebra-axis orthogonality MANDATORY clause + K-counter advancement; `joint-theorem-promotion.md` 4-stage pathway + Stage-2 PASS-AND independence). Pre-registered gate: `S89-RULE-FILE-COHERENCE-SWEEP-AUDIT` PASS = closing-paragraph-coherence test applied to each of the 3 candidate rule-files; report records (i) rule-file × candidate-reading × contradiction-status triples, (ii) any rule-files surfaced as needing remediation; INFO = sweep performed, no remediation needed; FAIL = sweep skipped or audit-pattern itself is internally inconsistent.

6. **F(observable) vs F(trigger predicate) layer-decomposition refinement — promotion of EG2 to MANDATORY rule extension?**: EG2 proposes an extension to `epistemic-discipline.md §"Layer-Decomposition"` distinguishing F(observable) (substrate-IS-framing-governed; preserve multi-axis) from F(trigger predicate) (rule-text-evidence-governed; possibly single-axis). Status at K=1 (W-25 calibration). Pre-registered gate: `S89-LAYER-DECOMP-F-IMAGE-SPLIT-LAND` PASS = clause appended to `epistemic-discipline.md` with K=1 calibration (W-25) + 2 reserved K-counter rows; status SUGGESTION; promotion to MANDATORY at K=3 per the standard.

7. **Forward calibration corpus reservation — what wave-shape would advance Corpus A's K-counter to 2?**: Per sagan's S5 + my DG1, the SPLIT_REQUIRED heuristic at PB(W) ≥ 4 is the planner-skill-layer countermeasure. If S89 follows that heuristic, no covered_count ≥ 4 instance fires in S89. Open question: does the K=3 promotion threshold reach in finite future sessions UNDER the normal operation of the SPLIT_REQUIRED heuristic, OR does K stay at 1 indefinitely as a "rule-did-its-job" signal? Sagan's "sociological metric" framing (R2 line 1162) is one answer; my "rule retires at SUGGESTION-status if K never advances" framing (G3 Q4) is another. Pre-registered gate: `S89-CORPUS-A-FORWARD-CALIBRATION-EXPECTATION` PASS = explicit clause in `mechanical-closure-discipline.md §"PLANNING DEFECT"` stating which framing the rule adopts (sociological-metric OR rule-retirement-on-non-advancement); FAIL = framing left ambiguous.

8. **Workshop-internal R3 closing-paragraph test extension — applies to OTHER calibration corpora besides §"PLANNING DEFECT"?**: The closing-paragraph-coherence audit pattern (EG1) was deployed to ONE rule (`mechanical-closure-discipline.md §"PLANNING DEFECT"`) at the W-25 workshop. Is the pattern itself general enough to be a session-recurring audit, or is it a one-off W-25 calibration? Open question for next-session investigator-skill (`/rclab-investigate`) consumers.

## Wrap-Up — Workshop Impact Summary

*[Agent B (gen-physicist) fills this in the FINAL round alongside the Verdict table.]*

### What Changed

- **W7c is calibration-corpus instance #1 of `mechanical-closure-discipline.md §"PLANNING DEFECT"` under the literal-independent reading of the rule-text** (CG1 confirms; WP §2 / §9 / §"Constraint-Map Updates" declarations stand as recorded; sagan's reading wins via the closing-paragraph-coherence test on lines 30-31 vs 282-286).
- **Two-corpora landing is now the agreed forward shape** (CG3 / E1): Corpus A keeps the existing §"PLANNING DEFECT" clause count-keyed at K=1; Corpus B is a NEW forward-pinned-follow-up wave class (per E2) at `wave-classification.md` also at K=1. Both have W7c as instance #1, measured along orthogonal axes.
- **The strict conjunctive reading of `mechanical-closure-discipline.md §"PLANNING DEFECT"` is REJECTED** as a reading of the rule-file as authored (CG1 substitution chain: conjunctive antecedent forces FORBIDDEN ∧ acceptable contradiction at lines 30-31 vs 282-286).

### What Holds

- **The methodology-IS observable on the W7c plan artifact remains multi-axis** (covered_count, DPP_routing_count, item_1_status_per_gate). CG1 retracts only the conjunctive TRIGGER reading, not the multi-axis OBSERVABLE structure. Sagan's C1 + my Re:S6 still hold.
- **Item-1 of `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` remains the per-closure admissibility predicate**; W7c's 4 closures all PASS item 1 (per WP §1 lines 866-869). Item-1 enforcement at plan-freeze is unchanged by this workshop.
- **The directional-asymmetry argument (D4) survives**: forward label-changes (joint-theorem-promotion STAGE-1 → STAGE-3) and backward label-changes (G2 amendment) live in different epistemic classes; backward retractions on rule-reading-disagreement grounds are NOT routine and require structural justification absent here.
- **Verdict-line content on disk for #84/#85/#86/#167 is ABSOLUTELY PERMANENT** (per `gate-verdicts.md §"Rules"` item 2; this workshop touches no audit_sha256 / content_sha256 / value strings / schemes / conventions / L_max).

### What Breaks or Strains

- **The current `mechanical-closure-discipline.md §"PLANNING DEFECT"` clause is internally consistent under the literal-independent reading but DIAGNOSTICALLY IMPRECISE**: it does not distinguish item-1-clean forward-pinned-follow-up waves (W7c) from hypothetical item-1-violating waves (W7c-prime, structurally empty per D3). Both readings hit the same count threshold; the rule conflates them. EG1's closing-paragraph-coherence test surfaced this; the two-corpora landing addresses it.
- **The `epistemic-discipline.md §"Layer-Decomposition"` clause does not currently distinguish F(observable) from F(trigger predicate)**: my Re:S6 made the category error of conflating them; the framework has no rule-text preventing future agents from making the same error. EG2 proposes the lift.
- **EG3 surfaces 3 candidate rule-files that may have latent closing-paragraph-coherence contradictions** (`v3-closure-recovery.md`, `cross-pillar-bridge-anatomy.md`, `joint-theorem-promotion.md`); these are unaudited at workshop-close.

### Carry-Forward Computations

1. **Closing-paragraph-coherence disambiguation clause for `mechanical-closure-discipline.md §"PLANNING DEFECT"`**
   - **What**: append a disambiguation clause after line 281 stating "the trigger fires on covered_count ≥ N_PLANNING_DEFECT_THRESHOLD = 4 INDEPENDENTLY of item-1 status; the closing paragraph at lines 282-286 'remains acceptable AT EXECUTION TIME' assumes item-1-PASS by construction (per the rule-section's structural composition with `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1)."
   - **Inputs**: rule-text at lines 22-31 + lines 274-286; W-25 calibration-corpus instance (this workshop); EG1 closing-paragraph-coherence-test methodology rule.
   - **Gate**: `S89-MECH-CLOSURE-DISAMBIGUATION-CLAUSE-LAND` PASS = clause appended; cross-references to W-25 + lines 30-31 explicit; closing-paragraph-coherence test re-applied confirms internal consistency. FAIL = clause missing or contradicts the closing paragraph.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class per `wave-classification.md` M1∧M2∧M3∧M4; rule-file edit only, no compute).

2. **Forward-pinned-follow-up wave class definition landing at `wave-classification.md`**
   - **What**: append a NEW sub-section to `wave-classification.md` defining the forward-pinned-follow-up wave class (per E2: PB(W) ≥ 1 AND DPP routing instructions point to mid-session-expected machinery/data landings) with M1-M4-analog conjunction tests + Corpus B trigger predicate + W7c calibration-corpus row at K=1.
   - **Inputs**: existing METHODOLOGY-class / COMPUTE-class / MIXED-class taxonomy at `wave-classification.md` (DG3 analogical landing); W-25 E2 class definition; W7c plan + WP for instance-#1 calibration data.
   - **Gate**: `S89-WAVE-CLASS-FORWARD-PINNED-FOLLOWUP-LAND` PASS = sub-section landed at `wave-classification.md` (NOT a new rule-file); class definition includes forward-pinning-density observable axis; W7c row in the calibration-corpus table at K=1; status SUGGESTION pending K=3.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

3. **Carry-forward-displacement metric pre-registration**
   - **What**: pin the metric (carry_forward_displacement(W) := total_carry_forward_effort(W) / W.budget; trigger when ≥ 1.5× AND ≥ 50% of carry-forwards are W{N}_machinery-displacement items) at ONE specific landing site with K=1 calibration (W7c: 5.6/3.8 ≈ 1.47× and 5/10 = 50%).
   - **Inputs**: W7c WP §8 carry-forward enumeration (lines 934-996); sagan S5 + C3 metric specification; wave-budget definition from session plan §summary.
   - **Gate**: `S89-CF-DISPLACEMENT-METRIC-LAND` PASS = metric pinned at ONE site with explicit threshold formulas + K=1 calibration row + reserved K=2 / K=3 rows; landing site choice (extension to `feedback_fix-in-session-never-defer.md` vs new `carry-forward-displacement-discipline.md` vs integration into `wave-classification.md`) is part of the sub-gate. FAIL = metric pinned at multiple sites OR threshold formulas not numerical.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

4. **K-counter forward-only clause for `feedback_rules-compensate-missing-structure.md`**
   - **What**: append a clause stating "K-counter advancements record OBSERVED instances at session-close; backward retraction on rule-reading-disagreement grounds is FORBIDDEN absent a Class-3-equivalent demonstration on the rule-text-as-authored." This codifies the CG2 / D4 directional-asymmetry concession.
   - **Inputs**: D4 substitution chain on forward vs backward label-changes; `joint-theorem-promotion.md` STAGE-1 → STAGE-3 forward-promotion precedent; existing `feedback_rules-compensate-missing-structure.md` K-counter mechanism.
   - **Gate**: `S89-KCOUNTER-FORWARD-ONLY-CLAUSE` PASS = clause appended; cross-references W-25 calibration; explicit prohibition of routine backward retraction on rule-reading-disagreement grounds. FAIL = no clause OR clause permits backward retraction without Class-3-equivalent demonstration.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class).

5. **Closing-paragraph-coherence sweep audit on 3 candidate rule-files**
   - **What**: apply the EG1 closing-paragraph-coherence audit pattern to (a) `v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 1-7 vs Stage 1/2/3 procedure; (b) `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause vs K-counter advancement criteria; (c) `joint-theorem-promotion.md` 4-stage pathway vs Stage-2 PASS-AND independence. Report contradiction-status for each candidate-reading × rule-file pair.
   - **Inputs**: EG1 audit-pattern specification; the 3 rule-files; W-25 audit-pattern application as the calibration template.
   - **Gate**: `S89-RULE-FILE-COHERENCE-SWEEP-AUDIT` PASS = sweep performed for all 3 rule-files; report records (rule-file × candidate-reading × contradiction-status) triples; any rule-file contradictions surfaced are queued for remediation. INFO = sweep performed, no contradictions surfaced. FAIL = sweep skipped or audit pattern itself is internally inconsistent.
   - **Effort**: 0.6 wave-equivalents (METHODOLOGY-class hygiene-style audit; 3 rule-files × ~0.2 wave-equiv each).

6. **F(observable) vs F(trigger predicate) layer-decomposition refinement at `epistemic-discipline.md §"Layer-Decomposition"`**
   - **What**: append the EG2 sub-section distinguishing F(observable) (substrate-IS-framing-governed; preserve multi-axis structural content) from F(trigger predicate) (rule-text-evidence-governed; possibly single-axis or multi-axis); pin W-25 as K=1 calibration; reserve K=2, K=3 rows.
   - **Inputs**: existing `epistemic-discipline.md §"Layer-Decomposition"` content (F substrate ↔ methodology pair, F methodology ↔ audit pair, Phi correspondence); E3 sagan-derived split; my Re:S6 category error as negative-calibration counter-instance.
   - **Gate**: `S89-LAYER-DECOMP-F-IMAGE-SPLIT-LAND` PASS = sub-section appended; F-image decomposition explicit; W-25 K=1 calibration row + 2 reserved rows; status SUGGESTION; promotion to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. FAIL = sub-section conflates F(observable) and F(trigger predicate) OR omits the W-25 calibration.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

7. **SPLIT_REQUIRED heuristic landing at `/rclab-plan` skill text**
   - **What**: append the sagan S5 3-tier decision rule (PB(W) ≥ 4 → SPLIT_REQUIRED; 2 ≤ PB(W) < 4 ∧ PB_frac ≥ 0.50 → SPLIT_RECOMMENDED; else → SINGLE_WAVE_OK) to `/rclab-plan` skill text as a plan-freeze-time consultation.
   - **Inputs**: sagan S5 substitution chain (workshop lines 296-324); E2 forward-pinned-follow-up wave class definition (CF #2); W7c PB = 4 calibration.
   - **Gate**: `S89-RCLAB-PLAN-SPLIT-HEURISTIC-LAND` PASS = heuristic appended to skill text; explicit cross-reference to forward-pinned-follow-up wave class (CF #2); plan-author consultation step pre-registered at plan-freeze. FAIL = heuristic missing or conflated with rule-fire diagnostic at `mechanical-closure-discipline.md`.
   - **Effort**: 0.2 wave-equivalents (planner-skill-layer edit; not a rule-file edit).

8. **EG1 closing-paragraph-coherence test PROMOTION to a methodology rule extension**
   - **What**: append the EG1 audit-pattern specification (closing-paragraph-coherence test for rule-text composition) to `epistemic-discipline.md §"Pre-Registration Completeness"` as a NEW sub-section. K=1 calibration (W-25); 2 reserved K-counter rows.
   - **Inputs**: EG1 audit-pattern derivation; W-25 calibration as the first instance.
   - **Gate**: `S89-CLOSING-PARAGRAPH-COHERENCE-RULE-LAND` PASS = sub-section appended with audit-pattern definition + W-25 K=1 calibration + 2 reserved rows; status SUGGESTION; promotion to MANDATORY at K=3. FAIL = sub-section omits the structural-test specification or the W-25 calibration.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class).

9. **WP §2 in-session NOTE (NOT amendment) for traceability — record the W-25 workshop adjudication outcome without retracting the prior declaration**
   - **What**: append a NOTE paragraph at WP §2 (after current line 881) recording: "Workshop W-25 (sagan x gen-physicist, 2026-05-08) adjudicated this calibration. Sagan's literal-independent reading wins per the closing-paragraph-coherence test (CG1). The instance-#1 declaration STANDS AS RECORDED per the directional-asymmetry argument (CG2 / D4). The two-corpora landing per CG3 / E1 means W7c is ALSO instance #1 of a NEW Corpus B (forward-pinned-follow-up wave class) landed at `wave-classification.md` per CF #2. Cross-link to W-25 workshop document for full adjudication."
   - **Inputs**: this workshop's verdict table + CG1 / CG2 / CG3; WP §2 current text; CF #2 landing.
   - **Gate**: `S89-W7C-WP-§2-NOTE-LAND` PASS = NOTE appended after current §2 content (NOT before; NOT replacing); cross-link to W-25 workshop document explicit; instance-#1 declaration unchanged; verdict-line content unchanged. FAIL = NOTE retracts the prior declaration OR touches verdict-line content.
   - **Effort**: 0.1 wave-equivalents (working-paper edit; not a rule-file edit).

10. **Corpus A K-counter forward-calibration-expectation clause for `mechanical-closure-discipline.md §"PLANNING DEFECT"`**
    - **What**: append a clause stating which framing the rule adopts for K-counter expectation: (a) sociological-metric framing (K = 3 promotion is a reachable signal that the pattern recurred 3 times across distinct sessions; rule operates as accumulator), OR (b) rule-retirement-on-non-advancement framing (K stays at 1 if SPLIT_REQUIRED heuristic is followed; rule reaches MANDATORY only on planner-skill failure). Pin one explicit interpretation.
    - **Inputs**: G3 Q4 + sagan answer at line 1162; W-25 verdict on this question (defaulting to sagan's sociological-metric framing absent dissent at the workshop).
    - **Gate**: `S89-CORPUS-A-FORWARD-CALIBRATION-EXPECTATION` PASS = clause pinned with explicit framing choice; calibration-corpus table at `mechanical-closure-discipline.md §"PLANNING DEFECT"` updated to reflect the framing. FAIL = framing left ambiguous or both interpretations admitted simultaneously.
    - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class).

### Closing Line

The W-25 closing-paragraph-coherence test (sagan's D1) settles the rule-text adjudication in favor of the literal-independent reading (W7c IS Corpus-A instance #1), and the two-corpora landing (E1) preserves the structural-class signal at a NEW Corpus B at `wave-classification.md` so neither reading is retracted and both calibrations carry forward.

*[NOT STARTED — one sentence]*
