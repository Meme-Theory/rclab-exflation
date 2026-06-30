# Session 88 W9 Synthesis: §W3a-18 Surrogate FAIL Information Value

**Date**: 2026-05-07
**Agent**: sagan-empiricist (Sagan)
**Source Documents**:
- `sessions/archive/session-88/session-88-w3a-workingpaper.md` (813 lines; §W3a-18 at lines 248-502)
- `sessions/session-plan/session-88-plan-w3a.md` (703 lines; §W3a-18 at lines 225-414)
- `sessions/archive/session-88/workshops/_seed-w3a.md` (Workshop 2 at lines 21-27)
- `computations/session-88/s88_gate_verdicts.txt` (W3a-18 canonical line at line 80; audit_sha256 = `80405c227a1d04e9...`)
- `.claude/rules/substrate-first-canonical-sourcing.md` §iv (MANDATORY at K=4 promotion S88 W7b-83)
- `.claude/rules/gate-verdicts.md` §"Option A — sig_5 remediation pathway under absolute verdict permanence" (S88 W8-100)
- `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration as track-discriminator pattern"
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" (Hybrid Independence Test, K=1)
- `.claude/agent-memory/sagan-empiricist/MEMORY.md`

---

## I. Session Outcome

The §W3a-18 surrogate FAIL is **substantively informative on a positive structural finding (W11-5 NON-COMPOSABILITY confirmed at composability_residual = 0.887 ≫ 0.01)** but is **NOT informative as a falsifier of the canonical Connes-Karoubi pairing** because the surrogate's sign is mechanically locked to a Peter-Weyl partition fraction by the algebraic identity `R_surrogate = 2·f_BdG − 1` — a combinatorial constraint with no cohomology-class content. The Sagan adjudication on the four-question seed is: (a) algebraically uninformative on canonical sign+magnitude; (b) **GO** on extending `substrate-first-canonical-sourcing.md §iv` to the cohomology-class layer with K=1 calibration corpus = §W3a-18; (c) **GO** on Option-A `supersedes`-amended verdict line per `gate-verdicts.md §"Option A"` (the WP §258-275 disclosure is necessary but not sufficient — verdict-line consumers do not read working-paper prose); (d) **GO** on dual-prior pre-registration for the S89 canonical Connes-Karoubi gate, with priors set such that surrogate FAIL is treated as uninformative on the canonical's PASS prediction.

---

## II. Key Results

### Result 1 — Algebraic Distance Between Surrogate and Canonical: Sign-Rigidity Theorem

**Result**: `sign(R_surrogate) = sign(2·f_BdG − 1)` is determined entirely by the BdG-fraction `f_BdG := a_3_BdG / a_3_full ∈ [0, 1]`. No Hochschild cocycle, Chern character, or Connes-Karoubi pairing geometry enters this sign. **Classification: GEOMETRIC** (the surrogate is a substrate-distance-1 spectral-moment ratio reduced to a Peter-Weyl combinatorial fraction; it is not a cohomology-class observable).

**Substitution chain (Sage-verified at machine precision):**

```
Step 1 (definition):   R_surrogate := (a_3_BdG − a_3_M_3(C)) / (a_3_BdG + a_3_M_3(C))
Step 2 (set-partition): a_3_full = a_3_BdG + a_3_M_3(C) at machine epsilon
                        (Sage: partition_residual_rel = 1.35e-16; WP §333-334: 2.70e-16)
Step 3 (substitute):    Let f := a_3_BdG / a_3_full ∈ [0, 1]
                        Then a_3_M_3(C) / a_3_full = (1 − f).
                        R_surrogate = (f − (1 − f)) / (f + (1 − f)) = (2f − 1) / 1 = 2f − 1
Step 4 (simplify):      R_surrogate is an affine function of the BdG color-singlet
                        substrate-distance-1 weight fraction. Range: R_surrogate ∈ [−1, +1].
Step 5 (direction):     sign(R_surrogate) = +1 iff f > 0.5; = −1 iff f < 0.5.
                        Observed (W3a-18, L_max=10): f = 0.31641, hence R_surrogate < 0 forced.
                        Sage verification: R_surrogate via (2f − 1) = −0.367176370025644;
                        R_surrogate via direct = −0.367176370025643.
                        Identity confirmed at machine epsilon (relative deviation = 1 ULP).
Conclusion: The surrogate's sign is a structural property of the SU(3) Peter-Weyl partition
            fraction at L_max=10. It is independent of any pairing structure. The canonical
            Connes-Karoubi pairing ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩ has no algebraic identity
            of this form; its sign is determined by the cocycle-projector pairing geometry.
```

The canonical observable is `R_canonical := ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩` per `cross-pillar-bridge-anatomy.md §"Level 1 — Substrate-IS Structural Identity"` calibration W-5. This is a Connes-Karoubi K-theory pairing — a bilinear coupling between a Hochschild cocycle and a Chern character class. Its functional form is **NOT** `(weight − weight)/(weight + weight)`; it is a residue-formula evaluation per Connes-Moscovici 1995 §III.4. The two observables are **not algebraically conjugate**: the surrogate is a Peter-Weyl multiplicity contraction; the canonical is a topological pairing on K-theory.

**Bayes factor of surrogate FAIL on canonical PASS hypothesis:**

```
BF = P(R_surrogate fails | canonical fails) / P(R_surrogate fails | canonical passes)
```

Because the surrogate's sign is forced by the f = 0.316 partition fraction and not by pairing geometry, both numerator and denominator are dominated by the f-fraction structure. The likelihood ratio is approximately 1 (the surrogate FAILs whether or not the canonical PASSes, because its sign is set by f). Under a Sagan-style assessment (memory rule: "BF = (prior predictive range) / (posterior width)"), the surrogate carries no posterior-width contribution to the canonical hypothesis. **The surrogate FAIL is epistemically null with respect to the canonical Connes-Karoubi pairing's sign+magnitude prediction at L_max=10.**

### Result 2 — Composability Diagnostic IS Substantively Informative (positive structural finding)

**Result**: `composability_residual = |R_surrogate − R_M_3(C)_projected_W3a-14| = 0.887 ≫ 0.01` confirms the W11-5 multiplicity-weighted Mellin-pole-window observable does **NOT** factor through ι_*. **Classification: PHONONIC** (substrate-IS structural property of the W11-5 observable construction).

**Substitution chain:**

```
Step 1 (definition):   composability_residual := |R_surrogate − R_M_3(C)_projected_W3a-14|
Step 2 (substitution):  R_surrogate = −0.36717 (this gate, ι_*-composable by partition-construction)
                        R_M_3(C)_projected_W3a-14 = −1.25397 (W11-5-machinery on triality-0 sub-list)
Step 3 (simplification): composability_residual = |−0.36717 − (−1.25397)| = 0.88680
                        Sage-verified: 0.886793629974357.
Step 4 (direction):     Per plan §322-323 (this is a pre-registered diagnostic threshold,
                        not a post-hoc threshold-shopping):
                          residual ≥ 1e−2 ⇒ W11-5 construction is NON-ι_*-COMPOSABLE
                        Observed: 0.887 is ~89× past the 1e−2 diagnostic threshold.
Conclusion: The W11-5 observable, when restricted to the triality-0 sector list (ι_*-image)
            via the W11-5 multiplicity-weighted machinery, gives a different value than
            the ι_*-composable substrate-distance-1 spectral-moment partition does. This
            difference IS structural information: the W11-5 observable's machinery is
            sensitive to global Peter-Weyl multiplicity weights that A_K^BdG_preimage
            does not carry. The W11-5 FAIL is at the OBSERVABLE level, not the bridge map.
```

This finding is substantively informative because it **strengthens** a surviving structural corridor (the inheritance morphism ι_* is well-defined; the failure is observable-construction-specific) by **closing** an alternative explanation (ι_* itself is malformed). Per Sagan memory rule 4: "Closures STRENGTHEN survivors". The composability diagnostic is the genuine epistemic content of §W3a-18 — distinct from the surrogate's sign+magnitude which carries none.

### Result 3 — Surrogate-Tagging Defect on Verdict Line

**Result**: The §W3a-18 verdict line at `computations/session-88/s88_gate_verdicts.txt:80` carries `convention=iota-star-composable-preimage-construction` with **NO** `-SURROGATE-` suffix. **Classification: NON-PHONONIC** (methodology / audit-trail hygiene).

The S88 W7b-83 promotion of `substrate-first-canonical-sourcing.md §iv` to MANDATORY at K=4 was scoped to SCHEMATIC-helper consumption (`_spectral_action_regulators.py`-class layer). The §W3a-18 surrogate is **a structurally distinct class of substrate-first-pin pathology**: the gate consumes no SCHEMATIC helper module, but it computes a substrate-physics-grounded surrogate observable BY ANALOGY with the lit anchor's algebraic form, while the canonical Connes-Karoubi pairing infrastructure exists only in queued (S89+) form. The substrate-first-canonical-sourcing.md §iv class taxonomy (FULL vs SCHEMATIC at the helper layer) does not currently cover this case.

The W11-5 FAIL stood at REGISTRY-FAIL prior to W3a-18. The §W3a-18 verdict line will be consumed by:
- **W3b synthesis** (next wave, volovik+connes joint synthesizers)
- **knowledge-MCP indexing** (`/weave --update` Phase 6 routing manifest export)
- **S89+ planners** drafting the W3c queue
- **Future session orchestrators** querying `mcp__knowledge__.trace_entity("W11-5 cross-pillar bridge anatomy")` or related searches

The current `convention=iota-star-composable-preimage-construction` tag does **not signal to any of these consumers** that the FAIL is on a surrogate, not the canonical. The WP §258-275 Honest-Disclosure block + §461 caveat exist in the working-paper file, but per the layer-functor F at the methodology↔audit pair (`epistemic-discipline.md §"Layer-Decomposition"`), the verdict-line `convention=` field IS the audit-layer image of the substrate-layer "what was actually computed" predicate. The audit layer is structurally separate from the working-paper layer — downstream consumers of the verdict file cannot be assumed to read the WP. A surrogate-tagged verdict line is the audit-layer equivalent of the substrate-layer disclosure.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W3a-18 (S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY) | FAIL (composite); 3-tuple `sign=FAIL magnitude=FAIL regime=VALID` | `ratio_mismatch_redefined = 11.385` (228× past PASS-loose ceiling 0.05); `composability_residual = 0.887` (DIAGNOSTIC, ≫ 0.01); `R_surrogate = 2f−1 = −0.367` with `f = 0.316` (sign forced by combinatorics) |

Source: `computations/session-88/s88_gate_verdicts.txt:80` audit_sha256 = `80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8`. Gate verdict is authoritative per epistemic-discipline.md §"Source Authority Hierarchy" item 3 ("Gate verdict results"); not re-adjudicated here.

---

## IV. Structural Implications

### IV.A — Adjudication on Seed Question (a): Is surrogate FAIL substantively informative about canonical Connes-Karoubi prediction at L_max=10?

**Sagan verdict: NO on sign+magnitude (surrogate FAIL is epistemically null on canonical's sign+magnitude prediction); YES on the composability sub-diagnostic (W11-5 NON-COMPOSABILITY confirmed at residual 0.887).**

The two facts that the surrogate establishes are not the same fact:

1. **Surrogate's sign+magnitude FAIL** (R_surrogate = −0.367 vs R_lit = +0.0354): driven by `R_surrogate = 2·f_BdG − 1` with f = 0.316. This algebraic identity IS the sign-determining mechanism. The canonical Connes-Karoubi pairing has no analogous identity — its sign is determined by the cocycle-projector pairing's K-theory class signature. **No constraint on canonical sign.**

2. **Composability diagnostic** (residual 0.887 ≫ 0.01): driven by the difference between the W11-5 multiplicity-weighted observable evaluated on the triality-0 sub-list (W3a-14: −1.254) and the substrate-distance-1 partition-fraction surrogate (W3a-18: −0.367). The 0.887 magnitude IS structural information about the W11-5 machinery's sensitivity to Peter-Weyl multiplicity weights, **independent** of which observable class either represents. This DOES constrain the structural reading: W11-5 FAIL is observable-construction-specific, NOT bridge-map-defective.

The seed Workshop 2 frames these as "surrogate FAIL constrains canonical PASS — Track A informative prior 0.7 / Track B uninformative prior 0.5". The Sagan reading: this dual prior is mis-formulated because the two facts above are STRUCTURALLY ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3, S87 W-2 close). The sign+magnitude question is one axis; the composability question is another. A correct dual-prior pre-registration for the S89 canonical gate (see §IV.D below) must separate these.

### IV.B — Adjudication on Seed Question (b): Should `substrate-first-canonical-sourcing.md §iv` be extended to cohomology-class layer?

**Sagan verdict: GO on extension. K=1 calibration corpus = §W3a-18.**

The §iv MANDATORY-at-K=4 rule covers SCHEMATIC-helper consumption (a producing script imports a helper module whose docstring self-identifies as SCHEMATIC). The §W3a-18 case is **a structurally distinct class of substrate-first-pin pathology**: the gate consumes no SCHEMATIC helper module, but it computes a substrate-physics-grounded SURROGATE for an observable whose CANONICAL infrastructure (faithful Connes-Karoubi pairing) is queued-but-unimplemented. Per `feedback_rules-compensate-missing-structure.md` K-counter discipline, this is K=1 of a new sub-clause. The extension does not require rewriting the existing §iv body; it adds a new sub-clause covering the surrogate-vs-canonical-cohomology-class case.

The proposed sub-clause is fully specified in §V.5 below. The K=1 status means this is SUGGESTION at landing; it hardens to MANDATORY at K=3 distinct calibration instances. The §W3a-18 instance is the seed; future instances (e.g., any gate that computes a substrate-physics-grounded analog of a canonical NCG pairing because the canonical infrastructure is queued) advance the counter.

**Justification for the K=1 landing rather than queueing:** per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`, the rule extension is fix-in-session because (a) the substrate-first-canonical-sourcing.md §iv K=4 promotion is RECENT (S88 W7b-83 close, 2026-05-05); (b) the §W3a-18 case is the IMMEDIATE STRUCTURAL EXTENSION of the same pathology class to the cohomology-class layer; (c) the rule extension itself is METHODOLOGY-class per `wave-classification.md §M4` (allowlist would need to admit a new gate-ID for the rule-file edit landing).

### IV.C — Adjudication on Seed Question (c): Should §W3a-18 verdict line be Option A `supersedes`-amended?

**Sagan verdict: GO on Option A `supersedes`-amended verdict line.**

The current verdict line at `computations/session-88/s88_gate_verdicts.txt:80` carries:

```
S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY: FAIL -- value=1.138493e+01 scheme=NCG-cohomology-class-Hochschild-pairing-pole-1 convention=iota-star-composable-preimage-construction L_max=10 audit_sha256=80405c227a1d04e9...
```

Two problems with the as-emitted line:

1. **`scheme=NCG-cohomology-class-Hochschild-pairing-pole-1`** is structurally MISLEADING: the gate did NOT compute a Hochschild pairing; it computed a substrate-distance-1 spectral-moment partition-fraction surrogate. The `scheme=` field describes the canonical that the gate INTENDED to operationalize, not the surrogate that was actually evaluated. Downstream knowledge-MCP indexing will register this gate as a Hochschild-pairing computation (`mcp__knowledge__.trace_entity("Hochschild pairing")` will return W3a-18 as a hit), which is structurally false.

2. **`convention=iota-star-composable-preimage-construction`** correctly states ONE structural property (the construction is ι_*-composable by partition) but does NOT signal that the value is a surrogate, not the canonical evaluation.

Per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` (S88 W8-100 user adjudication, 2026-05-05): the original line is RETAINED on disk; a corrective canonical line is APPENDED with `supersedes=80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8` tag in the dual-SHA companion comment row, and the corrective line carries the missing `-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` suffix in `convention=`. Downstream consumers cite the latest non-superseded line per the Option A reading discipline.

The Sagan defense of the WP-disclosure-sufficient counter-position fails because: (a) the verdict file IS THE AUDIT-LAYER ARTIFACT consumed by knowledge-MCP, `/weave --update`, and downstream cross-session orchestrators; (b) those consumers do NOT read the working-paper file; (c) the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`) maps the substrate-layer disclosure (WP §258-275 Honest-Disclosure block) under F to an analogous methodology-layer disclosure (rule-file extension §IV.B) and an audit-layer disclosure (verdict-line `convention=` suffix). All three layers are needed; the WP block alone is the substrate-layer image only.

This is NOT a Class-3 PROHIBITED_ACTIONS violation (post-hoc audit-trail editing) per `v3-closure-recovery.md §PROHIBITED_ACTIONS`: Option A IS the structurally permitted alternative. The original line is BYTE-LEVEL PRESERVED; the corrective is APPENDED. Per the gate-verdicts.md §"Option A" rule-2: "The corrective canonical line carries a `supersedes=<full-64-char-old-audit-sha>` token in its `value=` field OR in the dual-SHA companion comment row, naming the original audit_sha256 the corrective line replaces in the audit-trail-canonical reading."

### IV.D — Adjudication on Seed Question (d): Should S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL pre-register dual-prior on whether surrogate FAIL constrains canonical PASS?

**Sagan verdict: GO with REVISED dual-prior structure.**

The seed proposes:
- Track A: surrogate FAIL informative; prior 0.7 canonical also FAILs.
- Track B: surrogate FAIL uninformative; prior 0.5 canonical PASSes.

Per the algebra-axis orthogonality of §IV.A, this dual prior conflates the sign+magnitude axis with the composability-diagnostic axis. The Sagan re-formulation:

**Dual prior pre-registration spec for `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`** (per `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"`, MANDATORY at K=2 from S86 W-9 baseline):

```
TRACK A — Surrogate sign+magnitude FAIL is informative on canonical sign+magnitude:
  Prior: 0.20 (DOWNGRADED from seed's 0.70)
  Rationale: R_surrogate = 2·f_BdG − 1 algebraic identity makes surrogate's sign a
             function of Peter-Weyl partition fraction, NOT cohomology-class structure;
             canonical Connes-Karoubi pairing's sign is determined by K-theory class
             signature with no analogous combinatorial-fraction reduction.
  Discriminator: PASS at S89 canonical → posterior on Track A drops to ~0.05;
                 FAIL at S89 canonical → posterior on Track A rises to ~0.40.
                 (BF for FAIL → Track A is bounded above by ~2.0 since FAILs in
                  general can occur for many independent structural reasons.)

TRACK B — Surrogate sign+magnitude FAIL is uninformative on canonical sign+magnitude:
  Prior: 0.80 (UPGRADED from seed's 0.50)
  Rationale: same algebraic-distance argument; canonical and surrogate are not
             algebraically conjugate observables.
  Discriminator: PASS at S89 canonical → posterior on Track B rises to ~0.95;
                 FAIL at S89 canonical → posterior on Track B drops to ~0.60.

ORTHOGONAL TRACK C — Composability diagnostic (residual 0.887) IS informative:
  Prior: 0.95 (high confidence; this is the substantive structural finding)
  Discriminator: PASS at S89 canonical → confirms W11-5 FAIL was observable-construction-
                 specific, bridge ι_* well-defined, posterior on Track C → 0.99;
                 FAIL at S89 canonical → bridge map ι_* MAY itself be defective,
                 posterior on Track C drops to ~0.50; route to W3c-(b) convention
                 demarcation theorem (per W3a-19 carry-forward).
```

The structural difference from the seed's dual-prior: the orthogonal Track C is independent of Tracks A/B and serves as a separate posterior-update axis on the bridge-map well-definedness question. This matches the algebra-axis orthogonality K-counter discipline; the two questions cannot be conflated under a single dual-prior.

**Pre-registered substantive direction**: per Sagan memory rule 1 (Pre-registration / Venus Rule), only pre-registered gates move probability. The S89 canonical gate's PASS/FAIL outcome is the DISCRIMINATING evidence; this dual-prior pre-registration MUST be in the S89 plan-block at plan-freeze time. The W3b synthesis is the appropriate venue for the pre-registration to land (per the seed Workshop 1 routing); the S89 plan author then consumes the W3b synthesis.

### IV.E — Three-Level Structural-Confidence Ladder Status (per `cross-pillar-bridge-anatomy.md`)

The W3a-18 surrogate FAIL leaves the FWD-C3 instance #2 (W11-5) bridge entry status at the `permanent-results-registry.md §VII.AJ` row UNCHANGED:

- **Level 1** (substrate-IS structural identity): cocycle ratio invariant 7.324992 PRESERVED at publication precision (residual 1.76e-05 within Class 8.3 tol 1e-4); set-partition identity exact at machine epsilon. STRUCTURAL THEOREM verified.
- **Level 2** (algebraic envelope): L^{-3} envelope at d=4 ⇒ 10^{-3} at L_max=10; ratio_mismatch / |R_lit| ≤ 0.001 strict OR ≤ 0.05 loose. STRUCTURAL PREDICTION standing.
- **Level 3** (empirical anchor at canonical L_max=10): SURROGATE evaluation gives 11.385 ⇒ Level 3 violates Level 2 by 228× ON THE SURROGATE. Canonical Level 3 evaluation is queued for S89+ W3c (`S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`).

Registry-PASS criterion (Level 3 < Level 2 envelope at canonical L_max) FAILs ON THE SURROGATE; canonical evaluation pending. **Per the Hybrid Independence Test at `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"`, this gate is an inherited-axes companion of W11-5 instance #2 — same Pillar I/II ↔ V substrate↔laboratory pair, same bridge map class, same algebraic envelope. K-counter UNCHANGED at K=2.**

### IV.F — Constraint Map Updates (Sagan-side)

| Constraint | Implication | Surviving solution space | Root cause |
|:-----------|:------------|:-------------------------|:-----------|
| Surrogate observable `R = 2·f − 1` is sign-locked by Peter-Weyl partition fraction | Surrogate cannot independently constrain canonical sign+magnitude | Canonical Connes-Karoubi pairing is the only observable that can falsify the cohomology-class hypothesis at L_max=10 | Algebraic conjugacy: surrogate is a Peter-Weyl combinatorial reduction; canonical is a K-theory pairing |
| W11-5 NON-COMPOSABILITY confirmed (residual 0.887) | W11-5 FAIL is at the OBSERVABLE level, not the bridge-map level | Bridge map ι_* well-defined (S86 W1b-T8 inheritance theorem PRESERVED); structural fix is observable-construction redefinition (W3c-(a) canonical pairing) OR convention demarcation (W3c-(b)) | W11-5 multiplicity-weighted Mellin-pole window depends on A_K-global Peter-Weyl multiplicity weights, not A_K^BdG-local data |
| Verdict-line `convention=` field carries no surrogate suffix | Knowledge-MCP indexing will register W3a-18 as a Hochschild-pairing computation (structurally false) | Option A `supersedes`-amended verdict line corrects this without violating verdict permanence | Audit-layer disclosure separation from substrate-layer disclosure under layer-functor F |
| §iv MANDATORY-K=4 covers SCHEMATIC-helper layer only | Cohomology-class-layer surrogate-vs-canonical pathology not currently rule-covered | New §iv sub-clause covers cohomology-class layer at K=1 (§W3a-18 calibration); MANDATORY at K=3 promotion threshold | Substrate-first canonical sourcing principle generalizes across helper-module layer + cohomology-class layer |

---

## V. Carry-Forward Computations

### V.1 — Option A `supersedes`-amended verdict line for §W3a-18

- **What**: Append a new canonical line to `computations/session-88/s88_gate_verdicts.txt` for `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY` with `convention=iota-star-composable-preimage-construction-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` and a dual-SHA companion comment row carrying `supersedes=80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8`. Recompute the closure_hash over the input-pin map (which now includes the surrogate-tag pin in addition to the original 9 pins) to produce a NEW audit_sha256 for the corrective line. Original line at line 80 is BYTE-PRESERVED.
- **Inputs**: original §W3a-18 producing-script `computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.py`; original verdict-line audit_sha256 for `supersedes=` token; substrate-first-canonical-sourcing.md §iv extension text (V.5 below) as the rule-pin source.
- **Gate**: `S88-W9-W3A-18-VERDICT-LINE-SUPERSEDES-AMENDMENT`. PASS iff (a) corrective canonical line appears in verdict file with `supersedes=80405c22...` in companion row; (b) audit_sha256 of corrective line is unique (sig_5 closure preserved); (c) `_mechanical_closure_audit.py` (or analogous Option-A audit script if landed) parses the supersession chain correctly. INFO if any condition partially met. FAIL if corrective line emission breaks dual-SHA discipline.
- **Effort**: 0.2 wave-equivalents (single-shot append script + audit-trail verification; no eigenvalue computation).

### V.2 — `substrate-first-canonical-sourcing.md §iv` extension to cohomology-class layer

- **What**: Add a new sub-clause to `.claude/rules/substrate-first-canonical-sourcing.md §iv` covering the SURROGATE-vs-CANONICAL distinction at the COHOMOLOGY-CLASS layer (above the SCHEMATIC-helper layer that the existing §iv covers). The sub-clause specifies: (a) detection pattern: producing script computes a substrate-physics-grounded surrogate for an observable whose canonical infrastructure (e.g., faithful Connes-Karoubi pairing, Connes-Moscovici dim-spectrum residue evaluation, K-theoretic torsion classifier) is queued-but-unimplemented; (b) MANDATORY verdict-line `convention=` suffix `-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN`; (c) MANDATORY working-paper Honest-Disclosure block declaring the surrogate-vs-canonical distinction, the structural distance argument, and the queued canonical infrastructure carry-forward; (d) MANDATORY downstream-consumer reading discipline (W3b synthesis, knowledge-MCP indexing, S89+ planners must NOT propagate surrogate FAILs to canonical-hypothesis-falsification claims). K=1 calibration corpus = §W3a-18.
- **Inputs**: existing `substrate-first-canonical-sourcing.md §iv` text (current MANDATORY-K=4 promotion at S88 W7b-83); §W3a-18 WP §258-275 Honest-Disclosure block as reference exemplar; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause for the orthogonality framing; `gate-verdicts.md §"Option A"` for the verdict-line tagging discipline.
- **Gate**: `S88-W9-SUBSTRATE-FIRST-IV-COHOMOLOGY-CLASS-EXTENSION`. METHODOLOGY-class per `wave-classification.md §M4`. PASS iff (a) sub-clause text added to rule file; (b) K=1 calibration corpus entry `§W3a-18` documented with surrogate observable specification + algebraic-distance theorem (`R_surrogate = 2·f − 1` sign-rigidity); (c) audit script `_substrate_first_provenance_audit.py` extension queued (S87 carry-forward V.1) updated to detect cohomology-class-layer surrogate pattern; (d) gate-ID added to `methodology-wave-allowlist.md` row.
- **Effort**: 0.5 wave-equivalents (rule-file edit + allowlist append + audit-script extension queue).

### V.3 — Dual-prior pre-registration for `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`

- **What**: Pre-register the Sagan-revised dual-prior structure (Tracks A, B, C per §IV.D above) in the S89 plan-block for `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`. Document priors, discriminator outcomes, and the algebra-axis orthogonality justification for separating the sign+magnitude axis (Tracks A/B) from the composability-diagnostic axis (Track C). Cross-link to the §W3a-18 surrogate FAIL as the EVIDENCE BASIS (not as a falsifier of the canonical) and to the §W3a-18 composability_residual = 0.887 finding as the substantive structural input.
- **Inputs**: §W3a-18 surrogate FAIL (this gate); §W3a-18 composability_residual finding; `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` (MANDATORY at K=2, S86 W-9); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.
- **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL` plan-block authored with the Sagan-revised dual-prior pre-registration as part of its standard plan-block. PASS-strict iff `ratio_mismatch_canonical ≤ 0.001`; PASS-loose / INFO if (0.001, 0.05]; FAIL if > 0.05. The PASS/FAIL outcome triggers the pre-registered Track-A/B/C posterior re-allocation per §IV.D.
- **Effort**: 0.3 wave-equivalents at S88 (plan-block authorship); the canonical evaluation itself is the W3c S89+ ~3 wave-equivalents from the WP §744-786 carry-forward (separate from this pre-registration spec gate).

### V.4 — Cocycle ratio Sage-exact cross-validation under L_max scan (CF-W3a-ADDITIONAL-B promotion)

- **What**: Per the seed CF-W3a-ADDITIONAL-B carry-forward, the §W3a-14 + §W3a-18 cocycle ratio cross-check (computed 7.324974 vs canonical 7.324992; residual 1.76e-05 within Class 8.3 publication-precision floor 1e-4) was performed at L_max=10 only. The §W3a-19 L_max-scan extended to {16, 18, 20} did NOT cross-validate the cocycle ratio. Test cocycle ratio invariant preservation across L_max ∈ {16, 18, 20} via closed-form sector enumeration; verify the canonical pin is L_max-independent at the publication-precision floor.
- **Inputs**: `canonical_constants.py: cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`; §W3a-19 sector enumeration code at L_max ∈ {16, 18, 20}.
- **Gate**: `S89-W3A-COCYCLE-RATIO-LMAX-INVARIANCE-CROSS-VALIDATION`. PASS iff `|ratio(L) − 7.324992| / 7.324992 ≤ 1e−4` (Class 8.3 publication precision tol) for ALL L ∈ {10, 16, 18, 20}. INFO if 1e-4 < deviation ≤ 1e-3. FAIL otherwise.
- **Effort**: 0.2 wave-equivalents (single closed-form recompute from canonical pins; no eigenvalue work).

### V.5 — Rule-extension diff specification for `substrate-first-canonical-sourcing.md §iv`

The rule-extension diff is defined here in full to anchor V.2's deliverable:

**New sub-clause**: §iv-bis "Surrogate-vs-Canonical at Cohomology-Class Layer" — placed after the existing §iv K=4 calibration corpus table.

**Detection**: producing script computes a substrate-physics-grounded surrogate observable BY ALGEBRAIC ANALOGY with a laboratory-IN observable's algebraic form (e.g., `(a − b)/(a + b)` ratio shape; difference-of-spectral-moments construction), where the canonical observable (Connes-Karoubi pairing, Connes-Moscovici residue evaluation, K-theoretic torsion classifier, or other NCG-axiomatic substrate-IS observable) is queued-but-unimplemented per a documented carry-forward.

**MANDATORY at plan-freeze for S89+ gates**: (i) verdict-line `convention=` field carries `-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` suffix; (ii) working-paper Honest-Disclosure block declares the surrogate-vs-canonical distinction, includes a substitution-chain-derived algebraic-distance theorem for the surrogate (calibration: §W3a-18 `R = 2·f − 1` sign-rigidity), and cites the queued canonical infrastructure carry-forward 4-field spec; (iii) downstream consumers (W3b synthesis, knowledge-MCP indexing, S89+ planners) must NOT propagate surrogate sign+magnitude FAILs to canonical-hypothesis-falsification claims; only the composability diagnostic (or analogous structural by-product) propagates.

**K=1 calibration corpus instance**: §W3a-18 (S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY). Surrogate: `R_surrogate = (a_3_BdG − a_3_M3C)/(a_3_BdG + a_3_M3C)`. Canonical: `R_canonical = ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩` per Connes-Moscovici 1995 §III.4 dim-spectrum residue formula. Algebraic-distance theorem: `R_surrogate = 2·f_BdG − 1` with f_BdG = a_3_BdG/a_3_full, sign forced by Peter-Weyl partition fraction; canonical's sign determined by K-theory class signature (no analogous combinatorial-fraction reduction). Composability sub-diagnostic IS substantively informative (residual 0.887 ≫ 0.01 confirms W11-5 NON-COMPOSABILITY); surrogate sign+magnitude FAIL is epistemically null on canonical sign+magnitude.

**Status**: SUGGESTION at K=1 (this clause); promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold.

**Audit-script extension (queued)**: extend `_substrate_first_provenance_audit.py` (S87 carry-forward V.1) to detect cohomology-class-layer surrogate pattern by (a) regex on producing-script docstring for "surrogate" / "by analogy with" / "queued for" near a Hochschild / Connes-Karoubi / K-theory keyword; (b) verdict-line `convention=` field check for `-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` suffix when (a) matches.

- **What**: Apply the diff text above to `.claude/rules/substrate-first-canonical-sourcing.md §iv` as a new sub-clause; add row to K=1 calibration corpus.
- **Inputs**: this synthesis §V.5 spec; existing §iv text; W3a-18 WP §258-275 + §313-320 + §407 + §461 references.
- **Gate**: `S88-W9-SUBSTRATE-FIRST-IV-COHOMOLOGY-CLASS-EXTENSION` (same as V.2; this is the spec, V.2 is the landing).
- **Effort**: 0 additional wave-equivalents beyond V.2 (the spec is consumed by V.2).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `R_surrogate = 2·f_BdG − 1` sign-rigidity theorem | GEOMETRIC | Sage-verified at machine epsilon (relative deviation 1 ULP) | Surrogate FAIL is epistemically null on canonical Connes-Karoubi pairing's sign+magnitude prediction; closes the seed Workshop 2 question (a) on the negative side |
| 2 | Composability diagnostic `residual = 0.887 ≫ 0.01` | PHONONIC | Pre-registered DIAGNOSTIC threshold (plan §322-323); not FAIL evidence | W11-5 NON-COMPOSABILITY confirmed; bridge map ι_* well-defined; structural fix locus is observable-construction redefinition (W3c-(a)) OR convention demarcation (W3c-(b)) |
| 3 | Verdict-line surrogate-tagging defect at line 80 | NON-PHONONIC (audit hygiene) | GO on Option A `supersedes`-amended emission per `gate-verdicts.md §"Option A"` (S88 W8-100) | Knowledge-MCP indexing currently registers W3a-18 as a Hochschild-pairing computation (structurally false); Option-A correction preserves verdict permanence and fixes audit-layer disclosure |
| 4 | `substrate-first-canonical-sourcing.md §iv` extension to cohomology-class layer | NON-PHONONIC (methodology rule) | GO on K=1 sub-clause landing; MANDATORY at K=3 promotion | Closes structurally-distinct surrogate-vs-canonical pathology class above the SCHEMATIC-helper layer; §W3a-18 is the K=1 calibration corpus |
| 5 | Sagan-revised dual-prior pre-registration spec for S89 canonical gate | NON-PHONONIC (methodology spec) | GO with three-track structure (Tracks A/B sign+magnitude axis; Track C composability axis; algebra-axis orthogonality) | Aligns dual-prior pre-registration with `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3; correctly separates the two structurally distinct discriminator axes |
| 6 | Cocycle ratio invariant 7.324992 PRESERVED at publication precision (residual 1.76e-05 within Class 8.3 tol 1e-4) | PHONONIC | UNCHANGED across §W3a-14 + §W3a-18 | S86 W1b-T8 inheritance theorem floor PRESERVED; (Δ_B/Δ_A)^p=0 cancellation theorem PRESERVED at machine precision |
| 7 | FWD-C3 instance #2 (W11-5) `permanent-results-registry.md §VII.AJ` row | (registry status) | REGISTRY-FAIL with W3c-queue diagnostic note (UNCHANGED by W3a-18) | K-counter UNCHANGED at K=2; canonical Connes-Karoubi evaluation pending S89 W3c |

---

**End of synthesis.**

**Verdict on the four seed questions (compact form):**

(a) Surrogate FAIL is **NOT informative** on canonical sign+magnitude (sign-rigidity theorem `R_surrogate = 2·f − 1` decouples surrogate from cohomology-class structure); is **substantively informative** on the orthogonal composability axis (residual 0.887 confirms W11-5 NON-COMPOSABILITY).

(b) **GO** on `substrate-first-canonical-sourcing.md §iv` extension to cohomology-class layer. K=1 calibration corpus = §W3a-18. SUGGESTION at K=1; MANDATORY at K=3.

(c) **GO** on Option-A `supersedes`-amended verdict line. Original line BYTE-PRESERVED at `s88_gate_verdicts.txt:80`; corrective line APPENDED with `convention=iota-star-composable-preimage-construction-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` and `supersedes=80405c227a1d04e9...` companion. WP §258-275 Honest-Disclosure block is necessary but not sufficient (audit-layer consumers do not read WP).

(d) **GO** on dual-prior pre-registration with three-track structure (A: surrogate informative on canonical sign+magnitude, prior 0.20 — DOWNGRADED from seed's 0.70; B: surrogate uninformative, prior 0.80 — UPGRADED from seed's 0.50; C: composability axis, prior 0.95 — orthogonal track). Algebra-axis orthogonality K-counter MANDATORY clause is the structural justification.
