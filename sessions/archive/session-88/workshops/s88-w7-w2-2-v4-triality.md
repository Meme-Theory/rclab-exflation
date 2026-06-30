# Session S88 W7 Synthesis: §W2-2 V_4-on-triality-mod-2 D-W8-1 Collapse — Structural Closure vs L_max-Conditional Artifact

**Date**: 2026-05-07
**Agent**: connes-ncg-theorist (solo review)
**Source Documents**:
- `sessions/archive/session-88/session-88-w2-workingpaper.md` (1168 lines; gate §W2-2 lines 146–263; gate §W2-1 lines 7–143; gate §W2-3 lines 267–379; gate §W2-10 lines 820–878)
- `sessions/session-plan/session-88-plan-w2.md` (889 lines; plan §W2-2 lines 113–159)
- `sessions/archive/session-88/workshops/_seed-w2.md` (Workshop 1 spec lines 12–22; carry-forwards CF-W2-ADDITIONAL-A/B lines 28–38)
- `computations/session-88/s88_gate_verdicts.txt` (verdict line for §W2-2 audit_sha256=`4a23fbbb2f6d073e…`; FAIL with `max_delta=9.758e+01`, `sip_M=+8`, `sip_C=+8`, `sip_H=+20`)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`
- Sage-QQ enumeration (this synthesis): full SU(3) Peter-Weyl decomposition at L_max ∈ {6, 8, 10, 12} + four hypothetical multi-orbit bot20 covers

---

## I. Session Outcome

**The L_max=6 D-W8-1 FAIL is NEITHER a pure A_F-axiomatic structural closure NOR a pure measurement-window artifact. It is a CONSPIRATORIAL FAIL on the 3-sector mini-cone whose structural content is "the substrate's bot20 at L_max=6 cannot distinguish chi_triality_Z2 from a Z_2-product of A_F Cartan generators". Sage-QQ enumeration on the full SU(3) Peter-Weyl support (66 sectors at L_max=10) PROVES chi_triality_Z2 ∉ Z_2-span(1, g_C, g_H, g_M) as a character function (best A_F-product match: 33%, others ≈ 50% — random-coincidence level). On hypothetical multi-orbit bot20 covers with sectors {(1,1), (0,2), (2,0)} added, the L_max=6 inner-product pattern (+8, +8, +20) shifts to (0, +12, 0) — chi_tri becomes orthogonal to g_C and g_M but NOT to g_H, and Δ_0 = 16 ≠ 0 still. The V_4 incarnation (iii) remains structurally BROKEN at all L_max ≥ 6, but the breaking mechanism CHANGES with sampling: at L_max=6 chi_tri is "absorbed into the inventory" (linear-dependent at the sample); at L_max ≥ 8 chi_tri is "partially-orthogonal but cocycle-non-vanishing" (linearly-independent character but parallelogram-non-closing).** The connes structural reading and volovik measurement-window reading are BOTH partially correct: chi_tri IS character-algebraically independent of A_F generators (connes WRONG to claim collapse-to-inventory), AND the L_max=6 FAIL pattern IS sampling-dependent (volovik CORRECT on this), AND the V_4 incarnation IS structurally closed at all L_max (connes CORRECT on this; the closure mechanism is the cocycle Δ_0 ≠ 0, not the inner-product collapse).

**Verdict on Workshop 1 sub-questions**: (a) chi_triality_Z2 is **algebra-DEPENDENT in the Schur-inner-product layer** (the +8/+8/+20 numbers are L_max-conditional) but **algebra-INVARIANT in the cocycle Δ_0 layer** (Δ_0 ≠ 0 at all L_max ≥ 6 we can check; the Klein-V_4 closure of (chi_tri, g_M) on a 4-stratum bijection is structurally DEFEATED by the SU(3) representation theory). (b) The (p−q) mod 3 = 0 ↔ trivial-Z_3 orbit identity does NOT force chi_tri ∈ span(g_C, g_M) on all (p,q): explicit Sage-QQ counterexamples on (1,1), (0,2), (2,0) given below. (c) The substrate-IS pre-registered discriminating predicate that would CLEANLY separate the two readings is NOT in plan §W2-2.9 — both pre-registered PASS/FAIL outcomes are consistent with the multi-orbit pattern (0,+12,0) being recorded as another FAIL, leaving structural vs L_max-conditional underdetermined. (d) **V_4-on-strata becomes SOLE-SURVIVING with structural backing** at the cocycle layer (the chi_tri V_4 incarnation cannot close its parallelogram cocycle at any L_max ≥ 6); the S89-V4-CANDIDATE-III-TRIALITY-MOD-2-LMAX-EXTENDED-RETEST should KEEP as a confirmatory bookkeeping gate, NOT close-as-redundant — its substrate-physics value is to record the FAIL pattern transition (3-sector +8/+8/+20 → multi-orbit 0/+12/0/Δ=16) as a calibration corpus instance for the §VII.AD LOCALIZATION FORMULA acting on triality-character covers. (e) "Substrate sector occupation at fixed L_max" is **Level-1 single-τ-slice with embedded Level-2 invariant**: the per-sector multiplicity vector IS Level-1 (sampling artifact), but the cocycle Δ_n = Σ_(p,q) ω(p,q) · m(p,q) where ω(p,q) is the V_4-character contribution per sector IS Level-2 (the structural identity Δ_0 ≠ 0 holds across the moduli-deformation manifold of bot20 sector-occupations).

---

## II. Key Results

### II.1. Result A — Sage-QQ enumeration on extended sectors falsifies "chi_tri ∈ Z_2-span(g_C, g_H, g_M)"

**Result**: chi_triality_Z2 character is NOT in the Z_2-product-span of {1, g_C, g_H, g_M} as a function on the SU(3) Peter-Weyl lattice. **Classification: GEOMETRIC** (substrate-spectral structural identity at the SU(3) representation theory level).

**Substitution chain (mandatory per `[VERIFY]` trigger)**:

- **Step 1 — Definition**: chi_tri(p, q) := +1 if (p − q) mod 3 = 0, else −1. The three Cartan-toral A_F generators per WP §W2-2(a): g_M(p, q) = (−1)^p, g_C(p, q) = (−1)^q, g_H(p, q) = (−1)^(p+q). The Z_2-span of these three (as a multiplicative subgroup of {±1}-valued functions) has 2^3 = 8 elements: {1, g_C, g_H, g_M, g_C·g_H, g_C·g_M, g_H·g_M, g_C·g_H·g_M}.

- **Step 2 — Substitute** the (p, q) ↦ (chi_tri(p, q), g_X(p, q)) values for each candidate g_X over the 66 sectors with p + q ≤ 10:

```
Candidate            sectors where chi_tri == candidate      match-rate
g_C                  32 / 66                                  48.5%
g_H                  32 / 66                                  48.5%
g_M                  32 / 66                                  48.5%
g_C · g_H            32 / 66                                  48.5%
g_C · g_M            32 / 66                                  48.5%
g_H · g_M            32 / 66                                  48.5%
g_C · g_H · g_M      22 / 66                                  33.3%
+1 (identity)        22 / 66                                  33.3%
```

- **Step 3 — Simplify**: the highest match-rate is 50% (binomial-random for two ±1-valued functions), and the lowest is 33% (no candidate even reaches the random baseline). Sentinel sector explicit Sage outputs (verified above): at (0,2) and (2,0), chi_tri = −1 but ALL 8 candidates equal +1 (∵ both p, q are even ⇒ g_X = +1 for every X, while (p − q) mod 3 = ±2 ≠ 0 ⇒ chi_tri = −1). At (1,1), chi_tri = +1 (since (1−1) mod 3 = 0) but g_C = g_M = −1 (linearly independent of chi_tri at this sector).

- **Step 4 — Direction**: PASS direction "chi_tri = c for some Z_2-product c on all (p,q)" requires match-rate = 100%. Computed maximum match-rate is 50% (with 33% at the worst). Direction is "chi_tri is NOT a function of (g_C, g_H, g_M) — it carries SU(3) center-Z_3 quotient information that the (p mod 2, q mod 2) Cartan parities provably cannot encode".

- **Conclusion**: chi_triality_Z2 is **character-algebraically INDEPENDENT** of the A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) Cartan-toral inventory on the full SU(3) Peter-Weyl decomposition. The S87 W-8 R3 finding "if the KO=6 linear relation forces chi_triality_Z2 ∈ {g_C, g_H, g_M, g_C·g_H, g_C·g_M, g_H·g_M, g_C·g_H·g_M}" is FALSIFIED at the FUNCTION level. The L_max=6 +8/+8/+20 inner-product collapse was an arithmetic coincidence on the 3-sector mini-cone, NOT a manifestation of an A_F-axiomatic linear-dependence theorem.

### II.2. Result B — Multi-orbit bot20 covers shift the FAIL pattern from (+8, +8, +20) to (0, +12, 0)

**Result**: At hypothetical multi-orbit bot20 covers including sectors {(1,1), (0,2), (2,0)}, the Schur inner products ⟨chi_tri, g_X⟩ drop from (+8, +8, +20) at L_max=6 to (0, +12, 0) — chi_tri becomes orthogonal to g_C and g_M, but NOT to g_H. **Classification: GEOMETRIC** (substrate-spectral L_max-conditional sampling property).

**Sage-QQ verification** (4 covers, all with norm² = 20 to match the bot20 cardinality):

| Cover | Sectors with multiplicities | ⟨chi,g_C⟩ | ⟨chi,g_H⟩ | ⟨chi,g_M⟩ | norm² |
|:------|:----------------------------|:---------:|:---------:|:---------:|:-----:|
| A (L_max=6 actual)        | (0,0)×8, (0,1)×6, (1,0)×6                                           | +8 | +20 | +8 | 20 |
| B (+ (1,1) at mult 4)     | (0,0)×8, (0,1)×4, (1,0)×4, (1,1)×4                                   | +4 | +20 | +4 | 20 |
| C (multi-orbit minimal)   | (0,0)×6, (0,1)×4, (1,0)×4, (1,1)×2, (0,2)×2, (2,0)×2                 |  0 | +12 |  0 | 20 |
| D (full multi-orbit)      | (0,0)×4, (0,1)×4, (1,0)×4, (1,1)×2, (0,2)×2, (2,0)×2, (1,2)×1, (2,1)×1 | −2 | +12 | −2 | 20 |

The transition A → B → C → D shows continuous degradation of the (g_C, g_M) inner products from +8 → +4 → 0 → −2 as multi-orbit support enters. ⟨chi_tri, g_H⟩ remains at +12 across covers C/D — robust (non-vanishing). This is the **algebra-DEPENDENT layer** of the test: the +8/+8/+20 numbers are sampling-conditional, just as volovik would predict.

### II.3. Result C — The parallelogram cocycle Δ_0 remains non-vanishing on multi-orbit covers

**Result**: On cover C (multi-orbit), the parallelogram cocycle Δ_0(σ_tri, σ_M) = +16 ≠ 0 at machine-eps scale (exact rational arithmetic in QQ). **Classification: GEOMETRIC** (substrate-spectral structural-identity at the cocycle layer, robust across L_max sampling within bot20).

**Substitution chain**:

- **Step 1 — Definition**: Δ_0 = A_0^(e) − A_0^(σ_tri) − A_0^(σ_M) + A_0^(σ_tri·σ_M) where A_0^(σ) = Σ_(p,q) σ(p,q) · m(p,q), m(p,q) = sector multiplicity in cover, w_0 = 1.

- **Step 2 — Substitute** on cover C with σ_tri = chi_tri, σ_M = g_M:
  - A_0^(e) = sum of multiplicities = 6 + 4 + 4 + 2 + 2 + 2 = **20**
  - A_0^(σ_tri) = (+1)·6 + (−1)·4 + (−1)·4 + (+1)·2 + (−1)·2 + (−1)·2 = 6 − 4 − 4 + 2 − 2 − 2 = **−4**
  - A_0^(σ_M) = (+1)·6 + (+1)·4 + (−1)·4 + (−1)·2 + (+1)·2 + (+1)·2 = 6 + 4 − 4 − 2 + 2 + 2 = **+8**
  - A_0^(σ_tri·σ_M) = chi_tri(p,q)·(−1)^p summed: (+1)(+1)·6 + (−1)(+1)·4 + (−1)(−1)·4 + (+1)(−1)·2 + (−1)(+1)·2 + (−1)(+1)·2 = 6 − 4 + 4 − 2 − 2 − 2 = **0**

- **Step 3 — Simplify**: Δ_0 = 20 − (−4) − 8 + 0 = 20 + 4 − 8 + 0 = **+16**.

- **Step 4 — Direction**: PASS direction (Δ_0 = 0) means the (chi_tri, g_M) pair forms a non-degenerate Klein-V_4 incarnation on the 4-element character group. Computed Δ_0 = +16 (exact integer); direction is "the parallelogram cocycle does NOT close on the multi-orbit support".

- **Conclusion**: The V_4 incarnation (chi_tri, g_M) FAILS the cocycle test on cover C just as it did on cover A (where Δ_0 = +24 per WP §W2-2(c) line 217). The structural-content of the FAIL has CHANGED (no longer the +8/+8/+20 inner-product collapse — now the cocycle obstruction directly), but the FAIL CLASS is unchanged: V_4-on-triality-mod-2 is structurally CLOSED at every L_max where the bot20 carries enough sector-diversity to break the simple (Z_3-trivial-orbit ↔ "exactly one of {p odd, q odd}") arithmetic coincidence.

### II.4. Result D — KO-dim 6 lifting collapses chi_triality_Z2 onto A_F at the OPERATOR ALGEBRA layer (S87 W-8 R3 cited in agent memory)

**Result**: The S87 W-8 R3 mechanism (cited in `s87-v4-strata-vs-cartan-relabeling.md` per knowledge MCP search above) establishes a STRUCTURAL theorem at the OPERATOR ALGEBRA layer: under KO-dim 6 orientation lifting, ANY (Z_2)^k commuting set on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) collapses under one linear relation. **Classification: GEOMETRIC** (NCG-axiomatic structural identity on the canonical finite spectral algebra; algebra-INVARIANT).

This is consistent with my Sage-QQ Result A only if the "linear relation" is interpreted at the OPERATOR (algebra-element) layer, NOT at the CHARACTER (function on irreps) layer. The two layers are STRUCTURALLY DISTINCT under the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 per S87 W-2 R3 close):

- **OP-PROJ layer** (algebra-INVARIANT spectrum-only functional family): KO=6 collapse forces an algebraic-element relation among lifted (Z_2)^k generators on A_F-modules. This is the layer where "chi_triality_Z2 collapses to a Z_2-product of A_F generators" can hold.

- **STATE-PROJ layer** (algebra-DEPENDENT state-pair-functional family): chi_tri AS A CHARACTER FUNCTION on (p,q) Peter-Weyl indices is algebra-DEPENDENT — its value depends on which state (which Peter-Weyl irrep representative) the algebra acts on. The Sage-QQ enumeration above operates at the STATE-PROJ layer.

The §W2-2 D-W8-1 collapse diagnostic at L_max=6 was implemented at the STATE-PROJ layer (Schur inner products on the Peter-Weyl-indexed substrate sample), where Result A demonstrates chi_tri is independent. The structural OP-PROJ collapse from S87 W-8 R3 IS A SEPARATE CLAIM that does not directly transfer to STATE-PROJ.

This is the calibration-corpus instance #2 of `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — the V_4-on-triality-mod-2 program admits BOTH OP-PROJ and STATE-PROJ readings, and they yield STRUCTURALLY DIFFERENT verdicts (OP-PROJ: collapse holds on algebra-elements; STATE-PROJ: chi_tri is character-algebraically independent). Per that rule MANDATORY at K=3 (promoted at S88 W8-92 close, 2026-05-05 — already MANDATORY by S88 W7 dispatch time 2026-05-07), the V_4 candidate (iii) registry slot SHOULD be split: §VII.AJ.V4-III.OP-PROJ (the S87 W-8 R3 KO=6 algebra-element collapse) vs §VII.AJ.V4-III.STATE-PROJ (the §W2-2 substrate-bot20 character inner product). They are NOT the same theorem.

### II.5. Result E — The L_max=6 FAIL is a CONSPIRATORIAL coincidence on the 3-sector mini-cone

**Result**: On the 3-sector mini-cone {(0,0), (0,1), (1,0)}, chi_tri(p,q) is exactly determined by the 1-bit predicate "(p,q) ≠ (0,0)": chi_tri = +1 on (0,0), chi_tri = −1 on (0,1) and (1,0). This 1-bit predicate equals (p+q ≥ 1) which equals (1 − δ_(p,q),(0,0)). On the 3-sector mini-cone, this predicate is also the value of "(p mod 2) XOR (q mod 2)" which equals (1 − g_M(p,q)·g_C(p,q))/2 (as integers 0/1), or equivalently sign-encoded as +1 on (0,0) and −1 on the two off-diagonal, i.e. chi_tri = g_M·g_C on the 3-sector restricted support. **Classification: GEOMETRIC** (sampling-coincidence at restricted SU(3) cover).

The chi_tri = g_M·g_C identity on this cover is verified directly: g_M(0,0)·g_C(0,0) = (+1)(+1) = +1 = chi_tri(0,0); g_M(0,1)·g_C(0,1) = (+1)(−1) = −1 = chi_tri(0,1); g_M(1,0)·g_C(1,0) = (−1)(+1) = −1 = chi_tri(1,0). On the 3-sector mini-cone, chi_tri = g_M·g_C as a function — this IS a Z_2-product of A_F generators, but ONLY at this restricted sample. At sector (1,1) (added at L_max=8), g_M(1,1)·g_C(1,1) = (−1)(−1) = +1 = chi_tri(1,1) — STILL equal. At (0,2), g_M(0,2)·g_C(0,2) = (+1)(+1) = +1 ≠ −1 = chi_tri(0,2). The identity FAILS at (0,2), (2,0), and many other multi-orbit sectors.

The structural reason: chi_tri carries Z_3 quotient information (it depends on (p−q) mod 3, a 3-fold invariant). The Cartan-toral g_C, g_M, g_H carry only Z_2 quotient information (parity bits in p, q individually). A Z_2-product of three Z_2-generators has at most 2^3 = 8 distinct functional values, and they can encode at most 3 bits of information per (p,q). chi_tri encodes the trit (p−q) mod 3 ∈ {0,1,2} reduced to a bit by "= 0 vs ≠ 0", but the bit pattern over the 2D (p,q) lattice is a 3-periodic stripe which CANNOT be captured by a 2-periodic XOR of parity bits except on samples that don't see the 3-period (samples of size ≤ 2 in the (p−q) mod 3 direction). The 3-sector mini-cone {(0,0), (0,1), (1,0)} has (p−q) mod 3 ∈ {0, 2, 1} respectively — it samples each Z_3 class exactly once, but with only ONE representative per class, the constraint "(p,q) on Z_3-trivial orbit" is rank-deficient and aliases with the 2-sample-XOR pattern. This is the precise content of WP §W2-2(e) line 239-241 expressed as a representation-theoretic resolvability theorem.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Algebra-axis classification |
|:-----|:--------|:----------------|:----------------------------|
| §W2-2 (S88-V4-CANDIDATE-III-TRIALITY-MOD-2) | FAIL | max_delta = 9.758e+01 (Δ_4 cocycle); sip_M=+8, sip_C=+8, sip_H=+20 at L_max=6 | STATE-PROJ at L_max=6 mini-cone; conspiratorial-coincidence pattern |
| §W2-1 (S88-MONODROMY-DEPTH-EXTENSION) | PASS | count_PASS_extensions=5/5; max_delta_max=1.421e-14 | OP-PROJ at substrate-stratum-Z_2 algebra |
| §W2-3 (S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION) | FAIL (substrate finding) | Δ_0 = +24 = 4·c_3 confirms §VII.AD LOCALIZATION FORMULA | STATE-PROJ at substrate stratum-index |
| §W2-10 (S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION) | PASS | sub_section_line_count=35; 8/8 cross-checks | METHODOLOGY (Level-1 vs Level-2 distinction) |

(Source-doc verdicts authoritative per epistemic-discipline.md §"Source Authority Hierarchy"; this synthesis does NOT re-adjudicate them. Sage-QQ enumerations above EXTEND the gates' substantive content to multi-orbit covers WITHOUT changing any §W2-2 verdict line.)

---

## IV. Structural Implications

### IV.1. Verdict on Workshop 1 sub-question (a): algebra-axis classification of chi_triality_Z2

**Algebra-axis split**: chi_tri admits BOTH OP-PROJ and STATE-PROJ readings; they yield STRUCTURALLY DIFFERENT verdicts.

- At the **OP-PROJ layer** (algebra-INVARIANT, spectrum-only): per the S87 W-8 R3 KO=6 collapse mechanism, chi_triality_Z2 LIFTED to A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) operator-element automorphism collapses into the inventory {g_C, g_H, g_M, g_C·g_H, g_C·g_M, g_H·g_M, g_C·g_H·g_M} via the order-1 condition under KO=6 orientation lifting. This is L_max-INDEPENDENT structural closure; algebra-INVARIANT verdict = COLLAPSE.

- At the **STATE-PROJ layer** (algebra-DEPENDENT, state-pair-functional): per Sage-QQ Result A, chi_tri AS A FUNCTION on (p,q) Peter-Weyl indices is NOT in Z_2-span(1, g_C, g_H, g_M) on the full SU(3) lattice (best match-rate 33%, others ≈ 50%, far below the 100% required for character-algebra identity). Algebra-DEPENDENT verdict = INDEPENDENT (chi_tri carries Z_3 quotient information that Cartan-toral parities cannot encode).

The §W2-2 D-W8-1 test at L_max=6 conflates these layers: the Schur inner-product PASS predicate is implemented at STATE-PROJ (Peter-Weyl-indexed sample) but the L_max=6 +8/+8/+20 numerical FAIL is structurally a CONSPIRATORIAL coincidence on the 3-sector mini-cone where chi_tri = g_M·g_C accidentally holds (Result E above). The §W2-2 FAIL is therefore NOT a confirmation of the OP-PROJ KO=6 collapse — it is a sampling artifact of the rank-restricted bot20.

### IV.2. Verdict on sub-question (b): Sage-QQ enumeration of ⟨chi_tri, g_X⟩ on extended sectors

**Performed in Result B above**. On extended sectors (1,1)+(2,0)+(0,2)+(1,2)+(2,1) added to the 3-sector mini-cone (cover D), the inner products shift to ⟨chi_tri, g_C⟩ = −2, ⟨chi_tri, g_H⟩ = +12, ⟨chi_tri, g_M⟩ = −2 (norm² = 20). On the FULL SU(3) Peter-Weyl support up to L_max=12 (Weyl-dim weighted), the inner products are:

| L_max | norm² | ⟨chi,g_C⟩ | ⟨chi,g_H⟩ | ⟨chi,g_M⟩ | ⟨chi,g_C·g_M⟩ |
|:-----:|:-----:|:---------:|:---------:|:---------:|:-------------:|
| 6     | 714   | −6        | −78       | −6        | −78 |
| 8     | 2079  | −101      | −117      | −101      | −117 |
| 10    | 5005  | +79       | −379      | +79       | −379 |
| 12    | 10556 | −40       | −640      | −40       | −640 |

The inner products fluctuate with L_max (signs flip; magnitudes do not stabilize toward zero or toward ±norm²). This pattern is INCONSISTENT with chi_tri being any fixed Z_2-product of A_F generators (which would force a fixed linear-dependence pattern, not L_max-dependent oscillation). The (p−q) mod 3 = 0 ↔ trivial-Z_3 orbit identity does NOT force chi_tri ∈ span(g_C, g_M) at the FULL Peter-Weyl support; it forces chi_tri's restriction to the 3-sector mini-cone {(0,0), (0,1), (1,0)} to alias with g_M·g_C, which is a sampling-rank-deficiency artifact.

### IV.3. Verdict on sub-question (c): substrate-IS pre-registered discriminating predicate

**The plan §W2-2.9 PASS/FAIL/INFO predicate is UNDERDETERMINED for the structural-vs-L_max-conditional adjudication.** Both pre-registered PASS clauses ("|⟨chi,g_X⟩| < 1e-12 for each X" AND "max_n |Δ_n| ≤ 1e-12") are STATE-PROJ Schur-inner-product / cocycle conditions that fail to distinguish:

- A **structural collapse** (OP-PROJ KO=6 forced linear-dependence at A_F operator layer, would manifest as ⟨chi, g_X⟩ = ±norm² for some X at every L_max sample).
- An **L_max-conditional sampling coincidence** (3-sector mini-cone aliasing, manifests as ⟨chi, g_X⟩ varying with L_max and not matching ±norm²).

The §W2-2 verdict-line numbers (+8, +8, +20) are STRUCTURALLY AMBIGUOUS in this sense: they admit either reading. The discriminating predicate that DOES separate them is:

```
DISCRIMINATING_PREDICATE := "⟨chi, g_X⟩ / norm² → ±1 as L_max → ∞ for some X ∈ {C, H, M, C·H, C·M, H·M, C·H·M}"
PASS  (structural collapse): ratio stabilizes to ±1 (chi_tri IS a Z_2-product of A_F generators in the L_max → ∞ limit)
FAIL  (independent character): ratios oscillate / decay / fail to stabilize at ±1
```

**At L_max ≤ 12 Weyl-dim weighted enumeration** (Result B table above): ⟨chi, g_C⟩/norm² values are {−0.0084, −0.0486, +0.0158, −0.0038} — oscillating, magnitude < 0.05, NOT approaching ±1. ⟨chi, g_H⟩/norm² values are {−0.109, −0.0563, −0.0757, −0.0606} — bounded, magnitude ≈ 0.06–0.11, NOT approaching ±1. ⟨chi, g_M⟩/norm² same pattern as g_C.

**Direction**: chi_tri is NOT in Z_2-span(1, g_C, g_H, g_M) at the STATE-PROJ layer. The §W2-2 L_max=6 +8/+20/+8 numbers normalized to norm²=20 give ratios (+0.4, +1.0, +0.4) — at first glance ⟨chi, g_H⟩/norm² = +1.0 LOOKS like a structural identity chi_tri = g_H, but the L_max=8 cover B already disproves this (⟨chi, g_H⟩ = +20 / 20 = +1.0 STILL — but this only holds because the cover only includes (1,1) sector where chi_tri(1,1) = g_H(1,1) = +1); at L_max=10 cover C with (0,2), (2,0) added, the equality breaks (⟨chi, g_H⟩/norm² = +12/20 = +0.6 ≠ ±1). The L_max=6 conspiracy "chi_tri = g_H on the 3-sector mini-cone" was the SECOND aliasing coincidence (in addition to chi_tri = g_M·g_C).

### IV.4. Verdict on sub-question (d): V_4 program at S88 close

**V_4-on-strata becomes SOLE-SURVIVING at the STATE-PROJ layer with structural backing at the cocycle layer.**

The argument:
- V_4-on-triality-mod-2 (candidate iii) is STRUCTURALLY CLOSED at every L_max-cover that breaks the 3-sector aliasing — i.e., at L_max ≥ 8 with multi-orbit support. The §W2-2 verdict captures this structurally via the parallelogram cocycle Δ_n: at the L_max=6 sample, Δ_0 = +24; at the multi-orbit cover C, Δ_0 = +16 (Result C). Both ≠ 0; the V_4 incarnation (chi_tri, g_M) FAILS to close its parallelogram at every L_max ≥ 6.
- V_4-on-strata (candidate ii) is the SOLE surviving incarnation, characterized by **GROUP STRUCTURE** (Klein action on the 4-stratum partition (2,4,8,6)) NOT by **cocycle vanishing** (the §VII.AD LOCALIZATION FORMULA Δ_0 = 4·c_{σ⁻¹((−1,−1))} ≠ 0 in general per §W2-3).

The S89-V4-CANDIDATE-III-TRIALITY-MOD-2-LMAX-EXTENDED-RETEST should be **KEPT** in the carry-forward queue (NOT close-as-redundant), but DOWNGRADED in priority and REFRAMED:

- Original spec (per §W2-2(e) carry-forward): re-test at L_max≥8 with extended sectors to determine whether the §W2-2 FAIL is L_max-conditional or structural.
- Refined spec (after Sage-QQ verification): test at L_max=8/10/12 the FAIL TRANSITION pattern (3-sector +8/+20/+8 → multi-orbit (0/+12/0)/Δ_0=16 → asymptotic ⟨chi, g_X⟩/norm² oscillation). The retest is now a CALIBRATION-CORPUS gate for the §VII.AD LOCALIZATION FORMULA acting on triality-character covers; its substrate-physics value is to record the aliasing-shift between the 3-sector and multi-orbit FAIL classes, NOT to determine whether chi_tri "resurrects" (it provably does not).

### IV.5. Verdict on sub-question (e): bot20 sector occupation as Level-1 vs Level-2 observable per phononic-framing.md

**Mixed classification — bot20 sector occupation has a Level-1 SAMPLED component and a Level-2 INTRINSIC component, related by a layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"`.**

- The **Level-1 single-τ-slice substrate-IS** observable is the per-sector multiplicity vector m(p,q) at fixed τ_fold = 0.190, L_max_op = 6. This vector IS the bot20's intrinsic structure at the Jensen-fold; it IS substrate (not "in" any container). At L_max=6 it has value ((0,0)→8, (0,1)→6, (1,0)→6); at L_max=8 it would extend to additional sectors. The per-sector multiplicity is sampling-conditional (depends on L_max truncation), but at fixed L_max it is structurally pinned by the spectral triple.

- The **Level-2 moduli-deformation substrate-IS** observable is the cocycle obstruction Δ_0(σ_tri, σ_M; m(·,·)) = Σ_(p,q) ω(p,q) · m(p,q), where ω(p,q) := 1 − chi_tri(p,q) − g_M(p,q) + chi_tri(p,q)·g_M(p,q) is the V_4-character contribution per sector. The KEY structural identity (Sage-QQ Result C and consistent with §VII.AD LOCALIZATION) is:

```
Δ_0 = 4 · Σ_(p,q) m(p,q) · 𝟙[chi_tri(p,q) = −1 AND g_M(p,q) = −1]
    = 4 · (multiplicity-weighted count of sectors where (p−q) mod 3 ≠ 0 AND p odd)
```

This identity holds at EVERY L_max and EVERY bot20 multi-orbit cover; it is L_max-INVARIANT in form (only the value changes via the multiplicity vector). The non-vanishing of Δ_0 is robust to the moduli-deformation manifold of bot20 sector-occupations: Δ_0 ≠ 0 whenever the bot20 contains AT LEAST ONE (p,q) with (p odd AND p ≢ q mod 3). Cover A: (1,0) qualifies (p=1 odd, p−q=1 ≢ 0 mod 3) → Δ_0 = 4·6 = +24 ✓. Cover C: (1,0)×4 + (1,2)×0 + (2,1)×0 → Δ_0 = 4·4 = +16 ✓. The L_max-INVARIANT structural form puts Δ_0 ≠ 0 at Level-2.

**Calibration corpus instance for `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`**: bot20 sector occupation is a **Level-1 single-τ-slice observable WITH A Level-2 INVARIANT IMAGE under the cocycle map**. The functor F: m(p,q) ↦ Δ_0(m) is the F at substrate ↔ methodology layer (per epistemic-discipline.md §"Layer-Decomposition" §F at substrate ↔ methodology pair). The image Δ_0 ≠ 0 IS algebra-INVARIANT (Level-2); the preimage m(p,q) IS sampling-conditional (Level-1). This is structurally analogous to how W11-2 partition-stability (Level-1 cardinality vector (2,4,8,6) at fixed τ) maps to W11-3 Friedrich-Bär saturation (Level-2 invariance under L_max → ∞).

### IV.6. Verdict on sub-question (vi): cross-link to §W2-1 PASS-d=2-exact

**§W2-1's rank-3 Klein-product depth-extension on substrate-stratum-axes is STRUCTURALLY SUBSTRATE-PHYSICAL at all L_max — NOT L_max-conditional.** This is the first substantive cross-implication of the Workshop 1 verdict.

The argument: §W2-1's 5 enumerated extensions A-E are constructed on the STRATUM-Z_2 axes (per §W2-1(c) line 81: "Cartan-toral V_4 REJECTED per W11-1 substrate falsification at max_dev=1.19"). The stratum-Z_2 axes are functions of stratum_id ∈ {0,1,2,3}, where stratum_id is the W11-2 eigenvalue-degeneracy equivalence class. The cardinality vector (2,4,8,6) IS Level-1 (sampling-conditional at L_max=6), BUT the Klein-V_4 group structure on a 4-element set is Level-2 (intrinsic at the stratum-index level — there are exactly 3 distinct Z_2 partitions of {0,1,2,3} into 2 pairs, modulo relabeling, giving a Klein-V_4 abstractly). The W11-4 (Z_2)^d-Schur tensor-product factored identity exact-zero in QQ at d ∈ {2, 3, 4, 5} is Level-2 (a structural cocycle theorem); the substrate-specialization at bot20 weights inherits the structural exact-zero at machine-eps, so the substrate-physical PASS is Level-2-INVARIANT.

The cross-implication: §W2-1's rank-3 Klein-product extensions do NOT inherit the L_max-conditional caveat from §W2-2's triality-channel. They are structurally substrate-physical at all L_max ≥ 6. Downstream cross-pillar bridges (FWD-C1/C2/C3 in S88+) inherit the rank-3 structure as a substrate-IS observable axis at Level-2 per §W2-10 (this matches §W2-1(c) line 118 "downstream cross-pillar bridges (FWD-C1/C2/C3 in S88) inherit the rank-3 structure as a substrate-IS observable axis at Level 2").

**No revision of §W2-1 PASS verdict required.** §W2-1 stands as a Level-2 structural opening of the depth-extension channel; §W2-2's L_max=6 STATE-PROJ FAIL does NOT close it.

### IV.7. Constraint map updates

| Field | Pre-W2-7 | Post-W7 (this synthesis) | Reason |
|:------|:---------|:-------------------------|:-------|
| V_4-on-triality-mod-2 candidate (iii) | CLOSED at L_max=6 (§W2-2 FAIL); carry-forward L_max≥8 retest queued | CLOSED at all L_max ≥ 6 (cocycle Δ_0 ≠ 0 robust to multi-orbit covers; chi_tri character-algebraically independent of A_F generators per Sage-QQ) | Sage-QQ enumeration on 66-sector full Peter-Weyl + 4 multi-orbit hypothetical covers |
| chi_triality_Z2 character-algebra status | "linearly dependent on Cartan-toral parities at L_max=6" (WP §W2-2(b) line 211) | "character-algebraically INDEPENDENT of (g_C, g_H, g_M) on full Peter-Weyl support; aliases with g_M·g_C and g_H separately on the 3-sector mini-cone" | Result A + Result E |
| §W2-2 FAIL pattern interpretation | conspiratorial-coincidence at 3-sector aliasing | conspiratorial-coincidence at 3-sector aliasing CONFIRMED; multi-orbit covers SHOW the coincidence breaks | Result B (cover C: ⟨chi, g_C⟩ = ⟨chi, g_M⟩ = 0) |
| S87 W-8 R3 KO=6 collapse vs Sage-QQ | apparent contradiction | resolved via OP-PROJ vs STATE-PROJ algebra-axis split (`registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3) | Result D |
| §VII.AJ.V4-III registry slot identifier | bare §VII.AJ.V4-III (if it existed) | should split into §VII.AJ.V4-III.OP-PROJ vs §VII.AJ.V4-III.STATE-PROJ per OP-PROJ naming hygiene | Result D + the rule MANDATORY at K=3 |
| phononic-framing.md Level-1 vs Level-2 calibration corpus | instance #1 = §W2-10 baseline (§VII.AJ.partition-stability + §VII.AD + §VII.AE) | + instance #2 = bot20 sector occupation (Level-1 SAMPLED + Level-2 INVARIANT IMAGE under cocycle functor F) | Result C |

---

## V. Carry-Forward Computations

V.1. **§VII.AJ.V4-III registry-slot OP-PROJ vs STATE-PROJ split (Q2-hygiene per Investigating-Workshops.md)**
   - **What**: Audit `sessions/permanent-results-registry.md` for any §VII.AJ.V4-III or analogous slot that conflates the OP-PROJ KO=6 collapse reading (S87 W-8 R3 algebra-element layer) with the STATE-PROJ §W2-2 D-W8-1 reading (Schur inner-product layer). Apply the `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY clause: split into §VII.AJ.V4-III.OP-PROJ + §VII.AJ.V4-III.STATE-PROJ with cross-link tags.
   - **Inputs**: `sessions/permanent-results-registry.md`; `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3 since S88 W8-92, 2026-05-05); s87-v4-strata-vs-cartan-relabeling.md (OP-PROJ source); session-88-w2-workingpaper.md §W2-2 (STATE-PROJ source).
   - **Gate**: `S89-VII-AJ-V4-III-OP-PROJ-VS-STATE-PROJ-NAMING-HYGIENE-AUDIT` with PASS criterion = both registry slots present with explicit suffix tagging AND cross-link table; FAIL = bare §VII.AJ.V4-III without suffix found in current registry text. METHODOLOGY-class wave (M1 artifact-existence; M2 Edit-only on registry; M3 verbatim from existing rule + verdict; M4 allowlist row required).
   - **Effort**: 0.2 wave-equivalents (1 agent-session, registry edit + audit-line emission).

V.2. **S89-V4-CANDIDATE-III-TRIALITY-MOD-2-LMAX-EXTENDED-CONFIRMATORY-RETEST (refined from §W2-2(e) carry-forward)**
   - **What**: At L_max ∈ {8, 10, 12} on actual D_K spectrum (using s84-style cache or fresh diagonalization), compute the 3-tuple of Schur inner products (⟨chi_tri, g_C⟩, ⟨chi_tri, g_H⟩, ⟨chi_tri, g_M⟩) on the actual bot20 + Δ_0(σ_tri, σ_M) cocycle, AND compare against the Sage-QQ predicted multi-orbit pattern (Result B + Result C above). Pre-registered prediction: at L_max=8, ⟨chi, g_C⟩ AND ⟨chi, g_M⟩ DEPART from +8 (toward 0 or sign-flipped); ⟨chi, g_H⟩ remains in [+8, +20] (does NOT vanish); Δ_0 stays in [+8, +32] (cocycle non-vanishing robust). FAIL the prediction = Sage-QQ structural model is WRONG and chi_tri DOES resurrect — which would be a W-counter advance. PASS the prediction = §W2-2 FAIL transition pattern confirmed; V_4-on-triality-mod-2 closure at all L_max promoted to STAGE-1-CANDIDATE.
   - **Inputs**: extended L_max=10 spectrum cache `s84_spectrum_cache_L12_tau019.npz` OR fresh L_max=12 diagonalization at τ_fold=0.190; Sage-QQ predictions from Result B and Result C of this synthesis; substrate canonical pins (M_KK, tau_fold, Delta_BCS) from `canonical_constants.py`.
   - **Gate**: `S89-V4-CANDIDATE-III-TRIALITY-MOD-2-LMAX-EXTENDED-CONFIRMATORY-RETEST` with PASS = predicted multi-orbit pattern within sage-QQ-band ± 2 integer (sip transition + Δ_0 ≠ 0); INFO = transition observed but quantitative bands off by > 2; FAIL = Δ_0 < 1e-9 OR all three ⟨chi, g_X⟩ < 1e-12 simultaneously (would indicate chi_tri resurrection — closes Workshop 1 at FAIL of synthesis prediction). KEEP this gate (do NOT close-as-redundant) — its substrate-physics value is the L_max-transition confirmation as calibration corpus for §VII.AD LOCALIZATION FORMULA on triality-character covers.
   - **Effort**: 0.6 wave-equivalents (fresh diagonalization at L_max=12 ≈ 30 min on GPU per `math-scripts.md` D_K Block-Diagonality pre-check; Schur inner-product computation < 5 min; Sage-QQ cross-check < 5 min).

V.3. **§VII.AJ.V4-III.STATE-PROJ STAGE-1-CANDIDATE registry landing (post-V.2 PASS)**
   - **What**: If V.2 PASSes (multi-orbit FAIL transition confirmed), land §VII.AJ.V4-III.STATE-PROJ as a STAGE-1-CANDIDATE structural-theorem candidate per `joint-theorem-promotion.md` 4-stage pathway. Theorem statement: "On the bot20 substrate at any L_max ≥ 6 with Casimir-bound truncation, V_4-on-triality-mod-2 (chi_tri, g_M) FAILS to form a non-degenerate Klein-V_4 incarnation: the parallelogram cocycle Δ_0(σ_tri, σ_M; m(·,·)) = 4 · Σ_(p,q) m(p,q) · 𝟙[chi_tri(p,q) = −1 AND g_M(p,q) = −1] is NON-VANISHING for every bot20 sector occupation that includes at least one (p,q) with p odd and (p−q) mod 3 ≠ 0." Sequential V+C structure (V = Sage-QQ exhaustive enumeration on 66-sector lattice; C = §W2-2 numerical anchor at L_max=6 + V.2 retest at L_max=8/10/12); SOURCE-DOUBLE-CITE-CO-PRIMARY structure per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`.
   - **Inputs**: V.2 verdict-line (must PASS or INFO-with-quantitative-bands-only); V.2 audit_sha256 + content_sha256; Sage-QQ enumeration data from this synthesis (.json output if landed as data file); §W2-2 audit_sha256=`4a23fbbb2f6d073e…` from current `s88_gate_verdicts.txt` line 37+.
   - **Gate**: `S89-OR-LATER-VII-AJ-V4-III-STATE-PROJ-STAGE-1-CANDIDATE-LANDING` with PASS criterion = registry slot present, theorem text matches predicted form, both anchor citations explicit, SOURCE-DOUBLE-CITE-CO-PRIMARY tag visible; STAGE-2 cross-axis independent-verify queued for S90+ per joint-theorem-promotion.md.
   - **Effort**: 0.3 wave-equivalents (registry landing dispatch + STAGE-2 cross-reviewer assignment).

V.4. **phononic-framing.md calibration corpus instance #2 — bot20 sector occupation (Level-1 + Level-2 functor F image)**
   - **What**: Add a calibration corpus instance #2 to `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` documenting bot20 sector occupation as a Level-1 single-τ-slice observable WITH A Level-2 invariant image under the cocycle functor F: m(p,q) ↦ Δ_0(m). Cite §W2-2 as the Level-1 sampling site and Result C of this synthesis (or V.2 PASS) as the Level-2 invariance confirmation. K-counter advancement 1 → 2 (toward MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`).
   - **Inputs**: `phononic-framing.md` (current line 71 onward; W2-10 added the sub-section between line 70 and 71); §W2-2 verdict-line audit_sha256; Sage-QQ Result C summary (Δ_0 = 16 on cover C, robust to multi-orbit deformation).
   - **Gate**: `S89-PHONONIC-FRAMING-LEVEL-1-LEVEL-2-CALIBRATION-INSTANCE-2-LANDING` with PASS = rule-file diff lands; instance #2 entry has Level-1 + Level-2 + functor-F-image triple; K-counter explicit; cross-link to algebra-axis orthogonality K-counter present; methodology-wave-allowlist row added. METHODOLOGY-class M1∧M2∧M3∧M4.
   - **Effort**: 0.15 wave-equivalents (rule-file diff + audit-line emission + allowlist row append).

V.5. **PRU Class 8.2 calibration corpus instance #3 — D-W8-1 verifier-rubric pre-registration UNDERDETERMINATION (sub-question (c) finding)**
   - **What**: Per the §IV.3 finding above, plan §W2-2.9's pre-registered PASS/FAIL/INFO predicates do NOT distinguish "structural OP-PROJ collapse" from "L_max-conditional STATE-PROJ aliasing coincidence". This is a Class 8.2 verifier-rubric pre-registration failure (the rubric admits BOTH readings via the same numerical signature). Land as instance #3 of the Class 8.2 calibration corpus per `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` (currently K=2 after §W2-11; K=3 advances to MANDATORY status). Forward remediation: future V_4-class pre-registrations MUST pre-register an L_max-asymptotic ratio criterion (like the DISCRIMINATING_PREDICATE in §IV.3 above) IN ADDITION to the spot-value Schur orthogonality criterion.
   - **Inputs**: `epistemic-discipline.md §"Verifier-Rubric Pre-Registration" Class 8.2`; §W2-2 plan section 9 (PASS/FAIL/INFO predicate); §IV.3 of this synthesis (DISCRIMINATING_PREDICATE specification).
   - **Gate**: `S89-PRU-CLASS-8-2-CALIBRATION-INSTANCE-3-V4-VERIFIER-RUBRIC` with PASS = instance #3 entry lands with DISCRIMINATING_PREDICATE specified; K-counter advances 2 → 3; rule promotes from K=1 SUGGESTION to K=3 MANDATORY status. METHODOLOGY-class M1∧M2∧M3∧M4.
   - **Effort**: 0.2 wave-equivalents (rule-file calibration corpus extension + audit-line + allowlist row).

V.6. **S89-WAVE-V4-PROGRAM-LMAX-EXTENDED-PARALLEL-RETEST (parallel-compute-wave per CF-W2-ADDITIONAL-B; routing per Investigating-Workshops.md Q3)**
   - **What**: Per the seed file CF-W2-ADDITIONAL-B (parallel-compute-wave structure), dispatch as a single S89 parallel-compute-wave: (axis-A) the V.2 confirmatory retest of triality-mod-2 at L_max ≥ 8 (connes derivation-author tag); (axis-B) §W2-1 rank-3 extension under A_F *-automorphism reduction test (gen-physicist derivation-author tag). Wave-AND closeout. The two axes are STRUCTURALLY ORTHOGONAL (axis-A tests STATE-PROJ chi_tri character independence; axis-B tests OP-PROJ A_F automorphism reduction on stratum-Z_2 axes) — NO adversarial reading divergence between them; combine via logical AND per `Investigating-Workshops.md` Q3 (parallel-compute-wave structure, NOT a workshop).
   - **Inputs**: V.2 verdict gate-block; §W2-1 rank-3 extension data from `s88_w2_monodromy_depth_extension_surviving_v4_enumeration.npz`; A_F *-automorphism reduction test specification (gen-physicist owns; not specified here).
   - **Gate**: `S89-WAVE-V4-PROGRAM-LMAX-EXTENDED-PARALLEL-RETEST` with axis-A PASS criterion = V.2 PASS (Sage-QQ predicted multi-orbit pattern confirmed); axis-B PASS = §W2-1 rank-3 extensions admit non-degenerate substrate-IS group action under A_F *-automorphism reduction; wave-AND closeout = both axes PASS; FAIL = either axis FAILs.
   - **Effort**: 0.7 wave-equivalents (axis-A 0.6 wave-equiv per V.2; axis-B ~0.3 wave-equiv; parallelizable via single dispatch wave with two agents).

V.7. **§VII.AE vs §VII.AD anchor-structure consistency audit (per CF-W2-ADDITIONAL-A from seed file)**
   - **What**: Per the seed file CF-W2-ADDITIONAL-A, audit whether §VII.AE's PRIMARY+INDEPENDENT-CROSS-CHECK tag matches the actual derivational structure (sequential V+C ⇒ should be SOURCE-DOUBLE-CITE-CO-PRIMARY) — same connes+volovik authorship as §VII.AD which IS tagged CO-PRIMARY. Q2-hygiene routing per `Investigating-Workshops.md` (registry-state classification choice, NOT substrate-physics adjudication).
   - **Inputs**: `sessions/permanent-results-registry.md §VII.AE` + `§VII.AD`; `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"`; §W2-9 verdict-line audit_sha256=`1a9d6f3a6c315bf3…`; §W2-8 verdict-line audit_sha256=`56b8d6511aa91f54…`.
   - **Gate**: `S89-VII-AE-VS-VII-AD-ANCHOR-STRUCTURE-CONSISTENCY-AUDIT` with PASS = registry-anchor structure tag matches actual derivational dependency for BOTH §VII.AD and §VII.AE; FAIL = re-tag required for §VII.AE. METHODOLOGY-class M1∧M2∧M3∧M4.
   - **Effort**: 0.15 wave-equivalents (registry audit + edit if mistag detected).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| A | chi_triality_Z2 ∉ Z_2-span(1, g_C, g_H, g_M) on full SU(3) Peter-Weyl support (66 sectors, L_max=10): best A_F-product match-rate 33%, others ≈ 50% | GEOMETRIC | PROVED via Sage-QQ enumeration | OP-PROJ S87 W-8 R3 KO=6 collapse claim DOES NOT transfer to STATE-PROJ; the two layers are structurally distinct per algebra-axis orthogonality K-counter MANDATORY at K=3 |
| B | Multi-orbit bot20 cover C ((1,1)+(0,2)+(2,0) added) shifts ⟨chi, g_X⟩ from (+8, +20, +8) to (0, +12, 0): chi_tri orthogonal to g_C, g_M but NOT g_H | GEOMETRIC | VERIFIED via Sage-QQ on 4 covers | §W2-2 +8/+20/+8 numbers ARE L_max-conditional sampling artifacts, but chi_tri does NOT resurrect at multi-orbit support — the FAIL pattern shifts to (0, +12, 0) with cocycle Δ_0 = 16 still ≠ 0 |
| C | Parallelogram cocycle Δ_0(σ_tri, σ_M; m(·,·)) = 4 · Σ m(p,q) · 𝟙[chi_tri(p,q)=−1 AND g_M(p,q)=−1] is L_max-INVARIANT in form; Δ_0 ≠ 0 robust to multi-orbit covers | GEOMETRIC | PROVED via Sage-QQ; consistent with §VII.AD LOCALIZATION FORMULA Δ_0 = 4·c_{σ⁻¹((−1,−1))} | V_4-on-triality-mod-2 candidate (iii) STRUCTURALLY CLOSED at all L_max ≥ 6; V_4-on-strata SOLE-SURVIVING incarnation; cocycle layer is the L_max-INVARIANT structural pin |
| D | OP-PROJ KO=6 collapse (S87 W-8 R3) and STATE-PROJ Schur inner-product test (§W2-2) yield STRUCTURALLY DIFFERENT verdicts; both are valid at their respective layers | GEOMETRIC | RESOLVED via algebra-axis orthogonality K-counter MANDATORY at K=3 | §VII.AJ.V4-III registry slot SHOULD split into .OP-PROJ + .STATE-PROJ per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY clause |
| E | The L_max=6 +8/+20/+8 conspiracy is a sampling-rank-deficiency artifact: chi_tri = g_M·g_C and chi_tri = g_H both ALIAS on the 3-sector mini-cone (each Z_3 class sampled exactly once) but FAIL on multi-orbit covers | GEOMETRIC | PROVED algebraically + verified via Sage-QQ on sentinel sectors (1,1)/(0,2)/(2,0) | The "chi_tri collapses to (g_C, g_H, g_M) span" reading at L_max=6 is INSTANCE OF THE Z_3-vs-Z_2-aliasing pattern on rank-restricted samples; broken by ANY cover with two representatives of any Z_3 class |
| F | bot20 sector occupation has Level-1 (sampling-conditional multiplicity vector) AND Level-2 (cocycle Δ_0 ≠ 0 invariant under multiplicity deformation) components linked by layer-functor F: m ↦ Δ_0 | GEOMETRIC | calibration corpus instance #2 for `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` | K-counter for that rule advances 1 → 2 (toward MANDATORY at K=3) |
| G | Plan §W2-2.9 PASS/FAIL/INFO predicate UNDERDETERMINED for structural-vs-L_max-conditional adjudication; both readings consistent with same numerical signature | METHODOLOGY | PRU Class 8.2 calibration corpus instance #3 candidate | Class 8.2 K-counter advances 2 → 3 (promotes K=1 SUGGESTION → K=3 MANDATORY); future V_4 pre-registrations MUST pre-register L_max-asymptotic ratio criterion |
| H | §W2-1 PASS-d=2-exact rank-3 Klein-product extensions on substrate-stratum-Z_2 axes are STRUCTURALLY substrate-physical at all L_max (NOT L_max-conditional) | GEOMETRIC | VERDICT UNCHANGED (W2-1 PASS authoritative); cross-implication clarified | Downstream cross-pillar bridges (FWD-C1/C2/C3) may inherit rank-3 substrate axis as Level-2 observable per §W2-10; rank-3 channel does NOT inherit triality-channel L_max-conditional caveat |
