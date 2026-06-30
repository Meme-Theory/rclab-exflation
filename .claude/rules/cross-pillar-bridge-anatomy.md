# Cross-Pillar Bridge Anatomy

Governs registration of cross-pillar bridge theorems in `sessions/permanent-results-registry.md`. Cross-link: `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space".

A cross-pillar bridge theorem connects a substrate-IS observable on one pillar to a laboratory-IN observable on a different pillar. Every registry entry MUST declare BOTH the IS-not-IN anatomy (5 elements) AND the three-level structural-confidence ladder.

**This file is a LOOKUP + ENFORCEMENT index, not an exposition.** There are too many registration cases to carry their full methodology inline. Each heading below states the one-line DIRECTIVE (what is required / forbidden), its enforcement trigger + severity, its status (SUGGESTION/MANDATORY, K=N), and the audit hook. The full taxonomy, tables, structural derivations, regex pattern definitions, worked examples, per-instance landings, dual-SHA provenance, and K-counter advancement records for **every** section live in `sessions/framework/registry/cross-pillar-bridge-corpus.md` at the cited `§N`. Headings are preserved verbatim so every existing `cross-pillar-bridge-anatomy.md §"…"` cross-reference (in session papers, audit scripts, and sister rules) still resolves — it lands on the directive + a corpus pointer. **Maintenance contract**: do NOT re-inline taxonomy/tables/derivations/examples here; add detail to the corpus and point to it. This file carries directives only.

## Three-Level Structural-Confidence Ladder

Every entry MUST declare all three levels explicitly. Missing-level entries are registry-incomplete (plan-freeze HARD-HALT).

### Level 1 — Substrate-IS Structural Identity (cohomology-class level)

STRUCTURAL THEOREM; regulator-invariant, L-independent (holds at every L_max); identity at the cohomology-class / K-theory-pairing / spectral-triple-axiom level.

### Level 2 — Algebraic Convergence Envelope

STRUCTURAL PREDICTION; L_max-dependent `L^{-α}` bound on the convergence rate to the continuum / laboratory image; refines with L-scan.

#### Level-2 audit axes (Level-2-A vs Level-2-B)

DIRECTIVE: structural-exact envelopes MUST PASS BOTH axes at Stage-2 — **Level-2-A** (operational content; transit-dynamics axis; audited by cross-reviewer-B) and **Level-2-B** (regulator-invariance; spectral-functional axis; audited by cross-reviewer-A). Status: advisory K=1. Full detail: corpus §9.

#### Level-2 sub-class (binding vs non-binding)

DIRECTIVE: declare the sub-class. **Level-2-binding** = `L^{-α}` is the convergence rate of an HKR-image that BINDS Level-1 (operationally bounds `‖HKR(c_L) − c_continuum‖`); registry-PASS-eligible. **Level-2-non-binding** = bare-decomposition rate, no HKR image, `c_continuum` undefined; FORBIDDEN for registry-PASS. Enforcement: Level-2-non-binding → plan-freeze HARD-HALT (remediation: cite the HKR / Connes-Karoubi / K-theory boundary map + the `c_continuum` reference quantity); sub-class undeclared → registry-INCOMPLETE HARD-HALT. Status: SUGGESTION K=2 (→ MANDATORY at K=3). Full detail (the *Level-2 Layer Distinction* calibration): corpus §1 + §7.

#### Deferred-pending intermediate verdict-class

DIRECTIVE: between binding-ELIGIBLE and non-binding-INELIGIBLE, three tags reserve a §VII slot while empirical realization is partial — `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (SCHEMATIC proxy / Casimir-bound), `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (symbolic-only, no numerical anchor), `REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT` (operational-machinery state-side spec). Routing: all three → plan-freeze **S2 advisory** (NOT HARD-HALT); the tag RESERVES the slot and does NOT contribute to registry-PASS by itself. Status: SUGGESTION K=2 (→ MANDATORY at K=3). Audit: `computations/_shared/_cross_pillar_bridge_audit.py::detect_deferred_pending_sub_class` (regex defs live in the script). Slot-reservation semantics + per-instance landings: corpus §1 (Instance #3) + §14.

#### FOUR-rule cross-composition meta-pattern

DIRECTIVE: a §VII entry may simultaneously inhabit FOUR orthogonal rule structures — (1) layer-separability carve-out, (2) PROXY-REFINEMENT deferred-pending, (3) OPERATIONAL-ALIGNMENT deferred-pending, (4) Three-Layer Regulator L3-OBSERVABLE stratum. Cross-composition advances its own K-counter via the Hybrid Independence Test. Status: SUGGESTION K=1. Admissibility predicate + calibration: corpus §14.

### Level 3 — Empirical Anchor at Canonical L_max

EMPIRICAL CONFIRMATION; numerical evaluation at canonical truncation satisfying the Level-2 envelope.

#### Level-3 anchor singleness sub-clause

DIRECTIVE: for Hybrid entries (single slot with a regulator-class-keyed Level-2-B sub-row table), Level-3 MUST be single-pinned at the substrate-natural canonical; the sub-row table is DIAGNOSTIC ONLY and its values MUST NOT be cross-referenced as Level-3 co-primaries (cross-corner co-primary at the Level-3 axis FORBIDDEN per `substrate-first-canonical-sourcing.md §(i)`). Status: SUGGESTION K=1. Full detail: corpus §15.

### Registry-PASS criterion

```
Level-3 empirical value  <  Level-2 envelope value  at canonical L_max
```

Counted toward registry-PASS only when Level-2 is Level-2-binding. Level-3 violation OR non-binding Level-2 OR missing level → FAIL or registry-INCOMPLETE.

### Tier-1/Tier-2 dimensional-re-anchorability gate

DIRECTIVE: a Level-3 anchor is registry-PASS-ELIGIBLE only if EITHER **(Tier-1)** its residual-to-`c_continuum` shrinks with L_max (convergent ⇒ a substrate-singled-out `L*` exists), OR **(Tier-2)** its divergent channel's truncation-invariant content is DIMENSIONLESS and the anchor is RE-ANCHORED to that invariant (a log-derivative / ratio / cohomology-class anchor). A **Tier-2-dimensionful** anchor (a dimensionful magnitude on a divergent channel) is registry-PASS-INELIGIBLE: its Level-3 row is HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`, while the joint theorem-STRUCTURE may independently hold STAGE-3-PERMANENT via Stage-2 PASS-AND on the non-Level-3 clauses. Status: SUGGESTION K=2 (→ MANDATORY at K=3). Audit: Tier-1/Tier-2 detector extension to `_cross_pillar_bridge_audit.py` (S2 advisory). Structural basis (`O(L,K)=W(L)·g(K)` ⇒ only log-derivatives annihilate `W(L)`) + inaugural occupant (§VII.AX.OP-PROJ n_PBH): corpus §25.

## Non-Promotion-by-Held-Number Meta-Taxonomy

DIRECTIVE: a non-promotion verdict on a substrate-IS observable is a NON-PROMOTION-BY-HELD-NUMBER instance iff (P1) the theorem-STRUCTURE is permanent/proven ∧ (P2) a NUMBER is HELD against substrate-natural extraction ∧ (P3) the held NUMBER is NOT sideways-re-pinned to a methodology-floor F-image. Each instance MUST declare which of three differentiae fires: **dimensionful-slot-collision** / **undischarged-magnitude-bound** / **sign-lock**. Orthogonal to the deferred-pending verdict-class (NON-PROMOTION keys on extractability under an already-SETTLED structure; deferred-pending keys on WHEN a binding Level-2 lands) — a held-NUMBER non-promotion MUST NOT be mis-filed as a deferred-pending slot-reservation, and vice versa. Status: SUGGESTION K=1 (→ MANDATORY at K=3; distinctness on the 3-way discriminator axis). Audit: held-NUMBER-vs-deferred-pending disambiguator extension to `_cross_pillar_bridge_audit.py` (S2). Genus predicate + 3-way differentia table + 3 inaugural instances: corpus §26.

## Single-observable-per-triple structural filter

DIRECTIVE: to license a slot-split of observable values O₁/O₂ at the same nominal `(algebra, projector, pole)` triple, the proposer MUST produce a parameter scan demonstrating a DISCONTINUOUS jump in the observable identity at some finite parameter value. Continuous deformation FORBIDS the slot-split (the divergence is a methodology-floor F-image at the regulator-class axis per K=4 MANDATORY level-pin discipline); alternative regulator-class readings land as Level-2-B DIAGNOSTIC sub-rows, NOT independent §VII entries. Status: SUGGESTION K=1. Full detail: corpus §16.

### Diffusion-window-observable specialization (spectral-dimension comparisons)

DIRECTIVE: for a substrate-IS spectral-dimension observable `d_s(σ) = −2 d ln P(σ)/d ln σ` compared against an external dimensional-reduction reference (CDT / asymptotic-safety), fix the **(observable, diffusion-window) pair** on BOTH sides before any reduction verdict — `lim_{σ→0} d_s(σ)` (Weyl/MP manifold dimension) and `d_s(σ_*~1/E_0²)` (windowed) are DISTINCT functionals of the same `P(σ)` and may differ arbitrarily. Fair comparison applies the same functional `Φ` at the same scale-type; the discriminator is the directly-fitted energy-axis DOS exponent `γ_E`, with any impedance constraint `Z = ρ_E·v_g` a CONSISTENCY CHECK, not a lock. **K=2 (observable-identity axis)**: a criterion calibrated on `Φ_graph-Laplacian` is NOT transportable to `Φ_heat-trace` (distinct functionals); retire `min d_s < 3`, the van-Hove discriminator lives on the energy axis (`γ_E`). Status: SUGGESTION K=2. Full directive + K=1/K=2 corpus: §24.

## IS-not-IN Anatomy (5 elements)

Promotes the IS-not-IN convention (`phononic-framing.md §"IS Space, Not IN Space"`) from framing-rule to STRUCTURAL REQUIREMENT. Every entry MUST declare all five elements explicitly:

1. **Substrate-IS observable** — finite-L spectral-triple observable on `(A^{≤L}, H^{≤L}, D^{≤L})`. The substrate IS this observable.
2. **Laboratory-IN observable** — continuum measurement / sweep observable. The lab measures this quantity IN a continuum container.
3. **Bridge map** — explicit map between the two: HKR / K-theory boundary / Connes-Karoubi pairing (not "analogous" / "corresponds to").
4. **Algebraic envelope** — convergence rate `L^{-α}` bound.
5. **Empirical anchor** — numerical satisfaction at canonical L_max.

### Element 3 fiducial-anchor binding discipline

DIRECTIVE: when the bridge map composes a substrate-IS observable through a **pre-substrate pin P** that is itself a laboratory-IN observable at a different pillar, the entry MUST declare which incarnation of P binds — (i) **substrate-self-consistent** (P = framework prediction at the same algebra-axis family), (ii) **external-observation** (P = lab measurement at the different pillar), (iii) **joint-hypersurface** (lab discrimination is 2D in (P, observable) space). Undeclared binding → registry-incompleteness FAIL, plan-freeze HARD-HALT. Status: advisory K=1 (n_s pre-substrate-pin track). Full detail: corpus §10.

#### Bridge-map-scheme suffix discipline

DIRECTIVE: when the bridge map admits multiple scheme evaluations of the same secondary-class observable, Element 3 MUST carry one suffix tag on the verdict-line `convention=` field — `-APS-1975-secondary-class` (Atiyah-Patodi-Singer ρ-invariant), `-Cheeger-Simons` (full-leaf-foliation differential character), or `-Bismut-Cheeger` (adiabatic-limit η-form). Bare Element 3 (no scheme suffix) is FORBIDDEN under multi-scheme UNLESS structural-output-type independence (Reading A) is pre-established (e.g., `|GV_APS1975 − GV_Cheeger-Simons| < 1e-3` in M_KK² units + cite the scheme-INDEPENDENCE theorem). Enforcement: absent suffix on a multi-scheme entry → plan-freeze HARD-HALT. Status: MANDATORY at K=3 (axis-β). Audit: `_cross_pillar_bridge_audit.py` Element-3 binding subroutine, scheme-suffix verification. Positive/negative regex + calibration + MACHINERY-SCOPE cross-link: corpus §10.

### Element 2 OE-form discipline

DIRECTIVE: Element 2 (laboratory-IN observable) MUST be specified in OPERATOR-EXPRESSION form, not prose-only — (i) **integration domain** (`∫` over BZ / substrate-distance pole; degenerate `∑` for finite-rank Pillar V), (ii) **trace** (`Tr` / `Tr_{M_2(C)}` / etc.), (iii) **named projector** (`P_<index>` or `Π^{sup}_{sub}`; no generic bare `P`). Prose-only forms (`…measurement|spectroscopy|test`) FORBIDDEN. Legacy entries GRANDFATHERED with mandatory retrofit; new entries MUST satisfy the positive regex at plan-freeze. Status: MANDATORY (at plan-freeze). Audit: `_cross_pillar_bridge_audit.py` OE-form regex on Element-2 text within each bridge §-anchor block. Positive/negative regex + K=3 calibration: corpus §2.

## Cross-link to phononic-framing

This rule is the STRUCTURAL specialization of `phononic-framing.md §"IS Space, Not IN Space"` at the registry-anatomy level. When citing a cross-pillar bridge entry, the direction of explanation MUST flow:

```
Substrate (Pillar A) IS the [substrate-IS observable]
   → Bridge map (HKR / K-theory)
   → Laboratory (Pillar B) IN [laboratory-IN observable]
```

Inverting this direction (treating Pillar B as fundamental) is a container-thinking violation per `phononic-framing.md`.

## Per-Bulletin-per-pole Level-1 wall classification

DIRECTIVE: extends the Level-1/2/3 ladder to **intra-pillar** Pillar-VII (Mellin-cone) Bulletin-class entries, where the Level distinction operates over substrate-distance pole indices `s ∈ {3, 4, 5, …}` rather than pillar pairs. Status: advisory until K=3 (MANDATORY at cohomology-class-distinct K=3 AND pole-distinct K=3). Mapping table + full detail: corpus §8.

### Mapping (per-pole specialization)

Level 1 ↦ per-pole substrate-distance-IS spectral identity at the s-th pole; Level 2 ↦ per-pole truncation envelope `L^{-α(s)}`; Level 3 ↦ per-pole numerical anchor at L_max=10 OR analytic limit. Full table: corpus §8.

### Forward enforcement

Future Pillar-VII Bulletin entries MUST: (1) declare the substrate-distance pole index in the header; (2) give Level-1 classification (FI/RD/MIXED + rational/irrational/structurally-IRRATIONAL); (3) give Level-2 pole-specific `α(s)` with a Casimir-bound or Friedrich-Bär saturation argument; (4) give Level-3 at L_max=10 OR analytic limit.

### Per-pole-per-observable-class 4-tuple discipline

Each entry declares its 4-tuple `(pole_index, regulator-invariance ∈ {FI,RD,MIXED}, observable-class ∈ {algebra-INVARIANT, algebra-DEPENDENT}, layer ∈ {atlas-row, cache-moment, operational-machinery, dual-anchor-joint-hypersurface})`. Multi-tuple entries declare all positions + cross-tuple inheritance; cross-cell co-primary FORBIDDEN. Status: advisory until K=3. Full detail: corpus §8.

### Level-2 empirical-β verification rule

Level-2 `L^{-α}` verification MUST perform BOTH: (1) asymptotic Sage-Q regression at L ∈ [10, Friedrich-Bär cutoff / L=100 default] (the canonical envelope exponent); (2) in-cache log-log fit at canonical L_max (diagnostic). Declare both; if `|asymptotic − empirical|/asymptotic > 0.10`, cite the cache-ceiling effect + Friedrich-Bär saturation theorem. Status: advisory until K=3. Full detail: corpus §9.

### Scope distinction from cross-pillar bridges

Per-Bulletin-per-pole entries are intra-pillar: the 5-anatomy IS-not-IN elements are NOT mandatory at the same per-element granularity, but the Level-1/2/3 ladder IS preserved. Intra-Pillar-VII cross-pole bridges adopt the per-pole ladder for both poles plus a cross-pole identity layer.

## Forward template-adoption (5-anatomy + 3-level discipline)

### Hybrid Independence Test (K-counter advancement predicate)

An instance counts toward the K-counter iff `(i ∨ ii ∨ iii) ∧ iv`: (i) distinct substrate-IS pillar; (ii) distinct laboratory-IN pillar; (iii) distinct bridge-map class (HKR / Connes-Karoubi pairing / K-theory boundary); (iv) independent algebraic envelope (NOT a numerical refinement of an existing instance's envelope). Entries citing the discipline but failing the test are tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and recorded OUTSIDE the K-counter table. Status: advisory K=1. Full detail: corpus §3.

### Two-clause separation (registry-PASS vs K-counter advancement)

Two INDEPENDENT predicates (conflation is a `v3-closure-recovery.md` Class-3 PROHIBITED_ACTIONS adjacency): **per-entry registry-PASS** (`Level-3 < Level-2 at canonical L_max`) gates STAGE-3-PERMANENT promotion; **rule-level K-counter advancement** (3 Hybrid-Independence-Test-distinct calibration-LANDINGs) gates SUGGESTION → MANDATORY. An entry may be registry-INCOMPLETE under the first AND a valid calibration-LANDING under the second. The same separation applies to the parallel Algebra-axis orthogonality K-counter.

### Three forward bridge candidates

Pre-registered for dispatch: **FWD-C1** Pillar I ↔ Pillar II (n_s spectral-action ↔ Planck CMB); **FWD-C2** Pillar II ↔ Pillar V (Mellin-Barnes residue ↔ BdG spectral triple); **FWD-C3** Pillar IV ↔ Pillar V (substrate cocycle norms ↔ 3He-B / 3He-A observables). Per-candidate pre-registration blocks (substrate-IS/lab-IN IDs, bridge map, envelope, anchor target, inheritance-kernel rank): corpus §4.

### Rank-2 generalization

Candidates with `rank(ker ι_*) ≥ 2` MUST be designed under `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B"`. The cohomology-asymmetry test (Class B) MUST pre-register all `binomial(rank, 2)` cross-cocycle ratios with substrate-derived values + tolerance bands, complementing the kernel-signature tests (Class A; rows F_a returning NULL).

### Status

**MANDATORY at K=3** for the 5-anatomy + 3-level discipline. Full calibration corpus: corpus §5.

## Algebra-axis orthogonality K-counter (parallel discipline)

CONJECTURE: on any finite spectral triple `(A, H, D)` satisfying the 7 NCG axioms, the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership.

### Mandatory at plan-freeze

For any §VII entry on `(A_K, H_K, D_K)`, validators MUST verify:

1. **Corner-cell declaration** — entry declares its 4-corner cell ∈ {I, II, III, IV} per `permanent-results-registry.md §VII.U.2`.
2. **Cross-corner co-primary FORBIDDEN** — SOURCE-DOUBLE-CITE-CO-PRIMARY across distinct corner cells fails `registry-landing.md §"Detection"` criterion (1).
3. **Cross-pole co-primary FORBIDDEN** per `epistemic-discipline.md §"Pole-Scope sub-clause"`.
4. **Cross-corner cross-pole magnitude comparisons** FORBIDDEN as PASS/FAIL gates; narrative-only with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration.

Missing any of (1)-(4) → registry-incompleteness FAIL, plan-freeze HARD-HALT via `_corner_classification_audit.py`.

### Status

**MANDATORY at K=3**. NCG-axiomatic structural-theorem proof queued as Stage-1-Candidate per `joint-theorem-promotion.md`. Full corpus + axiomatic derivation: corpus §6.

### Observable-Naming-History vs Parse-Tree-Structure (sub-clause)

DIRECTIVE: state-history labels (`n_a^GGE`, `GGE-state`, `Bogoliubov(…)`, `α_s_canonical`, `α_s_route_N`, `Δ_M`, etc.) encode experimental/thermodynamic history, NOT structural form on the substrate algebra — corner classification operates on **parse-tree STRUCTURE** per `permanent-results-registry.md §VII.U.2` clause (e). §VII entries citing state-historic observables MUST declare a parse-tree expansion block. Enforcement: `_registry_landing_audit.py` regex-detects the state-history label set; if a label matches AND a parse-tree expansion block is absent → `MISSING-PARSE-TREE-EXPANSION` at S2 advisory, halting plan-freeze. Status: advisory K=2. Full label pattern set + calibration: corpus §13.

### Within-cell discriminator axes (α/β/γ/δ)

When multiple candidate observables parse to the SAME corner cell, four pairwise-independent within-cell axes apply: (α) K-theoretic vs representation-theoretic; (β) source-side vs target-side; (γ) primary corridor (b) vs auxiliary corridor (c); (δ) evaluator-trace-layer vs K_0-rank-layer. Status: SUGGESTION K=1. Per-axis definitions + composition: corpus §17.

## Audit at plan-freeze

`computations/_shared/_cross_pillar_bridge_audit.py` verifies these conditions; missing elements return diagnostic FAIL.

**For ALL cross-pillar bridge entries**:

1. All 5 IS-not-IN anatomy elements present in entry text.
2. All 3 level markers (Level 1 / Level 2 / Level 3) present with explicit values.
3. Level 3 numerical value < Level 2 envelope at canonical L_max.
4. Bridge map explicitly named (HKR / K-theory boundary / Connes-Karoubi pairing — not "analogous" or "corresponds to").
5. Level-2 envelope sub-class explicitly declared (binding OR non-binding); REJECTED at HARD-HALT if non-binding.
6. If Level-2-binding declared, bridge map citation MUST be explicit.
7. If `rank(ker ι_*) ≥ 2`, cross-reference to `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B"` present.

**For new entries (forward template-adoption)**:

8. Bridge label maps to {FWD-C1, FWD-C2, FWD-C3} OR declares a new candidate ID.

**For Pillar-VII Bulletin-class entries (per-pole sub-section)**:

9. Substrate-distance pole index explicitly declared in Bulletin header.
10. Level-1 classification per the per-pole form (FI/RD/MIXED + rational/irrational/structurally-IRRATIONAL).
11. Level-2 envelope cites pole-specific `α(s)` AND Casimir-bound or Friedrich-Bär saturation argument.
12. Level-3 anchor at canonical L_max=10 OR analytic limit.

## Forward-looking convention-pin

Forward-looking. Any future cross-pillar bridge candidate MUST adopt this anatomy; entries lacking the anatomy are registry-incomplete and route to plan-freeze HARD-HALT.

## Composite Bridge-Map Dimensional-Class Admissibility

DIRECTIVE: a COMPOSITE bridge map `B = f⊙g` (Element 3) at substrate-distance pole `s>0` on `(A_K, H_K, D_K)`, with canonical Level-3 anchor of homogeneity degree `d_A`, is **admissible** iff BOTH conjuncts hold — **Conjunct 1 (homogeneity)**: `deg(B) = d_A` (a Wodzicki-trace factor carries `−2s ≠ 0` by Wodzicki uniqueness; an HKR cohomology-class ratio carries `0`; `d_τ(s) = −2s` is index-rigid, no pole `s>0` has `d_τ→0`); **Conjunct 2 (substrate-natural-binding)**: `B` carries non-trivial L_max-dependence surviving the dimensionless ratio (a canonical-import *scalar* is VACUOUS — it cancels in the ratio). The conjunction is irreducible. Operational test: scheme-spread `Δ_scheme(B) → machine-zero` across {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger} (secondary-class axis ONLY, not the orthogonal UV-regulator RD axis). **Forward-design rule**: any FWD-C1/C2/C3 composite candidate MUST declare `deg(Element-1-composite)` and `deg(Element-5-anchor)` at plan-freeze and verify they match AND the matching morphism is non-scalar — a scalar corrector is a Class-8 PRU defect detectable before compute. Status: SUGGESTION K=1 (→ MANDATORY at K=3). Audit: `_cross_pillar_bridge_audit.py::detect_composite_bridge_map_taxonomy` (S2 advisory; NOT HARD-HALT). Five-formulation taxonomy (T1–T5) + sub-question verdicts + downstream consumers: corpus §18.

### Per-observable transport-degree scale-separation

DIRECTIVE: each substrate-IS spectral functional `O ∈ {n_s, r, n_T, α_s, …}` has a substrate-scale value `O(M_KK)` (inside the BZ) and a CMB-pivot image under the composite bridge map `T_{BZ→pivot} ⊙ (HKR ∘ Connes-Karoubi)`; the two coincide iff `deg(T_{BZ→pivot})` is the T2-VACUOUS scalar case (a 54-decade unit conversion cancelling in the dimensionless observable), and differ iff the transport is a substrate-natural NON-SCALAR morphism. The substrate=pivot vs substrate≠pivot verdict IS the §VII.BA five-formulation taxonomy verdict on the transport factor. Status: SUGGESTION K=2 (instances n_T, α_s). Full directive + K-counter corpus: §23.

DIRECTIVE (dimensional-class indexing + parity selection rule; S110 W4; SUGGESTION at K=2): the per-observable transport degree is INDEXED by the observable's mass dimension `d_A` via `B = (M_KK^{d_A} scale leg) ⊙ (dimensionless morphism)` — `d_A=0` ⇒ the trivial `M_KK^0=1` scale leg, transport degree carried entirely by the dimensionless morphism (scalar T2-VACUOUS, or substrate-natural NON-SCALAR); `d_A=1` ⇒ the non-trivial `M_KK^1` scale leg carries the 54.04-decade unit conversion (`deg=+1`). PARITY: the morphism sector is EVEN-degree (`−2(s−s')` Wodzicki ratios, `0` HKR); the only ODD-degree carrier is the `M_KK^1` scale leg, so every `d_A=odd` observable is forced onto the sign-locked odd scale leg with no even-degree morphism able to correct it (the two `Q=R·M_KK^m` halves are parity-separated). This is a DIRECTIVE EXTENSION of the per-observable transport-degree theorem, NOT a K-counter advancement — §23 stays SUGGESTION K=2 (the K=3 slot remains reserved for an independently factorization-EXTRACTED new-observable degree, r/α_t). Full directive + derivation: corpus §23.0(5).

## Workshop-Campaign Forward-Directive Mirrors (§VII.AX / §VII.AV / §VII.AY)

### Registry-PASS criterion — Level-3 annotation discipline

DIRECTIVE: a registered Level-3 row's PASS verdict is governed SOLELY by the central-value criterion `Level-3 < Level-2 at canonical L_max`. Descriptive 1σ-band / edge-containment statements are NON-LOAD-BEARING annotations and MUST NOT be read as PASS predicates; a band-containment gate STRONGER than central-value MUST be pre-registered as a Class-8.2 verifier-rubric criterion AND is admissible ONLY for a substrate-IS or laboratory-IN PHYSICAL band that survives L_max→∞ — a Friedrich-Bär (or any) TRUNCATION-uncertainty envelope can NEVER be credentialed as a PASS gate (it would let a methodology-floor F-image veto a substrate-IS structural PASS). Audit-mirror: Class-(i) `INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT` at `registry-landing.md`. Status: SUGGESTION K=1. Full directive + corpus: §20.

### Algebra-axis orthogonality K-counter — Regulator-behavior sibling discriminator

DIRECTIVE: on `(A_K, H_K, D_K)`, an algebra-DEPENDENT state-pair functional on a GAPPED occupation distribution is regulator-INVARIANT (IR-self-regularized by the gap `|Δ_a|`); an algebra-INVARIANT spectrum-only functional is regulator-DEPENDENT (`O(heat-kernel moment-ratio spread) ≈ O(20%)`). This is a SIBLING discriminator of the algebra-axis orthogonality conjecture on an axis ORTHOGONAL to parse-tree-membership (regulator-RESPONSE vs parse-tree); INDEPENDENT per Hybrid-Independence-Test criterion (iv); NOT folded into the parse-tree K-counter. Status: SUGGESTION K=1. Full directive + K=1 corpus + 2-bit `L_max`-FLAT-vs-`m_PV`-FLOWING fingerprint: §22.

### Element-5 — Class-8.3 publication-precision extension

DIRECTIVE: an Element-5 anchor published at `n` sig figs MUST set its Stage-2/Stage-3 verifier tolerance RELATIVE at `rel_tol ≥ 10^(−sig_figs_of_agreement)`; a floor-level PASS that cannot discriminate the anchor's candidate F-images MUST carry a `canonical-value-question-DEFERRED-to-<substrate-recompute-CF>` tag; Stage-3 separates into ELIGIBILITY (tolerance fix) vs STAGE-3-PERMANENT (re-pin to the bit-exact substrate canonical). Primary directive home: `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"`. Status: SUGGESTION K=1. Full directive + K=1 corpus: §21.

## Calibration corpus + K-counter status (pointers)

Master lookup index. Each row maps a directive above to its corpus section and current enforcement status. The corpus section is authoritative for taxonomy, tables, derivations, regex, worked examples, and per-instance landings.

| Rule sub-section | Corpus location | Current status |
|:-----------------|:----------------|:---------------|
| Level-2 sub-class (binding vs non-binding) | corpus.md §1 + §7 | SUGGESTION K=2 |
| Deferred-pending intermediate verdict-class | corpus.md §1 + §14 | SUGGESTION K=2 |
| Element 2 OE-form discipline | corpus.md §2 | MANDATORY (at plan-freeze) |
| Hybrid Independence Test | corpus.md §3 | advisory K=1 |
| Three forward bridge candidates (FWD-C1/C2/C3) | corpus.md §4 | forward SUGGESTION |
| 5-anatomy + 3-level discipline (K=3 corpus) | corpus.md §5 | MANDATORY at K=3 |
| Algebra-axis orthogonality K-counter | corpus.md §6 | MANDATORY at K=3 |
| Element 3 fiducial-anchor binding (n_s pre-substrate-pin track) | corpus.md §10 | advisory K=1 |
| Bridge-map-scheme suffix discipline (axis β) | corpus.md §10 | MANDATORY at K=3 |
| Per-Bulletin-per-pole Level-1 classification | corpus.md §8 | MANDATORY cohomology-class-distinct K=3 AND pole-distinct K=3 |
| Level-2-A vs Level-2-B audit-axis | corpus.md §9 | advisory K=1 |
| Substrate-input-orthogonality (Stage-2 ceiling) | corpus.md §11 | advisory K=1 |
| Cross-reviewer audit-machinery self-citation | corpus.md §12 | advisory K=1 |
| Observable-Naming-History vs Parse-Tree-Structure | corpus.md §13 | advisory K=2 |
| FOUR-rule cross-composition meta-pattern | corpus.md §14 | SUGGESTION K=1 |
| Level-3 anchor singleness sub-clause | corpus.md §15 | SUGGESTION K=1 |
| Single-observable-per-triple structural filter | corpus.md §16 | SUGGESTION K=1 |
| Within-cell discriminator axes (α/β/γ/δ) | corpus.md §17 | SUGGESTION K=1 |
| Composite Bridge-Map Dimensional-Class Admissibility | corpus.md §18 | SUGGESTION K=1 |
| Level-3 annotation discipline (Registry-PASS criterion) | corpus.md §20 | SUGGESTION K=1 |
| Element-5 publication-precision extension (Class-8.3) | corpus.md §21 | SUGGESTION K=1 |
| Regulator-behavior sibling discriminator (algebra-axis) | corpus.md §22 | SUGGESTION K=1 |
| Per-observable transport-degree scale-separation | corpus.md §23 | SUGGESTION K=2 |
| Diffusion-window-observable specialization (spectral-dim) | corpus.md §24 | SUGGESTION K=2 |
| Tier-1/Tier-2 dimensional-re-anchorability gate (Registry-PASS) | corpus.md §25 | SUGGESTION K=2 |
| Non-Promotion-by-Held-Number Meta-Taxonomy | corpus.md §26 | SUGGESTION K=1 |
