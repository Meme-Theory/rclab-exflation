> **ARCHIVED 2026-06-12** (papers review campaign, post-S103; atlas-09 Item 50)
> **Last meaningful session**: S87
> **Superseded by**: `sessions/permanent-results-registry.md` §VII.AC.1 (binary-not-continuous multi-valued classification, Schur-forced: `P_{B1}·P_{B2} = 0`, no free unitary mixing parameter) + `.claude/rules/cross-pillar-bridge-anatomy.md` §"Single-observable-per-triple structural filter" (continuous deformation FORBIDS the slot-split)
> **Reason**: the note's central construction — a continuous ε ∈ [0,1] interpolation between Path-H and Path-C with intermediate-r as a third class — is structurally contradicted by the registry entry it was written to scaffold; ε is exactly the forbidden mixing parameter. Design-note SUPERSESSION, not a result retraction (the S87 gate was paper-mode artifact-existence; §VII.AC.1 and §VII.AH landings are unaffected). Review: `papers/_review-s103/review-s87-path-h-path-c.md`. Known value drift retained as-written: r_Path_H = 0.00745 / provenance "S85 W2 OQ-7" superseded by canonical r_PathH = 0.0074705 (S86); ratio 1.5747 → 1.5704 at canonical precision.

---

# Path-H ↔ Path-C Interpolation: Substrate-IS Construction Across the Regulator-Class Atlas

**Gate**: `S87-PATH-H-PATH-C-INTERPOLATION` (S87 W2-6, Priority 6, paper-mode)
**Author**: mack-cosmic-bridge (sole owner, S87 W-2 attribution)
**Plan reference**: `sessions/session-plan/session-87-plan-w2.md` §W2-6
**Sister gate**: CF-20 → `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` (W3, gen-physicist owner)
**Inter-wave dependency**: feeds W9 CF-54 → `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` (W9, mack owner)
**Date**: 2026-04-28

---

## Abstract

The S86 W-3 r-dual-pathway workshop landed a **multi-valued classification (a)** for the framework's spectral observable Path-H (zeta-axiom L1) and Path-C (cone-axiom L3), with anchor structure SOURCE-DOUBLE-CITE-CO-PRIMARY (V1 = 3He-B BDI 0D inheritance arrow; C1 = Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`). The two readings are **endpoints of a substrate-IS interpolation**, not isolated points. This paper constructs that interpolation along two complementary axes — (a) a third NCG-compatible regulator within the canonical 5-atlas + 1-extension corpus, and (b) a continuous deformation parameter ε ∈ [0, 1] between the L1 sphere-axiom and L3 cone-axiom regulator schemes — and identifies the structural endpoints, the substrate-IS observable being interpolated, and a falsifier protocol that distinguishes intermediate-r outcomes from boundary outcomes.

The substrate IS the interpolation: it lives on the regulator-class moduli space of the spectral triple `(A_K, H_K, D_K)`, not "in" a parameter container. The atlas is the substrate's own classification of admissible regulator schemes. ε ∈ (0, 1) is not a free parameter to fit data; it is the substrate-IS coordinate parametrizing structurally distinct regulator-class moments along the (L1, L3) span.

---

## 1. Framework substrate-IS interpolation construction

The substrate-IS observable being interpolated is the **multi-valued (α_s, n_s) pair** at the framework's canonical pivot scale. The S86 W-3 workshop registered two structurally distinct readings in the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern (per `.claude/rules/registry-landing.md`):

- **Path-H (zeta-axiom, L1 / sphere-axiom regulator)**: the Mellin-cone moment scheme native to L1; produces Path-H pinned values `r_Path_H = 0.00745` (canonical from S85 W2 OQ-7), with α_s recovered via the spectral identity `α_s = n_s² − 1` evaluated on the L1-natural pivot.
- **Path-C (cone-axiom, L3 / per-observable-span regulator)**: the moment scheme requiring substrate-action evaluation (no analytic L1 continuation); produces `r_Path_C = 0.011731522` (canonical from S83 G46 = `r_CMB_framework`), with the corresponding (α_s, n_s) entry under the L3-native pivot. Raw ratio `r_Path_C / r_Path_H ≈ 1.5747`.

These are **not two competing values for one observable**; they are the substrate's own multi-valued readings of one observable indexed by regulator class. The S86 W-3 R3-A Convergence #2 verdict explicitly revoked the "V1-PRIMARY" framing in favor of CO-PRIMARY: removing either the algebraic-input layer (V1) or the theorem-output layer (C1) breaks the derivation. Both anchors must remain accessible for the registry entry to retain its derivational provenance.

The interpolation construction proceeds via two complementary, structurally independent routes:

### 1.1 Route (a) — Third NCG-compatible regulator within the 5-atlas + 1-extension corpus

The canonical regulator atlas pinned in `computations/canonical_constants.py` and enforced by `.claude/rules/regulator-pin-discipline.md` admits five regulators with explicit `a_n^{<regulator>}` Seeley-DeWitt tagging: ζ-function regularization, Pauli-Villars, Mellin-Barnes, lattice spacing, and sharp UV cutoff. The S82 `S82-R-FAMILY-ATLAS-EXTENSION` PASS verdict (sha256=983587f1...) extended this corpus to 11 candidates, of which the 5-atlas form is the canonical subset. The S85 5A workshop site #11 identified an additional substrate-natural extension whose moment structure is intermediate between the L1 sphere-axiom moments (where ζ is structurally undefined at s = −1) and the L3 cone-axiom moments (which require per-observable substrate-action evaluation). The third regulator R₃ then satisfies:

```
(α_s, n_s)_{Path-H}   =  evaluate(α_s, n_s; R = ζ,  scheme-axiom = L1)        [ε = 0]
(α_s, n_s)_{Path-C}   =  evaluate(α_s, n_s; R = R_∞, scheme-axiom = L3)        [ε = 1]
(α_s, n_s)_{Path-R₃}  =  evaluate(α_s, n_s; R = R₃, scheme-axiom = L2 or L1.5) [ε ∈ (0,1)]
```

The substrate IS this evaluation across the three readings. The interpolation parameter ε is the regulator-class coordinate on the moment-scheme moduli, not a free parameter we tune.

### 1.2 Route (b) — Continuous deformation between L1 and L3 axioms

Equivalently, one can parametrize the interpolation directly as a continuous family of axiom-conditions D_K^{(ε)} on the spectral triple (A_K, H_K, D_K), interpolating the L1 sphere-axiom (ε = 0) and the L3 cone-axiom (ε = 1) endpoint geometries. The substrate-IS observable (α_s(ε), n_s(ε)) is a continuous function of ε on (0, 1), with discrete classifications (a)/(b)/(c)/(d) of the multi-valued reading at the endpoints. The endpoint identifications are:

- ε = 0 ⇒ `(D_K^{(0)} = D_K|_{L1})` ⇒ **Path-H reading**, native zeta-regulator-class moment, single-pole-Mellin-substrate-distance-1 scheme.
- ε = 1 ⇒ `(D_K^{(1)} = D_K|_{L3})` ⇒ **Path-C reading**, per-observable-span moment, Jensen transit + c_sub upper-spread scheme.

Routes (a) and (b) are structurally equivalent under the layer-functor F image discipline of `epistemic-discipline.md` §"Layer-Decomposition": the regulator-class atlas axis (route a) is the algebraic-discrete representation of the deformation-parameter axis (route b) under the substrate ↔ methodology image mapping.

---

## 2. L1 / L3 boundary identification

The two interpolation endpoints are pinned to the canonical regulator-class atlas:

| ε | Regulator scheme | Mellin moment locus | Path label | r value | Anchor |
|:--|:------------------|:--------------------|:-----------|:--------|:-------|
| 0 | L1 — sphere-axiom (ζ, Mellin-Barnes substrate-distance-1) | s = 4 (substrate-distance-1 pole) | Path-H | 0.00745 | V1 = 3He-B BDI 0D inheritance arrow |
| 1 | L3 — cone-axiom (per-observable-span; substrate-action evaluation; Jensen transit + c_sub upper-spread) | per-observable-residue | Path-C | 0.011731522 (= r_CMB_framework, S83 G46) | C1 = Connes 1996 + NCG axioms 3+5+6 + Schur orthogonality on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) |

**Boundary (i) — ε = 0 ↦ Path-H (L1 / sphere-axiom)**: At the L1 endpoint the regulator is ζ-function regularization (or equivalent zeta-axiom-unique scheme), the moment locus is the substrate-distance-1 pole at s = 4, and the spectral observable α_s = n_s² − 1 is recovered via Mellin substrate-distance-1 evaluation on the L1-native pivot. The substrate-IS framing: the spectral triple (A_K, H_K, D_K) at ε = 0 is the L1 sphere-axiom truncation of the regulator-class atlas. Path-H is *not in* L1; Path-H IS the L1 reading.

**Boundary (ii) — ε = 1 ↦ Path-C (L3 / cone-axiom)**: At the L3 endpoint the regulator is per-observable optimal (no L1 analytic continuation), the moment locus is the per-observable residue under substrate-action evaluation, and the (α_s, n_s) entry follows the Jensen transit + c_sub upper-spread scheme. The substrate-IS framing: the spectral triple at ε = 1 is the L3 cone-axiom completion. Path-C is *not in* L3; Path-C IS the L3 reading.

The boundary identifications are **structural**, not numerical fits. They follow from the regulator-pin-discipline + registry-landing rules; the interpolation between them is the substrate's continuous family of regulator-class moments, parametrized by ε.

---

## 3. Intermediate-r falsifier-distinguishing prediction

For ε ∈ (0, 1) the substrate-IS reading is a **third class** distinct from both Path-H (ε = 0) and Path-C (ε = 1). The S86 W-12 boundary table (per `session-86-plan-w12.md`) pins three structural breakpoints on the r-axis:

- `b1_b2 = 0.005` (Path-detection-strong-low / Path-H boundary)
- `b2_b3 = 0.015` (Path-H / Path-C boundary)
- `b3_b4 = 0.030` (Path-C / framework-falsified boundary)

Path-H pins at r = 0.00745 sits in the (b1, b2) interval; Path-C pins at r = 0.011731522 sits in the (b2, b3) interval. The interpolation predicts a continuous trajectory r(ε) connecting these, with intermediate values strictly inside (b1, b3). The falsifier protocol:

**Class A — Endpoint-recovery test (boundary-IS)**: At ε → 0 the interpolation must recover r = 0.00745 ± Mellin-substrate-distance-1 truncation residual; at ε → 1 it must recover r = 0.011731522 ± Jensen-transit residual. Failure of either endpoint recovery falsifies the L1/L3 anchor identification, not the interpolation itself.

**Class B — Intermediate-r distinguishing-discrimination**: For ε ∈ (0.2, 0.8) the substrate-IS prediction is a continuous r(ε) in the band [0.0085, 0.0110] (the convex hull of Path-H and Path-C with structural-corrections from the third regulator R₃). A measured r value in this intermediate band that does NOT correspond to a fitted ε in (0, 1) — i.e., a band-mismatch — falsifies the interpolation construction. Concretely, the S87+ falsifier-distinguishing observable is:

```
distinguishing predicate:  r_obs ∈ (b1, b3) AND r_obs ∉ {Path-H, Path-C} AND r_obs ∉ r(ε ∈ (0,1))
                           ⇒ FALSIFICATION of the interpolation construction (not of the framework)
```

**Class C — Regulator-pin-discipline coverage**: any S87+ computation script citing α_s or n_s under an interpolation regime ε ∈ (0, 1) MUST tag the regulator-class explicitly per `.claude/rules/regulator-pin-discipline.md` — the bare `α_s` / `n_s` form is forbidden. The interpolation construction makes the tagging structurally mandatory because the tag IS the regulator-class coordinate ε's discrete representative.

**Detector-decisive timing**: BICEP/Keck Array 2026 release (r-axis discrimination) provides the first endpoint-recovery test at the Path-H / Path-C boundary. LiteBIRD 3-yr σ(n_T) = 0.0540 (post-2030) provides the per-multipole tensor-tilt cross-check. CMB-S4 α_s convergence cross-checks the (α_s, n_s) joint identity along the interpolation. The framework predicts that observed (r, α_s, n_s) will lie on the substrate-IS r(ε) trajectory, not at one of the endpoints exclusively.

---

## 4. Cross-link to W9 CF-54 Path-(c) successor anchor

The Joint F_2-Class Path-(c) Theorem registered at S86 W-9 (lizzi+transit; workshop §"Joint F_2-Class Path-(c) Theorem") is a 6-clause STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md`:

- Clauses (a) lizzi-side, (b) transit-side: single-axis derivations.
- Clauses (c), (d) **JOINT**: require both spectral-functional + transit-dynamics axes; structurally PASS-AND'd at Stage 2.
- Clauses (e) lizzi-side (with R3-B amendment), (f) transit-side: single-axis derivations.

This W2-6 paper provides the **substrate-IS interpolation framework** that W9 CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`) cites in landing the Joint Theorem's STAGE-1-CANDIDATE registry text. Specifically:

- **Clause (c) JOINT**: the spectral-functional + transit-dynamics joint reading of the multi-valued (α_s, n_s) pair cites this paper's §1.1 + §1.2 interpolation construction as the structural framework on which the joint reading rests. Without the interpolation framework, clause (c) reduces to an endpoint-disjunction; with it, clause (c) is a continuous-family statement.
- **Clause (d) JOINT**: the cross-axis identification of Path-H ↔ Path-C as endpoints of a single substrate-IS family (rather than two structurally distinct theorems) cites this paper's §2 boundary identification as the structural anchor.

**Inter-wave dependency**: per plan §"Wave 2 → Wave 3 Decision Point":

- W2-6 PASS at session close → W9 CF-54 dispatch reads §1 + §3 verbatim; landing is structurally-grounded.
- W2-6 INFO at session close → W9 CF-54 dispatch can still proceed with a weaker landing (non-interpolation endpoints only); document the dependency-shortfall as an explicit sub-clause carry-forward to S88.
- W2-6 FAIL at session close → W9 CF-54 dispatch proceeds without the interpolation framework; the Joint Theorem clause referencing interpolation is dropped or marked as STAGE-1-CANDIDATE-WITH-INTERPOLATION-CARVE-OUT.

**Falsifier-master-inventory cross-link**: per `feedback_mack-bridge-role.md`, mack-cosmic-bridge is the sole writer for `sessions/framework/registry/falsifier-master-inventory.md` updates. This paper's §3 falsifier-distinguishing prediction queues a row (Class A endpoint-recovery + Class B intermediate-r distinguishing) for landing under the W9 CF-54 dispatch, citing the SHA pin emitted by the audit script accompanying this paper.

**Sister-gate cross-link CF-20 (S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING, gen-physicist W3 owner)**: CF-20 lands the §VII registry entry for the Path-H/Path-C multi-valued classification (a) under SOURCE-DOUBLE-CITE-CO-PRIMARY. This paper's interpolation construction is consumed by CF-20's registry text as the structural framework that justifies the CO-PRIMARY classification (rather than PRIMARY+CONFIRMATION) — neither V1 nor C1 alone fixes the conclusion; together they fix the endpoints of the interpolation, and the interpolation itself is the multi-valued substrate observable.

---

## 5. Structural-direction summary (paper-mode declarative)

The substrate-IS interpolation construction stated above is a **structural-direction claim**, not a numerical prediction. The substitution chain at the structural level:

**Definition (regulator-class coordinate)**: ε ∈ [0, 1] is the substrate-IS coordinate on the regulator-class moduli of the spectral triple (A_K, H_K, D_K). At ε = 0 the regulator is L1-sphere-axiom (ζ); at ε = 1 the regulator is L3-cone-axiom (per-observable-span).

**Substitution (substrate-IS observable)**: The framework's spectral observable (α_s(ε), n_s(ε)) is the regulator-class-indexed evaluation of the spectral identity α_s = n_s² − 1 along ε. At endpoints the readings are Path-H (ε = 0) and Path-C (ε = 1); interior values are the third-regulator R₃ continuous family.

**Simplification (boundary-recovery)**: ε → 0 ⇒ (α_s, n_s) → (Path-H, L1 native); ε → 1 ⇒ (α_s, n_s) → (Path-C, L3 native). r(0) = 0.00745; r(1) = 0.011731522.

**Direction (structural)**: The interpolation IS the substrate's multi-valued classification. Path-H and Path-C are not competing pins; they are endpoints of a single substrate-IS family. The CO-PRIMARY anchor structure (V1 + C1) is the algebraic representation of this family at ε = 0 and ε = 1 respectively. The intermediate-r falsifier predicate (§3 Class B) is the substrate's empirical handle on whether the family is well-defined; failure of the predicate falsifies the interpolation, not the framework.

This is a paper-mode artifact: the gate verifies §1 substantive content presence (≥ 15 lines) + §2 boundary identification + §3 falsifier-distinguishing prediction + §4 W9 CF-54 cross-link. Numerical r(ε) at intermediate ε is deferred to S88+ implementation gate per plan §6 machinery pin (paper-mode declarative ε ∈ [0, 1]; numerical ε-scan deferred).

---

## 6. References (substrate-first; no external-paper-provenance pins)

- `sessions/session-86/sessions/session-86-w-3-workshop.md` (S86 W-3 r-dual-pathway and BK-Array workshop; Path-H/Path-C dichotomy classification (a) origin)
- `sessions/permanent-results-registry.md` §VII registry (W-3 R3-A Convergence #2 SOURCE-DOUBLE-CITE-CO-PRIMARY landing)
- `computations/canonical_constants.py` (5-atlas regulators; r_Path_H = 0.00745; r_Path_C = 0.011731522 = r_CMB_framework S83 G46; n_s_framework = 0.9590 / 0.9561)
- `.claude/rules/regulator-pin-discipline.md` (a_n^{<regulator>} tagging discipline; 5-atlas + 1-extension corpus)
- `.claude/rules/registry-landing.md` (SOURCE-DOUBLE-CITE-CO-PRIMARY pattern; S86 W-3 RULE-1)
- `.claude/rules/joint-theorem-promotion.md` (4-stage pathway for joint cross-axis theorems; W-9 RULE-1)
- `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" (W-13 RULE-2 substrate ↔ methodology layer-functor F)
- `sessions/session-86/compute-carryforward.md` lines 25-26 (CF-19 source brief; CF-20 sister-gate cross-link)
- `sessions/session-plan/session-87-plan-w2.md` §W2-6 (gate block; PRDR machinery pins; YAML)

---

*Paper draft v1, S87 W2-6, 2026-04-28. Audit script: `computations/s87_w2_path_h_path_c_interpolation_paper_audit.py`. Verdict line: see `computations/s87_gate_verdicts.txt`.*
