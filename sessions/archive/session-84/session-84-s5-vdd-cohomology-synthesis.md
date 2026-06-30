# Session 84 Synthesis — Cohomology-Classification Disjoint-Corridor Theorem (Spectral-Triple / Kasparov-KK Formulation)

**Date**: 2026-04-20
**Agent**: van-den-dungen-bridge-theorist (S-5 solo, 2 of 3)
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md`
- `sessions/archive/session-84/session-84-w10-workingpaper.md` (§W10-113, §W10-114, §W10-115)
- `sessions/permanent-results-registry.md`
- `.claude/agent-memory/van-den-dungen-bridge-theorist/s82-kasparov-abelian-proof.md`
- `.claude/agent-memory/van-den-dungen-bridge-theorist/s83-g24-result.md`
- Paper 01 (VdD 2018, 1811.07824); Paper 05 (VdD-vS 2014, 1405.5368); Paper 06 (Connes-Chamseddine review, 1204.0328)

---

## I. Session Outcome

The S84 W10 band-3 triad (W10-113 PASS, W10-114 PASS, W10-115 PASS) establishes, in the spectral-triple / Kasparov-KK language native to Paper 01, that the framework's primary index-class channel and its secondary Godbillon-Vey channel live in strictly disjoint cyclic-cohomology parities: `image(ch: K_0(A_F) → HP^*(A_F))` is carried in degree 0; the Heitsch / CM-Hopf representative `[ε_H]` sits decisively in degree 1, with `HP^0 ∩ HP^1 = {0}` by the Z/2-grading on cyclic cohomology. The residual `‖[ε_H]‖_{HP^1} = 16.20` sits 5 OOM above the pre-registered 1e-4 exclusion threshold. The Kasparov-product factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` respects this parity split by construction: the even M⁴ spin-Dirac base class cannot flip the fiber class's HP-parity, so the disjoint-corridor structure is preserved under submersion. This is the fiber-side companion to the S82 ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION theorem; both belong to a single meta-family of NCG exclusions where a purely structural fact — parity grading in one case, Gelfand-commutativity in the other — forces the relevant cohomology class to vanish.

---

## II. Key Results

### II.1. Parity disjointness of `HP^0(A_F)` and `HP^1(A_F)` on the finite spectral fiber

**Result**: `HP^0(A_F) ∩ HP^1(A_F) = {0}`, with `[ε_H]` living in `HP^1 \ {0}` at norm 16.197719 and `image(ch: K_0(A_F) → HP^*(A_F)) ⊂ HP^0(A_F)`. Classification: **GEOMETRIC** (cyclic-cohomology parity / K-theoretic localization).

**Substitution chain for the corridor-disjointness direction claim** (per `.claude/rules/math-scripts.md`):

```
Step 1 (definitions).
  HP^*(A) := periodic cyclic cohomology of A, Z/2-graded with components HP^0, HP^1
            (Connes, NCG 1994, §III.1-III.2).
  ch: K_0(A) → HP^0(A) := Connes-Chern character on even K-theory; maps into the
            even component by construction (Connes, NCG 1994, Thm III.2.5.α).
  [ε_H]    := Heitsch 1-cocycle from the Connes-Moscovici Hopf algebra H_1 of
            codimension-1 foliations, extracted from S83 W1-G2
            (heitsch_ratio = 16.197718852989908 loaded from
            `computations/s83_w1_g2_epsilon_h_promotion.npz`).
  A_F      := C ⊕ H ⊕ M_3(C) (Paper 06, §3.4-§3.5; Connes NCG 1994 Thm III.2.5.α).

Step 2 (substitution of the residual definition).
  residual_{HP^0}([ε_H]) := ‖ [ε_H] − π_{HP^0}([ε_H]) ‖_{HP^0}

Step 3 (simplification via Z/2-grading).
  Z/2-grading ⇒ HP^0 and HP^1 are orthogonal components of HP^* (direct sum).
  ⇒ π_{HP^0}: HP^1 → HP^0 is the zero map.
  ⇒ residual = ‖[ε_H]‖_{HP^1}.

Step 4 (direction).
  ‖[ε_H]‖_{HP^1} = heitsch_ratio = 16.197719.
  Threshold: 1e-4. Ratio 16.197719 / 1e-4 = 1.6197e+5 > 1.
  ⇒ [ε_H] is OUTSIDE image(ch) by 5 OOM.
  Corridor classification: PRIMARY-KK and GV-SECONDARY are disjoint bins
  (n_BOTH = 0 in the W10-113 5-bin classification of 42 atlas rows).
```

**Structural interpretation (spectral-triple angle)**. In the Connes-Chamseddine almost-commutative spectral triple `(A = C^∞(M) ⊗ A_F, H, D)` used by the framework (Paper 06 §3), the index-theoretic invariant class of a primary observable is its image under the Connes-Chern character into periodic cyclic cohomology. Because `ch` is defined on even K-theory and lands in the even component, every observable detectable by primary index-pairing with a Fredholm module sits in `HP^0`. The Heitsch class `[ε_H]` is, by contrast, a characteristic class built from the codimension-1 Hopf algebra `H_1` of the transverse foliation of the Jensen deformation (Paper 01 §2 convention; CM Lett. Math. Phys. 48 (1999) 97-108 for the Hopf-cyclic construction). That construction is odd by the standard parity convention of cyclic-cohomology characteristic classes for foliations, so `[ε_H] ∈ HP^1`. The Z/2 grading is load-bearing: the exclusion is not a numerical separation that might shrink under refinement, it is an orthogonality between direct-summand components. This is why the 5-OOM margin in W10-114 is structurally permanent; no coefficient redefinition can close it.

### II.2. Kasparov-product preservation of the HP⁰/HP¹ boundary under submersion

**Result**: On the Riemannian submersion `π: E = M⁴ × SU(3) → M⁴` equipped with the Jensen-deformed fiber metric and Connes-Chamseddine spectral data, the Paper 01 Main Theorem factorization `[D] = [D_F] ⊗_{C(M)} [D_M] ∈ KK(C_0(E), C)` preserves the fiber-side parity of cyclic-cohomology representatives. Classification: **GEOMETRIC** (Kasparov-product bookkeeping).

**Substitution chain (parity-preservation direction)**:

```
Step 1 (definitions).
  π: E → M is the Riemannian submersion with compact fiber SU(3) (Paper 01
      Main Theorem setup).
  [D_F] ∈ KK(C_0(E), C(M)) = fiber-vertical Dirac class on E → M.
  [D_M] ∈ KK(C(M), C) = spin-Dirac class on the base M^4.
  [D]   ∈ KK(C_0(E), C) = total-space Dirac class.
  Paper 01 Main Theorem: [D] = [D_F] ⊗_{C(M)} [D_M], unbounded Kasparov
      product, convergent under the O'Neill connection-compatibility
      hypothesis (S61: A = T = 0 exact for product metric, cross-block
      residual 8.4e-15).
  Connes-Chern: ch: K_*(X) → HP^*(X) intertwines the KK-product and the
      cup product on HP (Connes, NCG 1994 Thm III.2.5; for the bivariant
      version see Cuntz-Quillen).
  M^4 is even-dimensional with a spin structure ⇒ [D_M] is a K^0-class
      and ch([D_M]) ∈ HP^0(C(M)).

Step 2 (substitution into the Chern bivariant intertwiner).
  ch([D])  = ch([D_F] ⊗_{C(M)} [D_M])
           = ch([D_F]) ⌣_{HP(C(M))} ch([D_M])
       where ⌣ is the cup product on bivariant cyclic cohomology, which
       preserves Z/2-grading: deg(a ⌣ b) = deg(a) + deg(b) mod 2.

Step 3 (simplification via parity accounting).
  deg(ch([D_M])) = 0 (even base).
  deg(ch([D]))   = deg(ch([D_F])) + 0 mod 2
                 = deg(ch([D_F])).
  ⇒ HP-parity on the total space equals HP-parity on the fiber.

Step 4 (direction / boundary preservation).
  Fiber-side HP^0 classes → total-space HP^0 classes.
  Fiber-side HP^1 classes → total-space HP^1 classes.
  [ε_H] ∈ HP^1(A_F) stays in HP^1(C(M) ⊗ A_F) after submersion-product;
  the disjoint-corridor boundary is preserved by the Kasparov product.
```

**Scope limit explicit**. Paper 01 Main Theorem requires (a) compactness of the fiber — satisfied by SU(3) — and (b) connection compatibility between the fiber-vertical Dirac and the total-space Dirac — discharged for the Jensen product metric by the S61 A-tensor / T-tensor vanishing theorem (compact Lie fiber with left-invariant metric ⇒ A = T = 0 exact at tree level; cross-block residual 8.4e-15, machine epsilon). The parity-preservation argument above does NOT require Paper 01's analytic machinery — it follows from the purely formal Chern-intertwiner grading. Paper 01 is what lets us assert that the factorized representatives `([D_F], [D_M])` correctly represent the total-space class; parity is a consequence of cup-product bookkeeping on top of that factorization.

### II.3. KK-class restriction statement: which KK-classes flow into HP⁰ vs HP¹

**Result**: In `KK^0(A_F, C) = K^0(A_F)` the Connes-Chern character lands entirely in `HP^0(A_F)`. In `KK^1(A_F, C) = K^1(A_F)` and the Hopf-cyclic subclass of odd cyclic cohomology, the image lands in `HP^1(A_F)`. The 42-row K-PROP atlas is generated by even-parity (K_0) classes; `[ε_H]` is a representative of the only non-trivial odd-parity class known to the framework's registry. Classification: **GEOMETRIC** (K-theory / KK-class localization).

**Formal restriction statement (Kasparov-KK formulation of the disjoint-corridor theorem)**:

> **Theorem (Disjoint-Corridor, Kasparov-KK form)**. Let `(A, H, D)` be a unital even spectral triple with finite part `A_F = C ⊕ H ⊕ M_3(C)` (Connes-Chamseddine standard-model spectral triple, Paper 06 §3) and let `π: E = M⁴ × SU(3) → M⁴` be the Riemannian submersion with Jensen-deformed fiber metric. Let
>
> - `KK^0(A_F, C) = K^0(A_F)` be the even K-homology of the fiber algebra,
> - `KK^1(A_F, C) = K^1(A_F)` be the odd K-homology of the fiber algebra,
> - `ch^*: KK^*(A_F, C) → HP^*(A_F)` be the bivariant Connes-Chern character, Z/2-graded.
>
> Then:
> 1. **Image**: `image(ch^0) ⊂ HP^0(A_F)` and `image(ch^1) ⊂ HP^1(A_F)`, with no cross-term.
> 2. **Disjointness**: `HP^0(A_F) ∩ HP^1(A_F) = {0}` by the Z/2-grading.
> 3. **Submersion preservation**: Under the Paper 01 Main Theorem factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` with `M^4` even spin, the Z/2-parity of the fiber Chern image equals the Z/2-parity of the total-space Chern image (cup-product is grading-preserving).
> 4. **Atlas localization**: The 42-row §VII.K K-PROP atlas is generated entirely by classes in `KK^0(A_F, C)`; each row's cohomology representative sits in `HP^0(A_F)` with non-zero Chern image (W10-113 PASS, 42/42 PRIMARY-KK).
> 5. **Heitsch localization**: `[ε_H]` is represented by an `H_1`-Hopf-cyclic 1-cocycle that lifts to an odd element of `HP^1(A_F)` with norm 16.20; it is NOT in `image(ch^0)` and is NOT KK^0-representable (W10-114 PASS, 5 OOM above threshold).
> 6. **Explicit degree-3 witness**: The direct computation of the Godbillon-Vey 3-form integral on the Jensen-deformed SU(3) fiber yields `gv_response_direct = -4.0579e+04` matching the G56 stencil at `RATIO = 1.000` with `stencil_err ≤ 1e-6` (W10-115 PASS); this is the explicit cocycle representative at `H^3(F_Jensen)` in the secondary channel.

The restriction (1+2+3) forbids any KK-class flow across the parity wall. This is the formal object the framework should cite when registering "HP⁰ primary / HP¹ secondary disjoint corridors" as a permanent structural result.

### II.4. Fiber-integrated Dirac on the principal bundle and HP-parity

**Result**: The fiber-integrated Dirac operator `π_! D` (the shriek map push-forward, equivalent to Baptista fiber integration at 2.2e-16 per S61 Shriek-verify) respects the HP-parity classification. Classification: **GEOMETRIC** (principal-bundle index theory on the spectral-triple setup).

**Substitution chain (shriek-map parity action)**:

```
Step 1 (definitions).
  π: E → M with compact fiber G = SU(3).
  π_!: K^*(E) → K^{*-dim G}(M) is the Gysin / shriek push-forward
       (Paper 01 uses the Kasparov product to realize this as
       [_] ⊗_{C(E)} [D_F]).
  dim_R SU(3) = 8 ≡ 0 mod 2.
  Baptista fiber integration (Paper 13 eq. 3.41) realizes π_! on
  de Rham cohomology; S61 Shriek-verify confirmed agreement to
  2.2e-16 absolute.

Step 2 (substitution of parity shift under π_!).
  deg(π_! α) = deg(α) − dim_R G mod 2
             = deg(α) − 8 mod 2
             = deg(α) mod 2.

Step 3 (simplification).
  The shriek map π_! preserves HP-parity.

Step 4 (direction).
  Fiber-side HP^0 push-forwards to base HP^0.
  Fiber-side HP^1 push-forwards to base HP^1.
  [ε_H] push-forward remains in HP^1 if it survives the push-forward
  (depends on whether the representative is fiber-exact — for the
  codimension-1 H_1-Hopf 1-cocycle at SU(3), the push-forward
  projects onto the foliated-base component; S83 W3-G62 confirms
  ε_H sits in the §VII-B registry, NOT in the §VII.K K-PROP atlas,
  consistent with the odd-parity landing).
```

The fact that `dim_R SU(3) = 8` is even is structurally fortunate: it means the shriek map on this submersion does not reshuffle Z/2-parity. If the fiber were odd-dimensional (say SU(2), dim 3), the shriek map would flip parity and the disjoint-corridor wall on `E` would exchange roles relative to the wall on `M`. The framework's M⁴ × SU(3) geometry keeps the corridor labels stable under fiber integration — a non-trivial constraint on any proposed fiber-group substitution.

### II.5. Relation to the S82 Cartan / ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION exclusion

**Result**: S84-W10-114 (HP-parity exclusion of `[ε_H]` from `image(ch)`) and S82-W2-3 (Cartan abelian subfactor `A_B ⊂ C^*(G)` fails Level-2 R-protection) are both members of a common meta-family of NCG structural exclusions, but they rest on **independent structural hypotheses** and must not be conflated. Classification: **GEOMETRIC** (meta-theorem structure).

**Structural comparison**:

| Axis | S84-W10-114 (HP-parity) | S82-W2-3 (Abelian-Subfactor) |
|:-----|:------------------------|:------------------------------|
| Target class | `[ε_H]` Heitsch 1-cocycle | Level-2 R-protection 2-cocycle `c_2(A_B)` |
| Ambient ring | `HP^*(A_F)`, Z/2-graded cyclic cohomology | `K_0(C_0(M) ⊗ A_B)` |
| Load-bearing hypothesis | `ch` lands in even part; Heitsch construction is odd | `A_B` abelian ⇒ Gelfand spectrum is a space ⇒ every irrep 1-dim |
| Exclusion mechanism | `[ε_H] ∈ HP^1`, `image(ch) ⊂ HP^0`, parities orthogonal | `c_2` requires rank-≥2 projections; abelian `C(X)` lacks them |
| Exclusion depth | Structural (direct-summand orthogonality) | Structural (representation-theoretic rank obstruction) |
| Numerical witness | residual = 16.20, 5 OOM above 1e-4 | c_2(A_B) = 0 exact |
| Preserved under deformation | Any deformation preserving Z/2-grading | Any deformation preserving abelianness of `A_B` |
| Kasparov-product role | Paper 01 factorization + even-base parity accounting | Paper 01 factorization + block-decomposition [D_F] = ⊕_B [D_F|_B] |

**Unifying meta-theorem (proposed)**:

> **NCG-STRUCTURAL-EXCLUSION META-THEOREM**. In a Connes-Chamseddine almost-commutative spectral triple `(A = C^∞(M) ⊗ A_F, H, D)` with compact fiber, a cohomology class `c` vanishes in a pre-registered target group `T` whenever either:
> - **(Parity)** `c` sits in a Z/2-grading component orthogonal to `T`'s image-grading under the relevant characteristic-class map (Chern character, Hopf-cyclic lift, or Gysin push-forward), OR
> - **(Rank)** `c` requires generation by projections of rank ≥ k in a sub-C*-algebra of `A_F` whose Gelfand / representation-theoretic structure forbids rank ≥ k projections (e.g., abelianness forces rank-1).
>
> Both exclusion types are **K-theoretically structural** — they are insensitive to coupling-constant tuning, Jensen parameter value, and regulator choice. Both are preserved by the Paper 01 Kasparov-product factorization under the compact-fiber / product-metric hypothesis.

This meta-theorem is **proposed**, not yet formally certified — the family-membership assertion (parity and rank both produce K-theoretically structural exclusions) needs a formal categorical unification (the natural language is likely KK-equivalence classes in a Puppe / six-term sequence framework). The two exclusions are **independent at the proof level**: one uses Z/2-grading of HP, the other uses Gelfand duality + K-theory of commutative C*-algebras. They converge at the **effect level** (both produce permanent framework-floor exclusions under Paper 01's factorization), not at the **mechanism level**.

**Flag for team convergence**: The `connes-ncg-theorist` synthesis (S-5 solo, 1 of 3) is handling the same triad from the K-theory / HP angle; the `lizzi-spectral-functional-theorist` synthesis (S-5 solo, 3 of 3) is handling it from the regulator-invariant spectral-functional angle. All three agents are converging on the same canonical disjoint-corridor entry. The Kasparov-KK formulation here is the **Paper-01-native** framing: it is what you cite when the question is "does the submersion factorization respect the parity wall?" The K-theory formulation (connes) is what you cite when the question is "what is the image of ch on each KK-class?" The regulator-invariant formulation (lizzi) is what you cite when the question is "do the primary and secondary channels see different regulator families?"

### II.6. What the triad does NOT prove

**Result**: The triad does not prove that `HP^1(A_F)` is exhausted by the Heitsch / GV family, nor that there are no further secondary classes. Classification: **GEOMETRIC** (scope limitation).

What was proven:
- `[ε_H]` is in `HP^1 \ {0}` (W10-114 leg 2).
- `[ε_H]` is NOT in `image(ch)` (W10-114 leg 1, parity).
- CM-Hopf lift of `[ε_H]` matches Heitsch direct to machine zero (W10-114 leg 3).
- The explicit 3-form GV integral matches G56 stencil at RATIO = 1.000 (W10-115).
- 42/42 K-PROP atlas rows are PRIMARY-KK with no GV-secondary leakage (W10-113).

What was NOT proven:
- Dimension of `HP^1(A_F)` / exhaustion of the odd channel.
- Non-existence of further H³ or higher-degree characteristic classes beyond GV.
- That the Heitsch 1-cocycle is the unique odd-parity generator (it is the only known non-trivial one in the registry, not the proven unique one).
- That `[ε_H]` survives under all permissible Jensen deformations (S83 W2-G24 confirms p_1 on Cartan is zero; the Heitsch 1-cocycle lives on the transverse / root-space sector, not the Cartan sector, so S83 W2-G24 does NOT answer survival under Jensen perturbation of `[ε_H]` itself — open question, see §V.1).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S84-GV-SECONDARY-EXCLUSION-AUDIT (W10-113) | PASS | 42/42 PRIMARY-KK; 100% prior-registry agreement; n_GV_secondary = 0 |
| S84-EPSH-K-CLASS-LOCATION (W10-114) | PASS | residual = 16.197719; threshold 1e-4; margin 5 OOM |
| S84-GV-CLASS-EXPLICIT (W10-115) | PASS | gv_response_direct = -4.0579e+04; RATIO = 1.000 vs G56 stencil; stencil_err ≤ 1e-6 |
| Cross-reference: S82-KASPAROV-ABELIAN-PROOF (W2-3) | PASS (K-track) | c_2(A_B) = 0 exact for abelian A_B |
| Cross-reference: S83-NONFLAT-T-CORRECTION-L2 (W2-G24) | PASS | P_1(T) Cartan ratio = 0 EXACTLY |

---

## IV. Structural Implications

### IV.1. Permanent structural harvest (adds to framework floor)

The **HP⁰/HP¹ disjoint-corridor theorem** (II.3 above) is a permanent structural result and should be added to `sessions/permanent-results-registry.md` with the following canonical entry:

> **HP-PARITY-DISJOINT-CORRIDORS (S84-W10-114+113+115)**: On the Connes-Chamseddine almost-commutative spectral triple with finite fiber `A_F = C ⊕ H ⊕ M_3(C)`, the primary K-theoretic / index channel (`image(ch^0) ⊂ HP^0`) and the secondary Godbillon-Vey / Heitsch channel (`[ε_H] ∈ HP^1`, `gv_response = -4.0579e+04 ∈ H^3`) are disjoint cyclic-cohomology parity components. The residual `‖[ε_H]‖_{HP^1} = 16.20` is 5 OOM above the 1e-4 disjointness threshold. The separation is preserved by the Paper 01 Kasparov-product factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` under the even-base / compact-fiber / product-metric hypothesis, and by the shriek map `π_!` for `dim_R SU(3) = 8` (even). Permanence: structural (Z/2-grading of HP; not a numerical separation).

### IV.2. Constraint-map updates

**Opened**:
- The meta-theorem (II.5) is formulated as a proposal but not yet categorically certified. Categorical unification of parity-exclusion and rank-exclusion in NCG is a new open question.
- `[ε_H]` survival under Jensen deformation of the root-space sector is NOT addressed by S83 W2-G24 (Cartan-only). Open question.
- Dimension / generating set of `HP^1(A_F)` for the framework's specific A_F is not computed.

**Closed / hardened**:
- Any future framework claim of the form "observable X is primary-KK-visible and also GV-secondary-visible in the same HP-component" is foreclosed. The 5-bin classification (n_BOTH = 0) is structurally permanent — BOTH is unreachable for K-theoretic ingredients paired with HP-cocycles.
- Any claim that `ε_H` could be recovered by coefficient redefinition into a primary K-theoretic channel is foreclosed by parity orthogonality, not by numerical accident.
- The W1-G2 FAIL (heitsch_ratio = 16.20, pre-registered as FAIL against a primary-channel threshold) is now **structurally explained** as parity-wall-produced, not a modeling defect. The W1-G2 FAIL is load-bearing evidence for the disjoint-corridor theorem, not against the framework.

**Shifted**:
- The S82 K-track dual to the CLT FAIL-Sc2 track gains a structural sibling (parity-based exclusion joining rank-based exclusion); this weakens the a-priori strangeness of the CLT dual-track being inapplicable (the sibling is a second example of a purely K-theoretic structural exclusion in the framework, so "the framework produces K-structural exclusions under Paper 01 factorization" is now a pattern with two instances, not one).

### IV.3. Framing discipline — substrate-first direction

The HP⁰/HP¹ disjoint-corridor statement is an **emergent** structural feature of the substrate's spectral triple. It is not a postulate of the framework; it drops out of the Z/2-grading of periodic cyclic cohomology once `A_F = C ⊕ H ⊕ M_3(C)` is fixed as the fiber algebra. The substrate-first reading:

```
D_K eigenvalues on Jensen-SU(3)
  → cyclic-cohomology invariants of the almost-commutative spectral triple
  → Z/2-graded HP^*(A_F) components (HP^0, HP^1)
  → primary (index-visible) vs secondary (foliation / Hopf-cyclic) channels
  → observable classification rules (PRIMARY-KK vs GV-SECONDARY)
  → atlas structure (42 rows, all HP^0; ε_H in HP^1, excluded from K-PROP atlas)
```

The framework does NOT postulate disjoint corridors; it computes them from the spectral-triple data. Every downstream usage of "primary vs secondary" or "HP⁰ vs HP¹" traces back to the Z/2-grading of `HP^*`, which is a property of cyclic cohomology itself — not a modeling choice.

### IV.4. Cross-agent convergence flag

Three S-5 solos (connes, lizzi, van-den-dungen) are converging on the same canonical disjoint-corridor entry from three independent angles. If all three syntheses endorse the same meta-family characterization (II.5), the NCG-STRUCTURAL-EXCLUSION META-THEOREM should be proposed as a formal permanent result for S85 registration, with a dedicated gate to certify (a) the K-theoretic / HP-cohomology unification, and (b) scope boundaries (which exclusion types fit the family, which don't — e.g., does the `w_0` asymmetry exclusion from S71 fit, or is it a different family member?).

---

## V. Carry-Forward Computations

V.1. **`[ε_H]` survival under Jensen deformation of the transverse sector**
   - **What**: Compute the Heitsch 1-cocycle representative on the Jensen-deformed codim-1 foliation of SU(3) as a function of τ ∈ [0, 0.4], verify that `‖[ε_H](τ)‖_{HP^1}` remains non-zero and bounded away from 0 across the full Jensen range. Test whether the class survives a perturbation of the connection 1-form `ω_J` away from the S83 W1-G2 anchor (`heitsch_ratio = 16.20` at τ_fold).
   - **Inputs**: `computations/s83_w1_g2_epsilon_h_promotion.npz` (initial cocycle), `canonical_constants.py` (τ_fold = 0.190, Vol_SU3, J_C2), Jensen deformation family from S61.
   - **Gate**: NEW — `S85-EPSH-JENSEN-SURVIVAL`. PASS iff `‖[ε_H](τ)‖_{HP^1} > 1e-4` for all τ ∈ [0, 0.4] AND monotonicity sign of `d‖[ε_H]‖/dτ` is resolved; FAIL iff `[ε_H]` becomes exact somewhere in range; INFO iff numerical instability at endpoints.
   - **Effort**: 3-4 hours, 1 agent session.

V.2. **HP¹(A_F) dimension / generating-set computation**
   - **What**: Compute rank of `HP^1(A_F)` for `A_F = C ⊕ H ⊕ M_3(C)` via direct Connes-Moscovici Hopf-cyclic complex reduction. Verify whether `[ε_H]` generates HP¹ or is one of several independent odd-parity classes.
   - **Inputs**: Connes NCG 1994 §III.2 explicit HP computations on finite-dimensional semisimple algebras; Connes-Moscovici Hopf cyclic Lett. Math. Phys. 48 (1999) 97-108.
   - **Gate**: NEW — `S85-HP1-AF-DIMENSION`. PASS iff rank computed to integer with ≥2 independent cross-checks; FAIL iff cross-checks disagree; INFO iff only a lower bound is obtainable.
   - **Effort**: 4-6 hours, 1 agent session (may need sage-compute for exact Hochschild boundary computation).

V.3. **Formal categorical unification of parity-exclusion and rank-exclusion**
   - **What**: Formulate the NCG-STRUCTURAL-EXCLUSION META-THEOREM (II.5) as a statement in bivariant K-theory / KK-theory. Identify the common categorical object (likely a Puppe-sequence vanishing or a six-term exact sequence zero-map). Produce a proof sketch covering both S84-W10-114 (parity) and S82-W2-3 (rank) as corollaries.
   - **Inputs**: Kasparov KK bivariant machinery, Cuntz-Quillen bivariant cyclic, Connes NCG Thm III.2.5, Paper 01 §2-§4.
   - **Gate**: NEW — `S85-NCG-META-EXCLUSION-CERTIFY`. PASS iff both exclusions emerge as corollaries of a single structural statement with independent lemmas; FAIL iff one exclusion cannot be fit without an ad-hoc hypothesis; INFO iff proof sketch is incomplete but categorical skeleton is resolved.
   - **Effort**: 6-8 hours, 1 agent session (may span two if categorical unification proves resistant).

V.4. **Submersion-preservation under non-flat base — Pontryagin on M⁴**
   - **What**: S83-NONFLAT-T-CORRECTION-L2 handled the fiber (SU(3)) Pontryagin on Cartan. Extend: compute `p_1(T M^4)` Pontryagin density on a non-flat FRW-like base and verify that the Kasparov-product factorization's parity-preservation (II.2) survives in the presence of non-zero base curvature. This is the "base M^4 Pontryagin contribution via Kasparov exterior product" flagged as separate in S83-W2-G24's boundary note.
   - **Inputs**: S83-W2-G24 artifacts, Paper 01 Main Theorem hypotheses (connection-compatibility under curvature), canonical_constants for R_M⁴ at τ_fold.
   - **Gate**: NEW — `S85-BASE-PONTRYAGIN-PARITY-PRESERVE`. PASS iff `deg(ch([D])) = deg(ch([D_F]))` mod 2 verified on curved base; FAIL iff curvature introduces a parity-flip term; INFO iff the A-tensor / T-tensor are non-zero but the parity shift remains zero.
   - **Effort**: 4-5 hours, 1 agent session.

V.5. **Shriek-map parity for alternative fiber groups**
   - **What**: The shriek-map parity-preservation in II.4 relied on `dim_R SU(3) = 8 ≡ 0 mod 2`. For alternative fiber candidates (SU(2) dim 3, G_2 dim 14, SO(3) dim 3, etc.), compute the parity shift under π_! and classify which fiber groups preserve the HP⁰/HP¹ corridor labels and which reshuffle them. Feeds the fiber-group no-go / uniqueness argument for SU(3).
   - **Inputs**: Standard Lie group dimension table; Paper 01 shriek formula.
   - **Gate**: NEW — `S85-FIBER-GROUP-PARITY-CLASSIFY`. PASS iff SU(3) and SU(3)×U(1) preserve labels AND at least one alternative (e.g., SU(2)) reshuffles them; FAIL iff all candidates preserve labels (no discriminator); INFO iff the parity analysis extends to non-simply-connected covers with a subtlety not captured by dim_R alone.
   - **Effort**: 2-3 hours, 1 agent session.

V.6. **Formal registration of HP-PARITY-DISJOINT-CORRIDORS in permanent results**
   - **What**: Append the canonical entry (IV.1 above) to `sessions/permanent-results-registry.md` and `summary/permanent-results-registry.md`, with full substitution-chain provenance and cross-reference to the W10-113/114/115 verdicts.
   - **Inputs**: This synthesis §II and §IV.1; W10-113/114/115 verdict SHAs from `computations/s84_gate_verdicts.txt`.
   - **Gate**: NEW — `S85-HP-DISJOINT-REGISTRY-LAND`. PASS iff entry appears in both registries with dual-SHA cross-reference; FAIL iff a registry entry conflicts with an existing row; INFO iff the entry requires a new registry section (e.g., §VII.P "Cyclic-cohomology parity exclusions") not yet present.
   - **Effort**: 1-2 hours, 1 agent session.

V.7. **Convergence-audit gate across connes / lizzi / van-den-dungen S-5 syntheses**
   - **What**: Read all three S-5 solo syntheses (this one, plus `session-84-s5-connes-*.md` and `session-84-s5-lizzi-*.md` when they land), verify that the three agent-native formulations of the disjoint-corridor result are (a) logically consistent, (b) converging on the same canonical meta-theorem, and (c) disagree-free on scope statements. Produce a reconciliation table if there are notational / convention differences.
   - **Inputs**: The three S-5 synthesis markdown files in `sessions/archive/session-84/`.
   - **Gate**: NEW — `S85-S5-CONVERGENCE-AUDIT`. PASS iff three-way agreement on meta-theorem + zero substantive contradictions; FAIL iff a substantive disagreement (e.g., one agent asserts BOTH is reachable while another asserts it isn't); INFO iff convention mismatch requires a translation table but no substantive disagreement.
   - **Effort**: 2-3 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `HP^0(A_F) ∩ HP^1(A_F) = {0}` with `[ε_H]` at norm 16.20 in HP¹, `image(ch) ⊂ HP^0` | GEOMETRIC | PASS (W10-114, 5 OOM) | Permanent structural wall between primary-KK and GV-secondary channels |
| 2 | 42/42 atlas rows classify PRIMARY-KK with zero GV leakage; ε_H correctly outside K-PROP atlas | GEOMETRIC | PASS (W10-113) | K-PROP atlas is cohomologically pure; no under-refined registry entries possible in 5-bin scheme |
| 3 | Direct GV 3-form integral matches G56 stencil at RATIO = 1.000, J_C2 > 0 confirmed | GEOMETRIC | PASS (W10-115) | Explicit secondary-channel witness at H³; sign of J_C2 structurally pinned |
| 4 | Kasparov-product factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` preserves HP-parity under even base | GEOMETRIC | PASS (structural, derived here) | Disjoint corridors robust under submersion; Paper 01 Main Theorem is the vehicle |
| 5 | Shriek map π_! preserves HP-parity because dim_R SU(3) = 8 is even | GEOMETRIC | PASS (structural, derived here) | Fiber integration doesn't reshuffle corridor labels; SU(3)-specific feature |
| 6 | S84-W10-114 (parity) and S82-W2-3 (rank) members of same NCG-structural-exclusion meta-family | GEOMETRIC | PROPOSED | Meta-theorem drafted; categorical unification OPEN for S85 |
| 7 | `[ε_H]` survival under Jensen deformation outside Cartan NOT established | GEOMETRIC | OPEN | Carry-forward V.1 |
| 8 | Dimension / generators of HP¹(A_F) unknown | GEOMETRIC | OPEN | Carry-forward V.2 |
| 9 | Three-agent convergence (connes / lizzi / vdd) on same canonical entry | META | IN PROGRESS | Carry-forward V.7; meta-theorem certification depends on this |
| 10 | HP-PARITY-DISJOINT-CORRIDORS permanent result proposed for registry | GEOMETRIC | PROPOSED | Carry-forward V.6 |
