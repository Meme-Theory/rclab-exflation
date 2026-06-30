# WS-S112-7 YUKSHAPE — Round 1
## paasch-mass-quantization-analyst — Round 1, steelman Reading B (permanent wall)

**Thesis (one line):** No G-invariant construction on `(A_K, H_K, D_K)` — Casimir-graded *or* full-SU(3) σ-model — can supply a non-monotone sign-changing scalar across the quark-generation sectors, because the same property (homogeneity ⇒ multiplicity-scalar) that forbids the Casimir-graded handle forbids EVERY G-invariant handle; the only escape (drop order-one / enlarge the algebra) provably leaves the substrate's admissible 7-axiom class and adds an unobserved gauge group. The SHAPE branch is therefore a PERMANENT wall, structurally identical in kind to the just-closed M_KK magnitude obstruction: the fermion SHAPE hierarchy is irreducibly EXTERNAL.

---

## 0. What is already pinned (query-first; do not re-litigate)

This workshop does not start from zero. The single-τ-slice version of Reading B is ALREADY a STAGE-3-PERMANENT registry theorem. I cite it as the anchor and then defend the one thing it does not literally close: the *off-Casimir / full-SU(3) σ-model* escape route that is the whole substance of the A↔B tension.

| Pinned object | Content | Source |
|:--|:--|:--|
| **§VII.BV** NO-SIGN-CHANGING-SLOPE-HANDLE (STAGE-3-PERMANENT) | Four routes (a inner-fluctuation / b spectrum-only G-moment / c twisted-inner `Ω¹_σ` / d opposite-action `JAJ⁻¹`) ALL yield UNIFORM `(+,+,+)`. `crossing_realized=False`, `sign_flip=False`, `uniform=True`. `C₂ tower = {4/3, 3, 6}`. | `permanent-results-registry.md §VII.BV`; verdict `S103-NO-SIGN-HANDLE-REGISTRY-LANDING: PASS` |
| **§VII.BL** ε_LX-EXTERNAL two-wall schema | (W1) reality `[J, D_K+ε_LX]=0` SATISFIABLE; (W2) homogeneity ⇒ multiplicity-scalar; (W3) every `A_K`-built form respects both walls ⇒ breaks NEITHER. **Corollary/design rule:** any hierarchy-discharging mechanism MUST be an external non-LI fibre connection breaking W2, non-gauge-removable (`P_nLI=‖ε_LX‖²>0`). | `permanent-results-registry.md §VII.BL` |
| **E7 Structural Monotonicity** | `dS_SA/dτ>0`; every G-invariant scalar moment factors through `C₂` and is monotone-in-C₂; per-sector slope sign is fixed for each k, all monotone f, all Λ, all 10 sectors. | knowledge MCP `proven`; `spectral-geometer-layers.md` Eq (4.12) |
| **S110 CV-8 Arm-G DEAD** | `CF1-YUK-C2COSET: FAIL`; the LAST untested internal geometric probe (off-U(2) C²-coset split) failed — "the whole left-invariant geometric corridor is DEAD." | `permanent-results-registry.md`; verdict `S110-CF1-YUK-C2COSET FAIL` |
| **S31 order-one assessment** | Dropping Axiom 5 ⇒ algebra stays `M₂(ℍ)⊕M₄(ℂ)`, gauge group = **Pati-Salam** `SU(2)_L×SU(2)_R×SU(4)_C`, NOT the SM. | `session-31-order-one-assessment.md` |
| **Paasch program** (my domain) | `φ_paasch` is INTER-SECTOR ONLY (`m_{(3,0)}/m_{(0,0)}`); NO intra-sector crossings; BCS `exp(−1/M)` categorically destroys φ-structure; `LOG-SIGNED-40` (the per-sector signed sum) single-signed `+787.773` at its one computed point. | `paasch-reference.md`; `PHI-BDG-47 FAIL` |

The tension that survives all of this: **does a full-SU(3) σ-model (beyond the C₂-graded ω-ladder) carry a non-monotone sign-changing DOF that the four enumerated routes missed?** My R1 case is that it does not, and *cannot*, while remaining a G-invariant construction on the substrate.

---

## 1. The exact thing that must exist for Reading A to win

State the target precisely so neither side strawmans. The joint up/down quark mass crossing (the observed fact that the up-type and down-type Yukawa hierarchies are *not* co-monotone across generations — `m_u≪m_c≪m_t` but `m_d<m_s<m_b` with a different inter-generation spacing, so the up/down RATIO is non-monotone in generation) requires, on the substrate, a **per-generation slope kernel**

```
κ_g(τ) := d/dτ [ scalar functional of the (p,q)_g sector content ],   g ∈ {gen1=(1,0), gen2=(1,1), gen3=(3,0)}
```

whose SIGN is NOT uniform across g — i.e. `∃ g, g'` with `sign(κ_g) ≠ sign(κ_{g'})` (the §VII.BV admissible-pattern condition `sign(κ₁^up − κ₁^dn) = −sign(d₁^dn − d₁^up)`).

Reading A's claim, stated charitably: the four routes (a)–(d) in §VII.BV are all built from the **C₂-graded ω-ladder / `A_K`-inner calculus**; a *full* SU(3) σ-model — a map `Σ: SU(3) → target` with its own field content, not reducible to a finite sum of `aᵢ[D_K, bᵢ]` — lives "outside the Casimir-graded sub-calculus" and might carry a sign-changing DOF.

**To win, Reading A must exhibit a functional `Φ` that is simultaneously:**
(R-i) **G-invariant** — invariant under the substrate's isometry `Isom(K, g_τ) = U(1)×SU(3)_R` (otherwise it is not a property of the homogeneous substrate; it is external data smuggled in);
(R-ii) **scalar-valued on each generation sector** — it must assign a per-gen slope `κ_g` (a number), because the observable is a per-gen mass slope;
(R-iii) **non-monotone in generation** — `sign(κ_g)` flips across `{(1,0),(1,1),(3,0)}`.

I will now argue (R-i) ∧ (R-ii) ⇒ ¬(R-iii). That is the wall.

---

## 2. The wall: homogeneity ⇒ multiplicity-scalar ⇒ the per-gen slope factors through C₂ ⇒ uniform sign

This is the load-bearing derivation. It is NOT specific to the inner-fluctuation calculus; it is a property of *any* G-invariant scalar built on a homogeneous spectral triple.

**Step 1 — left-invariance pins the representation to be multiplicity-scalar.**
`D_K` is left-invariant on `K = SU(3)` (Jensen-deformed). Left-invariance ⇒ `D_K` commutes with all right-translation generators `R_X`, `X ∈ su(3)`. By Peter–Weyl, `H_K = ⊕_{(p,q)} V_{(p,q)} ⊗ ℂ^{m(p,q)} ⊗ ℂ^{16}`, where the **left-regular** factor `V_{(p,q)}` carries the `R_X`-action and the **multiplicity** factor `ℂ^{m(p,q)}` is `R_X`-INERT. Therefore `D_K` acts as a SCALAR on `ℂ^{m(p,q)}`:
```
D_K = ⊕_{(p,q)} D_{(p,q)} ⊗ 1_{m(p,q)} ,        [§VII.BL (W2); permanent-results-registry.md]
```
and the generation index IS the multiplicity index `t = (p−q) mod 3` (`proven_384`; SM generations = SU(3) Z₃-triality multiplicity).

**Step 2 — every G-invariant scalar functional factors through the Casimir.**
Let `Φ` be ANY functional satisfying (R-i)+(R-ii): G-invariant and scalar on each sector. By Schur's lemma on the simple block `V_{(p,q)}`, the only `SU(3)_R`-invariant operators on `V_{(p,q)}` are multiples of the identity; their invariant labels are the Casimir eigenvalues. For a *spectral* functional this is literally `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` with `λ_k` and `m_k` sector-labelled by `(p,q)` — and on the homogeneous fiber `λ²_{(p,q)} ∝ C₂(p,q) + const` (the Casimir IS the Laplacian on the group). Hence
```
Φ|_{sector (p,q)} = Φ̂(C₂(p,q))                  for some single function Φ̂.       (★)
```
There is no *additional* invariant on a simple SU(3) block to depend on. This is exactly the **§VII.BV route-(b) statement** and the **E7 monotone-in-C₂ statement** — and crucially it is stated for the WHOLE algebra-INVARIANT family `F({λ_k,m_k})`, not just the inner-fluctuation sub-calculus.

**Step 3 — the C₂ tower is strictly monotone, so a monotone Φ̂ gives a uniform-sign slope.**
The three quark-generation sectors carry
```
C₂(1,0) = 4/3 ,  C₂(1,1) = 3 ,  C₂(3,0) = 6      (strictly increasing, all positive; §VII.BV Def 2)
```
The per-gen slope is `κ_g(τ) = d/dτ Φ̂(C₂(g); τ)`. By the E7 theorem the τ-flow `⟨λ²⟩` is monotone (`d⟨λ²⟩/dτ>0`), and `a_{2k}(τ)` has FIXED sign for each k across all sectors (Eq 4.12). Therefore the chain-rule slope `κ_g = Φ̂'(C₂(g))·(dC₂-image/dτ)` inherits the SAME sign for every g — the per-gen slope vector is UNIFORM:
```
sign(κ_{gen1}) = sign(κ_{gen2}) = sign(κ_{gen3}) = (+,+,+) .
```
This is precisely what the S103 witness records: `r_gen = (0.752965, 0.735593, 0.709821)` — monotone-decreasing in C₂, **same-signed**, `crossing_realized=False`.

**Conclusion of §2:** (R-i) ∧ (R-ii) ⇒ ¬(R-iii). Any G-invariant scalar that assigns a per-gen slope is forced through (★), hence monotone-in-C₂, hence uniform-sign. **The crossing handle is not in the Casimir-graded calculus because it is not in the G-invariant-scalar class at all** — and the C₂-grading is not an *assumption* of route (b), it is a *theorem* (★) about what G-invariance permits.

This is the first and decisive blow against Reading A: the σ-model's "fullness" buys nothing, because the bottleneck is (R-i)+(R-ii), which any per-gen-slope-producing G-invariant functional must satisfy, σ-model or not.

---

## 3. The off-Casimir threat, taken at full strength — and why it breaks

Reading A's strongest move is to deny (R-ii): "a full SU(3) σ-model need not produce a *scalar* per-gen slope by Schur — it can carry an internal field with its own profile, and the non-monotonicity lives in the field configuration, not in a C₂-labelled number." I take this seriously. There are exactly three ways to instantiate it, and each one breaks on a *different* pinned wall. This triple-redundancy is the heart of why the wall is permanent rather than merely unprobed.

### 3a. Route via a NON-scalar (non-Schur) operator on the fiber — breaks W2 (homogeneity)

If `Φ` is to distinguish generations *within* a sign-changing pattern, it must act NON-trivially on the multiplicity index `ℂ^{m(p,q)}` (that is the only place the generation label lives — Step 1). But any operator acting non-trivially on `ℂ^{m(p,q)}` does NOT commute with `D_K` (which is scalar there) UNLESS it is itself `R_X`-covariant — and `ℂ^{m(p,q)}` is `R_X`-inert, so a non-scalar action on it is NOT `SU(3)_R`-invariant. It breaks (R-i). This is the §VII.BL (W2) wall verbatim: a generation-distinguishing deformation MUST break left-invariance on the multiplicity space. **A "full-SU(3) σ-model" that is genuinely G-invariant cannot touch the multiplicity index; the moment it touches it to get a sign flip, it is no longer left-invariant — it is `ε_LX`, the external non-LI connection.**

This is not a Casimir-grading artifact. It is the homogeneity of the substrate. The σ-model does not escape it; it runs straight into it.

### 3b. Route via DROPPING order-one / enlarging the algebra — breaks the 7-axiom substrate (Axiom 5) AND adds an unobserved gauge group

The technically honest way to make inner fluctuations generation-dependent is to ENLARGE the algebra so that the off-diagonal (generation-mixing) commutators survive — i.e. drop the order-one condition (Axiom 5). This is exactly the route §VII.BL clause (f) names ("the enlarged-algebra route that WOULD make fluctuations generation-dependent generically violates order-one and adds an unobserved `SU(3)_gen` gauge factor"). The S31 order-one assessment makes it quantitative and DECISIVE:

```
Without Axiom 5:  A stays  M₂(ℍ) ⊕ M₄(ℂ)
                  Inn(A_PS) = SU(2)_L × SU(2)_R × SU(4)_C   (Pati–Salam)
With Axiom 5:     M₂(ℍ) ⊕ M₄(ℂ)  --Axiom 5-->  ℂ ⊕ ℍ ⊕ M₃(ℂ)   (the Standard Model algebra)
```

So the σ-model-on-an-enlarged-algebra is not a free lunch on the *same* substrate — it is a DIFFERENT substrate, whose gauge content is Pati–Salam-or-larger and whose extra `SU(3)_gen` family gauge bosons are UNOBSERVED. The framework's entire derivation of the SM gauge group (one of its STAGE-3-PERMANENT results, KO-dim=6, SM quantum numbers, the unique 7-axiom algebra `A_F = ℂ⊕ℍ⊕M₃(ℂ)` under M₃ χ-kill, S88 W4a-17) is the statement that Axiom 5 holds. You cannot keep the SM gauge group AND have generation-dependent inner fluctuations: the very condition (Axiom 5) that gives you the SM is the condition that makes inner fluctuations multiplicity-scalar. **Reading A's σ-model trades the SHAPE wall for an observed-physics contradiction (extra gauge bosons / wrong gauge group).** That is not "the wall was specific to the sub-calculus"; that is "the only off-sub-calculus route is outside the substrate's admissible class."

### 3c. Route via a grading-PRESERVING generation-dependent factor — collapses back to §2 (monotone-in-C₂)

The framework already TRIED the most charitable in-class version of Reading A. The S102 W4 construction is
```
Y_g^full = Scale_gap · h(C₂(g)) · g_eps(C₂(g))           [session-102-plan-w4.md]
```
where `g_eps` is the generation-dependent factor that "preserves the grading (the §VII.BL corollary)." Read the structure: `g_eps` is a function `g_eps(C₂(g))` — it is STILL a function of the Casimir. By (★) of §2 it is therefore STILL monotone-in-C₂-class (or, if non-monotone as a function, it is non-monotone *off the substrate*, supplied by hand as external `ε_LX` data). A grading-preserving factor cannot generate a sign flip the grading does not already contain, because "grading-preserving" means "factors through C₂," which is exactly the uniform-sign class. The S101-D5-MD-GAPEQ verdict confirms this empirically: `shape_dev=0.3972`, `shape-FAIL`, `right-species-wrong-grading` — the substrate delivers the right *kind* of object but the WRONG (monotone) grading, and cannot be pushed non-monotone from inside.

**Net of §3:** the three exhaustive instantiations of "off-Casimir" each fail on a distinct, independently-pinned wall — homogeneity (3a), order-one/observed-gauge-group (3b), grading-preservation-collapses-to-monotone (3c). There is no fourth door. The σ-model is not a new room; it is the same three walls seen from a different angle.

---

## 4. Independent corroboration from the Paasch / mass-quantization sector (my domain)

The mass-quantization program supplies an INDEPENDENT line of evidence that the substrate's flavor sector carries no intrinsic non-monotone sign DOF — arrived at from spectral-ratio phenomenology rather than NCG axioms, so it is a genuine cross-check, not a restatement.

1. **`φ_paasch` is INTER-SECTOR ONLY.** The one robust spectral-ratio structure the substrate carries is `φ_paasch = m_{(3,0)}/m_{(0,0)} = 1.531584` — a ratio BETWEEN Peter-Weyl sectors. It is a property of the *ordering* `(0,0) < … < (3,0)`, i.e. a MONOTONE inter-sector ladder. There are **no intra-sector crossings** anywhere in the program (`paasch-reference.md` Proven Structural Facts). A non-monotone sign-changing per-gen DOF is exactly an intra-/cross-sector *crossing*; the spectral-ratio phenomenology that the substrate DOES support is the monotone-ladder kind, never the crossing kind. This is the same uniform-monotone signature as §2, seen in the mass spectrum rather than the slope.

2. **`PHI-BDG-47 FAIL` + the BCS theorem.** When you dress the bare spectrum (the only way to get generation-resolved physical masses), `exp(−1/M)`-type BCS dressing CATEGORICALLY destroys the φ-structure and compresses every inter-sector ratio monotonically toward 1 (`max R_dressed=1.465`, proven algebraically S27). The dressing channel is monotone-compressing — it cannot *manufacture* a sign reversal it did not have; it only shrinks ratios. So neither the bare spectrum (monotone ladder) nor the dressing channel (monotone compression) supplies a crossing.

3. **`LOG-SIGNED-40` is single-signed.** The one open Paasch gate that is literally a per-sector SIGNED sum returns `S_signed(0.19) = +787.773` at its single computed point — a single, definite sign. The natural per-sector signed functional the substrate offers is sign-DEFINITE, consistent with the uniform `(+,+,+)` of §VII.BV. (Caveat, honestly flagged: this is one τ-point; a full τ-sweep is the open computation. But a sign *flip across generations at fixed τ* is a different object from a sign change *in τ*, and §2 forbids the former regardless of what the τ-sweep of the latter shows.)

The mass-quantization sector therefore independently sees the substrate as carrying a MONOTONE inter-sector ladder and a monotone (compressing) dressing channel — exactly the structure that §2 derives from homogeneity. Two different methodologies, same wall.

---

## 5. Why this is a PERMANENT WALL, and the right verdict-form

The §VII.BL corollary already named the escape: the hierarchy must be carried by an **external non-LI fibre connection `ε_LX`, breaking W2, non-gauge-removable, `P_nLI = ‖ε_LX‖² > 0`** (anchored at `ε² = 4.0000e-04`, the shared baryogenesis-frontier `S97-BARYOGEN-EXT-SOURCE`). That is a statement that the MAGNITUDE/EXISTENCE of the between-generation hierarchy is external. The SHAPE branch is the *sign-pattern* refinement of the same statement, and it inherits the same external-ness for the same reason: a sign flip across generations is, by §2, exactly a multiplicity-index-distinguishing operation, which is exactly what `ε_LX` (and only `ε_LX`) can do.

So the structurally correct verdict is a **pinned permanent-wall theorem completing the homogeneity-obstruction genus**:

> **NO-NON-MONOTONE-SIGN-DOF (SHAPE branch).** On the homogeneous Jensen-deformed spectral triple `(A_K, H_K, D_K(τ))` with `A_K = ℂ⊕ℍ⊕M₃(ℂ)` and KO-dim 6, there is NO G-invariant construction — Casimir-graded inner/twisted/opposite-action one-form, full-SU(3) σ-model, OR grading-preserving generation-dependent factor — that supplies a non-monotone sign-changing per-generation scalar slope across the quark sectors `{(1,0),(1,1),(3,0)}`. The crossing (sign-changing) SHAPE handle is irreducibly EXTERNAL: it can only be carried by a non-left-invariant fibre connection `ε_LX` (breaking W2 while preserving W1), the same external channel that carries the hierarchy MAGNITUDE. Equivalently: the substrate's flavor SHAPE sector is empty in exactly the sense the M_KK magnitude obstruction was empty before its just-closed external derivation — both the magnitude AND the shape of the fermion mass texture are external to the homogeneous substrate's G-invariant calculus.

This is FALSIFIER-RELEVANT in the framework's own terms: it converts "we haven't found the σ-model handle yet" (an open liability, Q18b/Q44 SHAPE) into a structural statement with a definite content — the fermion SHAPE hierarchy is external by the same homogeneity-obstruction that makes the magnitude external, and any future model that claims a substrate-internal SHAPE handle is REFUTED unless it exhibits a G-invariant `Φ` evading §2 (which §3 shows requires either breaking left-invariance, dropping Axiom 5 with unobserved gauge bosons, or collapsing to monotone-in-C₂). It completes the genus: SCALE branch dissolves via M_KK-derivation; SHAPE branch is a permanent wall; both terminate at the *same* external `ε_LX`.

It is a NON-PROMOTION-BY-HELD-NUMBER instance (per `cross-pillar-bridge-anatomy.md`) — the theorem STRUCTURE is permanent, the sign-pattern NUMBER is HELD against substrate-natural extraction (`crossing_realized=False`), and it is NOT sideways-re-pinned to a methodology-floor image. Differentia: **sign-lock** (the uniform `(+,+,+)` is structurally enforced; the held quantity is a sign-pattern, not a magnitude or a slot-collision).

---

## 6. The single strongest threat to my own pole (honest engagement)

I must not strawman Reading A. The genuinely dangerous version is NOT "drop Axiom 5" (that is dispatched in 3b) and NOT "grading-preserving factor" (dispatched in 3c). It is this:

> **A G-invariant σ-model whose target carries its own non-trivial topology/holonomy, such that the per-generation slope is a HOLONOMY (a `π₁`/Wilson-loop-valued object), not a Schur-scalar — and a holonomy can change sign without violating Schur, because it is not an operator on a single simple block but a global phase around the SU(3) configuration.**

This is dangerous because §2's Step 2 (Schur ⇒ factors through C₂) assumes `Φ` is an *operator on each simple block*. A holonomy/Wilson-loop functional is not obviously of that form. And the framework itself has a registered object of exactly this flavor: §VII (the B2 (1,1)-fiber) carries a **C²-coset Wilson-loop holonomy `f_WZ` that is a frame-invariant NON-Schur-scalar** under an isotropy-breaking deformation. So a non-Schur G-invariant *does* exist on the substrate. Reading A's best case is: build `κ_g` from `f_WZ`-type holonomy, not from a C₂-scalar, and the sign flip might be free.

**Why I still hold Reading B against this — and where it must be settled.** The decisive datum is S110 `CF1-YUK-C2COSET: FAIL`, which is precisely a test of an off-U(2) C²-coset (holonomy-carrying) deformation. Its witness numbers are the answer to exactly this threat:
- `dY12_d0 = −8.73e-16`, `abs_dY12_d0 = 8.73e-16` — the off-diagonal (generation-mixing, sign-carrying) Yukawa derivative at the symmetric point is ZERO to machine precision;
- `schur_ok = True`, `schur_offdiag0 = 1.75e-17`, `distinct0 = 1` — the Schur (degenerate-multiplet) point is PROTECTED; the deformation does not lift it at first order;
- `crit_lift = False` (the lift criterion FAILS) even though `rank_increased = True`, `crit_rank = True` — i.e. the holonomy deformation CAN increase the matrix rank at finite `δ` (`first_rank2_delta = 0.005`) but does so SYMMETRICALLY (`crit_cubic=True`, cubic onset), with NO first-order sign-changing handle at the homogeneous point.

In words: the one realized non-Schur holonomy probe the framework built (the last internal geometric corridor, CV-8 Arm-G) produces a rank increase but NOT a sign-changing first-order slope — it lifts the degeneracy *evenly*, not with a crossing. The holonomy is real, but its action on the generation slope is sign-DEFINITE / even, not non-monotone. That is why CV-8 Arm-G is recorded DEAD. So even the non-Schur threat, when actually instantiated, lands back on the uniform-sign side.

The clean way to make this airtight (and the natural R2/R3 deliverable if connes-ncg-theorist presses the holonomy route): a **selection-rule / triality argument** that the holonomy functional's center-character forces its generation-slope to be sign-definite. The §VII.BV-adjacent CKM-triality texture already shows the substrate's generation channels are center-character-graded (`t = (p−q) mod 3`: gen3 has `t=1`, gen1/gen2 have `t=0`; cross-`t` matrix elements vanish EXACTLY). A holonomy `κ_g` built G-invariantly must respect this Z₃-grading, and a sign-changing pattern across `{t=0, t=0, t=1}` is a specific Z₃-forbidden texture — I expect (R2 target) the same `t(|f|²)=0` argument that forces the CKM zeros forces the holonomy slope to be sign-uniform. If that closes, the non-Schur escape is sealed and the wall is unconditional.

---

## 7. Honest current lean + single most decisive consideration

**(i) Current lean — Reading B, with high confidence at the single-τ-slice level and moderate-to-high confidence on the σ-model extension.**
- The single-τ-slice wall is ALREADY STAGE-3-PERMANENT (§VII.BV); nothing in this workshop weakens it.
- The off-Casimir extension is, I argue, ALSO walled, by the triple-redundant §3 argument (homogeneity / order-one-gauge / grading-collapse) plus the realized-probe datum that the last internal holonomy corridor (CV-8 Arm-G, S110) FAILED to produce a sign-changing handle.
- The one place I do NOT yet have a machine-checked closure is the *general* non-Schur holonomy functional (§6) — I have the realized instance (FAIL) and a strong selection-rule expectation, but not a no-go theorem covering ALL `π₁`-valued G-invariant functionals. That gap is the legitimate residue of the tension, and it is the R2/R3 work.

**(ii) The single most decisive consideration:** *Homogeneity, not Casimir-grading, is the obstruction.* The generation index lives ONLY on the `R_X`-inert multiplicity factor `ℂ^{m(p,q)}` (Step 1). Any functional that distinguishes generations enough to flip a sign must act non-trivially THERE — and any G-invariant (left-invariant-respecting) functional CANNOT act non-trivially there. "Casimir-graded vs full-SU(3) σ-model" is a distinction WITHIN the G-invariant class, and the wall is a property OF the G-invariant class (homogeneity ⇒ multiplicity-scalar). So the σ-model's extra richness is orthogonal to the obstruction: it cannot reach the one index (`m(p,q)`) where the sign flip would have to live without ceasing to be G-invariant — at which point it is `ε_LX`, external by definition. The wall is permanent for the same reason the M_KK magnitude obstruction was: the substrate is homogeneous, and a generation-resolved sign-texture is precisely what homogeneity forbids it to carry internally.
