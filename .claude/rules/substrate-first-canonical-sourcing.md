# Substrate-First Canonical-Sourcing Discipline

Governs canonical sourcing of NUMERICAL pins in computation scripts, working-paper sections, plan-block PIN MAPs, and `canonical_constants.py` provenance entries. Complementary to `phononic-framing.md` (explanation-direction axis); operates on the sourcing axis.

Calibration corpora, K-counter advancement records, dated promotion events, per-instance narratives, and worked-example traces live at `sessions/framework/registry/pru-class-corpus.md`. The pointer table at the end of this file maps each sub-section to its corpus location. This file carries directives only.

## Scope

- `phononic-framing.md` — explanation-direction axis: invert container-thinking in narrative.
- `substrate-first-canonical-sourcing.md` — sourcing axis: pins MUST source from substrate-first computation, NOT external-paper provenance treated as authoritative.

Both apply at the same epistemological depth (substrate is logically prior). They operate on disjoint artifact classes (narrative paragraphs vs numerical pin sources).

## (i) Methodological vs canonical external-paper citations

**METHODOLOGICAL** (admissible) — external-paper citations serve as:

- Conceptual framing references.
- Cross-check anchors.
- Heritage citations.
- Notational source for definitions.

**CANONICAL** (FORBIDDEN — reroute to substrate-first source) — external-paper citations:

- Provide a NUMERICAL VALUE without the substrate-first computation having been performed.
- Cite a paper section heading as numerical-extraction source without verifying the heading exists.
- Treat SCHEMATIC library helper outputs as physical regularizations without disclosing the SCHEMATIC class.
- Use order-of-magnitude estimates when the substrate canonical exists.

Operational test: a methodological citation SUPPORTS the substrate-first computation; a canonical citation REPLACES it. Only the former is allowed.

**Status**: MANDATORY at K=4. Calibration corpus: `pru-class-corpus.md §12`.

## (ii) Audit pattern (SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze)

For every plan pin (`name = value`) at plan-freeze:

1. **External-paper provenance** (`<paper-path> §<section-id>` or `<paper-path>:<lines>`) — glob the external file for the heading or line range. If absent → AUDIT-FAIL `ABSENT-EXTERNAL-HEADING`; query `mcp__knowledge__.search_knowledge(name)` for the substrate-first canonical and recommend rerouting.
2. **Placeholder pattern** (`O(10⁻ⁿ)`, `≈ ...`, `placeholder`, `TBD`, `pending`, `analytic estimate`) — query `mcp__knowledge__.get_constant(name)`. Severity by `D_max = |log₁₀(canonical) − log₁₀(placeholder_central)|`:
   - `D_max ≥ 3.0` → AUDIT-FAIL `CLASS-(f) HARD-HALT`.
   - `1.0 ≤ D_max < 3.0` → `CLASS-(f) MANDATORY` (manual remediation).
   - No canonical exists → `CLASS-(f) ADVISORY` (substrate computation required before plan-freeze).
3. **SCHEMATIC helper** (`_spectral_action_regulators.py`, `_phononic_helpers.py`, etc. — docstring self-identifies as SCHEMATIC):
   - Gate-block missing CLASS pin → AUDIT-FAIL `SCHEMATIC-UNDISCLOSED`.
   - CLASS = SCHEMATIC + verdict-line `convention=` encodes the SCHEMATIC suffix → AUDIT-PASS.
4. **Substrate-first computation** (`computations/_shared/sN_*.py` script or `computations/_shared/sN_*.npz` data file) → AUDIT-PASS.

Audit script: `computations/_shared/_substrate_first_provenance_audit.py`. Executes after `_source_reconciliation_audit.py` and before `_pru_cardinality_audit.py` PRDR enumeration.

### Audit pipeline composition order

```
PRU (cardinality pre-flight)
  → SOURCE-RECON (value drift on pinned-vs-pinned)
  → SUBSTRATE-FIRST-PROVENANCE (source-existence on pin-vs-substrate-canonical)
  → PRDR (machinery enumeration)
  → gate execution
  → v3-recovery audit
```

## (ii.A) Atlas-row vs cache-moment layer orthogonality (within algebra-INVARIANT family)

Pins evaluated as algebra-INVARIANT spectrum-only functionals via CM-1995 §III.4 dimension-spectrum residue formula admit TWO structurally orthogonal evaluation conventions:

- **atlas-row layer at locked-norm L_k=1** — residue evaluated as closed-form algebraic identity on the substrate algebra (e.g., F_traj=(k+1)/2 identity).
- **cache-moment layer at canonical L_max truncation** — residue evaluated as numerical cache-moment ratio on the L_max-truncated D_K spectrum cache (e.g., `M_k^zeta_cache / M_k^SDW_cache`).

Both are evaluation conventions of the SAME substrate-IS canonical quantity at algebra `A_K`; they are not orthogonal containers but orthogonal F-images per `epistemic-discipline.md §"Layer-Decomposition"`.

### Discipline

1. PIN MAP entries citing closed-form atlas-row identities MUST declare the consumption layer (atlas-row vs cache-moment).
2. Cross-layer testing of an atlas-row identity at the cache-moment layer MUST cite the explicit pre-normalization machinery (locked-norm L_k=1).
3. Missing layer declaration when both layers admissible → SOURCE-RECONCILIATION advisory (S2) per `epistemic-discipline.md §"Source Reconciliation"` Class-(d). Audit: `_substrate_first_provenance_audit.py` Class-(d) variant detector.

**Cross-link**: intra-algebra-INVARIANT refinement of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. Parent rule operates at algebra-INVARIANT vs algebra-DEPENDENT axis; this sub-rule operates WITHIN the algebra-INVARIANT family.

**Status**: advisory until K=3.

### (ii.A refinement — weighting-functional family; SUGGESTION at K=2)

When a substrate-distance pole admits a THIRD F-image beyond atlas-row and cache-moment (a K_0-inheritance-class pairing whose weight is forced by the χ'-inheritance morphism), the §(ii.A) atlas-row/cache-moment binary is INSUFFICIENT and is re-axed to a WEIGHTING-FUNCTIONAL FAMILY `Φ_w : [φ] ↦ (M_KK/M_Pl)²·∫|λ|^{-s}w(λ)dμ` fibered over a finite topological base `[φ] ∈ K_0(A_K)`; atlas-row and cache-moment are two members of the family. The deeper canonical is the Fredholm module (topological shadow `[φ]` + analytic shadow `μ`). Topological STOPPING rule: every weighting factors through the same finite `[φ]`, so the K-counter is a base-count not a fiber-count — counting weightings is illegitimate. Full directive + K-counter calibration corpus: `sessions/framework/registry/cross-pillar-bridge-corpus.md §19`.

## (ii.B) Plan-text-drift correction orchestrator-convention (MANDATORY)

When a producing script encounters plan-text drift (PIN MAP entry references an upstream value or SHA superseded between plan-freeze and runtime), the producing script MUST:

1. Detect the drift at runtime via npz-ground-truth resolution per `gate-verdicts.md §"Canonical Verdict-File Path"` runtime canonical-path rescue.
2. Document the drift correction in the verdict-line `value=` field (e.g., `value='runtime_canonical_path_corrected_from_<plan-pinned>_to_<runtime>'`) OR in the dual-SHA companion comment row OR in the working-paper §"Methodology" deviation subsection.
3. Emit the verdict line with the corrected runtime value as the canonical entry; preserve the plan-pinned value as a comment-row pointer for audit trail.
4. Forward-propagate the correction to downstream gates' PIN MAP entries within the same session (orchestrator-direct-write hot-fix at next gate's pre-dispatch verification).

**Audit**: `_plan_staleness_audit.py --extension-v2` detects plan-text-drift patterns.

**Cross-link**: extends `epistemic-discipline.md §"Source Reconciliation"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE with runtime-vs-plan-freeze drift detection. SOURCE-RECON detects pin-vs-canonical drift at plan-freeze; plan-text-drift detects pin-vs-runtime drift at gate-execution.

## (iii) Worked example

Canonical worked example of Class-(f) routing under audit step (1): `pru-class-corpus.md §12 Instance #1`.

## (iv) SCHEMATIC vs full physical level pin rule

**Status**: MANDATORY at plan-freeze for all gates consuming SCHEMATIC helpers (K=4 calibration corpus). Promotion threshold per `feedback_rules-compensate-missing-structure.md`.

For any computation script consuming a helper module whose docstring self-identifies as SCHEMATIC (canonical case: `computations/_shared/_spectral_action_regulators.py`):

1. Plan gate-block MUST include a CLASS pin field with one of two values:
   - **FULL** (full physical regularization) — faithful implementation of the underlying physical regularization (e.g., live Mellin-cone evaluator via `analytic_zeta`, full Pauli-Villars subtraction with mass-scale running).
   - **SCHEMATIC** (schematic analog) — deterministic schematic capturing the structural form of the regularization but not the full physical content.
2. Verdict line MUST encode the class in `convention=` with appropriate suffix. SCHEMATIC requires `convention=<scheme>-SCHEMATIC`. Companion comment row `# tier_pin=TIER-2` SHOULD accompany the canonical line for POSITIVE compliance (see 4-class taxonomy below).
3. Synthesis section MUST include an explicit cross-class disclosure paragraph (canonical form: "the [X] holds for these schematic forms; a live-physical-regularization re-run is a separate question").

Without (1)-(3), gate verdicts under SCHEMATIC helpers are structurally indistinguishable from FULL-physical verdicts in downstream consumption — class-conflation pathology analogous to UV-regulator conflation (`UV_REGULARIZATION_CONFLATION`).

### 4-class compliance taxonomy

Four disclosure elements gate compliance:

- (1) CLASS pin SCHEMATIC declared in plan-block (or producing-script's docstring section).
- (2) `convention=...-SCHEMATIC` suffix on verdict-line `convention=` field.
- (3) SCHEMATIC docstring acknowledgment in producing script (explicit citation of the helper's SCHEMATIC docstring OR an OPERATIONAL DEVIATION block citing this rule).
- (4) `# tier_pin=TIER-2` companion comment row in verdict file alongside the canonical line.

| Class | Disclosure profile | Severity |
|:------|:-------------------|:---------|
| **POSITIVE** | (1) ∧ (2) ∧ (3) ∧ (4) all PASS | NO-ACTION; canonical disclosure pattern; future scripts SHOULD pattern-match |
| **PARTIAL-POSITIVE** | (1) ∧ (2) ∧ (3) PASS; (4) tier_pin row ABSENT | ADVISORY (S2); substrate-side complete; tier_pin row forward-recommended-not-mandatory |
| **MIXED-PARTIAL** | FULL-physical-side gate's substrate-side disclosure COMPLETE (rules 1-3 in FULL-appropriate form, no `-SCHEMATIC` suffix); SCHEMATIC-side predecessor lacks `-SCHEMATIC` suffix (GRANDFATHER asymmetry, pre-K=4-MANDATORY emission) | ADVISORY (S2); cross-gate disclosure pattern (not intra-gate); FULL-physical side structurally complete; predecessor grandfathered |
| **NEGATIVE** | ≤2-of-4 elements PASS | MANDATORY (S1); Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY per `epistemic-discipline.md §"Source Reconciliation"` Class-(d) |

**Intra-gate partition signature**: `(rules-1∧2∧3-all-PASS, tier_pin-row-PRESENT)` over {0,1}×{0,1}: (T,T) = POSITIVE; (T,F) = PARTIAL-POSITIVE; (F,*) = NEGATIVE. MIXED-PARTIAL is a separate cross-gate class outside the intra-gate partition.

### MIXED-PARTIAL K-counter advancement criterion (BOTH-SIDES-POST-K=4-MANDATORY)

MIXED-PARTIAL K-counter advances K → K+1 ONLY when the candidate instance satisfies **BOTH-SIDES-POST-K=4-MANDATORY**: BOTH sides of the SCHEMATIC↔FULL F-image divergence are individually post-K=4-MANDATORY at their producing gates AND BOTH carry structurally complete dual-tag disclosure (CLASS pin SCHEMATIC declaration + `-SCHEMATIC` convention suffix + tier_pin row).

EITHER-SIDE criterion REJECTED: it would advance trivially as SCHEMATIC predecessors get measured against new FULL-physical gates. BOTH-SIDES captures structurally distinct instances only.

**Status (MIXED-PARTIAL sub-class)**: SUGGESTION at K=1. K=3 MANDATORY promotion pending.

### Forward-looking enforcement

- **Plan-freeze halt**: any gate whose producing script imports a SCHEMATIC helper WITHOUT pre-registering CLASS pin = SCHEMATIC AND verdict-line `convention=` carrying the `-SCHEMATIC` suffix triggers plan-halt. Audit script: `computations/session-88/s88_w7b_lf_e_schematic_module_audit.py` (forward-extensible to plan-freeze auditor `_substrate_first_provenance_audit.py`).
- **Cross-link to regulator-pin-discipline**: level-pin discipline complements regulator-pin discipline at `regulator-pin-discipline.md`. Regulator-pin closes UV-regulator silent conflation (a_n^{ζ} vs a_n^{Pauli-Villars}); level-pin closes SCHEMATIC-vs-physical silent conflation. Both pathologies share substrate at the `UV_REGULARIZATION_CONFLATION` result.
- **Positive-calibration model**: future SCHEMATIC-helper-consuming scripts SHOULD pattern-match the POSITIVE disclosure protocol (TIER-2 SCHEMATIC declaration in docstring + `-SCHEMATIC` suffix in convention tag + `# tier_pin=TIER-2` companion row).
- **Inheritance-pin retroactive remediation**: gates whose PIN MAP contains a pin DERIVED from a NEGATIVE-CALIBRATION SCHEMATIC output (per K=4 calibration corpus + Class-(d) reclassification at `epistemic-discipline.md §"Source Reconciliation"` Class-(d)) MUST:
  (i) tag the inherited pin with Class-(d) inheritance-class in `convention=` (e.g., `convention=<scheme>-CLASS-D-INHERITANCE-FROM-<WITNESS>`);
  (ii) invoke the Class-(d) derivation-chain audit per `epistemic-discipline.md §"Source Reconciliation"` Class-(d) remediation (verify derivation chain; ratio check against source primitives; algebraic-equivalence audit at plan-authorship per Class 8.3 item 5);
  (iii) if threshold sensitivity to SCHEMATIC-vs-FULL jump is `≥ 1 OOM` tolerance, run substrate-canonical FULL physical regularization (the Pauli-Villars pipeline at Λ_UV = M_KK) BEFORE plan-freeze; treat the SCHEMATIC value as cross-check only.
  Forward audit subroutine: `_substrate_first_provenance_audit.py` Class-(d)-INHERITANCE-CHAIN traces pin provenance backward.

Calibration corpus: `pru-class-corpus.md §12`.

## (iv-bis) Surrogate-vs-Canonical at Cohomology-Class Layer

When a plan-block proposes a **surrogate observable** for a cohomology-class quantity (e.g., a substrate-distance-N spectral-moment ratio standing in for a Hochschild cocycle / Chern character / Connes-Karoubi pairing evaluation), the plan-block MUST pre-register the **algebraic-distance theorem** between the surrogate and the canonical:

(i) Derive the substitution chain reducing the surrogate to its component substrate-physics quantities (per `math-scripts.md §"Double-Check Logic Before Compute"`).
(ii) Identify whether the surrogate's sign and/or magnitude is **mechanically locked** to a Peter-Weyl combinatorial fraction (or other substrate-internal combinatorial constraint) by the substitution chain. If yes, the surrogate is a GEOMETRIC observable, NOT a cohomology-class observable.
(iii) Document explicitly whether a surrogate FAIL is informative on the canonical's PASS/FAIL prediction. A surrogate whose sign is mechanically locked to a substrate-distance combinatorial fraction is uninformative on a canonical whose sign depends on Hochschild cocycle / Chern character geometry — in that case, a separate canonical-evaluation gate is REQUIRED (the surrogate FAIL does NOT falsify the canonical).

Without (i)-(iii), surrogate-FAIL → canonical-FAIL inference admits silent class-conflation between geometric (substrate-distance combinatorial) and cohomology-class (Hochschild / Chern / Connes-Karoubi) observables.

**Status**: advisory until K=3. Calibration corpus + algebraic-distance theorem `R_surrogate = 2·f − 1`: `pru-class-corpus.md §11`.

## (v) SOURCE-RECONCILIATION audit class (f) — PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL

Extension to `epistemic-discipline.md §"Source Reconciliation"` 5-class taxonomy:

**(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — the plan pin is a textual approximation, order-of-magnitude estimate, or placeholder string AND a substrate-first canonical exists (or could be computed) for the same quantity.

**Detection**:

- Pattern set on the pin's VALUE field: `O\(10\^?-?\d+\)`, `≈ ...`, `~ 10\^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`, `rough estimate`, `order-of-magnitude`.
- Conjunction with substrate-canonical existence test: `mcp__knowledge__.get_constant(name)` returns a value OR `mcp__knowledge__.search_knowledge(name)` returns a substrate-computation hit.

**Severity** (HARD-HALT default at `D_max ≥ 3.0`):

- `D_max ≥ 3.0` → **HARD-HALT**.
- `1.0 ≤ D_max < 3.0` → **MANDATORY** (manual remediation; pre-registered canonical substitution before plan-freeze).
- `0.1 ≤ D_max < 1.0` → **ADVISORY** (substrate canonical recommended but not blocking).
- `D_max < 0.1` → **NO-ACTION** (within the class-(d) absorbable band).

**Remediation**: query `mcp__knowledge__.get_constant(name)` for the canonical value; substitute into the plan PIN VALUE field; re-run SUBSTRATE-FIRST-PROVENANCE sub-audit; PASS on canonical substitution.

**Status**: MANDATORY at K=4. Calibration corpus: `pru-class-corpus.md §4`.

## Cross-link to phononic-framing

The "IS Space, Not IN Space" mandate operates at TWO operational layers:

1. **Explanation-direction layer** (`phononic-framing.md`) — invert container-thinking in narrative. Every explanation flows FROM substrate TOWARD emergent physics.
2. **Canonical-sourcing layer** (this rule) — pins MUST source from substrate-first computation. External-paper provenance is methodological cross-check, never canonical replacement.

Both layers must be satisfied independently. An agent who narrates substrate-first but cites an external-paper placeholder for a numerical pin violates the canonical-sourcing layer while honoring the explanation-direction layer.

## Calibration corpus + K-counter status (pointers)

| Rule sub-section | Corpus location | Current status |
|:-----------------|:----------------|:---------------|
| (i) Methodological vs canonical | `pru-class-corpus.md §12` | MANDATORY at K=4 |
| (ii.A) Atlas-row vs cache-moment | corpus entry pending | advisory until K=3 |
| (ii.A refinement) Weighting-functional family | `cross-pillar-bridge-corpus.md §19` | SUGGESTION at K=2 |
| (ii.B) Plan-text-drift correction | corpus entry pending | MANDATORY |
| (iii) Worked example | `pru-class-corpus.md §12 Instance #1` | N/A (instance) |
| (iv) SCHEMATIC vs FULL level-pin rule | `pru-class-corpus.md §12` | MANDATORY at K=4 |
| (iv) 4-class compliance taxonomy (POSITIVE/PARTIAL-POSITIVE/NEGATIVE) | `pru-class-corpus.md §12` | MANDATORY at K=4 |
| (iv) MIXED-PARTIAL sub-class | corpus entry pending | SUGGESTION at K=1 |
| (iv-bis) Surrogate-vs-Canonical | `pru-class-corpus.md §11` | advisory until K=3 |
| (v) Source-Recon Class-(f) PIN-PLACEHOLDER | `pru-class-corpus.md §4` | MANDATORY at K=4 |
