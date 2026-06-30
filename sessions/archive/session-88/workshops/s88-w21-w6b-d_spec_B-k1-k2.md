# Session 88 Synthesis: d_spec_B Conv-B Form's Relationship to the k=1 / k=2 Hörmander-Weyl Asymptotic Structure — τ-flow-DEFORMED k=1-like Interpolation vs Structural-Breakdown Reading

**Date**: 2026-05-07
**Agent**: lizzi-spectral-functional-theorist (FI/RD originator; primary author of `permanent-results-registry.md §VII.U.2 clause (e)` parse-tree decision procedure for algebra-INVARIANT vs algebra-DEPENDENT classification)
**Source Documents**:
- `sessions/archive/session-88/session-88-w6b-workingpaper.md` (912 lines; gates §W6b-53 / 54 / 55 / 56)
- `sessions/session-plan/session-88-plan-w6b.md` (500 lines)
- `sessions/archive/session-88/workshops/_seed-w6b.md` (workshop seed; tension framing)
- `sessions/permanent-results-registry.md` §VII.U.2 (four-corner classification, K=3 MANDATORY); §VII.U.6 W1b-T5 LANDING + §VII.U.6.k1-vs-k2 (lines 12988-13196); §VII.AF.1 (W-5 calibration corpus)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md` (FI/RD doctrine; spectral-functional-asymptotic perspective)
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3)
- `.claude/rules/joint-theorem-promotion.md` (4-stage Stage-1-CANDIDATE pathway)

---

## I. Session Outcome

The W6b-56 registry-note framing of `d_spec_B(τ) = 5/(1−τ/(5π))` as a "Jensen-perturbed Weyl-counting that interpolates between the k=2 bare-D form (recovers 8 at τ → 5π, the singularity of the HK-5 form) and a τ-dependent reading" is **STRUCTURALLY INCORRECT** and routes to **QUALIFY** (not RETRACT, not SUSTAIN-as-theorem-candidate). Under the lizzi (FI/RD spectral-functional-asymptotic) reading, `d_spec_B` is an algebra-INVARIANT spectrum-only-functional whose τ-flow trajectory passes through both k=1 (=5 at τ=0) and k=2 (=8 at τ=15π/8) numerical values as a continuous monotonic exponent — but `d_spec_B` is **not on the k=1/k=2 ladder**; the ladder is a discrete (k ∈ ℤ) classification of distinct rep-theoretic / spectral-asymptotic counting schemes, and a continuous Jensen-deformed exponent passing through those integer values at isolated τ-points is a **numerical coincidence at endpoints**, not a structural identification "as" a k=1-like or k=2-like exponent. The τ → 5π singularity is the **structural breakdown of the HK-5 closed-form** (Jensen-deformation regime of validity terminates), not an asymptotic "approach to k=2"; under the verified Python substitution chain, the trajectory passes through 8 at finite-interior τ = 15π/8 ≈ 5.89 and continues monotonically to +∞ at the boundary τ = 5π ≈ 15.71, so "recovers 8 at τ → 5π" is provably false. The W6b-54 Level-2 anatomy template `α = round(d_spec_B − 1) = 4` is **rescued** under the lizzi reading by a different derivation chain: not "k=1-like exponent minus 1" but "Jensen-deformed Weyl-counting exponent at τ_fold minus 1", which is structurally well-defined under W-5 anatomy template precedent regardless of k-ladder framing. The §VII.U.6 W1b-T5 LANDING **does** advance the cross-pillar-bridge K-counter as instance #2 (after W-5 §VII.AF instance #1) under both readings, but the registry note text MUST be qualified to remove the "interpolates between k=2 and k=1 endpoints" structural-claim language and re-cast as numerical-coincidence-at-endpoints language.

---

## II. Key Results

### Result 1 — Algebra-axis classification of `d_spec_B`: ALGEBRA-INVARIANT spectrum-only-functional

**Result**: `d_spec_B(τ_fold)` is an **algebra-INVARIANT** spectrum-only-functional in the sense of `permanent-results-registry.md §VII.U.2 clause (a)`, NOT an algebra-DEPENDENT state-pair-functional. Classification: **GEOMETRIC** (substrate spectral asymptotic).

`d_spec_B(τ)` is by construction the leading-order Weyl-counting EXPONENT of the Jensen-deformed Dirac operator `D_can(τ)`:

```
N(λ; τ) := #{eigenvalues of D_can(τ) below λ}
        ~ C(τ) · λ^{d_spec_B(τ)}      (λ → ∞)
```

This is a pure spectrum-only functional: the symbolic form references only `{λ_k(D_can(τ)), m_k(D_can(τ))}`, with no `π(a)` operator-algebra or `[D, π(a)]` commutator references. By the §VII.U.2 clause (e) parse-tree decision procedure (canonicalized at S88 §W5b-46 audit `_corner_classification_audit.py`), `d_spec_B` falls in the algebra-INVARIANT family **by symbolic form**. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3, this classification IS the relevant axis-tag for registry-bridge-anatomy basis eligibility: algebra-INVARIANT functionals are admissible as registry-bridge-anatomy basis (Corner I or II depending on Mellin pole). The Mellin pole is s=3 (substrate-distance-1) per the §VII.U.6 W1b-T5 LANDING block (which explicitly cites "Res[Tr(D_K^{-2s}); s=3]" as the substrate-IS observable). Therefore `d_spec_B` lives in **Corner I (INVARIANT × s=3)**.

The registry's existing W6b-56 framing "Jensen-perturbed Weyl-counting" is consistent with algebra-INVARIANT classification (Weyl counting IS spectrum-only). What is INconsistent is the "k=1-like" vs "k=2-like" identification language: k=1 and k=2 are two **discrete** members of a one-parameter family of rep-theoretic / spectral-asymptotic counts (`Σ dim(V_λ)^k` for `k ∈ {1, 2}`), each itself algebra-INVARIANT. A continuous Jensen-deformed exponent that happens to pass through `(d+r)/2 = 5` at τ=0 and through `d = 8` at τ = 15π/8 is **not in the same one-parameter family**; it is a different object (the Weyl-counting exponent of `D_can(τ)` for varying τ at fixed k=2 spectral-asymptotic notion).

### Result 2 — τ → 5π singularity interpretation: **structural breakdown** of HK-5 closed-form regime

**Result**: τ → 5π is a **structural breakdown** of the Jensen TT-deformation regime of validity, NOT an "asymptotic approach to k=2 = 8". Classification: **GEOMETRIC**.

**Substitution chain** (Python-verified inline):
- Definition: `slope_A(τ) = 5 / (1 − τ/(5π))`; `d_spec_B(τ) := slope_A(τ)` under Conv-B identification (S87 W1b-5).
- Substitute τ = 0: `slope_A(0) = 5/(1−0) = 5.0000` (matches `(d+r)/2 = 5` for SU(3) numerically).
- Substitute slope_A(τ) = 8: solve `5/(1−τ/(5π)) = 8` → `1−τ/(5π) = 5/8` → `τ/(5π) = 3/8` → `τ = 15π/8 ≈ 5.890486`.
- Substitute τ → 5π⁻: `1 − τ/(5π) → 0⁺`, so `slope_A → +∞` (Python: at τ = 5π − 10⁻⁴, slope_A = 7.854e+05; at τ = 5π − 10⁻³, slope_A = 7.854e+04; clear divergence).
- Direction: `slope_A(τ)` is monotonically increasing on `[0, 5π)`; passes through 8 at the **finite-interior** `τ = 15π/8 ≈ 5.89`, then continues monotonically through 9, 10, 13.7, 110.9, 9862.7 as τ approaches the boundary 5π. The boundary value is **+∞** (divergence), NOT 8.

The W6b-56 registry-note phrase "recovers 8 at τ → 5π, the singularity of the HK-5 form" is therefore **provably structurally incorrect**. The HK-5 closed-form trajectory does not "recover" 8 at the boundary; it **passes through** 8 at a finite-interior τ and then **diverges** to +∞. The boundary singularity τ = 5π is the structural breakdown of the closed-form (Jensen TT-deformation regime of validity terminates at the radius `τ_max < 5π`); the closed-form's predictive content for `d_spec_B(τ)` is restricted to its regime-of-validity domain `τ ∈ [0, τ_max]` with `τ_max < 5π`, NOT to the entire interval `[0, 5π)`. At τ_fold = 0.19 << 5π, we are deep inside the regime of validity and `d_spec_B(τ_fold) ≈ 5.061` is a well-defined Jensen-deformed Weyl exponent — but extrapolating this to "the trajectory continues to k=2 at the boundary" is a category error: the closed-form has no validity at the boundary, and the numerical pass-through at τ = 15π/8 has no structural interpretation as "the k=2 value".

The connes reading per the workshop seed — "the trajectory from k=1 (at τ=0) toward divergence (at τ → 5π) IS an extrapolation toward k=2 = 8 via a finite-τ pass-through at τ = 15π/8" — fails on two grounds:
1. **The trajectory does not stop at 8**: it passes through 8 monotonically and continues to +∞. There is no asymptotic structure that singles out 8 as "the limiting value"; 8 is an arbitrary point on the trajectory.
2. **The boundary itself is structurally undefined**: the HK-5 closed-form's regime of validity is bounded; the boundary τ = 5π is OUTSIDE the validity domain. Saying "what happens at the boundary" is inadmissible per the closed-form's intended scope.

The `slope_A(0) = 5 = (d+r)/2` numerical coincidence at τ=0 has the same epistemic status as the `slope_A(15π/8) = 8 = d` numerical coincidence at finite interior: both are points on the continuous Jensen-deformation trajectory that happen to numerically equal integer Weyl-count values for SU(3). Neither coincidence makes `d_spec_B` "structurally a k=1-like" or "k=2-like" exponent. They are just numerical pass-throughs.

### Result 3 — W6b-54 Level-2 anatomy template `α = round(d_spec_B − 1) = 4`: derivation rescued under different chain

**Result**: The W6b-54 Level-2 envelope `|residual(L)| ≤ 10⁻⁸ · L⁻⁴` with α=4 **survives** the lizzi reading, but via a **different derivation chain** than "k=1-like Jensen-deformed exponent minus 1". The replacement chain is "Jensen-deformed Weyl-counting exponent at τ_fold minus 1", a structurally well-defined extension of W-5 anatomy template precedent. Classification: **GEOMETRIC**.

**Substitution chain** (W-5 anatomy template generalization):
- W-5 Level-2 envelope at d=4 (Pillar III ↔ Pillar IV bridge, §VII.AF.1): exponent α = d − 1 = 3.
- Substrate-physics interpretation of W-5 α-template: the algebraic envelope rate `L⁻ᵅ` for the convergence of finite-L Hochschild pairing to its HKR `L_max → ∞` image is governed by the Mellin-Strip dimensional weight of the substrate's Dirac-operator Weyl exponent at the pole. At W-5, the substrate's Dirac operator is bare (`D_can(τ=0)` equivalent on Pillar III), so the Weyl exponent equals the bare manifold dim d=4, and α = d − 1 = 3.
- §VII.U.6 generalization (Jensen-deformed substrate): the substrate's Dirac operator is Jensen-deformed (`D_can(τ_fold)` with τ_fold = 0.19), so the Weyl exponent equals `d_spec_B(τ_fold) ≈ 5.061`, and `α_template = round(5.061 − 1) = round(4.061) = 4`.
- Direction: α = 4 follows from the W-5 anatomy template precedent **without** invoking any "k=1-like" identification of `d_spec_B`. The replacement narrative is: "α equals the Weyl exponent at the operative τ-anchor minus 1, where the Weyl exponent reduces to the bare manifold dim in the bare-D limit (W-5 case) and to the Jensen-deformed value in the deformed case (§VII.U.6 case)". This derivation is structurally correct under the lizzi reading because it cites only the algebra-INVARIANT Weyl-exponent role of `d_spec_B` (its content as a substrate-IS spectrum-only functional), not its position on the k=1 / k=2 ladder.

The connes-reading derivation chain — "α = (k=1-like exponent at τ_fold) − 1 = 4" — and the lizzi-reading derivation chain — "α = (Jensen-deformed Weyl exponent at τ_fold) − 1 = 4" — yield the **same numerical value** α = 4 but rest on **structurally distinct** justifications. This is the workshop's adjudicable substrate-physics question, and the lizzi-reading derivation is the structurally-canonical one because:

(i) It does not require `d_spec_B` to be "on" the k=1 ladder (a structural commitment that fails per Result 2).

(ii) It generalizes the W-5 anatomy template precedent **uniformly**: at any τ where the Jensen-deformed Weyl exponent is defined and within regime of validity, the template applies with α = round(exponent − 1). This recovers W-5 (τ=0 → exponent = d = 4 → α=3) and extends to §VII.U.6 (τ=τ_fold → exponent = `d_spec_B` ≈ 5.061 → α=4) under the same algebraic identity.

(iii) It avoids the structurally-incorrect "interpolation between k-endpoints" framing while preserving all the numerical pinning of the W6b-54 audit (α=4, C=10⁻⁸, strict Level-3 < Level-2 by 16 OOM).

The W6b-54 verdict (PASS at audit_sha256=`c44fb8857449c7ae...`) **stands** under the lizzi reading; only the interpretive narrative for the α-template generalization changes.

### Result 4 — W6b-56 registry note framing: QUALIFY (not SUSTAIN, not RETRACT)

**Result**: The W6b-56 registry note `### §VII.U.6.k1-vs-k2` requires qualifying edits to the final paragraph (lines 13186 of the registry) replacing "interpolates between the k=2 bare-D form (recovers 8 at τ → 5π, the singularity of the HK-5 form) and a τ-dependent reading" with structurally-correct numerical-coincidence-at-endpoints language. The body of the note (Hörmander-Weyl general form, k=2 vs k=1 distinction at the static-rep-theoretic level, SU(N) cross-check table) is **structurally correct** and stands. Only the bridge to `d_spec_B` requires qualifying. Classification: **GEOMETRIC** (registry-text qualification).

The qualifying edit (proposed verbatim replacement of registry line 13186):

**BEFORE** (current):
> "For G = SU(3): k=1 exponent = 5; k=2 exponent = 8. The bare manifold dim = 8 (HK-3 binding) IS the k=2 exponent. The d_spec_B = 5/(1−τ/(5π)) Conv-B form (per S88 W6b-53 landing; ≈5.061 at τ_fold) is the τ-flow-DEFORMED k=1-like exponent under Jensen flow on D_can — NOT a static k=1 dim-sum, but a Jensen-perturbed Weyl-counting that interpolates between the k=2 bare-D form (recovers 8 at τ → 5π, the singularity of the HK-5 form) and a τ-dependent reading."

**AFTER** (proposed under QUALIFY):
> "For G = SU(3): k=1 exponent = 5; k=2 exponent = 8. The bare manifold dim = 8 (HK-3 binding) IS the k=2 exponent. The d_spec_B = 5/(1−τ/(5π)) Conv-B form (per S88 W6b-53 landing; ≈5.061 at τ_fold) is the **Jensen-deformed Weyl-counting exponent of D_can(τ)** — algebra-INVARIANT spectrum-only functional in the sense of §VII.U.2 clause (a). At τ=0 the exponent **numerically coincides** with the SU(3) k=1 rep-theoretic value (`(d+r)/2 = 5`); at the finite-interior τ = 15π/8 ≈ 5.890 the exponent **numerically coincides** with the SU(3) k=2 spectral-asymptotic value (d = 8). These coincidences are pass-throughs of the continuous τ-flow trajectory, NOT structural identifications of d_spec_B as a k=1-like or k=2-like exponent: d_spec_B is the τ-flow-tracked Weyl exponent at fixed k=2 spectral-asymptotic notion, evaluated on the Jensen-deformed Dirac operator. The boundary τ → 5π is the **structural breakdown of the HK-5 closed-form regime of validity** (Jensen TT-deformation domain terminates at radius τ_max < 5π); slope_A(τ) → +∞ at the boundary by direct calculation (Python-verified: at τ = 5π−10⁻⁴, slope_A ≈ 7.85e+05), NOT a 'recovery to k=2'. The Jensen TT-deformation regime of validity bounds the closed-form's predictive scope; at τ_fold = 0.19 << 5π we are deep inside the regime."

This QUALIFY revision preserves the 4 Sage-MCP-verified cross-checks (SU(2)/SU(3)/SU(4) k=1/k=2 identities), the general Hörmander-Weyl form, the cross-links to W-5 / W6b-53/54/55, and the §VII.U.6.k1-vs-k2 sub-section's structural utility (resolving the S87 W2 R3 conflation surface). It removes the structurally-incorrect "interpolation between k-endpoints" framing AND the provably-false "recovers 8 at τ → 5π" claim. The W6b-56 verdict (PASS at audit_sha256=`d7b57347e82703cd...`) stands; only the registry text is qualified.

### Result 5 — Cross-pillar-bridge K-counter advancement: §VII.U.6 W1b-T5 LANDING is INELIGIBLE as instance #2 under hybrid independence test

**Result**: §VII.U.6 W1b-T5 LANDING is **INELIGIBLE** for cross-pillar-bridge K-counter advancement as calibration-corpus instance #2 under the **Hybrid Independence Test** of `cross-pillar-bridge-anatomy.md §"Forward template-adoption" §"Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"`. Classification: **GEOMETRIC** (K-counter accounting).

**Hybrid Independence Test substitution chain** `(i ∨ ii ∨ iii) ∧ (iv)`:
- W-5 §VII.AF.1 instance #1 anchors:
  - Substrate-IS pillar (i): Pillar III (HP^1 cohomology on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}))
  - Laboratory-IN pillar (ii): Pillar IV (Peotta-Törmä continuum BZ-trace)
  - Bridge map (iii): HKR `L_max → ∞`
  - Algebraic envelope (iv): `L⁻³` at d=4 with C=1 (Sage-rational)
- §VII.U.6 candidate instance #2 anchors:
  - Substrate-IS pillar (i): Pillar III (Mellin-cone evaluator residue at substrate-distance-1 pole on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10})) — **SAME pillar as W-5 instance #1**.
  - Laboratory-IN pillar (ii): continuum Mellin-cone strip integral over `Re(s) ∈ (3-ε, 3+ε)` — distinct from W-5's continuum BZ-trace, **but on the same Pillar III substrate** (the laboratory-IN side is the continuum image of the same finite-spectral-triple substrate).
  - Bridge map (iii): HKR `L_max → ∞` — **SAME bridge-map class as W-5 instance #1**.
  - Algebraic envelope (iv): `L⁻⁴` at α=4 with C=10⁻⁸ — **independent algebraic envelope** (different (α, C) pair from W-5; not a numerical refinement; structurally distinct exponent rationale).

Hybrid Independence Test clauses:
- (i) FAIL: same substrate-IS pillar as W-5.
- (ii) MARGINAL: laboratory-IN observable is a different continuum integration domain (Mellin-strip vs BZ-trace) but built on the same Pillar III substrate; arguably FAIL under strict reading.
- (iii) FAIL: same HKR bridge-map class as W-5.
- (iv) PASS: independent algebraic envelope with structurally distinct (α, C) pair.

`(i ∨ ii ∨ iii)` ⇒ at best MARGINAL on clause (ii); strict reading FAILs all three. `(iv)` PASS does not rescue: the test requires `(i ∨ ii ∨ iii) ∧ (iv)` (logical AND with the disjunction).

**Direction**: the §VII.U.6 W1b-T5 LANDING is a **shared-anchor companion** to the W-5 §VII.AF.1 instance #1 with partial-axes-distinct content (only clause (iv) cleanly distinct). Per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` §"Companion-entry tagging (retroactive)" calibration corpus K=1 baseline (the §VII.AG.1 W6-1 precedent), §VII.U.6 W1b-T5 LANDING SHOULD be tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and recorded **OUTSIDE** the Hybrid Independence Test K-counter table. It retains full registry-entry status (the 5-anatomy + 3-level declaration is valid for cross-citation purposes) but does NOT advance the K-counter toward the K=3 MANDATORY status of the Hybrid Independence Test.

This is consistent with the §VII.AG.1 W6-1 precedent that the algebra-axis-orthogonality K-counter (which IS at K=3 MANDATORY) and the Hybrid Independence Test K-counter (which is at K=1 SUGGESTION pending K=3 MANDATORY promotion) operate at distinct epistemic layers. The §VII.U.6 W1b-T5 LANDING contributes to the algebra-axis-orthogonality K-counter (Corner I instance) but not to the Hybrid Independence Test K-counter.

The CF-W6b-C carry-forward in the W6b seed (which proposes to register §VII.U.6 W1b-T5 LANDING as instance #2) requires **structural revision** before dispatch: the Hybrid Independence Test failure on clauses (i)+(iii) (and arguably (ii)) routes the entry to companion-tagging, NOT K-counter advancement.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W6b-53 (CONV-B-RE-PIN) | PASS (sustained) | residual = 2.615e−05 (closed-form HK-5 vs Richardson L⁻³); `d_spec_B(τ_fold) = 5.0612193741921109` (Sage QQ-π exact) |
| §W6b-54 (LEVEL-2-ENVELOPE-AUDIT) | PASS (sustained) | (α=4, C=1/10⁸); Level-3 / Level-2 = 8.066e−16 (16 OOM strict-< margin) |
| §W6b-55 (SUBSTRATE-FRAMING-EDIT) | PASS (sustained) | 5 forbidden = 0; 3 required = 1; W6b-53 duplication fixed |
| §W6b-56 (K1-VS-K2-COUNTING-DISTINCTION) | PASS-with-QUALIFY | Hörmander-Weyl form + SU(N) table sustained; final-paragraph `d_spec_B`-bridging language qualified per Result 4 |

Workshop-1 structural verdict (this synthesis) is the registry-text qualification of W6b-56's final paragraph + INELIGIBILITY tagging of §VII.U.6 W1b-T5 LANDING for Hybrid Independence Test K-counter advancement.

---

## IV. Structural Implications

### What opened

1. **Algebra-axis classification of `d_spec_B` is FIXED at Corner I (INVARIANT × s=3)** under the §VII.U.2 clause (e) parse-tree decision procedure. Future entries citing `d_spec_B(τ)` MUST declare this corner-cell explicitly per §VII.U.2 clause (d) MANDATORY-K=3 enforcement; cross-corner co-primary structure with Corner III/IV entries is FORBIDDEN per clause (f).

2. **SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE companion-tagging precedent** for §VII.U.6 W1b-T5 LANDING is the second invocation (after §VII.AG.1 W6-1) of this distinction in `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`. The Hybrid Independence Test K-counter remains at K=1 (the W-5 §VII.AF.1 baseline); §VII.U.6 W1b-T5 LANDING does NOT advance it. This is a structural finding about the K-counter's epistemic granularity: cross-pillar bridges that share substrate-IS pillar AND bridge-map class are companions, not independent calibration corpus instances.

3. **The W-5 anatomy template `α = round(Weyl exponent at operative τ-anchor − 1)`** is the lizzi-reading canonical generalization. Replaces the W6b-54-cited "α = round(d_spec_B − 1)" framing while preserving numerical content. Future cross-pillar-bridge Level-2 envelope landings on Jensen-deformed substrates SHOULD adopt this canonical generalization as the algebraic-envelope α-derivation.

### What closed

1. **The "interpolation between k=1 and k=2 endpoints" structural-claim language in W6b-56 is closed**: provably false per Result 2 (slope_A passes through 8 at finite-interior τ, not boundary; slope_A → +∞ at boundary). This closes a substrate-IS misreading that, if propagated, would contaminate downstream cites of d_spec_B's algebra-axis classification.

2. **The "recovers 8 at τ → 5π" registry text is closed as Class-(c) PIN-DRIFT-FROM-STALE-SOURCE** under `epistemic-discipline.md §"Source Reconciliation"`. The plan §W6b-56 wrote the claim against a pre-Python-verified version of the slope_A trajectory; Python verification (substitution chain verified inline in this synthesis) shows the trajectory diverges at the boundary, not "recovers" 8. Qualifies for in-session correction per `feedback_fix-in-session-never-defer.md`; mack-cosmic-bridge sole-writer applies the QUALIFY edit.

3. **The connes-reading "asymptotic approach to k=2" interpretation is closed**: τ → 5π is structural breakdown, not asymptotic limit. The closed-form's regime of validity bounds the predictive content; extrapolating outside that bound is inadmissible.

### What shifted

1. **The W6b-56 verdict shifts from PASS-as-substrate-IS-theorem-candidate to PASS-with-QUALIFY**. The SU(N) cross-check table + Hörmander-Weyl general form remain canonical; the d_spec_B-bridging language requires qualifying. This is not a retraction (the gate's PASS predicate satisfaction is unchanged); it is a qualification of the structural narrative.

2. **The CF-W6b-C carry-forward (cross-pillar-bridge K-counter advancement) shifts from "register as instance #2" to "tag as SHARED-ANCHOR-COMPANION"**. The registry edit pattern is structurally different: companion-tagging preserves the §VII.U.6 W1b-T5 LANDING's full anatomy declaration without advancing the Hybrid Independence Test K-counter.

3. **Constraint-map row "k=1 vs k=2 conflation registered at §VII.U.6.k1-vs-k2"** stands but with the qualifying edit: the conflation IS resolved at the Hörmander-Weyl static-counting level (k=1 dim-sum vs k=2 spectral-asymptotic), independent of any d_spec_B identification. The d_spec_B story is a separate (Jensen-deformation) layer that is structurally orthogonal to the static k-classification.

---

## V. Carry-Forward Computations

V.1. **Apply QUALIFY edit to §VII.U.6.k1-vs-k2 final paragraph (registry line 13186)**
   - **What**: Replace W6b-56's structurally-incorrect "interpolates between the k=2 bare-D form (recovers 8 at τ → 5π, the singularity of the HK-5 form) and a τ-dependent reading" language with the verbatim AFTER-text from Result 4 above (numerical-coincidence-at-endpoints framing + structural-breakdown-not-asymptotic-limit framing + boundary-out-of-regime-of-validity caveat). Retain Hörmander-Weyl form, SU(N) cross-check table, and 4 cross-links unchanged. Forbidden_target = current line-13186 paragraph; required_replacement = AFTER-text from this synthesis Result 4. Edit must be performed by mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.
   - **Inputs**: This synthesis Result 4 AFTER-text verbatim; W6b-56 verdict line audit_sha256=`d7b57347e82703cda5648181b9dadb999c8cf651775eb46942d9f23741d5b02a` (anchor for the existing PASS); Python-verified slope_A trajectory data (this synthesis Result 2 inline verification).
   - **Gate**: `S89-W6B-56-K1-VS-K2-REGISTRY-NOTE-QUALIFY` (METHODOLOGY-class per `wave-classification.md` M1-M4; rule-file/registry edit with artifact-existence-with-substantive-content predicate). PASS criterion: post-edit grep `interpolates between the k=2 bare-D form` returns 0; post-edit grep `Jensen-deformed Weyl-counting exponent of D_can(τ)` returns ≥ 1; post-edit grep `numerical-coincidence` (within new paragraph) returns ≥ 1; post-edit grep `structural breakdown of the HK-5 closed-form regime of validity` returns ≥ 1; SU(N) cross-check table + 4 cross-links unchanged. INFO if pre-edit already shows post-edit state. FAIL if any condition violated.
   - **Effort**: 0.3 wave-equivalents (single targeted registry-edit gate; no spectral computation; mack-cosmic-bridge orchestrator-direct-write).

V.2. **Tag §VII.U.6 W1b-T5 LANDING as SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE under Hybrid Independence Test**
   - **What**: Append a new audit-trail line to the §VII.U.6 W1b-T5 LANDING block (after line 13157 cross-references, before the closing `---` at line 13160 pre-W6b-56) recording the companion-tagging decision per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"` §"Companion-entry tagging (retroactive)". The line should read: "**Hybrid Independence Test classification** (S88 W21 lizzi-spectral-functional-theorist synthesis, 2026-05-07): SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE relative to W-5 §VII.AF.1 instance #1 (clause (iv) algebraic envelope (α=4, C=10⁻⁸) is independent of W-5's (α=3, C=1); clauses (i) substrate-IS Pillar III + (iii) HKR bridge-map are SHARED with W-5; clause (ii) laboratory-IN observable is Mellin-strip integral vs W-5's BZ-trace, MARGINAL on strict reading). This entry is recorded OUTSIDE the Hybrid Independence Test K-counter table; full registry-entry status retained for cross-citation purposes."
   - **Inputs**: This synthesis Result 5 substitution chain verbatim; `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` §"Companion-entry tagging (retroactive)"; §VII.AG.1 W6-1 precedent (the K=1 baseline calibration instance for SHARED-ANCHOR-COMPANION tagging); W6b-54 verdict line audit_sha256=`c44fb8857449c7ae73256e3d129dd8852d6d051ad89a4648d747f759ad083af8` (anchor for the (α=4, C=10⁻⁸) Level-2 pin).
   - **Gate**: `S89-VII-U-6-HYBRID-INDEPENDENCE-COMPANION-TAGGING` (METHODOLOGY-class). PASS criterion: post-edit grep `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` in §VII.U.6 W1b-T5 LANDING block returns ≥ 1; post-edit grep `OUTSIDE the Hybrid Independence Test K-counter` returns ≥ 1; pre-edit no occurrences. INFO if pre-edit already shows post-edit state.
   - **Effort**: 0.3 wave-equivalents (single targeted registry-edit gate; no spectral computation; mack-cosmic-bridge orchestrator-direct-write).

V.3. **Re-derive W6b-54 Level-2 anatomy template generalization under the lizzi-canonical "Jensen-deformed Weyl exponent at operative τ-anchor minus 1" formulation**
   - **What**: Revise the §VII.U.6 W1b-T5 LANDING `5-element IS-not-IN anatomy` element 4 (lines 13066-13075) to replace the current "W-5 cross-pillar-bridge-anatomy template `α = round(d_spec_B − 1)` at `d_spec_B(tau_fold) ≈ 5.061`" language with the lizzi-canonical formulation: "W-5 cross-pillar-bridge-anatomy template `α = round(W_τ − 1)` where W_τ is the Weyl-counting exponent of D_can(τ) at the operative τ-anchor (in the bare-D limit τ=0, W_τ reduces to the bare manifold dim d; in the Jensen-deformed case τ=τ_fold, W_τ equals d_spec_B(τ_fold)). At W-5: τ=0, W_0 = d = 4, α = 3. At §VII.U.6: τ=τ_fold = 0.19, W_τ_fold = d_spec_B(τ_fold) ≈ 5.061, α = round(4.061) = 4." Numerical values unchanged; derivation chain replaced with structurally-canonical version.
   - **Inputs**: This synthesis Result 3 substitution chain verbatim; W-5 §VII.AF.1 calibration corpus block (lines 14588-14618 of registry); W6b-54 verdict + content_sha256=`04f5b7bcf45345c5...` (current Level-2 envelope text); §VII.U.6 W1b-T5 LANDING current 5-anatomy block (lines 13066-13075).
   - **Gate**: `S89-VII-U-6-LEVEL-2-ANATOMY-LIZZI-CANONICAL-RECAST` (METHODOLOGY-class). PASS criterion: post-edit grep `Jensen-deformed Weyl-counting exponent of D_can(τ)` in §VII.U.6 W1b-T5 LANDING anatomy element 4 returns ≥ 1; post-edit grep `α = round(W_τ − 1)` returns ≥ 1; pre-edit no occurrences; numerical content (α=4, C=10⁻⁸, envelope=1e-12 at L_max=10) preserved verbatim.
   - **Effort**: 0.3 wave-equivalents (single targeted registry-edit gate; mack-cosmic-bridge orchestrator-direct-write).

V.4. **§VII.U.2 audit re-annotation of §VII.U.6 W1b-T5 LANDING as Corner I (INVARIANT × s=3)** — confirm post-W6b-56-QUALIFY consistency
   - **What**: Re-run `_corner_classification_audit.py` on the post-V.1 (QUALIFY-edited) and post-V.3 (lizzi-canonical-recast) §VII.U.6 W1b-T5 LANDING block to confirm Corner I assignment is preserved under the qualified registry text. The §VII.U.2 W5b-46 audit currently classifies §VII.U.6 W1b-T5 LANDING as Corner I via lexical s=3 marker presence; the QUALIFY edit MUST preserve this lexical content. Audit-script PASS criterion: post-edit Corner I assignment preserved.
   - **Inputs**: `computations/_shared/_corner_classification_audit.py` (S88 W5b-46); post-V.1 + post-V.3 registry SHA; §VII.U.2 clause (e) parse-tree decision procedure pinned at 12930 of registry; canonical S87 W1a §VII.U.6 W1b-T5 LANDING audit_sha256=`74c16f36e83643f121948b969da1e1a4270a982c0974a94e39442c96710ad3bb` (landing anchor).
   - **Gate**: `S89-VII-U-2-AUDIT-RE-RUN-VII-U-6-CORNER-PRESERVATION` (COMPUTE-class; this is a re-evaluation of an existing audit script's Corner output, NOT a registry edit). PASS criterion: audit_output.corner_assignment(§VII.U.6 W1b-T5 LANDING) == "I" post-edit. FAIL if Corner shifts (would indicate the QUALIFY edit accidentally removed the s=3 lexical marker; in-session remediation per `feedback_fix-in-session-never-defer.md`).
   - **Effort**: 0.2 wave-equivalents (existing audit script re-run; no new infrastructure).

V.5. **Future closed-form HK-5 regime-of-validity τ_max bound derivation** (substantive substrate-physics carry-forward)
   - **What**: Derive an explicit τ_max bound for the HK-5 closed-form `slope_A(τ) = 5/(1−τ/(5π))` regime of validity. The boundary singularity at τ = 5π is the structural breakdown; the regime of validity is `τ ∈ [0, τ_max]` with `τ_max < 5π`, but the precise value of τ_max is not currently pinned. Approach: identify the τ at which the next-order Jensen-deformation correction (beyond the leading HK-5 closed form) becomes the same order as the leading term, defining the practical τ_max. Output τ_max as a new canonical_constants pin `tau_max_HK5_regime`.
   - **Inputs**: S87 W1b-3 / W1b-5 producing scripts; closed-form HK-5 derivation in S87 W1b-5 workshop; canonical_constants `tau_fold = 0.19` and `M_KK = 7.429e16` for context.
   - **Gate**: `S89-HK5-REGIME-OF-VALIDITY-TAU-MAX-DERIVATION` (COMPUTE-class). PASS criterion: τ_max pinned with PROVENANCE entry in canonical_constants.py; τ_fold = 0.19 < τ_max with margin ≥ 10× (i.e., τ_max ≥ 1.9). INFO if τ_max in [0.5, 1.9] (margin tighter than 10× but τ_fold still inside regime); FAIL if τ_max < τ_fold (would invalidate the W6b-53 Conv-B canonical landing's regime-of-validity premise).
   - **Effort**: 0.6 wave-equivalents (substantive derivation; gen-physicist or lizzi-spectral-functional-theorist solo).

V.6. **Plan-authorship discipline extension: pre-Python-verify boundary/asymptotic claims for closed-form τ-flow trajectories**
   - **What**: Extend `epistemic-discipline.md §"Pre-Registration Completeness — PRDR (Pre-Registration Dry-Run)"` Class 8.2 verifier-rubric pre-registration corpus with a NEW calibration instance: W6b-56 plan §W6b-56 substitution-chain-Step claim "recovers 8 at τ → 5π" was structurally false under direct Python verification (slope_A → +∞ at boundary). Forward-enforcement: any plan-block claiming an asymptotic limit / boundary value for a closed-form τ-flow trajectory MUST pre-flight Python-verify the boundary direction at plan-freeze. Companion: extend the 5A Sub-diff B `_machinery_feasibility_audit.py` with a "boundary direction substitution chain" sub-check.
   - **Inputs**: This synthesis Result 2 substitution chain + Python verification; W6b-56 plan §W6b-56 substitution-chain Step (the structurally-incorrect "recovers 8 at τ → 5π" claim); existing Class 8.2 calibration corpus at `sessions/framework/registry/pru-class-corpus.md §1`.
   - **Gate**: `S89-PRU-CLASS-8-2-EXTENSION-W6B-56-BOUNDARY-DIRECTION` (METHODOLOGY-class per `wave-classification.md` M1-M4; rule-file extension; M4 allowlist append at plan-freeze). PASS criterion: artifact-existence-with-substantive-content (Class 8.2 corpus row appended; cross-link to W6b-56 verdict-line audit_sha256; substitution chain pin specified for "boundary direction" sub-check). INFO if pre-edit already shows the extension landed.
   - **Effort**: 0.4 wave-equivalents (rule-file extension + calibration-corpus row append + audit-script extension queue).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | d_spec_B is algebra-INVARIANT spectrum-only-functional | GEOMETRIC | STRUCTURAL VERDICT | Corner I (INVARIANT × s=3) per §VII.U.2 clause (e); registry-bridge-anatomy basis eligible; cross-corner co-primary FORBIDDEN with Corner III/IV |
| 2 | τ → 5π is structural breakdown, NOT asymptotic approach to k=2 | GEOMETRIC | STRUCTURAL VERDICT (Python-verified) | "Recovers 8 at τ → 5π" claim is provably false; slope_A → +∞ at boundary; trajectory passes through 8 at finite-interior τ = 15π/8 ≈ 5.89 then continues monotonically to +∞ |
| 3 | W6b-54 α=4 derivation rescued under lizzi-canonical chain | GEOMETRIC | STRUCTURAL VERDICT | Replacement chain "α = round(W_τ − 1)" generalizes W-5 anatomy template uniformly; numerical content α=4, C=10⁻⁸ unchanged; W6b-54 verdict stands |
| 4 | W6b-56 registry note framing: QUALIFY (not SUSTAIN, not RETRACT) | GEOMETRIC | QUALIFY | Final-paragraph "interpolates between k-endpoints" language replaced with numerical-coincidence-at-endpoints + structural-breakdown-at-boundary framing; Hörmander-Weyl form + SU(N) table + cross-links sustained |
| 5 | §VII.U.6 W1b-T5 LANDING is INELIGIBLE for Hybrid Independence Test K-counter advancement | GEOMETRIC | STRUCTURAL VERDICT | Tag as SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE; record OUTSIDE Hybrid Independence Test K-counter table; preserves full registry-entry status; CF-W6b-C carry-forward requires structural revision before dispatch |

---

## VII. Algebra-Axis / IS-not-IN Substrate Framing

Per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`, the direction of explanation in this synthesis flows uniformly:

```
substrate spectral content (D_can(τ) eigenvalue distribution at fixed τ)
   → Weyl-counting exponent W_τ as algebra-INVARIANT spectrum-only functional (Corner I)
   → closed-form HK-5 representation slope_A(τ) = 5/(1−τ/(5π)) on regime of validity τ ∈ [0, τ_max]
   → numerical pass-through at integer Weyl-count values (5 at τ=0; 8 at τ = 15π/8) — coincidences, not structural identifications
   → boundary structural breakdown at τ = 5π (Jensen TT-deformation regime terminates)
   → laboratory-IN observable (Mellin-strip integral on continuum image) via HKR L_max → ∞ bridge
```

`d_spec_B(τ)` IS the τ-flow-tracked Weyl exponent of the substrate's Jensen-deformed Dirac operator. The substrate IS the spectral triple `(A_K, H_K, D_K(τ))`; `d_spec_B` is an emergent spectral asymptotic property, NOT a "dimension of an NCG cone the substrate inhabits". The k=1 / k=2 ladder is a discrete classification of distinct rep-theoretic / spectral-asymptotic counting schemes operating on the **same** spectrum; `d_spec_B(τ)` is a continuous Jensen-deformation exponent at fixed-k=2 spectral-asymptotic notion. The two layers are STRUCTURALLY ORTHOGONAL per the §VII.U.2 algebra-axis / Mellin-pole 4-corner classification (which itself is MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`).

The lizzi-reading insistence on numerical-coincidence-at-endpoints language (rather than "interpolation between k-endpoints" structural-claim language) IS the substrate-IS reading: the trajectory's pass-throughs at integer Weyl-count values are **observations** about a continuous substrate-IS quantity, NOT **identifications** of that quantity with a discrete-k member of the ladder. Treating `d_spec_B` as "k=1-like at one end and k=2-like at the other" is the kind of category error that `phononic-framing.md` §"The Error Pattern" specifically forbids: it inverts substrate (the Jensen-deformed exponent) and emergent (the discrete k-ladder of static counting schemes), making the substrate a "thing on the ladder" rather than what it IS — a τ-flow-tracked spectrum-only functional intrinsic to the deformation manifold.

---

**End of Workshop W21 Synthesis** — d_spec_B Conv-B form's relationship to k=1/k=2 Hörmander-Weyl asymptotic structure: STRUCTURAL VERDICT QUALIFY on W6b-56 registry-note framing; algebra-axis classification Corner I; W6b-54 α=4 rescued under lizzi-canonical chain; §VII.U.6 W1b-T5 LANDING INELIGIBLE for Hybrid Independence Test K-counter advancement, SHARED-ANCHOR-COMPANION tagged. Six structured carry-forward computations enumerated (V.1-V.6) covering registry-text qualification, companion-tagging, anatomy-template recast, audit re-run, regime-of-validity τ_max derivation, and PRU Class 8.2 calibration-corpus extension. Workshop verdict produces NEW pinned positions on all five sub-questions of the seed file's adjudication question; output is the QUALIFY routing (registry text qualified, NOT new STAGE-1-CANDIDATE entry per joint-theorem-promotion.md); future cites of d_spec_B's k=1/k=2 relationship MUST resolve to Result 1 (algebra-axis classification) + Result 2 (boundary as structural breakdown, not asymptotic approach) + Result 3 (W-5 anatomy template generalization under lizzi-canonical chain).
