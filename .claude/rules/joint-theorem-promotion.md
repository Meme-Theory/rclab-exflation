# Joint Theorem Promotion Pathway

This rule defines the 4-stage upgrade pathway for **joint cross-axis theorem registration** in `sessions/permanent-results-registry.md`. A joint theorem is one whose statement contains clauses requiring evidence from MORE THAN ONE methodological axis (e.g., spectral-functional + transit-dynamics; substrate-physics + cosmological-dynamics; NCG-axiomatic + GGE-relic).

This rule is the **constructive** complement to `.claude/rules/epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2 (which forbids "agreement among agents" as evidential weight). The 4-stage pathway specifies HOW joint-axis evidence becomes registry-eligible without falling into the agreement-as-evidence trap.

## Why a constructive complement is needed

The "agreement among agents" exclusion (epistemic-discipline §What Does NOT Count) prevents shared-context-produced agreement from being mistaken for independent confirmation. But this exclusion alone provides no pathway for genuine joint-axis theorems — those whose statement is intrinsically cross-axis and CANNOT be derived from a single-axis perspective.

The 4-stage pathway resolves the tension: joint clauses must be authored ONCE (workshop-internal, Stage 0), registered as a CANDIDATE (Stage 1), then independently verified by TWO agents on opposite axes who operate WITHOUT prior workshop context (Stage 2), before the theorem is permanent (Stage 3). The "agreement" emerging from Stage 2 is structurally NOT shared-context agreement (the two cross-reviewers have NEVER seen the workshop output).

## The 4 Stages

### Stage 0 — Workshop-Internal Candidate

- **Where**: Within a workshop's closure or wrap-up section
- **Form**: Joint theorem candidate text drafted by the workshop's authoring agents (typically 2 agents on different axes); contains all clauses (a)..(n) with cross-axis attribution per clause
- **PASS criterion**: All clauses are stated with explicit author-side attribution (e.g., clause (a) lizzi-side, clause (b) transit-side, clause (c) JOINT, clause (d) JOINT, clause (e) lizzi-side, clause (f) transit-side); workshop verdict freezes the text
- **Status**: workshop-internal artifact only; NOT yet in `permanent-results-registry.md`

### Stage 1 — Registration as Candidate (next session)

- **Where**: `sessions/permanent-results-registry.md`, registry slot allocated per `regulator-pin-discipline.md` next-free-letter protocol
- **Form**: Full theorem text from Stage 0 + 4-stage tag `STAGE-1-CANDIDATE` + identification of joint clauses (those requiring Stage-2 cross-axis verify) + corrigenda from the originating workshop
- **PASS criterion**: Registry entry written with all clauses, all corrigenda, joint-clause flags, and authorship attribution. `STAGE-1-CANDIDATE` tag on theorem-name line.
- **Status**: registered as CANDIDATE only — not yet permanent; downstream gates may CITE the candidate but must include the `STAGE-1-CANDIDATE` qualifier

### Stage 2 — Two-Agent Parallel Cross-Check (mandatory upgrade gate)

- **Where**: One dedicated gate (e.g., an `EXTENDED-THEOREM-INDEPENDENT-VERIFY` gate)
- **Form**: TWO independent cross-reviewers, ONE per axis, dispatched in parallel:
  - **Axis-A cross-reviewer** audits clauses authored on axis A + JOINT clauses
  - **Axis-B cross-reviewer** audits clauses authored on axis B + JOINT clauses
  - Both cross-reviewers operate WITHOUT prior workshop context (read only the registered Stage-1 entry; do NOT receive the workshop-internal text)
  - JOINT clauses are PASS-AND'd across the two verdicts (both cross-reviewers must independently PASS each joint clause)
- **PASS criterion**:
  - BOTH cross-reviewers return PASS on their respective single-axis clauses
  - JOINT clauses PASS independently in BOTH verdicts (logical AND, not OR)
  - Stage 2 verdict is INDEPENDENT verification per `epistemic-discipline.md` §"What Counts as Evidence"
- **FAIL criterion**: Either cross-reviewer returns FAIL on ANY clause → Stage 2 → 3 promotion blocked; theorem stays at Stage 1; FAILing clauses route to next-session remediation
- **INFO criterion**: Either cross-reviewer returns INFO on a clause → theorem stays at Stage 1; the INFO clause is documented as a Stage-2-INFO-deferred item

### Stage 3 — Permanent Registration

- **Where**: `sessions/permanent-results-registry.md` — replace `STAGE-1-CANDIDATE` tag with `STAGE-3-PERMANENT`
- **Form**: Theorem joins the permanent-results table alongside existing structural results (KO-dim=6, J-D_K=0, etc.)
- **PASS criterion**: Stage 2 PASS verdict landed; orchestrator session-end synthesis updates the registry tag from STAGE-1-CANDIDATE to STAGE-3-PERMANENT
- **Status**: permanent — eligible for citation as a structural theorem without the candidate qualifier

## Two-Agent Independent-Verify (Stage 2 details)

The Stage 2 cross-check requires TWO independent agents on DIFFERENT axes, dispatched IN PARALLEL, BOTH OPERATING WITHOUT PRIOR WORKSHOP CONTEXT. Single-agent verification on joint clauses is structurally INSUFFICIENT (Stage 2 → 3 audit script `_joint_theorem_independent_verify_audit.py` REFUSES single-agent firings on joint clauses).

The "without prior workshop context" condition is critical:
- The cross-reviewers receive ONLY the registered Stage-1 entry text + relevant input files
- They do NOT receive the workshop's transcripts
- They cannot be the original workshop authoring agents
- The orchestrator dispatches them with explicit instruction to verify the registered theorem from first principles, NOT to re-derive it via the workshop's path

This protocol breaks the shared-context-produces-shared-output failure mode: if both cross-reviewers independently PASS a joint clause without reading the workshop, the agreement is structurally independent.

### Stage-2 Axis-B Selection Protocol

When dispatching the Stage-2 Axis-B cross-reviewer, the orchestrator MUST satisfy ALL THREE conditions of the Axis-B Selection Protocol:

1. **Axis-distinctness**: The Axis-B reviewer's primary methodology is on a DIFFERENT axis from Axis-A. Examples: Axis-A = NCG-axiomatic / spectral-functional → Axis-B = transit-dynamics / superfluid-universe / cosmological-bridge. Axis-A and Axis-B reviewers MUST NOT share the same axis even if their named methodologies differ in narrow specialty (e.g., two NCG-side reviewers fail axis-distinctness).

2. **Original-authoring-agent exclusion with downstream-inheritance reach**: Neither cross-reviewer may be (a) the original workshop authoring agent OR (b) a successor agent whose memory inherits the workshop's reading-path through prior session synthesis. The downstream-inheritance reach extends to agents whose project-memory or feedback-files cite the workshop's transcripts as canonical reference; such agents are structurally pre-loaded with the workshop's view and fail the "without prior workshop context" requirement.

3. **Audit-coverage adequacy**: The Axis-B reviewer's domain expertise MUST cover ALL joint clauses + ALL Axis-B-side single-axis clauses. A reviewer with partial coverage (e.g., expert on transit-dynamics but not on cosmological-bridge applications) creates audit-coverage gaps where joint clauses pass formally but lack substantive cross-axis examination.

**Failure mode**: a reviewer whose project memory inherits a workshop's reading-path (e.g., via direct re-citation of the workshop transcripts in the reviewer's `reference_*.md` memory files) FIRES the downstream-inheritance reach test (condition 2 above), requiring re-dispatch with a same-axis reviewer of distinct downstream-inheritance lineage. Forward enforcement: `_joint_theorem_independent_verify_audit.py` flags reviewer-selection violations at plan-freeze with HARD-HALT remediation.

### Substrate-input-orthogonality clause

For any Stage-2 verification with N ≥ 2 observables {obs_1, ..., obs_N}, the procedural floor MUST be supplemented with the **substrate-input-orthogonality predicate**:

- ∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both).

PASS-AND across orthogonal-data observables is the structural ceiling for the procedural-floor independence guarantee. Without substrate-input orthogonality, Stage-2 PASS-AND establishes structural-output-type independence (different decision pipelines on the same data) but not structural-input independence (the data itself is shared); the calibration corpus advances under explicit "substrate-input-overlap caveat" tagging.

Cross-link to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 (the "agreement among agents" exclusion this clause sharpens) and to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (the structural-orthogonality precedent at the cross-pillar-bridge layer).

Calibration corpus + K-counter advancement records + audit-script extension queue: `sessions/framework/registry/pru-class-corpus.md §15`.

Status **MANDATORY at K=3**. Stage-2 PASS-AND verdicts emitted under SUGGESTION status carry an explicit **substrate-input-overlap caveat** when the predicate fails; instances at the structural ceiling omit the caveat.

## Calibration corpus

Per-instance calibration (clause-attribution worked examples, stage-by-stage landing records, cross-reviewer assignments): `sessions/framework/registry/pru-class-corpus.md`.

## Cross-link to "What Does NOT Count as Evidence" item 2

The `.claude/rules/epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2 forbids "agreement among agents" as evidential weight on the grounds that "shared context produces shared outputs, not independent confirmation". This rule does NOT contradict that exclusion; it specifies the **constructive pathway** that produces structurally-independent agreement:

- "Agreement among agents" with shared context (e.g., one workshop's closure agreement; both agents read the same workshop transcript) → still NOT evidence
- "Agreement among agents" with NO shared context (Stage 2 cross-reviewers, dispatched with only the registered Stage-1 entry, never having read the workshop) → IS evidence per the standard "What Counts as a Result" criterion

The 4-stage pathway is the only recognized pathway for joint cross-axis theorems to enter the permanent-results table.

## Audit at plan-freeze

Plan-freeze validators dispatching a Stage 2 gate MUST verify (via `_joint_theorem_independent_verify_audit.py`):

1. Two cross-reviewers are dispatched in parallel (not sequentially)
2. Cross-reviewers are on DIFFERENT axes (e.g., spectral-functional + transit-dynamics)
3. Cross-reviewers are NOT the original workshop authoring agents
4. Dispatch prompts do NOT include the workshop's transcripts
5. JOINT clauses are PASS-AND'd across both verdicts in the gate logic
6. Cross-reviewer's audit machinery is NOT structurally self-authored. If reviewer R applies a parse-tree decision procedure / 4-corner classification / cohomology bridge map at the verdict-emission layer, R is NOT the sole author of that machinery. If R is the sole author, an alternate machinery route MUST be applied at the verdict layer OR a second reviewer cross-checks the machinery application. (Status SUGGESTION at K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. Calibration corpus + audit-script extension queue: `sessions/framework/registry/pru-class-corpus.md §16`.)

Missing any of (1)-(6) → audit FAIL → Stage 2 → 3 promotion blocked.

## Forward-looking convention-pin

This rule is forward-looking. Any future cross-axis joint theorem MUST adopt this pathway; theorems registered without the 4-stage progression are NOT eligible for permanent-results-table inclusion.
