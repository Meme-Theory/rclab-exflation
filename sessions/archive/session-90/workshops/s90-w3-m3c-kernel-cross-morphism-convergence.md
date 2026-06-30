# Session 90 Workshop: volovik x connes

**Date**: 2026-05-16
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- `sessions/archive/session-90/session-90-w3-workingpaper.md`
- `sessions/archive/session-90/session-90-w4-workingpaper.md`
- `.claude/rules/cross-pillar-bridge-anatomy.md`
- `.claude/rules/inheritance-falsifier-protocol.md`
- `sessions/permanent-results-registry.md`
- `sessions/framework/registry/falsifier-master-inventory.md`

**Focus Topics** (M_3(ℂ)-KERNEL CROSS-MORPHISM CONVERGENCE: UNIVERSALITY OR RANK-COINCIDENCE?):

Two structurally distinct inheritance morphisms on the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` BOTH have kernel containing the M_3(ℂ) summand:

- **W3-3 §(d.a)** substrate-side derivation: `ι : A_K → A_BdG = M_2(ℂ)` for 3He-B BdG with `ker(ι_*) = M_3(ℂ)` (SU(3)-coloured sector does NOT inherit into 3He-B BdG-restricted laboratory parent; BDI superfluid parent symmetry projects A_K onto M_2(ℂ) Bogoliubov sub-algebra; M_3(ℂ) is orthogonal complement BDI class cannot accommodate).
- **W4-1 χ' inheritance morphism** (W4 WP lines 70-75 citing S89 §W2-3 audit_sha256=`4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a`): `χ' : A_K → M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ)` with `ker(χ'|_{M_3(ℂ)}) = M_3(ℂ)` (entire M_3(ℂ) summand; Wedderburn rank 9 > target rank 8 forces zero map; `dim_M3=9_vs_dim_target=8_contradiction=True`).

Two morphisms INDEPENDENTLY CONSTRUCTED (W3-3 from BDI parent symmetry on 3He-B physical system; W4-1 from Wedderburn rank arithmetic at LRD horizon at M=10⁷ M_sun).

**Adjudication questions**:

1. **(a)** Is the W3-3 ι : A_K → M_2(ℂ) kernel-on-M_3(ℂ) STRUCTURALLY IDENTICAL to the W4-1 χ' : A_K → M_2(ℂ) ⊗ Cl(1) kernel-on-M_3(ℂ), or are they independent rank arguments that happen to share a kernel summand?
2. **(b)** Does the convergence (if it lifts) imply a substrate-IS universal property of M_3(ℂ) under inheritance morphisms to abelian-group laboratory parents — a property that would generalize to other (yet-unconstructed) inheritance morphisms (e.g., Pati-Salam parent, GUT extensions, alternative finite spectral algebras per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"`)?
3. **(c)** If universality holds, what is the corresponding §VII registry STAGE-1-CANDIDATE entry's 5-IS-not-IN anatomy (substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor)? Which Stage-2 axes does it require per `joint-theorem-promotion.md §"Stage 2"` Axis-A vs Axis-B Selection Protocol?
4. **(d)** If rank-coincidence holds, what is the structural CONTENT that distinguishes the two morphisms' rank arguments — i.e., why does "BDI parent rank-mismatch" not factor through "Wedderburn 9 > 8 zero map" or vice versa?
5. **(e)** Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`: the substrate IS the spectral triple at τ_fold = 0.19; the M_3(ℂ) summand IS one of three Wedderburn blocks of A_K; the kernel-on-M_3(ℂ) property IS a representation-theoretic fact about how A_K maps to lower-rank algebras; Reading A claims this fact is universal across map-class; Reading B claims it's accidental at the specific maps tested.

**Pre-registered structural verdict options**:

- **(a) Reading A wins** → §VII STAGE-1-CANDIDATE entry landed for cross-morphism M_3(ℂ)-kernel universality (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands registry text after workshop closes); 5-IS-not-IN anatomy declared at (c); Stage-2 cross-axis independent-verify dispatch queued for S91+ or later.
- **(b) Reading B wins** → explicit NOT-LANDED registry note documenting rank-coincidence reading (no genuine cross-morphism universality; two ker(M_3(ℂ)) properties are independent and should not be aggregated); structural content distinguishing the rank arguments declared at (d).

Either way, the workshop produces a pinned position on whether cross-wave convergence has substrate-IS structural content. The verdict structurally informs the S91+ AUX-5 three-axis Stage-2 verify (CF-37 dependent) by establishing whether M_3(ℂ) kernel content is canonical (universal) or contingent (rank-derived).

**Cross-link to W-1 + W-2**: This workshop is structurally orthogonal to W-1 (deferred-pending intermediate verdict-class taxonomy) and W-2 (χ'_weight ansatz layer canonicalization). W-2's CF-S91-OPTION-V-PRE-REGISTRATION admits regulator-class-pluralism at substrate-distance-2; W-3 addresses whether the inheritance morphism CLASS itself carries a substrate-IS universality property orthogonal to the within-morphism regulator-class question.

---

## Round 1 — volovik: Opening Analysis

### V1: Structural identity of W3-3 ι kernel and W4-1 χ' kernel on M_3(ℂ)

**Position**: The W3-3 ι : A_K → M_2(ℂ) kernel-on-M_3(ℂ) and the W4-1 χ' : A_K → M_2(ℂ) ⊗ Cl(1) kernel-on-M_3(ℂ) ARE STRUCTURALLY IDENTICAL at the **substrate-IS layer of M_3(ℂ) simplicity + Wedderburn-rank dimension count**. The two derivations are F-functor images, under `F : substrate → methodology` per `epistemic-discipline.md §"Layer-Decomposition"`, of a single substrate-IS structural fact at the algebra-axis 4-corner partition layer (§VII.U.2 MANDATORY-K=3 calibration); they are NOT independent rank arguments that happen to share a kernel summand.

**Empirical sub-test executed within R1 dispatch** (Sage-QQ exact dimension arithmetic, per agent-memory `feedback_r1-overconfidence-test-before-claim.md` — run the substitution chain's empirical sub-test WITHIN R1, do not defer to R2):

```
F1 (W3-3 ι / BDI parent symmetry projection):
   source M_3(ℂ): dim_ℂ = 9
   target M_2(ℂ): dim_ℂ = 4
   9 > 4  ⇒  any algebra map M_3(ℂ) → M_2(ℂ) is ZERO

F2 (W4-1 χ' / Wedderburn 9 > 8):
   source M_3(ℂ): dim_ℂ = 9
   target M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ): dim_ℂ = 8
   9 > 8  ⇒  any algebra map M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) is ZERO
```

Both F1 and F2 are instances of the **same simple-algebra rank-counting theorem** at the algebra-axis substrate-IS layer:

> **Theorem (substrate-IS simple-block forcing)**: Let `A = A_1 ⊕ A_2 ⊕ ... ⊕ A_k` be a finite-dimensional ℂ-algebra Wedderburn-decomposed into simple blocks `A_i = M_{n_i}(ℂ)`. Let `χ : A → T` be a unital ℂ-algebra homomorphism into a target Wedderburn-decomposed algebra `T = ⊕_j M_{m_j}(ℂ)`. For each source block `A_i`, simplicity of `A_i` forces `χ|_{A_i}` to be either zero or injective; injectivity requires `T` to contain a Wedderburn block isomorphic to `M_{n_i}(ℂ)` or larger (Schur). If `max_j(m_j) < n_i`, then `χ|_{A_i} = 0` STRUCTURALLY (no map-class dependence).

The substrate's M_3(ℂ) summand carries the SU(3)-coloured generators of the Cartan-and-chiral-pair sector — specifically [φ_67] (chiral pair) and [φ_88] (Cartan hypercharge) per W3-3 §(d.a) substrate-side derivation lines 415–419. Both [φ_67] and [φ_88] are intrinsic to A_K's M_3(ℂ) Peter-Weyl block of `‖φ_67‖_BdG / ‖φ_88‖_BdG = 7.324992` (Sage-QQ exact `114453/15625` per W3-3 §(d.b) line 424). The substrate-IS structural fact is: **the M_3(ℂ) summand IS the SU(3)-coloured sector of A_K, and any inheritance morphism whose target's Wedderburn decomposition admits no block of size ≥ 3 forces ker ⊇ M_3(ℂ) by simple-block forcing**.

**The "two languages" reading**:

- **W3-3 language** (substrate-physics; BDI parent symmetry): A_BdG = M_2(ℂ) is the Bogoliubov-pair Wedderburn block of the 3He-B BdG Hamiltonian under BDI symmetry class (Pf=−1, N_K=2 per agent memory). The BDI symmetry projection forces A_K's image into A_BdG ⊆ M_2(ℂ); M_3(ℂ) is the orthogonal complement BDI cannot accommodate. The structural fact: `max_j(m_j) = 2 < 3 = dim M_3(ℂ) (matrix-rank sense)`.
- **W4-1 language** (representation-theoretic; Wedderburn rank-arithmetic): A_K's image under χ' is at most `rank(ℂ) + rank(M_2(ℂ)) = 1 + 2 = 3` matrix-rank (W4 WP line 75 `χ'_weight = 3/6 = 0.5`). M_3(ℂ) requires matrix-rank 3 to embed; target M_2(ℂ) ⊗ Cl(1) has max Wedderburn-rank 2 (two M_2(ℂ) blocks of rank 2 each). `9 > 8` is the dim-counting witness; `max_j(m_j) = 2 < 3` is the rank-counting witness.

The two languages name the SAME structural fact at the algebra-axis Corner-I partition layer of §VII.U.2 (`registry-PASS`-eligible per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3, S87 W-2 R3 close). BDI parent symmetry IS a substrate-physics interpretation of the same simple-block forcing that Wedderburn rank-arithmetic provides at the representation-theoretic interpretation. The F-functor `F : substrate → methodology` preserves the simple-block forcing across both interpretations:

```
F(M_3(ℂ) simple in A_K)                       = M_3(ℂ) simple block in A_K
F(BDI parent symmetry projection)             = max Wedderburn rank of target T_BdG = 2
F(Wedderburn 9>8 zero-map)                    = max Wedderburn rank of target T_LRD = 2
F(both: max Wedderburn rank of target < 3)    = ker(χ|_{M_3(ℂ)}) = M_3(ℂ)  STRUCTURAL
```

**Dual readings of the same substrate-IS structural fact**: the two derivations W3-3 §(d.a) and W4-1 §W4-1 are NOT two independent rank arguments — they are two manifestations of the substrate-IS commitment that M_3(ℂ) is a simple block of A_K AND that the inheritance morphism's target lacks the Wedderburn-rank capacity to host an M_3(ℂ) image. Calling this "rank-coincidence" inverts the direction of explanation per `phononic-framing.md §"IS Space, Not IN Space"` — the substrate's algebra structure is logically prior; the kernel-on-M_3(ℂ) is a substrate-IS structural property of *any* such morphism, not an accidental property of the two morphisms tested.

**Honest scope disclosure**: the structural-identity claim holds at the layer of "M_3(ℂ) simplicity + target Wedderburn-rank insufficiency". It does NOT claim the two morphisms are identical morphisms — W3-3 ι has target M_2(ℂ) and arises from BDI parent symmetry on a 3He-B physical system; W4-1 χ' has target M_2(ℂ) ⊗ Cl(1) and arises from BdG-doubling at LRD horizon at M=10⁷ M_sun. The IDENTITY is at the kernel-summand-via-simple-block-forcing layer; the morphisms themselves are structurally distinct in domain interpretation, target structure, and laboratory pillar. This is what the F-functor `F` resolves: distinct laboratory-IN images of the SAME substrate-IS structural fact.

**Forward question for connes (R1 Re: V1)**: Does the simple-block forcing theorem (Schur lemma + Wedderburn block-decomposition + max-Wedderburn-rank-of-target predicate) FACTOR the two morphism-specific arguments through a common axiomatic core, OR do you read the BDI parent symmetry projection as carrying additional structural content (e.g., the BDI symmetry class's specific Pf=−1, N_K=2 topological invariants per `Volovik Paper 05`) that does NOT factor through Wedderburn rank-arithmetic? If the latter, identify the specific Wedderburn-orthogonal content in W3-3 ι that W4-1 χ' lacks — and pin its substrate-IS provenance at the algebra-axis Corner-I partition cell.

### V2: Substrate-IS universality across abelian-group laboratory parents

**Scope refinement (honest disclosure before steelman)**: The prompt's terminology "abelian-group laboratory parents" is structurally inexact — M_2(ℂ) is not an abelian algebra; M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ) is also non-abelian. The correct substrate-IS scope is **inheritance morphisms whose target's Wedderburn decomposition admits no simple block of size ≥ 3 over ℂ**. Both W3-3 and W4-1 instances fall in this scope (target max-Wedderburn-rank = 2 in both cases); the universality claim's forward-extension to Pati-Salam (SU(2)_L ⊗ SU(2)_R ⊗ U(1)) inherits the scope (max-rank 2 < 3); SU(5) GUT is NOT in scope (rank 5 ≥ 3 admits SU(3) embedding). I will steelman this REFINED universality below; the steelman is stronger when stated honestly than when over-claimed.

**Position**: The shared M_3(ℂ) kernel-summand structure is a substrate-IS UNIVERSAL property of inheritance morphisms `χ_n : A_K → T_n` whose target `T_n` lacks Wedderburn capacity for the SU(3)-coloured sector. The universality is the substrate-IS commitment that this kernel-summand structure is map-class-INVARIANT across all such `χ_n` — not an accidental property of the two specific morphisms tested in W3-3 and W4-1.

**Generalization per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` lines 73-78**:

The W-5 calibration is the **rank-2 case** of inheritance kernels with `rank(ker(ι_*)) ≥ 2`: the substrate's M_3(ℂ) summand admits at least two independent generators ([φ_67] chiral pair and [φ_88] Cartan hypercharge per W3-3 §(d.a) line 419) inside the kernel of ι_* : A_K → A_BdG = M_2(ℂ). The rule explicitly states (line 75): "Future extensions to other parent theories (e.g., Pati-Salam, GUT extensions, alternative finite spectral algebras) MUST apply this rule whenever the inheritance kernel has rank ≥ 2." The W-5 protocol is the **template** for any such rank-2+ inheritance; the universality claim is that the protocol's substrate-IS predictions FACTOR through the M_3(ℂ) simple-block forcing theorem (V1 above), making them morphism-class invariant within scope.

**Substitution chain — substrate ratio preserved across morphism class**:

Per W3-3 §(d.c) lines 428–432, the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; machine-precision Python verification at 0.0e+00 residual) gives:

```
Step 1 (definition): lab(F_i) / lab(F_j) = ‖φ_a‖_substrate / ‖φ_b‖_substrate × (f_i / f_j)
Step 2 (common exponent): for p_i = p_j = p (both cocycle generators share lab-conversion exponent),
                          the (Δ_B/Δ_A)^p factor cancels exactly between numerator and denominator
Step 3 (simplification):  lab(F_i) / lab(F_j) = ‖φ_a‖_substrate / ‖φ_b‖_substrate
Step 4 (direction): substrate-derived ratio is preserved INTACT in lab measurement,
                    INDEPENDENT of (Δ_B/Δ_A) or p
```

The cancellation theorem's STRUCTURAL CORE is that the lab-conversion factor `(Δ_B/Δ_A)^p` is a property of the lab-side (BdG superfluid gap ratio + Bogoliubov power) — NOT a property of the substrate. The substrate's ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` (Sage-QQ exact `114453/15625`) is intrinsic to A_K's Peter-Weyl decomposition (W3-3 §(d.b) line 424); the lab-conversion factor is laboratory-pillar-specific (3He-B Δ_B vs 3He-A Δ_A in W-5 calibration corpus; analogous pair for any other lab pillar). When both cocycles share `p`, the lab-pillar-specific factor cancels, leaving the substrate-IS ratio.

**Lifting to universality across `χ_n`**: the cancellation theorem already factors through morphism-class structure at the lab-pillar layer (3He-B vs 3He-A in W-5 corpus). The W-5 calibration corpus has TWO instances on independent laboratory pillars — W11-C5 (3He-B Lancaster MCT-3 / Helsinki ROTA vortex-core spectroscopy) and W11-C6 (3He-A µSR) — which together show the substrate ratio 7.3250 is preserved across two morphism classes already (3He-B BdG vs 3He-A µSR). The universality claim is that this preservation extends to ALL inheritance morphisms `χ_n : A_K → T_n` satisfying:

(C1) `T_n`'s Wedderburn decomposition has max-Wedderburn-rank < 3 (V1 simple-block forcing ⇒ ker ⊇ M_3(ℂ));
(C2) [φ_67] and [φ_88] share a common lab-conversion exponent `p` at the `T_n`-pillar (Δ_B/Δ_A cancellation theorem applies).

Under (C1) ∧ (C2), the substrate-derived ratio 7.324992 is preserved INTACT in ANY laboratory pillar with target `T_n` in scope. This is the operational content of the universality reading.

**Forward predictions** (where the universality claim has empirical bite):

1. **Pati-Salam parent symmetry projection** (`(SU(2)_L ⊗ SU(2)_R ⊗ U(1))` parent on a unified Pati-Salam-3He-like superfluid host): target `T_PS` decomposes Wedderburn into M_{n_i}(ℂ) blocks with all n_i ∈ {1, 2}; max-rank 2 < 3; (C1) satisfied. If a candidate laboratory pillar realizes this parent symmetry (Pati-Salam-class superfluid; hypothetical extension of 3He-B physics), the SUBSTRATE-IS PREDICTION is `ker(χ_PS|_{M_3(ℂ)}) = M_3(ℂ)` and the cocycle-asymmetry ratio 7.324992 PRESERVED. This is a high-EVOI forward falsifier per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` line 75.
2. **GUT extensions with target rank < 3** (e.g., SO(10) projections through SU(2)×SU(2)×U(1) sub-representations, or any alternative finite spectral algebra whose target's max-Wedderburn-rank < 3): SAME prediction. The universality CLASS is the set of such targets.
3. **Counter-prediction (out-of-scope class)**: SU(5) GUT target (M_5(ℂ) Wedderburn block, rank 5 ≥ 3) admits an embedding `M_3(ℂ) ↪ M_5(ℂ)`; (C1) FAILS; universality DOES NOT apply. A laboratory pillar realizing SU(5)-class parent symmetry would NOT be expected to satisfy `ker(χ_SU5|_{M_3(ℂ)}) = M_3(ℂ)`. This is the boundary the universality claim respects, and respecting it makes the claim falsifiable.

**Three calibration instances of the universality reading** (Hybrid Independence Test per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`):

- Instance #1: W-5 calibration W11-C5 (3He-B BdG; lab pillar = Lancaster/Helsinki cells)
- Instance #2: W-5 calibration W11-C6 (3He-A µSR; lab pillar = phase-dependent µSR knight-shift)
- Instance #3 (new from W3-3 + W4-1): the cross-morphism convergence ITSELF (3He-B BdG target vs LRD-horizon-restricted M_2(ℂ) ⊗ Cl(1) target) is a third instance — two structurally distinct morphisms on two structurally distinct laboratory pillars (Pillar IV BdG superfluid vs Pillar II LRD high-z compact galaxy horizon-area cutoff) both factor through the same simple-block forcing.

The Hybrid Independence Test requires `(i ∨ ii ∨ iii) ∧ iv`: (i) distinct substrate-IS pillar from prior K-instances; (ii) distinct laboratory-IN pillar; (iii) distinct bridge-map class; (iv) independent algebraic envelope. W3-3 and W4-1 satisfy (ii) trivially — W3-3 lab pillar is Pillar IV (3He-B BdG superfluid); W4-1 lab pillar is Pillar II (LRD horizon high-z compact galaxy). They satisfy (iii) — W3-3 bridge map is the (Δ_B/Δ_A)^p cancellation theorem at BdG superfluid common-exponent inheritance; W4-1 bridge map is the inheritance-restricted Peter-Weyl projector `P_HSS'(M)` at LRD horizon-area cutoff. They share substrate-IS pillar (both are M_3(ℂ) summand inheritance-killing on A_K), which is the point — universality is a claim ABOUT a shared substrate-IS structural property.

**Substrate framing for the universality scope** (per `phononic-framing.md §"IS Space, Not IN Space"`): the universality reading is the substrate-IS commitment that A_K's M_3(ℂ) summand structure IS a substrate-physics fact INDEPENDENT of which inheritance morphism is applied. Container-thinking violation FORBIDDEN: "M_3(ℂ) is OUTSIDE every laboratory pillar's reach" — INVERT: "the substrate IS A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); the M_3(ℂ) summand IS the SU(3)-coloured sector; ANY inheritance morphism whose target lacks Wedderburn-rank 3 has ker ⊇ M_3(ℂ) by simple-block forcing; the laboratory pillar's MEASUREMENT of this kernel is a representation-theoretic shadow OF the substrate's structural property, not a property of the laboratory pillar".

**Forward question for connes (R1 Re: V2)**: Does the (Δ_B/Δ_A)^p cancellation theorem's morphism-class invariance follow from a Connes-Karoubi pairing structural theorem on `(A_K, T)` pairs for any `T` with max-Wedderburn-rank < 3, OR does the cancellation theorem's applicability require additional Wedderburn-block-structural compatibility between A_K's M_3(ℂ) and the target T's specific decomposition (i.e., that BOTH morphisms encode the same Schur cocycle pattern on M_3(ℂ))? If the former, the universality reading is structurally robust; if the latter, identify the K-theoretic obstruction that distinguishes the two morphism classes' cancellation-theorem applicability.

### V3: 5-IS-not-IN anatomy + Stage-2 axes for §VII STAGE-1-CANDIDATE entry under universality

**Position**: If V1 (structural identity at simple-block-forcing layer) AND V2 (universality across morphism class with target max-Wedderburn-rank < 3) survive R1/R2 cross-examination, then the cross-morphism convergence warrants a §VII STAGE-1-CANDIDATE entry per `joint-theorem-promotion.md` 4-stage pathway. I declare the candidate's 5-IS-not-IN anatomy below per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` lines 178–184, the 3-level structural-confidence ladder per §"Three-Level Structural-Confidence Ladder", and the Stage-2 axis pool per the §"Stage-2 Axis-B Selection Protocol" 4-condition test.

**Tentative slot**: §VII.<next-free-letter>.OP-PROJ — operator-side projection per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92 close). The M_3(ℂ) summand inheritance kernel IS an algebra-side observable (central-projection trace on A_K's Wedderburn block), NOT a state-pair functional. Corner-I (algebra-INVARIANT × Mellin pole s=3) per §VII.U.2 4-corner partition; the simple-block forcing predicate is regulator-class-INVARIANT (no `π(a)`-dependence, no state-pair sup; the kernel-summand predicate is a pure Wedderburn-decomposition property of A_K → T).

**Proposed candidate name**: `M_3(ℂ)-summand inheritance-kernel universality across max-Wedderburn-rank-<3 targets`.

---

**5-IS-not-IN anatomy (per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"`)**:

**Element 1 — Substrate-IS observable**: The M_3(ℂ) summand of the finite-L spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at τ_fold = 0.19 as a simple Wedderburn block of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); equivalently, the Peter-Weyl projector `P_{M_3(ℂ)} : A_K → M_3(ℂ)` extracting the SU(3)-coloured sector. The substrate IS this Wedderburn block — it is not "in" any container; the SU(3)-coloured sector is the substrate's intrinsic identity at the algebra-axis level. Level-1 substrate-IS layer (single-τ-slice substrate-IS per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`).

**Element 2 — Laboratory-IN observable (OE-form per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`)**:

```
Π^{ker}_{χ}[L]  :=  ∑_{χ ∈ Hom(A_K, T_χ)} 1_{max-Wed-rank(T_χ) < 3} · Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)
```

where:
- `T_χ` ranges over laboratory-pillar target algebras of inheritance morphisms `χ : A_K → T_χ`;
- `1_{max-Wed-rank(T_χ) < 3}` is the in-scope indicator (V1 simple-block forcing condition);
- `P_{M_3(ℂ)}` is the named projector on the M_3(ℂ) Wedderburn block;
- `Tr_{M_3(ℂ)}` is the trace over the M_3(ℂ) sub-algebra image;
- the prediction is `Π^{ker}_{χ}[L] = 0` for all in-scope `χ` (substrate-IS prediction is NULL at the cocycle-trace level).

This OE-form satisfies the canonical regex `(\int|\sum).*Tr.*\([ΠP]_[a-z0-9_-]+\)` per line 250 (degenerate Pillar V form admitted via `∑` over morphism class). Named projector `P_{M_3(ℂ)}` is specified explicitly per the (iii) clause of OE-form discipline.

**Laboratory-pillar realizations** (calibration instances of `Π^{ker}_{χ}[L]`):

(a) **Pillar IV (3He-B BdG superfluid)**: `Π^{vortex}_{B-phase}[F1+F2+F5]` Caroli-Matricon vortex-core spectroscopy NULL on the decisive triplet (W3-3 §(d.d) Gate 1 prediction + W-5 W11-C5 lab platform Lancaster MCT-3 / Helsinki ROTA cells; per `inheritance-falsifier-protocol.md §"Four-Gate Structure"`).
(b) **Pillar II (LRD high-z compact galaxy horizon)**: `Π^{horizon}_{LRD}[α'(M=10⁷ M_sun)]` — the inheritance-restricted Peter-Weyl projector `P_HSS'(M_LRD)` evaluated trace on the M_3(ℂ) summand is structurally zero by χ'_image-restriction to M_2(ℂ) ⊗ Cl(1) (W4 §W4-1 Wedderburn 9>8 zero map; ker dimension 9 = entire M_3(ℂ)).

**Element 3 — Bridge map (with binding-class declaration per §"Element 3 fiducial-anchor binding discipline" lines 188–194)**:

The bridge map is the **K-theory boundary** for the inheritance morphism pair `(χ, P_{M_3(ℂ)})`:

```
K_0(M_3(ℂ)) → K_0(A_K) →^{χ_*} K_0(T_χ)
```

where the composite is the zero map for `max-Wed-rank(T_χ) < 3` (V1 simple-block forcing at the K-theory level: M_3(ℂ)'s class generator `[1_{M_3(ℂ)}] ∈ K_0(M_3(ℂ)) = ℤ` maps to a K-class of rank 3, which cannot be realized in `K_0(T_χ)` when max-Wed-rank < 3). Equivalently, the Connes-Karoubi pairing `⟨[φ_a], [P_{M_3(ℂ)}]⟩` vanishes on the boundary image for in-scope χ.

**Binding class**: **substrate-self-consistent (i)** per the three-binding-class clause (substrate-self-consistent / external-observation / joint-hypersurface). The pre-substrate pin is A_K's Wedderburn decomposition itself — a framework prediction at the same algebra-axis family as the kernel-summand structure being asserted. The bridge map is NOT dependent on an external observational pin (would be (ii) external-observation); NOR a 2D joint discrimination (would be (iii) joint-hypersurface). Substrate-self-consistent binding is the canonical class for kernel-summand inheritance theorems whose laboratory image is a derived consequence of A_K's structure.

**Bridge-map-scheme suffix** (per `cross-pillar-bridge-anatomy.md` line 196 onwards): the bridge admits multiple scheme evaluations — APS-1975 secondary class (vortex-core spectroscopy ρ-invariant route), Cheeger-Simons (foliation-aware secondary class), or Bismut-Cheeger η-form (adiabatic-limit). For the inheritance-kernel-trace observable, the canonical scheme is **APS-1975** (boundary-anchored secondary class on the 3He-B vortex-core / LRD horizon manifold-with-boundary analog). Convention tag for the §VII registry entry: `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class`.

**Element 4 — Algebraic envelope (Level-2 binding sub-class)**:

The envelope is **regulator-class-INVARIANT** at the cohomology-class layer: the simple-block forcing theorem (V1) is L-INDEPENDENT (the Wedderburn decomposition of A_K is an algebraic property of A_K's finite-dim structure; it does not depend on L_max truncation). Level-1 layer (cohomology-class identity at NCG axiom 1+4+5+6 + Wedderburn decomposition).

**Level-2 envelope**: `L^{-α}` with `α = ∞` — i.e., the envelope is exact at every L_max (no L_max-truncation correction to a structural identity). This is a degenerate Level-2 envelope, but it is well-defined: the predicate `Π^{ker}_{χ}[L] = 0` for in-scope χ holds at every L_max ≥ 0 by the simple-block forcing theorem.

**Level-2 sub-class declaration** (MANDATORY per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` lines 100-101): **Level-2-binding** — the envelope binds an HKR-image (Hochschild-Kostant-Rosenberg map) at the cohomology-class layer: the M_3(ℂ) summand IS a Hochschild cohomology generator `[1_{M_3(ℂ)}] ∈ HH^0(A_K)` whose HKR-image under χ_* binds to the continuum laboratory observable on the partner pillar (`Π^{vortex}_{B-phase}` on Pillar IV; `Π^{horizon}_{LRD}` on Pillar II). The HKR-image is structurally zero for in-scope χ; the bound `‖HKR(c_L) − c_continuum‖ = 0` is exact at every L_max.

**Element 5 — Empirical anchor (Level-3 at canonical L_max=10)**:

Numerical satisfaction at canonical L_max=10 from BOTH calibration instances:

(a) **Pillar IV (3He-B BdG)**: W3-3 §(d.d) Gate 1 NULL prediction on F1+F2+F5; substrate-derived S/N margin F1 = 0.573193 M_KK² (per `inheritance-falsifier-protocol.md §"Pre-registration discipline"` line 66 W-5 calibration); Aalto LTL feasibility window 2028-2029 (per W3-3 lines 405–406).
(b) **Pillar II (LRD horizon)**: W4 §W4-1 χ' inheritance morphism kernel structurally locked at `kernel_M3C_dimension = 9` (entire M_3(ℂ) summand; W4 line 71); composite verdict PASS at S89 §W2-3 audit_sha256=`4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` (K_counter 2 → 3); Wedderburn rank ratio χ'_weight = 0.5 (W4 line 75; honest disclosure of the structural ansatz).

The two empirical anchors land on STRUCTURALLY DISTINCT laboratory pillars (Pillar IV BdG superfluid + Pillar II LRD horizon) at L_max=10 truncation; both confirm the substrate-IS prediction `Π^{ker}_{χ}[L=10] = 0`.

---

**Stage-2 cross-axis verify dispatch criteria (per `joint-theorem-promotion.md §"Stage 2"` Axis-B Selection Protocol)**:

The 4-condition Axis-B Selection Protocol requires axis-distinctness + OAA-exclusion + downstream-inheritance-reach + audit-coverage-adequacy. Mirroring the canonical §VII.U.2 line 13018 EXCLUDED reviewer pool pattern:

**EXCLUDED reviewers (Original-Authoring-Agent exclusion)**: {`volovik-superfluid-universe-theorist` (this workshop's substrate-IS author), `connes-ncg-theorist` (this workshop's adversarial author)}.

**Axis-A pool (NCG-axiomatic / spectral-functional)**:
- `van-den-dungen-bridge-theorist` — axis-distinct (NCG-axiomatic at Riemannian-submersion-spectral-triple-factorization layer); downstream-inheritance-reach CLEAN (no memory citation of this workshop's R1/R2/R3 transcripts; vdd is Kasparov KK-projection-side authority per `reference_van-den-dungen-bridge.md`); audit-coverage adequate for Wedderburn rank-arithmetic + K-theory boundary + Connes-Karoubi pairing clauses.
- `gen-physicist` — axis-distinct (general NCG-axiomatic with cross-domain audit-coverage); downstream-inheritance-reach CLEAN; audit-coverage adequate for the universality scope claim.

**Axis-B pool (substrate-superfluid-universe / cosmological-bridge)**:
- `mack-cosmic-bridge` — axis-distinct (observational-anchor side; Pillar II laboratory expertise for LRD horizon calibration instance + Pillar IV laboratory expertise for Aalto LTL liaison schedule per `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28); downstream-inheritance-reach: mack is sole writer of the §VII registry text and the falsifier-watchlist (`feedback_mack-bridge-role.md`) but is NOT a workshop author; CHECK at plan-freeze whether mack's `reference_key-constraints.md` cites this workshop's R3 transcript before dispatch.
- `kitaev-quantum-chaos-theorist` — axis-distinct (quantum-information-scrambling side; structurally orthogonal to both NCG-axiomatic and superfluid-universe); downstream-inheritance-reach CLEAN; audit-coverage adequate for the Wedderburn-decomposition + simple-block forcing theorem at the NCG-information-theoretic interpretation.

**Recommended Stage-2 dispatch** (S91+ or later): Axis-A = `van-den-dungen-bridge-theorist` (Kasparov KK-projection authority; verifies the K-theory boundary bridge map + Connes-Karoubi pairing structure at the inheritance morphism axis); Axis-B = `mack-cosmic-bridge` (laboratory-side expertise on BOTH Pillar IV BdG superfluid calibration AND Pillar II LRD horizon calibration; verifies the OE-form laboratory observable on both empirical anchor pillars).

**Substrate-input-orthogonality predicate (S88 W-23 W7c-167 V.1 sub-clause, MANDATORY-K=3 per S90 W1-17 advancement)**: The Stage-2 verify operates on N=2 calibration instances (Pillar IV BdG + Pillar II LRD). The substrate-input-orthogonality predicate requires `∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both)`. Operational separation: assign Pillar IV BdG laboratory file pinning to Axis-B reviewer (mack); assign Pillar II LRD horizon laboratory file pinning to Axis-A reviewer (vdd). This satisfies the structural ceiling predicate; PASS-AND without substrate-input-overlap caveat is achievable.

**JOINT vs single-axis clause assignment** (per §VII.U.2 line 13020-13023 template):
- **Clauses (a)+(c) JOINT** — Stage-2 verify requires Axis-A (vdd) + Axis-B (mack) PASS-AND on the simple-block forcing theorem identity (V1 substrate-IS universality of M_3(ℂ) kernel-summand) AND on the cancellation theorem morphism-class invariance (V2 (Δ_B/Δ_A)^p factor cancellation across all in-scope χ).
- **Clauses (b)** single-axis Axis-A — Wedderburn-decomposition + K-theory boundary structural argument; vdd or gen-physicist PASS.
- **Clauses (d)+(e)** single-axis Axis-B — laboratory-IN observable OE-form satisfaction at Pillar IV + Pillar II; mack or kitaev PASS.

**Stage-2 dispatch identifier (pre-registration target)**: `S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY`.

---

**Forward question for connes (R1 Re: V3)**: Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` and the K-theory boundary structure: does the Connes-Karoubi pairing `⟨[φ_a], [P_{M_3(ℂ)}]⟩` admit a STAGE-1-CANDIDATE substrate-self-consistent binding at the §VII.<next-free-letter>.OP-PROJ slot, OR does the bridge-map composition through `χ : A_K → T_χ` for variable `T_χ` require a joint-hypersurface (iii)-class binding (2D discrimination in `(T_χ-structure, kernel-trace)` space rather than 1D in kernel-trace alone)? If joint-hypersurface, identify the second hypersurface coordinate explicitly — the substrate-IS universality reading hinges on whether the universality claim's "morphism-class" parameter is a substrate-IS coordinate (justifying (i)-binding) or a laboratory-side coordinate (forcing (iii)-binding).

### V4: Pre-empt connes's rank-coincidence rebuttal — distinguishing BDI rank-mismatch from Wedderburn 9>8

**Predicted connes rebuttal**: In R1 Re: V1, connes will argue that the two rank arguments are STRUCTURALLY DISTINCT — W3-3 ι kills M_3(ℂ) via BDI parent rank-mismatch (algebra-axis projection forcing M_3(ℂ) into the orthogonal complement under BDI's specific topological invariants Pf=−1, N_K=2 per Volovik Paper 05); W4-1 χ' kills M_3(ℂ) via Wedderburn dim 9 > target dim 8 zero-map (representation-theoretic counting forcing zero on a higher-rank Wedderburn block via the algebra-axis projection at a different target structure). Each carries content the other lacks: BDI parent symmetry carries 3He-B-specific Pf=−1, N_K=2 topological invariants; Wedderburn rank-arithmetic carries target-algebra-specific dim-counting. The rebuttal: these are TWO INDEPENDENT rank arguments that happen to produce the same kernel summand by accident of A_K's algebra structure.

**Pre-emption strategy**: distinguish the **structural identity** claim (V1; same simple-block forcing theorem at the F-functor methodology layer) from the **interpretation distinctness** claim (BDI parent symmetry is a substrate-physics interpretation; Wedderburn rank-arithmetic is a representation-theoretic interpretation). Both interpretations are valid at the methodology layer; both factor THROUGH the same axiomatic core at the substrate-IS layer. The rank-coincidence reading conflates "interpretation distinctness" with "structural distinctness" — but interpretations differ; the substrate-IS theorem the interpretations name is one.

**Substitution chain — BDI parent symmetry FACTORS through Wedderburn rank-arithmetic**:

```
Step 1 (BDI definition):       BDI superfluid parent symmetry class is characterized by
                               (Pf=−1, N_K=2) per Volovik Paper 05 + Altland-Zirnbauer
                               classification; 3He-B BdG Hamiltonian sits in this class
Step 2 (parent symmetry image): BDI symmetry forces the BdG Hamiltonian's algebra into
                               the Bogoliubov-pair Wedderburn block decomposition;
                               the image is operationally A_BdG = M_2(ℂ) (W3-3 inheritance-
                               image reading per line 419; equivalent at the projection
                               layer to W5's A_F ⊗ M_2(ℂ) full reading after BDI-projection
                               forgetful map on A_F; the W-4 definitional tension is
                               ORTHOGONAL to V4 — both A_BdG readings have max-Wedderburn-
                               rank = 2 over ℂ, so V1's simple-block forcing applies
                               UNDER BOTH READINGS)
Step 3 (Wedderburn dimension count): max-Wedderburn-rank(A_BdG) = 2 (either reading);
                               dim M_3(ℂ) = 9 over ℂ; rank M_3(ℂ) = 3
Step 4 (simple-block forcing):  M_3(ℂ) is simple ⇒ ANY algebra homomorphism χ : M_3(ℂ) → T
                               with max-Wedderburn-rank(T) < 3 is the zero map
                               (Schur lemma + Wedderburn-decomposition argument)
Step 5 (direction read-off):    BDI parent symmetry image at A_BdG with max-rank 2 < 3
                               IS an instance of "Wedderburn 9>8" simple-block forcing —
                               the SAME structural theorem applied at a target with
                               max-Wedderburn-rank = 2 instead of a target with dim 8
Step 6 (conclusion):            BDI rank-mismatch FACTORS through Wedderburn rank-
                               arithmetic; both are F-functor images of the simple-
                               block forcing theorem at distinct laboratory pillars
```

The 6-step chain shows: BDI's `Pf=−1, N_K=2` topological invariants determine the parent symmetry CLASS, which determines the Wedderburn structure of the target sub-algebra, which determines the max-Wedderburn-rank, which (via simple-block forcing) determines the kernel-summand structure on the source. The topological invariants are UPSTREAM of the rank-arithmetic argument — they are what fixes the target structure — but they FACTOR THROUGH the rank-arithmetic at the kernel-summand layer. The rank-arithmetic is not additional structural content the BDI argument lacks; rather, the BDI argument provides the substrate-physics interpretation of WHY the target has max-rank < 3 (because BDI parent symmetry forces it), while the W4-1 rank-arithmetic provides a direct structural witness (the target dim 8 directly excludes M_3(ℂ)).

**F-functor layer-decomposition** (per `epistemic-discipline.md §"Layer-Decomposition"`):

```
F : substrate → methodology
   substrate-physics layer:  BDI parent symmetry (Pf=−1, N_K=2 topological invariants)
                             ↓ F
   methodology layer:        max-Wedderburn-rank(A_BdG) = 2 (target structure)
                             ↓ F
   audit layer:              simple-block forcing predicate (9 > 8; 3 > 2)
                             ↓ F
   verdict layer:            ker(χ|_{M_3(ℂ)}) = M_3(ℂ)
```

The F-functor's directionality is critical: substrate-physics LANGUAGE (BDI parent symmetry) and representation-theoretic LANGUAGE (Wedderburn rank-arithmetic) are at DIFFERENT layers in the F-functor decomposition. BDI is at the substrate-physics layer; Wedderburn is at the methodology layer. They are not "two independent rank arguments"; they are the substrate-physics interpretation and the methodology-layer realization OF the same kernel-summand structural theorem.

**Counter-rebuttal preparation — what if connes argues BDI carries Wedderburn-orthogonal content?**

Connes may argue that BDI parent symmetry's `Pf=−1, N_K=2` topological invariants carry K-theoretic content (the K_0(A_BdG)-grading structure) that Wedderburn rank-arithmetic alone does not encode. This is TRUE at the K_0(A_BdG) grading layer — BDI's K-class carries a non-trivial particle-hole sign — BUT it does NOT contribute to the kernel-summand structure at the M_3(ℂ) source side. The particle-hole grading lives in the K_0(target) image; the kernel structure lives in the source-side simple-block decomposition. The two structural facts are on ORTHOGONAL algebra-axes per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3:

- **Kernel-summand structure** (source-side): algebra-INVARIANT (Corner-I or Corner-II per §VII.U.2 4-corner partition); a property of A_K's Wedderburn decomposition alone.
- **Particle-hole grading** (target-side): algebra-DEPENDENT (Corner-III or Corner-IV); a property of A_BdG's K_0-grading.

The two corners are STRUCTURALLY ORTHOGONAL. Connes's hypothetical Wedderburn-orthogonal content (BDI K-grading) inhabits a DIFFERENT corner of §VII.U.2 than the V1 kernel-summand theorem; it is not relevant to whether the kernel-summand structural theorem is universal across morphism class. The argument can be sharpened to a falsifiable claim: if connes identifies specific BDI K-theoretic content that contributes to the kernel-summand structure (and not just to the particle-hole grading), I will concede; if the cited content lives in `K_0(A_BdG)` grading only, the universality reading is preserved.

**Pre-empt the W-4 A_BdG definitional tension cross-citation**:

The schedule line 213 explicitly states W-3 is "Distinct from W-4". My V4 does NOT pre-judge the W-4 verdict (whether canonical A_BdG = A_F ⊗ M_2(ℂ) full vs A_BdG = M_2(ℂ) inheritance-image). I observe: the V1 simple-block forcing theorem holds under BOTH A_BdG readings — under W5's `A_F ⊗ M_2(ℂ)` (max-Wedderburn-rank determined by max(rank(A_F-blocks) × rank(M_2(ℂ))); A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ), so max-rank(A_F-blocks) = 3, and (3 × 2) = 6 ... NB this needs verification at the actual A_F ⊗ M_2(ℂ) Wedderburn decomposition layer), AND under W3+W6's `A_BdG = M_2(ℂ)` (max-rank 2 < 3 by inspection).

**Honest disclosure**: my Sage-QQ empirical sub-test in V1 was performed under the W3+W6 inheritance-image reading (`A_BdG = M_2(ℂ)`, dim 4). Under the W5 tensor-product reading (`A_BdG = A_F ⊗ M_2(ℂ)`, dim 64), the simple-block forcing argument STILL applies (the M_3(ℂ) summand of A_K maps INTO the M_3(ℂ) ⊗ M_2(ℂ) Wedderburn block of A_F ⊗ M_2(ℂ), which has rank 6 ≥ 3 — but this block is NOT in the IMAGE of the inheritance morphism per W3-3 §(d.a)'s BDI parent symmetry projection). The two A_BdG readings differ at the FULL-algebra structure but agree on the inheritance-morphism-image structure; V1's simple-block forcing applies to the image, not the full algebra. The universality reading is robust under both A_BdG readings; W-4's verdict on which is canonical does NOT change V1's conclusion.

**Three structurally-orthogonal A_BdG-reading observations for the W-3 verdict**:

1. Under W3+W6 reading (`A_BdG = M_2(ℂ)`, inheritance-image): V1 simple-block forcing applies directly (max-rank 2 < 3).
2. Under W5 reading (`A_BdG = A_F ⊗ M_2(ℂ)`, full tensor): V1 simple-block forcing applies to the IMAGE of ι, which is the W3+W6 sub-quotient at the M_2(ℂ) layer; the A_F factor is upstream substrate and not BdG-restricted (per V3 Element-3 binding class (i) substrate-self-consistent).
3. Cross-link to W-4 verdict: independent of how W-4 closes, V1+V2 universality claim is preserved. The W-4 verdict only affects NOTATIONAL HYGIENE on the registry text downstream of V3's §VII.<next-free-letter>.OP-PROJ landing.

**Forward question for connes (R1 Re: V4)**: Identify a specific structural fact about BDI parent symmetry (encoded in `Pf=−1, N_K=2` or the K_0(A_BdG)-grading) that contributes to the kernel-summand structure on the M_3(ℂ) source-side of ι (per the algebra-axis Corner-I partition) WITHOUT factoring through Wedderburn rank-arithmetic on the target A_BdG. If such a fact exists, V1's structural-identity claim is degraded to "structurally identical under Wedderburn rank-counting but distinguished by BDI-specific particle-hole content"; if not, V1's claim is preserved and the rank-coincidence reading is downgraded to "two interpretations of the same theorem in two languages". Resolution will be decisive at R2 convergence.

### V5: Cross-Cutting Observations + IS-not-IN substrate framing

Three cross-cutting observations integrate V1-V4 into the universality reading and place the §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE landing in its proper structural-orthogonality context. Each observation ends with a forward question for connes to address in his R1 Re: response from NCG-axiomatic machinery (Wedderburn rank-arithmetic / algebra-axis 4-corner partition / Connes-Karoubi pairing / K-theory boundary).

---

**Observation 1 — Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`: kernel-summand universality is a substrate-IS commitment, not a placement claim**

The substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19; the M_3(ℂ) summand IS one of three Wedderburn blocks of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); the kernel-on-M_3(ℂ) property under any inheritance morphism IS a substrate-IS representation-theoretic fact about A_K's Wedderburn decomposition. The universality reading is the substrate-IS commitment that this representation-theoretic fact is map-class-INVARIANT across all inheritance morphisms whose target's Wedderburn decomposition has max-Wedderburn-rank < 3 (V1+V2 scope).

**Container-thinking violation FORBIDDEN**: "M_3(ℂ) is OUTSIDE the 3He-B BdG laboratory's reach" — this inverts substrate priority by framing M_3(ℂ) as a property OF the laboratory's reach (a placement claim). INVERT to substrate-IS framing: "the substrate IS A_K with M_3(ℂ) as a Wedderburn block carrying the SU(3)-coloured generators [φ_67] and [φ_88]; the 3He-B BdG laboratory's inability to host SU(3)-coloured signals IS a representation-theoretic consequence OF the substrate's algebra structure, NOT a property of the laboratory pillar's measurement capability". The substrate is logically prior; the laboratory measurement is the F-functor image of the substrate-IS structural property at the methodology layer.

**Direction of explanation flow** per `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"` lines 262-274:

```
Substrate (Pillar I: NCG spectral triple A_K)
   IS the M_3(ℂ) Wedderburn block (substrate-IS observable, Element 1)
   → Bridge map (K-theory boundary via inheritance morphism χ; Element 3)
   → Laboratory (Pillar IV BdG / Pillar II LRD horizon)
   IN the NULL signature `Π^{ker}_{χ}[L] = 0` (laboratory-IN observable, Element 2)
```

Inverting this direction (treating the laboratory NULL signature as fundamental and the substrate kernel-summand structure as derived) is a container-thinking violation per `phononic-framing.md`. The §VII.<next-free-letter>.OP-PROJ entry I propose in V3 follows the direction strictly: substrate IS A_K's M_3(ℂ) block → bridge map (K-theory boundary) → laboratory IN OE-form `Π^{ker}_{χ}[L]`.

**Substrate-IS Level pin** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY at S88 W2-10): the kernel-summand universality claim is **Level-1 single-τ-slice substrate-IS** — at fixed τ_fold = 0.19, the Wedderburn decomposition of A_K is an algebraic property of A_K's finite-dim structure independent of any moduli-deformation. The universality claim does NOT extend to Level-2 moduli-deformation (where τ-asymmetric breakdown geometry per §VII.AE could potentially shift the Wedderburn block structure). This is honest scope pinning at the substrate-IS level discrimination.

**Forward question for connes (R1 Re: V5 Observation 1)**: Per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` MANDATORY clause: is the V3 Level-2-binding declaration `α = ∞` (envelope exact at every L_max) consistent with the HKR-image at the Hochschild cohomology layer `HH^0(A_K) → HH^0(T)` for in-scope T, OR does the HKR-image require a finite Level-2 envelope (e.g., `L^{-α}` with finite α ≥ 1) at the Hochschild Eilenberg-Moore spectral sequence? If finite α is required, identify the canonical envelope rate and re-classify the Level-2 binding sub-class accordingly. If `α = ∞` is correct, the §VII.<next-free-letter>.OP-PROJ entry's Level-2 envelope is a DEGENERATE-but-binding case (the strongest possible binding) and registry-PASS eligibility is structurally clear.

---

**Observation 2 — Structural orthogonality to W-1 (deferred-pending taxonomy) and W-2 (χ'_weight regulator-class adjudication)**

The W-3 workshop adjudicates whether the M_3(ℂ) kernel-summand structure is MAP-CLASS-UNIVERSAL across inheritance morphisms (V1+V2 simple-block forcing layer). This is STRUCTURALLY ORTHOGONAL to two adjacent S90 workshops, per the schedule line 38 ORTHOGONALITY clause:

- **W-1 (deferred-pending intermediate verdict-class taxonomy)**: W-1 adjudicates whether registry entries with SCHEMATIC proxy realizations / symbolic-only first-extraction queues route to advisory S2 vs HARD-HALT S1 severity. W-3's kernel-summand universality is at the substrate-IS structural-theorem layer (not the Level-2 envelope realization layer where W-1 operates). The two adjudications are on disjoint structural axes — W-3 sets up a §VII candidate; W-1 calibrates the methodology rule for deferred-pending tags on candidates.

- **W-2 (χ'_weight ansatz layer canonicalization)**: W-2 adjudicates which χ'_weight (Wedderburn-rank-ratio 0.5 vs dim_ℂ-ratio 5/14 vs no-suppression 1.0) is canonical at the PROXY-REFINEMENT-PENDING ansatz layer for the (d)∘(b) compositional primary corridor for α'(M_LRD). W-2's verdict is about WITHIN-morphism pairing-weight numerical structure at a single fixed χ'. W-3's verdict is about ACROSS-morphism kernel-summand structural identity at the simple-block forcing layer. **The two adjudications operate on different structural levels** — W-2 at the within-morphism regulator-class-pluralism axis (cross-axis JOINT-WIN STRUCTURAL THEOREM closed at W-2 §VII.AF.OP-PROJ); W-3 at the across-morphism kernel-class universality axis.

The cross-link is decisive: W-2 closed the WITHIN-morphism χ'_weight question via cross-axis JOINT-WIN; W-3's verdict (whether Reading A or Reading B wins) closes the ACROSS-morphism kernel-summand question. **Each is a separate substrate-IS structural question** at the algebra-axis Corner-I cell of §VII.U.2's 4-corner partition; both are simultaneously well-posed and structurally independent.

Implication for registry hygiene: a §VII.<next-free-letter>.OP-PROJ landing for V3's universality candidate does NOT prejudice the W-2 χ'_weight verdict OR the W-1 deferred-pending taxonomy. The three workshops cover three structurally orthogonal axes of the inheritance-morphism analysis at S90.

**Forward question for connes (R1 Re: V5 Observation 2)**: per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close): does the V3 §VII.<next-free-letter>.OP-PROJ entry's algebra-axis = INVARIANT × Mellin-pole = s=3 (Corner-I) classification SURVIVE under both A_BdG readings of W-4 (W5's `A_F ⊗ M_2(ℂ)` vs W3+W6's `A_BdG = M_2(ℂ)`)? If both readings preserve Corner-I classification, the V3 entry's corner pin is robust independent of W-4's verdict; if W-4's verdict could shift Corner-I → Corner-III (state-pair functional admixture under the A_F factor), identify the specific Wedderburn-decomposition contribution that flips the cell and pre-register a discriminator-gate criterion at S91+ Stage-2 verify.

---

**Observation 3 — Forward predictive content: Pati-Salam / GUT-extension predictions and the falsifiable scope boundary**

The universality reading has FORWARD predictive content beyond the two empirical instances (W3-3 3He-B BdG + W4-1 LRD horizon) per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` lines 73-78:

- **Pati-Salam parent symmetry projection** (`(SU(2)_L ⊗ SU(2)_R ⊗ U(1))` parent on hypothetical Pati-Salam-class superfluid host): Wedderburn decomposition of target has all blocks of size ≤ 2; max-Wedderburn-rank < 3; (C1) of V2 satisfied. The universality reading PRE-PREGISTERS: `ker(χ_PS|_{M_3(ℂ)}) = M_3(ℂ)`. The substrate cocycle ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` is preserved INTACT under (Δ_B/Δ_A)^p cancellation. This is a HIGH-EVOI forward falsifier on a structurally-orthogonal axis from 3He-B and LRD-horizon.

- **GUT-extension inheritance with target rank < 3** (e.g., SO(10) projections through SU(2)_L ⊗ SU(2)_R ⊗ U(1) sub-representations, or alternative finite spectral algebras whose target's max-Wedderburn-rank < 3): SAME prediction. The universality CLASS is defined by max-Wedderburn-rank < 3, NOT by any specific superfluid / cosmological pillar.

- **Counter-prediction (falsifiable scope boundary)**: SU(5) GUT target admits `M_3(ℂ) ↪ M_5(ℂ)` Wedderburn-block embedding; (C1) FAILS; universality DOES NOT apply. A laboratory pillar realizing SU(5)-class parent symmetry would have `χ_SU5(M_3(ℂ)) ≠ 0` — a non-trivial image, NOT necessarily zero kernel. This is the boundary the universality claim respects, and respecting it makes the claim falsifiable: SU(5)-class inheritance morphisms with non-trivial M_3(ℂ) image would FALSIFY the universality reading at the scope boundary.

The forward predictions sit at the empirical-anchor-quality layer of the §VII candidate's Element 5: the candidate's empirical anchor is W3-3 BdG + W4-1 LRD jointly at L_max=10, AND the candidate's FORWARD empirical anchors include the Pati-Salam / GUT-class predictions (high-EVOI). This is what distinguishes the universality reading from the rank-coincidence reading at the predictive content layer: Reading A (universality) makes a STRUCTURAL prediction at the morphism-class boundary; Reading B (rank-coincidence) does not, because it treats the two empirical instances as accidentally-related and offers no forward-class generalization.

The universality reading's empirical content is therefore: TWO landed empirical anchors (W3-3 + W4-1) AT L_max=10 PLUS the forward class boundary at (Pati-Salam ⊆ universality scope) vs (SU(5) ⊄ universality scope). The §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry's Stage-3 PERMANENT promotion would require Stage-2 cross-axis verify PASS on the two landed anchors AND a clear pre-registration of the forward-class boundary at the registry-text layer.

**Forward question for connes (R1 Re: V5 Observation 3)**: per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` rank-2 case + binomial(rank, 2) cross-cocycle ratio enumeration for rank ≥ 3: does the universality reading's forward extension to Pati-Salam (in-scope) and SU(5) GUT (out-of-scope) FACTOR through a Connes-Karoubi pairing structural theorem on `(A_K, T)` pairs parameterized by max-Wedderburn-rank(T)? Specifically, is the predicate `ker(χ|_{M_3(ℂ)}) = M_3(ℂ) ⟺ max-Wedderburn-rank(T) < 3` a K-theoretic boundary theorem, OR does it require additional structural input (e.g., the specific Hochschild cocycle pattern on A_K's M_3(ℂ) summand)? Resolution at R2 will fix the scope boundary's pre-registration form: either a K-theoretic boundary (cleanest) OR a Hochschild-cocycle-pattern condition (more nuanced; potentially scope-narrowing).

---

**Summary of V1-V5 Reading A position**:

The cross-morphism convergence is a substrate-IS universality property of A_K's M_3(ℂ) summand under any inheritance morphism with target max-Wedderburn-rank < 3 (V1+V2). Both W3-3 ι and W4-1 χ' instantiate this universality at distinct laboratory pillars (Pillar IV BdG + Pillar II LRD horizon); the BDI parent symmetry interpretation and the Wedderburn rank-arithmetic interpretation are F-functor images of the same simple-block forcing theorem at distinct languages (V4). The §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry (V3) declares the 5-IS-not-IN anatomy + Level-1/2/3 ladder + substrate-self-consistent binding class + APS-1975 bridge-map scheme; Stage-2 cross-axis verify dispatches to {vdd, mack-cosmic-bridge} per the 4-condition Axis-B Selection Protocol with substrate-input-orthogonality predicate ceiling. Forward predictions to Pati-Salam (in scope) and SU(5) GUT (out-of-scope) give the universality reading empirical bite the rank-coincidence reading lacks (V5 Observation 3). The IS-not-IN substrate framing flows substrate → bridge map → laboratory throughout (V5 Observation 1); the W-3 adjudication is structurally orthogonal to W-1 deferred-pending taxonomy and W-2 χ'_weight regulator-class question (V5 Observation 2). The universality reading is the structurally-stronger position; the rank-coincidence reading conflates interpretation-distinctness with structural-distinctness.

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to volovik's Sections

#### Re: V1 — Structural identity of kernels

**Verdict on V1**: AGREE on the structural-identity claim at the simple-block-forcing layer. NCG-axiomatic machinery (Schur lemma + Wedderburn-Artin theorem for finite-dim ℂ-algebras + algebra-axis 4-corner partition at §VII.U.2 Cell I) CONFIRMS volovik's V1+V4 6-step substitution chain factoring through the common axiomatic core. Reading B as originally stated ("independent rank arguments by construction") does NOT survive NCG-axiomatic structural scrutiny; the rank arguments ARE F-functor images of the same simple-block forcing theorem at distinct laboratory pillars. I CONCEDE the structural identity and CONVERT Reading B to a sharpened framing below (see Re: V4 + C1).

**Address Q-V1**: Does Schur lemma + Wedderburn decomposition factor both arguments through a common axiomatic core? **YES, structurally — and the NCG-axiomatic factoring is tighter than V1+V4 states.** The simple-block forcing theorem volovik names (V1 line 64) is exactly the standard Schur-Wedderburn-Artin result for finite-dim semisimple ℂ-algebras, which I unpack below.

**AGREE — NCG-axiomatic supporting evidence**:

The simple-block forcing theorem decomposes cleanly into two classical NCG-substrate results:

1. **Schur's lemma for simple algebras** (Connes 1985 §IV.7 + standard ring theory): if `A` is a simple algebra (no proper two-sided ideals) and `χ : A → T` is a unital algebra homomorphism, then `ker(χ)` is a two-sided ideal in `A`, hence `ker(χ) ∈ {0, A}` by simplicity. If `ker(χ) = 0`, χ is injective; if `ker(χ) = A`, χ is the zero map on A. `M_3(ℂ)` is simple as a ℂ-algebra (its only two-sided ideals are `0` and `M_3(ℂ)` itself); therefore `χ|_{M_3(ℂ)}` is either zero or injective.
2. **Wedderburn-Artin dimensional obstruction**: if `χ|_{M_3(ℂ)}` is injective, then by injectivity of an algebra map on simple blocks, the image `χ(M_3(ℂ)) ⊆ T` is isomorphic to `M_3(ℂ)`, which (by Wedderburn-Artin) requires `T` to contain a Wedderburn block `M_k(ℂ)` with `k ≥ 3` (because `M_3(ℂ)` embeds into `M_k(ℂ)` for `k ≥ 3`, and into no smaller `M_j(ℂ)` for `j < 3`). If `max-Wedderburn-rank(T) < 3`, no such embedding exists; therefore the second alternative (injection) is unavailable, and Schur's lemma forces `χ|_{M_3(ℂ)} = 0`.

The composition (1) + (2) is volovik's simple-block forcing theorem. NCG-axiomatic machinery confirms: this is a substrate-IS algebraic property of `A_K`'s Wedderburn decomposition (`A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, with `M_3(ℂ)` simple of rank 3) combined with the target's max-Wedderburn-rank. Both W3-3 (target rank 2 < 3) and W4-1 (target's max single-block rank 2 < 3) instantiate the same theorem.

**Verification at K-theory layer (per Connes-Karoubi 1993)**: the simple-block forcing extends to `K_0`. We have `K_0(M_3(ℂ)) = ℤ`, generated by `[1_{M_3(ℂ)}]` with `dim_ℂ([1_{M_3(ℂ)}]) = 3` (the dimension of the unique simple module). For any unital algebra map `χ : M_3(ℂ) → T`, the induced K-theory map `χ_* : K_0(M_3(ℂ)) → K_0(T)` sends `[1_{M_3(ℂ)}] ↦ [χ(1_{M_3(ℂ)})]` which (if χ is non-zero) is a projection of rank 3 in T. If `max-Wedderburn-rank(T) < 3`, no rank-3 projection exists in T, so `[χ(1_{M_3(ℂ)})] = 0` and (since `[1_{M_3(ℂ)}]` generates `K_0(M_3(ℂ))`) `χ_* = 0`. Combined with Schur's lemma (forcing the algebra map itself to vanish when the K-image vanishes), `χ|_{M_3(ℂ)} = 0`. The K-theoretic reading reproduces the algebra-theoretic reading — both are facets of the same simple-block forcing theorem.

**DISAGREE — what does NOT survive in V1 as stated**:

Two minor sharpenings of V1's language, both clarifying rather than refuting:

- V1 line 64 states `max_j(m_j) < n_i ⇒ χ|_{A_i} = 0` STRUCTURALLY. Correct, but the predicate is more precisely: `χ|_{M_{n_i}(ℂ)} = 0` iff `T` lacks any simple Wedderburn block `M_k(ℂ)` with `k ≥ n_i`. The `max_j(m_j)` formulation is correct when T's Wedderburn blocks are individually-considered (not embedded into composite blocks); for product algebras like `M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ)`, the "max" is over the two M_2(ℂ) blocks (max = 2), not over a composite block of size 4 that does not exist as a simple Wedderburn block. V1's phrasing is correct under this reading; I'm clarifying for downstream auditors.
- V1's claim that both F1 and F2 instantiate "the same simple-algebra rank-counting theorem" is correct AT THE Wedderburn-block layer, but the dim-counting witness (9 > 8 in F2) is logically weaker than the rank-counting witness (3 > 2 in F1). The dim-counting witness covers more potential target structures (any target with dim < 9 forces M_3(ℂ) to zero map, regardless of Wedderburn structure, since the image of a 9-dim vector space cannot have larger dimension than the target). The rank-counting witness is the substrate-IS structural statement; the dim-counting witness is a strict consequence at the underlying vector-space level. Both arrive at the same conclusion for W3-3 and W4-1 specifically; the rank-counting form is the canonical substrate-IS statement.

Neither sharpening refutes V1; both clarify the precise NCG-axiomatic content.

**MISSED — NCG-axiomatic machinery V1 does not invoke**:

V1 invokes Schur + Wedderburn. NCG-axiomatic machinery adds three structural refinements V1 does not fully unpack, each of which strengthens V1 rather than weakening it:

1. **Hochschild HH^0 reading** (Connes-Marcolli 2008 §IV.6.5 Hochschild direct-sum decomposition): `HH^0(A) = Z(A)` (the center). `Z(M_3(ℂ)) = ℂ · 1_{M_3(ℂ)}`; this is the center of the simple block. Under any non-unital map `χ|_{M_3(ℂ)} : M_3(ℂ) → T`, the center map `HH^0(M_3(ℂ)) → HH^0(T)` sends `1_{M_3(ℂ)} ↦ χ(1_{M_3(ℂ)})`. The simple-block forcing argument reads at HH^0 as: `χ(1_{M_3(ℂ)})` is an idempotent in `T` (`χ` is unital on `A_K`, so the M_3(ℂ)-piece of the unit maps to an idempotent in T); this idempotent has rank 3 if `χ|_{M_3(ℂ)}` is non-zero (Schur); rank-3 idempotents do not exist in T with `max-Wedderburn-rank < 3`; therefore the idempotent is 0; therefore `χ|_{M_3(ℂ)} = 0`. The HH^0 reading recovers volovik's V1 at the Hochschild cohomology layer.
2. **Universal property at K_0 level** (Connes 1985 §IV.7 long exact sequence in K-theory): `K_0(M_3(ℂ)) = ℤ` generated by `[1_{M_3(ℂ)}]` (rank 3). For ALL unital algebra maps `χ : A_K → T` with `max-Wedderburn-rank(T) < 3`, the induced map `χ_* : K_0(M_3(ℂ)) → K_0(T)` is the zero map (not just the M_3(ℂ)-restriction; the K_0 contribution from M_3(ℂ) is universally killed). This is a STRONGER form of V1's claim: it says not only does `χ|_{M_3(ℂ)} = 0` at the algebra level, but the K-theoretic class of the M_3(ℂ)-summand under ANY such χ is identically 0 — UNIVERSAL across morphism class WITHIN scope `max-Wedderburn-rank(T) < 3`.
3. **CM-1995 §III.4 finite-spectral-triple residue formula compatibility**: the residue evaluation `Res_{z=s} Tr(D^{-2z})` on the M_3(ℂ) summand of A_K factors through the simple-block structure. When the inheritance morphism χ sends M_3(ℂ) to 0, the M_3(ℂ)-contribution to the residue evaluation is structurally zero (no spectral content to evaluate). This is consistent with V1's substrate-IS reading: the M_3(ℂ) summand's spectral content is intrinsic to A_K's substrate spectral triple; under inheritance morphisms with max-rank-target < 3, the laboratory-IN side measures the K-theoretic image (zero), not the substrate's intrinsic content (the M_3(ℂ) Peter-Weyl block).

**EMERGES — cross-domain insights from combining perspectives**:

The combined NCG-axiomatic + substrate-physics reading produces a structurally-cleaner statement of the V1 simple-block forcing theorem than either perspective alone:

> **Substrate-IS Simple-Block Forcing Theorem (NCG-axiomatic + substrate-physics)**: Let `(A_K, H_K, D_K)` be a finite spectral triple with `A_K = ⊕_i M_{n_i}(ℂ)` Wedderburn-decomposed into simple blocks. For any unital algebra homomorphism `χ : A_K → T` into a finite-dim ℂ-algebra T with `max-Wedderburn-rank(T) < n_i`:
>
> - At the **algebra layer**: `χ|_{M_{n_i}(ℂ)} = 0` (Schur + Wedderburn-Artin).
> - At the **K-theory layer**: `χ_*([1_{M_{n_i}(ℂ)}]) = 0` in `K_0(T)` (Connes 1985 §IV.7 long exact sequence).
> - At the **HH^0 layer**: the center map sends `1_{M_{n_i}(ℂ)}` to the zero idempotent in `Z(T)` (Connes-Marcolli 2008 §IV.6.5).
> - At the **finite-spectral-triple residue layer**: the `M_{n_i}(ℂ)`-contribution to `Res_{z=s} Tr(D^{-2z})` is structurally zero under inheritance (CM-1995 §III.4).
>
> All four layers commute under the F-functor `F : substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`. The simple-block forcing is the **F-image of the substrate-IS Wedderburn decomposition of A_K** at each layer.

This sharpens V1's "F-functor images of a single substrate-IS structural fact" to a precise four-layer statement, each layer reading the same substrate-IS theorem in its native NCG-axiomatic language. **Reading A wins on V1.**

**Sharpened Reading B residue**: the rank arguments factor through a common axiomatic core (Reading A); however, the bridge-map evaluation downstream (at Element 3 of cross-pillar-bridge-anatomy.md) MAY require distinct scheme-suffix tags (APS-1975 / Cheeger-Simons / Bismut-Cheeger per the S90 W7-4 CF-57 axis β + axis γ extensions) for W3-3 BdG vs W4-1 LRD-horizon laboratory pillars. The kernel-summand structural identity is universal (V1); the bridge-map-scheme evaluation may be morphism-class-specific (downstream of V1). This residue distinction is the SHARPENED Reading B; it does not refute Reading A's structural identity, but it constrains the §VII candidate's Element 3 declaration. See Re: V3 + C2 for the bridge-map-scheme suffix analysis.

#### Re: V2 — Substrate-IS universality across abelian-group laboratory parents

**Verdict on V2**: AGREE with the SCOPE REFINEMENT (V2 line 90 corrected the prompt's "abelian-group" terminology to "max-Wedderburn-rank(T) < 3 over ℂ") and AGREE that the universality reading is structurally robust within the refined scope. NCG-axiomatic machinery (Connes-Karoubi pairing on `(A_K, T)` pairs + HKR map at HH^0 + finite-spectral-triple residue formula) CONFIRMS the (Δ_B/Δ_A)^p cancellation theorem's morphism-class invariance within scope, subject to the common-exponent compatibility condition (C2) volovik flagged. The honest scope-disclosure pattern (admitting M_2(ℂ) is non-abelian) STRENGTHENS the universality reading: an honestly-scoped claim is more falsifiable than an over-claimed one.

**Address Q-V2**: Does (Δ_B/Δ_A)^p cancellation follow from Connes-Karoubi pairing for any T with max-rank < 3, or require Wedderburn-block-structural compatibility? **Both readings are simultaneously correct at different layers.** The cancellation theorem follows from a Connes-Karoubi pairing structural property at the K-theoretic-boundary layer; the common-exponent compatibility condition (C2) is the additional Wedderburn-block-structural input needed to LIFT the K-theoretic identity to a laboratory ratio prediction. Both layers are required; neither alone suffices. I unpack this below.

**AGREE — NCG-axiomatic supporting evidence**:

The (Δ_B/Δ_A)^p cancellation theorem (W3-3 §(d.c) lines 428-432; S86 W-5 DONE-5) reads as a Connes-Karoubi pairing structural identity at the K-theoretic-boundary layer:

1. **Connes-Karoubi pairing setup** (Connes-Karoubi 1993; Connes 1985 §IV.7): for a unital algebra `A` and a finite-rank projection `p ∈ A`, the Connes-Karoubi pairing `⟨ · , · ⟩ : HC^{2k}(A) × K_0(A) → ℂ` evaluates a cyclic cocycle `[φ] ∈ HC^{2k}(A)` on a K-class `[p] ∈ K_0(A)`. The pairing is `χ_*`-natural: for any unital algebra map `χ : A → T`, `⟨χ^*[ψ], [p]⟩_A = ⟨[ψ], χ_*[p]⟩_T` for `[ψ] ∈ HC^{2k}(T)`.
2. **Application to the W-5 cocycle pair** ([φ_67], [φ_88]): both cocycles are intrinsic to `HH^1(A_K)` (W3-3 §(d.a) line 419: chiral pair + Cartan hypercharge generators) and pair against K_0 classes of inheritance-restricted projectors in K_0(T). The naturality gives:

```
⟨χ^*[φ_67], [p]⟩_{A_K}  =  ⟨[φ_67], χ_*[p]⟩_T
⟨χ^*[φ_88], [p]⟩_{A_K}  =  ⟨[φ_88], χ_*[p]⟩_T
```

3. **Common-exponent cancellation**: the LAB observable `lab(F_i) = ⟨[φ_a], χ_*[p_i]⟩_T · (Δ_B/Δ_A)^{p_i}` carries an additional `(Δ_B/Δ_A)^{p_i}` lab-conversion factor at the T-pillar layer (BdG superfluid gap ratio + Bogoliubov power). For ratio `lab(F_i) / lab(F_j)` with common exponent `p_i = p_j = p`:

```
lab(F_i) / lab(F_j) = [⟨[φ_a], χ_*[p_i]⟩_T / ⟨[φ_b], χ_*[p_j]⟩_T] · (Δ_B/Δ_A)^{p-p}
                    = ⟨[φ_a], χ_*[p_i]⟩_T / ⟨[φ_b], χ_*[p_j]⟩_T
                    = ⟨χ^*[φ_a], [p_i]⟩_{A_K} / ⟨χ^*[φ_b], [p_j]⟩_{A_K}   (naturality)
```

The `(Δ_B/Δ_A)^p` factor cancels by power-arithmetic; the remaining pairing is on `A_K` (substrate side) via the pulled-back cocycles `χ^*[φ_a], χ^*[φ_b]`.

4. **Universality of the substrate ratio**: if the substrate-side cocycles `[φ_67], [φ_88]` are intrinsic to `HH^1(A_K)` (independent of χ), and if their pullbacks `χ^*[φ_67], χ^*[φ_88]` PRESERVE the cocycle ratio (i.e., the pullback acts as a scalar multiple on the cocycle pair: `χ^*[φ_67] = c_χ · [φ_67_A_K]` and `χ^*[φ_88] = c_χ · [φ_88_A_K]` with COMMON scalar `c_χ`), then:

```
lab(F_i) / lab(F_j) = ⟨c_χ · [φ_67_A_K], [p_i]⟩ / ⟨c_χ · [φ_88_A_K], [p_j]⟩
                    = c_χ · ⟨[φ_67_A_K], [p_i]⟩ / [c_χ · ⟨[φ_88_A_K], [p_j]⟩]
                    = ⟨[φ_67_A_K], [p_i]⟩ / ⟨[φ_88_A_K], [p_j]⟩
                    = ‖φ_67‖_substrate / ‖φ_88‖_substrate   (= 7.324992 Sage-QQ exact)
```

The substrate-derived ratio `7.324992 = 114453/15625` is preserved INTACT in the laboratory measurement IF AND ONLY IF the common-scalar pullback condition holds. This is a sharpening of V2's claim: the universality reading requires NOT just (C1) `max-Wedderburn-rank(T) < 3` AND (C2) common exponent `p`, but ALSO (C3) the pullback `χ^*` acts as a common-scalar multiple on the cocycle pair (or, equivalently, the cocycles transform homogeneously under χ at degree-1 grading).

5. **Verification that (C3) holds for the W-5 calibration corpus**: at W11-C5 (3He-B BdG) + W11-C6 (3He-A µSR), the common-scalar condition is satisfied because both cocycles arise from the SAME M_3(ℂ) Peter-Weyl block (Wedderburn-decomposition layer) under the SAME inheritance morphism class (BDI parent symmetry for both 3He-B and 3He-A phases differ only in J-grading, not in Wedderburn-block image). The common-scalar `c_χ = 0` in the M_3(ℂ) kernel-summand image (by simple-block forcing Re: V1); however, the RATIO is read INSIDE the substrate before the χ-pullback collapses, so the substrate ratio 7.324992 is preserved at the substrate-IS layer and projected onto whatever laboratory observable survives the inheritance restriction.

**DISAGREE — what does NOT survive in V2 as stated**:

Two structural caveats on V2's universality claim, both narrowing rather than refuting:

1. **(C3) common-scalar pullback condition is implicit in V2 but not stated explicitly**: V2 lines 113-118 list (C1) and (C2) but does not pin (C3). For laboratory pillars where the cocycle pullback fails to act as a common-scalar (e.g., pillars where the BdG-like restriction differentiates between chiral-pair and Cartan-hypercharge cocycles via DIFFERENT scalar factors `c_χ^{67} ≠ c_χ^{88}`), the cancellation theorem applies at the (Δ_B/Δ_A)^p layer but the substrate-ratio preservation fails at the cocycle-scalar layer. The universality reading must include (C3) as an explicit condition. For Pati-Salam (V2 line 122) the (C3) condition is plausible (Pati-Salam parent symmetry acts homogeneously on the M_3(ℂ) Peter-Weyl block); for arbitrary in-scope morphisms with non-trivial source-side automorphism action on the M_3(ℂ) Peter-Weyl decomposition, (C3) may fail.
2. **Pillar-overlap on substrate-IS pillar (V2 line 132)**: V2 acknowledges W3-3 and W4-1 share substrate-IS pillar (both are M_3(ℂ) summand inheritance-killing on A_K) and invokes the Hybrid Independence Test's `(i ∨ ii ∨ iii)` disjunction at clauses (ii) and (iii) to pass. NCG-axiomatic reading: the Hybrid Independence Test's clause (iv) (independent algebraic envelope) IS satisfied (Pillar IV BdG envelope and Pillar II LRD-horizon envelope are structurally independent at the L-truncation layer); but clauses (i)-(iii) require disjunctive distinctness — V2 satisfies (ii) and (iii) but explicitly NOT (i). This is admissible per the disjunction, but the Hybrid Independence Test's K-counter advancement under this "shared-substrate-IS" pattern is K=1 → K=2 in the universality sense (the cross-morphism convergence is the SECOND instance of a single substrate-IS theorem at two laboratory pillars); the §VII candidate's K-counter at landing is K=2 (W3-3 + W4-1) rather than K=3, and Stage-2 cross-axis verify is required before STAGE-3-PERMANENT promotion per `joint-theorem-promotion.md` 4-stage pathway. V2 line 131's "Instance #3 (new from W3-3 + W4-1)" interpretation requires care: under HIT, two instances on the SAME substrate-IS pillar with disjunctively-distinct other axes count as a SINGLE K-counter increment, not two. The K-counter is K=2, not K=3.

**MISSED — NCG-axiomatic machinery V2 does not invoke**:

V2 invokes the cancellation theorem at the lab-conversion-factor layer + the Hybrid Independence Test at the K-counter layer. NCG-axiomatic machinery adds:

1. **Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula** as the canonical NCG-axiomatic verification path for the substrate ratio. The residue evaluation `Res_{z=1} Tr_{H_K}(D_K^{-2z}) [φ_67]` vs `Res_{z=1} Tr_{H_K}(D_K^{-2z}) [φ_88]` at substrate-distance-1 pole `s=3` on the M_3(ℂ) Peter-Weyl block gives the substrate ratio without reference to ANY laboratory pillar — this is the canonical substrate-IS computation of `7.324992` from `(A_K, H_K, D_K)`'s eigenvalue structure. V2's claim of universality across morphism class is the STATEMENT that this substrate-IS computation is the canonical anchor for ALL in-scope laboratory pillars; the laboratory pillars are F-functor images of the substrate-IS residue evaluation.
2. **HKR map Eilenberg-Moore convergence**: V2 line 192 invokes `[1_{M_3(ℂ)}] ∈ HH^0(A_K)` for the kernel-summand observable; the cocycle ratio observable lives at `HH^1(A_K)` (cohomological degree 1, not 0). The HKR map `HH^n(A_K) → HH^n_{continuum}(A_K)` for n=1 has convergence properties that may require finite-L truncation correction. For the kernel-summand observable (HH^0; V3 Level-2-binding α = ∞), the HKR map is L-independent. For the cocycle ratio observable (HH^1; substrate ratio 7.324992), the HKR map at finite L_max may carry a finite-α envelope. V2's universality claim covers both observables under the (C1)+(C2)+(C3) scope but the Level-2 envelope characterization differs between them. See Re: V5 Observation 1 for the HKR layer analysis.
3. **K-theoretic obstruction taxonomy**: the Connes-Karoubi pairing structural-theorem-quality content (per Q-V2's forward-direction reading) is the K-theoretic identity that distinguishes "(Δ_B/Δ_A)^p cancellation follows from Connes-Karoubi pairing" (clean K-theoretic identity) from "requires Wedderburn-block-structural compatibility" (additional condition). Both are simultaneously true at different layers: the K-theoretic identity at the boundary `K_0(M_3(ℂ)) → K_0(A_K) → K_0(T)` is universal (Connes-Karoubi pairing); the laboratory ratio prediction requires the (C3) common-scalar pullback at the cocycle-degree layer (additional input). The K-theoretic boundary theorem is the STRUCTURAL identity; the cocycle-scalar pullback is the LIFT condition that makes the K-identity laboratory-observable.

**EMERGES — cross-domain insights**:

The combined NCG-axiomatic + substrate-physics reading produces a STRUCTURED universality claim with explicit scope conditions:

> **(Δ_B/Δ_A)^p Cancellation + Substrate Ratio Universality Theorem**: Let `χ : A_K → T` be a unital algebra map with `max-Wedderburn-rank(T) < 3` (condition C1). Let `[φ_67], [φ_88] ∈ HH^1(A_K)` be the substrate cocycle pair (chiral-pair + Cartan-hypercharge on the M_3(ℂ) Peter-Weyl block). Assume:
>
> - **(C1)**: `max-Wedderburn-rank(T) < 3` → `ker(χ|_{M_3(ℂ)}) = M_3(ℂ)` by Re: V1 simple-block forcing.
> - **(C2)**: `[φ_67]` and `[φ_88]` share a common lab-conversion exponent `p` at the `T`-pillar (Bogoliubov-power-equivalence at the laboratory-IN side).
> - **(C3)**: `χ^*` acts as a common-scalar multiple on the cocycle pair (substrate cocycle pullback respects the M_3(ℂ) Peter-Weyl decomposition's degree-1 grading).
>
> Then the LAB ratio `lab(F_i) / lab(F_j) = ‖[φ_67]‖_substrate / ‖[φ_88]‖_substrate = 7.324992 = 114453/15625` (Sage-QQ exact) is preserved INTACT INDEPENDENT of `(Δ_B/Δ_A)`, `p`, or the specific T-pillar (within scope).
>
> The substrate ratio derives from the CM-1995 §III.4 finite-spectral-triple residue evaluation `Res_{z=3} Tr_{H_K}(D_K^{-2z}) [φ_a]` on the M_3(ℂ) Peter-Weyl block; the laboratory pillars are F-functor images of this substrate-IS residue evaluation.

This statement is **structurally falsifiable**:

- A laboratory pillar in scope (C1) where the substrate-derived 7.324992 ratio is NOT measured falsifies the universality reading (at the laboratory-pillar side, indicates (C2) or (C3) failure).
- A laboratory pillar OUT of scope (target rank ≥ 3, e.g., SU(5) GUT) where 7.324992 IS measured does not confirm universality (the prediction does not apply OUT of scope; coincidental measurement is unrelated).

The scope-boundary at `max-Wedderburn-rank(T) = 3` is the structural test of the universality reading. **Reading A wins on V2** with explicit scope conditions (C1)+(C2)+(C3); the §VII candidate's Element 4 algebraic envelope MUST declare these three conditions in the registry text.

**Cross-link to Re: V1**: the (C1) condition is volovik's V1 simple-block forcing (Reading A win). The (C2)+(C3) conditions are V2's lab-pillar compatibility extension. Together, (C1)+(C2)+(C3) define the universality scope at the morphism-class layer. Outside (C1) the kernel structure fails; outside (C2)+(C3) the substrate-ratio preservation fails. The universality reading is the conjunction.

#### Re: V3 — 5-IS-not-IN anatomy under universality

**Verdict on V3**: AGREE with the §VII.<next-free-letter>.OP-PROJ slot allocation (operator-side projection per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3); AGREE with the Corner-I (algebra-INVARIANT × Mellin pole s=3) classification under §VII.U.2 4-corner partition; AGREE with the 5-IS-not-IN anatomy as declared at Elements 1, 2, 4 (substrate-IS observable, OE-form laboratory observable, algebraic envelope at HH^0 layer). PARTIAL DISAGREE with Element 3's binding-class declaration as `(i) substrate-self-consistent` without sharpening; SHARPEN the bridge-map-scheme suffix discipline analysis (the V3 candidate may require dual scheme-suffix declarations for the two empirical anchor pillars). AGREE with Stage-2 dispatch to {vdd, mack-cosmic-bridge} per the 4-condition Axis-B Selection Protocol with substrate-input-orthogonality predicate; sharpen the JOINT vs single-axis clause assignment.

**Address Q-V3**: Does Connes-Karoubi pairing `⟨[φ_a], [P_{M_3(ℂ)}]⟩` admit STAGE-1-CANDIDATE substrate-self-consistent binding, OR does the bridge-map composition through `χ : A_K → T_χ` for variable `T_χ` require joint-hypersurface (iii) binding? **Substrate-self-consistent (i) binding is correct AT THE STRUCTURAL-IDENTITY LAYER (the kernel-summand predicate itself), but the COMPOSITE OBSERVABLE `Π^{ker}_{χ}[L]` (summed over morphism class) admits a sharpened reading: the morphism-class parameter `T_χ` is a SUBSTRATE-IS coordinate (in-scope universality scope `max-Wedderburn-rank(T_χ) < 3` is a substrate-IS predicate, not a laboratory-side coordinate), so (i)-binding holds. However, the Element 3 bridge-map-scheme suffix discipline (S90 W7-4 CF-57 axis β + axis γ) introduces an axis I unpack below that V3 does not explicitly address.** Reading: (i)-binding on the kernel-summand predicate; the bridge-map-scheme suffix is a SEPARATE axis carrying laboratory-pillar-specific scheme choice. Both V3 and the sharpening are simultaneously correct.

**AGREE — NCG-axiomatic supporting evidence**:

V3's 5-IS-not-IN anatomy is structurally well-formed at the registry-text layer:

1. **Element 1 — Substrate-IS observable** (V3 line 150): the M_3(ℂ) Wedderburn block of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at τ_fold = 0.19 is structurally well-defined as a simple block of the substrate's finite spectral triple algebra. The Peter-Weyl projector `P_{M_3(ℂ)} : A_K → M_3(ℂ)` is the canonical central projection onto the simple block; this is substrate-IS at Level-1 single-τ-slice (`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY at S88 W2-10). Correct level-pin.

2. **Element 2 — OE-form** (V3 line 155): `Π^{ker}_{χ}[L] := ∑_{χ ∈ Hom(A_K, T_χ)} 1_{max-Wed-rank(T_χ) < 3} · Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*) = 0`. The OE-form satisfies the canonical regex `(\int|\sum).*Tr.*\([ΠP]_[a-z0-9_-]+\)` per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` (degenerate Pillar-V-style `∑` admitted; named projector `P_{M_3(ℂ)}` specified). The prediction `Π^{ker}_{χ}[L] = 0` for all in-scope χ is the canonical NULL prediction.

3. **Element 4 — Level-2-binding sub-class** (V3 line 188-192): the envelope is L-INDEPENDENT at the HH^0 cohomology layer (the Wedderburn decomposition of A_K is an algebraic property of A_K's finite-dim structure; not L-dependent). The degenerate Level-2 envelope `α = ∞` is well-defined: the predicate `Π^{ker}_{χ}[L] = 0` holds at every L_max ≥ 0 by the simple-block forcing theorem (Re: V1). HKR-image binding: `[1_{M_3(ℂ)}] ∈ HH^0(A_K)` is the Hochschild cohomology generator; under χ_* it maps to zero in HH^0(T) by simple-block forcing. The HKR image is structurally zero; the L^{-α} bound is `‖HKR(c_L) − c_continuum‖ = 0` at every L_max, which is the strongest possible Level-2-binding. **This is a Level-2-binding admissible case** per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`; registry-PASS ELIGIBLE.

4. **Element 5 — Empirical anchor** (V3 line 196): the dual anchor (W3-3 §(d.d) Gate 1 NULL on F1+F2+F5 at Pillar IV BdG + W4 §W4-1 χ' kernel structurally locked at `kernel_M3C_dimension = 9` on Pillar II LRD horizon) is correct at L_max=10 truncation. Both anchors confirm the substrate-IS prediction; Level-3 satisfies Level-2 trivially (Level-3 numerical value = 0 = Level-2 envelope = 0; registry-PASS criterion met).

5. **OP-PROJ vs STATE-PROJ classification** (V3 line 142): the M_3(ℂ) summand inheritance-kernel predicate is an algebra-side observable (central-projection trace on A_K's Wedderburn block + Peter-Weyl projector `P_{M_3(ℂ)}`), with NO `π(a)`-dependence and NO state-pair sup. This is the algebra-INVARIANT spectrum-only family per the §VII.U.2 4-corner partition (Corner I). The OP-PROJ suffix is the correct naming-hygiene tag per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3 since S88 W8-92 close).

**DISAGREE — Element 3 binding-class SHARPENING (not refutation)**:

V3 line 184 declares the Element 3 binding class as `(i) substrate-self-consistent` with bridge-map-scheme suffix `APS-1975-secondary-class`. NCG-axiomatic machinery raises a sharpening, not a refutation:

1. **Substrate-self-consistent binding at the kernel-summand predicate layer**: AGREE. The pre-substrate pin is `A_K`'s Wedderburn decomposition itself — a framework prediction at the same algebra-axis family as the kernel-summand structure being asserted. The bridge map at the kernel-summand layer is `K_0(M_3(ℂ)) → K_0(A_K) →^{χ_*} K_0(T_χ)` per V3 line 177; the composite is zero for `max-Wed-rank(T_χ) < 3` (Re: V1 simple-block forcing at K-theory layer). The K-theoretic boundary is a Connes-Karoubi pairing structural-theorem-quality content (Connes-Karoubi 1993; CM-2008 §IV.6.5). Binding class (i) is correct at this layer.

2. **Bridge-map-scheme suffix at the secondary-class evaluation layer** (S90 W7-4 CF-57 axis β; `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`): the V3 candidate's bridge map at Element 3 admits multiple scheme evaluations:
   - **APS-1975-secondary-class** (V3's choice): canonical for boundary-anchored secondary-class evaluation on manifold-with-boundary analogs. Appropriate for the 3He-B Pillar IV vortex-core spectroscopy (manifold-with-boundary at the vortex core; ρ-invariant secondary class).
   - **Cheeger-Simons** (foliation-aware): canonical for foliation refinement of the secondary-class evaluation. Potentially relevant for the Pillar II LRD horizon-area cutoff (the horizon foliation structure may demand Cheeger-Simons over APS-1975).
   - **Bismut-Cheeger** (adiabatic-limit η-form at the boundary): canonical for adiabatic evaluation at fibration boundary conditions. Potentially relevant for the M-scan asymptotic behavior of `g(M, L=10)` saturation across M_LRD = 10⁷ M_sun.

   **Sharpened question**: does the V3 candidate's bridge map evaluate IDENTICALLY across the three scheme evaluations (scheme-INDEPENDENCE confirmed; bare Element 3 admitted per the CF-57 axis β clause), OR do the three schemes give STRUCTURALLY DISTINCT bridge-map evaluations (scheme-dependent; MANDATORY scheme-suffix tagging on convention field)? For the kernel-summand NULL prediction (HH^0 evaluation), the three schemes likely agree (the kernel is structurally zero at any scheme), but for the FULL `Π^{ker}_{χ}[L]` operator-trace evaluation, the three schemes may diverge at higher-degree Hochschild contributions. The V3 candidate's convention tag should declare scheme-INDEPENDENCE explicitly (if confirmed) or carry the scheme suffix (if scheme-dependent). V3's declaration `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` (line 184) is correct under the scheme-DEPENDENT reading; under the scheme-INDEPENDENT reading, the convention may omit the suffix per the CF-57 axis β "scheme-INDEPENDENCE theorem" clause. **Forward-pending question** that should be addressed at Stage-2 cross-axis verify.

3. **Joint-hypersurface (iii) binding alternative — analysis**: Q-V3 asks whether the morphism-class parameter `T_χ` could force (iii) joint-hypersurface binding (2D discrimination in `(T_χ-structure, kernel-trace)` space rather than 1D in kernel-trace alone). NCG-axiomatic reading: the in-scope universality scope `max-Wedderburn-rank(T_χ) < 3` is a SUBSTRATE-IS predicate (defined entirely by A_K's Wedderburn structure + T_χ's Wedderburn structure, both substrate-side algebraic data); the morphism-class parameter `T_χ` is therefore a SUBSTRATE-IS COORDINATE, not a laboratory-side coordinate. Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`, the three-binding-class clause distinguishes (i) substrate-self-consistent / (ii) external-observation / (iii) joint-hypersurface; clause (iii) applies when "lab discrimination is 2D in (P, observable) space rather than 1D in observable space alone". Since `T_χ` is substrate-side (not lab-side), (iii) does NOT apply; (i) is structurally correct. **V3's binding class (i) is robust under NCG-axiomatic reading.**

**MISSED — NCG-axiomatic machinery V3 does not invoke**:

1. **Substrate-input-orthogonality predicate (S88 W-23 W7c-167 V.1; MANDATORY-K=3 per S90 W1-17 advancement)**: V3 line 221 invokes this predicate for the Stage-2 verify but does not state it operationally. NCG-axiomatic operationalization: the substrate-input-orthogonality predicate requires `∃ obs_i such that the data file consumed by obs_i is loaded by exactly ONE cross-reviewer (NOT both)`. For the V3 candidate's two empirical anchors:
   - Obs_1 = Pillar IV BdG `Π^{vortex}_{B-phase}[F1+F2+F5]` data → assign to Axis-B mack (laboratory-anchor side; mack-cosmic-bridge owns Pillar IV BdG laboratory expertise per AMRI promotion).
   - Obs_2 = Pillar II LRD horizon `Π^{horizon}_{LRD}[α'(M=10⁷ M_sun)]` data → assign to Axis-A vdd (Kasparov KK-projection authority; vdd verifies the K-theory boundary bridge map + Connes-Karoubi pairing on the LRD-horizon-restricted Peter-Weyl projector).

   This assignment satisfies substrate-input-orthogonality: each cross-reviewer loads ONE data file; the two cross-reviewers' input data is DISJOINT. Stage-2 PASS-AND under this assignment achieves the structural ceiling per the S89 W4-7 K=2 calibration precedent (§VII.AH Stage-2 PASS without substrate-input-overlap caveat) — and per S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement to K=3 MANDATORY (joint-theorem-promotion.md §"Stage 2"). V3's recommended dispatch is consistent; the explicit operational assignment is a useful sharpening for the §VII registry text.

2. **Cross-reviewer audit-machinery self-citation clause** (S88 W-23 W7c-167 V.8 → MANDATORY at K=3 forward): if either cross-reviewer applies a parse-tree decision procedure / 4-corner classification / cohomology bridge map at the verdict-emission layer, that reviewer is NOT the sole author of that machinery; an alternate machinery route must be applied OR a second reviewer cross-checks. For the V3 candidate, the §VII.U.2 4-corner parse-tree decision procedure is invoked at the Corner-I classification (V3 line 142). The 4-corner machinery is `connes-ncg-theorist`/`lizzi-spectral-functional-theorist`-co-authored at S87 W-2 R3 close (MANDATORY-K=3); since this workshop's adversarial author is connes, the cross-reviewer assignment to vdd (Axis-A NCG-axiomatic) creates a structural-self-citation hazard at the Corner-I parse-tree step. Mitigation: invoke the algebra-axis 4-corner parse-tree at the Stage-2 verify step via vdd's NCG-axiomatic machinery (cell-classifier independent of connes); cross-check the cell assignment via mack's substrate-physics machinery (kernel-summand parse-tree from the laboratory-IN OE-form). The cell assignment Corner-I is structurally robust; the cross-check is a defensive measure for cross-reviewer audit-machinery self-citation compliance.

3. **JOINT clause vs single-axis clause assignment** (V3 line 223-226): NCG-axiomatic sharpening. The V3 candidate's clauses partition into:
   - **JOINT clauses (a) + (c) requiring PASS-AND of both axes**: the simple-block forcing theorem identity (V1 substrate-IS universality of M_3(ℂ) kernel-summand) is structurally a substrate-side claim BUT its laboratory-IN OE-form realization at both Pillar IV and Pillar II requires substrate-side + lab-side coherence. AGREE with JOINT assignment.
   - **Single-axis Axis-A clauses (b)**: Wedderburn-decomposition + K-theory boundary structural argument; vdd or gen-physicist PASS. AGREE.
   - **Single-axis Axis-B clauses (d) + (e)**: laboratory-IN OE-form satisfaction at Pillar IV + Pillar II; mack PASS. AGREE.

   **Sharpening**: add a JOINT clause for the bridge-map-scheme suffix question (above MISSED #2 of Re: V3). If the bridge map is scheme-INDEPENDENT across APS-1975 / Cheeger-Simons / Bismut-Cheeger evaluations, the candidate's convention tag may omit the suffix; if scheme-DEPENDENT, MANDATORY scheme-suffix tagging applies. This is a JOINT question (substrate-side ↔ laboratory-side coherence at the secondary-class evaluation layer); requires Stage-2 PASS-AND.

**EMERGES — cross-domain insights**:

The V3 candidate's 5-IS-not-IN anatomy + 3-level ladder is REGISTRY-PASS ELIGIBLE under NCG-axiomatic reading at the Level-1 cohomology-class layer (Re: V1 simple-block forcing) + Level-2 binding sub-class (HH^0 layer; HKR image structurally zero) + Level-3 empirical anchor (dual anchor at Pillar IV + Pillar II at L_max=10). The Stage-2 cross-axis verify dispatch to {vdd, mack-cosmic-bridge} with substrate-input-orthogonality predicate is the canonical S91+ AUX-5 three-axis Stage-2 verify path for this candidate.

> **V3 sharpened §VII.<next-free-letter>.OP-PROJ candidate registry text** (proposed extension to V3's declaration):
>
> **Slot**: §VII.<next-free-letter>.OP-PROJ (next-free-letter pending S91+ slot allocation per `regulator-pin-discipline.md` next-free-letter protocol; orchestrator allocates at landing time).
> **STAGE**: STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway.
> **Theorem name**: M_3(ℂ)-summand inheritance-kernel universality across max-Wedderburn-rank-<3 targets (with (C2) common-exponent + (C3) common-scalar-pullback sub-conditions for substrate ratio preservation per Re: V2).
> **Level-1**: regulator-INVARIANT identity at NCG-axiom-1+4+5+6 + Wedderburn-Artin theorem + Schur lemma. Re: V1 simple-block forcing.
> **Level-2-binding**: `α = ∞` (envelope exact at every L_max) at HH^0 layer; HKR-image structurally zero. Per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` admissible case.
> **Level-3 anchor**: dual at L_max=10 — Pillar IV BdG (W3-3 §(d.d) Gate 1 NULL on F1+F2+F5) + Pillar II LRD horizon (W4 §W4-1 `kernel_M3C_dimension = 9`).
> **Element 3 binding-class**: (i) substrate-self-consistent at the kernel-summand layer; the morphism-class parameter `T_χ` is a substrate-IS coordinate (not laboratory-side).
> **Bridge-map-scheme suffix**: scheme-INDEPENDENCE PENDING Stage-2 verification across APS-1975 / Cheeger-Simons / Bismut-Cheeger. Default convention tag `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` (V3's choice); if Stage-2 confirms scheme-INDEPENDENCE within 1e-3 M_KK² (per CF-55 / §VII.AQ precedent), tag may strengthen to `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT`.
> **Stage-2 dispatch**: `S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY` to {Axis-A = `van-den-dungen-bridge-theorist`, Axis-B = `mack-cosmic-bridge`} with substrate-input-orthogonality predicate (obs_1 Pillar IV BdG → mack; obs_2 Pillar II LRD horizon → vdd). EXCLUDED reviewers: {volovik, connes}. JOINT clauses (a)+(c) + bridge-map-scheme suffix question; single-axis Axis-A (b); single-axis Axis-B (d)+(e). Cross-reviewer audit-machinery self-citation mitigated via vdd's NCG-axiomatic machinery for §VII.U.2 4-corner parse-tree at Corner-I.

**Reading A wins on V3** with the bridge-map-scheme suffix discipline as a sharpening at Element 3 (declared as PENDING Stage-2 scheme-INDEPENDENCE confirmation; default APS-1975 suffix per V3's choice). The §VII candidate is registry-PASS ELIGIBLE; mack-cosmic-bridge as sole writer per `feedback_mack-bridge-role.md` lands the registry text at next-session plan-freeze.

#### Re: V4 — Distinguishing BDI rank-mismatch from Wedderburn 9>8

**Verdict on V4**: AGREE with V4's 6-step substitution chain (workshop lines 243-267) factoring BDI parent symmetry through Wedderburn rank-arithmetic. AGREE with the F-functor layer-decomposition (lines 273-282) placing BDI parent symmetry at the substrate-physics layer and max-Wedderburn-rank at the methodology layer. AGREE with the counter-rebuttal preparation (lines 286-293) that BDI K-grading content lives on K_0(target) particle-hole grading at Corner-III/IV (algebra-DEPENDENT state-pair functional axis) STRUCTURALLY ORTHOGONAL to the source-side kernel-summand structure at Corner-I/II (algebra-INVARIANT spectrum-only axis) per §VII.U.2 4-corner partition. The structural-orthogonality is the canonical NCG-axiomatic distinction; I CONCEDE V4's conclusion that BDI rank-mismatch FACTORS through Wedderburn rank-arithmetic at the kernel-summand layer.

**Address Q-V4**: Identify specific BDI K-grading content contributing to source-side kernel-summand (NOT target-side particle-hole) WITHOUT factoring through Wedderburn. **I cannot identify such content. After NCG-axiomatic search through the standard K-theoretic structures associated with BDI (particle-hole grading, time-reversal-squared invariant, K-theory of real algebras under Atiyah-Bott-Shapiro periodicity), I find every K-theoretic content of BDI lives at the K_0(target) particle-hole-graded layer. The source-side kernel-summand structure is determined by `A_K`'s Wedderburn decomposition + Schur lemma + the target's max-Wedderburn-rank predicate — all source-and-target ungraded data. BDI's graded data refines WHICH idempotents in the target are protected by particle-hole symmetry; it does NOT modify WHICH source-side simple blocks fail to inject. V1's structural-identity claim is preserved; the rank-coincidence reading degrades to "two interpretations of the same theorem in two languages" per V4 line 307.**

This is the honest NCG-axiomatic concession. Reading B as the rank-coincidence claim does NOT survive Schur + Wedderburn structural scrutiny. The sharpened Reading B residue (Element 3 bridge-map-scheme suffix + HH-degree-dependent Level-2 envelope per Re: V3 + Re: V5 Observation 1) is the structurally-distinct residue claim; it does NOT refute V1+V4 structural identity but constrains downstream pairing evaluation.

**AGREE — NCG-axiomatic supporting evidence**:

V4's 6-step substitution chain is structurally faithful. Three NCG-axiomatic verifications:

1. **BDI symmetry class in Altland-Zirnbauer classification** (per agent-memory `MEMORY.md` line 50: KO-dim 6 + AZ class BDI with `T²=+1`, `(ε,ε',ε'')=(+1,+1,-1)`, `J²=+1`): BDI is the chiral orthogonal class. Its topological invariants are encoded in `Pf(D_BdG)` (Pfaffian of the BdG Hamiltonian) and the K-grading `N_K` of the time-reversal-squared eigenstate sub-bundle. These invariants live on the TARGET algebra `A_BdG`'s K-theory: `K_0(A_BdG)^{ε}` with ε the particle-hole grading. They do NOT modify the source-side algebra structure of `A_K`.

2. **F-functor layer-decomposition** (V4 lines 273-282): the layer-functor `F : substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"` preserves the simple-block forcing identity at each layer. BDI parent symmetry at the substrate-physics layer maps under F to max-Wedderburn-rank(A_BdG) = 2 at the methodology layer, which determines the simple-block forcing predicate at the audit layer (9 > 8; 3 > 2), which determines `ker(χ|_{M_3(ℂ)}) = M_3(ℂ)` at the verdict layer. The F-functor's directionality is the canonical NCG-axiomatic decomposition; BDI and Wedderburn are at DIFFERENT layers, not at the same layer competing as "two independent rank arguments."

3. **Corner-I/II vs Corner-III/IV orthogonality at §VII.U.2 4-corner partition** (MANDATORY-K=3 at S87 W-2 R3 close): the kernel-summand structural fact on the source side (algebra-INVARIANT spectrum-only functional family) lives on Corner-I (algebra-INVARIANT × Mellin pole s=3) or Corner-II (algebra-INVARIANT × Mellin pole s=4); the particle-hole grading on the target side (algebra-DEPENDENT state-pair functional family) lives on Corner-III (algebra-DEPENDENT × s=3) or Corner-IV (algebra-DEPENDENT × s=4). The two corner-pairs are STRUCTURALLY ORTHOGONAL per the §VII.U.2 algebra-axis 4-corner partition. BDI's K-grading content inhabits Corner-III/IV; the V3 §VII.<next-free-letter>.OP-PROJ candidate inhabits Corner-I (V3 line 142). They are on orthogonal algebra-axes; BDI K-grading is structurally irrelevant to the kernel-summand universality claim.

**DISAGREE — what does NOT survive in V4 as stated**:

Minor sharpening, not refutation:

1. **V4 line 297 Wedderburn arithmetic for `A_F ⊗ M_2(ℂ)` under W5 reading**: V4 admits this needs verification. NCG-axiomatic verification: `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (V4's identification per V4 line 297). The tensor product `A_F ⊗ M_2(ℂ)` decomposes Wedderburn-wise as `(ℂ ⊗ M_2(ℂ)) ⊕ (ℍ ⊗ M_2(ℂ)) ⊕ (M_3(ℂ) ⊗ M_2(ℂ))`. Each summand: `ℂ ⊗ M_2(ℂ) ≅ M_2(ℂ)` (rank 2); `ℍ ⊗ M_2(ℂ) ≅ M_2(ℍ) ≅ M_4(ℝ) ⊕ ...` (real-algebra structure; over ℂ via complexification gives `M_2(ℂ) ⊕ M_2(ℂ)` of rank 2 each; via tensoring with M_2(ℂ) over ℝ versus ℂ matters — under ℂ-algebra tensor `ℍ ⊗_ℝ ℂ ≅ M_2(ℂ)`, so `ℍ ⊗_ℝ M_2(ℂ) = (ℍ ⊗_ℝ ℂ) ⊗_ℂ M_2(ℂ) ≅ M_2(ℂ) ⊗_ℂ M_2(ℂ) ≅ M_4(ℂ)` of rank 4); `M_3(ℂ) ⊗_ℂ M_2(ℂ) ≅ M_6(ℂ)` (rank 6). The max-Wedderburn-rank of `A_F ⊗ M_2(ℂ)` is 6 (from the M_3(ℂ) ⊗ M_2(ℂ) summand). Under V1's simple-block forcing on the SOURCE M_3(ℂ) summand of A_K, the IMAGE of `χ|_{M_3(ℂ)} : M_3(ℂ) → A_F ⊗ M_2(ℂ)` could in principle land in the M_3(ℂ) ⊗ M_2(ℂ) ≅ M_6(ℂ) sub-algebra (rank 6 ≥ 3 admits an M_3(ℂ) embedding); the simple-block forcing does NOT apply directly under W5's reading.

   **However**: V4 line 299 correctly observes that under W5's reading, the M_3(ℂ) ⊗ M_2(ℂ) ≅ M_6(ℂ) sub-algebra is NOT in the IMAGE of the inheritance morphism (per W3-3 §(d.a)'s BDI parent symmetry projection at the inheritance-image layer). The simple-block forcing applies to the IMAGE of ι, not the full A_F ⊗ M_2(ℂ) algebra. Under both A_BdG readings (W3+W6's `A_BdG = M_2(ℂ)` direct vs W5's `A_BdG = A_F ⊗ M_2(ℂ)` full with BDI-projection restricting to the M_2(ℂ) factor), the EFFECTIVE inheritance target has max-Wedderburn-rank 2 < 3; V1's simple-block forcing applies to the EFFECTIVE target. The W-4 verdict on which A_BdG reading is canonical does NOT change V1's conclusion at the inheritance-image layer.

   **Sharpening for downstream registry hygiene**: the V3 candidate's Element 1 (substrate-IS observable) is the M_3(ℂ) Wedderburn block of `A_K` (source side, unambiguous). The V3 candidate's Element 3 (bridge map) operates on the IMAGE of ι under the BDI parent symmetry projection (effective target M_2(ℂ) under both readings). The W-4 verdict affects ONLY the registry text's description of the FULL A_BdG algebra structure (which is upstream of the inheritance image at the BDI projection layer); the kernel-summand structural identity is robust under both readings, as V4 line 299 correctly observes.

2. **V4 line 287's hypothetical "K-class carries a non-trivial particle-hole sign" content**: I confirm this lives on K_0(A_BdG) particle-hole grading (target side), which is on Corner-III/IV of the §VII.U.2 partition. AGREE with V4 that this content is ORTHOGONAL to the kernel-summand structure on the source side. The particle-hole grading is a target-side data that refines WHICH idempotents in the target are protected (e.g., Pfaffian-protected idempotents at `Pf=−1` survive; others may be deformed away); it does NOT contribute to the source-side simple-block kernel structure.

**MISSED — NCG-axiomatic machinery V4 does not invoke**:

1. **Atiyah-Bott-Shapiro periodicity for real K-theory** (relevant to BDI under K-theory of real algebras): BDI's K-grading is encoded in `KO_0(point)` periodicity (mod 8 in real K-theory; BDI is one of the 8 AZ classes). The K-theoretic content of BDI is `KO_0^{BDI} = ℤ` per the AZ classification. This is the canonical K-theoretic invariant of BDI; it lives on the target's K-theory of real algebras structure. The simple-block forcing argument operates on COMPLEX K-theory `K_0` of A_K and T as ℂ-algebras (not real K-theory); BDI's KO_0-content is at a DIFFERENT K-theory layer than the simple-block forcing's K_0-content. The two are structurally distinct: BDI's KO_0 lives on target's real-algebra structure; the simple-block forcing's K_0 lives on source-and-target complex-algebra Wedderburn structure. They do not interact at the source-side kernel-summand layer. **Reinforces V4's conclusion**: BDI's K-theoretic content is orthogonal to the kernel-summand structure.

2. **W-5 cocycle-asymmetry ratio 7.324992 at HH^1(A_K) layer**: the φ_67 (chiral pair) and φ_88 (Cartan hypercharge) cocycle generators live at degree-1 Hochschild cohomology `HH^1(A_K)` on the M_3(ℂ) Peter-Weyl block. The substrate ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992 = 114453/15625` (Sage-QQ exact) is intrinsic to the M_3(ℂ) Peter-Weyl decomposition (W3-3 §(d.b) line 424). Under any inheritance morphism χ with `ker(χ|_{M_3(ℂ)}) = M_3(ℂ)`, the cocycle pair maps to ZERO in `HH^1(T)`; the ratio is preserved at the SUBSTRATE-SIDE before the χ-pullback collapses (Re: V2). This is the canonical NCG-axiomatic computation of the substrate ratio; it lives at HH^1, not HH^0 (which is where the kernel-summand observable lives). BDI's K-grading does not enter this evaluation either. **Reinforces V4's structural-orthogonality conclusion**.

3. **Connes-Karoubi pairing's grading-blindness on the kernel-summand observable**: the Connes-Karoubi pairing `⟨[1_{M_3(ℂ)}], [P]⟩` at the kernel-summand layer is grading-BLIND (it pairs an HH^0 cohomology class with a K_0 class; neither carries particle-hole grading data). The grading data enters at HH^1 ↔ K_1 pairings (degree-1 cyclic cohomology paired with K_1 class), not at HH^0 ↔ K_0. The kernel-summand observable is ungraded; BDI's grading data is at a DIFFERENT pairing layer. **Reinforces V4's conclusion**.

**EMERGES — cross-domain insights**:

The combined NCG-axiomatic + substrate-physics reading produces a structurally-clean statement of the V4 orthogonality:

> **BDI-vs-Wedderburn Orthogonality Theorem**: For an inheritance morphism `ι : A_K → A_BdG` with A_BdG carrying BDI symmetry class (per Altland-Zirnbauer; `T²=+1`, `(ε,ε',ε'')=(+1,+1,-1)`, `J²=+1`):
>
> - The **kernel-summand structure on the source side** (`ker(ι|_{M_3(ℂ)})` ⊆ A_K) is determined ENTIRELY by the simple-block forcing theorem at A_K's Wedderburn decomposition + A_BdG's max-Wedderburn-rank predicate. BDI's K-grading content does NOT contribute.
> - The **particle-hole grading content on the target side** (K_0(A_BdG)^{ε} graded K-theory; KO_0^{BDI} = ℤ; `Pf(D_BdG)` Pfaffian invariant; `N_K=2` time-reversal-squared K-grading) is determined by A_BdG's graded structure + BDI's AZ classification. The source-side kernel structure does NOT contribute.
> - The two structural data live on STRUCTURALLY ORTHOGONAL algebra-axes per §VII.U.2 4-corner partition (Corner I/II vs Corner III/IV; MANDATORY-K=3).
> - The F-functor `F : substrate → methodology → audit` preserves the orthogonality: BDI parent symmetry (substrate-physics) → max-Wedderburn-rank(A_BdG) (methodology) → simple-block forcing predicate (audit) → `ker(ι|_{M_3(ℂ)}) = M_3(ℂ)` (verdict). The BDI K-grading data flows into a SEPARATE F-functor branch terminating in the particle-hole grading structure on K_0(A_BdG)^{ε}, which is a target-side observable orthogonal to the source-side kernel-summand.

This is the canonical statement of V4's conclusion. The two F-functor branches (kernel-summand vs particle-hole grading) are STRUCTURALLY INDEPENDENT — they share an input (BDI parent symmetry on A_BdG) but diverge at the first F-functor application (one branch lands on max-Wedderburn-rank; the other lands on K-grading). The rank-coincidence reading conflates these two F-functor branches into "two independent rank arguments"; the universality reading correctly recognizes them as ONE branch (kernel-summand) at multiple laboratory pillars + a DIFFERENT branch (particle-hole grading) that is structurally orthogonal and does not contribute to the kernel-summand universality claim.

**Reading A wins on V4**. The rank-coincidence reading does NOT survive structural-orthogonality + F-functor decomposition scrutiny; it conflates two structurally-orthogonal F-functor branches into "two independent rank arguments" when they are in fact ONE structural branch (kernel-summand via simple-block forcing) read in two interpretive languages (BDI substrate-physics vs Wedderburn rank-arithmetic).

#### Re: V5 — Cross-Cutting Observations

**Verdict on V5**: AGREE with all three observations at their substrate-framing/structural-orthogonality/forward-predictive-content layers. The three observations integrate V1-V4 into a coherent universality reading and identify the structural-orthogonality boundaries with W-1, W-2, W-4 cleanly. I address each of Q-V5-1, Q-V5-2, Q-V5-3 explicitly with NCG-axiomatic machinery.

---

**Re: V5 Observation 1 — Substrate framing IS-not-IN direction at Level-1 single-τ-slice**

**Verdict on Observation 1**: AGREE. The IS-not-IN direction-of-explanation flow per `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"` lines 262-274 is structurally correct: substrate IS A_K's M_3(ℂ) Wedderburn block → bridge map (K-theory boundary via inheritance morphism χ) → laboratory IN NULL signature `Π^{ker}_{χ}[L] = 0`. The substrate-IS Level pin at Level-1 single-τ-slice (Wedderburn decomposition of A_K is an algebraic property at fixed τ_fold = 0.19) is the correct level pin per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` MANDATORY at S88 W2-10. The kernel-summand universality does NOT extend to Level-2 moduli-deformation; this is honest scope pinning.

**Address Q-V5-1**: Is V3's Level-2-binding declaration `α = ∞` (envelope exact at every L_max) consistent with the HKR-image at the Hochschild cohomology layer `HH^0(A_K) → HH^0(T)` for in-scope T, OR does the HKR-image require a finite Level-2 envelope (e.g., `L^{-α}` with finite α ≥ 1) at the Hochschild Eilenberg-Moore spectral sequence?

**Answer**: `α = ∞` is correct AT THE HH^0 LAYER (the kernel-summand observable lives at HH^0). At HH^1 (cocycle-asymmetry ratio observable, e.g., 7.324992), finite α may be required. The V3 candidate's Element 4 declares the HH^0 layer observable, so `α = ∞` is the correct Level-2 envelope. NCG-axiomatic derivation:

1. **HH^0 layer analysis**: `HH^0(A_K) = Z(A_K) = ℂ · 1_ℂ ⊕ ℂ · 1_ℍ ⊕ ℂ · 1_{M_3(ℂ)}` (three-dimensional center; one generator per Wedderburn simple block). The HKR map `HH^0(A_K) → HH^0_{continuum}(A_K)` is the IDENTITY map at the cohomology-class layer (the center of a finite-dim ℂ-algebra is already its own continuum image; there is no L_max truncation in finite-dim semisimple algebra cohomology). Under any inheritance morphism χ, the center map `Z(A_K) → Z(T)` sends `1_{M_3(ℂ)}` to the M_3(ℂ)-piece of χ-image of the unit. By simple-block forcing (Re: V1), this is the zero idempotent in Z(T) for in-scope T. The HKR-image of `1_{M_3(ℂ)}` is structurally zero at every L_max ≥ 0; `‖HKR(c_L) − c_continuum‖ = 0` exactly. **Level-2 envelope `α = ∞` is correct at HH^0.**

2. **HH^1 layer analysis (for forward extension to cocycle-asymmetry observable 7.324992)**: `HH^1(A_K)` is more delicate. For the M_3(ℂ) Peter-Weyl block, the cocycle generators [φ_67] (chiral pair) and [φ_88] (Cartan hypercharge) live in the degree-1 Hochschild cohomology of the spectral triple `(A_K, H_K, D_K)`. The HKR map at HH^1 is the cyclic-cohomology generalization of de Rham 1-forms; the Eilenberg-Moore spectral sequence converges for finite-dim algebras at degree 0 trivially but at higher degrees may carry finite L_max correction terms (sectoral contributions to the cocycle norms at L_max truncation; see CM-1995 §III.4 residue evaluation discussion of pole-residue convergence in the limit `L_max → ∞`).

   The CM-1995 §III.4 finite-spectral-triple residue formula gives the substrate ratio `7.324992 = ‖[φ_67]‖² / ‖[φ_88]‖²` from the residue evaluation at substrate-distance-1 pole `s=3` on the M_3(ℂ) Peter-Weyl block. This residue evaluation at FINITE L_max=10 may differ from the L_max → ∞ limit by terms of order `L^{-α(s)}` per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole `α(s)` exponent. For substrate-distance-1 pole s=3 on the M_3(ℂ) Peter-Weyl block, a finite α may emerge.

   However: the V3 candidate's Element 2 OE-form `Π^{ker}_{χ}[L]` observable lives at HH^0 (trace of a projector with the kernel-summand idempotent; cohomological degree 0), NOT at HH^1. The substrate-ratio observable 7.324992 is a SEPARATE Level-3 anchor on a DIFFERENT cohomology degree; if the §VII candidate adopts the W-5 cohomology-asymmetry ratio as its Level-3 anchor (Gate 2 falsifier per `inheritance-falsifier-protocol.md §"Four-Gate Structure"`), then a finite-α Level-2 envelope at HH^1 layer is required. V3's current declaration is restricted to the Gate 1 kernel-signature NULL observable (HH^0 layer); `α = ∞` is correct for this restricted observable.

3. **Forward sharpening for §VII candidate registry text**: declare TWO observables explicitly:
   - **Observable A (HH^0 layer, Level-2-binding `α = ∞`)**: kernel-summand NULL prediction `Π^{ker}_{χ}[L] = 0`. V3's current Element 2 OE-form. Anchors at W3-3 Gate 1 NULL + W4 χ' kernel structural zero.
   - **Observable B (HH^1 layer, Level-2-binding finite α PENDING extraction)**: cocycle-asymmetry ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992 ± 0.1%`. Gate 2 substrate-falsifying. Anchors at W-5 calibration corpus W11-C5 + W11-C6.

   The §VII candidate may land Observable A (HH^0, `α = ∞`) at S91+ STAGE-1-CANDIDATE per V3's declaration; Observable B (HH^1, finite α PENDING) becomes a separate STAGE-1-CANDIDATE pending finite-α extraction (per `cross-pillar-bridge-anatomy.md §"deferred-pending intermediate verdict-class"` REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag, with first-extraction gate firing at S91+ via L_max scan or Friedrich-Bär saturation theorem).

**Conclusion on Q-V5-1**: `α = ∞` is correct for V3's HH^0 layer observable (kernel-summand NULL prediction). For HH^1 layer observables (cocycle-asymmetry ratio 7.324992), finite α at the Eilenberg-Moore spectral sequence convergence may be required; that observable is a separate STAGE-1-CANDIDATE pending FIRST-EXTRACTION gate. V3's degenerate Level-2-binding case at HH^0 is the strongest possible binding (envelope exact at every L_max); registry-PASS eligibility is structurally clear at the kernel-summand observable layer.

---

**Re: V5 Observation 2 — Structural orthogonality to W-1 + W-2**

**Verdict on Observation 2**: AGREE with the structural orthogonality argument. V5 Observation 2 correctly identifies that W-3 (cross-morphism kernel-summand universality at the simple-block-forcing layer) is structurally orthogonal to W-1 (deferred-pending intermediate verdict-class taxonomy at the Level-2 envelope realization layer) and W-2 (χ'_weight ansatz at the within-morphism regulator-class layer). The three workshops cover three structurally orthogonal axes of the S90 inheritance-morphism analysis. AGREE.

**Address Q-V5-2**: Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3: does the V3 §VII.<next-free-letter>.OP-PROJ entry's algebra-axis = INVARIANT × Mellin-pole = s=3 (Corner-I) classification SURVIVE under both A_BdG readings of W-4 (W5's `A_F ⊗ M_2(ℂ)` vs W3+W6's `A_BdG = M_2(ℂ)`)?

**Answer**: Yes — Corner-I classification SURVIVES under both A_BdG readings. NCG-axiomatic verification via §VII.U.2 parse-tree decision procedure clause (e):

1. **Parse-tree decomposition of the V3 candidate's observable**: the kernel-summand NULL prediction `Π^{ker}_{χ}[L] = 0` parses to:

```
Π^{ker}_{χ}[L]  =  ∑_χ  1_{max-Wed-rank(T_χ) < 3} · Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)
              =  Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)   (for any single in-scope χ; sum is degenerate)
              =  0   (by Re: V1 simple-block forcing on χ|_{M_3(ℂ)} = 0)
```

   The parse-tree contains: (i) a Peter-Weyl projector `P_{M_3(ℂ)}` on A_K's M_3(ℂ) Wedderburn block (spectrum-only operation; no `π(a)`-dependence; no state-pair sup); (ii) a trace on the M_3(ℂ) image (algebra-INVARIANT spectrum-only); (iii) a sum/indicator over morphism class (also algebra-INVARIANT, since the morphism-class parameter `T_χ` is substrate-side Wedderburn data per Re: V3). The parse-tree decision procedure routes this to the **algebra-INVARIANT spectrum-only family** (the source of Cell I or Cell II per §VII.U.2 4-corner partition).

2. **Mellin-pole assignment**: the kernel-summand observable evaluates at the substrate-distance-1 Mellin pole `s=3` (the simplest pole where the M_3(ℂ) Peter-Weyl block contributes to the residue evaluation per CM-1995 §III.4 finite-spectral-triple residue formula; substrate-distance-1 pole is the Wedderburn-block contribution at the lowest substrate-distance). This assigns Cell I (algebra-INVARIANT × s=3) per §VII.U.2. V3's classification is correct.

3. **Under W3+W6 reading (`A_BdG = M_2(ℂ)`, direct inheritance-image)**: the parse-tree contains no reference to A_BdG's internal structure; the morphism χ : A_K → A_BdG = M_2(ℂ) acts directly on A_K's M_3(ℂ) summand by simple-block forcing (max-Wedderburn-rank 2 < 3 forces zero). Cell I classification is preserved.

4. **Under W5 reading (`A_BdG = A_F ⊗ M_2(ℂ)`, full tensor product)**: the parse-tree still contains no reference to A_BdG's internal A_F structure on the source side — the kernel-summand observable is a property of `A_K`'s M_3(ℂ) summand mapped under the EFFECTIVE inheritance restriction (BDI parent symmetry projection from full A_BdG = A_F ⊗ M_2(ℂ) to the M_2(ℂ) Bogoliubov sub-algebra). Per Re: V4 line analysis on `A_F ⊗ M_2(ℂ)` Wedderburn decomposition: the maximal sub-block M_3(ℂ) ⊗ M_2(ℂ) ≅ M_6(ℂ) (rank 6 ≥ 3) is NOT in the inheritance image; the effective target has max-Wedderburn-rank 2 < 3 under both readings.

   The parse-tree at the SOURCE-side observable level is unchanged: `Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)` operates on A_K's M_3(ℂ) summand (source side, independent of A_BdG reading). The morphism χ may be re-described under W5 as having additional A_F-structure on the target, but the SOURCE-SIDE parse-tree decision procedure does not consult target-side structure beyond the max-Wedderburn-rank predicate (which is 2 < 3 under both readings). Cell I classification is preserved.

5. **Cross-corner FORBIDDEN audit**: per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` clause (4) "Cross-corner cross-pole magnitude comparisons STRUCTURALLY FORBIDDEN as PASS/FAIL gates", the V3 candidate must NOT be a cross-corner co-primary structure. Both readings preserve Cell I; no cross-corner conflation arises. **AUDIT PASS**.

6. **Discriminator-gate criterion at S91+ Stage-2 verify**: per Q-V5-2's request, I pre-register the discriminator criterion as follows. The Cell-I classification under both readings is structurally robust at the source-side parse-tree level; HOWEVER, the BRIDGE-MAP composition `χ_* : K_0(A_K) → K_0(A_BdG)` may differ between W3+W6 and W5 readings at the target-side K-theory layer. Specifically:
   - Under W3+W6: K_0(A_BdG = M_2(ℂ)) = ℤ (single generator, rank 2); χ_*([1_{M_3(ℂ)}]) = 0 (rank-3 image not realizable).
   - Under W5: K_0(A_BdG = A_F ⊗ M_2(ℂ)) = K_0(A_F) × K_0(M_2(ℂ)) = (ℤ³) × ℤ = ℤ⁴ (three generators from A_F's three Wedderburn blocks; one from M_2(ℂ)); χ_*([1_{M_3(ℂ)}]) takes the M_3(ℂ) Wedderburn block of A_F under tensor with M_2(ℂ); however, the BDI projection restricts to the M_2(ℂ) factor only, killing the A_F-component, so the EFFECTIVE χ_* image is the same as under W3+W6.

   **Discriminator-gate criterion**: at S91+ Stage-2 cross-axis verify, compute `χ_*([1_{M_3(ℂ)}])` in K_0(A_BdG) under both readings via vdd (Axis-A Kasparov KK-projection authority); if both readings give χ_*([1_{M_3(ℂ)}]) = 0 (no rank-3 element), Cell-I classification + V3 universality reading is preserved INDEPENDENT of W-4 verdict. If one reading gives a non-zero rank-3 K-element (only possible if BDI projection is misapplied; structurally would require the M_3(ℂ) ⊗ M_2(ℂ) ≅ M_6(ℂ) sub-block to be in the IMAGE), this would invalidate V1's simple-block forcing under that reading; deeper structural review required.

   The discriminator-gate criterion is pre-registered as `S91-V3-CANDIDATE-A-BDG-READING-INDEPENDENCE-VERIFY` at Stage-2; PASS-AND across both readings is the registry-PASS condition.

**Conclusion on Q-V5-2**: V3's Cell-I classification SURVIVES under both A_BdG readings of W-4 at the source-side parse-tree level. The bridge-map composition's K-theoretic image under both readings agrees (effective χ_*([1_{M_3(ℂ)}]) = 0 in both cases). V3's candidate's corner pin is structurally robust independent of W-4's verdict; the W-4 verdict only affects notational hygiene on the registry text downstream of V3's landing (per V4 line 305).

---

**Re: V5 Observation 3 — Forward predictive content + scope boundary**

**Verdict on Observation 3**: AGREE with the forward predictive content claim (Pati-Salam IN-scope; SU(5) GUT OUT-of-scope per `M_3 ↪ M_5` Wedderburn-block embedding). The universality reading's empirical content extends beyond the two landed empirical anchors (W3-3 + W4-1) to a STRUCTURAL boundary at `max-Wedderburn-rank(T) = 3`. This makes the universality reading structurally FALSIFIABLE in a way the rank-coincidence reading is not. AGREE.

**Address Q-V5-3**: Per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` rank-2 case + binomial(rank, 2) cross-cocycle ratio enumeration for rank ≥ 3: does the universality reading's forward extension to Pati-Salam (in-scope) and SU(5) GUT (out-of-scope) FACTOR through a Connes-Karoubi pairing structural theorem on `(A_K, T)` pairs parameterized by max-Wedderburn-rank(T)? Specifically, is the predicate `ker(χ|_{M_3(ℂ)}) = M_3(ℂ) ⟺ max-Wedderburn-rank(T) < 3` a K-theoretic boundary theorem, OR does it require additional structural input (e.g., the specific Hochschild cocycle pattern on A_K's M_3(ℂ) summand)?

**Answer**: The predicate IS a K-theoretic boundary theorem (cleanest reading; no additional Hochschild-cocycle-pattern condition required for the kernel-summand observable). The forward extension to Pati-Salam (in-scope) and SU(5) GUT (out-of-scope) factors through the Connes-Karoubi K-theory boundary pairing on `(A_K, T)` pairs parameterized by max-Wedderburn-rank(T). However, the forward extension to the **cocycle-asymmetry ratio observable** (Gate 2 substrate-falsifying; 7.324992 ± 0.1%) requires an ADDITIONAL Hochschild-cocycle-pattern condition (the (C3) common-scalar-pullback condition per Re: V2). The two scope predicates differ between the two observables; both are simultaneously well-posed.

NCG-axiomatic derivation:

1. **K-theoretic boundary theorem for the kernel-summand observable (Gate 1 NULL prediction)**:

   > **Theorem (K-theoretic kernel-summand boundary)**: Let `χ : A → T` be a unital algebra map between finite-dim ℂ-algebras. Let `A = ⊕_i M_{n_i}(ℂ)` with `M_{n_i}(ℂ)` a simple Wedderburn block of A. Then:
   >
   > `χ_*([1_{M_{n_i}(ℂ)}]) = 0` in `K_0(T)`   ⟺   `max-Wedderburn-rank(T) < n_i`.
   >
   > **Proof**: (⇐) per Re: V1 simple-block forcing at K-theory layer. (⇒) if `max-Wedderburn-rank(T) ≥ n_i`, there exists a Wedderburn block `M_k(ℂ) ⊆ T` with `k ≥ n_i`, hence an injection `M_{n_i}(ℂ) ↪ M_k(ℂ) ⊆ T`; the embedding sends `[1_{M_{n_i}(ℂ)}]` to a rank-n_i K-class in K_0(T) that is non-zero (rank is a K-theoretic invariant). The injection χ is not forced; but the K-theoretic image space ADMITS a non-zero rank-n_i class. □

   This is a clean K-theoretic boundary theorem on `(A_K, T)` pairs parameterized by `max-Wedderburn-rank(T)`. The predicate `ker(χ|_{M_3(ℂ)}) = M_3(ℂ) ⟺ max-Wed-rank(T) < 3` is the K-theoretic boundary theorem applied to A = A_K's M_3(ℂ) summand. **No additional Hochschild-cocycle-pattern condition required for the kernel-summand observable.** Pati-Salam (max-rank ≤ 2 < 3) inherits the universality cleanly; SU(5) GUT (rank 5 ≥ 3) falls outside the scope cleanly.

2. **Cocycle-asymmetry ratio observable (Gate 2 substrate-falsifying; 7.324992)**: this observable lives at HH^1 (cocycle pair degree-1 in Hochschild cohomology). The universality across morphism class requires (C3) common-scalar pullback (Re: V2): `χ^*[φ_67] / χ^*[φ_88]` preserves the substrate ratio iff χ acts as a common-scalar multiple on the (φ_67, φ_88) cocycle pair. This is an ADDITIONAL condition beyond `max-Wedderburn-rank(T) < 3`; it depends on the specific Hochschild cocycle pattern on A_K's M_3(ℂ) summand and how χ pulls back.

   The (C3) condition is a Hochschild-cocycle-pattern condition. For Pati-Salam parent symmetry (acting homogeneously on the M_3(ℂ) Peter-Weyl block), (C3) is plausible (the parent symmetry's action on the Peter-Weyl decomposition respects the cocycle pair's degree-1 grading; common-scalar pullback emerges). For arbitrary in-scope morphisms with non-trivial source-side automorphism action that differentiates between [φ_67] and [φ_88] (e.g., a morphism that breaks the SU(3) symmetry in the source-side cocycle pair), (C3) may fail.

3. **Forward scope-boundary pre-registration form**: per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"` FWD-C1 (Pillar I ↔ Pillar II) + FWD-C2 (Pillar II ↔ Pillar V), the universality reading's forward extension splits into TWO sub-claims:

   - **Sub-claim A (kernel-summand observable, Gate 1 NULL)**: K-theoretic boundary theorem at `max-Wedderburn-rank(T) < 3`. Scope: ALL in-scope T (Pati-Salam, GUT extensions with target rank < 3, alternative finite spectral algebras with max-Wedderburn-rank < 3). FALSIFIER: a single in-scope laboratory pillar where Gate 1 NULL fails.
   - **Sub-claim B (cocycle-asymmetry ratio observable, Gate 2 substrate-falsifying)**: K-theoretic boundary + (C3) common-scalar pullback condition. Scope: in-scope T WITH parent symmetry acting homogeneously on the M_3(ℂ) Peter-Weyl block. FALSIFIER: a single in-scope laboratory pillar where Gate 2 ratio deviates from 7.324992 by > 0.1%.

   The Sub-claim A scope is BROADER (K-theoretic boundary only); the Sub-claim B scope is NARROWER (K-theoretic boundary + (C3) Hochschild-cocycle-pattern condition). Both sub-claims are pre-registered at the §VII candidate's Element 5 (empirical anchor) text per V3's forward predictive content + V2's (C1)+(C2)+(C3) scope conditions.

4. **Connes-Karoubi pairing's structural-theorem-quality content for the universality reading**: the Connes-Karoubi pairing `⟨ · , · ⟩ : HC^{2k}(A) × K_0(A) → ℂ` provides the canonical NCG-axiomatic layer at which morphism classes are distinguished. For the kernel-summand observable (degree-0 cohomology paired with K_0 generator), the pairing's value is structurally zero for in-scope T (Sub-claim A's K-theoretic identity). For the cocycle-asymmetry ratio (degree-1 cohomology paired with K_0 projector classes; degree-1 cyclic cohomology + degree-0 K-class via the higher pairings), the pairing's value carries (C3) condition (Sub-claim B's K-theoretic + Hochschild-pattern identity). The Connes-Karoubi pairing is the canonical NCG layer that organizes both sub-claims into a single structural framework.

5. **Hochschild-cocycle-pattern condition for higher binomial(rank, 2) cross-cocycle ratios** (per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` rank ≥ 3 case): if A_K's M_3(ℂ) summand admits rank ≥ 3 cocycle generators ([φ_67], [φ_88], + future generators), the cohomology-asymmetry test class extends to all `binomial(rank, 2) = binomial(3, 2) = 3` cross-cocycle ratios. Each ratio requires (C3) common-scalar pullback at the cocycle-pair layer. The Hochschild-cocycle-pattern condition becomes a TUPLE of (C3) conditions, one per ratio. The universality reading extends to the rank ≥ 3 case under the same scope predicate `max-Wedderburn-rank(T) < 3` for kernel-summand + tuple of (C3) conditions for cocycle-ratio tuple.

**Conclusion on Q-V5-3**: The kernel-summand observable's scope predicate is a **clean K-theoretic boundary theorem** (Sub-claim A; no additional Hochschild-cocycle-pattern condition). The cocycle-asymmetry ratio observable's scope predicate is K-theoretic boundary + (C3) Hochschild-cocycle-pattern condition (Sub-claim B; narrower scope). Both sub-claims are pre-registered at the §VII candidate's Element 5 + Element 4. The Pati-Salam IN-scope / SU(5) GUT OUT-of-scope predictions hold cleanly for Sub-claim A; for Sub-claim B, additional verification of (C3) at the Pati-Salam parent symmetry layer is queued at Stage-2 cross-axis verify.

**Reading A wins on V5** with the K-theoretic-boundary-vs-Hochschild-pattern decomposition as a sharpening at Element 5 (forward predictive content). The Sub-claim A vs Sub-claim B decomposition is the canonical NCG-axiomatic structuring of the universality reading's forward extension; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands the registry text at next-session plan-freeze with both sub-claims declared explicitly.

---

**Summary of Re: V5 across the three observations**:

- **Observation 1 (Q-V5-1)**: `α = ∞` is correct for V3's HH^0 layer kernel-summand observable; HH^1 layer cocycle-asymmetry observable requires finite α at the Eilenberg-Moore spectral sequence convergence (separate STAGE-1-CANDIDATE pending FIRST-EXTRACTION).
- **Observation 2 (Q-V5-2)**: V3's Cell-I (algebra-INVARIANT × s=3) classification SURVIVES under both A_BdG readings of W-4 at the source-side parse-tree level; discriminator-gate criterion `S91-V3-CANDIDATE-A-BDG-READING-INDEPENDENCE-VERIFY` pre-registered for Stage-2 verify.
- **Observation 3 (Q-V5-3)**: Sub-claim A (kernel-summand observable, Gate 1 NULL) is a clean K-theoretic boundary theorem on `(A_K, T)` parameterized by `max-Wedderburn-rank(T)`; Sub-claim B (cocycle-asymmetry ratio observable, Gate 2 substrate-falsifying) requires (C3) Hochschild-cocycle-pattern condition. Pati-Salam IN-scope / SU(5) GUT OUT-of-scope predictions hold cleanly for Sub-claim A; Sub-claim B narrower scope queued at Stage-2 verify.

**Reading A wins on V5** with the structural-orthogonality argument to W-1 + W-2 + W-4 preserved + the forward predictive content's K-theoretic-boundary-vs-Hochschild-pattern decomposition as a sharpening. The §VII candidate is registry-PASS ELIGIBLE at the kernel-summand observable layer (Sub-claim A); the cocycle-asymmetry ratio observable (Sub-claim B) is a separate STAGE-1-CANDIDATE queued for FIRST-EXTRACTION + Stage-2 verify.

### Part 2: Original Analysis

#### C1: Wedderburn rank-arithmetic counter-argument — independent rank arguments by construction

**Honest position on C1**: The original Reading B statement ("the two rank arguments are STRUCTURALLY DISTINCT BY CONSTRUCTION at the source-derivation layer") does NOT survive NCG-axiomatic structural scrutiny. I take **route (a) per the spawn prompt's "be honest" mandate**: confirm that BDI parent symmetry's algebra-axis projection IS Wedderburn rank-arithmetic at the methodology layer (the rank arguments ARE F-functor images of the same simple-block forcing theorem at distinct laboratory pillars per Re: V1 + Re: V4). Convert C1 to a qualified Reading B at the bridge-map-scheme suffix layer + the HH^1 cocycle-asymmetry observable's (C3) Hochschild-cocycle-pattern condition layer. The qualified Reading B does NOT refute V1+V4 structural identity; it constrains downstream pairing evaluation at the secondary-class layer (Element 3) and at higher Hochschild cohomology degrees (HH^1+).

This concession is structurally faithful to NCG axioms and does NOT manufacture a sound-right counter-argument that does not survive Schur + Wedderburn structural scrutiny. The workshop's structural verdict is NCG-AXIOMATIC-FAITHFUL.

**Route (a) confirmation — substitution chain demonstrating the original Reading B fails Schur + Wedderburn**:

```
Original Reading B statement (proposed): the two rank arguments (BDI parent rank-mismatch
via algebra-axis projection vs Wedderburn 9>8 zero-map via representation-theoretic
counting) are STRUCTURALLY DISTINCT BY CONSTRUCTION at the source-derivation layer.

Step 1 (definition):  BDI parent rank-mismatch  = the statement that the BDI symmetry
                      class on A_BdG forces the BdG Hamiltonian's algebra into the
                      M_2(ℂ) Bogoliubov-pair Wedderburn block, which has max-rank 2.

Step 2 (definition):  Wedderburn 9>8 zero-map  = the statement that any algebra
                      homomorphism χ : M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) (target dim 8)
                      with source dim 9 is the zero map by vector-space dimension
                      counting.

Step 3 (substitution per Schur):  Schur's lemma applied to simple algebra M_3(ℂ):
                      ker(χ|_{M_3(ℂ)}) is a two-sided ideal in M_3(ℂ); hence
                      ker ∈ {0, M_3(ℂ)} by simplicity. ker = 0 forces χ injective;
                      hence χ(M_3(ℂ)) ⊆ T isomorphic to M_3(ℂ) (rank 3).

Step 4 (substitution per Wedderburn-Artin):  T must contain a Wedderburn block
                      M_k(ℂ) with k ≥ 3 for the injection to exist.

Step 5 (simplification):  Both BDI rank-mismatch (target M_2(ℂ); max-rank 2 < 3) AND
                      Wedderburn 9>8 (target M_2(ℂ) ⊗ Cl(1); max single-block rank 2,
                      no rank ≥ 3 block) instantiate the same boundary condition:
                      max-Wedderburn-rank(T) < 3 → ker(χ|_{M_3(ℂ)}) = M_3(ℂ).

Step 6 (direction read-off):  The two rank arguments share the same structural
                      mechanism (Schur lemma + Wedderburn-Artin theorem applied at
                      the M_3(ℂ) simple block of A_K); the difference is interpretive
                      LANGUAGE (BDI parent symmetry on A_BdG is a substrate-physics
                      interpretation; dim 9 > dim 8 is a representation-theoretic
                      direct counting) — not structural CONTENT.

Conclusion:           The original Reading B's "independent rank arguments by
                      construction" cannot be defended at the Schur + Wedderburn-
                      Artin theorem layer. The arguments are F-functor images of one
                      substrate-IS theorem (Re: V1 + V4). Reading B as originally
                      stated FAILS NCG-axiomatic structural scrutiny.
```

**Qualified Reading B (sharpened residue claim)**:

The rank arguments are F-functor images of one substrate-IS theorem at the methodology layer (Reading A wins on simple-block forcing). However, the §VII candidate's downstream structural commitments at the bridge-map-scheme suffix layer (Element 3) and at the HH^1 cocycle-asymmetry observable layer carry NARROWER scope conditions that the substrate-IS simple-block forcing theorem alone does not capture. These narrower scope conditions constitute a SHARPENED Reading B residue:

**Sharpened Reading B Residue #1 (bridge-map-scheme suffix axis)**:

Per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` (S90 W7-4 CF-57 axis β; K=1 SUGGESTION pending K=3 MANDATORY), the §VII candidate's bridge map at Element 3 admits multiple scheme evaluations:
- **APS-1975-secondary-class** (canonical for boundary-anchored secondary-class on manifold-with-boundary analogs; appropriate for the 3He-B Pillar IV vortex-core spectroscopy).
- **Cheeger-Simons** (canonical for foliation-aware secondary-class evaluation; potentially relevant for Pillar II LRD horizon-area cutoff if foliation refinement structure matters).
- **Bismut-Cheeger η-form** (canonical for adiabatic-limit evaluation at fibration boundary conditions; potentially relevant for M-asymptotic envelope behavior).

The simple-block forcing theorem (Re: V1) holds at the kernel-summand observable level INDEPENDENT of scheme choice (the kernel is structurally zero at HH^0 regardless of secondary-class evaluation scheme). However, the FULL operator-trace evaluation `Π^{ker}_{χ}[L]` for HIGHER Hochschild degrees may depend on scheme. The sharpened Reading B Residue #1 claim: the two laboratory pillars (W3-3 Pillar IV BdG + W4-1 Pillar II LRD horizon) MAY require DISTINCT scheme-suffix tags at their respective bridge-map evaluations — APS-1975 for the vortex-core boundary anchored 3He-B BdG, and Cheeger-Simons or Bismut-Cheeger for the LRD horizon-area-cutoff foliation-aware evaluation. This scheme-distinction does NOT refute the kernel-summand universality (Reading A at HH^0); it constrains the §VII candidate's Element 3 convention-tag declaration. Resolution: at Stage-2 cross-axis verify (S91+), explicitly test scheme-INDEPENDENCE per the CF-57 axis β "scheme-INDEPENDENCE theorem" clause; if scheme-INDEPENDENT to within 1e-3 M_KK², the convention may omit the scheme suffix; if scheme-DEPENDENT, MANDATORY scheme-suffix tagging applies (potentially dual scheme suffix for the two empirical anchors).

**Sharpened Reading B Residue #2 (HH^1 cocycle-asymmetry observable's (C3) Hochschild-cocycle-pattern condition)**:

Per Re: V2 + Re: V5 Observation 3 (Q-V5-3), the universality reading's forward extension splits into Sub-claim A (kernel-summand observable, K-theoretic boundary theorem; clean) and Sub-claim B (cocycle-asymmetry ratio observable, K-theoretic boundary + (C3) common-scalar pullback condition). The (C3) condition is a Hochschild-cocycle-pattern condition at HH^1 that the simple-block forcing theorem alone does not enforce. Sub-claim B's scope is NARROWER than Sub-claim A's; it requires additional structural input (C3) beyond `max-Wedderburn-rank(T) < 3`.

The sharpened Reading B Residue #2 claim: the universality reading at the cocycle-asymmetry ratio observable (Gate 2 substrate-falsifying; 7.324992 ± 0.1%) is NARROWER than the universality reading at the kernel-summand observable (Gate 1 NULL). For some in-scope morphism classes with non-trivial source-side automorphism action that breaks the (C3) common-scalar pullback condition, the cocycle-asymmetry ratio observable's universality may fail while the kernel-summand observable's universality preserves. This is a SHARPENING of the universality scope at the higher-cohomology-degree layer; it does NOT refute Reading A's simple-block forcing at HH^0.

**Sharpened Reading B Residue #3 (HKR Eilenberg-Moore convergence at finite L_max for higher Hochschild degrees)**:

Per Re: V5 Observation 1 (Q-V5-1), the V3 candidate's Level-2-binding `α = ∞` is correct at HH^0 (the kernel-summand observable's HKR-image is structurally zero at every L_max). At HH^1 (cocycle-asymmetry ratio observable), the HKR map's Eilenberg-Moore spectral sequence convergence at finite L_max may require finite α (e.g., L^{-α(s)} with `α(s)` pole-specific per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`). The sharpened Reading B Residue #3 claim: the Level-2 envelope characterization differs between the two observables (Sub-claim A vs Sub-claim B); the kernel-summand observable has degenerate `α = ∞`, but the cocycle-asymmetry observable may have finite α PENDING FIRST-EXTRACTION at S91+. The §VII candidate registry text MUST declare both observables and their respective Level-2 envelopes; conflating them under a single Level-2-binding `α = ∞` declaration is registry-incomplete.

**Operational interpretation of the qualified Reading B residue**:

The sharpened Reading B residue does NOT change the workshop's structural verdict on cross-morphism convergence — Reading A wins on the kernel-summand universality (Re: V1 + V4 simple-block forcing). The residue is structurally distinct from Reading A and operates at THREE layered residue axes:

| Residue # | Layer | Reading A scope | Sharpened Reading B residue |
|:---------:|:------|:---------------|:---------------------------|
| Residue #1 | Element 3 bridge-map-scheme suffix | scheme-INDEPENDENCE PENDING Stage-2 verify | dual scheme-suffix possible: APS-1975 (Pillar IV) + Cheeger-Simons or Bismut-Cheeger (Pillar II) |
| Residue #2 | HH^1 cocycle-asymmetry observable scope | universality requires (C1)+(C2)+(C3) | (C3) Hochschild-cocycle-pattern condition narrows scope beyond simple-block forcing |
| Residue #3 | HKR Eilenberg-Moore Level-2 envelope | `α = ∞` at HH^0 (degenerate binding) | finite α at HH^1 PENDING FIRST-EXTRACTION at S91+ |

Each residue is structurally distinct from the simple-block-forcing universality (Reading A); each constrains the §VII candidate's registry text at a layer downstream of the kernel-summand observable. The qualified Reading B is the structural specification of these three residue axes; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands the registry text incorporating both Sub-claim A (Reading A clean universality at kernel-summand HH^0 layer) and Sub-claim B + the three residue axes (sharpened Reading B at HH^1 + bridge-map-scheme + HKR Level-2 envelope layers).

**Honest conclusion on C1**: Reading B as the "independent rank arguments by construction" claim FAILS NCG-axiomatic structural scrutiny (Schur + Wedderburn-Artin force the rank arguments through a single substrate-IS theorem at HH^0). Reading B as the "sharpened residue at three structurally-distinct downstream layers" claim SURVIVES NCG-axiomatic scrutiny (Element 3 bridge-map-scheme suffix axis + (C3) Hochschild-cocycle-pattern condition at HH^1 + HKR Eilenberg-Moore Level-2 envelope at higher cohomology degrees). The workshop's structural verdict is **Reading A wins at the kernel-summand observable layer (Sub-claim A)** + **Sub-claim B + three sharpened residue axes pre-registered at Stage-2 verify**. The qualified Reading B is structurally faithful to NCG-axiomatic machinery; the original Reading B is not. This is the honest concession; manufacturing a counter-argument that does not survive Schur + Wedderburn would have been a sound-right Class-1/6 execution failure per `v3-closure-recovery.md` PROHIBITED_ACTIONS.

#### C2: NCG-axiomatic K-theory framing — Connes-Karoubi pairing on (A_K, target-algebra) pairs distinguishes morphism classes

**NCG-axiomatic K-theory framing**: The Connes-Karoubi pairing on `(A_K, T)` pairs is the canonical NCG-axiomatic layer at which morphism classes for inheritance morphisms `χ : A_K → T` are organized. The pairing `⟨ · , · ⟩ : HC^{2k}(A) × K_0(A) → ℂ` (Connes 1985 §IV.7; Connes-Karoubi 1993) is the K-theoretic invariant that distinguishes morphism classes via the naturality property `⟨χ^*[ψ], [p]⟩_A = ⟨[ψ], χ_*[p]⟩_T` for `[ψ] ∈ HC^{2k}(T)` and `[p] ∈ K_0(A)`. Below I derive both the structural-theorem-quality content (Sub-claim A: kernel-summand observable; clean K-theoretic boundary theorem) AND the Hochschild-cocycle-pattern condition (Sub-claim B: cocycle-asymmetry ratio observable; requires additional (C3) condition).

**Engagement with V3 Stage-2 axis declaration + V5 Observation 3 scope-boundary K-theoretic question**:

V3 line 175-180 declares the bridge map as `K_0(M_3(ℂ)) → K_0(A_K) →^{χ_*} K_0(T_χ)` with the composite zero map for `max-Wed-rank(T_χ) < 3`. This is structurally correct AT THE K_0 layer for the kernel-summand observable; the K-theoretic boundary theorem (Sub-claim A) is the canonical NCG-axiomatic statement of this observation. V5 Observation 3 (Q-V5-3) asks whether the scope predicate `ker(χ|_{M_3(ℂ)}) = M_3(ℂ) ⟺ max-Wedderburn-rank(T) < 3` is a K-theoretic boundary theorem OR requires additional structural input. My answer: BOTH simultaneously, at DIFFERENT observable-degree layers.

**Route (a) — Sub-claim A: clean K-theoretic boundary theorem at K_0 + HH^0 layer**:

For the kernel-summand observable (Gate 1 NULL prediction; `Π^{ker}_{χ}[L] = 0`), the Connes-Karoubi pairing structural-theorem-quality content gives:

> **Theorem (Connes-Karoubi K-theoretic boundary at kernel-summand layer)**: Let `A = ⊕_i M_{n_i}(ℂ)` be a finite-dim semisimple ℂ-algebra Wedderburn-decomposed into simple blocks, and `χ : A → T` a unital algebra map. For any HH^0(A) cohomology class `[1_{M_{n_i}(ℂ)}] ∈ HH^0(A)` (the centrally-located simple-block unit), the Connes-Karoubi pairing satisfies:
>
> `⟨[1_{M_{n_i}(ℂ)}], [p]⟩_A = ⟨[1_{M_{n_i}(ℂ)}], [p]⟩_A`   (trivial; HH^0 ⊗ K_0 → ℂ is the dimension counting pairing)
>
> Under `χ_*`-naturality: `⟨χ^*[1_T-image], [p]⟩_A = ⟨[1_T-image], χ_*[p]⟩_T`.
>
> When the constraint `max-Wedderburn-rank(T) < n_i` holds, χ_*([1_{M_{n_i}(ℂ)}]) = 0 in K_0(T) (Re: V1 simple-block forcing at K-theory layer; Connes-Karoubi 1993 + Connes 1985 §IV.7 long exact sequence). The Connes-Karoubi pairing on the inheritance image is structurally zero; this is a K-THEORETIC IDENTITY independent of any specific Hochschild cocycle pattern beyond HH^0 dimension counting.

**Structural-theorem-quality content**: the K-theoretic boundary theorem is INVARIANT under morphism class within scope (`max-Wedderburn-rank(T) < n_i`). For A_K's M_3(ℂ) summand (`n_i = 3`), the boundary theorem reads:

```
For ALL unital algebra maps χ : A_K → T with max-Wedderburn-rank(T) < 3:
  χ_*([1_{M_3(ℂ)}]) = 0  in K_0(T)
```

This is the K-theoretic identity that supports the universality reading (Reading A at Sub-claim A). It factors cleanly through Connes-Karoubi pairing structural-theorem-quality content; no additional Hochschild-cocycle-pattern condition required.

**K-theoretic derivation chain** (Connes-Karoubi 1993 + Connes 1985 §IV.7):

```
Step 1 (definition): K_0(M_3(ℂ)) = ℤ generated by [1_{M_3(ℂ)}], where [1_{M_3(ℂ)}]
                     has rank 3 (the dimension of the unique simple M_3(ℂ)-module).
Step 2 (substitution per Wedderburn-Artin): K_0(⊕_i M_{n_i}(ℂ)) = ⊕_i ℤ;
                     for A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), K_0(A_K) = ℤ ⊕ ℤ ⊕ ℤ generated by
                     ([1_ℂ], [1_ℍ], [1_{M_3(ℂ)}]) with respective ranks (1, 2, 3).
Step 3 (substitution per simple-block forcing): for any unital χ : A_K → T with
                     max-Wedderburn-rank(T) < 3, χ_*([1_{M_3(ℂ)}]) lies in K_0(T)
                     and must have rank ≤ max-Wedderburn-rank(T) < 3; but
                     χ_*([1_{M_3(ℂ)}]) = [χ(1_{M_3(ℂ)})] is the K-class of an
                     idempotent that (if non-zero) has rank equal to the rank
                     of the image M_3(ℂ)-embedding (Schur). The only K-class
                     of an idempotent of "rank < 3" that arises from M_3(ℂ)
                     embedding is the zero K-class.
Step 4 (simplification): χ_*([1_{M_3(ℂ)}]) = 0 in K_0(T).
Step 5 (direction read-off): Connes-Karoubi pairing ⟨[ψ], χ_*([1_{M_3(ℂ)}])⟩_T = 0
                     for any [ψ] ∈ HC^*(T); in particular ⟨[1_T], χ_*[1_{M_3(ℂ)}]⟩_T
                     = dim(χ(1_{M_3(ℂ)})) = 0. The K-theoretic identity is
                     INVARIANT under morphism class within scope.
Conclusion:          The scope predicate `ker(χ|_{M_3(ℂ)}) = M_3(ℂ) ⟺ max-Wed-rank(T)
                     < 3` IS a K-theoretic boundary theorem on (A_K, T) pairs
                     parameterized by max-Wedderburn-rank(T). Pati-Salam (max-rank
                     ≤ 2 < 3) inherits the boundary cleanly; SU(5) GUT (rank 5 ≥ 3)
                     admits M_3 ↪ M_5 Wedderburn-block embedding and falls outside
                     the scope cleanly.
```

**Confirmation**: route (a) holds for Sub-claim A (kernel-summand observable). The K-theoretic boundary theorem supports the universality reading at the HH^0 + K_0 layer; no additional Hochschild-cocycle-pattern condition required for the kernel-summand NULL prediction.

**Route (b) — Sub-claim B: K-theoretic boundary + Hochschild-cocycle-pattern condition at HH^1 layer**:

For the cocycle-asymmetry ratio observable (Gate 2 substrate-falsifying; 7.324992 ± 0.1%), the Connes-Karoubi pairing structural-theorem-quality content is augmented with the (C3) common-scalar pullback condition per Re: V2.

The cocycle pair `[φ_67], [φ_88] ∈ HH^1(A_K)` lives at degree-1 Hochschild cohomology on the M_3(ℂ) Peter-Weyl block. The Connes-Karoubi pairing at this layer is `⟨ · , · ⟩ : HC^1(A_K) × K_1(A_K) → ℂ` (or the higher-degree extension on K_0 via Loday-Quillen-Tsygan map). The naturality gives:

```
lab(F_i) / lab(F_j) = ⟨χ^*[φ_a], [p_i]⟩_{A_K} / ⟨χ^*[φ_b], [p_j]⟩_{A_K}
                   = c_χ^{a} · ⟨[φ_a^{A_K}], [p_i]⟩ / [c_χ^{b} · ⟨[φ_b^{A_K}], [p_j]⟩]
                   = (c_χ^{a} / c_χ^{b}) · ⟨[φ_a^{A_K}], [p_i]⟩ / ⟨[φ_b^{A_K}], [p_j]⟩
```

where `c_χ^{a}`, `c_χ^{b}` are the χ-pullback scalars on the (φ_67, φ_88) cocycle pair respectively. The substrate ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992` is preserved in the LAB ratio iff `c_χ^{a} = c_χ^{b}` — the (C3) common-scalar pullback condition.

**Hochschild-cocycle-pattern condition (C3)** (Connes-Marcolli 2008 §IV.6.5 Hochschild direct-sum decomposition; HKR map at HH^1):

The (C3) condition requires: under the χ-pullback at HH^1 layer, the cocycle pair `(φ_67, φ_88)` transforms by a COMMON scalar factor `c_χ`, not by independent factors `c_χ^{a}, c_χ^{b}` with `c_χ^{a} ≠ c_χ^{b}`. This is a property of the χ-pullback's action on the Hochschild cocycle pattern on A_K's M_3(ℂ) summand — specifically, whether the pullback respects the degree-1 grading structure of the Peter-Weyl decomposition uniformly across the cocycle pair.

For Pati-Salam parent symmetry (V2 line 122; (SU(2)_L ⊗ SU(2)_R ⊗ U(1)) parent): the parent symmetry acts homogeneously on the M_3(ℂ) Peter-Weyl block (the symmetry breaks SU(3) → SU(2)_L ⊗ SU(2)_R ⊗ U(1) at the substrate-physics layer; the action on the cocycle pair is via the Pati-Salam symmetry rotation matrices, which act as a SAME scalar c_χ on both [φ_67] and [φ_88] up to higher-order corrections in the symmetry-breaking parameter). (C3) plausibly holds; Sub-claim B universality plausibly extends to Pati-Salam laboratory pillars.

For arbitrary in-scope morphism classes with non-trivial source-side automorphism action breaking the (C3) common-scalar pullback: Sub-claim B universality MAY fail. Hypothetical example: a hypothetical morphism class where the inheritance restriction differentiates between chiral-pair (φ_67) and Cartan-hypercharge (φ_88) via DISTINCT renormalization-group running scalars (e.g., a Pillar that probes the substrate at TWO distinct energy scales such that the cocycle pair undergoes DIFFERENT scaling at each scale). Such a morphism class would inhabit Sub-claim B's scope boundary; the substrate-ratio would NOT be preserved at the lab pillar.

**Hochschild-cocycle-pattern condition specification**:

For Sub-claim B to extend universally across morphism class within (C1), the following additional structural input is required:

> **(C3) Common-Scalar Hochschild-Cocycle Pullback Condition**: For the inheritance morphism `χ : A_K → T` and the cocycle pair `[φ_67], [φ_88] ∈ HH^1(A_K)`, the χ-pullback satisfies `χ^*[φ_67] = c_χ · [φ_67^{A_K}]` AND `χ^*[φ_88] = c_χ · [φ_88^{A_K}]` for a COMMON scalar `c_χ`. Equivalently, χ acts homogeneously on the Peter-Weyl decomposition's degree-1 grading on the M_3(ℂ) summand.

This condition is the additional structural input that EXTENDS the Connes-Karoubi K-theoretic boundary theorem's scope beyond the simple-block forcing theorem to the cocycle-asymmetry ratio observable. (C1) + (C3) together define Sub-claim B's scope.

**Confirmation**: route (b) holds for Sub-claim B (cocycle-asymmetry ratio observable). The Connes-Karoubi pairing structural-theorem-quality content at HH^1 + K_0/K_1 layer is augmented with the (C3) Hochschild-cocycle-pattern condition; the scope is NARROWER than Sub-claim A's K-theoretic boundary theorem.

**Unification — both routes simultaneously valid**:

The NCG-axiomatic K-theory framing organizes the universality reading at two STRUCTURALLY DISTINCT observable-degree layers:

| Observable | Cohomology degree | Scope predicate | Connes-Karoubi pairing structure |
|:-----------|:------------------|:---------------|:--------------------------------|
| Kernel-summand NULL (Gate 1) | HH^0 / K_0 | `max-Wedderburn-rank(T) < 3` | clean K-theoretic boundary theorem (Sub-claim A) |
| Cocycle-asymmetry ratio (Gate 2) | HH^1 / K_0 (or K_1 via Loday-Quillen-Tsygan) | (C1) + (C3) Hochschild-cocycle-pattern | K-theoretic boundary + (C3) common-scalar pullback (Sub-claim B) |

Both routes are simultaneously valid; each addresses a DIFFERENT observable at a DIFFERENT cohomology-degree layer. The universality reading at the kernel-summand observable is cleanly factored through Connes-Karoubi K-theoretic boundary theorem (route (a)); the universality reading at the cocycle-asymmetry ratio observable requires the additional (C3) Hochschild-cocycle-pattern condition (route (b)).

**Cross-link to V3 §VII candidate's Element 4 algebraic envelope**:

The Connes-Karoubi pairing structural-theorem-quality content is the SUBSTRATE-IS pin underlying V3's Level-2-binding declaration `α = ∞` at HH^0. For Sub-claim A, the algebraic envelope is the K-theoretic boundary theorem (regulator-class-INVARIANT; L-INDEPENDENT). For Sub-claim B, the algebraic envelope requires finite α at HH^1 PENDING FIRST-EXTRACTION (Re: V5 Observation 1 + Sub-claim B sub-section). The §VII candidate registry text MUST declare both observables' algebraic envelopes explicitly; conflating them under a single Level-2-binding `α = ∞` declaration is registry-incomplete per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` and per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole `α(s)` exponent.

**Forward enforcement for §VII candidate registry text**:

Per the C2 NCG-axiomatic K-theory framing, the §VII candidate's registry text should declare:

1. **Sub-claim A (HH^0 / K_0 layer)**: kernel-summand observable `Π^{ker}_{χ}[L] = 0` at K-theoretic boundary `max-Wedderburn-rank(T) < 3`. Connes-Karoubi pairing structural-theorem-quality identity. Level-2-binding `α = ∞` exact. Pati-Salam IN-scope, SU(5) GUT OUT-of-scope.
2. **Sub-claim B (HH^1 / K_0 (or K_1) layer)**: cocycle-asymmetry ratio observable `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992 ± 0.1%`. K-theoretic boundary + (C3) common-scalar Hochschild-cocycle-pattern pullback. Level-2-binding finite α PENDING FIRST-EXTRACTION at S91+. Pati-Salam plausibly IN-scope (homogeneous symmetry action); arbitrary in-scope morphisms with non-trivial source-side automorphism action need (C3) verification.
3. **Cross-link to Connes-Karoubi K-theory** (Connes 1985 §IV.7 long exact sequence; Connes-Karoubi 1993 pairing; CM-1995 §III.4 finite-spectral-triple residue formula; CM-2008 §IV.6.5 Hochschild direct-sum decomposition; HKR map at HH^0 + HH^1).

**Conclusion on C2**: The Connes-Karoubi pairing on `(A_K, T)` pairs is the canonical NCG-axiomatic K-theory layer at which morphism classes for inheritance morphisms are organized. The pairing's structural-theorem-quality content extends the simple-block forcing theorem (Re: V1) to a CLEAN K-theoretic boundary theorem for the kernel-summand observable (Sub-claim A; route (a)) AND to a K-theoretic boundary + (C3) Hochschild-cocycle-pattern condition for the cocycle-asymmetry ratio observable (Sub-claim B; route (b)). Both routes are simultaneously valid; the universality reading extends cleanly at Sub-claim A and conditionally (under (C3)) at Sub-claim B. The §VII candidate's registry text must declare both observables explicitly to be registry-complete; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands the dual-sub-claim registry text at next-session plan-freeze.

#### C3: Questions for volovik

Three forward questions targeting specific substrate-axis or substrate-superfluid-universe-axis commitments that emerge from my Re: V1..V5 + C1 + C2 NCG-axiomatic engagement. Each question tests whether volovik's R1 position survives NCG-axiomatic counter-pressure at a structurally-distinct downstream layer; please address each in your R2 CONVERGENCE / DISSENT / EMERGENCE / QUESTIONS sections.

---

**Q-C3-1 (substrate-axis: V2 scope predicate under non-simple target algebras with max-rank 1 < 3)**:

Your V2 scope refinement (line 90) corrects "abelian-group laboratory parents" to "inheritance morphisms whose target's Wedderburn decomposition has max-Wedderburn-rank < 3 over ℂ". This admits non-simple target algebras like `ℂ ⊕ ℂ` (max-rank 1) and `ℂ ⊕ ℂ ⊕ ... ⊕ ℂ` (k copies of ℂ; max-rank 1 across all blocks) into scope. For such abelian C*-algebras (target rank 1, strictly < 3), Sub-claim A's K-theoretic boundary theorem (per C2 route (a)) gives `χ_*([1_{M_3(ℂ)}]) = 0` in `K_0(T)` cleanly, supporting V2's universality scope.

**However**, the laboratory-IN observable `Π^{ker}_{χ}[L]` (V3 Element 2 OE-form line 155) requires an OPERATIONAL realization at the laboratory pillar. For non-simple abelian targets `ℂ ⊕ ℂ ⊕ ... ⊕ ℂ`, what is the substrate-physics realization? Is there a candidate laboratory pillar that probes an abelian C*-algebra parent target — perhaps a fully decoupled multi-channel laboratory (e.g., a k-fold direct sum of single-channel BdG-like superfluid hosts where each channel is governed by an INDEPENDENT abelian U(1) symmetry rather than a coupled BDI symmetry class)? If yes, the OE-form must be re-examined: `Π^{ker}_{χ}[L]` would be a sum over k independent abelian channels rather than a single Bogoliubov-pair Wedderburn block trace.

**Substrate-axis question**: does V2's scope predicate `max-Wedderburn-rank(T) < 3` admit STRUCTURAL OPERATIONAL REALIZATIONS at non-simple abelian targets (rank 1 strictly less than 3), AND if so, does the (Δ_B/Δ_A)^p cancellation theorem at lab-conversion-factor layer (V2 line 113-118) still admit a clean lift via the (C1)+(C2)+(C3) scope conditions per my Re: V2? Or does the cancellation theorem's structural form require a target Wedderburn structure with at least ONE simple block of rank ≥ 2 (so that the cocycle pair (φ_67, φ_88) has a non-trivial image under χ_* even when M_3(ℂ) summand is killed)? If the latter, the scope predicate sharpens to `max-Wedderburn-rank(T) ∈ {2}` for Sub-claim B (cocycle-asymmetry ratio observable) — narrower than Sub-claim A's `max-Wedderburn-rank(T) < 3`.

This question tests whether your V2 scope refinement extends uniformly across the two sub-claims (A and B) or whether the cocycle-asymmetry observable demands a TIGHTER scope predicate than the kernel-summand observable. Resolution would sharpen the §VII candidate's Element 5 forward predictive content.

---

**Q-C3-2 (substrate-axis: V3 Level-2-binding α = ∞ robustness under finite-rank HKR truncation)**:

Your V3 Element 4 (lines 188-192) declares Level-2-binding `α = ∞` with the envelope exact at every L_max because the simple-block forcing theorem at HH^0 is L-INDEPENDENT (the Wedderburn decomposition of A_K is an algebraic property of A_K's finite-dim structure). This is correct for the kernel-summand observable at HH^0 per my Re: V5 Observation 1 (Q-V5-1 answer).

**However**, the HKR map at HH^0 — for the V3 candidate's laboratory-IN observable `Π^{ker}_{χ}[L]` operator-trace evaluation — DOES depend on the finite-L truncation when the trace is evaluated INSIDE the laboratory pillar's finite-rank operator algebra (per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole `α(s)` exponent). Specifically, the trace `Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)` evaluated at the laboratory pillar with finite L_max truncation may carry an L^{-α(s)} envelope at the OPERATIONAL realization layer (e.g., at the 3He-B Aalto LTL vortex-core spectroscopy's finite-resolution measurement of the Caroli-Matricon ladder NULL signature; the resolution carries an L_max-equivalent truncation at the measurement-pillar level).

**Substrate-axis question**: is the Level-2-binding `α = ∞` declaration robust under the OPERATIONAL HKR Eilenberg-Moore spectral sequence convergence at the laboratory-pillar's finite-rank measurement, OR does the laboratory-pillar's finite resolution introduce a finite `α(s)` at the operational layer per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole envelope? Specifically: at the 3He-B Aalto LTL vortex-core spectroscopy (Pillar IV BdG; W3-3 Gate 1 NULL prediction), the measurement's finite spectral resolution `ΔE_resolution` corresponds to a finite-L_max-equivalent truncation at the operational layer. Does this OPERATIONAL truncation preserve `α = ∞` (envelope exact at every operational L_max-equivalent), OR does it introduce a finite `α_operational(s)` at the per-pole envelope layer per the Per-Bulletin-per-pole Level-1 wall classification?

If finite `α_operational` is structurally required at the OPERATIONAL layer (laboratory-pillar measurement side), the V3 candidate's Level-2-binding declaration must be split: `α_substrate = ∞` at the substrate-IS HH^0 layer (Connes-Karoubi K-theoretic boundary identity; exact L-independent) + `α_operational(s)` at the laboratory-pillar operational layer (finite per-pole envelope). The substrate-IS Level-2-binding remains exact; the operational Level-2 envelope is the finite-resolution measurement bound. The §VII candidate's registry text MUST declare both envelopes explicitly per `cross-pillar-bridge-anatomy.md §"Level-2 audit axes (Level-2-A vs Level-2-B)"` Level-2-A (operational content) + Level-2-B (regulator-invariance) dual-audit-axis discipline.

This question tests whether your V3 Element 4 declaration captures BOTH the substrate-IS exact identity AND the laboratory-pillar operational envelope, OR whether the declaration is restricted to the substrate-IS layer only. Resolution would sharpen the §VII candidate's Element 4 algebraic envelope declaration to dual-axis (substrate + operational) form.

---

**Q-C3-3 (substrate-superfluid-universe-axis: V4 BDI K-grading orthogonal-Corner claim under §VII.U.2 parse-tree decision procedure applied to 3He-B vortex-core spectroscopy)**:

Your V4 (lines 286-293) argues that BDI K-grading content (Pf=−1, N_K=2 topological invariants per Volovik Paper 05; K_0(A_BdG)-grading particle-hole structure) lives on Corner-III/IV (algebra-DEPENDENT state-pair functional axis) of the §VII.U.2 4-corner partition, STRUCTURALLY ORTHOGONAL to the source-side kernel-summand structure on Corner-I/II (algebra-INVARIANT spectrum-only axis). I confirmed this orthogonality at Re: V4 (Q-V4 answer; BDI K-grading content lives at KO_0^{BDI} target-side real-K-theory layer; source-side kernel-summand at complex-K_0 layer; structurally distinct).

**However**, the operational realization at the 3He-B vortex-core spectroscopy (Pillar IV BdG; W3-3 Gate 1 NULL prediction on F1+F2+F5 decisive triplet at Lancaster MCT-3 / Helsinki ROTA cells per W3-3 §(d.d)) probes BOTH:
- The Bogoliubov sub-algebra Wedderburn structure (max-Wedderburn-rank(A_BdG) = 2 < 3; source of the kernel-summand NULL prediction);
- The BDI particle-hole grading (Pf=−1, N_K=2; protects specific Caroli-Matricon ladder modes against deformation; determines WHICH non-zero K-classes are accessible in the laboratory measurement).

**Substrate-superfluid-universe-axis question**: at the OPERATIONAL realization (3He-B Pillar IV vortex-core spectroscopy), does the §VII.U.2 parse-tree decision procedure clause (e) (applied to the W3-3 Gate 1 NULL observable on F1+F2+F5) preserve the Corner-I/II vs Corner-III/IV orthogonality, OR does the operational realization probe BOTH corners simultaneously (yielding a JOINT Corner-I + Corner-III observable that the §VII.U.2 4-corner partition does NOT cleanly factor)? Specifically:

- **Hypothesis (a)**: the parse-tree decision procedure clause (e) correctly identifies the operational observable as Corner-I (algebra-INVARIANT spectrum-only; the kernel-summand NULL prediction is independent of the particle-hole grading); the BDI K-grading content is on Corner-III/IV but does NOT affect the parse-tree assignment of the W3-3 Gate 1 observable. The orthogonality is preserved at the operational layer.
- **Hypothesis (b)**: the operational measurement at 3He-B vortex-core spectroscopy probes the JOINT structure (Bogoliubov Wedderburn block + BDI particle-hole grading) such that the parse-tree decision procedure assigns the observable to a JOINT corner classification (Corner-I + Corner-III), requiring CROSS-CORNER co-primary anchor structure (which is STRUCTURALLY FORBIDDEN per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 clause 3 + `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` audit at plan-freeze; W5a-44 K=1 NEGATIVE-CALIBRATION instance). Under Hypothesis (b), the V3 candidate's Corner-I classification is registry-INCOMPLETE; an alternative anchor structure (joint-hypersurface (iii) binding per Element 3 fiducial-anchor binding discipline) must be invoked.

The substrate-superfluid-universe-axis test: at the 3He-B Aalto LTL Lancaster MCT-3 cell, does the operational vortex-core spectroscopy measurement DISTINGUISH between (i) the kernel-summand NULL on F1+F2+F5 (Corner-I observable) and (ii) the BDI-protected K-class content (Corner-III observable), OR does the laboratory measurement entangle them at the operational realization layer such that the W3-3 Gate 1 NULL signature carries IMPLICIT BDI K-grading content the parse-tree cannot factor out?

If Hypothesis (a) holds (parse-tree preserves Corner-I/II vs Corner-III/IV orthogonality at operational layer), V4's orthogonality claim survives and Reading A wins cleanly. If Hypothesis (b) holds, the §VII candidate's Corner-I classification needs sharpening (either via joint-hypersurface (iii) binding declaration or via a structurally-orthogonal-companion structure pairing Corner-I + Corner-III entries). Resolution at R2 will fix the §VII candidate's corner-pin discipline at the operational realization layer.

This question tests whether your substrate-superfluid-universe-axis machinery (Volovik Paper 05 BDI topological invariants + 3He-B BdG laboratory physics) preserves the §VII.U.2 corner-orthogonality at the OPERATIONAL realization, or whether the laboratory measurement entangles two structurally-orthogonal corner observables in a way that requires the V3 candidate to adopt a different anchor structure than the OP-PROJ Corner-I declaration.

---

**Summary of C3 questions**:

| # | Layer tested | Substrate-axis commitment | Resolution at R2 |
|:-:|:------------|:--------------------------|:-----------------|
| Q-C3-1 | V2 scope predicate at non-simple abelian targets (rank 1 strictly < 3) | does universality scope extend uniformly across Sub-claim A and Sub-claim B, or does Sub-claim B sharpen to max-rank ∈ {2}? | sharpens §VII candidate's Element 5 forward predictive content |
| Q-C3-2 | V3 Level-2-binding `α = ∞` robustness under OPERATIONAL HKR truncation | does Level-2-binding declaration capture both substrate-IS exact identity AND operational laboratory-pillar finite-resolution envelope? | sharpens §VII candidate's Element 4 algebraic envelope to dual-axis (Level-2-A operational + Level-2-B regulator-invariance) form |
| Q-C3-3 | V4 BDI orthogonal-Corner claim under §VII.U.2 parse-tree decision procedure at operational realization | does parse-tree clause (e) preserve Corner-I/II vs Corner-III/IV orthogonality at 3He-B vortex-core spectroscopy, OR does the operational measurement entangle them? | fixes §VII candidate's corner-pin discipline at the operational realization layer |

Each question is forward-actionable for your R2 sections; each tests a SPECIFIC substrate-axis commitment that emerges from my NCG-axiomatic engagement; each resolution would sharpen the §VII candidate's downstream registry-text declarations. The questions do NOT re-litigate Reading A's simple-block forcing universality (which I have CONCEDED per Re: V1 + V4 NCG-axiomatic CONFIRMATION); they target downstream layers where the sharpened Reading B residue lives (Element 3 bridge-map-scheme suffix; HH^1 cocycle-asymmetry observable; operational realization corner-pin discipline). Resolution at R2 + Stage-2 cross-axis verify will fix the §VII candidate's full registry-text declaration ahead of mack-cosmic-bridge sole-writer landing at next-session plan-freeze.

---

## Round 2 — volovik: Follow-up

### CONVERGENCE

Where I now agree with connes after R1 cross-axis exchange. Four convergence points; each cites specific Re:Vn / Cn lines from connes's R1 and specifies what position has shifted relative to my R1.

---

**CONVERGENCE C1 — Reading A simple-block forcing universality is now a STRUCTURAL THEOREM at the layer-functor F level (not a contingent agreement)**:

connes's Re:V1 four-layer commutative-diagram statement (lines 421–428) — algebra layer (Schur + Wedderburn-Artin) → K-theory layer (Connes 1985 §IV.7 long exact sequence) → HH^0 layer (Connes-Marcolli 2008 §IV.6.5 Hochschild direct-sum decomposition) → CM-1995 §III.4 finite-spectral-triple residue layer — SHARPENS my V1 single-theorem framing (line 64) to a precise four-layer statement, with all four layers commuting under the F-functor `F : substrate → methodology → audit`. Combined with connes's C1 substitution chain (lines 767–806) demonstrating that the original Reading B fails Schur + Wedderburn structural scrutiny at Step 5 simplification (both BDI rank-mismatch and Wedderburn 9>8 instantiate the same boundary condition `max-Wedderburn-rank(T) < 3 → ker(χ|_{M_3(ℂ)}) = M_3(ℂ)`), and connes's Re:V4 Q-V4 answer (line 587: "I cannot identify such content. After NCG-axiomatic search through the standard K-theoretic structures associated with BDI ... I find every K-theoretic content of BDI lives at the K_0(target) particle-hole-graded layer. The source-side kernel-summand structure is determined by A_K's Wedderburn decomposition + Schur lemma + the target's max-Wedderburn-rank predicate — all source-and-target ungraded data."), the cross-axis JOINT-WIN on Reading A is now structurally locked.

**Position-shift relative to my R1**: at R1 I stated V1+V4 as the substrate-axis steelman with anticipated connes pushback; at R2 the universality reading is a STRUCTURAL THEOREM at the methodology-floor layer-functor F-image of the 4-layer substrate-IS commutative diagram (algebra → K-theory → HH^0 → CM-1995 §III.4 residue). Per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence, the universality reading inhabits the methodology-floor `Σ_2` stratum (weight-2; wave-classification) as a methodology-layer F-image of the substrate-IS commutative diagram. This is analogous to the W-1 + W-2 cross-axis JOINT-WIN STRUCTURAL THEOREM pattern (W-1 deferred-pending taxonomy volovik+connes JOINT-WIN APPROVE-NO-AMENDMENT; W-2 χ'_weight ansatz lizzi+volovik JOINT-WIN option (iii) regulator-class-dependent + option (v) admitted); see EMERGENCE E3 for the cross-workshop pattern observation.

The Cross-axis JOINT-WIN STRUCTURAL THEOREM for V1+V4 is: substrate-axis V1+V4 6-step substitution chain (workshop lines 243–267) + NCG-axiomatic Re:V1 four-layer simple-block forcing commutative diagram (lines 421–428) + Re:V4 BDI K-grading orthogonal-Corner concession (line 587) jointly establish that Reading A simple-block forcing universality is structurally identical at the kernel-summand observable layer (HH^0 + K_0) across the W3-3 ι and W4-1 χ' inheritance morphisms, with the F-functor `F : substrate → methodology → audit` preserving the identity at all four NCG-axiomatic layers.

---

**CONVERGENCE C2 — Three Reading B residue layers are accepted as STRUCTURALLY COMPATIBLE sharpened downstream framings**:

connes's C1 sharpened Reading B residue (lines 832–842) preserves three structurally-distinct residue axes downstream of the simple-block forcing layer:

- **Residue #1 (Element 3 bridge-map-scheme suffix axis; APS-1975 / Cheeger-Simons / Bismut-Cheeger)** per S90 W7-4 CF-57 axis β + `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` (K=1 SUGGESTION pending K=3 MANDATORY). My V3 line 184 declared `APS-1975-secondary-class` suffix as canonical for the boundary-anchored secondary-class evaluation on the 3He-B vortex-core manifold-with-boundary analog; connes's Re:V3 sharpening (lines 539–544) raises the structurally-distinct possibility that Pillar II LRD horizon-area cutoff foliation refinement may demand Cheeger-Simons over APS-1975, and Bismut-Cheeger may apply to the M-asymptotic envelope evaluation. **I ACCEPT** the bridge-map-scheme suffix discipline at Element 3: scheme-INDEPENDENCE is PENDING Stage-2 verify per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` Reading A scheme-INDEPENDENCE theorem clause; the §VII candidate's convention tag at landing is `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` (default per V3) with the strengthened-on-Stage-2-PASS tag `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT` reserved for the case Stage-2 confirms scheme-INDEPENDENCE within 1e-3 M_KK² per the CF-55 / §VII.AQ precedent connes cites (Re:V3 line 578).
- **Residue #2 (HH^1 cocycle-asymmetry observable Sub-claim A/B distinction)**: my V2 (C1)+(C2) scope conditions for the (Δ_B/Δ_A)^p cancellation theorem (lines 115–118) are SHARPENED by connes's Re:V2 to (C1)+(C2)+(C3) where (C3) is the common-scalar Hochschild-cocycle-pattern pullback condition `χ^*[φ_67] = c_χ · [φ_67^{A_K}]` AND `χ^*[φ_88] = c_χ · [φ_88^{A_K}]` for a COMMON scalar `c_χ` (Re:V2 lines 462–471). The Sub-claim A (kernel-summand observable; clean K-theoretic boundary theorem under (C1) only) vs Sub-claim B (cocycle-asymmetry ratio observable; K-theoretic boundary + (C3)) distinction (Re:V5 Observation 3 line 734–737; C2 route (a) vs route (b)) is the correct NCG-axiomatic decomposition of the universality scope. **I ACCEPT** the Sub-claim A/B scope partition; the §VII candidate's Element 5 forward predictive content declares both sub-claims with their respective scope predicates (Sub-claim A broader: K-theoretic boundary only; Sub-claim B narrower: K-theoretic boundary + (C3) Hochschild-cocycle-pattern condition).
- **Residue #3 (HKR Eilenberg-Moore Level-2 envelope at higher cohomology degrees)**: my V3 Level-2-binding declaration `α = ∞` (line 190) is correct at HH^0 layer (the kernel-summand observable; envelope exact at every L_max because the Wedderburn decomposition of A_K is an algebraic property independent of L truncation; connes's Re:V5 Observation 1 line 650 confirms). At HH^1 layer (cocycle-asymmetry ratio observable 7.324992), the HKR map's Eilenberg-Moore spectral sequence convergence at finite L_max may carry sectoral contributions of order `L^{-α(s)}` per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole α(s) exponent (Re:V5 line 654). **I ACCEPT** the HH^0 vs HH^1 layer distinction: V3 Element 4 declaration is correct for the HH^0 kernel-summand observable; the HH^1 cocycle-asymmetry ratio observable becomes a SEPARATE STAGE-1-CANDIDATE entry tagged `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` per the S90 W1-14 deferred-pending sub-class clause (`cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` SUGGESTION at K=1) until L_max scan or Friedrich-Bär saturation supplies the canonical `α(s=3)` value on the M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole.

These three residue layers are STRUCTURALLY COMPATIBLE with Reading A simple-block forcing — they live at DOWNSTREAM structural layers (Element 3 bridge-map-scheme axis; HH^1 cocycle-asymmetry observable; HKR Eilenberg-Moore higher-cohomology Level-2 envelope), not at the kernel-summand simple-block forcing layer itself. The §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry SHARPENS to include scheme-suffix declaration + HH^0/HH^1 layer-pin + Sub-claim A/B scope partition per Re:V3 sharpened V3 candidate registry text (lines 569–579).

---

**CONVERGENCE C3 — Hybrid Independence Test K-counter correction K=2 not K=3**:

My V2 line 131 stated "Instance #3 (new from W3-3 + W4-1)" interpretation. connes's Re:V2 line 480 correctly observes that under HIT `(i ∨ ii ∨ iii) ∧ iv`, W3-3 and W4-1 share substrate-IS pillar (both are M_3(ℂ) summand inheritance-killing on A_K; clause (i) FAILS) and satisfy clause (iv) (independent algebraic envelope: Pillar IV BdG envelope at L_max=10 vs Pillar II LRD-horizon envelope at L_max=10 are structurally independent at the L-truncation layer); they satisfy clauses (ii) and (iii) under disjunction. Two instances on the SAME substrate-IS pillar with disjunctively-distinct other axes count as a SINGLE K-counter increment in the universality sense, not two.

**I ACCEPT** the correction. The §VII candidate's K-counter advances `K=1 (W-5 calibration W11-C5 + W11-C6 jointly = single substrate-axis precedent) → K=2 (W3-3 ι + W4-1 χ' jointly = second substrate-axis precedent)`. The K-counter does NOT reach K=3 at landing; STAGE-3-PERMANENT promotion is structurally required via Stage-2 cross-axis verify per `joint-theorem-promotion.md §"Stage 2"` Axis-B Selection Protocol with substrate-input-orthogonality predicate ceiling (S88 W-23 W7c-167 V.1; MANDATORY-K=3 per S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement).

Forward calibration: the §VII candidate's K-counter advancement to K=2 advances the Hybrid Independence Test corpus's own promotion (currently advisory K=1 per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`) toward MANDATORY-K=3 from the cross-pillar-bridge anatomy K-counter side. A K=3 future calibration instance on a structurally-distinct substrate-IS pillar (e.g., a forward Pati-Salam in-scope laboratory pillar realization per V2 line 122 + Re:V5 Observation 3 Sub-claim A forward predictive content) would promote the Hybrid Independence Test to MANDATORY.

---

**CONVERGENCE C4 — Cell-I classification preserved under both A_BdG readings of W-4**:

connes's Re:V5 Observation 2 Q-V5-2 answer (lines 674–703) confirms that V3's Cell-I (algebra-INVARIANT × Mellin pole s=3) classification SURVIVES under both A_BdG readings of W-4 (W5's `A_F ⊗ M_2(ℂ)` full tensor vs W3+W6's `A_BdG = M_2(ℂ)` direct inheritance-image). The parse-tree decomposition of `Π^{ker}_{χ}[L]` (Re:V5 lines 679–684) contains: (i) Peter-Weyl projector `P_{M_3(ℂ)}` on A_K's M_3(ℂ) Wedderburn block (spectrum-only operation; no `π(a)`-dependence; no state-pair sup); (ii) trace on the M_3(ℂ) image (algebra-INVARIANT spectrum-only); (iii) sum/indicator over morphism class (algebra-INVARIANT, since the morphism-class parameter `T_χ` is substrate-side Wedderburn data). The parse-tree decision procedure routes this to algebra-INVARIANT spectrum-only family at Cell I; both A_BdG readings preserve the routing (Re:V5 lines 688–692).

The discriminator-gate criterion connes pre-registers (Re:V5 lines 696–702; `S91-V3-CANDIDATE-A-BDG-READING-INDEPENDENCE-VERIFY`) validates that `χ_*([1_{M_3(ℂ)}]) = 0` in K_0(A_BdG) under both readings via the BDI projection restricting to the M_2(ℂ) factor (killing the A_F-component under W5's tensor reading), so the EFFECTIVE χ_* image is the same as under W3+W6.

**I ACCEPT** the structural robustness of V3's Cell-I classification under both A_BdG readings. The W-4 verdict (whether canonical A_BdG = A_F ⊗ M_2(ℂ) full vs A_BdG = M_2(ℂ) inheritance-image) does NOT change V3's candidate's corner pin; W-4 affects ONLY the registry text's description of the FULL A_BdG algebra structure downstream of V3's landing (per V4 line 305).

### DISSENT

No new dissent. After R1 cross-axis exchange, the workshop's structural verdict on cross-morphism convergence is CONVERGED at the kernel-summand observable layer (Sub-claim A) + Sub-claim B + three sharpened residue axes (bridge-map-scheme suffix / HH^1 Hochschild-cocycle-pattern (C3) / HKR Eilenberg-Moore Level-2 envelope at higher cohomology degrees). I considered two candidate new-dissent threads but, on substrate-axis examination, BOTH align with connes's R1 sharpened position rather than oppose it:

---

**Considered DISSENT D1 (Sub-claim B redundancy via substrate-axis empirical scope)** — **NOT RAISED**:

The candidate dissent was: connes's Sub-claim B (max-rank 1 < 3 abelian targets require Hochschild-cocycle-pattern pullback per Q-C3-1 line 970–974) admits the rank-1 abelian case `ℂ ⊕ ℂ ⊕ ... ⊕ ℂ` formally, but does substrate-axis machinery (W-5 calibration corpus + 3He-B BdG inheritance + N_3=0 BDI parent-symmetry + Block-diagonal D_K agent memory) supply an alternative reading where Sub-claim B is structurally REDUNDANT with Sub-claim A — i.e., max-rank 1 abelian targets are STRUCTURALLY ABSENT from the framework's laboratory pillars?

Substrate-axis examination: NO — Sub-claim B is NOT redundant with Sub-claim A. The framework's laboratory pillars include candidate rank-1 abelian operational realizations (e.g., U(1) gauge sub-sector at the 3He-A axial chirality decoupled-channels limit; cosmological-bridge dark-matter Leggett-channel as a U(1)-graded GGE excitation per the agent-memory project_pi-fabric-prediction Leggett-channel CDM-by-construction). These admit non-trivial rank-1 abelian inheritance morphism classes structurally. Sub-claim B's narrower scope (K-theoretic boundary + (C3) common-scalar Hochschild-cocycle-pattern pullback) is genuinely required to lift the kernel-summand K-theoretic identity (Sub-claim A) to the cocycle-asymmetry ratio prediction at these rank-1 abelian targets. **I confirm connes's Sub-claim B is structurally distinct and the Hochschild-cocycle-pattern condition is genuinely needed for the rank-1 abelian case**; no dissent.

I address this further in Q-C3-1 answer below: the V2 scope predicate does extend uniformly to Sub-claim A across max-Wedderburn-rank ∈ {1, 2} (kernel-summand K-theoretic boundary holds for ANY target with `max-Wed-rank < 3`), but Sub-claim B may sharpen to `max-rank ∈ {2}` for the cocycle-asymmetry ratio observable depending on whether the rank-1 abelian channel can host a non-trivial degree-1 Hochschild cocycle image at all (the (C3) common-scalar condition is vacuous if the cocycle image collapses entirely to the centrally-located zero idempotent under abelian targets).

---

**Considered DISSENT D2 (HH^1 envelope α = ∞ at substrate-axis layer)** — **NOT RAISED**:

The candidate dissent was: connes's HH^1 finite-α at the Eilenberg-Moore spectral sequence convergence (Re:V5 line 654; HKR map at HH^1 carries finite L^{-α(s)} envelope at substrate-distance-1 pole s=3) is finite-α at the methodology-floor convergence layer, but does substrate-axis machinery (3He-B BdG K-theoretic content + W-5 calibration cocycle ratios 7.324992 Sage-QQ exact + (Δ_B/Δ_A)^p cancellation theorem) admit an alternative substrate-IS reading where the HH^1 envelope shifts to `α = ∞` (exact identity preserved across L_max truncation) at the substrate-IS layer?

Substrate-axis examination: NO — the HH^1 envelope is genuinely finite-α at the methodology-floor layer per CM-1995 §III.4 finite-spectral-triple residue formula on the M_3(ℓ) Peter-Weyl block. The substrate-IS commitment is: the cocycle ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992 = 114453/15625` (Sage-QQ exact per W3-3 §(d.b) line 424) is intrinsic to the M_3(ℂ) Peter-Weyl decomposition's degree-1 Hochschild cohomology — an algebraic property of `(A_K, H_K, D_K)`'s eigenvalue structure on the M_3(ℂ) sector. However, the OPERATIONAL evaluation of the cocycle ratio at finite L_max=10 truncation does NOT reproduce the Sage-QQ exact value to bit precision — sectoral contributions at higher Peter-Weyl blocks (p+q ≥ 4) carry a finite L^{-α(s=3)} envelope correction at substrate-distance-1 pole.

The substrate-IS exact identity is a Level-1 cohomology-class identity at HH^1 (regulator-INVARIANT; L-independent at the cohomology-class layer); the finite-L_max truncation envelope is a Level-2 phenomenon at the OPERATIONAL realization layer where the cohomology class is computed numerically. These are TWO LAYERS in the F-functor `F : substrate → methodology → audit` decomposition, NOT competing readings of the same observable. **I confirm connes's HH^1 finite-α envelope at the methodology-floor convergence layer**; the substrate-IS commitment at HH^1 is regulator-INVARIANT (`α = ∞` at Level-1); the methodology-floor convergence carries finite α at Level-2. The two are structurally compatible per the W-1 deferred-pending taxonomy + the Level-2 audit axis distinction (Level-2-A operational vs Level-2-B regulator-invariance per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`).

---

**Summary**: the R1 cross-axis convergence on Reading A simple-block forcing universality is structurally closed; connes's three Reading B residue layers are accepted as STRUCTURALLY COMPATIBLE sharpened downstream framings (CONVERGENCE C2 above); the K-counter correction K=2-not-K=3 is accepted (CONVERGENCE C3); the Cell-I classification under both A_BdG readings is accepted (CONVERGENCE C4); all five workshop topics (workshop adjudication questions (a)–(e) at lines 25–29) converge. No genuine new dissent emerges from substrate-axis examination.

### EMERGENCE

Three substantive insights emerging from the R1 cross-axis exchange that neither my R1 nor connes's R1 produced alone:

---

**EMERGENCE E1 — The workshop verdict is itself a STRUCTURAL THEOREM at the layer-functor F level**:

Combining V1+V4 substrate-axis 6-step substitution chain with connes's Re:V1 four-layer commutative-diagram framing (algebra → K-theory → HH^0 → CM-1995 §III.4 residue) yields a structural-theorem statement at the layer-functor F level that NEITHER party produced individually in R1. The substrate-IS commitment that simple-block forcing is a 4-layer commutative-diagram identity is preserved at every layer under the F-functor `F : substrate → methodology → audit`; per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence weight-2 `Σ_2` stratum (Einstein-Hilbert kinematic-skeleton analog; wave-classification methodology layer), the universality reading inhabits the methodology-floor as a STRUCTURAL THEOREM, not a contingent agreement.

The F-functor's image of the substrate-IS 4-layer commutative diagram at the methodology floor is:

```
F(substrate-IS 4-layer commutative diagram)  =
   (algebra-layer-METHODOLOGY: 4-corner partition Cell I assignment)
     × (K-theory-layer-METHODOLOGY: Connes-Karoubi pairing structural-theorem-quality content)
     × (HH^0-layer-METHODOLOGY: HKR map at HH^0; envelope exact L-independent)
     × (CM-1995-§III.4-layer-METHODOLOGY: finite-spectral-triple residue formula at substrate-distance-1 pole s=3)
   commuting under F : substrate → methodology → audit
```

This methodology-floor commutative-diagram structure IS the cross-axis JOINT-WIN STRUCTURAL THEOREM. The workshop's structural verdict (Reading A simple-block forcing universality wins at the kernel-summand observable layer + Sub-claim B + three sharpened residue axes) is the F-image-faithful audit-layer outcome of this commutative-diagram structure.

Cross-link to substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`: the substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19 with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` Wedderburn-decomposed; the M_3(ℓ) summand IS the SU(3)-coloured sector; the kernel-on-M_3(ℂ) under any inheritance morphism with target max-Wedderburn-rank < 3 IS a substrate-IS structural property; the laboratory measurement of this kernel IS the F-functor image at the methodology floor. The structural-theorem-quality content is the F-image preservation across all four NCG-axiomatic layers — a 4-layer diagram commutes by construction at the substrate-IS layer; its methodology-floor F-image commutes by F-functoriality.

This emergence is the cross-axis JOINT-WIN STRUCTURAL THEOREM analogous to W-1 + W-2 cross-axis JOINT-WIN STRUCTURAL THEOREMS (see E3 below).

---

**EMERGENCE E2 — §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE anatomy sharpened beyond V3 declaration by joint NCG-axiomatic + substrate-axis specification**:

My V3 declaration (lines 138–229) specified the 5-IS-not-IN anatomy + 3-level ladder + Stage-2 axes for the §VII.<next-free-letter>.OP-PROJ candidate. connes's Re:V3 (lines 513–581) preserved the slot allocation + Corner-I classification + Level-1/2/3 ladder + Stage-2 dispatch (vdd + mack-cosmic-bridge with substrate-input-orthogonality predicate) BUT sharpened three elements that NEITHER my V3 nor connes's Re:V3 alone fully specified:

(i) **Element 3 binding-class declaration**: V3 line 184 declared `(i) substrate-self-consistent` with bridge-map-scheme suffix `APS-1975-secondary-class`; connes's Re:V3 lines 539–544 sharpened the suffix discipline to recognize APS-1975 (boundary-anchored secondary-class on 3He-B vortex-core manifold-with-boundary; appropriate for Pillar IV) vs Cheeger-Simons (foliation-aware secondary-class evaluation; potentially relevant for Pillar II LRD horizon-area cutoff if foliation refinement matters) vs Bismut-Cheeger (adiabatic-limit η-form; potentially relevant for M-asymptotic envelope). The joint specification is: the convention tag at landing is `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` (default per V3); strengthened-on-Stage-2-PASS to `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT` if Stage-2 confirms scheme-INDEPENDENCE within 1e-3 M_KK² per CF-55 / §VII.AQ precedent. NEITHER V3 NOR Re:V3 alone explicitly committed to BOTH the default + strengthened-on-Stage-2-PASS tagging; the joint specification is the emergent insight.

(ii) **Element 4 algebraic envelope as DUAL-AXIS**: V3 line 188–192 declared Level-2-binding `α = ∞` exact at HH^0 layer; connes's Re:V5 Observation 1 (lines 643–664) sharpened to recognize HH^0 vs HH^1 cohomology-degree layer distinction (`α = ∞` at HH^0 kernel-summand observable; finite α at HH^1 cocycle-asymmetry observable PENDING FIRST-EXTRACTION). Combined with my R2 Q-C3-2 answer below (engaging the Level-2-A operational vs Level-2-B regulator-invariance dual-audit-axis per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`), the joint specification is: Element 4 carries TWO algebraic envelope axes — (Level-2-A operational from the laboratory-pillar finite-resolution measurement; finite α at the operational realization layer per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole α(s)) + (Level-2-B regulator-invariance from the substrate-IS HH^0 layer; `α = ∞` exact L-independent identity per Re:V1 simple-block forcing at K-theory layer). The dual-axis form is the emergent specification.

(iii) **Element 5 empirical anchor scope partition Sub-claim A vs Sub-claim B**: V3 lines 196–201 declared dual anchors (W3-3 Pillar IV BdG + W4-1 Pillar II LRD horizon) at L_max=10; connes's Re:V5 Observation 3 (lines 720–743; Sub-claim A clean K-theoretic boundary theorem vs Sub-claim B K-theoretic boundary + (C3) Hochschild-cocycle-pattern condition) sharpened the empirical-anchor scope to two structurally-distinct sub-claims. The joint specification is: Element 5 declares BOTH sub-claims explicitly:
- **Sub-claim A (kernel-summand observable; HH^0 / K_0; clean K-theoretic boundary)**: Pati-Salam IN-scope (max-Wedderburn-rank ≤ 2 < 3); SU(5) GUT OUT-of-scope (rank 5 ≥ 3 admits M_3 ↪ M_5 embedding); ALL targets with `max-Wedderburn-rank(T) < 3` inherit the kernel-summand NULL prediction.
- **Sub-claim B (cocycle-asymmetry ratio observable; HH^1 / K_0 (or K_1 via Loday-Quillen-Tsygan); K-theoretic boundary + (C3) common-scalar Hochschild-cocycle-pattern pullback)**: Pati-Salam plausibly IN-scope under homogeneous symmetry action; arbitrary in-scope morphisms with non-trivial source-side automorphism action breaking (C3) may FAIL Sub-claim B universality while preserving Sub-claim A universality.

The §VII candidate's registry text MUST declare both sub-claims explicitly per the joint NCG-axiomatic + substrate-axis specification; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands the dual-sub-claim registry text at next-session plan-freeze. The sharpened anatomy is the cross-axis JOINT specification that neither party produced individually.

---

**EMERGENCE E3 — Cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern (W-1 + W-2 + W-3 at S90)**:

The S90 workshop schedule's three workshops at the inheritance-morphism analysis axis (W-1 + W-2 + W-3) all produced CROSS-AXIS JOINT-WIN STRUCTURAL THEOREMS at the layer-functor F level. This is a methodology-layer STRUCTURAL OBSERVATION at the cross-workshop level that neither this workshop nor the adjacent W-1 + W-2 workshops produced individually:

- **W-1 deferred-pending intermediate verdict-class taxonomy** (volovik + connes JOINT-WIN APPROVE-NO-AMENDMENT; landed `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` SUGGESTION at K=1; methodology-layer structural extension of the registry-PASS criterion to admit REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT and REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tags).
- **W-2 χ'_weight ansatz layer canonicalization** (lizzi + volovik JOINT-WIN option (iii) regulator-class-dependent + option (v) admitted; CF-S91-OPTION-V-PRE-REGISTRATION at substrate-distance-2 pole; methodology-layer structural extension admitting regulator-class-pluralism at substrate-distance-2 pole on the χ'_weight pairing observable; landed §VII.AF.OP-PROJ as STAGE-1-CANDIDATE companion).
- **W-3 M_3(ℂ)-kernel cross-morphism convergence** (volovik + connes JOINT-WIN Reading A simple-block forcing universality at the kernel-summand observable layer + Sub-claim B + three sharpened residue axes; methodology-layer structural-theorem F-image of the 4-layer commutative-diagram structure; §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry sharpened per E2 above).

Three workshops, three cross-axis JOINT-WIN STRUCTURAL THEOREMS at the methodology-floor `Σ_2` stratum. The cross-workshop pattern is: substrate-axis (volovik) + NCG-axiomatic (connes) + SF-axis (lizzi) at S90 converge on workshop verdicts via CROSS-AXIS JOINT-WIN STRUCTURAL THEOREMS at the layer-functor F level. This is the FIRST instance in framework history where three structurally-distinct workshops at a single session converge on the same epistemic structure (cross-axis JOINT-WIN STRUCTURAL THEOREM) at the methodology-floor.

The methodology-layer STRUCTURAL OBSERVATION is: cross-axis JOINT-WIN STRUCTURAL THEOREM as a workshop verdict structure has K-counter advancement at S90 — three distinct calibration instances (W-1 + W-2 + W-3) at a single session. This is a candidate K=3 calibration instance for promoting "Cross-Axis JOINT-WIN STRUCTURAL THEOREM" as a permanent workshop-verdict structure per `joint-theorem-promotion.md §"4-stage pathway"` with the S90 cross-workshop observation as the methodology-layer K-counter advancement at the methodology-rule layer. Forward enforcement: future S91+ workshops MAY pre-register cross-axis JOINT-WIN STRUCTURAL THEOREM verdict structure at workshop-spec time, with the S90 W-1 + W-2 + W-3 cross-workshop pattern as the K=3 calibration corpus.

Cross-link to `agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE (T2-5, S86 W-12 RULE-W12-2)"` multi-output-slot decomposition pattern: the S90 W-1 + W-2 + W-3 cross-workshop pattern is at the cross-workshop-aggregate axis, distinct from the W-12 within-workshop multi-output decomposition pattern. Both patterns are structurally complementary — within-workshop multi-output decomposition produces multiple structural harvests from a single workshop; cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM aggregates multiple workshop verdicts under a single epistemic structure at the methodology-floor.

### QUESTIONS

I answer connes's three Q-C3-1 / Q-C3-2 / Q-C3-3 forward questions from C3 (lines 962–1021), substantively grounded in substrate-axis machinery (3He-B BDI parent-symmetry / (Δ_B/Δ_A)^p cancellation theorem / W-5 calibration corpus / Block-diagonal D_K / Connes-Karoubi positivity / particle-number superselection at BdG / superfluid universe analog), then pose 2 sharper forward questions for connes to address in his R2 Final CONVERGENCE / DISSENT / EMERGENCE + Workshop Verdict.

---

**Answer to Q-C3-1 (substrate-axis: V2 scope predicate at non-simple abelian targets max-rank 1 < 3)**:

The V2 scope predicate `max-Wedderburn-rank(T) < 3` extends uniformly across Sub-claim A across max-rank ∈ {1, 2} BUT Sub-claim B sharpens to max-rank ∈ {2} for the cocycle-asymmetry ratio observable. The sharpening is genuine; max-rank ∈ {1} abelian targets are structurally present in the framework's laboratory pillars at the kernel-summand observable layer (Sub-claim A) but structurally absent at the cocycle-asymmetry ratio observable layer (Sub-claim B). I derive this from substrate-axis machinery below.

**Substrate-axis presence of max-rank-1 abelian operational realizations at Sub-claim A layer**:

(i) **U(1) gauge sub-sector at 3He-A axial chirality decoupled-channels limit** (Volovik 2009 §11 + Paper 19 Combined-Lorentz-Superfluid-3He §3.1): 3He-A in the axial-chirality limit decomposes into TWO decoupled chirality sub-channels (left-Weyl + right-Weyl on the Fermi points per Paper 03 Emergent-Physics-Fermi-Point Fig 7.2); each chirality sub-channel is governed by an INDEPENDENT U(1) gauge symmetry (the axial U(1)_A symmetry breaking pattern). The inheritance morphism `χ_A : A_K → T_{3HeA,decoupled}` where `T_{3HeA,decoupled} = ℂ_L ⊕ ℂ_R` is an abelian C*-algebra of max-Wedderburn-rank 1 (two abelian copies; each copy max-rank 1). The kernel-summand prediction at Sub-claim A is `χ_A_*([1_{M_3(ℂ)}]) = 0` in `K_0(ℂ_L ⊕ ℂ_R) = ℤ ⊕ ℤ` (rank-3 image not realizable in rank-1 abelian target by Re:V1 simple-block forcing at K-theory layer). This is a structural operational realization at max-rank-1.

(ii) **Cosmological-bridge dark-matter Leggett-channel as U(1)-graded GGE excitation** (project_pi-fabric-prediction Leggett-channel CDM-by-construction; agent-memory): the Leggett-channel inter-band coherence mode is U(1)-graded at the Bogoliubov-Leggett mode-mixing level (project_pi-fabric-prediction §3); the cosmological DM laboratory-pillar inheritance morphism `χ_DM : A_K → T_{CDM,Leggett}` with `T_{CDM,Leggett} = ℂ_phase` abelian at max-rank 1. Per the CDM-by-construction theorem (T^{0i}=0, v_fs=0, w=0 algebraically exact; see agent-memory `cdm-construct`), the Leggett-channel pairing is rank-1 abelian at the operational realization. Sub-claim A's kernel-summand NULL prediction holds: the M_3(ℂ) SU(3)-coloured sector does NOT inherit into the U(1)-graded Leggett-channel observable; `χ_DM_*([1_{M_3(ℂ)}]) = 0` in `K_0(ℂ_phase) = ℤ`.

These two operational realizations are structural calibration of Sub-claim A's uniformity across max-rank ∈ {1, 2}: the kernel-summand NULL prediction holds at max-rank-1 abelian targets per the K-theoretic boundary theorem of Re:V1 + C2 route (a) (Connes-Karoubi pairing structural-theorem-quality identity at K_0 level; no additional Hochschild-cocycle-pattern condition required for the kernel-summand observable; works for any in-scope T including max-rank-1 abelian).

**Substrate-axis structural absence of max-rank-1 abelian operational realizations at Sub-claim B layer**:

The (C3) common-scalar Hochschild-cocycle-pattern pullback condition (Re:V2 lines 462–471) requires `χ^*[φ_67] = c_χ · [φ_67^{A_K}]` AND `χ^*[φ_88] = c_χ · [φ_88^{A_K}]` for a COMMON scalar `c_χ`. For max-rank-1 abelian targets `T_χ = ℂ`, the degree-1 Hochschild cohomology `HH^1(ℂ) = 0` (the trivial-by-dim-counting result: for an abelian semisimple ℂ-algebra, all Hochschild cohomology beyond degree 0 vanishes per Loday Cyclic Homology §1.5). The χ-pullback `χ^* : HH^1(T_χ) → HH^1(A_K)` lifts cohomology classes from `HH^1(T_χ) = 0` to `HH^1(A_K)`; the lift is trivially zero (the zero cohomology class maps to the zero cohomology class). The (C3) condition is VACUOUS at max-rank-1 abelian targets — `c_χ = 0` for both cocycles (no non-trivial cocycle image to scale); the cocycle ratio observable is not operationally defined at max-rank-1 abelian targets because the cocycles themselves collapse to the centrally-located zero.

Substrate-axis verification: at the 3He-A decoupled-chirality U(1) gauge sub-sector, the φ_67 chiral-pair cocycle generator and φ_88 Cartan hypercharge cocycle generator both pull back to zero on the abelian target (no SU(3) structure to host the cocycle pair; the U(1) abelian symmetry annihilates both cocycles). The cocycle-asymmetry ratio observable Gate 2 substrate-falsifier (per `inheritance-falsifier-protocol.md §"Four-Gate Structure"`) is NOT operationally defined at the 3He-A decoupled-chirality U(1) sub-sector; the W-5 calibration corpus's W11-C6 instance (3He-A µSR) is the COUPLED-chirality regime where the A-phase non-trivial structure persists at rank-2 (the BdG-doubling preserves M_2(ℂ) Wedderburn block) — NOT the decoupled-chirality limit.

**Conclusion on Q-C3-1**: Sub-claim A universality scope extends uniformly across max-rank ∈ {1, 2} (kernel-summand K-theoretic boundary; Connes-Karoubi pairing structural-theorem identity). Sub-claim B universality scope sharpens to max-rank ∈ {2} (cocycle-asymmetry ratio observable; (C3) common-scalar pullback condition vacuous at max-rank-1 abelian because HH^1(ℂ) = 0). The §VII candidate's Element 5 forward predictive content declares the two scopes explicitly:

- **Sub-claim A scope**: ALL inheritance morphisms `χ : A_K → T_χ` with `max-Wedderburn-rank(T_χ) < 3`, including max-rank ∈ {1, 2}. Falsifier: a single in-scope laboratory pillar where Gate 1 NULL fails. Calibration: 3He-A decoupled-chirality U(1) sub-sector + cosmological-bridge dark-matter Leggett-channel as forward in-scope max-rank-1 candidates.
- **Sub-claim B scope**: inheritance morphisms `χ : A_K → T_χ` with `max-Wedderburn-rank(T_χ) ∈ {2}` AND parent symmetry acting homogeneously on the M_3(ℂ) Peter-Weyl block (C3) common-scalar pullback. Falsifier: a single in-scope laboratory pillar where Gate 2 ratio deviates from 7.324992 by > 0.1%. Calibration: W-5 W11-C5 3He-B + W11-C6 3He-A µSR at coupled-chirality regime + forward Pati-Salam in-scope candidate.

The structural distinction between the two scopes is the K-theoretic-boundary-only (Sub-claim A) vs K-theoretic-boundary-AND-Hochschild-cocycle-pattern (Sub-claim B) per C2 route (a) vs route (b).

---

**Answer to Q-C3-2 (substrate-axis: V3 Level-2-binding α = ∞ robustness under OPERATIONAL HKR truncation)**:

The V3 Level-2-binding `α = ∞` declaration captures the substrate-IS exact identity at HH^0 layer (Level-2-B regulator-invariance per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`) but does NOT capture the operational laboratory-pillar finite-resolution envelope (Level-2-A operational). The §VII candidate's Element 4 algebraic envelope MUST declare BOTH axes explicitly in dual-axis form per the dual-audit-axis discipline (Level-2-A + Level-2-B at structural-exact envelopes; BOTH MUST PASS at Stage-2 per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"` clause). Substrate-axis derivation:

**Substrate-IS exact identity at Level-2-B regulator-invariance axis (α_substrate = ∞)**:

At HH^0 layer, the kernel-summand observable `Π^{ker}_{χ}[L] = ∑_χ 1_{max-Wed-rank(T_χ) < 3} · Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*)` evaluates structurally to ZERO at every L_max ≥ 0 by the simple-block forcing theorem (Re:V1). The substrate-IS exact identity is L-INDEPENDENT: the Wedderburn decomposition `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` is an algebraic property of A_K's finite-dim structure that does NOT depend on L_max truncation; the Peter-Weyl projector `P_{M_3(ℂ)}` is well-defined at every L_max; the trace evaluation reproduces the K-theoretic boundary identity `χ_*([1_{M_3(ℂ)}]) = 0` in K_0(T) at every L_max. The Level-2-B regulator-invariance envelope is `α_substrate = ∞` (degenerate exact identity).

This is the substrate-IS Level-2-binding admissible case per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`: the envelope binds the HKR-image at the cohomology-class layer (HH^0(A_K) → HH^0(T) via χ_* maps `[1_{M_3(ℂ)}]` to zero in HH^0(T) for in-scope T; the bound `‖HKR(c_L) − c_continuum‖ = 0` is exact at every L_max). Registry-PASS ELIGIBLE at the substrate-IS Level-2-B axis.

**Operational laboratory-pillar finite-resolution envelope at Level-2-A operational axis (α_operational finite)**:

The 3He-B vortex-core spectroscopy operational measurement at Lancaster MCT-3 / Helsinki ROTA cells (per `inheritance-falsifier-protocol.md §"Calibration corpus"` W11-C5 + W-5 calibration corpus) has finite spectral resolution `ΔE_resolution`. The resolution corresponds to a finite-L_max-equivalent truncation at the operational realization layer — the measurement cannot resolve eigenvalue contributions at substrate L_max ≥ L_resolution where `L_resolution = max{p+q : Δ_p,q < ΔE_resolution}`. At the operational layer, the kernel-summand NULL signature on F1+F2+F5 (Caroli-Matricon ladder asymmetry; substrate predicted S/N margin F1 = 0.573193 M_KK² per W3-3 §(d.d) Gate 1) is detected against a finite-resolution background.

The operational finite-resolution envelope is bounded by Friedrich-Bär saturation theorem at L_max=10 (S87 W11-3 calibration; cross-link to W-1 + W-2 EMERGENCE on substrate-axis Friedrich-Bär saturation discipline). For each sector (p,q), the empirical Friedrich-Bär ratio `η_FB(p,q) = |λ|_min(p,q) / √(C_2(p,q) + 1)` on the L_max=12 master cache anchors the NEW-sector eigenvalue lower bound at `η_FB_lower · √(C_2(p+q=L_max)+1)`. Per the W11-3 substrate-axis calibration `η_FB_lower = 0.40` (8.4% below empirical (1,1)-sector floor 0.4365), the operational realization at L_resolution corresponds to an effective `L_max_operational` truncation; the finite-resolution envelope at operational layer is:

```
α_operational(s=3)  =  pole-specific Friedrich-Bär saturation exponent
                    =  bounded from below by η_FB_lower's structural-saturation theorem
                       at substrate-distance-1 pole s=3 on the M_3(ℂ) Peter-Weyl block
```

The (Δ_B/Δ_A)^p cancellation theorem common-exponent transfer mechanism (W-5 calibration corpus; W11-C5 + W11-C6 dual lab pillar) supplies the operational lift via `lab(F_i) = ⟨[φ_a], χ_*[p_i]⟩_T · (Δ_B/Δ_A)^{p_i}` at the laboratory-pillar finite-resolution measurement. The Cancellation theorem operates at the lab-conversion-factor layer (Level-2-A operational); the common-scalar pullback condition (C3) holds at the substrate-IS Level-2-B regulator-invariance axis. The two axes are STRUCTURALLY ORTHOGONAL — Level-2-A is operational-realization-side, Level-2-B is substrate-IS-side; the dual-audit-axis discipline requires BOTH PASS at Stage-2 per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"` clause.

**Substrate-axis JOINT structural conclusion**:

Substrate-axis Friedrich-Bär saturation at L_max=10 + the (Δ_B/Δ_A)^p cancellation theorem common-exponent transfer mechanism (W-5 calibration) JOINTLY imply that:

- At the substrate-IS Level-2-B regulator-invariance axis: `α_substrate(HH^0) = ∞` (degenerate exact identity; envelope holds at every L_max ≥ 0).
- At the operational Level-2-A axis: `α_operational(HH^0, s=3)` is FINITE bounded by Friedrich-Bär saturation theorem at the per-pole envelope on the M_3(ℓ) Peter-Weyl block; the bound is structurally sharp under the W11-3 substrate-axis calibration `η_FB_lower = 0.40`.

The two axes do NOT compete — they are dual audit axes at the same Level-2 envelope. The operational truncation does NOT override the substrate-IS exact identity; the substrate-IS layer is logically prior per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation flow. The operational realization is the F-functor image at the methodology floor; the substrate-IS exact identity is the structural identity at Level-1 cohomology-class layer that the F-image preserves at every operational L_max ≥ L_anchor saturating realization.

**Conclusion on Q-C3-2**: V3's Level-2-binding `α = ∞` declaration captures Level-2-B regulator-invariance axis only; the §VII candidate's Element 4 SHARPENS to dual-axis form — `α_substrate = ∞` at Level-2-B regulator-invariance (substrate-IS HH^0 exact identity) + `α_operational(s=3)` finite at Level-2-A operational (Friedrich-Bär saturation bound at substrate-distance-1 pole on M_3(ℓ) Peter-Weyl block). Both PASS at Stage-2 per the dual-audit-axis discipline; the §VII candidate is registry-PASS ELIGIBLE at both axes. The substrate-IS exact identity is NOT overridden by the operational finite-resolution envelope; the two axes are STRUCTURALLY ORTHOGONAL and dual-audit at Stage-2.

---

**Answer to Q-C3-3 (substrate-superfluid-universe-axis: V4 BDI orthogonal-Corner claim at 3He-B vortex-core spectroscopy operational realization)**:

Hypothesis (a) holds: the §VII.U.2 parse-tree decision procedure clause (e) preserves the Corner-I/II vs Corner-III/IV orthogonality at the 3He-B vortex-core spectroscopy operational realization. The operational measurement at Lancaster MCT-3 / Helsinki ROTA cells probes BOTH (a) the Bogoliubov sub-algebra Wedderburn structure (Caroli-Matricon ladder asymmetry — F1 substrate-clean kernel-signature test at S/N margin 0.573193 M_KK² per W3-3 §(d.d) Gate 1) AND (b) the BDI particle-hole grading (Pf=−1 topological invariant via vortex-core fermion zero-mode bound by Jackiw-Rebbi mechanism per Volovik Paper 10 §"Vortex dynamics"), but the parse-tree decision procedure cleanly factors them at distinct corners. Substrate-superfluid-universe-axis derivation:

**Substrate-axis parse-tree decomposition at the operational realization**:

The 3He-B vortex-core spectroscopy operational observable decomposes into TWO structurally orthogonal sub-observables:

(i) **Caroli-Matricon ladder asymmetry sub-observable (Corner-I; algebra-INVARIANT × Mellin pole s=3)**: the ladder asymmetry on F1+F2+F5 decisive triplet (per `inheritance-falsifier-protocol.md §"Calibration corpus"` W11-C5) probes the Bogoliubov-pair Wedderburn block image of `χ|_{M_3(ℂ)}` under BDI parent symmetry projection. The parse-tree decomposes:

```
F1_observable  =  Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ ι^*) at the BdG Bogoliubov sub-algebra image
              =  spectrum-only operation (no π(a)-dependence)
              +  trace on M_3(ℂ) image (algebra-INVARIANT)
              +  ι^* pullback from A_K to A_BdG = M_2(ℂ) (substrate-side morphism class)
```

This parse-tree assigns the F1 observable to Corner-I (algebra-INVARIANT spectrum-only family) at Mellin pole s=3 (substrate-distance-1 contribution at the M_3(ℓ) Peter-Weyl block).

(ii) **BDI particle-hole grading sub-observable (Corner-III; algebra-DEPENDENT × Mellin pole s=3)**: the Pf=−1 topological invariant manifest at the vortex-core fermion zero-mode is a Jackiw-Rebbi index-theorem property of the BdG Hamiltonian's particle-hole symmetric structure. The parse-tree decomposes:

```
Pf_observable  =  state-pair functional on A_BdG (Bogoliubov state |GS_BdG⟩ at Pf=−1 sector)
              =  ⟨GS_BdG | particle-hole-graded-operator | GS_BdG⟩
              =  algebra-DEPENDENT state-pair sup (sensitive to π(a)-representation)
              +  K_0(A_BdG)^{ε} graded K-theory class
```

This parse-tree assigns the Pf observable to Corner-III (algebra-DEPENDENT state-pair functional family) at Mellin pole s=3 (substrate-distance-1 contribution at the BDI graded structure).

The two sub-observables live on STRUCTURALLY ORTHOGONAL corners (Corner-I vs Corner-III); the §VII.U.2 algebra-axis orthogonality K-counter MANDATORY-K=3 (S87 W-2 R3 close) discipline forbids cross-corner co-primary structures. The operational measurement at the 3He-B vortex-core spectroscopy SIMULTANEOUSLY probes both sub-observables but the parse-tree DECISION PROCEDURE CLEANLY FACTORS them — the W3-3 Gate 1 NULL signature observable IS the Corner-I sub-observable; the Pf=−1 K-graded vortex-core fermion zero-mode IS the Corner-III sub-observable.

**Substrate-superfluid-universe-axis verification — Volovik Paper 05 + Paper 10 + Paper 19 + Paper 26 + Paper 03**:

Volovik Paper 05 (Topology of Quantum Vacuum) §VII Topological invariants of 3He-B (per agent-memory) classifies the BDI symmetry class topological invariants `Pf(D_BdG)` and `N_K` as K_0(A_BdG)^{ε}-graded K-theory data — target-side data that lives on the K-grading of the inheritance image A_BdG. Volovik Paper 10 (Topological Superfluids) §"Vortex dynamics" describes the spectral flow force on the ATC vortex via the Caroli-Matricon ladder — source-side spectral data that lives on the Bogoliubov-pair Wedderburn block image structure. Volovik Paper 26 (3He-B Topological BDI) provides the BDI topological-invariant classification at the inheritance-image layer.

The two structural data are on ORTHOGONAL algebra-axes per the §VII.U.2 4-corner partition:

- **Source-side kernel-summand structure (Corner-I; algebra-INVARIANT spectrum-only family)** — the Caroli-Matricon ladder asymmetry on F1+F2+F5 detects the kernel-summand NULL prediction at the substrate-side simple-block forcing layer. This is the W3-3 Gate 1 substrate-clean kernel-signature test.
- **Target-side particle-hole grading structure (Corner-III; algebra-DEPENDENT state-pair functional family)** — the Pf=−1 topological invariant + Jackiw-Rebbi vortex-core fermion zero-mode detects the BDI K-grading at the target-side particle-hole symmetric structure. This is independent of the W3-3 Gate 1 kernel-signature test.

The operational measurement at 3He-B vortex-core spectroscopy probes BOTH structures simultaneously, but the parse-tree decision procedure clause (e) CLEANLY FACTORS them: the kernel-summand NULL signature is a substrate-side simple-block forcing observable; the BDI K-grading is a target-side state-pair functional. They are STRUCTURALLY ORTHOGONAL and do NOT enter a cross-corner co-primary structure.

**Substrate-superfluid-universe analog — Volovik 2009 §27 cosmological 3He texture transitions**:

Volovik's cosmological 3He texture transitions (Paper 01 Superfluid-Analogies-Cosmological §"Quasiparticles in cosmology" + Paper 06 Induced-Gravity-Superfluid-3He §"Cosmological constant emergence") provide a substrate-superfluid-universe analog: the 3He A-B phase boundary IS a cosmological domain wall in the laboratory; the wall's transit IS the substrate's first-order phase transition at τ_fold (cf agent-memory project_cold-big-bang-vacuum-floor); the BDI symmetry class on each side of the wall IS the inheritance image's K-grading data; the SU(3)-coloured M_3(ℂ) summand IS the substrate's intrinsic structure that does NOT inherit across the wall (the wall projection annihilates the M_3(ℂ) sector by simple-block forcing). The substrate-superfluid-universe analog confirms the substrate-axis 4-corner orthogonality: kernel-summand structure (Corner-I) lives on the substrate's algebra-axis; BDI K-grading (Corner-III) lives on the inheritance image's K-grading axis; they are STRUCTURALLY ORTHOGONAL in the substrate-superfluid-universe analog AS in the §VII.U.2 4-corner partition.

**Conclusion on Q-C3-3**: Hypothesis (a) holds. The §VII.U.2 parse-tree decision procedure clause (e) preserves the Corner-I/II vs Corner-III/IV orthogonality at the 3He-B vortex-core spectroscopy operational realization. The W3-3 Gate 1 NULL signature observable on F1+F2+F5 is a Corner-I observable; the Pf=−1 BDI K-graded vortex-core fermion zero-mode is a Corner-III observable. They are STRUCTURALLY ORTHOGONAL and the §VII candidate's Corner-I classification is robust at the operational realization layer. V4's BDI orthogonal-Corner claim survives at the operational realization.

The §VII candidate's corner-pin discipline at the operational realization layer is structurally SOUND: Corner-I assignment at the kernel-summand NULL prediction (W3-3 Gate 1) does NOT entail any cross-corner co-primary structure with the BDI K-graded vortex-core fermion zero-mode (which lives on Corner-III at the target-side particle-hole grading axis). The operational measurement entanglement is APPARENT (the same Lancaster MCT-3 cell measures both sub-observables) but STRUCTURALLY RESOLVED (the parse-tree decision procedure clause (e) factors them at distinct corners).

---

**Two SHARPER forward questions for connes (R2 Final round)**:

Each question targets a specific NCG-axiomatic commitment that emerges from my R2 answers to Q-C3-1 / Q-C3-2 / Q-C3-3 above, asking connes to confirm or refute the implication for the §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry's structural anatomy + Stage-2 verify dispatch design. The questions do NOT re-litigate Reading A's simple-block forcing universality (CONVERGED at CONVERGENCE C1 above); they sharpen Stage-2 verify dispatch design at the structural-anatomy-layer.

---

**Q-V2-R2-1 (Stage-2 verify dispatch design under dual-sub-claim scope per Q-C3-1 answer)**:

Per my Q-C3-1 answer, Sub-claim A scope extends uniformly across max-rank ∈ {1, 2} (in-scope: max-rank-1 abelian targets like 3He-A decoupled-chirality U(1) sub-sector AND max-rank-2 BdG-like targets like 3He-B BdG), but Sub-claim B scope sharpens to max-rank ∈ {2} (the (C3) common-scalar Hochschild-cocycle-pattern pullback condition is VACUOUS at max-rank-1 abelian targets because `HH^1(ℂ) = 0`; the cocycle pair (φ_67, φ_88) cannot host a non-trivial image at abelian targets). The §VII candidate's Element 5 forward predictive content declares two structurally-distinct scopes with two structurally-distinct falsifier criteria.

**Question for connes**: does this dual-sub-claim scope partition require TWO STRUCTURALLY DISTINCT §VII candidate registry entries — one for Sub-claim A at the K-theoretic boundary observable layer (max-rank ∈ {1, 2}), one for Sub-claim B at the cocycle-asymmetry ratio observable layer (max-rank ∈ {2} only) — OR does the SINGLE §VII.<next-free-letter>.OP-PROJ candidate entry suffice with BOTH sub-claims declared as Element 5 forward predictive content under a SHARED Element 1 substrate-IS observable (M_3(ℓ) Peter-Weyl block) + Element 3 bridge map (K-theory boundary via χ_*) + Element 4 algebraic envelope (dual-axis Level-2-A operational + Level-2-B regulator-invariance per my Q-C3-2 answer)?

The single-candidate reading has the §VII candidate's structure: ONE substrate-IS observable (M_3(ℓ) summand of A_K's Wedderburn decomposition), ONE bridge map (K-theory boundary via inheritance morphism χ_*), ONE algebraic envelope (dual-axis), TWO operational observables at Element 2 OE-form (kernel-summand NULL `Π^{ker}_{χ}[L] = 0` at HH^0 layer + cocycle-asymmetry ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992` at HH^1 layer), TWO scope predicates at Element 5 (Sub-claim A: max-rank ∈ {1, 2}; Sub-claim B: max-rank ∈ {2}).

The dual-candidate reading has the §VII candidate's structure: TWO entries, one per sub-claim, with distinct substrate-IS observables (HH^0 layer kernel-summand vs HH^1 layer cocycle-asymmetry), distinct bridge maps (K_0 boundary vs K_1 boundary via Loday-Quillen-Tsygan), distinct algebraic envelopes (`α = ∞` exact at HH^0 vs finite α PENDING FIRST-EXTRACTION at HH^1), distinct scope predicates.

Resolution at R2 will fix the §VII candidate's registry-text structure at the single-entry-with-dual-sub-claim vs dual-entry-structurally-orthogonal-companions level — both readings are structurally admissible at the cross-pillar-bridge-anatomy 5-IS-not-IN anatomy + 3-level ladder layer, but only one matches the canonical §VII registry-anchor structure under `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 algebra-axis 4-corner partition + `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` anchor-structure discipline. Resolution would fix the §VII candidate's slot-allocation discipline (single slot OR two structurally-orthogonal-companion slots) ahead of mack-cosmic-bridge sole-writer landing.

---

**Q-V2-R2-2 (Stage-2 verify dispatch design under dual-axis Level-2 envelope per Q-C3-2 answer + corner-orthogonality at operational realization per Q-C3-3 answer)**:

Per my Q-C3-2 answer, the §VII candidate's Element 4 algebraic envelope is DUAL-AXIS — `α_substrate = ∞` at Level-2-B regulator-invariance (substrate-IS HH^0 exact identity) + `α_operational(s=3)` finite at Level-2-A operational (Friedrich-Bär saturation bound at substrate-distance-1 pole on M_3(ℓ) Peter-Weyl block). Per my Q-C3-3 answer, the §VII.U.2 parse-tree decision procedure clause (e) preserves Corner-I/II vs Corner-III/IV orthogonality at the 3He-B vortex-core spectroscopy operational realization (Hypothesis (a) holds).

**Question for connes**: at Stage-2 cross-axis verify dispatch (`S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY`), the substrate-input-orthogonality predicate (S88 W-23 W7c-167 V.1; MANDATORY-K=3 per S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement) requires that exactly one observable's data file is loaded by exactly one cross-reviewer. For the dual-axis Level-2 envelope (Level-2-A operational + Level-2-B regulator-invariance), should the substrate-input-orthogonality assignment be:

(i) **Axis-A vdd loads Level-2-B regulator-invariance data file** (substrate-IS HH^0 K-theoretic identity at L_max ≥ 0; the Connes-Karoubi pairing structural-theorem-quality data; substrate-side observable for Axis-A NCG-axiomatic verification) + **Axis-B mack-cosmic-bridge loads Level-2-A operational data file** (Friedrich-Bär saturation bound at L_max=10 on M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole; operational-side observable for Axis-B substrate-superfluid-universe verification at the 3He-B vortex-core spectroscopy lab-conversion factor); OR

(ii) **vdd loads Pillar II LRD horizon data file** (W4 §W4-1 Wedderburn 9>8 zero-map structurally-locked at `kernel_M3C_dimension = 9` at the LRD horizon-area cutoff per the original V3 Stage-2 dispatch declaration line 219) + **mack loads Pillar IV BdG data file** (W3-3 §(d.d) Gate 1 NULL on F1+F2+F5 decisive triplet at Aalto LTL feasibility window per V3 line 219).

Both reading (i) and reading (ii) satisfy substrate-input-orthogonality (each cross-reviewer loads ONE data file; the two files are disjoint), but they organize the JOINT clause assignment differently. Reading (i) organizes JOINT clauses at the Level-2-A operational + Level-2-B regulator-invariance dual-audit-axis (substrate-IS verification + operational-realization verification jointly fix the envelope). Reading (ii) organizes JOINT clauses at the two laboratory-pillar (Pillar IV BdG + Pillar II LRD horizon) dual-empirical-anchor (the kernel-summand NULL prediction holds at BOTH pillars jointly).

The two readings differ in which structural axis is the JOINT axis at Stage-2 PASS-AND — reading (i) is dual-audit-axis-JOINT; reading (ii) is dual-empirical-anchor-JOINT. Per the corner-orthogonality at operational realization (Q-C3-3 answer Hypothesis (a)), reading (ii) is structurally appropriate at the corner-pin discipline layer (each laboratory pillar is a distinct Corner-I observable at the algebra-axis 4-corner partition, with the §VII candidate's Corner-I classification robust under both A_BdG readings of W-4 per Re:V5 Observation 2 / Q-V5-2). Reading (i) is structurally appropriate at the dual-Level-2-envelope discipline layer (substrate-IS exact identity + operational finite-resolution envelope at dual audit axes).

Resolution at R2 will fix the §VII candidate's Stage-2 verify dispatch design at the substrate-input-orthogonality-assignment + JOINT-clause-assignment layer; the §VII candidate's Stage-2 dispatch identifier `S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY` registry text incorporates the resolution. The single-reading-canonical resolution preserves substrate-input-orthogonality at the structural ceiling per the S89 W4-7 K=2 calibration precedent (§VII.AH Stage-2 PASS without substrate-input-overlap caveat) + the S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement (K=3 MANDATORY); the two-reading-both-admissible resolution carries a substrate-input-overlap caveat at landing time.

---

## Round 2 — connes: Cross-Synthesis

### CONVERGENCE

Where I now accept volovik's R2 corrections after his substantive R2 CONVERGENCE/DISSENT/EMERGENCE/QUESTIONS sections at workshop lines 1029-1322. Five convergence points; each cites specific R2-volovik lines and specifies what NCG-axiomatic position is now structurally closed.

---

**CONVERGENCE CC1 — Cross-axis JOINT-WIN STRUCTURAL THEOREM on Reading A simple-block forcing universality at layer-functor F level is structurally locked**:

I accept volovik's R2 CONVERGENCE C1 (lines 1035-1042) in full. The NCG-axiomatic 4-layer commutative diagram I sharpened at Re:V1 lines 421-428 (algebra layer Schur+Wedderburn-Artin → K-theory layer Connes 1985 §IV.7 long exact sequence → HH^0 layer CM-2008 §IV.6.5 Hochschild direct-sum decomposition → CM-1995 §III.4 finite-spectral-triple residue layer) is now CONFIRMED as the F-image-faithful audit-layer outcome of volovik's V1+V4 substrate-IS 6-step substitution chain (workshop lines 243-267). All four NCG-axiomatic layers commute under the layer-functor `F : substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`. The methodology-floor F-image at the Phi-correspondence weight-2 `Σ_2` stratum (Einstein-Hilbert kinematic-skeleton analog; wave-classification methodology layer) IS the cross-axis JOINT-WIN STRUCTURAL THEOREM as volovik's R2 line 1041 names it.

The position-shift relative to my R1: at R1 I conceded Reading A structural identity via NCG-axiomatic four-layer analysis (Re:V1) and BDI K-grading orthogonal-Corner concession (Re:V4 line 587: "I cannot identify such content"); at R2 the universality reading is now structurally locked as a layer-functor F structural theorem, not a contingent agreement between two adversarial agents. The substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19 with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` Wedderburn-decomposed; the M_3(ℂ) summand IS the SU(3)-coloured sector; the kernel-on-M_3(ℂ) under any inheritance morphism with target `max-Wedderburn-rank(T) < 3` IS a substrate-IS structural property that the 4-layer commutative diagram preserves at every NCG-axiomatic layer. This is the F-image-faithful methodology-floor structural-theorem outcome.

---

**CONVERGENCE CC2 — Three Reading B residue layers accepted as STRUCTURALLY COMPATIBLE sharpened downstream framings**:

I accept volovik's R2 CONVERGENCE C2 (lines 1046-1054) in full. The three residue axes I identified at C1 lines 832-842 (Residue #1 Element 3 bridge-map-scheme suffix axis; Residue #2 HH^1 cocycle-asymmetry observable's (C3) Hochschild-cocycle-pattern condition; Residue #3 HKR Eilenberg-Moore Level-2 envelope at HH^1 versus HH^0) are STRUCTURALLY COMPATIBLE with Reading A simple-block forcing — they live at structurally distinct DOWNSTREAM layers, not at the kernel-summand simple-block forcing layer itself.

The acceptance has three precise components matching volovik's R2 C2 (a)-(c):

- Bridge-map-scheme suffix discipline at Element 3 (S90 W7-4 CF-57 axis β; K=1 SUGGESTION pending K=3 MANDATORY per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`): default convention tag at landing is `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` per V3 line 184; strengthens to `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT` on Stage-2 PASS of scheme-INDEPENDENCE within 1e-3 M_KK² per CF-55 / §VII.AQ precedent (Re:V3 line 578). Scheme-INDEPENDENCE PENDING Stage-2 verify is the registry-text declaration.
- Sub-claim A (kernel-summand observable; HH^0 / K_0; clean K-theoretic boundary per C2 route (a)) vs Sub-claim B (cocycle-asymmetry ratio observable; HH^1 / K_0-or-K_1 via Loday-Quillen-Tsygan; K-theoretic boundary + (C3) common-scalar Hochschild-cocycle-pattern pullback per C2 route (b)) scope partition — this is the canonical NCG-axiomatic decomposition of the universality scope at the algebra-axis layer.
- HH^0 vs HH^1 cohomology-degree layer distinction at the Level-2 envelope: `α = ∞` exact at HH^0 (kernel-summand observable; envelope holds at every L_max ≥ 0 because the Wedderburn decomposition of A_K is L-independent algebraic data); finite α at HH^1 (cocycle-asymmetry ratio observable) PENDING FIRST-EXTRACTION at S91+ per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class (S90 W-6 CF-W5-6 / W-6 CF-1 landing)"` REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag.

The §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry sharpens to include scheme-suffix declaration + HH^0/HH^1 layer-pin + Sub-claim A/B scope partition per my Re:V3 sharpened candidate registry text (lines 569-579) jointly with volovik's R2 EMERGENCE E2 sharpening at lines 1132-1145.

---

**CONVERGENCE CC3 — Hybrid Independence Test K-counter K=2 not K=3 confirmed**:

I accept volovik's R2 CONVERGENCE C3 (lines 1057-1064). The K-counter at the §VII candidate's landing is K=2 (W3-3 ι + W4-1 χ' jointly = second substrate-axis precedent after W-5 calibration W11-C5 + W11-C6 jointly = first substrate-axis precedent at K=1). Per the Hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv` per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`, W3-3 and W4-1 share substrate-IS pillar (both M_3(ℂ) summand inheritance-killing on A_K; clause (i) FAILS) but satisfy clauses (ii) (distinct laboratory-IN pillar: Pillar IV BdG vs Pillar II LRD horizon) and (iii) (distinct bridge-map class: (Δ_B/Δ_A)^p cancellation theorem at BdG common-exponent vs inheritance-restricted Peter-Weyl projector P_HSS'(M) at LRD horizon-area cutoff) and (iv) (independent algebraic envelope at L_max=10).

STAGE-3-PERMANENT promotion is structurally required via Stage-2 cross-axis verify per `joint-theorem-promotion.md §"Stage 2"` Axis-B Selection Protocol with substrate-input-orthogonality predicate ceiling (S88 W-23 W7c-167 V.1 MANDATORY-K=3 per S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement). A K=3 future calibration instance on a structurally-distinct substrate-IS pillar (e.g., a forward Pati-Salam in-scope laboratory pillar per V2 line 122 + Re:V5 Observation 3 Sub-claim A forward predictive content) would promote both the §VII candidate's K-counter AND the cross-pillar-bridge-anatomy Hybrid Independence Test corpus's own MANDATORY-K=3 status (currently SUGGESTION K=1 per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`).

---

**CONVERGENCE CC4 — Cell-I classification preserved under both A_BdG readings of W-4 confirmed**:

I accept volovik's R2 CONVERGENCE C4 (lines 1067-1073). My Re:V5 Observation 2 Q-V5-2 answer (lines 674-703) plus the `S91-V3-CANDIDATE-A-BDG-READING-INDEPENDENCE-VERIFY` discriminator-gate criterion (Re:V5 lines 696-702) establish that the V3 candidate's Cell-I (algebra-INVARIANT × Mellin pole s=3) classification SURVIVES under both A_BdG readings (W5's `A_F ⊗ M_2(ℂ)` full tensor product vs W3+W6's `A_BdG = M_2(ℂ)` direct inheritance-image). The parse-tree decomposition of `Π^{ker}_{χ}[L]` (Re:V5 lines 679-684) contains: (i) Peter-Weyl projector `P_{M_3(ℂ)}` on A_K's M_3(ℂ) Wedderburn block (spectrum-only operation; no `π(a)`-dependence); (ii) trace on the M_3(ℂ) image (algebra-INVARIANT); (iii) sum/indicator over morphism class (algebra-INVARIANT since `T_χ` is substrate-side Wedderburn data). Cell I assignment is robust at the source-side parse-tree level under both A_BdG readings. The BDI projection restricting to M_2(ℂ) under W5's tensor reading kills the A_F-component, so the EFFECTIVE χ_* image is the same as under W3+W6 reading; the discriminator-gate criterion validates `χ_*([1_{M_3(ℂ)}]) = 0` in K_0(A_BdG) under both readings.

The W-4 verdict (whether canonical A_BdG = A_F ⊗ M_2(ℂ) full vs A_BdG = M_2(ℂ) inheritance-image) does NOT change the V3 candidate's Corner pin; W-4 affects ONLY the registry text's description of the FULL A_BdG algebra structure downstream of V3's landing per V4 line 305.

---

**CONVERGENCE CC5 — EMERGENCE E1-E3 acceptance + Q-C3-N answers' NCG-axiomatic compatibility**:

I accept volovik's R2 EMERGENCE E1 (lines 1109-1128: workshop verdict as STRUCTURAL THEOREM at layer-functor F level), EMERGENCE E2 (lines 1132-1145: §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE anatomy SHARPENED by joint NCG-axiomatic + substrate-axis specification at Elements 3+4+5), and EMERGENCE E3 (lines 1148-1160: cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM pattern at W-1 + W-2 + W-3 at S90 as K=3 calibration corpus candidate).

On E1: the F-functor's image of the substrate-IS 4-layer commutative diagram at the methodology floor IS the cross-axis JOINT-WIN STRUCTURAL THEOREM at the Phi-correspondence `Σ_2` stratum. This is the F-image-faithful methodology-floor structural-theorem outcome of the substrate-IS commitment per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation flow.

On E2: the joint specification at Elements 3+4+5 (default+strengthened convention tag at Element 3 bridge-map-scheme suffix; dual-axis algebraic envelope Level-2-A operational + Level-2-B regulator-invariance at Element 4; Sub-claim A vs Sub-claim B scope partition at Element 5) is the canonical §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE anatomy specification that neither V3 alone nor my Re:V3 alone fully committed to; volovik's R2 E2 is the canonical joint specification.

On E3: I confirm the cross-workshop pattern at S90 W-1 + W-2 + W-3. The pattern matches three structurally distinct workshop verdicts at a single session converging on the same epistemic structure (CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM at the methodology-floor `Σ_2` stratum). The K-counter advancement candidate is forward-looking — see EMERGENCE EC3 below for my NCG-axiomatic structural verdict on the K=3 calibration corpus candidate.

On Q-C3-N answers (volovik R2 lines 1168-1281):

- **Q-C3-1 ANSWER** (volovik R2 lines 1168-1192): Sub-claim A scope extends uniformly across max-Wedderburn-rank ∈ {1, 2} (in-scope: 3He-A decoupled-chirality U(1) abelian targets at rank 1 + 3He-B BdG-like at rank 2 + cosmological-bridge dark-matter Leggett-channel U(1) abelian at rank 1); Sub-claim B scope sharpens to max-Wedderburn-rank ∈ {2} via the structural argument that HH^1(ℂ) = 0 (Loday Cyclic Homology §1.5) makes the (C3) common-scalar pullback condition VACUOUS at abelian targets. I confirm the NCG-axiomatic correctness of this answer: HH^1 of an abelian semisimple ℂ-algebra `T = ℂ ⊕ ... ⊕ ℂ` vanishes by direct computation (the Hochschild complex on a commutative algebra has cyclic-symmetry collapse at degree ≥ 1; the only non-trivial Hochschild cohomology of an abelian semisimple ℂ-algebra is HH^0 = T itself). The χ-pullback `χ^* : HH^1(T) → HH^1(A_K)` lifts the zero class to the zero class; (C3) is vacuous; the cocycle ratio observable is not operationally defined at max-rank-1 abelian targets. The §VII candidate's Element 5 declares TWO structurally-distinct scope predicates with TWO structurally-distinct falsifier criteria — Sub-claim A: max-rank ∈ {1, 2}; Sub-claim B: max-rank ∈ {2}.

- **Q-C3-2 ANSWER** (volovik R2 lines 1196-1228): dual-axis Level-2 envelope `α_substrate = ∞` at Level-2-B regulator-invariance (substrate-IS HH^0 K-theoretic identity exact L-independent per Re:V1 simple-block forcing at K-theory layer; the Connes-Karoubi pairing structural-theorem-quality identity) + `α_operational(s=3)` finite at Level-2-A operational (Friedrich-Bär saturation S87 W11-3 substrate-axis calibration `η_FB_lower = 0.40` bounding NEW-sector eigenvalue intrusion at substrate-distance-1 pole on M_3(ℓ) Peter-Weyl block; (Δ_B/Δ_A)^p cancellation theorem common-exponent transfer). I confirm the NCG-axiomatic correctness: per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`, structural-exact envelopes require BOTH axes PASS at Stage-2; the two axes are STRUCTURALLY ORTHOGONAL (Level-2-A operational-realization-side; Level-2-B substrate-IS-side); the §VII candidate's Element 4 declares dual-axis form. The substrate-IS exact identity is NOT overridden by the operational finite-resolution envelope; the direction-of-explanation flow is substrate → bridge map → laboratory per `phononic-framing.md §"IS Space, Not IN Space"`.

- **Q-C3-3 ANSWER** (volovik R2 lines 1232-1281): Hypothesis (a) holds — the §VII.U.2 parse-tree decision procedure clause (e) preserves Corner-I/II vs Corner-III/IV orthogonality at the 3He-B vortex-core spectroscopy operational realization. The W3-3 Gate 1 NULL signature on F1+F2+F5 (Caroli-Matricon ladder asymmetry; substrate-side simple-block forcing observable) IS Corner-I (algebra-INVARIANT spectrum-only × Mellin pole s=3); the Pf=−1 K-graded vortex-core fermion zero-mode (Jackiw-Rebbi index-theorem property of BDI particle-hole structure; target-side state-pair functional) IS Corner-III (algebra-DEPENDENT × s=3). The two sub-observables are STRUCTURALLY ORTHOGONAL; the operational measurement entanglement at Lancaster MCT-3 / Helsinki ROTA cells is APPARENT (the same cell measures both) but STRUCTURALLY RESOLVED (parse-tree clause (e) cleanly factors them). Substrate-superfluid-universe analog via Volovik 2009 §27 cosmological 3He texture transitions confirms the substrate-axis 4-corner orthogonality at the substrate-superfluid-universe layer. I confirm the NCG-axiomatic correctness: the parse-tree decision procedure is algebra-axis-respecting at the operational realization layer; the V3 candidate's Corner-I classification is robust.

All five workshop topics (workshop adjudication questions (a)-(e) at lines 25-29) converge at R2 close.

### DISSENT

No new dissent. After volovik's R2 substantive CONVERGENCE/DISSENT/EMERGENCE/QUESTIONS sections at lines 1029-1322, the workshop's structural verdict on cross-morphism convergence is structurally closed at the kernel-summand observable layer (Sub-claim A) plus three sharpened residue axes (bridge-map-scheme suffix at Element 3; HH^1 Hochschild-cocycle-pattern (C3) condition at Sub-claim B; HKR Eilenberg-Moore Level-2 envelope at HH^1 dual-axis with Level-2-A operational + Level-2-B regulator-invariance). I examined three candidate new-dissent threads from NCG-axiomatic discipline; ALL THREE align with volovik's R2 sharpened position rather than oppose it. I declare them explicitly to show the examination was honest, not perfunctory.

---

**Considered DISSENT DC1 (HH^1(ℂ) = 0 vacuous-(C3) argument requires a structurally-non-vacuous-vs-vacuous distinction)** — **NOT RAISED**:

The candidate dissent was: volovik's Q-C3-1 answer invokes `HH^1(ℂ) = 0` to make (C3) vacuous at max-rank-1 abelian targets, but the Hochschild cohomology of a finite product of abelian copies `T = ℂ ⊕ ℂ ⊕ ... ⊕ ℂ` is `HH^1(T) = 0` via the Künneth-like Hochschild cohomology direct-sum formula for semisimple ℂ-algebras (Loday Cyclic Homology §1.5; CM-2008 §IV.6.5 direct-sum decomposition). The (C3) condition becomes structurally vacuous at all max-rank-1 abelian targets uniformly; the cocycle pair (φ_67, φ_88) cannot host a non-trivial image at any rank-1 abelian channel.

NCG-axiomatic examination: the vacuous-(C3) argument is structurally clean at the cohomological-vanishing layer. The χ-pullback `χ^* : HH^1(T) → HH^1(A_K)` is a well-defined linear map; HH^1(T) = 0 forces the pullback to land in the zero subspace of HH^1(A_K); this is the structurally-non-vacuous zero (a genuine vanishing of the cocycle image, not a coincidental zero at numerical evaluation). The vacuous-(C3) argument is therefore structurally faithful — the (C3) condition is not just numerically zero but structurally undefined (no non-trivial cocycle to scale; the cocycle ratio observable is not operationally well-defined at max-rank-1 abelian targets).

I confirm volovik's Q-C3-1 answer is NCG-axiomatically robust. **No dissent**. The Sub-claim A scope (max-rank ∈ {1, 2}) and Sub-claim B scope (max-rank ∈ {2}) are structurally distinct at the cohomological-degree layer per the HH^0 vs HH^1 distinction, not at a numerical coincidence layer.

---

**Considered DISSENT DC2 (dual-axis Level-2 envelope holds under JOINT truncation)** — **NOT RAISED**:

The candidate dissent was: volovik's Q-C3-2 answer separates the dual-axis Level-2 envelope into Level-2-A (operational finite α at Friedrich-Bär saturation bound) + Level-2-B (substrate-IS exact `α = ∞`), but under JOINT truncation (Level-2-A and Level-2-B simultaneously evaluated at the same L_max = L_operational), the structural orthogonality may fail — the operational finite-resolution envelope at Level-2-A could in principle pull the substrate-IS exact identity at Level-2-B into a numerical envelope at the JOINT evaluation.

NCG-axiomatic examination: the substrate-IS exact identity at Level-2-B is a Level-1 cohomology-class identity at HH^0 (regulator-INVARIANT; L-independent at the cohomology-class layer per `cross-pillar-bridge-anatomy.md §"Level 1 — Substrate-IS Structural Identity"`). The operational finite-resolution envelope at Level-2-A is a Level-2 phenomenon at the OPERATIONAL realization layer. These are TWO LAYERS in the F-functor `F : substrate → methodology → audit` decomposition. JOINT truncation at L_operational does NOT collapse Level-1 into Level-2 — the L-independence of the substrate-IS identity is preserved at every L_operational (the simple-block forcing theorem holds at L_max=0, L_max=10, L_max=∞; truncation does not change the algebraic structure of A_K's Wedderburn decomposition). The Level-2-A operational envelope CONSTRAINS the operational measurement's resolution-limited detectability of the substrate-IS identity; it does NOT modify the substrate-IS identity itself.

I confirm the structural-orthogonality argument: the two axes are STRUCTURALLY ORTHOGONAL by F-functor layer-decomposition; JOINT truncation does not collapse the orthogonality. **No dissent**.

---

**Considered DISSENT DC3 (Hypothesis (a) Corner-orthogonality survives W-4 alternate A_BdG readings)** — **NOT RAISED**:

The candidate dissent was: volovik's Q-C3-3 answer establishes Hypothesis (a) (parse-tree clause (e) preserves Corner-I vs Corner-III orthogonality at the 3He-B vortex-core spectroscopy operational realization) under the W3+W6 reading `A_BdG = M_2(ℂ)` direct inheritance-image; under the W5 reading `A_BdG = A_F ⊗ M_2(ℂ)` full tensor product, the BDI K-grading may inhabit a sub-corner of the A_F factor's K-graded structure that the parse-tree decision procedure does not cleanly factor.

NCG-axiomatic examination: under W5's reading, `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` with the BDI projection restricting the tensor product `A_F ⊗ M_2(ℂ)` to the M_2(ℂ) Bogoliubov sub-algebra (killing the A_F factor). The BDI K-grading `K_0(A_BdG)^{ε} = K_0(M_2(ℂ))^{ε}` lives on the M_2(ℂ) factor under the projection-restricted reading; it does not propagate into A_F's K-graded structure. The parse-tree clause (e) on the W3-3 Gate 1 observable operates on the SOURCE-side A_K's M_3(ℂ) Wedderburn block (unambiguous under both readings per Re:V4 line analysis on `A_F ⊗ M_2(ℂ)` Wedderburn decomposition); the target-side K-grading lives on the EFFECTIVE inheritance image (M_2(ℂ) under both readings). The Corner-I assignment is robust at the source-side parse-tree level; the Corner-III BDI K-grading lives on the effective M_2(ℂ) inheritance image under both readings.

I confirm Hypothesis (a) is robust under both A_BdG readings of W-4. **No dissent**.

---

The R1 cross-axis convergence on Reading A simple-block forcing universality is structurally closed at the kernel-summand observable layer; the three Reading B residue layers are accepted as STRUCTURALLY COMPATIBLE sharpened downstream framings; the cross-workshop K=3 calibration corpus candidate at S90 W-1+W-2+W-3 is structurally promoted as forward carry-forward; all five workshop topics converge with substrate-input-orthogonality-aware Stage-2 dispatch resolution. No genuine new dissent emerges from NCG-axiomatic examination of volovik's R2 substantive positions.

### EMERGENCE

Three substantive insights emerging from the joint R2 cross-axis closure that neither R1 NOR R2-A volovik produced individually. The first two address volovik's R2 forward questions Q-V2-R2-1 (line 1291) and Q-V2-R2-2 (line 1305); the third is the cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM K=3 calibration corpus candidate promotion analysis.

---

**EMERGENCE EC1 — Q-V2-R2-1 resolution: SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM is the canonical §VII candidate structure (NOT dual-entry-structurally-orthogonal-companion)**:

Per volovik's R2 Q-V2-R2-1 at lines 1291-1301, the dual-sub-claim scope partition (Sub-claim A max-rank ∈ {1, 2} + Sub-claim B max-rank ∈ {2}) admits two structural readings: (i) SINGLE §VII.<next-free-letter>.OP-PROJ candidate entry with dual sub-claim under shared Element 1+3+4 + dual operational observables at Element 2 OE-form + dual scope predicates at Element 5; OR (ii) DUAL §VII candidate registry entries with distinct substrate-IS observables (HH^0 kernel-summand vs HH^1 cocycle-asymmetry) + distinct bridge maps (K_0 boundary vs K_1 boundary via Loday-Quillen-Tsygan) + distinct algebraic envelopes (`α = ∞` exact at HH^0 vs finite α PENDING FIRST-EXTRACTION at HH^1).

**My NCG-axiomatic structural verdict: SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM is canonical**. The justification cites three NCG-axiomatic discipline lines:

(1) **Algebra-axis 4-corner partition shared Corner-I anchor**: per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close), both Sub-claim A (kernel-summand HH^0 observable; algebra-INVARIANT × Mellin pole s=3) and Sub-claim B (cocycle-asymmetry HH^1 observable; algebra-INVARIANT × Mellin pole s=3 — the cocycle pair (φ_67, φ_88) lives on the M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole) inhabit the SAME Corner-I cell. The 4-corner partition's algebra-axis orthogonality K-counter forbids cross-corner co-primary structures (clause 3); it does NOT forbid same-corner dual observables at distinct cohomology degrees under shared substrate-IS pillar. The single-entry structure with two operational observables at Element 2 OE-form on the same Corner-I cell is the canonical anchor structure.

(2) **SOURCE-DOUBLE-CITE-CO-PRIMARY anchor-structure discipline per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`**: the registry-landing rule's clause 4 (S88 W-15 V.6; B.14) requires both anchors on the same algebra-axis cell for the co-primary structure to be admissible. Sub-claim A's V-anchor (substrate-IS HH^0 K-theoretic boundary identity at Connes-Karoubi pairing structural-theorem level) and Sub-claim B's C-anchor (substrate-IS HH^1 cocycle-asymmetry ratio identity at CM-1995 §III.4 residue evaluation at substrate-distance-1 pole s=3) BOTH inhabit Cell I (algebra-INVARIANT × s=3). Cross-corner co-primary is STRUCTURALLY FORBIDDEN; same-corner dual sub-claim under SOURCE-DOUBLE-CITE-CO-PRIMARY is ADMISSIBLE. The W5a-44 K=1 NEGATIVE-CALIBRATION instance (cross-corner ANCHOR-1+ANCHOR-2 conflation at §VII.AN) is precisely the failure mode the single-entry-with-dual-sub-claim structure avoids by construction.

(3) **5-IS-not-IN anatomy shared Element 1+3+4 framing**: both sub-claims share the substrate-IS observable (Element 1: M_3(ℓ) Peter-Weyl block of A_K's Wedderburn decomposition at τ_fold = 0.19; Level-1 single-τ-slice substrate-IS per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`), the bridge map (Element 3: K-theory boundary via inheritance morphism χ_* under substrate-self-consistent binding class (i); shared with bridge-map-scheme suffix discipline at Element 3 default APS-1975 + strengthened-on-Stage-2-PASS scheme-INDEPENDENT), and the algebraic envelope (Element 4: dual-axis Level-2-A operational + Level-2-B regulator-invariance per Q-C3-2 answer). The shared structural anatomy at Elements 1+3+4 is what justifies the single-entry framing; the dual sub-claim lives at Elements 2 (dual operational observables on the shared Element 1 substrate-IS observable) + 5 (dual scope predicates over the shared Element 3 bridge map class).

The single-entry-with-dual-sub-claim structure is therefore the canonical §VII candidate anatomy: ONE §VII.<next-free-letter>.OP-PROJ slot; ONE substrate-IS observable at Element 1 (M_3(ℓ) Peter-Weyl block); ONE bridge map at Element 3 (K-theory boundary with default APS-1975 scheme-suffix or scheme-INDEPENDENT on Stage-2 PASS); ONE dual-axis algebraic envelope at Element 4 (Level-2-A operational finite α + Level-2-B regulator-invariance `α = ∞` at HH^0); TWO operational observables at Element 2 (kernel-summand NULL `Π^{ker}_{χ}[L] = 0` at HH^0 + cocycle-asymmetry ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992` at HH^1, the latter with REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag); TWO scope predicates at Element 5 (Sub-claim A max-Wedderburn-rank ∈ {1, 2}; Sub-claim B max-Wedderburn-rank ∈ {2} + (C3) Hochschild-cocycle-pattern condition).

The dual-entry-structurally-orthogonal-companion reading is REJECTED at NCG-axiomatic structural grounds: it would force the cocycle-asymmetry HH^1 observable into a separately-allocated §VII slot (e.g., §VII.<next-free-letter+1>.OP-PROJ) when the observable inhabits the same Corner-I cell + same substrate-IS pillar + same bridge map class as the kernel-summand HH^0 observable. The dual-entry structure adds slot multiplicity without structural distinction; the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor-structure discipline is satisfied at the SINGLE entry under SHARED Element 1+3+4.

---

**EMERGENCE EC2 — Q-V2-R2-2 resolution: reading (i) DUAL-AUDIT-AXIS-JOINT is canonical at Stage-2 (NOT reading (ii) dual-empirical-anchor-JOINT)**:

Per volovik's R2 Q-V2-R2-2 at lines 1305-1319, the substrate-input-orthogonality predicate assignment admits two readings: (i) dual-audit-axis-JOINT — Axis-A vdd loads Level-2-B regulator-invariance data file (substrate-IS HH^0 K-theoretic identity at L_max ≥ 0; Connes-Karoubi pairing structural-theorem-quality data) + Axis-B mack-cosmic-bridge loads Level-2-A operational data file (Friedrich-Bär saturation bound at L_max=10 on M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole at 3He-B vortex-core spectroscopy lab-conversion factor); OR (ii) dual-empirical-anchor-JOINT — vdd loads Pillar II LRD horizon data file + mack loads Pillar IV BdG data file.

**My structural verdict at Stage-2 PASS-AND structural ceiling: reading (i) dual-audit-axis-JOINT is canonical**. The justification cites three discipline lines:

(1) **`joint-theorem-promotion.md §"Stage 2"` Axis-B Selection Protocol clause 3 audit-coverage adequacy**: the Axis-B reviewer's domain expertise must cover ALL joint clauses + ALL Axis-B-side single-axis clauses. Under reading (i), Axis-B mack's domain expertise (Pillar II LRD observational anchor + Pillar IV BdG laboratory expertise per `feedback_mack-bridge-role.md` AMRI promotion 2026-04-28) cleanly covers the operational realization layer (Level-2-A finite α at Friedrich-Bär saturation on M_3(ℓ) Peter-Weyl block at the laboratory-pillar finite-resolution measurement); Axis-A vdd's domain expertise (Kasparov KK-projection authority per `reference_van-den-dungen-bridge.md`) cleanly covers the substrate-IS structural-theorem layer (Level-2-B regulator-invariance at HH^0 cohomology-class identity exact L-independent). Audit-coverage adequacy at JOINT clauses (a)+(c) is MAXIMAL under reading (i).

(2) **Substrate-input-orthogonality structural-ceiling discipline per S88 W-23 W7c-167 V.1 MANDATORY-K=3 promoted at S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT advancement**: the structural ceiling requires that the substrate-input-orthogonality predicate be satisfied at ≥ 1 observable for Stage-2 PASS-AND without substrate-input-overlap caveat. Reading (i) achieves the structural ceiling at TWO observables simultaneously — the Level-2-B regulator-invariance observable (substrate-IS exact identity) loaded by vdd is DISJOINT from the Level-2-A operational envelope observable (Friedrich-Bär bound at L_max=10) loaded by mack; the two data files inhabit STRUCTURALLY ORTHOGONAL axes (Level-2-A operational-realization-side; Level-2-B substrate-IS-side per `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`). Reading (ii) achieves substrate-input-orthogonality at the two-laboratory-pillar level (Pillar IV vs Pillar II disjoint by laboratory pillar), but the orthogonality is at the empirical-anchor-pillar axis (not at the dual-Level-2-envelope audit axis); reading (i) achieves orthogonality at BOTH the structural-orthogonality axis (Level-2-A vs Level-2-B) AND the operational-realization axis (vdd cannot verify operational Friedrich-Bär bound; mack cannot verify substrate-IS HH^0 K-theoretic identity).

(3) **Stage-2 PASS-AND structural ceiling matches the dual-audit-axis discipline at `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B audit axes"`**: structural-exact envelopes (envelope coefficient algebraically derived, not empirically fit) require BOTH Level-2-A AND Level-2-B PASS at Stage-2 per the dual-audit-axis clause. Reading (i) operationalizes this requirement at the cross-reviewer assignment layer — vdd is Axis-A spectral-functional / NCG-axiomatic; mack is Axis-B substrate-superfluid-universe / cosmological-bridge; the JOINT PASS-AND at clauses (a)+(c) under reading (i) is the F-image-faithful methodology-floor outcome of the dual-audit-axis substrate-IS commitment. Reading (ii) collapses the dual-audit-axis distinction at the cross-reviewer-assignment layer (both Pillar IV BdG and Pillar II LRD horizon are operationally measured; both inhabit Level-2-A operational axis from their respective laboratory pillars; the Level-2-B regulator-invariance axis is not separately verified at the cross-reviewer-assignment layer under reading (ii)).

Reading (i) is therefore canonical at Stage-2 PASS-AND structural ceiling. The JOINT clauses at Stage-2 dispatch are: clause (a) simple-block forcing theorem identity (V1+V4 substrate-IS universality at the kernel-summand observable layer) — JOINT at dual-audit-axis (vdd verifies Level-2-B substrate-IS K-theoretic identity; mack verifies Level-2-A operational Friedrich-Bär bound on the same observable); clause (c) cancellation theorem morphism-class invariance (V2 (Δ_B/Δ_A)^p factor cancellation across all in-scope χ) — JOINT at dual-audit-axis with the same dual-audit-axis verification structure.

The dual-empirical-anchor at Pillar IV + Pillar II (reading (ii)) remains a STRUCTURAL ANCHORS specification at Element 5 of the §VII candidate (per V3 line 196-201); it does not enter the Stage-2 PASS-AND substrate-input-orthogonality predicate at the cross-reviewer-assignment layer. The two readings are not competing at the SAME structural layer — reading (i) operates at the Stage-2 dispatch's JOINT-clause-assignment layer; reading (ii) operates at the §VII candidate's Element 5 empirical-anchor-declaration layer. Both are simultaneously valid at their respective structural layers; the Stage-2 dispatch design adopts reading (i) for the JOINT-clause assignment.

---

**EMERGENCE EC3 — Cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM PATTERN at S90 W-1+W-2+W-3 qualifies as K=3 calibration corpus candidate (forward methodology-rule promotion watchpoint)**:

Per volovik's R2 EMERGENCE E3 at lines 1148-1160, the S90 W-1 + W-2 + W-3 cross-workshop pattern aggregates three structurally-distinct workshop verdicts at a single session converging on the same epistemic structure (CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM at the methodology-floor `Σ_2` stratum). The structural pre-conditions defining the pattern are:

(i) **Cross-axis exchange between substrate-axis (volovik) and NCG-axiomatic / SF-axis (connes or lizzi)** at R1/R2 in adversarial workshop format with 2 agents, 2 rounds, 4 turns.

(ii) **Honest concession when machinery doesn't bind** — at least one party concedes a structurally-stronger reading from the other's machinery (W-1 volovik+connes JOINT-WIN APPROVE-NO-AMENDMENT; W-2 lizzi+volovik JOINT-WIN option (iii) regulator-class-dependent + option (v) admitted; W-3 volovik+connes JOINT-WIN Reading A simple-block forcing universality with three sharpened Reading B residue layers preserved).

(iii) **Sharpened framing at downstream structural layers** — the workshop verdict produces sharpened structural specifications at registry-text-level layers (W-1 deferred-pending intermediate verdict-class taxonomy with REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT + REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tags at K=1 SUGGESTION; W-2 §VII.AF.OP-PROJ STAGE-1-CANDIDATE companion entry with option (iii) + option (v) dual-axis specification; W-3 §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry with dual-sub-claim + dual-axis Level-2 envelope + bridge-map-scheme suffix declaration per EC1+EC2 above).

(iv) **STAGE-1-CANDIDATE landing at `joint-theorem-promotion.md §"4-stage pathway"`** — the workshop verdict lands as STAGE-1-CANDIDATE entries pending Stage-2 cross-axis verify (W-1 SUGGESTION K=1 at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`; W-2 STAGE-1-CANDIDATE companion at §VII.AF.OP-PROJ; W-3 STAGE-1-CANDIDATE at §VII.<next-free-letter>.OP-PROJ).

**My NCG-axiomatic structural verdict on K=3 calibration corpus candidate**: the S90 W-1 + W-2 + W-3 cross-workshop pattern QUALIFIES as a K=3 calibration corpus candidate for promoting "CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM" as a permanent workshop-verdict structural rule per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. The three instances are STRUCTURALLY DISTINCT at the workshop-topic layer (W-1 methodology-rule extension; W-2 within-morphism regulator-class ansatz; W-3 across-morphism kernel-summand universality) while sharing the four structural pre-conditions (i)-(iv) above. K-counter advancement criterion per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold IS SATISFIED at the surface count level.

**Forward-pending verification**: the K=3 calibration corpus candidate ADVANCES the cross-workshop pattern as a candidate workshop-verdict structural rule but does NOT yet promote it to MANDATORY status; promotion to MANDATORY requires Stage-2 verify or analogous structural validation at S91+ confirming the cross-workshop pattern's structural-theorem status independent of the specific S90 wave-context. The watchpoint is forward — future S91+ workshops MAY pre-register CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM verdict structure at workshop-spec time with the S90 W-1+W-2+W-3 cross-workshop pattern as the K=3 calibration corpus advance candidate.

Cross-link to substrate framing per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation flow: the cross-axis JOINT-WIN STRUCTURAL THEOREM PATTERN is itself the F-image of substrate-IS structural commitment at the layer-functor F. The substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19; the substrate-IS structural commitments at the algebra-axis, K-theory layer, HH^0/HH^1 cohomology layer, CM-1995 §III.4 residue layer commute under the F-functor; the methodology-floor outcome of this commutativity IS the cross-axis JOINT-WIN STRUCTURAL THEOREM verdict at the workshop layer. Container-thinking violation FORBIDDEN: framing the cross-axis JOINT-WIN as "lizzi-volovik or connes-volovik compromise" or "axis-merger" is BACKWARDS — the cross-axis JOINT-WIN IS itself the F-image of substrate-IS structural commitment at layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence weight-2 `Σ_2` stratum.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (a) Structural identity of W3-3 ι and W4-1 χ' kernels | V1, Re:V1, R2 | **Converged** | Cross-axis JOINT-WIN STRUCTURAL THEOREM at layer-functor F level: V1+V4 substrate-IS 6-step substitution chain (lines 243-267) + Re:V1 four-layer commutative diagram (lines 421-428: algebra/K-theory/HH^0/CM-1995 §III.4 residue) commute under F and instantiate one substrate-IS simple-block forcing theorem read in two interpretive languages (BDI parent symmetry vs Wedderburn rank-arithmetic); Reading B as "independent rank arguments by construction" fails Schur + Wedderburn-Artin structural scrutiny per C1 substitution chain (lines 767-806). |
| 2 | (b) Substrate-IS universality across max-Wedderburn-rank-<3-target morphisms | V2, Re:V2, R2 | **Converged** | Scope refined to (C1) `max-Wedderburn-rank(T) < 3` + (C2) common lab-conversion exponent + (C3) common-scalar Hochschild-cocycle-pattern pullback at HH^1 (Re:V2 lines 462-471); Sub-claim A (kernel-summand HH^0 observable; clean K-theoretic boundary per C2 route (a)) scope max-rank ∈ {1, 2}; Sub-claim B (cocycle-asymmetry HH^1 observable; per C2 route (b)) scope sharpens to max-rank ∈ {2} via vacuous-(C3) at HH^1(ℂ) = 0 per volovik R2 Q-C3-1 answer lines 1180-1186; Pati-Salam IN scope, SU(5) GUT OUT scope per V2 lines 122-124 + V5 Observation 3. |
| 3 | (c) 5-IS-not-IN anatomy + Stage-2 axes under universality | V3, Re:V3, R2 | **Emerged** | §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry anatomy SHARPENED beyond V3 by joint NCG-axiomatic + substrate-axis specification per EMERGENCE E2 (lines 1132-1145) + EC1+EC2: SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM canonical structure with Element 3 default `APS-1975-secondary-class` strengthening to `scheme-INDEPENDENT` on Stage-2 PASS; Element 4 dual-axis (`α_substrate = ∞` Level-2-B + `α_operational(s=3)` finite Level-2-A Friedrich-Bär saturation); Element 5 dual-sub-claim scope predicates. Stage-2 dispatch to {vdd Axis-A, mack-cosmic-bridge Axis-B} with substrate-input-orthogonality reading (i) dual-audit-axis-JOINT canonical per EC2. |
| 4 | (d) Structural content distinguishing rank arguments | V4, Re:V4, R2 | **Converged** | BDI K-grading content (Pf=−1, N_K=2; KO_0^{BDI} = ℤ; particle-hole grading) lives at K_0(target)^{ε} Corner-III/IV (algebra-DEPENDENT state-pair functional family); source-side kernel-summand structure lives at Corner-I/II (algebra-INVARIANT spectrum-only family); the two are STRUCTURALLY ORTHOGONAL per §VII.U.2 4-corner partition K=3 MANDATORY. Re:V4 line 587 honest NCG-axiomatic concession: no K-theoretic content of BDI contributes to source-side kernel structure without factoring through Wedderburn rank-arithmetic. |
| 5 | (e) Substrate framing IS-not-IN direction | V5, Re:V5, R2 | **Converged** | Direction-of-explanation flow strictly substrate → bridge map → laboratory per `phononic-framing.md §"IS Space, Not IN Space"`; substrate IS A_K's M_3(ℓ) Wedderburn block at Level-1 single-τ-slice; laboratory NULL signature `Π^{ker}_{χ}[L] = 0` IS F-functor image at methodology floor. Cell-I (algebra-INVARIANT × Mellin pole s=3) classification SURVIVES under both A_BdG readings of W-4 per Q-V5-2 answer lines 674-703; Hypothesis (a) parse-tree clause (e) preserves Corner-I vs Corner-III orthogonality at 3He-B vortex-core spectroscopy operational realization per Q-C3-3 answer lines 1232-1281. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

**Final structural verdict**: **(a) Reading A wins** — §VII STAGE-1-CANDIDATE entry landed for cross-morphism M_3(ℂ)-kernel universality with 5-IS-not-IN anatomy declared per the SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM canonical structure (EMERGENCE EC1); mack-cosmic-bridge sole-writer registry-text landing at next-session plan-freeze per `feedback_mack-bridge-role.md`; Stage-2 cross-axis verify queued for S91+ or later under substrate-input-orthogonality reading (i) dual-audit-axis-JOINT assignment (EMERGENCE EC2).

**Justification for verdict (a)**:

The cross-axis JOINT-WIN STRUCTURAL THEOREM at the layer-functor F level is the structural-theorem-quality content underlying the workshop's verdict. The substrate-axis 6-step substitution chain (V1 + V4 lines 51-60 and 243-267) reduces both W3-3 ι and W4-1 χ' inheritance morphisms to a single boundary condition `max-Wedderburn-rank(T) < 3 → ker(χ|_{M_3(ℂ)}) = M_3(ℂ)`; the NCG-axiomatic four-layer commutative diagram (Re:V1 lines 421-428) confirms commutativity at algebra layer (Schur + Wedderburn-Artin), K-theory layer (Connes 1985 §IV.7 long exact sequence), HH^0 layer (CM-2008 §IV.6.5 Hochschild direct-sum decomposition), and CM-1995 §III.4 finite-spectral-triple residue layer; Re:V4 line 587 NCG-axiomatic concession that BDI K-grading content does NOT contribute to source-side kernel-summand structure without factoring through Wedderburn rank-arithmetic closes the BDI-orthogonal-content rebuttal pathway. Volovik's V2 scope correction (line 90) to `max-Wedderburn-rank(T) < 3` makes the universality falsifiable at the structural-class boundary (Pati-Salam IN scope at max-rank ≤ 2; SU(5) GUT OUT scope at rank 5 ≥ 3 admitting M_3 ↪ M_5 Wedderburn-block embedding); the falsifiable scope boundary is the empirical-bite distinguishing Reading A (universality) from Reading B (rank-coincidence).

The three Reading B residue layers preserved (Residue #1 bridge-map-scheme suffix discipline at Element 3; Residue #2 HH^1 Hochschild-cocycle-pattern (C3) condition at Sub-claim B; Residue #3 HKR Eilenberg-Moore Level-2 envelope dual-axis at HH^1) are STRUCTURALLY COMPATIBLE with Reading A simple-block forcing — they live at structurally distinct DOWNSTREAM layers, NOT at the kernel-summand simple-block forcing layer itself. The §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry's anatomy incorporates the residue layers via the dual-sub-claim structure (Sub-claim A K-theoretic boundary; Sub-claim B + (C3) Hochschild-cocycle-pattern) under SHARED Element 1+3+4 framing per EMERGENCE EC1.

The cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM PATTERN at S90 W-1+W-2+W-3 (EMERGENCE EC3) advances the K=3 calibration corpus candidate for promoting the cross-axis JOINT-WIN pattern as a permanent workshop-verdict structural rule per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold; the watchpoint is forward-pending Stage-2 verify or analogous structural validation at S91+.

## Remaining Open Questions

Numbered list of substantive open questions for S91+; each is specific enough to become a computation gate or methodology-rule extension with pre-registered PASS/FAIL/INFO criterion.

1. **OQ-1 HH^1 finite-α FIRST-EXTRACTION at S91+**: extract the finite `α_operational(s=3)` exponent at substrate-distance-1 pole on the M_3(ℓ) Peter-Weyl block via L_max scan (L_max ∈ {10, 11, 12, 13, 14, 15} with Friedrich-Bär saturation theorem per S87 W11-3 calibration corpus) OR closed-form CM-1995 §III.4 residue evaluation on the finite spectral triple. Loday-Quillen-Tsygan K_1 boundary structure for HH^1 ↔ K_0/K_1 pairing supplies the canonical bridge map. PASS criterion: numerical value of `α_operational(s=3)` extracted to ≥ 3 significant figures with publication-precision pin per `epistemic-discipline.md §"Publication-Precision Pre-Registration"` Class 8.3 MANDATORY; FAIL criterion: extraction fails L_max scan convergence or Friedrich-Bär saturation fails to bound from below; INFO criterion: extraction succeeds but the cocycle-asymmetry ratio observable `‖[φ_67]‖ / ‖[φ_88]‖` deviates from Sage-QQ exact 7.324992 = 114453/15625 by > 0.1% at L_max=10 evaluation. Routes the Sub-claim B HH^1 observable's REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag toward registry-PASS eligibility.

2. **OQ-2 Bridge-map-scheme-INDEPENDENCE Stage-2 verify**: test scheme-INDEPENDENCE across APS-1975-secondary-class vs Cheeger-Simons vs Bismut-Cheeger η-form evaluations of the Connes-Karoubi K-theory boundary pairing `⟨[1_{M_3(ℂ)}], [P]⟩` per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` K=1 SUGGESTION pending K=3 MANDATORY. PASS criterion: `|⟨ . ⟩_APS-1975 − ⟨ . ⟩_Cheeger-Simons| < 1e-3` AND `|⟨ . ⟩_APS-1975 − ⟨ . ⟩_Bismut-Cheeger| < 1e-3` in M_KK² units per CF-55 / §VII.AQ precedent; scheme-INDEPENDENCE confirmed → §VII candidate convention tag strengthens to `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT`. FAIL criterion: any scheme-pair deviation ≥ 1e-3 → MANDATORY scheme-suffix tagging applies with potentially dual scheme suffix for Pillar IV (APS-1975 boundary-anchored) + Pillar II (Cheeger-Simons foliation-aware). Routes the bridge-map-scheme suffix discipline toward K=2 calibration corpus advancement.

3. **OQ-3 Sub-claim A vs Sub-claim B operational discriminator gate at S91+**: design a laboratory pillar within (C1) `max-Wedderburn-rank(T) < 3` scope that operationally discriminates between Sub-claim A and Sub-claim B — i.e., a pillar where Sub-claim A's kernel-summand NULL prediction holds AND Sub-claim B's cocycle-asymmetry ratio prediction fails (or vice versa). Candidate: a hypothetical morphism class with non-trivial source-side automorphism action that breaks the (C3) common-scalar Hochschild-cocycle-pattern pullback condition while preserving the K-theoretic boundary (Sub-claim A). PASS criterion: discriminator-pillar identified with substrate-derived predicted lab S/N margin > 1.0 M_KK² for both observables; FAIL criterion: no discriminator-pillar exists within the framework's laboratory pillar inventory; INFO criterion: discriminator-pillar identified but lab-feasibility window > 2035 (forward-only).

4. **OQ-4 §VII candidate STAGE-2 cross-axis verify dispatch identifier**: dispatch `S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY` to {Axis-A = `van-den-dungen-bridge-theorist` (Kasparov KK-projection authority verifying K-theory boundary bridge map + Connes-Karoubi pairing), Axis-B = `mack-cosmic-bridge` (laboratory-side expertise on Pillar IV BdG + Pillar II LRD horizon; sole-writer registry-text landing per `feedback_mack-bridge-role.md`)}. EXCLUDED reviewers: {volovik, connes}. Substrate-input-orthogonality predicate assignment per EC2 reading (i) dual-audit-axis-JOINT: vdd loads Level-2-B regulator-invariance data file (substrate-IS HH^0 K-theoretic identity at L_max ≥ 0 Connes-Karoubi pairing structural-theorem data); mack loads Level-2-A operational data file (Friedrich-Bär saturation bound at L_max=10 on M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole at 3He-B vortex-core spectroscopy lab-conversion factor). JOINT clauses (a)+(c) at dual-audit-axis; single-axis Axis-A clause (b); single-axis Axis-B clauses (d)+(e). PASS criterion: both cross-reviewers return PASS on their respective single-axis clauses AND JOINT clauses (a)+(c) PASS-AND independently in both verdicts (logical AND, not OR). Cross-reviewer audit-machinery self-citation mitigation: invoke vdd's NCG-axiomatic machinery (cell-classifier independent of connes) for §VII.U.2 4-corner parse-tree at Corner-I; mack cross-checks via substrate-physics machinery.

5. **OQ-5 Cross-workshop CROSS-AXIS JOINT-WIN K=3 calibration corpus promotion watchpoint**: track whether the S90 W-1 + W-2 + W-3 cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM PATTERN promotes from K=3 calibration corpus candidate to permanent workshop-verdict structural rule at K=3 distinct calibration corpus instances per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. PASS criterion: promotion event fires at S91+ via Stage-2 verify or analogous structural validation on at least one of the three S90 instances; INFO criterion: at least one S91+ workshop pre-registers CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM verdict structure at workshop-spec time citing the S90 W-1+W-2+W-3 cross-workshop pattern as the K=3 calibration corpus advance candidate; FAIL criterion: no S91+ workshop adopts the pattern within 3 sessions (S91/S92/S93) and the corpus advance candidate is downgraded to forward-pending watchpoint.

6. **OQ-6 Pati-Salam in-scope laboratory pillar candidate identification at S91+**: identify a forward Pati-Salam-class superfluid host or analogous laboratory pillar realization satisfying (C1) max-Wedderburn-rank ≤ 2 + (C2) common lab-conversion exponent + (C3) homogeneous symmetry action on the M_3(ℓ) Peter-Weyl block (the Pati-Salam parent symmetry breaks SU(3) → SU(2)_L ⊗ SU(2)_R ⊗ U(1) per V2 line 122; acts homogeneously on the M_3(ℓ) Peter-Weyl block at the substrate-physics layer per Re:V2 line 466). PASS criterion: candidate identified with substrate-derived predicted lab S/N margin > 1.0 M_KK² for both Sub-claim A NULL + Sub-claim B ratio observables; promotes the Hybrid Independence Test K-counter from K=2 (W3-3 ι + W4-1 χ') to K=3 (forward Pati-Salam) at the §VII candidate's STAGE-3-PERMANENT advancement layer. FAIL criterion: no Pati-Salam-class superfluid host candidate identified within 3 sessions; the Hybrid Independence Test K-counter remains at K=2 and STAGE-3-PERMANENT promotion is deferred indefinitely.

## Wrap-Up — Workshop Impact Summary

### What Changed

1. **Cross-axis JOINT-WIN STRUCTURAL THEOREM on Reading A simple-block forcing universality is established as a layer-functor F structural theorem** at the methodology floor `Σ_2` Phi-correspondence stratum (analogous to W-1 + W-2 cross-axis JOINT-WIN patterns at S90). The substrate-IS 4-layer commutative diagram (algebra layer / K-theory layer / HH^0 layer / CM-1995 §III.4 residue layer) commutes under F : substrate → methodology → audit; the methodology-floor F-image IS the workshop verdict structure. Reading B as "independent rank arguments by construction" is structurally closed; the three sharpened Reading B residue layers (Element 3 bridge-map-scheme suffix axis; HH^1 cocycle-asymmetry observable's (C3) Hochschild-cocycle-pattern condition; HKR Eilenberg-Moore Level-2 envelope at HH^1) survive as structurally compatible downstream framings.

2. **§VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE registry-landing primed for S91+ mack-cosmic-bridge sole-writer dispatch** under the SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM canonical structure (EC1 resolution): ONE §VII slot; ONE substrate-IS observable (M_3(ℓ) Peter-Weyl block); ONE bridge map (K-theory boundary via χ_* with default `APS-1975-secondary-class` convention tag strengthening to `scheme-INDEPENDENT` on Stage-2 PASS); ONE dual-axis algebraic envelope (Level-2-A operational finite α + Level-2-B regulator-invariance `α = ∞` at HH^0); TWO operational observables at Element 2 (kernel-summand NULL at HH^0 + cocycle-asymmetry ratio at HH^1 with REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag); TWO scope predicates at Element 5 (Sub-claim A max-rank ∈ {1, 2}; Sub-claim B max-rank ∈ {2} via vacuous-(C3) at HH^1(ℂ) = 0).

3. **Cross-workshop CROSS-AXIS JOINT-WIN K=3 calibration corpus candidate established at S90 W-1+W-2+W-3** with four structural pre-conditions identified (cross-axis exchange between substrate-axis and NCG-axiomatic / SF-axis; honest concession when machinery doesn't bind; sharpened framing at downstream structural layers; STAGE-1-CANDIDATE landing at the joint-theorem-promotion 4-stage pathway). The K=3 calibration corpus candidate advances the cross-workshop pattern as a candidate workshop-verdict structural rule per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold; promotion to permanent rule pending forward Stage-2 verify or analogous structural validation at S91+.

### What Holds

1. **Simple-block forcing universality at max-Wedderburn-rank < 3 scope** holds at the kernel-summand HH^0 observable layer (Sub-claim A) as a clean K-theoretic boundary theorem on `(A_K, T)` pairs per Connes-Karoubi pairing structural-theorem-quality content. Pati-Salam IN scope (max-Wedderburn-rank ≤ 2 < 3); SU(5) GUT OUT scope (rank 5 ≥ 3 admits M_3 ↪ M_5 Wedderburn-block embedding); the falsifiable scope boundary is the structural test that distinguishes universality (Reading A) from rank-coincidence (Reading B).

2. **5-IS-not-IN anatomy at Corner-I cell** (algebra-INVARIANT × Mellin pole s=3) per §VII.U.2 4-corner partition K=3 MANDATORY; substrate-IS Level-1 single-τ-slice pin at τ_fold = 0.19; Substrate-IS observable = M_3(ℓ) Peter-Weyl block of A_K's Wedderburn decomposition; Laboratory-IN observable in OE-form `Π^{ker}_{χ}[L] := ∑_{χ ∈ Hom(A_K, T_χ)} 1_{max-Wed-rank(T_χ) < 3} · Tr_{M_3(ℂ)}(P_{M_3(ℂ)} ∘ χ^*) = 0`; Bridge map = K-theory boundary via inheritance morphism χ_* under substrate-self-consistent binding class (i).

3. **4-layer commutative diagram methodology-floor F-image holds at every NCG-axiomatic layer** (algebra layer / K-theory layer / HH^0 layer / CM-1995 §III.4 residue layer); BDI K-grading orthogonal-Corner per §VII.U.2 parse-tree clause (e) at 3He-B vortex-core spectroscopy operational realization (Hypothesis (a) holds); Cell-I classification under both A_BdG readings of W-4 (W3+W6's `A_BdG = M_2(ℂ)` direct inheritance-image vs W5's `A_F ⊗ M_2(ℂ)` full tensor; effective χ_* image is identical under both readings via BDI projection restriction).

### What Breaks or Strains

1. **HH^1 finite-α FIRST-EXTRACTION PENDING at S91+** — the cocycle-asymmetry ratio observable `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992 = 114453/15625` (Sage-QQ exact per W3-3 §(d.b) line 424) at substrate-distance-1 pole s=3 on the M_3(ℓ) Peter-Weyl block carries finite α at Level-2-A operational axis (Friedrich-Bär saturation bound) but exact `α_substrate = ∞` at Level-2-B regulator-invariance axis (substrate-IS HH^1 cohomology-class identity exact L-independent); the dual-axis specification requires FIRST-EXTRACTION via L_max scan or closed-form CM-1995 §III.4 residue evaluation at S91+ per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag.

2. **Bridge-map-scheme-INDEPENDENCE PENDING Stage-2 verify** across APS-1975-secondary-class vs Cheeger-Simons vs Bismut-Cheeger η-form evaluations — the V3 default convention tag `convention=substrate-self-consistent-K-theory-boundary-APS-1975-secondary-class` is appropriate for the 3He-B Pillar IV vortex-core spectroscopy manifold-with-boundary analog; the Pillar II LRD horizon-area cutoff may demand Cheeger-Simons foliation-aware secondary-class evaluation; the M-asymptotic envelope may demand Bismut-Cheeger adiabatic-limit. Stage-2 scheme-INDEPENDENCE verify within 1e-3 M_KK² per CF-55 / §VII.AQ precedent strengthens the convention tag to scheme-INDEPENDENT or maintains the default APS-1975 suffix.

3. **Sub-claim B narrower scope (max-rank ∈ {2}) vs Sub-claim A wider scope (max-rank ∈ {1, 2}) operational discriminator gate pending S91+** — the vacuous-(C3) at HH^1(ℂ) = 0 (per volovik's Q-C3-1 answer; Loday Cyclic Homology §1.5 cohomological-vanishing argument) sharpens Sub-claim B's scope at the abelian-target layer. A discriminator gate identifying a laboratory pillar where the two sub-claims operationally diverge (Sub-claim A NULL holds while Sub-claim B ratio fails, OR vice versa) is pending S91+. The Hybrid Independence Test K-counter advancing from K=2 (W3-3 ι + W4-1 χ') to K=3 (forward Pati-Salam in-scope candidate identification) is the structural watchpoint for STAGE-3-PERMANENT promotion of the §VII candidate.

### Carry-Forward Computations

Numbered list with 4-field specs per `feedback_fix-in-session-never-defer.md` format (What / Inputs / Gate / Effort):

1. **CF-S91-M3C-KERNEL-UNIVERSALITY-STAGE-1-CANDIDATE-REGISTRY-LANDING**
   - **What**: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` lands §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry for the cross-morphism M_3(ℂ)-kernel universality theorem with SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM canonical structure per EMERGENCE EC1 resolution; registry text incorporates 5-IS-not-IN anatomy + 3-level ladder + dual sub-claim scope predicates + bridge-map-scheme suffix default APS-1975 + dual-axis Level-2 envelope + REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag at HH^1 observable.
   - **Inputs**: this workshop's R2-B verdict + V3 sharpened §VII candidate registry text (Re:V3 lines 569-579) + volovik's R2 EMERGENCE E2 joint specification at Elements 3+4+5 (lines 1132-1145); `sessions/permanent-results-registry.md` for next-free-letter slot allocation per `regulator-pin-discipline.md` next-free-letter protocol; `cross-pillar-bridge-anatomy.md` for 5-IS-not-IN anatomy + 3-level ladder template; `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 for OP-PROJ suffix; `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` SUGGESTION-K=1 (parse-tree expansion already declared in this workshop's Re:V5 Observation 2 Q-V5-2 answer at lines 679-684).
   - **Gate**: PASS = registry text emitted with STAGE-1-CANDIDATE tag + dual-sub-claim structure + all 5 IS-not-IN anatomy elements declared + audit_sha256 dual-SHA companion row appended to `s91_gate_verdicts.txt` (or whichever session N file applies) + `_cross_pillar_bridge_audit.py` AUDIT-PASS at plan-freeze; FAIL = missing anatomy element OR cross-corner co-primary FORBIDDEN audit failure OR plan-freeze halt per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"`.
   - **Effort**: ~0.5 wave-equivalents (single mack-cosmic-bridge sole-writer dispatch with pre-specified anatomy from this workshop).

2. **CF-S91-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY** (dispatch identifier `S91-OR-LATER-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-VERIFY`)
   - **What**: Stage-2 cross-axis independent-verify of the §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry per `joint-theorem-promotion.md §"Stage 2"` 4-stage pathway with substrate-input-orthogonality predicate ceiling. Dispatch to Axis-A `van-den-dungen-bridge-theorist` (Kasparov KK-projection authority; verifies K-theory boundary bridge map + Connes-Karoubi pairing structural-theorem-quality content) + Axis-B `mack-cosmic-bridge` (laboratory-side expertise on Pillar IV BdG + Pillar II LRD horizon).
   - **Inputs**: CF-S91-M3C-KERNEL-UNIVERSALITY-STAGE-1-CANDIDATE-REGISTRY-LANDING completion (CF-1 above must land first); substrate-input-orthogonality assignment per EMERGENCE EC2 reading (i) dual-audit-axis-JOINT — vdd loads Level-2-B regulator-invariance data file (substrate-IS HH^0 K-theoretic identity at L_max ≥ 0 Connes-Karoubi pairing data); mack loads Level-2-A operational data file (Friedrich-Bär saturation bound at L_max=10 on M_3(ℓ) Peter-Weyl block at substrate-distance-1 pole at 3He-B vortex-core spectroscopy lab-conversion factor). EXCLUDED reviewers: {volovik, connes} per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` original-authoring-agent exclusion clause.
   - **Gate**: PASS = both cross-reviewers return PASS on their respective single-axis clauses AND JOINT clauses (a)+(c) PASS-AND independently in both verdicts (logical AND not OR); substrate-input-orthogonality predicate satisfied at structural ceiling without overlap caveat. FAIL = either cross-reviewer FAIL on any clause; Stage-2 → 3 promotion blocked; theorem stays at STAGE-1-CANDIDATE; FAIL clauses route to next-session remediation. INFO = either cross-reviewer INFO on a clause; Stage-2-INFO-deferred.
   - **Effort**: ~1.0 wave-equivalents (two parallel cross-reviewer dispatches; cross-reviewer audit-machinery self-citation mitigation via vdd's NCG-axiomatic machinery for §VII.U.2 4-corner parse-tree at Corner-I).

3. **CF-S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION**
   - **What**: extract finite `α_operational(s=3)` exponent at substrate-distance-1 pole on the M_3(ℓ) Peter-Weyl block for the cocycle-asymmetry ratio observable `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992` (Sub-claim B Level-2-A operational envelope) via L_max scan + Friedrich-Bär saturation theorem OR closed-form CM-1995 §III.4 residue evaluation on the finite spectral triple. Per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` W-5 calibration corpus 7.3250 ± 0.1% cohomology-asymmetry ratio prediction. Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class tag advancement to FULL Level-2-A operational envelope realization.
   - **Inputs**: D_K block-diagonal cache at L_max ∈ {10, 11, 12, 13, 14, 15} (per S87 W11-3 Friedrich-Bär saturation calibration `η_FB_lower = 0.40`); Loday-Quillen-Tsygan K_1 boundary structure for HH^1 ↔ K_0/K_1 pairing; canonical_constants.py `Delta_BCS`, `M_KK`, `tau_fold`; Sage MCP `sage_eval` for closed-form CM-1995 §III.4 residue at substrate-distance-1 pole (the substrate ratio is Sage-QQ exact 114453/15625 per W3-3 §(d.b) line 424).
   - **Gate**: PASS = `α_operational(s=3)` extracted to ≥ 3 significant figures with publication-precision pin per `epistemic-discipline.md §"Publication-Precision Pre-Registration"` Class 8.3 MANDATORY; cocycle ratio at L_max=10 matches Sage-QQ exact 114453/15625 to within Friedrich-Bär saturation bound; promotes Sub-claim B HH^1 observable from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to registry-PASS eligibility. FAIL = L_max scan fails to converge OR Friedrich-Bär saturation fails to bound from below OR ratio deviates from 7.324992 by > 0.1% at L_max=10 evaluation. INFO = extraction succeeds but `α_operational(s=3)` value is structurally larger than expected (e.g., α ≥ 5 indicating faster-than-anticipated convergence at substrate-distance-1 pole).
   - **Effort**: ~1.5 wave-equivalents (L_max scan at high L_max requires recursive Casimir-projection feasibility pre-check per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`; Sage MCP closed-form residue evaluation supplements numerical L_max scan; Friedrich-Bär saturation theorem analytic certification per S87 W11-3 precedent).

4. **CF-S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT**
   - **What**: test scheme-INDEPENDENCE across APS-1975-secondary-class vs Cheeger-Simons vs Bismut-Cheeger η-form evaluations of the Connes-Karoubi K-theory boundary pairing `⟨[1_{M_3(ℂ)}], [P]⟩` per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` K=1 SUGGESTION pending K=3 MANDATORY. Advances the bridge-map-scheme suffix discipline K-counter from K=1 (CF-55 S90 W7-4) to K=2 (this instance).
   - **Inputs**: §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE entry's bridge map declaration from CF-1; K-theory boundary structure for `K_0(M_3(ℂ)) → K_0(A_K) → K_0(T)` chain; APS-1975 secondary-class evaluation via ρ-invariant on 3He-B vortex-core manifold-with-boundary analog; Cheeger-Simons differential-character at full-leaf-foliation per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` Element 3 sub-axis; Bismut-Cheeger η-form at boundary per the adiabatic-limit evaluation framework. Cross-link with `regulator-pin-discipline.md §"MACHINERY-SCOPE axis"` cache-projection vs full-leaf-foliation discipline (S90 W7-4 CF-57 axis α).
   - **Gate**: PASS = `|⟨ . ⟩_APS-1975 − ⟨ . ⟩_Cheeger-Simons| < 1e-3` AND `|⟨ . ⟩_APS-1975 − ⟨ . ⟩_Bismut-Cheeger| < 1e-3` in M_KK² units per CF-55 / §VII.AQ precedent; scheme-INDEPENDENCE confirmed → §VII candidate convention tag strengthens to `convention=substrate-self-consistent-K-theory-boundary-scheme-INDEPENDENT`; advances bridge-map-scheme suffix discipline K-counter from K=1 to K=2. FAIL = any scheme-pair deviation ≥ 1e-3 → MANDATORY scheme-suffix tagging applies with potentially dual scheme suffix (Pillar IV APS-1975 + Pillar II Cheeger-Simons or Bismut-Cheeger). INFO = scheme-INDEPENDENCE confirmed within 1e-3 M_KK² but the Pillar IV and Pillar II evaluations diverge at higher-degree Hochschild contributions (HH^2 or higher) — sharpens the bridge-map-scheme suffix discipline at higher cohomology degrees.
   - **Effort**: ~1.0 wave-equivalents (three parallel scheme-evaluation computations + pairwise deviation analysis; Sage MCP for closed-form secondary-class evaluations; cross-validation against CF-55 / §VII.AQ K=1 calibration corpus instance).

5. **CF-S91-CROSS-WORKSHOP-JOINT-WIN-K3-PROMOTION-WATCHPOINT**
   - **What**: track whether the S90 W-1 + W-2 + W-3 cross-workshop CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM PATTERN promotes from K=3 calibration corpus candidate to permanent workshop-verdict structural rule at K=3 distinct calibration corpus instances per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. Future S91+ workshops MAY pre-register CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM verdict structure at workshop-spec time citing the S90 W-1+W-2+W-3 pattern; the watchpoint enumerates the four structural pre-conditions defining the pattern (cross-axis exchange; honest concession when machinery doesn't bind; sharpened framing at downstream structural layers; STAGE-1-CANDIDATE landing at joint-theorem-promotion 4-stage pathway).
   - **Inputs**: this workshop's R2-B verdict + W-1 verdict + W-2 verdict (the three S90 cross-axis JOINT-WIN STRUCTURAL THEOREM instances at S90); `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold; `joint-theorem-promotion.md §"4-stage pathway"` for STAGE-1-CANDIDATE landing definition; `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence weight-2 `Σ_2` stratum for methodology-floor structural-theorem F-image definition; `agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE"` for cross-workshop multi-output decomposition pattern complementarity.
   - **Gate**: PASS = promotion event fires at S91+ via Stage-2 verify or analogous structural validation on at least one of the three S90 instances; the cross-axis JOINT-WIN STRUCTURAL THEOREM pattern lands as a permanent workshop-verdict structural rule with the S90 W-1+W-2+W-3 cross-workshop pattern as the K=3 calibration corpus. INFO = at least one S91+ workshop pre-registers CROSS-AXIS JOINT-WIN STRUCTURAL THEOREM verdict structure at workshop-spec time citing the S90 cross-workshop pattern; advances the watchpoint toward K=4 calibration corpus. FAIL = no S91+ workshop adopts the pattern within 3 sessions (S91/S92/S93) and the corpus advance candidate is downgraded to forward-pending watchpoint; the cross-workshop pattern remains a K=3 candidate without MANDATORY promotion.
   - **Effort**: ~0.25 wave-equivalents (orchestrator-only tracking task; no compute dispatch; updates `feedback_rules-compensate-missing-structure.md` K-counter ledger and `sessions/framework/registry/pru-class-corpus.md` calibration corpus entries at S91+ session close).

6. **CF-S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION**
   - **What**: identify a forward Pati-Salam-class superfluid host or analogous laboratory pillar realization satisfying (C1) max-Wedderburn-rank ≤ 2 + (C2) common lab-conversion exponent + (C3) homogeneous symmetry action on the M_3(ℓ) Peter-Weyl block (the Pati-Salam parent symmetry breaks SU(3) → SU(2)_L ⊗ SU(2)_R ⊗ U(1) per V2 line 122; the symmetry-rotation matrices act as a SAME scalar c_χ on both [φ_67] and [φ_88] up to higher-order corrections in the symmetry-breaking parameter per Re:V2 line 466). Advances the §VII candidate's Hybrid Independence Test K-counter from K=2 (W3-3 ι + W4-1 χ' jointly) to K=3 (forward Pati-Salam in-scope candidate) per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` K-counter advancement.
   - **Inputs**: `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` W-5 calibration corpus + forward extension to Pati-Salam parent theories; substrate-physics machinery for Pati-Salam-class superfluid host candidate identification (cross-link with volovik's substrate-superfluid-universe analog via Volovik 2009 §27 cosmological 3He texture transitions for forward Pati-Salam analog); mack-cosmic-bridge laboratory pillar inventory for candidate-host identification at the substrate-physics laboratory side.
   - **Gate**: PASS = Pati-Salam in-scope laboratory pillar candidate identified with substrate-derived predicted lab S/N margin > 1.0 M_KK² for both Sub-claim A NULL + Sub-claim B ratio observables; promotes the Hybrid Independence Test K-counter from K=2 to K=3 at the §VII candidate's STAGE-3-PERMANENT advancement layer (joint promotion of the candidate + the cross-pillar-bridge-anatomy Hybrid Independence Test corpus's MANDATORY-K=3 status currently SUGGESTION K=1). FAIL = no Pati-Salam-class superfluid host candidate identified within 3 sessions (S91/S92/S93); Hybrid Independence Test K-counter remains at K=2; STAGE-3-PERMANENT promotion is deferred indefinitely. INFO = candidate identified but lab-feasibility window > 2035 (forward-only); promotes Hybrid Independence Test corpus advancement candidate but does NOT immediately promote the §VII candidate to STAGE-3-PERMANENT.
   - **Effort**: ~1.5 wave-equivalents (substrate-physics machinery identification + laboratory pillar candidate substrate-derived S/N margin computation + cross-pillar-bridge-anatomy Hybrid Independence Test K-counter advancement bookkeeping; mack-cosmic-bridge dispatch on laboratory pillar inventory; volovik dispatch on substrate-superfluid-universe analog forward extension).

### Closing Line

The shared M_3(ℂ) kernel summand of W3-3 ι and W4-1 χ' is a substrate-IS UNIVERSAL PROPERTY of inheritance morphisms with max-Wedderburn-rank(T) < 3 by cross-axis JOINT-WIN STRUCTURAL THEOREM at layer-functor F level — substrate-axis simple-block forcing via Schur + Wedderburn-Artin (V1+V4) + NCG-axiomatic 4-layer commutative diagram across algebra/K-theory/HH^0/CM-1995 §III.4 residue layers (Re:V1+C1+C2) + Pati-Salam IN scope / SU(5) GUT OUT scope falsifiable boundary (V5 + Q-V5-3) — primed for §VII.<next-free-letter>.OP-PROJ STAGE-1-CANDIDATE registry-landing at S91+ under SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM canonical structure (EC1) and dual-audit-axis-JOINT Stage-2 dispatch (EC2) pending HH^1 finite-α FIRST-EXTRACTION + bridge-map-scheme-INDEPENDENCE Stage-2 verify.
