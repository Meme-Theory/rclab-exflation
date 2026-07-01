# Atlas D11: Cross-Pillar Bridge Corpus

**Sessions covered**: S86 W-5 (rule origin) — S88 W-25 (MANDATORY-K=3 corpus + Hybrid Independence Test K=1 + Per-Bulletin-per-pole K=3 cohomology-class-distinct); S89–S118 currency reconcile in §XIV
**Updated**: 2026-07-01 (S89-S118 currency reconcile; S119-current). The 5-anatomy + 3-level discipline below is FROZEN at S88 and remains current; the ~45 §VII bridge/obstruction landings S89–S118 (slots AU→CK) extend the calibration set and are cataloged in atlas-07 §XVI + `sessions/framework/registry/cross-pillar-bridge-corpus.md`, summarized in §XIV.
**Companion atlas (methodology-side)**: `atlas-12-methodology-floor.md`
**Source rule**: `.claude/rules/cross-pillar-bridge-anatomy.md` (323 lines; rule body)
**Source corpus**: `sessions/framework/registry/cross-pillar-bridge-corpus.md` (per-instance corpora)
**Joint-theorem cross-link**: `.claude/rules/joint-theorem-promotion.md` (Stage-2 cross-axis verify)
**Inheritance cross-link**: `.claude/rules/inheritance-falsifier-protocol.md` (rank-2 ker(ι_*) protocol)

This atlas is the human-readable narrative of the cross-pillar bridge corpus — substrate-IS observables connected to laboratory-IN observables via explicit bridge maps, organized as a structural-confidence hierarchy. Atlas-11 catalogs CONTENT (the bridge instances); atlas-12 catalogs DISCIPLINE (the methodology rules that govern admission). The two are STRUCTURALLY ORTHOGONAL per the algebra-axis K-counter MANDATORY clause; cross-corner co-primary between them is FORBIDDEN.

---

## I. Introduction — what is a cross-pillar bridge?

A **cross-pillar bridge theorem** connects a substrate-IS observable on one pillar (one finite-L spectral-triple structure) to a laboratory-IN observable on a different pillar (continuum measurement / sweep observable on a different platform). The substrate IS the observable on `(A^{≤L}, H^{≤L}, D^{≤L})`; the laboratory IN measures a continuum image; the bridge map is HKR / K-theory boundary / Connes-Karoubi pairing.

**Direction of explanation** (`cross-pillar-bridge-anatomy.md:160-168`):

```
Substrate (Pillar A) IS the [substrate-IS observable]
   → Bridge map (HKR / K-theory)
   → Laboratory (Pillar B) IN [laboratory-IN observable]
```

Inverting this direction (treating Pillar B as fundamental and Pillar A as derived) is a container-thinking violation per `phononic-framing.md` §"IS Space, Not IN Space". The bridge anatomy makes the direction explicit at the registry-entry level so that downstream citations cannot drift.

**Why a corpus matters**: cross-pillar bridges are the most leverage-sensitive failure mode in the framework — substrate ↔ laboratory conflation inverts the structural priority of the spectral triple. The K=3 MANDATORY discipline (S88 W4a-17 close, 2026-05-04) makes the 5-anatomy + 3-level ladder a pre-registration requirement at plan-freeze. Three distinct calibration LANDINGs survived the saturation: one PASS (`§VII.AF.1`, S87 W5-1), one REGISTRY-FAIL (W11-5, S87), one STAGE-1-CANDIDATE (`§VII.W-3.LAB`, S88 W4a-17). That triplet IS the corpus this atlas catalogs.

The S86 W-5 substrate workshop (`sessions/archive/session-86/workshops/s86-hp1-cohomology-quantum-metric-bridge.md`, 2-agent volovik × connes 3-round 6-turn iterative; lizzi DROPPED with T6 anchor + Mellin Corollary E carried by connes) is the structural seed. R3-α and R3-β rounds produced both the 3-level ladder and the 5-element IS-not-IN anatomy as RULE-1 + RULE-2 of the workshop. This atlas inherits BOTH.

---

## II. The 5-element IS-not-IN anatomy

Future cross-pillar bridge theorems MUST declare ALL five anatomy elements explicitly. Bare entries lacking any element are registry-incomplete and route to plan-freeze halt.

### Element 1 — Substrate-IS observable

Finite-L spectral-triple observable on `(A^{<=L}, H^{<=L}, D^{<=L})`. The substrate IS this observable; it is not "in" any container. Calibration (W-5): finite-L Hochschild pairing `R_universal` evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`.

### Element 1 fiducial-anchor binding discipline (S88 W-15 W15-V.7; K=1 advisory)

When the bridge map composes a substrate-IS observable through a **pre-substrate pin P** that is itself a laboratory-IN observable at a different pillar, the bridge entry MUST declare which incarnation of P is binding: (i) **substrate-self-consistent** (P = framework prediction at the same algebra-axis family); (ii) **external-observation** (P = laboratory measurement at the different pillar); (iii) **joint-hypersurface** (lab discrimination is 2D in (P, observable) space rather than 1D in observable space alone). Conflation-with-undeclared-binding is a registry-incompleteness FAIL routing to plan-freeze halt. K=1 calibration: S88 W-15 W4c-36 + W5a-44 V.4 — n_s as pre-substrate pin in the bridge map for the α_s-canonical observable; reading-difference between (i) and (ii) is 15× the substrate's own combined falsification band.

### Element 2 — Laboratory-IN observable

Continuum measurement / sweep observable. The laboratory measures this quantity IN a continuum geometric container. Calibration (W-5): Pillar IV continuum BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Peotta-Törmä superfluid-stiffness / quantum-metric integrated trace).

### Element 2 OE-form discipline (S88 W7a-73; K=2 calibration corpus)

Element 2 MUST be specified in OPERATOR-EXPRESSION form (OE-form), NOT prose-only:

- **(i)** integration domain (`∫` over BZ for Pillar IV; `∫` over substrate-distance pole for Pillar II; degenerate `∑` for finite-rank Pillar V where integral reduces to sum)
- **(ii)** trace over substrate algebra (`Tr` over `A`, `Tr_{M_2(C)}` over BdG sub-algebra, etc.)
- **(iii)** named projector `P_<index>` or `Π^{<superscript>}_{<subscript>}` (no generic `P`)

**Positive-match regex**: `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)`. Π-notation admitted as P-equivalent. Finite-rank Pillar V degenerate cases use extended regex `(\int|\sum).*Tr.*\([ΠP]_[a-z0-9_-]+\)`.

**Negative-match (FORBIDDEN)**: prose Element 2 specifications ending in "measurement"/"spectroscopy"/"test" without OE-form. K=2 calibration corpus: W-5 §VII.W positive (`R_geom = ∫_BZ Tr g_ab^{(P_0)}(k)`); W11-5 FAIL pre-retrofit (Caroli-Matricon prose-only; required §W7a-75 retrofit to `Π^{vortex}_{B-phase}` + `Π^{µSR}_{A-phase}`).

### Element 3 — Bridge map

Explicit map between substrate and laboratory: HKR (Hochschild-Kostant-Rosenberg) / K-theory boundary / Connes-Karoubi pairing. Bridge map MUST be explicitly named (not "analogous to"/"corresponds to"). Calibration (W-5): `L_max → ∞` HKR image identifying finite-L Hochschild pairing with continuum BZ-trace.

### Element 4 — Algebraic envelope

Convergence rate `L^{-α}` bound on how the substrate-IS image approaches the laboratory-IN image. Calibration (W-5): `L^{-3}` envelope at d=4 (predicted 0.10% at L_max=10).

### Element 5 — Empirical anchor

Numerical satisfaction at canonical L_max. Calibration (W-5): `0.0095%` F_4 strict at L_max=10 (`10×` inside Level-2 envelope; Sage-QQ `r = 19/200`).

---

## III. The 3-level structural-confidence ladder

Every cross-pillar bridge entry MUST declare all three levels explicitly. Each level has a distinct epistemic role.

### Level 1 — Substrate-IS Structural Identity (cohomology-class level)

- **Status**: STRUCTURAL THEOREM
- **Properties**: regulator-invariant; L-independent; holds at every L_max
- **Form**: identity at the cohomology-class / K-theory pairing / spectral-triple-axiom level
- **Calibration (W-5)**: `‖[ε_H]‖_{HP^1, r} = |f_4^r| · R_universal` where `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` is the regulator-invariant Connes-Karoubi pairing on the Jensen-deformed band-0 projector (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula)

### Level 2 — Algebraic Convergence Envelope

- **Status**: STRUCTURAL PREDICTION
- **Properties**: L_max-dependent; algebraically derived; refines with L-scan
- **Form**: bound on convergence rate to continuum / laboratory image
- **Calibration (W-5)**: `L^{-3}` algebraic envelope at d=4; predicted 0.10% at L_max=10

### Level 3 — Empirical Anchor at Canonical L_max

- **Status**: EMPIRICAL CONFIRMATION
- **Properties**: numerical evaluation at canonical truncation
- **Form**: numerical value satisfying the Level 2 envelope
- **Calibration (W-5)**: empirical W5-6 atlas match `0.0095%` (F_4 strict) at L_max=10 — `10×` inside Level 2 envelope (match/envelope = `0.0950 = 19/200` Sage-QQ exact)

### Level-2-A vs Level-2-B coverage (S88 W4a-17 V.3; K=1 advisory)

Level-2 envelopes admit two orthogonal audit axes:

- **Level-2-A** (operational content; transit-dynamics axis): envelope derived from operational machinery on the laboratory-IN side (Bogoliubov / parametric-resonance / Kibble-Zurek scaling). Audit role: Stage-2 cross-reviewer-B.
- **Level-2-B** (regulator-invariance; spectral-functional axis): envelope derived from substrate-IS spectral-functional regulator-invariance (`L^{-α}` envelope inherited from regulator-class-INVARIANT identity). Audit role: Stage-2 cross-reviewer-A.

For structural-exact Level-2 envelopes (algebraically derived rather than empirically fit), BOTH audits MUST PASS at Stage-2.

### Registry-PASS criterion

```
Level-3 empirical value  <  Level-2 envelope value  at canonical L_max
```

If Level 3 violates Level 2, the bridge theorem entry FAILs registry-PASS. If a level is missing, the entry is registry-INCOMPLETE.

**Substitution chain** (Sage-QQ verified 2026-05-09):

- Definition 1: `L3 := empirical match at L_max=10 = 0.0095% = 95/1000000`
- Definition 2: `L2 := algebraic envelope at d=4, L_max=10 = 10⁻³ = 1/1000`
- Substitute: `r := L3 / L2 = 95/1000 = 19/200`
- Simplify: `19/200 = 0.0950` (Sage-exact)
- Direction: `r = 0.0950 < 1` ⇒ Level-3 PASSes Level-2 with margin `200/19 ≈ 10.5263×` inside

### Level-2-binding vs Level-2-non-binding (S88 W8-88; sub-class taxonomy)

Provenance: gen-physicist orchestrator PRIMARY; CO-AUTHOR connes-ncg-theorist for cohomology-class-binding rationale review per Connes-Moscovici 1995 §III.4. Closes the bare-decomposition envelope false-PASS pathway by construction.

- **Level-2-binding (admissible for registry-PASS)**: envelope `L^{-α}` is convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally bounds `‖HKR(c_L) − c_continuum‖`. Calibration: W-5 `L^{-3}` at d=4 (HKR identifies Hochschild pairing with BZ-trace). Calibration #2 (W3b-15 KDE Sub-test B, S88 W-11 V.3): `L^{-α}` envelope on W3b-15 KDE Sub-test B observable IS Level-2-binding by HKR-image construction.

- **Level-2-non-binding (FORBIDDEN for registry-PASS)**: envelope `L^{-α}` is bare-decomposition convergence rate that does NOT bind Level-1. Operationally bounds `‖c_L − c_∞‖` where `c_∞` is substrate-internal limit (e.g., bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable. Counter-example pattern: `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map.

**Enforcement** (`cross-pillar-bridge-anatomy.md:61-65`):
- IF Level-2-binding ∧ (Level-3 < Level-2 envelope) → registry-PASS ELIGIBLE
- IF Level-2-non-binding (regardless of numerical comparison) → registry-INELIGIBLE; routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum`
- IF Level-2 sub-class undeclared → registry-INCOMPLETE; plan-freeze halt

---

## IV. K=3 MANDATORY corpus — the calibration instances

The K=3 corpus that promoted the rule from SUGGESTION to MANDATORY at S88 W4a-17 close (2026-05-04). Three structurally-distinct LANDINGs satisfy the Hybrid Independence Test (i ∨ ii ∨ iii) ∧ iv.

**Promotion rationale**: a single calibration instance does not exhibit cross-context stress-testing. K=3 forces three structurally-distinct workshops to instantiate the anatomy before edge cases are saturated; premature MANDATORY would lock in W-5-specific accidents (e.g., L^{-3} is d=4-specific; future bridges at d ≠ 4 may require different α).

### Instance #1 (K=1, LANDED PASS): §VII.AF.1.OP-PROJ — Pillar III ↔ Pillar IV Bridge Theorem

- **Provenance**: S86 W-5 (volovik PRIMARY + connes CO-AUTHOR); LANDED S87 W5-1 as `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` (audit_sha256=`5775770d2e01617e...`, content_sha256=`1a321c5bb2c04e8d...`); suffix-retrofit S88 W11 V.4 per Operator-Projection Reading-A naming hygiene.
- **Theorem text** (verbatim from W-5 workshop L2391, registry line 14704):
  > "Pillar III HP^1 cohomology norm factorizes as `‖[ε_H]‖_{HP^1, r} = |f_4^r| · R_universal`, where `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` is the regulator-invariant Connes-Karoubi pairing on the Jensen-deformed band-0 projector. Substrate IS the finite-L Hochschild pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; laboratory child realization measures the L_max → ∞ HKR image as the continuum BZ-trace `∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`. Convergence bounded by `L^{-3}` algebraic envelope at d=4 (predicted 0.10% at L_max=10); empirical W5-6 atlas match 0.0095% F_4 strict (10× inside envelope; Atlas_5 loose 0.0000% exactly)."

- **5-element anatomy**:
  1. Substrate-IS: finite-L Hochschild pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`
  2. Laboratory-IN: `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Peotta-Törmä quantum-metric trace)
  3. Bridge map: HKR `L_max → ∞` (explicit name; not "analogous")
  4. Algebraic envelope: `L^{-3}` at d=4
  5. Empirical anchor: `0.0095%` F_4 strict at L_max=10 (Sage-QQ `r = 19/200`)

- **Anchor structure**: SOURCE-DOUBLE-CITE-CO-PRIMARY. ANCHOR-1 (V_input, volovik): 3He-B BdG sector finite-L Hochschild pairing. ANCHOR-2 (C_output, connes): Connes-Karoubi pairing + HKR `L_max → ∞` bridge. Neither anchor stands alone (V alone has no laboratory-IN image; C alone has no finite-L domain).

- **Hybrid Independence Test verdict**: BASELINE (calibration #1; the test is anchored at this instance).

### Instance #2 (K=2, REGISTRY-FAIL): W11-5 — Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess)

- **Provenance**: S87 W11-5 (volovik PRIMARY); REGISTRY-FAIL.
- **Substitution chain** (Sage-QQ verified):
  - L3 = 1029/1000 (Level-3 ratio_mismatch)
  - L2 = 1/20 (Level-2 envelope)
  - ratio = L3/L2 = 1029/50 = 20.58
  - Direction: 20.58 ≫ 1 ⇒ Level-3 VIOLATES Level-2 by 20.58× (registered as ~21×)

- **Structural cause**: M_3(C) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin scheme. Inheritance theorem at S86 W1b-T8 PRESERVED (FAIL is observable-construction-specific, NOT bridge-map-defective). Carry-forward: `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`.

- **Why instance #2 advances K-counter despite REGISTRY-FAIL**: per `cross-pillar-bridge-anatomy.md:279-295` (Two-clause separation: registry-PASS vs K-counter advancement). The K-counter advances on STRUCTURAL distinctness under Hybrid Independence Test, not on per-entry empirical adequacy. W11-5 is structurally distinct from §VII.AF.1 (substrate-IS pillar = IV vs III; laboratory-IN pillar = V vs IV; bridge map class = inheritance morphism + (Δ_B/Δ_A)^p vs HKR `L_max → ∞`); it satisfies (i) ∨ (ii) ∨ (iii) AND (iv). The empirical FAIL-by-21× CLOSES a corridor in solution space but does NOT invalidate the bridge-map structural integrity.

### Instance #3 (K=3, STAGE-1-CANDIDATE): §VII.W-3.LAB — Substrate Cocycle-Ratio Preservation Under χ Inheritance Morphism

- **Provenance**: S88 W4a-17 (volovik PRIMARY + connes + mack co-authored); LANDED 2026-05-04; STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. Stage-2 two-agent cross-axis independent-verify deferred to multi-year experimental cycle (Lancaster MCT-3 + RHUL/Aalto LTL 2027-2030 horizon).

- **5-element anatomy**:
  1. **Substrate-IS observable**: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) finite-spectral-triple algebra + substrate cocycle pair (φ_67, φ_88) with **ratio 7.324992 = 114453/15625** (Sage-QQ exact; canonical_constants.py `substrate_cocycle_ratio_67_88`; S86 W-5 R2-B Convergence #3 + R2-A EMERGENCE #2). The substrate IS the rank-2 cocycle pair in ker(ι_*).
  2. **Laboratory-IN observable**: 3He-B vortex-core Caroli-Matricon ladder asymmetry (W11-C5; Lancaster MCT-3 / Helsinki ROTA cells) AND 3He-A µSR chirality discrimination (W11-C6; RHUL/Aalto LTL); supporting F2/F3/F4 channels + decisive triplet F1+F2+F5 + Gate-2 cohomology-asymmetry test.
  3. **Bridge map**: inheritance morphism `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (M_3(ℂ) → 0; BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor. Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual at machine precision) preserves substrate-derived ratio ‖φ_67‖/‖φ_88‖ = 7.324992 INTACT under common-exponent (Δ_B/Δ_A)^p rescaling.
  4. **Algebraic envelope (Level 2)**: cohomology-asymmetry test ratio preservation **7.3250 ± 0.1%** (S86 W-5 Gate-2 pre-registered band; structural-exact form, NOT L^{-α} convergence — replaces L_max-dependent envelope for inheritance-morphism class).
  5. **Empirical anchor (Level 3)**: S88+ Lancaster MCT-3 vortex-core spectroscopy + RHUL/Aalto LTL µSR run delivering NULL on F1+F2+F5 + ratio 7.3250 ± 0.1% on any non-NULL detection (4-gate falsifier protocol per `inheritance-falsifier-protocol.md`). MULTI-YEAR experimental cycle blocking Stage-3 promotion.

- **Inheritance kernel rank**: rank(ker ι_*) = 2 (φ_67 chiral pair + φ_88 Cartan hypercharge) — directly invokes `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` rank-2 case.

- **Stage-2 cross-axis pre-registration**:
  - Axis A: connes-ncg-theorist on NCG-axiomatic axis (KO-dim=6, A0 ∧ M2 axiom verification; χ kernel structure)
  - Axis B: lizzi-spectral-functional-theorist on spectral-functional axis (cocycle ratio under regulator class change; HP^1 cohomology stability)
  - Both dispatched WITHOUT prior workshop context; joint clauses PASS-AND across both verdicts
  - Forward gate ID: `S88-OR-LATER-VII-W-3-LAB-INDEPENDENT-VERIFY`

- **Why instance #3 advances K-counter despite Level-3 DEFERRED**: Calibration corpus instance #3 extends to a Level-3-DEFERRED case: the entry has no Level-3 numerical value yet (multi-year experimental cycle), is correctly flagged STAGE-1-CANDIDATE per `joint-theorem-promotion.md` Stage 1 of 4, AND counts as calibration instance #3 toward the K-counter.

---

## IV.B — Hybrid Independence Test (axis-distinctness × original-authoring-exclusion × audit-coverage)

The structural discriminator deciding which calibration corpus instances count toward K-counter advancement. Source: `cross-pillar-bridge-anatomy.md:252-273`; `cross-pillar-bridge-corpus.md §3`.

**Predicate**: A calibration corpus instance counts toward the K-counter iff `(i ∨ ii ∨ iii) ∧ iv`:

- **(i)** distinct substrate-IS pillar from prior K-instances (Pillar I / II / III / IV / V / VI / VII)
- **(ii)** distinct laboratory-IN pillar from prior K-instances
- **(iii)** distinct bridge map class (HKR / Connes-Karoubi pairing / K-theory boundary) from prior K-instances
- **(iv)** independent algebraic envelope (the Level-2 envelope is NOT a numerical refinement of an existing K-instance's envelope — refinements that share the same regulator-invariant structural form do NOT count as independent)

The **disjunction `(i ∨ ii ∨ iii)`** captures structural diversity along ANY of the three substrate-axis-/-lab-axis-/-bridge-axis dimensions; the **conjunction with (iv)** enforces that the algebraic envelope itself is structurally independent — purely numerical refinements do NOT advance K, even on different §VII slots.

### Companion-entry tagging (retroactive)

Registry entries that cite the 5-IS-not-IN + 3-level discipline but FAIL the Hybrid Independence Test are formally tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and recorded OUTSIDE the K-counter table. They retain full registry-entry status (the bridge-anatomy declaration remains valid) but do NOT advance K toward the K=3 MANDATORY threshold.

### Worked example: §VII.AG.1 retroactive companion-tagging

Five-step Hybrid Independence Test on §VII.AG.1 (S87 W6-1 CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY):

- **Step 1** (Definition): K-counter advancement threshold = N=3 promotion to MANDATORY per `feedback_rules-compensate-missing-structure.md`.
- **Step 2** (Definition): "Distinct calibration instance" PRE-Hybrid-Independence-Test = each §VII registry entry citing the 5-IS-not-IN + 3-level discipline naively counted as one K-instance.
- **Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv`):
  - §VII.AG.1 substrate-IS pillar = Pillar III (T7 quotient on Jensen-deformed band-0 sector); §VII.AF.1 W-5 substrate-IS pillar = Pillar III. **MATCH ⇒ clause (i) FAILS.**
  - §VII.AG.1 laboratory-IN pillar = Pillar IV (S67 cyclic-fold image); §VII.AF.1 W-5 laboratory-IN pillar = Pillar IV. **MATCH ⇒ clause (ii) FAILS.**
  - §VII.AG.1 bridge map = HKR `L_max → ∞` modulo cyclic-fold V_4 (a quotient-functor REFINEMENT of W-5's HKR map); §VII.AF.1 W-5 bridge map = HKR `L_max → ∞`. The cyclic-fold V_4 quotient is a refinement of the same HKR class, not a structurally distinct bridge map class. **REFINEMENT-NOT-INDEPENDENT ⇒ clause (iii) FAILS.**
  - Disjunction `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`.
- **Step 4** (Simplify): Conjunction `FALSE ∧ iv = FALSE` regardless of clause (iv). §VII.AG.1 fails the Hybrid Independence Test.
- **Step 5** (Direction): K-counter does NOT advance for §VII.AG.1; therefore §VII.AG.1 is OUTSIDE the K-counter and gets the retroactive tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`. The K-counter advancement at S87 W6-1 close was naive narrative inflation that the Independence Test now formally excludes.

**Status**: SUGGESTION at K=1 (S88 W8-87 baseline). Forward enforcement: plan-freeze halt on any S88+ K-counter advancement that does not document a per-clause Hybrid Independence Test verdict. The K-counter K=1 in this section refers to the calibration-corpus state UNDER the Hybrid Independence Test as a stand-alone discipline; it does NOT supersede the K=3 MANDATORY corpus in §IV (post-W4a-17 K=3 advancement IS consistent with the Test: W-5, W11-5, W4a-17 each satisfy `(i ∨ ii ∨ iii) ∧ iv`).

---

## V. Sub-class taxonomy: Level-2-binding vs Level-2-non-binding (full content)

Promoted from §III (overview) to its own section because the binding-vs-non-binding distinction drives the false-PASS pathway for bare-decomposition envelopes. See §III for definitions; this section documents the substitution chain and calibration corpus.

**5-step substitution chain** (`cross-pillar-bridge-corpus.md §1`):

- **Step 1 (definition)**: HKR : HH^*(A^{≤L}) → H^*_{dR}(continuum-image) is the Hochschild-Kostant-Rosenberg map. It maps periodic Hochschild cohomology of the finite-L spectral algebra to de Rham cohomology of the continuum image.
- **Step 2 (definition)**: Level-1 of the cross-pillar bridge ladder states `[ε_substrate-IS] ↔ HKR-image[ε_laboratory-IN]` at the cohomology-class level (regulator-invariant, L-independent). The identity holds at every L_max.
- **Step 3 (substitution)**: A `L^{-α}` envelope on `‖HKR(c_L) − c_continuum‖` IS Level-2-binding iff `c_continuum` is the HKR-image of the Level-1 cohomology class. The envelope describes convergence of the Level-1 binding under the bridge map's `L → ∞` limit.
- **Step 4 (simplification)**: A `L^{-α}` envelope on `Tr(D_K^{-2s})` (substrate-internal Mellin moment, no HKR image to a continuum laboratory observable on the partner pillar) does NOT bind Level-1; it is bare-decomposition. The substrate-internal limit `c_∞ = lim_{L→∞} Tr(D_K^{≤L,-2s})` is INTRINSIC, not a laboratory image.
- **Step 5 (direction)**: registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max` is MEANINGFUL ONLY for Level-2-binding envelopes; applying it to Level-2-non-binding envelopes admits false-PASS.

**Calibration corpus** (K=2):
- **Instance #1 (positive; W-5 §VII.AF.1)**: `L^{-3}` envelope at d=4 IS Level-2-binding. The HKR `L_max → ∞` image binds the HP^1 cohomology class to the Peotta-Törmä quantum-metric trace; the empirical W5-6 atlas match 0.0095% satisfies the binding envelope.
- **Instance #2 (S88 W-11 V.3, K=2)**: `L^{-α}` envelope on the W3b-15 KDE Sub-test B observable IS Level-2-binding by HKR-image construction. Cited W3b-15 audit_sha256=`cd13d13229aeb7961e74da5cf28f5612a3d45a524124aa0b9627654fc2dfa028`.

---

## VI. OE-form discipline (operator-expression form; full content)

See §II Element 2 for definitions; this section documents the K=2 calibration corpus and forward-looking convention pin.

**Calibration corpus** (K=2):

| # | Bridge | Element 2 form | Verdict |
|:-:|:-------|:---------------|:-------:|
| 1 | W-5 §VII.W (Pillar III ↔ Pillar IV) | `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` matches `\int.*d.*Tr.*\(P_0\)` | **PASS** (calibration baseline) |
| 2 | W11-5 FWD-C3 (Pillar IV ↔ Pillar V; pre-retrofit) | "Caroli-Matricon ladder asymmetry (W11-C5)" / "µSR chirality discrimination (W11-C6)" (prose-only) | **FAIL** (calibration counter-example; required §W7a-75 retrofit to projector form `Π^{vortex}_{B-phase}` + `Π^{µSR}_{A-phase}`) |

**Forward-looking convention pin**: From S88 W7a-73 onward, all NEW cross-pillar bridge-theorem entries MUST satisfy Element 2 OE-form regex at plan-freeze. Pre-S88 entries (W-5 §VII.W; W11-5 FWD-C3) GRANDFATHERED with mandatory retrofit at §W7a-75.

The OE-form discipline closes the W11-5 FWD-C3 REGISTRY-FAIL class of structural defect (Level-3 ratio_mismatch=1.029 violating Level-2 envelope 0.05 by ~21×) by construction at the rule-file level.

---

## VII. Substrate-input-orthogonality clause (Stage-2 PASS-AND ceiling)

Provenance: S88 W-23 W7c-167 V.1 (volovik-superfluid-universe-theorist; LEVEL-2 closure + obs1 PASS-AND independence workshop). Hardens the procedural-floor "without prior workshop context" guarantee (item 4 of `joint-theorem-promotion.md §"Two-Agent Independent-Verify"`) into a structural ceiling.

**Predicate**: For any Stage-2 verification with N ≥ 2 observables {obs_1, ..., obs_N}, the procedural floor MUST be supplemented with the **substrate-input-orthogonality predicate**:

> ∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both).

**Why it matters**: PASS-AND across orthogonal-data observables is the structural ceiling for the procedural-floor independence guarantee. Without substrate-input orthogonality, Stage-2 PASS-AND establishes structural-output-type independence (different decision pipelines on the same data) but not structural-input independence (the data itself is shared); the calibration corpus advances under explicit "substrate-input-overlap caveat" tagging.

**Cross-link**: to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 (the "agreement among agents" exclusion this clause sharpens) AND to `§X` algebra-axis orthogonality K-counter MANDATORY at K=3 (the structural-orthogonality precedent).

**Status**: K=1 advisory (S88 W7c-167; obs1 PASS-AND with substrate-input-overlap caveat; shared `s87_w7_ic_per_class_verify.npz` SHA-256 `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f`). Promotes to MANDATORY at K=3 distinct calibration instances.

---

## VIII. Per-Bulletin-per-pole Level-1/2/3 extension

Provenance: S88 W10-119 (mack-cosmic-bridge plan-pinned writer; orchestrator-direct-write in /rclab-solo with connes-ncg-theorist co-sign).

**Scope**: extends the 3-level structural-confidence ladder from CROSS-PILLAR (substrate Pillar A ↔ laboratory Pillar B) to INTRA-PILLAR Pillar-VII Mellin-cone Bulletin-class registry entries indexed by substrate-distance pole `s ∈ {3, 4, 5, ...}`.

**Mapping (per-pole specialization)**:

| Level | Cross-pillar form | Per-Bulletin-per-pole form |
|:------|:------------------|:---------------------------|
| Level 1 | regulator-invariant identity at axiom layer | per-pole substrate-distance-IS spectral identity at the s-th Mellin-cone pole; regulator-invariant; L-independent |
| Level 2 | `L^{-α}` convergence rate to continuum | per-pole L_max-truncation envelope `L^{-α(s)}` where α(s) is the pole-specific convergence rate (e.g., α(s=3) = 3 for substrate-distance-1 a_3 moments; α(s=4) = 4 for substrate-distance-2 a_4 moments) |
| Level 3 | numerical value at canonical L_max | per-pole numerical anchor at L_max=10 operational truncation OR analytic limit if pole-specific saturation theorem applies |

**Calibration corpus**:

| Bulletin | Pole | Level-1 (cohomology-class identity) | Level-2 (algebraic envelope) | Level-3 (empirical anchor) |
|:---------|:-----|:------------------------------------|:------------------------------|:----------------------------|
| **§VII.K-PROP.W10-4 ρ_∞ permanent-wall** | s=4 | ρ_∞ structurally IRRATIONAL per CC2 PROVEN; PERMANENT-WALL classification | simple-pole fit `ρ(L) = c0 + α/L² + β/L⁴`; L^{-2} dominant convergence at d=4 | `ρ_inf_full_f64 = -0.8103647022669215` (S87 W10-2 simple-pole fit) |
| **§VII.U.1 Mellin-Dirichlet identity** | s=3 | Mellin-Dirichlet identity at substrate-distance-1 pole; (A)-class pure-Mellin-support per F_4 | L_max-stability rel_diff = 0e+00 (S86 W-1 / S87 W1a-4 PASS) at L_max=12 | bit-identity stability across atlas members; (A)-class anchor `M^{(ζ)}_3 ≈ 2.97e-3` at L_max=10 |
| **§VII.AR LEVEL-DRESSED rank-ordering (S88 W-22 W7a-74 V.5)** | s=4 | Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 IS REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) | pole-specific α(s=4) per Casimir-bound saturation argument | rank-ordering value (CONDITIONAL on A.36 Reading A WIN swap-survives ≥4/5) |

**Status**: SUGGESTION at K=3 cohomology-class-distinct dimension. Mixed-status: MANDATORY-at-cohomology-class-distinct-K=3 for S89+ entries SHARING substrate-distance pole with existing corpus instances; SUGGESTION-pending-pole-distinct-K=3 for S89+ entries at NEW substrate-distance poles s ∈ {5, 6, 7, ...}. The §W10-120 DORMANT shell is queued to surface the pole-distinct third instance.

**Cross-link to cross-pillar bridges**: per-Bulletin-per-pole entries are **distinct from cross-pillar bridges** — the per-pole form is intra-pillar (within Pillar-VII Mellin-cone), so the 5-anatomy IS-not-IN elements are NOT mandatory at the same per-element granularity. The Level-1/2/3 ladder IS preserved; the rest of the cross-pillar discipline (HKR bridge map, IS-not-IN substrate-laboratory pair) does not apply intra-pillar.

---

## IX. Two-clause separation: registry-PASS vs K-counter advancement

Provenance: S88 W13 W-1 R3 (gen-physicist + landau; landed in-session 2026-05-08 per user directive eliminating deferred-CF-V.1 queue). Two-layer separation makes the registry-PASS-vs-K-counter epistemic distinction explicit.

The cross-pillar-bridge-anatomy discipline operates at **two structurally distinct epistemic layers** that must not be conflated:

- **Per-entry registry-PASS** (§III "Registry-PASS criterion"): gates whether a single registry entry's STAGE-tag may be promoted to STAGE-3-PERMANENT under the `joint-theorem-promotion.md` 4-stage pathway. Predicate: `Level-3 < Level-2 at canonical L_max`. Operates on the entry's own empirical satisfaction.
- **Rule-level corpus K-counter advancement** (§IV "MANDATORY at K=3" + §"Promotion event"): gates whether the rule's own status promotes from SUGGESTION to MANDATORY. Predicate: 3 distinct calibration-LANDING events satisfying the Hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv`. Operates on the rule's own corpus saturation.

The two predicates are INDEPENDENT.

**Worked examples**:
- Calibration corpus instance #2 (S87 W11-5 REGISTRY-FAIL) is the canonical worked example: the entry fails registry-PASS by Level-3 violating Level-2 by ~21×, AND COUNTS as calibration instance #2 toward the K-counter.
- Calibration corpus instance #3 (S88 W4a-17 .LAB STAGE-1-CANDIDATE) extends to a Level-3-DEFERRED case: the entry has no Level-3 numerical value yet (multi-year experimental cycle), is correctly flagged STAGE-1-CANDIDATE per joint-theorem-promotion 4-stage Stage 1 of 4, AND counts as calibration instance #3 toward the K-counter.

**Why orthogonality is structural**: K-counter saturation tests the rule's edge cases via cross-context calibration LANDINGs; per-entry registry-PASS tests the entry's own empirical adequacy. Conflating the two would either (a) starve the K-counter (refuse to count W11-5 / W4a-17, leaving K=1 forever and never reaching MANDATORY) — which would render the K-tracked promotion mechanism non-functional; or (b) require K-promotion to wait on multi-year experimental cycles — which would defeat the purpose of in-session forward-discipline pre-registration.

**Discipline**: Future readers MUST treat the two clauses as structurally orthogonal predicates on disjoint epistemic objects (the entry vs the rule). Conflation is a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc rewriting of pre-registered structure) per `v3-closure-recovery.md`.

The analogous separation applies to the parallel Algebra-axis orthogonality K-counter discipline (§X below).

---

## X. Algebra-axis orthogonality K=3 MANDATORY (parallel discipline)

Provenance: S87 W-2 R3 close (lizzi-spectral-functional-theorist PRIMARY synthesizer + connes-ncg-theorist CO-AUTHOR axiomatic derivation + mack-cosmic-bridge CO-AUTHOR observational discrimination map; workshop `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md`).

**The conjecture**: on any finite spectral triple `(A, H, D)` satisfying the 7 NCG axioms, the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level — there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproducing any algebra-INVARIANT spectral moment.

K=3 promotes to MANDATORY structural-theorem candidate (STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway, awaiting Stage-2 cross-axis independent-verify).

**N=3 calibration corpus**:

| # | Workshop | Algebra-INVARIANT exemplar | Algebra-DEPENDENT exemplar | Calibration evidence |
|:-:|:---------|:---------------------------|:---------------------------|:---------------------|
| 1 | S87 W1b-6 (lizzi+connes) | §VII.U.1 Mellin-Dirichlet identity (S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12) | full `M_n(ℂ)` Connes distance (regulator-divergent; INFO; no `{λ_n}` identity) | W1b-6 INFO verdict |
| 2 | S87 S-2 (lizzi+connes) | §VII.U.1 Mellin-Dirichlet identity | `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` Connes distance (regulator-saturated; STRICT residual `1.054e-01`; no `{λ_n}` identity) | S87 S-2 §3.2 closeout Reading-C synthesis |
| 3 | S87 W-2 (lizzi+connes+mack) | `α_s_canonical = n_s² − 1 = -8587279/100000000` Sage-QQ EXACT (W2-1 + W2-4 PASS at s=3 single-pole Mellin) | `α_s_route_3 = Var_a(n_a^GGE) = -7.046336` (W2-3 FAIL composite at higher-moment cone; algebra-DEPENDENT through GGE Bogoliubov vacuum specification) | this workshop's R3 close |

**Cross-cell ratio** (Sage-QQ exact 2026-05-09): `704633600/8587279 ≈ 82.0556×`.

**Substrate-physics derivation (axiomatic skeleton)**: NCG axioms 1+5 + Connes-Moscovici 1995 §III.4 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s = (d−n)/2] = Σ_k m_k λ_k^{−(d−n)}` GUARANTEE the algebra-INVARIANT family is non-trivial. NCG axioms 4+6 + Poincaré duality on `A_K` GUARANTEE the algebra-DEPENDENT family is non-trivial. The chirality-vs-A_F block-grading mismatch ensures `f(D²) ∩ π(A) = scalars` on the state-functional side, while the spectrum-only side is the full `Z(f(D²))` algebra. Both families are ALWAYS present; identity-class membership is structurally orthogonal by axiom-level NCG argument.

**Mandatory-at-plan-freeze enforcement**:

1. **Corner-cell declaration**: every entry declares its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table in §VII.U.2.
2. **Cross-corner co-primary FORBIDDEN**: SOURCE-DOUBLE-CITE-CO-PRIMARY structures scoping anchors across distinct corner cells fail `registry-landing.md §"Detection"` criterion (4) by algebra-axis orthogonality.
3. **Cross-pole co-primary FORBIDDEN**: per W-9 RULE-3 §"Pole-Scope sub-clause"; co-primary structures must inhabit the same Mellin pole-scope.
4. **Cross-corner cross-pole magnitude comparisons**: STRUCTURALLY FORBIDDEN as PASS/FAIL gates; permitted in narrative analyses ONLY with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration.

**Worked instance — §VII.AN-CORRIGENDUM**: the original §VII.AN landing carried SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure where ANCHOR-1 (V: S82 W3-9 single-pole Mellin closure) inhabited Cell I (algebra-INVARIANT × s=3) but ANCHOR-2 (C: S87 W2-3 GGE-Bog-occ-variance theorem) inhabited Cell IV (algebra-DEPENDENT × s=4). Per S88 W-15 V.6 landing, cross-corner co-primary structures are STRUCTURALLY FORBIDDEN. The CORRIGENDUM successor entry REMOVES ANCHOR-2 and migrates STRUCTURE tag to `PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM`. Substitution chain (Sage-QQ exact): `n_s_FW² − 1 = (9561/10000)² − 1 = -8587279/100000000 = α_s_canonical` EXACT in Q with NO ROUNDING.

**Cross-link to atlas-12**: atlas-12 catalogs the audit-side machinery enforcing the algebra-axis orthogonality at plan-freeze (audit script `_corner_classification_audit.py` queued at S88 CF-E; PRU Class-8 sub-class taxonomy for cross-corner co-primary detection; rule-file Phi correspondence pin via `epistemic-discipline.md §"Layer-Decomposition"`). Atlas-11 catalogs the substrate-IS structural conjecture itself; atlas-12 catalogs the methodology-floor enforcement mechanism. Both reside in `cross-pillar-bridge-anatomy.md` because the rule unifies the substrate-IS bridge anatomy and the algebra-axis orthogonality at the same rule-file location, but the CORPORA are split for atlas indexing.

---

## XI. Forward calibration: 3 forward bridge candidates (FWD-C1 / FWD-C2 / FWD-C3)

Provenance: S87 W5-5 (volovik orchestrator; co-signer connes-ncg-theorist). Forward-looking template-adoption SUGGESTION for `cross-pillar-bridge-anatomy.md`. Per S88 W4a-17 K=3 advancement, the discipline is now MANDATORY for new bridge entries; FWD-C1/C2/C3 ARE the pre-registered S88+ candidate slate.

### FWD-C1 — Pillar I ↔ Pillar II (substrate ↔ cosmology measurement)

- **Substrate-IS observable**: n_s spectral-action prediction from finite-L D_K eigenmoments on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) — the n_s_FW value is a substrate-IS scalar moment of the Jensen-deformed band-0 sector at τ_fold.
- **Laboratory-IN observable**: Planck CMB scalar spectral index n_s = 0.9649 ± 0.0042 (Planck 2018 TT,TE,EE+lowE+lensing) — measured IN the FRW cosmology container as the slope of the temperature power spectrum near k_pivot = 0.05 Mpc⁻¹.
- **Bridge map**: Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment. The bridge factors through the c_sub conformal-anomaly multiplier per S86 W5a Z-factor machinery.
- **Algebraic envelope**: L_max⁻³ at d=4 inherited from Pillar III ↔ IV (W-5 calibration); Level-2 canonical envelope pending substrate-first c_sub completion.
- **Empirical anchor target**: n_s_FW vs Planck n_s comparison at canonical L_max=10 under substrate-first IC (S86 W5a SR-flow Z-factor pivot).
- **Inheritance kernel rank**: rank(ker ι_*) = 1 (single n_s scalar; rank-2 not applicable).
- **Earliest S88+ dispatch**: post-c_sub completion.

### FWD-C2 — Pillar II ↔ Pillar V (Mellin-cone ↔ BdG spectral triple)

- **Substrate-IS observable**: Mellin-Barnes residue at substrate-distance s ∈ {3, 4} on the Pillar-II Mellin-cone, evaluated against ζ-regulated Hochschild moments of D_K — the substrate IS the Mellin-residue cocycle (workshop-§VII.U/V family on the spectral-distance axis).
- **Laboratory-IN observable**: BdG (Bogoliubov-de Gennes) spectral-triple observable in a self-consistent BCS lattice — measured IN the Brillouin-zone container as the BdG band structure with Pf=−1 BDI topology (3He-B child realization; Volovik 2003 §6).
- **Bridge map**: Connes-Karoubi pairing ∘ K-theory boundary map between the Pillar-II Mellin pole structure and the Pillar-V finite-rank BdG K_0(M_2(C)) image; companion to W-6 quotient-functor framework.
- **Algebraic envelope**: L_max⁻α with α ∈ {2, 3} under spectral-distance scaling; α pinned post-Mellin-pole-closure at S87 W2-? cluster-span PASS.
- **Empirical anchor target**: Pillar-II → Pillar-V Mellin-residue / BdG-band-edge match at canonical L_max=10; substrate-first cocycle norms ‖φ‖ Sage-exact.
- **Inheritance kernel rank**: rank(ker ι_*) ≥ 2 expected — Mellin-cone carries multiple residue generators; invokes rank-2 generalization.
- **Earliest S88+ dispatch**: post-§VII.U/V family closure.

### FWD-C3 — Pillar IV ↔ Pillar V (substrate cocycles ↔ 3He-B / 3He-A laboratory observables)

PARTIALLY LANDED via §VII.W-3.LAB (S88 W4a-17, instance #3 of K=3 corpus).

- **Substrate-IS observable**: Substrate-resident HP^1 cocycle norms ‖φ_67‖, ‖φ_88‖ (W-5 Sage-exact: ‖φ_67‖ = 0.793346 M_KK², ‖φ_88‖ = 0.108307 M_KK², ratio 7.324992 = 114453/15625 in Q) evaluated on the BdG-restricted spectral-triple sub-algebra of (A_K, H_K, D_K). The substrate IS the cocycle pair — these are intrinsic structural numbers.
- **Laboratory-IN observable**: 3He-B vortex-core Caroli-Matricon ladder asymmetry (W11-C5; Lancaster MCT-3) AND 3He-A µSR chirality discrimination (W11-C6; partially queued at S87 CF-32 + CF-33). Lab measures these IN the helium cryostat container under a (p, T) sweep over 0–34 bar.
- **Bridge map**: Inheritance morphism ι_*: A_K = C ⊕ H ⊕ M_3(C) → M_2(C) (BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor. Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual) preserves ‖φ_a‖/‖φ_b‖ INTACT in the lab measurement under common p.
- **Algebraic envelope**: Cohomology-asymmetry test: ratio preservation 7.3250 ± 0.1% (S86 W-5 Gate-2 pre-registered band). Level-2 envelope is the structural-exact form, not an L_max⁻α algebraic bound.
- **Empirical anchor target**: S88+ Lancaster MCT-3 vortex-core spectroscopy and RHUL/Aalto LTL µSR run delivering NULL on F1/F2/F5 + ratio 7.3250 ± 0.1% on any non-NULL detection (4-gate falsifier structure).
- **Inheritance kernel rank**: rank(ker ι_*) = 2 (φ_67 chiral pair + φ_88 Cartan hypercharge).
- **Earliest S88+ dispatch**: Partially LANDED via CF-32 + CF-33 lab pre-registrations (S87 W5-2 + W5-3); FULL bridge-anatomy registry entry queued for S88+ once lab data lands.

### Rank-2 generalization cross-reference

Candidates **FWD-C2** and **FWD-C3** carry inheritance-kernel rank ≥ 2 and MUST be designed under `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` (rank-2 dual-cocycle case + rank ≥ 3 binomial(rank, 2) cross-cocycle ratio enumeration). The W-5 calibration ratio ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact) is the canonical exemplar.

### Inheritance-falsifier 4-gate structure

- **Gate 1**: Kernel-signature row-wise NULL test on the **decisive** F-rows (W-5: F1 + F2 + F5)
- **Gate 2**: Cohomology-asymmetry cross-cocycle ratio test (W-5: 7.3250 ± 0.1% on any non-NULL detection)
- **Gate 3**: Kernel-signature row-wise NULL test on the **supporting** F-rows (W-5: F3 + F4)
- **Gate 4**: Discriminating slope analysis on cocycle-degenerate rows requiring parameter-sweep (W-5: F4 multi-pressure slope; Jacobi-cubic vs φ_88-linear over 0–34 bar)

### (Δ_B/Δ_A)^p Cancellation Theorem (operational form)

```
lab(F_i) / lab(F_j)  =  ‖φ_a‖ / ‖φ_b‖  ×  (f_i / f_j)
```

for common exponents `p_i = p_j = p` in the lab-conversion factors. The `(Δ_B/Δ_A)^p` factor cancels exactly between numerator and denominator. The substrate-derived ratio `‖φ_a‖ / ‖φ_b‖ = 7.324992` is therefore preserved INTACT in the lab measurement, INDEPENDENT of the precise value of (Δ_B/Δ_A) or p. Verified at machine precision: S86 W-5 DONE-5; 0.0e+00 residual (Python).

### Audit at plan-freeze for forward bridge candidates

1. The bridge label maps to one of {FWD-C1, FWD-C2, FWD-C3} OR declares a new candidate ID.
2. The 5 IS-not-IN anatomy elements are present (existing MANDATORY).
3. The 3 level markers are present (existing MANDATORY).
4. If rank(ker ι_*) ≥ 2: `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B"` cross-reference present.
5. K-counter incremented by 1; if K reaches 3 post-landing, the orchestrator promotes parent rule's status to MANDATORY in the same dispatch.

---

## XII. Cross-atlas dependencies

- **atlas-07-permanent-results**: enumerates §VII slots (XVI.A row §VII.AF.1.OP-PROJ + §VII.AF.1.STATE-PROJ + §VII.W-3.LAB). Atlas-07 carries the per-slot status / authorship / 1-line summary; atlas-11 carries the per-instance bridge-anatomy structural content (5 elements + 3 levels + Hybrid Independence Test verdict + Stage-1/2/3 promotion status) AND the K=3 MANDATORY corpus narrative.
- **atlas-02-mechanism-lifecycle**: bridge instances ARE closures. §VII.AF.1.OP-PROJ closure timeline: workshop S86 W-5 → registry-LANDED S87 W5-1 → suffix-retrofit S88 W11 V.4. W11-5 closure timeline: dispatch S87 W11-5 → REGISTRY-FAIL by 21× → carry-forward `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`. §VII.W-3.LAB closure timeline: workshop S88 W4a-17 → registry-LANDED STAGE-1-CANDIDATE 2026-05-04 → Stage-2 deferred to multi-year experimental cycle.
- **atlas-10-breakthrough-genealogy**: cross-pillar bridge anatomy itself is breakthrough #28 (S86 W-5); §VII.AF.1 first LANDED is #31; §VII.W-3.LAB K=3 saturation is #32; §VII.U.2 four-corner (algebra-axis registry landing) is #33.
- **atlas-12-methodology-floor**: atlas-12 carries the methodology-floor enforcement (audit scripts, PRU Class-8 enforcement, OE-form regex audit, plan-freeze halt protocols, methodology-wave-allowlist row management); atlas-11 carries the substrate-IS structural content. The two are layer-functor F image pairs per the Phi correspondence in `epistemic-discipline.md §"Layer-Decomposition"`.
- **`.claude/rules/cross-pillar-bridge-anatomy.md`** + **`sessions/framework/registry/cross-pillar-bridge-corpus.md`**: structural sources. Atlas-11 IS the human-readable atlas for the rule body + corpus combined — the rule body provides discipline statements + schema; the corpus file provides per-instance corpus + K-counter advancement log; atlas-11 is the curated, structural narrative explaining WHY the discipline exists, HOW the K=3 corpus was assembled, and WHAT the 5-anatomy + 3-level ladder structurally guarantees.

---

## XIII. Substrate framing (atlas-11 itself)

Per `phononic-framing.md §"IS Space, Not IN Space"`: atlas-11 is a CURATED narrative on the substrate-IS bridge anatomy. Every atlas-11 section flows FROM substrate TOWARD laboratory image:

```
Substrate (Pillar A, finite-L spectral triple `(A^{≤L}, H^{≤L}, D^{≤L})`)
   IS the [substrate-IS observable]
      → Bridge map (HKR `L_max → ∞` / Connes-Karoubi pairing / K-theory boundary
                    / inheritance morphism χ + (Δ_B/Δ_A)^p cancellation
                    / Mukhanov-Sasaki gauge ∘ HKR)
   → Laboratory (Pillar B) IN [laboratory-IN observable]
```

The substrate is logically prior to the laboratory image at BOTH the conceptual level (where do explanations come from?) and the numerical level (where do pin values come from? — per `substrate-first-canonical-sourcing.md`). External-paper provenance (Peotta-Törmä for Pillar IV BZ-trace; Volovik 2003 for Pillar V BdG; Mukhanov-Sasaki for Pillar II) is METHODOLOGICAL cross-check, not CANONICAL replacement.

The K=3 MANDATORY discipline at S88-close (2026-05-04) is the structural mechanism that forces this framing: NEW bridge entries that lack the 5-anatomy + 3-level ladder cannot land; entries that conflate substrate-IS with laboratory-IN cannot land; entries that invert the direction of explanation (treating Pillar B as fundamental and Pillar A as derived) cannot land.

The cross-pillar bridge corpus IS the framework's structural answer to: "how does substrate IS Pillar A connect to laboratory IN Pillar B without inverting the substrate-prior discipline?" The five anatomy elements, the three confidence levels, the K=3 corpus, the Hybrid Independence Test, the Level-2 sub-class taxonomy, the OE-form discipline, the substrate-input-orthogonality clause, the per-Bulletin-per-pole intra-pillar extension, the two-clause registry-PASS-vs-K-counter separation, the parallel algebra-axis orthogonality K=3, and the FWD-C1/C2/C3 forward calibration — all are structural mechanisms that PRESERVE the substrate-prior direction at registry-entry granularity.

---

## XIV. S89–S118 currency delta (corpus extension; catalog lives elsewhere)

The 5-anatomy + 3-level ladder, the K=3 MANDATORY discipline, the Hybrid Independence Test, and the Level-2-binding/non-binding sub-class taxonomy above are **frozen at S88 and remain current** — no re-derivation of the anatomy occurred S89–S118. What changed is CONTENT: the discipline was applied at plan-freeze to ~45 new §VII cross-pillar / intra-pillar landings (slots **AU → CK**), the live calibration set. This atlas does NOT re-catalog them; the per-slot inventory lives in **atlas-07 §XVI** (retitled "S52–S118") and the per-instance corpora + K-counter logs in **`sessions/framework/registry/cross-pillar-bridge-corpus.md`**.

**Structurally-notable new bridge instances** (highlights only — NOT the catalog; source: `_uplift-S119-materials/20-theorems-results-S89-S118.md §A.1`):

| slot | S{N} | bridge (substrate-IS → lab-IN) | corpus role |
|:-----|:-----|:-------------------------------|:------------|
| §VII.AU.OP-PROJ | S89 →3 S93 | FWD-C1 realized: substrate spectral-action tilt → CMB n_s; regulator-invariant α = −3 | the §XI FWD-C1 forward-candidate is now LANDED (STAGE-3-PERMANENT) |
| §VII.BG | S94 →3 S95 | α_s direct Connes-Karoubi K₀-pairing transport at the a₄ Yang-Mills pole s=2 | new bridge-map-class instance (K₀-pairing, not HKR L→∞) |
| §VII.BK | S97 | D_K ≅ D_F low-energy recovery of the Connes–Chamseddine SM finite geometry | substrate ↔ SM-geometry bridge |
| §VII.CB | S106 →3 | Type-IV core EMT `Tr_{M₂}(P_a₂·T^{(IV)})` → emergent metric g_M; **BINDING L⁻³**; Level-3 7.5e-9 < Level-2 1e-3 | new **REGISTRY-PASS** instance — structural sibling of the §VII.AF.1 baseline |
| §VII.CF | S110 →3 S111 | κ-sign-lock ∧ Wodzicki-parity joint foreclosure (only admissible transport = sign-locked `M_KK¹` scale leg) | anchors the new transport-degree / parity discipline |

**K-counter status deltas** (one line each; source: `20-theorems-results-S89-S118.md §B` + `cross-pillar-bridge-anatomy.md`):

- **Algebra-axis orthogonality** (§X): **held MANDATORY at K=3** — no change; re-confirmed across S89–S118 landings.
- **Per-observable transport-degree scale-separation** (`deg T_{BZ→pivot}`): **NEW — SUGGESTION at K=2**; its mass-dimension/parity selection rule (S110 W4) forces every odd-`d_A` observable onto the sign-locked `M_KK¹` scale leg. Physically load-bearing for §VII.CF and §VII.CG (the LRD-temperature and r=16ε foreclosures).
- Additional plan-freeze sub-directives landed S89–S118 as SUGGESTION/K=1–K=2 — Composite Bridge-Map dimensional-class admissibility; Tier-1/Tier-2 dimensional-re-anchorability gate (K=2); Level-3 annotation discipline; Non-Promotion-by-Held-Number meta-taxonomy — **pointer only**; see `cross-pillar-bridge-corpus.md`.
- **No new §VII.M-letter methodology slots** were opened S89–S118; the maturation is in `.claude/rules/*` + the corpus files, not the registry (see atlas-12 §XX).

---

*Sources: `cross-pillar-bridge-anatomy.md` (323 lines, S86 W-5 origin + S88 W4a-17 MANDATORY-K=3 promotion); `cross-pillar-bridge-corpus.md` (per-instance corpora, S88 W9-RULE-CLEANUP lift-out); `joint-theorem-promotion.md` (Stage-2 cross-axis verify); `inheritance-falsifier-protocol.md` (rank-2 ker(ι_*) protocol); `permanent-results-registry.md §VII.AF.1.OP-PROJ + §VII.AF.1.STATE-PROJ + §VII.W-3.LAB + §VII.AN/AO/AP`; S86 W-5 + S87 W5-1 + S87 W11-5 + S88 W4a-17 + S88 W7a-73 + S88 W7c-167 + S88 W8-87/88/92 + S88 W10-119 + S88 W13 W-1 R3 workshops. Sage-QQ exact rationals verified 2026-05-09 via mcp__sage__sage_eval.*
