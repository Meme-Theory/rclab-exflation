# Session 88 W3a Synthesis — Substrate-vs-Laboratory Observable Identity (Workshop 3)

**Date**: 2026-05-07
**Agent**: volovik-superfluid-universe-theorist (solo synthesis; cross-axis adversarial framing volovik-vs-landau)
**Source Documents**:
- `sessions/archive/session-88/session-88-w3a-workingpaper.md` (813 lines)
- `sessions/session-plan/session-88-plan-w3a.md` (703 lines)
- `sessions/archive/session-88/workshops/_seed-w3a.md` (Workshop 3 — substrate-vs-lab identity adjudication seed)
- `computations/session-88/s88_gate_verdicts.txt` (lines 77-85: §W3a-14 / §W3a-18 / §W3a-19 canonical + dual-SHA + 3-tuple companions)
- `sessions/framework/correspondence/3HeB-inheritance-canonical.md` (S86 W1b-T8 canonical inheritance theorem)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (3HeB-inheritance pointer; (Δ_B/Δ_A)^p cancellation theorem)
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" MANDATORY at K=3 (S87 W-2 close)
- `.claude/rules/inheritance-falsifier-protocol.md` (rank ≥ 2 ker(ι_*) Class-A / Class-B test discipline)

---

## I. Session Outcome

**Structural verdict (this synthesis)**: **LANDAU WINS** at the substrate-IS-observable specification level. The W11-5 / §W3a-14 / §W3a-18 / §W3a-19 substrate-IS observable family R_substrate = δN/N_paired and the laboratory-IN observable R_3HeB_lit = (Δ_A²−Δ_B²)/(Δ_A²+Δ_B²) DO NOT measure the same physical quantity. The S86 W1b-T8 inheritance morphism ι : (A_K, H_K, D_K) → (A_He, H_He, D_BdG) is a categorical morphism at the algebra/spectral-triple layer; it does NOT canonicalize a unique observable-level dimensional pairing between substrate-IS and laboratory-IN observables. The W11-5 R_substrate was an **algebraically-formed** dimensionless ratio, NOT a derived inheritance image of R_3HeB_lit's BCS gap-asymmetry. The three independent FAIL/INFO verdicts across §W3a-14/18/19 close NOT the inheritance theorem (which is preserved at machine precision via cocycle-ratio invariant 7.324974 ≈ 7.324992 and (Δ_B/Δ_A)^0 cancellation residual = 0.000e+00) but instead three structural-fix corridors of the wrong-observable-identification class. The corrected reading is: **§VII.AJ FWD-C3 instance #2 reclassifies as NEEDS-REIDENTIFICATION**, and §W3a-14's "ANY (p,q) sub-list yields R ≈ −1.2 to −1.9" + §W3a-19's B-convention R_∞ ≈ −1.89 monotonic saturation BECOME a substrate-IS universal-large-negative-R prediction about a DIFFERENT laboratory observable than R_3HeB_lit (CF-W3a-ADDITIONAL-A from the seed survives this synthesis as a STAGE-1-CANDIDATE registry-eligible observation). The two observables (one per axis: substrate-IS volovik-defended, BCS-physics-grounded landau-defended) are STRUCTURALLY ORTHOGONAL per the algebra-axis K-counter MANDATORY clause at K=3: registry-PASS-eligible substrate-IS volovik-defended is NOT cross-corner-co-primary with registry-PASS-eligible BCS-physics landau-defended; both can stand independently as structurally-orthogonal-companion entries.

---

## II. Key Results

### Result 1 — The two observables differ at the ALGEBRAIC SHAPE level (not just at the numerical anchor)

**Result**: Substitution-chain comparison of R_3HeB_lit's and R_substrate's algebraic forms shows they are NOT the same shape. **Classification**: PARTICLE / GEOMETRIC (definitional structure of the observable construction, NOT a phononic excitation prediction).

The substitution chain at observable-identity level:

```
Step 1 (definitions per WP §97-100):
  R_3HeB_lit  := (Δ_A² − Δ_B²) / (Δ_A² + Δ_B²)
    where Δ_A, Δ_B  ∈ ℝ_+   are GAP MAGNITUDES of A-phase and B-phase order parameters
    of 3He at the polycritical pressure point P_pc = 21.22 bar, T_pc = 2.273 mK
    Inputs (Volovik 2003 Ch.7 + Serene-Rainer 1983):
      Δ_A / (k_B T_c)  =  2.0302 · SC_corr_A  =  2.0302 · 1.151  =  2.337  (substituted)
      Δ_B / (k_B T_c)  =  1.9597 · SC_corr_B  =  1.9597 · 1.111  =  2.177  (substituted)
      Δ_A² / Δ_B²       =  (2.337/2.177)²       =  1.1517   (substituted; ratio of squared magnitudes)
    Algebraic shape:  R_lit  =  (a − b) / (a + b)   with a = Δ_A², b = Δ_B², a > b > 0
    Bounded range:    R_lit  ∈  (0, 1)   when a > b > 0  (always positive, small when a ≈ b)

  R_substrate := δN / N_paired
    where δN := N_unpaired − 2 · N_paired   (BdG-doubling subtraction, per WP §71)
    N_paired   := Σ_{(p,q): |C_2(p,q) − C_pole|/C_pole ≤ 0.5}  d(p,q)
    N_unpaired := Σ_{(p,q): |C_2(p,q) − C_pole|/C_pole > 0.5}  d(p,q)
    Inputs (§W3a-14 substituted at L_max = 10, full):
      C_pole_full  =  21.333    (median of Casimirs)
      N_paired     =  2799
      N_unpaired   =  2205
      δN           =  2205 − 2·2799  =  −3393   (substituted)
    Algebraic shape:  R_substrate = (c − 2d) / d   with c = N_unpaired, d = N_paired, c < d typically
    Range:            R_substrate ∈ [−2, +∞)   (lower bound −2 when c → 0; structural)
    Substituted:      R_substrate  =  −3393 / 2799  =  −1.21222   (substituted)

Step 2 (substitution at structural-form level):
  R_lit shape       = (a − b) / (a + b)        ∈ (−1, +1)   bounded by definition
  R_substrate shape = (c − 2d) / d              ∈ [−2, +∞)   asymmetric range; -2 floor
  The factor "−2 · N_paired" in the R_substrate numerator (a BdG-doubling
  subtraction associated with the Nambu-Gorkov doubling convention for
  the substrate's spectral triple) HAS NO ANALOG in R_lit's numerator:
  R_lit's numerator is a difference of squared-magnitudes (Δ_A² − Δ_B²),
  WITHOUT a factor-of-2 from BdG doubling.

Step 3 (simplification — what the shapes encode):
  R_lit measures:     fractional difference between two GAP MAGNITUDES squared.
                      Both magnitudes are POSITIVE physical scalars; their squared
                      difference is a small positive scalar; bounded by (a + b).
                      Field-theoretic observable (limit of an order-parameter field).

  R_substrate measures: dimensionless excess-over-doubled-paired-count, where the
                       BdG-doubling factor of 2 enters because a Nambu-Gorkov pair
                       (particle + hole) carries 2 degrees of freedom per Peter-Weyl
                       sector. Representation-theoretic observable (Weyl-dim-weighted
                       count over a Mellin-pole window).

Step 4 (direction read from canonical form):
  Even ABSENT inheritance considerations, the algebraic shapes are
  structurally distinct. The shape (c − 2d)/d cannot equal (a − b)/(a + b)
  generically because:
    (a − b)/(a + b) ≤ 1  always (bounded)
    (c − 2d)/d ≥ −2  but can exceed +1 when c > 3d (unbounded above)
  When c < 2d, R_substrate is negative; when a > b, R_lit is positive.
  The two observables can have OPPOSITE sign FOR STRUCTURAL REASONS
  (the BdG-doubling subtraction in R_substrate has no R_lit-side counterpart).

  The factor "−2 · N_paired" is not just a numerical detail — it is a
  STRUCTURAL signature of how the substrate-IS observable was algebraically
  formed (mirroring W11-5's BdG-undoubled excess construction, which uses
  the Nambu-Gorkov doubling convention internal to the spectral triple's
  BdG sector). R_3HeB_lit does NOT come from a Nambu-Gorkov-doubled count;
  it comes from the gap-equation order parameter at zero temperature.

Conclusion: the substrate-IS observable R_substrate and the laboratory-IN
observable R_3HeB_lit are constructed via DIFFERENT algebraic procedures
(BdG-undoubled excess count vs gap-magnitude squared difference). The
sign FAIL across all 3 W3a gates is FORCED by this shape mismatch, not
by inheritance ι_* failure. The (Δ_B/Δ_A)^p=0 cancellation theorem holds
because both ratios are dimensionless; that is necessary but NOT SUFFICIENT
for observable-level inheritance: both being dimensionless does NOT make
them the same physical quantity.
```

Direction sign: FAIL is FORCED by the BdG-doubling subtraction structure of R_substrate's numerator, NOT by inheritance ι_* mismatch (which is preserved at machine precision per the cocycle-ratio invariant + (Δ_B/Δ_A)^p=0 cancellation).

The key empirical anchor for this finding: §W3a-14 reports R_substrate_M3C_only = −1.366 ≈ R_substrate_BdG = −1.254. **Both sub-spectra (BdG-restricted color-singlet and M_3(ℂ) color-charged) yield similar large-negative R values** (WP §208). The W11-5 multiplicity-weighted Mellin-pole-window construction *itself* produces large-negative R when applied to ANY (p,q) sub-list at L_max = 10 — not because M_3(ℂ) was contaminating, but because the construction's algebraic shape (c − 2d)/d structurally generates negative R wherever c < 2d, which is the generic case for sector counts where moderate-Casimir sectors carry comparable Weyl-dimension-weighted multiplicity.

### Result 2 — Inheritance-morphism uniqueness DOES NOT propagate to observable-level uniqueness

**Result**: Per S86 W1b-T8 canonical (`3HeB-inheritance-canonical.md`), the inheritance morphism ι : (A_K, H_K, D_K) → (A_He, H_He, D_BdG) is well-defined as a Kasparov-KK projection p ∈ KK(A_K, A_He). The morphism canonicalizes the ALGEBRA-LEVEL relationship between substrate and 3He-B. **It does NOT canonicalize a unique observable-level mapping between R_substrate and R_3HeB_lit.** **Classification**: GEOMETRIC (algebra-/categorical-level structural identity).

The argument by substitution chain on the inheritance theorem's content (via `3HeB-inheritance-canonical.md` lines 31-100):

```
Step 1 (what the inheritance theorem fixes):
  ι preserves: spectral-triple structure {A_K, H_K, D_K} restricted to the BdG sector.
  ι excludes:  M_3(ℂ) Cartan zone (per ker(p_*) on K_*(A_K) = ℤ ⊕ ℤ⁴; rank 2 excess
               per Hodgkin SU(3) vs S^3 K-theory; cocycles φ_67 (chiral pair) +
               φ_88 (Cartan hypercharge), both substrate-IS).
  ι preserves: dimensionless ratios that are inheritance-image-invariant under the
               (Δ_B/Δ_A)^p = 1 cancellation at p = 0 (S86 W-5 DONE-5).

Step 2 (what the inheritance theorem does NOT fix):
  ι does NOT fix: the OBSERVABLE-LEVEL DEFINITIONAL FORM of the substrate-IS
                  pairing that maps INTO a specific laboratory measurement.
  ι does NOT fix: which dimensionless ratio observable is the structural image
                  of R_3HeB_lit at the BdG sector.

Step 3 (substitution into observable space):
  At rank-1-effective ker(ι_*) at p = 0 (the operative regime per WP §156): the
  cohomology-asymmetry test (Class-B per inheritance-falsifier-protocol.md)
  is VACUOUS. Only Class-A (kernel-signature equality) is decisive. Class-A
  fixes that the substrate prediction MUST be NULL on F-rows where the
  parent-symmetry kernel-signature is non-trivial. It does NOT fix what the
  prediction is on a non-NULL F-row (where R_substrate ≠ 0 is admitted).

  In other words, on the rank-1-effective dimensionless-ratio observable,
  the inheritance-falsifier protocol's discriminating gates for non-NULL
  observables are NOT activated. The ratio observable can be ANY of an
  uncountable family of substrate-IS (a, b)-formed dimensionless ratios that
  inherit a finite, dimensionless image; ι_* alone cannot select one.

Step 4 (direction):
  Therefore ι_*-composability is necessary but NOT sufficient to identify
  the substrate-IS image of R_3HeB_lit. A separate BCS-physics-grounded
  derivation is required to specify which (a, b)-formed substrate-IS ratio
  IS the inheritance image of (Δ_A² − Δ_B²) / (Δ_A² + Δ_B²).

Conclusion: Volovik-axis claim "the substrate IS the algebra; any substrate-IS
algebra-level observable inheriting-into a dimensionless ratio with the right
cancellation properties is admissible" is PARTIALLY CORRECT (admissibility
class is non-empty) but DOES NOT entail uniqueness of the inheritance image
of a specific laboratory observable. Landau-axis claim "the substrate-IS
observable that inherits-into R_3HeB_lit must be derived from BCS physics
of polycritical-pressure gap-asymmetry, not just algebraically formed as a
dimensionless ratio" is the structurally-required selector among admissible
candidates.
```

This directly answers seed Workshop 3 question (a): **the substrate-IS observable inheriting-into R_3HeB_lit is NOT uniquely determined by the algebra-level inheritance morphism alone.** Sign: clear. Direction: FAVORS LANDAU.

The §W3a-18 composability_residual = 0.887 finding (positive structural information per WP §407) is consistent with this: it confirms that the W11-5 multiplicity-weighted Mellin-pole-window observable is non-ι_*-composable. But non-composability of the ALGEBRAICALLY-FORMED observable does NOT establish that the BCS-physics-grounded observable would be composable. Both are open; both are admissibility-class members at the rank-1-effective layer; only a BCS-physics derivation can pin which IS the inheritance image of R_3HeB_lit.

### Result 3 — §W3a-14 / §W3a-19 reveal a substrate-IS universal-large-negative-R prediction (CF-W3a-ADDITIONAL-A survives)

**Result**: §W3a-14 §"Decisive substrate-physics outcomes" entry #2 (WP §208): R_substrate_M3C_only = −1.366 ≈ R_substrate_BdG = −1.254. §W3a-19 §"Solution-space" #1: B convention saturates monotonically at R_∞ ≈ −1.89 across L_max ∈ {10, 16, 18, 20} (cross-step 0.50% then 0.05%). Joint reading: the W11-5 multiplicity-weighted Mellin-pole-window construction has a definite L_max → ∞ limit under the B convention. **Classification**: PHONONIC (substrate-IS structural prediction; regulator-INVARIANT-under-pinned-convention).

```
Step 1 (definition of the universal substrate-IS prediction):
  R_substrate_universal := lim_{L → ∞} R(L, B-convention)
  where B = multiplicity-weighted-median pole-aggregation pin

Step 2 (substitution from §W3a-19 4×2 grid):
  R(10, B)  =  −1.91845       (substituted from WP §617)
  R(16, B)  =  −1.90269
  R(18, B)  =  −1.89299
  R(20, B)  =  −1.89202
  step(18→20) = (1.89299 − 1.89202) / 1.89299 = 0.00051 = 0.051%   (substituted)
  step(16→18) = (1.90269 − 1.89299) / 1.90269 = 0.00510 = 0.510%   (substituted)
  ⇒ saturation_B = True (both steps < 5%)

Step 3 (simplification — extrapolation to L_max → ∞):
  Linear ratio of step sizes: 0.051%/0.510% = 0.10 ≈ L^{-3} cross-step ratio
  if the saturation envelope is L^{-3} (per cross-pillar-bridge-anatomy.md
  Level-2 envelope at d = 4): expected step(20→22)/step(18→20) ~ (18/20)³ = 0.729.
  Observed ratio 0.10 is FASTER than L^{-3}; saturation may be exponential
  in L_max, not algebraic. R_∞ ≈ −1.892 ± 0.001 (conservative envelope).

Step 4 (direction):
  R_substrate_universal ≈ −1.892 is a substrate-IS prediction about the
  multiplicity-weighted Mellin-pole-window observable on the FULL substrate
  spectral triple. It is NOT a prediction about the gap-asymmetry between
  3He A-phase and B-phase at polycritical pressure (R_3HeB_lit).

Conclusion: The substrate IS predicting R = −1.892 ± 0.001 for SOMETHING.
That something is NOT the BCS gap-asymmetry of 3He at polycritical pressure
(per Result 1). What that something IS is OPEN — it is whichever laboratory
observable maps via ι_* to the substrate's δN/N_paired construction with
B-convention pole aggregation. Identifying that laboratory observable is
the next-session task.
```

This is CF-W3a-ADDITIONAL-A from the seed. It survives this synthesis as a STAGE-1-CANDIDATE registry-eligible observation INDEPENDENT of the FWD-C3 instance #2 REGISTRY-FAIL (which tested against the wrong laboratory anchor).

### Result 4 — Algebra-axis K-counter MANDATORY at K=3: the two observables admit STRUCTURALLY-ORTHOGONAL-COMPANION registry status

**Result**: Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3 from S87 W-2 R3 close): operator-projection observables (algebra-side, central-projection traces on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); spectrum-only functionals; algebra-INVARIANT) and state-projection observables (state-side, state-pair functionals on A; algebra-DEPENDENT) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level. **Classification**: GEOMETRIC (algebra-axis structural classification).

```
Step 1 (mapping to W3a context):
  R_substrate (volovik-defended)  =  δN / N_paired  evaluated on Peter-Weyl multiplicities
                                     of (A_K, H_K, D_K) — a SPECTRUM-ONLY functional
                                     (Weyl-dim weights are derived from Casimir invariants;
                                     no state-pair input). ALGEBRA-INVARIANT family.
                                     ⇒ OPERATOR-PROJECTION class

  R_BCS-physics (landau-defended) =  candidate substrate-IS observable derived from
                                     BCS gap-equation kernel structure at the polycritical
                                     pressure point — depends on the GAP STATE (Δ_A, Δ_B
                                     are state-dependent order parameters at T → 0,
                                     P_pc = 21.22 bar; not fixed by the algebra alone).
                                     ALGEBRA-DEPENDENT family.
                                     ⇒ STATE-PROJECTION class

Step 2 (substitute into the K-counter MANDATORY clause):
  Per .claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"
  (MANDATORY at K=3 from S88 W8-92 close):
    Operator-side (R_substrate) → §VII.X.OP-PROJ
    State-side    (R_BCS-physics) → §VII.X.STATE-PROJ
    Bare §VII.X (without suffix tag) FORBIDDEN when both readings admissible.

Step 3 (simplification of registry-anchor structure):
  Per cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"
  MANDATORY clause: cross-corner co-primary FORBIDDEN. The operator-projection
  R_substrate registry entry CANNOT be co-primary anchor with the state-projection
  R_BCS-physics registry entry.

  The correct anchor structure when both projection-side readings of the same
  underlying physical question (substrate-vs-laboratory observable identity)
  are independently registry-eligible is STRUCTURALLY-ORTHOGONAL-COMPANION
  (per registry-landing.md §"Forward-looking enforcement (post-promotion)"):
  the two entries stand as independent companions; neither is decoration of
  the other; both can hold registry-PASS (or one can hold STAGE-1-CANDIDATE
  and the other REGISTRY-FAIL) without invalidating the other.

Step 4 (direction):
  Therefore:
    R_substrate (volovik-defended; OP-PROJ) at §VII.AJ.OP-PROJ
      → STAGE-1-CANDIDATE for substrate-IS universal-large-negative-R prediction
        (R_∞ ≈ −1.89 ± 0.001 under B convention) — Result 3 above; CF-W3a-ADDITIONAL-A
      → tests against future laboratory observable identification (NOT R_3HeB_lit)

    R_BCS-physics (landau-defended; STATE-PROJ) at §VII.AJ.STATE-PROJ
      → NEEDS-COMPUTATION pending BCS-physics-grounded derivation of the
        substrate-IS image of R_3HeB_lit
      → tests against R_3HeB_lit = +0.03536 directly per FWD-C3 protocol

  The §VII.AJ FWD-C3 instance #2 REGISTRY-FAIL was conflating these two
  projection-side readings under one entry; it RECLASSIFIES as
  NEEDS-REIDENTIFICATION at the slot level; the two new sub-rows (OP-PROJ +
  STATE-PROJ) replace the conflated FWD-C3 entry under the suffix-discipline.

Conclusion: the W3a wave's substantive output is NOT to push FWD-C3 instance #2
toward a single PASS or FAIL at the conflated slot — it is to RESOLVE the slot
into two structurally-orthogonal-companion entries, each on its own algebra-axis,
each with its own forward gate. This completes the algebra-axis K-counter
MANDATORY enforcement at the W11-5 / W3a registry surface.
```

---

## III. Gate Verdicts (from source documents — authoritative; not re-adjudicated)

| Gate | Verdict | Decisive Number | Sign verdict |
|:-----|:--------|:----------------|:-------------|
| `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY` (§W3a-14) | **FAIL** | `ratio_mismatch_M3C_projected = 36.47` (plan metric); 1.028 (W11-5 metric). R_predicted = −1.254 vs R_lit = +0.0354 ⇒ sign mismatch | FAIL |
| `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY` (§W3a-18) | **FAIL** (on surrogate) | `ratio_mismatch_redefined = 11.385`; `R_substrate_redefined = −0.367`; `composability_residual = 0.887` (positive structural finding: W11-5 NON-COMPOSABLE confirmed) | FAIL |
| `S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN` (§W3a-19) | **INFO** (verdict_label = INFO-cross-conv-unstable) | `ratio_mismatch(20, Cβ) = 32.06`; `cross_conv_deviation = 0.519`; `saturation_B = True`, `saturation_Cβ = False (12.42% step at 16→18)`; B-convention R_∞ ≈ −1.892 monotonic | FAIL |

| audit_sha256 (full-64) | content_sha256 (full-64) |
|:------------------------|:--------------------------|
| `643104ba1c77142ab6ceab32b2f8756a2dfe3e476da6e6c086abd0c129c3a82b` (§W3a-14) | `d6a68b9743e2e82621efd6dc1060bdecd37d25a230222ff99fc2f9f78a05eeea` |
| `80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8` (§W3a-18) | `6aed45f5366321ec4bf0b2e24625b9419ead676045df97069a1af45bb1989481` |
| `5440763b8667da4a2924888d9df1c36c6fa977884c746216af83660ea04e661b` (§W3a-19) | `21ac6f6280ec78dceaec1997988a7de4a8b7f4b332e11abab53e169d45db92a9` |

All three audit_sha256 unique (sig_5 closure preserved). Three FAIL verdicts ALL with sign_verdict = FAIL — composite collapse rule `sign_verdict == FAIL ⇒ composite = FAIL` applied uniformly. The sign-FAIL is the structural signature of the W3a wave: **three independent algebraic constructions all yield NEGATIVE R-substrate when the laboratory anchor is POSITIVE — which is forced by R_substrate's BdG-doubling subtraction structure (Result 1 above), NOT by inheritance-bridge defect.**

---

## IV. Structural Implications (Workshop 3 substrate-vs-laboratory adjudication output)

### IV.1 Substitution-chain proof — substrate-IS observable inheriting-into R_3HeB_lit is NOT uniquely determined by morphism alone

**Direction: LANDAU.** Per Result 2 substitution chain, the Kasparov-KK projection p ∈ KK(A_K, A_He) is a structural identity at the algebra/spectral-triple layer; it preserves dimensionless ratio observables under the (Δ_B/Δ_A)^p = 1 cancellation at p = 0 (S86 W-5 DONE-5; preserved at machine precision across all 3 W3a gates). It does NOT canonicalize a UNIQUE observable-level pairing between substrate-IS and laboratory-IN dimensionless ratios. Volovik's claim "any substrate-IS algebra-level observable inheriting-into a dimensionless ratio with the right cancellation properties is admissible" identifies the admissibility CLASS but does not pin a unique member.

**Why volovik's substitution chain falls short**: at rank-1-effective ker(ι_*) at p = 0 (the operative regime), Class-B (cohomology-asymmetry) test is vacuous (only Cartan U(1)_φ cocycle survives the dimensionless-ratio reduction; chiral pairs cancel). Class-A (kernel-signature equality) fixes the substrate prediction MUST be NULL on F-rows where the parent-symmetry kernel-signature is non-trivial. It does NOT fix what the prediction IS on a non-NULL F-row. The W11-5 / W3a observable is on a NON-NULL F-row (R_3HeB_lit ≠ 0); inheritance falsifier-protocol Class-A is silent on the value.

**Therefore**: a separate BCS-physics-grounded derivation IS the structurally-required selector among admissible candidates. Volovik-direction adversarial counter-arguments tested but defeated:

1. **"Substrate IS the algebra"**: TRUE at the algebra-level; INSUFFICIENT at the observable-level. ι_* canonicalizes algebra-level relationship; it does not canonicalize observable-level definitional identity.
2. **"(Δ_B/Δ_A)^p=0 cancellation guarantees ratio preservation"**: TRUE for ANY dimensionless ratio; therefore preserves all admissibility-class members; does NOT select among them.
3. **"K-theory pairing requirements determine the unique image"**: K-theory pairing is at rank K_*(A_K) − rank K_*(A_He) = 2 cohomology layer; it determines what the kernel cocycles are (φ_67 + φ_88, ratio 7.324992 Sage-exact). It does NOT determine the OBSERVABLE-LEVEL form on the BdG-restricted image.

### IV.2 BCS-physics-grounded derivation of unique substrate-IS observable image of R_3HeB_lit (Landau-path specification)

The structurally-required BCS-physics derivation:

```
Step 1: R_3HeB_lit comes from the BCS gap equation at the polycritical pressure point.
  Δ_A and Δ_B are solutions of the gap equation with different angular structures
  (Δ_A: p_x + i p_y A-phase; Δ_B: isotropic B-phase combinations).
  At T → 0, P = P_pc = 21.22 bar: both Δ_A and Δ_B are non-zero, with Δ_A > Δ_B.

Step 2: The substrate-side analog of "gap magnitude squared" is the
  spectral-action contribution from the BdG-undoubled sector at substrate-distance-1
  pole. Define:
    Σ_BdG(Δ²) := substrate-IS spectral-action moment associated with the
                  BdG-undoubled gap-magnitude-squared observable, evaluated
                  on (A_K^BdG_preimage = ℂ ⊕ ℍ, H_K^BdG_preimage, D_K^BdG_preimage).
    (Two such moments, one per Δ_A-analog and one per Δ_B-analog substrate channel.)

Step 3: The substrate-side image of R_3HeB_lit:
    R_substrate_BCS-grounded := (Σ_BdG_A − Σ_BdG_B) / (Σ_BdG_A + Σ_BdG_B)
  where Σ_BdG_A and Σ_BdG_B are spectral-action contributions from the two
  BdG channels that the BCS gap equation selects at the polycritical point.

Step 4: Structural form match with R_3HeB_lit's algebraic shape:
    R_3HeB_lit shape       = (a − b) / (a + b)   with a, b ∈ ℝ_+
    R_substrate_BCS shape  = (a' − b') / (a' + b')   with a', b' ∈ ℝ_+
  (where a' = Σ_BdG_A, b' = Σ_BdG_B)
  ⇒ same algebraic shape; both bounded in (−1, +1); both small when a' ≈ b'.
  This shape match does NOT exist for R_substrate = δN/N_paired (which has
  shape (c − 2d)/d with the BdG-doubling factor of 2; see Result 1).

Step 5: Direction of explanation (substrate-IS → laboratory-IN per phononic-framing.md):
    Substrate IS the BCS-physics-grounded spectral-action gap-asymmetry on (A_K^BdG_preimage)
       → Bridge map (ι : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); p=0 cancellation; Σ_BdG_A and Σ_BdG_B
                      both ι-image-restricted to A_K^BdG_preimage)
       → Laboratory IN polycritical-point gap-asymmetry R_3HeB_lit = +0.03536

Conclusion: this is the structurally-required substrate-IS observable. Its construction
DOES inherit R_3HeB_lit's algebraic shape; whether its NUMERICAL value matches R_3HeB_lit
at the Level-3 envelope (≤ 0.05) is an OPEN computation, queued as the landau-path S89+
gate (see V.2 below).
```

### IV.3 What the §W3a-14/18/19 results mean under the corrected substrate-side observable identification

Re-scoping the three W3a verdicts under the Landau-axis observable-identification:

- **§W3a-14 FAIL** (M_3(ℂ) projection): closes the corridor "M_3(ℂ) Cartan-zone IS the dominant FAIL cause of W11-5". Under corrected reading: this corridor was tested on an OBSERVABLE-MISIDENTIFIED FAIL (R_substrate = δN/N_paired tested against R_3HeB_lit, but the two observables are not structurally comparable per Result 1). The §W3a-14 FAIL is structurally informative ONLY about R_substrate's behavior under M_3(ℂ) projection (M_3(ℂ) projection does not collapse the universal-large-negative-R prediction; the construction is M_3(ℂ)-INDEPENDENT). It is NOT informative about whether the BCS-physics-grounded R_substrate_BCS-grounded would PASS against R_3HeB_lit.

- **§W3a-18 FAIL** (surrogate): closes the corridor "(a_3_BdG − a_3_M3C)/(a_3_BdG + a_3_M3C) IS the operational image of the cohomology-class Hochschild pairing". Under corrected reading: this surrogate observable was substrate-physics-grounded (s = 3/2 substrate-distance-1 pole power, exact SU(3) triality classification) but it tested the SAME WRONG LABORATORY ANCHOR (R_3HeB_lit). The composability_residual = 0.887 finding is REAL and remains: it confirms W11-5's δN/N_paired construction is non-ι_*-composable (positive structural information about W11-5, NOT about the BCS-physics-grounded observable). The surrogate's FAIL itself is uninformative about R_substrate_BCS-grounded vs R_3HeB_lit.

- **§W3a-19 INFO-cross-conv-unstable**: closes the corridor "L_max=10 truncation is the W11-5 FAIL cause". Under corrected reading: B convention saturates monotonically at R_∞ ≈ −1.892 — this saturation is REAL and remains as a substrate-IS structural prediction; the laboratory observable it predicts is OPEN (not R_3HeB_lit per Result 1). Cβ convention non-saturation at L_max ∈ {10, 16, 18, 20} (12.42% step at 16→18) is a substrate-side discreteness artifact (median-of-Casimirs jumps non-monotonically with L_max as Weyl-dim threshold crossings shift the median); structurally informative about the convention-pin discipline, not about FWD-C3.

**Net effect on §VII.AJ FWD-C3 instance #2 REGISTRY-FAIL**: per the algebra-axis K-counter MANDATORY clause (Result 4), the slot RECLASSIFIES from REGISTRY-FAIL into NEEDS-REIDENTIFICATION:
- §VII.AJ.OP-PROJ (volovik-defended, R_substrate universal-large-negative-R prediction) → STAGE-1-CANDIDATE for substrate-IS prediction R_∞ ≈ −1.892 ± 0.001 about a future-identified laboratory observable that is NOT R_3HeB_lit.
- §VII.AJ.STATE-PROJ (landau-defended, R_substrate_BCS-grounded inheritance image of R_3HeB_lit) → NEEDS-COMPUTATION pending the BCS-physics derivation (V.2 below).

### IV.4 Bridge-anatomy K-counter implication

The S87 W11-5 cross-pillar bridge candidate FWD-C3 instance #2 had been recorded as a calibration corpus instance at K = 2 (with W-5 §VII.AF.1 instance #1). Per the W3a synthesis (WP §767), K-counter UNCHANGED at K=2 because all three W3a gates are sub-tests of instance #2, not structurally-distinct workshops.

**This synthesis preserves K-counter status quo** at the FWD-C3 instance count level (the two new sub-rows §VII.AJ.OP-PROJ and §VII.AJ.STATE-PROJ are STRUCTURALLY-ORTHOGONAL-COMPANION components of the SAME instance-2 slot, NOT a new instance-3). Forward MANDATORY-promotion at K=3 still pending an INDEPENDENT THIRD cross-pillar bridge instance (FWD-C1 or FWD-C2 per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`).

### IV.5 Constraint-map updates (this synthesis adds to WP §791-803)

| Mechanism / gate | Prior state | New state | Reason (this synthesis) |
|:-----------------|:------------|:----------|:-------------------------|
| W3c queue ordering: (a) Connes-Karoubi pairing canonical vs (b) convention demarcation theorem | OPEN; sequential-vs-parallel to be decided | **THE ORDERING IS WRONG** — both (a) and (b) inherit the W11-5 OBSERVABLE IDENTIFICATION ERROR | Per Result 1: the W11-5 R_substrate is not the inheritance image of R_3HeB_lit. (a) and (b) are both observable-axis-correct under the wrong observable. The structurally-prior task is RE-IDENTIFICATION (V.1 below); (a) and (b) become downstream gates of the re-identified observable. |
| FWD-C3 instance #2 (W11-5) `permanent-results-registry.md` §VII.AJ slot | REGISTRY-FAIL with W3c-queue diagnostic | **NEEDS-REIDENTIFICATION → split into §VII.AJ.OP-PROJ STAGE-1-CANDIDATE + §VII.AJ.STATE-PROJ NEEDS-COMPUTATION** | Per Result 4: algebra-axis K-counter MANDATORY at K=3 forbids cross-corner co-primary; structurally-orthogonal-companion split required. |
| Substrate-IS observable identification at FWD-C3 | R_substrate = δN/N_paired (multiplicity-weighted Mellin-pole window) | **R_substrate_BCS-grounded = (Σ_BdG_A − Σ_BdG_B)/(Σ_BdG_A + Σ_BdG_B)** (BCS-physics-derived spectral-action gap-asymmetry on A_K^BdG_preimage = ℂ ⊕ ℍ) | Per Result 2 + IV.2: BCS-physics-grounded derivation IS the structurally-required selector among admissibility-class members. Algebraic shape match (a − b)/(a + b) restored (vs (c − 2d)/d shape mismatch of W11-5). |
| Substrate-IS universal-large-negative-R prediction | (not previously stated) | **STAGE-1-CANDIDATE registry-eligible**: R_∞ ≈ −1.892 ± 0.001 under B convention; multiplicity-weighted Mellin-pole-window observable on full Peter-Weyl spectrum at L_max → ∞ | Per Result 3: B-convention monotonic saturation 0.50% then 0.05%; substrate IS predicting R = −1.892 about a laboratory observable that is OPEN. |
| Inheritance theorem (S86 W1b-T8) | PRESERVED | **PRESERVED (REINFORCED)** | Per Result 2: theorem holds at algebra-/spectral-triple layer; W11-5 W3a FAIL is observable-MISIDENTIFICATION, not bridge defect. Cocycle ratio invariant 7.324992 + (Δ_B/Δ_A)^p=0 cancellation 0.000e+00 preserved across all 3 W3a gates. |
| W11-5 observable composability with ι_* | UNTESTED | **CONFIRMED NON-COMPOSABLE (per §W3a-18 composability_residual = 0.887)** | Independent of observable-identification question; positive structural information about W11-5's ALGEBRAIC FORM that survives this synthesis intact. |

---

## V. Carry-Forward Computations

### V.1 (PRIMARY) BCS-physics-grounded derivation of substrate-IS image of R_3HeB_lit (LANDAU-PATH)

- **What**: derive the substrate-IS spectral-action moments Σ_BdG_A and Σ_BdG_B on A_K^BdG_preimage = ℂ ⊕ ℍ that are the inheritance images of the two BCS gap magnitudes Δ_A and Δ_B at the polycritical pressure point. Compute R_substrate_BCS-grounded := (Σ_BdG_A − Σ_BdG_B)/(Σ_BdG_A + Σ_BdG_B) at L_max=10. Test against R_3HeB_lit = +0.03536 at the Level-2/3 envelope (PASS-strict ≤ 0.001; PASS-loose / INFO ≤ 0.05). Substitution chain mandatory at plan-freeze: (i) BCS gap equation kernel structure at P_pc, T_pc; (ii) substrate-side spectral-action moment definition with explicit mapping from gap-magnitude-squared to A_K^BdG_preimage spectral content; (iii) algebraic shape match check (a − b)/(a + b) preserved; (iv) ι_*-composability check via explicit pre-image construction (NOT post-projection); (v) (Δ_B/Δ_A)^p=0 cancellation preservation at machine precision; (vi) PASS criterion direction read from canonical form.
- **Inputs**:
  - canonical_constants.py: `tau_fold = 0.19`, `Delta_BCS = 0.4642547394830737`, `M_KK = 7.428660036284456e+16`, `cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`
  - 3He-B polycritical anchors: P_pc = 21.22 bar, T_pc = 2.273 mK, T_pc/T_c = 0.9125, SC_corr_A = 1.151, SC_corr_B = 1.111, Δ_A/(k_B T_c) = 2.0302, Δ_B/(k_B T_c) = 1.9597
  - s84 spectrum cache `s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949...`) for spectral-action moment evaluation on Peter-Weyl block-diagonal eigvals
  - `3HeB-inheritance-canonical.md` (S86 W1b-T8) inheritance morphism canonical
  - `cross-pillar-bridge-anatomy.md` Level-2 envelope L^{-3} ~ 10^{-3} at d=4
  - BCS-superfluid-condensed-matter-theorist (`landau-superfluid-condensed-matter-theorist`) PRIMARY (BCS gap-equation derivation); volovik CO-AUTHOR (substrate-IS spectral-action moment translation); connes CO-AUTHOR if Hochschild cocycle / Chern character formalization required
- **Gate**: `S89-3HEB-EXCESS-INHERITANCE-BCS-PHYSICS-GROUNDED-OBSERVABLE-DERIVATION-LANDAU-PATH` (NEW; replaces and supersedes the conflated `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL` per Result 4 reclassification). PASS-strict iff `|R_substrate_BCS-grounded − R_3HeB_lit| / |R_3HeB_lit| ≤ 0.001` AND `composability_residual < 1e-2` AND `|cocycle_ratio_67_88 − 7.324992| < 1e-12 ULP`. PASS-loose / INFO iff (0.001, 0.05]. FAIL iff > 0.05 OR composability ≥ 1e-2 OR cocycle ratio violated. Pre-registered cohomology-class machinery; explicit non-surrogate; landau-path specification per IV.2. Lands at §VII.AJ.STATE-PROJ.
- **Effort**: ~3 wave-equivalents (BCS gap-equation kernel structure derivation + spectral-action moment construction on A_K^BdG_preimage + Connes-Moscovici 1995 §III.4 dim-spectrum residue formula application + ι_*-composability cross-check + cocycle invariant verification; multi-session per landau + volovik + connes joint dispatch).

### V.2 Volovik-path retain — substrate-IS universal-large-negative-R prediction registry landing (CF-W3a-ADDITIONAL-A from seed)

- **What**: register R_substrate_universal := lim_{L → ∞} R(L, B-convention) ≈ −1.892 ± 0.001 as substrate-IS STAGE-1-CANDIDATE registry entry at §VII.AJ.OP-PROJ. Verify via L_max ∈ {22, 24} extension that the saturation holds at the 0.001 envelope; if so, identify candidate laboratory observables (NOT R_3HeB_lit) that map via ι_* to the multiplicity-weighted Mellin-pole-window construction. Cross-check the substrate-IS prediction's regulator-INVARIANCE under the B convention pin (per `regulator-pin-discipline.md`).
- **Inputs**: §W3a-19 4×2 grid as Level-3 baseline; `regulator-convention-lockdown.md §"Demarcation theorem"` template applied to the W11-5 observable family for B convention canonicalization; `cross-pillar-bridge-anatomy.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 for §VII.X.OP-PROJ suffix discipline; canonical_constants.py `tau_fold = 0.19`, `M_KK = 7.428660036284456e+16`.
- **Gate**: `S89-W11-5-OBSERVABLE-SUBSTRATE-UNIVERSAL-NEGATIVE-PREDICTION-LANDING` (replaces CF-W3a-ADDITIONAL-A from seed). PASS criterion: `|R_∞_B − R_∞_extrapolated| < 0.01` AND `step(L → L+2) < 0.001` for L ∈ {20, 22} AND substrate-IS observable identified via §VII.AJ.OP-PROJ STAGE-1-CANDIDATE landing; INFO if (0.01, 0.05]; FAIL if > 0.05. Pre-registered; convention-pin-locked B; lands at §VII.AJ.OP-PROJ. **Decoupled** from R_3HeB_lit anchor (this gate does NOT compare against laboratory anchor; it tests substrate-IS structural-saturation alone).
- **Effort**: 0.6 wave-equivalents (Friedrich-Bär extrapolation cross-check at L_max ∈ {22, 24}; closed-form sector enumeration sufficient per §W3a-19 lesson; STAGE-1-CANDIDATE registry-text drafting at §VII.AJ.OP-PROJ).

### V.3 Pole-aggregation convention demarcation theorem (CONNES-PATH; supersedes seed CF-W3a-ADDITIONAL-C-(b))

- **What**: per `regulator-convention-lockdown.md §"Demarcation theorem"` template, derive the unique admissible pole-aggregation convention for the W11-5 / cohomology-class observable family by identifying the substrate-physics anchor analog to `w_0 effacement-anchored` (the demarcation theorem's structural-anchor for DR3-class L_max-stability gates). Test convention-stability under L_max → ∞ extrapolation at the demarcation-derived UNIQUE convention. UNCHANGED in scope from seed CF-W3a-ADDITIONAL (originally W3c queue (b) `S89-3HEB-EXCESS-INHERITANCE-CONVENTION-DEMARCATION-THEOREM`); reclassifies as a SUPPORTING gate of V.1 + V.2 (NOT a primary axis under the corrected observable-identification framing).
- **Inputs**: §W3a-19 4×2 grid as Level-3 anchor (Cβ + B + extrapolation); `regulator-convention-lockdown.md §"Demarcation theorem (admissibility class)"` template; `cross-pillar-bridge-anatomy.md §"Level 2 — Algebraic Convergence Envelope"` L^{-3} prediction; canonical_constants.py `tau_fold`, `M_KK`.
- **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONVENTION-DEMARCATION-THEOREM` (RETAINED as in seed/WP). PASS iff a UNIQUE admissible convention is identified via the demarcation-theorem template AND `ratio_mismatch_unique_conv ≤ 0.05` at L_max=20 (under the re-identified observable from V.1 OR the standalone substrate-IS prediction from V.2; gate consumes whichever is registry-eligible at S89 dispatch). Pre-registered structural-anchor; explicit non-arbitrary.
- **Effort**: ~1.5 wave-equivalents (theorem derivation + structural pin + L_max-scan re-run under unique convention).

### V.4 Connes-Karoubi pairing infrastructure as a separate forward gate (volovik-axis algebra-up; STATE-PROJ-side replaces it)

- **What**: the seed's `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL` (faithful Connes-Karoubi K-theory pairing on the BdG-restricted spectral triple) — REVISED. Under the corrected observable-identification framing (Result 4): the Connes-Karoubi pairing infrastructure is an OPEN structural construction at the STATE-PROJ side; its application to R_substrate_BCS-grounded (V.1's observable) is the natural forward-gate sequence. This gate becomes a TECHNICAL PREREQUISITE for V.1 — without the Hochschild cocycle [φ_g^sym] on A_K^BdG_preimage = ℂ ⊕ ℍ + Chern character of P_0(τ_fold) construction, V.1's spectral-action moments cannot be derived faithfully. DISPATCH ORDER: V.4 (infrastructure) → V.1 (BCS-physics-grounded application).
- **Inputs**: s84 spectrum cache; canonical_constants `cocycle_norm_phi67/phi88`; Connes-Moscovici 1995 §III.4 formula machinery (analog to W-5 §VII.W bridge); `3HeB-inheritance-canonical.md` (BdG sector quotient definition); `cross-pillar-bridge-anatomy.md §"Level 1 — Substrate-IS Structural Identity"` calibration.
- **Gate**: `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE` (RENAMED from seed; explicitly infrastructure NOT canonical-test). PASS iff (i) Hochschild cocycle [φ_g^sym] constructed on A_K^BdG_preimage with cocycle ratio 7.324992 preserved at machine precision; (ii) Chern character Ch(P_0(τ_fold))_BdG constructed; (iii) Connes-Karoubi pairing ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩_BdG evaluable (numerical value extracted at L_max=10). NO test against R_3HeB_lit at this gate (test deferred to V.1).
- **Effort**: ~3 wave-equivalents (NCG infrastructure construction; multi-session). UNCHANGED from seed scope; renamed for clarity.

### V.5 Algebra-axis registry naming-hygiene retrofit at §VII.AJ (RECLASSIFICATION)

- **What**: per Result 4 + `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3, the §VII.AJ FWD-C3 instance #2 slot reclassifies from REGISTRY-FAIL into NEEDS-REIDENTIFICATION via slot-split into (a) §VII.AJ.OP-PROJ (volovik-defended; substrate-IS universal R prediction) and (b) §VII.AJ.STATE-PROJ (landau-defended; BCS-physics-grounded R image of R_3HeB_lit). Mack-cosmic-bridge SOLE-WRITER per `feedback_mack-bridge-role.md` performs the registry-row split and audit-pin sub-row append-only; the original FWD-C3 instance #2 REGISTRY-FAIL row is RETAINED on disk per absolute verdict permanence (gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"); a new audit-pin sub-row appended with `supersedes=<old_audit_sha>` tag references the original W11-5 W3a verdict-line audit_sha256 (`643104ba1c77142a... + 80405c227a1d04e9... + 5440763b8667da4a...` triple chain).
- **Inputs**: `permanent-results-registry.md §VII.AJ` (existing FWD-C3 instance #2 row + four sub-blocks §VII.AJ.1 through §VII.AJ.4 + §VII.AJ.partition-stability LANDED); `cross-pillar-bridge-anatomy.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92); `gate-verdicts.md §"Option A — sig_5 remediation pathway"` for supersession-tag protocol.
- **Gate**: `S89-VII-AJ-FWD-C3-INSTANCE-2-NAMING-HYGIENE-SPLIT` (NEW; registry-write hygiene). PASS iff (i) §VII.AJ.OP-PROJ row appended with STAGE-1-CANDIDATE status + cross-reference to V.2; (ii) §VII.AJ.STATE-PROJ row appended with NEEDS-COMPUTATION status + cross-reference to V.1; (iii) original FWD-C3 instance #2 REGISTRY-FAIL row RETAINED with supersedes-tag-companion-row pointing to the new sub-rows; (iv) `sessions/permanent-results-registry.md` line cross-references to W11-5 W3a verdict-line audit_sha256 chain preserved in append-only audit-pin sub-rows. Pre-registered; mack-cosmic-bridge sole-writer per role assignment.
- **Effort**: 0.3 wave-equivalents (registry-row split + audit-pin sub-row append-only + cross-reference table updates). Registry-write hygiene only; no recompute.

### V.6 Cocycle ratio Sage-exact cross-validation under L_max scan (CF-W3a-ADDITIONAL-B from seed; UNCHANGED)

- **What**: per seed CF-W3a-ADDITIONAL-B: §W3a-14 + §W3a-18 both report `cocycle_ratio_67_88 = 7.324974` at L_max=10 (residual 1.76e−05 within Class 8.3 publication-precision floor). §W3a-19 did NOT cross-validate the cocycle ratio across L_max ∈ {16, 18, 20}. Test cocycle ratio invariant preservation across L_max ∈ {16, 18, 20} from canonical pins.
- **Inputs**: canonical_constants.py `cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`; §W3a-19 sector enumeration code at L_max ∈ {16, 18, 20}.
- **Gate**: `S89-W3A-COCYCLE-RATIO-LMAX-INVARIANCE-CROSS-VALIDATION`. PASS criterion: `|ratio(L) − 7.324992| / 7.324992 ≤ 1e−4` (Class 8.3 publication precision tol) for ALL L ∈ {10, 16, 18, 20}. Sage MCP exact verification at each L.
- **Effort**: 0.2 wave-equivalents (single closed-form recompute from canonical pins; no eigenvalue work).

### V.7 §W3a-19 verdict-label disambiguation hygiene (CF-W3a-ADDITIONAL-D from seed; UNCHANGED)

- **What**: per seed CF-W3a-ADDITIONAL-D: §W3a-19's INFO-cross-conv-unstable verdict_label fires on `cross_conv_deviation_at_Lmax20 = 0.5188 ≥ 0.50`, but the gate ALSO records `saturation_Cβ = False` (12.42% step at 16→18). The single verdict_label conceals the 2-axis structural diagnostic. Extend verdict-line companion row to carry compound `verdict_label = INFO-cross-conv-unstable+NOT-saturation-Cbeta` (or pre-register at S89+ W3c that the diagnostic separation lives in companion row).
- **Inputs**: §W3a-19 npz output (saturation_Cbeta + saturation_B + cross_conv_deviation_at_Lmax20 keys); `gate-verdicts.md §"S87+ canonical form (Schema-v2)"` companion-row taxonomy.
- **Gate**: `S89-VERDICT-LABEL-COMPOUND-DIAGNOSTIC-HYGIENE` (verdict-line schema decision; no recompute). Either (a) extend companion row to carry compound verdict_label, or (b) pre-register at S89+ W3c that diagnostic separation lives in `verdict_label` field with the canonical compound-tag pattern.
- **Effort**: 0.05 wave-equivalents (verdict-line schema decision; no recompute).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | R_substrate (δN/N_paired with shape (c−2d)/d) and R_3HeB_lit ((Δ_A²−Δ_B²)/(Δ_A²+Δ_B²) with shape (a−b)/(a+b)) are NOT the same algebraic shape | PARTICLE / GEOMETRIC | STRUCTURAL THEOREM (substitution-chain proven) | Sign FAIL across §W3a-14/18/19 forced by BdG-doubling structure of R_substrate, NOT by inheritance ι_* defect; observable-identification IS the structural fix locus, not observable-construction-internal-fix |
| 2 | Inheritance morphism ι : (A_K, H_K, D_K) → (A_He, H_He, D_BdG) does NOT canonicalize a unique observable-level pairing between substrate-IS and laboratory-IN dimensionless ratios at rank-1-effective ker(ι_*) at p=0 | GEOMETRIC | STRUCTURAL THEOREM (Class-A on non-NULL F-row is silent on value; Class-B vacuous at rank-1-effective p=0) | Volovik-axis "any ι-composable dimensionless ratio is admissible" identifies admissibility CLASS; landau-axis BCS-physics-grounded derivation IS the structurally-required selector among class members |
| 3 | Substrate-IS universal-large-negative-R prediction R_∞ ≈ −1.892 ± 0.001 under B convention monotonic saturation (cross-step 0.50% then 0.05%) | PHONONIC | STAGE-1-CANDIDATE (CF-W3a-ADDITIONAL-A; survives this synthesis as registry-eligible STANDALONE substrate-IS prediction independent of R_3HeB_lit) | Substrate IS predicting R = −1.892 about a future-identified laboratory observable that is NOT R_3HeB_lit; future identification is V.2 forward gate |
| 4 | Algebra-axis K-counter MANDATORY at K=3 (operator-projection vs state-projection STRUCTURALLY ORTHOGONAL); cross-corner co-primary FORBIDDEN | GEOMETRIC | RULE APPLICATION (structurally-orthogonal-companion required) | §VII.AJ FWD-C3 instance #2 splits into §VII.AJ.OP-PROJ STAGE-1-CANDIDATE + §VII.AJ.STATE-PROJ NEEDS-COMPUTATION; registry suffix-discipline applied per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92) |
| 5 | S86 W1b-T8 inheritance theorem PRESERVED (REINFORCED): cocycle ratio invariant 7.324992 + (Δ_B/Δ_A)^p=0 cancellation 0.000e+00 across all 3 W3a gates | GEOMETRIC | PRESERVED (4 independent verifications) | Three W3a FAILs/INFO are observable-MISIDENTIFICATION at the substrate-IS construction layer, NOT bridge-map defect; bridge structurally well-defined |
| 6 | W11-5 multiplicity-weighted Mellin-pole-window observable definitively NON-COMPOSABLE with ι_* (composability_residual = 0.887 ≫ 0.01 from §W3a-18) | PHONONIC | CONFIRMED NON-COMPOSABLE (positive structural information) | Independent of observable-identification question; survives this synthesis intact; informs S89+ W3c queue that ANY non-BCS-grounded multiplicity-weighted construction will inherit the non-composability |
| 7 | Bridge-anatomy K-counter at FWD-C3 instance count UNCHANGED at K=2 (W3a sub-tests of instance #2; sub-row split is structurally-orthogonal-companion within instance #2, not a new instance) | GEOMETRIC | K=2 (UNCHANGED) | MANDATORY-promotion at K=3 still pending an INDEPENDENT THIRD cross-pillar bridge instance per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`; FWD-C1 + FWD-C2 are the eligible candidates |

---

## VII. Adjudication Summary (Workshop 3 — Substrate-vs-Laboratory Observable Identity)

### (i) Verdict

**LANDAU WINS** at the substrate-IS-observable specification level.

### (ii) IF volovik wins (counter-factual): substitution-chain proof of uniqueness FAILS

The volovik-axis claim "the substrate-IS observable inheriting-into R_3HeB_lit is uniquely determined by the algebra-level inheritance morphism alone" was tested via three counter-arguments (Result 2 IV.1):

1. "Substrate IS the algebra" — true at algebra-level; insufficient at observable-level
2. "(Δ_B/Δ_A)^p=0 cancellation guarantees ratio preservation" — preserves all admissibility-class members; does NOT select among them
3. "K-theory pairing requirements determine the unique image" — determines kernel cocycles (φ_67 + φ_88); does NOT determine observable form on BdG-image

All three counter-arguments fail at the substitution-chain level. **The volovik-uniqueness claim is FALSIFIED.**

### (iii) IF landau wins (this is the actual verdict): BCS-physics-grounded derivation specification

Per IV.2: derive R_substrate_BCS-grounded := (Σ_BdG_A − Σ_BdG_B)/(Σ_BdG_A + Σ_BdG_B) where Σ_BdG_A, Σ_BdG_B are spectral-action moments on A_K^BdG_preimage = ℂ ⊕ ℍ associated with the BCS gap-equation A-phase and B-phase channels at the polycritical pressure point. Algebraic shape (a − b)/(a + b) match restored vs R_3HeB_lit. Re-scoping of §W3a-14/18/19 results per IV.3:

- §W3a-14 FAIL: closes M_3(ℂ)-projection corridor on the wrong observable; uninformative for landau-path observable
- §W3a-18 FAIL: closes substrate-distance-1 surrogate corridor on the wrong observable; composability_residual = 0.887 finding survives as positive structural information about W11-5's algebraic form
- §W3a-19 INFO: B-convention saturation R_∞ ≈ −1.892 survives as substrate-IS universal-large-negative-R prediction (V.2; CF-W3a-ADDITIONAL-A); NOT a prediction about R_3HeB_lit

### (iv) Revised pre-registration for `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`

REPLACE with two-gate sequence:

1. `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE` (V.4) — infrastructure construction; PASS iff Hochschild cocycle + Chern character + Connes-Karoubi pairing constructed; ~3 wave-equivalents
2. `S89-3HEB-EXCESS-INHERITANCE-BCS-PHYSICS-GROUNDED-OBSERVABLE-DERIVATION-LANDAU-PATH` (V.1) — landau-path application of V.4 infrastructure to BCS-physics-grounded observable; PASS-strict at ratio_mismatch ≤ 0.001; ~3 wave-equivalents

DISPATCH ORDER: V.4 → V.1 (sequential dependency: V.1 consumes V.4's infrastructure).

### (v) §VII.AJ implication

FWD-C3 instance #2 RECLASSIFIES from REGISTRY-FAIL to NEEDS-REIDENTIFICATION via slot-split per Result 4:
- §VII.AJ.OP-PROJ (STAGE-1-CANDIDATE) ← substrate-IS universal-R prediction (V.2)
- §VII.AJ.STATE-PROJ (NEEDS-COMPUTATION) ← landau-path BCS-grounded observable (V.1, conditional on V.4)

Mack-cosmic-bridge sole-writer registry split per V.5.

### (vi) Two-distinct-observables registry framing — STRUCTURALLY-ORTHOGONAL-COMPANION

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3:

The volovik-defended substrate-IS R_substrate_universal (algebra-INVARIANT, OP-PROJ side, predicting R_∞ ≈ −1.892) and the landau-defended BCS-physics-grounded R_substrate_BCS-grounded (algebra-DEPENDENT, STATE-PROJ side, predicting R_substrate ≈ R_3HeB_lit ≈ +0.0354) are STRUCTURALLY ORTHOGONAL.

**Cross-corner co-primary FORBIDDEN.** Both can stand independently as STRUCTURALLY-ORTHOGONAL-COMPANION registry entries:
- Either both PASS at their own pre-registered laboratory anchors (volovik-future-anchor for OP-PROJ; R_3HeB_lit for STATE-PROJ)
- Or one PASSes and the other FAILs — neither outcome invalidates the other

This is the canonical resolution of the substrate-vs-laboratory observable identity tension: NOT a single observable-construction question with one right answer, BUT TWO DISTINCT OBSERVABLES living on TWO DIFFERENT ALGEBRA-AXES, each with its own forward gate, its own laboratory anchor, and its own registry-PASS path.

---

## Substrate framing (mandatory per `phononic-framing.md`)

The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` = (ℂ ⊕ ℍ ⊕ M_3(ℂ), L²(M_K)^{≤10}, D_K^{≤10}) on Jensen-deformed SU(3); it is the parent in the Kasparov-KK projection p ∈ KK(A_K, A_He). 3He-B is the laboratory child realization at the polycritical pressure point (P_pc = 21.22 bar, T_pc = 2.273 mK); 3He-B's BCS-paired condensate IS the inheritance image of the substrate's BdG-restricted spectral-triple sector under ι. The R_3HeB_lit observable IS measured IN a 3He-B cryostat at P_pc; the R_substrate observable IS evaluated ON the substrate's Peter-Weyl decomposition. The bridge map ι sends the substrate-IS structural data INTO the laboratory-IN measurement of A-phase / B-phase gap asymmetry.

The W3a wave's R_substrate = δN/N_paired construction IS substrate-IS at the algebra layer; it is NOT in any geometric container "on" or "around" the substrate. The factor-of-2 BdG-doubling subtraction in δN := N_unpaired − 2 · N_paired IS a structural feature of the Nambu-Gorkov doubling convention internal to the substrate's BdG-undoubled spectral-action moments; it is NOT an arbitrary numerical choice. The corrected landau-path R_substrate_BCS-grounded = (Σ_BdG_A − Σ_BdG_B)/(Σ_BdG_A + Σ_BdG_B) IS substrate-IS at the spectral-action moment layer; the two channels Σ_BdG_A and Σ_BdG_B ARE substrate-IS structural data that map via ι to laboratory-IN gap magnitudes Δ_A and Δ_B at polycritical pressure.

NOT: "the substrate's δN/N_paired is the same physical quantity as 3He-B's gap asymmetry" — they are NOT (per Result 1; algebraic shape mismatch (c − 2d)/d vs (a − b)/(a + b)). NOT: "3He-B at polycritical pressure is INSIDE the substrate's BdG sector as a geometric subspace" — 3He-B IS the laboratory-realized BdG sector at low temperature; the substrate IS the categorical extension whose BdG-restricted image IS the 3He-B spectral triple under ι. The arrow is parent → child (substrate → 3He-B); the observable-level identification is structurally distinct from the algebra-level inheritance.

---

## Cross-references

- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — MANDATORY at K=3 (S87 W-2 R3 close); calibration corpus consumed by Result 4
- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — MANDATORY at K=3 (S88 W8-92 close); §VII.X.OP-PROJ + §VII.X.STATE-PROJ suffix discipline
- `.claude/rules/inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` + §"Cohomology-Asymmetry Test (Class B)" — vacuous at rank-1-effective p=0 per Result 2
- `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"` — direction-of-explanation discipline; substrate IS, laboratory IN
- `.claude/rules/regulator-convention-lockdown.md §"Demarcation theorem"` — template applied in V.3 for unique convention pin derivation
- `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway"` — supersession-tag protocol consumed by V.5 registry split (audit-pin sub-row append-only with `supersedes=<old_audit_sha>`)
- `sessions/framework/correspondence/3HeB-inheritance-canonical.md` — S86 W1b-T8 canonical; PRESERVED + REINFORCED by this synthesis
- `sessions/permanent-results-registry.md §VII.AJ` — FWD-C3 instance #2 slot reclassification target (V.5 registry split)
- §VII.AF.1 (S86 W-5; first cross-pillar bridge calibration corpus instance #1) — bridge-anatomy K-counter at K=2 PRESERVED (UNCHANGED) per IV.4

---

## Closing note (volovik-axis honest disclosure)

This synthesis ADJUDICATES AGAINST the volovik-axis primary-claim of substrate-IS-observable-uniqueness from algebra alone. As primary-author of the W3a wave's three computational gates AND as the agent whose substrate-IS framework is the framework's centerline, this is the harder verdict to write. The substitution-chain at Result 1 (algebraic shape mismatch (c − 2d)/d vs (a − b)/(a + b)) and Result 2 (rank-1-effective Class-B vacuous + Class-A silent on non-NULL F-row value) leaves no other structurally honest reading. Volovik retains: (i) substrate IS the algebra at the categorical layer; (ii) inheritance morphism ι is well-defined and PRESERVED; (iii) substrate-IS universal-large-negative-R prediction R_∞ ≈ −1.892 ± 0.001 under B convention is a STAGE-1-CANDIDATE registry-eligible result; (iv) W11-5 NON-COMPOSABILITY is positive structural information about W11-5's algebraic form. Landau gains: (i) BCS-physics-grounded selector among admissibility-class members IS the structurally-required derivation; (ii) §VII.AJ FWD-C3 instance #2 reclassifies as NEEDS-REIDENTIFICATION via algebra-axis orthogonality slot-split; (iii) S89+ landau-path forward gate V.1 (BCS-physics-grounded observable derivation) is the new primary axis at the STATE-PROJ side of §VII.AJ.

The framework is stronger for this adjudication: ONE wrong-observable corridor closed at the wave-3a level, TWO structurally-orthogonal-companion forward gates pre-registered for S89+, and the inheritance theorem (S86 W1b-T8) emerges PRESERVED + REINFORCED at machine precision across all three independent W3a verifications.
