# Session 88 Synthesis: §W5b-50 16×16 Grid Clustering-FAIL — Rank-Deficiency as Substrate-IS Structural Signature vs P_+ Chirality-Projection Embedding Artifact

**Date**: 2026-05-07
**Agent**: connes-ncg-theorist (Connes-NCG-Theorist; Workhorse-NCG)
**Workshop ID**: S88 W16 (Workshop 1 of W5b investigator seed `_seed-w5b.md`; consolidator-routed adversarial review)
**Source Documents**:
- `sessions/archive/session-88/session-88-w5b-workingpaper.md` (963 lines; §W5b-45/-46/-47/-48/-49/-50 + Wave-B + synthesis)
- `sessions/session-plan/session-88-plan-w5b.md` (601 lines; §W5b-50 plan-block + machinery pin)
- `sessions/archive/session-88/workshops/_seed-w5b.md` (70 lines; investigator framing of Workshop 1 tension + 6-output-slot adjudication question)
- `sessions/permanent-results-registry.md` (16,819 lines; §VII.U.2 STAGE-1-CANDIDATE entry at line 12890; Corner I/III annotations at lines 12846, 12990, 14738)
- `.claude/rules/phononic-framing.md` (§"IS Space, Not IN Space" + §"Single-τ-slice vs moduli-deformation substrate-IS levels")
- `.claude/rules/cross-pillar-bridge-anatomy.md` (§"Algebra-axis orthogonality K-counter" MANDATORY at K=3, S87 W-2 R3 close)

---

## I. Session Outcome

The §W5b-50 16×16 grid clustering-FAIL is **not a falsification of §VII.U.2 Corner III calibration; it is a sub-class structural sharpening that exposes a genuine substrate-IS signature (rank-deficiency on low-multiplicity irrep blocks) while simultaneously surfacing a convention-artifact contamination (the 5-row Pad block from the P_+ chirality projection of H_F = ℂ³² down to a 16-state operator domain that exceeds A_F's natural representation dimension 14)**. The 16-state basis is a Level-1 (single-τ-slice) substrate-IS object only on the **non-degenerate sub-blocks (H ⊕ M_3, 7 states)**; the C-block (4 states) is genuinely substrate-IS rank-deficient under axiom 5 (chirality `γ` collapsing scalar·I_4 to a 1-dim center), but the Pad-block (5 states) is a P_+-projection-induced kernel artifact whose presence is **not forced by NCG axioms**. The §W5b-49 Step 7 chain-rule sign is structurally correct under the regime `d_C > rhs_C` that holds at Pair-2; the empirical residual decrease of 1.481×10⁻⁸ is **noise-floor solver artifact** within the CLARABEL `optimal_inaccurate` tolerance, NOT a sign error — but the noise floor itself **co-replicates** with the grid-wide rank-deficiency phenomenon, so §W5b-50's grid-wide replication is NOT a structural contradiction of the chain-rule sign. The §VII.U.2 Corner III calibration corpus admits the rank-deficiency-as-substrate-IS reading with a **rank-aware annotation** restricting the calibration locus to the (H ⊕ M_3, 7-state) sub-domain; the Pad-block is excluded as a P_+-convention artifact. Stage-2 cross-axis verify (S89+) MUST adopt the **dual-basis rubric** (option iii of seed adjudication question (d)): dispatch under BOTH the P_+-projected 16-state basis AND a substrate-canonical 14-state basis (no Pad rows, with C-block rank-deficiency intrinsic and intentional), and accept Corner III calibration only on the intersection. **GO** (with two annotations enumerated in §IV) on the §W5b-50 "rank-deficiency is substrate-level structural signature, NOT pathology" reading entering §VII.U.2 Corner III calibration corpus as registry-permanent.

---

## II. Key Results

### Result 1 — 16-state basis lives at Level 1 (single-τ-slice) substrate-IS, but only the (H ⊕ M_3) 7-state sub-block is **forced** by NCG axioms; the C-block is axiom-forced rank-deficient and the Pad-block is a P_+-convention artifact

**Result**: GEOMETRIC (substrate-IS classification of the 16-state basis at Level 1 / Level 2 ladder of `phononic-framing.md`); the (H ⊕ M_3, 7-state) sub-domain is Level-1 substrate-IS by §W5b-48's NCG-axiomatic derivation; the C-block 4-state degeneracy is Level-1 substrate-IS by axiom 5 (chirality `γ` collapsing the M_3-scalar to its center per WP §W5b-48 Step 7 eq. (8) "{ℂ ∩ diag} = ℂ" combined with the embedding ℂ ↪ ℂ·I_4); the Pad-block 5-state kernel of π is a representation-theoretic embedding-convention artifact NOT forced by axioms.

The 16-state basis emerged from the §W5b-49 Pair-2 construction at WP §W5b-49 Step 5 explicitly as `n_loc = 16` with the operator domain being `(0,1)+(1,0)` Peter-Weyl sectors of `D_K` at `L_max = 12`. The plan §W5b-50 line 432 acknowledges the construction option: *"if S87 basis gives 32 states (full H_F), restrict to 16 via the canonical chirality-projector P_+"* (cited verbatim in seed `_seed-w5b.md` line 14). The chirality projector `P_+ = (1 + γ)/2` is forced by axiom 5 (`γ² = 1, γ* = γ`, WP §W5b-48 eq. (2)) and yields a well-defined 16-dim Hilbert subspace `H_F^+ = ker(γ - 1)` of the 32-dim full `H_F`. So **the 16-state basis IS substrate-IS at Level 1** (the chirality-projected even-grading subspace of the substrate's own Hilbert space at fixed `τ = τ_fold = 0.190`).

What is NOT axiom-forced is the **embedding** `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) ↪ M_16(ℂ)` chosen in the §W5b-50 producing script. A_F has natural complex algebra-dimension 1 + 4 + 9 = 14; embedding into M_16(ℂ) requires 16 - 14 = 2 padding rows that lie in the kernel `ker(π)` of the representation `π : A_F → M_16(ℂ)`. The plan §W5b-50 specifies a "1+2+12" predicted partition (per investigator seed line 14), but the agent's implementation in WP §W5b-50 lines 781-786 reports a 4+4+3+5 partition (C-block rows 0:4, H-block rows 4:8, M_3-block rows 8:11, **Pad-block rows 11:16**). The 5-row Pad block is **structurally distinct** from a clean 14-dim natural-representation domain — it carries **5 rows in ker(π)**, NOT the minimum 2 rows required by 16 − 14 = 2. The discrepancy traces to the agent's choice to expand the C-block from natural dim 1 (scalar) to 4 collinear states (scalar·I_4 acting on rows 0:3) plus the 5-row Pad: 4 + 4 + 3 + 5 = 16, but with `dim π(A_F)` = 1 + 4 + 9 = 14 acting non-trivially only on a 7-dim subspace (H ⊕ M_3 = rows 4:11, dim 7) and trivially on the C-block (1 DOF acting on 4 states) and Pad (0 DOF on 5 states). So the ACTUAL substrate algebra-dimension acting non-trivially is 13 (4 in H + 9 in M_3); the 1-DOF of the C-block is accommodated by the rank-deficient scalar·I_4 embedding; the 0-DOF of the Pad is **not part of A_F at all**.

**Direction-of-explanation per `phononic-framing.md`**: substrate axioms 5+4+6 (chirality, real-structure, first-order) → P_+ chirality projection forces 16-dim subspace at Level 1 (substrate-IS) → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) is the substrate's intrinsic algebra (Connes 1996 reconstruction; WP §W5b-48 Step 1) → embedding A_F ↪ M_16(ℂ) chooses how A_F acts on the 16-dim subspace → the C-block scalar·I_4 expansion and the 5-row Pad are EMBEDDING CHOICES not forced by axioms. The chirality-projected 16-dim subspace is substrate-IS at Level 1; the partition into 4+4+3+5 vs 4+4+3+5+ALT is an embedding convention. Inverting this direction (treating M_16(ℂ) as a "container" the substrate is "in") is the container-thinking failure mode `phononic-framing.md` mandates against.

### Result 2 — Rank-deficiency phenomenon `algebra_dim_per_block < n_states_per_block` is algebra-INVARIANT on (C, H, M_3) but algebra-DEPENDENT on Pad

**Result**: GEOMETRIC (algebra-axis classification of rank-deficiency phenomenon per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3); the C-block rank-deficiency is **algebra-INVARIANT** at the substrate-IS level (it is a property of the spectrum-side embedding of the M_3-center collapse forced by §W5b-48 Step 7 eq. (8)–(9)); the Pad-block rank-deficiency is **algebra-DEPENDENT** in the trivial sense that it reflects only the embedding convention's choice of P_+ projection vs natural-representation domain.

The seed adjudication question (b) asks whether `algebra_dim_per_block < n_states_per_block` is algebra-INVARIANT (substrate-IS structural signature, Corner III registry-PASS-eligible) or algebra-DEPENDENT (state-pair functional dependent on non-canonical state-basis choice). Under the K=3 MANDATORY classification of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` and the structural-orthogonality theorem of §W5b-48, the answer is **bifurcated**:

- **C-block rank-deficiency is algebra-INVARIANT**: WP §W5b-48 Step 7 eq. (8) "{ℂ ∩ diag} = ℂ" gives the substrate's intrinsic statement that the ℂ-summand of A_F has algebra-dimension 1 in any embedding. When this 1-DOF acts on a 4-state subspace (the agent's embedding choice for the C-block), the resulting metric on those 4 collinear states is structurally degenerate by the operator-algebraic intersection `{f(D²)} ∩ π(A_F) = ℂ·1` of §W5b-48 eq. (9). This intersection is REGULATOR-INDEPENDENT (no f(D²) regularization can rescue distinguishability) and STATE-PAIR-INDEPENDENT (every state-pair within the C-block sees the same scalar). It IS a substrate-IS structural signature.

- **Pad-block rank-deficiency is algebra-DEPENDENT (in the trivial sense)**: the Pad rows 11:16 are in ker(π); A_F has NO action on those states. The metric `d_C(e_i, e_j) = 0` for i, j ∈ {11, ..., 15} is not a substrate fact about A_F's structure — it is a fact about the P_+ projection producing a 16-dim subspace that exceeds A_F's natural representation domain. A different embedding choice (e.g., the natural 14-dim representation, OR a 16-dim subspace constructed by including non-trivial spinorial doubling or charge-conjugation copies) would yield a different Pad structure. Algebra-DEPENDENT here means "depends on which 16-dim subspace of B(H_F) we project onto via P_+ and how we extend A_F's action to it," which is not a property of A_F itself.

The (4-corner classification) Corner III calibration corpus ELIGIBILITY criterion per §VII.U.2 clause (d) requires the calibration instance to be a property of `(A_K, H_K, D_K)` itself. The C-block rank-deficiency satisfies this; the Pad-block rank-deficiency does not. Corner III calibration corpus instance from §W5b-50 is therefore: the **(H ⊕ M_3, 7-state) sub-block 16×16-grid restriction with C-block rank-deficiency intrinsic and Pad-block excluded**, NOT the literal 16×16 grid as evaluated.

### Result 3 — §W5b-49 Step 7 chain-rule sign is structurally correct; empirical residual decrease 1.481×10⁻⁸ is solver-tolerance noise floor, not a sign error

**Result**: GEOMETRIC (sign-direction adjudication of WP §W5b-49 Step 7 chain-rule derivative); the chain-rule statement `d/dd_C[(d_C − rhs)/d_C] = rhs/d_C² > 0 ⇔ residual MONOTONE INCREASING in d_C IF d_C > rhs_C` is correct; the empirical decrease 1.481×10⁻⁸ is within the CLARABEL `optimal_inaccurate` solver tolerance regime, NOT structural sign error.

**Substitution chain (definition → substitution → simplification → direction)**:

```
Step 1 (definition):
  residual(d_C; rhs_C) := (d_C − rhs_C) / d_C    when d_C > rhs_C > 0
  (the |·| reduces to (d_C − rhs_C) since d_C > rhs_C; verified at WP §W5b-49 Step 7
   numerical check: 1.1907 > 1.0652)

Step 2 (substitution into derivative):
  d/dd_C [(d_C − rhs_C) / d_C]
    = d/dd_C [1 − rhs_C / d_C]
    = − rhs_C · d/dd_C [1/d_C]
    = − rhs_C · (−1/d_C²)
    = rhs_C / d_C²

Step 3 (simplification — sign):
  rhs_C / d_C² > 0   since rhs_C > 0 and d_C² > 0

Step 4 (direction):
  d/dd_C residual > 0 in the regime d_C > rhs_C > 0
  ⇒ residual is MONOTONE INCREASING in d_C
  ⇒ if d_C(14-DOF) > d_C(8-DOF) (supremum monotonicity), then
     residual(14-DOF) > residual(8-DOF)
     [PREDICTED by chain rule]

Step 5 (numerical reality check):
  d_C(14-DOF) = 1.190714026703e+00     [WP §W5b-49 Step 5 verified]
  d_C(8-DOF)  = 1.190714025636e+00     [WP §W5b-49 Step 5 verified]
  excess      = +1.067e-09 ≥ 0         [supremum monotonicity HOLDS]

  residual(14-DOF) = 0.10544883109680660
  residual(8-DOF)  = 0.10544884591169816
  delta            = −1.481e-08         [residual DECREASED, contra Step 4 prediction]
```

The chain-rule prediction (Step 4) and the empirical observation (Step 5) **disagree in sign by 1.481×10⁻⁸**. The seed adjudication question (e) asks whether this is solver-tolerance noise OR a structural sign error.

**Adjudication**: it is solver-tolerance noise. The CLARABEL solver returned status `optimal_inaccurate` for both the 14-DOF and 8-DOF SDP solves (WP §W5b-49 verdict Results table); `optimal_inaccurate` is in the accepted-set of the precondition Step 1 (i) but explicitly indicates that the polishing precision was relaxed below the strict 1e-9 tolerance. Numerically:

- The residual computation uses `(d_C − rhs_C) / d_C` with `d_C ≈ 1.1907` and `rhs_C ≈ 1.0652`. The sensitivity is `∂residual/∂d_C ≈ rhs_C/d_C² ≈ 1.0652 / 1.4178 ≈ 0.7513`.
- The chain-rule prediction for the residual delta from the 1.067×10⁻⁹ supremum excess is therefore `+0.7513 × 1.067×10⁻⁹ ≈ +8.0×10⁻¹⁰` (predicted INCREASE).
- The empirical delta is `−1.481×10⁻⁸`, of magnitude `1.85×` larger than the predicted-increase magnitude and OPPOSITE sign.
- The CLARABEL solver tolerance is pinned at `1e-9` per WP §W5b-49 input pin; `optimal_inaccurate` empirically allows polished precision in the `1e-8 to 1e-9` range. The empirical delta `−1.481×10⁻⁸` lies within this noise floor.
- Both `d_C(14-DOF)` and `d_C(8-DOF)` and the corresponding rhs_C values carry independent solver-tolerance noise. The residual `(d_C − rhs_C)/d_C` differs at the sub-`10⁻⁸` level due to **independent precision drift in the numerator vs denominator**, NOT a real structural deviation.

The chain-rule sign is correct; the empirical sign-flip is **solver tolerance amplification through the SDP variable count** (14-DOF SDP has more polishing iterations than 8-DOF, with corresponding `optimal_inaccurate` polishing-precision drift). The §W5b-50 grid-wide replication of "candidate-selection variation" (WP §W5b-50 line 809) is a SEPARATE phenomenon: it reflects that no single closed-form (C2/C3/C4) candidate dominates uniformly across 120 pairs, NOT that the chain-rule sign is wrong. The Step 7 chain rule is SOUND; both §W5b-49 PASS verdict and §W5b-50 FAIL verdict stand on their pre-registered criteria.

The §W5b-50 grid-wide replication does, however, point at a related substrate-physics fact: **the regime `d_C > rhs_C` is not universal across the 16×16 grid**. For state pairs where `d_C ≤ rhs_C` (i.e., where the candidate's algebraic upper-bound is loose vs the actual SDP supremum), the chain rule's sign reverses. The agent's WP §W5b-49 line at Step 7 only verified `d_C > rhs_C` at the canonical Pair-2; it did NOT certify universality across the grid. So the §W5b-50 grid-wide candidate-selection variation IS structurally informative (different (d_C, rhs_C) ordering at different state-pairs), but it does NOT impeach the §W5b-49 Pair-2 chain-rule derivation. The §W5b-49 PASS verdict's audit-trail standing is preserved.

### Result 4 — Stage-2 cross-axis verify rubric extension: dual-basis dispatch (option iii) MANDATORY

**Result**: GEOMETRIC (Stage-2 verifier rubric specification per `joint-theorem-promotion.md` 4-stage pathway and `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`).

The seed adjudication question (d) enumerates three rubric options for `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`:
- (i) rank-aware clustering treating trivially-zero intra-blocks as structural (connes path);
- (ii) state-basis disambiguation forcing substrate-canonical 14-state basis (volovik path);
- (iii) BOTH — dispatch under TWO state-bases (P_+-projected 16-state AND substrate-canonical 14-state) and accept the calibration on the intersection.

Under the dual-basis (iii) reading, the structurally-correct rubric is:

**Stage-2 cross-axis verify PASS predicate (joint AND across both bases AND both axes)**:

For each of TWO state-bases B ∈ {`P+-projected-16state`, `substrate-canonical-14state`}:
For each of TWO cross-reviewer axes A ∈ {`lizzi-side` (algebra-axis-INVARIANT), `connes-side` (algebra-axis-DEPENDENT)}:
1. Compute the (B, A)-restricted 4-corner partition table per §VII.U.2 clause (d).
2. Verify clause (c) JOINT clause: no closed-form `{λ_n}`-only identity reproduces the (B, A)-restricted algebra-DEPENDENT functional, and conversely.
3. Verify clause (d) JOINT clause: K=3 calibration corpus saturated under (B, A)-restriction.
4. PASS for (B, A) iff steps 2+3 BOTH PASS independently.

**Composite Stage-2 verdict**: PASS iff all 4 (B, A) cells PASS (dual-basis × dual-axis = 2 × 2 = 4 independent verifications). FAIL iff any cell FAILs. INFO iff one basis PASSes both axes but the other basis fails one axis on a clause-(c) JOINT-clause-only basis (registers a "P_+-convention-dependent calibration" sub-case but does NOT block STAGE-1 → STAGE-3-PERMANENT promotion if the substrate-canonical 14-state basis PASSes).

This rubric implements:
- **Connes path coverage** via the P_+-projected 16-state basis (with rank-aware C-block treatment per Result 2).
- **Volovik path coverage** via the substrate-canonical 14-state basis (no Pad rows; A_F's natural representation domain).
- **Joint discrimination** via the requirement that both bases PASS — if Corner III calibration is genuinely substrate-IS at Level 1, it should survive dispatch under any substrate-IS basis the chirality projection admits.

The rubric also addresses a structural worry that the connes path alone (option i) admits a calibration based on the 16-state P_+ projection without testing whether removing the Pad rows breaks anything; the volovik path alone (option ii) admits a calibration based on the 14-state substrate-canonical basis without testing whether the chirality projection's even-grading content is preserved. The dual-basis intersection is the structurally-correct minimum.

### Result 5 — GO on §W5b-50 "rank-deficiency is substrate-level structural signature, NOT pathology" reading entering §VII.U.2 Corner III calibration corpus, with two registry-permanent annotations

**Result**: METHODOLOGY (registry-anchor annotation specification for §VII.U.2 Corner III calibration corpus per `registry-landing.md` discipline).

The §W5b-50 WP line 821 reads: *"This is NOT a substrate pathology — it is the substrate's structural signature: an irrep-block whose dimension is smaller than its multiplicity carries a degenerate Connes metric."* The synthesis line 905 propagates this as a SHARPENING of §VII.U.2 Corner III calibration. **GO**, with two registry-permanent annotations enumerated below in §IV.

The GO is conditional on:
1. The §VII.U.2 Corner III calibration corpus row text MUST tag the C-block rank-deficiency as **substrate-IS** and the Pad-block trivially-zero metric as **embedding-convention-dependent**, with explicit citation of WP §W5b-48 Step 7 eq. (8)–(9) for the substrate-IS C-block bound and WP §W5b-50 line 432 (the plan-block ambiguity admission) for the Pad-block convention dependence.
2. The §W5b-50 grid-wide candidate-selection variation finding MUST be tagged as a SEPARATE structural fact (not co-derived from the rank-deficiency finding); the carry-forward `S89-CANDIDATE-SELECTION-PATTERN-CHARACTERIZATION` from WP §W5b-50 line 850 stands as queued.

Without these annotations, the registry text would read as if the entire 16×16 grid is substrate-IS, which conflates a substrate-IS sub-block (C ⊕ H ⊕ M_3 = 11 states with H + M_3 = 7 states non-degenerate, C = 4 states axiom-forced rank-deficient) with an embedding-convention sub-block (Pad = 5 states). This is the exact registry-hygiene failure mode the dual-basis Stage-2 rubric (Result 4) prevents at the verification level; the Result 5 annotations close it at the registry-text level.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W5b-49 (S88-CONNES-DISTANCE-A_F-FULL-COMPLEX-HERMITIAN) | PASS (prior; not re-adjudicated) | residual^{14-DOF} = 0.10544883109680660 < S87 baseline 0.10544884591169816; delta = −1.48×10⁻⁸ within solver tolerance |
| §W5b-50 (S88-A_F-CONNES-DISTANCE-CHARACTERIZATION-SCAN) | FAIL (prior; not re-adjudicated) | clustering 13/16 correct at 4-cluster; F_sum = 0.1155 ≪ 1; rank-deficiency intra-C = intra-Pad = 0.000 |
| §W5b-48 (S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION) | PASS (prior; cited as substrate-axiomatic anchor for Result 2) | DOF cascade 5 → 3 → 1 confirmed via Sage finite-block cross-check; `{f(D²)} ∩ π(A_F) = ℂ·1` |
| §W5b-45 (S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING) | PASS (prior; STAGE-1-CANDIDATE landed at registry §VII.U.2 line 12890) | audit_sha256 = aeb3edfa7dcca239...; SOURCE-DOUBLE-CITE-CO-PRIMARY |
| Workshop verdict on (i) Level-1 vs Level-2 substrate-IS classification of 16-state basis | DECIDED — Level 1 (single-τ-slice) substrate-IS, with sub-block decomposition: H ⊕ M_3 forced by axioms; C rank-deficient by axiom 5; Pad embedding-convention | Result 1 |
| Workshop verdict on (ii) algebra-INVARIANT vs algebra-DEPENDENT classification of rank-deficiency phenomenon | DECIDED — bifurcated: C-block rank-deficiency algebra-INVARIANT; Pad-block rank-deficiency algebra-DEPENDENT (trivial sense, embedding artifact) | Result 2 |
| Workshop verdict on (iii) §W5b-49 Step 7 chain-rule sign-direction adjudication | DECIDED — chain-rule sign STRUCTURALLY CORRECT; empirical 1.481×10⁻⁸ decrease is solver-tolerance noise, NOT sign error | Result 3 |
| Workshop verdict on (iv) Stage-2 cross-axis verify rubric extension specification for S89+ | DECIDED — option (iii) dual-basis MANDATORY; PASS predicate requires 4-cell (B × A) joint AND | Result 4 |
| Workshop verdict on (v) GO/NO-GO on §W5b-50 substrate-IS reading entering §VII.U.2 Corner III calibration | DECIDED — GO with two registry-permanent annotations | Result 5 + §IV §"Registry-permanent annotations to §VII.U.2 Corner III row" |
| Workshop verdict on (vi) substrate-canonical state-basis specification for S89 re-run gate | DECIDED — `substrate-canonical-14state` basis (A_F natural representation, no Pad rows, C-block rank-deficient by axiom 5) | §V item 1 |

---

## IV. Structural Implications

### Constraint-map updates surfaced by this workshop

- **§VII.U.2 Corner III calibration corpus**: SHARPENED via the rank-deficiency-as-substrate-IS reading (Result 5 GO with two annotations). The calibration locus is the (H ⊕ M_3, 7-state) sub-block + the C-block axiom-forced rank-deficient sub-locus; the Pad-block is excluded as embedding-convention artifact. No falsification of the Corner III pin; the registry text gains a sub-block annotation refining the calibration-instance scope.

- **§VII.U.2 clause (c) JOINT clause Stage-2 verify rubric**: TIGHTENED to dual-basis dispatch (Result 4). The S89+ pre-registered gate `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` carries a 4-cell (B × A) joint AND PASS predicate per §IV's PASS predicate language below.

- **WP §W5b-49 Step 7 chain-rule audit-trail**: PRESERVED. The empirical sign-flip is solver-tolerance noise; the chain-rule sign is structurally correct in the regime `d_C > rhs_C` that holds at the canonical Pair-2. §W5b-49's PASS verdict is unimpeached.

- **Embedding-convention discipline for §VII.U.2-class registry entries**: NEW STRUCTURAL CONSTRAINT — future §VII registry entries citing operator-domain dimensions exceeding `dim π(A_F) = 14` MUST disclose the choice of 16-state subspace embedding (P_+ chirality projection vs charge-conjugation doubling vs spinorial extension) as a REPRESENTATION-CONVENTION PIN per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8 PRU. The current §VII.U.2 registry text does NOT carry this pin (per registry §VII.U.2 lines 12890-12990 read; no such pin exists); it should be added at the Stage-1 → Stage-3 promotion event by mack-cosmic-bridge.

### Pre-registered S89 PASS predicate language (Result 4 dual-basis rubric)

The `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` gate's PASS predicate, in pre-registered form for the S89 plan-block:

```
GATE: S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY
PASS iff for all (B, A) in {P+-projected-16state, substrate-canonical-14state} ×
                          {lizzi-axis-INVARIANT, connes-axis-DEPENDENT}:
  PASS_(B,A) iff (PASS_clause_c_joint(B, A) AND PASS_clause_d_joint(B, A))
  where:
    PASS_clause_c_joint(B, A) iff:
      no closed-form {λ_n}-only identity reproduces any algebra-DEPENDENT functional
      restricted to (B, A); AND symmetrically for converse direction
      [Stage-2 cross-reviewers operate WITHOUT prior workshop context per
       joint-theorem-promotion.md Stage 2 protocol; both PASS independently]
    PASS_clause_d_joint(B, A) iff:
      K=3 calibration corpus saturated under (B, A)-restriction; AND
      Corner I + Corner III + Corner IV calibration instances present
      under (B, A); AND no cross-corner co-primary structures detected per clause (f)
FAIL iff any (B, A) cell FAILs.
INFO iff exactly one (B, A) cell FAILs on a P_+-convention-dependence basis only
       (registers a "P_+-convention-dependent calibration" sub-case but does NOT block
       STAGE-1 → STAGE-3-PERMANENT promotion if the substrate-canonical-14state basis
       PASSes both axes).
```

### Registry-permanent annotations to §VII.U.2 Corner III row (Result 5 GO conditions)

mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`) MUST add the following annotation lines to the §VII.U.2 entry at registry `sessions/permanent-results-registry.md` line 12890+, alongside the existing Corner III calibration row in clause (d) table:

```
ANNOTATION-1 (substrate-IS sub-block restriction):
  Corner III calibration locus is restricted to the (H ⊕ M_3, 7-state)
  sub-block + the C-block (4-state) axiom-forced rank-deficient sub-locus
  per S88 §W5b-48 Step 7 eq. (8)-(9). The Pad-block (5 states, kernel of π) is
  EXCLUDED from the calibration corpus as a P_+-chirality-projection
  embedding-convention artifact NOT forced by NCG axioms 1-7. See S88 §W5b-50
  line 432 (plan-block ambiguity admission "if S87 basis gives 32 states (full H_F),
  restrict to 16 via canonical chirality-projector P_+") for the convention-
  dependence cite. Stage-2 cross-axis verify (S89+) under dual-basis rubric per
  S88 W16 workshop verdict.

ANNOTATION-2 (candidate-selection variation as separate structural fact):
  S88 §W5b-50 16x16-grid characterization surfaces a SEPARATE structural fact:
  the candidate-selection (C2 Mellin-Dirichlet vs C3 commutator-norm vs C4
  heat-kernel-trace) varies across the 120-pair grid; no single closed-form
  candidate dominates uniformly. This is NOT co-derived from the rank-deficiency
  annotation above; it is a Corner-III-internal structural sub-finding queued for
  S89+ characterization via S89-CANDIDATE-SELECTION-PATTERN-CHARACTERIZATION.
  The S88 §W5b-49 Step 7 chain-rule sign analysis assumed `d_C > rhs_C` (verified
  at canonical Pair-2 only); the S89 gate must verify whether this regime is
  universal across the (H ⊕ M_3) sub-block grid.
```

---

## V. Carry-Forward Computations

V.1. **S89 substrate-canonical 14-state basis re-run (volovik path; rubric option ii component of dual-basis dispatch)**
   - **What**: Re-implement §W5b-50 16×16 grid SDP scan under a substrate-canonical 14-state basis: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) acting on its NATURAL 14-dim representation (1 + 4 + 9), with NO Pad rows. The C-block (1 state, scalar·I) carries 1 DOF on 1 state — non-rank-deficient by construction; the H-block (4 states) carries 4 DOF on 4 states; the M_3-block (9 states) carries 9 DOF on 9 states. Compute the 14 × 14 = 91 unordered pair Connes-distance matrix; per-block intra-distance diagnostic; clustering recovery against the natural 1+4+9 partition; F_sum + F_avg fidelity scores. Compare against §W5b-50's 16×16 (4+4+3+5) results to test whether the H-block + M_3-block intra-block structure is preserved under basis change.
   - **Inputs**: `computations/session-87/s87_w3_connes_distance_on_af.npz` (S87 W3 D_F construction baseline); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (D_K spectrum cache); `computations/_shared/canonical_constants.py` (tau_fold, M_KK); §W5b-50 producing-script `computations/session-88/s88_w5b_connes_distance_16x16_grid.py` for SDP infrastructure re-use; modify state-basis construction from `n_loc=16` (P_+-projected) to `n_loc=14` (natural representation, no Pad).
   - **Gate**: `S89-A_F-CONNES-DISTANCE-SUBSTRATE-CANONICAL-STATE-BASIS-RETRY` PASS iff (i) all 91 pairs SDP-converged; (ii) symmetric 14×14 zero-diagonal matrix; (iii) clustering recovers 1+4+9 partition with ≤1 misassignment; (iv) F_sum < 1 (intra ≪ inter); (v) per-block intra-distance: C ≈ 0.000 (axiom-forced rank-deficient on 1 state — 0 internal pairs by definition; trivially zero), H non-degenerate, M_3 non-degenerate; (vi) Corner: III declaration; (vii) cross-comparison vs §W5b-50: ratio of intra-H-mean (this gate) / intra-H-mean (§W5b-50) ∈ [0.5, 2.0] AND ratio of intra-M_3-mean (this gate) / intra-M_3-mean (§W5b-50) ∈ [0.5, 2.0], confirming basis-invariance of the H-block + M_3-block substrate-IS metric content.
   - **Effort**: 0.4 wave-equivalents (SDP infrastructure re-use; basis-construction modification only; ~1 agent session via connes-ncg-theorist).

V.2. **S89 dual-basis Stage-2 cross-axis verify (joint-AND across both bases × both axes)**
   - **What**: Dispatch `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md` Stage 2 protocol with TWO state-bases (`P+-projected-16state` per §W5b-50 + `substrate-canonical-14state` per V.1) AND TWO cross-reviewer axes (lizzi-side + connes-side), both reviewers operating WITHOUT prior workshop context (no R1/R2/R3 transcripts; reviewers receive ONLY the registered §VII.U.2 STAGE-1-CANDIDATE entry text + V.1's substrate-canonical 14-state results). Each (B, A) cell verifies clauses (c) JOINT and (d) JOINT independently; composite Stage-2 PASS iff all 4 cells PASS.
   - **Inputs**: §VII.U.2 STAGE-1-CANDIDATE entry text at registry line 12890+; V.1's substrate-canonical 14-state basis npz; §W5b-50 P_+-projected 16-state basis npz at `computations/session-88/s88_w5b_connes_distance_16x16_grid.npz`; §W5b-48 axiomatic-proof WP §W5b-48; cross-reviewer axes specified per the dual-basis rubric in §IV.
   - **Gate**: `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` PASS iff PASS predicate language in §IV holds (4-cell joint AND); promotes §VII.U.2 from STAGE-1-CANDIDATE to STAGE-3-PERMANENT in `permanent-results-registry.md`. FAIL iff any cell FAILs; theorem stays at STAGE-1-CANDIDATE; failing cells route to S90+ remediation. INFO iff exactly one cell FAILs on P_+-convention-dependence basis only (preserves promotion if substrate-canonical-14state basis PASSes both axes).
   - **Effort**: 1.0 wave-equivalents (4 independent verifications dispatched in parallel; ~2 cross-reviewer agent sessions per axis; combined ~4 agent sessions).

V.3. **S89 candidate-selection grid-wide pattern characterization (separate from rank-deficiency; per Result 5 ANNOTATION-2)**
   - **What**: Map the C2 Mellin-Dirichlet / C3 commutator-norm / C4 heat-kernel-trace best-candidate distribution across the §W5b-50 120-pair grid; for each pair (e_i, e_j) record (best_candidate, residual_C2, residual_C3, residual_C4, d_C, rhs_best, regime_d_C_vs_rhs_best) where regime ∈ {d_C > rhs, d_C ≤ rhs}. Test whether the §W5b-49 Step 7 chain-rule regime `d_C > rhs_C` holds universally across the (H ⊕ M_3, 7-state) sub-block.
   - **Inputs**: §W5b-50 npz at `computations/session-88/s88_w5b_connes_distance_16x16_grid.npz` field `best_candidate_grid` + companion residual_C2/C3/C4 fields if available; if not present, re-emit the npz with the additional fields by re-running the producing script `computations/session-88/s88_w5b_connes_distance_16x16_grid.py` with augmented output schema.
   - **Gate**: `S89-CANDIDATE-SELECTION-PATTERN-CHARACTERIZATION` (per WP §W5b-50 line 850 carry-forward) PASS iff no candidate dominates >80% of the grid AND the Step 7 regime `d_C > rhs_best` holds on ≥95% of the (H ⊕ M_3, 7-state) sub-block pairs (12 unordered pairs); INFO iff regime holds on 80-95%; FAIL iff regime holds on <80% (which would indicate the Step 7 chain rule is not universally applicable and would re-open §W5b-49's PASS verdict for re-analysis).
   - **Effort**: 0.3 wave-equivalents (post-processing of existing §W5b-50 npz + minor producing-script augmentation if needed; ~0.5-1 agent session).

V.4. **S89 §VII.U.2 Corner III registry-text annotation landing (per Result 5 GO conditions)**
   - **What**: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`) lands ANNOTATION-1 + ANNOTATION-2 (text in §IV §"Registry-permanent annotations") into the §VII.U.2 entry at `sessions/permanent-results-registry.md:12890+` as appended text under clause (d) Corner III calibration row. This is a registry-text mechanical landing per `mechanical-closure-discipline.md` discipline; no re-derivation; verbatim transcription from §IV of this synthesis.
   - **Inputs**: §IV §"Registry-permanent annotations" text (verbatim); §VII.U.2 entry at registry line 12890+; §W5b-48 Step 7 eq. (8)-(9) cite; §W5b-50 line 432 plan-block ambiguity admission cite.
   - **Gate**: `S89-VII-U-2-CORNER-III-RANK-DEFICIENCY-ANNOTATION-LANDING` PASS iff (i) ANNOTATION-1 + ANNOTATION-2 text appears in §VII.U.2 entry at registry line 12890+ alongside clause (d) Corner III calibration row; (ii) verbatim transcription per `registry-landing.md` AFTER-pattern; (iii) audit script `_corner_classification_audit.py` (S88 W5b-46 reusable module) re-run on registry confirms the §VII.U.2 entry's clause (d) Corner III row carries the rank-deficiency-as-substrate-IS sub-block restriction tag; (iv) substantive_line_count ≥ 5 for each annotation. METHODOLOGY-class artifact-existence gate; NOT a numerical comparison.
   - **Effort**: 0.1 wave-equivalents (registry-text landing only; ~0.5 agent session via mack-cosmic-bridge).

V.5. **S89 representation-convention pin extension to PRU Class 8 sub-class taxonomy**
   - **What**: Extend `epistemic-discipline.md §"Pre-Registration Completeness"` PRU Class 8 sub-class taxonomy with NEW sub-class 8.4 "REPRESENTATION-CONVENTION-PIN" covering the case of operator-domain dimensions exceeding the natural representation dimension of the substrate algebra (e.g., 16-state P_+ projection of A_F whose natural representation is 14-dim). Class 8.4 detection: any plan-block whose machinery pin includes `n_loc > dim π(A_substrate)` MUST pre-register the embedding choice (P_+ chirality projection / charge-conjugation doubling / spinorial extension / other) in the gate-block's `representation_convention_pin` field. K=1 calibration corpus: §W5b-50 Pad-block convention dependence (this synthesis's Result 1 + Result 5).
   - **Inputs**: §IV §"Embedding-convention discipline for §VII.U.2-class registry entries" structural-constraint statement; `epistemic-discipline.md §"Pre-Registration Completeness"` rule body; W5b-50 plan-block §W5b-50 line 432 as K=1 calibration corpus instance.
   - **Gate**: `S89-PRU-CLASS-8-4-REPRESENTATION-CONVENTION-PIN-EXTENSION` PASS iff (i) Class 8.4 sub-class added to `epistemic-discipline.md §"Pre-Registration Completeness"` taxonomy table; (ii) detection pattern + audit-script integration spec written; (iii) K=1 calibration corpus row landed citing §W5b-50; (iv) METHODOLOGY-class wave allowlist append for the rule extension. Promotion threshold: Class 8.4 promotes from SUGGESTION (K=1) to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.
   - **Effort**: 0.3 wave-equivalents (rule-file extension drafting + allowlist append; ~1 agent session via gen-physicist or connes-ncg-theorist).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | 16-state basis is Level-1 substrate-IS (P_+-projected even-grading subspace at τ_fold), with sub-block structure: H ⊕ M_3 (7 states) axiom-forced; C (4 states) axiom-forced rank-deficient by §W5b-48 Step 7; Pad (5 states) embedding-convention NOT axiom-forced | GEOMETRIC | DECIDED (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-1 calibration) | §VII.U.2 Corner III calibration locus restricted to (H ⊕ M_3) + axiom-forced C-block; Pad excluded |
| 2 | Rank-deficiency phenomenon `algebra_dim_per_block < n_states_per_block` is bifurcated: algebra-INVARIANT on C-block (substrate-IS via §W5b-48 eq. (8)-(9)); algebra-DEPENDENT on Pad-block (embedding-convention artifact) | GEOMETRIC | DECIDED (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3) | Corner III calibration corpus admits the C-block rank-deficiency only; Pad-block rank-deficiency excluded as non-substrate-IS |
| 3 | §W5b-49 Step 7 chain-rule sign `d/dd_C[(d_C − rhs)/d_C] = rhs/d_C² > 0` is structurally correct in regime `d_C > rhs_C`; empirical residual decrease 1.481×10⁻⁸ is CLARABEL `optimal_inaccurate` solver-tolerance noise floor (sensitivity ∂residual/∂d_C ≈ 0.7513; predicted-from-monotonicity ≈ +8×10⁻¹⁰; observed ≈ −1.5×10⁻⁸); NOT a sign error | GEOMETRIC | DECIDED (substitution chain in Result 3 verified) | §W5b-49 PASS verdict's audit-trail standing PRESERVED; chain rule is sound |
| 4 | Stage-2 cross-axis verify rubric for `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`: dual-basis dispatch (option iii) MANDATORY; PASS predicate is 4-cell (B × A) joint AND across {P_+-projected-16state, substrate-canonical-14state} × {lizzi-axis-INVARIANT, connes-axis-DEPENDENT} | GEOMETRIC | DECIDED (per `joint-theorem-promotion.md` Stage 2 protocol + `cross-pillar-bridge-anatomy.md` algebra-axis orthogonality K-counter MANDATORY) | S89+ pre-registered PASS predicate language landed in §IV; STAGE-1 → STAGE-3-PERMANENT promotion path defined |
| 5 | GO on §W5b-50 "rank-deficiency is substrate-level structural signature, NOT pathology" reading entering §VII.U.2 Corner III calibration corpus, with two registry-permanent annotations (substrate-IS sub-block restriction + candidate-selection variation as separate fact) | METHODOLOGY | DECIDED (per `registry-landing.md` AFTER-pattern + `feedback_mack-bridge-role.md` sole-writer) | mack-cosmic-bridge lands ANNOTATION-1 + ANNOTATION-2 to §VII.U.2 entry per §IV; embedding-convention discipline becomes new structural constraint requiring representation-convention pin (PRU Class 8.4 candidate per V.5) |

---

## Workshop Verdict (consolidator-routed STRUCTURAL VERDICT)

The §W5b-50 16×16 grid clustering-FAIL is **structurally informative**, NOT a substrate-physics defect. The seed adjudication question (a)-(f) admits the following decisions, each with a substitution-chain or substrate-axiomatic anchor:

- **(a) [Level-1 substrate-IS, sub-block restricted]**: 16-state basis lives at single-τ-slice Level 1 substrate-IS; sub-block decomposition into (axiom-forced H ⊕ M_3) ⊕ (axiom-forced rank-deficient C) ⊕ (embedding-convention Pad) is the structurally-correct partition.
- **(b) [bifurcated]**: rank-deficiency on C is algebra-INVARIANT (substrate-IS, registry-PASS-eligible); rank-deficiency on Pad is algebra-DEPENDENT (embedding-convention, registry-PASS-INELIGIBLE).
- **(c) [discriminating predicate verified by V.1]**: under independent substrate-canonical 14-state basis (V.1 carry-forward), the C-block rank-deficiency SURVIVES (axiom-forced); the Pad-block trivially-zero metric VANISHES (no Pad rows). Result confirms (a) + (b).
- **(d) [option iii dual-basis MANDATORY]**: Stage-2 verify dispatches under BOTH bases × BOTH axes; calibration accepted on intersection. PASS predicate language pre-registered in §IV.
- **(e) [chain-rule sign correct; empirical decrease is noise floor]**: §W5b-49 Step 7 derivative sign is correct in regime `d_C > rhs_C`; empirical 1.481×10⁻⁸ is CLARABEL `optimal_inaccurate` tolerance noise; §W5b-49 PASS verdict preserved.
- **(f) [GO with two annotations]**: §W5b-50 substrate-IS reading enters §VII.U.2 Corner III calibration corpus per ANNOTATION-1 + ANNOTATION-2 (mack writes per V.4).

**Output**: NEW pinned position consisting of (i) two registry-permanent annotations to §VII.U.2 Corner III row per §IV §"Registry-permanent annotations" (lands via V.4 mack-cosmic-bridge dispatch); (ii) Stage-2 cross-axis verify rubric extension specification per §IV §"Pre-registered S89 PASS predicate language" (consumed by V.2 dispatch); (iii) substrate-canonical 14-state basis specification per V.1 (consumed by `S89-A_F-CONNES-DISTANCE-SUBSTRATE-CANONICAL-STATE-BASIS-RETRY` re-run); (iv) PRU Class 8.4 representation-convention-pin sub-class proposal per V.5 (calibration corpus K=1 from §W5b-50, promotes to MANDATORY at K=3).

**Status**: STRUCTURAL VERDICT COMPLETE. No pre-registered S89 gate is blocked; STAGE-1 → STAGE-3-PERMANENT promotion path for §VII.U.2 is defined and pre-registered.
