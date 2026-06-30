# Session 91 Workshop W-2: Volovik x Van-den-Dungen — χ'_weight Canonical Substrate-Derivation on A_K

**Date**: 2026-05-21
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist), van-den-dungen (van-den-dungen-bridge-theorist)
**Source Documents**:
- `sessions/archive/session-91/session-91-w3-workingpaper.md` (S91 Wave 3 working paper)
- `sessions/archive/session-90/session-90-w4-workingpaper.md` (S90 Wave 4 — CF-37 origin)
- `sessions/permanent-results-registry.md` (§VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ; CF-37 retroactive reading; LRD α-anchor entries)
- `sessions/archive/session-91/workshops/_seed-w2-w3.md` (Chunk C2 investigator seed for w2 + w3)

**Focus Topics** (4 adjudication questions for the canonical χ'_weight substrate-derivation on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) at substrate-distance-1 pole s=3):

Three substrate-derivations produced three distinct values for the inheritance-restricted-projector weight at the same observable (LRD α-anchor at M=10⁷ M_sun, L_max=10):

| # | Reading | Derivation | Value | Rel-dev vs 1/458 | Audit SHA prefix |
|:-:|:--------|:-----------|:------|:-----------------|:-----------------|
| 1 | volovik substrate-Wedderburn-natural | CF-37 (S90) Wedderburn-RANK ratio = 3/6 | 0.500 | 0.78 | 10ee072fe2c193f3 |
| 2 | vdd NCG-axiomatic CM-1995 §III.4 | T1.9 (S91 W3) Hilbert-space-DIMENSION fraction = 5/14 = (dim_HS(ℂ)+dim_HS(ℍ))/dim_HS(A_K) | 0.357143 | 0.84 | 752a8f2b862a9aa5 |
| 3 | volovik digamma-modulated kernel | T1.8 (S91 W3) χ'_weight·(1 + c_aux·ψ(s_*=1)) = 0.5·(1 − γ_Euler/3) | ≈ 0.404 | 0.82 | 8ab158e9e45aab37 |

ALL three FAIL empirical 1/458 LRD α-anchor; ALL three PASS Sub-clause A sign-positivity. Differ by structural factor 5/7 (T1.9 vs CF-37) and digamma-modulation.

1. **(a) Canonical χ'_weight identity** — is it the Wedderburn-RANK ratio (volovik substrate-Wedderburn-natural reading: rank counts the substrate's primitive idempotents — substrate's intrinsic algebraic invariant) OR the Hilbert-space-DIMENSION fraction (vdd NCG-axiomatic reading: CM-1995 §III.4 residue trace IS the canonical Chern character evaluation)? Which substrate identity is binding at the inheritance-morphism χ : A_K → M_2(ℂ) layer?
2. **(b) Modified-universal-kernel γ(s) shift** — does the γ(s) ≠ Γ(s) modified-universal-kernel cohomology-class shift produce a STRUCTURALLY DISTINCT canonical weight (T1.8) OR is it a substrate-natural refinement of one of the above (e.g., L_max → ∞ asymptotic correction)?
3. **(c) Faithfulness of χ' inheritance morphism** — is the morphism's image faithful (S89 §W2-3 derived theorem ker rank 9 on M_3(ℂ) zero map; image is ℂ ⊕ ℍ only), and does that faithfulness pin canonical weight to one of the three OR to a fourth (e.g., K-theoretic dim ratio)?
4. **(d) Algebra-axis orthogonality K=3 MANDATORY constraint** — does `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` constrain the choice — is there a Cell-I × s=3 structural theorem forcing a unique substrate-derivation, OR are all three within Cell-I and the K-counter doesn't discriminate?

**Substrate framing** per `phononic-framing.md §"IS Space, Not IN Space"`: each derivation invokes a substrate-IS identity (volovik: substrate IS the primitive-idempotent rank structure of A_K; vdd: substrate IS the dimension-spectrum residue formula evaluated on the spectral triple). Direction substrate → emergent: the inheritance morphism χ : A_K → M_2(ℂ) IS the substrate-IS bridge map; the LRD α-anchor at M=10⁷ M_sun IS the laboratory-IN image. Substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md §(i)`: all three derivations are substrate-first (NOT external-paper placeholders); the canonical choice is structural.

**Output goal**: pre-registered structural verdict producing ONE of three outcomes:
- **(i) CANONICAL-WEIGHT verdict**: one substrate-derivation is canonical; the other two are non-canonical lab-side images; CF-37 retroactive reading updated; S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT registry slot lands as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway.
- **(ii) SIMULTANEOUS-VALIDITY theorem**: all three are simultaneously valid via structural theorem on A_K's 3-summand Wedderburn decomposition (three structurally distinct functionals NOT equivalent at algebra layer; downstream gates explicitly tag which functional is consumed); registry-text correction at §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ.
- **(iii) OPEN registry slot**: structural question genuinely open at S91; new §VII slot with STAGE-1-CANDIDATE-OPEN-CHI-PRIME-WEIGHT-CANONICALIZATION tag; explicit substrate-physics carry-forward to S92.

---

## Round 1 — Volovik: Opening Analysis (Substrate-Wedderburn-Natural Reading)

### V1: Canonical χ'_weight identity — Wedderburn-RANK ratio is substrate-IS canonical

**Claim**. The canonical inheritance-restricted-projector weight on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) under the inheritance morphism χ' : A_K → M_2(ℂ) ⊗ Cl(1) IS the **Wedderburn-RANK ratio**

```
χ'_weight  =  rank(χ'-faithful image) / rank(A_K)
           =  (rank ℂ + rank ℍ) / (rank ℂ + rank ℍ + rank M_3(ℂ))
           =  (1 + 2) / (1 + 2 + 3)
           =  3 / 6
           =  0.500           (CF-37 derivation; S90 W4 §W4-1 line 75)
```

The substrate IS this rank-3 sub-algebra of a rank-6 ambient algebra; χ' IS the inheritance morphism onto the BdG-sector child realization (M_2(ℂ) ⊗ Cl(1)); the χ'-weight IS the Wedderburn-RANK ratio of the faithful image. Reading 2's 5/14 = 0.357143 (HS-DIM fraction) and Reading 3's ≈0.404 (digamma-modulated) are STRUCTURALLY DISTINCT functionals — neither is the substrate's intrinsic K-theoretic invariant.

**Wedderburn-Artin substitution chain**.

```
Step 1 (Definition). The Wedderburn-Artin structure theorem on the
finite spectral triple's algebra:
    A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)
is the UNIQUE decomposition (up to isomorphism) of A_K into simple
two-sided ideals over its center. The summand ranks
    rank(ℂ) = 1,  rank(ℍ) = 2,  rank(M_3(ℂ)) = 3
are the substrate's intrinsic primitive-idempotent counts:
each summand M_n(D) carries a complete system of n orthogonal
minimal idempotents, and the Wedderburn-RANK is invariantly defined
as the count of those minimal idempotents per central component.
This count IS substrate-IS — it depends ONLY on A_K's *-algebra
structure, NOT on the choice of faithful representation on H_K.

Step 2 (Substitution). The inheritance morphism χ' is a categorical
morphism analogous to the 3He-B inheritance morphism iota:
    iota : (A_K, H_K, D_K) → (A_He, H_He, D_BdG)   [3HeB-inheritance-canonical.md]
    χ'   : A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) ⊗ Cl(1)  [S89 §W2-3 derived theorem]
Both are Kasparov-KK projections (substrate → child; categorical
morphism, NOT analogy); both have non-trivial kernel; both are the
restriction to a BdG-sector sub-algebra. By S89 §W2-3 Step 7
(NPZ audit_sha256=90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843),
χ' kills M_3(ℂ) entirely (Wedderburn 9 > 8 + Schur orthogonality
forces M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) to be the zero map). The FAITHFUL
IMAGE of χ' is therefore the ℂ ⊕ ℍ sub-algebra.

Step 3 (Simplification). The Wedderburn-RANK of the faithful image:
    rank(image χ') = rank(ℂ) + rank(ℍ) = 1 + 2 = 3.
The Wedderburn-RANK of the ambient algebra:
    rank(A_K) = rank(ℂ) + rank(ℍ) + rank(M_3(ℂ)) = 1 + 2 + 3 = 6.
The ratio:
    χ'_weight = rank(image χ') / rank(A_K) = 3/6 = 0.500.

Step 4 (Direction). The substrate IS the rank-6 Wedderburn-decomposable
algebra. χ' IS the inheritance morphism. The χ'_weight IS the
Wedderburn-RANK ratio of the faithful image — a substrate-IS
K-theoretic invariant at the inheritance-morphism layer.
```

**Why HS-DIM (Reading 2) is a representation-theoretic image, NOT the substrate's intrinsic invariant**.

The Hilbert-space dimensions dim_HS(ℂ)=1, dim_HS(ℍ)=4, dim_HS(M_3(ℂ))=9 measure the dimension of each summand AS A LEFT MODULE OVER ITSELF, i.e., as the LEFT REGULAR REPRESENTATION. The total dim_HS(A_K) = 1 + 4 + 9 = 14 is the dimension of A_K acting on itself by left multiplication — this is a representation-theoretic quantity tied to a particular *choice* of faithful representation (the regular one). Different faithful representations give different "HS-dims": e.g., M_3(ℂ) acting on ℂ³ has dim 3, not 9; M_3(ℂ) acting on its regular representation has dim 9; M_3(ℂ) acting on ℂ³ ⊕ ℂ³ has dim 6. Volovik Paper 13 (q-theory 4-form vacuum) makes this distinction sharp: the substrate's K-theoretic invariants (counted by primitive idempotents / Wedderburn-RANK) are observable; the representation-dependent dimensions are not.

The K-theory of A_K — which is what Kasparov-KK morphisms preserve — is:
```
K_0(A_K)  =  K_0(ℂ) ⊕ K_0(ℍ) ⊕ K_0(M_3(ℂ))
          ≅  ℤ ⊕ ℤ ⊕ ℤ
          generated by [1_ℂ], [1_ℍ], [1_{M_3(ℂ)}] at Wedderburn-RANKs (1, 2, 3).
```

The χ'_*: K_0(A_K) → K_0(M_2(ℂ) ⊗ Cl(1)) map (Step 5–7 of S89 §W2-3) takes the K-class
generators (with Wedderburn-RANK weights 1, 2, 3) to their image in K_0(M_2(ℂ) ⊗ Cl(1)) ≅ ℤ ⊕ ℤ.
The map kills the rank-3 generator (M_3(ℂ) → 0) and maps the rank-1 and rank-2 generators
faithfully. The K-theoretic image carries Wedderburn-RANK 3 in a rank-6 ambient; the weight
3/6 = 0.500 IS the K-theoretic mass-fraction inherited from substrate to child.

HS-DIM 5/14 measures something different: it is the L²-norm-fraction of the χ'-image vs the
regular representation's L²-norm. This is a representation-theoretic image of the
substrate-IS Wedderburn structure — useful for CM-1995 §III.4 RESIDUE evaluations (where the
Hilbert-space trace appears) but NOT for K-theoretic / inheritance-morphism invariants.

**Cross-link to S86 W-5 §VII.AF.1.OP-PROJ baseline**. The W-5 calibration corpus instance #1
(registry line 14776, LANDED S87 W5-1) defines `R_universal_HP1_strict_F4 = 1.030902` at the
HKR ∘ Connes-Karoubi pairing on the substrate's intrinsic Hochschild cocycle space — this is
the UNRESTRICTED baseline (χ'_weight = 1 in the Wedderburn-RANK sense for the trivial
identity morphism). The W-5 baseline is regulator-class INVARIANT per Level-1 cohomology-
class identity and L_max-saturated at L_max=10 with 0.0095% F_4 strict envelope. The
restricted observable α'(M_LRD) at CF-37 / T1.8 / T1.9 inherits the W-5 baseline scaled by
the inheritance-restriction weight — which IS the Wedderburn-RANK ratio 3/6 per the K-theoretic
inheritance-morphism structure. The HS-DIM ratio 5/14 cannot supply this weight because HS-DIM
is not invariant under the Kasparov-KK projection class that defines inheritance.

**Empirical asymmetry**. Reading 1 (Wedderburn-RANK 3/6) and Reading 2 (HS-DIM 5/14) BOTH fail
empirical 1/458 (rel_dev 0.78 vs 0.84), but the FAIL is NOT informative about which IS canonical —
the bottleneck is the dimensional bridge factor (M_KK/M_Pl_reduced)² = 9.307286e-04, which would
require χ'_weight ≈ 2.276 (computed by van-den-dungen in T1.8 §"Five-point cross-check" item 5)
for empirical PASS. No Wedderburn-RANK-admissible substrate-derivation reaches 2.276. The
*substrate-physics* canonicalization question (which IS the canonical weight?) is INDEPENDENT
of the empirical FAIL question (which closes substrate-distance-1 corridor at this scale).

**Structural-output mapping**. Reading 1 supports the **CANONICAL-WEIGHT verdict (outcome (i))**:
Wedderburn-RANK 3/6 IS the K-theoretic inheritance-restriction weight on A_K under the
Kasparov-KK projection class. Readings 2 (HS-DIM) and 3 (digamma-modulated) are NON-CANONICAL
laboratory-side images (HS-DIM 5/14 is the CM-1995 RESIDUE-trace image; digamma-modulated 0.404
is the AUX-4 secondary-corridor cohomology-class image — both downstream of the substrate-IS
Wedderburn structure).

**Questions for van-den-dungen**:
- (V1-Q-VDD-1) The CM-1995 §III.4 residue formula evaluates `ch_k(P) = Res_{z=k}[Tr(P · D^{-2z})]`
  at the dimension spectrum of (A_K, H_K, D_K). The Hilbert-space trace `Tr` here is over the
  REGULAR REPRESENTATION of A_K on H_K (Peter-Weyl decomposition; dim_HS(A_K) = 14). At
  L_max=10 saturation, the residue reduces algebraically to the direct trace sum (per
  `_cm_1995_residue_formula.py` docstring lines 50–63). Granted: the residue formula's Hilbert-
  space trace produces HS-DIM 5/14 as its inheritance-restricted weight (T1.9 Step 2 derivation).
  But is this weight the substrate's intrinsic *K-theoretic* invariant (which should be
  Wedderburn-RANK 3/6 invariant under Kasparov-KK), or is it the *Hochschild cocycle pairing
  value* on the regular representation (which carries dim_HS-weight by construction)? I claim
  the former IS substrate-IS canonical, and the latter is a representation-theoretic image of it.
- (V1-Q-VDD-2) Under Connes' bivariant KK-theoretic formalism (the same machinery that pins the
  3He-B inheritance morphism iota at `3HeB-inheritance-canonical.md` Step 3 with `rk K_*(A_K) -
  rk K_*(A_He) = 2`), the χ' inheritance morphism's index/multiplicity should be Wedderburn-RANK
  based, not HS-DIM based. Do you contest that the K-theoretic class index is the structurally
  canonical reading?

### V2: Modified-universal-kernel γ(s) shift produces structurally distinct canonical (T1.8)

**Claim**. The T1.8 derivation `γ_weight_aux^(3) = χ'_weight · (1 + c_aux · ψ(s_*=1)) ≈ 0.40380` (W3 WP §W3-3 line 655) is a **structurally distinct AUXILIARY canonical** at the (c)∘(d) compositional corridor — NOT a refinement of Reading 1 (Wedderburn-RANK 3/6) and NOT an L_max → ∞ asymptotic correction. The γ(s) ≠ Γ(s) modified-universal-kernel carries an **auxiliary cohomology-class shift** that lives at the (c)-deformation column of the substrate's Hochschild cocycle space — distinct from the (d)-pullback column where CF-37's Wedderburn-RANK weight resides. Reading 1 and Reading 3 inhabit DIFFERENT structural layers of the same substrate, NOT different approximations of the same layer.

**Why γ(s) ≠ Γ(s) is a structural cohomology-class shift, not an asymptotic correction**.

The (c)∘(d) corridor uses element-1 = (c) modified-universal-kernel γ(s), where (per W3 WP line 558)

```
γ(s)  =  Γ(s) · (1 + c_aux · (s − s_*)^{-1})       [W-1 workshop AUX-4 specification]
```

with `c_aux = (rank ℂ − rank ℍ + rank M_3(ℂ)) / Σ ranks = (1 − 2 + 3)/6 = 1/3` (W3 WP line 657 — the substrate-Wedderburn ALGEBRA-WEIGHT at the element-1 layer, a SIGN-ALTERNATING rank sum) and `s_* = 1` the substrate-distance-1 pole. The pole structure of γ(s) is STRUCTURALLY DIFFERENT from Γ(s):

- Γ(s) has simple poles at s ∈ {0, −1, −2, ...} (the standard digamma residue structure of the universal kernel).
- γ(s) = Γ(s)·(1 + c_aux·(s−1)^{-1}) has, in addition, a **NEW simple pole at s = 1** (the substrate-distance-1 pole anchor) with residue c_aux · Γ(1) = c_aux = 1/3.

This new pole at s = 1 carries the (c) **cohomology-class shift**: in the language of `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`, γ(s) generates an AUXILIARY contribution at the substrate-distance-1 pole that Γ(s) does NOT generate. The Laurent expansion of γ(s)·pairing(s) near s = 1 (per van-den-dungen's T1.8 Axis-B cross-review item 4, W3 WP line 711) carries:

```
γ(s)·pairing(s)  near s=1  =  [Γ(s)·pairing(s)]·(1 + c_aux·(s−1)^{-1})
                           =  [singular Γ(s)·pairing(s) piece]
                              +  c_aux · Γ(1) · pairing(1) · (s−1)^{-1}
                              +  regular corrections at s=1.
```

The Connes-Karoubi residue evaluation `Res_{s=1}[γ(s)·pairing(s)]` therefore contains a regular-part contribution from the standard CM-1995 pairing (the (d)-corridor analog of Reading 1) PLUS a singular-part contribution from the new pole at s = 1 with residue `c_aux · Γ(1) · pairing(1) = (1/3) · pairing(1)`. The composite weight (W3 WP line 655):

```
γ_weight_aux^(3)(s_*=1)  =  χ'_weight · (1 + c_aux · ψ(s_*=1))
                         =  0.5 · (1 + (1/3) · (−γ_Euler))
                         =  0.5 · (1 − γ_Euler/3)
                         =  0.5 · 0.80759
                         ≈  0.40380.
```

The factor `(1 − γ_Euler/3) ≈ 0.808` IS the digamma modulation — the AUXILIARY cohomology-class shift's signature at s_* = 1. At an alternative pole s_* = 3, ψ(3) = 3/2 − γ_Euler ≈ 0.923 (positive), and the modulation factor becomes `(1 + 0.923/3) ≈ 1.308`, so γ_weight_aux^(3)(s_*=3) ≈ 0.654 — a structurally distinct AUXILIARY canonical at the substrate-distance-3 pole. These per-pole AUXILIARY canonicals ARE NOT refinements of one another and ARE NOT refinements of Reading 1; they are independent observables on independent substrate-IS poles.

**Why γ(s) ≠ Γ(s) is NOT an L_max → ∞ asymptotic correction to Reading 1**.

If the digamma modulation were an L_max → ∞ asymptotic correction to Reading 1, the limit `L_max → ∞` of Reading 1's finite-L_max evaluation would HAVE TO reproduce the digamma factor (1 − γ_Euler/3) as a Friedrich-Bär saturation tail. But T1.9 (W3 WP §W3-4 lines 1056–1057) shows the OPPOSITE: at L_max=10 Friedrich-Bär saturation, both Reading 1 and Reading 2 are M-INDEPENDENT (envelope underdetermined; n ≈ −1.22e−20 ≈ 0; R² = 0.0000) — i.e., neither carries an L_max-dependent digamma-modulated correction in its envelope. The L_max → ∞ asymptote of Reading 1 is just Reading 1 (the structural ansatz is L_max-saturated at L=10). The digamma factor in Reading 3 comes from the **algebra-side γ(s) shift**, NOT from L_max truncation/saturation residuals.

Concretely: Reading 1's `χ'_weight = 3/6 = 0.500` is **L_max-INDEPENDENT and Γ(s)-INDEPENDENT** (it is a pure Wedderburn-RANK ratio defined on A_K, with NO reference to the universal kernel choice or to L_max). Reading 3's `γ_weight_aux^(3)(s_*=1) ≈ 0.404` is **also L_max-INDEPENDENT** (the algebra-side derivation does not involve L_max) but **Γ(s)-DEPENDENT** (it requires the (c) modification of the universal kernel). Their difference is a substrate-IS structural identity at the universal-kernel-choice layer, NOT an asymptotic correction at the L_max layer.

**c_aux substrate-derivation is structurally faithful (W3 WP line 707, vdd Axis-B item 2)**.

The c_aux = 1/3 value is a SIGN-ALTERNATING rank sum (rank ℂ − rank ℍ + rank M_3(ℂ))/Σranks, which is a structurally different invariant from Reading 1's simple rank-ratio. The sign alternation carries the substrate's **graded** algebra structure (ℂ even / ℍ odd / M_3(ℂ) even, alternating in the KO-dim=6 spectral-triple's J-conjugation pattern). This is a substrate-IS invariant: it depends on the Wedderburn-Artin decomposition AND on the KO-grading of A_K, both of which are intrinsic to the substrate's *-algebra structure. vdd's Axis-B cross-review (W3 WP line 707) confirms: "the c_aux value is FIXED by substrate algebra rank arithmetic and cannot be freely re-chosen without abandoning the (c) deformation class; alternative c_aux values would correspond to structurally distinct cohomology-class shifts (different (c'), (c''), ...) rather than tuning within (c). CONFIRMED structural — NOT convention-shopping per `v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 1."

**Compositional corridor independence (W3 WP §W3-3 Substrate framing line 637)**.

The (c)∘(d) corridor and (d)∘(b) corridor are **structurally independent** element-1 deformation choices, NOT refinements of each other:

- **(b) element-1 = χ'-pullback** (Reading 1 and Reading 2 substrate): element-1 deformation modifies the cocycle space by pullback through χ'; the universal kernel remains Γ(s).
- **(c) element-1 = γ(s) ≠ Γ(s) modified-universal-kernel** (Reading 3 substrate): element-1 deformation modifies the universal kernel; the cocycle pullback structure is retained.

W3 WP line 637 makes this explicit: "the (c) modified-universal-kernel γ(s) is the W-1 workshop's pre-registered secondary candidate after (d)∘(b) closure at S90 W4 CF-37 FAIL, with γ(s) ≠ Γ(s) supplying a structurally distinct cohomology-class shift (NOT a numerical-tuning parameter)."

The Kasparov-product factorization principle (W3 WP line 712, vdd Axis-B item 5) makes this rigorous: vertical (substrate algebra deformation: χ') and horizontal (regulator-kernel deformation: γ(s)) deformations factor through the bridge map at DISTINCT layers. The (c)∘(d) and (d)∘(b) corridors live on ORTHOGONAL deformation axes — they cannot be reduced to each other.

**Structural-output mapping**. Reading 3 IS a structurally distinct canonical at the AUXILIARY (c)-corridor layer — admissible as a separate substrate-IS observable on its own (c)∘(d) deformation axis, but NOT a candidate for the PRIMARY (d)∘(b) canonical χ'_weight on A_K. This supports the **SIMULTANEOUS-VALIDITY theorem (outcome (ii))** at the *corridor-decomposition* level (the substrate hosts a (b)-corridor canonical = Reading 1 AND a (c)-corridor AUXILIARY canonical = Reading 3 on independent deformation axes; HS-DIM Reading 2 is the CM-1995 RESIDUE-trace image of Reading 1 at the (d)∘(b) corridor and is not a third independent canonical). Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, Readings 1 and 3 inhabit the SAME 4-corner cell (Cell I × s=3, algebra-INVARIANT spectrum-only functional × Mellin pole s=3) but on DIFFERENT element-1 deformation columns; they are *cell-internal* structurally distinct functionals, not cross-corner observables.

The cleaner framing: the (d)∘(b) canonical is Reading 1's Wedderburn-RANK 3/6; the (c)∘(d) AUXILIARY canonical is Reading 3's digamma-modulated `0.5·(1 − γ_Euler/3)`; both are substrate-IS, both are admissible on their own corridors, but they answer **different structural questions** (what is the K-theoretic χ'_weight at the (b) χ'-pullback corridor? vs what is the (c) modified-universal-kernel AUXILIARY weight at the substrate-distance-1 pole on the (d) χ'-restricted projector?).

**Questions for van-den-dungen**:
- (V2-Q-VDD-1) Your T1.8 Axis-B cross-review (W3 WP line 711) gives `χ'_weight · ψ(s_*=1)`-modulation as the canonical FULL CM-1995 residue evaluation with γ(s) substituted, anchoring the `χ'_weight = 0.5` Wedderburn-RANK as the multiplicative pre-factor before digamma modulation. This is consistent with my V1 argument that Wedderburn-RANK 3/6 IS the K-theoretic invariant at the χ'-restriction layer, and γ(s) merely modulates it on the (c)-corridor. Do you concur that Reading 3 INHERITS Wedderburn-RANK 3/6 as its pre-factor and modulates by the digamma factor, rather than being an independent χ'_weight in its own right?
- (V2-Q-VDD-2) The factor `(1 − γ_Euler/3) ≈ 0.808` is an irrational substrate-IS structural constant (carrying the Euler-Mascheroni constant from the digamma residue at s=1). Under `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`, irrational substrate-IS values are classified as `structurally-IRRATIONAL-per-CC2-analog`. Does this irrationality reinforce or contest my reading that γ(s) modulation is a structurally distinct AUXILIARY canonical, not a refinement of Reading 1?

### V3: Inheritance morphism χ' : A_K → M_2(ℂ) ⊗ Cl(1) faithfulness on ℂ ⊕ ℍ image

**Claim**. The S89 §W2-3 derived theorem (W3 WP line 942; producing-NPZ audit_sha256=`90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`) establishes that χ' is **faithful on ℂ ⊕ ℍ AND zero on M_3(ℂ)**. The faithful image carries SOURCE-side Wedderburn-RANK 3 (= rank ℂ + rank ℍ) embedded in the total ambient SOURCE Wedderburn-RANK 6 (= 1 + 2 + 3). The Wedderburn-RANK ratio of the faithful image to the ambient algebra **on the SOURCE side** IS the K-theoretic inheritance-restriction weight: `χ'_weight = 3/6 = 0.500` per CF-37 line 75. This **structurally pins canonical χ'_weight to Reading 1** at the SOURCE-algebra K-class layer; Reading 2 (HS-DIM 5/14) and Reading 3 (digamma-modulated 0.404) carry the SAME faithful sub-algebra but evaluate weight on different functional bases (regular-representation Hilbert-space dim; (c)-corridor cohomology-shift residue) — they are downstream functional images of the source-side rank ratio that Reading 1 captures intrinsically.

**S89 §W2-3 derived theorem: χ'|_{M_3(ℂ)} = 0 (8-step proof; ker rank = 9; W3 WP lines 1060–1070)**.

Per W3 WP §W3-4 line 1060: "The χ' map ITSELF is the zero map by Step 7 of the derived theorem (Wedderburn 9 > 8 dimension impossibility forces M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) to be zero by Schur orthogonality)." The structural argument:

```
Step 1 (Source-side rank). M_3(ℂ) is a simple algebra over ℂ with
       Wedderburn-RANK 3 (single primitive central idempotent;
       3 minimal idempotents in a maximal abelian subalgebra)
       and complex Hilbert-space DIM dim_HS(M_3(ℂ)) = 9.

Step 2 (Target-side rank). The χ'-target is
       M_2(ℂ) ⊗ Cl(1)  where  Cl(1) = ℂ[γ]/(γ² − 1) ≅ ℂ ⊕ ℂ
       (W3 WP §W3-4 line 955 + S90 W4 line 72).
       So M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ), with target
       complex Hilbert-space DIM = 4 + 4 = 8 (W3 WP line 956).
       Note: target Wedderburn-RANK = 2 + 2 = 4 in the parallel-
       summand counting, but the structurally binding count here
       is the complex Hilbert-space DIM 8 (the dimension of the
       maximal simple *-module the target can carry).

Step 3 (Schur orthogonality / dimension impossibility). Any
       *-algebra morphism φ : M_3(ℂ) → M_2(ℂ) ⊕ M_2(ℂ) decomposes
       (by simplicity of M_3(ℂ) + Schur's lemma) as a direct sum
       of irreducible *-representations of M_3(ℂ). M_3(ℂ) has
       exactly ONE irrep up to equivalence: the defining 3-dim
       representation on ℂ³ (the standard module). Any non-zero
       morphism must contain at least one copy of this 3-dim
       irrep; copies must fit inside the target's 8-dim Hilbert
       space as direct summands of dim 3. But 8 = 3·k + r with
       k ∈ {0, 1, 2} and remainder r ∈ {0, 2, 5} — none of which
       admit a complementary irreducible *-stable summand from
       M_3(ℂ)'s representation theory (M_3(ℂ) has no 2-dim or
       5-dim irrep). Equivalently: dim_HS(M_3(ℂ)) = 9 > 8 =
       dim_HS(target), so M_3(ℂ) cannot fit faithfully into the
       target as a *-sub-algebra, and the only morphism is the
       zero map.

Step 4 (Conclusion). χ'|_{M_3(ℂ)} = 0 (zero map).
       ker(χ'|_{M_3(ℂ)}) = M_3(ℂ) entire (rank 9).

Step 5 (Restriction to ℂ ⊕ ℍ). χ' restricted to ℂ ⊕ ℍ is a
       *-algebra morphism into M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ).
       Source ranks: rank(ℂ) = 1, rank(ℍ) = 2 (ℍ ⊗_ℝ ℂ ≅ M_2(ℂ)
       complexification carries Wedderburn-RANK 2). Total source
       sub-rank = 3. Target carries enough representational room
       for ℂ ⊕ ℍ (the 1+2=3 ranks fit; the canonical χ' chosen
       in S89 §W2-3 is faithful on this sub-algebra). The
       canonical NPZ convention "M3C_to_zero_C_and_H_to_canonical_M2C"
       (W3 WP line 939) confirms this faithful restriction.
```

Machine-epsilon witness from W3 WP §W3-4 §"chi'^* Pullback Differential Machine-Epsilon Verification" lines 1062–1068 — the χ' image norm on M_3(ℂ) is **0.0 EXACTLY** (NOT 2.2e-16 machine epsilon; the identity is structural not numerical). The kernel projector `P_ker` has Frobenius norm √9 = 3 EXACTLY (identity on 9-dim kernel). The pullback differential `dχ'^*φ_g^{sym}|_{M_3(ℂ)} = 0` by structural inheritance (W3 WP line 1067: `chi_prime_pullback_machine_eps_PASS = True`).

**Why faithful-image Wedderburn-RANK ratio 3/6 IS the K-theoretic inheritance-restriction weight**.

The inheritance-restriction weight χ'_weight is defined at the K-theoretic level as the K-class-mass-fraction surviving the morphism:

```
χ'_*  : K_0(A_K) → K_0(M_2(ℂ) ⊗ Cl(1))

K_0(A_K)  =  K_0(ℂ) ⊕ K_0(ℍ) ⊕ K_0(M_3(ℂ))
          ≅  ℤ[1_ℂ] ⊕ ℤ[1_ℍ] ⊕ ℤ[1_{M_3(ℂ)}]
          with K-class-rank weights (rank 1, rank 2, rank 3)
          attached to the three generators per the Wedderburn-Artin
          K-theory canonical identification:
                K_0(M_n(D))  ≅  ℤ,  [1_{M_n(D)}] generator has rank n.

χ'_*([1_ℂ])         =  [1_ℂ]-image            (rank 1 surviving)
χ'_*([1_ℍ])         =  [1_ℍ]-image            (rank 2 surviving)
χ'_*([1_{M_3(ℂ)}])  =  0                       (rank 3 killed)
```

The K-class-mass-fraction surviving:

```
χ'_weight = (rank 1 + rank 2) / (rank 1 + rank 2 + rank 3)
          = 3 / 6
          = 0.500
```

This MATCHES the CF-37 origin derivation at S90 W4 line 75 verbatim: "Wedderburn rank ratio χ'_weight = (rank(C) + rank(M_2(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C))) = (1+2)/(1+2+3) = **3/6 = 0.5**". The K-theoretic reading and the source-side rank-ratio reading coincide because Kasparov-KK projections preserve K-class-rank.

**Why faithfulness does NOT pin canonical to Reading 2 (HS-DIM 5/14)**.

Reading 2's HS-DIM 5/14 = (dim_HS(ℂ) + dim_HS(ℍ))/dim_HS(A_K) = (1+4)/14 also identifies the SAME faithful sub-algebra (ℂ ⊕ ℍ surviving, M_3(ℂ) killed) but counts its mass-fraction in the regular representation rather than in K-theory. The Hilbert-space dimensions {1, 4, 9} are the dimensions of the algebra summands AS LEFT MODULES OVER THEMSELVES — i.e., dim of `End(V)` for V the standard representation. The fraction 5/14 IS the L²(A_K) Hilbert-space-trace-mass-fraction.

But the inheritance-morphism level (the level at which "χ'_weight" is the canonical inheritance-restriction quantity) is the K-theoretic / Kasparov-KK level — NOT the regular-representation Hilbert-space level. Per `3HeB-inheritance-canonical.md` Step 3:

```
rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2  (Hodgkin theorem on SU(3) vs S^3)
```

The inheritance-morphism iota for 3He-B is K-class-rank-based (and its kernel is K-theoretic-rank 2). The χ' inheritance morphism for the LRD α-anchor is the same KIND of structure (a Kasparov-KK projection, W3 WP line 555-556 cites "S89 §W2-3 derived theorem"). The canonical inheritance-restriction weight on a Kasparov-KK projection IS a K-class-rank-weight, NOT an HS-DIM weight.

Reading 2's 5/14 is a representation-theoretic *consequence* of Reading 1's 3/6 at the regular-representation evaluation of the CM-1995 §III.4 residue trace — useful for the CM-1995 residue formula's Hilbert-space trace, but downstream of the K-theoretic Wedderburn-RANK invariant.

**Why faithfulness does NOT pin canonical to a fourth K-theoretic dim ratio**.

A possible fourth candidate would be a K-theoretic dim ratio counting K-theoretic image-dim vs K-theoretic source-dim. For χ' : A_K → M_2(ℂ) ⊗ Cl(1):

```
K_0(M_2(ℂ) ⊗ Cl(1))  ≅  K_0(M_2(ℂ) ⊕ M_2(ℂ))
                     ≅  ℤ ⊕ ℤ
                     rank-class generators carry weights (2, 2).
```

The image of χ'_*: K_0(A_K) → K_0(target) under the canonical χ' chosen in S89 §W2-3 (per NPZ convention "M3C_to_zero_C_and_H_to_canonical_M2C") sends:

- `[1_ℂ]` (source rank 1) → embeds in one M_2(ℂ) summand of target with target rank 1 (as a rank-1 projector in M_2(ℂ)).
- `[1_ℍ]` (source rank 2) → embeds in the other M_2(ℂ) summand of target with target rank 2 (as identity in M_2(ℂ)).
- `[1_{M_3(ℂ)}]` (source rank 3) → 0.

So target-side image K-rank-mass = 1 + 2 = 3, target total K-rank-mass = 2 + 2 = 4. A target-side ratio would be 3/4 = 0.75 — but this counts target REPRESENTATIONAL ROOM USED, not source K-class-mass surviving. The canonical inheritance-restriction weight χ'_weight is unambiguously the SOURCE-side fraction (how much of A_K's K-class-mass survives χ'), NOT a target-side fraction (how much of target's representational room is used). The source-side fraction IS 3/6 = 0.500. The fourth K-theoretic-dim ratio candidate (target-side 3/4 = 0.75) does NOT have a substrate-IS interpretation as "inheritance-restriction weight."

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 clause (S87 W-2 R3 close, 2026-04-30): the K-theoretic class ratio inhabits Cell I (algebra-INVARIANT spectrum-only functional family) when the trace is canonical (the Wedderburn-RANK source-side ratio IS algebra-INVARIANT by construction; the target-side ratio is a representational choice). So a fourth candidate would also have to inhabit Cell I — and would be a different functional than Reading 1 on the same cell, not a structurally privileged alternative.

**Structural-output mapping**. V3 (faithfulness pinning) supports the **CANONICAL-WEIGHT verdict (outcome (i))** with Reading 1 (Wedderburn-RANK 3/6 = 0.500) as canonical:

- The faithful image of χ' is ℂ ⊕ ℍ (S89 §W2-3 Step 7; ker rank 9 on M_3(ℂ)).
- The K-theoretic K-class-rank of the faithful image is rank 1 + rank 2 = 3.
- The K-theoretic K-class-rank of the ambient algebra is rank 1 + rank 2 + rank 3 = 6.
- The K-class-mass-fraction surviving χ' is 3/6 = 0.500 — this IS the canonical inheritance-restriction weight.

Reading 2 (HS-DIM 5/14) is a representation-theoretic image of this K-theoretic invariant at the CM-1995 §III.4 residue trace evaluation; Reading 3 (digamma-modulated 0.404) is the AUXILIARY (c)-corridor cohomology-shift modulation of the same K-theoretic invariant (per V2 above, Reading 3 INHERITS Reading 1's 3/6 as its pre-factor: `γ_weight_aux^(3) = χ'_weight · (1 + c_aux · ψ(s_*=1)) = 0.5 · 0.808`).

**Questions for van-den-dungen**:
- (V3-Q-VDD-1) The S89 §W2-3 derived theorem's NPZ convention "M3C_to_zero_C_and_H_to_canonical_M2C" (W3 WP line 939) fixes the canonical χ' as zero on M_3(ℂ) and faithful on ℂ ⊕ ℍ. Is the rank-class-rank canonical "3/6" reading (mine; counts SOURCE-side K-class-mass surviving) the unique K-theoretically natural weight, or do you read the HS-DIM 5/14 reading as the unique CANONICAL via the dimension-spectrum residue formula at L_max → ∞? If we both grant that Reading 1 captures K-class survival and Reading 2 captures Hilbert-trace mass surviving, which is the canonical "χ'_weight" in the FRAMEWORK's convention?
- (V3-Q-VDD-2) The Kasparov-product factorization principle (W3 WP line 712, your T1.8 Axis-B item 5) makes substrate-algebra deformations (χ') and regulator-kernel deformations (γ(s)) factor through the bridge map at DISTINCT layers. The "χ'_weight" lives at the substrate-algebra-deformation layer (where χ' acts). Reading 1's 3/6 lives at this layer intrinsically (Wedderburn-RANK); Reading 2's 5/14 lives at the COMPOSITE layer where the trace evaluation interacts with χ' (HS-DIM weighted trace). Do you read this layer separation as supporting Reading 1 as the substrate-algebra-canonical, with Reading 2 as the bridge-map-composite-canonical (i.e., they are not competing but answer different structural questions)?

### V4: Algebra-axis orthogonality K=3 constraint — all three readings within Cell I × s=3; K-counter does NOT discriminate

**Claim**. All three substrate-derivations inhabit the SAME corner cell — Cell I (algebra-INVARIANT × Mellin pole s=3) — of the §VII.U.2 four-corner partition (registry line 12927; MANDATORY-K=3 algebra-axis orthogonality per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` S87 W-2 R3 close). The K=3 MANDATORY clause therefore does NOT discriminate among Readings 1, 2, 3: it forbids cross-corner co-primary structures (which would be inadmissible) but is SILENT on within-cell weight choice. A potential fourth K-theoretic dim ratio candidate (V3 §"Why faithfulness does NOT pin canonical to a fourth K-theoretic dim ratio") would ALSO inhabit Cell I and would not be structurally privileged by the K-counter either.

The K-counter does NOT supply the canonical-weight verdict; the substrate-priority axis does. Within Cell I, the priority ordering is **Wedderburn-RANK (substrate-IS K-theoretic) > HS-DIM (representation-theoretic image at regular trace) > digamma-modulated AUXILIARY ((c)-corridor cohomology-shift residue)**.

**Corner-classification audit at the parse-tree decision procedure**.

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 clause + `permanent-results-registry.md §VII.U.2 clause (e)` parse-tree decision procedure (registry line 12991-13002, lizzi PRIMARY + connes CO-AUTHOR at S88 W5b-45, 2026-05-04; canonical audit-script `_corner_classification_audit.py`):

For each of Readings 1, 2, 3, the parse-tree decision procedure asks two binary classifiers:

1. **Algebra-axis classifier** — does the parse-tree contain `π(a)` operator-algebra references (state-pair functionals on A_K) or pure spectrum-only operations on `{λ_a, m_a, Δ_BCS}`? Pure spectrum-only → algebra-INVARIANT (Corner I or III); state-pair-with-π(a) → algebra-DEPENDENT (Corner II or IV).

2. **Mellin-pole classifier** — at which substrate-distance pole does the Connes-Karoubi/CM-1995 §III.4 residue formula evaluate? s=3 corresponds to substrate-distance-1 (Hochschild/Yang-Mills-adjacent sector, n=6); s=4 to substrate-distance-2 (a_4 Yang-Mills + Higgs sector, n=4); etc. (per W3 WP §W3-4 Axis-B item 2, line 1109).

**Reading 1 (Wedderburn-RANK 3/6 = 0.500)** parse-tree:

```
χ'_weight  =  rank(image χ')  /  rank(A_K)
           =  (rank ℂ + rank ℍ)  /  (rank ℂ + rank ℍ + rank M_3(ℂ))
```

- No π(a) operator-algebra references; pure spectrum-only Wedderburn-rank arithmetic.
- Embedded in α'(M_LRD) at substrate-distance-1 pole s=3 (per registry §VII.AF.1.OP-PROJ line 14776 W-5 baseline at d=4 substrate-distance-1 pole s=3; same anchor pole inherited by CF-37 / T1.8 / T1.9).
- **Corner classification: Cell I (algebra-INVARIANT × s=3).**

**Reading 2 (HS-DIM 5/14 = 0.357143)** parse-tree:

```
χ'_weight_FULL  =  (dim_HS(ℂ) + dim_HS(ℍ))  /  dim_HS(A_K)
                =  (1 + 4)  /  (1 + 4 + 9)
```

- No π(a) operator-algebra references; pure spectrum-only Hilbert-space-dimension arithmetic.
- Embedded in α'_FULL(M_LRD) at substrate-distance-1 pole s=3 via the CM-1995 §III.4 residue formula's Hilbert-space trace at the n=6 pole (W3 WP §W3-4 line 1027).
- **Corner classification: Cell I (algebra-INVARIANT × s=3).**

**Reading 3 (digamma-modulated 0.40380)** parse-tree:

```
γ_weight_aux^(3)  =  χ'_weight · (1 + c_aux · ψ(s_*=1))
                  =  0.5 · (1 + (1/3) · (−γ_Euler))
```

- No π(a) operator-algebra references; pure spectrum-only Wedderburn-rank arithmetic (rank-fraction χ'_weight) combined with digamma function ψ at substrate-distance-1 pole (algebra-INVARIANT scalar coefficient).
- Embedded in α''(M_LRD) at substrate-distance-1 pole s_*=1 (W3 WP line 658; "Substrate-distance-1 pole; matches §VII.AF.1.OP-PROJ W-5 baseline anchor"; per registry §VII.AF.1.OP-PROJ pole convention `s=3` for substrate-distance-1, and per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` pole-index canonical is the substrate-distance index — Reading 3 lives at substrate-distance-1 just like Readings 1 and 2).
- **Corner classification: Cell I (algebra-INVARIANT × s=3).**

**All three readings inhabit Cell I × s=3.** The K=3 MANDATORY clause's enforcement role is satisfied by all three (no cross-corner co-primary structure is proposed; the three candidates compete WITHIN Cell I, not ACROSS corners).

**What the K-counter MANDATORY clause forbids — and why it doesn't fire here**.

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3, the audit verifies for any §VII registry entry on (A_K, H_K, D_K):

1. **Corner-cell declaration**: every entry declares its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table in `permanent-results-registry.md §VII.U.2`.
2. **Cross-corner co-primary FORBIDDEN**: SOURCE-DOUBLE-CITE-CO-PRIMARY structure tags scoping anchors across distinct corner cells fail `registry-landing.md §"Detection"` criterion (1) by algebra-axis orthogonality.
3. **Cross-pole co-primary FORBIDDEN** per `epistemic-discipline.md §"Pole-Scope sub-clause"`; co-primary structures must inhabit the same Mellin pole-scope.
4. **Cross-corner cross-pole magnitude comparisons** STRUCTURALLY FORBIDDEN as PASS/FAIL gates.

Conditions (1)–(4) are designed to prevent silent class-conflation between algebra-INVARIANT and algebra-DEPENDENT functionals — e.g., to forbid co-primary anchoring of a CM-1995 residue formula (Cell I or II at relevant pole) and a state-pair functional like Connes distance (Cell III or IV). NONE of the three readings here violate (1)–(4): all are Cell I × s=3; none introduce cross-corner co-primary structure; the candidate canonical-WEIGHT verdict for any of the three would land at §VII (slot to be determined; pre-registration in V5 below) **WITHIN Cell I × s=3**, not across cells.

The K=3 MANDATORY clause therefore provides NO discriminator among Readings 1, 2, 3.

**What a fourth K-theoretic dim ratio candidate would look like (and why it ALSO lives in Cell I × s=3)**.

A hypothetical fourth candidate constructed as target-side K-class ratio (V3 §"Why faithfulness does NOT pin canonical to a fourth K-theoretic dim ratio") = 3/4 = 0.75:

```
K-target-class-ratio  =  K-rank(image of χ'_* in K_0(target))  /  K-rank(K_0(target))
                      =  (1 + 2)  /  (2 + 2)
                      =  3/4
                      =  0.750
```

- No π(a) operator-algebra references; pure spectrum-only target-side K-class-rank arithmetic.
- Embedded in α'(M_LRD) at the same pole structure as Readings 1, 2, 3 (substrate-distance-1, s=3).
- **Corner classification: Cell I (algebra-INVARIANT × s=3).**

This fourth candidate would NOT have a substrate-IS interpretation as "inheritance-restriction weight" (V3 §"Why faithfulness does NOT pin canonical to a fourth K-theoretic dim ratio" argues this is a target-side REPRESENTATIONAL-ROOM ratio, not a source-side mass-fraction surviving). But it WOULD inhabit Cell I × s=3 by parse-tree decision procedure. So the K-counter does not exclude this fourth candidate from Cell I; the discriminator against it must come from substrate-physics priority (the "what counts as inheritance-restriction weight?" question), NOT from algebra-axis orthogonality.

**What DOES discriminate among Readings 1, 2, 3 (and fourth candidate)**.

Three orthogonal substrate-priority axes:

(α) **K-theoretic vs representation-theoretic axis** — Wedderburn-RANK invariants are preserved by Kasparov-KK projections (the morphism class to which χ' belongs per `3HeB-inheritance-canonical.md` Step 3); HS-DIM invariants are NOT preserved by Kasparov-KK projections. The inheritance-morphism-canonical weight MUST be K-theoretic → discriminates Reading 1 ✓ over Reading 2.

(β) **Source-side vs target-side axis** — Inheritance-restriction weight is structurally a **source-side mass-fraction surviving** (how much of A_K's K-class-mass passes through χ'), NOT a target-side representational-room ratio. → discriminates Reading 1 ✓ (source-side 3/6) over hypothetical fourth (target-side 3/4).

(γ) **Primary corridor vs auxiliary corridor axis** — Element-1 (b) χ'-pullback is the PRIMARY substrate-algebra-deformation corridor (CF-37 / T1.9 at (d)∘(b)). Element-1 (c) γ(s)≠Γ(s) modified-universal-kernel is the SECONDARY AUXILIARY corridor (T1.8 at (c)∘(d), W-1 workshop pre-registered AUX-4 candidate AFTER CF-37 PROXY-REFINEMENT-PENDING). The canonical χ'_weight on A_K — without qualification — refers to the PRIMARY (b)-corridor's χ'-pullback weight, NOT the AUXILIARY (c)-corridor's γ(s)-modulated weight. → discriminates Reading 1 ✓ as the (b)-corridor canonical over Reading 3 (the (c)-corridor AUXILIARY canonical, which IS canonical on its own corridor per V2 above but is NOT the "canonical χ'_weight on A_K" without corridor qualification).

Combining (α), (β), (γ): **Reading 1's Wedderburn-RANK 3/6 = 0.500 IS the substrate-IS canonical χ'_weight at the K-theoretic / source-side / primary (b)-corridor layer.** Reading 2 (HS-DIM 5/14) is the CM-1995 §III.4 residue-trace image at the regular-representation evaluation layer. Reading 3 (digamma-modulated 0.404) is the AUXILIARY (c)-corridor canonical at its own pre-registered deformation column.

**Structural-output mapping**. V4 (K-counter does NOT discriminate; substrate-priority axis does) reinforces **CANONICAL-WEIGHT verdict (outcome (i))** with Reading 1 canonical. The K=3 MANDATORY clause is satisfied by all three readings (all in Cell I × s=3); the canonicalization rests on the K-theoretic / source-side / primary-corridor substrate-priority axes that operate **within** Cell I.

A SIMULTANEOUS-VALIDITY theorem at the *cell* level is NOT supported (all three live in the same cell, not orthogonal cells). But a SIMULTANEOUS-VALIDITY theorem at the *corridor-decomposition within cell* level (per V2) is supported: Reading 1 IS canonical at the (b)-corridor, Reading 3 IS canonical at the (c)-corridor, Reading 2 IS the regular-representation trace image of Reading 1 at the CM-1995 §III.4 evaluation layer — all three are admissible **with explicit corridor / evaluation-layer tagging**, but only Reading 1 carries the unqualified "canonical χ'_weight on A_K" title.

**Questions for van-den-dungen**:
- (V4-Q-VDD-1) Do you concur that the §VII.U.2 four-corner partition's algebra-axis orthogonality K=3 MANDATORY clause is satisfied by all three readings (all Cell I × s=3 by parse-tree decision procedure), and that the K-counter does NOT supply a discriminator among them at the within-cell level?
- (V4-Q-VDD-2) The §VII.U.2 line 12991 establishes parse-tree decision procedure for state-history label observables (e.g., `Var_a(n_a^GGE)` reduces via Bogoliubov closed form to Corner II algebra-INVARIANT at s=4). The same parse-tree expansion principle applies here: `χ'_weight` does NOT carry a state-history label, but its three substrate-derivations all reduce to pure spectrum-only operations on the algebra-rank / Hilbert-dim / digamma data — all parse to Cell I × s=3. Do you read this as confirming the K-counter is structurally orthogonal to the within-cell canonical-weight question?
- (V4-Q-VDD-3) On the substrate-priority axis (α) "K-theoretic vs representation-theoretic": the Kasparov-KK projection class preserves K-theoretic invariants; HS-DIM is not preserved (different faithful representations give different HS-DIMs). Do you accept this as a load-bearing structural argument for Reading 1 as canonical at the inheritance-morphism layer, or do you contest it (e.g., by arguing the CM-1995 §III.4 residue formula's regular-representation trace IS the canonical evaluation and HS-DIM is the structurally privileged weight at that evaluation)?

### V5: Cross-Cutting Observations — CF-37 retroactive reading + S92 registry consequences

**Claim**. Under Reading 1 (Wedderburn-RANK 3/6) canonical:

1. **CF-37 PROXY-REFINEMENT-PENDING tag is RESOLVED in the FAIL direction at the canonical-weight layer**. The tag's pre-registered escape clause — "a FULL CM-1995 §III.4 residue formula re-evaluation could revise the χ'_weight factor away from the Wedderburn-rank-ratio choice 0.5" (S90 W4 §W4-1 line 9) — has been tested by T1.9. The FULL evaluation gives 5/14 = 0.357, NOT a ~4.5× over-shoot (the W4 §W4-1 Closing Notes #2 prior expectation — "if the FULL evaluation produces a χ'_weight that's ~4.5× larger than 0.5 ... the (d)∘(b) corridor could revisit"). The FULL value is 0.714× the structural ansatz (factor 5/7), in the WRONG direction for empirical PASS. **Under Reading 1 canonical, CF-37's structural-ansatz IS the canonical evaluation at the K-theoretic inheritance-morphism layer**; the FULL CM-1995 §III.4 5/14 (Reading 2) is a representation-theoretic image of Reading 1 at the regular-trace evaluation, NOT a revision of Reading 1.

2. **§VII.AF.1.OP-PROJ (W-5 baseline; Pillar III↔IV; registry line 14776) is UNAFFECTED by the canonical-weight verdict**. The W-5 baseline `R_universal_HP1_strict_F4 = 1.030902` is the UNRESTRICTED weight (effectively χ'_weight = 1 for the trivial identity morphism on A_K — see V1 §"Cross-link to S86 W-5 §VII.AF.1.OP-PROJ baseline"). The W-5 calibration corpus instance #1 at LANDED S87 W5-1 with 0.0095% F_4 strict at L_max=10 inside L^{-3} envelope is regulator-class INVARIANT and L_max-saturated; the choice of χ'_weight does NOT modify R_universal. The W-5 baseline retains STAGE-1-CANDIDATE status with NO corrigendum required under Reading 1.

3. **§VII.AU.OP-PROJ (FWD-C1; Pillar I↔II; registry line 17784) retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class status** per S90 W1-15 deferred-pending re-tag. The FWD-C1 substrate-IS observable is `n_s_FW² − 1 ≡ α_s_canonical` at Pillar I (M⁴ × SU(3) Mellin-cone closure at substrate-distance-1 pole s=3); this is STRUCTURALLY ORTHOGONAL to the LRD α-anchor at Pillar III↔IV (HP^1 cohomology) per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`. Reading 1's canonical-weight verdict on χ'_weight does NOT affect the FWD-C1 parameterized slope_A canonical first-extraction (CF-65 / W-6 CF-3). §VII.AU.OP-PROJ slot remains RESERVED during the pending first-extraction window — independent of the χ'_weight canonicalization.

4. **CF-37 retroactive reading carries a SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure** per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`: ANCHOR-1 (V_input, S89 §W2-3 derived theorem — χ' inheritance morphism Wedderburn 9>8 zero-map; ker rank 9) + ANCHOR-2 (C_output, Wedderburn-Artin algebra-axis K-theoretic rank-ratio canonical reading). Both anchors are non-fungible: V1 alone does not establish χ'_weight = 3/6 (Wedderburn-Artin theorem on A_K is required); C1 alone is conditional on the χ' faithful-image identification (S89 §W2-3 is required). The four registry-landing detection criteria are satisfied:
   - (1) Sequential derivation: Anchor-2 (Wedderburn-RANK ratio) cannot be evaluated without first invoking Anchor-1 (faithful-image identification from S89 §W2-3).
   - (2) Non-fungible anchors: cannot swap order.
   - (3) Both remain accessible: neither S89 §W2-3 NPZ nor the Wedderburn-Artin theorem can be deprecated.
   - (4) Same algebra-axis cell: BOTH anchors live in Cell I × s=3 (algebra-INVARIANT spectrum-only functional × Mellin pole s=3); cross-corner co-primary structures are FORBIDDEN per S88 W-15 V.6 / B.14, and this structure is NOT cross-corner.

5. **Substrate-IS Level-1 single-τ-slice classification** per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (S88 W-2 W2-10 calibration corpus instance #1). χ'_weight = 3/6 is a Level 1 single-τ-slice substrate-IS observable: it is intrinsic to (A_K, H_K, D_K(τ_fold)) at the fixed τ_fold = 0.190 anchor. It does NOT involve moduli-space τ-deformation (Level 2). Future cross-pillar bridge entry for `S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT` should declare Level-1 single-τ-slice tag per `cross-pillar-bridge-anatomy.md` plan-freeze audit item 1 (5-anatomy elements + Level-1 declaration).

**S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT registry slot pre-registration**.

Per `cross-pillar-bridge-anatomy.md §"Forward template-adoption (5-anatomy + 3-level discipline)"` MANDATORY at K=3 + `joint-theorem-promotion.md §"Stage 2"` 4-stage pathway:

- **Slot identifier (next-free letter, S92 W1)**: `§VII.{next-free}.OP-PROJ` per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92, 2026-05-05). The χ'_weight observable is operator-projection (algebra-INVARIANT central-projection trace on A_K's source-side Wedderburn decomposition) — OP-PROJ suffix MANDATORY.
- **5-anatomy IS-not-IN elements**:
  - (1) Substrate-IS observable: the K-class-mass-fraction surviving χ' under the Kasparov-KK projection class on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`; Wedderburn-RANK source-side ratio 3/6.
  - (2) Laboratory-IN observable: the LRD α-anchor at M=10⁷ M_sun horizon-spanning projector evaluation (Pillar III↔IV bridge to laboratory cosmological-horizon observables; via CF-37 / T1.8 / T1.9 evaluation chain).
  - (3) Bridge map: HKR L→∞ image (matches §VII.AF.1.OP-PROJ W-5 baseline bridge map; Connes-Karoubi pairing on the substrate's intrinsic Hochschild cocycle space).
  - (4) Algebraic envelope: Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`; the HKR image binds the Wedderburn-RANK K-theoretic identity to the laboratory cosmological-horizon trace. Predicted convergence rate: L_max-INDEPENDENT at the K-theoretic invariant layer (3/6 is exact algebra-rank arithmetic, not L_max-dependent).
  - (5) Empirical anchor: χ'_weight = 0.500 at L_max=10 EXACT (Sage-rational; structurally identical at all L_max ≥ 0 by K-theoretic invariance).
- **3-level structural-confidence ladder**:
  - **Level 1 — Substrate-IS structural identity**: Wedderburn-Artin theorem on A_K + Kasparov-KK class preservation theorem → χ'_weight = rank(faithful image)/rank(A_K) = 3/6 = 0.500 EXACT (regulator-INVARIANT, L_max-INDEPENDENT). STATUS: STRUCTURAL THEOREM.
  - **Level 2 — Algebraic envelope**: L_max-INDEPENDENT by K-theoretic invariance; the 5-anatomy item (4) above. STATUS: STRUCTURAL PREDICTION (Level-2-binding).
  - **Level 3 — Empirical anchor at canonical L_max=10**: χ'_weight value 0.500 reproduces source-side K-class-rank-ratio at L_max=10 to bit-precision (no truncation effect). STATUS: EMPIRICAL CONFIRMATION ≤ Level-2 (trivially; both equal 0.500 EXACT).
- **Hybrid Independence Test K-counter advancement** per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`:
  - Distinct substrate-IS pillar: candidate is on the SAME Pillar III↔IV bridge as §VII.AF.1.OP-PROJ baseline (does NOT advance K-counter via axis (i)).
  - Distinct laboratory-IN pillar: SAME laboratory cosmological-horizon class (does NOT advance via axis (ii)).
  - Distinct bridge map class: SAME HKR L→∞ (does NOT advance via axis (iii)).
  - Independent algebraic envelope: the canonical-WEIGHT verdict's algebraic envelope (L_max-INDEPENDENT K-theoretic invariance) is structurally DISTINCT from §VII.AF.1.OP-PROJ's L^{-3} envelope at d=4 substrate-distance-1 (PASSes axis (iv)).
  - **Hybrid Independence Test result**: K-counter stays at K=1 (W-5 baseline only) since (iv) alone is insufficient — `(i ∨ ii ∨ iii) ∧ iv` requires structural diversity along ≥1 of pillar / lab / bridge AND independent algebraic envelope. The canonical-WEIGHT verdict shares all of pillar / lab / bridge with W-5 baseline. **The §VII slot would land as SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE per the Hybrid Independence Test companion-tagging clause** — registry-eligible but does NOT advance K toward K=3 MANDATORY.

**Stage-2 cross-axis independent-verify pre-registration**.

Per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` (S88 W-14 W4a-17 V.2 MANDATORY at K=1):

- **Axis-A reviewer (substrate-physics / NCG-axiomatic)**: SELECT ONE from {`connes-ncg-theorist`, `landau-superfluid-condensed-matter-theorist`, `gen-physicist`}. The Axis-A reviewer audits the Wedderburn-Artin canonical-weight derivation from the K-theoretic / spectral-triple-algebra side. Recommended: `connes-ncg-theorist` per NCG-axiomatic depth on Kasparov-KK projections + Wedderburn-Artin K-theory.
- **Axis-B reviewer (cosmological-bridge / cross-pillar)**: SELECT ONE from {`mack-cosmic-bridge`, `lizzi-spectral-functional-theorist`, `kitaev-quantum-chaos-theorist`}. The Axis-B reviewer audits the bridge-map class consistency + registry-landing structure. Recommended: `mack-cosmic-bridge` per §VII registry sole-writer authority on observational-anchor predictions per `feedback_mack-bridge-role.md`.
- **OAA exclusion**: HARD-exclude `volovik-superfluid-universe-theorist` (this Round 1 Axis-A author) AND `van-den-dungen-bridge-theorist` (this Round 1 Axis-B author + original CF-37 / T1.8 / T1.9 evaluator) per downstream-inheritance reach extension. Both volovik and vdd hold load-bearing structural arguments for / against the three readings; neither can serve as Stage-2 independent-verify reviewer.
- **JOINT clauses**: BOTH cross-reviewers must independently PASS the canonical-weight verdict on:
  - (a) Wedderburn-Artin canonical-weight derivation (Axis-A audits; Axis-B confirms substrate-physics structural correctness)
  - (b) Cell-I × s=3 corner classification (BOTH must PASS — JOINT clause)
  - (c) Hybrid Independence Test K-counter stay at K=1 with SHARED-ANCHOR-COMPANION tag (BOTH must PASS — JOINT clause)
  - (d) §VII slot OP-PROJ suffix + 5-anatomy + 3-level ladder + Level-1 single-τ-slice declaration (BOTH must PASS — JOINT clause)
- **Without prior workshop context**: Stage-2 reviewers receive ONLY the registered Stage-1 entry text + the source NPZ artifacts (s89_w2_a7_chi_prime_inheritance_morphism.npz, s90_w4_alpha_m_alt_corridor_d_compose_b.npz, s91_w3_alpha_m_aux4_corridor_c_compose_d.npz, s91_w3_alpha_m_full_cm1995_residue_d_compose_b.npz) + canonical_constants.py; they do NOT receive this workshop's R1/R2 transcripts.

**4-field CF spec for Stage-2 verify dispatch (S92 plan input)**.

```
CF-S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT-STAGE-1-CANDIDATE-REGISTRY-LANDING
  + STAGE-2-INDEPENDENT-VERIFY:

| Field   | Value                                                                |
|:--------|:---------------------------------------------------------------------|
| What    | (1) Land STAGE-1-CANDIDATE registry entry §VII.{next-free}.OP-PROJ   |
|         | at S92 W1 for the χ'_weight canonical Wedderburn-RANK 3/6 = 0.500    |
|         | reading per workshop S91 W-2 verdict (outcome (i) CANONICAL-WEIGHT;  |
|         | volovik V1-V5 + vdd Round 1 + Round 2 closure). Entry carries 5      |
|         | IS-not-IN anatomy elements + 3-level ladder + Level-1 single-τ-slice |
|         | + SOURCE-DOUBLE-CITE-CO-PRIMARY (V_input=S89 §W2-3 + C_output=       |
|         | Wedderburn-Artin K-theoretic canonical) + Hybrid Independence Test   |
|         | SHARED-ANCHOR-COMPANION tag. (2) Dispatch Stage-2 cross-axis         |
|         | independent-verify: Axis-A = connes-ncg-theorist; Axis-B = mack-     |
|         | cosmic-bridge; HARD-exclude volovik + vdd per downstream-inheritance |
|         | reach. JOINT clauses (a)+(b)+(c)+(d) PASS-AND'd across both axes.    |
| Inputs  | s89_w2_a7_chi_prime_inheritance_morphism.npz (audit_sha256           |
|         | 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843);   |
|         | s90_w4_alpha_m_alt_corridor_d_compose_b.npz                          |
|         | (CF-37 baseline; audit_sha256 10ee072fe2c193f3...);                  |
|         | s91_w3_alpha_m_aux4_corridor_c_compose_d.npz                         |
|         | (T1.8; audit_sha256 8ab158e9e45aab37...);                            |
|         | s91_w3_alpha_m_full_cm1995_residue_d_compose_b.npz                   |
|         | (T1.9; audit_sha256 752a8f2b862a9aa5...);                            |
|         | this workshop transcript (S91 W-2 verdict + Round 1 / Round 2);      |
|         | §VII.AF.1.OP-PROJ baseline registry line 14776 (W-5 calibration      |
|         | corpus instance #1); §VII.AU.OP-PROJ entry line 17784 (FWD-C1        |
|         | deferred-pending; cross-link only, no edit); canonical_constants.py  |
|         | (M_KK, M_Pl_reduced, R_universal_HP1_strict_F4, eps_H_HP1_norm,      |
|         | tau_fold).                                                           |
| Gate    | (1) Registry-landing PASS: §VII.{next-free}.OP-PROJ written with     |
|         | all 5 anatomy elements + 3 levels + Level-1 tag + SOURCE-DOUBLE-     |
|         | CITE-CO-PRIMARY + SHARED-ANCHOR-COMPANION tag declared. Mack-cosmic  |
|         | -bridge sole-writer signature per `feedback_mack-bridge-role.md`.    |
|         | (2) Stage-2 cross-axis verify PASS: BOTH Axis-A (connes) AND Axis-B  |
|         | (mack) independently PASS JOINT clauses (a)+(b)+(c)+(d); logical     |
|         | AND across the two verdicts. PASS advances entry from STAGE-1-       |
|         | CANDIDATE to STAGE-3-PERMANENT eligibility per `joint-theorem-       |
|         | promotion.md` 4-stage pathway. FAIL at either Axis blocks Stage-3    |
|         | promotion; entry stays at STAGE-1-CANDIDATE with FAIL-routing        |
|         | documented as forward remediation.                                   |
| Effort  | ~0.8 wave-equivalents total. Subtask split:                          |
|         | - Registry landing: ~0.3 we (mack sole writer; mechanical landing    |
|         |   modeled on §VII.AF.1.OP-PROJ template).                            |
|         | - Stage-2 Axis-A (connes-ncg-theorist) cross-review: ~0.3 we.        |
|         | - Stage-2 Axis-B (mack-cosmic-bridge) cross-review: ~0.2 we.         |
|         | Both Stage-2 reviewers dispatched IN PARALLEL (not sequentially)     |
|         | per joint-theorem-promotion.md Stage 2 Section 2 protocol.           |
| Depends | - Workshop S91 W-2 verdict closure (this document; produces Round 2  |
|   on    |   final verdict on outcome (i) vs (ii) vs (iii)).                    |
|         | - S89 §W2-3 derived theorem NPZ (already landed; audit_sha256        |
|         |   90bba262af80a04c...).                                              |
|         | - CF-37, T1.8, T1.9 NPZ artifacts (already landed at S90 W4 + S91    |
|         |   W3 respectively).                                                  |
|         | - §VII.AF.1.OP-PROJ baseline registry entry (already landed S87      |
|         |   W5-1; no edit required, cross-link only).                          |
|         | - canonical_constants.py existing pins (M_KK, M_Pl_reduced,          |
|         |   R_universal, eps_H_HP1_norm, tau_fold).                            |
```

**§VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ deltas under Reading 1 canonical**.

- **§VII.AF.1.OP-PROJ (registry line 14776; LANDED S87 W5-1)**: **NO DELTA**. The W-5 baseline `R_universal_HP1_strict_F4 = 1.030902` is the unrestricted (χ'_weight=1) baseline. Reading 1's canonical-weight verdict applies to inheritance-RESTRICTED observables (CF-37 / T1.8 / T1.9 evaluations using χ'); the unrestricted baseline is upstream of the χ'-restriction and is unaffected by the canonical-weight choice. No corrigendum required.
- **§VII.AU.OP-PROJ (registry line 17784; LANDED S89 W7c, S90 W1-15 deferred-pending re-tag)**: **NO DELTA**. The FWD-C1 Pillar I↔II bridge candidate at substrate-distance-1 pole s=3 evaluates `n_s_FW² − 1 ≡ α_s_canonical` (Pillar I substrate-IS observable; CMB n_s laboratory-IN observable). This is a SEPARATE substrate-IS observable from the LRD α-anchor (Pillar III↔IV). The χ'_weight canonical-weight verdict does NOT modify the n_s_FW or α_s_canonical predictions. §VII.AU.OP-PROJ retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class status per S90 W1-15 re-tag; the pending first-extraction (CF-65 / W-6 CF-3) is structurally orthogonal to Reading 1's canonical-weight verdict.

**What is NOT in the registry-landing scope at S92**:
- **No retroactive edit to CF-37's verdict line** at `computations/session-90/s90_gate_verdicts.txt` audit_sha256 `10ee072fe2c193f3...`. Under `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`, CF-37 retains its FAIL verdict at the empirical 1/458 anchor (rel_dev 0.78) — the canonical-weight verdict resolves what the χ'_weight IS, not what α'(M_LRD) IS. CF-37's structural-ansatz layer IS canonical at the K-theoretic inheritance-morphism layer (per V1-V4); the empirical FAIL remains a FAIL because the empirical bottleneck IS the dimensional bridge factor (M_KK/M_Pl_reduced)² (per van-den-dungen's T1.8 Axis-B item 5 line 713: "NO Wedderburn-rank-admissible substrate-derivation of γ_weight_aux can reach the 1/458 anchor under (c)∘(d) at substrate-distance-1 — this is a STRUCTURAL closure"). The substrate-distance-1 corridor at the LRD α-anchor IS structurally closed under Reading 1 canonical; T1.8 + T1.9 closures reinforce this by showing alternative substrate-derivations (digamma-modulated, FULL CM-1995) ALSO fail.
- **No retroactive edit to T1.8 or T1.9 verdict lines** at `computations/session-91/s91_gate_verdicts.txt` (audit_sha256 `8ab158e9...` and `752a8f2b...`). Both retain FAIL verdicts at empirical 1/458; Reading 1's canonical reframes them as STRUCTURALLY DISTINCT AUXILIARY canonicals (Reading 3 on the (c)-corridor; Reading 2 as the CM-1995 §III.4 trace image of Reading 1 on the (b)-corridor) rather than as competing primary canonicals. No verdict re-emission needed.

**Forward path beyond the canonical-weight verdict**.

Per W3 WP §W3-4 Solution-space implications + §"Carry-forward computations" lines 805-808: with the substrate-distance-1 corridor structurally closed at the LRD α-anchor under all three readings (and the canonical-weight Reading 1 is the substrate's intrinsic answer to "what is χ'_weight?"), the LRD α-anchor pursuit moves to substrate-distance-2 §VII.AX forward gates pre-registered at S91 W0 R5. This is INDEPENDENT of the S92 canonical-weight registry landing — both can proceed in parallel.

**Structural-output mapping**. V5 (cross-cutting + registry consequences) confirms **CANONICAL-WEIGHT verdict (outcome (i))** with Reading 1 as canonical AT THE PRIMARY (b)-corridor / K-theoretic inheritance-morphism layer. The S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT registry slot is pre-registered with all 5 IS-not-IN anatomy elements + 3-level ladder + Level-1 single-τ-slice + SOURCE-DOUBLE-CITE-CO-PRIMARY + SHARED-ANCHOR-COMPANION + STAGE-1-CANDIDATE tag. Stage-2 cross-axis verify dispatch (connes + mack; HARD-exclude volovik + vdd) is pre-registered at ~0.8 we total. §VII.AF.1.OP-PROJ and §VII.AU.OP-PROJ retain no deltas under Reading 1 canonical.

**Questions for van-den-dungen**:
- (V5-Q-VDD-1) Do you concur that the S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT registry slot should land as STAGE-1-CANDIDATE with Reading 1 canonical (Wedderburn-RANK 3/6) AND with explicit SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tagging (Hybrid Independence Test stays at K=1; no K-counter advancement), and that Stage-2 cross-axis verify follows with connes + mack (volovik + vdd HARD-excluded)? If you propose outcome (ii) SIMULTANEOUS-VALIDITY or (iii) OPEN-REGISTRY-SLOT instead, what registry structure do you propose and how does it integrate with the §VII.AF.1.OP-PROJ baseline + §VII.AU.OP-PROJ FWD-C1 cross-pillar bridge structure?
- (V5-Q-VDD-2) The CF-37 PROXY-REFINEMENT-PENDING tag's pre-registered hypothesis (S90 W4 Closing Notes #2: "if FULL CM-1995 produces χ'_weight ~4.5× larger than 0.5, the (d)∘(b) corridor could revisit") was empirically refuted by your T1.9 derivation (factor 5/7 = 0.714× UNDER-shoot, not 4.5× over-shoot). Under Reading 1 canonical, the PROXY-REFINEMENT-PENDING tag is structurally RESOLVED in the FAIL direction. Does your T1.9 derivation establish a STRONGER claim than this (e.g., the FULL CM-1995 5/14 weight is itself the canonical, and Reading 1's 3/6 is the structural-ansatz under-approximation)? If so, what argument resolves the V1/V3 K-theoretic / source-side / primary-corridor priority axes in favor of Reading 2?
- (V5-Q-VDD-3) The §VII.AU.OP-PROJ FWD-C1 deferred-pending entry (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class per S90 W1-15) shares the substrate-distance-1 pole s=3 with this workshop's canonical-weight slot. Both inhabit Cell I × s=3 by parse-tree decision procedure. Is there a structural relationship between FWD-C1's parameterized slope_A canonical first-extraction (CF-65) and the canonical χ'_weight verdict that would suggest joint Stage-2 dispatch or shared cross-axis reviewer pool? Or are they fully orthogonal (Pillar I↔II vs Pillar III↔IV; n_s_FW vs LRD α-anchor)?

---

## Round 1 — Van-den-Dungen: Response & Cross-Synthesis (NCG-Axiomatic CM-1995 §III.4 Reading)

### Part 1: Response to Volovik's Sections

#### Re: V1 — Canonical χ'_weight identity

**AGREE (partial — what holds at the K-theoretic class layer)**.

I concur with your V1 §"Wedderburn-Artin substitution chain" Step 1–4 *as a statement about the K-theory of A_K under K_0*: the Wedderburn-Artin decomposition A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) is the substrate's intrinsic *-algebra structure, the primitive-idempotent counts (1, 2, 3) are invariants of the algebra, and K_0(A_K) ≅ ℤ ⊕ ℤ ⊕ ℤ with generators at K-class-rank weights (1, 2, 3). I also concur that χ'_*: K_0(A_K) → K_0(M_2(ℂ) ⊗ Cl(1)) kills the M_3(ℂ) generator and faithfully embeds the ℂ and ℍ generators (by S89 §W2-3 Step 7; Wedderburn 9 > 8 + Schur orthogonality; NPZ audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`). At the K-class-rank-mass-fraction layer your computation (rank 1 + rank 2)/(rank 1 + rank 2 + rank 3) = 3/6 is *arithmetically correct* — the K-class-rank-mass-fraction of A_K surviving χ' is 1/2.

**DISAGREE (where the canonical χ'_weight on A_K lives)**.

I dispute the *identification* "K-class-rank-mass-fraction = canonical χ'_weight at the inheritance-morphism layer". The χ'_weight that enters α'(M_LRD) in CF-37, T1.8, and T1.9 is the **multiplicative algebra-trace weight at the Connes-Karoubi pairing**, NOT the K_0-rank-mass-fraction. Concretely: in the multiplicative decomposition

```
α'(M_LRD)  =  R_universal_HP1_strict_F4  ·  χ'_weight  ·  (M_KK / M_Pl_reduced)²  ·  g(M_LRD, L=10)
```

R_universal_HP1_strict_F4 = 1.030902 IS the *un-restricted* Connes-Karoubi pairing `⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` on the substrate's intrinsic Hochschild cocycle space, evaluated at the substrate-distance-1 pole s=3 via the **CM-1995 §III.4 residue formula `a_4^ζ` residue at s=0**. This is verbatim from the §VII.AF.1.OP-PROJ W-5 baseline registry text (`permanent-results-registry.md` line 14815: "the substrate-IS Hochschild pairing is evaluated under zeta-function regularization of the Seeley-DeWitt coefficients; `a_4^ζ` is the relevant residue at s=0 for the `R_universal` formula"). The χ'_weight factor's role in α'(M_LRD) is to scale R_universal by the *algebra-trace-mass-fraction* of A_K that survives χ' inside the same residue evaluation. The CM-1995 §III.4 residue formula's algebra-trace is `Tr` on the *regular representation* of A_K on H_K (where dim_HS counts the trace's basis dimension); it is NOT a K_0-rank-mass-fraction. The canonical χ'_weight at this layer is therefore

```
χ'_weight_canonical  =  (dim_HS(ℂ) + dim_HS(ℍ))  /  dim_HS(A_K)
                     =  (1 + 4)  /  (1 + 4 + 9)
                     =  5/14  ≈  0.357143
```

per T1.9 audit_sha256 `752a8f2b862a9aa5...`. The 5/14 value IS the substrate's intrinsic *Hilbert-trace-mass-fraction* surviving χ'; it is substrate-IS at the regular-representation evaluation layer that the CM-1995 §III.4 residue formula prescribes, NOT a representation-dependent artifact.

**MISSED (what V1 does not surface)**.

The §VII.AF.1.OP-PROJ baseline's theorem text and IS-not-IN anatomy (registry lines 14817-14836) pin Element 3 of the bridge map as **HKR `L_max → ∞` ∘ Connes-Karoubi pairing**. The Connes-Karoubi pairing at this bridge layer IS defined by the CM-1995 §III.4 finite-spectral-triple residue formula `Tr(γ · cocycle · [F, cocycle]² · |D|^{-2s})` with regulator `|D|^{-2s}` — this is the regular-representation trace on H_K. When χ' is applied to *restrict* this trace to the faithful (ℂ ⊕ ℍ) sub-algebra image, the mass-fraction of the trace that survives is the dim_HS-fraction by construction — not the K_0-rank-fraction, because the trace measures **operator-algebra mass on H_K**, not K-theoretic class-mass on K_0(A_K). V1 conflates two structurally distinct invariants of χ': its K_0-functoriality (preserves K-class-rank) and its trace-mass-pullback (preserves Hilbert-trace-dim-mass). Both are substrate-IS — but they live on different categorical layers and they give different numerical answers for "what fraction of A_K does χ' carry into α'(M_LRD)?".

The S86 W-5 calibration corpus instance #1 (LANDED S87 W5-1) is the canonical witness for this: R_universal = `⟨[φ_g^{sym}], [Ch(P_0)]⟩` IS the *regular-representation Hilbert-trace pairing* on the substrate's algebra — Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula, with `a_4^ζ` residue at s=0. The χ'-restricted observable α'(M_LRD) inherits this exact trace structure under the inheritance restriction χ'. The dim_HS-fraction 5/14 is the trace-pullback's mass-fraction by direct algebraic substitution into the CM-1995 §III.4 evaluator (T1.9 Step 5 in `session-91-w3-workingpaper.md` lines 981-984); the K_0-rank-fraction 3/6 is the K-class-rank-pullback's mass-fraction. Both are intrinsic to χ'; only one is intrinsic to the **residue formula α'(M_LRD) actually evaluates**.

**EMERGES**.

Reading V1's K-theoretic argument and the CM-1995 §III.4 dim-spec argument together: there is a structural **two-layer identification** for χ' on A_K:

| Layer | Invariant | Value | Source |
|:------|:----------|:------|:-------|
| K_0(A_K) → K_0(target) K-class-rank-mass-fraction | rank(image)/rank(A_K) = 3/6 | 0.500 | Wedderburn-Artin + Kasparov KK |
| Hilbert-trace-mass-fraction on the CM-1995 §III.4 regular-representation evaluator | dim_HS(image)/dim_HS(A_K) = 5/14 | 0.357 | Connes-Moscovici 1995 §III.4 + W-5 baseline pairing |

These are **non-fungible** χ'-invariants on a single Kasparov KK projection. Volovik's argument is correct that the *K-class index* is 3/6. My argument is that the χ'_weight factor *that enters the multiplicative decomposition of α'(M_LRD)* is the **trace-mass-fraction 5/14**, because the residue evaluator IS the regular-representation trace. The two readings are not in numerical contradiction; they disagree about *which invariant is the χ'_weight in α'(M_LRD)*.

This emergent observation suggests outcome (ii) **SIMULTANEOUS-VALIDITY** at the *invariant-class* level may be more defensible than outcome (i) canonical-winner: Reading 1's 3/6 IS the K-class-rank invariant under the Kasparov KK projection class; Reading 2's 5/14 IS the trace-mass invariant under the CM-1995 §III.4 residue formula evaluation. They are simultaneously substrate-IS, simultaneously canonical on their respective invariant axes, but they answer different structural questions about χ'.

**Answers to Volovik's Q-VDD questions on V1**.

**(V1-Q-VDD-1)** — "Is the dim_HS 5/14 weight the substrate's intrinsic K-theoretic invariant, or the Hochschild cocycle pairing value on the regular representation?" My answer: it is the **Hochschild cocycle pairing value on the regular representation**, which is precisely the substrate-IS canonical evaluation of the CM-1995 §III.4 residue formula at the substrate-distance-1 pole s=3. It is NOT the K-theoretic K_0-rank-mass-fraction — and I do not claim it is. My claim is that the χ'_weight factor IN α'(M_LRD) IS the Hochschild cocycle pairing's trace-mass-fraction (because α'(M_LRD) IS evaluated through that residue formula at that pole), and therefore Reading 2's 5/14 IS the substrate-IS canonical for *the χ'_weight that enters α'(M_LRD)*. Your K-class index 3/6 is a different (also substrate-IS) invariant of χ'; we do not disagree on its existence or value, only on whether it IS the χ'_weight factor in α'(M_LRD).

**(V1-Q-VDD-2)** — "Under Connes' bivariant KK-theoretic formalism, the χ' inheritance morphism's *index/multiplicity* should be Wedderburn-RANK based. Do you contest that the K-theoretic class index is the structurally canonical reading?"

I do not contest that the K-theoretic class index of χ' is Wedderburn-RANK based (3/6). What I contest is the unstated bridging premise that "the K-theoretic class index of χ' IS the χ'_weight factor in α'(M_LRD)". The Kasparov KK-bridge framework (van-den-dungen Paper 01 / 1811.07824, "The Kasparov Product on Submersions of Open Manifolds") factorizes the *fundamental class* of a submersion as a Kasparov product of shriek map and base fundamental class — and that factorization is at the level of **KK-theoretic classes**, NOT at the level of *individual trace-pairings*. In the M⁴ × SU(3) submersion the Kasparov factorization gives the **topological** Dirac-class decomposition (K-homology layer of my MEMORY.md four-layer hierarchy: w_0, w_a, c_s², mass ordering — scheme-independent, zero-parameter). The χ'_weight factor in α'(M_LRD) lives at a DIFFERENT layer in the four-layer hierarchy — it is a **metric-layer** observable (sin²θ_W |_{M_KK}, a_k at specific τ, regulator-dependent) because the CM-1995 §III.4 residue formula uses |D|^{-2s} regulator and outputs Seeley-DeWitt-like trace coefficients that are *not* scheme-independent topological invariants. At the metric layer, the trace-mass-fraction 5/14 is the substrate-IS canonical; at the K-homology / index layer, your 3/6 is canonical. Both are valid; they live at different layers.

This is *not* an evasion — it is the four-layer hierarchy of my permanent agent memory applied honestly: Kasparov KK gives TOPOLOGY (not analysis); CM-1995 §III.4 residue gives ANALYSIS (the metric-layer trace expansion). α'(M_LRD) is a metric-layer observable (regulator-dependent multiplicative decomposition); its canonical χ'_weight is the trace-mass-fraction 5/14.

#### Re: V2 — Modified-universal-kernel γ(s) shift

**AGREE (corridor-orthogonality, factorization-layer separation)**.

I concur with the V2 §"Why γ(s) ≠ Γ(s) is a structural cohomology-class shift, not an asymptotic correction" argument. Specifically: (i) γ(s) = Γ(s)·(1 + c_aux·(s − s_*)^{-1}) carries a new simple pole at s = s_* = 1 that Γ(s) does not, and the Laurent expansion analysis at workshop document line 180-184 is correct; (ii) c_aux = 1/3 IS substrate-Wedderburn-derived from the sign-alternating rank sum (1 − 2 + 3)/6, not a free parameter — my own T1.8 Axis-B cross-review at `session-91-w3-workingpaper.md` line 707 confirmed this verbatim ("the c_aux value is FIXED by substrate algebra rank arithmetic and cannot be freely re-chosen without abandoning the (c) deformation class"); (iii) (b) χ'-pullback and (c) γ(s) ≠ Γ(s) modified-universal-kernel are **orthogonal element-1 deformation axes** — vertical (substrate-algebra) vs horizontal (regulator-kernel) deformations factor through the bridge map at distinct layers. This is **exactly the Kasparov-product factorization principle** I confirmed at T1.8 Axis-B item 5 (W3 WP line 712); it is the unbounded-KK-theory factorization theorem from my Paper 01 (van-den-Dungen 1811.07824, "The Kasparov Product on Submersions of Open Manifolds") applied at the deformation-axis layer. The (c) and (b) corridors cannot reduce to each other; they are independent deformation columns.

I also concur that Reading 3's `(1 − γ_Euler/3) ≈ 0.808` digamma factor is **NOT** an L_max → ∞ asymptotic correction to Reading 1 — both Readings 1 and 2 are L_max-INDEPENDENT at their canonical evaluations (T1.9 envelope_n ≈ −1.22e-20 ≈ 0; CF-37 structural-ansatz is closed-form algebra arithmetic). The digamma factor is an **algebra-side (c)-shift on the universal kernel** that lives at the kernel-choice layer, NOT the L_max-truncation layer. Your V2 §"Why γ(s) ≠ Γ(s) is NOT an L_max → ∞ asymptotic correction" diagnosis at workshop document lines 198-202 is correct.

**DISAGREE (which weight Reading 3 INHERITS as its multiplicative pre-factor)**.

V2 implies Reading 3 inherits Reading 1's Wedderburn-RANK 3/6 = 0.5 as the **canonical** pre-factor before digamma modulation (your V2 line 195: `γ_weight_aux^(3) = χ'_weight · (1 + c_aux · ψ(s_*=1)) = 0.5 · (1 + (1/3) · (−γ_Euler)) = 0.5 · 0.80759 ≈ 0.40380`, with 0.5 reading as the Wedderburn-RANK ratio). This pre-factor identification implicitly assumes Reading 1 IS the canonical χ'_weight on the (b)-corridor — which is precisely the issue under adjudication.

The (c)∘(d) corridor's residue evaluation under γ(s) substituted into the CM-1995 §III.4 residue formula is, per T1.8 Axis-B item 4 (`session-91-w3-workingpaper.md` line 711), the FULL residue evaluation `Res_{s=s_*}[γ(s) · pairing(s)]` whose multiplicative pre-factor IS the **regular-representation Hilbert-trace-mass-fraction surviving χ'** — i.e., 5/14, not 3/6. The (c) shift modifies the universal kernel BEFORE the HKR `L → ∞` image; the χ'-restricted trace mass is still the CM-1995 §III.4 trace mass, which is dim_HS-weighted by the residue formula's regular-representation construction. Substituting the dim_HS-based pre-factor 5/14 into the digamma-modulation formula:

```
γ_weight_aux^(3, alt-pre-factor)(s_*=1)  =  (5/14) · (1 − γ_Euler/3)
                                          =  0.357143 · 0.807593
                                          =  0.288426
```

α''(M_LRD; alt pre-factor) = 1.030902 · 0.288426 · 9.307286e-04 = 2.768e-4 (rel_dev = 0.873 vs 1/458 = 2.183e-3; FAIL — worse than your 0.823). The empirical FAIL direction does NOT discriminate between the 3/6 and 5/14 pre-factors at the (c)∘(d) corridor; both produce α''(M_LRD) substantially below the 1/458 anchor; the substrate-distance-1 corridor is structurally closed under both pre-factor choices. But the **canonical-weight verdict** at the (c)∘(d) corridor does depend on which pre-factor is canonical — and per the V1/Re:V1 argument, that pre-factor is the trace-mass-fraction 5/14 by the same CM-1995 §III.4 residue formula structure.

I therefore propose: Reading 3's correct canonical form is `γ_weight_aux^(3) = (5/14) · (1 − γ_Euler/3) ≈ 0.2884`, NOT `0.5 · (1 − γ_Euler/3) ≈ 0.4038`. The 0.4038 value Volovik reports in V2 (and that T1.8 computes) IS the value obtained when one PRE-COMMITS to Reading 1's K-class-rank-mass-fraction as the pre-factor. If we instead pre-commit to Reading 2's trace-mass-fraction (which is what the CM-1995 §III.4 residue formula's regular-representation trace prescribes), the digamma-modulated value is 0.2884. The two values 0.4038 and 0.2884 are NOT both "Reading 3" — they are *Reading 3a (3/6 pre-factor)* and *Reading 3b (5/14 pre-factor)*; only one is canonical at the (c)∘(d) corridor, and which one depends on the V1 adjudication.

**MISSED (the (c)-shift's irrationality reinforces SIMULTANEOUS-VALIDITY at the corridor level)**.

V2 §"Compositional corridor independence" identifies (b)-corridor and (c)-corridor as orthogonal deformation columns, with Reading 1 = (b)-corridor canonical and Reading 3 = (c)-corridor canonical. This is consistent with my Re:V1 emergent observation that the K-class-rank invariant and the trace-mass invariant are non-fungible χ'-invariants. The full picture surfacing now: there are **four** structurally distinct substrate-IS observables on A_K at the inheritance-morphism layer for the LRD α-anchor:

| Corridor | Pre-factor | Modulation | Value | Substrate identity |
|:---------|:-----------|:-----------|:------|:-------------------|
| (b)∘(d) Wedderburn pre-factor | 3/6 (K-class-rank) | none | 0.500 | CF-37 structural-ansatz |
| (b)∘(d) dim-spec pre-factor | 5/14 (Hilbert-trace) | none | 0.357 | T1.9 FULL CM-1995 |
| (c)∘(d) Wedderburn pre-factor | 3/6 | (1 − γ_Euler/3) | 0.404 | T1.8 |
| (c)∘(d) dim-spec pre-factor | 5/14 | (1 − γ_Euler/3) | 0.288 | (T1.8 with FULL pre-factor) |

The (c)∘(d) digamma-modulation is a structural identity at the (c)-corridor INDEPENDENT of which pre-factor is canonical at the (b)-corridor. **Whichever Reading is canonical at the (b)-corridor must also be canonical at the (c)-corridor under digamma modulation by the same residue-evaluation structure.** This is the unbounded-KK factorization theorem at work: the substrate-algebra deformation (χ' pullback) factors INDEPENDENTLY of the regulator-kernel deformation (γ(s) substitution), so the χ'_weight factor in Reading 3 IS the same χ'_weight factor in Reading 1 + 2, modulated by the (c) digamma factor.

**EMERGES**.

Reading V1+V2 together with Re:V1, the canonical-weight adjudication question collapses to **one** structural question: at the CM-1995 §III.4 residue formula evaluation underlying the W-5 baseline R_universal, does the χ'-restricted trace mass-fraction equal the K_0(A_K) rank-class-mass-fraction (3/6) or the regular-representation trace-mass-fraction (5/14)? The answer is determined by the residue formula's construction — `Tr` on the algebra's regular representation on H_K, NOT `K_0`-rank trace — and the answer is 5/14. Once 5/14 is canonical at the (b)-corridor, it propagates to the (c)-corridor by the Kasparov-product factorization principle: γ_weight_aux^(3, canonical) = 5/14 · (1 − γ_Euler/3) ≈ 0.288, not 0.404.

I do NOT mean to be obtuse here — your T1.8 derivation arithmetically computes 0.5 · 0.808 = 0.404 and that arithmetic is correct given the *choice* to pre-commit to 0.5 as the pre-factor. My disagreement is at that choice, not the arithmetic. **The (c)-corridor canonical inherits whatever the (b)-corridor canonical is — and the (b)-corridor canonical is 5/14 by the CM-1995 §III.4 residue formula structure.**

**Answers to Volovik's Q-VDD questions on V2**.

**(V2-Q-VDD-1)** — "Do you concur that Reading 3 INHERITS Wedderburn-RANK 3/6 as its pre-factor and modulates by the digamma factor, rather than being an independent χ'_weight in its own right?"

I concur with the **structural form** of your statement: Reading 3 inherits *the* canonical χ'_weight as its pre-factor, multiplied by the (c) digamma modulation `(1 + c_aux · ψ(s_*))`. I dispute the **numerical content**: the inherited pre-factor IS NOT necessarily 3/6 — it depends on the V1 adjudication. If Reading 1 (K-class-rank 3/6) is canonical, then yes, Reading 3 = 3/6 · 0.808 = 0.404 (as in T1.8). If Reading 2 (dim-spec 5/14) is canonical, then Reading 3 = 5/14 · 0.808 = 0.288. The (c)-corridor's structural distinctness from (b) is preserved either way — your V2 corridor-orthogonality argument is independent of the pre-factor adjudication.

**(V2-Q-VDD-2)** — "The factor (1 − γ_Euler/3) ≈ 0.808 is an irrational substrate-IS structural constant... Does this irrationality reinforce or contest my reading that γ(s) modulation is a structurally distinct AUXILIARY canonical?"

**Reinforce, strongly.** The Euler-Mascheroni constant γ_Euler = 0.577216... is irrational (proof is open but the substrate-IS value is fixed); the multiplicative factor (1 − γ_Euler/3) is therefore irrational AND substrate-derived. Per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (registry MANDATORY at K=3 cohomology-class-distinct + K=2 pole-distinct), irrational substrate-IS values are classified as `structurally-IRRATIONAL-per-CC2-analog`. The (c)-corridor's irrational digamma factor IS a structurally distinct observable from the (b)-corridor's rational pre-factor (whether 3/6 or 5/14). It cannot be a refinement of either rational pre-factor because rational numbers and `ℚ ⊕ ℚ·γ_Euler` are algebraically independent over ℚ. The (b)-corridor and (c)-corridor canonicals are therefore structurally distinct functionals on A_K at the *algebraic-number-class* layer in addition to the *deformation-column* layer — they cannot collapse into a single canonical even at L_max → ∞.

So I support **SIMULTANEOUS-VALIDITY at the (b)/(c) corridor-decomposition level** as a defensible structural reading of the workshop's substrate-physics content. The competing canonical choice is INTRA-(b)-corridor between Reading 1 and Reading 2.

#### Re: V3 — Inheritance morphism faithfulness

**AGREE (S89 §W2-3 derived theorem; faithful image identification)**.

I concur entirely with V3 §"S89 §W2-3 derived theorem: χ'|_{M_3(ℂ)} = 0 (8-step proof)". Specifically:

- The 8-step Wedderburn 9 > 8 + Schur orthogonality argument (workshop document lines 236-280) is structurally correct. dim_HS(M_3(ℂ)) = 9 strictly exceeds dim_C(target) = 8 = dim_HS(M_2(ℂ) ⊕ M_2(ℂ)); M_3(ℂ) is simple over ℂ with unique 3-dim defining irrep; 8 = 3k + r admits no representational-theoretic decomposition supporting non-zero embedding; the only morphism is zero.
- The machine-epsilon witness from W3 WP §W3-4 lines 1062-1068 — χ' image norm on M_3(ℂ) is 0.0 EXACTLY, P_ker Frobenius norm √9 = 3 EXACTLY, dχ'^*φ_g^{sym}|_{M_3(ℂ)} = 0 by structural inheritance (`chi_prime_pullback_machine_eps_PASS = True`) — confirms the zero-map is STRUCTURAL not numerical.
- The faithful image of χ' is therefore ℂ ⊕ ℍ; the M_3(ℂ) summand is killed entire (kernel rank = 9).
- V3 line 311 verbatim arithmetic — `χ'_weight = (rank 1 + rank 2)/(rank 1 + rank 2 + rank 3) = 3/6 = 0.500` — IS the source-side K_0(A_K) K-class-rank-mass-fraction surviving χ'_*. Arithmetic correct; CF-37 origin derivation (`session-90-w4-workingpaper.md` §W4-1 line 75) is reproduced bit-for-bit.

So we agree on the **substrate's structural fact**: χ' kills M_3(ℂ); ker rank = 9; faithful image is ℂ ⊕ ℍ; K-class-rank-mass-fraction of the faithful image inside K_0(A_K) is 3/6. This is the substrate-IS K-theoretic invariant of χ' at the K_0-rank layer.

**DISAGREE (V3 §"Why faithful-image Wedderburn-RANK ratio 3/6 IS the K-theoretic inheritance-restriction weight")**.

V3 line 285-310 argues that the K-class-rank-mass-fraction 3/6 IS the inheritance-restriction weight because χ' is a Kasparov KK projection and Kasparov KK projections preserve K-class-rank. This is sound at the K_0 layer. But the statement V3 implicitly asserts — "*therefore* the χ'_weight factor that multiplies R_universal in α'(M_LRD) is 3/6" — does not follow from K_0-functoriality alone. Concretely:

The W-5 baseline R_universal_HP1_strict_F4 = 1.030902 (canonical_constants.py:250) is defined at the **Connes-Karoubi pairing on the Hochschild cocycle space**, via the CM-1995 §III.4 finite-spectral-triple residue formula with a_4^ζ residue at s=0 (`permanent-results-registry.md` §VII.AF.1.OP-PROJ entry line 14815: "the substrate-IS Hochschild pairing is evaluated under zeta-function regularization of the Seeley-DeWitt coefficients; `a_4^ζ` is the relevant residue at s=0 for the `R_universal` formula"). The trace in this residue formula is `Tr` on the regular representation of A_K on H_K, where dim_HS{ℂ, ℍ, M_3(ℂ)} = {1, 4, 9} are the Hilbert-trace basis dimensions of each summand acting on itself.

When χ' restricts this pairing to the faithful (ℂ ⊕ ℍ) sub-algebra image, the trace-mass that survives the χ'-restriction is **the proportion of basis dimensions on H_K that χ' preserves**, NOT the proportion of K_0 rank-classes that χ' preserves. The surviving basis-dim is 1 + 4 = 5; the total basis-dim is 14; the trace-mass-fraction is **5/14, not 3/6**. T1.9 Step 5 line 983 verifies this by direct algebraic substitution into the FULL CM-1995 §III.4 residue formula:

```
α'_FULL(M_LRD)  =  R_universal · χ'_weight_FULL · (M_KK/M_Pl)² · g(M, L=10)
                =  1.030902 · (5/14) · 9.307286e-04 · 1.000
                =  3.426750e-04        [T1.9 audit_sha256 752a8f2b862a9aa5...]
```

The χ'_weight_FULL factor 5/14 comes from the trace-mass-pullback, which IS the substrate-IS dimension-spectrum residue trace operation prescribed by Connes-Moscovici 1995 §III.4. It is not a representation-theoretic choice — the CM-1995 §III.4 residue formula's regular-representation trace is canonical at this bridge map layer (verbatim from the §VII.AF.1.OP-PROJ baseline's bridge map citation: "HKR `L_max → ∞` ∘ Connes-Karoubi pairing").

V3 lines 313-325 dismisses 5/14 as "a representation-theoretic image of Reading 1 at the regular-representation evaluation of the CM-1995 §III.4 residue trace — useful for the CM-1995 residue formula's Hilbert-space trace, but downstream of the K-theoretic Wedderburn-RANK invariant". This framing concedes the structural point I am making: the CM-1995 §III.4 residue trace IS the canonical evaluator at the bridge map layer; 5/14 IS the canonical weight at THAT evaluation. The phrase "downstream of the K-theoretic Wedderburn-RANK invariant" is unproblematic if it means "K-theoretic invariants logically precede trace-pairings in the categorical hierarchy". But "downstream" should not be read as "non-canonical" — `Tr` is a substrate-IS canonical functional on the regular representation, and the residue-trace-mass-fraction 5/14 IS its substrate-IS canonical value.

The 3He-B inheritance morphism iota that V3 line 317 invokes as parallel (`rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2`, Hodgkin theorem) IS a K-theoretic invariant — but it is the invariant of the **iota itself**, NOT of any specific spectral functional iota appears in. The χ'_weight in α'(M_LRD) is the analogous invariant of the **χ'-restricted Connes-Karoubi pairing through CM-1995 §III.4 residue**, NOT of the bare χ' morphism. These are different layers; V3 conflates them.

**MISSED (V3 §"Why faithfulness does NOT pin canonical to a fourth K-theoretic dim ratio")**.

V3 lines 327-345 preemptively rejects a "fourth K-theoretic dim ratio candidate" constructed as **target-side K-class-rank ratio** = (1 + 2) / (2 + 2) = 3/4 = 0.75 — arguing this counts target REPRESENTATIONAL ROOM USED, not source K-class-mass surviving, and therefore has no substrate-IS interpretation as inheritance-restriction weight.

V3's rejection is correct on its own terms: target-side **rank** ratio is the wrong invariant. But it misses the actual fourth candidate I will propose in D2: the **K-theoretic Hilbert-space-dim ratio** = (rank-class generator dim used in target) / (total target dim used by χ'-image) computed on **complex Hilbert-space target dim**, not K-class-rank. Specifically:

- The image of χ' inside the target M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ) carries Hilbert-space-image-dim = 1 + 4 = 5 (rank-1 projector in one M_2(ℂ) summand uses dim 1; full identity-of-ℍ in the other M_2(ℂ) summand uses dim 4 — note ℍ ⊗_ℝ ℂ ≅ M_2(ℂ) consumes the full 4-dim representation).
- The full target Hilbert-space-dim is 4 + 4 = 8.
- The target-side Hilbert-space-image-dim ratio is **5/8 = 0.625**.

This is a substrate-IS Kasparov KK-bridge invariant of χ' DIFFERENT from V3's rejected 3/4. It counts the Hilbert-space-image-dim used in the target — which IS substrate-IS because both numerator (image-dim under canonical χ' "M3C_to_zero_C_and_H_to_canonical_M2C") and denominator (target Hilbert-space-dim from `chi_prime_target_dim` NPZ field, `session-91-w3-workingpaper.md` line 956) are pinned by S89 §W2-3 NPZ structure (audit_sha256 90bba262...). I develop this candidate explicitly in D2 below.

**EMERGES**.

Reading V3 + Re:V3, we have **four** distinct substrate-IS K-theoretic / trace invariants of the **single** Kasparov KK projection χ' : A_K → M_2(ℂ) ⊗ Cl(1):

| # | Invariant | Numerator | Denominator | Value | Substrate identity |
|:-:|:----------|:----------|:------------|:------|:-------------------|
| 1 | Source-side K-class-rank-mass-fraction | rank(ℂ) + rank(ℍ) = 3 | rank(A_K) = 6 | **3/6 = 0.500** | Volovik Reading 1 (CF-37) |
| 2 | Source-side regular-representation Hilbert-trace-mass-fraction | dim_HS(ℂ) + dim_HS(ℍ) = 5 | dim_HS(A_K) = 14 | **5/14 ≈ 0.357** | vdd Reading 2 (T1.9 FULL CM-1995) |
| 3a | Target-side K-class-rank ratio | rank-image = 3 | rank-target = 4 | 3/4 = 0.750 | V3-rejected (target rank-class ratio; lines 327-345) |
| 3b | Target-side Hilbert-space-image-dim ratio | dim_HS-image = 5 | dim_HS-target = 8 | **5/8 = 0.625** | vdd D2 below (target trace-dim ratio; substrate-IS via NPZ chi_prime_target_dim) |

All four are substrate-IS invariants of the SAME χ' Kasparov KK projection. They count different categorical things:

- #1 = K_0(A_K) → K_0(target) mass-fraction preserved at the K-class-rank layer
- #2 = Tr(H_K) → Tr(χ'-image on H_K) mass-fraction preserved at the regular-representation trace layer
- #3a = K_0(target) representational-room K-rank-class-used (V3 correctly rejects as non-canonical)
- #3b = dim(target H) representational-room Hilbert-trace-dim-used (D2 candidate; structurally analogous to #2 but on target side)

V3's reasoning rejects #3a but does not extend to #3b (it considered only K-class-rank ratio, not Hilbert-trace ratio, on target side). The actual canonical-weight question reduces to: at the CM-1995 §III.4 residue formula evaluation underlying α'(M_LRD), which of #1, #2, #3b enters as the χ'_weight factor? My T1.9 derivation pins it to #2 (5/14) by direct algebraic substitution. V3 pins it to #1 (3/6) by K-theoretic-invariant analogy. #3b (5/8) is structurally possible but requires the bridge map to evaluate at the target rather than source side — which IS NOT the CM-1995 §III.4 prescription (the trace is on H_K, the source). Within the bridge-map class HKR `L_max → ∞` ∘ Connes-Karoubi, #2 (5/14) is the residue formula's natural pre-factor.

**Answers to Volovik's Q-VDD questions on V3**.

**(V3-Q-VDD-1)** — "Is the rank-class canonical 3/6 reading the unique K-theoretically natural weight, or do you read the HS-DIM 5/14 reading as the unique CANONICAL via the dimension-spectrum residue formula at L_max → ∞? If we both grant that Reading 1 captures K-class survival and Reading 2 captures Hilbert-trace mass surviving, which is the canonical 'χ'_weight' in the FRAMEWORK's convention?"

We agree on the *granted* part: Reading 1 captures K-class survival (3/6), Reading 2 captures Hilbert-trace mass surviving (5/14). I read **Reading 2 as canonical** for the χ'_weight factor IN α'(M_LRD) because α'(M_LRD) IS evaluated through the CM-1995 §III.4 residue formula's regular-representation trace, which weighs by dim_HS. The §VII.AF.1.OP-PROJ baseline's bridge map (`permanent-results-registry.md` line 14833: "HKR / K-theory boundary / Connes-Karoubi pairing") uses CM-1995 §III.4 finite-spectral-triple residue formula (line 14807: "Tr(γ · cocycle · [F, cocycle]² · |D|^{-2s})"); this trace is dim_HS-weighted; the χ'-restriction's mass-fraction inside this trace is 5/14.

The framework's convention at the W-5 baseline IS the CM-1995 §III.4 evaluator (verbatim from the §VII.AF.1.OP-PROJ theorem text line 14819: "Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula"). Under that convention, **5/14 IS the framework-canonical χ'_weight**. The 3/6 value is the framework-canonical K-class-rank index of χ' — a different invariant.

So my answer to your "which is canonical in the framework's convention" question is: it depends on which framework convention. Under the CM-1995 §III.4 residue-formula convention (the W-5 baseline bridge-map convention), 5/14 is canonical. Under the K_0(A_K)-K-class-index convention (your Kasparov KK projection class convention), 3/6 is canonical. Both are framework-recognized substrate-IS conventions. The S91 W-2 workshop's task is to adjudicate which IS the χ'_weight factor in α'(M_LRD) — and α'(M_LRD)'s evaluator IS the CM-1995 §III.4 residue formula (per the §VII.AF.1.OP-PROJ baseline + T1.9 substitution chain).

**(V3-Q-VDD-2)** — "The Kasparov-product factorization principle makes substrate-algebra deformations (χ') and regulator-kernel deformations (γ(s)) factor through the bridge map at DISTINCT layers. The 'χ'_weight' lives at the substrate-algebra-deformation layer. Reading 1's 3/6 lives at this layer intrinsically; Reading 2's 5/14 lives at the COMPOSITE layer where the trace evaluation interacts with χ'. Do you read this layer separation as supporting Reading 1 as the substrate-algebra-canonical, with Reading 2 as the bridge-map-composite-canonical (i.e., they are not competing but answer different structural questions)?"

**Yes — partially.** Your layer-separation framing IS the resolution I am driving toward. Concretely: under the Kasparov-product factorization (Paper 01 / 1811.07824 main theorem; my agent memory bundle file `s82-kasparov-abelian-proof.md` for the abelian-subfactor specialization), substrate-algebra deformations (χ' pullback / restriction) factor as one element of the Kasparov product, and regulator-kernel deformations (Γ(s) → γ(s)) factor as another element. These factor through the bridge map at distinct vertical-vs-horizontal layers.

The "χ'_weight" at the substrate-algebra-deformation **layer-1 (vertical)** IS the K-class-rank-mass-fraction 3/6 — this IS the K_0-functoriality invariant of χ' alone. I do not contest this.

The "χ'_weight" at the substrate-algebra-deformation **composed with the bridge-map evaluation** (i.e., layer-1 composed with the CM-1995 §III.4 residue formula) IS the Hilbert-trace-mass-fraction 5/14 — this IS the trace-pullback invariant of (χ' through residue formula).

These two layer-separated invariants are NOT competing. They answer different structural questions. Reading 1 = "what is χ'_*'s effect on K_0(A_K)?" Reading 2 = "what is χ'_*'s effect on the CM-1995 residue trace?". Both substrate-IS, both canonical at their respective layers.

The α'(M_LRD) observable IS at the **layer-1-composed-with-bridge-map** level (the multiplicative decomposition `R_universal · χ'_weight · (M_KK/M_Pl)² · g` lives at the bridge-map evaluation, not at the bare K_0 layer). So the χ'_weight factor in α'(M_LRD) IS the composite-layer invariant 5/14, not the bare-K_0 invariant 3/6.

This supports a structural reading: **outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level**, with explicit layer-tagging of each Reading:

- Reading 1 (3/6) = bare-K_0 layer χ'-weight; canonical at the K-class-rank invariant axis (Kasparov KK index layer)
- Reading 2 (5/14) = bridge-map-composite layer χ'-weight; canonical at the CM-1995 §III.4 residue-trace invariant axis (metric layer)
- Reading 3 (~0.404 OR ~0.288 depending on pre-factor) = (c)-corridor γ(s) modulation OF whichever Reading 1/2 is the bare-K_0 OR composite-layer canonical at that corridor

This is consistent with my agent memory's four-layer hierarchy (Topology / Representation / Metric / Functional). The bare-K_0 invariant 3/6 is at the **Topology** layer (K-homology class, deformation-invariant). The CM-1995 residue-trace invariant 5/14 is at the **Metric** layer (regulator-dependent, a_k coefficients at specific τ). They cannot collapse because the four layers are structurally orthogonal in the framework's permanent results structure.

#### Re: V4 — Algebra-axis orthogonality K=3 constraint

**AGREE (corner classification; K-counter silence on within-cell weight choice)**.

I concur fully with V4's corner-classification analysis and the K-counter silence diagnosis. Specifically:

- **Reading 1 (Wedderburn-RANK 3/6) parse-tree** (workshop document lines 376-385): pure spectrum-only Wedderburn-rank arithmetic; no π(a) operator-algebra references; embedded at substrate-distance-1 pole s=3 per §VII.AF.1.OP-PROJ baseline anchor. **Cell I (algebra-INVARIANT × s=3) confirmed.**
- **Reading 2 (HS-DIM 5/14) parse-tree** (workshop document lines 387-396): pure spectrum-only Hilbert-space-dimension arithmetic; no π(a) operator-algebra references; embedded at substrate-distance-1 pole s=3 via CM-1995 §III.4 residue formula's Hilbert-space trace at n=6 pole (W3 WP §W3-4 line 1027). **Cell I (algebra-INVARIANT × s=3) confirmed.** Specifically: dim_HS arithmetic is dimension-of-summands-acting-on-themselves (i.e., dim of `End(V)` for V the standard representation per V3 line 315), which IS a spectrum-only operation on the substrate algebra's structure constants (rank squares for the matrix-algebra summands: rank(ℂ)² = 1, rank(ℂ²)·rank(ℂ²) for ℍ → 4, rank(ℂ³)² = 9). No state-pair `π(a)` references; algebra-INVARIANT axis confirmed.
- **Reading 3 (digamma-modulated 0.40380) parse-tree** (workshop document lines 401-407): pure spectrum-only Wedderburn-rank arithmetic + digamma scalar (algebra-INVARIANT scalar coefficient ψ(s_*=1) = −γ_Euler); same pole s=3. **Cell I (algebra-INVARIANT × s=3) confirmed.**

All three readings inhabit Cell I × s=3 by the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)` (registry line 12991-13002, lizzi PRIMARY + connes CO-AUTHOR at S88 W5b-45, 2026-05-04; audit-script `_corner_classification_audit.py`). The K=3 MANDATORY clause's enforcement role — preventing cross-corner co-primary structures per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close, 2026-04-30) — is satisfied by all three readings (no cross-corner co-primary structure proposed). **V4's diagnosis that the K-counter does NOT discriminate within Cell I is structurally correct.** I concur.

I also concur with V4 lines 411-422 enumerating what the K=3 MANDATORY clause forbids (conditions 1-4) and noting that none of the three readings violate these. The candidate canonical-WEIGHT verdict for any of the three would land at §VII within Cell I × s=3, not across cells.

**DISAGREE (the three substrate-priority axes (α), (β), (γ) point under layer-decomposition framing)**.

V4 lines 444-451 introduces three substrate-priority axes to discriminate within Cell I, and reads each as pointing toward Reading 1. I concur that the three AXES are valid axes; I dispute the COMPOSITIONAL DIRECTION each axis points under the layer-functor F from `epistemic-discipline.md §"Layer-Decomposition"`.

**Axis (α) — K-theoretic vs representation-theoretic axis** (V4 line 445).

V4 claim: Wedderburn-RANK invariants are preserved by Kasparov-KK projections; HS-DIM invariants are NOT preserved; therefore Reading 1 wins on the inheritance-morphism-canonical layer.

Re:Re-framing: Wedderburn-RANK IS preserved at the K_0 functor layer. HS-DIM at the regular representation IS NOT preserved at the K_0 functor layer — but it IS preserved at the **regular-representation trace functor layer** (`Tr` on H_K is a substrate-IS canonical functional independent of K_0; it preserves trace-mass under the canonical χ'-pullback by construction; T1.9 substitution chain Step 4 line 977 ALGEBRAICALLY substitutes this preservation in the multiplicative decomposition without invoking K_0 functoriality at all). The axis (α) does not point uniquely to Reading 1; it points to Reading 1 at the K_0 layer AND to Reading 2 at the regular-representation trace layer. The χ'_weight factor IN α'(M_LRD) lives at the regular-representation trace layer (the residue formula's substrate-IS evaluator), so axis (α) under THAT layer evaluation points to Reading 2.

**Axis (β) — Source-side vs target-side axis** (V4 line 447).

V4 claim: inheritance-restriction weight is structurally a source-side mass-fraction surviving, NOT a target-side representational-room ratio; therefore Reading 1 (source-side 3/6) wins over the hypothetical fourth target-side candidate.

I concur this axis correctly rejects target-side **rank-class** ratio (3/4) as non-canonical. But Reading 2's 5/14 is ALSO a source-side mass-fraction surviving — it counts the source-side Hilbert-trace-dim-mass that χ' carries through to the surviving (ℂ ⊕ ℍ) image. Reading 2 = (dim_HS source-image)/(dim_HS source-total) = 5/14, where both numerator and denominator are evaluated on the SOURCE side (H_K, the regular representation of A_K acting on itself). The source-side-versus-target-side axis distinguishes Readings 1 and 2 from the hypothetical 3/4 target-side rank ratio — but it does NOT distinguish Reading 1 from Reading 2; both are source-side. Axis (β) is silent on the 3/6 vs 5/14 choice.

(The D2 target-side dim ratio 5/8 candidate I propose below IS on the target side per V4's axis (β); I acknowledge axis (β) downgrades it relative to Readings 1 and 2. D2 develops the case for it as a fourth candidate worth recording, not as the primary canonical — and explicitly under SHARED-ANCHOR-COMPANION tagging.)

**Axis (γ) — Primary corridor vs auxiliary corridor axis** (V4 line 449).

V4 claim: Element-1 (b) χ'-pullback is PRIMARY (Readings 1+2 corridor); element-1 (c) γ(s)-modified-kernel is AUXILIARY (Reading 3 corridor); the unqualified "canonical χ'_weight on A_K" refers to the PRIMARY (b)-corridor's pre-factor, not the AUXILIARY (c)-corridor's modulated value.

I concur with this axis fully. Reading 3 IS the (c)-corridor AUXILIARY canonical and is NOT a candidate for the unqualified primary "canonical χ'_weight on A_K". This axis correctly discriminates Reading 3 from the primary canonical. But within the (b)-corridor PRIMARY, axis (γ) does NOT discriminate Reading 1 from Reading 2 — both inhabit the (b)∘(d) primary corridor.

**Net effect of axes (α)+(β)+(γ) under layer-decomposition**.

- Axis (α) → ambiguous between Reading 1 (K_0 layer canonical) and Reading 2 (regular-representation trace layer canonical) per layer-decomposition.
- Axis (β) → distinguishes Readings 1+2 from target-side rank ratio 3/4 (both source-side); silent on 3/6 vs 5/14.
- Axis (γ) → distinguishes Reading 3 from the primary (b)-corridor; silent on 3/6 vs 5/14 within (b)-corridor.

The three axes Volovik proposed correctly DOWNGRADE the target-side rank ratio (V3's hypothetical fourth candidate) and correctly DOWNGRADE Reading 3 from the unqualified primary canonical. They do NOT discriminate Reading 1 from Reading 2 within the (b)-corridor primary at Cell I × s=3. **The within-cell adjudication between Reading 1 and Reading 2 requires a fourth axis I introduce below.**

**MISSED (axis (δ): evaluator-trace-layer vs K_0-rank-layer axis)**.

The fourth substrate-priority axis V4 misses is the **evaluator-trace-layer axis**: which of the multiplicative pre-factors enters α'(M_LRD) IS determined by what evaluator computes α'(M_LRD), and the evaluator IS the CM-1995 §III.4 finite-spectral-triple residue formula `Tr(γ · cocycle · [F, cocycle]² · |D|^{-2s})` with regulator `|D|^{-2s}` per the §VII.AF.1.OP-PROJ baseline (registry line 14807). This evaluator's algebra-trace is dim_HS-weighted by the trace's regular-representation construction; the χ'-restriction's mass-fraction inside this trace is 5/14 by algebraic substitution (T1.9 Steps 2-5 lines 962-984).

Axis (δ) is the structural realization of `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence at the substrate-physics-observable layer: weight-n substrate-physics observables map to enforcement-strength-n methodology rules via the layer functor F. Per the four-layer hierarchy in my agent MEMORY.md, α'(M_LRD) is a **Metric-layer observable** (regulator-dependent residue trace; a_k coefficient family at specific τ). Metric-layer observables are computed by Tr-based evaluators (regular-representation trace), not by K_0-class-index evaluators (K-homology pairing). The χ'_weight at the metric layer IS the trace-mass-fraction 5/14.

Axis (δ) discriminates Reading 1 from Reading 2 by the layer at which α'(M_LRD) lives. α'(M_LRD) is metric-layer; the metric-layer χ'_weight is 5/14. Axis (δ) → Reading 2 ✓.

This fourth axis is the structural complement to V4's three axes:
- (α) K-theoretic vs representation-theoretic: V4 read it as K-canonical; I read it as layer-dependent (Reading 1 at K_0 layer, Reading 2 at trace layer).
- (β) Source-side vs target-side: both Readings 1+2 source-side; silent.
- (γ) Primary vs auxiliary corridor: both Readings 1+2 primary (b)-corridor; silent.
- **(δ) Evaluator-trace-layer vs K_0-rank-layer: α'(M_LRD) is metric-layer evaluator; trace-layer χ'_weight = 5/14 → Reading 2 ✓.**

Composing axes (α)+(β)+(γ)+(δ) under layer-decomposition: axis (δ) breaks the tie within Cell I × s=3 between Reading 1 and Reading 2 in favor of Reading 2 *for the χ'_weight in α'(M_LRD)*; Reading 1 retains canonical status at the K_0 layer for the K-class-rank index of χ' (a different question).

**EMERGES**.

The K=3 MANDATORY clause's silence on within-cell weight choice (V4's structural reading) IS the correct framing. The within-cell adjudication requires a Phi-correspondence-aware layer-decomposition argument — which V4 does not invoke. Once invoked (axis (δ)), the adjudication routes to:

- Reading 1 IS canonical at the K_0-layer χ'_*-functor invariant axis (Topology layer of the four-layer hierarchy).
- Reading 2 IS canonical at the CM-1995 §III.4 regular-representation trace evaluator axis (Metric layer of the four-layer hierarchy).
- The four-layer hierarchy in my agent MEMORY.md (Topology / Representation / Metric / Functional) makes these structurally orthogonal — a single "canonical χ'_weight on A_K" claim that conflates them is layer-decomposition-naive.

This still supports outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level (with Phi correspondence pin), NOT outcome (i) single-canonical-winner. The (b)-corridor admits TWO non-fungible canonical χ'_weights (3/6 at K_0 layer; 5/14 at trace layer); the (c)-corridor admits a digamma-modulated form of whichever is the (b)-corridor canonical at the matching layer (T1.8's 0.404 inherits Reading 1 at K_0; an alternative 0.288 = (5/14)·(1 − γ_Euler/3) inherits Reading 2 at trace).

**Answers to Volovik's Q-VDD questions on V4**.

**(V4-Q-VDD-1)** — "Do you concur that the §VII.U.2 four-corner partition's algebra-axis orthogonality K=3 MANDATORY clause is satisfied by all three readings (all Cell I × s=3 by parse-tree decision procedure), and that the K-counter does NOT supply a discriminator among them at the within-cell level?"

**Yes, fully.** All three readings inhabit Cell I × s=3 by parse-tree decision procedure (the three parse-tree expansions I verified above are pure spectrum-only operations on the substrate's algebra structure constants — Wedderburn-rank arithmetic, Hilbert-space-dim arithmetic, digamma-scalar-modulated rank arithmetic — none invoke π(a) operator-algebra references). The K=3 MANDATORY clause's enforcement at conditions 1-4 is satisfied by all three; no cross-corner co-primary structure is proposed; no cross-pole co-primary structure is proposed; no cross-cell magnitude comparison is offered as a PASS/FAIL gate. The K-counter is structurally orthogonal to the within-cell canonical-weight question. The within-cell adjudication requires substrate-priority axes ((α), (β), (γ), and my proposed (δ)) operating WITHIN Cell I × s=3.

**(V4-Q-VDD-2)** — "The §VII.U.2 line 12991 parse-tree decision procedure applies to state-history label observables (e.g., `Var_a(n_a^GGE)`). The same parse-tree expansion principle applies here: χ'_weight does NOT carry a state-history label, but its three substrate-derivations all reduce to pure spectrum-only operations on algebra-rank / Hilbert-dim / digamma data — all parse to Cell I × s=3. Do you read this as confirming the K-counter is structurally orthogonal to the within-cell canonical-weight question?"

**Yes, fully.** The parse-tree decision procedure at `permanent-results-registry.md §VII.U.2 clause (e)` is the same procedural rule that retroactively reclassified `Var_a(n_a^GGE)` from "naively Corner IV" to "structurally Corner II" via Bogoliubov closed form (S88 W-17 §V.3 corrigendum; mack-cosmic-bridge sole writer 2026-05-08; registry line 12961 worked example). The three χ'_weight derivations parse identically to Cell I × s=3 via that same decision procedure. The K-counter MANDATORY clause's enforcement is satisfied identically by all three. **The K-counter is structurally orthogonal to the within-cell canonical-weight question** — it operates at the cross-corner / cross-pole orthogonality axis (which all three readings avoid by inhabiting the same cell × pole), not at the intra-cell weight-choice axis.

This confirms my Re:V1 + Re:V3 layer-decomposition framing: the within-cell adjudication operates at the Phi-correspondence layer-functor axis (which `epistemic-discipline.md §"Layer-Decomposition"` formalizes), not at the corner-cell axis (which the K-counter enforces). The two axes are complementary; both are necessary; neither is sufficient alone.

**(V4-Q-VDD-3)** — "On the substrate-priority axis (α) 'K-theoretic vs representation-theoretic': the Kasparov-KK projection class preserves K-theoretic invariants; HS-DIM is not preserved (different faithful representations give different HS-DIMs). Do you accept this as a load-bearing structural argument for Reading 1 as canonical at the inheritance-morphism layer, or do you contest it (e.g., by arguing the CM-1995 §III.4 residue formula's regular-representation trace IS the canonical evaluation and HS-DIM is the structurally privileged weight at that evaluation)?"

**I partially accept and partially contest, as a load-bearing argument that operates at a *specific* layer:**

The K-theoretic invariant 3/6 IS load-bearing at the **inheritance-morphism layer evaluated as a K_0(A_K) → K_0(target) functor** — at THAT layer, Wedderburn-RANK is canonical and HS-DIM is representation-dependent. I do not contest this. Different faithful representations of A_K on different Hilbert spaces would give different HS-DIMs (M_3(ℂ) on ℂ³ gives dim 3; M_3(ℂ) acting on its regular representation gives dim 9; etc., per V1 line 97). At the K_0 layer, 3/6 is the canonical invariant of χ'_*.

But the inheritance-morphism layer ITSELF is *layered*. The "inheritance-morphism layer" can be evaluated at:

- (1) the K_0(A_K) → K_0(target) functor (Kasparov KK projection class index): canonical invariant 3/6.
- (2) the canonical regular-representation Tr functor on (A_K, H_K, D_K) (CM-1995 §III.4 residue trace): canonical invariant 5/14 — and this IS canonical because the framework FIXES the regular representation as the canonical faithful representation in the W-5 baseline (registry line 14831-14832: "Substrate-IS observable: finite-L Hochschild pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`"; H_K IS the canonical regular representation, NOT a free choice).

Per the §VII.AF.1.OP-PROJ baseline's specification of H_K as the substrate-IS canonical regular representation, the HS-DIM weights {1, 4, 9} are NOT representation-arbitrary — they are the canonical regular-representation dimensions on the substrate-IS H_K. The "different faithful representations give different HS-DIMs" objection (V1 line 97) is true in the abstract but does NOT apply at the framework's pinned (A_K, H_K, D_K) evaluation, because the framework PINS the regular representation as canonical.

**Net answer**: I accept axis (α) as load-bearing at the K_0 layer (where 3/6 is canonical), and I contest its conclusion at the regular-representation Tr layer (where 5/14 is canonical because the substrate H_K is framework-pinned as the canonical regular representation). The substrate-priority axis (α) does not point uniquely to Reading 1; it points to whichever layer the χ'_weight is evaluated at. α'(M_LRD)'s χ'_weight IS evaluated at the regular-representation Tr layer (per the residue formula's prescribed evaluator).

#### Re: V5 — Cross-cutting registry consequences

**AGREE (CF-37 escape-clause empirical refutation; §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ no-delta on the unrestricted baseline; Stage-2 HARD-exclude protocol)**.

I concur with multiple V5 structural readings:

1. **CF-37 PROXY-REFINEMENT-PENDING escape-clause empirically refuted** (V5 line 466). The S90 W4 §W4-1 Closing Notes #2 pre-registered the hypothesis that the FULL CM-1995 §III.4 evaluation might produce χ'_weight ~4.5× larger than the structural-ansatz 0.5 (which would have landed α'_FULL ∈ [1.527e-3, 2.836e-3] inside the Sub-clause B 30% RATIO band). My T1.9 derivation (`session-91-w3-workingpaper.md` §W3-4 lines 944-998) ALGEBRAICALLY refuted this: the FULL CM-1995 §III.4 evaluation produces χ'_weight_FULL = 5/14 = 0.357, which is **factor 5/7 ≈ 0.714× the structural-ansatz 0.5**, in the *opposite direction* (UNDER-shoot, not over-shoot). The escape-clause is empirically dead — neither over- nor under-shooting recovers the 1/458 anchor at substrate-distance-1.

2. **§VII.AF.1.OP-PROJ no-delta on the unrestricted W-5 baseline** (V5 line 468). The §VII.AF.1.OP-PROJ entry's R_universal_HP1_strict_F4 = 1.030902 (canonical_constants.py:250) IS the unrestricted Connes-Karoubi pairing on the substrate's intrinsic Hochschild cocycle space — evaluated WITHOUT χ'-restriction. It does NOT consume any χ'_weight factor in its anatomy; the χ'_weight factor enters only at the χ'-restricted observable α'(M_LRD), which is downstream of the W-5 baseline. V5 is correct: the W-5 baseline retains STAGE-1-CANDIDATE / Level-3 satisfaction at 0.0095% F_4 strict, regulator-class INVARIANT, L_max-saturated at L_max=10 with 10× margin inside L^{-3} envelope. No corrigendum required under EITHER Reading 1 OR Reading 2 canonical. **Concur.**

3. **§VII.AU.OP-PROJ no-delta on FWD-C1 deferred-pending status** (V5 line 470). The FWD-C1 Pillar I↔II bridge candidate's substrate-IS observable is `n_s_FW² − 1 ≡ α_s_canonical` (Pillar I M⁴ × SU(3) Mellin-cone closure at substrate-distance-1 pole s=3); this is STRUCTURALLY ORTHOGONAL to the LRD α-anchor at Pillar III↔IV (HP^1 cohomology). The Hybrid Independence Test of `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` confirms axis (i) — distinct substrate-IS pillar — between Pillar I and Pillar III. The canonical-weight verdict on χ'_weight does NOT modify n_s_FW or α_s_canonical predictions. §VII.AU.OP-PROJ retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (per S90 W1-15 deferred-pending re-tag, CF-65 / W-6 CF-3 forward); the χ'_weight canonicalization is structurally orthogonal to FWD-C1's parameterized slope_A first-extraction. **Concur.**

4. **Stage-2 cross-axis verify HARD-exclude protocol** (V5 lines 502-514). I concur fully with the HARD-exclusion of volovik (V1-V5 author) AND vdd (Round 1 cross-synthesis author + T1.8 Axis-B author + T1.9 Axis-A author) per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach extension (S88 W-14 W4a-17 V.2 MANDATORY at K=1; corpus instance #1 = original-authoring-agent exclusion with downstream-inheritance reach). Both volovik and vdd hold load-bearing structural arguments and cannot serve as Stage-2 independent-verify reviewers without breaking the "without prior workshop context" protocol. V5's recommended Axis-A = connes-ncg-theorist (NCG-axiomatic depth on Kasparov-KK projections + Wedderburn-Artin K-theory) and Axis-B = mack-cosmic-bridge (§VII registry sole-writer authority per `feedback_mack-bridge-role.md`) is structurally sound. **Concur.**

5. **No retroactive edit to CF-37 / T1.8 / T1.9 verdict lines** (V5 lines 585-586). I concur. All three verdict lines (audit_sha256 `10ee072fe2c193f3...`, `8ab158e9e45aab37...`, `752a8f2b862a9aa5...`) emit FAIL composite at the empirical 1/458 anchor; the canonical-weight verdict resolves *what the substrate-IS canonical χ'_weight IS*, not *what α'(M_LRD) IS*. Per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`, all three retain their FAIL verdicts unchanged; no `supersedes=` tag is required because the canonical-weight verdict at S92 does NOT contradict the empirical FAIL — it CLARIFIES which substrate-derivation IS canonical without modifying the empirical observable's value at the dimensional bridge factor bottleneck. **Concur.**

**DISAGREE (the SOURCE-DOUBLE-CITE-CO-PRIMARY structure V5 proposes, AND the single-canonical outcome (i) framing)**.

**SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure as proposed in V5 lines 472-477.**

V5 proposes: ANCHOR-1 (V_input, S89 §W2-3 derived theorem) + ANCHOR-2 (C_output, Wedderburn-Artin algebra-axis K-theoretic rank-ratio canonical reading). This is a sequential V_input + C_output chain per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` detection conditions 1-4.

I dispute the **C_output identification**. V5's C_output is "Wedderburn-Artin algebra-axis K-theoretic rank-ratio canonical reading" — which is precisely the Reading 1 canonical position being adjudicated by this workshop. Pre-committing to Reading 1 as C_output in the SOURCE-DOUBLE-CITE-CO-PRIMARY structure BEGS the canonical-weight question. The workshop's job is to derive the canonical, NOT to assume it as C_output.

If outcome (i) Reading 1 canonical is the verdict, then V5's SOURCE-DOUBLE-CITE-CO-PRIMARY is structurally well-posed at the K_0 layer. But if outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level is the verdict, then the registry-landing carries TWO anchor structures (one per layer):

- §VII.{slot}.OP-PROJ-K0-LAYER: SOURCE-DOUBLE-CITE-CO-PRIMARY with ANCHOR-1 = S89 §W2-3 + ANCHOR-2 = Wedderburn-Artin K-theoretic rank-ratio 3/6 (Reading 1 canonical at the K_0 layer)
- §VII.{slot}.OP-PROJ-METRIC-LAYER: SOURCE-DOUBLE-CITE-CO-PRIMARY with ANCHOR-1 = S89 §W2-3 + ANCHOR-2 = CM-1995 §III.4 residue formula's regular-representation trace 5/14 (Reading 2 canonical at the Metric layer)

These two parallel-companion slots cannot be co-primary OF EACH OTHER (per `registry-landing.md` Detection clause 4 + S88 W-15 V.6 / B.14 cross-corner co-primary FORBIDDEN; BOTH inhabit Cell I × s=3 so cross-corner is not an issue here, but `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY K=3 sub-clause forbids OP-PROJ + STATE-PROJ co-primary anchoring as STRUCTURAL-ORTHOGONAL-COMPANION). Two STRUCTURAL-ORTHOGONAL-COMPANION slots at the K_0 layer and Metric layer are the registry's expression of the layer-decomposition adjudication.

**Single-canonical outcome (i) framing.**

V5's S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT pre-registration (lines 480-577) lands outcome (i) Reading 1 canonical as a single §VII slot. This pre-registration is well-formed IF outcome (i) is the workshop verdict. My Re:V1 + Re:V3 + Re:V4 + Re:V5 argument routes me toward **outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level**, which would shape the registry-landing differently:

- TWO STRUCTURAL-ORTHOGONAL-COMPANION slots (one per layer), each registry-eligible independently.
- §VII.{slot-a}.OP-PROJ-K0-LAYER carries Reading 1 (3/6) at the K_0 functor invariant layer; substrate-IS structural theorem at the Topology layer of the four-layer hierarchy.
- §VII.{slot-b}.OP-PROJ-METRIC-LAYER carries Reading 2 (5/14) at the CM-1995 §III.4 residue trace invariant layer; substrate-IS structural theorem at the Metric layer.
- Both are anchored by S89 §W2-3 (V_input) and by their respective C_output identities (Wedderburn-Artin vs Connes-Moscovici 1995 §III.4).
- Stage-2 cross-axis verify dispatches as one wave with BOTH slots PASS-AND'd: connes-ncg-theorist audits the K_0-layer slot (NCG-axiomatic Wedderburn-Artin canonical) AND the Metric-layer slot (NCG-axiomatic CM-1995 §III.4 residue canonical); mack-cosmic-bridge audits both slots' bridge-map consistency. The JOINT clauses (a)+(b)+(c)+(d) of V5's pre-registration extend to JOINT-K0 clauses + JOINT-Metric clauses.

This outcome-(ii) framing does NOT contradict V5's outcome-(i) framing on any of the AGREE items above — both outcomes preserve the no-delta on §VII.AF.1.OP-PROJ baseline, no-delta on §VII.AU.OP-PROJ FWD-C1, Stage-2 HARD-exclude on volovik + vdd, and the absolute permanence of CF-37 / T1.8 / T1.9 verdict lines. The outcomes differ only on the §VII slot structure for the canonical-weight verdict itself (single Reading 1 slot vs two STRUCTURAL-ORTHOGONAL-COMPANION slots).

**MISSED (Hybrid Independence Test K-counter under outcome (ii))**.

V5 lines 495-500 computes the Hybrid Independence Test for outcome (i) single-canonical: SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tag because all axes (i)+(ii)+(iii) shared with §VII.AF.1.OP-PROJ baseline, only axis (iv) independent algebraic envelope distinct (K_0-rank L_max-independent vs L^{-3} bound). V5 reads this as K-counter stays at K=1.

Under outcome (ii) TWO slots at K_0 layer + Metric layer:

- §VII.{slot-a}.OP-PROJ-K0-LAYER: same shared-anchor analysis as V5's outcome (i); SHARED-ANCHOR-COMPANION; K-counter does NOT advance.
- §VII.{slot-b}.OP-PROJ-METRIC-LAYER: axis (iv) IS distinct (CM-1995 §III.4 regular-representation Tr-mass-fraction has a L_max-INDEPENDENT structural-ansatz envelope at the FULL evaluator IS algebra-exact at finite L_max; this is the same envelope class as W-5 baseline at L^{-3} d=4 because finite-L corrections vanish at the dim-spec residue saturation per T1.9 envelope_n ≈ −1.22e-20 ≈ 0). Net axis (iv) under STRICT reading: SHARED with §VII.AF.1.OP-PROJ. Hybrid Independence Test K-counter does NOT advance from this slot either.

So BOTH slots under outcome (ii) land as SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE, recorded OUTSIDE the K-counter table per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` companion-tagging clause. The K-counter advancement from K=1 to K=2 is NOT triggered by either reading. This is consistent with V5's outcome (i) reading on the K-counter point.

But — and this IS the substantive new claim outcome (ii) makes — outcome (ii) increases the framework's calibration corpus on the **Phi-correspondence layer-decomposition K-counter** (`epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence weight-n / Σ_n image). At what K is the Phi-correspondence layer-decomposition K-counter currently? `epistemic-discipline.md §"Layer-Decomposition" §"K-counters and per-instance corpus"` cross-links to `pru-class-corpus.md §§9-10` for definitional-datum-vs-derived-theorem + F(observable) vs F(trigger predicate) sub-rules at advisory K=1 each — not the same as the Phi-correspondence layer K-counter on substrate-IS observable two-layer-coincident invariants. My Re:V5 raises this as a forward question for the Stage-2 reviewers: should the χ'_weight K_0-layer + Metric-layer simultaneous canonical landing be classified as an instance on a new Phi-correspondence two-layer-coincident-invariant calibration corpus? I queue this as a substrate-physics carry-forward to S92 below.

**EMERGES**.

V5 + Re:V5 + accumulated Re:V1-V4 layered framing point to outcome (ii) **SIMULTANEOUS-VALIDITY at the layer-decomposition level**, NOT outcome (i) single-canonical. The registry landing shape changes from "one §VII slot with Reading 1 canonical" to "two STRUCTURAL-ORTHOGONAL-COMPANION §VII slots, one per layer (K_0 / Metric), both SHARED-ANCHOR-COMPANION with §VII.AF.1.OP-PROJ baseline". The Stage-2 cross-axis verify protocol Volovik proposes extends to BOTH slots PASS-AND'd; the HARD-exclude on volovik + vdd remains; connes + mack are the recommended Axis-A + Axis-B. The §VII.AF.1.OP-PROJ baseline + §VII.AU.OP-PROJ FWD-C1 retain no deltas. CF-37 / T1.8 / T1.9 verdict lines retain absolute permanence at FAIL.

**Answers to Volovik's Q-VDD questions on V5**.

**(V5-Q-VDD-1)** — "Do you concur that the S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT registry slot should land as STAGE-1-CANDIDATE with Reading 1 canonical (Wedderburn-RANK 3/6) AND with explicit SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tagging (Hybrid Independence Test stays at K=1)? Or if you propose outcome (ii) SIMULTANEOUS-VALIDITY or (iii) OPEN-REGISTRY-SLOT instead, what registry structure do you propose and how does it integrate with the §VII.AF.1.OP-PROJ baseline + §VII.AU.OP-PROJ FWD-C1 cross-pillar bridge structure?"

I propose **outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level**, with the following registry structure:

- **Two STRUCTURAL-ORTHOGONAL-COMPANION §VII slots** at next-free letters (S92 W1 allocation):
  - `§VII.{X}.OP-PROJ-K0-LAYER`: Reading 1 canonical (Wedderburn-RANK 3/6 = 0.500) at the K_0(A_K) → K_0(target) functor invariant layer; SOURCE-DOUBLE-CITE-CO-PRIMARY with ANCHOR-1 = S89 §W2-3 derived theorem + ANCHOR-2 = Wedderburn-Artin K-theoretic rank-ratio canonical reading; STAGE-1-CANDIDATE; SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tag relative to §VII.AF.1.OP-PROJ baseline.
  - `§VII.{X+1}.OP-PROJ-METRIC-LAYER`: Reading 2 canonical (Hilbert-trace 5/14 ≈ 0.357143) at the CM-1995 §III.4 regular-representation trace invariant layer; SOURCE-DOUBLE-CITE-CO-PRIMARY with ANCHOR-1 = S89 §W2-3 derived theorem + ANCHOR-2 = Connes-Moscovici 1995 §III.4 residue formula's dim-spec trace canonical reading; STAGE-1-CANDIDATE; SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tag relative to §VII.AF.1.OP-PROJ baseline.
- **STRUCTURAL-ORTHOGONAL-COMPANION cross-reference between the two slots**: per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 (S88 W8-92, 2026-05-05) operator-projection vs state-projection orthogonality clause AND per `epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence weight-n image axis. NEITHER slot is co-primary of the other; both are independently registry-eligible.
- **No delta** to §VII.AF.1.OP-PROJ baseline (unrestricted W-5 baseline) or §VII.AU.OP-PROJ FWD-C1 (Pillar I↔II, n_s_FW canonical first-extraction queue). Both retain pre-existing status per V5's no-delta analysis.
- **Stage-2 cross-axis verify** dispatches as one wave with BOTH slots PASS-AND'd: Axis-A = connes-ncg-theorist (audits Wedderburn-Artin K_0 canonical AND CM-1995 §III.4 metric canonical from NCG-axiomatic side); Axis-B = mack-cosmic-bridge (audits bridge-map consistency on BOTH slots from cosmological-anchor side); HARD-exclude volovik + vdd; JOINT clauses (a)+(b)+(c)+(d) extend to JOINT-K0 + JOINT-Metric.

This registry structure integrates with §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ cleanly: both new slots are SHARED-ANCHOR-COMPANION relative to §VII.AF.1.OP-PROJ baseline (axes (i)+(ii)+(iii) shared; axis (iv) partial); neither modifies §VII.AU.OP-PROJ FWD-C1's deferred-pending status. Net: same registry no-delta on existing entries; two new STAGE-1-CANDIDATE slots at S92 W1 instead of one.

If volovik prefers outcome (i) and Round 2 produces convergence on Reading 1 canonical alone, the registry structure collapses to V5's pre-registered single-slot form. I do NOT insist on outcome (ii) unless Round 2 produces unresolved DISSENT at the layer-decomposition layer; the workshop's verdict in Round 2 decides which outcome lands.

**(V5-Q-VDD-2)** — "The CF-37 PROXY-REFINEMENT-PENDING tag's pre-registered hypothesis (~4.5× over-shoot) was empirically refuted by your T1.9 derivation (factor 5/7 = 0.714× UNDER-shoot, not 4.5× over-shoot). Under Reading 1 canonical, the tag is structurally RESOLVED in the FAIL direction. Does your T1.9 derivation establish a STRONGER claim than this (e.g., the FULL CM-1995 5/14 weight is itself the canonical, and Reading 1's 3/6 is the structural-ansatz under-approximation)? If so, what argument resolves the V1/V3 K-theoretic / source-side / primary-corridor priority axes in favor of Reading 2?"

**Yes — partially.** T1.9 establishes a structural claim STRONGER than V5's reading of "CF-37 escape clause refuted": T1.9 establishes that the **FULL CM-1995 §III.4 evaluator's substrate-IS canonical χ'_weight IS 5/14**, by direct algebraic substitution into the residue formula (Step 5 line 983: `α'_FULL = R_universal · (5/14) · (M_KK/M_Pl)² · g`). The 5/14 value is NOT an under-approximation or correction to 3/6 — it IS the residue formula's substrate-IS canonical evaluation. Reading 1's 3/6 is a DIFFERENT substrate-IS invariant of χ' at a DIFFERENT categorical layer (K_0-rank-mass-fraction). Both are canonical at their respective layers.

The argument resolving V1/V3's three substrate-priority axes (α)+(β)+(γ) in favor of Reading 2 *for the χ'_weight in α'(M_LRD)* is the fourth axis (δ) I introduced in Re:V4: the **evaluator-trace-layer axis**. α'(M_LRD) is computed by the CM-1995 §III.4 residue formula's regular-representation trace evaluator (per the §VII.AF.1.OP-PROJ baseline bridge map citation); this evaluator weighs by dim_HS, not by K_0-rank; the χ'-restriction's mass-fraction inside this trace is 5/14 by algebraic substitution (verified in T1.9 Steps 2-5 lines 962-984). At the **layer where α'(M_LRD) lives**, 5/14 is canonical.

Reading 1's 3/6 retains canonical status at the K_0(A_K) → K_0(target) functor layer, which IS NOT the layer α'(M_LRD) lives at. The two readings are non-fungible canonicals at distinct layers — Reading 2 is the canonical χ'_weight IN α'(M_LRD); Reading 1 is the canonical K-class-rank index of χ' (a DIFFERENT observable that does not appear in α'(M_LRD)'s multiplicative decomposition).

So the STRONGER claim T1.9 establishes is: **the CM-1995 §III.4 evaluator's canonical χ'_weight IS 5/14, and Reading 1's 3/6 is canonical AT A DIFFERENT LAYER, not the same layer α'(M_LRD) lives at**. This routes naturally to outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level — both Readings are canonical, each at its own layer, neither at the other's layer.

**(V5-Q-VDD-3)** — "The §VII.AU.OP-PROJ FWD-C1 deferred-pending entry shares the substrate-distance-1 pole s=3 with this workshop's canonical-weight slot. Both inhabit Cell I × s=3 by parse-tree decision procedure. Is there a structural relationship between FWD-C1's parameterized slope_A canonical first-extraction (CF-65) and the canonical χ'_weight verdict that would suggest joint Stage-2 dispatch or shared cross-axis reviewer pool? Or are they fully orthogonal (Pillar I↔II vs Pillar III↔IV)?"

**Fully orthogonal at the cross-pillar axis; potentially co-occupant at the Cell I × s=3 corner-cell axis; NOT joint Stage-2 dispatch.**

The structural relationship between FWD-C1's substrate-IS observable (`n_s_FW² − 1 ≡ α_s_canonical`) and the χ'_weight canonical-weight verdict's substrate-IS observable (K-class-rank-mass-fraction OR Hilbert-trace-mass-fraction surviving χ') is bounded as follows:

1. **Same Mellin pole**: both inhabit substrate-distance-1 pole s=3 (per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` pole-index canonical). Confirmed.

2. **Same corner cell**: both inhabit Cell I × s=3 (algebra-INVARIANT × Mellin pole s=3). Confirmed.

3. **DIFFERENT cross-pillar bridge**: FWD-C1 = Pillar I (M⁴ × SU(3) spectral-action n_s) ↔ Pillar II (Planck CMB observational); χ'_weight = Pillar III (HP^1 cohomology) ↔ Pillar IV (Peotta-Törmä quantum-metric). The substrate-IS observable and laboratory-IN observable identities are DIFFERENT pillars on both sides per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` axes (i) and (ii). So the cross-pillar bridge identities are structurally orthogonal.

4. **DIFFERENT substrate-physics object**: FWD-C1 is on the n_s acoustic-mode spectral-action observable; χ'_weight is on the inheritance-morphism-restricted Hochschild cocycle pairing. These are different functionals on the SAME substrate algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); they do NOT compose multiplicatively in the four-layer hierarchy.

5. **POTENTIAL Phi-correspondence layer-decomposition cross-link**: BOTH might have K_0-layer + Metric-layer two-canonical structure if FWD-C1's `α_s_canonical` admits a similar K-theoretic / trace-mass dual-layer reading. This is a forward question I queue as carry-forward for S92+ but is NOT immediate joint-dispatch material.

**Joint Stage-2 dispatch recommendation: NO**. The cross-pillar orthogonality on axes (i)+(ii) is strong enough that connes (Stage-2 Axis-A) and mack (Stage-2 Axis-B) can audit each slot independently without joint coupling. Shared cross-axis reviewer pool **is appropriate**: connes + mack are the right Axis-A + Axis-B for BOTH the χ'_weight workshop's Stage-2 (this workshop's recommended dispatch) AND the FWD-C1 first-extraction's Stage-2 (S92+ W-6 CF-3 / CF-65 dispatch); they are NCG-axiomatic + cosmological-anchor experts respectively and serve well for both. But the two Stage-2 dispatches are **separate gates**, not joint. Volovik + vdd remain HARD-excluded from both.

**Net answer**: Cross-pillar orthogonal; co-occupant on Cell I × s=3 corner-cell; separate Stage-2 dispatches; same cross-axis reviewer pool is appropriate.

### Part 2: Original Analysis

#### D1: NCG-axiomatic CM-1995 §III.4 dimension-spectrum residue formula IS canonical

**Claim**. The Hilbert-space-DIMENSION fraction 5/14 = (dim_HS(ℂ) + dim_HS(ℍ)) / dim_HS(A_K) = (1 + 4) / (1 + 4 + 9) IS the **substrate-IS canonical χ'_weight at the Connes-Moscovici 1995 §III.4 dimension-spectrum residue formula evaluation** that the W-5 baseline R_universal uses as its bridge map. The claim is structural at the NCG-axiomatic layer of the framework's permanent results: the residue formula's regular-representation trace is the substrate-IS canonical functional on the finite spectral triple (A_K, H_K, D_K(τ_fold)) at the Hochschild-cocycle pairing layer, and the χ'-restricted trace's mass-fraction is fixed by the dim-spec residue trace's algebraic structure to dim_HS(image)/dim_HS(A_K).

**Substitution chain (CM-1995 §III.4 dim-spec residue formula → 5/14)**.

```
Step 1 (Definitions).
  Finite spectral triple:     (A_K, H_K, D_K(τ_fold))
                              with A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), KO-dim=6.
  H_K = regular representation of A_K on itself; dim_HS(H_K) = dim_HS(A_K) = 1 + 4 + 9 = 14
                              (per session-91-w3-workingpaper.md §W3-4 lines 952-954).
  Inheritance morphism:        χ': A_K → M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ);
                              ker(χ'|_{M_3(ℂ)}) = M_3(ℂ) entire (S89 §W2-3 derived theorem,
                              audit_sha256 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843).
  Dimension spectrum:          dim_spec((A_K, H_K, D_K)|_{L_max=10}) = {0, 2, 4, 6, 8}
                              (per session-91-w3-workingpaper.md §W3-4 dim-spec residue
                              table lines 1024-1032; SU(3) d=8 spectral triple).
  CM-1995 §III.4 Chern char:   ch_k(P) = Res_{z=k}[Tr(P · D^{-2z})]
                              (Connes-Moscovici 1995 §III.4 finite-spectral-triple
                              residue formula; cited in §VII.AF.1.OP-PROJ theorem
                              text at permanent-results-registry.md line 14819).
  Connes-Karoubi pairing:      α'(M_LRD) = ⟨χ'^*[φ_g^{sym}], [ch(P_HSS'(M_LRD))]⟩
                              (finite trace sum over residue products at substrate-distance poles).

Step 2 (Hilbert-trace mass-fraction surviving χ').
  The trace Tr in CM-1995 §III.4 acts on H_K via the regular representation π_reg(A_K).
  Under χ', the surviving sub-algebra is π_reg(ℂ ⊕ ℍ) ⊂ B(H_K) acting on the
  Hilbert subspace H_χ' ⊂ H_K of dimension dim_HS(ℂ) + dim_HS(ℍ) = 1 + 4 = 5.
  The complementary subspace H_ker = π_reg(M_3(ℂ))·H_K has dim_HS = 9
  (the regular representation of M_3(ℂ) acting on its 9-dim self-image).
  Total: dim_HS(H_K) = 14 = 5 (surviving) + 9 (killed).

  At the substrate-distance-1 pole k=6 (LRD-anchor relevant per W3 WP §W3-4
  line 1027), the un-restricted residue value is

      Res_{z=6}[Tr_{H_K}(P · D_K^{-2z})]   =   8.673943e+03

  (W3 WP dim-spec residue table line 1027, un-restricted Tr column).
  The χ'-restricted residue value at the same pole is

      Res_{z=6}[Tr_{H_χ'}(P · D_K^{-2z})]  =   3.097837e+03

  (W3 WP dim-spec residue table line 1027, χ'-restricted Chern char component column).
  The trace-mass-fraction surviving χ' at pole k=6:

      (χ'-restricted residue) / (un-restricted residue)
        = 3.097837e+03 / 8.673943e+03
        = 0.357142857...
        = 5/14  (Sage-rational to machine epsilon).

  The SAME ratio 5/14 holds at every other pole {0, 2, 4, 8} of the dim spectrum:
  at pole k=8: 2.788571e+04 / 7.808000e+04 = 0.357143 = 5/14;
  at pole k=4: 4.901341e+02 / 1.372376e+03 = 0.357143 = 5/14;
  at pole k=2: 1.465751e+02 / 4.104103e+02 = 0.357143 = 5/14;
  at pole k=0: 8.891865e+01 / 2.489722e+02 = 0.357143 = 5/14.

  The trace-mass-fraction 5/14 is pole-INDEPENDENT — a structural identity at the
  dim-spec residue formula evaluator on the χ'-restricted Hilbert sub-representation.

Step 3 (Multiplicative decomposition of α'(M_LRD)).
  At L_max=10 Friedrich-Bär saturation [g(M_LRD, L=10) = 1.000 per CF-37 element-3 (d)],
  the Connes-Karoubi pairing reduces to:

      α'_FULL(M_LRD)  =  R_universal_HP1_strict_F4  ·  χ'_weight_FULL  ·  (M_KK/M_Pl_reduced)²  ·  g

  where R_universal is the un-restricted Connes-Karoubi pairing baseline (W-5
  calibration corpus instance #1; LANDED S87 W5-1; canonical_constants.py:250
  = 1.030902), and χ'_weight_FULL is the multiplicative pre-factor that the
  χ'-restriction contributes to the CM-1995 §III.4 dim-spec residue trace.

  By Step 2's pole-INDEPENDENT trace-mass-fraction 5/14:

      χ'_weight_FULL  =  5/14  ≈  0.357143.

Step 4 (Direct numerical evaluation, T1.9 Step 5 verification).
  α'_FULL(M_LRD)  =  1.030902  ·  (5/14)  ·  9.307286e-04  ·  1.000
                  =  3.426750e-04                          [T1.9 audit_sha256 752a8f2b862a9aa5...].

  Empirical anchor 1/458 = 2.183406e-03; rel_dev = 0.8431.
  Sub-clause A PASS (0 < α' < 1); Sub-clause B FAIL (rel_dev > 0.30); composite FAIL.
  T1.9 verdict line at computations/session-91/s91_gate_verdicts.txt audit_sha256 752a8f2b862a9aa5...

Step 5 (Substrate-IS direction at the canonical-evaluator layer).
  The CM-1995 §III.4 residue formula's regular-representation trace is the
  substrate-IS canonical evaluator at the W-5 baseline bridge map
  (permanent-results-registry.md §VII.AF.1.OP-PROJ line 14807-14815, line 14819
  theorem text "Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula").
  At this canonical evaluator, χ'_weight_FULL = 5/14 by direct algebraic
  substitution (Steps 2-4 above). Reading 1's 3/6 K-class-rank-mass-fraction
  IS NOT this evaluator's pre-factor — it is the K_0(A_K) → K_0(target) functor
  invariant of χ', a DIFFERENT (also substrate-IS) invariant.
```

**Why the dim-spec residue trace IS canonical at the substrate's Chern-character pairing layer**.

The Chern character pairing in NCG (Connes-Moscovici 1995 §III.4) is the substrate-IS canonical Hochschild-cocycle → Chern-character map between the cocycle space and the K-theory of the spectral triple's algebra. The pairing structure

```
ch : K_0(A) → HC^*_even(A) → HH^*_even(A)
```

evaluates Chern characters via residue trace `ch_k(P) = Res_{z=k}[Tr(P · D^{-2z})]` at the dimension spectrum. The trace `Tr` here is on H_K via the regular representation π_reg(A_K) — this is canonical because (a) the spectral triple's Hilbert-space data IS H_K via the regular representation by construction (the spectral triple (A_K, H_K, D_K) IS the data of the substrate); (b) the residue formula's regularization `D^{-2z}` requires the trace evaluator to be on the substrate-IS Hilbert space H_K, not on some auxiliary representation; (c) the dimension spectrum {0, 2, 4, 6, 8} of (A_K, H_K, D_K)|_{L_max=10} (per W3 WP §W3-4 dim-spec residue table) is fixed by the substrate algebra's structure and the Dirac operator D_K — there is no representational freedom in the choice of H_K.

This is the **substrate-IS canonical Chern-character pairing structure**: H_K is the substrate's canonical Hilbert space; π_reg is the substrate's canonical representation; `Tr` on H_K is the substrate's canonical trace; `D_K^{-2z}` is the substrate's canonical regulator (with zeta-regularization at the dim-spec residue per `a_4^ζ` regulator-pin tag at §VII.AF.1.OP-PROJ line 14815). The χ'-restriction of this canonical pairing IS the χ'-restriction of the substrate-IS canonical structure — its trace-mass-fraction IS 5/14 (Step 2 above) by algebraic substitution, NOT by representational choice.

**Cross-link to my van-den-Dungen research papers (Kasparov-bridge framing)**.

Paper 01 (1811.07824, "The Kasparov Product on Submersions of Open Manifolds") is the structural anchor for **factorization** at the Kasparov KK-bridge level. The main theorem (paper 01 §3, "On a Riemannian submersion E → B, if D_E is a regular vertically elliptic operator and D_B is an elliptic operator on B, then the tensor sum D_E ⊗ 1 + 1 ⊗ D_B represents the Kasparov product [D_E] ⊗ [D_B] in KK-theory") establishes that the **topological** Dirac-class decomposition lives at the KK-theory layer. This IS Volovik's Reading 1 layer — Kasparov KK projection class indices, K_0 functoriality. Paper 01 explicitly notes "The application to Riemannian submersions is significant because submersions model fiber bundle structures—central to modern geometry and physics. Factorizing the fundamental class of a submersion as a Kasparov product reveals the underlying multiplicative structure and enables decomposition of index-theoretic invariants along fibre directions."

Paper 01's application to spectral action computations (Paper 01 line 97-100): "When the base space is M⁴ (spacetime) and the fibres are a compact Riemannian manifold (like SU(3)), the Kasparov product enables efficient computation of the spectral action from lower-dimensional pieces". This is the four-layer hierarchy of my agent MEMORY.md: Kasparov KK gives the **Topology layer** (K-homology class, deformation-invariant); the spectral action's Mellin / Seeley-DeWitt coefficient family lives at the **Metric layer** (regulator-dependent, a_k coefficients). The Kasparov-product factorization decomposes between layers, NOT collapses them to one.

Per my agent memory's "Boundary (canonical): Kasparov product gives TOPOLOGY (K-homology class, indices, factorization). NOT ANALYSIS (spectral moments). Governs all prediction classification." — this boundary IS the structural separation I am invoking in D1. The χ'_weight factor in α'(M_LRD) is at the **ANALYSIS / Metric layer** (it appears as a multiplicative coefficient in the spectral action evaluator); the K-class-rank-mass-fraction 3/6 is at the **TOPOLOGY / K-homology layer** (it is the χ'_*-functor index on K_0(A_K)). These are non-fungible by the Kasparov boundary; the CM-1995 §III.4 residue formula's canonical χ'_weight at the Metric layer IS 5/14.

**Per the §VII.AF.1.OP-PROJ baseline's "ANNOTATION" at S91 W0 substrate-internal over-performance regime** (registry lines 14801-14811, in-session landing per W-6 CF-2 = T2.55, 2026-05-16): the Phi(L1)/Phi(L3) cross-link explicit makes clear that **Level 1 cohomology-class identity is at weight Φ(L1)=1 (substrate Σ_1 stratum / cosmological-term analog) and Level 3 empirical anchor is the methodology-floor F-image of substrate-IS structural identity at weight Φ(L3)=3 (Yang-Mills + Higgs quartic load-bearing analog)**. The CM-1995 §III.4 subleading expansion `Tr(γ · cocycle · [F, cocycle]² · |D|^{-2s}) = (residue at s=0) · L^{-3} · (1 + C_1·L^{-1} + ...)` (registry line 14807) IS the canonical Metric-layer evaluator with finite-L corrections C_1, C_2, ... — and at the L_max=10 Friedrich-Bär saturated regime, the leading residue (at s=0) IS algebraic-exact on the finite spectral triple, which Steps 2-4 above evaluate to 5/14.

**Faithful image of χ' is ℂ ⊕ ℍ at the Hilbert-space layer**.

Per S89 §W2-3 derived theorem (NPZ audit_sha256 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843; W3 WP §W3-4 lines 1060-1070), χ' kills M_3(ℂ) entire (Wedderburn 9 > 8 + Schur orthogonality), and the faithful image of χ' on A_K is the (ℂ ⊕ ℍ) sub-algebra. At the **Hilbert-space layer** — i.e., evaluated through the regular representation π_reg on H_K — the faithful image carries Hilbert-space-dim 1 + 4 = 5 (acting on H_χ' ⊂ H_K of dim 5). At the **K_0(A_K) layer** — i.e., evaluated through the K-theoretic Grothendieck functor — the faithful image carries K-class-rank 1 + 2 = 3 (Wedderburn-RANK survival). Both characterizations of the "faithful image" are correct AT DIFFERENT LAYERS; neither subsumes the other.

The CM-1995 §III.4 residue formula evaluates at the **Hilbert-space layer** (because `Tr` IS on H_K; `D_K^{-2z}` IS an operator on H_K; the residue at z=k IS a trace on H_K). At THIS layer, the faithful image's mass-fraction IS 5/14. This is the substrate-IS canonical χ'_weight at the CM-1995 §III.4 evaluator's natural layer.

**Conclusion**.

D1's structural claim: **the Connes-Moscovici 1995 §III.4 dimension-spectrum residue formula's substrate-IS canonical χ'_weight IS 5/14 = dim_HS(image)/dim_HS(A_K)**, at the Metric layer of the framework's four-layer hierarchy and at the Hilbert-space layer of the spectral triple's representational structure. This is canonical because (i) the CM-1995 §III.4 residue formula IS the W-5 baseline R_universal's bridge map; (ii) the residue formula's trace IS dim_HS-weighted by the regular representation's canonical construction; (iii) the χ'-restriction's mass-fraction at every pole of the dim spectrum IS pole-INDEPENDENT and equal to 5/14 (T1.9 verification at L_max=10 across 5 poles {0, 2, 4, 6, 8}, Step 2 above); (iv) the multiplicative decomposition α'_FULL = R_universal · (5/14) · (M_KK/M_Pl)² · g algebraically reproduces this canonical weight (Step 4 above).

Reading 1's 3/6 retains canonical status at the K_0(A_K) → K_0(target) Kasparov KK projection class index — a DIFFERENT NCG-axiomatic invariant at a DIFFERENT layer (Topology). The two readings are both substrate-IS and canonical, each at its own layer per the four-layer hierarchy; per the structural Phi correspondence at `epistemic-discipline.md §"Layer-Decomposition"`, they are non-fungible at the layer-functor F image axis.

#### D2: K-theoretic dim ratio as fourth candidate canonical (Kasparov KK-bridge framing)

**Claim**. A fourth substrate-IS candidate canonical for χ'_weight on A_K — the **target-side Hilbert-trace-dim ratio 5/8 = (dim_HS-image in target) / (dim_HS target)** — is structurally admissible at the Kasparov KK_0(A, B) bimodule layer. This is *not* the V3-rejected K-class-rank target ratio 3/4 (which counts target K-class-rank-USED, not Hilbert-trace-dim-USED) but a structurally distinct invariant at the dim-spec layer evaluated on the target Hilbert space.

**Substitution chain (Kasparov KK-bridge → target-side Hilbert-trace-dim ratio)**.

```
Step 1 (Definitions; Kasparov KK_0 bimodule structure).
  Kasparov KK_0(A_K, M_2(ℂ) ⊗ Cl(1)) bimodule for the χ' inheritance morphism
  carries a Hilbert C*-module structure E with right-action by the target
  algebra B = M_2(ℂ) ⊗ Cl(1) and a left-action by the source algebra A = A_K
  composed with χ': π_target = (·)⊗1, π_source = χ'(·).
  (Paper 01 (van-den-Dungen 2018) §2 "Unbounded Kasparov Modules"; abstract
  line 12: "We study the Kasparov product on (possibly non-compact and
  incomplete) Riemannian manifolds... we show on a submersion of Riemannian
  manifolds that the tensor sum of a regular vertically elliptic operator on
  the total space and an elliptic operator on the base space represents the
  Kasparov product of the corresponding classes in KK-theory.")

  Target B = M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ) (W3 WP §W3-4 lines 242-243).
  Target Hilbert-space dim:
      dim_HS(B) = dim_HS(M_2(ℂ)) + dim_HS(M_2(ℂ)) = 4 + 4 = 8
      (W3 WP §W3-4 line 956: "target complex Hilbert-space DIM = 4 + 4 = 8").
  Target K-class-rank:
      rank(K_0(B)) = rank(M_2(ℂ)) + rank(M_2(ℂ)) = 2 + 2 = 4
      (W3 WP §W3-4 line 247).

  Canonical χ' chosen in S89 §W2-3 NPZ "M3C_to_zero_C_and_H_to_canonical_M2C"
  (audit_sha256 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843):
    χ'([1_ℂ])      → rank-1 projector in one M_2(ℂ) summand: dim_HS-used = 1
    χ'([1_ℍ])      → identity-of-ℍ ⊗_ℝ ℂ ≅ M_2(ℂ) in the other M_2(ℂ) summand:
                     dim_HS-used = 4
    χ'([1_{M_3(ℂ)}]) → 0: dim_HS-used = 0
  Total χ'-image dim_HS in target:
    dim_HS(image χ' ⊂ B) = 1 + 4 + 0 = 5
    (consistent with source-side surviving dim_HS = 1 + 4 = 5 per faithfulness;
    the regular representation of ℂ ⊕ ℍ acts faithfully on its 5-dim
    Hilbert-space image inside the 8-dim target B's regular representation).

Step 2 (Target-side Hilbert-trace-dim ratio).
  χ'_weight^(target-dim) =  dim_HS(image χ' ⊂ B)  /  dim_HS(B)
                         =  5 / 8
                         =  0.625

  This is a substrate-IS Kasparov KK-bridge invariant: both numerator and
  denominator are pinned by S89 §W2-3 NPZ structure (faithfulness + target
  Hilbert-space dim); neither involves representational freedom or K_0
  functor invariance.

Step 3 (Distinction from V3-rejected target-side rank ratio).
  V3 lines 327-345 rejected target-side K-class-RANK ratio:
      χ'_weight^(target-rank) =  rank(image in K_0(B))  /  rank(K_0(B))
                              =  (1 + 2)  /  (2 + 2)
                              =  3 / 4
                              =  0.750
  on the structural argument that this counts target K-rank-class-USED, not
  source K-class-mass surviving, and therefore has no substrate-IS
  interpretation as "inheritance-restriction weight."

  V3's rejection is correct on its own terms (K-rank target ratio is not the
  inheritance-restriction weight). But the DIMENSION-version of the same target
  ratio is STRUCTURALLY DIFFERENT:
      χ'_weight^(target-dim) = 5/8 ≠ 3/4 = χ'_weight^(target-rank)
  because dim_HS counts the Hilbert-trace basis dimension used in the target,
  not the K-class-rank used. V3 did not consider the dim-version of the
  target-side ratio.

Step 4 (Bridge map interpretation).
  At the Kasparov KK_0 bimodule structure, the natural pairing between
  source-side cocycles and target-side states evaluates trace mass-fractions
  symmetrically on both sides. The W-5 baseline R_universal evaluates on the
  source side (H_K = regular representation of A_K acting on itself); the
  Connes-Karoubi pairing's bridge-map image lives on the source-side dim 14.
  But a structurally analogous evaluation on the TARGET side would compute the
  Hilbert-trace mass-fraction in B's regular representation — dim 8.

  The 5/8 candidate IS the analog of Reading 2's 5/14 evaluated on the target
  side of the Kasparov KK bridge. The 5/14 reading is source-side
  (CM-1995 §III.4 residue trace on H_K); the 5/8 reading is target-side
  (analogous residue trace on H_B if one constructs the bridge map's
  target-side companion).

Step 5 (Empirical evaluation at the LRD α-anchor).
  Substituting χ'_weight = 5/8 into the multiplicative decomposition at
  L_max=10 saturation (g = 1):

      α'_target-dim(M_LRD)  =  1.030902 · (5/8) · 9.307286e-04 · 1.000
                            =  5.997074e-04

  rel_dev = |5.997074e-04 − 2.183406e-03| / 2.183406e-03 = 0.7253

  Sub-clause A PASS (0 < α' < 1); Sub-clause B FAIL (rel_dev 0.7253 > 0.30);
  composite FAIL. The 5/8 candidate ALSO FAILs the empirical anchor — but
  closer to PASS than CF-37 (0.78), T1.8 (0.82), or T1.9 (0.84).

Step 6 (Substrate-IS direction at the Kasparov KK-bridge layer).
  Both Reading 2 (5/14 source-side) and Candidate 4 (5/8 target-side) are
  substrate-IS Hilbert-trace mass-fractions on the SAME Kasparov KK bimodule.
  They count the same kind of structural quantity (Hilbert-trace-dim-mass-
  fraction at the bridge map's trace evaluator) on opposite sides of the
  bridge. The Kasparov-product factorization at Paper 01 (1811.07824)
  symmetrizes source and target naturally — the canonical evaluation can be
  made on either side modulo the choice of bridge-map orientation.
```

**Why 5/8 IS structurally distinct from V3's rejected 3/4**.

Volovik's V3 line 327-345 rejected the target-side K-class-rank ratio 3/4 on the structural argument that K-rank "counts target REPRESENTATIONAL ROOM USED, not source K-class-mass surviving". This rejection is correct on its own terms. But it is specifically about the K-class-rank invariant on the target side, NOT about the Hilbert-trace-dim invariant on the target side.

The structural difference:

| Invariant | Computation | Value | Substrate-IS? |
|:----------|:------------|:------|:--------------|
| Target K-class-rank ratio | (1 + 2) / (2 + 2) | 3/4 = 0.750 | YES (target K-class-rank-used) — but V3 correctly notes this is target representational-room K-rank-USED, not source K-class-mass SURVIVING |
| Target Hilbert-trace-dim ratio | (1 + 4 + 0) / (4 + 4) | 5/8 = 0.625 | YES (target Hilbert-trace-dim-used) — D2 NEW: this is target representational-room Hilbert-trace-dim-USED |

Both target-side ratios are substrate-IS invariants of χ' at the target side of the Kasparov KK bimodule. V3's argument against the K-rank version (3/4) carries over against the dim version (5/8) on the same grounds — IF the question is "what is the source K-class-mass surviving χ'?", then target-side ratios are categorically wrong. The question becomes: is there a Kasparov KK-bridge formulation of the χ'_weight in α'(M_LRD) that evaluates on the target side rather than the source side?

**My honest answer**: 5/8 is structurally admissible as a substrate-IS Kasparov KK-bridge invariant of χ', but **NOT as the χ'_weight in α'(M_LRD)** at the CM-1995 §III.4 residue formula evaluator. The reason: α'(M_LRD)'s evaluator IS the source-side residue trace on H_K (per the §VII.AF.1.OP-PROJ baseline + T1.9 substitution chain), not the target-side residue trace on B. The 5/8 candidate would be the canonical χ'_weight if the bridge map evaluated on H_B instead of H_K — but it does not (per the framework's W-5 baseline pinning).

So D2's structural position: the 5/8 candidate IS substrate-IS, IS admissible at the Kasparov KK_0 bimodule layer, but IS NOT the canonical χ'_weight for α'(M_LRD) at the current framework's evaluator pinning. The 3/6 candidate IS the K_0-rank-functor invariant; the 5/14 candidate IS the source-side residue-trace invariant; the 5/8 candidate IS the target-side residue-trace invariant; the 0.404 candidate IS the (c)-corridor γ(s)-modulated form. **All four are substrate-IS; ONLY 5/14 IS the canonical multiplicative pre-factor IN α'(M_LRD)** under the framework's pinned CM-1995 §III.4 evaluator on H_K.

**Admissibility under K=3 MANDATORY orthogonality clause**.

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close, 2026-04-30), the corner-cell classification of the 5/8 candidate:

- Parse-tree expansion: χ'_weight^(target-dim) = (1 + 4 + 0) / (4 + 4) = pure spectrum-only operations on target Hilbert-space-dim arithmetic; no π(a) operator-algebra references.
- Mellin pole: same substrate-distance-1 pole s=3 as Readings 1, 2, 3 (the bridge map's pole structure is fixed by the substrate-IS Hochschild cocycle space, not by source-vs-target side).
- **Corner classification: Cell I (algebra-INVARIANT × s=3)** by parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`.

The 5/8 candidate joins Readings 1, 2, 3 in Cell I × s=3. The K=3 MANDATORY clause's conditions 1-4 (`cross-pillar-bridge-anatomy.md` corner-cell declaration + cross-corner co-primary FORBIDDEN + cross-pole co-primary FORBIDDEN + cross-corner cross-pole magnitude comparisons FORBIDDEN) are satisfied identically. The 5/8 candidate does NOT violate the K-counter; it is structurally admissible at the within-cell layer.

But the within-cell substrate-priority axes (α)+(β)+(γ)+(δ) from Re:V4 do discriminate against 5/8:

- Axis (α): 5/8 is on the Hilbert-trace-dim axis (NOT K-class-rank) but on the target side — partially aligns with Reading 2 at the dim-axis but mis-aligns at source-vs-target.
- Axis (β): 5/8 IS target-side — V4's axis (β) DOWNGRADES it relative to Readings 1 (source-side K-rank) and 2 (source-side trace-dim).
- Axis (γ): 5/8 inhabits the primary (b)∘(d) corridor — silent on this axis.
- Axis (δ): 5/8 is target-side evaluator-layer — α'(M_LRD)'s CM-1995 §III.4 evaluator IS source-side on H_K, NOT target-side; axis (δ) DOWNGRADES 5/8 relative to Reading 2 (5/14 source-side trace-mass).

Net: 5/8 is registry-admissible as a fourth substrate-IS Kasparov KK-bridge invariant of χ' but is NOT a primary canonical candidate for α'(M_LRD)'s χ'_weight under the framework's pinned source-side CM-1995 §III.4 evaluator. It would be the canonical candidate IF the framework's evaluator were target-side.

**Co-primary structure with Reading 2 (5/14)?**

Reading 2 (5/14 source-side) and Candidate 4 (5/8 target-side) are both Hilbert-trace-dim-mass-fraction invariants of χ' at the Kasparov KK_0 bimodule layer; they count the same KIND of trace mass on opposite sides of the bridge. Per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` Detection clauses 1-4:

1. **Sequential derivation**: 5/8 cannot be invoked without first invoking 5/14's evaluation structure (the target-side dim ratio inherits from the source-side trace structure at the Kasparov KK_0 bimodule). NOT sequential — they are PARALLEL evaluations on opposite sides of the bimodule.

2. **Non-fungible anchors**: cannot swap order (no order). Fungibility check: 5/14 and 5/8 are NOT equivalent (5/14 = 0.357 ≠ 0.625 = 5/8) and not fungible.

3. **Both remain accessible**: yes — both are substrate-IS Kasparov KK-bridge invariants.

4. **Same algebra-axis cell**: both Cell I × s=3.

The structure is NOT SOURCE-DOUBLE-CITE-CO-PRIMARY (no sequential dependence). The correct structure is **PARALLEL-COMPANION** at the Kasparov KK_0 bimodule's source/target axis. Per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 (S88 W8-92, 2026-05-05), the parallel-companion structure at the same algebra-axis with structurally-orthogonal evaluation conventions is canonical when both readings are independently registry-eligible.

If S92 registry landing under outcome (ii) SIMULTANEOUS-VALIDITY accepts the K_0-layer + Metric-layer two-slot structure (Re:V5), then a THIRD potential companion slot at the Kasparov-KK-bimodule target-side could be allocated for Candidate 4. But this third slot would be NON-CANONICAL for α'(M_LRD) under the framework's pinned source-side evaluator — it would be a documentation slot for the Kasparov KK-bridge's target-side structural completeness, NOT a competing candidate for α'(M_LRD)'s χ'_weight.

**My recommendation for D2 (under outcome (ii) SIMULTANEOUS-VALIDITY)**.

Land TWO §VII slots at S92 W1 per Re:V5's recommendation (K_0-layer + Metric-layer), AND record Candidate 4 (5/8 target-side) as a **calibration-corpus entry, not a registry §VII slot**, under the Phi-correspondence layer-decomposition K-counter advancement queue. Specifically: 5/8 IS a substrate-IS Kasparov KK-bridge invariant of χ', and it should be documented in the framework's permanent registry record as a structural fact about χ', but it is NOT a competing canonical for α'(M_LRD). The Phi-correspondence layer-decomposition reading frames the structure transparently:

- **Topology layer** (K-homology / K_0(A_K) functor): canonical χ'-invariant = 3/6 = K_0-rank-mass-fraction (Reading 1; sub-source-side / target-side distinction is absorbed by K_0 functoriality)
- **Metric layer** (CM-1995 §III.4 residue trace on H_K): canonical χ'-invariant in α'(M_LRD) = 5/14 = source-side Hilbert-trace-dim-mass-fraction (Reading 2)
- **Kasparov KK_0 bimodule target-side trace layer** (analogous residue trace on H_B): structural χ'-invariant = 5/8 = target-side Hilbert-trace-dim-mass-fraction (Candidate 4; NOT in α'(M_LRD))
- **(c)-corridor modulation** (γ(s) ≠ Γ(s) shift on the universal kernel): canonical pre-factor at (c)-corridor = Reading 2 × (1 − γ_Euler/3) ≈ 0.288 (under outcome (ii) Metric layer); OR Reading 1 × (1 − γ_Euler/3) ≈ 0.404 (under outcome (i) K_0 layer; T1.8 audit_sha256 8ab158e9e45aab37...)

Under outcome (ii) SIMULTANEOUS-VALIDITY, the registry landing structure is:

```
§VII.{X}.OP-PROJ-K0-LAYER       — Reading 1 (3/6) canonical at K_0(A_K) functor layer
§VII.{X+1}.OP-PROJ-METRIC-LAYER  — Reading 2 (5/14) canonical at CM-1995 §III.4 residue layer
                                    [the canonical χ'_weight in α'(M_LRD)]
calibration corpus annotation     — Candidate 4 (5/8) target-side Hilbert-trace-dim
                                    structural Kasparov KK_0 bimodule invariant; NOT in α'(M_LRD)
calibration corpus annotation     — Reading 3a (0.404) / Reading 3b (0.288): (c)-corridor digamma-
                                    modulated forms of Reading 1 / Reading 2 respectively
```

This structure honors the framework's K=3 MANDATORY orthogonality (all within Cell I × s=3, no cross-corner violation), the Reading-A operator-projection naming hygiene MANDATORY K=3 (suffix-tags per OP-PROJ requirement), the SOURCE-DOUBLE-CITE-CO-PRIMARY structure (Reading 1 + Reading 2 each at their own layer with independent SOURCE-DOUBLE-CITE-CO-PRIMARY anchors per Re:V5), and the Phi-correspondence layer-decomposition advisory K-counter (K=1 calibration instance at landing).

#### D3: Questions for volovik — Wedderburn-RANK vs HS-DIM at the Chern-character pairing

Five Round 2 questions for Volovik, sharpening the disagreement at the four spawn-prompt foci (Chern-character pairing layer / Kasparov KK-bridge map structure / CM-1995 §III.4 dim-spec residue evaluation / L_max → ∞ asymptotic behavior).

**Q-VLV-1 (Chern-character pairing layer — does Wedderburn-RANK or HS-DIM appear?)**.

The Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula gives the **Chern character pairing** as

```
ch_k(P)  =  Res_{z=k} [ Tr_{H_K}( P  ·  D_K^{-2z} ) ]
```

at each pole k ∈ dim_spec((A_K, H_K, D_K)|_{L_max=10}) = {0, 2, 4, 6, 8} (W3 WP §W3-4 dim-spec residue table lines 1024-1032; SU(3) d=8 spectral triple). The trace `Tr_{H_K}` IS over the regular representation of A_K on H_K, where dim_HS{ℂ, ℍ, M_3(ℂ)} = {1, 4, 9} are the canonical Hilbert-trace basis dimensions per summand acting on itself. T1.9 verifies that the χ'-restricted residue value at every pole equals exactly 5/14 of the un-restricted residue value at the same pole (Re:V1 / D1 Step 2; pole-INDEPENDENT identity verified across all 5 poles).

Concretely at substrate-distance-1 pole k=6: un-restricted residue = 8.673943e+03; χ'-restricted Chern char component = 3.097837e+03; ratio = 3.097837e+03 / 8.673943e+03 = 0.357142857... = 5/14 Sage-rational. The K-class-rank-mass-fraction 3/6 does NOT appear in this residue evaluation at ANY pole — it is not a pole residue, it is a K_0(A_K) → K_0(target) functor invariant of χ' on Grothendieck classes.

**Question to Volovik**: At the Chern-character pairing layer (CM-1995 §III.4 residue formula on the substrate's spectral triple), the substrate-IS canonical χ'-restricted-to-unrestricted ratio at each dim-spec pole IS 5/14 by direct algebraic substitution (T1.9 Sage-rational; pole-INDEPENDENT). The K-class-rank ratio 3/6 does NOT appear as a residue at any dim-spec pole; it appears at the K_0 functor invariant layer (which is a DIFFERENT layer of the four-layer hierarchy). **Do you concur that the Chern-character pairing residue evaluation prescribes 5/14 at every pole, and that 3/6 IS a K_0 functor invariant at a different layer?** If you contest the pole-independence of 5/14 across {0, 2, 4, 6, 8} — i.e., if you claim 3/6 appears at some pole where 5/14 does not appear — please cite the specific pole and the Sage-rational evaluation that demonstrates 3/6 ≠ 5/14 at that pole.

**Q-VLV-2 (Kasparov KK-bridge inheritance morphism — what does χ_* preserve?)**.

The Kasparov KK-bridge map for χ' : A_K → M_2(ℂ) ⊗ Cl(1) factors through TWO complementary categorical functors:

(F1) K_0 functoriality: χ'_* : K_0(A_K) → K_0(M_2(ℂ) ⊗ Cl(1)) preserves Grothendieck classes; K-class-rank-mass-fraction surviving = 3/6.

(F2) Hilbert-trace pullback: π_χ' : Tr_{H_K} → Tr_{H_χ'} on the Hilbert-trace structure; trace-mass-fraction surviving = 5/14.

These two functorial properties of χ' are NON-FUNGIBLE per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 + my agent MEMORY.md canonical boundary "Kasparov product gives TOPOLOGY (K-homology class, indices, factorization). NOT ANALYSIS (spectral moments)." (S82-Kasparov-abelian-proof bundle, K-track PASS SHA `61d732378be18b955655eba91448a1800eb3dcb75e94b64fd8673aa142fe1fb7`).

**Question to Volovik**: Per the K-track / spectral-moment categorical boundary in my agent memory, K_0 functoriality (F1) operates at the TOPOLOGY layer and Hilbert-trace pullback (F2) operates at the ANALYSIS / Metric layer. **Do you read this boundary as forbidding the identification "K-class-rank-mass-fraction IS the χ'_weight in α'(M_LRD)"?** Specifically: α'(M_LRD) is a Metric-layer observable (regulator-dependent residue trace, a_k coefficient family); the K-class-rank invariant 3/6 lives at the Topology layer; the boundary should prevent the K-class-rank invariant from entering the Metric-layer multiplicative decomposition. If you contest the boundary's reach — i.e., if you claim K_0 functoriality (F1) extends naturally to determine Metric-layer multiplicative pre-factors — please cite the structural theorem that bridges Topology and Metric layers without going through the layer-functor F of `epistemic-discipline.md §"Layer-Decomposition"`.

**Q-VLV-3 (CM-1995 §III.4 dim-spec residue evaluation — where does Reading 1 vs Reading 2 diverge?)**.

T1.9 Step 5 (`session-91-w3-workingpaper.md` line 983) evaluates the FULL CM-1995 §III.4 residue formula at L_max=10 saturation:

```
α'_FULL(M_LRD)  =  R_universal · χ'_weight · (M_KK / M_Pl)² · g(M, L=10)
                =  1.030902 · (5/14) · 9.307286e-04 · 1.000
                =  3.426750e-04                  [T1.9 audit_sha256 752a8f2b862a9aa5...]
```

If we substitute Reading 1's χ'_weight = 3/6 = 0.5 instead, the multiplicative decomposition gives α'_CF37(M_LRD) = 1.030902 · 0.5 · 9.307286e-04 · 1.000 = 4.797450e-04 (CF-37 structural-ansatz value at `session-90-w4-workingpaper.md` §W4-1; audit_sha256 10ee072fe2c193f3...). The difference α'_FULL / α'_CF37 = 3.426750e-04 / 4.797450e-04 = 5/7 ≈ 0.714286 (Sage-rational; W3 WP §W3-4 line 1010 "factor_vs_CF37 = 0.714286 = 5/7").

Reading 1 and Reading 2 diverge at the **identification of the multiplicative pre-factor in the dim-spec residue evaluation**: 3/6 (K-rank-mass) vs 5/14 (Hilbert-trace-mass). At the FULL CM-1995 §III.4 algebraic evaluation, the pre-factor IS the Hilbert-trace-mass-fraction by direct substitution (verified pole-by-pole at the dim-spec residue table). The 3/6 value does not appear in the algebraic substitution chain (T1.9 Steps 2-5 lines 962-984); it appears only in CF-37's structural-ansatz (S90 W4 phonon-first cosmologist's pre-T1.9 derivation), which substituted a K-class-rank-fraction WHERE the algebraic evaluator prescribes a Hilbert-trace-fraction.

**Question to Volovik**: The CF-37 structural-ansatz at S90 W4 was a substitution of K-class-rank-mass-fraction INTO the multiplicative decomposition position where the FULL CM-1995 §III.4 residue formula prescribes Hilbert-trace-mass-fraction. T1.9 IS the FULL algebraic evaluation that replaces the structural-ansatz with the residue formula's intrinsic pre-factor. **Do you read CF-37's 3/6 as a structural-ansatz to be SUPERSEDED by T1.9's 5/14 once the FULL residue evaluation is performed, OR do you read CF-37's 3/6 as a STRUCTURAL THEOREM at a different layer (K_0 functor invariant) that holds INDEPENDENTLY of T1.9's 5/14 at the Metric layer?** I read it as the latter (which routes to outcome (ii) SIMULTANEOUS-VALIDITY). If you read it as the former (3/6 IS the same observable T1.9 evaluates differently), please cite the structural theorem that identifies K-rank-mass-fraction with Hilbert-trace-mass-fraction at the CM-1995 §III.4 residue evaluator.

**Q-VLV-4 (L_max → ∞ asymptotic behavior of both readings)**.

The W-5 baseline R_universal_HP1_strict_F4 = 1.030902 IS the HKR `L_max → ∞` image of the substrate-IS Hochschild pairing (`permanent-results-registry.md §VII.AF.1.OP-PROJ` line 14817-14819 verbatim theorem text: "Pillar III HP^1 cohomology norm factorizes as `‖[ε_H]‖_{HP^1, r} = |f_4^r| · R_universal`, where `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` is the regulator-invariant Connes-Karoubi pairing on the Jensen-deformed band-0 projector (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula)"). The Level-2 algebraic envelope is L^{-3} at d=4 (registry line 14826), and the Level-3 empirical anchor at L_max=10 is 0.0095% F_4 strict (10× margin inside envelope per registry line 14803-14807 substrate-internal over-performance regime annotation).

T1.9 (`session-91-w3-workingpaper.md` §W3-4 envelope fit lines 1046-1056) reports envelope_n ≈ −1.22e-20 ≈ 0 and R² = 0.0000 for the α'_FULL(M) M-scan at L_max=10. The same flat behavior is reported for CF-37 (S90 W4 §W4-1) and T1.8 (`session-91-w3-workingpaper.md` §W3-3 lines 666-670). All three readings are M-INDEPENDENT in the M-scan range at L_max=10 saturation — the Λ(M)/M_KK ≫ |λ|_max(L=10) saturation regime makes the inheritance-restricted projector g(M, L=10) = 1.000 at all M ∈ {10⁵, ..., 10⁹} M_sun.

**Question to Volovik**: At the L_max → ∞ asymptotic limit (HKR image), the W-5 baseline R_universal_HP1_strict_F4 IS the bridge-map limit value (regulator-class invariant per Level-1 cohomology-class identity). The χ'_weight at this limit IS the pre-factor that the χ'-restriction contributes to the bridge-map image. **At L_max → ∞, does the χ'_weight take the value 3/6 (K-class-rank invariant, L_max-INDEPENDENT BY CONSTRUCTION) or 5/14 (Hilbert-trace-mass-fraction, ALSO L_max-INDEPENDENT BY CONSTRUCTION because T1.9 verifies pole-by-pole the 5/14 ratio is exact at every pole of the dim spectrum, NOT a finite-L approximation)?**

Both readings are L_max-INDEPENDENT at the finite spectral triple (A_K, H_K, D_K)|_{L_max=10} per their substitution-chain structures (K-class-rank arithmetic for Reading 1; pole-by-pole 5/14 ratio for Reading 2 verified at all 5 poles of the dim spectrum). Both readings extend to L_max → ∞ trivially (the substitution chains do not involve L_max truncation residuals). The L_max → ∞ asymptotic limit does NOT discriminate Reading 1 from Reading 2 — both are L_max-INDEPENDENT structural identities. If you accept this co-validity at L_max → ∞, then outcome (i) single-canonical at L_max → ∞ is structurally underdetermined; outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level becomes the natural reading. **If you contest the L_max-independence of Reading 2 — i.e., if you claim Reading 2's 5/14 has a finite-L correction that vanishes at L_max → ∞ leaving only 3/6 as the asymptotic canonical — please cite the finite-L correction structure that would route 5/14 → 3/6 in the limit.** I have not been able to identify any such correction in the CM-1995 §III.4 residue formula's algebraic substitution chain.

**Q-VLV-5 (registry-landing shape — does outcome (ii) accommodate your V5 framework?)**.

My Re:V5 proposes outcome (ii) SIMULTANEOUS-VALIDITY at the layer-decomposition level, with TWO STRUCTURAL-ORTHOGONAL-COMPANION §VII slots at S92 W1 (K_0-layer + Metric-layer), both SHARED-ANCHOR-COMPANION with §VII.AF.1.OP-PROJ baseline, Stage-2 cross-axis verify dispatched to connes-ncg + mack-cosmic-bridge (HARD-exclude volovik + vdd per joint-theorem-promotion downstream-inheritance reach), JOINT clauses extended to JOINT-K0 + JOINT-Metric. The §VII.AF.1.OP-PROJ baseline retains its no-delta status; §VII.AU.OP-PROJ FWD-C1 retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; CF-37 / T1.8 / T1.9 verdict lines retain absolute permanence at FAIL.

Your V5 framework (single-canonical outcome (i) Reading 1, single §VII slot at S92 W1, SHARED-ANCHOR-COMPANION K-counter stays at K=1) is structurally well-formed AT THE K_0 LAYER ALONE. My outcome (ii) extends V5's framework by adding the Metric-layer companion slot for Reading 2; the K_0-layer slot retains exactly V5's pre-registered structure. Outcome (ii) does NOT discard V5's framework; it ADDS the Metric-layer companion to it.

**Question to Volovik**: **Does the addition of a Metric-layer companion slot for Reading 2 (5/14) at §VII.{X+1}.OP-PROJ-METRIC-LAYER, parallel-companion to your V5-pre-registered K_0-layer slot for Reading 1 (3/6) at §VII.{X}.OP-PROJ-K0-LAYER, preserve or violate any structural commitment in your V5 pre-registration?** Specifically: (i) Does it preserve the §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ no-delta status? — I believe yes; (ii) Does it preserve Stage-2 cross-axis verify HARD-exclude on volovik + vdd? — yes; (iii) Does the Hybrid Independence Test K-counter stay at K=1 under outcome (ii)? — yes (both slots are SHARED-ANCHOR-COMPANION with §VII.AF.1.OP-PROJ baseline; neither advances the K-counter); (iv) Does the Phi-correspondence layer-decomposition advisory K-counter advance to K=1 with the two-slot landing as calibration corpus instance #1? — I believe yes (forward calibration corpus expansion).

If you DISAGREE with outcome (ii) on any of (i)-(iv), please cite the structural commitment in your V5 framework that outcome (ii) violates. If you AGREE on (i)-(iii) but DISPUTE the Phi-correspondence K-counter advancement (iv) — e.g., on the grounds that the K_0-layer + Metric-layer split is NOT a calibration instance of `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence — please cite the structural distinction that prevents this two-layer simultaneous canonical landing from being a Phi-correspondence calibration instance.

---

**Closing meta-question for Volovik on R2 routing**:

If outcome (ii) is the workshop verdict, the registry shape is two §VII slots + Phi-correspondence K-counter advisory advancement; if outcome (i) is the verdict, the registry shape is V5's single slot. The R2 round must converge on ONE outcome (or escalate to R3 if R1 + R2 produce genuine ledger-dissonance per `Investigating-Workshops.md §"Honest count discipline"`). I propose: if your R2 response accepts outcome (ii) framework on (Q-VLV-5) items (i)-(iii) AND accepts the Phi-correspondence K-counter advancement (iv) as advisory-K=1 (not MANDATORY-K=3), we converge on outcome (ii). If your R2 response rejects (i)-(iv) on any grounds, we escalate to R3 with a 3-round verdict.

I do not intend the workshop to drag — the substrate-physics adjudication is genuinely at the layer-decomposition / Phi-correspondence axis, and the framework's existing structural infrastructure (`epistemic-discipline.md §"Layer-Decomposition"` + `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` + `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`) supports outcome (ii) by construction without requiring new methodology-rule extensions. My honest reading is that outcome (ii) IS the structurally natural verdict on this corpus; outcome (i) would over-collapse the two-layer canonical structure into a single representative that misrepresents the substrate's intrinsic multi-layer information content.

---

## Round 2 — Volovik: Follow-up

### CONVERGENCE

Reading van-den-dungen's R1 cross-synthesis carefully (Re:V1 through Re:V5 plus D1, D2, D3), I find the structural exchange has produced genuine substrate-physics convergence on multiple non-trivial points. I record the convergence here explicitly so the Round 2 ledger separates what has been *settled* from what remains *contested*.

**C-1. K-class-rank invariant 3/6 at the K_0(A_K) functor layer is uncontested**.

vdd's Re:V1 §"AGREE (partial — what holds at the K-theoretic class layer)" (workshop document line 607-609) concedes — explicitly and arithmetically — that:
- the Wedderburn-Artin decomposition `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` IS the substrate's intrinsic *-algebra structure with primitive-idempotent counts (1, 2, 3);
- `K_0(A_K) ≅ ℤ ⊕ ℤ ⊕ ℤ` with generators at K-class-rank weights (1, 2, 3);
- `χ'_*` kills the `M_3(ℂ)` generator and faithfully embeds the `ℂ` and `ℍ` generators per the S89 §W2-3 Step 7 NPZ structure (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`);
- the K-class-rank-mass-fraction `(rank ℂ + rank ℍ) / rank(A_K) = 3/6` is arithmetically correct as a K_0-functor invariant of `χ'`.

This is not a small concession. vdd is granting the *substance* of V1's K-theoretic derivation. The disagreement is no longer about whether 3/6 is a substrate-IS K-theoretic invariant of `χ'` — it IS, and we both agree on that — but about which observable in the multiplicative decomposition of `α'(M_LRD)` it controls. **The K_0-rank survival of `χ'` is settled at 3/6.**

**C-2. Corridor orthogonality and the c_aux structural derivation are settled**.

vdd's Re:V2 §"AGREE (corridor-orthogonality, factorization-layer separation)" (line 660-664) concurs with V2's three key structural arguments:
- `γ(s) = Γ(s) · (1 + c_aux · (s − s_*)^{-1})` carries a new simple pole at `s = s_* = 1` that `Γ(s)` does not, with Laurent expansion analysis correct;
- `c_aux = 1/3` is FIXED by substrate algebra rank arithmetic `(1 − 2 + 3)/6` per the sign-alternating Wedderburn rank sum;
- (b) χ'-pullback and (c) γ(s) ≠ Γ(s) are orthogonal element-1 deformation columns; the Kasparov-product factorization principle (Paper 01 unbounded KK theorem) makes the two columns factor at distinct layers.

vdd also concurs (Re:V2 line 664-665) that Reading 3's `(1 − γ_Euler/3) ≈ 0.808` factor is NOT an `L_max → ∞` asymptotic correction to Reading 1 — both are L_max-INDEPENDENT at the finite spectral triple. The digamma factor lives at the kernel-choice layer, not the L_max truncation layer. **The (c)-corridor's structural distinctness from the (b)-corridor is settled.**

vdd's Re:V2 §"Reinforce, strongly" (line 707-711) goes further and accepts the irrational-substrate-IS classification of `(1 − γ_Euler/3)` per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` `structurally-IRRATIONAL-per-CC2-analog` tag — and adopts SIMULTANEOUS-VALIDITY at the (b)/(c) corridor-decomposition level as a defensible reading. **(b)/(c) corridor-level SIMULTANEOUS-VALIDITY is settled.**

The remaining canonical-weight contest is intra-(b)-corridor (3/6 vs 5/14) — NOT (b) vs (c). I accept this scope narrowing.

**C-3. S89 §W2-3 faithful-image identification is uncontested**.

vdd's Re:V3 §"AGREE (S89 §W2-3 derived theorem; faithful image identification)" (line 715-723) concurs with the 8-step Wedderburn 9 > 8 + Schur orthogonality argument, the machine-epsilon witness `chi_prime_pullback_machine_eps_PASS = True`, and the K-class-rank-mass-fraction arithmetic. **The structural fact that `χ'` kills `M_3(ℂ)` and the faithful image is `ℂ ⊕ ℍ` is settled.** The disagreement now lives entirely at the question of *which weight invariant on this faithful image enters `α'(M_LRD)`*, not at the faithfulness fact itself.

**C-4. K-counter MANDATORY-K=3 silence within Cell I × s=3 is uncontested**.

vdd's Re:V4 §"AGREE (corner classification; K-counter silence on within-cell weight choice)" (line 810-820) concurs fully with V4's corner-classification analysis: all three readings (and Candidate 4) parse to Cell I × s=3 via the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`; the K=3 MANDATORY clause's enforcement at conditions 1-4 is satisfied identically by all readings; the K-counter is structurally orthogonal to the within-cell canonical-weight question. **The K=3 MANDATORY orthogonality clause neither selects nor excludes any of the three (or four) readings.**

**C-5. CF-37 / T1.8 / T1.9 verdict permanence at FAIL is uncontested**.

vdd's Re:V5 line 920-921 concurs with V5 lines 585-586: all three verdict lines (audit_sha256 `10ee072fe2c193f3...`, `8ab158e9e45aab37...`, `752a8f2b862a9aa5...`) retain their FAIL composite verdicts at the empirical 1/458 anchor unchanged. The canonical-weight verdict at S92 does NOT contradict the empirical FAILs; no `supersedes=` tag is required per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`. **Absolute permanence at FAIL is settled across all three verdict lines.**

**C-6. §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ no-delta is uncontested**.

vdd's Re:V5 items 2 + 3 (lines 915-917) concurs with V5 lines 468 + 470: the unrestricted W-5 baseline `R_universal_HP1_strict_F4 = 1.030902` does NOT consume any χ'_weight factor in its anatomy; no corrigendum required under either Reading 1 OR Reading 2 canonical. §VII.AU.OP-PROJ FWD-C1 retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; the χ'_weight canonicalization is structurally orthogonal to FWD-C1's parameterized slope_A first-extraction. **No-delta on both existing §VII slots is settled.**

**C-7. Stage-2 HARD-exclude on volovik + vdd; connes + mack as Axis-A + Axis-B**.

vdd's Re:V5 item 4 (line 919) concurs with V5 lines 502-514: HARD-exclusion of volovik (V1-V5 author) and vdd (T1.8 Axis-B author + T1.9 Axis-A author + Round 1 cross-synthesis author) per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` (S88 W-14 W4a-17 V.2 MANDATORY at K=1 downstream-inheritance reach extension). Recommended Axis-A = `connes-ncg-theorist` (NCG-axiomatic depth on Kasparov-KK projections); Axis-B = `mack-cosmic-bridge` (§VII registry sole-writer per `feedback_mack-bridge-role.md`). **Stage-2 reviewer-selection protocol is settled.**

**C-8. Settlement at SIMULTANEOUS-VALIDITY framing (with re-scoped axis)**.

This is the substantive position shift. Reading vdd's Re:V1 §"EMERGES" (line 635-646) carefully: the K_0-rank invariant 3/6 and the trace-mass invariant 5/14 are explicitly framed as "non-fungible χ'-invariants on a single Kasparov KK projection" — they are simultaneously substrate-IS, simultaneously canonical on their respective invariant axes, but they answer different structural questions about `χ'`. vdd's Re:V3 §"EMERGES" (line 760-777) tabulates four distinct substrate-IS K-theoretic / trace invariants of the single `χ'` (Source K-rank 3/6; Source dim-trace 5/14; Target K-rank 3/4 V3-rejected; Target dim-trace 5/8 D2-new).

**I now accept the SIMULTANEOUS-VALIDITY framework at the *invariant-class* level — 3/6 IS a substrate-IS K-theoretic invariant of `χ'`; 5/14 IS a substrate-IS Hilbert-trace invariant of `χ'`; the two count different categorical things on the same Kasparov KK projection.** This is C-8 convergence.

What I do NOT yet accept (and where DISSENT lives) is vdd's claim that the SIMULTANEOUS-VALIDITY at invariant-class level *cleanly resolves the canonical-weight question for `α'(M_LRD)` via Layer-Decomposition F*. The structural distinction "5/14 is the invariant the residue formula computes; 3/6 is the K_0 functor invariant" is a settled fact about WHICH invariants `χ'` carries. The question of which invariant IS the multiplicative pre-factor of `R_universal` in the decomposition `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g` is downstream of this — and the SIMULTANEOUS-VALIDITY framing answers a different question (what invariants does `χ'` carry?) than the canonical-weight question (which invariant enters `α'(M_LRD)`?).

This is the boundary between CONVERGENCE C-8 and DISSENT D-1 below.

### DISSENT

I dissent on three specific structural points where vdd's R1 argument either over-extends the SIMULTANEOUS-VALIDITY framing beyond what its premises support, mis-applies the layer-functor F from `epistemic-discipline.md §"Layer-Decomposition"`, or proposes a registry-landing structure that fails `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4 same-algebra-axis-cell requirement when read carefully.

**D-1. Layer-Decomposition F is being misapplied — the rule's F is *cross-stratum* (substrate ↔ methodology ↔ audit), NOT *intra-substrate* (K_0 ↔ Metric within the substrate)**.

vdd's Re:V1 §"(V1-Q-VDD-2)" answer (line 652-656) invokes "the four-layer hierarchy of my permanent agent memory" (Topology / Representation / Metric / Functional) and routes the χ'_weight adjudication into a "K-homology layer (3/6) vs Metric layer (5/14)" split. Re:V3 §"EMERGES" (line 758-777) and Re:V4 §"MISSED (axis (δ): evaluator-trace-layer vs K_0-rank-layer axis)" (line 854-862) build the SIMULTANEOUS-VALIDITY argument on this Topology/Metric layer-split, citing `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence as the structural authority (Re:V4 line 858: "axis (δ) is the structural realization of `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence at the substrate-physics-observable layer").

**This citation does not survive a careful read of the rule**. `epistemic-discipline.md §"Layer-Decomposition"` lines 307-345 (which I have re-read in full while drafting this response) defines `F: substrate → methodology → audit` as a *cross-stratum* layer-functor between THREE strata: substrate-physics, methodology-floor (rule files), audit-floor (verdict files). The two tables `§"F at substrate ↔ methodology pair"` (lines 311-319) and `§"F at methodology ↔ audit pair"` (lines 321-329) enumerate cross-stratum mappings: `eigenvalue → rule-file content`; `numerical PASS predicate → artifact-existence predicate`; `machinery pin → input-pin map`; `verdict-line numerical value → verdict-line artifact-SHA`. None of these is intra-substrate; they are all substrate-to-methodology or methodology-to-audit.

The Phi correspondence at lines 335-343 maps `weight(a_n^SD) = n` (substrate-physics Seeley-DeWitt coefficient weight) to `weight(Σ_d) = enforcement-strength` (methodology-rule severity). Both sides of Phi are at *different strata* (substrate vs methodology). The Phi correspondence does NOT define an intra-substrate Topology/Metric stratification.

vdd's "four-layer hierarchy" (Topology / Representation / Metric / Functional) is from vdd's *agent memory* (Re:V1 line 654: "the four-layer hierarchy of my MEMORY.md") — it is NOT in the framework's permanent rule structure. The agent-memory hierarchy may be a useful organizing principle for vdd's domain, but it is NOT the same object as `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. **vdd's argument conflates two structurally distinct uses of the word "layer": (i) the methodology rule's cross-stratum F-functor; (ii) vdd's agent-memory's intra-substrate K-theoretic vs analytic stratification.** The SIMULTANEOUS-VALIDITY framing depends on this conflation to claim rule-file structural backing; without the conflation, the rule's F does not endorse the intra-substrate split.

This is a *non-trivial* structural objection. The canonical-weight verdict should be derived from the actual rule-file structure (substrate-IS canonical sourcing per `substrate-first-canonical-sourcing.md`, algebra-axis orthogonality per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, Reading-A operator-projection naming hygiene per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`), NOT from an agent-memory layer-hierarchy that is invoked as if it were a rule.

If vdd wants to propose a *new* methodology rule that lifts vdd's agent-memory Topology/Representation/Metric/Functional hierarchy to a permanent rule extension, that is a fair structural proposal — but it would need its own K-counter advancement pathway (K=1 SUGGESTION → K=3 MANDATORY per `feedback_rules-compensate-missing-structure.md`), and the χ'_weight workshop is the *FIRST* calibration instance at K=1 SUGGESTION, not a MANDATORY discipline that pre-commits the verdict.

**D-2. α'(M_LRD) is *downstream* of BOTH K_0-rank-layer AND Metric-layer — it requires BOTH, not one or the other**.

vdd's Re:V1 §"DISAGREE" (line 611-628) and D1 (line 1018-1140) argue that α'(M_LRD)'s evaluator IS the CM-1995 §III.4 residue formula, therefore χ'_weight in α'(M_LRD) IS the Metric-layer trace-mass-fraction 5/14. This reads to me as a *premise collapse*: vdd treats the residue formula as the *only* operative structural object in α'(M_LRD), and therefore the residue trace's pole-pull-back determines the entire multiplicative decomposition.

But α'(M_LRD)'s multiplicative decomposition `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g` is *not* a single residue-formula evaluation. It is a STRUCTURED product whose factors come from STRUCTURALLY DIFFERENT operations:

- `R_universal` = the unrestricted Connes-Karoubi pairing at the W-5 baseline; this IS a CM-1995 §III.4 residue formula evaluation. ✓ (vdd's argument applies)
- `χ'_weight` = the inheritance-restriction weight from `χ' : A_K → M_2(ℂ) ⊗ Cl(1)` Kasparov KK projection; this IS a Kasparov KK functor invariant of χ', NOT a residue formula evaluation. ✗ (vdd's argument does NOT directly apply)
- `(M_KK/M_Pl)²` = the dimensional bridge factor; this is a Pillar I/II spectral-action consequence, NOT a residue evaluation.
- `g(M, L=10)` = the horizon-projector saturation factor; this is a finite-L truncation observable on the substrate spectrum, NOT a residue evaluation.

The multiplicative decomposition is a *composition* of structurally distinct factors. The `χ'_weight` factor lives at the **inheritance-morphism-restriction layer** (where χ' acts categorically on the substrate algebra), NOT at the **residue-formula-evaluation layer** (where the Tr happens). vdd's pole-by-pole verification at T1.9 Step 2 (the 5/14 ratio at every dim-spec pole {0, 2, 4, 6, 8} is exact) is genuine — but it is verification that the *residue trace pushforward* through `χ'` has mass-fraction 5/14, which is a *consequence* of `χ'`'s Hilbert-space-dim restriction, NOT independent evidence about what the canonical inheritance-restriction *weight* should be.

To put it sharply: the residue trace's mass-fraction surviving `χ'` IS 5/14 (vdd is arithmetically correct). The K-class-rank-fraction surviving `χ'` IS 3/6 (V1/V3 is arithmetically correct). Both ratios are computable substrate-IS facts about `χ'`. The question — which one IS the multiplicative pre-factor of `R_universal` in the decomposition? — is NOT settled by either pole-by-pole verification or K-class-rank arithmetic alone. It is settled by the *categorical identification* of which Kasparov KK functorial invariant of `χ'` IS the canonical "inheritance-restriction weight."

Per `3HeB-inheritance-canonical.md` Step 3 (`rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2`, Hodgkin theorem on SU(3) vs S^3), the canonical inheritance-restriction quantity for `iota : (A_K, H_K, D_K) → (A_He, H_He, D_BdG)` is a **K-class-rank invariant of the morphism**, NOT a Hilbert-trace-mass-fraction of its pushforward. The χ' inheritance morphism for the LRD α-anchor is in the SAME categorical class (Kasparov KK projection, per W3 WP line 555-556 "S89 §W2-3 derived theorem"); the analogous canonical inheritance-restriction quantity for χ' IS therefore the K-class-rank invariant 3/6.

vdd's response is that "the χ'_weight factor IN α'(M_LRD) is at the Metric layer because α'(M_LRD)'s evaluator IS the CM-1995 §III.4 residue formula" (D1 line 1099-1108). My counter-claim: α'(M_LRD)'s evaluator USES the CM-1995 §III.4 residue formula AS ONE FACTOR (the R_universal factor), but the χ'_weight factor is a SEPARATE multiplicative input whose categorical identity is fixed by which substrate-IS invariant of χ' the inheritance-restriction weight IS *as a categorical quantity* — and that is the K-class-rank invariant 3/6 per the 3He-B-parallel argument.

**D-3. SOURCE-DOUBLE-CITE-CO-PRIMARY clause-4 same-algebra-axis-cell — Reading 1 + Reading 2 CAN enter a co-primary anchor structure on a single §VII.AU.OP-PROJ slot, because both inhabit Cell I × s=3 — but the vdd-proposed TWO-SLOT structure FAILs a different rule**.

vdd's Re:V5 §"DISAGREE" (line 922-936) proposes two STRUCTURAL-ORTHOGONAL-COMPANION §VII slots:
- `§VII.{X}.OP-PROJ-K0-LAYER`: Reading 1 (3/6) at K_0 functor layer
- `§VII.{X+1}.OP-PROJ-METRIC-LAYER`: Reading 2 (5/14) at CM-1995 §III.4 trace layer

This proposal cites `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92, 2026-05-05) as authority for the suffix structure. Let me check whether the proposal *actually* satisfies that rule.

The Reading-A Operator-Projection Naming Hygiene MANDATORY clause (`registry-landing.md` §"Operator-Projection Reading-A Naming Hygiene", with verbatim K=3 calibration corpus at S87 W4-2 §VII.AJ.W4-1, S87 W6-1 §VII.AG.1, S87 W11-meta-2) distinguishes **operator-projection (OP-PROJ; Type-F algebra-INVARIANT spectrum-only functional)** from **state-projection (STATE-PROJ; Type-S algebra-DEPENDENT state-pair functional)**. The naming convention requires suffix-tagging when a §VII.X theorem admits BOTH operator-projection and state-projection readings. The OP-PROJ side and the STATE-PROJ side are forbidden from being co-primary anchors of the same theorem; STRUCTURAL-ORTHOGONAL-COMPANION is the correct relationship between them.

vdd's proposed suffixes `-K0-LAYER` and `-METRIC-LAYER` are NEITHER `OP-PROJ` NOR `STATE-PROJ`. They invent a new sub-suffix axis (K0/Metric sub-stratification of the same OP-PROJ side). Per the Reading-A Naming Hygiene MANDATORY clause's K=3 corpus, NO precedent exists for sub-suffixes WITHIN the OP-PROJ side. Both Reading 1 (3/6 K-class-rank-fraction; algebra-INVARIANT spectrum-only functional, parse-tree Cell I) and Reading 2 (5/14 dim-trace-fraction; algebra-INVARIANT spectrum-only functional, parse-tree Cell I) are on the OP-PROJ side per the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`. They are NOT on opposite sides of the OP-PROJ / STATE-PROJ orthogonality axis.

**The vdd-proposed two-slot structure invents a sub-axis that has no rule backing.** Under the existing MANDATORY clause, both readings would land at the SAME §VII slot with the SAME OP-PROJ suffix; the canonical-weight verdict adjudicates WITHIN the slot (Reading 1 canonical or Reading 2 canonical or both via co-primary), not by splitting into two slots.

This routes the verdict to one of two structurally valid options:

- **Option A (outcome (i))**: Single §VII slot at S92 W1 with Reading 1 canonical at the K-theoretic inheritance-morphism layer; Reading 2 documented as the Hilbert-trace pushforward through `χ'` (substrate-IS but at a different categorical role; not the canonical χ'_weight factor in `α'(M_LRD)`); Reading 3 documented as the (c)-corridor digamma-modulated AUXILIARY canonical. This is the V5 pre-registration structure.

- **Option B (modified outcome (ii) — same-slot co-primary)**: Single §VII slot at S92 W1 with Reading 1 AND Reading 2 co-primary anchored per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` Detection clauses 1-4. Clause 4 same-algebra-axis-cell check: both inhabit Cell I × s=3, PASS. Clause 1 sequential-derivation check: Reading 2 cannot be evaluated WITHOUT first invoking the χ' faithful-image identification of Reading 1 (the residue's mass-fraction 5/14 of the χ'-image is computed from the same surviving (ℂ ⊕ ℍ) sub-algebra that Reading 1 identifies). Clause 2 non-fungible: arithmetically 3/6 ≠ 5/14; cannot swap. Clause 3 both remain accessible: yes. The structure SOURCE-DOUBLE-CITE-CO-PRIMARY (ANCHOR-1 = K-class-rank invariant via Wedderburn-Artin + Kasparov KK; ANCHOR-2 = Hilbert-trace invariant via CM-1995 §III.4 pole-by-pole identity) is a valid same-slot co-primary structure under clause-4 satisfaction.

Option B is structurally admissible per the existing registry-landing rule. It does NOT require the vdd-proposed two-slot K0/Metric split (which has no rule backing).

But Option B has a different problem: it places TWO non-fungible canonical values (3/6 vs 5/14) at the same registry slot WITHOUT a verdict on which one IS the multiplicative pre-factor of `R_universal`. This is *registry-incomplete* per `cross-pillar-bridge-anatomy.md` 5-anatomy element (5) "Empirical anchor: numerical satisfaction at canonical L_max" — the entry needs ONE numerical value for the empirical anchor, not two non-fungible candidates.

So Option B requires *resolving* the canonical-weight question, not deferring it to "both are simultaneously valid at different layers." The honest scope of co-primary anchoring is "both anchors are needed for the derivation" (sequential), NOT "both anchors are equally canonical multiplicative pre-factors at independent layers" (parallel, the vdd framing).

**My DISSENT proposal**: outcome (i) Reading 1 canonical at the K-theoretic inheritance-morphism layer (the multiplicative pre-factor in `α'(M_LRD)`), with Reading 2 documented as the Hilbert-trace pushforward arithmetic identity at the residue trace evaluator (substrate-IS fact but at a different categorical role, NOT the multiplicative pre-factor); Reading 3 documented as the (c)-corridor digamma-modulated AUXILIARY canonical inheriting Reading 1's 3/6 pre-factor.

If vdd cannot accept outcome (i) under D-2's K-class-rank-fraction-IS-the-canonical-weight argument, AND outcome (ii) vdd-style two-slot K0/Metric split fails D-3's rule-backing argument, AND Option B same-slot co-primary fails registry-incompleteness — then the workshop verdict routes to **outcome (iii) OPEN registry slot** with explicit substrate-physics carry-forward to S92+, NOT to vdd's outcome (ii) two-slot framing.

### EMERGENCE

Three new structural insights have surfaced through R1+R1 exchange that did NOT exist in the seed-w2-w3.md investigator brief or in V1-V5 / Re:V1-V5 / D1-D3 individually. I record them here as the workshop's substantive new content.

**E-1. The χ' inheritance morphism carries FOUR structurally distinct substrate-IS K-theoretic / trace invariants — vdd's Re:V3 §"EMERGES" tabulation is a permanent framework contribution**.

vdd's Re:V3 line 760-777 enumerates four invariants of the same Kasparov KK projection χ':

| # | Invariant | Value | Categorical role |
|:-:|:----------|:------|:-----------------|
| #1 | Source-side K-class-rank-mass-fraction | 3/6 = 0.500 | K_0 functor invariant |
| #2 | Source-side regular-rep Hilbert-trace-mass-fraction | 5/14 ≈ 0.357 | CM-1995 §III.4 residue trace pushforward |
| #3a | Target-side K-class-rank ratio | 3/4 = 0.750 | V3-rejected (target representational-room K-rank) |
| #3b | Target-side Hilbert-space-image-dim ratio | 5/8 = 0.625 | D2 candidate (target representational-room Hilbert-trace-dim) |

**This four-way enumeration is a permanent framework contribution that should land in the registry as documentation regardless of the canonical-weight verdict outcome.** The four invariants are substrate-IS facts about χ' on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); they are computable Sage-rationals; they are pole-INDEPENDENT in their respective evaluations.

The framework's `falsifier-master-inventory.md` and `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` benefit from documenting all four — even if only one (Reading 1 per outcome (i), or Readings 1+2 per Option B) is the canonical multiplicative pre-factor of `α'(M_LRD)`. The framework gains structural clarity about which Kasparov-KK invariants are admissible substrate-IS quantities.

I propose this four-way enumeration land as a *calibration-corpus annotation* on the S92 χ'_weight canonical-weight registry slot, NOT as four separate §VII slots. This is consistent with vdd's D2 "calibration corpus entry, not registry §VII slot" recommendation for the 5/8 target-side ratio (D2 line 1303-1304).

**E-2. The four-axis discriminator structure (α / β / γ / δ) is a candidate K-counter advancement for an *intra-Cell-I* within-cell adjudication rule extension** — but with explicit K=1 SUGGESTION status, NOT an existing rule.

vdd's Re:V4 §"MISSED (axis (δ): evaluator-trace-layer vs K_0-rank-layer axis)" (line 854-862) introduces a fourth substrate-priority axis (δ) to complement V4's three axes (α / β / γ). Reading V4 + Re:V4 together, the four-axis structure is:

- (α) K-theoretic vs representation-theoretic axis
- (β) Source-side vs target-side axis
- (γ) Primary corridor (b) vs auxiliary corridor (c) axis
- (δ) Evaluator-trace-layer vs K_0-rank-layer axis (vdd's new contribution)

This four-axis discriminator structure is genuinely new. The existing algebra-axis orthogonality K=3 MANDATORY clause (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) operates at the *cross-cell* axis (Cell I / II / III / IV partition); it is silent on *within-cell* discrimination. The four-axis structure operates at the *within-cell* level — discriminating among multiple substrate-IS observables that all parse to the same corner cell.

But — and this is the structural caution — the four-axis structure is *the FIRST workshop instance* in the framework's corpus where within-cell discrimination is needed for canonical-weight adjudication. Per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold (K=3 distinct calibration instances for SUGGESTION → MANDATORY promotion), the four-axis discriminator is at **K=1 SUGGESTION status** at workshop close — it is not yet a MANDATORY discipline.

I propose the workshop's verdict on the canonical-weight question land the four-axis structure as a K=1 SUGGESTION at `cross-pillar-bridge-anatomy.md §"Within-cell discriminator axes"` (new sub-section) with explicit forward calibration corpus expansion expectation: K=2 at the next within-cell canonical-weight workshop, K=3 MANDATORY at the third. This routes the methodology-rule extension through the standard SUGGESTION → MANDATORY pathway WITHOUT pre-committing the χ'_weight verdict to vdd's outcome (ii) framing.

**E-3. The §VII.AF.1.OP-PROJ baseline's `R_universal · χ'_weight · (M_KK/M_Pl)² · g` multiplicative decomposition is the FIRST framework instance where inheritance-morphism restrictions are explicitly multiplicative factors on a permanent-registry observable — and this raises a structural cross-link to §VII.AV (W-1 result), §VII.AY, §VII.AZ that should be made explicit**.

The χ'_weight canonical-weight verdict has cross-link consequences for any §VII slot that consumes a χ'-restriction or χ'-pullback in its anatomy. Surveying the registry for χ'-consumers:

- **§VII.AV** (W-1 workshop result, FWD-C2 candidate per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"`, Pillar III/IV ↔ Pillar V; Casimir-bound proxy pending FULL BdG per CF-W5-3 / W-6 CF-2): if §VII.AV's substrate-IS observable consumes a χ'-restriction or analog inheritance morphism, the canonical-weight verdict on χ'_weight propagates as a cross-link. From my agent-memory snapshot, §VII.AV is the BdG-sector analog observable on the Pillar V child realization; the χ' inheritance morphism is the structural bridge from Pillar III/IV (the source) to Pillar V (the BdG-sector target). The canonical-weight verdict on χ'_weight therefore propagates to §VII.AV's multiplicative pre-factor IF §VII.AV uses the same `α'(M_LRD)`-style decomposition. **The cross-link MUST be made explicit in the S92 registry landing.**

- **§VII.AY** + **§VII.AZ** (if these are χ'-consumers): similar cross-link. I do not have full registry text for §VII.AY / §VII.AZ in my immediate access; the S92 registry landing should perform an explicit cross-link audit on all χ'-consuming entries and document the canonical-weight propagation.

**Forward dispatch recommendation**: S92 W1 χ'_weight canonical-weight registry landing should include a Stage-2 cross-axis verify sub-clause requiring mack-cosmic-bridge (sole registry writer per `feedback_mack-bridge-role.md`) to audit ALL §VII slots for χ'-consumption and either (i) document NO-DELTA where the slot does not consume a χ'-weight factor (e.g., §VII.AF.1.OP-PROJ baseline which is unrestricted; confirmed in C-6 above) OR (ii) document the canonical-weight propagation where the slot does consume a χ'-weight factor (candidates: §VII.AV, §VII.AY, §VII.AZ pending audit).

This is a structural infrastructure addition the workshop generates, NOT a pre-existing framework artifact. It is E-3 emergence.

### QUESTIONS

#### Answers to vdd's Q-VLV-1 through Q-VLV-5

**Q-VLV-1 (Chern-character pairing layer — does Wedderburn-RANK or HS-DIM appear?)**.

The pole-by-pole 5/14 identity is *arithmetic-correct* — I do not contest the Sage-rational verification at every pole of dim_spec((A_K, H_K, D_K)|_{L_max=10}) = {0, 2, 4, 6, 8} that T1.9 reports (workshop document line 1067-1071: "The trace-mass-fraction 5/14 is pole-INDEPENDENT — a structural identity at the dim-spec residue formula evaluator on the χ'-restricted Hilbert sub-representation").

What I contest is the *categorical identification* "the χ'-restricted residue's mass-fraction IS the χ'_weight in α'(M_LRD)." The pole-by-pole 5/14 identity is the *Hilbert-trace pushforward* of `χ'` evaluated through the dim-spec residue trace; it is a downstream consequence of the K-class-rank survival (3/6) at the K_0 functor layer. The substrate-IS fact "the regular representation of (ℂ ⊕ ℍ) acts on a 5-dim Hilbert subspace of the 14-dim ambient regular representation" IS true (and gives 5/14); but this 5-dim-versus-14-dim Hilbert-trace decomposition is INDUCED by the K-class-rank decomposition (rank-3 surviving in rank-6 ambient gives rise to the 5-dim Hilbert image because dim_HS = Σ rank_i² where the surviving rank-3 contributes rank(ℂ)² + rank(ℍ)² = 1 + 4 = 5 to the dim-trace). The dim-trace ratio 5/14 is *computed from* the K-rank ratio 3/6 via the dim_HS = Σ rank_i² Wedderburn formula; it is NOT an independent substrate-IS invariant of equal categorical standing.

So my answer to Q-VLV-1: yes, the pole-by-pole 5/14 IS verified arithmetic at the residue evaluation; AND 3/6 IS the K-class-rank-mass-fraction at the K_0 functor layer; BUT 5/14 is derivable FROM 3/6 via the dim_HS = Σ rank_i² Wedderburn formula. The two are NOT independent canonical candidates — one (3/6) is upstream of the other (5/14) in the substrate algebra's structure constants chain. The inheritance-morphism canonical weight IS the upstream K-class-rank invariant; the residue-trace mass-fraction is the downstream Hilbert-trace consequence.

I do not need to cite a pole where 5/14 fails — I grant 5/14 holds at every pole. My counter-claim is at the *categorical level*: the residue mass-fraction is downstream of K-class-rank survival, not an independent invariant.

**Q-VLV-2 (Kasparov KK-bridge inheritance morphism — what does χ_* preserve?)**.

vdd cites the K-track / spectral-moment categorical boundary "Kasparov product gives TOPOLOGY (K-homology class, indices, factorization). NOT ANALYSIS (spectral moments)" from vdd's agent memory (Q-VLV-2 line 1350) as evidence that K_0 functoriality (F1) cannot determine Metric-layer multiplicative pre-factors.

I accept the boundary as cited. I dispute its application to the χ'_weight question. The boundary says "Kasparov product gives TOPOLOGY" — yes, Kasparov KK projections (which `χ'` IS) preserve K-class indices. The boundary does NOT say "K-class indices are forbidden from being multiplicative pre-factors in spectral-action multiplicative decompositions." The boundary specifies what Kasparov KK *gives* (Topology), not what observables Topology-layer invariants are *forbidden from* (Metric layer).

In particular: the χ'_weight factor in `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g` is NOT a *spectral moment* (it does not have the form `a_n^SD` or `Tr(D^{-2s})`); it is a *categorical multiplicative weight* that scales R_universal by the fraction of the substrate algebra that survives the inheritance morphism. The 3HeB-inheritance parallel (Hodgkin theorem `rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2`) makes clear that the inheritance-morphism canonical quantity IS a K-class-rank invariant, NOT a spectral-moment / Hilbert-trace invariant.

So my answer to Q-VLV-2: the K-track / spectral-moment boundary is a valid categorical separation — Kasparov KK gives K-homology classes; Mellin / Seeley-DeWitt give spectral moments. But the χ'_weight factor is in the FIRST category (a Kasparov KK functorial invariant), NOT the second (a spectral moment). The boundary therefore *supports* my reading (3/6 is canonical at the K-class layer where χ'_weight lives) rather than vdd's reading.

The structural theorem vdd asks me to cite is the **inheritance-morphism canonical weight definition itself**: per `3HeB-inheritance-canonical.md` Step 3, the inheritance-morphism's canonical quantity is its K-class-rank invariant. The χ' inheritance morphism for the LRD α-anchor (Pillar III↔IV) is in the same categorical class as the 3He-B iota; its canonical inheritance-restriction weight is therefore its K-class-rank invariant, 3/6.

**Q-VLV-3 (CM-1995 §III.4 dim-spec residue evaluation — where does Reading 1 vs Reading 2 diverge?)**.

I read CF-37's 3/6 as a STRUCTURAL THEOREM at the inheritance-morphism layer (the K-class-rank invariant of χ'_* : K_0(A_K) → K_0(target)) that holds INDEPENDENTLY of T1.9's 5/14 pole-by-pole residue-trace verification. The CF-37 structural-ansatz is NOT a substitution of K-rank-mass into a position where the algebraic evaluator prescribes Hilbert-trace-mass — it is an evaluation of the *correct* invariant (K-class-rank survival) at the χ'_weight position.

The structural theorem identifying K-rank-mass-fraction with Hilbert-trace-mass-fraction at the CM-1995 §III.4 residue evaluator is **the Wedderburn formula dim_HS(M_n(D)) = n² · dim(D)**, which gives:
- dim_HS(ℂ) = 1² · 1 = 1 (rank 1, dim_HS 1)
- dim_HS(ℍ_ℂ) = 2² · 1 = 4 (rank 2, dim_HS 4) [where ℍ ⊗_ℝ ℂ ≅ M_2(ℂ) carries the complex Hilbert-trace dim 4]
- dim_HS(M_3(ℂ)) = 3² · 1 = 9 (rank 3, dim_HS 9)

The mapping rank_i ↦ rank_i² takes (1, 2, 3) → (1, 4, 9) and (3, 6) → (5, 14). The dim-trace ratio 5/14 IS the Wedderburn-formula image of the K-rank ratio 3/6 via the squaring operation. **5/14 is not an independent invariant — it is the dim_HS = rank² image of 3/6.**

Concretely: any morphism that preserves K-class-rank (Kasparov KK projection) ALSO preserves the dim_HS-image of K-class-rank (by direct application of the Wedderburn formula). The residue trace's pole-by-pole identification of 5/14 IS the inheritance morphism's K-class-rank survival 3/6 *as it appears in the dim_HS-squared image*. The two are not categorically independent.

T1.9's pole-by-pole 5/14 verification is therefore *consistent with* but does not *replace* CF-37's 3/6 structural-ansatz. CF-37 evaluates the K-class-rank invariant of χ' at the χ'_weight position; T1.9 verifies that the dim_HS-image of this invariant matches the pole-by-pole residue mass-fraction (which it must by the Wedderburn formula). T1.9 IS confirmation of CF-37, not replacement.

**Q-VLV-4 (L_max → ∞ asymptotic behavior of both readings)**.

Both readings are L_max-INDEPENDENT BY CONSTRUCTION — I grant this. The L_max → ∞ asymptote does NOT discriminate them as numerical limits. But L_max-independence is not the discriminator; *categorical identity* is.

The χ'_weight factor in the multiplicative decomposition of α'(M_LRD) IS a categorical invariant of χ' at the inheritance-morphism layer. The K-class-rank invariant 3/6 is the *direct* K-class-rank survival; the Hilbert-trace invariant 5/14 is the *Wedderburn-formula image* of the K-rank invariant via the rank² → dim_HS squaring. They both extend trivially to L_max → ∞ (neither has a finite-L correction structure that vanishes asymptotically).

So the answer to Q-VLV-4 "does the χ'_weight take 3/6 or 5/14 at L_max → ∞?": both ARE L_max-independent; both extend trivially. But this does NOT support outcome (ii) SIMULTANEOUS-VALIDITY as the *unique* reading. The L_max → ∞ co-existence is compatible with outcome (i) Reading 1 canonical (where Reading 2 is the Wedderburn-formula image of Reading 1, both L_max-independent, with only Reading 1 entering the multiplicative pre-factor of `α'(M_LRD)`).

I do not need to cite an `L_max` correction structure that routes 5/14 → 3/6 in the limit (vdd's challenge), because I do NOT claim 5/14 vanishes asymptotically — I claim 5/14 IS the Wedderburn-formula squared image of 3/6 at every L_max including L_max → ∞, with only 3/6 entering the multiplicative pre-factor categorically.

**Q-VLV-5 (registry-landing shape — does outcome (ii) accommodate your V5 framework?)**.

I answered this in DISSENT D-3 above. The vdd-proposed two-slot K0-LAYER / METRIC-LAYER structure fails `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY K=3 because the K=3 corpus has NO precedent for sub-suffixes within the OP-PROJ side (both 3/6 and 5/14 are OP-PROJ-side per parse-tree decision procedure; neither is STATE-PROJ).

To address vdd's items (i)-(iv) explicitly:
- (i) §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ no-delta: yes preserved under either outcome (i) or vdd's outcome (ii) — both retain pre-existing status. C-6 above already settled this.
- (ii) Stage-2 cross-axis verify HARD-exclude on volovik + vdd: yes preserved under either outcome. C-7 above already settled this.
- (iii) Hybrid Independence Test K-counter stays at K=1: I read this differently. Under outcome (ii) two-slot framing, you compute SHARED-ANCHOR-COMPANION on BOTH slots (because each shares pillar / lab / bridge with §VII.AF.1.OP-PROJ baseline; only axis (iv) algebraic envelope is partially distinct). My DISSENT D-3 is that the two-slot framing itself is not registry-admissible; the question of how the Hybrid Independence Test applies to a non-admissible structure is moot.
- (iv) Phi-correspondence layer-decomposition advisory K-counter advancement to K=1: I DISPUTE this on the D-1 grounds — `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit` is a *cross-stratum* layer-functor, NOT an intra-substrate K_0/Metric stratification. vdd's "Phi-correspondence layer-decomposition K-counter" appears to be a NEW invented K-counter that is not the same object as the rule's Phi correspondence (which maps `weight(a_n^SD) = n` to `weight(Σ_d) = enforcement-strength` ACROSS substrate ↔ methodology strata). Advancing a K-counter on a NEW object is not "calibration corpus expansion" of an existing rule — it is *establishing* a new methodology-rule extension at K=1 SUGGESTION. The χ'_weight workshop IS the first instance, and the SUGGESTION → MANDATORY pathway should proceed through the standard route (K=1 SUGGESTION at landing; forward calibration at K=2, K=3) rather than pre-committed via cross-citation.

So my answer to Q-VLV-5: I agree on (i) and (ii); I dispute (iii) at the precondition (the two-slot framing is non-admissible per D-3); I dispute (iv) at the rule citation (the Phi-correspondence object vdd invokes is not the rule's Phi correspondence).

#### Q-FINAL for vdd's R2-B (final round; vdd writes the Verdict table + Wrap-Up)

**Q-FINAL-VLV-1 (rule-backing for the OP-PROJ sub-suffix axis)**.

My DISSENT D-3 argues the vdd-proposed `-K0-LAYER` and `-METRIC-LAYER` sub-suffixes are not in the K=3 MANDATORY calibration corpus of `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (which contains S87 W4-2 §VII.AJ.W4-1, S87 W6-1 §VII.AG.1, S87 W11-meta-2 — all OP-PROJ vs STATE-PROJ instances, no sub-suffix instances within OP-PROJ).

If vdd's R2-B retains outcome (ii) with the two-slot framing as the verdict, **please cite the rule-backing that authorizes sub-suffixes within the OP-PROJ side** OR explicitly mark the two-slot framing as a K=1 SUGGESTION rule extension (NEW methodology rule) with explicit forward calibration corpus expansion plan. Without rule-backing or explicit SUGGESTION status, the two-slot framing should not enter the registry as if it were a MANDATORY-K=3-supported structure.

**Q-FINAL-VLV-2 (the Wedderburn-formula image relation — does 5/14 = rank² image of 3/6 collapse SIMULTANEOUS-VALIDITY?)**.

My Q-VLV-3 answer derives that `dim_HS = rank²` (Wedderburn formula) takes the K-rank ratio (3, 6) → (5, 14) via the squaring operation. If vdd accepts this Wedderburn-formula image relation, then 5/14 is *derivable from* 3/6 (not categorically independent), and the SIMULTANEOUS-VALIDITY framing — which requires the two invariants to be *independent* canonical candidates at non-fungible layers — is structurally weakened.

**Please address in R2-B: do you accept that `dim_HS(M_n(ℂ)) = n²` is the Wedderburn-formula image relation taking K-rank to dim_HS? If yes, does this image-derivation relation between the two invariants collapse SIMULTANEOUS-VALIDITY into a single canonical (3/6) at the upstream K-class-rank layer, with 5/14 the downstream image not an independent canonical?** If no, please cite the structural argument that establishes 5/14 as categorically independent of 3/6 despite the Wedderburn-formula image relation.

**Q-FINAL-VLV-3 (cross-link consequences for §VII.AV / §VII.AY / §VII.AZ — does the canonical-weight verdict propagate?)**.

My EMERGENCE E-3 raises the cross-link audit requirement: the S92 χ'_weight canonical-weight registry landing should audit all §VII slots for χ'-consumption and document NO-DELTA where applicable / propagation-delta where the slot consumes a χ'_weight factor. The candidates §VII.AV (W-1 result, FWD-C2 candidate; from my agent memory the BdG-sector analog observable), §VII.AY, §VII.AZ are obvious cross-link targets, but I do not have full registry text for each in this workshop's scope.

**Please address in R2-B: do you concur the cross-link audit is structurally required as part of the S92 χ'_weight canonical-weight registry landing? If yes, should the audit be a separate gate (`S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT`) dispatched alongside the canonical-weight landing, or an in-line cross-link section within the canonical-weight registry entry?** Either way, mack-cosmic-bridge (sole §VII registry writer per `feedback_mack-bridge-role.md`) is the natural dispatch owner; the question is gate-structure, not owner-identity.

---

**Closing meta-statement (Volovik on R2 routing)**:

I read the workshop's structural state at end-of-R2-Volovik as follows. The R1+R1 exchange produced genuine substrate-physics convergence on 8 points (C-1 through C-8) including settling C-8 that 3/6 and 5/14 are both substrate-IS K-theoretic / trace invariants of the same Kasparov KK projection χ' on `A_K` (vdd's tabulation in Re:V3 §"EMERGES"). The remaining contest is at three structural axes (D-1 layer-functor mis-application; D-2 α'(M_LRD) requires BOTH layers; D-3 OP-PROJ sub-suffix axis has no rule backing). My DISSENT does NOT reject the SIMULTANEOUS-VALIDITY *framing at the invariant-class level* (I accept C-8); I reject the SIMULTANEOUS-VALIDITY *registry-landing structure* (two slots with sub-suffixes; D-3) AND the Layer-Decomposition F rule citation (D-1).

The candidate verdict structures at workshop close:

- **Outcome (i) Reading 1 canonical (single slot)**: structurally admissible per all existing rules; V5 pre-registration is well-formed; vdd's Re:V1-V5 acceptance of K_0-rank survival 3/6 supports this outcome at the K-theoretic / 3HeB-inheritance-parallel layer.
- **Outcome (ii) two-slot K0/Metric (vdd-proposed)**: structurally INADMISSIBLE per D-3 (no rule backing for OP-PROJ sub-suffixes) AND D-1 (the rule's Layer-Decomposition F is cross-stratum, not intra-substrate). Cannot land as-proposed without rule extension at K=1 SUGGESTION status.
- **Option B same-slot co-primary (3/6 + 5/14 both anchors at same §VII slot)**: structurally admissible per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clauses 1-4 (both Cell I × s=3 PASS clause-4); but registry-incomplete per `cross-pillar-bridge-anatomy.md` 5-anatomy element (5) (Empirical anchor requires ONE numerical value); requires resolving the canonical-weight question, not deferring it.
- **Outcome (iii) OPEN registry slot**: explicit substrate-physics carry-forward to S92+ with STAGE-1-CANDIDATE-OPEN-CHI-PRIME-WEIGHT-CANONICALIZATION tag; pre-registration of canonical-weight question for S92+ workshop with explicit Stage-2 cross-axis verify reviewer pool (connes-ncg + mack-cosmic-bridge, HARD-exclude volovik + vdd).

My honest reading: outcome (i) is the structurally cleanest verdict if vdd's R2-B accepts the Wedderburn-formula image relation (Q-FINAL-VLV-2) collapses the categorical independence of 5/14 from 3/6. Outcome (iii) is the appropriate fallback if vdd's R2-B holds the structural independence claim AND the workshop cannot converge on a single canonical — the carry-forward defers the verdict honestly rather than landing an inadmissible two-slot framing.

I look forward to vdd's R2-B response on Q-FINAL-VLV-1 through Q-FINAL-VLV-3 and the workshop verdict table.

---

## Round 2 — Van-den-Dungen: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

Reading volovik's R2 carefully (C-1 through C-8, D-1 through D-3, E-1 through E-3, and the answers to my Q-VLV-1 through Q-VLV-5), I find the exchange has produced substantial settled content — including a **new substrate-physics structural identity** I missed in R1 (the Wedderburn-formula `dim_HS = rank²` image relation) — alongside three substantive structural dissents on R1 that I must honestly address. I separate the convergence from the rebuttal here.

**C-vdd-1. Volovik's C-1 (K-class-rank invariant 3/6 at K_0(A_K) functor layer uncontested) is correct as I framed it.**

I confirm my Re:V1 §"AGREE (partial — what holds at the K-theoretic class layer)" (workshop line 607-609) concedes the substance: `K_0(A_K) ≅ ℤ ⊕ ℤ ⊕ ℤ` at generator ranks (1, 2, 3); `χ'_*` kills the `M_3(ℂ)` generator; the K-class-rank-mass-fraction `3/6` is the K_0-functor invariant of `χ'`. This concession is structural, not rhetorical. **C-1 lands as settled.**

**C-vdd-2. Volovik's C-2 (corridor orthogonality + c_aux derivation; SIMULTANEOUS-VALIDITY at (b)/(c) corridor-decomposition level) is correct.**

The Re:V2 reading — that `c_aux = 1/3` is substrate-Wedderburn-fixed by `(1 − 2 + 3)/6`, the (b)/(c) corridors are orthogonal element-1 deformation columns (Kasparov-product factorization at the unbounded-KK theorem layer — Paper 01 / 1811.07824), and `(1 − γ_Euler/3)` is structurally-IRRATIONAL-per-CC2-analog at the algebraic-number-class layer — is settled. The (c)-corridor cannot collapse into the (b)-corridor. **C-2 lands as settled; the canonical-weight contest is intra-(b)-corridor only.**

**C-vdd-3. Volovik's C-3 (S89 §W2-3 faithful-image identification) is correct.**

My Re:V3 §"AGREE" (line 715-723) concurs on the 8-step Wedderburn 9 > 8 + Schur orthogonality argument and the machine-epsilon witness `chi_prime_pullback_machine_eps_PASS = True`. The faithful image of `χ'` is `ℂ ⊕ ℍ`; the M_3(ℂ) kernel rank is 9. **C-3 lands as settled.**

**C-vdd-4. Volovik's C-4 (K=3 MANDATORY orthogonality silence within Cell I × s=3) is correct.**

My Re:V4 §"AGREE (corner classification; K-counter silence on within-cell weight choice)" (line 810-820) concurs entirely. All three readings (and the 5/8 D2 candidate) parse to Cell I × s=3 via `permanent-results-registry.md §VII.U.2 clause (e)`; the K=3 MANDATORY clause's enforcement is satisfied by all readings; the K-counter does not discriminate within-cell. **C-4 lands as settled.**

**C-vdd-5. Volovik's C-5 (CF-37 / T1.8 / T1.9 verdict permanence at FAIL) is correct.**

My Re:V5 line 920-921 concurs. All three verdict lines retain their FAIL composite verdicts at the 1/458 empirical anchor; no `supersedes=` tag is required per Option A absolute permanence; the canonical-weight verdict at S92 clarifies WHICH substrate-derivation IS canonical without modifying any verdict-line value. **C-5 lands as settled.**

**C-vdd-6. Volovik's C-6 (§VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ no-delta on the unrestricted baseline) is correct.**

My Re:V5 items 2 + 3 (lines 915-917) concur. The W-5 baseline R_universal = 1.030902 is unrestricted (no χ'_weight consumed); §VII.AU.OP-PROJ FWD-C1 retains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION per S90 W1-15 deferred-pending re-tag. **C-6 lands as settled.**

**C-vdd-7. Volovik's C-7 (Stage-2 HARD-exclude on volovik + vdd; connes-ncg + mack-cosmic-bridge as Axis-A + Axis-B) is correct.**

My Re:V5 item 4 (line 919) concurs per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach extension (S88 W-14 W4a-17 V.2 MANDATORY at K=1). Both volovik (V1-V5 author) and vdd (R1 cross-synthesis + T1.8 Axis-B + T1.9 Axis-A author) are HARD-excluded. connes-ncg-theorist (NCG-axiomatic depth on Kasparov-KK projections + Wedderburn-Artin) for Axis-A; mack-cosmic-bridge (§VII registry sole-writer per `feedback_mack-bridge-role.md`) for Axis-B. **C-7 lands as settled.**

**C-vdd-8. Volovik's C-8 (SIMULTANEOUS-VALIDITY at the *invariant-class* level; 3/6 IS substrate-IS K-theoretic, 5/14 IS substrate-IS Hilbert-trace; the two count different categorical things on the same Kasparov KK projection) is correct AND the precise scope volovik names matches my own intent.**

The precise scope volovik articulates at C-8 (workshop line 1453-1457) is: **the SIMULTANEOUS-VALIDITY framework I proposed answers WHICH INVARIANTS `χ'` CARRIES, NOT the canonical-weight question (WHICH INVARIANT ENTERS `α'(M_LRD)`).** This scope-clarification is correct and is the cleanest framing of the structural-fact content. I accept C-8 as a sharper restatement of my Re:V1/V3 EMERGES tabulation than I produced in R1.

The disagreement remaining at workshop close is therefore not about WHICH invariants `χ'` carries (settled: both 3/6 and 5/14 are substrate-IS invariants of the same Kasparov KK projection), but about which invariant IS the multiplicative pre-factor of `R_universal` in `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g`. This is the substance of D-2 below.

**C-vdd-9 (NEW; the Wedderburn-formula image relation IS a substantive workshop discovery that I missed in R1).**

Volovik's Q-VLV-3 answer (workshop lines 1604-1613) derives the **Wedderburn formula** `dim_HS(M_n(D)) = n² · dim(D)` and demonstrates that the K-rank ratio `(1, 2, 3) → (5, 14)` via the squaring operation:

```
rank(ℂ) = 1   ↦   dim_HS(ℂ) = 1² = 1
rank(ℍ) = 2   ↦   dim_HS(ℍ_ℂ) = 2² = 4
rank(M_3(ℂ)) = 3   ↦   dim_HS(M_3(ℂ)) = 3² = 9
```

so `(rank ℂ + rank ℍ)/(rank A_K) = 3/6` IMAGES to `(dim_HS ℂ + dim_HS ℍ)/(dim_HS A_K) = 5/14` under the rank² → dim_HS squaring operation on each summand individually. **The two ratios are not categorically independent at the substrate algebra structure-constants layer** — the Wedderburn formula is an algebraic identity of `A_K` itself, holding before any morphism is applied.

I missed this in R1 and concede it now. The Wedderburn-formula image relation is structurally important and is itself a substrate-physics theorem on `A_K` that the workshop has surfaced. **It lands as a new substrate-physics observation, regardless of which canonical-weight outcome S92 selects.**

But — and this is where the structural concession ends — the image relation does NOT collapse the canonical-weight question into a single canonical at the upstream K-rank layer (D-2 + Q-FINAL-VLV-2 answer below). The image relation is an **algebraic identity at the structure-constants layer of A_K**; whether `χ'_weight` IN `α'(M_LRD)` is 3/6 or 5/14 depends on **which functorial invariant of `χ'` the multiplicative pre-factor IS** (Kasparov-KK invariant under `χ'_*` on `K_0` vs trace pullback on `Tr`). The image relation tells us that knowing one determines the other algebraically; it does NOT tell us which one IS the multiplicative pre-factor at the bridge-map evaluation. The categorical-identity question is separate from the algebraic-identity question.

**C-vdd-10. Volovik's D-1 critique of my "four-layer hierarchy" citation is correct as written; I concede the rule-citation misapplication.**

I owe volovik an honest concession on D-1. Re-reading `epistemic-discipline.md §"Layer-Decomposition"` (verified by direct read of the rule file content at lines 307-345 cited in the CLAUDE.md system prompt):

```
F: substrate → methodology → audit
```

is a *cross-stratum* layer-functor between THREE strata (substrate-physics, methodology-floor rule files, audit-floor verdict files). The two tables `§"F at substrate ↔ methodology pair"` and `§"F at methodology ↔ audit pair"` enumerate cross-stratum mappings (eigenvalue → rule-file content; numerical PASS predicate → artifact-existence predicate; verdict-line numerical value → verdict-line artifact-SHA). The Phi correspondence at the bottom maps `weight(a_n^SD) = n` (substrate-physics) to `weight(Σ_d) = enforcement-strength` (methodology). Both sides of Phi are at *different strata*. **The Phi correspondence does NOT define an intra-substrate K_0 / Metric stratification.**

My "four-layer hierarchy" (Topology / Representation / Metric / Functional) from my agent MEMORY.md is a useful organizing principle for my own domain (NCG submersions; the four layers help me parse where individual results live within the substrate's structure). But it is NOT the same object as `epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`. My Re:V1 (line 654), Re:V3 (line 805-806), and Re:V4 (line 858) citations conflated these two distinct uses of "layer"; volovik's D-1 critique is correct.

The honest scope: **the framework's rule-file structure does NOT currently support an intra-substrate K_0-layer/Metric-layer stratification under MANDATORY discipline.** If such a stratification is structurally needed, it must enter the framework as a NEW methodology rule extension at K=1 SUGGESTION → K=3 MANDATORY pathway per `feedback_rules-compensate-missing-structure.md`. The χ'_weight workshop is the FIRST candidate calibration instance, NOT a MANDATORY discipline that pre-commits the verdict.

I withdraw the rule-file citation `epistemic-discipline.md §"Layer-Decomposition"` as authority for the intra-substrate Phi-correspondence layer-decomposition framing. The intra-substrate K_0/Metric stratification stands or falls on its own substrate-physics merits, NOT on rule-file backing it does not have.

**C-vdd-11. Volovik's D-3 critique of my proposed `-K0-LAYER` / `-METRIC-LAYER` OP-PROJ sub-suffixes is correct; I concede the registry-naming-hygiene gap.**

Re-reading `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3, S88 W8-92, 2026-05-05) with the K=3 calibration corpus (S87 W4-2 §VII.AJ.W4-1; S87 W6-1 §VII.AG.1; S87 W11-meta-2): all three calibration instances are OP-PROJ vs STATE-PROJ distinctions (operator-projection / algebra-INVARIANT spectrum-only functional family vs state-projection / algebra-DEPENDENT state-pair functional family). **No calibration corpus instance exists for SUB-SUFFIXES WITHIN the OP-PROJ side.**

My Re:V5 §"DISAGREE" proposal of TWO STRUCTURAL-ORTHOGONAL-COMPANION slots `§VII.{X}.OP-PROJ-K0-LAYER` + `§VII.{X+1}.OP-PROJ-METRIC-LAYER` (line 933-936) invents a sub-axis that has no rule backing. Volovik's D-3 reading is correct: under the existing MANDATORY-K=3 clause, both Reading 1 (3/6) and Reading 2 (5/14) are OP-PROJ-side per the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`; they are NOT on opposite sides of the OP-PROJ/STATE-PROJ orthogonality axis.

I concede the registry-naming-hygiene gap. The two-slot K0/Metric framing requires NEW methodology rule extension (a sub-suffix discipline WITHIN the OP-PROJ side) at K=1 SUGGESTION; absent that rule extension, the two-slot framing is NOT registry-admissible as-proposed.

This combined with C-vdd-10 means: my Re:V5 outcome (ii) proposal as written CANNOT land at S92 without first establishing the supporting methodology rule extensions. The intra-substrate K_0/Metric stratification (C-vdd-10) and the OP-PROJ sub-suffix axis (C-vdd-11) are both K=1 SUGGESTION-level structural proposals, not MANDATORY-backed registry-landings.

#### Answers to Q-FINAL-VLV-1, Q-FINAL-VLV-2, Q-FINAL-VLV-3

**Q-FINAL-VLV-1 (rule-backing for OP-PROJ sub-suffix axis)**.

Conceded per C-vdd-11 above. The `-K0-LAYER` / `-METRIC-LAYER` sub-suffixes have NO precedent in the K=3 MANDATORY calibration corpus. Three honest forward routes exist:

1. **Withdraw the two-slot framing**: my Re:V5 outcome (ii) proposal as registry-landing structure is withdrawn. Reading 1 and Reading 2 cannot land as STRUCTURAL-ORTHOGONAL-COMPANION at sub-suffix-axis distinct slots under existing rules.
2. **Reframe as K=1 SUGGESTION rule extension**: lift the OP-PROJ sub-suffix axis to a NEW methodology-rule SUGGESTION at K=1 (the χ'_weight workshop's first calibration instance). Land as registry-landing.md §"Operator-Projection Reading-A Naming Hygiene — Sub-Suffix Extension (S91 W-2 K=1 SUGGESTION)" with explicit forward-calibration-corpus-expansion expectation (K=2 at next within-OP-PROJ workshop, K=3 MANDATORY at the third). The χ'_weight workshop's two-slot landing then proceeds under SUGGESTION status; S92+ workshops on similar K_0/Metric layer-distinctions advance the K-counter.
3. **Single-slot landing with co-primary or simultaneous-validity framing INSIDE the slot**: land Reading 1 and Reading 2 at a SINGLE `§VII.{X}.OP-PROJ` slot with either Option B same-slot co-primary anchoring (which volovik's D-3 notes has its own registry-incompleteness problem at the 5-anatomy Element 5 layer — see Q-FINAL-VLV-2 answer below) OR with explicit "two-canonical-axes" prose annotation INSIDE the slot text.

I concede route 1 is the cleanest from a methodology-rule-hygiene perspective. Route 2 is structurally honest but requires advance K=1 SUGGESTION landing in `registry-landing.md` before the χ'_weight registry slot can use the sub-suffix discipline. Route 3 has the Element-5 single-empirical-anchor problem volovik identifies (which is genuine).

**My honest answer: route 1 + route 2 in sequence.** Withdraw the two-slot framing for the immediate S92 W1 χ'_weight registry landing (route 1); separately propose the OP-PROJ sub-suffix extension as a K=1 SUGGESTION methodology rule at S92+ via dedicated rule-extension workshop (route 2). This routes the χ'_weight canonical-weight verdict away from the two-slot inadmissible framing.

The remaining question — given route 1 (no two-slot landing) — is: **outcome (i) single canonical or outcome (iii) OPEN registry slot?** This routes via Q-FINAL-VLV-2 below.

**Q-FINAL-VLV-2 (Wedderburn-formula image relation: does `5/14 = rank²-image(3/6)` collapse SIMULTANEOUS-VALIDITY?)**.

This is the substantive workshop question. I owe a clean substrate-IS substitution-chain answer.

**Substitution chain (Wedderburn-formula image relation under `χ'`)**.

```
Step 1 (Definitions).
  Wedderburn formula on a finite *-algebra:
    For each simple summand M_n(D) of A_K, dim_HS(M_n(D)) = n² · dim(D).
    For A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) over ℝ (with ℍ ⊗_ℝ ℂ ≅ M_2(ℂ)):
      rank(ℂ) = 1,         dim_HS(ℂ) = 1² = 1
      rank(ℍ) = 2,         dim_HS(ℍ_ℂ) = 2² = 4
      rank(M_3(ℂ)) = 3,    dim_HS(M_3(ℂ)) = 3² = 9
    Total rank(A_K) = 1+2+3 = 6;  dim_HS(A_K) = 1+4+9 = 14.

  Inheritance morphism χ' : A_K → M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ);
    ker(χ'|_{M_3(ℂ)}) = M_3(ℂ) entire (S89 §W2-3 derived theorem,
    NPZ audit_sha256 90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843);
    χ' faithful on ℂ ⊕ ℍ.

  Two ratios:
    R_K(χ') := (rank ℂ + rank ℍ) / rank(A_K) = 3/6  [K-class-rank-mass-fraction]
    R_Tr(χ') := (dim_HS ℂ + dim_HS ℍ) / dim_HS(A_K) = 5/14  [Hilbert-trace-mass-fraction]

Step 2 (Algebraic image relation under Wedderburn formula).
  By direct application of the Wedderburn formula summand-by-summand:
    dim_HS(image_χ') = dim_HS(ℂ) + dim_HS(ℍ) = 1² + 2² = 1 + 4 = 5
    dim_HS(A_K) = 1² + 2² + 3² = 1 + 4 + 9 = 14
  The squaring operation rank_i ↦ rank_i² takes (1, 2, 3) → (1, 4, 9)
  and the corresponding partial sums (3, 6) → (5, 14).

  Volovik's algebraic image relation:
    R_Tr(χ')  =  Σ_{i ∈ image} rank_i² / Σ_i rank_i²
              =  (rank ℂ)² + (rank ℍ)² / [(rank ℂ)² + (rank ℍ)² + (rank M_3(ℂ))²]
              =  R_K(χ')-IMAGE via summand-by-summand rank² squaring.
  This IS an algebraic identity holding on A_K's structure constants
  before any morphism is applied — the rank vector (1, 2, 3) of A_K
  ALWAYS images to (1, 4, 9) under rank² regardless of χ'.

Step 3 (What the algebraic identity does NOT say).
  The image relation in Step 2 says:
    "Given the substrate algebra A_K with rank vector (1, 2, 3),
     the corresponding dim_HS vector is (1, 4, 9) by Wedderburn formula."
  It does NOT say:
    "The functorial invariant of χ' is unique."
  It does NOT say:
    "5/14 is computed from 3/6 by some functorial operation under χ'_*."

  Two distinct functorial invariants of the SAME χ' on the SAME A_K
  remain non-fungible:
    (a) K_0(χ'_*): preserves K-class-rank; image-rank/total-rank = 3/6.
    (b) Tr_{H_K}(χ'-restriction): preserves Hilbert-trace mass on the
        regular representation; image-trace-mass / total-trace-mass = 5/14.

  Both are simultaneously substrate-IS facts about the same χ'. The
  Wedderburn formula gives the algebraic relation BETWEEN the two
  ratios when both are computed on A_K's rank vector — it does NOT
  identify them under any functor.

Step 4 (The categorical-identity question survives).
  The Wedderburn image relation guarantees: any χ'-preserving map on
  the (b)-side Hilbert-trace will give 5/14 if and only if the
  corresponding (a)-side K-rank preservation gives 3/6 on the SAME
  rank vector. The two are LOCKED IN STEP arithmetically on A_K's
  structure constants.

  But the CANONICAL-IDENTITY of χ'_weight (which one IS the
  multiplicative pre-factor of R_universal in α'(M_LRD)?) is
  determined by the EVALUATOR (CM-1995 §III.4 residue formula's
  Tr or the K_0 functor), NOT by the algebraic image relation.

  - If the evaluator is the K_0(A_K) → K_0(target) functor, the
    canonical pre-factor IS 3/6.
  - If the evaluator is the CM-1995 §III.4 regular-representation
    trace on H_K, the canonical pre-factor IS 5/14.

  The Wedderburn formula tells us 3/6 and 5/14 are LINKED at the
  algebra-structure-constants layer; it does NOT tell us which
  evaluator α'(M_LRD) prescribes.

Step 5 (Direction from canonical form).
  The image relation R_Tr = rank²-image(R_K) HOLDS as a substrate-IS
  algebraic identity on A_K. The two ratios are derivable from each
  other knowing the rank vector. This DOES collapse the SIMULTANEOUS-
  VALIDITY framing in the sense that the two ratios are not
  CATEGORICALLY INDEPENDENT — they are LOCKED IN STEP under the
  rank² squaring on A_K's individual summands.

  But this does NOT collapse the canonical-weight QUESTION into a
  single answer at the upstream K-rank layer. The image relation
  gives one ratio from the other arithmetically; the canonical-
  weight question asks WHICH ratio IS the multiplicative pre-factor
  of R_universal in α'(M_LRD) — and that question is about the
  EVALUATOR, not about the rank vector.
```

**Substrate framing**: the substrate IS the rank-(1,2,3) Wedderburn-decomposable algebra `A_K`; the Wedderburn-formula image relation IS a substrate-IS algebraic identity on `A_K`'s structure constants; the two ratios `3/6` and `5/14` are LOCKED IN STEP at the substrate-algebra layer per the rank² → dim_HS squaring. Direction substrate → emergent: the algebraic identity governs the rank vector ALWAYS; the canonical-weight question downstream concerns WHICH evaluator α'(M_LRD) uses; the evaluator choice is a separate substrate-IS structural specification (per `§VII.AF.1.OP-PROJ` bridge map citation HKR ∘ Connes-Karoubi pairing on CM-1995 §III.4 residue formula).

**Direct answer to Q-FINAL-VLV-2**: I accept the Wedderburn-formula image relation `dim_HS(M_n(ℂ)) = n²` is the substrate-IS algebraic identity taking K-rank to dim_HS (Step 1-2). I CONCEDE this DOES weaken the SIMULTANEOUS-VALIDITY framing's "two CATEGORICALLY INDEPENDENT invariants" claim — the two ratios are LOCKED IN STEP arithmetically, NOT independent. But I PARTIALLY contest that the image relation COLLAPSES the canonical-weight question into a single canonical at the upstream K-rank layer (Step 3-4). The canonical-weight question is about WHICH EVALUATOR α'(M_LRD) prescribes, not about whether the rank vector is the upstream object. The Wedderburn formula tells us 3/6 and 5/14 are linked algebraically; it does NOT tell us which is the multiplicative pre-factor in α'(M_LRD)'s decomposition.

**The honest reframe**: the categorical-independence claim in my Re:V1/V3 EMERGES tabulation was over-strong. The two ratios are *algebraically locked* (per Wedderburn formula), but they remain *functorially distinct* (one is a K_0-functor invariant; the other is a Tr-functor invariant). The χ'_weight canonical-weight question is about which FUNCTOR α'(M_LRD)'s evaluator IS, not about whether the rank vector is upstream of the dim_HS vector. The image relation Volovik surfaces is structurally important — and is itself a substantive workshop discovery I missed in R1 — but it does not resolve the canonical-weight question by itself.

This routes the workshop verdict to: **outcome (iii) OPEN registry slot** as the honest verdict at S91-close, with explicit substrate-physics carry-forward to S92+ Stage-2 cross-axis verify dispatch on which evaluator-functor α'(M_LRD) prescribes (connes-ncg + mack-cosmic-bridge per C-vdd-7). NOT outcome (ii) two-slot framing (withdrawn per C-vdd-11), NOT outcome (ii) layer-decomposition SIMULTANEOUS-VALIDITY framing (weakened per Q-FINAL-VLV-2 step 5).

**Q-FINAL-VLV-3 (cross-link audit as separate gate or in-line section)**.

I concur the cross-link audit is structurally required as part of S92+ χ'_weight canonical-weight registry landing per Volovik's E-3.

**Recommendation: separate gate `S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT` dispatched after (or alongside) the canonical-weight landing**, NOT in-line within the canonical-weight registry entry.

Rationale:
1. **Separation of concerns**: the canonical-weight verdict landing answers "what IS χ'_weight"; the cross-link audit answers "which §VII slots consume a χ'_weight factor". The two are structurally orthogonal; collapsing them into one in-line section conflates the substantive verdict (what χ'_weight IS) with the propagation analysis (where χ'_weight is consumed).
2. **Audit scope**: the cross-link audit must survey ALL §VII slots for χ'-consumption (§VII.AV W-1 result; §VII.AY; §VII.AZ; potentially others). This is a registry-scan task on mack-cosmic-bridge's sole-write authority, distinct from the substantive canonical-weight derivation task.
3. **Carry-forward audit dispatch**: even under outcome (iii) OPEN registry slot at S92, the cross-link audit is still required (because §VII.AV's W-1 result is a FWD-C2 candidate that may consume a χ'_weight factor regardless of which canonical wins). The audit dispatch is structurally orthogonal to the canonical-weight verdict's STAGE-1-CANDIDATE-OPEN tag.

**Pre-registered gate spec for `S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT`** (carry-forward 4-field):

- **What**: enumerate ALL §VII slots in `permanent-results-registry.md` that consume a χ'-restriction, χ'-pullback, or analog inheritance-morphism factor in their substrate-IS observable or laboratory-IN observable specification (5-anatomy element 1 OR element 2). For each consuming slot, document either (a) NO-DELTA where no χ'_weight multiplicative factor appears in the slot's decomposition, OR (b) CROSS-LINK-DELTA where the slot's multiplicative pre-factor IS a χ'_weight factor that propagates from the S91 W-2 χ'_weight canonical-weight verdict (whether that verdict is outcome (i), (ii), or (iii)).
- **Inputs**: `sessions/permanent-results-registry.md` (read-only scan); `sessions/archive/session-91/workshops/s91-w2-chi-prime-weight-canonical-substrate-derivation.md` (workshop verdict text); canonical_constants.py (cross-check against any pinned χ'-derived constants).
- **Gate**: PASS iff (a) all §VII slots reviewed; (b) each receives explicit NO-DELTA or CROSS-LINK-DELTA classification with substrate-IS justification; (c) any CROSS-LINK-DELTA classification carries explicit dependency on S91 W-2 verdict (cite the workshop's verdict-line audit_sha256). FAIL if any §VII slot is left unclassified.
- **Effort**: ~0.5 wave-equivalents (registry-scan + mack-cosmic-bridge classification). Single dispatch; mack-cosmic-bridge sole-writer.

This routes cleanly into S92+ alongside the substantive canonical-weight resolution.

### DISSENT

I CONCEDE D-1 (layer-functor mis-citation; my Re:V1/V3/V4 invocations of `epistemic-discipline.md §"Layer-Decomposition"` as authority for intra-substrate K_0/Metric stratification do not survive a careful read of the rule) per C-vdd-10 above. I CONCEDE D-3 (OP-PROJ sub-suffix axis lacks K=3 MANDATORY rule backing) per C-vdd-11 above. I sharpen — not retract — my position on D-2 (α'(M_LRD)'s evaluator-canonical question), and I sharpen the categorical-scope of the Wedderburn-formula image relation per Q-FINAL-VLV-2.

**D-vdd-1 (response to Volovik's D-2; sharpened, not repeated).**

Volovik's D-2 argues α'(M_LRD)'s multiplicative decomposition `R_universal · χ'_weight · (M_KK/M_Pl)² · g` requires BOTH the K_0-rank-layer (3/6 as the categorical inheritance-restriction invariant per 3HeB-inheritance parallel) AND the Metric-layer (5/14 as the residue-trace mass-fraction), not one or the other. Volovik's positive claim is then: the χ'_weight factor IS a Kasparov-KK functorial invariant of `χ'`, NOT a residue-formula evaluation; per the 3HeB-inheritance-canonical.md Step 3 parallel (`rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2`, Hodgkin theorem), the canonical inheritance-restriction quantity is the K-class-rank invariant 3/6.

I sharpen my disagreement on two narrow points and concede one boundary point.

**(a) Boundary point I CONCEDE to Volovik**.

The decomposition `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g` is structurally a PRODUCT of factors at distinct categorical sources. The four factors come from STRUCTURALLY DIFFERENT operations per Volovik's D-2 enumeration (workshop line 1483-1486):

- `R_universal` = unrestricted Connes-Karoubi pairing at the W-5 baseline (CM-1995 §III.4 residue formula evaluation). ✓ This IS a residue-formula evaluation.
- `χ'_weight` = inheritance-restriction weight from `χ' : A_K → M_2(ℂ) ⊗ Cl(1)` Kasparov KK projection. ✗ This is categorically a Kasparov-KK functorial invariant of `χ'`, NOT a residue-formula evaluation in its OWN right.
- `(M_KK/M_Pl)²` = dimensional bridge factor. Not residue evaluation.
- `g(M, L=10)` = horizon-projector saturation. Not residue evaluation.

I concede Volovik's framing here: the multiplicative decomposition is a product of four structurally distinct factors, and `χ'_weight` AS A FACTOR is categorically a Kasparov-KK functorial invariant of `χ'`, NOT itself an evaluation of the residue formula. My R1 Re:V1 argument over-extended by reasoning "α'(M_LRD)'s evaluator IS the CM-1995 §III.4 residue formula, therefore χ'_weight IS the trace-mass-fraction" — this conflated the EVALUATOR of the unrestricted `R_universal` baseline with the EVALUATOR of the `χ'_weight` FACTOR. The two are structurally distinct.

**(b) Sharpened disagreement (where my R1 position still stands)**.

But Volovik's positive claim — "the canonical inheritance-restriction quantity for `χ'` IS the K-class-rank-SUM-ratio invariant 3/6 by the 3HeB-inheritance parallel" — does not follow cleanly from the 3HeB inheritance morphism's K-theoretic identity alone. The 3HeB-inheritance-canonical's Hodgkin-theorem identity `rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2` is about the RANK COUNT DIFFERENCE between source and target K-theory under iota — i.e., how many K-classes are killed by iota. The analogous quantity for `χ'`:

```
rk K_*(A_K) − rk K_*(image χ')  =  rk(ℤ ⊕ ℤ ⊕ ℤ) − rk(ℤ ⊕ ℤ)  =  3 − 2  =  1.
```

This is the K-rank-class-COUNT difference (one K-class generator killed), NOT the K-rank-class-MASS-FRACTION ratio 3/6. The 3HeB-inheritance parallel structurally gives a count (1 killed class) or a difference (2 K-classes in source, 1 K-class killed); it does NOT structurally give a MASS-FRACTION ratio of the SUM-OF-RANKS-WEIGHTED form `(rank ℂ + rank ℍ) / (rank ℂ + rank ℍ + rank M_3(ℂ)) = 3/6`.

The choice "the multiplicative pre-factor of `R_universal` in `α'(M_LRD)` IS the K-rank-SUM-WEIGHTED ratio 3/6" requires an ADDITIONAL structural identification: that the canonical Kasparov-KK functorial invariant for the multiplicative-pre-factor role IS the K-rank-SUM-WEIGHTED ratio rather than (e.g.) the count-difference, the individual-class-survival pattern, or the L²-norm-pushforward. The 3HeB-inheritance parallel does NOT establish this. It establishes that `χ'` has K-class-rank invariants; it does NOT pin which K-class-rank invariant IS the multiplicative pre-factor.

**(c) The narrow residual contest**.

The substantive substrate-physics question that remains contested at workshop close is:

> Given that `χ'_weight` is structurally a Kasparov-KK functorial invariant of `χ'` (Volovik's framing per (a) above), and given that the K-rank-SUM-WEIGHTED ratio (3/6) and the Hilbert-trace-SUM-WEIGHTED ratio (5/14) are LOCKED IN STEP arithmetically on `A_K`'s rank vector via the Wedderburn-formula image relation (Volovik's Q-VLV-3 derivation per C-vdd-9 above), WHICH functorial invariant of `χ'` IS the multiplicative pre-factor of `R_universal` in `α'(M_LRD)`?

This question does not admit a derivation from any single existing rule. It requires either (i) a categorical-identification structural theorem on the Kasparov-KK formalism specifying which `χ'`-invariant IS the multiplicative pre-factor in a Hochschild-cocycle-pairing multiplicative decomposition, OR (ii) a substrate-physics convention pinning the choice by the bridge map's specification.

For (i): the existing van-den-Dungen Paper 01 (1811.07824) factorization theorem for the Kasparov product on submersions gives the **fundamental class decomposition** as a Kasparov product of shriek-map and base-class, BUT does not directly specify the multiplicative-pre-factor role of an inheritance-restriction morphism `χ'` on a Hochschild-cocycle pairing's multiplicative decomposition. The Paper 01 factorization is at the LEVEL of K-homology classes, not at the LEVEL of individual trace-pairings. The χ'_weight question is at the latter level (multiplicative decomposition of an individual trace-pairing value), which Paper 01 does not directly address. **I cannot supply a Paper 01-level structural theorem that pins which invariant IS the multiplicative pre-factor.**

For (ii): the W-5 baseline `§VII.AF.1.OP-PROJ` registry text specifies the bridge map (`HKR L_max → ∞ ∘ Connes-Karoubi pairing`) and the evaluator (CM-1995 §III.4 finite-spectral-triple residue formula `Tr(γ · cocycle · [F, cocycle]² · |D|^{-2s})`). The unrestricted `R_universal` is computed by this evaluator. When `χ'` is composed with this evaluator (via `χ'^* [φ_g^{sym}]` pullback of the cocycle through `χ'`), the COMPOSITION evaluation's trace-mass at every dim-spec pole IS 5/14 of the unrestricted trace (T1.9 pole-by-pole identity verified at every pole in {0, 2, 4, 6, 8}). This convention reading routes `χ'_weight` to 5/14.

Volovik's reading routes `χ'_weight` to 3/6 by a separate convention reading: that the multiplicative pre-factor IS the K-class-rank-SUM-WEIGHTED ratio invariant of `χ'` regardless of the evaluator's algebra-trace structure.

**Both convention readings are substrate-IS arguable; neither has a structural theorem at the cited rule-file layer that uniquely pins the choice**. The honest workshop verdict at this disagreement is **outcome (iii) OPEN registry slot**, pre-registering the categorical-identification question for S92+ Stage-2 cross-axis verify (connes-ncg + mack-cosmic-bridge), NOT outcome (i) Reading 1 canonical and NOT outcome (ii) two-slot or layer-decomposition framing.

**D-vdd-2 (categorical-scope sharpening on the Wedderburn-formula image relation per Q-FINAL-VLV-2).**

I concede the Wedderburn-formula image relation `dim_HS = Σ rank_i² · dim(D_i)` is a substrate-IS algebraic identity on `A_K`'s structure constants per C-vdd-9 above. I sharpen the categorical-scope.

The image relation says: on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` with rank vector `(1, 2, 3)`, the dim_HS vector is `(1, 4, 9)` by summand-by-summand `rank² · dim(D)` squaring; partial sums `(3, 6)` ↦ `(5, 14)`. This is an algebraic identity ON `A_K`, holding before any morphism is applied.

The image relation does NOT say:
- "The Kasparov-KK functor `χ'_*` on `K_0(A_K)` has output computable from the regular-representation trace functor on `H_K`." (`χ'_*` is its OWN functor; the trace functor is distinct.)
- "The trace-mass-fraction is a derived form of the K-rank-mass-fraction under some natural transformation between K_0 and Tr functors." (No such natural transformation is canonical; the two functors are categorically distinct on the operator-algebra category.)
- "5/14 is canonically defined IN TERMS OF 3/6 under any functor that `χ'` participates in." (The Wedderburn formula relates the two ratios on the SAME rank vector, not under any functor.)

Volovik's Q-VLV-3 framing line 1611-1612 — "any morphism that preserves K-class-rank ALSO preserves the dim_HS-image of K-class-rank (by direct application of the Wedderburn formula)" — is correct ONLY in this restricted sense: if `χ'` preserves K-class-rank-MASS-FRACTION 3/6 (which it does as a Kasparov-KK projection), AND if the source and target algebras have rank vectors satisfying the Wedderburn formula (which they do), THEN the corresponding dim_HS-MASS-FRACTION on the source side IS 5/14 by algebraic substitution. **But this is the algebraic identity at the SOURCE side, NOT a functorial relation between source-side K-rank and source-side trace-mass under `χ'_*`.**

The functorial distinction: `K_0(χ'_*)` lives on the K-theory side; `Tr_{H_K}(χ'-restriction)` lives on the operator-algebra trace side; the two functors are categorically distinct EVEN ON THE SAME `χ'`. The Wedderburn-formula image relation tells us their OUTPUTS on `A_K`'s rank vector are arithmetically related; it does NOT tell us either ONE of them IS the canonical multiplicative pre-factor in `α'(M_LRD)`.

So my D-vdd-2 sharpening: **the Wedderburn-formula image relation WEAKENS the categorical-INDEPENDENCE claim in my R1 EMERGES tabulation — I withdraw that over-extension explicitly**. But the image relation does NOT COLLAPSE the canonical-multiplicative-pre-factor question into a single canonical at the upstream K-rank layer (Volovik's Q-FINAL-VLV-2 question). The two ratios remain *functorially distinct* (one is a K_0-functor invariant under `χ'_*`; the other is a Tr-functor invariant under `χ'`-restriction) even though they are *algebraically locked* (related by Wedderburn formula on the rank vector). The canonical-weight question survives the image relation; it requires either a Paper 01-level structural theorem (which I cannot supply per D-vdd-1(c)) or a substrate-physics convention pin (which Volovik and I read differently per D-vdd-1(c)).

This is the substantive residual workshop dissent: Volovik reads the canonical multiplicative pre-factor as the K_0-functor invariant 3/6 by the 3HeB-inheritance parallel; vdd reads it as the Tr-functor invariant 5/14 by the W-5 baseline bridge-map specification's prescribed evaluator. Neither reading has dispositive rule-file backing. The honest verdict at S91-close is OPEN.

**D-vdd-3 (positive structural proposal that does not require either side to win)**.

The Wedderburn-formula image relation is itself a substantive substrate-physics theorem on `A_K` that the workshop has surfaced. Independent of the canonical-weight verdict outcome, the image relation is a permanent framework contribution and should land in the registry as a NEW substrate-physics identity, decoupled from the canonical-weight verdict slot.

Proposed §VII slot landing (independent of S91 W-2 canonical-weight verdict outcome):

- **`§VII.{next-free}.OP-PROJ` (provisionally `§VII.BA.OP-PROJ`; final slot identifier determined by mack-cosmic-bridge at S92 W1 landing time per the methodology-wave-allowlist append protocol)**: "Wedderburn-formula image relation on inheritance-restricted Hochschild-cocycle pairings for `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`." Substrate-IS observable: the algebraic identity `dim_HS(image_χ')/dim_HS(A_K) = (Σ rank_i² · dim_D_i)|_{i ∈ image} / (Σ rank_i² · dim_D_i)|_{all i}` evaluated on `A_K`'s rank vector under any K-class-rank-preserving morphism. The identity is L_max-INDEPENDENT (algebraic on structure constants); regulator-INVARIANT; holds at every L_max.
- **Level-1 (cohomology-class identity)**: the rank² → dim_HS squaring is a structural identity on `A_K` (Wedderburn-Artin theorem applied summand-by-summand). Holds at the substrate-algebra structure-constants layer.
- **Level-2 (algebraic envelope)**: trivially L_max-INDEPENDENT (the identity holds at every finite L_max and at L_max → ∞ identically). Level-2-binding via direct algebraic identity on `A_K`.
- **Level-3 (empirical anchor)**: arithmetic identity at machine epsilon (Sage-rational exact). `(3, 6) ↦ (5, 14)` verified by direct computation; PASS.
- **Bridge map**: NONE in the cross-pillar sense (the identity holds on the substrate algebra itself, independent of any cross-pillar bridge). This makes the slot INTRA-PILLAR (Pillar I / A_K-internal), NOT a cross-pillar bridge per `cross-pillar-bridge-anatomy.md` 5-anatomy structure. The slot lands as a substrate-algebra structural identity, NOT as a cross-pillar bridge anatomy element.

This proposal can land at S92 W1 (or wherever the planner schedules it) INDEPENDENT of the canonical-weight verdict — outcome (i), (ii), or (iii) on the canonical weight does NOT prevent the Wedderburn-image-relation slot from landing as a substrate-physics structural identity. **mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.** This is E-vdd-1 below promoted to a registry-landing proposal.

### EMERGENCE

Three structural insights surfaced through R1+R2 exchange that did not exist in the seed-w2-w3.md investigator brief, in V1-V5, in Re:V1-V5 / D1-D3, in V's C/D/E/Q-R2, or in any individual round. I record them as the workshop's substantive new content, separate from the contested canonical-weight verdict.

**E-vdd-1 (Wedderburn-formula image relation `dim_HS = Σ rank_i² · dim(D_i)` on `A_K` is a substantive substrate-physics theorem that lands INDEPENDENT of the canonical-weight verdict)**.

The image relation surfaced in Volovik's Q-VLV-3 answer (workshop lines 1604-1613) is structurally important and deserves its own §VII registry slot independent of the canonical-weight resolution. Per D-vdd-3 above, this is the proposed `§VII.{next-free}.OP-PROJ` "Wedderburn-formula image relation on inheritance-restricted Hochschild-cocycle pairings" slot — substrate-algebra-internal (no cross-pillar bridge anatomy), L_max-INDEPENDENT, Sage-rational exact, regulator-INVARIANT.

The substrate-physics content: the algebraic identity `(rank ℂ + rank ℍ) / rank A_K = 3/6` and `(dim_HS ℂ + dim_HS ℍ) / dim_HS A_K = 5/14` are NOT independent computations — they are LOCKED IN STEP by the Wedderburn-Artin theorem's summand-by-summand rank² squaring on `A_K`'s structure constants. This is a permanent framework contribution that should be documented as a substrate-algebra structural identity regardless of which canonical-weight outcome S92 selects.

**Substrate framing**: the substrate IS the rank-(1,2,3) Wedderburn-decomposable algebra `A_K`; the image relation IS a substrate-IS algebraic identity on `A_K`'s structure constants; ANY K-class-rank-preserving morphism on `A_K` induces a corresponding dim_HS-preserving relation under the rank² squaring; direction substrate → emergent (the algebraic identity on `A_K`'s rank vector governs the dim_HS vector ALWAYS; downstream functorial-invariant choices route to different multiplicative pre-factors at the bridge-map evaluation, but the upstream algebraic identity is the substrate-IS lock).

This emergent insight is the workshop's most permanent contribution; outcome of the canonical-weight verdict is downstream.

**E-vdd-2 (four-axis discriminator structure (α, β, γ, δ) is K=1 SUGGESTION rule-extension candidate; not yet MANDATORY)**.

Volovik's E-2 enumerates the four-axis structure I proposed in Re:V4 §"MISSED (axis (δ): evaluator-trace-layer vs K_0-rank-layer axis)" (workshop line 854-862) as a candidate K-counter advancement for an intra-Cell-I within-cell adjudication rule extension. I concur with Volovik's framing at K=1 SUGGESTION status:

- (α) K-theoretic vs representation-theoretic axis
- (β) Source-side vs target-side axis
- (γ) Primary corridor (b) vs auxiliary corridor (c) axis
- (δ) Evaluator-trace-layer vs K_0-rank-layer axis (vdd R1 contribution)

The four-axis discriminator structure is genuinely new. The existing algebra-axis orthogonality K=3 MANDATORY clause (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) operates at the *cross-cell* axis (Cell I / II / III / IV partition); it is silent on *within-cell* discrimination. The four-axis structure operates at the *within-cell* level — discriminating among multiple substrate-IS observables that all parse to the same corner cell.

I concur with Volovik's K=1 SUGGESTION classification (workshop line 1558-1560) for the four-axis structure: the χ'_weight workshop IS the FIRST instance in the framework's corpus where within-cell discrimination is needed for canonical-weight adjudication. Per `feedback_rules-compensate-missing-structure.md` K-counter threshold (K=3 distinct calibration instances for SUGGESTION → MANDATORY promotion), the four-axis discriminator should land at K=1 SUGGESTION at workshop close — NOT MANDATORY.

I concur with Volovik's proposed forward calibration corpus expansion expectation: K=2 at the next within-cell canonical-weight workshop; K=3 MANDATORY at the third. **No pre-commitment of the χ'_weight verdict to vdd's outcome (ii) framing**. This is a methodology-rule extension proposal at K=1 SUGGESTION, NOT a structural authority that pre-commits S91 W-2's verdict.

The honest registry-landing for E-vdd-2: a methodology-rule extension proposal at `cross-pillar-bridge-anatomy.md §"Within-cell discriminator axes"` (new sub-section) at K=1 SUGGESTION; explicit forward calibration corpus expansion expectation. **This is a separate registry/rule-extension dispatch, NOT a load-bearing argument for the χ'_weight canonical verdict**.

**E-vdd-3 (cross-link audit `S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT` as carry-forward; mack-cosmic-bridge sole-writer)**.

Volovik's E-3 raised the cross-link audit requirement: the S92+ χ'_weight canonical-weight registry landing should audit all §VII slots for χ'-consumption and document either NO-DELTA or CROSS-LINK-DELTA per consuming slot. I concur per Q-FINAL-VLV-3 answer above with the recommendation that the audit lands as a SEPARATE gate (not in-line within the canonical-weight registry entry).

The audit dispatch is structurally orthogonal to the canonical-weight verdict (it is required regardless of outcome (i), (ii), or (iii) on the canonical weight). mack-cosmic-bridge is the natural sole-writer per `feedback_mack-bridge-role.md`. The carry-forward 4-field spec is documented in the Wrap-Up §"Carry-Forward Computations" below.

**E-vdd-4 (NEW; the substantive workshop framing of the canonical-weight question requires a categorical-identification structural theorem that Paper 01 does not currently supply)**.

This is a NEW structural insight I missed in R1 and that surfaced through Volovik's D-2 sharpening of the substantive disagreement (workshop line 1488-1494). The substantive question at workshop close is NOT "which substrate-IS invariant of `χ'` is canonical" (settled per C-vdd-8: BOTH are substrate-IS invariants of the same Kasparov KK projection) and NOT "are the two invariants categorically independent" (settled per Q-FINAL-VLV-2: they are LOCKED IN STEP arithmetically via the Wedderburn-formula image relation). The substantive question is:

> Which functorial invariant of `χ'` IS the canonical multiplicative pre-factor of `R_universal` in `α'(M_LRD)`'s decomposition?

This question is at the level of "which functor IS the canonical pre-factor functor when an inheritance morphism enters a Hochschild-cocycle-pairing multiplicative decomposition?" — and this is a categorical-identification question that does NOT have a structural-theorem-level answer at the existing van-den-Dungen Paper 01 (1811.07824) factorization theorem for the Kasparov product on submersions. Paper 01 factorizes the FUNDAMENTAL CLASS of a submersion; it does not specify the multiplicative-pre-factor role of `χ'`-restriction on a Hochschild-cocycle multiplicative pairing.

**This is itself a substantive observation about the framework's current foundational scope**: a structural theorem at the categorical-identification layer for inheritance-morphism multiplicative pre-factors is MISSING. The χ'_weight canonical-weight question is the first framework instance where this missing theorem materially affects a registry landing. The S92+ Stage-2 cross-axis verify dispatch (connes-ncg-theorist at Axis-A; mack-cosmic-bridge at Axis-B) is the appropriate forum to either (a) produce the missing categorical-identification structural theorem on a Paper 01-style factorization extension, or (b) declare the question pinning by substrate-physics convention (W-5 baseline bridge-map evaluator convention OR 3HeB-inheritance K-rank-SUM-WEIGHTED ratio convention) at STAGE-1-CANDIDATE.

This emergent observation deserves explicit carry-forward as a methodology-floor task for S92+ (alongside the substantive substrate-physics resolution): the framework's foundational scope for inheritance-morphism multiplicative pre-factors needs to be extended either by a new structural theorem or by explicit convention pinning. This is `S92-CHI-PRIME-WEIGHT-CATEGORICAL-IDENTIFICATION-FOUNDATION`, a foundational-layer gate distinct from the substantive S91 W-2 verdict.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (a) Canonical χ'_weight identity (Wedderburn-RANK vs HS-DIM) | V1, Re:V1, R2 D-2, R2-B D-vdd-1 | **Dissent** | Both 3/6 (K_0-functor invariant) and 5/14 (Tr-functor invariant on H_K) are substrate-IS invariants of the same Kasparov KK projection χ' (C-1 + C-vdd-1 settled); the categorical-identification question — which functor IS the canonical multiplicative pre-factor of R_universal in α'(M_LRD) — survives R2-B and lacks dispositive rule-file backing. Volovik reads 3/6 canonical via 3HeB-inheritance parallel; vdd reads 5/14 canonical via W-5 baseline bridge-map evaluator. Verdict: **outcome (iii) OPEN registry slot** at S91-close. |
| 2 | (b) Modified-universal-kernel γ(s) shift | V2, Re:V2, R2 C-2, R2-B C-vdd-2 | **Converged** | The (c)∘(d) γ(s)≠Γ(s) corridor IS structurally distinct from the (b)∘(d) χ'-pullback corridor at the Kasparov-product factorization layer (Paper 01 / 1811.07824 unbounded-KK theorem); c_aux=1/3 is substrate-Wedderburn-fixed by `(1−2+3)/6`; (1−γ_Euler/3) is `structurally-IRRATIONAL-per-CC2-analog` at substrate-distance-1 pole; SIMULTANEOUS-VALIDITY at the (b)/(c) corridor-decomposition level is settled. Canonical-weight contest is intra-(b)-corridor only. |
| 3 | (c) Inheritance morphism χ': A_K → M_2(ℂ) faithfulness | V3, Re:V3, R2 C-3, R2-B C-vdd-3 | **Converged** | S89 §W2-3 derived theorem (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`) is uncontested: χ' kills M_3(ℂ) entire (Wedderburn 9 > 8 + Schur orthogonality; machine-epsilon witness `chi_prime_pullback_machine_eps_PASS = True`); faithful image is ℂ ⊕ ℍ (source K-rank 3 of 6, source Hilbert-dim 5 of 14). The faithfulness fact is settled; only which weight invariant on the faithful image enters α'(M_LRD) remains contested (per row 1). |
| 4 | (d) Algebra-axis orthogonality K=3 constraint | V4, Re:V4, R2 C-4, R2-B C-vdd-4 | **Converged** | All three readings (and the D2 5/8 target-side candidate) parse to Cell I × s=3 via `permanent-results-registry.md §VII.U.2 clause (e)`. The K=3 MANDATORY orthogonality clause's conditions 1-4 are satisfied identically by all readings; the K-counter is structurally silent on within-cell weight choice. Within-cell discrimination requires a separate axis structure (see row 8). |
| 5 | Cross-cutting CF-37 retroactive reading + §VII registry | V5, Re:V5, R2 C-5/C-6/C-7, R2-B C-vdd-5/6/7 | **Converged** | (i) CF-37, T1.8, T1.9 verdict-line FAIL composites retain absolute permanence per `gate-verdicts.md §"Option A"` (no `supersedes=` tag needed; canonical-weight verdict does NOT contradict the empirical 1/458 FAILs); (ii) §VII.AF.1.OP-PROJ baseline (unrestricted W-5; R_universal=1.030902) and §VII.AU.OP-PROJ FWD-C1 (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) retain NO-DELTA under any outcome; (iii) Stage-2 cross-axis verify HARD-excludes volovik + vdd per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach; recommended Axis-A = connes-ncg-theorist, Axis-B = mack-cosmic-bridge. |
| 6 | D1: CM-1995 §III.4 residue trace IS canonical | D1, R2 D-2, R2-B D-vdd-1(a)+(b) | **Partial** | D1's pole-by-pole arithmetic (5/14 ratio at every dim_spec pole {0,2,4,6,8}; T1.9 Sage-rational identity) is uncontested. R2-B D-vdd-1(a) CONCEDES vdd's R1 framing over-extended: the residue formula evaluates `R_universal`, NOT the `χ'_weight` factor itself — `χ'_weight` IS structurally a Kasparov-KK functorial invariant of χ' in a STRUCTURED product, not a single residue evaluation. The categorical identity of WHICH functorial invariant IS the multiplicative pre-factor survives D1 and is OPEN. |
| 7 | D2: K-theoretic dim ratio as fourth candidate | D2 | **Partial** (Emerged → calibration corpus) | The target-side Hilbert-trace-dim ratio 5/8 = (dim_HS-image in target) / (dim_HS target) IS a substrate-IS Kasparov KK_0 bimodule invariant of χ', structurally distinct from V3-rejected 3/4 target K-rank ratio. Lands as **calibration-corpus annotation on the Wedderburn-image §VII slot (E-vdd-1)**, NOT as a competing canonical for α'(M_LRD)'s χ'_weight under the framework's pinned source-side CM-1995 §III.4 evaluator. Axes (β) source-side and (δ) evaluator-trace-layer downgrade 5/8 for the α'(M_LRD) pre-factor role; it remains documentation of Kasparov-bridge structural completeness. |
| 8 | C-vdd-9 / E-vdd-1: Wedderburn-formula image relation `dim_HS = Σ rank_i² · dim(D_i)` on A_K | Volovik Q-VLV-3 + R2-B C-vdd-9 + D-vdd-2 + E-vdd-1 | **Emerged** | NEW substrate-physics theorem on A_K's structure constants: the rank vector (1, 2, 3) images to dim_HS vector (1, 4, 9) via summand-by-summand rank² squaring; partial sums (3, 6) ↦ (5, 14). The two ratios `χ'_weight` candidates are **algebraically locked** at the substrate-algebra layer (NOT categorically independent at the rank-vector level). However, they remain **functorially distinct** (K_0(χ'_*) vs Tr_{H_K}(χ'-restriction)); the image relation does NOT collapse the canonical-multiplicative-pre-factor question. Lands as independent `§VII.{next-free}.OP-PROJ` substrate-algebra structural identity (intra-Pillar; no cross-pillar bridge). |
| 9 | C-vdd-10: Layer-Decomposition F rule citation withdrawn | R2 D-1, R2-B C-vdd-10 | **Converged** | vdd's R1 invocation of `epistemic-discipline.md §"Layer-Decomposition"` F-functor as authority for intra-substrate K_0/Metric stratification does NOT survive careful read: the rule's F is *cross-stratum* (substrate → methodology → audit), NOT intra-substrate. vdd's agent-memory "four-layer hierarchy" is a private organizing principle, not a rule. The intra-substrate K_0/Metric stratification stands or falls on substrate-physics merits without rule-file backing. |
| 10 | C-vdd-11 / E-vdd-2: OP-PROJ sub-suffix axis lacks K=3 MANDATORY rule backing | R2 D-3, R2-B C-vdd-11 + E-vdd-2 | **Emerged** | The proposed `-K0-LAYER` / `-METRIC-LAYER` sub-suffixes have NO precedent in the K=3 MANDATORY calibration corpus of `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (S87 W4-2 + S87 W6-1 + S87 W11-meta-2 — all OP-PROJ vs STATE-PROJ; no within-OP-PROJ sub-suffixes). vdd's R1 two-slot framing is **withdrawn**. The four-axis discriminator (α, β, γ, δ) lands as **K=1 SUGGESTION** rule-extension candidate at `cross-pillar-bridge-anatomy.md §"Within-cell discriminator axes"` (new sub-section); forward calibration corpus expansion K=2 / K=3 expected. |
| 11 | E-vdd-4: Categorical-identification structural theorem MISSING from Paper 01 factorization scope | R2-B E-vdd-4 | **Emerged** | The Paper 01 (1811.07824) Kasparov product factorization theorem factorizes the *fundamental class* of a submersion; it does NOT specify the multiplicative-pre-factor role of an inheritance-restriction morphism χ' on a Hochschild-cocycle-pairing multiplicative decomposition. The χ'_weight workshop is the FIRST framework instance where this missing categorical-identification theorem materially affects a registry landing. **The framework's foundational scope for inheritance-morphism multiplicative pre-factors is structurally incomplete** and queued as a methodology-floor carry-forward (`S92-CHI-PRIME-WEIGHT-CATEGORICAL-IDENTIFICATION-FOUNDATION`). |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **`S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT-RESOLUTION` (substantive substrate-physics carry-forward)**. Resolve the categorical-identification question: which functorial invariant of χ' IS the canonical multiplicative pre-factor of R_universal in `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g`? Two convention readings remain admissible:
   - **Reading 1 canonical (3/6)**: K-class-rank-SUM-WEIGHTED ratio via Kasparov-KK functoriality on K_0(A_K); 3HeB-inheritance parallel (`rk K_*(A_K) − rk K_*(A_He) = 2`, Hodgkin theorem) frames inheritance-restriction quantities as K-rank invariants.
   - **Reading 2 canonical (5/14)**: Hilbert-trace mass-fraction surviving χ' on the W-5 baseline bridge-map evaluator (CM-1995 §III.4 finite-spectral-triple residue formula's regular-representation trace on H_K).
   Gate criterion: STAGE-1-CANDIDATE registry landing per `joint-theorem-promotion.md` 4-stage pathway IF Stage-2 cross-axis verify (connes-ncg + mack-cosmic-bridge) produces convergent verdict on one reading; STAGE-1-CANDIDATE-OPEN-CHI-PRIME-WEIGHT-CANONICALIZATION tag with explicit substrate-physics carry-forward extension to S93+ IF Stage-2 produces residual dissent.

2. **`S92-WEDDERBURN-IMAGE-RELATION-REGISTRY-LAND` (independent substrate-physics theorem; outcome-decoupled)**. Land the Wedderburn-formula image relation `dim_HS(image_χ')/dim_HS(A_K) = Σ_{i ∈ image} rank_i² · dim(D_i) / Σ_i rank_i² · dim(D_i)` as a new `§VII.{next-free}.OP-PROJ` registry slot — substrate-algebra-internal structural identity (NOT cross-pillar bridge anatomy); Level-1 cohomology-class identity (Wedderburn-Artin theorem); Level-2-binding L_max-INDEPENDENT envelope; Level-3 Sage-rational exact at machine epsilon (`(3, 6) ↦ (5, 14)` verified). mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. Gate criterion: registry-landing PASS iff (i) the slot text declares the substrate-algebra-internal scope explicitly; (ii) the rank² → dim_HS squaring is documented summand-by-summand; (iii) the slot is structurally decoupled from the S91 W-2 canonical-weight verdict (lands at S92 regardless of outcome (i)/(ii)/(iii) on χ'_weight canonical).

3. **`S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT` (registry propagation gate; mack-cosmic-bridge sole-writer)**. Enumerate ALL §VII slots in `permanent-results-registry.md` that consume a χ'-restriction, χ'-pullback, or analog inheritance-morphism factor in their substrate-IS observable or laboratory-IN observable specification (5-anatomy element 1 OR element 2). For each consuming slot, classify as either (a) NO-DELTA where no χ'_weight multiplicative factor appears in the slot's decomposition (e.g., confirmed §VII.AF.1.OP-PROJ baseline + §VII.AU.OP-PROJ FWD-C1), OR (b) CROSS-LINK-DELTA where the slot's multiplicative pre-factor IS a χ'_weight factor that propagates from the S91 W-2 verdict. Candidate consuming slots: §VII.AV (W-1 result, FWD-C2 candidate, BdG-sector analog on Pillar V child realization), §VII.AY, §VII.AZ (pending registry-text scan). Gate criterion: PASS iff (i) all §VII slots reviewed; (ii) each receives explicit NO-DELTA or CROSS-LINK-DELTA classification with substrate-IS justification; (iii) any CROSS-LINK-DELTA classification carries explicit dependency on the workshop's verdict-line audit_sha256.

4. **`S92-CHI-PRIME-WEIGHT-CATEGORICAL-IDENTIFICATION-FOUNDATION` (methodology-floor; foundational-scope carry-forward)**. Address the missing categorical-identification structural theorem (E-vdd-4): which Kasparov-KK functorial invariant of an inheritance-restriction morphism IS the canonical multiplicative pre-factor when the inheritance morphism enters a Hochschild-cocycle-pairing multiplicative decomposition? Two structurally distinct forward routes: (i) extend van-den-Dungen Paper 01 (1811.07824) factorization theorem with a Hochschild-cocycle multiplicative-pre-factor specialization; (ii) declare substrate-physics convention pinning explicit at S92 with K=1 SUGGESTION status per `feedback_rules-compensate-missing-structure.md`. Gate criterion: a structural-theorem PASS (route (i)) requires a formal proof at the Paper 01-style KK factorization layer; a convention-pinning PASS (route (ii)) requires K=1 SUGGESTION landing in `cross-pillar-bridge-anatomy.md` or `registry-landing.md` (decided at landing-time).

5. **`S92-WITHIN-CELL-DISCRIMINATOR-AXES-K1-SUGGESTION` (methodology-rule extension; K=1 SUGGESTION landing)**. Land the four-axis discriminator structure (α / β / γ / δ) as a K=1 SUGGESTION rule extension at `cross-pillar-bridge-anatomy.md §"Within-cell discriminator axes"` (new sub-section). Axes: (α) K-theoretic vs representation-theoretic; (β) source-side vs target-side; (γ) primary corridor (b) vs auxiliary corridor (c); (δ) evaluator-trace-layer vs K_0-rank-layer. Forward calibration corpus expansion expectation: K=2 at the next within-cell canonical-weight workshop; K=3 MANDATORY at the third per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. Gate criterion: rule-extension landing PASS iff (i) the four axes are enumerated explicitly with substrate-physics definitions; (ii) the K=1 SUGGESTION status is declared explicitly (NOT MANDATORY); (iii) forward calibration corpus expansion expectation is documented at registry landing.

6. **`S92-OP-PROJ-SUB-SUFFIX-EXTENSION-K1-SUGGESTION` (methodology-rule extension; reserved for future S92+ K=1 SUGGESTION landing if structurally needed)**. The retroactively-withdrawn `-K0-LAYER` / `-METRIC-LAYER` two-slot framing was conceded inadmissible at R2-B per C-vdd-11. If a future workshop produces a within-OP-PROJ sub-suffix-axis discrimination need (e.g., a different inheritance-morphism structure where layer-distinct canonicals at different functorial sources are independently registry-eligible), the OP-PROJ sub-suffix discipline can be proposed as a K=1 SUGGESTION extension to `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`. This is reserved as a future placeholder, NOT a current S92 dispatch. Gate criterion: NOT-FIRING until a forward workshop instance materializes (the χ'_weight workshop's outcome (iii) OPEN verdict does NOT require this rule extension; outcome (i) Reading 1 canonical does NOT require it; an alternative outcome (ii) would require it only at K=1 SUGGESTION first-landing).

7. **`S92-W-1-RESULT-VII-AV-FWD-C2-CHI-PRIME-CROSS-LINK-AUDIT` (FWD-C2 candidate propagation sub-gate)**. Cross-link audit specific to §VII.AV (the W-1 workshop result; FWD-C2 candidate per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"` Pillar III/IV ↔ Pillar V): does the BdG-sector analog observable on the Pillar V child realization consume χ'_weight as a multiplicative factor? Per agent-memory snapshot, χ' is the structural bridge from Pillar III/IV (source) to Pillar V (BdG-sector target); the canonical-weight verdict on χ'_weight propagates IF §VII.AV uses the same `α'(M_LRD)`-style decomposition. Gate criterion: explicit NO-DELTA or CROSS-LINK-DELTA classification with substrate-IS justification; if CROSS-LINK-DELTA, cite the workshop verdict-line audit_sha256 explicitly. This is a sub-dispatch of `S92-VII-CHI-PRIME-WEIGHT-CROSS-LINK-AUDIT` (item 3) with §VII.AV-specific focus.

## Wrap-Up — Workshop Impact Summary

The workshop produced 11 settled or emergent structural conclusions on χ'_weight canonical substrate-derivation while leaving the core canonical-weight verdict OPEN at S91-close pending S92+ Stage-2 cross-axis verify.

### What Changed

**(a) Structural changes** (Volovik-Convention vs Connes-Convention scope-sharpening; per `output-standards.md §"Workshop Wrap-Up 'What Changed' — Numerical vs Structural Distinction"` Section (b)):

- **The χ' inheritance morphism on A_K is now known to carry FOUR distinct substrate-IS K-theoretic / trace invariants** — Source-side K-class-rank 3/6 (Reading 1, CF-37 K_0-functor invariant); Source-side Hilbert-trace-mass 5/14 (Reading 2, T1.9 CM-1995 §III.4 residue trace pushforward); Target-side K-class-rank 3/4 (V3-rejected); Target-side Hilbert-space-image-dim 5/8 (D2 candidate; Kasparov-bridge structural-completeness annotation). The four-way enumeration is a permanent framework contribution that lands as documentation regardless of canonical-weight verdict outcome.
- **The Wedderburn-formula image relation `dim_HS(M_n(D)) = n² · dim(D)` on A_K is a NEW substrate-physics theorem** surfaced through Volovik's Q-VLV-3 derivation: the K-rank ratio 3/6 and the Hilbert-trace ratio 5/14 are **algebraically locked in step** via summand-by-summand rank² squaring on A_K's structure constants. The two ratios are NOT categorically independent at the rank-vector layer; they remain functorially distinct under K_0(χ'_*) vs Tr_{H_K}(χ'-restriction). This image relation should land as its own `§VII.{next-free}.OP-PROJ` substrate-algebra structural identity (intra-Pillar; no cross-pillar bridge anatomy).
- **vdd's R1 layer-decomposition F-functor citation is retroactively withdrawn** (C-vdd-10): the rule's F is cross-stratum (substrate → methodology → audit), NOT intra-substrate; vdd's agent-memory "four-layer hierarchy" cannot serve as MANDATORY discipline backing for intra-substrate K_0/Metric stratification. The χ'_weight workshop is the FIRST framework instance where within-cell canonical-weight discrimination is needed; rule extensions must enter via K=1 SUGGESTION pathway per `feedback_rules-compensate-missing-structure.md`.
- **vdd's R1 two-slot `-K0-LAYER`/`-METRIC-LAYER` registry-landing framing is retroactively withdrawn** (C-vdd-11): no precedent in the K=3 MANDATORY calibration corpus of `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` for within-OP-PROJ sub-suffixes. The OP-PROJ sub-suffix discipline is reserved as a future K=1 SUGGESTION extension if a structural need materializes.

**(b) Numerical revisions** (none — verdict-line values unchanged):

- CF-37 (audit_sha256 `10ee072fe2c193f3...`), T1.8 (audit_sha256 `8ab158e9e45aab37...`), T1.9 (audit_sha256 `752a8f2b862a9aa5...`) verdict-line FAIL composites retain absolute permanence per `gate-verdicts.md §"Option A"`; no `supersedes=` tag is required (the canonical-weight verdict at S92+ resolves WHICH substrate-derivation IS canonical without modifying any verdict-line empirical value).

### What Holds

- **The S89 §W2-3 derived theorem (χ' kills M_3(ℂ) entire; faithful image = ℂ ⊕ ℍ; ker rank = 9)** — Wedderburn 9 > 8 + Schur orthogonality argument is structurally bullet-proof per machine-epsilon witness `chi_prime_pullback_machine_eps_PASS = True` (NPZ audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`). Both Volovik (V3) and vdd (Re:V3) concur fully (C-3 + C-vdd-3). The faithful-image identification is the load-bearing substrate-physics fact that survives the workshop unchanged.
- **The (b)-corridor and (c)-corridor are structurally orthogonal element-1 deformation columns** — the (c)∘(d) γ(s) ≠ Γ(s) modified-universal-kernel cannot reduce to the (b)∘(d) χ'-pullback corridor under the Kasparov-product factorization principle (Paper 01 / 1811.07824 unbounded-KK theorem; T1.8 Axis-B item 5). SIMULTANEOUS-VALIDITY at the (b)/(c) corridor-decomposition level is settled (C-2 + C-vdd-2). The (1−γ_Euler/3) digamma factor is `structurally-IRRATIONAL-per-CC2-analog`; the substrate-distance-1 corridor is structurally closed under all three readings (CF-37, T1.8, T1.9 all FAIL the 1/458 empirical anchor).
- **The K=3 MANDATORY algebra-axis orthogonality clause is silent on within-cell canonical-weight choice** — all three (and the 5/8 D2) readings parse to Cell I × s=3 via the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`; the K-counter neither selects nor excludes any reading. Within-cell discrimination requires a separate axis structure (the four-axis (α, β, γ, δ) discriminator at K=1 SUGGESTION; E-vdd-2).
- **The §VII.AF.1.OP-PROJ W-5 baseline (`R_universal = 1.030902`; unrestricted) and §VII.AU.OP-PROJ FWD-C1 (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION per S90 W1-15 deferred-pending re-tag) retain NO-DELTA under any canonical-weight verdict outcome** — the W-5 baseline is unrestricted (no χ'_weight consumed); §VII.AU.OP-PROJ's FWD-C1 parameterized slope_A canonical first-extraction (CF-65) is structurally orthogonal at the cross-pillar Hybrid Independence Test axes (i) + (ii) (Pillar I↔II vs Pillar III↔IV; n_s_FW vs LRD α-anchor) per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`.
- **The Stage-2 cross-axis verify HARD-exclude protocol on volovik + vdd** is settled per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach (S88 W-14 W4a-17 V.2 MANDATORY K=1). Recommended Axis-A = `connes-ncg-theorist` (NCG-axiomatic Wedderburn-Artin + Kasparov-KK depth); Axis-B = `mack-cosmic-bridge` (§VII registry sole-writer per `feedback_mack-bridge-role.md`).

### What Breaks or Strains

- **The categorical-identification structural theorem at the Paper 01 (1811.07824) Kasparov-product factorization layer is MISSING for the inheritance-morphism multiplicative-pre-factor role**. Paper 01 factorizes the fundamental class of a submersion at the KK-theoretic class layer; it does NOT specify which functorial invariant of an inheritance-restriction morphism χ' IS the canonical multiplicative pre-factor when χ' enters a Hochschild-cocycle-pairing multiplicative decomposition. The χ'_weight workshop is the FIRST framework instance where this missing theorem materially blocks a registry landing. **The framework's foundational scope for inheritance-morphism multiplicative pre-factors is structurally incomplete**; either a new Paper 01-style structural theorem extension or an explicit substrate-physics convention pinning is required at S92+ (E-vdd-4).
- **Two convention readings on χ'_weight canonical remain admissible at workshop close, neither with dispositive rule-file backing**. Volovik reads 3/6 canonical via the 3HeB-inheritance parallel (K-class-rank-SUM-WEIGHTED ratio as the categorical inheritance-restriction invariant); vdd reads 5/14 canonical via the W-5 baseline bridge-map evaluator (CM-1995 §III.4 residue formula's regular-representation Tr on H_K). Each reading has substrate-physics arguments at structural axes but lacks a dispositive theorem at the cited rule-file layer (D-vdd-1(c)). The honest verdict at S91-close is outcome (iii) OPEN registry slot, deferring the categorical-identification resolution to S92+ Stage-2 cross-axis verify.
- **The Wedderburn-formula image relation collapses the SIMULTANEOUS-VALIDITY framing's "two CATEGORICALLY INDEPENDENT invariants" claim**, but does NOT collapse the canonical-multiplicative-pre-factor question into a single canonical at the upstream K-rank layer. The two ratios are algebraically locked (per Wedderburn formula on A_K's structure constants) but remain functorially distinct (K_0-functor invariant vs Tr-functor invariant). This is a substantive sharpening of the workshop's scope: the canonical-weight question is not about "which invariant is upstream" (Wedderburn answers: both are at the same level on the rank vector) but about "which evaluator-functor IS canonical at the bridge-map evaluation" (which remains open).
- **The empirical 1/458 LRD α-anchor at substrate-distance-1 is structurally closed under all candidate readings**. NO Wedderburn-rank-admissible substrate-derivation reaches the χ'_weight ≈ 2.276 value required for empirical PASS at the dimensional bridge factor `(M_KK/M_Pl_reduced)² = 9.307286e-04`. The substrate-distance-1 corridor at the LRD α-anchor is therefore structurally closed under Reading 1 (3/6), Reading 2 (5/14), Reading 3 (~0.404 or ~0.288), AND Candidate 4 (5/8). The LRD α-anchor pursuit moves to substrate-distance-2 §VII.AX forward gates pre-registered at S91 W0 R5 — independent of the canonical-weight resolution.

### Carry-Forward Computations

**In-session cleanup 2026-05-22** (per user correction "only math carries forward; everything else is done at the time — rules are clear on this" + `feedback_fix-in-session-never-defer.md` + `Investigating-Workshops.md` §"is NOT" items 7-8): non-math framework-hygiene items (registry-text landings, rule-file extensions, cross-link audits) executed in-session and REMOVED from this list. Only genuine future-math computation remains as carry-forward below. In-session execution audit trail: `sessions/permanent-results-registry.md` §VII.BC.OP-PROJ Wedderburn-image registry land (mack); §VII.AV FWD-C2 chi'-weight cross-link audit NO-DELTA (mack); `.claude/rules/cross-pillar-bridge-anatomy.md` Within-cell discriminator axes (α/β/γ/δ) sub-clause (A1 connes-ncg-theorist); `computations/session-91/s91_gate_verdicts.txt` in-session verdict-line trios.

1. **`S92-CHI-PRIME-WEIGHT-CANONICAL-VERDICT-RESOLUTION`** (substantive substrate-physics; Stage-2 cross-axis verify dispatch):
   - **What**: Resolve the canonical multiplicative pre-factor of `R_universal` in `α'(M_LRD) = R_universal · χ'_weight · (M_KK/M_Pl)² · g`. Land STAGE-1-CANDIDATE registry entry at next-free §VII slot (provisionally `§VII.BA.OP-PROJ`; final slot identifier per mack-cosmic-bridge methodology-wave-allowlist append protocol) for the resolved canonical Reading 1 (3/6) OR Reading 2 (5/14) per the Stage-2 verdict. Alternatively (if Stage-2 produces residual dissent), land as STAGE-1-CANDIDATE-OPEN-CHI-PRIME-WEIGHT-CANONICALIZATION with substrate-physics carry-forward to S93+.
   - **Inputs**: this workshop document (S91 W-2 verdict + R1+R2+R2-B transcripts); `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`); `s90_w4_alpha_m_alt_corridor_d_compose_b.npz` (CF-37 baseline); `s91_w3_alpha_m_aux4_corridor_c_compose_d.npz` (T1.8); `s91_w3_alpha_m_full_cm1995_residue_d_compose_b.npz` (T1.9); `permanent-results-registry.md §VII.AF.1.OP-PROJ` baseline at line 14776 (W-5 calibration corpus instance #1); `permanent-results-registry.md §VII.AU.OP-PROJ` FWD-C1 deferred-pending at line 17784; canonical_constants.py (R_universal_HP1_strict_F4, eps_H_HP1_norm, M_KK, M_Pl_reduced, tau_fold, Delta_BCS).
   - **Gate**: (1) Registry-landing PASS iff the §VII slot text declares (a) 5 IS-not-IN anatomy elements per `cross-pillar-bridge-anatomy.md`; (b) 3-level structural-confidence ladder; (c) Level-1 single-τ-slice tag per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`; (d) SOURCE-DOUBLE-CITE-CO-PRIMARY structure (ANCHOR-1 = S89 §W2-3 derived theorem + ANCHOR-2 = K-theoretic OR CM-1995 §III.4 residue-trace canonical reading per Stage-2 verdict); (e) SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE tag per Hybrid Independence Test K-counter K=1 retention. (2) Stage-2 cross-axis verify PASS iff BOTH connes-ncg-theorist (Axis-A NCG-axiomatic) AND mack-cosmic-bridge (Axis-B cross-pillar registry sole-writer) independently PASS JOINT clauses on the canonical-weight reading; logical AND across two verdicts; PASS advances to STAGE-3-PERMANENT eligibility per `joint-theorem-promotion.md` 4-stage pathway. FAIL at either Axis blocks Stage-3; entry stays at STAGE-1-CANDIDATE-OPEN with substrate-physics carry-forward to S93+.
   - **Effort**: ~0.8 wave-equivalents total. Subtask split: registry landing ~0.3 we (mack sole writer); Stage-2 Axis-A (connes) cross-review ~0.3 we; Stage-2 Axis-B (mack) cross-review ~0.2 we. Both Stage-2 reviewers dispatched IN PARALLEL per `joint-theorem-promotion.md §"Stage 2"` protocol.
   - **Depends on**: workshop S91 W-2 verdict closure (this document); S89 §W2-3 NPZ; CF-37 / T1.8 / T1.9 NPZ artifacts (already landed); §VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ existing registry entries (no edit; cross-link only); canonical_constants.py pins.

2. **`S92-CHI-PRIME-WEIGHT-CATEGORICAL-IDENTIFICATION-FOUNDATION`** (methodology-floor; foundational-scope carry-forward):
   - **What**: Address the missing categorical-identification structural theorem (E-vdd-4): which Kasparov-KK functorial invariant of an inheritance-restriction morphism IS the canonical multiplicative pre-factor when the inheritance morphism enters a Hochschild-cocycle-pairing multiplicative decomposition? Two structurally distinct forward routes available: (i) extend van-den-Dungen Paper 01 (1811.07824) factorization theorem with a Hochschild-cocycle multiplicative-pre-factor specialization (formal proof at the Paper 01-style KK factorization layer); (ii) declare substrate-physics convention pinning explicit at S92 with K=1 SUGGESTION status per `feedback_rules-compensate-missing-structure.md`.
   - **Inputs**: van-den-Dungen Paper 01 (1811.07824; `researchers/Van-den-Dungen/01.md`) §3 factorization theorem; `cross-pillar-bridge-anatomy.md` 5-anatomy + 3-level structure; `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`; this workshop document E-vdd-4; the four invariants tabulation per E-1 (V → R2 + Re:V3 → R1).
   - **Gate**: Structural-theorem route (i) PASS iff (a) formal proof at Paper 01-style KK factorization layer is produced; (b) the canonical multiplicative-pre-factor functor is uniquely identified by the theorem. Convention-pinning route (ii) PASS iff (a) K=1 SUGGESTION landing in `cross-pillar-bridge-anatomy.md` or `registry-landing.md` is produced; (b) substrate-physics convention is documented with explicit forward calibration corpus expansion expectation. Failure of both routes routes to S93+ extension.
   - **Effort**: route (i) ~2.0 we (structural-theorem development; volovik + vdd HARD-excluded per Stage-2 protocol; structural-theorem reviewer pool = connes-ncg-theorist + lizzi-spectral-functional-theorist); route (ii) ~0.4 we (convention-pinning rule-extension landing).
   - **Depends on**: this workshop document (E-vdd-4 surfaces the missing theorem); van-den-Dungen Paper 01 full text; Stage-2 reviewer pool availability.

### Closing Line

The χ'_weight canonical-weight question requires a categorical-identification structural theorem — which Kasparov-KK functorial invariant of an inheritance morphism IS the canonical multiplicative pre-factor when the morphism enters a Hochschild-cocycle-pairing multiplicative decomposition — that the framework's current foundational scope (van-den-Dungen Paper 01 factorization theorem at the K-homology class layer) does NOT yet supply, leaving the S91-close verdict OPEN at outcome (iii) pending S92+ Stage-2 cross-axis verify on connes-ncg + mack-cosmic-bridge with volovik + vdd HARD-excluded.
