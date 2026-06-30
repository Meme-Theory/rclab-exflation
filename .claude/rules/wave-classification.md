# Wave Classification (METHODOLOGY vs COMPUTE)

## Rule

Every wave in a session plan MUST be classified as one of three classes
at plan-freeze time:

- **METHODOLOGY-class** — wave produces rule-file / template / skill
  edits whose PASS predicate is artifact-existence-with-substantive-
  content, NOT a numerical comparison against a pre-registered
  threshold.
- **COMPUTE-class** — wave produces computation numerical output with a
  pre-registered PASS / FAIL / INFO threshold (the canonical compute
  pattern).
- **MIXED-class** — wave contains BOTH METHODOLOGY-style and
  COMPUTE-style gate-items; MUST be sub-wave-decomposed before
  plan-freeze (see §"NROY clause" below).

A wave is **METHODOLOGY-class** iff ALL FOUR of the following M1-M4
tests hold (strict logical conjunction):

### M1 — PASS predicate type

The pre-registered PASS predicate is artifact-existence-with-
substantive-content, NOT a numerical comparison. Specifically:

```
PASS iff (file F exists at path P)
        AND (F contains section §S)
        AND (substantive_line_count(§S) >= 15)
        AND (content_sha256(§S) matches input-pin-map-derived hash)
```

Failing M1: any predicate of the form `value < threshold`, `|x - y| <
tol`, `eigenvalue in band [a, b]`, `chi_squared < N`, or any other
numerical comparison against a pre-registered numerical threshold.

### M2 — Producing-operation type

The producing operations are restricted to:

- `Edit` / `Write` / `MultiEdit` on files matching
  `.claude/{rules,templates,skills}/**`
- `grep` / `wc` / SHA-256 cross-checks
- Integer counts (line counts, section counts, slot counts)

Producing operations FORBIDDEN under METHODOLOGY-class:

- ANY `.py` script whose output is a numerical comparison against a
  pre-registered threshold.
- Eigenvalue computations, linear algebra, FFTs, integrals.
- Fixture-with-hand-engineered-numerical-targets (a fixture script
  whose output is hardcoded to satisfy the gate's threshold by
  construction is the canonical M2 violation).

### M3 — Source-of-truth type

The wave's content derives from one of:

- Verbatim sub-diff from a prior closed workshop / synthesis.
- Verbatim 5-class taxonomy / pre-registered enumeration from a
  rule-file or registry entry.
- Anchor-citation-only landings (registry pointer rows).

FORBIDDEN under METHODOLOGY-class:

- First-principles new derivation.
- Substantively new physics.
- New theorem proofs without an upstream workshop deriving them.

If the wave's content requires substantively new derivation, it is
NOT METHODOLOGY-class — route it through the appropriate workshop or
COMPUTE-class wave first, then land the verbatim-extract here.

### M4 — Allowlist membership

The wave's gate-ID appears in `.claude/rules/methodology-wave-allowlist.md`.

The allowlist is append-only and orchestrator-only-edit (subagents
denied edit by harness convention; see `methodology-wave-allowlist.md`
for the recursion-attack closure rationale).

A gate-ID NOT in the allowlist CANNOT be METHODOLOGY-class regardless
of M1-M3 satisfaction; absence from the allowlist forces fallthrough
to COMPUTE-class (which then fails M1 / M2 because the gate has no
numerical threshold) or MIXED-class triage.

## Strict-conjunction requirement

The 4-test is `M1 AND M2 AND M3 AND M4`. ALL FOUR must hold for a
gate to be METHODOLOGY-class. Any one failure routes the gate to:

- **M1 fails (numerical predicate present)** → COMPUTE-class.
- **M2 fails (`.py` producing script present)** → COMPUTE-class OR
  MIXED-class (depends on whether other gate-items in the same wave
  satisfy M1-M4).
- **M3 fails (new derivation required)** → upstream workshop or
  COMPUTE-class first; landing as METHODOLOGY-class only after the
  derivation is verbatim-extractable from a closed workshop.
- **M4 fails (gate-ID not allowlisted)** → COMPUTE-class fallthrough
  OR plan-freeze halt requesting orchestrator allowlist append (per
  the recursion-attack-closure protocol).

## NROY clause (workshop header line 32)

A wave CANNOT be both COMPUTE-class and METHODOLOGY-class. The 4-test
conjunction and its negation cannot both hold, so the classification
is partition-honest by construction.

**MIXED-class** waves (gate-items partition into METHODOLOGY ∪ COMPUTE
subsets at the wave-item level) MUST be sub-wave-decomposed before
plan-freeze:

- Example: a MIXED wave W → W-a (COMPUTE half) +
  W-b (METHODOLOGY half).
- The COMPUTE-half retains its numerical threshold + `.py` script.
- The METHODOLOGY-half lands the rule-file / registry edit per the
  M1-M4 conjunction.
- Each sub-wave gets its own gate-ID and independent verdict line.

A MIXED-class wave that is NOT sub-decomposed by plan-freeze causes
plan-freeze halt (analogous to a PRU cardinality failure). The halt
emits a remediation request to the plan author: enumerate sub-wave
decomposition before re-freezing.

## Self-classification at plan-freeze

The classification is performed AT PLAN-FREEZE TIME, not at runtime.
The plan-authoring orchestrator (or the `_wave_classification_audit.py`
auditor) MUST emit a per-gate `(M1, M2, M3, M4)`
4-tuple plus the resulting classification to the plan-freeze log
before any dispatch fires.

This converts the runtime ambiguity (is this a methodology gate or a
compute gate?) into a plan-time pre-registration discipline (the
classification is itself an input pin of the gate, not a runtime
inference). The pattern matches PRU pre-registration: the auditor
runs at plan-freeze and routes failures to MANDATORY remediation.

## Dispatch consequences

Once classified, the wave's dispatch path is fixed:

- **COMPUTE-class waves** dispatch via `/rclab-coordinate` compute-mode
  (the canonical compute pattern: computation script + verdict line + working-
  paper section, all per the dual-SHA closure protocol).
- **METHODOLOGY-class waves** SKIP `/rclab-coordinate` compute-mode.
  The orchestrator writes the rule-file edits directly, treating each
  wave-item as analogous to the team-lead synthesis section. (See
  `team-lead-behavior.md §"METHODOLOGY-Class Wave Discipline"` for the
  team-lead-side behavior protocol.)
- **MIXED-class waves** decompose into sub-waves first, then each
  sub-wave dispatches per its own classification.

## Forward-pinned-follow-up wave class (SUGGESTION at K=1)

A wave is **forward-pinned-follow-up class** iff ALL FOUR of the following
M1'-M4' tests hold (analog of the M1-M4 METHODOLOGY-class strict
conjunction):

- **M1' — Prereq-block ≥ 1**: the wave's plan-block declares ≥ 1 gate
  whose machinery pin or input-SHA pin points to a mid-session-expected
  landing (data file from a prior wave in the same session,
  canonical_constants pin promoted in an in-session prior wave, or
  registry slot expected to land mid-session).
- **M2' — DPP routing instructions present**: the plan's downstream
  decision-point table specifies routing instructions for the
  prereq-block scenario (typically "PRE-REG-INC, deferred to S{N+1}",
  or "carry-forward to next wave conditional on prereq landing").
- **M3' — Item-1-clean per gate** per `mechanical-closure-discipline.md
  §"When mechanical closure IS acceptable"` item 1 (the plan author HAS
  anticipated the prereq-block scenario at plan-authorship time; the
  closure script is NOT post-hoc plan editing).
- **M4' — Wave-class allowlist consistency**: if the wave is also
  METHODOLOGY-class, gate-IDs MUST appear in
  `methodology-wave-allowlist.md`; otherwise the wave is COMPUTE-class
  with forward-pinning structure (no allowlist gate but plan-block
  prereq-block disclosure required).

The Corpus B trigger predicate is **structural-class-keyed**
(M1' ∧ M2' ∧ M3' ∧ M4'), distinct from the count-keyed Corpus A trigger
at `mechanical-closure-discipline.md §"PLANNING DEFECT"` (covered_count
≥ N_PLANNING_DEFECT_THRESHOLD = 4). The two corpora are STRUCTURALLY
ORTHOGONAL per `epistemic-discipline.md §"Layer-Decomposition"` F(observable)
vs F(trigger) split; a wave may be instance-#1 of BOTH simultaneously.

### Forward-pinning-density observable

The forward-pinning-density observable on a wave plan-block at plan-freeze
is multi-axis: `(PB(W), DPP_routing_count(W), item_1_status_per_gate(W))`.
Per-axis specifications + K=1 calibration row + reserved K=2/K=3 rows
+ forward enforcement steps: `sessions/framework/registry/pru-class-corpus.md §13`.

### Dispatch consequence

Forward-pinned-follow-up waves dispatch per their underlying class
(METHODOLOGY-class via orchestrator-direct-write; COMPUTE-class via
`/rclab-coordinate` compute-mode). The forward-pinned-follow-up
classification is an OVERLAY tag at plan-freeze, not a separate
dispatch path; it serves as the structural marker for downstream
audit (PRU Class-8 plan-authorship-defect detection at the
forward-pinning axis, complementary to `mechanical-closure-discipline.md
§"PLANNING DEFECT"` count-keyed detection).

Status promotes from SUGGESTION to MANDATORY at K=3 distinct calibration
instances per `feedback_rules-compensate-missing-structure.md`.

## Dual-SHA closure for METHODOLOGY-class

Per the layer-functor F image at the methodology layer (see
`epistemic-discipline.md §"Layer-Decomposition"`), the dual-SHA closure
for METHODOLOGY-class waves is:

- `content_sha256` over the rule-file diff (the F-image of the
  numerical PASS-predicate eigenvalue under substrate ↔ methodology).
- `audit_sha256` over the input-pin map of source documents (NOT a
  fixture-replay numerical PASS).

The dual-SHA discipline applies identically; only the
substrate of the SHA inputs differs.

## Cross-references

- **Structural parent**: `epistemic-discipline.md §"Layer-Decomposition"`
  (layer-functor F maps numerical PASS predicate ↔
  artifact-existence predicate at the substrate ↔ methodology layer pair).
- **Allowlist enforcement**: `.claude/rules/methodology-wave-allowlist.md`
  (M4 substrate).
- **Team-lead behavior**: project-root `team-lead-behavior.md`
  §"METHODOLOGY-Class Wave Discipline" (the
  orchestrator-direct-write convention path).
- **MCP pre-check hook**: `.claude/hooks/mcp-pre-check.sh` (PreToolUse
  hook actor-blind, fires on orchestrator + subagent
  identically; load-bearing Phi(a_4) axis).
- **Audit script**: `computations/_shared/_wave_classification_audit.py`
  (pre-registers wave-class at plan-freeze).
- **Pre-population precedent**: the initial allowlist rows in
  `methodology-wave-allowlist.md`, landed per the no-technical-debt rule.
