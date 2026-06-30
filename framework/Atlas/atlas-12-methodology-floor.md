# Atlas D12: Methodology Floor

**Sessions covered**: S78 (PRU Class 8 origin) — S88 W-25 (current methodology-floor maturation)
**Updated**: 2026-05-09
**Companion atlas (substrate-side)**: `atlas-11-cross-pillar-bridge-corpus.md`
**Source rule files**: 24 framework rules at `.claude/rules/`
**Source templates**: 9 framework templates at `.claude/templates/` + 1 frozen example at `.claude/templates/examples/`

This atlas describes HOW the substrate is investigated, NOT WHAT the substrate IS. Atlas-12 is the audit-trail-layer atlas of the layer-functor F. Cross-link to atlas-11 (substrate-IS bridges) makes the substrate-vs-methodology orthogonality explicit. Methodology rules are NOT physics — they govern process.

The two atlases are STRUCTURALLY ORTHOGONAL: atlas-11 captures substrate-IS observables; atlas-12 captures methodology rules that govern HOW the substrate is investigated. Cross-corner co-primary between atlas-11 and atlas-12 is FORBIDDEN per the algebra-axis orthogonality K-counter MANDATORY clause (S87 W-2 R3 close, MANDATORY at K=3).

---

## I. Introduction — what is the methodology floor?

The methodology floor is the substrate ↔ methodology ↔ audit infrastructure that emerged S82-S88. It includes:

- **24 framework rule files** at `.claude/rules/` (process discipline; see §"NEW-RULES" enumeration)
- **9 templates** at `.claude/templates/` + 1 frozen example (canonical scaffolds for synthesis, plans, working papers, workshops, agents; see §"TEMPLATES" enumeration)
- **The layer-functor F** mapping substrate-physics quantities to methodology images to audit images (§II)
- **PRU Class 8.0–8.6 sub-class taxonomy** (machinery-pin cardinality / verifier-rubric / output-precision / representation-convention-pin / joint-hypersurface-form / layered-substitution-chain) (§IV)
- **Joint-theorem 4-stage promotion pathway** (workshop-internal candidate → registered candidate → two-axis cross-verify → permanent) (§V)
- **AMRI (Agent-Memory Registry Inversion)** detection and cleanup history (§VIII)
- **Methodology-wave classification** (M1–M4 strict conjunction with allowlist enforcement) (§VI–VII)
- **Workshop methodology** (4-condition definition + 3-question discriminator) (§IX)

**Pin to atlas-11**: atlas-11 is the substrate-side atlas (cross-pillar-bridge-corpus, ~24 entries with 5-anatomy + 3-level ladder); atlas-12 is the methodology-side atlas (the discipline that ENFORCES atlas-11's anatomy).

**Pin to atlas-04 (assumptions)**: the methodology floor includes assumed-and-proven items (process axioms): plan-freeze-time pre-registration is binding; verdict permanence (Option A protocol); PROHIBITED_ACTIONS Class 1–4; orchestrator-only edit on rule files (closes recursion attack).

**Pin to atlas-09 (retractions)**: AMRI cleanups are SUPERSESSIONS — agent memory entries that were promoted to project-level registries and SUPERSEDED at the original location.

---

## II. Layer-functor F: substrate ↔ methodology ↔ audit

Source: `epistemic-discipline.md §"Layer-Decomposition"`.

The **layer-functor** `F: substrate → methodology → audit` links the substrate-physics layer of the framework to the methodology-floor layer (rule files, agent standards) to the audit-floor layer (verdict files, audit scripts, hooks).

### F at substrate ↔ methodology pair

| Substrate-physics quantity | Methodology image under F |
|:--------------------------|:--------------------------|
| eigenvalue                | rule-file content         |
| numerical PASS predicate  | artifact-existence predicate |
| machinery pin             | input-pin map             |
| verdict-line numerical value | verdict-line artifact-SHA |
| fixture-by-construction   | orchestrator-direct-without-cross-actor |

### F at methodology ↔ audit pair

| Methodology quantity | Audit-leg image under F |
|:---------------------|:------------------------|
| rule-file content    | audit-line content      |
| artifact-existence predicate | SHA-uniqueness predicate |
| input-pin map        | `closure_hash(input_pin_map) = audit_sha256` (S82 W1 helper) |
| verdict-line artifact-SHA | `audit_sha256` (self-referential at audit layer) |
| orchestrator-direct-without-cross-actor | SHA-hardcoding bug (v3-closure-recovery sig_5) |

### Morita-equivalence framing

`F` preserves PRU-class invariants analogous to how `Mor_NCG` preserves K-theoretic invariants. A PRU Class-8.2 violation at the substrate layer (verifier-rubric pre-registration failure) maps under F to an analogous failure at the methodology layer (rule-file pre-registration failure) and at the audit layer (audit-line pre-registration failure). The class-8 sub-taxonomy (8.0/8.1/8.2/8.3) is preserved by F.

### Status

**TRIPLET-VERIFIED at S88 W13** via synthetic SHA-hardcoding-attack triggering v3 ladder sig_5 (per atlas-04 §VIII M4 + atlas-10 #34 narrative). Pair-verified at S86 R3 (substrate ↔ methodology pair); audit-leg verification was queued as `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` carry-forward and CLOSED at S88 W13 with the synthetic sig_5 attack confirming F-image at the audit layer matches the substrate ↔ methodology layer pair under SHA-uniqueness predicate. Triplet now FULLY VERIFIED across all three layers.

### Definitional-datum-vs-derived-theorem K-counter

K=2 at 2026-05-08; advisory until K=3. Distinguishes **definitional-datum** (true by construction at one layer of F) from **derived-theorem** (true by structural derivation at a different layer). Future plan-blocks claiming substrate-IS evidence MUST declare which layer of F the evidence sits at; codepath-layer claims are tautological-by-construction and DO NOT count as substrate-IS evidence.

### F(observable) vs F(trigger predicate) split

K=1; F applies DIFFERENTLY to observables vs trigger predicates. F(observable) preserves multi-axis structural content (per the algebra-axis orthogonality K-counter MANDATORY); F(trigger) is rule-text-evidence-governed and MAY be single-axis. Plan-block authoring discipline MUST tag observables and trigger predicates separately at plan-freeze; the F-image is computed independently for each.

---

## III. Phi correspondence: weight(a_n^SD) = weight(Σ_n)

Source: `epistemic-discipline.md §"Layer-Decomposition" Phi correspondence`.

The graded-ring-isomorphism Phi correspondence maps substrate-side Seeley-DeWitt weights to methodology-side enforcement-strengths:

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

## IV. PRU Class 8.0–8.6 sub-class taxonomy

Source: `epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`.

| Sub-class | Name | Origin | Status | Corpus location |
|:----------|:-----|:-------|:-------|:----------------|
| 8.0 / 8.1 | machinery-pin cardinality failure | S78 (original Class 8) | MANDATORY | parent rule + Source-Reconciliation 6-class taxonomy |
| 8.2 | verifier-rubric pre-registration failure | S86 W-12 ("Z_4 or similar" admitted V_4) | MANDATORY at K=5 (post-S88 W-7 + W-22 + W-21 simultaneous K=2→K=5 advancement, 2026-05-08) | `pru-class-corpus.md §1` |
| 8.3 | output-precision pre-registration failure | S86 W1c-8 (10 vs 15 sig figs) | MANDATORY at K=4 (post-S87 W8) | `pru-class-corpus.md §2` |
| 8.4 | representation-convention-pin failure | S88 W-16 W5b-50 V.5 (operator-domain dim > natural rep dim of substrate algebra; Pad-block convention dependence) | K=1 advisory until K=3 | `pru-class-corpus.md §5` |
| 8.5 | joint-hypersurface-pre-registration-form failure | S88 W-15 W4c-36 V.9 (gates consuming substrate-IS through CHILD pin must emit 2D hypersurface verdict-line value field) | K=1 advisory until K=3 | `pru-class-corpus.md §6` |
| 8.6 | layered-substitution-chain-audit failure | S88 W-17 W5b-47 V.5 (3-layer substitution chain crossing §VII.U.2 corner cells; arithmetic / parse-tree / operationalization layers must be pre-registered) | K=1 advisory until K=3 | `pru-class-corpus.md §7` |

### Source-Reconciliation Class-(a)–(f) taxonomy (companion to Class 8.0/8.1)

- **(a) PIN-TIGHT-SOURCE-LOOSE** — pin band tighter than canonical band
- **(b) PIN-LOOSE-SOURCE-TIGHT** — pin band wider than canonical band (highest-leverage class; FALSE-PASS direction)
- **(c) PIN-DRIFT-FROM-STALE-SOURCE** — pin computed against a since-superseded canonical (with c.OOM-misread sub-class)
- **(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY** — pin is a derived form of a primary canonical
- **(e) PIN-PROMOTES-TO-CANONICAL-ON-PASS** — pin will become canonical on PASS
- **(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — pin given as textual approximation, OOM estimate, or placeholder string AND a substrate-first canonical exists; MANDATORY at K=4 (S88 W7b-83 close)

### Pre-Registration Completeness — Closing-Paragraph-Coherence Audit Pattern (EG1)

S88 W-25 W7c-167 §V CF #8 (sagan + gen-physicist closing-paragraph-coherence workshop). K=1 SUGGESTION pending K=3 MANDATORY. For any rule-file section composed of (i) enumerated antecedent list + (ii) closing paragraph that disambiguates rule behavior, plan-freeze auditors MUST apply the closing-paragraph-coherence test: (1) identify two competing structural readings (literal-independent vs strict-conjunctive), (2) test each reading against the closing paragraph's qualifying language, (3) reject the reading that produces self-contradiction.

### Audit pipeline composition order (S87+)

```
PRU (cardinality pre-flight) → SOURCE-RECON (value pre-flight) →
SUBSTRATE-FIRST-PROVENANCE (source-existence) → PRDR (machinery enumeration) →
gate execution → v3-recovery audit
```

---

## V. Joint-theorem 4-stage promotion pathway

Source: `joint-theorem-promotion.md` (S86 W-9).

A **joint theorem** is one whose statement contains clauses requiring evidence from MORE THAN ONE methodological axis (e.g., spectral-functional + transit-dynamics; substrate-physics + cosmological-dynamics).

### Stage 0 — Workshop-Internal Candidate

- **Where**: within a workshop's R3 closure or wrap-up section
- **Form**: joint theorem candidate text drafted by the workshop's authoring agents (typically 2 agents on different axes); contains all clauses with cross-axis attribution
- **PASS criterion**: all clauses are stated with explicit author-side attribution; workshop verdict freezes the text
- **Status**: workshop-internal artifact only; NOT yet in `permanent-results-registry.md`

### Stage 1 — S87 (next-session) Registration as Candidate

- **Where**: `permanent-results-registry.md`, registry slot allocated per `regulator-pin-discipline.md` next-free-letter protocol
- **Form**: full theorem text + 4-stage tag `STAGE-1-CANDIDATE` + identification of joint clauses + corrigenda from workshop R3-B
- **Status**: registered as CANDIDATE only — not yet permanent; downstream gates may CITE the candidate but must include the qualifier

### Stage 2 — Two-Agent Parallel Cross-Check (mandatory upgrade gate)

- **Where**: one dedicated gate (e.g., `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY`)
- **Form**: TWO independent cross-reviewers, ONE per axis, dispatched in parallel:
  - **Axis-A cross-reviewer** audits clauses authored on axis A + JOINT clauses
  - **Axis-B cross-reviewer** audits clauses authored on axis B + JOINT clauses
  - Both cross-reviewers operate WITHOUT prior workshop context (read only the registered Stage-1 entry; do NOT receive the workshop-internal R3 text)
  - JOINT clauses are PASS-AND'd across the two verdicts (logical AND, not OR)
- **PASS criterion**: BOTH cross-reviewers return PASS on their respective single-axis clauses; JOINT clauses PASS independently in BOTH verdicts
- **FAIL criterion**: either cross-reviewer returns FAIL on ANY clause → Stage 2 → 3 promotion blocked

### Stage 3 — Permanent Registration

- **Where**: replace `STAGE-1-CANDIDATE` with `STAGE-3-PERMANENT`
- **Status**: permanent — eligible for citation as a structural theorem without the candidate qualifier

### Axis-B Selection Protocol (S88 W-14 W4a-17 V.2; B.15)

Stage-2 Axis-B reviewer selection MUST satisfy ALL THREE conditions:

1. **Axis-distinctness**: Axis-B reviewer's primary methodology is on a DIFFERENT axis from Axis-A.
2. **Original-authoring-agent exclusion with downstream-inheritance reach**: neither cross-reviewer may be (a) the original workshop authoring agent OR (b) a successor agent whose memory inherits the workshop's reading-path through prior session synthesis.
3. **Audit-coverage adequacy**: the Axis-B reviewer's domain expertise MUST cover ALL joint clauses + ALL Axis-B-side single-axis clauses.

**K=1 calibration corpus**: Stage-2 dispatch for §VII.W-3.LAB STAGE-1-CANDIDATE selected lizzi (Axis-A spectral) + transit-dynamics-aether-mechanic (Axis-B transit). Failure mode encountered: lizzi's project memory inherited from S87 W-9 R3-B Path-(c) lock-in via direct re-citation in lizzi's `reference_*.md` memory files — the downstream-inheritance reach test FIRES, requiring re-dispatch with non-lizzi spectral-side reviewer (re-routed to connes-ncg-theorist).

### Substrate-input-orthogonality clause (S88 W-23 W7c-167 V.1)

For any Stage-2 verification with N ≥ 2 observables, the procedural floor MUST be supplemented with the predicate: ∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both). PASS-AND across orthogonal-data observables is the structural ceiling for the procedural-floor independence guarantee. Without substrate-input orthogonality, Stage-2 PASS-AND establishes structural-output-type independence (different decision pipelines on the same data) but not structural-input independence.

K=1 SUGGESTION pending K=3 MANDATORY. Stage-2 PASS-AND verdicts emitted under SUGGESTION status carry an explicit "substrate-input-overlap caveat" tagging when the predicate fails.

### Cross-reviewer-machinery-self-authorship requirement (S88 W-23 W7c-167 V.8; B.60)

If reviewer R applies a parse-tree decision procedure / 4-corner classification / cohomology bridge map at the verdict-emission layer, R is NOT the sole author of that machinery. If R is the sole author, an alternate machinery route MUST be applied at the verdict layer OR a second reviewer cross-checks the machinery application. K=1 SUGGESTION pending K=3 MANDATORY.

### Cross-link to "What Does NOT Count as Evidence" item 2

The 4-stage pathway is the constructive complement to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2. "Agreement among agents" with shared workshop context → still NOT evidence. "Agreement among agents" with NO shared context (Stage 2 cross-reviewers reading only the registered Stage-1 entry) → IS evidence per the standard "What Counts as a Result" criterion.

### Calibration corpus

- **Joint F_2-Class Path-(c) Theorem (S86 W-9 lizzi+transit)**: 6-clause statement with 4 corrigenda. Joint clauses (c) and (d). Stage 1 queued as `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` (CF-1, ~0.5 wave-equivalents); Stage 2 queued as `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (CF-6, ~1.0 wave-equivalents); Stage 3 blocked on Stage 2 PASS.
- **§VII.AM Universal Lock Condition (S88 W1b2-65)**: second STAGE-1-CANDIDATE in the corpus; 3-clause joint theorem (J3 BH-horizon pixelation lock + S58 fold-effacement Γ_eff=0.99970 + W1b2-64 cascade-tail Page-time non-activation).

---

## VI. Methodology-wave classification (M1–M4 strict conjunction)

Source: `wave-classification.md` (S86 W-13 RULE-1 / Sigma_2).

Every wave in a session plan MUST be classified at plan-freeze time as one of:

- **METHODOLOGY-class** — wave produces rule-file / template / skill edits whose PASS predicate is artifact-existence-with-substantive-content, NOT a numerical comparison against a pre-registered threshold.
- **COMPUTE-class** — wave produces computation numerical output with a pre-registered PASS / FAIL / INFO threshold (the canonical S82+ pattern).
- **MIXED-class** — wave contains BOTH METHODOLOGY-style and COMPUTE-style gate-items; MUST be sub-wave-decomposed before plan-freeze.

A wave is **METHODOLOGY-class** iff ALL FOUR of the following M1–M4 tests hold (strict logical conjunction):

### M1 — PASS predicate type

```
PASS iff (file F exists at path P)
        AND (F contains section §S)
        AND (substantive_line_count(§S) >= 15)
        AND (content_sha256(§S) matches input-pin-map-derived hash)
```

Failing M1: any predicate of the form `value < threshold`, `|x − y| < tol`, `eigenvalue in band [a, b]`, `chi_squared < N`, or any other numerical comparison against a pre-registered numerical threshold.

### M2 — Producing-operation type

Restricted to:
- `Edit` / `Write` / `MultiEdit` on files matching `.claude/{rules,templates,skills}/**`
- `grep` / `wc` / SHA-256 cross-checks
- Integer counts (line counts, section counts, slot counts)

FORBIDDEN: ANY `.py` script whose output is a numerical comparison against a pre-registered threshold; eigenvalue computations, linear algebra, FFTs, integrals; fixture-with-hand-engineered-numerical-targets (the W0a-2 trap).

### M3 — Source-of-truth type

The wave's content derives from one of: verbatim sub-diff from a prior closed workshop / synthesis; verbatim 5-class taxonomy / pre-registered enumeration from a rule-file or registry entry; anchor-citation-only landings (registry pointer rows).

FORBIDDEN: first-principles new derivation; substantively new physics; new theorem proofs without an upstream workshop deriving them.

### M4 — Allowlist membership

The wave's gate-ID appears in `.claude/rules/methodology-wave-allowlist.md`. The allowlist is append-only and orchestrator-only-edit (subagents denied edit by harness convention).

### Strict-conjunction requirement

The 4-test is `M1 ∧ M2 ∧ M3 ∧ M4`. ALL FOUR must hold. Any one failure routes to:
- M1 fails → COMPUTE-class
- M2 fails → COMPUTE-class OR MIXED-class
- M3 fails → upstream workshop or COMPUTE-class first
- M4 fails → COMPUTE-class fallthrough OR plan-freeze halt

### NROY clause

A wave CANNOT be both COMPUTE-class and METHODOLOGY-class. The 4-test conjunction and its negation cannot both hold, so the classification is partition-honest by construction. **MIXED-class** waves MUST be sub-wave-decomposed before plan-freeze (precedent: S86 W0a-2 → W0a-2a (COMPUTE half) + W0a-2b (METHODOLOGY half)).

### Forward-pinned-follow-up wave class (S88 W-25 W7c-167 §V.2; SUGGESTION at K=1)

A wave is **forward-pinned-follow-up class** iff M1'–M4' hold (analog of METHODOLOGY-class):
- **M1'**: ≥ 1 gate's machinery pin or input-SHA pin points to mid-session-expected landing
- **M2'**: plan's downstream decision-point table specifies routing for the prereq-block scenario
- **M3'**: item-1-clean per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"`
- **M4'**: wave-class allowlist consistency

Orthogonal to count-keyed PLANNING DEFECT trigger (covered_count ≥ 4); structural-class-keyed.

---

## VII. Methodology-wave allowlist (append-only orchestrator-only)

Source: `methodology-wave-allowlist.md` (S86 W-13 / Sigma_5; per-instance provenance at `methodology-wave-instances.md`).

### Schema (3-column, post-S88 W9-RULE-CLEANUP lift-out)

```
gate_id | session | sha256_of_plan_block
```

Per-row rationale prose (rule extension landed, registry slot written, K-counter advance, M1-M4 conjunction enumeration, authorship/role notes) lives at `sessions/framework/registry/methodology-wave-instances.md` keyed by `### {gate_id} ({session}) — {sha}` heading. The rule file is the authoritative M4 allowlist; the registry is the provenance ledger.

### Edit discipline (4 rules)

1. **Append-only** (rows MAY be added; rows MAY NOT be removed/reordered/modified post-landing)
2. **Orchestrator-only edit** (subagents denied Edit/Write/MultiEdit by harness convention) — closes the recursion attack
3. **Per-row dual-SHA** (computed via `closure_hash(plan_block_text)` matching audit-SHA pattern)
4. **Append-helper writes 3-column rows only** + parallel registry entry per `### {gate_id} ({session}) — {sha}`

### Recursion-attack closure

WITHOUT orchestrator-only edit: a subagent dispatched on a non-allowlisted gate-ID could append its own gate-ID to the allowlist mid-execution, satisfying M4 by self-promotion and bypassing the M1-M4 conjunction's intent.

WITH orchestrator-only edit: subagent edit-denial breaks the self-promotion path; allowlist additions can only originate from the orchestrator at plan-freeze time (or from explicit user instruction).

### Cardinality

Post-S88 close: ~62 rows across S86–S88. S88 contributes the bulk (~50 rows) covering registry landings, rule-file extensions, K-counter advancements, and AMRI promotions.

### S88 W9-RULE-CLEANUP lift-out

Schema column count 4→3 (rationale column lifted to `methodology-wave-instances.md`). Allowlist size 42928 → 10872 chars (74.7% reduction; well under 40K harness threshold). The 40 per-row rationale prose entries lifted verbatim to NEW registry file (39089 chars).

---

## VIII. AMRI cleanup history

Source: `agent-standards.md §"Agent-Memory Registry Inversion (AMRI)"` (3-test protocol).

### AMRI tests (any one fires AMRI)

1. **Input-pin test** — another gate lists the memory file as Input-SHA pin in its PRDR machinery block.
2. **Output-target test** — a gate's method section writes to `.claude/agent-memory/*/MEMORY.md` or `project_*.md` as primary registry-maintenance output.
3. **Cross-agent overlap test** — two or more agents' memories contain overlapping entries for the same observable, mechanism, or detector.

### Scope of "memory files"

BOTH per-agent `.claude/agent-memory/<agent-type>/*.md` AND orchestrator project memory `~/.claude/projects/<project-slug>/memory/*.md`. The user's clarification (2026-04-28): "you HAVE to follow AMRI [for orchestrator memory]; not [following] fully breaks the traceability."

### Calibration corpus (≥4 AMRI promotions documented)

| # | Source | Target | Session | Notes |
|:-:|:-------|:-------|:--------|:------|
| 1 | `sessions/session-plan/session-87-plan-w13.md` lines 664-668 (5 agent-memory pin rows: connes-ncg, spectral-geometer, transit-dynamics, volovik, gen-physicist) | removed from INPUT-PIN MAP table; project-level RQ ownership at §W13-1.5 retained | S87 W0 (2026-04-28) | Test 1 fired on each of 5 rows; per-agent role assignment was redundant bookkeeping with AMRI penalty. |
| 2 | mack-cosmic-bridge `reference_key-constraints.md` (Planck/DESI/BICEP-Keck observational anchors + framework prediction snapshots S58–S66) | `sessions/framework/registry/mack-observational-constraints.md` | S87 W0 (2026-04-28) | Test 1 fired multiple times (`session-85-plan-w4.md:357`, `session-86-plan-w15.md:240`, `session-87-plan-w9a.md:848`, `archive/session-68-context.md:158`); cross-agent overlap test ALSO fired with `falsifier-master-inventory.md`, `branch-iv-canonical.md`, `pre-registered-observations.md`. AMRI-promoted with provenance header + cross-link table. |
| 3 | rule-file bloat (`cross-pillar-bridge-anatomy.md` + `epistemic-discipline.md` crossed 40K harness perf threshold via per-wave instance landings) | `sessions/framework/registry/cross-pillar-bridge-corpus.md` (6-section corpus) + `sessions/framework/registry/pru-class-corpus.md` (4-section + extensions corpus) | S88 W9-RULE-CLEANUP (2026-05-06) | Cross-pillar 49672→29241 chars (41% reduction); epistemic 43709→31153 chars (29% reduction). Rule statements + base calibration retained in parents; per-instance corpora + K-counter logs + axiomatic skeletons lifted with bidirectional cross-link. |
| 4 | `methodology-wave-allowlist.md` 40 rows of multi-paragraph rationale prose (structurally identical to a session log) | `sessions/framework/registry/methodology-wave-instances.md` | S88 W9-ALLOWLIST-LIFT-OUT (2026-05-06) | Allowlist size 42928→10872 chars (74.7% reduction). Schema column count 4→3. Companion to W9-RULE-CLEANUP precedent. |

### Detection tool

`computations/_shared/_agent_memory_inversion_audit.py`. **Migration tool**: `/shortterm <agent>` with AMRI-PROMOTE classification.

### What must NOT live in agent memory

- Watchlists / detector rosters / observational-prediction tables
- Cross-session machinery-parameter registries
- Canonical constant values (those live in `canonical_constants.py`)
- Gate-verdict tables / session-wide tallies
- Anything referenced by another agent's spawn prompt as authoritative data

---

## IX. Workshop methodology (Investigating-Workshops 4-condition definition + 3-question discriminator)

Source: `Investigating-Workshops.md` (S82+; user correction 2026-05-02).

### 4-condition workshop definition (ALL FOUR must hold)

1. **TWO+ agents with COMPETING perspectives on a SPECIFIC TENSION** (not parallel-agreement)
2. **Genuine LEDGER-DISSONANCE** (competing-claim adjudication on a number, sign, structural reading, methodology choice, or convention pin)
3. **Multi-round structure** (R1 steelman / R2 respond to opponent's best case / R3 converge on verdict)
4. **Output: STRUCTURAL VERDICT** (NEW pinned position — verdict, registry entry, rule diff, pre-registered gate — NOT a queued computation)

### What is NOT a workshop

Solo compute follow-ups; verification gates (Stage-2 cross-check, plan-freeze audit); re-listings of WP-enumerated carry-forwards; single-agent "synthesis"; methodology-rule extension proposals where both agents would agree; registry-state classification choices / hygiene-promotion items / framework-housekeeping; parallel-compute-wave structures dressed as N-agent panels.

### 3-question discriminator (apply BEFORE adding any candidate; first YES wins)

- **Q1 — Math/physics adjudication?** Does the candidate's resolution require deciding between TWO+ competing readings of a substrate-physics observable / structural identity / convention with first-principles arguments on both sides? If YES → workshop.
- **Q2 — Registry-state classification, hygiene, gate finalization, or framework-issue?** Does the candidate involve choosing between status markers / promoting LANDED-but-not-promoted records / fixing PROVENANCE-dict hygiene / addressing registry-write race protection? If YES → compute carry-forward to the WP (route to `/rclab-plan` via WP CF blocks, NOT workshop schedule).
- **Q3 — Parallel-compute-wave structure?** N prerequisite conditions, each on a different axis, each with own pre-registered PASS criterion AND verdicts combine via logical AND? If YES → compute carry-forward to the WP, marked "wave-together".

### Routing summary

| Decision | Route to | File / mechanism |
|:---------|:---------|:-----------------|
| Q1 YES | Workshop schedule via `/rclab-investigate` | `sessions/session-{N}/session-{N}-workshop-schedule[-w{W}].md` |
| Q2 YES | Compute carry-forward to the WP | WP §"Carry-Forward Computations" |
| Q3 YES | Compute carry-forward to the WP, marked "wave-together" | Same as Q2 |

### Calibration corpus (failures)

- **S87 batch-1 dispatch (2026-05-02)** — 8 investigators each produced 5-7 "candidates" mostly labeled as "workshops"; on user audit, all 8 seeds contained solo compute follow-ups dressed as 2-agent workshops, verification gates as "workshops", re-listings of wave-synthesis carry-forward queues, narrative inflation around already-WP-known content. User correction: "And these agents are NOT identifying 'workshops', they're just listing carry-forward equations and bloviating."
- **S88 W13 (2026-05-07)** — initial workshop schedule had 4 workshops; user audit removed 2: W-2 §VII.K-META (registry-hygiene, not math; routed as compute carry-forward CF-W13-5) and W-4 PATH-B STEP-0 (parallel-compute-wave dressed as 4-agent workshop; routed as compute carry-forward CF-W13-6 with 4 parallel pre-registered S89 axis-gates + 1 wave-AND closeout). After removals, schedule retained 2 genuine workshops.

### "No workshops" is a valid output

A session with clean PASSes, unambiguous verdicts, no cross-wave conflicts, settled methodology produces ZERO workshops. Honest count: typical session produces 0–4 genuine workshops.

---

## X. Mechanical-closure discipline + Layer-separability carve-out

Source: `mechanical-closure-discipline.md` (S86 W3 origin; S88 W8-89 carve-out).

### 5-clause acceptability for mechanical closure

Orchestrator-authored verdict-line emission for upstream-blocked gates may be authored ONLY when ALL FIVE hold:

1. **Upstream-block topology is the cause**: every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, AND plan's downstream decision-point table specifies the documented outcome
2. **Verdict honesty**: emitted verdicts are FAIL or PRE-REG-INC, NEVER PASS. PASS verdicts from a mechanical closure script are PROHIBITED_ACTIONS Class 4 (ansatz-forced PASS).
3. **Per-gate-distinct audit_sha256**: pinmap embeds per-gate identity keys so SHAs are pairwise distinct
4. **Audit-trail signature**: descriptive `value` string names blocking prereq + status; future audit can grep + verify
5. **Working-paper update is in-script**: the closure script MUST update WP §Status / Verdict / Results / Substrate-framing IN THE SAME RUN as the verdict-line append

### Layer-separability carve-out (S88 W8-89; SUGGESTION at K=1 → MANDATORY at K=3)

Admits closed-form mechanical evaluation on Type-F (single-summand-projection-trace) sub-observables WITH conditions L1–L4 + Stage-2 PASS-AND:

- **L1 — Layer-functor cleanness**: substrate-physics observable admits F decomposition; Type-F vs Type-S partition aligns with substrate ↔ methodology layer pair under F.
- **L2 — Type-F closed-form**: Type-F sub-observable admits closed-form algebraic identity (canonical: single-summand-projection trace `Tr_{M_n(C)}(P · A)` with P minimal central projection on `A_K = C ⊕ H ⊕ M_3(C)`); evaluable bit-precision in single-pass pure function.
- **L3 — Type-S separation**: Type-S structurally separated per algebra-axis orthogonality 4-corner classification; mechanical closure on Type-F does NOT pre-determine Type-S verdict.
- **L4 — Honesty disclosure**: verdict-line `convention=` field MUST encode the carve-out tag `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F`; WP section MUST include explicit Type-F / Type-S separation paragraph.

### Stage-2 cross-reviewer PASS-AND requirement

- **Axis A** (spectral / NCG-axiomatic): connes-ncg-theorist audits L1 + L2 from spectral side (verifies F decomposition + closed-form evaluation matches central-projection trace identity)
- **Axis B** (substrate / superfluid-universe): volovik-superfluid-universe-theorist audits L3 + L4 from substrate side (verifies Type-F vs Type-S structural separation + convention-tag matches substrate-IS / laboratory-IN distinction)

Both operate WITHOUT prior workshop context. Stage-2 PASS-AND requires ALL FOUR clauses (L1, L2, L3, L4) to PASS independently in BOTH cross-reviewer verdicts (logical AND, not OR).

### PLANNING DEFECT trigger

Fires at `covered_count ≥ N_PLANNING_DEFECT_THRESHOLD = 4`. Wave plan was OVER-OPTIMISTIC about prerequisite landings. Class-8 PRU vulnerability at plan-authorship time. Closing-paragraph-coherence disambiguation (S88 W-25 W7c-167; B.19): the trigger is count-keyed independent of item-1 status; the closing paragraph "remains acceptable AT EXECUTION TIME" assumes item-1-PASS BY CONSTRUCTION (literal-independent reading canonical, strict-conjunctive REJECTED).

### Cross-link to PROHIBITED_ACTIONS Class 1 (boundary)

The L4 honesty-disclosure clause is the boundary between the structural extension (this carve-out) and PROHIBITED_ACTIONS Class 1 (convention-shopping). A closure script that emits a generic `convention=<scheme>` tag without the `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` suffix while silently performing Type-F partition closure is convention-shopping — Class 1 violation.

---

## XI. Substrate-first canonical-sourcing

Source: `substrate-first-canonical-sourcing.md` (S86 W1a-S3).

Operates at the **canonical-sourcing axis** (complementary to `phononic-framing.md`'s explanation-direction axis): pins must source from substrate's first-principles computation, not external-paper provenance treated as authoritative.

### Methodological vs canonical (the operational distinction)

External-paper provenance is **METHODOLOGICAL** (correct usage) when serving as: conceptual framing references; cross-check anchors; heritage citations; notational source for definitions.

External-paper provenance is **CANONICAL** (FORBIDDEN — must reroute to substrate-first source) when: providing the NUMERICAL VALUE of a pin without substrate-first computation having been performed; citing a paper section heading without verifying it exists; treating schematic library helper outputs as physical regularizations without disclosing the SCHEMATIC class; using order-of-magnitude estimates as pinned values when the substrate canonical exists.

### 4-step audit pattern

`_substrate_first_provenance_audit.py` (proposed S87 carry-forward V.1):

1. **External-paper heading glob**: if absent → AUDIT-FAIL `ABSENT-EXTERNAL-HEADING`; recommend rerouting to substrate source via `mcp__knowledge__.search_knowledge`.
2. **Placeholder pattern detection**: regex on pin VALUE: `O\(10\^?-?\d+\)`, `≈ ...`, `~ 10\^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`. Conjunction with substrate-canonical existence test.
3. **Schematic library helper detection**: verify CLASS pin field FULL vs SCHEMATIC; verdict-line `convention=` carries `-SCHEMATIC` suffix.
4. **Substrate-first computation citation** → AUDIT-PASS.

### SCHEMATIC vs full physical level pin rule (MANDATORY at K=4 promotion, S88 W7b-83 close)

When a computation script consumes a helper module whose docstring identifies it as SCHEMATIC analog (canonical: `_spectral_action_regulators.py`):

1. The plan gate-block MUST include CLASS pin field with FULL or SCHEMATIC.
2. The verdict line MUST encode the class in the `convention=` field (e.g., `convention=substrate-distance-1-SCHEMATIC`).
3. The synthesis section MUST include explicit cross-class disclosure paragraph.

### Class-(f) PIN-PLACEHOLDER calibration corpus (K=4 MANDATORY at S88 W7b-83)

| # | Witness | Class | Severity |
|:-:|:--------|:------|:---------|
| 1 | W4-2 (S86; reclassified Class-(d) per S88 W-24) | NEGATIVE-CALIBRATION baseline | MANDATORY band |
| 2 | W9b-2 (S87; reclassified Class-(d) per S88 W-24) | NEGATIVE-CALIBRATION | MANDATORY band |
| 3 | W9c-1 (S87) | POSITIVE-CALIBRATION canonical model with `convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC` + `tier_pin=TIER-2` companion row | NO-ACTION |
| 4 | W5b-2 sub-test (c) (S86) | CALIBRATION-LOCUS-EXEMPT inheritance locus | EXEMPT |

### Substrate-first calibration corpus precedents (3 first-witnesses)

- **W0c-3 §(b)** (vdd §VI absent in 14 papers; rerouted to S83 W2-G24 Cartan-flat R|_{Cartan⁴} = 0)
- **W4-2 line 503** (SCHEMATIC `_spectral_action_regulators.py` helpers vs full Connes-Chamseddine 1996 §2.2-2.3 physical multipliers)
- **W5a-2 §10** (placeholder `xi_E_GGE_inv ≈ O(10⁻²)` vs canonical `xi_E_GGE_inv = 13.642473425595973` from W4 P4 commit; D_max = 3.13 OOM hits HARD-HALT band)

---

## XII. Registry-landing conventions

Source: `registry-landing.md` (S86 W-3 RULE-1 + S88 W3c-30 + S88 W8-92).

### SOURCE-DOUBLE-CITE-CO-PRIMARY

For sequential V_input + C_output chains (NOT PRIMARY+CONFIRMATION which assumes parallel independence).

```
§VII.{slot} {THEOREM-NAME}
  ANCHOR-1 (input layer, V): {citation}
  ANCHOR-2 (output layer, C): {citation}
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V → A_F → C → conclusion
  Closure SHA pin: {64-char workshop verdict SHA}
```

### 4-condition detection

1. **Sequential** — Anchor-2 cannot be invoked WITHOUT first invoking Anchor-1
2. **Non-fungible** — anchors cannot be swapped or reordered without breaking the chain
3. **Both anchors must remain accessible** — neither can be deprecated or removed without invalidating the conclusion
4. **Both anchors must be on the same algebra-axis cell** (S88 W-15 V.6) per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. **Cross-corner co-primary FORBIDDEN.**

### Bridge-Landing Script Architecture (single-shot pattern; S88 W3c-30)

```
write_promotion → fsync → re-read → verify → emit (exactly one verdict line)
```

The promotion text is FULLY built in memory before any disk write; the post-fsync re-read is the FINAL verification step; the verify step's outcome determines the verdict; the emission is exactly one canonical line + one dual-SHA companion row.

**FORBIDDEN BEFORE pattern**: write → re-read → verify → conditionally re-write/append (FAIL/INFO emit) → re-read → re-verify → emit corrective PASS. Calibration corpus: S87 W5 dispatch trace (4-of-5 dual-trio FAIL/INFO → PASS verdict-line records at `computations/session-87/s87_gate_verdicts.txt:149-178`).

### Operator-Projection Reading-A Naming Hygiene (MANDATORY at K=3, S88 W8-92 close, 2026-05-05)

Registry slots admitting BOTH operator-projection (algebra-INVARIANT central-projection traces) and state-projection (algebra-DEPENDENT state-pair functionals) readings MUST suffix-tag the projection side:

- Operator-side: `§VII.X.OP-PROJ`
- State-side: `§VII.X.STATE-PROJ`
- Bare `§VII.X` (without suffix) is FORBIDDEN when both readings admissible.

**K=3 calibration corpus**: S87 W4-2 §VII.AJ.W4-1 + S87 W6-1 §VII.AG.1 + S87 W11-meta-2.

**Audit detection regex**:
- Positive (admissible): `^### §VII\.[A-Z]+(\.[A-Z0-9-]+)*\.(OP-PROJ|STATE-PROJ)\b`
- Negative (FORBIDDEN when both readings admissible): bare `^### §VII\.[A-Z]+\b(?!.*(?:OP-PROJ|STATE-PROJ))`

### Calibration corpus origin

S86 W-3 R3 Convergence #2 (Path-H/Path-C multi-valued classification (a)). V1 (3He-B BDI 0D inheritance arrow) + C1 (Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality of A_F = C ⊕ H ⊕ M_3(C)). Volovik's R2-A V1-PRIMARY framing was REVOKED at R3-A; SOURCE-DOUBLE-CITE-CO-PRIMARY adopted.

---

## XIII. Verifier-rubric pre-registration (Class 8.2)

Source: `epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"`. K=5 MANDATORY at S88 W-7/W-21/W-22 simultaneous advancement (2026-05-08).

### 4 required elements

When a gate's PASS criterion involves rubric-grading of qualitative content:

1. **Pattern set**: enumerate specific lexical / structural patterns the verifier accepts (e.g., for substrate-first: `D_K`, `spectral moment`, `Mellin-cone`, `spectral residue`, `Seeley-DeWitt`, `Heitsch cocycle`)
2. **Disjunction-vs-conjunction declaration**: ALL patterns required (conjunction) or ANY (disjunction) per content unit
3. **Negative-marker set** (optional): patterns that auto-fail (e.g., `"in curved spacetime"` without explicit substrate-correction marker)
4. **Pre-registered calibration corpus**: 1+ exemplar passing-content snippet pinned by SHA

Without (1)–(4), execution-time iteration to calibrate the rubric is structurally indistinguishable from iterate-until-PASS (Class 6 PROHIBITED_ACTIONS) — even when underlying content is unchanged across runs.

### Cross-Proxy Adjudication extension (T1-19, S86 W-9)

When a cross-review gate is dispatched to challenge a prior INFO/FAIL via alternative proxy:

1. Pre-register the proxy operationalization with rubric pinning per (1)-(4) above
2. **Open-verdict framing**: the verdict between (A) prior FAIL stands and (B) cross-proxy yields PASS MUST remain open and not pre-judged
3. **Document the proxy's algebraic relationship to the prior**: ALGEBRAICALLY DISTINCT (different operator/pole/Mellin slot) or ALGEBRAICALLY EQUIVALENT but semantically distinct

### K=5 calibration corpus

| # | Source | Failure mode |
|:-:|:-------|:-------------|
| 1 | S86 W-12 BULLETIN-S4 | Rubric initially required literal "Seeley-DeWitt" string; bulletin #4 used canonical "Mellin-cone moment of D_K" + "spectral residue" — substrate-first but lexically distinct. "Z_4 or similar" admitted V_4 via cardinality match. |
| 2 | S86 W-8 R3 / W2-11 | Stratum-vs-Cartan-toral V_4 underdetermination under rubric |
| 3 | S88 W-7 W2-2 V.5 D-W8-1 | Rubric underdetermination at the bot20-vs-stratum reading layer |
| 4 | S88 W-22 W7a-74 V.3 | Numerical-metric class: `spread ≤ 0.06` rubric admitted both `full_atlas` and `f2_only_class` definitions |
| 5 | S88 W-21 W6b-56 V.6 | Boundary-direction sub-check: asymptotic-limit phrasing admitted FALSE claim ("recovers 8 at τ → 5π" structurally false under direct Python verification) |

---

## XIV. Publication-precision pre-registration (Class 8.3)

Source: `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"`. K=4 MANDATORY at S87 W8 close (2026-04-30).

### 5 required elements

When a gate's output VALUE will be cited downstream:

1. **Publication precision pin**: state number of significant figures (e.g., `n_s_published_sig_figs = 15` for full float64; `= 10` for ten-figure presentation)
2. **Verifier tolerance match**: downstream verifier MUST set `rel_tol ≥ 10^(−publication_sig_figs)`. A verifier with rel_tol tighter than publication precision is structurally guaranteed to FAIL on precision-floor mismatch.
3. **Round-trip cross-check**: producing gate emits full float64 to `.npz` AND rounded value to working-paper section. Downstream verifier loads from data file (full precision), not working-paper.
4. **Canonical-metric pin** (cluster-span family): when a refactor's threshold compares against a canonical-anchor value reported in a prior session's verdict file, the threshold formula MUST express the same metric the canonical reports.
5. **Algebraic-equivalence audit at plan-authorship**: when a spawn prompt cites a canonical-anchor value, plan-authoring orchestrator MUST verify the spawn-prompt's threshold formula is the same function of underlying quantities

### K=4 calibration corpus

- **W1c-8 `n_s`** (S86): 10-sig-fig presentation (0.9784607074) vs full float64 (0.978460707430765); rel_tol=1e-12 < 1e-10
- **W2-4 cluster-span** (S86): canonical-metric `|ratio − 2|` vs normalized form factor-2 mismatch at float-cancellation floor (~1e-15)
- **W8-2 `max_pair_ratio_A_5`** (S87): 6-sig-fig published (9.240439e-01) vs full float64 (9.240438549812e-01); FAIL composite sign=PASS/mag=FAIL/regime=VALID; promoted `max_pair_ratio_A_5_FW = 9.240438549812e-01` to `canonical_constants.py`
- **W8-8 `gv_canonical_difference`** (S87): 14-sig-fig plan-pinned (-40579.15004795) vs full float64 (-40579.1500479506); INFO composite (per-regulator deviation = ZERO across A_5_extended)
- **W13-3 R_842 stale-rectangle relabel** (S86; Class-(c) PIN-DRIFT-FROM-STALE-SOURCE): plan §W13-3.6 cited `R_842 = [-1.05, -0.85] × [-0.2, +0.2]`, but per S84 migration table that's the OLD R_918; migrated R_842 is `[-0.942, -0.742] × [-0.2, +0.2]`

---

## XV. Forward methodology debts

### K-counter advancements pending (advisory until K=3)

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
- Cross-reviewer-machinery-self-authorship requirement: K=1, SUGGESTION

### Audit-script extension queue

- `_substrate_first_provenance_audit.py` (S87 carry-forward V.1; not yet implemented)
- `_joint_theorem_independent_verify_audit.py` extensions (`S89-STAGE-2-AXIS-B-DOWNSTREAM-INHERITANCE-AUDIT`; substrate-input-orthogonality predicate; cross-reviewer-machinery-self-authorship audit)
- `_registry_landing_audit.py` Class-(g) flags: `OP-VS-STATE-PROJECTION-NAMING-DRIFT`; `S89-CROSS-CORNER-CO-PRIMARY-AUDIT`
- `_machinery_feasibility_audit.py` boundary-direction substitution-chain sub-check
- `_source_reconciliation_audit.py` Class-(g) flags: `JOINT-HYPERSURFACE-1D-SCALAR-DEGENERATE`; `SPEARMAN-SPREAD-METRIC-UNDECLARED`
- `_cross_pillar_bridge_audit.py` extension for Hybrid Independence Test PER-CLAUSE verdict tagging
- `S89-CROSS-PILLAR-BRIDGE-AUDIT-LEVEL2-SUB-CLASS-CHECK`

### Open methodology questions

- Functional-selection methodology (which spectral functional uniquely determines the framework's predictions?) — atlas-08 cross-link
- Layer-functor F audit-leg verification (`S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`)
- M_meta promotion criterion (track future multi-deliverable workshops for adoption of (Scope, Layer) projection; promote at K=3)
- Prompt-encoded-vs-memorized validation (`S87-MCP-DISCIPLINE-INVERSION-VALIDATION` PASS at orchestrator MCP fabrication rate < 5%)

---

## XVI. The 24 framework rule files

Every rule file cited below is verified to exist (24/24 confirmed via `Glob ".claude/rules/*.md"`).

| # | Rule file | Origin | Role (1-line) |
|:-:|:----------|:-------|:--------------|
| 1 | `joint-theorem-promotion.md` | S86 W-9 | 4-stage candidate→registered→cross-axis-verified→permanent pathway; constructive complement to "agreement among agents" exclusion. Includes Axis-B Selection Protocol + substrate-input-orthogonality clause + cross-reviewer-machinery-self-authorship requirement. |
| 2 | `cross-pillar-bridge-anatomy.md` | S86 W-5 | MANDATORY 5-anatomy + 3-level ladder for cross-pillar registry entries; Level-2 layer distinction (binding vs non-binding); Element 1 fiducial-anchor binding; Element 2 OE-form discipline; Hybrid Independence Test K-counter; Algebra-axis orthogonality K-counter (MANDATORY at K=3); Per-Bulletin-per-pole Level-1 wall classification. |
| 3 | `mechanical-closure-discipline.md` | S86 W3 | Orchestrator-authored verdict-line emission discipline for upstream-blocked gates (5-clause acceptability); Layer-separability carve-out (S88 W8-89; SUGGESTION at K=1); PLANNING DEFECT trigger at covered_count ≥ 4. |
| 4 | `regulator-pin-discipline.md` | S86 W0c-7 | a_n^{regulator} tagging mandatory for NEW citations of Seeley-DeWitt coefficients; Sage-Exact Rationals for Ω_GW Regulator-Class Values extension; Class-(c) PIN-DRIFT-FROM-STALE-SOURCE W-11 calibration corpus extension. |
| 5 | `regulator-convention-lockdown.md` | S86 W12-4 | Mellin-Barnes / Schur-Zubarev convention freeze (CAC) for DR3-class L_max-stability gates; demarcation theorem (admissibility class via effacement-preservation criterion at L=10). |
| 6 | `substrate-first-canonical-sourcing.md` | S86 W1a-S3 | Substrate-IS canonical > external-paper provenance; 4-step audit pattern; SCHEMATIC vs full physical level pin (MANDATORY at K=4); Surrogate-vs-Canonical at Cohomology-Class Layer (K=1 advisory); Class-(f) PIN-PLACEHOLDER taxonomy. |
| 7 | `methodology-wave-allowlist.md` | S86 W-13 | Append-only allowlist of METHODOLOGY-class gate-IDs; orchestrator-only edit by harness convention (closes recursion attack); 3-column schema (post-S88 W9-RULE-CLEANUP lift-out); ~62 rows S86–S88. |
| 8 | `wave-classification.md` | S86 W-13 | M1–M4 strict-conjunction test for METHODOLOGY-class; NROY clause (cannot be both COMPUTE and METHODOLOGY); MIXED-class sub-decomposition; Forward-pinned-follow-up wave class (K=1 SUGGESTION). |
| 9 | `Investigating-Workshops.md` | S82+ (user correction 2026-05-02) | 4-condition workshop definition + 3-question discriminator (Q1 math/physics adjudication → workshop; Q2 hygiene → WP CF; Q3 parallel-compute-wave → WP CF wave-together); calibration corpus (S87 batch-1 8-investigator failure; S88 W13 2-removal). |
| 10 | `inheritance-falsifier-protocol.md` | S86 W-5 RULE-3 | Rank-2 ker(ι_*) protocol with 4 gates (kernel-signature decisive + cohomology-asymmetry ratio + kernel-signature supporting + slope-discrimination); (Δ_B/Δ_A)^p cancellation theorem. |
| 11 | `registry-landing.md` | S86 W-3 RULE-1 | SOURCE-DOUBLE-CITE-CO-PRIMARY (sequential V+C chains); Bridge-Landing Script Architecture (single-shot pattern, S88 W3c-30); Operator-Projection Reading-A Naming Hygiene (OP-PROJ vs STATE-PROJ; MANDATORY at K=3, S88 W8-92). |
| 12 | `phononic-framing.md` | S86 W-5 RULE-2 | IS-not-IN convention (substrate IS observable, not IN container); LCDM-vs-substrate vocabulary table; Single-τ-slice vs moduli-deformation substrate-IS levels (S88 W-2 W2-10; K=2 advisory). |
| 13 | `epistemic-discipline.md` | S82+ (extended; v3 union landing S86 W0a-1) | Layer-Decomposition (F functor); Phi correspondence; PRU Class 8.0–8.6 sub-class taxonomy; Source Reconciliation Class-(a)–(f) taxonomy; Verifier-rubric pre-registration (Class 8.2); Publication-precision pre-registration (Class 8.3); Pole-Scope sub-clause (MANDATORY at K=4, S88 W7a-72); Resolution-Specificity Scoping sub-clause; Closing-Paragraph-Coherence Audit Pattern (EG1). |
| 14 | `evoi-prioritization.md` | S82+ | Framework probability methodology; EVOI = P(pass)·\|delta_P(pass)\| + P(fail)·\|delta_P(fail)\|; effort-based probability tracking. |
| 15 | `agent-standards.md` | S82+ (HIGH-DENSITY WORKSHOP TEMPLATE T2-5 from S86 W-12) | Universal agent standards (formal rigor, persistent memory); AMRI 3-test detection; HIGH-DENSITY WORKSHOP TEMPLATE (multi-layer output-slot decomposition). |
| 16 | `output-standards.md` | S82+ (T1-13/T1-14 from S86 W-3) | 7-component action items format; 7-section handoff document; Workshop Wrap-Up "What Changed" numerical-vs-structural distinction; Carry-Forward Dependency Enumeration. |
| 17 | `teammate-behavior.md` | S82+ | Inbox-first; 3-files-before-inbox-recheck cap; one-writer-per-output; deduplicate-notifications-against-completed-work. |
| 18 | `session-handoffs.md` | S82+ | Session naming (`session-NN/`); mandatory handoff per Output Standards 7-section format; chronological integrity (never renumber); recommendation carry-forward (next session's plan is ONLY carry-forward mechanism). |
| 19 | `computation-environment.md` | S82+ | Hardware + Python specs (`phonon-exflation-sim/.venv312/Scripts/python.exe`; AMD RX 9070 XT; CPU thread-cap pattern); referenced by `math-scripts.md`. |
| 20 | `knowledge-index-usage.md` | S82+ | MCP knowledge query discipline; canonical pattern (search_knowledge before computing; get_constant for value+provenance; trace_entity for evidence chain). |
| 21 | `math-scripts.md` | S82+ (extended S87 W11) | Canonical constants discipline (every S34+ script imports from canonical_constants.py); local variable tagging `# (local)`; double-check logic before compute (substitution chain mandatory for sign/direction/threshold claims); D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check (S87 W11 calibration); machinery-feasibility audit; canonical write-order for new framework predictions; mnemonic-vs-exact ratio discipline. |
| 22 | `mcp-servers.md` | S82+ | MCP server inventory (knowledge, sage, paper-search, mathscinet, oeis, zbmath, astro, madrigal); query patterns + reinforcement guidance. |
| 23 | `gate-verdicts.md` | S82+ (Option A landed S88 W8-100) | Verdict-line schema (canonical line + dual-SHA companion comment row); Option A `supersedes=<old_audit_sha>` tag protocol under absolute verdict permanence; canonical `append_verdict()` helper. |
| 24 | `v3-closure-recovery.md` | S82+ (S78 origin) | Stage 1 automatic re-dispatch (max 2 iterations per signal); Stage 2 V3-NON-COMPLIANT fallback; Stage 3 user-intervention trigger; PROHIBITED_ACTIONS Class 1–4 (convention-shopping, iterate-until-PASS, post-hoc pre-registration editing, ansatz-forced PASS); bounded-iteration termination proof. |

**Total: 24 rule files** (target ≥14 — substantially exceeded).

---

## XVII. The 9 framework templates (+1 frozen example)

Every template cited below is verified to exist (9/9 confirmed via `Glob ".claude/templates/*.md"`).

| # | Template | Role |
|:-:|:---------|:-----|
| 1 | `pru-pre-registration-template.md` | Canonical PRDR scaffold + 8-item R3 YAML gate-block + cutoff_axis YAML pin + PRDR keyword 8-K-atom enumeration + 5-class file-pin (SHA) taxonomy. Cited by `epistemic-discipline.md §"Pre-Registration Completeness"`. |
| 2 | `iteration-audit.md` | Standardized decision rule + tag vocabulary (8 tags: integrator-config / convention-pin-fix / convention-pin-ADDITION / regime-diagnostic-addition / quantity-definition-drift / unclear / iterate-until-PASS / verdict-class-transition) + severity grading (HIGH / MEDIUM / LOW) + WARRANT classes + remediation format. Eliminates PRU at audit-workshop level by construction. |
| 3 | `synthesis.md` | Synthesis report template (I. Session Outcome / II. Key Results / III. Gate Verdicts / IV. Structural Implications / V. Carry-Forward Computations [MANDATORY 4-field specs]). Per `feedback_fix-in-session-never-defer.md`. |
| 4 | `workshop.md` | Workshop document template (build FULL skeleton before launching agents; *[NOT STARTED]* placeholders filled by agents during execution). Multi-round structure (R1 / R2 / R3) per `Investigating-Workshops.md`. |
| 5 | `workshop-schedule.md` | Workshop / Synthesis Schedule template (campaign of slash-command invocations across `/rclab-review` solos + `/rclab-workshop` workshops). Skill-slot mapping load-bearing invariant. Produced by `/rclab-investigate`. |
| 6 | `workingpaper.md` | Working paper template (the answer log; runtime agent writes its gate's completed entry). Canonical shell shape at `examples/workingpaper-shell-example.md` (frozen). |
| 7 | `agent-roster.md` | Canonical name-to-type mapping (Name Prefix → subagent_type → Short Name); resolves SendMessage routing. |
| 8 | `plan-compute.md` | Compute plan template (Session Objective with pre-registered master gate; Wave Structure with dependency graph; per-wave gate blocks). |
| 9 | `mellin-balance-pre-declaration.md` | Mellin-Balance Pre-Declaration template (S84 W6-71 origin); MANDATORY for all S84+ cluster-test gates; prevents recurrence of S83 G15/G28/G34 ad-hoc cluster-membership failures by forcing pre-registration of Mellin-moment balance BEFORE any scan is run. |

**Plus**: `examples/workingpaper-shell-example.md` (frozen 10-gate dispatch shell, does not get filled in by runtime).

**Total: 9 templates + 1 frozen example** (target ≥6 — exceeded).

---

## XVIII. Cross-atlas dependencies

### Atlas-09 (retractions)

AMRI cleanups documented in §VIII are SUPERSESSIONS — agent memory entries that were promoted to project-level registry/correspondence files and SUPERSEDED at the original location. Cross-link entries:
- mack-cosmic-bridge `reference_key-constraints.md` SUPERSEDED → atlas-12 §VIII row 2
- session-87-plan-w13.md INPUT-PIN MAP rows 664-668 SUPERSEDED → atlas-12 §VIII row 1
- cross-pillar-bridge-anatomy.md per-instance corpora SUPERSEDED → atlas-12 §VIII row 3
- methodology-wave-allowlist.md rationale-prose column SUPERSEDED → atlas-12 §VIII row 4

### Atlas-11 (cross-pillar-bridge-corpus)

**Division of labor**:
- **Atlas-11** (substrate-side): cross-pillar bridge ENTRIES — substrate-IS observables with their 5-anatomy + 3-level ladder content. The CONTENT.
- **Atlas-12** (methodology-side): the RULES that govern atlas-11's anatomy. The DISCIPLINE that produces atlas-11.

**Overlap point**: `cross-pillar-bridge-anatomy.md` rule itself appears in BOTH atlases (as content in atlas-11 §X, as discipline in atlas-12 §XVI row 2). Atlas-11 quotes the 5-anatomy + 3-level ladder as the schema atlas-11 entries follow; atlas-12 owns the full rule-file content and audit pipeline.

### Atlas-04 (assumptions)

The methodology floor includes assumed-and-proven items (process axioms): (a) plan-freeze-time pre-registration is binding; (b) verdict permanence (Option A protocol); (c) PROHIBITED_ACTIONS Class 1–4; (d) orchestrator-only edit on rule files (closes recursion attack); (e) AMRI 3-test detection; (f) M1–M4 strict conjunction for METHODOLOGY-class waves; (g) MAX_ITERATIONS_PER_SIGNAL = 2 for v3-closure-recovery Stage 1.

### Atlas-08 (open questions)

Methodology open questions belong in atlas-08:
- Functional-selection methodology
- Layer-functor F audit-leg verification (`S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`)
- M_meta promotion criterion (track future multi-deliverable workshops; promote at K=3)
- Prompt-encoded-vs-memorized validation
- All K=1 SUGGESTION items pending K=3 MANDATORY (8.4/8.5/8.6/Hybrid Independence/substrate-input-orthogonality/closing-paragraph-coherence/F-trigger-split/Forward-pinned-follow-up/Layer-separability)

### `.claude/rules/*` and `.claude/templates/*`

Atlas-12 is the curated index OF the rule-file corpus; the rule files themselves are the canonical source. Every atlas-12 reference cites `.claude/rules/<name>.md:line_number` or `.claude/templates/<name>.md`.

---

## XIX. Substrate-Framing Discipline Compliance (atlas-12 itself)

This atlas treats methodology rules as PROCESS, not physics:

- §II frames F as a Morita-equivalence-preserving FUNCTOR between layers (categorical, not physical)
- §III frames Phi as a graded-ring isomorphism between weight axes (algebraic, not physical)
- §IV–§XIV frames each rule as a discipline that GOVERNS HOW the substrate is investigated, never as substrate physics itself
- §XII (registry landing) explicitly cross-links to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause to enforce that atlas-11 (substrate) and atlas-12 (methodology) are STRUCTURALLY ORTHOGONAL — cross-corner co-primary FORBIDDEN

The methodology floor IS the framework's structural answer to: "how do you ENFORCE substrate-priority discipline at registry-entry granularity, plan-freeze-time, and audit-trail emission, without the substrate being able to police itself?" The 24 rule files, 9 templates, layer-functor F, Phi correspondence, PRU Class 8.0–8.6 taxonomy, joint-theorem 4-stage pathway, AMRI cleanup, methodology-wave M1-M4 + allowlist, workshop 4-condition + 3-question discriminator, mechanical-closure 5-clause + Layer-separability L1-L4 carve-out, substrate-first canonical-sourcing 4-step audit + SCHEMATIC level pin, registry-landing SOURCE-DOUBLE-CITE-CO-PRIMARY + OP-PROJ vs STATE-PROJ, verifier-rubric Class 8.2 K=5 + publication-precision Class 8.3 K=4 — all are structural mechanisms that PRESERVE the substrate-prior direction at the methodology-floor layer.

---

*Sources: 24 rule files at `.claude/rules/` (verified via `Glob`); 9 templates at `.claude/templates/` + 1 frozen example at `.claude/templates/examples/`; `epistemic-discipline.md §"Layer-Decomposition"` (F functor + Phi correspondence); `agent-standards.md §"Agent-Memory Registry Inversion (AMRI)"` (3-test protocol); `joint-theorem-promotion.md` (4-stage pathway + Axis-B Selection Protocol + substrate-input-orthogonality clause + cross-reviewer-machinery-self-authorship requirement); `wave-classification.md` (M1-M4 strict conjunction + NROY clause + Forward-pinned-follow-up wave class); `methodology-wave-allowlist.md` (append-only orchestrator-only allowlist + recursion-attack closure); `Investigating-Workshops.md` (4-condition workshop definition + 3-question discriminator + S87 batch-1 + S88 W13 calibration); `mechanical-closure-discipline.md` (5-clause acceptability + Layer-separability L1-L4 carve-out); `substrate-first-canonical-sourcing.md` (4-step audit pattern + SCHEMATIC level pin K=4 MANDATORY); `registry-landing.md` (SOURCE-DOUBLE-CITE-CO-PRIMARY + Bridge-Landing Script Architecture + OP-PROJ vs STATE-PROJ Naming Hygiene K=3 MANDATORY); `regulator-pin-discipline.md` + `regulator-convention-lockdown.md`; `pru-class-corpus.md` (PRU Class 8.0-8.6 corpus); `methodology-wave-instances.md` (per-instance provenance ledger); `gate-verdicts.md` (Option A protocol); `v3-closure-recovery.md` (PROHIBITED_ACTIONS Class 1-4).*
