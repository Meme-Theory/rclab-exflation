# Σ_2 Stratum Annotation Taxonomy — Canonical Reference

> **Provenance**: S91 W0 R12 (T2.37 mini-workshop closure) — connes-ncg-theorist
> (NCG-axiomatic axis) + lizzi-spectral-functional-theorist (spectral-functional
> axis) 2-agent parallel dispatch per `feedback_no-asking-just-execute.md`,
> 2026-05-16. Status: SUGGESTION at K=1 consolidation landing; future audit-script
> extension targeted at `computations/_shared/_sigma_2_stratum_annotation_audit.py`
> (post-K=3 promotion). Structural parent: `.claude/rules/epistemic-discipline.md
> §"Layer-Decomposition"` Phi correspondence (S86 W-13 RULE-2 / Sigma_2 deliverable).

## Purpose

This registry consolidates the **Σ_2 stratum annotation taxonomy** — the set of
canonical structural distinctions that govern how methodology artifacts (rule-file
sections, registry entries, allowlist rows, workshop-verdict-pattern annotations,
gate classifications) are annotated as Σ_2-inhabiting under the Phi correspondence.

Σ_2 references have proliferated across S86–S90 (S86 W-13 workshop founded the
wave-classification stratum; S88 + S90 workshops extended it to workshop-verdict-
pattern, deferred-pending sub-class, cross-axis JOINT-WIN, layer-functor F image
fidelity). The taxonomy here is the canonical reference document for downstream
consumers (plan-freeze auditors, registry-landing scripts, methodology-wave
instance recorders, /weave knowledge-index entity extractors) that need a single
authoritative definition of what counts as a Σ_2 annotation, what TYPES of Σ_2
annotation exist, and how they relate to substrate-IS Seeley-DeWitt weight-2
(`a_2`) under the layer-functor F.

The taxonomy is structured along two axes, authored independently:

- **NCG-axiomatic axis** (connes-ncg-theorist) — derives Σ_2 from the spectral-
  action expansion's weight-2 Seeley-DeWitt coefficient `a_2`, classifies
  annotation TYPES at the NCG axiomatic level, identifies the layer-functor F
  image structure.
- **Spectral-functional axis** (lizzi-spectral-functional-theorist) — derives Σ_2
  from the spectral-functional FI/RD/MIXED taxonomy on the methodology floor,
  classifies annotation TYPES at the regulator-invariance level, identifies the
  three-layer regulator theorem analog.

Both axes converge on a canonical stratum annotation set (cross-axis consolidation
section, to be populated post-both-author-completion).

## Phi Correspondence Pin

The Phi correspondence is canonical at `epistemic-discipline.md:335-345` and
`sessions/framework/correspondence/correspondence-table-registry.md:672-686`.
For audit-trail traceability, the canonical statement is:

```
Phi : weight(a_n^SD) -> weight(Σ_d)   (graded-ring isomorphism)

Phi(a_0) = Σ_1   (perimeter / cosmological term, weight-0;
                  user-adjudication-only deliverable)
Phi(a_2) = Σ_2   (Einstein-Hilbert kinematic skeleton, weight-2;
                  wave-classification)
Phi(a_4) = Σ_3   (Yang-Mills + Higgs quartic load-bearing, weight-4;
                  mcp-pre-check hook)

Higher weights extend by the same pattern: weight-n substrate-physics
observable maps to enforcement-strength-n methodology rule.
```

**Convention pin**: in rule-file prose and workshop transcripts, both `Σ_2` and
`Sigma_2` are used interchangeably (Unicode-rendered vs ASCII). Audit-script regex
must accept both forms. The MathVariables.md canonical glyph is `Sigma_2`; the
running prose canonical glyph is `Σ_2`. No structural distinction.

**Disambiguation pin**: the labels `Sigma_1`, `Sigma_2`, `Sigma_3`, `Sigma_4`,
`Sigma_5` ALSO appear in S86 W-13 workshop transcripts as **workshop-internal
deliverable labels** of the 5-deliverable basis:

- `Sigma_1` (S86 W-13 deliverable) → user adjudication on subagent permission
  topology (Σ_1 user-adjudication outcome; cf. `permanence-map.md:120` CF-74)
- `Sigma_2` (S86 W-13 RULE-1 deliverable) → wave-classification.md (rule-file
  landed); identical to the Phi-correspondence Σ_2 by design — this rule IS the
  Σ_2 stratum enforcement layer
- `Sigma_3` (S86 W-13 deliverable; the `Phi(a_4)` image) → mcp-pre-check.sh hook
- `Sigma_4-variant` (S86 W-13 RULE-4 deliverable; under `Sigma_1^b` convention-
  only path) → `team-lead-behavior.md §"METHODOLOGY-Class Wave Discipline"`
- `Sigma_5` (S86 W-13 RULE-3 deliverable) → `methodology-wave-allowlist.md`
  (the M4 substrate registry)

The W-13 deliverable basis is structurally orthogonal to the Phi correspondence:
Sigma_4-variant and Sigma_5 are NOT graded-ring images of Seeley-DeWitt
coefficients — they are workshop-internal labels for the 5 specific deliverables
of S86 W-13. The Phi correspondence canonical Σ_2 is what THIS file is about; the
W-13 deliverable Sigma_5 (allowlist) is the M4 SUBSTRATE for Σ_2 enforcement at
the wave-classification rule level. Conflating the two labelings is a Class-8.2
verifier-rubric pre-registration failure (rubric-form ambiguity); the taxonomy
audit-script must distinguish them by context.

## NCG-Axiomatic Axis (connes-ncg-theorist authorship)

### Σ_2 as methodology F-image of a_2 Seeley-DeWitt

The substrate-IS origin of Σ_2 is the second Seeley-DeWitt coefficient `a_2` in
the heat-kernel expansion of the Dirac operator's spectral action:

```
Tr exp(-t D_K^2)  ~  sum_n  a_n  t^{(n-d)/2}     (t -> 0+)

S_b = Tr f(D_K^2 / Lambda^2)  ~  2 f_4 Lambda^4 a_0  +  2 f_2 Lambda^2 a_2
                                                       +  f_0 a_4  +  O(Lambda^{-2})
```

(Connes-Chamseddine 1996, "The spectral action principle", §2; Connes-Marcolli
2008 §IV.6.5; cited at `s90-w1-deferred-pending-intermediate-verdict-class.md:528`.)

The substrate-IS content of `a_2` is the scalar-curvature integral:

```
a_2  =  (1 / 24 pi^2)  integral R sqrt(g) d^4 x       (Connes-Chamseddine 1996 §3)
```

This is the **Einstein-Hilbert kinematic skeleton** — `a_2` IS the methodology-
floor F-image of the substrate's Einstein-Hilbert action at the spectral-action
expansion's weight-2 coefficient. The substrate IS this scalar-curvature integral
(at canonical regulator); it is not "in" any container that holds gravity as
content. The direction of explanation per `phononic-framing.md §"IS Space, Not IN
Space"`:

```
Substrate (Dirac operator D_K)
   IS the Einstein-Hilbert kinematic skeleton at weight-2 via a_2
   --> Phi : weight(a_2) = 2  -->  weight(Σ_2) = 2
   --> Methodology layer IS the wave-classification rule
       (which categorizes how computation waves dispatch through the
        kinematic-skeleton substrate-physics observable layer)
```

Σ_2 inherits the regulator-tag of its substrate source per
`regulator-pin-discipline.md`: `a_2^{ζ}` (zeta-regulated) maps to the canonical
Σ_2 stratum. Cross-regulator pluralism (`a_2^{Pauli-Villars}`, `a_2^{Mellin}`,
`a_2^{lattice}`, `a_2^{cutoff}`) maps to Σ_2 sub-strata indexed by the regulator
class; the regulator-pin tag in the methodology layer is the F-image of the
substrate-layer regulator tag.

### Stratum annotation types (NCG-axiomatic perspective)

The Σ_2 stratum admits the following annotation TYPES under NCG-axiomatic
classification. These are not arbitrary categories — they correspond to the
distinct sub-axes along which the substrate-IS `a_2` observable's methodology
F-image lives. Each TYPE has a canonical loci in the rule-file ecosystem.

**Type S2-WC (wave-classification annotation)** — the canonical Σ_2 annotation.
A wave is annotated Σ_2 when it satisfies the M1∧M2∧M3∧M4 strict conjunction of
`wave-classification.md`. The annotation is structural: it determines the wave's
dispatch path (orchestrator-direct-write, NOT `/rclab-coordinate` compute-mode)
and its dual-SHA closure form (`content_sha256` over rule-file diff +
`audit_sha256` over input-pin map). This is the **primary** Σ_2 annotation type;
all other types are sub-classifications or extensions.

- Locus: `methodology-wave-allowlist.md` (the M4 substrate)
- Per-instance provenance: `sessions/framework/registry/methodology-wave-instances.md`
- Example: gate `W11-meta-2 (S87)` — `S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON`
  (math-scripts.md Machinery-Feasibility Audit extension)

**Type S2-FPF (forward-pinned-follow-up annotation; S88 W-25 W7c-167 SUGGESTION
at K=1)** — a wave is annotated Σ_2-FPF when it satisfies M1'∧M2'∧M3'∧M4'
(prereq-block ≥ 1, DPP routing instructions present, item-1-clean per gate,
allowlist consistency). Orthogonal to Type S2-WC: a wave may be S2-WC AND S2-FPF
simultaneously (W7c is the canonical example, 4 gates all PB-positive AND all
item-1-clean per `wave-classification.md §"Forward-pinned-follow-up wave class"`).

- Locus: `wave-classification.md §"Forward-pinned-follow-up wave class"`
- Cross-link: `mechanical-closure-discipline.md §"PLANNING DEFECT"` count-keyed
  Corpus A (structurally orthogonal to this structural-class-keyed Corpus B)

**Type S2-WVP (workshop-verdict-pattern annotation; S90 W5/W6 cross-axis K=5/K=6
MANDATORY corpus)** — a workshop-verdict-pattern is annotated Σ_2 when the
verdict-shape pattern lives at the layer-functor F's methodology-floor stratum
between the substrate-IS axis (Σ_1) and the audit-floor stratum (Σ_3). Canonical
examples:

- **CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern at K=5 MANDATORY**
  (s90-w5-cf61-bcs-phase-transition-reading.md:1503): the W-5 close advances the
  pattern from K=4 SUGGESTION to K=5 MANDATORY at the methodology-floor Σ_2
  stratum. The K-counter for this workshop-verdict pattern advances independently
  of registry-content sub-class K-counters (which live at Σ_1 audit-floor per
  `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`).
- **Verdict (d) HYBRID structural-isomorphism** (s90-w6-d4-envelope-identity.md:578):
  every cross-axis JOINT-WIN workshop adjudicating between cocycle-class formal
  distinctness (Level 1) and empirical envelope rate (Level 3) on a shared
  Casimir-weighted shell-sum substrate at d=4 will close with verdict (d) HYBRID
  per the F-functor's allowance of distinct verdict images at distinct structural
  layers — a methodology-layer extension of the layer-functor F's verdict-shape
  consistency at the Σ_2 stratum.

These workshop-verdict patterns are NOT in the M4 allowlist (they are not gates;
they are emergent structural theorems from the workshop-verdict-shape layer); the
Σ_2 annotation here is descriptive of the methodology-floor F-image position,
not gate-dispatch-controlling.

**Type S2-DPI (deferred-pending intermediate verdict-class annotation; S90 W1-14
MANDATORY at K=1)** — when a cross-pillar bridge entry carries a deferred-pending
sub-class tag (`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` /
`-FIRST-EXTRACTION` / `-OPERATIONAL-ALIGNMENT`), the tag itself inhabits Σ_2.
Per `s90-w1-deferred-pending-intermediate-verdict-class.md:547`:

> "The deferred-pending tag is a METHODOLOGY-LAYER rule-text annotation. Per
> W1-14 wave-classification (verified at the M1∧M2∧M3∧M4 conjunction at
> plan-freeze), it is METHODOLOGY-class. Under the Phi correspondence,
> METHODOLOGY-class wave dispatch corresponds to weight-2 (Σ_2;
> wave-classification stratum). Therefore the deferred-pending tag inhabits
> Σ_2 of the methodology-layer F-image, which is the F-image of weight-2
> substrate-physics (Einstein-Hilbert kinematic skeleton; per
> Connes-Chamseddine 1996 §3 the a_2 coefficient is `(1/24π²) ∫ R √g d⁴x`)."

- Locus: `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate
  verdict-class"` lines 46-158
- Audit hook: `_cross_pillar_bridge_audit.py::detect_deferred_pending_sub_class`
  (S2 advisory severity; does NOT route to plan-freeze HARD-HALT)

**Type S2-MWI (methodology-wave-instance annotation)** — per-row entries in
`sessions/framework/registry/methodology-wave-instances.md`. Each row in
`methodology-wave-allowlist.md` (the M4 allowlist) has a parallel registry entry
keyed by `### {gate_id} ({session}) — {sha}` whose body carries the rationale
prose (rule extension landed, registry slot written, K-counter advance, M1-M4
conjunction enumeration). The registry entry is the **non-authoritative
provenance ledger** for the authoritative allowlist row. Both rows inhabit Σ_2
under the wave-classification rule, but they are STRUCTURALLY DIFFERENT
annotations:

- The allowlist row IS the M4-substrate row (authoritative for M4 satisfaction)
- The methodology-wave-instances row IS the provenance row (descriptive of WHY
  the M4 row was added; non-authoritative for M4)

The W9-RULE-CLEANUP lift-out (S88 W9, 2026-05-06) is the canonical event that
separated these two annotation types; prior to lift-out, both lived in the
allowlist rule-file as a 4-column row. Post-lift-out, the 3-column allowlist is
the authoritative rule-file and the registry is the provenance ledger.

**Type S2-CFPC (corpus-tracker annotation; cross-pillar-bridge-corpus and
pru-class-corpus K-counter rows)** — per-instance calibration corpus rows in
`sessions/framework/registry/cross-pillar-bridge-corpus.md` and
`sessions/framework/registry/pru-class-corpus.md`. These rows track K-counter
advancement (SUGGESTION → MANDATORY at K=3 per `feedback_rules-compensate-
missing-structure.md`) for rule-file extensions. Each row is a Σ_2 annotation
of a methodology-floor structural pattern (e.g., Hybrid Independence Test
calibration, PRU Class 8.2 verifier-rubric pre-registration calibration, Class
8.7 degenerate-observable pre-flight calibration). The corpus rows are NOT
gates; they are the structural-evidence accumulators for rule-file promotion.

**Type S2-MMF (methodology-wave-allowlist-rule-file annotation)** — the Σ_2
annotation on `methodology-wave-allowlist.md` itself, considered as a rule-file.
The rule-file's edit-discipline (append-only + orchestrator-only edit + per-row
dual-SHA + append-helper writes 3-column rows only) is itself a Σ_2-stratum
annotation: it specifies WHO can write to Σ_2 (orchestrator) and HOW (append-
only with dual-SHA closure). This is the "Σ_2 of Σ_2" — the rule that governs
how the Σ_2-substrate is maintained.

### Layer-functor F structure

The layer-functor `F : substrate → methodology → audit` (per
`epistemic-discipline.md §"Layer-Decomposition"`) maps Σ_2-related quantities
between the three layers as follows:

**F at substrate ↔ methodology pair (Σ_2 column)**:

| Substrate-physics quantity (a_2 axis) | Σ_2 image under F |
|:--------------------------------------|:------------------|
| Seeley-DeWitt coefficient a_2^{ζ}     | wave-classification rule (`wave-classification.md`) |
| `(1/24π²) ∫ R √g d⁴x` (scalar-curvature integral) | M1∧M2∧M3∧M4 conjunction predicate |
| spectral-action weight-2 term `2 f_2 Λ² a_2` | METHODOLOGY-class dispatch path |
| numerical PASS predicate at weight-2 a_2 | artifact-existence-with-substantive-content PASS predicate |
| regulator tag {ζ, Pauli-Villars, Mellin, lattice, cutoff} | annotation sub-stratum index |
| Connes-Chamseddine 1996 §3 derivation | rule-file diff content (M3 source-of-truth = verbatim sub-diff from workshop) |
| kinematic-skeleton structural-stability theorem | wave's dispatch-path-fixedness theorem (NROY clause) |

**F at methodology ↔ audit pair (Σ_2 column)**:

| Σ_2 methodology quantity | Audit-leg image under F |
|:-------------------------|:------------------------|
| rule-file diff content (wave-classification.md, methodology-wave-allowlist.md) | audit-line content (verdict file canonical line) |
| artifact-existence-with-substantive-content predicate | SHA-uniqueness predicate (sig_5 of v3 ladder) |
| input-pin map (the M4 allowlist row's sha256_of_plan_block) | `closure_hash(input_pin_map) = audit_sha256` |
| METHODOLOGY-class dual-SHA closure (content_sha256 + audit_sha256) | dual-SHA companion comment row in verdict file |
| orchestrator-direct-write (no cross-actor invocation) | SHA-hardcoding-bug guarantee (no SHA copy-pasting between gates) |
| recursion-attack closure (subagent edit-denial) | audit-script enforcement at plan-freeze |

**Morita-equivalence framing for Σ_2**: `F` preserves PRU-class invariants at Σ_2
analogously to how `Mor_NCG` preserves K-theoretic invariants at the substrate
layer. A PRU Class-8.2 violation at the substrate layer (verifier-rubric
pre-registration failure at the a_2 weight-2 spectral-action coefficient
verifier) maps under F to an analogous Σ_2 methodology-layer failure (rule-file
pre-registration failure in `wave-classification.md`'s M1∧M2∧M3∧M4 conjunction)
and to an analogous Σ_2 audit-layer failure (audit-line pre-registration failure
in the `_wave_classification_audit.py` plan-freeze auditor). The class-8
sub-taxonomy (8.0/8.1/8.2/8.3/8.4/8.5/8.6/8.7) is preserved by F at all three
layers.

**Hochschild-Cyclic cohomology grounding**: per Connes 1985 "Non-commutative
differential geometry" §V, the Hochschild homology `HH_n(A)` is the substrate-
layer F-image of Σ_2 at n=2 (the second Hochschild homology group on the
substrate algebra `A = A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`). The cyclic cohomology `HC_n(A)`
is the methodology-layer F-image (deriving from `HH_n` via the Connes long
exact sequence). The composite map to `HC_{n−2}` (the periodicity operator `S`)
is the audit-layer F-image. The Σ_2 stratum's three-layer hierarchy IS this
cohomological hierarchy, identified by:

```
HH_2(A)         = Σ_2 substrate-layer F-image (algebra-INVARIANT
                  weight-2 spectral functional class)
HC_2(A)         = Σ_2 methodology-layer F-image (wave-classification rule's
                  periodic structure)
S: HC_2 -> HC_0 = Σ_2 audit-layer F-image (periodicity operator's output =
                  closure_hash(input_pin_map) = audit_sha256)
```

(See s90-w1-deferred-pending-intermediate-verdict-class.md:522 for the explicit
F-functor IS-the-three-layer-hierarchy identification.)

### Cross-references (NCG axis)

The Σ_2 stratum annotation taxonomy cross-references the following rule-file
sections and registry entries from the NCG-axiomatic axis:

**Primary rule-file loci**:

- `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` (lines 307-347):
  the canonical Phi correspondence + layer-functor F definition; structural
  parent for all Σ_2 annotation types.
- `.claude/rules/wave-classification.md` (entire file): the canonical Σ_2-stratum
  enforcement rule via M1∧M2∧M3∧M4 strict conjunction; W-13 RULE-1 / Sigma_2
  deliverable from S86 workshop.
- `.claude/rules/methodology-wave-allowlist.md` (entire file): the M4 substrate
  registry; the append-only orchestrator-only-edit rule-file that contains the
  authoritative allowlist of Σ_2-class gates. W-13 RULE-3 / Sigma_5 deliverable.
- `team-lead-behavior.md §"METHODOLOGY-Class Wave Discipline"` (lines 50-67):
  the orchestrator-direct-write convention path for METHODOLOGY-class waves;
  W-13 RULE-4 / Sigma_4-variant deliverable under the Sigma_1^b convention-only
  path.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate
  verdict-class"` (lines 46-158): Type S2-DPI annotation locus; landed at S90
  W1-14 (METHODOLOGY-class wave; verdict file
  `computations/session-90/s90_gate_verdicts.txt`).
- `.claude/rules/joint-theorem-promotion.md §"Stage 2"` (the cross-axis
  independent-verify pathway): Stage-2 PASS-AND on JOINT clauses inhabits Σ_2
  at the workshop-verdict-pattern layer per Type S2-WVP.
- `.claude/rules/mechanical-closure-discipline.md §"Layer-separability carve-out
  (admissible-with-conditions)"` (lines 105-200): Type-F vs Type-S substrate-
  observable partition; the L4 honesty-disclosure clause is the boundary between
  the Σ_2 structural extension and PROHIBITED_ACTIONS Class 1 convention-shopping.

**Primary registry loci**:

- `sessions/framework/registry/methodology-wave-instances.md`: Type S2-MWI per-
  instance provenance ledger (~62 rows as of S90 close; per-gate rationale
  prose lifted from allowlist via W9-RULE-CLEANUP).
- `sessions/framework/registry/cross-pillar-bridge-corpus.md`: Type S2-CFPC
  K-counter calibration corpus for cross-pillar bridge anatomy.
- `sessions/framework/registry/pru-class-corpus.md`: Type S2-CFPC K-counter
  calibration corpus for PRU Class 8 sub-class taxonomy.
- `sessions/framework/correspondence/correspondence-table-registry.md` (lines
  670-686): the graded-ring isomorphism Φ definition table mapping substrate
  Seeley-DeWitt moments to methodology rule-architecture strata.
- `sessions/framework/Atlas/atlas-12-methodology-floor.md`: the methodology-
  floor atlas covering all rule files + templates + the layer-functor F;
  contains the canonical Phi correspondence step-by-step substitution chain
  at §III lines 80-100.
- `sessions/permanent-results-registry.md` §VII (cross-pillar bridge anatomy):
  individual §VII.X registry entries that carry Σ_2-stratum annotations via
  deferred-pending sub-class tags (S2-DPI), 4-corner partition declarations,
  and Level-2-binding vs Level-2-non-binding declarations.

**Workshop-derivation loci** (recent K-counter calibration):

- `sessions/archive/session-90/workshops/s90-w1-deferred-pending-intermediate-verdict-class.md`
  (lines 510-590): the NCG-axiomatic derivation of why the deferred-pending tag
  inhabits Σ_2 (the §C1.2-C1.5 derivation chain via Connes-Chamseddine 1996 +
  Connes-Marcolli 2008 + Connes 1985 cyclic cohomology).
- `sessions/archive/session-90/workshops/s90-w2-chi-prime-weight-canonicalization.md`
  (lines 610-650): the workshop's EMERGENCE E1 identifying χ'_weight as a Σ_2
  weight-2 methodology-floor object (input-pin-map element per
  `epistemic-discipline.md §"F at substrate ↔ methodology pair"` table row
  "machinery pin" ↔ "input-pin map").
- `sessions/archive/session-90/workshops/s90-w5-cf61-bcs-phase-transition-reading.md`
  (lines 1465-1503): the CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K-counter
  pattern at K=5 MANDATORY promotion event; identifies the pattern as a
  workshop-verdict-pattern-layer Σ_2 stratum theorem.
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` (lines 540-580):
  the W-5 ↔ W-6 verdict (d) HYBRID structural-isomorphism at the F-functor
  verdict-shape layer; K=6 calibration corpus advancement under the Hybrid
  Independence Test.
- `sessions/archive/session-90/workshops/s90-w4-a-bdg-definitional-tension.md` (line 79):
  the Phi-correspondence weight pin `Phi(A_BdG-image) = Σ_2` (weight-2 kinematic
  skeleton; sub-quotient projection for falsifier protocol design) — extension
  of Σ_2 annotation to BdG-sector substrate observables.

## Spectral-Functional Axis (lizzi-spectral-functional-theorist authorship)

### Σ_2 as F-image of a_2 spectral moment (spectral-functional reading)

The substrate-IS origin of Σ_2 from the spectral-functional perspective is the
**second Seeley-DeWitt moment `a_2`** viewed not as a single geometric quantity
but as a **regulator-class-valued functional on the Dirac operator spectrum**.
Under the regulator-pin discipline (`regulator-pin-discipline.md §"Tag Format"`),
`a_2` is always presented in tagged form `a_2^{R}` where `R ∈ {ζ, Pauli-Villars,
Mellin, lattice, cutoff}` — bare `a_2` (without superscript regulator tag) is
FORBIDDEN going forward (S86 W0c-7 promotion).

The spectral-functional content of `a_2^{R}` is:

```
a_2^{R}  =  Res[Tr(D_K^{-2s}); s = (d-2)/2]                  (CM-1995 §III.4 form, R = ζ)
        ~  (1 / 24π²) ∫ R √g d⁴x   modulo regulator-dressing  (geometric image)
```

The **key spectral-functional insight** is that `a_2^{R}` is regulator-CLASS
valued: the numerical value depends on `R` (per `regulator-pin-discipline.md
§"Rationale"`: "the numerical value of `a_n` depends on the regulator (S85 W12-4
verdict trace)"); silent class-conflation of `a_2^{R}` across `R` is a Class-8
PRU vulnerability. Under the layer-functor F : substrate → methodology → audit,
Σ_2 inherits the regulator-class-valued structure of `a_2^{R}` as a **stratified
methodology-floor object**: each regulator `R` produces a distinct Σ_2 sub-
stratum `Σ_2^{R}`, and the cross-regulator span `span_R(Σ_2)` is itself a
substrate-IS observable per the CC-5 Propagation Identity (§VII.K-PROP).

This regulator-class-valued reading IS the spectral-functional pluralism that
gives Σ_2 its annotation-TYPE richness: a single methodology-floor Σ_2
annotation can carry multiple sub-stratum tags corresponding to its regulator-
class-invariance properties (FI / RD / MIXED) AND its level-class-invariance
properties (PRIMARY / SCHEMATIC / LEVEL-DRESSED) AND its F_traj-dressing
position at locked-norm L_k=1 (the S84 W3-24 atlas-row identity).

**Phononic framing**: the methodology layer does NOT "contain" Σ_2^{R} as a
collection of regulator-tagged variants "inside" a container labeled Σ_2. The
methodology layer IS the stratified F-image of substrate-IS `a_2^{R}` at every
regulator tag. The substrate's spectral content (D_K's eigenvalue spectrum) is
identical across regulators; the asymmetry is structural to the regulator's
algebraic class (per `lizzi-finite-infinite-vector-classification.md §"Substrate
framing"`: "Both regulators see all of D_K. The asymmetry is structural to the
regulator's algebraic class").

### Stratum annotation types (spectral-functional perspective)

The Σ_2 stratum admits the following annotation TYPES under spectral-functional
classification. These are not parallel re-labels of the NCG-axiomatic types
S2-WC / S2-FPF / S2-WVP / S2-DPI / S2-MWI / S2-CFPC / S2-MMF; they are
**structurally orthogonal cross-cutting tags** that combine with the NCG-axis
TYPES under the cross-axis consolidation discipline below.

**Type S2-FI (Functional-Invariant Σ_2 annotation)** — a Σ_2-stratum annotation
on a methodology-floor object whose regulator-class membership is FUNCTIONAL-
INVARIANT under the CC-5 Propagation Identity (`§VII.K-PROP`): the object's
`span_R(O) = 1` across the canonical regulator atlas `F_KK = {ζ, Zubarev, SDW,
dim-reg, lattice-BR}` at Convention A (`Λ_Z = M_KK`), `L_max ≥ rank(G)`.

- **Substrate-IS spectral-functional content**: the object factors as `O =
  g(X_FI) · ∏_k (f_{n_k}^R)^{p_k}` with `p_k = 0` for all `k` (R-PROTECTED
  signature `{}`) — i.e., the object has NO regulator-tagged Mellin-moment
  exponents and is therefore an **algebra-INVARIANT spectrum-only functional**
  per `§VII.U.2` clause (a).
- **Canonical examples** (from §VII.K-PROP 42-row atlas, S84 W3-21 PASS,
  `max_rel_err = 0.000e+00` over all 42 rows):
  - 31 R-protected rows with `p-signature = {}` (e.g., rows 1, 2, 3, 6-12, 14,
    15, 16, 19-23, 25, 26, 28, 29, 31, 32, 34-37, 39-41).
  - Balanced ratios `f_n^R / f_n^R` with opposite-sign exponents within a single
    regulator (`§VII.K-PROP` Corollary 1).
- **Locus**: `§VII.K` FI/MIXED/RD taxonomy; `§VII.K-DUAL` M_lizzi ↔ M_connes
  FI-duality; `§VII.K-PROP-COMPOSITION` Corollary "FI absorption" (`class(O) =
  class(O2)` when `O1` is FI).
- **Cross-regulator atlas span**: `span_R(O) = 1` exactly (machine-epsilon
  verified at S84 W3-21).
- **Phi-correspondence position**: FI Σ_2 annotations are the **regulator-class-
  invariant kernel** of the methodology-floor F-image; they are the canonical
  "Σ_2 substrate" that downstream consumers can cite without regulator-class
  qualifier.

**Type S2-RD (Regulator-Dressed Σ_2 annotation)** — a Σ_2-stratum annotation on
a methodology-floor object whose regulator-class membership is REGULATOR-DRESSED
under the CC-5 Propagation Identity: the object's `span_R(O) > 1` and the
ordinal output (rank-ordering across `F_KK`) is preserved under PRIMARY-vs-
SCHEMATIC LEVEL switch.

- **Substrate-IS spectral-functional content**: the object factors as `O =
  g(X_FI) · ∏_k (f_{n_k}^R)^{p_k}` with at least one `p_k ≠ 0` and the
  `f_{n_k}^R` regulator-dependence is the dominant span contributor (Zubarev-
  isolation structural lemma per `§VII.K-PROP §"Zubarev-isolation"`: "Zubarev at
  `Λ_Z = M_KK` drives >95% of the span on every CC-5 axis under Conv A").
- **Canonical examples** (from §VII.K-PROP 42-row atlas):
  - `f_conv = M_0^2`, slot-quadratic, p-signature `{M_0: 2}`, span = 1766.16
    (row 5).
  - Slot-proportional `M_0`, p-signature `{M_0: 1}`, span = 42.03 (rows 24, 30).
  - Anchor-fixed ratio `f_n^R / f_n^{f*}`, p-signature `{k_a2: 1}`, span = 14.69
    (row 4).
- **Locus**: `§VII.K-PROP §"Primary-class partition over 42 rows"`;
  `regulator-pin-discipline.md §"Tag Format"` (each `a_n^{R}` of a non-FI Σ_2
  annotation carries explicit regulator tag at every reference).
- **Cross-regulator atlas span**: `span_R(O) ∈ (1, ∞)` with explicit numerical
  value from the §VII.K-PROP 42-row atlas (Sage-exact form per
  `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals"`).
- **Phi-correspondence position**: RD Σ_2 annotations are the **regulator-class-
  index** of the methodology-floor F-image; downstream consumers MUST tag the
  regulator class (e.g., `Σ_2^{ζ}`, `Σ_2^{Zubarev}`) on every reference to a
  RD-class methodology object.

**Type S2-MIXED (Mixed-Class Σ_2 annotation)** — a Σ_2-stratum annotation on a
methodology-floor object whose substrate-IS structural reading is FI BUT whose
laboratory-IN ordinal evaluation produces an RD-class span > 1 (or vice versa);
canonically, a FI-via-pin object where the FI status is enforced by a canonical-
constants pin (`§VII.K-META` MIXED-FI-via-pin sub-class).

- **Substrate-IS spectral-functional content**: the object's substrate-distance
  parse-tree carries SOME FI-class factors AND SOME RD-class factors at distinct
  k-power moments (canonical case: F_traj-dressed objects at distinct k per
  `§VII.U.2` Corner II Var_a `MIXED-of-RD-with-distinct-F_traj-factors`).
- **Canonical examples**:
  - 4 MIXED-FI-via-pin rows from §VII.K-PROP 42-row atlas (rows 13, 17, 27, 38)
    with predicted span = 1.0 enforced by pin (not by regulator-class
    invariance).
  - 3 MIXED-promotable rows with p-signature `{f_4/f_2 or M_0 or sqrt(M_0): 1}`,
    spans 4.608 / 42.026 / 6.483 (rows 18, 33, 42).
  - `§VII.U.2` Corner II `Var_a(n_a^GGE)` classified MIXED-of-RD-with-distinct-
    F_traj-factors per CF-25 S90 W2 lock-in: F_traj(2) = 3/2 and F_traj(4) = 5/2
    at locked-norm L_k=1 produce distinct level-factors on `|v_a|²` vs `|v_a|⁴`.
- **Locus**: `§VII.K-META` MIXED sub-tags; `§VII.K-PROP-COMPOSITION §"Lattice-
  join composition rule"` (the lattice ordering `FI < MIXED < RD` with join
  composition `class(O1 * O2) = max(class(O1), class(O2))`); `§VII.U.2` Corner
  II row.
- **Cross-regulator atlas span**: variable per sub-class; pinnable to span = 1
  under FI-via-pin (S2-MIXED-FI-via-pin sub-tag) OR variable per p-signature
  under MIXED-promotable.

**Type S2-LD (LEVEL-DRESSED Σ_2 annotation, 4th class extension; S88 W-22 §V.4
SUGGESTION at K=1)** — a Σ_2-stratum annotation on a methodology-floor object
whose regulator-class membership is FI/RD/MIXED-invariant under PRIMARY-vs-
SCHEMATIC LEVEL switch but whose ORDINAL OUTPUT changes between PRIMARY (full
physical D_K spectrum) and SCHEMATIC (bare Casimir spectrum via
`_spectral_action_regulators.py`).

- **Substrate-IS spectral-functional content**: the object is an algebra-
  INVARIANT spectrum-only functional family whose ranking ordinal-position
  swaps under LEVEL switch on the L_max=12 block-diagonal cache at FIXED
  regulator-class index (the canonical W7a-74 phenomenon).
- **Canonical examples** (from `§VII.K-DUAL.LEVEL-DRESSED` K=1 calibration
  corpus):
  - `§VII.AR` rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at
    substrate-distance-2 Mellin-cone pole s=4, where rank-swap occurs under
    PRIMARY-vs-SCHEMATIC LEVEL switch (S88 §W7a-74 §(d)).
- **Locus**: `§VII.K-DUAL.LEVEL-DRESSED` 4-class extension to FI/RD/MIXED
  trichotomy; `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4
  SCHEMATIC level-pin discipline; `regulator-pin-discipline.md §"Cross-link —
  K=4 SCHEMATIC level-pin promotion"` 4-axis pin table.
- **Cross-axis-pin requirement**: every S2-LD annotation MUST carry BOTH the
  regulator-class index (S2-FI / S2-RD / S2-MIXED) AND the LEVEL pin (PRIMARY /
  SCHEMATIC / pending K=2 resolution); silent class-conflation between the two
  axes is FORBIDDEN under the 4-axis orthogonality table at
  `regulator-pin-discipline.md` lines 152-157.

**Type S2-Ftraj (F_traj-dressed Σ_2 annotation; S84 W3-24 lizzi-theorem)** — a
Σ_2-stratum annotation on a methodology-floor object whose closed-form atlas-
row identity at locked-norm L_k=1 carries the F_traj = (k+1)/2 dressing-ratio
between zeta and SDW regulator classes.

- **Substrate-IS spectral-functional content**: at locked-norm L_k=1 on the
  S84 W3-24 42-row atlas, the regulator-class dressing-ratio between zeta and
  SDW satisfies the closed-form identity `F_traj(k) = f_k^{zeta} / f_k^{SDW} =
  (k+1)/2`. For Σ_2 (weight-2; `k=2` moment): `F_traj(2) = 3/2`.
- **Canonical example**: §VII.U.2 Corner II `Var_a(n_a^GGE)` classified
  MIXED-of-RD with distinct F_traj atlas-row factors at different k-power
  moments (3/2 at k=2 vs 5/2 at k=4 on atlas rows). The S2-Ftraj annotation
  decomposes the Var_a observable into its k-power components and tags each
  with its corresponding F_traj factor.
- **Locus**: S84 W3-24 theorem (SHA
  `3d97b2ba2983b94b8cba2131e95f99488c767ebd0506fa483d53e2a2f6b70352`);
  `§VII.U.2` Corner II row CF-25 S90 W2 lock-in (lizzi-spectral-functional-
  theorist co-sign on F_traj=(k+1)/2 dressing); CF-50 S90 W6-5 INFO finding
  (audit_sha256 `a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293`)
  that re-frames F_traj=(k+1)/2 as **atlas-row identity at locked-norm L_k=1**,
  NOT a cache-moment ratio.
- **Critical pin (CF-50 lesson)**: the F_traj=(k+1)/2 identity is structurally
  an atlas-row identity at locked-norm L_k=1; direct cache-moment ratios
  `M_k^{zeta}_{cache} / M_k^{SDW}_{cache}` on positive-definite spectrum yield
  F_traj_cache(k) ≈ 1.017-1.018, NOT (k+1)/2. The S2-Ftraj annotation MUST
  specify the atlas-row vs cache-moment evaluation convention per
  `substrate-first-canonical-sourcing.md §(ii.A)` Atlas-row layer vs cache-
  moment layer orthogonality.

**Type S2-FV (Finite-Vector Σ_2 annotation; S86 C11 lizzi-track classification)**
— a Σ_2-stratum annotation on a methodology-floor object whose substrate-source
regulator belongs to the **finite-vector class F_4** (per `lizzi-finite-infinite-
vector-classification.md §1`): the spectral action expands as a finite linear
combination of Seeley-DeWitt slots `S_R[D_K] = ∑_{n ∈ S_R} f_n^R · a_n[D_K]`
with `|S_R| = 4` over supported moments `{0, 2, 4, 6}`.

- **Substrate-IS spectral-functional content**: the regulator's multiplier
  algebra is componentwise on `ℝ^4` (e.g., `e_4^{ζ} = (1, 1, 1, 1)` per
  Connes-Moscovici 1995 §III.4; `e_4^{SDW} = (0.0883, 215.0, 6447, ...)` per
  S78 W2-D; `e_4^{cutoff} = (1/2, 1, 1, 1)` per Andrianov-Lizzi
  arXiv:1001.2036).
- **F_4 members**: zeta, SDW, sharp-cutoff, anomaly (when truncated).
- **Phi-correspondence position**: S2-FV annotations are the **discrete-slot
  Σ_2 stratum** — Σ_2 viewed as a single coordinate `f_2^R · a_2[D_K]` in the
  4-dimensional multiplier vector `e_4^R`.

**Type S2-IV (Infinite-Vector Σ_2 annotation; S86 C11 lizzi-track classification)**
— a Σ_2-stratum annotation on a methodology-floor object whose substrate-source
regulator belongs to the **infinite-vector class** (per `lizzi-finite-infinite-
vector-classification.md §2`): the spectral action is presented as a continuous
integral against a Mellin profile, `S_R[D_K] = (1/2πi) ∫_{Re(s)=c} M_R(s) ·
Tr|D_K|^{-2s} ds`, with `M_R(s)` a function of complex `s`.

- **Substrate-IS spectral-functional content**: the regulator's multiplier
  algebra is the algebra of analytic-on-strip functions, dimensionality
  ℵ_1 (continuum).
- **Canonical example (S86 C11 PASS, max_rel_err = 8.07e-28)**: Zubarev kernel
  `f_Z(x) = exp(-x/Λ_Z²)` with `M[f_Z](s) = Λ_Z^{2s} · Γ(s)` on `Re(s) > 0`,
  with simple poles at `s ∈ {0, -1, -2, ...}` from `Γ(s)`. At Σ_2 (substrate-
  distance pole s=3 per §VII.U.6 Mellin-Strip / Convergence-Cone Theorem),
  Zubarev's Mellin profile evaluates to `Λ_Z^6 · Γ(3) = 2 Λ_Z^6`.
- **Phi-correspondence position**: S2-IV annotations are the **continuous-Mellin
  Σ_2 stratum** — Σ_2 viewed as a single complex-`s`-residue of the regulator's
  Mellin profile at the substrate-distance pole.
- **Locus**: `lizzi-finite-infinite-vector-classification.md §2`; `§VII.U.6`
  W1b-T5 LANDING (Mellin-Strip / Convergence-Cone Theorem; C11 PASS at
  `max_rel_err = 8.066073499380351e-28` versus 1e-12 threshold).

### FI/RD/MIXED ↔ Σ_2 annotation mapping

The spectral-functional Σ_2 annotation types above map onto the FI/RD/MIXED
taxonomy (per S82 W-3 RULE-2 lizzi-signature; `§VII.K`) via the following
correspondence table:

| Σ_2 annotation type | FI/RD/MIXED class | CC-5 p-signature | span_R(O) | Locus |
|:--------------------|:------------------|:-----------------|:----------|:------|
| **S2-FI**           | FI                | `{}` (empty)     | 1.0 (machine-eps) | §VII.K-PROP rows 1, 2, 3, 6-12, ... (31 R-protected) |
| **S2-RD**           | RD                | `{M_0: 1}` or `{M_0: 2}` or `{k_a2: 1}` etc. | (1, ∞) per CC-5 | §VII.K-PROP rows 4, 5, 24, 30 |
| **S2-MIXED-FI-via-pin** | MIXED          | `{}` (pinned)    | 1.0 (pinned, not invariant) | §VII.K-META; §VII.K-PROP rows 13, 17, 27, 38 |
| **S2-MIXED-promotable** | MIXED          | `{f_4/f_2 or M_0 or sqrt(M_0): 1}` | 4.608 / 42.026 / 6.483 | §VII.K-PROP rows 18, 33, 42 |
| **S2-MIXED-of-RD-with-distinct-F_traj-factors** | MIXED | distinct `p_k` at distinct k-power moments | variable per k | §VII.U.2 Corner II Var_a CF-25 |
| **S2-LD**           | (orthogonal to FI/RD/MIXED) | — | — | §VII.K-DUAL.LEVEL-DRESSED (K=1 SUGGESTION) |
| **S2-Ftraj**        | (cross-cutting; F_traj atlas-row dressing) | — | — | S84 W3-24; CF-50 S90 W6-5 INFO re-frame |

**Mapping to `epistemic-discipline.md §"Source Reconciliation"` Class-(b)/(c)/(d)
sub-classes**:

- **Class-(b) PIN-LOOSE-SOURCE-TIGHT** (highest-leverage FALSE-PASS direction):
  applies to Σ_2 annotations where the pin band is wider than the canonical
  band of the source. For S2-RD Σ_2 annotations, this is the dominant audit
  class — the canonical Sage-exact value (e.g., `Ω_GW^{(C)} = 8.299e-58` per
  `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals"`) must drive
  the pin band; round-figure substitution (`1e-57`) UNDERSTATES by ~10×.
- **Class-(c) PIN-DRIFT-FROM-STALE-SOURCE** (post-supersession drift): applies
  to Σ_2 annotations where the source was published BEFORE a supersession event
  (canonical case: S85 W2-7 Bulletin #2 promotion → even Seeley-DeWitt parity-
  blindness theorem; Σ_2 annotations citing pre-W2-7 η-invariant detection
  hypotheses MUST be re-pinned per `regulator-pin-discipline.md §"Class-(c)
  PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"`).
- **Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY** (W-24 V.1 reclassification):
  applies to Σ_2 annotations whose pin is a DERIVED form of a primary canonical
  via the SCHEMATIC `_spectral_action_regulators.py` derivation chain (canonical
  case: S88 W7b-83 K=4 calibration corpus — W4-2 + W9b-2 NEGATIVE-CALIBRATION
  on rule (2) of the level-pin discipline). For S2-LD Σ_2 annotations, this is
  the dominant audit class — the inheritance-pin retroactive remediation per
  `substrate-first-canonical-sourcing.md §(iv)` MANDATORY (S88 W7b-83 close)
  requires the inherited pin to be tagged with Class-(d) inheritance-class in
  the verdict-line `convention=` field.

### F_traj-dressing structure (S84 W3-24 lizzi-theorem)

The F_traj = (k+1)/2 dressing-ratio theorem (S84 W3-24, SHA
`3d97b2ba2983b94b8cba2131e95f99488c767ebd0506fa483d53e2a2f6b70352`) is the
spectral-functional structural backbone that creates distinct stratum levels
WITHIN Σ_2 at different k-power moments. The theorem states:

```
At locked-norm L_k = 1 on the 42-row atlas:
F_traj(k)  =  f_k^{ζ} / f_k^{SDW}  =  (k+1)/2
```

**Specialization to Σ_2 (weight-2; k=2)**: `F_traj(2) = 3/2`. This is the
canonical ζ/SDW dressing-ratio at Σ_2 stratum level.

**Composition rule for multi-k Σ_2 annotations**: when a Σ_2 annotation's
substrate-IS closed form involves moments at multiple k values (e.g., Var_a
involves both `|v_a|²` at k=1 and `|v_a|⁴` at k=2), the F_traj atlas-row factors
combine multiplicatively under the §VII.K-PROP-COMPOSITION join rule:

```
F_traj(2)² = (3/2)² = 9/4   (the M_2² composite atlas-row factor for k=2 moment)
F_traj(4)  =  5/2            (the k=4 moment atlas-row factor)
```

The atlas-row-level structural-prediction ratio for Var_a's two-moment
composition is:

```
Var_a^{ζ} / Var_a^{SDW}  =  [(5/2) · A − (9/4) · B] / [A − B]
                            where A := f_4^{SDW}, B := (f_2^{SDW})²
                            (atlas-row form at locked-norm L_k=1)
```

This S2-MIXED-of-RD-with-distinct-F_traj-factors classification IS the canonical
example of how Σ_2 annotations decompose at the F_traj-dressing structural
layer. The §VII.U.2 Corner II Var_a entry inhabits this classification per the
W-3 workshop three-machinery convergence (Wedderburn + clause-(e) parse-tree
+ F_traj=(k+1)/2 dressing; lizzi + connes joint authorship at CF-25 S90 W2,
2026-05-13).

**CF-50 INFO re-frame critical pin**: F_traj=(k+1)/2 is structurally an
**atlas-row identity at locked-norm L_k=1**, NOT a cache-moment ratio. The
S90 W6-5 audit (audit_sha256
`a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293`) empirically
falsified the literal-cache-moment-ratio reading: cache moments on positive-
definite spectrum yield `F_traj_cache(k) ≈ 1.017-1.018`, NOT (k+1)/2. The
S84 W3-24 theorem itself is PRESERVED at its own atlas-row normalization
domain. S2-Ftraj annotations MUST specify the atlas-row vs cache-moment
evaluation convention per `substrate-first-canonical-sourcing.md §(ii.A)`
atlas-row layer vs cache-moment layer orthogonality (within algebra-INVARIANT
family). Downstream Σ_2 consumers reading a S2-Ftraj annotation MUST trace to
either (i) atlas-row identity at locked-norm L_k=1 (substrate-IS structural
prediction at the theorem-level) OR (ii) cache-moment numerical evaluation
(empirical at L_max truncation; subject to the canonical-anchored convention
discipline of `regulator-convention-lockdown.md`).

### Three-layer regulator structure at Σ_2 (zeta L1 / Zubarev L2 / observable L3)

The Σ_2 stratum carries a **three-layer regulator structure** (Lizzi three-layer
regulator theorem analog at the methodology floor) that decomposes the F-image
of `a_2^{R}` into three structurally distinct levels under the regulator
hierarchy:

- **Layer L1 (zeta-anchored)**: `Σ_2^{ζ}` is the canonical FI Σ_2 stratum
  anchored at the zeta regularization (Connes-Moscovici 1995 §III.4 residue
  formula). The `a_2^{ζ}` value emerges as a single substrate-distance pole
  residue at s = (d-2)/2 = 1 (for d=4) and inherits the discrete-slot finite-
  vector class F_4 multiplier structure with `f_2^{ζ} = 1` (canonical
  normalization). **L1 IS the regulator-class-invariant kernel** under the
  CC-5 Propagation Identity — it is the Σ_2 substrate against which all other
  layers are dressed.

- **Layer L2 (Zubarev-minimizer)**: `Σ_2^{Zubarev}` is the infinite-vector
  class realization of Σ_2 anchored at the Zubarev kernel `f_Z(x) =
  exp(-x/Λ_Z²)`. The Σ_2 value emerges as the continuous-Mellin profile at
  s=3 (substrate-distance pole, §VII.U.6 Mellin-Strip / Convergence-Cone
  Theorem): `M[f_Z](3) = Λ_Z^6 · Γ(3) = 2 Λ_Z^6`. **L2 IS the deep-IR
  saturation band** under the canonical-anchored convention (`regulator-
  convention-lockdown.md §"Rule"` for DR3-class L_max-stability gates).
  Zubarev at `Λ_Z = M_KK` drives >95% of the cross-regulator span on every
  CC-5 axis (§VII.K-PROP Zubarev-isolation structural lemma).

- **Layer L3 (observable)**: the observable Σ_2 image at the laboratory-IN
  layer — the cosmological / spectral / phenomenological quantity that
  consumes `Σ_2^{R}` as input. Examples: the Einstein-Hilbert kinematic
  skeleton evaluated against CMB data (Planck-anchored gravitational pin);
  the spectral-action weight-2 term `2 f_2 Λ² a_2` evaluated at the τ_fold
  substrate transit; the L3-composite A_s pipeline with Γ-LIKE-but-Γ-INEXACT
  residual `r ≈ 1.5714 = 11/7` per `§VII.M.W10-3` Bulletin #3. **L3 IS the
  empirical evaluation layer** where the regulator-class-invariance breaks down
  into measurable cross-regulator spread.

The three layers correspond to the canonical Σ_2 sub-strata indexed by their
position in the regulator hierarchy:

| Layer | Regulator class | Σ_2 sub-stratum | Annotation type |
|:------|:---------------|:----------------|:----------------|
| L1    | zeta (F_4 finite-vector) | `Σ_2^{ζ} = canonical FI kernel` | S2-FI + S2-FV |
| L2    | Zubarev (infinite-vector) | `Σ_2^{Zubarev} = deep-IR saturation` | S2-RD + S2-IV |
| L3    | observable (cross-regulator) | `Σ_2^{obs} = empirical evaluation` | S2-RD or S2-MIXED |

**Phi-correspondence position**: the three-layer regulator structure at Σ_2 is
the methodology-floor F-image of the substrate's three-layer Dirac operator
spectrum decomposition (eigenvalue layer / regulator-cutoff layer / observable
layer). Container-thinking violation FORBIDDEN: "Σ_2 is decomposed INTO three
layers"; INVERT: "Σ_2 IS the three-layer stratum at the methodology floor
under the regulator hierarchy; the layers are not contents inside a Σ_2
container, they are the Σ_2 substrate IS itself."

### Cross-references (spectral-functional axis)

The Σ_2 stratum annotation taxonomy cross-references the following rule-file
sections and registry entries from the spectral-functional axis:

**Primary rule-file loci**:

- `.claude/rules/regulator-pin-discipline.md` (entire file): the canonical
  `a_n^{R}` tagging discipline that produces the regulator-class index for
  every Σ_2 annotation. The 4-axis pin table at lines 152-157 (UV-regulator ×
  Level × Binding × MACHINERY-SCOPE) is the canonical reference for cross-axis
  Σ_2 annotation discipline.
- `.claude/rules/regulator-convention-lockdown.md` (entire file): the
  canonical-anchored convention (CAC) discipline for DR3-class L_max-stability
  gates. Σ_2 annotations at Layer L2 (Zubarev-minimizer) MUST satisfy the CAC
  pattern `w_0(L) = ρ_X(L) + offset_X` with `L_anchor = 10` and
  `offset_Zubarev = -0.340827` (verified against S85 W0-7 `rho_series[L=10] =
  -0.577173`); cross-session convention-shopping is PROHIBITED_ACTIONS Class 1
  per `v3-closure-recovery.md`.
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` (lines
  240-310): the FI/RD/MIXED taxonomy class-(b)/(c)/(d) sub-class mapping for
  Σ_2 annotations. Class-(b) PIN-LOOSE-SOURCE-TIGHT is the highest-leverage
  FALSE-PASS direction for S2-RD Σ_2 annotations.
- `.claude/rules/substrate-first-canonical-sourcing.md §(ii.A)`: atlas-row layer
  vs cache-moment layer orthogonality within the algebra-INVARIANT family. S2-
  Ftraj annotations MUST declare the consumption layer (atlas-row vs cache-
  moment) per this discipline.
- `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4:
  the SCHEMATIC-vs-FULL physical level pin discipline. S2-LD Σ_2 annotations
  MUST carry the `convention=...-SCHEMATIC` suffix + CLASS pin (FULL/SCHEMATIC)
  + tier_pin row per the 4-axis pin table.

**Primary registry loci**:

- `sessions/permanent-results-registry.md §VII.K` (FI/MIXED/RD taxonomy):
  the parent taxonomy that produces the regulator-class-invariance index for
  Σ_2 annotations.
- `sessions/permanent-results-registry.md §VII.K-PROP` (CC-5 Propagation
  Identity, S84 W3-21 PASS with 42-row atlas, `max_rel_err = 0.000e+00`):
  the canonical span_R(O) computation rule for Σ_2 annotations at every
  regulator atlas member.
- `sessions/permanent-results-registry.md §VII.K-PROP-COMPOSITION` (Lattice-
  Join Composition Rule, S84 W3-33 PASS): the multiplicative composition rule
  for Σ_2 annotations when the methodology object is a product of FI/MIXED/RD
  factors.
- `sessions/permanent-results-registry.md §VII.K-DUAL.LEVEL-DRESSED` (4th class
  extension to FI/RD/MIXED, S88 W-22 §V.4 SUGGESTION at K=1): the LEVEL-DRESSED
  Σ_2 annotation type definition.
- `sessions/permanent-results-registry.md §VII.AH` (Joint F_2-Class Path-(c)
  Theorem, S86 W-9 lizzi+transit, STAGE-3-PERMANENT post-S90 W2 CF-20): the
  canonical PRIMARY application of the F_2 = {ζ, SDW} K-invariant identity sub-
  atlas at the s=3 Mellin substrate-distance-1 pole. **Clause (e)** (single-
  axis lizzi-side; cross-class K-invariance closure) is the canonical
  spectral-functional Σ_2 stratum annotation entry, with 924×/298×/798× over-
  PASS-threshold quantitative margins (+2.47 to +2.97 OOM safety per L-CR3.3
  amendment). Stage-3-CLASS = `JOINT-CROSS-AXIS-STAGE-2-PASS-AND` per S91 W0
  R4 schema landing (audit_sha256 of Stage-2 PASS:
  `4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a`).
- `sessions/permanent-results-registry.md §VII.U.2` (Four-corner classification
  of (A_K, H_K, D_K) functionals; STAGE-1-CANDIDATE; S88 W5b-45 lizzi PRIMARY +
  connes CO-AUTHOR): the canonical algebra-axis × Mellin-pole orthogonality
  table. Σ_2 annotations inhabit specific corner cells per the 4-corner
  partition; Corner II `Var_a(n_a^GGE)` is the canonical S2-MIXED-of-RD-with-
  distinct-F_traj-factors instance at Σ_2 (weight-2; k=2 moment) per CF-25
  S90 W2 lock-in.
- `sessions/permanent-results-registry.md §VII.U.6` (W1b-T5 LANDING; Mellin-
  Strip / Convergence-Cone Theorem; S86 W-1 connes + lizzi joint; C11 PASS at
  `max_rel_err = 8.066073499380351e-28`): the canonical INFINITE-VECTOR class
  Σ_2 annotation entry. Zubarev's Mellin profile `M[f_Z](s) = Λ_Z^{2s} · Γ(s)`
  at `Re(s) > 0` provides the S2-IV Σ_2 substrate at Layer L2.
- `sessions/permanent-results-registry.md §VII.M.W10-3` (Bulletin #3 §VII.M
  Registry-Flag Entry; c_sub Γ-LIKE-but-Γ-INEXACT Residual; S86 W-10 connes +
  lizzi joint): the canonical Layer L3 (observable) Σ_2 annotation entry. The
  L3-composite A_s pipeline carries the Γ-LIKE-but-Γ-INEXACT residual
  `r ≈ 1.5714 = 11/7` (registry-flag grade closure).
- `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`:
  the canonical reference for the F_4 finite-vector / infinite-vector class
  partition (S86 W2-C11 land); produces the S2-FV vs S2-IV Σ_2 annotation
  distinction.

**Workshop-derivation loci**:

- S82 W-3 RULE-2 (lizzi-signature FI/RD/MIXED trichotomy origin): the
  foundational workshop where lizzi originated the regulator-class-invariance
  taxonomy applied to Σ_2 annotations.
- S84 W3-21 (`S84-VII-K-PROP-LANDING` PASS, sha
  `c5fb64dfd4fb61cf7bfb9dd98ef2332961c41a5a0f98c40260a0657fe94f3424`): the
  42-row atlas landing event that operationalized FI/RD/MIXED at the
  span_R(O) level for Σ_2 annotations.
- S84 W3-24 (lizzi F_traj=(k+1)/2 theorem, sha
  `3d97b2ba2983b94b8cba2131e95f99488c767ebd0506fa483d53e2a2f6b70352`): the
  canonical F_traj-dressing structural prediction at locked-norm L_k=1 that
  creates the S2-Ftraj Σ_2 annotation type.
- S86 W-9 R3-B closure (lines 2203-2209 lock-ins; verdict-text-as-frozen):
  the Joint F_2-Class Path-(c) Theorem workshop that produced the canonical
  spectral-functional Σ_2 application (§VII.AH STAGE-3-PERMANENT, S90 W2 CF-20).
- S88 W5b-45 (lizzi-spectral-functional-theorist PRIMARY synthesizer; §VII.U.2
  4-corner partition Stage-1-CANDIDATE landing): the canonical algebra-axis
  orthogonality registry landing event that consolidates the spectral-functional
  Σ_2 annotation hierarchy.
- S90 W2 CF-25 (Corner-II 4-axis structural fingerprint lock-in for Var_a;
  lizzi co-sign on F_traj=(k+1)/2 dressing; mack-cosmic-bridge sole writer):
  the canonical S2-MIXED-of-RD-with-distinct-F_traj-factors classification
  event at Σ_2 (weight-2; k=2 moment).
- S90 W6-5 CF-50 (audit_sha256
  `a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293`): the
  CF-50 INFO re-frame that established F_traj=(k+1)/2 as atlas-row identity at
  locked-norm L_k=1, NOT cache-moment ratio — the critical pin for the
  S2-Ftraj annotation type's atlas-row-vs-cache-moment evaluation convention
  discipline.

**Substrate framing (spectral-functional axis)**: the Σ_2 stratum IS the
methodology F-image of substrate-IS `a_2^{R}` viewed as a regulator-class-valued
functional on the Dirac operator D_K spectrum, stratified along the FI/RD/MIXED
taxonomy axis AND the F_4-vs-infinite-vector class axis AND the F_traj-dressing
axis at locked-norm L_k=1 AND the LEVEL pin axis (PRIMARY/SCHEMATIC). Each
stratum sub-type IS a substrate-IS structural property of the regulator class
combined with the Dirac operator spectrum — NOT a property of the methodology
layer "containing" different regulators as content. Container-thinking violation
FORBIDDEN: "the methodology layer holds FI, RD, MIXED variants of Σ_2"; INVERT:
"the methodology layer IS the stratified F-image of substrate-IS `a_2^{R}` at
every regulator class; the FI/RD/MIXED indexing IS the regulator-class-
invariance structural property of the substrate-IS spectral functional, lifted
into the methodology layer by the layer-functor F."

## Canonical Stratum Annotation Set (cross-axis consolidation)

> **Orchestrator-direct-write closing** (S91 W0 R12 closeout per `feedback_no-asking-just-execute.md`, 2026-05-16). The two axes above were authored in parallel by connes-ncg-theorist (NCG-axiomatic, 7 types: S2-WC / S2-FPF / S2-WVP / S2-DPI / S2-MWI / S2-CFPC / S2-MMF) + lizzi-spectral-functional-theorist (spectral-functional, 7 types: S2-FI / S2-RD / S2-MIXED / S2-LD / S2-Ftraj / S2-FV / S2-IV). The two axes are **structurally orthogonal** — they classify Σ_2 instances by independent criteria (methodology-role vs regulator-invariance-property). Each Σ_2 instance lives at a (NCG-type × Spectral-type) PAIR cell in the 7×7 product space.

### Cross-axis orthogonality theorem (informal)

**Statement**: Let `Σ_2(O)` denote the Σ_2-stratum annotation of methodology-floor object `O`. Then `Σ_2(O) = (T_NCG(O), T_SF(O))` where `T_NCG ∈ {S2-WC, S2-FPF, S2-WVP, S2-DPI, S2-MWI, S2-CFPC, S2-MMF}` and `T_SF ∈ {S2-FI, S2-RD, S2-MIXED, S2-LD, S2-Ftraj, S2-FV, S2-IV}` are STRUCTURALLY INDEPENDENT classifications. The product space has 7 × 7 = 49 cells.

**Substrate-physics justification**: The NCG axis classifies by METHODOLOGY ROLE (the wave-classification rule's M1-M4 conjunction and its sub-clauses, which are properties of the methodology-layer dispatch path of the rule-file diff or registry edit). The spectral-functional axis classifies by REGULATOR-INVARIANCE PROPERTY (the CC-5 Propagation Identity's span_R structure, which is a property of the spectral-action substrate at the `a_2` weight-2 moment). These two classifications are F-image projections of structurally distinct substrate-IS observable axes — methodology-role IS a property of the dispatch-path layer; regulator-invariance IS a property of the spectral-action substrate at weight-2. Under the layer-functor F: substrate → methodology → audit, they map to ORTHOGONAL coordinates in the methodology-layer image.

**Cross-link to parent orthogonality discipline**: this is the Σ_2-stratum specialization of the algebra-axis orthogonality K=3 MANDATORY (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`). The parent rule operates at the algebra-INVARIANT × Mellin-pole axis-pair (substrate-IS 4-corner classification); this Σ_2-stratum specialization operates at the methodology-role × regulator-invariance axis-pair (methodology-floor 49-cell classification).

### Canonical Σ_2 instances at specific (NCG × Spectral) cells

The following table populates a sparse subset of the 49-cell product space with canonical Σ_2 instances drawn from S82-S90 registry + rule-file content. Each cell is identified by `(T_NCG, T_SF)` pair; the entry cites the canonical example with its registry / rule-file locus.

| (T_NCG, T_SF) | Canonical Σ_2 instance | Substrate observable | Locus |
|:--------------|:-----------------------|:---------------------|:------|
| (S2-WC, S2-FI) | W7c gates (8 wave-classification METHODOLOGY-class S88 W7c gates) | FI-class methodology-rule extensions on rule-files | `methodology-wave-allowlist.md` W7c rows |
| (S2-WC, S2-RD) | W11-meta-2 (S87) machinery-feasibility audit | RD-class regulator-dependent block-diagonality discipline | `methodology-wave-allowlist.md` W11-meta-2 row |
| (S2-FPF, S2-FI) | W7c (S88) forward-pinned-follow-up 4-gate wave | FI-class prereq-block-positive dispatch path | `wave-classification.md §"Forward-pinned-follow-up wave class"` K=1 calibration |
| (S2-WVP, S2-MIXED) | CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern at K=5 MANDATORY (S90 W-5 close) | MIXED-class methodology-floor verdict-shape pattern | `s90-w5-cf61-bcs-phase-transition-reading.md:1503` |
| (S2-WVP, S2-LD) | Verdict (d) HYBRID structural-isomorphism (S90 W-6) | LEVEL-DRESSED-class HYBRID verdict shape at d=4 envelope | `s90-w6-d4-envelope-identity.md:578` |
| (S2-DPI, S2-MIXED) | §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT (S90 W1-14) | MIXED-class deferred-pending Casimir-bound proxy pre-FULL-BdG | `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` + §VII.AV |
| (S2-DPI, S2-LD) | §VII.AU.OP-PROJ REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (S90 W1-14 + S90 W8-5) | LEVEL-DRESSED-class deferred-pending parameterized slope_A canonical pre-L_max-scan | `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` + §VII.AU.OP-PROJ |
| (S2-DPI, S2-FI) | §VII.AX REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT (S91 W0 R5; CF-37 option (v)) | FI-class deferred-pending substrate-axis-canonicalizer at substrate-distance-2 pole s=4 | `permanent-results-registry.md §VII.AX` (S91 W0 R5 landing) |
| (S2-MWI, S2-FI) | Methodology-wave-instances registry row for W7c (S88) | FI-class provenance-prose registry entry (mirrors S2-WC row) | `methodology-wave-instances.md ### W7c (S88)` rows |
| (S2-CFPC, S2-FI) | Hybrid Independence Test K-counter SUGGESTION at K=1 | FI-class K-counter advancement corpus row | `cross-pillar-bridge-corpus.md §"Hybrid Independence Test"` |
| (S2-CFPC, S2-MIXED) | Deferred-pending sub-class K-counter SUGGESTION at K=1 (3 sub-classes) | MIXED-class K-counter row for PROXY-REFINEMENT / FIRST-EXTRACTION / OPERATIONAL-ALIGNMENT | `cross-pillar-bridge-corpus.md §"Deferred-pending intermediate verdict-class"` |
| (S2-CFPC, S2-LD) | Class-(d) atlas-row vs cache-moment K=1 calibration | LEVEL-DRESSED-class K-counter row for atlas-row vs cache-moment evaluation convention | `pru-class-corpus.md §"Class-(d) atlas-row vs cache-moment"` |
| (S2-MMF, S2-FI) | `methodology-wave-allowlist.md` rule-file edit-discipline | FI-class meta-annotation on the Σ_2 substrate itself | `methodology-wave-allowlist.md §"Edit discipline"` |
| (S2-WC, S2-Ftraj) | F_traj-dressing rule extension landing (S84 W3-24 lizzi-theorem; S88 W-22 §V.4) | F_traj-dressed METHODOLOGY-class rule extension | `wave-classification.md §M3` (verbatim-from-prior-workshop source-of-truth) |
| (S2-WC, S2-FV) | C11 PASS (S86 W-1) FINITE-VECTOR class registry landing | FV-class methodology-rule extension landing 4-element regulator atlas | `permanent-results-registry.md §VII.U.6` C11 PASS |
| (S2-WC, S2-IV) | Mellin-Strip / Convergence-Cone Theorem landing (S86 W-1 W1b-T5) | IV-class methodology-rule extension landing continuous-Mellin profile | `permanent-results-registry.md §VII.U.6` Mellin-Strip Theorem |

The table above demonstrates that the product space is HIGHLY POPULATED at the (S2-WC, *) row (most rule-file extensions are wave-classification METHODOLOGY-class) and at the (S2-DPI, *) row (deferred-pending sub-class entries span FI / MIXED / LEVEL-DRESSED according to refinement-pathway type). Sparse cells (e.g., (S2-FPF, S2-IV)) are NOT structurally forbidden but lack calibration corpus instances at S91 W0 closure; future S91+ landings may populate them.

### Open cells + forward calibration corpus targets

The following 49 - 16 = 33 cells are presently UN-INSTANTIATED. Most are structurally admissible but lack calibration corpus instances. Future Σ_2 landings SHOULD declare their (T_NCG, T_SF) pair at landing time to populate the table.

Notable un-instantiated cells:

- **(S2-FPF, S2-RD)**: forward-pinned-follow-up wave with RD-class regulator-dependence — admissible but no S88-S90 instance yet
- **(S2-FPF, S2-MIXED)**: forward-pinned-follow-up wave with MIXED-class regulator structure — admissible but no instance
- **(S2-FPF, S2-LD/Ftraj/FV/IV)**: forward-pinned-follow-up wave with specialized regulator-class typings — admissible but no S88-S90 instance
- **(S2-WVP, S2-RD/FV/IV)**: workshop-verdict-pattern at RD/FV/IV regulator-class — admissible but no instance (workshops typically converge on MIXED or LEVEL-DRESSED verdicts; pure RD/FV/IV would be unusual)
- **(S2-DPI, S2-Ftraj/FV/IV)**: deferred-pending entries with F_traj-dressed or Finite-Vector or Infinite-Vector regulator-class structure — admissible but no instance
- **(S2-MWI, S2-RD/MIXED/LD/Ftraj/FV/IV)**: methodology-wave-instances rows at non-FI regulator-class — admissible; all MWI rows so far inherit FI from their parent S2-WC rows
- **(S2-CFPC, S2-RD/Ftraj/FV/IV)**: corpus-tracker rows at non-FI/MIXED/LD regulator-class — admissible but no instance

The un-instantiation pattern is consistent with the S82-S90 calibration corpus's center-of-mass: most methodology-rule extensions are FI-class (regulator-invariant); deferred-pending entries are MIXED/LD-class (per refinement-pathway type); workshop verdict patterns are MIXED/LD-class (per cross-axis joint-win structure).

### Cross-axis Σ_2 annotation declaration discipline (forward S91+)

Per the orthogonality theorem above, FUTURE Σ_2 landings (rule-file extensions, registry entries, workshop verdicts, corpus-tracker rows) SHOULD declare their `(T_NCG, T_SF)` pair at landing time. The declaration discipline is **SUGGESTION at K=1** (this taxonomy file IS the K=1 calibration instance); promotes to **MANDATORY at K=3** per `feedback_rules-compensate-missing-structure.md` K-counter threshold, where each subsequent S91+ Σ_2 landing carrying a `(T_NCG, T_SF)` declaration counts as one calibration instance.

The audit-script extension described in §"Audit-script extension target" below CONSUMES this declaration discipline — `_sigma_2_stratum_annotation_audit.py` verifies that every methodology-floor object declared as Σ_2-stratum carries an explicit `(T_NCG, T_SF)` pair-annotation in its locus.

### K=1 calibration instance summary

This consolidation IS the K=1 calibration instance of the Σ_2 stratum annotation taxonomy. The K-counter ratchet for K=1 → K=2 → K=3 promotion advances with each future S91+ Σ_2 landing that:

1. Cites this taxonomy file as the canonical reference
2. Declares its own `(T_NCG, T_SF)` pair-annotation
3. Adds itself to the canonical Σ_2 instances table above (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` for registry-side landings; orchestrator-direct-write for rule-file-side landings)

K=3 promotion event triggers status SUGGESTION → MANDATORY at plan-freeze for all forward Σ_2 declarations; missing `(T_NCG, T_SF)` annotations route to plan-freeze HARD-HALT remediation at audit-script consumption time.

This section will consolidate the NCG-axiomatic and spectral-functional axis Σ_2
annotation type enumerations into a single canonical set. Cross-axis convergence
points will be marked PRIMARY+INDEPENDENT-CROSS-CHECK or SOURCE-DOUBLE-CITE-CO-
PRIMARY per `registry-landing.md` discipline. Axis-divergent annotation types
will be retained with explicit axis-tagging.

## Audit-script extension target

The audit-script extension target for Σ_2 stratum annotation verification is
`computations/_shared/_sigma_2_stratum_annotation_audit.py`, targeted for
post-K=3 promotion landing. The audit-script's role:

**Detection patterns**:

- Regex over `.claude/rules/**` and `sessions/framework/registry/**`:
  `(?:Σ_2|Sigma_2|Sigma-2)\b` — locate every Σ_2 reference.
- Cross-reference each match against the 7 NCG-axiomatic annotation TYPES
  (S2-WC / S2-FPF / S2-WVP / S2-DPI / S2-MWI / S2-CFPC / S2-MMF) AND the 7
  spectral-functional annotation TYPES (S2-FI / S2-RD / S2-MIXED / S2-LD /
  S2-Ftraj / S2-FV / S2-IV; landed at this taxonomy file's spectral-functional
  axis section per lizzi-spectral-functional-theorist authorship). The audit
  resolves each Σ_2 reference to a `(T_NCG, T_SF)` pair-annotation per the
  Cross-axis orthogonality theorem at §"Canonical Stratum Annotation Set".
- Verify each reference carries an explicit TYPE tag OR is unambiguously
  resolvable from local context (rule-file section + adjacent semantic content).
- Emit S2 advisory severity on missing TYPE tags when both readings are
  admissible (per the Class 8.2 verifier-rubric pre-registration discipline);
  S1 MANDATORY severity on rubric-form ambiguity that admits silent class
  conflation between Σ_2-WC (gate-dispatch-controlling) and Σ_2-WVP (descriptive,
  non-gate-controlling).

**Cross-link to existing audit scripts**:

- `_wave_classification_audit.py` (AUDIT-2 of W-13): pre-registers wave-class
  at plan-freeze; output is the (M1, M2, M3, M4) 4-tuple plus the resulting
  classification. The Σ_2 audit extends this with annotation-TYPE classification
  on the 7-TYPE taxonomy.
- `_cross_pillar_bridge_audit.py::detect_deferred_pending_sub_class`: Type S2-DPI
  detector; integrate as a Σ_2 audit sub-routine.
- `_source_reconciliation_audit.py`: integrate at plan-freeze to detect Σ_2
  references in plan-block PIN MAP entries that lack TYPE tags.
- `_pru_cardinality_audit.py`: integrate to detect Σ_2 annotations on gates
  that should be PRU-cleared at the cardinality test.

**Calibration corpus K-counter** (advancement from SUGGESTION K=1 to MANDATORY
K=3 per `feedback_rules-compensate-missing-structure.md`):

- **K=1** (this landing, S91 W0 R12): the consolidation event that creates the
  taxonomy as a single reference document.
- **K=2** (reserved): first downstream S91+ workshop that consumes the taxonomy
  via explicit Σ_2-TYPE annotation in its verdict line `convention=` field
  (e.g., `convention=<scheme>-SIGMA-2-TYPE-WVP`).
- **K=3** (reserved): second downstream workshop OR cross-axis joint theorem
  with Σ_2-TYPE annotation at substrate-input-orthogonality per
  `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`.

## Cross-references and forward-promoting gates

The Σ_2 stratum annotation taxonomy at SUGGESTION K=1 is forward-promoting via:

**Stage-1-CANDIDATE registry promotion (S91+)**: candidate registration in
`sessions/permanent-results-registry.md §VII` next-free-letter slot allocated
via `_script_template.py` next-free-letter helper. The candidate text:

> "Σ_2 stratum annotation taxonomy: methodology-floor F-image of substrate-IS
> a_2 Seeley-DeWitt coefficient admits 7 NCG-axiomatic annotation types (S2-WC,
> S2-FPF, S2-WVP, S2-DPI, S2-MWI, S2-CFPC, S2-MMF) plus spectral-functional
> axis types (pending lizzi authorship), structurally orthogonal at the
> layer-functor F decomposition layer per `epistemic-discipline.md
> §"Layer-Decomposition"`. Stage-2 cross-check requires axis-distinct
> reviewers per `joint-theorem-promotion.md §"Axis-B Selection Protocol"`."

**Stage-2 cross-check (S92+)**: two-agent parallel cross-verify with:

- Axis A (NCG-axiomatic): reviewer with NCG-axiomatic primary methodology,
  distinct from connes-ncg-theorist (downstream-inheritance-reach exclusion).
  Candidate: agent on spectral-geometer axis OR feynman axis (NCG-adjacent but
  axis-distinct).
- Axis B (spectral-functional): reviewer with spectral-functional primary
  methodology, distinct from lizzi-spectral-functional-theorist. Candidate:
  agent on volovik-superfluid-universe axis OR transit-dynamics-aether-mechanic
  axis.

**Stage-3 PERMANENT promotion (S93+)**: upon Stage-2 PASS-AND, promote
STAGE-1-CANDIDATE to STAGE-3-PERMANENT. The taxonomy enters the canonical
reference set with full registry-level authority.

**Audit-script first-deployment gate (S91+ candidate)**:
`S91-OR-LATER-SIGMA-2-ANNOTATION-AUDIT-FIRST-DEPLOYMENT` — author
`_sigma_2_stratum_annotation_audit.py` with the 7-TYPE classification scheme
+ self-test driver (synthetic positives for each TYPE + synthetic negative for
mis-tagged Σ_2 references). Verdict-line emission per
`.claude/rules/gate-verdicts.md` S87+ schema-v2 dual-SHA pattern.

**Cross-link to feedback rules**:

- `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold:
  this taxonomy is at K=1 SUGGESTION; promotes at K=3 distinct calibration
  instances.
- `feedback_no-asking-just-execute.md`: the parallel 2-agent dispatch
  protocol that landed this file is the no-asking-housekeeping pattern; the
  taxonomy is the structural output of the housekeeping fix.
- `feedback_mack-bridge-role.md`: mack-cosmic-bridge sole-writer convention
  does NOT apply to this taxonomy (this is methodology-floor consolidation, not
  observational-anchor registry maintenance).
- `feedback_max-effort-full-fidelity.md`: the taxonomy's content length is
  determined by structural completeness (7 NCG-axiomatic TYPES + cross-axis
  pending content + audit-script extension target + forward-promoting gates),
  not by an external line-count target.

**Substrate framing**: the Σ_2 stratum IS the methodology F-image of substrate-IS
Seeley-DeWitt weight-2 `a_2` (the Einstein-Hilbert scalar-curvature integral on
the substrate's Dirac operator D_K spectrum). The methodology layer does NOT
contain Σ_2 as content "inside" a methodology container; the methodology layer
IS Σ_2 at the wave-classification stratum. Container-thinking violation
FORBIDDEN: "wave-classification.md HOLDS the Σ_2 rule"; INVERT: "the
wave-classification rule IS the methodology-floor F-image of substrate-IS a_2 at
weight-2; the file is the persistence mechanism for that F-image, not a
container that holds it as content." Per `phononic-framing.md §"IS Space, Not IN
Space"`, the direction of explanation flows:

```
Substrate D_K spectrum
  IS the Einstein-Hilbert kinematic skeleton at weight-2 via a_2
  --> Phi : substrate-physics weight = methodology-enforcement strength
  --> Σ_2 IS the methodology-floor F-image
  --> wave-classification rule IS the persistence mechanism for that F-image
  --> the M1∧M2∧M3∧M4 conjunction IS the structural predicate
      that determines gate dispatch path via Σ_2 inhabitation
```

Inverting this direction (treating wave-classification.md as fundamental and
the substrate a_2 coefficient as derived) is a container-thinking violation per
`phononic-framing.md §"Mandatory Reframe"`.
