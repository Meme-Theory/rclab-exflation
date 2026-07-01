# Epistemic Discipline

IMPORTANT: These rules govern how ALL agents handle evidence, claims, and confidence. Violations undermine the entire research methodology.

This file is a **DIRECTIVE document**. Direction and statement, not log or ledger. Calibration corpus, per-instance narratives, K-counter advancement records, audit-SHA hex strings, dated promotion histories, and session-event provenance belong in `sessions/framework/registry/<topic>-corpus.md` (canonical: `pru-class-corpus.md`), NOT here. Rule extensions land here as directives only; their evidentiary basis lives in the corpus.

## Constraint Methodology

- **Pre-register gates BEFORE computation** — define pass/fail criteria, then compute
- **Negative results are boundaries, not failures** — they constrain the solution space
- **Never cite constraint counts as arguments** — "we have 12 constraints" proves nothing
- **Separate bookkeeping from reasoning** — reference tables and narrative analysis are distinct
- **Latest synthesis wins** — for deduplication, the most recent synthesis document is canonical

## Confidence & Probability

- **No filler confidence language** — avoid "promising," "encouraging," "likely correct"
- **Pre-registered gates are the evidence** — everything else is commentary
- **Framework probability methodology** lives in `evoi-prioritization.md`.

## What Does NOT Count as Evidence

- Restatements of prior claims in new words
- Counts of how many agents agree
- Internal consistency alone (a wrong theory can be internally consistent)
- Analogies without quantitative backing

The constructive complement (how independent agreement DOES enter the registry, via the 4-stage pathway) lives in `joint-theorem-promotion.md`.

## Source Authority Hierarchy

When sources conflict, higher authority wins:

1. Skeptic verdicts (highest)
2. Synthesis files
3. Gate verdict results
4. Session minutes
5. Raw computation output (lowest)

## Evidence Hierarchy

1. **Structural constraints** are permanent. A proven monotonicity theorem, an exact block-diagonality, a representation-theoretic identity — these define the walls of the solution space. Report as geometry: "The allowed region excludes all single-particle spectral functionals."
2. **Computational gates** are decisive. A pre-registered pass/fail criterion tested against new computation is the only thing that changes the state of knowledge. Report as measurements: "KC-3 at tau = 0.50 returned [value] against threshold [value]. Gate status: PASS/FAIL/UNCOMPUTED."
3. **Organizational insights** are useful but not evidential. Report as structure: "These three results trace to a single algebraic identity," not as evidence for or against anything.

## How to Assess a Mechanism

A mechanism lives or dies on its **structural position** within the mapped constraint surface:

- What walls does it respect?
- What gates has it passed?
- What gates remain uncomputed?
- What is the dimensionality and topology of the region it occupies?

Three categories:

- **Well-motivated by the constraint map** — occupies the sole surviving region after systematic elimination.
- **Untested** — in an unexplored region.
- **Closed** — violates a proven wall.

## What Counts as a Result

- A new number computed from first principles against a pre-registered criterion.
- A proven structural theorem (exact or to machine epsilon).
- A constraint that eliminates a region of solution space with a specific mathematical reason.

## What Does Not Count as a Result

- Agreement among agents (shared context produces shared outputs, not independent confirmation).
- Narrative coherence (a good story is not evidence; the universe is not obligated to have a plot).
- The number of prior closed mechanisms (constraint mapping is progress, not a failure rate).
- Restatement of existing results under new organizational framing.

## Reporting Format

For each finding, state:

- **What was computed** (equation, method, numerical result)
- **What region of solution space it constrains** (which mechanisms survive, which are excluded, and why)
- **What remains uncomputed** (the next gate, with its pre-registered criterion)

## Pre-Registration Completeness

Beyond pre-registering gates, a plan must pre-register the MACHINERY each gate depends on. A gate-relevant machinery parameter left unpinned creates execution-time freedom.

- **PRU (Pre-Registration Underspecification)**: plan leaves one or more gate-relevant machinery parameters unpinned. Detection: multiple verdict-log entries for the same gate.
- **PRDR (Pre-Registration Dry-Run)**: before plan-freeze, dry-run the producing script, enumerate every free parameter via static analysis, and pin or declare-as-diagnostic each one in the gate block.

PRU is a plan-property failure (Class 8), structurally distinct from execution-property failures (convention-shopping, ansatz-forced PASSes, vacuous-margin, load-and-compare-to-self, linear-rescale-as-cross-check, iterate-until-PASS, false cross-checks). A scrubbed plan that prevents all 7 execution failures but does not pre-register machinery via PRDR remains PRU-vulnerable.

PRU applies recursively: any process producing gated outputs is PRU-susceptible if its plan does not enumerate its free parameters.

The canonical PRDR scaffold (R3 YAML gate-block, cutoff_axis YAML pin, PRDR keyword 8-K-atom enumeration, 5-class file-pin SHA taxonomy) is at `.claude/templates/pru-pre-registration-template.md`. New gate blocks pull from the template; rule extensions go through the template's changelog.

### PRU Class 8 sub-class taxonomy

| Sub-class | Name | Status |
|:----------|:-----|:-------|
| 8.0 / 8.1 | machinery-pin cardinality failure | MANDATORY |
| 8.2 | verifier-rubric pre-registration failure | MANDATORY |
| 8.3 | output-precision pre-registration failure | MANDATORY |
| 8.4 | representation-convention-pin failure | advisory until K=3 |
| 8.5 | joint-hypersurface-pre-registration-form failure | advisory until K=3 |
| 8.6 | layered-substitution-chain-audit failure | advisory until K=3 |
| 8.7 | degenerate-observable pre-flight failure | advisory until K=3 |

K-counter status, calibration corpus, and per-instance promotion records: `sessions/framework/registry/pru-class-corpus.md`.

### Verifier-Rubric Pre-Registration (Class 8.2; MANDATORY)

When a gate's PASS/FAIL/INFO criterion involves rubric-grading of qualitative content (substrate-first reasoning, container-thinking detection, narrative-quality scoring, framing-compliance check), the gate block MUST pre-register the verifier rubric specification alongside the threshold:

1. **Pattern set**: enumerate the specific lexical / structural patterns the verifier accepts.
2. **Disjunction-vs-conjunction declaration**: state whether the verifier requires ALL patterns (conjunction) or ANY (disjunction) per content unit.
3. **Negative-marker set** (optional): patterns that auto-fail.
4. **Pre-registered calibration corpus**: 1+ exemplar passing-content snippet pinned by SHA so the rubric can be re-validated without re-deriving the qualitative judgment.

Without (1)-(4), execution-time iteration to calibrate the rubric is structurally indistinguishable from iterate-until-PASS (`v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6) — even when the underlying content is unchanged across runs.

**Boundary-direction substitution-chain sub-check**: any plan-block claiming an asymptotic limit / boundary value for a closed-form τ-flow trajectory MUST pre-flight Python-verify boundary direction at plan-freeze. Audit-script extension: `_machinery_feasibility_audit.py` carries the "boundary direction substitution chain" sub-check.

**Spearman-spread metric pre-registration**: every gate whose PASS-band involves a Spearman cross-regulator spread metric MUST declare `spread_metric_definition ∈ {full_atlas, f2_only_class}` in plan-block PIN MAP (`full_atlas` = max − min across all 5 F_2-rep substitutions; `f2_only_class` = max − min across F_2-class members only). Audit-script extension: `_source_reconciliation_audit.py` Class-(g) `SPEARMAN-SPREAD-METRIC-UNDECLARED` flag at plan-freeze with HARD-HALT remediation; detection regex `(?i)\b(spread|range)\b.*(?:0\.06|≤\s*0\.0\d+).*` requires `spread_metric_definition` declaration in the adjacent plan-block.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §1`.

### Cross-Proxy Adjudication

When a cross-review gate is dispatched to challenge a prior INFO/FAIL via alternative proxy:

1. Pre-register the proxy operationalization with rubric pinning per the four Class-8.2 elements above.
2. **Open-verdict framing**: the verdict between (A) prior FAIL stands and (B) cross-proxy yields PASS MUST remain open and not pre-judged. NO Class-6-adjacent ("iterate-until-PASS") framing in the spawn prompt.
3. **Document the proxy's algebraic relationship to the prior**: ALGEBRAICALLY DISTINCT (different operator/pole/Mellin slot) or ALGEBRAICALLY EQUIVALENT but semantically distinct. Declare which.

### Publication-Precision Pre-Registration (Class 8.3; MANDATORY)

When a gate's output VALUE will be cited downstream (in a follow-up gate's verifier, a canonical-constants entry, a registry row), the producing gate MUST pre-register the publication precision alongside the value:

1. **Publication precision pin**: state the number of significant figures the value will be published at.
2. **Verifier tolerance match**: any downstream verifier MUST set rel_tol ≥ 10^(−publication_sig_figs). A verifier with rel_tol tighter than publication precision is structurally guaranteed to FAIL on precision-floor mismatch.
3. **Round-trip cross-check**: producing gate emits full float64 to data file (`.npz`) AND rounded value to working-paper section. Downstream verifier loads from data file (full precision), not working-paper.
4. **Canonical-metric pin**: when a refactor's threshold compares against a canonical-anchor value reported in a prior session's verdict file, the threshold formula MUST express the same metric the canonical reports. E.g., cluster-span gates testing `b_pow(span_2) = 2 · b_pow(span_3)` MUST use `|ratio − 2|` (with `ratio = b2/b3`), NOT `|b2 − 2·b3|/|b2|` (factor-2 different at float-cancellation floor). Expected achievable floor under canonical metric: `~10 × float_eps = 2.22e-15`; safe threshold `< 1e-14`.
5. **Algebraic-equivalence audit at plan-authorship**: when a spawn prompt cites a canonical-anchor value from a prior verdict file, the plan-authoring orchestrator MUST verify that the spawn-prompt's threshold formula is the same function of the underlying quantities as the canonical reference's formula. Differences require either reformulating the threshold to use the canonical's metric, or recalibrating the threshold's numerical bound to the spawn-prompt's metric. Part of `_source_reconciliation_audit.py` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation.

6. **Canonical-pin sanity-check tolerance**: when a downstream verifier performs a sanity-check against a canonical-pin value (e.g., `assert abs(computed − canonical_pin) < abs_tol`), the verifier's absolute tolerance MUST satisfy `abs_tol ≥ pin_value · 10^(−publication_sig_figs)`. A sanity-check with `abs_tol` tighter than the pin's own publication-precision floor is structurally guaranteed to FAIL at the publication-precision boundary, NOT at the substrate-physics boundary. Audit: `_source_reconciliation_audit.py` Class-(a) PIN-TIGHT-SOURCE-LOOSE extension detects sanity-check tolerances tighter than pin publication-precision floor; missing tolerance match → MANDATORY remediation.

Pre-rule gates with published-but-unpinned precision: their downstream verifiers must use rel_tol ≥ 1e-9 (presentation-precision-tolerant default) when no pin is available. Plan-freeze auditors emit MANDATORY remediation on detection of tolerance < 10^(−published_sig_figs) anywhere in plan-block thresholds.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §2`.

7. **Element-5 agreement-precision tolerance + DEFERRED-tag** (advisory until K=3): a cross-pillar-bridge Element-5 anchor published at `n` sig figs MUST set its Stage-2/Stage-3 verifier tolerance RELATIVE at `rel_tol ≥ 10^(−sig_figs_of_agreement)`, where the agreement precision across the anchor's candidate F-images may be FEWER than `n`; an absolute `<ε` with `ε/pin < 10^(−n)` is PIN-TIGHT-SOURCE-LOOSE. A floor-level PASS that cannot discriminate the candidate F-images MUST carry a `canonical-value-question-DEFERRED-to-<recompute-CF>` tag; Stage-3 ELIGIBILITY (tolerance fix) is distinct from STAGE-3-PERMANENT (re-pin to the bit-exact substrate canonical), and the pin is HELD under the DEFERRED tag during the interim rather than sideways-re-pinned to a methodology-floor F-image. Audit: `computations/_shared/_cross_pillar_bridge_audit.py::detect_element5_publication_precision_tolerance`. Calibration corpus: `sessions/framework/registry/cross-pillar-bridge-corpus.md §21`.

### Registry-Write Hygiene under Parallel-Writer Race

Registry-write helpers (next-N allocators, slot-allocation routines, append-only writers) MUST:

1. **Scan ALL header levels** before allocation — `## Header #N` + `### Header #N` + `#### Header #N`. A scan limited to one hash level under-counts existing slots and produces collision under parallel writers.
2. **Use append-only Python writers, not Edit-tool round-trips**, for shared-write registries. The Edit tool is mtime-conditional: when two agents both Read the file then Edit, the second Edit fails with mtime conflict. For the VERDICT FILE specifically, the canonical writer is the race-safe `emit_verdict` knowledge-MCP tool (single, lock-serialized writer; `gate-verdicts.md` §"Race-Safe Emission") — NOT a raw `open("a")` append, which is NOT atomic across processes on Windows (concurrent appenders lose lines). For other shared-write registries (`elimination-bulletins.md`, `permanent-results-registry.md`), use the single-shot `open("a")` append-helper pattern; where cross-process concurrency is possible, guard the append with a lockfile.
3. **Detect and document slot-rerouting in the producing script's verdict line**. When a planned slot is occupied at runtime, rerouting to next-free-letter is permitted, but the verdict line MUST emit FAIL-with-remediation (not PASS) so the rerouting is visible in the audit trail.

Failure to follow (1)-(2) produces collisions / mtime races; failure to follow (3) hides slot drift from downstream consumers and breaks audit provenance.

**Multi-slot pre-allocation**: when a single workshop produces multiple registry-landings whose slot-identity must remain non-colliding across waves, use a synchronization lockfile (canonical pattern: `sessions/framework/s87-slot-pre-allocation-lockfile.md`). Lockfile contains explicit RESERVED-FOR-WORKSHOP-{N}-W-{M} entries with cross-reference template for "Provenance" / "Sponsors" / "Anchor List" fields. Producing scripts reroute to the next-free-letter on runtime occupancy with FAIL-with-remediation in the verdict line.

### Quotient-functor pre-registration

When a candidate bridge theorem connects an ∞-dim spectral-action wall (Pillar-VII) and a finite-rank obstruction wall (Pillar-V or analogous), the plan MUST pre-register the quotient relation under which the bridge is claimed:

1. **Quotient-equivalence specification** — e.g., cyclic-fold pairing on N-conjunct categorical structure
2. **Rank-match check at the quotient level** — kernel/cokernel at quotient = finite-rank Pillar-V observable
3. **Explicit declaration of residual cokernel content** killed by the quotient

Bridges declared as full-functor isomorphisms when an ∞-dim ↔ finite-rank disparity exists are dimensional-impossibility-violating and must be re-classified as quotient-functor or rejected at plan-freeze.

### Forward-Backward Inference Closure on Substrate-Physics Manifolds

Every substrate-physics manifold M with prior-cite history admits an `fb_pair(M) = (forward(M), backward(M))` construction:

- `forward(M)` = derivation chain INTO M (which prior gates' outputs feed M's inputs)
- `backward(M)` = consumer chain OUT OF M (which downstream gates consume M's outputs)

Every gate landing on a substrate-physics manifold M MUST emit the `fb_pair(M)` skeleton in the gate block. Without it, plan-author validators cannot verify that all upstream/downstream consumers will remain consistent under the gate's verdict.

### Dual-prior pre-registration as track-discriminator

When a forward gate's outcome admits TWO substantively distinct interpretive tracks (e.g., "Reading_1: structural" vs "Reading_2: numerical-only"), the plan MUST pre-register a dual prior:

1. **Track A prior**: prior probability mass under interpretive Track A (with explicit ratio, e.g., 0.4 vs 0.6).
2. **Track B prior**: prior probability mass under Track B.
3. **Discriminator gate criterion**: gate's PASS/FAIL/INFO outcome maps to a specific posterior re-allocation between tracks (e.g., PASS → 0.9 to Track A; FAIL → 0.9 to Track B; INFO → unchanged).

Without it, the gate's outcome can be re-narrativized to fit either track at session-end synthesis (a violation of pre-registration discipline analogous to convention-shopping).

### Pole-Scope sub-clause (MANDATORY)

When a structural correlation is established at one Mellin-cone pole, the theorem text MUST scope the claim to **that pole** AND the plan MUST pre-register an anchor-formula for any pole-extension test:

1. **Pole-scoping declaration**: theorem text reads "structural correlation X holds at pole s=N" (NOT "in general").
2. **Pre-registered anchor-formula** for pole-extension: the producing script MUST cite the anchor-formula at plan-freeze time, NOT discover it during execution (PRU-Class-8 prevention).
3. **Discriminator predicate** between Reading_1 (generic pluralism: correlation holds at all poles) and Reading_2 (pole-specific: correlation localizes to one pole).

Pole-scoping enforcement is plan-halt-on-violation. Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §3`.

### Resolution-Specificity Scoping

When `|ρ_S| = 1.0` EXACT (or any other extremality value) is reported across an N-element class projection, the registry text MUST scope the claim to "the N-class projection" (not generic substrate-pluralism):

1. **N-element class declaration**: registry text reads "extremality value V holds across the N-class projection" with N explicitly named.
2. **Forward-extension caveat**: registry text MUST acknowledge that future regulator-atlas extensions (e.g., A_5 → A_6 by adding a sixth regulator) could in principle lower the extremality.
3. **Cross-link to atlas-cardinality canonical**: if the `canonical_constants.py` atlas-cardinality pin changes, the registry entry must be re-validated under the new N.

**Two-layer reading discipline**: when extremality `|ρ_S| = 1.0` is reported with empirical cross-regulator-class spread > 0 at the pole, the registry text MUST distinguish:

- **Layer 1 — Pole-universal F_2-class anti-correlation** (algebra-INVARIANT spectrum-only functional family).
- **Layer 2 — Pole-compressing cross-regulator atlas spread** (algebra-DEPENDENT state-pair-functional family).

The two layers are STRUCTURALLY ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. Conflating them is a Resolution-Specificity Scoping clause-1 violation; entries citing extremality at any N-class projection MUST tag whether the claim is Layer-1 (pole-universal) or Layer-2 (pole-specific) and report empirical spread when claiming Layer-2.

### Closing-Paragraph-Coherence Audit Pattern

For any rule-file section composed of (i) an enumerated antecedent list followed by (ii) a closing paragraph that disambiguates the rule's behavior at execution time, plan-freeze auditors MUST apply the closing-paragraph-coherence test:

1. **Identify the antecedent's two competing structural readings** — typically a literal-independent reading (each antecedent-clause is independently testable; closing paragraph is composition with a separately-stated companion rule) vs a strict-conjunctive reading (closing paragraph applies when ALL antecedent-clauses hold simultaneously).
2. **Test each reading against the closing paragraph's qualifying language** — substitute each reading into the closing paragraph and check whether it produces a self-contradiction (FORBIDDEN-AT-AUTHORING-TIME ∧ acceptable-AT-EXECUTION-TIME, etc.).
3. **Reject the reading that produces self-contradiction**; declare the structurally-coherent reading as canonical for the rule-as-authored.

When a rule's closing paragraph admits multiple readings, the structural fix is to compose the rule with explicit companion-rule citation rather than to leave the closing paragraph ambiguous.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §14`.

### Class 8.7 pattern extensions P3 + P4

When the Class 8.7 detector at `_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable()` extends beyond the inaugural pattern set, the detector MUST include the following two patterns:

- **Pattern P3 (substrate-distance-N pole residue-formula form)**: regex pattern `r'Res_\{s=0\}\s*s\^2\s*\*\s*Tr'` or `r'substrate-distance-2 pole.*residue-formula'` — detects plan-block text citing substrate-distance-N pole residue-formula evaluations where the residue formula reduces to direct sum at s=0 under finite cardinality of the spectral triple's spectrum.
- **Pattern P4 (Peter-Weyl per-block decomposition aggregate residue form)**: regex pattern `r'Peter-Weyl per-block.*aggregate'` OR `r'block-decomposition.*residue.*aggregate'` — detects plan-block text citing Peter-Weyl per-block decomposition aggregate residue evaluations where the per-block algebraic identity reduces to direct sum at the aggregate level.

**Rule-body framing**: the canonical Class 8.7 rule-body language reads **"finite-cardinality tautology under canonical Γ(s) on a finite spectral triple"** (NOT the generic "dimension-spectrum is degenerate" form, which mis-frames the substrate-IS pathology).

**False-positive disambiguator**: P3 + P4 regex patterns must NOT match the canonical FULL physical `_cm_1995_residue_formula.py` evaluator — that evaluator IS the substrate-natural disambiguator demonstrating the structural pathology source, not an instance of it.

**Self-test extension**: the `s90_w1_pru_class_8_7_test.py` self-test driver MUST cover synthetic positive (P3 + P4) AND synthetic negative (canonical FULL physical regulator citation) cases.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §"Class 8.7"`.

### Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until K=3)

When a gate's producing script computes an observable of the form `Tr(P · A) − R_CM` or `ζ_D(0)` (single-pole CM-1995 §III.4 residue-formula evaluation at a substrate-distance pole) on a finite spectral triple `(A, H, D)` whose dimension-spectrum is degenerate (multiple roots at the residue pole), the plan-block MUST pre-register a degeneracy-witness alongside the threshold:

1. **Coincident-root declaration**: explicit enumeration of which roots of the dimension-spectrum coincide at the residue pole the gate evaluates.
2. **Per-pole multiplicity**: integer multiplicity `m_p` at each pole the gate consumes (from Peter-Weyl block decomposition or analog spectral-decomposition basis).
3. **Compositional-corridor pin**: the specific `(d)∘(b)` (or analog) compositional corridor the gate uses to disambiguate the residue evaluation in the presence of degeneracy.

Without (1)-(3), a naive single-pole CM-1995 §III.4 evaluation discards the multiplicity structure and silently consumes the substrate-IS degeneracy without disclosure. The Class 8.7 detector at `_pru_cardinality_audit.py` scans plan-block text for the degenerate-observable detection patterns (`Tr(P_HSS) − R_CM` form; `value = ζ_D(0)` form) and emits S2 advisory severity when the patterns match AND no degeneracy-witness markers are declared.

Audit: `computations/_shared/_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable()`.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §"Class 8.7 Calibration Corpus"`.

## Source Reconciliation (Class 8.1)

PRU detects MISSING pins (cardinality test). SOURCE-RECONCILIATION detects PINNED-BUT-DRIFT pins (value test). The two audits commute by construction and are KEPT SEPARATE — pin-set cardinality and pin-value comparison are independent set operations. Run sequentially: PRU first (must clear before SOURCE-RECON runs); SOURCE-RECON second; gate execution third.

For every plan pin (`name = value`), the SOURCE-RECON sub-audit at plan-freeze:

1. queries `mcp__knowledge__.get_constant(name)` for the canonical value.
2. computes `d_i = |log10(pin) - log10(source)|`.
3. classifies the drift per the 6-class taxonomy (class (f) per `substrate-first-canonical-sourcing.md`):
   - **(a) PIN-TIGHT-SOURCE-LOOSE** — pin band tighter than canonical band.
   - **(b) PIN-LOOSE-SOURCE-TIGHT** — pin band wider than canonical band (highest-leverage class; FALSE-PASS direction).
   - **(c) PIN-DRIFT-FROM-STALE-SOURCE** — pin computed against a since-superseded canonical.
     - **(c.OOM-misread) sub-class**: stale-source values structurally OOM wrong (vs band-drift); D_max > 3.0 HARD-HALT band by construction.
   - **(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY** — pin is a derived form of a primary canonical.
   - **(e) PIN-PROMOTES-TO-CANONICAL-ON-PASS** — pin will become canonical on PASS (post-gate hook; canonical does not yet exist at plan-freeze).
   - **(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — pin given as textual approximation, OOM estimate, or placeholder string AND a substrate-first canonical exists. Detection patterns: `O(10^?-?\d+)`, `≈ ...`, `~ 10^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`. Conjunction with substrate-canonical existence test via `mcp__knowledge__.get_constant` or `mcp__knowledge__.search_knowledge`. Severity defaults to HARD-HALT at D_max ≥ 3.0. Full audit pattern + worked examples: `substrate-first-canonical-sourcing.md`.
4. assigns severity per the band calibration:
   - `D_max < 0.1` → no rule-file action.
   - `0.1 ≤ D_max < 1.0` → SOURCE-RECONCILIATION advisory (S2).
   - `1.0 ≤ D_max < 3.0` → SOURCE-RECONCILIATION MANDATORY (S1); halts plan-freeze.
   - `D_max ≥ 3.0` → hard plan-freeze halt; manual review required.
5. emits SOURCE-RECON advisory (S2) or MANDATORY-halt (S1) or hard-halt (≥3.0 OOM).

**Class-to-remediation table**:

- (a) → loosen pin to source band
- (b) → tighten pin or invoke source-structural-bound (FALSE-PASS direction; highest leverage)
- (c) → re-pin to current canonical; log drift in plan-revision history
- (d) → verify derivation chain; ratio check against source primitives; algebraic-equivalence audit at plan-authorship per Class 8.3 item 5 above
- (e) → LOG promotion event in `canonical_constants.py` provenance with `promoted_from = "S{N}-{gate}"`
- (f) → query `mcp__knowledge__.get_constant(name)` for canonical; substitute into plan PIN VALUE field; re-run SUBSTRATE-FIRST-PROVENANCE sub-audit (`substrate-first-canonical-sourcing.md`); PASS on canonical substitution. HARD-HALT remediation at D_max ≥ 3.0.

Class-(c) post-supersession-event extension (e.g., a literal threshold tested a hypothesis a Bulletin already disproved): see `regulator-pin-discipline.md`.

Class-(f) SCHEMATIC-helper-consumption sub-class: a producing script consumes a helper module whose docstring self-identifies as SCHEMATIC (e.g., `_spectral_action_regulators.py`) without disclosing the level in the verdict-line `convention=` field. Level pin discipline is MANDATORY at plan-freeze for all gates consuming SCHEMATIC helpers; full discipline at `substrate-first-canonical-sourcing.md §(iv)`. Calibration corpus: `sessions/framework/registry/pru-class-corpus.md §4`.

### PRU pipeline composition order

```
PRU (cardinality pre-flight)  →  SOURCE-RECON (value pre-flight)  →
SUBSTRATE-FIRST-PROVENANCE (source-existence)  →
DEFERRED-PENDING REGISTRY-ANATOMY (sub-class detection; S2 advisory)  →
PRDR (machinery enumeration)  →
gate execution  →  v3-recovery audit
```

The audit script is `computations/_shared/_source_reconciliation_audit.py`. Plan-freeze invokes it after `_pru_cardinality_audit.py`; failure routes to MANDATORY remediation per the 4-band calibration.

The **DEFERRED-PENDING REGISTRY-ANATOMY** stage invokes `computations/_shared/_cross_pillar_bridge_audit.py::detect_deferred_pending_sub_class(section_text, section_anchor)` on each §VII registry slot block. The detector returns `{deferred_pending: bool, sub_class: 'PROXY-REFINEMENT' | 'FIRST-EXTRACTION' | 'OPERATIONAL-ALIGNMENT' | 'BOTH' | 'NONE', severity: 'S2'|'NONE', ...}` per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`. Detection produces S2 advisory; does NOT route to plan-freeze HARD-HALT. The deferred-pending sub-class RESERVES the §VII slot during the pending refinement / extraction / operational-alignment window without contributing to registry-PASS by itself; downstream gates that consume a deferred-pending entry MUST cite the refinement-pathway forward-promoting gate per the anatomy rule's refinement-pathway table.

## Layer-Decomposition

The **layer-functor** `F: substrate → methodology → audit` links the substrate-physics layer to the methodology-floor layer (rule files, agent standards) to the audit-floor layer (verdict files, audit scripts, hooks).

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
| input-pin map        | `closure_hash(input_pin_map) = audit_sha256` |
| verdict-line artifact-SHA | `audit_sha256` (self-referential at audit layer) |
| orchestrator-direct-without-cross-actor | SHA-hardcoding bug (`v3-closure-recovery.md` sig_5) |

### Morita-equivalence framing

`F` preserves PRU-class invariants analogous to how `Mor_NCG` preserves K-theoretic invariants. A PRU Class-8.2 violation at the substrate layer (verifier-rubric pre-registration failure) maps under F to an analogous failure at the methodology layer (rule-file pre-registration failure) and at the audit layer (audit-line pre-registration failure). The class-8 sub-taxonomy (8.0/8.1/8.2/8.3) is preserved by F.

### Phi correspondence

The graded-ring-isomorphism Phi correspondence maps `weight(a_n^SD) = n` canonically to `weight(Σ_d) = enforcement-strength`:

```
Phi(a_0) = Σ_1   (perimeter / cosmological term, weight-0; user-adjudication-only deliverable)
Phi(a_2) = Σ_2   (Einstein-Hilbert kinematic skeleton, weight-2; wave-classification)
Phi(a_4) = Σ_3   (Yang-Mills + Higgs quartic load-bearing, weight-4; mcp-pre-check hook)
```

Higher weights extend by the same pattern: weight-n substrate-physics observable maps to enforcement-strength-n methodology rule.

K-counters and per-instance corpus for Layer-Decomposition sub-rules (definitional-datum-vs-derived-theorem, F(observable) vs F(trigger predicate) split): `sessions/framework/registry/pru-class-corpus.md §§9-10`.
